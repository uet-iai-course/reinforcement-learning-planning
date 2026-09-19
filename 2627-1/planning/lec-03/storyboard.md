# Bài 03 — Storyboard triển khai

Đã triển khai phần 1–1/7. Bảy phần và 120 phút theo [kế hoạch chi tiết](detailed-slide-plan.md); bản này ghi quyết định thể hiện thực tế. Các phần chưa triển khai dùng bản HTML cũ, không được tính là hoàn tất.

## Phần 1. Từ tương tác đến mô hình xác suất — 8 phút

Đầu vào: giao diện tác tử–môi trường ở Bài 02. Đầu ra: nhu cầu mô tả quy luật sinh các quỹ đạo và tính giá trị bằng mô hình. Đây là phần mở đầu, chỉ ôn và đặt vấn đề; định nghĩa mới nằm ở các phần sau.


### L03-01-01 — Quá trình quyết định Markov

Thời lượng: 1 phút. Vai trò: tiêu đề bài giảng.

**Đầu vào:** Bài 02 đã giới thiệu giao diện tác tử–môi trường và các thành phần của bài toán.

**Nội dung trên slide:** “Quá trình quyết định Markov”; “Bài 03 · Học tăng cường”; học kỳ 1, năm học 2026–2027; Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội.

**Cách thể hiện:** Trang tiêu đề theo mẫu và CSS chung; tên bài là nội dung lớn nhất. Không dùng tiêu đề phần 1 thay cho tên bài.

**Giải thích và hình thức hóa:** Giới thiệu mục tiêu bằng lời: từ mô hình đã biết và chính sách cố định, tính giá trị dài hạn. Chưa có công thức mới.

**Kết nối:** Sang bản đồ nội dung toàn bài.

**Kiểm tra/ghi chú đáp án:** Không đặt câu hỏi tại trang tiêu đề.

**Nguồn:** PPTX28; thông tin học phần.

**Quyết định thể hiện khi triển khai:** Trang tiêu đề chỉ đặt tên bài và thông tin học phần, không có công thức mới vì đây là điểm vào của toàn bài; mục tiêu nằm trong notes. Không dùng hình trực giác để tránh lặp với slide mở phần ngay sau đó. Tiên quyết: Bài 02 (giao diện tác tử–môi trường, tổng thưởng). Cầu nối: slide nội dung bài học.

### L03-01-02 — Nội dung bài học

Thời lượng: 1 phút. Vai trò: định hướng toàn bài.

**Đầu vào:** Tên và mục tiêu Bài 03.

**Nội dung trên slide:** Bảy phần theo thứ tự: 1. Từ tương tác đến mô hình xác suất; 2. Chuỗi Markov; 3. Quá trình phần thưởng Markov; 4. Phương trình Bellman; 5. MDP và chính sách cố định; 6. Giá trị trạng thái và giá trị hành động; 7. Tổng hợp và vận dụng.

**Cách thể hiện:** Danh sách hai cột hoặc sơ đồ bảy mục, đánh dấu phần 1. Không hiện thời lượng, ID hoặc chỉ dẫn tác giả.

**Giải thích và hình thức hóa:** Các tên gọi mới chỉ xuất hiện như tên nội dung, chưa yêu cầu sinh viên hiểu định nghĩa. Khi nói, diễn đạt mạch bằng lời: mô tả chuyển tiếp, thêm thưởng, đánh giá tương lai, rồi xét lựa chọn hành động. “Quá trình quyết định Markov (MDP)” được viết đầy đủ trong mục 5 khi dựng slide.

**Kết nối:** Sang slide mở phần 1, rồi ví dụ một mô hình sinh nhiều quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Không thêm kiểm tra tại trang nội dung; phần 1 kết thúc bằng câu hỏi riêng.

**Nguồn:** Dàn ý bảy phần đã được thống nhất; PPTX28–58.

**Quyết định thể hiện khi triển khai:** Danh sách hai cột giúp bảy mục vừa khung 1280x720 mà không cần hình; mục 1 được nhấn mạnh để sinh viên biết vị trí hiện tại. Thứ tự mục chính là bản đồ khái niệm: mỗi lớp mô hình là mở rộng của lớp trước, nên thứ tự đọc cũng là thứ tự xây dựng. Không hiện thời lượng hay ID vì đó là thông tin điều hành, không phải nội dung học.

### L03-01-03 — Từ tương tác đến mô hình xác suất

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** Bản đồ bài học ở 01-02 và giao diện tác tử–môi trường từ Bài02.

**Nội dung trên slide:** Tiêu đề phần và câu: “Cùng trạng thái và hành động có thể cho kết quả khác nhau.”

**Cách thể hiện:** Một nút hiện tại, một hành động và hai kết quả; chưa đặt bộ ký hiệu MDP.

**Giải thích và hình thức hóa:** Nhắc lại vòng tương tác bằng lời; bài này giả sử đã biết xác suất chuyển.

**Kết nối:** Từ một bước tương tác sang nhiều khả năng diễn tiến.

**Kiểm tra/ghi chú đáp án:** Không đặt câu hỏi riêng trên trang mở.

**Nguồn:** PPTX 28–29; nối Bài 02.

**Quyết định thể hiện khi triển khai:** Hình trực giác gồm một nút trạng thái, một nút hành động và hai nút trạng thái kế tiếp với hai mũi tên, thể hiện đúng luận điểm duy nhất của slide: một bước tương tác có nhiều khả năng diễn tiến. Hai nhãn trạng thái 1 và trạng thái 2 phân biệt hai kết quả khác nhau. Chưa dùng bộ ký hiệu MDP để không vượt trước định nghĩa ở phần 5. Tiên quyết: giao diện tác tử–môi trường Bài 02. Cầu nối: slide sau cho thấy nhiều quỹ đạo sinh ra từ chính tính ngẫu nhiên này.

