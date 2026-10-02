# Bài 07. Xấp xỉ hàm trong Học tăng cường

Học phần Học tăng cường · Học kỳ 1, năm học 2026–2027.

Khi không gian trạng thái lớn hoặc liên tục, bảng giá trị của Bài 05–06 được thay bằng một hàm có tham số dùng chung. Bài này dùng lớp hàm tuyến tính theo đặc trưng, xây dựng cập nhật Monte Carlo (MC) và sai phân thời gian (TD) cho dự đoán, rồi Sarsa và mục tiêu Q-learning cho điều khiển. Mỗi bảo đảm hội tụ được nêu cùng giả thiết về chính sách, đặc trưng, phân phối dữ liệu và bước học.

## Bản đồ chủ đề

Bản đồ bốn nhóm: nhóm **cốt lõi** gồm 12 chủ đề `lec-07-topic-01` đến `lec-07-topic-12` tạo thành mạch chính; nhóm **cầu nối** gồm `lec-07-topic-13` tóm tắt tiên quyết từ Bài 06; nhóm **bổ sung** gồm `lec-07-topic-14` và `lec-07-topic-15` cho kết quả hiện đại và chứng minh; nhóm **đọc thêm/thực hành** gồm `lec-07-topic-16` với tính tay bài 7–8. Sáu mạch chính: mở/cầu nối 7 phút; động cơ–đặc trưng 23 phút; MC 21 phút; TD–Bellman chiếu 33 phút; điều khiển/SARSA 19 phút; Q-learning–bộ ba bất ổn–thực hành–kết luận 17 phút; tổng 120 phút. Phần chữa bài 30 phút dùng bài 4, 7 và 8. Thứ tự trình bày mỗi chủ đề theo vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng/giới hạn → kiểm tra; các chủ đề 13, 14 và 15 gộp bước trực giác với ví dụ vì chúng chỉ tóm tắt hoặc nêu hướng nghiên cứu, không có ví dụ tính được trong nguồn.

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

### So sánh MC–TD

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: tổng hợp khác biệt về đích, độ chệch, phương sai, cập nhật trực tuyến và lý thuyết.
- Kết nối vào: MC gradient và TD bán gradient.
- Kết nối ra: dẫn tới điều khiển với giá trị hành động.
- Nguồn: tr. 37 và bài tập 2.

### Điều khiển với giá trị hành động và SARSA tuyến tính

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: chuyển từ dự đoán $v$ sang điều khiển $q$.
- Kết nối vào: so sánh MC–TD.
- Kết nối ra: dẫn tới Q-learning và bộ ba bất ổn.
- Nguồn: tr. 38–40 và bài tập 8.

### Đích Q-learning tuyến tính và bộ ba bất ổn

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: nêu đích khác chính sách và nguy cơ bất ổn.
- Kết nối vào: SARSA tuyến tính.
- Kết nối ra: dẫn tới giới hạn lý thuyết và kết luận.
- Nguồn: tr. 38–41 và bài tập 3.

### Phạm vi lý thuyết, giới hạn và kết luận

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: đóng mạch, nêu các vấn đề mở.
- Kết nối vào: kết quả hiện đại và hai bài tính tay đã tổng hợp toàn bài.
- Kết nối ra: định hướng đọc thêm.
- Nguồn: tr. 43–44.

### Mở đầu: từ bảng giá trị đến hàm xấp xỉ

- Nhóm: `cầu nối`.
- Vai trò trong mạch: mở bài, nhắc điều kiện hội tụ dạng bảng, nêu ba điểm đối chiếu các thuật toán, nội dung và mục tiêu học tập.
- Kết nối vào: bảng giá trị, điều kiện GLIE và Robbins–Monro của Bài 05–06.
- Kết nối ra: câu hỏi điều gì thay đổi khi $Q$ là hàm tuyến tính dẫn vào nội dung mới.
- Nguồn: tr. 3, 5–20; chỉ tóm tắt điều kiện, không trình bày lại chứng minh dài.

### Kết quả MDP tuyến tính

- Nhóm: `bổ sung`.
- Vai trò trong mạch: cho thấy lý thuyết hiện đại tiến gần thực tế.
- Kết nối vào: nguy cơ của bộ ba bất ổn trong điều khiển khác chính sách.
- Kết nối ra: dẫn tới danh sách vấn đề mở.
- Nguồn: tr. 42; chỉ nêu hướng nghiên cứu và ký hiệu, không phát biểu định lý đầy đủ vì nguồn thiếu thiết lập chi tiết.

### Hội tụ của Monte Carlo tuyến tính

- Nhóm: `bổ sung`.
- Vai trò trong mạch: điều kiện hội tụ của Monte Carlo tuyến tính, nghiệm là cực tiểu $J_\mu$; phép đạo hàm và vai trò Robbins–Monro (bài tập 4, 6).
- Kết nối vào: gradient và thuật toán Monte Carlo.
- Kết nối ra: Monte Carlo phải chờ hết lượt, dẫn tới TD(0).
- Nguồn: tr. 34; bài tập 4 và 6.

