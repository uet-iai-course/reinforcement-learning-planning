# Storyboard triển khai — Bài 03: Quá trình quyết định Markov

Bản viết lại dùng robot thu gom lon. Đã triển khai 7/7 phần; 50/50 slide. [Kế hoạch đã chốt](storyboard-mdp-replanned.md) được dùng làm cơ sở; các điều chỉnh khi dựng và rà được ghi dưới đây. Bản HTML cũ đã được thay thế; không trộn các phần cũ vào deck mới.

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

## 3. Phần 1 — Từ tương tác đến trạng thái Markov

**Chức năng:** đặt bài toán cần giải và xác định thông tin đầu vào đủ cho mô hình. Đầu vào là vòng tương tác ở Bài 02; đầu ra là một bước thời gian được đọc đúng và giả thiết Markov được hiểu như yêu cầu đối với trạng thái.

**Mạch trình bày trước khi chia slide:**

1. Giới thiệu bài giảng và đường đi của bài học.
2. Cho robot đang pin thấp đứng trước lựa chọn tìm, chờ hoặc sạc.
3. Theo dõi một lần lựa chọn và phản hồi để gắn chỉ số thời gian.
4. So sánh hai lịch sử khác nhau nhưng cùng mức pin hiện tại.
5. Phát biểu điều kiện Markov từ phép so sánh đó, rồi kiểm tra giới hạn của cách chọn trạng thái.

**Chu trình học:** vấn đề/ví dụ 01-03 → trực giác 01-04/05 → hình thức 01-06 → ứng dụng và kiểm tra 01-07. Hai slide đầu định hướng; không phải hai khái niệm mới. Tổng 12 phút.

### L03R-01-01 — Quá trình quyết định Markov

Thời lượng: 1 phút. Vai trò: tiêu đề bài giảng, đồng thời mở phần 1.

**Mặt slide:** tên bài “Quá trình quyết định Markov (MDP)”; Bài 03, Học tăng cường, học kỳ 1 năm 2026–2027, đơn vị theo mẫu hiện có. Tên viết tắt được giới thiệu cùng tên đầy đủ. Không thêm tiêu đề phần 1 riêng.

**Cách thể hiện:** bố cục tiêu đề của deck; chưa đưa công thức hoặc toàn bộ đồ thị robot.

**Ghi chú và cầu nối:** Bài 02 đã nhận diện các thành phần. Bài này sẽ viết quy luật tương tác bằng xác suất và dùng quy luật đó để tính kết quả dài hạn của một cách hành động. Chuyển sang bản đồ nội dung.

**Nguồn:** PPTX28; mục tiêu chương 3 SB.

### L03R-01-02 — Nội dung bài học

Thời lượng: 1 phút. Vai trò: định hướng.

**Mặt slide:** bảy tên phần theo bảng tổng quan; dòng mục tiêu “Mô tả mô hình, suy ra Bellman, tính giá trị của một chính sách”.

**Cách thể hiện:** danh sách bảy mục chia hai cột, đánh dấu phần 1 đang học. Dùng tên khái niệm để định hướng, chưa đưa công thức.

**Ghi chú và cầu nối:** xác suất có điều kiện, kỳ vọng và giải hệ tuyến tính là công cụ đã học. Tất cả được dùng trên cùng robot hai mức pin. Chuyển ngay sang quyết định cụ thể.

**Nguồn:** mục tiêu chương 3 SB; cấu trúc do người soạn đề xuất.

### L03R-01-03 — Robot thu gom lon

Thời lượng: 2 phút. Vai trò: vấn đề và ví dụ mở đầu.

**Mặt slide:** robot thu gom lon bằng pin sạc; H là pin cao, L là pin thấp. Tại L, robot có thể Tìm, Chờ hoặc Sạc. Tìm có thể thu được lon và cũng có thể làm cạn pin; sạc dùng một bước để phục hồi pin.

**Cách thể hiện:** SVG robot đơn giản cạnh biểu tượng pin; ba nhánh lựa chọn từ L. Chưa gắn xác suất hoặc ký hiệu hàm giá trị. Caption ghi “Ví dụ robot thu gom lon, phỏng theo Sutton–Barto”.

**Ghi chú và cầu nối:** mục tiêu là thu gom lâu dài; lựa chọn hiện tại thay đổi những lựa chọn có thể tiếp tục thực hiện. Trước khi so sánh chúng, cần mô tả một bước tương tác. Một bước là một chu kỳ quyết định, không nhất thiết một giây.

**Nguồn:** SB ví dụ 3.3, tr.52–53.

### L03R-01-04 — Một bước tương tác

Thời lượng: 2 phút. Vai trò: gắn đối tượng với chỉ số.

**Mặt slide:** một kết quả đã xảy ra: H → Tìm → nhận 2 điểm và sang L. Dưới hình lần lượt đặt $S_t=\mathrm H$, $A_t=\mathrm{tim}$, rồi cặp $(R_{t+1},S_{t+1})=(2,\mathrm L)$. Mẫu dữ liệu là $(S_t,A_t,R_{t+1},S_{t+1})$.

**Cách thể hiện:** trục thời gian trái–phải; phần thưởng và trạng thái kế tiếp nằm cùng một phản hồi. Sau khi đọc ví dụ, mở rộng thành $S_0,A_0,R_1,S_1,A_1,R_2,S_2,\ldots$.

**Ghi chú và cầu nối:** thứ tự các trường trong một bộ dữ liệu là quy ước ghi; thưởng mang chỉ số $t+1$ vì do hành động ở $t$ dẫn tới. Đây là một mẫu, chưa phải quy luật xác suất. Lịch sử chứa nhiều mẫu như vậy.

**Nguồn:** SB (3.1), tr.48; số thưởng theo đặc tả minh họa.

### L03R-01-05 — Hai lịch sử, cùng trạng thái hiện tại

Thời lượng: 2 phút. Vai trò: trực giác Markov.

**Mặt slide:** hai dải lịch sử: robot vừa tìm kiếm xong và robot vừa chờ; cả hai hiện ở L. Cả hai cùng chọn Tìm. Trong mô hình hai mức pin, phân phối phản hồi tiếp theo giống nhau.

**Cách thể hiện:** hai đường quá khứ nhập vào cùng nút L, rồi dùng chung cây phản hồi chưa gắn số. Nhãn “quá khứ khác nhau”, “cùng pin hiện tại và hành động”.

**Ghi chú và cầu nối:** đây là giả thiết của mô hình lý tưởng, không phải khẳng định mức pin luôn đủ cho mọi robot thật. Nếu vị trí cũng làm thay đổi cơ hội gặp lon thì trạng thái phải bổ sung vị trí. Phát biểu bằng xác suất trên trang sau.

**Nguồn:** SB §3.1, tr.49; áp dụng vào ví dụ 3.3.

### L03R-01-06 — Tính Markov

Thời lượng: 2 phút. Vai trò: hình thức hóa trực giác vừa có.

**Mặt slide:** gọi $H_t=(S_0,A_0,R_1,\ldots,S_t)$ là lịch sử tới thời điểm $t$. Với mọi phản hồi $(s',r)$:

$$
\Pr(S_{t+1}=s',R_{t+1}=r\mid H_t,A_t)
=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t,A_t).
$$

**Cách thể hiện:** Công thức Markov toàn chiều rộng, nối trực tiếp với hình hai lịch sử đã có ở01-05. Không lặp lại hình trên cùng trang công thức.

**Ghi chú và cầu nối:** các xác suất điều kiện xét ở những điều kiện có thể xảy ra. Trạng thái giữ thông tin từ quá khứ có ảnh hưởng tới phân phối bước tới. Biết trạng thái đủ không có nghĩa đã biết các xác suất trong phân phối ấy; phần 2 sẽ mô tả chúng.

**Nguồn:** SB §3.1, tr.49; viết tường minh bằng lịch sử.

### L03R-01-07 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: ứng dụng và kiểm tra.

**Mặt slide — Câu hỏi:**

1. Hành động $A_t$ tạo ra $R_t$ hay $R_{t+1}$?
2. Hai robot cùng pin thấp nhưng ở hai vị trí có cơ hội gặp lon khác nhau: chỉ dùng mức pin làm trạng thái đã đủ chưa?
3. Quan sát đúng trạng thái có đồng nghĩa biết xác suất chuyển không?

**Cách thể hiện:** danh sách đánh số; chỉ giữ biểu tượng robot và pin nhỏ nếu còn chỗ.

**Ghi chú đáp án:** 1. $R_{t+1}$. 2. Chưa đủ nếu vị trí thay đổi phân phối phản hồi; cần bổ sung thông tin liên quan. 3. Không; trạng thái là đầu vào, mô hình là quy luật phản hồi có điều kiện. **Câu nối:** “Ta sẽ mô tả quy luật này bằng bảng các kết quả có thể xảy ra.”

**Nguồn:** vận dụng SB §3.1 và Bài 02.

## 4. Phần 2 — Mô hình xác suất của MDP

**Chức năng:** biến mô tả robot thành mô hình có thể tính toán. Đầu vào là một bước phản hồi và yêu cầu Markov; đầu ra là hạt nhân chung, xác suất chuyển và thưởng trung bình. Chưa chọn chính sách.

**Mạch trình bày trước khi chia slide:**

1. Cố định trạng thái L và hành động Tìm để chỉ còn sự ngẫu nhiên của môi trường.
2. Vẽ hai kết quả có cả trạng thái mới lẫn thưởng; mở rộng thành bảng của robot.
3. Đặt tên $p$ cho xác suất trong bảng, nêu miền và điều kiện chuẩn hóa.
4. Gộp các hàng để lấy xác suất chuyển; lấy trung bình có trọng số để có thưởng kỳ vọng.
5. Tập hợp các đối tượng thành đặc tả MDP và kiểm tra bằng một cặp trạng thái–hành động.

**Chu trình học:** vấn đề/ví dụ 02-01/02 → biểu diễn cụ thể 02-03 → hình thức 02-04 → ứng dụng và công thức suy ra 02-05 → tổng hợp 02-06 → kiểm tra 02-07. Tổng 18 phút.

### L03R-02-01 — Mô hình xác suất của MDP

Thời lượng: 1 phút. Vai trò: tiêu đề phần và đặt vấn đề.

**Mặt slide:** đúng tiêu đề phần; một câu “Cùng pin thấp và hành động Tìm có thể dẫn tới hai phản hồi”.

**Cách thể hiện:** nút L → hành động Tìm → hai ô kết quả còn để trống. Hành động là lựa chọn đã cố định, không ghi xác suất chọn hành động lên cạnh này.

**Ghi chú và cầu nối:** một mẫu H→Tìm→L ở phần trước không cho biết tần suất từng kết quả. Mô hình phải mô tả mọi phản hồi có thể xảy ra sau một cặp trạng thái–hành động.

**Nguồn:** SB ví dụ 3.3, tr.52–53.

### L03R-02-02 — Hai phản hồi của hành động Tìm

Thời lượng: 3 phút. Vai trò: ví dụ số trước ký hiệu xác suất chung.

**Mặt slide:** từ L, Tìm dẫn tới L và nhận $2$ với xác suất $1/2$; hoặc cạn pin, được cứu hộ về H và nhận $-3$ với xác suất $1/2$. Từ H, Tìm dẫn tới H hoặc L, mỗi nơi $1/2$, đều nhận $2$.

**Cách thể hiện:** trước hết chỉ hiện nhánh từ L. Mỗi đầu mũi tên là một ô chứa cặp “trạng thái mới; thưởng”, trọng số nằm trên cạnh. Sau khi đọc đủ nhánh, hiện thêm cây từ H. Caption “Ví dụ số: thưởng cố định trên mỗi nhánh”.

**Giải thích và cầu nối:** không tách rút thăm trạng thái và thưởng thành hai lần độc lập: ở L, biết thưởng $-3$ là biết robot đã được cứu về H. Cứu hộ tính trọn trong một bước mô hình; không cộng thêm $2$. Bảng ở trang sau ghi chính những nhánh này cùng các hành động còn lại.

**Nguồn:** số hóa SB ví dụ 3.3 theo đặc tả đầu storyboard.

### L03R-02-03 — Bảng phản hồi của robot

Thời lượng: 3 phút. Vai trò: đi từ hình sang dữ liệu mô hình.

**Mặt slide:** bảng bảy hàng đã xác định ở mục 2, với các cột “hiện tại”, “hành động”, “kế tiếp”, “thưởng”, “xác suất”. Chỉ ghi các kết quả có xác suất dương.

**Cách thể hiện:** giữ H–Tìm và L–Tìm từ trang trước; lần lượt thêm H–Chờ, L–Chờ, L–Sạc. Khoanh nhóm hàng theo cùng cặp hiện tại–hành động; tổng xác suất của mỗi nhóm bằng 1. Không thu nhỏ bảng để đặt thêm đồ thị đầy đủ bên cạnh.

**Giải thích và cầu nối:** ở H chỉ có Tìm/Chờ; ở L thêm Sạc. Chờ giữ mức pin, nhận 1; Sạc từ L về H, nhận 0. Các ô không có trong bảng có xác suất 0. Cần một ký hiệu ngắn để truy vấn từng dòng.

**Nguồn:** SB ví dụ 3.3; tinh thần bài tập 3.4, với giả thiết thưởng cố định đã nêu.

### L03R-02-04 — Xác suất chuyển trạng thái và phần thưởng

Thời lượng: 3 phút. Vai trò: định nghĩa hạt nhân chung.

**Mặt slide:** gọi $\mathcal S$ là tập trạng thái, $\mathcal A(s)$ là tập hành động hợp lệ, $\mathcal R$ là tập điểm thưởng; cả ba loại tập đều hữu hạn. Từ một dòng cụ thể:

$$p(\mathrm H,-3\mid\mathrm L,\mathrm{tim})=\frac12.$$

Sau đó đưa định nghĩa và chuẩn hóa:

$$p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a),$$
$$p(s',r\mid s,a)\ge0,\qquad \sum_{s'\in\mathcal S}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1.$$

