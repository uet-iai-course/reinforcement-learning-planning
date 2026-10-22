# Bài 08 — Deep Q-Learning

Trong chương này, chúng ta thay hàm tuyến tính $\hat q(s,a,w)=x(s,a)^\top w$ của Bài 07 bằng một mạng nơ-ron nhận quan sát và trả về một giá trị cho mỗi hành động trong tập hữu hạn, rồi xây dựng thuật toán Deep Q-Network (DQN) từ bốn thành phần: đích hồi quy có mặt nạ kết thúc, bộ nhớ phát lại (experience replay), hàm mất mát với dừng gradient và mạng mục tiêu (target network). Bộ nhớ phát lại và mạng mục tiêu giảm bất ổn khi huấn luyện, nhưng DQN vẫn có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, tức đủ ba yếu tố của bộ ba bất ổn (deadly triad) ở Bài 07, nên thuật toán không có bảo đảm hội tụ tổng quát.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đọc vector giá trị hành động $\mathbf q_\theta(o)\in\mathbb R^{\lvert\mathcal A\rvert}$ do mạng trả về, chọn giá trị $Q_\theta(o,a)$ của hành động đã thực hiện, và tính đích hồi quy của một mẫu chuyển; phân biệt mẫu kết thúc (đích không chứa phần bootstrap) với mẫu bị cắt ngắn (đích vẫn chứa phần bootstrap).
2. Nêu tác dụng và giới hạn của bộ nhớ phát lại: giảm tương quan giữa các mẫu liền nhau nhưng không tạo dữ liệu độc lập cùng phân phối theo một phân phối cố định; chỉ ra hai nguồn dữ liệu khác chính sách và tính xác suất hai mẫu liền nhau cùng vào một mini-batch.
3. Tính hàm mất mát và gradient của nó theo các dự đoán trên một mini-batch, chỉ ra phần nào không nhận gradient, và truy dấu một vòng của thuật toán DQN với hai bộ đếm $t$ và $k_{\mathrm{opt}}$.
4. Viết hạ gradient ngẫu nhiên (SGD), RMSprop và Adam theo từng tọa độ; nêu những gì lựa chọn bộ tối ưu không thay đổi: công thức đích, cách thu thập dữ liệu và lớp hàm.
5. Tính độ thay đổi của đích một mẫu khi đồng bộ mạng mục tiêu; nêu vì sao DQN không có bảo đảm hội tụ tổng quát.
6. Giải một bước DQN trên một mini-batch có cả mẫu kết thúc lẫn mẫu bị cắt ngắn, nêu kết quả và giả thiết đã dùng ở mỗi bước tính.

<!-- note-topic-id: lec-08-topic-13 -->
## Kiến thức tiên quyết

Kết quả của bài trước được dẫn theo mục của ghi chú bài đó, dạng "ghi chú Bài 06, Mục 4", và phát biểu lại dưới đây.

- **Q-learning dạng bảng** (ghi chú Bài 06, Mục 4, Định nghĩa 06.15, Thuật toán 06.16). Trên một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn, sau khi thực hiện $A_t$ tại $S_t$ và nhận phần thưởng $R_{t+1}$, trạng thái $S_{t+1}$, Q-learning cập nhật đúng một ô của bảng:
  $$
  \begin{aligned}
  &Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)\\
  &\qquad\ +\alpha_t\,\delta_t,\\
  &\delta_t=R_{t+1}+\gamma\max_{a'}Q_t(S_{t+1},a')\\
  &\qquad\ -Q_t(S_t,A_t),
  \end{aligned}
  $$
  các ô khác giữ nguyên, và $Q(s,\cdot)=0$ khi $s$ là trạng thái kết thúc. Ở đây $\alpha_t\in(0,1]$ là bước học của cặp $(S_t,A_t)$ tại lần cập nhật này và $\gamma\in[0,1)$ là hệ số chiết khấu. $\delta_t$ là sai số TD, và $R_{t+1}+\gamma\max_{a'}Q_t(S_{t+1},a')$ là mục tiêu cập nhật; mục tiêu này chứa ước lượng hiện tại $Q_t$ nên là mục tiêu bootstrap (bootstrap target).
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
| $\odot$, $\oslash$ | nhân, chia theo từng tọa độ | phép toán trên $\mathbb R^d$ |
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
| `lec-08-topic-08` | Phép chọn theo hành động và dừng gradient | tr. 16, 20–22, 33–34 | Đồ thị tính; $\operatorname{sg}$, gather; gradient chỉ qua đường dự đoán | Vào: topic-09 → Ra: gradient đúng trong cài đặt |
| `lec-08-topic-09` | Hàm mất mát trên mini-batch | tr. 16, 20–22, 34 | MSE với đích là hằng, gradient, không lồi theo $\theta$ | Vào: topic-07 → Ra: hàm vô hướng và gradient cho topic-08 |
| `lec-08-topic-10` | Vòng huấn luyện DQN: hai bộ đếm $t$ và $k_{\mathrm{opt}}$ | tr. 18–22 | Giả mã đầy đủ | Vào: topic-05–09 → Ra: thuật toán hoàn chỉnh |
| `lec-08-topic-11` | Kích thước tensor của mini-batch Atari | tr. 14–22, 35 | Kích thước và kiểu tensor | Vào: topic-10 → Ra: kiểm tra cài đặt |
| `lec-08-topic-12` | Bất ổn và phạm vi bảo đảm của DQN | tr. 12–13, 29–34 | Hai nguồn bất ổn và hai cơ chế giảm; độ thay đổi của đích tại mốc đồng bộ; bộ ba bất ổn trong DQN | Vào: topic-10, topic-14 → Ra: kết luận có điều kiện cho phần 7 |

### Nhóm bổ sung

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-14` | Vai trò của bộ tối ưu và ba quy tắc cập nhật | tr. 22–28 | Ba quy tắc cập nhật và giới hạn | Vào: topic-10 → Ra: lựa chọn bộ tối ưu có căn cứ |

### Nhóm đọc thêm/thực hành

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-15` | Tổng kết và chuyển tiếp: kết quả và giả thiết, so sánh ba phương pháp, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, đọc thêm, tóm tắt chương | tr. 12–13, 20–21, 29–36 | Tổng kết | Vào: topic-01 đến topic-14 → Ra: câu trả lời có điều kiện cho vấn đề trung tâm; Bài 09 |

### Bảy phần của chương

Chúng ta đi qua bảy phần sau.

1. Mở đầu: kiến thức tiên quyết, ký hiệu, mục tiêu và bài toán trung tâm (`lec-08-topic-13`, `lec-08-topic-17`).
2. Mạng giá trị hành động và đích hồi quy: giới hạn của bảng, đầu vào bốn khung Atari, mạng giá trị hành động, mạng mục tiêu, đích có mặt nạ kết thúc, kết thúc và cắt ngắn (`lec-08-topic-01`, `lec-08-topic-16`, `lec-08-topic-02` đến `lec-08-topic-05`).
3. Bộ nhớ phát lại: tương quan giữa các mẫu chuyển liên tiếp, cơ chế lưu và lấy mẫu đều, dữ liệu khác chính sách, giới hạn (`lec-08-topic-18`, `lec-08-topic-06`, `lec-08-topic-19`, `lec-08-topic-07`).
4. Hàm mất mát và thuật toán DQN: hàm mất mát trên mini-batch, dừng gradient, vòng huấn luyện, kích thước tensor (`lec-08-topic-09`, `lec-08-topic-08`, `lec-08-topic-10`, `lec-08-topic-11`).
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

Bài giảng gốc (trang 9 và 11) còn nêu hai cận độ phức tạp mẫu: $\tilde O\bigl(\lvert\mathcal S\rvert\lvert\mathcal A\rvert/((1-\gamma)^4\varepsilon_{\mathrm{acc}}^2)\bigr)$ mẫu để Q-learning dạng bảng đạt chính sách $\varepsilon_{\mathrm{acc}}$-tối ưu, và $\tilde O\bigl(d/((1-\gamma)^3\varepsilon_{\mathrm{acc}}^2)\bigr)$ cho xấp xỉ hàm với $d$ đặc trưng; ở đây $\varepsilon_{\mathrm{acc}}$ là sai số cho phép của chính sách, khác $\epsilon_{\mathrm{exp}}$. Sai số đo bằng $v_\pi(s)\ge v_*(s)-\varepsilon_{\mathrm{acc}}$ với mọi $s$ (trang 8), nhưng nguồn không nêu mô hình lấy mẫu (bộ sinh độc lập hay dọc một quỹ đạo) và xác suất thành công, chỉ nêu định tính điều kiện khám phá và bao phủ; cận thứ hai không gắn với một thuật toán cụ thể. Vì vậy chúng ta không dùng hai cận như định lý. Hai ý vẫn dùng ở phần sau: số ô của bảng tăng theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$, và xấp xỉ hàm chỉ có bảo đảm dưới giả thiết mạnh; bài giảng gốc (trang 11) nêu tính biểu diễn được ($q_*$ nằm trong lớp hàm), bao phủ đủ và độ ổn định của cập nhật.


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

Trong ví dụ một tham số, mạng mục tiêu không đưa $\theta$ tới $10$ nhanh hơn. Gọi $r=0{,}5^C$. Một chu kỳ $C$ bước đưa $\theta^-$ thành $(1+0{,}9\,\theta^-)(1-r)+\theta^-r$, nên $\theta^-_{\mathrm{new}}-10=(0{,}9+0{,}1\,r)\,(\theta^--10)$, với $\theta^-_{\mathrm{new}}$ là tham số mạng mục tiêu sau chu kỳ. Với $C=3$, khoảng cách tới $10$ nhân với $0{,}9125$ sau mỗi ba bước, trong khi không có mạng mục tiêu, ba bước nhân khoảng cách với $0{,}95^3\approx0{,}857$. Giữa hai lần đồng bộ, mỗi bước là hồi quy về nhãn cố định, nên vòng phản hồi giữa dự đoán và đích chỉ khép lại tại các mốc đồng bộ; đó là tác dụng của mạng mục tiêu; lợi ích ổn định với mạng lớn là kết quả thực nghiệm. Ở phần 6 (Ví dụ 08.24), chúng ta xét một ví dụ hai trạng thái dùng chung tham số, trong đó mạng mục tiêu làm chậm nhưng không ngăn được phân kỳ. Bài giảng gốc (trang 33) nêu mạng mục tiêu như cách làm mục tiêu thay đổi chậm hơn để quá trình tối ưu ổn định hơn; đó là tác dụng thực nghiệm, không phải bảo đảm hội tụ.

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

Đích gồm hai phần. $R_{t+1}$ là phần thưởng đã quan sát; $\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$ là ước lượng của phần lợi tức còn lại, đọc trên vector $\mathbf q_{\theta^-}(O_{t+1})$ sau một lần tính của mạng mục tiêu. Thừa số $(1-Z_{t+1})$, gọi là mặt nạ kết thúc, bằng $0$ khi lượt kết thúc, nên khi đó $y_t=R_{t+1}$; đây đúng là quy ước $Q(s,\cdot)=0$ của dạng bảng, viết cho một hàm không có ô riêng cho trạng thái kết thúc. $q_t$ phụ thuộc $\theta$, còn $y_t$ chỉ phụ thuộc dữ liệu và $\theta^-$. Với $\theta^-$ cố định, $y_t$ là một số cố định gắn với mẫu chuyển, và $\delta_t>0$ nghĩa là dự đoán cần tăng.

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

Đến đây mỗi mẫu chuyển đã có một đích hồi quy $y_t$. Bước cập nhật $\theta$ lấy trung bình gradient trên một mini-batch $b$ mẫu, như hạ gradient ngẫu nhiên (stochastic gradient descent, SGD) trong học có giám sát. Lập luận quen thuộc cho SGD dùng giả thiết các mẫu trong mini-batch độc lập và cùng phân phối (i.i.d.): khi đó trung bình của $b$ gradient mẫu có phương sai bằng $1/b$ phương sai của một gradient mẫu. Nếu tác tử cập nhật ngay trên các mẫu chuyển vừa thu thập theo thứ tự thời gian, giả thiết này không còn đúng.

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
Nếu bốn mẫu độc lập, $\operatorname{Var}\bar g=\sigma^2/4=0{,}25\,\sigma^2$. Cỡ mẫu hiệu dụng (effective sample size), tức số mẫu độc lập cho cùng phương sai, là $\sigma^2/\operatorname{Var}\bar g=\sigma^2/(0{,}881\,\sigma^2)\approx1{,}1$.

**Diễn giải.** Với tương quan này, mini-batch bốn mẫu liền nhau giảm phương sai gần như không hơn một mẫu. Muốn trung bình gradient có phương sai nhỏ, các mẫu trong mini-batch phải đến từ những thời điểm xa nhau.
:::

![Hai hàng, mỗi hàng là 20 bước thời gian của cùng một quỹ đạo, vẽ bằng chấm tròn rỗng. Hàng trên, liên tiếp: bốn mẫu ở t bằng 17 đến 20 đánh dấu bằng hình vuông đặc, ngoặc chung ghi cùng đoạn quỹ đạo, cùng theta. Hàng dưới, lấy rải: bốn mẫu ở t bằng 3, 8, 12, 19 đánh dấu bằng tam giác đặc.](img/lec-08/correlated-minibatch.svg)

Hình so sánh hai cách chọn bốn mẫu từ hai mươi bước của cùng một quỹ đạo. Hàng trên chọn bốn bước cuối $t=17,\dots,20$ (hình vuông đặc): chúng thuộc cùng một đoạn quỹ đạo và cùng một phiên bản $\theta$. Hàng dưới chọn bốn bước rải trên toàn quỹ đạo, $t=3,8,12,19$ (tam giác đặc): tương quan giữa các mẫu nhỏ hơn vì chúng cách nhau xa hơn.

Tương quan không nhất thiết làm gradient trung bình bị chệch. Với tương quan dương, hệ quả là phương sai lớn hơn, và hướng cập nhật đi theo vùng quan sát vừa thăm: qua nhiều bước liên tiếp, gradient dao động theo đoạn quỹ đạo gần nhất thay vì theo toàn bộ dữ liệu. Ngay cả khi lấy mẫu rải như hàng dưới, các mẫu vẫn không độc lập cùng phân phối: chúng cùng thuộc một quỹ đạo, và phân phối của dữ liệu đổi khi chính sách hành vi đổi theo $\theta$.

**Trong thực hành.** Cỡ mẫu hiệu dụng phụ thuộc mức tương quan, và mức này đổi theo môi trường và chính sách; Ví dụ 08.9 chỉ minh họa cơ chế; mức tương quan thật cần đo trên dữ liệu của từng môi trường.

Chúng ta cần một cách chọn mẫu cho mini-batch không phụ thuộc thứ tự thu thập. Ở mục tiếp theo, chúng ta lưu các mẫu chuyển vào một bộ nhớ và lấy mẫu đều từ đó.

<!-- note-topic-id: lec-08-topic-06 -->
### Bộ nhớ phát lại (experience replay)

Theo Ví dụ 08.9, bốn mẫu chuyển liền nhau, với tương quan $0{,}9^k$ giữa hai mẫu cách nhau $k$ bước, giảm phương sai của gradient trung bình như khoảng $1{,}1$ mẫu độc lập. Muốn mini-batch gồm các mẫu ở những thời điểm xa nhau, chúng ta phải giữ lại các mẫu chuyển đã thu thập thay vì dùng mỗi mẫu một lần, và phải chọn mẫu cho mini-batch không theo thứ tự thu thập. Bộ nhớ của máy tính có hạn, nên còn phải quy định mẫu nào bị bỏ khi bộ nhớ đầy. Bài giảng gốc (trang 19, 32) nêu hai việc đầu: lưu kinh nghiệm của tác tử, rồi lấy ngẫu nhiên các mini-batch từ đó. Mnih và cộng sự (2015, mục Methods) giải quyết việc thứ ba: bộ nhớ chỉ giữ $N$ mẫu chuyển gần nhất, và mini-batch được lấy đều từ các mẫu đang lưu.

::: definition Định nghĩa 08.7 (Bộ nhớ phát lại)
Cho số nguyên dương $N$, gọi là dung lượng, và cỡ mini-batch $b\in\mathbb N_+$. Bộ nhớ phát lại (experience replay) là một bộ đệm vòng (ring buffer) $\mathcal D$ gồm $N$ vị trí đánh số $1,\dots,N$ và một con trỏ ghi; mỗi vị trí chứa nhiều nhất một mẫu chuyển sáu thành phần $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ của Định nghĩa 08.6. Đánh số các mẫu chuyển $1,2,\dots$ theo thứ tự thu thập. Bộ nhớ hoạt động theo hai quy tắc.

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

**Trong thực hành.** Bộ nhớ thường được cài bằng các mảng cấp phát sẵn $N$ hàng cho từng thành phần của mẫu chuyển, một con trỏ ghi và một bộ đếm $\lvert\mathcal D\rvert$; rút một mini-batch là sinh $b$ chỉ số đều trong $\{1,\dots,\lvert\mathcal D\rvert\}$. Với đầu vào Atari của Ví dụ 08.2, mỗi mẫu chứa hai chồng bốn khung $84\times84$, tức $2\cdot28\,224=56\,448$ số; nếu mỗi điểm ảnh là một byte, $N=10^6$ mẫu chiếm khoảng $56$ GB. Hai chồng $O_t$, $O_{t+1}$ của một mẫu dùng chung ba khung, và $O_{t+1}$ của mẫu $k$ trùng $O_t$ của mẫu $k+1$, nên lưu mỗi khung một lần ($84\cdot84=7\,056$ byte) rồi ghép chồng khi rút giảm con số này khoảng tám lần. Bộ nhớ chỉ đổi cách chọn mẫu: đích của một mẫu được rút vẫn tính theo Định nghĩa 08.4 với $\theta^-$ tại lúc rút, không phải $\theta^-$ tại lúc mẫu được thu thập (bài giảng gốc, trang 20).

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

Mệnh đề sau chuyển lý do của dạng bảng (Sutton và Barto, 2018, §6.5, §6.6) sang đích hồi quy của DQN.

::: proposition Mệnh đề 08.8 (Đích một bước không phụ thuộc hành vi đã sinh mẫu)
**Giả thiết.** Quan sát $O_t$ đủ Markov (Nhận xét 08.2), và động lực của môi trường, tức phân phối của $(R_{t+1},O_{t+1},Z_{t+1})$ khi biết $(O_t,A_t)$, không đổi theo thời gian. Tham số $\theta^-$ cố định. Mẫu $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ được rút đều từ $\mathcal D$ (Định nghĩa 08.7), trong đó mỗi mẫu được ghi bởi một hành vi chọn $A_t$ chỉ dựa trên lịch sử tới bước $t$ (quan sát, hành động, phần thưởng, cờ, kể cả tham số $\theta_t$ học từ lịch sử đó) và một nguồn ngẫu nhiên độc lập với môi trường.

**Kết luận.** $\mathbb E[y_i\mid O_i,A_i]=(\mathcal TQ_{\theta^-})(O_i,A_i)$ hầu chắc chắn, dù mẫu do phiên bản hành vi nào sinh ra (với quan sát rời rạc: với mọi $(o,a)$ có xác suất dương), trong đó
$$
(\mathcal TQ_{\theta^-})(o,a)=\mathbb E\Bigl[R_{t+1}+\gamma(1-Z_{t+1})\max_{a'}Q_{\theta^-}(O_{t+1},a')\Bigm|O_t=o,A_t=a\Bigr].
$$

**Điều kiện áp dụng.** Đích một bước với phép cực đại tính trọn tại $O'_i$.

**Phạm vi.** Mệnh đề chỉ nói về kỳ vọng có điều kiện của đích khi biết cặp $(O_i,A_i)$. Phân phối của chính cặp $(O_i,A_i)$ trong $\mathcal D$ vẫn do các hành vi đã sinh dữ liệu quyết định. Đẳng thức coi $\theta^-$ là hằng cho trước; trong DQN, $\theta^-$ học từ chính dữ liệu của $\mathcal D$, nên với mẫu đã góp vào $\theta^-$ đẳng thức chỉ đúng gần đúng.
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
**Dữ kiện.** $\lvert\mathcal A\rvert=4$, $\epsilon_{\mathrm{exp}}=0{,}1$, $\gamma=0{,}9$. Tại quan sát $o$, $\mathbf q_\theta(o)=(0{,}8;\,2{,}5;\,-0{,}3;\,1{,}9)$ như Ví dụ 08.3, nên hành động tham lam là $a_2$; giả sử $Q_{\theta^-}(o,\cdot)$ cũng đạt cực đại tại $a_2$. Hành vi chọn $a_4$ và nhận mẫu chuyển có $R_i=1$, $Z_i=0$, $\max_{a'}Q_{\theta^-}(O'_i,a')=4$.

**Tính.** Đích $y_i=1+0{,}9\cdot4=4{,}6$, một mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(o,a_4)$ theo Mệnh đề 08.8. Xác suất hành vi chọn $a_4$ là $0{,}1/4=0{,}025$, xác suất chính sách tham lam chọn $a_4$ là $0$. Nếu nhân sai số của mẫu với tỉ số $\pi(a_4\mid o)/\mu(a_4\mid o)=0/0{,}025=0$, với $\mu$ là chính sách hành vi (ký hiệu $b$ của Bài 06), mẫu bị xóa khỏi cập nhật.

**Diễn giải.** Hiệu chỉnh theo tỉ số tại $A_i$ làm mọi mẫu của hành động không tham lam có trọng số $0$, nên $Q_\theta(o,a_4)$ không bao giờ học từ dữ liệu, dù đích $4{,}6$ là mẫu đúng của giá trị cần ước lượng.
:::

**Trong thực hành.** Hàm mất mát DQN cơ bản không chứa tỉ số lấy mẫu quan trọng, và Mệnh đề 08.8 giải thích vì sao điều này đúng với đích một bước. Khi đích dùng nhiều bước, như đích $n$ bước, các hành động $A_{t+1},\dots,A_{t+n-1}$ đều lấy từ hành vi đã ghi mẫu, và đích chỉ đánh giá chính sách đích khi được hiệu chỉnh bằng tích các tỉ số lấy mẫu quan trọng (Sutton và Barto, 2018, §7.3). Hành vi vẫn quyết định tần suất của từng cặp $(O_i,A_i)$ trong mini-batch, tức trọng số của từng cặp khi khớp $Q_\theta$. Với bảng, mỗi ô được khớp riêng nên trọng số này không đổi giá trị đích của ô; với xấp xỉ hàm, các cặp tranh nhau tham số dùng chung, và trọng số theo phân phối của $\mathcal D$ là thành phần học khác chính sách trong bộ ba bất ổn của Bài 07.

**Kiểm tra nhanh.** Một mẫu trong $\mathcal D$ được ghi bởi hành vi theo $\theta$ của $2{,}5\cdot10^5$ bước tối ưu trước. Khi mẫu được rút, đích của nó tính bằng tham số nào, và có cần hiệu chỉnh cho phiên bản hành vi cũ không? Đích tính bằng $\theta^-$ tại lúc rút. Theo Mệnh đề 08.8, khi $O_i$ đủ Markov và động lực không đổi, phiên bản hành vi cũ chỉ quyết định cặp $(O_i,A_i)$ được ghi, không đổi kỳ vọng của đích, nên không cần hiệu chỉnh.

Chúng ta đã có hai kết quả về bộ nhớ phát lại: mini-batch rút đều từ $N$ mẫu gần nhất, và đích một bước của mỗi mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_i,A_i)$ bất kể phiên bản hành vi đã sinh mẫu. Phân phối của các cặp $(O_i,A_i)$ trong mini-batch thì vẫn do các hành vi cũ và hiện tại quyết định, và các mẫu vẫn cùng thuộc một số quỹ đạo. Ở mục tiếp theo, chúng ta nêu những điều bộ nhớ phát lại không bảo đảm.

<!-- note-topic-id: lec-08-topic-07 -->
### Giới hạn của bộ nhớ phát lại

Bộ nhớ phát lại cho mini-batch rút đều từ $N$ mẫu gần nhất (Định nghĩa 08.7), và đích một bước của mỗi mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_i,A_i)$ bất kể phiên bản hành vi đã sinh mẫu (Mệnh đề 08.8). Trước khi dùng mini-batch này để cập nhật $\theta$, chúng ta cần phát biểu đúng phạm vi của cơ chế: nó làm được gì, đo bằng số, và không bảo đảm điều gì.

Bộ nhớ phát lại làm được ba việc. Thứ nhất, nó giảm tương quan ngắn hạn: hai mẫu trong một mini-batch hiếm khi liền nhau, với xác suất $2/N$ khi rút không hoàn lại (Ví dụ 08.12 dưới đây). Thứ hai, nó tái sử dụng mẫu: với các giá trị của Mnih và cộng sự (2015, Extended Data Table 1), $N=10^6$, một bước tối ưu sau mỗi $4$ bước môi trường và $b=32$, một mẫu ở trong bộ nhớ trong $10^6$ bước môi trường, tức $2{,}5\cdot10^5$ bước tối ưu, mỗi bước rút $32$ lần, mỗi lần trúng mẫu đó với xác suất $10^{-6}$; số lần mẫu được dùng có kỳ vọng $2{,}5\cdot10^5\cdot32\cdot10^{-6}=8$. Thứ ba, mỗi mini-batch trộn nhiều đoạn quỹ đạo thay vì chỉ đoạn vừa thu thập, nên một bước cập nhật ít bị kéo theo vùng quan sát vừa thăm. Bài giảng gốc (trang 32) nêu các lợi ích tái sử dụng dữ liệu quá khứ và cải thiện hiệu quả mẫu. Tương quan theo thời gian giảm nhưng vẫn còn, vì xác suất $2/N$ của một cặp liền nhau luôn dương.

