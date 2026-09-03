# Cầu nối worker MCP–OpenRouter theo vai trò

Thành phần này gọi worker trực tiếp qua Chat Completions API của OpenRouter và
cung cấp công cụ MCP theo vai trò:

- `list_files`: liệt kê tệp trong kho;
- `read_text_file`: đọc một đoạn tệp UTF-8 có giới hạn;
- `search_text`: tìm chuỗi văn bản theo nghĩa đen.
- `write_text_file`: ghi một tệp UTF-8, chỉ được đưa vào schema của writer và
  chỉ hoạt động bên trong `--repo-root`.
- `replace_text_file`: thay chính xác một đoạn UTF-8 trong tệp hiện có, kiểm tra
  số lần khớp trước khi ghi; chỉ writer nhận công cụ này.

Mô hình không gọi MCP trực tiếp. Client Python gửi schema công cụ MCP cho
OpenRouter, nhận `tool_calls`, thực thi chúng qua MCP rồi gửi kết quả về mô
hình. Đây là vòng lặp tool-calling phía client theo API của OpenRouter.

## Cài đặt

```bash
cd openrouter-mcp
uv sync
```

Khóa chỉ đặt trong môi trường; không ghi vào kho:

```bash
export OPENROUTER_API_KEY="..."
```

Nếu biến chưa được export, cầu nối tự nạp riêng `OPENROUTER_API_KEY` từ
`.env` tại `--repo-root`. Đây là cấu hình phía điều phối viên; tệp và giá trị
khóa không được đưa vào công cụ MCP, prompt, log tiến độ hoặc kết quả worker.

## Gọi worker

Chạy từ thư mục `openrouter-mcp`:

```bash
uv run openrouter-mcp-reader \
  --repo-root .. \
  --json \
  "Đọc AGENTS.md và tóm tắt trách nhiệm. Không sửa tệp."
```

Reviewer dùng cùng các công cụ chỉ đọc:

```bash
uv run openrouter-mcp-reviewer --repo-root .. --json "Rà báo cáo..."
```

Writer phải nhận một gốc ghi nhỏ nhất có thể. Ví dụ kiểm thử chỉ cấp thư mục
tạm, không cấp toàn bộ kho:

```bash
mkdir -p /tmp/rl-plan-openrouter-smoke
uv run openrouter-mcp-writer \
  --repo-root /tmp/rl-plan-openrouter-smoke \
  --json \
  "Chỉ tạo worker-check.txt với nội dung được yêu cầu."
```

Kết quả `--json` gồm `role`, `requested_model`, `observed_model`, `provider`
và `output`. Ba trường model/provider là metadata do cầu nối thu tại runtime,
không phải lời tự khai của mô hình.

### Theo dõi tiến độ

Mặc định, client phát sự kiện tiến độ dạng JSON Lines trên `stderr` trong khi
worker chạy. JSON kết quả cuối vẫn được ghi riêng trên `stdout`, nên điều phối
viên có thể theo dõi từng vòng API và từng tool-call mà không phải đợi toàn bộ
tác vụ kết thúc. Trong lúc nhà cung cấp chưa trả xong một phản hồi,
`api_request_waiting` được phát mỗi tối đa 15 giây. `--timeout` là hạn tuyệt đối
theo thời gian thực cho mỗi request, không chỉ là timeout của từng pha mạng.
Ví dụ sự kiện:

```json
{"event":"tool_call_started","elapsed_seconds":12.4,"role":"reviewer","round":2,"tool":"read_text_file","path":"2627-1/lecture-01-gioi-thieu-hoc-tang-cuong.html"}
```

Sự kiện không chứa prompt, truy vấn tìm kiếm, nội dung tệp hoặc giá trị bí mật.
Dùng `--progress text` nếu cần log dễ đọc hoặc `--progress none` để tắt.

Các tệp `.env` và biến thể như `.env.local` bị loại khỏi `list_files` và
`search_text`, đồng thời bị từ chối ở cả công cụ đọc và ghi.

### Hồ sơ tham số theo công việc

Dùng `--task-profile` để chọn ngân sách phù hợp. Có thể ghi đè riêng bằng
`--max-rounds`, `--timeout`, `--max-tokens`, `--temperature`,
`--reasoning-effort` hoặc
`--empty-answer-retries`. Mỗi hồ sơ mặc định thử lại một lần nếu nhà cung cấp
trả HTTP 200 nhưng nội dung cuối rỗng; sự kiện `empty_answer_received` cho biết
trường hợp này ngay trong log tiến độ. Vòng thử lại nằm ngoài ngân sách
`max_rounds`. Nếu vẫn rỗng, worker kết thúc với lỗi thay vì trả JSON thành công.
`finish_reason` bằng `error` hoặc `length` cũng được coi là chưa hoàn tất và
kích hoạt cùng cơ chế phục hồi.