**Cách thể hiện:** chuyển nhãn của dòng bảng sang đúng bốn vị trí trong công thức. Cặp $(s,a)$ cố định; chỉ $(s',r)$ chạy trong tổng. Các dòng công thức xuất hiện lần lượt.

**Giải thích và cầu nối:** dùng một hàm $p$ không có chỉ số thời gian nghĩa là thêm giả thiết quy luật không đổi theo thời gian. Giả thiết này khác điều kiện Markov của phần 1. Chỉ số trong SB (3.2) được dịch từ $t-1,t$ sang $t,t+1$.

**Nguồn:** SB (3.2)–(3.3), tr.48–49.

### L03R-02-05 — Xác suất chuyển và thưởng trung bình

Thời lượng: 3 phút. Vai trò: lấy hai đại lượng từ cùng mô hình.

**Mặt slide:** vẫn cố định L–Tìm. Xác suất về H là $1/2$; thưởng trung bình là

$$\frac12(2)+\frac12(-3)=-\frac12.$$

Đọc từ bảng rồi khái quát:

$$p(s'\mid s,a)=\sum_r p(s',r\mid s,a),$$
$$r(s,a)=\mathbb E[R_{t+1}\mid S_t=s,A_t=a]=\sum_{s',r}r\,p(s',r\mid s,a).$$

**Cách thể hiện:** hai bản sao nhỏ của nhóm L–Tìm: một bản gộp theo trạng thái đích, một bản nhân thưởng với trọng số. Giữ công thức cùng các hàng vừa gộp.

**Giải thích và cầu nối:** $r(s,a)$ có thể bằng $-1/2$ dù không lần nào nhận đúng điểm đó. Biến ngẫu nhiên $R_{t+1}$ và kỳ vọng $r(s,a)$ khác nhau. Khi viết $p$ ba đối số, đó là xác suất chuyển đã cộng hết các mức thưởng.

**Nguồn:** SB (3.4)–(3.5), tr.49.

### L03R-02-06 — Các thành phần của MDP

Thời lượng: 2 phút. Vai trò: tổng hợp hình thức sau khi từng thành phần đã có nghĩa.

**Mặt slide:** bốn hàng ghép tên đối tượng với robot: $\mathcal S=\{\mathrm H,\mathrm L\}$; $\mathcal A(s)$ phụ thuộc mức pin; $\mathcal R=\{-3,0,1,2\}$; $p$ là bảng phản hồi. Tóm tắt mô hình bằng

$$\mathcal M=\bigl(\mathcal S,\{\mathcal A(s)\}_{s\in\mathcal S},\mathcal R,p\bigr).$$

**Cách thể hiện:** mỗi hàng có biểu tượng/nhánh nhỏ đã dùng; không đưa một bộ ký hiệu đứng riêng trước ví dụ. Caption “Trạng thái Markov; quy luật phản hồi không đổi theo thời gian”.

**Giải thích và cầu nối:** đây là cách gom các thành phần của §3.1 thành một bộ, không phải phương trình đánh số của sách. Bộ mô tả môi trường; tiêu chuẩn cộng thưởng và cách chọn hành động được xây dựng ở phần 3 và 4. Biết mô hình chưa tự xác định hành động tốt nhất.

**Nguồn:** SB §3.1; PPTX49. Chọn cách viết bộ chưa có $\gamma$ vì tiêu chuẩn đánh giá được định nghĩa ở phần kế tiếp.

### L03R-02-07 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: vận dụng hạt nhân và kỳ vọng.

**Mặt slide — Câu hỏi:**

1. Đọc $p(\mathrm H,0\mid\mathrm L,\mathrm{sac})$ và tổng xác suất của các phản hồi sau L–Sạc.
2. Tính thưởng trung bình khi Tìm ở L. Điểm trung bình có phải điểm robot luôn nhận không?
3. Sau L–Tìm, nếu biết thưởng là $-3$, trạng thái kế tiếp là gì? Điều này nói gì về quan hệ giữa thưởng và trạng thái kế tiếp?

**Cách thể hiện:** kèm ba hàng liên quan của bảng; sinh viên không phải nhớ toàn bộ mô hình.

**Ghi chú đáp án:** 1. Cả hai bằng 1. 2. $-1/2$; kết quả thực tế chỉ là 2 hoặc −3. 3. H; hai đại lượng không độc lập trong ví dụ này. **Câu nối:** “Mô hình đã cho điểm của từng bước. Ta cần một tiêu chuẩn để tính cả chuỗi bước.”

**Nguồn:** vận dụng SB (3.2)–(3.5).

## 5. Phần 3 — Phần thưởng và tổng thưởng

**Chức năng:** xác định đại lượng sẽ được đánh giá trong những phần sau. Đầu vào là thưởng từng bước; đầu ra là tổng thưởng trên một quỹ đạo cùng các điều kiện cho phép lấy kỳ vọng.

**Mạch trình bày trước khi chia slide:**

1. Theo dõi robot qua nhiều chu kỳ, phân biệt việc sạc với kết thúc nhiệm vụ.
2. Đặt cạnh nhau hai dãy thưởng ba bước và tính điểm khi giảm trọng số theo thời gian.
3. Từ phép tính bằng số, định nghĩa $G_t$ và $\gamma$ cho nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn.
4. Dùng một tổng hình học cụ thể để giải thích điều kiện hữu hạn; kiểm tra chỉ số và ý nghĩa của chiết khấu.

**Chu trình học:** vấn đề/ví dụ 03-01/02 → trực giác và tính số 03-03 → hình thức 03-04 → điều kiện và áp dụng 03-05 → kiểm tra 03-06. Không chứng minh tính duy nhất của phép cộng từ một tiên đề preference; tổng chiết khấu là tiêu chuẩn được chọn theo giáo trình. Tổng 14 phút.

### L03R-03-01 — Phần thưởng và tổng thưởng

Thời lượng: 1 phút. Vai trò: tiêu đề phần.

**Mặt slide:** tên phần; một dải ba lần robot hành động và ba ô điểm thưởng, kèm câu “Đánh giá kết quả của cả chuỗi hành động”.

**Cách thể hiện:** trục thời gian, chưa hiện tổng vô hạn. Một ô điểm không được dùng để thay cho cả chuỗi.

**Ghi chú và cầu nối:** tìm, chờ và sạc có tác động khác nhau tới các bước sau. Trước khi cộng điểm cần biết bài toán có kết thúc tự nhiên hay còn tiếp diễn.

**Nguồn:** SB §3.2–3.3, tr.53–55.

### L03R-03-02 — Nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn

Thời lượng: 3 phút. Vai trò: ví dụ làm rõ phạm vi cộng thưởng.

**Mặt slide:** robot L→Sạc→H rồi tiếp tục hoạt động; cứu hộ cũng tiếp tục. Đặt cạnh một lượt đi tới đích: sau khi kết thúc, không còn thưởng của lượt ấy. Gọi $T$ là thời điểm kết thúc; robot thu gom trong mô hình đang xét có $T=\infty$.

**Cách thể hiện:** hai trục thời gian; trên trục có kết thúc, đệm các số 0 sau đích theo hình ở SB §3.4. Trạng thái kết thúc có hình vuông và nhãn, không chỉ phân biệt bằng màu.

**Giải thích và cầu nối:** bắt đầu lượt mới là lần tương tác mới; không nối phần thưởng của lượt mới vào tổng của lượt cũ. Một đoạn ba bước cắt ra để minh họa chưa phải một lượt hoàn chỉnh của robot. Trên cả hai trục, thưởng xảy ra ở thời điểm nào sẽ quyết định trọng số của nó.

**Nguồn:** SB §3.3–3.4, tr.54–57; ví dụ mê cung đã có ở Bài 02.

### L03R-03-03 — Điểm thưởng ở các thời điểm

Thời lượng: 3 phút. Vai trò: tính bằng số trước định nghĩa tổng chiết khấu.

**Mặt slide:** từ L, hai đoạn ba bước hợp lệ: Sạc rồi Tìm, Tìm có dãy thưởng $(0,2,2)$; Chờ ba lần có dãy $(1,1,1)$. Tổng không chiết khấu lần lượt là 4 và 3. Với trọng số $1,1/2,1/4$:

$$0+\frac12\,2+\frac14\,2=\frac32,\qquad
1+\frac12\,1+\frac14\,1=\frac74.$$

**Cách thể hiện:** hai dải thưởng cùng căn thời điểm; hàng trọng số chung ở dưới. Nêu $\gamma=1/2$ là hệ số làm trọng số giảm một nửa sau mỗi bước, sau khi sinh viên đã tính hai tổng.

**Giải thích và cầu nối:** so sánh này dành cho hai đoạn cụ thể, không chứng minh chính sách Chờ tốt hơn trong toàn tương lai. Chiết khấu thay đổi cách đánh giá thời điểm nhận điểm. Trang sau đặt tên cho đại lượng được cộng từ một thời điểm bất kỳ.

**Nguồn:** vận dụng SB (3.8); dãy thưởng do người soạn chọn từ bảng robot.

### L03R-03-04 — Tổng thưởng từ thời điểm hiện tại

Thời lượng: 3 phút. Vai trò: định nghĩa $G_t$ và quy ước kết thúc.

**Mặt slide:** $G_t$ là tổng thưởng kể từ sau hành động tại thời điểm $t$. Với lượt kết thúc ở $T$:

$$G_t=\sum_{k=t+1}^{T}\gamma^{k-t-1}R_k.$$

Với nhiệm vụ tiếp diễn hoặc sau khi đệm thưởng 0:

$$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}.$$