### Khung đích và thực hành điều khiển

- Nhóm: `đọc thêm/thực hành`.
- Vai trò trong mạch: thực hành tổng hợp trước khi kết luận, dùng cho chữa bài 7–8.
- Kết nối vào: SARSA tuyến tính và đích Q-learning.
- Kết nối ra: cung cấp bằng chứng tính toán để kết luận thu hồi mục tiêu bài học.
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

Bài tập 4. Cho $\hat v(s,w) = x(s)^\top w$ (phiếu bài tập viết $\phi(s)$) và mất mát $\ell_t(w) = \frac{1}{2}\big(G_t - x(S_t)^\top w\big)^2$. Đạo hàm theo $w$:

$$\nabla_w \ell_t(w) = \frac{1}{2} \cdot 2\big(G_t - x(S_t)^\top w\big) \cdot (-x(S_t)) = -\big(G_t - x(S_t)^\top w\big)x(S_t).$$

Một bước hạ gradient với bước $\alpha_t$:

$$w_{t+1} = w_t - \alpha_t \nabla_w \ell_t(w_t) = w_t + \alpha_t \big(G_t - x(S_t)^\top w_t\big)x(S_t),$$

đúng công thức yêu cầu. Điều kiện để cập nhật hội tụ về cực tiểu toàn cục là các điều kiện ở mục 8.1: bước học thỏa Robbins–Monro, đặc trưng bị chặn, mômen hữu hạn và giả thiết lấy mẫu phù hợp (iid như nguồn tr. 34, hoặc chuỗi Markov trộn).

Bài tập 6, vai trò của hai điều kiện Robbins–Monro. Điều kiện $\sum_n \alpha_n = \infty$ bảo đảm tổng các bước đủ lớn để thuật toán còn tiếp tục học: nếu tổng hữu hạn, $w$ có thể dừng ở nơi chưa tới nghiệm. Điều kiện $\sum_n \alpha_n^2 < \infty$ giữ tổng phương sai của nhiễu tích lũy $\sum_n \alpha_n^2\,\mathrm{Var}[\text{nhiễu}_n]$ hữu hạn khi phương sai nhiễu bị chặn, nên nhiễu không đẩy $w$ đi xa mãi. Hai điều kiện này dùng cho cả Monte Carlo và TD với xấp xỉ hàm.

::: exercise Câu hỏi kiểm tra
Tính Hessian của $\ell_t(w)$ và suy ra $\ell_t$ lồi; từ đó giải thích vì sao cực tiểu địa phương là cực tiểu toàn cục.
:::

::: hint
Tính đạo hàm bậc hai của $\frac{1}{2}(G_t - x^\top w)^2$ theo $w$.
:::

::: solution
$\nabla_w^2 \ell_t(w) = x(S_t)x(S_t)^\top$, là ma trận bán xác định dương vì $u^\top x(S_t)x(S_t)^\top u = (x(S_t)^\top u)^2 \ge 0$ với mọi $u$. Hàm lồi nên mọi cực tiểu địa phương là cực tiểu toàn cục; do đó hạ gradient với bước học thỏa Robbins–Monro và dữ liệu phù hợp hội tụ về cực tiểu toàn cục của sai số bình phương trên phân phối dữ liệu.
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

Thay $y_t=y_t^{\mathrm{TD}}$ vào dạng cập nhật của mục 6.1, cập nhật tuyến tính là

$$w_{t+1} = w_t + \alpha_t \delta_t x(S_t), \qquad \delta_t = R_{t+1} + \gamma x(S_{t+1})^\top w_t - x(S_t)^\top w_t.$$

Đây là bán gradient: nó là gradient của $\frac{1}{2}\big(y_t^{\mathrm{TD}} - \hat v(S_t,w)\big)^2$ chỉ khi coi đích là hằng số, bỏ qua sự phụ thuộc của $y_t^{\mathrm{TD}}$ vào $w_t$. Vì vậy không thể phân tích nó như hồi quy SGD thông thường; cần công cụ khác — toán tử Bellman chiếu — ở chủ đề tiếp theo.

::: exercise Câu hỏi kiểm tra
Viết gradient đầy đủ của hàm mất mát $\frac{1}{2}\big(y_t^{\mathrm{TD}}(w) - x(S_t)^\top w\big)^2$ với $y_t^{\mathrm{TD}}(w) = R_{t+1} + \gamma x(S_{t+1})^\top w$, rồi chỉ ra số hạng mà cập nhật bán gradient bỏ qua.
:::

::: hint
Đạo hàm theo quy tắc tích: $\nabla (y(w) - x^\top w)^2$ có hai số hạng.
:::

::: solution
Đặt $e(w) = y_t^{\mathrm{TD}}(w) - x(S_t)^\top w = R_{t+1} + \gamma x(S_{t+1})^\top w - x(S_t)^\top w$. Khi đó $\nabla_w e = \gamma x(S_{t+1}) - x(S_t)$ và gradient đầy đủ của $\frac12e(w)^2$ là $e(w)\big(\gamma x(S_{t+1}) - x(S_t)\big)$. Bước hạ gradient vì thế tỉ lệ với $e(w)[x(S_t)-\gamma x(S_{t+1})]$. Cập nhật bán gradient chỉ giữ phần $e(w_t)x(S_t)$, tức bỏ qua số hạng $-\gamma e(w_t)x(S_{t+1})$.
:::

