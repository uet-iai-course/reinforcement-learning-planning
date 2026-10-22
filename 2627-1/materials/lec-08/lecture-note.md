# Bài 08 — Deep Q-Learning

Trong chương này, chúng ta thay hàm tuyến tính $\hat q(s,a,w)=x(s,a)^\top w$ của Bài 07 bằng một mạng nơ-ron nhận quan sát và trả về một giá trị cho mỗi hành động trong tập hữu hạn, rồi xây dựng thuật toán Deep Q-Network (DQN) từ bốn thành phần: đích hồi quy có mặt nạ kết thúc, bộ nhớ phát lại (experience replay), hàm mất mát với dừng gradient và mạng mục tiêu (target network). Bộ nhớ phát lại và mạng mục tiêu giảm bất ổn khi huấn luyện, nhưng DQN vẫn có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, tức đủ ba yếu tố của bộ ba bất ổn (deadly triad) ở Bài 07, nên thuật toán không có bảo đảm hội tụ tổng quát.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đọc vector giá trị hành động $\mathbf q_\theta(o)\in\mathbb R^{\lvert\mathcal A\rvert}$ do mạng trả về, chọn giá trị $Q_\theta(o,a)$ của hành động đã thực hiện, và tính đích hồi quy của một mẫu chuyển; phân biệt mẫu kết thúc (đích không chứa phần bootstrap) với mẫu bị cắt ngắn (đích vẫn chứa phần bootstrap).
2. Nêu tác dụng và giới hạn của bộ nhớ phát lại: giảm tương quan giữa các mẫu liền nhau nhưng không tạo dữ liệu độc lập cùng phân phối theo một phân phối cố định; chỉ ra hai nguồn dữ liệu khác chính sách và tính xác suất hai mẫu liền nhau cùng vào một mini-batch.
3. Tính hàm mất mát và gradient của nó theo các dự đoán trên một mini-batch, chỉ ra phần nào không nhận gradient, và truy dấu một vòng của thuật toán DQN với hai bộ đếm $t$ và $k_{\mathrm{opt}}$.
4. Viết hạ gradient ngẫu nhiên (SGD), RMSprop và Adam theo từng tọa độ; nêu những gì lựa chọn bộ tối ưu không thay đổi: công thức đích, cách thu thập dữ liệu và lớp hàm.
5. Tính độ thay đổi của đích một mẫu khi đồng bộ mạng mục tiêu; nêu giả thiết còn thiếu để có bảo đảm hội tụ khi DQN có đủ bộ ba bất ổn.
6. Giải một bước DQN trên một mini-batch có cả mẫu kết thúc lẫn mẫu bị cắt ngắn, nêu kết quả và giả thiết đã dùng ở mỗi bước tính.

<!-- note-topic-id: lec-08-topic-13 -->
## Kiến thức tiên quyết

Kết quả của bài trước được dẫn theo mục của ghi chú bài đó, dạng "ghi chú Bài 06, Mục 4", và phát biểu lại dưới đây.

- **Q-learning dạng bảng** (ghi chú Bài 06, Mục 4, Định nghĩa 06.15, Thuật toán 06.16). Trên một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn, sau khi thực hiện $A_t$ tại $S_t$ và nhận phần thưởng $R_{t+1}$, trạng thái $S_{t+1}$, Q-learning cập nhật đúng một ô của bảng:
  $$Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t\Bigl[R_{t+1}+\gamma\max_{a'}Q_t(S_{t+1},a')-Q_t(S_t,A_t)\Bigr],$$
  các ô khác giữ nguyên, và $Q(s,\cdot)=0$ khi $s$ là trạng thái kết thúc. Ở đây $\alpha_t\in(0,1]$ là bước học của cặp $(S_t,A_t)$ tại lần cập nhật này và $\gamma\in[0,1)$ là hệ số chiết khấu. Biểu thức trong ngoặc vuông, trừ số hạng $Q_t(S_t,A_t)$, là mục tiêu cập nhật; nó chứa ước lượng hiện tại $Q_t$ nên là mục tiêu bootstrap (bootstrap target).
