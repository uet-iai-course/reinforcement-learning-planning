# /goal — Quy trình hai giai đoạn cho một buổi học: lecture note rồi slide deck

## Biến đầu vào

- `BÀI_NN`: số bài cần xử lý, ví dụ `BÀI_06`. Có thể thay bằng tên bài hoặc đường dẫn tệp trong kho nguồn học kỳ 2 năm học 2025–2026 tại `RL-hk2-2025-2026/`; sản phẩm đích vẫn thuộc học kỳ 1 năm học 2026–2027.
- Suy ra số bài và tên bài từ tên tệp, nội dung nguồn và các bài hiện có. Nếu vẫn không xác định được, dừng sau khi kiểm kê và hỏi người dùng. Không tự chọn bài.

## Phạm vi và chuẩn

- Học phần là **Học tăng cường** (học kỳ 1, 2026–2027), tuân theo `AGENTS.md`. Không nhầm chuẩn Học tăng cường với giải thuật dữ liệu lớn; mọi thuật ngữ, công thức, giả thiết phải theo tiêu chuẩn Học tăng cường trong `AGENTS.md`.
- Tham khảo trực tiếp `../ds-foundation-algorithms/AGENTS.md`, `../ds-foundation-algorithms/2627-1/material-viewer.*`, `material-index.css`, `materials/_templates/lecture-note.md` và `index.html`; chuyển các cơ chế dưới đây sang Học tăng cường, không sao chép nội dung môn học:
  - Lecture note của mỗi bài nằm tại `2627-1/materials/lec-NN/lecture-note.md`.
  - Lecture note Markdown là bản nội dung đã kiểm định dùng để đồng bộ slide deck. Không sao chép nguyên văn note lên trang chiếu; giữ chung thuật ngữ, ký hiệu, giả thiết, ví dụ và thứ tự khái niệm.
  - Mỗi thẻ trong `2627-1/index.html` có hai nhóm: **Bài giảng** (link slide deck) và **Ghi chú bài giảng** (link material-viewer). Link viewer chỉ được thêm khi lecture note đã đạt kiểm định.
  - Bản đồ chủ đề của mỗi bài gồm bốn nhóm: **cốt lõi**, **cầu nối**, **bổ sung**, **đọc thêm**. Đề xuất mục cầu nối hoặc bổ sung chỉ khi có khoảng trống cụ thể đã chỉ ra và có nguồn cụ thể; không thêm cho đủ.
  - Dùng `note-topic-id` trong lecture note và `data-slide-id` trong slide deck để ánh xạ hai chiều giữa note và trang chiếu.
- Ngôn ngữ, biên tập, `$no-ai-slop`, `$quill`, cấu trúc học tập, tiêu chuẩn toán học và RevealJS theo đúng `AGENTS.md`.

## Quy tắc vận hành bắt buộc

- Người dùng cho phép Codex **commit và push** sau khi hoàn tất lecture note hoặc slide deck, không cần hỏi lại. Thực hiện commit và push ngay khi cổng kiểm soát của giai đoạn đạt.
- Người dùng cho phép gửi tệp nội bộ project lên OpenRouter, **trừ** `.env`, mọi biến thể `.env.*`, bí mật và thông tin xác thực. Không đọc, không đưa vào prompt, log hoặc kết quả.
- Cấm force push, rebase và viết lại lịch sử Git.
- Dùng `$no-ai-slop` cho lecture note, slide và ghi chú diễn giả. Cấm câu hỏi tu từ, câu cảm thán, lời ca tụng, khẩu hiệu, giọng quảng bá, lời dẫn rỗng, nhịp câu máy móc và mọi chỉ dẫn hoặc hướng dẫn dành cho người viết lộ ra trong sản phẩm.
- Dùng `$quill` để rà dàn ý và tính liên tục, nhưng **không tạo `quill.json`**.
- Phân vai mô hình qua OpenRouter:
  - `openrouter-mcp-reader` / `openrouter-mcp-reviewer` với `--model deepseek/deepseek-v3.2` cho các vai phân tích logic, toán học và Học tăng cường.
  - Các vai mạch viết, góc nhìn sinh viên và no-ai-slop chạy bằng tiến trình `openrouter-mcp-reader` hoặc `openrouter-mcp-reviewer` riêng với `--model z-ai/glm-5.3-flash`.
  - Chỉ tin `requested_model`, `observed_model` và `provider` trong kết quả `--json` làm bằng chứng runtime; không tin lời tự khai của worker.
  - Mọi lệnh worker dùng `--json`. Không dùng `collaboration.spawn_agent`. Khi một worker lỗi, dừng và báo nguyên văn lỗi; không đổi model ngầm, không gọi worker mặc định thay thế.