**Cách thể hiện:** Hai cột cho lượt hữu hạn và tổng vô hạn; cột sau xuất hiện bằng fragment. Giữ cỡ chữ chung và nêu số hạng đầu cùng quy ước kết thúc.

**Giải thích và cầu nối:** $\gamma\in[0,1]$; trong nhiệm vụ tiếp diễn của bài dùng $\gamma<1$. Với bài có lượt, ký hiệu $\mathcal S^+$ thêm trạng thái kết thúc vào $\mathcal S$ như sách; $G_T=0$. Các tổng qua trạng thái kế tiếp gồm cả trạng thái kết thúc nếu có. Đệm 0 là quy ước toán học, không thêm quyết định của tác tử sau khi đã kết thúc. Còn phải kiểm tra tổng và kỳ vọng có hữu hạn không.

**Nguồn:** SB (3.7)–(3.8), (3.11), tr.54–57. Dịch chỉ số trong hai tổng phải được kiểm riêng; chúng cùng bắt đầu bằng $R_{t+1}$.

### L03R-03-05 — Điều kiện để tổng thưởng hữu hạn

Thời lượng: 2 phút. Vai trò: giải thích một giả thiết sẽ dùng trong Bellman.

**Mặt slide:** nếu mỗi bước nhận 1 và $\gamma=1/2$, tổng là $1+1/2+1/4+\cdots=2$. Tổng quát, nếu $\lvert R_t\rvert\le M$ và $0\le\gamma<1$:

$$\lvert G_t\rvert\le\sum_{k=0}^{\infty}\gamma^kM=\frac{M}{1-\gamma}.$$

Robot có $M=3$, $\gamma=1/2$, nên $\lvert G_t\rvert\le6$ với mọi quỹ đạo.

**Cách thể hiện:** tổng hình học bằng các đoạn độ dài giảm dần; chuyển từ mức thưởng 1 sang cận M. Công thức là cận trị tuyệt đối, không phải giá trị chính xác của robot.

**Ghi chú và cầu nối:** cận này cũng bảo đảm kỳ vọng trị tuyệt đối hữu hạn, cho phép dùng tuyến tính và kỳ vọng lặp ở phần 5. Với $\gamma=1$, thưởng bị chặn và kỳ vọng số bước tới kết thúc hữu hạn là một điều kiện đủ. Chỉ có một trạng thái mang nhãn “kết thúc” chưa bảo đảm tác tử sẽ tới đó hoặc kỳ vọng thời gian tới đó hữu hạn.

**Nguồn:** SB tr.55 sau (3.8); cận hình học và điều kiện kỳ vọng ở trường hợp $\gamma=1$ được giải thích bổ sung.

### L03R-03-06 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: vận dụng và kiểm chỉ số.

**Mặt slide — Câu hỏi:**

1. Robot về H sau Sạc có kết thúc nhiệm vụ không?
2. Với dãy ba thưởng $(0,2,2)$ và $\gamma=1/2$, điểm của đoạn là bao nhiêu? Nếu $\gamma=0$ thì còn số hạng nào?
3. Cận 6 ở trang trước có nghĩa mọi quỹ đạo của robot đều có tổng thưởng bằng 6 không?

**Ghi chú đáp án:** 1. Không. 2. $3/2$; khi $\gamma=0$ chỉ giữ thưởng đầu, bằng 0. 3. Không, đó là cận trị tuyệt đối. **Câu nối:** “Cùng bắt đầu từ một trạng thái vẫn có nhiều tổng thưởng; cách chọn hành động và ngẫu nhiên của môi trường quyết định phân phối của chúng.”

**Nguồn:** vận dụng SB §3.3–3.4.

## 6. Phần 4 — Chính sách và hàm giá trị

**Chức năng:** xác định phân phối tổng thưởng cần lấy kỳ vọng và phân biệt hai thí nghiệm đánh giá. Đầu vào là mô hình và $G_t$; đầu ra là $v_\pi$ và $q_\pi$ với cùng một chính sách tiếp diễn.

**Mạch trình bày trước khi chia slide:**

1. Cho một cách điều khiển robot bằng lời và bảng xác suất hành động.
2. Định nghĩa chính sách từ bảng; phân biệt ngẫu nhiên của hành động với phản hồi môi trường.
3. Tính trung bình tổng thưởng của hai bước đầu bằng cây xác suất có ít nhánh.
4. Mở rộng đối tượng được lấy trung bình sang toàn bộ tương lai để định nghĩa giá trị trạng thái.
5. Thay thí nghiệm: ấn định một hành động đầu rồi trở lại chính sách cũ; định nghĩa giá trị hành động.
6. Kiểm tra sự khác nhau giữa mô hình, chính sách, một tổng thưởng và hai hàm giá trị.

**Chu trình học:** vấn đề/ví dụ chính sách 04-01/02 → hình thức 04-03 → ví dụ trung bình 04-04 → định nghĩa $v$ 04-05 → thí nghiệm cụ thể 04-06 → định nghĩa $q$ 04-07 → vận dụng/kiểm tra 04-08. $v$ và $q$ có ví dụ riêng trước định nghĩa; chưa lấy công thức Bellman làm định nghĩa. Tổng 17 phút.

### L03R-04-01 — Chính sách và hàm giá trị

Thời lượng: 1 phút. Vai trò: tiêu đề phần.

**Mặt slide:** tên phần; robot ở L với ba lựa chọn; câu “Tổng thưởng còn phụ thuộc cách chọn hành động”.

**Cách thể hiện:** tái dùng ba nhánh lựa chọn, không thêm ký hiệu giá trị vào hình mở phần.

**Ghi chú và cầu nối:** bảng $p$ chỉ mô tả điều xảy ra khi một hành động đã được chọn. Muốn nói đến trung bình của nhiều quỹ đạo, phải biết cách chọn các hành động trên những quỹ đạo đó.

**Nguồn:** SB §3.5, tr.58.

### L03R-04-02 — Một cách điều khiển robot

Thời lượng: 2 phút. Vai trò: ví dụ chính sách.

**Mặt slide:** tại H luôn Tìm; tại L chọn Chờ hoặc Sạc, mỗi hành động xác suất $1/2$. Bảng hai hàng ghi đủ xác suất 0 của các hành động không được chọn; ô H–Sạc là “không hợp lệ”, không ghi 0 như một hành động hợp lệ.

**Cách thể hiện:** hành động được chọn bằng bảng/cây từ trạng thái; xác suất của cách chọn đặt trước nút hành động. Chưa gắn xác suất của môi trường lên cùng tầng.

**Giải thích và cầu nối:** đây là một cách điều khiển cố định để đánh giá, chưa có khẳng định tối ưu. Chính sách có thể tất định ở một trạng thái và ngẫu nhiên ở trạng thái khác. Các con số trên bảng sẽ được gọi là $\pi(a\mid s)$.

**Nguồn:** minh họa cho định nghĩa chính sách SB §3.5; chính sách cụ thể do người soạn chọn.

### L03R-04-03 — Chính sách là phân phối trên hành động

Thời lượng: 2 phút. Vai trò: định nghĩa và phân biệt hai nguồn ngẫu nhiên.

**Mặt slide:** từ ô L–Chờ có $\pi(\mathrm{cho}\mid\mathrm L)=1/2$, khái quát:

$$\pi(a\mid s)=\Pr(A_t=a\mid S_t=s),\qquad
\pi(a\mid s)\ge0,\quad\sum_{a\in\mathcal A(s)}\pi(a\mid s)=1.$$

**Cách thể hiện:** một cây ba tầng trạng thái → hành động → phản hồi. Tầng đầu mang $\pi$, tầng sau mang $p$; có nhãn chữ cho hai tầng, không chỉ dùng màu.

**Giải thích và cầu nối:** trong bài, chính sách Markov dừng chỉ phụ thuộc trạng thái hiện tại và không đổi theo thời gian. Cố định chính sách ngẫu nhiên không loại bỏ việc rút thăm hành động. Mô hình và chính sách cùng tạo ra xác suất của một nhánh quỹ đạo.

**Nguồn:** SB §3.5, tr.58; cách viết xác suất theo ký hiệu của bài.

### L03R-04-04 — Trung bình trên các nhánh quỹ đạo

Thời lượng: 3 phút. Vai trò: ví dụ kỳ vọng trước giá trị trạng thái.

**Mặt slide:** bắt đầu ở H, theo chính sách đã cho, $\gamma=1/2$. Chỉ xét hai bước đầu, đặt $G_0^{[2]}=R_1+\gamma R_2$:

| Trường hợp | Xác suất | $G_0^{[2]}$ |
|---|---:|---:|
| Sau bước 1 ở H, bước 2 Tìm | $1/2$ | $2+(1/2)2=3$ |
| Sau bước 1 ở L, bước 2 Chờ | $(1/2)(1/2)=1/4$ | $2+(1/2)1=5/2$ |
| Sau bước 1 ở L, bước 2 Sạc | $(1/2)(1/2)=1/4$ | $2+(1/2)0=2$ |

$$\mathbb E_\pi[G_0^{[2]}\mid S_0=\mathrm H]
=\frac12\,3+\frac14\,\frac52+\frac14\,2=\frac{21}{8}.$$

**Cách thể hiện:** Cây hai bước với ba nhóm tổng. Hai kết quả cuối sau H–Tìm được gộp vì cùng thưởng2; phân biệt xác suất chọn hành động ở tầng giữa và xác suất nhóm tổng ở cột cuối.

**Giải thích và cầu nối:** ký hiệu $\mathbb E_\pi$ lấy trung bình theo cả chính sách và môi trường. Không lấy trung bình đều ba hàng. Đây là tổng của hai bước, không phải giá trị toàn tương lai; giá trị trạng thái sẽ lấy trung bình của $G_0$ đầy đủ.

**Nguồn:** phép tính từ đặc tả robot; trực giác kỳ vọng của SB (3.12).

### L03R-04-05 — Giá trị trạng thái

Thời lượng: 3 phút. Vai trò: định nghĩa sau phép lấy trung bình cụ thể.

**Mặt slide:** xuất phát ở $s$, từ đầu đến cuối chọn hành động theo $\pi$. Giá trị trạng thái là

$$v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s].$$

Với robot, $v_\pi(\mathrm H)$ là kỳ vọng tổng thưởng toàn tương lai khi bắt đầu pin cao và dùng bảng chính sách vừa chọn.

**Cách thể hiện:** kéo dài các nhánh hai bước bằng dấu tiếp diễn; ngoặc $G_t$ ôm cả phần tương lai. Thay ba con số hữu hạn bằng các tổng của toàn quỹ đạo; không đưa nghiệm $13/4$ trước khi lập hệ.

**Giải thích và cầu nối:** $v_\pi:\mathcal S\to\mathbb R$; trạng thái kết thúc, nếu có, mang giá trị 0. $G_t$ thay đổi theo quỹ đạo; $v_\pi(s)$ là một số xác định khi mô hình, chính sách và tiêu chuẩn tổng thưởng đã cố định. Điều kiện hữu hạn đã kiểm ở phần 3. Định nghĩa này để chính sách chọn cả hành động đầu; muốn đánh giá riêng một lựa chọn, đổi thí nghiệm ở trang sau.

