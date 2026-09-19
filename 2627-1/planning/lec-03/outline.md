# Bài 03 — Dàn ý triển khai

Trạng thái: đã triển khai phần 1–3/7 theo [kế hoạch chi tiết](detailed-slide-plan.md). Các phần sau vẫn là nội dung cũ cho đến lượt thay thế tương ứng.

## Mục tiêu và phạm vi

Sinh viên năm 3 đã học học máy, học sâu, xác suất và thuật toán; đã học Bài 02 về trạng thái, quan sát, chính sách, tổng thưởng và mô hình chuyển. Sau Bài 03, sinh viên có thể đọc một mô hình hữu hạn, suy ra phương trình giá trị và đánh giá một chính sách cố định.

- 47 slide, gồm 1 slide tiêu đề bài, 1 slide nội dung bài học, 7 slide mở phần và 7 slide câu hỏi kiểm tra; 120 phút trình bày và hoạt động ngắn trong lớp.
- 30 phút chữa bài tập nguồn, tách khỏi 120 phút. Không tạo code demo mới.
- Toàn bài mở bằng slide tiêu đề “Quá trình quyết định Markov”, tiếp theo là slide “Nội dung bài học”; cả hai nằm trong phần 1. Sau đó mới đến slide mở phần “Từ tương tác đến mô hình xác suất” và các slide còn lại của phần 1. Các phần 2–7 bắt đầu ngay bằng slide tiêu đề phần. Slide mở phần có một hình gợi tình huống và tối đa một câu dẫn, không có danh sách công thức.
- Mỗi khái niệm mới đi từ vấn đề, ví dụ trực quan và phép tính cụ thể tới định nghĩa/công thức; sau đó vận dụng và kiểm tra. Các trường hợp rút gọn được ghi ở từng phần.
- Giữ giả thiết mô hình đã biết, hữu hạn và không đổi theo thời gian. Tính Markov và tính không đổi theo thời gian là hai giả thiết riêng. Quan sát đầy đủ không đồng nghĩa biết mô hình.
- Tập trung Bellman kỳ vọng; Bellman tối ưu, lặp giá trị và lặp chính sách thuộc Bài 04.
- Khi triển khai: dùng `lecture-slide.css`, RevealJS cục bộ, SVG có nhãn và mô tả thay thế, KaTeX cho công thức. Chỉ đưa nội dung học thuật và mạch nói vào HTML/notes; các hướng dẫn dựng hình, thời lượng và ID trong tài liệu này là thông tin nội bộ.

## Nguồn và cách sử dụng