- Không đọc `.env`, biến thể `.env`, hoặc bất kỳ tệp bí mật nào.

## Giai đoạn I — Lecture note

1. **Kiểm kê và lập kế hoạch (reader, song song):** chạy `openrouter-mcp-reader` với `--task-profile plan` và `--task-profile source` trong hai tiến trình riêng. Tác tử lập kế hoạch và tác tử phân tích nguồn đề xuất bản đồ chủ đề độc lập. Đầu ra bất biến của đợt này gồm mục tiêu, tiên quyết, bảng ánh xạ nguồn, kiểm kê công thức–ví dụ–hình–mã, rủi ro và hai bản đề xuất chủ đề.
2. **Hợp nhất bản đồ chủ đề (reader/reviewer):** một tác tử riêng đối chiếu hai đề xuất và phân loại `cốt lõi`, `cầu nối`, `bổ sung`, `đọc thêm`. Mỗi mục ghi nguồn, vai trò trong mạch, kiến thức đầu vào, sản phẩm học tập, vị trí, kết nối trước–sau và tác động phạm vi. Chỉ giữ mục cầu nối hoặc bổ sung khi nó sửa một khoảng trống cụ thể và có nguồn phù hợp. Điều phối viên duyệt phạm vi trước khi writer chạy.
3. **Soạn note (một writer, tuần tự):** `openrouter-mcp-writer` với `--repo-root` hẹp tạo `2627-1/materials/lec-NN/lecture-note.md`. Mỗi chủ đề có `note-topic-id`; công thức dùng `$...$`/`$$...$$`; mỗi khái niệm trọng tâm đi theo vấn đề → trực giác → ví dụ tính tay → hình thức/thuật toán → ứng dụng và giới hạn → kiểm tra. Chỉ gộp bước khi vẫn giữ một luận điểm trung tâm và ghi lý do trong dàn ý cùng nhật ký rà soát. Ghi nguồn theo trang hoặc trang chiếu nguồn. Biên tập theo `$no-ai-slop`; rà dàn ý và tính liên tục bằng `$quill` mà không tạo `quill.json`.
4. **Năm reviewer song song:** chạy năm tiến trình `openrouter-mcp-reviewer --task-profile review` riêng. Dùng `--model z-ai/glm-5.3-flash` cho góc nhìn sinh viên và kết nối–mạch viết; dùng `--model deepseek/deepseek-v3.2` cho chuyên gia Học tăng cường, độ chính xác toán học–thuật toán và phản biện học thuật–giảng dạy. Mỗi báo cáo có `mức độ`, `vị trí`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.
5. **Sửa tuần tự:** một writer hợp nhất báo cáo và sửa note tuần tự; ghi quyết định với đề xuất không áp dụng vào nhật ký rà soát.
6. **Recheck theo phạm vi:** sau mỗi lần sửa, chỉ rà lại các phần bị ảnh hưởng và hai mục lân cận mỗi phía (`--task-profile recheck`). Nếu sửa mở bài, kết bài hoặc luận điểm trung tâm, rà lại toàn bộ.
7. **Cổng kiểm soát giai đoạn I:** note đạt kiểm định, mọi lỗi chặn bàn giao và nghiêm trọng đã xử lý, bản đồ chủ đề đủ bốn nhóm, `note-topic-id` duy nhất, không vi phạm no-ai-slop.
8. **Công bố và index:** với lecture note đầu tiên, tạo hoặc thích nghi `material-viewer.html`, `material-viewer.css`, `material-viewer.js`, `material-index.css`, `materials/_templates/lecture-note.md` và thư viện cục bộ cần thiết; cập nhật `.gitignore` để các tệp công khai này được theo dõi. Viewer phải làm sạch HTML, chỉ nhận `doc` trong `materials/lec-NN/`, buộc NN của `doc` và `deck` trùng nhau, render KaTeX cục bộ và dùng được bằng bàn phím. Trong `index.html`, liên kết ghi chú dùng đúng dạng `material-viewer.html?doc=materials/lec-NN/lecture-note.md&deck=lecture-NN-<ten-bai>.html`. Chưa đạt kiểm định thì hiển thị `Chưa có`, không tạo liên kết giả. Ghi trong `review-log.md` rằng nhóm tài nguyên hai liên kết thay thế quy tắc một liên kết duy nhất hiện có trong `AGENTS.md`, theo yêu cầu của goal này.
9. **Commit và push** khi cổng đạt (đã được phép, không hỏi lại). Kiểm tra `git status --short` và diff; không đưa tệp tạm hoặc thay đổi bài khác vào commit. Dùng `feat(materials-NN): add <ten-bai> lecture note` hoặc `fix(materials-NN): revise <ten-bai> lecture note`, rồi `git push origin main`. Thông báo tệp, URL ghi chú, kiểm tra, sai khác có chủ ý và giới hạn.

