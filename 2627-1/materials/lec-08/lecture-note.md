# Bài 08 — Deep Q-Learning

Trong chương này, chúng ta thay hàm tuyến tính $\hat q(s,a,w)=x(s,a)^\top w$ của Bài 07 bằng một mạng nơ-ron nhận quan sát và trả về một giá trị cho mỗi hành động trong tập hữu hạn, rồi xây dựng thuật toán Deep Q-Network (DQN) từ bốn thành phần: đích hồi quy có mặt nạ kết thúc, bộ nhớ phát lại (experience replay), hàm mất mát với dừng gradient và mạng mục tiêu (target network). Bộ nhớ phát lại và mạng mục tiêu giảm bất ổn khi huấn luyện, nhưng DQN vẫn có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, tức đủ ba yếu tố của bộ ba bất ổn (deadly triad) ở Bài 07, nên thuật toán không có bảo đảm hội tụ tổng quát.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Đọc vector giá trị hành động $\mathbf q_\theta(o)\in\mathbb R^{\lvert\mathcal A\rvert}$ do mạng trả về, chọn giá trị $Q_\theta(o,a)$ của hành động đã thực hiện, và tính đích hồi quy của một mẫu chuyển; phân biệt mẫu kết thúc (đích không chứa phần bootstrap) với mẫu bị cắt ngắn (đích vẫn chứa phần bootstrap).
2. Nêu tác dụng và giới hạn của bộ nhớ phát lại: giảm tương quan giữa các mẫu liền nhau nhưng không tạo dữ liệu độc lập cùng phân phối theo một phân phối cố định; chỉ ra hai nguồn dữ liệu khác chính sách và tính xác suất hai mẫu liền nhau cùng vào một mini-batch.
3. Tính hàm mất mát và gradient của nó theo các dự đoán trên một mini-batch, chỉ ra phần nào không nhận gradient, và truy dấu một vòng của thuật toán DQN với hai bộ đếm $t$ và $k_{\mathrm{opt}}$.
4. Viết hạ gradient ngẫu nhiên (SGD), RMSprop và Adam theo từng tọa độ; nêu điều bộ tối ưu không sửa được: đích bootstrap, phân phối dữ liệu và lớp hàm.
5. Tính độ nhảy của đích một mẫu khi đồng bộ mạng mục tiêu; nêu giả thiết còn thiếu để có bảo đảm hội tụ khi DQN có đủ bộ ba bất ổn.
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
- **Mạng nơ-ron và lan truyền ngược** (kiến thức học máy tiên quyết, không thuộc ghi chú Bài 01–07; Goodfellow, Bengio và Courville, 2016, Chương 6 và 9). Mạng nhiều tầng (multilayer perceptron, MLP) là hợp của các ánh xạ affine và hàm kích hoạt phi tuyến; mạng tích chập (convolutional neural network, CNN) dùng các tầng tích chập có trọng số dùng chung trên mọi vị trí của ảnh. Cả hai là hàm khả vi theo vector tham số $\theta$, và lan truyền ngược (backpropagation) tính gradient của một hàm mất mát vô hướng theo $\theta$ bằng quy tắc dây chuyền. Chương này chỉ dùng mạng như một hàm khả vi theo $\theta$.

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

Một số chữ trùng với bài trước nhưng mang nghĩa khác. $\epsilon_{\mathrm{exp}}$ là $\varepsilon$ của Bài 06–07; chỉ số dưới tách nó khỏi $\epsilon_{\mathrm{opt}}$. $q_i$ là dự đoán của mạng trên mẫu $i$, khác giá trị thật $q_*$. $m_j$, $v_j$ là trung bình trượt của gradient, khác hàm giá trị $v_\pi$; $\rho$ là hệ số suy giảm của RMSprop, khác tỉ số lấy mẫu quan trọng $\rho_t$ của Bài 06–07. Bài 06–07 viết $m$ cho số hành động; chương này viết $\lvert\mathcal A\rvert$. Tham số $\theta$ đóng vai của $w$ ở Bài 07, và $Q_\theta(o,a)$ thay $\hat q(s,a,w)$.