::: remark Nhận xét 08.9 (Ba điều bộ nhớ phát lại không bảo đảm)
Với bộ nhớ phát lại của Định nghĩa 08.7:

1. các mẫu trong một mini-batch không độc lập và cùng phân phối (i.i.d.) theo một phân phối cố định: khi biết $\mathcal D$, các lần rút có hoàn lại là i.i.d. theo phân phối thực nghiệm của $\mathcal D$, nhưng nội dung của $\mathcal D$ là các đoạn liền của những quỹ đạo do chính tác tử thu thập, xác suất hai lần rút trúng hai mẫu liền nhau là $2(N-1)/N^2\approx2/N>0$, và hai mẫu liên tiếp $k$, $k+1$ của một lượt dùng chung một quan sát, vì $O'$ của mẫu $k$ là $O$ của mẫu $k+1$;
2. phân phối của $\mathcal D$ không đứng yên: hành vi đổi cùng $\theta$ và bộ đệm thay mẫu cũ nhất bằng mẫu mới, nên phân phối của các cặp $(O_i,A_i)$ được rút trôi theo thời gian;
3. thuật toán dùng bộ nhớ phát lại không có bảo đảm hội tụ: xấp xỉ hàm, bootstrap và học khác chính sách vẫn cùng có mặt, tức bộ ba bất ổn của Bài 07 vẫn đủ ba yếu tố.
:::

Ba điều này có ba nguồn khác nhau. Điều thứ nhất đến từ việc mọi mẫu đều do một tác tử thu thập dọc các quỹ đạo. Lấy mẫu đều có hoàn lại làm các lần rút độc lập với nhau khi đã biết $\mathcal D$, nhưng không làm nội dung của $\mathcal D$ thành các mẫu độc lập của một phân phối cố định: nó chỉ làm hiếm các cặp liền nhau, không tạo ra các quỹ đạo độc lập. Như đã nêu ở mục tương quan, mẫu tương quan không nhất thiết làm gradient trung bình bị chệch; hệ quả chắc chắn hơn là phương sai lớn hơn so với cùng số mẫu độc lập. Điều thứ hai đến từ vòng lặp giữa dữ liệu và tham số: $\theta$ đổi thì hành vi đổi, hành vi đổi thì các mẫu mới ghi vào $\mathcal D$ đổi. Vì vậy lời giải hồi quy tốt nhất của Nhận xét 08.5, vốn giả sử các cặp $(O_t,A_t)$ lấy theo một phân phối cố định, chỉ áp dụng gần đúng khi phân phối của $\mathcal D$ đổi chậm so với số bước tối ưu giữa hai lần đồng bộ. Điều thứ ba đến từ chỗ bộ nhớ chỉ đổi cách chọn mẫu: nó không bỏ xấp xỉ hàm, không bỏ bootstrap, và theo Mệnh đề 08.8 nó còn thêm một nguồn dữ liệu khác chính sách. Mệnh đề 07.37 của Bài 07 cho một ví dụ tuyến tính hai trạng thái có đủ ba yếu tố mà tham số tăng không chặn; bộ nhớ phát lại không loại trừ ví dụ đó.

::: example Ví dụ 08.12 (Hai mẫu liền nhau trong một mini-batch)
**Dữ kiện.** $N=6$, bộ nhớ chứa mẫu $3,\dots,8$ như Ví dụ 08.10: các vị trí $1,\dots,6$ chứa mẫu $7,8,3,4,5,6$. Mini-batch có $b=2$ mẫu, rút không hoàn lại.

**Tính.** Rút không hoàn lại hai trong sáu mẫu cho $\binom62=15$ cặp, mỗi cặp có xác suất như nhau. Cặp mẫu $4$, mẫu $5$ có xác suất $1/15$. Hai mẫu liền nhau theo thứ tự thu thập là năm cặp $(3,4)$, $(4,5)$, $(5,6)$, $(6,7)$, $(7,8)$, nên xác suất rút được hai mẫu liền nhau là $5/15=1/3$. Cặp $(6,7)$ được tính dù mẫu $6$ ở vị trí $6$ và mẫu $7$ ở vị trí $1$: "liền nhau" xét theo thời gian, không theo vị trí trong bộ đệm.

**Tổng quát.** Với $N$ mẫu liên tiếp trong bộ nhớ, có $N-1$ cặp liền nhau trong $\binom N2$ cặp, nên xác suất là $(N-1)/\binom N2=2/N$; với $N=10^6$, xác suất bằng $2\cdot10^{-6}$.

**Diễn giải.** Dung lượng lớn làm hiếm cặp liền nhau, nhưng xác suất luôn dương, và các mẫu không liền nhau của cùng một lượt vẫn có thể tương quan.
:::

**Trong thực hành.** Dung lượng $N$ là một lựa chọn cân bằng. $N$ lớn làm hiếm cặp liền nhau và làm phân phối của $\mathcal D$ trôi chậm, nhưng giữ lâu các mẫu của những hành vi đã cũ. $N$ nhỏ giữ dữ liệu gần hành vi hiện tại, nhưng mini-batch gần với mini-batch liên tiếp hơn; ở cực $N=b$ của mục bộ nhớ phát lại, mọi mẫu trong mini-batch đều liền nhau. Mnih và cộng sự (2015, mục Methods) nêu thêm hai giới hạn của cách làm này: bộ đệm ghi đè theo thứ tự thời gian và lấy mẫu đều coi mọi mẫu chuyển quan trọng như nhau, không phân biệt mẫu mang nhiều thông tin. Hiệu quả của bộ nhớ phát lại trong DQN là kết quả thực nghiệm, không phải hệ quả của một định lý.

**Kiểm tra nhanh.** Hai mẫu liên tiếp $k$ và $k+1$ trong cùng một lượt có thành phần nào trùng nhau? Quan sát kế tiếp $O_{t+1}$ của mẫu $k$ chính là quan sát $O_t$ của mẫu $k+1$; khi mẫu $k$ là bước cuối của lượt thì không, vì mẫu $k+1$ bắt đầu từ quan sát đầu của lượt mới.

Ở phần 3, chúng ta đã có bốn kết quả. Mẫu chuyển liền nhau tương quan, nên mini-batch liên tiếp có cỡ mẫu hiệu dụng nhỏ: bốn mẫu với tương quan $0{,}9^k$ chỉ tương đương khoảng $1{,}1$ mẫu độc lập (Ví dụ 08.9). Bộ nhớ phát lại là bộ đệm vòng giữ $N$ mẫu gần nhất, mini-batch gồm $b$ lần rút đều (Định nghĩa 08.7), và mỗi mẫu được dùng lại trung bình khoảng $8$ lần với các giá trị của DQN gốc. Đích một bước của mỗi mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_i,A_i)$ dù mẫu do phiên bản hành vi nào sinh ra, nên không cần tỉ số lấy mẫu quan trọng (Mệnh đề 08.8). Cuối cùng, bộ nhớ không tạo mẫu độc lập cùng một phân phối cố định, không làm phân phối dữ liệu đứng yên, và không đem lại bảo đảm hội tụ (Nhận xét 08.9). Đến đây chúng ta có, cho mỗi bước tối ưu, một mini-batch $b$ mẫu với đích $y_i$ cố định giữa hai lần đồng bộ, nhưng chưa có cách biến mini-batch đó thành một bước cập nhật $\theta$. Ở phần 4, chúng ta viết hàm mất mát trên mini-batch, cho gradient chỉ đi qua dự đoán $Q_\theta(O_i,A_i)$ bằng phép dừng gradient, rồi ghép thu thập, lưu, rút mẫu, tối ưu và đồng bộ thành thuật toán DQN đầy đủ.

## 4. Hàm mất mát và thuật toán DQN

<!-- note-topic-id: lec-08-topic-09 -->
### Hàm mất mát trên mini-batch

Ở cuối phần 3, mỗi bước tối ưu có một mini-batch $b$ mẫu rút đều từ bộ nhớ phát lại, và mỗi mẫu có một dự đoán của mạng trực tuyến cùng một đích tính bằng mạng mục tiêu. Bộ tối ưu theo gradient cần một hàm vô hướng duy nhất của $\theta$ để lấy gradient. Chúng ta cần gộp $b$ cặp (dự đoán, đích) thành một hàm như vậy, sao cho cực tiểu của nó là lời giải của bài hồi quy dự đoán về đích.

Khi đã rút, các mẫu của mini-batch không còn mang thứ tự thời gian: mẫu thứ $i$ có thể được ghi trước hay sau mẫu thứ $i+1$ bất kỳ bao nhiêu bước. Vì vậy ta viết mẫu thứ $i$ là $(O_i,A_i,R_i,O'_i,Z_i,U_i)$: $R_i$ và $O'_i$ thay cho $R_{t+1}$ và $O_{t+1}$ của mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ được ghi tại bước $t$. Viết $R_{i+1}$ hay $O_{i+1}$ sẽ sai, vì mẫu $i+1$ của mini-batch không phải bước kế tiếp của mẫu $i$.

Mẫu chuyển của Ví dụ 08.7 có dự đoán $-1{,}5$ và đích $-2$; mẫu thứ nhất của ví dụ xuyên suốt, cùng số liệu với Ví dụ 08.8, có dự đoán $q_1=3{,}1$ và đích $4{,}6$. Ghép thành một mini-batch, $q=(3{,}1;\,-1{,}5)$ và $y=(4{,}6;\,-2)$, tức sai số $1{,}5$ và $-0{,}5$. Tổng sai số bằng $1$ che mất cả hai sai lệch vì chúng trái dấu; trung bình bình phương $\tfrac12(1{,}5^2+0{,}5^2)=1{,}25$ chỉ bằng $0$ khi mọi dự đoán trùng đích. Cực tiểu một đại lượng như vậy theo $\theta$ là hồi quy các $q_i$ về nhãn $y_i$.

::: definition Định nghĩa 08.10 (Hàm mất mát trên mini-batch)
Cho mini-batch $B=\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$ rút từ bộ nhớ phát lại $\mathcal D$ (Định nghĩa 08.7), mạng trực tuyến $Q_\theta$ với $\theta\in\mathbb R^d$, mạng mục tiêu $Q_{\theta^-}$ với $\theta^-$ cố định (Định nghĩa 08.3) và $\gamma\in[0,1)$. Với mỗi $i$, dự đoán và đích của mẫu $i$ là
$$
q_i=Q_\theta(O_i,A_i),\qquad y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a').
$$
Hàm mất mát (loss) sai số bình phương trung bình (mean squared error, MSE) trên $B$ là
$$
L_B(\theta)=\frac1b\sum_{i=1}^b\bigl(y_i-q_i\bigr)^2,
$$
trong đó mỗi $y_i$ là một hằng số theo $\theta$. Cờ $U_i$ không vào $L_B$.
:::

Ký hiệu $q_i$ chỉ dự đoán của mạng trên mẫu $i$; nó khác $q_*$, giá trị hành động tối ưu. Mỗi số hạng $y_i-q_i$ là sai số TD $\delta_i$ của mẫu $i$ theo Định nghĩa 08.4, nên $L_B$ là trung bình bình phương các sai số TD trên mini-batch. $L_B$ phụ thuộc $\theta$ chỉ qua các $q_i$. Lấy đạo hàm theo $\theta$, với $y_i$ là hằng:
$$
\begin{aligned}
\nabla_\theta L_B(\theta)&=\frac1b\sum_{i=1}^b2\,(y_i-q_i)\,\nabla_\theta(y_i-q_i)\\
&=\frac2b\sum_{i=1}^b(q_i-y_i)\,\nabla_\theta Q_\theta(O_i,A_i).
\end{aligned}
$$
Dòng thứ nhất là quy tắc dây chuyền cho hàm bình phương; dòng thứ hai dùng $\nabla_\theta y_i=0$ và $\nabla_\theta q_i=\nabla_\theta Q_\theta(O_i,A_i)$. Theo $q_i$, đạo hàm riêng là $\partial L_B/\partial q_i=\tfrac2b(q_i-y_i)$: một bước hạ gradient nhỏ làm $q_i$ giảm khi $q_i>y_i$ và tăng khi $q_i<y_i$, nếu chỉ xét riêng $q_i$. Khi các $q_i$ dùng chung $\theta$, một bước cũng đổi các $q_j$ khác, và dấu thay đổi của từng $q_i$ còn phụ thuộc tích $\nabla_\theta q_i^\top\nabla_\theta q_j$.

Định nghĩa dựa trên ba lựa chọn, và bỏ lựa chọn nào cũng đổi kết quả. Thứ nhất, đích được coi là hằng theo $\theta$. Với $\theta^-$ là một vector riêng, điều này đúng tự nhiên, vì $y_i$ chỉ phụ thuộc $\theta^-$ và dữ liệu. Bỏ điều kiện này, chẳng hạn khi đích tính bằng chính $\theta$ và gradient đi qua cả đích: trong ví dụ một tham số $Q_\theta=\theta$, $R=1$, $\gamma=0{,}9$, $\theta=0$ của Ví dụ 08.5, hàm $(1+0{,}9\,\theta-\theta)^2=(1-0{,}1\,\theta)^2$ có đạo hàm $-0{,}2$ tại $\theta=0$, còn khi coi đích $1$ là hằng, đạo hàm của $(1-\theta)^2$ là $-2$. Gradient đầy đủ qua đích cho một phương pháp khác, phương pháp gradient dư (residual gradient) của Sutton và Barto (2018, §11.5), với điểm dừng khác; DQN và Q-learning bán gradient của Bài 07 đều coi đích là hằng. Thứ hai, hệ số $1/b$ làm thang của $L_B$ không phụ thuộc cỡ mini-batch; nếu dùng tổng thay cho trung bình, gradient lớn lên theo $b$ và tốc độ học phải nhỏ đi tương ứng. Thứ ba, bình phương làm hàm hồi quy tốt nhất là kỳ vọng có điều kiện $\mathbb E[y_i\mid O_i,A_i]=(\mathcal TQ_{\theta^-})(O_i,A_i)$ (Nhận xét 08.5, Mệnh đề 08.8). Thay bình phương bằng giá trị tuyệt đối, hàm tốt nhất là trung vị có điều kiện của $y_i$, nói chung khác $(\mathcal TQ_{\theta^-})(O_i,A_i)$ khi phân phối của phần thưởng hoặc của quan sát kế tiếp không đối xứng.

::: remark Nhận xét 08.11 (Hàm mất mát không lồi theo tham số)
Với $\theta^-$ và mini-batch $B$ cố định, $L_B$ là hàm lồi của vector $(q_1,\dots,q_b)$. Nếu $Q_\theta(o,a)=x(o,a)^\top\theta$ tuyến tính theo $\theta$, thì $L_B$ là một hàm bậc hai lồi theo $\theta$. Với $Q_\theta$ phi tuyến theo $\theta$, chẳng hạn một mạng nhiều tầng, $L_B$ nói chung không lồi theo $\theta$, và một phương pháp theo gradient không bảo đảm đạt cực tiểu toàn cục.
:::

Tính phi tuyến của $Q_\theta$ chưa đủ để $L_B$ mất tính lồi: với $Q_\theta=\theta^2$ và một đích $y<0$, hàm $(y-\theta^2)^2=(\theta^2+\lvert y\rvert)^2$ có đạo hàm bậc hai $12\theta^2+4\lvert y\rvert>0$ nên vẫn lồi; vì vậy Nhận xét 08.11 nói "nói chung". Một phản ví dụ nhỏ cho thấy điểm dừng của gradient có thể không phải cực tiểu. Xét một mẫu, $b=1$, đích $y_1=1$, và mạng tuyến tính hai tầng với một nơ-ron ẩn, $Q_\theta=\theta_1\theta_2$ với $\theta=(\theta_1,\theta_2)$. Khi đó $L(\theta)=(1-\theta_1\theta_2)^2$, có
$$
\nabla_\theta L=-2(1-\theta_1\theta_2)\begin{pmatrix}\theta_2\\ \theta_1\end{pmatrix},\qquad \nabla^2_\theta L(0,0)=\begin{pmatrix}0&-2\\-2&0\end{pmatrix}.
$$
Tại $\theta=(0,0)$, gradient bằng $0$ nhưng $L=1$, trong khi $L=0$ trên đường cong $\theta_1\theta_2=1$; ma trận Hessian có hai trị riêng $2$ và $-2$, nên $(0,0)$ là điểm yên ngựa và $L$ không lồi. Hạ gradient khởi tạo đúng tại $(0,0)$ đứng yên ở đó. Goodfellow, Bengio và Courville (2016, Chương 8) bàn về điểm yên ngựa và cực tiểu địa phương khi tối ưu mạng nơ-ron.

**Trong thực hành.** Dự đoán của cả mini-batch được tính bằng một lần tính xuôi của mạng trực tuyến trên $b$ quan sát, cho mảng kích thước $[b,\lvert\mathcal A\rvert]$, rồi lấy giá trị của hành động đã lưu ở mỗi hàng; đích được tính bằng mạng mục tiêu mà không lưu đồ thị gradient. Sai số bình phương trung bình là lựa chọn của chương để mọi phép tính minh bạch. Bình phương làm các mẫu có sai số lớn chiếm phần lớn gradient; hàm mất mát Huber, bậc hai khi $\lvert y_i-q_i\rvert\le1$ và tuyến tính ngoài khoảng đó, giới hạn ảnh hưởng này và là một lựa chọn khác trong thực hành. Mnih và cộng sự (2015, mục Methods) cắt số hạng sai số của cập nhật vào $[-1,1]$, tương đương dùng hàm mất mát giá trị tuyệt đối cho các sai số ngoài khoảng $(-1,1)$.

**Kiểm tra nhanh.** Lặp mỗi mẫu của một mini-batch hai lần để được mini-batch $2b$ mẫu. $L_B$ và $\nabla_\theta L_B$ đổi thế nào? Không đổi: tử số và mẫu số của trung bình cùng nhân đôi. Nếu dùng tổng thay cho trung bình, cả hai nhân đôi.

Định nghĩa 08.10 cho một hàm vô hướng của $\theta$ và gradient của nó, với giả thiết đích là hằng. Trong chương trình, dự đoán được lấy từ một vector $\lvert\mathcal A\rvert$ giá trị, và đích được tính từ một mạng có cùng kiến trúc; nếu không ghi rõ, thư viện vi phân tự động có thể truyền gradient qua đích. Ở mục tiếp theo, chúng ta viết phép chọn giá trị theo hành động đã lưu và phép dừng gradient, hai thao tác làm chương trình tính đúng gradient của Định nghĩa 08.10.

<!-- note-topic-id: lec-08-topic-08 -->
### Phép chọn theo hành động và dừng gradient

Định nghĩa 08.10 cho hàm mất mát $L_B$ với đích $y_i$ là hằng theo $\theta$. Một chương trình tính $L_B$ phải làm thêm hai việc mà công thức không nói ra. Thứ nhất, mạng trực tuyến trả về cả vector $\mathbf q_\theta(O_i)$ gồm $\lvert\mathcal A\rvert$ giá trị, trong khi $L_B$ chỉ dùng giá trị của hành động $A_i$ đã lưu trong mẫu. Thứ hai, thư viện vi phân tự động lần ngược mọi phép tính dẫn tới $L_B$; nếu đích được tính từ một mạng dùng chung tham số với mạng trực tuyến, gradient sẽ đi qua cả đích.

Việc thứ hai có tiền lệ trong Bài 07. Ở đó, cập nhật bán gradient (semi-gradient) của Q-learning tuyến tính là $w_{n+1}=w_n+\alpha_n\bigl(y_t-\hat q(S_t,A_t,w_n)\bigr)x(S_t,A_t)$: mục tiêu $y_t=R_{t+1}+\gamma\max_{a'}\hat q(S_{t+1},a',w_n)$ chứa chính $w_n$, nhưng được coi là hằng khi lấy đạo hàm. Phép dừng gradient là cách viết quy ước đó vào đồ thị tính (Sutton và Barto, 2018, §9.3).

::: definition Định nghĩa 08.12 (Phép chọn theo hành động và dừng gradient)
Cho mini-batch $B$ của Định nghĩa 08.10 và mảng $M\in\mathbb R^{b\times\lvert\mathcal A\rvert}$ có hàng thứ $i$ là $\mathbf q_\theta(O_i)$.

1. Phép chọn theo hành động (gather) nhận $M$ và vector chỉ số $(A_1,\dots,A_b)$, trả về vector $(q_1,\dots,q_b)$ với $q_i=M_{i,A_i}=[\mathbf q_\theta(O_i)]_{A_i}=Q_\theta(O_i,A_i)$: một phần tử ở mỗi hàng.
2. Dừng gradient (stop-gradient) là toán tử $\operatorname{sg}$ trong đồ thị tính: $\operatorname{sg}(u)$ có giá trị bằng $u$, và khi lan truyền ngược, đạo hàm của $\operatorname{sg}(u)$ theo mọi tham số được lấy bằng $0$.

Dạng cài đặt của hàm mất mát là
$$
L_B(\theta)=\frac1b\sum_{i=1}^b\bigl(\operatorname{sg}(y_i)-q_i\bigr)^2.
$$
:::

$\operatorname{sg}$ không phải một hàm số theo nghĩa thông thường: hàm đồng nhất có đạo hàm $1$, còn $\operatorname{sg}$ là một chỉ dẫn cho thủ tục lấy đạo hàm, tương đương với việc coi $y_i$ là hằng như trong Định nghĩa 08.10. Trong các thư viện, nó ứng với `detach()` hoặc khối `torch.no_grad()` của PyTorch, `tf.stop_gradient` của TensorFlow và `jax.lax.stop_gradient` của JAX. Khi $y_i$ được tính bằng $\theta^-$ là một vector tham số riêng, $y_i$ không phụ thuộc $\theta$, nên $\nabla_\theta y_i=0$ đã đúng về mặt toán học và $\operatorname{sg}$ không đổi kết quả; nó vẫn hữu ích vì thư viện không phải lưu đồ thị của đường tạo đích. $\operatorname{sg}$ trở nên cần thiết khi đích được tính bằng chính $\theta$, chẳng hạn khi không có mạng mục tiêu, hoặc khi mạng mục tiêu được cài bằng cùng một đối tượng với mạng trực tuyến.

Lấy gradient của dạng cài đặt:
$$
\begin{aligned}
\nabla_\theta L_B(\theta)&=\frac1b\sum_{i=1}^b2\bigl(\operatorname{sg}(y_i)-q_i\bigr)\bigl(\nabla_\theta\operatorname{sg}(y_i)-\nabla_\theta q_i\bigr)\\
&=\frac2b\sum_{i=1}^b(q_i-y_i)\,\nabla_\theta q_i.
\end{aligned}
$$
Dòng thứ nhất là quy tắc dây chuyền cho hàm bình phương; dòng thứ hai dùng $\nabla_\theta\operatorname{sg}(y_i)=0$ theo Định nghĩa 08.12 và giá trị $\operatorname{sg}(y_i)=y_i$. Kết quả trùng gradient của Định nghĩa 08.10. Theo phép chọn theo hành động, $q_i=M_{i,A_i}$, nên $\partial q_i/\partial M_{i,a}$ bằng $1$ khi $a=A_i$ và bằng $0$ với $a\ne A_i$: lan truyền ngược đặt $\tfrac2b(q_i-y_i)$ vào ô $(i,A_i)$ của mảng $[b,\lvert\mathcal A\rvert]$ và $0$ vào mọi ô khác, rồi mạng trực tuyến lan tiếp các giá trị này về $\theta$.

Phép chọn theo hành động và phép dừng gradient giữ hai điều khác nhau. Phép chọn theo hành động bảo đảm hàm mất mát so sánh đích với giá trị của đúng hành động đã thực hiện. Bỏ nó và dùng $\max_aQ_\theta(O_i,a)$ thay cho $Q_\theta(O_i,A_i)$: với $\mathbf q_\theta(o)=(0{,}8;\,2{,}5;\,-0{,}3;\,1{,}9)$ của Ví dụ 08.3 và $A_i=a_4$, phép cực đại lấy $2{,}5$ của $a_2$ thay cho $1{,}9$ của $a_4$, và cập nhật kéo giá trị của $a_2$ về một đích sinh từ hành động $a_4$. Phép dừng gradient bảo đảm cập nhật là cập nhật bán gradient của Bài 07. Bỏ nó khi đích tính bằng chính $\theta$: với $Q_\theta=\theta$, $R=1$, $\gamma=0{,}9$, $\theta=0$ như Ví dụ 08.5, đạo hàm của $(1+0{,}9\,\theta-\theta)^2$ là $-0{,}2$, so với $-2$ khi coi đích là hằng; đó là phương pháp gradient dư (residual gradient) của Sutton và Barto (2018, §11.5), không phải DQN.

![Hai hàng. Hàng trên, đường tạo đích, không nhận gradient: O phẩy i vào mạng mục tiêu Q theta trừ, rồi lấy max theo a phẩy; cùng R i và Z i từ ô bên dưới tạo đích y i; y i đi qua ô sg viền nét đứt. Hàng dưới, đường dự đoán, nhận gradient: O i vào mạng trực tuyến Q theta, cho một vector giá trị; phép chọn theo hành động gather nhận A i từ ô bên trên và lấy một phần tử, được q i. Hai mũi tên từ sg của y i và từ q i cùng đi vào ô MSE bên phải.](img/lec-08/dqn-computation-graph.svg)

Hình vẽ đồ thị tính của $L_B$ cho một mẫu. Hàng trên là đường tạo đích: $O'_i$ đi qua mạng mục tiêu, phép cực đại theo $a'$ cho một số, rồi $R_i$ và $Z_i$ hoàn tất $y_i$; ô $\operatorname{sg}$ viền nét đứt đánh dấu nơi gradient dừng. Hàng dưới là đường dự đoán: $O_i$ đi qua mạng trực tuyến, phép chọn theo hành động nhận $A_i$ và lấy một phần tử, cho $q_i$. Chỉ hàng dưới nhận gradient của $L_B$.

::: example Ví dụ 08.13 (Gradient đi qua phép chọn theo hành động)
**Dữ kiện.** $b=2$, $\lvert\mathcal A\rvert=3$. Mạng trực tuyến trả về
$$
M=\begin{pmatrix}1{,}0&3{,}1&0{,}2\\-1{,}5&0{,}4&2{,}0\end{pmatrix},
$$
hành động đã lưu $A_1=a_2$, $A_2=a_1$, và đích $y_1=4{,}6$, $y_2=-2$.

**Tính.** Phép chọn cho $q_1=M_{1,2}=3{,}1$ và $q_2=M_{2,1}=-1{,}5$. Với $b=2$, $\tfrac2b=1$, nên đạo hàm của $L_B$ theo $M$ là
$$
\frac{\partial L_B}{\partial M}=\begin{pmatrix}0&3{,}1-4{,}6&0\\-1{,}5-(-2)&0&0\end{pmatrix}=\begin{pmatrix}0&-1{,}5&0\\0{,}5&0&0\end{pmatrix}.
$$

**Diễn giải.** Ô $M_{2,3}=2{,}0$ là giá trị lớn nhất của hàng 2 nhưng nhận gradient $0$, vì hành động đã lưu là $a_1$. Hạ gradient tăng $M_{1,2}$ và giảm $M_{2,1}$, tức kéo mỗi $q_i$ về $y_i$.
:::

**Trong thực hành.** Trong PyTorch, phép chọn thường viết `q = net(obs).gather(1, act.unsqueeze(1)).squeeze(1)`, với `act` là tensor số nguyên kiểu `int64` kích thước $[b]$; đích được tính trong khối `with torch.no_grad():` từ mạng mục tiêu. Hai lỗi hay gặp là dùng phép cực đại của mạng trực tuyến thay cho phép chọn theo $A_i$, và tính đích bằng mạng trực tuyến mà không dừng gradient. Bài tập 08.2 ở cuối chương kiểm tra hai thao tác này trên một đoạn mã: phép chọn viết sai bằng chỉ số hàng và đích tính ngoài khối `no_grad`.

**Kiểm tra nhanh.** Vì sao đường tạo đích dùng phép cực đại tại $O'_i$, còn đường dự đoán dùng phép chọn theo $A_i$? Tại $O_i$, hành động $A_i$ đã xảy ra và đích là mẫu của giá trị cặp $(O_i,A_i)$, nên dự đoán phải là giá trị của đúng cặp đó. Tại $O'_i$, đích đánh giá chính sách tham lam, nên dùng giá trị lớn nhất; hành động thực hiện tiếp theo tại $O'_i$ không được lưu trong mẫu và không cần.

Đến đây chúng ta có hàm mất mát, gradient của nó và hai thao tác làm chương trình tính đúng gradient đó: phép chọn theo hành động và phép dừng gradient. Bài tập 08.1 ở cuối chương tính tay đích, sai số, hàm mất mát và đạo hàm theo $q_i$ trên số liệu của Ví dụ 08.7 và 08.8. Ở mục tiếp theo, chúng ta ghép thu thập, lưu, rút mẫu, bước tối ưu này và đồng bộ thành một vòng lặp với hai bộ đếm.

<!-- note-topic-id: lec-08-topic-10 -->
### Vòng huấn luyện DQN: hai bộ đếm $t$ và $k_{\mathrm{opt}}$

Đến cuối mục trước, chúng ta có một bước tối ưu hoàn chỉnh: rút $b$ mẫu từ bộ nhớ phát lại $\mathcal D$, lấy $q_i$ bằng phép chọn theo hành động, tính $y_i$ bằng mạng mục tiêu dưới phép dừng gradient, rồi đi một bước theo $-\nabla_\theta L_B$. Bước này chỉ chạy được khi $\mathcal D$ có dữ liệu, và dữ liệu chỉ sinh ra khi tác tử tương tác với môi trường. Mỗi bước môi trường sinh đúng một mẫu chuyển, còn mỗi bước tối ưu dùng một mini-batch $b$ mẫu. Hai việc chạy xen kẽ với hai nhịp khác nhau, nên chúng ta cần hai bộ đếm riêng: $t\in\mathbb N_0$ đếm bước môi trường, $k_{\mathrm{opt}}\in\mathbb N_0$ đếm bước tối ưu.

Vòng thu thập chạy theo $t$. Tại quan sát $O_t$, mạng trực tuyến chọn $A_t$ theo quy tắc $\epsilon_{\mathrm{exp}}$-tham lam từ $Q_\theta(O_t,\cdot)$; môi trường trả $R_{t+1}$, $O_{t+1}$ và hai cờ $Z_{t+1}$, $U_{t+1}$; mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ được ghi vào $\mathcal D$, và $O_{t+1}$ thành quan sát của bước kế tiếp. Vòng tối ưu chạy theo $k_{\mathrm{opt}}$. Mỗi bước rút đều một mini-batch $B$ từ $\mathcal D$, tính đích $y_i$ bằng $Q_{\theta^-}$, rồi cập nhật $\theta$ theo gradient của $L_B$; sau mỗi $C$ bước tối ưu, tham số mạng mục tiêu được gán $\theta^-\leftarrow\theta$. Ba số nguyên dương điều khiển hai nhịp: $N_{\mathrm{start}}$ là số mẫu tối thiểu trong $\mathcal D$ trước bước tối ưu đầu tiên, $F$ là số bước môi trường giữa hai bước tối ưu, và $C$ là số bước tối ưu giữa hai lần đồng bộ.

![Sơ đồ hai vòng. Vòng thu thập bên trái, mỗi bước tăng bộ đếm t: mạng trực tuyến Q theta chọn hành động A theo quy tắc epsilon exp tham lam và gửi cho môi trường; môi trường trả quan sát kế tiếp O phẩy về mạng trực tuyến và gửi mẫu chuyển O, A, R, O phẩy, Z, U vào bộ nhớ phát lại D. Vòng tối ưu bên phải, mỗi bước tăng bộ đếm k opt: rút đều b mẫu từ bộ nhớ thành mini-batch B; mạng mục tiêu Q theta trừ cấp đích y i cho mini-batch; gradient của hàm mất mát L B theo theta cập nhật mạng trực tuyến. Mũi tên nét đứt từ mạng trực tuyến sang mạng mục tiêu: mỗi C bước tối ưu gán theta trừ bằng theta.](img/lec-08/dqn-training-loop.svg)

Hình vẽ hai vòng. Các mũi tên của vòng thu thập (bên trái) mang $A$, $O'$ và mẫu chuyển $(O,A,R,O',Z,U)$; các mũi tên của vòng tối ưu (bên phải) mang mini-batch, đích $y_i$ và gradient $\nabla_\theta L_B$. Mũi tên nét đứt là phép đồng bộ, đếm theo $k_{\mathrm{opt}}$. Hai vòng chạm nhau ở hai chỗ. Ở bộ nhớ $\mathcal D$, vòng thu thập ghi và vòng tối ưu đọc. Ở mạng trực tuyến, vòng thu thập dùng $Q_\theta$ để chọn hành động và vòng tối ưu cập nhật $\theta$. Chỗ chạm thứ hai tạo một vòng phản hồi: mỗi bước tối ưu đổi hành vi $\epsilon_{\mathrm{exp}}$-tham lam, hành vi mới đổi dữ liệu ghi vào $\mathcal D$, nên phân phối của $\mathcal D$ trôi theo thời gian. Mệnh đề 08.8 vẫn áp dụng, vì hành vi tại bước $t$ chỉ dùng $\theta_t$ học từ lịch sử tới bước $t$. Mạng mục tiêu không nằm trong vòng thu thập; nó chỉ đổi tại các mốc đồng bộ.

