# Bài 07 — Hàm xấp xỉ trong Học tăng cường

## Mục tiêu và kiến thức tiên quyết

- Giải thích vì sao bảng tra không còn phù hợp khi không gian trạng thái hoặc hành động lớn hoặc liên tục, và nêu ba lợi ích của xấp xỉ hàm: tổng quát hoá, ra quyết định nhanh và hỗ trợ không gian liên tục hoặc cao chiều.
- Viết và phân tích xấp xỉ tuyến tính cho giá trị trạng thái $\hat v(s,w)$ và giá trị hành động $\hat q(s,a,w)$, kể cả vai trò của thiết kế đặc trưng.
- Phân biệt cập nhật Monte Carlo với gradient đầy đủ và cập nhật TD(0) bán gradient; phát biểu đúng giả thiết và giới hạn hội tụ của TD tuyến tính theo chính sách.
- Triển khai điều khiển với giá trị hành động: SARSA tuyến tính và đích Q-learning tuyến tính; nhận diện bộ ba bất ổn (*deadly triad*) như một nguy cơ, không phải kết luận luôn phân kỳ.
- Tự tính lại đầy đủ bài tập 7 và 8, nêu từng vector đặc trưng, từng đích và từng bước cập nhật.

Kiến thức tiên quyết từ Bài 06: quy trình quyết định Markov (MDP), dự đoán và điều khiển Monte Carlo, TD(0), SARSA, Q-learning dạng bảng, điều kiện GLIE và điều kiện Robbins–Monro. Toán cần dùng: tích vô hướng có trọng số, ma trận, phép chiếu trực giao theo chuẩn có trọng số và trị riêng.

## Bản đồ chủ đề

Bản đồ bốn nhóm: nhóm **cốt lõi** gồm 12 chủ đề `lec-07-topic-01` đến `lec-07-topic-12` tạo thành mạch chính; nhóm **cầu nối** gồm `lec-07-topic-13` tóm tắt tiên quyết từ Bài 06; nhóm **bổ sung** gồm `lec-07-topic-14` và `lec-07-topic-15` cho kết quả hiện đại và chứng minh; nhóm **đọc thêm/thực hành** gồm `lec-07-topic-16` với tính tay bài 7–8. Sáu mạch chính: mở/cầu nối 7 phút; động cơ–đặc trưng 23 phút; MC 21 phút; TD–Bellman chiếu 33 phút; điều khiển/SARSA 19 phút; Q-learning–bộ ba bất ổn–thực hành–kết luận 17 phút; tổng 120 phút. Phần chữa bài 30 phút dùng bài 4, 7 và 8. Thứ tự trình bày mỗi chủ đề theo vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng/giới hạn → kiểm tra; các chủ đề 13, 14 và 15 gộp bước trực giác với ví dụ vì chúng chỉ tóm tắt hoặc nêu hướng nghiên cứu, không có ví dụ tính được trong nguồn.

### Giới hạn bảng tra

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mở đầu mạch động cơ, đặt vấn đề mà cả bài giải quyết.
- Kết nối vào: bảng tra $V^\pi$, $Q^\pi$ từ Bài 06.
- Kết nối ra: dẫn tới nhu cầu chia sẻ tham số.
- Nguồn: tr. 22–23.

### Chia sẻ tham số

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: nêu ý tưởng học hàm tham số và lợi ích chia sẻ thông tin.
- Kết nối vào: giới hạn bảng tra.
- Kết nối ra: dẫn tới xấp xỉ tuyến tính cụ thể.
- Nguồn: tr. 23.

### Xấp xỉ tuyến tính và miền/kích thước

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: chuẩn hoá ký hiệu $x$, $w$, $\Phi$ dùng suốt bài.
- Kết nối vào: ý tưởng hàm tham số.
- Kết nối ra: nền cho mọi cập nhật MC/TD tuyến tính phía sau.
- Nguồn: tr. 24–31.