Ứng với giáo trình *Học máy thống kê*: $q_*$ là $Q^*$, và $q_\pi$ là $Q^\pi$.

---

## Bản đồ chủ đề (bốn nhóm)

### Nhóm cầu nối

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-13` | Kiến thức tiên quyết: Q-learning dạng bảng (Bài 06), Q-learning bán gradient và bộ ba bất ổn (Bài 07) | tr. 3–7 | Nhắc quy tắc cập nhật, học khác chính sách, điều kiện hội tụ | Vào: Bài 06–07 → Ra: mục tiêu bootstrap và phạm vi bảo đảm |

### Nhóm cốt lõi

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-01` | Giới hạn của bảng giá trị hành động | tr. 8–15 | Đặt vấn đề quy mô và khái quát hóa | Vào: topic-13 → Ra: nhu cầu $Q_\theta$ |
| `lec-08-topic-16` | Đầu vào bốn khung Atari và tính Markov | tr. 17, 35 | Ví dụ cho giao diện mạng; giới hạn của bốn khung | Vào: topic-01 → Ra: quan sát $O_t$ cho topic-02 |
| `lec-08-topic-02` | Giao diện DQN và hai mạng | tr. 14–17, 20, 31, 33 | Định nghĩa $Q_\theta$, $Q_{\theta^-}$ | Vào: topic-01 → Ra: hai bản sao mạng |
| `lec-08-topic-03` | Bootstrap thành bài toán hồi quy | tr. 16, 20–22, 34 | Đích $y_t$ và sai số TD | Vào: topic-02 → Ra: nhãn hồi quy |
| `lec-08-topic-04` | Kết thúc thật và mặt nạ $(1-Z)$ | tr. 21 | Phân biệt $Z$ và $U$ | Vào: topic-03 → Ra: đích đúng |
| `lec-08-topic-05` | Chuyển tiếp và hai cờ, autoreset | tr. 21 | Hợp đồng dữ liệu | Vào: topic-04 → Ra: bộ sáu thành phần |
| `lec-08-topic-06` | Bộ nhớ phát lại | tr. 19–21, 32 | Cơ chế lưu và lấy mẫu | Vào: topic-05 → Ra: mini-batch |
| `lec-08-topic-07` | Replay giảm tương quan, không tạo i.i.d. | tr. 19, 29–32 | Giới hạn của replay | Vào: topic-06 → Ra: phát biểu đúng phạm vi |
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

Chương đi theo bảy phần, cùng thứ tự với bộ trang chiếu.

1. Mở đầu: kiến thức tiên quyết, ký hiệu, mục tiêu và bài toán trung tâm (`lec-08-topic-13`, `lec-08-topic-01`).
2. Mạng giá trị hành động và đích hồi quy: giới hạn của bảng, đầu vào bốn khung Atari, giao diện mạng, mạng mục tiêu, đích có mặt nạ kết thúc, kết thúc và cắt ngắn (`lec-08-topic-01`, `lec-08-topic-16`, `lec-08-topic-02` đến `lec-08-topic-05`).
3. Bộ nhớ phát lại: tương quan giữa các mẫu chuyển liên tiếp, cơ chế lưu và lấy mẫu đều, dữ liệu khác chính sách, giới hạn (`lec-08-topic-06`, `lec-08-topic-07`).
4. Hàm mất mát và thuật toán DQN: hàm mất mát trên mini-batch, dừng gradient, vòng huấn luyện, kích thước tensor (`lec-08-topic-08` đến `lec-08-topic-11`).
5. Bộ tối ưu theo gradient: SGD, RMSprop, Adam theo từng tọa độ (`lec-08-topic-14`).
6. Bất ổn và phạm vi bảo đảm của DQN: hai nguồn bất ổn, độ nhảy của đích khi đồng bộ, bộ ba bất ổn (`lec-08-topic-12`).
7. Tổng kết và chuyển tiếp: kết quả và giả thiết, bài tập tổng hợp, câu hỏi tự kiểm tra (`lec-08-topic-15`).

Đọc trước: Sutton và Barto (2018), §11.3 (bộ ba bất ổn) và §16.5 (DQN trên trò chơi Atari); Mnih và cộng sự (2015).

