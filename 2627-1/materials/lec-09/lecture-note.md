# Bài 09 — Double DQN và gradient chính sách

Trong chương này, chúng ta xét hai đại lượng mà một thuật toán học tăng cường ước lượng từ mẫu rồi dùng để cập nhật. Đại lượng thứ nhất là giá trị của hành động được chọn trong mục tiêu bootstrap của DQN (Bài 08). Khi các ước lượng không chệch nhưng có nhiễu, kỳ vọng của phép cực đại trên chúng không nhỏ hơn giá trị đúng lớn nhất, và việc tách chọn hành động khỏi đánh giá hành động, trong Double DQN và Double Q-learning, làm giảm độ chệch này. Đại lượng thứ hai là gradient của lợi tức kỳ vọng theo tham số của một chính sách được học trực tiếp: hàm điểm (score function) viết gradient đó thành một kỳ vọng theo các lượt, và thuật toán REINFORCE dùng một lượt làm mẫu của kỳ vọng này, nên, dưới giả thiết của định lý gradient chính sách (môi trường không phụ thuộc tham số, phần thưởng và độ dài lượt bị chặn), cho ước lượng không chệch của gradient chính sách.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Tính độ chệch của phép cực đại trên các ước lượng không chệch có nhiễu, và nêu khi nào hai vế của bất đẳng thức $\mathbb E[\max_a\widehat Q_a]\ge\max_a\mathbb E[\widehat Q_a]$ bằng nhau. Sản phẩm: $\mathbb E[\max_a\widehat Q_a]=1/2$ khi hai hành động có giá trị đúng bằng $0$ và nhiễu $\pm1$ độc lập.
2. Tính mục tiêu DQN, mục tiêu Double DQN và một cập nhật Double Q-learning trên cùng một mẫu chuyển; nêu vì sao mạng mục tiêu chỉ gần độc lập với mạng trực tuyến. Sản phẩm: hai mục tiêu $5{,}5$ và $4{,}6$ trên mẫu có $Q_{\theta^-}(s',\cdot)=(5;\,4)$, $Q_\theta(s',\cdot)=(3;\,6)$, và một ô của bảng Double Q-learning đổi từ $4$ thành $4{,}06$ trên cùng số liệu.
3. Chọn họ phân phối của chính sách theo miền hành động, softmax cho tập hữu hạn và Gaussian cho hành động thực; nêu một bài toán mà chính sách ngẫu nhiên tốt hơn mọi chính sách tất định khi đặc trưng gộp hai trạng thái. Sản phẩm: so sánh chính sách tất định với chính sách chọn hai hướng với xác suất $1/2$ ở hai ô có cùng đặc trưng.
4. Viết hàm mục tiêu $J(\theta)$ của một chính sách, ước lượng gradient của nó bằng sai phân hữu hạn, và tính hàm điểm của chính sách softmax và chính sách Gaussian. Sản phẩm: trên bài toán một bước hai hành động, $J=2$, sai phân hữu hạn cho $0{,}655$ so với giá trị đúng $2/3$, và hàm điểm $\psi_\theta(s,1)=(1/3;\,-1/3)$.
5. Phát biểu định lý gradient chính sách cùng các giả thiết của nó, và thực hiện một cập nhật REINFORCE trên một lượt. Sản phẩm: một cập nhật với lợi tức $3$ đưa xác suất của hành động 1 từ $2/3$ lên $0{,}710$.

<!-- note-topic-id: lec-09-topic-15 -->
## Kiến thức tiên quyết

Số hiệu `08.k` chỉ ghi chú Bài 08 và `03.k` chỉ ghi chú Bài 03; mỗi kết quả được phát biểu lại dưới đây ở dạng dùng được ngay.

