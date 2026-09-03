# Codex điều phối worker qua OpenRouter MCP

Khởi chạy Codex bằng `./codex-orchestrator`. Codex chính vẫn dùng nhà cung cấp
đang cấu hình cho người dùng. Ba worker dự án được gọi bằng các tiến trình CLI
trong `openrouter-mcp/`, không qua `collaboration.spawn_agent`:

- `openrouter_reader` → `openrouter-mcp-reader`;
- `openrouter_reviewer` → `openrouter-mcp-reviewer`;
- `openrouter_writer` → `openrouter-mcp-writer`.

## Khởi chạy

Đặt khóa trong `.env` ở gốc kho; cầu nối chỉ nạp `OPENROUTER_API_KEY` ở phía
điều phối viên và không đưa tệp hoặc giá trị khóa cho worker:

```bash
OPENROUTER_API_KEY="..."
./codex-orchestrator
```

Có thể truyền thẳng câu lệnh hoặc tùy chọn Codex:

```bash
./codex-orchestrator "Dùng các tác tử theo quy trình trong AGENTS.md."
```

Có thể dùng biến môi trường đã export thay cho `.env`. Cài môi trường cầu nối
một lần bằng `cd openrouter-mcp && uv sync`. Mỗi lệnh worker phải dùng `--json`
để trả metadata model/provider cùng nội dung.

## Mô hình worker và trách nhiệm điều phối

Mỗi worker chỉ nhận một nhiệm vụ hẹp, có đầu vào, đầu ra và phạm vi tệp cụ
thể. Reader và reviewer chỉ nhận
công cụ đọc. Writer nhận `write_text_file` và `replace_text_file`, nhưng chỉ
ghi được bên trong `--repo-root` của tiến trình. Mọi vai trò đều bị chặn đọc,
tìm kiếm hoặc ghi `.env` và các biến thể `.env.*`.

Codex chính phải đối chiếu `requested_model`, `observed_model` và `provider`
do cầu nối thu từ phản hồi OpenRouter; lời tự khai trong nội dung worker không
phải bằng chứng runtime. Nếu một worker lỗi, dừng giai đoạn phụ thuộc và báo
nguyên văn lỗi. Không gọi worker mặc định thay thế.

Để đổi mô hình, đặt `OPENROUTER_MODEL` hoặc truyền `--model`. Mô hình thay thế
phải hỗ trợ tool calling trên OpenRouter.

Không thêm khóa API, tệp `.env`, lịch sử phiên hoặc dữ liệu xác thực vào kho.

## Cấu hình đã kiểm chứng cho pipeline lecture note và slide deck

Chạy trong `openrouter-mcp/` và đặt cache của `uv` tại thư mục tạm để không
phụ thuộc quyền ghi vào cache người dùng:

```bash
UV_CACHE_DIR=/tmp/rl-plan-uv-cache uv run <worker> \
  --repo-root /data/tqlong/rl-plan \
  --json --model <model> --task-profile <profile> \
  --max-rounds <rounds> --timeout 180 \
  '<nhiệm vụ hẹp, kèm danh sách tệp chính xác>'
```

Các tổ hợp đã chạy thành công:

| Vai trò | Worker | Model | Profile | Số vòng |
|---|---|---|---|---:|
| Lập kế hoạch lecture note | `openrouter-mcp-reader` | `deepseek/deepseek-v3.2` | `plan` | 12 |
| Phân tích nguồn lecture note | `openrouter-mcp-reader` | `deepseek/deepseek-v3.2` | `source` | 20 |
| Phân tích logic, toán, RL phạm vi hẹp | `openrouter-mcp-reader` | `deepseek/deepseek-v3.2` | `recheck` | 8 |
| Rà mạch viết, sinh viên | `openrouter-mcp-reviewer` | `z-ai/glm-5.3-flash` | `recheck` | 4–6 |
| Rà logic, toán, RL | `openrouter-mcp-reviewer` | `deepseek/deepseek-v3.2` | `recheck` | 6–8 |
| Rà note trên hai tệp cố định | `openrouter-mcp-reviewer` | `z-ai/glm-5.3-flash` hoặc `deepseek/deepseek-v3.2` | `review` | 4 |
| Tái rà một tệp, phạm vi hẹp | `openrouter-mcp-reviewer` | `z-ai/glm-5.3-flash` hoặc `deepseek/deepseek-v3.2` | `recheck` | 3 |
| Rà deck trên bốn tệp cố định | `openrouter-mcp-reviewer` | `z-ai/glm-5.3-flash` hoặc `deepseek/deepseek-v3.2` | `review` | 8 |
| Tái rà deck sau đổi cấu trúc, 2–3 tệp | `openrouter-mcp-reviewer` | `z-ai/glm-5.3-flash` hoặc `deepseek/deepseek-v3.2` | `recheck` | 5 |
| Ghi một phạm vi tệp | `openrouter-mcp-writer` | `z-ai/glm-5.3-flash` | `write` | 12 |
| Ghi nhiều điểm trong deck | `openrouter-mcp-writer` | `z-ai/glm-5.3-flash` | `write` | 20 |