---

## 1. Mở đầu

### Bài toán trung tâm của chương

Bài 06 học $q_*$ bằng một bảng có một ô cho mỗi cặp trạng thái–hành động, và Bài 07 thay bảng bằng hàm tuyến tính theo đặc trưng chọn trước. Bài toán của chương này là học $q_*$ khi quan sát là ảnh, tập hành động hữu hạn và mô hình của môi trường không được cho. Với quan sát là ảnh, bảng không lưu được và cũng không có sẵn một bộ đặc trưng chọn tay. Chúng ta dùng một mạng nơ-ron trả về giá trị của mọi hành động và học tham số của mạng từ các mẫu chuyển. Bài giảng gốc (trang 12) nêu bốn khó khăn của bước thay này: hàm mất mát không lồi theo tham số, nên không có bảo đảm hội tụ toàn cục; mục tiêu bootstrap phụ thuộc chính mạng đang học; phân phối dữ liệu đổi theo chính sách hành vi; và phương pháp có đủ bộ ba bất ổn.

Mỗi phần sau của chương trả lời một phần của bài toán, và mỗi câu trả lời đúng dưới một điều kiện.

2. Mạng trả về vector giá trị của mọi hành động. Khi đích được tính bằng một bản sao của mạng giữ cố định giữa hai lần đồng bộ, mỗi mẫu chuyển có một nhãn hồi quy cố định.
3. Khi mini-batch được lấy đều từ bộ nhớ phát lại, tương quan ngắn hạn giữa các mẫu giảm; dữ liệu vẫn chưa độc lập cùng phân phối theo một phân phối cố định.
4. Khi gradient được chặn ở đích, chỉ giá trị dự đoán của hành động đã thực hiện nhận gradient.
5. Bộ tối ưu đổi gradient thành bước tham số; đích bootstrap và phân phối dữ liệu giữ nguyên dù chọn bộ tối ưu nào.
6. Khi có đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, DQN không có bảo đảm hội tụ tổng quát, và các kết luận về hiệu quả của nó dựa trên thí nghiệm.

Bài giảng gốc (trang 9 và 11) còn nêu hai cận độ phức tạp mẫu: $\tilde O\bigl(\lvert\mathcal S\rvert\lvert\mathcal A\rvert/((1-\gamma)^4\varepsilon_{\mathrm{acc}}^2)\bigr)$ mẫu để Q-learning dạng bảng đạt chính sách $\varepsilon_{\mathrm{acc}}$-tối ưu, và $\tilde O\bigl(d/((1-\gamma)^3\varepsilon_{\mathrm{acc}}^2)\bigr)$ cho xấp xỉ hàm với $d$ đặc trưng; ở đây $\varepsilon_{\mathrm{acc}}$ là sai số cho phép của chính sách, khác $\epsilon_{\mathrm{exp}}$. Chúng ta không dùng hai cận này như định lý vì nguồn không nêu mô hình lấy mẫu (mẫu từ một bộ sinh độc lập hay dọc một quỹ đạo), chuẩn đo sai số, xác suất thành công, điều kiện bao phủ và thuật toán cụ thể mà cận áp dụng. Hai ý vẫn dùng ở phần sau: số ô của bảng tăng theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$, và xấp xỉ hàm chỉ có bảo đảm khi có thêm giả thiết cấu trúc, chẳng hạn $q_*$ nằm trong lớp hàm và dữ liệu bao phủ đủ (bài giảng gốc, trang 11).


## 2. Mạng giá trị hành động và đích hồi quy

<!-- note-topic-id: lec-08-topic-01 -->
### Giới hạn của bảng giá trị hành động

**Vấn đề.** Q-learning dạng bảng giữ một ô cho mỗi cặp trạng thái–hành động, và một ô chỉ đổi khi chính cặp đó xuất hiện trong dữ liệu. Bảng có $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$ ô, nên chỉ dùng được khi số trạng thái nhỏ và mỗi cặp được thăm đủ nhiều lần. Ví dụ sau đo hai điều kiện này trên một bài toán điều khiển đã gặp ở Bài 05–07.