### L03-01-04 — Một mô hình, nhiều quỹ đạo

Thời lượng: 2 phút. Vai trò: vấn đề và trực giác.

**Đầu vào:** Một bước có thể có nhiều kết quả; trạng thái quan sát được.

**Nội dung trên slide:** Hai đường đi từ cùng điểm xuất phát trên đồ thị sinh viên.

**Cách thể hiện:** Chỉ hiện các nút liên quan đến hai đường; cùng điểm xuất phát và cùng kết thúc Sleep, hai diễn tiến khác nhau.

**Giải thích và hình thức hóa:** Quỹ đạo là một kết quả lấy mẫu. Mô hình là quy luật sinh ra cả các quỹ đạo chưa quan sát; chưa đồng nhất hai tổng cụ thể với kỳ vọng.

**Kết nối:** Từ sự khác nhau của đường đi đến việc phải dùng phân phối.

**Kiểm tra/ghi chú đáp án:** Một đường quan sát được có xác định hết xác suất chuyển không? Không.

**Nguồn:** PPTX 31–32.

**Quyết định thể hiện khi triển khai:** Hình vẽ hai hàng quỹ đạo riêng biệt, cùng xuất phát từ C1 và cùng kết thúc ở Sleep, mỗi hàng có nhãn Đường 1/Đường 2 để sinh viên đọc được ngay luận điểm: cùng điểm đầu, nhiều diễn tiến. Hai quỹ đạo là các đường hợp lệ suy ra từ đồ thị, không phải hai kết thúc khác nhau. Chỉ hiện các nút liên quan, đúng yêu cầu của kế hoạch. Đây là bước vấn đề–trực giác trước khi đưa vào phân phối ở phần 2; chưa tính tổng thưởng để không trộn với phần 3. Tiên quyết: khái niệm trạng thái và quỹ đạo từ Bài 02. Cầu nối: cần một cách mô tả gọn quy luật sinh mọi quỹ đạo — đó là ba lớp mô hình ở slide sau.

### L03-01-05 — Ba lớp mô hình

Thời lượng: 1 phút. Vai trò: bản đồ khái niệm.

**Đầu vào:** Hai quỹ đạo từ cùng điểm đầu; nhu cầu mô tả quy luật sinh chúng.

**Nội dung trên slide:** Chuỗi trạng thái → thêm thưởng → thêm lựa chọn hành động.

**Cách thể hiện:** Ba hình dùng cùng các nút; lần lượt thêm nhãn thưởng và nút lựa chọn.

**Giải thích và hình thức hóa:** Gọi đầy đủ ba tên bằng tiếng Việt; chưa yêu cầu ghi nhớ các bộ thành phần hoặc viết tắt.

**Kết nối:** Phần 2 bắt đầu bằng lớp đơn giản nhất.

**Kiểm tra/ghi chú đáp án:** Đầu ra cần đạt cuối bài: từ mô hình và chính sách viết được phương trình giá trị.

**Nguồn:** PPTX 30,34,49.

**Quyết định thể hiện khi triển khai:** Ba hàng của hình dùng cùng hai trạng thái A và B: hàng một chỉ có chuyển tiếp, hàng hai thêm nhãn thưởng trên phản hồi, hàng ba thêm hai lựa chọn hành động a và b trước khi về B, vẫn giữ nhãn thưởng — trực quan thể hiện quan hệ bao chứa giữa ba lớp mà không mất phần thưởng khi thêm hành động. Nhãn tiếng Việt đủ ba lớp, không công thức, vì slide chỉ làm bản đồ khái niệm. Tiên quyết: hai quỹ đạo từ cùng điểm đầu ở slide trước cho thấy cần mô hình hóa quy luật. Cầu nối: phần 2 bắt đầu bằng lớp đơn giản nhất, chuỗi Markov.

### L03-01-06 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: kiểm tra tiên quyết.

**Đầu vào:** Phân biệt trạng thái, mô hình và một mẫu quỹ đạo.

**Nội dung trên slide:** 1. Quan sát đúng trạng thái có đồng nghĩa biết xác suất chuyển không?
2. Cùng trạng thái có thể dẫn tới các trạng thái kế tiếp khác nhau không?

**Cách thể hiện:** Hai câu đánh số, đáp án trong notes.

**Giải thích và hình thức hóa:** Chỉ kiểm tra những khái niệm đã có, chưa hỏi ma trận hay Bellman.

**Kết nối:** Từ phân biệt trạng thái và mô hình sang đọc đồ thị chuyển.

**Kiểm tra/ghi chú đáp án:** 1. Không. 2. Có, nếu chuyển ngẫu nhiên.

**Nguồn:** Bài 02; PPTX 29–30.

**Quyết định thể hiện khi triển khai:** Hai câu trong danh sách đánh số dưới một nhãn Câu hỏi chung; đáp án nằm trọn trong notes để slide chỉ giữ câu hỏi. Câu 1 tách quan sát khỏi mô hình, câu 2 khẳng định tính ngẫu nhiên — đúng hai phân biệt mà phần 1 đặt ra. Không dùng hình vì hai câu đủ tự đứng và slide kiểm tra cần gọn. Tiên quyết: slide 01-03 và 01-04. Cầu nối: sang phần 2, đọc đồ thị chuyển.