## Giai đoạn II — Slide deck

1. **Kế hoạch deck (reader):** từ lecture note đã đạt kiểm định, lập kế hoạch ánh xạ `note-topic-id` → `data-slide-id`, dàn ý 5–7 mạch `<section>` ngoài, storyboard và thời lượng 120 phút.
2. **Soạn deck (một writer, tuần tự):** tạo `2627-1/lecture-NN-<ten-bai>.html`, SVG tại `2627-1/img/lec-NN/`, và ba tệp quy trình tại `2627-1/planning/lec-NN/` (`outline.md`, `storyboard.md`, `review-log.md`) theo đúng `AGENTS.md`: mẫu `lecture-template.html`, `lecture-style.css`, `lang="vi"`, khung 1280×720, thư viện cục bộ, `data-slide-id` duy nhất, ghi chú diễn giả `<aside class="notes">`, mọi hình vẽ lại SVG. Biên tập theo `$no-ai-slop`; rà bằng `$quill` không tạo `quill.json`.
3. **Năm reviewer song song:** dùng đúng năm tiến trình và phân vai mô hình ở giai đoạn I; rà slide deck, ghi chú diễn giả và ánh xạ với lecture note.
4. **Sửa tuần tự và recheck theo phạm vi:** như giai đoạn I.
5. **Cổng kiểm soát giai đoạn II:**
   - Kiểm định viewer/RevealJS: chạy `python3 -m reloadserver 8765` tại thư mục gốc (cổng là đối số vị trí, không dùng `--port`); mở `http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html` và duyệt mọi trang ngang, dọc; kiểm tra tràn chữ, công thức KaTeX, SVG, đường dẫn, bàn phím, tương phản ở khung 16:9 và màn hình hẹp.
   - Kiểm định index: `2627-1/index.html` có thẻ bài với nhóm **Bài giảng** (link deck) và nhóm **Ghi chú bài giảng** (link material-viewer tĩnh, chỉ khi note đã đạt kiểm định); không link tới tệp quy trình.
   - Kiểm định material-viewer tĩnh: viewer hiển thị đúng nội dung Markdown, `note-topic-id` khớp bản đồ chủ đề, không phụ thuộc mạng.
   - Dùng Codex Slides rà trực quan sau cùng; nếu không khả dụng, báo rõ giới hạn và không tuyên bố đã rà bằng Codex Slides.
