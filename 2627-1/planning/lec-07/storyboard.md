# Storyboard Bài 07

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/thuật toán | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Cốt lõi | Linh hoạt |
|---|---|---|---|---|---|---|---|---:|---:|
| Định hướng | `L07-01`, `L07-02` | `L07-02` | không áp dụng: chỉ nối từ Bài 06 | không áp dụng | `L07-03` xác định sản phẩm học tập | `L07-03` | kết quả dạng bảng → phạm vi mới | 7 | 0 |
| Xấp xỉ và đặc trưng | `L07-04` | `L07-05` | `L07-06` | `L07-07`, `L07-08`, `L07-10` | `L07-09`, `L07-11` | `L07-11` | bảng tra → mô hình tuyến tính có miền, kích thước và giới hạn biểu diễn | 21 | 2 |
| MC tuyến tính | `L07-12` | `L07-13` | `L07-14` | `L07-15`, `L07-16` | `L07-16`, `X02` | `L07-16`, `X01` | return $G_t$ → gradient đầy đủ và cập nhật tuần tự | 19 | 2 |
| TD tuyến tính và Bellman chiếu | `L07-18` | `L07-18` | `L07-19`; ví dụ hình học `L07-21` | `L07-20`, `L07-20b`, `L07-22`, `L07-23` | `L07-24` | `L07-24`, `L07-35` | chuyển tiếp một bước → bán gradient → thuật toán → hình chiếu → trực giao → điểm cố định | 27 | 3 |
| So sánh MC–TD | `L07-25` | `L07-25` | không áp dụng: tổng hợp hai cụm đã có ví dụ | không áp dụng | `L07-25` | `L07-25` | hai đích đã học → phân biệt đối tượng phân tích | 3 | 0 |
| Điều khiển | `L07-26` | `L07-26`, `L07-28` | `L07-27`, `L07-30` (một bước số trước thuật toán) | `L07-28`, `L07-29` | `L07-30` | `L07-28`, `X03` | đặc trưng $x(s,a)$ → SARSA với chính sách $\varepsilon$-greedy hiện hành | 18 | 1 |
| Khác chính sách và bất ổn | `L07-31` | phần mở đầu `L07-31` | so sánh đích trên mẫu `L07-30` | quy tắc đích ở `L07-31`; phân loại ở `L07-32` | `L07-33`, `L07-34` | `L07-31`, `L07-33`, `L07-35` | đổi hành động kế tiếp sang cực đại → nhận diện trường hợp cần phân tích riêng | 16 | 1 |

Các khoảng trang trên không chồng lấn. Tổng phần chính là 111 phút cốt lõi và 9 phút linh hoạt; tổng chữa bài là 30 phút (`X01`: 8, `X02`: 10, `X03`: 12). Ký hiệu $x$, $w$, $G_t$ và $\delta_t$ được truyền nguyên dạng từ ví dụ sang công thức và bài tập.

## Bản đồ từng trang