::: example Ví dụ 08.1 (Lunar Lander rời rạc hóa thành bảng)
**Dữ kiện.** Thực hành Bài 05 chia sáu biến liên tục của tàu đổ bộ thành $3\cdot4^5=3\,072$ ô và ghép với số chân đang chạm đất ($0$, $1$ hoặc $2$), được $9\,216$ ô trạng thái. Trên $2\,000$ lượt huấn luyện, $1\,896$ ô được ghé ít nhất một lần (notebook Lunar Lander của Bài 07, mục 5; ghi chú Bài 07, Ví dụ 07.1). Tàu có bốn hành động.

**Tính.** Tỉ lệ ô có mẫu là $1\,896/9\,216\approx0{,}206$; $9\,216-1\,896=7\,320$ ô chỉ giữ giá trị khởi tạo. Bảng giá trị hành động trên cùng lưới có $9\,216\cdot4=36\,864$ ô.

**Diễn giải.** Khoảng bốn phần năm số ô trạng thái không có dữ liệu sau $2\,000$ lượt, dù ô bên cạnh đã được ghé nhiều lần; với bảng giá trị hành động, mỗi ô trạng thái còn tách thành bốn ô.
:::

Khi quan sát là ảnh, số quan sát khác nhau có thể gặp quá lớn để liệt kê, và gần như mọi quan sát mới là một ô chưa có mẫu. Bảng vì thế không dùng được, cả về bộ nhớ lẫn về dữ liệu.

**Trực giác.** Thay bảng bằng một hàm có tham số dùng chung $\theta$, chẳng hạn một mạng nơ-ron $Q_\theta(o,a)$ nhận quan sát $o$. Hàm cho giá trị ở cả quan sát chưa gặp, và một cập nhật theo $\theta$ đổi giá trị ở nhiều quan sát cùng lúc. Đây là cơ chế tổng quát hóa của Bài 07 (mức lan của một cập nhật, Mệnh đề 07.2), với mạng thay cho hàm tuyến tính theo đặc trưng chọn trước.

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

Hình đọc từ trái sang phải. Tiền xử lý tác động lên từng khung thô, rồi bốn khung đã xử lý mới được xếp chồng thành $O_t$; mạng nhận $O_t$ và trả về một cột $\lvert\mathcal A\rvert$ giá trị. Bài giảng gốc gọi chồng bốn khung là "đầu vào trạng thái"; chương này gọi là quan sát, vì bốn khung chưa chắc chứa đủ thông tin để thay cho trạng thái Markov, điều được xét ngay sau giao diện của mạng.

Ví dụ 08.2 chỉ cố định giao diện vào và ra của mạng. Tái lập một kết quả Atari đã công bố còn cần số khung lặp lại cho mỗi hành động, cách bắt đầu lượt, kiến trúc cụ thể, siêu tham số và giao thức đánh giá; nguồn không cho các chi tiết này, nên chúng ta không nêu số liệu thành tích.

<!-- note-topic-id: lec-08-topic-02 -->
### Giao diện DQN và hai mạng

**Vấn đề.** Nếu cùng một bộ tham số $\theta$ vừa tạo dự đoán vừa tạo đích
bootstrap, một bước cập nhật có thể đổi cả dự đoán lẫn nhãn — vòng phản hồi di động.

**Trực giác.** Tách hai bản sao của cùng kiến trúc: mạng trực tuyến nhận gradient,
mạng mục tiêu tạo đích và được giữ cố định giữa các lần đồng bộ.

**Ví dụ.** Khởi tạo $\theta$, rồi đặt $\theta^-\leftarrow\theta$. Mạng mục tiêu
không được cập nhật bởi loss; nó chỉ đổi khi được sao chép từ mạng online.

**Hình thức.** Giao diện DQN cho hành động rời rạc:

$$\mathbf q_\theta(o)\in\mathbb R^{|\mathcal A|},\qquad Q_\theta(o,a)=[\mathbf q_\theta(o)]_a.$$

- $Q_\theta$: mạng trực tuyến (online), tham số $\theta$, nhận gradient.
- $Q_{\theta^-}$: mạng mục tiêu (target), tham số $\theta^-$, tạo phần bootstrap,
  cố định giữa hai lần đồng bộ.

