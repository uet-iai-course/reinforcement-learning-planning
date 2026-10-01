# CLAUDE.md

This repo holds the RevealJS lecture decks, lecture notes and planning files for **Học tăng cường** (Reinforcement Learning), semester 1 of 2026–2027 (`2627-1/`). Source decks come from the 2025–2026 semester in `RL-hk2-2025-2026/`.

`AGENTS.md` is the full, authoritative specification, written in Vietnamese. `prompt_lecture_note_deck.md` is the two-stage `/goal` workflow (lecture note first, then slide deck) and extends `AGENTS.md` for materials and the index. This file tells Claude Code how to apply both: repo layout, commands, the rules most often broken, and how the multi-agent workflow maps onto Claude Code tools. Precedence: the user's instructions first, then `AGENTS.md` (and `prompt_lecture_note_deck.md` when that workflow is running), then this file. Read the relevant section of `AGENTS.md` before any deck or materials work.

## Repo map

| Path | Contents |
|---|---|
| `2627-1/lecture-NN-<ten-bai>.html` | One RevealJS deck per lecture (01–12 exist; the `.pdf` exports beside them are untracked) |
| `2627-1/lecture-slide.css` | The **only** course stylesheet, shared by every deck and the template |
| `2627-1/lecture-template.html` | Structural and visual base for new decks (untracked; copy structure, never content) |
| `2627-1/revealjs/`, `plugin/`, `vendor/{katex,marked,dompurify}/` | Local runtime; decks must not load anything from the network |
| `2627-1/img/lec-NN/` | SVG assets for each lecture |
| `2627-1/planning/lec-NN/` | `outline.md`, `storyboard.md`, `review-log.md` (plus older analysis files in some lectures) |
| `2627-1/materials/lec-NN/lecture-note.md` | Lecture note per lecture; template in `materials/_templates/lecture-note.md` |
| `2627-1/material-viewer.{html,css,js}`, `material-index.css` | Static Markdown viewer for lecture notes |
| `2627-1/index.html` | Course index; currently lists lectures 1–6 only |
| `RL-hk2-2025-2026/` | Source decks (PPTX/PDF) and `resources/` (homework PDFs). Untracked. |
| `.codex/`, `codex-orchestrator`, `openrouter-mcp/` | Historical Codex/OpenRouter setup. Not used by the current workflow. |

Ignore `.DS_Store`, `._*` files and `~$*` Office lock files everywhere.

## Commands

```bash
python3 -m reloadserver 8765                      # from repo root; port is positional, never --port
# deck:  http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html
# note:  http://localhost:8765/2627-1/material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html
git diff --check
```

Headless Chromium through Python Playwright is installed and is the visual-check tool (see Visual verification). There is no build step and no materials sync script in this repo.

## Hard rules

- Never read, load or send `.env` or `.env.*`. Never put secrets in prompts, logs or commits.
- Do not use OpenRouter, `openrouter-mcp/`, `codex-orchestrator`, or direct model API/CLI calls to stand in for sub-agents.
- **Choosing a lecture:** if the user hasn't named a source file, stop after listing `RL-hk2-2025-2026/` and ask. If the lecture number or title can't be inferred from the file name and content, ask before drafting.
- **CSS:** every deck, including the template, links `href="lecture-slide.css"`.
  - Reusable rules go in `lecture-slide.css`. Local CSS in a deck only for a one-slide need the shared file can't meet, and it must not override the shared system.
  - No per-lecture CSS files or copies of the stylesheet.
  - Editing `lecture-slide.css` means checking the template and every existing deck at wide and narrow sizes.
- **RevealJS config:** `lang="vi"`, 1280×720; outer `<section>` = one strand, inner `<section>` = one slide; footer at the end of `.slides` with course name, semester and lecture number.
  - Settings: `controlsLayout: "edges"`, `slideNumber: true`, `hash: true`, `hashOneBasedIndex: true`.
  - Plugins: `RevealMath.KaTeX`, `RevealNotes`, `RevealHighlight`, all local.