### Thiết kế đặc trưng và giới hạn biểu diễn

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: cho thấy chất lượng đặc trưng quyết định chất lượng xấp xỉ.
- Kết nối vào: xấp xỉ tuyến tính.
- Kết nối ra: giải thích sai số xấp xỉ và aliasing trong ví dụ chuỗi phía sau.
- Nguồn: tr. 28–31.

### Phân loại đích MC/TD

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: phân biệt hai loại "nhãn" trong RL với học có giám sát.
- Kết nối vào: xấp xỉ tuyến tính.
- Kết nối ra: dẫn tới hai cập nhật MC và TD.
- Nguồn: tr. 27, 32.

### MC với gradient đầy đủ

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mạch MC, cập nhật gradient thật trên mất mát bình phương.
- Kết nối vào: phân loại đích.
- Kết nối ra: đối chiếu với bán gradient TD.
- Nguồn: tr. 33–34 và bài tập 4.

### TD(0) bán gradient

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mạch TD, cập nhật với đích tự khởi tạo (*bootstrap*).
- Kết nối vào: MC gradient đầy đủ.
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

### Hội tụ dạng bảng từ Bài 06

- Nhóm: `cầu nối`.
- Vai trò trong mạch: mở bài, nhắc kết quả tiên quyết.
- Kết nối vào: chứng minh điều khiển MC với GLIE và SARSA dạng bảng từ Bài 06.
- Kết nối ra: câu hỏi "chuyện gì xảy ra nếu $Q$ là hàm tuyến tính" dẫn vào nội dung mới.
- Nguồn: tr. 5–20, chỉ tóm tắt điều kiện, không trình bày lại chứng minh dài.

### Kết quả MDP tuyến tính

- Nhóm: `bổ sung`.
- Vai trò trong mạch: cho thấy lý thuyết hiện đại tiến gần thực tế.
- Kết nối vào: nguy cơ của bộ ba bất ổn trong điều khiển khác chính sách.
- Kết nối ra: dẫn tới danh sách vấn đề mở.
- Nguồn: tr. 42; chỉ nêu hướng nghiên cứu và ký hiệu, không phát biểu định lý đầy đủ vì nguồn thiếu thiết lập chi tiết.

### Chứng minh MC-SGD và vai trò Robbins–Monro

- Nhóm: `bổ sung`.
- Vai trò trong mạch: củng cố nền toán của cập nhật MC và bước học.
- Kết nối vào: MC với gradient đầy đủ.
- Kết nối ra: làm rõ đối chiếu gradient đầy đủ của MC với bán gradient của TD.
- Nguồn: bài tập 4 và 6.

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
- Kỳ vọng $\mathbb E_\pi[\cdot]$ tính theo quỹ đạo sinh bởi $\pi$; kỳ vọng có điều kiện $\mathbb E[\cdot \mid S_t = s, A_t = a]$.
- Bước học $\alpha_t$ theo số lần cập nhật; trong tính tay, $\alpha$ là hằng số cho từng bài.

<!-- note-topic-id: lec-07-topic-13 -->
## Cầu nối: hội tụ dạng bảng từ Bài 06

Vấn đề: trước khi thêm hàm xấp xỉ, cần nhớ chính xác những gì đã được bảo đảm trong trường hợp bảng tra, để biết chính xác cái gì mất đi khi thay bảng bằng hàm tham số.

Trực giác và tóm tắt điều kiện. Với điều khiển Monte Carlo dạng bảng trên MDP hữu hạn theo lượt, phần thưởng bị chặn, nếu dãy chính sách thỏa GLIE — mọi cặp $(s,a)$ được thăm vô hạn lần và chính sách hội tụ về tham lam — thì $Q_k(s,a) \to q_*(s,a)$; chuỗi suy luận là GLIE cho đủ dữ liệu, luật số lớn mạnh cho đánh giá đúng, cải tiến chính sách ép tiến về tối ưu, và phản chứng loại trừ chính sách giới hạn không tối ưu. Với SARSA dạng bảng trên MDP hữu hạn, $\gamma < 1$, chính sách GLIE và bước học thỏa Robbins–Monro $\sum_t \alpha_t(s,a) = \infty$, $\sum_t \alpha_t^2(s,a) < \infty$ cho từng cặp, thì $Q_t(s,a) \to q_*(s,a)$ gần như chắc chắn; chứng minh viết sai số dưới dạng xấp xỉ ngẫu nhiên, dùng tính co của toán tử Bellman tối ưu $\|T_*Q_t - q_*\|_\infty \le \gamma \|Q_t - q_*\|_\infty$, rồi dùng GLIE để chuyển từ đánh giá sang điều khiển. Chi tiết chứng minh đã trình bày trong Bài 06, ở đây không lặp lại.