Ký hiệu $o$ (quan sát) khi đầu vào chưa chắc đủ Markov; chỉ dùng $s$ khi biểu
diễn đủ Markov.

**Ứng dụng và giới hạn.** Mạng mục tiêu làm chậm vòng phản hồi nhưng không tạo
mục tiêu bất biến vĩnh viễn; nó vẫn đổi tại các mốc đồng bộ. Các lựa chọn kiến
trúc điển hình: MLP cho đặc trưng số chiều thấp, CNN cho đầu vào giống ảnh, hàm
kích hoạt ReLU/tanh/sigmoid; số tầng, độ rộng và cách biểu diễn đầu vào ảnh hưởng
trực tiếp đến năng lực xấp xỉ và độ ổn định.

**Kiểm tra nhanh.** Mạng mục tiêu có nhận gradient từ loss hiện tại không? — Không;
nó chỉ cung cấp phần bootstrap và nằm trong vùng dừng gradient.

### Bốn khung và tính Markov

**Giới hạn.** Bốn khung là lựa chọn thiết kế kinh điển, **không phải định lý bảo
đảm Markov**: nó bổ sung động học ngắn hạn nhưng có thể vẫn thiếu biến ẩn hoặc
lịch sử dài hơn. Một đặc tả tái lập kết quả Atari còn cần tiền xử lý, lặp khung,
khởi đầu episode, kiến trúc, siêu tham số và giao thức đánh giá — nguồn không
cung cấp đầy đủ, nên ghi chú này không bịa các con số đó.

<!-- note-topic-id: lec-08-topic-03 -->
### Bootstrap trở thành bài toán hồi quy

**Vấn đề.** Cập nhật từ điển của Q-learning không cho biết cách cập nhật một mạng;
cần chuyển bootstrap thành một bài toán hồi quy có nhãn.

**Trực giác.** Giữ $Q_{\theta^-}$ cố định, đích trở thành một "nhãn" tạm thời cố
định; mạng online học để dự đoán gần nhãn đó.

**Ví dụ.** Mạng online dự đoán $q_t = Q_\theta(O_t,A_t)$; nhãn hồi quy là

$$y_t = R_{t+1} + \gamma(1-Z_{t+1})\max_{a'}Q_{\theta^-}(O_{t+1},a').$$

Sai số sai phân thời gian: $\delta_t = y_t - q_t$.

**Hình thức.** Đích gồm phần thưởng quan sát được $R_{t+1}$ và một ước lượng
bootstrap từ mạng mục tiêu. Vì $\theta^-$ cố định giữa các lần đồng bộ, đích của
một chuyển tiếp không đổi trong khoảng đó; nó chỉ đổi tại mốc đồng bộ.

**Ứng dụng và giới hạn.** Cách viết này cho phép dùng toàn bộ công cụ hồi quy
(mini-batch, gradient, optimizer), nhưng nhãn vẫn phụ thuộc vào một bản sao gần
đây của chính mạng đang học — nguồn gốc của mục tiêu di động.

**Kiểm tra nhanh.** Đích đổi khi nào? — Chỉ khi $\theta^-$ được đồng bộ; giữa hai
lần đồng bộ, đích của một chuyển tiếp cố định.

<!-- note-topic-id: lec-08-topic-04 -->
### Kết thúc thật làm mất nhánh bootstrap

Quay lại đích hồi quy ở chủ đề trước, bước này xử lý riêng trường hợp chuyển tiếp
kết thúc.