::: example Ví dụ 08.14 (Hai nhịp với cấu hình Atari)
**Dữ kiện.** Mnih và cộng sự (2015, Extended Data Table 1) tối ưu sau mỗi $F=4$ bước môi trường, đồng bộ sau mỗi $C=10\,000$ bước tối ưu, với mini-batch $b=32$. Xét giai đoạn sau khi $\mathcal D$ đã có đủ $N_{\mathrm{start}}$ mẫu.

**Tính.** Giữa hai lần đồng bộ có $C=10\,000$ bước tối ưu, tức $F\cdot C=4\cdot10\,000=40\,000$ bước môi trường, trong đó $\theta^-$ đứng yên. Trong khoảng đó, vòng thu thập ghi $40\,000$ mẫu chuyển mới, còn vòng tối ưu rút $C\cdot b=320\,000$ mẫu, tức $b/F=8$ lần rút cho mỗi mẫu mới.

**Diễn giải.** Nếu đếm chu kỳ đồng bộ theo $t$ thay cho $k_{\mathrm{opt}}$, cùng số $10\,000$ cho đồng bộ thường gấp $F=4$ lần, nên $\theta^-$ chỉ đứng yên trong $2\,500$ bước tối ưu. Khi $\mathcal D$ đã đầy với dung lượng $N$, mỗi mẫu ở lại $N$ bước môi trường, tức $N/F$ bước tối ưu, và mỗi lần rút chọn nó với xác suất $1/N$; kỳ vọng số lần nó được rút là $(N/F)\cdot b\cdot(1/N)=b/F=8$, không phụ thuộc $N$.
:::

**Trong thực hành.** Một chương trình DQN giữ $t$ và $k_{\mathrm{opt}}$ là hai biến riêng: $t$ tăng sau mỗi lần gọi bước môi trường, $k_{\mathrm{opt}}$ tăng sau mỗi lần cập nhật $\theta$. Hai cấu hình có $F$ khác nhau, ở cùng một $t$, đã thực hiện số bước tối ưu khác nhau; vì vậy khi so sánh hiệu quả mẫu, trục ngang phải là $t$, số tương tác với môi trường, còn lịch đồng bộ và lịch của bộ tối ưu tính theo $k_{\mathrm{opt}}$.

Sơ đồ cho các việc của mỗi vòng nhưng chưa chốt thứ tự: kiểm điều kiện tối ưu trước hay sau khi tăng $t$, đồng bộ trước hay sau khi tăng $k_{\mathrm{opt}}$, đặt lại môi trường lúc nào. Chúng ta chốt các thứ tự đó bằng giả mã.

Trước các bước lặp, chúng ta cố định đầu vào, đầu ra và trạng thái ban đầu của thuật toán. Đầu vào gom mọi đại lượng đã gặp: hệ số chiết khấu và hai mạng của phần 2, bộ nhớ phát lại của phần 3, hàm mất mát và bộ tối ưu của phần 4, cùng ba số nhịp $N_{\mathrm{start}}$, $F$, $C$ vừa nêu.

::: algorithm Thuật toán 08.13 (DQN với bộ nhớ phát lại và mạng mục tiêu)
**Đầu vào.** Hệ số chiết khấu $\gamma\in[0,1)$; xác suất thăm dò $\epsilon_{\mathrm{exp}}\in[0,1]$; một bộ tối ưu theo gradient với tốc độ học $\eta>0$; ngân sách $T\in\mathbb N_+$ bước môi trường; năm số nguyên dương $N$ (dung lượng của $\mathcal D$), $b$ (cỡ mini-batch), $N_{\mathrm{start}}$ (số mẫu tối thiểu trong $\mathcal D$ trước bước tối ưu đầu tiên), $F$ (số bước môi trường giữa hai bước tối ưu) và $C$ (số bước tối ưu giữa hai lần đồng bộ), với $b\le N_{\mathrm{start}}\le N$.

**Đầu ra.** Tham số $\theta$ khi dừng và chính sách tham lam $\pi(o)\in\arg\max_{a}Q_\theta(o,a)$.

**Khởi tạo.** $\mathcal D\leftarrow\varnothing$, một bộ đệm vòng dung lượng $N$; $\theta$ ngẫu nhiên; $\theta^-\leftarrow\theta$; $O_0$ là quan sát đầu tiên sau khi đặt lại môi trường; $t\leftarrow0$; $k_{\mathrm{opt}}\leftarrow0$.

**Lặp** khi $t<T$:

1. Chọn $A_t$ theo quy tắc $\epsilon_{\mathrm{exp}}$-tham lam từ $Q_\theta(O_t,\cdot)$, trong đó $O_t$ là quan sát hiện hành: với xác suất $\epsilon_{\mathrm{exp}}$ chọn đều một hành động trong $\mathcal A$, ngược lại chọn một hành động trong $\arg\max_aQ_\theta(O_t,a)$.
2. Thực hiện $A_t$; nhận $R_{t+1}$, hai cờ $Z_{t+1}$, $U_{t+1}$ và quan sát trả về.
3. Lưu mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ vào $\mathcal D$, trong đó $O_{t+1}$ là quan sát cuối của mẫu chuyển, lấy trước mọi lần đặt lại; khi $\lvert\mathcal D\rvert=N$, mẫu mới ghi đè mẫu cũ nhất.
4. Nếu $Z_{t+1}\lor U_{t+1}=1$: đặt lại môi trường; quan sát hiện hành của bước kế là quan sát đầu lượt mới. Nếu không, quan sát hiện hành của bước kế là $O_{t+1}$. Tăng $t\leftarrow t+1$.

Nếu $\lvert\mathcal D\rvert\ge N_{\mathrm{start}}$ và $t\bmod F=0$, thực hiện bước 5–9; nếu không, quay lại bước 1.