- **Chính sách hành vi, chính sách đích và học khác chính sách** (ghi chú Bài 06, Mục 1 và Mục 4, Định nghĩa 06.3, 06.14, Nhận xét 06.17). Chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy) theo $Q$ với $m$ hành động chọn hành động tham lam với xác suất $1-\varepsilon+\varepsilon/m$ và mỗi hành động khác với xác suất $\varepsilon/m$. Trong Q-learning, chính sách hành vi $\varepsilon$-tham lam sinh dữ liệu, còn chính sách đích là chính sách tham lam theo $Q$; hai chính sách khác nhau nên Q-learning học khác chính sách (off-policy). Với chính sách đích tham lam $\pi$, $\max_{a'}Q(S_{t+1},a')=\sum_{a'}\pi(a'\mid S_{t+1})Q(S_{t+1},a')$, tức phép cực đại chính là kỳ vọng theo chính sách đích. Q-learning một bước không cần tỉ số lấy mẫu quan trọng (importance sampling ratio) vì hai lẽ: $A_t$ là đối số điều kiện của ô $Q(S_t,A_t)$, ô ước lượng $q_*(S_t,A_t)$, nên việc hành vi chọn $A_t$ không làm lệch mục tiêu; còn phần tiếp nối tại $S_{t+1}$ được tính trọn bằng phép cực đại trên bảng, không qua một hành động lấy mẫu từ hành vi. Hành vi vẫn quyết định cặp nào được cập nhật: một cặp không bao giờ được chọn giữ mãi giá trị khởi tạo.
- **Hội tụ của Q-learning dạng bảng** (ghi chú Bài 06, Mục 5, Định nghĩa 06.19, Định lý 06.21). Giả sử MDP hữu hạn với động lực không đổi theo thời gian, phần thưởng bị chặn, $0\le\gamma<1$, mẫu sinh từ chính MDP, mọi cặp $(s,a)$ được cập nhật vô hạn lần, và với mỗi cặp, dãy bước học thỏa điều kiện Robbins–Monro $\sum_n\alpha_n(s,a)=\infty$, $\sum_n\alpha_n(s,a)^2<\infty$. Khi đó $Q_t(s,a)\to q_*(s,a)$ hầu chắc chắn với mọi cặp. Kết quả là tiệm cận và chỉ áp dụng cho biểu diễn bảng; chính sách hành vi tùy ý miễn là phủ mọi cặp.
- **Xấp xỉ tuyến tính và Q-learning bán gradient** (ghi chú Bài 07, Mục 1 và Mục 5, Định nghĩa 07.35). Bảng được thay bằng $\hat q(s,a,w)=x(s,a)^\top w$, với $x(s,a)\in\mathbb R^d$ là vector đặc trưng chọn trước và $w\in\mathbb R^d$ dùng chung cho mọi cặp. Với mục tiêu $y_t=R_{t+1}+\gamma\max_{a'}\hat q(S_{t+1},a',w_n)$, hoặc $y_t=R_{t+1}$ khi $S_{t+1}$ kết thúc, cập nhật bán gradient (semi-gradient) là $w_{n+1}=w_n+\alpha_n\bigl(y_t-\hat q(S_t,A_t,w_n)\bigr)x(S_t,A_t)$: mục tiêu được coi là hằng khi lấy gradient, dù nó phụ thuộc $w_n$. Tại bước cắt ngắn, $S_{t+1}$ chưa kết thúc nên mục tiêu vẫn chứa phép cực đại.
- **Bộ ba bất ổn** (ghi chú Bài 07, Mục 5, Mệnh đề 07.37, Định nghĩa 07.38). Một phương pháp học giá trị có bộ ba bất ổn (deadly triad) khi có đồng thời xấp xỉ hàm, bootstrap và học khác chính sách. Q-learning bán gradient có cả ba, nên không có bảo đảm hội tụ chung. Mệnh đề 07.37 cho một ví dụ phân kỳ của TD(0) khác chính sách cùng ba yếu tố: với $x(s_1)=1$, $x(s_2)=2$, chỉ cập nhật chuyển $s_1\to s_2$ có phần thưởng $0$, $\gamma\in(\tfrac12,1)$ và $\alpha>0$, tham số thỏa $w_n=\bigl(1+\alpha(2\gamma-1)\bigr)^nw_0$, nên $\lvert w_n\rvert\to\infty$ khi $w_0\ne0$.
- **Mạng nơ-ron và lan truyền ngược** (kiến thức học máy tiên quyết, không thuộc ghi chú Bài 01–07; Goodfellow, Bengio và Courville, 2016, Chương 6 và 9). Mạng nhiều tầng (multilayer perceptron, MLP) là hợp của các ánh xạ affine và hàm kích hoạt phi tuyến; mạng tích chập (convolutional neural network, CNN) dùng các tầng tích chập có trọng số dùng chung trên mọi vị trí của ảnh. Cả hai là hàm khả vi theo vector tham số $\theta$, và lan truyền ngược (backpropagation) tính gradient của một hàm mất mát vô hướng theo $\theta$ bằng quy tắc dây chuyền. Chúng ta chỉ dùng mạng như một hàm khả vi theo $\theta$.

## Bảng ký hiệu

Bảng gồm ký hiệu dùng xuyên suốt chương; ký hiệu dùng một lần được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal O$, $O_t$ | tập quan sát; quan sát đưa vào mạng ở bước $t$ | tập; phần tử của $\mathcal O$ (ảnh hoặc vector) |
| $S_t$ | trạng thái của MDP; chỉ dùng thay $O_t$ khi $O_t$ đủ Markov | $\mathcal S$ |
| $\mathcal A$, $\lvert\mathcal A\rvert$, $A_t$ | tập hành động; số hành động; hành động ở bước $t$ | tập hữu hạn |
| $R_{t+1}$ | phần thưởng nhận sau $A_t$ | $\mathbb R$ |
| $\gamma$ | hệ số chiết khấu | $[0,1)$ |
| $Z_{t+1}$, $U_{t+1}$ | cờ kết thúc của MDP; cờ cắt ngắn ngoài mô hình | $\{0,1\}$ |
| $q_*$ | giá trị hành động tối ưu | hàm thực trên $\mathcal S\times\mathcal A$ |
| $\theta$, $\theta^-$, $d$ | tham số mạng trực tuyến; tham số mạng mục tiêu; số tham số | $\mathbb R^d$; $d\in\mathbb N_+$ |
| $Q_\theta(o,a)$, $\mathbf q_\theta(o)$ | giá trị hành động do mạng tính; vector các giá trị đó theo mọi hành động | $\mathbb R$; $\mathbb R^{\lvert\mathcal A\rvert}$ |
| $t$ | bộ đếm bước môi trường | $\mathbb N_0$ |
| $k_{\mathrm{opt}}$, $j$ | bộ đếm bước tối ưu; chỉ số bước trong công thức của bộ tối ưu, $j=k_{\mathrm{opt}}$ sau khi tăng | $\mathbb N_0$; $\mathbb N_+$ |
| $\mathcal D$, $N$ | bộ nhớ phát lại; dung lượng của nó | tập mẫu chuyển; $\mathbb N_+$ |
| $b$, $i$ | cỡ mini-batch; chỉ số mẫu trong mini-batch | $\mathbb N_+$; $\{1,\dots,b\}$ |
| $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ | mẫu chuyển thứ $i$ của mini-batch | bộ sáu thành phần |
| $q_i$, $y_i$, $\delta_i$ | dự đoán $Q_\theta(O_i,A_i)$; đích hồi quy; sai số TD $y_i-q_i$ (dạng theo thời gian: $q_t$, $y_t$, $\delta_t$) | $\mathbb R$ |
| $L_B(\theta)$ | hàm mất mát trên mini-batch $B$ | $\mathbb R^d\to[0,\infty)$ |
| $\operatorname{sg}$ | phép dừng gradient: giữ giá trị, đạo hàm bằng $0$ | ánh xạ |
| $N_{\mathrm{start}}$, $F$, $C$ | số mẫu tối thiểu trước bước tối ưu đầu; số bước môi trường giữa hai lần tối ưu; số bước tối ưu giữa hai lần đồng bộ | $\mathbb N_+$, $b\le N_{\mathrm{start}}\le N$ |
| $\epsilon_{\mathrm{exp}}$ | xác suất thăm dò của chính sách hành vi | $[0,1]$ |
| $\eta$, $g_j$ | tốc độ học; gradient mini-batch ở bước tối ưu $j$ | $(0,\infty)$; $\mathbb R^d$ |
| $\rho$, $\beta_1$, $\beta_2$, $m_j$, $v_j$ | hệ số suy giảm và trung bình trượt của RMSprop và Adam | $[0,1)$; $\mathbb R^d$ |
| $\epsilon_{\mathrm{opt}}$ | hằng số ổn định trong mẫu số của bộ tối ưu | $(0,\infty)$ |

Quy ước đọc. $R_{t+1}$ gắn với chuyển từ bước $t$ sang bước $t+1$. Khi tương tác với môi trường, mẫu chuyển viết theo thời gian $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$; sau khi lấy mini-batch, chỉ số $i$ không mang thứ tự thời gian nên mẫu viết $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, không dùng $R_{i+1}$ hay $O_{i+1}$. Hai bộ đếm $t$ và $k_{\mathrm{opt}}$ tăng theo hai nhịp khác nhau: $t$ sau mỗi bước môi trường, $k_{\mathrm{opt}}$ sau mỗi lần cập nhật $\theta$. Kỳ vọng trên mini-batch lấy theo phép lấy mẫu đều từ $\mathcal D$ hiện tại.

Một số chữ trùng với bài trước nhưng mang nghĩa khác. $\epsilon_{\mathrm{exp}}$ là $\varepsilon$ của Bài 06–07; chỉ số dưới tách nó khỏi $\epsilon_{\mathrm{opt}}$. $q_i$ là dự đoán của mạng trên mẫu $i$, khác giá trị thật $q_*$. $m_j$, $v_j$ là trung bình trượt của gradient, khác hàm giá trị $v_\pi$; $\rho$ là hệ số suy giảm của RMSprop, khác tỉ số lấy mẫu quan trọng $\rho_t$ của Bài 06–07. Bài 06–07 viết $m$ cho số hành động; ở đây ta viết $\lvert\mathcal A\rvert$. Tham số $\theta$ đóng vai của $w$ ở Bài 07, và $Q_\theta(o,a)$ thay $\hat q(s,a,w)$. Ví dụ một tham số ở phần 2 dùng bước học $\alpha$ của Bài 07; từ phần 4, tốc độ học của bộ tối ưu viết $\eta$.

Ứng với giáo trình *Học máy thống kê*: $q_*$ là $Q^*$, và $q_\pi$ là $Q^\pi$.

---

## Bản đồ chủ đề (bốn nhóm)

### Nhóm cầu nối

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-13` | Kiến thức tiên quyết: Q-learning dạng bảng (Bài 06), Q-learning bán gradient và bộ ba bất ổn (Bài 07) | tr. 3–7 | Nhắc quy tắc cập nhật, học khác chính sách, điều kiện hội tụ | Vào: Bài 06–07 → Ra: mục tiêu bootstrap và phạm vi bảo đảm |
| `lec-08-topic-17` | Mở đầu: mục tiêu, nội dung và bài toán trung tâm | tr. 1–2, 8–13 | Nêu bài toán và câu trả lời có điều kiện của từng phần | Vào: Bài 06–07 → Ra: khung cho phần 2–6 |

### Nhóm cốt lõi

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-01` | Giới hạn của bảng giá trị hành động | tr. 8–15 | Đặt vấn đề quy mô và khái quát hóa | Vào: topic-13 → Ra: nhu cầu $Q_\theta$ |
| `lec-08-topic-16` | Đầu vào bốn khung Atari và tính Markov | tr. 17, 35 | Ví dụ cho giao diện mạng; giới hạn của bốn khung | Vào: topic-01 → Ra: quan sát $O_t$ cho topic-02 |
| `lec-08-topic-02` | Mạng giá trị hành động, đích di động và mạng mục tiêu | tr. 14–17, 20, 31, 33, 35 | Định nghĩa $\mathbf q_\theta$, $Q_\theta$; giả thiết Markov khi viết mục tiêu; $Q_{\theta^-}$ | Vào: topic-01, topic-16 → Ra: $\mathbf q_\theta$ và hai bản sao mạng |
| `lec-08-topic-03` | Đích hồi quy | tr. 16, 20–22, 34 | Đích $y_t$ và sai số TD | Vào: topic-02 → Ra: nhãn hồi quy |
| `lec-08-topic-04` | Ví dụ: đích tại mẫu chuyển kết thúc | tr. 21 | Phân biệt $Z$ và $U$ | Vào: topic-03 → Ra: đích đúng |
| `lec-08-topic-05` | Kết thúc và cắt ngắn | tr. 21 | Hai cờ $Z$, $U$; mặt nạ chỉ dùng $Z$ | Vào: topic-04 → Ra: bộ sáu thành phần |
| `lec-08-topic-18` | Tương quan giữa các mẫu chuyển liên tiếp | tr. 19, 30 | Vấn đề của mẫu liền nhau | Vào: topic-05 → Ra: nhu cầu bộ nhớ phát lại |
| `lec-08-topic-06` | Bộ nhớ phát lại | tr. 18–20, 32 | Bộ đệm vòng dung lượng $N$, ghi đè mẫu cũ nhất, rút đều; quan sát cuối khi tự đặt lại | Vào: topic-18 → Ra: mini-batch |
| `lec-08-topic-19` | Dữ liệu khác chính sách trong bộ nhớ | tr. 6–7, 19, 32 | Hai nguồn khác chính sách; đích một bước không cần tỉ số lấy mẫu quan trọng | Vào: topic-06 → Ra: phạm vi của đích trên dữ liệu cũ |
| `lec-08-topic-07` | Giới hạn của bộ nhớ phát lại | tr. 19, 29–32 | Ba việc làm được, ba điều không bảo đảm; câu hỏi $N=6$, $b=2$ | Vào: topic-19 → Ra: phát biểu đúng phạm vi; nhu cầu hàm mất mát cho phần 4 |
| `lec-08-topic-08` | Gather và dừng gradient | tr. 16, 22, 34 | Đồ thị tính toán | Vào: topic-03 → Ra: loss batch |
| `lec-08-topic-09` | Mất mát và gradient batch | tr. 21–22, 34 | MSE và $\nabla_\theta L$ | Vào: topic-08 → Ra: gradient cho optimizer |
| `lec-08-topic-10` | Vòng DQN: hai đồng hồ $t$ và $k_{\mathrm{opt}}$ | tr. 18–22 | Giả mã đầy đủ | Vào: topic-05–09 → Ra: thuật toán hoàn chỉnh |
| `lec-08-topic-11` | Hợp đồng tensor của batch | tr. 14–22, 35 | Kích thước và kiểu tensor | Vào: topic-09 → Ra: kiểm tra cài đặt |
| `lec-08-topic-12` | Mạng mục tiêu và các nguồn bất ổn | tr. 19, 21, 29–33 | Đồng bộ đích và giới hạn ổn định | Vào: topic-10 → Ra: phạm vi bảo đảm của DQN |

### Nhóm bổ sung

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-14` | SGD, RMSprop, Adam theo từng tọa độ | tr. 22–28 | Ba quy tắc cập nhật và giới hạn | Vào: topic-09 → Ra: lựa chọn optimizer có căn cứ |

### Nhóm đọc thêm/thực hành

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-15` | Kiểm tra tổng hợp, ba bài thảo luận, đọc thêm | tr. 12–13, 29–36 | Ứng dụng và tổng kết | Vào: topic-12, 14 → Ra: kết luận cuối tệp |

### Bảy phần của chương

Chúng ta đi qua bảy phần sau.

1. Mở đầu: kiến thức tiên quyết, ký hiệu, mục tiêu và bài toán trung tâm (`lec-08-topic-13`, `lec-08-topic-17`).
2. Mạng giá trị hành động và đích hồi quy: giới hạn của bảng, đầu vào bốn khung Atari, mạng giá trị hành động, mạng mục tiêu, đích có mặt nạ kết thúc, kết thúc và cắt ngắn (`lec-08-topic-01`, `lec-08-topic-16`, `lec-08-topic-02` đến `lec-08-topic-05`).
3. Bộ nhớ phát lại: tương quan giữa các mẫu chuyển liên tiếp, cơ chế lưu và lấy mẫu đều, dữ liệu khác chính sách, giới hạn (`lec-08-topic-18`, `lec-08-topic-06`, `lec-08-topic-19`, `lec-08-topic-07`).
4. Hàm mất mát và thuật toán DQN: hàm mất mát trên mini-batch, dừng gradient, vòng huấn luyện, kích thước tensor (`lec-08-topic-08` đến `lec-08-topic-11`).
5. Bộ tối ưu theo gradient: SGD, RMSprop, Adam theo từng tọa độ (`lec-08-topic-14`).
6. Bất ổn và phạm vi bảo đảm của DQN: hai nguồn bất ổn, độ thay đổi của đích khi đồng bộ, bộ ba bất ổn (`lec-08-topic-12`).
7. Tổng kết và chuyển tiếp: kết quả và giả thiết, bài tập tổng hợp, câu hỏi tự kiểm tra (`lec-08-topic-15`).

Đọc trước: Sutton và Barto (2018), §11.3 (bộ ba bất ổn) và §16.5 (DQN trên trò chơi Atari); Mnih và cộng sự (2015).

---

## 1. Mở đầu

<!-- note-topic-id: lec-08-topic-17 -->
### Bài toán trung tâm của chương

Bài 06 học $q_*$ bằng một bảng có một ô cho mỗi cặp trạng thái–hành động, và Bài 07 thay bảng bằng hàm tuyến tính theo đặc trưng chọn trước. Bài toán của chương này là học $q_*$ khi quan sát là vector liên tục hoặc ảnh, tập hành động hữu hạn và mô hình của môi trường không được cho. Với quan sát như vậy, bảng hoặc quá lớn, hoặc phần lớn ô không có mẫu (Mục 2), và với ảnh cũng không có sẵn bộ đặc trưng chọn tay. Chúng ta dùng một mạng nơ-ron trả về giá trị của mọi hành động và học tham số của mạng từ các mẫu chuyển. Bài giảng gốc (trang 12) nêu bốn khó khăn của bước thay này: hàm mất mát không lồi theo tham số, nên không có bảo đảm hội tụ toàn cục; mục tiêu bootstrap phụ thuộc chính mạng đang học; phân phối dữ liệu đổi theo chính sách hành vi; và phương pháp có đủ bộ ba bất ổn.

Chúng ta trả lời bài toán theo từng phần; mỗi câu trả lời dưới đây đúng dưới một điều kiện.

2. Mạng trả về vector giá trị của mọi hành động. Khi đích được tính bằng một bản sao của mạng giữ cố định giữa hai lần đồng bộ, mỗi mẫu chuyển có một nhãn hồi quy cố định.
3. Khi mini-batch được lấy đều từ bộ nhớ phát lại, tương quan ngắn hạn giữa các mẫu giảm; dữ liệu vẫn chưa độc lập cùng phân phối theo một phân phối cố định.
4. Khi gradient được chặn ở đích, chỉ giá trị dự đoán của hành động đã thực hiện nhận gradient.
5. Bộ tối ưu chỉ quyết định cách đổi gradient thành bước tham số. Công thức đích, cơ chế thu thập dữ liệu và lớp hàm không phụ thuộc lựa chọn bộ tối ưu, nên không bộ tối ưu nào loại được các nguồn bất ổn của phần 6.
6. Khi có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, DQN không có bảo đảm hội tụ tổng quát, và các kết luận về hiệu quả của DQN gốc chủ yếu dựa trên thí nghiệm.

Bài giảng gốc (trang 9 và 11) còn nêu hai cận độ phức tạp mẫu: $\tilde O\bigl(\lvert\mathcal S\rvert\lvert\mathcal A\rvert/((1-\gamma)^4\varepsilon_{\mathrm{acc}}^2)\bigr)$ mẫu để Q-learning dạng bảng đạt chính sách $\varepsilon_{\mathrm{acc}}$-tối ưu, và $\tilde O\bigl(d/((1-\gamma)^3\varepsilon_{\mathrm{acc}}^2)\bigr)$ cho xấp xỉ hàm với $d$ đặc trưng; ở đây $\varepsilon_{\mathrm{acc}}$ là sai số cho phép của chính sách, khác $\epsilon_{\mathrm{exp}}$. Sai số đo bằng $v_\pi(s)\ge v_*(s)-\varepsilon_{\mathrm{acc}}$ với mọi $s$ (trang 8), nhưng nguồn không nêu mô hình lấy mẫu (bộ sinh độc lập hay dọc một quỹ đạo) và xác suất thành công, chỉ nêu định tính điều kiện khám phá và bao phủ; cận thứ hai không gắn với một thuật toán cụ thể. Vì vậy chúng ta không dùng hai cận như định lý. Hai ý vẫn dùng ở phần sau: số ô của bảng tăng theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$, và xấp xỉ hàm chỉ có bảo đảm khi có thêm giả thiết cấu trúc, chẳng hạn $q_*$ nằm trong lớp hàm và dữ liệu bao phủ đủ (bài giảng gốc, trang 11).


## 2. Mạng giá trị hành động và đích hồi quy

<!-- note-topic-id: lec-08-topic-01 -->
### Giới hạn của bảng giá trị hành động

**Vấn đề.** Q-learning dạng bảng giữ một ô cho mỗi cặp trạng thái–hành động, và một ô chỉ đổi khi chính cặp đó xuất hiện trong dữ liệu. Bảng có $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$ ô, nên chỉ dùng được khi số trạng thái nhỏ và mỗi cặp được thăm đủ nhiều lần. Ví dụ sau đo hai điều kiện này trên một bài toán điều khiển đã gặp ở Bài 05–07.

::: example Ví dụ 08.1 (Lunar Lander rời rạc hóa thành bảng)
**Dữ kiện.** Thực hành Bài 05 chia sáu biến liên tục của tàu đổ bộ thành $3\cdot4^5=3\,072$ ô và ghép với số chân đang chạm đất ($0$, $1$ hoặc $2$), được $9\,216$ ô trạng thái. Trên $2\,000$ lượt của một chính sách cố định, $1\,896$ ô được ghé ít nhất một lần (notebook Lunar Lander của Bài 07, mục 5; ghi chú Bài 07, Ví dụ 07.1). Tàu có bốn hành động.

**Tính.** Tỉ lệ ô có mẫu là $1\,896/9\,216\approx0{,}206$; $9\,216-1\,896=7\,320$ ô chỉ giữ giá trị khởi tạo. Bảng giá trị hành động trên cùng lưới có $9\,216\cdot4=36\,864$ ô.

**Diễn giải.** Khoảng bốn phần năm số ô trạng thái không có dữ liệu sau $2\,000$ lượt, dù ô bên cạnh đã được ghé nhiều lần; với bảng giá trị hành động, mỗi ô trạng thái còn tách thành bốn ô.
:::

Khi quan sát là ảnh, số quan sát khác nhau có thể gặp quá lớn để liệt kê, và gần như mọi quan sát mới là một ô chưa có mẫu. Bảng vì thế không dùng được, cả về bộ nhớ lẫn về dữ liệu.

**Trực quan.** Thay bảng bằng một hàm có tham số dùng chung $\theta$, chẳng hạn một mạng nơ-ron $Q_\theta(o,a)$ nhận quan sát $o$. Hàm cho giá trị ở cả quan sát chưa gặp, và một cập nhật theo $\theta$ đổi giá trị ở nhiều quan sát cùng lúc. Đây là cơ chế tổng quát hóa của Bài 07 (mức lan của một cập nhật, Mệnh đề 07.2), với mạng thay cho hàm tuyến tính theo đặc trưng chọn trước.

![Bên trái: bảng minh họa 4 hàng, 5 cột, 4 trong 20 ô có mẫu (đánh dấu chấm), 16 ô chưa có mẫu; mỗi ô lưu độc lập. Bên phải: quan sát o vào mạng Q theta, mạng trả về Q theta của o với các hành động a1 đến a4; tham số theta dùng chung.](img/lec-08/table-vs-dqn.svg)

Hình đặt hai cách lưu cạnh nhau. Bên trái, bảng minh họa có khoảng một phần năm số ô có mẫu, gần với tỉ lệ $20{,}6\%$ của Ví dụ 08.1; ô không có chấm giữ giá trị khởi tạo. Bên phải, một quan sát đi vào mạng và mạng trả về giá trị của mọi hành động; mọi giá trị dùng chung tham số $\theta$.

**Ứng dụng và giới hạn.** Bài giảng gốc (trang 14–15) nêu bốn lợi ích của dạng có tham số: không lưu tường minh mọi cặp, tổng quát hóa giữa các trạng thái tương tự, trích xuất đặc trưng từ đầu vào có cấu trúc như ảnh, và khả vi nên cập nhật được bằng gradient. Cái giá là sai số xấp xỉ và giao thoa: một cập nhật cũng đổi các giá trị đang đúng. Với mạng nhiều tầng, hàm mất mát không lồi theo $\theta$ và các bảo đảm hội tụ dạng bảng không còn áp dụng.

**Kiểm tra nhanh.** Trong Ví dụ 08.1, vì sao $7\,320$ ô trạng thái vẫn giữ giá trị khởi tạo dù các ô bên cạnh đã có mẫu? Với bảng, mỗi ô chỉ đổi khi chính nó được ghé; với một hàm có tham số dùng chung, cập nhật ở ô bên cạnh cũng đổi giá trị ở các ô này.

<!-- note-topic-id: lec-08-topic-16 -->
### Ví dụ: đầu vào bốn khung Atari

Trước khi định nghĩa giao diện của mạng, chúng ta xét một trường hợp cụ thể mà bài giảng gốc (trang 35) dùng: DQN chơi trò chơi Atari, nơi quan sát là ảnh màn hình.

::: example Ví dụ 08.2 (Đầu vào bốn khung Atari)
**Dữ kiện.** Mỗi bước môi trường trả về một khung ảnh màn hình và thay đổi điểm số.

- Quan sát $O_t$: bốn khung gần nhất, mỗi khung đã tiền xử lý thành ảnh $H\times W$, xếp chồng thành mảng $4\times H\times W$. Mnih và cộng sự (2015) chuyển mỗi khung sang ảnh xám và thu về $84\times84$.
- Hành động $A_t\in\mathcal A$: lệnh điều khiển rời rạc; số hành động hợp lệ từ $4$ đến $18$ tùy trò chơi (Mnih và cộng sự, 2015).
- Phần thưởng $R_{t+1}$: thay đổi điểm số tức thời.
- Mạng: các tầng tích chập rồi các tầng kết nối đầy đủ; đầu ra có $\lvert\mathcal A\rvert$ thành phần, mỗi thành phần ứng với một hành động.

**Diễn giải.** Một lần tính xuôi cho giá trị của mọi hành động, nên phép cực đại $\max_aQ_\theta(O_t,a)$ và hành động tham lam được đọc trên một vector. Một khung đơn không cho biết vận tốc hay hướng chuyển động; bốn khung liên tiếp cho thông tin động học ngắn hạn (bài giảng gốc, trang 35).
:::

![Từ trái sang phải: bốn khung ảnh thô gần nhất; bước tiền xử lý; bốn khung đã xử lý xếp chồng thành O t có kích thước 4 nhân H nhân W; mạng tích chập rồi tầng kết nối đầy đủ; đầu ra là Q theta của O t với từng hành động a 1 tới a có chỉ số bằng số hành động.](img/lec-08/atari-pipeline.svg)

Hình đọc từ trái sang phải. Tiền xử lý tác động lên từng khung thô, rồi bốn khung đã xử lý mới được xếp chồng thành $O_t$; mạng nhận $O_t$ và trả về một cột $\lvert\mathcal A\rvert$ giá trị. Bài giảng gốc gọi chồng bốn khung là "đầu vào trạng thái"; ở đây ta gọi là quan sát, vì bốn khung chưa chắc chứa đủ thông tin để thay cho trạng thái Markov, điều được xét ngay sau giao diện của mạng.

Ví dụ 08.2 chỉ cố định giao diện vào và ra của mạng. Tái lập một kết quả Atari đã công bố còn cần số khung lặp lại cho mỗi hành động, cách bắt đầu lượt, kiến trúc cụ thể, siêu tham số và giao thức đánh giá; nguồn không cho các chi tiết này, nên chúng ta không nêu số liệu thành tích.

<!-- note-topic-id: lec-08-topic-02 -->
### Mạng giá trị hành động

Ví dụ 08.1 cho thấy bảng giá trị hành động không có dữ liệu ở phần lớn ô, và Ví dụ 08.2 cho một mạng nhận chồng bốn khung ảnh rồi trả về $\lvert\mathcal A\rvert$ giá trị. Chúng ta cần một định nghĩa dùng được cho mọi tập quan sát và mọi tập hành động hữu hạn, để các mục sau viết mục tiêu, hàm mất mát và chính sách hành vi trên cùng một đối tượng.

Nhắc lại Định nghĩa 07.1: xấp xỉ tuyến tính $\hat q(s,a,w)=x(s,a)^\top w$ dùng vector đặc trưng $x(s,a)\in\mathbb R^d$ chọn trước, không đổi khi học. Mạng giá trị hành động đổi hai chỗ. Thứ nhất, đặc trưng không còn chọn tay: các tầng của mạng biến quan sát thô thành biểu diễn, và các tầng này cũng có tham số được học. Thứ hai, hành động không còn là đối số đầu vào: mạng trả về một giá trị cho mỗi hành động cùng lúc. Tham số $\theta$ đóng vai của $w$.

::: definition Định nghĩa 08.1 (Mạng giá trị hành động)
Cho tập quan sát $\mathcal O$, tập hành động hữu hạn $\mathcal A=\{a_1,\dots,a_{\lvert\mathcal A\rvert}\}$ và số nguyên dương $d$. Mạng giá trị hành động là một ánh xạ $\mathbf q_\theta:\mathcal O\to\mathbb R^{\lvert\mathcal A\rvert}$ phụ thuộc tham số $\theta\in\mathbb R^d$. Giá trị hành động do mạng tính là thành phần của vector đầu ra ứng với hành động đó:

$$
Q_\theta(o,a)=[\mathbf q_\theta(o)]_a,\qquad o\in\mathcal O,\ a\in\mathcal A.
$$

Giá trị lớn nhất và tập hành động tham lam tại $o$ là

$$
\max_{a\in\mathcal A}Q_\theta(o,a),\qquad \mathcal G_\theta(o)=\arg\max_{a\in\mathcal A}Q_\theta(o,a).
$$
:::

Theo định nghĩa, mạng nhận một quan sát và trả về một vector, mỗi hành động ứng với một tọa độ; $Q_\theta(o,a)$ chỉ là phép lấy thành phần. Mục tiêu Q-learning cần $\max_{a'}Q_\theta(O_{t+1},a')$, còn chính sách hành vi $\epsilon_{\mathrm{exp}}$-tham lam cần một hành động trong $\mathcal G_\theta(O_t)$; cả hai đọc trên vector đầu ra sau một lần tính xuôi. Mnih và cộng sự (2015, mục Methods) chọn kiến trúc này vì khi mạng nhận cặp quan sát–hành động làm đầu vào, mỗi hành động cần một lần tính riêng và chi phí tăng tuyến tính theo $\lvert\mathcal A\rvert$. Khi $\mathcal G_\theta(o)$ có nhiều phần tử, ta phá hòa chia đều như với chính sách tham lam của Bài 06.

Giả thiết $\mathcal A$ hữu hạn có vai trò riêng. Bỏ giả thiết này, chẳng hạn khi hành động là một số thực trong một khoảng, vector đầu ra không xác định và $\max_aQ_\theta(o,a)$ trở thành một bài toán tối ưu theo $a$ phải giải ở mỗi bước. Sutton và Barto (2018, §13.7) trình bày cách tham số hóa chính sách cho hành động liên tục; DQN chỉ xét tập hành động hữu hạn.

::: example Ví dụ 08.3 (Đọc vector giá trị hành động)
**Dữ kiện.** $\mathcal A=\{a_1,a_2,a_3,a_4\}$. Tại quan sát $o$, mạng trả về $\mathbf q_\theta(o)=(0{,}8;\ 2{,}5;\ -0{,}3;\ 1{,}9)$ (số minh họa). Chính sách hành vi là $\epsilon_{\mathrm{exp}}$-tham lam với $\epsilon_{\mathrm{exp}}=0{,}1$.

**Tính.** $Q_\theta(o,a_3)=[\mathbf q_\theta(o)]_{a_3}=-0{,}3$. Giá trị lớn nhất là $\max_aQ_\theta(o,a)=2{,}5$, đạt duy nhất tại $a_2$, nên $\mathcal G_\theta(o)=\{a_2\}$. Chính sách $\epsilon_{\mathrm{exp}}$-tham lam chọn $a_2$ với xác suất $1-0{,}1+0{,}1/4=0{,}925$ và mỗi hành động còn lại với xác suất $0{,}1/4=0{,}025$; kiểm tra: $0{,}925+3\cdot0{,}025=1$.

**Diễn giải.** Ba đại lượng mà các mục sau dùng, gồm giá trị của hành động đã thực hiện, giá trị lớn nhất trong mục tiêu và hành động tham lam của chính sách hành vi, đều lấy từ cùng một vector sau một lần tính.
:::

![Quan sát o đi vào mạng có tham số theta; một lần tính trả về vector q theta của o gồm bốn ô ứng với a1 đến a4, giá trị minh họa 0,8; 2,5; âm 0,3; 1,9. Ô a2 có viền kép và dấu tam giác bên dưới: giá trị lớn nhất 2,5, arg max bằng a2.](img/lec-08/q-vector.svg)

Hình vẽ dữ kiện của Ví dụ 08.3. Quan sát $o$ đi qua mạng có tham số $\theta$, và một lần tính cho cả bốn ô của $\mathbf q_\theta(o)$. Ô $a_2$ có viền kép và một dấu tam giác bên dưới, đánh dấu giá trị lớn nhất $2{,}5$ và $\arg\max$ bằng $a_2$.

::: remark Nhận xét 08.2 (Giả thiết Markov khi viết mục tiêu theo quan sát)
Phương trình Bellman tối ưu của Bài 06 viết trên trạng thái của một MDP. Khi viết mục tiêu $R_{t+1}+\gamma\max_{a'}Q_\theta(O_{t+1},a')$ theo quan sát, ta giả thiết $O_t$ đủ Markov: phân phối của $(R_{t+1},O_{t+1})$ khi biết $O_t$ và $A_t$ không phụ thuộc các quan sát và hành động trước đó. Khi đó $O_t$ thay được $S_t$, và $q_*(o,a)$ là nghiệm của phương trình Bellman tối ưu theo quan sát. Bỏ giả thiết này: một khung ảnh Atari cho vị trí của vật thể nhưng không cho hướng chuyển động (bài giảng gốc, trang 35), nên hai tình huống có cùng quan sát $o$ có thể cần hai giá trị khác nhau. Mục tiêu vẫn tính được, nhưng $q_*(o,a)$ không còn được xác định bởi một phương trình Bellman theo quan sát, và mục tiêu chỉ là xấp xỉ.
:::

**Trong thực hành.** $\mathbf q_\theta(o)$ là tensor đầu ra của mạng, kích thước $[\lvert\mathcal A\rvert]$ cho một quan sát và $[b,\lvert\mathcal A\rvert]$ cho $b$ quan sát của một mini-batch; giá trị $Q_\theta(O_i,A_i)$ của hành động đã lưu được lấy ra bằng phép chọn theo hành động (gather) ở phần 4. Bài giảng gốc (trang 17) nêu các lựa chọn kiến trúc điển hình: mạng nhiều tầng cho quan sát là vector số chiều thấp như CartPole hay Lunar Lander, mạng tích chập cho ảnh, hàm kích hoạt ReLU, tanh hoặc sigmoid; số tầng, độ rộng và cách biểu diễn đầu vào ảnh hưởng tới năng lực xấp xỉ và độ ổn định khi huấn luyện. Giả thiết Markov là giả thiết về quan sát, nên đổi kiến trúc không làm nó đúng; với ảnh, nó phụ thuộc số khung được xếp chồng. Mạng giá trị hành động cũng không đi kèm bảo đảm hội tụ nào: thay hàm tuyến tính bằng mạng vẫn giữ yếu tố xấp xỉ hàm của bộ ba bất ổn.

**Kiểm tra nhanh.** Với $\mathbf q_\theta(o)=(1;\ 4;\ 4;\ 0)$ và $\epsilon_{\mathrm{exp}}=0{,}2$, tập hành động tham lam là $\mathcal G_\theta(o)=\{a_2,a_3\}$; phá hòa chia đều cho $a_2$ xác suất $0{,}2/4+0{,}8/2=0{,}45$, và $a_1$, $a_4$ mỗi hành động $0{,}05$.

Mạng giá trị hành động cho mọi giá trị cần dùng từ một lần tính. Chúng ta còn hai việc. Thứ nhất, kiểm tra chồng bốn khung của Ví dụ 08.2 có đủ Markov để Nhận xét 08.2 áp dụng hay không. Thứ hai, mục tiêu $R_{t+1}+\gamma\max_{a'}Q_\theta(O_{t+1},a')$ được tính bằng chính $\theta$ đang học, nên một bước cập nhật có thể đổi cả dự đoán lẫn mục tiêu; chúng ta xử lý điểm này ở hai mục "Một tham số tạo cả dự đoán lẫn đích" và "Mạng mục tiêu".

### Bốn khung và tính Markov

Nhận xét 08.2 cần $O_t$ đủ Markov: phân phối của $(R_{t+1},O_{t+1})$ khi biết toàn bộ lịch sử quan sát và hành động chỉ phụ thuộc $O_t$ và $A_t$. Ví dụ 08.2 lấy $O_t$ là chồng bốn khung gần nhất. Chúng ta kiểm tra xem lựa chọn này cho được gì và còn thiếu gì, trên một vật thể đơn giản nhất của trò chơi Atari: một quả bóng chuyển động thẳng đều.

::: example Ví dụ 08.4 (Quả bóng trên một khung và trên bốn khung)
**Dữ kiện.** Tọa độ điểm ảnh của tâm quả bóng (cột, hàng; hàng tăng khi đi xuống) trong bốn khung $t-3$, $t-2$, $t-1$, $t$ là $(10,40)$, $(14,37)$, $(18,34)$, $(22,31)$ (số minh họa). Quả bóng không chạm biên trong khoảng này.

**Tính.** Một khung $t$ chỉ cho vị trí $(22,31)$; mọi vận tốc đều khớp với khung này. Hiệu hai khung liên tiếp là $(14,37)-(10,40)=(4,-3)$, $(18,34)-(14,37)=(4,-3)$, $(22,31)-(18,34)=(4,-3)$: vận tốc $(4,-3)$ điểm ảnh mỗi khung, không đổi, nên gia tốc ước lượng từ ba khung cuối bằng $(0,0)$. Vị trí dự đoán ở khung $t+1$ là $(22,31)+(4,-3)=(26,28)$.

**Diễn giải.** Một khung xác định vị trí nhưng không xác định hướng và tốc độ; hai khung cho vận tốc, ba khung cho gia tốc. Với vật chuyển động như vậy, chồng bốn khung chứa đủ thông tin để dự đoán vị trí kế tiếp.
:::

![Bên trái, một khung: một quả bóng tại vị trí hiện tại, hai mũi tên nét đứt ngược hướng kèm dấu hỏi, vì một khung không cho biết hướng và tốc độ. Bên phải, bốn khung xếp chồng: bốn vị trí của quả bóng tại t trừ 3 đến t, cách đều nhau trên một đường đi lên sang phải; ba vị trí cũ là vòng tròn rỗng nét đứt, vị trí hiện tại tô đặc; mũi tên liền chỉ hướng chuyển động tiếp theo.](img/lec-08/frame-stack-markov.svg)

Hình đặt hai trường hợp cạnh nhau. Bên trái, quả bóng trong một khung có thể đang đi theo hai hướng ngược nhau, nên hai mũi tên nét đứt mang dấu hỏi. Bên phải, ba vị trí cũ (vòng tròn rỗng nét đứt) và vị trí hiện tại (tô đặc) cách đều nhau trên một đường thẳng, như dữ kiện của Ví dụ 08.4; mũi tên liền chỉ hướng chuyển động kế tiếp. Bài giảng gốc (trang 35) nêu đúng lý do này: một ảnh đơn lẻ có thể không cho biết vận tốc hay hướng chuyển động, nhiều khung cho động học ngắn hạn.

Ví dụ 08.4 chỉ xét một vật chuyển động thẳng đều và luôn hiển thị. Chồng bốn khung không làm $O_t$ đủ Markov trong mọi trò chơi, vì ba loại thông tin vẫn có thể nằm ngoài nó: một vật bị vật khác che khuất trong cả bốn khung; một biến của trò chơi không hiển thị trên màn hình, chẳng hạn một bộ đếm thời gian ẩn; và một sự kiện xảy ra trước cửa sổ bốn khung nhưng còn ảnh hưởng tới phần thưởng về sau. Khi đó hai tình huống có cùng $O_t$ có thể có tương lai khác nhau, và theo Nhận xét 08.2, mục tiêu Q-learning tính theo $O_t$ chỉ là xấp xỉ. Số bốn là một lựa chọn thiết kế của Mnih và cộng sự (2015); không có định lý nào bảo đảm số khung đó là đủ.

**Trong thực hành.** Chồng khung thường được cài như một lớp bọc môi trường giữ hàng đợi các khung gần nhất. Khi một lượt mới bắt đầu, hàng đợi chưa đủ bốn khung, nên cài đặt cần một quy ước cho đầu lượt, chẳng hạn lặp lại khung đầu; quy ước này phải giống nhau khi huấn luyện và khi đánh giá. Khi bốn khung không đủ, một hướng xử lý là thay một tầng kết nối đầy đủ bằng một tầng hồi quy để mạng tự tích lũy lịch sử dài hơn (Hausknecht và Stone, 2015, "Deep Recurrent Q-Learning for Partially Observable MDPs", AAAI Fall Symposium); hướng này nằm ngoài phạm vi chương.

**Kiểm tra nhanh.** Chồng bốn khung có làm $O_t$ đủ Markov trong mọi trò chơi Atari không? Không; thông tin không hiển thị trên màn hình hoặc có trước bốn khung vẫn có thể thiếu, và khi đó cùng một $O_t$ ứng với nhiều tình huống có tương lai khác nhau.

Đến đây quan sát và giao diện của mạng đã cố định. Mục tiêu $R_{t+1}+\gamma\max_{a'}Q_\theta(O_{t+1},a')$ vẫn được tính bằng chính $\theta$ đang học; chúng ta xét hệ quả của điều này ở mục kế tiếp.

### Một tham số tạo cả dự đoán lẫn đích

Trong Q-learning dạng bảng, cập nhật ô $(S_t,A_t)$ không đổi ô ở $S_{t+1}$ khi $S_{t+1}\ne S_t$, nên mục tiêu của mẫu chuyển giữ nguyên sau bước cập nhật. Với mạng giá trị hành động, dự đoán $Q_\theta(O_t,A_t)$ và phần bootstrap $\max_{a'}Q_\theta(O_{t+1},a')$ dùng chung $\theta$, nên một bước theo $\theta$ đổi cả hai. Ví dụ sau đo sự thay đổi này trong trường hợp nhỏ nhất: một tham số duy nhất.

::: example Ví dụ 08.5 (Một tham số tạo cả dự đoán lẫn đích)
**Dữ kiện.** Mạng có một tham số và cho cùng một giá trị ở mọi cặp: $Q_\theta(o,a)=\theta$ với mọi $o\in\mathcal O$, $a\in\mathcal A$. Một mẫu chuyển có $R_{t+1}=1$, $O_{t+1}$ chưa kết thúc; $\gamma=0{,}9$, $\theta_0=0$, bước học $\alpha=0{,}5$. Cập nhật bán gradient (Định nghĩa 07.21) với $q=Q_\theta(O_t,A_t)$ và $y=R_{t+1}+\gamma\max_{a'}Q_\theta(O_{t+1},a')$ là $\theta\leftarrow\theta+\alpha(y-q)\nabla_\theta Q_\theta(O_t,A_t)$, ở đây $\nabla_\theta Q_\theta(O_t,A_t)=1$.

**Tính.** Tại $\theta_0=0$: $q=0$ và $y=1+0{,}9\cdot0=1$. Bước cập nhật cho $\theta_1=0+0{,}5\,(1-0)=0{,}5$. Tính lại trên cùng mẫu chuyển: $q=0{,}5$ và $y=1+0{,}9\cdot0{,}5=1{,}45$.

**Diễn giải.** Sai số $y-q$ giảm từ $1$ xuống $1{,}45-0{,}5=0{,}95$. Nếu đích giữ nguyên ở $1$, sai số sau bước là $1-0{,}5=0{,}5$. Dự đoán tăng $0{,}5$, nhưng đích cũng tăng $0{,}9\cdot0{,}5=0{,}45$, vì cả hai cùng chứa $\theta$.
:::

![Trục giá trị thẳng đứng từ 0 đến 1,5. Trước bước cập nhật: dự đoán q bằng 0 (hình tròn), đích y bằng 1 (hình vuông). Sau một bước: q bằng 0,5, y bằng 1,45. Hai mũi tên nét đứt cho thấy cả dự đoán lẫn đích cùng tăng.](img/lec-08/moving-target-step.svg)

Hình vẽ hai giá trị của Ví dụ 08.5 trên một trục. Hình tròn là dự đoán $q$, hình vuông là đích $y$; cột trái trước bước cập nhật, cột phải sau bước. Hai mũi tên nét đứt cùng hướng lên: bước cập nhật kéo $q$ về phía $y$, đồng thời đẩy $y$ đi xa thêm.

Lặp lại cập nhật trên cùng mẫu chuyển cho $\theta_{n+1}=\theta_n+0{,}5\,(1+0{,}9\,\theta_n-\theta_n)=0{,}95\,\theta_n+0{,}5$. Dãy này hội tụ về nghiệm của $\theta=1+0{,}9\,\theta$, tức $\theta=10$, vì $\theta_{n+1}-10=0{,}95\,(\theta_n-10)$; mỗi bước chỉ rút khoảng cách tới $10$ đi $5\%$. Với đích giữ cố định ở một giá trị $c$, cùng bước học cho $\theta_{n+1}-c=0{,}5\,(\theta_n-c)$: $\theta$ tiến về $c$, chưa phải về $10$. Trong ví dụ một tham số, đích di động không gây phân kỳ: dãy vẫn hội tụ về $10$. Khi nhiều trạng thái dùng chung tham số, hệ số tương ứng có thể lớn hơn $1$: Mệnh đề 07.37 cho một ví dụ tuyến tính hai trạng thái mà tham số tăng không chặn. Bài giảng gốc (trang 31) tóm tắt hiện tượng: khi mạng thay đổi, mục tiêu cũng thay đổi, và điều này có thể dẫn tới dao động hoặc phân kỳ. Muốn mỗi bước là hồi quy về một nhãn đứng yên, như học có giám sát, chúng ta cần tách tham số tạo đích khỏi tham số được cập nhật.

### Mạng mục tiêu

Trong Ví dụ 08.5, đích tính bằng chính $\theta$ đổi từ $1$ thành $1{,}45$ sau một bước, dù mẫu chuyển không đổi. Muốn mỗi bước cập nhật là một bước hồi quy về một nhãn đứng yên, chúng ta tách tham số tạo đích khỏi tham số được cập nhật: giữ một bản sao của mạng, tính đích bằng bản sao đó, và chỉ thỉnh thoảng làm mới bản sao.

::: definition Định nghĩa 08.3 (Mạng mục tiêu và đồng bộ)
Cho mạng giá trị hành động $\mathbf q_\theta$ (Định nghĩa 08.1), bộ đếm bước tối ưu $k_{\mathrm{opt}}\in\mathbb N_0$ và số nguyên dương $C$. Mạng mục tiêu (target network) là mạng $Q_{\theta^-}$ có cùng kiến trúc với $Q_\theta$ và vector tham số riêng $\theta^-\in\mathbb R^d$; mạng $Q_\theta$, được cập nhật bằng gradient, gọi là mạng trực tuyến (online network). Tham số $\theta^-$

1. được khởi tạo bằng $\theta^-\leftarrow\theta$;
2. không đổi khi $\theta$ được cập nhật bằng gradient;
3. sau mỗi bước tối ưu, khi $k_{\mathrm{opt}}$ vừa tăng thỏa $k_{\mathrm{opt}}\bmod C=0$, được gán $\theta^-\leftarrow\theta$.

Phép gán ở mục 3 gọi là đồng bộ (sao chép cứng); $C$ là số bước tối ưu giữa hai lần đồng bộ. Phần bootstrap của đích được tính bằng $Q_{\theta^-}$ thay cho $Q_\theta$.
:::

Theo định nghĩa, giữa hai lần đồng bộ $\theta^-$ là một hằng số, nên đích của mỗi mẫu chuyển là một số cố định và mỗi bước cập nhật $\theta$ là một bước hồi quy về nhãn đó; chỉ $Q_\theta$ nhận gradient. Tại mỗi mốc đồng bộ, đích của mọi mẫu chuyển đổi cùng lúc, vì $\theta^-$ nhận giá trị mới. Mạng mục tiêu vì vậy làm đích đổi theo từng đợt thay vì sau mỗi bước, nhưng không giữ đích cố định mãi.

Mỗi điều kiện có vai trò riêng. "Cùng kiến trúc" làm phép gán $\theta^-\leftarrow\theta$ có nghĩa: hai vector tham số có cùng số chiều và cùng cách đọc. Khởi tạo $\theta^-\leftarrow\theta$ làm các đích đầu tiên đến từ chính mạng đang học; bỏ điều kiện này, $C$ bước tối ưu đầu tiên hồi quy về các giá trị của một mạng khởi tạo khác, không liên quan tới $Q_\theta$. Chu kỳ $C$ quyết định nhịp thay đổi của đích. Với $C=1$, $\theta^-$ bằng $\theta$ ngay trước mỗi bước, và cập nhật trùng với cập nhật bán gradient của Ví dụ 08.5. Khi $C$ rất lớn, đích gần như không bao giờ được làm mới, nên $Q_\theta$ chỉ học được giá trị một bước tính từ mạng ban đầu.

![Trục ngang là bộ đếm bước tối ưu k opt với các mốc 0, C, 2C, 3C. Đường gấp khúc có chấm nhỏ là tham số theta của mạng trực tuyến, đổi sau mỗi bước tối ưu. Đường bậc thang đậm là theta trừ của mạng mục tiêu: tại các mốc 0, C và 2C, đánh dấu bằng vòng tròn rỗng, nó nhận đúng giá trị của theta tại mốc đó rồi giữ nằm ngang trong C bước; chú giải ghi mốc đồng bộ, theta trừ gán bằng theta.](img/lec-08/target-network-timeline.svg)

Hình vẽ hai tham số trên cùng một trục giá trị, theo bộ đếm bước tối ưu $k_{\mathrm{opt}}$. Đường gấp khúc có chấm nhỏ là $\theta$, đổi sau mỗi bước tối ưu. Đường bậc thang đậm là $\theta^-$: tại các mốc $0$, $C$, $2C$ (vòng tròn rỗng), $\theta^-$ nhận đúng giá trị của $\theta$ tại mốc đó, rồi nằm ngang trong $C$ bước tiếp theo, trong khi $\theta$ tiếp tục đổi. Các giá trị trong hình chỉ minh họa hình dạng, không đến từ một lần chạy.

::: example Ví dụ 08.6 (Một tham số với mạng mục tiêu, $C=3$)
**Dữ kiện.** Như Ví dụ 08.5: $Q_\theta(o,a)=\theta$, một mẫu chuyển có $R_{t+1}=1$, $O_{t+1}$ chưa kết thúc, $\gamma=0{,}9$, $\alpha=0{,}5$, $\theta_0=0$. Đích tính bằng mạng mục tiêu: $y=1+0{,}9\,\theta^-$; khởi tạo $\theta^-=\theta_0=0$; $C=3$.

**Tính.** Với $\theta^-=0$, đích $y=1$ trong ba bước: $\theta_1=0+0{,}5\,(1-0)=0{,}5$, $\theta_2=0{,}5+0{,}5\,(1-0{,}5)=0{,}75$, $\theta_3=0{,}75+0{,}5\,(1-0{,}75)=0{,}875$. Sau bước thứ ba, $k_{\mathrm{opt}}=3$ là bội của $C$, nên $\theta^-\leftarrow0{,}875$ và đích mới là $1+0{,}9\cdot0{,}875=1{,}7875$.

**Diễn giải.** Trong ba bước, đích đứng yên và sai số $y-\theta_k$ giảm một nửa mỗi bước: $1$, $0{,}5$, $0{,}25$, $0{,}125$. Đích chỉ đổi tại mốc đồng bộ, một lần, từ $1$ lên $1{,}7875$.
:::

Trong ví dụ một tham số, mạng mục tiêu không đưa $\theta$ tới $10$ nhanh hơn. Gọi $r=0{,}5^C$. Một chu kỳ $C$ bước đưa $\theta^-$ thành $(1+0{,}9\,\theta^-)(1-r)+\theta^-r$, nên $\theta^-_{\text{mới}}-10=(0{,}9+0{,}1\,r)\,(\theta^--10)$. Với $C=3$, khoảng cách tới $10$ nhân với $0{,}9125$ sau mỗi ba bước, trong khi không có mạng mục tiêu, ba bước nhân khoảng cách với $0{,}95^3\approx0{,}857$. Giữa hai lần đồng bộ, mỗi bước là hồi quy về nhãn cố định, nên vòng phản hồi giữa dự đoán và đích chỉ khép lại tại các mốc đồng bộ; đó là tác dụng của mạng mục tiêu; lợi ích ổn định với mạng lớn là kết quả thực nghiệm. Ở phần 6, chúng ta xét một ví dụ hai trạng thái dùng chung tham số, trong đó mạng mục tiêu làm chậm nhưng không ngăn được phân kỳ. Bài giảng gốc (trang 33) nêu mạng mục tiêu như cách làm mục tiêu thay đổi chậm hơn để quá trình tối ưu ổn định hơn; đó là tác dụng thực nghiệm, không phải bảo đảm hội tụ.

**Trong thực hành.** Hai mạng là hai bản của cùng một lớp mạng; đồng bộ là sao chép toàn bộ tham số của mạng trực tuyến sang mạng mục tiêu, và mạng mục tiêu chỉ chạy lan truyền xuôi, không tính gradient. Bộ nhớ tham số vì vậy gấp đôi. Mnih và cộng sự (2015, Extended Data Table 1) dùng $C=10\,000$ lần cập nhật. Một số thuật toán dùng cập nhật mềm $\theta^-\leftarrow\tau\theta+(1-\tau)\theta^-$ với $\tau$ nhỏ sau mỗi bước, chẳng hạn $\tau=0{,}001$ trong DDPG (Lillicrap và cộng sự, 2016, "Continuous control with deep reinforcement learning", ICLR); chúng ta chỉ dùng sao chép cứng như DQN gốc. Điều kiện đồng bộ đếm bước tối ưu $k_{\mathrm{opt}}$, không đếm bước môi trường $t$; ở phần 4, hai bộ đếm này được ghép vào thuật toán.

**Kiểm tra nhanh.** Với $C=1$, cập nhật dùng mạng mục tiêu trùng với cập nhật nào? Vì $\theta^-$ được gán bằng $\theta$ sau mỗi bước, trước bước kế tiếp hai tham số bằng nhau, nên cập nhật trùng với cập nhật bán gradient dùng chính $\theta$ trong đích, như Ví dụ 08.5.

Đến đây chúng ta đã có mạng giá trị hành động và một bản sao giữ cố định để tính đích. Việc còn lại của phần này là viết đích thành nhãn hồi quy cho một mẫu chuyển, kể cả khi mẫu chuyển kết thúc lượt hoặc bị cắt ngắn.

<!-- note-topic-id: lec-08-topic-03 -->
### Đích hồi quy

Mạng mục tiêu cho một bộ tham số $\theta^-$ đứng yên giữa hai lần đồng bộ. Chúng ta dùng nó để viết mục tiêu Q-learning cho một mẫu chuyển. Q-learning dạng bảng dùng quy ước $Q(s,\cdot)=0$ tại trạng thái kết thúc. Mạng không có ô riêng cho trạng thái kết thúc: đầu ra của nó tại quan sát cuối lượt là một vector bất kỳ do tham số quyết định. Vì vậy mẫu chuyển phải mang theo một cờ cho biết bước này có kết thúc MDP hay không.

::: definition Định nghĩa 08.4 (Cờ kết thúc, đích hồi quy và sai số TD)
Xét mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1})$ với $O_t,O_{t+1}\in\mathcal O$, $A_t\in\mathcal A$, $R_{t+1}\in\mathbb R$ và cờ kết thúc $Z_{t+1}\in\{0,1\}$; $Z_{t+1}=1$ khi và chỉ khi MDP đang mô hình hóa kết thúc tại bước $t+1$. Cho mạng trực tuyến $Q_\theta$, mạng mục tiêu $Q_{\theta^-}$ (Định nghĩa 08.3) và $\gamma\in[0,1)$. Đích hồi quy (còn gọi là mục tiêu cập nhật) của mẫu chuyển là