**Vấn đề.** Nếu chỉ viết $y = r + \gamma\max_{a'}Q_{\theta^-}(s',a')$ mà không xử
lý kết thúc, đích tại chuyển tiếp kết thúc sẽ chứa một ước lượng vô nghĩa về
"trạng thái sau khi kết thúc".

**Trực giác.** Mặt nạ $(1-Z)$ triệt tiêu nhánh bootstrap đúng khi quy trình đang
mô hình hóa đã kết thúc.

**Ví dụ.** Cho $\gamma=0{,}9$, $R_{t+1}=-2$,
$\max_{a'}Q_{\theta^-}(O_{t+1},a')=100$:

- Chưa kết thúc ($Z_{t+1}=0$): $y_t = -2 + 0{,}9\cdot 100 = 88$.
- Đã kết thúc ($Z_{t+1}=1$): $y_t = -2$. Giá trị $100$ **không** ảnh hưởng đến đích.

**Hình thức.** $Z_{t+1}=1$ là kết thúc thật của MDP đang mô hình hóa. Mặt nạ nhân
nhánh bootstrap với không, không phải một hiệu chỉnh nhỏ.

**Ứng dụng và giới hạn.** Lỗi phổ biến: dùng một biến `done` đã gộp máy móc
(terminated OR truncated) làm mặt nạ. Cắt ngắn ngoài mô hình ($U=1$) **không** tự
động đặt bootstrap bằng 0 — xem topic-05.

**Kiểm tra nhanh.** Tại chuyển tiếp kết thúc, đích bằng gì? — Đúng bằng phần
thưởng $R_{t+1}$; nhánh bootstrap bị nhân với $0$.

<!-- note-topic-id: lec-08-topic-05 -->
### Một chuyển tiếp cần hai cờ: $Z$ và $U$

**Vấn đề.** Dữ liệu thu thập thực tế có hai sự kiện khác nhau bị gộp thành "done":
kết thúc của nhiệm vụ và việc dừng thu thập do giới hạn bên ngoài.

**Trực giác.** Chỉ kết thúc của MDP mới xóa tương lai; cắt ngắn chỉ dừng *việc thu
thập*, nhiệm vụ tiếp diễn vẫn còn tương lai nên vẫn bootstrap.

**Ví dụ.** Chuyển tiếp lưu trong replay:

$$(O_t, A_t, R_{t+1}, O_{t+1}, Z_{t+1}, U_{t+1}).$$

- $Z_{t+1}=1$: quy trình đang mô hình hóa kết thúc → không bootstrap.
- $U_{t+1}=1$: bộ thu thập dừng (hết thời lượng, hết ngân sách bước); nhiệm vụ
  tiếp diễn thường vẫn bootstrap.

**Hình thức — môi trường tự khởi động lại.** Khi API tự reset sau bước cuối,
quan sát trả về thuộc *lượt mới*, không thuộc chuyển tiếp vừa xảy ra. Replay phải
lưu *quan sát cuối của chuyển tiếp* (ví dụ trường `final_observation`), không thay
bằng quan sát đầu của lượt mới. Mặt nạ trong loss phải theo $Z$ (kết thúc MDP),
không theo một biến done đã gộp.

**Ứng dụng và giới hạn.** Phân biệt đúng hai cờ quyết định đích có đúng nghĩa
Bellman hay không; nhầm $U$ làm $Z$ làm mất giá trị tương lai một cách tùy tiện.

**Kiểm tra nhanh.** $U_i=1$ có nghĩa là không bootstrap không? — Không; $U_i$ là
cắt ngắn do cơ chế thu thập, nhiệm vụ tiếp diễn vẫn bootstrap; chỉ $Z_i=1$ mới
triệt tiêu nhánh bootstrap.

## Bộ nhớ phát lại, hàm mất mát, vòng huấn luyện và bất ổn

<!-- note-topic-id: lec-08-topic-06 -->
### Bộ nhớ phát lại (experience replay)

**Vấn đề.** Học từ các chuyển tiếp liền nhau theo thứ tự thời gian khiến mini-batch
chứa thông tin trùng lặp và lệch theo quỹ đạo gần nhất.

**Trực giác.** Thay vì học từ chuỗi liên tiếp, DQN lưu nhiều chuyển tiếp vào bộ
đệm $\mathcal D$ và huấn luyện trên các bộ sáu thành phần được lấy ngẫu nhiên.

**Ví dụ.** Bộ đệm vòng dung lượng $N\in\mathbb N_+$; mini-batch có $b\in\mathbb N_+$
mẫu với $b\le N$. Lấy đều các vị trí trong $\mathcal D$ và tái sử dụng chuyển tiếp.
Replay trộn cả hành vi khám phá hiện tại lẫn các phiên bản hành vi cũ — đây là
nguồn lệch chính sách thứ hai của DQN (nguồn thứ nhất là $\epsilon$-greedy so với
phép cực đại Bellman).

**Hình thức.** Lưu
$(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ vào $\mathcal D$; lấy ngẫu nhiên
mini-batch từ $\mathcal D$ để tính mất mát. Mất mát DQN cơ bản không gắn tỉ số lấy mẫu quan
trọng vì cùng lý do như Q-learning dạng bảng: $A_i$ là đối số điều kiện của $Q_\theta(O_i,A_i)$,
còn phần tiếp nối tại $O'_i$ được tính trọn bằng phép cực đại, không qua hành động lấy mẫu từ hành vi.

**Ứng dụng và giới hạn.** Lợi ích: phá vỡ tương quan theo thời gian, tái sử dụng
dữ liệu quá khứ, cải thiện hiệu quả mẫu. Giới hạn: xem topic-07.

**Kiểm tra nhanh.** Vì sao loss DQN cơ bản không cần tỉ số lấy mẫu quan trọng? — Vì
$A_i$ đã được cố định trong điều kiện của $Q_\theta(O_i,A_i)$, và hành động tại $O'_i$ không được
lấy mẫu từ hành vi mà được thay bằng phép cực đại, chính là kỳ vọng theo chính sách đích tham lam.

<!-- note-topic-id: lec-08-topic-07 -->
### Replay giảm tương quan, không tạo i.i.d.

**Vấn đề.** Tối ưu mạng nơ-ron thường giả sử mini-batch gần i.i.d.; chuyển tiếp
liên tiếp thu thập trực tuyến tương quan mạnh. Replay có giải quyết triệt để không?

**Trực giác.** Các chuyển tiếp liền nhau đi qua quan sát gần nhau và dùng cùng
phiên bản chính sách; mini-batch liên tiếp có cỡ mẫu hiệu dụng nhỏ hơn số phần tử,
gradient dao động theo đoạn quỹ đạo gần nhất, mạng có thể quá khớp vùng trạng thái
mới và "quên" vùng cũ.

**Ví dụ.** Lấy mẫu từ replay trộn các thời điểm, nhưng các mẫu vẫn có thể chồng
lấn quan sát, đến từ các chính sách hành vi khác nhau, và bộ đệm hữu hạn loại dần
dữ liệu cũ.

**Hình thức — phát biểu đúng phạm vi.**

- Replay *làm được*: giảm tương quan ngắn hạn của mẫu liền nhau; tăng tái sử dụng
  dữ liệu; làm mini-batch đa dạng hơn quỹ đạo mới nhất.
- Replay *không bảo đảm*: độc lập cùng phân phối (i.i.d.); phân phối bộ đệm đứng
  yên; thuật toán hội tụ.

**Ứng dụng và giới hạn.** Dùng từ "giảm", không dùng "loại bỏ" tương quan. Không
nói tương quan luôn làm gradient bị chệch; hệ quả chắc chắn hơn là tự tương quan,
độ đa dạng thấp và phương sai cập nhật phụ thuộc quỹ đạo.

**Kiểm tra nhanh.** Replay có biến dữ liệu thành i.i.d. không? — Không; nó chỉ
giảm tương quan ngắn hạn và tăng tái sử dụng.

<!-- note-topic-id: lec-08-topic-08 -->
### Gather và dừng gradient ở đích

**Vấn đề.** Trong batch, mạng xuất giá trị cho *mọi* hành động, nhưng loss chỉ cần
giá trị của *hành động đã lưu*; đồng thời gradient không được chảy vào đường tạo đích.

**Trực giác.** Hai đường tính tách bạch:

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

**Trực giác.** MSE trung bình trên batch; gradient theo từng $q_i$ tỉ lệ với sai
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

**Trực giác.** Tương tác tạo chuyển tiếp; tối ưu lấy chuyển tiếp đã lưu. Ba siêu
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

**Trực giác.** Mọi tensor trong loss phải khớp hợp đồng: batch quan sát đi qua hai
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

**Trực giác.** Giữ $\theta^-$ cố định trong $C$ bước tối ưu, rồi sao chép mạng
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
