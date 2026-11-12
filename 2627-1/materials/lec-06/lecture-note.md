# Bài 06 — Điều khiển phi mô hình

Trong chương này, chúng ta giải bài toán điều khiển (control) phi mô hình (model-free): học một bảng giá trị hành động (action value) từ các lượt (episode) tương tác và dùng chính bảng ấy để chọn hành động khi chưa biết mô hình môi trường. Chúng ta so sánh ba thuật toán điều khiển Monte Carlo, Sarsa và Q-learning theo dữ liệu cần có trước mỗi cập nhật, theo chính sách mà bảng đánh giá và theo giả thiết của các định lý hội tụ.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Phân biệt giá trị hành động thật $q_\pi$, giá trị hành động tối ưu $q_*$ và bảng ước lượng $Q$; xác định một mẫu chuyển cung cấp thông tin gì và không cung cấp thông tin gì về các cặp trạng thái–hành động (Bài tập 06.1, 06.2, 06.8, 06.14).
2. Tính phân phối của chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy), kể cả khi nhiều hành động đồng hạng, và kiểm tra điều kiện áp dụng của mệnh đề cải thiện chính sách trong lớp $\varepsilon$-mềm (Bài tập 06.2, 06.11, 06.12).
3. Thực hiện điều khiển Monte Carlo theo lần ghé đầu tiên của cặp trạng thái–hành động trên một lượt cho trước, với bộ đếm chỉ tính các lợi tức đã dùng (Bài tập 06.3, 06.10, 06.14, 06.16).
4. Thực hiện từng cập nhật Sarsa và Q-learning, xử lý đúng trạng thái kết thúc (terminal state) và lượt bị cắt ngắn (truncated episode), phân biệt chính sách hành vi với chính sách đích (Bài tập 06.4, 06.5, 06.7, 06.10, 06.13, 06.15, 06.17, 06.18, 06.19).
5. Kiểm tra giả thiết của các định lý hội tụ, gồm độ phủ, điều kiện tham lam trong giới hạn với thăm dò vô hạn (GLIE), điều kiện Robbins–Monro theo cặp, $\gamma<1$ và tính Markov, và phân biệt bảo đảm lý thuyết với việc dừng theo ngân sách (Bài tập 06.6, 06.9, 06.12, 06.13).

Bài tập 06.1–06.13 nằm trong ghi chú; [tệp bài tập](material-viewer.html?doc=materials/lec-06/exercises.md&deck=lecture-06-dieu-khien-phi-mo-hinh.html) chứa Bài tập 06.14–06.19, lấy từ bài tập của Sutton và Barto (2018).

## Kiến thức tiên quyết

Số hiệu `03.k`, `04.k`, `05.k` chỉ ghi chú Bài 03, Bài 04, Bài 05; `06.k` chỉ ghi chú này.