6. **Commit và push** khi cổng đạt (đã được phép, không hỏi lại). Kiểm tra `git status --short` và diff. Dùng `feat(lecture-NN): add <ten-bai> slide deck` cho deck mới hoặc `fix(lecture-NN): revise <ten-bai> slide deck` cho lần sửa đáng kể, rồi `git push origin main`. Bàn giao tệp deck, URL cục bộ cổng 8765, tệp note, hình đã vẽ lại, kiểm tra, sai khác có chủ ý, ngoại lệ và giới hạn.

## Nguyên tắc pipeline và mức song song

- Chia công việc thành các đợt `fan-out → fan-in → cổng kiểm soát`. Chỉ mở đợt sau khi đầu vào chung đã ổn định và điều phối viên đã chấp nhận đầu ra của đợt trước.
- Song song hóa các tác vụ chỉ đọc độc lập: plan với source; các gói nguồn không trùng nhau; năm reviewer; các kiểm tra liên kết, công thức, cấu trúc và tài nguyên. Mỗi tiến trình nhận danh sách tệp, mục tiêu, sản phẩm và điều kiện dừng rõ ràng.
- Đóng băng hồ sơ nguồn và đặc tả đã duyệt trước khi writer chạy. Reviewer đọc cùng một checkpoint để báo cáo có thể hợp nhất.
- Chỉ một writer được sửa một tập tệp tại một thời điểm. Không để writer của lecture note và writer của slide deck chạy đồng thời. Không sửa deck khi giai đoạn lecture note chưa commit và push thành công.
- Sau khi hợp nhất báo cáo, tạo một hàng đợi sửa tuần tự. Thay đổi toán học hoặc thuật toán quay lại reviewer độ chính xác; thay đổi cấu trúc hoặc câu chuyển quay lại reviewer mạch viết; thay đổi hiển thị quay lại kiểm định trực quan.
- Có thể kiểm kê nguồn của bài kế tiếp trong một pipeline riêng chỉ khi người dùng đã chỉ định bài đó; không để đầu ra hoặc writer của hai bài trộn chung commit.

## Checklist đầu ra

- [ ] `2627-1/materials/lec-NN/lecture-note.md` đạt kiểm định, có `note-topic-id` và bản đồ chủ đề bốn nhóm.
- [ ] `2627-1/lecture-NN-<ten-bai>.html` đạt kiểm định RevealJS, ánh xạ `data-slide-id` ↔ `note-topic-id` đầy đủ.
- [ ] SVG trong `2627-1/img/lec-NN/`, không ảnh raster trái phép.
- [ ] `2627-1/planning/lec-NN/` đủ `outline.md`, `storyboard.md`, `review-log.md`.
- [ ] `2627-1/index.html` cập nhật hai nhóm Bài giảng / Ghi chú bài giảng.
- [ ] Material-viewer tĩnh hoạt động và được liên kết.
- [ ] Năm báo cáo reviewer độc lập cho mỗi giai đoạn; mọi lỗi bắt buộc đã xử lý.
- [ ] Nội dung hiển thị, lecture note và ghi chú diễn giả đã tự kiểm trực tiếp theo `no-ai-slop/eval.md`.
- [ ] Kiểm định cổng 8765 và Codex Slides hoàn tất.
- [ ] Commit và push đã thực hiện sau mỗi giai đoạn, không force push.

## Điều kiện dừng

- Không xác định được số bài hoặc tên bài sau khi kiểm tra tên tệp và nội dung nguồn: dừng và hỏi người dùng.
- Worker OpenRouter lỗi: dừng giai đoạn phụ thuộc, báo nguyên văn lỗi, không đổi model ngầm.
- Thiếu giả thiết, ảnh raster cần ngoại lệ hoặc thông tin không suy ra được từ kho: dừng phần bị ảnh hưởng và hỏi người dùng.
- Cổng kiểm soát không đạt sau khi sửa: không commit, tiếp tục xử lý rồi chạy lại kiểm định.
