# Bài 07. Xấp xỉ hàm trong Học tăng cường

Học phần Học tăng cường · Học kỳ 1, năm học 2026–2027.

Khi không gian trạng thái lớn hoặc liên tục, bảng giá trị của Bài 05–06 được thay bằng một hàm có tham số dùng chung. Bài này dùng lớp hàm tuyến tính theo đặc trưng, xây dựng cập nhật Monte Carlo (MC) và sai phân thời gian (TD) cho dự đoán, rồi Sarsa và mục tiêu Q-learning cho điều khiển. Mỗi bảo đảm hội tụ được nêu cùng giả thiết về chính sách, đặc trưng, phân phối dữ liệu và bước học.

## Bản đồ chủ đề

Bản đồ bốn nhóm: nhóm **cốt lõi** gồm 13 chủ đề `lec-07-topic-01` đến `lec-07-topic-12` và `lec-07-topic-14` tạo thành mạch chính (riêng mục 14.2 của `lec-07-topic-14` là đọc thêm); nhóm **cầu nối** gồm `lec-07-topic-13` tóm tắt tiên quyết từ Bài 06; nhóm **bổ sung** gồm `lec-07-topic-15` cho điều kiện hội tụ của Monte Carlo tuyến tính; nhóm **đọc thêm/thực hành** gồm `lec-07-topic-16` với tính tay bài 7–8. Sáu mạch chính: mở đầu và cầu nối; động cơ và đặc trưng; Monte Carlo; TD và Bellman chiếu; điều khiển và Sarsa; Q-learning, bộ ba bất ổn, phạm vi lý thuyết và tổng kết. Phần chữa bài dùng bài 4, 7 và 8. Thứ tự trình bày mỗi chủ đề theo vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng/giới hạn → kiểm tra; các chủ đề 13, 14 và 15 gộp bước trực giác với ví dụ vì chúng chỉ tóm tắt hoặc nêu hướng nghiên cứu, không có ví dụ tính được trong nguồn.

### Giới hạn của bảng tra

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mở đầu mạch nhu cầu xấp xỉ hàm, đặt vấn đề mà cả bài giải quyết.
- Kết nối vào: bảng $V\approx v_\pi$, $Q\approx q_\pi$ của Bài 05–06.
- Kết nối ra: dẫn tới nhu cầu chia sẻ tham số.
- Nguồn: tr. 22–23.

### Hàm có tham số dùng chung

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: nêu ý tưởng học hàm có tham số, ba lợi ích và hệ quả một cập nhật đổi nhiều dự đoán.
- Kết nối vào: giới hạn bảng tra.
- Kết nối ra: dẫn tới xấp xỉ tuyến tính cụ thể.
- Nguồn: tr. 23.

### Bài toán dự đoán và xấp xỉ tuyến tính

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: phát biểu bài toán dự đoán với $J_\mu$, chuẩn hoá ký hiệu $x$, $w$, $\Phi$ dùng suốt bài.
- Kết nối vào: ý tưởng hàm tham số.
- Kết nối ra: nền cho mọi cập nhật MC/TD tuyến tính phía sau.
- Nguồn: tr. 23–27, 34; $J_\mu$ theo Sutton và Barto, §9.2.

### Đặc trưng và giới hạn biểu diễn

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: cho thấy chất lượng đặc trưng quyết định chất lượng xấp xỉ.
- Kết nối vào: xấp xỉ tuyến tính.
- Kết nối ra: đặc trưng cho cặp trạng thái–hành động dùng lại trong ví dụ chuỗi; sai số xấp xỉ tách khỏi sai số ước lượng trước khi xây dựng mục tiêu cập nhật.
- Nguồn: tr. 28–31.

### Mục tiêu cập nhật

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: thay $v_\pi$ chưa biết bằng mục tiêu tính từ mẫu; phân biệt mục tiêu không chứa $w$ (gradient đầy đủ) với mục tiêu chứa $w$ (bán gradient).
- Kết nối vào: tiêu chí $J_\mu$ và lớp hàm tuyến tính.
- Kết nối ra: dẫn tới cập nhật Monte Carlo và TD.
- Nguồn: tr. 27, 32.

### Monte Carlo với hàm xấp xỉ

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: lợi tức làm mục tiêu không chệch, cập nhật theo gradient đầy đủ của mất mát bình phương.
- Kết nối vào: mục tiêu cập nhật.
- Kết nối ra: đối chiếu với bán gradient TD.
- Nguồn: tr. 33–34 và bài tập 4.

### TD(0) với hàm xấp xỉ

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mục tiêu một bước có bootstrap, cập nhật bán gradient sau mỗi chuyển tiếp.
- Kết nối vào: Monte Carlo phải chờ hết lượt.
- Kết nối ra: dẫn tới phân tích Bellman chiếu.
- Nguồn: tr. 35–36.

### Điểm cố định Bellman chiếu

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mô tả nghiệm mà TD tuyến tính hướng tới.
- Kết nối vào: TD(0) bán gradient.
- Kết nối ra: nền cho so sánh MC–TD và giới hạn lý thuyết.
- Nguồn: bài tập 5.

### Hai mục tiêu dự đoán

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: tổng hợp khác biệt về mục tiêu, kỳ vọng, phương sai, thời điểm cập nhật, loại gradient và nghiệm tuyến tính.
- Kết nối vào: Monte Carlo gradient đầy đủ và TD bán gradient, điểm cố định Bellman chiếu.
- Kết nối ra: dẫn tới điều khiển với giá trị hành động.
- Nguồn: tr. 37 và bài tập 2.

### Điều khiển với xấp xỉ hàm

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: chuyển từ dự đoán với chính sách cố định sang điều khiển với giá trị hành động; Sarsa tuyến tính trên chuỗi năm trạng thái.
- Kết nối vào: so sánh Monte Carlo và TD(0).
- Kết nối ra: dẫn tới Q-learning và bộ ba bất ổn.
- Nguồn: tr. 38–40 và bài tập 8.

### Q-learning và bộ ba bất ổn

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: nêu đích khác chính sách và nguy cơ bất ổn.
- Kết nối vào: Sarsa tuyến tính.
- Kết nối ra: dẫn tới giới hạn lý thuyết và kết luận.
- Nguồn: tr. 38–41 và bài tập 3.

### Phạm vi lý thuyết

- Nhóm: `cốt lõi`; mục 14.2 (kết quả cho MDP tuyến tính) là đọc thêm.
- Vai trò trong mạch: bảng phạm vi các kết quả hội tụ đã dùng trong bài; đọc thêm kết quả cho MDP tuyến tính.
- Kết nối vào: phân loại bằng ba câu kiểm tra bộ ba bất ổn.
- Kết nối ra: kiểm tra mạch suy luận và tổng kết.
- Nguồn: tr. 34, 41–44; kết quả MDP tuyến tính ở tr. 42 chỉ nêu bậc độ hối tiếc.

### Kiểm tra tổng hợp và tổng kết

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: năm bước phân tích một quy tắc cập nhật, áp dụng cho TD(0) tuyến tính; tổng kết bài.
- Kết nối vào: bảng phạm vi các kết quả hội tụ.
- Kết nối ra: học tăng cường sâu ở Bài 08; bài tập thực hành điều khiển.
- Nguồn: tổng hợp tr. 22–44; Bài tập tuần 7.

### Mở đầu: từ bảng giá trị đến hàm xấp xỉ

- Nhóm: `cầu nối`.
- Vai trò trong mạch: mở bài, nhắc điều kiện hội tụ dạng bảng, nêu ba điểm đối chiếu các thuật toán, nội dung và mục tiêu học tập.
- Kết nối vào: bảng giá trị, điều kiện GLIE và Robbins–Monro của Bài 05–06.
- Kết nối ra: câu hỏi điều gì thay đổi khi $Q$ là hàm tuyến tính dẫn vào nội dung mới.
- Nguồn: tr. 3, 5–20; chỉ tóm tắt điều kiện, không trình bày lại chứng minh dài.

### Hội tụ của Monte Carlo tuyến tính

- Nhóm: `bổ sung`.
- Vai trò trong mạch: điều kiện hội tụ của Monte Carlo tuyến tính, nghiệm là cực tiểu $J_\mu$; phép đạo hàm và vai trò Robbins–Monro (bài tập 4, 6).
- Kết nối vào: gradient và thuật toán Monte Carlo.
- Kết nối ra: Monte Carlo phải chờ hết lượt, dẫn tới TD(0).
- Nguồn: tr. 34; bài tập 4 và 6.

### Thực hành: chuỗi năm trạng thái

- Nhóm: `đọc thêm/thực hành`.
- Vai trò trong mạch: thực hành sau phần tổng kết, dùng cho chữa bài 7–8 (Monte Carlo trên một lượt, Sarsa trên ba mẫu) và khung mục tiêu cập nhật.
- Kết nối vào: chuỗi và đặc trưng của mục 12.2, Sarsa tuyến tính và mục tiêu Q-learning.
- Kết nối ra: củng cố các cập nhật Monte Carlo và Sarsa bằng phép tính đầy đủ trên cùng một thiết lập.
- Nguồn: tr. 40 và bài tập 7–8.

## Ký hiệu và quy ước

- Không gian trạng thái $\mathcal S$ và không gian hành động $\mathcal A$; trong ví dụ chuỗi, $\mathcal S = \{A, B, C, D, E\}$ với $A$ và $E$ là trạng thái kết thúc, $\mathcal A = \{0, 1\}$ với $0$ là đi trái, $1$ là đi phải.
- Chính sách $\pi$; khi điều khiển, chính sách tham lam theo ước lượng là $\pi_w(s) \in \arg\max_a \hat q(s,a,w)$.
- Chỉ số thời gian $t = 0, 1, 2, \dots$; phần thưởng nhận được khi chuyển ra khỏi $S_t$ là $R_{t+1}$, trạng thái kế là $S_{t+1}$. Phần thưởng gắn với trạng thái kết thúc được ký hiệu $R(A) = 1000$, $R(E) = 10$; mọi phần thưởng còn lại bằng $-1$; hệ số chiết khấu $\gamma = 1$ trong ví dụ chuỗi.
- Vector đặc trưng $x(s) \in \mathbb R^d$ cho giá trị trạng thái, $x(s,a) \in \mathbb R^d$ cho giá trị hành động; vector trọng số $w \in \mathbb R^d$; $w_t$ là trọng số sau $t$ lần cập nhật, $w_0$ là khởi tạo.
- $\Phi$ là ma trận đặc trưng với hàng là $x(s)^\top$; $D$ là ma trận chéo chứa phân phối dừng theo chính sách $d(s)$; $P_\pi$ là ma trận chuyển theo chính sách $\pi$; $r_\pi$ là vector phần thưởng kỳ vọng theo $\pi$.
- $\mu$ là phân phối trọng số trong mục tiêu hồi quy MC; không đồng nhất $\mu$ với phân phối dừng $d$ nếu chưa có giả thiết tương ứng.
- Kỳ vọng $\mathbb E_\pi[\cdot]$ tính theo quỹ đạo sinh bởi $\pi$; kỳ vọng có điều kiện $\mathbb E[\cdot \mid S_t = s, A_t = a]$.
- Bước học $\alpha_t$ theo số lần cập nhật; trong tính tay, $\alpha$ là hằng số cho từng bài.

<!-- note-topic-id: lec-07-topic-13 -->
## 1. Mở đầu

### 1.1. Từ bảng giá trị đến hàm xấp xỉ

Monte Carlo, TD(0), Sarsa và Q-learning ở Bài 05–06 lưu một giá trị riêng cho mỗi trạng thái hoặc mỗi cặp trạng thái–hành động. Các kết luận hội tụ dạng bảng đi kèm điều kiện: MDP hữu hạn, phần thưởng bị chặn, mọi trạng thái (hoặc cặp) được thăm vô hạn lần, và bước học thỏa Robbins–Monro với cập nhật sai phân thời gian. Điều khiển Monte Carlo và Sarsa cần thêm điều kiện tham lam trong giới hạn với thăm dò vô hạn (GLIE); Q-learning dạng bảng chỉ cần thăm mọi cặp vô hạn lần và bước học Robbins–Monro. Lập luận chứng minh dựa vào việc mỗi cặp có ước lượng riêng, được cập nhật vô hạn lần và không bị cập nhật ở cặp khác làm thay đổi. Nguồn tr. 5–20 trình bày phác thảo chứng minh cho điều khiển Monte Carlo với GLIE và cho Sarsa; bài này không lặp lại các phác thảo đó.

Bài này thay bảng bằng hàm $\hat v(s,w)$ và $\hat q(s,a,w)$ với vector tham số $w$ dùng chung cho mọi trạng thái. Một cập nhật tại một trạng thái làm đổi ước lượng ở nhiều trạng thái khác, nên lập luận hội tụ theo từng ô của bảng không còn áp dụng trực tiếp. Nguồn tr. 16 đặt câu hỏi điều gì xảy ra khi $Q$ là hàm tuyến tính hoặc mạng sâu; phần còn lại của bài trả lời câu hỏi này cho lớp hàm tuyến tính.

Các thuật toán trong bài được đối chiếu theo ba điểm (nguồn tr. 3):

1. loại mục tiêu cập nhật: lợi tức đầy đủ hay bootstrap, tức mục tiêu chứa ước lượng hiện tại, như mục tiêu TD(0) ở Bài 05;
2. học theo chính sách (dữ liệu sinh từ chính sách đang học) hay khác chính sách;
3. cách cải thiện chính sách.

Dự đoán học $v_\pi$ hoặc $q_\pi$ của một chính sách cố định; điều khiển vừa đánh giá vừa cải thiện chính sách.

::: exercise Câu hỏi kiểm tra
Nêu hai điều kiện của GLIE và giải thích vì sao thiếu điều kiện thăm vô hạn thì kết luận hội tụ dạng bảng không còn đứng vững.
:::

::: hint
Xét trung bình mẫu $Q_k(s,a)$ của một cặp chỉ có hữu hạn mẫu khi $k\to\infty$.
:::

::: solution
GLIE yêu cầu (i) $\lim_{k\to\infty} N_k(s,a) = \infty$ cho mọi cặp $(s,a)$ và (ii) $\pi_k$ hội tụ về chính sách tham lam theo $Q_k$. Nếu một cặp chỉ được thăm hữu hạn lần, trung bình mẫu tại cặp đó dừng ở một số hữu hạn mẫu nên sai số có thể không biến mất. Khi đó không thể kết luận $Q_k \to q_*$ cho mọi cặp, và chính sách tham lam theo $Q_k$ có thể bỏ qua một hành động có giá trị lớn hơn.
:::

### 1.2. Nội dung và mục tiêu

Bài gồm năm phần: hàm xấp xỉ và đặc trưng; Monte Carlo với hàm xấp xỉ; TD(0) và Bellman chiếu; điều khiển và Sarsa; Q-learning và bộ ba bất ổn. Phần bài tập chữa Bài 4, 7 và 8 của phiếu bài tập tuần 7. Dự đoán, với chính sách cố định, được xét trước điều khiển, khi chính sách thay đổi theo tham số. Các ví dụ số ở phần điều khiển và phần bài tập dùng chuỗi năm trạng thái của Bài 06 với một vector đặc trưng ba chiều.

Sau bài học, người học cần thực hiện được các công việc sau:

- Viết $\hat v$, $\hat q$ tuyến tính theo đặc trưng, nêu miền và kích thước.
- Tính cập nhật Monte Carlo, TD(0) và Sarsa tuyến tính trên ví dụ số.
- Phân biệt gradient đầy đủ (Monte Carlo) với bán gradient (TD).
- Nêu điểm cố định Bellman chiếu và giả thiết hội tụ của TD tuyến tính.
- Phân biệt mục tiêu Sarsa và Q-learning; nhận diện bộ ba bất ổn (deadly triad) trong một quy tắc cập nhật.

Kiến thức tiên quyết từ Bài 03–06: quá trình quyết định Markov (MDP), toán tử Bellman của một chính sách, dự đoán Monte Carlo và TD(0), điều khiển Monte Carlo, Sarsa và Q-learning dạng bảng, điều kiện GLIE và điều kiện Robbins–Monro. Toán cần dùng: tích vô hướng có trọng số, ma trận, phép chiếu trực giao theo chuẩn có trọng số và trị riêng. Bài không chứng minh hội tụ cho Sarsa hoặc Q-learning với xấp xỉ hàm và không xét các phương pháp actor-critic.