$$
y_t=R_{t+1}+\gamma\,(1-Z_{t+1})\max_{a'\in\mathcal A}Q_{\theta^-}(O_{t+1},a').
$$

Dự đoán của mạng trực tuyến là $q_t=Q_\theta(O_t,A_t)$, và sai số sai phân thời gian (sai số TD) là $\delta_t=y_t-q_t$.
:::

Đích gồm hai phần. $R_{t+1}$ là phần thưởng đã quan sát; $\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$ là ước lượng của phần lợi tức còn lại, đọc trên vector $\mathbf q_{\theta^-}(O_{t+1})$ sau một lần tính của mạng mục tiêu. Mặt nạ $(1-Z_{t+1})$ bằng $0$ khi lượt kết thúc, nên khi đó $y_t=R_{t+1}$; đây đúng là quy ước $Q(s,\cdot)=0$ của dạng bảng, viết cho một hàm không có ô riêng cho trạng thái kết thúc. $q_t$ phụ thuộc $\theta$, còn $y_t$ chỉ phụ thuộc dữ liệu và $\theta^-$. Với $\theta^-$ cố định, $y_t$ là một số cố định gắn với mẫu chuyển, và $\delta_t>0$ nghĩa là dự đoán cần tăng.

Các điều kiện trong định nghĩa có vai trò riêng. $Z_{t+1}$ chỉ ghi kết thúc của chính MDP; việc dừng thu thập vì một giới hạn bên ngoài được ghi bằng một cờ khác, xét ở cuối phần này. Bỏ mặt nạ, đích tại bước cuối lượt cộng thêm $\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$, một giá trị không ứng với phần thưởng nào; sai lệch này được tính bằng số ở mục kế tiếp. Điều kiện $\gamma<1$ cùng phần thưởng bị chặn giữ $q_*$ hữu hạn khi lượt không kết thúc. Dùng $Q_{\theta^-}$ thay cho $Q_\theta$ là điều làm $y_t$ đứng yên giữa hai lần đồng bộ (Định nghĩa 08.3). Cuối cùng, đích chỉ có nghĩa là mục tiêu Bellman khi $O_{t+1}$ đủ Markov (Nhận xét 08.2).