<!-- note-topic-id: lec-07-topic-08 -->
## Điểm cố định Bellman chiếu

Vấn đề: nếu cập nhật TD tuyến tính hội tụ, nó hội tụ về đâu? Vì đích bán gradient không phải gradient thật, nghiệm không phải là nghiệm hồi quy tối thiểu lỗi bình phương thông thường.

Trực giác: TD kỳ vọng hoạt động như một phép lặp trên $w$; điểm dừng là nơi cập nhật kỳ vọng bằng không, tức vector đặc trưng trung bình của sai số TD triệt tiêu.

Hình thức và phát biểu. Xét TD(0) tuyến tính với

$$w_{t+1} = w_t + \alpha_t \delta_t x(S_t), \qquad \delta_t = R_{t+1} + \gamma x(S_{t+1})^\top w_t - x(S_t)^\top w_t.$$

Ký hiệu $\Phi$ là ma trận đặc trưng (hàng thứ $s$ là $x(s)^\top$), $D$ là ma trận chéo của phân phối dừng theo chính sách $d$, $P_\pi$ là ma trận chuyển theo chính sách $\pi$, $r_\pi$ là vector phần thưởng kỳ vọng. Toán tử Bellman theo chính sách là $T^\pi v = r_\pi + \gamma P_\pi v$. Nếu tồn tại điểm cố định $w_{\mathrm{TD}}$ của cập nhật kỳ vọng thì nó thỏa

$$\Phi w_{\mathrm{TD}} = \Pi_D T^\pi (\Phi w_{\mathrm{TD}}),$$

trong đó $\Pi_D$ là phép chiếu trực giao theo chuẩn $D$, tức $\Pi_D v = \Phi(\Phi^\top D \Phi)^{-1}\Phi^\top D\, v$ khi $\Phi^\top D \Phi$ khả nghịch.

Chứng minh (bài tập 5). Lấy kỳ vọng có điều kiện của $\delta_t x(S_t)$ tại điểm cố định. Với phân phối dừng $d$,

$$\mathbb E_\pi[\delta_t x(S_t)] = \mathbb E_\pi\big[(R_{t+1} + \gamma x(S_{t+1})^\top w - x(S_t)^\top w)x(S_t)\big] = b - A w,$$

trong đó $b = \Phi^\top D\, r_\pi$ và $A = \Phi^\top D (I - \gamma P_\pi)\Phi$. Điểm cố định thỏa $b - A w_{\mathrm{TD}} = 0$, tức $\Phi^\top D\, r_\pi = \Phi^\top D (I - \gamma P_\pi) \Phi w_{\mathrm{TD}}$. Nhân hai vế với $(\Phi^\top D \Phi)^{-1}\Phi^\top D$ và dùng $T^\pi(\Phi w) = r_\pi + \gamma P_\pi \Phi w$:

$$\Phi w_{\mathrm{TD}} = \Phi(\Phi^\top D\Phi)^{-1}\Phi^\top D\,\big(r_\pi + \gamma P_\pi \Phi w_{\mathrm{TD}}\big) = \Pi_D T^\pi(\Phi w_{\mathrm{TD}}),$$

điều phải chứng minh. Ý nghĩa: $\hat v = \Phi w_{\mathrm{TD}}$ là hình chiếu trực giao theo chuẩn $D$ của $T^\pi \hat v$ xuống không gian sinh bởi đặc trưng — TD không tìm $v^\pi$ mà tìm điểm gần nhất có thể với hình ảnh Bellman của chính nó.

Giới hạn hội tụ (phát biểu chuẩn, theo chính sách cố định): TD tuyến tính hội tụ tới $w_{\mathrm{TD}}$ khi các giả thiết sau cùng được thỏa — chính sách $\pi$ cố định, dữ liệu theo chính sách, chuỗi Markov phù hợp (chẳng hạn bất khả quy và không tuần hoàn để phân phối dừng duy nhất tồn tại), $\gamma < 1$, ma trận đặc trưng $\Phi$ đủ hạng (để $\Phi^\top D\Phi$ khả nghịch), và bước học thích hợp theo Robbins–Monro. Bảo đảm này không chuyển sang SARSA hay Q-learning với xấp xỉ hàm, vì ở đó chính sách thay đổi hoặc đích khác chính sách.

::: exercise Câu hỏi kiểm tra
Giải thích vì sao phương trình $\Phi w_{\mathrm{TD}} = \Pi_D T^\pi(\Phi w_{\mathrm{TD}})$ cho thấy TD triệt tiêu sai số Bellman chiếu chứ không trực tiếp tối ưu lỗi $\|\hat v - v^\pi\|_D$.
:::

::: hint
So sánh hai đại lượng: $\|\Pi_D T^\pi \hat v - \hat v\|_D$ và $\|v^\pi - \hat v\|_D$.
:::

