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
- **Chính sách, lợi tức và giá trị hành động** (Định nghĩa 03.8, 03.9, 03.13, 03.16). Chính sách $\pi$ gán cho mỗi trạng thái $s$ một phân phối $\pi(\cdot\mid s)$ trên $\mathcal A$; chính sách tất định là trường hợp dồn toàn bộ xác suất vào một hành động. Trong nhiệm vụ có kết thúc, lượt (episode) dừng tại bước ngẫu nhiên $T$, và lợi tức (return) từ bước $t$ là $G_t=\sum_{k=t}^{T-1}\gamma^{\,k-t}R_{k+1}$ với quy ước $G_T=0$; Bài 03 viết cùng tổng dưới dạng $\sum_{k=t+1}^{T}\gamma^{\,k-t-1}R_k$. Giá trị hành động $q_\pi(s,a)=\mathbb E_\pi[G_0\mid S_0=s,A_0=a]$ là lợi tức kỳ vọng khi thực hiện $a$ tại $s$ rồi theo $\pi$. Với chính sách Markov dừng, $\mathbb E_\pi[G_t\mid S_t=s,A_t=a]=q_\pi(s,a)$ ở mọi bước $t$ mà sự kiện $\{S_t=s,A_t=a\}$ có xác suất dương (Bổ đề 03.20(d)).
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
| $Z_i$, $U_i$ | cờ kết thúc của MDP; cờ cắt ngắn | $\{0,1\}$ |
| $(S_i,A_i,R_i,S'_i,Z_i,U_i)$, $b$ | mẫu chuyển thứ $i$ của mini-batch; cỡ mini-batch | bộ sáu thành phần; $\mathbb N_+$ |
| $\theta$, $d$ | tham số mạng trực tuyến (Mục 2–3) hoặc tham số chính sách (Mục 4–7); số chiều của $\theta$ | $\mathbb R^d$; $d\in\mathbb N_+$ |
| $\theta^-$, $C$ | tham số mạng mục tiêu; số bước tối ưu giữa hai lần đồng bộ | $\mathbb R^d$; $\mathbb N_+$ |
| $Q_\theta$, $Q_{\theta^-}$ | mạng trực tuyến; mạng mục tiêu | hàm thực trên $\mathcal S\times\mathcal A$ |
| $y_i$, $a_i^*$ | mục tiêu của mẫu $i$; hành động mạng trực tuyến chọn tại $S'_i$ | $\mathbb R$; $\mathcal A$ |
| $\operatorname{sg}$ | dừng gradient | toán tử trong đồ thị tính |
| $\widehat Q_a$ | ước lượng có nhiễu của giá trị hành động $a$ tại một trạng thái cố định | biến ngẫu nhiên thực |
| $Q_1$, $Q_2$ | hai bảng của Double Q-learning | hàm thực trên $\mathcal S\times\mathcal A$ |
| $\alpha$ | bước học của Double Q-learning và của bước tăng gradient, cùng vai với tốc độ học $\eta$ của Bài 08 | $(0,\infty)$ |
| $\phi(s,a)$, $\phi(s)$ | đặc trưng của cặp trạng thái–hành động; đặc trưng của trạng thái | $\mathbb R^d$ |
| $\mu$, $\sigma^2$ | trung bình và phương sai của chính sách Gaussian | $\mathbb R$; $(0,\infty)$ |
| $J(\theta)$ | hàm mục tiêu: lợi tức kỳ vọng từ trạng thái đầu | $\mathbb R$ |
| $\psi_\theta(s,a)$, $\psi_t$ | hàm điểm $\nabla_\theta\log\pi_\theta(a\mid s)$; viết tắt của $\psi_\theta(S_t,A_t)$ | $\mathbb R^d$ |
| $\tau$, $p_\theta(\tau)$ | quỹ đạo $(S_0,A_0,R_1,\dots,S_T)$; xác suất hoặc mật độ của quỹ đạo dưới $\pi_\theta$ | dãy hữu hạn; $[0,\infty)$ |
| $H_t$ | lịch sử $(S_0,A_0,R_1,\dots,R_t,S_t)$ | dãy hữu hạn |
| $\widehat g$ | ước lượng REINFORCE của $\nabla_\theta J$ | $\mathbb R^d$ |
| $\nu^\pi_\gamma$ (viết gọn $\nu^\pi$) | phân bố chiếm dụng chiết khấu của trạng thái dưới $\pi$ | phân phối trên $\mathcal S$ |

Quy ước đọc. $R_{t+1}$ gắn với chuyển từ bước $t$ sang bước $t+1$. Sau bước kết thúc $T$, ta coi lượt đi vào một trạng thái hấp thụ có phần thưởng $0$, nên $G_T=0$ và mọi giá trị tại trạng thái kết thúc bằng $0$. Kỳ vọng $\mathbb E_\pi$ lấy theo $S_0\sim\rho_0$, $A_t\sim\pi(\cdot\mid S_t)$ và $(S_{t+1},R_{t+1})\sim P(\cdot\mid S_t,A_t)$. Trong mini-batch, chỉ số $i$ không mang thứ tự thời gian, nên mẫu viết $R_i$, $S'_i$ thay cho $R_{t+1}$, $S_{t+1}$. Chữ hoa $Q$ chỉ các ước lượng (mạng, bảng, $\widehat Q_a$), chữ thường $q_\pi$ chỉ giá trị đúng. Khi tọa độ của vector có dấu phẩy thập phân, các tọa độ được ngăn bằng dấu chấm phẩy, như $(1{,}5;\,3)$; ta dùng cùng cách viết cho mọi vector của chương.

Chữ $\theta$ có hai vai. Ở Mục 2–3, $\theta$ là tham số của mạng giá trị hành động như trong Bài 08; từ Mục 4, $\theta$ là tham số của chính sách như trong bài giảng gốc và trong Sutton và Barto (2018, Chương 13). Hai vai không xuất hiện trong cùng một công thức. Số liệu trong các ví dụ là số liệu sư phạm tự xây dựng, trừ các số đo lấy từ bài thực hành của Bài 08, có ghi rõ nguồn tại chỗ dùng.

Ứng với giáo trình *Học máy thống kê*: $q_\pi$ là $Q^\pi$. Phân phối đầu $\mu$ và hàm động lực $p(s',r\mid s,a)$ của Bài 03 được viết $\rho_0$ và $P(s',r\mid s,a)$ ở đây, để chữ $\mu$ dành cho trung bình của chính sách Gaussian và chữ $p$ cho xác suất $p_\theta(\tau)$ của một quỹ đạo. Phân bố chiếm dụng viết $\nu^\pi_\gamma$, không dùng $d$ (số chiều của $\theta$) hay $\mu$.

---

## Bản đồ chủ đề (bốn nhóm)

### Nhóm cầu nối

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-09-topic-15` | Kiến thức tiên quyết và ký hiệu | tr. 3–10 | Nhắc mục tiêu DQN, dừng gradient, chính sách, lợi tức, bất đẳng thức Jensen | Vào: Bài 03, Bài 08 → Ra: ký hiệu chung của chương | phần mở đầu |
| `lec-09-topic-16` | Mở đầu: mục tiêu, nội dung và bài toán trung tâm | tr. 1–2, 11, 22–25 | Nêu hai đại lượng ước lượng từ mẫu và câu trả lời có điều kiện của từng mục | Vào: topic-15 → Ra: khung cho Mục 2–6 | 1 |
| `lec-09-topic-01` | Phép cực đại trong mục tiêu DQN | tr. 3–11 | Chỉ ra phép cực đại vừa chọn vừa đánh giá; số đo đánh giá cao trên CartPole | Vào: topic-16 → Ra: nhu cầu đo độ chệch của phép cực đại | 2 |
| `lec-09-topic-14` | Ước lượng gradient bằng sai phân hữu hạn | tr. 33 | Bước vấn đề của hàm điểm: sai phân cần $d+1$ giá trị $J$, mỗi giá trị từ nhiều lượt | Vào: topic-07 → Ra: nhu cầu một ước lượng gradient từ lượt mẫu | 5 |

### Nhóm cốt lõi

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-09-topic-02` | Độ chệch của phép cực đại | tr. 12–13 | Ví dụ hai hành động có nhiễu $\pm1$; bất đẳng thức $\mathbb E[\max]\ge\max\mathbb E$ | Vào: topic-01 → Ra: nguyên nhân là cùng ước lượng chọn và đánh giá | 2 |
| `lec-09-topic-03` | Mục tiêu Double DQN | tr. 14–16 | Chọn bằng mạng trực tuyến, đánh giá bằng mạng mục tiêu; thuật toán Double DQN | Vào: topic-02 → Ra: mục tiêu và thuật toán | 3 |
| `lec-09-topic-05` | Double Q-learning dạng bảng | tr. 20–21 | Hai bảng, cập nhật chéo; so sánh với Double DQN trên cùng số liệu | Vào: topic-03, topic-04 → Ra: hai cách tách và giới hạn chung của học giá trị | 3 |
| `lec-09-topic-06` | Chính sách tham số hóa | tr. 22–29 | Lưới gộp trạng thái; phân phối phân loại, softmax, Gaussian | Vào: topic-05 → Ra: $\pi_\theta(\cdot\mid s)$ rời rạc hoặc liên tục | 4 |
| `lec-09-topic-07` | Hàm mục tiêu và giả thiết | tr. 30–32 | $J(\theta)$, bước tăng gradient, giả thiết đổi đạo hàm và kỳ vọng | Vào: topic-06 → Ra: bài toán tối ưu theo $\theta$ | 5 |
| `lec-09-topic-08` | Hàm điểm của chính sách softmax | tr. 34–36 | Định nghĩa hàm điểm; $\psi=\phi-\mathbb E_\pi\phi$ | Vào: topic-14 → Ra: hàm điểm rời rạc | 5 |
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
3. Tách chọn và đánh giá: hai bản ước lượng độc lập, mục tiêu và thuật toán Double DQN, phạm vi của Double DQN, Double Q-learning dạng bảng (`lec-09-topic-03`, `lec-09-topic-04`, `lec-09-topic-05`).
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

<!-- note-topic-id: lec-09-topic-01 -->
### DQN còn ghép chọn với đánh giá

**Vấn đề.** Với dạng bảng chính xác, Q-learning hội tụ dưới các giả thiết tiêu chuẩn. Với mạng neural, huấn luyện có thể phân kỳ vì hai nguyên nhân: tương quan giữa các mẫu và mục tiêu không dừng (tr. 3–4).

**Trực giác.** Mục tiêu DQN chứa $\max_{a'}Q_{\theta^-}(s',a')$: khi mạng thay đổi, mục tiêu thay đổi theo — mô hình đuổi theo một mục tiêu đang di chuyển (tr. 4).

**Hai công cụ đã học ở Bài 08** (tr. 5–10):

- **Bộ nhớ phát lại (experience replay):** lưu $(s,a,r,s')$ vào bộ đệm, lấy mini-batch ngẫu nhiên — phá tương quan theo thời gian, tái sử dụng dữ liệu.
- **Target network:** duy trì $Q_{\theta^-}$ để tính đích, sao chép $\theta^-\leftarrow\theta$ theo chu kỳ $C$ bước — làm đích thay đổi chậm.

Hàm mất mát trên lô $b$ mẫu:

$$L_B(\theta)=\frac1b\sum_{i=1}^{b}\big[\operatorname{sg}(y_i)-Q_\theta(S_i,A_i)\big]^2,$$

với đích DQN từng trường hợp:

$$y_i=\begin{cases}R_i,&Z_i=1,\\ R_i+\gamma\max_{a'}Q_{\theta^-}(S'_i,a'),&Z_i=0.\end{cases}$$

Gradient chỉ đi qua $Q_\theta(S_i,A_i)$; đích và mạng mục tiêu không nhận gradient.

**Giới hạn còn lại.** Replay và mạng mục tiêu xử lý hai cơ chế khác nhau, nhưng **không tách việc chọn hành động khỏi việc đánh giá hành động**: trong $\max_{a'}Q_{\theta^-}(s',a')$, cùng một bộ ước lượng vừa chọn vừa đánh giá. Đây là chủ đề của topic-02.

**Kiểm tra.** Trong đích DQN, biến nào chọn hành động ở $s'$? — Chính $Q_{\theta^-}$, qua phép max.

*Nguồn: tr. 3–10.*

<!-- note-topic-id: lec-09-topic-02 -->
### Sai lệch cực đại và ví dụ Rademacher

**Vấn đề.** Viết $\widehat Q_a=Q^*_a+\varepsilon_a$ với $\mathbb E[\varepsilon_a]=0$. Từng ước lượng không chệch, nhưng

$$\max_a\widehat Q_a=\max_a\big(Q^*_a+\varepsilon_a\big)$$

nhiều khả năng lớn hơn $\max_a Q^*_a$, vì phép max có xu hướng chọn hành động có hiện thực nhiễu thuận lợi (tr. 12–13). Cùng một mẫu nhiễu quyết định cả hành động thắng lẫn giá trị được báo cáo.

::: example
**Ví dụ Rademacher.** Hai hành động có giá trị thật bằng $0$. Nhiễu $\varepsilon_1,\varepsilon_2$ độc lập, nhận $-1$ hoặc $1$ với xác suất $1/2$. Từng ước lượng: $\mathbb E[\widehat Q_1]=\mathbb E[\widehat Q_2]=0$. Bốn cặp $(\varepsilon_1,\varepsilon_2)$ đồng xác suất: $(-1,-1)$ cho $\max=-1$; ba cặp còn lại cho $\max=1$. Do đó

$$\mathbb E\big[\max_a\widehat Q_a\big]=\tfrac14(-1)+\tfrac34(1)=\tfrac12\neq 0=\max_a\mathbb E[\widehat Q_a].$$

Sai lệch dương xuất hiện dù từng ước lượng không chệch.
:::

**Hình thức.** Hàm cực đại theo véc-tơ là hàm lồi, nên Jensen cho

$$\mathbb E\Big[\max_a\widehat Q_a\Big]\ \ge\ \max_a\mathbb E[\widehat Q_a].$$

Phạm vi phát biểu: đây là **bất đẳng thức không nghiêm** nói chung. Dấu bằng có thể xảy ra (ví dụ một hành động luôn thắng); dấu nghiêm cần điều kiện bổ sung về phân phối nhiễu và quan hệ giữa các ước lượng. Không phát biểu "mọi lần lấy max đều đánh giá quá cao" — kết luận là về kỳ vọng.

**Nhu cầu.** Vì sai lệch này lặp lại qua bootstrap và có thể dẫn đến mất ổn định hoặc phân kỳ, cần tách **chọn** và **đánh giá** hành động bằng hai bộ ước lượng khác nhau.

**Kiểm tra.** Trong ví dụ Rademacher, vì sao $\max_a\mathbb E[\widehat Q_a]=0$? — Vì $\mathbb E[\widehat Q_a]=0$ với cả hai hành động.

*Nguồn: tr. 11–13.*

---

## 3. Tách chọn và đánh giá

<!-- note-topic-id: lec-09-topic-03 -->
### Đích Double DQN

**Trực giác.** Tách hai vai trò của phép max: mạng online **chọn** hành động kế tiếp tốt nhất theo thứ hạng hiện tại, mạng mục tiêu **đánh giá** hành động đã chọn (tr. 14–16).

**Hình thức.** Với tập hành động hữu hạn $\mathcal A$, đặt

$$a_i^*=\arg\max_{a\in\mathcal A}Q_\theta(S'_i,a)\quad\text{if }Z_i=0,$$

và đích từng trường hợp:

$$y_i=\begin{cases}R_i,&Z_i=1,\\ R_i+\gamma\,\operatorname{sg}\!\big(Q_{\theta^-}(S'_i,a_i^*)\big),&Z_i=0.\end{cases}$$

Ba điểm bắt buộc:

- **Không gọi argmax ở nhánh terminal:** khi $Z_i=1$, đích là $R_i$; tính $a_i^*$ tại trạng thái kết thúc là vô nghĩa.
- **$\operatorname{sg}$ chặn gradient:** đích và mạng mục tiêu không nhận gradient; chỉ $Q_\theta(S_i,A_i)$ đi qua loss.
- **Hòa argmax:** cài đặt phải ghi quy tắc phá hòa.

::: example
**Đối chiếu hai đích.** Cho $r=1$, $\gamma=0{,}9$, $Z=0$, $Q_{\theta^-}(s',\cdot)=(5,4)$, $Q_\theta(s',\cdot)=(3,6)$.

- **DQN:** mạng mục tiêu vừa chọn vừa đánh giá — chọn hành động 1 (giá trị $5$), đích $y^{\mathrm{DQN}}=1+0{,}9\cdot 5=5{,}5$.
- **Double DQN:** mạng online chọn hành động 2 (giá trị $6$), mạng mục tiêu đánh giá $4$, đích $y^{\mathrm{DDQN}}=1+0{,}9\cdot 4=4{,}6$.

Chênh lệch không chứng minh Double DQN luôn gần giá trị thật hơn trong từng mẫu; cơ chế nhằm giảm liên hệ giữa nhiễu tạo thứ hạng và nhiễu tạo giá trị đánh giá.
:::

**Ứng dụng và giới hạn.** Double DQN chỉ thay công thức bootstrap, không thay hướng gradient của loss. Nó giảm sai lệch đánh giá quá cao, làm giá trị Q ổn định hơn và thứ hạng hành động đáng tin cậy hơn (tr. 17).

**Kiểm tra.** Trong ví dụ trên, nếu hoán đổi hai bộ giá trị thì hai đích đổi thành bao nhiêu? — Khi hoán đổi, mạng mục tiêu mới là $(3,6)$ và mạng online mới là $(5,4)$. DQN có mạng mục tiêu vừa chọn vừa đánh giá: max của $(3,6)$ là $6$, nên đích $1+0{,}9\cdot 6=6{,}4$. Double DQN dùng mạng online $(5,4)$ chọn hành động 1, rồi mạng mục tiêu $(3,6)$ đánh giá hành động 1 bằng $3$, nên đích $1+0{,}9\cdot 3=3{,}7$.

*Nguồn: tr. 14–16.*

<!-- note-topic-id: lec-09-topic-04 -->
### Phạm vi tác dụng của Double DQN

**Phát biểu giới hạn đúng** (tr. 17–19):

- Double DQN **không** tự loại bỏ tương quan mẫu — đó là việc của replay.
- Double DQN **không** tự loại bỏ tính không dừng của mục tiêu — đó là việc của target network.
- Double DQN **không** bảo đảm hội tụ với mọi kiến trúc mạng neural tùy ý.
- Có thể gây học chậm trong một số hoàn cảnh.

**Vì sao hai mạng không độc lập.** $\theta^-$ là bản sao trễ của $\theta$, nên hai sai số đánh giá có quan hệ; không được dùng lập luận độc lập như trong Double Q-learning lý tưởng để mô tả hai mạng sâu. Tách chọn–đánh giá **thường giảm** sai lệch cực đại, không buộc sai lệch bằng $0$.

**Vị trí của bộ tối ưu.** RMSprop/Adam/SGD ảnh hưởng đến cách tham số được tối ưu; Double DQN ảnh hưởng đến mục tiêu mà bộ tối ưu phải khớp. Hai cải tiến xử lý hai vấn đề khác nhau.

**Kiểm tra.** Kết luận về chất lượng cần dựa trên gì? — Nhiều lần chạy và thước đo đánh giá, không chỉ loss huấn luyện.

*Nguồn: tr. 17–19.*

<!-- note-topic-id: lec-09-topic-05 -->
### Double Q-learning dạng bảng

**Nguyên tắc double.** Duy trì hai bảng $Q_1,Q_2$; mỗi bước cập nhật **một** bảng, bảng còn lại đánh giá hành động do bảng đang cập nhật chọn (tr. 20–21).

**Hình thức.** Khởi tạo $Q_1,Q_2$ tùy ý, $Q_1(\text{terminal},\cdot)=Q_2(\text{terminal},\cdot)=0$. Chính sách hành vi (ví dụ $\varepsilon$-greedy trên $Q_1+Q_2$) chọn $A$; sau khi quan sát $(R,S',Z)$, với xác suất $1/2$ cập nhật bảng thứ nhất:

$$a^*=\arg\max_{a\in\mathcal A}Q_1(S',a),\qquad Z=0,$$

$$y_1=\begin{cases}R,&Z=1,\\ R+\gamma Q_2(S',a^*),&Z=0,\end{cases}$$

$$Q_1(S,A)\leftarrow Q_1(S,A)+\alpha\,[y_1-Q_1(S,A)].$$

Nhánh còn lại hoán đổi $Q_1\leftrightarrow Q_2$. Hai điểm bắt buộc:

- **Che bootstrap khi terminal:** khi $Z=1$, đích là $R$, không tính argmax trên trạng thái kết thúc.
- **Chọn bằng bảng đang cập nhật, đánh giá bằng bảng kia:** $Q_1$ chọn, $Q_2$ đánh giá. Lấy $\max$ của $Q_2$ sẽ phá cơ chế tách.

::: example
**Tính tay.** Cho $Q_1(S,A)=4$, $\alpha=0{,}1$, $R=1$, $\gamma=0{,}9$, $Z=0$. Tại $S'$: $Q_1=(2,1)$, $Q_2=(1,4)$.

- $Q_1$ chọn $a^*=1$ (giá trị $2$); $Q_2$ đánh giá hành động 1 bằng $1$.
- $y_1=1+0{,}9\cdot 1=1{,}9$.
- $Q_1^{\mathrm{new}}(S,A)=4+0{,}1\,(1{,}9-4)=3{,}79$.
:::

**So sánh hai cách tách** (tr. 14–21):

| | Double Q-learning | Double DQN |
|---|---|---|
| biểu diễn | hai bảng $Q_1,Q_2$ | online $Q_\theta$, target $Q_{\theta^-}$ |
| cập nhật | chọn ngẫu nhiên một bảng | luôn cập nhật online |
| đánh giá | bảng còn lại | bản sao trễ |
| dữ liệu | thường trực tuyến | thường từ replay |

Cùng nguyên tắc tách chọn–đánh giá, nhưng **không phải cùng thuật toán**. Tên "Double" không cho phép suy ra tùy ý rằng bốn hay tám bộ ước lượng sẽ tốt hơn: thêm bộ ước lượng làm đổi thuật toán, chi phí và quan hệ tương quan.

**Kiểm tra.** Double Q-learning cập nhật mấy bảng trong một bước? — Một bảng; bảng kia chỉ đánh giá.

*Nguồn: tr. 20–21.*

---

## 4. Chính sách tham số hóa

<!-- note-topic-id: lec-09-topic-06 -->
### Chính sách trực tiếp là phân phối hành động

**Vấn đề của học giá trị.** $Q_\theta$ kết hợp với argmax quá tất định: argmax chỉ trả một hành động, khó dùng trực tiếp cho hành động liên tục, và trong biểu diễn đặc trưng kém (ví dụ ô xám che hai hướng E và W đều tối ưu), hàm Q buộc chọn một trong hai và đều lệch với phương án tối ưu (tr. 22–25).

**Trực giác.** Thay vì học giá trị rồi trích chính sách bằng argmax, tham số hóa **trực tiếp** một phân phối hành động $\pi_\theta:s\mapsto\mathcal P(\cdot\mid s)$ để lấy mẫu (tr. 25–29).

**Hai giới hạn cần nói đúng:**

- Trong MDP quan sát đầy đủ, một chính sách **tất định** tối ưu có thể tồn tại; không cần ngẫu nhiên hóa để đạt tối ưu. Lợi ích của tham số hóa trực tiếp là giao diện lấy mẫu khả vi và miền hành động liên tục, không phải "ngẫu nhiên tốt hơn".
- **Không nói chính sách ngẫu nhiên tự khôi phục thông tin trạng thái đã mất:** nếu hai trạng thái cho cùng biểu diễn, cùng tham số chính sách tạo cùng phân phối hành động. Muốn quyết định khác nhau, cần biểu diễn hoặc bộ nhớ đủ thông tin.

**Điều khiển và học.** Tại $s$: lấy $A\sim\pi_\theta(\cdot\mid s)$ rồi gửi cho môi trường; học bằng cách điều chỉnh $\theta$ để tăng xác suất của hành động gắn với return cao.

**Kiểm tra.** Chính sách trực tiếp có phải hệ quả của Double DQN không? — Không; nó là một lựa chọn biểu diễn độc lập.

*Nguồn: tr. 22–29.*

---

## 5. Hàm mục tiêu và hàm điểm

<!-- note-topic-id: lec-09-topic-07 -->
### Mục tiêu episodic và giả thiết

**Quy ước.** $S_0\sim\rho_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$, $R_{t+1}$ nhận sau $A_t$, $0\le\gamma<1$, $T<\infty$ hầu chắc chắn:

$$G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},\qquad J(\theta)=\mathbb E_{\tau\sim p_\theta}[G_0].$$

Sau $T$, nối một trạng thái hấp thụ có phần thưởng và giá trị bằng $0$ — quy ước này cho phép dùng tổng vô hạn mà không đổi mục tiêu episodic (tr. 30–32, 39–40).

**Bài toán tối ưu.** Cực đại hóa $J(\theta)$; cập nhật $\theta\leftarrow\theta+\alpha\,\widehat g$ với $\widehat g\approx\nabla_\theta J(\theta)$, $\alpha>0$. Dấu cộng vì mục tiêu được cực đại hóa (tr. 30–33).

**Giả thiết** (tr. 33–40) — chi phối toàn bộ suy diễn sau này:

1. $\rho_0$ và động lực $P$ **không phụ thuộc** $\theta$.
2. $\pi_\theta$ khả vi, có **miền hỗ trợ cố định** và dương tại hành động được lấy mẫu.
3. $G_0\nabla_\theta\log p_\theta(\tau)$ khả tích; có điều kiện (ví dụ một chặn trội phù hợp) cho phép đổi đạo hàm với tích phân.
4. $S_t$ là trạng thái Markov; sau kết thúc dùng tiếp diễn hấp thụ.

Miền hỗ trợ thay đổi theo $\theta$ có thể sinh thêm hạng biên.

**Kiểm tra.** Vì sao dấu cập nhật là cộng? — Vì ta cực đại hóa $J$, không cực tiểu hóa loss.

*Nguồn: mục tiêu ở tr. 30–34; các điều kiện support và khả tích được làm rõ để dùng cho suy diễn ở tr. 39.*

<!-- note-topic-id: lec-09-topic-08 -->
### Hàm điểm softmax

**Hàm điểm.** Với hành động đã lấy mẫu và $\pi_\theta(a\mid s)>0$:

$$\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s),\qquad \nabla_\theta\pi_\theta(a\mid s)=\pi_\theta(a\mid s)\,\psi_\theta(s,a).$$

Đồng nhất thức đạo hàm log chỉ hợp lệ tại nơi xác suất hoặc mật độ dương (tr. 34).

**Softmax cho hành động rời rạc.** Cho đặc trưng $\phi(s,a)\in\mathbb R^d$ cố định khi lấy đạo hàm theo $\theta$, logit $z_a(s)=\phi(s,a)^\top\theta$:

$$\pi_\theta(a\mid s)=\frac{e^{\phi(s,a)^\top\theta}}{\sum_b e^{\phi(s,b)^\top\theta}},\qquad \psi_\theta(s,a)=\phi(s,a)-\sum_b\pi_\theta(b\mid s)\,\phi(s,b).$$

Hàm điểm là đặc trưng của hành động chọn trừ trung bình đặc trưng theo chính sách; do đó $\mathbb E_{A\sim\pi_\theta}[\psi_\theta(s,A)]=0\in\mathbb R^d$. Nếu $\phi$ cũng có tham số học, công thức phải dùng quy tắc dây chuyền đầy đủ (tr. 35–36).

::: example
**Ví dụ hai hành động.** $\pi_\theta(1\mid s)=2/3$, $\pi_\theta(2\mid s)=1/3$, $\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$:

$$\psi_\theta(s,1)=(1,0)-\big(\tfrac23,\tfrac13\big)=\big(\tfrac13,-\tfrac13\big),\qquad \psi_\theta(s,2)=\big(-\tfrac23,\tfrac23\big).$$

Tổng có trọng số: $\tfrac23(\tfrac13,-\tfrac13)+\tfrac13(-\tfrac23,\tfrac23)=(0,0)$.
:::

**Kiểm tra.** Kỳ vọng có điều kiện của hàm điểm dưới chính sách bằng gì? — $0\in\mathbb R^d$.

*Nguồn: tr. 35–36.*

<!-- note-topic-id: lec-09-topic-09 -->
### Hàm điểm Gaussian phương sai cố định

**Hành động liên tục.** Lấy mẫu $A\mid S=s\sim\mathcal N(\mu_\theta(s),\sigma^2)$ với $\mu_\theta(s)=\phi(s)^\top\theta$; giữ $\phi(s)\in\mathbb R^d$ và $\sigma^2>0$ cố định (tr. 37–38):

$$\psi_\theta(s,a)=\frac{a-\mu_\theta(s)}{\sigma^2}\,\phi(s)\in\mathbb R^d.$$

- Hành động lớn hơn trung bình cho phần dư dương → tăng log mật độ của hành động đó.
- Phương sai nhỏ khuếch đại độ lớn hàm điểm.
- Công thức chỉ là gradient theo tham số trung bình; nếu $\phi$ hoặc $\sigma$ phụ thuộc $\theta$, cần đạo hàm thêm theo quy tắc dây chuyền.
- Với hành động bị chặn, Gaussian không biến đổi có thể sinh hành động ngoài miền; có thể cần biến đổi.

::: example
**Tính tay.** $\phi(s)=(1,2)$, $\theta=(0,0)$ nên $\mu=0$, $\sigma^2=1$, $a=1{,}5$:

$$\psi_\theta(s,a)=\frac{1{,}5-0}{1}\,(1,2)=(1{,}5,\,3).$$

Nếu hệ số return âm, hướng hàm điểm bị đảo và bước cập nhật làm giảm log mật độ của hành động vừa lấy mẫu; một mẫu đơn lẻ không bảo đảm cải thiện chính sách.
:::

**Kiểm tra.** Góc lái liên tục phù hợp với họ phân phối nào? — Gaussian.

*Nguồn: tr. 37–38.*

---

## 6. Gradient chính sách và REINFORCE

<!-- note-topic-id: lec-09-topic-10 -->
### Tỷ số xác suất và nhân quả

**Tỷ số xác suất (likelihood ratio).** Với $J(\theta)=\int G_0(\tau)\,p_\theta(\tau)\,\mathrm d\tau$ và các giả thiết ở topic-07:

::: derivation
$$\nabla_\theta J(\theta)=\int G_0(\tau)\,\nabla_\theta p_\theta(\tau)\,\mathrm d\tau=\mathbb E_{\tau\sim p_\theta}\!\big[G_0\,\nabla_\theta\log p_\theta(\tau)\big].$$

Dòng đầu dùng điều kiện đổi đạo hàm–tích phân; dòng sau dùng $\nabla_\theta p_\theta=p_\theta\nabla_\theta\log p_\theta$.
:::

**Phân tích xác suất quỹ đạo.** Vì $\rho_0$ và $P$ không phụ thuộc $\theta$:

$$p_\theta(\tau)=\rho_0(s_0)\prod_{t=0}^{T-1}\pi_\theta(a_t\mid s_t)\,P(s_{t+1},r_{t+1}\mid s_t,a_t),\qquad \nabla_\theta\log p_\theta(\tau)=\sum_{t=0}^{T-1}\psi_\theta(s_t,a_t).$$

Gradient của xác suất quỹ đạo gom thành tổng hàm điểm từng bước (tr. 39–40).

**Lập luận nhân quả loại phần thưởng quá khứ.** Đặt $H_t=(S_0,A_0,R_1,\ldots,A_{t-1},R_t,S_t)$. Không cần giả sử các phần thưởng độc lập với hành động:

::: derivation
Với $A_t\sim\pi_\theta(\cdot\mid S_t)$ (rời rạc: thay tích phân bằng tổng theo $a$):

$$\mathbb E_{A_t\sim\pi_\theta}\!\big[\psi_t\mid H_t\big]=\nabla_\theta\!\int_{\mathcal A}\pi_\theta(a\mid S_t)\,\mathrm da=0,$$

trong đó $\psi_t=\psi_\theta(S_t,A_t)$ là hàm điểm tại bước $t$.

Với $G_{<t}=\sum_{k=0}^{t-1}\gamma^kR_{k+1}$ đo được theo $H_t$, ta có $G_0=G_{<t}+\gamma^tG_t$, và vì $G_{<t}$ đo được trước khi lấy mẫu $A_t$:

$$\mathbb E\big[G_{<t}\,\psi_t\big]=0\quad\Longrightarrow\quad \mathbb E\Big[G_0\sum_t\psi_t\Big]=\mathbb E\Big[\sum_t\gamma^tG_t\,\psi_t\Big].$$
:::

Đây là lập luận nhân quả (điều kiện theo lịch sử), **không phải** giả thiết độc lập. Hệ số $\gamma^t$ không được bỏ: nó đi kèm quy ước $J(\theta)=\mathbb E[G_0]$.

**Kiểm tra.** Vì sao $\mathbb E[G_{<t}\psi_t]=0$? — $G_{<t}$ đo được theo $H_t$, còn kỳ vọng có điều kiện của $\psi_t$ theo $H_t$ bằng $0$.

*Nguồn: tr. 39–40.*

<!-- note-topic-id: lec-09-topic-12 -->
### REINFORCE episodic

**Thuật toán Monte Carlo** (tr. 40; sửa thứ tự thu thập và hệ số chiết khấu so với nguồn — sửa có chủ ý để nhất quán với $J(\theta)=\mathbb E[G_0]$):

1. Khởi tạo $\theta$ tùy ý, chọn $\alpha>0$, $0\le\gamma<1$.
2. Với mỗi episode: chép $\theta_{\mathrm{old}}\leftarrow\theta$; thu **trọn episode** dưới $\pi_{\theta_{\mathrm{old}}}$; giữ $\theta_{\mathrm{old}}$ cố định đến khi cộng xong.
3. Tính mọi $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$ lùi từ $T-1$ về $0$.
4. Cộng $\widehat g=\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$.
5. Cập nhật **một lần**: $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\,\widehat g$.

Không tuyên bố không chệch/hội tụ nếu thiếu các giả thiết ở topic-07. Đây là ước lượng một mẫu; từng episode không bảo đảm cải thiện $J$.

::: example
**Áp dụng cho softmax.** Dùng lại $\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$, $\theta=(\log 2,0)$ nên $\pi_\theta(1\mid s)=2/3$, $\psi_\theta(s,1)=(\tfrac13,-\tfrac13)$. Một episode một bước chọn hành động 1, nhận $G_0=3$; $\alpha=0{,}1$:

$$\widehat g=3\big(\tfrac13,-\tfrac13\big)=(1,-1),\qquad \theta_{\mathrm{new}}=(\log 2+0{,}1,\,-0{,}1),$$

$$\pi_{\theta_{\mathrm{new}}}(1\mid s)=\frac{2e^{0{,}1}}{2e^{0{,}1}+e^{-0{,}1}}\approx0{,}710>\tfrac23.$$

Return dương tăng chênh lệch logit giữa hai hành động thêm $0{,}2$, nên xác suất của hành động đã nhận return dương tăng.
:::

**Kiểm tra.** Vì sao cập nhật một lần sau episode thay vì từng bước? — Vì $G_t$ cần toàn bộ phần thưởng tương lai của episode và $\theta_{\mathrm{old}}$ phải cố định trong khi thu.

*Nguồn: tr. 40.*

<!-- note-topic-id: lec-09-topic-11 -->
### Phân bố chiếm dụng chiết khấu

Phần bổ sung; có thể lược khi thiếu thời gian.

Đặt $Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$. Nếu chân trời cưỡng bức phụ thuộc $t$, ghép $t$ vào trạng thái; trạng thái hấp thụ có $Q^\pi=0$. Phân bố chiếm dụng chuẩn hóa:

$$d_{\rho_0,\gamma}^{\pi}(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi(S_t=s),$$

với hệ số $1/(1-\gamma)$ bảo đảm $\sum_s d^\pi(s)=1$. Trọng số $\gamma^t$ trong ước lượng quỹ đạo chính là trọng số tạo phân bố lượt thăm — lượt thăm muộn được tính ít hơn. Khi đó:

$$\mathbb E\Big[\sum_{t\ge0}\gamma^tG_t\psi_t\Big]=\frac1{1-\gamma}\,\mathbb E_{S\sim d^\pi,\,A\sim\pi}\!\big[Q^\pi(S,A)\,\psi_\theta(S,A)\big]=\nabla_\theta J(\theta),$$

vì kỳ vọng có điều kiện thay $G_t$ bằng $Q^\pi$. Đây là **cách viết thứ hai** của cùng một định lý: dạng quỹ đạo (topic-10) và dạng phân bố chiếm dụng. Các giả thiết khả vi, miền hỗ trợ và khả tích đã nêu ở topic-07 vẫn áp dụng.

*Nguồn: tr. 39 và suy diễn.*

---

## 7. Tổng kết và chuyển tiếp

<!-- note-topic-id: lec-09-topic-14 -->
### Đọc thêm: sai phân hữu hạn

Đọc thêm, ngoài tuyến chính. Từ định nghĩa đạo hàm, xấp xỉ từng thành phần:

$$\frac{\partial J(\theta)}{\partial\theta_k}\approx\frac{J(\theta+\epsilon u_k)-J(\theta)}{\epsilon},$$

với $u_k$ là véc-tơ đơn vị hướng $k$ (tr. 33). Đơn giản, áp dụng được cho chính sách bất kỳ kể cả không khả vi, nhưng nhiễu lớn, kém hiệu quả khi số tham số lớn — vì vậy tuyến chính của bài dùng hàm điểm thay vì sai phân.

*Nguồn: tr. 33.*

<!-- note-topic-id: lec-09-topic-13 -->
### Cầu nối: baseline và actor–critic

Baseline và actor–critic được triển khai ở Bài 10.

Ước lượng $\widehat g=\sum_t\gamma^tG_t\psi_t$ dùng return Monte Carlo nên có phương sai lớn. Bài kế tiếp dùng **baseline** để giảm phương sai mà không gây chệch, và **actor–critic** để bootstrap giá trị thay vì chờ hết episode. Hai trong bốn hợp đồng của bài này — hàm điểm chỉ dùng nơi mật độ dương, chỉ số return nhất quán — vẫn giữ nguyên khi thêm baseline.

*Nguồn: tr. 40, chỉ báo trước.*

### Bốn hợp đồng cần giữ

1. **Double DQN:** online chọn; target đánh giá; kết thúc che bootstrap; đích dừng gradient.
2. **Chính sách:** phân phối đúng miền hành động (xác suất ở rời rạc, mật độ ở liên tục); hàm điểm chỉ dùng nơi mật độ dương.
3. **REINFORCE:** chỉ số return nhất quán ($\gamma^tG_t$); thu dưới tham số cũ; cộng rồi cập nhật một lần.
4. **Sai lệch cực đại:** thu hồi bất đẳng thức Jensen $\mathbb E\big[\max_a\widehat Q_a\big]\ge\max_a\mathbb E[\widehat Q_a]$; kết luận là về kỳ vọng, không về từng lần lấy max.

---

## Bài tập củng cố

### X01 — Sai lệch Rademacher và hai đích

::: exercise
1. Liệt kê bốn cặp giá trị $(\varepsilon_1,\varepsilon_2)$ Rademacher độc lập và kiểm lại $\mathbb E[\max_a\widehat Q_a]=1/2$ khi giá trị thật bằng $0$.
2. Với $r=1$, $\gamma=0{,}8$, $Z=0$, $Q_{\theta^-}(s',\cdot)=(2,7)$ và $Q_\theta(s',\cdot)=(4,1)$, tính đích DQN và đích Double DQN.
:::

::: hint
Phần 1: đếm trong bốn cặp đồng xác suất có bao nhiêu cặp cho cực đại bằng $-1$. Phần 2: DQN để $Q_{\theta^-}$ vừa chọn vừa đánh giá; Double DQN lấy argmax theo $Q_\theta$ rồi đánh giá bằng $Q_{\theta^-}$.
:::

::: solution
1. Bốn cặp: $(-1,-1)\to\max=-1$; $(-1,1),(1,-1),(1,1)\to\max=1$. Kỳ vọng $\tfrac14(-1)+\tfrac34(1)=\tfrac12$, trong khi $\max_a\mathbb E[\widehat Q_a]=0$.
2. DQN: mạng mục tiêu chọn hành động 2 (giá trị $7$), $y^{\mathrm{DQN}}=1+0{,}8\cdot 7=6{,}6$. Double DQN: mạng online chọn hành động 1 (giá trị $4$), mạng mục tiêu đánh giá $2$, $y^{\mathrm{DDQN}}=1+0{,}8\cdot 2=2{,}6$.
:::

### X02 — Hai hàm điểm

::: exercise
1. Với ví dụ softmax $\pi_\theta(1\mid s)=2/3$, $\pi_\theta(2\mid s)=1/3$, $\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$: tính $\psi_\theta(s,2)$ và kiểm $\mathbb E_{A\sim\pi}[\psi_\theta(s,A)]=0$.
2. Với Gaussian: đổi thành $a=-1$, giữ $\phi(s)=(1,2)$, $\mu=0$, $\sigma^2=1$. Tính $\psi_\theta(s,a)$.
:::

::: hint
Phần 1: hàm điểm là đặc trưng hành động trừ trung bình đặc trưng theo chính sách; kỳ vọng có trọng số bằng xác suất $\pi_\theta(b\mid s)$. Phần 2: dùng $\psi=(a-\mu)/\sigma^2\cdot\phi(s)$.
:::

::: solution
1. $\psi_\theta(s,2)=(0,1)-(\tfrac23,\tfrac13)=(-\tfrac23,\tfrac23)$. Kỳ vọng: $\tfrac23(\tfrac13,-\tfrac13)+\tfrac13(-\tfrac23,\tfrac23)=(0,0)$.
2. $\psi_\theta(s,-1)=\dfrac{-1-0}{1}(1,2)=(-1,-2)$.
:::

### X03 — Kiểm cập nhật REINFORCE

::: exercise
1. Giữ dữ kiện ví dụ softmax ($\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$, $\theta=(\log 2,0)$, $\pi_\theta(1\mid s)=2/3$, episode một bước chọn hành động 1, $\alpha=0{,}1$) nhưng đặt $G_0=-3$. Tính $\theta_{\mathrm{new}}$ và $\pi_{\theta_{\mathrm{new}}}(1\mid s)$.
2. Episode hai bước với $R_1=1$, $R_2=2$, $\gamma=0{,}9$: tính $G_0$ và $G_1$.
3. Nêu tham số phải giữ cố định trong khi thu một episode nhiều bước.
:::

::: hint
Phần 1: $\widehat g=G_0\,\psi_\theta(s,1)$; return âm đảo hướng cập nhật. Phần 2: $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$ với $T=2$. Phần 3: hợp đồng lấy mẫu của REINFORCE episodic.
:::

::: solution
1. $\widehat g=-3(\tfrac13,-\tfrac13)=(-1,1)$, nên $\theta_{\mathrm{new}}=(\log 2-0{,}1,\;0{,}1)$ và
$$\pi_{\theta_{\mathrm{new}}}(1\mid s)=\frac{2e^{-0{,}1}}{2e^{-0{,}1}+e^{0{,}1}}\approx0{,}621<\tfrac23.$$
Xác suất hành động 1 giảm vì return âm.
2. $G_1=R_2=2$; $G_0=R_1+\gamma R_2=1+0{,}9\cdot 2=2{,}8$.
3. $\theta_{\mathrm{old}}$ phải giữ cố định trong khi thu trọn episode; chỉ cập nhật một lần sau khi cộng xong $\widehat g$.
:::

---

## Tài liệu tham khảo

1. Tạ Việt Cường. *Bài giảng 10: Policy Gradient* (bản trích dùng cho Bài 09: lecture09-ddqn-and-policy-gradient-part1.pdf, tr. 1–40). Phòng thí nghiệm HMI, Trường Đại học Công nghệ, Học kỳ 1, 2026–2027.
2. Mnih, V. và cộng sự. "Human-level control through deep reinforcement learning." *Nature* 518 (2015): 529–533. (Experience replay, target network, thuật toán DQN — tr. 5–10.)
3. van Hasselt, H. "Double Q-learning." *NeurIPS* 2010. (Double Q-learning dạng bảng — tr. 20–21.)
4. van Hasselt, H., Guez, A., Silver, D. "Deep Reinforcement Learning with Double Q-learning." *AAAI* 2016. (Double DQN — tr. 14–19.)
5. Williams, R. J. "Simple statistical gradient-following algorithms for connectionist reinforcement learning." *Machine Learning* 8 (1992): 229–256. (REINFORCE — tr. 40.)
6. Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. (Định lý gradient chính sách, phân bố chiếm dụng — tr. 39.)