Đích hồi quy nối DQN với hồi quy có giám sát. Với $\theta^-$ cố định và một tập mẫu chuyển $\{(O_i,A_i,R_i,O'_i,Z_i)\}_{i=1}^b$, bài toán cực tiểu $\tfrac12\sum_i\bigl(y_i-Q_\theta(O_i,A_i)\bigr)^2$ theo $\theta$ là hồi quy bình phương tối thiểu với đầu vào $(O_i,A_i)$ và nhãn $y_i$. Bài toán này khác hồi quy có giám sát ở ba điểm: nhãn là ước lượng tạo từ một bản sao của chính mô hình, không phải giá trị đo được; nhãn đổi tại mỗi mốc đồng bộ; và dữ liệu do chính sách hành vi sinh ra, nên phân phối của nó đổi theo $\theta$. Với Q-learning dạng bảng và $C=1$, $\tfrac12(y_t-Q(S_t,A_t))^2$, khi coi $y_t$ là hằng, có đạo hàm theo ô $Q(S_t,A_t)$ bằng $-\delta_t$, nên quy tắc $Q\leftarrow Q+\alpha\delta_t$ là một bước hạ gradient trên chính ô đó.

::: remark Nhận xét 08.5 (Hàm hồi quy tốt nhất cho đích cố định)
Giả sử $O_t$ đủ Markov, $\theta^-$ cố định, các cặp $(O_t,A_t)$ được lấy theo một phân phối cố định và $\mathbb E[y_t^2]<\infty$. Trong mọi hàm $f$ của $(o,a)$, hàm làm nhỏ nhất kỳ vọng $\mathbb E\bigl[(y_t-f(O_t,A_t))^2\bigr]$ là kỳ vọng có điều kiện
$$
\begin{aligned}
f^\star(o,a)&=\mathbb E\bigl[y_t\mid O_t=o,A_t=a\bigr]\\
&=\mathbb E\Bigl[R_{t+1}+\gamma(1-Z_{t+1})\max_{a'}Q_{\theta^-}(O_{t+1},a')\Bigm| O_t=o,A_t=a\Bigr],
\end{aligned}
$$
tức $(\mathcal TQ_{\theta^-})(o,a)$ với $\mathcal T$ là toán tử Bellman tối ưu viết theo quan sát; đẳng thức đúng hầu chắc chắn theo phân phối của $(O_t,A_t)$. Một lượt hồi quy giữa hai lần đồng bộ vì vậy xấp xỉ một bước lặp giá trị $Q_{\theta^-}\mapsto\mathcal T Q_{\theta^-}$, trong giới hạn của lớp hàm và của số bước tối ưu. Nhận xét không nói gì về hội tụ của chuỗi các bước như vậy: mỗi bước có sai số xấp xỉ và sai số tối ưu, và phân phối dữ liệu đổi theo $\theta$.
:::

**Trong thực hành.** Đích được tính cho cả mini-batch bằng một lần tính xuôi của mạng mục tiêu trên các quan sát kế tiếp, cho mảng kích thước $[b,\lvert\mathcal A\rvert]$, rồi lấy cực đại theo chiều hành động để được một giá trị cho mỗi mẫu. Cờ $Z_i$ được lưu cùng mẫu chuyển và đổi sang kiểu số khi tính $1-Z_i$. Đích không được truyền gradient về $\theta$; ở phần 4, điều này được viết thành phép dừng gradient trong hàm mất mát.

Chúng ta đã có nhãn cho mỗi mẫu chuyển. Ở mục kế tiếp, chúng ta tính đích trên một mẫu chuyển kết thúc, có và không có mặt nạ $(1-Z)$.

<!-- note-topic-id: lec-08-topic-04 -->
### Ví dụ: đích tại mẫu chuyển kết thúc

Mặt nạ $(1-Z_{t+1})$ trong Định nghĩa 08.4 chỉ tác động khi lượt kết thúc. Ví dụ sau đo tác động đó trên một mẫu chuyển có giá trị lớn ở quan sát cuối lượt. Cùng số liệu này là mẫu thứ hai của mini-batch hai mẫu chuyển dùng lại ở phần 4, khi chỉ số thời gian $t$ được thay bằng chỉ số mẫu $i$.

::: example Ví dụ 08.7 (Đích tại mẫu chuyển kết thúc)
**Dữ kiện.** $\gamma=0{,}9$. Một mẫu chuyển kết thúc lượt có

| $R_{t+1}$ | $Z_{t+1}$ | $\max_{a'}Q_{\theta^-}(O_{t+1},a')$ | $q_t$ |
|---|---|---|---|
| $-2$ | $1$ | $100$ | $-1{,}5$ |

Giá trị $100$ là đầu ra của mạng mục tiêu tại quan sát cuối lượt (số minh họa).

**Tính.** Với mặt nạ, $y_t=-2+0{,}9\cdot(1-1)\cdot100=-2$ và $\delta_t=y_t-q_t=-2-(-1{,}5)=-0{,}5.$

Nếu cài đặt bỏ mặt nạ, tức coi $Z_{t+1}=0$, thì $y_t=-2+0{,}9\cdot100=88$ và $\delta_t=88-(-1{,}5)=89{,}5$.

**Diễn giải.** Với mặt nạ, đích bằng đúng phần thưởng cuối cùng, và $\delta_t<0$ kéo dự đoán $-1{,}5$ xuống về $-2$. Bỏ mặt nạ, đích lệch $90$ đơn vị và $\delta_t$ đổi dấu, nên dự đoán bị kéo lên về $88$.
:::

Sau bước kết thúc không còn phần thưởng nào, nên giá trị đúng của phần lợi tức còn lại là $0$. Dạng bảng ghi điều này bằng quy ước $Q(s,\cdot)=0$ tại trạng thái kết thúc. Mạng không có ô riêng như vậy: $\max_{a'}Q_{\theta^-}(O_{t+1},a')$ tại quan sát cuối lượt là một số do tham số quyết định, có thể lớn tùy ý, và nó không ứng với phần thưởng nào. Mặt nạ $(1-Z_{t+1})$ thay cho quy ước của dạng bảng.

Lỗi bỏ mặt nạ không dừng ở một mẫu chuyển. Mẫu chuyển trước đó trong lượt có đích chứa $\max_{a'}Q_{\theta^-}$ tại $O_t$, tức chứa chính dự đoán vừa bị kéo lên; qua các lần đồng bộ, giá trị tùy ý ở cuối lượt lan ngược về các mẫu chuyển trước. Một lỗi cùng loại là lấy mặt nạ từ một cờ gộp cả kết thúc lẫn dừng vì giới hạn bên ngoài; hai trường hợp được tách ở mục cuối của phần này.

**Trong thực hành.** Cờ $Z_{t+1}$ phải được lưu cùng mẫu chuyển ngay khi thu thập, vì sau khi lượt kết thúc, môi trường thường được đặt lại và quan sát kế tiếp thuộc lượt mới. Một cách kiểm tra cài đặt là tính đích của một mẫu kết thúc bằng tay như Ví dụ 08.7 và so với giá trị chương trình trả về.

<!-- note-topic-id: lec-08-topic-05 -->
### Kết thúc và cắt ngắn

Khi thu thập dữ liệu, một lượt có thể dừng vì hai lý do khác nhau. MDP có thể đi tới trạng thái kết thúc, như tàu đổ bộ chạm đất hoặc rơi. Người thu thập cũng có thể dừng lượt vì một giới hạn đặt bên ngoài MDP, thường là số bước tối đa của một lượt. Hai lý do này cần hai cách xử lý khác nhau trong đích, nên mẫu chuyển ghi chúng bằng hai cờ.

::: definition Định nghĩa 08.6 (Cờ cắt ngắn và mẫu chuyển sáu thành phần)
Với mẫu chuyển của Định nghĩa 08.4, cờ cắt ngắn $U_{t+1}\in\{0,1\}$ bằng $1$ khi và chỉ khi việc thu thập dừng sau bước $t+1$ vì một giới hạn không thuộc động lực của MDP. Mẫu chuyển được lưu dưới dạng bộ sáu
$$
(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1}).
$$
Đích hồi quy chỉ dùng mặt nạ $(1-Z_{t+1})$ như trong Định nghĩa 08.4; môi trường được đặt lại để bắt đầu lượt mới khi $Z_{t+1}\lor U_{t+1}=1$.
:::

Hai cờ có hai vai. $Z_{t+1}$ quyết định đích: sau bước kết thúc không còn phần thưởng nào, nên phần bootstrap bằng $0$. $Z_{t+1}\lor U_{t+1}$ quyết định việc đặt lại môi trường. Khi $U_{t+1}=1$ và $Z_{t+1}=0$, tác tử dừng vì giới hạn bước, nhưng nếu đi tiếp từ $O_{t+1}$ thì vẫn nhận thêm phần thưởng; giá trị của phần còn lại khác $0$ và được ước lượng bằng $\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$. Đây là cách xử lý cắt ngắn của Q-learning bán gradient trong Bài 07: tại bước cắt ngắn, mục tiêu vẫn chứa phép cực đại.

![Quan sát O t, qua hành động A t và phần thưởng R t+1, tới quan sát O t+1. Nhánh trên, khung viền liền: Z t+1 bằng 1, MDP kết thúc, đích y t bằng R t+1. Nhánh dưới, khung viền nét đứt: U t+1 bằng 1 và Z t+1 bằng 0, hết giới hạn bước, đích y t bằng R t+1 cộng gamma nhân max của Q theta trừ tại O t+1.](img/lec-08/termination-truncation.svg)

Hình vẽ một mẫu chuyển từ $O_t$ tới $O_{t+1}$ và hai cách lượt có thể dừng tại $O_{t+1}$. Nhánh trên (khung viền liền) là kết thúc của MDP, với đích $y_t=R_{t+1}$. Nhánh dưới (khung viền nét đứt) là cắt ngắn khi MDP chưa kết thúc, với đích vẫn chứa phần bootstrap. Trong cả hai nhánh, môi trường được đặt lại.

::: example Ví dụ 08.8 (Đích tại mẫu chuyển bị cắt ngắn)
**Dữ kiện.** $\gamma=0{,}9$. Một mẫu chuyển chạm giới hạn số bước của lượt khi MDP chưa kết thúc:

| $R_{t+1}$ | $Z_{t+1}$ | $U_{t+1}$ | $\max_{a'}Q_{\theta^-}(O_{t+1},a')$ |
|---|---|---|---|
| $1$ | $0$ | $1$ | $4$ |

**Tính.** Mặt nạ đúng là $1-Z_{t+1}=1$, nên $y_t=1+0{,}9\cdot4=4{,}6$. Nếu cài đặt dùng mặt nạ $1-(Z_{t+1}\lor U_{t+1})=0$, đích thành $y_t=1$.

**Diễn giải.** Gộp hai cờ hạ đích của mẫu chuyển này đi $3{,}6$, như thể lượt kết thúc thật ở bước giới hạn. Mọi mẫu chuyển chạm giới hạn bước đều bị hạ theo cách đó, nên mạng học rằng các quan sát gần cuối lượt có giá trị thấp, dù MDP không có lý do nào cho điều này.
:::

Cùng số liệu (trừ hai cờ) là mẫu thứ nhất của mini-batch hai mẫu chuyển dùng lại ở phần 4.

Cách xử lý trên dựa trên một giả thiết: giới hạn số bước không thuộc nhiệm vụ. Nếu giới hạn là một phần của nhiệm vụ, chẳng hạn phải hạ cánh trong $200$ bước, và thời gian còn lại có trong quan sát, thì hết giờ là kết thúc thật của MDP và ta đặt $Z_{t+1}=1$. Nếu giới hạn thuộc nhiệm vụ nhưng thời gian còn lại không có trong quan sát, quan sát không đủ Markov theo Nhận xét 08.2 (Pardo và cộng sự, 2018, "Time Limits in Reinforcement Learning", ICML).

**Trong thực hành.** Thư viện môi trường thường trả về hai cờ riêng cho kết thúc và cắt ngắn; $Z$ lấy từ cờ kết thúc, $U$ từ cờ cắt ngắn. Một biến "xong" tính bằng phép hoặc của hai cờ chỉ dùng để quyết định việc đặt lại môi trường, không dùng làm mặt nạ.

Chúng ta đã có ba kết quả. Mạng giá trị hành động trả về $\lvert\mathcal A\rvert$ giá trị sau một lần tính (Định nghĩa 08.1). Mạng mục tiêu giữ $\theta^-$ cố định trong $C$ bước tối ưu, nên mỗi mẫu chuyển có một nhãn đứng yên giữa hai lần đồng bộ (Định nghĩa 08.3). Đích hồi quy $y_t=R_{t+1}+\gamma(1-Z_{t+1})\max_{a'}Q_{\theta^-}(O_{t+1},a')$ chỉ dùng cờ kết thúc làm mặt nạ, còn cờ cắt ngắn chỉ quyết định việc đặt lại môi trường (Định nghĩa 08.4, 08.6). Các kết quả này nói cách tính nhãn cho một mẫu chuyển, nhưng chưa nói mẫu chuyển nào được dùng để cập nhật. Nếu cập nhật theo đúng thứ tự thu thập, các mẫu liền nhau gần giống nhau và cùng lệch về đoạn quỹ đạo gần nhất. Ở phần 3, chúng ta lưu các mẫu chuyển sáu thành phần vào một bộ nhớ và lấy mẫu đều từ đó để giảm tương quan này.

## 3. Bộ nhớ phát lại

<!-- note-topic-id: lec-08-topic-18 -->
### Tương quan giữa các mẫu chuyển liên tiếp

Đến đây mỗi mẫu chuyển đã có một nhãn hồi quy. Bước cập nhật $\theta$ lấy trung bình gradient trên một mini-batch $b$ mẫu, như hạ gradient ngẫu nhiên (stochastic gradient descent, SGD) trong học có giám sát. Lập luận quen thuộc cho SGD dùng giả thiết các mẫu trong mini-batch độc lập và cùng phân phối (i.i.d.): khi đó trung bình của $b$ gradient mẫu có phương sai bằng $1/b$ phương sai của một gradient mẫu. Nếu tác tử cập nhật ngay trên các mẫu chuyển vừa thu thập theo thứ tự thời gian, giả thiết này không còn đúng.

**Trực quan.** Các mẫu chuyển liền nhau trên một quỹ đạo đi qua những quan sát gần nhau, và cùng do một phiên bản tham số $\theta$ chọn hành động. Gradient của chúng vì vậy gần giống nhau: bốn mẫu liền nhau mang ít thông tin mới hơn bốn mẫu ở bốn thời điểm xa nhau. Bài giảng gốc (trang 30) nêu ba ý: tối ưu mạng nơ-ron thường giả sử mini-batch gần i.i.d.; mẫu tương quan có thể làm lệch cập nhật và tăng phương sai; mạng có thể quá khớp quỹ đạo gần đây và quên các vùng trạng thái cũ hơn.

::: example Ví dụ 08.9 (Cỡ mẫu hiệu dụng của bốn mẫu liền nhau)
**Dữ kiện.** Xét một tọa độ của gradient mẫu, gọi là $g_1,g_2,g_3,g_4$ cho bốn mẫu chuyển liền nhau. Giả sử mỗi $g_k$ có phương sai $\sigma^2$, và tương quan giữa hai mẫu cách nhau $k$ bước là $0{,}9^k$ (giả thiết minh họa).

**Tính.** Với $\bar g=\tfrac14\sum_{i=1}^4g_i$,
$$
\begin{aligned}
\operatorname{Var}\bar g&=\frac{\sigma^2}{16}\sum_{i=1}^4\sum_{j=1}^40{,}9^{\lvert i-j\rvert}
=\frac{\sigma^2}{16}\bigl(4+2(3\cdot0{,}9+2\cdot0{,}81+0{,}729)\bigr)\\
&=\frac{14{,}098}{16}\,\sigma^2\approx0{,}881\,\sigma^2.
\end{aligned}
$$
Nếu bốn mẫu độc lập, $\operatorname{Var}\bar g=\sigma^2/4=0{,}25\,\sigma^2$. Cỡ mẫu hiệu dụng, tức số mẫu độc lập cho cùng phương sai, là $\sigma^2/(0{,}881\,\sigma^2)\approx1{,}1$.

**Diễn giải.** Với tương quan này, mini-batch bốn mẫu liền nhau giảm phương sai gần như không hơn một mẫu. Muốn trung bình gradient có phương sai nhỏ, các mẫu trong mini-batch phải đến từ những thời điểm xa nhau.
:::

![Hai hàng, mỗi hàng là 20 bước thời gian của cùng một quỹ đạo, vẽ bằng chấm tròn rỗng. Hàng trên, liên tiếp: bốn mẫu ở t bằng 17 đến 20 đánh dấu bằng hình vuông đặc, ngoặc chung ghi cùng đoạn quỹ đạo, cùng theta. Hàng dưới, lấy rải: bốn mẫu ở t bằng 3, 8, 12, 19 đánh dấu bằng tam giác đặc.](img/lec-08/correlated-minibatch.svg)

Hình so sánh hai cách chọn bốn mẫu từ hai mươi bước của cùng một quỹ đạo. Hàng trên chọn bốn bước cuối $t=17,\dots,20$ (hình vuông đặc): chúng thuộc cùng một đoạn quỹ đạo và cùng một phiên bản $\theta$. Hàng dưới chọn bốn bước rải trên toàn quỹ đạo, $t=3,8,12,19$ (tam giác đặc): tương quan giữa các mẫu nhỏ hơn vì chúng cách nhau xa hơn.

Tương quan không nhất thiết làm gradient trung bình bị chệch. Với tương quan dương, hệ quả là phương sai lớn hơn, và hướng cập nhật đi theo vùng quan sát vừa thăm: qua nhiều bước liên tiếp, gradient dao động theo đoạn quỹ đạo gần nhất thay vì theo toàn bộ dữ liệu. Ngay cả khi lấy mẫu rải như hàng dưới, các mẫu vẫn không độc lập cùng phân phối: chúng cùng thuộc một quỹ đạo, và phân phối của dữ liệu đổi khi chính sách hành vi đổi theo $\theta$.

**Trong thực hành.** Cỡ mẫu hiệu dụng phụ thuộc mức tương quan, và mức này đổi theo môi trường và chính sách; Ví dụ 08.9 chỉ minh họa cơ chế. Một dấu hiệu dễ quan sát khi cập nhật trên mẫu liền nhau là giá trị hàm mất mát dao động theo từng đoạn của lượt.

Chúng ta cần một cách chọn mẫu cho mini-batch không phụ thuộc thứ tự thu thập. Ở mục tiếp theo, chúng ta lưu các mẫu chuyển vào một bộ nhớ và lấy mẫu đều từ đó.

<!-- note-topic-id: lec-08-topic-06 -->
### Bộ nhớ phát lại (experience replay)

Theo Ví dụ 08.9, bốn mẫu chuyển liền nhau, với tương quan $0{,}9^k$ giữa hai mẫu cách nhau $k$ bước, giảm phương sai của gradient trung bình như khoảng $1{,}1$ mẫu độc lập. Muốn mini-batch gồm các mẫu ở những thời điểm xa nhau, chúng ta phải giữ lại các mẫu chuyển đã thu thập thay vì dùng mỗi mẫu một lần, và phải chọn mẫu cho mini-batch không theo thứ tự thu thập. Bộ nhớ của máy tính có hạn, nên còn phải quy định mẫu nào bị bỏ khi bộ nhớ đầy. Bài giảng gốc (trang 19, 32) nêu hai việc đầu: lưu kinh nghiệm của tác tử, rồi lấy ngẫu nhiên các mini-batch từ đó. Mnih và cộng sự (2015, mục Methods) giải quyết việc thứ ba: bộ nhớ chỉ giữ $N$ mẫu chuyển gần nhất, và mini-batch được lấy đều từ các mẫu đang lưu.

::: definition Định nghĩa 08.7 (Bộ nhớ phát lại)
Cho số nguyên dương $N$, gọi là dung lượng, và cỡ mini-batch $b\in\mathbb N_+$. Bộ nhớ phát lại (experience replay) là một bộ đệm vòng $\mathcal D$ gồm $N$ vị trí đánh số $1,\dots,N$ và một con trỏ ghi; mỗi vị trí chứa nhiều nhất một mẫu chuyển sáu thành phần $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ của Định nghĩa 08.6. Đánh số các mẫu chuyển $1,2,\dots$ theo thứ tự thu thập. Bộ nhớ hoạt động theo hai quy tắc.

1. Ghi: sau mỗi bước môi trường, mẫu chuyển vừa thu thập được ghi vào vị trí của con trỏ ghi, rồi con trỏ tiến một vị trí, từ vị trí $N$ quay về vị trí $1$. Mẫu chuyển thứ $k$ nằm ở vị trí $((k-1)\bmod N)+1$; khi bộ nhớ đã đầy, mẫu mới ghi đè mẫu cũ nhất.
2. Rút: một mini-batch gồm $b$ lần rút đều từ $\lvert\mathcal D\rvert=\min(k,N)$ mẫu đang lưu sau $k$ lần ghi. Các lần rút độc lập (rút có hoàn lại), hoặc không lặp lại vị trí (rút không hoàn lại, cần $b\le\lvert\mathcal D\rvert$); trong cả hai cách, xét riêng từng lần rút, mỗi mẫu đang lưu có xác suất $1/\lvert\mathcal D\rvert$.
:::

Hai quy tắc trả lời hai câu hỏi khác nhau. Quy tắc ghi quyết định bộ nhớ chứa gì: sau $k\ge N$ lần ghi, $\mathcal D$ chứa đúng $N$ mẫu chuyển gần nhất, từ mẫu $k-N+1$ đến mẫu $k$. Quy tắc rút quyết định mini-batch gồm gì: mọi mẫu đang lưu có cùng cơ hội được chọn, bất kể được ghi lúc nào. Với $N$ lớn, hai lần rút độc lập hiếm khi trúng hai mẫu liền nhau: xác suất đó bằng $2(N-1)/N^2\approx2/N$, tức khoảng $2\cdot10^{-6}$ với $N=10^6$, dung lượng Mnih và cộng sự (2015, Extended Data Table 1) dùng cho Atari cùng cỡ mini-batch $b=32$.

Mỗi quy tắc có vai trò riêng. Dung lượng hữu hạn giữ bộ nhớ trong giới hạn của máy, nhưng $N$ phải lớn hơn nhiều so với $b$. Bỏ yêu cầu này, chẳng hạn $N=b=4$ và rút không hoàn lại: mỗi mini-batch là đúng bốn mẫu chuyển gần nhất, tức bốn mẫu liền nhau như trong Ví dụ 08.9, nên tương quan trong mini-batch không giảm. Ghi đè mẫu cũ nhất giữ $\mathcal D$ gần với hành vi hiện tại. Bỏ quy tắc này, chẳng hạn ngừng ghi khi bộ nhớ đầy: $\mathcal D$ giữ mãi $N$ mẫu đầu tiên, sinh ra khi $\theta$ còn gần giá trị khởi tạo, nên các quan sát mà chính sách về sau mới đi tới không bao giờ vào mini-batch. Rút đều làm mini-batch không phụ thuộc thứ tự thu thập. Bỏ quy tắc này, chẳng hạn luôn rút $b$ mẫu mới nhất: phép cập nhật trở lại thành cập nhật theo thứ tự thời gian của Ví dụ 08.9.

::: example Ví dụ 08.10 (Bộ đệm vòng dung lượng 6)
**Dữ kiện.** $N=6$, $b=2$. Tác tử đã thu thập $8$ mẫu chuyển, đánh số $1,\dots,8$ theo thứ tự thu thập.

**Tính.** Mẫu $1$ đến $6$ lần lượt vào vị trí $1$ đến $6$, và bộ nhớ đầy. Mẫu $7$ vào vị trí $((7-1)\bmod6)+1=1$, ghi đè mẫu $1$; mẫu $8$ vào vị trí $2$, ghi đè mẫu $2$. Sau $8$ bước, các vị trí $1,\dots,6$ chứa mẫu $7,8,3,4,5,6$, $\lvert\mathcal D\rvert=6$, và con trỏ ghi ở vị trí $3$, nơi chứa mẫu $3$, mẫu cũ nhất. Mỗi lần rút chọn mỗi mẫu $3,\dots,8$ với xác suất $1/6$; mẫu $1$ và $2$ có xác suất $0$.

**Diễn giải.** Mini-batch trong hình gồm vị trí $2$ và $5$, tức mẫu $8$ và mẫu $5$, cách nhau ba bước trên dòng thời gian. Mẫu $9$ sẽ ghi đè mẫu $3$, và sau đó mẫu $3$ không còn được rút.
:::

![Sáu ô xếp thành một dải, nối thành vòng bằng một mũi tên đi từ ô thứ sáu vòng xuống dưới về ô thứ nhất. Sau 8 bước, các ô từ trái sang phải chứa mẫu 7, 8, 3, 4, 5, 6: mẫu 7 và 8, viền đậm và chữ đậm, đã ghi đè mẫu 1 và 2. Mũi tên con trỏ ghi chỉ vào ô chứa mẫu 3, mẫu cũ nhất, nơi mẫu 9 sẽ được ghi. Hai tam giác đặc dưới ô chứa mẫu 8 và ô chứa mẫu 5 đánh dấu một mini-batch b bằng 2 rút đều từ bộ đệm.](img/lec-08/replay-buffer.svg)

Hình vẽ trạng thái của bộ nhớ trong Ví dụ 08.10. Sáu ô là sáu vị trí; mũi tên vòng từ ô cuối về ô đầu chỉ thứ tự ghi của bộ đệm vòng. Hai ô đầu, viền và chữ đậm, chứa mẫu $7$ và $8$, đã ghi đè mẫu $1$ và $2$. Mũi tên phía trên chỉ vị trí của con trỏ ghi, ô chứa mẫu cũ nhất. Hai tam giác đặc đánh dấu hai vị trí được rút vào một mini-batch cỡ $b=2$.

**Môi trường tự đặt lại.** Quy tắc ghi đòi mỗi vị trí chứa đúng một mẫu chuyển, tức $O_{t+1}$ phải là quan sát mà tác tử nhận ngay sau $A_t$. Ở bước cuối của lượt, khi $Z_{t+1}\lor U_{t+1}=1$, một số thư viện môi trường tự đặt lại. Trong một cách cài đặt, lời gọi thực hiện bước trả về quan sát đầu của lượt mới, còn quan sát cuối của lượt cũ nằm trong một trường thông tin riêng, có tên phụ thuộc phiên bản thư viện. Bộ nhớ phải lưu quan sát cuối của lượt cũ làm $O_{t+1}$; quan sát đầu của lượt mới là quan sát xuất phát của mẫu chuyển kế tiếp. Trong một cách cài đặt khác, lời gọi kế tiếp chỉ đặt lại môi trường; khi đó không có mẫu chuyển nào đi từ quan sát cuối của lượt cũ sang quan sát đầu của lượt mới, và bộ nhớ không được lưu cặp quan sát đó. Trong cách thứ nhất, lưu nhầm quan sát đầu của lượt mới làm $O_{t+1}$ chỉ đổi đích của mẫu chuyển bị cắt ngắn: với $Z_{t+1}=1$, mặt nạ $(1-Z_{t+1})$ xóa phần bootstrap nên $O_{t+1}$ không vào đích; với $U_{t+1}=1$, $Z_{t+1}=0$, đích $R_{t+1}+\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$ lấy giá trị từ một quan sát không nối với $O_t$.

**Trong thực hành.** Bộ nhớ thường được cài bằng các mảng cấp phát sẵn $N$ hàng cho từng thành phần của mẫu chuyển, một con trỏ ghi và một bộ đếm $\lvert\mathcal D\rvert$; rút một mini-batch là sinh $b$ chỉ số đều trong $\{1,\dots,\lvert\mathcal D\rvert\}$. Với đầu vào Atari của Ví dụ 08.2, mỗi mẫu chứa hai chồng bốn khung $84\times84$, tức $2\cdot28\,224=56\,448$ số; nếu mỗi điểm ảnh là một byte, $N=10^6$ mẫu chiếm khoảng $56$ GB. Hai chồng của các mẫu liền nhau dùng chung ba khung, nên lưu mỗi khung một lần ($84\cdot84=7\,056$ byte) rồi ghép chồng khi rút giảm con số này khoảng tám lần. Bộ nhớ chỉ đổi cách chọn mẫu: đích của một mẫu được rút vẫn tính theo Định nghĩa 08.4 với $\theta^-$ tại lúc rút, không phải $\theta^-$ tại lúc mẫu được thu thập (bài giảng gốc, trang 20).

**Kiểm tra nhanh.** Trong Ví dụ 08.10, sau $10$ bước, $\mathcal D$ chứa những mẫu nào và mẫu $11$ sẽ ghi vào vị trí nào? Mẫu $9$ và $10$ ghi đè mẫu $3$ và $4$ ở vị trí $3$ và $4$, nên $\mathcal D$ chứa mẫu $5,\dots,10$; mẫu $11$ vào vị trí $((11-1)\bmod6)+1=5$ và ghi đè mẫu $5$.

Bộ nhớ phát lại cho mỗi bước tối ưu một mini-batch rút đều từ $N$ mẫu chuyển gần nhất. Mỗi mẫu trong $\mathcal D$ do phiên bản hành vi lúc thu thập sinh ra, nên $\mathcal D$ trộn dữ liệu của nhiều chính sách hành vi, và các chính sách này khác chính sách tham lam mà đích hồi quy đánh giá. Ở mục tiếp theo, chúng ta xét vì sao đích hồi quy vẫn dùng được trên dữ liệu như vậy mà không cần tỉ số lấy mẫu quan trọng.

<!-- note-topic-id: lec-08-topic-19 -->
### Dữ liệu khác chính sách trong bộ nhớ

Mỗi mẫu chuyển trong bộ nhớ phát lại do hành vi tại lúc thu thập sinh ra, còn đích hồi quy $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$ đánh giá chính sách tham lam theo $Q_{\theta^-}$. Chúng ta cần biết dữ liệu khác chính sách đích ở những điểm nào, và đích có cần hiệu chỉnh vì sự khác biệt đó hay không.

Nhắc lại từ Bài 06: trong Q-learning dạng bảng, chính sách hành vi $\varepsilon$-tham lam sinh dữ liệu, còn chính sách đích là chính sách tham lam theo $Q$; hai chính sách khác nhau nên Q-learning học khác chính sách (off-policy). Q-learning một bước không cần tỉ số lấy mẫu quan trọng vì hai lẽ. Thứ nhất, $A_t$ là đối số điều kiện của ô $Q(S_t,A_t)$, ô ước lượng $q_*(S_t,A_t)$, nên việc hành vi chọn $A_t$ với xác suất nào không làm lệch mục tiêu của ô đó. Thứ hai, phần tiếp nối tại $S_{t+1}$ được tính trọn bằng phép cực đại, và với chính sách đích tham lam $\pi$, $\max_{a'}Q(S_{t+1},a')=\sum_{a'}\pi(a'\mid S_{t+1})Q(S_{t+1},a')$, tức đúng bằng kỳ vọng theo chính sách đích; không có hành động nào sau $A_t$ được lấy mẫu từ hành vi.

Trong DQN, dữ liệu khác chính sách đích theo hai nguồn.

1. Hành vi $\epsilon_{\mathrm{exp}}$-tham lam theo $Q_\theta$ khác chính sách tham lam của đích, ngay cả với $\theta$ hiện tại. Với $\lvert\mathcal A\rvert=4$ và $\epsilon_{\mathrm{exp}}=0{,}1$, hành vi chọn hành động tham lam với xác suất $1-0{,}1+0{,}1/4=0{,}925$ và mỗi hành động khác với xác suất $0{,}025$, trong khi chính sách tham lam gán xác suất $1$ và $0$.
2. Bộ nhớ giữ các mẫu do những phiên bản $\theta$ cũ sinh ra. Mnih và cộng sự (2015, Extended Data Table 1) dùng $N=10^6$ và cập nhật $\theta$ sau mỗi $4$ bước môi trường, nên khi bộ nhớ đầy, mẫu cũ nhất do một hành vi theo $\theta$ của khoảng $10^6/4=2{,}5\cdot10^5$ bước tối ưu trước sinh ra.

![Bên trái hai khung: hành vi theo theta cũ, đánh dấu bằng vòng tròn rỗng, và hành vi theo theta hiện tại, đánh dấu bằng hình vuông đặc. Hai mũi tên từ hai khung cùng đổ vào bộ nhớ phát lại ở giữa, vẽ thành sáu ô: hai ô đầu chứa hình vuông, bốn ô sau chứa vòng tròn. Một mũi tên từ bộ nhớ sang khung mini-batch bên phải, chứa một vòng tròn và một hình vuông: mini-batch trộn mẫu của cả hai phiên bản hành vi.](img/lec-08/offpolicy-replay.svg)

Hình vẽ nguồn thứ hai. Hai phiên bản hành vi, theo $\theta$ cũ (vòng tròn rỗng) và theo $\theta$ hiện tại (hình vuông đặc), cùng ghi vào bộ nhớ phát lại; hai ô đầu chứa mẫu mới vừa ghi đè hai mẫu cũ nhất, như bộ đệm vòng của Ví dụ 08.10. Mini-batch rút đều từ bộ nhớ nên trộn mẫu của cả hai phiên bản.

Mệnh đề sau chuyển lý do của dạng bảng sang đích hồi quy của DQN.

::: proposition Mệnh đề 08.8 (Đích một bước không phụ thuộc hành vi đã sinh mẫu)
**Giả thiết.** Quan sát $O_t$ đủ Markov (Nhận xét 08.2), và động lực của môi trường, tức phân phối của $(R_{t+1},O_{t+1},Z_{t+1})$ khi biết $(O_t,A_t)$, không đổi theo thời gian. Tham số $\theta^-$ cố định. Mẫu $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ được rút đều từ $\mathcal D$ (Định nghĩa 08.7), trong đó mỗi mẫu được ghi bởi một hành vi chọn $A_t$ chỉ dựa trên lịch sử quan sát, hành động và một nguồn ngẫu nhiên riêng.

**Kết luận.** Với mọi cặp $(o,a)$ có xác suất dương trong $\mathcal D$,
$$
\begin{aligned}
\mathbb E\bigl[y_i\mid O_i=o,A_i=a\bigr]&=\mathbb E\Bigl[R_{t+1}+\gamma(1-Z_{t+1})\max_{a'}Q_{\theta^-}(O_{t+1},a')\Bigm|O_t=o,A_t=a\Bigr]\\
&=(\mathcal TQ_{\theta^-})(o,a),
\end{aligned}
$$
dù mẫu do phiên bản hành vi nào sinh ra.

**Điều kiện áp dụng.** Đích một bước với phép cực đại tính trọn tại $O'_i$.

**Phạm vi.** Mệnh đề chỉ nói về kỳ vọng có điều kiện của đích khi biết cặp $(O_i,A_i)$. Phân phối của chính cặp $(O_i,A_i)$ trong $\mathcal D$ vẫn do các hành vi đã sinh dữ liệu quyết định.
:::

::: proof Chứng minh Mệnh đề 08.8
**Bước 1 (một mẫu khi được ghi).** Xét mẫu được ghi tại bước $t$ bởi hành vi theo một tham số $\theta_t$ nào đó. Hành vi chọn $A_t$ từ lịch sử và nguồn ngẫu nhiên riêng, không dùng tới $(R_{t+1},O_{t+1},Z_{t+1})$ chưa xảy ra. Khi $O_t$ đủ Markov và động lực không đổi, phân phối của $(R_{t+1},O_{t+1},Z_{t+1})$ khi biết lịch sử và $A_t$ chỉ phụ thuộc $(O_t,A_t)$, nên khi biết $O_t=o$, $A_t=a$, nó là một phân phối $p(\cdot\mid o,a)$ chung cho mọi $\theta_t$.

**Bước 2 (phép rút).** Phép rút đều chọn vị trí mà không nhìn vào nội dung mẫu. Vì vậy, khi biết mẫu được rút có $(O_i,A_i)=(o,a)$, bộ $(R_i,O'_i,Z_i)$ vẫn có phân phối $p(\cdot\mid o,a)$ của Bước 1, bất kể vị trí và phiên bản hành vi.

**Bước 3 (kỳ vọng của đích).** Với $\theta^-$ cố định, $y_i$ là một hàm xác định của $(R_i,O'_i,Z_i)$. Lấy kỳ vọng theo $p(\cdot\mid o,a)$:
$$
\begin{aligned}
\mathbb E\bigl[y_i\mid O_i=o,A_i=a\bigr]&=\mathbb E_{(R,O',Z)\sim p(\cdot\mid o,a)}\Bigl[R+\gamma(1-Z)\max_{a'}Q_{\theta^-}(O',a')\Bigr]\\
&=(\mathcal TQ_{\theta^-})(o,a).
\end{aligned}
$$
Không có hành động nào sau $A_i$ được lấy từ hành vi, nên không có tỉ số xác suất nào cần đưa vào. $\square$
:::

Mệnh đề dựa trên hai giả thiết có vai trò riêng. Giả thiết Markov làm phân phối của phần tiếp nối chỉ phụ thuộc $(O_i,A_i)$. Bỏ giả thiết này, chẳng hạn khi quan sát là một khung ảnh không cho biết hướng chuyển động của quả bóng (Ví dụ 08.4): cùng một quan sát $o$ ứng với nhiều trạng thái ẩn, và tỉ lệ các trạng thái ẩn này phụ thuộc hành vi đã đưa tác tử tới $o$, nên mẫu của hai phiên bản hành vi có kỳ vọng đích khác nhau. Giả thiết động lực không đổi làm mẫu cũ vẫn là mẫu đúng của môi trường hiện tại. Bỏ giả thiết này, chẳng hạn khi luật của môi trường đổi giữa chừng: các mẫu ghi trước thời điểm đổi mô tả một môi trường không còn tồn tại, và chúng ở lại trong bộ nhớ cho tới khi bị ghi đè.

::: example Ví dụ 08.11 (Tỉ số lấy mẫu quan trọng xóa mẫu của hành động thăm dò)
**Dữ kiện.** $\lvert\mathcal A\rvert=4$, $\epsilon_{\mathrm{exp}}=0{,}1$, $\gamma=0{,}9$. Tại quan sát $o$, $\mathbf q_\theta(o)=(0{,}8;\,2{,}5;\,-0{,}3;\,1{,}9)$ như Ví dụ 08.3, nên hành động tham lam là $a_2$. Hành vi chọn $a_4$ và nhận mẫu chuyển có $R_i=1$, $Z_i=0$, $\max_{a'}Q_{\theta^-}(O'_i,a')=4$.

**Tính.** Đích $y_i=1+0{,}9\cdot4=4{,}6$, một mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(o,a_4)$ theo Mệnh đề 08.8. Xác suất hành vi chọn $a_4$ là $0{,}1/4=0{,}025$, xác suất chính sách tham lam chọn $a_4$ là $0$. Nếu nhân sai số của mẫu với tỉ số $\pi(a_4\mid o)/b(a_4\mid o)=0/0{,}025=0$, với $b$ ở đây là chính sách hành vi, mẫu bị xóa khỏi cập nhật.

**Diễn giải.** Hiệu chỉnh theo tỉ số tại $A_i$ làm mọi mẫu của hành động không tham lam có trọng số $0$, nên $Q_\theta(o,a_4)$ không bao giờ học từ dữ liệu, dù đích $4{,}6$ là mẫu đúng của giá trị cần ước lượng.
:::

**Trong thực hành.** Hàm mất mát DQN cơ bản không chứa tỉ số lấy mẫu quan trọng, và Mệnh đề 08.8 giải thích vì sao điều này đúng với đích một bước. Khi đích dùng nhiều bước, như đích $n$ bước, các hành động $A_{t+1},\dots,A_{t+n-1}$ đều lấy từ hành vi đã ghi mẫu, và đích chỉ đánh giá chính sách đích khi được hiệu chỉnh bằng tích các tỉ số lấy mẫu quan trọng (Sutton và Barto, 2018, §7.3). Hành vi vẫn quyết định tần suất của từng cặp $(O_i,A_i)$ trong mini-batch, tức trọng số của từng cặp khi khớp $Q_\theta$. Với bảng, mỗi ô được khớp riêng nên trọng số này không đổi giá trị đích của ô; với xấp xỉ hàm, các cặp tranh nhau tham số dùng chung, và trọng số theo phân phối của $\mathcal D$ là thành phần học khác chính sách trong bộ ba bất ổn của Bài 07.

**Kiểm tra nhanh.** Một mẫu trong $\mathcal D$ được ghi bởi hành vi theo $\theta$ của $2{,}5\cdot10^5$ bước tối ưu trước. Khi mẫu được rút, đích của nó tính bằng tham số nào, và có cần hiệu chỉnh cho phiên bản hành vi cũ không? Đích tính bằng $\theta^-$ tại lúc rút. Theo Mệnh đề 08.8, khi $O_i$ đủ Markov và động lực không đổi, phiên bản hành vi cũ chỉ quyết định cặp $(O_i,A_i)$ được ghi, không đổi kỳ vọng của đích, nên không cần hiệu chỉnh.

Chúng ta đã có hai kết quả về bộ nhớ phát lại: mini-batch rút đều từ $N$ mẫu gần nhất, và đích một bước của mỗi mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_i,A_i)$ bất kể phiên bản hành vi đã sinh mẫu. Phân phối của các cặp $(O_i,A_i)$ trong mini-batch thì vẫn do các hành vi cũ và hiện tại quyết định, và các mẫu vẫn cùng thuộc một số quỹ đạo. Ở mục tiếp theo, chúng ta nêu những điều bộ nhớ phát lại không bảo đảm.

<!-- note-topic-id: lec-08-topic-07 -->
### Giới hạn của bộ nhớ phát lại

Bộ nhớ phát lại cho mini-batch rút đều từ $N$ mẫu gần nhất (Định nghĩa 08.7), và đích một bước của mỗi mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_i,A_i)$ bất kể phiên bản hành vi đã sinh mẫu (Mệnh đề 08.8). Trước khi dùng mini-batch này để cập nhật $\theta$, chúng ta cần phát biểu đúng phạm vi của cơ chế: nó làm được gì, đo bằng số, và không bảo đảm điều gì.

Bộ nhớ phát lại làm được ba việc. Thứ nhất, nó giảm tương quan ngắn hạn: hai mẫu trong một mini-batch hiếm khi liền nhau, với xác suất $2/N$ khi rút không hoàn lại (Ví dụ 08.12 dưới đây). Thứ hai, nó tái sử dụng mẫu: với các giá trị của Mnih và cộng sự (2015, Extended Data Table 1), $N=10^6$, một bước tối ưu sau mỗi $4$ bước môi trường và $b=32$, một mẫu ở trong bộ nhớ trong $10^6$ bước môi trường, tức $2{,}5\cdot10^5$ bước tối ưu, mỗi bước rút $32$ lần, mỗi lần trúng mẫu đó với xác suất $10^{-6}$; số lần mẫu được dùng có kỳ vọng $2{,}5\cdot10^5\cdot32\cdot10^{-6}=8$. Thứ ba, mỗi mini-batch trộn nhiều đoạn quỹ đạo thay vì chỉ đoạn vừa thu thập, nên một bước cập nhật ít bị kéo theo vùng quan sát vừa thăm. Bài giảng gốc (trang 32) nêu các lợi ích tái sử dụng dữ liệu quá khứ và cải thiện hiệu quả mẫu, và viết rằng bộ nhớ "phá vỡ" tương quan theo thời gian; ở đây chúng ta viết "giảm", vì xác suất $2/N$ của một cặp liền nhau luôn dương.

::: remark Nhận xét 08.9 (Ba điều bộ nhớ phát lại không bảo đảm)
Với bộ nhớ phát lại của Định nghĩa 08.7:

1. các mẫu trong một mini-batch không độc lập và cùng phân phối (i.i.d.) theo một phân phối cố định: khi biết $\mathcal D$, các lần rút có hoàn lại là i.i.d. theo phân phối thực nghiệm của $\mathcal D$, nhưng nội dung của $\mathcal D$ là các đoạn của một số ít quỹ đạo, xác suất rút hai mẫu liền nhau là $2/N>0$, và hai mẫu liên tiếp $k$, $k+1$ của một lượt dùng chung một quan sát, vì $O'$ của mẫu $k$ là $O$ của mẫu $k+1$;
2. phân phối của $\mathcal D$ không đứng yên: hành vi đổi cùng $\theta$ và bộ đệm thay mẫu cũ nhất bằng mẫu mới, nên phân phối của các cặp $(O_i,A_i)$ được rút trôi theo thời gian;
3. thuật toán dùng bộ nhớ phát lại không có bảo đảm hội tụ: xấp xỉ hàm, bootstrap và học khác chính sách vẫn cùng có mặt, tức bộ ba bất ổn của Bài 07 vẫn đủ ba yếu tố.
:::

Ba điều này có ba nguồn khác nhau. Điều thứ nhất đến từ việc mọi mẫu đều do một tác tử thu thập dọc các quỹ đạo. Lấy mẫu đều làm các lần rút độc lập với nhau khi đã biết $\mathcal D$, nhưng không làm nội dung của $\mathcal D$ thành các mẫu độc lập của một phân phối cố định: nó chỉ làm hiếm các cặp liền nhau, không tạo ra các quỹ đạo độc lập. Như đã nêu ở mục tương quan, mẫu tương quan không nhất thiết làm gradient trung bình bị chệch; hệ quả chắc chắn hơn là phương sai lớn hơn so với cùng số mẫu độc lập. Điều thứ hai đến từ vòng lặp giữa dữ liệu và tham số: $\theta$ đổi thì hành vi đổi, hành vi đổi thì các mẫu mới ghi vào $\mathcal D$ đổi. Vì vậy lời giải hồi quy tốt nhất của Nhận xét 08.5, vốn giả sử các cặp $(O_t,A_t)$ lấy theo một phân phối cố định, chỉ áp dụng gần đúng khi phân phối của $\mathcal D$ đổi chậm so với số bước tối ưu giữa hai lần đồng bộ. Điều thứ ba đến từ chỗ bộ nhớ chỉ đổi cách chọn mẫu: nó không bỏ xấp xỉ hàm, không bỏ bootstrap, và theo Mệnh đề 08.8 nó còn thêm một nguồn dữ liệu khác chính sách. Mệnh đề 07.37 của Bài 07 cho một ví dụ tuyến tính hai trạng thái có đủ ba yếu tố mà tham số tăng không chặn; bộ nhớ phát lại không loại trừ ví dụ đó.

::: example Ví dụ 08.12 (Hai mẫu liền nhau trong một mini-batch)
**Dữ kiện.** $N=6$, bộ nhớ chứa mẫu $3,\dots,8$ như Ví dụ 08.10: các vị trí $1,\dots,6$ chứa mẫu $7,8,3,4,5,6$. Mini-batch có $b=2$ mẫu, rút không hoàn lại.

**Tính.** Rút không hoàn lại hai trong sáu mẫu cho $\binom62=15$ cặp, mỗi cặp có xác suất như nhau. Cặp mẫu $4$, mẫu $5$ có xác suất $1/15$. Hai mẫu liền nhau theo thứ tự thu thập là năm cặp $(3,4)$, $(4,5)$, $(5,6)$, $(6,7)$, $(7,8)$, nên xác suất rút được hai mẫu liền nhau là $5/15=1/3$. Cặp $(6,7)$ được tính dù mẫu $6$ ở vị trí $6$ và mẫu $7$ ở vị trí $1$: "liền nhau" xét theo thời gian, không theo vị trí trong bộ đệm.

**Tổng quát.** Với $N$ mẫu liên tiếp trong bộ nhớ, có $N-1$ cặp liền nhau trong $\binom N2$ cặp, nên xác suất là $(N-1)/\binom N2=2/N$; với $N=10^6$, xác suất bằng $2\cdot10^{-6}$.

**Diễn giải.** Dung lượng lớn làm hiếm cặp liền nhau, nhưng xác suất luôn dương, và các mẫu không liền nhau của cùng một lượt vẫn có thể tương quan.
:::

**Trong thực hành.** Dung lượng $N$ là một lựa chọn cân bằng. $N$ lớn làm hiếm cặp liền nhau và làm phân phối của $\mathcal D$ trôi chậm, nhưng giữ lâu các mẫu của những hành vi đã cũ. $N$ nhỏ giữ dữ liệu gần hành vi hiện tại, nhưng mini-batch gần với mini-batch liên tiếp hơn; ở cực $N=b$ của mục bộ nhớ phát lại, mọi mẫu trong mini-batch đều liền nhau. Mnih và cộng sự (2015, mục Methods) nêu thêm hai giới hạn của cách làm này: bộ đệm ghi đè theo thứ tự thời gian và lấy mẫu đều coi mọi mẫu chuyển quan trọng như nhau, không phân biệt mẫu mang nhiều thông tin. Hiệu quả của bộ nhớ phát lại trong DQN là kết quả thực nghiệm, không phải hệ quả của một định lý.

**Kiểm tra nhanh.** Hai mẫu liên tiếp $k$ và $k+1$ trong cùng một lượt có thành phần nào trùng nhau? Quan sát kế tiếp $O_{t+1}$ của mẫu $k$ chính là quan sát $O_t$ của mẫu $k+1$; khi mẫu $k$ là bước cuối của lượt thì không, vì mẫu $k+1$ bắt đầu từ quan sát đầu của lượt mới.

Ở phần 3, chúng ta đã có bốn kết quả. Mẫu chuyển liền nhau tương quan, nên mini-batch liên tiếp có cỡ mẫu hiệu dụng nhỏ: bốn mẫu với tương quan $0{,}9^k$ chỉ tương đương khoảng $1{,}1$ mẫu độc lập (Ví dụ 08.9). Bộ nhớ phát lại là bộ đệm vòng giữ $N$ mẫu gần nhất, mini-batch gồm $b$ lần rút đều (Định nghĩa 08.7), và mỗi mẫu được dùng lại trung bình khoảng $8$ lần với các giá trị của DQN gốc. Đích một bước của mỗi mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_i,A_i)$ dù mẫu do phiên bản hành vi nào sinh ra, nên không cần tỉ số lấy mẫu quan trọng (Mệnh đề 08.8). Cuối cùng, bộ nhớ không tạo mẫu độc lập cùng một phân phối cố định, không làm phân phối dữ liệu đứng yên, và không đem lại bảo đảm hội tụ (Nhận xét 08.9). Đến đây chúng ta có, cho mỗi bước tối ưu, một mini-batch $b$ mẫu với đích $y_i$ cố định giữa hai lần đồng bộ, nhưng chưa có cách biến mini-batch đó thành một bước cập nhật $\theta$. Ở phần 4, chúng ta viết hàm mất mát trên mini-batch, cho gradient chỉ đi qua dự đoán $Q_\theta(O_i,A_i)$ bằng phép dừng gradient, rồi ghép thu thập, lưu, rút mẫu, tối ưu và đồng bộ thành thuật toán DQN đầy đủ.

## Hàm mất mát, vòng huấn luyện và bất ổn

<!-- note-topic-id: lec-08-topic-08 -->
### Gather và dừng gradient ở đích

**Vấn đề.** Trong batch, mạng xuất giá trị cho *mọi* hành động, nhưng loss chỉ cần
giá trị của *hành động đã lưu*; đồng thời gradient không được chảy vào đường tạo đích.

**Trực quan.** Hai đường tính tách bạch:

- *Đường dự đoán*: $q_i = Q_\theta(O_i,A_i)$, phụ thuộc $\theta$, nhận gradient.
- *Đường tạo đích*: dùng $Q_{\theta^-}(O'_i,\cdot)$, $\theta^-$ cố định giữa hai
  lần đồng bộ, được đặt trong toán tử dừng gradient $\operatorname{sg}$.

**Ví dụ.** Gather là phép chọn theo chỉ số: từ tensor $[b,|\mathcal A|]$, lấy một
phần tử mỗi hàng theo hành động đã lưu $A_i$, tạo vector $q\in\mathbb R^b$.
Ký hiệu $\operatorname{sg}$ tương ứng detach/no-grad trong mã thực tế.

**Hình thức.** Với batch
$\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$:

$$L_B(\theta)=\frac1b\sum_{i=1}^b\bigl(\operatorname{sg}(y_i)-q_i\bigr)^2.$$

Gradient chỉ truyền qua mạng online $Q_\theta$, không qua mạng mục tiêu.

**Ứng dụng và giới hạn.** Bài dùng sai số bình phương trung bình (MSE) để giữ phép
tính minh bạch; Huber là biến thể thực hành có thể thay MSE trong một cài đặt
thực tế. Lỗi phổ biến: quên dừng gradient khiến gradient chảy vào mạng mục tiêu
(nếu nó chia sẻ tham số) hoặc tính gradient trên cả đích.

**Kiểm tra nhanh.** Nếu bỏ $\operatorname{sg}$ quanh $y_i$ và hai mạng chia sẻ
$\theta$, điều gì xảy ra? — Gradient đổi cả dự đoán lẫn nhãn trong cùng một bước;
vòng phản hồi di động trở lại.

<!-- note-topic-id: lec-08-topic-09 -->
### Mất mát và gradient của batch

**Vấn đề.** Cần viết loss và gradient với hệ số đúng để kiểm tra dấu cập nhật.

**Trực quan.** MSE trung bình trên batch; gradient theo từng $q_i$ tỉ lệ với sai
số $q_i - y_i$.

**Ví dụ.** Với batch $B$:

$$L_B(\theta)=\frac{1}{b}\sum_{i=1}^{b}\bigl(y_i-Q_\theta(O_i,A_i)\bigr)^2,
\qquad \theta\leftarrow\theta - \eta\nabla_\theta L_B(\theta).$$

**Hình thức.** Với $q_i = Q_\theta(O_i,A_i)$ và $y_i$ như chủ đề 03, có mặt nạ
theo chủ đề 04:

$$\nabla_\theta L_B=\frac{2}{b}\sum_{i=1}^b(q_i-y_i)\,\nabla_\theta q_i.$$

Tương đương, $\partial L_B/\partial q_i=(2/b)(q_i-y_i)$; quy tắc dây chuyền
nhân đại lượng này với $\nabla_\theta q_i$ rồi cộng theo lô.

Hệ số $\tfrac{2}{b}$ đến từ đạo hàm bình phương và phép lấy trung bình. Dấu của
$(q_i - y_i)$ quyết định $q_i$ tăng hay giảm dưới một bước gradient descent nhỏ:
sai số dương ($q_i > y_i$) làm $q_i$ giảm; sai số âm làm $q_i$ tăng.

**Ứng dụng và giới hạn.** Loss giảm trên batch không đồng nghĩa return đánh giá
tăng. MSE nhạy với sai số lớn; Huber là lựa chọn thực hành khác.

**Kiểm tra nhanh.** Với một mẫu, $\partial L/\partial q_i$ bằng gì? —
$\tfrac{2}{b}(q_i - y_i)$; với $b=2$, hệ số hiệu dụng là $(q_i-y_i)$.

<!-- note-topic-id: lec-08-topic-10 -->
### Vòng DQN: hai đồng hồ $t$ và $k_{\mathrm{opt}}$

**Vấn đề.** Tương tác và tối ưu xen kẽ nhau với các nhịp khác nhau; cần tách rõ
bước môi trường $t$ khỏi bước tối ưu $k_{\mathrm{opt}}$ để giả mã không mơ hồ.

**Trực quan.** Tương tác tạo chuyển tiếp; tối ưu lấy chuyển tiếp đã lưu. Ba siêu
tham số nhịp: $N_{\mathrm{start}}$ (số mẫu làm nóng replay trước khi tối ưu),
$F$ (số bước môi trường giữa hai lần tối ưu), $C$ (chu kỳ đồng bộ mạng mục tiêu,
đếm theo bước tối ưu).

**Hình thức — giả mã.**

*Đầu vào:* $\gamma,\epsilon_{\mathrm{exp}}\in[0,1]$;
$b,N_{\mathrm{start}},N,F,C\in\mathbb N_+$ với $b\le N_{\mathrm{start}}\le N$;
optimizer với tốc độ học $\eta>0$. *Đầu ra:* $\theta$ và chính sách tham lam theo
$Q_\theta$.

1. Khởi tạo $\mathcal D$, $\theta$; đặt $\theta^-\leftarrow\theta$; $O_0$ từ
   reset; $t\leftarrow 0$; $k_{\mathrm{opt}}\leftarrow 0$.
2. Chọn $A_t$ theo $\epsilon_{\mathrm{exp}}$-greedy từ $Q_\theta(O_t,\cdot)$.
3. Bước môi trường; nhận $R_{t+1}$, hai cờ $Z,U$, quan sát trả về và thông tin API.
4. Xác định quan sát của chuyển tiếp: nếu giao diện tự đặt lại môi trường và cung
   cấp `final_observation` trong thông tin trả về, dùng quan sát cuối đó; nếu
   không, dùng quan sát do bước môi trường trả về; lưu vào $\mathcal D$.
5. Nếu cần reset mà API chưa tự reset, gọi reset; gán quan sát bắt đầu vòng kế;
   tăng $t\leftarrow t+1$.
6. Nếu $|\mathcal D|\ge N_{\mathrm{start}}$ và $t\bmod F=0$ (kiểm sau khi tăng $t$):
   lấy đều mini-batch từ $\mathcal D$; gather $q_i=Q_\theta(O_i,A_i)$; trong
   no-grad tính $y_i$; tính MSE; cập nhật $\theta$;
   $k_{\mathrm{opt}}\leftarrow k_{\mathrm{opt}}+1$.
7. Sau cập nhật, nếu $k_{\mathrm{opt}}\bmod C=0$ thì $\theta^-\leftarrow\theta$.
8. Ngoài điều kiện tối ưu: dừng theo ngân sách hoặc tiêu chuẩn đánh giá định trước.

**Ứng dụng và giới hạn.** Bản đơn giản có thể chọn $F=1$, nhưng vẫn phải chờ đủ
$N_{\mathrm{start}}$. Đánh giá dùng chính sách tham lam riêng, không trộn return
khám phá với return đánh giá. Dùng $\gamma<1$ cho nhiệm vụ tiếp diễn.

**Kiểm tra nhanh.** $t\bmod F=0$ và $k_{\mathrm{opt}}\bmod C=0$ đếm trên cùng một
đồng hồ không? — Không; $t$ đếm bước môi trường, $k_{\mathrm{opt}}$ đếm bước tối
ưu; $F$ và $C$ thuộc hai đồng hồ khác nhau.

<!-- note-topic-id: lec-08-topic-11 -->
### Hợp đồng tensor của batch

**Vấn đề.** Lỗi cài đặt DQN thường là lỗi kích thước và kiểu tensor, không phải lỗi
toán.

**Trực quan.** Mọi tensor trong loss phải khớp hợp đồng: batch quan sát đi qua hai
mạng, gather và max tạo hai vector cùng kích thước $[b]$.

**Ví dụ — hợp đồng cho batch Atari:**

- $O, O'$: `float32`, dạng $[b,4,h,w]$.
- $A$: `int64`, dạng $[b]$.
- $R$: `float32`, dạng $[b]$.
- $Z, U$: `bool`, dạng $[b]$.
- Hai mạng tạo $[b,|\mathcal A|]$; gather chọn một hành động mỗi hàng; max tạo một
  giá trị mỗi hàng; $q, y\in\mathbb R^b$; loss là vô hướng.

**Hình thức.** Nếu $A$ có dạng cột $[b,1]$, gather rồi squeeze về $[b]$; tránh
broadcasting thành ma trận $[b,b]$. Chuyển $Z$ sang kiểu số khi tính $1-Z$. Replay
có thể lưu quan sát `uint8` rồi chuyển `float32` khi tạo batch. Mọi tensor dùng
trong loss phải ở cùng thiết bị.

**Ứng dụng và giới hạn.** Hợp đồng này là giao diện tối thiểu để đọc và kiểm tra
tensor, không phải đặc tả tái lập kết quả.

**Kiểm tra nhanh.** Nếu $A$ có dạng $[b,1]$ mà quên squeeze, gather có thể tạo gì?
— Tensor $[b,b]$ do broadcasting; phải squeeze về $[b]$ trước khi tính sai số.

<!-- note-topic-id: lec-08-topic-12 -->
### Mạng mục tiêu và các nguồn bất ổn

**Vấn đề.** Nếu $\theta^-$ đổi mỗi bước, đích di động như khi chỉ có một mạng; nếu
không bao giờ đổi, đích lỗi thời. Cần một nhịp đồng bộ rõ ràng.

**Trực quan.** Giữ $\theta^-$ cố định trong $C$ bước tối ưu, rồi sao chép mạng
online sau bước tối ưu:

$$k_{\mathrm{opt}}\leftarrow k_{\mathrm{opt}}+1,\qquad
k_{\mathrm{opt}}\bmod C=0:\ \theta^-\leftarrow\theta.$$

Thứ tự đúng: cập nhật $\theta$, tăng bộ đếm tối ưu, rồi mới kiểm tra đồng bộ.

**Ví dụ — đích nhảy bao nhiêu khi đồng bộ?** Xét ngay sau $\theta^-\leftarrow\theta$:

$$y_i^{\mathrm{new}}-y_i^{\mathrm{old}}
=\gamma(1-Z_i)\Bigl[\max_{a'}Q_{\theta}(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\Bigr].$$

Mẫu cũ trong replay có thể nhận đích mới dù bộ sáu thành phần
$(O_i,A_i,R_i,O'_i,Z_i,U_i)$ không đổi.

**Hình thức.** Với một chuyển tiếp cố định và $\theta^-$ chưa đổi, $y_i$ cố định.
Mạng mục tiêu làm chậm đích di động; $C$ là một đánh đổi thực nghiệm.

**Ứng dụng và giới hạn.** Mạng mục tiêu không tạo mục tiêu bất biến vĩnh viễn,
không bảo đảm hội tụ, và không phải "mạng đánh giá chính sách" — nó chỉ cung cấp
phần bootstrap. $C$ lớn làm đích ổn định hơn nhưng lỗi thời hơn.

**Kiểm tra nhanh.** Sau đồng bộ, đích của một chuyển tiếp cũ có đổi không? — Có;
nó được tính lại bằng $\theta^-$ mới tại lần lấy mẫu kế tiếp, dù dữ liệu không đổi.

**Ba nguồn bất ổn cần theo dõi.** Chuyển tiếp liên tiếp có tương quan mạnh; đích
bootstrap thay đổi theo mạng; và DQN đồng thời dùng xấp xỉ hàm, bootstrap cùng
dữ liệu lệch chính sách. Sự kết hợp sau thường được gọi là *bộ ba nguy hiểm*.
Nó có thể gây dao động hoặc phân kỳ trong một số thiết lập, không có nghĩa DQN
luôn phân kỳ. Bộ nhớ phát lại giảm tương quan ngắn hạn, còn mạng mục tiêu làm
chậm sự thay đổi của đích. Hai cơ chế này không tạo dữ liệu độc lập, phân phối
đồng nhất và không cho bảo đảm hội tụ tổng quát.

---

## Phần 3 — Bộ tối ưu

<!-- note-topic-id: lec-08-topic-14 -->
### SGD, RMSprop và Adam theo từng tọa độ

**Vấn đề.** Optimizer nhận gradient của loss và đổi nó thành bước tham số; nó
không sửa đích hay dữ liệu sai. Ba quy tắc cập nhật phổ biến chuẩn hóa gradient
theo những cách khác nhau.

**Hình thức chung.** Với chỉ số cập nhật $j\in\mathbb N_+$ (trùng $k_{\mathrm{opt}}$)
và tốc độ học $\eta>0$:

$$g_j=\nabla_\theta L_{B_j}(\theta_{j-1}),\qquad \theta_j=\operatorname{Update}(\theta_{j-1},g_j).$$

Các hệ số $\rho,\beta_1,\beta_2\in[0,1)$; $\epsilon_{\mathrm{opt}}>0$ ổn định phép
chia. **Lưu ý:** $\epsilon_{\mathrm{opt}}$ (số học của optimizer) khác hoàn toàn
$\epsilon_{\mathrm{exp}}$ (xác suất khám phá của chính sách hành vi).

**SGD.**

$$\theta_j=\theta_{j-1}-\eta g_j.$$

Không cần trạng thái phụ theo từng tham số; mọi tọa độ dùng cùng hệ số bước $\eta$.
Đơn giản, tiết kiệm bộ nhớ, dễ phân tích; nhưng nhạy với tốc độ học và có thể dao
động trong bài toán điều kiện kém.

**RMSprop** (theo từng tọa độ, $v_0=0$, $\rho\in[0,1)$; biến thể epsilon ngoài căn):

$$v_j=\rho v_{j-1}+(1-\rho)\,g_j\odot g_j,\qquad
\theta_j=\theta_{j-1}-\eta\, g_j\oslash\bigl(\sqrt{v_j}+\epsilon_{\mathrm{opt}}\bigr).$$

Gradient lớn kéo dài ở một tọa độ làm giảm bước hiệu dụng tại tọa độ đó; gradient
nhỏ nhận bước tương đối lớn hơn. Hữu ích trong DQN vì mục tiêu TD nhiễu và không
dừng; RMSprop xuất hiện trong các cài đặt DQN ban đầu.

**Adam** ($m_0=v_0=0$, $\beta_1,\beta_2\in[0,1)$):

$$m_j=\beta_1m_{j-1}+(1-\beta_1)g_j,\qquad v_j=\beta_2v_{j-1}+(1-\beta_2)g_j\odot g_j,$$
$$\hat m_j=\frac{m_j}{1-\beta_1^j},\qquad \hat v_j=\frac{v_j}{1-\beta_2^j},\qquad
\theta_j=\theta_{j-1}-\eta\,\hat m_j\oslash\bigl(\sqrt{\hat v_j}+\epsilon_{\mathrm{opt}}\bigr).$$

Hiệu chỉnh lệch quan trọng ở các bước đầu vì hai moment khởi tạo bằng không. Adam
kết hợp động lượng (làm trơn hướng tìm kiếm) với chuẩn hóa thích nghi kiểu RMS,
thường giúp tăng tốc huấn luyện trong deep RL.

**So sánh và lựa chọn.**

| Phương pháp | Trạng thái phụ | Điều cần tinh chỉnh |
|---|---|---|
| SGD | không | tốc độ học và lịch giảm |
| RMSprop | $v_j$ | $\eta,\rho,\epsilon_{\mathrm{opt}}$ |
| Adam | $m_j,v_j$ | $\eta,\beta_1,\beta_2,\epsilon_{\mathrm{opt}}$ |

So sánh cần đồng thời: return đánh giá, độ ổn định qua nhiều lần chạy độc lập,
loss huấn luyện và chi phí tính toán. **Không có lựa chọn thắng tuyệt đối**; một
lịch bước phù hợp có thể quan trọng hơn tên optimizer.

**Giới hạn.** Một bộ tối ưu tốt hơn không tự giải quyết bất ổn cốt lõi của
Q-learning với xấp xỉ hàm: nó không sửa cấu trúc bootstrap, tính khác chính sách
hay xấp xỉ hàm. Replay memory và mạng mục tiêu vẫn là thiết yếu. Công thức Adam
không tạo bảo đảm hội tụ cho DQN.

**Kiểm tra nhanh.** Optimizer thích nghi có sửa mục tiêu Bellman không? — Không;
nó chỉ chuẩn hóa gradient theo từng tọa độ, đích và dữ liệu không đổi.

---

## Kiểm tra tổng hợp và đọc thêm

<!-- note-topic-id: lec-08-topic-15 -->
### Kiểm tra tổng hợp, thảo luận và đọc thêm

**Kiểm tra tổng hợp (bốn câu).**

1. Replay giảm cơ chế nào và để lại giới hạn nào? — Giảm tương quan ngắn hạn và
   tăng tái sử dụng dữ liệu; không tạo i.i.d., không bảo đảm hội tụ.
2. Mạng mục tiêu làm chậm đại lượng nào? — Sự thay đổi của đích bootstrap giữa
   các lần đồng bộ; đích vẫn nhảy tại mốc $\theta^-\leftarrow\theta$.
3. Khi nào cắt ngắn vẫn cần bootstrap? — Khi nhiệm vụ tiếp diễn và việc dừng chỉ
   do giới hạn thu thập ($U=1$, $Z=0$).
4. Optimizer thích nghi có sửa bộ ba nguy hiểm không? — Không; nó chỉ chuẩn hóa
   bước cập nhật, không đụng vào xấp xỉ hàm, bootstrap hay dữ liệu khác chính sách.

**Ba bài thảo luận (từ nguồn).**

1. Vì sao experience replay làm cho cập nhật mini-batch đáng tin cậy hơn?
2. Vì sao các bộ tối ưu thích nghi có thể giúp DQN dù chúng không sửa trực tiếp
   mục tiêu Bellman?
3. Tìm các phương pháp để tăng tính khám phá trong DQN.

**Đọc thêm / thực hành.** Đọc giả mã "Deep Q-learning with experience replay"
trong nguồn (tr. 20–21) và đối chiếu từng dòng với vòng DQN ở topic-10: điểm nào
giả mã nguồn đã có (replay dung lượng $N$, hai mạng $\theta,\theta^-$, đích có
mặt nạ terminal, đồng bộ mỗi $C$ bước), điểm nào ghi chú này bổ sung (hai cờ
$Z,U$, làm nóng $N_{\mathrm{start}}$, nhịp $F$, autoreset, dừng gradient). Khi
thực hành trên Atari, chỉ cần giữ hợp đồng tối thiểu: bốn khung → CNN → vector
$|\mathcal A|$ giá trị hành động.

---

## Ba bài tập (30 phút, 10 phút mỗi bài)

::: exercise Bài tập 1 — Tính đích, mất mát và gradient

Cho $b=2$, $\gamma=0{,}9$:

| $i$ | $R_i$ | $Z_i$ | $\max_{a'}Q_{\theta^-}(O'_i,a')$ | $q_i=Q_\theta(O_i,A_i)$ |
|---|---|---|---|---|
| 1 | 1 | 0 | 4 | 3,1 |
| 2 | −2 | 1 | 100 | −1,5 |

Tính $y_i$, $\delta_i=y_i-q_i$, MSE $L_B$ và $\partial L/\partial(q_1,q_2)$.
Cho biết mẫu nào làm tăng $q$ dưới một bước hạ gradient nhỏ.
:::

::: hint
Áp dụng mặt nạ $(1-Z_i)$ trước khi tính sai số. Số 100 ở mẫu 2 là mồi
kiểm tra: chuyển tiếp đã kết thúc nên nó không đi vào đích. Với MSE trung bình
trên hai mẫu, đạo hàm theo $q_i$ là $\tfrac{2}{b}(q_i-y_i)$.
:::

::: solution

- $y_1 = 1 + 0{,}9\cdot(1-0)\cdot 4 = 4{,}6$; $y_2 = -2 + 0{,}9\cdot(1-1)\cdot 100 = -2$.
- $\delta_1 = 4{,}6-3{,}1 = 1{,}5$; $\delta_2 = -2-(-1{,}5) = -0{,}5$.
- $L_B = \tfrac12(1{,}5^2 + 0{,}5^2) = \tfrac12(2{,}25+0{,}25) = 1{,}25$.
- $\partial L/\partial q_1 = 2\cdot\tfrac12\cdot(3{,}1-4{,}6) = -1{,}5$;
  $\partial L/\partial q_2 = 2\cdot\tfrac12\cdot(-1{,}5+2) = 0{,}5$.
- Mẫu 1 có gradient theo $q_1$ âm, nên phép trừ gradient làm $q_1$ tăng; mẫu 2
  có gradient dương nên $q_2$ giảm.
:::

::: exercise Bài tập 2 — Sửa bốn lỗi trong giả mã

Đoạn giả mã sau chứa bốn lỗi:

```
done = terminated or truncated
next_o = obs_after_step        # API có thể đã tự reset
y = r + gamma * (1 - done) * q_target(next_o).max()
loss = ((y - q_online(o)[a]) ** 2).mean()
```

Sửa: (i) quan sát kế tiếp, (ii) mặt nạ theo kết thúc MDP, (iii) đường gradient
(dừng gradient ở đích), (iv) phép chọn hành động theo lô.
:::

::: hint
Quan sát sau bước có thể thuộc lượt mới nếu API tự đặt lại — cần quan sát
cuối của chuyển tiếp. Biến done gộp không được dùng trong loss; cắt ngắn ngoài mô
hình vẫn bootstrap. Đích phải tính trong no-grad. Chọn một hành động đã lưu trên
mỗi hàng bằng gather, không lập chỉ mục vô hướng.
:::

::: solution

```
final_o = info.get("final_observation")
next_o = obs_after_step if final_o is None else final_o
z = terminated.float()          # kết thúc của MDP đang mô hình hóa
with no_grad():
    y = r + gamma * (1 - z) * q_target(next_o).max(dim=1).values
q = q_online(o).gather(1, a[:, None]).squeeze(1)
loss = ((y - q) ** 2).mean()
```

Giải thích: (i) dùng `final_observation` làm quan sát cuối của chuyển tiếp; (ii)
mặt nạ chỉ theo `terminated`, biến done gộp không dùng trong loss; (iii) `no_grad`
dừng gradient qua mạng mục tiêu; (iv) `gather` chọn một phần tử mỗi hàng rồi
`squeeze` về $[b]$. Giả định `final_observation` là quan sát cuối đúng và cờ
`terminated` của API trùng kết thúc MDP đang mô hình hóa; cắt ngắn ngoài mô hình
vẫn bootstrap.
:::

::: exercise Bài tập 3 — Thiết kế thí nghiệm loại bỏ

Thiết kế thí nghiệm loại bỏ (ablation) công bằng để đo tác động của replay và của
mạng mục tiêu: dự đoán trước tác động của từng nhánh lên tự tương quan của batch,
độ đa dạng mẫu, tốc độ đổi của đích, TD error, dao động tham số và đường return.
Nêu cách tổng hợp nhiều lần chạy độc lập. Không yêu cầu viết chương trình.
:::

::: hint
Công bằng nghĩa là mọi nhánh dùng cùng kiến trúc, ngân sách, bộ tối ưu,
lịch khám phá và cùng tập seed (hoặc ghép cặp seed giữa các nhánh). Chọn chỉ số đo
trước khi chạy; đừng chỉ nhìn một lần chạy.
:::

::: solution
Thiết kế: ba nhánh — đầy đủ, bỏ replay (học trên chuyển tiếp liên
tiếp), bỏ mạng mục tiêu (bootstrap từ mạng online); định trước cùng số lần chạy
cho mỗi nhánh và cùng ngân sách bước. Giữ nguyên mọi thành phần khác. Chỉ số đo:
return đánh giá theo chính sách tham lam riêng, TD error, chuẩn gradient, độ phân
tán giữa các lần chạy, và (cho replay) tự tương quan theo độ trễ của mẫu trong
batch. Tổng hợp: dùng cùng tập seed hoặc ghép cặp giữa các nhánh để giảm nhiễu so
sánh; báo thống kê trung tâm và độ phân tán (không chỉ trung bình). Kết luận mong
đợi theo lý thuyết của bài: bỏ replay làm tăng tương quan ngắn hạn; bỏ mạng mục
tiêu làm đích đổi sau mỗi bước tối ưu; cả hai nhánh không thay đổi việc bộ ba
nguy hiểm vẫn tồn tại — không nhánh cho bảo đảm hội tụ.
:::

---

## Kết luận

Hợp đồng của một bản DQN đúng gồm sáu điểm kiểm tra:

1. **Biểu diễn:** quan sát vào, vector giá trị Q cho tập hành động rời rạc ra;
   $Q_\theta$ nhận gradient, $Q_{\theta^-}$ tạo đích.
2. **Chuyển tiếp:** chỉ số nhất quán; phân biệt kết thúc MDP $Z$ với cắt ngắn
   ngoài mô hình $U$; lưu quan sát cuối của chuyển tiếp khi môi trường tự reset.
3. **Đích:** có mặt nạ $(1-Z)$, mạng mục tiêu và dừng gradient;
   $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$.
4. **Dữ liệu:** replay giảm tương quan và tái sử dụng dữ liệu nhưng không tạo
   i.i.d. và không bảo đảm hội tụ.
5. **Đồng bộ:** giữ $\theta^-$ cố định rồi sao chép $\theta^-\leftarrow\theta$ sau
   bước tối ưu theo chu kỳ $C$; hai đồng hồ $t$ và $k_{\mathrm{opt}}$ tách biệt.
6. **Kết luận:** đánh giá thực nghiệm qua nhiều lần chạy độc lập; không suy ra hội
   tụ tổng quát. Bộ ba nguy hiểm — xấp xỉ hàm, bootstrap, dữ liệu khác chính sách —
   vẫn còn trong DQN; replay và mạng mục tiêu giảm nhẹ hai biểu hiện trực tiếp
   (tương quan, mục tiêu di động) nhưng không loại bỏ nguyên nhân cấu trúc.

Mỗi mục trên chặn một lỗi có thể làm thuật toán sai nghĩa hoặc làm kết luận vượt quá
bằng chứng; dùng danh sách này như kiểm tra cuối trước khi đọc hoặc viết một cài
đặt DQN.