::: solution
Điểm cố định triệt tiêu sai số Bellman chiếu $\|\Pi_D T^\pi \hat v - \hat v\|_D$, tức khoảng cách giữa $\hat v$ và hình Bellman chiếu của nó. Nếu lớp hàm không chứa $v^\pi$, hình chiếu của $T^\pi \hat v$ nói chung không phải là hình chiếu của $v^\pi$, nên $\hat v$ tại điểm cố định khác với phép chiếu của $v^\pi$. Đây là hiện tượng lệch mục tiêu: TD giải bài toán điểm cố định Bellman chiếu, không trực tiếp tối thiểu hoá khoảng cách tới $v^\pi$.
:::

<!-- note-topic-id: lec-07-topic-09 -->
## So sánh MC–TD

Vấn đề: sau khi có cả hai cập nhật, cần đối chiếu để biết khi nào dùng cái nào.

Trực giác: MC "dễ hiểu về mặt thống kê", TD "mạnh hơn về mặt tính toán". Trong RL hiện đại, TD/bootstrapping thắng về hiệu năng, nhưng lý thuyết khó hơn đáng kể.

Hình thức, bảng so sánh theo tr. 37:

| Tiêu chí | MC | TD |
|---|---|---|
| Đích | $G_t$ | $R_{t+1} + \gamma \hat v(S_{t+1}, w_t)$ |
| Độ chệch | không chệch theo tổng thưởng | có độ chệch do tự khởi tạo |
| Phương sai | cao | thường thấp hơn |
| Cập nhật trực tuyến | phải chờ hết lượt | thực hiện sau từng bước |
| Lý thuyết | gần hồi quy | xấp xỉ ngẫu nhiên và Bellman chiếu |
| Khác chính sách + xấp xỉ hàm | có thể dùng lấy mẫu quan trọng nhưng phương sai lớn | có nguy cơ phân kỳ do bộ ba bất ổn |

Ứng dụng và giới hạn: MC phù hợp khi cần đích không chệch và lượt ngắn; TD phù hợp khi cần cập nhật trực tuyến và phương sai thấp. Với dữ liệu khác chính sách kết hợp xấp xỉ hàm, MC có thể dùng lấy mẫu quan trọng nhưng phương sai lớn, còn TD có nguy cơ phân kỳ do bộ ba bất ổn.

::: exercise Câu hỏi kiểm tra (bài tập 2)
So sánh dự đoán MC và dự đoán TD(0) với xấp xỉ tuyến tính theo bốn tiêu chí: dạng đích, độ chệch/phương sai, khả năng cập nhật trực tuyến và độ khó phân tích lý thuyết.
:::

::: hint
Dùng bảng trên; với lý thuyết, nhớ MC gần hồi quy còn TD cần toán tử Bellman chiếu.
:::

::: solution
MC dùng đích $G_t$ — tổng thưởng đầy đủ, không phụ thuộc $w$ — nên không chệch theo tổng thưởng nhưng có phương sai cao; TD dùng $R_{t+1} + \gamma x(S_{t+1})^\top w_t$ nên có độ chệch do tự khởi tạo nhưng thường có phương sai thấp hơn. MC phải chờ hết lượt; TD cập nhật ngay sau mỗi bước. Về lý thuyết, MC-SGD gần hồi quy SGD chuẩn với dữ liệu độc lập cùng phân phối và điều kiện Robbins–Monro; TD tuyến tính cần phân tích xấp xỉ ngẫu nhiên với toán tử Bellman chiếu, giả thiết chuỗi Markov phù hợp, $\gamma < 1$ và $\Phi$ đủ hạng.
:::

<!-- note-topic-id: lec-07-topic-10 -->
## Điều khiển với giá trị hành động và SARSA tuyến tính

Vấn đề: để điều khiển, ta cần ước lượng giá trị hành động chứ không chỉ giá trị trạng thái.

Trực giác: xấp xỉ $\hat q(s,a,w) \approx Q^\pi(s,a)$ hoặc $Q^*(s,a)$, rồi rút chính sách tham lam $\pi_w(s) \in \arg\max_a \hat q(s,a,w)$. Bài toán điều khiển vừa tự khởi tạo đích, vừa cải thiện chính sách, nên đích thay đổi liên tục.

Hình thức. Hai cập nhật quen thuộc với hàm xấp xỉ:

SARSA (theo chính sách):

$$\delta_t = R_{t+1} + \gamma \hat q(S_{t+1}, A_{t+1}, w_t) - \hat q(S_t, A_t, w_t), \qquad w_{t+1} = w_t + \alpha_t \delta_t \nabla_w \hat q(S_t, A_t, w_t).$$

Q-learning (khác chính sách):

$$\delta_t = R_{t+1} + \gamma \max_a \hat q(S_{t+1}, a, w_t) - \hat q(S_t, A_t, w_t).$$

Trường hợp tuyến tính với $x(s,a)$, SARSA trở thành

