# Bài 07 — Xấp xỉ hàm trong Học tăng cường

Trong chương này, chúng ta thay bảng giá trị của Bài 05–06 bằng một hàm tuyến tính theo đặc trưng (feature) với vector tham số dùng chung, xây dựng lại Monte Carlo, phương pháp sai phân thời gian (temporal difference, TD) TD(0), Sarsa và Q-learning trên hàm đó, và nêu điểm đích cùng giả thiết hội tụ của từng quy tắc.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Viết $\hat v(s,w)=x(s)^\top w$, $\hat q(s,a,w)=x(s,a)^\top w$ với miền và kích thước; tính mức lan của một cập nhật, nhận diện nhập nhằng đặc trưng (aliasing) (Bài tập 07.1, 07.2, 07.3, 07.12, 07.15, 07.16; tệp bài tập: 07.20).
2. Thực hiện bằng tay một cập nhật Monte Carlo gradient, TD(0), Sarsa và Q-learning bán gradient (semi-gradient), ghi mục tiêu, sai lệch và tham số mới (Bài tập 07.7, 07.10, 07.11, 07.13).
3. Phân biệt gradient đầy đủ với bán gradient theo việc mục tiêu có chứa tham số, và chỉ ra số hạng bị bỏ (Bài tập 07.4, 07.5, 07.7).
4. Phát biểu điểm cố định Bellman chiếu, tính nghiệm TD(0) và Monte Carlo trên ví dụ nhỏ, nêu đủ giả thiết hội tụ của TD(0) tuyến tính (Bài tập 07.8, 07.9, 07.17; tệp bài tập: 07.22, 07.24).
5. Phân biệt mục tiêu Sarsa với mục tiêu Q-learning và nhận diện bộ ba bất ổn (deadly triad) trong một quy tắc cập nhật (Bài tập 07.13, 07.14, 07.18; tệp bài tập: 07.23, 07.25).
6. Đối chiếu kết quả thực hành với giả thiết của kết quả lý thuyết trước khi kết luận về hội tụ hay phân kỳ (Bài tập 07.6, 07.19; tệp bài tập: 07.21, 07.23, 07.24, 07.25).

Số hiệu sau "tệp bài tập:" chỉ bài trong [Bài tập Bài 07](material-viewer.html?doc=materials/lec-07/exercises.md&deck=lecture-07-xap-xi-ham.html), bộ bài giao chính thức của bài học; Bài tập 07.20–07.25 chỉ có trong tệp đó, các bài còn lại nằm trong chương này.

<!-- note-topic-id: lec-07-topic-13 -->
## Kiến thức tiên quyết

Kết quả của bài trước được dẫn theo mục của ghi chú bài đó, dạng "ghi chú Bài 05, Mục 3", và phát biểu lại dưới đây.

- **Lợi tức và hàm giá trị** (ghi chú Bài 03, Mục 2 và Mục 3; ghi chú Bài 06, Mục 1). Với lượt (episode) kết thúc ở thời điểm $T$, lợi tức (return) $G_t=\sum_{j=0}^{T-t-1}\gamma^jR_{t+j+1}$ thỏa $G_t=R_{t+1}+\gamma G_{t+1}$, $G_T=0$. Ta có $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$, $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ và $q_*(s,a)=\max_\pi q_\pi(s,a)$.
- **Phương trình Bellman dạng ma trận** (ghi chú Bài 03, Mục 4 và Mục 5; ghi chú Bài 04, Mục 1). Với $\mathcal S$ hữu hạn, ma trận chuyển $P_\pi$ và phần thưởng kỳ vọng một bước $r_\pi$, toán tử $T_\pi v=r_\pi+\gamma P_\pi v$ với $\gamma<1$ là ánh xạ co theo chuẩn cực đại và có điểm cố định duy nhất $v_\pi$.
- **Chuỗi Markov cảm sinh và phân phối dừng.** Với $\pi$ cố định, chuỗi trạng thái dưới $\pi$ là chuỗi Markov với ma trận chuyển $P_\pi$ (ghi chú Bài 03, Mục 5.2). Phần còn lại là kiến thức xác suất tiên quyết bổ sung, chưa có trong ghi chú các bài trước (Sutton và Barto, 2018, §9.2; §10.3 cho chuỗi ergodic). Chuỗi là tối giản (irreducible) khi từ mọi trạng thái có thể tới mọi trạng thái khác, và không tuần hoàn (aperiodic) khi việc quay lại một trạng thái không bị giới hạn vào bội của một chu kỳ lớn hơn $1$. Khi $\mathcal S$ hữu hạn, chuỗi tối giản có phân phối dừng (stationary distribution) duy nhất $d_\pi$, với $d_\pi^\top P_\pi=d_\pi^\top$ và $d_\pi>0$; chỉ cần tối giản cho tính duy nhất, còn không tuần hoàn là giả thiết riêng của Định lý 07.29.
- **Monte Carlo và TD(0) dạng bảng** (ghi chú Bài 05, Mục 2 và Mục 3). $V(S_t)\leftarrow V(S_t)+\alpha[G_t-V(S_t)]$ sau khi lượt kết thúc; $V(S_t)\leftarrow V(S_t)+\alpha[R_{t+1}+\gamma V(S_{t+1})-V(S_t)]$ ngay sau chuyển, với $V=0$ tại trạng thái kết thúc. Mục tiêu chứa ước lượng hiện tại gọi là mục tiêu bootstrap (bootstrap target).
- **Điều kiện Robbins–Monro** (ghi chú Bài 05, Mục 2 và Mục 4). Dãy bước học dương thỏa $\sum_n\alpha_n=\infty$ và $\sum_n\alpha_n^2<\infty$; $\alpha_n=1/(n+1)$ thỏa, bước hằng không thỏa điều kiện thứ hai.
- **ε-tham lam, chính sách hành vi và chính sách đích** (ghi chú Bài 06, Mục 1, 3, 4). Chính sách $\varepsilon$-tham lam theo $Q$ với $m$ hành động chọn hành động tham lam với xác suất $1-\varepsilon+\varepsilon/m$, mỗi hành động khác với xác suất $\varepsilon/m$, theo một quy tắc phá hòa (tie-breaking) cố định. Chính sách hành vi $\pi_b$ sinh dữ liệu; chính sách đích là chính sách mà giá trị đang được học. Sarsa, với mục tiêu $R_{t+1}+\gamma Q(S_{t+1},A_{t+1})$, học theo chính sách (on-policy); Q-learning, với mục tiêu $R_{t+1}+\gamma\max_{a'}Q(S_{t+1},a')$, học khác chính sách (off-policy).
- **Lấy mẫu quan trọng (importance sampling)** (ghi chú Bài 06, Mục 6, Định nghĩa 06.24). Khi dữ liệu do chính sách hành vi $\pi_b$ sinh mà cần kỳ vọng theo chính sách đích $\pi$, mỗi hành động được nhân tỉ số $\rho_t=\pi(A_t\mid S_t)/\pi_b(A_t\mid S_t)$, với điều kiện hỗ trợ $\pi(a\mid s)>0\Rightarrow\pi_b(a\mid s)>0$.
- **Hội tụ dạng bảng** (ghi chú Bài 06, Mục 5). Với quá trình quyết định Markov (Markov decision process, MDP) hữu hạn, phần thưởng bị chặn, $\gamma<1$, Q-learning dạng bảng hội tụ tới $q_*$ hầu chắc chắn (almost surely) khi mọi cặp được cập nhật vô hạn lần với bước học Robbins–Monro theo cặp; Sarsa cần thêm điều kiện GLIE.
- **Đại số tuyến tính.** Với $D$ chéo dương, $\langle u,v\rangle_D=u^\top Dv$ là tích vô hướng, $\lVert v\rVert_D=\sqrt{v^\top Dv}$, và $\lvert\langle u,v\rangle_D\rvert\le\lVert u\rVert_D\lVert v\rVert_D$ (Cauchy–Schwarz). Ma trận $M$ với $z^\top Mz>0$ khi $z\ne0$ thì khả nghịch.
- **Xác suất.** $\mathbb E[\mathbb E[X\mid Y]]=\mathbb E[X]$; $\mathbb E[(X-c)^2\mid Y]=\mathrm{Var}(X\mid Y)+(\mathbb E[X\mid Y]-c)^2$ với mọi hằng $c$; Jensen: $(\sum_ip_iy_i)^2\le\sum_ip_iy_i^2$ khi $p_i\ge0$, $\sum_ip_i=1$.

## Bảng ký hiệu