Các hồ sơ dùng reasoning effort `low` vì GLM 5.3 Flash luôn bật reasoning và
mặc định của nhà cung cấp là `max`. Việc giới hạn effort giữ đủ ngân sách token
cho báo cáo cuối. Sự kiện `api_response_received` ghi `finish_reason`, tổng
token hoàn tất và reasoning token khi nhà cung cấp trả các trường này.

| Hồ sơ | Vòng | Timeout mỗi API | Token đầu ra | Dùng cho |
|---|---:|---:|---:|---|
| `plan` | 12 | 600 giây | 16.000 | Lập kế hoạch |
| `source` | 20 | 600 giây | 24.000 | Phân tích và ánh xạ nguồn |
| `storyboard` | 10 | 600 giây | 12.000 | Kiểm định storyboard |
| `review` | 8 | 600 giây | 12.000 | Năm rà soát độc lập |
| `write` | 20 | 600 giây | 32.000 | Soạn một sản phẩm hoàn chỉnh đã cô lập |
| `recheck` | 6 | 600 giây | 10.000 | Rà lại đúng một note/deck; báo cáo ngắn |
| `patch` | 6 | 300 giây | 7.000 | Sửa một hoặc hai khối độc lập |

Ví dụ:

```bash
uv run openrouter-mcp-reviewer --repo-root .. --json --task-profile review \
  "Rà Lecture 01 theo góc nhìn sinh viên."
```

Reader mặc định dùng `deepseek/deepseek-v3.2`; reviewer và writer mặc định dùng
`z-ai/glm-5.3-flash`. Vai rà toán hoặc chuyên môn Học tăng cường phải truyền
`--model deepseek/deepseek-v3.2`; vai sinh viên và mạch viết giữ mặc định GLM.
Tên GLM hiện hành từng được thử nghiệm dưới tên `stealth/ox-alpha`. OpenRouter
đã ngừng slug thử nghiệm;
nếu vẫn truyền `stealth/ox-alpha`, client sẽ báo ánh xạ rồi gọi
`z-ai/glm-5.3-flash`. Có thể thay model bằng biến môi trường hoặc đối số:

```bash
export OPENROUTER_MODEL="provider/model"
uv run openrouter-mcp-reader --repo-root .. --json "Nhiệm vụ chỉ đọc"
```

Model được chọn phải hỗ trợ tham số `tools` trên OpenRouter.

Các preset là ngân sách tối đa, không thay cho việc cô lập đầu vào. Reviewer
DeepSeek chỉ nhận đúng một note hoặc deck và được yêu cầu đọc tệp đó một lần.
Writer `write` chỉ soạn một sản phẩm; mọi hàng đợi chỉnh sửa sau review phải
tách thành các lượt `patch`, mỗi lượt tối đa hai khối độc lập. Cách chia này
tránh hai lỗi đã lặp ở Bài 04–07: cạn vòng gọi công cụ và
`finish_reason=length` sau khi worker ghi bán phần.

`z-ai/glm-5.3-flash` là model có tính phí. Kiểm tra giá hiện hành trên
OpenRouter trước khi chạy tác vụ lớn.

## Chạy MCP server độc lập

Server dùng stdio theo mặc định:

```bash
MCP_REPO_ROOT=.. uv run openrouter-mcp-server
```

## Kiểm thử

```bash
uv run python -m unittest discover -s tests -v
```

## Giới hạn an toàn

- Mọi đường dẫn phải nằm trong `MCP_REPO_ROOT`.
- Reader và reviewer không nhận schema công cụ ghi.
- Writer chỉ có thể ghi tệp trong `MCP_REPO_ROOT`; không có công cụ xóa, chạy
  lệnh hoặc truy cập mạng.
- Tệp đọc tối đa 1 MB; số dòng và số kết quả đều bị giới hạn.
- Client dừng khi vượt quá số vòng gọi công cụ cho phép.
- Cầu nối này thay cho `collaboration.spawn_agent` đối với ba vai trò dự án;
  nó không đăng ký loại tác tử vào runtime Codex hiện tại.