$$w_{t+1} = w_t + \alpha_t \delta_t x(S_t, A_t), \qquad \delta_t = R_{t+1} + \gamma x(S_{t+1}, A_{t+1})^\top w_t - x(S_t, A_t)^\top w_t,$$

với quy ước $\hat q(E, \cdot, w) = 0$ khi $S_{t+1}$ là trạng thái kết thúc. Tính tay đầy đủ ở chủ đề thực hành.

Ứng dụng và giới hạn: SARSA tuyến tính vẫn dùng dữ liệu theo chính sách như SARSA dạng bảng, nhưng các bảo đảm hội tụ dạng bảng (MDP hữu hạn, $\gamma < 1$, GLIE, Robbins–Monro) không tự động chuyển sang trường hợp xấp xỉ hàm. Các kết quả hữu hạn thời gian cho SARSA tuyến tính cần giả thiết cấu trúc mạnh hơn.

::: exercise Câu hỏi kiểm tra
Vì sao trong SARSA tuyến tính, đích $\gamma x(S_{t+1}, A_{t+1})^\top w_t$ dùng hành động $A_{t+1}$ thực tế, còn Q-learning dùng $\max_a$?
:::

::: hint
Nhớ SARSA là thuật toán theo chính sách: hành động kế tiếp được lấy từ chính sách hành vi.
:::

::: solution
SARSA đánh giá chính sách hành vi đang chạy, nên đích phải là giá trị của cặp $(S_{t+1}, A_{t+1})$ mà chính sách đó thực sự chọn tiếp — do đó cần $A_{t+1}$ được lấy mẫu. Q-learning học $q_*$ bất kể chính sách hành vi, nên đích thay hành động kế bằng giá trị tốt nhất $\max_a \hat q(S_{t+1}, a, w_t)$. Q-learning vì thế là thuật toán khác chính sách; khi kết hợp đích tự khởi tạo với xấp xỉ hàm, nó có đủ ba thành phần của bộ ba bất ổn.
:::

<!-- note-topic-id: lec-07-topic-11 -->
## Đích Q-learning tuyến tính và bộ ba bất ổn

Vấn đề: Q-learning tuyến tính có hội tụ như SARSA tuyến tính không?

Trực giác: đích Q-learning tuyến tính là $R_{t+1} + \gamma \max_a x(S_{t+1}, a)^\top w_t$; nó vừa tự khởi tạo vì phụ thuộc $w_t$, vừa khác chính sách vì dữ liệu đến từ chính sách hành vi, vừa dùng xấp xỉ hàm. Ba thành phần này đồng thời tạo thành bộ ba bất ổn:

$$\text{tự khởi tạo} + \text{khác chính sách} + \text{xấp xỉ hàm},$$

có thể làm TD hoặc Q-learning phân kỳ. Bộ ba bất ổn là một nguy cơ, không phải kết luận rằng mọi lần chạy đều phân kỳ; TD tuyến tính theo chính sách với chính sách cố định vẫn hội tụ dưới giả thiết phù hợp. Vì vậy Q-learning tuyến tính khác chính sách cần các điều kiện chặt hơn.

Các hướng khắc phục nêu trong nguồn gồm điều chỉnh trọng số cho dữ liệu khác chính sách, mạng mục tiêu, điều chuẩn và cắt ngưỡng; chúng đặc biệt quan trọng trong Học tăng cường sâu.

Ứng dụng và giới hạn: với MC khác chính sách, có thể dùng lấy mẫu quan trọng nhưng phương sai lớn. Với TD khác chính sách, nguy cơ phân kỳ là rào cản lý thuyết chính và chưa được giải quyết triệt để; nhiều cách ổn định hoá cần giả thiết mạnh hoặc dẫn tới nghiệm chệch.

::: exercise Câu hỏi kiểm tra (bài tập 3)
Trình bày bộ ba bất ổn và giải thích vì sao từng thành phần riêng lẻ không gây vấn đề tương tự.
:::

::: hint
Xét từng cặp: tự khởi tạo + xấp xỉ hàm theo chính sách; tự khởi tạo + khác chính sách dạng bảng; khác chính sách + xấp xỉ hàm không tự khởi tạo.
:::

::: solution
Bộ ba bất ổn là sự kết hợp của tự khởi tạo, dữ liệu khác chính sách và xấp xỉ hàm; nó có thể làm TD hoặc Q-learning bất ổn hay phân kỳ. Trong các trường hợp đối chiếu, phương pháp dạng bảng vẫn giữ cấu trúc toán tử Bellman; TD tuyến tính theo chính sách với chính sách cố định hội tụ tới điểm cố định Bellman chiếu dưới giả thiết phù hợp; MC khác chính sách không tự khởi tạo có thể dùng lấy mẫu quan trọng. Khi cả ba thành phần xuất hiện, phép cập nhật không còn tương ứng với một toán tử co trên không gian tham số, còn sai số xấp xỉ lan truyền qua đích tự khởi tạo. Đây là nguy cơ, không phải kết luận luôn phân kỳ.
:::

<!-- note-topic-id: lec-07-topic-14 -->
## Kết quả MDP tuyến tính

