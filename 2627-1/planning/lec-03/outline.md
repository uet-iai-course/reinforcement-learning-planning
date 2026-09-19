# Bài 03 — Dàn ý triển khai

Trạng thái: đã viết lại và kiểm định đủ 47 slide thuộc 7 phần theo [kế hoạch chi tiết](detailed-slide-plan.md); kiểm định cuối ghi trong review-log.md.

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
| Quá trình quyết định Markov (MDP), $p(s',r\mid s,a)$ | 05-03 | Lựa chọn học/nghỉ ở 05-02 |
| $P^\pi,r^\pi$ | 05-06 | Gộp nút hành động trên hình ở 05-05 |
| $q_\pi(s,a)$ | 06-03 | So sánh hai hành động đầu tiên ở 06-02 |
| Bellman kỳ vọng theo $v_\pi,q_\pi$ | 06-04…07 | Cùng sơ đồ trạng thái → hành động → phản hồi |

$P$ trong chuỗi Markov là ma trận; $p(s',r\mid s,a)$ trong MDP là xác suất chung, tương ứng với ký hiệu $P(s',r\mid s,a)$ ở Bài 02. $r(s)$ và $r^\pi(s)$ là kỳ vọng của phần thưởng, khác biến ngẫu nhiên $R_{t+1}$. Dùng véc-tơ cột cho $v,r,\mu$; do P chuẩn hóa theo hàng, $\mu_{t+1}=P^{\mathsf T}\mu_t$. Xét chính sách Markov dừng khi viết giá trị không có chỉ số thời gian; không khẳng định mọi chính sách đều thuộc lớp này.


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

## Phần 4

- `L03-04-01`: Phương trình Bellman.
- `L03-04-02`: Một bước và phần còn lại.
- `L03-04-03`: Tách phần thưởng tích lũy.
- `L03-04-04`: Từ tổng thưởng đến giá trị.
- `L03-04-05`: Bellman cho quá trình phần thưởng Markov.
- `L03-04-06`: Hệ Bellman ba trạng thái.
- `L03-04-07`: Dạng ma trận và nghiệm.
- `L03-04-08`: Điều kiện để giá trị hữu hạn.
- `L03-04-09`: Câu hỏi kiểm tra.

## Phần 5

- `L03-05-01`: MDP và chính sách cố định.
- `L03-05-02`: Lựa chọn làm thay đổi phản hồi.
- `L03-05-03`: Quá trình quyết định Markov.
- `L03-05-04`: Cố định một chính sách.
- `L03-05-05`: Từ MDP đến quá trình phần thưởng Markov.
- `L03-05-06`: Mô hình dưới chính sách.
- `L03-05-07`: Câu hỏi kiểm tra.

## Phần 6

- `L03-06-01`: Giá trị trạng thái và giá trị hành động.
- `L03-06-02`: Ấn định hành động đầu tiên.
- `L03-06-03`: Định nghĩa giá trị hành động.
- `L03-06-04`: Từ giá trị hành động đến giá trị trạng thái.
- `L03-06-05`: Giá trị hành động từ phản hồi một bước.
- `L03-06-06`: Bellman kỳ vọng cho giá trị hành động.
- `L03-06-07`: Bellman kỳ vọng cho giá trị trạng thái.
- `L03-06-08`: Vận dụng với xe đua.
- `L03-06-09`: Câu hỏi kiểm tra.

## Phần 7

- `L03-07-01`: Tổng hợp và vận dụng.
- `L03-07-02`: Từ mô hình đến phương trình giá trị.
- `L03-07-03`: Bài tập và bước tiếp theo.
- `L03-07-04`: Câu hỏi kiểm tra.

## Ánh xạ từng trang nguồn

Nguồn chính: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`. Bảng này ghi ánh xạ của bản triển khai; các ví dụ số bổ sung được phân biệt với số liệu nguyên bản.

| Trang nguồn | Slide đích | Quyết định và lý do |
|---:|---|---|
| 28 | L03-01-01…03 | Tách tiêu đề bài, nội dung bài học và mở phần theo yêu cầu người dùng. |
| 29 | L03-01-03/06, L03-02-03 | Rút gọn ôn Markov; phân biệt quan sát đầy đủ với biết mô hình. |
| 30 | L03-02-03 | Giữ định nghĩa chuỗi; bổ sung rõ giả thiết đồng nhất theo thời gian. |
| 31 | L03-02-01/02 | Vẽ lại đồ thị sinh viên, giữ bảy trạng thái và xác suất. |
| 32 | L03-01-04, L03-02-02 | Giữ quỹ đạo nguồn trong02-02; bổ sung hai đường đi ở01-04 để nối sang các ví dụ tổng thưởng. |
| 33 | L03-02-04/05 | Giữ toàn ma trận; thêm phép truyền phân phối và ví dụ trộn tạiC1/FB. |
| 34 | L03-03-02/03 | Đưa ví dụ thưởng trước định nghĩa MRP; phân biệt biến thưởng và kỳ vọng thưởng. |
| 35 | L03-03-01/02, L03-04-02 | Vẽ lại đồ thị có thưởng; dùng nhánhC3 để chuẩn bị Bellman. |
| 36 | L03-03-03/04 | Giữ tổng có chiết khấu và miềngamma; tính hai tổng quỹ đạo. |
| 37 | L03-03-03, L03-04-08 | Gộp phần giải thích chiết khấu với định nghĩa và điều kiện hữu hạn; nội dung động cơ đã học ởBài02. |
| 38 | L03-03-04, L03-04-08 | Gộp ảnh hưởng chiết khấu vào phép tính và cận tổng hình học; không lặp phần thưởng–mục tiêu củaBài02. |
| 39 | L03-03-05 | Giữ định nghĩa giá trị, đặt sau ví dụ hai tổng khác nhau. |
| 40 | L03-03-04/06 | Giữ hai quỹ đạo vàgamma=1/2; tự tính lại tổng−2,25 và−3,125. |
| 41 | L03-03-03/05, L03-04-08 | Gộp trường hợpgamma=0 vào định nghĩa/cận; không chép bảng giá trị bảy trạng thái. |
| 42 | L03-04-06/07 | Thay bảng nghiệm bảy trạng thái bằng hệ ba trạng thái từhw02 để sinh viên tự giải được; giữgamma=0,9. |
| 43 | L03-04-08, L03-06-08 | Gộp trường hợpgamma=1 vào điều kiện kết thúc; vận dụng trên xeđua thay vì chép bảng nghiệm sinh viên. |
| 44 | L03-04-01…04 | Tách trực giác, tổng thưởng và kỳ vọng lặp; nêu lý do từng dấu bằng. |
| 45 | L03-04-05 | Giữ Bellman MRP; chỉ rõ bước dùng Markov và đồng nhất thời gian. |
| 46 | L03-04-02/05 | Giữ quan hệ một bước quaPass/Pub; không gán thưởng một bước thành giá trị dài hạn. |
| 47 | L03-04-06/07 | Giữ dạng ma trận; bổ sung hệ và nghiệm từhw02 bài3. |
| 48 | L03-04-07/08 | Giữ giải hệ, chi phí bậc ba và giới hạn; thêm điều kiện khả nghịch, xử lý trạng thái kết thúc. |
| 49 | L03-05-01/03 | Giữ MDP hữu hạn; dùng xác suất chung trạng thái–thưởng nhất quán Bài02. |
| 50 | L03-05-01/02/04/05, L03-06-01/02 | Vẽ lại StudentMDP năm trạng thái; giữ thưởng/cạnh; nêu thay đổi so vớiMRP bảy trạng thái. |
| 51 | L03-06-08/09 | Chuyển ví dụ xeđua tới phần vận dụng; giữ sáu kết quả và quy ước quá nhiệt nhận−10. |
| 52 | L03-05-04/06/07 | Giữ chính sách; thêm phép gộp MDP dưới chính sách bằng số rồi công thức. |
| 53 | L03-06-01…04 | Đưa hai thí nghiệm hành động đầu trước định nghĩa v/q; nêu quy ước hành động có xác suất chính sách bằng0. |
| 54 | L03-05-04/05 | Thay bảng giá trị có sẵn bằng phép gộp tạiC2; xác suất0,75/0,25 được ghi là ví dụ luyện thêm, không nhận là số liệu gốc. |
| 55 | L03-06-08/09 | Giữ chính sách đều, gamma=1 và giá trị xeđua; tính q và kiểm lại v. |
| 56 | L03-06-04…06 | Tách kỳ vọng theo hành động, phản hồi môi trường và hành động tiếp theo. |
| 57 | L03-06-05…07 | Giữ Bellman kỳ vọng; nối lại dạngMRP cảm sinh để tránh hai hệ công thức rời nhau. |
| 58 | L03-07-03/04 | Giữ bài tập/đọc thêm; phần tối ưu nối sangBài04, không dạy thuật toán mới trong kết bài. |

Bài tập `resources/hw02.pdf`: bài3 → L03-02-06, L03-04-06/07/09; bài4 → L03-05-05…07, L03-06-07; bài7 → L03-06-04/09; bài8 → L03-06-05…07. L03-07-03 tập hợp các bài này cho 30 phút luyện tập. Không tạo code demo mới.

## Nguồn chuẩn cho công thức — Sutton và Barto

Theo yêu cầu bổ sung ngày 20-09-2026, định nghĩa và phương trình Học tăng cường được đối chiếu với Richard S. Sutton và Andrew G. Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, chương 3. Bản PDF đã đọc là bản 2018/2020 do [DTU lưu](https://www2.imm.dtu.dk/courses/02465/pensum/sutton2018.pdf); số trang dưới đây là số in trong sách, không phải số trang của trình xem PDF.

| Nội dung | Nguồn trong sách | Slide và cách dùng |
|---|---|---|
| Hạt nhân $p(s',r\mid s,a)$ và chuẩn hóa | (3.2)–(3.3), tr.48–49 | 05-03; đổi chỉ số $t-1,t$ thành $t,t+1$ để khớp vòng tương tác. |
| Xác suất chuyển và thưởng kỳ vọng | (3.4)–(3.5), tr.49 | 03-03 và 05-05/06; MRP là trường hợp không còn lựa chọn hành động, hoặc đã lấy trung bình theo chính sách. |
| Tổng thưởng có chiết khấu | (3.8), tr.55; quy ước kết thúc ở mục 3.4, tr.57 | 03-04 và mọi ví dụ số; giữ thưởng 0 sau kết thúc. |
| Tách tổng thưởng | (3.9), tr.55 | 04-03, giữ đầy đủ ba bước biến đổi. |
| Giá trị trạng thái, giá trị hành động | (3.12)–(3.13), tr.58 | 03-05 là trường hợp MRP; 06-03 dùng định nghĩa dưới chính sách. |
| Giá trị trạng thái theo giá trị hành động | Bài tập 3.12, tr.58; 3.18, tr.62 | 06-04, suy diễn bằng kỳ vọng toàn phần. |
| Giá trị hành động theo phản hồi và giá trị trạng thái | Bài tập 3.13, tr.58; 3.19, tr.62 | 06-05, suy diễn từ tổng thưởng và hạt nhân chung. |
| Bellman kỳ vọng cho giá trị hành động | Bài tập 3.17, tr.61 | 06-06 là lời giải có suy diễn; không gọi đây là phương trình (3.17). |
| Bellman kỳ vọng cho giá trị trạng thái | (3.14), tr.59 | 06-07; 04-04/05 là trường hợp MRP; dạng ma trận ở 04-07 và 05-06 suy ra bằng gom các phương trình. |
| Giá trị hữu hạn | Đoạn sau (3.8), tr.55; mục 3.4, tr.57 | 04-08; cận trị tuyệt đối và điều kiện kỳ vọng thời gian kết thúc hữu hạn là phần giải thích toán học bổ sung, không gán số phương trình của sách. |

Dùng $p$ thường cho hạt nhân xác suất như sách, còn $P$ hoa cho ma trận chuyển của chuỗi và $P^\pi$ cho ma trận cảm sinh. $p$ ở đây tương ứng ký hiệu $P(s',r\mid s,a)$ đã dùng trong Bài 02. Trong bài này, $\mathcal S$ bao gồm cả trạng thái kết thúc; nó tương ứng $\mathcal S^+$ của sách khi xét bài toán có lượt. $v(\text{kết thúc})=v_\pi(\text{kết thúc})=0$.

Các đồ thị sinh viên, xe đua và bài tập số vẫn lấy từ nguồn slide đã chọn. Không gán các ví dụ đó cho Sutton–Barto. Những công thức MRP, lấy trung bình theo chính sách và dạng ma trận được ghi rõ là trường hợp riêng hoặc suy ra từ công thức trong sách.
