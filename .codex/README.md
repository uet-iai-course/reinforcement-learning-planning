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

### Bài 04 — cấu hình đã quan sát

- Lập kế hoạch deck ổn định với reader DeepSeek, hồ sơ `plan`, 10 lượt, timeout 600 giây, 14.000 token; cấu hình 8 lượt đã vượt giới hạn công cụ.
- Rà deck độc lập ổn định với reviewer GLM hoặc DeepSeek, hồ sơ `review`, 8 lượt. Vai phản biện sư phạm có thể cần chạy lại nếu chạm giới hạn 8 lượt.
- Tái rà deck phạm vi 2–3 tệp ổn định với GLM 5 lượt và DeepSeek 6–8 lượt, timeout 600 giây, 7.000–9.000 token. Tái rà toán DeepSeek 6 lượt đã vượt giới hạn; 8 lượt thành công.
- Writer GLM cho nhiều sửa rải rác đã vượt giới hạn ở 8 và 10 lượt. Với trường hợp tương tự, dùng gói tệp hẹp hơn hoặc cấu hình 20 lượt đã chạy tốt ở các bài trước; luôn kiểm JSON runtime và diff trước khi chấp nhận.

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

Với lecture note Bài 03 dài khoảng 34 KB, writer tạo bản đầu chạy ổn định bằng
`z-ai/glm-5.3-flash`, profile `write`, `--max-rounds 12 --timeout 600
--max-tokens 28000`; worker đọc năm tệp nguồn cố định trong một batch, ghi note
ở vòng 2 và kết thúc ở vòng 3. Writer vá 7–9 đoạn cục bộ chạy ổn định bằng
`--max-rounds 6 --timeout 300 --max-tokens 8000–9000`, với nhiều lệnh
`replace_text_file` trong cùng một batch. Một lượt sửa rộng với 12 vòng đã ghi
một phần rồi dừng ở `model exceeded the tool-call limit (12)`; vì vậy không
dùng 12 vòng cho hàng đợi nhiều thay thế tuần tự nếu prompt không yêu cầu gộp
tool call.

Reviewer toán DeepSeek cho note Bài 03 ổn định nhất khi prompt buộc đúng một
`read_text_file` toàn tệp (`start_line=1`, `max_lines=2000`), rồi trả báo cáo:
`--max-rounds 4 --timeout 600 --max-tokens 12000`. Lượt này hoàn tất ở vòng 2.
Recheck toàn note dùng `--max-rounds 3 --timeout 600 --max-tokens 9000`; recheck
một đoạn 50 dòng dùng `--max-rounds 3 --timeout 300 --max-tokens 4000`. Không
chia tệp dài thành nhiều lần đọc: các lượt DeepSeek đọc ba tệp bằng nhiều tool
call đã lần lượt chạm giới hạn 5, 8 và 12; một lượt gom ba tệp với timeout 300
giây dừng ở `OpenRouter request exceeded 300s wall timeout`.

Reviewer mạch GLM cho toàn lecture note Bài 03 chạy được bằng profile `recheck`,
`--max-rounds 3 --timeout 300 --max-tokens 6000`; worker kết thúc ở vòng 3.
Prompt nên buộc một lần đọc toàn tệp. GLM đôi khi vẫn lặp cùng tool call, nên
giữ trần 3 vòng và kiểm tra log tiến độ trước khi chấp nhận báo cáo.

Với slide deck Bài 03, reader lập kế hoạch ổn định khi bốn tệp được cô lập,
dùng `deepseek/deepseek-v3.2`, profile `plan`, `--max-rounds 8 --timeout 600
--max-tokens 12000`; câu trả lời cuối được phép sau vòng công cụ thứ 8. Writer
GLM sửa ba tệp deck/planning hoàn tất bằng `--max-rounds 10 --timeout 600
--max-tokens 16000`. Writer vá đúng hai chuỗi hoàn tất bằng `--max-rounds 6
--timeout 300 --max-tokens 6000`.

Reviewer deck Bài 03 không nên đọc bốn tệp bằng DeepSeek trong nhiều tool-call:
các lượt trần 8 và 12 đều dừng ở `model exceeded the tool-call limit`. Cấu hình
ổn định là cô lập một `deck.html` khoảng 31 KB, profile `review` hoặc `recheck`,
`--max-rounds 6 --timeout 600 --max-tokens 9000–12000`; lượt toán và tái rà toán
đều hoàn tất, giữ đúng `deepseek/deepseek-v3.2`. Reviewer GLM đọc bốn tệp với
`--max-rounds 8 --timeout 600 --max-tokens 12000` hoàn tất cho vai sinh viên và
mạch viết; tái rà một deck dùng `--max-rounds 6 --timeout 600 --max-tokens
9000`. Một writer rộng 12 vòng đã ghi bán phần rồi chạm giới hạn; nên tách các
vá còn lại thành lượt hẹp và kiểm diff sau mỗi lượt.