Giới hạn của bảng tra: không thể lưu hết mọi trạng thái và hành động khi $|\mathcal S|$, $|\mathcal A|$ lớn hoặc liên tục; không tổng quát hoá giữa các trạng thái "na ná nhau"; dữ liệu RL không i.i.d. và không dừng. Câu hỏi kết nối của nguồn: chuyện gì xảy ra nếu hàm $Q$ là hàm tuyến tính hoặc mạng sâu? Toàn bộ phần còn lại của bài trả lời câu hỏi này.

::: exercise Câu hỏi kiểm tra
Nêu hai điều kiện của GLIE và giải thích vì sao thiếu điều kiện khám phá vô hạn làm chứng minh bảng tra sụp đổ.
:::

::: hint
Xem lại Bước 1 của chứng minh điều khiển MC: vai trò của $N_k(s,a) \to \infty$ đối với trung bình mẫu.
:::

::: solution
GLIE yêu cầu (i) $\lim_{k\to\infty} N_k(s,a) = \infty$ cho mọi cặp $(s,a)$ và (ii) $\pi_k$ hội tụ về chính sách tham lam. Nếu một cặp chỉ được thăm hữu hạn lần, trung bình mẫu tại cặp đó dừng ở một số hữu hạn mẫu nên sai số có thể không biến mất; khi đó không thể kết luận $Q_k \to q_*$ cho mọi cặp, và phản chứng ở Bước 4 không còn giá trị vì đánh giá chưa chính xác.
:::

<!-- note-topic-id: lec-07-topic-01 -->
## Giới hạn bảng tra

Vấn đề: bảng tra gán một số riêng cho mỗi trạng thái hoặc mỗi cặp trạng thái–hành động, tức là học các ánh xạ $V^\pi: \mathcal S \to \mathbb R$ và $Q^\pi: \mathcal S \times \mathcal A \to \mathbb R$ dưới dạng bảng. Cách này dễ hiểu và dễ phân tích, nhưng khó mở rộng khi $|\mathcal S|$, $|\mathcal A|$ lớn hoặc liên tục.

Trực giác: hai trạng thái "na ná nhau" trong bảng tra là hai ô hoàn toàn tách biệt; kinh nghiệm ở một trạng thái không giúp gì cho trạng thái kia, dù chúng giống nhau về cấu trúc. Ngoài ra, dữ liệu RL không i.i.d. và không dừng, nên việc ước lượng độc lập từng ô vừa tốn mẫu vừa lãng phí thông tin.

Hình thức: hai lợi ích chính của xấp xỉ hàm là (i) khả năng tổng quát hoá giữa các trạng thái tương tự — cập nhật ở một trạng thái kéo theo thay đổi ước lượng ở các trạng thái có đặc trưng gần nhau — và (ii) khả năng ra quyết định nhanh trong không gian lớn, vì chỉ cần tính $\hat v(s,w)$ thay vì tra bảng khổng lồ.

Giới hạn: tổng quát hoá là con dao hai lưỡi; nếu đặc trưng kém, thông tin sai ở một trạng thái lan sang các trạng thái khác. Đây là chủ đề của phần thiết kế đặc trưng.

::: exercise Câu hỏi kiểm tra
Vì sao lập luận "dữ liệu RL không i.i.d. và không dừng" khiến bảng tra tốn mẫu hơn so với một hàm tham số chia sẻ thông tin?
:::

::: hint
So sánh số mẫu cần để ước lượng độc lập từng ô với số tham số của một hàm tuyến tính.
:::