- **IDs:** every slide has a unique `data-slide-id`. It appears only in HTML and planning files, never on the slide face or in speaker notes.
- **Paths** are relative and valid when the server runs at the repo root.
- **Figures:** every diagram, chart and technical figure is redrawn as SVG (`2627-1/img/lec-NN/`, or inline when small and single-use) with `role="img"` and specific alt text. Keep labels, arrow directions, legends, data and meaningful proportions exactly as in the source.
  - Never embed rasters extracted from PDF or PPTX. A raster needs the user's explicit approval, recorded in `review-log.md`; without it, stop that part and ask.
  - Formulas, tables and code use KaTeX, HTML or code blocks, never images. In Markdown use only `$...$` and `$$...$$`.
  - No AI-generated images standing in for data or evidence. Colour is never the only signal.
- **Code demos:** convert only what the source contains. Don't invent notebooks or programs.
- **Index:** never link `planning/`, outlines, storyboards, review logs, `note-for-author.md` or sources. Only finished lectures appear.
  - Each card has two groups: **Bài giảng** (deck link) and **Ghi chú bài giảng** (viewer link, only once the note has passed review; otherwise `Chưa có`). This replaces the single-link rule in `AGENTS.md`, per `prompt_lecture_note_deck.md`.

## Writing course content (Vietnamese)

Everything a student sees is formal, academic, native Vietnamese: titles, slide text, figure captions, speaker notes, lecture notes, solutions.

- **English:** only for proper names, software, standard symbols, algorithm names and terms without a settled translation.
- **Abbreviations:** spell out in Vietnamese first, abbreviation in parentheses.
- **Banned tone:** no rhetorical questions, exclamations, praise, slogans or promotional phrasing.
  - No simulated speech or instructor directions, e.g. "chúng ta hãy nhìn", "nhấn mạnh với sinh viên", "đến đây chuyển sang trang sau".
  - Learning tasks ("Tính", "Xác định", "Chứng minh") and algorithm steps are fine.
- **No unsupported additions:** no claims, figures, sources or examples without a basis.
- **Titles:** name the concept, problem or result. No "Tại sao…?"/"Vì sao…?", calls to action or progress narration.
- **Bullets:** at most two lines each at 16:9; move explanation into the notes.
- **Keep off the slide face and out of speaker notes:** slide IDs, workflow labels, routing and timings. These live only in planning files.
- **Questions on slides** use the label **"Câu hỏi:"**.
- **Speaker notes** (`<aside class="notes">`) are short academic explanation: assumptions, what a formula or figure means, easy confusions, the link to what follows, and hints or solutions as reasoning steps. They must not just repeat the slide or contain only metadata.

### Skills: `no-ai-slop` and `quill`

`AGENTS.md` writes these as `no-ai-slop` and `quill`; in Claude Code both are user-level skills under `~/.claude/skills/`. Load them with the `Skill` tool, or read the files directly. Sub-agents must load them too; say so in every brief that touches text.

- **`no-ai-slop` is mandatory** for drafting, editing or reviewing titles, slide text, notes and materials. Read `~/.claude/skills/no-ai-slop/SKILL.md` first.
  - Writers and editors use **Edit** mode, then self-check against `~/.claude/skills/no-ai-slop/eval.md` and fix what fails before handing over.
  - Read-only reviewers use **Detect** mode: name the pattern, quote the line, propose a fix. They do not edit files.
  - Record the scope and result of the check in `review-log.md`. Never cite AI-detector scores or guesses about authorship as evidence.
  - Academic register and mathematical/algorithmic precision outrank the skill's advice on personal voice, humour or fragments. Keep definitions, result labels, assessment questions and summaries that have a learning function.
- **`quill`** is used only to check outline, concept order, terminology and continuity across sections. **Never create `quill.json`** and never run its Init workflow; this is not a book project.
  - Use the relevant parts of `~/.claude/skills/quill/references/workflows.md` (Outline, Threads, Character / Concept, Revise) as a checklist against `outline.md` and `storyboard.md`.

## Deck structure and content

- **Strands:** 5–7 outer sections, including an opening and a conclusion.
  - Each strand has its own function, an input from the strand before, and an output the next one uses.
  - Going outside 5–7 needs a source or user reason, recorded in `storyboard.md` and `review-log.md`.