**Nguồn:** SB (3.12), tr.58.

### L03R-04-06 — Ấn định hành động đầu tiên

Thời lượng: 2 phút. Vai trò: ví dụ chuẩn bị cho giá trị hành động.

**Mặt slide:** xuất phát ở L; lần lượt buộc hành động đầu là Tìm, Chờ hoặc Sạc. Sau phản hồi đầu tiên, cả ba thí nghiệm đều trở lại chính sách ở 04-02.

**Cách thể hiện:** ba hàng cùng xuất phát L. Khoanh hành động đầu của mỗi hàng; sau nút trạng thái mới dùng cùng hộp “tiếp tục theo $\pi$”. Nhánh Tìm giữ hai phản hồi của mô hình, không thay thành kết quả chắc chắn.

**Giải thích và cầu nối:** ấn định Tìm một lần vẫn có nghĩa dù chính sách thường không chọn Tìm ở L. Không buộc robot lặp hành động đầu mãi mãi. Phân phối tổng thưởng của mỗi thí nghiệm có một kỳ vọng riêng; đó là đối tượng cần đặt tên.

**Nguồn:** SB diễn giải giá trị hành động ngay trước (3.13), tr.58.

### L03R-04-07 — Giá trị hành động

Thời lượng: 2 phút. Vai trò: định nghĩa $q_\pi$ và miền của thí nghiệm.

**Mặt slide:** tại $s$, thực hiện $a$ một lần, sau đó theo $\pi$:

$$q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a],\qquad a\in\mathcal A(s).$$

So với $v_\pi(s)$, khác biệt là cách xác định hành động đầu tiên.

**Cách thể hiện:** đặt định nghĩa ngay dưới ba thí nghiệm rút gọn của trang trước; trên mặt có câu “Ấn định hành động đầu, rồi tiếp tục theo cùng chính sách”.

**Giải thích và cầu nối:** ký hiệu kỳ vọng điều kiện được hiểu theo thí nghiệm vừa định nghĩa, kể cả khi $\pi(a\mid s)=0$; không dựa vào chia cho xác suất của một biến cố 0. $q_\pi$ tính cả tương lai, không đồng nhất với $r(s,a)$. Trạng thái kết thúc không còn hành động cần đánh giá. Hai định nghĩa sẽ cho hai cách đọc cùng phép trung bình Bellman.

**Nguồn:** SB (3.13), tr.58; làm rõ quy ước hành động đầu.

### L03R-04-08 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: kiểm tra các đối tượng trước khi suy diễn.

**Mặt slide — Câu hỏi:**

1. Thay cách chọn Chờ/Sạc ở L có làm thay đổi bảng $p$ không? Có thể làm thay đổi giá trị không?
2. $21/8$ vừa tính là kỳ vọng hai bước hay giá trị toàn tương lai?
3. Tính $q_\pi(\mathrm L,\mathrm{tim})$ nghĩa là buộc Tìm bao nhiêu lần trước khi trở lại $\pi$?

**Ghi chú đáp án:** 1. Bảng môi trường không đổi; phân phối quỹ đạo và giá trị có thể đổi. 2. Kỳ vọng của đúng hai bước. 3. Một lần, rồi theo $\pi$ kể từ trạng thái kế tiếp. **Câu nối:** “Thay vì liệt kê toàn bộ quỹ đạo, ta tách bước đầu và dùng lại giá trị của trạng thái kế tiếp.”

**Nguồn:** vận dụng SB §3.5.

## 7. Phần 5 — Phương trình Bellman

**Chức năng:** suy ra quan hệ giữa các giá trị, giải thích vì sao không cần liệt kê mọi quỹ đạo. Đầu vào là định nghĩa $G_t,v_\pi,q_\pi$, chính sách và hạt nhân; đầu ra là ba quan hệ giá trị và hai phương trình Bellman kỳ vọng.

**Mạch trình bày trước khi chia slide:**

1. Tại L, đọc hai nhánh Chờ/Sạc của chính sách và viết “thưởng ngay + giá trị phần còn lại” bằng các hệ số đã biết.
2. Chứng minh việc tách bước đầu trên một dãy thưởng; bước này chưa cần Markov.
3. Lấy kỳ vọng theo hành động đầu bằng xác suất toàn phần.
4. Trong mỗi hành động, lấy kỳ vọng theo cặp phản hồi $(s',r)$ bằng cùng bảng $p$.
5. Chỉ ở đây dùng trạng thái Markov cùng chính sách dừng để thay kỳ vọng tương lai bằng $v_\pi(s')$; thu Bellman cho $v$.
6. Giữ cố định hành động đầu để có $q$ theo $v$; lấy trung bình các $q$ để trở lại $v$.
7. Thế $v(s')$ bằng trung bình của các $q(s',a')$ để có Bellman cho $q$.

**Chu trình học:** vấn đề/ví dụ 05-01/02 → trực giác tách một bước 05-03 → hình thức và suy diễn 05-04…06 → ứng dụng cách tách cho hành động 05-07/08 → phép thế 05-09 → kiểm tra 05-10. Từng phép biến đổi là một bước cần giải thích, không gom cả chuỗi vào một trang rồi thu nhỏ chữ. Tổng 30 phút.

### L03R-05-01 — Phương trình Bellman

Thời lượng: 1 phút. Vai trò: tiêu đề phần.

**Mặt slide:** tên phần; một trạng thái dẫn qua bước đầu tới hai ô “giá trị từ trạng thái kế tiếp”. Câu dẫn “Tách bước đầu, dùng lại giá trị của phần còn lại”.

**Cách thể hiện:** hình nhìn trước một bước, nối với cây nhiều bước ở phần 4. Các ô tương lai là các đại lượng đã có định nghĩa, chưa biết giá trị số.

**Ghi chú và cầu nối:** định nghĩa kỳ vọng trên toàn tương lai chưa cho cách tính gọn. Ta thử nhóm các quỹ đạo theo bước đầu, bắt đầu tại L của robot.

**Nguồn:** SB diễn giải trước và sau (3.14), tr.59.

### L03R-05-02 — Một bước từ pin thấp

Thời lượng: 3 phút. Vai trò: phương trình ví dụ trước suy diễn tổng quát.

**Mặt slide:** dưới chính sách đã chọn, tại L: Chờ nhận 1 rồi ở L; Sạc nhận 0 rồi tới H; xác suất chọn mỗi hành động $1/2$. Với $\gamma=1/2$:

$$v_\pi(\mathrm L)=\frac12\left[1+\frac12v_\pi(\mathrm L)\right]
+\frac12\left[0+\frac12v_\pi(\mathrm H)\right].$$

**Cách thể hiện:** từ cây hai nhánh, thay đuôi mỗi nhánh bằng hộp $v_\pi$ tương ứng, rồi dựng từng ngoặc. Hai hệ số ngoài mang nhãn “xác suất hành động”; hệ số trước giá trị mang nhãn “chiết khấu”. Chúng có cùng số $1/2$ nhưng khác vai trò.

**Giải thích và cầu nối:** mỗi ngoặc là thưởng một bước cộng giá trị tương lai đã chiết khấu. Giá trị L xuất hiện ở cả hai vế do Chờ giữ nguyên mức pin; chưa giải phương trình này. Các trang tiếp theo giải thích vì sao cấu trúc đó đúng cho mọi trạng thái.

**Nguồn:** vận dụng SB (3.14) vào đặc tả robot.

### L03R-05-03 — Tách phần thưởng tích lũy

Thời lượng: 3 phút. Vai trò: phép biến đổi trên một quỹ đạo.

**Mặt slide:**

$$\begin{aligned}
G_t&=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots\\
&=R_{t+1}+\gamma\bigl(R_{t+2}+\gamma R_{t+3}+\cdots\bigr)\\
&=R_{t+1}+\gamma G_{t+1}.
\end{aligned}$$

**Cách thể hiện:** mở từng dòng; ngoặc khoanh đuôi của cùng dãy thưởng. Bên dưới ghi riêng $G_{t+1}=R_{t+2}+\gamma R_{t+3}+\cdots$ để kiểm tra chỉ số. Dùng thưởng 0 sau kết thúc nếu có.

**Giải thích và cầu nối:** dòng 1 khai triển định nghĩa; dòng 2 đặt $\gamma$ ra ngoài các số hạng từ bước thứ hai; dòng 3 nhận đúng tổng bắt đầu ở thời điểm $t+1$. Không dùng xác suất, chính sách hay Markov ở phép tách này. Điều kiện hội tụ đã có ở phần 3. Tiếp theo lấy kỳ vọng của đẳng thức.

**Nguồn:** SB (3.9), tr.55, viết đầy đủ các số hạng.

### L03R-05-04 — Lấy trung bình theo hành động đầu

Thời lượng: 3 phút. Vai trò: tầng kỳ vọng thứ nhất.

**Mặt slide:** từ định nghĩa giá trị và đẳng thức vừa chứng minh:

$$v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s].$$

Nhóm các quỹ đạo theo $A_t=a$:

$$v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)
\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s,A_t=a].$$

**Cách thể hiện:** Khối công thức căn dòng toàn chiều rộng: định nghĩa sau khi tách tổng, rồi kỳ vọng theo hành động. Không đặt cây lặp bên cạnh công thức.

**Giải thích và cầu nối:** dùng kỳ vọng toàn phần theo hành động đầu, không phải chọn giá trị lớn nhất. Mô hình vẫn ngẫu nhiên bên trong mỗi hộp. Các hành động có trọng số 0 không đóng góp; khi nói riêng kỳ vọng sau một hành động, hiểu theo thí nghiệm hành động đầu đã định nghĩa ở phần 4.

**Nguồn:** bước trung gian làm tường minh suy diễn SB (3.14).

### L03R-05-05 — Lấy trung bình theo phản hồi môi trường

Thời lượng: 4 phút. Vai trò: tầng kỳ vọng thứ hai và tuyến tính.

**Mặt slide:** trước công thức, nêu quy ước điều kiện viết tắt: $s,a,s',r$ lần lượt là giá trị của $S_t,A_t,S_{t+1},R_{t+1}$. Với một hành động đã cố định:

$$\begin{aligned}
&\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid s,a]\\
&\quad=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\mathbb E_\pi[G_{t+1}\mid s,a,s',r]\right].
\end{aligned}$$

**Cách thể hiện:** Hai phản hồi số của L–Tìm và quy ước ký hiệu đứng trước khối kỳ vọng theo cặp phản hồi. Giữ đủ điều kiện s,a,s',r; không bỏ điều kiện ở bước này.

**Giải thích từng biến đổi:** kỳ vọng toàn phần nhóm theo cặp $(S_{t+1},R_{t+1})$; trong một nhóm, $R_{t+1}=r$ đã cố định nên ra khỏi kỳ vọng; tuyến tính đưa $\gamma$ ra ngoài. Chưa bỏ điều kiện $s,a,r$ trong kỳ vọng tương lai. Không nhân xác suất thưởng với xác suất chuyển như thể chúng độc lập. Chỉ các nhóm có xác suất dương cần kỳ vọng điều kiện riêng.

**Nguồn:** SB (3.14); mở riêng bước kỳ vọng lặp và giữ đầy đủ điều kiện.

### L03R-05-06 — Từ trạng thái kế tiếp đến giá trị tương lai

Thời lượng: 4 phút. Vai trò: chỉ rõ nơi dùng Markov và kết thúc suy diễn Bellman trạng thái.

**Mặt slide:** giữ quy ước điều kiện ở trang trước. Với mô hình Markov và chính sách Markov dừng:

$$\mathbb E_\pi[G_{t+1}\mid s,a,s',r]
=\mathbb E_\pi[G_{t+1}\mid S_{t+1}=s']
=v_\pi(s').$$

Thế vào hai tầng trung bình:

$$v_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma v_\pi(s')\right].$$

**Cách thể hiện:** Ba giả thiết đi trước hai đẳng thức nhận diện kỳ vọng tương lai; công thức Bellman căn dòng bên dưới. Công thức là hình chính, không thêm SVG.

**Giải thích từng bước:** biết $s'$ đủ để mô tả phân phối tương lai khi các hành động sau đó theo cùng chính sách; tính không đổi theo thời gian cho phép dùng cùng hàm $v_\pi$ tại $t+1$. Đây là điểm cần Markov, khác phép tách $G_t$ ở 05-03. Khi $s'$ kết thúc, dùng $v_\pi(s')=0$. Trở lại cây L và nhận lại đúng hai ngoặc của 05-02.

**Nguồn:** SB (3.12), (3.14), tr.58–59.

### L03R-05-07 — Giá trị hành động từ phản hồi một bước

Thời lượng: 2 phút. Vai trò: áp dụng cách tách với hành động đầu đã ấn định.

**Mặt slide:** trước hết đọc hai nhánh L–Tìm:

$$q_\pi(\mathrm L,\mathrm{tim})=
\frac12\left[2+\frac12v_\pi(\mathrm L)\right]
+\frac12\left[-3+\frac12v_\pi(\mathrm H)\right].$$

Từ định nghĩa $q$, tách $G_t$ và dùng đúng phép nhóm vừa chứng minh:

$$\begin{aligned}
q_\pi(s,a)&=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid s,a]\\
&=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma v_\pi(s')\right].
\end{aligned}$$

**Cách thể hiện:** Phép tính số của L–Tìm trước quan hệ q theo v tổng quát; cả hai toàn chiều rộng. Không thêm cây lặp vì hai phản hồi đã được chuẩn bị.

**Giải thích và cầu nối:** không nhân thêm $\pi(a\mid s)$ ở bước đầu vì đã ấn định $a$. Chính sách vẫn quyết định phần tương lai thông qua $v_\pi$. Nếu để chính sách chọn hành động đầu, phải lấy trung bình các giá trị hành động.

**Nguồn:** SB bài tập 3.13, tr.58 và 3.19, tr.62; suy ra từ các bước 05-03…06.

### L03R-05-08 — Giá trị trạng thái từ các giá trị hành động

Thời lượng: 3 phút. Vai trò: khép quan hệ giữa hai thí nghiệm đánh giá.

**Mặt slide:** tại L, chính sách chọn hai hành động:

$$v_\pi(\mathrm L)=\frac12q_\pi(\mathrm L,\mathrm{cho})
+\frac12q_\pi(\mathrm L,\mathrm{sac}).$$

Sau ví dụ, viết lại bước kỳ vọng theo hành động đầu:

$$\begin{aligned}
v_\pi(s)&=\sum_a\pi(a\mid s)\mathbb E_\pi[G_t\mid s,a]\\
&=\sum_a\pi(a\mid s)q_\pi(s,a).
\end{aligned}$$

**Cách thể hiện:** Ví dụ v tại L là trung bình của hai q, rồi hai dòng suy diễn tổng quát. Không dùng cột hẹp hoặc hình lặp.

**Giải thích và cầu nối:** Tìm không đóng góp vào $v_\pi(\mathrm L)$ của chính sách này do trọng số 0; $q_\pi(\mathrm L,\mathrm{tim})$ vẫn được định nghĩa. Quan hệ đúng tại mọi trạng thái, nên có thể dùng nó tại $s'$ để thay phần tương lai trong phương trình của $q$.

**Nguồn:** SB bài tập 3.12, tr.58 và 3.18, tr.62.

### L03R-05-09 — Bellman kỳ vọng cho giá trị hành động

Thời lượng: 4 phút. Vai trò: phép thế từng bước, không đưa công thức cuối đột ngột.

**Mặt slide:** viết quan hệ vừa có tại trạng thái kế tiếp:

$$v_\pi(s')=\sum_{a'\in\mathcal A(s')}\pi(a'\mid s')q_\pi(s',a').$$

Đặt cạnh phương trình $q$ theo $v$, đánh dấu vị trí sẽ thế; sau đó hiện:

$$q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)
\left[r+\gamma\sum_{a'}\pi(a'\mid s')q_\pi(s',a')\right].$$

**Cách thể hiện:** Viết quan hệ ở trạng thái kế tiếp s', sau đó thế trực tiếp vào công thức q. Ba nhóm công thức đủ lớn, không thêm sơ đồ.

**Giải thích từng bước:** $a$ là hành động đã thực hiện ở $t$; $a'$ là hành động chọn ở $t+1$ tại $s'$, vì vậy dùng $\pi(a'\mid s')$. Chỉ có một hệ số $\gamma$ vì từ $t$ sang $t+1$ mới qua một bước. Với trạng thái kết thúc, toàn bộ giá trị tương lai bằng 0; không yêu cầu hành động tiếp theo thực tế.

**Nguồn:** lời giải bài tập 3.17, SB tr.61, từ bài tập 3.12–3.13. Không gán số phương trình (3.17).

### L03R-05-10 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra lập luận và tầng xác suất.

**Mặt slide — Câu hỏi:**

1. Số hạng đầu của $G_{t+1}$ là gì? Vì sao phép tách $G_t$ chưa cần Markov?
2. Ở bước nào trong suy diễn Bellman mới dùng tính Markov và chính sách dừng?
3. Trong $v_\pi(s)$, trọng số $\pi(a\mid s)p(s',r\mid s,a)$ mô tả điều gì? Vì sao phương trình của $q_\pi(s,a)$ không lấy trung bình hành động đầu lần nữa?

**Ghi chú đáp án:** 1. $R_{t+2}$; phép tách là đại số trên một dãy đã cho. 2. Khi thay kỳ vọng phần tương lai đã điều kiện hóa bằng $v_\pi(s')$. 3. Xác suất chọn hành động rồi nhận cặp phản hồi; đây là quy tắc nhân có điều kiện, không giả thiết độc lập. Với $q$, hành động đầu đã ấn định. **Câu nối:** “Các phương trình vẫn chứa giá trị chưa biết ở cả hai vế. Với robot hai trạng thái, ta sẽ giải chúng đồng thời.”

**Nguồn:** vận dụng SB (3.9), (3.14), bài tập 3.17–3.19.

## 8. Phần 6 — Đánh giá một chính sách từ mô hình

**Chức năng:** biến các quan hệ Bellman thành kết quả tính được, rồi nhận diện dạng tổng quát. Đầu vào là bảng robot, chính sách cố định và $\gamma=1/2$; đầu ra là nghiệm giá trị, phép kiểm bằng $q$ và cách rút MDP về MRP.

**Mạch trình bày trước khi chia slide:**

1. Viết đúng hai phương trình cho H và L từ hai cây một bước.
2. Giải hệ bằng phép trừ và thế, chưa đưa nghịch đảo ma trận trước bài toán số.
3. Dùng nghiệm tính hai giá trị hành động và kiểm lại trung bình theo chính sách.
4. Gộp các đường đi qua hành động để tính trực tiếp xác suất chuyển và thưởng trung bình của mỗi trạng thái.
5. Từ bảng đã gộp, định nghĩa chuỗi Markov và MRP cảm sinh; sau đó mới viết Bellman bằng ma trận.
6. Kiểm tra bằng hành động chưa dùng trong chính sách và bằng một hàng chuyển.

**Chu trình học:** vấn đề và ví dụ 06-01/02 → phép giải cụ thể 06-03 → ứng dụng/kiểm nghiệm 06-04 → ví dụ rút gọn mô hình 06-05 → hình thức MRP và ma trận 06-06/07 → kiểm tra 06-08. Phần này có hai cụm gắn nhau: giải một MDP nhỏ và khái quát phép tính thành mô hình đã gộp. Tổng 21 phút.

### L03R-06-01 — Đánh giá một chính sách từ mô hình

Thời lượng: 1 phút. Vai trò: tiêu đề phần.

**Mặt slide:** tên phần; hai trạng thái H và L, mỗi trạng thái có một ô giá trị chưa biết. Câu dẫn “Hai trạng thái, hai giá trị cần tìm”.

**Cách thể hiện:** quay về hình robot của phần 1; giữ bảng chính sách nhỏ và $\gamma=1/2$ để xác định rõ bài toán.

**Ghi chú và cầu nối:** không ước lượng từ các lần chạy và không tìm chính sách tối ưu trong phép tính này. Dữ kiện đầu vào là mô hình đầy đủ và chính sách; đầu ra là giá trị kỳ vọng đúng của từng trạng thái trong mô hình đó.

**Nguồn:** vận dụng SB (3.14); PPTX47–48.

### L03R-06-02 — Hệ Bellman của robot

Thời lượng: 2 phút. Vai trò: lập hệ từ hình.

**Mặt slide:** đặt $v_H=v_\pi(\mathrm H)$, $v_L=v_\pi(\mathrm L)$. Tại H luôn Tìm; tại L chọn Chờ/Sạc như trước:

$$\begin{aligned}
v_H&=2+\frac12\left(\frac12v_H+\frac12v_L\right),\\
v_L&=\frac12\left(1+\frac12v_L\right)
+\frac12\left(0+\frac12v_H\right).
\end{aligned}$$

**Cách thể hiện:** đọc cây H và viết phương trình thứ nhất; đọc lại cây L của 05-02 và viết phương trình thứ hai. Đặt nhãn “chính sách”, “chuyển trạng thái”, “chiết khấu” vào các hệ số tương ứng trong lúc xây từng phương trình.

**Giải thích và cầu nối:** ở H, hành động có xác suất 1 nhưng môi trường chia hai kết quả. Ở L, chính sách chia hai hành động, mỗi hành động có kết quả chắc chắn. Cả hai trường hợp dẫn tới giá trị tương lai có cùng hai ẩn. Không thay $v_L$ bằng thưởng chờ 1. Hai phương trình cần được giải đồng thời.

**Nguồn:** chuyên biệt SB (3.14) theo dữ kiện đã công bố.

### L03R-06-03 — Giải hai phương trình giá trị

Thời lượng: 3 phút. Vai trò: biến đổi đại số đầy đủ.

**Mặt slide:** khai triển hai phương trình, cùng hệ số của phần tương lai:

$$\begin{aligned}
v_H&=2+\frac14v_H+\frac14v_L,\\
v_L&=\frac12+\frac14v_H+\frac14v_L.
\end{aligned}$$

Trừ phương trình thứ hai khỏi phương trình thứ nhất:

$$v_H-v_L=\frac32.$$

Thế $v_H=v_L+3/2$ vào phương trình thứ hai:

$$v_L=\frac12+\frac14\left(v_L+\frac32\right)+\frac14v_L
=\frac78+\frac12v_L.$$

Suy ra $v_L=7/4$ và $v_H=13/4$.

**Cách thể hiện:** Một khối căn dòng chứa hai phương trình, phép trừ, phép thế và nghiệm cuối. Các bước tách bằng khoảng trắng; kiểm thế nghiệm trong notes.

**Giải thích và kiểm lại:** $13/4=2+(1/4)(13/4+7/4)$ và $7/4=1/2+(1/4)(13/4+7/4)$. Cả hai đúng. $13/4$ là giá trị toàn tương lai, khác $21/8$ của hai bước đầu; không dùng kết quả hữu hạn đó thay cho nghiệm Bellman.

**Nguồn:** phép giải hệ do người soạn tính từ ví dụ; không gán nghiệm số cho sách.

### L03R-06-04 — Kiểm tra giá trị bằng các hành động

Thời lượng: 3 phút. Vai trò: áp dụng $q$ theo $v$ và kiểm tra $v$ theo $q$.

**Mặt slide:** dùng nghiệm vừa tìm:

$$q_\pi(\mathrm L,\mathrm{cho})=1+\frac12\,\frac74=\frac{15}{8},$$
$$q_\pi(\mathrm L,\mathrm{sac})=0+\frac12\,\frac{13}{4}=\frac{13}{8}.$$

Lấy trung bình theo chính sách:

$$v_\pi(\mathrm L)=\frac12\,\frac{15}{8}+\frac12\,\frac{13}{8}=\frac74.$$

**Cách thể hiện:** thay giá trị vào đúng hai hộp tương lai trên cây L; lần lượt hiện phép tính từng hành động, rồi lấy trung bình hai kết quả. Không đưa bảng tất cả năm $q$ cùng lúc.

**Giải thích và cầu nối:** Chờ một lần rồi theo $\pi$ có giá trị cao hơn Sạc một lần rồi theo $\pi$ trong ví dụ này. Đây là so sánh với phần tiếp diễn cố định; chưa chứng minh chính sách nào tối ưu. Cả hai cách tính giá trị L trùng nhau. Có thể gộp luôn các nhánh hành động để tính trực tiếp từ trạng thái sang trạng thái.

**Nguồn:** vận dụng SB bài tập 3.12–3.13.

### L03R-06-05 — Gộp các nhánh dưới chính sách

Thời lượng: 3 phút. Vai trò: ví dụ số cho MRP cảm sinh.

**Mặt slide:** tại H, hai kết quả của Tìm có xác suất $1/2$ và thưởng 2. Tại L, Chờ đưa về L với xác suất $1/2$, Sạc đưa về H với xác suất $1/2$; thưởng trung bình bằng $(1/2)1+(1/2)0=1/2$.

| Hiện tại | Kế tiếp H | Kế tiếp L | Thưởng trung bình một bước |
|---|---:|---:|---:|
| H | $1/2$ | $1/2$ | $2$ |
| L | $1/2$ | $1/2$ | $1/2$ |

**Cách thể hiện:** Đọc các nhánh ở H và L bằng số rồi lập bảng xác suất chuyển và thưởng trung bình. Bảng số là ví dụ trực quan trước định nghĩa MRP ở06-06.

**Giải thích và cầu nối:** chính sách đã được lấy trung bình vào các trọng số; tính ngẫu nhiên vẫn còn. Bảng phụ thuộc chính sách cụ thể đang dùng. Việc chỉ còn trạng thái và chuyển tiếp dẫn đến tên gọi chuỗi Markov; giữ cả thưởng cho quá trình phần thưởng Markov.

**Nguồn:** hệ quả SB (3.4)–(3.5), §3.5; hw02 bài 4.

### L03R-06-06 — Chuỗi Markov và MRP dưới chính sách

Thời lượng: 3 phút. Vai trò: hình thức hóa phép gộp.

**Mặt slide:** ma trận chuyển dưới chính sách có phần tử

$$P^\pi_{ss'}=\sum_{a\in\mathcal A(s)}\pi(a\mid s)p(s'\mid s,a),$$

và thưởng trung bình của trạng thái là

$$r^\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)r(s,a).$$

Giữ trạng thái và chuyển tiếp: chuỗi Markov $(\mathcal S,P^\pi)$. Giữ thêm thưởng và chiết khấu: quá trình phần thưởng Markov (MRP) $(\mathcal S,P^\pi,r^\pi,\gamma)$.

**Cách thể hiện:** gắn mỗi công thức với một cột của bảng vừa tính. Hàng L cho $P^\pi_{LH}=P^\pi_{LL}=1/2$, $r^\pi(L)=1/2$. Mỗi hàng của $P^\pi$ tổng bằng 1.

**Giải thích và cầu nối:** hai công thức chỉ lấy trung bình những đại lượng đã định nghĩa ở 02-05. Chính sách Markov dừng làm phân phối phản hồi sau khi gộp chỉ phụ thuộc trạng thái hiện tại; vì vậy quá trình trạng thái vẫn Markov. $r^\pi$ lưu kỳ vọng thưởng cần cho bài toán giá trị; không mô tả đầy đủ phân phối thưởng. Chuỗi Markov và MRP không có một quyết định hành động mới ngoài chính sách đã gộp. Bellman của chúng chính là hệ vừa giải.

**Nguồn:** suy ra từ SB (3.4)–(3.5), (3.14); khái niệm tương ứng PPTX30,34; hw02 bài 4. Không gán số phương trình SB cho định nghĩa bộ MRP.

### L03R-06-07 — Bellman dưới dạng ma trận

Thời lượng: 3 phút. Vai trò: khái quát hệ phương trình và xác định điều kiện giải.

**Mặt slide:** chọn thứ tự trạng thái H, L; tổng quát có $n$ trạng thái. $v,r^\pi\in\mathbb R^n$ là véc-tơ cột, $P^\pi\in\mathbb R^{n\times n}$, $I$ là ma trận đơn vị. Gộp hai nhóm số hạng trong Bellman đã suy ra:

$$v_\pi(s)=r^\pi(s)+\gamma\sum_{s'}P^\pi_{ss'}v_\pi(s'),$$
$$v=r^\pi+\gamma P^\pi v
\quad\Longleftrightarrow\quad (I-\gamma P^\pi)v=r^\pi.$$

Với robot, hệ đó là

$$\begin{pmatrix}3/4&-1/4\\-1/4&3/4\end{pmatrix}
\begin{pmatrix}v_H\\v_L\end{pmatrix}
=\begin{pmatrix}2\\1/2\end{pmatrix}.$$

**Cách thể hiện:** tô một hàng để đối chiếu với phương trình H ở 06-03, rồi hàng L. Phép nhân $P^\pi v$ là các tổng có trọng số vừa học, không thêm quy tắc cập nhật mới. Công thức tổng quát xuất hiện trước ví dụ ma trận; ví dụ hệ số đã được chuẩn bị bằng hai phương trình và bảng ở các trang trước.

**Giải thích và điều kiện:** đầu vào gồm mô hình, chính sách và $\gamma$; tính $P^\pi,r^\pi$ rồi giải hệ cho $v$. Với ma trận xác suất hữu hạn và $0\le\gamma<1$, hệ có nghiệm duy nhất; có thể viết $v=(I-\gamma P^\pi)^{-1}r^\pi$. Chứng minh ngắn và trường hợp $\gamma=1$ đặt trong phụ lục ghi chú của storyboard, không dùng kết luận không điều kiện. Với ma trận đặc, giải trực tiếp thường tốn $O(n^3)$ phép tính; các phương pháp lặp sẽ học ở Bài 04. Trang chính ưu tiên lập hệ, không dạy thuật toán khử mới.

**Nguồn:** dạng ma trận suy ra từ SB (3.14); PPTX47–48.

### L03R-06-08 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra tính giá trị và rút gọn mô hình.

**Mặt slide — Câu hỏi:** cho lại $v_H=13/4$, $v_L=7/4$, $\gamma=1/2$ và hai nhánh L–Tìm.

1. Tính $q_\pi(\mathrm L,\mathrm{tim})$, dù chính sách đang dùng không chọn hành động đó tại L.
2. Từ bảng chính sách, tính hàng chuyển và thưởng trung bình của trạng thái L.
3. Nếu đổi chính sách, những đại lượng nào trong $p,P^\pi,r^\pi,v_\pi$ cần tính lại?

**Ghi chú đáp án:**

$$q_\pi(\mathrm L,\mathrm{tim})=
\frac12\left(2+\frac12\,\frac74\right)
+\frac12\left(-3+\frac12\,\frac{13}{4}\right)=\frac34.$$

Hàng L là $(1/2,1/2)$, thưởng trung bình $1/2$. Khi đổi chính sách, giữ mô hình $p$; phải xét lại $P^\pi,r^\pi,v_\pi$. Không khẳng định mọi thay đổi chính sách luôn làm mọi số đổi. **Câu nối:** “Một bài toán đánh giá chính sách đã được giải trọn từ mô hình đến giá trị; phần cuối nối lại các bước và chuyển sang bài tập.”

**Nguồn:** vận dụng SB §3.5; hw02 bài 4, 7, 8.

## 9. Phần 7 — Tổng hợp và vận dụng

**Chức năng:** trở lại quyết định của robot ở đầu bài và xác nhận sinh viên nối được từng đối tượng với phép tính. Đầu vào là mô hình và các giá trị đã giải; đầu ra là khả năng tự lập luận trên một quyết định, cùng nhiệm vụ luyện tập và điểm vào của Bài 04.

**Mạch trình bày trước khi chia slide:**

1. Trở lại robot pin thấp với các giá trị đã tính.
2. Đọc một hành động cụ thể từ dữ kiện môi trường và giá trị tương lai, rồi nhận ra công thức tổng quát đã học.
3. Giao bài tập theo đúng các năng lực vừa hình thành.
4. Kiểm tra điều kiện đủ dữ liệu, phân biệt các đại lượng và phạm vi kết luận về chính sách.

**Chu trình học:** ví dụ thu hồi 07-01/02 → nối lại hình thức đã biết 07-02 → vận dụng 07-03 → kiểm tra 07-04. Phần kết dùng chu trình rút gọn vì không giới thiệu khái niệm trọng tâm mới; không dựng một mô hình lớn khác ở cuối bài. Tổng 8 phút.

### L03R-07-01 — Tổng hợp và vận dụng

Thời lượng: 1 phút. Vai trò: tiêu đề phần và thu hồi vấn đề mở đầu.

**Mặt slide:** tên phần; robot ở L, bên cạnh các giá trị Chờ $15/8$, Sạc $13/8$, Tìm $3/4$, cùng nhãn “hành động đầu, sau đó theo $\pi$”.

**Cách thể hiện:** Sơ đồ ba hành động từ L với ba giá trị đã tính; giá trị gắn vào hành động, không thể hiện như một trạng thái đích chắc chắn.

**Ghi chú và cầu nối:** đầu bài chỉ biết các lựa chọn và tác động tới pin. Giờ mỗi lựa chọn có một giá trị dài hạn dưới cùng cách tiếp tục. Đọc ngược một phép tính để xác nhận mô hình, chính sách và giá trị không bị lẫn nhau.

**Nguồn:** kết quả ví dụ xuyên suốt; SB §3.5.

### L03R-07-02 — Đọc một quyết định bằng mô hình và giá trị

Thời lượng: 3 phút. Vai trò: từ ca cụ thể trở lại công thức đã học.

**Mặt slide:** xét L–Chờ. Môi trường cho $p(\mathrm L,1\mid\mathrm L,\mathrm{cho})=1$; giá trị trạng thái kế tiếp là $7/4$; $\gamma=1/2$. Vì thế:

$$q_\pi(\mathrm L,\mathrm{cho})=1+\frac12\,\frac74=\frac{15}{8}.$$

Đối chiếu từng thành phần với công thức:

$$q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma v_\pi(s')\right].$$

**Cách thể hiện:** dùng một nhánh của robot, ánh xạ xác suất 1, thưởng 1, trạng thái L và giá trị $7/4$ vào vị trí tương ứng. Công thức tổng quát hiện sau phép tính số, không lặp lại cả cây suy diễn phần 5.

**Giải thích và cầu nối:** $\pi(\mathrm{cho}\mid\mathrm L)=1/2$ là xác suất chính sách chọn hành động; nó khác xác suất phản hồi bằng 1. Không nhân $q$ với $1/2$ khi đánh giá hành động đã ấn định; chỉ dùng trọng số chính sách lúc ghép các $q$ thành $v$. Sinh viên sẽ thực hiện lại chuỗi thao tác này trên bài tập.

**Nguồn:** vận dụng SB bài tập 3.13/3.19; dùng kết quả phần 6.

### L03R-07-03 — Bài tập và bước tiếp theo

Thời lượng: 2 phút. Vai trò: xác định đầu ra luyện tập và giới hạn bài học.

**Mặt slide:** ba nhóm bài trong hw02:

| Bài | Nhiệm vụ | Kết quả cần viết |
|---|---|---|
| 3 | Kiểm tra ma trận ba trạng thái và lập Bellman | Hàng xác suất hợp lệ; hệ ba phương trình |
| 4 | Cố định chính sách, gộp MDP thành MRP | Công thức $P^\pi,r^\pi$ và giải thích phép trung bình |
| 7–8 | Nối $q$ với $v$, giải thích Bellman | Phép lấy trung bình và ý nghĩa từng thành phần |

Đọc SB §3.1–3.5. Bài 04: tìm chính sách tốt hơn khi biết mô hình.

**Cách thể hiện:** một bảng ngắn; không chèn nguyên đề bài dài hoặc toàn bộ chương sách lên mặt slide.

**Ghi chú và cầu nối:** 30 phút chữa bài ngoài tuyến 120 phút chia 10 phút cho bài 3, 10 phút cho bài 4, 10 phút cho bài 7–8. Bài 9 về Bellman tối ưu nối sang Bài 04; không suy diễn công thức tối ưu trong phần tổng kết này. Bài 10 có thể dùng luyện mô hình hóa sau giờ học nếu giảng viên giao.

**Nguồn:** hw02 bài 3, 4, 7, 8, 9, 10; ranh giới SB §3.5→§3.6.

### L03R-07-04 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: kiểm tra tổng hợp và kết bài.

**Mặt slide — Câu hỏi:**

1. Biết $p(s'\mid s,a)$, chính sách và hệ số chiết khấu đã đủ để tính giá trị trạng thái $v_\pi(s)$ chưa? Còn thiếu dữ kiện nào?
2. Một quỹ đạo có tổng thưởng khác $v_\pi(s)$ có mâu thuẫn với định nghĩa giá trị không?
3. $q_\pi(\mathrm L,\mathrm{cho})>q_\pi(\mathrm L,\mathrm{sac})$ đã chứng minh chính sách đang dùng là tối ưu chưa?

**Ghi chú đáp án:** 1. Còn thiếu mô hình thưởng; cho $r(s,a)$ là đủ cùng xác suất chuyển để viết Bellman kỳ vọng, hoặc cho hạt nhân chung $p(s',r\mid s,a)$. 2. Không; một tổng thưởng là kết quả của quỹ đạo, giá trị là kỳ vọng. 3. Chưa; ta mới so sánh hành động đầu với phần tiếp diễn theo chính sách đã cho. Bài 04 sẽ nghiên cứu việc thay đổi chính sách và mục tiêu tối ưu.

**Cách thể hiện:** chỉ ba câu hỏi đánh số; đáp án nằm trong notes. Kết ở năng lực tính và giới hạn kết luận, không thêm câu khẩu hiệu hoặc lặp lại mục lục.

**Nguồn:** vận dụng SB §3.1 và §3.5.

## 10. Ánh xạ nguồn và các thay đổi có chủ ý

| Slide PPTX | Quyết định | Nơi thực hiện trong storyboard mới | Lý do và ảnh hưởng |
|---|---|---|---|
| 28 | Giữ | Phần 1, tiêu đề bài | Bảo toàn tên và chủ đề MDP. |
| 29 | Sửa, tách | 01-04…07; 02-04 | Ví dụ hai lịch sử trước điều kiện Markov; thêm giả thiết đồng nhất thời gian riêng. |
| 30 | Chuyển | 06-05…07 | Chuỗi Markov được nhận diện từ MDP sau khi cố định chính sách, thay vì là cửa vào của bài. |
| 31–33 | Thay ví dụ | 02-02/03; 06-05…07 | Thay đồ thị sinh viên bảy trạng thái bằng robot hai trạng thái; giữ đọc đồ thị, chuẩn hóa và ma trận. Không dạy phân phối dừng. |
| 34 | Chuyển, sửa | 06-05/06 | Định nghĩa MRP sau ví dụ phép gộp; thưởng trung bình được phân biệt với thưởng quan sát. |
| 35 | Thay ví dụ | Phần 2–3 | Cùng robot có cả trạng thái, hành động và thưởng ngay từ đầu, không đổi đặc tả giữa MRP và MDP. |
| 36–38 | Giữ ý, sửa cách giải thích | 03-02…06 | Ví dụ trọng số trước tổng; không đồng nhất gamma nhỏ với thuật toán tham lam hoặc tuyên bố tổng là lựa chọn duy nhất. |
| 39 | Chuyển, sửa | 04-04/05 | Định nghĩa giá trị sau khi có chính sách và phép lấy kỳ vọng bằng số; không dùng ký hiệu $v$ trước đối tượng cần đánh giá. |
| 40–43 | Thay, gộp | 03-03; 04-04; 06-03 | Thay hai quỹ đạo sinh viên và các bảng giá trị cho nhiều gamma bằng các tổng robot và một chính sách xuyên suốt. Giảm số dữ kiện phải ghi nhớ; giữ vai trò của chiết khấu. |
| 44–46 | Tách, mở rộng | 05-02…06 | Tách rõ đại số, kỳ vọng toàn phần, tuyến tính và chỗ dùng Markov. Suy diễn trực tiếp Bellman MDP, không giảng cùng phép suy diễn hai lần cho hai mô hình khác nhau. |
| 47–48 | Chuyển, mở rộng ví dụ giải | 06-02…07 | Giải hai phương trình bằng tay trước khi trình bày dạng ma trận, điều kiện nghiệm và giới hạn của giải trực tiếp. |
| 49 | Chuyển lên | 02-04…06 | MDP xuất phát từ bài toán có lựa chọn, theo tuyến §3.1 của SB. |
| 50 | Thay ví dụ | Phần 1–2, 4, 6 | Robot từ SB thay Student MDP; không cần phân biệt hai đồ thị sinh viên khác nhau. |
| 51 | Thay ví dụ | 04-06/07; 06-04/08 | Các hành động của robot đủ để minh họa $q$ và đánh đổi thưởng/tương lai. Xe đua có thể dùng sau giờ học; không xuất hiện trong tuyến 120 phút. |
| 52 | Giữ, chuyển | 04-02/03 | Quy tắc cụ thể trước định nghĩa chính sách. |
| 53 | Tách | 04-04…08 | Phép trung bình trước $v$; thí nghiệm ấn định hành động trước $q$. |
| 54–55 | Thay ví dụ | 06-02…04 | Các giá trị đều được tìm ra từ hệ robot ngay trên lớp, không đưa sẵn nghiệm xe đua rồi mới giải thích. |
| 56–57 | Tách, mở rộng | 05-07…10 | Giải thích cả $q$ theo $v$, $v$ theo $q$ và phép thế cho Bellman $q$; nguồn từ SB §3.5 và bài tập 3.17–3.19. |
| 58 | Giữ, cập nhật | 07-03 | Đối chiếu đúng bài tập hw02 và mục đọc SB; Bellman tối ưu nối sang Bài 04. |

Bản HTML50slide đã thay thế deck47slide cũ. Đã cập nhật thẻ Bài03 trên index, đồng bộ outline/storyboard và xóa26SVG cũ không còn tham chiếu. Giữ nguồn và lịch sử thay đổi trong Git.

## 11. Hình và bố cục đã triển khai

Deck dùng chung `lecture-slide.css`, khung1280×720, RevealJS/KaTeX/Notes/Highlight cục bộ, bảy section ngoài. Có19SVG mới, mỗi SVG có role và mô tả thay thế; không có ảnh raster hoặc tài nguyên cốt lõi từ mạng. Công thức dựng bằng KaTeX, bảng bằng HTML. Màu đi cùng nhãn và hình dạng.

| Tài sản thực tế | Slide sử dụng |
|---|---|
| [robot-p01-recycling-robot-low.svg](../../img/lec-03/robot-p01-recycling-robot-low.svg) | `L03R-01-03` |
| [robot-p01-timestep-axis.svg](../../img/lec-03/robot-p01-timestep-axis.svg) | `L03R-01-04` |
| [robot-p01-two-histories.svg](../../img/lec-03/robot-p01-two-histories.svg) | `L03R-01-05` |
| [robot-p02-uncertain-feedback.svg](../../img/lec-03/robot-p02-uncertain-feedback.svg) | `L03R-02-01` |
| [robot-p02-search-outcomes.svg](../../img/lec-03/robot-p02-search-outcomes.svg) | `L03R-02-02` |
| [robot-p03-reward-timeline.svg](../../img/lec-03/robot-p03-reward-timeline.svg) | `L03R-03-01` |
| [robot-p03-episodic-continuing.svg](../../img/lec-03/robot-p03-episodic-continuing.svg) | `L03R-03-02` |
| [robot-p03-discounted-bands.svg](../../img/lec-03/robot-p03-discounted-bands.svg) | `L03R-03-03` |
| [robot-p03-geometric-series.svg](../../img/lec-03/robot-p03-geometric-series.svg) | `L03R-03-05` |
| [robot-p04-policy-choices.svg](../../img/lec-03/robot-p04-policy-choices.svg) | `L03R-04-01` |
| [robot-p04-two-layers.svg](../../img/lec-03/robot-p04-two-layers.svg) | `L03R-04-03` |
| [robot-p04-two-step-tree.svg](../../img/lec-03/robot-p04-two-step-tree.svg) | `L03R-04-04` |
| [robot-p04-continuing-branches.svg](../../img/lec-03/robot-p04-continuing-branches.svg) | `L03R-04-05` |
| [robot-p04-forced-first-action.svg](../../img/lec-03/robot-p04-forced-first-action.svg) | `L03R-04-06` |
| [robot-p05-one-step-lookahead.svg](../../img/lec-03/robot-p05-one-step-lookahead.svg) | `L03R-05-01` |
| [robot-p05-low-battery-branches.svg](../../img/lec-03/robot-p05-low-battery-branches.svg) | `L03R-05-02` |
| [robot-p06-policy-evaluation-setup.svg](../../img/lec-03/robot-p06-policy-evaluation-setup.svg) | `L03R-06-01` |
| [robot-p07-three-actions-values.svg](../../img/lec-03/robot-p07-three-actions-values.svg) | `L03R-07-01` |
| [robot-p07-branch-wait.svg](../../img/lec-03/robot-p07-branch-wait.svg) | `L03R-07-02` |

Các trang suy diễn Bellman dùng công thức toàn chiều rộng làm hình chính. Bỏ các cây lặp dự kiến ở05-04…09 để đủ chỗ cho điều kiện và phép biến đổi; cây số đã có05-01/02. 06-05 dùng diễn giải hai hàng rồi bảng số thay hình gộp nhiều tầng; bảng ấy là đầu vào cho định nghĩa MRP06-06. Những thay đổi này không bỏ bước toán hoặc đảo thứ tự khái niệm.

03-04 đặt hai loại tổng ở hai cột, hiện lần lượt. 04-04 gộp hai trạng thái cuối cùng cho tổng3; nhãn1ở bước2 là xác suất chính sách chọnTìm, còn xác suất nhóm cuối là1/2. 06-03 đặt toàn bộ phép trừ/thế trong một khối căn dòng. 07-01 gắn ba giá trị vào hành động, không gắn vào trạng thái đích. Mọi nguồn và đáp án nằm trong notes; không đưa chỉ dẫn soạn lên mặt slide hoặc vào lời giảng.

## 12. Ghi chú toán học để triển khai và chữa bài

### Các kết quả số đã tính lại

Với bảng robot, chính sách và $\gamma=1/2$ đã chốt:

$$P^\pi=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\qquad
r^\pi=\begin{pmatrix}2\\1/2\end{pmatrix},\qquad
v=\begin{pmatrix}13/4\\7/4\end{pmatrix}.$$

| Cặp trạng thái–hành động | $q_\pi$ | Phép kiểm bằng $r+\gamma v$ |
|---|---:|---|
| H–Tìm | $13/4$ | $2+(1/2)[(1/2)(13/4)+(1/2)(7/4)]$ |
| H–Chờ | $21/8$ | $1+(1/2)(13/4)$ |
| L–Tìm | $3/4$ | $(1/2)[2+(1/2)(7/4)]+(1/2)[-3+(1/2)(13/4)]$ |
| L–Chờ | $15/8$ | $1+(1/2)(7/4)$ |
| L–Sạc | $13/8$ | $(1/2)(13/4)$ |

Các tổng ba bước có chiết khấu là $3/2$ và $7/4$. Trung bình của hai bước đầu từ H là $21/8$. Sự trùng số giữa một vài đại lượng là ngẫu nhiên trong bộ tham số đã chọn, không phải đẳng thức tổng quát giữa tổng thưởng ngắn hạn, giá trị trạng thái và giá trị hành động. Không đưa cả bảng năm $q$ lên slide nếu nó làm loãng nhiệm vụ đang xét.

### Cơ sở cho nghiệm duy nhất khi có chiết khấu

Ghi chú cho 06-07, không thêm slide chính. Gọi $d$ là nghiệm của hệ thuần nhất $(I-\gamma P^\pi)d=0$ và đặt $D=\max_i\lvert d_i\rvert$. Vì $P^\pi$ không âm, tổng mỗi hàng bằng 1:

$$\lvert d_i\rvert
=\left\lvert\gamma\sum_jP^\pi_{ij}d_j\right\rvert
\le\gamma\sum_jP^\pi_{ij}\lvert d_j\rvert
\le\gamma D.$$

Lấy lớn nhất theo $i$ được $D\le\gamma D$. Với $0\le\gamma<1$, suy ra $D=0$, nên ma trận vuông $I-\gamma P^\pi$ khả nghịch. Đây là lập luận đại số bổ sung, không trích thành định lý được đánh số của SB. Với robot, định thức bằng $(3/4)^2-(1/4)^2=1/2$, kiểm tra trực tiếp được.

Khi $\gamma=1$ và có trạng thái hấp thụ, ma trận đầy đủ $I-P^\pi$ có hàng 0, không dùng nghịch đảo đầy đủ. Đặt giá trị kết thúc bằng 0 và xét các trạng thái chưa kết thúc với điều kiện về thời gian kết thúc. Storyboard không tuyên bố cứ có trạng thái kết thúc thì mọi giá trị đều hữu hạn.

### Các điều kiện trong phép biến đổi Bellman

| Bước | Công cụ dùng | Điều chưa được suy ra ở bước đó |
|---|---|---|
| Tách $G_t$ | Đại số trên tổng hội tụ hoặc tổng hữu hạn | Chưa cần Markov, chưa lấy kỳ vọng. |
| Nhóm theo $A_t$ | Kỳ vọng toàn phần, chính sách xác định trọng số | Chưa bỏ tính ngẫu nhiên của môi trường. |
| Nhóm theo $(S_{t+1},R_{t+1})$ | Kỳ vọng lặp, hạt nhân chung, tuyến tính | Chưa bỏ các điều kiện quá khứ trong kỳ vọng tương lai. |
| Nhận diện $v_\pi(s')$ | Trạng thái Markov; chính sách Markov dừng; động lực và tiêu chuẩn không đổi theo thời gian | Không suy ra công thức tối ưu hoặc phép max. |
| Ghép $v$ và $q$ | Định nghĩa hai thí nghiệm, kỳ vọng theo hành động đầu | Không lấy trung bình hành động đầu lần nữa trong $q(s,a)$. |
| Dạng ma trận | Gom hệ số từ Bellman đã chứng minh | Khả nghịch cần điều kiện; không là giả thiết tự có với mọi gamma. |

## 13. Kiểm định bản triển khai

Bản triển khai dùng quy trình đa tác tử OpenRouter: reader lập kế hoạch/ánh xạ và kiểm storyboard; writer từng phần; năm reviewer độc lập theo hai góiA20slide+B30slide; correction writer riêng sau khi đủ báo cáo. Điều phối viên kiểm tra và sửa các đầu ra sai, không coi lời tự xác nhận của worker là bằng chứng. Chi tiết runtime, lỗi, quyết định và phạm vi rà lại nằm trong [review-log.md](review-log.md).

Rà theo Quill về điểm vào–ra, thứ tự ký hiệu và sự liên tục của robot xuyên suốt; không tạo quill.json. Biên tập nội dung hiển thị và notes theo no-ai-slop và eval.md. Mỗi phần kết thúc bằng ba câu hỏi đánh số; không thêm code demo. Bảy phần lần lượt12/18/14/17/30/21/8phút, tổng120phút;30phút chữa hw02 tách riêng.

Kiểm định RevealJS gồm HTML/ID/section, nguồn trong notes, công thức KaTeX, số học bằng phân số, đường dẫn, SVG và toàn bộ50slide ở1280×720/390×844. Bằng chứng cuối cùng và giới hạn Codex Slides được ghi trong nhật ký; không dùng kiểm định của deck cũ để chứng nhận bản robot.

## Ánh xạ ghi chú tự học theo bộ slide hiện hành — 20/09/2026

Ghi chú giữ bảy phần theo thứ tự của deck. Các slide tiêu đề được gộp vào đề mục; nội dung, ví dụ, công thức và lời giải được viết thành văn tự học. Bản cũ gồm 13 chủ đề Student/Racing Car được thay vì không còn khớp ví dụ và quan hệ tiên quyết của deck. Không thay 50 slide hay thời lượng 120 phút.

| Trang nguồn | Nội dung trang | Phần ghi chú |
|---|---|---|
| L03R-01-01 | Quá trình quyết định Markov (MDP) | lec-03-part-01 |
| L03R-01-02 | Nội dung bài học | lec-03-part-01 |
| L03R-01-03 | Robot thu gom lon | lec-03-part-01 |
| L03R-01-04 | Một bước tương tác | lec-03-part-01 |
| L03R-01-05 | Hai lịch sử, cùng trạng thái hiện tại | lec-03-part-01 |
| L03R-01-06 | Tính Markov | lec-03-part-01 |
| L03R-01-07 | Câu hỏi kiểm tra | lec-03-part-01 |
| L03R-02-01 | Mô hình xác suất của MDP | lec-03-part-02 |
| L03R-02-02 | Hai phản hồi của hành động Tìm | lec-03-part-02 |
| L03R-02-03 | Bảng phản hồi của robot | lec-03-part-02 |
| L03R-02-04 | Xác suất chuyển trạng thái và phần thưởng | lec-03-part-02 |
| L03R-02-05 | Xác suất chuyển và thưởng trung bình | lec-03-part-02 |
| L03R-02-06 | Các thành phần của MDP | lec-03-part-02 |
| L03R-02-07 | Câu hỏi kiểm tra | lec-03-part-02 |
| L03R-03-01 | Phần thưởng và tổng thưởng | lec-03-part-03 |
| L03R-03-02 | Nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn | lec-03-part-03 |
| L03R-03-03 | Điểm thưởng ở các thời điểm | lec-03-part-03 |
| L03R-03-04 | Tổng thưởng từ thời điểm hiện tại | lec-03-part-03 |
| L03R-03-05 | Điều kiện để tổng thưởng hữu hạn | lec-03-part-03 |
| L03R-03-06 | Câu hỏi kiểm tra | lec-03-part-03 |
| L03R-04-01 | Chính sách và hàm giá trị | lec-03-part-04 |
| L03R-04-02 | Một cách điều khiển robot | lec-03-part-04 |
| L03R-04-03 | Chính sách là phân phối trên hành động | lec-03-part-04 |
| L03R-04-04 | Trung bình trên các nhánh quỹ đạo | lec-03-part-04 |
| L03R-04-05 | Giá trị trạng thái | lec-03-part-04 |
| L03R-04-06 | Ấn định hành động đầu tiên | lec-03-part-04 |
| L03R-04-07 | Giá trị hành động | lec-03-part-04 |
| L03R-04-08 | Câu hỏi kiểm tra | lec-03-part-04 |
| L03R-05-01 | Phương trình Bellman | lec-03-part-05 |
| L03R-05-02 | Một bước từ pin thấp | lec-03-part-05 |
| L03R-05-03 | Tách phần thưởng tích lũy | lec-03-part-05 |
| L03R-05-04 | Lấy trung bình theo hành động đầu | lec-03-part-05 |
| L03R-05-05 | Lấy trung bình theo phản hồi môi trường | lec-03-part-05 |
| L03R-05-06 | Từ trạng thái kế tiếp đến giá trị tương lai | lec-03-part-05 |
| L03R-05-07 | Giá trị hành động từ phản hồi một bước | lec-03-part-05 |
| L03R-05-08 | Giá trị trạng thái từ các giá trị hành động | lec-03-part-05 |
| L03R-05-09 | Bellman kỳ vọng cho giá trị hành động | lec-03-part-05 |
| L03R-05-10 | Câu hỏi kiểm tra | lec-03-part-05 |
| L03R-06-01 | Đánh giá một chính sách từ mô hình | lec-03-part-06 |
| L03R-06-02 | Hệ Bellman của robot | lec-03-part-06 |
| L03R-06-03 | Giải hai phương trình giá trị | lec-03-part-06 |
| L03R-06-04 | Kiểm tra giá trị bằng các hành động | lec-03-part-06 |
| L03R-06-05 | Gộp các nhánh dưới chính sách | lec-03-part-06 |
| L03R-06-06 | Chuỗi Markov và MRP dưới chính sách | lec-03-part-06 |
| L03R-06-07 | Bellman dưới dạng ma trận | lec-03-part-06 |
| L03R-06-08 | Câu hỏi kiểm tra | lec-03-part-06 |
| L03R-07-01 | Tổng hợp và vận dụng | lec-03-part-07 |
| L03R-07-02 | Đọc một quyết định bằng mô hình và giá trị | lec-03-part-07 |
| L03R-07-03 | Bài tập và bước tiếp theo | lec-03-part-07 |
| L03R-07-04 | Câu hỏi kiểm tra | lec-03-part-07 |

Chu trình đọc: phần 1 lấy mẫu robot để dẫn vào Markov; phần 2 lấy cây phản hồi và bảng bảy hàng để định nghĩa mô hình; phần 3 lấy hai dãy thưởng để định nghĩa tổng và điều kiện hữu hạn; phần 4 lấy bảng chính sách và cây hai bước để định nghĩa giá trị; phần 5 lấy cây một bước từ L để suy diễn Bellman; phần 6 giải hệ robot trước khi gộp thành MRP và ma trận; phần 7 dùng kết quả hành động để vận dụng và giao bài tập. Mỗi phần kết thúc bằng ba câu hỏi kèm lời giải có thể mở khi tự học.