Bảng gồm ký hiệu dùng xuyên suốt chương; ký hiệu dùng một lần được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $\mathcal A$, $m$ | tập trạng thái; tập hành động; số hành động | $\mathcal S$ hữu hạn trong kết quả dạng ma trận; $m=\lvert\mathcal A\rvert$ |
| $t$, $T$ | thời điểm của mẫu trong lượt; thời điểm kết thúc lượt | $\{0,1,\dots\}$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động; phần thưởng của chuyển $S_t\to S_{t+1}$ | $\mathcal S$; $\mathcal A$; $\mathbb R$ |
| $p(s',r\mid s,a)$ | động lực môi trường | xác suất |
| $\pi$, $\pi_b$, $\pi_w$ | chính sách; chính sách hành vi; chính sách $\varepsilon$-tham lam theo $\hat q(\cdot,\cdot,w)$ | phân phối trên $\mathcal A$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$ |
| $G_t$ | lợi tức từ $t$ | biến ngẫu nhiên |
| $v_\pi$, $q_\pi$, $q_*$ | giá trị thật | hàm thực |
| $x(s)$, $x(s,a)$, $d$ | vector đặc trưng; số chiều | $\mathbb R^d$ |
| $\phi(s)$, $k$ | đặc trưng trạng thái của mã hóa bốn khối; số chiều | $\mathbb R^k$ |
| $\mathbf 1_a$, $\mathbf 1_s$ | vector chỉ thị của hành động, của trạng thái | $\{0,1\}^m$; $\{0,1\}^{\lvert\mathcal S\rvert}$ |
| $d_{\text{trái}}(s)$, $u(a)$ | khoảng cách tới tường trái, dấu của hành động trên chuỗi năm trạng thái | $\{1,2,3\}$; $\{1,-1\}$ |
| $w$, $w_n$, $[w]_i$ | tham số; tham số sau $n$ lần cập nhật; thành phần thứ $i$ | $\mathbb R^d$ |
| $\hat v(s,w)$, $\hat q(s,a,w)$ | giá trị ước lượng | $\mathbb R$ |
| $\alpha_n$, $\alpha$ | bước học của lần cập nhật từ $w_n$; bước hằng | $(0,\infty)$ |
| $y_t$, $e_t$, $\delta_t$ | mục tiêu; sai lệch Monte Carlo; sai số TD của mẫu tại $t$ | $\mathbb R$ |
| $\ell_t$ | mất mát mẫu | $\mathbb R^d\to[0,\infty)$ |
| $\mu$, $J_\mu$, $\lVert\cdot\rVert_\mu$ | phân phối trọng số; sai số giá trị $J_\mu=\tfrac12\overline{\mathrm{VE}}$; chuẩn có trọng số $\mu$ | phân phối trên $\mathcal S$; hàm; chuẩn |
| $\Sigma_\mu$, $w_{\mathrm{MC}}$ | $\sum_s\mu(s)x(s)x(s)^\top$; điểm cực tiểu của $J_\mu$ | $\mathbb R^{d\times d}$; $\mathbb R^d$ |
| $d_\pi$, $D$ | phân phối dừng dưới $\pi$; $\operatorname{diag}(d_\pi)$ | phân phối; ma trận |
| $\Phi$ | ma trận đặc trưng, hàng $x(s)^\top$ | $\mathbb R^{\lvert\mathcal S\rvert\times d}$ |
| $P_\pi$, $r_\pi$, $T_\pi$ | ma trận chuyển, phần thưởng kỳ vọng, toán tử Bellman | ma trận; vector; ánh xạ |
| $\Pi_D$, $\lVert\cdot\rVert_D$ | phép chiếu lên $\{\Phi w\}$ theo $\lVert\cdot\rVert_D$; chuẩn | ma trận; chuẩn |
| $A$, $b$, $w_{\mathrm{TD}}$ | $\Phi^\top D(I-\gamma P_\pi)\Phi$; $\Phi^\top Dr_\pi$; nghiệm $Aw=b$ | $\mathbb R^{d\times d}$; $\mathbb R^d$; $\mathbb R^d$ |
| $J_{\mathrm{kt}}$, $\bar g$ | sai số dự đoán lợi tức trên tập kiểm tra của notebook; $\bar g(s)=\mathbb E[G_t\mid S_t=s]$ theo phân phối ghé của dữ liệu | số thực; hàm thực |
| $\varepsilon$ | xác suất thăm dò | $[0,1]$ |
| $\mathrm A,\dots,\mathrm E$ | tên trạng thái của chuỗi năm trạng thái | nhãn |

Quy ước đọc. $R_{t+1}$ gắn với chuyển $S_t\to S_{t+1}$; giá trị tại trạng thái kết thúc bằng $0$; $\mathbb E_\pi$ lấy theo quỹ đạo sinh bởi $\pi$ và $p$. Chỉ số $n$ đếm số lần cập nhật, $t$ là thời điểm của mẫu dùng trong lần cập nhật đó. $(a;b)$ là vector cột hai thành phần; bất đẳng thức vector hiểu theo thành phần. Trong các đoạn thực hành, một số dạng "trung bình ± sai số chuẩn" qua các lượt đánh giá; với hiệu ghép cặp, tức trung bình hiệu giữa hai đại lượng trên cùng các lượt sinh từ cùng hạt giống ngẫu nhiên (random seed), phần sau dấu ± là nửa độ rộng khoảng tin cậy $95\%$.

$d_\pi$ và $d_{\text{trái}}$ là hai ký hiệu riêng, khác số chiều $d$. Tên trạng thái của chuỗi viết chữ đứng để phân biệt với ma trận $A$, $D$ và hành động $A_t$.

Ứng với giáo trình *Học máy thống kê*: $v_\pi$, $q_\pi$ là $V^\pi$, $Q^\pi$; $x(s,a)^\top w$ là $\phi(s,a)^\top w$; $p(s',r\mid s,a)$ ứng với $T$, $R$ của bộ $\langle S,A,T,R,\gamma\rangle$. Bài tập tuần 7 (2025–2026) viết $\phi(s)$ cho $x(s)$. Bộ số của Ví dụ 07.2, 07.3, 07.7–07.11 là số liệu sư phạm tự xây dựng.

## Bản đồ chủ đề

Mười tám chủ đề thuộc bốn nhóm; "trang N" là trang của bài giảng gốc (2025–2026).

| Chủ đề (mã) | Nhóm | Mục | Vai trò; dẫn tới | Nguồn |
|---|---|---|---|---|
| Giới hạn của bảng tra (`lec-07-topic-01`) | cốt lõi | 1.1 | bài toán trung tâm; Bài 06 → nhu cầu tham số chung | trang 22–23 |
| Hàm có tham số dùng chung (`lec-07-topic-02`) | cốt lõi | 1.2 | mức lan; bảng tra → mọi cập nhật | trang 23–26 |
| Bài toán dự đoán và sai số giá trị (`lec-07-topic-03`) | cốt lõi | 1.3 | tiêu chí $J_\mu$; → Mục 2–3 | trang 23, 27, 34 |
| Đặc trưng và nhập nhằng (`lec-07-topic-04`) | cốt lõi | 1.4 | bốn khối, nhập nhằng; → Mục 4 | trang 28–31 |
| Mục tiêu cập nhật (`lec-07-topic-05`) | cốt lõi | 2.1 | gradient đầy đủ, bán gradient; $J_\mu$ → Mục 2–3 | trang 27, 32 |
| Monte Carlo gradient (`lec-07-topic-06`) | cốt lõi | 2.2 | hạ gradient ngẫu nhiên trên $J_\mu$; → Mục 2.3 | trang 33–34 |
| Hội tụ của Monte Carlo tuyến tính (`lec-07-topic-15`) | cốt lõi | 2.3 | đích là hình chiếu của $v_\pi$; → Mục 3 | trang 34; Bài tập tuần 7, bài 4, 6 |
| TD(0) bán gradient (`lec-07-topic-07`) | cốt lõi | 3.1 | cập nhật sau mỗi chuyển; → Mục 3.2 | trang 35–36 |
| Điểm cố định Bellman chiếu (`lec-07-topic-08`) | cốt lõi | 3.2 | đích và hội tụ của TD; → Mục 4 | trang 43–45; bài 5 |
| Hai mục tiêu dự đoán (`lec-07-topic-09`) | cốt lõi | 3.3 | so sánh; → Mục 4 | trang 37; bài 2 |
| Sarsa bán gradient (`lec-07-topic-10`) | cốt lõi | 4.1–4.2 | điều khiển theo chính sách; → Mục 5 | trang 38–40 |
| Q-learning bán gradient (`lec-07-topic-11`) | cốt lõi | 5.1 | điều khiển khác chính sách; → Mục 5.2 | trang 38, 41 |
| Bộ ba bất ổn (`lec-07-topic-17`) | cốt lõi | 5.2 | giới hạn bảo đảm; → Mục 6 | trang 41, 43; bài 3 |
| Phạm vi các kết quả hội tụ (`lec-07-topic-14`) | cốt lõi | 6.1 | bảng giả thiết; → Bài 08 | trang 34, 41–44 |
| Phân tích một quy tắc cập nhật (`lec-07-topic-12`) | cốt lõi | 6.2 | năm bước; → tình huống | trang 22–44 |
| Kiến thức tiên quyết (`lec-07-topic-13`) | cầu nối | Kiến thức tiên quyết | bảo đảm dạng bảng cần một ô mỗi cặp; → Mục 1 | trang 3, 5–20 |
| Bài tập trên chuỗi năm trạng thái (`lec-07-topic-16`) | bổ sung | 4.3 | tính tay trọn lượt; → Mục 5 | Bài tập tuần 7, bài 7, 8; trang 40 |
| MDP tuyến tính (`lec-07-topic-18`) | đọc thêm | Hướng dẫn đọc thêm | giả thiết cấu trúc; → hướng nghiên cứu | trang 42 |

## 1. Hàm giá trị tuyến tính theo đặc trưng

Trong ghi chú Bài 06, Mục 5, Q-learning dạng bảng hội tụ tới $q_*$ nhờ một ô riêng cho mỗi cặp trạng thái–hành động, chỉ đổi khi cặp đó xuất hiện trong dữ liệu. Thực hành Bài 05 chia sáu biến liên tục của Lunar Lander và số chân đang chạm đất ($3$ mức) thành $9\,216$ ô; trên $2\,000$ lượt huấn luyện chỉ $1\,896$ ô có mẫu. Flappy Bird có $12$ biến liên tục; chia mỗi biến thành $10$ khoảng sẽ cho $10^{12}$ ô.

Để học giá trị khi không thể dành một ô cho mỗi trạng thái, chúng ta cần một biểu diễn trong đó một mẫu thay đổi ước lượng ở các trạng thái tương tự. Chúng ta dùng $\hat v(s,w)=x(s)^\top w$ với $w$ dùng chung, xác định điểm đích của từng quy tắc cập nhật và phát biểu, kèm nguồn, điều kiện hội tụ; với điều khiển, chúng ta chỉ ra giả thiết bị mất và dựng một ví dụ phân kỳ.

![Sơ đồ cấu trúc chương: bảng tra được thay bằng hàm tuyến tính (Mục 1); lưới hai hàng (mục tiêu G_t không chứa w; mục tiêu bootstrap chứa w) và ba cột (dự đoán, điều khiển theo chính sách, điều khiển khác chính sách) đặt Monte Carlo gradient (Mục 2, hội tụ tới cực tiểu J_μ), TD(0) (Mục 3, hội tụ tới w_TD), Sarsa (Mục 4, không có bảo đảm chung), Q-learning (Mục 5, có thể phân kỳ); dải dưới là Mục 6.](img/lec-07/chapter-map.svg)

Hình trên sắp bốn quy tắc theo hai câu hỏi. Hàng cho biết mục tiêu có chứa $w$ hay không, tức gradient đầy đủ hay bán gradient. Cột cho biết dữ liệu đến từ chính sách cố định, chính sách đang được cải thiện, hay chính sách khác chính sách đích; mỗi bước sang phải hoặc xuống dưới làm phân tích hội tụ khó hơn.

<!-- note-topic-id: lec-07-topic-01 -->
### 1.1 Giới hạn của bảng tra

Bảng lưu $V(s)\approx v_\pi(s)$ hoặc $Q(s,a)\approx q_\pi(s,a)$ riêng cho từng trạng thái hoặc cặp; ví dụ sau đo giới hạn của cách lưu này.

::: example Ví dụ 07.1 (Lunar Lander rời rạc hóa thành bảng)
**Dữ kiện.** Thực hành Bài 05 chia sáu biến liên tục của tàu thành $3\cdot4^5=3\,072$ ô và ghép với số chân đang chạm đất ($0$, $1$ hoặc $2$, tức $3$ mức), được $9\,216=3\cdot4^5\cdot3$ ô; giá trị của một chính sách cố định được dự đoán bằng trung bình lợi tức trong từng ô. Tập huấn luyện có $2\,000$ lượt, $546\,869$ chuyển; $1\,896$ ô được ghé ít nhất một lần (một lần chạy đã nhúng trong notebook Lunar Lander của Bài 07, mục 5).

**Yêu cầu.** Tính tỉ lệ ô có dữ liệu và số ô không có ước lượng.

**Tính.** $1\,896/9\,216\approx0{,}206$, tức khoảng $20{,}6\%$; số ô không có mẫu là $9\,216-1\,896=7\,320$.

**Diễn giải.** Một trạng thái rơi vào $7\,320$ ô này chỉ có giá trị khởi tạo, dù ô bên cạnh đã được ghé nhiều lần.

**Kiểm tra lại.** $1\,896+7\,320=9\,216=3\,072\cdot3$.
:::

Theo bài giảng gốc (2025–2026), trang 22–23, bảng tra có ba khó khăn, và Ví dụ 07.1 minh họa hai khó khăn đầu.

1. **Bộ nhớ và số mẫu.** Không gian lớn hay liên tục không lưu được một ô cho mỗi phần tử, và mỗi ô cần đủ lần ghé riêng.
2. **Không tổng quát hóa.** Hai trạng thái giống nhau vẫn có hai ô độc lập.
3. **Dữ liệu không độc lập cùng phân phối (iid) và không dừng.** Mẫu trong một lượt phụ thuộc nhau, và phân phối trạng thái đổi khi chính sách đổi; khó khăn này đúng với mọi biểu diễn và xuất hiện lại trong giả thiết của Định lý 07.17 và 07.29.

Một cách trực quan, hai trạng thái của tàu chỉ khác nhau chút ít về độ cao có lợi tức gần nhau, nên muốn một mẫu ở trạng thái này cho thông tin về trạng thái kia, hai trạng thái phải dùng chung một phần biểu diễn. Mô tả này chưa phải định nghĩa.

Nhầm lẫn thường gặp là chia ô mịn hơn để giải khó khăn thứ nhất: số ô tăng thì số mẫu mỗi ô giảm, còn chia thô thì các trạng thái khác nhau phải nhận cùng giá trị.

<!-- note-topic-id: lec-07-topic-02 -->
### 1.2 Hàm có tham số dùng chung

Về mặt ý tưởng, mỗi trạng thái được mô tả bằng một vector số đo $x(s)$, và giá trị ước lượng là tổ hợp các số đo đó với hệ số chung cho mọi trạng thái. Đây chưa phải định nghĩa; trước khi phát biểu, chúng ta tính một cập nhật cụ thể.

![Hai cách lưu giá trị. Bên trái, bảng tra: mỗi trạng thái một ô. Bên phải, hàm có tham số: trạng thái s đi qua vector đặc trưng x(s), rồi kết hợp với vector tham số w để cho dự đoán v̂(s,w); mọi trạng thái dùng chung w.](img/lec-07/tabular-vs-parametric.svg)

Ở bên trái hình, cập nhật một ô không chạm tới ô khác; ở bên phải, mọi dự đoán đi qua cùng $w$. Ví dụ sau đo mức thay đổi đó với các trạng thái hai đặc trưng.

::: example Ví dụ 07.2 (Một cập nhật lan sang trạng thái thứ hai)
**Dữ kiện.** Hai trạng thái hai đặc trưng có $x(s)=(1;1)$, $x(s')=(1;0{,}5)$; dự đoán là $x(\cdot)^\top w$ với $w=(0;0)$. Tại $s$, sai lệch giữa mục tiêu và dự đoán là $e=2$; quy tắc sửa là $\Delta w=\alpha e\,x(s)$ với $\alpha=0{,}1$. Mục 2 suy ra quy tắc này từ gradient của sai số bình phương.

**Yêu cầu.** Tính độ thay đổi dự đoán tại $s$ và $s'$.

**Tính.**

$$
\begin{aligned}
\Delta w&=0{,}1\cdot2\cdot(1;1)=(0{,}2;0{,}2),\\
\Delta\hat v(s)&=0{,}2+0{,}2=0{,}4,\qquad \Delta\hat v(s')=0{,}2+0{,}5\cdot0{,}2=0{,}3.
\end{aligned}
$$

**Diễn giải.** Mẫu chỉ có tại $s$, nhưng dự đoán tại $s'$ cũng tăng, vì hai vector có chung thành phần thứ nhất.

**Kiểm tra lại.** $\alpha e\,x(s')^\top x(s)=0{,}2\cdot1{,}5=0{,}3$.
:::

![Một mẫu tại s với sai lệch e = 2 tạo Δw = αe x(s). Vì w dùng chung, dự đoán tại s tăng 0,4 và dự đoán tại s′ tăng 0,3.](img/lec-07/shared-parameter-effect.svg)

Hình trên vẽ lại Ví dụ 07.2: một mẫu đổi $w$ dùng chung, nên cả hai dự đoán cùng đổi.

::: definition Định nghĩa 07.1 (Hàm giá trị có tham số và xấp xỉ tuyến tính)
Cho tập trạng thái $\mathcal S$, tập hành động hữu hạn $\mathcal A$ và số nguyên dương $d$.

Hàm giá trị trạng thái có tham số là ánh xạ $\hat v:\mathcal S\times\mathbb R^d\to\mathbb R$; với mỗi $w$, $\hat v(\cdot,w)$ ước lượng $v_\pi$. Hàm giá trị hành động có tham số $\hat q:\mathcal S\times\mathcal A\times\mathbb R^d\to\mathbb R$ ước lượng $q_\pi$ hoặc $q_*$.

Vector đặc trưng là ánh xạ $x:\mathcal S\to\mathbb R^d$, hoặc $x:\mathcal S\times\mathcal A\to\mathbb R^d$, chọn trước và không đổi khi học. Xấp xỉ tuyến tính theo đặc trưng là

$$
\hat v(s,w)=x(s)^\top w=\sum_{i=1}^d[x(s)]_i\,[w]_i,\qquad \hat q(s,a,w)=x(s,a)^\top w.
\tag{1.1}
$$
:::

Công thức (1.1) tuyến tính theo $w$, không nhất thiết theo trạng thái, vì $x(s)$ có thể là hàm phi tuyến của trạng thái. Gradient $\nabla_w\hat v(s,w)=x(s)$ và $\nabla_w\hat q(s,a,w)=x(s,a)$ không phụ thuộc $w$, nên mọi quy tắc của chương cộng vào $w$ một bội của vector đặc trưng, với chi phí tỉ lệ số thành phần khác $0$ của vector đó.

Định nghĩa 07.1 tổng quát hóa bảng $V$, $Q$ của Bài 05–06 (Hệ quả 07.3). $\hat v(\cdot,w)$ là một phần tử của lớp hàm mà đặc trưng cho phép, khác $v_\pi$ do chính sách và môi trường quyết định.

::: proposition Mệnh đề 07.2 (Mức lan của một cập nhật tuyến tính)
**Giả thiết.** $\hat v$ dạng (1.1); tham số đổi từ $w$ thành $w'=w+\alpha e\,x(s)$ với $\alpha>0$, $e\in\mathbb R$, $s\in\mathcal S$.

**Kết luận.** Với mọi $s'\in\mathcal S$,

$$
\hat v(s',w')-\hat v(s',w)=\alpha e\,x(s')^\top x(s);
\tag{1.2}
$$

riêng tại $s$, dự đoán đổi $\alpha e\lVert x(s)\rVert^2$.

**Điều kiện áp dụng.** Mọi quy tắc dạng "cộng một bội của $x(s)$", gồm cả bốn quy tắc của chương.

**Phạm vi.** Với hàm không tuyến tính theo $w$, (1.2) không đúng nguyên văn.
:::

::: proof Chứng minh Mệnh đề 07.2
Theo (1.1), $\hat v(s',w')-\hat v(s',w)=x(s')^\top(w+\alpha e\,x(s))-x(s')^\top w=\alpha e\,x(s')^\top x(s)$. Thay $s'=s$ được $\alpha e\lVert x(s)\rVert^2$. $\square$
:::

Mức lan sang $s'$ tỉ lệ với tích vô hướng hai vector đặc trưng: dương thì cùng chiều, bằng $0$ thì không đổi, âm thì ngược chiều. Cùng cơ chế lan cả sai lệch: nếu mục tiêu tại $s$ sai, dự đoán tại $s'$ bị kéo theo. Nhầm lẫn thường gặp là coi tổng quát hóa luôn có lợi; Mệnh đề 07.37 dựng một ví dụ trong đó sự lan này làm tham số tăng không chặn.

::: corollary Hệ quả 07.3 (Đặc trưng chỉ thị cho lại bảng tra)
**Giả thiết.** $\mathcal S$ hữu hạn, $d=\lvert\mathcal S\rvert$, $x(s)=\mathbf 1_s$.

**Kết luận.** $\hat v(s,w)=[w]_s$, và cập nhật $w'=w+\alpha e\,x(s)$ chỉ đổi $[w]_s$, đúng bằng cập nhật bảng $V(s)\leftarrow V(s)+\alpha e$.

**Điều kiện áp dụng.** Cần một tham số cho mỗi trạng thái.

**Phạm vi.** Bảo đảm dạng bảng không tự chuyển sang đặc trưng khác.
:::

::: proof Chứng minh Hệ quả 07.3
$x(s)^\top w$ lấy đúng thành phần thứ $s$ của $w$. Với $s'\ne s$, $x(s')^\top x(s)=0$, còn $x(s)^\top x(s)=1$; theo Mệnh đề 07.2, chỉ dự đoán tại $s$ đổi, và đổi $\alpha e$. $\square$
:::

::: remark Nhận xét 07.4 (Các lớp hàm khác)
Theo bài giảng gốc (trang 25–26), còn có cây quyết định, rừng ngẫu nhiên, hàm nhân (kernel), láng giềng gần nhất, cơ sở Fourier, mã hóa lưới ô (tile coding) và mạng nơ-ron. Hai lớp Fourier và lưới ô vẫn thuộc dạng (1.1) (Sutton và Barto, 2018, §9.5); mạng nơ-ron thì không, và có ít bảo đảm hơn (§9.7). Các định lý của Mục 2–3 phát biểu cho lớp tuyến tính.
:::

**Trong thực hành.** Trong notebook Lunar Lander (mục 6), với đặc trưng tuyến tính thô chín thành phần, sau cập nhật đầu tại $S_0$ với $w_0=0$, dự đoán tại $S_1$ là $x(S_1)^\top w_1=0{,}5832$, khác $0$ dù $S_1$ chưa được cập nhật (một lần chạy đã nhúng trong notebook). Với bảng, dự đoán đó vẫn bằng giá trị khởi tạo.

::: exercise Bài tập 07.1 (Mức lan sang ba trạng thái)
Cho $x(s)=(1;0)$, $x(s')=(0;1)$, $x(s'')=(-1;1)$, dự đoán $x(\cdot)^\top w$ với $w=(0;0)$, và một cập nhật tại $s$ với $\Delta w=\alpha e\,x(s)$, $e=2$, $\alpha=0{,}1$. Tính độ thay đổi dự đoán tại $s$, $s'$, $s''$ và giải thích dấu.
:::

::: hint
Dùng (1.2): mức lan bằng $\alpha e$ nhân tích vô hướng với $x(s)$.
:::

::: solution
**Tính.** $\Delta w=(0{,}2;0)$, nên $\Delta\hat v(s)=0{,}2$, $\Delta\hat v(s')=0$, $\Delta\hat v(s'')=-0{,}2$.

**Diễn giải.** $x(s')^\top x(s)=0$ nên $s'$ không đổi; $x(s'')^\top x(s)=-1$ nên $s''$ đổi ngược chiều với $s$ (Mệnh đề 07.2).

**Kiểm tra lại.** $\alpha e\,x(s'')^\top x(s)=0{,}2\cdot(-1)=-0{,}2$.
:::

<!-- note-topic-id: lec-07-topic-03 -->
### 1.3 Bài toán dự đoán và sai số giá trị

Với tham số dùng chung, làm đúng hơn ở một trạng thái thường làm sai hơn ở trạng thái khác (Mệnh đề 07.2; Sutton và Barto, 2018, §9.2). Để chọn $w$, chúng ta cần nói trạng thái nào được ưu tiên; ví dụ sau cho thấy lựa chọn đó quyết định nghiệm.

::: example Ví dụ 07.3 (Hai trạng thái cùng vector đặc trưng, đổi trọng số)
**Dữ kiện.** $x(s_1)=x(s_2)=1$, nên $\hat v(s_1,w)=\hat v(s_2,w)=w=:c$; $v_\pi(s_1)=0$, $v_\pi(s_2)=2$; trọng số $\mu_1+\mu_2=1$.

**Yêu cầu.** Tìm $c$ nhỏ nhất hóa $E(c)=\tfrac12[\mu_1c^2+\mu_2(2-c)^2]$ với $(\mu_1;\mu_2)=(\tfrac12;\tfrac12)$ và $(\tfrac34;\tfrac14)$.

**Tính.** $E'(c)=\mu_1c-\mu_2(2-c)=c-2\mu_2=0$ khi $c=2\mu_2$.

- $(\tfrac12;\tfrac12)$: $c=1$, $E(1)=\tfrac12[\tfrac12+\tfrac12]=\tfrac12$.
- $(\tfrac34;\tfrac14)$: $c=\tfrac12$, $E(\tfrac12)=\tfrac12[\tfrac34\cdot\tfrac14+\tfrac14\cdot\tfrac94]=\tfrac38$.

**Diễn giải.** Dự đoán chung là trung bình có trọng số của hai giá trị thật; đổi trọng số thì nghiệm đổi.

**Kiểm tra lại.** $\mu_1\cdot0+\mu_2\cdot2$ cho $1$ và $\tfrac12$.
:::

Về mặt ý tưởng, chúng ta đo sai số bình phương ở từng trạng thái rồi lấy trung bình theo một phân phối cho biết trạng thái nào quan trọng hơn. Mô tả này chưa phải định nghĩa; định nghĩa sau nêu đủ giả thiết.

::: definition Định nghĩa 07.5 (Bài toán dự đoán và sai số giá trị)
Cho một MDP với phần thưởng bị chặn, chính sách $\pi$ cố định, và $\gamma<1$ hoặc mọi lượt kết thúc với thời gian kết thúc kỳ vọng hữu hạn, để $v_\pi$ hữu hạn. Cho đặc trưng $x$, hàm $\hat v$ dạng (1.1) và phân phối $\mu$ trên $\mathcal S$. Sai số giá trị của $w$ là

$$
J_\mu(w)=\tfrac12\sum_{s\in\mathcal S}\mu(s)\big(v_\pi(s)-\hat v(s,w)\big)^2 .
\tag{1.3}
$$

Bài toán dự đoán với xấp xỉ hàm là tìm $w$ có $J_\mu(w)$ nhỏ khi chỉ có các lượt sinh theo $\pi$, không biết $p$. Khi $\mathcal S$ liên tục, tổng thay bằng kỳ vọng theo $\mu$.
:::

Mỗi trạng thái đóng góp bình phương sai lệch nhân trọng số $\mu(s)$; $\overline{\mathrm{VE}}=2J_\mu$ là sai số giá trị bình phương trung bình của Sutton và Barto (2018, §9.2, tr. 199). Ví dụ 07.3 là trường hợp $\mathcal S=\{s_1,s_2\}$, $d=1$.

Thường chọn $\mu$ là tỉ lệ thời gian tác tử (agent) ở mỗi trạng thái khi đi theo $\pi$, gọi là phân phối theo chính sách: $d_\pi$ với bài toán không kết thúc, số lần ghé trung bình mỗi lượt đã chuẩn hóa với bài toán theo lượt. Ký hiệu $d_\pi$ chỉ dùng cho phân phối dừng.

Nhầm lẫn thường gặp là coi $J_\mu$ tính được từ dữ liệu: nó chứa $v_\pi$, và Mục 2 thay $v_\pi$ bằng mục tiêu tính từ mẫu.

::: definition Định nghĩa 07.6 (Ma trận đặc trưng và lớp biểu diễn)
Cho $\mathcal S$ hữu hạn, đánh số các trạng thái. Ma trận đặc trưng $\Phi\in\mathbb R^{\lvert\mathcal S\rvert\times d}$ có hàng thứ $s$ là $x(s)^\top$, nên vector dự đoán là $\Phi w$. Lớp biểu diễn là $\{\Phi w:w\in\mathbb R^d\}$. Với $\lVert v\rVert_\mu^2=\sum_s\mu(s)v(s)^2$, ta có $J_\mu(w)=\tfrac12\lVert v_\pi-\Phi w\rVert_\mu^2$.
:::

Lớp biểu diễn là không gian cột của $\Phi$ (Bài tập 07.2), và $J_\mu(w)$ là một nửa bình phương khoảng cách có trọng số từ $v_\pi$ tới một điểm của lớp.

**Trong thực hành.** Trong notebook Lunar Lander (mục 5), thước đo là $J_{\mathrm{kt}}$, trung bình của $(G_t-\hat v(S_t,w))^2$ trên $500$ lượt kiểm tra. Theo hệ thức phương sai, $J_{\mathrm{kt}}$ bằng xấp xỉ một hằng số cộng trung bình của $(\bar g(S_t)-\hat v(S_t,w))^2$; $\bar g$ trùng $v_\pi$ chỉ khi quan sát có tính Markov, điều không được bảo đảm vì quan sát thiếu địa hình. Hai mốc là $5\,797{,}1$ cho $\hat v\equiv0$ và $3\,021{,}2$ cho hằng số tốt nhất (một lần chạy đã nhúng trong notebook).

::: exercise Bài tập 07.2 (Lớp biểu diễn là một không gian con)
Với $\mathcal S$ hữu hạn và $\Phi$ của Định nghĩa 07.6:

- chứng minh $\{\Phi w:w\in\mathbb R^d\}$ là không gian cột của $\Phi$, có số chiều $\operatorname{rank}\Phi\le d$;
- suy ra rằng khi $\operatorname{rank}\Phi<\lvert\mathcal S\rvert$ có hàm giá trị nằm ngoài lớp.
:::

::: hint
Viết $\Phi w=\sum_i[w]_i\,\Phi_{:,i}$ theo các cột $\Phi_{:,i}$.
:::

::: solution
**Bước 1 (không gian con).** $\lambda_1\Phi w_1+\lambda_2\Phi w_2=\Phi(\lambda_1w_1+\lambda_2w_2)$ với mọi số thực $\lambda_1$, $\lambda_2$, và $\Phi\cdot0=0$.

**Bước 2 (không gian cột).** $\Phi w=\sum_{i=1}^d[w]_i\Phi_{:,i}$ là tổ hợp tuyến tính của các cột, và mọi tổ hợp như vậy có dạng $\Phi w$; số chiều là $\operatorname{rank}\Phi\le d$.

**Bước 3 (hệ quả).** Nếu $\operatorname{rank}\Phi<\lvert\mathcal S\rvert$, không gian cột là không gian con thực sự, nên có $v$ nằm ngoài nó; nếu $v_\pi$ là một vector như vậy và $\mu>0$ thì $J_\mu(w)>0$ với mọi $w$.

**Kiểm tra lại.** Với Hệ quả 07.3, $\Phi=I$ có hạng đầy đủ: bảng biểu diễn được mọi hàm giá trị.
:::

<!-- note-topic-id: lec-07-topic-04 -->
### 1.4 Đặc trưng, mã hóa bốn khối và nhập nhằng

Với dạng (1.1), mọi thông tin mô hình dùng được về trạng thái nằm trong $x(s)$. Còn hai câu hỏi: chọn $x(s)$ thế nào, và dựng $x(s,a)$ thế nào cho điều khiển; ví dụ sau trả lời câu thứ nhất.

::: example Ví dụ 07.4 (Đặc trưng của Lunar Lander)
**Dữ kiện.** Trong notebook Lunar Lander (mục 4), mỗi biến liên tục $o_j$ được đưa về $z_j=\operatorname{clip}\big((o_j-\underline o_j)/(\overline o_j-\underline o_j),0,1\big)$ với cận $\underline o_j$, $\overline o_j$ cố định; độ cao dùng $[-0{,}25;1{,}6]$. Họ tuyến tính thô là $(1;\,2z-1;\,l_1;\,l_2)$ với hai cờ chân $l_1,l_2\in\{0,1\}$. Họ Fourier bậc 3 gồm các $\cos(\pi\eta^\top z)$ với $\eta\in\{0,1,2,3\}^6$ có tối đa hai thành phần khác $0$, cộng hai cờ chân. Bài giảng gốc (trang 31) có một đặc trưng điều hướng cùng kiểu.

**Yêu cầu.** Tính số chiều của hai họ và thành phần độ cao của họ tuyến tính thô tại độ cao $1{,}403$.

**Tính.**

- Tuyến tính thô: hằng số, sáu biến, hai cờ: $1+6+2=9$.
- Fourier bậc 3: một vector $\eta=0$; $6\cdot3=18$ vector có đúng một thành phần khác $0$ (chọn biến, chọn bậc); $\binom62\cdot3^2=135$ vector có đúng hai thành phần khác $0$ (chọn cặp biến, chọn bậc cho mỗi biến); cộng hai cờ: $1+18+135+2=156$.
- Độ cao: $z=(1{,}403+0{,}25)/1{,}85\approx0{,}8935$ và $2z-1\approx0{,}787$.

**Diễn giải.** Thành phần hằng $1$ cho hệ số chặn; họ Fourier biểu diễn được tương tác của từng cặp biến, không của ba biến trở lên.

**Kiểm tra lại.** Notebook in $9$, $156$ và thành phần độ cao $0{,}787$ (một lần chạy đã nhúng trong notebook).
:::

Đặc trưng tốt giữ thông tin cần để dự đoán lợi tức dưới chính sách đang xét, nên $v_\pi$ gần lớp biểu diễn. Đặc trưng kém gây sai số xấp xỉ, nhập nhằng và chính sách kém. Theo bài giảng gốc (trang 31), lý thuyết cổ điển giả sử đặc trưng cho trước.

Với điều khiển, một cách trực quan, mỗi hành động cần một phần giá trị riêng phụ thuộc trạng thái. Mô tả này chưa phải định nghĩa; ví dụ sau tính khối tạo ra phần riêng đó.

::: example Ví dụ 07.5 (Tích Kronecker với hai đặc trưng và hai hành động)
**Dữ kiện.** $\phi(s)=(\phi_1;\phi_2)$; hai hành động với $\mathbf 1_1=(1;0)$, $\mathbf 1_2=(0;1)$.

**Yêu cầu.** Viết $\phi(s)\otimes\mathbf 1_1$ và $\phi(s)\otimes\mathbf 1_2$.

**Tính.** Tích Kronecker thay mỗi $\phi_i$ bằng khối $\phi_i\mathbf 1_a$: $\phi(s)\otimes\mathbf 1_1=(\phi_1;0;\phi_2;0)$ và $\phi(s)\otimes\mathbf 1_2=(0;\phi_1;0;\phi_2)$.

**Diễn giải.** Tọa độ $1$, $3$ chỉ khác $0$ khi chọn hành động $1$, nên trọng số ở đó chỉ ảnh hưởng giá trị của hành động $1$.

**Kiểm tra lại.** Cộng hai vector được $(\phi_1;\phi_1;\phi_2;\phi_2)$; gộp tọa độ theo từng $\phi_i$ cho lại $\phi(s)$.
:::

::: definition Định nghĩa 07.7 (Đặc trưng bốn khối)
Cho $\phi:\mathcal S\to\mathbb R^k$ và $m$ hành động. Đặc trưng bốn khối là

$$
x(s,a)=\big(\phi(s);\ \mathbf 1_a;\ \phi(s)\otimes\mathbf 1_a;\ 1\big)\in\mathbb R^{d},\qquad d=k+m+mk+1 .
\tag{1.4}
$$

Tham số chia thành $w^{(1)}\in\mathbb R^k$, $w^{(2)}\in\mathbb R^m$, $w^{(3)}\in\mathbb R^{mk}$, $w^{(4)}\in\mathbb R$; $w^{(3)}_a\in\mathbb R^k$ gồm các thành phần của $w^{(3)}$ ở những tọa độ mà $\phi(s)\otimes\mathbf 1_a$ có thể khác $0$.
:::

Đây là mã hóa của bài giảng gốc (trang 31); đổi thứ tự thành $\mathbf 1_a\otimes\phi(s)$ chỉ hoán vị tọa độ.

::: proposition Mệnh đề 07.8 (Vai trò của khối Kronecker)
**Giả thiết.** $\hat q(s,a,w)=x(s,a)^\top w$ với $x$ theo (1.4).

**Kết luận.**

- (a) $\hat q(s,a,w)=\phi(s)^\top\big(w^{(1)}+w^{(3)}_a\big)+[w^{(2)}]_a+w^{(4)}$.
- (b) Nếu bỏ khối thứ ba, $\hat q(s,a,w)-\hat q(s,a',w)=[w^{(2)}]_a-[w^{(2)}]_{a'}$ không phụ thuộc $s$, nên với quy tắc phá hòa cố định, hành động tham lam như nhau ở mọi trạng thái.

**Điều kiện áp dụng.** Số hành động hữu hạn.

**Phạm vi.** Chỉ nói về khả năng biểu diễn.
:::

::: proof Chứng minh Mệnh đề 07.8
**Bước 1 (khai triển theo khối).** $x(s,a)^\top w=\phi(s)^\top w^{(1)}+\mathbf 1_a^\top w^{(2)}+(\phi(s)\otimes\mathbf 1_a)^\top w^{(3)}+w^{(4)}$. Số hạng thứ hai bằng $[w^{(2)}]_a$. Vector $\phi(s)\otimes\mathbf 1_a$ có $\phi_i(s)$ ở tọa độ thứ $i$ của nhóm ứng với $a$ và $0$ ở chỗ khác, nên số hạng thứ ba bằng $\phi(s)^\top w^{(3)}_a$.

**Bước 2 (bỏ khối thứ ba).** Khi đó $\hat q(s,a,w)=\phi(s)^\top w^{(1)}+[w^{(2)}]_a+w^{(4)}$; trong hiệu giữa hai hành động, $\phi(s)^\top w^{(1)}$ và $w^{(4)}$ triệt tiêu. $\square$
:::

Khối Kronecker cho mỗi hành động một vector trọng số riêng $w^{(3)}_a$ trên đặc trưng trạng thái; thiếu nó, các giá trị hành động chỉ khác nhau một hằng số. Đặc trưng của chuỗi năm trạng thái ở Mục 4 có cùng giới hạn (Mệnh đề 07.32).

::: remark Nhận xét 07.9 (Mã hóa bốn khối không đủ hạng cột)
Thành phần $\phi_i(s)$ của khối thứ nhất bằng tổng theo $a'\in\mathcal A$ của các tọa độ ứng với $\phi_i$ trong khối thứ ba, và hằng số $1$ bằng tổng các thành phần của $\mathbf 1_a$. Vì vậy ma trận có hàng $x(s,a)^\top$ không đủ hạng cột: nhiều $w$ cho cùng $\hat q$, và giả thiết "cột độc lập" của Định lý 07.29 không thỏa.
:::

Còn một giới hạn mà không mã hóa nào tránh được: dự đoán chỉ phụ thuộc trạng thái qua vector đặc trưng.

::: example Ví dụ 07.6 (Hai quan sát Lunar Lander cùng vector đặc trưng)
**Dữ kiện.** Như Ví dụ 07.4, $z_y=\operatorname{clip}\big((y+0{,}25)/1{,}85,0,1\big)$. Hai quan sát giống nhau trừ độ cao $y=1{,}7$ và $y=1{,}8$.

**Yêu cầu.** So sánh hai vector đặc trưng.

**Tính.** $(1{,}7+0{,}25)/1{,}85\approx1{,}054$ và $(1{,}8+0{,}25)/1{,}85\approx1{,}108$; cả hai bị cắt về $z_y=1$, nên $z$ và mọi họ đặc trưng cho cùng một vector.

**Diễn giải.** Với mọi $w$, hai quan sát nhận cùng dự đoán, dù tàu ở độ cao $1{,}8$ còn quãng hạ dài hơn.

**Kiểm tra lại.** $1{,}85<1{,}95<2{,}05$, nên cả hai tỉ số vượt $1$.
:::

::: proposition Mệnh đề 07.10 (Nhập nhằng đặc trưng)
**Giả thiết.** $\hat v$ dạng (1.1); $s_1\ne s_2$ có $x(s_1)=x(s_2)$; $\mu(s_1),\mu(s_2)>0$.

**Kết luận.** $\hat v(s_1,w)=\hat v(s_2,w)$ với mọi $w$, và

$$
J_\mu(w)\ \ge\ \frac12\cdot\frac{\mu(s_1)\,\mu(s_2)}{\mu(s_1)+\mu(s_2)}\big(v_\pi(s_1)-v_\pi(s_2)\big)^2\qquad\text{với mọi }w .
\tag{1.5}
$$

**Điều kiện áp dụng.** Mọi dữ liệu và mọi thuật toán.

**Phạm vi.** Khi $v_\pi(s_1)\ne v_\pi(s_2)$, không $w$ nào đúng ở cả hai trạng thái; hiện tượng này gọi là nhập nhằng.
:::

::: proof Chứng minh Mệnh đề 07.10
**Bước 1 (cùng dự đoán).** $\hat v(s_1,w)=x(s_1)^\top w=x(s_2)^\top w=\hat v(s_2,w)=:c$.

**Bước 2 (cận dưới).** Bỏ các số hạng không âm của trạng thái khác trong (1.3): $2J_\mu(w)\ge\mu_1(v_1-c)^2+\mu_2(v_2-c)^2$ với $\mu_i=\mu(s_i)$, $v_i=v_\pi(s_i)$. Vế phải cực tiểu tại $c^*=(\mu_1v_1+\mu_2v_2)/(\mu_1+\mu_2)$, nơi $v_1-c^*=\mu_2(v_1-v_2)/(\mu_1+\mu_2)$ và $v_2-c^*=-\mu_1(v_1-v_2)/(\mu_1+\mu_2)$:

$$
\begin{aligned}
\mu_1(v_1-c^*)^2+\mu_2(v_2-c^*)^2&=\frac{\mu_1\mu_2^2+\mu_2\mu_1^2}{(\mu_1+\mu_2)^2}(v_1-v_2)^2&&\text{(thay hai sai lệch)}\\
&=\frac{\mu_1\mu_2}{\mu_1+\mu_2}(v_1-v_2)^2&&\text{(rút gọn).}
\end{aligned}
$$

Chia cho $2$ được (1.5). $\square$
:::

Với Ví dụ 07.3, vế phải của (1.5) bằng $\tfrac12\cdot\tfrac14\cdot4=\tfrac12$ khi $\mu=(\tfrac12;\tfrac12)$ và $\tfrac38$ khi $\mu=(\tfrac34;\tfrac14)$, đúng các giá trị nhỏ nhất đã tính. Cận (1.5) không chứa dữ liệu, nên không giảm khi thêm dữ liệu.

::: definition Định nghĩa 07.11 (Sai số xấp xỉ và sai số ước lượng)
Trong bối cảnh của Định nghĩa 07.5, sai số xấp xỉ là $\inf_wJ_\mu(w)$. Với tham số $\hat w$ do một thuật toán trả về từ dữ liệu hữu hạn, sai số ước lượng là $J_\mu(\hat w)-\inf_wJ_\mu(w)\ge0$.
:::

Sai số xấp xỉ chỉ phụ thuộc $v_\pi$, $\mu$ và đặc trưng, nên muốn giảm phải đổi đặc trưng; sai số ước lượng đến từ số mẫu, nhiễu và bước học. Nhầm lẫn thường gặp là chạy thuật toán lâu hơn để giảm một sai số do đặc trưng quyết định, như nhập nhằng (Mệnh đề 07.10).

**Trong thực hành.** Trong notebook Flappy Bird (mục 6), bốn họ đặc trưng được huấn luyện bằng Q-learning với cùng hằng $\kappa$ của bước học chuẩn hóa $\alpha=\kappa/\mathbb E\lVert x\rVert^2$ và $4\,000$ lượt. Trên $20$ lượt kiểm định, chính sách tham lam qua trung bình $0{,}00$ ống với họ `der` ($k=5$), $0{,}40$ với `raw` ($k=13$) và $34{,}70$ với Fourier bậc 3 `four3` ($k=256$) (một lần chạy đã nhúng trong notebook). Notebook giải thích kết quả của `der` bằng sai số xấp xỉ: giá trị hành động phụ thuộc phi tuyến vào vị trí của chim trong khe.


::: exercise Bài tập 07.3 (Sai số xấp xỉ của hai trạng thái cùng đặc trưng)
Cho $s_1$, $s_2$ cùng vector đặc trưng, $v_\pi(s_1)=0$, $v_\pi(s_2)=2$, không có trạng thái khác, $\mu=(\beta;1-\beta)$ với $\beta\in(0,1)$.

- (a) Tìm $c^*(\beta)$ và sai số xấp xỉ theo $\beta$.
- (b) Tính hai đại lượng khi $\beta=\tfrac12$.
- (c) Thêm dữ liệu có làm sai số xấp xỉ giảm không.
:::

::: hint
Dùng Mệnh đề 07.10 với $\mu_1=\beta$, $\mu_2=1-\beta$.
:::

::: solution
**(a)** $J_\mu=\tfrac12[\beta c^2+(1-\beta)(2-c)^2]$, đạo hàm $c-2(1-\beta)$, nên $c^*=2(1-\beta)$ và $\inf J_\mu=\tfrac12\big[4\beta(1-\beta)^2+4\beta^2(1-\beta)\big]=2\beta(1-\beta)$, trùng (1.5).

**(b)** $\beta=\tfrac12$: $c^*=1$, sai số xấp xỉ $\tfrac12$.

**(c)** Không: theo Mệnh đề 07.10, $J_\mu(w)\ge2\beta(1-\beta)$ với mọi $w$. Thêm dữ liệu chỉ giảm sai số ước lượng; muốn giảm sai số xấp xỉ phải làm $x(s_1)\ne x(s_2)$.

**Kiểm tra lại.** $\beta=\tfrac34$ cho $c^*=\tfrac12$ và $\tfrac38$, trùng Ví dụ 07.3.
:::

Như vậy, chúng ta đã thay bảng bằng hàm tuyến tính (Định nghĩa 07.1), trong đó một cập nhật lan theo tích vô hướng của các đặc trưng (Mệnh đề 07.2), và đo chất lượng bằng $J_\mu$ (Định nghĩa 07.5) với sai số nhỏ nhất do đặc trưng quyết định (Mệnh đề 07.10). Tuy nhiên, $J_\mu$ chứa $v_\pi$. Trong Mục 2, chúng ta thay $v_\pi$ bằng lợi tức quan sát được và chứng minh phép thay này giữ nguyên điểm cực tiểu.

## 2. Monte Carlo gradient với hàm xấp xỉ

Trên Lunar Lander, tập huấn luyện có $546\,869$ chuyển, trong đó $504\,869$ thuộc lượt kết thúc thật và có lợi tức $G_t$ đầy đủ, nhưng không có giá trị $v_\pi$ nào, nên tiêu chí (1.3) chưa tính được. Để học $w$ từ các lượt đó, chúng ta cần một đại lượng tính được thay cho $v_\pi(S_t)$ và cần biết phép thay có giữ nguyên điểm cực tiểu của $J_\mu$ hay không.

<!-- note-topic-id: lec-07-topic-05 -->
### 2.1 Mục tiêu cập nhật

Một cách trực quan, mỗi mẫu cho một "nhãn" thay cho giá trị thật, như trong học có giám sát, nhưng nhãn do chính sách sinh dữ liệu quyết định, và có khi do cả tham số đang học (bài giảng gốc, trang 27). Mô tả này chưa phải định nghĩa.

::: example Ví dụ 07.7 (Hai mục tiêu cho cùng một mẫu)
**Dữ kiện.** $x(S_t)=(2;1)$, $w=(1;-1)$; lượt chứa $S_t$ có lợi tức $G_t=5$; chuyển sau $S_t$ cho $R_{t+1}=1$ và $x(S_{t+1})=(1;0)$; $\gamma=0{,}9$. Tham số $w'=(1{,}8;-0{,}6)$ là tham số sau cập nhật của Ví dụ 07.8.

**Yêu cầu.** Tính $y^{\mathrm{MC}}=G_t$ và $y^{\mathrm{TD}}(w)=R_{t+1}+\gamma\,x(S_{t+1})^\top w$ tại $w$ và tại $w'$.

**Tính.** $y^{\mathrm{MC}}=5$ ở cả hai tham số; $y^{\mathrm{TD}}(w)=1+0{,}9\cdot1=1{,}9$ và $y^{\mathrm{TD}}(w')=1+0{,}9\cdot1{,}8=2{,}62$.

**Diễn giải.** Lợi tức do quỹ đạo cung cấp, không đổi khi $w$ đổi; mục tiêu TD (còn gọi là mục tiêu một bước) dùng dự đoán hiện tại tại $S_{t+1}$ nên đổi theo $w$.

**Kiểm tra lại.** $x(S_{t+1})^\top w'=1{,}8$.
:::

::: definition Định nghĩa 07.12 (Mục tiêu cập nhật, mất mát mẫu và cập nhật gradient đầy đủ)
Cho trạng thái $S_t$ và số thực $y_t$ tính từ dữ liệu, gọi là mục tiêu cập nhật, dùng thay cho $v_\pi(S_t)$. Mất mát mẫu là $\ell_t(w)=\tfrac12\big(y_t-\hat v(S_t,w)\big)^2$. Lần cập nhật đưa $w_n$ thành $w_{n+1}$, dùng mẫu tại thời điểm $t$ và bước học $\alpha_n>0$, là

$$
w_{n+1}=w_n+\alpha_n\big(y_t-\hat v(S_t,w_n)\big)\nabla_w\hat v(S_t,w_n),
\tag{2.1}
$$

dạng tuyến tính $w_{n+1}=w_n+\alpha_n\big(y_t-x(S_t)^\top w_n\big)x(S_t)$. Khi $y_t$ không phụ thuộc $w$, (2.1) bằng $w_n-\alpha_n\nabla_w\ell_t(w_n)$ và gọi là cập nhật gradient đầy đủ.
:::

Trong (2.1), hiệu $y_t-\hat v(S_t,w_n)$ là sai lệch, $\nabla_w\hat v$ là hướng làm dự đoán tại $S_t$ tăng nhanh nhất, còn $\alpha_n$ quyết định độ dài bước. Chỉ số $n$ đếm số lần cập nhật, khác thời điểm $t$ của mẫu.

Monte Carlo dùng $y_t=G_t$, không chứa $w$, nên là gradient đầy đủ; TD(0) ở Mục 3 dùng $y_t$ chứa $w$ (Định nghĩa 07.21). Trong bài giảng gốc (trang 32), (2.1) mang tên chung hạ gradient ngẫu nhiên (stochastic gradient descent, SGD) hoặc bán gradient.

::: exercise Bài tập 07.4 (Phần của mục tiêu TD phụ thuộc tham số)
Với hàm tuyến tính và $y_t^{\mathrm{TD}}=R_{t+1}+\gamma\,\hat v(S_{t+1},w_n)$:

- viết $y_t^{\mathrm{TD}}$ theo $w_n$ và chỉ ra thành phần phụ thuộc $w_n$;
- giải thích vì sao (2.1) với mục tiêu này khác bước hạ gradient của $\tfrac12\big(R_{t+1}+\gamma x(S_{t+1})^\top w-x(S_t)^\top w\big)^2$.
:::

::: hint
Lấy đạo hàm theo $w$ của biểu thức trong ngoặc, chứa $w$ ở cả hai dự đoán.
:::

::: solution
**Viết tường minh.** $y_t^{\mathrm{TD}}=R_{t+1}+\gamma\,x(S_{t+1})^\top w_n$; số hạng $\gamma\,x(S_{t+1})^\top w_n$ phụ thuộc $w_n$.

**So sánh.** Với $\delta(w)=R_{t+1}+\gamma x(S_{t+1})^\top w-x(S_t)^\top w$, bước hạ gradient là $\alpha_n\delta(w)\big(x(S_t)-\gamma x(S_{t+1})\big)$. Cập nhật (2.1) chỉ giữ $\alpha_n\delta(w)x(S_t)$ và bỏ $-\alpha_n\gamma\delta(w)x(S_{t+1})$, phần đến từ mục tiêu.

**Kiểm tra lại.** Khi $\gamma=0$, mục tiêu không chứa $w$ và hai bước trùng nhau.
:::

<!-- note-topic-id: lec-07-topic-06 -->
### 2.2 Lợi tức và cập nhật Monte Carlo

Mục tiêu Monte Carlo là $y_t=G_t=\sum_{j=0}^{T-t-1}\gamma^jR_{t+j+1}$ (bài giảng gốc, trang 33–34): không bootstrap, không chứa $w$, nhưng chỉ biết khi lượt kết thúc.

::: proposition Mệnh đề 07.13 (Lợi tức là mục tiêu không chệch)
**Giả thiết.** $\pi$ cố định; $G_t$ có kỳ vọng hữu hạn; $w$ cố định, không phụ thuộc lượt chứa $S_t$.

**Kết luận.** $\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s)$, nhắc lại từ ghi chú Bài 03, Mục 3; và $\mathbb E_\pi\big[(G_t-\hat v(S_t,w))\,x(S_t)\mid S_t=s\big]=\big(v_\pi(s)-\hat v(s,w)\big)x(s)$.

**Điều kiện áp dụng.** Lợi tức sinh bởi chính $\pi$.

**Phạm vi.** Nói về từng mẫu, không về tham số học từ hữu hạn mẫu.
:::

::: proof Chứng minh Mệnh đề 07.13
Đẳng thức thứ nhất là định nghĩa của $v_\pi$. Khi $S_t=s$, $\hat v(s,w)$ và $x(s)$ là hằng số, nên kỳ vọng có điều kiện chỉ tác động lên $G_t$. $\square$
:::

Trước khi viết thuật toán, chúng ta thực hiện một cập nhật bằng tay.

::: example Ví dụ 07.8 (Một cập nhật Monte Carlo)
**Dữ kiện.** Trạng thái hai đặc trưng $S_t$ với $x(S_t)=(2;1)$; $w_n=(1;-1)$; $G_t=5$; $\alpha=0{,}1$.

**Yêu cầu.** Tính $w_{n+1}$ theo (2.1) với $y_t=G_t$ và dự đoán mới tại $S_t$.

**Tính.**

$$
\begin{aligned}
\text{dự đoán: }&\hat v(S_t,w_n)=2-1=1,\\
\text{mục tiêu và sai lệch: }&y_t=5,\qquad e_t=5-1=4,\\
\text{tham số mới: }&w_{n+1}=(1;-1)+0{,}1\cdot4\cdot(2;1)=(1{,}8;-0{,}6).
\end{aligned}
$$

Dự đoán mới là $3{,}6-0{,}6=3$.

**Diễn giải.** Lợi tức lớn hơn dự đoán nên $w$ dịch theo hướng $x(S_t)$; sai lệch giảm từ $4$ xuống $2$; lợi tức không được tính lại.

**Kiểm tra lại.** Theo Mệnh đề 07.2, dự đoán tăng $\alpha e_t\lVert x(S_t)\rVert^2=0{,}1\cdot4\cdot5=2$.
:::

![Mặt phẳng tham số. Từ gốc O vẽ vector w_n = (1; −1) và vector đặc trưng x(S_t) = (2; 1) nét đứt. Từ đầu mút của w_n, mũi tên dài 0,4·x(S_t) dẫn tới w_{n+1} = (1,8; −0,6).](img/lec-07/mc-update-vector.svg)

Hình trên vẽ Ví dụ 07.8 trong mặt phẳng tham số. Bước song song với $x(S_t)$, gradient của dự đoán, và dài $0{,}4$ lần vector đó. Dự đoán dịch một phần $\alpha\lVert x(S_t)\rVert^2=0{,}5$ của sai lệch; khi tích này lớn hơn $1$, bước vượt qua mục tiêu (Bài tập 07.10).

::: proposition Mệnh đề 07.14 (Cập nhật Monte Carlo là bước hạ gradient ngẫu nhiên trên $J_\mu$)
**Giả thiết.** $\hat v$ dạng (1.1); $\pi$ cố định; $S_t\sim\mu$; $G_t$ là lợi tức sau $S_t$ theo $\pi$, kỳ vọng hữu hạn; $w$ không phụ thuộc mẫu $(S_t,G_t)$.

**Kết luận.** $\nabla_w\ell_t(w)=-\big(G_t-x(S_t)^\top w\big)x(S_t)$ và $\mathbb E[\nabla_w\ell_t(w)]=\nabla J_\mu(w)$.

**Điều kiện áp dụng.** Phân phối của $S_t$ phải đúng là trọng số $\mu$ của $J_\mu$.

**Phạm vi.** Hướng trung bình của một bước; hội tụ là Định lý 07.17.
:::

::: proof Chứng minh Mệnh đề 07.14
**Bước 1 (gradient mẫu).** $G_t$ không phụ thuộc $w$, nên quy tắc chuỗi cho $\nabla_w\tfrac12(G_t-x(S_t)^\top w)^2=-(G_t-x(S_t)^\top w)x(S_t)$.

**Bước 2 (kỳ vọng).**

$$
\begin{aligned}
\mathbb E[\nabla_w\ell_t(w)]&=-\textstyle\sum_s\mu(s)\,\mathbb E_\pi\big[(G_t-x(s)^\top w)x(s)\mid S_t=s\big]&&\text{(kỳ vọng lặp, }S_t\sim\mu)\\
&=-\textstyle\sum_s\mu(s)\big(v_\pi(s)-x(s)^\top w\big)x(s)&&\text{(Mệnh đề 07.13)}\\
&=\nabla J_\mu(w)&&\text{(đạo hàm (1.3)).}\ \square
\end{aligned}
$$
:::

Mệnh đề 07.14 nói rằng Monte Carlo là SGD trên $J_\mu$; một mục tiêu có kỳ vọng khác $v_\pi(S_t)$ sẽ cho hướng trung bình khác $-\nabla J_\mu$. Thuật toán sau cập nhật tại mọi lần ghé (every-visit) của trạng thái trong lượt.

::: algorithm Thuật toán 07.15 (Monte Carlo gradient tuyến tính, mọi lần ghé)
**Đầu vào.** Chính sách $\pi$; đặc trưng $x$; $\gamma$; số lượt $K$; dãy bước học $(\alpha_n)$.

**Đầu ra.** $w\in\mathbb R^d$ và $\hat v(\cdot,w)=x(\cdot)^\top w$.

**Giả thiết.** Mọi lượt dùng được kết thúc sau hữu hạn bước; $\pi$ không đổi.

**Khởi tạo.** $w\leftarrow w_0$, $n\leftarrow0$.

**Tham số.** $K$, $(\alpha_n)$.

1. Với mỗi lượt $i=1,\dots,K$, sinh $S_0,R_1,\dots,R_T,S_T$ theo $\pi$. Nếu lượt bị cắt ngắn (truncation) vì giới hạn số bước trước khi gặp trạng thái kết thúc, bỏ lượt đó vì lợi tức chưa đầy đủ.
2. Tính lùi: $G_T\leftarrow0$; với $t=T-1,\dots,0$: $G_t\leftarrow R_{t+1}+\gamma G_{t+1}$.
3. Với $t=0,\dots,T-1$ theo thứ tự: $e_t\leftarrow G_t-x(S_t)^\top w$; $w\leftarrow w+\alpha_ne_t\,x(S_t)$; $n\leftarrow n+1$.

**Điều kiện dừng.** Sau $K$ lượt; kết thúc một lượt khác dừng thuật toán.

**Chi phí mỗi bước.** Tỉ lệ số thành phần khác $0$ của $x(S_t)$; bộ nhớ $d$ tham số và phần thưởng của lượt.
:::

Bước 3 với dữ kiện của Ví dụ 07.8 cho đúng $w=(1{,}8;-0{,}6)$. Các cập nhật trong một lượt diễn ra tuần tự; muốn dùng lần ghé đầu tiên (first-visit), chỉ cập nhật tại lần ghé đầu tiên của trạng thái trong lượt (ghi chú Bài 05, Mục 2).

Giải bình phương tối thiểu trên toàn bộ dữ liệu cho Monte Carlo theo lô, gần bài toán hồi quy (bài giảng gốc, trang 33); Sutton và Barto (2018, §9.3, tr. 202) có cùng thuật toán với tên Gradient Monte Carlo.

**Trong thực hành.** Trong notebook Lunar Lander (mục 6), bước học là hằng $\alpha=\kappa/\mathbb E\lVert x(S)\rVert^2$, giữ mức dịch của dự đoán ở cỡ $\kappa$ lần sai lệch bất kể số chiều (Sutton và Barto, 2018, §9.6). Bước 1 bỏ $42$ lượt bị cắt ngắn. Một lượt qua dữ liệu với Fourier bậc 3 cho $J_{\mathrm{kt}}=2\,190{,}1$ (một lần chạy đã nhúng trong notebook).

<!-- note-topic-id: lec-07-topic-15 -->
### 2.3 Hội tụ của Monte Carlo tuyến tính

Mỗi bước đi đúng hướng theo trung bình; còn phải biết dãy tham số dừng ở đâu khi mỗi bước dùng một mục tiêu có nhiễu. Bổ đề sau cho thấy nhiễu của $G_t$ không làm dịch điểm cực tiểu.

::: lemma Bổ đề 07.16 (Phân tích phương sai và độ lệch)
**Giả thiết.** Như Mệnh đề 07.14, với $\mathbb E[G_t^2]<\infty$.

**Kết luận.** $\mathbb E\big[(G_t-\hat v(S_t,w))^2\big]=\sum_s\mu(s)\,\mathrm{Var}(G_t\mid S_t=s)+2J_\mu(w)$.

**Điều kiện áp dụng.** $\mathbb E[G_t\mid S_t=s]=v_\pi(s)$.

**Phạm vi.** Số hạng phương sai không phụ thuộc $w$, nên mất mát kỳ vọng và $J_\mu$ có cùng điểm cực tiểu.
:::

::: proof Chứng minh Bổ đề 07.16
Cố định $S_t=s$, áp dụng hệ thức phương sai với $X=G_t$, $c=\hat v(s,w)$, rồi Mệnh đề 07.13:

$$
\begin{aligned}
\mathbb E\big[(G_t-\hat v(s,w))^2\mid S_t=s\big]&=\mathrm{Var}(G_t\mid S_t=s)+\big(\mathbb E[G_t\mid S_t=s]-\hat v(s,w)\big)^2&&\text{(hệ thức phương sai)}\\
&=\mathrm{Var}(G_t\mid S_t=s)+\big(v_\pi(s)-\hat v(s,w)\big)^2&&\text{(Mệnh đề 07.13).}
\end{aligned}
$$

Lấy trung bình theo $\mu$ và dùng (1.3). $\square$
:::

Định lý sau là phát biểu của bài giảng gốc (trang 34) với đủ giả thiết; nó cần Mệnh đề 07.14 cho hướng trung bình và Bổ đề 07.16 cho điểm đích.

::: theorem Định lý 07.17 (Hội tụ của Monte Carlo gradient tuyến tính)
**Giả thiết.**

1. $\pi$ và $\mu$ cố định.
2. Lần cập nhật đưa $w_n$ thành $w_{n+1}$ dùng mẫu $(S^{(n)},G^{(n)})$ độc lập với các mẫu trước, $S^{(n)}\sim\mu$, $G^{(n)}$ là lợi tức sau $S^{(n)}$ theo $\pi$.
3. Đặc trưng bị chặn; $\mathbb E[(G^{(n)})^2]<\infty$.
4. $\Sigma_\mu=\sum_s\mu(s)x(s)x(s)^\top$ xác định dương.
5. Bước học xác định trước, thỏa Robbins–Monro.

**Kết luận.** $J_\mu$ có cực tiểu duy nhất $w_{\mathrm{MC}}=\Sigma_\mu^{-1}\sum_s\mu(s)x(s)v_\pi(s)$, và $w_n\to w_{\mathrm{MC}}$ hầu chắc chắn. Khi $\mathcal S$ hữu hạn và $\mu>0$, $\Phi w_{\mathrm{MC}}$ là hình chiếu của $v_\pi$ lên lớp biểu diễn theo $\lVert\cdot\rVert_\mu$.

**Điều kiện áp dụng.** Mẫu trong một lượt của Thuật toán 07.15 phụ thuộc nhau, nên định lý không áp dụng nguyên văn; trường hợp đó cần một phiên bản khác, không trình bày ở đây.

**Phạm vi.** $\Phi w_{\mathrm{MC}}=v_\pi$ chỉ khi $v_\pi$ thuộc lớp biểu diễn.
:::

::: proof Chứng minh Định lý 07.17
**Bước 1 (cực tiểu duy nhất).** $J_\mu(w)=\tfrac12w^\top\Sigma_\mu w-w^\top\sum_s\mu(s)x(s)v_\pi(s)+\text{hằng số}$ có Hessian $\Sigma_\mu$ xác định dương (giả thiết 4), nên lồi chặt, với cực tiểu duy nhất là nghiệm của $\Sigma_\mu w=\sum_s\mu(s)x(s)v_\pi(s)$.

**Bước 2 (cùng điểm cực tiểu).** Theo Bổ đề 07.16, mất mát kỳ vọng bằng $2J_\mu$ cộng hằng số.

**Bước 3 (hội tụ).** Theo Mệnh đề 07.14, $w_{n+1}=w_n-\alpha_n(\nabla J_\mu(w_n)+\xi_n)$, với nhiễu $\xi_n$ có kỳ vọng $0$ khi biết quá khứ (giả thiết 2) và phương sai bị chặn bởi $C(1+\lVert w_n\rVert^2)$ với một hằng số $C$ (giả thiết 3). Vì $\Sigma_\mu$ xác định dương, $\lVert w\rVert^2\le c'(1+\lVert\nabla J_\mu(w)\rVert^2)$ với hằng số $c'$, nên cận có dạng $K_1+K_2\lVert\nabla J_\mu(w_n)\rVert^2$. Với cận này và bước Robbins–Monro, kết quả về gradient ngẫu nhiên ở Bertsekas và Tsitsiklis (1996), chương 4, cho $\nabla J_\mu(w_n)\to0$ hầu chắc chắn, tức $w_n\to w_{\mathrm{MC}}$; chứng minh kết quả đó nằm ngoài phạm vi học phần (xem thêm Sutton và Barto, 2018, §9.3, tr. 202). Ý tưởng: bỏ nhiễu, phép lặp $w\leftarrow w-\alpha\Sigma_\mu(w-w_{\mathrm{MC}})$ co về $w_{\mathrm{MC}}$; hai điều kiện Robbins–Monro cho quãng đường đủ dài và tổng nhiễu hội tụ.

**Bước 4 (hình chiếu).** Với $D_\mu=\operatorname{diag}(\mu)$, phương trình ở Bước 1 là $\Phi^\top D_\mu(v_\pi-\Phi w_{\mathrm{MC}})=0$: phần dư trực giao với mọi cột của $\Phi$ theo trọng số $\mu$, đúng điều kiện của hình chiếu. $\square$
:::

Mỗi giả thiết có vai trò riêng, và bỏ một giả thiết thì kết luận có thể sai.

- Bỏ "$\pi$, $\mu$ cố định": tiêu chí đổi theo thời gian, không còn đích cố định; đây là tình huống của Mục 4.
- Bỏ "$\Sigma_\mu$ xác định dương": với mã hóa bốn khối (Nhận xét 07.9), $J_\mu$ có cả một tập cực tiểu.
- Bỏ $\sum_n\alpha_n^2<\infty$: với bước hằng, $w_n$ dao động quanh $w_{\mathrm{MC}}$.
- Bỏ $\sum_n\alpha_n=\infty$: với $\alpha_n=1/(n+1)^2$, tổng các bước hữu hạn, nên $w_n$ có thể dừng trước $w_{\mathrm{MC}}$.

Bước 1 dùng giả thiết 4, Bước 2 dùng việc lợi tức sinh bởi $\pi$, Bước 3 dùng giả thiết 2, 3, 5. So với hội tụ dạng bảng của Bài 05, định lý đổi đích: bảng tiến tới $v_\pi$ ở mỗi ô, hàm tuyến tính tiến tới hình chiếu của $v_\pi$.

::: remark Nhận xét 07.18 (Điều kiện Robbins–Monro với tham số dùng chung)
Nhắc lại (ghi chú Bài 05, Mục 2 và Mục 4): $\sum_n\alpha_n=\infty$ giữ cho thuật toán còn học tới đích, $\sum_n\alpha_n^2<\infty$ làm nhiễu tích lũy tắt dần. Điểm mới là nhiễu $\xi_n$ là vector trong $\mathbb R^d$ dùng chung cho mọi trạng thái, với phương sai có thể tăng theo $\lVert w_n\rVert^2$; bước Robbins–Monro vì thế phải đi kèm cận $C(1+\lVert w_n\rVert^2)$ như ở Bước 3 của chứng minh Định lý 07.17.
:::

**Trong thực hành.** Trong notebook Lunar Lander (mục 8), Monte Carlo theo lô giải phương trình chuẩn $\big(\sum_tx_tx_t^\top\big)w=\sum_tx_tG_t$ trên các lượt kết thúc thật. Với Fourier bậc 3, nghiệm cho $J_{\mathrm{kt}}=1\,481{,}0$, thấp hơn $1\,626{,}8$ của bảng $9\,216$ ô và $2\,190{,}1$ của một lượt với bước hằng; các số là một lần chạy đã nhúng trong notebook. Một lượt với bước hằng nhỏ chưa tới nghiệm; bước hằng cũng không thỏa Robbins–Monro.

::: exercise Bài tập 07.5 (Đạo hàm cập nhật Monte Carlo)
Cho $\hat v(s,w)=x(s)^\top w$ và $\ell_t(w)=\tfrac12\big(G_t-x(S_t)^\top w\big)^2$. Đây là Bài tập tuần 7 (2025–2026), bài 4; phiếu viết $\phi(s)$ cho $x(s)$.

- (a) Tính $\nabla_w\ell_t(w)$.
- (b) Suy ra một bước hạ gradient với bước học $\alpha_n$ và chứng minh nó trùng (2.1) với $y_t=G_t$.
- (c) Tính Hessian, chứng minh $\ell_t$ lồi và nêu điều kiện để cập nhật hội tụ về cực tiểu toàn cục của $J_\mu$.
:::

::: hint
Quy tắc chuỗi, với $G_t$ không phụ thuộc $w$; với (c), xét $z^\top x(S_t)x(S_t)^\top z$ và Định lý 07.17.
:::

::: solution
**(a)** $\nabla_w\ell_t(w)=-\big(G_t-x(S_t)^\top w\big)x(S_t)$; đây là gradient đầy đủ vì $G_t$ không chứa $w$.

**(b)** $w_{n+1}=w_n-\alpha_n\nabla_w\ell_t(w_n)=w_n+\alpha_n\big(G_t-x(S_t)^\top w_n\big)x(S_t)$, đúng (2.1).

**(c)** $\nabla^2_w\ell_t=x(S_t)x(S_t)^\top$ và $z^\top x(S_t)x(S_t)^\top z=(x(S_t)^\top z)^2\ge0$, nên $\ell_t$ lồi. Theo Định lý 07.17, cập nhật hội tụ hầu chắc chắn tới $w_{\mathrm{MC}}$ khi:

- $\pi$, $\mu$ cố định;
- mẫu độc lập với $S_t\sim\mu$;
- đặc trưng bị chặn và $\mathbb E[G_t^2]<\infty$;
- $\Sigma_\mu$ xác định dương;
- bước học thỏa Robbins–Monro.

Bài giảng gốc (trang 34) nêu ba điều kiện: iid, đặc trưng bị chặn, Robbins–Monro.

**Kiểm tra lại.** Với Ví dụ 07.8, (b) cho $(1{,}8;-0{,}6)$.
:::

::: exercise Bài tập 07.6 (Điều kiện Robbins–Monro)
Giải thích vì sao $\sum_n\alpha_n=\infty$ giữ cho Monte Carlo và TD có xấp xỉ hàm còn học được, còn $\sum_n\alpha_n^2<\infty$ giữ nhiễu tích lũy hữu hạn. Đây là Bài tập tuần 7 (2025–2026), bài 6.
:::

::: hint
Xét quãng đường $w$ đi được khi mỗi cập nhật bị chặn, và phương sai của tổng nhiễu có trọng số.
:::

::: solution
**Điều kiện thứ nhất.** Nếu mỗi cập nhật bị chặn bởi $M$, quãng đường $w$ đi được không vượt $M\sum_n\alpha_n$; tổng hữu hạn thì khởi tạo đủ xa sẽ không tới nghiệm.

**Điều kiện thứ hai.** Với nhiễu không tương quan, phương sai bị chặn bởi $\sigma^2$, phương sai của $\sum_n\alpha_n\xi_n$ không vượt $\sigma^2\sum_n\alpha_n^2$. Với hàm xấp xỉ, cận $\sigma^2$ được thay bằng $C(1+\lVert w_n\rVert^2)$ (Nhận xét 07.18); khi đó cần thêm lập luận rằng $w_n$ không tiến ra vô cùng, và kết quả dẫn ở Bước 3 của chứng minh Định lý 07.17 xử lý điều đó.

**Kiểm tra lại.** $\alpha_n=1/(n+1)$ thỏa cả hai; bước hằng chỉ thỏa điều kiện thứ nhất.
:::

Như vậy, chúng ta đã thay $v_\pi(S_t)$ bằng lợi tức (Mệnh đề 07.13), chứng minh cập nhật là SGD trên $J_\mu$ (Mệnh đề 07.14), và phát biểu kèm nguồn rằng với mẫu độc lập, bước Robbins–Monro, tham số hội tụ tới hình chiếu $w_{\mathrm{MC}}$ của $v_\pi$ (Định lý 07.17). Tuy nhiên, $G_t$ chỉ có khi lượt kết thúc. Trong Mục 3, chúng ta thay phần lợi tức chưa quan sát bằng dự đoán hiện tại.

## 3. TD(0) bán gradient và điểm cố định Bellman chiếu

Thuật toán 07.15 bỏ $42$ lượt bị cắt ngắn của Lunar Lander, chiếm $7{,}7\%$ số chuyển, và mỗi cập nhật chờ tới cuối lượt. TD(0) dạng bảng (ghi chú Bài 05, Mục 3) cập nhật ngay bằng $R_{t+1}+\gamma V(S_{t+1})$; với hàm tuyến tính, mục tiêu đó chứa $w$ (Ví dụ 07.7), nên Định lý 07.17 không còn áp dụng, và chúng ta cần biết cập nhật mới hướng tới đâu.

<!-- note-topic-id: lec-07-topic-07 -->
### 3.1 Mục tiêu TD và cập nhật bán gradient

Về mặt ý tưởng, vì $G_t=R_{t+1}+\gamma G_{t+1}$, ta giữ phần thưởng vừa nhận và thay $G_{t+1}$ bằng dự đoán hiện tại $\hat v(S_{t+1},w)$, rồi cập nhật ngay sau chuyển; mục tiêu nhận được là mục tiêu TD của Ví dụ 07.7. Mô tả này chưa phải định nghĩa; ví dụ sau thực hiện một cập nhật.

::: example Ví dụ 07.9 (Một cập nhật TD(0))
**Dữ kiện.** Trạng thái hai đặc trưng với $x(S_t)=(1;2)$, $x(S_{t+1})=(2;0)$; $w_n=(0{,}5;1)$; $R_{t+1}=1$; $\gamma=0{,}9$; $\alpha=0{,}1$.

**Yêu cầu.** Tính mục tiêu, sai số TD, tham số mới và mục tiêu tính lại bằng tham số mới.

**Tính.** Hai dự đoán dùng $w_n$, tính trước khi cập nhật: $\hat v(S_t,w_n)=2{,}5$, $\hat v(S_{t+1},w_n)=1$.

$$
\begin{aligned}
\text{mục tiêu: }&y_t=1+0{,}9\cdot1=1{,}9,\\
\text{sai số TD: }&\delta_t=1{,}9-2{,}5=-0{,}6,\\
\text{tham số mới: }&w_{n+1}=(0{,}5;1)+0{,}1\cdot(-0{,}6)\cdot(1;2)=(0{,}44;0{,}88).
\end{aligned}
$$

**Diễn giải.** Dự đoán mới tại $S_t$ là $2{,}2$, giảm về phía $1{,}9$; vector cập nhật là $x(S_t)$, không phải $x(S_{t+1})$. Mục tiêu cũng đổi: tính lại bằng $w_{n+1}$ được $1+0{,}9\cdot0{,}88=1{,}792$.

**Kiểm tra lại.** Theo Mệnh đề 07.2, dự đoán tại $S_t$ đổi $0{,}1\cdot(-0{,}6)\cdot5=-0{,}3$.
:::

::: definition Định nghĩa 07.19 (Mục tiêu TD(0) và sai số TD)
Với chuyển $(S_t,R_{t+1},S_{t+1})$ dùng trong lần cập nhật từ $w_n$,

$$
y_t=R_{t+1}+\gamma\,\hat v(S_{t+1},w_n),\qquad \delta_t=y_t-\hat v(S_t,w_n),
\tag{3.1}
$$

với $\hat v(S_{t+1},w_n)=0$ khi $S_{t+1}$ là trạng thái kết thúc.
:::

Mục tiêu (3.1) là mục tiêu bootstrap; với đặc trưng chỉ thị (Hệ quả 07.3) nó trùng mục tiêu TD(0) dạng bảng. Khác lợi tức (Mệnh đề 07.13), nó nói chung không có kỳ vọng $v_\pi(S_t)$.

::: proposition Mệnh đề 07.20 (Độ chệch của mục tiêu TD)
**Giả thiết.** $\pi$ cố định; $w$ không phụ thuộc chuyển đang xét.

**Kết luận.** $\mathbb E_\pi[y_t\mid S_t=s]-v_\pi(s)=\gamma\,\mathbb E_\pi\big[\hat v(S_{t+1},w)-v_\pi(S_{t+1})\mid S_t=s\big]$, với cả hai giá trị bằng $0$ tại trạng thái kết thúc.

**Điều kiện áp dụng.** Chuyển sinh bởi $\pi$.

**Phạm vi.** Độ chệch bằng $0$ khi $\hat v(\cdot,w)=v_\pi$ trên các trạng thái kế tiếp; nói chung khác $0$.
:::

::: proof Chứng minh Mệnh đề 07.20
Phương trình Bellman kỳ vọng (ghi chú Bài 03, Mục 4) cho $v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s]$. Trừ đẳng thức này khỏi kỳ vọng của (3.1), số hạng $R_{t+1}$ triệt tiêu. $\square$
:::

Đổi lại độ chệch, mục tiêu TD cho cập nhật ngay sau chuyển và chỉ chứa một phần thưởng ngẫu nhiên, nên thường có phương sai nhỏ hơn lợi tức (bài giảng gốc, trang 35).

::: definition Định nghĩa 07.21 (Cập nhật bán gradient)
Khi $y_t$ phụ thuộc $w$ qua ước lượng hiện tại, cập nhật (2.1) với $y_t$ tính bằng $w_n$ và giữ cố định khi lấy đạo hàm gọi là cập nhật bán gradient. Với TD(0) tuyến tính,

$$
w_{n+1}=w_n+\alpha_n\,\delta_t\,x(S_t),\qquad \delta_t=R_{t+1}+\gamma\,x(S_{t+1})^\top w_n-x(S_t)^\top w_n .
\tag{3.2}
$$
:::

Gradient đầy đủ của $\tfrac12\delta_t(w)^2$ cho bước $\alpha_n\delta_t\big(x(S_t)-\gamma x(S_{t+1})\big)$; (3.2) bỏ $-\alpha_n\gamma\delta_tx(S_{t+1})$, phần đến từ mục tiêu. Đó là hiện tượng của Ví dụ 07.9: mục tiêu đổi từ $1{,}9$ thành $1{,}792$ khi $w$ đổi, và cập nhật bỏ qua sự thay đổi này (Sutton và Barto, 2018, §9.3, tr. 202–203).

Vì vậy (3.2) không giảm một mất mát cố định. Nhầm lẫn thường gặp là nghĩ bán gradient là tính chất của dạng hàm; tên này chỉ nói đạo hàm bỏ qua đường đi qua mục tiêu.

::: algorithm Thuật toán 07.22 (TD(0) bán gradient tuyến tính)
**Đầu vào.** Chính sách $\pi$; đặc trưng $x$; $\gamma$; ngân sách $N$ chuyển; dãy bước học $(\alpha_n)$; giới hạn số bước mỗi lượt, nếu có.

**Đầu ra.** $w\in\mathbb R^d$.

**Giả thiết.** $\pi$ không đổi; dữ liệu sinh bởi $\pi$.

**Khởi tạo.** $w\leftarrow w_0$; trạng thái đầu $S$ của một lượt.

**Tham số.** $N$, $(\alpha_n)$.

1. Với $n=0,\dots,N-1$: chọn $A\sim\pi(\cdot\mid S)$, thực hiện, quan sát $R$, $S'$.
2. Nếu $S'$ là trạng thái kết thúc: $y\leftarrow R$; ngược lại: $y\leftarrow R+\gamma\,x(S')^\top w$.
3. $\delta\leftarrow y-x(S)^\top w$; $w\leftarrow w+\alpha_n\delta\,x(S)$; $y$ và $\delta$ dùng $w$ trước cập nhật.
4. Nếu $S'$ kết thúc, hoặc lượt đạt giới hạn số bước (khi đó $y$ ở bước 2 vẫn có bootstrap): lấy trạng thái đầu của lượt mới; ngược lại: $S\leftarrow S'$.

**Điều kiện dừng.** Sau $N$ chuyển; một $\delta$ nhỏ ở một mẫu không chứng tỏ hội tụ.

**Chi phí mỗi bước.** Tỉ lệ với số thành phần khác $0$ của $x(S)$ và $x(S')$; bộ nhớ $d$ tham số.
:::

Bước 2 và 3 với dữ kiện của Ví dụ 07.9 cho đúng $y=1{,}9$, $\delta=-0{,}6$, $w=(0{,}44;0{,}88)$ (Sutton và Barto, 2018, §9.3, tr. 203).

::: remark Nhận xét 07.23 (Kết thúc lượt, cắt ngắn và dừng thuật toán)
Lượt kết thúc khi gặp trạng thái kết thúc, và $y=R$. Lượt bị cắt ngắn khi bị dừng vì giới hạn số bước trong khi trạng thái chưa kết thúc; khi đó mục tiêu vẫn bootstrap từ $x(S')^\top w$. Thuật toán dừng khi hết ngân sách. Coi lượt cắt ngắn là kết thúc thật sẽ gán giá trị tiếp nối $0$ sai.
:::

**Trong thực hành.** Hai notebook cắt ngắn lượt, ở $1\,000$ bước với Lunar Lander và ở $50$ ống với Flappy Bird, và vẫn bootstrap tại bước cắt ngắn; nhờ vậy TD dùng được $42$ lượt mà Monte Carlo bỏ. Một lượt qua dữ liệu Lunar Lander cho $J_{\mathrm{kt}}=1\,855{,}2$, so với $2\,190{,}1$ của Monte Carlo (một lần chạy đã nhúng trong notebook).

::: exercise Bài tập 07.7 (Số hạng bị bỏ trong một cập nhật TD(0))
Với $x(S_t)=(1;2)$, $x(S_{t+1})=(2;0)$, $w_n=(0{,}5;1)$, $R_{t+1}=1$, $\gamma=0{,}9$ của Ví dụ 07.9, tính phần cập nhật bán gradient giữ lại $\delta_tx(S_t)$, số hạng bị bỏ $\gamma\delta_tx(S_{t+1})$, và hướng giảm đầy đủ $\delta_t\big(x(S_t)-\gamma x(S_{t+1})\big)$.
:::

::: hint
$\delta_t=-0{,}6$ (Ví dụ 07.9).
:::

::: solution
**Tính.** Giữ lại: $(-0{,}6;-1{,}2)$. Bị bỏ: $0{,}9\cdot(-0{,}6)\cdot(2;0)=(-1{,}08;0)$. Hướng đầy đủ: $(-0{,}6;-1{,}2)-(-1{,}08;0)=(0{,}48;-1{,}2)$.

**Diễn giải.** Hai hướng ngược dấu ở thành phần thứ nhất: tăng $[w]_1$ làm mục tiêu tăng nhanh hơn dự đoán tại $S_t$, điều mà bán gradient bỏ qua.

**Kiểm tra lại.** $(-0{,}6;-1{,}2)-(0{,}48;-1{,}2)=(-1{,}08;0)$.
:::

<!-- note-topic-id: lec-07-topic-08 -->
### 3.2 Điểm cố định Bellman chiếu

Vì (3.2) không giảm một mất mát cố định, chúng ta tìm điểm dừng của nó qua bước cập nhật trung bình. Với $\mathcal S$ hữu hạn, trung bình của mục tiêu TD tại $s$ là $r_\pi(s)+\gamma\sum_{s'}P_\pi(s,s')x(s')^\top w$, tức thành phần thứ $s$ của $T_\pi(\Phi w)$. Một cách trực quan, TD kéo $\Phi w$ về phía $T_\pi(\Phi w)$; vector này thường nằm ngoài lớp biểu diễn, nên điểm đạt được là điểm gần nó nhất trong lớp. Mô tả này chưa phải định nghĩa.

::: example Ví dụ 07.10 (Hình chiếu lên một đường thẳng)
**Dữ kiện.** Lớp biểu diễn gồm các vector $\lambda f$ với $f=(1;1)$ và $\lambda\in\mathbb R$; vector $h=(2;0)$ nằm ngoài lớp.

**Yêu cầu.** Tìm điểm của lớp gần $h$ nhất theo khoảng cách Euclid.

**Tính.** $\frac{f^\top h}{f^\top f}f=\frac22(1;1)=(1;1)$.

**Diễn giải.** Phần dư $(1;-1)$ vuông góc với lớp.

**Kiểm tra lại.** $\lVert h-\lambda f\rVert^2=(2-\lambda)^2+\lambda^2$ bằng $2$ tại $\lambda=1$ và $4$ tại $\lambda=0$ hay $\lambda=2$.
:::

![Mặt phẳng là lớp biểu diễn gồm các vector Φw. Từ điểm Φw trong lớp, toán tử Bellman T_π cho điểm T_π(Φw) nằm phía trên, ngoài lớp. Đường nét đứt vuông góc hạ từ điểm đó xuống lớp, cho hình chiếu Π_D T_π(Φw).](img/lec-07/projected-bellman.svg)

Hình trên vẽ một bước của cơ chế: $T_\pi$ đưa $\Phi w$ ra khỏi lớp, phép chiếu đưa kết quả trở lại; với TD, phép chiếu dùng trọng số $d_\pi$ (Mệnh đề 07.25).

::: definition Định nghĩa 07.24 (Phép chiếu có trọng số và toán tử Bellman chiếu)
Cho $\mathcal S$ hữu hạn, $d_\pi(s)>0$ với mọi $s$, $D=\operatorname{diag}(d_\pi)$ và $\Phi$ có các cột độc lập tuyến tính. Phép chiếu lên lớp biểu diễn theo $\lVert\cdot\rVert_D$ là $\Pi_D=\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top D$: với mỗi $v\in\mathbb R^{\lvert\mathcal S\rvert}$, $\Pi_Dv$ là vector $\Phi w$ gần $v$ nhất theo $\lVert\cdot\rVert_D$. Toán tử Bellman chiếu là $\Pi_DT_\pi$; tham số $w$ với $\Phi w=\Pi_DT_\pi(\Phi w)$ gọi là điểm cố định Bellman chiếu.
:::

$\Phi^\top D\Phi$ khả nghịch vì $z^\top\Phi^\top D\Phi z=\lVert\Phi z\rVert_D^2>0$ khi $z\ne0$. Hình chiếu được đặc trưng bởi $\Phi^\top D(v-\Pi_Dv)=0$. Khác điểm cố định $v_\pi$ của $T_\pi$ (ghi chú Bài 04, Mục 1), điểm cố định Bellman chiếu nằm trong lớp biểu diễn, và nói chung khác cả $v_\pi$ lẫn $\Pi_Dv_\pi$.

::: proposition Mệnh đề 07.25 (Hướng cập nhật trung bình của TD(0))
**Giả thiết.** $\mathcal S$ hữu hạn; chuỗi trạng thái dưới $\pi$ có phân phối dừng $d_\pi$; $S_t\sim d_\pi$ và $(R_{t+1},S_{t+1})$ sinh theo $\pi$; $w$ cố định.

**Kết luận.** Với $A=\Phi^\top D(I-\gamma P_\pi)\Phi$, $b=\Phi^\top Dr_\pi$:

$$
\mathbb E\big[\delta_t\,x(S_t)\big]=\Phi^\top D\big(T_\pi(\Phi w)-\Phi w\big)=b-Aw .
\tag{3.3}
$$

**Điều kiện áp dụng.** Dữ liệu theo chính sách; trọng số $d_\pi$ là tần suất cập nhật dài hạn.

**Phạm vi.** Hướng trung bình của một bước với $w$ cố định.
:::

::: proof Chứng minh Mệnh đề 07.25
**Bước 1 (điều kiện theo $S_t$).** $\mathbb E[\delta_tx(S_t)\mid S_t=s]=x(s)\big((T_\pi\Phi w)(s)-(\Phi w)(s)\big)$, vì $x(s)$ là hằng số khi biết $S_t=s$.

**Bước 2 (trung bình theo $d_\pi$).**

$$
\begin{aligned}
\mathbb E[\delta_tx(S_t)]&=\textstyle\sum_sd_\pi(s)\,x(s)\big((T_\pi\Phi w)(s)-(\Phi w)(s)\big)&&\text{(kỳ vọng lặp)}\\
&=\Phi^\top D\big(r_\pi+\gamma P_\pi\Phi w-\Phi w\big)&&\text{(hàng của }\Phi\text{; định nghĩa }T_\pi)\\
&=b-Aw&&\text{(nhóm số hạng chứa }w).\ \square
\end{aligned}
$$
:::

Công thức (3.3) nói rằng, theo trung bình, TD đẩy $w$ theo hướng $b-Aw$; hướng này bằng $0$ đúng khi $Aw=b$, và mệnh đề sau cho thấy đó là điểm cố định Bellman chiếu.

::: proposition Mệnh đề 07.26 (Điểm dừng trung bình là điểm cố định Bellman chiếu)
**Giả thiết.** Như Định nghĩa 07.24.

**Kết luận.** $b-Aw=0$ khi và chỉ khi $\Phi w=\Pi_DT_\pi(\Phi w)$.

**Điều kiện áp dụng.** $\Phi^\top D\Phi$ khả nghịch.

**Phạm vi.** Mô tả điểm mà hướng trung bình bằng $0$; chưa nói dãy (3.2) hội tụ tới đó.
:::

::: proof Chứng minh Mệnh đề 07.26
Đặt $v=T_\pi(\Phi w)$; theo (3.3), $b-Aw=\Phi^\top D(v-\Phi w)$. Nếu biểu thức này bằng $0$, nhân trái với $\Phi(\Phi^\top D\Phi)^{-1}$ được $\Pi_Dv-\Phi w=0$. Ngược lại, nếu $\Phi w=\Pi_Dv$ thì $\Phi^\top D(v-\Phi w)=\Phi^\top D(v-\Pi_Dv)=0$. $\square$
:::

Mệnh đề 07.26 là Bài tập tuần 7 (2025–2026), bài 5: theo trung bình, TD dừng khi phần dư Bellman $T_\pi(\Phi w)-\Phi w$ trực giao với các cột của $\Phi$ theo $\langle\cdot,\cdot\rangle_D$.

::: example Ví dụ 07.11 (Hai trạng thái với đặc trưng 1 và 2)
**Dữ kiện.** $x(s_1)=1$, $x(s_2)=2$, nên $\Phi=(1;2)$. Từ mỗi trạng thái chuyển tới $s_1$ hoặc $s_2$ với xác suất $\tfrac12$; rời $s_1$ nhận $1$, rời $s_2$ nhận $0$, nên $r_\pi=(1;0)$; $\gamma=0{,}9$; bài toán không kết thúc, $d_\pi=(\tfrac12;\tfrac12)$.

**Yêu cầu.** Tính $v_\pi$, $w_{\mathrm{MC}}=\arg\min_wJ_{d_\pi}(w)$, $w_{\mathrm{TD}}$, và so hai sai số giá trị.

**Tính.**

- Với $\bar v=\tfrac12(v_1+v_2)$: $v_1=1+0{,}9\bar v$, $v_2=0{,}9\bar v$, nên $\bar v=5$ và $v_\pi=(5{,}5;4{,}5)$.
- $w_{\mathrm{MC}}=(\tfrac12\cdot5{,}5+\tfrac12\cdot2\cdot4{,}5)/(\tfrac12+\tfrac12\cdot4)=7{,}25/2{,}5=2{,}9$.
- $(I-\gamma P_\pi)\Phi=(1-1{,}35;\,2-1{,}35)=(-0{,}35;0{,}65)$, nên $A=\tfrac12(-0{,}35)+\tfrac12\cdot2\cdot0{,}65=0{,}475$, $b=\tfrac12$, $w_{\mathrm{TD}}=0{,}5/0{,}475=20/19\approx1{,}053$.
- $2J_{d_\pi}(w_{\mathrm{MC}})=\tfrac12(2{,}6)^2+\tfrac12(1{,}3)^2=4{,}225$ và $2J_{d_\pi}(w_{\mathrm{TD}})\approx\tfrac12(4{,}447)^2+\tfrac12(2{,}395)^2\approx12{,}757$.

**Diễn giải.** Cùng đặc trưng và phân phối, Monte Carlo cho $\Phi w=(2{,}9;5{,}8)$, TD cho $\Phi w\approx(1{,}053;2{,}105)$: hai đích khác nhau. Sai số của TD lớn gấp khoảng $3{,}02$ lần, dưới hệ số $1/(1-\gamma)=10$ của Nhận xét 07.30. Chuỗi không kết thúc nên không quan sát được lợi tức đầy đủ nào; $w_{\mathrm{MC}}$ là điểm mà Monte Carlo gradient hướng tới nếu có lợi tức đầy đủ với $S\sim d_\pi$ (Định lý 07.17 với $\mu=d_\pi$).

**Kiểm tra lại.** $T_\pi(\Phi w_{\mathrm{TD}})=(\tfrac{46}{19};\tfrac{27}{19})$ có hệ số hình chiếu $\big(\tfrac12\cdot\tfrac{46}{19}+\tfrac12\cdot2\cdot\tfrac{27}{19}\big)/2{,}5=\tfrac{20}{19}$, đúng $w_{\mathrm{TD}}$.
:::

![Bảng trái, theo chính sách: s₁ có đặc trưng 1 (v̂ = w), s₂ có đặc trưng 2 (v̂ = 2w); mỗi trạng thái chuyển tới s₁ hoặc s₂ với xác suất ½; rời s₁ thưởng 1, rời s₂ thưởng 0; γ = 0,9; cập nhật ở cả hai trạng thái. Bảng phải, khác chính sách: một mảnh MDP khác cùng hai đặc trưng; s₁ có một hành động, chuyển tất định sang s₂ với thưởng 0; chỉ chuyển này được cập nhật, mỗi lần nhân w với 1 + α(2γ − 1).](img/lec-07/two-state-features.svg)

Bảng trái của hình là dữ kiện của Ví dụ 07.11. Bảng phải là mảnh MDP của Ví dụ 07.15, chỉ chung hai vector đặc trưng với Ví dụ 07.11, còn mô hình, phần thưởng và phân phối cập nhật đều khác. Để dãy (3.2) tiến tới $w_{\mathrm{TD}}$, hệ trung bình $w\leftarrow w+\alpha(b-Aw)$ phải ổn định; bổ đề và mệnh đề sau chứng minh điều đó khi dữ liệu theo chính sách.

::: lemma Bổ đề 07.27 (Ma trận chuyển không giãn theo chuẩn có trọng số dừng)
**Giả thiết.** $P_\pi$ là ma trận ngẫu nhiên và $d_\pi^\top P_\pi=d_\pi^\top$.

**Kết luận.** $\lVert P_\pi v\rVert_D\le\lVert v\rVert_D$ với mọi $v$.

**Điều kiện áp dụng.** $d_\pi$ là phân phối dừng của chính $P_\pi$.

**Phạm vi.** Bài toán không kết thúc.
:::

::: proof Chứng minh Bổ đề 07.27
$(P_\pi v)(s)$ là trung bình có trọng số của các $v(s')$, nên theo Jensen, $\big((P_\pi v)(s)\big)^2\le\sum_{s'}P_\pi(s,s')v(s')^2$. Nhân với $d_\pi(s)$ và cộng:

$$
\begin{aligned}
\lVert P_\pi v\rVert_D^2&\le\textstyle\sum_{s'}\big(\sum_sd_\pi(s)P_\pi(s,s')\big)v(s')^2&&\text{(Jensen, đổi thứ tự tổng)}\\
&=\lVert v\rVert_D^2&&(d_\pi^\top P_\pi=d_\pi^\top).\ \square
\end{aligned}
$$
:::

Bổ đề 07.27 là bước còn thiếu để chứng minh $A$ xác định dương: nó cho phép so $v^\top DP_\pi v$ với $\lVert v\rVert_D^2$.

::: proposition Mệnh đề 07.28 (Ma trận $A$ xác định dương)
**Giả thiết.** Như Bổ đề 07.27; $\gamma\in[0,1)$; $d_\pi>0$; cột của $\Phi$ độc lập.

**Kết luận.** $z^\top Az\ge(1-\gamma)\lVert\Phi z\rVert_D^2>0$ với mọi $z\ne0$; do đó $A$ khả nghịch và $w_{\mathrm{TD}}=A^{-1}b$ là điểm cố định Bellman chiếu duy nhất.

**Điều kiện áp dụng.** Cả bốn giả thiết; $A$ không cần đối xứng.

**Phạm vi.** Kết luận về hệ trung bình; hội tụ của dãy ngẫu nhiên là Định lý 07.29.
:::

::: proof Chứng minh Mệnh đề 07.28
Đặt $v=\Phi z$:

$$
\begin{aligned}
z^\top Az&=\lVert v\rVert_D^2-\gamma\,v^\top DP_\pi v&&\text{(định nghĩa }A)\\
&\ge\lVert v\rVert_D^2-\gamma\lVert v\rVert_D\lVert P_\pi v\rVert_D&&\text{(Cauchy–Schwarz)}\\
&\ge(1-\gamma)\lVert v\rVert_D^2&&\text{(Bổ đề 07.27).}
\end{aligned}
$$

Cột độc lập và $d_\pi>0$ cho $\lVert v\rVert_D>0$ khi $z\ne0$. Nếu $Az=0$ thì $z^\top Az=0$, nên $z=0$. Theo Mệnh đề 07.26, điểm cố định Bellman chiếu là nghiệm duy nhất của $Aw=b$. $\square$
:::

Trong Ví dụ 07.11, $A=0{,}475\ge0{,}1\cdot\lVert\Phi\rVert_D^2=0{,}25$. Định lý sau dùng Mệnh đề 07.25, 07.26, 07.28 để phát biểu hội tụ của dãy ngẫu nhiên.

::: theorem Định lý 07.29 (Hội tụ của TD(0) tuyến tính, Tsitsiklis và Van Roy)
**Giả thiết.**

1. $\pi$ cố định; dữ liệu là một quỹ đạo sinh bởi chính $\pi$ (theo chính sách).
2. $\mathcal S$ hữu hạn; chuỗi trạng thái tối giản, không tuần hoàn (theo nghĩa ở phần Kiến thức tiên quyết), phân phối dừng $d_\pi>0$; bài toán không kết thúc.
3. $\gamma\in[0,1)$; phần thưởng bị chặn.
4. Cột của $\Phi$ độc lập tuyến tính.
5. Bước học dương, xác định trước, thỏa Robbins–Monro.

**Kết luận.** Dãy $w_n$ của (3.2) hội tụ hầu chắc chắn tới $w_{\mathrm{TD}}=A^{-1}b$, nghiệm duy nhất của $\Phi w=\Pi_DT_\pi(\Phi w)$.

**Điều kiện áp dụng.** Mọi giả thiết thỏa đồng thời; bài báo gốc còn vài điều kiện kỹ thuật (Sutton và Barto, 2018, §9.4, tr. 208).

**Phạm vi.** $w_{\mathrm{TD}}$ nói chung khác $w_{\mathrm{MC}}$ (Ví dụ 07.11); định lý không nói gì về dữ liệu khác chính sách hay chính sách đổi theo $w$.
:::

::: proof Chứng minh Định lý 07.29
Chứng minh đầy đủ nằm ngoài phạm vi học phần; xem Tsitsiklis và Van Roy (1997), Bertsekas và Tsitsiklis (1996, chương 6), Sutton và Barto (2018, §9.4, tr. 206–207). Ý tưởng: theo Mệnh đề 07.25, $w_{n+1}=w_n+\alpha_n(b-Aw_n)+\alpha_n\xi_n$; theo Mệnh đề 07.28, hệ không nhiễu co về $w_{\mathrm{TD}}$; phần khó là chứng minh tổng nhiễu tắt dần khi các mẫu liên tiếp phụ thuộc nhau, nhờ giả thiết 2 và 5. $\square$
:::

Mỗi giả thiết có một phản ví dụ hoặc trường hợp giới hạn khi bị bỏ.

- Bỏ "theo chính sách": trọng số cập nhật không còn là $d_\pi$, Bổ đề 07.27 không dùng được, và $A$ có thể không xác định dương; trong Ví dụ 07.15, $A=1-2\gamma<0$ và $w_n$ tăng không chặn.
- Bỏ "cột độc lập": với mã hóa bốn khối (Nhận xét 07.9), nghiệm của $Aw=b$ không duy nhất.
- Bỏ "$\gamma<1$": vế phải của Mệnh đề 07.28 bằng $0$.
- Bỏ Robbins–Monro: với bước hằng, $w_n$ dao động quanh $w_{\mathrm{TD}}$.

So với Định lý 07.17, định lý này đổi mục tiêu không chệch lấy mục tiêu bootstrap và trả giá bằng điểm đích: điểm cố định Bellman chiếu thay cho hình chiếu của $v_\pi$. Với bài toán theo lượt có một kết quả tương tự với chặn khác (Sutton và Barto, 2018, §9.4, tr. 208; Bertsekas và Tsitsiklis, 1996).

**Trong thực hành.** Trong notebook Lunar Lander (mục 8), phương trình thực nghiệm $\hat Aw=\hat b$ của (3.3) được giải trực tiếp, gọi là TD bình phương tối thiểu (least-squares TD, LSTD) (Sutton và Barto, 2018, §9.8). Hạng của $\Phi$ là $156/156$, nên giả thiết 4 thỏa trên dữ liệu. Trên các lượt kết thúc thật, LSTD cho $J_{\mathrm{kt}}=1\,622{,}2$, cao hơn $1\,481{,}0$ của Monte Carlo theo lô (một lần chạy đã nhúng trong notebook); Tình huống 07.1 đọc chênh lệch này.

::: exercise Bài tập 07.8 (Nghiệm TD và nghiệm Monte Carlo trên hai trạng thái)
Cho $x(s_1)=1$, $x(s_2)=2$; từ mỗi trạng thái chuyển tới $s_1$ hoặc $s_2$ với xác suất $\tfrac12$; rời $s_1$ nhận $0$, rời $s_2$ nhận $1$; $\gamma=0{,}9$; bài toán không kết thúc, $d_\pi=(\tfrac12;\tfrac12)$.

- (a) Chỉ ra bước nào trong chứng minh Mệnh đề 07.26 cần $\Phi^\top D\Phi$ khả nghịch, và kiểm điều kiện đó trên dữ kiện này. Câu hỏi dựa trên Bài tập tuần 7 (2025–2026), bài 5.
- (b) Tính $v_\pi$, $w_{\mathrm{MC}}$ với $\mu=d_\pi$ và $w_{\mathrm{TD}}$.
:::

::: hint
Với (a), xem bước nhân trái trong chứng minh. Với (b), $A$ giống Ví dụ 07.11; chỉ $b$ và $v_\pi$ đổi.
:::

::: solution
**(a)** Chiều thuận nhân trái với $\Phi(\Phi^\top D\Phi)^{-1}$ để đưa $\Phi^\top D(v-\Phi w)=0$ về $\Pi_Dv=\Phi w$; bản thân $\Pi_D$ cũng được định nghĩa qua nghịch đảo này. Ở đây $\Phi^\top D\Phi=\tfrac12\cdot1+\tfrac12\cdot4=2{,}5\ne0$.

**(b)** $v_1=0{,}9\bar v$, $v_2=1+0{,}9\bar v$, nên $\bar v=5$, $v_\pi=(4{,}5;5{,}5)$. $w_{\mathrm{MC}}=(\tfrac12\cdot4{,}5+\tfrac12\cdot2\cdot5{,}5)/2{,}5=3{,}1$. $A=0{,}475$, $b=\tfrac12\cdot2\cdot1=1$, $w_{\mathrm{TD}}=40/19\approx2{,}105$.

**Kiểm tra lại.** $T_\pi(\Phi w_{\mathrm{TD}})=(\tfrac{54}{19};\tfrac{73}{19})$, hệ số hình chiếu $\tfrac{100}{19}/2{,}5=\tfrac{40}{19}$.
:::

<!-- note-topic-id: lec-07-topic-09 -->
### 3.3 Hai mục tiêu dự đoán

Nhận xét sau gom các khác biệt giữa Monte Carlo và TD(0), theo bảng của bài giảng gốc (trang 37).

::: remark Nhận xét 07.30 (So sánh Monte Carlo và TD(0) với hàm tuyến tính)
| Tiêu chí | Monte Carlo | TD(0) |
|---|---|---|
| Mục tiêu | $G_t$ | $R_{t+1}+\gamma\,\hat v(S_{t+1},w)$ |
| Thời điểm cập nhật | cuối lượt | sau mỗi chuyển |
| Kỳ vọng của mục tiêu | $v_\pi(S_t)$ (Mệnh đề 07.13) | nói chung chệch (Mệnh đề 07.20) |
| Phương sai | thường lớn hơn | thường nhỏ hơn |
| Loại cập nhật | gradient đầy đủ | bán gradient |
| Điểm đích | $\Pi_Dv_\pi$ khi $\mu=d_\pi$ | điểm cố định Bellman chiếu |

Hàng phương sai chỉ đúng trong các thiết lập thường gặp. Với bài toán không kết thúc, theo công thức (9.14) ở Sutton và Barto (2018, §9.4, tr. 207), $\overline{\mathrm{VE}}(w_{\mathrm{TD}})\le\frac1{1-\gamma}\min_w\overline{\mathrm{VE}}(w)$, hệ số $100$ khi $\gamma=0{,}99$.
:::

::: exercise Bài tập 07.9 (So sánh hai phương pháp dự đoán)
So sánh dự đoán Monte Carlo và TD(0) với xấp xỉ tuyến tính theo dạng mục tiêu, độ chệch và phương sai, khả năng cập nhật trực tuyến, độ khó phân tích lý thuyết; mỗi tiêu chí dẫn một kết quả của chương. Đây là Bài tập tuần 7 (2025–2026), bài 2.
:::

::: hint
Dùng Nhận xét 07.30; so giả thiết của Định lý 07.17 với Định lý 07.29.
:::

::: solution
Ba tiêu chí đầu đọc từ bảng của Nhận xét 07.30, với căn cứ ở Định nghĩa 07.12, 07.19, Mệnh đề 07.13, 07.20, Nhận xét 07.23. Tiêu chí cuối cần so hai định lý.

- **Phân tích Monte Carlo.** Cập nhật là SGD trên $J_\mu$ (Mệnh đề 07.14), gần bài toán hồi quy, và hội tụ tới hình chiếu của $v_\pi$ (Định lý 07.17).
- **Phân tích TD.** Cập nhật không giảm mất mát cố định; cần hệ trung bình $b-Aw$, tính xác định dương của $A$ và toán tử Bellman chiếu, với giả thiết theo chính sách và bài toán không kết thúc (Định lý 07.29).

**Kiểm tra lại.** Ví dụ 07.11 cho $w_{\mathrm{MC}}=2{,}9$ và $w_{\mathrm{TD}}\approx1{,}053$ trên cùng dữ liệu.
:::

Như vậy, TD(0) là bán gradient (Định nghĩa 07.21), có hướng trung bình $b-Aw$ (Mệnh đề 07.25), dừng theo trung bình tại điểm cố định Bellman chiếu (Mệnh đề 07.26), và hội tụ tới đó dưới các giả thiết của Định lý 07.29. Tuy nhiên, Mục 2–3 giữ chính sách cố định và chỉ cho giá trị trạng thái. Trong Mục 4, chúng ta học giá trị hành động và để chính sách thay đổi theo tham số.

## 4. Sarsa bán gradient cho điều khiển

Xét chuỗi năm trạng thái $\mathrm A$–$\mathrm E$, xuất phát ở $\mathrm D$, với $\mathrm A$, $\mathrm E$ kết thúc; vào $\mathrm A$ nhận $1\,000$, vào $\mathrm E$ nhận $10$, chuyển khác nhận $-1$ (Ví dụ 07.12 dưới đây). Tác tử ở $\mathrm D$ phải chọn đi trái hay đi phải mà không biết mô hình. Hàm $\hat v$ của Mục 2–3 chỉ cho giá trị trạng thái; chọn hành động tham lam theo nó đòi hỏi $\sum_{s',r}p(s',r\mid s,a)[r+\gamma\hat v(s',w)]$, tức phải biết $p$. Như ghi chú Bài 06, Mục 1, cách tránh mô hình là học giá trị hành động.

<!-- note-topic-id: lec-07-topic-10 -->
### 4.1 Giá trị hành động và vòng điều khiển

Về mặt ý tưởng, điều khiển với xấp xỉ hàm là một vòng khép kín, như hình sau. Mô tả này chưa phải định nghĩa.

![Vòng điều khiển: tham số w xác định q̂(s,a,w); q̂ xác định chính sách ε-tham lam π_w; chính sách sinh dữ liệu (S, A, R, S′); dữ liệu cho mục tiêu y, với TD mục tiêu chứa w; mục tiêu cho cập nhật w theo δ = y − q̂.](img/lec-07/control-loop.svg)

Đi theo mũi tên trên hình, chính sách sinh dữ liệu đổi mỗi khi $w$ đổi, nên phân phối trạng thái và mục tiêu cũng đổi (bài giảng gốc, trang 39); giả thiết "$\pi$ cố định" của Định lý 07.17 và 07.29 không còn.

::: example Ví dụ 07.12 (Chuỗi năm trạng thái với đặc trưng ba chiều)
**Dữ kiện.** Chuỗi $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$; $\mathrm D$ là trạng thái đầu; $\mathrm A$, $\mathrm E$ kết thúc. Hành động $0$ đi trái, $1$ đi phải, chuyển tất định. Vào $\mathrm A$ nhận $1\,000$, vào $\mathrm E$ nhận $10$, chuyển khác nhận $-1$; $\gamma=1$; tối đa ba bước mỗi lượt. Chuỗi lấy từ bài giảng gốc, trang 40, và Bài tập tuần 7 (2025–2026), phần C. Đặc trưng

$$
x(s,a)=\big(d_{\text{trái}}(s);\ u(a);\ 1\big),\qquad d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3),\qquad u(0)=1,\ u(1)=-1,
$$

với $d_{\text{trái}}$ là khoảng cách tới tường trái và $u(a)$ là dấu của hành động; $w_0=(1;1;-1)$.

**Yêu cầu.** Tính $\hat q(s,a,w_0)$ ở $\mathrm B$, $\mathrm C$, $\mathrm D$ và hành động tham lam.

**Tính.** $\hat q(s,0,w_0)=d_{\text{trái}}(s)$ và $\hat q(s,1,w_0)=d_{\text{trái}}(s)-2$, nên $\hat q(\mathrm B,\cdot)=(1;-1)$, $\hat q(\mathrm C,\cdot)=(2;0)$, $\hat q(\mathrm D,\cdot)=(3;1)$; hành động tham lam là $0$ ở cả ba.

**Diễn giải.** Từ $\mathrm D$, đi trái cho lợi tức $-1-1+1\,000=998$, đi phải cho $10$; hành động tham lam đúng nhưng giá trị ước lượng còn xa giá trị thật.

**Kiểm tra lại.** $\hat q(s,1,w_0)-\hat q(s,0,w_0)=-2$ ở mọi trạng thái.
:::

![Chuỗi A–B–C–D–E. D là trạng thái đầu; A và E có viền kép, là trạng thái kết thúc. Hành động 0 đi trái, 1 đi phải. Nhãn cạnh ghi hành động rồi phần thưởng: vào A thưởng 1000, vào E thưởng 10, các chuyển khác thưởng −1. Khoảng cách tới tường trái bằng 1, 2, 3 tại B, C, D.](img/lec-07/five-state-features.svg)

Hình trên ghi mỗi cạnh bằng hành động và phần thưởng, cùng $d_{\text{trái}}$ dưới ba trạng thái không kết thúc. Đặc trưng thiết kế trực tiếp cho cặp $(s,a)$, không có khối Kronecker.

::: definition Định nghĩa 07.31 (Chính sách ε-tham lam theo giá trị hành động tuyến tính)
Cho $\hat q(s,a,w)=x(s,a)^\top w$ với $m$ hành động, $\varepsilon\in[0,1]$ và một quy tắc phá hòa cố định. Chính sách $\pi_w$ là chính sách $\varepsilon$-tham lam của phần Kiến thức tiên quyết, với bảng $Q$ thay bằng $\hat q(\cdot,\cdot,w)$; $\varepsilon=0$ cho chính sách tham lam.
:::

Khác Bài 06, mỗi cập nhật $w$ có thể đổi hành động tham lam ở nhiều trạng thái cùng lúc (Mệnh đề 07.2).

::: proposition Mệnh đề 07.32 (Hiệu giữa hai hành động trên chuỗi năm trạng thái)
**Giả thiết.** Đặc trưng của Ví dụ 07.12.

**Kết luận.** $\hat q(s,1,w)-\hat q(s,0,w)=-2[w]_2$ với mọi $s\in\{\mathrm B,\mathrm C,\mathrm D\}$ và mọi $w$; chính sách tham lam chọn cùng một hành động ở ba trạng thái.

**Điều kiện áp dụng.** Đặc trưng $(d_{\text{trái}}(s);u(a);1)$.

**Phạm vi.** Ở chuỗi này đi trái tốt hơn ở mọi trạng thái nên giới hạn chưa gây sai; với bài toán cần hành động khác nhau theo trạng thái, đặc trưng này không biểu diễn được chính sách tốt.
:::

::: proof Chứng minh Mệnh đề 07.32
$x(s,1)$ và $x(s,0)$ chỉ khác thành phần thứ hai, $u(1)-u(0)=-2$, nên hiệu bằng $-2[w]_2$, không chứa $s$. $\square$
:::

Mệnh đề 07.32 là trường hợp riêng của Mệnh đề 07.8(b): đặc trưng thiếu tương tác trạng thái–hành động; Bài tập 07.12 sửa giới hạn này.

### 4.2 Sarsa bán gradient

Như Sarsa dạng bảng (ghi chú Bài 06, Mục 3), mục tiêu dùng giá trị của cặp kế tiếp mà chính sách đang chạy thực sự chọn.

::: example Ví dụ 07.13 (Một cập nhật Sarsa trên chuỗi năm trạng thái)
**Dữ kiện.** Chuỗi và đặc trưng của Ví dụ 07.12; $w_0=(1;1;-1)$, $\alpha=0{,}2$, $\gamma=1$; mẫu $(S,A,R,S',A')=(\mathrm D,0,-1,\mathrm C,0)$, với $A'$ do chính sách $\varepsilon$-tham lam đang chạy chọn.

**Yêu cầu.** Tính mục tiêu, sai số TD và $w_1$.

**Tính.** $x(\mathrm D,0)=(3;1;1)$, $x(\mathrm C,0)=(2;1;1)$; với $w_0$: $\hat q(\mathrm D,0)=3$, $\hat q(\mathrm C,0)=2$.

$$
\begin{aligned}
\text{mục tiêu: }&y=-1+2=1,\\
\text{sai số TD: }&\delta=1-3=-2,\\
\text{tham số mới: }&w_1=(1;1;-1)+0{,}2\cdot(-2)\cdot(3;1;1)=(-0{,}2;0{,}6;-1{,}4).
\end{aligned}
$$

**Diễn giải.** $\hat q(\mathrm D,0,w_1)=-1{,}4$: vì $\alpha\lVert x(\mathrm D,0)\rVert^2=2{,}2>1$, dự đoán vượt qua mục tiêu $1$. Cặp $(\mathrm C,0)$ không được cập nhật nhưng $\hat q(\mathrm C,0,w_1)=-1{,}2$.

**Kiểm tra lại.** Theo Mệnh đề 07.2, $\hat q(\mathrm D,0)$ đổi $-0{,}4\cdot11=-4{,}4$, và $3-4{,}4=-1{,}4$.
:::

::: algorithm Thuật toán 07.33 (Sarsa bán gradient theo lượt)
**Đầu vào.** Đặc trưng $x(s,a)$; $\varepsilon$ và quy tắc phá hòa; $\gamma$; số lượt $K$; $(\alpha_n)$; giới hạn số bước mỗi lượt, nếu có.

**Đầu ra.** $w$ và chính sách $\pi_w$.

**Giả thiết.** Tập hành động hữu hạn; lượt kết thúc hoặc bị cắt ngắn sau hữu hạn bước.

**Khởi tạo.** $w\leftarrow w_0$, $n\leftarrow0$.

**Tham số.** $\varepsilon$, $K$, $(\alpha_n)$.

1. Với mỗi lượt: lấy trạng thái đầu $S$, chọn $A$ theo $\pi_w$.
2. Thực hiện $A$, nhận $R$, $S'$.
3. Nếu $S'$ kết thúc: $y\leftarrow R$. Ngược lại: chọn $A'$ theo $\pi_w$ tại $S'$ bằng $w$ hiện tại, $y\leftarrow R+\gamma\,x(S',A')^\top w$; điều này đúng cả khi lượt vừa đạt giới hạn số bước.
4. $\delta\leftarrow y-x(S,A)^\top w$; $w\leftarrow w+\alpha_n\delta\,x(S,A)$; $n\leftarrow n+1$.
5. Nếu $S'$ kết thúc hoặc lượt đạt giới hạn số bước: sang lượt mới. Ngược lại: $S\leftarrow S'$, $A\leftarrow A'$, quay lại bước 2.

**Điều kiện dừng.** Sau $K$ lượt.

**Chi phí mỗi bước.** $m$ tích vô hướng để chọn $A'$; bước 4 tỉ lệ với số thành phần khác $0$ của $x(S,A)$.
:::

Bước 3 và 4 với mẫu của Ví dụ 07.13 cho đúng $y=1$, $\delta=-2$, $w_1$. So với Thuật toán 07.22, Sarsa đổi đặc trưng thành $x(S,A)$, mục tiêu thành $\hat q(S',A',w)$, và chính sách sinh dữ liệu thành $\pi_w$, đổi theo $w$.

Cập nhật vẫn là bán gradient. Vì $A'$ do $\pi_w$ chọn, kể cả khi thăm dò, Sarsa học theo chính sách (Sutton và Barto, 2018, §10.1, tr. 244).

::: remark Nhận xét 07.34 (Phạm vi bảo đảm của Sarsa với hàm tuyến tính)
Theo Sutton và Barto (2018, §10.1, tr. 244), với chính sách giữ cố định, Sarsa hội tụ như TD(0). Thuật toán 07.33 không giữ chính sách cố định, nên giả thiết 1 của Định lý 07.29 và bảo đảm dạng bảng của ghi chú Bài 06, Mục 5 đều không áp dụng. Chúng ta không phát biểu kết quả hội tụ tổng quát cho Sarsa với xấp xỉ hàm; các phân tích hữu hạn mẫu như của Zou, Xu và Liang (2019) cần giả thiết riêng về thăm dò, bước học và cách chính sách phụ thuộc $w$.
:::

**Trong thực hành.** Hai notebook dùng Thuật toán 07.33 với bốn khối trên Fourier bậc 3 và bước hằng, rồi đánh giá chính sách tham lam trên $100$ lượt kiểm tra (một lần chạy đã nhúng trong mỗi notebook). Dấu ± theo quy ước ở phần Quy ước đọc: trung bình ± sai số chuẩn (standard error, SE), hoặc nửa khoảng tin cậy $95\%$ với hiệu ghép cặp.

Trên Lunar Lander ($d=785$), thước đo là tổng phần thưởng không chiết khấu của lượt, gọi tắt là tổng phần thưởng. Sarsa đạt $200{,}9\pm15{,}7$, bộ điều khiển viết tay $236{,}9$. Thực hành Bài 06 cho $26{,}2$ với bảng $2\,187$ ô gốc, cùng lịch giảm $\varepsilon$ theo lượt và cùng số lượt, và $202{,}8$ với bảng tinh chỉnh dùng hai đặc trưng từ bộ điều khiển viết tay; hai bên khác cả biểu diễn lẫn bước học, nên chênh lệch không quy được riêng cho biểu diễn tuyến tính.

Trên Flappy Bird, Sarsa qua $38{,}04\pm1{,}61$ ống, luật tay $34{,}30\pm1{,}30$, hiệu ghép cặp $3{,}74\pm2{,}90$. Cấu hình không thỏa giả thiết của bảo đảm nào, nên các số chỉ mô tả lần chạy.

<!-- note-topic-id: lec-07-topic-16 -->
### 4.3 Bài tập trên chuỗi năm trạng thái

Hai bài đầu là bài 7 và 8 của Bài tập tuần 7 (2025–2026); bài thứ ba dùng kết quả của bài 8.

::: exercise Bài tập 07.10 (Monte Carlo trên một lượt của chuỗi)
Chuỗi năm trạng thái như Ví dụ 07.12: $x(s,a)=(d_{\text{trái}}(s);u(a);1)$, $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$, $u(0)=1$, $u(1)=-1$, $\gamma=1$; $w_0=(1;1;-1)$, $\alpha=0{,}1$; một lượt $(\mathrm D,0,-1,\mathrm C)$, $(\mathrm C,0,-1,\mathrm B)$, $(\mathrm B,0,1\,000,\mathrm A)$.

- (a) Tính $G_0$, $G_1$, $G_2$.
- (b) Viết $x(\mathrm D,0)$, $x(\mathrm C,0)$, $x(\mathrm B,0)$.
- (c) Cập nhật theo thứ tự thời gian bằng $w_{n+1}=w_n+\alpha\big(G_t-x(S_t,A_t)^\top w_n\big)x(S_t,A_t)$.
- (d) Tính $\hat q(\mathrm D,0,w_3)$, $\hat q(\mathrm C,0,w_3)$, $\hat q(\mathrm B,0,w_3)$.
:::

::: hint
Với $\gamma=1$, $G_t$ là tổng phần thưởng tới hết lượt; mỗi lần dùng $w$ vừa có.
:::

::: solution
**(a)** $G_2=1\,000$, $G_1=999$, $G_0=998$.

**(b)** $(3;1;1)$, $(2;1;1)$, $(1;1;1)$.

**(c)**

- Lần 1: $\hat q=3$, sai lệch $995$, bước $99{,}5$, $w_1=(299{,}5;100{,}5;98{,}5)$.
- Lần 2: $\hat q=798$, sai lệch $201$, bước $20{,}1$, $w_2=(339{,}7;120{,}6;118{,}6)$.
- Lần 3: $\hat q=578{,}9$, sai lệch $421{,}1$, bước $42{,}11$, $w_3=(381{,}81;162{,}71;160{,}71)$.

**(d)** $1\,468{,}85$; $1\,087{,}04$; $705{,}23$.

**Diễn giải.** $\hat q(\mathrm D,0)$ vượt $G_0=998$ vì hai lý do. Thứ nhất, $\alpha\lVert x(\mathrm D,0)\rVert^2=1{,}1>1$, nên ngay lần 1 dự đoán thành $3+1{,}1\cdot995=1\,097{,}5$. Thứ hai, hai cập nhật sau kéo nó lên qua tham số dùng chung. Chưa có bước cải thiện chính sách.

**Kiểm tra lại.** $3\cdot381{,}81+162{,}71+160{,}71=1\,468{,}85$.
:::

::: exercise Bài tập 07.11 (Ba cập nhật Sarsa trên chuỗi)
Chuỗi và đặc trưng như Bài tập 07.10; $w_0=(1;1;-1)$, $\alpha=0{,}2$, $\varepsilon=0{,}25$, $\gamma=1$. Ba mẫu: $(\mathrm D,0,-1,\mathrm C,0)$, $(\mathrm C,1,-1,\mathrm D,1)$, $(\mathrm D,1,10,\mathrm E,\text{kết thúc})$. Phiếu bài tập gọi ba mẫu là liên tiếp; nhưng mẫu 1 có hành động kế tiếp $0$ tại $\mathrm C$, còn mẫu 2 thực hiện hành động $1$ tại $\mathrm C$, nên ở đây coi ba mẫu là độc lập. Dùng (3.2), thay $x(S_t)$, $x(S_{t+1})$ bằng $x(S_t,A_t)$, $x(S_{t+1},A_{t+1})$, với $\hat q(\mathrm E,\cdot,w)=0$.

- (a) Tính $\delta$ và tham số mới sau mỗi mẫu.
- (b) Tính $\hat q(\mathrm D,0,w_3)$, $\hat q(\mathrm C,1,w_3)$, $\hat q(\mathrm D,1,w_3)$ và kiểm tra $\hat q(\mathrm D,1,w_3)-\hat q(\mathrm D,0,w_3)=-2[w_3]_2$.
:::

::: hint
Hai giá trị trong một $\delta$ dùng tham số trước cập nhật; mẫu 1 là Ví dụ 07.13; $\varepsilon$ không vào phép tính vì hành động kế tiếp đã cho.
:::

::: solution
**Mẫu 1.** $\delta=-2$, $w_1=(-0{,}2;0{,}6;-1{,}4)$.

**Mẫu 2.** $\hat q(\mathrm C,1,w_1)=-0{,}4-0{,}6-1{,}4=-2{,}4$; $\hat q(\mathrm D,1,w_1)=-0{,}6-0{,}6-1{,}4=-2{,}6$; mục tiêu $-3{,}6$; $\delta=-1{,}2$; $w_2=w_1-0{,}24\cdot(2;-1;1)=(-0{,}68;0{,}84;-1{,}64)$.

**Mẫu 3.** $\hat q(\mathrm D,1,w_2)=-4{,}52$; $\delta=14{,}52$; $w_3=w_2+2{,}904\cdot(3;-1;1)=(8{,}032;-2{,}064;1{,}264)$.

**(b)** $23{,}296$; $19{,}392$; $27{,}424$.

**Diễn giải.** Mẫu 1 là chuyển $(\mathrm D,0,-1,\mathrm C)$ đầu lượt của Bài tập 07.10, cùng $w_0$. Ở đó mục tiêu Monte Carlo $G_0=998$, với $\alpha=0{,}1$, đẩy $\hat q(\mathrm D,0)$ từ $3$ lên $3+1{,}1\cdot995=1\,097{,}5$. Ở đây mục tiêu Sarsa $-1+\hat q(\mathrm C,0,w_0)=1$, với $\alpha=0{,}2$, kéo nó xuống $3+2{,}2\cdot(-2)=-1{,}4$. Mục tiêu bootstrap chỉ chứa phần thưởng $-1$ và dự đoán hiện tại tại $(\mathrm C,0)$, nên chưa mang thông tin về phần thưởng $1\,000$ khi vào $\mathrm A$.

**Kiểm tra lại.** $27{,}424-23{,}296=4{,}128=-2\cdot(-2{,}064)$.
:::

::: exercise Bài tập 07.12 (Chính sách tham lam sau ba cập nhật Sarsa)
Trên chuỗi năm trạng thái với $x(s,a)=(d_{\text{trái}}(s);u(a);1)$, $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$, $u(0)=1$, $u(1)=-1$, $\gamma=1$, cho $w_3=(8{,}032;-2{,}064;1{,}264)$ là kết quả của Bài tập 07.11. Từ $\mathrm D$, đi trái cho lợi tức $998$, đi phải cho $10$.

- (a) Xác định hành động tham lam tại $\mathrm B$, $\mathrm C$, $\mathrm D$ và so với hành động tốt hơn.
- (b) Thêm một thành phần vào $x(s,a)$ để thứ tự hai hành động có thể khác nhau giữa các trạng thái, và chứng minh điều đó bằng hiệu $\hat q(s,1,w)-\hat q(s,0,w)$.
:::

::: hint
Mệnh đề 07.32 cho (a); với (b), thêm tích $d_{\text{trái}}(s)u(a)$, giống khối Kronecker.
:::

::: solution
**(a)** Hiệu bằng $-2\cdot(-2{,}064)=4{,}128>0$ ở mọi trạng thái, nên tham lam chọn đi phải ở cả ba, trong khi đi trái tốt hơn ($998$ so với $10$ từ $\mathrm D$). Ba mẫu ngắn và bước có $\alpha\lVert x\rVert^2=2{,}2$ ở mẫu cuối đã đảo dấu $[w]_2$.

**(b)** Với $x(s,a)=(d_{\text{trái}}(s);u(a);1;d_{\text{trái}}(s)u(a))$, hiệu bằng $-2[w]_2-2d_{\text{trái}}(s)[w]_4$, phụ thuộc $s$ khi $[w]_4\ne0$.

**Kiểm tra lại.** $[w]_2=1$, $[w]_4=-1$ cho hiệu $0$, $2$, $4$ tại $\mathrm B$, $\mathrm C$, $\mathrm D$.
:::

Như vậy, chúng ta đã dựng $\pi_w$ (Định nghĩa 07.31) và Sarsa bán gradient (Thuật toán 07.33), và thấy đặc trưng của chuỗi buộc chính sách tham lam giống nhau ở mọi trạng thái (Mệnh đề 07.32). Tuy nhiên, Sarsa ước lượng giá trị của chính sách $\varepsilon$-tham lam đang chạy, không phải $q_*$. Trong Mục 5, chúng ta đổi mục tiêu sang phép cực đại và chỉ ra cái giá của phép đổi đó.

## 5. Q-learning bán gradient và bộ ba bất ổn

Trong Bài tập 07.11, mẫu thứ hai kết thúc bằng hành động $1$ tại $\mathrm D$, trong khi theo $w_1$ hành động tham lam tại $\mathrm D$ là $0$, vì $\hat q(\mathrm D,0,w_1)=-1{,}4>\hat q(\mathrm D,1,w_1)=-2{,}6$. Mục tiêu Sarsa dùng đúng hành động thăm dò này. Q-learning dạng bảng (ghi chú Bài 06, Mục 4) học $q_*$ nhờ phép cực đại; chúng ta cần biết điều gì xảy ra khi đưa phép cực đại vào hàm tuyến tính.

<!-- note-topic-id: lec-07-topic-11 -->
### 5.1 Mục tiêu Q-learning với hàm xấp xỉ

Về mặt ý tưởng, Q-learning tách hai chính sách. Chính sách hành vi sinh dữ liệu và còn thăm dò. Chính sách đích là chính sách tham lam theo $\hat q$ và chỉ xuất hiện trong mục tiêu. Mô tả này chưa phải định nghĩa; ví dụ sau so hai mục tiêu trên cùng một mẫu.

::: example Ví dụ 07.14 (Hai mục tiêu trên mẫu thứ hai của chuỗi)
**Dữ kiện.** Chuỗi và đặc trưng của Ví dụ 07.12; $\gamma=1$, $\alpha=0{,}2$, $w_0=(1;1;-1)$. Hai mẫu đầu của Bài tập 07.11, coi là độc lập như ở đó: $(\mathrm D,0,-1,\mathrm C,0)$ và $(\mathrm C,1,-1,\mathrm D,1)$.

**Yêu cầu.** Thực hiện hai cập nhật Q-learning với mục tiêu $R+\gamma\max_{a'}\hat q(S',a',w)$ và so với Sarsa ở mẫu thứ hai.

**Tính.**

- Mẫu 1: $\hat q(\mathrm C,\cdot,w_0)=(2;0)$, mục tiêu $-1+2=1$, trùng Sarsa vì hành động kế tiếp của mẫu là hành động tham lam; $w_1=(-0{,}2;0{,}6;-1{,}4)$ như Ví dụ 07.13.
- Mẫu 2: $\hat q(\mathrm C,1,w_1)=-2{,}4$, $\hat q(\mathrm D,0,w_1)=-1{,}4$, $\hat q(\mathrm D,1,w_1)=-2{,}6$.

$$
\begin{aligned}
\text{Sarsa: }&y=-1-2{,}6=-3{,}6,\qquad \delta=-1{,}2,\\
\text{Q-learning: }&y=-1+\max(-1{,}4;-2{,}6)=-2{,}4,\qquad \delta=0,\qquad w_2=w_1.
\end{aligned}
$$

**Diễn giải.** Hành động kế tiếp của mẫu 2, đi phải tại $\mathrm D$, là hành động thăm dò. Sarsa đưa giá trị của nó vào mục tiêu; Q-learning thay bằng giá trị của hành động tham lam và không đổi $w$.

**Kiểm tra lại.** $\hat q(\mathrm D,0,w_1)-\hat q(\mathrm D,1,w_1)=1{,}2=2[w_1]_2$ (Mệnh đề 07.32).
:::

::: definition Định nghĩa 07.35 (Mục tiêu Q-learning với hàm xấp xỉ)
Với chuyển $(S_t,A_t,R_{t+1},S_{t+1})$ dùng trong lần cập nhật từ $w_n$,

$$
y_t=\begin{cases}R_{t+1}, & S_{t+1}\text{ là trạng thái kết thúc},\\ R_{t+1}+\gamma\max_{a'}\hat q(S_{t+1},a',w_n), & \text{ngược lại},\end{cases}
\tag{5.1}
$$

và cập nhật bán gradient là $w_{n+1}=w_n+\alpha_n\big(y_t-\hat q(S_t,A_t,w_n)\big)x(S_t,A_t)$.
:::

Mục tiêu (5.1) là mục tiêu Q-learning dạng bảng với $Q$ thay bằng $\hat q$, không phụ thuộc hành động kế tiếp thực sự được chọn; hai mục tiêu Sarsa và Q-learning bằng nhau khi hành động kế tiếp là hành động tham lam. Dữ liệu theo chính sách hành vi còn mục tiêu theo chính sách tham lam, nên Q-learning học khác chính sách. Thuật toán sau được bổ sung theo quy trình của hai notebook; bài giảng gốc (trang 38) chỉ nêu mục tiêu.

::: algorithm Thuật toán 07.36 (Q-learning bán gradient theo lượt)
**Đầu vào.** Đặc trưng $x(s,a)$; $\varepsilon$ và quy tắc phá hòa; $\gamma$; $K$; $(\alpha_n)$; giới hạn số bước mỗi lượt, nếu có.

**Đầu ra.** $w$ và chính sách tham lam theo $\hat q(\cdot,\cdot,w)$.

**Giả thiết.** Tập hành động hữu hạn; lượt kết thúc hoặc bị cắt ngắn sau hữu hạn bước.

**Khởi tạo.** $w\leftarrow w_0$, $n\leftarrow0$.

**Tham số.** $\varepsilon$, $K$, $(\alpha_n)$.

1. Với mỗi lượt: lấy trạng thái đầu $S$.
2. Chọn $A$ theo $\pi_w$ tại $S$ (chính sách hành vi), thực hiện, nhận $R$, $S'$.
3. Tính $y$ theo (5.1) bằng $w$ hiện tại; tại bước cắt ngắn, $S'$ chưa kết thúc nên $y$ vẫn chứa phép cực đại.
4. $\delta\leftarrow y-x(S,A)^\top w$; $w\leftarrow w+\alpha_n\delta\,x(S,A)$; $n\leftarrow n+1$.
5. Nếu $S'$ kết thúc hoặc lượt đạt giới hạn số bước: sang lượt mới. Ngược lại: $S\leftarrow S'$ và quay lại bước 2, khi đó hành động mới được chọn bằng $w$ đã cập nhật.

**Điều kiện dừng.** Sau $K$ lượt.

**Chi phí mỗi bước.** Bước 2 và 3 mỗi bước $m$ tích vô hướng; bước 4 tỉ lệ với số thành phần khác $0$ của $x(S,A)$.
:::

Bước 3 và 4 với Ví dụ 07.14 cho $w_2=w_1=(-0{,}2;0{,}6;-1{,}4)$. So với Thuật toán 07.33, Q-learning đổi hai chỗ: mục tiêu dùng $\max_{a'}$, và hành động tại $S'$ được chọn sau cập nhật bằng $w$ mới, trong khi Sarsa chọn $A'$ trước cập nhật. Mục tiêu (5.1) không khẳng định $\hat q$ hội tụ tới $q_*$ (bài giảng gốc, trang 41).

**Trong thực hành.** Hai notebook dùng Thuật toán 07.36 với cùng đặc trưng và cách chọn bước học như Sarsa (một lần chạy đã nhúng trong mỗi notebook). Trên Lunar Lander, Q-learning đạt tổng phần thưởng $205{,}3\pm8{,}4$; bảng tinh chỉnh của Bài 06 cho $235{,}5$, với cùng lưu ý như ở Mục 4.2. Trên Flappy Bird, Q-learning qua $28{,}86\pm1{,}98$ ống, thấp hơn Sarsa với hiệu ghép cặp $-9{,}18\pm4{,}50$; bảng thử nghiệm khi soạn cho cùng cấu hình $36{,}3\pm1{,}4$ và $35{,}0\pm3{,}6$ ống (độ lệch chuẩn qua ba hạt giống), nên một lần chạy chưa đủ để xếp thứ tự.


Trên Lunar Lander, trung bình của $\max_a\hat q(S_0,a,w)$ cao hơn lợi tức $G_0$ một lượng $12{,}4\pm2{,}2$ với Q-learning và thấp hơn $7{,}9\pm3{,}2$ với Sarsa (hiệu ghép cặp trên cùng $100$ lượt, nửa khoảng tin cậy $95\%$); chiều của Q-learning phù hợp với việc cực đại trên ước lượng có nhiễu đánh giá quá cao, dù sai số xấp xỉ cũng góp vào. Double Q-learning (Sutton và Barto, 2018, §6.7) tách việc chọn và đánh giá hành động cho hai vector tham số; trên Flappy Bird, với $8\,000$ lượt, nó qua $38{,}24\pm1{,}79$ ống.


::: exercise Bài tập 07.13 (Ba cập nhật Q-learning trên chuỗi)
Trên chuỗi năm trạng thái với $x(s,a)=(d_{\text{trái}}(s);u(a);1)$, $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$, $u(0)=1$, $u(1)=-1$, $\gamma=1$; $w_0=(1;1;-1)$, $\alpha=0{,}2$; ba mẫu độc lập $(\mathrm D,0,-1,\mathrm C)$, $(\mathrm C,1,-1,\mathrm D)$, $(\mathrm D,1,10,\mathrm E,\text{kết thúc})$. Thực hiện ba cập nhật Q-learning theo Định nghĩa 07.35; tính $w_3$, $\hat q(\mathrm D,0,w_3)$, $\hat q(\mathrm D,1,w_3)$ và so với kết quả Sarsa $w_3=(8{,}032;-2{,}064;1{,}264)$ của Bài tập 07.11.
:::

::: hint
Hai mẫu đầu ở Ví dụ 07.14; mẫu cuối vào trạng thái kết thúc nên mục tiêu là $R$.
:::

::: solution
**Mẫu 1, 2.** $w_1=w_2=(-0{,}2;0{,}6;-1{,}4)$ (Ví dụ 07.14).

**Mẫu 3.** $\hat q(\mathrm D,1,w_2)=-2{,}6$, $\delta=12{,}6$, $w_3=w_2+2{,}52\cdot(3;-1;1)=(7{,}36;-1{,}92;1{,}12)$.

**Giá trị.** $\hat q(\mathrm D,0,w_3)=22{,}08-1{,}92+1{,}12=21{,}28$; $\hat q(\mathrm D,1,w_3)=22{,}08+1{,}92+1{,}12=25{,}12$. Hai thuật toán tách nhau từ mẫu 2, nơi hành động kế tiếp là thăm dò.

**Kiểm tra lại.** $25{,}12-21{,}28=3{,}84=-2\cdot(-1{,}92)$.
:::

<!-- note-topic-id: lec-07-topic-17 -->
### 5.2 Bộ ba bất ổn

Định lý 07.29 cần dữ liệu theo chính sách, vì trọng số $d_\pi$ trong Mệnh đề 07.25 và Bổ đề 07.27 đến từ đó, còn Q-learning cập nhật theo phân phối của chính sách hành vi. Ví dụ sau (Sutton và Barto, 2018, §11.2, tr. 260) dùng TD(0) dự đoán khác chính sách và cho thấy hậu quả có thể có khi bỏ giả thiết theo chính sách. Q-learning có cùng ba yếu tố của ví dụ (xấp xỉ hàm, mục tiêu bootstrap, dữ liệu khác chính sách), và theo Sutton và Barto (2018, §11.2, tr. 263), Q-learning có phản ví dụ phân kỳ tương tự phản ví dụ bảy trạng thái của Baird.

::: example Ví dụ 07.15 (TD(0) khác chính sách trên hai trạng thái, tham số tăng không chặn)
**Dữ kiện.** Một mảnh MDP gồm hai trạng thái với $x(s_1)=1$, $x(s_2)=2$, nên $\hat v=(w;2w)$; chỉ hai vector đặc trưng là chung với Ví dụ 07.11. Ở $s_1$ chỉ có một hành động, chuyển tất định sang $s_2$ với phần thưởng $0$, nên tỉ số lấy mẫu quan trọng $\rho_t$ trên chuyển này bằng $1$. Ở $s_2$, chính sách hành vi chọn những hành động mà chính sách đích không chọn; tỉ số trên các chuyển đó bằng $0$, nên chỉ chuyển $s_1\to s_2$ được cập nhật, lặp lại nhiều lần. TD(0) bán gradient với $\gamma=0{,}9$, $\alpha=0{,}1$, $w_0=1$.

**Yêu cầu.** Tính $w_1$, $w_2$ và $w_n$.

**Tính.**

$$
\begin{aligned}
\text{sai số TD: }&\delta=0+0{,}9\cdot2w_n-w_n=0{,}8\,w_n,\\
\text{tham số mới: }&w_{n+1}=w_n+0{,}1\cdot0{,}8\,w_n=1{,}08\,w_n .
\end{aligned}
$$

Vậy $w_1=1{,}08$, $w_2=1{,}1664$, $w_n=1{,}08^n$; ví dụ $w_{30}\approx10{,}06$.

**Diễn giải.** Mỗi cập nhật nâng $\hat v(s_1)$ về phía $1{,}8w$, nhưng vì tham số dùng chung, $\hat v(s_2)=2w$ tăng nhanh hơn, nên sai số TD lần sau lớn hơn. Quy tắc ở đây là TD(0) dự đoán, không có phép cực đại như mục tiêu Q-learning.

**Kiểm tra lại.** $1{,}08^2=1{,}1664$.
:::

::: proposition Mệnh đề 07.37 (Phân kỳ trong ví dụ hai trạng thái)
**Giả thiết.** Dữ kiện của Ví dụ 07.15 với $\gamma\in(\tfrac12,1)$, $\alpha>0$ bất kỳ, $w_0\ne0$.

**Kết luận.** $w_n=\big(1+\alpha(2\gamma-1)\big)^nw_0$, nên $\lvert w_n\rvert\to\infty$.

**Điều kiện áp dụng.** Phân phối cập nhật chỉ gồm chuyển $s_1\to s_2$.

**Phạm vi.** Một trường hợp phân kỳ của TD(0) dự đoán khác chính sách; không nói mọi cập nhật khác chính sách đều phân kỳ.
:::

::: proof Chứng minh Mệnh đề 07.37
$\delta=\gamma\cdot2w_n-w_n=(2\gamma-1)w_n$, và (3.2) với $x(s_1)=1$ cho $w_{n+1}=(1+\alpha(2\gamma-1))w_n$; quy nạp cho công thức. Khi $\gamma>\tfrac12$, hệ số lớn hơn $1$ với mọi $\alpha>0$. $\square$
:::

Theo Mục 3, phân phối cập nhật tập trung ở $s_1$ cho "ma trận" $A=x(s_1)(x(s_1)-\gamma x(s_2))=1-2\gamma<0$, không xác định dương như Mệnh đề 07.28 cần; bước nhỏ hơn chỉ làm $w$ tăng chậm hơn.

::: definition Định nghĩa 07.38 (Bộ ba bất ổn)
Một phương pháp học giá trị có bộ ba bất ổn khi có đồng thời:

- **xấp xỉ hàm:** tham số dùng chung, một cập nhật đổi nhiều dự đoán;
- **bootstrap:** mục tiêu chứa ước lượng hiện tại;
- **học khác chính sách:** phân phối các chuyển dùng để cập nhật khác phân phối do chính sách đích sinh ra.
:::

Yếu tố thứ ba là khái niệm học khác chính sách của ghi chú Bài 06, Mục 4, nhìn qua phân phối cập nhật: tần suất các chuyển được cập nhật khác tần suất do chính sách đích tạo ra, và tần suất này là trọng số trong hướng trung bình (3.3).

![Tam giác có ba đỉnh: xấp xỉ hàm ở trên, bootstrap ở dưới bên trái, học khác chính sách ở dưới bên phải; ở giữa tam giác ghi "có thể phân kỳ", nghĩa là khi cả ba cùng có mặt, cập nhật TD có thể phân kỳ.](img/lec-07/deadly-triad.svg)

Hình đặt ba yếu tố ở ba đỉnh tam giác, nhãn "có thể phân kỳ" ở giữa. Theo bài giảng gốc (trang 41) và Sutton và Barto (2018, §11.3, tr. 264), khi đủ ba yếu tố, TD và Q-learning có thể phân kỳ; khi chỉ có hai, có thể tránh được bất ổn. Ví dụ 07.15 có đủ ba.

Bỏ một yếu tố cho các trường hợp đã biết:

- Bỏ "khác chính sách": TD(0) tuyến tính theo chính sách hội tụ (Định lý 07.29).
- Bỏ "xấp xỉ hàm": Q-learning dạng bảng hội tụ (ghi chú Bài 06, Mục 5).
- Bỏ "bootstrap": Monte Carlo với dữ liệu khác chính sách dùng lấy mẫu quan trọng, đổi lại phương sai lớn (bài giảng gốc, trang 37).

Theo Sutton và Barto (2018, §11.3), nguy cơ xuất hiện ngay trong bài toán dự đoán, không cần điều khiển.

::: remark Nhận xét 07.39 (Đọc đúng khẳng định về bộ ba bất ổn)
"Có thể phân kỳ" nói về một lớp phương pháp: không có bảo đảm hội tụ chung, và có ví dụ phân kỳ (Mệnh đề 07.37; ví dụ của Baird ở Sutton và Barto, 2018, §11.2, tr. 261–262). Nó không nói một lần chạy sẽ phân kỳ. Dấu hiệu của phân kỳ là $\lVert w\rVert$ hoặc dự đoán tăng không chặn; chính sách kém với $\lVert w\rVert$ bị chặn là hiện tượng khác.

Các hướng khắc phục theo bài giảng gốc (trang 41) gồm đổi trọng số cập nhật, mạng mục tiêu (target network), điều chuẩn và cắt ngưỡng; Bài 08 dùng mạng mục tiêu. Theo trang 43, nhiều cách ổn định hóa cần giả thiết mạnh hoặc cho nghiệm chệch.
:::

**Trong thực hành.** Bảng thử nghiệm khi soạn, nhúng trong notebook Flappy Bird, cho Q-learning với họ đa thức bậc 2 `poly2` có $\lVert w\rVert$ lớn nhất $1\,895{,}1$, Sarsa trên cùng họ $15{,}1$; cả hai qua $0$ ống. Trên Lunar Lander, $\lVert w\rVert$ của Q-learning tăng từ $42{,}3$ ở lượt $500$ lên $52{,}2$ ở lượt $3\,000$, không có bước nhảy (một lần chạy đã nhúng trong notebook).

::: exercise Bài tập 07.14 (Nhận diện bộ ba bất ổn)
Với mỗi quy tắc sau, xác định ba yếu tố của Định nghĩa 07.38. Đây là Bài tập tuần 7 (2025–2026), bài 3. Với (a)–(c), kết luận thêm có bảo đảm theo Định lý 07.29 hay không.

- (a) TD(0) tuyến tính theo chính sách cố định.
- (b) Sarsa tuyến tính với $\pi_w$.
- (c) Q-learning tuyến tính.
- (d) Monte Carlo tuyến tính với dữ liệu khác chính sách và lấy mẫu quan trọng.
:::

::: hint
Ba câu kiểm: tham số có dùng chung; mục tiêu có chứa ước lượng đang học; phân phối dữ liệu có khác chính sách đích.
:::

::: solution
- **(a)** Xấp xỉ hàm, bootstrap; theo chính sách. Có bảo đảm theo Định lý 07.29 khi các giả thiết còn lại thỏa.
- **(b)** Xấp xỉ hàm, bootstrap; theo chính sách. Chưa đủ ba, nhưng $\pi_w$ đổi theo $w$ nên giả thiết 1 của Định lý 07.29 không thỏa; không có bảo đảm chung (Nhận xét 07.34).
- **(c)** Đủ ba; không có bảo đảm chung. Mệnh đề 07.37 là ví dụ phân kỳ của TD(0) khác chính sách cùng ba yếu tố; Q-learning có phản ví dụ tương tự phản ví dụ của Baird (Sutton và Barto, 2018, §11.2, tr. 263).
- **(d)** Xấp xỉ hàm, khác chính sách; không bootstrap. Không đủ ba. Định lý 07.17 không áp dụng nguyên văn, vì giả thiết 2 đòi lợi tức sinh theo $\pi$; lấy mẫu quan trọng ở ghi chú Bài 06, Mục 6 là công cụ để sửa kỳ vọng trong trường hợp này.

**Kiểm tra lại.** Chỉ (c) đủ ba yếu tố, phù hợp với bài giảng gốc (trang 37, 41).
:::

Như vậy, chúng ta đã viết Q-learning bán gradient (Định nghĩa 07.35, Thuật toán 07.36) và chỉ ra bằng Mệnh đề 07.37 rằng khi đủ bộ ba bất ổn (Định nghĩa 07.38), tham số có thể tăng không chặn. Tuy nhiên, các kết quả nằm ở bốn mục với giả thiết riêng. Trong Mục 6, chúng ta gom chúng thành bảng phạm vi và quy trình phân tích.

## 6. Phạm vi bảo đảm và phân tích một quy tắc cập nhật

Notebook Flappy Bird chạy Q-learning tuyến tính trên bốn khối với bước học hằng, được $28{,}86$ ống, và còn cài Double Q-learning, một quy tắc chưa được phân tích ở Mục 2–5. Trước khi đọc các số này như bằng chứng hội tụ hay phân kỳ, chúng ta cần biết mỗi kết quả đòi hỏi giả thiết nào và cách kiểm các giả thiết đó trên một cấu hình cụ thể.

<!-- note-topic-id: lec-07-topic-14 -->
### 6.1 Phạm vi các kết quả hội tụ

Bảng sau đặt mỗi phương pháp cạnh những giả thiết mà kết luận của nó không thể thiếu.

::: remark Nhận xét 07.40 (Phạm vi các kết quả của chương)
| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Monte Carlo gradient tuyến tính | $\pi$, $\mu$ cố định; mẫu độc lập; đặc trưng bị chặn; $\mathbb E[G^2]<\infty$; $\Sigma_\mu$ xác định dương; Robbins–Monro | hội tụ tới $w_{\mathrm{MC}}$, hình chiếu của $v_\pi$ (Định lý 07.17) |
| TD(0) bán gradient tuyến tính | theo chính sách, $\pi$ cố định; chuỗi tối giản, không tuần hoàn; bài toán không kết thúc; $\gamma<1$; phần thưởng bị chặn; cột của $\Phi$ độc lập; Robbins–Monro | hội tụ tới $w_{\mathrm{TD}}$ (Định lý 07.29) |
| Sarsa bán gradient | $\pi_w$ đổi theo $w$ | không có kết quả chung (Nhận xét 07.34) |
| Q-learning bán gradient | đủ bộ ba bất ổn | không có bảo đảm chung; phản ví dụ: TD(0) khác chính sách cùng ba yếu tố (Mệnh đề 07.37); với Q-learning, phản ví dụ tương tự phản ví dụ của Baird (Sutton và Barto, 2018, §11.2, tr. 263) |
| Hàm phi tuyến, mạng nơ-ron | — | cần phân tích riêng (Bài 08) |

Hai dòng đầu khác đích (Ví dụ 07.11). Các vấn đề còn mở theo bài giảng gốc (trang 43) gồm lý thuyết cho xấp xỉ sâu, bộ ba bất ổn và học biểu diễn.
:::

<!-- note-topic-id: lec-07-topic-12 -->
### 6.2 Năm bước phân tích một quy tắc cập nhật

Để dùng bảng của Nhận xét 07.40 cho một quy tắc cụ thể, chúng ta kiểm lần lượt năm điều sau.

::: remark Nhận xét 07.41 (Năm bước phân tích)
1. Đặc trưng trên trạng thái hay trên cặp; số chiều của $x$ và $w$.
2. Mục tiêu có chứa $w$ không: gradient đầy đủ (Định nghĩa 07.12) hay bán gradient (Định nghĩa 07.21).
3. Công thức cập nhật và đại lượng giữ cố định khi lấy đạo hàm.
4. Chính sách hành vi và chính sách đích: theo hay khác chính sách; cố định hay đổi theo $w$.
5. Đối chiếu một dòng của Nhận xét 07.40; chỉ nêu hội tụ khi mọi giả thiết của dòng đó thỏa.
:::

::: example Ví dụ 07.16 (Năm bước cho TD(0) tuyến tính với chính sách cố định)
**Dữ kiện.** Thuật toán 07.22 với $\pi$ cố định, $\alpha_n=1/(n+1)$, trên chuỗi hữu hạn, tối giản, không tuần hoàn; bài toán không kết thúc; phần thưởng bị chặn; $\gamma=0{,}9$; cột của $\Phi$ độc lập.

**Áp dụng năm bước.**

1. Đặc trưng trên trạng thái; $x(s),w\in\mathbb R^d$.
2. Mục tiêu $R_{t+1}+\gamma x(S_{t+1})^\top w_n$ chứa $w_n$: bán gradient.
3. $w_{n+1}=w_n+\alpha_n\delta_tx(S_t)$, mục tiêu giữ cố định.
4. Dữ liệu và chính sách đích đều là $\pi$ cố định: theo chính sách.
5. Khớp dòng TD, kể cả "không kết thúc" và "phần thưởng bị chặn"; $1/(n+1)$ thỏa Robbins–Monro (Bài tập 07.6). Kết luận: $w_n\to w_{\mathrm{TD}}$ hầu chắc chắn (Định lý 07.29).

**Kiểm tra lại.** Với bước hằng $0{,}01$, bước 5 không khớp và không kết luận được hội tụ.
:::

Năm bước áp cho Double Q-learning của notebook Flappy Bird cho cùng kết luận như Bài tập 07.18: mục tiêu vẫn bootstrap, dữ liệu vẫn khác chính sách và tham số dùng chung, nên đủ bộ ba bất ổn và không có bảo đảm chung.

Như vậy, bảo đảm hội tụ của chương chỉ phủ dự đoán với chính sách cố định (Nhận xét 07.40); điều khiển tuyến tính không có bảo đảm chung, và Q-learning có phản ví dụ phân kỳ tương tự phản ví dụ của Baird (Sutton và Barto, 2018, §11.2, tr. 263). Bài 08 thay $x(s,a)^\top w$ bằng mạng nơ-ron trong Deep Q-Network, dùng mạng mục tiêu và bộ nhớ phát lại (replay buffer); bảo đảm tuyến tính không tự chuyển sang thiết lập đó.

## Tình huống áp dụng và ứng dụng

::: application Tình huống 07.1 (Dự đoán giá trị trên Lunar Lander bằng Monte Carlo và TD tuyến tính)
**Bài toán.** Trong notebook Lunar Lander, cần dự đoán giá trị của chính sách $\pi$: với xác suất $0{,}1$ chọn hành động ngẫu nhiên đều, còn lại theo bộ điều khiển viết tay của Gymnasium. Dữ liệu gồm $2\,000$ lượt huấn luyện, $500$ lượt kiểm tra; $\gamma=0{,}99$; lượt bị cắt ngắn ở $1\,000$ bước.

**Mô hình hóa.** Định nghĩa 07.5 với Fourier bậc 3 ($d=156$) và thước đo $J_{\mathrm{kt}}$; Monte Carlo là Thuật toán 07.15 và nghiệm theo lô; TD là Thuật toán 07.22 và LSTD (Mệnh đề 07.25, 07.26).

**Kiểm giả thiết.**

- $\pi$ cố định, theo chính sách: thỏa.
- Cột của $\Phi$ độc lập: hạng $156/156$; thỏa trên dữ liệu.
- Robbins–Monro: không thỏa, bước hằng.
- Mẫu độc lập (Định lý 07.17): không thỏa trong một lượt.
- Bài toán không kết thúc (Định lý 07.29): không thỏa.
- Trạng thái Markov: chưa chắc, quan sát thiếu địa hình.

**Số liệu** (một lần chạy đã nhúng trong notebook). $J_{\mathrm{kt}}$ bằng $5\,797{,}1$ với $\hat v\equiv0$; $3\,021{,}2$ với hằng số tốt nhất; $1\,626{,}8$ với bảng $9\,216$ ô; $2\,190{,}1$ và $1\,855{,}2$ với Monte Carlo và TD một lượt; $1\,481{,}0$ với Monte Carlo theo lô; $1\,622{,}2$ với LSTD trên cùng các lượt kết thúc thật.

**Diễn giải.** Hàm tuyến tính $156$ tham số có $J_{\mathrm{kt}}$ thấp hơn bảng $9\,216$ ô nhờ tổng quát hóa (Mệnh đề 07.2). Hai nghiệm theo lô khác nhau vì khác đích (Ví dụ 07.11), và $J_{\mathrm{kt}}$ đo khoảng cách tới đích của Monte Carlo. Khoảng cách giữa nghiệm một lượt và nghiệm theo lô là sai số ước lượng (Định nghĩa 07.11).

**Giới hạn.** Ba giả thiết không thỏa và một giả thiết chưa chắc, nên Định lý 07.17 và 07.29 không áp dụng nguyên văn; các số là của một lần chạy.
:::

::: application Tình huống 07.2 (Q-learning tuyến tính khi giả thiết theo chính sách không thỏa)
**Bài toán.** Trên Flappy Bird ($12$ biến liên tục, hai hành động), $\hat q$ được học bằng Thuật toán 07.36 với bốn khối, $d=3k+3$. Cần biết Định lý 07.29 có cho kết luận hội tụ không, và đọc $\lVert w\rVert$ thế nào.

**Kiểm giả thiết.**

- Bootstrap: mục tiêu (5.1) chứa $w$.
- Khác chính sách: dữ liệu theo $\pi_w$, mục tiêu theo chính sách tham lam.
- Xấp xỉ hàm: tham số dùng chung.
- Giả thiết 1 của Định lý 07.29 không thỏa (Nhận xét 07.34, Định nghĩa 07.38); giả thiết 4 không thỏa với mã hóa bốn khối (Nhận xét 07.9).

**Áp dụng.** Đủ bộ ba bất ổn: không có bảo đảm chung. Mệnh đề 07.37 cho thấy, với TD(0) khác chính sách cùng ba yếu tố, tham số có thể tăng không chặn; Q-learning có phản ví dụ tương tự phản ví dụ của Baird (Sutton và Barto, 2018, §11.2, tr. 263).

**Số liệu** (chép lại từ Mục 5.2 và notebook). Bảng thử nghiệm khi soạn: với `poly2` ($k=15$), $\lVert w\rVert$ lớn nhất $1\,895{,}1$ với Q-learning và $15{,}1$ với Sarsa, cả hai $0$ ống. Với `four3`, lần chạy đã nhúng trong notebook cho $\lVert w\rVert$ cuối $6{,}86$ với Q-learning và $5{,}08$ với Sarsa sau $4\,000$ lượt.

**Diễn giải và giới hạn.** Theo Nhận xét 07.39, $\lVert w\rVert$ lớn trên `poly2` phù hợp với bộ ba bất ổn trên một lớp hàm kém nhưng chưa phải bằng chứng phân kỳ; đường bị chặn trên `four3` cũng không chứng minh hội tụ. Muốn kết luận phải đo $\lVert w\rVert$ theo lượt trên nhiều hạt giống.
:::

**Ứng dụng.**

- **Bài 08 (Deep Q-Network)** giữ mục tiêu (5.1), thay $x(s,a)^\top w$ bằng mạng nơ-ron, dùng mạng mục tiêu và bộ nhớ phát lại để giảm bất ổn của Mục 5.2.
- **Bài 09 (Double DQN)** xử lý độ chệch do phép cực đại, phù hợp với hiệu ghép cặp $+12{,}4\pm2{,}2$ (nửa khoảng tin cậy $95\%$) đo trên Lunar Lander.
- **Bài 09–11 (gradient chính sách)** dùng TD với xấp xỉ hàm để đánh giá; khi chính sách được giữ cố định, Định lý 07.29 nêu giả thiết của bảo đảm.
- **Hai notebook Bài 07** dùng Định lý 07.17, Mệnh đề 07.26 để đọc $J_{\mathrm{kt}}$ và Định nghĩa 07.38 để đọc $\lVert w\rVert$ (Tình huống 07.1, 07.2).

## Tóm tắt chương

Chúng ta bắt đầu từ giới hạn của bảng: Lunar Lander rời rạc hóa có $9\,216$ ô nhưng chỉ $1\,896$ ô có dữ liệu (Ví dụ 07.1). Bảng được thay bằng hàm tuyến tính theo đặc trưng (Định nghĩa 07.1), trong đó một cập nhật lan theo tích vô hướng của các đặc trưng (Mệnh đề 07.2), và chất lượng được đo bằng $J_\mu$ (Định nghĩa 07.5). Thay $v_\pi$ bằng lợi tức cho Monte Carlo gradient, hội tụ tới hình chiếu của $v_\pi$ khi mẫu độc lập và bước học thỏa Robbins–Monro (Định lý 07.17). Thay bằng mục tiêu bootstrap cho TD(0) bán gradient, hội tụ tới điểm cố định Bellman chiếu dưới giả thiết theo chính sách của Định lý 07.29. Với điều khiển, Sarsa mất giả thiết chính sách cố định (Nhận xét 07.34), còn Q-learning có đủ bộ ba bất ổn: ví dụ TD(0) khác chính sách cùng ba yếu tố cho tham số tăng không chặn (Mệnh đề 07.37), và Q-learning có phản ví dụ phân kỳ tương tự phản ví dụ của Baird (Sutton và Barto, 2018, §11.2, tr. 263). Bài 08 thay hàm tuyến tính bằng mạng nơ-ron, nơi các bảo đảm này không còn tự động đúng.

**Định nghĩa và kết quả theo mục.**

- Mục 1: $\hat v=x^\top w$ (Định nghĩa 07.1); mức lan $\alpha e\,x(s')^\top x(s)$ (Mệnh đề 07.2); đặc trưng chỉ thị cho lại bảng (Hệ quả 07.3); lớp hàm khác (Nhận xét 07.4); $J_\mu$ (Định nghĩa 07.5); lớp biểu diễn là không gian cột của $\Phi$ (Định nghĩa 07.6); bốn khối, $d=k+m+mk+1$ (Định nghĩa 07.7); thiếu khối Kronecker thì tham lam như nhau mọi nơi (Mệnh đề 07.8); bốn khối không đủ hạng cột (Nhận xét 07.9); cận (1.5) khi hai trạng thái cùng đặc trưng (Mệnh đề 07.10); sai số xấp xỉ không giảm theo dữ liệu (Định nghĩa 07.11).
- Mục 2: mục tiêu không chứa $w$ cho gradient đầy đủ (Định nghĩa 07.12); $\mathbb E[G_t\mid S_t]=v_\pi(S_t)$ (Mệnh đề 07.13); $\mathbb E[\nabla\ell_t]=\nabla J_\mu$ (Mệnh đề 07.14); Thuật toán 07.15; mất mát kỳ vọng bằng $2J_\mu$ cộng phương sai (Bổ đề 07.16); $w_n\to w_{\mathrm{MC}}$ (Định lý 07.17); Robbins–Monro với tham số dùng chung (Nhận xét 07.18).
- Mục 3: mục tiêu TD (Định nghĩa 07.19), độ chệch của nó (Mệnh đề 07.20); bán gradient (Định nghĩa 07.21); Thuật toán 07.22; cắt ngắn vẫn bootstrap (Nhận xét 07.23); $\Pi_DT_\pi$ (Định nghĩa 07.24); $\mathbb E[\delta_tx(S_t)]=b-Aw$ (Mệnh đề 07.25); $b-Aw=0\iff\Phi w=\Pi_DT_\pi\Phi w$ (Mệnh đề 07.26); $\lVert P_\pi v\rVert_D\le\lVert v\rVert_D$ (Bổ đề 07.27); $A$ xác định dương (Mệnh đề 07.28); $w_n\to w_{\mathrm{TD}}$ (Định lý 07.29); so sánh (Nhận xét 07.30).
- Mục 4: $\pi_w$ (Định nghĩa 07.31); hiệu $-2[w]_2$ trên chuỗi (Mệnh đề 07.32); Thuật toán 07.33; Sarsa không có bảo đảm chung (Nhận xét 07.34).
- Mục 5: mục tiêu cực đại (Định nghĩa 07.35); Thuật toán 07.36; $w_n=(1+\alpha(2\gamma-1))^nw_0$ (Mệnh đề 07.37); ba yếu tố (Định nghĩa 07.38); "có thể phân kỳ" nói về một lớp phương pháp (Nhận xét 07.39).
- Mục 6: bảng giả thiết (Nhận xét 07.40); năm bước phân tích (Nhận xét 07.41).

**Công thức cần nhớ.**

Cập nhật dự đoán với mục tiêu Monte Carlo hoặc TD(0):

$$
w_{n+1}=w_n+\alpha_n\big(y_t-x(S_t)^\top w_n\big)x(S_t),\qquad y_t=G_t\ \text{hoặc}\ y_t=R_{t+1}+\gamma\,x(S_{t+1})^\top w_n .
$$

Cập nhật điều khiển với mục tiêu Sarsa hoặc Q-learning:

$$
w_{n+1}=w_n+\alpha_n\big(y_t-x(S_t,A_t)^\top w_n\big)x(S_t,A_t),\qquad y_t=R_{t+1}+\gamma\,x(S_{t+1},A_{t+1})^\top w_n\ \text{hoặc}\ y_t=R_{t+1}+\gamma\max_{a'}x(S_{t+1},a')^\top w_n .
$$

Hướng trung bình và điểm cố định của TD(0) tuyến tính:

$$
\mathbb E[\delta_tx(S_t)]=b-Aw,\qquad \Phi w_{\mathrm{TD}}=\Pi_DT_\pi(\Phi w_{\mathrm{TD}})\iff Aw_{\mathrm{TD}}=b .
$$

**Giả thiết hay bị bỏ quên.**

- $\mu$ là trọng số tùy chọn, $d_\pi$ là phân phối dừng; Định lý 07.29 dùng $d_\pi$.
- Bảo đảm của TD(0) tuyến tính cần dữ liệu theo chính sách, chính sách cố định và bài toán không kết thúc.
- Cột của $\Phi$ độc lập; mã hóa bốn khối không thỏa.
- Bước học hằng không thỏa Robbins–Monro.
- Lượt bị cắt ngắn không phải lượt kết thúc; mục tiêu vẫn bootstrap.
- Monte Carlo với hàm xấp xỉ là gradient đầy đủ.

## Bài tập củng cố

Bộ bài giao chính thức của buổi học là [Bài tập Bài 07](material-viewer.html?doc=materials/lec-07/exercises.md&deck=lecture-07-xap-xi-ham.html). Tệp giữ số hiệu và kết quả của tám bài tập thân chương 07.3, 07.5, 07.7, 07.8, 07.10, 07.11, 07.13, 07.14, thêm Bài tập 07.20–07.25 (giới hạn của bảng tra, bốn dãy bước học, điểm dừng trung bình của TD(0), Q-learning trên một mảnh MDP hai trạng thái, hai bài lập trình trên hai notebook của bài) và không lặp các đề 07.15–07.19 dưới đây.

### Mức nhận biết

::: exercise Bài tập 07.15 (Số đại lượng cần học)
Trên Lunar Lander, thực hành Bài 06 dùng bảng $Q$ trên $2\,187$ ô với $4$ hành động; notebook Bài 07 dùng mã hóa bốn khối trên Fourier bậc 3 với $k=156$.

- (a) Tính số đại lượng cần học của mỗi cách.
- (b) Một mẫu tại $(s,a)$ đổi những ước lượng nào.
- (c) Nêu cái giá của tham số dùng chung.
:::

::: hint
Định nghĩa 07.7 cho $d$; Hệ quả 07.3 và Mệnh đề 07.2 cho (b).
:::

::: solution
**(a)** Bảng: $2\,187\cdot4=8\,748$. Bốn khối: $156+4+624+1=785$.

**(b)** Bảng: chỉ ô $(s,a)$. Bốn khối: mọi cặp có $x(s',a')^\top x(s,a)\ne0$.

**(c)** Sai lệch lan sang cặp khác, và lớp hàm có thể không chứa giá trị thật (Định nghĩa 07.11).

**Kiểm tra lại.** $4\cdot156=624$.
:::

::: exercise Bài tập 07.16 (Đặc trưng khoảng cách trên chuỗi năm trạng thái)
Chuỗi $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ với $\mathrm A$, $\mathrm E$ kết thúc; hành động $0$ đi trái, $1$ đi phải, chuyển tất định; vào $\mathrm A$ nhận $1\,000$, vào $\mathrm E$ nhận $10$, chuyển khác nhận $-1$; tối đa ba bước mỗi lượt; $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$.

- (a) Với $\gamma=1$, tính $v_\pi$ tại $\mathrm B$, $\mathrm C$, $\mathrm D$ cho chính sách luôn đi trái và luôn đi phải.
- (b) Với $x(s)=(d_{\text{trái}}(s);1)$, giá trị nào thuộc lớp biểu diễn, với $w$ nào.
- (c) Lặp lại (a), (b) với chính sách luôn đi trái và $\gamma=0{,}5$.
:::

::: hint
$(v_{\mathrm B};v_{\mathrm C};v_{\mathrm D})$ thuộc lớp khi và chỉ khi $v_{\mathrm C}-v_{\mathrm B}=v_{\mathrm D}-v_{\mathrm C}$.
:::

::: solution
**(a)** Trái: $(1\,000;999;998)$. Phải: $(8;9;10)$; cả hai đi tới trạng thái kết thúc trong tối đa ba bước.

**(b)** Cả hai thuộc lớp: $1\,001-d_{\text{trái}}$ với $w=(-1;1\,001)$, và $7+d_{\text{trái}}$ với $w=(1;7)$; sai số xấp xỉ bằng $0$.

**(c)** $v(\mathrm B)=1\,000$, $v(\mathrm C)=-1+500=499$, $v(\mathrm D)=-1+249{,}5=248{,}5$; hai hiệu $-501$ và $-250{,}5$ khác nhau, nên không thuộc lớp và sai số xấp xỉ dương khi mọi trọng số dương.

**Kiểm tra lại.** $1\,001-3=998$, $7+1=8$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 07.17 (Khi giá trị thật thuộc lớp biểu diễn)
Trong bối cảnh của Định nghĩa 07.24, giả sử $v_\pi=\Phi w^*$. Chứng minh $w^*$ cực tiểu hóa $J_\mu$ với mọi $\mu$ và là điểm cố định Bellman chiếu, nên $w_{\mathrm{MC}}=w_{\mathrm{TD}}=w^*$ khi hai điểm này duy nhất.
:::

::: hint
$J_\mu(w^*)=0$; $T_\pi v_\pi=v_\pi$; $\Pi_Du=u$ khi $u$ thuộc lớp.
:::

::: solution
**Bước 1 (Monte Carlo).** $J_\mu(w^*)=\tfrac12\lVert v_\pi-\Phi w^*\rVert_\mu^2=0\le J_\mu(w)$.

**Bước 2 (TD).** $\Pi_DT_\pi(\Phi w^*)=\Pi_DT_\pi v_\pi=\Pi_Dv_\pi=\Pi_D\Phi w^*=\Phi w^*$, lần lượt do giả thiết, điểm cố định của $T_\pi$, giả thiết, và hình chiếu giữ nguyên phần tử của lớp.

**Bước 3 (duy nhất).** Theo Định lý 07.17 và Mệnh đề 07.28, cả hai bằng $w^*$.

**Kiểm tra lại.** Trong Ví dụ 07.11, $v_\pi=(5{,}5;4{,}5)$ không tỉ lệ với $(1;2)$, và phép tính ở đó cho hai điểm khác nhau. Điều kiện của bài tập là đủ, không phải cần.
:::

### Mức vận dụng

::: exercise Bài tập 07.18 (Phân tích Q-learning tuyến tính trên Flappy Bird)
Trên Flappy Bird, $\hat q$ được học bằng Q-learning bán gradient với mã hóa bốn khối trên Fourier bậc 3 ($k=256$, hai hành động) và bước hằng. Áp dụng năm bước của Nhận xét 07.41 và kết luận về hội tụ.
:::

::: hint
Ở bước 5, so với hai dòng cuối của Nhận xét 07.40.
:::

::: solution
1. Đặc trưng trên cặp; $d=256+2+512+1=771$.
2. Mục tiêu (5.1) chứa $w$: bán gradient.
3. $w\leftarrow w+\alpha(y-x(S,A)^\top w)x(S,A)$, $y$ giữ cố định.
4. Hành vi $\varepsilon$-tham lam, đích tham lam: khác chính sách; chính sách đổi theo $w$.
5. Đủ bộ ba bất ổn, bốn khối không đủ hạng cột, bước hằng: không dòng nào cho bảo đảm; không suy ra được hội tụ.

**Kiểm tra lại.** $d=3k+3=771$.
:::

::: exercise Bài tập 07.19 (Chọn phương pháp dự đoán khi có lượt bị cắt ngắn)
Dữ liệu Lunar Lander có $2\,000$ lượt, trong đó $42$ lượt bị cắt ngắn ở $1\,000$ bước, chiếm $7{,}7\%$ số chuyển.

- (a) Thuật toán 07.15 và 07.22 xử lý các lượt này thế nào.
- (b) Mỗi nghiệm theo lô hướng tới đâu.
- (c) Vì sao $J_{\mathrm{kt}}$ của LSTD ($1\,622{,}2$) lớn hơn của Monte Carlo theo lô ($1\,481{,}0$) không chứng tỏ TD kém hơn khi làm thành phần đánh giá của một thuật toán điều khiển.
:::

::: hint
Nhận xét 07.23, chứng minh Định lý 07.17, Mệnh đề 07.26 và định nghĩa $J_{\mathrm{kt}}$, $\bar g$ ở Mục 1.3.
:::

::: solution
**(a)** Monte Carlo bỏ các lượt này vì lợi tức chưa đầy đủ; TD bootstrap tại bước cắt ngắn và dùng mọi chuyển (Nhận xét 07.23).

**(b)** Monte Carlo theo lô cho hình chiếu theo $\lVert\cdot\rVert_\mu$ của $\bar g$ lên lớp biểu diễn, với $\mu$ là phân phối ghé trên các lượt kết thúc thật và $\bar g$ lấy theo phân phối đó (Bước 1 và Bước 4 của chứng minh Định lý 07.17, áp cho phân phối thực nghiệm). $\bar g$ trùng $v_\pi$ khi trạng thái có tính Markov và không bỏ lượt nào; bỏ các lượt cắt ngắn có thể làm lệch phân phối ghé và $\bar g$. LSTD cho điểm cố định Bellman chiếu thực nghiệm (Mệnh đề 07.26).

**(c)** $J_{\mathrm{kt}}$ đo khoảng cách tới lợi tức, đúng đích của Monte Carlo. TD cập nhật trực tuyến, dùng được lượt cắt ngắn và có mục tiêu phương sai thường nhỏ hơn (Nhận xét 07.30); lựa chọn phụ thuộc nhu cầu.

**Kiểm tra lại.** $1\,622{,}2$ đo trên đúng các lượt kết thúc thật, nên chênh lệch không đến từ lượt cắt ngắn.
:::

<!-- note-topic-id: lec-07-topic-18 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

- Tạ Việt Cường (2026). *Lecture 07: Hàm xấp xỉ trong Reinforcement Learning*, bài giảng gốc (2025–2026), trang 1–45: phạm vi và thứ tự; Mục 1 dựa trên trang 22–31, Mục 2 trên trang 27, 32–34, Mục 3 trên trang 35–37, Mục 4 trên trang 38–40, Mục 5 trên trang 38, 41, Mục 6 trên trang 41–45.
- Tạ Việt Cường (2026). *Bài tập tuần 7 — Function Approximation* (2025–2026), bài 1–8: Bài tập 07.5, 07.6, 07.8–07.11, 07.14 và chuỗi năm trạng thái; bài 1 và bài 5 còn là Bài tập 07.20 và 07.22 của tệp bài tập.
- Sutton, R. S. và Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2: §9.1–9.4 cho Mục 1–3; §9.5, 9.6, 9.8 cho đặc trưng, bước học, LSTD; §10.1 cho Mục 4; §6.7, 11.2–11.3 cho Mục 5.
- Bertsekas, D. P. và Tsitsiklis, J. N. (1996). *Neuro-Dynamic Programming*: chương 4 cho Định lý 07.17; chương 6 cho Định lý 07.29.
- Tsitsiklis, J. N. và Van Roy, B. (1997). An analysis of temporal-difference learning with function approximation. *IEEE Transactions on Automatic Control* 42(5): Định lý 07.29.
- Zou, S., Xu, T. và Liang, Y. (2019). Finite-sample analysis for SARSA with linear function approximation. *NeurIPS*: Nhận xét 07.34.
- Đọc thêm về MDP tuyến tính: Jin, Yang, Wang và Jordan (2020), *COLT*. Bài giảng gốc (trang 42) chỉ nêu bậc kết quả: trong MDP tuyến tính theo lượt với $d$ đặc trưng và chân trời $H$, một biến thể lạc quan của lặp giá trị bình phương tối thiểu (least-squares value iteration, LSVI) có độ hối tiếc (regret), tức tổng thiệt hại so với chính sách tối ưu, bậc $\tilde O(\sqrt{d^3H^3N})$ sau $N$ bước.
- Giáo trình *Học máy thống kê*, chương 6: giọng kể, thuật ngữ, tương ứng ký hiệu.
- Hai notebook thực hành Bài 07 (Lunar Lander, Flappy Bird): nguồn của mọi số liệu thực hành.
- **Bài tập.** [Bài tập Bài 07](material-viewer.html?doc=materials/lec-07/exercises.md&deck=lecture-07-xap-xi-ham.html), bộ bài giao chính thức ở ba mức: tám bài trùng bài tập thân chương, Bài tập 07.20–07.25 là bài mới, trong đó 07.24 và 07.25 là bài lập trình trên hai notebook; bảng đầu tệp gắn từng bài với một mạch nội dung của bài học.