Vấn đề: lý thuyết hiện đại nói gì về bảo đảm cho xấp xỉ tuyến tính trong điều khiển?

Hướng nghiên cứu: trong lớp MDP tuyến tính — nơi cấu trúc MDP được biểu diễn qua đặc trưng chiều $d$ — kết quả của Jin và cộng sự (2020) cho thấy một biến thể lạc quan của lặp giá trị bình phương tối thiểu (LSVI) đạt độ hối tiếc cỡ $\tilde O(\sqrt{d^3 H^3 T})$ trong thiết lập theo lượt với chân trời $H$, không phụ thuộc trực tiếp vào số trạng thái hay số hành động. Với cấu trúc tuyến tính đúng, độ khó phụ thuộc chiều đặc trưng thay vì kích thước bảng.

Giới hạn của phát biểu trong nguồn: nguồn chỉ nêu kết quả ở mức định hướng, thiếu định nghĩa chính xác về MDP tuyến tính, cách xây dựng khoảng tin cậy và các hằng số. Vì vậy phần này chỉ ghi nhận hướng nghiên cứu và bậc độ hối tiếc, không phát biểu định lý đầy đủ hay suy rộng sang xấp xỉ hàm tổng quát.

::: exercise Câu hỏi kiểm tra
Độ hối tiếc $\tilde O(\sqrt{d^3 H^3 T})$ phụ thuộc những đại lượng nào và không phụ thuộc những đại lượng nào? Điều đó nói lên điều gì về vai trò của đặc trưng?
:::

::: hint
Đọc kỹ phát biểu: $d$, $H$, $T$ so với số trạng thái và số hành động.
:::

::: solution
Độ hối tiếc phụ thuộc chiều đặc trưng $d$, chân trời $H$ và số bước tương tác $T$, và không phụ thuộc trực tiếp vào $|\mathcal S|$ hay $|\mathcal A|$. Với MDP tuyến tính, độ khó được đo bằng chiều của cấu trúc tuyến tính chứ không bằng kích thước không gian trạng thái–hành động.
:::

<!-- note-topic-id: lec-07-topic-16 -->
## Khung đích và thực hành điều khiển

### Phân loại đích

Vấn đề: trước khi tính tay, cần một khung phân loại thống nhất để không nhầm đích của từng thuật toán.

Trực giác: mọi thuật toán trong bài đều có dạng cập nhật $w_{t+1} = w_t + \alpha_t (y_t - \hat q(S_t, A_t, w_t)) x(S_t, A_t)$; chúng chỉ khác nhau ở đích $y_t$ và ở chính sách sinh dữ liệu.

Hình thức, bốn đích:

- Điều khiển MC: $y_t = G_t$, tổng thưởng đầy đủ của lượt.
- Dự đoán TD(0): $y_t = R_{t+1} + \gamma x(S_{t+1})^\top w_t$.
- SARSA: $y_t = R_{t+1} + \gamma x(S_{t+1}, A_{t+1})^\top w_t$, với $A_{t+1}$ từ chính sách hành vi.
- Q-learning: $y_t = R_{t+1} + \gamma \max_a x(S_{t+1}, a)^\top w_t$.

Ứng dụng: bảng này là bản đồ khi tính tay — xác định đích trước, rồi áp cùng một khuôn cập nhật. Giới hạn: chỉ MC có đích độc lập với $w$; ba đích còn lại đều tự khởi tạo và do đó là bán gradient.

::: exercise Câu hỏi kiểm tra
Với cùng một mẫu chuyển tiếp $(S_t, A_t, R_{t+1}, S_{t+1})$, viết cả bốn đích và chỉ ra đích nào trùng nhau trong trường hợp nào.
:::

::: hint
So sánh $\gamma x(S_{t+1}, A_{t+1})^\top w_t$ với $\gamma \max_a x(S_{t+1}, a)^\top w_t$.
:::

::: solution
Bốn đích như trên. Dự đoán TD(0) và SARSA dùng hai loại hàm khác nhau: TD dùng giá trị trạng thái, còn SARSA dùng giá trị hành động. Nếu quy ước $v(S_{t+1})=q(S_{t+1},A_{t+1})$ trong trường hợp chỉ có một hành động khả dụng, hai đích có cùng giá trị số. SARSA và Q-learning trùng khi hành động $A_{t+1}$ do chính sách hành vi chọn cũng là hành động tham lam tại $S_{t+1}$. MC khác các đích còn lại vì dùng tổng thưởng đầy đủ và không tự khởi tạo.
:::

### Tính tay đánh giá MC và SARSA trên chuỗi năm trạng thái

Vấn đề: kiểm chứng toàn bộ khuôn lý thuyết bằng hai phép tính đầy đủ trên chuỗi $A\ B\ C\ D\ E$.

Thiết lập (tr. 40 và bài tập 7–8). $A$ và $E$ là trạng thái kết thúc; $D$ là trạng thái bắt đầu; hành động $0$ là đi trái, $1$ là đi phải; môi trường tất định, tối đa 3 bước, $\gamma = 1$. Phần thưởng: $R(A) = 1000$, $R(E) = 10$, mọi phần thưởng còn lại bằng $-1$ (phần thưởng gắn với trạng thái kết thúc được nhận khi bước vào trạng thái đó). Xấp xỉ tuyến tính cho $Q$:

$$\hat q(s,a,w) = x(s,a)^\top w, \qquad x(s,a) = \begin{bmatrix} d_{\text{left}}(s) \\ u(a) \\ 1 \end{bmatrix},$$

trong đó $d_{\text{left}}(B) = 1$, $d_{\text{left}}(C) = 2$, $d_{\text{left}}(D) = 3$ (khoảng cách tới tường trái), và $u(0) = +1$, $u(1) = -1$.

#### Bài 7: đánh giá MC trên một lượt trong quá trình điều khiển

Cho $w_0 = [1, 1, -1]^\top$, $\alpha = 0.1$, và một lượt duy nhất. Phép tính này chỉ cập nhật giá trị; chưa thực hiện bước cải thiện chính sách.

$$(D, 0, -1, C),\quad (C, 0, -1, B),\quad (B, 0, +1000, A).$$

Bước 1 — các tổng thưởng. Với $\gamma = 1$, $G_t$ là tổng phần thưởng từ thời điểm $t$ đến hết lượt:

$$G_2 = R_3 = +1000, \qquad G_1 = R_2 + R_3 = -1 + 1000 = 999, \qquad G_0 = R_1 + R_2 + R_3 = -1 - 1 + 1000 = 998.$$

Bước 2 — các vector đặc trưng:

$$x(D,0) = \begin{bmatrix} 3 \\ +1 \\ 1 \end{bmatrix}, \qquad x(C,0) = \begin{bmatrix} 2 \\ +1 \\ 1 \end{bmatrix}, \qquad x(B,0) = \begin{bmatrix} 1 \\ +1 \\ 1 \end{bmatrix}.$$

Bước 3 — cập nhật MC theo đúng thứ tự thời gian, $w_{t+1} = w_t + \alpha (G_t - x_t^\top w_t) x_t$.

Lần 1, $(D,0)$, $G_0 = 998$: $x_0^\top w_0 = 3(1) + 1(1) + 1(-1) = 3$; sai số $998 - 3 = 995$; bước $\alpha \cdot 995 = 99.5$;

$$w_1 = \begin{bmatrix} 1 \\ 1 \\ -1 \end{bmatrix} + 99.5 \begin{bmatrix} 3 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 299.5 \\ 100.5 \\ 98.5 \end{bmatrix}.$$

Lần 2, $(C,0)$, $G_1 = 999$: $x_1^\top w_1 = 2(299.5) + 100.5 + 98.5 = 599 + 199 = 798$; sai số $999 - 798 = 201$; bước $0.1 \cdot 201 = 20.1$;

$$w_2 = \begin{bmatrix} 299.5 \\ 100.5 \\ 98.5 \end{bmatrix} + 20.1 \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 339.7 \\ 120.6 \\ 118.6 \end{bmatrix}.$$

Lần 3, $(B,0)$, $G_2 = 1000$: $x_2^\top w_2 = 339.7 + 120.6 + 118.6 = 578.9$; sai số $1000 - 578.9 = 421.1$; bước $0.1 \cdot 421.1 = 42.11$;

$$w_3 = \begin{bmatrix} 339.7 \\ 120.6 \\ 118.6 \end{bmatrix} + 42.11 \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 381.81 \\ 162.71 \\ 160.71 \end{bmatrix}.$$

Bước 4 — giá trị xấp xỉ cuối cùng:

$$\hat q(D,0) = 3(381.81) + 162.71 + 160.71 = 1145.43 + 323.42 = 1468.85,$$
$$\hat q(C,0) = 2(381.81) + 162.71 + 160.71 = 763.62 + 323.42 = 1087.04,$$
$$\hat q(B,0) = 381.81 + 162.71 + 160.71 = 705.23.$$

Nhận xét: một lượt duy nhất với đích $+1000$ đẩy trọng số lên rất mạnh; các giá trị xấp xỉ vượt xa tổng thưởng thực tế vì chỉ có một mẫu và bước học cố định $\alpha = 0.1$. Điều này minh họa vì sao phân tích hội tụ cần điều kiện thích hợp cho dãy bước học.

#### Bài 8: SARSA, tự tính lại đầy đủ

Cho $w_0 = [1, 1, -1]^\top$, $\alpha = 0.2$, $\epsilon = 0.25$, và ba mẫu liên tiếp. Giá trị $\epsilon$ mô tả chính sách hành vi đã sinh mẫu; ba mẫu đã cho sẵn nên $\epsilon$ không đi vào phép cập nhật dưới đây.

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
Trong bài 8, vì sao $\delta_1=-1.2$? Kiểm tra lại rằng $\hat q(D,1,w_3)-\hat q(D,0,w_3)=-2w_{3,2}$.
:::

::: hint
Tính $\delta_1$ từ công thức; với phần kiểm tra, tính $\hat q(D,1,w_3) - \hat q(D,0,w_3)$ theo thành phần thứ hai của $w_3$.
:::

