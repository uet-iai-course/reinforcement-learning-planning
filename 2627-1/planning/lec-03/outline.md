# Dàn ý triển khai — Bài 03: Quá trình quyết định Markov

Đã triển khai 4/7 phần (28/50 slide) theo storyboard robot. Thiết kế đầy đủ:120 phút; 30 phút chữa hw02. Đối tượng: sinh viên năm3 đã học xác suất, đại số tuyến tính, học máy và Bài02.

## 1. Đích học tập và quyết định về cấu trúc

Sinh viên năm 3 đã học xác suất, kỳ vọng có điều kiện, đại số tuyến tính và Bài 02. Sau bài này, sinh viên phải tự làm được bốn việc: mô tả một bài toán bằng MDP; phân biệt quy luật môi trường với chính sách; suy ra Bellman từ tổng thưởng; dùng mô hình và chính sách đã cho để lập, giải và kiểm tra một hệ giá trị nhỏ.

Tuyến mới lấy **robot thu gom lon** trong ví dụ 3.3 của Sutton và Barto làm ví dụ xuyên suốt. Trạng thái, hành động, xác suất, phần thưởng, chính sách và giá trị đều thuộc cùng một mô hình hai trạng thái. Sinh viên không phải chuyển giữa hai đồ thị sinh viên có đặc tả khác nhau trong lúc học ký hiệu.

MDP xuất hiện ngay sau bài toán tương tác. Chuỗi Markov và quá trình phần thưởng Markov (MRP) được nhận diện sau khi cố định chính sách: chúng giải thích phép rút gọn mô hình để tính giá trị. Thứ tự này gần mạch chương 3 của giáo trình: tương tác và động lực → mục tiêu và tổng thưởng → chính sách và giá trị → Bellman. Đây là thay đổi cấu trúc có chủ ý, không chỉ sửa câu chữ của bản cũ.

