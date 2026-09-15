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
`--reasoning-effort` (`none`, `minimal`, `low`, `high`, `max`) hoặc
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
| `source` | 14 | 600 giây | 18.000 | Phân tích và ánh xạ nguồn |
| `storyboard` | 10 | 600 giây | 12.000 | Kiểm định storyboard |
| `review-full` / `review` | 6 | 180 giây | 5.000 | Rà toàn bài theo từng vai |
| `review-section` | 4 | 120 giây | 3.500 | Rà một cụm khái niệm; mặc định reviewer |
| `review-change` | 2 | 90 giây | 2.200 | Rà tiêu đề, câu dẫn hoặc thay đổi nhỏ |
| `write` | 20 | 900 giây | 32.000 | Soạn một sản phẩm hoàn chỉnh đã cô lập |
| `recheck` | 2 | 90 giây | 2.200 | Rà lại đúng vấn đề đã sửa |
| `patch` | 10 | 300 giây | 6.000 | Sửa một hoặc hai khối độc lập |

Ví dụ:

```bash
uv run openrouter-mcp-reviewer --repo-root .. --json --task-profile review-full \
  "Rà Lecture 01 theo góc nhìn sinh viên; chỉ đọc các tệp được chỉ định."
```

Reader mặc định dùng `deepseek/deepseek-v4-flash-0731`; reviewer và writer mặc định dùng
`z-ai/glm-5.3-flash`. Vai rà toán hoặc chuyên môn Học tăng cường phải truyền
`--model deepseek/deepseek-v4-flash-0731`; vai sinh viên và mạch viết giữ mặc định GLM.
Khi không truyền `--reasoning-effort`, cầu nối dùng `none` cho DeepSeek V4 Flash
và `minimal` cho GLM 5.3 Flash. Hai giá trị này tránh để phần suy luận chiếm hết
ngân sách trả lời; đối số tường minh vẫn có ưu tiên cao hơn.
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
Với deck HTML nén, không giao cùng lượt việc gắn hàng chục thuộc tính, sửa nội
dung và cập nhật planning. Thực hiện ánh xạ cơ học trước, sau đó chạy một patch
cho HTML và một patch riêng cho outline/storyboard. Thử nghiệm Bài 11 cho thấy
một writer gộp ba tệp đã dùng hết 20.000 token trước khi gọi công cụ; các patch
cô lập hoàn tất trong 4–7 lượt với ngân sách 6.000 token.
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

## Chọn cách gọi reviewer theo tác vụ

Không dùng một lệnh rà toàn deck cho mọi chỉnh sửa. Chọn phạm vi trước khi chọn
ngân sách. Các giới hạn dưới đây là ngân sách khởi đầu, không bảo đảm API luôn
phản hồi kịp. Không tự tăng timeout hoặc chuyển mô hình khi nhà cung cấp chậm.

| Tác vụ | Hồ sơ | Đầu vào cần chuẩn bị | Giới hạn lịch sử gửi API | Tổng thời gian worker |
|---|---|---|---:|---:|
| Tiêu đề, câu dẫn, chỉnh chữ, thay đổi nhỏ | `review-change` | Trích đoạn đã sửa, hai trang lân cận mỗi phía; sơ đồ các section nếu sửa mạch | 16.000 ký tự | 150 giây |
| Rà lại một lỗi | `recheck` | Vấn đề cũ, đoạn sau sửa, giả thiết và các phần phụ thuộc | 16.000 ký tự | 150 giây |
| Công thức, thuật toán, một cụm khái niệm | `review-section` | Định nghĩa, ký hiệu, giả thiết, ví dụ và nguồn của cụm | 32.000 ký tự | 240 giây |
| Bản nháp mới hoặc đổi luận điểm/mở–kết bài | `review-full` | Một bài và các bằng chứng cần cho vai được giao | 60.000 ký tự | 360 giây |

Giới hạn ký tự tính trên JSON lịch sử thông điệp, gồm chỉ dẫn, prompt, kết quả
công cụ và câu trả lời trước đó; không phải số token và không chỉ là kích thước
tệp. Cầu nối kiểm tra trước **mỗi** request. Nếu vượt giới hạn, lệnh thất bại
trước khi gửi request đó; không cắt bằng chứng rồi giả vờ đã rà toàn bộ.
Kết quả đọc tệp của reviewer không bị cắt thêm bởi cầu nối; công cụ đọc vẫn có
phạm vi dòng riêng, phải kiểm tra dấu hiệu còn dòng chưa đọc.