::: solution
$\delta_1=-1-2.6+2.4=-1.2$. Phần kiểm tra: $\hat q(D,1,w_3)-\hat q(D,0,w_3)=27.424-23.296=4.128$; hai vector đặc trưng chỉ khác thành phần $u(a)$, nên chênh lệch bằng $w_{3,2}(-1-1)=-2w_{3,2}=-2(-2.064)=4.128$.
:::

<!-- note-topic-id: lec-07-topic-12 -->
## Phạm vi lý thuyết, giới hạn và kết luận

Vấn đề: tổng hợp những gì lý thuyết bảo đảm và những gì còn thiếu sau các ví dụ tính tay.

Các hạn chế lý thuyết theo tr. 43:

1. Xấp xỉ phi tuyến và mạng sâu chưa có lý thuyết tổng quát cho DQN hoặc actor–critic ngoài một số trường hợp đặc biệt.
2. Bộ ba bất ổn chưa được giải quyết triệt để; nhiều cách ổn định hoá cần giả thiết mạnh hoặc dẫn tới nghiệm chệch.
3. Phần lớn định lý giả sử đặc trưng đã phù hợp, chưa giải thích đầy đủ quá trình học biểu diễn.
4. TD triệt tiêu sai số Bellman chiếu, không trực tiếp tối thiểu hoá sai số so với $v^\pi$ hoặc chất lượng chính sách cuối.
5. Bảo đảm khám phá với xấp xỉ hàm tổng quát còn hạn chế và phụ thuộc mạnh vào cấu trúc bài toán.
6. Trong học tăng cường ngoại tuyến, phân phối hành vi có thể không phủ đủ các trạng thái–hành động cần đánh giá.

Kết luận theo tr. 44: xấp xỉ hàm giúp Học tăng cường làm việc với không gian trạng thái lớn hoặc liên tục. Monte Carlo gần bài toán hồi quy vì đích không phụ thuộc trọng số đang học, nhưng có phương sai lớn và phải chờ hết lượt. TD cập nhật sau từng bước và thường có phương sai thấp hơn, song dùng đích tự khởi tạo nên cần phân tích điểm cố định Bellman chiếu. Khi chuyển sang điều khiển, chính sách thay đổi; trường hợp khác chính sách còn có nguy cơ của bộ ba bất ổn. Vì vậy mọi bảo đảm hội tụ phải đi kèm đúng giả thiết về chính sách, đặc trưng, chuỗi Markov và bước học.

::: exercise Câu hỏi kiểm tra
Xếp bốn trường hợp MC, TD(0), SARSA và Q-learning với xấp xỉ tuyến tính theo mức độ khó của phân tích hội tụ; nêu yếu tố làm mỗi trường hợp khó hơn trường hợp trước.
:::

::: hint
Phân biệt đích hoàn chỉnh với đích tự khởi tạo, theo chính sách với khác chính sách, và dự đoán với điều khiển.
:::

::: solution
MC gần hồi quy nhất vì đích hoàn chỉnh không phụ thuộc $w$. TD(0) khó hơn vì tự khởi tạo đích, nhưng với chính sách cố định và các giả thiết đã nêu, TD tuyến tính theo chính sách hội tụ tới điểm cố định Bellman chiếu. SARSA khó hơn nữa vì vừa tự khởi tạo vừa cải thiện chính sách trong quá trình học. Q-learning tuyến tính khác chính sách kết hợp đủ ba thành phần của bộ ba bất ổn, nên không được suy ra bảo đảm hội tụ từ TD dự đoán. Đây là thứ tự về độ khó phân tích, không phải bảng xếp hạng hiệu quả thực nghiệm.
:::

## Tài liệu tham khảo

- Tạ Việt Cường. Lecture 07: Hàm xấp xỉ trong Reinforcement Learning. VNU-UET, tháng 4 năm 2026, tr. 1–45.
- Tạ Việt Cường. Bài tập tuần 7 — Function Approximation, ngày 8 tháng 4 năm 2026, bài 1–8.
- David Silver. Lecture 6: Value Function Approximation. UCL RL Course.
- J. Tsitsiklis và B. Van Roy. Analysis of temporal-difference learning with function approximation. 1996.
- J. Bhandari, D. Russo, R. Singal. A Finite Time Analysis of Temporal Difference Learning With Linear Function Approximation. COLT 2018 / Operations Research 2021.
- C. Jin, Z. Yang, Z. Wang, M. I. Jordan. Provably Efficient Reinforcement Learning with Linear Function Approximation. COLT 2020.
- S. Zou, T. Xu, Y. Liang. Finite-Sample Analysis for SARSA with Linear Function Approximation. NeurIPS 2019.
- S. Zhang, H. Yao, S. Whiteson. Breaking the Deadly Triad with a Target Network. ICML 2021.
- Y. Peng, K. Jin, L. Zhang, Z. Zhang. A Finite Sample Analysis of Distributional TD Learning with Linear Function Approximation. NeurIPS 2025.