| Phần | Mạch chính | Đầu vào từ phần trước | Sản phẩm chuyển sang phần sau | Slide | Phút |
|---|---|---|---|---:|---:|
| 1 | Từ tương tác đến trạng thái Markov | Giao diện tác tử–môi trường ở Bài 02 | Biết một bước gồm gì và trạng thái cần giữ thông tin nào | 7 | 12 |
| 2 | Mô hình xác suất của MDP | Trạng thái, hành động, phản hồi cùng một bước | Đọc và viết được $p(s',r\mid s,a)$, thưởng trung bình | 7 | 18 |
| 3 | Phần thưởng và tổng thưởng | Quy luật phản hồi một bước | Tính và giải thích $G_t$, $\gamma$, kết thúc và tính hữu hạn | 6 | 14 |
| 4 | Chính sách và hàm giá trị | Mô hình và tiêu chuẩn tổng thưởng | Phân biệt $\pi$, $G_t$, $v_\pi$, $q_\pi$ | 8 | 17 |
| 5 | Phương trình Bellman | Các định nghĩa giá trị và kỳ vọng có điều kiện | Giải thích được từng dấu bằng và từng tầng lấy trung bình | 10 | 30 |
| 6 | Đánh giá một chính sách từ mô hình | Bellman cho một chính sách cố định | Giải hệ robot; suy ra chuỗi Markov, MRP và dạng ma trận | 8 | 21 |
| 7 | Tổng hợp và vận dụng | Mô hình, chính sách, giá trị đã tính | Nối dữ kiện với công thức, kiểm giới hạn và chuẩn bị Bài 04 | 4 | 8 |
| **Tổng** | | | | **50** | **120** |

30 phút còn lại dùng chữa bài tập nguồn, phân bổ ở cuối storyboard. Không thêm code demo. 50 slide gồm một slide tiêu đề bài, một slide nội dung, sáu slide tiêu đề phần và bảy slide câu hỏi kiểm tra. Các trang tiêu đề không chứa định nghĩa mới. Phần 1 bắt đầu bằng **“Quá trình quyết định Markov”**, tiếp theo là **“Nội dung bài học”**, rồi đi vào ví dụ; không chèn thêm trang tiêu đề phần 1. Phần 2–7 bắt đầu bằng đúng tên phần trong bảng.

## 2. Nguồn và quy ước xuyên suốt

Nguồn chuẩn, viết tắt **SB** trong các mục dưới: Richard S. Sutton và Andrew G. Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, chương 3; [bản PDF do DTU lưu](https://www2.imm.dtu.dk/courses/02465/pensum/sutton2018.pdf). Số trang là số in trong sách. Đã đọc nội dung liên quan và xem trực tiếp trang 52 để kiểm tra đồ thị, xác suất và thưởng của robot.

Nguồn học phần: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, slide 28–58; `RL-hk2-2025-2026/resources/hw02.pdf`. Các khái niệm chính của nguồn vẫn được giữ, nhưng đổi thứ tự và ví dụ theo yêu cầu lập lại kế hoạch. Phần Bellman tối ưu và các thuật toán giải MDP thuộc Bài 04.

| Nội dung | Nguồn chuẩn | Vị trí trong tuyến mới |
|---|---|---|
| Một bước và quỹ đạo | SB (3.1), tr.48 | Phần 1 |
| Hạt nhân chung và chuẩn hóa | SB (3.2)–(3.3), tr.48–49 | Phần 2 |
| Xác suất chuyển, thưởng trung bình | SB (3.4)–(3.5), tr.49 | Phần 2 |
| Trạng thái Markov | SB §3.1, tr.49 | Phần 1, nhắc tại phần 2 |
| Robot thu gom lon | SB ví dụ 3.3, tr.52–53 | Xuyên suốt; bản số hóa có giả thiết bổ sung bên dưới |
| Tổng thưởng, chiết khấu, kết thúc | SB (3.7)–(3.11), tr.54–57 | Phần 3; tách tổng ở phần 5 |
| Chính sách, giá trị trạng thái/hành động | SB §3.5, (3.12)–(3.13), tr.58 | Phần 4 |
| Bellman kỳ vọng cho $v_\pi$ | SB (3.14), tr.59 | Phần 5 |
| Quan hệ $v$–$q$, $q$–$v$ | SB bài tập 3.12–3.13, tr.58; 3.18–3.19, tr.62 | Phần 5 |
| Bellman kỳ vọng cho $q_\pi$ | SB **bài tập** 3.17, tr.61 | Phần 5; không gọi là phương trình (3.17) |
| MRP cảm sinh, hệ và ma trận | Hệ quả của các công thức trên; PPTX30,34,47–48,52; hw02 bài 3–4 | Phần 6 |

### Một đặc tả robot dùng cho mọi phép tính

- Trạng thái $\mathrm H$: pin cao; $\mathrm L$: pin thấp. Hành động Tìm, Chờ, Sạc; trong công thức viết $\mathrm{tim},\mathrm{cho},\mathrm{sac}$.
- $\mathcal A(\mathrm H)=\{\mathrm{tim},\mathrm{cho}\}$; $\mathcal A(\mathrm L)=\{\mathrm{tim},\mathrm{cho},\mathrm{sac}\}$. Robot pin cao không có hành động Sạc trong mô hình này.
- Bản số cho lớp chọn hai tham số xác suất của sách bằng $1/2$, thưởng tìm thành công bằng $2$, thưởng chờ bằng $1$, cứu hộ bằng $-3$, sạc chủ động bằng $0$. **Thêm giả thiết thưởng cố định trên từng nhánh** để xác định đầy đủ phân phối chung $p$. Sách cho thưởng kỳ vọng trên nhánh; chỉ biết kỳ vọng không đủ để xác định phân phối thưởng. Không ghi các con số do người soạn chọn thành số liệu thực nghiệm hoặc thông số nguyên văn của sách.
- Hết pin khi Tìm ở $\mathrm L$ dẫn tới cứu hộ, trở lại $\mathrm H$ và nhận $-3$ trong cùng một bước mô hình. Không cộng thêm thưởng tìm kiếm. Cứu hộ và Sạc đều đưa về pin cao nhưng có thưởng khác nhau. Cả hai không kết thúc nhiệm vụ.

| $s$ | $a$ | $s'$ | $r$ | $p(s',r\mid s,a)$ |
|---|---|---|---:|---:|
| H | Tìm | H | 2 | $1/2$ |
| H | Tìm | L | 2 | $1/2$ |
| H | Chờ | H | 1 | $1$ |
| L | Tìm | L | 2 | $1/2$ |
| L | Tìm | H | −3 | $1/2$ |
| L | Chờ | L | 1 | $1$ |
| L | Sạc | H | 0 | $1$ |

Các bộ còn lại có xác suất 0. $\mathcal R=\{-3,0,1,2\}$. Bảng này là dữ kiện kiểm soát của storyboard; sinh viên nhận nó từng bước ở phần 2.

Từ phần 4, dùng cùng một chính sách: tại H luôn Tìm; tại L chọn Chờ hoặc Sạc, mỗi hành động xác suất $1/2$. Những hành động khác có xác suất 0. Giữ $\gamma=1/2$. Chính sách này dùng để học cách **đánh giá**; không giả định nó tối ưu.

### Thứ tự đưa ký hiệu vào

| Ký hiệu | Được gọi tên/định nghĩa lần đầu | Dữ kiện có trước |
|---|---|---|
| $S_t,A_t,R_{t+1},S_{t+1}$ | 01-04 | Robot ở H, chọn Tìm, nhận điểm và đổi mức pin |
| $H_t$ và tính Markov | 01-06 | Hai lịch sử cùng kết thúc ở L tại 01-05 |
| $\mathcal S,\mathcal A(s),\mathcal R,p$ | 02-03/04 | Cây kết quả và bảng robot |
| $p(s'\mid s,a)$, $r(s,a)$ | 02-05 | Gộp hàng và lấy trung bình trên cùng bảng |
| $T,\mathcal S^+$ | 03-02/04 | Nhiệm vụ có kết thúc, đệm thưởng 0 |
| $\gamma,G_t$ | 03-03/04 | Hai dãy thưởng ngắn, trọng số $1,1/2,1/4$ |
| $\pi(a\mid s)$ | 04-03 | Bảng cách chọn hành động ở 04-02 |
| $G_0^{[2]}$ | 04-04 | Tổng thưởng của đúng hai bước đầu, chưa phải toàn tương lai |
| $v_\pi(s)$ | 04-05 | Trung bình có trọng số trên các nhánh cùng xuất phát |
| $q_\pi(s,a)$ | 04-07 | Thử ấn định hành động đầu rồi trở lại cùng chính sách |
| $v_H,v_L$ | 06-02 | Viết tắt $v_\pi(\mathrm H),v_\pi(\mathrm L)$ đã định nghĩa |
| $P^\pi,r^\pi$, chuỗi Markov, MRP | 06-05/06 | Gộp các nhánh dưới chính sách bằng số |
| $v,r^\pi\in\mathbb R^n$, $I$ | 06-07 | Hai phương trình đã giải, hai hàng chuyển đã tính |

Quy luật môi trường và chính sách được giả sử Markov, không đổi theo thời gian khi viết các giá trị không có chỉ số $t$. Tính Markov và tính không đổi theo thời gian là hai giả thiết khác nhau. $p$ thường chỉ hạt nhân; $P^\pi$ hoa chỉ ma trận. Chữ hoa chỉ biến ngẫu nhiên, chữ thường chỉ giá trị nhận được. $R_{t+1}$ là thưởng quan sát; $r(s,a)$ là kỳ vọng một bước; $G_t$ là tổng thưởng trên quỹ đạo. Điều kiện hữu hạn của kỳ vọng phải được nêu trước khi biến đổi Bellman.

## Danh sách slide đã triển khai

- `L03R-01-01`: Quá trình quyết định Markov.
- `L03R-01-02`: Nội dung bài học.
- `L03R-01-03`: Robot thu gom lon.
- `L03R-01-04`: Một bước tương tác.
- `L03R-01-05`: Hai lịch sử, cùng trạng thái hiện tại.
- `L03R-01-06`: Tính Markov.
- `L03R-01-07`: Câu hỏi kiểm tra.
- `L03R-02-01`: Mô hình xác suất của MDP.
- `L03R-02-02`: Hai phản hồi của hành động Tìm.
- `L03R-02-03`: Bảng phản hồi của robot.
- `L03R-02-04`: Xác suất chuyển trạng thái và phần thưởng.
- `L03R-02-05`: Xác suất chuyển và thưởng trung bình.
- `L03R-02-06`: Các thành phần của MDP.
- `L03R-02-07`: Câu hỏi kiểm tra.
- `L03R-03-01`: Phần thưởng và tổng thưởng.
- `L03R-03-02`: Nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn.
- `L03R-03-03`: Điểm thưởng ở các thời điểm.
- `L03R-03-04`: Tổng thưởng từ thời điểm hiện tại.
- `L03R-03-05`: Điều kiện để tổng thưởng hữu hạn.
- `L03R-03-06`: Câu hỏi kiểm tra.
- `L03R-04-01`: Chính sách và hàm giá trị.
- `L03R-04-02`: Một cách điều khiển robot.
- `L03R-04-03`: Chính sách là phân phối trên hành động.
- `L03R-04-04`: Trung bình trên các nhánh quỹ đạo.
- `L03R-04-05`: Giá trị trạng thái.
- `L03R-04-06`: Ấn định hành động đầu tiên.
- `L03R-04-07`: Giá trị hành động.
- `L03R-04-08`: Câu hỏi kiểm tra.

## Đặc tả và ánh xạ nguồn

Mạch và vai trò từng slide, chu trình học, lý do chuyển ví dụ sinh viên/xe sang robot: storyboard.md và review-log.md. Mọi công thức dùng ký hiệu Sutton và Barto, ấn bản2, chương3; ma trận là hệ quả của Bellman. Không có code demo mới.