| Mã | Luận điểm và bước học | Nguồn | Phút | Câu nối |
|---|---|---|---:|---|
| `L07-01` | Mở bài: tên bài, nội dung chính (xấp xỉ tuyến tính theo đặc trưng, Monte Carlo, TD, Sarsa, Q-learning), tác giả nguồn và liên kết ghi chú bài giảng; ghi chú diễn giả nêu vấn đề thay bảng bằng hàm tham số dùng chung. | tr. 1, 21–23 | 2 | Từ tên bài sang bảng giá trị của Bài 05–06 và lý do thay bằng hàm xấp xỉ. |
| `L07-02` | Từ bảng giá trị đến hàm xấp xỉ: Bài 05–06 lưu một giá trị riêng cho mỗi trạng thái hoặc cặp; hội tụ cần thăm mọi trạng thái (hoặc cặp) vô hạn lần, Robbins–Monro, GLIE với điều khiển Monte Carlo và Sarsa; bài này dùng chung $w$, một cập nhật đổi nhiều ước lượng nên lập luận theo từng ô không áp dụng trực tiếp; ba điểm đối chiếu Monte Carlo, TD, Sarsa, Q-learning (mục tiêu cập nhật với bootstrap, học theo hay khác chính sách, cách cải thiện chính sách). | tr. 3, 5–20 | 3 | Ba điểm đối chiếu dùng xuyên bài; sang nội dung và mục tiêu. |
| `L07-03` | Nội dung và mục tiêu: năm phần của bài cùng phần bài tập; năm mục tiêu kiểm tra được (viết xấp xỉ tuyến tính, tính cập nhật Monte Carlo/TD(0)/Sarsa, phân biệt gradient đầy đủ của Monte Carlo và bán gradient của TD, điểm cố định Bellman chiếu, phân biệt mục tiêu Sarsa và Q-learning và nhận diện bộ ba bất ổn); dự đoán trước điều khiển. | tr. 2–4, 21–44 | 2 | Dẫn vào phần đầu: giới hạn của bảng tra. |
| `L07-04` | Giới hạn của bảng tra: bảng $V\approx v_\pi$, $Q\approx q_\pi$ dễ phân tích nhưng khó mở rộng; ba khó khăn theo nguồn (không lưu hết khi không gian lớn hay liên tục; không tổng quát hóa; dữ liệu không iid và không dừng); câu hỏi về ô của trạng thái gần $s$. | tr. 22–23 | 3 | Hai giới hạn đầu dẫn tới hàm có tham số dùng chung; khó khăn thứ ba dẫn tới giả thiết lấy mẫu của các điều kiện hội tụ. |
| `L07-05` | Hàm giá trị có tham số: $\hat v(s,w)\approx v_\pi(s)$, $\hat q(s,a,w)\approx q_\pi(s,a)$ với $w\in\mathbb R^d$ dùng chung; hình bảng tra và mô hình tham số; ba lợi ích theo nguồn (chia sẻ thông tin; quyết định nhanh, không gian liên tục hoặc nhiều chiều). | tr. 23 | 2 | Vì $w$ dùng chung, một cập nhật có thể đổi nhiều dự đoán; trang sau tính một ví dụ. |
| `L07-06` | Tổng quát hóa qua tham số dùng chung: $\hat v=x(s)^Tw$, quy tắc $\Delta w=\alpha e\,x(s)$ (suy ra ở phần Monte Carlo); ví dụ đủ dữ kiện cho $\Delta\hat v(s)=0{,}4$, $\Delta\hat v(s')=0{,}3$; mức lan $\alpha e\,x(s')^Tx(s)$ tỉ lệ với tích vô hướng hai đặc trưng. | tr. 23, 32 | 3 | Từ ví dụ sang phát biểu bài toán dự đoán với hàm xấp xỉ. |
| `L07-07` | Bài toán dự đoán với hàm xấp xỉ: $\pi$ cố định trên MDP có phần thưởng bị chặn, $\gamma<1$ hoặc lượt kết thúc với xác suất 1, đặc trưng và tham số; tiêu chí $J_\mu(w)$ với $\mu$ là phân phối của trạng thái dùng để học (thường là tần suất khi chạy $\pi$); $v_\pi$ chưa biết nên phần sau dùng mục tiêu cập nhật tính từ mẫu. | tr. 23, 27, 34; Sutton–Barto §9.2 | 4 | Chọn lớp hàm tuyến tính cho $\hat v$. |
| `L07-08` | Hình thức: chọn lớp tuyến tính $\hat v(s,w)=x(s)^Tw$, $\hat q(s,a,w)=x(s,a)^Tw$ với $x,w\in\mathbb R^d$ và $\nabla_w\hat v=x(s)$; các lớp hàm khác của nguồn chỉ được gọi tên. | tr. 24–26 | 3 | Đặc trưng $x$ phải được thiết kế theo miền bài toán. |
| `L07-09` | Ứng dụng: thiết kế đặc trưng; ví dụ vector điều hướng của nguồn với thành phần hằng $1$ (hệ số chặn); ba nhận xét (đặc trưng tốt làm bài toán gần tuyến tính, đặc trưng kém gây sai số, nhập nhằng và chính sách kém, lý thuyết cổ điển giả sử đặc trưng cho trước); dải hình CartPole, Lunar Lander, cờ vua. | tr. 28–31 | 3 | Mở rộng đặc trưng sang cặp $(s,a)$ cho điều khiển. |
| `L07-10` | Hình thức: đặc trưng cho cặp trạng thái–hành động theo nguồn, $x(s,a)=[\phi(s);e_a;\phi(s)\otimes e_a;1]$, kích thước $p+m+mp+1$, vai trò trọng số đi kèm từng khối, $\hat q=\phi(s)^T(w^{(1)}+u_a)+c_a+b$; hệ quả: thiếu khối Kronecker thì hành động tham lam như nhau ở mọi trạng thái. | tr. 31 | 3 | Mọi cách mã hóa đều chịu chung giới hạn: hai đầu vào cùng vector đặc trưng nhận cùng dự đoán. |
| `L07-11` | Kiểm tra giới hạn biểu diễn: cùng vector đặc trưng thì cùng dự đoán; ví dụ đặc trưng hằng; mọi dự đoán nằm trong lớp $\{\Phi w\}$, sai số xấp xỉ là khoảng cách từ $v_\pi$ tới lớp này; câu hỏi: thêm dữ liệu không xóa được sai số xấp xỉ. | tr. 31 | 2 | Lớp hàm đã xác định; phần sau xây dựng mục tiêu cập nhật từ mẫu để học $w$. |
| `L07-12` | Vấn đề: $J_\mu$ cần $v_\pi$ chưa biết, nên thay bằng mục tiêu cập nhật tính từ mẫu ($G_t$ cho Monte Carlo, $R_{t+1}+\gamma\hat v(S_{t+1},w)$ cho TD) và mất mát mẫu $\ell_t$; mục tiêu không chứa $w$ cho gradient đầy đủ, mục tiêu chứa $w$ cho bán gradient; nhắc điểm đối chiếu thứ nhất (loại mục tiêu). | tr. 27, 32 | 3 | Xét mục tiêu không chứa $w$ trước: lợi tức Monte Carlo. |
| `L07-13` | Trực giác: lợi tức $G_t$ làm mục tiêu Monte Carlo; không bootstrap, không chứa $w$, phải chờ hết lượt; $\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s)$ nên $G_t$ là mẫu không chệch của $v_\pi(S_t)$; phương sai lớn. | tr. 27, 33 | 3 | Dùng một mẫu để xác định hướng sửa. |
| `L07-14` | Ví dụ số Monte Carlo trước khi đạo hàm: $\hat v=1$, $e_t=4$, $w_{t+1}=(1{,}8;-0{,}6)^T$, dự đoán mới $3$ (sai lệch từ $4$ xuống $2$); quy tắc $\Delta w=\alpha e_t x(S_t)$ dùng lại từ phần tổng quát hóa. | suy ra từ tr. 33 | 4 | Khái quát hướng sửa bằng gradient của mất mát mẫu. |
| `L07-15` | Hình thức: quy tắc của ví dụ là bước hạ gradient trên $\ell_t(w)=\tfrac12(G_t-\hat v)^2$; $\nabla_w\ell_t$, cập nhật tuyến tính; $G_t$ không chứa $w$ nên là gradient đầy đủ; gọi tên SGD. | tr. 32–34; HW4 | 4 | Đóng gói thành thuật toán. |
| `L07-16` | Thuật toán Monte Carlo tuyến tính: đầu vào/đầu ra, chỉ số $n$ của bước học khác $t$, sinh lượt, tính lùi lợi tức, cập nhật tuần tự mọi lần ghé; câu hỏi tổng quát hóa ($\Delta\hat v=0{,}8$ tại đặc trưng $(1;0)^T$). | tr. 33–34; HW4, HW7 | 3 | Nêu điều kiện để lặp cập nhật có bảo đảm. |
| `L07-17` | Điều kiện hội tụ của Monte Carlo tuyến tính theo nguồn tr. 34 (iid, đặc trưng bị chặn, Robbins–Monro); phân tích phương sai–độ lệch cho thấy cực tiểu trùng cực tiểu $J_\mu$; giả thiết cố định $\pi,\mu$, đặc trưng, $\mathbb E[G_t^2]<\infty$; nghiệm bằng $v_\pi$ chỉ khi lớp hàm chứa $v_\pi$. | tr. 34; HW4, HW6 | 4 | Monte Carlo chờ hết lượt; chuyển sang TD(0) cập nhật sau mỗi chuyển tiếp. |
| `L07-18` | Vấn đề và trực giác TD: Monte Carlo chờ hết lượt; TD(0) thay $G_{t+1}$ bằng $\hat v(S_{t+1},w_t)$, mục tiêu $y_t^{\mathrm{TD}}$, sai số TD $\delta_t$; cập nhật sau mỗi chuyển tiếp; mục tiêu chứa $w_t$ nên chệch khi $\hat v\ne v_\pi$; trạng thái kết thúc có giá trị tiếp nối 0. | tr. 27, 35–36 | 4 | Tính một chuyển tiếp trước khi khái quát. |
| `L07-19` | Ví dụ số TD một bước: $\hat v(S_t)=2{,}5$, $\hat v(S_{t+1})=1$, $y^{\mathrm{TD}}=1{,}9$, $\delta_t=-0{,}6$, $w_{t+1}=(0{,}44;0{,}88)^T$, dự đoán mới $2{,}2$; quy tắc như Monte Carlo với mục tiêu TD; mục tiêu cũng đổi sau cập nhật (ghi chú). | suy ra từ tr. 35–36 | 4 | Khái quát thành bán gradient và thuật toán. |
| `L07-20` | Hình thức: gradient đầy đủ của $\tfrac12\delta_t(w)^2$, TD(0) bỏ số hạng $\gamma x(S_{t+1})$ nên là bán gradient (câu hỏi nguồn tr. 32); quy tắc tuyến tính; bán gradient không là bước giảm của một mất mát cố định. | tr. 32, 35–36 | 3 | Đóng gói quy tắc thành thuật toán. |
| `L07-20b` | Thuật toán TD(0) tuyến tính: đầu vào/đầu ra, ngân sách chuyển tiếp, giá trị tiếp nối 0 khi kết thúc, $y$ và $\delta$ tính bằng cùng $w$. | tr. 35–36 | 2 | Xem ảnh Bellman có nằm trong lớp biểu diễn không. |
| `L07-21` | Vấn đề và trực giác: TD(0) dừng ở đâu; $\mathcal S$ hữu hạn, $\Phi$, lớp $\{\Phi w\}$, $T_\pi v=r_\pi+\gamma P_\pi v$; trung bình mục tiêu TD là $T_\pi(\Phi w)$, nói chung ngoài lớp nên TD chỉ khớp hình chiếu; ví dụ $(2;0)^T$ chiếu lên đường $c(1;1)^T$ cho $(1;1)^T$. | tr. 37; HW5 | 4 | Trọng số của phép chiếu xuất hiện từ trung bình cập nhật TD. |
| `L07-22` | Hình thức: với $S_t\sim d_\pi$ (phân phối dừng, $\mu=d_\pi$) và $w$ cố định, $\mathbb E[\delta_tx(S_t)]=\Phi^TD(T_\pi\Phi w-\Phi w)=b-Aw$; TD dừng về trung bình khi phần dư Bellman trực giao với các cột $\Phi$ theo $\langle u,v\rangle_D$. | HW5; tr. 37 | 4 | Chuyển điều kiện trực giao thành phương trình điểm cố định. |
| `L07-23` | Hình thức: phép chiếu theo $D$ (điểm gần nhất theo $\|\cdot\|_D$), $\Pi_D=\Phi(\Phi^TD\Phi)^{-1}\Phi^TD$; điều kiện dừng tương đương $\Phi w_{\mathrm{TD}}=\Pi_DT_\pi(\Phi w_{\mathrm{TD}})\iff Aw_{\mathrm{TD}}=b$; TD tìm điểm cố định của $\Pi_DT_\pi$, khác $\Pi_Dv_\pi$ của Monte Carlo (tr. 43). | HW5; tr. 43 | 5 | Gắn phương trình với điều kiện hội tụ. |
| `L07-24` | Ứng dụng và kiểm tra: điều kiện hội tụ của TD tuyến tính (Tsitsiklis và Van Roy, 1997): dữ liệu theo $\pi$ cố định, chuỗi ergodic với $d_\pi>0$; $\gamma<1$, đặc trưng bị chặn, $\Phi$ đủ hạng cột, Robbins–Monro; $u^TAu\ge(1-\gamma)\|\Phi u\|_D^2$ nên hệ trung bình ổn định, $w_t\to w_{\mathrm{TD}}$; câu hỏi đối tượng hội tụ. | tr. 35–37, 44–45; HW5–6 | 4 | So sánh mục tiêu Monte Carlo và TD trước khi điều khiển. |
| `L07-25` | Tổng hợp: bảng sáu hàng so sánh Monte Carlo và TD(0) (mục tiêu, thời điểm cập nhật, kỳ vọng mục tiêu, phương sai, loại cập nhật, nghiệm tuyến tính). | tr. 33–37 | 3 | Cả hai dự đoán với $\pi$ cố định; điều khiển cần $\hat q$ và chính sách thay đổi. |
| `L07-26` | Vấn đề điều khiển: dự đoán giữ $\pi$ cố định; chọn hành động không có mô hình cần $\hat q\approx q_\pi$ hoặc $q_*$ và $\pi_w\in\arg\max\hat q$; điểm đối chiếu thứ hai (hành vi/đích) và thứ ba (cải thiện chính sách); vừa bootstrap vừa cải thiện chính sách nên mục tiêu đổi liên tục (tr. 39). | tr. 38–39 | 3 | Chọn đặc trưng hành động cho ví dụ chuỗi. |
| `L07-27` | Ví dụ: chuỗi năm trạng thái của Bài 06 ($\gamma=1$, lượt tối đa ba bước), đặc trưng $x(s,a)=(d_{\text{trái}};u(a);1)^T$; hệ quả $\hat q(s,1)-\hat q(s,0)=-2w_2$ ở mọi $s$ nên hành động tham lam như nhau ở B, C, D. | tr. 40; HW7–8 | 5 | Dùng hành động kế tiếp thật trong Sarsa. |
| `L07-28` | Hình thức và trực giác Sarsa: thay $Q(S',A')$ bằng $\hat q(S',A',w)$; chính sách $\varepsilon$-tham lam hiện hành, phá hòa cố định; $\delta_t$ và $w_{t+1}=w_t+\alpha\delta_tx(S_t,A_t)$; $A_{t+1}$ do chính sách hiện hành chọn (học theo chính sách); câu hỏi thay bằng hành động tham lam. | tr. 38–39; HW8 | 3 | Tính một cập nhật Sarsa trên chuỗi. |
| `L07-30` | Ví dụ tính tay một bước Sarsa (HW8, mẫu $(D,0,-1,C,0)$, $\gamma=1$): $\hat q(D,0)=3$, $\hat q(C,0)=2$, $\delta_0=-2$, $w_1=(-0{,}2;0{,}6;-1{,}4)^T$; đặt trước thuật toán. | HW8 | 4 | Đóng gói các bước thành thuật toán Sarsa. |
| `L07-29` | Thuật toán Sarsa với hàm xấp xỉ: đầu vào/đầu ra, năm bước (chọn $A$, $A'$ theo $\varepsilon$-tham lam bằng $w$ trước cập nhật; mục tiêu với giá trị tiếp nối 0 khi kết thúc; cập nhật theo $x(S,A)$); phạm vi bảo đảm: chính sách đổi theo $w$ nên cần giả thiết riêng. | tr. 38–39, 45 | 4 | Kiểm mục tiêu Q-learning trên cùng mẫu $(D,0,-1,C,0)$. |
| `L07-31` | Vấn đề và hình thức Q-learning: thay $A_{t+1}$ bằng hành động cực đại; mục tiêu theo hai trường hợp (kết thúc / chưa kết thúc), cập nhật như Sarsa với $x(S_t,A_t)$; học khác chính sách (điểm đối chiếu thứ hai); câu hỏi so hai mục tiêu trên mẫu $(D,0,-1,C,0)$, $w_0=(1;1;-1)^T$. | tr. 38, 41; HW8 | 4 | Phân loại ba yếu tố của thiết lập khác chính sách. |
| `L07-32` | Hình thức hóa bộ ba bất ổn: Q-learning tuyến tính có đủ bootstrap, khác chính sách, xấp xỉ hàm, nên có thể phân kỳ (tr. 41); cần điều kiện riêng; hướng khắc phục theo nguồn (Bài 08 xét mạng mục tiêu). | tr. 37, 41 | 3 | Áp dụng ba câu hỏi nhận diện vào các quy tắc đã học. |
| `L07-33` | Kiểm tra bộ ba bất ổn: ba câu kiểm tra (biểu diễn, mục tiêu, phân phối) ứng với ba yếu tố; áp dụng cho Q-learning tuyến tính (đủ ba) và Sarsa tuyến tính (theo chính sách, chính sách đổi theo $w$); đáp án dạng bảng xuất hiện từng bước. | tr. 41–43; Bài tập 3 | 3 | Đặt kết luận vào đúng phạm vi lý thuyết (`L07-34`). |
| `L07-34` | Phạm vi các kết quả hội tụ: bảng bốn thiết lập (Monte Carlo tuyến tính, TD tuyến tính theo chính sách, điều khiển hoặc khác chính sách với xấp xỉ hàm, xấp xỉ phi tuyến) và kết quả bài đã nêu cho từng thiết lập; ghi chú diễn giả nêu kết quả MDP tuyến tính (tr. 42) và vấn đề mở (tr. 43). | tr. 34, 41–44 | 3 | Kiểm tra toàn bộ mạch suy luận (`L07-35`). |
| `L07-35` | Kiểm tra tổng hợp năm bước. | tổng hợp | 2 | Nối các khái niệm sang bài học sâu. |
| `L07-36` | Kết: bảo đảm tuyến tính không tự chuyển sang Deep Q-Network. | tr. 26, 41–45 | 2 | Chuyển sang phần bài tập dọc. |
| `X01` | Chữa HW4: đạo hàm MC. | HW4 | 8 | Từ công thức sang cập nhật tuần tự. |
| `X02` | Chữa HW7: ba cập nhật MC. | HW7 | 10 | Giữ cùng đặc trưng cho SARSA. |
| `X03` | Chữa HW8: ba cập nhật SARSA. | HW8 | 12 | Kết thúc bằng kiểm tra chỉ số và terminal. |

Chín phút linh hoạt nằm trong các khoảng không chồng lấn: `L07-04`–`L07-11` (2), `L07-12`–`L07-17` (2), `L07-18`–`L07-25` (3), `L07-26`–`L07-30` (1), `L07-31`–`L07-36` (1). Có thể rút phần trao đổi ở `L07-06`, `L07-16`, `L07-22`, `L07-23`, `L07-30` và `L07-33`. Không hiển thị phân tuyến hoặc thời lượng trên trang chiếu và ghi chú.

## Bản đồ sáu mạch

Bảy cụm khái niệm được chứa trong sáu mạch; cụm so sánh MC–TD nằm cuối M4.

| Mạch | Chức năng | Kết nối vào | Đầu ra | Cụm chứa | Trang |
|---|---|---|---|---|---|
| M1 | Mở đầu, cầu nối từ dạng bảng, ba trục phân tích và đích học tập | Kết quả dạng bảng của Bài 06 | Ba trục dùng xuyên bài và kỳ vọng học tập | Định hướng | `L07-01`–`L07-03` |
| M2 | Lý do cần xấp xỉ, chia sẻ tham số, đặc trưng và giới hạn biểu diễn | Ba trục của M1 | Lớp hàm tuyến tính với miền, kích thước và giới hạn rõ | Xấp xỉ và đặc trưng | `L07-04`–`L07-11` |
| M3 | Phân loại đích, MC tuyến tính từ ví dụ đến thuật toán và điều kiện | Lớp hàm của M2 | Thuật toán MC tuyến tính và điều kiện SGD | MC tuyến tính | `L07-12`–`L07-17` |
| M4 | TD(0), bán gradient, Bellman chiếu và so sánh MC–TD | Đích MC của M3 | Điểm cố định Bellman chiếu; bảng so sánh hai đích | TD tuyến tính và Bellman chiếu; so sánh MC–TD (cuối mạch) | `L07-18`–`L07-25` |
| M5 | Điều khiển: giá trị hành động, SARSA tuyến tính và cập nhật số | Điểm cố định và so sánh của M4 | Thuật toán SARSA control và một bước số | Điều khiển | `L07-26`–`L07-30` |
| M6 | Q-learning, deadly triad, phạm vi lý thuyết, kết luận và chữa bài dọc | SARSA của M5 | Phân biệt đích max, chẩn đoán bất ổn, ranh giới lý thuyết | Khác chính sách và bất ổn | `L07-31`–`L07-36` |

## Ánh xạ hai chiều ghi chú–trang chiếu

Mỗi trang trong 40 trang chiếu (`L07-01`–`L07-36`, `L07-20b` và `X01`–`X03`) thuộc đúng một chủ đề; cả 16 chủ đề đều có trang tương ứng. Bảng dưới đây đối chiếu trực tiếp với thuộc tính `data-note-topic-id` trong HTML.

| Topic | Trang chiếu |
|---|---|
| `lec-07-topic-13` | `L07-01`, `L07-02`, `L07-03` |
| `lec-07-topic-01` | `L07-04` |
| `lec-07-topic-02` | `L07-05`, `L07-06` |
| `lec-07-topic-03` | `L07-07`, `L07-08` |
| `lec-07-topic-04` | `L07-09`, `L07-10`, `L07-11` |
| `lec-07-topic-05` | `L07-12` |
| `lec-07-topic-06` | `L07-13`, `L07-14`, `L07-15`, `L07-16` |
| `lec-07-topic-15` | `L07-17`, `X01` |
| `lec-07-topic-07` | `L07-18`, `L07-19`, `L07-20`, `L07-20b` |
| `lec-07-topic-08` | `L07-21`, `L07-22`, `L07-23`, `L07-24` |
| `lec-07-topic-09` | `L07-25` |
| `lec-07-topic-10` | `L07-26`, `L07-27`, `L07-28`, `L07-30`, `L07-29` |
| `lec-07-topic-11` | `L07-31`, `L07-32`, `L07-33` |
| `lec-07-topic-14` | `L07-34` |
| `lec-07-topic-12` | `L07-35`, `L07-36` |
| `lec-07-topic-16` | `X02`, `X03` |

## Hàng chữa bài trong hành trình

Ba trang dọc `X01`–`X03` là hàng chữa bài 30 phút, nằm ngoài 120 phút chính: `X01` (8 phút) đạo hàm MC, `X02` (10 phút) cập nhật MC tuần tự, `X03` (12 phút) ba bước SARSA. Các trang dọc nằm trong M6 về vị trí trình chiếu nhưng thời lượng chữa bài không tính vào 120 phút chính.