::: solution
Với bảng tra, mỗi ô $(s,a)$ cần đủ mẫu riêng để ước lượng chính xác, và các mẫu không i.i.d. khiến việc dùng lại dữ liệu giữa các ô không tự động xảy ra. Với hàm tham số có $d$ tham số, mọi mẫu đều cập nhật cùng một $w$, nên thông tin từ một quỹ đạo được chia sẻ cho mọi trạng thái có đặc trưng tương tự; số lượng "đại lượng cần học" giảm từ cỡ $|\mathcal S \times \mathcal A|$ xuống $d$.
:::

<!-- note-topic-id: lec-07-topic-02 -->
## Chia sẻ tham số

Vấn đề: làm sao học một ước lượng giá trị mà không cần một tham số riêng cho mỗi trạng thái?

Trực giác: thay vì lưu bảng, học một hàm tham số $\hat v(s,w) \approx V^\pi(s)$ hoặc $\hat q(s,a,w) \approx Q^\pi(s,a)$, trong đó $w$ là vector trọng số dùng chung cho mọi trạng thái. Cùng một bộ $w$ phục vụ mọi truy vấn, nên mỗi cập nhật điều chỉnh cách đánh giá của cả lớp trạng thái.

Hình thức: cách tiếp cận này mang lại ba lợi ích nêu trong nguồn: quyết định nhanh, chia sẻ thông tin giữa nhiều trạng thái, và hỗ trợ không gian trạng thái liên tục hoặc cao chiều.

Ứng dụng và giới hạn: chia sẻ tham số là nền của nhiều phương pháp Học tăng cường hiện đại, nhưng nó cũng tạo tương tác giữa các cặp trạng thái–hành động. Một cập nhật tại $(s,a)$ làm thay đổi $\hat q$ tại các cặp khác; đây là một thành phần của bộ ba bất ổn sẽ gặp ở phần sau.

::: exercise Câu hỏi kiểm tra
Cho hai trạng thái $s_1 \ne s_2$ với $x(s_1) = x(s_2)$. Vì sao với hàm tham số ta bắt buộc có $\hat v(s_1,w) = \hat v(s_2,w)$, và điều đó nói lên điều gì?
:::

::: hint
Viết định nghĩa $\hat v(s,w)$ theo $x(s)$ và $w$.
:::

::: solution
Vì $\hat v(s,w) = x(s)^\top w$ chỉ phụ thuộc vào $s$ qua $x(s)$, hai trạng thái có cùng vector đặc trưng có cùng ước lượng. Đây chính là cơ chế tổng quát hoá: hàm không phân biệt được hai trạng thái mà đặc trưng không phân biệt; chất lượng của xấp xỉ vì vậy phụ thuộc hoàn toàn vào việc đặc trưng có tách biệt đúng các trạng thái cần phân biệt hay không.
:::

<!-- note-topic-id: lec-07-topic-03 -->
## Xấp xỉ tuyến tính và miền/kích thước

Vấn đề: chọn lớp hàm nào để xấp xỉ giá trị?

Trực giác: lớp đơn giản nhất và có nhiều bảo đảm lý thuyết nhất là lớp hàm tuyến tính theo tham số: giá trị là tích vô hướng giữa vector đặc trưng của trạng thái và vector trọng số.

Hình thức. Xấp xỉ tuyến tính được định nghĩa là

$$\hat v(s,w) = x(s)^\top w, \qquad \hat q(s,a,w) = x(s,a)^\top w,$$

trong đó $x(s) \in \mathbb R^d$ và $x(s,a) \in \mathbb R^d$ là các vector đặc trưng, $w \in \mathbb R^d$ là vector trọng số. Các dạng xấp xỉ khác nêu trong nguồn gồm cây quyết định, rừng ngẫu nhiên, kernel, láng giềng gần nhất, cơ sở Fourier và tile coding; mạng nơ-ron mạnh về biểu diễn nhưng tối ưu khó hơn và ít bảo đảm tổng quát. Bài này tập trung vào lớp tuyến tính vì mọi kết quả hội tụ cổ điển đều được phát biểu cho lớp này.