`source` hoặc `review` chỉ dùng khi đầu vào đã được cô lập. Với tài liệu lớn,
`recheck` ổn định hơn khi prompt cấm liệt kê và tìm kiếm, đồng thời nêu đúng
từng tệp được phép đọc. Không cho worker quét `2627-1/vendor/`, thư viện
RevealJS hoặc toàn bộ kho. Tạo hồ sơ nguồn nhỏ trước nếu tài liệu gốc là PDF
hoặc PPTX.

Sau mỗi lệnh, lưu ba trường `requested_model`, `observed_model` và `provider`
từ JSON vào nhật ký rà soát. Không coi tên model do worker tự viết trong phần
nội dung là bằng chứng.

Hai cấu hình reader đầu tiên được kiểm chứng khi xử lý lecture note Bài 01
ngày 02/09/2026. Cả hai trả
`requested_model = observed_model = deepseek/deepseek-v3.2`, provider
`OpenRouter`. Hồ sơ `plan` cần một lượt thử lại sau phản hồi HTTP 200 rỗng và
hoàn tất ở vòng 11. Hồ sơ `source` hoàn tất ở vòng 9; request tổng hợp cuối kéo
dài gần hết timeout 300 giây. Các lượt chạy trong sandbox trước đó trả
`api_transport_error`, vì vậy worker dùng OpenRouter phải chạy với quyền mạng
nâng cao và vẫn nạp khóa ở phía cầu nối từ `.env`; không đọc hoặc chuyển nội
dung `.env` cho worker.

Writer Bài 01 dùng profile `write`, trần 12 vòng, timeout 300 giây và 32.000
token; hoàn tất ở vòng 9 sau một phản hồi `finish_reason=error` được cầu nối
thử lại. Runtime trả `requested_model = observed_model =
z-ai/glm-5.3-flash`, provider `OpenRouter`. Với `--repo-root` hẹp không chứa
`.env`, cầu nối không tự tìm thấy khóa. Cách đã kiểm chứng là tạo liên kết
`.env` tạm trong repo-root của writer trỏ về `.env` ở gốc kho, xác minh MCP
vẫn chặn đọc `.env`, rồi gỡ liên kết ngay sau lượt chạy.

Lượt chỉnh sửa deck Bài 01 có nhiều điểm dùng cùng model/profile với
`--max-rounds 20 --timeout 300 --max-tokens 32000` và hoàn tất ở vòng 17;
runtime trả `requested_model = observed_model = z-ai/glm-5.3-flash`, provider
`OpenRouter`. Cấu hình 12 vòng trước đó dừng với `tool_call_limit` sau khi đã
ghi một phần. Vì vậy dùng 12 vòng cho writer hẹp, còn hàng đợi sửa nhiều tệp
hoặc nhiều điểm dùng 20 vòng. `timeout` áp dụng cho từng yêu cầu API; tổng thời
gian của tiến trình có thể vượt 300 giây khi có nhiều vòng công cụ.

Với lecture note Bài 02, reviewer chỉ đọc hai tệp cố định chạy ổn định bằng
`--max-rounds 4 --timeout 300 --max-tokens 7000`: GLM hoàn tất vòng 2 và
DeepSeek hoàn tất vòng 3. Cấu hình mặc định `review` với timeout 240 giây đã
từng làm GLM dừng ở `api_wall_timeout`, nên dùng 300 giây cho note dài khoảng
40 KB. Recheck đúng một tệp và phạm vi rất hẹp chạy ổn định bằng
`--max-rounds 3 --timeout 300 --max-tokens 3000`; cả GLM và DeepSeek hoàn tất
vòng 2. Prompt phải giới hạn số lần `read_text_file` và yêu cầu báo cáo ngắn;
một lượt GLM trước đó với đầu ra 5.000 token đã chạm `finish_reason=length`
rồi mới hoàn tất ở lượt phục hồi.

Với slide deck Bài 02, lượt rà bốn tệp bằng `--max-rounds 4` không đủ: cả năm
reviewer dừng với `model exceeded the tool-call limit (4)` sau khi đọc tệp.
Lượt chạy lại cùng model/profile bằng `--max-rounds 8 --timeout 300
--max-tokens 7000` hoàn tất; GLM thường đọc bốn tệp trong một batch rồi trả ở
vòng 2, DeepSeek trả ở vòng 5. Recheck sau thay đổi cấu trúc chạy ổn định bằng
`--max-rounds 5 --timeout 300 --max-tokens 4500`; GLM hoàn tất vòng 3 và
DeepSeek hoàn tất vòng 4. Không đổi model khi tăng giới hạn vòng.