`openrouter-mcp-reviewer` mặc định dùng `review-section`. `review` tương đương
ngân sách `review-full`; `recheck` nay dành cho phạm vi nhỏ, không phải một deck.
Các mặc định reader và writer không đổi. Có thể ghi đè bằng `--timeout`
(mỗi API), `--total-timeout` (toàn worker), `--max-context-chars` và
`--max-tokens`, nhưng phải có lý do cụ thể cho phạm vi được tăng.
Ngân sách tổng bao gồm cả lượt đọc công cụ và lượt phục hồi câu trả lời bị cắt.

### Đầu vào trích đoạn, không cho tự mở rộng

Với tác vụ nhỏ, dùng `--no-tools` và đặt bằng chứng ngay trong prompt. Cờ này
loại bỏ schema công cụ khỏi request và từ chối nếu mô hình vẫn yêu cầu công cụ.
Chỉ reviewer dùng được cờ này. Mỗi trích đoạn cần tên tệp, ID trang hoặc dòng,
và ranh giới; không đưa `.env`, biến bí mật hoặc dữ liệu ngoài phạm vi vào prompt.

```bash
uv run openrouter-mcp-reviewer --repo-root .. --json \
  --task-profile review-change --no-tools \
  'Rà tiêu đề theo bằng chứng sau. Phạm vi: [tệp, ID trang].
  Thay đổi: [nội dung trước và sau].
  Bằng chứng: [trích đoạn thật, trang lân cận, chuỗi section].
  Báo cáo dưới 300 từ; nêu bằng chứng thiếu, không suy đoán phần chưa đọc.'
```

Các phần trong ngoặc vuông phải được thay bằng dữ liệu thật trước khi chạy.
Khi chuẩn bị prompt dài bằng chương trình, truyền nó thành một đối số trong
`subprocess.run([...])`, không ghép thành mã shell.

### Rà có công cụ đọc

Dùng `review-section` cho một cụm. Chỉ định chính xác tệp và phạm vi dòng trong
prompt; yêu cầu không list/search khi đã biết vị trí. Với HTML nén, ít dòng vẫn
có thể rất dài: chuẩn bị trích đoạn theo `data-slide-id` thay vì đọc cả tệp.
Cờ giới hạn ký tự chỉ chặn kích thước; phạm vi đường dẫn/dòng trong prompt vẫn
là chỉ dẫn cho worker, không phải một danh sách đường dẫn bị khóa bằng mã.

Rà toàn bài bằng `review-full`. Nếu vượt ngân sách, chia thành các gói có bảng
bao phủ trang nguồn/trang đích; mỗi gói giữ đủ tiên quyết và trang lân cận.
Vai mạch viết còn cần một lượt tổng hợp toàn tuyến bằng bản đồ section và các
điểm nối. Không dùng kết quả rà một gói để tuyên bố đã rà toàn bài.

### Khi API chậm hoặc câu trả lời bị cắt

1. Xem `context_chars`, `request_timeout_seconds`, `reason` và `finish_reason`
   trong log. `api_request_waiting` chỉ là nhịp báo chờ, không phải tiến độ sinh.
2. `context_budget`: chia gói hoặc rút phần không liên quan; không tự tăng trần
   cho một tác vụ nhỏ. Cầu nối chưa gửi request vượt trần.
3. `api_wall_timeout` hoặc `worker_wall_timeout`: dừng gói; chỉ thử lại tối đa
   một lần sau khi thu hẹp đầu vào, giữ cùng mô hình và ghi kết quả runtime.
   Cầu nối không tự thử lại timeout, không đổi mô hình.
4. `finish_reason=length`: yêu cầu báo cáo ngắn hơn. Cầu nối cho phép một lượt
   phục hồi mặc định trong tổng ngân sách; không tăng token vô hạn.
5. Nếu vẫn thất bại, ghi gói nào chưa được rà; không đánh dấu đạt. Không kết
   luận “nhà cung cấp nghẽn” chỉ từ log chờ.

Năm vai độc lập vẫn chạy bằng năm tiến trình. Số gói có thể nhiều hơn số vai;
điều phối viên hợp nhất và kiểm tra độ bao phủ. Không chạy thêm một đợt lớn chỉ
để chẩn đoán timeout; dùng kiểm thử giả lập cho ngân sách và một request nhỏ
nếu cần xác minh kết nối thật.