Khác biệt với học có giám sát: trong Học tăng cường, "nhãn" thường là đích tự khởi tạo hoặc tổng thưởng ngẫu nhiên,

$$y_t^{\mathrm{MC}} = G_t, \qquad y_t^{\mathrm{TD}} = R_{t+1} + \gamma\, \hat v(S_{t+1}, w),$$

nên dữ liệu vừa phụ thuộc chính sách, vừa phụ thuộc chính mô hình đang học.

Ví dụ về cấu trúc đặc trưng cho điều khiển: $x(s,a) = [\,x(s);\ \mathrm{one\text{-}hot}(a);\ x(s) \otimes \mathrm{one\text{-}hot}(a);\ 1\,]$, ghép đặc trưng trạng thái, mã hoá hành động và tích tensor của chúng.

Giới hạn: lớp tuyến tính chỉ biểu diễn được các hàm giá trị nằm trong không gian sinh bởi các đặc trưng; phần thiếu hụt là sai số xấp xỉ không thể xoá bằng cách học $w$.

::: exercise Câu hỏi kiểm tra
Với $x(s) \in \mathbb R^d$, tập hợp $\{\hat v(\cdot, w) : w \in \mathbb R^d\}$ là gì về mặt hình học, và vì sao nó là một không gian con chứ không phải toàn bộ không gian hàm trên $\mathcal S$?
:::

::: hint
Xét tổ hợp tuyến tính của hai trọng số $w_1, w_2$ và giá trị tương ứng.
:::

::: solution
Tập đó là không gian con có số chiều bằng hạng của ma trận đặc trưng $\Phi$, nên không vượt quá $d$. Nó do các thành phần của $x$ sinh ra. Thật vậy, $\hat v(\cdot, \theta w_1 + (1-\theta) w_2) = \theta \hat v(\cdot, w_1) + (1-\theta) \hat v(\cdot, w_2)$, nên tập này đóng với tổ hợp tuyến tính. Khi $\operatorname{rank}(\Phi) < |\mathcal S|$, không gian con này không chứa mọi hàm trên $\mathcal S$; vì vậy tồn tại hàm giá trị có sai số xấp xỉ không thể loại bỏ chỉ bằng cách học $w$.
:::

<!-- note-topic-id: lec-07-topic-04 -->
## Thiết kế đặc trưng và giới hạn biểu diễn

Vấn đề: chất lượng của xấp xỉ tuyến tính phụ thuộc hoàn toàn vào việc đặc trưng được thiết kế thế nào.

Trực giác qua ví dụ trong nguồn: với một bài toán điều hướng, có thể dùng vector

$$x(s) = [\,\text{khoảng cách tới đích},\ \text{khoảng cách tới vật cản},\ \text{tốc độ},\ 1\,]^\top.$$

Các ví dụ minh hoạ trong nguồn gồm Cartpole, Lunar Lander và cờ vua, nơi đặc trưng tóm tắt tình thế thành vài con số có ý nghĩa.

Hình thức: đặc trưng tốt làm bài toán gần tuyến tính hơn, tức hàm giá trị thực gần nằm trong không gian sinh bởi đặc trưng; đặc trưng kém gây sai số xấp xỉ, hiện tượng aliasing — hai trạng thái cần giá trị khác nhau bị biểu diễn giống nhau — và chính sách kém. Phần lớn lý thuyết cổ điển giả sử đặc trưng đã biết trước và tốt sẵn; việc học biểu diễn hầu như nằm ngoài các định lý đó.

Ứng dụng và giới hạn: trong ví dụ chuỗi năm trạng thái ở phần thực hành, đặc trưng $x(s,a)$ gồm khoảng cách tới tường trái, dấu hành động và hằng số $1$; đặc trưng này đủ để phân biệt các cặp $(s,a)$ trong ví dụ, nhưng với bài toán lớn hơn, việc chọn đặc trưng là vấn đề mở.