Vá công thức D04 Bài 03 trên đúng một HTML hoàn tất với writer GLM, profile
`write`, `--max-rounds 4 --timeout 300 --max-tokens 5000`. Recheck DeepSeek
trên cùng một HTML, profile `recheck` và cùng trần 4 vòng/5.000 token, xác nhận
biểu thức ngắt dòng tương đương công thức kỳ vọng và không còn lỗi toán.

Với lecture note Bài 04 khoảng 46 KB, ba reader DeepSeek chạy thành công trên
gói nguồn cô lập: lập kế hoạch `plan/12/600/16000`, phân tích nguồn
`source/20/600/24000`, và hợp nhất `plan/10/600/18000` (profile/số vòng/timeout/
token). Writer bản đầu GLM dùng `write/12/600/32000`; lượt vá Bài 9 phạm vi hẹp
dùng `write/5/300/7000`. Tất cả lượt thành công trả model quan sát đúng model
yêu cầu và provider `OpenRouter`.

Writer GLM không ổn định khi nhận nhiều thay thế tuần tự trên note Bài 04:
hai lượt `write/8/600/14000` và `write/12/600/14000` ghi được một phần rồi dừng
`tool_call_limit`; lượt hẹp `write/6/600/9000` dừng `incomplete_answer` sau hai
phản hồi `finish_reason=length`; lượt ba thay thế `write/4/300/5000` cũng ghi
một phần rồi dừng `tool_call_limit`. Vì vậy phải kiểm diff sau từng lượt và
dùng writer chỉ cho một hoặc hai khối độc lập; bản vá cơ học còn lại do điều
phối viên thực hiện và được reviewer độc lập tái kiểm.

Reviewer note Bài 04 chạy ổn định nhất với một tệp cô lập: DeepSeek
`recheck/4/600/10000` cho toàn note và GLM `recheck/3/600/7000` cho mạch viết.
Tái rà đoạn ngắn 40–210 dòng dùng DeepSeek hoặc GLM với `recheck`, 3–5 vòng,
timeout 300 giây và 3.500–5.000 token. DeepSeek vẫn có thể gọi thêm search dù
prompt yêu cầu một lần đọc; nếu chạm giới hạn vòng, chạy lại cùng model với
phạm vi dòng nhỏ hơn, không đổi model.

Với lecture note Bài 05 khoảng 36 KB, reader DeepSeek chạy tốt bằng
`plan/12/600/14000` và `source/20/600/18000`; lượt source cần một lần tự thử
lại phản hồi rỗng. Hợp nhất chỉ nên cho đúng hai JSON và dùng
`recheck/6/600/10000`; lượt đọc phạm vi rộng hơn với 8 vòng đã dừng
`model exceeded the tool-call limit (8)`. Writer bản đầu GLM ổn định với
`write/20/600/32000` và cơ chế phục hồi phản hồi chưa hoàn chỉnh.

Năm review note Bài 05: GLM đọc note hoặc ba tệp note/planning ổn định với
3–6 vòng, timeout 600 giây; DeepSeek nên cô lập đúng một note và dùng
`recheck/4–6/600/10000`. Ba lượt DeepSeek ban đầu đọc nhiều tệp bằng
`review/8` đều chạm giới hạn công cụ, nhưng chạy lại trên đúng một note hoàn
tất với model không đổi. Hai lượt writer sửa rộng bằng GLM `write/12` ghi bán
phần rồi chạm giới hạn; với nhiều thay thế, dùng 20 vòng hoặc tách thành các
bản vá hẹp và kiểm diff sau từng lượt. Tái kiểm cuối Bài 05 chạy tốt bằng
DeepSeek `recheck/4/600/10000` và GLM `recheck/4/600/8000`; DeepSeek có thể
đọc note trên 400 dòng thành hai đoạn và gọi thêm search, nên không hạ dưới 4
vòng.

Với deck Bài 05 khoảng 28 KB, reader kế hoạch DeepSeek hoàn tất bằng
`plan/10/600/16000`; writer GLM bản đầu hoàn tất bằng `write/20/600/18000`.
Reviewer GLM cho vai sinh viên và mạch viết chạy ổn định với 8 vòng, timeout
600 giây và 10.000–11.000 token. Reviewer DeepSeek đọc nhiều tệp với 6–7 vòng
có thể chạm `tool_call_limit`; cô lập đúng một deck rồi dùng
`recheck/6–8/600/10000` đã hoàn tất với model quan sát đúng yêu cầu. Tái rà mạch
bốn tệp bằng GLM nên đặt `--repo-root` trực tiếp tại `2627-1`, dùng
`recheck/8/600/9000`; nếu để gốc cao hơn, model có thể tự ghép lặp `2627-1` và
lãng phí giới hạn công cụ. Writer GLM nhiều thay thế với 16 vòng có thể lặp
phép thay thế không khớp rồi dừng giới hạn; nên tách bản vá nhỏ hoặc dùng trần
20 vòng và luôn kiểm diff.