1. **Nguồn chính:** `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 28–58. Giữ tuyến chuỗi Markov → quá trình phần thưởng Markov → Bellman → MDP → Bellman kỳ vọng. Bài tập: `RL-hk2-2025-2026/resources/hw02.pdf`, bài 3, 4, 7, 8.
2. [David Silver, Lecture 2: Markov Decision Processes](https://web.stanford.edu/class/cme241/lecture_slides/david_silver_slides/MDP.pdf): ví dụ sinh viên và sơ đồ nhìn trước một bước; trang PDF 7–9, 10–23, 24–34. Không lấy phần tối ưu và các mở rộng ngoài phạm vi.
3. [Berkeley CS188, Fall 2025, Lecture 8](https://inst.eecs.berkeley.edu/~cs188/fa25/assets/lectures/cs188-fa25-lec08.pdf): cách phân biệt nút hành động/nút ngẫu nhiên, ví dụ xe đua; trang PDF 20–22. Không sao chép CSS hoặc tài sản.
4. [Stanford CS234, ghi chú Lecture 2 của Rahul Sarkar và Emma Brunskill](https://web.stanford.edu/~rsarkar/materials/lecture2-CS234.pdf): kiểm tra giả thiết, chuyển từ đồ thị sang ma trận và đánh giá khi biết mô hình. Đây là ghi chú bài giảng, không phải bộ slide để sao chép bố cục.

Ví dụ sinh viên là mạch chính. Bài tập ba trạng thái là ví dụ tính toán nhỏ để giải hệ; xe đua là bài vận dụng chuyển sang tình huống khác. Không thêm một ví dụ lớn thứ ba. Mọi xác suất và thưởng giữ theo nguồn; quy ước xe quá nhiệt nhận -10, không cộng thêm +2, được nêu rõ trước khi tính.

## Phân bổ

| Phần | Tiêu đề mở phần | Slide | Phút |
|---|---|---:|---:|
| 1 | Từ tương tác đến mô hình xác suất | 6 | 8 |
| 2 | Chuỗi Markov | 6 | 18 |
| 3 | Quá trình phần thưởng Markov | 6 | 18 |
| 4 | Phương trình Bellman | 9 | 24 |
| 5 | MDP và chính sách cố định | 7 | 20 |
| 6 | Giá trị trạng thái và giá trị hành động | 9 | 24 |
| 7 | Tổng hợp và vận dụng | 4 | 8 |
| **Tổng** | | **47** | **120** |

47 slide nhiều hơn ước lượng ban đầu 36–40 vì có slide tiêu đề bài, slide nội dung bài học, 7 trang mở phần và các bước suy diễn được tách riêng. Không tăng số khái niệm hoặc thời lượng. Phần 4 và 6 dành tổng 48 phút cho Bellman; các slide mở phần chỉ 1 phút. Phần 1 có sáu slide trong 8 phút: 1 + 1 + 1 + 2 + 1 + 2.

## Ký hiệu và thứ tự xuất hiện

| Ký hiệu/khái niệm | Nơi xuất hiện chính thức | Chuẩn bị bằng ví dụ |
|---|---|---|
| Trạng thái, Markov, tổng thưởng, chính sách | Đã có ở Bài 02; chỉ nhắc ngắn | 01-04 |
| $P_{ij}$, ma trận chuyển | 02-03 | Các cạnh ra ở 02-02 |
| Phân phối trạng thái $\mu_t$ | 02-05 | Dồn xác suất theo các cạnh bằng số trước |
| Thưởng trung bình $r(s)$, quá trình phần thưởng Markov (MRP) | 03-03 | Gắn thưởng vào bước chuyển ở 03-02 |
| $G_t$ và $v(s)$ của MRP | 03-04/05 | Hai quỹ đạo với tổng khác nhau |
| Bellman, dạng hệ tuyến tính | 04-03…07 | Nhánh một bước ở 04-02 |
| Quá trình quyết định Markov (MDP), $P(s',r\mid s,a)$ | 05-03 | Lựa chọn học/nghỉ ở 05-02 |
| $P^\pi,r^\pi$ | 05-06 | Gộp nút hành động trên hình ở 05-05 |
| $q_\pi(s,a)$ | 06-03 | So sánh hai hành động đầu tiên ở 06-02 |
| Bellman kỳ vọng theo $v_\pi,q_\pi$ | 06-04…07 | Cùng sơ đồ trạng thái → hành động → phản hồi |

$P$ trong chuỗi Markov là ma trận; $P(s',r\mid s,a)$ trong MDP là xác suất chung, tiếp nối ký hiệu Bài 02. $r(s)$ và $r^\pi(s)$ là kỳ vọng của phần thưởng, khác biến ngẫu nhiên $R_{t+1}$. Dùng véc-tơ cột cho $v,r,\mu$; do P chuẩn hóa theo hàng, $\mu_{t+1}=P^{\mathsf T}\mu_t$. Xét chính sách Markov dừng khi viết giá trị không có chỉ số thời gian; không khẳng định mọi chính sách đều thuộc lớp này.


## Phần 1

- `L03-01-01`: Quá trình quyết định Markov.
- `L03-01-02`: Nội dung bài học.
- `L03-01-03`: Từ tương tác đến mô hình xác suất.
- `L03-01-04`: Một mô hình, nhiều quỹ đạo.
- `L03-01-05`: Ba lớp mô hình.
- `L03-01-06`: Câu hỏi kiểm tra.

## Phần 2

- `L03-02-01`: Chuỗi Markov.
- `L03-02-02`: Một ngày của sinh viên.
- `L03-02-03`: Xác suất chuyển và tính Markov.
- `L03-02-04`: Từ đồ thị đến ma trận chuyển.
- `L03-02-05`: Phân phối sau một bước.
- `L03-02-06`: Câu hỏi kiểm tra.

## Phần 3

- `L03-03-01`: Quá trình phần thưởng Markov.
- `L03-03-02`: Phần thưởng trên từng bước.
- `L03-03-03`: Định nghĩa quá trình phần thưởng Markov.
- `L03-03-04`: Hai quỹ đạo, hai tổng thưởng.
- `L03-03-05`: Giá trị của một trạng thái.
- `L03-03-06`: Câu hỏi kiểm tra.