- **Mục tiêu DQN và mạng mục tiêu** (Định nghĩa 08.3, 08.4, Thuật toán 08.13). DQN học một mạng giá trị hành động $Q_\theta(s,a)$ trên tập hành động hữu hạn $\mathcal A$. Mạng mục tiêu $Q_{\theta^-}$ có cùng kiến trúc; tham số $\theta^-$ không nhận gradient và được gán $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu, phép gán gọi là đồng bộ. Với mẫu chuyển $(S_i,A_i,R_i,S'_i,Z_i)$, mục tiêu (target) của DQN là
  $$y_i=R_i+\gamma(1-Z_i)\max_{a'\in\mathcal A}Q_{\theta^-}(S'_i,a'),$$
  trong đó cờ kết thúc $Z_i\in\{0,1\}$ bằng $1$ khi MDP kết thúc tại $S'_i$, và thừa số $(1-Z_i)$ là mặt nạ kết thúc.
- **Hàm mất mát và dừng gradient** (Định nghĩa 08.10, 08.12). Trên một mini-batch cỡ $b$, hàm mất mát là $L_B(\theta)=\frac1b\sum_{i=1}^b\bigl(\operatorname{sg}(y_i)-Q_\theta(S_i,A_i)\bigr)^2$. Phép dừng gradient (stop-gradient) $\operatorname{sg}$ giữ nguyên giá trị và cho đạo hàm bằng $0$, nên gradient chỉ đi qua dự đoán $Q_\theta(S_i,A_i)$ của hành động đã thực hiện.
- **Kết thúc và cắt ngắn** (Định nghĩa 08.6). Cờ cắt ngắn $U_i\in\{0,1\}$ bằng $1$ khi việc thu thập dừng vì một giới hạn nằm ngoài MDP, chẳng hạn giới hạn $500$ bước của CartPole. Mục tiêu chỉ dùng mặt nạ $(1-Z_i)$, nên một mẫu có $U_i=1$ và $Z_i=0$ vẫn giữ phần bootstrap.
- **Phạm vi bảo đảm của DQN** (Nhận xét 08.19, 08.21). Bộ nhớ phát lại giảm tương quan giữa các mẫu liền nhau, và mạng mục tiêu làm chậm sự thay đổi của mục tiêu. DQN vẫn có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, nên không có bảo đảm hội tụ tổng quát.
- **Hạ gradient** (Định nghĩa 08.16). Hạ gradient ngẫu nhiên cập nhật $\theta\leftarrow\theta-\eta\,g$ với $g$ là gradient của hàm mất mát trên một mini-batch và $\eta>0$. Khi cần cực đại hóa một hàm, ta đi theo chiều ngược lại, $\theta\leftarrow\theta+\alpha\,\widehat g$; dạng này xuất hiện ở Mục 5.
- **Chính sách, lợi tức và giá trị hành động** (Định nghĩa 03.8, 03.9, 03.13, 03.16). Chính sách $\pi$ gán cho mỗi trạng thái $s$ một phân phối $\pi(\cdot\mid s)$ trên $\mathcal A$; chính sách tất định là trường hợp dồn toàn bộ xác suất vào một hành động. Trong nhiệm vụ có kết thúc, lượt (episode) dừng tại bước ngẫu nhiên $T$, và lợi tức (return) từ bước $t$ là $G_t=\sum_{k=t}^{T-1}\gamma^{\,k-t}R_{k+1}$ với quy ước $G_T=0$; Bài 03 viết cùng tổng dưới dạng $\sum_{k=t+1}^{T}\gamma^{\,k-t-1}R_k$. Giá trị hành động $q_\pi(s,a)=\mathbb E_\pi[G_0\mid S_0=s,A_0=a]$ là lợi tức kỳ vọng khi thực hiện $a$ tại $s$ rồi theo $\pi$. Giá trị hành động tối ưu là $q_*(s,a)=\max_\pi q_\pi(s,a)$ (Định nghĩa 04.19); mục tiêu DQN là ước lượng mẫu của vế phải phương trình Bellman tối ưu cho $q_*$. Với chính sách Markov dừng, $\mathbb E_\pi[G_t\mid S_t=s,A_t=a]=q_\pi(s,a)$ ở mọi bước $t$ mà sự kiện $\{S_t=s,A_t=a\}$ có xác suất dương (Bổ đề 03.20(d)).
- **Chính sách tối ưu tất định** (Định lý 04.25). Trên một MDP hữu hạn có tính Markov, phần thưởng bị chặn và $0\le\gamma<1$, có một chính sách Markov dừng, tất định, tối ưu trên mọi chính sách (Bài 04 gọi là chính sách xác định); chính sách tham lam theo $q_*$ là một chính sách như vậy. Mục 4 dùng kết quả này để đối chiếu với trường hợp chính sách chỉ được phụ thuộc vào đặc trưng.
- **Bất đẳng thức Jensen** (kiến thức xác suất tiên quyết; ghi chú Bài 07 dùng dạng $(\sum_ip_iy_i)^2\le\sum_ip_iy_i^2$). Nếu $f:\mathbb R^m\to\mathbb R$ lồi và vector ngẫu nhiên $X$ có $\mathbb E\lVert X\rVert<\infty$, thì $f(\mathbb E[X])\le\mathbb E[f(X)]$. Ở Mục 2, bất đẳng thức này được áp dụng cho hàm lồi $f(x)=\max_ax_a$.
- **Kỳ vọng có điều kiện** (kiến thức xác suất tiên quyết; ghi chú Bài 07 nhắc tính chất tháp). $\mathbb E\bigl[\mathbb E[X\mid Y]\bigr]=\mathbb E[X]$, và nếu $W$ là một hàm của $Y$ thì $\mathbb E[WX\mid Y]=W\,\mathbb E[X\mid Y]$ khi các kỳ vọng tồn tại. Hai tính chất này được dùng ở Mục 6, với $Y$ là lịch sử của một lượt.

## Bảng ký hiệu

Bảng gồm ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một ví dụ được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương, trừ $\theta$, có hai vai được nêu ngay sau bảng.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $S_t$ | tập trạng thái; trạng thái ở bước $t$, trùng quan sát $O_t$ của Bài 08 | tập; phần tử của $\mathcal S$ |
| $\mathcal A$, $A_t$, $m$ | tập hành động; hành động ở bước $t$; số hành động khi $\mathcal A$ hữu hạn | hữu hạn ở Mục 2–3, hữu hạn hoặc $\mathbb R$ ở Mục 4–6; $m\in\mathbb N_+$ |
| $R_{t+1}$ | phần thưởng nhận sau $A_t$ | $\mathbb R$ |
| $\gamma$ | hệ số chiết khấu | $[0,1)$ |
| $T$ | bước kết thúc của lượt | biến ngẫu nhiên trên $\mathbb N_0$ |
| $\rho_0$, $P(s',r\mid s,a)$ | phân phối trạng thái đầu; hàm động lực của MDP | phân phối trên $\mathcal S$; phân phối của $(S_{t+1},R_{t+1})$ với mỗi $(s,a)$ |
| $G_t$ | lợi tức từ bước $t$ | biến ngẫu nhiên thực |
| $\pi(a\mid s)$, $\pi_\theta(a\mid s)$ | chính sách; chính sách có tham số $\theta$ | xác suất khi $\mathcal A$ hữu hạn, mật độ khi $\mathcal A=\mathbb R$ |
| $\mathbb E_\pi$ | kỳ vọng trên quỹ đạo sinh bởi $\rho_0$, $\pi$ và $P$ | toán tử |
| $q_\pi(s,a)$ | giá trị hành động đúng của $\pi$ | $\mathbb R$ |
| $q_*(s,a)$ | giá trị hành động tối ưu | $\mathbb R$ |
| $Z_i$, $U_i$ | cờ kết thúc của MDP; cờ cắt ngắn | $\{0,1\}$ |
| $(S_i,A_i,R_i,S'_i,Z_i,U_i)$, $b$ | mẫu chuyển thứ $i$ của mini-batch; cỡ mini-batch | bộ sáu thành phần; $\mathbb N_+$ |
| $\theta$, $d$ | tham số mạng trực tuyến (Mục 2–3) hoặc tham số chính sách (Mục 4–7); số chiều của $\theta$ | $\mathbb R^d$; $d\in\mathbb N_+$ |
| $\theta^-$, $C$ | tham số mạng mục tiêu; số bước tối ưu giữa hai lần đồng bộ | $\mathbb R^d$; $\mathbb N_+$ |
| $Q_\theta$, $Q_{\theta^-}$ | mạng trực tuyến; mạng mục tiêu | hàm thực trên $\mathcal S\times\mathcal A$ |
| $y_i$, $a_i^*$ | mục tiêu của mẫu $i$; hành động mạng trực tuyến chọn tại $S'_i$ | $\mathbb R$; $\mathcal A$ |
| $\operatorname{sg}$ | dừng gradient | toán tử trong đồ thị tính |
| $\widehat Q_a$ | ước lượng có nhiễu của giá trị hành động $a$ tại một trạng thái cố định | biến ngẫu nhiên thực |
| $q_a$, $\beta$ | giá trị đúng của hành động $a$ tại trạng thái đó; độ chệch của phép cực đại | $\mathbb R$ |
| $Q_1$, $Q_2$ | hai bảng của Double Q-learning | hàm thực trên $\mathcal S\times\mathcal A$ |
| $\widehat Q^A_a$, $\widehat Q^B_a$ | hai bản ước lượng của $q_a$: bản chọn, bản đánh giá | biến ngẫu nhiên thực |
| $\epsilon_{\mathrm{exp}}$ | xác suất thăm dò của hành vi $\epsilon_{\mathrm{exp}}$-tham lam | $[0,1]$ |
| $\alpha$ | bước học của Double Q-learning và của bước tăng gradient, cùng vai với tốc độ học $\eta$ của Bài 08 | $(0,\infty)$ |
| $\phi(s,a)$, $\phi(s)$ | đặc trưng của cặp trạng thái–hành động; đặc trưng của trạng thái | $\mathbb R^d$ |
| $\mu$, $\sigma^2$ | trung bình và phương sai của chính sách Gaussian | $\mathbb R$; $(0,\infty)$ |
| $J(\theta)$ | hàm mục tiêu: lợi tức kỳ vọng từ trạng thái đầu | $\mathbb R$ |
| $\psi_\theta(s,a)$, $\psi_t$ | hàm điểm $\nabla_\theta\log\pi_\theta(a\mid s)$; viết tắt của $\psi_\theta(S_t,A_t)$ | $\mathbb R^d$ |
| $\tau$, $p_\theta(\tau)$ | quỹ đạo $(S_0,A_0,R_1,\dots,S_T)$; xác suất hoặc mật độ của quỹ đạo dưới $\pi_\theta$ | dãy hữu hạn; $[0,\infty)$ |
| $H_t$ | lịch sử $(S_0,A_0,R_1,\dots,R_t,S_t)$ | dãy hữu hạn |
| $\widehat g$ | ước lượng REINFORCE của $\nabla_\theta J$ | $\mathbb R^d$ |
| $\nu^\pi_\gamma$ (viết gọn $\nu^\pi$) | phân bố chiếm dụng chiết khấu của trạng thái dưới $\pi$ | phân phối trên $\mathcal S$ |

Quy ước đọc. $R_{t+1}$ gắn với chuyển từ bước $t$ sang bước $t+1$. Sau bước kết thúc $T$, ta coi lượt đi vào một trạng thái hấp thụ có phần thưởng $0$, nên $G_T=0$ và mọi giá trị tại trạng thái kết thúc bằng $0$. Kỳ vọng $\mathbb E_\pi$ lấy theo $S_0\sim\rho_0$, $A_t\sim\pi(\cdot\mid S_t)$ và $(S_{t+1},R_{t+1})\sim P(\cdot\mid S_t,A_t)$. Trong mini-batch, chỉ số $i$ không mang thứ tự thời gian, nên mẫu viết $R_i$, $S'_i$ thay cho $R_{t+1}$, $S_{t+1}$. Chữ hoa $Q$ chỉ các ước lượng (mạng, bảng, $\widehat Q_a$), chữ thường $q_\pi$ chỉ giá trị đúng. Ký hiệu $\log$ chỉ logarit tự nhiên. Khi tọa độ của vector có dấu phẩy thập phân, các tọa độ được ngăn bằng dấu chấm phẩy, như $(1{,}5;\,3)$; ta dùng cùng cách viết cho mọi vector của chương.

Chữ $\theta$ có hai vai. Ở Mục 2–3, $\theta$ là tham số của mạng giá trị hành động như trong Bài 08; từ Mục 4, $\theta$ là tham số của chính sách như trong bài giảng gốc và trong Sutton và Barto (2018, Chương 13). Hai vai không xuất hiện trong cùng một công thức. Số liệu trong các ví dụ là số liệu sư phạm tự xây dựng, trừ các số đo lấy từ bài thực hành của Bài 08, có ghi rõ nguồn tại chỗ dùng.

Ứng với giáo trình *Học máy thống kê*: $q_\pi$ là $Q^\pi$. Phân phối đầu $\mu$ và hàm động lực $p(s',r\mid s,a)$ của Bài 03 được viết $\rho_0$ và $P(s',r\mid s,a)$ ở đây, để chữ $\mu$ dành cho trung bình của chính sách Gaussian và chữ $p$ cho xác suất $p_\theta(\tau)$ của một quỹ đạo. Phân bố chiếm dụng viết $\nu^\pi_\gamma$, không dùng $d$ (số chiều của $\theta$) hay $\mu$.

---

## Bản đồ chủ đề (bốn nhóm)

### Nhóm cầu nối

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-09-topic-15` | Kiến thức tiên quyết và ký hiệu | tr. 3–10 | Nhắc lại Bài 03, Bài 08, bất đẳng thức Jensen | Vào: Bài 03, Bài 08 → Ra: ký hiệu chung của chương | phần mở đầu |
| `lec-09-topic-16` | Mở đầu: mục tiêu, nội dung và bài toán trung tâm | tr. 1–2, 11, 22–25 | Bài toán trung tâm của chương | Vào: topic-15 → Ra: khung cho Mục 2–6 | 1 |
| `lec-09-topic-01` | Phép cực đại trong mục tiêu DQN | tr. 3–11 | Số đo đánh giá cao trên CartPole | Vào: topic-16 → Ra: nhu cầu đo độ chệch của phép cực đại | 2 |
| `lec-09-topic-14` | Ước lượng gradient bằng sai phân hữu hạn | tr. 33 | Bước vấn đề của hàm điểm | Vào: topic-07 → Ra: nhu cầu một ước lượng gradient từ lượt mẫu | 5 |

### Nhóm cốt lõi

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-09-topic-02` | Độ chệch của phép cực đại | tr. 12–13 | Ví dụ hai hành động có nhiễu $\pm1$; bất đẳng thức $\mathbb E[\max]\ge\max\mathbb E$ | Vào: topic-01 → Ra: nguyên nhân là cùng ước lượng chọn và đánh giá | 2 |
| `lec-09-topic-17` | Ước lượng kép | tr. 13–14, 21 | Ví dụ hai bản độc lập; mệnh đề ước lượng kép không chệch lên; chệch âm | Vào: topic-02 → Ra: nguyên tắc tách chọn và đánh giá | 3 |
| `lec-09-topic-03` | Mục tiêu Double DQN | tr. 14–16 | Chọn bằng mạng trực tuyến, đánh giá bằng mạng mục tiêu; thuật toán Double DQN | Vào: topic-17 → Ra: mục tiêu và thuật toán | 3 |
| `lec-09-topic-05` | Double Q-learning dạng bảng | tr. 20–21 | Hai bảng, cập nhật chéo; so sánh với Double DQN trên cùng số liệu | Vào: topic-03, topic-04 → Ra: hai cách tách và giới hạn chung của học giá trị | 3 |
| `lec-09-topic-06` | Chính sách tham số hóa | tr. 22–29 | Lưới gộp trạng thái; phân phối phân loại, softmax, Gaussian | Vào: topic-05 → Ra: $\pi_\theta(\cdot\mid s)$ rời rạc hoặc liên tục | 4 |
| `lec-09-topic-07` | Hàm mục tiêu và bước tăng gradient | tr. 30–32 | $J(\theta)$ và bước tăng gradient | Vào: topic-06 → Ra: bài toán tối ưu theo $\theta$ | 5 |
| `lec-09-topic-08` | Hàm điểm và hàm điểm của chính sách softmax | tr. 34–36 | Hàm điểm; công thức softmax; kỳ vọng bằng $0$ | Vào: topic-14 → Ra: hàm điểm rời rạc, $\mathbb E_{A\sim\pi}[\psi]=0$ | 5 |
| `lec-09-topic-09` | Hàm điểm của chính sách Gaussian | tr. 37–38 | $\psi=(a-\mu)\phi/\sigma^2$ với phương sai cố định | Vào: topic-08 → Ra: hàm điểm liên tục | 5 |
| `lec-09-topic-10` | Gradient của $J$ theo tỉ số xác suất | tr. 39 | Xác suất quỹ đạo, bỏ phần thưởng quá khứ | Vào: topic-08, topic-09 → Ra: $\nabla J$ dạng kỳ vọng theo quỹ đạo | 6 |
| `lec-09-topic-11` | Định lý gradient chính sách | tr. 39 | Dạng quỹ đạo và dạng phân bố chiếm dụng | Vào: topic-10 → Ra: kết quả mà REINFORCE lấy mẫu | 6 |
| `lec-09-topic-12` | REINFORCE | tr. 40 | Ví dụ một cập nhật, thuật toán đầy đủ | Vào: topic-11 → Ra: ước lượng không chệch của $\nabla J$ | 6 |

### Nhóm bổ sung

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-09-topic-04` | Phạm vi của Double DQN | tr. 17–19 | Hai mạng tương quan; những điều Double DQN không sửa | Vào: topic-03 → Ra: kết luận có điều kiện về tác dụng của Double DQN | 3 |

### Nhóm đọc thêm/thực hành

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-09-topic-13` | Tổng kết và chuyển tiếp: kết quả và giả thiết, so sánh phương pháp, tình huống áp dụng, câu hỏi tự kiểm tra, tóm tắt chương, bài tập | tr. 11–40 | Tổng kết; tình huống áp dụng gắn bài thực hành Bài 08 | Vào: topic-01 đến topic-12 → Ra: câu trả lời có điều kiện cho bài toán trung tâm; Bài 10 | 7 |

### Bảy phần của chương

Chúng ta đi qua bảy phần sau.

1. Mở đầu: kiến thức tiên quyết, ký hiệu, mục tiêu và bài toán trung tâm (`lec-09-topic-15`, `lec-09-topic-16`).
2. Độ chệch của phép cực đại: phép cực đại trong mục tiêu DQN, ví dụ hai hành động có nhiễu, bất đẳng thức kỳ vọng (`lec-09-topic-01`, `lec-09-topic-02`).
3. Tách chọn và đánh giá: hai bản ước lượng độc lập, mục tiêu và thuật toán Double DQN, phạm vi của Double DQN, Double Q-learning dạng bảng (`lec-09-topic-17`, `lec-09-topic-03`, `lec-09-topic-04`, `lec-09-topic-05`).
4. Chính sách tham số hóa: giới hạn của chính sách tham lam theo $Q$, phân phối phân loại, softmax và Gaussian (`lec-09-topic-06`).
5. Hàm mục tiêu và hàm điểm: hàm mục tiêu $J(\theta)$, sai phân hữu hạn, hàm điểm của softmax và Gaussian (`lec-09-topic-07`, `lec-09-topic-14`, `lec-09-topic-08`, `lec-09-topic-09`).
6. Gradient chính sách và REINFORCE: tỉ số xác suất, lợi tức từ thời điểm $t$, định lý gradient chính sách, thuật toán REINFORCE (`lec-09-topic-10`, `lec-09-topic-11`, `lec-09-topic-12`).
7. Tổng kết và chuyển tiếp: kết quả và giả thiết, so sánh phương pháp, tình huống áp dụng, bài tập (`lec-09-topic-13`).

Đọc trước: Sutton và Barto (2018), §6.7 (độ chệch của phép cực đại và học kép), §13.1–13.3 (chính sách tham số hóa, định lý gradient chính sách, REINFORCE) và §13.7 (chính sách cho hành động liên tục).

---

## 1. Mở đầu

<!-- note-topic-id: lec-09-topic-16 -->
### Bài toán trung tâm của chương

Bài 08 kết thúc với thuật toán DQN (Thuật toán 08.13). Mạng $Q_\theta$ được hồi quy về mục tiêu $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(S'_i,a')$, tính bằng một mạng mục tiêu giữ cố định giữa hai lần đồng bộ. Bộ nhớ phát lại và mạng mục tiêu xử lý hai nguồn bất ổn: tương quan giữa các mẫu và sự thay đổi của mục tiêu (Nhận xét 08.19). Một thành phần của mục tiêu chưa được xét. Phép cực đại $\max_{a'}Q_{\theta^-}(S'_i,a')$ dùng cùng một ước lượng để chọn hành động tốt nhất tại $S'_i$ và để báo giá trị của hành động đó.

Hậu quả của việc này đo được trong bài thực hành của Bài 08 (mục 7, DQN trên CartPole). Trong CartPole, mỗi bước giữ được cột cho phần thưởng $1$ và hệ số chiết khấu là $\gamma=0{,}99$. Lợi tức chiết khấu của mọi lượt vì vậy nhỏ hơn $\sum_{k\ge0}0{,}99^k=1/(1-0{,}99)=100$; với giới hạn $500$ bước, lợi tức lớn nhất là $(1-0{,}99^{500})/0{,}01\approx99{,}3$. Ở lần chạy khi soạn bài thực hành, mạng đã huấn luyện cho $\max_aQ_\theta(O_0,a)=108{,}5$ tại quan sát đầu của một lượt có lợi tức thực tế $G_0=99{,}3$. Giá trị $108{,}5$ vượt cận $100$, nên không là giá trị đúng của bất kỳ chính sách nào. Con số này chưa tách được phần đánh giá cao do phép cực đại với phần do các sai số xấp xỉ khác; trong Mục 2, chúng ta tách riêng phần thứ nhất trên một ví dụ tính tay.

Một giới hạn khác của cách học này dẫn tới nửa sau của chương. DQN chọn hành động bằng $\arg\max_aQ_\theta(s,a)$ trên một tập hữu hạn, nên chính sách thu được là tất định và mỗi bước cần một phép cực đại trên $\mathcal A$. Khi hành động là một số thực, chẳng hạn một góc lái, phép cực đại không còn là phép so sánh trên vài giá trị. Khi đặc trưng không phân biệt được hai trạng thái cần hai hành động khác nhau, bài giảng gốc (trang 23–25) đưa ra một lưới ô mà mọi chính sách tất định theo đặc trưng đó đều kém chính sách chọn ngẫu nhiên hai hướng, mỗi hướng với xác suất $1/2$. Cả hai trường hợp dẫn tới việc học trực tiếp một chính sách $\pi_\theta(a\mid s)$ có tham số $\theta$, và tăng hàm mục tiêu $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ bằng các bước gradient. Hàm $J$ chỉ quan sát được qua các lượt mẫu, nên gradient của nó cũng phải được ước lượng từ mẫu.

Hai nửa vì vậy có chung một câu hỏi: đại lượng được ước lượng từ mẫu để cập nhật có chệch hay không, và dưới giả thiết nào. Ở nửa đầu, đại lượng đó là giá trị của hành động được chọn tại trạng thái kế, nằm trong mục tiêu bootstrap. Ở nửa sau, đó là gradient $\nabla_\theta J(\theta)$. Hình dưới gồm hai chuỗi lập luận, mỗi chuỗi một hàng.

![Hai hàng, mỗi hàng ba khung nối bằng mũi tên. Hàng trên, giá trị trong mục tiêu bootstrap: mục tiêu DQN với max theo a phẩy của Q theta trừ tại S phẩy (Mục 2); cùng ước lượng chọn và đánh giá nên kỳ vọng của max lớn hơn hoặc bằng max của kỳ vọng (Mục 2); tách chọn và đánh giá bằng Double DQN và Double Q-learning (Mục 3). Hàng dưới, gradient của J theta: chính sách pi theta của a cho s với tập hành động hữu hạn hoặc liên tục (Mục 4); hàm điểm, gradient của pi theta bằng pi theta nhân gradient của log pi theta (Mục 5); REINFORCE, kỳ vọng của g mũ bằng gradient của J theta (Mục 6).](img/lec-09/central-problem.svg)

Hàng trên của hình đi theo mục tiêu bootstrap của DQN. Phép cực đại trong mục tiêu là nguồn của độ chệch (Mục 2), và hai thuật toán ở khung cuối thay một ước lượng bằng hai ước lượng (Mục 3). Hàng dưới đi theo chính sách tham số hóa. Đẳng thức trong khung giữa biến gradient của một xác suất thành tích của xác suất đó với gradient của log xác suất (Mục 5), và đẳng thức ở khung cuối nói rằng, dưới các giả thiết của Mục 6, ước lượng của REINFORCE có kỳ vọng bằng gradient đúng. Hai hàng dùng hai kiểu viền khác nhau, và mỗi khung ghi mục xử lý nó.

Chúng ta trả lời bài toán theo từng mục; mỗi câu trả lời dưới đây đúng dưới một điều kiện.

2. Nếu mỗi ước lượng $\widehat Q_a$ của giá trị đúng $q_a$ của hành động $a$ tại một trạng thái không chệch nhưng có nhiễu, thì $\mathbb E[\max_a\widehat Q_a]\ge\max_aq_a$, nên mục tiêu DQN có xu hướng đánh giá cao. Hai vế bằng nhau, chẳng hạn, khi một hành động luôn cho ước lượng lớn nhất.
3. Nếu hành động được chọn bằng một ước lượng và được đánh giá bằng một ước lượng không chệch, độc lập với ước lượng chọn, thì kỳ vọng của giá trị báo cáo không vượt giá trị đúng lớn nhất. Double Q-learning cập nhật hai bảng trên các mẫu khác nhau; vì mỗi bảng bootstrap từ bảng kia, tính độc lập chỉ đúng ở dạng lý tưởng. Double DQN chọn bằng mạng trực tuyến và đánh giá bằng mạng mục tiêu; vì $\theta^-$ là bản sao trễ của $\theta$, hai mạng tương quan, nên điều kiện chỉ thỏa gần đúng, và mức giảm độ chệch phải đo bằng thực nghiệm.
4. Nếu tập hành động liên tục, hoặc đặc trưng gộp những trạng thái cần hành động khác nhau, thì cần học trực tiếp chính sách $\pi_\theta(a\mid s)$. Softmax cho tập hành động hữu hạn và Gaussian cho hành động thực là hai họ phân phối của chương.
5. Nếu $\pi_\theta(a\mid s)>0$ và khả vi theo $\theta$, thì $\nabla_\theta\pi_\theta(a\mid s)=\pi_\theta(a\mid s)\,\psi_\theta(s,a)$ với hàm điểm $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$. Đẳng thức này biến một tổng theo hành động thành một trung bình theo hành động được lấy mẫu.
6. Nếu thêm $\rho_0$ và $P$ không phụ thuộc $\theta$, phần thưởng và độ dài lượt bị chặn, và được phép đổi thứ tự đạo hàm theo $\theta$ với tích phân theo quỹ đạo, thì
   $$\nabla_\theta J(\theta)=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^t\,G_t\,\psi_\theta(S_t,A_t)\Bigr].$$
   REINFORCE lấy một lượt làm mẫu của kỳ vọng này, nên ước lượng của nó không chệch.

   Một điều kiện đủ cụ thể cho phép đổi thứ tự: $\lvert R_{t+1}\rvert\le R_{\max}$, $T\le T_{\max}$, và đặc trưng bị chặn, $\lVert\phi\rVert\le\Phi$. Với chính sách softmax, hàm điểm $\phi(s,a)-\sum_b\pi_\theta(b\mid s)\phi(s,b)$ có chuẩn không quá $2\Phi$, nên mọi đại lượng trong tích phân bị chặn. Với chính sách Gaussian có $\sigma^2$ cố định, hàm điểm $(a-\mu)\phi(s)/\sigma^2$ không bị chặn theo $a$; khi $\theta$ chạy trong một lân cận bị chặn, trung bình $\mu=\phi(s)^\top\theta$ bị chặn, nên đạo hàm của mật độ theo $\theta$ bị trội bởi một đa thức của $a$ nhân một mật độ Gaussian, là hàm khả tích. Trong cả hai trường hợp, định lý hội tụ bị chặn cho phép đổi thứ tự; Mục 6 trình bày lập luận này.

Câu trả lời 3 cần bản đánh giá không chệch và độc lập với bản chọn; câu trả lời 6 cần môi trường không phụ thuộc tham số của chính sách, phần thưởng và độ dài lượt bị chặn, và phép đổi thứ tự đạo hàm với tích phân. Trong Mục 7, các giả thiết này được đặt cạnh từng kết quả trong một bảng. Ước lượng của REINFORCE không chệch nhưng có phương sai lớn; các cách giảm phương sai, như đường cơ sở (baseline) và ước lượng lợi thế, thuộc Bài 10.

Như vậy, chúng ta có một khung chung cho cả chương: ước lượng từ mẫu một đại lượng dùng để cập nhật, và xác định khi nào ước lượng đó không chệch. Khung này chưa giải thích vì sao phép cực đại lại chệch lên, và chệch bao nhiêu. Trong Mục 2, chúng ta trả lời câu hỏi đó trên một ví dụ hai hành động tính tay được, rồi phát biểu bất đẳng thức tổng quát.

---

## 2. Độ chệch của phép cực đại

Mục tiêu hồi quy của DQN (Định nghĩa 08.4) là $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(S'_i,a')$. Ở Mục 1, ta đã thấy rằng trên CartPole, mạng đã huấn luyện của bài thực hành Bài 08 báo một giá trị vượt cận trên của mọi lợi tức. Để biết phần nào của độ vượt đó do chính phép cực đại gây ra, chúng ta cần một ví dụ trong đó mọi nguồn sai số khác bị loại bỏ, và một phát biểu tổng quát về kỳ vọng của phép cực đại trên các ước lượng có nhiễu. Chúng ta xây dựng cả hai dưới đây.

<!-- note-topic-id: lec-09-topic-01 -->
### Phép cực đại trong mục tiêu DQN

Phép cực đại trong $y_i$ làm hai việc cùng lúc. Nó chọn hành động $a'$ có giá trị ước lượng lớn nhất tại trạng thái kế $S'_i$, và nó báo chính giá trị ước lượng đó làm phần bootstrap của mục tiêu. Cả hai việc dùng cùng một mạng $Q_{\theta^-}$. Bộ nhớ phát lại (Định nghĩa 08.7) thay đổi cách chọn mẫu chuyển vào mini-batch, còn mạng mục tiêu (Định nghĩa 08.3) thay đổi tham số dùng để tính phần bootstrap; phép cực đại trong $y_i$ giữ nguyên ở cả hai cơ chế.

Phép cực đại này đã có trong Q-learning dạng bảng của Bài 06. Dưới các giả thiết của Định lý 06.21 (MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$, mọi cặp được cập nhật vô hạn lần, bước học thỏa điều kiện Robbins–Monro theo cặp), $Q_t\to q_*$ hầu chắc chắn, nên sai số của các ước lượng, và cùng với nó độ chệch của phép cực đại, mất dần khi số bước tăng. Với số mẫu hữu hạn, các ước lượng còn sai số, và Sutton và Barto (2018, §6.7, Ví dụ 6.7) cho một MDP nhỏ trong đó Q-learning dạng bảng chọn sai hành động trong nhiều lượt đầu vì lý do này. Với mạng nơ-ron, không có định lý hội tụ tương ứng (Nhận xét 08.21), nên không có lý do để chờ sai số tự mất.

::: example Ví dụ 09.1 (Giá trị ước lượng trên CartPole)
**Dữ kiện.** CartPole: mỗi bước giữ được cột cho phần thưởng $1$; hệ số chiết khấu $\gamma=0{,}99$; lượt bị cắt ngắn ở bước $500$. Quan sát của môi trường được coi là trạng thái. Bài thực hành của Bài 08 (mục 7) huấn luyện DQN rồi in, cho lượt đầu của một hạt giống kiểm tra, giá trị $\max_aQ_\theta(S_0,a)=108{,}5$ và lợi tức thực tế $G_0=99{,}3$ ở lần chạy khi soạn.

**Cận trên của lợi tức.** Mọi phần thưởng bằng $1$, nên lợi tức của một lượt dài $n$ bước là $\sum_{k=0}^{n-1}0{,}99^k=(1-0{,}99^n)/0{,}01<100$. Không có giới hạn bước, giá trị của mọi chính sách vẫn không vượt $\sum_{k\ge0}0{,}99^k=100$. Với $n=500$, lợi tức là $(1-0{,}99^{500})/0{,}01\approx99{,}3$, khớp số in ra.

**So sánh.** $108{,}5-100=8{,}5>0$: giá trị mạng báo vượt cận trên của mọi lợi tức, nên không là giá trị đúng của bất kỳ chính sách nào.

**Kiểm tra lại.** $0{,}99^{500}=e^{500\log0{,}99}\approx e^{-5{,}025}\approx0{,}0066$, nên $(1-0{,}0066)/0{,}01\approx99{,}34$.
:::

![Trục số từ 90 đến 110. Đường nét đứt tại 100 ghi cận 1 chia 1 trừ gamma bằng 100, cận của mọi lợi tức và mọi giá trị đúng. Hình tròn tại 99,3 ghi lợi tức G 0 của một lượt cắt ở bước 500. Hình thoi tại 108,5 ghi max theo a của Q theta tại S 0. Ngoặc từ 100 đến 108,5 ghi vượt cận 8,5.](img/lec-09/cartpole-overestimate.svg)

Hình đặt ba số của Ví dụ 09.1 trên cùng một trục. Lợi tức thực tế nằm ngay dưới cận $100$, như một chính sách giữ cột đủ $500$ bước phải có; giá trị mạng báo nằm bên phải cận. Khoảng $8{,}5$ là phần đánh giá cao chắc chắn có, không phụ thuộc vào việc chính sách tốt đến đâu.

Ví dụ 09.1 chưa cho biết bao nhiêu trong $8{,}5$ do phép cực đại. Mạng còn sai số xấp xỉ, dữ liệu huấn luyện đổi theo chính sách hành vi, và số liệu chỉ đến từ một lần chạy. Một nhầm lẫn thường gặp là gán toàn bộ độ vượt cho phép cực đại; muốn tách phần đó, ta cần một tình huống trong đó các ước lượng không chệch và nguồn sai số duy nhất là nhiễu.

<!-- note-topic-id: lec-09-topic-02 -->
### Độ chệch của phép cực đại và bất đẳng thức kỳ vọng

Xét một trạng thái kế cố định với tập hành động hữu hạn $\mathcal A$. Gọi $q_a$ là giá trị đúng của hành động $a$ tại trạng thái này và $\widehat Q_a$ là ước lượng của nó, viết $\widehat Q_a=q_a+\varepsilon_a$ với nhiễu $\varepsilon_a$ có $\mathbb E[\varepsilon_a]=0$. Trong mục tiêu DQN, $\widehat Q_a$ đóng vai $Q_{\theta^-}(S'_i,a)$; nhiễu đến từ số mẫu hữu hạn và từ quá trình huấn luyện.

Một cách trực quan, phép cực đại chọn hành động có $\widehat Q_a$ lớn nhất, và ước lượng lớn nhất thường là ước lượng có nhiễu dương lớn. Vì cùng các $\widehat Q_a$ vừa quyết định hành động thắng $a^*$ vừa cho giá trị báo cáo $\widehat Q_{a^*}=q_{a^*}+\varepsilon_{a^*}$, nhiễu được chọn đi thẳng vào giá trị báo cáo. Hành động $a^*$ là biến ngẫu nhiên phụ thuộc chính các nhiễu, nên $\mathbb E[\varepsilon_{a^*}]$ nói chung khác $0$ dù mỗi $\mathbb E[\varepsilon_a]$ bằng $0$.

::: example Ví dụ 09.2 (Hai hành động có nhiễu ±1)
**Dữ kiện.** Hai hành động có giá trị đúng $q_1=q_2=0$. Nhiễu $\varepsilon_1$, $\varepsilon_2$ độc lập, mỗi biến bằng $-1$ hoặc $+1$ với xác suất $1/2$; vì giá trị đúng bằng $0$, $\widehat Q_a=\varepsilon_a$.

**Tính từng ước lượng.** $\mathbb E[\widehat Q_a]=\tfrac12(-1)+\tfrac12(+1)=0=q_a$ với $a=1,2$: cả hai ước lượng không chệch.

**Tính cực đại.** Bốn cặp $(\widehat Q_1;\widehat Q_2)$ đồng xác suất $1/4$:

| $(\widehat Q_1;\widehat Q_2)$ | $(-1;-1)$ | $(-1;+1)$ | $(+1;-1)$ | $(+1;+1)$ |
|---|---|---|---|---|
| $\max_a\widehat Q_a$ | $-1$ | $+1$ | $+1$ | $+1$ |

$$\mathbb E\bigl[\max_a\widehat Q_a\bigr]=\tfrac14(-1+1+1+1)=\tfrac12.$$

**Diễn giải.** $\max_aq_a=0$, nên phép cực đại báo trung bình cao hơn giá trị đúng lớn nhất $\tfrac12$ đơn vị.

**Kiểm tra lại.** Chỉ cặp $(-1;-1)$ cho cực đại nhỏ hơn giá trị đúng; ba cặp còn lại có ít nhất một nhiễu dương, và phép cực đại chọn đúng nhiễu đó.
:::

![Bốn khung, mỗi khung một cặp giá trị ước lượng của hành động 1 và 2 với xác suất một phần tư: âm một và âm một cho cực đại âm một, ba cặp còn lại cho cực đại cộng một; ba khung có cực đại dương viền đậm.](img/lec-09/maximization-bias.svg)

Hình liệt kê bốn hiện thực của Ví dụ 09.2. Ba khung viền đậm là ba hiện thực mà phép cực đại báo $+1$; khung còn lại cho thấy một hiện thực cụ thể vẫn có thể cho cực đại nhỏ hơn giá trị đúng. Kết luận của ví dụ là về kỳ vọng.

::: definition Định nghĩa 09.1 (Độ chệch của phép cực đại)
Cho tập hữu hạn $\mathcal A$, các số thực $q_a$ và các biến ngẫu nhiên khả tích $\widehat Q_a$, $a\in\mathcal A$. Ước lượng $\widehat Q_a$ không chệch nếu $\mathbb E[\widehat Q_a]=q_a$. Độ chệch của phép cực đại (maximization bias) là
$$
\beta=\mathbb E\Bigl[\max_{a\in\mathcal A}\widehat Q_a\Bigr]-\max_{a\in\mathcal A}q_a.
$$
:::

Định nghĩa so kỳ vọng của giá trị mà phép cực đại báo với giá trị đúng lớn nhất, tức đúng đại lượng phần bootstrap của mục tiêu DQN muốn ước lượng tại một trạng thái kế. Trong Ví dụ 09.2, $\beta=\tfrac12$. Độ chệch được định nghĩa cho một trạng thái cố định; trong mục tiêu DQN, trạng thái kế $S'_i$ thay đổi theo mẫu, và $\beta$ là độ chệch có điều kiện khi biết $S'_i$.

Khái niệm này khác độ chệch của từng ước lượng. "Mỗi $\widehat Q_a$ không chệch" là điều kiện trên từng hành động riêng lẻ; $\beta$ đo một hàm phi tuyến của cả vector ước lượng. Ví dụ 09.2 cho thấy điều kiện thứ nhất không kéo theo $\beta=0$. Mệnh đề sau cho biết chiều của $\beta$ trong mọi trường hợp.

::: proposition Mệnh đề 09.2 (Độ chệch của phép cực đại không âm)
**Giả thiết.** $\mathcal A$ hữu hạn; các $\widehat Q_a$, $a\in\mathcal A$, là biến ngẫu nhiên khả tích trên cùng một không gian xác suất.

**Kết luận.** (a) $\mathbb E[\max_a\widehat Q_a]\ge\max_a\mathbb E[\widehat Q_a]$. (b) Nếu mọi $\widehat Q_a$ không chệch cho $q_a$ thì $\beta\ge0$. (c) Gọi $b^*$ là một hành động có $\mathbb E[\widehat Q_{b^*}]=\max_a\mathbb E[\widehat Q_a]$; dấu bằng ở (a) xảy ra khi và chỉ khi $\max_a\widehat Q_a=\widehat Q_{b^*}$ hầu chắc chắn. Khi các ước lượng không chệch, $b^*$ là một phần tử bất kỳ của $\arg\max_aq_a$. Khi có nhiều hành động đạt $\max_a\mathbb E[\widehat Q_a]$, điều kiện không phụ thuộc cách chọn $b^*$, và $\widehat Q_{b^*}$ bằng cực đại kể cả khi hòa.

**Điều kiện áp dụng.** Không cần các nhiễu độc lập hay cùng phân phối, và không cần phân phối cụ thể của nhiễu.

**Phạm vi.** Kết luận nói về kỳ vọng tại một trạng thái kế cố định. Mệnh đề không cho độ lớn của $\beta$, không nói từng hiện thực của cực đại đều lớn hơn $\max_aq_a$, và không mô tả độ chệch tích lũy thế nào qua các bước bootstrap.
:::

::: proof
**Bước 1 (kết luận a).** Hàm $f:\mathbb R^m\to\mathbb R$, $f(x)=\max_ax_a$, là cực đại của các hàm tuyến tính $x\mapsto x_a$, nên lồi. Vector $X=(\widehat Q_a)_{a\in\mathcal A}$ khả tích vì từng thành phần khả tích. Bất đẳng thức Jensen (Kiến thức tiên quyết) cho
$$
\begin{aligned}
\max_a\mathbb E[\widehat Q_a]&=f(\mathbb E[X])\\
&\le\mathbb E[f(X)]\\
&=\mathbb E\bigl[\max_a\widehat Q_a\bigr].
\end{aligned}
$$
Dòng đầu là định nghĩa của $f$, dòng thứ hai là bất đẳng thức Jensen. Cách khác, không dùng Jensen: với mọi $b$, $\max_a\widehat Q_a\ge\widehat Q_b$; lấy kỳ vọng được $\mathbb E[\max_a\widehat Q_a]\ge\mathbb E[\widehat Q_b]$, rồi lấy cực đại theo $b$.

**Bước 2 (kết luận b).** Khi $\mathbb E[\widehat Q_a]=q_a$ với mọi $a$, vế phải của (a) bằng $\max_aq_a$; trừ hai vế cho $\max_aq_a$ được $\beta\ge0$.

**Bước 3 (kết luận c).** Đặt $D=\max_a\widehat Q_a-\widehat Q_{b^*}$. Ta có $D\ge0$ và $\mathbb E[D]=\mathbb E[\max_a\widehat Q_a]-\max_a\mathbb E[\widehat Q_a]$. Một biến ngẫu nhiên không âm có kỳ vọng $0$ khi và chỉ khi nó bằng $0$ hầu chắc chắn, nên dấu bằng ở (a) xảy ra khi và chỉ khi $D=0$ hầu chắc chắn. $\square$
:::

Mệnh đề 09.2 nói rằng phép cực đại trên các ước lượng không chệch không bao giờ đánh giá thấp theo kỳ vọng, và đánh giá cao nghiêm ngặt khi và chỉ khi không có $b^*\in\arg\max_aq_a$ nào thỏa $\widehat Q_{b^*}=\max_a\widehat Q_a$ hầu chắc chắn. Hai giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ khả tích: nếu $\widehat Q_1$ có phân phối Cauchy chuẩn, $\mathbb E[\widehat Q_1]$ không tồn tại, nên vế phải của (a) không xác định.
- Bỏ không chệch ở (b): nếu $\widehat Q_a=q_a-1$ tất định với mọi $a$, thì $\beta=-1<0$. Kết luận (a) vẫn đúng, nhưng vế phải không còn là giá trị đúng lớn nhất.

Giả thiết khả tích được dùng ở Bước 1 để Jensen áp dụng được; giả thiết không chệch chỉ được dùng ở Bước 2. Điều kiện ở (c) giải thích Ví dụ 09.2: cả hai hành động thuộc $\arg\max_aq_a$, nhưng ở cặp $(-1;+1)$ hành động 1 không đạt cực đại và ở cặp $(+1;-1)$ hành động 2 không đạt cực đại, nên $\beta>0$.

::: example Ví dụ 09.3 (Khoảng cách giữa các giá trị đúng)
**Dữ kiện.** Như Ví dụ 09.2: hai hành động, nhiễu $\varepsilon_1$, $\varepsilon_2$ độc lập, mỗi biến bằng $\pm1$ với xác suất $1/2$, $\widehat Q_a=q_a+\varepsilon_a$. Xét hai trường hợp giá trị đúng: (i) $q=(0{,}5;\,0)$; (ii) $q=(3;\,0)$.

**Trường hợp (i).** $\widehat Q_1\in\{-0{,}5;\,1{,}5\}$, $\widehat Q_2\in\{-1;\,1\}$. Bốn cặp cho cực đại $-0{,}5$; $1$; $1{,}5$; $1{,}5$, nên $\mathbb E[\max_a\widehat Q_a]=\tfrac14(-0{,}5+1+1{,}5+1{,}5)=0{,}875$ và $\beta=0{,}875-0{,}5=0{,}375$.

**Trường hợp (ii).** $\widehat Q_1\in\{2;\,4\}$ luôn lớn hơn $\widehat Q_2\in\{-1;\,1\}$, nên $\max_a\widehat Q_a=\widehat Q_1$ ở mọi cặp, $\mathbb E[\max_a\widehat Q_a]=3$ và $\beta=0$.

**Diễn giải.** Khi khoảng cách giữa hai giá trị đúng tăng từ $0$ lên $0{,}5$ rồi $3$, độ chệch giảm từ $0{,}5$ xuống $0{,}375$ rồi $0$. Trường hợp (ii) thỏa điều kiện dấu bằng của Mệnh đề 09.2(c) với $b^*=1\in\arg\max_aq_a$: $\widehat Q_1=\max_a\widehat Q_a$ ở mọi hiện thực.

**Kiểm tra lại.** Trường hợp (i): $\tfrac14\cdot3{,}5=0{,}875$.
:::

Ví dụ 09.3 cho thấy độ chệch lớn nhất khi các hành động có giá trị đúng gần nhau so với độ lớn của nhiễu.

::: remark Nhận xét 09.3 (Nhầm lẫn thường gặp về độ chệch của phép cực đại)
1. "Mỗi lần lấy cực đại đều đánh giá cao." Sai: trong Ví dụ 09.2, cặp $(-1;-1)$ cho cực đại $-1<0$. Mệnh đề 09.2 nói về kỳ vọng.
2. "Ước lượng không chệch cho từng hành động thì cực đại cũng không chệch." Sai: Ví dụ 09.2 có $\beta=\tfrac12$.
3. "Độ chệch luôn dương nghiêm ngặt." Sai: Ví dụ 09.3(ii) có $\beta=0$; dấu lớn hơn nghiêm ngặt xảy ra khi và chỉ khi không có $b^*\in\arg\max_aq_a$ nào thỏa $\widehat Q_{b^*}=\max_a\widehat Q_a$ hầu chắc chắn.
4. "Bộ nhớ phát lại hoặc mạng mục tiêu loại bỏ độ chệch này." Sai: cả hai cơ chế giữ nguyên phép cực đại trên cùng một mạng trong $y_i$.
:::

**Trong thực hành.** Trong DQN, $\widehat Q_a$ là $Q_{\theta^-}(S'_i,a)$, các giá trị đúng là $q_*(S'_i,a)$, và nhiễu là sai số của mạng mục tiêu sau một số bước huấn luyện hữu hạn. Giả thiết không chệch thường không thỏa, và các sai số của các hành động không độc lập vì dùng chung tham số; kết luận (a) của Mệnh đề 09.2 vẫn đúng vì không cần hai điều này, nhưng so sánh với $\max_aq_*(S'_i,a)$ cần thêm giả thiết. Bài giảng gốc (trang 12) nêu rằng độ chệch này lặp lại qua các bước bootstrap; chúng ta không chứng minh mức tích lũy. Số đo của Ví dụ 09.1 phù hợp với kết luận này nhưng không chứng minh nó, vì chỉ có một lần chạy và nhiều nguồn sai số. Phần gợi mở của bài thực hành Bài 08 đo lại cùng đại lượng với mục tiêu của Double DQN.

Như vậy, Định nghĩa 09.1 đặt tên cho đại lượng mà Ví dụ 09.1 gợi ra, và Mệnh đề 09.2 chứng minh rằng với các ước lượng không chệch, đại lượng đó không âm, và dương nghiêm ngặt khi và chỉ khi không có $b^*\in\arg\max_aq_a$ nào thỏa $\widehat Q_{b^*}=\max_a\widehat Q_a$ hầu chắc chắn; Ví dụ 09.2 và 09.3 cho các giá trị $\tfrac12$, $0{,}375$ và $0$. Trong chứng minh, cùng một vector $X$ xác định cả hành động thắng lẫn giá trị $\max_aX_a$; khi số mẫu hữu hạn và nhiễu khác $0$, độ chệch nói chung còn dương. Trong Mục 3, chúng ta giữ phép chọn nhưng đánh giá hành động được chọn bằng một ước lượng khác, rồi xét khi nào cách này bỏ được độ chệch lên.

*Nguồn: bài giảng gốc lecture09-ddqn-and-policy-gradient-part1.pdf (2025–2026), trang 3–13; Sutton và Barto (2018), §6.7; bài thực hành Bài 08, mục 7.*

---

## 3. Tách chọn và đánh giá

Mệnh đề 09.2 cho biết phép cực đại trên các ước lượng không chệch có độ chệch không âm, và chứng minh của nó chỉ ra nguyên nhân: cùng một vector ước lượng vừa quyết định hành động thắng vừa cho giá trị báo cáo. Trong Ví dụ 09.2, nguyên nhân đó làm giá trị báo cáo trung bình cao hơn giá trị đúng $\tfrac12$ đơn vị. Để bỏ được độ chệch lên, chúng ta cần tách hai vai: chọn hành động bằng một ước lượng, đánh giá hành động đó bằng một ước lượng khác. Chúng ta xét khi nào cách tách đó loại được độ chệch lên, rồi xây hai thuật toán dùng nó: Double DQN cho mạng và Double Q-learning cho bảng.

<!-- note-topic-id: lec-09-topic-17 -->
### Ước lượng kép

Một cách trực quan, nếu hành động thắng được chọn bằng một bản ước lượng, thì nhiễu của bản đó quyết định hành động nào thắng nhưng không đi vào giá trị báo cáo. Nếu giá trị được đọc từ một bản thứ hai có nhiễu độc lập với bản thứ nhất, thì nhiễu của bản thứ hai không "biết" hành động nào đã thắng, nên trung bình của nó bằng $0$.

::: example Ví dụ 09.4 (Hai bản ước lượng độc lập)
**Dữ kiện.** Hai hành động có giá trị đúng $q_1=q_2=0$. Hai bản ước lượng $\widehat Q^A_a=q_a+\varepsilon^A_a$ và $\widehat Q^B_a=q_a+\varepsilon^B_a$, $a=1,2$; bốn nhiễu $\varepsilon^A_1$, $\varepsilon^A_2$, $\varepsilon^B_1$, $\varepsilon^B_2$ độc lập, mỗi nhiễu bằng $-1$ hoặc $+1$ với xác suất $1/2$. Hành động được chọn là $a^*=\arg\max_a\widehat Q^A_a$, hòa thì chọn hành động 1; giá trị báo cáo là $\widehat Q^B_{a^*}$.

**Chọn.** Bốn cặp $(\widehat Q^A_1;\widehat Q^A_2)$ đồng xác suất $1/4$: $(-1;-1)\to a^*=1$; $(-1;+1)\to a^*=2$; $(+1;-1)\to a^*=1$; $(+1;+1)\to a^*=1$.

**Đánh giá.** Trong mỗi cặp, $a^*$ đã xác định và bản B độc lập với bản A, nên $\mathbb E[\widehat Q^B_{a^*}\mid\widehat Q^A]=q_{a^*}+\mathbb E[\varepsilon^B_b]\big|_{b=a^*}=0$. Lấy trung bình theo bốn cặp: $\mathbb E[\widehat Q^B_{a^*}]=0$.

**Diễn giải.** $\max_aq_a=0$, nên giá trị báo cáo không chệch. Dùng một bản cho cả hai việc, Ví dụ 09.2 cho $\tfrac12$.

**Kiểm tra lại.** Quy tắc phá hòa không đổi kết quả: với mỗi hành động $b$, $\mathbb E[\varepsilon^B_b]=0$.
:::

![Dòng trên ghi cặp bản A, mỗi cặp xác suất một phần tư, hòa thì chọn hành động 1. Bốn khung: âm một âm một chọn a sao bằng 1; âm một cộng một chọn 2; cộng một âm một chọn 1; cộng một cộng một chọn 1; ở mọi khung, kỳ vọng của bản B tại a sao khi biết cặp bản A bằng 0.](img/lec-09/double-estimator.svg)

Hình liệt kê bốn hiện thực của bản A trong Ví dụ 09.4. Hành động được chọn thay đổi giữa các khung, như trong Ví dụ 09.2, nhưng ở mọi khung, kỳ vọng có điều kiện của giá trị báo cáo khi biết cặp bản A bằng $0$, vì giá trị đó được đọc từ bản B. Ví dụ dùng hai điều: bản B không chệch, và bản B độc lập với bản A. Mệnh đề sau cho thấy hai điều đó đủ cho mọi phân phối nhiễu.

::: proposition Mệnh đề 09.4 (Ước lượng kép không chệch lên)
**Giả thiết.** $\mathcal A$ hữu hạn; $\widehat Q^A=(\widehat Q^A_a)_{a\in\mathcal A}$ và $\widehat Q^B=(\widehat Q^B_a)_{a\in\mathcal A}$ là hai vector ngẫu nhiên độc lập; mỗi $\widehat Q^B_a$ khả tích và không chệch, $\mathbb E[\widehat Q^B_a]=q_a$. Hành động $a^*$ là một hàm của $\widehat Q^A$, chẳng hạn $a^*\in\arg\max_a\widehat Q^A_a$ với một quy tắc phá hòa cố định.

**Kết luận.** $\mathbb E[\widehat Q^B_{a^*}]=\mathbb E[q_{a^*}]\le\max_aq_a$. Ước lượng kép $\widehat Q^B_{a^*}$ không chệch cho giá trị đúng của hành động được chọn, và độ chệch so với $\max_aq_a$ không dương.

**Điều kiện áp dụng.** Không cần $\widehat Q^A$ không chệch; không cần các thành phần của mỗi vector độc lập với nhau.

**Phạm vi.** Dấu bằng chỉ xảy ra khi $a^*\in\arg\max_aq_a$ hầu chắc chắn; khi bản A chọn sai với xác suất dương, ước lượng kép chệch âm. Mệnh đề không nói về phương sai của ước lượng.
:::

::: proof
**Bước 1 (điều kiện theo bản A).** Vì $a^*$ là hàm của $\widehat Q^A$ và $\widehat Q^B$ độc lập với $\widehat Q^A$, với mỗi giá trị $b$ của $a^*$ ta có $\mathbb E[\widehat Q^B_{a^*}\mid\widehat Q^A]=\mathbb E[\widehat Q^B_b]\big|_{b=a^*}=q_{a^*}$.

**Bước 2 (lấy kỳ vọng).** Theo tính chất tháp của kỳ vọng có điều kiện (Kiến thức tiên quyết),
$$
\begin{aligned}
\mathbb E[\widehat Q^B_{a^*}]&=\mathbb E\bigl[\mathbb E[\widehat Q^B_{a^*}\mid\widehat Q^A]\bigr]\\
&=\mathbb E[q_{a^*}]\\
&\le\max_aq_a.
\end{aligned}
$$
Dòng đầu là tính chất tháp, dòng thứ hai là Bước 1, dòng cuối dùng $q_{a^*}\le\max_aq_a$ ở mọi hiện thực.

**Bước 3 (dấu bằng).** $\max_aq_a-q_{a^*}\ge0$ có kỳ vọng $0$ khi và chỉ khi nó bằng $0$ hầu chắc chắn, tức $a^*\in\arg\max_aq_a$ hầu chắc chắn. $\square$
:::

Mệnh đề 09.4 đổi chiều kết luận của Mệnh đề 09.2: một bản ước lượng cho cả hai việc thì chệch lên hoặc bằng, hai bản độc lập thì chệch xuống hoặc bằng. Ba giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ độc lập: lấy $\widehat Q^B=\widehat Q^A$. Khi đó ước lượng kép trở về phép cực đại của Ví dụ 09.2, với độ chệch $\tfrac12>0$.
- Bỏ không chệch của bản B: nếu $\widehat Q^B_a=q_a+1$ tất định, giá trị báo cáo bằng $q_{a^*}+1$, có thể vượt $\max_aq_a$.
- Bỏ "$a^*$ là hàm của $\widehat Q^A$": nếu $a^*=\arg\max_a\widehat Q^B_a$, ta lại có phép cực đại trên bản B.

Bước 1 dùng độc lập, không chệch và khả tích của bản B; Bước 2 dùng tính chất tháp.

::: example Ví dụ 09.5 (Ước lượng kép có thể chệch âm)
**Dữ kiện.** Như Ví dụ 09.4 nhưng giá trị đúng $q=(0{,}5;\,0)$: $\widehat Q^A_1\in\{-0{,}5;\,1{,}5\}$, $\widehat Q^A_2\in\{-1;\,1\}$, bốn nhiễu $\pm1$ độc lập, xác suất $1/2$.

**Chọn.** Bốn cặp của bản A: $(-0{,}5;-1)\to1$; $(-0{,}5;1)\to2$; $(1{,}5;-1)\to1$; $(1{,}5;1)\to1$. Vậy $\Pr(a^*=1)=\tfrac34$.

**Đánh giá.** Theo Mệnh đề 09.4, $\mathbb E[\widehat Q^B_{a^*}]=\tfrac34\cdot0{,}5+\tfrac14\cdot0=0{,}375$.

**So sánh.** $\max_aq_a=0{,}5$: ước lượng kép chệch $-0{,}125$. Một bản ước lượng (Ví dụ 09.3(i)) cho $0{,}875$, chệch $+0{,}375$.

**Kiểm tra lại.** $0{,}375-0{,}5=-0{,}125$; độ lớn của độ chệch âm nhỏ hơn độ chệch dương của một bản trong ví dụ này, nhưng Mệnh đề 09.4 không khẳng định điều đó trong mọi trường hợp.
:::

Câu hỏi thảo luận của bài giảng gốc (trang 21) về bốn hay tám ước lượng không trả lời được bằng tên gọi: như Ví dụ 09.5 cho thấy, độ chệch của mỗi cách tách phụ thuộc cách chọn, quan hệ giữa các bản và số mẫu mỗi bản nhận, nên phải được phân tích riêng.

<!-- note-topic-id: lec-09-topic-03 -->
### Mục tiêu và thuật toán Double DQN

Mục tiêu DQN $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(S'_i,a')$ dùng mạng mục tiêu $Q_{\theta^-}$ cả để chọn lẫn để đánh giá hành động tại $S'_i$: đúng tình huống "một bản" của Mệnh đề 09.2. Thay vì huấn luyện thêm một mạng, van Hasselt, Guez và Silver (2016) dùng lại hai mạng mà DQN đã có. Mạng trực tuyến $Q_\theta$ đóng vai bản A, mạng mục tiêu $Q_{\theta^-}$ đóng vai bản B.

::: example Ví dụ 09.6 (Một mẫu chuyển, hai mục tiêu)
**Dữ kiện.** $R=1$, $\gamma=0{,}9$, $Z=0$; tại trạng thái kế $S'$ có hai hành động, $Q_{\theta^-}(S',\cdot)=(5;\,4)$ và $Q_\theta(S',\cdot)=(3;\,6)$.

**Mục tiêu DQN.** $\max_aQ_{\theta^-}(S',a)=5$, nên $y=1+0{,}9\cdot5=5{,}5$.

**Mục tiêu Double DQN.** Mạng trực tuyến chọn $a^*=\arg\max_aQ_\theta(S',a)=2$; mạng mục tiêu đánh giá $Q_{\theta^-}(S',2)=4$; $y=1+0{,}9\cdot4=4{,}6$.

**Diễn giải.** Hai mạng xếp hạng hai hành động ngược nhau, và mục tiêu giảm $0{,}9$.

**Kiểm tra lại.** Bài thực hành của Bài 08 (mục 15.2) kiểm hai số $5{,}5$ và $4{,}6$ bằng phép kiểm tự động, và kiểm rằng với $Z=1$ mục tiêu Double DQN bằng $R=1$.
:::

![Bảng hai hàng, hai cột hành động. Hàng trên, mạng mục tiêu: 5 và 4. Hàng dưới, mạng trực tuyến: 3 và 6. Hình thoi cạnh số 5: DQN lấy cực đại của hàng trên. Khung vuông quanh số 6: Double DQN chọn hành động 2. Mũi tên ghi đánh giá đi từ số 6 tới số 4 có viền ellip nét đứt.](img/lec-09/ddqn-example.svg)

Hình đặt hai mạng trên cùng một bảng. DQN chỉ đọc hàng trên; Double DQN chọn cột ở hàng dưới rồi đọc giá trị của cột đó ở hàng trên. Vì giá trị ở hàng trên tại một cột bất kỳ không vượt cực đại của hàng đó, $Q_{\theta^-}(S',a^*)\le\max_aQ_{\theta^-}(S',a)$ ở mọi mẫu, nên với $Z=0$ luôn có $y^{\mathrm{DDQN}}\le y^{\mathrm{DQN}}$, dấu bằng khi hai mạng chọn cùng hành động. Bất đẳng thức này nói về hai mục tiêu, không nói mục tiêu nào gần giá trị đúng hơn trong một mẫu cụ thể.

::: algorithm Thuật toán 09.5 (Double DQN)
**Đầu vào.** Như Thuật toán 08.13: $\gamma\in[0,1)$; xác suất thăm dò $\epsilon_{\mathrm{exp}}\in[0,1]$; một bộ tối ưu theo gradient; ngân sách $t_{\mathrm{end}}$ bước môi trường; dung lượng $N$ của bộ nhớ phát lại $\mathcal D$, cỡ mini-batch $b$, số mẫu tối thiểu $N_{\mathrm{start}}$, số bước môi trường $F$ giữa hai bước tối ưu, số bước tối ưu $C$ giữa hai lần đồng bộ, với $b\le N_{\mathrm{start}}\le N$.

**Đầu ra.** Tham số $\theta$ và chính sách tham lam theo $Q_\theta$.

**Khởi tạo.** $\theta$ ngẫu nhiên; $\theta^-\leftarrow\theta$; $\mathcal D\leftarrow\varnothing$; $t\leftarrow0$; $k_{\mathrm{opt}}\leftarrow0$.

**Lặp** khi $t<t_{\mathrm{end}}$:

1. Chọn $A_t$ theo quy tắc $\epsilon_{\mathrm{exp}}$-tham lam từ $Q_\theta(S_t,\cdot)$; thực hiện, nhận $R_{t+1}$, $S_{t+1}$, $Z_{t+1}$, $U_{t+1}$; lưu mẫu chuyển vào $\mathcal D$; đặt lại môi trường khi $Z_{t+1}\lor U_{t+1}=1$; $t\leftarrow t+1$.
2. Nếu $\lvert\mathcal D\rvert\ge N_{\mathrm{start}}$ và $t\bmod F=0$: rút đều mini-batch $\{(S_i,A_i,R_i,S'_i,Z_i,U_i)\}_{i=1}^b$ từ $\mathcal D$ và làm bước 3–5.
3. Không lấy gradient: $a_i^*=\arg\max_aQ_\theta(S'_i,a)$ và $y_i=R_i+\gamma(1-Z_i)\,Q_{\theta^-}(S'_i,a_i^*)$.
4. Một bước của bộ tối ưu trên $L_B(\theta)=\frac1b\sum_{i=1}^b\bigl(\operatorname{sg}(y_i)-Q_\theta(S_i,A_i)\bigr)^2$; $k_{\mathrm{opt}}\leftarrow k_{\mathrm{opt}}+1$.
5. Nếu $k_{\mathrm{opt}}\bmod C=0$: $\theta^-\leftarrow\theta$.

**Kích thước.** Ở bước 3, $Q_\theta(S'_\cdot,\cdot)$ và $Q_{\theta^-}(S'_\cdot,\cdot)$ là các mảng $b\times m$; $a^*\in\mathcal A^b$, $y\in\mathbb R^b$, $Z\in\{0,1\}^b$.

**Chi phí mỗi bước tối ưu.** Ba lần tính của mạng trên mini-batch (mạng trực tuyến trên $S_i$ và $S'_i$, mạng mục tiêu trên $S'_i$), so với hai lần của DQN.
:::

Thuật toán 09.5 khác Thuật toán 08.13 đúng ở bước 3. Thuật toán 08.13 viết ngân sách là $T$; ở đây viết $t_{\mathrm{end}}$ vì $T$ đã dành cho bước kết thúc lượt. Phép arg max là hàm hằng từng khúc theo $\theta$, nên không có gradient đi qua $a_i^*$, và $\operatorname{sg}$ giữ $y_i$ là hằng như trong DQN. Khi $Z_i=1$, giá trị tại $S'_i$ không vào mục tiêu; dạng từng trường hợp "$y_i=R_i$ khi $Z_i=1$, $y_i=R_i+\gamma Q_{\theta^-}(S'_i,a_i^*)$ khi $Z_i=0$" cho cùng giá trị, và cài đặt theo mini-batch có thể tính $a_i^*$ cho mọi mẫu rồi nhân mặt nạ. Mẫu bị cắt ngắn ($U_i=1$, $Z_i=0$) vẫn giữ phần bootstrap.

**Trong thực hành.** Trong bài thực hành của Bài 08, hàm `dqn_loss_double` (mục 14) và tùy chọn `double` (mục 15) cài đúng bước 3: tính `argmax` của mạng trực tuyến trên $S'_i$, rồi lấy giá trị của mạng mục tiêu tại chỉ số đó, cả hai trong khối không lấy gradient. Mạng trực tuyến chỉ là bản A gần đúng của Mệnh đề 09.4: nó không độc lập với mạng mục tiêu. Chúng ta xét hệ quả của điều này dưới đây.

<!-- note-topic-id: lec-09-topic-04 -->
### Phạm vi của Double DQN

Mệnh đề 09.4 cần bản đánh giá độc lập với bản chọn. Trong Double DQN, $\theta^-$ là bản sao của $\theta$ tại mốc đồng bộ gần nhất, và cả hai được huấn luyện trên cùng một bộ nhớ phát lại; sai số của hai mạng vì vậy tương quan. Giả thiết độc lập không thỏa, nên Mệnh đề 09.4 không áp dụng, và không có bảo đảm rằng Double DQN hết chệch lên.

::: remark Nhận xét 09.6 (Điều Double DQN thay đổi và không thay đổi)
1. Double DQN chỉ đổi công thức mục tiêu. Tương quan giữa các mẫu, sự thay đổi của mục tiêu tại mốc đồng bộ và việc thiếu bảo đảm hội tụ tổng quát (Nhận xét 08.21) vẫn như DQN; bài giảng gốc (trang 18) liệt kê các điều này.
2. Ngay sau mốc đồng bộ, $\theta^-=\theta$ và mục tiêu Double DQN trùng mục tiêu DQN. Hai mạng khác nhau nhiều hơn khi số bước tối ưu từ mốc đồng bộ tăng.
3. Bài giảng gốc (trang 17) nêu các tác động mong đợi: giảm đánh giá cao, giá trị ổn định hơn, thứ hạng hành động đáng tin hơn. Đây là các quan sát thực nghiệm của van Hasselt, Guez và Silver (2016) trên trò chơi Atari, không phải hệ quả của một định lý.
4. Bộ ước lượng kép có thể chệch âm (Ví dụ 09.5), nên giảm đánh giá cao không đồng nghĩa với ước lượng đúng.
:::

**Trong thực hành.** Mức giảm độ chệch và tác động lên chính sách phải đo bằng thực nghiệm. Bài thực hành của Bài 08 (mục 15.4) so Double DQN với cấu hình gốc trên Lunar Lander, năm hạt giống, $10^5$ bước môi trường: Double DQN đạt trung bình $200{,}0$, cấu hình gốc đạt $205{,}4$ trên cùng năm hạt giống, hiệu ghép cặp $-5{,}4$ với $t=-0{,}38$, chưa phân biệt được ở mức $5\%$. Số liệu này không cho thấy Double DQN tốt hơn trên bài toán đó với ngân sách đó; nó cũng không mâu thuẫn với Mệnh đề 09.2, vì tổng thưởng của chính sách cuối là một đại lượng khác độ chệch của mục tiêu.

<!-- note-topic-id: lec-09-topic-05 -->
### Double Q-learning dạng bảng

Double DQN dùng một bản sao trễ làm bản đánh giá. Với biểu diễn bảng, ta có thể giữ hai bảng $Q_1$, $Q_2$ học trên hai tập mẫu khác nhau, gần hơn với tình huống của Mệnh đề 09.4. Đây là Double Q-learning (van Hasselt, 2010); bài thực hành Flappy Bird của Bài 07 (mục 13) đã cài một phiên bản với hàm giá trị tuyến tính.

::: example Ví dụ 09.7 (Một cập nhật Double Q-learning)
**Dữ kiện.** $R=1$, $\gamma=0{,}9$, $Z=0$, bước học $\alpha=0{,}1$; ô cần cập nhật có $Q_1(S,A)=4$; tại $S'$, $Q_1(S',\cdot)=(3;\,6)$ và $Q_2(S',\cdot)=(5;\,4)$; đồng xu chọn cập nhật $Q_1$.

**Chọn.** $a^*=\arg\max_aQ_1(S',a)=2$.

**Mục tiêu.** $y_1=R+\gamma Q_2(S',a^*)=1+0{,}9\cdot4=4{,}6$.

**Sai số và giá trị mới.** $y_1-Q_1(S,A)=4{,}6-4=0{,}6$; $Q_1(S,A)\leftarrow4+0{,}1\cdot0{,}6=4{,}06$. Bảng $Q_2$ không đổi.

**Diễn giải.** Đây là số liệu của Ví dụ 09.6 với $Q_1$ ở vai $Q_\theta$ và $Q_2$ ở vai $Q_{\theta^-}$; mục tiêu bằng mục tiêu Double DQN $4{,}6$. Hai thuật toán khác nhau ở bước sau: Double Q-learning đổi đúng một ô của một bảng, còn Double DQN đổi tham số dùng chung của mạng trực tuyến.

**Kiểm tra lại.** $4{,}06$ nằm giữa giá trị cũ $4$ và mục tiêu $4{,}6$.
:::

![Bảng hai hàng: hàng trên Q 2 tại S phẩy bằng 5 và 4, bảng đánh giá; hàng dưới Q 1 tại S phẩy bằng 3 và 6, bảng chọn và được cập nhật. Khung vuông quanh số 6: Q 1 chọn hành động 2. Mũi tên ghi đánh giá đi lên số 4 có viền ellip nét đứt: Q 2 đánh giá hành động 2 bằng 4.](img/lec-09/double-q-example.svg)

Hình dùng cùng bố cục với hình của Ví dụ 09.6: hàng trên đánh giá, hàng dưới chọn, mũi tên đi từ hàng dưới lên hàng trên. Ở đây hàng chọn là bảng được cập nhật, ở vị trí của mạng trực tuyến trong Ví dụ 09.6.

::: algorithm Thuật toán 09.7 (Double Q-learning)
**Đầu vào.** MDP hữu hạn với $\mathcal A$ hữu hạn; bước học $\alpha\in(0,1]$; $\gamma\in[0,1)$; xác suất thăm dò $\epsilon_{\mathrm{exp}}$; số lượt.

**Đầu ra.** Hai bảng $Q_1$, $Q_2$ và chính sách tham lam theo $Q_1+Q_2$.

**Khởi tạo.** $Q_1(s,a)$, $Q_2(s,a)$ tùy ý với mọi $s$, $a$; $Q_1(s,\cdot)=Q_2(s,\cdot)=0$ tại trạng thái kết thúc.

**Lặp** cho mỗi lượt: khởi tạo $S$; lặp cho mỗi bước của lượt:

1. Chọn $A$ theo quy tắc $\epsilon_{\mathrm{exp}}$-tham lam từ $Q_1(S,\cdot)+Q_2(S,\cdot)$; thực hiện $A$, nhận $R$, $S'$ và cờ kết thúc $Z$.
2. Với xác suất $1/2$: $a^*=\arg\max_aQ_1(S',a)$ và $Q_1(S,A)\leftarrow Q_1(S,A)+\alpha\bigl[R+\gamma(1-Z)\,Q_2(S',a^*)-Q_1(S,A)\bigr]$.
3. Ngược lại: $a^*=\arg\max_aQ_2(S',a)$ và $Q_2(S,A)\leftarrow Q_2(S,A)+\alpha\bigl[R+\gamma(1-Z)\,Q_1(S',a^*)-Q_2(S,A)\bigr]$.
4. $S\leftarrow S'$; kết thúc lượt khi $Z=1$.

**Chi phí mỗi bước.** Hai phép cực đại trên $\mathcal A$ (một cho hành vi, một cho mục tiêu) và một cập nhật một ô; bộ nhớ gấp đôi Q-learning.
:::

Thuật toán 09.7 khác Q-learning (Bài 06) ở bước 2–3: mục tiêu đọc giá trị của bảng kia tại hành động do bảng được cập nhật chọn. Mỗi mẫu chuyển chỉ đi vào một bảng, nên hai bảng ước lượng từ hai tập mẫu khác nhau. Hai bảng vẫn không độc lập hoàn toàn: mỗi bảng bootstrap từ bảng kia, và hành vi dùng tổng hai bảng. Giả thiết của Mệnh đề 09.4 vì vậy chỉ thỏa ở dạng lý tưởng. Van Hasselt (2010) chứng minh Double Q-learning hội tụ tới $q_*$ dưới các giả thiết tương tự Định lý 06.21; chúng ta không trình bày chứng minh đó.

| | DQN | Double DQN | Double Q-learning |
|---|---|---|---|
| chọn $a^*$ tại $S'$ | $Q_{\theta^-}$ | $Q_\theta$ | bảng được cập nhật |
| đánh giá $a^*$ | $Q_{\theta^-}$ | $Q_{\theta^-}$ | bảng còn lại |
| quan hệ hai ước lượng | cùng một ước lượng | bản sao trễ, tương quan | mẫu khác nhau, bootstrap từ nhau |
| dữ liệu cập nhật | mini-batch từ bộ nhớ phát lại | mini-batch từ bộ nhớ phát lại | từng mẫu chuyển |
| độ chệch của mục tiêu | $\ge0$ (Mệnh đề 09.2) | không bảo đảm hết chệch lên; phải đo | $\le0$ nếu bản đánh giá không chệch, độc lập (Mệnh đề 09.4); độc lập chỉ thỏa lý tưởng |

Bảng đặt ba phương pháp cạnh nhau theo cùng tiêu chí. Hai hàng đầu cho thấy chỉ cặp ước lượng chọn và đánh giá thay đổi; hàng thứ ba quyết định hàng cuối qua Mệnh đề 09.2 và 09.4.

::: remark Nhận xét 09.8 (Nhầm lẫn thường gặp về tách chọn và đánh giá)
1. "Double DQN không chệch." Sai: mạng mục tiêu tương quan với mạng trực tuyến, nên Mệnh đề 09.4 không áp dụng.
2. "Ước lượng kép luôn tốt hơn một bản." Không có bảo đảm như vậy: Ví dụ 09.5 cho độ chệch $-0{,}125$, và mỗi bảng của Double Q-learning chỉ nhận khoảng một nửa số mẫu.
3. "Double Q-learning lấy cực đại của bảng kia." Sai: bảng kia chỉ đánh giá hành động do bảng được cập nhật chọn; lấy $\max_aQ_2(S',a)$ trả lại phép cực đại của một bản.
4. "Mỗi bước Double Q-learning cập nhật cả hai bảng." Sai: đúng một ô của một bảng đổi.
:::

Như vậy, Mệnh đề 09.4 chứng minh rằng chọn bằng một bản và đánh giá bằng một bản độc lập, không chệch thì không còn chệch lên, với cái giá có thể chệch âm (Ví dụ 09.5). Thuật toán 09.5 áp nguyên tắc này vào DQN bằng cách thay một dòng mục tiêu, và Thuật toán 09.7 áp nó vào bảng bằng hai bảng cập nhật chéo; trên cùng số liệu, hai thuật toán cho cùng mục tiêu $4{,}6$ (Ví dụ 09.6, 09.7). Cả hai chỉ thỏa giả thiết độc lập gần đúng, nên tác dụng của chúng phải đo. Cả ba phương pháp của mục này, DQN, Double DQN và Double Q-learning, còn chung một giới hạn: chính sách được suy ra bằng $\arg\max_aQ(s,a)$, nên xác suất chọn hành động không được học. Chính sách tham lam là tất định, và hành vi $\epsilon_{\mathrm{exp}}$-tham lam chỉ thêm một mức ngẫu nhiên cố định; mỗi bước còn cần một phép cực đại trên tập hành động hữu hạn. Trong Mục 4, chúng ta xét hai tình huống mà giới hạn này trở thành trở ngại, hành động liên tục và đặc trưng gộp trạng thái, rồi học trực tiếp một phân phối hành động.

*Nguồn: bài giảng gốc lecture09-ddqn-and-policy-gradient-part1.pdf (2025–2026), trang 13–21; van Hasselt (2010); van Hasselt, Guez và Silver (2016); Sutton và Barto (2018), §6.7; bài thực hành Bài 08, mục 14–15.*

---

## 4. Chính sách tham số hóa

Mục 3 kết thúc ở một giới hạn chung của DQN, Double DQN và Double Q-learning: hành động được chọn bằng $\arg\max_aQ(s,a)$, nên xác suất chọn hành động không được học, và mỗi bước cần một phép cực đại trên $\mathcal A$. Chính sách tham lam là tất định; hành vi $\epsilon_{\mathrm{exp}}$-tham lam chỉ thêm một mức ngẫu nhiên cố định. Giới hạn này có hại không, khi Định lý 04.25 đã bảo đảm một chính sách tối ưu tất định? Chúng ta trả lời bằng hai tình huống: một lưới mà đặc trưng gộp hai trạng thái cần hai hành động khác nhau, và hành động là một số thực. Cả hai dẫn tới việc học trực tiếp một phân phối hành động có tham số.

<!-- note-topic-id: lec-09-topic-06 -->
### Giới hạn của chính sách tham lam theo $Q$

Bài giảng gốc (trang 23–25) dùng một lưới nhỏ. Hàng trên có năm ô, đánh số 1 đến 5 từ trái sang phải; hàng dưới có ô X dưới ô 1 và ô 5, ô đích dưới ô 3. Tác tử ở hàng trên chọn Đông, Tây hoặc Nam; mỗi bước đi một ô, gặp tường thì đứng yên. Đi Nam từ ô 3 vào ô đích và kết thúc lượt; đi Nam từ ô 1 hoặc ô 5 vào ô X, một ô kẹt mà từ đó không bao giờ tới đích; đi Nam từ ô 2, ô 4 thì đứng yên. Tác tử quan sát đặc trưng $x(s)$ có bốn giá trị: ô 1, ô 3, ô 5 mỗi ô một giá trị riêng, còn hai ô xám 2 và 4 cùng một giá trị, ký hiệu $x=\mathrm g$. Từ ô 2, hướng tốt là Đông; từ ô 4, hướng tốt là Tây.

Hai điểm của mô hình này là giả thiết thêm vào nguồn, ghi là sai khác có chủ ý. Nguồn (trang 23) viết đặc trưng $x(s,a)=1$ nếu $s$ là ô xám và $0$ ở nơi khác; đặc trưng đó gộp luôn ba ô trắng, nên lớp chính sách tất định theo đặc trưng còn hẹp hơn, và chính sách "ô 1 Đông, ô 3 Nam, ô 5 Tây" dùng dưới đây không thuộc lớp đó. Chúng ta dùng đặc trưng chỉ gộp hai ô xám, để giữ đúng kết luận của nguồn (trang 24–25) mà không thêm chỗ gộp khác. Nguồn cũng không nói hai ô trống dưới ô xám là tường hay ô đi vào được, và không cho phần thưởng; mô hình chuyển, ô kẹt X và các số bước dưới đây là phần bổ sung.

![Lưới hai hàng năm cột. Hàng trên ô 1 đến ô 5, ô 2 và ô 4 màu xám có cùng đặc trưng x bằng g, ba ô trắng có đặc trưng riêng; mỗi bước đi một ô, gặp tường thì đứng yên. Hàng dưới: ô kẹt X dưới ô 1 và ô 5, ô đích dưới ô 3. Mũi tên: ô 1 sang Đông, ô 3 xuống ô đích, ô 5 sang Tây, và chính sách tất định đi Đông ở cả hai ô xám; ô 4 và ô 5 nối bằng đường nét đứt ghi kẹt.](img/lec-09/aliased-grid-policy.svg)

::: example Ví dụ 09.8 (Lưới gộp trạng thái, chính sách tất định)
**Dữ kiện.** Lưới năm ô như trên; mọi chính sách theo đặc trưng chọn cùng một phân phối hành động ở ô 2 và ô 4, và có thể chọn khác nhau ở ô 1, 3, 5. Đại lượng cần tính là số bước $h_i$ từ ô $i$ tới ô đích; $h_i=\infty$ nếu không bao giờ tới.

**Tất định, Đông ở hai ô xám.** Ô 3 đi Nam: $h_3=1$. Ô 2 đi Đông tới ô 3: $h_2=2$; ô 1 đi Đông: $h_1=3$. Từ ô 4, Đông đưa tới ô 5; ô 5 hoặc đi Tây trở lại ô 4, lặp mãi, hoặc đi Nam vào X, hoặc đứng yên. Trong cả ba trường hợp $h_4=h_5=\infty$. Chọn Nam ở hai ô xám thì đứng yên ở đó, còn tệ hơn.

**Tất định, Tây ở hai ô xám.** Đối xứng: $h_4=2$, $h_5=3$, còn $h_1=h_2=\infty$.

**Diễn giải.** Mọi chính sách tất định theo đặc trưng có hai ô xuất phát không bao giờ tới đích. Một hàm giá trị hành động $Q_\theta(s,a)$ chỉ phụ thuộc $s$ qua $x(s)$ cho cùng thứ hạng hành động ở hai ô xám, nên phép tham lam theo nó rơi vào một trong hai trường hợp trên (bài giảng gốc, trang 24).

**Kiểm tra lại.** Với chính sách phân biệt được ô (Đông ở ô 2, Tây ở ô 4), $h_2=h_4=2$ và $h_1=h_5=3$: lưới là một MDP hữu hạn quan sát đầy đủ, và có chính sách tất định tốt.
:::

Một cách trực quan, khi hai ô không phân biệt được cần hai hướng ngược nhau, chọn ngẫu nhiên giữa hai hướng ở cả hai ô cho mỗi ô một xác suất dương đi đúng hướng. Chính sách ngẫu nhiên không biết mình đang ở ô nào; nó chỉ tránh việc kẹt vĩnh viễn ở một ô.

![Cùng lưới năm ô, ô kẹt X dưới ô 1 và ô 5, ô đích dưới ô 3. Ở ô 2 và ô 4 có hai mũi tên Đông và Tây, mỗi mũi tên xác suất một phần hai; ô 1 sang Đông, ô 3 xuống ô đích, ô 5 sang Tây. Hàng dưới lưới ghi h i, số bước kỳ vọng tới đích từ từng ô: 5, 4, 1, 4, 5.](img/lec-09/aliased-grid-stochastic.svg)

::: example Ví dụ 09.9 (Lưới gộp trạng thái, chính sách ngẫu nhiên)
**Dữ kiện.** Lưới như Ví dụ 09.8. Ở hai ô xám, chính sách đi Đông với xác suất $p$ và Tây với xác suất $1-p$; ô 1 đi Đông, ô 3 đi Nam, ô 5 đi Tây (bài giảng gốc, trang 25, xét $p=\tfrac12$).

**Phương trình từ ô 2.** Với xác suất $p$, đi Đông tới ô 3 rồi xuống đích: hai bước. Với xác suất $1-p$, đi Tây tới ô 1 rồi Đông trở lại ô 2: hai bước, rồi còn $h_2$ bước. Vậy
$$
h_2=p\cdot2+(1-p)(2+h_2)\quad\Longrightarrow\quad h_2=\frac2p.
$$

**Từ ô 4.** Đối xứng, đi Đông là hướng sai: $h_4=\dfrac{2}{1-p}$.

**Chọn $p$.** Trung bình của hai ô xám là $\tfrac12\bigl(\tfrac2p+\tfrac2{1-p}\bigr)=\dfrac{1}{p(1-p)}$, nhỏ nhất khi $p(1-p)$ lớn nhất, tức $p=\tfrac12$. Khi đó $h_2=h_4=4$, $h_1=h_5=5$.

**Diễn giải.** Tiêu chí so sánh là trung bình trên ô xuất phát. Với ô xuất phát đều trên năm ô, chính sách ngẫu nhiên cho trung bình $(5+4+1+4+5)/5=3{,}8$ bước, trong khi mọi chính sách tất định theo đặc trưng có hai ô không bao giờ tới (Ví dụ 09.8). Từ riêng ô 2, chính sách tất định Đông chỉ cần $2$ bước, nên chính sách ngẫu nhiên không tốt hơn ở mọi ô. So với chính sách phân biệt được ô ($h_2=h_4=2$), chính sách ngẫu nhiên vẫn tốn gấp đôi số bước từ ô xám.

**Theo lợi tức chiết khấu.** Gán phần thưởng $-1$ cho mỗi bước chưa tới đích (kể cả bước đi vào đích) và giữ tác tử ở ô X mãi với phần thưởng $-1$ mỗi bước. Với $V_3=-1$ và $V_1=-1+\gamma V_2$, ta có $V_2=-1+\gamma\bigl[pV_3+(1-p)V_1\bigr]$, nên
$$
V_2=-\frac{1+\gamma}{1-(1-p)\gamma^2},\qquad V_4=-\frac{1+\gamma}{1-p\gamma^2}.
$$
Mỗi số hạng $1/(1-c)$ lồi theo $p$, và tổng đối xứng qua $p=\tfrac12$, nên $V_2+V_4$ lớn nhất tại $p=\tfrac12$; với $\gamma=0{,}9$, $V_2=V_4=-1{,}9/0{,}595\approx-3{,}19$, còn chính sách tất định Đông cho $V_4=-1/(1-\gamma)=-10$. Kết luận trùng với kết luận theo số bước.

**Kiểm tra lại.** Với $p=\tfrac12$: $h_2=\tfrac12\cdot2+\tfrac12(2+4)=1+3=4$.
:::

Hai ví dụ cần được đặt cạnh kết quả của Bài 04.

::: remark Nhận xét 09.9 (Chính sách tối ưu tất định và lớp chính sách bị gộp)
Định lý 04.25 nói: trên một MDP hữu hạn có tính Markov, phần thưởng bị chặn và $0\le\gamma<1$, có một chính sách Markov dừng, tất định, tối ưu trên mọi chính sách. Lưới của Ví dụ 09.8, với phần thưởng $-1$ ở mỗi bước chưa tới đích, ô X là ô kẹt (ở lại mãi với phần thưởng $-1$ mỗi bước) và $\gamma<1$, thỏa các giả thiết này khi chính sách được phép phụ thuộc vào ô; khi đó lợi tức giảm theo số bước, và chính sách "Đông ở ô 2, Tây ở ô 4" (cùng ô 1 Đông, ô 3 Nam, ô 5 Tây) là tối ưu, với $V_2=V_4=-(1+\gamma)$. Khi chính sách chỉ được phụ thuộc $x(s)$, lớp chính sách cho phép nhỏ hơn: định lý không nói gì về cực đại trên lớp này, và Ví dụ 09.9 cho thấy cực đại đó có thể đạt tại một chính sách ngẫu nhiên. Hai kết luận không mâu thuẫn: một nói về toàn bộ chính sách Markov, một nói về chính sách bị ràng buộc bởi đặc trưng.
:::

Lý do thứ hai không cần gộp trạng thái. Khi hành động là một số thực, chẳng hạn góc lái của một xe trong một khoảng, chính sách tham lam $\arg\max_aQ(s,a)$ đòi giải một bài toán tối ưu liên tục ở mỗi bước; nếu $Q$ là một mạng nơ-ron, bài toán đó nói chung không lồi. Rời rạc hóa góc lái thành vài giá trị đưa bài toán về trường hợp hữu hạn, đổi lại độ phân giải của hành động.

### Chính sách tham số hóa

Cả hai tình huống dẫn tới cùng một cách làm: thay vì học $Q$ rồi suy ra chính sách bằng phép cực đại, chúng ta tham số hóa trực tiếp phân phối hành động và học tham số của nó (bài giảng gốc, trang 26).

::: definition Định nghĩa 09.10 (Chính sách tham số hóa)
Cho $\theta\in\mathbb R^d$. Một chính sách tham số hóa (parameterized policy) là một họ $\{\pi_\theta\}$, trong đó với mỗi $s\in\mathcal S$, $\pi_\theta(\cdot\mid s)$ là một phân phối trên $\mathcal A$: hàm xác suất khi $\mathcal A$ hữu hạn, hàm mật độ khi $\mathcal A\subseteq\mathbb R$; và với mỗi $s$, $a$, ánh xạ $\theta\mapsto\pi_\theta(a\mid s)$ khả vi.
:::

Định nghĩa có hai vai. Để điều khiển, tác tử lấy mẫu $A_t\sim\pi_\theta(\cdot\mid S_t)$ rồi gửi $A_t$ cho môi trường. Để học, chúng ta chỉnh $\theta$ sao cho hành động dẫn tới lợi tức cao có xác suất lớn hơn; cách chỉnh là nội dung của Mục 5 và Mục 6. Chính sách tham số hóa là một chính sách Markov dừng theo nghĩa của Định nghĩa 03.13, với thêm một tham số khả vi. Chính sách tất định là trường hợp giới hạn khi phân phối dồn về một hành động; định nghĩa không loại nó, nhưng khi đó $\pi_\theta$ thường không khả vi theo $\theta$ nữa.

Từ mục này, $\theta$ là tham số của chính sách. Ở Mục 2 và 3, cùng chữ đó là tham số của mạng giá trị hành động; hai vai không xuất hiện trong cùng một công thức. Với hành động liên tục, $\pi_\theta(a\mid s)$ là mật độ, có thể lớn hơn $1$; chỉ tích phân của nó trên một khoảng mới là xác suất.

::: example Ví dụ 09.10 (Phân phối trên bốn hành động)
**Dữ kiện.** Bốn hành động $1,2,3,4$ tại một trạng thái $s$ (bài giảng gốc, trang 27–28).

**Phân phối đều.** $\pi(a\mid s)=\tfrac14$ với mọi $a$. Phân phối này không phụ thuộc trạng thái và không có tham số, nên không có gì để học.

**Phân phối phân loại.** $\pi(\cdot\mid s)=(0{,}1;\,0{,}2;\,0{,}2;\,0{,}5)$: hành động 4 được chọn một nửa số lần. Phân phối này đạt được bằng chính sách softmax, định nghĩa ngay sau đây (Định nghĩa 09.11), với đặc trưng $\phi(s,a)$ là vector đơn vị thứ $a$ trong $\mathbb R^4$ và $\theta=(\log0{,}1;\,\log0{,}2;\,\log0{,}2;\,\log0{,}5)$, vì khi đó $e^{\phi(s,a)^\top\theta}=\pi(a\mid s)$ và tổng mẫu số bằng $1$.

**Kiểm tra lại.** $0{,}1+0{,}2+0{,}2+0{,}5=1$.
:::

![Bên trái: cột xác suất 0,1; 0,2; 0,2; 0,5 cho bốn hành động. Bên phải: mật độ Gaussian theo hành động thực a quanh trung bình mu, hai đường a min và a max đánh dấu miền bị chặn, hai đuôi ngoài miền tô màu.](img/lec-09/policy-distributions.svg)

Hình đặt hai họ phân phối cạnh nhau. Bên trái, mỗi hành động có một cột xác suất, tổng các cột bằng $1$. Bên phải, mật độ Gaussian dương trên toàn trục số thực; phần tô màu là khối xác suất rơi ngoài miền hành động hợp lệ.

::: definition Định nghĩa 09.11 (Chính sách softmax)
Cho $\mathcal A$ hữu hạn, đặc trưng $\phi(s,a)\in\mathbb R^d$ giữ cố định và $\theta\in\mathbb R^d$. Chính sách softmax là
$$
\pi_\theta(a\mid s)=\frac{\exp\bigl(\phi(s,a)^\top\theta\bigr)}{\sum_{b\in\mathcal A}\exp\bigl(\phi(s,b)^\top\theta\bigr)}.
$$
:::

Số $\phi(s,a)^\top\theta$ là mức ưu tiên của hành động $a$ tại $s$; chính sách softmax đổi các mức ưu tiên thành xác suất bằng hàm mũ rồi chuẩn hóa. Mọi hành động có xác suất dương, và cộng cùng một hằng vào mọi mức ưu tiên không đổi chính sách. Với hai hành động, $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ và $\theta=(\log2;\,0)$, ta được $\pi_\theta(1\mid s)=\tfrac{2}{2+1}=\tfrac23$ và $\pi_\theta(2\mid s)=\tfrac13$; bộ số này là bài toán một bước hai hành động dùng ở Mục 5 và 6. Bài giảng gốc (trang 29) dùng đặc trưng là khoảng cách tới vật cản. So với phép tham lam theo $Q$, softmax biểu diễn được các xác suất dương bất kỳ khi đặc trưng đủ phong phú; nếu ở ô xám chỉ xét hai hướng Đông và Tây với cùng mức ưu tiên, nó cho đúng xác suất $\tfrac12$ của Ví dụ 09.9.

::: definition Định nghĩa 09.12 (Chính sách Gaussian với phương sai cố định)
Cho $\mathcal A=\mathbb R$, đặc trưng trạng thái $\phi(s)\in\mathbb R^d$ giữ cố định, $\theta\in\mathbb R^d$ và $\sigma^2>0$ cố định. Chính sách Gaussian có mật độ
$$
\pi_\theta(a\mid s)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\Bigl(-\frac{\bigl(a-\mu_\theta(s)\bigr)^2}{2\sigma^2}\Bigr),\qquad\mu_\theta(s)=\phi(s)^\top\theta.
$$
:::

Trung bình $\mu_\theta(s)$ là hành động "trung tâm" tại $s$, và $\sigma$ đo độ trải của các hành động được lấy mẫu quanh nó. Mật độ dương trên toàn trục số thực, nên khi hành động hợp lệ nằm trong một khoảng $[a_{\min},a_{\max}]$, một phần khối xác suất rơi ra ngoài. Cài đặt thường cắt mẫu về khoảng, hoặc đưa mẫu qua một hàm đơn điệu như $\tanh$. Với phép cắt, ta có thể coi việc cắt là một phần của môi trường và tiếp tục dùng mật độ Gaussian của mẫu trước khi cắt; với $a=\tanh(u)$, mật độ của $a$ có thêm thừa số $1/(1-a^2)$ từ phép đổi biến, và hàm điểm ở Mục 5 phải tính theo mật độ đó. Bài giảng gốc (trang 38) đặt câu hỏi về vấn đề của chính sách Gaussian; miền bị chặn là một câu trả lời, độ trải $\sigma$ cố định không học là một câu trả lời khác.

| | Softmax | Gaussian, $\sigma^2$ cố định |
|---|---|---|
| miền $\mathcal A$ | hữu hạn | $\mathbb R$ (miền bị chặn cần cắt hoặc biến đổi) |
| đặc trưng | $\phi(s,a)$ theo cặp trạng thái–hành động | $\phi(s)$ theo trạng thái |
| tham số quyết định | mức ưu tiên $\phi(s,a)^\top\theta$ | trung bình $\phi(s)^\top\theta$ |
| chuẩn hóa | $\sum_a\pi_\theta(a\mid s)=1$ | $\int\pi_\theta(a\mid s)\,\mathrm da=1$ |
| lấy mẫu | phân phối phân loại $\operatorname{Cat}\bigl(\pi_\theta(\cdot\mid s)\bigr)$ | $\mathcal N\bigl(\mu_\theta(s),\sigma^2\bigr)$ |

::: remark Nhận xét 09.13 (Nhầm lẫn thường gặp về chính sách ngẫu nhiên)
1. "Chính sách ngẫu nhiên khôi phục thông tin trạng thái bị gộp." Sai: ở Ví dụ 09.9, chính sách vẫn không biết mình ở ô 2 hay ô 4 và đi sai hướng với xác suất $\tfrac12$; nó chỉ tránh kẹt. Muốn đạt $h_2=h_4=2$, cần đặc trưng hoặc bộ nhớ phân biệt hai ô.
2. "Trong MDP quan sát đầy đủ cũng cần chính sách ngẫu nhiên để tối ưu." Sai theo Định lý 04.25; lợi ích của chính sách ngẫu nhiên ở đây đến từ ràng buộc trên lớp chính sách.
3. "$\epsilon_{\mathrm{exp}}$-tham lam là chính sách ngẫu nhiên được học." Sai: xác suất $\epsilon_{\mathrm{exp}}$ cố định, không tối ưu theo bài toán; chính sách tham số hóa học chính các xác suất.
4. "$\pi_\theta(a\mid s)$ của Gaussian là xác suất của $a$." Sai: đó là mật độ; xác suất một giá trị thực cụ thể bằng $0$.
:::

**Trong thực hành.** Trong một cài đặt, chính sách tham số hóa là một hàm, tuyến tính theo đặc trưng hoặc một mạng nơ-ron, trả về các mức ưu tiên (softmax) hoặc trung bình (Gaussian), và tác tử lấy mẫu từ phân phối đó ở mỗi bước. Định lý 04.25 giả sử chính sách được phép phụ thuộc vào trạng thái đầy đủ; với xấp xỉ hàm, đặc trưng thường gộp nhiều trạng thái, và với quan sát không Markov, quan sát gộp các trạng thái khác nhau, nên tình huống của Ví dụ 09.9 không hiếm. Với góc lái của xe hay mô-men của khớp robot, chính sách Gaussian tránh việc giải $\max_a$ ở mỗi bước.

Như vậy, Ví dụ 09.8 và 09.9 cho thấy khi đặc trưng gộp hai trạng thái cần hai hành động khác nhau, mọi chính sách tất định theo đặc trưng có ô không bao giờ tới đích, còn chính sách ngẫu nhiên $\tfrac12$ đưa mọi ô tới đích, trung bình $3{,}8$ bước khi ô xuất phát đều trên năm ô; Nhận xét 09.9 giải thích vì sao điều này không mâu thuẫn với Định lý 04.25. Định nghĩa 09.10–09.12 cho hai họ chính sách học được xác suất hoặc mật độ, softmax cho tập hữu hạn và Gaussian cho hành động thực. Họ $\pi_\theta$ chưa cho biết nên chỉnh $\theta$ theo hướng nào. Trong Mục 5, chúng ta định nghĩa hàm mục tiêu $J(\theta)$, lợi tức kỳ vọng của $\pi_\theta$, và tìm cách ước lượng gradient của nó.

*Nguồn: bài giảng gốc lecture09-ddqn-and-policy-gradient-part1.pdf (2025–2026), trang 22–29, 36–38; Sutton và Barto (2018), §13.1, Ví dụ 13.1, §13.7; ghi chú bài giảng Bài 04, Định lý 04.25.*

---

## 5. Hàm mục tiêu và hàm điểm

Mục 4 cho một họ chính sách $\pi_\theta$ khả vi theo $\theta$: chính sách softmax trên tập hành động hữu hạn và chính sách Gaussian trên hành động thực. Họ đó chưa cho biết nên chỉnh $\theta$ theo hướng nào. Muốn chỉnh, chúng ta cần một số đo chất lượng của $\pi_\theta$ và một cách tìm hướng làm số đo đó tăng. Số đo là lợi tức kỳ vọng $J(\theta)$; hướng là gradient $\nabla_\theta J(\theta)$. Trong học tăng cường, $J$ không có công thức, vì phần thưởng và động lực của môi trường chưa biết; ta chỉ quan sát được lợi tức của các lượt. Chúng ta xét cách ước lượng gradient đơn giản nhất, sai phân hữu hạn, và chỉ ra chi phí của nó; rồi định nghĩa hàm điểm, đại lượng cho phép ước lượng gradient từ chính các lượt của $\pi_\theta$, và tính nó cho hai họ của Mục 4. Mọi ví dụ của mục dùng chung một bài toán nhỏ, được vẽ thành thẻ dữ kiện dưới đây.

![Thẻ dữ kiện bài toán một bước, chính sách softmax, hai hành động: bảng hai cột cho a bằng 1 và a bằng 2, đặc trưng phi của s, a bằng (1; 0) và (0; 1); xác suất pi theta bằng 2/3 và 1/3; phần thưởng r bằng 3 và 0. Dòng dưới: theta bằng (log 2; 0), lượt dừng sau A 0.](img/lec-09/one-step-card.svg)

Chính sách là softmax của Định nghĩa 09.11, nên $\pi_\theta(1\mid s)=\tfrac{e^{\log2}}{e^{\log2}+e^0}=\tfrac23$.

<!-- note-topic-id: lec-09-topic-07 -->
### Hàm mục tiêu và bước tăng gradient

Muốn so sánh hai giá trị của $\theta$, chúng ta cần gán cho mỗi chính sách một số. Bài giảng gốc (trang 30) chọn giá trị của chính sách tại trạng thái đầu, tức lợi tức kỳ vọng khi xuất phát từ đó rồi đi theo $\pi_\theta$. Một chính sách tốt hơn là một chính sách có số này lớn hơn.

::: example Ví dụ 09.11 (Hàm mục tiêu của bài toán một bước)
**Dữ kiện.** Bài toán một bước, hai hành động: $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, chính sách softmax, $r(1)=3$, $r(2)=0$; lượt dừng sau $A_0$.

**Lợi tức.** Lượt có một phần thưởng, nên $G_0=R_1=r(A_0)$: bằng $3$ nếu chọn hành động 1, bằng $0$ nếu chọn hành động 2.

**Kỳ vọng.** Với $\theta=(\log2;\,0)$,
$$
J(\theta)=\mathbb E_{\pi_\theta}[G_0]=3\cdot\tfrac23+0\cdot\tfrac13=2.
$$
Với $\theta'=(0;\,0)$, hai hành động có xác suất $\tfrac12$, nên $J(\theta')=1{,}5$. Dạng tổng quát: $J(\theta)=3\pi_\theta(1\mid s)=\dfrac{3e^{\theta_1}}{e^{\theta_1}+e^{\theta_2}}$.

**Diễn giải.** $\theta$ tốt hơn $\theta'$ vì đặt xác suất lớn hơn lên hành động có phần thưởng lớn hơn. $J$ tăng khi $\theta_1-\theta_2$ tăng và bị chặn trên bởi $3$, giá trị của chính sách tất định chọn hành động 1.
:::

::: definition Định nghĩa 09.14 (Hàm mục tiêu)
Cho một MDP có kết thúc với phân phối trạng thái đầu $\rho_0$, hàm động lực $P$, phần thưởng bị chặn $|R_{t+1}|\le R_{\max}$ và $0\le\gamma<1$. Với chính sách tham số hóa $\pi_\theta$, giả sử bước kết thúc $T$ hữu hạn hầu chắc chắn; sau $T$, lượt đi vào một trạng thái hấp thụ có phần thưởng $0$. Hàm mục tiêu (objective function) của $\pi_\theta$ là
$$
J(\theta)=\mathbb E_{\pi_\theta}[G_0],\qquad G_0=\sum_{t=0}^{T-1}\gamma^tR_{t+1},
$$
trong đó kỳ vọng lấy theo $S_0\sim\rho_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$ và $(S_{t+1},R_{t+1})\sim P(\cdot\mid S_t,A_t)$.
:::

Định nghĩa đọc như sau: chạy chính sách $\pi_\theta$ từ một trạng thái đầu ngẫu nhiên tới khi lượt dừng, cộng các phần thưởng có chiết khấu, rồi lấy trung bình trên mọi lượt có thể. Bài giảng gốc viết $J(\theta)=V^{\pi}(s_1)$ với một trạng thái đầu cố định $s_1$; đó là trường hợp $\rho_0$ dồn hết xác suất vào $s_1$. Với $\rho_0$ tổng quát, $J(\theta)=\sum_s\rho_0(s)v_{\pi_\theta}(s)$, với $v_{\pi_\theta}$ là hàm giá trị trạng thái của Bài 03. Trong ba thành phần sinh ra lượt, chỉ chính sách phụ thuộc $\theta$; $\rho_0$ và $P$ là của môi trường. Điều này quyết định cách lấy đạo hàm ở Mục 6.

Các giả thiết có vai trò riêng. Phần thưởng bị chặn và $\gamma<1$ cho $|G_0|\le R_{\max}/(1-\gamma)$ trên mọi lượt, nên kỳ vọng tồn tại. Bỏ phần thưởng bị chặn: một phân phối phần thưởng không khả tích, chẳng hạn phân phối Cauchy, làm $\mathbb E[G_0]$ không xác định. Giả thiết $T<\infty$ hầu chắc chắn cho phép viết $G_0$ là một tổng hữu hạn; quy ước trạng thái hấp thụ cho phép viết cùng đại lượng là tổng vô hạn $\sum_{t\ge0}\gamma^tR_{t+1}$ với mọi phần thưởng sau $T$ bằng $0$, như quy ước đọc ở đầu chương.

::: example Ví dụ 09.12 (Lợi tức của một lượt hai bước)
**Dữ kiện.** Một lượt dừng tại $T=2$ với $R_1=1$, $R_2=2$; $\gamma=0{,}9$.

**Tính.** $G_1=R_2=2$; $G_0=R_1+\gamma R_2=1+0{,}9\cdot2=2{,}8$; $G_2=0$ theo quy ước.

**Kiểm tra lại.** $G_0=R_1+\gamma G_1=1+0{,}9\cdot2=2{,}8$, đúng hệ thức đệ quy của lợi tức.
:::

Hàm mục tiêu $J$ khác mục tiêu $y_i$ của DQN ở Mục 2 và 3, dù hai từ giống nhau. $y_i$ là một số gắn với một mẫu chuyển, dùng làm giá trị hồi quy cho $Q_\theta(S_i,A_i)$; $J$ là một hàm của tham số chính sách, cần cực đại hóa.

Khi đã có $J$, bài toán học trở thành bài toán tối ưu: tìm $\theta$ làm $J(\theta)$ lớn nhất. Bài giảng gốc (trang 31) nêu hai nhóm cách giải. Nhóm không dùng gradient, như leo đồi (hill climbing) và giải thuật di truyền, chỉ cần so sánh giá trị $J$ của các tham số thử. Nhóm dùng gradient đi theo hướng tăng nhanh nhất của $J$ tại tham số hiện tại. Chúng ta theo nhóm thứ hai, vì nó dùng được cấu trúc khả vi của $\pi_\theta$ và mở rộng được tới mạng nơ-ron với nhiều tham số.

Nhắc lại từ Bài 08: hạ gradient cập nhật $\theta\leftarrow\theta-\eta\,\nabla_\theta L_B(\theta)$ để cực tiểu hóa hàm mất mát. Muốn cực đại hóa $J$, ta đi theo chiều ngược lại:
$$
\theta\leftarrow\theta+\alpha\,\nabla_\theta J(\theta),\qquad\alpha>0.
$$
Dấu cộng có lý do bậc một. Theo khai triển Taylor, $J(\theta+\alpha g)=J(\theta)+\alpha\,\nabla_\theta J(\theta)^\top g+o(\alpha)$; với $g=\nabla_\theta J(\theta)$, số hạng bậc một bằng $\alpha\lVert\nabla_\theta J(\theta)\rVert^2\ge0$, nên với $\alpha$ đủ nhỏ và gradient khác $0$, $J$ tăng. Bài giảng gốc (trang 32) gọi $\nabla_\theta J(\theta)=\bigl(\partial J/\partial\theta_1;\,\dots;\,\partial J/\partial\theta_d\bigr)$ là gradient chính sách (policy gradient). Khi gradient không tính được chính xác, ta thay nó bằng một ước lượng $\widehat g$; phần còn lại của chương là việc xây dựng $\widehat g$.

Trên bài toán một bước, $J$ có dạng đóng, nên gradient tính được trực tiếp. Đạo hàm của softmax hai hành động là $\partial\pi_\theta(1\mid s)/\partial\theta_1=\pi_\theta(1\mid s)\pi_\theta(2\mid s)$ và $\partial\pi_\theta(1\mid s)/\partial\theta_2=-\pi_\theta(1\mid s)\pi_\theta(2\mid s)$. Vậy
$$
\nabla_\theta J(\theta)=3\,\pi_\theta(1\mid s)\,\pi_\theta(2\mid s)\,(1;\,-1)=3\cdot\tfrac23\cdot\tfrac13\,(1;\,-1)=\bigl(\tfrac23;\,-\tfrac23\bigr)
$$
tại $\theta=(\log2;\,0)$. Một bước với $\alpha=0{,}1$ cho $\theta=(\log2+0{,}0667;\,-0{,}0667)$, $\pi_\theta(1\mid s)\approx0{,}696$ và $J\approx2{,}087>2$.

Câu hỏi thảo luận của bài giảng gốc (trang 30), tìm một chính sách tốt khác gì tìm một hàm giá trị tốt, có câu trả lời ở hai dòng cập nhật trên. Học giá trị (Bài 06–08) cực tiểu hóa sai số dự đoán của $Q_\theta$ so với một mục tiêu, rồi suy ra chính sách bằng $\arg\max$; một hàm giá trị tốt theo nghĩa sai số nhỏ chưa chắc cho chính sách tốt nhất trong một lớp bị ràng buộc, như Ví dụ 09.8 cho thấy. Học chính sách tối ưu trực tiếp đại lượng cần cực đại.

**Trong thực hành.** Trong một cài đặt, $J(\theta)$ không bao giờ được tính: ta chỉ có lợi tức của các lượt đã chạy, và trung bình của chúng là một ước lượng có nhiễu của $J$. Các thư viện tối ưu thường được viết để cực tiểu hóa, nên cài đặt cực tiểu hóa $-J$, hoặc một hàm mất mát thay thế có gradient bằng $-\widehat g$; dấu trừ này là nguồn lỗi thường gặp khi chuyển từ mã DQN sang mã gradient chính sách.

<!-- note-topic-id: lec-09-topic-14 -->
### Ước lượng gradient bằng sai phân hữu hạn

Phép tính gradient ở trên dùng $r(1)=3$, $r(2)=0$ và công thức của $J$. Khi phần thưởng và động lực chưa biết, $J(\theta)$ chỉ đo được qua lợi tức của các lượt chạy bằng $\pi_\theta$. Cách đơn giản nhất để có gradient từ các phép đo giá trị là quay về định nghĩa đạo hàm (bài giảng gốc, trang 33): $f'(x)=\lim_{h\to0}\bigl(f(x+h)-f(x)\bigr)/h$. Thay giới hạn bằng một bước nhỏ $\epsilon>0$ theo từng tọa độ, với $u_k$ là vector đơn vị thứ $k$ của $\mathbb R^d$,
$$
\frac{\partial J(\theta)}{\partial\theta_k}\approx\frac{J(\theta+\epsilon u_k)-J(\theta)}{\epsilon},\qquad k=1,\dots,d.
$$

::: example Ví dụ 09.13 (Sai phân hữu hạn trên bài toán một bước)
**Dữ kiện.** Bài toán một bước với $\theta=(\log2;\,0)$, $J(\theta)=2$; $\epsilon=0{,}1$.

**Tọa độ 1.** $\theta+\epsilon u_1=(\log2+0{,}1;\,0)$, nên hành động 1 có xác suất $\dfrac{2e^{0{,}1}}{2e^{0{,}1}+1}\approx0{,}6885$ và $J\approx2{,}0655$. Thương sai phân: $(2{,}0655-2)/0{,}1\approx0{,}655$.

**Tọa độ 2.** $\theta+\epsilon u_2=(\log2;\,0{,}1)$, nên $J=\dfrac{6}{2+e^{0{,}1}}\approx1{,}9323$. Thương sai phân: $\approx-0{,}677$.

**So sánh.** Giá trị đúng là $\bigl(\tfrac23;\,-\tfrac23\bigr)\approx(0{,}667;\,-0{,}667)$. Sai lệch khoảng $0{,}01$ ở mỗi tọa độ đến từ $\epsilon$ hữu hạn; với $\epsilon=0{,}01$, thương ở tọa độ 1 là $0{,}6656$.

**Chi phí.** Ba giá trị $J(\theta)$, $J(\theta+\epsilon u_1)$, $J(\theta+\epsilon u_2)$, tức $d+1$ với $d=2$.
:::

Ví dụ dùng giá trị đúng của $J$. Trong học tăng cường, mỗi giá trị $J$ được thay bằng trung bình lợi tức $\widehat J$ trên $n$ lượt, và hai nguồn sai số cộng lại. Sai số do $\epsilon$ (sai số cắt cụt) giảm khi $\epsilon$ nhỏ. Sai số do nhiễu thì tăng: nếu hai trung bình dùng các lượt độc lập và lợi tức có phương sai $\sigma_G^2$ ở cả hai tham số, thương sai phân có phương sai
$$
\operatorname{Var}\Bigl[\frac{\widehat J(\theta+\epsilon u_k)-\widehat J(\theta)}{\epsilon}\Bigr]\approx\frac{2\sigma_G^2}{n\epsilon^2}.
$$
Trên bài toán một bước, $G_0\in\{3;\,0\}$ nên $\sigma_G^2=9\pi(1\mid s)\pi(2\mid s)=2$ tại $\theta$ và $\approx1{,}93$ tại $\theta+\epsilon u_1$. Với $n=100$ lượt cho mỗi giá trị và $\epsilon=0{,}1$, độ lệch chuẩn của thương khoảng $2$, gấp ba lần giá trị cần ước lượng $\tfrac23$; muốn độ lệch chuẩn $0{,}1$ cần khoảng $39\,000$ lượt cho mỗi giá trị. Giảm $\epsilon$ để bớt sai số cắt cụt làm phương sai tăng theo $1/\epsilon^2$.

Chi phí tăng theo số tham số. Mỗi ước lượng gradient cần chạy $d+1$ chính sách khác nhau, mỗi chính sách nhiều lượt; với một mạng nơ-ron có $10^5$ tham số, một bước cập nhật cần $10^5+1$ nhóm lượt. Bài giảng gốc tóm tắt: đơn giản, nhiễu lớn, kém hiệu quả, nhưng đôi khi vẫn hữu ích, và áp dụng được cho chính sách bất kỳ, kể cả chính sách không khả vi. Sai phân hữu hạn chỉ cần đo $J$, nên dùng được cho chính sách tất định theo ngưỡng hay chính sách là một chương trình. Với chính sách khả vi như softmax và Gaussian, chúng ta muốn một ước lượng gradient lấy từ chính các lượt của $\pi_\theta$, không phải chạy thêm $d$ chính sách nhiễu.

<!-- note-topic-id: lec-09-topic-08 -->
### Hàm điểm

Trở lại bài toán một bước. Lượt có một phần thưởng, nên $G_0=r(A_0)$, và $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ là tổng có trọng số xác suất: $J(\theta)=\sum_a\pi_\theta(a\mid s)\,r(a)$. Phần thưởng $r(a)$ là của môi trường, không phụ thuộc $\theta$, nên gradient chỉ rơi vào xác suất: $\nabla_\theta J=\sum_ar(a)\nabla_\theta\pi_\theta(a\mid s)$. Tổng này trải trên mọi hành động, cần phần thưởng của từng hành động, và không có trọng số $\pi_\theta$, nên chưa là một kỳ vọng; một lượt chỉ cho phần thưởng của hành động đã lấy mẫu. Một cách trực quan, ta muốn mỗi số hạng có thừa số $\pi_\theta(a\mid s)$, vì khi đó tổng là kỳ vọng theo $A\sim\pi_\theta(\cdot\mid s)$ và ước lượng được bằng mẫu. Nhân và chia mỗi số hạng cho $\pi_\theta(a\mid s)>0$ cho đúng thừa số đó, vì theo quy tắc đạo hàm của logarit, $\nabla_\theta\pi_\theta/\pi_\theta=\nabla_\theta\log\pi_\theta$:
$$
\begin{aligned}
J(\theta)&=\sum_a\pi_\theta(a\mid s)\,r(a),\\
\nabla_\theta J(\theta)&=\sum_ar(a)\,\nabla_\theta\pi_\theta(a\mid s)\\
&=\sum_a\pi_\theta(a\mid s)\,r(a)\,\nabla_\theta\log\pi_\theta(a\mid s)\\
&=\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}\bigl[r(A)\,\nabla_\theta\log\pi_\theta(A\mid s)\bigr].
\end{aligned}
$$
Dòng hai dùng $\nabla_\theta r(a)=0$; dòng ba nhân, chia cho $\pi_\theta(a\mid s)$; dòng bốn là định nghĩa kỳ vọng. Vế phải chỉ cần phần thưởng tại hành động đã lấy mẫu: một hành động $A\sim\pi_\theta(\cdot\mid s)$ cho một mẫu $r(A)\nabla_\theta\log\pi_\theta(A\mid s)$ của gradient, không cần biết $r$ của các hành động khác và không phải chạy thêm $d$ chính sách như sai phân hữu hạn. Cùng phép nhân, chia áp dụng cho mọi hàm $f$ của hành động không phụ thuộc $\theta$: $\sum_af(a)\nabla_\theta\pi_\theta(a\mid s)=\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}\bigl[f(A)\nabla_\theta\log\pi_\theta(A\mid s)\bigr]$. Bài giảng gốc (trang 34) gọi phép biến đổi này là dùng tỉ số xác suất (likelihood ratio); Mục 6 áp dụng nó cho $J$ trên cả lượt.

::: example Ví dụ 09.14 (Đạo hàm log xác suất trên bài toán một bước)
**Dữ kiện.** Bài toán một bước, chính sách softmax với đặc trưng đơn vị, $\theta=(\log2;\,0)$, $\pi_\theta(\cdot\mid s)=\bigl(\tfrac23;\,\tfrac13\bigr)$, $r(1)=3$, $r(2)=0$.

**Log xác suất.** $\log\pi_\theta(1\mid s)=\theta_1-\log\bigl(e^{\theta_1}+e^{\theta_2}\bigr)$.

**Gradient.** $\partial/\partial\theta_1$: $1-\dfrac{e^{\theta_1}}{e^{\theta_1}+e^{\theta_2}}=1-\pi_\theta(1\mid s)=\tfrac13$; $\partial/\partial\theta_2$: $-\pi_\theta(2\mid s)=-\tfrac13$. Vậy $\nabla_\theta\log\pi_\theta(1\mid s)=\bigl(\tfrac13;\,-\tfrac13\bigr)$.

**Vế phải của dẫn xuất.** Chỉ hành động 1 có phần thưởng khác $0$, nên $\mathbb E_{A\sim\pi_\theta}\bigl[r(A)\nabla_\theta\log\pi_\theta(A\mid s)\bigr]=\tfrac23\cdot3\bigl(\tfrac13;\,-\tfrac13\bigr)=\bigl(\tfrac23;\,-\tfrac23\bigr)$.

**Kiểm tra lại.** Trùng gradient tính trực tiếp $3\pi_\theta(1\mid s)\pi_\theta(2\mid s)(1;\,-1)=\bigl(\tfrac23;\,-\tfrac23\bigr)$ ở đầu mục; và $\pi_\theta(1\mid s)\bigl(\tfrac13;\,-\tfrac13\bigr)=\bigl(\tfrac29;\,-\tfrac29\bigr)=\nabla_\theta\pi_\theta(1\mid s)$.
:::

::: definition Định nghĩa 09.15 (Hàm điểm)
Cho chính sách tham số hóa $\pi_\theta$, trạng thái $s$ và hành động $a$ với $\pi_\theta(a\mid s)>0$. Hàm điểm (score function) của $\pi_\theta$ tại $(s,a)$ là
$$
\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)\in\mathbb R^d.
$$
Khi $\mathcal A$ liên tục, $\pi_\theta(a\mid s)$ là mật độ và định nghĩa giữ nguyên.
:::

Hàm điểm là một vector cùng số chiều với $\theta$. Tọa độ thứ $k$ của nó cho biết log xác suất của hành động $a$ thay đổi bao nhiêu khi tăng $\theta_k$; vì $\nabla\log\pi=\nabla\pi/\pi$, đó là thay đổi tương đối của xác suất. Đi một bước nhỏ theo $\psi_\theta(s,a)$ làm tăng $\pi_\theta(a\mid s)$; đi ngược chiều làm giảm. Tên gọi lấy từ thống kê, nơi gradient của log hàm hợp lý theo tham số được gọi là hàm điểm. Trong Ví dụ 09.14, $\psi_\theta(s,1)=\bigl(\tfrac13;\,-\tfrac13\bigr)$: tăng $\theta_1$ hoặc giảm $\theta_2$ đều làm hành động 1 dễ được chọn hơn.

Định nghĩa cần $\pi_\theta(a\mid s)>0$. Nếu một hành động có xác suất $0$, logarit của nó không xác định, và hành động đó cũng không bao giờ xuất hiện trong mẫu. Chính sách tất định vi phạm điều kiện này ở mọi hành động không được chọn, và thường không khả vi theo $\theta$; phép tham lam theo $Q$ và hành vi $\epsilon_{\mathrm{exp}}$-tham lam cũng không khả vi theo tham số của $Q$ vì phép $\arg\max$. Softmax cho mọi hành động xác suất dương, Gaussian cho mọi số thực mật độ dương, nên hai họ của Mục 4 thỏa điều kiện ở mọi $(s,a)$. Khi dùng hàm điểm để lấy kỳ vọng, như ở mệnh đề dưới đây, cần thêm một điều: tập $\{a:\pi_\theta(a\mid s)>0\}$, gọi là miền hỗ trợ, không đổi theo $\theta$.

### Hàm điểm của chính sách softmax

Áp dụng định nghĩa cho chính sách softmax của Định nghĩa 09.11 cho một công thức đóng.

::: proposition Mệnh đề 09.16 (Hàm điểm của chính sách softmax)
**Giả thiết.** $\mathcal A$ hữu hạn; đặc trưng $\phi(s,a)\in\mathbb R^d$ không phụ thuộc $\theta$; $\pi_\theta(a\mid s)=\exp\bigl(\phi(s,a)^\top\theta\bigr)/\sum_{b\in\mathcal A}\exp\bigl(\phi(s,b)^\top\theta\bigr)$.

**Kết luận.** Với mọi $s$ và mọi $a\in\mathcal A$,
$$
\psi_\theta(s,a)=\phi(s,a)-\sum_{b\in\mathcal A}\pi_\theta(b\mid s)\,\phi(s,b).
$$
:::

::: proof
**Bước 1 (log xác suất).** Lấy logarit của định nghĩa:
$$
\log\pi_\theta(a\mid s)=\phi(s,a)^\top\theta-\log\sum_{b\in\mathcal A}e^{\phi(s,b)^\top\theta}.
$$

**Bước 2 (hạng thứ nhất).** $\nabla_\theta\bigl(\phi(s,a)^\top\theta\bigr)=\phi(s,a)$, vì $\phi(s,a)$ không phụ thuộc $\theta$.

**Bước 3 (hạng thứ hai).** Theo quy tắc dây chuyền,
$$
\begin{aligned}
\nabla_\theta\log\sum_be^{\phi(s,b)^\top\theta}
&=\frac{\sum_be^{\phi(s,b)^\top\theta}\,\phi(s,b)}{\sum_ce^{\phi(s,c)^\top\theta}}\\
&=\sum_b\pi_\theta(b\mid s)\,\phi(s,b).
\end{aligned}
$$

**Bước 4.** Trừ hai hạng được kết luận. $\square$
:::

Mệnh đề đọc như sau: hàm điểm của hành động $a$ là đặc trưng của $a$ trừ đặc trưng trung bình theo chính sách hiện tại. Giả thiết đặc trưng cố định được dùng ở Bước 2 và 3; nếu $\phi$ là đầu ra của một mạng có tham số được học cùng $\theta$, gradient phải đi tiếp qua mạng đó, và công thức trên chỉ là phần gradient theo lớp cuối.

![Ba chấm tròn là đặc trưng phi của s, 1; s, 2; s, 3 với xác suất 0,5; 0,3; 0,2 ghi trong hộp bên phải. Hình thoi rỗng là trung bình đặc trưng theo pi theta. Ba mũi tên đi từ hình thoi tới ba chấm, ghi psi theta của s, 1; s, 2; s, 3.](img/lec-09/softmax-score.svg)

Hình vẽ ba hành động trong mặt phẳng đặc trưng với xác suất $0{,}5$; $0{,}3$; $0{,}2$. Hình thoi là đặc trưng trung bình, tức trọng tâm của ba điểm với trọng số xác suất; mỗi mũi tên là một hàm điểm. Vì hình thoi là trọng tâm có trọng số, $0{,}5$ lần mũi tên thứ nhất cộng $0{,}3$ lần mũi tên thứ hai cộng $0{,}2$ lần mũi tên thứ ba bằng vector $0$. Hành động có xác suất nhỏ thường nằm xa trọng tâm hơn, nên hàm điểm của nó dài hơn.

::: example Ví dụ 09.15 (Hàm điểm softmax hai hành động)
**Dữ kiện.** Bài toán một bước: $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$, $\pi_\theta(\cdot\mid s)=\bigl(\tfrac23;\,\tfrac13\bigr)$.

**Đặc trưng trung bình.** $\tfrac23(1;\,0)+\tfrac13(0;\,1)=\bigl(\tfrac23;\,\tfrac13\bigr)$.

**Hàm điểm.** $\psi_\theta(s,1)=(1;\,0)-\bigl(\tfrac23;\,\tfrac13\bigr)=\bigl(\tfrac13;\,-\tfrac13\bigr)$; $\psi_\theta(s,2)=(0;\,1)-\bigl(\tfrac23;\,\tfrac13\bigr)=\bigl(-\tfrac23;\,\tfrac23\bigr)$.

**Trung bình theo chính sách.** $\tfrac23\bigl(\tfrac13;\,-\tfrac13\bigr)+\tfrac13\bigl(-\tfrac23;\,\tfrac23\bigr)=\bigl(\tfrac29-\tfrac29;\,-\tfrac29+\tfrac29\bigr)=(0;\,0)$.

**Diễn giải.** Bước theo $\psi_\theta(s,1)$ tăng $\theta_1$ và giảm $\theta_2$, nên tăng $\pi_\theta(1\mid s)$; bước theo $\psi_\theta(s,2)$ làm ngược lại. $\psi_\theta(s,2)$ dài gấp đôi $\psi_\theta(s,1)$ vì hành động 2 ít được chọn hơn.

**Kiểm tra lại.** $\psi_\theta(s,1)$ trùng kết quả tính trực tiếp của Ví dụ 09.14.
:::

Kết quả $(0;\,0)$ của ví dụ đúng cho mọi chính sách thỏa ba giả thiết sau.

::: proposition Mệnh đề 09.17 (Kỳ vọng của hàm điểm)
**Giả thiết.** Với trạng thái $s$ cố định: (i) $\pi_\theta(a\mid s)$ khả vi theo $\theta$ tại mọi $a$ trong miền hỗ trợ; (ii) miền hỗ trợ $\{a:\pi_\theta(a\mid s)>0\}$ không phụ thuộc $\theta$; (iii) khi $\mathcal A$ liên tục, có một hàm khả tích $h(a)$ với $\lVert\nabla_\theta\pi_{\theta'}(a\mid s)\rVert\le h(a)$ cho mọi $\theta'$ trong một lân cận của $\theta$.

**Kết luận.** $\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}\bigl[\psi_\theta(s,A)\bigr]=0\in\mathbb R^d$. Hệ quả: với mọi $c$ không phụ thuộc $A$ (khi đã biết $s$), $\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}\bigl[c\,\psi_\theta(s,A)\bigr]=0$.
:::

::: proof
**Bước 1 (đổi hàm điểm thành gradient của xác suất).** Trên miền hỗ trợ, $\pi_\theta(a\mid s)\psi_\theta(s,a)=\nabla_\theta\pi_\theta(a\mid s)$. Ngoài miền hỗ trợ, số hạng có trọng số $0$ và không đóng góp. Với $\mathcal A$ hữu hạn,
$$
\begin{aligned}
\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}\bigl[\psi_\theta(s,A)\bigr]
&=\sum_{a:\,\pi_\theta(a\mid s)>0}\pi_\theta(a\mid s)\,\psi_\theta(s,a)\\
&=\sum_{a:\,\pi_\theta(a\mid s)>0}\nabla_\theta\pi_\theta(a\mid s).
\end{aligned}
$$

**Bước 2 (đổi đạo hàm và tổng).** Theo (ii), tập lấy tổng không đổi khi $\theta$ thay đổi, nên đạo hàm của tổng bằng tổng các đạo hàm:
$$
\sum_{a:\,\pi_\theta(a\mid s)>0}\nabla_\theta\pi_\theta(a\mid s)=\nabla_\theta\sum_{a:\,\pi_\theta(a\mid s)>0}\pi_\theta(a\mid s)=\nabla_\theta1=0.
$$

**Bước 3 (trường hợp liên tục).** Thay tổng bằng tích phân trên miền hỗ trợ. Giả thiết (iii) cho phép đổi $\nabla_\theta$ với tích phân theo định lý hội tụ bị chặn, và $\int\pi_\theta(a\mid s)\,\mathrm da=1$ với mọi $\theta$.

**Bước 4 (hệ quả).** $c$ là hằng số đối với phép lấy kỳ vọng theo $A$, nên $\mathbb E[c\,\psi_\theta(s,A)]=c\,\mathbb E[\psi_\theta(s,A)]=0$. $\square$
:::

Ba giả thiết có vai trò riêng. Khả vi cho hàm điểm tồn tại. Miền hỗ trợ cố định được dùng ở Bước 2: bỏ nó, kết luận sai. Phản ví dụ: $A\sim$ phân phối đều trên $[0,\theta]$ với $\theta>0$; mật độ là $1/\theta$ trên $[0,\theta]$, nên $\psi_\theta(a)=\tfrac{\mathrm d}{\mathrm d\theta}\log(1/\theta)=-1/\theta$ với mọi $a$ trong miền hỗ trợ, và $\mathbb E[\psi_\theta(A)]=-1/\theta\ne0$. Đạo hàm của $\int_0^\theta\tfrac1\theta\,\mathrm da=1$ vẫn bằng $0$, nhưng phần $+1/\theta$ đến từ cận trên di động của tích phân và hàm điểm không nhìn thấy nó. Giả thiết (iii) chỉ cần cho hành động liên tục; với tập hành động hữu hạn, tổng hữu hạn và phép đổi luôn đúng. Softmax thỏa cả ba; Gaussian với $\sigma$ cố định thỏa cả ba, với miền hỗ trợ là $\mathbb R$.

Hệ quả của mệnh đề sẽ được dùng hai lần. Ở Mục 6, các phần thưởng nhận trước khi lấy mẫu $A_t$ đóng vai $c$, và mệnh đề cho phép bỏ chúng khỏi ước lượng gradient. Ở Bài 10, một đường cơ sở (baseline) phụ thuộc trạng thái đóng vai $c$. Mệnh đề cũng cho biết hàm điểm một mình không chứa thông tin về hướng tốt: trung bình của nó bằng $0$ dưới mọi chính sách. Chỉ khi nhân với một đại lượng phụ thuộc hành động, như phần thưởng của hành động đó, kỳ vọng mới khác $0$.

<!-- note-topic-id: lec-09-topic-09 -->
### Hàm điểm của chính sách Gaussian

Với hành động thực, chẳng hạn góc lái, Định nghĩa 09.12 dùng chính sách Gaussian $A\mid S=s\sim\mathcal N\bigl(\mu_\theta(s),\sigma^2\bigr)$ với $\mu_\theta(s)=\phi(s)^\top\theta$, đặc trưng trạng thái $\phi(s)\in\mathbb R^d$ và $\sigma^2>0$ giữ cố định. Bài giảng gốc (trang 37) hỏi hàm điểm của chính sách này; định nghĩa cho câu trả lời trực tiếp.

::: proposition Mệnh đề 09.18 (Hàm điểm của chính sách Gaussian)
**Giả thiết.** $\mathcal A=\mathbb R$; $\phi(s)\in\mathbb R^d$ và $\sigma^2>0$ không phụ thuộc $\theta$; $\pi_\theta(\cdot\mid s)$ là mật độ của $\mathcal N\bigl(\phi(s)^\top\theta,\sigma^2\bigr)$.

**Kết luận.** Với mọi $s$ và mọi $a\in\mathbb R$,
$$
\psi_\theta(s,a)=\frac{a-\mu_\theta(s)}{\sigma^2}\,\phi(s).
$$
:::

::: proof
**Bước 1 (log mật độ).** Từ Định nghĩa 09.12,
$$
\log\pi_\theta(a\mid s)=-\frac{\bigl(a-\mu_\theta(s)\bigr)^2}{2\sigma^2}-\tfrac12\log\bigl(2\pi\sigma^2\bigr),
$$
trong đó $\pi$ ở hạng cuối là hằng số $3{,}14\ldots$; hạng này không phụ thuộc $\theta$ vì $\sigma$ cố định.

**Bước 2 (quy tắc dây chuyền).** $\nabla_\theta\mu_\theta(s)=\phi(s)$, nên
$$
\begin{aligned}
\nabla_\theta\log\pi_\theta(a\mid s)
&=-\frac{2\bigl(a-\mu_\theta(s)\bigr)}{2\sigma^2}\cdot\bigl(-\nabla_\theta\mu_\theta(s)\bigr)\\
&=\frac{a-\mu_\theta(s)}{\sigma^2}\,\phi(s).\qquad\square
\end{aligned}
$$
:::

Hàm điểm Gaussian là đặc trưng trạng thái nhân với phần dư chuẩn hóa $\bigl(a-\mu_\theta(s)\bigr)/\sigma^2$. Hai hệ quả đọc được ngay. Thứ nhất, hướng: bước $\Delta\theta=\alpha\,\psi_\theta(s,a)$ đổi trung bình tại $s$ một lượng $\phi(s)^\top\Delta\theta=\alpha\,\tfrac{a-\mu_\theta(s)}{\sigma^2}\lVert\phi(s)\rVert^2$, cùng dấu với $a-\mu_\theta(s)$: trung bình dời về phía hành động đã lấy mẫu. Thứ hai, độ lớn: hàm điểm tỉ lệ với $1/\sigma^2$, nên chính sách ít ngẫu nhiên cho hàm điểm lớn và ước lượng gradient có phương sai lớn. Mệnh đề 09.17 kiểm lại được trực tiếp: $\mathbb E[A-\mu_\theta(s)]=0$, nên $\mathbb E[\psi_\theta(s,A)]=0$.

::: example Ví dụ 09.16 (Hàm điểm Gaussian tại $a=1{,}5$)
**Dữ kiện.** $\phi(s)=(1;\,2)$, $\theta=(0;\,0)$ nên $\mu_\theta(s)=0$; $\sigma^2=1$; hành động lấy mẫu $a=1{,}5$.

**Hàm điểm.** $\psi_\theta(s,a)=\dfrac{1{,}5-0}{1}(1;\,2)=(1{,}5;\,3)$.

**Một bước với hệ số.** Xét bước $\Delta\theta=\alpha c\,\psi_\theta(s,a)$ với $\alpha=0{,}1$. Độ dời trung bình là $\phi(s)^\top\Delta\theta=0{,}1\cdot c\cdot(1\cdot1{,}5+2\cdot3)=0{,}75\,c$. Với $c=1$: $\mu_\theta(s)$ tăng lên $0{,}75$, về phía $a$. Với $c=-1$: $\mu_\theta(s)$ giảm xuống $-0{,}75$, ra xa $a$.

**Kiểm tra lại.** Theo công thức tổng quát, độ dời là $\alpha c\,(a-\mu)\lVert\phi(s)\rVert^2/\sigma^2=0{,}1\cdot c\cdot1{,}5\cdot5=0{,}75\,c$.
:::

Ở Mục 6, hệ số $c$ là lợi tức của lượt: lợi tức dương kéo trung bình về phía hành động vừa thử, lợi tức âm đẩy trung bình ra xa.

Bài giảng gốc (trang 38) hỏi vấn đề của chính sách Gaussian. Có hai câu trả lời có cơ sở. Mật độ dương trên cả trục số, nên với miền hành động bị chặn, mẫu phải được cắt hoặc biến đổi (Mục 4 nêu cách tính hàm điểm cho từng cách). Phương sai $\sigma^2$ cố định không học được mức thăm dò; học $\sigma$ được xét ở Bài tập 09.7.

::: remark Nhận xét 09.19 (Nhầm lẫn thường gặp về hàm điểm)
1. "Hàm điểm là gradient của $J$." Sai: $\psi_\theta(s,a)$ là gradient của log xác suất của một hành động; gradient của $J$ cần thêm trọng số là phần thưởng hay lợi tức, và lấy kỳ vọng.
2. "Hàm điểm có kỳ vọng $0$ nên vô ích." Sai: kỳ vọng của $f(A)\psi_\theta(s,A)$ khác $0$ khi $f$ phụ thuộc hành động; trên bài toán một bước, $\mathbb E[r(A)\psi_\theta(s,A)]=\tfrac23\cdot3\bigl(\tfrac13;\,-\tfrac13\bigr)=\bigl(\tfrac23;\,-\tfrac23\bigr)$, đúng gradient tính ở trên.
3. "Hàm điểm softmax là $\phi(s,a)$." Sai: thiếu hạng trừ đặc trưng trung bình; khi đó trung bình theo chính sách khác $0$, và bước cập nhật luôn đẩy về hướng đặc trưng trung bình.
4. "Mệnh đề 09.17 đúng với mọi dữ liệu." Sai: kỳ vọng lấy theo $A\sim\pi_\theta(\cdot\mid s)$; hành động sinh từ một chính sách khác không cho trung bình $0$.
:::

**Trong thực hành.** Trong một cài đặt, hàm điểm hiếm khi được viết ra thành công thức. Mạng chính sách trả về các logit $\phi(s,a)^\top\theta$ (hoặc đầu ra của mạng) hay trung bình $\mu_\theta(s)$; thư viện tính $\log\pi_\theta(a\mid s)$ của hành động đã lấy mẫu, và phép vi phân tự động lan truyền ngược qua mạng cho $\psi_\theta(s,a)$. Khi đặc trưng là các lớp ẩn được học, đó chính là quy tắc dây chuyền mà Mệnh đề 09.16 bỏ qua. Log xác suất softmax nên tính bằng hàm log-softmax, dựa trên phép trừ cực đại trong $\log\sum e^{z}$, để tránh tràn số. Gán logit $-\infty$ cho các hành động không hợp lệ ở một trạng thái giữ miền hỗ trợ cố định theo $\theta$, nên Mệnh đề 09.17 vẫn áp dụng. Với xấp xỉ hàm hay quan sát không Markov, hàm điểm vẫn xác định, vì nó chỉ phụ thuộc chính sách; giả thiết dễ bị vi phạm nhất là dữ liệu: hành động lấy từ bộ nhớ phát lại do các chính sách cũ sinh ra không có phân phối $\pi_\theta(\cdot\mid s)$, nên Mệnh đề 09.17 và các ước lượng ở Mục 6 không còn đúng nếu không hiệu chỉnh.

Như vậy, Định nghĩa 09.14 biến việc học chính sách thành bài toán cực đại hóa $J(\theta)$, lợi tức kỳ vọng từ trạng thái đầu, và bước tăng gradient $\theta\leftarrow\theta+\alpha\nabla_\theta J$ làm $J$ tăng khi bước đủ nhỏ; trên bài toán một bước, $J=2$ và $\nabla_\theta J=\bigl(\tfrac23;\,-\tfrac23\bigr)$. Sai phân hữu hạn chỉ cần đo $J$ nhưng tốn $d+1$ nhóm lượt cho mỗi gradient và có phương sai tỉ lệ với $1/(n\epsilon^2)$; với $n=100$ lượt và $\epsilon=0{,}1$, độ lệch chuẩn khoảng $2$ so với giá trị $\tfrac23$. Hàm điểm (Định nghĩa 09.15) viết $\nabla_\theta\pi=\pi\,\psi_\theta$, nên một tổng theo hành động thành kỳ vọng theo hành động lấy mẫu; Mệnh đề 09.16 và 09.18 cho công thức đóng với softmax và Gaussian, và Mệnh đề 09.17 cho trung bình của hàm điểm bằng $0$ khi miền hỗ trợ cố định. Còn thiếu hai điều. Hàm điểm là của một bước, còn một lượt có nhiều bước, và trạng thái ở bước sau phụ thuộc hành động ở bước trước. Phép đổi đạo hàm với kỳ vọng trên cả lượt cũng cần giả thiết về môi trường. Mục 6 viết xác suất của cả lượt, lấy gradient của nó bằng tổng các hàm điểm, và nêu các giả thiết để đổi đạo hàm với kỳ vọng.

*Nguồn: bài giảng gốc lecture09-ddqn-and-policy-gradient-part1.pdf (2025–2026), trang 30–38; Sutton và Barto (2018), §13.1–13.3, §13.7; ghi chú bài giảng Bài 08, Định nghĩa 08.16.*

---

## 6. Gradient chính sách và REINFORCE

Mục 5 cho hàm điểm $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$ của một bước, có kỳ vọng $0$ theo hành động (Mệnh đề 09.17), và cho gradient đúng $\bigl(\tfrac23;\,-\tfrac23\bigr)$ của bài toán một bước. Một lượt thường có nhiều bước, và trạng thái ở bước sau phụ thuộc hành động ở bước trước, nên gradient của $J$ không là tổng của các gradient một bước tính riêng. Chúng ta viết $J$ thành kỳ vọng trên cả quỹ đạo, lấy gradient bằng phép biến đổi tỉ số xác suất, bỏ các hạng có kỳ vọng $0$, và phát biểu kết quả thành định lý gradient chính sách cùng các giả thiết của nó. Thuật toán REINFORCE là cách lấy mẫu trực tiếp vế phải của định lý.

<!-- note-topic-id: lec-09-topic-10 -->
### Tỉ số xác suất và xác suất của quỹ đạo

Trên bài toán một bước, $J(\theta)=\sum_ar(a)\pi_\theta(a\mid s)$. Dùng $\nabla_\theta\pi_\theta=\pi_\theta\psi_\theta$ của Mục 5, gradient thành một kỳ vọng theo hành động lấy mẫu.

::: example Ví dụ 09.17 (Gradient của bài toán một bước bằng hàm điểm)
**Dữ kiện.** Bài toán một bước, chính sách softmax, $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$, $r(1)=3$, $r(2)=0$; $\psi_\theta(s,1)=\bigl(\tfrac13;\,-\tfrac13\bigr)$, $\psi_\theta(s,2)=\bigl(-\tfrac23;\,\tfrac23\bigr)$ (Ví dụ 09.15).

**Tính.** $\nabla_\theta J=\sum_ar(a)\pi_\theta(a\mid s)\psi_\theta(s,a)=\tfrac23\cdot3\bigl(\tfrac13;\,-\tfrac13\bigr)+\tfrac13\cdot0\cdot\bigl(-\tfrac23;\,\tfrac23\bigr)=\bigl(\tfrac23;\,-\tfrac23\bigr)$.

**Kiểm tra lại.** Trùng vế phải của Ví dụ 09.14 và gradient tính trực tiếp ở Mục 5, và gần thương sai phân $0{,}655$ của Ví dụ 09.13; hạng của hành động 2 bằng $0$ vì $r(2)=0$.
:::

Với nhiều bước, đối tượng được lấy mẫu là cả lượt.

::: definition Định nghĩa 09.20 (Quỹ đạo và xác suất quỹ đạo)
Một quỹ đạo (trajectory) là dãy $\tau=(S_0,A_0,R_1,S_1,A_1,\dots,R_T,S_T)$ sinh bởi $S_0\sim\rho_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$ và $(S_{t+1},R_{t+1})\sim P(\cdot\mid S_t,A_t)$, dừng tại bước kết thúc $T$. Xác suất (hoặc mật độ) của quỹ đạo dưới $\pi_\theta$ là
$$
p_\theta(\tau)=\rho_0(S_0)\prod_{t=0}^{T-1}\pi_\theta(A_t\mid S_t)\,P(S_{t+1},R_{t+1}\mid S_t,A_t).
$$
:::

Công thức nhân là quy tắc dây chuyền của xác suất cùng tính Markov: mỗi thừa số chỉ phụ thuộc trạng thái và hành động ngay trước nó. Lợi tức $G_0(\tau)=\sum_{t=0}^{T-1}\gamma^tR_{t+1}$ là một hàm của quỹ đạo; khi $\tau$ cố định, $G_0(\tau)$ không phụ thuộc $\theta$. Do đó $J(\theta)=\int G_0(\tau)\,p_\theta(\tau)\,\mathrm d\tau$, với tích phân là tổng khi mọi thành phần rời rạc, và $\theta$ chỉ đi vào qua $p_\theta$. Nếu đổi được $\nabla_\theta$ với tích phân,
$$
\nabla_\theta J(\theta)=\int G_0(\tau)\,\nabla_\theta p_\theta(\tau)\,\mathrm d\tau=\mathbb E_{\tau\sim p_\theta}\bigl[G_0(\tau)\,\nabla_\theta\log p_\theta(\tau)\bigr],
$$
trong đó đẳng thức thứ hai dùng $\nabla_\theta p_\theta=p_\theta\nabla_\theta\log p_\theta$ trên tập $p_\theta>0$. Thương $\nabla_\theta p_\theta/p_\theta$ cho cách viết này tên gọi tỉ số xác suất (likelihood ratio). Ví dụ 09.17 là trường hợp $T=1$.

::: lemma Bổ đề 09.21 (Gradient của log xác suất quỹ đạo)
**Giả thiết.** $\rho_0$ và $P$ không phụ thuộc $\theta$; $\pi_\theta(A_t\mid S_t)>0$ và khả vi theo $\theta$ tại mọi bước của $\tau$.

**Kết luận.** $\nabla_\theta\log p_\theta(\tau)=\sum_{t=0}^{T-1}\psi_t$, với $\psi_t=\psi_\theta(S_t,A_t)$.
:::

::: proof
Lấy logarit của Định nghĩa 09.20: $\log p_\theta(\tau)=\log\rho_0(S_0)+\sum_{t=0}^{T-1}\bigl[\log\pi_\theta(A_t\mid S_t)+\log P(S_{t+1},R_{t+1}\mid S_t,A_t)\bigr]$. Hạng đầu và các hạng $\log P$ không phụ thuộc $\theta$ nên có gradient $0$; mỗi hạng còn lại có gradient $\psi_t$. $\square$
:::

Bổ đề là lý do gradient chính sách học được mà không cần mô hình: $P$ có mặt trong $p_\theta(\tau)$ nhưng biến mất khỏi $\nabla_\theta\log p_\theta(\tau)$, nên mỗi số hạng chỉ cần trạng thái, hành động đã quan sát và công thức của chính sách. Ghép với tỉ số xác suất, $\nabla_\theta J=\mathbb E\bigl[G_0\sum_t\psi_t\bigr]$: mỗi hàm điểm được nhân với lợi tức của cả lượt. Phần thưởng đã nhận trước khi chọn $A_t$ không thể do $A_t$ gây ra, nên hạng tương ứng phải có kỳ vọng $0$.

Đặt lịch sử $H_t=(S_0,A_0,R_1,\dots,A_{t-1},R_t,S_t)$ và tách lợi tức tại bước $t$:
$$
G_0=G_{<t}+\gamma^tG_t,\qquad G_{<t}=\sum_{k=0}^{t-1}\gamma^kR_{k+1}.
$$
$G_{<t}$ xác định khi biết $H_t$. Khi biết $H_t$, hành động $A_t$ lấy từ $\pi_\theta(\cdot\mid S_t)$, nên theo Mệnh đề 09.17, $\mathbb E[\psi_t\mid H_t]=0$, và theo tính chất tháp của kỳ vọng có điều kiện,
$$
\mathbb E\bigl[G_{<t}\,\psi_t\bigr]=\mathbb E\bigl[G_{<t}\,\mathbb E[\psi_t\mid H_t]\bigr]=0.
$$
Lập luận chỉ dùng thứ tự thời gian và tính Markov của chính sách; nó không giả sử phần thưởng độc lập với hành động.

::: example Ví dụ 09.18 (Lượt hai bước)
**Dữ kiện.** Lượt dừng tại $T=2$, cùng trạng thái $s$ ở hai bước, chính sách softmax với $\theta=(\log2;\,0)$; $A_0=A_1=1$ nên $\psi_0=\psi_1=\psi=\bigl(\tfrac13;\,-\tfrac13\bigr)$; $R_1=1$, $R_2=2$, $\gamma=0{,}9$.

**Lợi tức.** $G_1=2$, $G_0=1+0{,}9\cdot2=2{,}8$ (Ví dụ 09.12).

**Ba ước lượng.** (i) Lợi tức của cả lượt: $G_0(\psi_0+\psi_1)=5{,}6\,\psi\approx(1{,}867;\,-1{,}867)$. (ii) Lợi tức từ bước $t$: $G_0\psi_0+\gamma G_1\psi_1=(2{,}8+1{,}8)\psi=4{,}6\,\psi\approx(1{,}533;\,-1{,}533)$. (iii) Bỏ $\gamma^t$: $G_0\psi_0+G_1\psi_1=4{,}8\,\psi$, xét ở Ví dụ 09.21.

**Phần chênh.** (i) − (ii) $=R_1\psi_1$: phần thưởng nhận trước $A_1$ nhân hàm điểm của $A_1$, kỳ vọng $0$. Hai ước lượng (i), (ii) khác nhau trên lượt này nhưng có cùng kỳ vọng.
:::

<!-- note-topic-id: lec-09-topic-11 -->
### Định lý gradient chính sách

Ba bước trên, tỉ số xác suất, Bổ đề 09.21 và việc bỏ phần thưởng quá khứ, cần các giả thiết sau. Chúng ta nêu một điều kiện đủ đơn giản, bao được hai họ chính sách của Mục 4.

- **(G1)** $\rho_0$ và $P$ không phụ thuộc $\theta$; trạng thái $S_t$ có tính Markov.
- **(G2)** Với mọi $s$, $\pi_\theta(\cdot\mid s)$ khả vi theo $\theta$ và có miền hỗ trợ không đổi theo $\theta$.
- **(G3)** $|R_{t+1}|\le R_{\max}$ và $T\le T_{\max}$ hầu chắc chắn.
- **(G4)** $\pi_\theta$ là chính sách softmax, hoặc chính sách Gaussian với $\sigma$ cố định, với đặc trưng bị chặn $\lVert\phi\rVert\le\Phi$.

::: theorem Định lý 09.22 (Gradient chính sách, dạng quỹ đạo)
**Giả thiết.** (G1)–(G4).

**Kết luận.**
$$
\nabla_\theta J(\theta)=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_\theta(S_t,A_t)\Bigr].
$$

**Điều kiện áp dụng.** Dữ liệu là các lượt sinh bởi chính $\pi_\theta$; lợi tức $G_t$ tính với cùng $\gamma$ như trong $J$; $T$ là bước kết thúc của MDP.

**Phạm vi.** Định lý nói về gradient tại một $\theta$, không nói về hội tụ của phép tăng gradient; (G3)–(G4) là điều kiện đủ, không cần.
:::

::: proof
**Bước 1 (viết theo quỹ đạo).** Theo Định nghĩa 09.20, $J(\theta)=\int G_0(\tau)p_\theta(\tau)\,\mathrm d\tau$, và $|G_0|\le T_{\max}R_{\max}$ theo (G3).

**Bước 2 (đổi đạo hàm với tích phân).** Với softmax và $T\le T_{\max}$, khi trạng thái và phần thưởng chỉ nhận hữu hạn giá trị, $J$ là một tổng hữu hạn các hàm khả vi, nên phép đổi hiển nhiên. Trường hợp tổng quát dùng định lý hội tụ bị chặn: theo (G4), trong một lân cận của $\theta$, $\lVert\nabla_\theta p_{\theta'}(\tau)\rVert=p_{\theta'}(\tau)\bigl\lVert\sum_t\psi_{\theta'}(S_t,A_t)\bigr\rVert$ bị chặn bởi một hàm khả tích của $\tau$; với softmax vì $\lVert\psi\rVert\le2\Phi$, với Gaussian vì mật độ có đuôi Gaussian còn $|a-\mu|$ chỉ tăng tuyến tính.

**Bước 3 (tỉ số xác suất).** $\nabla_\theta J=\mathbb E_{\tau\sim p_\theta}\bigl[G_0\nabla_\theta\log p_\theta(\tau)\bigr]$.

**Bước 4 (Bổ đề 09.21).** Theo (G1), (G2): $\nabla_\theta J=\mathbb E\bigl[G_0\sum_{t=0}^{T-1}\psi_t\bigr]$.

**Bước 5 (bỏ phần thưởng quá khứ).** Viết tổng đến $T_{\max}$ với chỉ thị $\mathbf 1\{t<T\}$; chỉ thị này xác định khi biết $H_t$ (trạng thái $S_t$ chưa kết thúc). Với mỗi $t$,
$$
\begin{aligned}
\mathbb E\bigl[\mathbf 1\{t<T\}\,G_0\,\psi_t\bigr]
&=\mathbb E\bigl[\mathbf 1\{t<T\}\,G_{<t}\,\psi_t\bigr]+\mathbb E\bigl[\mathbf 1\{t<T\}\,\gamma^tG_t\,\psi_t\bigr]\\
&=\mathbb E\bigl[\mathbf 1\{t<T\}\,G_{<t}\,\mathbb E[\psi_t\mid H_t]\bigr]+\mathbb E\bigl[\mathbf 1\{t<T\}\,\gamma^tG_t\,\psi_t\bigr]\\
&=\mathbb E\bigl[\mathbf 1\{t<T\}\,\gamma^tG_t\,\psi_t\bigr],
\end{aligned}
$$
vì $\mathbb E[\psi_t\mid H_t]=0$ theo Mệnh đề 09.17 áp dụng tại $S_t$. Cộng theo $t$ được kết luận. $\square$
:::

Định lý đọc như sau: hướng tăng của lợi tức kỳ vọng là trung bình, trên các lượt của chính sách hiện tại, của các hàm điểm, mỗi hàm điểm nhân với phần lợi tức đến sau nó và với trọng số $\gamma^t$. Mỗi giả thiết có vai trò riêng. (G1) được dùng ở Bước 4; nếu môi trường phụ thuộc $\theta$, chẳng hạn khi tham số cũng điều khiển phân phối trạng thái đầu, $\nabla\log p_\theta$ có thêm hạng của môi trường và kết luận sai. (G2) được dùng ở Bước 5 qua Mệnh đề 09.17; bỏ miền hỗ trợ cố định, phản ví dụ phân phối đều trên $[0,\theta]$ của Mục 5 cho $\mathbb E[\psi_t\mid H_t]\ne0$. (G3), (G4) chỉ được dùng ở Bước 2. Với $\gamma<1$, có thể bỏ $T\le T_{\max}$ khi $\lVert\psi_{\theta'}\rVert\le C$ đều trong một lân cận của $\theta$ (đúng với softmax). Viết $J=\sum_{t\ge0}\gamma^t\,\mathbb E\bigl[R_{t+1}\mathbf 1\{t<T\}\bigr]$; số hạng thứ $t$ là kỳ vọng trên $t+1$ bước đầu của lượt, nên khả vi theo Bước 2–4 với gradient có chuẩn không quá $(t+1)CR_{\max}$. Chuỗi các gradient bị chặn bởi $\sum_t\gamma^t(t+1)CR_{\max}<\infty$, nên hội tụ đều và được lấy đạo hàm từng số hạng (Sutton và cộng sự, 2000). Chặn $p_{\theta'}(\tau)$ trực tiếp trên cả lượt thì không đủ, vì tỉ số $p_{\theta'}(\tau)/p_\theta(\tau)$ có thể tăng theo hàm mũ của $T$. Trọng số $\gamma^t$ đến từ chính định nghĩa $J=\mathbb E[G_0]$: phần thưởng ở bước $k$ được chiết khấu $\gamma^k=\gamma^t\gamma^{k-t}$.

Thay $G_t$ bằng kỳ vọng có điều kiện của nó cho dạng thứ hai, dạng mà bài giảng gốc (trang 39) và Sutton và Barto (2018, §13.2) phát biểu.

::: corollary Hệ quả 09.23 (Gradient chính sách, dạng phân bố chiếm dụng)
**Giả thiết.** (G1)–(G4); chính sách Markov dừng; lượt kết thúc do MDP đi vào trạng thái hấp thụ, nơi $q_\pi=0$.

**Kết luận.** Với phân bố chiếm dụng chiết khấu $\nu^\pi_\gamma(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_{\pi_\theta}(S_t=s)$,
$$
\nabla_\theta J(\theta)=\frac{1}{1-\gamma}\,\mathbb E_{S\sim\nu^\pi_\gamma,\;A\sim\pi_\theta(\cdot\mid S)}\bigl[q_\pi(S,A)\,\psi_\theta(S,A)\bigr],\qquad\pi=\pi_\theta.
$$
:::

::: proof
**Bước 1.** Theo tính chất tháp và Bổ đề 03.20(d), $\mathbb E[G_t\psi_t]=\mathbb E\bigl[\mathbb E[G_t\mid S_t,A_t]\,\psi_t\bigr]=\mathbb E[q_\pi(S_t,A_t)\psi_t]$.

**Bước 2.** Gom theo trạng thái: $\sum_t\gamma^t\mathbb E[q_\pi(S_t,A_t)\psi_t]=\sum_s\Bigl(\sum_t\gamma^t\Pr(S_t=s)\Bigr)\sum_a\pi_\theta(a\mid s)q_\pi(s,a)\psi_\theta(s,a)$; tổng theo $t$ mở rộng tới vô hạn vì sau $T$ lượt ở trạng thái hấp thụ với $q_\pi=0$.

**Bước 3.** $\sum_t\gamma^t\Pr(S_t=s)=\nu^\pi_\gamma(s)/(1-\gamma)$. $\square$
:::

Đọc bằng lời, $\nu^\pi_\gamma(s)$ là tần suất thăm $s$ trên các lượt, mỗi lần thăm ở bước $t$ được tính với trọng số tỉ lệ $\gamma^t$, nên lần thăm ở bước muộn tính nhẹ hơn. Thừa số $1-\gamma$ trong $\nu^\pi_\gamma$ làm các trọng số $(1-\gamma)\gamma^t$ cộng lại bằng $1$, nên $\nu^\pi_\gamma$ là một phân phối; thừa số $1/(1-\gamma)$ ở trước bù lại. Nhiều tài liệu bỏ chuẩn hóa và viết $\nabla J\propto\sum_s\eta(s)\sum_aq_\pi(s,a)\nabla_\theta\pi_\theta(a\mid s)$, với $\eta(s)=\sum_t\gamma^t\Pr(S_t=s)$ không chuẩn hóa; hai cách khác nhau một hằng số dương.

<!-- note-topic-id: lec-09-topic-12 -->
### Thuật toán REINFORCE

Định lý 09.22 viết gradient thành một kỳ vọng theo lượt, nên một lượt chạy bằng $\pi_\theta$ cho một mẫu của nó. Bài giảng gốc (trang 40) gọi thuật toán lấy mẫu này là REINFORCE (Williams, 1992).

::: example Ví dụ 09.19 (Một cập nhật REINFORCE)
**Dữ kiện.** Bài toán một bước, chính sách softmax, $\theta=(\log2;\,0)$, $r(1)=3$, $r(2)=0$, $\alpha=0{,}1$. Lượt chọn $A_0=1$, nên $G_0=3$.

**Ước lượng.** $\widehat g=G_0\,\psi_\theta(s,1)=3\bigl(\tfrac13;\,-\tfrac13\bigr)=(1;\,-1)$.

**Cập nhật.** $\theta\leftarrow(\log2+0{,}1;\,-0{,}1)$; $\pi_\theta(1\mid s)=\dfrac{2e^{0{,}1}}{2e^{0{,}1}+e^{-0{,}1}}=\dfrac{2}{2+e^{-0{,}2}}\approx0{,}710$.

**Kiểm tra lại.** Nếu lượt chọn $A_0=2$, $G_0=0$ và $\widehat g=0$. Kỳ vọng: $\tfrac23(1;\,-1)+\tfrac13\cdot0=\bigl(\tfrac23;\,-\tfrac23\bigr)=\nabla_\theta J$.
:::

::: algorithm Thuật toán 09.24 (REINFORCE)
**Đầu vào.** Chính sách tham số hóa $\pi_\theta$ khả vi; bước học $\alpha>0$; $\gamma\in[0,1)$; số lượt $N$.

**Khởi tạo.** $\theta$ tùy ý.

**Với mỗi lượt $n=1,\dots,N$:**
1. $\theta_{\mathrm{old}}\leftarrow\theta$. Thu một lượt $S_0,A_0,R_1,\dots,S_T$ với $A_t\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid S_t)$; không đổi tham số trong khi thu.
2. $G_T=0$; với $t=T-1,\dots,0$: $G_t=R_{t+1}+\gamma G_{t+1}$.
3. $\widehat g=\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$.
4. $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\,\widehat g$.

**Đầu ra.** $\pi_\theta$ sau $N$ lượt.
:::

![Ba nút S 0, A 0; S 1, A 1; S 2, A 2 nối bằng mũi tên ghi R 1, R 2, R 3; hành động lấy mẫu từ pi theta old, giữ cố định cả lượt. Mũi tên cong đi ngược từ cuối lượt về đầu: G t bằng R t cộng 1 cộng gamma G t cộng 1. Hộp bên phải: g mũ bằng tổng gamma mũ t G t psi t, cập nhật theta một lần.](img/lec-09/reinforce-trajectory.svg)

Hình vẽ thứ tự tính của một lượt: thu cả lượt với tham số cố định, tính lợi tức lùi từ cuối lượt, cộng các đóng góp rồi cập nhật một lần. Lợi tức phải tính lùi vì $G_t$ cần mọi phần thưởng sau bước $t$; do đó REINFORCE chỉ cập nhật khi lượt đã kết thúc. Sutton và Barto (2018, §13.3) cập nhật $\theta$ ngay theo từng $t$ sau khi lượt kết thúc; hai biến thể khác nhau ở bậc $\alpha^2$.

::: corollary Hệ quả 09.25 (REINFORCE là ước lượng không chệch)
**Giả thiết.** (G1)–(G4); lượt ở bước 1 của Thuật toán 09.24 sinh bởi $\pi_{\theta_{\mathrm{old}}}$.

**Kết luận.** $\mathbb E\bigl[\widehat g\mid\theta_{\mathrm{old}}\bigr]=\nabla_\theta J(\theta_{\mathrm{old}})$.
:::

Hệ quả là Định lý 09.22 tại $\theta_{\mathrm{old}}$, vì $\widehat g$ là đúng biểu thức trong kỳ vọng, tính trên một lượt. Nó cần hai điều mà thuật toán phải giữ. Thứ nhất, mọi hàm điểm tính tại tham số đã sinh ra lượt; cập nhật $\theta$ giữa chừng làm các bước sau của lượt đến từ chính sách khác. Thứ hai, lượt phải do $\pi_{\theta_{\mathrm{old}}}$ sinh ra: REINFORCE là học theo chính sách (on-policy). Các lượt cũ trong một bộ nhớ phát lại do tham số khác sinh ra, nên trung bình của $\widehat g$ trên chúng không còn là $\nabla J(\theta_{\mathrm{old}})$ nếu không nhân với tỉ số $p_{\theta_{\mathrm{old}}}(\tau)/p_{\theta'}(\tau)$. Đây là khác biệt cơ bản với DQN và Double DQN, vốn học khác chính sách từ bộ nhớ phát lại.

Không chệch không có nghĩa là chính xác. Ước lượng dùng lợi tức Monte Carlo của cả lượt, nên phương sai của nó có thể lớn.

::: example Ví dụ 09.20 (Phương sai của REINFORCE trên bài toán một bước)
**Dữ kiện.** Như Ví dụ 09.19.

**Phân phối của $\widehat g$.** $(1;\,-1)$ với xác suất $\tfrac23$; $(0;\,0)$ với xác suất $\tfrac13$. Kỳ vọng $\bigl(\tfrac23;\,-\tfrac23\bigr)$.

**Phương sai.** Mỗi tọa độ: $\tfrac23\cdot1-\tfrac49=\tfrac29$. Tổng phương sai $\tfrac49$, trong khi $\lVert\nabla_\theta J\rVert^2=\tfrac89$.

**Diễn giải.** Một lượt cho độ lệch chuẩn khoảng $0{,}67$ so với độ dài gradient khoảng $0{,}94$; muốn sai số nhỏ, cần trung bình trên nhiều lượt.
:::

Phương sai còn phụ thuộc vào cách đo phần thưởng, dù gradient thì không: cộng cùng một hằng vào mọi phần thưởng không đổi $\nabla J$ trên bài toán một bước (vì $\sum_a\nabla\pi_\theta(a\mid s)=0$) nhưng thay đổi phương sai (Bài tập 09.9). Bài 10 dùng tính chất này để giảm phương sai bằng một đường cơ sở (baseline).

Nhiều cài đặt dùng $\sum_tG_t\psi_t$ thay cho $\sum_t\gamma^tG_t\psi_t$. Khi $\gamma<1$, kỳ vọng của ước lượng này nói chung không bằng $\nabla J$, và Nota và Thomas (2020) chỉ ra rằng nó nói chung không là gradient của hàm mục tiêu nào. Hai ước lượng trùng nhau khi $\gamma=1$. Lý do thường nêu: trọng số $\gamma^t$ làm các bước cuối của lượt dài gần như không đóng góp. Khi dùng, cần biết rằng hướng cập nhật không còn là gradient của $J$.

Ví dụ sau cho thấy hướng lệch trên một bài toán nhỏ.

::: example Ví dụ 09.21 (Bỏ $\gamma^t$ trên hai trạng thái)
**Dữ kiện.** Lượt hai bước: $S_0=s_A$, $S_1=s_B$ bất kể hành động, dừng tại $T=2$. Mỗi trạng thái có chính sách softmax hai hành động riêng với đặc trưng đơn vị và tham số riêng $\theta^A$, $\theta^B$, cả hai bằng $(\log2;\,0)$; phần thưởng $r(1)=3$, $r(2)=0$ ở cả hai trạng thái; $\gamma=0{,}9$. Đặt $g=\bigl(\tfrac23;\,-\tfrac23\bigr)$, gradient của bài toán một bước.

**Gradient đúng.** $J=\mathbb E[R_1]+\gamma\,\mathbb E[R_2]$; $R_1$ chỉ phụ thuộc $\theta^A$, $R_2$ chỉ phụ thuộc $\theta^B$. Vậy $\nabla J=(g;\,\gamma g)=(0{,}667;\,-0{,}667;\,0{,}6;\,-0{,}6)$.

**Định lý 09.22.** $\mathbb E[G_0\psi_0]=\mathbb E[R_1\psi_0]+\gamma\,\mathbb E[R_2\psi_0]=g+0$ (vì $A_1$ độc lập với $A_0$), $\mathbb E[\gamma G_1\psi_1]=\gamma g$: đúng $(g;\,\gamma g)$.

**Bỏ $\gamma^t$.** $\mathbb E[G_0\psi_0+G_1\psi_1]=(g;\,g)$. Góc giữa $(g;\,g)$ và $(g;\,\gamma g)$ có $\cos=\dfrac{1+\gamma}{\sqrt2\sqrt{1+\gamma^2}}\approx0{,}9986$, tức khoảng $3^\circ$: hướng lệch, trạng thái muộn được tính nặng hơn mức $J$ yêu cầu.
:::

::: remark Nhận xét 09.26 (Nhầm lẫn thường gặp về gradient chính sách)
1. "Định lý gradient chính sách cần biết $P$." Sai: $P$ biến mất khỏi $\nabla\log p_\theta$ (Bổ đề 09.21); nó chỉ cần các lượt sinh bởi $P$.
2. "Bỏ được phần thưởng quá khứ vì phần thưởng độc lập với hành động." Sai: lý do là thứ tự thời gian, $\mathbb E[\psi_t\mid H_t]=0$; phần thưởng sau $A_t$ phụ thuộc $A_t$ và không bỏ được.
3. "Không chệch nên mỗi cập nhật làm $J$ tăng." Sai: trong Ví dụ 09.19, một lượt chọn hành động 2 cho $\widehat g=0$; với lợi tức âm do nhiễu, một cập nhật có thể làm $J$ giảm.
:::

**Trong thực hành.** Trong một cài đặt, $\widehat g$ không được ghép từ các hàm điểm viết tay. Ta lưu $\log\pi_\theta(A_t\mid S_t)$ của mỗi bước trong khi thu lượt, tính các $G_t$ lùi như hằng số không nhận gradient, rồi để phép vi phân tự động lấy gradient của hàm mất mát thay thế
$$
L(\theta)=-\sum_{t=0}^{T-1}\gamma^tG_t\,\log\pi_\theta(A_t\mid S_t),
$$
có $-\nabla_\theta L=\widehat g$; dấu trừ đổi bước hạ gradient của thư viện thành bước tăng $J$. Hàm này không phải hàm mục tiêu: giá trị của nó không đo chất lượng chính sách, chỉ gradient của nó có nghĩa. Lấy trung bình $\widehat g$ trên vài lượt trước mỗi cập nhật làm giảm phương sai mà không làm mất tính không chệch. Với xấp xỉ hàm bằng mạng nơ-ron, (G4) được thay bằng điều kiện gradient của logit hoặc của trung bình theo $\theta$ bị chặn trên miền trạng thái; khi đó hàm điểm vẫn bị chặn (softmax) hoặc có đuôi Gaussian; với quan sát không Markov, chính sách theo quan sát vẫn có Định lý 09.22 theo lượt, nhưng Hệ quả 09.23 với $q_\pi(s,a)$ không còn áp dụng. Với CartPole, lượt bị cắt ở bước $500$ (Bài 08) cho $G_t$ cụt: ước lượng khi đó nhắm bài toán có chân trời hữu hạn.

Như vậy, Định lý 09.22 viết gradient của $J$ thành kỳ vọng trên các lượt của $\pi_\theta$, trong đó mỗi hàm điểm nhân với lợi tức đến sau nó, và REINFORCE (Thuật toán 09.24) lấy mẫu kỳ vọng đó mà không cần $P$, không chệch dưới (G1)–(G4). Còn hai giới hạn: phương sai của ước lượng lớn và tăng khi cộng một hằng vào phần thưởng ($\tfrac49$ thành $\tfrac{16}9$ trên bài toán một bước), còn dữ liệu phải theo chính sách nên mỗi lượt chỉ dùng cho một cập nhật. Bài 10 giảm phương sai bằng đường cơ sở và bằng phương pháp actor–critic, trong đó một hàm giá trị học được thay cho lợi tức Monte Carlo.

*Nguồn: bài giảng gốc lecture09-ddqn-and-policy-gradient-part1.pdf (2025–2026), trang 39–40; Williams (1992); Sutton và cộng sự (2000); Sutton và Barto (2018), §13.2–13.3; Nota và Thomas (2020).*

---

## 7. Tổng kết và chuyển tiếp

<!-- note-topic-id: lec-09-topic-13 -->
### Kết quả và giả thiết của bài

Chúng ta gom các kết quả của Mục 2 đến Mục 6 vào một bảng. Mỗi hàng đặt một kết quả cạnh giả thiết mà thiếu nó thì công thức sai nghĩa hoặc kết luận vượt quá bằng chứng.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Độ chệch của phép cực đại (Mệnh đề 09.2) | $\mathcal A$ hữu hạn; mỗi $\widehat Q_a$ khả tích và không chệch cho $q_a$ | $\mathbb E[\max_a\widehat Q_a]\ge\max_aq_a$; bằng nhau khi và chỉ khi một hành động tốt nhất luôn thắng |
| Ước lượng kép (Mệnh đề 09.4) | bản đánh giá $\widehat Q^B$ không chệch, độc lập với bản chọn $\widehat Q^A$ | $\mathbb E[\widehat Q^B_{a^*}]\le\max_aq_a$; có thể chệch âm |
| Mục tiêu Double DQN (Thuật toán 09.5) | $Z_i$ chỉ ghi kết thúc của MDP; $\theta^-$ cố định giữa hai lần đồng bộ; mục tiêu trong $\operatorname{sg}$ | $y_i=R_i+\gamma(1-Z_i)Q_{\theta^-}(S'_i,a_i^*)$, $a_i^*=\arg\max_aQ_\theta(S'_i,a)$ |
| Double Q-learning (Thuật toán 09.7) | mỗi bước cập nhật một bảng; bảng kia đánh giá; hành vi theo $Q_1+Q_2$ | $Q_1(S,A)\leftarrow Q_1(S,A)+\alpha\bigl[R+\gamma(1-Z)Q_2(S',a^*)-Q_1(S,A)\bigr]$ |
| Chính sách tham số hóa (Định nghĩa 09.10–09.12) | $\pi_\theta$ khả vi; xác suất khi $\mathcal A$ hữu hạn, mật độ khi $\mathcal A=\mathbb R$ | softmax $\propto e^{\phi(s,a)^\top\theta}$; Gaussian $\mathcal N(\phi(s)^\top\theta,\sigma^2)$ |
| Hàm điểm (Định nghĩa 09.15, Mệnh đề 09.16–09.18) | $\pi_\theta(a\mid s)>0$; $\phi$, $\sigma$ cố định; miền hỗ trợ cố định cho kỳ vọng | $\psi_\theta=\phi(s,a)-\sum_b\pi_\theta(b\mid s)\phi(s,b)$; $\psi_\theta=\tfrac{a-\mu_\theta(s)}{\sigma^2}\phi(s)$; $\mathbb E[\psi_\theta(s,A)]=0$ |
| Định lý gradient chính sách (Định lý 09.22, Hệ quả 09.23) | (G1)–(G4); dạng phân bố chiếm dụng cần thêm lượt kết thúc do MDP | $\nabla_\theta J=\mathbb E\bigl[\sum_t\gamma^tG_t\psi_t\bigr]=\tfrac1{1-\gamma}\mathbb E_{\nu^\pi_\gamma,\pi_\theta}[q_{\pi_\theta}\psi_\theta]$ |
| REINFORCE (Thuật toán 09.24, Hệ quả 09.25) | lượt sinh bởi $\pi_{\theta_{\mathrm{old}}}$; giữ $\theta_{\mathrm{old}}$ cố định cả lượt; giữ $\gamma^t$ | $\widehat g=\sum_t\gamma^tG_t\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$, $\mathbb E[\widehat g]=\nabla_\theta J(\theta_{\mathrm{old}})$ |

Bảng đọc theo hai nửa: bốn hàng đầu nói về giá trị của hành động được chọn trong mục tiêu bootstrap, bốn hàng sau nói về gradient của lợi tức kỳ vọng theo tham số chính sách.

### So sánh bốn phương pháp

Bài có bốn phương pháp học từ mẫu: DQN của Bài 08 (Thuật toán 08.13), Double DQN, Double Q-learning và REINFORCE. Ba phương pháp đầu học giá trị hành động và suy ra chính sách bằng phép cực đại; phương pháp cuối học trực tiếp chính sách.

| Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng |
|---|---|---|---|
| DQN (Thuật toán 08.13) | bước tối ưu trên $L_B$ với mục tiêu $R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(S'_i,a')$; đồng bộ $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu | mini-batch rút đều từ bộ nhớ phát lại; dữ liệu khác chính sách | sau $t_{\mathrm{end}}$ bước môi trường |
| Double DQN (Thuật toán 09.5) | như DQN, mục tiêu $R_i+\gamma(1-Z_i)Q_{\theta^-}(S'_i,a_i^*)$ | như DQN | như DQN |
| Double Q-learning (Thuật toán 09.7) | đồng xu chọn bảng được cập nhật; bảng đó chọn $a^*$, bảng kia đánh giá; đổi một ô | mẫu chuyển vừa thu, dùng một lần; hành vi theo $Q_1+Q_2$ | sau số lượt định trước |
| REINFORCE (Thuật toán 09.24) | $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\sum_t\gamma^tG_t\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$, một lần mỗi lượt | một lượt sinh bởi $\pi_{\theta_{\mathrm{old}}}$, dùng cho đúng một cập nhật | sau $N$ lượt |

DQN và Double DQN khác nhau đúng ở một dòng mục tiêu; không điều kiện dừng nào ở bảng là tiêu chuẩn hội tụ, cả bốn là ngân sách.

| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Mục tiêu DQN | cùng một ước lượng chọn và đánh giá; mỗi ước lượng không chệch | phần bootstrap chệch lên hoặc bằng (Mệnh đề 09.2) |
| Double Q-learning | hai bảng xem như độc lập, bảng đánh giá không chệch; chỉ thỏa ở dạng lý tưởng | không chệch lên; có thể chệch âm (Mệnh đề 09.4, Ví dụ 09.5) |
| Double DQN | $\theta^-$ là bản sao trễ của $\theta$, nên không độc lập | gần thỏa điều kiện tách; không bảo đảm hết chệch lên, mức giảm phải đo bằng thí nghiệm |
| REINFORCE | (G1)–(G4); lượt theo $\pi_{\theta_{\mathrm{old}}}$ | $\widehat g$ không chệch cho $\nabla J(\theta_{\mathrm{old}})$; phương sai lớn |

Bảng thứ hai chỉ chứa kết luận về độ chệch. Chương không phát biểu định lý hội tụ nào cho bốn phương pháp; riêng DQN và Double DQN có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách nên không có bảo đảm hội tụ tổng quát (Nhận xét 08.21). Hai hàng giữa khác nhau ở mức độc lập: Mệnh đề 09.4 cần độc lập, Double Q-learning chỉ thỏa gần đúng vì mỗi bảng bootstrap từ bảng kia, còn Double DQN thỏa yếu hơn nữa vì mạng mục tiêu là một bản sao trễ của mạng trực tuyến.

### Trả lời vấn đề trung tâm

Bài toán của chương là xác định khi nào một ước lượng từ mẫu không chệch, cho hai đại lượng dùng để cập nhật: giá trị của hành động được chọn trong mục tiêu bootstrap, và gradient của $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ theo $\theta$. Mục 1 nêu trước một câu trả lời có điều kiện cho mỗi mục; các số đi kèm nằm ở Tóm tắt chương.

1. Khi mỗi $\widehat Q_a$ không chệch nhưng có nhiễu, phép cực đại chệch lên hoặc bằng, bằng nhau khi và chỉ khi một hành động tốt nhất luôn thắng (Mệnh đề 09.2).
2. Khi bản đánh giá không chệch và độc lập với bản chọn, giá trị báo cáo không chệch lên và có thể chệch âm (Mệnh đề 09.4); Double DQN chỉ gần thỏa điều kiện này, nên không bảo đảm hết chệch lên và mức giảm phải đo bằng thí nghiệm.
3. Khi tập hành động liên tục, hoặc khi đặc trưng gộp các trạng thái cần hành động khác nhau, cần học trực tiếp $\pi_\theta$; với ô xuất phát đều trên lưới gộp trạng thái, chính sách ngẫu nhiên tốt hơn mọi chính sách tất định theo đặc trưng (Ví dụ 09.9).
4. Khi $\pi_\theta(a\mid s)>0$ và khả vi, $\nabla_\theta\pi_\theta=\pi_\theta\psi_\theta$, và với miền hỗ trợ cố định, hàm điểm có kỳ vọng $0$ (Mệnh đề 09.17).
5. Dưới (G1)–(G4), $\nabla_\theta J=\mathbb E\bigl[\sum_t\gamma^tG_t\psi_t\bigr]$ và REINFORCE cho ước lượng không chệch từ mỗi lượt sinh bởi chính sách hiện tại (Định lý 09.22, Hệ quả 09.25).

Vì thế câu trả lời của chương là có điều kiện. Phép cực đại trên các ước lượng không chệch có nhiễu chệch lên hoặc bằng, và tách chọn khỏi đánh giá chỉ bỏ được độ chệch lên khi bản đánh giá độc lập. Gradient của lợi tức kỳ vọng có ước lượng không chệch từ mẫu khi môi trường không phụ thuộc tham số và dữ liệu theo đúng chính sách hiện tại (bài giảng gốc, trang 11–40; Sutton và Barto, 2018, §6.7, §13.1–13.3; van Hasselt, 2010; van Hasselt, Guez và Silver, 2016; Williams, 1992). Ước lượng không chệch đó có phương sai lớn, và đây là điểm xuất phát của Bài 10.

### Câu hỏi tự kiểm tra

Mỗi câu dưới đây dùng một kết quả của chương; khi trả lời, chúng ta nêu cả kết quả đã dùng.

1. Mỗi $\widehat Q_a$ không chệch thì $\max_a\widehat Q_a$ có không chệch cho $\max_aq_a$ không? Nói chung không: kỳ vọng của cực đại lớn hơn hoặc bằng giá trị đúng lớn nhất, và bằng nhau khi và chỉ khi một hành động tốt nhất luôn thắng phép cực đại (Mệnh đề 09.2). Với hai giá trị đúng bằng nhau và nhiễu $\pm1$, độ chệch là $\tfrac12$.
2. Double DQN có làm hai ước lượng độc lập không? Không. Mạng mục tiêu là bản sao trễ của mạng trực tuyến và hai mạng học trên cùng dữ liệu, nên giả thiết độc lập của Mệnh đề 09.4 chỉ thỏa gần đúng; Double DQN không bảo đảm hết chệch lên, và mức giảm phải đo bằng thí nghiệm (Nhận xét 09.6).
3. Trong MDP quan sát đầy đủ, khi nào vẫn cần chính sách ngẫu nhiên? Khi chính sách bị ràng buộc theo một đặc trưng gộp các trạng thái cần hành động khác nhau, như hai ô xám của Ví dụ 09.8. Nếu chính sách được phép phụ thuộc vào trạng thái đầy đủ, có một chính sách tối ưu tất định (Định lý 04.25, Nhận xét 09.9).
4. REINFORCE cần giả thiết nào về $\rho_0$, $P$ và về dữ liệu? $\rho_0$ và $P$ không phụ thuộc $\theta$, để $\nabla_\theta\log p_\theta(\tau)$ chỉ còn tổng các hàm điểm (Bổ đề 09.21); lượt phải sinh bởi chính $\pi_{\theta_{\mathrm{old}}}$ với tham số giữ cố định (Hệ quả 09.25).

Bài giảng gốc (trang 11 và 21) nêu thêm câu hỏi thảo luận về các vấn đề của DQN và về việc dùng bốn hay tám ước lượng. Câu thứ hai được trả lời một phần sau Ví dụ 09.5: độ chệch của mỗi cách tách phụ thuộc cách chọn, quan hệ giữa các bản và số mẫu mỗi bản nhận.

### Bài tập về nhà và tài liệu đọc

Mười bài tập của chương nằm ở mục "Bài tập củng cố" cuối tệp, xếp theo ba mức, mỗi bài có gợi ý và lời giải; học phần chưa có tệp bài tập riêng cho Bài 09. Theo mục: Bài tập 09.1 (mức nhận biết) và 09.2 dùng Mục 2; Bài tập 09.3 dùng Mục 3; Bài tập 09.4 dùng Mục 4; Bài tập 09.5–09.7 dùng Mục 5; Bài tập 09.8, 09.9 dùng Mục 6; Bài tập 09.10 là bài tổng hợp, đã giải trên trang chiếu. Bài tập 09.5 và 09.8 trùng bài tập trên trang chiếu của Mục 5 và 6, cùng bộ số và lời giải; bài tập trên trang chiếu của Mục 3 (mục tiêu DQN và Double DQN với $Q_{\theta^-}(S',\cdot)=(2;\,7)$, $Q_\theta(S',\cdot)=(4;\,1)$, $\gamma=0{,}8$) có lời giải ngay trên trang chiếu.

Tài liệu đọc gồm bốn mục của Sutton và Barto (2018): §6.7 về độ chệch của phép cực đại và học kép, §13.1 về chính sách tham số hóa, §13.2–13.3 về định lý gradient chính sách và REINFORCE, §13.7 về chính sách cho hành động liên tục; và bài báo của van Hasselt, Guez và Silver (2016) về Double DQN.

Bài 10 nhận giới hạn còn lại của REINFORCE, phương sai lớn: nó trừ một đường cơ sở (baseline) phụ thuộc trạng thái để giảm phương sai, thay lợi tức Monte Carlo bằng một hàm giá trị học được trong phương pháp actor–critic, rồi giới hạn độ lớn của mỗi bước cập nhật chính sách bằng TRPO và PPO.

## Tình huống áp dụng và ứng dụng

::: application Tình huống 09.1 (Double DQN trên Lunar Lander và Flappy Bird)
**Bài toán.** Notebook thực hành Bài 08 (`thuc-hanh-dqn-cartpole-lunarlander-flappybird.ipynb`) huấn luyện DQN trên `LunarLander-v3` và trên Flappy Bird. Cần biết thay mục tiêu DQN bằng mục tiêu Double DQN có làm chính sách tốt hơn không.

**Mô hình hóa.** Mục 15.2 của notebook cài đặt mục tiêu của Thuật toán 09.5, $y_i=R_i+\gamma(1-Z_i)\operatorname{sg}\bigl(Q_{\theta^-}(O'_i,a_i^*)\bigr)$ với $a_i^*=\arg\max_aQ_\theta(O'_i,a)$, và giữ mọi phần khác của Thuật toán 08.13. Ô kiểm bằng `assert` ở mục 15.2 cho lại hai mục tiêu $5{,}5$ và $4{,}6$ của Ví dụ 09.6.

**Kiểm giả thiết.**

- Mệnh đề 09.4 cần bản đánh giá độc lập với bản chọn: không thỏa, vì $\theta^-$ là bản sao trễ của $\theta$. Kết luận chỉ có thể là Double DQN gần thỏa điều kiện tách; nó không bảo đảm hết chệch lên, và mức giảm phải đo.
- Mệnh đề 09.2 cần các ước lượng không chệch: không thỏa, vì sai số của mạng sau một số bước huấn luyện hữu hạn nói chung không có kỳ vọng $0$.
- Mặt nạ chỉ dùng $Z$; cắt ngắn ở giới hạn bước vẫn bootstrap: thỏa, như Thuật toán 08.13.

**Áp dụng.** Bảng chọn cấu hình ở mục 15.4–15.5 của notebook, đo bằng tổng thưởng (Lunar Lander) hoặc số ống (Flappy Bird) của chính sách cuối trên $100$ lượt đánh giá, cho các số sau. Trên Lunar Lander với $10^5$ bước môi trường, Double DQN đạt trung bình $200{,}0$ trên năm hạt giống, cấu hình gốc đạt $205{,}4$ trên đúng năm hạt giống đó; hiệu ghép cặp $-5{,}4$, $t=-0{,}38$. Trên Flappy Bird với $3\cdot10^5$ bước, Double DQN đạt $39{,}8$ ống trên ba hạt giống so với $31{,}5$ của cấu hình gốc trên cùng hạt giống, $t=0{,}76$. Không hiệu nào phân biệt được ở mức $5\%$.

**Giới hạn.** Ba tới năm hạt giống không đủ để phân biệt các hiệu cỡ vài phần trăm; tổng thưởng của chính sách cuối không đo trực tiếp độ chệch của giá trị. Phép đo độ chệch theo van Hasselt, Guez và Silver (2016), so $\max_aQ_\theta(O_t,a)$ với lợi tức chiết khấu thực tế $G_t$ dọc các lượt đánh giá, là nhiệm vụ 1 ở mục 14 của notebook và chưa được thực hiện; Ví dụ 09.1 là phép đo đó cho DQN trên CartPole. Cấu hình tốt nhất trên Lunar Lander ($261{,}1$ trên tám hạt giống) gộp năm yếu tố: ngân sách gấp ba, lịch thăm dò dài gấp ba, tốc độ học giảm dần, lợi tức ba bước và Double DQN, nên không tách được đóng góp của Double DQN.
:::

::: application Tình huống 09.2 (REINFORCE trên dữ liệu của bộ nhớ phát lại: giả thiết không thỏa)
**Bài toán.** Một bản cài đặt muốn tiết kiệm lượt chạy bằng cách lưu các lượt cũ vào một bộ nhớ phát lại và tính $\widehat g$ của REINFORCE trên chúng, như DQN làm với mẫu chuyển.

**Kiểm giả thiết.** Hệ quả 09.25 cần lượt sinh bởi chính $\pi_{\theta_{\mathrm{old}}}$. Xét bài toán một bước với $r(1)=3$, $r(2)=0$, tham số hiện tại $\theta=(\log2;\,0)$, $\pi_\theta=\bigl(\tfrac23;\,\tfrac13\bigr)$, và các lượt trong bộ nhớ sinh bởi tham số cũ $\theta'=(0;\,0)$, $\pi_{\theta'}=\bigl(\tfrac12;\,\tfrac12\bigr)$. Trung bình của $\widehat g=r(A)\psi_\theta(s,A)$ trên các lượt cũ là $\tfrac12\cdot3\bigl(\tfrac13;\,-\tfrac13\bigr)=\bigl(\tfrac12;\,-\tfrac12\bigr)$, khác gradient đúng $\bigl(\tfrac23;\,-\tfrac23\bigr)$ tại $\theta$: hướng giữ nguyên trong ví dụ hai hành động này, nhưng độ lớn lệch $25\%$, và với nhiều hành động hay nhiều bước, hướng cũng lệch.

**Khắc phục.** Nhân mỗi lượt với tỉ số xác suất $p_\theta(\tau)/p_{\theta'}(\tau)$, ở đây $\pi_\theta(A\mid s)/\pi_{\theta'}(A\mid s)$, bằng $\tfrac43$ khi $A=1$: trung bình thành $\tfrac12\cdot\tfrac43\cdot3\bigl(\tfrac13;\,-\tfrac13\bigr)=\bigl(\tfrac23;\,-\tfrac23\bigr)$, đúng gradient. Trên lượt nhiều bước, tỉ số là tích theo các bước nên phương sai có thể tăng theo hàm mũ của độ dài lượt; Bài 10 dùng một tỉ số một bước có giới hạn trong PPO.
:::

**Ứng dụng.**

- **Bài 10** giữ định lý gradient chính sách của chương này, trừ một đường cơ sở để giảm phương sai, thay lợi tức Monte Carlo bằng một hàm giá trị học được (actor–critic), và giới hạn độ lớn bước cập nhật bằng TRPO và PPO.
- **Kết hợp các cải tiến của DQN.** Mục tiêu Double DQN là một trong sáu thành phần của Rainbow, cùng với mạng dueling, lợi tức nhiều bước và phát lại ưu tiên (Hessel và cộng sự, 2018); notebook Bài 08 thử từng thành phần riêng ở mục 15.

## Tóm tắt chương

Mục tiêu bootstrap của DQN chứa một phép cực đại trên các ước lượng có nhiễu, và trên CartPole mạng báo $108{,}5$ cho một trạng thái mà mọi lợi tức không vượt $100$. Khi mỗi ước lượng không chệch, kỳ vọng của phép cực đại không nhỏ hơn giá trị đúng lớn nhất; với hai hành động có giá trị bằng nhau và nhiễu $\pm1$, độ chệch là $\tfrac12$. Chọn bằng một bản và đánh giá bằng một bản độc lập, không chệch thì không còn chệch lên, có thể chệch âm $-0{,}125$; trên cùng mẫu chuyển, Double DQN cho mục tiêu $4{,}6$ thay cho $5{,}5$, và Double Q-learning đổi một ô từ $4$ thành $4{,}06$. Các phương pháp này suy chính sách bằng $\arg\max$, nên trên lưới gộp trạng thái mọi chính sách tất định theo đặc trưng có ô kẹt, còn chính sách ngẫu nhiên $\tfrac12$ cần trung bình $3{,}8$ bước. Học trực tiếp $\pi_\theta$ cần gradient của $J$: sai phân hữu hạn cần $d+1$ giá trị $J$ và có độ lệch chuẩn khoảng $2$ với $100$ lượt mỗi giá trị, còn hàm điểm viết gradient thành kỳ vọng theo lượt. Dưới (G1)–(G4), định lý gradient chính sách cho $\nabla J=\mathbb E[\sum_t\gamma^tG_t\psi_t]$, và REINFORCE lấy mẫu kỳ vọng này không chệch; một cập nhật với lợi tức $3$ đưa $\pi_\theta(1\mid s)$ từ $\tfrac23$ lên $0{,}710$. Ước lượng đó có tổng phương sai $\tfrac49$ trên bài toán một bước, thành $\tfrac{16}9$ khi cộng $1$ vào mọi phần thưởng.

**Kết quả theo mục.**

- Mục 2: Định nghĩa 09.1 (độ chệch của phép cực đại), Mệnh đề 09.2 (độ chệch không âm, điều kiện dấu bằng).
- Mục 3: Mệnh đề 09.4 (ước lượng kép không chệch lên), Thuật toán 09.5 (Double DQN), Thuật toán 09.7 (Double Q-learning), Nhận xét 09.6 (phạm vi của Double DQN).
- Mục 4: Định nghĩa 09.10–09.12 (chính sách tham số hóa, softmax, Gaussian), Nhận xét 09.9 (chính sách tối ưu tất định và lớp chính sách bị gộp).
- Mục 5: Định nghĩa 09.14 (hàm mục tiêu), Định nghĩa 09.15 (hàm điểm), Mệnh đề 09.16–09.18 (hàm điểm softmax, kỳ vọng bằng $0$, hàm điểm Gaussian).
- Mục 6: Bổ đề 09.21, Định lý 09.22 (gradient chính sách), Hệ quả 09.23 (dạng phân bố chiếm dụng), Thuật toán 09.24 (REINFORCE), Hệ quả 09.25 (không chệch).

**Công thức cần nhớ.**

$$
\begin{aligned}
y_i^{\mathrm{DDQN}}&=R_i+\gamma(1-Z_i)\,Q_{\theta^-}\bigl(S'_i,\arg\max_aQ_\theta(S'_i,a)\bigr),\\
\psi_\theta(s,a)&=\nabla_\theta\log\pi_\theta(a\mid s),\qquad\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}[\psi_\theta(s,A)]=0,\\
\nabla_\theta J(\theta)&=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_\theta(S_t,A_t)\Bigr].
\end{aligned}
$$

**Giả thiết hay bị quên.** Bất đẳng thức của phép cực đại nói về kỳ vọng, không về từng hiện thực. Ước lượng kép cần độc lập; mạng mục tiêu không độc lập với mạng trực tuyến. Mặt nạ chỉ chứa cờ kết thúc, không chứa cờ cắt ngắn. Hàm điểm cần xác suất dương và miền hỗ trợ cố định. Định lý gradient chính sách cần môi trường không phụ thuộc tham số. REINFORCE cần lượt theo đúng chính sách hiện tại, tham số cố định trong cả lượt, và trọng số $\gamma^t$. Không có kết luận hội tụ nào trong chương này.

---

## Bài tập củng cố

Các bài tập dưới đây xếp theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Mọi bài có dữ kiện tự đủ; bài ở hai mức sau có gợi ý và lời giải.

### Mức nhận biết

Bốn câu hỏi của mục "Câu hỏi tự kiểm tra" ở Mục 7 cũng thuộc mức này; lời giải ngắn đặt ngay sau mỗi câu.

::: exercise Bài tập 09.1 (Phép cực đại trên ước lượng không chệch)
Tại một trạng thái kế, mỗi hành động $a$ có ước lượng $\widehat Q_a$ không chệch cho giá trị đúng $q_a$, với nhiễu khác $0$. (a) $\max_a\widehat Q_a$ có là ước lượng không chệch của $\max_aq_a$ không? Nêu kết quả đã dùng. (b) Nêu một trường hợp có dấu bằng.
:::

::: hint
Hàm $x\mapsto\max_ax_a$ lồi; xem điều kiện dấu bằng của Mệnh đề 09.2.
:::

::: solution
**Câu (a).** Nói chung không. Theo Mệnh đề 09.2, $\mathbb E[\max_a\widehat Q_a]\ge\max_a\mathbb E[\widehat Q_a]=\max_aq_a$, nên độ chệch không âm; với hai hành động có giá trị đúng bằng $0$ và nhiễu $\pm1$ độc lập, độ chệch là $\tfrac12$ (Ví dụ 09.2).

**Câu (b).** Dấu bằng khi một hành động tốt nhất luôn thắng phép cực đại, chẳng hạn $q=(3;\,0)$ với nhiễu $\pm1$: ước lượng của hành động 1 không nhỏ hơn $2$, của hành động 2 không lớn hơn $1$ (Ví dụ 09.3(ii)).

**Kiểm tra lại.** Nhầm lẫn thường gặp: suy từ "mỗi ước lượng không chệch" ra "cực đại không chệch"; phép cực đại là hàm phi tuyến của cả vector ước lượng.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 09.2 (Độ chệch khi một hành động tốt hơn)
Hai hành động có giá trị đúng $q_1=1$, $q_2=0$; nhiễu $\varepsilon_1$, $\varepsilon_2$ độc lập, mỗi biến bằng $-1$ hoặc $+1$ với xác suất $1/2$; $\widehat Q_a=q_a+\varepsilon_a$. Tính $\mathbb E[\max_a\widehat Q_a]$ và độ chệch $\beta$. Điều kiện dấu bằng của Mệnh đề 09.2(c) có thỏa không?
:::

::: hint
Liệt kê bốn cặp $(\widehat Q_1;\widehat Q_2)$ với $\widehat Q_1\in\{0;\,2\}$, $\widehat Q_2\in\{-1;\,1\}$, rồi lấy trung bình của cực đại.
:::

::: solution
**Liệt kê.** Bốn cặp đồng xác suất: $(0;-1)\to0$; $(0;1)\to1$; $(2;-1)\to2$; $(2;1)\to2$.

**Tính.** $\mathbb E[\max_a\widehat Q_a]=\tfrac14(0+1+2+2)=1{,}25$; $\max_aq_a=1$; $\beta=0{,}25$.

**Điều kiện dấu bằng.** Hành động có kỳ vọng lớn nhất là hành động 1, nhưng ở cặp $(0;1)$ hành động 2 thắng; điều kiện không thỏa, nên $\beta>0$, khớp với số tính được.

**Kiểm tra lại.** $\beta$ nằm giữa $0{,}375$ ở khoảng cách $0{,}5$ và $0$ ở khoảng cách $3$ của Ví dụ 09.3, đúng chiều giảm theo khoảng cách.
:::

::: exercise Bài tập 09.3 (Nhánh còn lại của Double Q-learning)
Dữ kiện như Ví dụ 09.7: $R=1$, $\gamma=0{,}9$, $Z=0$, $\alpha=0{,}1$, $Q_1(S',\cdot)=(3;\,6)$, $Q_2(S',\cdot)=(5;\,4)$; thêm $Q_2(S,A)=3$. Đồng xu chọn cập nhật $Q_2$. Tính $a^*$, mục tiêu, sai số và $Q_2(S,A)$ mới. So mục tiêu này với mục tiêu Q-learning một bảng nếu dùng $Q_2$ cho cả chọn lẫn đánh giá.
:::

::: hint
Bảng được cập nhật là $Q_2$, nên $Q_2$ chọn hành động và $Q_1$ đánh giá.
:::

::: solution
**Chọn.** $a^*=\arg\max_aQ_2(S',a)=1$ vì $5>4$.

**Mục tiêu.** $y_2=1+0{,}9\cdot Q_1(S',1)=1+0{,}9\cdot3=3{,}7$.

**Sai số và giá trị mới.** $3{,}7-3=0{,}7$; $Q_2(S,A)\leftarrow3+0{,}1\cdot0{,}7=3{,}07$.

**So sánh.** Dùng $Q_2$ cho cả hai việc: $1+0{,}9\cdot5=5{,}5$. Mục tiêu kép thấp hơn $1{,}8$.

**Kiểm tra lại.** $3{,}07$ nằm giữa giá trị cũ $3$ và mục tiêu $3{,}7$, đúng với một bước $\alpha=0{,}1$ đi về phía mục tiêu.
:::

::: exercise Bài tập 09.4 (Xác suất khác $\tfrac12$ ở ô xám)
Lưới năm ô của Mục 4: hàng trên gồm ô 1 đến ô 5, ô đích dưới ô 3, ô kẹt X dưới ô 1 và ô 5; mỗi bước đi một ô, gặp tường thì đứng yên. Ô 1 đi Đông, ô 3 đi Nam, ô 5 đi Tây; ở hai ô xám 2 và 4, vốn cùng đặc trưng, chính sách đi Đông với xác suất $p=0{,}8$ và Tây với xác suất $0{,}2$. Tính số bước kỳ vọng tới đích $h_2$, $h_4$ và trung bình của chúng; so với $p=\tfrac12$.
:::

::: hint
Dùng $h_2=2/p$ và $h_4=2/(1-p)$ từ Ví dụ 09.9.
:::

::: solution
**Tính.** $h_2=2/0{,}8=2{,}5$; $h_4=2/0{,}2=10$.

**Trung bình.** $\tfrac12(2{,}5+10)=6{,}25$, so với $4$ khi $p=\tfrac12$.

**Kiểm tra lại.** Công thức $\tfrac1{p(1-p)}=\tfrac1{0{,}16}=6{,}25$.
:::

::: exercise Bài tập 09.5 (Hàm điểm softmax và Gaussian)
(a) Chính sách softmax hai hành động với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ và $\theta=(0;\,\log3)$. Tính $\pi_\theta(\cdot\mid s)$, $\psi_\theta(s,1)$, $\psi_\theta(s,2)$, và kiểm $\mathbb E_{A\sim\pi_\theta}[\psi_\theta(s,A)]=0$.

(b) Chính sách Gaussian với $\phi(s)=(1;\,2)$, $\theta=(0;\,0)$, $\sigma^2=1$ và hành động lấy mẫu $a=-1$. Tính $\psi_\theta(s,a)$ và nêu bước theo hàm điểm dời $\mu_\theta(s)$ về phía nào.
:::

::: hint
(a) Mẫu số softmax là $e^0+e^{\log3}$; với đặc trưng là vector đơn vị, đặc trưng trung bình trùng vector xác suất. (b) Dùng Mệnh đề 09.18 rồi tính $\phi(s)^\top\psi_\theta(s,a)$.
:::

::: solution
**Câu (a).** $\pi_\theta(\cdot\mid s)=\bigl(\tfrac{1}{1+3};\,\tfrac{3}{1+3}\bigr)=\bigl(\tfrac14;\,\tfrac34\bigr)$, cũng là đặc trưng trung bình. $\psi_\theta(s,1)=(1;\,0)-\bigl(\tfrac14;\,\tfrac34\bigr)=\bigl(\tfrac34;\,-\tfrac34\bigr)$; $\psi_\theta(s,2)=(0;\,1)-\bigl(\tfrac14;\,\tfrac34\bigr)=\bigl(-\tfrac14;\,\tfrac14\bigr)$. Kỳ vọng: $\tfrac14\bigl(\tfrac34;\,-\tfrac34\bigr)+\tfrac34\bigl(-\tfrac14;\,\tfrac14\bigr)=\bigl(\tfrac3{16}-\tfrac3{16};\,-\tfrac3{16}+\tfrac3{16}\bigr)=(0;\,0)$.

**Câu (b).** Với $a=-1$: $\psi_\theta(s,a)=\dfrac{-1-0}{1}(1;\,2)=(-1;\,-2)$. Bước $\Delta\theta=\alpha\psi_\theta(s,a)$ dời trung bình $\alpha\,\phi(s)^\top(-1;\,-2)=-5\alpha<0$: với bước nhỏ ($\alpha<0{,}2$), trung bình giảm về phía $a=-1$ mà không vượt qua nó.

**Kiểm tra lại.** Ở (a), hành động 1 ít được chọn hơn nên hàm điểm của nó dài hơn, ngược với Ví dụ 09.15. Nhầm lẫn thường gặp: quên trừ đặc trưng trung bình, được $\psi_\theta(s,1)=(1;\,0)$, và kỳ vọng $\bigl(\tfrac14;\,\tfrac34\bigr)\ne0$.
:::

::: exercise Bài tập 09.6 (Sai phân trung tâm)
Bài toán một bước, chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$, $r(1)=3$, $r(2)=0$, nên $J(\theta)=3\pi_\theta(1\mid s)$. Tính sai phân trung tâm $\bigl(J(\theta+\epsilon u_1)-J(\theta-\epsilon u_1)\bigr)/(2\epsilon)$ với $\epsilon=0{,}1$; so với sai phân một phía $0{,}655$ của Ví dụ 09.13 và giá trị đúng $\tfrac23$. Một ước lượng gradient đầy đủ bằng sai phân trung tâm cần bao nhiêu giá trị $J$?
:::

::: hint
$J(\theta)=3\pi_\theta(1\mid s)$; với $\theta-\epsilon u_1=(\log2-0{,}1;\,0)$, $\pi_\theta(1\mid s)=2e^{-0{,}1}/(2e^{-0{,}1}+1)$.
:::

::: solution
**Tính.** $J(\theta+\epsilon u_1)\approx2{,}0655$ (Ví dụ 09.13); $J(\theta-\epsilon u_1)=3\cdot\dfrac{2e^{-0{,}1}}{2e^{-0{,}1}+1}\approx1{,}9323$. Sai phân trung tâm: $(2{,}0655-1{,}9323)/0{,}2\approx0{,}666$.

**So sánh.** Sai lệch so với $\tfrac23$ khoảng $0{,}0004$, nhỏ hơn nhiều so với $0{,}011$ của sai phân một phía: sai số cắt cụt của sai phân trung tâm tỉ lệ với $\epsilon^2$ thay vì $\epsilon$.

**Chi phí.** Mỗi tọa độ cần hai giá trị $J$ mới, nên cả gradient cần $2d$ giá trị thay vì $d+1$. Phương sai do nhiễu vẫn tỉ lệ với $1/(n\epsilon^2)$.

**Kiểm tra lại.** Nhầm lẫn thường gặp: chia cho $\epsilon$ thay vì $2\epsilon$, được $1{,}33$.
:::

::: exercise Bài tập 09.7 (Học độ lệch chuẩn Gaussian)
Chính sách Gaussian với trung bình $\mu_\theta(s)=\phi(s)^\top\theta$ và độ lệch chuẩn $\sigma=e^\omega$, $\omega$ là một tham số học được. (a) Chứng minh $\partial\log\pi/\partial\omega=\bigl(a-\mu_\theta(s)\bigr)^2/\sigma^2-1$. (b) Kiểm kỳ vọng của đại lượng này theo $A\sim\pi$ bằng $0$. (c) Tính giá trị tại $a=1{,}5$, $\mu_\theta(s)=0$, $\sigma=1$, và nêu một bước theo nó làm $\sigma$ tăng hay giảm.
:::

::: hint
Viết $\log\pi=-\tfrac12(a-\mu)^2e^{-2\omega}-\omega-\tfrac12\log(2\pi)$.
:::

::: solution
**Câu (a).** Đạo hàm theo $\omega$: $-\tfrac12(a-\mu)^2\cdot(-2)e^{-2\omega}-1=(a-\mu)^2/\sigma^2-1$.

**Câu (b).** $\mathbb E\bigl[(A-\mu)^2\bigr]=\sigma^2$, nên kỳ vọng bằng $\sigma^2/\sigma^2-1=0$, đúng Mệnh đề 09.17.

**Câu (c).** $1{,}5^2/1-1=1{,}25>0$: bước theo hàm điểm tăng $\omega$, tức tăng $\sigma$, làm mẫu xa trung bình như $a=1{,}5$ dễ xảy ra hơn.

**Kiểm tra lại.** Mẫu có $|a-\mu|<\sigma$ cho giá trị âm: bước theo nó thu hẹp phân phối.
:::

### Mức vận dụng

::: exercise Bài tập 09.8 (Cập nhật REINFORCE)
Bài toán một bước, chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$, $\alpha=0{,}1$.

(a) Phần thưởng của hành động 1 là $-3$, của hành động 2 là $0$; một lượt chọn hành động 1. Tính $\theta$ mới và $\pi_\theta(1\mid s)$.

(b) Bỏ điều kiện lượt dừng sau một bước: một lượt hai bước, cả hai bước ở trạng thái $s$, $A_0=1$, $A_1=2$, $R_1=1$, $R_2=2$, $\gamma=0{,}9$. Tính $G_0$, $G_1$ và $\widehat g$.
:::

::: hint
(a) $\widehat g=G_0\psi_\theta(s,1)$. (b) Tính lợi tức lùi; nhân $\psi_\theta(s,1)$ với $G_0$ và $\psi_\theta(s,2)$ với $\gamma G_1$.
:::

::: solution
**Câu (a).** $\widehat g=-3\bigl(\tfrac13;\,-\tfrac13\bigr)=(-1;\,1)$; $\theta=(\log2-0{,}1;\,0{,}1)$; $\pi_\theta(1\mid s)=\dfrac{2e^{-0{,}1}}{2e^{-0{,}1}+e^{0{,}1}}=\dfrac{2}{2+e^{0{,}2}}\approx0{,}621<\tfrac23$.

**Câu (b).** $G_1=2$, $G_0=1+0{,}9\cdot2=2{,}8$. $\widehat g=2{,}8\bigl(\tfrac13;\,-\tfrac13\bigr)+0{,}9\cdot2\bigl(-\tfrac23;\,\tfrac23\bigr)=(0{,}933;\,-0{,}933)+(-1{,}2;\,1{,}2)=(-0{,}267;\,0{,}267)$.

**Kiểm tra lại.** Ở (b), đóng góp của bước sau, $1{,}8\cdot\tfrac23=1{,}2$ mỗi tọa độ, lớn hơn đóng góp $2{,}8\cdot\tfrac13\approx0{,}933$ của bước đầu vì hàm điểm của hành động 2 dài gấp đôi, nên cập nhật nghiêng về hành động 2. Nhầm lẫn thường gặp: nhân cả hai hàm điểm với $G_0$, được $2{,}8\bigl(\psi_\theta(s,1)+\psi_\theta(s,2)\bigr)=(-0{,}933;\,0{,}933)$; hoặc bỏ $\gamma$ ở bước sau, được $(-0{,}4;\,0{,}4)$.
:::

::: exercise Bài tập 09.9 (Cộng một hằng vào phần thưởng)
Bài toán một bước, chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$, $\pi_\theta(\cdot\mid s)=\bigl(\tfrac23;\,\tfrac13\bigr)$; phần thưởng $r(1)=4$, $r(2)=1$ thay cho $(3;\,0)$, tức cộng $1$ vào mọi phần thưởng. (a) Chứng minh $\nabla_\theta J$ không đổi. (b) Tính tổng phương sai của $\widehat g=r(A)\psi_\theta(s,A)$ và so với $\tfrac49$.
:::

::: hint
(a) $\nabla_\theta\pi_\theta(1\mid s)+\nabla_\theta\pi_\theta(2\mid s)=0$. (b) Hai giá trị của $\widehat g$: $4\psi_\theta(s,1)$ và $1\cdot\psi_\theta(s,2)$.
:::

::: solution
**Câu (a).** $\nabla J=\sum_a(r(a)+1)\nabla\pi_\theta(a\mid s)=\sum_ar(a)\nabla\pi_\theta(a\mid s)+\nabla\sum_a\pi_\theta(a\mid s)=\bigl(\tfrac23;\,-\tfrac23\bigr)+0$.

**Câu (b).** $\widehat g=\bigl(\tfrac43;\,-\tfrac43\bigr)$ với xác suất $\tfrac23$, $\bigl(-\tfrac23;\,\tfrac23\bigr)$ với xác suất $\tfrac13$; kỳ vọng $\bigl(\tfrac89-\tfrac29;\,\dots\bigr)=\bigl(\tfrac23;\,-\tfrac23\bigr)$. Mỗi tọa độ: $\tfrac23\cdot\tfrac{16}9+\tfrac13\cdot\tfrac49-\tfrac49=\tfrac{36}{27}-\tfrac49=\tfrac89$. Tổng phương sai $\tfrac{16}9$, gấp bốn lần $\tfrac49$.

**Kiểm tra lại.** Kỳ vọng không đổi đúng như (a). Nhầm lẫn thường gặp: cho rằng gradient tăng theo phần thưởng; chỉ phần thưởng tương đối giữa các hành động quyết định gradient.
:::

::: exercise Bài tập 09.10 (Tổng hợp trên bài toán một bước)
Bài toán một bước, chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$; phần thưởng tất định $r(1)=3$, $r(2)=0$; lượt dừng sau hành động đầu tiên.

(a) Tính $J$ và $\nabla_\theta J$.

(b) Tính $\widehat g=r(A)\psi_\theta(s,A)$ cho từng hành động và kiểm $\mathbb E[\widehat g]=\nabla_\theta J$.

(c) Phần thưởng được đo có nhiễu: $\widehat r_a=r(a)+\varepsilon_a$, với $\varepsilon_1$, $\varepsilon_2$ độc lập, mỗi biến bằng $\pm1$ với xác suất $\tfrac12$. Tính $\mathbb E[\max_a\widehat r_a]$ và so với $\max_ar(a)$. Lặp lại khi $r(2)=2{,}5$.
:::

::: hint
(a), (b): $\pi_\theta=\bigl(\tfrac23;\,\tfrac13\bigr)$, $\psi_\theta(s,1)=\bigl(\tfrac13;\,-\tfrac13\bigr)$. (c): liệt kê bốn cặp $(\varepsilon_1,\varepsilon_2)$ đồng xác suất, rồi dùng điều kiện dấu bằng của Mệnh đề 09.2.
:::

::: solution
**Câu (a).** $J=3\cdot\tfrac23+0\cdot\tfrac13=2$; $\nabla_\theta J=\sum_ar(a)\pi_\theta(a\mid s)\psi_\theta(s,a)=\tfrac23\cdot3\bigl(\tfrac13;\,-\tfrac13\bigr)=\bigl(\tfrac23;\,-\tfrac23\bigr)$.

**Câu (b).** $A=1$: $\widehat g=3\bigl(\tfrac13;\,-\tfrac13\bigr)=(1;\,-1)$, xác suất $\tfrac23$. $A=2$: $\widehat g=0\cdot\psi_\theta(s,2)=(0;\,0)$, xác suất $\tfrac13$. $\mathbb E[\widehat g]=\tfrac23(1;\,-1)=\bigl(\tfrac23;\,-\tfrac23\bigr)$, đúng $\nabla_\theta J$ (Hệ quả 09.25).

**Câu (c).** $\widehat r_1\in\{2;\,4\}$ và $\widehat r_2\in\{-1;\,1\}$, nên $\widehat r_1>\widehat r_2$ ở cả bốn cặp: hành động 1 luôn thắng, $\mathbb E[\max_a\widehat r_a]=\mathbb E[\widehat r_1]=3=\max_ar(a)$, không chệch; đây là trường hợp dấu bằng của Mệnh đề 09.2. Với $r(2)=2{,}5$: $\widehat r_2\in\{1{,}5;\,3{,}5\}$; bốn cặp cho cực đại $2$; $3{,}5$; $4$; $4$, nên $\mathbb E[\max_a\widehat r_a]=\tfrac14(2+3{,}5+4+4)=3{,}375$, chệch $+0{,}375$.

**Kiểm tra lại.** Độ chệch $0{,}375$ ở khoảng cách $0{,}5$ trùng Ví dụ 09.3(i), vì chỉ khoảng cách giữa hai giá trị đúng và phân phối nhiễu quyết định độ chệch. Nhầm lẫn thường gặp: cho rằng phép cực đại luôn chệch dương nghiêm ngặt, hoặc cho rằng $\widehat g$ không chệch thì mỗi lượt cho đúng gradient.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

**Hướng dẫn đọc thêm.** Sutton và Barto (2018), §6.7, trình bày độ chệch của phép cực đại bằng một MDP nhỏ có nhiều hành động nhiễu và so Q-learning với Double Q-learning trên đó; đọc cùng Mục 2–3. §13.1–13.3 trình bày chính sách tham số hóa, định lý gradient chính sách (dạng phân bố trạng thái, không chuẩn hóa) và REINFORCE; §13.4 về REINFORCE có đường cơ sở là phần mở đầu của Bài 10; §13.7 về chính sách cho hành động liên tục. Van Hasselt (2010) chứng minh ước lượng kép và đề xuất Double Q-learning; van Hasselt, Guez và Silver (2016) đo độ đánh giá cao của DQN trên Atari và đề xuất Double DQN. Williams (1992) là bài gốc của REINFORCE; Sutton và cộng sự (2000) phát biểu định lý gradient chính sách với xấp xỉ hàm; Nota và Thomas (2020) phân tích việc bỏ trọng số $\gamma^t$.

**Tài liệu tham khảo.**

1. Tạ Việt Cường. *Bài giảng 10: Policy Gradient*, dùng cho Bài 09 (lecture09-ddqn-and-policy-gradient-part1.pdf, tr. 1–40). Phòng thí nghiệm HMI, Trường Đại học Công nghệ, học kỳ 2, 2025–2026.
2. Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. §6.7, §13.1–13.4, §13.7.
3. van Hasselt, H. "Double Q-learning." *Advances in Neural Information Processing Systems* 23, 2010.
4. van Hasselt, H., Guez, A., Silver, D. "Deep Reinforcement Learning with Double Q-learning." *AAAI* 2016.
5. Mnih, V. và cộng sự. "Human-level control through deep reinforcement learning." *Nature* 518 (2015): 529–533.
6. Williams, R. J. "Simple statistical gradient-following algorithms for connectionist reinforcement learning." *Machine Learning* 8 (1992): 229–256.
7. Sutton, R. S., McAllester, D., Singh, S., Mansour, Y. "Policy gradient methods for reinforcement learning with function approximation." *Advances in Neural Information Processing Systems* 12, 2000.
8. Nota, C., Thomas, P. S. "Is the Policy Gradient a Gradient?" *AAMAS* 2020.
9. Hessel, M. và cộng sự. "Rainbow: Combining Improvements in Deep Reinforcement Learning." *AAAI* 2018.