- **Quá trình quyết định Markov và lợi tức** (Định nghĩa 03.2, 03.4, 03.7, 03.9, 03.26; Nhận xét 03.10; Mệnh đề 03.11). Quá trình quyết định Markov (Markov decision process, MDP) hữu hạn được mô tả bởi động lực $p(s',r\mid s,a)$, không phụ thuộc phần lịch sử trước $(s,a)$; dưới một chính sách dừng cố định, dãy trạng thái và phần thưởng tạo một quá trình phần thưởng Markov (Định nghĩa 03.26). Lợi tức (return) từ thời điểm $t$ là $G_t=\sum_{j=t}^{T-1}\gamma^{j-t}R_{j+1}$ với $G_T=0$; khi phần thưởng bị chặn bởi $R_{\max}$ và $0\le\gamma<1$ thì $|G_t|\le R_{\max}/(1-\gamma)$.
- **Giá trị trạng thái và giá trị hành động** (Định nghĩa 03.15, 03.16; Bổ đề 03.20(c), (d); Mệnh đề 03.6, 03.22, 03.23). Với chính sách dừng (stationary policy) $\pi$, giá trị trạng thái (state value) là $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ và giá trị hành động là $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$. Hai hàm liên hệ bởi $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$ và $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$, trong đó $r(s,a)$ là phần thưởng kỳ vọng và $p(s'\mid s,a)$ là xác suất chuyển suy ra từ $p(s',r\mid s,a)$.
- **Toán tử Bellman của một chính sách** (Định nghĩa 04.1, 04.3; Bổ đề 04.2; Mệnh đề 04.4; Hệ quả 04.6). Toán tử Bellman đánh giá (Bellman operator) $T_\pi$ biến bảng $u$ thành $(T_\pi u)(s)=\sum_a\pi(a\mid s)\big[r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)u(s')\big]$; nó đơn điệu, và khi $0\le\gamma<1$ là ánh xạ co (contraction) hệ số $\gamma$ theo chuẩn vô cùng $\lVert\cdot\rVert_\infty$ (còn gọi là chuẩn cực đại; max norm) với điểm bất động duy nhất $v_\pi$.
- **Định lý cải thiện chính sách** (Định nghĩa 04.12, Định lý 04.13). Trong MDP hữu hạn có phần thưởng bị chặn và $0\le\gamma<1$, với $\pi$ là chính sách dừng: nếu $\pi'$ là chính sách dừng xác định với $q_\pi(s,\pi'(s))\ge v_\pi(s)$ tại mọi $s$, chẳng hạn chính sách tham lam (greedy policy) theo $q_\pi$, thì $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s$; đó là bước cải thiện chính sách (policy improvement).
- **Giá trị tối ưu** (Định nghĩa 04.19, 04.22; Bổ đề 04.23; Mệnh đề 04.24; Định lý 04.25). Trong MDP hữu hạn có phần thưởng bị chặn và $0\le\gamma<1$, giá trị tối ưu (optimal value) $v_*(s)$ là cận trên đúng (supremum) của $v_\pi(s)$ trên mọi chính sách, kể cả chính sách phụ thuộc lịch sử, và $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_*(s')]$. Toán tử Bellman tối ưu (Bellman optimality operator) $T_*$ là ánh xạ co, nhờ bất đẳng thức $\lvert\max_ax_a-\max_ay_a\rvert\le\max_a\lvert x_a-y_a\rvert$; tồn tại một chính sách dừng xác định tối ưu, và $v_*(s)=\max_aq_*(s,a)$.
- **Monte Carlo dự đoán và trung bình gia tăng** (Định nghĩa 05.6, 05.8; Mệnh đề 05.9; Thuật toán 05.13). Monte Carlo (MC) dự đoán ước lượng $v_\pi(s)$ bằng trung bình các lợi tức sau các lần ghé $s$; lần ghé đầu tiên (first-visit) chỉ dùng lần ghé có chỉ số thời gian nhỏ nhất trong lượt, mọi lần ghé (every-visit) dùng tất cả. Trung bình của $n$ lợi tức $g_1,\dots,g_n$ tính được bằng truy hồi trung bình gia tăng (incremental mean) $V_n=V_{n-1}+(g_n-V_{n-1})/n$, với bộ đếm tăng trước khi dùng.
- **Sai phân thời gian TD(0) và khung cập nhật** (Định nghĩa 05.10, 05.20; Thuật toán 05.21). Sai phân thời gian (temporal difference, TD) một bước, TD(0), cập nhật $V(S_t)\leftarrow V(S_t)+\alpha\big[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\big]$, với $V=0$ tại trạng thái kết thúc. Cả hai có dạng $V\leftarrow V+\alpha[\text{mục tiêu}-V]$; mục tiêu bootstrap (bootstrap target) là mục tiêu chứa một giá trị ước lượng.
- **Hội tụ của TD(0) và điều kiện Robbins–Monro theo trạng thái** (Định lý 05.30; Bài tập 05.11). Với tập trạng thái hữu hạn, chính sách $\pi$ cố định, dữ liệu sinh theo $\pi$, phần thưởng bị chặn, $\gamma<1$ (hoặc $\gamma=1$ khi mọi lượt dưới $\pi$ kết thúc với xác suất $1$), mỗi trạng thái được cập nhật vô hạn lần và bước học (step size, learning rate) $\alpha_n(s)\in[0,1]$ ở lần cập nhật thứ $n$ của $s$ thỏa $\sum_n\alpha_n(s)=\infty$, $\sum_n\alpha_n(s)^2<\infty$, TD(0) hội tụ hầu chắc chắn (almost surely) tới $v_\pi$. Lịch $\alpha_n=1/n$ thỏa hai tổng, bước hằng không thỏa tổng thứ hai, và theo Bài tập 05.11, $\alpha_n=n^{-p}$ thỏa khi và chỉ khi $1/2<p\le1$.
- **Xác suất và chuỗi số.** Kỳ vọng có điều kiện và luật kỳ vọng lặp (law of iterated expectations); hội tụ hầu chắc chắn là hội tụ trên một biến cố có xác suất $1$. Chuỗi $\sum_n n^{-p}$ hội tụ khi và chỉ khi $p>1$.

## Bảng ký hiệu

Bảng gồm ký hiệu dùng xuyên suốt chương; ký hiệu dùng cục bộ được giới thiệu tại chỗ. Trừ các ngoại lệ nêu sau bảng, mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái không kết thúc; tập có thêm các trạng thái kết thúc | tập hữu hạn |
| $\mathcal A(s)$, $m(s)$ | tập hành động hợp lệ tại $s\in\mathcal S$; số phần tử của nó | tập hữu hạn khác rỗng; số nguyên $m(s)\ge1$ |
| $M$ | số cặp trạng thái–hành động hợp lệ, $M=\sum_{s\in\mathcal S}m(s)$ | số nguyên dương |
| $t$, $T$ | chỉ số bước trong lượt; thời điểm kết thúc của lượt | $t\in\{0,1,\dots\}$; $T$ nguyên dương hoặc $\infty$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động tại bước $t$; phần thưởng của chuyển từ $t$ sang $t+1$ | $\mathcal S^+$; $\mathcal A(S_t)$; $\mathbb R$ |
| $p(s',r\mid s,a)$ | động lực của môi trường; tác tử không biết | phân phối trên $\mathcal S^+\times\mathbb R$ |
| $p(s'\mid s,a)$, $r(s,a)$ | xác suất chuyển; phần thưởng kỳ vọng, suy ra từ $p(s',r\mid s,a)$ | $[0,1]$; $\mathbb R$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; các định lý dùng $[0,1)$ |
| $G_t$ | lợi tức từ thời điểm $t$, $G_T=0$ | biến ngẫu nhiên thực |
| $\pi(a\mid s)$, $b(a\mid s)$ | chính sách đích; chính sách hành vi | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $\pi_k$, $\pi_t$ | chính sách dùng trong lượt $k$; chính sách dùng để chọn hành động ở bước $t$ | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $\pi_L$, $\pi_I$ | chính sách luôn đi trái; chính sách tham lam theo bảng khởi tạo nghiêng phải | chính sách tất định trên dãy năm ô |
| $v_\pi$, $q_\pi$ | giá trị trạng thái và giá trị hành động thật của $\pi$ | $\mathcal S\to\mathbb R$; cặp hợp lệ $\to\mathbb R$ |
| $v_*$, $q_*$ | giá trị trạng thái tối ưu; giá trị hành động tối ưu | $\mathcal S\to\mathbb R$; cặp hợp lệ $\to\mathbb R$ |
| $Q$, $Q_t$, $Q^{[k]}$ | bảng ước lượng; bảng ngay trước cập nhật ở bước $t$; bảng trước lượt $k$ | $\mathbb R^M$ |
| $V$, $V_t$ | bảng ước lượng giá trị trạng thái; bảng tại bước $t$ | $\mathbb R^{\lvert\mathcal S\rvert}$ |
| $\varepsilon$, $\varepsilon_k$ | tham số thăm dò; giá trị dùng trong lượt $k$ | $[0,1]$ |
| $\mathcal G_Q(s)$, $\pi_\varepsilon$ | tập hành động đạt cực đại của hàng $s$ trong $Q$; chính sách $\varepsilon$-tham lam theo $Q$ | tập con khác rỗng của $\mathcal A(s)$; phân phối |
| $N(s,a)$ | số lợi tức Monte Carlo đã dùng cho cặp $(s,a)$ | $\{0,1,\dots\}$ |
| $f(s,a)$ | lần ghé đầu tiên của cặp $(s,a)$ trong một lượt | $\{0,\dots,T-1\}$ |
| $n(s,a)$, $\alpha_n(s,a)$ | số cập nhật đã hoàn thành của cặp; bước học ở lần cập nhật thứ $n$ của cặp | $\{0,1,\dots\}$; $(0,1]$ |
| $\alpha_t$ | bước học dùng ở bước $t$, $\alpha_t=\alpha_{n(S_t,A_t)+1}(S_t,A_t)$ | $(0,1]$ |
| $Y_t$, $\delta_t$ | mục tiêu cập nhật; sai lệch $Y_t-Q_t(S_t,A_t)$ | $\mathbb R$ |
| $C_t(s,a)$ | số lần cặp $(s,a)$ được thực hiện trong các bước $0,\dots,t$ | $\{0,1,\dots\}$ |
| $K$, $H$, $h$ | ngân sách số lượt (Monte Carlo); ngân sách số cập nhật; số cập nhật đã làm | số nguyên dương; số nguyên không âm |
| $d_0$ | phân phối trạng thái đầu của mỗi lượt | phân phối trên $\mathcal S$ |
| $T_\pi$, $T_*$ | toán tử Bellman của chính sách $\pi$; toán tử Bellman tối ưu | ánh xạ trên bảng $\mathcal S\to\mathbb R$ |
| $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ | tên năm ô của ví dụ xuyên suốt | nhãn, không phải biến |

Các quy ước đọc của chương bao gồm:

- $R_{t+1}$ là phần thưởng nhận được trên chuyển từ $S_t$ sang $S_{t+1}$ sau hành động $A_t$;
- giá trị của mọi trạng thái kết thúc bằng $0$, trong cả hàm thật lẫn bảng ước lượng;
- kỳ vọng $\mathbb E_\pi$ lấy theo cả chính sách $\pi$ lẫn động lực $p$;
- bất đẳng thức giữa hai hàm hiểu theo từng trạng thái;
- tên ô viết chữ đứng ($\mathrm A$ khác hành động $A_t$, $\mathrm B$ khác chính sách hành vi $b$).

Một số chữ có thêm nghĩa cục bộ:

- $k$ ngoài chỉ số lượt còn làm chỉ số chạy trong tổng;
- $n$ ngoài số cập nhật của một cặp còn là số lượt đánh giá ở Mục 6 và chỉ số của dãy $t_n$;
- $p$ trong lịch $\alpha_n=n^{-p}$ là số mũ;
- $B$ chữ nghiêng ở Mục 6 là độ rộng khoảng chứa lợi tức.

Tương ứng với giáo trình *Học máy thống kê*: $v_\pi$, $q_\pi$ là $V^\pi$, $Q^\pi$; $p(s',r\mid s,a)$ thay cho $T(s,a,s')$, $R(s,a,s')$, và bộ $\langle S,A,T,R,\gamma\rangle$ ứng với $(\mathcal S,\mathcal A,p)$ cùng $\gamma$; mục tiêu $Y_t$ là "giá trị mục tiêu".

<!-- note-topic-id: lec-06-topic-01 -->
## 1. Giá trị hành động và thăm dò

Trong Bài 05, chúng ta đã ước lượng $v_\pi$ của một chính sách cố định chỉ từ các lượt tương tác, bằng Monte Carlo hoặc TD(0) (Thuật toán 05.13, 05.21). Trong Bài 04, chúng ta đã cải thiện một chính sách bằng cách chọn hành động có $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$ lớn nhất (Định lý 04.13). Hai công cụ này chưa ghép được: bước cải thiện cần $p(s'\mid s,a)$ và $r(s,a)$, đúng những đại lượng bài toán phi mô hình không cho.

Bài toán sau làm rõ chỗ thiếu. Trên một dãy năm ô A–B–C–D–E, mỗi lượt bắt đầu tại ô D và tác tử (agent) chọn đi trái hoặc đi phải. Đi phải từ D kết thúc lượt ngay tại E với phần thưởng $10$; đi trái ba lần qua C, B tới A cho các phần thưởng $-1$, $-1$, $1000$, tổng cộng $998$. Tác tử không biết các con số này; nó chỉ thấy những mẫu chuyển (transition sample) đã xảy ra. Một ước lượng $V(\mathrm D)$ theo kiểu Bài 05 gộp kết quả của cả hai hành động thành một số, còn tách hai hướng bằng $r+\gamma V(s')$ lại cần biết mỗi hành động dẫn tới đâu.

Để chọn hành động tại D mà không có mô hình, chúng ta cần ước lượng trực tiếp giá trị của từng cặp trạng thái–hành động, và cần một cách chọn hành động vẫn thử hướng chưa được ưu tiên. Chúng ta xây dựng:

- bảng giá trị hành động và chính sách $\varepsilon$-tham lam, cùng bảo đảm rằng bước cải thiện $\varepsilon$-tham lam không làm giảm giá trị (Mệnh đề 06.6);
- ba cách tạo mục tiêu cho bảng: điều khiển Monte Carlo, Sarsa và Q-learning (Thuật toán 06.9, 06.12, 06.16);
- giả thiết để bảng hội tụ tới giá trị tối ưu (Định lý 06.21, 06.22).

![Sơ đồ ba tầng. Trên: Mục 1, bảng Q theo cặp, chính sách ε-tham lam, Mệnh đề 06.6. Giữa: khung Q(S,A) ← Q(S,A) + α[Y − Q(S,A)] và ba ô Mục 2 Monte Carlo (Y = G), Mục 3 Sarsa (Y = R + γQ(S′,A′)), Mục 4 Q-learning (Y = R + γ max Q(S′,·)). Dưới: Mục 5, GLIE và Robbins–Monro theo cặp cho Q → q*, Định lý 06.21, 06.22; mũi tên từ Monte Carlo là nét đứt vì Định lý 06.21, 06.22 không áp dụng cho điều khiển Monte Carlo (Nhận xét 06.23)](img/lec-06/chapter-structure.svg)

Hình trên đọc từ trên xuống. Ô trên cùng là đối tượng chung của ba thuật toán: bảng $Q$ theo cặp và chính sách $\varepsilon$-tham lam. Ba ô hàng giữa dùng chung khung cập nhật ở dải giữa và chỉ khác nhau ở mục tiêu cập nhật (update target) $Y$, nên cần dữ liệu khác nhau trước khi cập nhật. Mũi tên nét đứt từ Monte Carlo chỉ rằng với điều khiển Monte Carlo, các lợi tức trong một ô đến từ nhiều chính sách, nên trung bình mẫu và Mệnh đề 06.6 không ghép thành chứng minh hội tụ tới $q_*$ (Nhận xét 06.23).

<!-- note-topic-id: lec-06-topic-02 -->
### 1.1 Giá trị của từng hành động tại một trạng thái

Để so sánh hai hành động tại D, chúng ta cần một đại lượng gắn với cặp $(\mathrm D,0)$ và một đại lượng gắn với cặp $(\mathrm D,1)$, đo được từ mẫu. Trước hết, chúng ta cố định môi trường dùng xuyên suốt chương.

::: example Ví dụ 06.1 (Dãy năm ô)
**Dữ kiện.** Năm ô xếp thành hàng A–B–C–D–E. Tập trạng thái không kết thúc là $\mathcal S=\{\mathrm B,\mathrm C,\mathrm D\}$; thêm hai trạng thái kết thúc A và E được $\mathcal S^+=\{\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E\}$. Tại mỗi $s\in\mathcal S$, tập hành động là $\mathcal A(s)=\{0,1\}$: hành động $0$ đi sang ô bên trái, hành động $1$ đi sang ô bên phải. Chuyển là tất định. Phần thưởng gắn với ô vừa đi tới:

| Ô đi tới | Phần thưởng |
|---|---:|
| A | $1000$ |
| E | $10$ |
| B, C hoặc D | $-1$ |

Mỗi lượt bắt đầu tại D, hệ số chiết khấu là $\gamma=1$, và lượt kết thúc khi vào A hoặc E. Có ba trạng thái không kết thúc, mỗi trạng thái hai hành động, nên số cặp hợp lệ là $M=3\cdot2=6$.

**Tính hai lợi tức từ D.** Lượt "đi phải ngay" là D→E, một chuyển, nên $G_0=10$. Lượt "đi trái ba lần" là D→C→B→A với ba phần thưởng $-1,-1,1000$, nên

$$
G_0=-1+(-1)+1000=998 .
$$

**Kiểm tra lại.** Tính lùi từ cuối lượt thứ hai: $G_2=1000$, $G_1=-1+1000=999$, $G_0=-1+999=998$, khớp kết quả trên.
:::

![Dãy năm ô A, B, C, D, E xếp ngang. A và E ghi "kết thúc", D ghi "bắt đầu". Mỗi cạnh ghi hành động và phần thưởng: từ B sang A là hành động 0 với phần thưởng 1000; giữa B, C, D các cạnh sang trái là hành động 0 với phần thưởng −1, sang phải là hành động 1 với phần thưởng −1; từ D sang E là hành động 1 với phần thưởng 10.](img/lec-06/chain-five-states.svg)

Trên hình, mỗi cạnh mang nhãn "hành động · phần thưởng", tức phần thưởng $R_{t+1}$ được nhận trên chuyển chứ không phải tại ô xuất phát. Hai ô ngoài cùng là trạng thái kết thúc: sau khi vào A hoặc E không còn hành động nào, và giá trị tiếp nối tại đó bằng $0$ vì phần thưởng cuối đã được tính trên cạnh.

Hai lợi tức $998$ và $10$ của Ví dụ 06.1 đã gợi ý rằng đi trái tốt hơn, nhưng $998$ còn phụ thuộc vào việc tác tử tiếp tục đi trái ở C và B. Trong khi học, tác tử chỉ có một bảng số do chính nó khởi tạo và cập nhật. Xét bảng khởi tạo sau.

::: example Ví dụ 06.2 (Bảng khởi tạo nghiêng phải)
**Dữ kiện.** Dãy năm ô của Ví dụ 06.1. Bảng khởi tạo gán một số cho mỗi cặp:

| Trạng thái | $Q_0(s,0)$: trái | $Q_0(s,1)$: phải |
|---|---:|---:|
| B | $0$ | $1$ |
| C | $1$ | $0$ |
| D | $0$ | $1$ |

Chúng ta gọi bảng này là bảng khởi tạo nghiêng phải, vì tại ô bắt đầu D nó xếp hành động phải trên hành động trái.

**Đọc bảng.** Hành động có số lớn nhất trong mỗi hàng là: phải tại B ($1>0$), trái tại C ($1>0$), phải tại D ($1>0$).

**Đối chiếu với lợi tức.** Tại D, bảng xếp phải ($1$) trên trái ($0$), ngược với thứ tự của hai lợi tức $10<998$ ở Ví dụ 06.1. Các số trong bảng chưa đến từ quan sát nào.

**Kiểm tra lại.** Bảng có $6$ ô, bằng số cặp $M=6$ của Ví dụ 06.1.
:::

Nhắc lại từ Bài 03: giá trị của hành động $a$ tại trạng thái $s$ dưới chính sách $\pi$ là lợi tức trung bình khi cố định hành động đầu là $a$ rồi để $\pi$ quyết định mọi hành động sau đó (Định nghĩa 03.16). Ví dụ sau tính đại lượng này trên dãy năm ô.

::: example Ví dụ 06.3 (Chính sách luôn đi trái)
**Dữ kiện.** Dãy năm ô của Ví dụ 06.1, $\gamma=1$. Chính sách $\pi_L$ chọn hành động $0$ (trái) với xác suất $1$ tại B, C và D.

**Hành động đầu là $0$.** Từ D đi trái tới C, nhận $-1$. Từ đó $\pi_L$ đi trái tới B, nhận $-1$, rồi tới A, nhận $1000$. Lợi tức là $-1-1+1000=998$.

**Hành động đầu là $1$.** Từ D đi phải tới E, nhận $10$, lượt kết thúc; chính sách tiếp nối không được dùng tới. Lợi tức là $10$.

**Diễn giải.** Hai số cùng dùng chính sách tiếp nối $\pi_L$ và chỉ khác hành động đầu. Vì chuyển và $\pi_L$ đều tất định, mỗi kỳ vọng bằng đúng một lợi tức.

**Kiểm tra lại.** Vì $\pi_L$ chọn $0$ tại D với xác suất $1$, $v_{\pi_L}(\mathrm D)=\sum_a\pi_L(a\mid\mathrm D)\,q_{\pi_L}(\mathrm D,a)=1\cdot998+0\cdot10=998$.
:::

Ở dạng ký hiệu, với chính sách dừng $\pi$,

$$
q_\pi(s,a)=\mathbb E_\pi\big[G_t\mid S_t=s,\ A_t=a\big],
$$

trong đó điều kiện $A_t=a$ cố định hành động đầu, còn các hành động $A_{t+1},A_{t+2},\dots$ lấy theo $\pi$ và các chuyển lấy theo $p$. Ví dụ 06.3 cho $q_{\pi_L}(\mathrm D,0)=998$ và $q_{\pi_L}(\mathrm D,1)=10$. Đối tượng mới của chương là bảng mà tác tử dùng để xấp xỉ các giá trị này và giá trị tốt nhất có thể đạt được.

::: definition Định nghĩa 06.1 (Bảng giá trị hành động)
Bảng giá trị hành động là một hàm $Q$ gán cho mỗi cặp hợp lệ $(s,a)$, với $s\in\mathcal S$ và $a\in\mathcal A(s)$, một số thực $Q(s,a)$; bảng có $M$ ô. Bảng được khởi tạo bằng một bảng $Q_0$ cho trước và chỉ thay đổi qua các cập nhật từ mẫu. Với trạng thái kết thúc $s$, quy ước $Q(s,\cdot)=0$.
:::

Đích mà bảng xấp xỉ có thể là giá trị hành động tối ưu (optimal action value). Nhắc lại Định nghĩa 04.19: trong MDP hữu hạn có phần thưởng bị chặn và $0\le\gamma<1$, $v_*(s)$ là cận trên đúng của $v_\pi(s)$ trên mọi chính sách, và $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_*(s')]$. Với mọi chính sách dừng $\pi$, $v_\pi\le v_*$, nên theo Mệnh đề 03.22 ta có $q_\pi\le q_*$. Theo Định lý 04.25(b), tồn tại chính sách dừng xác định $\pi_*$ với $v_{\pi_*}=v_*$, và với chính sách này $q_{\pi_*}=q_*$. Do đó $q_*(s,a)=\max_\pi q_\pi(s,a)$, với cực đại lấy trên các chính sách dừng và đạt tại $\pi_*$.

Chúng ta giữ riêng ba đối tượng:

- $q_\pi$: một hàm xác định bởi chính sách $\pi$ và môi trường, không phụ thuộc dữ liệu;
- $q_*$: giá trị tốt nhất của mỗi cặp;
- $Q$ (Định nghĩa 06.1): một bảng số do thuật toán giữ, ước lượng của $q_\pi$ hoặc $q_*$ tùy thuật toán, có thể sai tùy ý trước khi có dữ liệu.

Bảng của Ví dụ 06.2 là phản ví dụ cho việc đồng nhất $Q$ với $q_\pi$. Hành động $1$ tại D luôn kết thúc lượt với phần thưởng $10$, nên $q_\pi(\mathrm D,1)=10$ với mọi chính sách $\pi$. Bảng khởi tạo lại ghi $Q_0(\mathrm D,1)=1$, thấp hơn $9$ đơn vị so với giá trị thật của mọi chính sách.

Bảng $Q$ mở rộng bảng $V$ của Bài 05 từ trạng thái sang cặp trạng thái–hành động: thay vì $|\mathcal S|$ ô, bảng có $M=\sum_sm(s)$ ô, với $m(s)$ là số hành động hợp lệ tại $s$. Phép mở rộng này là cái giá để bỏ mô hình: đổi lại, việc chọn hành động theo $Q$ chỉ cần so các số trong một hàng, không cần $p$ và $r$.

Quan hệ $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$ cho thấy $v_\pi$ là trung bình của một hàng $q_\pi$ theo $\pi$, nên một hàng $Q$ chứa nhiều thông tin hơn một ô $V$. Khác biệt giữa $q_\pi$ và $q_*$ là khác biệt giữa dự đoán (prediction) và điều khiển: bài toán dự đoán ước lượng $q_\pi$ cho một $\pi$ cố định, còn bài toán điều khiển vừa ước lượng vừa đổi $\pi$ với đích là $q_*$.

Định nghĩa của $q_*$ dùng $0\le\gamma<1$, còn dãy năm ô dùng $\gamma=1$; với hệ số này, một chính sách tất định có thể không có giá trị hữu hạn.

::: remark Nhận xét 06.2 (Vòng B–C và lợi tức không hữu hạn)
Gọi $\pi_I$ là chính sách tất định chọn hành động có số lớn nhất của bảng khởi tạo nghiêng phải (Ví dụ 06.2): phải tại B, trái tại C, phải tại D. Bắt đầu từ D, $\pi_I$ đi phải tới E và kết thúc. Nếu hành động đầu tại D là trái, tác tử tới C rồi theo $\pi_I$ đi C→B→C→B→… mãi mãi, mỗi bước nhận $-1$.

Với $\gamma=1$, lợi tức sau $k$ bước của vòng này là $-k$, giảm không giới hạn, nên kỳ vọng định nghĩa $q_{\pi_I}(\mathrm D,0)$ không là một số thực. Số $998$ của Ví dụ 06.3 là $q_{\pi_L}(\mathrm D,0)$, không thể gán cho $(\mathrm D,0)$ dưới chính sách tiếp nối $\pi_I$.

Với $\gamma=0{,}9$, cùng vòng ấy cho giá trị hữu hạn. Từ C và từ B, lợi tức là $-\sum_{k\ge0}0{,}9^k=-10$, nên $q_{\pi_I}(\mathrm D,0)=-1+0{,}9\cdot(-10)=-10$, trong khi $q_{\pi_I}(\mathrm D,1)=10$. Giả thiết $\gamma<1$ trong định nghĩa $q_*$ và trong các định lý hội tụ (Định lý 06.21, 06.22) bảo đảm mọi chính sách có giá trị hữu hạn, nên loại bỏ tình huống này.

Tuy vậy, cận trên đúng của lợi tức kỳ vọng trên các chính sách vẫn hữu hạn: mọi lượt kết thúc từ D có lợi tức không vượt $998$, đạt bởi $\pi_L$, còn mọi quỹ đạo không kết thúc có lợi tức tiến tới $-\infty$.
:::

![Dãy năm ô với các mũi tên của chính sách tham lam theo bảng khởi tạo nghiêng phải: từ B sang C là hành động 1 với phần thưởng −1, từ C sang B là hành động 0 với phần thưởng −1, từ D sang E là hành động 1 với phần thưởng 10; D ghi "bắt đầu tại D", A và E ghi "kết thúc".](img/lec-06/greedy-chain.svg)

Hình trên vẽ các mũi tên của $\pi_I$: hai mũi tên giữa B và C tạo một chu trình không qua trạng thái kết thúc, còn mũi tên D→E là lý do lượt bắt đầu tại D theo $\pi_I$ vẫn kết thúc.

::: exercise Bài tập 06.1 (Thông tin trong một mẫu chuyển)
Trên dãy năm ô của Ví dụ 06.1 ($\mathcal S=\{\mathrm B,\mathrm C,\mathrm D\}$, hành động $0$ trái và $1$ phải, A và E kết thúc), tác tử ghi được mẫu $(\mathrm D,1,10,\mathrm E)$ theo thứ tự trạng thái, hành động, phần thưởng, trạng thái kế tiếp.

1. Xác định trạng thái, hành động, phần thưởng, trạng thái kế tiếp, và số hành động còn thực hiện trong lượt sau mẫu này.
2. Xác định mẫu này cung cấp dữ liệu gì về cặp $(\mathrm D,0)$.
3. Giải thích vì sao muốn so sánh hai hành động tại D, tác tử phải giữ hai ô riêng $Q(\mathrm D,0)$ và $Q(\mathrm D,1)$.
:::

::: hint
Đọc bộ bốn theo thứ tự đã cho. Phân biệt hành động đã được thực hiện với hành động chưa xuất hiện trong dữ liệu, và dùng quy ước kết thúc tại A, E.
:::

::: solution
**Câu 1.** Trạng thái là D, hành động là $1$ (phải), phần thưởng là $10$, trạng thái kế tiếp là E. Vì E là trạng thái kết thúc, không còn hành động nào trong lượt.

**Câu 2.** Mẫu không chứa lần thực hiện hành động $0$ tại D, nên không cho dữ liệu nào về cặp $(\mathrm D,0)$.

**Câu 3.** Mẫu $(\mathrm D,1,10,\mathrm E)$ chỉ là một quan sát của cặp $(\mathrm D,1)$. Nếu chỉ giữ một ô $V(\mathrm D)$, quan sát này trộn với các quan sát sau hành động trái. Hai ô riêng cho phép so sánh $Q(\mathrm D,0)$ với $Q(\mathrm D,1)$ mà không cần mô hình.

**Kiểm tra lại.** Mẫu có đúng một hành động là $1$, nên chỉ ô $(\mathrm D,1)$ có thể được cập nhật từ nó. Hai lỗi thường gặp: dùng $998$ như một dữ liệu về $(\mathrm D,0)$, trong khi số này chỉ tính được khi biết mô hình; và coi $10$ là giá trị của trạng thái D, khi đó hai hành động bị trộn vào một ô.
:::

### 1.2 Thăm dò và chính sách $\varepsilon$-tham lam

Giả sử tác tử luôn chọn hành động có số lớn nhất trong bảng hiện tại. Với bảng khởi tạo nghiêng phải, mọi lượt đều là D→E, và ô $Q(\mathrm D,0)$ không bao giờ nhận một mẫu nào: nó giữ mãi giá trị $0$, trong khi đi trái liên tục cho lợi tức $998>10$. Cách chọn hành động quyết định ô nào của bảng nhận dữ liệu, nên để bảng có cơ hội sửa sai, chúng ta cần một quy tắc vẫn thử các hành động chưa được ưu tiên.

![Bốn ô nối thành vòng: Tương tác → Dữ liệu → Cập nhật Q → Chính sách, và mũi tên quay lại từ Chính sách về Tương tác ghi "chọn hành động cho tương tác tiếp".](img/lec-06/control-loop.svg)

Hình trên vẽ vòng của bài toán điều khiển: chính sách sinh dữ liệu, dữ liệu cập nhật bảng $Q$, bảng xác định chính sách cho lần tương tác sau. Mũi tên quay lại là điểm khác với bài toán dự đoán của Bài 05, nơi chính sách cố định.

Về mặt ý tưởng, tác tử dành phần lớn xác suất cho hành động tốt nhất theo bảng hiện tại (khai thác, exploitation) và dành một phần nhỏ $\varepsilon$ để chọn đều trong mọi hành động (thăm dò, exploration). Khi nhiều hành động cùng đạt cực đại, không có lý do ưu tiên hành động nào, nên phần khai thác được chia đều cho chúng. Ví dụ sau tính cụ thể các xác suất.

::: example Ví dụ 06.4 (Xác suất chọn hành động tại D)
**Dữ kiện.** Hàng D của bảng khởi tạo nghiêng phải là $Q(\mathrm D,0)=0$, $Q(\mathrm D,1)=1$; tại D có $m(\mathrm D)=2$ hành động. Tham số thăm dò $\varepsilon=1/4$.

**Nhánh thăm dò.** Với xác suất $1/4$, chọn đều trong hai hành động; mỗi hành động nhận $\tfrac14\cdot\tfrac12=\tfrac18$.

**Nhánh khai thác.** Với xác suất $1-\tfrac14=\tfrac34$, chọn hành động cực đại duy nhất là $1$.

**Cộng hai nhánh.**

$$
\begin{aligned}
\Pr(A=0\mid\mathrm D)&=\frac18,\\
\Pr(A=1\mid\mathrm D)&=\frac34+\frac18=\frac78 .
\end{aligned}
$$

**Trường hợp đồng hạng.** Nếu $Q(\mathrm D,0)=Q(\mathrm D,1)=1$, phần khai thác $\tfrac34$ chia đều thành $\tfrac38$ cho mỗi hành động, nên mỗi hành động có xác suất $\tfrac18+\tfrac38=\tfrac12$.

**Kiểm tra lại.** $\tfrac18+\tfrac78=1$ và $\tfrac12+\tfrac12=1$.
:::

Trong Ví dụ 06.4, nhánh thăm dò chọn trong toàn bộ tập hành động, kể cả hành động cực đại, nên hành động không cực đại có xác suất $\varepsilon/m(s)=1/8$. Định nghĩa sau viết quy tắc này cho mọi trạng thái và mọi số hành động.

::: definition Định nghĩa 06.3 (Chính sách $\varepsilon$-tham lam)
Cho bảng $Q$, trạng thái $s\in\mathcal S$ với $m(s)=|\mathcal A(s)|$ hành động, và $\varepsilon\in[0,1]$. Tập hành động cực đại của hàng $s$ là

$$
\mathcal G_Q(s)=\operatorname*{arg\,max}_{a\in\mathcal A(s)}Q(s,a),
$$

một tập con khác rỗng của $\mathcal A(s)$. Chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy) theo $Q$ là

$$
\pi_\varepsilon(a\mid s)=\frac{\varepsilon}{m(s)}+(1-\varepsilon)\,\frac{\mathbf 1\{a\in\mathcal G_Q(s)\}}{|\mathcal G_Q(s)|},\qquad a\in\mathcal A(s),
$$

trong đó $\mathbf 1\{\cdot\}$ bằng $1$ khi điều kiện trong ngoặc đúng và bằng $0$ khi sai.
:::

Công thức gồm hai số hạng. Số hạng thứ nhất $\varepsilon/m(s)$ là phần chọn đều, cộng lại trên mọi hành động bằng $\varepsilon$. Số hạng thứ hai chia phần khai thác $1-\varepsilon$ đều cho các hành động đồng hạng cực đại, cộng lại bằng $1-\varepsilon$. Mỗi xác suất không âm và tổng bằng $1$, nên $\pi_\varepsilon(\cdot\mid s)$ là một phân phối trên $\mathcal A(s)$. Với $\mathcal G_Q(\mathrm D)=\{1\}$ và $\varepsilon=1/4$, công thức cho lại $(1/8,\,7/8)$ của Ví dụ 06.4.

Hai trường hợp riêng:

- Với $\varepsilon=0$, $\pi_0$ chia đều xác suất cho các hành động cực đại; khi mỗi hàng có một cực đại, $\pi_0$ là chính sách tham lam (Định nghĩa 04.12), còn khi có đồng hạng, $\pi_0$ thay quy tắc phá hòa (tie-breaking) của định nghĩa ấy bằng phép chia đều.
- Với $\varepsilon=1$, $\pi_1$ là chính sách đều (uniform policy).

Ví dụ: trong bài thực hành (notebook, phần 5), hàng $Q(s,\cdot)=(1;\,3;\,3;\,0)$ với $\varepsilon=0{,}2$ có $\mathcal G_Q(s)=\{1,2\}$. Mỗi hành động nhận $0{,}2/4=0{,}05$ từ phần chọn đều, hai hành động đồng hạng nhận thêm $0{,}8/2=0{,}4$, nên phân phối là $(0{,}05;\,0{,}45;\,0{,}45;\,0{,}05)$.

Nhầm lẫn thường gặp là coi $\varepsilon$ là xác suất chọn hành động "khác hành động tốt nhất". Với $m(s)$ hành động và một cực đại duy nhất, xác suất ấy là $\varepsilon(m(s)-1)/m(s)$, và khối xác suất trên hành động cực đại là $1-\varepsilon+\varepsilon/m(s)$. Tính chất cần giữ là mỗi hành động có xác suất ít nhất $\varepsilon/m(s)$.

::: definition Định nghĩa 06.4 (Chính sách $\varepsilon$-mềm)
Cho $\varepsilon\in[0,1]$. Một chính sách $\pi$ gọi là $\varepsilon$-mềm ($\varepsilon$-soft) nếu

$$
\pi(a\mid s)\ge\frac{\varepsilon}{m(s)}\qquad\text{với mọi } s\in\mathcal S,\ a\in\mathcal A(s).
$$
:::

Lớp chính sách $\varepsilon$-mềm rộng hơn tập chính sách $\varepsilon$-tham lam. Mọi chính sách $\varepsilon$-tham lam đều $\varepsilon$-mềm, vì số hạng thứ hai của Định nghĩa 06.3 không âm. Chiều ngược lại sai: với hai hành động và $\varepsilon=1/4$, các phân phối $1/4$-tham lam chỉ là $(1/8;\,7/8)$, $(7/8;\,1/8)$ và $(1/2;\,1/2)$, nên chính sách $(0{,}3;\,0{,}7)$ thỏa cận dưới $1/8$ nhưng không là chính sách $1/4$-tham lam theo bảng nào. Còn $(0{,}1;\,0{,}9)$ không $1/4$-mềm, vì $0{,}1<0{,}125$.

Tính chất $\varepsilon$-mềm với $\varepsilon>0$ bảo đảm mỗi hành động có xác suất dương tại một trạng thái đã được ghé. Nó không bảo đảm mọi trạng thái đều được ghé; khả năng đạt tới một trạng thái còn phụ thuộc động lực và trạng thái đầu.

### 1.3 Cải thiện chính sách trong lớp $\varepsilon$-mềm

Định lý cải thiện chính sách (Định lý 04.13) dùng chính sách tham lam theo $q_\pi$, vốn không thăm dò. Thay bước tham lam bằng bước $\varepsilon$-tham lam vẫn không làm giảm giá trị, với điều kiện chính sách hiện tại đã $\varepsilon$-mềm và $q_\pi$ được biết chính xác.

Về mặt ý tưởng, chính sách $\varepsilon$-mềm $\pi$ và chính sách $\varepsilon$-tham lam $\pi'$ có chung phần sàn $\varepsilon/m(s)$ cho mỗi hành động. Chúng chỉ khác nhau ở cách phân bổ phần còn lại $1-\varepsilon$: $\pi'$ dồn phần này vào các hành động có $q_\pi$ lớn nhất, còn $\pi$ rải nó theo một trọng số nào đó. Trung bình có trọng số không vượt giá trị lớn nhất, nên một bước theo $\pi'$ không tệ hơn một bước theo $\pi$. Ví dụ sau xét một bài toán chỉ có một bước.

::: example Ví dụ 06.5 (Một trạng thái, ba hành động)
**Dữ kiện.** Một trạng thái không kết thúc $s$ với ba hành động $0,1,2$. Mỗi hành động kết thúc lượt ngay, với phần thưởng tất định lần lượt $3$, $3$, $-1$. Tham số $\varepsilon=0{,}3$; chính sách hiện tại là $\pi(\cdot\mid s)=(0{,}1;\,0{,}1;\,0{,}8)$.

**Giá trị hành động.** Sau mỗi hành động lượt kết thúc, nên $q_\pi(s,\cdot)=(3;\,3;\,-1)$, không phụ thuộc $\pi$.

**Kiểm tra $\varepsilon$-mềm.** Cận dưới là $\varepsilon/m(s)=0{,}3/3=0{,}1$; ba xác suất $0{,}1$, $0{,}1$, $0{,}8$ đều $\ge0{,}1$.

**Giá trị của $\pi$.** $v_\pi(s)=0{,}1\cdot3+0{,}1\cdot3+0{,}8\cdot(-1)=-0{,}2$.

**Chính sách $\varepsilon$-tham lam theo $q_\pi$.** Tập cực đại là $\{0,1\}$; mỗi hành động nhận $0{,}1$ từ phần chọn đều, hai hành động cực đại nhận thêm $0{,}7/2=0{,}35$. Vậy $\pi'(\cdot\mid s)=(0{,}45;\,0{,}45;\,0{,}1)$ và

$$
v_{\pi'}(s)=0{,}45\cdot3+0{,}45\cdot3+0{,}1\cdot(-1)=2{,}6 .
$$

**Phân tách theo phần sàn.** Phần sàn đóng góp như nhau cho hai chính sách: $0{,}1\cdot(3+3-1)=0{,}5$. Phần còn lại của $\pi$ là $(0;\,0;\,0{,}7)$, tức trọng số $(0;\,0;\,1)$ nhân với $0{,}7$, đóng góp $0{,}7\cdot(-1)=-0{,}7$. Phần còn lại của $\pi'$ đóng góp $0{,}7\cdot\max_aq_\pi(s,a)=0{,}7\cdot3=2{,}1$.

**Kiểm tra lại.** $0{,}5-0{,}7=-0{,}2=v_\pi(s)$ và $0{,}5+2{,}1=2{,}6=v_{\pi'}(s)$; $2{,}6\ge-0{,}2$.
:::

Ví dụ 06.5 có một bước nên so sánh một bước cũng là so sánh giá trị. Khi lượt dài hơn, chúng ta cần chuyển bất đẳng thức một bước thành bất đẳng thức giữa hai hàm giá trị. Công cụ cho việc này là toán tử Bellman của một chính sách (Định nghĩa 04.1).

::: remark Nhận xét 06.5 (Nhắc lại: toán tử Bellman của một chính sách)
Cho MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$ và chính sách dừng $\pi$, có thể ngẫu nhiên. Với mỗi bảng $u$ trên $\mathcal S$, mở rộng bằng $u=0$ tại trạng thái kết thúc, toán tử Bellman của $\pi$ cho

$$
(T_\pi u)(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\Big[r(s,a)+\gamma\sum_{s'\in\mathcal S^+}p(s'\mid s,a)\,u(s')\Big],\qquad s\in\mathcal S .
$$

Bổ đề 04.2, Mệnh đề 04.4 và Hệ quả 04.6 cho ba tính chất:

- (a) $T_\pi$ đơn điệu, tức $u\le z$ kéo theo $T_\pi u\le T_\pi z$;
- (b) $T_\pi$ là ánh xạ co hệ số $\gamma$ theo chuẩn $\|u\|_\infty=\max_{s\in\mathcal S}|u(s)|$;
- (c) $v_\pi$ là điểm bất động duy nhất của $T_\pi$, và với mọi $u_0$, dãy $u_{j+1}=T_\pi u_j$ hội tụ tới $v_\pi$.

Tác tử không tính được $T_\pi$ vì không biết $p$ và $r$; toán tử chỉ là công cụ chứng minh.
:::

::: proposition Mệnh đề 06.6 (Cải thiện chính sách $\varepsilon$-tham lam)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$. Cố định $\varepsilon\in[0,1]$. Chính sách dừng $\pi$ là $\varepsilon$-mềm (Định nghĩa 06.4), và $q_\pi$ được biết chính xác. Chính sách $\pi'$ là chính sách $\varepsilon$-tham lam theo $q_\pi$, tức Định nghĩa 06.3 với $Q=q_\pi$ và cùng $\varepsilon$.

**Kết luận.** Với mọi $s\in\mathcal S$,

$$
\begin{aligned}
\sum_{a}\pi'(a\mid s)\,q_\pi(s,a)&\ge v_\pi(s),\\
v_{\pi'}(s)&\ge v_\pi(s).
\end{aligned}
$$

**Điều kiện áp dụng.** Bảng dùng để tạo $\pi'$ phải là $q_\pi$ của chính chính sách $\pi$ hiện tại, không phải một ước lượng từ mẫu; hai chính sách dùng cùng một $\varepsilon$.

**Phạm vi.** Mệnh đề chỉ so sánh $\pi'$ với $\pi$ trong lớp $\varepsilon$-mềm, và bất đẳng thức có thể không chặt; với $\varepsilon=0$, khi mỗi hàng $q_\pi(s,\cdot)$ có cực đại duy nhất, mệnh đề trùng với trường hợp tham lam của Định lý 04.13.
:::

::: proof Chứng minh Mệnh đề 06.6
**Bước 1 (trường hợp $\varepsilon=1$).** Khi $\varepsilon=1$, điều kiện $\varepsilon$-mềm buộc $\pi(a\mid s)\ge1/m(s)$ cho mọi $a$; tổng các xác suất bằng $1$ nên mọi bất đẳng thức là đẳng thức và $\pi$ là chính sách đều. Định nghĩa 06.3 với $\varepsilon=1$ cũng cho chính sách đều. Do đó $\pi'=\pi$ và hai kết luận đúng với dấu bằng. Từ đây giả sử $\varepsilon<1$.

**Bước 2 ($\pi$ là phần sàn cộng một trung bình có trọng số).** Với mỗi $s$, đặt

$$
w(a\mid s)=\frac{\pi(a\mid s)-\varepsilon/m(s)}{1-\varepsilon},\qquad a\in\mathcal A(s).
$$

Vì $\pi$ là $\varepsilon$-mềm, tử số không âm, nên $w(a\mid s)\ge0$. Tổng theo $a$ của tử số là $1-\varepsilon$, nên $\sum_aw(a\mid s)=1$. Căn cứ là Định nghĩa 06.4 và việc $\pi(\cdot\mid s)$ là phân phối.

**Bước 3 (kết luận thứ nhất).** Với mọi $s$,

$$
\begin{aligned}
\sum_a\pi'(a\mid s)q_\pi(s,a)
&=\frac{\varepsilon}{m(s)}\sum_aq_\pi(s,a)+(1-\varepsilon)\max_aq_\pi(s,a) &&\text{(1)}\\
&\ge\frac{\varepsilon}{m(s)}\sum_aq_\pi(s,a)+(1-\varepsilon)\sum_aw(a\mid s)q_\pi(s,a) &&\text{(2)}\\
&=\sum_a\Big[\frac{\varepsilon}{m(s)}+(1-\varepsilon)w(a\mid s)\Big]q_\pi(s,a) &&\text{(3)}\\
&=\sum_a\pi(a\mid s)q_\pi(s,a) &&\text{(4)}\\
&=v_\pi(s) &&\text{(5)}.
\end{aligned}
$$

Căn cứ của từng dòng: (1) Định nghĩa 06.3, các hành động trong tập cực đại của $q_\pi(s,\cdot)$ có cùng giá trị cực đại và chia nhau phần $1-\varepsilon$; (2) trung bình có trọng số $w$ của Bước 2 không vượt giá trị cực đại; (3) gộp hai tổng; (4) định nghĩa của $w$; (5) quan hệ $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$ (Mệnh đề 03.23).

**Bước 4 (kết luận thứ hai).** Theo quan hệ $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$ (Mệnh đề 03.22), vế trái của Bước 3 là $(T_{\pi'}v_\pi)(s)$, nên $T_{\pi'}v_\pi\ge v_\pi$. Đặt $u_0=v_\pi$ và $u_{j+1}=T_{\pi'}u_j$. Khi đó

$$
\begin{aligned}
u_1&=T_{\pi'}u_0\ge u_0 &&\text{(1)}\\
u_{j+1}&=T_{\pi'}u_j\ge T_{\pi'}u_{j-1}=u_j &&\text{(2)}\\
u_j&\ge u_0=v_\pi\quad\text{với mọi } j &&\text{(3)}\\
v_{\pi'}&=\lim_{j\to\infty}u_j\ge v_\pi &&\text{(4)}.
\end{aligned}
$$

Căn cứ của từng dòng: (1) $T_{\pi'}v_\pi\ge v_\pi$ vừa chứng minh; (2) Nhận xét 06.5(a) áp dụng cho $\pi'$, với giả thiết quy nạp $u_j\ge u_{j-1}$; (3) quy nạp theo $j$; (4) Nhận xét 06.5(c) và bất đẳng thức được giữ qua giới hạn. Đây là lập luận chứng minh Định lý 04.13, áp dụng cho $\pi'$ ngẫu nhiên. $\square$
:::

Mệnh đề nói rằng nếu chính sách hiện tại đã giữ cho mỗi hành động xác suất ít nhất $\varepsilon/m(s)$, thì chuyển sang chính sách $\varepsilon$-tham lam theo đúng giá trị hành động của nó không làm giảm giá trị tại trạng thái nào. Với Ví dụ 06.5, kết luận thứ nhất là $2{,}6\ge-0{,}2$.

Ba giả thiết của mệnh đề có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ hoặc trường hợp giới hạn.

- Bỏ "$q_\pi$ được biết chính xác": trong Ví dụ 06.5, xét $\pi=(0{,}45;\,0{,}45;\,0{,}1)$ có $v_\pi(s)=2{,}6$ và một bảng ước lượng sai $Q(s,\cdot)=(-1;\,-1;\,3)$. Chính sách $0{,}3$-tham lam theo bảng này là $(0{,}1;\,0{,}1;\,0{,}8)$, có giá trị $-0{,}2<2{,}6$. Giả thiết này được dùng ở dòng (5) của Bước 3 và ở Bước 4, nơi vế trái của Bước 3 phải bằng $(T_{\pi'}v_\pi)(s)$.
- Bỏ "$\pi$ là $\varepsilon$-mềm": cũng trong Ví dụ 06.5, chính sách tất định chọn hành động $0$ có giá trị $3$, còn chính sách $0{,}3$-tham lam theo $q_\pi$ có giá trị $2{,}6<3$. Ở Bước 2, trọng số $w(1\mid s)=(0-0{,}1)/0{,}7$ âm, nên lập luận "trung bình không vượt cực đại" không còn dùng được.
- Bỏ "$\gamma<1$": Bước 4 dùng tính co để đồng nhất giới hạn của $u_j$ với $v_{\pi'}$. Trên dãy năm ô với $\gamma=1$, một chính sách tất định có thể đi vòng mãi giữa B và C và có lợi tức không hữu hạn (Nhận xét 06.2), nên $v_{\pi'}$ có thể không xác định. Kết quả khi $\gamma=1$ cần thêm giả thiết mọi chính sách được xét kết thúc hầu chắc chắn.

Mệnh đề 06.6 mở rộng trường hợp tham lam của Định lý 04.13 sang chính sách $\varepsilon$-tham lam với $\varepsilon>0$ và sang trường hợp $\varepsilon=0$ có đồng hạng, khi $\pi_0$ chia đều xác suất nên là chính sách ngẫu nhiên, ngoài phạm vi Định lý 04.13. Cái giá của việc giữ $\varepsilon>0$ là kết luận chỉ so sánh trong lớp $\varepsilon$-mềm; lặp lại bước này dẫn tới chính sách tốt nhất trong lớp đó, có thể kém hơn chính sách tối ưu (Sutton và Barto, 2018, §5.4). Trong Ví dụ 06.5, chính sách tốt nhất trong lớp $0{,}3$-mềm có giá trị $2{,}6$, còn chính sách tất định chọn hành động $0$ đạt $3$.

::: remark Nhận xét 06.7 (Giới hạn của Mệnh đề 06.6 khi học từ mẫu)
Trong ba thuật toán của chương, tác tử không có $q_\pi$ mà chỉ có bảng $Q$ cập nhật từ một số hữu hạn mẫu, nên giả thiết "$q_\pi$ được biết chính xác" không thỏa, và bước $\varepsilon$-tham lam có thể làm giá trị giảm, như phản ví dụ $2{,}6\to-0{,}2$ sau Mệnh đề 06.6.

Khi $\varepsilon_k$ giảm dần giữa các lượt, như trong Thuật toán 06.9, chính sách $\varepsilon_k$-tham lam cũng là $\varepsilon_{k+1}$-mềm vì $\varepsilon_k/m(s)\ge\varepsilon_{k+1}/m(s)$, nên giả thiết mềm vẫn thỏa với $\varepsilon=\varepsilon_{k+1}$. Giả thiết duy nhất bị vi phạm là "$q_\pi$ được biết chính xác". Khi $\varepsilon$ tăng giữa hai lượt, giả thiết mềm có thể không thỏa.
:::

**Trong thực hành.** Trong bài thực hành LunarLander của chương, bảng $Q$ có $2187\times4$ ô, khởi tạo bằng $0$, và chính sách hành vi là chính sách $\varepsilon_k$-tham lam theo bảng hiện tại, với $\varepsilon_k$ giảm tuyến tính từ $1$ về $\varepsilon_{\min}=0{,}05$ trong $1500$ lượt đầu rồi giữ nguyên (notebook, phần 5). Phần sàn $\varepsilon/m(s)$ giữ cho mỗi hành động tại một ô đã ghé còn được thử: với $\varepsilon_{\min}=0{,}05$ và bốn hành động, mỗi hành động không cực đại có xác suất $0{,}0125$ ở mỗi lần ghé. Trong notebook, bảng là ước lượng từ mẫu và được cập nhật sau mỗi bước, nên giả thiết "$q_\pi$ được biết chính xác" của Mệnh đề 06.6 không thỏa và chính sách hành vi đổi ngay trong lượt. Do đó mệnh đề không bảo đảm giá trị của chính sách hành vi tăng dần theo lượt (Nhận xét 06.7).

::: exercise Bài tập 06.2 (Chính sách $\varepsilon$-tham lam và điều kiện của Mệnh đề 06.6)
Các câu 1, 3, 4 xét dãy năm ô của Ví dụ 06.1 ($\gamma=1$, hai hành động $0$ trái và $1$ phải tại mỗi ô không kết thúc); câu 2 xét một trạng thái ngoài dãy năm ô.

1. Cho hàng D của bảng là $Q(\mathrm D,0)=0$, $Q(\mathrm D,1)=1$ và $\varepsilon=0{,}2$. Tính xác suất của mỗi hành động tại D theo Định nghĩa 06.3.
2. Tại một trạng thái có ba hành động với hàng $Q(s,\cdot)=(4;\,1;\,1)$ và $\varepsilon=0{,}6$, tính phân phối $\varepsilon$-tham lam.
3. Trong $q_\pi(\mathrm D,0)$, nêu hành động nào được cố định và hành động nào lấy theo $\pi$.
4. Bảng khởi tạo nghiêng phải là B $(0,1)$, C $(1,0)$, D $(0,1)$ theo thứ tự hành động $(0,1)$ (Ví dụ 06.2). Xác định bảng này đã đủ căn cứ để áp dụng Mệnh đề 06.6 cho dãy năm ô hay chưa.
:::

::: hint
Tách nhánh thăm dò và nhánh khai thác; ở câu 2, phần khai thác chia đều cho các hành động đồng hạng. Với câu 4, đối chiếu từng giả thiết của Mệnh đề 06.6: bảng dùng để tạo $\pi'$ là gì, và hệ số chiết khấu của dãy năm ô là bao nhiêu.
:::

::: solution
**Câu 1.** Hành động $1$ là cực đại duy nhất. Hành động $0$ có xác suất $0{,}2/2=0{,}1$; hành động $1$ có $0{,}8+0{,}1=0{,}9$.

**Câu 2.** $\mathcal G_Q(s)=\{0\}$. Mỗi hành động nhận $0{,}6/3=0{,}2$ từ phần chọn đều; hành động cực đại nhận thêm $0{,}4$. Phân phối là $(0{,}6;\,0{,}2;\,0{,}2)$.

**Câu 3.** $q_\pi(\mathrm D,0)$ cố định hành động đầu $A_t=0$; mọi hành động từ bước $t+1$ trở đi lấy theo $\pi$.

**Câu 4.** Chưa đủ, vì hai lý do. Thứ nhất, Mệnh đề 06.6 đòi hỏi $\pi'$ được tạo từ $q_\pi$ chính xác, còn bảng khởi tạo chưa là giá trị hành động của chính sách nào; Ví dụ 06.2 cho thấy $Q_0(\mathrm D,1)=1$ trong khi $q_\pi(\mathrm D,1)=10$ với mọi $\pi$. Thứ hai, mệnh đề dùng $\gamma<1$, còn dãy năm ô dùng $\gamma=1$.

**Kiểm tra lại.** Ở câu 1 và câu 2, tổng xác suất đều bằng $1$: $0{,}1+0{,}9=1$ và $0{,}6+0{,}2+0{,}2=1$. Hai lỗi thường gặp: gán xác suất $\varepsilon=0{,}2$ cho hành động không cực đại, quên rằng nhánh thăm dò chọn đều trong cả hai hành động, kể cả hành động cực đại; và coi bảng khởi tạo như $q_\pi$ rồi áp dụng mệnh đề cải thiện.
:::

Như vậy, bảng $Q$ (Định nghĩa 06.1) cho phép so các hành động trong một hàng mà không cần mô hình; chính sách $\varepsilon$-tham lam (Định nghĩa 06.3) giữ mọi hành động trong lớp $\varepsilon$-mềm (Định nghĩa 06.4); và trong lớp này, bước cải thiện $\varepsilon$-tham lam theo $q_\pi$ chính xác không làm giảm giá trị (Mệnh đề 06.6). Tuy nhiên, trong bài toán phi mô hình, $q_\pi$ chưa biết và chúng ta chỉ có các lượt tương tác.

<!-- note-topic-id: lec-06-topic-03 -->
## 2. Điều khiển Monte Carlo

Trên dãy năm ô, với lượt D→E, tác tử quan sát được lợi tức $10$ sau cặp $(\mathrm D,1)$; với lượt D→C→B→A, nó quan sát được lợi tức $998$ sau cặp $(\mathrm D,0)$. Để đưa các con số này vào bảng, chúng ta cần:

- quy tắc gắn mỗi lợi tức với đúng một cặp;
- bộ đếm số lợi tức đã dùng;
- thời điểm đổi chính sách.

### 2.1 Lợi tức của cặp trạng thái–hành động

Monte Carlo dự đoán (Thuật toán 05.13) ước lượng $v_\pi(s)$ bằng trung bình các lợi tức sau các lần ghé $s$. Để ước lượng $q_\pi(s,a)$, chúng ta làm tương tự với cặp: chỉ những lợi tức đứng sau một lần thực hiện $a$ tại $s$ mới được tính cho ô $(s,a)$.

Một cách trực quan, điều khiển Monte Carlo lặp lại ba việc:

- sinh một lượt hoàn chỉnh theo chính sách hiện tại;
- gán lợi tức của mỗi thời điểm cho cặp đã xảy ra ở thời điểm đó rồi cập nhật trung bình của cặp;
- lập chính sách mới cho lượt sau.

Chính sách không đổi trong lượt, nên các lợi tức của lượt đánh giá đúng chính sách đã sinh ra nó. Phương pháp có chính sách được đánh giá trùng với chính sách sinh dữ liệu gọi là phương pháp theo chính sách (on-policy).

::: example Ví dụ 06.6 (Một lượt tham lam D→E)
**Dữ kiện.** Dãy năm ô, $\gamma=1$. Bảng khởi tạo nghiêng phải: B $(0,1)$, C $(1,0)$, D $(0,1)$, mỗi cặp ghi theo thứ tự hành động $(0,1)$. Mọi bộ đếm $N(s,a)$, số lợi tức đã dùng cho cặp $(s,a)$, bằng $0$. Chính sách của lượt là chính sách tham lam theo bảng ($\varepsilon=0$).

**Sinh lượt.** Tại D, hành động cực đại là $1$, nên lượt là D→E với $R_1=10$; lượt kết thúc ở $T=1$.

**Lợi tức.** $G_0=10$, gắn với cặp $(S_0,A_0)=(\mathrm D,1)$.

**Cập nhật trung bình.** Tăng bộ đếm trước: $N(\mathrm D,1)=1$. Rồi

$$
\begin{aligned}
Q(\mathrm D,1)&\leftarrow Q(\mathrm D,1)+\frac{G_0-Q(\mathrm D,1)}{N(\mathrm D,1)}\\
&=1+\frac{10-1}{1}=10 .
\end{aligned}
$$

Năm ô còn lại giữ nguyên.

**Kiểm tra lại.** Sau một lợi tức, trung bình của các lợi tức đã dùng cho $(\mathrm D,1)$ là $10$, trùng giá trị mới. Giá trị khởi tạo $1$ không phải một quan sát; nếu lấy $(1+10)/2=5{,}5$ là đã thêm một quan sát không có trong dữ liệu.
:::

Ví dụ 06.6 dùng hai quy ước: lợi tức gắn với cặp xảy ra ở thời điểm đó, và bộ đếm không tính giá trị khởi tạo. Nhắc lại từ Định nghĩa 05.6: lần ghé đầu tiên của trạng thái $s$ trong một lượt là thời điểm nhỏ nhất $t$ có $S_t=s$.

::: definition Định nghĩa 06.8 (Lần ghé đầu tiên của cặp và bộ đếm Monte Carlo)
Cho một lượt $S_0,A_0,R_1,S_1,A_1,\dots,R_T,S_T$ với $S_T$ là trạng thái kết thúc. Một lần ghé cặp $(s,a)$ là một thời điểm $t<T$ có $(S_t,A_t)=(s,a)$. Lần ghé đầu tiên của cặp $(s,a)$ trong lượt là

$$
f(s,a)=\min\{t<T:\ (S_t,A_t)=(s,a)\},
$$

xác định khi cặp xuất hiện trong lượt. Monte Carlo lần ghé đầu tiên theo cặp chỉ gắn lợi tức $G_{f(s,a)}$ với $(s,a)$. Bộ đếm $N(s,a)$ là số lợi tức đã được gắn với $(s,a)$ qua mọi lượt; nó bắt đầu từ $N(s,a)=0$ và không tính giá trị khởi tạo.
:::

Định nghĩa 06.8 khác Định nghĩa 05.6 ở một điểm: hai lần ghé cùng trạng thái nhưng với hai hành động khác nhau thuộc về hai cặp khác nhau. Nếu một lượt đi D (trái), C (phải), D (trái), C (trái), thì $(\mathrm C,1)$ có lần ghé đầu tiên tại $t=1$ và $(\mathrm C,0)$ có lần ghé đầu tiên tại $t=3$, dù cả hai lần đều ở ô C.

Việc cập nhật dùng lại trung bình gia tăng (Mệnh đề 05.9): nếu bộ đếm bắt đầu từ $0$ và được tăng trước khi chia, quy tắc $Q\leftarrow Q+(G-Q)/N$ cho đúng trung bình số học của các lợi tức đã gắn với ô, và giá trị khởi tạo bị thay hẳn ở lợi tức thứ nhất. Chỉ số của bộ đếm là số lợi tức của cặp đang xét, không phải số lượt toàn cục.

### 2.2 Một lượt có thăm dò

Ví dụ 06.6 dùng chính sách tham lam, nên chỉ cập nhật được $(\mathrm D,1)$. Với $\varepsilon=1/4$, bảng nghiêng phải cho $(\mathrm D,0)$ xác suất $1/8$ ở đầu mỗi lượt (Ví dụ 06.4). Ví dụ sau dùng bảng khởi tạo nghiêng trái, chỉ khác bảng nghiêng phải ở hàng D; dưới bảng này $(\mathrm D,0)$ là hành động tham lam, nên bước thăm dò của lượt xảy ra tại B. Để mọi người học tái tạo được cùng một lượt, ta thay nguồn ngẫu nhiên bằng một dãy số tất định.

::: example Ví dụ 06.7 (Lượt thăm dò sinh bằng dãy số cho trước)
**Dữ kiện.** Dãy năm ô, $\varepsilon=1/4$. Bảng khởi tạo nghiêng trái giữ hàng B, C của bảng nghiêng phải và đổi hàng D:

| Trạng thái | $Q_0(s,0)$ | $Q_0(s,1)$ |
|---|---:|---:|
| B | $0$ | $1$ |
| C | $1$ | $0$ |
| D | $1$ | $0$ |

Dãy số: $x_0=1$, $x_j=(2x_{j-1}+1)\bmod 5$ và $u_j=(x_j+1)/5$ với $j=1,2,\dots$; chỉ số $j$ đếm số đã dùng, khác thời điểm $t$ của lượt. Quy tắc dùng số: mỗi lần chọn hành động đọc một số $u$; nếu $u>1/4$ thì chọn hành động cực đại; nếu $u\le1/4$ thì đọc thêm một số, chọn trái khi số này $\le1/2$, chọn phải khi số này $>1/2$. Mọi hàng dùng ở đây có cực đại duy nhất.

**Dãy số.** $x_1=(2\cdot1+1)\bmod5=3$, $x_2=(2\cdot3+1)\bmod5=2$, $x_3=(2\cdot2+1)\bmod5=0$, $x_4=(2\cdot0+1)\bmod5=1$; do đó $u_1=4/5$, $u_2=3/5$, $u_3=1/5$, $u_4=2/5$.

**Sinh lượt.**

| Trạng thái | Số quyết định nhánh | Số bổ sung | Hành động |
|---|---:|---:|---|
| D | $u_1=4/5>1/4$ | không dùng | $0$, cực đại của hàng D |
| C | $u_2=3/5>1/4$ | không dùng | $0$, cực đại của hàng C |
| B | $u_3=1/5\le1/4$ | $u_4=2/5\le1/2$ | $0$, thăm dò (cực đại của hàng B là $1$) |

Lượt thu được là D→C→B→A với ba hành động trái và các phần thưởng $-1,-1,1000$.

**Kiểm tra lại.** Theo quy tắc, xác suất chọn hành động không cực đại là $\tfrac14\cdot\tfrac12=\tfrac18=\varepsilon/m$, khớp Định nghĩa 06.3 khi các số là đều trên $[0,1]$.
:::

::: example Ví dụ 06.8 (Cập nhật Monte Carlo từ lượt D–C–B–A)
**Dữ kiện.** Lượt D→C→B→A của Ví dụ 06.7: $(S_0,A_0,R_1)=(\mathrm D,0,-1)$, $(S_1,A_1,R_2)=(\mathrm C,0,-1)$, $(S_2,A_2,R_3)=(\mathrm B,0,1000)$, $S_3=\mathrm A$ kết thúc, $T=3$, $\gamma=1$. Bảng khởi tạo nghiêng trái: B $(0,1)$, C $(1,0)$, D $(1,0)$; mọi $N(s,a)=0$.

**Lợi tức, tính lùi.** $G_3=0$, $G_2=1000+G_3=1000$, $G_1=-1+G_2=999$, $G_0=-1+G_1=998$.

**Lần ghé đầu tiên.** Ba cặp $(\mathrm D,0)$, $(\mathrm C,0)$, $(\mathrm B,0)$ mỗi cặp xuất hiện một lần, tại $t=0,1,2$.

**Cập nhật.** Mỗi cặp có $N=1$ sau khi tăng, nên giá trị mới bằng lợi tức:

| Trạng thái | $Q(s,0)$ | $Q(s,1)$ | $N(s,0)$ | $N(s,1)$ |
|---|---:|---:|---:|---:|
| B | $1000$ | $1$ | $1$ | $0$ |
| C | $999$ | $0$ | $1$ | $0$ |
| D | $998$ | $0$ | $1$ | $0$ |

**Diễn giải.** Hàng D giờ xếp trái ($998$) trên phải ($0$), nên chính sách cho lượt sau ưu tiên trái tại D.

**Kiểm tra lại.** $Q(\mathrm D,0)=998$ trùng lợi tức "đi trái ba lần" của Ví dụ 06.1.
:::

![Lượt bốn thời điểm: D ở thời điểm 0, C ở thời điểm 1, B ở thời điểm 2, A ở thời điểm 3; ba cạnh ghi "0 · −1", "0 · −1", "0 · 1000"; dưới các ô D, C, B ghi lợi tức 998, 999 và 1000.](img/lec-06/episode-return.svg)

Hình trên đặt lợi tức dưới ô xuất phát của mỗi thời điểm: $G_t$ là tổng các phần thưởng trên các cạnh nằm bên phải thời điểm $t$. Ba lợi tức $998$, $999$, $1000$ trên hình là ba giá trị mới của Ví dụ 06.8.

Thuật toán sau ghép các thao tác của Ví dụ 06.6 và 06.8 thành một quy trình có ngân sách.

### 2.3 Thuật toán điều khiển Monte Carlo

::: algorithm Thuật toán 06.9 (Điều khiển Monte Carlo theo chính sách, lần ghé đầu tiên)
**Đầu vào.** Môi trường lấy mẫu được với phân phối trạng thái đầu $d_0$ trên $\mathcal S$; các tập $\mathcal A(s)$; hệ số $\gamma$; bảng hữu hạn $Q_0$; lịch thăm dò $0<\varepsilon_k\le1$, $k=1,2,\dots$; ngân sách $K$ lượt (số nguyên dương).

**Đầu ra.** Bảng $Q$ và chính sách $\varepsilon_K$-tham lam theo bảng cuối.

**Giả thiết.** Mọi chính sách được dùng sinh lượt kết thúc hầu chắc chắn, và lợi tức khả tích.

**Khởi tạo.** $Q\leftarrow Q_0$; $N(s,a)\leftarrow0$ với mọi cặp hợp lệ.

**Tham số.** $\varepsilon_k$ (chẳng hạn $\varepsilon_k=1/k$) và $K$.

1. Với mỗi lượt $k=1,\dots,K$: ghi $Q^{[k]}$ là bảng hiện tại; cố định $\pi_k$ là chính sách $\varepsilon_k$-tham lam theo $Q^{[k]}$; đặt lại quỹ đạo và ánh xạ lần ghé đầu tiên $f$ về rỗng; lấy $S_0\sim d_0$.
2. Tại mỗi thời điểm $t$ của lượt: lấy $A_t\sim\pi_k(\cdot\mid S_t)$; nếu cặp $(S_t,A_t)$ chưa có trong $f$, đặt $f(S_t,A_t)=t$; thực hiện $A_t$, nhận $R_{t+1}$ và $S_{t+1}$; lưu chuyển vào quỹ đạo. Lặp tới khi $S_{t+1}$ là trạng thái kết thúc; gọi thời điểm ấy là $T$. Trong lúc thu thập, $Q$ và $\pi_k$ không đổi.
3. Đặt $G_T=0$ và với $t=T-1,\dots,0$ tính $G_t=R_{t+1}+\gamma G_{t+1}$.
4. Với mỗi cặp $(s,a)$ có trong $f$: $N(s,a)\leftarrow N(s,a)+1$, rồi $Q(s,a)\leftarrow Q(s,a)+\big[G_{f(s,a)}-Q(s,a)\big]/N(s,a)$.
5. Nếu $k<K$, sang lượt $k+1$ với bảng và bộ đếm giữ nguyên; nếu $k=K$, trả $Q$ và chính sách $\varepsilon_K$-tham lam theo $Q$.

**Điều kiện dừng.** Sau đúng $K$ lượt hoàn chỉnh.

**Chi phí mỗi bước.** Bộ nhớ $O(M+T)$ cho $Q$, $N$, quỹ đạo và $f$ của lượt hiện tại. Với tra cứu $f$ trong thời gian hằng, bước 3–4 tốn $O(T)$ mỗi lượt; chọn hành động ở bước 2 tốn thêm $O(m(S_t))$ mỗi thời điểm để tìm cực đại của hàng.
:::

Thuật toán 06.9 có thể lần theo đúng Ví dụ 06.8: với $k=1$ và lịch có $\varepsilon_1=1/4$, $Q^{[1]}$ là bảng nghiêng trái, $\pi_1$ là chính sách $1/4$-tham lam, bước 2 sinh lượt D→C→B→A bằng dãy số của Ví dụ 06.7, bước 3 cho $(998,999,1000)$, bước 4 cho bảng của Ví dụ 06.8. Bước 4 là đánh giá bằng mẫu, bước 1 của lượt sau là bước cải thiện $\varepsilon$-tham lam có dạng của Mệnh đề 06.6, áp dụng cho bảng ước lượng (Nhận xét 06.7).

So với Monte Carlo dự đoán (Thuật toán 05.13), mục tiêu vẫn là lợi tức hoàn chỉnh $G_t$, nhưng thuật toán:

- gắn lợi tức với cặp thay cho trạng thái;
- lập lại chính sách sau mỗi lượt;
- cần hành vi mềm để mọi cặp có cơ hội được thăm.

::: remark Nhận xét 06.10 (Lượt, ngân sách và tiền tố bị cắt)
Lượt kết thúc là sự kiện của môi trường; chỉ khi đó lợi tức $G_t$ mới tính được. Hết ngân sách $K$ là điểm dừng của thuật toán, xảy ra giữa hai lượt, và không nói gì về độ chính xác của bảng. Một tiền tố bị cắt tại trạng thái chưa kết thúc, chẳng hạn chỉ có D→C, không cho lợi tức hoàn chỉnh nên không dùng được cho thuật toán này.

Các lợi tức của những lượt khác nhau được sinh bởi những chính sách khác nhau, nên trung bình trong mỗi ô trộn đánh giá của nhiều chính sách.
:::

**Trong thực hành.** Bài thực hành LunarLander nêu Thuật toán 06.9 như một nhiệm vụ mở (phần 13, nhiệm vụ 9). Trong một lần chạy đã nhúng trong notebook, $500$ lượt huấn luyện cuối của Sarsa (Thuật toán 06.12), sinh bởi chính sách hành vi $\varepsilon_k$-tham lam, dài trung bình $655$ bước và $7\%$ số lượt bị cắt ngắn ở bước $1000$ (phần 8.1). Nếu Thuật toán 06.9 học trên dữ liệu như vậy, các lượt bị cắt ngắn không dùng được (Nhận xét 06.10) và mỗi cập nhật phải chờ hàng trăm bước.

::: exercise Bài tập 06.3 (Lần ghé đầu tiên trên lượt có cặp lặp)
Trên dãy năm ô ($\gamma=1$), cho lượt D→C→D→C→B→A với dãy hành động $0,1,0,0,0$ và dãy phần thưởng $-1,-1,-1,-1,1000$. Bộ đếm ban đầu $N(\mathrm D,0)=0$.

1. Tính các lợi tức $G_0,\dots,G_4$.
2. Tính $Q(\mathrm D,0)$ và $N(\mathrm D,0)$ sau Monte Carlo lần ghé đầu tiên theo cặp (Định nghĩa 06.8).
3. Tính lại nếu dùng mọi lần ghé: nhắc lại rằng Monte Carlo mọi lần ghé (Định nghĩa 05.6) gắn với cặp lợi tức sau mỗi lần ghé, không chỉ lần đầu.
4. Xác định các cặp tại ô C và số lợi tức mỗi cặp nhận.
:::

::: hint
Đánh số thời điểm từ $0$ và tính lợi tức lùi. Lần ghé đầu tiên xác định theo chiều thời gian, dù lợi tức được tính theo chiều ngược.
:::

::: solution
**Câu 1.** Tính lùi: $G_4=1000$, $G_3=-1+1000=999$, $G_2=998$, $G_1=997$, $G_0=996$.

**Câu 2.** Cặp $(\mathrm D,0)$ xuất hiện tại $t=0$ và $t=2$. Lần ghé đầu tiên là $t=0$, nên chỉ lợi tức $G_0=996$ được dùng: $N(\mathrm D,0)=1$ và $Q(\mathrm D,0)=996$.

**Câu 3.** Mọi lần ghé dùng cả $G_0=996$ và $G_2=998$: $N(\mathrm D,0)=2$ và $Q(\mathrm D,0)=(996+998)/2=997$.

**Câu 4.** Tại C có hai lần ghé với hai hành động khác nhau: $(\mathrm C,1)$ tại $t=1$ với lợi tức $997$, và $(\mathrm C,0)$ tại $t=3$ với lợi tức $999$. Đây là hai cặp riêng, mỗi cặp nhận một lợi tức.

**Kiểm tra lại.** Giá trị khởi tạo không được tính thành mẫu ở cả hai cách, vì bộ đếm bắt đầu từ $0$. Hai cách chỉ khác nhau ở cặp lặp $(\mathrm D,0)$. Hai lỗi thường gặp: đếm theo trạng thái thay cho theo cặp, coi hai lần ghé ô C là của cùng một đơn vị; và chia cho $N+1$, như thể giá trị khởi tạo là một quan sát.
:::

Điều khiển Monte Carlo (Thuật toán 06.9) thay $q_\pi$ chính xác bằng trung bình lợi tức theo lần ghé đầu tiên của cặp (Định nghĩa 06.8) và cải thiện $\varepsilon$-tham lam sau mỗi lượt. Mục tiêu của nó là lợi tức hoàn chỉnh $G_t$, nên không ô nào được cập nhật trước khi lượt kết thúc.

<!-- note-topic-id: lec-06-topic-04 -->
## 3. Sarsa và mục tiêu một bước

Sau chuyển D→C của một lượt mới, tác tử đã nhận phần thưởng $-1$ và đang đứng ở C, một trạng thái chưa kết thúc, nên chưa có $G_0$ để cập nhật ô $(\mathrm D,0)$. Trong Bài 05, TD(0) đã giải quyết khó khăn tương tự bằng cách thay phần lợi tức chưa quan sát bằng $\gamma V(S_{t+1})$ (Định nghĩa 05.20). Với bảng $Q$, chúng ta cần xác định ô nào đóng vai $V(S_{t+1})$.

### 3.1 Mục tiêu một bước cho giá trị hành động

Về mặt ý tưởng, phần lợi tức sau C là lợi tức khi tác tử tiếp tục từ C theo chính sách đang dùng, bắt đầu bằng một hành động $A'$ tại C. Nếu tác tử chọn luôn $A'$ và cam kết thực hiện nó, thì ô $Q(\mathrm C,A')$ là ước lượng hiện có của đúng phần tiếp nối đó, và mục tiêu cho $(\mathrm D,0)$ là $-1+\gamma Q(\mathrm C,A')$. Để làm rõ bảng nào được đọc, $A'$ được chọn lúc nào và trạng thái kết thúc được xử lý ra sao, xem ví dụ sau.

::: example Ví dụ 06.9 (Năm mẫu chuyển, hai cập nhật Sarsa đầu)
**Dữ kiện.** Dãy năm ô, $\gamma=1$, bước học hằng $\alpha=0{,}8$. Bảng khởi tạo nghiêng phải, ghi theo thứ tự hành động $(0,1)$: B $(0,1)$, C $(1,0)$, D $(0,1)$. Năm mẫu, với $S,A,R,S',A'$ là trạng thái, hành động, phần thưởng, trạng thái kế tiếp và hành động kế tiếp đã chọn:

| Mẫu | $S$ | $A$ | $R$ | $S'$ | $A'$ |
|---:|---|---:|---:|---|---|
| 1 | D | 0 | $-1$ | C | 0 |
| 2 | C | 0 | $-1$ | B | 0 |
| 3 | B | 0 | $1000$ | A | không có |
| 4 | D | 1 | $10$ | E | không có |
| 5 | D | 0 | $-1$ | C | 0 |

Ba mẫu đầu thuộc lượt D→C→B→A; mẫu 4 thuộc lượt D→E; mẫu 5 thuộc lượt thứ ba, có dữ liệu dừng ở C, một trạng thái chưa kết thúc. Các hành động $A$ và $A'$ trong bảng là dữ kiện cho trước; mỗi hành động đều có xác suất dương dưới chính sách $\varepsilon$-tham lam với $\varepsilon>0$. Năm mẫu này dùng chung cho Sarsa và Q-learning.

**Mẫu 1.** Hành động kế tiếp tại C là $0$, có $Q(\mathrm C,0)=1$.

$$
\begin{aligned}
Y&=-1+1\cdot Q(\mathrm C,0)=-1+1=0,\\
\delta&=Y-Q(\mathrm D,0)=0-0=0,\\
Q(\mathrm D,0)&\leftarrow0+0{,}8\cdot0=0 .
\end{aligned}
$$

**Mẫu 2.** Hành động kế tiếp tại B là $0$, có $Q(\mathrm B,0)=0$.

$$
\begin{aligned}
Y&=-1+1\cdot Q(\mathrm B,0)=-1+0=-1,\\
\delta&=Y-Q(\mathrm C,0)=-1-1=-2,\\
Q(\mathrm C,0)&\leftarrow1+0{,}8\cdot(-2)=-0{,}6 .
\end{aligned}
$$

**Diễn giải.** Ô $Q(\mathrm B,1)=1$ là ô lớn nhất của hàng B nhưng không tham gia mục tiêu của mẫu 2, vì hành động được chọn để tiếp tục tại B là $0$.

**Kiểm tra lại.** $-0{,}6=-3/5$; với $\alpha=4/5$, $1+\tfrac45(-2)=1-\tfrac85=-\tfrac35$.
:::

![Hai ô C và B nối bởi cạnh "0; thưởng −1". Tại B vẽ hai nhánh hành động: hành động 0 có giá trị 0, ghi "đã lấy mẫu", vẽ nét liền đậm; hành động 1 có giá trị 1, ghi "cực đại", vẽ nét đứt. Chú thích: nét liền đậm là giá trị dùng trong mục tiêu, nên mục tiêu Sarsa dùng giá trị 0 của hành động đã lấy mẫu.](img/lec-06/sarsa-target.svg)

Hình trên vẽ mẫu 2 của Ví dụ 06.9; nhánh nét liền đậm là giá trị đi vào mục tiêu. Định nghĩa sau viết quy tắc của hai mẫu đầu cho mọi bước.

::: definition Định nghĩa 06.11 (Mục tiêu và sai lệch Sarsa)
Gọi $Q_t$ là bảng ngay trước cập nhật ở bước $t$. Sau khi thực hiện $A_t$ tại $S_t$ và nhận $R_{t+1}$, $S_{t+1}$: nếu $S_{t+1}\in\mathcal S$, chọn $A_{t+1}$ theo chính sách đang dùng, lập từ $Q_t$. Mục tiêu Sarsa là

$$
Y_t=\begin{cases}
R_{t+1}+\gamma\,Q_t(S_{t+1},A_{t+1}), & S_{t+1}\in\mathcal S,\\
R_{t+1}, & S_{t+1}\ \text{là trạng thái kết thúc}.
\end{cases}
$$

Sai lệch Sarsa (TD error) là $\delta_t=Y_t-Q_t(S_t,A_t)$. Với bước học $\alpha_t\in(0,1]$, cập nhật Sarsa đổi đúng một ô:

$$
\begin{aligned}
Q_{t+1}(S_t,A_t)&=Q_t(S_t,A_t)+\alpha_t\,\delta_t,\\
Q_{t+1}(s,a)&=Q_t(s,a)\ \text{với}\ (s,a)\ne(S_t,A_t).
\end{aligned}
$$
:::

Mục tiêu $Y_t$ gồm phần thưởng vừa quan sát và $\gamma$ nhân ước lượng hiện có của phần tiếp nối bắt đầu bằng hành động $A_{t+1}$ sẽ được thực hiện. Sai lệch $\delta_t$ không phải sai số so với $q_\pi$ hay $q_*$, vì chính $Y_t$ chứa một ước lượng. Nhánh kết thúc dùng quy ước $Q(\text{kết thúc},\cdot)=0$ của Định nghĩa 06.1: phần thưởng khi vào A hoặc E đã nằm trong $R_{t+1}$. Tên Sarsa lấy từ bộ năm $(S_t,A_t,R_{t+1},S_{t+1},A_{t+1})$.

Mục tiêu Sarsa là mục tiêu TD(0) (Định nghĩa 05.20) trên cặp: $V(S_{t+1})$ thành $Q(S_{t+1},A_{t+1})$. Dưới một chính sách cố định, dãy cặp $(S_t,A_t)$ tạo một quá trình phần thưởng Markov (Markov reward process) trên tập cặp, có dạng của Định nghĩa 03.26. Áp dụng Định lý 05.30 cho quá trình này, Sarsa với chính sách cố định hội tụ hầu chắc chắn tới $q_\pi$ khi mọi cặp được cập nhật vô hạn lần và bước học thỏa Robbins–Monro theo cặp (Sutton và Barto, 2018, §6.4).

Hai cách hiểu sai thường gặp liên quan tới $A_{t+1}$. Cách thứ nhất là chọn lại hành động từ bảng mới sau cập nhật; hành động được thực hiện khi đó có thể khác hành động đã dùng trong mục tiêu. Cách thứ hai là thay $Q_t(S_{t+1},A_{t+1})$ bằng ô lớn nhất của hàng $S_{t+1}$, tức mục tiêu Q-learning (Định nghĩa 06.15).

### 3.2 Thuật toán Sarsa

Để thành thuật toán, quy tắc của Ví dụ 06.9 cần thêm ba quy định:

- $A_{t+1}$ dùng trong mục tiêu là hành động thực hiện ở bước sau;
- bước học được chọn theo số lần cập nhật của từng cặp;
- vòng lặp dừng theo ngân sách cập nhật, độc lập với việc lượt kết thúc.

::: algorithm Thuật toán 06.12 (Sarsa dạng bảng)
**Đầu vào.** Môi trường lấy mẫu được với phân phối đầu $d_0$ trên $\mathcal S$; các tập $\mathcal A(s)$; hệ số $\gamma$; bảng hữu hạn $Q_0$; lịch thăm dò $\varepsilon$ (hằng hoặc giảm dần); lịch bước học $\alpha_n(s,a)\in(0,1]$; ngân sách $H$ cập nhật (số nguyên dương).

**Đầu ra.** Bảng $Q$ và chính sách $\varepsilon$-tham lam theo bảng cuối.

**Giả thiết.** Dữ liệu sinh từ chính môi trường cần học; bước học của một cập nhật được chọn trước khi quan sát mẫu dùng cho cập nhật đó.

**Khởi tạo.** $Q\leftarrow Q_0$, $Q(\text{kết thúc},\cdot)=0$; bộ đếm cập nhật của từng cặp $n(s,a)\leftarrow0$; số cập nhật đã làm $h\leftarrow0$. Lấy $S\sim d_0$ và $A$ theo chính sách $\varepsilon$-tham lam từ $Q$.

**Tham số.** $\varepsilon$, $\alpha_n(s,a)$, $H$.

1. Chọn bước học $\alpha\leftarrow\alpha_{n(S,A)+1}(S,A)$. Thực hiện $A$, nhận $R$ và $S'$.
2. Nếu $S'$ chưa kết thúc: lấy một lần $A'$ theo chính sách $\varepsilon$-tham lam từ bảng $Q$ chưa cập nhật, và đặt $Y\leftarrow R+\gamma Q(S',A')$. Nếu $S'$ kết thúc: đặt $Y\leftarrow R$, không chọn $A'$.
3. Đọc giá trị cũ $Q(S,A)$ và cập nhật $Q(S,A)\leftarrow Q(S,A)+\alpha\,[Y-Q(S,A)]$. Tăng $n(S,A)$ và $h$ thêm $1$.
4. Nếu $h=H$: trả $Q$ và chính sách $\varepsilon$-tham lam theo $Q$.
5. Nếu $S'$ chưa kết thúc: đặt $(S,A)\leftarrow(S',A')$ và về bước 1; hành động thực hiện tiếp là đúng $A'$ đã chọn ở bước 2. Nếu $S'$ kết thúc: lấy trạng thái đầu mới $S\sim d_0$ và $A$ theo chính sách từ bảng hiện tại, giữ $Q$, $n$, $h$, rồi về bước 1.

**Điều kiện dừng.** Sau đúng $H$ cập nhật.

**Chi phí mỗi bước.** Bộ nhớ $O(M)$ cho $Q$ và $n$; không cần lưu quỹ đạo. Mỗi bước tốn một lần tra cứu $Q(S',A')$ cho mục tiêu và $O(m(S'))$ để chọn $A'$ theo chính sách $\varepsilon$-tham lam.
:::

Hai bước đầu của thuật toán lần theo đúng Ví dụ 06.9: với mẫu 2, bước 2 chọn $A'=0$ tại B từ bảng chưa cập nhật và cho $Y=-1$, bước 3 cho $Q(\mathrm C,0)=-0{,}6$, bước 5 chuyển sang cặp $(\mathrm B,0)$ để xử lý mẫu 3.

::: example Ví dụ 06.10 (Sarsa trên năm mẫu, gồm hai mẫu vào trạng thái kết thúc)
**Dữ kiện.** Dãy năm ô, $\gamma=1$, $\alpha=0{,}8$. Sau hai mẫu đầu của Ví dụ 06.9, bảng là B $(0,1)$, C $(-0{,}6,0)$, D $(0,1)$. Ba mẫu còn lại (Ví dụ 06.9), theo thứ tự $(S,A,R,S',A')$:

| Mẫu | $S$ | $A$ | $R$ | $S'$ | $A'$ |
|---:|---|---:|---:|---|---|
| 3 | B | 0 | $1000$ | A | không có |
| 4 | D | 1 | $10$ | E | không có |
| 5 | D | 0 | $-1$ | C | 0 |

**Mẫu 3.** $S'=\mathrm A$ kết thúc, nên $Y=1000$; $\delta=1000-Q(\mathrm B,0)=1000$; $Q(\mathrm B,0)\leftarrow0+0{,}8\cdot1000=800$.

**Mẫu 4.** $S'=\mathrm E$ kết thúc, nên $Y=10$; $\delta=10-Q(\mathrm D,1)=10-1=9$; $Q(\mathrm D,1)\leftarrow1+0{,}8\cdot9=8{,}2$.

**Mẫu 5.** $S'=\mathrm C$ chưa kết thúc, $A'=0$, và bảng hiện tại có $Q(\mathrm C,0)=-0{,}6$ từ mẫu 2. Do đó $Y=-1+(-0{,}6)=-1{,}6$; $\delta=-1{,}6-Q(\mathrm D,0)=-1{,}6$; $Q(\mathrm D,0)\leftarrow0+0{,}8\cdot(-1{,}6)=-1{,}28$.

**Bảng sau từng mẫu** (mỗi ô ghi cặp giá trị theo thứ tự hành động $(0,1)$):

| Sau mẫu | Hàng B | Hàng C | Hàng D |
|---:|---|---|---|
| 0 (khởi tạo) | $(0;\,1)$ | $(1;\,0)$ | $(0;\,1)$ |
| 1 | $(0;\,1)$ | $(1;\,0)$ | $(0;\,1)$ |
| 2 | $(0;\,1)$ | $(-0{,}6;\,0)$ | $(0;\,1)$ |
| 3 | $(800;\,1)$ | $(-0{,}6;\,0)$ | $(0;\,1)$ |
| 4 | $(800;\,1)$ | $(-0{,}6;\,0)$ | $(0;\,8{,}2)$ |
| 5 | $(800;\,1)$ | $(-0{,}6;\,0)$ | $(-1{,}28;\,8{,}2)$ |

**Diễn giải.** Sau năm mẫu, hàng D xếp phải ($8{,}2$) trên trái ($-1{,}28$). Giá trị lớn $800$ tại $(\mathrm B,0)$ chưa truyền về D, vì mẫu 2 cập nhật $(\mathrm C,0)$ trước khi $(\mathrm B,0)$ nhận $800$, và mẫu 5 dùng $(\mathrm C,0)$ chứ không dùng $(\mathrm B,0)$.

**Kiểm tra lại.** $8{,}2=41/5$, $-1{,}28=-32/25$, và $\tfrac45\cdot(-\tfrac85)=-\tfrac{32}{25}$.
:::

Ví dụ 06.10 cho thấy hai đặc điểm của mục tiêu một bước. Thông tin về phần thưởng $1000$ chỉ đi lùi một ô mỗi lần cặp đứng trước nó được cập nhật. Ngược lại, mẫu 5 cập nhật được $(\mathrm D,0)$ trước khi lượt thứ ba kết thúc.

::: remark Nhận xét 06.13 (Kết thúc lượt, cắt ngắn và hết ngân sách)
Với mục tiêu Sarsa, ba sự kiện sau có hậu quả khác nhau.

- **Kết thúc lượt.** $S_{t+1}$ là trạng thái kết thúc của môi trường (A hoặc E). Mục tiêu là $Y_t=R_{t+1}$, không chọn $A_{t+1}$.
- **Cắt ngắn (truncation).** Môi trường ngừng lượt sau một số bước cố định trong khi $S_{t+1}$ chưa kết thúc, như giới hạn $1000$ bước của LunarLander. Trạng thái $S_{t+1}$ vẫn có phần tiếp nối, nên mục tiêu vẫn là $R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$; đặt $Y_t=R_{t+1}$ là coi một trạng thái giữa chừng như trạng thái kết thúc có giá trị $0$.
- **Hết ngân sách.** Thuật toán dừng sau $H$ cập nhật. Nếu $S'$ ở cập nhật cuối chưa kết thúc, $A'$ vẫn phải được chọn để tạo mục tiêu, dù nó không bao giờ được thực hiện.
:::

Thuật toán 06.12 và Thuật toán 06.9 khác nhau ở mục tiêu, và khác biệt này có ba hệ quả:

- **Dữ liệu và thời điểm cập nhật.** Monte Carlo dùng lợi tức hoàn chỉnh $G_t$, cần lượt kết thúc và cập nhật sau lượt; Sarsa dùng $R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$, chỉ cần bộ năm và cập nhật sau mỗi chuyển.
- **Sai số do ước lượng.** Mục tiêu Sarsa chứa ước lượng $Q_t$, nên khi $Q_t$ còn sai thì mục tiêu cũng sai theo; ở mẫu 1 của Ví dụ 06.9, mục tiêu $0$ được tính từ giá trị khởi tạo $Q(\mathrm C,0)=1$ chưa từng được quan sát.
- **Bộ nhớ.** Monte Carlo lưu cả quỹ đạo, Sarsa chỉ lưu bảng.

**Trong thực hành.** Bài thực hành cài đặt Thuật toán 06.12 trên LunarLander với ngân sách tính theo $K=3000$ lượt thay cho $H$ cập nhật; tổng số cập nhật $h$ vẫn được đếm (notebook, phần 6 và 8). Bảng có $2187$ ô của một lưới rời rạc hóa (discretization) quan sát liên tục và bốn hành động; bước học theo cặp là $\alpha_n=\max(0{,}05,\ n^{-0{,}6})$. Ở bước cắt ngắn $1000$, mục tiêu vẫn chứa $\gamma Q(S',A')$ đúng như Nhận xét 06.13; khi tàu vào trạng thái kết thúc với phần thưởng $\pm100$, mục tiêu chỉ là phần thưởng đó.

::: exercise Bài tập 06.4 (Cập nhật Sarsa với bước học khác)
Trên dãy năm ô ($\gamma=1$), bảng hiện tại có $Q(\mathrm D,0)=0$ và $Q(\mathrm C,0)=-0{,}6$. Tác tử quan sát chuyển $(\mathrm D,0,-1,\mathrm C)$ và chọn $A'=0$ tại C; bước học là $\alpha=0{,}5$.

1. Tính $Y$, $\delta$ và giá trị mới của $Q(\mathrm D,0)$, mỗi đại lượng trên một dòng.
2. Xác định thời điểm chọn $A'$ và hành động phải thực hiện nếu tiếp tục tương tác.
3. Tính lại câu 1 trong trường hợp giả định C là trạng thái kết thúc.
4. Nếu ngân sách hết ngay sau cập nhật ở câu 1, xác định mục tiêu có thay đổi không.
:::

::: hint
Dùng giá trị hiện tại của ô $(\mathrm C,0)$, không dùng bảng khởi tạo. Phân biệt trạng thái kết thúc với điểm dừng thu thập dữ liệu (Nhận xét 06.13).
:::

::: solution
**Câu 1.**

$$
\begin{aligned}
Y&=-1+1\cdot(-0{,}6)=-1{,}6,\\
\delta&=-1{,}6-0=-1{,}6,\\
Q(\mathrm D,0)&\leftarrow0+0{,}5\cdot(-1{,}6)=-0{,}8 .
\end{aligned}
$$

**Câu 2.** $A'=0$ được chọn ở bước 2 của Thuật toán 06.12, trước khi cập nhật, từ bảng chưa cập nhật. Nếu tương tác tiếp tục, hành động thực hiện tại C phải là đúng $A'=0$.

**Câu 3.** Nếu C kết thúc thì không chọn $A'$: $Y=-1$, $\delta=-1$, $Q(\mathrm D,0)\leftarrow0+0{,}5\cdot(-1)=-0{,}5$.

**Câu 4.** Mục tiêu không đổi: C vẫn là trạng thái không kết thúc, nên $Y$ vẫn chứa $Q(\mathrm C,0)$; hết ngân sách chỉ có nghĩa $A'$ không được thực hiện.

**Kiểm tra lại.** Với $\alpha=0{,}8$ thay cho $0{,}5$, câu 1 cho $0+0{,}8\cdot(-1{,}6)=-1{,}28$, trùng hàng 5 của bảng trong Ví dụ 06.10. Ba lỗi thường gặp: dùng $Q_0(\mathrm C,0)=1$ của bảng khởi tạo nghiêng phải thay cho giá trị hiện tại $-0{,}6$, cho $Y=0$ và $Q(\mathrm D,0)$ không đổi; đặt $Y=R$ khi hết ngân sách, coi C như trạng thái kết thúc, và nhận $-0{,}5$ ở câu 4; và chọn lại hành động tại C sau cập nhật, khi đó hành động được thực hiện có thể khác $A'$ đã dùng trong mục tiêu.
:::

Sarsa (Định nghĩa 06.11, Thuật toán 06.12) cập nhật sau mỗi chuyển bằng mục tiêu một bước, với kết thúc lượt, cắt ngắn và hết ngân sách được xử lý tách bạch (Nhận xét 06.13). Mục tiêu của nó đọc ô của hành động kế tiếp mà chính sách thăm dò đã chọn, kể cả khi hành động ấy không đạt cực đại theo bảng.

<!-- note-topic-id: lec-06-topic-05 -->
## 4. Q-learning và học khác chính sách

Ở mẫu 2 của Ví dụ 06.9, ô $(\mathrm C,0)$ giảm xuống $-0{,}6$ vì mục tiêu Sarsa dùng $Q(\mathrm B,0)=0$ của hành động thăm dò tại B, dù bảng xếp hành động $1$ cao hơn. Muốn ước lượng giá trị của $(\mathrm C,0)$ khi từ B trở đi luôn chọn hành động tốt nhất, chúng ta cần một mục tiêu dùng hành động tốt nhất theo bảng tại B, bất kể hành vi chọn gì. Muốn vậy, chúng ta phải tách hai vai mà Sarsa gộp làm một: chính sách sinh dữ liệu và chính sách mà mục tiêu đánh giá.

### 4.1 Chính sách hành vi và chính sách đích

Một cách trực quan, có hai câu hỏi khác nhau đằng sau mỗi mẫu. Câu thứ nhất là "hành động nào đã được thực hiện"; cơ chế sinh dữ liệu trả lời nó và qua đó xác định ô được cập nhật. Câu thứ hai là "phần tiếp nối được đánh giá theo cách chọn nào"; mục tiêu trả lời nó và qua đó xác định bảng xấp xỉ giá trị của chính sách nào. Trong Sarsa, hai câu có cùng câu trả lời; trong Q-learning, chúng có câu trả lời khác nhau.

![Sơ đồ: ô "Hành vi b" chọn "Hành động" tác động lên "Môi trường", môi trường tạo "Mẫu chuyển" (các mũi tên nét liền, đường sinh dữ liệu). Mẫu chuyển cùng "Bảng Q" đi vào ô "Mục tiêu" ghi "cực đại" và "đích tham lam", mục tiêu cập nhật bảng Q (các mũi tên nét đứt). Một mũi tên từ bảng Q về hành vi ghi "hành vi có thể dùng Q".](img/lec-06/behavior-target.svg)

Hình trên có hai đường. Đường nét liền là đường dữ liệu: chính sách hành vi $b$ chọn hành động, môi trường trả mẫu chuyển. Đường nét đứt là đường học: mẫu chuyển cùng bảng $Q$ tạo mục tiêu theo chính sách đích tham lam, rồi cập nhật bảng. Mũi tên "hành vi có thể dùng Q" nói rằng $b$ được phép lập từ chính bảng $Q$, chẳng hạn là chính sách $\varepsilon$-tham lam theo $Q$, nhưng hành động được thực hiện vẫn do $b$ chọn.

::: definition Định nghĩa 06.14 (Chính sách hành vi, chính sách đích; theo và khác chính sách)
**Chính sách hành vi.** Chính sách hành vi (behavior policy) $b(a\mid s)$ là chính sách chọn các hành động được thực hiện trong môi trường, tức chính sách sinh dữ liệu.

**Chính sách đích.** Chính sách đích (target policy) $\pi(a\mid s)$ là chính sách mà thuật toán đánh giá hoặc cải thiện, tức chính sách có giá trị được bảng xấp xỉ.

**Theo và khác chính sách.** Một phương pháp học theo chính sách (on-policy) nếu $b$ trùng $\pi$ tại mọi thời điểm; học khác chính sách (off-policy) nếu $b$ có thể khác $\pi$.
:::

Định nghĩa phân loại lại hai thuật toán đã có. Trong Thuật toán 06.9, lượt $k$ được sinh và được đánh giá bởi cùng $\pi_k$; trong Thuật toán 06.12, hành động kế tiếp trong mục tiêu lấy từ chính sách đang sinh dữ liệu. Cả hai có $b=\pi$, tức học theo chính sách. Ngược lại, dùng lại các lượt cũ của một chính sách trước đó để đánh giá chính sách hiện tại là học khác chính sách: khi đó $b$ là chính sách cũ, $\pi$ là chính sách mới.

Phân biệt theo/khác chính sách độc lập với phân biệt dự đoán/điều khiển: Q-learning là điều khiển khác chính sách, còn TD(0) với tỉ số lấy mẫu quan trọng (Định nghĩa 06.24) là dự đoán khác chính sách.

### 4.2 Mục tiêu cực đại

Với chính sách đích là chính sách tham lam theo $Q$, phần tiếp nối từ $S'$ bắt đầu bằng hành động có giá trị lớn nhất của hàng $S'$, nên giá trị ước lượng của nó là $\max_aQ(S',a)$. Ví dụ sau dùng lại năm mẫu để so với Sarsa.

::: example Ví dụ 06.11 (Q-learning ở mẫu 1–2)
**Dữ kiện.** Dãy năm ô, $\gamma=1$, $\alpha=0{,}8$. Một lần chạy riêng bắt đầu lại từ bảng khởi tạo nghiêng phải: B $(0,1)$, C $(1,0)$, D $(0,1)$. Hai mẫu đầu của Ví dụ 06.9: $(\mathrm D,0,-1,\mathrm C)$ và $(\mathrm C,0,-1,\mathrm B)$; hành động kế tiếp trong dữ liệu không được dùng.

**Mẫu 1.** Hàng C là $(1,0)$, cực đại bằng $1$.

$$
\begin{aligned}
Y&=-1+\max(1,0)=0,\\
\delta&=0-Q(\mathrm D,0)=0,\\
Q(\mathrm D,0)&\leftarrow0+0{,}8\cdot0=0 .
\end{aligned}
$$

**Mẫu 2.** Hàng B là $(0,1)$, cực đại bằng $1$.

$$
\begin{aligned}
Y&=-1+\max(0,1)=0,\\
\delta&=0-Q(\mathrm C,0)=-1,\\
Q(\mathrm C,0)&\leftarrow1+0{,}8\cdot(-1)=0{,}2 .
\end{aligned}
$$

**So với Sarsa.** Cùng mẫu 2, Sarsa cho $Q(\mathrm C,0)=-0{,}6$ vì dùng $Q(\mathrm B,0)=0$ của hành động thăm dò; Q-learning cho $0{,}2$ vì dùng $Q(\mathrm B,1)=1$.

**Kiểm tra lại.** $0{,}2=1/5$; $1-\tfrac45=\tfrac15$.
:::

![Hai ô C và B nối bởi cạnh "0; thưởng −1". Tại B vẽ hai nhánh: hành động 0 có giá trị 0, ghi "đã lấy mẫu", vẽ nét đứt; hành động 1 có giá trị 1, ghi "cực đại", vẽ nét liền đậm. Chú thích: nét liền đậm là giá trị dùng trong mục tiêu, nên mục tiêu Q-learning dùng giá trị cực đại 1.](img/lec-06/q-learning-target.svg)

Hình này vẽ cùng chuyển với hình của Sarsa, chỉ đổi nhánh được tô đậm. Giá trị cực đại $1$ là số của bảng ước lượng, trong khi đi trái từ B cho phần thưởng $1000$.

::: definition Định nghĩa 06.15 (Mục tiêu Q-learning)
Gọi $Q_t$ là bảng ngay trước cập nhật ở bước $t$. Sau khi thực hiện $A_t$ tại $S_t$ và nhận $R_{t+1}$, $S_{t+1}$, mục tiêu Q-learning là

$$
Y_t=\begin{cases}
R_{t+1}+\gamma\displaystyle\max_{a\in\mathcal A(S_{t+1})}Q_t(S_{t+1},a), & S_{t+1}\in\mathcal S,\\
R_{t+1}, & S_{t+1}\ \text{là trạng thái kết thúc}.
\end{cases}
$$

Sai lệch và cập nhật như Định nghĩa 06.11: $\delta_t=Y_t-Q_t(S_t,A_t)$ và $Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t\delta_t$, các ô khác giữ nguyên.
:::

Mục tiêu Q-learning chỉ cần bộ bốn $(S_t,A_t,R_{t+1},S_{t+1})$, và cả phép cực đại lẫn giá trị cũ đều đọc từ cùng bảng $Q_t$. Khi $S_{t+1}$ kết thúc, hai mục tiêu Sarsa và Q-learning cùng bằng $R_{t+1}$; khi $S_{t+1}$ chưa kết thúc và $\gamma>0$, chúng trùng nhau khi và chỉ khi hành động kế tiếp của Sarsa thuộc tập cực đại $\mathcal G_{Q_t}(S_{t+1})$.

Một nhầm lẫn thường gặp là cho rằng hành vi không ảnh hưởng tới kết quả học vì mục tiêu dùng cực đại. Hành vi $b$ quyết định cặp nào được cập nhật, và cặp mà $b$ không thực hiện giữ mãi giá trị khởi tạo. Nhầm lẫn thứ hai là đọc $\max_aQ_t(S_{t+1},a)$ như giá trị tối ưu thật; nó chỉ là cực đại của các ước lượng hiện có.

### 4.3 Thuật toán Q-learning

Thuật toán Q-learning lặp lại khung của Thuật toán 06.12 với mục tiêu của Định nghĩa 06.15. Vì mục tiêu không dùng hành động kế tiếp, hành động thực hiện ở bước sau được chọn sau cập nhật, theo bảng đã cập nhật.

::: algorithm Thuật toán 06.16 (Q-learning dạng bảng)
**Đầu vào.** Môi trường lấy mẫu được với phân phối đầu $d_0$ trên $\mathcal S$; các tập $\mathcal A(s)$; hệ số $\gamma$; bảng hữu hạn $Q_0$; quy tắc hành vi $b$ (chẳng hạn chính sách $\varepsilon$-tham lam theo bảng hiện tại); lịch bước học $\alpha_n(s,a)\in(0,1]$; ngân sách $H$ cập nhật.

**Đầu ra.** Bảng $Q$ và chính sách tham lam theo bảng cuối (chính sách đích).

**Giả thiết.** Dữ liệu sinh từ chính môi trường cần học; bước học của một cập nhật được chọn trước khi quan sát mẫu dùng cho cập nhật đó.

**Khởi tạo.** $Q\leftarrow Q_0$, $Q(\text{kết thúc},\cdot)=0$; bộ đếm cập nhật của từng cặp $n(s,a)\leftarrow0$; số cập nhật đã làm $h\leftarrow0$; lấy $S\sim d_0$.

**Tham số.** Quy tắc hành vi $b$ (ví dụ $\varepsilon$), $\alpha_n(s,a)$, $H$.

1. Chọn $A$ theo $b(\cdot\mid S)$ từ bảng hiện tại. Chọn bước học $\alpha\leftarrow\alpha_{n(S,A)+1}(S,A)$. Thực hiện $A$, nhận $R$ và $S'$.
2. Nếu $S'$ chưa kết thúc: đặt $Y\leftarrow R+\gamma\max_{a\in\mathcal A(S')}Q(S',a)$ từ bảng chưa cập nhật. Nếu $S'$ kết thúc: đặt $Y\leftarrow R$.
3. Cập nhật $Q(S,A)\leftarrow Q(S,A)+\alpha\,[Y-Q(S,A)]$. Tăng $n(S,A)$ và $h$ thêm $1$.
4. Nếu $h=H$: trả $Q$ và chính sách tham lam theo $Q$.
5. Nếu $S'$ chưa kết thúc: đặt $S\leftarrow S'$; nếu $S'$ kết thúc: lấy $S\sim d_0$. Giữ $Q$, $n$, $h$ và về bước 1.

**Điều kiện dừng.** Sau đúng $H$ cập nhật.

**Chi phí mỗi bước.** Bộ nhớ $O(M)$; không lưu quỹ đạo. Tìm cực đại tại $S'$ tốn $O(m(S'))$, cộng chi phí chọn hành động theo $b$.
:::

Với mẫu 2 của Ví dụ 06.11, bước 2 đọc hàng B $(0,1)$ của bảng chưa cập nhật và cho $Y=0$, bước 3 cho $Q(\mathrm C,0)=0{,}2$, bước 5 đặt $S\leftarrow\mathrm B$; hành động tại B được chọn ở bước 1 của vòng sau, theo bảng đã cập nhật.

Thuật toán 06.16 và Thuật toán 06.12 chỉ khác nhau ở một số hạng: số hạng tiếp nối $\gamma Q(S',A')$ được thay bằng $\gamma\max_aQ(S',a)$. Thay đổi này có ba hệ quả.

- **Dữ liệu.** Sarsa cần bộ năm và phải giữ $A'$ để thực hiện; Q-learning chỉ cần bộ bốn và chọn hành động sau cập nhật.
- **Đại lượng được học.** Kỳ vọng của mục tiêu Sarsa lấy theo chính sách $\varepsilon$-tham lam đang dùng; kỳ vọng của mục tiêu Q-learning là vế phải của phương trình Bellman tối ưu, có nghiệm $q_*$.
- **Trường hợp trùng nhau.** Khi hành vi là chính sách tham lam ($\varepsilon=0$), mỗi $A'$ của Sarsa thuộc $\mathcal G_{Q_t}(S')$, nên hai mục tiêu bằng nhau trên cùng dữ liệu; nếu thêm $S'\ne S$ và cùng quy tắc phá hòa, hai thuật toán còn chọn cùng hành động tiếp theo.

::: example Ví dụ 06.12 (Sarsa và Q-learning trên cùng năm mẫu)
**Dữ kiện.** Năm mẫu $(S,A,R,S')$ của Ví dụ 06.9, $\gamma=1$, $\alpha=0{,}8$:

| Mẫu | $S$ | $A$ | $R$ | $S'$ |
|---:|---|---:|---:|---|
| 1 | D | 0 | $-1$ | C |
| 2 | C | 0 | $-1$ | B |
| 3 | B | 0 | $1000$ | A |
| 4 | D | 1 | $10$ | E |
| 5 | D | 0 | $-1$ | C |

Lần chạy Q-learning bắt đầu lại từ bảng khởi tạo nghiêng phải: B $(0,1)$, C $(1,0)$, D $(0,1)$. Kết quả Sarsa lấy từ Ví dụ 06.10.

**Ba mẫu sau của Q-learning.** Sau mẫu 2, bảng Q-learning là B $(0,1)$, C $(0{,}2;0)$, D $(0,1)$ (Ví dụ 06.11).

- Mẫu 3: A kết thúc, $Y=1000$, $\delta=1000$, $Q(\mathrm B,0)\leftarrow0+0{,}8\cdot1000=800$.
- Mẫu 4: E kết thúc, $Y=10$, $\delta=9$, $Q(\mathrm D,1)\leftarrow1+0{,}8\cdot9=8{,}2$.
- Mẫu 5: hàng C là $(0{,}2;0)$, nên $Y=-1+\max(0{,}2;\,0)=-0{,}8$, $\delta=-0{,}8-0=-0{,}8$, $Q(\mathrm D,0)\leftarrow0+0{,}8\cdot(-0{,}8)=-0{,}64$.

**So sánh hai lần chạy** (mỗi ô theo thứ tự hành động $(0,1)$; hàng B của hai lần chạy giống nhau, $(800;1)$ sau mẫu 3):

| Lần chạy | Hàng C sau mẫu 2 | Hàng D sau mẫu 4 | Hàng D sau mẫu 5 |
|---|---|---|---|
| Sarsa (Ví dụ 06.10) | $(-0{,}6;\,0)$ | $(0;\,8{,}2)$ | $(-1{,}28;\,8{,}2)$ |
| Q-learning | $(0{,}2;\,0)$ | $(0;\,8{,}2)$ | $(-0{,}64;\,8{,}2)$ |

**Diễn giải.** Hai lần chạy dùng cùng bảng khởi tạo, nên mọi khác biệt đến từ mục tiêu. Khác biệt xuất hiện ở mẫu 2, nơi Sarsa đọc $Q(\mathrm B,0)$ còn Q-learning đọc $Q(\mathrm B,1)$, rồi truyền từ C về D ở mẫu 5. Mẫu 1 cho cùng cập nhật vì $A'=0$ thuộc tập cực đại của hàng C; mẫu 3 và 4 vì đi vào trạng thái kết thúc.

**Kiểm tra lại.** $-0{,}64=-16/25=\tfrac45\cdot(-\tfrac45)$.
:::

Trong Ví dụ 06.12, hai thuật toán dùng chung dữ liệu; nếu mỗi thuật toán tự sinh dữ liệu bằng chính sách của nó, hai quá trình có phân phối quỹ đạo khác nhau.

::: remark Nhận xét 06.17 (Q-learning một bước và dữ liệu hành vi)
Muốn ước lượng một kỳ vọng theo chính sách đích $\pi$ bằng hành động do $b$ lấy mẫu, ta nhân với tỉ số lấy mẫu quan trọng (importance sampling ratio) $\pi(a\mid s)/b(a\mid s)$. Q-learning một bước không cần tỉ số này. Ô được cập nhật $Q(S_t,A_t)$ ước lượng $q_*(S_t,A_t)$, đại lượng đã lấy $A_t$ làm điều kiện; phần tiếp nối tại $S_{t+1}$ là cực đại trên bảng, không dùng hành động lấy mẫu từ $b$.

Dữ liệu cho Q-learning vẫn phải thỏa hai điều kiện: mẫu $(R_{t+1},S_{t+1})$ được sinh bởi động lực của chính môi trường, và hành vi $b$ tiếp tục thăm mọi cặp cần học. Phát lại vô hạn lần một tập mẫu hữu hạn không khôi phục được phân phối chuyển và không tự thỏa giả thiết lấy mẫu của Định lý 06.21.
:::

Ví dụ sau so hai mục tiêu trên một chuyển của LunarLander.

::: example Ví dụ 06.13 (Một chuyển của tàu đổ bộ)
**Dữ kiện.** Lấy từ notebook thực hành Bài 06, phần 6–7: $\gamma=0{,}99$, $\alpha=0{,}1$, $Q_t(S_t,A_t)=3$, $R_{t+1}=-1{,}5$, $S_{t+1}$ chưa kết thúc với hàng $Q_t(S_{t+1},\cdot)=(2;\,5;\,5;\,1)$ cho bốn hành động $0,1,2,3$; hành động kế tiếp mà Sarsa đã chọn là $A_{t+1}=0$.

**Sarsa.**

$$
\begin{aligned}
Y_t&=-1{,}5+0{,}99\cdot2=0{,}48,\\
\delta_t&=0{,}48-3=-2{,}52,\\
Q_{t+1}(S_t,A_t)&=3+0{,}1\cdot(-2{,}52)=2{,}748 .
\end{aligned}
$$

**Q-learning.** Cực đại của hàng là $5$ (hành động $1$ và $2$ đồng hạng).

$$
\begin{aligned}
Y_t&=-1{,}5+0{,}99\cdot5=3{,}45,\\
\delta_t&=3{,}45-3=0{,}45,\\
Q_{t+1}(S_t,A_t)&=3+0{,}1\cdot0{,}45=3{,}045 .
\end{aligned}
$$

**Khi vào trạng thái kết thúc.** Nếu thay vào đó tàu rơi, $S_{t+1}$ kết thúc với $R_{t+1}=-100$, thì cả hai thuật toán dùng $Y_t=-100$, $\delta_t=-103$ và $Q_{t+1}(S_t,A_t)=3-10{,}3=-7{,}3$.

**Diễn giải.** Hai mục tiêu trùng nhau khi $A_{t+1}\in\{1,2\}$, tập cực đại của hàng $S_{t+1}$. Với $A_{t+1}=0$, Sarsa kéo ô xuống còn Q-learning kéo ô lên.

**Kiểm tra lại.** $3{,}045-2{,}748=0{,}297=0{,}1\cdot0{,}99\cdot(5-2)$, tức $\alpha\gamma$ nhân hiệu hai số hạng tiếp nối.
:::

**Trong thực hành.** Bài thực hành cài đặt Thuật toán 06.16 với hành vi $b$ là chính sách $\varepsilon_k$-tham lam theo bảng hiện tại và chính sách đích là chính sách tham lam theo bảng (notebook, phần 7–8). Ngoài số hạng cực đại trong mục tiêu, mã Q-learning chỉ khác mã Sarsa ở chỗ hành động thực hiện tiếp được chọn sau cập nhật. Vì chính sách đích là chính sách tham lam, notebook đánh giá bảng Q-learning bằng cách chạy chính sách tham lam đó, không thăm dò và không cập nhật; chính sách hành vi với $\varepsilon=0{,}05$ là một chính sách khác và được đánh giá riêng (phần 8.2).

::: exercise Bài tập 06.5 (Mục tiêu Sarsa và Q-learning trên cùng chuyển)
Trên dãy năm ô ($\gamma=1$), bảng hiện tại có $Q(\mathrm B,0)=800$, $Q(\mathrm B,1)=1$. Chuyển quan sát được là $(\mathrm C,0,-1,\mathrm B)$, và Sarsa đã chọn hành động kế tiếp $A'=1$ tại B.

1. Tính mục tiêu Sarsa và mục tiêu Q-learning.
2. Nêu điều kiện cần và đủ để hai mục tiêu trùng nhau khi trạng thái kế tiếp chưa kết thúc, với cùng bảng và cùng phần thưởng.
3. Nêu cặp nào được cập nhật trong mỗi thuật toán.
:::

::: hint
Sarsa phải dùng $A'=1$ đã cho; Q-learning dùng cực đại của hàng B. So sánh hai số hạng tiếp nối mà không đổi dữ liệu.
:::

::: solution
**Câu 1.** Mục tiêu Sarsa là $-1+Q(\mathrm B,1)=-1+1=0$. Mục tiêu Q-learning là $-1+\max(800,1)=799$.

**Câu 2.** Hai mục tiêu chỉ khác ở số hạng tiếp nối, nên chúng trùng nhau khi và chỉ khi $\gamma Q(S',A')=\gamma\max_aQ(S',a)$. Với $\gamma>0$, điều này tương đương $Q(S',A')=\max_aQ(S',a)$, tức $A'\in\mathcal G_Q(S')$; không cần cực đại duy nhất. Với $\gamma=0$, hai mục tiêu luôn trùng nhau và bằng $R$.

**Câu 3.** Cả hai thuật toán chỉ cập nhật ô $(\mathrm C,0)$ của cặp đã thực hiện; hành vi quyết định ô nào được cập nhật, mục tiêu quyết định cập nhật hướng về đâu.

**Kiểm tra lại.** Ở đây $A'=1\notin\mathcal G_Q(\mathrm B)=\{0\}$, nên hai mục tiêu khác nhau, khớp $0\ne799$. Hai lỗi thường gặp: để Sarsa tự thay $A'=1$ bằng hành động tốt hơn, khi đó thuật toán đã thành Q-learning; và cho rằng Q-learning cập nhật ô $(\mathrm B,0)$ vì ô này đạt cực đại, trong khi ô được cập nhật luôn là cặp $(S,A)$ đã thực hiện.
:::

Như vậy, Q-learning (Thuật toán 06.16) tách chính sách hành vi khỏi chính sách đích (Định nghĩa 06.14) và khác Sarsa đúng ở số hạng tiếp nối của mục tiêu (Định nghĩa 06.15). Tuy nhiên, năm mẫu không đủ để kết luận về chính sách tốt nhất: hai bảng đều xếp phải trên trái tại D (Ví dụ 06.12), trong khi đi trái liên tục cho $998$.

<!-- note-topic-id: lec-06-topic-06 -->
## 5. Điều kiện hội tụ

Xét dãy năm ô với $\gamma=0{,}9$: $q_*(\mathrm D,1)=10$ còn đi trái ba lần cho $q_*(\mathrm D,0)=-1+0{,}9\cdot(-1)+0{,}81\cdot1000=808{,}1$. Nếu hành vi là chính sách tham lam theo bảng khởi tạo nghiêng phải, mọi lượt đều là D→E: ô $(\mathrm D,1)$ tiến về $10$, ô $(\mathrm D,0)$ giữ mãi giá trị $0$, và bảng không bao giờ tới $q_*$.

Muốn bảng tiến tới $q_*$, chúng ta cần giả thiết về môi trường, về cách thăm dò và về bước học; các giả thiết này mở rộng điều kiện hội tụ của TD(0) (Định lý 05.30) từ trạng thái sang cặp trạng thái–hành động.

### 5.1 Từ cập nhật mẫu tới hội tụ

Về mặt ý tưởng, một cập nhật Q-learning là một bước lặp có nhiễu của toán tử Bellman tối ưu. Với cặp $(s,a)$ và bảng $Q_t$, kỳ vọng của mục tiêu Q-learning theo $(R_{t+1},S_{t+1})$ là

$$
r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\max_{a'}Q_t(s',a'),
$$

đúng là vế phải của phương trình Bellman tối ưu (Bellman optimality equation) cho $q_*$ (Định lý 04.25(c)).

Dạng $Q$ của toán tử Bellman tối ưu biến bảng $Q$ thành bảng có ô $(s,a)$ bằng biểu thức trên, với $Q$ thay cho $Q_t$; toán tử $T_*$ trong bảng ký hiệu tác động trên bảng $\mathcal S\to\mathbb R$. Nhắc lại Mệnh đề 04.24: khi $\gamma<1$, $T_*$ là ánh xạ co hệ số $\gamma$ theo chuẩn vô cùng, vì $|\max_ax_a-\max_ay_a|\le\max_a|x_a-y_a|$ (Bổ đề 04.23).

Cùng lập luận áp dụng cho dạng $Q$. Với hai bảng $Q$, $Q'$ bằng $0$ tại trạng thái kết thúc, số hạng $r(s,a)$ triệt tiêu trong hiệu của hai ảnh tại $(s,a)$. Theo Bổ đề 04.23 và $\sum_{s'}p(s'\mid s,a)=1$, hiệu ấy có trị tuyệt đối không vượt

$$
\gamma\sum_{s'}p(s'\mid s,a)\max_{a'}\lvert Q(s',a')-Q'(s',a')\rvert\le\gamma\lVert Q-Q'\rVert_\infty ,
$$

với $\lVert\cdot\rVert_\infty$ là chuẩn vô cùng trên các ô của bảng. Vì vậy, nếu không có nhiễu, lặp lại dạng $Q$ ấy đưa mọi bảng về $q_*$.

Mỗi mẫu chỉ cho một giá trị ngẫu nhiên quanh kỳ vọng đó và chỉ cập nhật một ô, nên cần ba điều:

- mọi ô được cập nhật mãi;
- bước học giảm đủ chậm để đi tới đích nhưng đủ nhanh để triệt tiêu nhiễu;
- các giả thiết làm cho toán tử là ánh xạ co.

Với Sarsa, kỳ vọng của mục tiêu phụ thuộc chính sách chọn $A_{t+1}$, nên còn cần chính sách ấy dần trở thành tham lam.

### 5.2 Tham lam trong giới hạn với thăm dò vô hạn

Mục tiêu Sarsa dùng hành động kế tiếp do chính sách hành vi chọn. Nếu hành vi giữ $\varepsilon$ cố định, kỳ vọng của mục tiêu Sarsa lấy theo một chính sách còn thăm dò; nếu bảng ổn định tại một giới hạn, giới hạn đó là giá trị của chính sách $\varepsilon$-tham lam theo chính bảng ấy, nói chung khác $q_*$. Nếu hành vi bỏ thăm dò quá sớm, một số cặp không còn được cập nhật, như ô $(\mathrm D,0)$ trong thí nghiệm ở đầu mục. Lịch thăm dò phải tránh cả hai tình huống trên. Ví dụ sau tính hai đại lượng tương ứng cho chính sách $\varepsilon_k$-tham lam tại ô bắt đầu D.

::: example Ví dụ 06.14 (Khối xác suất tham lam và số lần thử cặp $(\mathrm D,0)$ khi $\varepsilon$ giảm)
**Dữ kiện.** Tại ô D có hai hành động. Giả sử ở mọi lượt, hàng D của bảng có cùng một cực đại duy nhất là hành động $1$. Lượt $k$ dùng chính sách $\varepsilon_k$-tham lam (Định nghĩa 06.3); mỗi lượt bắt đầu tại D, nên D được ghé ít nhất một lần mỗi lượt.

**Khối xác suất trên hành động cực đại.** Theo Định nghĩa 06.3, khối này là $1-\varepsilon_k+\varepsilon_k/2=1-\varepsilon_k/2$.

- Với $\varepsilon$ cố định bằng $1/4$: khối bằng $7/8$ ở mọi lượt, không tiến tới $1$.
- Với $\varepsilon_k=1/k$: khối bằng $1-\tfrac1{2k}$, lần lượt $0{,}5$; $0{,}95$; $0{,}995$ tại $k=1,10,100$, và tiến tới $1$.

**Số lần thử cặp $(\mathrm D,0)$.** Gọi $\mathcal E_k$ là biến cố "ở thời điểm đầu của lượt $k$, tác tử chọn hành động $0$ tại D". Vì hàng D luôn có cực đại duy nhất là hành động $1$, xác suất của $\mathcal E_k$ có điều kiện theo toàn bộ quá khứ luôn bằng $\varepsilon_k/2$; một xác suất có điều kiện không phụ thuộc quá khứ kéo theo các biến cố $\mathcal E_1,\mathcal E_2,\dots$ độc lập. Bổ đề Borel–Cantelli phát biểu: nếu $\sum_k\Pr(\mathcal E_k)<\infty$ thì hầu chắc chắn chỉ hữu hạn biến cố xảy ra; nếu các biến cố độc lập và $\sum_k\Pr(\mathcal E_k)=\infty$ thì hầu chắc chắn vô hạn biến cố xảy ra.

- Với $\varepsilon_k=1/k$: $\sum_k\tfrac1{2k}=\infty$, nên cặp $(\mathrm D,0)$ được thực hiện vô hạn lần, hầu chắc chắn.
- Với $\varepsilon_k=1/k^2$: $\sum_k\tfrac1{2k^2}<\infty$, nên hầu chắc chắn chỉ hữu hạn biến cố $\mathcal E_k$ xảy ra. Vì hành động $1$ tại D kết thúc lượt ngay, cặp $(\mathrm D,0)$ chỉ có thể xuất hiện trong các lượt có $\mathcal E_k$, tức trong hữu hạn lượt; khối xác suất $1-\tfrac1{2k^2}$ vẫn tiến tới $1$.

**Kiểm tra lại.** Với $k=10$: $1-\tfrac1{20}=0{,}95$. Với $\varepsilon_k=1/k^2$, $\sum_k\tfrac1{k^2}\approx1{,}645$, nên tổng xác suất là khoảng $0{,}822$.
:::

Ví dụ 06.14 tách hai yêu cầu. Lịch $\varepsilon_k=1/k^2$ đạt yêu cầu "tham lam trong giới hạn" nhưng không đạt yêu cầu "thử vô hạn lần"; lịch $\varepsilon=1/4$ cố định thì ngược lại. Định nghĩa sau đòi cả hai.

::: definition Định nghĩa 06.18 (Tham lam trong giới hạn với thăm dò vô hạn, GLIE)
Gọi $t$ là chỉ số bước toàn cục qua mọi lượt, $\pi_t$ là chính sách dùng để chọn hành động tại bước $t$, $Q_t$ là bảng tại bước đó và $\mathcal G_{t}(s)=\operatorname*{arg\,max}_{a}Q_t(s,a)$. Dãy chính sách $(\pi_t)$ gọi là tham lam trong giới hạn với thăm dò vô hạn (greedy in the limit with infinite exploration, GLIE) nếu hầu chắc chắn hai điều sau cùng đúng:

1. **Thăm dò vô hạn.** Với mọi cặp hợp lệ $(s,a)$, $C_t(s,a)\to\infty$ khi $t\to\infty$, trong đó $C_t(s,a)$ là số lần cặp được thực hiện trong các bước $0,\dots,t$.
2. **Tham lam trong giới hạn.** Với mọi trạng thái $s$, $\sum_{a\in\mathcal G_t(s)}\pi_t(a\mid s)\to1$ khi $t\to\infty$.
:::

Yêu cầu thứ nhất là độ phủ: mọi cặp nhận vô hạn mẫu. Yêu cầu thứ hai nói rằng khối xác suất của chính sách dồn dần vào các hành động cực đại của bảng hiện tại; nó cho phép đồng hạng và không đòi chính sách hội tụ tới một hành động duy nhất. Bộ đếm lần thăm $C_t$ khác bộ đếm $N$ của Định nghĩa 06.8, vốn chỉ đếm lợi tức được dùng.

Nhầm lẫn thường gặp là coi "$\varepsilon_k\to0$" là đủ cho GLIE; Ví dụ 06.14 với $\varepsilon_k=1/k^2$ là phản ví dụ. Ngay cả với $\varepsilon_k=1/k$, lập luận của ví dụ chỉ áp dụng cho ô D, nơi mọi lượt bắt đầu, và dùng giả định hàng D giữ cực đại cố định. Khi cực đại đổi chỗ, lập luận phải dựa trên cận dưới $\varepsilon_k/2$ cho xác suất chọn mỗi hành động; một trạng thái chỉ tới được qua nhiều bước thăm dò cần kiểm riêng. Theo Sutton và Barto (2018, §6.4), với chính sách $\varepsilon$-tham lam có thể đặt $\varepsilon=1/t$.

Nếu $t$ trong lịch $\varepsilon=1/t$ là chỉ số bước toàn cục, thăm dò vô hạn vẫn phải được kiểm theo từng cặp. Giả sử một trạng thái có hai hành động chỉ được ghé tại các bước toàn cục $t_n=2^n$, $n=1,2,\dots$, và hàng của nó giữ cùng một cực đại duy nhất. Tổng xác suất chọn hành động không cực đại tại các lần ghé là $\sum_{n\ge1}2^{-n}/2=1/2<\infty$, nên theo vế thứ nhất của bổ đề Borel–Cantelli, hành động ấy chỉ được thử hữu hạn lần, hầu chắc chắn.

Singh và cộng sự (2000) dùng lịch theo trạng thái $\varepsilon_t(s)=c/C_t(s)$ với $0<c<1$, trong đó $C_t(s)=\sum_aC_t(s,a)$ là số lần ghé $s$ trong các bước $0,\dots,t$ (bộ đếm của Định nghĩa 06.18). Khi đó tại mỗi trạng thái được ghé vô hạn lần, với $m(s)$ hành động, tổng các xác suất chọn một hành động cố định ở các lần ghé là ít nhất $\tfrac{c}{m(s)}\big(1+\tfrac12+\tfrac13+\cdots\big)=\infty$. Các lần chọn không độc lập, nên kết luận "thử vô hạn lần" cần dạng có điều kiện của bổ đề Borel–Cantelli. Singh và cộng sự chứng minh lịch này thỏa định nghĩa GLIE của họ, vốn chỉ đòi điều kiện tại các trạng thái được ghé vô hạn lần.

### 5.3 Điều kiện Robbins–Monro theo cặp

Nhắc lại điều kiện của Định lý 05.30: bước học dùng ở lần cập nhật thứ $n$ của trạng thái $s$ thỏa $\sum_n\alpha_n(s)=\infty$ và $\sum_n\alpha_n(s)^2<\infty$. Trong điều khiển, đơn vị được cập nhật là cặp, và một cặp có thể được cập nhật rất thưa. Ví dụ sau cho thấy một lịch viết theo thời gian toàn cục có thể thỏa điều kiện trên toàn bộ quá trình nhưng không thỏa cho từng cặp.

::: example Ví dụ 06.15 (Lịch bước học toàn cục và một cặp được cập nhật thưa)
**Dữ kiện.** Một cặp $(s,a)$ chỉ được cập nhật tại các bước toàn cục $t_n=2^n$, $n=1,2,\dots$; lịch bước học viết theo thời gian toàn cục là $\alpha_t=1/t$.

**Tổng bước học mà cặp nhận được.**

$$
\sum_{n=1}^{\infty}\alpha_{t_n}=\sum_{n=1}^{\infty}2^{-n}=1<\infty ,
$$

nên tổng thứ nhất không thỏa cho cặp này, dù $\sum_t1/t=\infty$ trên toàn bộ quá trình.

**Kiểm tra lại.** Các số hạng là $\tfrac12,\tfrac14,\tfrac18,\dots$, tổng của $j$ số hạng đầu bằng $1-2^{-j}<1$.
:::

::: definition Định nghĩa 06.19 (Điều kiện Robbins–Monro theo cặp)
Với mỗi cặp hợp lệ $(s,a)$, gọi $\alpha_n(s,a)\in(0,1]$ là bước học dùng ở lần cập nhật thứ $n$ của cặp, được chọn từ thông tin có trước mẫu dùng cho lần cập nhật đó. Lịch bước học thỏa điều kiện Robbins–Monro theo cặp nếu, với mọi cặp, hầu chắc chắn

$$
\begin{aligned}
\sum_{n=1}^{\infty}\alpha_n(s,a)&=\infty,\\
\sum_{n=1}^{\infty}\alpha_n(s,a)^2&<\infty .
\end{aligned}
$$

Ở bước $t$, bước học được dùng là $\alpha_t=\alpha_{n(S_t,A_t)+1}(S_t,A_t)$, với $n(S_t,A_t)$ là số cập nhật cặp đã hoàn thành trước bước $t$.
:::

Tổng thứ nhất vô hạn bảo đảm ảnh hưởng của giá trị khởi tạo bị quên dần: nếu tổng hữu hạn như ở Ví dụ 06.15, bảng có thể dừng ở một giá trị còn mang dấu vết của khởi tạo. Tổng thứ hai hữu hạn bảo đảm nhiễu tích lũy của các mục tiêu bị khống chế; với bước hằng, nhiễu không bao giờ triệt tiêu. Hai tổng là giả thiết của định lý hội tụ; sau hữu hạn bước, không thể dùng hai tổng này để kiểm bảng đã hội tụ hay chưa.

Định nghĩa 06.19 mở rộng điều kiện theo trạng thái của Định lý 05.30 bằng cách đánh số theo lần cập nhật riêng của từng cặp; khi mỗi trạng thái chỉ có một hành động, hai điều kiện trùng nhau. Điều kiện mang tên Robbins và Monro (1951); Sutton và Barto (2018, §2.5, công thức 2.7) phát biểu nó cho dãy bước học của phép cập nhật gia tăng.

### 5.4 Hội tụ của Q-learning và Sarsa

Với GLIE (Định nghĩa 06.18) và Robbins–Monro theo cặp (Định nghĩa 06.19), ta phát biểu được hai định lý hội tụ; nhận xét sau gom các giả thiết nền chung của chúng.

::: remark Nhận xét 06.20 (Giả thiết nền và vị trí của dãy năm ô)
Hai định lý dưới đây đặt chung các giả thiết nền sau:

- MDP hữu hạn với động lực dừng (không đổi theo thời gian);
- phần thưởng bị chặn;
- $0\le\gamma<1$;
- biểu diễn bảng với $Q_0$ hữu hạn;
- mẫu $(R_{t+1},S_{t+1})$, có điều kiện theo toàn bộ lịch sử và cặp hiện tại $(S_t,A_t)=(s,a)$, có phân phối $p(\cdot,\cdot\mid s,a)$;
- bước học của mỗi cập nhật được chọn từ thông tin có trước mẫu dùng cho cập nhật đó.

Dãy năm ô dùng $\gamma=1$, trái với giả thiết $0\le\gamma<1$, và bước học hằng $0{,}8$, có $\sum_n0{,}8^2=\infty$ nên không thỏa Định nghĩa 06.19; do đó dãy năm ô nằm ngoài các định lý.
:::

::: theorem Định lý 06.21 (Hội tụ của Q-learning dạng bảng)
**Giả thiết.** Các giả thiết nền của Nhận xét 06.20 đúng. Thuật toán 06.16 chạy với $H=\infty$. Mọi cặp hợp lệ được cập nhật vô hạn lần, hầu chắc chắn. Lịch bước học thỏa Định nghĩa 06.19.

**Kết luận.** Với mọi cặp hợp lệ $(s,a)$, $Q_t(s,a)\to q_*(s,a)$ hầu chắc chắn khi $t\to\infty$.

**Điều kiện áp dụng.** Chính sách hành vi $b$ tùy ý, kể cả thay đổi theo bảng, miễn là nó giữ độ phủ; không cần GLIE và không cần tỉ số lấy mẫu quan trọng.

**Phạm vi.** Kết quả là tiệm cận: không cho tốc độ, không cho biết bảng tại một ngân sách hữu hạn gần $q_*$ đến đâu, và chỉ áp dụng cho biểu diễn bảng. Chứng minh nằm ngoài phạm vi học phần; xem Watkins và Dayan (1992, tr. 282 và phần chứng minh sau đó) và Bertsekas và Tsitsiklis (1996, §5.6). Watkins và Dayan phát biểu với $0\le\alpha_n<1$. Vì tổng bình phương hữu hạn, chỉ có hữu hạn lần $\alpha_n=1$; với lịch tất định theo số lần cập nhật, định lý áp dụng từ sau lần cuối ấy. Do đó lịch $\alpha_n=1/n$ (có $\alpha_1=1$) vẫn nằm trong phạm vi.
:::

::: theorem Định lý 06.22 (Hội tụ của Sarsa dạng bảng với GLIE)
**Giả thiết.** Các giả thiết nền của Nhận xét 06.20 đúng. Thuật toán 06.12 chạy với $H=\infty$, trong đó hành động $A_{t+1}$, thực hiện ở bước $t+1$, lấy theo $\pi_{t+1}(\cdot\mid S_{t+1})$ với $\pi_{t+1}$ lập theo $Q_t$, bảng ngay trước cập nhật ở bước $t$. Dãy chính sách $(\pi_t)$ là GLIE (Định nghĩa 06.18). Lịch bước học thỏa Định nghĩa 06.19.

**Kết luận.** Với mọi cặp hợp lệ $(s,a)$, $Q_t(s,a)\to q_*(s,a)$ hầu chắc chắn; khối xác suất của $\pi_t$ dồn dần vào các hành động tối ưu.

**Điều kiện áp dụng.** Với chính sách $\varepsilon_t$-tham lam, $\varepsilon_t$ phải giảm về $0$ nhưng đủ chậm để mọi cặp vẫn được thử vô hạn lần; với $\varepsilon$ cố định dương, điều kiện tham lam trong giới hạn không thỏa.

**Phạm vi.** Kết quả là tiệm cận và chỉ cho biểu diễn bảng. Chứng minh nằm ngoài phạm vi học phần; xem Singh, Jaakkola, Littman và Szepesvári (2000, định nghĩa GLIE tr. 291–292, Định lý 1 tr. 294–295). Định nghĩa GLIE gốc chỉ đòi điều kiện tại các trạng thái được ghé vô hạn lần và đi kèm giả thiết MDP liên thông; Định nghĩa 06.18 đòi mọi cặp được thăm vô hạn lần, nên mạnh hơn và thay cho giả thiết liên thông.
:::

Hai định lý nói rằng, khi mọi cặp được cập nhật mãi và bước học thỏa Robbins–Monro theo cặp, bảng Q-learning tiến tới $q_*$ bất kể hành vi thăm dò ra sao, còn bảng Sarsa tiến tới cùng giới hạn nếu thăm dò tắt dần theo GLIE. Vì tập hành động hữu hạn, sau một thời điểm ngẫu nhiên đủ lớn mọi hành động cực đại của $Q_t$ đều tối ưu, nên chính sách tham lam theo $Q_t$ là tối ưu; thời điểm ấy không biết trước. Q-learning có điều kiện về hành vi yếu hơn; không định lý nào cho biết thuật toán nào nhanh hơn trên một bài toán cụ thể.

Các giả thiết có vai trò riêng; bỏ từng giả thiết dẫn tới hệ quả sau.

- Bỏ độ phủ: trong thí nghiệm ở đầu mục ($\gamma=0{,}9$, hành vi tham lam theo bảng khởi tạo nghiêng phải), ô $(\mathrm D,0)$ giữ mãi $0$ trong khi $q_*(\mathrm D,0)=808{,}1$.
- Bỏ Robbins–Monro: xét một cặp có mục tiêu là các biến độc lập nhận $\pm1$ với xác suất bằng nhau, giá trị cần học là $0$. Với bước hằng $0{,}8$, $Q_n=0{,}2\,Q_{n-1}+0{,}8\,Y_n$ nên $\operatorname{Var}Q_n=0{,}04\operatorname{Var}Q_{n-1}+0{,}64$, tiến tới $0{,}64/0{,}96=2/3$; bảng dao động mãi quanh $0$.
- Bỏ GLIE (chỉ với Sarsa): với $\varepsilon$ cố định, mục tiêu Sarsa đánh giá chính sách $\varepsilon$-tham lam. Trong ví dụ đi men vách đá của Sutton và Barto (2018, Ví dụ 6.6), Sarsa với $\varepsilon=0{,}1$ học con đường an toàn xa vách, còn Q-learning học con đường tối ưu sát vách. Ví dụ này cho thấy hệ quả của $\varepsilon$ cố định lên con đường được học; vì không chiết khấu ($\gamma=1$), nó nằm ngoài giả thiết $\gamma<1$ của Định lý 06.22.
- Bỏ $\gamma<1$: với $\gamma=1$, toán tử Bellman tối ưu không còn là ánh xạ co theo chuẩn vô cùng, nên định lý không áp dụng và cần giả thiết thay thế. Vòng B–C không cho phản ví dụ, vì giá trị tối ưu của dãy năm ô vẫn hữu hạn (Nhận xét 06.2). Dãy thuộc lớp bài toán đường đi ngắn nhất ngẫu nhiên (stochastic shortest path), mà Bertsekas và Tsitsiklis (1996, §2.2, §5.6) xét với $\gamma=1$ dưới các giả thiết thay cho $\gamma<1$. Ở đây, $\pi_L$ kết thúc từ mọi trạng thái và mọi chính sách dừng có lượt vô hạn đều có lợi tức $-\infty$, vì mỗi bước không kết thúc nhận $-1$.
- Bỏ tính Markov của mẫu: trên LunarLander với các ô gộp nhiều quan sát, phân phối của ô kế tiếp phụ thuộc vị trí thật bên trong ô, nên không tồn tại một $p(\cdot\mid s,a)$ chung cho cả ô (Tình huống 06.1).

::: remark Nhận xét 06.23 (Hội tụ của điều khiển Monte Carlo)
Các lợi tức trong cùng một ô của Thuật toán 06.9 đến từ những chính sách $\pi_k$ khác nhau, không có chung kỳ vọng $q_\pi$; vì vậy, kể cả với dãy chính sách GLIE, tính chất của trung bình mẫu và Mệnh đề 06.6 không ghép thành một chứng minh hội tụ tới $q_*$.

Sutton và Barto (2018, §5.3) ghi rằng hội tụ của biến thể Monte Carlo với điểm bắt đầu thăm dò (exploring starts) chưa được chứng minh tổng quát và dẫn Tsitsiklis (2002) cho một lời giải từng phần.
:::

**Trong thực hành.** Trong bài thực hành LunarLander, bảng là bảng trên các ô gộp quan sát liên tục, hành vi giữ $\varepsilon_{\min}=0{,}05$ và bước học có sàn $0{,}05$; vì thế ba giả thiết Markov, GLIE và Robbins–Monro theo cặp không thỏa. Định lý 06.21–06.22 không áp dụng cho hai bảng của notebook, nên định lý không cho kết luận nào về hội tụ hay phân kỳ của chúng; chất lượng của hai bảng được đo bằng thực nghiệm (Tình huống 06.1).

::: exercise Bài tập 06.6 (Kiểm giả thiết hội tụ)
Giả sử MDP hữu hạn với động lực dừng, phần thưởng bị chặn, $\gamma=0{,}9$, $Q_0$ hữu hạn, mẫu sinh từ chính MDP, mọi cặp được cập nhật vô hạn lần, và mọi trạng thái có hai hành động. Với mỗi trường hợp, xác định Định lý 06.21 hoặc 06.22 có áp dụng không; nếu không, nêu giả thiết còn thiếu.

| Trường hợp | Thuật toán và hành vi | Bước học theo cặp |
|---|---|---|
| a | Q-learning, $\varepsilon$-tham lam với $\varepsilon=0{,}25$ cố định | $\alpha_n=1/n$ |
| b | Sarsa, $\varepsilon$-tham lam với $\varepsilon=0{,}25$ cố định | $\alpha_n=1/n$ |
| c | Sarsa, dãy chính sách GLIE | $\alpha_n=0{,}8$ |

Ở trường hợp b, có ít nhất một trạng thái mà hàng của bảng có cực đại duy nhất tại mọi bước từ một thời điểm nào đó.
:::

::: hint
Kiểm riêng điều kiện bước học (Định nghĩa 06.19) và điều kiện về hành vi của từng định lý. Trong trường hợp b, tính khối xác suất trên hành động cực đại; trong trường hợp c, tính tổng bình phương bước học.
:::

::: solution
**Trường hợp a.** Áp dụng được Định lý 06.21. Lịch $1/n$ thỏa hai tổng (Bài tập 05.11); Q-learning chỉ cần độ phủ, đã có theo giả thiết, và không cần hành vi trở nên tham lam.

**Trường hợp b.** Không áp dụng được Định lý 06.22: thiếu điều kiện tham lam trong giới hạn. Tại trạng thái có cực đại duy nhất, khối xác suất trên cực đại là $1-0{,}25+0{,}25/2=0{,}875=7/8$, không tiến tới $1$.

**Trường hợp c.** Không áp dụng được Định lý 06.22: $\sum_n0{,}8^2=\infty$ vi phạm tổng thứ hai của Định nghĩa 06.19.

**Kiểm tra lại.** Trong b và c, định lý không áp dụng, nên kết luận $Q_t\to q_*$ không có căn cứ từ định lý và thuật toán cũng không được chứng minh là phân kỳ. Hai lỗi thường gặp: coi một bước học dương bất kỳ, hoặc một $\varepsilon$ dương cố định, là đủ, trong khi bước hằng $0{,}8$ vi phạm tổng thứ hai và $\varepsilon$ cố định giữ khối cực đại ở $7/8$; và đòi GLIE cho Q-learning ở trường hợp a, trong khi Định lý 06.21 chỉ cần độ phủ.
:::

Dưới các giả thiết nền (Nhận xét 06.20), độ phủ và bước học Robbins–Monro theo cặp (Định nghĩa 06.19) đủ để Q-learning hội tụ hầu chắc chắn tới $q_*$ (Định lý 06.21), còn Sarsa cần thêm GLIE (Định nghĩa 06.18, Định lý 06.22). Hai định lý chỉ cho kết luận tiệm cận, nên bảng thu được sau một ngân sách hữu hạn, như trên LunarLander, phải được đánh giá bằng cách chạy chính sách qua nhiều lượt.

<!-- note-topic-id: lec-06-topic-08 -->
## 6. Đọc thêm: dự đoán khác chính sách và sai số đánh giá

Giả sử chúng ta muốn đánh giá chính sách luôn đi trái $\pi_L$ tại ô D, nhưng dữ liệu do chính sách hành vi $b$ là chính sách $1/4$-tham lam theo bảng khởi tạo nghiêng phải sinh ra: $b(0\mid\mathrm D)=1/8$, $b(1\mid\mathrm D)=7/8$ (Ví dụ 06.4). Phần lớn mẫu tại D đi phải và cho lợi tức $10$, trong khi $\pi_L$ không bao giờ đi phải, nên trung bình thô của các mẫu ước lượng sai đại lượng cần tìm. Với bài toán dự đoán này, chúng ta nhân mỗi mẫu với một tỉ số xác suất.

Bài thực hành đánh giá mỗi chính sách học được bằng trung bình của $100$ lượt, và sai số của trung bình như vậy có một chặn xác suất. Chúng ta nêu điều kiện để tỉ số xác suất và chặn sai số này đúng.

### 6.1 Dự đoán TD(0) khác chính sách

Về mặt ý tưởng, mẫu đi trái tại D hiếm dưới $b$ nhưng chắc chắn dưới $\pi_L$, nên phải được tính với trọng số lớn; mẫu đi phải không bao giờ xảy ra dưới $\pi_L$, nên có trọng số $0$. Với trọng số $\pi_L(a\mid\mathrm D)/b(a\mid\mathrm D)$, mẫu đi trái nhận $1/(1/8)=8$, mẫu đi phải nhận $0/(7/8)=0$, và kỳ vọng của trọng số theo $b$ là $\tfrac18\cdot8+\tfrac78\cdot0=1$.

::: definition Định nghĩa 06.24 (Tỉ số lấy mẫu quan trọng và điều kiện hỗ trợ)
Cho chính sách đích $\pi$ và chính sách hành vi $b$. Điều kiện hỗ trợ (coverage), khác với độ phủ (yêu cầu thăm dò vô hạn của Định nghĩa 06.18), là: với mọi $s\in\mathcal S$ và $a\in\mathcal A(s)$, $\pi(a\mid s)>0$ kéo theo $b(a\mid s)>0$. Với hành động $A_t$ lấy từ $b$, tỉ số lấy mẫu quan trọng (importance sampling ratio) một bước là

$$
\rho_t=\frac{\pi(A_t\mid S_t)}{b(A_t\mid S_t)}\in[0,\infty).
$$
:::

Mẫu số dương vì $A_t$ được lấy từ $b$; điều kiện hỗ trợ bảo đảm mọi hành động mà $\pi$ có thể chọn đều có thể xuất hiện trong dữ liệu. Một cách dùng tỉ số là nhân nó vào mục tiêu của TD(0):

$$
V(S_t)\leftarrow V(S_t)+\alpha\Big(\rho_t\big[R_{t+1}+\gamma V(S_{t+1})\big]-V(S_t)\Big).
$$

Theo Sutton và Barto (2018, §7.3, công thức 7.9–7.10), khi số bước bằng $1$, ta nhân tỉ số vào toàn bộ sai lệch:

$$
V(S_t)\leftarrow V(S_t)+\alpha\,\rho_t\big[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\big].
$$

Hai dạng có cùng kỳ vọng có điều kiện, vì hiệu của chúng là $\alpha(\rho_t-1)V(S_t)$ và kỳ vọng của $\rho_t$ bằng $1$. Mệnh đề sau phát biểu cho dạng thứ nhất.

::: proposition Mệnh đề 06.25 (Kỳ vọng có điều kiện của gia số TD(0) khác chính sách)
**Giả thiết.** MDP hữu hạn với động lực dừng, phần thưởng bị chặn, $0\le\gamma<1$; $\pi$ và $b$ cố định và thỏa điều kiện hỗ trợ; $V_t$ là bảng tại bước $t$, $V_t=0$ tại trạng thái kết thúc. Đặt $Y_t=R_{t+1}+\gamma V_t(S_{t+1})$ và gọi $\mathcal F_t$ là thông tin có trước khi lấy $A_t$, gồm $S_t$ và $V_t$.

**Kết luận.** Với $S_t=s$, $\mathbb E_b\big[\rho_tY_t-V_t(s)\mid\mathcal F_t\big]=(T_\pi V_t)(s)-V_t(s)$.

**Điều kiện áp dụng.** Kỳ vọng lấy theo $A_t\sim b(\cdot\mid s)$ và $(R_{t+1},S_{t+1})\sim p(\cdot,\cdot\mid s,A_t)$; $p$ và $r$ chỉ dùng trong lập luận, không là đầu vào của cập nhật.

**Phạm vi.** Mệnh đề nói về kỳ vọng của một gia số; nó không chứng minh hội tụ và không so sánh phương sai của hai dạng cập nhật.
:::

::: proof Chứng minh Mệnh đề 06.25
**Bước 1 (kỳ vọng của $\rho_tY_t$).** Điều kiện hóa theo $A_t=a$ rồi lấy trung bình theo $b$:

$$
\begin{aligned}
\mathbb E_b[\rho_tY_t\mid\mathcal F_t]
&=\sum_{a:\,b(a\mid s)>0}b(a\mid s)\,\frac{\pi(a\mid s)}{b(a\mid s)}\,\mathbb E[Y_t\mid\mathcal F_t,A_t=a] &&\text{(1)}\\
&=\sum_{a}\pi(a\mid s)\Big[r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)V_t(s')\Big] &&\text{(2)}\\
&=(T_\pi V_t)(s) &&\text{(3)}.
\end{aligned}
$$

Căn cứ của từng dòng: (1) luật kỳ vọng lặp theo $A_t$; (2) điều kiện hỗ trợ, vì các hành động bị bỏ khỏi tổng do $b(a\mid s)=0$ cũng có $\pi(a\mid s)=0$, cùng định nghĩa của $r$ và $p$; (3) định nghĩa của $T_\pi$ (Nhận xét 06.5).

**Bước 2 (trừ giá trị cũ).** Vì $V_t(s)$ đã biết khi điều kiện hóa theo $\mathcal F_t$, trừ nó khỏi Bước 1 cho kết luận. Theo cùng lập luận, $\mathbb E_b[\rho_t\mid\mathcal F_t]=\sum_{a:\,b(a\mid s)>0}\pi(a\mid s)=1$, nên dạng nhân tỉ số vào toàn bộ sai lệch có cùng kỳ vọng. $\square$
:::

Kỳ vọng vừa tính là phần dư Bellman (Bellman residual) của bảng hiện tại. Mục tiêu $\rho_tY_t$ có kỳ vọng có điều kiện $(T_\pi V_t)(s)$, còn $v_\pi(s)=(T_\pi v_\pi)(s)$ (Nhận xét 06.5(c)), nên độ chệch của mục tiêu so với $v_\pi(s)$ là

$$
\begin{aligned}
&(T_\pi V_t)(s)-v_\pi(s)\\
&=\gamma\sum_a\pi(a\mid s)\sum_{s'}p(s'\mid s,a)\\
&\qquad\times\big[V_t(s')-v_\pi(s')\big],
\end{aligned}
$$

khác $0$ chỉ khi bảng sai ở các trạng thái kế tiếp của $s$.

### 6.2 Sai số khi đánh giá một chính sách cố định

Cố định chính sách $\pi$ và phân phối trạng thái đầu $d_0$; đại lượng cần đánh giá là $J_{d_0}(\pi)=\mathbb E_{S_0\sim d_0,\pi}[G_0]$, và khi $d_0$ tập trung tại $s$ thì $J_{d_0}(\pi)=v_\pi(s)$. Với $n$ lượt độc lập, mỗi lượt cho lợi tức $G^{(i)}$, ước lượng Monte Carlo là $\widehat J_n=\tfrac1n\sum_{i=1}^nG^{(i)}$.

::: proposition Mệnh đề 06.26 (Chặn Hoeffding cho đánh giá một chính sách cố định)
**Giả thiết.** Số lượt $n\ge1$ được cố định trước khi lấy dữ liệu. Các lượt độc lập, cùng bắt đầu theo $d_0$, cùng thực hiện $\pi$, và được quan sát hoàn chỉnh. Có các số hữu hạn $L<U$ với $L\le G^{(i)}\le U$ hầu chắc chắn; đặt $B=U-L$.

**Kết luận.** Với mọi $\eta>0$,

$$
\Pr\Big\{\big|\widehat J_n-J_{d_0}(\pi)\big|>\eta\Big\}\le2\exp\Big(-\frac{2n\eta^2}{B^2}\Big),
$$

và do đó, với mọi mức $\beta\in(0,1)$,

$$
\Pr\Big\{\big|\widehat J_n-J_{d_0}(\pi)\big|\le B\sqrt{\tfrac{\ln(2/\beta)}{2n}}\Big\}\ge1-\beta .
$$

**Điều kiện áp dụng.** Chặn dùng khoảng chứa lợi tức, không chỉ chặn của phần thưởng.

**Phạm vi.** Chặn chỉ cho một chính sách cố định và một $n$ cố định trước; nó không áp dụng cho bảng $Q$ học thích nghi hay cho thời điểm dừng chọn theo dữ liệu. Chứng minh là áp dụng trực tiếp bất đẳng thức Hoeffding (1963, Định lý 2, tr. 16).
:::

Nghĩa là, với $\beta=0{,}05$, nếu lặp lại việc đánh giá $\pi$ bằng $n$ lượt mới nhiều lần, thì trong $100$ lần đánh giá, có khoảng $95$ lần trở lên cho $\widehat J_n$ lệch khỏi $J_{d_0}(\pi)$ không quá $B\sqrt{\ln40/(2n)}$; bán kính này giảm theo $1/\sqrt n$.

Ý tưởng chứng minh: bất đẳng thức Hoeffding cho tổng $n$ biến độc lập, mỗi biến nằm trong đoạn độ rộng $B$, chặn xác suất tổng lệch khỏi kỳ vọng quá $n\eta$ ở mỗi phía bởi $\exp(-2n\eta^2/B^2)$; cộng hai phía rồi giải $2\exp(-2n\eta^2/B^2)=\beta$ theo $\eta$ được kết luận thứ hai.

::: remark Nhận xét 06.27 (Độ rộng của lợi tức và trường hợp $\gamma=1$)
Với $0\le\gamma<1$, độ rộng $B$ suy từ chặn phần thưởng qua chuỗi hình học: nếu $0\le R\le R_{\max}$ thì $G\in[0,R_{\max}/(1-\gamma)]$ và $B=R_{\max}/(1-\gamma)$; nếu $|R|\le R_{\max}$ thì $B=2R_{\max}/(1-\gamma)$.

Ví dụ: phần thưởng trong $[0,1]$ và $\gamma=0{,}9$ cho $B=10$. Muốn bán kính không vượt $\eta=1$ với $\beta=0{,}05$, cần $n\ge\tfrac{B^2}{2\eta^2}\ln\tfrac2\beta=50\ln40\approx184{,}4$, tức $n\ge185$ lượt.

Với $\gamma=1$, công thức chia cho $1-\gamma$ không dùng được. Nếu mọi lượt dài không quá $H_0$ bước và $|R|\le R_{\max}$, có thể dùng $G\in[-H_0R_{\max},H_0R_{\max}]$; nếu chỉ biết lượt kết thúc với xác suất $1$ thì chưa có độ rộng hữu hạn. Vì thế chặn Hoeffding không áp dụng cho dãy năm ô với $\gamma=1$ mà không thêm giả thiết.
:::

**Trong thực hành.** Thay cho chặn của Mệnh đề 06.26, notebook báo trung bình kèm sai số chuẩn (standard error) $\mathrm{sd}/\sqrt n$ với $n=100$ lượt và khoảng $\pm1{,}96$ sai số chuẩn cho hiệu ghép cặp (paired difference), tức một xấp xỉ chuẩn (normal approximation) (notebook, phần 3). Chặn Hoeffding đúng với mọi $n$ nhưng cần biết trước độ rộng $B$, mà notebook không nêu khoảng biết trước nào cho tổng thưởng của một lượt LunarLander. Xấp xỉ chuẩn không cần $B$ nhưng chỉ gần đúng.

Tỉ số lấy mẫu quan trọng (Định nghĩa 06.24) cho gia số TD(0) khác chính sách đúng kỳ vọng $(T_\pi V_t)(s)-V_t(s)$ (Mệnh đề 06.25), và chặn Hoeffding (Mệnh đề 06.26) cho số lượt cần khi đánh giá một chính sách cố định.

<!-- note-topic-id: lec-06-topic-09 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 06.1 (Sarsa và Q-learning trên LunarLander)
**Bài toán và môi trường.** Môi trường `LunarLander-v3` của Gymnasium, hành động rời rạc, không gió. Quan sát gồm $8$ thành phần: sáu biến liên tục (tọa độ ngang và dọc, hai thành phần vận tốc, góc nghiêng, vận tốc góc) và hai cờ chân chạm đất. Bốn hành động là không bật động cơ, bật động cơ định hướng trái, bật động cơ chính, bật động cơ định hướng phải. Lượt kết thúc với phần thưởng $-100$ khi thân tàu chạm đất hoặc ra khỏi khung theo phương ngang ($\lvert x\rvert\ge1$), $+100$ khi tàu nằm yên, và bị cắt ngắn ở bước $1000$. Mọi số liệu dưới đây là của một lần chạy đã nhúng trong notebook thực hành Bài 06.

**Mô hình hóa.** Mỗi biến liên tục được chia thành ba khoảng và số chân chạm đất nhận ba giá trị, nên tập ô là $\mathcal S$ với $3^6\cdot3=2187$ phần tử; $\mathcal A(s)=\{0,1,2,3\}$ và $M=8748$ (notebook, phần 4). Trong tình huống này, $\gamma=0{,}99$, $Q_0=0$, chính sách hành vi là chính sách $\varepsilon_k$-tham lam với $\varepsilon_k$ giảm tuyến tính từ $1$ về $0{,}05$ trong $1500$ lượt rồi giữ nguyên, bước học theo cặp là $\alpha_n=\max(0{,}05,\ n^{-0{,}6})$, và ngân sách là $K=3000$ lượt huấn luyện. Sarsa là Thuật toán 06.12, Q-learning là Thuật toán 06.16; trạng thái lúc cắt ngắn được xử lý như trạng thái chưa kết thúc (Nhận xét 06.13).

**Kiểm giả thiết của Định lý 06.21 và 06.22.**

- Hữu hạn và $\gamma<1$: thỏa, vì tập ô hữu hạn và $\gamma=0{,}99$.
- Tính Markov của mẫu: không thỏa. Một ô gộp vô số quan sát; hai quan sát trong cùng ô có thể dẫn tới phân phối ô kế tiếp khác nhau, nên không có $p(\cdot\mid s,a)$ chung cho ô.
- Robbins–Monro theo cặp (Định nghĩa 06.19): không thỏa. Khi $n$ lớn, $\alpha_n=0{,}05$, nên $\sum_n\alpha_n^2=\infty$.
- GLIE cho Sarsa (Định nghĩa 06.18): không thỏa. Khối xác suất trên một cực đại duy nhất dừng ở $1-0{,}05+0{,}05/4=0{,}9625$.
- Cập nhật vô hạn lần: không kiểm được với ngân sách hữu hạn. Sau $3000$ lượt, $10\%$ (Sarsa) và $15\%$ (Q-learning) số cặp trong các ô được ghé chưa từng được cập nhật (notebook, phần 10).

**Áp dụng và đánh giá.** Notebook chạy chính sách tham lam theo mỗi bảng cuối $100$ lượt trên tập hạt giống (seed) kiểm tra chưa dùng trước đó, cùng hai mốc: chính sách ngẫu nhiên đều và bộ điều khiển viết tay `heuristic` của Gymnasium (notebook, phần 8.2). Tổng thưởng trung bình, kèm sai số chuẩn:

| Chính sách | Tổng thưởng | Nằm yên | Rơi hoặc ra ngoài | Cắt ngắn |
|---|---:|---:|---:|---:|
| ngẫu nhiên | $-194{,}8\pm12{,}3$ | $0\%$ | $99\%$ | $1\%$ |
| heuristic | $236{,}9\pm10{,}1$ | $90\%$ | $6\%$ | $4\%$ |
| Sarsa, tham lam | $26{,}2\pm14{,}0$ | $38\%$ | $18\%$ | $44\%$ |
| Q-learning, tham lam | $-6{,}6\pm17{,}2$ | $37\%$ | $61\%$ | $2\%$ |

Vì mọi chính sách dùng cùng dãy hạt giống, lượt thứ $i$ của hai chính sách tạo một cặp, và notebook báo hiệu ghép cặp kèm nửa độ rộng khoảng tin cậy (confidence interval) $95\%$ ($1{,}96$ sai số chuẩn):

- Sarsa trừ ngẫu nhiên: $221{,}0\pm39{,}0$;
- Q-learning trừ ngẫu nhiên: $188{,}2\pm40{,}9$;
- heuristic trừ Sarsa: $210{,}7\pm34{,}9$;
- heuristic trừ Q-learning: $243{,}5\pm38{,}8$;
- Sarsa trừ Q-learning: $32{,}8\pm46{,}2$.

**Diễn giải.** Bốn khoảng đầu không chứa $0$: cả hai bảng đã học được hành vi tốt hơn chọn ngẫu nhiên, và cả hai còn kém bộ điều khiển viết tay. Khoảng của hiệu Sarsa trừ Q-learning là $[-13{,}4;\ 79{,}0]$, chứa $0$, nên $100$ lượt chưa đủ để xếp hạng hai thuật toán. Ba cột cuối cho thấy hai kiểu thất bại: Sarsa có nhiều lượt bị cắt ngắn, Q-learning có nhiều lượt rơi.

Notebook cũng so giá trị mà bảng gán cho trạng thái đầu, trung bình của $\max_aQ(S_0,a)$, với trung bình lợi tức chiết khấu $G_0$ thật sự nhận được trên $100$ lượt: hiệu là $21{,}5\pm7{,}2$ với Q-learning và $-13{,}0\pm2{,}1$ với Sarsa (phần 9.2). Khoảng $\pm1{,}96$ sai số chuẩn của cả hai hiệu đều không chứa $0$, nên bảng Q-learning đánh giá cao còn bảng Sarsa đánh giá thấp lợi tức của chính sách tham lam đang chạy; với Q-learning, phép cực đại trên các ước lượng có nhiễu là một nguồn đã biết của đánh giá cao (overestimation) (Sutton và Barto, 2018, §6.7).

**Giới hạn.** Mỗi thiết lập chỉ được huấn luyện một lần. Năm lần huấn luyện sơ bộ, với hạt giống huấn luyện và hạt giống đánh giá khác, cho Sarsa trung bình $109{,}6$ (từ $66{,}1$ đến $136{,}1$), và kết quả $26{,}2$ ở trên thấp hơn mọi lần sơ bộ (phần 8.2).

Notebook còn thử một cách chia ô khác, dựng từ các đại lượng mà bộ điều khiển heuristic tính từ quan sát, cùng lịch thăm dò giảm về $\varepsilon_{\min}=0{,}01$ trong $2000$ lượt; trên cùng tập kiểm tra, Sarsa đạt $202{,}8\pm2{,}3$ và Q-learning đạt $235{,}5\pm4{,}3$, nhưng cả ba giả thiết vẫn bị vi phạm (phần 11).

**Kiểm tra lại.** $3^6\cdot3=2187$ và $2187\cdot4=8748$; $1-0{,}05+0{,}05/4=0{,}9625$. Các hiệu ghép cặp khớp hiệu các trung bình trong bảng: $26{,}2-(-194{,}8)=221{,}0$, $-6{,}6-(-194{,}8)=188{,}2$, $236{,}9-26{,}2=210{,}7$, $236{,}9-(-6{,}6)=243{,}5$, $26{,}2-(-6{,}6)=32{,}8$; và $32{,}8\mp46{,}2$ cho hai đầu mút $-13{,}4$ và $79{,}0$.

**Dẫn ngược.** Mô hình hóa: Định nghĩa 06.1, 06.3; thuật toán: Thuật toán 06.12, 06.16, Nhận xét 06.13; kiểm giả thiết: Định nghĩa 06.18, 06.19, Định lý 06.21, 06.22; đánh giá: hiệu ghép cặp thay cho Mệnh đề 06.26.
:::

::: application Tình huống 06.2 (Vòng B–C trên dãy năm ô: giả thiết không thỏa)
**Bài toán và môi trường.** Dãy năm ô của Ví dụ 06.1, $\gamma=1$, bảng khởi tạo nghiêng phải: B $(0,1)$, C $(1,0)$, D $(0,1)$. Hành vi là chính sách tham lam theo bảng hiện tại ($\varepsilon=0$), trừ hành động đầu tiên tại D, được chọn là trái bởi một bước thăm dò. Bước học hằng $\alpha=0{,}8$.

**Mô hình hóa.** Chính sách tham lam theo bảng khởi tạo là $\pi_I$ của Nhận xét 06.2: phải tại B, trái tại C, phải tại D. Sau bước D→C, nếu bảng không đổi thì $\pi_I$ đi C→B→C→B→… mãi mãi, mỗi bước nhận $-1$.

**Kiểm giả thiết.**

- Thuật toán 06.9 cần $\varepsilon_k>0$ và mọi lượt kết thúc hầu chắc chắn: cả hai không thỏa, vì hành vi dùng $\varepsilon=0$ và dưới $\pi_I$ lượt bắt đầu bằng D→C không kết thúc.
- Định lý 06.21 và 06.22 cần $\gamma<1$, độ phủ, Robbins–Monro: cả ba không thỏa ($\gamma=1$; $\varepsilon=0$ nên nhiều cặp không được thử; bước học hằng).

**Áp dụng Thuật toán 06.9.** Bảng không đổi trong lượt, nên lượt D→C→B→C→B→… không kết thúc và không có lợi tức hoàn chỉnh nào. Nếu chỉ ghi ba bước đầu, lượt bị cắt tại C sau D→C→B→C, một trạng thái chưa kết thúc. Trong cả hai trường hợp, Monte Carlo không cập nhật được ô nào.

**Áp dụng Thuật toán 06.12.** Sarsa cập nhật sau mỗi chuyển. Theo bước 2 của thuật toán, $A'$ được chọn tham lam từ bảng ngay trước cập nhật hiện tại:

| Bước | Chuyển $(S,A,R,S')$ | $A'$ tham lam | $Y$ | Giá trị mới |
|---:|---|---|---:|---|
| 0 | $(\mathrm D,0,-1,\mathrm C)$ | $0$, vì hàng C là $(1;0)$ | $-1+1=0$ | $Q(\mathrm D,0)=0$ |
| 1 | $(\mathrm C,0,-1,\mathrm B)$ | $1$, vì hàng B là $(0;1)$ | $-1+1=0$ | $Q(\mathrm C,0)=1+0{,}8(0-1)=0{,}2$ |
| 2 | $(\mathrm B,1,-1,\mathrm C)$ | $0$, vì hàng C là $(0{,}2;0)$ | $-1+0{,}2=-0{,}8$ | $Q(\mathrm B,1)=1+0{,}8(-1{,}8)=-0{,}44$ |
| 3 | $(\mathrm C,0,-1,\mathrm B)$ | $0$, vì hàng B là $(0;-0{,}44)$ | $-1+0=-1$ | $Q(\mathrm C,0)=0{,}2+0{,}8(-1{,}2)=-0{,}76$ |
| 4 | $(\mathrm B,0,1000,\mathrm A)$ | không có, A kết thúc | $1000$ | $Q(\mathrm B,0)=0+0{,}8\cdot1000=800$ |

Ở bước 2, phần thưởng âm của vòng làm $Q(\mathrm B,1)$ giảm xuống dưới $Q(\mathrm B,0)$, nên ở bước 3 hành vi tham lam tại B đổi sang trái, và lượt kết thúc tại A sau năm bước. Với giới hạn ba bước, Sarsa vẫn thực hiện được ba cập nhật đầu. Q-learning cho đúng các cập nhật trên: vì $S'\ne S$ ở mọi chuyển, cập nhật hiện tại không đổi hàng $S'$, nên $A'$ tham lam là cực đại của đúng hàng mà Q-learning dùng.

**Diễn giải.** Monte Carlo không học được gì từ một lượt không kết thúc, còn các phương pháp một bước học ngay trong lượt và trong trường hợp này phá được vòng: hàng B đổi cực đại sau cập nhật thứ ba và lượt kết thúc ở chuyển thứ năm.

**Kiểm tra lại.** Ở bước 2, $\delta=-0{,}8-1=-1{,}8$ và $1+0{,}8\cdot(-1{,}8)=-0{,}44$; ở bước 3, $\delta=-1-0{,}2=-1{,}2$ và $0{,}2+0{,}8\cdot(-1{,}2)=-0{,}76$.

**Giới hạn.** Cập nhật đầu tại $(\mathrm B,1)$ cho $Q(\mathrm B,1)=0{,}84\,Q_0(\mathrm B,1)-1{,}28$. Với $Q_0(\mathrm B,1)>32/21$, giá trị này chưa xuống dưới $Q(\mathrm B,0)=0$, nên vòng B–C kéo dài thêm; chẳng hạn với $Q_0(\mathrm B,1)=10$, lượt kết thúc ở chuyển thứ $17$.

**Dẫn ngược.** Tình huống dùng Nhận xét 06.2 cho vòng B–C, giả thiết của Thuật toán 06.9, Định nghĩa 06.11 cho mục tiêu Sarsa, và các giả thiết của Định lý 06.21–06.22.
:::

**Liên hệ với các bài sau.**

- **Bài 07.** Bảng $Q$ được thay bằng một hàm có tham số dùng chung giữa các trạng thái, vì bảng không tổng quát hóa giữa các ô gần nhau; hai bài thực hành của Bài 07 (LunarLander, Flappy Bird) dùng lại mục tiêu Sarsa và Q-learning với xấp xỉ tuyến tính.
- **Bài 08.** Deep Q-learning giữ mục tiêu cực đại của Định nghĩa 06.15 nhưng thay bảng bằng mạng nơ-ron, thêm bộ nhớ phát lại (replay memory, experience replay) và mạng mục tiêu (target network).
- **Bài 09.** Double DQN xử lý hiện tượng đánh giá cao do phép cực đại trên các ước lượng có nhiễu trong mục tiêu của Định nghĩa 06.15.

<!-- note-topic-id: lec-06-topic-07 -->
## Tóm tắt chương

Câu hỏi xuất phát là chọn hướng tại ô D của dãy năm ô khi không có mô hình: đi phải cho $10$, đi trái liên tục cho $998$, nhưng tác tử chỉ thấy mẫu. Chúng ta thay bảng $V$ của Bài 05 bằng bảng $Q$ theo cặp (Định nghĩa 06.1) và giữ thăm dò bằng chính sách $\varepsilon$-tham lam (Định nghĩa 06.3), với bảo đảm rằng bước $\varepsilon$-tham lam theo $q_\pi$ chính xác không làm giảm giá trị trong lớp $\varepsilon$-mềm (Mệnh đề 06.6). Ba thuật toán dùng chung khung $Q\leftarrow Q+\alpha[Y-Q]$ và chỉ khác mục tiêu $Y$: lợi tức hoàn chỉnh (Thuật toán 06.9), giá trị của hành động kế tiếp đã chọn (Thuật toán 06.12), cực đại của hàng kế tiếp (Thuật toán 06.16). Trên dữ liệu của chương, Monte Carlo xuất phát từ bảng khởi tạo nghiêng trái và sau lượt D–C–B–A xếp trái ($998$) trên phải ($0$) tại D (Ví dụ 06.8); Sarsa và Q-learning xuất phát từ bảng khởi tạo nghiêng phải và sau năm mẫu đều xếp phải ($8{,}2$) trên trái (lần lượt $-1{,}28$ và $-0{,}64$), vì phần thưởng $1000$ chưa truyền về D (Ví dụ 06.12). Hai kết quả dùng hai khởi tạo và hai bộ dữ liệu khác nhau, nên không xếp hạng được các thuật toán. Với đủ giả thiết, Q-learning hội tụ tới $q_*$ (Định lý 06.21) và Sarsa hội tụ khi thêm GLIE (Định lý 06.22); với điều khiển Monte Carlo, các lợi tức trong một ô đến từ nhiều chính sách $\pi_k$, nên trung bình mẫu và Mệnh đề 06.6 không ghép thành chứng minh hội tụ tới $q_*$ (Nhận xét 06.23). Trên LunarLander các giả thiết ấy không thỏa (Tình huống 06.1). Giới hạn còn lại là bảng cần một ô cho mỗi cặp và không tổng quát hóa giữa các ô gần nhau.

**Định nghĩa và kết quả theo mục.**

- Mục 1: bảng $Q$ có một ô cho mỗi cặp hợp lệ và $Q=0$ tại trạng thái kết thúc (Định nghĩa 06.1); với $\gamma=1$, vòng B–C cho một chính sách có giá trị không hữu hạn (Nhận xét 06.2); $\pi_\varepsilon(a\mid s)=\varepsilon/m(s)+(1-\varepsilon)\mathbf 1\{a\in\mathcal G_Q(s)\}/\lvert\mathcal G_Q(s)\rvert$ (Định nghĩa 06.3), và mọi chính sách $\varepsilon$-tham lam đều $\varepsilon$-mềm, tức $\pi(a\mid s)\ge\varepsilon/m(s)$ (Định nghĩa 06.4); $T_\pi$ đơn điệu, co hệ số $\gamma$ khi $\gamma<1$ và có điểm bất động duy nhất $v_\pi$ (Nhận xét 06.5); khi $\gamma<1$, nếu $\pi$ là $\varepsilon$-mềm và $\pi'$ là $\varepsilon$-tham lam theo $q_\pi$ chính xác với cùng $\varepsilon$ thì $v_{\pi'}\ge v_\pi$ (Mệnh đề 06.6); theo một bảng ước lượng, bước ấy không còn bảo đảm này, còn lịch $\varepsilon_k$ giảm dần vẫn giữ giả thiết mềm với $\varepsilon=\varepsilon_{k+1}$ (Nhận xét 06.7).
- Mục 2: mỗi cặp nhận nhiều nhất một lợi tức mỗi lượt, $G_{f(s,a)}$, và $N(s,a)$ chỉ đếm lợi tức đã dùng (Định nghĩa 06.8); điều khiển Monte Carlo cập nhật $Q(s,a)\leftarrow Q(s,a)+[G_{f(s,a)}-Q(s,a)]/N(s,a)$ sau mỗi lượt, lập chính sách $\varepsilon_k$-tham lam mới và dừng sau $K$ lượt (Thuật toán 06.9); chỉ lượt kết thúc mới cho lợi tức, còn hết ngân sách không nói gì về độ chính xác của bảng (Nhận xét 06.10).
- Mục 3: mục tiêu Sarsa là $R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$, bằng $R_{t+1}$ khi $S_{t+1}$ kết thúc (Định nghĩa 06.11); Sarsa chọn $A'$ từ bảng chưa cập nhật, thực hiện đúng $A'$ ở bước sau và dừng sau $H$ cập nhật (Thuật toán 06.12); chỉ kết thúc lượt mới đặt $Y_t=R_{t+1}$, còn ở bước cắt ngắn và khi hết ngân sách mục tiêu vẫn chứa $\gamma Q_t(S_{t+1},A_{t+1})$ (Nhận xét 06.13).
- Mục 4: phương pháp học theo chính sách khi $b=\pi$ và khác chính sách khi $b$ có thể khác $\pi$ (Định nghĩa 06.14); mục tiêu Q-learning là $R_{t+1}+\gamma\max_aQ_t(S_{t+1},a)$ (Định nghĩa 06.15); Q-learning chọn hành động sau cập nhật và trả chính sách tham lam theo bảng (Thuật toán 06.16); Q-learning một bước không cần tỉ số lấy mẫu quan trọng nhưng cần hành vi phủ mọi cặp và mẫu sinh từ chính môi trường (Nhận xét 06.17).
- Mục 5: GLIE đòi mọi cặp được thực hiện vô hạn lần và khối xác suất trên tập cực đại tiến tới $1$ (Định nghĩa 06.18); Robbins–Monro theo cặp đòi $\sum_n\alpha_n(s,a)=\infty$ và $\sum_n\alpha_n(s,a)^2<\infty$ với từng cặp (Định nghĩa 06.19); hai định lý dùng chung MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, $Q_0$ hữu hạn, mẫu sinh từ chính MDP và bước học chọn trước mẫu (Nhận xét 06.20); thêm độ phủ và Robbins–Monro theo cặp, Q-learning hội tụ hầu chắc chắn tới $q_*$ (Định lý 06.21), và Sarsa cũng vậy khi thêm GLIE (Định lý 06.22); các lợi tức trong một ô của điều khiển Monte Carlo đến từ nhiều chính sách $\pi_k$, nên trung bình mẫu và Mệnh đề 06.6 không ghép thành chứng minh hội tụ tới $q_*$ (Nhận xét 06.23).
- Mục 6 (đọc thêm): tỉ số $\rho_t=\pi(A_t\mid S_t)/b(A_t\mid S_t)$ dùng được khi $\pi(a\mid s)>0$ kéo theo $b(a\mid s)>0$ (Định nghĩa 06.24); khi đó gia số TD(0) khác chính sách có kỳ vọng có điều kiện $(T_\pi V_t)(s)-V_t(s)$ (Mệnh đề 06.25); với $n$ lượt độc lập và lợi tức trong một đoạn độ rộng $B$, sai số của trung bình không vượt $B\sqrt{\ln(2/\beta)/(2n)}$ với xác suất ít nhất $1-\beta$ (Mệnh đề 06.26); khi $0\le\gamma<1$ và $0\le R\le R_{\max}$ thì $B=R_{\max}/(1-\gamma)$, còn khi $\gamma=1$ cần một chặn độ dài lượt (Nhận xét 06.27).
- Tình huống áp dụng: trên LunarLander, cả hai bảng tốt hơn chính sách ngẫu nhiên nhưng $100$ lượt kiểm tra chưa xếp hạng được Sarsa với Q-learning, và ba giả thiết của Định lý 06.21–06.22 bị vi phạm (Tình huống 06.1); trên vòng B–C với $\gamma=1$, Monte Carlo không cập nhật được, còn Sarsa phá vòng sau ba cập nhật (Tình huống 06.2).

**Công thức cần nhớ.**

Chính sách $\varepsilon$-tham lam theo $Q$:

$$
\pi_\varepsilon(a\mid s)=\frac{\varepsilon}{m(s)}+(1-\varepsilon)\,\frac{\mathbf 1\{a\in\mathcal G_Q(s)\}}{|\mathcal G_Q(s)|}.
$$

Khung cập nhật chung và ba mục tiêu; với Monte Carlo, $(s,a)$ là cặp được cập nhật sau lượt, và với hai mục tiêu một bước, khi $S_{t+1}$ kết thúc thì $Y_t=R_{t+1}$:

$$
\begin{aligned}
Q(S_t,A_t)&\leftarrow Q(S_t,A_t)+\alpha_t\big[Y_t-Q(S_t,A_t)\big],\\
Y^{\text{MC}}&=G_{f(s,a)},\quad \alpha=1/N(s,a)\ \text{sau khi tăng } N(s,a),\\
Y_t^{\text{Sarsa}}&=R_{t+1}+\gamma\,Q_t(S_{t+1},A_{t+1}),\\
Y_t^{\text{Q}}&=R_{t+1}+\gamma\max_{a}Q_t(S_{t+1},a).
\end{aligned}
$$

Điều kiện Robbins–Monro theo cặp:

$$
\begin{aligned}
\sum_{n=1}^{\infty}\alpha_n(s,a)&=\infty,\\
\sum_{n=1}^{\infty}\alpha_n(s,a)^2&<\infty .
\end{aligned}
$$

**Giả thiết hay bị bỏ quên.**

- Mệnh đề 06.6 cần $q_\pi$ chính xác và cùng $\varepsilon$ cho hai chính sách; một bảng ước lượng từ mẫu không đủ.
- Các định lý hội tụ cần $\gamma<1$ và bước học Robbins–Monro theo cặp; dãy năm ô với $\gamma=1$ và bước học hằng $0{,}8$ vi phạm cả hai (Nhận xét 06.20).
- Robbins–Monro phải đúng theo từng cặp, không chỉ theo thời gian toàn cục (Ví dụ 06.15).
- GLIE chỉ cần cho Sarsa; $\varepsilon_k\to0$ chưa đủ cho GLIE nếu thăm dò tắt quá nhanh (Ví dụ 06.14).
- Kết thúc lượt, cắt ngắn và hết ngân sách là ba sự kiện khác nhau; chỉ kết thúc lượt mới đặt $Y=R$.
- Q-learning không cần tỉ số lấy mẫu quan trọng nhưng vẫn cần hành vi phủ mọi cặp và mẫu sinh từ chính môi trường.
- Các định lý cần mẫu có tính Markov; một lưới ô gộp quan sát liên tục vi phạm giả thiết này.

## Bài tập củng cố

### Mức nhận biết

::: exercise Bài tập 06.7 (Phân loại ba thuật toán)
Với điều khiển Monte Carlo (Thuật toán 06.9), Sarsa (Thuật toán 06.12) và Q-learning (Thuật toán 06.16):

1. Nêu chính sách hành vi $b$, chính sách đích $\pi$, và kết luận phương pháp học theo hay khác chính sách.
2. Nêu đơn vị dữ liệu cần có trước một cập nhật và thời điểm cập nhật.
3. Một tác tử chạy Q-learning trên dữ liệu do chính sách đều ngẫu nhiên sinh ra. Xác định phương pháp này theo hay khác chính sách, và có cần tỉ số lấy mẫu quan trọng không.
:::

::: hint
Đối chiếu Định nghĩa 06.14: chính sách nào chọn hành động được thực hiện, chính sách nào quyết định phần tiếp nối trong mục tiêu. Với câu 3, đọc lại Nhận xét 06.17.
:::

::: solution
**Câu 1.**

- Monte Carlo: $b=\pi=\pi_k$ trong lượt $k$; theo chính sách.
- Sarsa: $A_{t+1}$ trong mục tiêu lấy từ chính sách đang sinh dữ liệu, nên $b=\pi$; theo chính sách.
- Q-learning: $b$ là chính sách thăm dò, $\pi$ là chính sách tham lam theo bảng; khác chính sách.

**Câu 2.** Monte Carlo cần một lượt hoàn chỉnh và cập nhật sau lượt. Sarsa cần bộ năm $(S,A,R,S',A')$ và cập nhật sau mỗi chuyển, khi đã chọn $A'$. Q-learning cần bộ bốn $(S,A,R,S')$ và cập nhật sau mỗi chuyển.

**Câu 3.** Khác chính sách, vì $b$ là chính sách đều còn $\pi$ là chính sách tham lam theo bảng. Không cần tỉ số lấy mẫu quan trọng: $A_t$ nằm trong điều kiện của ô được cập nhật và phần tiếp nối được tính bằng cực đại trên bảng.

**Kiểm tra lại.** Lỗi thường gặp: coi Q-learning là theo chính sách vì $b$ được lập từ chính bảng $Q$; mục tiêu vẫn đánh giá chính sách tham lam, khác $b$.
:::

::: exercise Bài tập 06.8 (Đúng hay sai về $q_\pi$, $Q$ và $q_*$)
Xác định mỗi khẳng định đúng hay sai và giải thích bằng một ví dụ của chương.

1. Trên dãy năm ô, giá trị khởi tạo $Q_0(\mathrm D,1)=1$ của bảng nghiêng phải bằng $q_\pi(\mathrm D,1)$ của một chính sách $\pi$ nào đó.
2. $q_\pi(s,a)$ chỉ phụ thuộc $\pi$ qua các hành động sau hành động đầu.
3. Với mọi chính sách $\pi$, $v_\pi(s)=\max_aq_\pi(s,a)$.
4. Trong MDP hữu hạn có phần thưởng bị chặn và $\gamma<1$, với mọi chính sách dừng $\pi$ và mọi cặp, $q_*(s,a)\ge q_\pi(s,a)$.
5. Nếu một cập nhật Sarsa có $\delta_t=0$ thì $Q(S_t,A_t)=q_\pi(S_t,A_t)$, với $\pi$ là chính sách $\varepsilon$-tham lam đang sinh dữ liệu.
:::

::: hint
Dùng Ví dụ 06.2, 06.3, 06.5 và mẫu 1 của Ví dụ 06.9.
:::

::: solution
**Câu 1. Sai.** Hành động $1$ tại D luôn kết thúc lượt với phần thưởng $10$, nên $q_\pi(\mathrm D,1)=10\ne1$ với mọi $\pi$.

**Câu 2. Đúng.** Điều kiện $A_t=a$ cố định hành động đầu; $\pi$ chỉ quyết định $A_{t+1},A_{t+2},\dots$ (Ví dụ 06.3).

**Câu 3. Sai.** Trong Ví dụ 06.5, $\pi=(0{,}1;\,0{,}1;\,0{,}8)$ có $v_\pi(s)=-0{,}2$ còn $\max_aq_\pi(s,a)=3$. Đẳng thức chỉ đúng khi $\pi$ dồn toàn bộ xác suất vào các hành động cực đại của $q_\pi$.

**Câu 4. Đúng** trong điều kiện đã nêu: $v_\pi\le v_*$ nên $q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_\pi(s')]\le q_*(s,a)$ (Định nghĩa 04.19, Mệnh đề 03.22). Với dãy năm ô và $\gamma=1$, $q_*$ chưa được định nghĩa.

**Câu 5. Sai.** Ở mẫu 1 của Ví dụ 06.9, $\delta=0$ và $Q(\mathrm D,0)$ giữ giá trị $0$. Nếu dữ liệu sinh bởi chính sách $1/4$-tham lam $\pi$ theo bảng khởi tạo nghiêng phải (Ví dụ 06.4), giải $v_\pi=T_\pi v_\pi$ trên B, C, D được $v_\pi(\mathrm C)=3478/7$, nên $q_\pi(\mathrm D,0)=-1+v_\pi(\mathrm C)=3471/7\approx495{,}9\ne0$. Sai lệch bằng $0$ chỉ nói mục tiêu, vốn chứa ước lượng $Q(\mathrm C,0)=1$, trùng giá trị cũ.

**Kiểm tra lại.** Câu 1 và câu 5 cùng chỉ ra một ô của bảng khác giá trị thật: $Q_0(\mathrm D,1)=1\ne10$ và $Q(\mathrm D,0)=0\ne3471/7$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 06.9 (Lịch bước học có sàn của bài thực hành)
Bài thực hành dùng lịch bước học theo cặp $\alpha_n=\max(0{,}05,\ n^{-0{,}6})$, $n=1,2,\dots$ Nhắc lại từ Bài tập 05.11 rằng $\alpha_n=n^{-p}$ thỏa điều kiện Robbins–Monro khi và chỉ khi $1/2<p\le1$.

1. Xác định số $n_0$ nhỏ nhất sao cho $\alpha_n=0{,}05$ với mọi $n\ge n_0$.
2. Chứng minh lịch không thỏa Định nghĩa 06.19, dù phần $n^{-0{,}6}$ thỏa.
:::

::: hint
Giải $n^{-0{,}6}\le0{,}05$. Với câu 2, xét tổng bình phương của các số hạng từ $n_0$ trở đi.
:::

::: solution
**Câu 1.** $n^{-0{,}6}\le0{,}05$ khi và chỉ khi $n\ge0{,}05^{-1/0{,}6}=20^{5/3}\approx147{,}4$, nên $n_0=148$.

**Câu 2.** Với mọi $n\ge148$, $\alpha_n^2=0{,}0025$, nên $\sum_n\alpha_n^2\ge\sum_{n\ge148}0{,}0025=\infty$, vi phạm tổng thứ hai. Phần $n^{-0{,}6}$ thỏa vì $p=0{,}6\in(1/2,1]$; chính sàn $0{,}05$ phá điều kiện.

**Kiểm tra lại.** $147^{-0{,}6}\approx0{,}0501>0{,}05$ và $148^{-0{,}6}\approx0{,}0499<0{,}05$.
:::

::: exercise Bài tập 06.10 (Hai lượt Q-learning trên dãy năm ô)
Trên dãy năm ô ($\gamma=1$), chạy Q-learning với bước học hằng $\alpha=1/2$ từ bảng khởi tạo nghiêng trái: B $(0,1)$, C $(1,0)$, D $(1,0)$, mỗi cặp theo thứ tự hành động $(0,1)$. Dữ liệu là hai lượt giống nhau, mỗi lượt gồm ba chuyển $(\mathrm D,0,-1,\mathrm C)$, $(\mathrm C,0,-1,\mathrm B)$, $(\mathrm B,0,1000,\mathrm A)$.

1. Tính mục tiêu và giá trị mới của từng cập nhật, và bảng sau mỗi lượt.
2. Tính cập nhật đầu tiên của lượt thứ ba (cùng chuyển $(\mathrm D,0,-1,\mathrm C)$).
3. So sánh với Monte Carlo lần ghé đầu tiên (Thuật toán 06.9) trên cùng hai lượt, với mọi bộ đếm ban đầu bằng $0$.
:::

::: hint
Mỗi mục tiêu dùng bảng ngay trước cập nhật đó. Với $\alpha=1/2$, giá trị mới là trung bình của giá trị cũ và mục tiêu.
:::

::: solution
**Câu 1, lượt 1.**

- $(\mathrm D,0)$: $Y=-1+\max(1,0)=0$; $Q(\mathrm D,0)=1+\tfrac12(0-1)=0{,}5$.
- $(\mathrm C,0)$: $Y=-1+\max(0,1)=0$; $Q(\mathrm C,0)=1+\tfrac12(0-1)=0{,}5$.
- $(\mathrm B,0)$: A kết thúc, $Y=1000$; $Q(\mathrm B,0)=0+\tfrac12\cdot1000=500$.

Bảng sau lượt 1: B $(500;\,1)$, C $(0{,}5;\,0)$, D $(0{,}5;\,0)$.

**Câu 1, lượt 2.**

- $(\mathrm D,0)$: $Y=-1+\max(0{,}5;\,0)=-0{,}5$; $Q(\mathrm D,0)=0{,}5+\tfrac12(-0{,}5-0{,}5)=0$.
- $(\mathrm C,0)$: $Y=-1+\max(500,1)=499$; $Q(\mathrm C,0)=0{,}5+\tfrac12(499-0{,}5)=249{,}75$.
- $(\mathrm B,0)$: $Y=1000$; $Q(\mathrm B,0)=500+\tfrac12(1000-500)=750$.

Bảng sau lượt 2: B $(750;\,1)$, C $(249{,}75;\,0)$, D $(0;\,0)$. Hàng D đồng hạng.

**Câu 2.** $Y=-1+\max(249{,}75;\,0)=248{,}75$; $Q(\mathrm D,0)=0+\tfrac12\cdot248{,}75=124{,}375$.

**Câu 3.** Monte Carlo cho ngay sau lượt 1 bảng B $(1000;1)$, C $(999;0)$, D $(998;0)$, và lượt 2 giữ nguyên các trung bình. Q-learning chuyển phần thưởng $1000$ lùi một ô mỗi lượt, nên sau hai lượt $Q(\mathrm D,0)$ còn bằng $0$; ở lượt 2 nó còn giảm, vì mục tiêu dùng $Q(\mathrm C,\cdot)$ vừa bị hạ.

**Kiểm tra lại.** $249{,}75=999/4$ và $124{,}375=995/8$.
:::

::: exercise Bài tập 06.11 (Kiểm Mệnh đề 06.6 bằng số)
Dùng môi trường một bước của Ví dụ 06.5: một trạng thái $s$, ba hành động kết thúc lượt với phần thưởng $3$, $3$, $-1$. Cho $\varepsilon=0{,}3$ và $\pi(\cdot\mid s)=(0{,}2;\,0{,}1;\,0{,}7)$.

1. Kiểm tra $\pi$ là $\varepsilon$-mềm và tính $v_\pi(s)$.
2. Tính các trọng số $w(\cdot\mid s)$ của Bước 2 trong chứng minh Mệnh đề 06.6 và kiểm đẳng thức $\sum_a\pi(a\mid s)q_\pi(s,a)=\tfrac{\varepsilon}{m}\sum_aq_\pi(s,a)+(1-\varepsilon)\sum_aw(a\mid s)q_\pi(s,a)$.
3. Tính chính sách $\varepsilon$-tham lam $\pi'$ theo $q_\pi$ và $v_{\pi'}(s)$.
4. Chỉ ra một chính sách không $0{,}3$-mềm có giá trị lớn hơn $v_{\pi'}(s)$, và giải thích vì sao điều này không mâu thuẫn với Mệnh đề 06.6.
:::

::: hint
Cận dưới của lớp mềm là $\varepsilon/m=0{,}1$. Với câu 4, xem phạm vi của Mệnh đề 06.6.
:::

::: solution
**Câu 1.** Ba xác suất $0{,}2$, $0{,}1$, $0{,}7$ đều không nhỏ hơn $0{,}1$. $v_\pi(s)=0{,}2\cdot3+0{,}1\cdot3+0{,}7\cdot(-1)=0{,}2$.

**Câu 2.** $w=\big(\tfrac{0{,}2-0{,}1}{0{,}7};\,\tfrac{0{,}1-0{,}1}{0{,}7};\,\tfrac{0{,}7-0{,}1}{0{,}7}\big)=\big(\tfrac17;\,0;\,\tfrac67\big)$, tổng bằng $1$. Vế phải là $0{,}1\cdot(3+3-1)+0{,}7\cdot\big(\tfrac37-\tfrac67\big)=0{,}5-0{,}3=0{,}2$, bằng $v_\pi(s)$.

**Câu 3.** Tập cực đại là $\{0,1\}$, nên $\pi'=(0{,}45;\,0{,}45;\,0{,}1)$ và $v_{\pi'}(s)=1{,}35+1{,}35-0{,}1=2{,}6\ge0{,}2$.

**Câu 4.** Chính sách tất định chọn hành động $0$ có giá trị $3>2{,}6$. Nó không $0{,}3$-mềm vì gán xác suất $0$ cho hai hành động. Mệnh đề 06.6 chỉ so $\pi'$ với $\pi$ trong lớp $\varepsilon$-mềm và không khẳng định $\pi'$ tốt hơn mọi chính sách; trong lớp $0{,}3$-mềm, giá trị lớn nhất là $2{,}6$.

**Kiểm tra lại.** $\sum_aw(a\mid s)q_\pi(s,a)=-\tfrac37\le\max_aq_\pi(s,a)=3$, đúng chiều của Bước 3.
:::

### Mức vận dụng

::: exercise Bài tập 06.12 (Chính sách $\varepsilon$-tham lam của tàu đổ bộ)
Trong bài thực hành LunarLander, mỗi ô có bốn hành động. Tại một ô, hàng của bảng là $Q(s,\cdot)=(5;\,1;\,1;\,1)$.

1. Xác định $\varepsilon$ để xác suất chọn hành động $0$ bằng $0{,}9$.
2. Thiết lập tinh chỉnh của notebook giữ $\varepsilon_{\min}=0{,}01$ (phần 11). Tính khối xác suất trên hành động $0$ và xác suất chọn mỗi hành động còn lại; kết luận điều kiện tham lam trong giới hạn của GLIE có thỏa không nếu $\varepsilon$ giữ mãi giá trị này.
3. Giả sử đổi lịch thăm dò và lịch bước học sao cho GLIE và Robbins–Monro theo cặp đều thỏa. Giải thích vì sao Định lý 06.22 vẫn không áp dụng cho bảng $2187$ ô của notebook.
:::

::: hint
Với một cực đại duy nhất, xác suất của hành động cực đại là $1-\varepsilon+\varepsilon/m$. Với câu 3, đọc lại phần kiểm giả thiết của Tình huống 06.1.
:::

::: solution
**Câu 1.** $\mathcal G_Q(s)=\{0\}$, nên $\pi_\varepsilon(0\mid s)=\varepsilon/4+1-\varepsilon=1-3\varepsilon/4$. Đặt bằng $0{,}9$ được $3\varepsilon/4=0{,}1$, tức $\varepsilon=0{,}4/3\approx0{,}133$.

**Câu 2.** Khối trên hành động $0$ là $1-0{,}01+0{,}01/4=0{,}9925$; mỗi hành động còn lại có xác suất $0{,}01/4=0{,}0025$. Nếu $\varepsilon$ giữ mãi $0{,}01$, khối xác suất không tiến tới $1$, nên điều kiện tham lam trong giới hạn không thỏa.

**Câu 3.** Định lý 06.22 cần mẫu sinh từ một MDP hữu hạn trên chính tập trạng thái của bảng. Mỗi ô của notebook gộp vô số quan sát liên tục, và phân phối của ô kế tiếp phụ thuộc vị trí thật bên trong ô, nên quá trình trên các ô không có tính Markov. Giả thiết nền này vẫn bị vi phạm dù lịch thăm dò và bước học đã đúng.

**Kiểm tra lại.** Với $\varepsilon=0{,}4/3$: $1-\tfrac34\cdot\tfrac{0{,}4}{3}=1-0{,}1=0{,}9$. Ở câu 2: $0{,}9925+3\cdot0{,}0025=1$.
:::

::: exercise Bài tập 06.13 (Chọn phương pháp cho tàu đổ bộ)
Trong bài thực hành LunarLander, mỗi biến liên tục của quan sát được chia thành ba khoảng và số chân chạm đất nhận ba giá trị, nên có $3^6\cdot3=2187$ ô; mỗi ô có bốn hành động; $\gamma=0{,}99$. Lượt kết thúc khi tàu rơi hoặc ra khỏi khung (phần thưởng $-100$) hay nằm yên ($+100$), và bị cắt ngắn ở bước $1000$. Hành vi là chính sách $\varepsilon_k$-tham lam với $\varepsilon_k$ giảm tuyến tính từ $1$ về $\varepsilon_{\min}=0{,}05$ trong $1500$ lượt đầu rồi giữ nguyên; bước học theo cặp là $\alpha_n=\max(0{,}05,\ n^{-0{,}6})$. Trong một lần chạy đã nhúng trong notebook, $500$ lượt huấn luyện cuối của Sarsa (hành vi với $\varepsilon=0{,}05$) dài trung bình $655$ bước và $7\%$ số lượt bị cắt ngắn. Sau $3000$ lượt huấn luyện, chính sách tham lam theo mỗi bảng được đánh giá trên cùng $100$ lượt kiểm tra. Tổng phần thưởng không chiết khấu của lượt, trung bình $\pm$ sai số chuẩn, là $26{,}2\pm14{,}0$ với Sarsa và $-6{,}6\pm17{,}2$ với Q-learning; hiệu ghép cặp Sarsa trừ Q-learning là $32{,}8\pm46{,}2$, với $46{,}2$ là nửa độ rộng khoảng tin cậy $95\%$.

1. Chọn điều khiển Monte Carlo (Thuật toán 06.9) hay một phương pháp một bước, kèm lý do.
2. Viết mục tiêu Sarsa và mục tiêu Q-learning tại bước cắt ngắn.
3. Chỉ ra các giả thiết của Định lý 06.21–06.22 bị vi phạm và các giả thiết được thỏa.
4. Từ kết quả đánh giá, xác định đã xếp hạng được hai thuật toán chưa.
:::

::: hint
Phân biệt trạng thái kết thúc với lượt bị cắt ngắn (Nhận xét 06.10, 06.13). Với câu 3, kiểm lần lượt tính Markov, bước học và điều kiện tham lam trong giới hạn. Với câu 4, xét khoảng của hiệu ghép cặp có chứa $0$ không.
:::

::: solution
**Câu 1.** Chọn Sarsa hoặc Q-learning. Lượt bị cắt ngắn dừng tại một trạng thái chưa kết thúc nên không cho lợi tức hoàn chỉnh, và Thuật toán 06.9 không dùng được dữ liệu của nó (Nhận xét 06.10). Trong $500$ lượt huấn luyện cuối của Sarsa, $7\%$ số lượt bị cắt, nên Monte Carlo bỏ toàn bộ dữ liệu của các lượt ấy. Lượt dài trung bình $655$ bước, nên mỗi cập nhật Monte Carlo phải chờ hàng trăm bước. Phương pháp một bước cập nhật sau mỗi chuyển, kể cả trong lượt bị cắt.

**Câu 2.** Ở bước $1000$, $S'$ chưa kết thúc, nên mục tiêu vẫn chứa giá trị tiếp nối:

$$
\begin{aligned}
Y^{\text{Sarsa}}&=R+\gamma Q(S',A'),\\
Y^{\text{Q}}&=R+\gamma\max_aQ(S',a).
\end{aligned}
$$

Đặt $Y=R$ là coi một trạng thái giữa chừng như trạng thái kết thúc có giá trị $0$ (Nhận xét 06.13).

**Câu 3.** Ba giả thiết bị vi phạm:

- tính Markov: mỗi ô gộp vô số quan sát, và hai quan sát trong cùng ô có thể dẫn tới phân phối ô kế tiếp khác nhau, nên không có $p(\cdot\mid s,a)$ chung cho ô;
- Robbins–Monro theo cặp: $n^{-0{,}6}\le0{,}05$ khi và chỉ khi $n\ge20^{5/3}\approx147{,}4$, nên $\alpha_n=0{,}05$ khi $n\ge148$ và $\sum_n\alpha_n^2=\infty$ (Bài tập 06.9);
- GLIE, chỉ cần cho Sarsa: với một cực đại duy nhất, khối xác suất trên cực đại dừng ở $1-0{,}05+0{,}05/4=0{,}9625$, không tiến tới $1$.

Tập ô hữu hạn và $\gamma=0{,}99<1$ thì thỏa. Vì thiếu giả thiết, hai định lý không cho kết luận nào về hội tụ hay phân kỳ của hai bảng.

**Câu 4.** Chưa xếp hạng được. Hai chính sách được chạy trên cùng $100$ hạt giống kiểm tra, nên phép so sánh dùng hiệu ghép cặp: hiệu của hai tổng thưởng trên từng hạt giống, lấy trung bình, kèm nửa độ rộng $1{,}96$ sai số chuẩn của các hiệu. Khoảng ở đây là $32{,}8\pm46{,}2=[-13{,}4;\,79{,}0]$, chứa $0$, nên $100$ lượt kiểm tra chưa đủ để kết luận Sarsa tốt hơn Q-learning trên tàu đổ bộ. Nếu khoảng không chứa $0$, kết luận chỉ áp dụng cho hai bảng cụ thể đã học, vì mỗi bảng phụ thuộc hạt giống huấn luyện. Muốn so hai thuật toán, cần lặp lại huấn luyện với nhiều hạt giống (notebook, phần 13, nhiệm vụ 1).

**Kiểm tra lại.** $3^6\cdot3=729\cdot3=2187$; $148^{-0{,}6}\approx0{,}0499<0{,}05<147^{-0{,}6}\approx0{,}0501$; $32{,}8-46{,}2=-13{,}4$ và $32{,}8+46{,}2=79{,}0$. Ba lỗi thường gặp: đặt $Y=R$ ở bước cắt ngắn; nêu GLIE như giả thiết của Định lý 06.21, trong khi Q-learning chỉ cần độ phủ; và so hai trung bình $26{,}2$ và $-6{,}6$ với hai sai số chuẩn riêng, bỏ mất tương quan giữa hai chính sách trên cùng hạt giống.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

- **Bài giảng gốc.** Tạ Việt Cường, *Lecture 06: Điều khiển phi mô hình — Monte Carlo Control, SARSA, Q-Learning và tính chất hội tụ*, học phần Học tăng cường, năm học 2025–2026. Dãy năm ô lấy từ trang 15–21. Trang nguồn theo mục: Mục 1, trang 3–8, 15–16, 24; Mục 2, trang 9–11, 16–17; Mục 3, trang 12–14, 18; Mục 4, trang 8, 19–21; Mục 5, trang 11, 25–28; Mục 6, trang 19, 29; Tóm tắt, trang 22, 30.
- **Sutton và Barto (2018).** R. S. Sutton, A. G. Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §2.5 (công thức 2.7, tr. 33) cho Định nghĩa 06.19; §5.1, §5.3–5.4 (tr. 92–93, 97–103) cho Mục 1–2 và Nhận xét 06.23; §6.4 (tr. 129–130) cho Mục 3 và Định lý 06.22; §6.5 (Ví dụ 6.6, tr. 131–132) cho Mục 4 và Định lý 06.21; §6.7 (tr. 134–136) cho Tình huống 06.1; §7.3 (công thức 7.9–7.10, tr. 148) cho Mục 6.1.
- **Watkins và Dayan (1992).** C. J. C. H. Watkins, P. Dayan, "Q-learning", *Machine Learning* 8, 279–292. Định lý hội tụ của Q-learning dạng bảng, tr. 282, dùng cho Định lý 06.21.
- **Singh, Jaakkola, Littman và Szepesvári (2000).** "Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms", *Machine Learning* 38, 287–308. Định nghĩa GLIE (tr. 291–292) và Định lý 1 (tr. 294–295), dùng cho Định nghĩa 06.18 và Định lý 06.22; lịch thăm dò theo trạng thái $c/C_t(s)$ dùng ở Mục 5.2.
- **Bertsekas và Tsitsiklis (1996).** *Neuro-Dynamic Programming*, Athena Scientific. §2.2 (bài toán đường đi ngắn nhất ngẫu nhiên) và §5.6 cho trường hợp $\gamma=1$ ở Mục 5.4; Chương 4 (xấp xỉ ngẫu nhiên) và §5.6 (Q-learning) cho ý tưởng chứng minh ở Mục 5.1.
- **Tsitsiklis (2002).** J. N. Tsitsiklis, "On the Convergence of Optimistic Policy Iteration", *Journal of Machine Learning Research* 3, 59–72; dùng cho Nhận xét 06.23.
- **Robbins và Monro (1951).** H. Robbins, S. Monro, "A Stochastic Approximation Method", *Annals of Mathematical Statistics* 22, 400–407; nguồn gốc của điều kiện trong Định nghĩa 06.19.
- **Hoeffding (1963).** W. Hoeffding, "Probability Inequalities for Sums of Bounded Random Variables", *Journal of the American Statistical Association* 58, 13–30, Định lý 2; dùng cho Mệnh đề 06.26.
- **Giáo trình *Học máy thống kê*.** Chương Học tăng cường, mục học hàm Q; dùng cho cách dẫn dắt và thuật ngữ tiếng Việt ở phần mở chương và Mục 1.1.
- **Bài thực hành.** Notebook `thuc-hanh-lunarlander-dieu-khien-phi-mo-hinh.ipynb` của Bài 06, phần 3–11: Ví dụ 06.13, các đoạn "Trong thực hành", Tình huống 06.1, Bài tập 06.12 (câu 1, phần 5), Bài tập 06.13 (phần 4–8 và 10).