<!-- note-topic-id: lec-07-topic-01 -->
## 2. Nhu cầu xấp xỉ hàm

### 2.1. Giới hạn của bảng tra

Bảng lưu $V(s)\approx v_\pi(s)$ hoặc $Q(s,a)\approx q_\pi(s,a)$ riêng cho từng trạng thái hoặc từng cặp trạng thái–hành động. Cách biểu diễn này dễ phân tích nhưng khó mở rộng khi $|\mathcal S|$ hoặc $|\mathcal A|$ lớn hay liên tục (nguồn tr. 22–23). Có ba khó khăn.

1. Khi không gian trạng thái hoặc hành động lớn hay liên tục, không lưu được một ô cho mỗi phần tử. Mỗi ô cũng cần đủ lần thăm riêng để ước lượng của nó hội tụ, nên số mẫu cần có tăng theo số ô.
2. Bảng không tổng quát hóa. Hai trạng thái có tính chất giống nhau vẫn có hai ô độc lập, nên kinh nghiệm ở một trạng thái không làm đổi ước lượng ở trạng thái kia, dù hai giá trị có thể gần nhau.
3. Với mọi cách biểu diễn, dữ liệu học tăng cường không độc lập cùng phân phối (iid) và không dừng: các mẫu liên tiếp trong một lượt phụ thuộc nhau, và phân phối trạng thái được thăm thay đổi khi chính sách thay đổi. Khó khăn này xuất hiện lại trong giả thiết lấy mẫu của các điều kiện hội tụ ở phần Monte Carlo và TD.

Mục tiếp theo thay bảng bằng một hàm có tham số dùng chung để xử lý hai khó khăn đầu.

::: exercise Câu hỏi kiểm tra
Một bảng $Q$ có $|\mathcal S|\,|\mathcal A|$ ô; một hàm tham số có $d$ tham số dùng chung với $d\ll|\mathcal S|\,|\mathcal A|$. Giải thích vì sao bảng cần nhiều mẫu hơn để có ước lượng ở mọi cặp, và nêu cái giá của việc dùng chung tham số.
:::

::: hint
So sánh số đại lượng cần học và xét một mẫu tại cặp $(s,a)$ làm thay đổi những ước lượng nào.
:::

::: solution
Với bảng, mỗi ô chỉ thay đổi khi chính cặp đó được thăm, nên mọi cặp đều cần đủ mẫu riêng; số đại lượng cần học là $|\mathcal S|\,|\mathcal A|$. Với hàm tham số, mọi mẫu cập nhật cùng một vector $w$, nên một mẫu tại $(s,a)$ làm đổi ước lượng ở mọi cặp có đặc trưng tương tự; số đại lượng cần học giảm xuống $d$. Cái giá là một cập nhật cũng có thể làm sai lệch ước lượng ở các cặp khác, và lớp hàm có thể không biểu diễn đúng giá trị thật; hai vấn đề này được xét ở phần chia sẻ tham số và thiết kế đặc trưng.
:::

<!-- note-topic-id: lec-07-topic-02 -->
## 3. Hàm có tham số dùng chung

### 3.1. Hàm giá trị có tham số

Thay bảng bằng một hàm có tham số (nguồn tr. 23):

$$\hat v(s,w)\approx v_\pi(s),\qquad \hat q(s,a,w)\approx q_\pi(s,a),$$

trong đó $w\in\mathbb R^d$ là vector tham số dùng chung cho mọi trạng thái. Nguồn nêu ba lợi ích: quyết định nhanh, vì chỉ cần tính một hàm thay vì tra một bảng rất lớn; chia sẻ thông tin giữa các trạng thái qua $w$; và hỗ trợ không gian trạng thái liên tục hoặc nhiều chiều.

Trong hình minh họa của trang chiếu, trạng thái $s$ được đưa qua vector đặc trưng $x(s)$, rồi qua vector tham số $w$ để cho dự đoán $\hat v(s,w)$; dạng tuyến tính $\hat v(s,w)=x(s)^Tw$ được định nghĩa ở phần xấp xỉ tuyến tính. Số tham số $d$ thường nhỏ hơn nhiều so với số trạng thái, nhưng điều này không bắt buộc. Hàm có tham số cho ra một dự đoán ở cả trạng thái chưa gặp trong dữ liệu; dự đoán đó đúng đến đâu phụ thuộc vào đặc trưng và dữ liệu.

Vì $w$ dùng chung, một cập nhật có thể làm thay đổi dự đoán ở nhiều trạng thái; mục 3.2 tính một ví dụ.

### 3.2. Tổng quát hóa qua tham số dùng chung

Với dạng tuyến tính $\hat v(s,w)=x(s)^Tw$, dự đoán là tổ hợp tuyến tính các thành phần của $x(s)$ với hệ số $w$. Với sai lệch $e$ bằng mục tiêu cập nhật trừ $\hat v(s,w)$, quy tắc cập nhật cộng vào $w$ lượng $\Delta w=\alpha e\,x(s)$. Quy tắc này được suy ra ở phần Monte Carlo từ gradient của sai số bình phương; ở đây chỉ dùng hướng sửa của nó: khi $e>0$, $w$ dịch theo hướng làm $x(s)^Tw$ tăng.