::: exercise Câu hỏi kiểm tra
Cho ba trạng thái $B, C, D$ với khoảng cách tới tường trái lần lượt $1, 2, 3$. Nếu hàm giá trị thực tăng tuyến tính theo khoảng cách này, vì sao đặc trưng $d_{\text{left}}(s)$ là lựa chọn tốt? Ngược lại, nếu giá trị thực không tuyến tính theo khoảng cách thì sao?
:::

::: hint
Xét $\hat v(s) = a\,d_{\text{left}}(s) + b$ và hỏi lớp này chứa những hàm nào.
:::

::: solution
Nếu $v$ tuyến tính theo $d_{\text{left}}$, thì $v(s) = a\,d_{\text{left}}(s) + b$ với một cặp $a,b$, và lớp xấp xỉ chứa đúng hàm này nên sai số xấp xỉ bằng không. Nếu $v$ không tuyến tính theo khoảng cách, chẳng hạn có dạng bậc hai, thì mọi hàm trong lớp đều lệch; học trọng số chỉ tìm được phép chiếu tốt nhất, và sai số xấp xỉ còn lại không thể xoá bằng dữ liệu nhiều hơn.
:::

<!-- note-topic-id: lec-07-topic-05 -->
## Phân loại đích MC/TD

Vấn đề: khi thay bảng bằng hàm xấp xỉ, "nhãn" để học lấy từ đâu? Đây là điểm phân loại các thuật toán.

Trực giác: trong học có giám sát, nhãn là cố định. Trong Học tăng cường, nguồn chỉ ra hai loại đích: tổng thưởng đầy đủ $G_t$ của Monte Carlo và đích tự khởi tạo $R_{t+1} + \gamma \hat v(S_{t+1}, w)$ của TD. Ba điểm phân biệt Monte Carlo, TD, SARSA và Q-learning là loại đích, dữ liệu theo chính sách hay khác chính sách, và cách cải thiện chính sách.

Hình thức: ta thường tối thiểu hoá lỗi bình phương cục bộ

$$J_t(w) = \frac{1}{2}\big(y_t - \hat v(S_t, w)\big)^2,$$

suy ra cập nhật SGD/bán gradient

$$w_{t+1} = w_t + \alpha_t \big(y_t - \hat v(S_t, w_t)\big) \nabla_w \hat v(S_t, w_t).$$

Trường hợp tuyến tính, với $x_t = x(S_t)$:

$$w_{t+1} = w_t + \alpha_t \big(y_t - x_t^\top w_t\big) x_t.$$

Ứng dụng và giới hạn: vì đích $y_t^{\mathrm{TD}}$ phụ thuộc vào $w_t$ đang được cập nhật, gradient của hàm mất mát theo nghĩa đầy đủ không còn là $\big(y_t - \hat v\big)\nabla \hat v$; đây là lý do gọi là bán gradient, được phân tích kỹ ở hai chủ đề tiếp theo.

::: exercise Câu hỏi kiểm tra
Viết $y_t^{\mathrm{TD}}$ tường minh và chỉ ra thành phần nào của nó phụ thuộc vào $w_t$.
:::

::: hint
Thay $\hat v(S_{t+1}, w)$ bằng $x(S_{t+1})^\top w$.
:::

::: solution
$y_t^{\mathrm{TD}} = R_{t+1} + \gamma\, x(S_{t+1})^\top w_t$. Thành phần $R_{t+1}$ không phụ thuộc $w_t$, còn $\gamma\, x(S_{t+1})^\top w_t$ phụ thuộc vào trọng số hiện tại. Vì đích di chuyển theo $w_t$, đạo hàm của $J_t$ theo $w$ đầy đủ sẽ có thêm số hạng từ $\partial y_t^{\mathrm{TD}}/\partial w$, mà cập nhật bán gradient bỏ qua số hạng đó.
:::

<!-- note-topic-id: lec-07-topic-06 -->
## MC với gradient đầy đủ

Vấn đề: cập nhật Monte Carlo với hàm xấp xỉ là gì, và nó có phải là hạ gradient thật không?

