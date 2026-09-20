# Storyboard mới — Bài 03: Quá trình quyết định Markov

Ngày lập: 20-09-2026. Phạm vi: lập lại kế hoạch, chưa triển khai vào HTML. Soạn và tự rà trực tiếp trong phiên chính, không dùng sub-agent theo yêu cầu người dùng. Bản này đề xuất thay tuyến của `detailed-slide-plan.md`; `storyboard.md` hiện có vẫn ghi bản HTML đã triển khai.

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
| 5 | Phương trình Bellman | Các định nghĩa giá trị và kỳ vọng có điều kiện | Giải thích được từng dấu bằng và từng tầng lấy trung bình | 10 | 26 |
| 6 | Đánh giá một chính sách từ mô hình | Bellman cho một chính sách cố định | Giải hệ robot; suy ra chuỗi Markov, MRP và dạng ma trận | 8 | 25 |
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

**Mặt slide:** tên bài; Bài 03, Học tăng cường, học kỳ 1 năm 2026–2027, đơn vị theo mẫu hiện có. Không thêm tiêu đề phần 1 riêng.

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

**Cách thể hiện:** giữ hình hai lịch sử nhỏ ở trên; mở công thức sau. Đánh dấu điều kiện bên trái được thay bằng trạng thái và hành động hiện tại. Không gạch bỏ lịch sử như thể nó chưa từng tác động tới trạng thái.

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

**Mặt slide:** gọi $\mathcal S$ là tập trạng thái, $\mathcal A(s)$ là tập hành động hợp lệ, $\mathcal R$ là tập điểm thưởng hữu hạn. Từ một dòng cụ thể:

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
