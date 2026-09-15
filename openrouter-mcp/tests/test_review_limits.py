from __future__ import annotations

import asyncio
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

import httpx

from openrouter_mcp.bridge import TASK_PROFILES, _parser, check_context_budget, run_agent


class ReviewLimitsTest(unittest.TestCase):
    def test_defaults_and_scope_budgets(self):
        self.assertEqual(_parser('reviewer').parse_args(['review']).task_profile, 'review-section')
        self.assertEqual(_parser('writer').parse_args(['write']).task_profile, 'general')
        self.assertLess(TASK_PROFILES['review-change'].max_context_chars,
                        TASK_PROFILES['review-section'].max_context_chars)
        self.assertLess(TASK_PROFILES['review-section'].timeout_seconds,
                        TASK_PROFILES['review-full'].timeout_seconds)

    def test_context_counts_tool_results_without_truncating(self):
        messages = [{'role': 'tool', 'content': 'dữ kiện ' * 500}]
        before = messages[0]['content']
        with self.assertRaisesRegex(RuntimeError, 'split the task'):
            check_context_budget(messages, 100)
        self.assertEqual(messages[0]['content'], before)

    def run_review(self, post, **options):
        class FakeHTTP:
            def __init__(self, **kwargs): pass
            async def __aenter__(self): return self
            async def __aexit__(self, *args): pass
            async def post(self, *args, **kwargs): return await post(*args, **kwargs)
        async def scenario():
            with tempfile.TemporaryDirectory() as root:
                (Path(root) / 'evidence.txt').write_text('evidence ' * 2000)
                return await run_agent('Review these supplied headings only.',
                                       model='test/model', api_key='test-key', repo_root=root,
                                       role='reviewer', task_profile='review-change',
                                       no_tools=options.pop("no_tools", True), **options)
        with patch('openrouter_mcp.bridge.httpx.AsyncClient', FakeHTTP):
            return asyncio.run(scenario())

    def test_no_tools_omits_schema_and_preserves_runtime_model(self):
        async def post(*args, **kwargs):
            self.assertNotIn('tools', kwargs['json'])
            return httpx.Response(200, json={'model': 'observed/model', 'choices': [
                {'finish_reason': 'stop', 'message': {'role': 'assistant', 'content': 'No findings.'}}
            ]})
        self.assertEqual(self.run_review(post).observed_model, 'observed/model')

    def test_oversized_prompt_never_reaches_api(self):
        async def post(*args, **kwargs):
            self.fail('oversized evidence was sent')
        with self.assertRaisesRegex(RuntimeError, 'No oversized request was sent'):
            self.run_review(post, max_context_chars=10)

    def test_unexpected_tool_call_in_no_tools_mode_is_rejected(self):
        async def post(*args, **kwargs):
            return httpx.Response(200, json={'choices': [{'finish_reason': 'tool_calls',
                'message': {'role': 'assistant', 'tool_calls': [{'id': '1', 'type': 'function',
                'function': {'name': 'read_text_file', 'arguments': '{"path":"any.txt"}'}}]}}]})
        with self.assertRaisesRegex(RuntimeError, 'outside the permitted'):
            self.run_review(post)

    def test_large_tool_result_is_blocked_before_second_request(self):
        calls = 0
        async def post(*args, **kwargs):
            nonlocal calls
            calls += 1
            self.assertEqual(calls, 1, 'oversized tool evidence reached API')
            return httpx.Response(200, json={'choices': [{'finish_reason': 'tool_calls',
                'message': {'role': 'assistant', 'tool_calls': [{'id': '1', 'type': 'function',
                'function': {'name': 'read_text_file', 'arguments': '{"path":"evidence.txt"}'}}]}}]})
        with self.assertRaisesRegex(RuntimeError, 'context exceeds limit'):
            self.run_review(post, no_tools=False, max_context_chars=3000)
        self.assertEqual(calls, 1)

    def test_recovery_round_shares_total_budget(self):
        calls = 0
        async def post(*args, **kwargs):
            nonlocal calls
            calls += 1
            await asyncio.sleep(0.08 if calls == 1 else 1)
            return httpx.Response(200, json={'choices': [{'finish_reason': 'length',
                'message': {'role': 'assistant', 'content': 'Incomplete'}}]})
        with self.assertRaisesRegex(RuntimeError, 'time budget exhausted|wall timeout'):
            self.run_review(post, timeout_seconds=10, total_timeout_seconds=0.2)
        self.assertEqual(calls, 2)

    def test_total_budget_caps_a_slow_request(self):
        async def post(*args, **kwargs):
            await asyncio.sleep(1)
            self.fail('request was not cancelled')
        with self.assertRaisesRegex(RuntimeError, 'time budget exhausted|wall timeout'):
            self.run_review(post, timeout_seconds=10, total_timeout_seconds=0.05)


if __name__ == '__main__':
    unittest.main()