Ví dụ. Cho $x(s)=(1;1)^T$, $x(s')=(1;0{,}5)^T$, $w=(0;0)^T$, $e=2$, $\alpha=0{,}1$. Khi đó

$$\Delta w=0{,}1\cdot2\cdot(1;1)^T=(0{,}2;\,0{,}2)^T,\qquad \Delta\hat v(s)=x(s)^T\Delta w=0{,}4,\qquad \Delta\hat v(s')=x(s')^T\Delta w=0{,}2+0{,}1=0{,}3.$$

Mẫu chỉ được quan sát tại $s$, nhưng dự đoán tại $s'$ cũng tăng. Tổng quát,

$$\Delta\hat v(s')=x(s')^T\Delta w=\alpha e\,x(s')^Tx(s),$$

nên mức lan sang $s'$ tỉ lệ với tích vô hướng hai vector đặc trưng. Khi $x(s')^Tx(s)=0$, cập nhật tại $s$ không làm đổi dự đoán tại $s'$; nếu đặc trưng là vector one-hot của trạng thái, mọi cặp đặc trưng khác nhau trực giao và mô hình trở về bảng tra. Cùng cơ chế cũng lan sai lệch: nếu mục tiêu tại $s$ sai, dự đoán ở $s'$ bị kéo theo, và đó là cái giá của tổng quát hóa. Hiện tượng này là một thành phần của bộ ba bất ổn ở phần Q-learning.

::: exercise Câu hỏi kiểm tra
Cho $x(s)=(1;0)^T$, $x(s')=(0;1)^T$, $x(s'')=(-1;1)^T$, $w=(0;0)^T$, $e=2$, $\alpha=0{,}1$. Tính độ đổi dự đoán tại $s$, $s'$, $s''$ sau một cập nhật tại $s$ và giải thích dấu của từng kết quả.
:::

::: hint
Tính $\Delta w=\alpha e\,x(s)$, rồi dùng $\Delta\hat v(\cdot)=x(\cdot)^T\Delta w$.
:::

::: solution
$\Delta w=(0{,}2;\,0)^T$. Do đó $\Delta\hat v(s)=0{,}2$, $\Delta\hat v(s')=0$ và $\Delta\hat v(s'')=-0{,}2$. Vì $x(s')^Tx(s)=0$, cập nhật tại $s$ không ảnh hưởng tới $s'$. Vì $x(s'')^Tx(s)=-1<0$, dự đoán tại $s''$ đổi ngược chiều với dự đoán tại $s$.
:::

<!-- note-topic-id: lec-07-topic-03 -->
## 4. Bài toán dự đoán và xấp xỉ tuyến tính

### 4.1. Bài toán dự đoán với hàm xấp xỉ

Thiết lập: chính sách $\pi$ cố định trên quá trình quyết định Markov (MDP) có phần thưởng bị chặn; trạng thái $S_t\in\mathcal S$, phần thưởng $R_{t+1}\in\mathbb R$; $0\le\gamma<1$, hoặc mọi lượt kết thúc với xác suất 1. Các điều kiện này bảo đảm $v_\pi$ tồn tại và hữu hạn (nguồn tr. 7–8 dùng giả thiết phần thưởng bị chặn). Mỗi trạng thái có vector đặc trưng $x(s)\in\mathbb R^d$; dự đoán $\hat v(s,w)$ phụ thuộc tham số $w\in\mathbb R^d$.

Cần chọn $w$ để $\hat v(\cdot,w)$ gần $v_\pi$. Muốn sửa $w$ có hướng, cần một tiêu chí đo $\hat v$ gần $v_\pi$ đến đâu; tiêu chí được dùng là sai số bình phương có trọng số

$$J_\mu(w)=\tfrac12\sum_{s\in\mathcal S}\mu(s)\bigl(v_\pi(s)-\hat v(s,w)\bigr)^2,\qquad \mu(s)\ge0,\ \sum_s\mu(s)=1,$$

trong đó $\mu$ là phân phối của các trạng thái dùng để học, thường là tần suất trạng thái khi chạy $\pi$; trạng thái có $\mu(s)$ lớn được ưu tiên độ chính xác. Khi lớp hàm không chứa $v_\pi$, không có $w$ làm sai số bằng 0 ở mọi trạng thái, nên đổi $\mu$ có thể đổi nghiệm tốt nhất. Với không gian trạng thái liên tục, tổng được thay bằng kỳ vọng theo $\mu$. Ký hiệu $d_\pi$ dành cho phân phối dừng của chuỗi trạng thái dưới $\pi$, dùng ở phần TD; hai phân phối chỉ trùng nhau khi $\mu$ được chọn bằng $d_\pi$.

Nguồn (tr. 34) phát biểu hội tụ của Monte Carlo "trên phân phối dữ liệu"; $J_\mu$ nêu tường minh phân phối đó và tương ứng sai số giá trị $\overline{VE}$ ở Sutton và Barto (ấn bản 2, §9.2), thêm hệ số $\tfrac12$ để gọn đạo hàm. Vì $v_\pi$ chưa biết, các phần sau thay $v_\pi(S_t)$ bằng mục tiêu cập nhật tính từ mẫu.

### 4.2. Xấp xỉ tuyến tính

Sau khi có tiêu chí $J_\mu$, cần chọn dạng của $\hat v$. Lớp hàm dùng trong bài là lớp tuyến tính theo tham số: dự đoán là tích vô hướng giữa vector đặc trưng và vector tham số (nguồn tr. 24),

$$\hat v(s,w) = x(s)^\top w, \qquad \hat q(s,a,w) = x(s,a)^\top w,$$

trong đó $x(s)\in\mathbb R^d$, $x(s,a)\in\mathbb R^d$ và $w\in\mathbb R^d$, nên mỗi dự đoán là một số. Gradient theo tham số là

$$\nabla_w \hat v(s,w) = x(s), \qquad \nabla_w \hat q(s,a,w) = x(s,a),$$

không phụ thuộc $w$. Vì vậy mọi cập nhật trong bài có dạng cộng vào $w$ một bội của vector đặc trưng, như quy tắc ở mục 3.2. Chi phí một lần dự đoán hoặc cập nhật tỉ lệ với số thành phần khác 0 của vector đặc trưng.

Nguồn tr. 25–26 còn nêu các lớp hàm khác: cây quyết định, rừng ngẫu nhiên, kernel, láng giềng gần nhất, cơ sở Fourier, tile coding và mạng nơ-ron; mạng nơ-ron biểu diễn mạnh nhưng tối ưu khó hơn và có ít bảo đảm hơn. Bài này dùng lớp tuyến tính vì gradient đơn giản và các kết quả hội tụ được nêu trong bài đều phát biểu cho lớp này. Đặc trưng $x(s,a)$ cho cặp trạng thái–hành động được xây dựng ở mục 5.

Giới hạn: khi $w$ chạy trên $\mathbb R^d$, các hàm $\hat v(\cdot,w)$ tạo thành không gian con sinh bởi các thành phần đặc trưng. Hàm giá trị nằm ngoài không gian con này có sai số xấp xỉ không xóa được bằng cách học $w$.

::: exercise Câu hỏi kiểm tra
Với $x(s) \in \mathbb R^d$, tập hợp $\{\hat v(\cdot, w) : w \in \mathbb R^d\}$ là gì về mặt hình học, và vì sao nói chung nó không phải toàn bộ không gian hàm trên $\mathcal S$?
:::

::: hint
Xét tổ hợp tuyến tính $a w_1 + b w_2$ của hai vector tham số và dự đoán tương ứng.
:::

::: solution
Với $\mathcal S$ hữu hạn, xếp các $x(s)^\top$ thành hàng của ma trận $\Phi$; khi đó vector dự đoán là $\Phi w$. Vì $\hat v(\cdot, a w_1 + b w_2) = a\,\hat v(\cdot, w_1) + b\,\hat v(\cdot, w_2)$, tập này đóng với tổ hợp tuyến tính, tức là không gian con cột của $\Phi$, có số chiều $\operatorname{rank}(\Phi)\le d$. Khi $\operatorname{rank}(\Phi) < |\mathcal S|$, không gian con này không chứa mọi hàm trên $\mathcal S$, nên tồn tại hàm giá trị có sai số xấp xỉ không thể loại bỏ chỉ bằng cách học $w$.
:::

<!-- note-topic-id: lec-07-topic-04 -->
## 5. Đặc trưng và giới hạn biểu diễn

### 5.1. Thiết kế đặc trưng

Với lớp tuyến tính, mọi thông tin mô hình dùng được về trạng thái nằm trong vector đặc trưng $x(s)$. Nguồn (tr. 31) cho ví dụ một bài toán điều hướng:

$$x(s) = [\,\text{khoảng cách tới đích},\ \text{khoảng cách tới vật cản},\ \text{tốc độ},\ 1\,]^\top.$$

Thành phần hằng $1$ có trọng số riêng, nên $\hat v$ có hệ số chặn: dự đoán có thể khác 0 khi mọi đại lượng đo được bằng 0. Các ví dụ CartPole, Lunar Lander và cờ vua của nguồn (tr. 28–30) cho thấy loại đại lượng thường dùng: vị trí, vận tốc của xe cùng góc, vận tốc góc của cột; trạng thái động học của tàu đổ bộ; quân, lượt đi và cấu trúc bàn cờ. Đây là minh họa, không phải bộ đặc trưng đầy đủ cho các bài toán đó.

Ba nhận xét của nguồn (tr. 31):

- đặc trưng tốt làm bài toán gần tuyến tính hơn, tức $v_\pi$ gần nằm trong lớp $\{x^\top w : w\in\mathbb R^d\}$;
- đặc trưng kém gây sai số xấp xỉ, nhập nhằng (hai trạng thái cần giá trị khác nhau nhận cùng vector đặc trưng) và chính sách kém;
- phần lớn lý thuyết cổ điển giả sử đặc trưng đã cho trước; việc học biểu diễn hầu như nằm ngoài các định lý đó.

Đặc trưng tốt giữ thông tin cần để dự đoán lợi tức dưới chính sách đang xét. Trong ví dụ chuỗi năm trạng thái ở phần điều khiển, đặc trưng $x(s,a)$ gồm khoảng cách tới tường trái, dấu của hành động và hằng số $1$; với bài toán lớn hơn, chọn đặc trưng là vấn đề mở. Mục 5.2 xây dựng đặc trưng cho cặp trạng thái–hành động; mục 5.3 xét nhập nhằng.

::: exercise Câu hỏi kiểm tra
Cho ba trạng thái $B, C, D$ với khoảng cách tới tường trái lần lượt $1, 2, 3$. Nếu hàm giá trị thực tăng tuyến tính theo khoảng cách này, vì sao đặc trưng $d_{\text{left}}(s)$ là lựa chọn tốt? Ngược lại, nếu giá trị thực không tuyến tính theo khoảng cách thì sao?
:::

::: hint
Xét $\hat v(s) = a\,d_{\text{left}}(s) + b$ và hỏi lớp này chứa những hàm nào.
:::

::: solution
Nếu $v$ tuyến tính theo $d_{\text{left}}$, thì $v(s) = a\,d_{\text{left}}(s) + b$ với một cặp $a,b$, và lớp xấp xỉ chứa đúng hàm này nên sai số xấp xỉ bằng không. Nếu $v$ không tuyến tính theo khoảng cách, chẳng hạn có dạng bậc hai, thì mọi hàm trong lớp đều lệch; học trọng số chỉ tìm được phép chiếu tốt nhất, và sai số xấp xỉ còn lại không thể xóa bằng dữ liệu nhiều hơn.
:::

### 5.2. Đặc trưng cho cặp trạng thái–hành động

Điều khiển cần giá trị hành động $\hat q(s,a,w)=x(s,a)^\top w$, nên vector đặc trưng phải phụ thuộc cả trạng thái lẫn hành động. Với đặc trưng trạng thái $\phi(s)\in\mathbb R^p$, $m$ hành động rời rạc và mã one-hot $e_a\in\mathbb R^m$ (thành phần thứ $a$ bằng 1, còn lại bằng 0), nguồn (tr. 31) ghép bốn khối:

$$x(s,a)=\begin{bmatrix}\phi(s)\\ e_a\\ \phi(s)\otimes e_a\\ 1\end{bmatrix}\in\mathbb R^{p+m+mp+1}.$$

Tích Kronecker $\phi(s)\otimes e_a$ thay mỗi thành phần $\phi_i$ bằng khối $\phi_i e_a$. Ví dụ với $p=m=2$, $\phi(s)=(\phi_1;\phi_2)^\top$ và hành động thứ nhất, $\phi(s)\otimes e_1=(\phi_1;0;\phi_2;0)^\top$.

Tách $w$ theo bốn khối thành $w^{(1)}\in\mathbb R^p$, $c\in\mathbb R^m$, các vector $u_1,\dots,u_m\in\mathbb R^p$ và hệ số $b$. Khi đó

$$\hat q(s,a,w)=\phi(s)^\top\bigl(w^{(1)}+u_a\bigr)+c_a+b.$$

Khối $\phi(s)$ cho trọng số $w^{(1)}$ mọi hành động dùng chung; khối $e_a$ cho hằng số $c_a$ riêng của hành động $a$; khối tích Kronecker cho trọng số $u_a$ riêng của hành động $a$ trên $\phi(s)$; thành phần $1$ cho hệ số chặn chung. Nếu bỏ khối tích Kronecker, hiệu $\hat q(s,a,w)-\hat q(s,a',w)=c_a-c_{a'}$ không phụ thuộc trạng thái, nên hành động tham lam như nhau ở mọi trạng thái.

Đổi thứ tự thành $e_a\otimes\phi(s)$ chỉ hoán vị tọa độ của khối này; lớp hàm không đổi. Khối $\phi(s)$ bằng tổng theo hành động của các tọa độ tương ứng trong khối tích Kronecker, và $1$ bằng tổng các thành phần của $e_a$. Vì vậy lớp hàm trùng với lớp của $[e_a;\phi(s)\otimes e_a]$, ma trận đặc trưng không đủ hạng cột và $w$ không duy nhất; hai khối dư giữ phần dùng chung giữa các hành động. Đây là một cách mã hóa; có thể thiết kế đặc trưng trực tiếp cho $(s,a)$. Ví dụ chuỗi năm trạng thái ở phần điều khiển dùng đặc trưng ba chiều gồm khoảng cách tới tường trái, dấu của hành động và hằng số $1$.

### 5.3. Nhập nhằng đặc trưng (aliasing)

Vì $\hat v(s,w)=x(s)^\top w$ chỉ phụ thuộc $s$ qua $x(s)$, hai trạng thái có cùng vector đặc trưng luôn nhận cùng dự đoán:

$$x(s_1)=x(s_2)\ \Longrightarrow\ \hat v(s_1,w)=\hat v(s_2,w)\quad\forall w.$$

Nếu $v_\pi(s_1)\ne v_\pi(s_2)$, không có $w$ nào cho đúng cả hai giá trị; đây là hiện tượng nhập nhằng (aliasing) mà nguồn (tr. 31) nêu như một hệ quả của đặc trưng kém. Trường hợp cực đoan: chỉ dùng đặc trưng hằng $x(s)=1$ thì mọi trạng thái cùng dự đoán $w$.

Tổng quát hơn, với $\mathcal S$ hữu hạn, xếp các $x(s)^\top$ thành hàng của ma trận $\Phi$; mọi vector dự đoán có dạng $\Phi w$, nằm trong không gian cột của $\Phi$ (bài kiểm tra ở mục 4). Sai số xấp xỉ được đo bằng $\min_w J_\mu(w)$, bằng một nửa bình phương khoảng cách (chuẩn trọng số $\mu$) từ $v_\pi$ tới lớp này. Cần tách nó khỏi sai số ước lượng: sai số xấp xỉ không đổi khi thêm dữ liệu, còn sai số ước lượng đến từ số mẫu hữu hạn và nhiễu, có thể giảm khi thêm mẫu. Muốn giảm sai số xấp xỉ phải đổi đặc trưng.

Vì $v_\pi$ chưa biết (mục 4.1), phần tiếp theo xác định mục tiêu cập nhật tính từ mẫu để học $w$.

::: exercise Câu hỏi kiểm tra
Cho hai trạng thái $s_1\ne s_2$ với $x(s_1)=x(s_2)$ và $v_\pi(s_1)=0$, $v_\pi(s_2)=2$, $\mu(s_1)=\mu(s_2)=\tfrac12$, không có trạng thái nào khác. Tìm dự đoán chung $c=\hat v(s_1,w)=\hat v(s_2,w)$ làm nhỏ nhất $J_\mu$ và giá trị nhỏ nhất đó, giả sử $c$ có thể nhận mọi giá trị thực.
:::

::: hint
Viết $J_\mu$ theo $c$ rồi lấy đạo hàm theo $c$.
:::

::: solution
$J_\mu=\tfrac12\bigl[\tfrac12(0-c)^2+\tfrac12(2-c)^2\bigr]$. Đạo hàm theo $c$ bằng $\tfrac12\bigl[c-(2-c)\bigr]=c-1$, bằng 0 khi $c=1$. Khi đó $J_\mu=\tfrac12\bigl[\tfrac12+\tfrac12\bigr]=\tfrac12$. Giá trị $\tfrac12$ là sai số xấp xỉ, ứng với khoảng cách 1 theo chuẩn trọng số $\mu$ ($\tfrac12\cdot1^2$): dù có bao nhiêu dữ liệu, mô hình với đặc trưng này không thể đạt $J_\mu$ nhỏ hơn.
:::


<!-- note-topic-id: lec-07-topic-05 -->
## 6. Mục tiêu cập nhật

### 6.1. Mục tiêu mẫu thay cho giá trị thật

Tiêu chí $J_\mu$ ở mục 4.1 cần $v_\pi(S_t)$, nhưng $v_\pi$ chưa biết. Các thuật toán trong bài thay $v_\pi(S_t)$ bằng một mục tiêu cập nhật $y_t$ tính từ mẫu (nguồn tr. 27, 32):

$$y_t^{\mathrm{MC}} = G_t, \qquad y_t^{\mathrm{TD}} = R_{t+1} + \gamma\, \hat v(S_{t+1}, w),$$

trong đó $G_t$ là lợi tức từ thời điểm $t$ đến cuối lượt (mục 7), còn mục tiêu TD dùng dự đoán hiện tại ở trạng thái kế tiếp (bootstrap). Với mỗi mẫu, xét mất mát bình phương cục bộ

$$\ell_t(w) = \frac{1}{2}\big(y_t - \hat v(S_t, w)\big)^2.$$

Cả hai trường hợp dẫn tới cùng một dạng cập nhật

$$w_{t+1} = w_t + \alpha_t \big(y_t - \hat v(S_t, w_t)\big) \nabla_w \hat v(S_t, w_t),$$

với trường hợp tuyến tính $w_{t+1} = w_t + \alpha_t \big(y_t - x(S_t)^\top w_t\big) x(S_t)$. Khác biệt nằm ở việc mục tiêu có chứa $w$ hay không:

- mục tiêu Monte Carlo $G_t$ không chứa $w$, nên biểu thức trên đúng là bước giảm theo gradient đầy đủ của $\ell_t$, đạo hàm chỉ đi qua $\hat v(S_t,w)$;
- mục tiêu TD chứa $w$ qua $\hat v(S_{t+1},w)$; cập nhật TD giữ $y_t$ cố định khi lấy đạo hàm, nên chỉ là bán gradient. Phần TD (mục 9) phân tích số hạng bị bỏ.

Loại mục tiêu là điểm đối chiếu thứ nhất nêu ở mục 1.1. Tên gradient đầy đủ hay bán gradient phụ thuộc đạo hàm có đi qua mục tiêu hay không, không phụ thuộc mô hình có tuyến tính hay không.

Khác với học có giám sát, "nhãn" $y_t$ ở đây phụ thuộc chính sách sinh dữ liệu, và với TD còn phụ thuộc chính mô hình đang học (nguồn tr. 27). Nguồn gọi chung công thức cập nhật là SGD/bán gradient; bài này tách hai trường hợp theo việc mục tiêu có chứa $w$.

::: exercise Câu hỏi kiểm tra
Viết $y_t^{\mathrm{TD}}$ tường minh và chỉ ra thành phần nào của nó phụ thuộc vào $w_t$.
:::

::: hint
Thay $\hat v(S_{t+1}, w)$ bằng $x(S_{t+1})^\top w$.
:::

::: solution
$y_t^{\mathrm{TD}} = R_{t+1} + \gamma\, x(S_{t+1})^\top w_t$. Thành phần $R_{t+1}$ không phụ thuộc $w_t$, còn $\gamma\, x(S_{t+1})^\top w_t$ phụ thuộc vào trọng số hiện tại. Vì mục tiêu thay đổi theo $w$, đạo hàm đầy đủ của $\ell_t$ có thêm số hạng từ $\partial y_t^{\mathrm{TD}}/\partial w$; cập nhật bán gradient bỏ qua số hạng đó.
:::

<!-- note-topic-id: lec-07-topic-06 -->
## 7. Monte Carlo với hàm xấp xỉ

### 7.1. Lợi tức làm mục tiêu Monte Carlo

Với lượt kết thúc ở thời điểm $T$, mục tiêu Monte Carlo (MC) là lợi tức từ thời điểm $t$ (nguồn tr. 33):

$$G_t = \sum_{k=0}^{T-t-1} \gamma^k R_{t+1+k}, \qquad y_t^{\mathrm{MC}} = G_t.$$

Mục tiêu này không bootstrap và không chứa $w$, nhưng chỉ biết được khi lượt kết thúc. Với chính sách $\pi$ cố định, định nghĩa giá trị trạng thái (Bài 03) cho

$$\mathbb E_\pi[G_t \mid S_t = s] = v_\pi(s),$$

nên $G_t$ là mẫu không chệch của $v_\pi(S_t)$; thay $v_\pi(S_t)$ trong $J_\mu$ bằng $G_t$ đúng theo kỳ vọng. Lợi tức tồn tại và hữu hạn dưới các điều kiện ở mục 4.1. Đổi lại, $G_t$ cộng nhiều phần thưởng ngẫu nhiên nên thường có phương sai lớn (nguồn tr. 33). Đẳng thức trên chỉ nói về từng mẫu $G_t$: nó không nói vector $w$ học được từ hữu hạn mẫu là không chệch, và không xác định $\mu$, vốn do cách lấy các trạng thái $S_t$ quyết định. Mục tiêu TD không có tính chất không chệch này khi $\hat v\ne v_\pi$ (mục 11 đối chiếu hai phương pháp).

### 7.2. Một cập nhật Monte Carlo

Cho $x(S_t)=(2;1)^\top$, $w_t=(1;-1)^\top$, lợi tức $G_t=5$ và $\alpha=0{,}1$. Dự đoán hiện tại và sai lệch (mục tiêu trừ dự đoán, như ở mục 3.2) là

$$\hat v(S_t,w_t)=x(S_t)^\top w_t=2-1=1,\qquad e_t=G_t-\hat v(S_t,w_t)=4.$$

Lợi tức lớn hơn dự đoán, nên tăng dự đoán theo hướng $x(S_t)$ bằng quy tắc $\Delta w=\alpha e_t\,x(S_t)$:

$$w_{t+1}=w_t+0{,}1\cdot4\cdot(2;1)^\top=(1;-1)^\top+(0{,}8;0{,}4)^\top=(1{,}8;-0{,}6)^\top.$$

Dự đoán mới là $x(S_t)^\top w_{t+1}=3{,}6-0{,}6=3$, nên sai lệch giảm từ $4$ xuống $2$. Mức tăng của dự đoán bằng $\alpha e_t\|x(S_t)\|^2=0{,}1\cdot4\cdot5=2$; nếu $e_t<0$, dự đoán giảm. Lợi tức $G_t$ do quỹ đạo cung cấp và không được tính lại khi $w$ đổi, vì mục tiêu Monte Carlo không chứa $w$. Mục 7.3 chỉ ra quy tắc này là bước giảm theo gradient của mất mát mẫu.

### 7.3. Gradient của mất mát Monte Carlo

Quy tắc ở mục 7.2 là một bước hạ gradient trên mất mát của một mẫu $(S_t,G_t)$. Thay $y_t=G_t$ vào mất mát mẫu của mục 6.1 và lấy đạo hàm theo quy tắc chuỗi:

$$\ell_t(w) = \frac{1}{2}\big(G_t - \hat v(S_t,w)\big)^2, \qquad \nabla_w\ell_t(w) = -\big(G_t - \hat v(S_t,w)\big)\nabla_w \hat v(S_t,w).$$

Bước $w_{t+1}=w_t-\alpha_t\nabla_w\ell_t(w_t)$ cho

$$w_{t+1} = w_t + \alpha_t \big(G_t - \hat v(S_t, w_t)\big) \nabla_w \hat v(S_t, w_t),$$

và với mô hình tuyến tính, $\nabla_w\hat v(S_t,w)=x(S_t)$, nên $w_{t+1}=w_t+\alpha_t\big(G_t-x(S_t)^\top w_t\big)x(S_t)$. Với các số ở mục 7.2 và $\alpha_t=0{,}1$, công thức cho đúng $w_{t+1}=(1{,}8;-0{,}6)^\top$. Vì $G_t$ không phụ thuộc $w$, đây là gradient đầy đủ của mất mát mẫu. Mỗi bước chỉ dùng một mẫu nên phương pháp là hạ gradient ngẫu nhiên (SGD); nguồn gọi chung công thức là SGD/bán gradient, còn bài này gọi trường hợp mục tiêu $G_t$ là gradient đầy đủ.

Với $w$ cố định (không phụ thuộc mẫu đang dùng) và $\mathbb E|G_t|<\infty$, lấy kỳ vọng theo trạng thái mẫu $S_t\sim\mu$ và dùng $\mathbb E_\pi[G_t\mid S_t]=v_\pi(S_t)$:

$$\mathbb E\big[\nabla_w\ell_t(w)\big] = -\mathbb E_\mu\big[(v_\pi(S_t)-\hat v(S_t,w))\,x(S_t)\big] = \nabla_w J_\mu(w).$$

Vậy về trung bình, mỗi bước đi theo hướng giảm của $J_\mu$. Các mẫu trong cùng một lượt tương quan với nhau, nên điều kiện hội tụ cần giả thiết về cách lấy mẫu (độc lập, hoặc chuỗi Markov trộn). Mục 8 nêu điều kiện để dãy bước như vậy hội tụ, cùng phép đạo hàm chi tiết (Bài tập 4) và vai trò của điều kiện bước học.

### 7.4. Thuật toán Monte Carlo tuyến tính

Đầu vào: chính sách $\pi$ cố định, đặc trưng $x$, hệ số chiết khấu $\gamma$, trọng số khởi tạo $w_0$, số lượt $K$ và lịch bước học $\alpha_n$, trong đó $n$ đếm số lần cập nhật (khác thời điểm $t$ trong lượt). Đầu ra: $w$.

1. Khởi tạo $w\leftarrow w_0$, $n\leftarrow1$. Lặp lại $K$ lượt các bước 2–4.
2. Sinh một lượt $S_0,R_1,S_1,\dots,S_T$ theo $\pi$ tới khi kết thúc.
3. Tính lùi lợi tức: $G_T=0$, $G_t=R_{t+1}+\gamma G_{t+1}$ với $t=T-1,\dots,0$.
4. Với $t=0,\dots,T-1$ (mọi lần ghé): $e_t\leftarrow G_t-x(S_t)^\top w$; $w\leftarrow w+\alpha_n e_t\,x(S_t)$; $n\leftarrow n+1$.

Bước 4 cập nhật tuần tự theo thứ tự thời gian: mẫu kế tiếp dùng $w$ vừa cập nhật, nên kết quả khác với việc gom cả lượt thành một bước theo tổng gradient. Thuật toán dùng mọi lần ghé; muốn dùng lần ghé đầu thì chỉ cập nhật tại lần đầu trạng thái xuất hiện trong lượt (Bài 05). Lợi tức tính từ quỹ đạo và không tính lại khi $w$ đổi. Chi phí mỗi bước tỉ lệ với số thành phần khác 0 của $x(S_t)$; bộ nhớ là $d$ tham số. Nếu thay các bước ngẫu nhiên bằng bình phương tối thiểu trên cả tập dữ liệu (theo lô), Monte Carlo tuyến tính gần bài toán hồi quy chuẩn (nguồn tr. 33).

Ví dụ: ở mục 7.2, $\Delta w=(0{,}8;0{,}4)^\top$. Trạng thái có đặc trưng $(1;0)^\top$ không được cập nhật trực tiếp, nhưng dự đoán của nó tăng $x^\top\Delta w=1\cdot0{,}8+0\cdot0{,}4=0{,}8$ vì dùng chung thành phần thứ nhất của $w$. Mục 16 (Bài tập 7) tính đủ một lượt cho sẵn theo cùng thuật toán, với $x(S_t,A_t)$ thay cho $x(S_t)$ để ước lượng giá trị hành động.

::: exercise Câu hỏi kiểm tra
Giải thích vì sao cập nhật Monte Carlo với hàm xấp xỉ là gradient đầy đủ, trong khi cùng dạng công thức với mục tiêu TD thì không.
:::

::: hint
So sánh sự phụ thuộc của $G_t$ và của $R_{t+1} + \gamma \hat v(S_{t+1}, w)$ vào $w$.
:::

::: solution
Với Monte Carlo, mục tiêu $G_t$ chỉ phụ thuộc phần thưởng trên quỹ đạo, không phụ thuộc $w$, nên $\nabla_w \frac{1}{2}(G_t - \hat v(S_t,w))^2 = -(G_t - \hat v(S_t,w))\nabla_w \hat v(S_t,w)$ đúng chính xác. Với TD, đặt $\delta_t(w)=R_{t+1}+\gamma\hat v(S_{t+1},w)-\hat v(S_t,w)$. Bước giảm theo gradient đầy đủ của $\frac12\delta_t(w)^2$ tỉ lệ với $\delta_t(w)[\nabla_w\hat v(S_t,w)-\gamma\nabla_w\hat v(S_{t+1},w)]$. Cập nhật TD chỉ giữ số hạng thứ nhất và bỏ số hạng chứa gradient tại trạng thái kế tiếp, nên là bán gradient.
:::

<!-- note-topic-id: lec-07-topic-15 -->
## 8. Hội tụ của Monte Carlo tuyến tính

### 8.1. Điều kiện hội tụ của Monte Carlo tuyến tính

Nếu dữ liệu độc lập cùng phân phối (iid), đặc trưng bị chặn và bước học thỏa điều kiện Robbins–Monro

$$\sum_n \alpha_n = \infty, \qquad \sum_n \alpha_n^2 < \infty,$$

thì SGD với mục tiêu Monte Carlo hội tụ tới cực tiểu của sai số bình phương trên phân phối dữ liệu (nguồn tr. 34). Ví dụ $\alpha_n=1/n$ thỏa cả hai điều kiện; $\alpha_n=1/\sqrt n$ thỏa điều kiện thứ nhất nhưng không thỏa điều kiện thứ hai.

Cực tiểu đó là cực tiểu của $J_\mu$. Với $S_t\sim\mu$ và $\mathbb E_\pi[G_t\mid S_t]=v_\pi(S_t)$,

$$\mathbb E\big[(G_t-\hat v(S_t,w))^2 \mid S_t\big] = \mathrm{Var}(G_t\mid S_t) + \big(v_\pi(S_t)-\hat v(S_t,w)\big)^2,$$

và số hạng phương sai không phụ thuộc $w$, nên mất mát kỳ vọng với $G_t$ và $J_\mu$ có cùng điểm cực tiểu. Vì vậy dự đoán hội tụ tới điểm cực tiểu $J_\mu$ trong lớp tuyến tính; điểm này bằng $v_\pi$ chỉ khi lớp hàm chứa $v_\pi$, phần dư là sai số xấp xỉ của mục 5.3.

Giả thiết đi kèm: chính sách $\pi$, phân phối $\mu$ và đặc trưng cố định; lợi tức có mômen bậc hai hữu hạn, $\mathbb E[G_t^2]<\infty$. Tính lồi không phải giả thiết mà là hệ quả: với mô hình tuyến tính, Hessian của mất mát là $x(S_t)x(S_t)^\top\succeq0$, nên mất mát lồi theo $w$. Các mẫu trong cùng một lượt tương quan, nên giả thiết iid của nguồn không khớp trực tiếp với cách lấy mẫu theo lượt; khi đó cần định lý cho dữ liệu từ chuỗi Markov trộn, với giả thiết riêng. Ma trận mômen $\mathbb E[x(S_t)x(S_t)^\top]$ đủ hạng chỉ cần để vector tham số tối ưu là duy nhất; mã hóa bốn khối ở mục 5.2 không đủ hạng, nhưng dự đoán tối ưu vẫn xác định. Nếu $\pi$ hoặc $\mu$ thay đổi trong quá trình học, đây không còn là cùng một bài toán tối ưu cố định.

Monte Carlo phải chờ hết lượt mới có mục tiêu; mục 9 xét TD(0), cập nhật sau mỗi chuyển tiếp.

### 8.2. Bài tập: đạo hàm cập nhật Monte Carlo

::: exercise Bài tập 4
Cho $\hat v(s,w)=x(s)^\top w$ (phiếu bài tập viết $\phi(s)$) và mất mát Monte Carlo của một mẫu

$$\ell_t(w)=\tfrac12\big(G_t-x(S_t)^\top w\big)^2.$$


1. Tính $\nabla_w\ell_t(w)$.
2. Suy ra một bước hạ gradient với bước học $\alpha_t$.
3. Nêu điều kiện để cập nhật hội tụ về cực tiểu toàn cục.
:::

::: hint
Dùng quy tắc dây chuyền và lưu ý $G_t$ không phụ thuộc $w$. Với câu 3, tính Hessian của $\ell_t$ rồi đối chiếu các điều kiện ở mục 8.1.
:::

::: solution
(1) Theo quy tắc dây chuyền,

$$\nabla_w \ell_t(w) = \tfrac12 \cdot 2\big(G_t - x(S_t)^\top w\big) \cdot \big(-x(S_t)\big) = -\big(G_t - x(S_t)^\top w\big)x(S_t).$$

Vì $G_t$ không phụ thuộc $w$, đây là gradient đầy đủ của $\ell_t$.

(2) Bước hạ gradient đi ngược chiều gradient:

$$w_{t+1} = w_t - \alpha_t \nabla_w \ell_t(w_t) = w_t + \alpha_t \big(G_t - x(S_t)^\top w_t\big)x(S_t),$$

đúng cập nhật Monte Carlo cần chứng minh.

(3) Hessian $\nabla_w^2\ell_t(w)=x(S_t)x(S_t)^\top\succeq0$, vì $u^\top x(S_t)x(S_t)^\top u=(x(S_t)^\top u)^2\ge0$ với mọi $u$; mất mát lồi, nên mọi cực tiểu địa phương là cực tiểu toàn cục. Các điều kiện (mục 8.1): $\pi$, $\mu$ cố định; $\mathbb E[G_t^2]<\infty$; đặc trưng bị chặn; mẫu iid (như nguồn tr. 34) hoặc chuỗi Markov trộn cho các mẫu trong cùng lượt; bước học thỏa Robbins–Monro. Khi đó $w_t$ hội tụ tới tập cực tiểu của mất mát kỳ vọng, cũng là tập cực tiểu của $J_\mu$. Ma trận $\mathbb E[x(S_t)x(S_t)^\top]$ đủ hạng chỉ cần để vector tham số cực tiểu là duy nhất.
:::

::: exercise Bài tập 6
Giả sử dãy bước học $\{\alpha_n\}_{n\ge1}$ thỏa điều kiện Robbins–Monro

$$\sum_n \alpha_n = \infty, \qquad \sum_n \alpha_n^2 < \infty$$

(phiếu bài tập viết chỉ số $t$). Giải thích vì sao hai điều kiện này phù hợp cho Monte Carlo và TD với xấp xỉ hàm: điều kiện thứ nhất giúp thuật toán còn tiếp tục học, điều kiện thứ hai giúp nhiễu tích lũy vẫn hữu hạn.
:::

::: hint
Với điều kiện thứ nhất, xét tổng quãng đường $w$ có thể đi khi $\sum_n\alpha_n<\infty$. Với điều kiện thứ hai, xét tổng phương sai của nhiễu tích lũy $\sum_n \alpha_n^2\,\mathrm{Var}[\text{nhiễu}_n]$.
:::

::: solution
Điều kiện $\sum_n \alpha_n = \infty$ bảo đảm tổng các bước đủ lớn để thuật toán còn tiếp tục học: nếu tổng hữu hạn và độ lớn mỗi cập nhật bị chặn, tổng quãng đường $w$ đi được bị chặn, nên với điểm khởi tạo đủ xa, $w$ có thể dừng ở nơi chưa tới nghiệm. Điều kiện $\sum_n \alpha_n^2 < \infty$ giữ tổng phương sai của nhiễu tích lũy $\sum_n \alpha_n^2\,\mathrm{Var}[\text{nhiễu}_n]$ hữu hạn khi phương sai nhiễu bị chặn, nên nhiễu không đẩy $w$ đi xa mãi. Hai điều kiện này dùng cho cả Monte Carlo và TD với xấp xỉ hàm. Ví dụ $\alpha_n=1/n$ thỏa cả hai điều kiện; $\alpha_n=1/\sqrt n$ thỏa điều kiện thứ nhất nhưng không thỏa điều kiện thứ hai (mục 8.1).
:::

<!-- note-topic-id: lec-07-topic-07 -->
## 9. TD(0) với hàm xấp xỉ

### 9.1. Mục tiêu TD(0) với hàm xấp xỉ

Monte Carlo phải chờ hết lượt để có $G_t=R_{t+1}+\gamma G_{t+1}$. Như TD(0) dạng bảng ở Bài 05, TD(0) thay phần còn lại $G_{t+1}$ bằng dự đoán hiện tại (nguồn tr. 35):

$$y_t^{\mathrm{TD}} = R_{t+1} + \gamma \hat v(S_{t+1}, w_t), \qquad \delta_t = y_t^{\mathrm{TD}} - \hat v(S_t, w_t).$$

Đại lượng $\delta_t$ gọi là sai số TD. Cập nhật thực hiện ngay sau một chuyển tiếp, không chờ hết lượt. Phần thưởng mang chỉ số $t+1$ vì nó nhận được sau khi rời $S_t$. Nếu $S_{t+1}$ là trạng thái kết thúc thì giá trị tiếp nối bằng 0 và mục tiêu là $R_{t+1}$.

Mục tiêu chứa $w_t$ (bootstrap). Với $\pi$ cố định,

$$\mathbb E_\pi[y_t^{\mathrm{TD}}\mid S_t]-v_\pi(S_t)=\gamma\,\mathbb E_\pi\big[\hat v(S_{t+1},w_t)-v_\pi(S_{t+1})\mid S_t\big],$$

nên khi $\hat v\ne v_\pi$ mục tiêu nói chung không còn là mẫu không chệch của $v_\pi(S_t)$ như lợi tức ở mục 7.1; độ chệch bằng $\gamma$ nhân sai số dự đoán trung bình ở trạng thái kế tiếp. Đổi lại, mục tiêu một bước chỉ chứa một phần thưởng ngẫu nhiên nên trong các thiết lập thường gặp có phương sai nhỏ hơn lợi tức đầy đủ (nguồn tr. 35), dù điều này không đúng trong mọi bài toán.

### 9.2. Một cập nhật TD(0)

Cho $x(S_t)=(1;2)^\top$, $x(S_{t+1})=(2;0)^\top$, $w_t=(0{,}5;1)^\top$, $R_{t+1}=1$, $\gamma=0{,}9$ và $\alpha=0{,}1$. Cả hai dự đoán dùng cùng $w_t$, tính trước khi cập nhật:

$$\hat v(S_t,w_t)=0{,}5+2=2{,}5,\qquad \hat v(S_{t+1},w_t)=1+0=1,$$

$$y_t^{\mathrm{TD}}=1+0{,}9\cdot1=1{,}9,\qquad \delta_t=1{,}9-2{,}5=-0{,}6.$$

Quy tắc giống Monte Carlo, với mục tiêu TD thay cho lợi tức, $\Delta w=\alpha\,\delta_t\,x(S_t)$; vector cập nhật là $x(S_t)$ của trạng thái hiện tại, không phải $x(S_{t+1})$:

$$w_{t+1}=(0{,}5;1)^\top+0{,}1\cdot(-0{,}6)\cdot(1;2)^\top=(0{,}5;1)^\top-(0{,}06;0{,}12)^\top=(0{,}44;0{,}88)^\top.$$

Dự đoán mới tại $S_t$ là $0{,}44+1{,}76=2{,}2$, giảm về phía mục tiêu $1{,}9$. Sau cập nhật, mục tiêu cũng đổi: $\hat v(S_{t+1},w_{t+1})=0{,}88$, nên nếu tính lại, mục tiêu là $1+0{,}9\cdot0{,}88=1{,}792$. Monte Carlo không có hiện tượng này vì $G_t$ không chứa $w$.

### 9.3. Bán gradient TD(0) tuyến tính

Mục tiêu TD chứa $w$. Với $\delta_t(w)=R_{t+1}+\gamma x(S_{t+1})^\top w-x(S_t)^\top w$, gradient đầy đủ của $\tfrac12\delta_t(w)^2$ là

$$\nabla_w\tfrac12\delta_t(w)^2=\delta_t(w)\big(\gamma x(S_{t+1})-x(S_t)\big),$$

nên bước giảm theo gradient đầy đủ là $\delta_t(w)\big(x(S_t)-\gamma x(S_{t+1})\big)$. TD(0) bỏ phần $\gamma\delta_t x(S_{t+1})$ của gradient, phần đến từ mục tiêu, tức giữ mục tiêu cố định khi lấy đạo hàm; vì vậy gọi là bán gradient (nguồn tr. 32, 35–36). Thay $y_t=y_t^{\mathrm{TD}}$ vào dạng cập nhật của mục 6.1 được cập nhật tuyến tính

$$\delta_t = R_{t+1} + \gamma x(S_{t+1})^\top w_t - x(S_t)^\top w_t, \qquad w_{t+1} = w_t + \alpha_t \delta_t x(S_t),$$

cùng quy tắc $\Delta w=\alpha\,\delta_t\,x(S_t)$ của mục 9.2. Số hạng bị bỏ đến từ việc mục tiêu thay đổi theo $w$, đúng hiện tượng ở mục 9.2 (mục tiêu từ $1{,}9$ thành $1{,}792$). Bán gradient không phải bước giảm của một mất mát cố định, nên không phân tích được như SGD của Monte Carlo ở mục 8; mục 10 tìm điểm mà nó hướng tới. Lấy gradient đầy đủ của $\tfrac12\delta_t^2$ dẫn tới một bài toán khác, cực tiểu sai số TD bình phương, không xét trong bài.

### 9.4. Thuật toán TD(0) tuyến tính

Đầu vào: chính sách $\pi$ cố định, đặc trưng $x$, hệ số chiết khấu $\gamma$, trọng số khởi tạo $w_0$, bước học $\alpha_n$, ngân sách $N$ chuyển tiếp. Đầu ra: $w$.

1. Khởi tạo $w\leftarrow w_0$; lấy trạng thái đầu $S$.
2. Lặp $n=1,\dots,N$: chọn $A\sim\pi(\cdot\mid S)$, quan sát $R$ và $S'$, rồi làm các bước 3–5.
3. Nếu $S'$ là trạng thái kết thúc thì $y\leftarrow R$; ngược lại $y\leftarrow R+\gamma x(S')^\top w$.
4. $\delta\leftarrow y-x(S)^\top w$; $w\leftarrow w+\alpha_n\,\delta\,x(S)$.
5. Nếu $S'$ kết thúc, lấy trạng thái đầu mới cho $S$; ngược lại $S\leftarrow S'$.

Mỗi bước dùng một chuyển tiếp, không cần chờ hết lượt; $y$ và $\delta$ tính bằng cùng $w$ trước khi cập nhật. Thuật toán dừng theo ngân sách $N$ hoặc một tiêu chuẩn đặt trước; một giá trị $\delta$ nhỏ ở một mẫu không chứng minh $w$ đã hội tụ. Bảo đảm hội tụ ở mục 10 cần dữ liệu sinh theo chính sách cố định $\pi$. Vì bán gradient không giảm một mất mát cố định, muốn biết $w$ dừng ở đâu khi lặp đủ lâu cần xét ảnh Bellman của $\hat v$ và lớp biểu diễn (mục 10). Chi phí mỗi bước tỉ lệ với số thành phần khác 0 của $x(S)$ và $x(S')$; bộ nhớ là $d$ tham số.

::: exercise Câu hỏi kiểm tra
Viết gradient đầy đủ của mất mát $\frac{1}{2}\big(y_t^{\mathrm{TD}}(w) - x(S_t)^\top w\big)^2$ với $y_t^{\mathrm{TD}}(w) = R_{t+1} + \gamma x(S_{t+1})^\top w$, rồi chỉ ra số hạng mà cập nhật bán gradient bỏ qua. Với số liệu của mục 9.2, tính số hạng đó tại $w_t$.
:::

::: hint
Đạo hàm theo quy tắc chuỗi: $e(w)=y_t^{\mathrm{TD}}(w)-x(S_t)^\top w$ phụ thuộc $w$ qua cả hai dự đoán.
:::

::: solution
Đặt $e(w) = y_t^{\mathrm{TD}}(w) - x(S_t)^\top w = R_{t+1} + \gamma x(S_{t+1})^\top w - x(S_t)^\top w$. Khi đó $\nabla_w e = \gamma x(S_{t+1}) - x(S_t)$ và gradient đầy đủ của $\frac12e(w)^2$ là $e(w)\big(\gamma x(S_{t+1}) - x(S_t)\big)$. Bước hạ gradient vì thế tỉ lệ với $e(w)[x(S_t)-\gamma x(S_{t+1})]$. Cập nhật bán gradient chỉ giữ phần $e(w_t)x(S_t)$, tức bỏ qua số hạng $-\gamma e(w_t)x(S_{t+1})$. Với số liệu mục 9.2, $e(w_t)=\delta_t=-0{,}6$: phần giữ lại là $-0{,}6\,(1;2)^\top=(-0{,}6;-1{,}2)^\top$, số hạng bị bỏ là $-0{,}9\cdot(-0{,}6)\,(2;0)^\top=(1{,}08;0)^\top$; hướng giảm theo gradient đầy đủ là tổng $(0{,}48;-1{,}2)^\top$.
:::

<!-- note-topic-id: lec-07-topic-08 -->
## 10. Điểm cố định Bellman chiếu

### 10.1. Ảnh Bellman và phép chiếu

Bán gradient TD(0) không giảm một mất mát cố định (mục 9.3), nên cần cách khác để biết $w$ dừng ở đâu. Xét $\mathcal S$ hữu hạn. Hàm giá trị là một vector trong $\mathbb R^{|\mathcal S|}$; ma trận $\Phi$ có hàng $x(s)^\top$ (mục 5.3), nên mọi dự đoán thuộc lớp biểu diễn $\{\Phi w: w\in\mathbb R^d\}$. Toán tử Bellman của chính sách $\pi$ là

$$T_\pi v = r_\pi + \gamma P_\pi v,$$

với $r_\pi(s)$ là phần thưởng kỳ vọng một bước và $P_\pi(s,s')$ là xác suất chuyển dưới $\pi$; $v_\pi$ là điểm cố định $T_\pi v_\pi=v_\pi$ (Bài 03–04).

Trung bình mục tiêu TD tại mỗi trạng thái chính là ảnh Bellman của dự đoán hiện tại:

$$\mathbb E_\pi\big[R_{t+1}+\gamma x(S_{t+1})^\top w\mid S_t=s\big]=r_\pi(s)+\gamma\sum_{s'}P_\pi(s,s')\,x(s')^\top w=\big(T_\pi(\Phi w)\big)(s).$$

Vector $T_\pi(\Phi w)$ nói chung nằm ngoài lớp biểu diễn; gần nó nhất trong lớp là hình chiếu $\Pi T_\pi(\Phi w)$. Mục 10.2 và 10.3 cho thấy TD dừng tại $w$ thỏa $\Phi w=\Pi T_\pi(\Phi w)$, với phép chiếu theo trọng số $D$. Ví dụ: lớp chỉ chứa các vector $c(1;1)^\top$ và $T_\pi(\Phi w)=(2;0)^\top$. Không tham số nào biểu diễn đúng $(2;0)^\top$; hình chiếu trực giao (theo tích vô hướng thông thường) lên đường thẳng là $\frac{a^\top u}{a^\top a}a$ với $a=(1;1)^\top$, $u=(2;0)^\top$, tức $\tfrac{2}{2}(1;1)^\top=(1;1)^\top$. Trong TD, các trạng thái không được thăm đều nhau, nên phép chiếu dùng tích vô hướng có trọng số $u^\top Dv$; mục 10.2 cho thấy trọng số đó xuất hiện từ trung bình của cập nhật TD. Phần này dùng kiến thức đại số tuyến tính về phép chiếu trực giao lên không gian con.

### 10.2. Hướng cập nhật trung bình của TD

Xét cập nhật TD(0) tuyến tính $w_{t+1}=w_t+\alpha_t\delta_t x(S_t)$ với $\delta_t=R_{t+1}+\gamma x(S_{t+1})^\top w_t-x(S_t)^\top w_t$. Giả sử chuỗi trạng thái dưới $\pi$ có phân phối dừng duy nhất $d_\pi$ (điều kiện này được nêu cùng các giả thiết hội tụ ở mục 10.4). Lấy $S_t$ theo $d_\pi$, tức tần suất dài hạn của mỗi trạng thái khi chạy $\pi$; trong ký hiệu của mục 4.1, đây là trường hợp $\mu=d_\pi$. Giữ $w$ cố định. Theo kỳ vọng một bước ở mục 10.1,

$$\mathbb E[\delta_t x(S_t)\mid S_t=s]=x(s)\Big(\mathbb E_\pi\big[R_{t+1}+\gamma x(S_{t+1})^\top w\mid S_t=s\big]-x(s)^\top w\Big)=x(s)\big((T_\pi\Phi w)(s)-(\Phi w)(s)\big).$$

Lấy trung bình theo $d_\pi$, với $D=\operatorname{diag}(d_\pi)$ và $z=T_\pi(\Phi w)-\Phi w$,

$$\mathbb E[\delta_t x(S_t)]=\sum_s d_\pi(s)\,x(s)\,z(s)=\Phi^\top D\big(T_\pi(\Phi w)-\Phi w\big)=\underbrace{\Phi^\top D r_\pi}_{b}-\underbrace{\Phi^\top D(I-\gamma P_\pi)\Phi}_{A}\,w,$$

trong đó bước cuối thay $T_\pi(\Phi w)=r_\pi+\gamma P_\pi\Phi w$. Đây là gợi ý của Bài tập 5: viết kỳ vọng của $\delta_t x(S_t)$ dưới dạng $b-Aw$.

Trọng số là $d_\pi$ vì khi dữ liệu sinh theo $\pi$, trạng thái $s$ được cập nhật với tần suất dài hạn $d_\pi(s)$. Với bài toán theo lượt, $d_\pi$ là tần suất thăm dài hạn khi các lượt nối tiếp nhau; $P_\pi$ trong $T_\pi$ chỉ gồm chuyển giữa các trạng thái chưa kết thúc (giá trị tại trạng thái kết thúc bằng 0). TD dừng về trung bình khi $b-Aw=0$, tức $\Phi^\top D z=0$: phần dư Bellman $z=T_\pi(\Phi w)-\Phi w$ trực giao với mọi cột $\phi_j$ của $\Phi$ theo tích vô hướng $\langle u,v\rangle_D=u^\top Dv$.

### 10.3. Điểm cố định Bellman chiếu

Phép chiếu theo $D$ đưa một vector $v$ tới điểm gần nhất trong lớp $\{\Phi w\}$ theo chuẩn $\|v\|_D=\sqrt{v^\top Dv}$; đây là chuẩn khi mọi trạng thái có $d_\pi(s)>0$ (chuỗi ergodic, giả thiết ở mục 10.4). Khi $\Phi^\top D\Phi$ khả nghịch,

$$\Pi_D=\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top D.$$

Hình chiếu đặc trưng bởi phần dư trực giao với các cột của $\Phi$ theo $D$: $\Phi^\top D(v-\Pi_Dv)=0$. Vì vậy điều kiện dừng ở mục 10.2 tương đương với phương trình điểm cố định

$$\Phi w_{\mathrm{TD}}=\Pi_D T_\pi(\Phi w_{\mathrm{TD}})\iff Aw_{\mathrm{TD}}=b.$$

Chứng minh (Bài tập 5). Từ $b-Aw=0$, tức $\Phi^\top D\big(T_\pi(\Phi w)-\Phi w\big)=0$, nhân trái với $\Phi(\Phi^\top D\Phi)^{-1}$ được $\Pi_DT_\pi(\Phi w)-\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top D\Phi w=\Pi_DT_\pi(\Phi w)-\Phi w=0$. Ngược lại, nếu $\Phi w=\Pi_DT_\pi(\Phi w)$ thì nhân trái với $\Phi^\top D$ và dùng $\Phi^\top D\Pi_D=\Phi^\top D$ được $\Phi^\top D\Phi w=\Phi^\top DT_\pi(\Phi w)$, tức $b-Aw=0$. Trên hình của mục 10.1, điểm cố định là trường hợp $\Pi T_\pi(\Phi w)$ trùng với chính $\Phi w$.

Ý nghĩa. TD hướng tới điểm cố định của toán tử Bellman chiếu $\Pi_DT_\pi$. Monte Carlo với $\mu=d_\pi$ cực tiểu $J_\mu=\tfrac12\|v_\pi-\Phi w\|_D^2$, nên hướng tới hình chiếu $\Pi_Dv_\pi$ của giá trị thật (mục 8.1); hai điểm chỉ trùng nhau trong trường hợp đặc biệt, chẳng hạn khi $v_\pi$ nằm trong lớp biểu diễn. Phép so sánh với $\Pi_Dv_\pi$ là diễn giải bổ sung từ ý lệch mục tiêu ở nguồn (tr. 43): TD giải phương trình điểm cố định Bellman chiếu, không trực tiếp cực tiểu sai số tới $v_\pi$.

Điều kiện khả nghịch chỉ cần để viết $\Pi_D$ bằng nghịch đảo và để vector tham số nghiệm là duy nhất. Nếu $\Phi$ không đủ hạng cột, dùng giả nghịch đảo; hình chiếu $\Pi_Dv$ vẫn xác định dù nhiều $w$ cho cùng dự đoán. Phương trình chỉ mô tả điểm dừng về trung bình; mục 10.4 nêu điều kiện để dãy cập nhật ngẫu nhiên thật sự hội tụ tới $w_{\mathrm{TD}}$.

::: exercise Câu hỏi kiểm tra
Giải thích vì sao phương trình $\Phi w_{\mathrm{TD}} = \Pi_D T_\pi(\Phi w_{\mathrm{TD}})$ cho thấy TD triệt tiêu sai số Bellman chiếu chứ không trực tiếp cực tiểu sai số $\|\hat v - v_\pi\|_D$.
:::

::: hint
So sánh hai đại lượng: $\|\Pi_D T_\pi \hat v - \hat v\|_D$ và $\|v_\pi - \hat v\|_D$.
:::

::: solution
Điểm cố định triệt tiêu sai số Bellman chiếu $\|\Pi_D T_\pi \hat v - \hat v\|_D$, tức khoảng cách giữa $\hat v$ và hình chiếu ảnh Bellman của nó. Nếu lớp hàm không chứa $v_\pi$, hình chiếu của $T_\pi \hat v$ nói chung không trùng hình chiếu của $v_\pi$, nên $\hat v$ tại điểm cố định có thể khác hình chiếu của $v_\pi$. TD giải bài toán điểm cố định Bellman chiếu, không trực tiếp cực tiểu khoảng cách tới $v_\pi$.
:::

### 10.4. Điều kiện hội tụ của TD tuyến tính

Phương trình $Aw=b$ chỉ mô tả điểm dừng về trung bình. Kết quả cổ điển của Tsitsiklis và Van Roy (IEEE Transactions on Automatic Control, 1997; nguồn tr. 44–45) cho TD tuyến tính theo chính sách cần hai nhóm điều kiện:

- dữ liệu: chính sách $\pi$ cố định, lấy mẫu theo chính sách; chuỗi trạng thái ergodic (từ mọi trạng thái có thể tới mọi trạng thái khác và không lặp theo chu kỳ), có phân phối dừng duy nhất với $d_\pi(s)>0$ mọi $s$;
- hệ cập nhật: $\gamma<1$; đặc trưng bị chặn; $\Phi$ đủ hạng cột (cùng với $d_\pi>0$, điều này làm $\Phi^\top D\Phi$ khả nghịch); bước học thỏa Robbins–Monro.

Dưới các điều kiện này, $w_t\to w_{\mathrm{TD}}$ với xác suất 1, trong đó $w_{\mathrm{TD}}$ là nghiệm duy nhất của $Aw=b$, tức điểm cố định Bellman chiếu.

Lý do hệ trung bình $\dot w=b-Aw$ ổn định: với phân phối dừng, $\|P_\pi v\|_D\le\|v\|_D$ với mọi $v$. Thật vậy, theo từng hàng, $\big((P_\pi v)(s)\big)^2\le\sum_{s'}P_\pi(s,s')v(s')^2$ (bất đẳng thức Jensen, tổng hàng không vượt 1); nhân với $d_\pi(s)$ rồi cộng được $\|P_\pi v\|_D^2\le(d_\pi^\top P_\pi)v^2\le d_\pi^\top v^2=\|v\|_D^2$, với $v^2$ lấy bình phương từng thành phần. Trong bài toán theo lượt, $P_\pi$ dưới ngẫu nhiên và $d_\pi^\top P_\pi\le d_\pi^\top$ (phần chênh là khối lượng khởi động lại), nên bất đẳng thức vẫn đúng. Đặt $v=\Phi u$,

$$u^\top Au=\|v\|_D^2-\gamma\,v^\top DP_\pi v\ge\|v\|_D^2-\gamma\|v\|_D\|P_\pi v\|_D\ge(1-\gamma)\|\Phi u\|_D^2,$$

dương khi $u\ne0$ vì $\Phi$ đủ hạng cột và $d_\pi>0$. Vì vậy mọi trị riêng của $A$ có phần thực dương, $A$ khả nghịch và $w_{\mathrm{TD}}=A^{-1}b$. Hướng trung bình $b-Aw$ kéo $w$ về $w_{\mathrm{TD}}$; điều kiện Robbins–Monro và tính trộn của chuỗi làm phần nhiễu triệt tiêu. Mã hóa bốn khối ở mục 5.2 không đủ hạng cột; khi đó nghiệm tham số không duy nhất.

Bảo đảm này chỉ dành cho dự đoán theo chính sách với chính sách cố định. Nó không chuyển sang Sarsa hay Q-learning với xấp xỉ hàm, vì ở đó chính sách đổi theo $w$ hoặc mục tiêu khác chính sách sinh dữ liệu (mục 12, 13).

<!-- note-topic-id: lec-07-topic-09 -->
## 11. Hai mục tiêu dự đoán

### 11.1. So sánh Monte Carlo và TD(0)

Cả Monte Carlo và TD(0) đều dự đoán $v_\pi$ với chính sách $\pi$ cố định. Bảng dưới gom các kết quả của mục 7–10, theo bảng so sánh ở nguồn tr. 37:

| Tiêu chí | Monte Carlo | TD(0) |
|---|---|---|
| Mục tiêu | $G_t$ | $R_{t+1} + \gamma \hat v(S_{t+1}, w)$ |
| Thời điểm cập nhật | cuối lượt | sau mỗi chuyển tiếp |
| Kỳ vọng mục tiêu | bằng $v_\pi(S_t)$ | nói chung lệch khi $\hat v$ sai |
| Phương sai mục tiêu | thường cao hơn | thường thấp hơn |
| Loại cập nhật | gradient đầy đủ | bán gradient |
| Nghiệm tuyến tính | điểm cực tiểu $J_\mu$ ($\Pi_Dv_\pi$ khi $\mu=d_\pi$) | điểm cố định Bellman chiếu |

Kỳ vọng của mục tiêu Monte Carlo bằng $v_\pi(S_t)$ (mục 7.1); độ chệch của mục tiêu TD bằng $\gamma$ nhân sai số dự đoán trung bình ở trạng thái kế tiếp (mục 9.1). Hàng phương sai theo nguồn tr. 37 và chỉ đúng trong các thiết lập thường gặp: mục tiêu TD chứa một phần thưởng ngẫu nhiên, lợi tức chứa cả phần còn lại của lượt. Với cùng đặc trưng, hai phương pháp nói chung cho hai dự đoán khác nhau khi hội tụ: với $\mu=d_\pi$, Monte Carlo cho $\Pi_Dv_\pi$, TD cho điểm cố định của $\Pi_DT_\pi$ (mục 10.3).

Nguồn tóm tắt: Monte Carlo dễ phân tích về thống kê vì gần bài toán hồi quy; TD hiệu quả hơn về tính toán vì cập nhật trực tuyến, nhưng phân tích khó hơn. Bảng nguồn còn một hàng về học khác chính sách cùng xấp xỉ hàm: Monte Carlo có thể dùng lấy mẫu quan trọng nhưng phương sai lớn, TD có nguy cơ phân kỳ; hàng này được xét ở mục 13 cùng bộ ba bất ổn. Phần tiếp theo chuyển từ dự đoán sang điều khiển, nơi cần $\hat q$ và chính sách thay đổi theo $w$.

::: exercise Câu hỏi kiểm tra (bài tập 2)
So sánh dự đoán Monte Carlo và dự đoán TD(0) với xấp xỉ tuyến tính theo bốn tiêu chí: dạng mục tiêu, độ chệch và phương sai, khả năng cập nhật trực tuyến, độ khó phân tích lý thuyết.
:::

::: hint
Dùng bảng trên; với lý thuyết, nhớ Monte Carlo gần hồi quy còn TD cần toán tử Bellman chiếu.
:::

::: solution
Monte Carlo dùng mục tiêu $G_t$, lợi tức đầy đủ không phụ thuộc $w$, nên kỳ vọng của mục tiêu bằng $v_\pi(S_t)$ nhưng phương sai thường cao. TD(0) dùng $R_{t+1} + \gamma x(S_{t+1})^\top w_t$, nên mục tiêu nói chung lệch khi $\hat v$ sai nhưng phương sai thường thấp hơn. Monte Carlo phải chờ hết lượt; TD cập nhật ngay sau mỗi chuyển tiếp. Về lý thuyết, Monte Carlo là hạ gradient ngẫu nhiên trên sai số bình phương, hội tụ tới cực tiểu $J_\mu$ dưới điều kiện lấy mẫu và Robbins–Monro (mục 8.1); TD tuyến tính cần phân tích hệ trung bình $b-Aw$ và toán tử Bellman chiếu, với chuỗi ergodic, $\gamma < 1$, $\Phi$ đủ hạng cột và Robbins–Monro (mục 10.4).
:::

<!-- note-topic-id: lec-07-topic-10 -->
## 12. Điều khiển với xấp xỉ hàm

### 12.1. Giá trị hành động cho điều khiển

Phần dự đoán (mục 7–11) giữ chính sách $\pi$ cố định. Điều khiển phải chọn hành động mà không có mô hình. Với giá trị trạng thái, chọn hành động tham lam cần mô hình để tính $\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$; với giá trị hành động, chỉ cần so sánh các giá trị. Vì vậy, như Bài 06, ta học giá trị hành động (nguồn tr. 38):

$\hat q(s,a,w)=x(s,a)^\top w$ xấp xỉ $q_\pi$ của chính sách đang chạy (Sarsa) hoặc $q_*$ (Q-learning), và chính sách tham lam là

$$\pi_w(s)\in\arg\max_{a\in\mathcal A(s)}\hat q(s,a,w),$$

trong đó $x(s,a)$ là đặc trưng cặp trạng thái–hành động (mục 5.2) và $\pi_w$ phá hòa theo một quy tắc cố định. Hai điểm đối chiếu của mục 1.1 xuất hiện ở đây: chính sách hành vi sinh dữ liệu còn chính sách đích xác định giá trị cần học, và chính sách hành vi cần thăm dò, thường là $\varepsilon$-tham lam theo $\hat q$ như Bài 06; chính sách được cải thiện theo $\hat q$, nên thay đổi khi $w$ thay đổi.

Điều khiển cải thiện chính sách trong lúc học; với TD (Sarsa, Q-learning), mục tiêu còn bootstrap. Vì vậy mục tiêu thay đổi liên tục và dữ liệu không còn đến từ một phân phối cố định (nguồn tr. 39). Điểm cố định Bellman chiếu của mục 10 được chứng minh cho một chính sách cố định, nên không tự bảo đảm chính sách tham lam suy ra từ $\hat q$ là chính sách tốt. Nguồn tr. 39 đặt câu hỏi Monte Carlo hay TD(0) khó hội tụ hơn trong điều khiển; với xấp xỉ hàm, cả hai đều mất giả thiết chính sách cố định, và TD còn thêm mục tiêu bootstrap.

### 12.2. Chuỗi năm trạng thái với đặc trưng tuyến tính

Các ví dụ điều khiển và bài tập dùng chuỗi năm trạng thái của Bài 06 (nguồn tr. 40; Bài tập 7–8): $\mathcal S=\{A,B,C,D,E\}$, D là trạng thái đầu, A và E là trạng thái kết thúc; hành động 0 đi trái, 1 đi phải; môi trường tất định; thưởng khi đi vào A bằng 1000, vào E bằng 10, các chuyển khác bằng $-1$; $\gamma=1$; mỗi lượt tối đa ba bước. Giới hạn ba bước do nguồn nêu bằng lời; có thể xem đây là bài toán chân trời hữu hạn, và nếu cần trạng thái Markov thuần nhất thì thêm chỉ số thời gian vào trạng thái. $\gamma=1$ hợp lệ vì mỗi lượt hữu hạn nên lợi tức hữu hạn.

Đặc trưng ba chiều được thiết kế trực tiếp cho cặp $(s,a)$:

$$x(s,a)=\begin{bmatrix}d_{\text{trái}}(s)\\u(a)\\1\end{bmatrix},\qquad u(0)=1,\ u(1)=-1,\qquad \hat q(s,a,w)=x(s,a)^\top w,$$

với $d_{\text{trái}}(B)=1$, $d_{\text{trái}}(C)=2$, $d_{\text{trái}}(D)=3$ là khoảng cách tới tường trái. Đây không phải mã hóa bốn khối của mục 5.2: nó thiếu khối tích Kronecker, nên

$$\hat q(s,1,w)-\hat q(s,0,w)=[w]_2\,\big(u(1)-u(0)\big)=-2[w]_2$$

ở mọi $s$, trong đó $[w]_2$ là thành phần thứ hai của $w$ (hệ số của $u(a)$; ký hiệu $[w]_i$ để không lẫn với $w_t$ theo thời gian), và hành động tham lam như nhau ở B, C, D. Trong ví dụ này, đi trái là tối ưu ở mọi trạng thái, nên hạn chế đó chưa gây sai lựa chọn. Mục 16 dùng cùng thiết lập cho Bài tập 7 và 8.

### 12.3. Mục tiêu Sarsa với hàm xấp xỉ

Như Sarsa dạng bảng ở Bài 06, thay $Q(S_{t+1},A_{t+1})$ bằng $\hat q(S_{t+1},A_{t+1},w_t)$ (nguồn tr. 38). Hành động được chọn theo chính sách $\varepsilon$-tham lam hiện hành theo $\hat q(\cdot,\cdot,w_t)$, phá hòa theo một quy tắc cố định:

$$\delta_t = R_{t+1} + \gamma \hat q(S_{t+1}, A_{t+1}, w_t) - \hat q(S_t, A_t, w_t), \qquad w_{t+1} = w_t + \alpha_t \delta_t \nabla_w \hat q(S_t, A_t, w_t).$$

Với $\hat q$ tuyến tính, $\nabla_w\hat q(S_t,A_t,w)=x(S_t,A_t)$, đặc trưng của cặp vừa thực hiện, không phải $x(S_t)$:

$$w_{t+1} = w_t + \alpha_t \delta_t x(S_t, A_t), \qquad \delta_t = R_{t+1} + \gamma x(S_{t+1}, A_{t+1})^\top w_t - x(S_t, A_t)^\top w_t.$$

$A_{t+1}$ là hành động chính sách hiện hành thực sự chọn, kể cả khi thăm dò, nên Sarsa học theo chính sách. Nếu $S_{t+1}$ là trạng thái kết thúc thì giá trị tiếp nối bằng 0 và mục tiêu là $R_{t+1}$. Cả hai giá trị trong $\delta_t$ dùng cùng $w_t$, tính trước khi cập nhật. Thay $A_{t+1}$ bằng hành động tham lam thì mục tiêu thành mục tiêu Q-learning (mục 13).

Sau mỗi cập nhật $w$, chính sách $\varepsilon$-tham lam suy ra từ $\hat q$ có thể đổi. Vì vậy Sarsa với xấp xỉ hàm không còn là dự đoán dưới một chính sách cố định; bảo đảm của TD tuyến tính ở mục 10.4 và các bảo đảm dạng bảng của Bài 06 (GLIE, Robbins–Monro) không chuyển trực tiếp sang trường hợp này. Bài không phát biểu kết quả hội tụ tổng quát cho Sarsa với xấp xỉ hàm (nguồn tr. 39); các kết quả hữu hạn mẫu cho Sarsa tuyến tính (nguồn tr. 45) cần giả thiết riêng.

### 12.4. Một cập nhật Sarsa trên chuỗi

Trên chuỗi năm trạng thái của mục 12.2, cho $\gamma=1$, $w_0=(1;1;-1)^\top$, $\alpha=0{,}2$ và mẫu đầu tiên ($t=0$): $(S_0,A_0,R_1,S_1,A_1)=(D,0,-1,C,0)$; bộ năm này cho tên Sarsa. Đặc trưng là $x(D,0)=(3;1;1)^\top$ và $x(C,0)=(2;1;1)^\top$. Cả hai dự đoán dùng $w_0$, tính trước khi cập nhật:

$$\hat q(D,0,w_0)=3+1-1=3,\qquad \hat q(C,0,w_0)=2+1-1=2,\qquad \delta_0=-1+1\cdot2-3=-2,$$

$$w_1=w_0+0{,}2\cdot(-2)\cdot(3;1;1)^\top=(1;1;-1)^\top-(1{,}2;0{,}4;0{,}4)^\top=(-0{,}2;0{,}6;-1{,}4)^\top.$$

Mục tiêu $-1+2=1$ nhỏ hơn dự đoán $3$, nên dự đoán tại $(D,0)$ giảm: $\hat q(D,0,w_1)=-0{,}6+0{,}6-1{,}4=-1{,}4$. Vì $\alpha\|x(D,0)\|^2=0{,}2\cdot11=2{,}2>1$, bước cập nhật vượt qua mục tiêu (so với mục 7.2, nơi $\alpha\|x(S_t)\|^2=0{,}5<1$). Nhờ $w$ dùng chung, dự đoán tại cặp khác cũng đổi: $\hat q(C,0,w_1)=-0{,}4+0{,}6-1{,}4=-1{,}2$. Trong Bài tập 8, $\varepsilon=0{,}25$ mô tả chính sách đã sinh các hành động, nhưng không tham gia số học vì hành động kế tiếp đã cho trong mẫu. Mục 16 tính đủ ba cập nhật của Bài tập 8.

### 12.5. Thuật toán Sarsa với hàm xấp xỉ

Đầu vào: đặc trưng $x(s,a)$, $\varepsilon$, quy tắc phá hòa, hệ số chiết khấu $\gamma$, trọng số khởi tạo $w_0$, bước học $\alpha_n$, số lượt $K$. Đầu ra: $w$ và chính sách $\varepsilon$-tham lam theo $\hat q$.

1. Đặt $w\leftarrow w_0$, $n\leftarrow1$. Lặp $K$ lượt: lấy trạng thái đầu $S$, chọn $A$ theo $\varepsilon$-tham lam của $\hat q(S,\cdot,w)$.
2. Thực hiện $A$, nhận $R$, $S'$. Nếu $S'$ kết thúc: $y\leftarrow R$; ngược lại chọn $A'$ theo $\varepsilon$-tham lam của $\hat q(S',\cdot,w)$, $y\leftarrow R+\gamma\hat q(S',A',w)$.
3. $w\leftarrow w+\alpha_n\big[y-\hat q(S,A,w)\big]x(S,A)$; $n\leftarrow n+1$.
4. Nếu $S'$ chưa kết thúc: $S\leftarrow S'$, $A\leftarrow A'$, quay lại bước 2.

$A'$ được chọn bằng $w$ trước cập nhật của chuyển tiếp đó, như trong ví dụ ở mục 12.4; lần chọn tiếp theo dùng $w$ mới. Với $\hat q$ tuyến tính, gradient là $x(S,A)$. Cập nhật là bán gradient như TD(0): mục tiêu chứa $\hat q(S',A',w)$ nhưng được giữ cố định khi lấy đạo hàm.

Bảo đảm của TD tuyến tính (mục 10.4) cần chính sách cố định; ở Sarsa chính sách đổi theo $w$, nên kết quả hội tụ cần giả thiết riêng (nguồn tr. 39). Các phân tích như của Zou, Xu và Liang trong danh mục tài liệu của nguồn (tr. 45) đặt giả thiết về thăm dò, bước học và cách chính sách phụ thuộc $w$. Thay $A'$ trong mục tiêu bằng hành động cực đại thì được Q-learning, học khác chính sách (mục 13).

::: exercise Câu hỏi kiểm tra
Vì sao trong Sarsa tuyến tính, mục tiêu dùng $\gamma x(S_{t+1}, A_{t+1})^\top w_t$ với hành động $A_{t+1}$ thực tế, còn Q-learning dùng $\max_a$?
:::

::: hint
Sarsa là thuật toán học theo chính sách: hành động kế tiếp được lấy từ chính sách đang chạy.
:::

::: solution
Sarsa đánh giá chính sách đang chạy, nên mục tiêu phải là giá trị của cặp $(S_{t+1}, A_{t+1})$ mà chính sách đó thực sự chọn tiếp; do đó cần $A_{t+1}$ được lấy mẫu. Q-learning nhắm tới $q_*$ bất kể chính sách hành vi, nên mục tiêu thay hành động kế bằng giá trị tốt nhất $\max_a \hat q(S_{t+1}, a, w_t)$. Q-learning vì thế là thuật toán khác chính sách; khi kết hợp mục tiêu bootstrap với xấp xỉ hàm, nó có đủ ba thành phần của bộ ba bất ổn (mục 13).
:::

<!-- note-topic-id: lec-07-topic-11 -->
## 13. Q-learning và bộ ba bất ổn

### 13.1. Mục tiêu Q-learning với hàm xấp xỉ

Thay $A_{t+1}$ trong mục tiêu Sarsa bằng hành động cực đại, như Q-learning dạng bảng ở Bài 06 (nguồn tr. 38):

$$y_t=\begin{cases}R_{t+1}, & S_{t+1}\ \text{kết thúc},\\ R_{t+1}+\gamma\max_{a'}\hat q(S_{t+1},a',w_t), & \text{ngược lại},\end{cases}\qquad w_{t+1}=w_t+\alpha\big(y_t-\hat q(S_t,A_t,w_t)\big)x(S_t,A_t).$$

Ở trạng thái kết thúc không lấy cực đại, vì không còn hành động. Dữ liệu do chính sách hành vi $\varepsilon$-tham lam sinh, còn mục tiêu theo chính sách tham lam, nên Q-learning học khác chính sách (điểm đối chiếu thứ hai ở mục 1.1).

Ví dụ: với mẫu $(D,0,-1,C,0)$ và $w_0=(1;1;-1)^\top$ của mục 12.4, $x(C,1)=(2;-1;1)^\top$ cho $\hat q(C,1,w_0)=2-1-1=0$, còn $\hat q(C,0,w_0)=2$. Mục tiêu Q-learning là $-1+\max(2,0)=1$, trùng mục tiêu Sarsa $-1+2=1$, vì hành động 0 vừa được chọn vừa đạt cực đại. Nếu hành động kế tiếp trong mẫu là hành động thăm dò không tham lam, hai mục tiêu khác nhau. Mục này chỉ phân biệt hai quy tắc mục tiêu; nó không khẳng định Q-learning tuyến tính hội tụ tới $q_*$ (nguồn tr. 41).

### 13.2. Bộ ba bất ổn (deadly triad)

Q-learning tuyến tính có đủ ba yếu tố: mục tiêu $R_{t+1}+\gamma\max_{a'}x(S_{t+1},a')^\top w_t$ chứa $w_t$ (bootstrap), dữ liệu đến từ chính sách hành vi khác chính sách tham lam (học khác chính sách), và giá trị được biểu diễn bằng hàm tham số (xấp xỉ hàm). Theo nguồn (tr. 41), khi ba yếu tố

$$\text{bootstrap} + \text{khác chính sách} + \text{xấp xỉ hàm}$$

cùng có mặt, TD và Q-learning có thể phân kỳ; vì vậy bảo đảm hội tụ cho Q-learning tuyến tính cần điều kiện riêng, chặt hơn TD theo chính sách. Đây là nhận định về khả năng phân kỳ trong một lớp thiết lập. Muốn kết luận một thuật toán cụ thể phân kỳ hay hội tụ cần ví dụ phản chứng hoặc định lý riêng; một ví dụ phân kỳ kinh điển là ví dụ của Baird (đọc thêm Sutton và Barto, ấn bản 2, §11.2–11.3).

Bỏ một yếu tố thì nguồn bất ổn này không còn: TD tuyến tính theo chính sách (mục 10.4) và Q-learning dạng bảng (Bài 06) hội tụ, mỗi trường hợp dưới giả thiết riêng; Monte Carlo không bootstrap, khi khác chính sách dùng lấy mẫu quan trọng nhưng phương sai có thể lớn (nguồn tr. 37, hàng cuối bảng so sánh).

Hướng khắc phục (nguồn tr. 41): đổi trọng số cập nhật để ổn định học khác chính sách; mạng mục tiêu (target network), điều chuẩn (regularization) và cắt ngưỡng (truncation/clipping), đặc biệt quan trọng trong học tăng cường sâu. Bài 08 xét mạng mục tiêu. Nguồn (tr. 43) cũng ghi nhận rằng vấn đề này chưa được giải quyết triệt để: nhiều cách ổn định hóa cần giả thiết mạnh hoặc dẫn tới nghiệm chệch.

::: exercise Câu hỏi kiểm tra (bài tập 3)
Trình bày bộ ba bất ổn và giải thích vì sao từng thành phần riêng lẻ không gây vấn đề tương tự.
:::

::: hint
Xét từng cặp: bootstrap cùng xấp xỉ hàm theo chính sách; bootstrap cùng khác chính sách dạng bảng; khác chính sách cùng xấp xỉ hàm không bootstrap.
:::

::: solution
Bộ ba bất ổn là sự kết hợp của bootstrap, dữ liệu khác chính sách và xấp xỉ hàm; khi cả ba cùng có mặt, TD hoặc Q-learning có thể phân kỳ. Trong các trường hợp đối chiếu: Q-learning dạng bảng vẫn hội tụ dù học khác chính sách; TD tuyến tính theo chính sách với chính sách cố định hội tụ tới điểm cố định Bellman chiếu dưới các giả thiết của mục 10.4; Monte Carlo khác chính sách không bootstrap có thể dùng lấy mẫu quan trọng. Khi cả ba yếu tố xuất hiện, hướng cập nhật trung bình không còn được bảo đảm kéo $w$ về một điểm cố định, và sai số xấp xỉ lan truyền qua mục tiêu bootstrap. Đây là khả năng phân kỳ trong một lớp thiết lập; mỗi thuật toán cần phân tích riêng.
:::

### 13.3. Kiểm tra bộ ba bất ổn

Ba yếu tố của mục 13.2 được nhận diện trong một quy tắc cập nhật bằng ba câu kiểm tra:

| Câu kiểm tra | Câu hỏi | Trả lời có nghĩa là |
|---|---|---|
| Biểu diễn | Một cập nhật có đổi nhiều dự đoán qua tham số chung không? | xấp xỉ hàm |
| Mục tiêu | Mục tiêu có chứa dự đoán đang học không? | bootstrap |
| Phân phối | Chính sách sinh dữ liệu có khác chính sách đích không? | học khác chính sách |

Áp dụng cho hai quy tắc điều khiển tuyến tính đã học:

| Quy tắc | Biểu diễn | Mục tiêu | Phân phối | Kết luận |
|---|---|---|---|---|
| Q-learning tuyến tính | có | có | có | đủ ba: cần phân tích ổn định riêng |
| Sarsa tuyến tính | có | có | không | chưa đủ ba; nhưng chính sách đổi theo $w$, nên vẫn cần giả thiết riêng |

Q-learning tuyến tính dùng chung $w$ trong $\hat q(s,a,w)=x(s,a)^\top w$; mục tiêu $R_{t+1}+\gamma\max_{a'}x(S_{t+1},a')^\top w_t$ chứa $w_t$; dữ liệu sinh từ chính sách ε-tham lam, còn mục tiêu ứng với chính sách tham lam. Đủ ba yếu tố nghĩa là thuật toán thuộc lớp có thể phân kỳ và cần phân tích ổn định riêng; điều này không có nghĩa mỗi lần chạy chắc chắn phân kỳ.

Sarsa tuyến tính có hai câu đầu trả lời có. Hành động $A_{t+1}$ trong mục tiêu $R_{t+1}+\gamma\,x(S_{t+1},A_{t+1})^\top w_t$ được chọn bởi chính sách ε-tham lam đang sinh dữ liệu, nên Sarsa học theo chính sách và chưa đủ ba yếu tố. Tuy vậy chính sách ε-tham lam đổi theo $w$, nên kết quả hội tụ của TD dự đoán với chính sách cố định (mục 10.4) không áp dụng trực tiếp.

Ba câu kiểm tra chỉ dùng để phân loại; cách khắc phục là các hướng ở mục 13.2. Giảm bước học có thể đổi hành vi số của một lần chạy nhưng không tự tạo một định lý hội tụ. Phần tiếp theo nêu phạm vi của các kết quả lý thuyết trong bài. Nguồn: tr. 41–43; Bài tập tuần 7, Bài 3.

<!-- note-topic-id: lec-07-topic-14 -->
## 14. Phạm vi lý thuyết

### 14.1. Phạm vi các kết quả hội tụ

Các mục trước dùng hai kết quả hội tụ, mỗi kết quả gắn với một thiết lập. Bảng sau ghi lại thiết lập của từng kết quả và chỉ ra những trường hợp chúng không phủ tới.

| Thiết lập | Kết quả trong bài |
|---|---|
| Monte Carlo tuyến tính, $\pi$ và $\mu$ cố định | SGD trên mục tiêu bình phương lồi; hội tụ tới điểm cực tiểu $J_\mu$ dưới điều kiện lấy mẫu và Robbins–Monro (mục 8.1) |
| TD tuyến tính theo chính sách, chuỗi ergodic với phân phối dừng $d_\pi$ | hội tụ tới điểm cố định Bellman chiếu, dưới các điều kiện của Tsitsiklis và Van Roy (mục 10.4) |
| Điều khiển (Sarsa) hoặc khác chính sách (Q-learning) với xấp xỉ hàm | không suy ra từ hai kết quả trên; cần giả thiết riêng (mục 12, 13) |
| Xấp xỉ phi tuyến, mạng nơ-ron | cần phân tích riêng cho thuật toán và kiến trúc |

Hai dòng đầu khác nhau ở phân phối: $\mu$ là phân phối trọng số trong mục tiêu $J_\mu$, còn $d_\pi$ là phân phối dừng của chuỗi trạng thái khi đi theo $\pi$. Với $\mu=d_\pi$, hai điểm hội tụ nói chung vẫn khác nhau: Monte Carlo cho $\Pi_D v_\pi$, TD cho điểm cố định của $\Pi_D T_\pi$ (mục 11).

Ở dòng thứ ba, giả thiết chính sách cố định không còn: trong Sarsa, chính sách đổi theo $w$; trong Q-learning, dữ liệu đến từ chính sách khác chính sách đích. Bộ ba bất ổn (mục 13.2) chỉ ra trường hợp có thể phân kỳ. Dòng cuối ứng với học tăng cường sâu ở Bài 08.

Nguồn (tr. 43) liệt kê các vấn đề mở, trong đó: chưa có lý thuyết tổng quát cho xấp xỉ sâu như DQN hay actor-critic sâu; bộ ba bất ổn chưa được giải quyết triệt để. TD tìm điểm cố định Bellman chiếu; mục tiêu này không trực tiếp đo chất lượng điều khiển (nguồn tr. 43). Nguồn của mục: tr. 34, 41–44.

### 14.2. Đọc thêm: kết quả cho MDP tuyến tính

Nguồn (tr. 42) nêu kết quả của Jin và cộng sự (2020; danh mục nguồn tr. 45): trong MDP tuyến tính theo lượt với chiều đặc trưng $d$ và chân trời $H$, một biến thể lạc quan của lặp giá trị bình phương tối thiểu (least-squares value iteration, LSVI) đạt độ hối tiếc $\tilde O(\sqrt{d^3 H^3 T})$, không phụ thuộc trực tiếp vào số trạng thái hay số hành động. Kết quả này dựa trên giả thiết cấu trúc của MDP tuyến tính, nằm ngoài bốn thiết lập ở mục 14.1 và không áp dụng cho các thuật toán trong bảng.

Nguồn chỉ nêu bậc độ hối tiếc, không nêu định nghĩa chính xác của MDP tuyến tính, cách xây dựng khoảng tin cậy hay các hằng số. Vì vậy mục này chỉ ghi nhận hướng nghiên cứu.

::: exercise Câu hỏi kiểm tra
Xác định các đại lượng mà độ hối tiếc $\tilde O(\sqrt{d^3 H^3 T})$ phụ thuộc và không phụ thuộc trực tiếp; nêu ý nghĩa đối với vai trò của đặc trưng.
:::

::: hint
So sánh các đại lượng $d$, $H$, $T$ trong biểu thức với số trạng thái và số hành động.
:::

::: solution
Độ hối tiếc phụ thuộc chiều đặc trưng $d$, chân trời $H$ và số bước tương tác $T$, và không phụ thuộc trực tiếp vào $|\mathcal S|$ hay $|\mathcal A|$. Dưới giả thiết MDP tuyến tính, độ khó được đo bằng chiều đặc trưng thay cho kích thước không gian trạng thái–hành động.
:::

<!-- note-topic-id: lec-07-topic-12 -->
## 15. Kiểm tra tổng hợp và tổng kết

### 15.1. Kiểm tra phân tích một quy tắc cập nhật

Năm bước sau dùng để phân tích một quy tắc cập nhật mới trước khi nêu kết luận về nó:

1. Đặc trưng xác định trên trạng thái hay cặp trạng thái–hành động; kích thước của $x$ và $w$.
2. Mục tiêu có chứa $w$ không: gradient đầy đủ hay bán gradient.
3. Viết cập nhật; nêu đại lượng giữ cố định khi lấy đạo hàm.
4. Chính sách sinh dữ liệu và chính sách được đánh giá: theo hay khác chính sách; cố định hay đổi theo $w$.
5. Chỉ nêu hội tụ khi giả thiết lấy mẫu, hạng và bước học khớp một dòng của bảng phạm vi (mục 14.1).

Bước 2 ứng với điểm đối chiếu thứ nhất ở mục 1.1 (lợi tức đầy đủ hay bootstrap). Bước 4 ứng với điểm thứ hai (theo hay khác chính sách) và điểm thứ ba (cách cải thiện chính sách): trong dự đoán, chính sách cố định; trong điều khiển, chính sách được cải thiện theo $\hat q$ nên đổi theo $w$.

::: exercise Câu hỏi kiểm tra
Áp dụng năm bước cho TD(0) tuyến tính với chính sách $\pi$ cố định.
:::

::: hint
Đi lần lượt năm bước; ở bước 5, tìm dòng của bảng mục 14.1 có cùng thiết lập.
:::

::: solution
(1) $x(s)\in\mathbb R^d$, $w\in\mathbb R^d$. (2) Mục tiêu $R_{t+1}+\gamma x(S_{t+1})^\top w_t$ chứa $w_t$, nên cập nhật là bán gradient. (3) $w_{t+1}=w_t+\alpha_t\big(R_{t+1}+\gamma x(S_{t+1})^\top w_t-x(S_t)^\top w_t\big)x(S_t)$; mục tiêu được giữ cố định, chỉ lấy đạo hàm qua $\hat v(S_t,w)$. (4) Dữ liệu sinh theo $\pi$ và chính sách được đánh giá cũng là $\pi$, cố định: theo chính sách. (5) Khớp dòng TD của bảng ở mục 14.1: với chuỗi ergodic, $d_\pi(s)>0$, $\gamma<1$, đặc trưng bị chặn, $\Phi$ đủ hạng cột và bước học Robbins–Monro (mục 10.4), $w_t$ hội tụ với xác suất 1 tới $w_{\mathrm{TD}}$, nghiệm duy nhất của $Aw=b$, thỏa $\Phi w_{\mathrm{TD}}=\Pi_D T_\pi(\Phi w_{\mathrm{TD}})$.
:::

Nếu một bước không khớp, chẳng hạn chính sách đổi theo $w$ như trong Sarsa (mục 12), chưa đủ cơ sở để nêu kết luận hội tụ từ bảng phạm vi. Nguồn: tổng hợp tr. 22–43; Bài tập tuần 7.

### 15.2. Tổng kết và hướng tới Bài 08

Bài mở đầu bằng hai giới hạn của bảng tra (mục 2.1): không lưu được một ô cho mỗi trạng thái khi không gian lớn hoặc liên tục, và không tổng quát hóa giữa các trạng thái gần nhau. Tham số dùng chung $w$ giải quyết cả hai; đổi lại, một cập nhật đổi nhiều dự đoán, nên lập luận hội tụ theo từng ô của Bài 06 không còn dùng được và mỗi phương pháp cần kết quả riêng. Chất lượng xấp xỉ phụ thuộc đặc trưng: hai trạng thái cùng vector đặc trưng nhận cùng dự đoán, và sai số xấp xỉ không giảm khi thêm dữ liệu (mục 5.3). Khó khăn thứ ba ở mục 2.1, dữ liệu không độc lập cùng phân phối, nằm trong giả thiết lấy mẫu: Monte Carlo theo lượt cần kết quả cho dữ liệu từ chuỗi Markov trộn (mục 8.1), TD cần chuỗi ergodic (mục 10.4). Mỗi kết luận dưới đây đi kèm giả thiết của nó.

| Phương pháp | Kết luận trong bài | Giả thiết |
|---|---|---|
| Monte Carlo | gradient đầy đủ (mục tiêu $G_t$ không chứa $w$), gần hồi quy; hội tụ tới cực tiểu $J_\mu$ | $\pi$, $\mu$ cố định; điều kiện lấy mẫu; bước học Robbins–Monro (mục 8.1) |
| TD(0) | bán gradient; theo chính sách, hội tụ tới điểm cố định Bellman chiếu | chính sách cố định, chuỗi ergodic, $\gamma<1$, $\Phi$ đủ hạng cột, bước học Robbins–Monro (mục 10.4) |
| Sarsa | chính sách đổi theo $w$ | bài không nêu kết quả hội tụ chung; cần giả thiết riêng (mục 12) |
| Q-learning | thêm học khác chính sách: đủ ba yếu tố của bộ ba bất ổn | bài không nêu kết quả hội tụ chung; cần giả thiết riêng (mục 13) |

Theo nguồn (tr. 44), Monte Carlo dễ phân tích về mặt thống kê và gần hồi quy; mục tiêu của nó thường có phương sai cao và phải chờ hết lượt. TD cập nhật sau từng bước, hiệu quả tính toán hơn, mục tiêu thường có phương sai thấp hơn; TD tuyến tính theo chính sách có kết quả hội tụ cổ điển. Trong điều khiển, kết quả mạnh nhất cần giả thiết cấu trúc, như MDP tuyến tính ở mục 14.2.

Ngoài ba vấn đề mở đã nêu ở mục 14.1, nguồn (tr. 43) còn ghi nhận: phần lớn định lý giả sử đặc trưng đã phù hợp, chưa xét quá trình học biểu diễn; bảo đảm cho thăm dò với xấp xỉ hàm tổng quát còn chủ yếu ở lớp tuyến tính hoặc lớp có cấu trúc đặc biệt; trong học tăng cường ngoại tuyến, phân phối hành vi có thể không phủ đủ các cặp trạng thái–hành động cần đánh giá.

Bài 08 thay tích vô hướng $x(s,a)^\top w$ bằng mạng nơ-ron (Deep Q-Network); bảo đảm tuyến tính không tự chuyển sang. Nguồn (tr. 26) ghi nhận mạng nơ-ron mạnh về biểu diễn nhưng tối ưu khó hơn và ít bảo đảm tổng quát. Các kết quả hội tụ của bài này thuộc mô hình tuyến tính với giả thiết đã nêu; mạng mục tiêu và bộ nhớ phát lại là cơ chế thuật toán của Bài 08, với phạm vi thực nghiệm và lý thuyết riêng.

Bài 1–3 và 5–6 của phiếu bài tập tuần 7 dùng để tự ôn: Bài 1 về giới hạn của bảng tra (mục 2.1), Bài 2 về so sánh Monte Carlo và TD(0) (mục 11.1), Bài 3 về bộ ba bất ổn (mục 13.2), Bài 5 về dạng $b-Aw$ và điểm cố định Bellman chiếu (mục 10.2–10.3), Bài 6 về vai trò hai điều kiện Robbins–Monro (mục 8.2). Nguồn: tr. 26, 41–45; Bài tập tuần 7.

::: exercise Câu hỏi kiểm tra
Xếp bốn trường hợp Monte Carlo, TD(0), Sarsa và Q-learning với xấp xỉ tuyến tính theo mức độ khó của phân tích hội tụ; nêu yếu tố làm mỗi trường hợp khó hơn trường hợp trước.
:::

::: hint
Phân biệt mục tiêu không chứa $w$ với mục tiêu bootstrap, theo chính sách với khác chính sách, và dự đoán với điều khiển.
:::

::: solution
Monte Carlo gần hồi quy nhất vì mục tiêu $G_t$ không phụ thuộc $w$. TD(0) khó hơn vì mục tiêu bootstrap chứa $w$; với chính sách cố định và các giả thiết của mục 10.4, TD tuyến tính theo chính sách hội tụ tới điểm cố định Bellman chiếu. Sarsa khó hơn nữa vì vừa bootstrap vừa cải thiện chính sách trong quá trình học, nên chính sách đổi theo $w$. Q-learning tuyến tính học khác chính sách và có đủ ba yếu tố của bộ ba bất ổn, nên không suy ra được bảo đảm hội tụ từ kết quả của TD dự đoán. Thứ tự này đo độ khó của phân tích hội tụ, không xếp hạng hiệu quả thực nghiệm.
:::

<!-- note-topic-id: lec-07-topic-16 -->
## 16. Thực hành: chuỗi năm trạng thái

Hai bài tập 7 và 8 của phiếu bài tập tuần 7 dùng chuỗi năm trạng thái và đặc trưng của mục 12.2 (nguồn tr. 40): $A$ và $E$ kết thúc, $D$ là trạng thái đầu, hành động $0$ đi trái và $1$ đi phải, chuyển tất định, lượt tối đa ba bước, $\gamma=1$; thưởng vào $A$ bằng $1000$, vào $E$ bằng $10$, các chuyển khác bằng $-1$. Xấp xỉ tuyến tính

$$\hat q(s,a,w)=x(s,a)^\top w,\qquad x(s,a)=\big(d_{\text{trái}}(s);\,u(a);\,1\big)^\top,$$

với $d_{\text{trái}}(B)=1$, $d_{\text{trái}}(C)=2$, $d_{\text{trái}}(D)=3$, $u(0)=1$, $u(1)=-1$; $[w]_i$ là thành phần thứ $i$ của $w$.

### 16.1. Bài tập: Monte Carlo trên một lượt

::: exercise Bài tập 7
Cho $w_0=(1;1;-1)^\top$, $\alpha=0{,}1$ và một lượt duy nhất

$$(D,0,-1,C),\quad (C,0,-1,B),\quad (B,0,1000,A).$$

1. Tính các lợi tức $G_0$, $G_1$, $G_2$.
2. Viết các vector đặc trưng $x(D,0)$, $x(C,0)$, $x(B,0)$.
3. Cập nhật trọng số theo đúng thứ tự thời gian trong lượt bằng cập nhật Monte Carlo $w_{t+1}=w_t+\alpha\big(G_t-x(S_t,A_t)^\top w_t\big)x(S_t,A_t)$.
4. Tính $\hat q(D,0,w_3)$, $\hat q(C,0,w_3)$, $\hat q(B,0,w_3)$.
:::

::: hint
Với $\gamma=1$, $G_t$ là tổng phần thưởng từ $t+1$ đến hết lượt. Mỗi lần cập nhật dùng $w$ vừa có từ lần trước.
:::

::: solution
(1) $G_2=1000$, $G_1=-1+1000=999$, $G_0=-1-1+1000=998$.

(2) $x(D,0)=(3;1;1)^\top$, $x(C,0)=(2;1;1)^\top$, $x(B,0)=(1;1;1)^\top$.

(3) Lần 1, $(D,0)$: $\hat q(D,0,w_0)=3\cdot1+1\cdot1+1\cdot(-1)=3$; sai số $998-3=995$; bước $\alpha\cdot995=99{,}5$;

$$w_1=(1;1;-1)^\top+99{,}5\,(3;1;1)^\top=(299{,}5;\,100{,}5;\,98{,}5)^\top.$$

Lần 2, $(C,0)$: $\hat q(C,0,w_1)=2\cdot299{,}5+100{,}5+98{,}5=798$; sai số $999-798=201$; bước $20{,}1$;

$$w_2=w_1+20{,}1\,(2;1;1)^\top=(339{,}7;\,120{,}6;\,118{,}6)^\top.$$

Lần 3, $(B,0)$: $\hat q(B,0,w_2)=339{,}7+120{,}6+118{,}6=578{,}9$; sai số $1000-578{,}9=421{,}1$; bước $42{,}11$;

$$w_3=w_2+42{,}11\,(1;1;1)^\top=(381{,}81;\,162{,}71;\,160{,}71)^\top.$$

(4) $\hat q(D,0,w_3)=3\cdot381{,}81+162{,}71+160{,}71=1468{,}85$; $\hat q(C,0,w_3)=2\cdot381{,}81+323{,}42=1087{,}04$; $\hat q(B,0,w_3)=381{,}81+323{,}42=705{,}23$.
:::

Phép tính chỉ đánh giá giá trị hành động trên một lượt, chưa có bước cải thiện chính sách. Giá trị cuối tại $D$ vượt $G_0=998$ vì hai lý do. Thứ nhất, $\|x(D,0)\|^2=11$, nên $\alpha\|x(D,0)\|^2=1{,}1>1$: ngay lần 1, $\hat q(D,0,w_1)=3+1{,}1\cdot995=1097{,}5$ đã vượt mục tiêu, giống ví dụ Sarsa ở mục 12.4 ($\alpha\|x\|^2=2{,}2$) và khác ví dụ ở mục 7.2 ($\alpha\|x\|^2=0{,}5$). Thứ hai, hai lần cập nhật sau tại $C$ và $B$ tiếp tục kéo $\hat q(D,0)$ lên qua tham số dùng chung. Phiếu bài tập ghi "semi-gradient"; mục tiêu Monte Carlo $G_t$ không chứa $w$, nên cập nhật này là gradient đầy đủ (mục 6).

### 16.2. Bài tập: Sarsa trên ba mẫu

Cho $w_0 = [1, 1, -1]^\top$, $\alpha = 0.2$, $\varepsilon = 0.25$, và ba mẫu liên tiếp. Giá trị $\varepsilon$ mô tả chính sách hành vi đã sinh mẫu; ba mẫu đã cho sẵn nên $\varepsilon$ không đi vào phép cập nhật dưới đây.

$$(D, 0, -1, C, 0), \qquad (C, 1, -1, D, 1), \qquad (D, 1, +10, E, \text{terminal}).$$

Cập nhật $w_{t+1} = w_t + \alpha \delta_t x(S_t, A_t)$ với $\delta_t = R_{t+1} + \gamma \hat q(S_{t+1}, A_{t+1}, w_t) - \hat q(S_t, A_t, w_t)$, $\gamma = 1$, và $\hat q(E, \cdot, w) = 0$.

Các vector đặc trưng cần dùng: $x(D,0) = [3, +1, 1]^\top$, $x(C,0) = [2, +1, 1]^\top$, $x(C,1) = [2, -1, 1]^\top$, $x(D,1) = [3, -1, 1]^\top$.

Mẫu 1: $(D, 0, -1, C, 0)$.

$$\hat q(D,0,w_0) = 3(1) + 1(1) + 1(-1) = 3, \qquad \hat q(C,0,w_0) = 2(1) + 1(1) + 1(-1) = 2.$$

$$\delta_0 = -1 + 1 \cdot \hat q(C,0,w_0) - \hat q(D,0,w_0) = -1 + 2 - 3 = -2.$$

$$w_1 = w_0 + 0.2 \cdot (-2) \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} - \begin{bmatrix} 1.2 \\ 0.4 \\ 0.4 \end{bmatrix} = \begin{bmatrix} -0.2 \\ 0.6 \\ -1.4 \end{bmatrix}.$$

Mẫu 2: $(C, 1, -1, D, 1)$.

$$\hat q(C,1,w_1) = 2(-0.2) - 0.6 - 1.4 = -2.4, \qquad \hat q(D,1,w_1) = 3(-0.2) - 0.6 - 1.4 = -2.6.$$

$$\delta_1 = -1 + \hat q(D,1,w_1) - \hat q(C,1,w_1) = -1 - 2.6 + 2.4 = -1.2.$$

$$w_2 = w_1 + 0.2 \cdot (-1.2) \begin{bmatrix} 2 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.2 \\ 0.6 \\ -1.4 \end{bmatrix} + \begin{bmatrix} -0.48 \\ 0.24 \\ -0.24 \end{bmatrix} = \begin{bmatrix} -0.68 \\ 0.84 \\ -1.64 \end{bmatrix}.$$

Mẫu 3: $(D, 1, +10, E, \text{terminal})$, với $\hat q(E,\cdot,w_2) = 0$.

$$\hat q(D,1,w_2) = 3(-0.68) - 0.84 - 1.64 = -4.52.$$

$$\delta_2 = +10 + 0 - (-4.52) = 14.52.$$

$$w_3 = w_2 + 0.2 \cdot 14.52 \begin{bmatrix} 3 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.68 \\ 0.84 \\ -1.64 \end{bmatrix} + 2.904 \begin{bmatrix} 3 \\ -1 \\ 1 \end{bmatrix} = \begin{bmatrix} 8.032 \\ -2.064 \\ 1.264 \end{bmatrix}.$$

Trọng số cuối cùng $w_3 = [8.032, -2.064, 1.264]^\top$. Giá trị xấp xỉ mới:

$$\hat q(D,0,w_3) = 3(8.032) - 2.064 + 1.264 = 23.296,$$
$$\hat q(C,1,w_3) = 2(8.032) + 2.064 + 1.264 = 19.392,$$
$$\hat q(D,1,w_3) = 3(8.032) + 2.064 + 1.264 = 27.424.$$

Nhận xét: mẫu 3 với phần thưởng $+10$ vào trạng thái kết thúc $E$ tạo bước cập nhật lớn $\delta_2 = 14.52$; sau ba mẫu, $\hat q(D,1)$ vượt $\hat q(D,0)$.

::: exercise Câu hỏi kiểm tra
Trong bài 8, vì sao $\delta_1=-1.2$? Kiểm tra lại rằng $\hat q(D,1,w_3)-\hat q(D,0,w_3)=-2[w_3]_2$.
:::

::: hint
Tính $\delta_1$ từ công thức; với phần kiểm tra, tính $\hat q(D,1,w_3) - \hat q(D,0,w_3)$ theo thành phần thứ hai của $w_3$.
:::

::: solution
$\delta_1=-1-2.6+2.4=-1.2$. Phần kiểm tra: $\hat q(D,1,w_3)-\hat q(D,0,w_3)=27.424-23.296=4.128$; hai vector đặc trưng chỉ khác thành phần $u(a)$, nên chênh lệch bằng $[w_3]_2(-1-1)=-2[w_3]_2=-2(-2.064)=4.128$.
:::

### 16.3. Khung mục tiêu cập nhật

Các quy tắc trong bài có chung dạng: tham số được cộng thêm bước học nhân sai số giữa mục tiêu $y_t$ và dự đoán, nhân vector đặc trưng. Dự đoán dùng $\hat v(S_t,w_t)=x(S_t)^\top w_t$; điều khiển dùng $\hat q(S_t,A_t,w_t)=x(S_t,A_t)^\top w_t$. Các quy tắc khác nhau ở mục tiêu $y_t$ và ở chính sách sinh dữ liệu:

| Quy tắc | Mục tiêu $y_t$ | Chứa $w_t$ |
|---|---|---|
| Monte Carlo (dự đoán hoặc điều khiển) | $G_t$ | không: gradient đầy đủ |
| TD(0) dự đoán | $R_{t+1}+\gamma\,x(S_{t+1})^\top w_t$ | có: bán gradient |
| Sarsa | $R_{t+1}+\gamma\,x(S_{t+1},A_{t+1})^\top w_t$, $A_{t+1}$ từ chính sách hành vi | có: bán gradient |
| Q-learning | $R_{t+1}+\gamma\max_{a'}x(S_{t+1},a')^\top w_t$ | có: bán gradient |

::: exercise Câu hỏi kiểm tra
Với cùng một mẫu $(S_t,A_t,R_{t+1},S_{t+1},A_{t+1})$, xác định khi nào mục tiêu Sarsa và mục tiêu Q-learning bằng nhau.
:::

::: hint
So sánh $x(S_{t+1},A_{t+1})^\top w_t$ với $\max_{a'}x(S_{t+1},a')^\top w_t$.
:::

::: solution
Hai mục tiêu bằng nhau khi hành động $A_{t+1}$ do chính sách hành vi chọn cũng đạt cực đại của $\hat q(S_{t+1},\cdot,w_t)$, tức là hành động tham lam tại $S_{t+1}$. Mục tiêu TD(0) dự đoán dùng giá trị trạng thái nên thuộc bài toán khác (dự đoán); mục tiêu Monte Carlo dùng lợi tức đầy đủ và không bootstrap.
:::

## Tài liệu tham khảo

- Tạ Việt Cường. Lecture 07: Hàm xấp xỉ trong Reinforcement Learning. VNU-UET, tháng 4 năm 2026, tr. 1–45.
- Tạ Việt Cường. Bài tập tuần 7 — Function Approximation, ngày 8 tháng 4 năm 2026, bài 1–8.
- David Silver. Lecture 6: Value Function Approximation. UCL RL Course.
- J. Tsitsiklis và B. Van Roy. An Analysis of Temporal-Difference Learning with Function Approximation. IEEE Transactions on Automatic Control, 1997 (danh mục của bài giảng nguồn ghi năm 1996).
- J. Bhandari, D. Russo, R. Singal. A Finite Time Analysis of Temporal Difference Learning With Linear Function Approximation. COLT 2018 / Operations Research 2021.
- C. Jin, Z. Yang, Z. Wang, M. I. Jordan. Provably Efficient Reinforcement Learning with Linear Function Approximation. COLT 2020.
- S. Zou, T. Xu, Y. Liang. Finite-Sample Analysis for SARSA with Linear Function Approximation. NeurIPS 2019.
- S. Zhang, H. Yao, S. Whiteson. Breaking the Deadly Triad with a Target Network. ICML 2021.
- Y. Peng, K. Jin, L. Zhang, Z. Zhang. A Finite Sample Analysis of Distributional TD Learning with Linear Function Approximation. NeurIPS 2025.