- **Timing:** three 50-minute periods = 150 min; the deck covers 120 min, the other 30 are exercises and code demos.
- **Follow the source:** keep the order, flow and main ideas of the chosen source deck. Merge, split, add, cut or reorder only locally to fix errors, reduce overload, restore prerequisites or complete the learning flow, and log every deviation.
- **Concept journey for every core concept:** problem → intuition → example → formal statement/algorithm → application → check.
  - A lead-in example may sit with the problem, before intuition; the storyboard says which problem it makes concrete.
  - Steps may share a slide, but may not be reordered or silently dropped. Never open a core concept with a definition or notation.
  - Algorithms: hand-compute one step or iteration with initial values first; then give inputs, outputs, assumptions, initialisation, parameters, update rule, order of operations and stopping rule. Hand example, formula and pseudocode must agree.
- **One central point per slide.** Split long derivations, pseudocode or tables; never shrink text to fit.
  - Body text ≥ 0.75em; below 0.65em only for short captions the student-perspective reviewer confirmed are readable.
- **RL content standards:** distinguish agent, environment, state, observation, action, reward, policy, model and value function.
  - State domains, types, sizes, time indices, expectation conventions and termination before use.
  - Keep prediction vs control, on- vs off-policy, model-based vs model-free, $V$ vs $Q$ apart where relevant.
  - For MDPs state the Markov assumption, spaces, dynamics, reward and discount. For Bellman equations and updates check indices, conditioning, signs, discount, target and what is held fixed.
  - For deep RL distinguish online and target networks, replay buffer, bootstrap target, exploration behaviour and evaluation policy.
  - No claims of convergence, optimality, unbiasedness or stability without the deciding assumptions.
  - Recompute every numeric example, probability, expectation, value update and important tensor shape.
- **Sources:** traceable by source page or slide number. External sources only to correct or verify a claim, cited specifically.
- **Storyboard:** a section map (type, function, input, output, contribution to the central problem) plus one entry per slide with its reason to exist, the need it fills, links to the previous and next slide, the objective it supports, and a decision (`giữ | sửa | gộp | tách | thêm | bỏ`) with a reason. Each concept cluster records the slide IDs per step, what passes from example to formula, merged or `không áp dụng` steps, and timing toward 120 minutes.

## Multi-agent workflow in Claude Code

`AGENTS.md` requires an orchestrator plus sub-agents; don't do the whole workflow in one role.

- **Models:** the orchestrator is this session, running Claude Opus 5.5 (`claude-opus-5-5`) at effort `high`. If the session runs another model or effort, say so before delegating. Every sub-agent also runs Opus 5.5 at `high`.
- **Creating agents:** use the `Agent` tool.
  - `.claude/agents/` does not exist yet, so use `subagent_type: "fork"`; a fork inherits this session's model.
  - Never assign a workflow role to an agent type pinned to another model.
  - Continue an existing agent with `SendMessage` rather than spawning a new one.
- **Stopping rule:** if no Opus 5.5 sub-agent can be created, say so and stop the dependent work. Don't fall back silently to another model.
- **Concurrency:** read-only agents may run in parallel. **Only one agent writes files at a time.** The lecture-note writer and the deck writer never run together.
- **Every brief states:** role, inputs, output, file scope, done condition, whether `no-ai-slop` Edit or Detect mode applies, and "do not commit".
- **Logging:** record each agent's role, type, model and effort in `review-log.md`, using the tool call as evidence rather than the agent's own claim.

| Stage | Role(s) | Writes files? |
|---|---|---|
| Plan | Planning agent: goals, scope, concept list and journeys, task split, risks | No |
| Source analysis | Source-to-target slide map with decisions, figure inventory, gaps and inconsistencies | No |
| Draft | Authoring agent: outline, storyboard, deck, SVGs, notes; `no-ai-slop` Edit + `eval.md`; `quill` continuity check | Yes |
| Storyboard gate | Every slide's reason to exist, six-step journeys, section functions, 120-min timing | No |
| Review | Five independent roles on one frozen draft: student, RL expert, math/algorithm accuracy, academic/pedagogical critique (also `no-ai-slop` Detect), linking and storyline | No |
| Revise | One editor merges the reports, fixes HTML, SVG, outline, storyboard and notes in sequence, records rejected suggestions | Yes |
| Recheck | Math on changed content. Storyline on changed slides, ±2 neighbours and section boundaries; the whole deck if the opening, conclusion or thesis changed | No |
| Final check | Orchestrator or a verifier: technical, visual, planning sync, index, git | — |