5. Rút đều $b$ mẫu $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\dots,b$, từ $\mathcal D$.
6. Tính $q_i=[\mathbf q_\theta(O_i)]_{A_i}$ bằng phép chọn theo hành động (Định nghĩa 08.12).
7. Tính đích $y_i=\operatorname{sg}\bigl(R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')\bigr)$.
8. Bộ tối ưu cập nhật $\theta$ theo $\nabla_\theta L_B$, với $L_B=\tfrac1b\sum_{i=1}^b(y_i-q_i)^2$ (Định nghĩa 08.10); sau đó $k_{\mathrm{opt}}\leftarrow k_{\mathrm{opt}}+1$.
9. Nếu $k_{\mathrm{opt}}\bmod C=0$, gán $\theta^-\leftarrow\theta$.

Quay lại bước 1. Khi $t=T$, dừng và trả $\theta$ cùng chính sách tham lam theo $Q_\theta$.
:::

Thuật toán có hai nhóm đầu vào. Nhóm thứ nhất, gồm $\gamma$, $\epsilon_{\mathrm{exp}}$ và bộ tối ưu với $\eta$, quyết định từng phép tính: đích, hành vi và bước tham số; các quy tắc cập nhật cụ thể của bộ tối ưu được viết ở phần 5. Nhóm thứ hai, gồm năm số nguyên dương, quyết định nhịp: $N$ và $b$ là kích thước của bộ nhớ và của mini-batch, còn $N_{\mathrm{start}}$, $F$, $C$ quyết định khi nào vòng tối ưu chạy và khi nào mạng mục tiêu đổi. Ngân sách $T$ đếm theo $t$; trong thực hành có thể thay bằng một tiêu chuẩn dừng định trước trên lợi tức đánh giá.

Mỗi điều kiện trên đầu vào ngăn một sự cố cụ thể. Điều kiện $\gamma<1$ cùng phần thưởng bị chặn, $\lvert R_{t+1}\rvert\le R_{\max}$, cho $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$, nên mọi giá trị hành động hữu hạn cả khi lượt không kết thúc. Bỏ điều kiện này: với $\gamma=1$, một nhiệm vụ trả phần thưởng $+1$ mỗi bước và một chính sách không bao giờ làm lượt kết thúc có lợi tức vô hạn; mẫu bị cắt ngắn vẫn bootstrap ($Z=0$), nên giá trị $q$ của cặp mà chính sách đó chọn phải thỏa $q=1+q$, phương trình không có nghiệm hữu hạn. Điều kiện $N_{\mathrm{start}}\ge b$ để lần rút đầu tiên có thể gồm $b$ mẫu khác nhau (bắt buộc khi rút không hoàn lại); với $N_{\mathrm{start}}=1$ và $b=32$, rút có hoàn lại cho một mini-batch gồm $32$ bản sao của cùng một mẫu chuyển. Điều kiện $N_{\mathrm{start}}\le N$ là cần, vì $\lvert\mathcal D\rvert$ không bao giờ vượt $N$; với $N_{\mathrm{start}}>N$, điều kiện tối ưu trước bước 5 không bao giờ đúng và $\theta$ giữ giá trị khởi tạo. Cuối cùng, $C$ đếm theo $k_{\mathrm{opt}}$: với $C=1$, $\theta^-$ được gán bằng $\theta$ sau mọi bước tối ưu, nên đích ở bước kế tiếp tính bằng đúng giá trị tham số đang học, như trong Ví dụ 08.5.

Khởi tạo $\theta^-\leftarrow\theta$ làm đích của những bước tối ưu đầu tiên tính bằng cùng mạng ban đầu, thay cho một mạng mục tiêu ngẫu nhiên độc lập. Đầu ra là chính sách tham lam theo $Q_\theta$, khác hành vi $\epsilon_{\mathrm{exp}}$-tham lam dùng khi thu thập; khi đánh giá thuật toán, chúng ta chạy chính sách tham lam này trên các lượt riêng.

Bảng sau ghi giá trị đầu vào mà Mnih và cộng sự (2015, Extended Data Table 1) dùng cho các trò chơi Atari.

| ký hiệu | nghĩa | giá trị của Mnih và cộng sự (2015) |
|---|---|---|
| $\gamma$ | hệ số chiết khấu | $0{,}99$ |
| $\eta$ | tốc độ học của bộ tối ưu (RMSprop) | $0{,}00025$ |
| $\epsilon_{\mathrm{exp}}$ | xác suất thăm dò | giảm tuyến tính từ $1$ xuống $0{,}1$, rồi giữ $0{,}1$ |
| $N$ | dung lượng của $\mathcal D$ | $10^6$ |
| $b$ | cỡ mini-batch | $32$ |
| $N_{\mathrm{start}}$ | số mẫu trước bước tối ưu đầu | $5\cdot10^4$ |
| $F$ | số bước môi trường giữa hai bước tối ưu | $4$ |
| $C$ | số bước tối ưu giữa hai lần đồng bộ | $10^4$ |

Với các giá trị này, khi vòng tối ưu đã chạy, $\theta^-$ đứng yên trong $F\cdot C=4\cdot10^4$ bước môi trường (Ví dụ 08.14). Lịch giảm dần của $\epsilon_{\mathrm{exp}}$ không làm hỏng Mệnh đề 08.8: xác suất thăm dò tại bước $t$ là một hàm của $t$, nên hành vi vẫn chỉ phụ thuộc lịch sử tới bước $t$.

Bốn bước đầu của vòng lặp là vòng thu thập. Bước 1 dùng mạng trực tuyến hiện hành, nên hành vi đổi theo từng bước tối ưu. Bước 3 đòi $O_{t+1}$ là quan sát cuối của chính mẫu chuyển. Khi môi trường tự đặt lại sau bước cuối của một lượt, quan sát trả về có thể đã là quan sát đầu của lượt mới, còn quan sát cuối nằm trong thông tin phụ mà môi trường trả kèm; tên trường của thông tin này phụ thuộc thư viện và phiên bản. Lưu nhầm quan sát đầu lượt mới không gây sai ở mẫu kết thúc, vì $Z_{t+1}=1$ và mặt nạ xóa phần bootstrap. Ở mẫu bị cắt ngắn, $Z_{t+1}=0$ và $U_{t+1}=1$, đích $R_{t+1}+\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$ khi đó bootstrap từ một quan sát không nối với $O_t$. Bước 4 đặt lại khi $Z_{t+1}\lor U_{t+1}=1$, trong khi đích chỉ dùng $1-Z$ (Pardo và cộng sự 2018). Ở ranh giới lượt, quan sát hiện hành của bước kế là quan sát đầu lượt mới, còn $O_{t+1}$ trong mẫu đã lưu ở bước 3 vẫn là quan sát cuối của lượt cũ; hai quan sát này khác nhau, nên chúng ta không gán lại ký hiệu $O_{t+1}$. Bộ đếm $t$ tăng sau khi lưu, nên khi kiểm điều kiện tối ưu trước bước 5, $t$ là số bước môi trường đã hoàn tất và $\lvert\mathcal D\rvert=\min(t,N)$.

**Kiểm tra nhanh.** Cho $N=6$, $b=2$, $N_{\mathrm{start}}=3$, $F=2$. Bước tối ưu đầu tiên chạy khi nào? Sau $k\le6$ bước môi trường, $t=k$ và $\lvert\mathcal D\rvert=k$. Điều kiện tối ưu trước bước 5 cần $k\ge3$ và $k$ chẵn, nên bước tối ưu đầu tiên chạy khi $t=4$, với $\lvert\mathcal D\rvert=4$.

Bước 5–9 là vòng tối ưu của sơ đồ hai vòng. Điều kiện ở đầu được kiểm sau khi $t$ đã tăng ở bước 4, nên $t$ là số bước môi trường đã hoàn tất; nếu điều kiện sai, vòng lặp quay lại bước 1 mà không đổi $\theta$, $\theta^-$ hay $k_{\mathrm{opt}}$. Bước 6 và bước 7 là hai đường tính của Định nghĩa 08.12: phép chọn theo hành động lấy giá trị của hành động đã lưu, còn đích nằm trong $\operatorname{sg}$ và chỉ dùng $\theta^-$. Bước 8 và bước 9 có thứ tự cố định: cập nhật $\theta$, tăng $k_{\mathrm{opt}}$, rồi mới kiểm $C$. Với thứ tự này, lần đồng bộ thứ $m$ xảy ra ngay sau bước tối ưu thứ $mC$, và giữa hai lần đồng bộ có đúng $C$ bước tối ưu với cùng $\theta^-$. Kiểm $C$ trước khi tăng $k_{\mathrm{opt}}$ làm lần đồng bộ đầu xảy ra ngay sau bước tối ưu thứ nhất, vì khi đó $k_{\mathrm{opt}}=0$. Giữa hai mốc đồng bộ, đích $y_i$ của một mẫu đã lưu không đổi; nó chỉ đổi tại mốc đồng bộ, khi $\theta^-$ nhận giá trị mới.

::: example Ví dụ 08.15 (Truy dấu hai bộ đếm)
**Dữ kiện.** $N=6$, $b=2$, $N_{\mathrm{start}}=3$, $F=2$, $C=2$, $T=10$; khởi tạo $t=0$, $k_{\mathrm{opt}}=0$, $\mathcal D=\varnothing$.

**Tính.** Sau mỗi lần qua bước 4, $\lvert\mathcal D\rvert=\min(t,6)$. Điều kiện tối ưu cần $\min(t,6)\ge3$ và $t$ chẵn, nên bước 5–9 chạy tại $t=4,6,8,10$.

| $t$ | $\lvert\mathcal D\rvert$ | $k_{\mathrm{opt}}$ sau cập nhật (bước 8) | đồng bộ $\theta^-\leftarrow\theta$ (bước 9) |
|---|---|---|---|
| $4$ | $4$ | $1$ | không |
| $6$ | $6$ | $2$ | có |
| $8$ | $6$ | $3$ | không |
| $10$ | $6$ | $4$ | có |

Tại $t=10$, điều kiện $t<T$ sai và thuật toán dừng sau khi đồng bộ.

**Diễn giải.** Mười bước môi trường cho bốn bước tối ưu (năm thời điểm chẵn $t\le10$, trừ $t=2$ vì khi đó $\lvert\mathcal D\rvert=2<N_{\mathrm{start}}$) và hai lần đồng bộ. Nếu kiểm $C$ trước khi tăng $k_{\mathrm{opt}}$, đồng bộ xảy ra tại $t=4$ và $t=8$, tức ngay sau bước tối ưu thứ nhất và thứ ba, nên $\theta^-$ đầu tiên chỉ giữ cố định trong một bước tối ưu.
:::

**Trong thực hành.** Chọn $F=1$ cho một bước tối ưu sau mỗi bước môi trường, nhưng vòng tối ưu vẫn chờ đủ $N_{\mathrm{start}}$ mẫu. Lợi tức của các lượt thu thập được sinh bởi hành vi $\epsilon_{\mathrm{exp}}$-tham lam và trộn nhiều phiên bản của $\theta$, nên không đo chất lượng của chính sách đầu ra. Đánh giá chạy chính sách tham lam theo $Q_\theta$, hoặc một chính sách $\epsilon$-tham lam với $\epsilon$ nhỏ cố định, trên các lượt riêng; Mnih và cộng sự (2015, mục Methods) đánh giá với $\epsilon=0{,}05$.

**Kiểm tra nhanh.** Với $F=4$ và $C=10\,000$, trong $10^6$ bước môi trường sau khi $\mathcal D$ đã có đủ $N_{\mathrm{start}}$ mẫu, thuật toán thực hiện khoảng bao nhiêu bước tối ưu và bao nhiêu lần đồng bộ? Khoảng $10^6/4=250\,000$ bước tối ưu và $250\,000/10\,000=25$ lần đồng bộ.

Thuật toán 08.13 viết mỗi phép tính cho một mẫu $i$. Trong chương trình, $b$ mẫu của mini-batch được xử lý cùng lúc dưới dạng mảng, và phần lớn lỗi cài đặt là lỗi kích thước hoặc kiểu của các mảng đó. Ở mục tiếp theo, chúng ta nêu kích thước và kiểu của từng mảng trong một mini-batch Atari.

<!-- note-topic-id: lec-08-topic-11 -->
### Kích thước tensor của mini-batch Atari

Khi $b$ mẫu của một mini-batch được xử lý cùng lúc, mỗi đại lượng của Thuật toán 08.13 trở thành một mảng nhiều chiều (tensor) với một kích thước và một kiểu số. Một phép tính đúng trên từng mẫu vẫn cho kết quả sai khi kích thước của hai mảng không khớp, và thư viện thường không báo lỗi trong trường hợp này. Chúng ta cần ghi rõ kích thước và kiểu của mọi mảng đi vào hàm mất mát.

Nhắc lại cấu trúc của một quan sát Atari: $O_i$ gồm bốn khung xám kích thước $H\times W$ xếp chồng, với $H=W=84$ theo Mnih và cộng sự (2015), nên mỗi quan sát là một mảng $[4,H,W]$ gồm $4\cdot84\cdot84=28\,224$ số. Ký hiệu $[d_1,\dots,d_k]$ chỉ một mảng $k$ chiều với $d_j$ phần tử theo chiều thứ $j$; $[b]$ là một vector $b$ phần tử, và $[\,]$ là một số vô hướng.

::: remark Nhận xét 08.14 (Kích thước và kiểu của các mảng trong một mini-batch)
Cho mini-batch $B=\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$ của Thuật toán 08.13 với quan sát Atari. Chiều đầu của mọi mảng đánh số mẫu, và

| mảng | kích thước | kiểu | vai trò |
|---|---|---|---|
| $O$, $O'$ | $[b,4,H,W]$ | `float32` (lưu dạng `uint8`) | đầu vào của hai mạng |
| $A$ | $[b]$ | `int64` | chỉ số cột của phép chọn theo hành động |
| $R$ | $[b]$ | `float32` | phần thưởng trong đích |
| $Z$, $U$ | $[b]$ | `bool` | $Z$ vào mặt nạ $1-Z$; $U$ không vào $L_B$ |
| $\mathbf q_\theta(O)$, $\mathbf q_{\theta^-}(O')$ | $[b,\lvert\mathcal A\rvert]$ | `float32` | đầu ra của hai mạng |
| $q$, $y$ | $[b]$ | `float32` | dự đoán và đích |
| $L_B$ | $[\,]$ | `float32` | hàm mất mát |

Phép chọn theo hành động lấy ở hàng $i$ của $\mathbf q_\theta(O)$ phần tử cột $A_i$; phép cực đại của đích lấy theo chiều hành động, chiều thứ hai, của $\mathbf q_{\theta^-}(O')$. Mọi mảng đi vào $L_B$ nằm trên cùng một thiết bị tính, tức bộ xử lý thực hiện phép tính (CPU hoặc GPU).
:::

![Hai hàng. Hàng trên: quan sát O kích thước b, 4, H, W vào mạng trực tuyến Q theta, ra mảng b nhân số hành động; phép chọn theo hành động nhận A kích thước b từ ô bên dưới, lấy một phần tử mỗi hàng và cho q kích thước b. Hàng dưới: quan sát kế tiếp O phẩy kích thước b, 4, H, W vào mạng mục tiêu Q theta trừ, ra mảng b nhân số hành động; phép cực đại theo chiều hành động cho mảng kích thước b; cùng R và Z kích thước b từ ô bên trên tạo đích y kích thước b. q và y cùng vào ô hàm mất mát L B, một số vô hướng. Ghi chú dưới cùng: U kích thước b không vào L B.](img/lec-08/tensor-contract.svg)

Hình đọc theo hai hàng của đồ thị tính. Ở hàng trên, mạng trực tuyến biến $[b,4,H,W]$ thành $[b,\lvert\mathcal A\rvert]$, rồi phép chọn theo hành động dùng $A$ để giảm mỗi hàng còn một số, cho $q$ kích thước $[b]$. Ở hàng dưới, mạng mục tiêu cho $[b,\lvert\mathcal A\rvert]$, phép cực đại theo chiều hành động giảm mỗi hàng còn một số, rồi $R$ và $Z$ hoàn tất $y$ kích thước $[b]$. Hai vector cùng kích thước $[b]$ đi vào $L_B$, một số vô hướng. Cờ $U$ có trong mini-batch nhưng không đi vào $L_B$.

Mỗi dòng của Nhận xét 08.14 chặn một lỗi riêng. Kiểu số nguyên của $A$ là điều kiện để dùng $A_i$ làm chỉ số cột. Chiều đầu chung $b$ bảo đảm $y_i-q_i$ ghép đúng hai đại lượng của cùng một mẫu; bỏ điều kiện $q$ và $y$ cùng kích thước $[b]$ thì phép trừ lan truyền kích thước (broadcasting) ghép mọi cặp $(i,j)$, như Ví dụ 08.17 dưới đây. Phép cực đại phải lấy theo chiều hành động; lấy cực đại trên toàn mảng $[b,\lvert\mathcal A\rvert]$ cho một số duy nhất, và mọi mẫu nhận chung một giá trị bootstrap. Cùng thiết bị tính là điều kiện để thư viện thực hiện được phép tính; thư viện báo lỗi khi hai mảng của một phép toán nằm trên hai thiết bị khác nhau.

::: example Ví dụ 08.16 (Kích thước với $b=32$)
**Dữ kiện.** $b=32$, $H=W=84$, $\lvert\mathcal A\rvert=18$.

**Tính.** $O$ có kích thước $[32,4,84,84]$, gồm $32\cdot28\,224=903\,168$ số: $903\,168$ byte ở dạng `uint8` (một byte mỗi số) và $3\,612\,672$ byte, khoảng $3{,}6$ MB, ở dạng `float32` (bốn byte mỗi số). $O'$ có cùng kích thước. Mỗi mạng trả $[32,18]$, tức $576$ số; $q$, $y$, $A$, $R$, $Z$, $U$ mỗi mảng có $32$ phần tử; $L_B$ là một số.

**Diễn giải.** Gần như toàn bộ bộ nhớ của mini-batch nằm ở hai mảng quan sát; mọi mảng còn lại có chiều đầu $32$ và tối đa $18$ cột.
:::

::: example Ví dụ 08.17 (Lỗi lan truyền kích thước)
**Dữ kiện.** Mini-batch hai mẫu có $q=(3{,}1;\,-1{,}5)$ và $y=(4{,}6;\,-2)$, với $L_B=\tfrac12(1{,}5^2+0{,}5^2)=1{,}25$. Giả sử $q$ được giữ ở dạng cột $[2,1]$ sau phép chọn, còn $y$ có dạng $[2]$.

**Tính.** Phép trừ $y-q$ lan truyền thành ma trận $[2,2]$ có phần tử $(i,j)$ bằng $y_j-q_i$:
$$
\begin{pmatrix}4{,}6-3{,}1&-2-3{,}1\\4{,}6+1{,}5&-2+1{,}5\end{pmatrix}=\begin{pmatrix}1{,}5&-5{,}1\\6{,}1&-0{,}5\end{pmatrix}.
$$
Trung bình bình phương của bốn phần tử là $\tfrac14(2{,}25+26{,}01+37{,}21+0{,}25)=16{,}43$.

**Diễn giải.** Hai phần tử ngoài đường chéo ghép dự đoán của một mẫu với đích của mẫu kia; giá trị $16{,}43$ thay cho $1{,}25$, và gradient kéo mỗi $q_i$ về trung bình của cả hai đích. Bỏ chiều thừa (squeeze) để $q$ có dạng $[2]$ trước phép trừ cho lại $L_B=1{,}25$.
:::

**Trong thực hành.** Bộ nhớ phát lại lưu khung ở dạng `uint8` và chỉ chuyển sang `float32` khi tạo mini-batch. Với $N=10^6$ mẫu chuyển, lưu riêng $O$ và $O'$ của mỗi mẫu ở dạng `uint8` cần $2\cdot10^6\cdot28\,224$ byte, khoảng $56$ GB; lưu mỗi khung $84\times84$ một lần cần khoảng $10^6\cdot7\,056$ byte, khoảng $7$ GB; dạng `float32` nhân mỗi con số với bốn. Cờ $Z$ được chuyển sang kiểu số trước khi tính $1-Z$, vì một số thư viện không cho phép phép trừ trên kiểu `bool`. Kích thước ở đây là giao diện tối thiểu để đọc và kiểm tra chương trình, không phải đặc tả để tái lập kết quả Atari.

**Kiểm tra nhanh.** Gọi phép cực đại trên mảng $\mathbf q_{\theta^-}(O')$ kích thước $[b,\lvert\mathcal A\rvert]$ mà không chỉ chiều thì được gì? Một số vô hướng, giá trị lớn nhất trên mọi mẫu và mọi hành động; mọi $y_i$ dùng chung giá trị đó, nên đích của mỗi mẫu không còn phụ thuộc $O'_i$ của chính nó. Lấy cực đại theo chiều thứ hai cho đúng mảng $[b]$.

Đến đây Thuật toán 08.13 đã đầy đủ: đầu vào, hai vòng với hai bộ đếm, đích có mặt nạ và dừng gradient, và kích thước của mọi mảng trong một bước tối ưu. Bài tập 08.2 ở cuối chương kiểm tra các điều kiện này trên một đoạn mã. Bước 8 của thuật toán giao việc biến $\nabla_\theta L_B$ thành bước tham số cho bộ tối ưu; ở phần tiếp theo, chúng ta viết các quy tắc cập nhật của bộ tối ưu.

## 5. Bộ tối ưu theo gradient

<!-- note-topic-id: lec-08-topic-14 -->
### Vai trò của bộ tối ưu và ba quy tắc cập nhật

Ở bước 8 của Thuật toán 08.13, mỗi bước tối ưu có gradient $\nabla_\theta L_B$ của hàm mất mát trên một mini-batch, tính tại tham số hiện hành. Thuật toán chưa nói gradient này được đổi thành bước tham số theo quy tắc nào. Chúng ta cần một quy tắc như vậy, cùng các siêu tham số của nó, và cần biết quy tắc đó quyết định gì và không quyết định gì trong DQN.

::: definition Định nghĩa 08.15 (Bộ tối ưu theo gradient)
Cho dãy mini-batch $B_1,B_2,\dots$ và tham số khởi tạo $\theta_0\in\mathbb R^d$. Một bộ tối ưu (optimizer) theo gradient với tốc độ học $\eta>0$ gồm một trạng thái phụ $\psi_j$ với giá trị đầu $\psi_0$ (có thể rỗng) và một quy tắc $\operatorname{Update}$, sao cho tại bước tối ưu thứ $j=1,2,\dots$
$$
g_j=\nabla_\theta L_{B_j}(\theta_{j-1}),\qquad(\theta_j,\psi_j)=\operatorname{Update}(\theta_{j-1},\psi_{j-1},g_j);
$$
quy tắc $\operatorname{Update}$ có thể phụ thuộc $j$, như phép hiệu chỉnh lệch của Adam. Chỉ số $j$ bằng giá trị của $k_{\mathrm{opt}}$ ngay sau khi tăng ở bước 8 của Thuật toán 08.13; trong lúc bộ tối ưu chạy, $k_{\mathrm{opt}}=j-1$. Vì $k_{\mathrm{opt}}$ bắt đầu từ $0$, $j$ bắt đầu từ $1$ và mẫu số $1-\beta^{\,j}$ của Adam khác $0$.
:::

Định nghĩa đọc như sau: gradient $g_j$ được tính tại tham số $\theta_{j-1}$ trước bước, trên mini-batch $B_j$ của bước đó, rồi quy tắc $\operatorname{Update}$ dùng $g_j$ và trạng thái phụ để trả tham số mới. Khi không cần nhắc tới trạng thái phụ, ta viết gọn $\theta_j=\operatorname{Update}(\theta_{j-1},g_j)$. Ba quy tắc của phần này khác nhau ở trạng thái phụ: hạ gradient ngẫu nhiên không có trạng thái phụ, RMSprop giữ một vector $v_j$, Adam giữ hai vector $m_j$, $v_j$, mỗi vector cùng kích thước với $\theta$. Hằng $\epsilon_{\mathrm{opt}}>0$ của RMSprop và Adam chỉ giữ mẫu số khác $0$; nó khác xác suất thăm dò $\epsilon_{\mathrm{exp}}$ của hành vi.

![Chuỗi năm ô từ trái sang phải: mini-batch B j, hàm mất mát L B j, gradient g j, ô Update của bộ tối ưu, tham số theta j. Nhãn theta j trừ 1 phía trên có hai mũi tên đi xuống: vào ô hàm mất mát, nơi gradient được tính, và vào ô Update. Một mũi tên nét đứt đi từ ô theta j lên trên rồi sang trái, kết thúc ở nhãn theta j trừ 1, ghi theta j thành theta j trừ 1 của bước sau; phía trên ghi j tăng thêm 1, với j bằng k opt sau khi tăng.](img/lec-08/optimizer-step.svg)

Hình vẽ một bước tối ưu: mini-batch $B_j$ cho hàm mất mát $L_{B_j}$, lấy gradient tại $\theta_{j-1}$ được $g_j$, quy tắc $\operatorname{Update}$ trả $\theta_j$. Nhãn $\theta_{j-1}$ phía trên có hai nhánh: vào ô hàm mất mát, vì gradient được tính tại $\theta_{j-1}$, và vào ô $\operatorname{Update}$. Mũi tên nét đứt đưa $\theta_j$ về vị trí của $\theta_{j-1}$ ở bước sau, khi $j$ tăng thêm $1$. Hình không có mũi tên nào từ bộ tối ưu tới đích hay tới bộ nhớ phát lại.

Theo Định nghĩa 08.15, bộ tối ưu chỉ nhận $g_j$ và trạng thái phụ; từ đó suy ra giới hạn của nó trong DQN. Đích $y_i$ được tính bằng $Q_{\theta^-}$ theo công thức của bước 7, dữ liệu do vòng thu thập ghi vào $\mathcal D$, và lớp hàm $\{Q_\theta\}$ do kiến trúc mạng quyết định; cả ba không phụ thuộc lựa chọn bộ tối ưu. Bộ tối ưu vẫn đổi quỹ đạo $\theta_0,\theta_1,\dots$, nên gián tiếp đổi hành vi $\epsilon_{\mathrm{exp}}$-tham lam, dữ liệu được ghi về sau và giá trị $\theta^-$ tại các mốc đồng bộ. Nhưng vì công thức đích, cơ chế thu thập và lớp hàm giữ nguyên, không bộ tối ưu nào loại được các nguồn bất ổn nằm ở ba thành phần đó; phần 6 phân tích các nguồn này.

**Trong thực hành.** Giá trị hàm mất mát trên mini-batch không phải thước đo chất lượng của chính sách. Đích tự đổi tại mỗi mốc đồng bộ và dữ liệu trong $\mathcal D$ đổi theo hành vi, nên $L_B$ có thể tăng khi chính sách tốt lên, và giảm khi chính sách không đổi; lợi tức đánh giá trên các lượt riêng mới đo chất lượng của chính sách.

#### Hạ gradient ngẫu nhiên (SGD)

Dạng đơn giản nhất của quy tắc $\operatorname{Update}$ không giữ trạng thái phụ và đi một bước ngược hướng gradient (Goodfellow, Bengio và Courville, 2016, §8.3.1).

::: definition Định nghĩa 08.16 (Hạ gradient ngẫu nhiên)
Hạ gradient ngẫu nhiên (stochastic gradient descent, SGD) với tốc độ học $\eta>0$ là bộ tối ưu theo Định nghĩa 08.15 có trạng thái phụ rỗng và
$$
\theta_j=\theta_{j-1}-\eta\,g_j,\qquad g_j=\nabla_\theta L_{B_j}(\theta_{j-1}).
$$
Khi tốc độ học đổi theo bước, ta viết $\eta_j$ thay cho $\eta$.
:::

Chữ "ngẫu nhiên" chỉ nguồn của $g_j$: gradient được tính trên một mini-batch rút ngẫu nhiên, không trên toàn bộ dữ liệu. Với $\theta^-$ cố định và mỗi lần rút có phân phối đều trên $\mathcal D$, kỳ vọng của $g_j$ theo phép rút bằng gradient của hàm mất mát trung bình trên cả bộ nhớ, $\tfrac1{\lvert\mathcal D\rvert}\sum_{e\in\mathcal D}(y_e-q_e)^2$, với $e$ chạy trên các mẫu chuyển trong $\mathcal D$, tại $\theta_{j-1}$; $g_j$ là một ước lượng có nhiễu của gradient đó. SGD không giữ trạng thái phụ, nên chi phí bộ nhớ ngoài $\theta$ bằng $0$. Đổi lại, mọi tọa độ của $\theta$ dùng cùng hệ số $\eta$, và bước theo mỗi tọa độ tỉ lệ với độ lớn của gradient theo tọa độ đó.

::: example Ví dụ 08.18 (Một bước hạ gradient trên ví dụ một tham số)
**Dữ kiện.** Như Ví dụ 08.5: $Q_\theta=\theta$, một mẫu chuyển với $R=1$, $\gamma=0{,}9$, $\theta_0=0$; mạng mục tiêu giữ $\theta^-=0$, nên đích $y=1+0{,}9\cdot0=1$ là hằng. Hàm mất mát $L(\theta)=(1-\theta)^2$; tốc độ học $\eta=0{,}25$.

**Tính.** $g_1=\nabla_\theta L(\theta_0)=-2(1-0)=-2$, và một bước hạ gradient cho $\theta_1=\theta_0-\eta g_1=0+0{,}25\cdot2=0{,}5$.

**Diễn giải.** Kết quả trùng bước bán gradient $\theta_1=\theta_0+\alpha(y-\theta_0)=0{,}5$ với $\alpha=0{,}5$ của Ví dụ 08.5: với hàm mất mát bình phương trên một mẫu, $\nabla_\theta L=-2(y-q)\nabla_\theta q$, nên hạ gradient với tốc độ học $\eta$ là cập nhật bán gradient với bước $\alpha=2\eta$.
:::

::: example Ví dụ 08.19 (Một hệ số bước cho hai tọa độ)
**Dữ kiện.** Hàm mất mát $L(\theta)=\tfrac12(100\,\theta_1^2+\theta_2^2)$, tham số hiện hành $\theta_{j-1}=(0{,}02;\,0{,}02)$, tốc độ học $\eta=0{,}1$.

**Tính.** $g_j=(100\cdot0{,}02;\,0{,}02)=(2;\,0{,}02)$, nên bước là $-\eta g_j=(-0{,}2;\,-0{,}002)$ và $\theta_j=(-0{,}18;\,0{,}018)$. Theo tọa độ thứ nhất, mỗi bước nhân $\theta_1$ với $1-100\eta=-9$; theo tọa độ thứ hai, với $1-\eta=0{,}9$.

**Diễn giải.** Với $\eta=0{,}1$, tọa độ thứ nhất phân kỳ. Muốn $\theta_1$ hội tụ về $0$, cần $\lvert1-100\eta\rvert<1$, tức $0<\eta<0{,}02$; khi đó tọa độ thứ hai giảm chưa tới $2\%$ mỗi bước, và sau $100$ bước vẫn còn hơn $0{,}98^{100}\approx13\%$ giá trị ban đầu. Một hệ số chung không hợp cho cả hai tọa độ khi độ cong theo hai tọa độ chênh $100$ lần; đây là bài toán có điều kiện kém (Goodfellow, Bengio và Courville, 2016, §4.3).
:::

**Trong thực hành.** SGD thường dùng với một lịch giảm tốc độ học $\eta_j$ định trước. Trong bài toán hồi quy với phân phối dữ liệu cố định, các điều kiện $\sum_j\eta_j=\infty$, $\sum_j\eta_j^2<\infty$ cùng giả thiết về hàm mất mát là cơ sở của các kết quả hội tụ cho SGD; trong DQN, đích đổi tại các mốc đồng bộ và dữ liệu đổi theo hành vi, nên các kết quả đó không áp dụng trực tiếp. Ví dụ 08.19 không cho phép suy ra SGD luôn kém hơn các phương pháp thích nghi; nó chỉ cho thấy SGD nhạy với tỉ lệ giữa các tọa độ, điều mà RMSprop dưới đây xử lý bằng một hệ số bước riêng cho từng tọa độ.

#### RMSprop

Ví dụ 08.19 cho thấy giới hạn của một hệ số bước chung: với gradient $g_j=(2;\,0{,}02)$, SGD đi hai bước chênh $100$ lần, và không có $\eta$ nào hợp cho cả hai tọa độ. Chúng ta cần một hệ số bước riêng cho từng tọa độ, tự điều chỉnh theo độ lớn điển hình của gradient tại tọa độ đó. RMSprop làm việc này (bài giảng gốc, trang 25; Goodfellow, Bengio và Courville, 2016, §8.5.2).

::: definition Định nghĩa 08.17 (RMSprop)
Cho tốc độ học $\eta>0$, hệ số suy giảm $\rho\in[0,1)$ và hằng $\epsilon_{\mathrm{opt}}>0$. RMSprop là bộ tối ưu theo Định nghĩa 08.15 với trạng thái phụ $v_j\in\mathbb R^d$, $v_0=0$, và tại bước $j=1,2,\dots$
$$
\begin{aligned}
v_j&=\rho\,v_{j-1}+(1-\rho)\,g_j\odot g_j,\\
\theta_j&=\theta_{j-1}-\eta\,g_j\oslash\bigl(\sqrt{v_j}+\epsilon_{\mathrm{opt}}\bigr),
\end{aligned}
$$
trong đó $\odot$ và $\oslash$ là phép nhân và phép chia theo từng tọa độ; căn bậc hai và phép cộng $\epsilon_{\mathrm{opt}}$ cũng lấy theo từng tọa độ.
:::

Tọa độ $k$ của $v_j$ là trung bình trượt có trọng số mũ của $g_{1,k}^2,\dots,g_{j,k}^2$: $v_{j,k}=(1-\rho)\sum_{\ell=1}^{j}\rho^{\,j-\ell}g_{\ell,k}^2$. Vì vậy $\sqrt{v_{j,k}}$ là độ lớn điển hình của gradient theo tọa độ $k$ trong khoảng $1/(1-\rho)$ bước gần nhất, và bước theo tọa độ đó là $\eta\,g_{j,k}/(\sqrt{v_{j,k}}+\epsilon_{\mathrm{opt}})$: gradient được chia cho độ lớn điển hình của chính nó. Một tọa độ có gradient lớn kéo dài nhận bước hiệu dụng nhỏ, một tọa độ có gradient nhỏ kéo dài nhận bước hiệu dụng lớn. Trạng thái phụ là một vector cùng kích thước với $\theta$.

Hệ số $\rho$ quyết định độ dài của trí nhớ: với $\rho=0$, $v_j=g_j\odot g_j$ và bước theo mỗi tọa độ là $\eta\,\operatorname{sign}(g_{j,k})$ khi bỏ qua $\epsilon_{\mathrm{opt}}$, nên mọi thông tin về độ lớn của gradient bị bỏ. Hằng $\epsilon_{\mathrm{opt}}$ giữ mẫu số dương: tại một tọa độ có gradient bằng $0$ ở mọi bước, $v_{j,k}=0$ và phép chia $0/0$ không xác định nếu thiếu $\epsilon_{\mathrm{opt}}$. Ở đây $\epsilon_{\mathrm{opt}}$ đặt ngoài căn; một số thư viện đặt $\epsilon_{\mathrm{opt}}$ trong căn, $\sqrt{v_j+\epsilon_{\mathrm{opt}}}$, và hai quy ước cho bước khác nhau khi $v_j$ nhỏ.

::: example Ví dụ 08.20 (Một bước RMSprop trên hai tọa độ)
**Dữ kiện.** Như Ví dụ 08.19: $L(\theta)=\tfrac12(100\,\theta_1^2+\theta_2^2)$, $\theta_0=(0{,}02;\,0{,}02)$, nên $g_1=(2;\,0{,}02)$. RMSprop với $\rho=0{,}9$, $v_0=0$, $\eta=0{,}005$; bỏ qua $\epsilon_{\mathrm{opt}}$.

**Tính.** $v_1=0{,}1\cdot(2^2;\,0{,}02^2)=(0{,}4;\,0{,}00004)$, $\sqrt{v_1}\approx(0{,}6325;\,0{,}006325)$, và $g_1\oslash\sqrt{v_1}=(\sqrt{10};\,\sqrt{10})\approx(3{,}162;\,3{,}162)$. Bước là $-\eta\,(3{,}162;\,3{,}162)\approx(-0{,}0158;\,-0{,}0158)$, nên $\theta_1\approx(0{,}0042;\,0{,}0042)$.

**Diễn giải.** Ở bước đầu, $v_1=(1-\rho)\,g_1\odot g_1$, nên mỗi tọa độ đi đúng $\eta/\sqrt{1-\rho}=\eta\sqrt{10}$ theo dấu gradient, dù hai gradient chênh $100$ lần. Với cùng $\eta=0{,}005$, SGD đưa tọa độ thứ hai đi $0{,}0001$, tức $0{,}5\%$ giá trị của nó, còn RMSprop đưa tọa độ đó đi khoảng $79\%$.
:::

**Trong thực hành.** Mnih và cộng sự (2015, mục Methods và Extended Data Table 1) huấn luyện DQN gốc bằng một biến thể của RMSprop với tốc độ học $0{,}00025$ và mini-batch $32$. RMSprop đổi tỉ lệ bước giữa các tọa độ và không cho bảo đảm hội tụ cho DQN.

#### Adam

RMSprop chuẩn hóa độ lớn của bước theo từng tọa độ, nhưng hướng bước vẫn là gradient tức thời $g_j$ của một mini-batch, nên dao động theo nhiễu của từng mini-batch, như Ví dụ 08.21 dưới đây. Adam lấy thêm trung bình trượt của chính gradient, và hiệu chỉnh độ lệch của hai trung bình trượt ở các bước đầu.

::: example Ví dụ 08.21 (Hai bước ngược chiều của RMSprop và Adam)
**Dữ kiện.** Xét một tọa độ của gradient trên hai mini-batch liên tiếp: $g_1=2$, $g_2=-1$. RMSprop với $\rho=0{,}9$, $v_0=0$; Adam với $\beta_1=0{,}9$, $\beta_2=0{,}999$, $m_0=v_0=0$; cùng tốc độ học $\eta$; bỏ qua $\epsilon_{\mathrm{opt}}$.

**Tính.** RMSprop: $v_1=0{,}1\cdot4=0{,}4$, bước $-\eta\cdot2/\sqrt{0{,}4}\approx-3{,}16\,\eta$; $v_2=0{,}9\cdot0{,}4+0{,}1\cdot1=0{,}46$, bước $-\eta\cdot(-1)/\sqrt{0{,}46}\approx+1{,}47\,\eta$. Adam: $m_1=0{,}2$, $v_1=0{,}004$, $\hat m_1=2$, $\hat v_1=4$, bước $-\eta\cdot2/2=-\eta$; $m_2=0{,}9\cdot0{,}2+0{,}1\cdot(-1)=0{,}08$, $v_2=0{,}999\cdot0{,}004+0{,}001\cdot1=0{,}004996$, nên $\hat m_2=0{,}08/0{,}19\approx0{,}42$, $\hat v_2=0{,}004996/0{,}001999\approx2{,}50$, bước $-\eta\cdot0{,}42/\sqrt{2{,}50}\approx-0{,}27\,\eta$.

**Diễn giải.** RMSprop đi theo dấu của gradient tức thời, nên bước thứ hai đổi chiều. Ở Adam, $\hat m_2$ còn dương vì trung bình trượt giữ phần lớn gradient đầu, nên bước thứ hai cùng chiều bước đầu và nhỏ hơn; hướng bước của Adam chỉ đổi khi $m_j$ đổi dấu.
:::

Adam (Kingma và Ba, 2015; Goodfellow, Bengio và Courville, 2016, §8.5.3) thêm trung bình trượt của chính gradient và phép hiệu chỉnh lệch cho cả hai trung bình trượt.

::: definition Định nghĩa 08.18 (Adam)
Cho tốc độ học $\eta>0$, hai hệ số suy giảm $\beta_1,\beta_2\in[0,1)$ và hằng $\epsilon_{\mathrm{opt}}>0$. Adam là bộ tối ưu theo Định nghĩa 08.15 với trạng thái phụ $(m_j,v_j)\in\mathbb R^d\times\mathbb R^d$, $m_0=v_0=0$, và tại bước $j=1,2,\dots$
$$
\begin{aligned}
m_j&=\beta_1m_{j-1}+(1-\beta_1)\,g_j, & v_j&=\beta_2v_{j-1}+(1-\beta_2)\,g_j\odot g_j,\\
\hat m_j&=\frac{m_j}{1-\beta_1^{\,j}}, & \hat v_j&=\frac{v_j}{1-\beta_2^{\,j}},\\
\theta_j&=\theta_{j-1}-\eta\,\hat m_j\oslash\bigl(\sqrt{\hat v_j}+\epsilon_{\mathrm{opt}}\bigr),
\end{aligned}
$$
với mọi phép toán trên vector lấy theo từng tọa độ.
:::

$m_j$ là trung bình trượt có trọng số mũ của các gradient, $v_j$ của bình phương gradient; $\beta^{\,j}$ là lũy thừa bậc $j$ của $\beta$. Vì $m_0=0$, $m_j=(1-\beta_1)\sum_{\ell=1}^{j}\beta_1^{\,j-\ell}g_\ell$ có tổng trọng số $1-\beta_1^{\,j}$ thay cho $1$; khi mọi gradient bằng nhau và bằng $g$, $m_j=(1-\beta_1^{\,j})\,g$, lệch về $0$ ở các bước đầu. Chia cho $1-\beta_1^{\,j}$ bù đúng độ lệch đó, và tương tự cho $v_j$. Khi $j$ lớn, $\beta^{\,j}\to0$ và phép hiệu chỉnh không còn tác dụng. Adam giữ hai vector trạng thái phụ cùng kích thước với $\theta$.

Bỏ trung bình trượt của gradient, tức $\beta_1=0$, thì $\hat m_j=g_j$ và Adam trở thành RMSprop có hiệu chỉnh lệch cho $v_j$. Bỏ hiệu chỉnh lệch thì bước đầu bị nhân với $(1-\beta_1)/\sqrt{1-\beta_2}$, như Ví dụ 08.22 dưới đây.

::: example Ví dụ 08.22 (Bước đầu của Adam có và không có hiệu chỉnh lệch)
**Dữ kiện.** Như Ví dụ 08.19 và 08.20: $g_1=(2;\,0{,}02)$, $\theta_0=(0{,}02;\,0{,}02)$, $\eta=0{,}005$. Adam với $\beta_1=0{,}9$, $\beta_2=0{,}999$, $m_0=v_0=0$; bỏ qua $\epsilon_{\mathrm{opt}}$.

**Tính.** $m_1=0{,}1\cdot g_1=(0{,}2;\,0{,}002)$ và $v_1=0{,}001\cdot(4;\,0{,}0004)=(0{,}004;\,0{,}0000004)$. Có hiệu chỉnh: $\hat m_1=m_1/0{,}1=g_1$, $\hat v_1=v_1/0{,}001=g_1\odot g_1$, nên $\hat m_1\oslash\sqrt{\hat v_1}=(1;\,1)$, bước là $-\eta\,(1;\,1)=(-0{,}005;\,-0{,}005)$ và $\theta_1=(0{,}015;\,0{,}015)$. Không hiệu chỉnh: $m_1\oslash\sqrt{v_1}=(0{,}2/0{,}0632;\,0{,}002/0{,}000632)\approx(3{,}16;\,3{,}16)$.

**Diễn giải.** Có hiệu chỉnh, bước đầu theo mỗi tọa độ là đúng $\eta$ theo dấu gradient. Không hiệu chỉnh, bước đầu lớn gấp $(1-\beta_1)/\sqrt{1-\beta_2}=0{,}1/\sqrt{0{,}001}\approx3{,}16$ lần, với cùng $\eta$.
:::

**Trong thực hành.** Adam được dùng rộng rãi trong thực hành hiện nay (bài giảng gốc, trang 28), kể cả nhiều cài đặt DQN về sau; DQN gốc dùng RMSprop. Công thức của Adam không tạo bảo đảm hội tụ cho DQN: đích đổi tại các mốc đồng bộ và dữ liệu đổi theo hành vi.

#### So sánh ba bộ tối ưu

Ba quy tắc cùng nhận gradient $g_j$ và trả $\theta_j$; chúng khác nhau ở trạng thái phụ, ở siêu tham số và ở lượng trừ khỏi $\theta_{j-1}$ theo mỗi tọa độ. Ký hiệu $m_j$, $v_j$ chỉ trung bình trượt của $g_j$ và của $g_j\odot g_j$; $\hat m_j$, $\hat v_j$ là hai trung bình đó sau hiệu chỉnh lệch.

| phương pháp | trạng thái phụ | siêu tham số cần chỉnh | lượng trừ khỏi $\theta_{j-1}$ |
|---|---|---|---|
| SGD (Định nghĩa 08.16) | không | $\eta$, lịch giảm | $\eta\,g_j$ |
| RMSprop (Định nghĩa 08.17) | $v_j$ | $\eta$, $\rho$, $\epsilon_{\mathrm{opt}}$ | $\eta\,g_j\oslash(\sqrt{v_j}+\epsilon_{\mathrm{opt}})$ |
| Adam (Định nghĩa 08.18) | $m_j$, $v_j$ | $\eta$, $\beta_1$, $\beta_2$, $\epsilon_{\mathrm{opt}}$ | $\eta\,\hat m_j\oslash(\sqrt{\hat v_j}+\epsilon_{\mathrm{opt}})$ |

Bảng đọc theo cột cuối. SGD đi bước tỉ lệ với gradient, nên bước theo mỗi tọa độ mang thang của gradient tại tọa độ đó; RMSprop và Adam chia cho độ lớn điển hình của gradient, nên bước theo mỗi tọa độ có thang xấp xỉ $\eta$, như Ví dụ 08.20 và 08.22. Vì thang bước khác nhau, cùng một giá trị $\eta$ không so sánh được giữa SGD và hai phương pháp thích nghi; mỗi bộ tối ưu cần được chỉnh $\eta$ riêng. Mỗi trạng thái phụ là một vector cùng kích thước với $\theta$, nên RMSprop tốn thêm bộ nhớ bằng một bản $\theta$, Adam bằng hai bản.

Không có lựa chọn thắng trong mọi bài toán; lựa chọn được quyết định bằng thí nghiệm có kiểm soát. Một thí nghiệm như vậy giữ cùng kiến trúc, ngân sách bước môi trường, lịch thăm dò và tập hạt giống ngẫu nhiên cho mọi bộ tối ưu, chỉnh siêu tham số của từng bộ tối ưu với cùng ngân sách, và báo lợi tức đánh giá cùng độ phân tán giữa nhiều lần chạy độc lập; giá trị hàm mất mát không phải tiêu chí, vì lý do đã nêu ở đầu mục. DQN gốc của Mnih và cộng sự (2015) dùng một biến thể của RMSprop.

**Giới hạn.** Lựa chọn bộ tối ưu không đổi công thức đích (bootstrap), cách thu thập dữ liệu (khác chính sách) hay lớp hàm (xấp xỉ hàm), nên không loại được các nguồn bất ổn đó. Không công thức cập nhật nào ở trên tạo bảo đảm hội tụ cho DQN.

**Kiểm tra nhanh.** Với $\beta_1=0$, Adam trùng quy tắc nào? RMSprop với $\rho=\beta_2$ có hiệu chỉnh lệch cho $v_j$.

Chúng ta đã có ba quy tắc đổi gradient $\nabla_\theta L_B$ thành bước tham số. Trên hàm $\tfrac12(100\,\theta_1^2+\theta_2^2)$, SGD không có hệ số bước chung hợp cho cả hai tọa độ, còn RMSprop và Adam đi bước đầu cùng cỡ ở cả hai tọa độ, $\eta\sqrt{10}$ và $\eta$. Các quy tắc này quyết định quỹ đạo của $\theta$, nhưng không đổi đích bootstrap, cơ chế thu thập dữ liệu khác chính sách hay việc dùng xấp xỉ hàm. Ba yếu tố đó là bộ ba bất ổn của Bài 07. Ở phần 6, chúng ta đặt bộ nhớ phát lại và mạng mục tiêu cạnh các nguồn bất ổn này, tính độ thay đổi của đích tại một mốc đồng bộ, và nêu phạm vi bảo đảm của DQN.

## 6. Bất ổn và phạm vi bảo đảm của DQN

<!-- note-topic-id: lec-08-topic-12 -->
### Hai nguồn bất ổn và hai cơ chế giảm

Q-learning dạng bảng hội tụ tới $q_*$ với xác suất một khi MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$, mọi cặp trạng thái–hành động được cập nhật vô hạn lần và bước học của từng cặp thỏa điều kiện Robbins–Monro (Bài 06). Khi bảng được thay bằng mạng nơ-ron, không còn định lý nào như vậy: bài giảng gốc (trang 29) ghi rằng huấn luyện có thể phân kỳ, và trong phần mở đầu, Mnih và cộng sự (2015) nhận xét rằng học tăng cường với một hàm xấp xỉ phi tuyến như mạng nơ-ron có thể mất ổn định, thậm chí phân kỳ. Bài giảng gốc nêu hai nguyên nhân chính: tương quan giữa các mẫu và mục tiêu không dừng. Ở phần 2 và phần 3, chúng ta đã dựng hai cơ chế, mạng mục tiêu và bộ nhớ phát lại, mỗi cơ chế nhắm vào một nguyên nhân. Chúng ta đặt hai nguyên nhân, hai cơ chế và điều mỗi cơ chế còn để lại vào cùng một bảng.

::: remark Nhận xét 08.19 (Hai nguồn bất ổn và hai cơ chế giảm)
Xét Q-learning với mạng giá trị hành động $Q_\theta$, học từ các mẫu chuyển do chính tác tử thu thập. Hai nguồn bất ổn sau có cơ chế giảm riêng, và mỗi cơ chế để lại một phần của nguồn:

| Nguồn bất ổn | Ví dụ có số | Cơ chế giảm | Điều còn lại |
|---|---|---|---|
| Tương quan giữa các mẫu liền nhau | Bốn gradient mẫu liền nhau, phương sai $\sigma^2$, tương quan $0{,}9^k$ khi cách $k$ bước: trung bình có phương sai $\approx0{,}881\,\sigma^2$, bằng trung bình của khoảng $1{,}1$ mẫu độc lập | Bộ nhớ phát lại: lưu $N$ mẫu chuyển gần nhất, rút đều mini-batch $b$ mẫu | Mẫu trong bộ nhớ không độc lập; phân phối của bộ nhớ đổi theo hành vi, vốn đổi theo $\theta$ |
| Đích phụ thuộc tham số đang học (bootstrap) | $Q_\theta=\theta$, $R=1$, $\gamma=0{,}9$, $\theta_0=0$, $\alpha=0{,}5$: một bước đưa $\theta$ lên $0{,}5$ và đích từ $1$ lên $1{,}45$ | Mạng mục tiêu: tính phần bootstrap bằng $\theta^-$, đồng bộ $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu | Đích của mọi mẫu chuyển đổi cùng lúc tại mốc đồng bộ |
:::

Hai nguồn nằm ở hai chỗ khác nhau của bước cập nhật. Nguồn thứ nhất nằm ở dữ liệu đưa vào hàm mất mát: hạ gradient ngẫu nhiên giảm phương sai theo cỡ mini-batch chỉ khi các gradient mẫu gần độc lập, và bốn mẫu liền nhau trong ví dụ của bảng giảm phương sai gần như không hơn một mẫu. Vấn đề này có cả khi đích là nhãn cố định, như hồi quy có giám sát trên một chuỗi thời gian. Nguồn thứ hai nằm ở chính nhãn: đích $y=R+\gamma\max_{a'}Q_\theta(O',a')$ chứa tham số đang cập nhật, nên mỗi bước kéo dự đoán về phía đích cũng dời đích; trong ví dụ một tham số, dự đoán tăng $0{,}5$ còn đích tăng $0{,}45$. Bài giảng gốc (trang 31) ghi rằng việc đuổi theo một đích đang di chuyển có thể dẫn tới dao động hoặc phân kỳ.

Tương quan giữa các mẫu không phải một yếu tố của bộ ba bất ổn (Định nghĩa 07.38). Bộ ba bất ổn gồm xấp xỉ hàm, bootstrap và học khác chính sách; nó nói về khả năng phân kỳ của chính quy tắc cập nhật TD, kể cả khi không có nhiễu lấy mẫu. Mệnh đề 07.37 là một phản ví dụ: với $x(s_1)=1$, $x(s_2)=2$, chỉ cập nhật chuyển $s_1\to s_2$ có phần thưởng $0$, $\gamma\in(\tfrac12,1)$ và $\alpha>0$, tham số thỏa $w_n=\bigl(1+\alpha(2\gamma-1)\bigr)^nw_0$ và tăng không chặn khi $w_0\ne0$. Mỗi bước dùng cùng một mẫu chuyển, nên cập nhật là tất định và trùng với cập nhật kỳ vọng theo phân phối cập nhật; không có nhiễu lấy mẫu để bộ nhớ phát lại giảm, và bộ nhớ chỉ chứa mẫu chuyển này cũng cho đúng dãy đó, vậy mà tham số vẫn phân kỳ. Ngược lại, tương quan làm tăng phương sai ngay cả trong hồi quy có giám sát, nơi không có bootstrap và không có chính sách nào. Nguồn thứ hai thì gắn với yếu tố bootstrap của bộ ba: đích di động là cách bootstrap biểu hiện khi đích và dự đoán dùng chung tham số.

Mỗi cơ chế chỉ tác động lên nguồn của nó. Mạng mục tiêu không đổi cách chọn mẫu, nên không giảm tương quan trong mini-batch. Bộ nhớ phát lại không đổi công thức đích, nên không làm đích đứng yên. Bỏ bộ nhớ phát lại, mỗi bước tối ưu dùng các mẫu vừa thu theo thứ tự thời gian, đúng tình huống của dòng thứ nhất trong bảng. Bỏ mạng mục tiêu, tức đặt $C=1$, đích được tính lại bằng $\theta$ mới sau mỗi bước, đúng tình huống của dòng thứ hai. Cả hai cơ chế đều giữ nguyên ba yếu tố xấp xỉ hàm, bootstrap và dữ liệu khác chính sách: mạng mục tiêu vẫn bootstrap, chỉ bằng một bản sao trễ của mạng, và bộ nhớ phát lại còn thêm một nguồn dữ liệu khác chính sách (Mệnh đề 08.8).

Một nhầm lẫn thường gặp là nói mạng mục tiêu tạo ra đích di động. Đích di động có sẵn khi đích tính bằng $\theta$; mạng mục tiêu giữ tham số tạo đích cố định giữa hai lần đồng bộ, nên trong khoảng đó đích của mỗi mẫu chuyển là một hằng số.

**Trong thực hành.** Hai cơ chế ứng với các siêu tham số của Thuật toán 08.13: dung lượng $N$, cỡ mini-batch $b$ và ngưỡng $N_{\mathrm{start}}$ của bộ nhớ phát lại; chu kỳ $C$ của mạng mục tiêu. Mnih và cộng sự (2015, Extended Data Table 3) so sánh bốn tổ hợp có hoặc không có bộ nhớ phát lại và mạng mục tiêu trên năm trò chơi Atari; tổ hợp dùng cả hai cho điểm cao nhất ở cả năm trò chơi. Đó là bằng chứng thực nghiệm về tác dụng của hai cơ chế trên các trò chơi đã thử, không phải bảo đảm hội tụ. Với dữ liệu khác chính sách lấy từ bộ nhớ lớn và mạng có hàng triệu tham số, cả ba yếu tố của bộ ba bất ổn vẫn có mặt.

**Kiểm tra nhanh.** Mạng mục tiêu có giảm tương quan giữa các mẫu trong một mini-batch không? Không; mini-batch do cách lấy mẫu từ bộ nhớ quyết định, còn mạng mục tiêu chỉ đổi tham số dùng để tính đích.

Như vậy, mỗi nguồn bất ổn có một cơ chế giảm và một phần còn lại. Phần còn lại của nguồn thứ hai có thể đo được: tại mỗi mốc đồng bộ, đích của mọi mẫu chuyển đổi cùng lúc. Ở mục tiếp theo, chúng ta tính độ thay đổi đó cho một mẫu chuyển cụ thể.

### Đích của một mẫu chuyển qua mốc đồng bộ

Nhận xét 08.19 để lại một phần của nguồn bất ổn thứ hai: tại mỗi mốc đồng bộ, đích của mọi mẫu chuyển đổi cùng lúc. Chúng ta đo độ thay đổi này. Nhắc lại hai định nghĩa của phần 2. Theo Định nghĩa 08.3, mạng mục tiêu $Q_{\theta^-}$ giữ $\theta^-$ cố định và nhận $\theta^-\leftarrow\theta$ sau mỗi bước tối ưu làm $k_{\mathrm{opt}}$ thành bội của $C$. Theo Định nghĩa 08.4, viết cho mẫu chuyển thứ $i$ của bộ nhớ, đích là $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$. Giữa hai lần đồng bộ, $\theta^-$ là hằng, nên với mỗi mẫu chuyển đã lưu, $y_i$ là một số cố định dù $\theta$ đổi sau mỗi bước tối ưu.

::: remark Nhận xét 08.20 (Độ thay đổi của đích tại mốc đồng bộ)
Xét mẫu chuyển $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ nằm trong bộ nhớ phát lại $\mathcal D$ và $\gamma\in[0,1)$. Tại một mốc đồng bộ, gọi $\theta^-$ là tham số của mạng mục tiêu ngay trước mốc và $\theta$ là tham số của mạng trực tuyến tại mốc. Ngay sau phép gán $\theta^-\leftarrow\theta$, đích của mẫu chuyển đổi một lượng
$$
\Delta y_i=\gamma(1-Z_i)\Bigl[\max_{a'\in\mathcal A}Q_{\theta}(O'_i,a')-\max_{a'\in\mathcal A}Q_{\theta^-}(O'_i,a')\Bigr].
$$
Giữa hai mốc đồng bộ liên tiếp, đích của mẫu chuyển không đổi.
:::

Nhận xét suy ra trực tiếp từ Định nghĩa 08.4: $R_i$, $Z_i$ và $O'_i$ là các thành phần đã lưu nên không đổi, và chỉ tham số dùng trong phép cực đại đổi từ $\theta^-$ sang $\theta$; trừ hai biểu thức của đích, phần thưởng triệt tiêu. Ba điểm trong công thức cần đọc riêng. Mặt nạ $1-Z_i$ làm $\Delta y_i=0$ với mẫu chuyển kết thúc: đích của chúng bằng $R_i$ ở mọi thời điểm. Cờ cắt ngắn $U_i$ không xuất hiện, vì mẫu chuyển bị cắt ngắn vẫn bootstrap từ $O'_i$ và cũng đổi đích tại mốc. Độ lớn của $\Delta y_i$ là $\gamma$ nhân hiệu hai giá trị cực đại tại cùng quan sát $O'_i$, nên phụ thuộc quãng đường $\theta$ đi được trong $C$ bước tối ưu kể từ lần đồng bộ trước.

::: example Ví dụ 08.23 (Mẫu 1 qua mốc đồng bộ)
**Dữ kiện.** Mini-batch hai mẫu chuyển với $\gamma=0{,}9$. Mẫu 1: $R_1=1$, $Z_1=0$, và ngay trước mốc đồng bộ $\max_{a'}Q_{\theta^-}(O'_1,a')=4$. Mẫu 2: $R_2=-2$, $Z_2=1$, $\max_{a'}Q_{\theta^-}(O'_2,a')=100$. Giả sử tại mốc, mạng trực tuyến cho $\max_{a'}Q_\theta(O'_1,a')=5$.

**Tính.** Trước mốc, $y_1=1+0{,}9\cdot4=4{,}6$ và $y_2=-2+0{,}9\cdot0\cdot100=-2$. Sau $\theta^-\leftarrow\theta$, $y_1=1+0{,}9\cdot5=5{,}5$. Theo Nhận xét 08.20, $\Delta y_1=0{,}9\,(1-0)(5-4)=0{,}9$ và $\Delta y_2=0{,}9\,(1-1)\,[\cdot]=0$, nên $y_2=-2$ dù $\max_{a'}Q_\theta(O'_2,a')$ nhận giá trị nào.

**Diễn giải.** Sáu thành phần đã lưu của mẫu 1 không đổi, nhưng nhãn hồi quy của nó tăng $0{,}9$ sau mốc. Mẫu kết thúc giữ nhãn cũ.
:::

![Trục ngang là bộ đếm bước tối ưu k opt với các mốc 0, C và 2C; trục dọc là đích y 1 của mẫu chuyển thứ nhất. Từ 0 đến C, đường đậm nằm ngang ở 4,6, ghi max theo a phẩy của Q theta trừ tại O phẩy 1 bằng 4. Tại mốc C có vòng tròn rỗng ghi theta trừ gán bằng theta; đường đậm đi lên bằng nét đứt tới 5,5 rồi nằm ngang tới 2C, ghi max theo a phẩy của Q theta tại O phẩy 1 bằng 5. Ngoặc dọc tại mốc C ghi độ thay đổi delta y 1 bằng 0,9.](img/lec-08/target-sync-step.svg)

Hình vẽ đích $y_1$ của Ví dụ 08.23 theo bộ đếm bước tối ưu $k_{\mathrm{opt}}$. Từ $0$ đến $C$, đường nằm ngang ở $4{,}6$: trong khoảng này mỗi bước tối ưu là hồi quy về một nhãn đứng yên. Tại mốc $C$ (vòng tròn rỗng), phép gán $\theta^-\leftarrow\theta$ đưa đích lên $5{,}5$; ngoặc dọc ghi độ thay đổi $0{,}9$. Từ $C$ đến $2C$, đích lại nằm ngang ở mức mới. Đường đích có dạng bậc thang, giống đường của $\theta^-$ trong hình ở mục mạng mục tiêu, vì đích chỉ phụ thuộc $\theta$ qua $\theta^-$.

Đích trong DQN dễ bị coi là nhãn cố định như trong học có giám sát. Mạng mục tiêu giữ đích đứng yên trong từng khoảng $C$ bước, nhưng không giữ mãi: sau mỗi mốc, mọi mẫu chuyển chưa kết thúc nhận nhãn mới. Chu kỳ $C$ vì vậy là một đánh đổi. $C$ lớn cho các khoảng hồi quy dài với nhãn đứng yên, nhưng nhãn được tính từ một mạng cũ hơn và $\theta$ có nhiều bước để đi xa $\theta^-$, nên độ thay đổi tại mốc thường lớn hơn. $C$ nhỏ cho nhãn mới hơn nhưng đổi thường xuyên hơn; với $C=1$, đích tính lại sau mỗi bước, như Ví dụ 08.5. Không có giá trị $C$ nào được suy ra từ lý thuyết; Mnih và cộng sự (2015, Extended Data Table 1) dùng $C=10\,000$ bước tối ưu, chọn bằng thí nghiệm.

**Trong thực hành.** Bộ nhớ phát lại chỉ lưu sáu thành phần của mẫu chuyển, không lưu đích; đích được tính lại bằng $\theta^-$ hiện hành mỗi khi mẫu chuyển được rút vào một mini-batch (Thuật toán 08.13, bước 7). Vì vậy một mẫu chuyển cũ nhận đích mới mà không cần ghi lại vào $\mathcal D$, và độ thay đổi của Nhận xét 08.20 xuất hiện ở lần rút đầu tiên sau mốc. Mạng mục tiêu làm đích đổi theo từng đợt thay vì sau mỗi bước, nhưng không làm đích cố định vĩnh viễn và không tạo bảo đảm hội tụ.

**Kiểm tra nhanh.** Mẫu chuyển bị cắt ngắn, $U_i=1$, $Z_i=0$, có đổi đích tại mốc đồng bộ không? Có; mặt nạ chỉ chứa $Z_i$, nên mẫu này vẫn bootstrap từ $O'_i$ và $\Delta y_i$ tính như mẫu 1.

Như vậy, mạng mục tiêu biến sự thay đổi sau mỗi bước của đích thành các lần thay đổi rời rạc tại mốc đồng bộ, với độ lớn đo được bằng Nhận xét 08.20. Bộ nhớ phát lại và mạng mục tiêu đều không chạm tới ba thành phần xấp xỉ hàm, bootstrap và dữ liệu khác chính sách. Ở mục tiếp theo, chúng ta nhắc lại bộ ba bất ổn của Bài 07 và kiểm từng thành phần của nó trong DQN.

### Bộ ba bất ổn trong DQN

Bộ nhớ phát lại giảm tương quan giữa các mẫu, mạng mục tiêu làm đích đổi theo từng đợt. Cả hai giữ nguyên cách DQN biểu diễn giá trị, cách tính đích và nguồn của dữ liệu. Bài 07 đã chỉ ra rằng ba thành phần này, khi cùng có mặt, đủ để một phương pháp học giá trị mất bảo đảm hội tụ. Chúng ta nhắc lại định nghĩa đó và kiểm từng yếu tố trong DQN.

::: definition Định nghĩa 07.38 (Bộ ba bất ổn, nhắc lại từ Bài 07)
Một phương pháp học giá trị có bộ ba bất ổn (deadly triad) khi có đồng thời:

- **xấp xỉ hàm:** tham số dùng chung, một cập nhật đổi nhiều dự đoán;
- **bootstrap:** mục tiêu cập nhật chứa ước lượng hiện tại;
- **học khác chính sách:** phân phối các mẫu chuyển dùng để cập nhật khác phân phối do chính sách đích sinh ra.
:::

Bài 07 dùng định nghĩa này cùng một phản ví dụ. Trong Mệnh đề 07.37, hàm giá trị tuyến tính $\hat v(s,w)=x(s)\,w$ có $x(s_1)=1$, $x(s_2)=2$; chỉ chuyển $s_1\to s_2$ với phần thưởng $0$ được cập nhật bằng TD(0), với $\gamma\in(\tfrac12,1)$ và $\alpha>0$. Khi đó $w_n=\bigl(1+\alpha(2\gamma-1)\bigr)^nw_0$, nên $\lvert w_n\rvert\to\infty$ khi $w_0\ne0$. Ví dụ có đủ ba yếu tố: một tham số cho hai trạng thái, mục tiêu chứa $\hat v(s_2,w)$, và phân phối cập nhật chỉ gồm một chuyển, khác phân phối theo chính sách.

Ba yếu tố có mặt trong DQN như sau.

| yếu tố | dạng trong DQN | cơ chế của DQN có bỏ yếu tố này không |
|---|---|---|
| xấp xỉ hàm | mạng $Q_\theta$: một vector $\theta\in\mathbb R^d$ cho mọi cặp $(o,a)$, với $d$ nhỏ hơn nhiều số cặp | không; mạng mục tiêu có cùng kiến trúc |
| bootstrap | đích $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$ chứa ước lượng của chính mạng | không; mạng mục tiêu chỉ làm tham số trong đích trễ đi |
| học khác chính sách | chính sách đích tham lam theo giá trị của mạng; mẫu trong $\mathcal D$ do hành vi $\epsilon_{\mathrm{exp}}$-tham lam theo các phiên bản $\theta$ cũ sinh ra | không; bộ nhớ phát lại thêm nguồn khác chính sách thứ hai (Mệnh đề 08.8) |

::: remark Nhận xét 08.21 (Phạm vi bảo đảm của DQN)
**Giả thiết.** Thuật toán 08.13 với mạng giá trị hành động $Q_\theta$ có tham số dùng chung, đích $y_i$ tính bằng mạng mục tiêu $Q_{\theta^-}$, và mini-batch rút đều từ bộ nhớ phát lại $\mathcal D$ do hành vi $\epsilon_{\mathrm{exp}}$-tham lam ghi.

**Kết luận.** Thuật toán có đủ ba yếu tố của Định nghĩa 07.38, nên không có bảo đảm hội tụ tổng quát: lớp phương pháp có đủ ba yếu tố có ví dụ phân kỳ (Mệnh đề 07.37 cho TD(0) tuyến tính; Sutton và Barto, 2018, §11.2 cho ví dụ của Baird).

**Điều kiện áp dụng.** Kết luận nói về bảo đảm cho mọi bài toán, mọi kiến trúc và mọi siêu tham số; nó không nói một lần chạy cụ thể sẽ phân kỳ.

**Phạm vi.** Các bảo đảm đã biết cho học giá trị với xấp xỉ hàm hoặc bỏ một yếu tố (Định lý 07.29 cho TD(0) tuyến tính theo chính sách), hoặc thêm giả thiết mạnh hơn tính biểu diễn được. Riêng $q_*$ thuộc lớp hàm và dữ liệu bao phủ mọi trạng thái thì chưa đủ: trong ví dụ của Baird, hàm giá trị đúng bằng $0$ biểu diễn được với $w=0$, mọi trạng thái được cập nhật đều, vậy mà tham số tăng không chặn (Sutton và Barto, 2018, §11.2). Bài giảng gốc (trang 11) nêu thêm giả thiết độ ổn định của cập nhật. DQN tổng quát không có các giả thiết đó ở dạng kiểm chứng được.
:::

Bốn phần của nhận xét có vai trò khác nhau. Giả thiết liệt kê đúng ba thành phần của thuật toán ứng với ba yếu tố; bộ nhớ phát lại và mạng mục tiêu có trong giả thiết nhưng không xuất hiện trong kết luận, vì chúng không bỏ yếu tố nào. Bỏ một yếu tố cho các trường hợp Bài 07 đã biết: bỏ xấp xỉ hàm được Q-learning dạng bảng, hội tụ dưới các giả thiết của Bài 06; bỏ học khác chính sách được TD(0) tuyến tính theo chính sách, hội tụ theo Định lý 07.29; bỏ bootstrap được Monte Carlo, với dữ liệu khác chính sách phải dùng lấy mẫu quan trọng và chịu phương sai lớn. DQN không bỏ yếu tố nào trong ba. Phần phạm vi nối với bài giảng gốc (trang 13): không có bảo đảm độ phức tạp mẫu tổng quát cho Q-learning dùng mạng nhiều tầng, và thành công thực nghiệm của DQN dựa vào các kỹ thuật như bộ nhớ phát lại và mạng mục tiêu; khoảng cách giữa lý thuyết và thực hành vẫn là bài toán mở.

Một nhầm lẫn thường gặp là đọc "không có bảo đảm hội tụ" thành "DQN phân kỳ". Nhận xét 07.39 của Bài 07 phân biệt hai điều: "có thể phân kỳ" nói về một lớp phương pháp, có ví dụ phân kỳ; nó không dự báo kết quả của một lần chạy. Nhầm lẫn ngược lại là coi bộ nhớ phát lại và mạng mục tiêu là lời giải của bộ ba bất ổn; chúng giảm hai nguồn bất ổn của Nhận xét 08.19, còn ba yếu tố vẫn nguyên.

**Trong thực hành.** Dấu hiệu của phân kỳ là giá trị dự đoán $Q_\theta$ hoặc chuẩn $\lVert\theta\rVert$ tăng không chặn qua các lần đánh giá; một chính sách kém trong khi giá trị và tham số vẫn bị chặn là hiện tượng khác (Nhận xét 07.39). Trong thí nghiệm, chúng ta theo dõi cả lợi tức đánh giá lẫn độ lớn của giá trị dự đoán trên một tập quan sát cố định, và chạy nhiều hạt giống ngẫu nhiên, vì kết luận của Nhận xét 08.21 là về khả năng phân kỳ chứ không về một lần chạy.

**Kiểm tra nhanh.** Bộ nhớ phát lại có bỏ yếu tố học khác chính sách không? Không; mẫu cũ trong $\mathcal D$ do các phiên bản $\theta$ trước sinh ra, nên bộ nhớ còn thêm một nguồn khác chính sách bên cạnh phép thăm dò $\epsilon_{\mathrm{exp}}$-tham lam.

Như vậy, hai cơ chế của DQN giảm hai nguồn bất ổn, còn ba yếu tố của bộ ba bất ổn vẫn có mặt và DQN không có bảo đảm hội tụ tổng quát. Câu hỏi còn lại là mạng mục tiêu thay đổi gì trong chính phản ví dụ của Bài 07. Ở mục tiếp theo, chúng ta thêm mạng mục tiêu vào ví dụ hai trạng thái và tính hệ số tăng của tham số sau mỗi chu kỳ đồng bộ.

### Ví dụ: hai trạng thái với mạng mục tiêu

Nhận xét 08.21 nói rằng mạng mục tiêu không bỏ yếu tố nào của bộ ba bất ổn. Chúng ta kiểm khẳng định này trên chính phản ví dụ của Bài 07, bằng cách tính lại cập nhật khi mục tiêu dùng một tham số giữ cố định $C$ bước rồi đồng bộ, như mạng mục tiêu của DQN. Ví dụ là TD(0) dự đoán với hàm giá trị tuyến tính, không phải Q-learning; nó có đủ ba yếu tố và đủ nhỏ để tính tay.

::: example Ví dụ 08.24 (Hai trạng thái dùng chung tham số, có và không có mạng mục tiêu)
**Dữ kiện.** Hai trạng thái $s_1$, $s_2$ với đặc trưng $x(s_1)=1$, $x(s_2)=2$ và hàm giá trị tuyến tính một tham số $\hat v(s,w)=x(s)\,w$, nên $\hat v(s_1)=w$ và $\hat v(s_2)=2w$. Chỉ chuyển $s_1\to s_2$ với phần thưởng $R=0$ được cập nhật, bằng TD(0) bán gradient với $\gamma=0{,}9$, bước học $\alpha=0{,}1$:
$$
w\leftarrow w+\alpha\bigl[R+\gamma\,\hat v(s_2)-\hat v(s_1)\bigr]\,x(s_1).
$$

**Tính, không có mạng mục tiêu.** Mục tiêu dùng $w$ hiện hành: $w_{n+1}=w_n+0{,}1\,(0{,}9\cdot2w_n-w_n)=(1+0{,}1\cdot0{,}8)\,w_n=1{,}08\,w_n$, nên $w_n=1{,}08^n\,w_0$.

**Tính, có mạng mục tiêu.** Mục tiêu dùng tham số $w^-$ giữ cố định trong $C$ bước, $\hat v(s_2)=2w^-$, và bắt đầu chu kỳ với $w_0=w^-$. Mục tiêu là hằng $1{,}8\,w^-$, nên
$$
\begin{aligned}
w_{k+1}-1{,}8\,w^-&=w_k+0{,}1\,(1{,}8\,w^--w_k)-1{,}8\,w^-=0{,}9\,(w_k-1{,}8\,w^-),\\
w_C&=1{,}8\,w^-+0{,}9^C\,(w^--1{,}8\,w^-)=(1{,}8-0{,}8\cdot0{,}9^C)\,w^-.
\end{aligned}
$$
Sau chu kỳ, đồng bộ $w^-\leftarrow w_C$; mỗi chu kỳ nhân tham số với $1{,}8-0{,}8\cdot0{,}9^C$.

| $C$ | hệ số mỗi chu kỳ $1{,}8-0{,}8\cdot0{,}9^C$ | không có mạng mục tiêu, $1{,}08^C$ | hệ số tương đương mỗi bước |
|---|---|---|---|
| $1$ | $1{,}080$ | $1{,}080$ | $1{,}080$ |
| $5$ | $1{,}328$ | $1{,}469$ | $1{,}058$ |
| $10$ | $1{,}521$ | $2{,}159$ | $1{,}043$ |
| $100$ | $1{,}800$ | $\approx2{,}2\cdot10^{3}$ | $1{,}006$ |

**Diễn giải.** Với $C=1$, hai cách tính trùng nhau ($1{,}8-0{,}72=1{,}08$), đúng như mạng mục tiêu đồng bộ sau mỗi bước. Hệ số mỗi chu kỳ tăng theo $C$ vì $0{,}9^C$ giảm, nên nhỏ nhất bằng $1{,}08$ và tiến tới $1{,}8$ khi $C\to\infty$. Vì hệ số luôn lớn hơn $1$, $\lvert w\rvert\to\infty$ khi $w_0\ne0$ với mọi $C\ge1$: mạng mục tiêu làm tham số tăng chậm hơn tính theo bước, nhưng không ngăn phân kỳ.
:::

![Hai trạng thái là hai vòng tròn, s 1 bên trái và s 2 bên phải, nối bằng mũi tên từ s 1 sang s 2 ghi phần thưởng R bằng 0. Bên trái s 1 ghi đặc trưng x của s 1 bằng 1 và giá trị xấp xỉ v mũ của s 1 bằng w. Bên phải s 2 ghi x của s 2 bằng 2 và v mũ của s 2 bằng 2w. Hai giá trị dùng chung một tham số w.](img/lec-08/two-state-shared.svg)

Hình vẽ dữ kiện của Ví dụ 08.24: mũi tên $s_1\to s_2$ là chuyển duy nhất được cập nhật, và hai nhãn hai bên cho biết hai giá trị $w$, $2w$ cùng phụ thuộc một tham số. Mỗi cập nhật kéo $\hat v(s_1)$ về phía $0{,}9\cdot\hat v(s_2)$; vì $\hat v(s_2)=2\hat v(s_1)$, mục tiêu luôn bằng $1{,}8$ lần giá trị đang được cập nhật, nên kéo về mục tiêu cũng đẩy mục tiêu ra xa.

Cơ chế phân kỳ nằm ở chỗ mục tiêu $1{,}8\,w^-$ có độ lớn gấp $1{,}8$ lần $w^-$. Mạng mục tiêu giữ mục tiêu đứng yên trong $C$ bước, nên trong mỗi chu kỳ $w$ hội tụ về $1{,}8\,w^-$ với hệ số $0{,}9$ mỗi bước; nhưng sau đồng bộ, mục tiêu mới là $1{,}8\,w_C$, lại gấp $1{,}8$ lần tham số hiện hành. Ba yếu tố vẫn có mặt: một tham số cho hai trạng thái, mục tiêu chứa ước lượng của chính mô hình, và phân phối cập nhật chỉ gồm một chuyển. Bỏ yếu tố khác chính sách, tức cập nhật mọi chuyển theo phân phối dừng của một chính sách, đưa bài toán về trường hợp của Định lý 07.29: TD(0) tuyến tính theo chính sách hội tụ khi các giả thiết của định lý thỏa.

Đặt hệ số mỗi chu kỳ $1{,}521$ cạnh hệ số mỗi bước $1{,}08$ có thể dẫn tới kết luận sai rằng mạng mục tiêu làm bất ổn nặng hơn. So đúng là so trên cùng số bước: sau $10$ bước, có mạng mục tiêu nhân $1{,}521$, không có nhân $2{,}159$; tính theo mỗi bước là $1{,}043$ so với $1{,}08$.

**Trong thực hành.** Ví dụ giải thích vì sao mạng mục tiêu được mô tả là làm chậm sự thay đổi của đích chứ không bảo đảm ổn định: trong một bài toán có đủ ba yếu tố và có hướng phân kỳ, chu kỳ $C$ lớn hơn chỉ làm tốc độ tăng mỗi bước nhỏ đi. Đây là căn cứ cho phần phạm vi của Nhận xét 08.21: tác dụng ổn định của mạng mục tiêu trên các bài toán Atari là kết quả thực nghiệm, còn bảo đảm tổng quát không có.

**Kiểm tra nhanh.** Với $C=2$, hệ số mỗi chu kỳ bằng bao nhiêu và có phân kỳ không? $1{,}8-0{,}8\cdot0{,}81=1{,}152>1$, nên vẫn phân kỳ; so với $1{,}08^2=1{,}1664$ khi không có mạng mục tiêu.

Đến đây chúng ta có ba kết quả của phần 6. Hai cơ chế của DQN giảm hai nguồn bất ổn: bộ nhớ phát lại giảm tương quan, mạng mục tiêu giữ đích đứng yên giữa hai mốc đồng bộ, và tại mốc đích của mẫu 1 đổi $0{,}9$. DQN vẫn có đủ ba yếu tố của bộ ba bất ổn, nên không có bảo đảm hội tụ tổng quát. Trong phản ví dụ hai trạng thái, mạng mục tiêu hạ hệ số tăng mỗi bước từ $1{,}08$ xuống $1{,}043$ khi $C=10$, nhưng không ngăn phân kỳ. Tác dụng của từng cơ chế vì vậy phải đo bằng thí nghiệm; Bài tập 08.3 thiết kế một thí nghiệm loại bỏ như vậy, và phần 7 dùng các kết quả này để trả lời vấn đề trung tâm.

## 7. Tổng kết và chuyển tiếp

<!-- note-topic-id: lec-08-topic-15 -->
### Kết quả và giả thiết của bài

Chúng ta gom các kết quả của phần 2 đến phần 6 vào một bảng. Mỗi hàng đặt một kết quả cạnh giả thiết mà thiếu nó thì công thức sai nghĩa hoặc kết luận vượt quá bằng chứng.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Mạng giá trị hành động (Định nghĩa 08.1) | $\mathcal A$ hữu hạn; quan sát đủ Markov (với Atari: bốn khung xếp chồng, Nhận xét 08.2) | $\mathbf q_\theta(o)\in\mathbb R^{\lvert\mathcal A\rvert}$, $Q_\theta(o,a)=[\mathbf q_\theta(o)]_a$ |
| Mạng mục tiêu và đồng bộ (Định nghĩa 08.3) | $\theta^-$ cùng kiến trúc, không nhận gradient; đồng bộ sau bước tối ưu, khi $k_{\mathrm{opt}}$ vừa tăng là bội của $C$ | $\theta^-\leftarrow\theta$ khi $k_{\mathrm{opt}}\bmod C=0$ |
| Đích hồi quy (Định nghĩa 08.4, 08.6) | $Z_i$ chỉ ghi kết thúc của MDP; cắt ngắn $U_i=1$ vẫn bootstrap | $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$ |
| Bộ nhớ phát lại (Định nghĩa 08.7, Nhận xét 08.9) | rút đều; tối ưu chỉ khi $\lvert\mathcal D\rvert\ge N_{\mathrm{start}}$ | giảm tương quan ngắn hạn; mẫu không độc lập, phân phối của $\mathcal D$ đổi theo hành vi |
| Đích không cần tỉ số lấy mẫu quan trọng (Mệnh đề 08.8) | đích một bước; quan sát đủ Markov, động lực không đổi theo thời gian; $\theta^-$ cố định | $\mathbb E[y_i\mid O_i,A_i]=(\mathcal TQ_{\theta^-})(O_i,A_i)$ với mọi hành vi đã sinh mẫu |
| Hàm mất mát và gradient (Định nghĩa 08.10, 08.12) | đích trong $\operatorname{sg}$; $q_i$ là giá trị của hành động đã lưu $A_i$ | $L_B=\tfrac1b\sum_i(y_i-q_i)^2$, $\nabla_\theta L_B=\tfrac2b\sum_i(q_i-y_i)\nabla_\theta q_i$ |
| Thuật toán DQN (Thuật toán 08.13) | hai bộ đếm $t$, $k_{\mathrm{opt}}$ tách biệt; cập nhật, tăng $k_{\mathrm{opt}}$, rồi mới kiểm $C$ | thu thập, lưu, rút mini-batch, cập nhật, đồng bộ |
| Bộ tối ưu (Định nghĩa 08.15–08.18) | $g_j$ tính tại $\theta_{j-1}$ trên $B_j$; $j=k_{\mathrm{opt}}$ sau khi tăng | $\theta_j=\operatorname{Update}(\theta_{j-1},g_j)$: SGD, RMSprop, Adam |
| Độ thay đổi của đích (Nhận xét 08.20) | ngay sau $\theta^-\leftarrow\theta$, với $\theta^-$ trước mốc | $\Delta y_i=\gamma(1-Z_i)\bigl[\max_{a'}Q_\theta(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\bigr]$ |
| Phạm vi bảo đảm (Nhận xét 08.21) | đủ xấp xỉ hàm, bootstrap, học khác chính sách | không có bảo đảm hội tụ tổng quát; hai cơ chế không bỏ yếu tố nào |

Bảng đọc theo hàng. Ba hàng đầu xác định nhãn hồi quy của mỗi mẫu chuyển; hai hàng kế xác định dữ liệu đưa vào bước tối ưu và lý do đích không cần trọng số; ba hàng tiếp theo xác định một bước cập nhật trong thuật toán; hai hàng cuối nói đích đổi bao nhiêu tại mốc đồng bộ và thuật toán được bảo đảm đến đâu. Các cột giả thiết là chỗ thường sai trong cài đặt: gộp $Z$ với $U$ vào mặt nạ, để gradient đi qua đích, lấy cực đại của $\mathbf q_\theta(O_i)$ thay cho giá trị của $A_i$, hoặc kiểm $C$ trước khi tăng $k_{\mathrm{opt}}$.

### So sánh Q-learning bảng, tuyến tính và DQN

Đến đây chúng ta có ba phương pháp học $q_*$ từ mẫu chuyển: Q-learning dạng bảng (Thuật toán 06.16), Q-learning bán gradient tuyến tính (Định nghĩa 07.35, Thuật toán 07.36) và DQN (Thuật toán 08.13). Cả ba dùng đích một bước có phép cực đại và thu dữ liệu bằng hành vi $\epsilon_{\mathrm{exp}}$-tham lam, tức hành vi $\varepsilon$-tham lam của Bài 06–07. Muốn biết DQN đổi những gì so với hai phương pháp trước, và vì sao các thay đổi đó không đem theo định lý hội tụ của dạng bảng, chúng ta đặt ba phương pháp cạnh nhau trên cùng các tiêu chí.

Với mẫu chuyển $(O,A,R,O',Z)$, cả ba phương pháp dùng đích

$$
y=R+\gamma(1-Z)\max_{a'}\hat Q(O',a'),
$$

trong đó $\hat Q$ lần lượt là bảng $Q$ trước cập nhật, hàm tuyến tính $x(o,a)^\top w$ với $w$ hiện tại, và mạng mục tiêu $Q_{\theta^-}$. Với bảng và hàm tuyến tính, quan sát là trạng thái, $O=S$ và $O'=S'$. Mặt nạ $1-Z$ thay cho quy ước $Q(s,\cdot)=0$ tại trạng thái kết thúc, và ở cả ba phương pháp, mẫu bị cắt ngắn vẫn giữ phần bootstrap.

| Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng |
|---|---|---|---|
| Q-learning dạng bảng (Thuật toán 06.16) | $Q(S,A)\leftarrow Q(S,A)+\alpha_n(S,A)\bigl(y-Q(S,A)\bigr)$; chỉ ô $(S,A)$ đổi | mẫu chuyển vừa thu, dùng cho đúng một cập nhật | sau số cập nhật định trước |
| Q-learning bán gradient tuyến tính (Thuật toán 07.36) | $w\leftarrow w+\alpha_n\bigl(y-x(S,A)^\top w\bigr)\,x(S,A)$; đổi các thành phần của $w$ ứng với thành phần khác $0$ của $x(S,A)$ | mẫu chuyển vừa thu, dùng cho đúng một cập nhật | sau số lượt định trước |
| DQN (Thuật toán 08.13) | $\theta\leftarrow\operatorname{Update}(\theta,\nabla_\theta L_B)$, $L_B=\tfrac1b\sum_i(y_i-q_i)^2$ với $y_i$ trong $\operatorname{sg}$; $\theta^-\leftarrow\theta$ khi $k_{\mathrm{opt}}\bmod C=0$ | khi $\lvert\mathcal D\rvert\ge N_{\mathrm{start}}$, mỗi $F$ bước môi trường rút đều $b$ mẫu từ $\mathcal D$, nơi giữ tối đa $N$ mẫu gần nhất | sau $T$ bước môi trường (Thuật toán 08.13); trong thực hành có thể dừng sớm khi lợi tức đánh giá đạt ngưỡng chọn trước |

Trước hết, ba phương pháp khác nhau ở phạm vi của một cập nhật. Với bảng, một mẫu chỉ đổi ô của chính nó. Với hàm tuyến tính, một mẫu đổi $w$ dùng chung, nên đổi giá trị của mọi cặp có đặc trưng chung với $(S,A)$. Với DQN, gradient đi qua mọi tầng của mạng, nên một mini-batch nói chung đổi giá trị tại mọi quan sát.

Phép cực đại trong đích cũng được đọc ở ba chỗ: bảng chưa cập nhật, $w$ hiện tại, và $\theta^-$ giữ cố định giữa hai lần đồng bộ. Chỉ DQN tách tham số tạo đích khỏi tham số được cập nhật.

Chỗ khác thứ hai nằm ở cách dùng dữ liệu. Hai phương pháp đầu dùng mỗi mẫu chuyển một lần, ngay khi thu, nên hai cập nhật liền nhau dùng hai mẫu liền nhau của cùng một quỹ đạo. DQN lưu mẫu vào $\mathcal D$ rồi rút đều; khi $\mathcal D$ đã đầy, mỗi mẫu được rút trung bình $b/F$ lần, tức $8$ lần với $b=32$, $F=4$ của Mnih và cộng sự (2015) (Ví dụ 08.14). Đổi lại, dữ liệu của DQN khác chính sách theo hai nguồn: hành vi $\epsilon_{\mathrm{exp}}$-tham lam và các phiên bản $\theta$ cũ đã ghi mẫu (Mục 3).

Cả ba điều kiện dừng đều là ngân sách hoặc số đo hữu hạn. Định lý 06.21 cần số cập nhật không giới hạn, nên dừng sau một số cập nhật định trước chỉ trả bảng tại thời điểm dừng. Lợi tức đánh giá đo bằng chính sách tham lam theo $Q_\theta$ trên các lượt riêng, không thăm dò; đạt ngưỡng cho biết chính sách hiện thời đạt tiêu chí đã chọn, không cho biết $Q_\theta$ gần $q_*$ đến đâu.

| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Q-learning dạng bảng (Định lý 06.21) | MDP hữu hạn với động lực dừng, phần thưởng bị chặn, $0\le\gamma<1$, $Q_0$ hữu hạn, mẫu sinh từ chính MDP; số cập nhật không giới hạn; mọi cặp được cập nhật vô hạn lần, hầu chắc chắn; bước học thỏa điều kiện Robbins–Monro theo cặp (Định nghĩa 06.19) | $Q_t(s,a)\to q_*(s,a)$ hầu chắc chắn với mọi cặp; không cho tốc độ |
| Q-learning bán gradient tuyến tính (Định nghĩa 07.38, Mệnh đề 07.37) | có đồng thời xấp xỉ hàm, bootstrap và học khác chính sách | không có bảo đảm hội tụ chung; có thể phân kỳ |
| DQN (Nhận xét 08.21) | có cả ba yếu tố trên; bộ nhớ phát lại và mạng mục tiêu giảm hai nguồn bất ổn nhưng không bỏ yếu tố nào | không có bảo đảm hội tụ tổng quát; tác dụng của từng cơ chế được đánh giá bằng thí nghiệm qua nhiều lần chạy |

Trong bảng thứ hai, giả thiết ở hàng đầu và ở hai hàng sau có vai trò khác nhau. Ở hàng đầu, đó là các điều kiện để định lý áp dụng, và mỗi điều kiện có vai trò riêng. Bỏ điều kiện mọi cặp được cập nhật vô hạn lần: một cặp không bao giờ được thử giữ mãi giá trị khởi tạo. Bỏ điều kiện $\sum_n\alpha_n^2<\infty$, chẳng hạn dùng bước học hằng: khi phần thưởng hoặc chuyển trạng thái ngẫu nhiên, mỗi cập nhật vẫn kéo ô theo nhiễu của mẫu mới nhất, nên ô không hội tụ hầu chắc chắn (Sutton và Barto, 2018, §2.5). Bỏ biểu diễn bảng thì sang hàng thứ hai.

Ở hai hàng sau, đó là điều kiện làm mất bảo đảm. Kết luận "không có bảo đảm hội tụ chung" yếu hơn khẳng định thuật toán phân kỳ, và bằng chứng cho nó là một phản ví dụ. Xét TD(0) dự đoán khác chính sách trên hai trạng thái dùng chung tham số vô hướng $w$, với $x(s_1)=1$, $x(s_2)=2$, phần thưởng $R=0$, $\gamma=0{,}9$, $\alpha=0{,}1$, và chỉ chuyển $s_1\to s_2$ được cập nhật. Mỗi bước, $w\leftarrow w+0{,}1\,(0{,}9\cdot2w-w)=1{,}08\,w$, nên $\lvert w_n\rvert\to\infty$ khi $w_0\ne0$ (Mệnh đề 07.37). Khi mỗi trạng thái chỉ có một hành động, phép cực đại trong đích chỉ chọn hành động duy nhất, nên Q-learning bán gradient trên dữ liệu chỉ gồm chuyển $s_1\to s_2$ cho đúng dãy này. Giữ $w^-$ cố định $C=10$ bước rồi đồng bộ cho $w_{10}=(1{,}8-0{,}8\cdot0{,}9^{10})\,w^-\approx1{,}521\,w^-$ mỗi chu kỳ, tương đương nhân khoảng $1{,}043$ mỗi bước (Ví dụ 08.24): tham số tăng chậm hơn nhưng vẫn không chặn.

Hàng DQN đọc cùng cách. Bộ nhớ phát lại giảm tương quan giữa các mẫu, mạng mục tiêu làm chậm sự thay đổi của đích, còn xấp xỉ hàm, bootstrap và dữ liệu khác chính sách vẫn giữ nguyên. Trong thí nghiệm loại bỏ của Mnih và cộng sự (2015, Extended Data Table 3) trên năm trò chơi Atari, tổ hợp có cả hai cơ chế cho điểm cao nhất; đó là bằng chứng thực nghiệm trên các trò chơi đã thử, chưa có định lý tương ứng.

**Trong thực hành.** Hai trường hợp riêng nối ba hàng của bảng thứ nhất và cho một phép kiểm cài đặt. Với đặc trưng chỉ thị (one-hot), $x(s,a)$ là vector đơn vị của cặp $(s,a)$, nên $x(s,a)^\top w$ là một thành phần của $w$ và cập nhật tuyến tính trùng cập nhật bảng với cùng bước học. Với $N=b=F=C=1$ (khi đó $N_{\mathrm{start}}=1$), bộ tối ưu SGD có tốc độ học $\eta$ và mạng tuyến tính $Q_\theta(o,a)=x(o,a)^\top\theta$, mỗi bước tối ưu của DQN dùng đúng mẫu vừa thu, $\theta^-$ bằng $\theta$ hiện tại, và $\nabla_\theta(y-q)^2=-2(y-q)\,x(O,A)$ khi $y$ trong $\operatorname{sg}$; vậy quy tắc cập nhật của DQN trùng Q-learning bán gradient với bước hằng $\alpha=2\eta$. Ghép hai trường hợp, một bản cài đặt DQN với cấu hình đó và đặc trưng chỉ thị trên một MDP nhỏ phải cho đúng dãy bảng của Q-learning dạng bảng với $\alpha=2\eta$, nên có thể so từng cập nhật với phép tính tay.

DQN giữ dạng đích và hành vi thu dữ liệu của Q-learning, thay lớp hàm và cách dùng dữ liệu; vì có đủ ba yếu tố của bộ ba bất ổn, nó không thừa hưởng Định lý 06.21. Do đó các quy tắc ở bảng thứ nhất được kiểm bằng phép tính trên từng mini-batch, còn kết luận về hội tụ chỉ được kiểm bằng thí nghiệm qua nhiều lần chạy độc lập.

### Trả lời vấn đề trung tâm

Bài toán của chương là học $q_*$ khi quan sát là vector liên tục hoặc ảnh, tập hành động hữu hạn và mô hình của môi trường không được cho. Ở mục 1, chúng ta đã nêu trước một câu trả lời có điều kiện cho mỗi phần; đến đây mỗi câu có kết quả và số liệu đi kèm.

Mạng $\mathbf q_\theta(o)$ cho giá trị của mọi hành động trong một lần tính (Định nghĩa 08.1). Khi $\theta^-$ giữ cố định giữa hai lần đồng bộ (Định nghĩa 08.3), đích $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$ không phụ thuộc tham số đang cập nhật, nên trong khoảng đó mỗi mẫu chuyển có một nhãn hồi quy cố định. Mẫu 1 của ví dụ xuyên suốt, với $R_1=1$, $Z_1=0$, $\gamma=0{,}9$ và $\max_{a'}Q_{\theta^-}(O'_1,a')=4$, giữ đích $4{,}6$ tới mốc đồng bộ; tại mốc, giá trị cực đại thành $5$ và đích đổi $0{,}9$ thành $5{,}5$ (Ví dụ 08.23). Câu trả lời này cần mặt nạ chỉ chứa $Z$ và quan sát đủ Markov.

Khi mini-batch được rút đều từ $\mathcal D$, với mini-batch hai mẫu, xác suất hai mẫu rút được liền nhau chỉ khoảng $2/N$ (Nhận xét 08.9), nên tương quan ngắn hạn giảm. Với tương quan $0{,}9^k$, bốn gradient liền nhau chỉ tương đương khoảng $1{,}1$ mẫu độc lập (Ví dụ 08.9). Dữ liệu vẫn do một tác tử thu thập theo hành vi thay đổi dần, nên các mẫu chưa độc lập cùng một phân phối cố định. Theo Mệnh đề 08.8, đích không cần tỉ số lấy mẫu quan trọng khi quan sát đủ Markov và động lực không đổi.

Với đích trong $\operatorname{sg}$ và phép chọn theo hành động $q_i=[\mathbf q_\theta(O_i)]_{A_i}$ (Định nghĩa 08.12), gradient $\nabla_\theta L_B=\tfrac2b\sum_i(q_i-y_i)\nabla_\theta q_i$ chỉ đi qua giá trị của các hành động đã lưu. Trên mini-batch hai mẫu với đích $(4{,}6;\,-2)$ và dự đoán $(3{,}1;\,-1{,}5)$, đạo hàm theo hai dự đoán là $(-1{,}5;\,0{,}5)$. Gradient vẫn đổi mọi thành phần của $\theta$, nên giá trị ở các quan sát và hành động khác cũng thay đổi theo.

Bộ tối ưu chỉ quyết định cách đổi gradient thành bước tham số (Định nghĩa 08.15). Công thức đích, cơ chế thu thập dữ liệu và lớp hàm không phụ thuộc lựa chọn đó, nên không bộ tối ưu nào loại được nguồn bất ổn. Trên hàm $\tfrac12(100\theta_1^2+\theta_2^2)$, RMSprop và Adam đi bước đầu cùng cỡ ở hai tọa độ còn SGD thì không, nhưng khác biệt này chỉ thuộc về tốc độ của bài toán tối ưu.

DQN có đủ xấp xỉ hàm, bootstrap và học khác chính sách, nên không có bảo đảm hội tụ tổng quát (Nhận xét 08.21). Trên phản ví dụ hai trạng thái dùng chung tham số, mạng mục tiêu với $C=10$ chỉ hạ hệ số tăng mỗi bước từ $1{,}08$ xuống khoảng $1{,}043$ (Ví dụ 08.24). Vì vậy tác dụng của bộ nhớ phát lại và mạng mục tiêu được đánh giá bằng thí nghiệm qua nhiều lần chạy độc lập, như thí nghiệm loại bỏ của Mnih và cộng sự (2015, Extended Data Table 3) và thiết kế ở Bài tập 08.3.

Vì thế câu trả lời của chương là có điều kiện. DQN cho một quy trình học $q_*$ từ quan sát thô, trong đó nhãn hồi quy đứng yên giữa hai mốc đồng bộ, mini-batch được rút đều từ $\mathcal D$ và gradient chỉ đi qua $q_i$, nhưng chưa có định lý bảo đảm quy trình đó hội tụ tới $q_*$ (bài giảng gốc, trang 12–34; Sutton và Barto, 2018, §11.3, §16.5). Đích của DQN còn chứa phép cực đại trên ước lượng có nhiễu; Bài 09 xét độ chệch của phép cực đại này và Double DQN.

### Câu hỏi tự kiểm tra

Mỗi câu dưới đây dùng một kết quả của chương; khi trả lời, chúng ta nêu cả kết quả đã dùng.

1. Bộ nhớ phát lại giảm nguồn bất ổn nào, để lại giới hạn nào? Nó giảm tương quan giữa các mẫu liền nhau trong một mini-batch: khi rút đều từ $\mathcal D$ gồm $N$ mẫu, với mini-batch hai mẫu, xác suất hai mẫu rút được liền nhau chỉ khoảng $2/N$. Các mẫu vẫn không độc lập cùng một phân phối cố định, vì phân phối của $\mathcal D$ đổi theo hành vi, và cơ chế này không tạo bảo đảm hội tụ (Nhận xét 08.19, Nhận xét 08.9).
2. Mạng mục tiêu làm chậm đại lượng nào, và không loại yếu tố nào? Nó làm chậm sự thay đổi của đích: giữa hai lần đồng bộ, đích của mỗi mẫu đứng yên, và tại mốc đồng bộ đích đổi $\Delta y_i=\gamma(1-Z_i)\bigl[\max_{a'}Q_\theta(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\bigr]$, như $0{,}9$ ở mẫu 1 của ví dụ xuyên suốt. Đích vẫn là đích bootstrap, nên mạng mục tiêu không loại yếu tố nào của bộ ba bất ổn (Nhận xét 08.20, Nhận xét 08.21).
3. Khi nào mẫu chuyển bị cắt ngắn vẫn giữ phần bootstrap? Khi $U=1$ và $Z=0$, tức lượt dừng vì giới hạn số bước trong khi MDP chưa kết thúc. Mặt nạ chỉ dùng $1-Z$; cờ gộp $Z\lor U$ chỉ dùng để đặt lại môi trường (Định nghĩa 08.6, Bài tập 08.4).
4. Adam có loại được bộ ba bất ổn không? Không. Bộ tối ưu chỉ đổi gradient thành bước tham số, và lựa chọn của nó không đổi công thức đích, cách thu thập dữ liệu hay lớp hàm (Định nghĩa 08.15, Nhận xét 08.21).

Bài giảng gốc (trang 36) nêu thêm ba hướng thảo luận: vì sao bộ nhớ phát lại làm cập nhật trên mini-batch đáng tin cậy hơn; vì sao các bộ tối ưu thích nghi vẫn có thể giúp DQN dù không sửa đích Bellman; và những cách tăng thăm dò trong DQN. Hai hướng đầu được trả lời một phần bởi câu 1 và câu 4; hướng thứ ba nằm ngoài chương này.

### Bài tập về nhà và tài liệu đọc

Năm bài tập của chương nằm ở mục "Bài tập củng cố" cuối tệp, mỗi bài có gợi ý và lời giải; bốn bài đầu đã được giải trên trang chiếu. Bài tập 08.1 (đích, hàm mất mát và gradient trên một mini-batch) và Bài tập 08.2 (lỗi cài đặt đích DQN) dùng kết quả của phần 4; Bài tập 08.3 (thiết kế thí nghiệm loại bỏ) dùng phần 6; Bài tập 08.4 (một bước DQN trên CartPole) dùng đồng thời phần 2, 4 và 6; Bài tập 08.5 dùng phần 5 cho hệ số bước của SGD và phần 6 cho độ thay đổi của đích tại mốc đồng bộ.

Tài liệu đọc gồm hai mục của Sutton và Barto (2018): §11.3 về bộ ba bất ổn và §16.5 về DQN trên các trò chơi Atari; và bài báo của Mnih và cộng sự (2015), với mục Methods cho thuật toán, Extended Data Table 1 cho cấu hình siêu tham số và Extended Data Table 3 cho thí nghiệm loại bỏ.

Giả mã "Deep Q-learning with experience replay" của bài giảng gốc (trang 21) đã có bộ nhớ phát lại dung lượng $N$, hai mạng với $\theta^-=\theta$ lúc khởi tạo, đích bằng $r_j$ tại bước kết thúc và đồng bộ sau mỗi $C$ bước. Đối chiếu từng dòng với Thuật toán 08.13 cho thấy các chi tiết được thêm ở thuật toán đó: hai cờ $Z$ và $U$, số mẫu tối thiểu $N_{\mathrm{start}}$, nhịp tối ưu $F$, quan sát cuối của lượt khi môi trường tự đặt lại, phép dừng gradient, và việc đếm $C$ theo bước tối ưu. Với Atari, đầu vào của mạng là chồng bốn khung $84\times84$ và mạng tích chập trả về $\lvert\mathcal A\rvert$ giá trị hành động (Ví dụ 08.2).

Bài 09 xét độ chệch của phép cực đại (maximization bias) trong đích, Double DQN, rồi gradient chính sách.

## Tình huống áp dụng và ứng dụng

::: application Tình huống 08.1 (DQN cho CartPole-v1)
**Bài toán.** Trong môi trường `CartPole-v1` của Gymnasium (notebook thực hành Bài 04, phần 2), quan sát là vector $(x,\dot x,\phi,\dot\phi)$ gồm vị trí và vận tốc của xe, góc và vận tốc góc của cột; tác tử đẩy xe sang trái hoặc sang phải và nhận phần thưởng $+1$ ở mỗi bước. Cần học một chính sách giữ cột bằng DQN.

**Mô hình hóa.** Mạng giá trị hành động $\mathbf q_\theta(o)\in\mathbb R^2$ nhận vector bốn chiều (Định nghĩa 08.1), $\lvert\mathcal A\rvert=2$. Mỗi mẫu chuyển mang cờ $Z=1$ khi góc của cột vượt $12^\circ$ hoặc vị trí của xe vượt $2{,}4$ về một phía, và cờ $U=1$ khi lượt đạt $500$ bước (Định nghĩa 08.6). Thuật toán 08.13 dùng mặt nạ $1-Z$.

**Kiểm giả thiết.**

- Quan sát đủ Markov: bốn biến $(x,\dot x,\phi,\dot\phi)$ là trạng thái của mô phỏng (notebook Bài 04, phần 2), nên không cần chồng nhiều khung như với Atari (Nhận xét 08.2).
- Tập hành động hữu hạn: thỏa, hai hành động.
- Kết thúc và cắt ngắn tách được: thỏa, vì môi trường trả hai cờ riêng `terminated` và `truncated`; mặt nạ chỉ dùng $Z$ (Bài tập 08.4).
- Cận của giá trị: phần thưởng bằng $1$ mỗi bước nên lợi tức chiết khấu không vượt $1/(1-\gamma)$, tức $100$ với $\gamma=0{,}99$; một dự đoán vượt cận này chắc chắn sai.
- Bộ ba bất ổn: mạng nơ-ron, đích bootstrap và dữ liệu khác chính sách cùng có mặt, nên không có bảo đảm hội tụ tổng quát (Nhận xét 08.21).

**Áp dụng.** Bài tập 08.4 thực hiện một bước của Thuật toán 08.13 trên mini-batch có cả mẫu bị cắt ngắn và mẫu cột đổ.

**Giới hạn.** Không có lần chạy DQN trên CartPole đi kèm, nên ta không nêu số liệu về số bước giữ cột; kết luận về hiệu quả cần thí nghiệm qua nhiều hạt giống ngẫu nhiên, như thiết kế ở Bài tập 08.3.
:::

::: application Tình huống 08.2 (Atari với một khung: giả thiết Markov không thỏa)
**Bài toán.** Một bản cài đặt DQN cho một trò chơi Atari đưa vào mạng chỉ một khung ảnh xám $84\times84$ thay cho chồng bốn khung.

**Kiểm giả thiết.** Một khung cho vị trí của vật thể nhưng không cho vận tốc hay hướng chuyển động (bài giảng gốc, trang 35; Ví dụ 08.4). Hai tình huống có cùng khung nhưng khác hướng chuyển động có tương lai khác nhau, nên quan sát không đủ Markov (Nhận xét 08.2). Giả thiết Markov của Mệnh đề 08.8 không thỏa: kỳ vọng của đích khi biết $(O_i,A_i)$ còn phụ thuộc phân phối của phần trạng thái không quan sát được, và phân phối này đổi theo hành vi. Đích vì vậy chỉ là xấp xỉ của mục tiêu Bellman viết theo quan sát.

**Khắc phục.** Chồng bốn khung liên tiếp cho thông tin vận tốc ngắn hạn (Mnih và cộng sự, 2015, mục Methods); thay tầng kết nối đầy đủ bằng một tầng hồi quy để mạng tích lũy lịch sử dài hơn (Hausknecht và Stone, 2015). Cả hai cách chỉ làm quan sát gần Markov hơn; không cách nào chứng minh tính Markov cho mọi trò chơi.
:::

**Ứng dụng.**

- **Bài 09 (Double DQN)** giữ đích hồi quy, bộ nhớ phát lại và mạng mục tiêu của chương này, và xét độ chệch của phép cực đại trong đích.
- **Cập nhật mềm của mạng mục tiêu** thay phép gán $\theta^-\leftarrow\theta$ mỗi $C$ bước bằng $\theta^-\leftarrow\tau\theta+(1-\tau)\theta^-$ sau mỗi bước với $\tau$ nhỏ, chẳng hạn $\tau=0{,}001$ trong DDPG (Lillicrap và cộng sự, 2016).

## Tóm tắt chương

Một bảng giá trị hành động không dùng được khi quan sát là vector liên tục hoặc ảnh: lưới thô cho Lunar Lander đã có $9\,216$ ô trạng thái, và sau $2\,000$ lượt chỉ $1\,896$ ô có mẫu. Chúng ta thay bảng bằng một mạng trả vector $\mathbf q_\theta(o)$, và với Atari, đầu vào là bốn khung $84\times84$ xếp chồng để quan sát gần Markov. Với mạng mục tiêu tách tham số tạo đích khỏi tham số được cập nhật, mini-batch hai mẫu chuyển có đích $4{,}6$ và $-2$, hàm mất mát $1{,}25$ và gradient theo hai dự đoán $(-1{,}5;\,0{,}5)$. Bộ nhớ phát lại rút mini-batch đều từ $N$ mẫu gần nhất, vì bốn gradient liền nhau với tương quan $0{,}9^k$ chỉ bằng khoảng $1{,}1$ mẫu độc lập. Thuật toán DQN ghép thu thập, lưu, tối ưu và đồng bộ bằng hai bộ đếm; với cấu hình Atari $F=4$, $C=10^4$, mạng mục tiêu đứng yên trong $4\cdot10^4$ bước môi trường. Bộ tối ưu chỉ đổi gradient thành bước tham số: trên hàm $\tfrac12(100\theta_1^2+\theta_2^2)$, RMSprop và Adam đi bước đầu cùng cỡ ở hai tọa độ còn SGD thì không. Tại mỗi mốc đồng bộ, đích của mẫu chưa kết thúc đổi, như $0{,}9$ ở mẫu 1. DQN vẫn có đủ ba yếu tố của bộ ba bất ổn, và trong phản ví dụ hai trạng thái, mạng mục tiêu với $C=10$ chỉ hạ hệ số tăng mỗi bước từ $1{,}08$ xuống khoảng $1{,}043$, nên thuật toán không có bảo đảm hội tụ tổng quát.

**Công thức cần nhớ.**

$$
\begin{aligned}
y_i&=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a'),\\
L_B(\theta)&=\frac1b\sum_{i=1}^b\bigl(\operatorname{sg}(y_i)-Q_\theta(O_i,A_i)\bigr)^2,\\
\Delta y_i&=\gamma(1-Z_i)\Bigl[\max_{a'}Q_\theta(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\Bigr].
\end{aligned}
$$

**Giả thiết hay bị quên.** Mặt nạ chỉ chứa $Z$, không chứa $U$. Quan sát lưu trong mẫu chuyển là quan sát cuối của lượt, không phải quan sát đầu của lượt mới sau khi môi trường tự đặt lại. Đích là hằng theo $\theta$ khi lấy gradient. Đồng bộ đếm bước tối ưu, không đếm bước môi trường. Bộ nhớ phát lại không tạo mẫu độc lập cùng phân phối cố định. Không có bảo đảm hội tụ tổng quát cho DQN, nên tác dụng của mỗi cơ chế được đánh giá bằng thí nghiệm qua nhiều lần chạy.

---

## Bài tập củng cố

Các bài tập dưới đây xếp theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Bài tập ở hai mức sau có gợi ý và lời giải; ở mức nhận biết, các câu hỏi tự kiểm tra có lời giải ngắn ngay sau câu.

### Mức nhận biết

Bốn câu hỏi của mục "Câu hỏi tự kiểm tra" ở phần 7 là bài tập mức này; lời giải ngắn đặt ngay sau mỗi câu.

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 08.1 (Đích, hàm mất mát và gradient trên một mini-batch)

Cho $b=2$, $\gamma=0{,}9$ và mini-batch hai mẫu chuyển, với $q_i=Q_\theta(O_i,A_i)$:

| $i$ | $R_i$ | $Z_i$ | $\max_{a'}Q_{\theta^-}(O'_i,a')$ | $q_i$ |
|---|---|---|---|---|
| 1 | 1 | 0 | 4 | 3,1 |
| 2 | −2 | 1 | 100 | −1,5 |

Tính $y_i$, $\delta_i=y_i-q_i$, hàm mất mát $L_B$ (Định nghĩa 08.10) và $\partial L_B/\partial q_i$ với $i=1,2$.
Xét $q_1$, $q_2$ như hai biến riêng, cho biết $q_i$ nào tăng dưới một bước hạ gradient nhỏ.
:::

::: hint
Áp mặt nạ $(1-Z_i)$ trước khi tính sai số. Mẫu 2 có $Z_2=1$, nên giá trị $100$ của mạng mục tiêu tại quan sát cuối lượt không vào đích. Với hàm mất mát trung bình trên hai mẫu, đạo hàm theo $q_i$ là $\tfrac{2}{b}(q_i-y_i)$.
:::

::: solution

- $y_1 = 1 + 0{,}9\cdot(1-0)\cdot 4 = 4{,}6$; $y_2 = -2 + 0{,}9\cdot(1-1)\cdot 100 = -2$.
- $\delta_1 = 4{,}6-3{,}1 = 1{,}5$; $\delta_2 = -2-(-1{,}5) = -0{,}5$.
- $L_B = \tfrac12(1{,}5^2 + 0{,}5^2) = \tfrac12(2{,}25+0{,}25) = 1{,}25$.
- $\partial L_B/\partial q_1 = 2\cdot\tfrac12\cdot(3{,}1-4{,}6) = -1{,}5$;
  $\partial L_B/\partial q_2 = 2\cdot\tfrac12\cdot(-1{,}5+2) = 0{,}5$.
- Mẫu 1 có gradient theo $q_1$ âm, nên phép trừ gradient làm $q_1$ tăng; mẫu 2
  có gradient dương nên $q_2$ giảm.

Kết luận đúng khi xét $q_1$, $q_2$ như hai biến riêng. Trong DQN, cả hai cùng phụ thuộc $\theta$: một bước $\Delta\theta=-\eta\nabla_\theta L_B=\eta(1{,}5\,\nabla_\theta q_1-0{,}5\,\nabla_\theta q_2)$ cho $\Delta q_1\approx\nabla_\theta q_1^\top\Delta\theta=\eta\bigl(1{,}5\lVert\nabla_\theta q_1\rVert^2-0{,}5\,\nabla_\theta q_1^\top\nabla_\theta q_2\bigr)$, nên $q_1$ giảm khi $\nabla_\theta q_1^\top\nabla_\theta q_2>3\lVert\nabla_\theta q_1\rVert^2$.

**Kiểm tra lại.** Ba lỗi thường gặp: quên mặt nạ ở mẫu 2, cho $y_2=-2+0{,}9\cdot100=88$ và $\delta_2=89{,}5$; dùng giá trị lớn nhất của $\mathbf q_\theta(O_i)$ thay cho giá trị của hành động đã lưu $A_i$ (phép chọn theo hành động); quên hệ số $\tfrac2b$, hoặc dùng tổng thay cho trung bình, làm đạo hàm sai một hằng số nhân (với $b=2$, $\tfrac2b=1$ nên lỗi này chỉ lộ ra khi $b\ne2$).
:::

::: exercise Bài tập 08.5 (Hệ số bước của SGD và độ thay đổi của đích)
(a) Cho hàm mất mát $L(\theta)=\tfrac12(100\,\theta_1^2+\theta_2^2)$ trên $\theta=(\theta_1;\,\theta_2)\in\mathbb R^2$ và hạ gradient ngẫu nhiên (Định nghĩa 08.16) với tốc độ học $\eta=0{,}03$, xuất phát từ $\theta_0=(0{,}02;\,0{,}02)$. Tính hệ số nhân mỗi bước của từng tọa độ, giá trị $\theta_1$, $\theta_2$ sau hai bước, và cho biết tọa độ nào hội tụ về $0$.

(b) Một mẫu chuyển có $R_1=1$, $Z_1=0$, $\gamma=0{,}9$. Ngay trước mốc đồng bộ, $\max_{a'}Q_{\theta^-}(O'_1,a')=10$; tại mốc, $\max_{a'}Q_\theta(O'_1,a')=10{,}5$. Tính đích trước và sau mốc và độ thay đổi $\Delta y_1$ (Nhận xét 08.20).
:::

::: hint
(a) Gradient là $(100\,\theta_1;\,\theta_2)$, nên mỗi bước nhân $\theta_1$ với $1-100\eta$ và $\theta_2$ với $1-\eta$; một tọa độ hội tụ về $0$ khi trị tuyệt đối của hệ số nhỏ hơn $1$. (b) $\Delta y_1=\gamma(1-Z_1)\bigl[\max_{a'}Q_\theta(O'_1,a')-\max_{a'}Q_{\theta^-}(O'_1,a')\bigr]$.
:::

::: solution
**Câu (a).** Với $\eta=0{,}03$, hệ số của $\theta_1$ là $1-100\cdot0{,}03=-2$ và hệ số của $\theta_2$ là $1-0{,}03=0{,}97$. Sau một bước, $\theta_1=-0{,}04$, $\theta_2=0{,}0194$; sau hai bước, $\theta_1=0{,}08$, $\theta_2=0{,}018818$. Vì $\lvert-2\rvert>1$, $\theta_1=(-2)^j\cdot0{,}02$ đổi dấu mỗi bước và tăng không chặn: tọa độ thứ nhất phân kỳ. Vì $0<0{,}97<1$, $\theta_2$ hội tụ về $0$, nhưng chậm. Muốn tọa độ thứ nhất hội tụ cần $0<\eta<0{,}02$ (Ví dụ 08.19).

**Câu (b).** Trước mốc, $y_1=1+0{,}9\cdot(1-0)\cdot10=10$; sau mốc, $y_1=1+0{,}9\cdot10{,}5=10{,}45$. Vậy $\Delta y_1=0{,}9\cdot(10{,}5-10)=0{,}45$, đúng bằng hiệu hai giá trị đích.

**Kiểm tra lại.** Ba lỗi hay gặp: lấy hệ số $1-\eta$ cho cả hai tọa độ và kết luận SGD hội tụ; quên rằng hệ số âm với trị tuyệt đối lớn hơn $1$ vẫn là phân kỳ; tính $\Delta y_1$ mà bỏ hệ số $\gamma$, cho $0{,}5$ thay cho $0{,}45$.
:::

### Mức vận dụng

::: exercise Bài tập 08.2 (Lỗi cài đặt đích DQN)
Hàm `step(a)` trả quan sát sau bước `obs_after_step`, phần thưởng `r`, hai cờ `terminated` (cờ $Z$ của kết thúc MDP) và `truncated` (cờ $U$ của cắt ngắn), và `final_obs`: quan sát cuối của lượt nếu môi trường vừa tự đặt lại, ngược lại `None`. `D` là bộ nhớ phát lại; `D.sample(b)` trả sáu mảng `ob, ab, rb, ob2, zb, ub` của một mini-batch, chiều đầu $b$, lần lượt chứa $O_i$, $A_i$, $R_i$, $O'_i$, $Z_i$, $U_i$; `ab` có kiểu `int64`, `zb` và `ub` có kiểu `bool`. Hậu tố `b` giữ các mảng của mini-batch tách khỏi biến của bước môi trường. Hai mạng `q_online`, `q_target` nhận mảng $[b,4,H,W]$ và trả mảng $[b,\lvert\mathcal A\rvert]$.

```python
obs_after_step, r, terminated, truncated, final_obs = step(a)
D.add(o, a, r, obs_after_step, terminated, truncated)

ob, ab, rb, ob2, zb, ub = D.sample(b)
done = zb | ub
y = rb + gamma * (1 - done) * q_target(ob2).max()
loss = ((y - q_online(ob)[ab]) ** 2).mean()
```

Hai dòng đầu chạy ở mỗi bước môi trường; bốn dòng sau chạy trên một mini-batch. Hãy sửa năm lỗi: (a) quan sát kế tiếp được lưu vào `D`; (b) mặt nạ của đích; (c) đường gradient qua đích; (d) phép chọn theo hành động trên mini-batch; (e) chiều của phép cực đại. Với mỗi lỗi, nêu kích thước hoặc giá trị sai mà dòng mã tạo ra khi $b=2$ và $\lvert\mathcal A\rvert=3$, nếu có.
:::

::: hint
So từng dòng với Thuật toán 08.13: bước 3 lưu quan sát cuối của mẫu chuyển; bước 7 tính $y_i=\operatorname{sg}\bigl(R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')\bigr)$; bước 6 lấy $q_i=[\mathbf q_\theta(O_i)]_{A_i}$. Ghi kích thước của mảng sau mỗi phép toán theo Nhận xét 08.14.
:::

::: solution
Đoạn mã đã sửa:

```python
next_o = obs_after_step if final_obs is None else final_obs
D.add(o, a, r, next_o, terminated, truncated)

ob, ab, rb, ob2, zb, ub = D.sample(b)
with torch.no_grad():
    v = q_target(ob2).max(1).values
    y = rb + gamma * (1 - zb.float()) * v
q = q_online(ob).gather(1, ab.unsqueeze(1)).squeeze(1)
loss = ((y - q) ** 2).mean()
```

**Câu (a).** Khi môi trường tự đặt lại sau bước cuối của một lượt, `obs_after_step` là quan sát đầu của lượt mới. Ở mẫu kết thúc, mặt nạ xóa phần bootstrap nên lỗi không lộ; ở mẫu bị cắt ngắn, $Z=0$ và đích bootstrap từ một quan sát không nối với $O_t$. Dòng sửa lưu `final_obs` khi có. Tên trường chứa quan sát cuối phụ thuộc thư viện và phiên bản; `final_obs` là tên giả định của bài.

**Câu (b).** `done = zb | ub` gộp cắt ngắn vào mặt nạ, nên mọi mẫu bị cắt ngắn có $y_i=R_i$ thay cho $R_i+\gamma\max_{a'}Q_{\theta^-}(O'_i,a')$; với Ví dụ 08.8, đích $4{,}6$ bị hạ thành $1$. Mặt nạ đúng là $1-Z$; cờ $Z\lor U$ chỉ quyết định việc đặt lại môi trường ở bước 4. `zb.float()` đổi cờ sang kiểu số trước phép trừ.

**Câu (c).** Không có `no_grad`, thư viện lưu đồ thị của đường tạo đích. Khi `q_target` có tham số riêng, gradient theo $\theta$ không đổi nhưng thư viện tính thêm gradient cho $\theta^-$ mà bộ tối ưu không dùng; khi `q_target` và `q_online` là cùng một đối tượng, gradient đi qua đích và cập nhật thành phương pháp gradient dư (Mục "Phép chọn theo hành động và dừng gradient"). Tính đích trong `torch.no_grad()` là dạng cài đặt của $\operatorname{sg}$.

**Câu (d).** `q_online(ob)` có kích thước $[2,3]$. Chỉ số `[ab]` với `ab` kích thước $[2]$ lấy các hàng có số thứ tự $A_1$, $A_2$, cho mảng $[2,3]$, không phải hai giá trị $Q_\theta(O_i,A_i)$. Phép trừ `y - q_online(ob)[ab]` giữa $[2]$ và $[2,3]$ báo lỗi kích thước vì $2\ne3$; khi $\lvert\mathcal A\rvert=b$, phép trừ lan truyền thành ma trận $[b,b]$ không báo lỗi. `gather(1, ab.unsqueeze(1))` lấy ở hàng $i$ cột $A_i$, cho $[2,1]$, và `squeeze(1)` đưa về $[2]$.

**Câu (e).** `.max()` không chỉ chiều trả một số vô hướng, giá trị lớn nhất trên cả $2\cdot3=6$ phần tử, và cả hai mẫu dùng chung giá trị bootstrap đó; dòng mã chạy được, riêng phép `.max()` không báo lỗi. `.max(1).values` lấy cực đại theo chiều hành động cho mảng $[2]$, mỗi mẫu một giá trị.

**Kiểm tra lại.** Ba lỗi hay gặp khi sửa: viết `1 - zb` với `zb` kiểu `bool`, phép trừ bị một số thư viện từ chối; viết `.max(1)` mà quên `.values`, vì trong PyTorch phép này trả cả giá trị lẫn chỉ số; đặt cả dòng tính `q` vào khối `no_grad`, khi đó hàm mất mát không còn gradient theo $\theta$.
:::

::: exercise Bài tập 08.3 (Thiết kế thí nghiệm loại bỏ)
Một thí nghiệm loại bỏ (ablation) so DQN đầy đủ (Thuật toán 08.13) với hai nhánh, mỗi nhánh bỏ một cơ chế. Nhánh "bỏ bộ nhớ phát lại": mỗi bước tối ưu dùng $b$ mẫu chuyển vừa thu theo thứ tự thời gian. Nhánh "bỏ mạng mục tiêu": đặt $C=1$, nên đích được tính lại bằng tham số mới sau mỗi bước tối ưu. Không yêu cầu viết chương trình.

(a) Dự đoán tác động của nhánh bỏ bộ nhớ phát lại lên tương quan giữa các mẫu trong mini-batch, độ đa dạng mẫu và đường lợi tức đánh giá.

(b) Dự đoán tác động của nhánh $C=1$ lên tốc độ đổi của đích, sai số TD và dao động của tham số.

(c) Thiết kế thí nghiệm sao cho so sánh công bằng: nêu những gì được giữ cố định và những gì được đo.

(d) Nêu cách tổng hợp kết quả của nhiều lần chạy độc lập.
:::

::: hint
Dự đoán ở (a), (b) dùng Nhận xét 08.19 và Nhận xét 08.20. Công bằng nghĩa là hai nhánh chỉ khác nhánh đầy đủ ở đúng một thành phần. Chọn chỉ số đo và số lần chạy trước khi chạy; không kết luận từ một đường học.
:::

::: solution
**Câu (a).** Mẫu trong mini-batch là các mẫu liền nhau của một đoạn quỹ đạo, nên tương quan giữa chúng tăng và cỡ mẫu hiệu dụng giảm; với tương quan $0{,}9^k$ của Ví dụ 08.9, bốn mẫu liền nhau chỉ bằng khoảng $1{,}1$ mẫu độc lập. Mỗi mẫu chỉ có mặt trong các mini-batch ngay sau khi thu (khoảng $b/F$ bước tối ưu) rồi không được dùng lại, nên độ đa dạng của dữ liệu trong mỗi bước tối ưu giảm và số bước tối ưu trên mỗi mẫu cũng giảm. Dự đoán cho đường lợi tức: dao động lớn hơn giữa các đoạn huấn luyện và giữa các lần chạy; dự đoán này là giả thuyết cần đo.

**Câu (b).** Với $C=1$, $\theta^-$ bằng $\theta$ trước mỗi bước, nên đích của mỗi mẫu đổi sau mỗi bước tối ưu thay vì theo từng đợt $C$ bước; Nhận xét 08.20 cho độ thay đổi tại mỗi mốc. Sai số TD không còn là sai số so với một nhãn đứng yên trong một khoảng, nên có thể giảm chậm hoặc dao động. Ví dụ 08.5 cho thấy đích đổi sau mỗi bước vẫn có thể hội tụ; Ví dụ 08.24 với $C=1$ cho thấy tham số có thể tăng theo hệ số $1{,}08$ mỗi bước. Hướng nào xảy ra trong DQN phải đo.

**Câu (c).** Mỗi nhánh đổi đúng một thành phần so với nhánh đầy đủ. Giữ cố định kiến trúc mạng, ngân sách bước môi trường, bộ tối ưu và siêu tham số của nó, lịch thăm dò $\epsilon_{\mathrm{exp}}$, tần suất tối ưu $F$, cỡ mini-batch $b$, và tập hạt giống ngẫu nhiên (seed). Đo lợi tức đánh giá bằng chính sách tham lam theo $Q_\theta$ trên các lượt riêng, không dùng lợi tức của các lượt huấn luyện có thăm dò; đo thêm sai số TD trung bình, chuẩn gradient, và với nhánh bỏ bộ nhớ phát lại, tương quan giữa các mẫu trong mini-batch.

**Câu (d).** Mọi nhánh dùng cùng tập hạt giống, nên với mỗi hạt giống có một bộ kết quả ghép cặp; so hiệu giữa hai nhánh trong từng cặp giảm nhiễu do khởi tạo và môi trường. Báo trung bình hoặc trung vị cùng độ phân tán giữa các lần chạy, chẳng hạn độ lệch chuẩn hoặc khoảng tứ phân vị, và số lần chạy phân kỳ nếu có. Số hạt giống phụ thuộc ngân sách tính toán, nên đề không ấn định.

Kết quả của thí nghiệm kiểm hai dự đoán rút từ phần 6: bỏ bộ nhớ phát lại làm tăng tương quan ngắn hạn; bỏ mạng mục tiêu làm đích đổi sau mỗi bước tối ưu. Không nhánh nào bỏ được yếu tố nào của bộ ba bất ổn, nên không nhánh nào cho bảo đảm hội tụ (Nhận xét 08.21). Mnih và cộng sự (2015, Extended Data Table 3) báo một thí nghiệm cùng loại trên năm trò chơi Atari, trong đó tổ hợp dùng cả hai cơ chế cho điểm cao nhất.

**Kiểm tra lại.** Ba lỗi hay gặp: đổi hai thành phần trong cùng một nhánh, chẳng hạn bỏ mạng mục tiêu và đổi bộ tối ưu, nên không tách được tác dụng; dùng lợi tức của các lượt huấn luyện có thăm dò làm thước đo chất lượng của chính sách; kết luận từ một lần chạy, hoặc chỉ báo trung bình mà không báo độ phân tán.
:::

::: exercise Bài tập 08.4 (Một bước DQN trên CartPole)
Trong môi trường `CartPole-v1` của Gymnasium, tác tử nhận phần thưởng $+1$ ở mỗi bước, kể cả bước dẫn tới kết thúc. Lượt kết thúc ($Z=1$) khi góc của cột vượt $12^\circ$ hoặc vị trí của xe vượt $2{,}4$ về một phía, và bị cắt ngắn ($U=1$) khi đạt giới hạn $500$ bước. Giới hạn này do cấu hình đăng ký môi trường quy định, không thuộc động lực của MDP (notebook thực hành Bài 04, phần 2).

Một bản cài đặt DQN dùng $\gamma=0{,}9$, mini-batch $b=2$ và chu kỳ đồng bộ $C=1000$; ngay trước bước tối ưu đang xét, $k_{\mathrm{opt}}=999$. Mini-batch gồm hai mẫu chuyển, với $q_i=Q_\theta(O_i,A_i)$:

| $i$ | $R_i$ | $Z_i$ | $U_i$ | $\max_{a'}Q_{\theta^-}(O'_i,a')$ | $q_i$ |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 10 | 9 |
| 2 | 1 | 1 | 0 | 10 | 2 |

Mẫu 1 là bước thứ $500$ của một lượt mà cột chưa đổ; mẫu 2 là bước cột đổ.

(a) Tính đích $y_1$, $y_2$ theo Định nghĩa 08.4 và Định nghĩa 08.6.

(b) Tính hàm mất mát $L_B$ (Định nghĩa 08.10) và $\partial L_B/\partial q_i$ với $i=1,2$.

(c) Một bản cài đặt dùng mặt nạ $1-(Z_i\lor U_i)$ thay cho $1-Z_i$. Tính lại $y_1$ và $\delta_1=y_1-q_1$, rồi cho biết lỗi này làm lệch giá trị học được ở các quan sát gần bước $500$ theo chiều nào.

(d) Sau bước tối ưu này, Thuật toán 08.13 có gán $\theta^-\leftarrow\theta$ không? Trả lời lại khi một bản cài đặt kiểm $C$ trước khi tăng $k_{\mathrm{opt}}$.
:::

::: hint
Xác định cờ nào xóa nhánh bootstrap trước khi tính sai số: chỉ $Z_i$ ghi việc MDP kết thúc. Với phần thưởng $+1$ mỗi bước và $\gamma=0{,}9$, mọi lợi tức chiết khấu không vượt $1/(1-\gamma)=10$. Với câu (d), theo bước 8 và bước 9 của Thuật toán 08.13, $k_{\mathrm{opt}}$ tăng sau cập nhật rồi mới được so với bội của $C$.
:::

::: solution
**Câu (a).** Mẫu 1 có $Z_1=0$: cột chưa đổ và xe chưa ra ngoài, nên MDP chưa kết thúc dù $U_1=1$. Đích giữ phần bootstrap:
$$
y_1=1+0{,}9\cdot(1-0)\cdot10=10.
$$
Mẫu 2 có $Z_2=1$, nên phần bootstrap bị xóa và giá trị $10$ của mạng mục tiêu tại quan sát cột đã đổ không vào đích:
$$
y_2=1+0{,}9\cdot(1-1)\cdot10=1.
$$
Cả hai đích không vượt cận $1/(1-\gamma)=10$ của lợi tức chiết khấu khi phần thưởng bằng $1$ mỗi bước.

**Câu (b).** Sai số là $\delta_1=10-9=1$ và $\delta_2=1-2=-1$. Hàm mất mát là
$$
L_B=\tfrac12\bigl(1^2+(-1)^2\bigr)=1.
$$
Với $b=2$, $\partial L_B/\partial q_i=\tfrac2b(q_i-y_i)=q_i-y_i$, nên $\partial L_B/\partial q_1=-1$ và $\partial L_B/\partial q_2=1$. Xét $q_1$, $q_2$ như hai biến riêng, một bước hạ gradient nhỏ làm $q_1$ tăng về $10$ và $q_2$ giảm về $1$.

**Câu (c).** Với mặt nạ gộp, $1-(Z_1\lor U_1)=1-(0\lor1)=0$, nên $y_1=1$ và $\delta_1=1-9=-8$; đích của mẫu 2 vẫn bằng $1$ vì $Z_2=1$. Đích của mẫu 1 bị hạ $0{,}9\cdot10=9$ và $\partial L_B/\partial q_1=q_1-y_1=8>0$, nên bước hạ gradient kéo $q_1$ xuống về $1$: giá trị bị đánh giá thấp. Quan sát của CartPole gồm vị trí, vận tốc xe, góc và vận tốc góc của cột, không có số bước, nên một quan sát ở bước $500$ có thể trùng hoặc gần các quan sát ở những bước khác; mạng dùng chung tham số kéo xuống cả giá trị của các quan sát gần nó, không chỉ ở bước $500$; mỗi lượt chạm giới hạn góp thêm một mẫu như vậy (Pardo và cộng sự, 2018). Mặt nạ gộp sai vì cắt ngắn là giới hạn của việc thu thập, không phải trạng thái kết thúc của MDP; cờ gộp $Z\lor U$ chỉ dùng để quyết định đặt lại môi trường.

**Câu (d).** Theo Thuật toán 08.13, bước 8 cập nhật $\theta$ rồi tăng $k_{\mathrm{opt}}$ từ $999$ lên $1000$; bước 9 kiểm $1000\bmod1000=0$, nên gán $\theta^-\leftarrow\theta$, và $\theta^-$ mới chứa cả cập nhật vừa làm. Nếu một bản cài đặt kiểm $C$ trước khi tăng $k_{\mathrm{opt}}$, bước này so $999\bmod1000\ne0$ nên không đồng bộ; ở bước tối ưu kế tiếp, sau cập nhật thứ $1001$, phép kiểm thấy $1000\bmod1000=0$ và mới đồng bộ. Chu kỳ vẫn là $C$, nhưng mọi lần đồng bộ lùi một bước tối ưu, và lần đồng bộ đầu tiên xảy ra ngay sau bước tối ưu thứ nhất (Ví dụ 08.15).

**Kiểm tra lại.** Bốn lỗi hay gặp. Dùng cờ gộp $Z\lor U$ làm mặt nạ cho $y_1=1$, $\delta_1=-8$. Quên mặt nạ ở mẫu 2 cho $y_2=1+0{,}9\cdot10=10$, $\delta_2=8$ và $L_B=\tfrac12(1^2+8^2)=32{,}5$. Dùng tổng thay cho trung bình cho $L_B=2$ và đạo hàm $(-2;\,2)$, sai một hằng số nhân. Kiểm $C$ trước khi tăng $k_{\mathrm{opt}}$, hoặc đếm $C$ theo bước môi trường $t$, làm lần đồng bộ lệch khỏi bước tối ưu thứ $1000$.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Tạ Việt Cường (2026). *Bài giảng 8: Deep Q-Learning* (`lecture8-dqn.pdf`), bài giảng gốc của học phần (2025–2026), 36 trang: phạm vi và thứ tự. Phần 1 dựa trên trang 1–13; phần 2 trên trang 14–17, 20–21, 31, 33, 35; phần 3 trên trang 6–7, 18–20, 30, 32; phần 4 trên trang 16, 18, 20–22, 34; phần 5 trên trang 22–28; phần 6 trên trang 12–13, 29–34; phần 7 trên trang 12–36.
- Sutton, R. S. và Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §2.5 (bước học hằng); §6.5, §6.6, §7.3 (Q-learning và đích khác chính sách); §9.3 (bán gradient); §11.2 (phản ví dụ phân kỳ, ví dụ của Baird); §11.3 (bộ ba bất ổn); §11.5 (gradient dư); §13.7 (hành động liên tục); §16.5 (DQN trên Atari).
- Mnih, V. và cộng sự (2015). Human-level control through deep reinforcement learning. *Nature* 518, 529–533: mục Methods (thuật toán, tiền xử lý bốn khung); Extended Data Table 1 (siêu tham số $N$, $b$, $N_{\mathrm{start}}$, $F$, $C$, $\gamma$, tốc độ học, lịch $\epsilon_{\mathrm{exp}}$); Extended Data Table 3 (thí nghiệm loại bỏ trên năm trò chơi).
- Kingma, D. P. và Ba, J. (2015). Adam: A Method for Stochastic Optimization. *ICLR*: Định nghĩa 08.18 và phép hiệu chỉnh lệch.
- Goodfellow, I., Bengio, Y. và Courville, A. (2016). *Deep Learning*, MIT Press: Chương 6 và 9 (mạng nhiều tầng, mạng tích chập, lan truyền ngược); Chương 8, §8.3.1, §8.5.2, §8.5.3 (SGD, RMSprop, Adam, điểm yên ngựa); §4.3 (bài toán có điều kiện kém và giới hạn bước của hạ gradient).
- Pardo, F., Tavakoli, A., Levdik, V. và Kormushev, P. (2018). Time Limits in Reinforcement Learning. *ICML*: cờ cắt ngắn $U$, mặt nạ chỉ dùng $Z$, Bài tập 08.4.
- Hausknecht, M. và Stone, P. (2015). Deep Recurrent Q-Learning for Partially Observable MDPs. *AAAI Fall Symposium*: mạng hồi quy khi quan sát không đủ Markov.
- Lillicrap, T. P. và cộng sự (2016). Continuous control with deep reinforcement learning. *ICLR*: cập nhật mềm của mạng mục tiêu.
- Farama Foundation. Tài liệu môi trường `CartPole-v1` của thư viện Gymnasium: phần thưởng, điều kiện kết thúc, giới hạn $500$ bước (Bài tập 08.4).
- Ghi chú bài giảng Bài 06: Định nghĩa 06.3, 06.14, 06.15, 06.19, Thuật toán 06.16, Nhận xét 06.17, Định lý 06.21. Ghi chú bài giảng Bài 07: Định nghĩa 07.1, 07.21, 07.35, 07.38, Mệnh đề 07.2, 07.37, Định lý 07.29, Thuật toán 07.36, Nhận xét 07.39, Ví dụ 07.1.
- Notebook thực hành Bài 04 (`thuc-hanh-cartpole-quy-hoach-dong.ipynb`, phần 2): mô tả CartPole-v1 dùng ở Bài tập 08.4. Notebook Lunar Lander của Bài 07: số liệu của Ví dụ 08.1.
- Giáo trình *Học máy thống kê*: giọng kể, thuật ngữ và tương ứng ký hiệu ($q_*$ là $Q^*$).
