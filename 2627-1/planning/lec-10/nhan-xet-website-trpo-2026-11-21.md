# Nhận xét website TRPO sau chỉnh sửa (tác giả gửi 2026-11-21)

Văn bản trích từ `Nhan_xet_website_TRPO_sau_chinh_sua.docx` (yêu cầu: "Tham khảo các nhận xét này"). [IMG rIdNN] đánh dấu hình: Hình 1 là sơ đồ định hướng (dữ liệu của chính sách cũ → hàm thay thế "dự báo mức cải thiện" và KL "giới hạn độ thay đổi" → tối ưu trong miền tin cậy, gradient tự nhiên và tìm kiếm lùi → chính sách mới); Hình 2 là điểm đánh giá (mạch dẫn dắt 9, trực quan hóa 9, liên kết ví dụ–toán 9,5, cân bằng trực giác–chứng minh 7,5, từ lý thuyết đến thuật toán 8).

```text
BÁO CÁO RÀ SOÁT
Nhận xét bản cập nhật bài giảng TRPO
Trọng tâm: Hàm thay thế và miền tin cậy
Ngày rà soát: 21/11/2026   •   Đối tượng: giảng viên thiết kế học phần
Đường dẫn: https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-10-trpo-va-ppo.html#/4
1. Nhận định tổng quan
Bản cập nhật đã cải thiện rõ rệt mạch sư phạm: các khái niệm toán học được giới thiệu thông qua câu hỏi và hiện tượng cụ thể trước khi chuyển sang công thức, chặn sai số và thuật toán. Đặc biệt, việc sử dụng nhất quán MDP hai trạng thái giúp sinh viên thấy rõ ý nghĩa của surrogate objective và nguyên nhân xuất hiện trust region.
Bản hiện tại đã phù hợp để giảng dạy. Các chỉnh sửa tiếp theo nên tập trung vào độ chính xác của phát biểu về bảo đảm hiệu năng, cách định vị sơ đồ tổng thể TRPO, và mật độ chứng minh trong mạch chính.
2. Những cải thiện đáng ghi nhận
Nội dung
Bản đã sửa
Đánh giá
Động cơ TRPO
Bắt đầu từ câu hỏi biết hướng tăng J nhưng chưa biết bước dài bao nhiêu.
Rất tốt
Phân phối trạng thái
Sơ đồ luồng 100 episode so sánh hai chính sách.
Rất tốt
Performance Difference Lemma
Tách ba thành phần; nhấn mạnh occupancy mới.
Tốt
Hàm thay thế
Làm rõ phép thay ηπ′ bằng ηπ.
Rất tốt
Importance sampling
Tách điều đã hiệu chỉnh ở phân phối hành động và điều chưa hiệu chỉnh ở phân phối trạng thái.
Rất tốt
Sai số surrogate
So sánh dự báo +0,095 với cải thiện thực −0,085.
Rất tốt
Độ dài bước
Đồ thị Δℒ và ΔJ cùng bài tập tại t = 0,25.
Rất tốt
Trust region
Minh họa miền KL và ứng viên ngoài miền.
Tốt
Chặn sai số
Liên kết KL → TV → occupancy → sai số.
Tốt
Natural gradient
Minh họa ellipse và so sánh g với F⁻¹g.
Tốt

Điểm nổi bật nhất là ví dụ surrogate dự báo tăng 0,095 trong khi hiệu năng thực giảm 0,085: sinh viên có thể thấy bằng hình rằng tỉ số chính sách không loại bỏ được sai số do phân phối trạng thái thay đổi.
3. Năm đề xuất chỉnh sửa tiếp theo
3.1. Ưu tiên 1 — Chuẩn hóa phát biểu về bảo đảm cải thiện
Phần mở đầu không nên tạo ấn tượng rằng TRPO/PPO luôn đảm bảo hàm mục tiêu thực J không giảm. Cách diễn đạt này mạnh hơn tính chất của thuật toán khi triển khai trên mẫu và dùng các xấp xỉ.
Câu chữ đề nghị dùng:
“TRPO và PPO kiểm soát mức thay đổi chính sách nhằm giảm nguy cơ suy giảm hiệu năng khi cập nhật từ dữ liệu đã thu thập.”

Mức lý thuyết: định lý chặn cải thiện có ý nghĩa trong các giả thiết và đại lượng được xác định chính xác.
Mức bài toán KL: ràng buộc khoảng cách giúp kiểm soát sự thay đổi chính sách, không mặc nhiên đảm bảo J tăng.
Mức thuật toán thực hành: còn có sai số ước lượng, xấp xỉ bậc hai, KL theo bộ đệm và line search.
3.2. Ưu tiên 2 — Đưa sơ đồ tổng thể TRPO lên sớm
Ngay sau khi giới thiệu bài toán tối ưu miền tin cậy, nên cho sinh viên thấy toàn bộ quy trình. Sau đó mới quay lại giải thích Fisher matrix, natural gradient và line search. Mục đích là cung cấp “bản đồ” trước khi nghiên cứu từng bộ phận.
 [IMG rId11]
Hình 1. Sơ đồ định hướng: mục tiêu surrogate và ràng buộc KL cùng đi vào bước tối ưu TRPO.
3.3. Ưu tiên 3 — Đưa các chứng minh dài vào slide phụ
Mạch chính hiện có chuỗi chứng minh dày: Performance Difference Lemma, Pinsker, dịch chuyển occupancy, định lý chặn cải thiện, cận lỏng và hệ quả cải thiện đơn điệu. Chuỗi này hữu ích về toán học nhưng có thể làm sinh viên mất mạch từ trust region sang cách giải.
Giữ trong mạch chính slide diễn giải ba mắt xích “KL → Total Variation → Dịch chuyển occupancy → Sai số surrogate”, sau đó dùng một ví dụ cận lỏng để thảo luận. Chuyển các chứng minh đầy đủ sang slide dọc/phụ lục để phục vụ lớp cần độ sâu toán học.
3.4. Ưu tiên 4 — Khai thác ví dụ phản trực giác của natural gradient
Bài giảng đưa ra một ví dụ trong đó bước natural gradient đạt J ≈ 1,807, còn bước gradient thông thường dưới cùng ngân sách KL bậc hai đạt J ≈ 1,835. Đây là chi tiết rất đáng dùng để kiểm tra mức hiểu của sinh viên.
J(natural gradient) ≈ 1,807     <     J(gradient thường) ≈ 1,835

Câu hỏi đề xuất đặt trực tiếp trên slide: “Vì sao hướng natural gradient, được suy ra là tối ưu, lại có thể cho J thấp hơn trong ví dụ này?”
Trả lời bằng cách phân biệt rõ ba đối tượng:
Tầng
Đại lượng
Ý nghĩa
1
Hàm hiệu năng thực J
Đại lượng thật sự muốn tăng.
2
Hàm thay thế ℒ
Dự báo thay đổi J từ dữ liệu cũ.
3
Xấp xỉ tuyến tính của ℒ
Bài toán cục bộ mà natural gradient tối ưu, cùng KL xấp xỉ bậc hai.

Vì vậy, nghiệm của bài toán xấp xỉ cục bộ không nhất thiết tối ưu trên hàm hiệu năng thực.
3.5. Ưu tiên 5 — Phân biệt hai khái niệm “KL trung bình”
Hai công thức thường mang tên giống nhau nhưng dùng trọng số khác nhau: một ở cấp độ phân tích lý thuyết và một được ước lượng trên bộ đệm.
KL có trọng số lý thuyết:   D̄_KL = Σₛ νᵖⁱ(s) · D_KL(s)

KL trên bộ đệm:   D̂_KL = (1/N) Σₜ D_KL(Sₜ)

Khuyến nghị bổ sung một hình hai cột với cùng các giá trị KL(s), nhưng trọng số theo độ chiếm dụng có chiết khấu ở cột thứ nhất và tần suất xuất hiện trên mẫu ở cột thứ hai. Trong ví dụ, tổng trọng số νᵖⁱ(s) = 0,145 (không bằng 1) là chi tiết nên giải thích rõ về quy ước chuẩn hóa.
4. Đánh giá theo tiêu chí sư phạm
 [IMG rId12]
Hình 2. Điểm đánh giá chủ quan trên thang 10, dựa trên cấu trúc và hình minh họa ở website.
Các điểm mạnh nằm ở trực giác và sự liên kết giữa ví dụ với toán học. Hai nội dung còn dư địa cải thiện là cân bằng chứng minh với mạch giảng và chuyển tiếp từ bài toán lý thuyết sang triển khai thuật toán.
5. Kết luận và thứ tự triển khai
Không cần viết lại toàn bộ phần 4. Bản sửa hiện tại đã giúp sinh viên nhìn thấy logic hình thành TRPO: vấn đề bước cập nhật → surrogate → sai số do occupancy → giới hạn KL → natural gradient → line search. Nên tinh chỉnh các chỗ chuyển tiếp hơn là tiếp tục bổ sung kiến thức.
Nếu chỉ thực hiện ba thay đổi trong vòng chỉnh sửa tiếp theo, đề nghị ưu tiên:
1. Sửa các câu dễ gây hiểu nhầm về bảo đảm J không giảm.
2. Đưa sơ đồ thuật toán tổng thể lên ngay sau phát biểu bài toán miền tin cậy.
3. Tách các chứng minh dài sang các slide phụ để giữ nhịp giảng chính.

Thông điệp cuối: TRPO không chỉ là Policy Gradient với bước nhỏ. TRPO dùng một mô hình dự báo hiệu năng từ dữ liệu cũ, giới hạn miền tin cậy của mô hình này, rồi tìm bước cập nhật tốt nhất trong miền đó.
Nguồn đối chiếu: https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-10-trpo-va-ppo.html#/4```
