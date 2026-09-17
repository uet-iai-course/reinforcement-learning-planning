# Nhật ký viết lại Bài 02 — 2026-09-18

## Yêu cầu và kế hoạch

Viết lại bảy phần đã chấp nhận cho sinh viên năm 3, có phân tích mạch và cách thể hiện từng trang; dùng Quill rà quan hệ tiên quyết và no-ai-slop biên tập. Chỉ dẫn nội bộ nằm trong planning; slide và notes chỉ có nội dung học thuật, đáp án, nguồn. Commit riêng từng phần sau kiểm tra, chưa push. Bản đang triển khai, chưa qua năm vòng rà soát cuối.

## Điều phối và bằng chứng runtime

- plan-retry: requested_model=deepseek/deepseek-v4-flash-0731; observed_model=deepseek/deepseek-v4-flash-0731; provider=OpenRouter.
- source: requested_model=deepseek/deepseek-v4-flash-0731; observed_model=deepseek/deepseek-v4-flash-0731; provider=OpenRouter.
- write-01: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter.

Reader lập kế hoạch được chấp nhận về quy trình; điều phối viên sửa ánh xạ trang suy đoán và khẳng định quá mức về giả thuyết phần thưởng. Reader phân tích nguồn đã đọc bản trích; báo cáo có lỗi ngôn ngữ và ánh xạ, không dùng nguyên văn. Điều phối viên đối chiếu XML/ảnh nguồn và thay bằng bảng nguồn trong outline. Công thức dựng KaTeX, không làm SVG như đề xuất sai của reader. Đếm lại mê cung: 27 ô trống, 37 tường, không phải 36/28 như reader. Không gọi hình trang11 là minimax khi nguồn không nêu thuật toán. Reader không có quyền ghi.

## Nguồn, hình và sai khác có chủ ý

- Kiểm kê trực tiếp PPTX, XML và ảnh trang1–27; nguồn bài tập hw02 đã đọc. Bản cũ dùng mê cung6×4 và đường7 bước; bản này khôi phục lưới8×8, đích ngoài và đường16 bước của nguồn25–26.
- Đưa mê cung lên mở bài và dùng lại qua từng khái niệm để chuẩn bị công thức. Gộp giao diện và tín hiệu thưởng; tách chính sách thành phần riêng.
- Bỏ trang5–6 khỏi tuyến vì không phục vụ mục tiêu đã chốt; bỏ logo nhận diện và ảnh game27, giữ nhiệm vụ phân loại bằng thông tin/giả thiết. Không giữ raster, không có ngoại lệ raster.
- Trang11 có bàn cờ/cây lựa chọn, không phải trang trống. Giữ bàn cờ kết thúc ở phần6 để vận dụng thưởng và tổng thưởng; lược cây sao lưu giá trị vì đây là phần ôn bài01 và cơ chế cập nhật vượt mục tiêu bài02. Đã ghi quyết định trong ánh xạ nguồn.
- Sửa vai trò môi trường và chỉ số thưởng nguồn15, phát biểu Markov nguồn17, quan sát đầy đủ nguồn18, dự đoán nguồn24; kiểm định toán độc lập còn chờ.
- SVG nguồn-maze/policy/values và maze-local được dựng từ cấu trúc lưới, mũi tên, giá trị nguồn. Kiểm tra mọi ô của chính sách đều đến G, giá trị bằng âm số bước khi gamma=1. Tổng 27 trạng thái không kết thúc và G.

## Hạ tầng và công cụ

- CSS đổi thành lecture-slide.css; giữ nguyên quy tắc cũ, thêm lớp bố cục dùng chung chỉ kích hoạt bằng lecture-deck. 12 bài hiện có và mẫu tải được, CSS đúng tên và không lỗi JavaScript.
- Máy chủ python3 -m reloadserver 8765 chạy tại gốc rl-plan. Cổng trước đó phục vụ ds-foundation-algorithms; đã chuyển tiến trình xem trước sang rl-plan.
- Codex Slides: dự án 20260917174610-b-i-02-giao-di-n-t-c-t-m-i-tr-ng-b-n-vi--sj78. Đã mở trang chủ và dự án bằng Chromium cục bộ. Phiên này không có công cụ Browser nhúng của Codex; chưa tuyên bố đã rà hình cuối bằng Codex Slides.
- Đọc Quill Outline Workflow để rà mục đích/tiên quyết/đầu ra và liên tục; không tạo quill.json. Đọc no-ai-slop cùng eval.md, áp dụng cho body/notes.

## Phần 1 — kiểm tra và chỉnh sửa

Writer tạo bốn trang và phân tích. Điều phối viên sửa tọa độ Bắt đầu sai trong alt thành (0,2); đủ bảy mục trong bản đồ; bỏ lời chào rỗng, “Câu nối”, mã trang, lời bình thiết kế và hứa giải bằng thuật toán; sửa phân biệt hàm giá trị đánh giá với mô hình dự báo. Notes hiện là lời giải thích trực tiếp. Kiểm tra bố cục và bàn phím được ghi sau lượt chạy trình duyệt.