Trực giác: MC dùng tổng thưởng đầy đủ của lượt làm đích; đích này không phụ thuộc $w$, nên nó giống một nhãn cố định trong học có giám sát.

Hình thức. Đích MC là tổng lợi ích

$$G_t = \sum_{k=0}^{T-t-1} \gamma^k R_{t+1+k},$$

và cập nhật là

$$w_{t+1} = w_t + \alpha_t \big(G_t - \hat v(S_t, w_t)\big) \nabla_w \hat v(S_t, w_t).$$

Đây là gradient đầy đủ: vì $G_t$ không phụ thuộc $w$, số hạng này chính là $-\nabla_w \ell_t(w_t)$ với mất mát cục bộ $\ell_t(w) = \frac{1}{2}\big(G_t - \hat v(S_t,w)\big)^2$. Chứng minh từng bước ở chủ đề bổ sung 15.

Ưu điểm và nhược điểm: đích không tự khởi tạo nên không chệch theo tổng thưởng; nhược điểm là phương sai lớn và phải chờ hết lượt. Với bình phương tối thiểu tuyến tính theo lô, MC gần bài toán hồi quy chuẩn.

Điều kiện hội tụ: nếu dữ liệu i.i.d., đặc trưng bị chặn, $\sum_t \alpha_t = \infty$ và $\sum_t \alpha_t^2 < \infty$, thì MC-SGD hội tụ tới nghiệm tối ưu của lỗi bình phương trên phân phối dữ liệu. Lưu ý đây là hội tụ tới nghiệm hồi quy tốt nhất, không phải nhất thiết tới $v^\pi$, trừ khi lớp hàm chứa được $v^\pi$.

::: exercise Câu hỏi kiểm tra
Cho biết vì sao cập nhật MC với hàm xấp xỉ là gradient đầy đủ, trong khi cùng một dạng công thức với đích TD thì không.
:::

::: hint
So sánh sự phụ thuộc của $G_t$ và của $R_{t+1} + \gamma \hat v(S_{t+1}, w)$ vào $w$.
:::

::: solution
Với MC, đích $G_t$ chỉ phụ thuộc phần thưởng và quỹ đạo, không phụ thuộc $w$, nên $\nabla_w \frac{1}{2}(G_t - \hat v(S_t,w))^2 = -(G_t - \hat v(S_t,w))\nabla_w \hat v(S_t,w)$ chính xác. Với TD, đặt $\delta_t(w)=R_{t+1}+\gamma\hat v(S_{t+1},w)-\hat v(S_t,w)$. Bước hạ gradient đầy đủ của $\frac12\delta_t(w)^2$ tỉ lệ với $\delta_t(w)[\nabla_w\hat v(S_t,w)-\gamma\nabla_w\hat v(S_{t+1},w)]$. Cập nhật TD chỉ giữ số hạng thứ nhất và bỏ số hạng chứa gradient tại trạng thái kế, nên là bán gradient.
:::

<!-- note-topic-id: lec-07-topic-15 -->
## Chứng minh MC-SGD và vai trò Robbins–Monro

Vấn đề: chứng minh chính xác rằng một bước hạ gradient trên mất mát MC cục bộ cho ra công thức cập nhật đã nêu, và giải thích vì sao điều kiện Robbins–Monro phù hợp.

Chứng minh (bài tập 4). Cho $\hat v(s,w) = x(s)^\top w$ và mất mát $\ell_t(w) = \frac{1}{2}\big(G_t - x(S_t)^\top w\big)^2$. Đạo hàm theo $w$:

$$\nabla_w \ell_t(w) = \frac{1}{2} \cdot 2\big(G_t - x(S_t)^\top w\big) \cdot (-x(S_t)) = -\big(G_t - x(S_t)^\top w\big)x(S_t).$$

Một bước hạ gradient với bước $\alpha_t$:

$$w_{t+1} = w_t - \alpha_t \nabla_w \ell_t(w_t) = w_t + \alpha_t \big(G_t - x(S_t)^\top w_t\big)x(S_t),$$