- **Report format:** reviews return findings as `mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa` (lecture notes use `vị trí` instead of `trang chiếu`). The storyline reviewer also states `vai trò trong mạch`, `kết nối vào` and `kết nối ra`.
  - Severities are `chặn bàn giao`, `nghiêm trọng`, `trung bình` and `nhẹ`.
  - Every blocking and serious finding must be resolved.
- **Logging findings:** record each one in `review-log.md` with its status and decision. Never delete resolved findings.
- **Review scope:** for a local change give the reviewer the changed part, two slides either side and the section map when flow is involved. Math reviews keep the cluster's notation, assumptions, examples and sources. If a review fails for size, split it and retry with the same model.
- **Scaling to small edits:** a one-slide edit still goes editor → math and storyline rechecks on the affected slides → browser check → log. The full five-role review isn't needed.

## Visual verification

Required after every deck change. Only claim a visual check you actually ran.

1. Start `python3 -m reloadserver 8765` in the background from the repo root.
2. With Playwright Chromium, open the deck and jump to a slide by ID. Use `Reveal.getIndices(document.querySelector('section[data-slide-id="X"]'))`, then `Reveal.slide(h, v, 99)`, where `99` reveals all fragments.
3. Capture **1600×900** (16:9) and **390×844** (narrow). Visit every horizontal and vertical slide for a new deck.
4. Check: no console or page errors, no `.katex-error`, no broken resources or network requests for core assets, content fits the frame at 16:9, no horizontal overflow, no overlaps, body font sizes above the minimum, keyboard navigation works.
   - Ignore `.katex-mathml`, which is visually hidden.
5. View the screenshots yourself before reporting.
6. Keep screenshots in the session scratchpad, not in the repo.

For lecture notes, open the viewer URL and check that the Markdown renders, KaTeX has no errors, and nothing loads from the network.

## Lecture notes (`prompt_lecture_note_deck.md`)

- Stage I produces `2627-1/materials/lec-NN/lecture-note.md` and must pass review, commit and push before Stage II edits the deck.
- Each topic has a unique `note-topic-id`; decks map back with `data-slide-id`. Notes follow the same six-step concept journey.
- The topic map has four groups: `cốt lõi`, `cầu nối`, `bổ sung`, `đọc thêm`. Add bridge or supplementary items only for a named gap with a specific source.
- Viewer contract: `material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html`, both naming the same lecture.
- When a deck changes notation, assumptions, examples or concept order, review the note too.

## Git

- **Standing permission:** within the `prompt_lecture_note_deck.md` workflow, the user allows commit **and push** after each stage gate passes, without asking again. Outside that workflow, ask before committing.
- **Branch:** `main` tracks `origin/main`. Never force-push, rebase, amend or rewrite history.
- **Before committing:**
  - Run `git status --short` and `git diff --check`.
  - Stage explicit paths only; never `git add .` or `-A`. Most of the tree is ignored by an allow-list `.gitignore`; check new files are actually tracked.
  - Then run `git diff --cached --check`.
- **Commit scope:** only files from the finished work. For a deck: the deck HTML, `img/lec-NN/`, `planning/lec-NN/`, the related `index.html` entry, and shared files that truly had to change. Never mix two lectures in one commit.
- **Commit messages:**
  - `feat(materials-NN)` / `fix(materials-NN)` for lecture notes;
  - `feat(lecture-NN)` / `fix(lecture-NN)` for decks;
  - `docs:` for `AGENTS.md`, `CLAUDE.md` and workflow files.
- **After pushing:** confirm with `git fetch` and `git branch -r --contains HEAD`. If the push fails, report the local hash and the error, and do not claim the work is delivered.

## Done means

- The deck keeps the source's main ideas and flow; every deviation is logged.
- Every blocking and serious finding from the five reviews is resolved and logged.
- `outline.md`, `storyboard.md` and `review-log.md` in `planning/lec-NN/` match the current deck, including `data-slide-id`s.
- All figures are SVG or have an approved raster exception.
- The browser check passed at both sizes; no broken resources.
- `no-ai-slop` scope and self-check result are recorded in `review-log.md`.
- `index.html` is updated for completed lectures only, with no links to planning files.

The handoff lists: deck file and local URL, source file, redrawn figures and raster exceptions, checks run, intended deviations, remaining limits, and (when committed) commit hash and push verification.