Phần 1: 4 trang đã duyệt ở 1280×720 và 390×844; không tràn khung, lỗi KaTeX, ảnh hỏng, HTTP lỗi hoặc JavaScript lỗi; phím xuống hoạt động. Tắt tự chuyển sang cuộn ở màn hình hẹp để giữ điều hướng RevealJS. Đã xem ảnh trang mê cung và bản đồ nội dung; dịch nhãn Bắt đầu để không chồng chỉ số hàng.

## Phần 2 — kiểm tra và chỉnh sửa

Writer: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Bảy trang,20 phút. Bỏ bảng hàm giá trị bị dùng sớm ở trang mục tiêu, thay bằng bảng16/18 bước. Rút notes, bỏ chỉ dẫn người viết và lời dẫn, sửa ví dụ phản hồi trễ thành quy ước thưởng của ví dụ, không quy kết mọi ván cờ có cùng thưởng. Câu hỏi tương tác có nhãn chuẩn. Kiểm tra14 lượt màn hình rộng/hẹp không lỗi; hạ chiều cao hình dòng thời gian để tăng khoảng trắng. Kiểm tra lại sau chỉnh bố cục trước commit.

## Phần 3 — kiểm tra và chỉnh sửa

Writer: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Tám trang,25 phút. Sửa dữ kiện xe cho khớp hình1/5m/s cùng phanh; bỏ khẳng định X bắt buộc dùng lịch sử; phát biểu Markov xét biến cố điều kiện có xác suất dương, không yêu cầu xác suất kết quả dương. Công thức hai dòng đủ lớn. Loại lời bình về slide, chỉ dẫn người viết, câu tu từ; bài kiểm tra còn3trường hợp và robot trong đáp án. Thay hình nhỏ lặp bằng bảng, thêm lề tránh nút điều hướng. Kiểm tra16lượt rộng/hẹp không lỗi và kiểm tra lại cả3phần sau đổi lề.

## Phần 4 — kiểm tra và chỉnh sửa

Writer: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Năm trang,15 phút. Sửa ký hiệu tập thành mathcal X/A và phân biệt X_t với S_t; dùng không âm thay vì dương. Sửa hướng Đông tại(1,2) thực tế là tường, vẫn được chọn nhưng đứng yên. Đưa đáp án0,3 vào notes, bổ sung nguồn writer bỏ thiếu; bỏ chỉ dẫn thiết kế. Kiểm tra10lượt rộng/hẹp đủ5trang, không tràn, lỗi KaTeX, ảnh hỏng, HTTP hay JavaScript lỗi. Đã xem công thức chính sách xác định/ngẫu nhiên.

## Phần 5 — kiểm tra và chỉnh sửa

Writer: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Chín trang,25 phút. Sửa hướng đoạn cuối thành Nam–Đông–Đông; tách ví dụ ngẫu nhiên khỏi mê cung xác định; sửa điều kiện kỳ vọng hữu hạn, phân biệt dừng gần chắc chắn với kỳ vọng thời gian dừng hữu hạn. Công thức mô hình dùng điều kiện đầy đủ. Bỏ đáp án trên mặt câu hỏi và lời bình quy trình. Sửa escape dấu nhỏ hơn trong HTML; bổ sung kiểm tra dấu dollar còn sót. 18 lượt rộng/hẹp không tràn, không rawMath, lỗi KaTeX, ảnh hỏng hoặc lỗi tài nguyên/JavaScript. Đã tính lại tổng -1,-1.75,-3 và kỳ vọng -4; vòng rà toán độc lập cuối bài vẫn bắt buộc.

## Phần 6 — kiểm tra và chỉnh sửa

Writer: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Bảy trang,20 phút. Thêm một trang vận dụng bàn cờ nguồn11, đưa tổng dự kiến lên43 trang. Sửa so sánh chính sách thành nhiệm vụ đánh giá chính sách cố định và tìm chính sách tốt; không gán vòng lặp rồi thoát cho chính sách xác định chỉ phụ thuộc vị trí. Nêu rõ hành động va tường vẫn nhận -1, bước vào G cũng nhận -1, sau G không còn thưởng. Tính lại toàn bộ27 giá trị của mê cung, giữ đích ngoài lưới. Bàn cờ X thắng, thưởng cuối bằng1 nhưng tổng thưởng tại trạng thái kết thúc bằng0. Bỏ lời bình quy trình trong notes. 14 lượt rộng/hẹp không tràn, không lỗi toán, ảnh hay JavaScript; tăng cỡ số trong hình giá trị để đọc trên máy chiếu.

## Phần 7 — kiểm tra và chỉnh sửa

Writer: requested_model=z-ai/glm-5.3-flash; observed_model=z-ai/glm-5.3-flash; provider=OpenRouter. Ba trang,7 phút. Sửa X_t thành biểu diễn dùng để quyết định, không đồng nhất với lịch sử; sửa mô tả bài tập theo văn bản hw02, không gán bài10 cho riêng mê cung. Bảng tổng kết bốn vai trò, ba câu tự kiểm tra và tài liệu đọc nối sang bài03. Notes không còn chỉ dẫn biên soạn. Kiểm tra6 lượt rộng/hẹp không tràn, lỗi toán, ảnh hoặc tài nguyên/JavaScript; đã xem trang tổng kết và bài tập. Đủ7phần,43trang,120phút; đang chờ kiểm định storyboard và năm báo cáo độc lập.