đúng công thức yêu cầu. Vì $\ell_t$ là hàm bậc hai lồi theo $w$ (ma trận Hessian $x(S_t)x(S_t)^\top \succeq 0$), điều kiện để hội tụ về cực tiểu toàn cục là: dãy bước học thỏa Robbins–Monro $\sum_t \alpha_t = \infty$, $\sum_t \alpha_t^2 < \infty$; đặc trưng bị chặn; và dữ liệu có phân phối đủ để mất mát kỳ vọng có cực tiểu (ví dụ dữ liệu i.i.d. như phát biểu ở tr. 34).

Vai trò của Robbins–Monro (bài tập 6). Hai điều kiện $\sum_t \alpha_t = \infty$ và $\sum_t \alpha_t^2 < \infty$ phù hợp cho MC-SGD và TD-SGD vì: điều kiện thứ nhất bảo đảm tổng bước học đủ lớn để thuật toán còn tiếp tục học — nếu tổng hữu hạn thì $w$ dừng ở nơi chưa hội tụ; điều kiện thứ hai bảo đảm phương sai của nhiễu tích luỹ hữu hạn — tổng $\sum_t \alpha_t^2 \cdot \mathrm{Var}[\text{nhiễu}_t]$ hội tụ, nên nhiễu ngẫu nhiên không đẩy $w$ đi xa vĩnh viễn. Ví dụ $\alpha_t = 1/t$ thỏa cả hai; $\alpha_t = 1/\sqrt{t}$ thỏa điều kiện một nhưng không thỏa điều kiện hai.

::: exercise Câu hỏi kiểm tra
Tính Hessian của $\ell_t(w)$ và suy ra $\ell_t$ lồi; từ đó giải thích vì sao cực tiểu địa phương là cực tiểu toàn cục.
:::

::: hint
Tính đạo hàm bậc hai của $\frac{1}{2}(G_t - x^\top w)^2$ theo $w$.
:::

::: solution
$\nabla_w^2 \ell_t(w) = x(S_t)x(S_t)^\top$, là ma trận bán xác định dương vì $u^\top x(S_t)x(S_t)^\top u = (x(S_t)^\top u)^2 \ge 0$ với mọi $u$. Hàm lồi nên mọi cực tiểu địa phương là cực tiểu toàn cục; do đó hạ gradient với bước học thỏa Robbins–Monro và dữ liệu phù hợp hội tụ về cực tiểu toàn cục của lỗi bình phương trên phân phối dữ liệu.
:::

<!-- note-topic-id: lec-07-topic-07 -->
## TD(0) bán gradient

Vấn đề: TD(0) muốn cập nhật trực tuyến ngay sau mỗi bước chuyển, không chờ hết lượt; đích của nó là gì và cập nhật có tính chất gì?

Trực giác: thay vì chờ tổng thưởng đầy đủ, TD dùng ước lượng hiện tại của trạng thái kế làm một phần đích. Cách tự khởi tạo này giảm phương sai và cho phép cập nhật trực tuyến, nhưng đích bị chệch vì dựa trên $w_t$ chưa hội tụ.

Hình thức. Đích TD là $y_t^{\mathrm{TD}} = R_{t+1} + \gamma \hat v(S_{t+1}, w_t)$, và cập nhật tuyến tính là

$$w_{t+1} = w_t + \alpha_t \delta_t x(S_t), \qquad \delta_t = R_{t+1} + \gamma x(S_{t+1})^\top w_t - x(S_t)^\top w_t.$$

Đây là bán gradient: nó là gradient của $\frac{1}{2}\big(y_t^{\mathrm{TD}} - \hat v(S_t,w)\big)^2$ chỉ khi coi đích là hằng số, bỏ qua sự phụ thuộc của $y_t^{\mathrm{TD}}$ vào $w_t$. Vì vậy không thể phân tích nó như hồi quy SGD thông thường; cần công cụ khác — toán tử Bellman chiếu — ở chủ đề tiếp theo.

Ưu điểm: cập nhật trực tuyến, phương sai thấp hơn MC. Nhược điểm: đích tự khởi tạo bị chệch.

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
