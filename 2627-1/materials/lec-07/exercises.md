# Bài tập Bài 07 — Xấp xỉ hàm trong Học tăng cường

Bộ bài tập gồm mười bốn bài, phủ năm mạch nội dung 2–6 của bài học, ở ba mức: nhận biết (07.20, 07.21); tính toán hoặc chứng minh (07.3, 07.5, 07.7, 07.8, 07.10, 07.11, 07.13, 07.22); vận dụng vào bài toán Học tăng cường (07.14, 07.23, 07.24, 07.25). Tám bài 07.3, 07.5, 07.7, 07.8, 07.10, 07.11, 07.13 và 07.14 là bài tập trong các mục của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html) Bài 07 có trang "Bài tập: …" trên trang chiếu. Các bài này giữ số hiệu và kết quả của ghi chú, được phát biểu lại đủ dữ kiện; dòng "Trùng trang chiếu" dẫn tới trang đề bài và trang lời giải, và lời giải trong tệp cho cùng kết quả với lời giải trên trang. Sáu bài tập khác trong các mục của ghi chú (07.1, 07.2, 07.4, 07.6, 07.9, 07.12) không có trang bài tập trên trang chiếu; bảng dưới ghi chúng ở dạng "ghi chú: 07.k" và không chép lại. Bài tập 07.15–07.19 thuộc mục "Bài tập củng cố" của ghi chú và cũng không chép lại. Bài tập 07.18 có trang bài tập tổng hợp ở mạch 7 của trang chiếu nhưng thuộc "Bài tập củng cố", nên bảng dẫn tới ghi chú và tới trang đó. Sáu bài 07.20–07.25 chỉ có trong tệp này, tiếp nối bộ đếm Bài tập của ghi chú và đánh số theo thứ tự xuất hiện; hai bài 07.24 và 07.25 là bài [Lập trình] trên hai notebook thực hành của bài.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-07-xap-xi-ham.html#/1/1) | — |
| 2. Hàm giá trị tuyến tính theo đặc trưng | [Mở phần](lecture-07-xap-xi-ham.html#/2/1) | 07.3, 07.20; [ghi chú: 07.1 (Mục 1.2), 07.2 (Mục 1.3)](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html) |
| 3. Monte Carlo gradient với hàm xấp xỉ | [Mở phần](lecture-07-xap-xi-ham.html#/3/1) | 07.5, 07.21, 07.24; [ghi chú: 07.4 (Mục 2.1), 07.6 (Mục 2.3)](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html) |
| 4. TD(0) bán gradient và điểm cố định Bellman chiếu | [Mở phần](lecture-07-xap-xi-ham.html#/4/1) | 07.7, 07.8, 07.22, 07.24; [ghi chú: 07.9 (Mục 3.3)](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html) |
| 5. Sarsa bán gradient cho điều khiển | [Mở phần](lecture-07-xap-xi-ham.html#/5/1) | 07.10, 07.11, 07.25; [ghi chú: 07.12 (Mục 4.3)](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html) |
| 6. Q-learning bán gradient và bộ ba bất ổn | [Mở phần](lecture-07-xap-xi-ham.html#/6/1) | 07.13, 07.14, 07.23, 07.25 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-07-xap-xi-ham.html#/7/1) | [ghi chú: 07.18 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html); trang [Bài tập: phân tích Q-learning tuyến tính trên Flappy Bird](lecture-07-xap-xi-ham.html#/7/6) và [trang lời giải](lecture-07-xap-xi-ham.html#/7/7) |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 07. Giá trị ước lượng là hàm tuyến tính theo đặc trưng (feature): $\hat v(s,w)=x(s)^\top w$ cho giá trị trạng thái, $\hat q(s,a,w)=x(s,a)^\top w$ cho giá trị hành động, với vector đặc trưng $x(s)$ hoặc $x(s,a)$ và tham số dùng chung $w\in\mathbb R^d$. Giá trị thật là $v_\pi$, $q_\pi$, $q_*$. Phần thưởng (reward) $R_{t+1}$ gắn với chuyển $S_t\to S_{t+1}$; lợi tức (return) $G_t=R_{t+1}+\gamma G_{t+1}$ với $G_T=0$ ở thời điểm kết thúc $T$ của lượt (episode); giá trị tại trạng thái kết thúc bằng $0$. Chỉ số $n$ đếm số lần cập nhật, $t$ là thời điểm của mẫu dùng trong lần cập nhật đó; $\alpha_n$ là bước học của lần cập nhật từ $w_n$, $\alpha$ là bước học hằng. Hai giá trị trong một sai số TD dùng tham số trước cập nhật. $(a;b)$ là vector cột hai thành phần; bất đẳng thức giữa hai vector hiểu theo từng thành phần. Số thập phân viết với dấu phẩy.

Thuật ngữ và chữ viết tắt dùng trong tệp: sai phân thời gian (temporal difference, TD); bán gradient (semi-gradient); mục tiêu bootstrap (bootstrap target), tức mục tiêu chứa ước lượng hiện tại; theo chính sách (on-policy) và khác chính sách (off-policy); bộ ba bất ổn (deadly triad); nhập nhằng đặc trưng (aliasing); phân phối dừng (stationary distribution); hạ gradient ngẫu nhiên (stochastic gradient descent, SGD); TD bình phương tối thiểu (least-squares TD, LSTD); quá trình quyết định Markov (Markov decision process, MDP).

Ba bộ dữ kiện được dùng ở nhiều bài; mỗi bài dùng chúng đều nêu lại dữ kiện trong khối đề bài.

- **Chuỗi năm trạng thái** (bài giảng gốc 2025–2026, trang 40; Bài tập tuần 7, phần C). Trạng thái $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$; $\mathrm D$ là trạng thái đầu; $\mathrm A$, $\mathrm E$ kết thúc. Hành động $0$ đi trái, $1$ đi phải, chuyển tất định. Vào $\mathrm A$ nhận $1\,000$, vào $\mathrm E$ nhận $10$, mọi chuyển khác nhận $-1$; $\gamma=1$; tối đa ba bước mỗi lượt. Đặc trưng $x(s,a)=(d_{\text{trái}}(s);u(a);1)$ với khoảng cách tới tường trái $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$ và dấu của hành động $u(0)=1$, $u(1)=-1$; tham số đầu $w_0=(1;1;-1)$.
- **Hai trạng thái với đặc trưng 1 và 2.** $x(s_1)=1$, $x(s_2)=2$, nên $\Phi=(1;2)$ và $\hat v=(w;2w)$ với $w\in\mathbb R$. Bộ đặc trưng này đi với ba mô hình khác nhau: Ví dụ 07.11 của ghi chú (chuyển đều tới hai trạng thái, $r_\pi=(1;0)$, $d_\pi=(\tfrac12;\tfrac12)$); Bài tập 07.8 (cùng chuyển, $r_\pi=(0;1)$); Bài tập 07.22(c) (từ $s_2$ luôn về $s_1$, $r_\pi=(1;0)$, $d_\pi=(\tfrac23;\tfrac13)$).
- **Hai notebook thực hành** `thuc-hanh-lunarlander-xap-xi-tuyen-tinh.ipynb` và `thuc-hanh-flappybird-dieu-khien-tuyen-tinh.ipynb`. Mọi số liệu thực hành trong tệp là một lần chạy đã nhúng trong notebook, hoặc của bảng thử nghiệm khi soạn được nhúng trong notebook.

Mọi bộ số không ghi nguồn là số liệu sư phạm tự xây dựng. Lời giải nêu kết quả được dùng ở từng bước; số hiệu "Định nghĩa 07.k", "Mệnh đề 07.k", "Định lý 07.k" chỉ khối của ghi chú bài giảng.

## Mức nhận biết

### Bài tập 07.20. Giới hạn của bảng tra và hai lợi ích của xấp xỉ hàm

**Mức độ:** nhận biết. Mục tiêu học tập 1 của ghi chú.

**Nguồn:** Bài tập tuần 7 (2025–2026), bài 1; ghi chú bài giảng Bài 07, Mục 1.1–1.2; số liệu của thực hành Bài 05 và hai notebook Bài 07 (một lần chạy đã nhúng trong notebook).

::: exercise Bài tập 07.20 (Giới hạn của bảng tra và hai lợi ích của xấp xỉ hàm)
Flappy Bird có quan sát gồm $12$ biến liên tục và $2$ hành động; một bảng $Q$ được dựng bằng cách chia mỗi biến thành $10$ khoảng. Thực hành Bài 05 chia trạng thái Lunar Lander thành $9\,216$ ô; $2\,000$ lượt huấn luyện gồm $546\,869$ chuyển chỉ ghé $1\,896$ ô. Trong notebook Lunar Lander của Bài 07, đặc trưng tuyến tính thô có $9$ thành phần: hằng $1$, sáu biến liên tục đã chuẩn hóa về $[-1,1]$ và hai cờ chân chạm đất. Với $w_0=0$ và bước học $\alpha\approx0{,}00401$ (giá trị in ra đã làm tròn), cập nhật Monte Carlo đầu tiên tại $S_0$ có lợi tức $G_0=66{,}190$; sau cập nhật đó, dự đoán tại $S_1$ là $x(S_1)^\top w_1=0{,}5832$, dù $S_1$ chưa được cập nhật. Trong notebook Flappy Bird, $\hat q(s,a,w)=x(s,a)^\top w$ có $d=771$ tham số.

- (a) Tính số ô của bảng $Q$ cho Flappy Bird và số chuyển tối thiểu nếu mỗi ô cần ít nhất $10$ mẫu; so số chuyển đó với $546\,869$.
- (b) Từ (a) và số liệu Lunar Lander, nêu hai lý do bảng tra không phù hợp khi không gian trạng thái lớn hoặc liên tục.
- (c) Tính tích vô hướng $x(S_1)^\top x(S_0)$ suy ra từ ba số $\alpha$, $G_0$, $0{,}5832$. Xác định dự đoán tại $S_1$ sau cập nhật đó nếu dùng bảng tra và $S_0$, $S_1$ nằm ở hai ô khác nhau.
- (d) Đếm số phép nhân để tính $\hat q(s,\cdot,w)$ cho hai hành động và số đại lượng cần lưu với hàm tuyến tính của Flappy Bird; so với bảng ở (a), mỗi giá trị lưu bằng $8$ byte.
:::

::: hint Gợi ý Bài tập 07.20
Số ô là tích số khoảng của các biến nhân số hành động. Với (c), dùng Mệnh đề 07.2 cho cập nhật $w_1=w_0+\alpha e_0\,x(S_0)$; với bảng, $x(s)$ là vector chỉ thị của ô chứa $s$ (Hệ quả 07.3).
:::

::: solution Lời giải Bài tập 07.20
**Câu (a).** Số trạng thái rời rạc là $10^{12}$; nhân với $2$ hành động được $2\cdot10^{12}$ ô. Mỗi ô cần $10$ mẫu nên cần ít nhất $2\cdot10^{13}$ chuyển, gấp khoảng $3{,}66\cdot10^{7}$ lần $546\,869$.

**Câu (b).** Lý do thứ nhất là bộ nhớ và số mẫu: mỗi ô cần một giá trị và đủ lần ghé riêng. Với Lunar Lander, $546\,869$ chuyển chỉ phủ $1\,896/9\,216\approx20{,}6\%$ số ô; với Flappy Bird, số chuyển cần có ở (a) không đạt được trong thực hành. Lý do thứ hai là bảng không tổng quát hóa: hai trạng thái gần nhau nằm ở hai ô khác nhau không chia sẻ thông tin, nên mẫu ở ô này không cải thiện ô bên cạnh.

**Câu (c).** Vì $w_0=0$, sai lệch tại $S_0$ là $e_0=G_0$ và $w_1=\alpha G_0\,x(S_0)$. Theo Mệnh đề 07.2,

$$
\begin{aligned}
x(S_1)^\top w_1&=\alpha G_0\,x(S_1)^\top x(S_0),\\
x(S_1)^\top x(S_0)&=\frac{0{,}5832}{0{,}00401\cdot66{,}190}\approx2{,}2 .
\end{aligned}
$$

Tích vô hướng khác $0$, nên một mẫu tại $S_0$ đổi dự đoán tại $S_1$; thành phần hằng $1$ của hai vector góp số hạng $1$ vào tích đó. Đây là tổng quát hóa qua tham số dùng chung. Với bảng tra và hai ô khác nhau, $x(S_1)^\top x(S_0)=0$, nên dự đoán tại $S_1$ vẫn bằng giá trị khởi tạo $0$.

**Câu (d).** Mỗi giá trị $\hat q(s,a,w)$ là một tích vô hướng $771$ thành phần, nên hai hành động cần $2\cdot771=1\,542$ phép nhân, cộng một phép so sánh để chọn hành động tham lam, chưa kể chi phí tính $x(s,a)$. Hàm tuyến tính lưu $771$ số. Bảng ở (a) lưu $2\cdot10^{12}$ số, tức $1{,}6\cdot10^{13}$ byte. Chi phí của hàm tuyến tính không phụ thuộc số trạng thái và không cần xác định ô chứa trạng thái liên tục.

**Kiểm tra lại.** $2\cdot10^{13}/546\,869\approx3{,}66\cdot10^7$; ở (c), số $2{,}2$ chỉ xấp xỉ vì $\alpha$ in ra đã làm tròn. Lỗi thường gặp: cộng số khoảng thay vì nhân ($12\cdot10=120$ ô); kể dữ liệu không độc lập cùng phân phối như lý do riêng của bảng tra, trong khi khó khăn đó đúng với mọi biểu diễn (Mục 1.1 của ghi chú); cho rằng hai vector có chung một thành phần khác $0$ thì tích vô hướng chắc chắn khác $0$, trong khi các số hạng có thể triệt tiêu nhau.
:::

### Bài tập 07.21. Bốn dãy bước học và tổng bước hữu hạn

**Mức độ:** nhận biết ở câu (a), (b); tính toán ở câu (c). Mục tiêu học tập 6 của ghi chú: kiểm điều kiện Robbins–Monro trên một cấu hình cụ thể.

**Nguồn:** mở rộng Bài tập 07.6 của ghi chú bài giảng Bài 07 (Bài tập tuần 7, 2025–2026, bài 6) bằng bốn dãy bước học cụ thể; ghi chú, Mục 2.3 (giả thiết của Định lý 07.17 và phản ví dụ khi bỏ từng giả thiết), Nhận xét 07.18; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 07.21 (Bốn dãy bước học và tổng bước hữu hạn)
Dãy bước học dương $(\alpha_n)_{n\ge0}$, với $\alpha_n$ là bước học của lần cập nhật từ $w_n$, thỏa điều kiện Robbins–Monro khi $\sum_n\alpha_n=\infty$ và $\sum_n\alpha_n^2<\infty$. Xét bốn dãy $\alpha_n=1/(n+1)$, $\alpha_n=1/\sqrt{n+1}$, $\alpha_n=0{,}01$ và $\alpha_n=1/(n+1)^2$.

- (a) Với mỗi dãy, xác định điều kiện nào thỏa và điều kiện nào không.
- (b) Xác định dãy nào thỏa giả thiết về bước học của Định lý 07.17 (hội tụ của Monte Carlo gradient tuyến tính).
- (c) Một trạng thái duy nhất có $x(s)=1$, và mọi lượt cho lợi tức $G=10$, nên $v_\pi(s)=10$ và $w_{\mathrm{MC}}=10$. Cập nhật Monte Carlo là $w_{n+1}=w_n+\alpha_n(10-w_n)$ với $w_0=0$. Tính $w_1$, $w_2$ và $\lim_nw_n$ khi $\alpha_n=1/(n+2)$ và khi $\alpha_n=1/(n+2)^2$.
:::

::: hint Gợi ý Bài tập 07.21
Với (a), so với chuỗi điều hòa $\sum_k1/k=\infty$ và $\sum_k1/k^2=\pi^2/6$. Với (c), sai lệch $e_n=10-w_n$ thỏa $e_{n+1}=(1-\alpha_n)e_n$, nên $e_n=10\prod_{k=0}^{n-1}(1-\alpha_k)$; chỉ số được dịch thành $n+2$ để bước đầu nhỏ hơn $1$.
:::

::: solution Lời giải Bài tập 07.21
**Câu (a).**

| $\alpha_n$ | $\sum_n\alpha_n$ | $\sum_n\alpha_n^2$ | Robbins–Monro |
| --- | --- | --- | --- |
| $1/(n+1)$ | $\infty$ (chuỗi điều hòa) | $\pi^2/6<\infty$ | thỏa |
| $1/\sqrt{n+1}$ | $\infty$ | $\sum_k1/k=\infty$ | không, vi phạm điều kiện thứ hai |
| $0{,}01$ | $\infty$ | $\infty$ | không, vi phạm điều kiện thứ hai |
| $1/(n+1)^2$ | $\pi^2/6<\infty$ | $\pi^4/90<\infty$ | không, vi phạm điều kiện thứ nhất |

**Câu (b).** Chỉ $\alpha_n=1/(n+1)$. Hai dãy $1/\sqrt{n+1}$ và $0{,}01$ không thỏa giả thiết về bước học, nên Định lý 07.17 không cho kết luận. Với bước hằng, $w_n$ dao động quanh $w_{\mathrm{MC}}$ với biên độ không giảm. Với $1/\sqrt{n+1}$, định lý không khẳng định gì, kể cả phân kỳ: trong mô hình nhiễu độc lập có phương sai $\sigma^2$, phương sai của sai lệch xấp xỉ $\alpha_n\sigma^2/2\to0$. Dãy $1/(n+1)^2$ cho tổng quãng đường hữu hạn.

**Câu (c).** Với $\alpha_k=1/(k+2)$: $1-\alpha_k=(k+1)/(k+2)$, tích lồng nhau cho

$$
\begin{aligned}
e_n&=10\prod_{k=0}^{n-1}\frac{k+1}{k+2}=\frac{10}{n+1},\\
w_n&=10-\frac{10}{n+1}=\frac{10n}{n+1}.
\end{aligned}
$$

Vậy $w_1=5$, $w_2=20/3\approx6{,}667$ và $w_n\to10=w_{\mathrm{MC}}$. Với $\alpha_k=1/(k+2)^2$: đặt $j=k+2$, $1-1/j^2=\frac{(j-1)(j+1)}{j^2}$, nên

$$
\begin{aligned}
\prod_{j=2}^{n+1}\Big(1-\frac1{j^2}\Big)&=\prod_{j=2}^{n+1}\frac{j-1}{j}\cdot\prod_{j=2}^{n+1}\frac{j+1}{j}=\frac1{n+1}\cdot\frac{n+2}{2},\\
w_n&=10-\frac{5(n+2)}{n+1}.
\end{aligned}
$$

Vậy $w_1=2{,}5$, $w_2=10/3\approx3{,}333$ và $w_n\to5$, bằng một nửa $w_{\mathrm{MC}}=10$. Tổng các bước là $\sum_{j\ge2}1/j^2=\pi^2/6-1\approx0{,}645$, hữu hạn, nên phần sai lệch còn lại không bao giờ được bù.

**Diễn giải.** Ví dụ không có nhiễu, nên điều kiện thứ hai không thể hiện: bước hằng $0{,}01$ ở đây cho $e_n=10\cdot0{,}99^n\to0$. Khi lợi tức có nhiễu, bước hằng giữ $w_n$ dao động quanh $w_{\mathrm{MC}}$ (Mục 2.3 của ghi chú).

**Kiểm tra lại.** Tính trực tiếp: $w_1=0+\tfrac14\cdot10=2{,}5$, $w_2=2{,}5+\tfrac19\cdot7{,}5\approx3{,}333$. Bốn lỗi thường gặp: cho rằng $1/\sqrt{n+1}$ thỏa điều kiện thứ hai vì số hạng tiến về $0$; nói bước hằng vi phạm điều kiện thứ nhất; coi $\sum_n\alpha_n^2<\infty$ là đủ để học tới đích; coi Robbins–Monro là điều kiện cần, trong khi nó chỉ là giả thiết đủ của Định lý 07.17.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 07.3. Sai số xấp xỉ của hai trạng thái cùng đặc trưng

**Mức độ:** tính toán. Mục tiêu học tập 1 của ghi chú: nhận diện nhập nhằng đặc trưng, phân biệt sai số xấp xỉ với sai số ước lượng.

**Nguồn:** ghi chú bài giảng Bài 07, Mục 1.4, Bài tập 07.3; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: sai số xấp xỉ của hai trạng thái cùng đặc trưng](lecture-07-xap-xi-ham.html#/2/12); đề bài và lời giải ở cùng trang.

::: exercise Bài tập 07.3 (Sai số xấp xỉ của hai trạng thái cùng đặc trưng)
Hai trạng thái $s_1$, $s_2$ có cùng vector đặc trưng, nên $\hat v(s_1,w)=\hat v(s_2,w)=:c$ với mọi $w$. Giá trị thật là $v_\pi(s_1)=0$, $v_\pi(s_2)=2$; không có trạng thái khác; trọng số $\mu=(\beta;1-\beta)$ với $\beta\in(0,1)$. Sai số giá trị là $J_\mu=\tfrac12\big[\mu(s_1)(v_\pi(s_1)-c)^2+\mu(s_2)(v_\pi(s_2)-c)^2\big]$, và sai số xấp xỉ là $\inf_wJ_\mu(w)$.

- (a) Tìm $c^*(\beta)$ cực tiểu hóa $J_\mu$ và sai số xấp xỉ theo $\beta$.
- (b) Tính hai đại lượng khi $\beta=\tfrac12$.
- (c) Xác định thêm dữ liệu có làm sai số xấp xỉ giảm hay không.
:::

::: hint Gợi ý Bài tập 07.3
Đạo hàm của $J_\mu$ theo $c$; với (c), dùng cận dưới (1.5) của Mệnh đề 07.10 với $\mu_1=\beta$, $\mu_2=1-\beta$.
:::

::: solution Lời giải Bài tập 07.3
**Câu (a).** Thay dữ kiện:

$$
\begin{aligned}
J_\mu(c)&=\tfrac12\big[\beta c^2+(1-\beta)(2-c)^2\big],\\
J_\mu'(c)&=\beta c-(1-\beta)(2-c)=c-2(1-\beta).
\end{aligned}
$$

$J_\mu''(c)=1>0$, nên cực tiểu duy nhất là $c^*=2(1-\beta)$, trung bình có trọng số của hai giá trị thật. Tại đó $2-c^*=2\beta$, nên

$$
\begin{aligned}
\inf_wJ_\mu&=\tfrac12\big[4\beta(1-\beta)^2+4\beta^2(1-\beta)\big]\\
&=2\beta(1-\beta)\big[(1-\beta)+\beta\big]=2\beta(1-\beta).
\end{aligned}
$$

Giá trị này trùng vế phải của (1.5): $\tfrac12\cdot\tfrac{\beta(1-\beta)}{1}\cdot(0-2)^2=2\beta(1-\beta)$.

**Câu (b).** Với $\beta=\tfrac12$: $c^*=1$ và sai số xấp xỉ bằng $2\cdot\tfrac12\cdot\tfrac12=\tfrac12$.

**Câu (c).** Không. Theo Mệnh đề 07.10, $J_\mu(w)\ge2\beta(1-\beta)$ với mọi $w$, và cận này không chứa dữ liệu. Thêm dữ liệu chỉ làm giảm sai số ước lượng $J_\mu(\hat w)-\inf_wJ_\mu$ của tham số $\hat w$ học từ dữ liệu (Định nghĩa 07.11). Muốn giảm sai số xấp xỉ phải đổi đặc trưng để $x(s_1)\ne x(s_2)$.

**Kiểm tra lại.** Với $\beta=\tfrac34$: $c^*=\tfrac12$ và $J_\mu=\tfrac12\big[\tfrac34\cdot\tfrac14+\tfrac14\cdot\tfrac94\big]=\tfrac38=2\cdot\tfrac34\cdot\tfrac14$. Ba lỗi thường gặp: bỏ hệ số $\tfrac12$, cho $4\beta(1-\beta)$, tức $1$ khi $\beta=\tfrac12$; lấy $c^*=1$ là trung bình không trọng số với mọi $\beta$; cho rằng chạy lâu hơn hoặc thêm dữ liệu làm giảm một sai số do đặc trưng quyết định.
:::

### Bài tập 07.5. Đạo hàm cập nhật Monte Carlo

**Mức độ:** tính toán và chứng minh. Mục tiêu học tập 3 của ghi chú: gradient đầy đủ.

**Nguồn:** Bài tập tuần 7 (2025–2026), bài 4 (phiếu viết $\phi(s)$ cho $x(s)$); ghi chú bài giảng Bài 07, Mục 2.3, Bài tập 07.5.

**Trùng trang chiếu:** [Bài tập: đạo hàm cập nhật Monte Carlo](lecture-07-xap-xi-ham.html#/3/9) và [trang lời giải](lecture-07-xap-xi-ham.html#/3/10).

::: exercise Bài tập 07.5 (Đạo hàm cập nhật Monte Carlo)
Cho $\hat v(s,w)=x(s)^\top w$ và mất mát Monte Carlo của một mẫu $\ell_t(w)=\tfrac12\big(G_t-x(S_t)^\top w\big)^2$, với $G_t$ là lợi tức sau $S_t$.

- (a) Tính $\nabla_w\ell_t(w)$.
- (b) Suy ra một bước hạ gradient với bước học $\alpha_n$ và chứng minh nó trùng cập nhật Monte Carlo $w_{n+1}=w_n+\alpha_n\big(G_t-x(S_t)^\top w_n\big)x(S_t)$. Kiểm với $x(S_t)=(2;1)$, $w_n=(1;-1)$, $G_t=5$, $\alpha_n=0{,}1$.
- (c) Tính Hessian của $\ell_t$, chứng minh $\ell_t$ lồi và nêu điều kiện để cập nhật hội tụ về cực tiểu toàn cục của sai số giá trị $J_\mu$.
:::

::: hint Gợi ý Bài tập 07.5
Quy tắc chuỗi, với $G_t$ không phụ thuộc $w$. Với (c), xét $z^\top x(S_t)x(S_t)^\top z$ và giả thiết của Định lý 07.17.
:::

::: solution Lời giải Bài tập 07.5
**Câu (a).** $G_t$ tính từ phần thưởng trên quỹ đạo, không chứa $w$; $\nabla_w\big(x(S_t)^\top w\big)=x(S_t)$. Theo quy tắc chuỗi,

$$
\nabla_w\ell_t(w)=\big(G_t-x(S_t)^\top w\big)\cdot\big(-x(S_t)\big)=-\big(G_t-x(S_t)^\top w\big)x(S_t).
$$

Đây là gradient đầy đủ, vì không có số hạng nào của $\ell_t$ bị giữ cố định khi lấy đạo hàm.

**Câu (b).** Một bước hạ gradient là $w_{n+1}=w_n-\alpha_n\nabla_w\ell_t(w_n)$. Thay câu (a):

$$
w_{n+1}=w_n+\alpha_n\big(G_t-x(S_t)^\top w_n\big)x(S_t),
$$

đúng cập nhật Monte Carlo. Với dữ kiện đã cho: dự đoán $x(S_t)^\top w_n=2-1=1$; sai lệch $5-1=4$; $w_{n+1}=(1;-1)+0{,}1\cdot4\cdot(2;1)=(1{,}8;-0{,}6)$.

**Câu (c).** Lấy đạo hàm câu (a) theo $w$: $\nabla_w^2\ell_t=x(S_t)x(S_t)^\top$. Với mọi $z\in\mathbb R^d$, $z^\top x(S_t)x(S_t)^\top z=\big(x(S_t)^\top z\big)^2\ge0$, nên Hessian nửa xác định dương và $\ell_t$ lồi. Hessian có hạng $1$, nên một mất mát mẫu riêng lẻ không có cực tiểu duy nhất khi $d\ge2$. Theo Định lý 07.17, cập nhật hội tụ hầu chắc chắn (almost surely) tới cực tiểu duy nhất $w_{\mathrm{MC}}$ của $J_\mu$ khi:

- $\pi$ và $\mu$ cố định;
- các mẫu độc lập, với $S_t\sim\mu$ và $G_t$ là lợi tức sau $S_t$ theo $\pi$;
- đặc trưng bị chặn và $\mathbb E[G_t^2]<\infty$;
- $\Sigma_\mu=\sum_s\mu(s)x(s)x(s)^\top$ xác định dương;
- bước học thỏa Robbins–Monro.

Bài giảng gốc (2025–2026, trang 34) nêu ba điều kiện: mẫu độc lập cùng phân phối, đặc trưng bị chặn, Robbins–Monro; hai điều kiện còn lại cần cho tính duy nhất của đích và cho kỳ vọng của lợi tức.

**Kiểm tra lại.** Dự đoán mới tại $S_t$ là $3{,}6-0{,}6=3$; theo Mệnh đề 07.2 nó tăng $\alpha e\lVert x(S_t)\rVert^2=0{,}1\cdot4\cdot5=2$, đúng $1+2$. Ba lỗi thường gặp: sai dấu, viết $w_{n+1}=w_n-\alpha_n(G_t-x^\top w_n)x$, làm dự đoán đi xa mục tiêu; coi $G_t$ phụ thuộc $w$; kết luận $\ell_t$ lồi chặt từ Hessian nửa xác định dương.
:::

### Bài tập 07.7. Số hạng bị bỏ trong một cập nhật TD(0)

**Mức độ:** tính toán. Mục tiêu học tập 2 và 3 của ghi chú: một cập nhật TD(0) bằng tay, số hạng bị bỏ của bán gradient.

**Nguồn:** ghi chú bài giảng Bài 07, Mục 3.1, Bài tập 07.7; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: số hạng bị bỏ trong một cập nhật TD(0)](lecture-07-xap-xi-ham.html#/4/7); đề bài và lời giải ở cùng trang.

::: exercise Bài tập 07.7 (Số hạng bị bỏ trong một cập nhật TD(0))
Một chuyển có $x(S_t)=(1;2)$, $x(S_{t+1})=(2;0)$, $R_{t+1}=1$; tham số hiện tại $w_n=(0{,}5;1)$; $\gamma=0{,}9$. Sai số TD là $\delta_t=R_{t+1}+\gamma\,x(S_{t+1})^\top w_n-x(S_t)^\top w_n$.

- (a) Tính $\delta_t$.
- (b) Tính phần cập nhật bán gradient giữ lại $\delta_tx(S_t)$, số hạng bị bỏ $\gamma\delta_tx(S_{t+1})$ và hướng giảm đầy đủ $\delta_t\big(x(S_t)-\gamma x(S_{t+1})\big)$ của $\tfrac12\delta_t(w)^2$.
- (c) So dấu từng thành phần của hai hướng.
:::

::: hint Gợi ý Bài tập 07.7
Hai dự đoán trong $\delta_t$ dùng $w_n$. Gradient đầy đủ của $\tfrac12\delta_t(w)^2$ là $\delta_t(w)\big(\gamma x(S_{t+1})-x(S_t)\big)$, vì $w$ có mặt ở cả mục tiêu lẫn dự đoán.
:::

::: solution Lời giải Bài tập 07.7
**Câu (a).** Hai dự đoán: $x(S_t)^\top w_n=0{,}5+2=2{,}5$ và $x(S_{t+1})^\top w_n=1$. Mục tiêu $1+0{,}9\cdot1=1{,}9$; $\delta_t=1{,}9-2{,}5=-0{,}6$.

**Câu (b).**

$$
\begin{aligned}
\text{giữ lại: }&\delta_tx(S_t)=-0{,}6\cdot(1;2)=(-0{,}6;-1{,}2),\\
\text{bị bỏ: }&\gamma\delta_tx(S_{t+1})=0{,}9\cdot(-0{,}6)\cdot(2;0)=(-1{,}08;0),\\
\text{hướng đầy đủ: }&(-0{,}6;-1{,}2)-(-1{,}08;0)=(0{,}48;-1{,}2).
\end{aligned}
$$

**Câu (c).** Thành phần thứ hai trùng nhau vì $[x(S_{t+1})]_2=0$. Thành phần thứ nhất ngược dấu: bán gradient giảm $[w]_1$, còn hướng đầy đủ tăng $[w]_1$. Tăng $[w]_1$ một đơn vị làm mục tiêu tăng $0{,}9\cdot2=1{,}8$, còn dự đoán tại $S_t$ chỉ tăng $1$, nên $\delta_t$ tăng $0{,}8$ và $\lvert\delta_t\rvert$ giảm; cập nhật bán gradient bỏ qua đường đi qua mục tiêu này.

**Kiểm tra lại.** Giữ lại trừ hướng đầy đủ: $(-0{,}6;-1{,}2)-(0{,}48;-1{,}2)=(-1{,}08;0)$, đúng số hạng bị bỏ. Với $\alpha=0{,}1$, cập nhật TD(0) cho $w_{n+1}=(0{,}44;0{,}88)$. Hai lỗi thường gặp: cập nhật theo $x(S_{t+1})$ thay vì $x(S_t)$; tính dự đoán tại $S_{t+1}$ bằng tham số sau cập nhật, cho mục tiêu $1{,}792$ thay cho $1{,}9$.
:::

### Bài tập 07.8. Nghiệm TD và nghiệm Monte Carlo trên hai trạng thái

**Mức độ:** tính toán. Mục tiêu học tập 4 của ghi chú: tính nghiệm TD(0) và Monte Carlo trên ví dụ nhỏ.

**Nguồn:** câu (a) dựa trên Bài tập tuần 7 (2025–2026), bài 5; ghi chú bài giảng Bài 07, Mục 3.2, Bài tập 07.8; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** câu (b) trùng [Bài tập: nghiệm TD và nghiệm Monte Carlo trên hai trạng thái](lecture-07-xap-xi-ham.html#/4/14); đề bài và lời giải ở cùng trang.

::: exercise Bài tập 07.8 (Nghiệm TD và nghiệm Monte Carlo trên hai trạng thái)
Hai trạng thái có $x(s_1)=1$, $x(s_2)=2$, nên $\Phi=(1;2)$. Từ mỗi trạng thái, chuyển tới $s_1$ hoặc $s_2$ với xác suất $\tfrac12$; rời $s_1$ nhận $0$, rời $s_2$ nhận $1$, nên $r_\pi=(0;1)$; $\gamma=0{,}9$; bài toán không kết thúc, phân phối dừng $d_\pi=(\tfrac12;\tfrac12)$, $D=\operatorname{diag}(d_\pi)$. Nhắc lại: $A=\Phi^\top D(I-\gamma P_\pi)\Phi$, $b=\Phi^\top Dr_\pi$, $w_{\mathrm{TD}}$ là nghiệm của $Aw=b$, và $\Pi_D=\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top D$.

- (a) Chỉ ra bước nào trong chứng minh "$b-Aw=0$ khi và chỉ khi $\Phi w=\Pi_DT_\pi(\Phi w)$" (Mệnh đề 07.26) cần $\Phi^\top D\Phi$ khả nghịch, và kiểm điều kiện đó trên dữ kiện này. Chứng minh gồm ba dòng biến đổi: với $v=T_\pi(\Phi w)$, từ $b-Aw=\Phi^\top D(v-\Phi w)=0$ suy ra $\Phi^\top Dv=\Phi^\top D\Phi\,w$, rồi $\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top Dv=\Phi w$, tức $\Pi_Dv=\Phi w$ (Bài tập 07.22(b) viết đủ).
- (b) Tính $v_\pi$, $w_{\mathrm{MC}}$ cực tiểu hóa sai số giá trị với trọng số $\mu=d_\pi$, và $w_{\mathrm{TD}}$.
:::

::: hint Gợi ý Bài tập 07.8
Với (a), xem dòng thứ hai của chứng minh, bước nhân trái để đưa $\Phi^\top D(v-\Phi w)=0$ về $\Phi w=\Pi_Dv$. Với (b), đặt $\bar v=\tfrac12(v_1+v_2)$; $w_{\mathrm{MC}}=\sum_s\mu(s)x(s)v_\pi(s)\big/\sum_s\mu(s)x(s)^2$.
:::

::: solution Lời giải Bài tập 07.8
**Câu (a).** Đặt $v=T_\pi(\Phi w)$, nên $b-Aw=\Phi^\top D(v-\Phi w)$. Chiều thuận nhân trái đẳng thức $\Phi^\top D(v-\Phi w)=0$ với $\Phi(\Phi^\top D\Phi)^{-1}$ để được $\Pi_Dv-\Phi w=0$; bước này cần $\Phi^\top D\Phi$ khả nghịch, và bản thân $\Pi_D$ cũng được định nghĩa qua nghịch đảo đó. Chiều ngược chỉ dùng $\Phi^\top D(v-\Pi_Dv)=0$. Ở đây $\Phi^\top D\Phi=\tfrac12\cdot1^2+\tfrac12\cdot2^2=2{,}5\ne0$.

**Câu (b).** Phương trình Bellman cho $v_1=0+0{,}9\bar v$ và $v_2=1+0{,}9\bar v$. Cộng hai phương trình rồi chia $2$: $\bar v=\tfrac12+0{,}9\bar v$, nên $\bar v=5$ và $v_\pi=(4{,}5;5{,}5)$.

$$
\begin{aligned}
w_{\mathrm{MC}}&=\frac{\tfrac12\cdot1\cdot4{,}5+\tfrac12\cdot2\cdot5{,}5}{2{,}5}=\frac{7{,}75}{2{,}5}=3{,}1,\\
(I-\gamma P_\pi)\Phi&=(1-0{,}9\cdot1{,}5;\ 2-0{,}9\cdot1{,}5)=(-0{,}35;0{,}65),\\
A&=\tfrac12\cdot1\cdot(-0{,}35)+\tfrac12\cdot2\cdot0{,}65=0{,}475,\\
b&=\tfrac12\cdot1\cdot0+\tfrac12\cdot2\cdot1=1,\\
w_{\mathrm{TD}}&=1/0{,}475=40/19\approx2{,}105.
\end{aligned}
$$

Hai đích khác nhau: $w_{\mathrm{TD}}\approx2{,}105\ne3{,}1=w_{\mathrm{MC}}$.

**Kiểm tra lại.** $T_\pi(\Phi w_{\mathrm{TD}})=r_\pi+0{,}9\cdot1{,}5\cdot\tfrac{40}{19}(1;1)=(\tfrac{54}{19};\tfrac{73}{19})$; hệ số hình chiếu lên $\Phi$ là $\big(\tfrac12\cdot\tfrac{54}{19}+\tfrac12\cdot2\cdot\tfrac{73}{19}\big)/2{,}5=\tfrac{100}{19}/2{,}5=\tfrac{40}{19}$, đúng $w_{\mathrm{TD}}$. Hai lỗi thường gặp: dùng nhầm $r_\pi=(1;0)$ của Ví dụ 07.11 trong ghi chú, cho $w_{\mathrm{TD}}=20/19$, nghiệm của mô hình đó; thay $\gamma P_\pi\Phi$ bằng $\gamma\Phi$, bỏ phép lấy trung bình theo chuyển, cho $A=\tfrac12\cdot0{,}1+\tfrac12\cdot2\cdot0{,}2=0{,}25$ và $w_{\mathrm{TD}}=4$.
:::

### Bài tập 07.10. Monte Carlo trên một lượt của chuỗi

**Mức độ:** tính toán. Mục tiêu học tập 2 của ghi chú: cập nhật Monte Carlo gradient bằng tay, theo thứ tự thời gian.

**Nguồn:** Bài tập tuần 7 (2025–2026), bài 7; ghi chú bài giảng Bài 07, Mục 4.3, Bài tập 07.10. Phiếu gọi phép cập nhật là "Monte Carlo control with semi-gradient"; theo quy ước của bài, cập nhật Monte Carlo là gradient đầy đủ, và bài chỉ có bước đánh giá.

**Trùng trang chiếu:** [Bài tập: Monte Carlo trên một lượt của chuỗi](lecture-07-xap-xi-ham.html#/5/7) và [trang lời giải](lecture-07-xap-xi-ham.html#/5/8).

::: exercise Bài tập 07.10 (Monte Carlo trên một lượt của chuỗi)
Chuỗi năm trạng thái $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ với $\mathrm A$, $\mathrm E$ kết thúc; hành động $0$ đi trái, $1$ đi phải. Giá trị hành động $\hat q(s,a,w)=x(s,a)^\top w$ với $x(s,a)=(d_{\text{trái}}(s);u(a);1)$, $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$, $u(0)=1$, $u(1)=-1$; $\gamma=1$; $w_0=(1;1;-1)$, $\alpha=0{,}1$. Một lượt gồm ba chuyển $(\mathrm D,0,-1,\mathrm C)$, $(\mathrm C,0,-1,\mathrm B)$, $(\mathrm B,0,1\,000,\mathrm A)$, mỗi chuyển ghi $(S_t,A_t,R_{t+1},S_{t+1})$.

- (a) Tính $G_0$, $G_1$, $G_2$.
- (b) Viết $x(\mathrm D,0)$, $x(\mathrm C,0)$, $x(\mathrm B,0)$.
- (c) Cập nhật theo thứ tự thời gian bằng $w_{n+1}=w_n+\alpha\big(G_t-x(S_t,A_t)^\top w_n\big)x(S_t,A_t)$, với $n=t$.
- (d) Tính $\hat q(\mathrm D,0,w_3)$, $\hat q(\mathrm C,0,w_3)$, $\hat q(\mathrm B,0,w_3)$.
:::

::: hint Gợi ý Bài tập 07.10
Với $\gamma=1$, $G_t$ là tổng phần thưởng từ $t$ tới hết lượt; tính lùi $G_2$, $G_1$, $G_0$. Mỗi cập nhật dùng $w$ vừa có từ cập nhật trước.
:::

::: solution Lời giải Bài tập 07.10
**Câu (a).** Tính lùi từ $G_3=0$: $G_2=1\,000$, $G_1=-1+1\,000=999$, $G_0=-1+999=998$.

**Câu (b).** $x(\mathrm D,0)=(3;1;1)$, $x(\mathrm C,0)=(2;1;1)$, $x(\mathrm B,0)=(1;1;1)$.

**Câu (c).** Mỗi hàng dùng $w_n$ của hàng trước; cột "$\hat q$ trước" là $x(S_t,A_t)^\top w_n$, sai lệch là $G_t$ trừ cột đó.

| $(S_t,A_t)$ | $G_t$ | $x(S_t,A_t)$ | $\hat q$ trước | sai lệch | $w_{n+1}$ |
| --- | --- | --- | --- | --- | --- |
| $(\mathrm D,0)$ | $998$ | $(3;1;1)$ | $3$ | $995$ | $(299{,}5;100{,}5;98{,}5)$ |
| $(\mathrm C,0)$ | $999$ | $(2;1;1)$ | $798$ | $201$ | $(339{,}7;120{,}6;118{,}6)$ |
| $(\mathrm B,0)$ | $1\,000$ | $(1;1;1)$ | $578{,}9$ | $421{,}1$ | $(381{,}81;162{,}71;160{,}71)$ |

Chi tiết hàng đầu: $\hat q(\mathrm D,0,w_0)=3+1-1=3$; bước $0{,}1\cdot995=99{,}5$; $w_1=(1;1;-1)+99{,}5\cdot(3;1;1)=(299{,}5;100{,}5;98{,}5)$. Hàng hai: $\hat q(\mathrm C,0,w_1)=599+100{,}5+98{,}5=798$; bước $20{,}1$. Hàng ba: $\hat q(\mathrm B,0,w_2)=339{,}7+120{,}6+118{,}6=578{,}9$; bước $42{,}11$.

**Câu (d).**

$$
\begin{aligned}
\hat q(\mathrm D,0,w_3)&=3\cdot381{,}81+162{,}71+160{,}71=1\,468{,}85,\\
\hat q(\mathrm C,0,w_3)&=2\cdot381{,}81+162{,}71+160{,}71=1\,087{,}04,\\
\hat q(\mathrm B,0,w_3)&=381{,}81+162{,}71+160{,}71=705{,}23.
\end{aligned}
$$

**Diễn giải.** $\hat q(\mathrm D,0)$ vượt $G_0=998$ vì hai lý do. Thứ nhất, $\alpha\lVert x(\mathrm D,0)\rVert^2=0{,}1\cdot11=1{,}1>1$, nên ngay lần 1 dự đoán thành $3+1{,}1\cdot995=1\,097{,}5$, vượt qua mục tiêu. Thứ hai, hai cập nhật sau kéo nó lên thêm qua tham số dùng chung. Bài chỉ có bước đánh giá, chưa có bước cải thiện chính sách.

**Kiểm tra lại.** Ba lỗi thường gặp: dùng $w_0$ cho cả ba cập nhật, cho $w=(598{,}8;300{,}1;298{,}1)$; lấy $G_t$ bằng phần thưởng một bước; quên thành phần hằng $1$ của $x(s,a)$.
:::

### Bài tập 07.11. Ba cập nhật Sarsa trên chuỗi

**Mức độ:** tính toán. Mục tiêu học tập 2 của ghi chú: cập nhật Sarsa bán gradient bằng tay.

**Nguồn:** Bài tập tuần 7 (2025–2026), bài 8; ghi chú bài giảng Bài 07, Mục 4.3, Bài tập 07.11.

**Trùng trang chiếu:** [Bài tập: ba cập nhật Sarsa trên chuỗi](lecture-07-xap-xi-ham.html#/5/9) và [trang lời giải](lecture-07-xap-xi-ham.html#/5/10).

::: exercise Bài tập 07.11 (Ba cập nhật Sarsa trên chuỗi)
Chuỗi năm trạng thái và đặc trưng như Bài tập 07.10: $\mathrm A$, $\mathrm E$ kết thúc; $x(s,a)=(d_{\text{trái}}(s);u(a);1)$, $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$, $u(0)=1$, $u(1)=-1$; $w_0=(1;1;-1)$, $\alpha=0{,}2$, $\varepsilon=0{,}25$, $\gamma=1$. Ba mẫu $(S,A,R,S',A')$: $(\mathrm D,0,-1,\mathrm C,0)$, $(\mathrm C,1,-1,\mathrm D,1)$, $(\mathrm D,1,10,\mathrm E,\text{kết thúc})$. Phiếu bài tập gọi ba mẫu là liên tiếp; nhưng mẫu 1 có hành động kế tiếp $0$ tại $\mathrm C$, còn mẫu 2 thực hiện hành động $1$ tại $\mathrm C$, nên ở đây coi ba mẫu là độc lập. Cập nhật Sarsa là $w_{n+1}=w_n+\alpha\delta\,x(S,A)$ với $\delta=R+\gamma\,\hat q(S',A',w_n)-\hat q(S,A,w_n)$ và $\hat q(\mathrm E,\cdot,w)=0$.

- (a) Tính $\delta$ và tham số mới sau mỗi mẫu.
- (b) Tính $\hat q(\mathrm D,0,w_3)$, $\hat q(\mathrm C,1,w_3)$, $\hat q(\mathrm D,1,w_3)$ và kiểm tra $\hat q(\mathrm D,1,w_3)-\hat q(\mathrm D,0,w_3)=-2[w_3]_2$.
:::

::: hint Gợi ý Bài tập 07.11
Hai giá trị trong một $\delta$ dùng tham số trước cập nhật. $\varepsilon$ không vào phép tính vì hành động kế tiếp đã cho trong mẫu. $x(\mathrm C,1)=(2;-1;1)$, $x(\mathrm D,1)=(3;-1;1)$.
:::

::: solution Lời giải Bài tập 07.11
**Câu (a).** Bảng dùng cùng cột với trang lời giải của trang chiếu.

| $(S,A)$ | $\hat q(S,A)$ | $\hat q(S',A')$ | $\delta$ | $w_{n+1}$ |
| --- | --- | --- | --- | --- |
| $(\mathrm D,0)$ | $3$ | $2$ | $-2$ | $(-0{,}2;0{,}6;-1{,}4)$ |
| $(\mathrm C,1)$ | $-2{,}4$ | $-2{,}6$ | $-1{,}2$ | $(-0{,}68;0{,}84;-1{,}64)$ |
| $(\mathrm D,1)$ | $-4{,}52$ | $0$ | $14{,}52$ | $(8{,}032;-2{,}064;1{,}264)$ |

- Mẫu 1: $\hat q(\mathrm D,0,w_0)=3$, $\hat q(\mathrm C,0,w_0)=2$; $\delta=-1+2-3=-2$; $w_1=(1;1;-1)-0{,}4\cdot(3;1;1)=(-0{,}2;0{,}6;-1{,}4)$.
- Mẫu 2: $\hat q(\mathrm C,1,w_1)=-0{,}4-0{,}6-1{,}4=-2{,}4$; $\hat q(\mathrm D,1,w_1)=-0{,}6-0{,}6-1{,}4=-2{,}6$; $\delta=-1-2{,}6+2{,}4=-1{,}2$; $w_2=w_1-0{,}24\cdot(2;-1;1)=(-0{,}68;0{,}84;-1{,}64)$.
- Mẫu 3: $\mathrm E$ kết thúc nên mục tiêu là $10$; $\hat q(\mathrm D,1,w_2)=-2{,}04-0{,}84-1{,}64=-4{,}52$; $\delta=14{,}52$; $w_3=w_2+2{,}904\cdot(3;-1;1)=(8{,}032;-2{,}064;1{,}264)$.

**Câu (b).** $\hat q(\mathrm D,0,w_3)=24{,}096-2{,}064+1{,}264=23{,}296$; $\hat q(\mathrm C,1,w_3)=16{,}064+2{,}064+1{,}264=19{,}392$; $\hat q(\mathrm D,1,w_3)=24{,}096+2{,}064+1{,}264=27{,}424$. Hiệu $27{,}424-23{,}296=4{,}128=-2\cdot(-2{,}064)$. Hiệu dương nên chính sách tham lam theo $w_3$ chọn đi phải ở $\mathrm B$, $\mathrm C$, $\mathrm D$, dù từ $\mathrm D$ đi trái cho lợi tức $998$ và đi phải chỉ cho $10$.

**Diễn giải.** Mẫu 1 là chuyển $(\mathrm D,0,-1,\mathrm C)$ đầu lượt của Bài tập 07.10, cùng $w_0$. Ở đó mục tiêu Monte Carlo $998$, với $\alpha=0{,}1$, đẩy $\hat q(\mathrm D,0)$ từ $3$ lên $1\,097{,}5$; ở đây mục tiêu Sarsa $1$, với $\alpha=0{,}2$, kéo nó xuống $3+2{,}2\cdot(-2)=-1{,}4$. Mục tiêu bootstrap chỉ chứa phần thưởng $-1$ và dự đoán hiện tại tại $(\mathrm C,0)$, nên chưa mang thông tin về phần thưởng $1\,000$ khi vào $\mathrm A$.

**Kiểm tra lại.** Với $w_1$: $\hat q(\mathrm D,0,w_1)=-0{,}6+0{,}6-1{,}4=-1{,}4$, đúng $3-4{,}4$ theo Mệnh đề 07.2 ($\alpha\delta\lVert x(\mathrm D,0)\rVert^2=0{,}2\cdot(-2)\cdot11$). Ba lỗi thường gặp: dùng hành động tham lam tại $S'$ thay cho $A'$ đã cho, tức là làm Q-learning (mẫu 2 khi đó cho $\delta=0$, xem Bài tập 07.13); tính $\hat q(S',A')$ bằng tham số sau cập nhật; dùng $x(\mathrm E,\cdot)$ thay cho giá trị $0$ tại trạng thái kết thúc.
:::

### Bài tập 07.13. Ba cập nhật Q-learning trên chuỗi

**Mức độ:** tính toán. Mục tiêu học tập 2 và 5 của ghi chú: cập nhật Q-learning bán gradient bằng tay, phân biệt mục tiêu Q-learning với mục tiêu Sarsa.

**Nguồn:** ghi chú bài giảng Bài 07, Mục 5.1, Bài tập 07.13; dữ kiện của Bài tập tuần 7 (2025–2026), bài 8, với mục tiêu Q-learning.

**Trùng trang chiếu:** [Bài tập: ba cập nhật Q-learning trên chuỗi](lecture-07-xap-xi-ham.html#/6/5) và [trang lời giải](lecture-07-xap-xi-ham.html#/6/6).

::: exercise Bài tập 07.13 (Ba cập nhật Q-learning trên chuỗi)
Chuỗi năm trạng thái với $\mathrm A$, $\mathrm E$ kết thúc; $x(s,a)=(d_{\text{trái}}(s);u(a);1)$, $d_{\text{trái}}(\mathrm B,\mathrm C,\mathrm D)=(1,2,3)$, $u(0)=1$, $u(1)=-1$; $\gamma=1$; $w_0=(1;1;-1)$, $\alpha=0{,}2$. Ba mẫu độc lập $(S,A,R,S')$: $(\mathrm D,0,-1,\mathrm C)$, $(\mathrm C,1,-1,\mathrm D)$, $(\mathrm D,1,10,\mathrm E)$ với $\mathrm E$ kết thúc. Mục tiêu Q-learning là $y=R$ khi $S'$ kết thúc và $y=R+\gamma\max_{a'}\hat q(S',a',w_n)$ khi không; cập nhật $w_{n+1}=w_n+\alpha\big(y-\hat q(S,A,w_n)\big)x(S,A)$.

- (a) Thực hiện ba cập nhật; ghi mục tiêu, sai số TD và tham số mới.
- (b) Tính $\hat q(\mathrm D,0,w_3)$, $\hat q(\mathrm D,1,w_3)$ và so với kết quả Sarsa $w_3=(8{,}032;-2{,}064;1{,}264)$ trên cùng ba mẫu (Bài tập 07.11).
:::

::: hint Gợi ý Bài tập 07.13
Ở mẫu 2, so hai giá trị $\hat q(\mathrm D,0,w_1)$ và $\hat q(\mathrm D,1,w_1)$ trước khi lấy cực đại. Mẫu cuối vào trạng thái kết thúc nên mục tiêu là $R$.
:::

::: solution Lời giải Bài tập 07.13
**Câu (a).**

| $(S,A)$ | $\hat q(S,A)$ | $\max_{a'}\hat q(S',a')$ | $\delta$ | $w_{n+1}$ |
| --- | --- | --- | --- | --- |
| $(\mathrm D,0)$ | $3$ | $2$ | $-2$ | $(-0{,}2;0{,}6;-1{,}4)$ |
| $(\mathrm C,1)$ | $-2{,}4$ | $-1{,}4$ | $0$ | $(-0{,}2;0{,}6;-1{,}4)$ |
| $(\mathrm D,1)$ | $-2{,}6$ | $0$ | $12{,}6$ | $(7{,}36;-1{,}92;1{,}12)$ |

- Mẫu 1: $\hat q(\mathrm C,\cdot,w_0)=(2;0)$, cực đại $2$; mục tiêu $-1+2=1$, trùng mục tiêu Sarsa vì hành động kế tiếp của mẫu Sarsa là hành động tham lam; $\delta=-2$, $w_1=(-0{,}2;0{,}6;-1{,}4)$.
- Mẫu 2: $\hat q(\mathrm D,0,w_1)=-0{,}6+0{,}6-1{,}4=-1{,}4$ và $\hat q(\mathrm D,1,w_1)=-2{,}6$; mục tiêu $-1+\max(-1{,}4;-2{,}6)=-2{,}4$; $\delta=-2{,}4-(-2{,}4)=0$, nên $w_2=w_1$.
- Mẫu 3: mục tiêu $10$; $\delta=10-(-2{,}6)=12{,}6$; $w_3=w_2+0{,}2\cdot12{,}6\cdot(3;-1;1)=(-0{,}2;0{,}6;-1{,}4)+2{,}52\cdot(3;-1;1)=(7{,}36;-1{,}92;1{,}12)$.

**Câu (b).** $\hat q(\mathrm D,0,w_3)=22{,}08-1{,}92+1{,}12=21{,}28$; $\hat q(\mathrm D,1,w_3)=22{,}08+1{,}92+1{,}12=25{,}12$. Sarsa cho $w_3=(8{,}032;-2{,}064;1{,}264)$. Hai thuật toán tách nhau từ mẫu 2: hành động kế tiếp của mẫu Sarsa, đi phải tại $\mathrm D$, là hành động thăm dò; Sarsa đưa giá trị $-2{,}6$ của nó vào mục tiêu, còn Q-learning dùng giá trị $-1{,}4$ của hành động tham lam và không đổi $w$. Cả hai $w_3$ cho hiệu $\hat q(\mathrm D,1)-\hat q(\mathrm D,0)>0$, nên chính sách tham lam theo cả hai đều đi phải.

**Kiểm tra lại.** $25{,}12-21{,}28=3{,}84=-2\cdot(-1{,}92)=-2[w_3]_2$ (Mệnh đề 07.32). Hai lỗi thường gặp: dùng giá trị của hành động thực sự chọn tại $\mathrm D$ ở mẫu 2, cho lại kết quả Sarsa; lấy cực đại tại $\mathrm E$ thay cho giá trị $0$ của trạng thái kết thúc.
:::

### Bài tập 07.22. Điểm dừng trung bình của TD(0) tuyến tính

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập 4 của ghi chú: phát biểu và kiểm điểm cố định Bellman chiếu.

**Nguồn:** Bài tập tuần 7 (2025–2026), bài 5 (phiếu viết $\phi(s)$ cho $x(s)$); ghi chú bài giảng Bài 07, Mục 3.2 (Mệnh đề 07.25, 07.26). Dữ kiện câu (c) là số liệu sư phạm tự xây dựng: cùng hai vector đặc trưng với Ví dụ 07.11 nhưng chuỗi khác, có phân phối dừng không đều.

::: exercise Bài tập 07.22 (Điểm dừng trung bình của TD(0) tuyến tính)
Cho $\mathcal S$ hữu hạn, chính sách $\pi$ cố định với ma trận chuyển $P_\pi$ và vector phần thưởng kỳ vọng một bước $r_\pi$, phân phối dừng $d_\pi>0$, $D=\operatorname{diag}(d_\pi)$, ma trận đặc trưng $\Phi$ có hàng $x(s)^\top$ và các cột độc lập tuyến tính, $\gamma\in[0,1)$. TD(0) tuyến tính cập nhật $w_{n+1}=w_n+\alpha_n\delta_tx(S_t)$ với $\delta_t=R_{t+1}+\gamma\,x(S_{t+1})^\top w_n-x(S_t)^\top w_n$. Toán tử Bellman là $T_\pi v=r_\pi+\gamma P_\pi v$; phép chiếu lên $\{\Phi w\}$ theo chuẩn $\lVert v\rVert_D=\sqrt{v^\top Dv}$ là $\Pi_D=\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top D$.

- (a) Với $w$ cố định, $S_t\sim d_\pi$ và $(R_{t+1},S_{t+1})$ sinh theo $\pi$, chứng minh $\mathbb E[\delta_tx(S_t)]=b-Aw$, với $A=\Phi^\top D(I-\gamma P_\pi)\Phi$ và $b=\Phi^\top Dr_\pi$.
- (b) Chứng minh rằng nếu $b-Aw_{\mathrm{TD}}=0$ thì $\Phi w_{\mathrm{TD}}=\Pi_DT_\pi(\Phi w_{\mathrm{TD}})$.
- (c) Áp dụng cho hai trạng thái $x(s_1)=1$, $x(s_2)=2$. Từ $s_1$, chuyển tới $s_1$ hoặc $s_2$ với xác suất $\tfrac12$; từ $s_2$, luôn chuyển về $s_1$. Rời $s_1$ nhận $1$, rời $s_2$ nhận $0$; $\gamma=0{,}9$. Kiểm $d_\pi=(\tfrac23;\tfrac13)$; tính $A$, $b$, $w_{\mathrm{TD}}$ và ma trận $\Pi_D$; kiểm đẳng thức của (b) bằng phép nhân ma trận; so $\Pi_D$ với phép chiếu Euclid $\Phi(\Phi^\top\Phi)^{-1}\Phi^\top$.
- (d) Với cùng dữ kiện, $v_\pi=(\tfrac{200}{29};\tfrac{180}{29})$ và $w_{\mathrm{MC}}=\tfrac{380}{87}\approx4{,}368$ là điểm cực tiểu của sai số giá trị với trọng số $d_\pi$. Tính hướng trung bình $b-Aw_{\mathrm{MC}}$ và xác định chiều mà TD(0) đẩy $w$ khi xuất phát từ $w_{\mathrm{MC}}$.
:::

::: hint Gợi ý Bài tập 07.22
Với (a), lấy kỳ vọng có điều kiện theo $S_t=s$ trước, rồi lấy trung bình theo $d_\pi$; $\sum_sd_\pi(s)x(s)u(s)=\Phi^\top Du$ với mọi vector $u$. Với (b), nhân trái với $\Phi(\Phi^\top D\Phi)^{-1}$. Với (c), $d_\pi$ thỏa $d_\pi^\top P_\pi=d_\pi^\top$.
:::

::: solution Lời giải Bài tập 07.22
**Câu (a).** Khi biết $S_t=s$, $x(s)$ và $w$ là hằng số, và $\mathbb E_\pi[R_{t+1}\mid S_t=s]=r_\pi(s)$, nên

$$
\begin{aligned}
\mathbb E[\delta_tx(S_t)\mid S_t=s]&=x(s)\Big(r_\pi(s)+\gamma\sum_{s'}P_\pi(s,s')x(s')^\top w\\
&\qquad-x(s)^\top w\Big)\\
&=x(s)\big((T_\pi\Phi w)(s)-(\Phi w)(s)\big).
\end{aligned}
$$

Lấy trung bình theo $S_t\sim d_\pi$ (kỳ vọng lặp):

$$
\begin{aligned}
\mathbb E[\delta_tx(S_t)]&=\sum_sd_\pi(s)\,x(s)\big((T_\pi\Phi w)(s)-(\Phi w)(s)\big)\\
&=\Phi^\top D\big(r_\pi+\gamma P_\pi\Phi w-\Phi w\big)\\
&=\Phi^\top Dr_\pi-\Phi^\top D(I-\gamma P_\pi)\Phi w\\
&=b-Aw.
\end{aligned}
$$

**Câu (b).** Đặt $v=T_\pi(\Phi w_{\mathrm{TD}})$. Theo câu (a), $b-Aw_{\mathrm{TD}}=\Phi^\top D(v-\Phi w_{\mathrm{TD}})$. Ma trận $\Phi^\top D\Phi$ khả nghịch vì $z^\top\Phi^\top D\Phi z=\lVert\Phi z\rVert_D^2>0$ khi $z\ne0$ (cột độc lập, $d_\pi>0$). Từ $\Phi^\top D(v-\Phi w_{\mathrm{TD}})=0$:

$$
\begin{aligned}
\Phi^\top Dv&=\Phi^\top D\Phi\,w_{\mathrm{TD}},\\
\Phi(\Phi^\top D\Phi)^{-1}\Phi^\top Dv&=\Phi w_{\mathrm{TD}},\\
\Pi_DT_\pi(\Phi w_{\mathrm{TD}})&=\Phi w_{\mathrm{TD}}.
\end{aligned}
$$

Theo trung bình, TD(0) dừng khi phần dư Bellman $T_\pi(\Phi w)-\Phi w$ trực giao với mọi cột của $\Phi$ theo tích vô hướng $\langle u,u'\rangle_D=u^\top Du'$. $\square$

**Câu (c).** Phân phối dừng: $\tfrac23\cdot\tfrac12+\tfrac13\cdot1=\tfrac23$ và $\tfrac23\cdot\tfrac12+\tfrac13\cdot0=\tfrac13$, nên $d_\pi^\top P_\pi=d_\pi^\top$ với $d_\pi=(\tfrac23;\tfrac13)$. Tiếp theo, $P_\pi\Phi=(\tfrac12\cdot1+\tfrac12\cdot2;\ 1)=(1{,}5;1)$, nên $(I-\gamma P_\pi)\Phi=(1-1{,}35;\ 2-0{,}9)=(-0{,}35;1{,}1)$.

$$
\begin{aligned}
A&=\tfrac23\cdot1\cdot(-0{,}35)+\tfrac13\cdot2\cdot1{,}1=\tfrac12,\\
b&=\tfrac23\cdot1\cdot1+\tfrac13\cdot2\cdot0=\tfrac23,\\
w_{\mathrm{TD}}&=\tfrac23\big/\tfrac12=\tfrac43 .
\end{aligned}
$$

$\Phi^\top D\Phi=\tfrac23\cdot1+\tfrac13\cdot4=2$ và $\Phi^\top D=(\tfrac23;\,\tfrac23)^\top$, nên

$$
\Pi_D=\frac12\begin{bmatrix}1\\2\end{bmatrix}\begin{bmatrix}\tfrac23&\tfrac23\end{bmatrix}=\begin{bmatrix}\tfrac13&\tfrac13\\[2pt]\tfrac23&\tfrac23\end{bmatrix}.
$$

Ảnh Bellman: $T_\pi(\Phi w_{\mathrm{TD}})=r_\pi+\gamma P_\pi\Phi\,w_{\mathrm{TD}}=(1;0)+\tfrac43(1{,}35;0{,}9)=(2{,}8;1{,}2)$. Nhân với $\Pi_D$:

$$
\Pi_D\begin{bmatrix}2{,}8\\1{,}2\end{bmatrix}=\begin{bmatrix}\tfrac13(2{,}8+1{,}2)\\[2pt]\tfrac23(2{,}8+1{,}2)\end{bmatrix}=\begin{bmatrix}\tfrac43\\[2pt]\tfrac83\end{bmatrix}=\Phi w_{\mathrm{TD}}.
$$

Phép chiếu Euclid là $\tfrac15\begin{bmatrix}1&2\\2&4\end{bmatrix}$, khác $\Pi_D$; áp vào $(2{,}8;1{,}2)$ nó cho $(1{,}04;2{,}08)\ne\Phi w_{\mathrm{TD}}$. Trọng số $D$ quyết định điểm cố định.

**Câu (d).** $b-Aw_{\mathrm{MC}}=\tfrac23-\tfrac12\cdot\tfrac{380}{87}=\tfrac{58-190}{87}=-\tfrac{44}{29}\approx-1{,}517<0$. Theo trung bình, TD(0) giảm $w$ khi xuất phát từ $w_{\mathrm{MC}}$; hướng trung bình $b-Aw=\tfrac12(w_{\mathrm{TD}}-w)$ đổi dấu tại $w_{\mathrm{TD}}=\tfrac43$, nên điểm dừng của TD(0) khác điểm cực tiểu sai số giá trị.

**Kiểm tra lại.** $\Pi_D^2=\Pi_D$: hàng đầu của $\Pi_D^2$ là $(\tfrac19+\tfrac29;\ \tfrac19+\tfrac29)=(\tfrac13;\tfrac13)$. Với $v_\pi$ đã cho: $v_1=1+0{,}9(\tfrac12v_1+\tfrac12v_2)$ và $v_2=0{,}9v_1$ đều đúng. Ba lỗi thường gặp: dùng phép chiếu Euclid, bỏ trọng số $D$, cho $(1{,}04;2{,}08)$; viết $A=\Phi^\top D(I-\gamma P_\pi)$, thiếu $\Phi$ bên phải; kết luận dãy TD(0) hội tụ chỉ từ câu (b), trong khi (b) chỉ mô tả điểm có hướng trung bình bằng $0$ (hội tụ là Định lý 07.29).
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 07.14. Nhận diện bộ ba bất ổn

**Mức độ:** vận dụng. Mục tiêu học tập 5 của ghi chú: nhận diện bộ ba bất ổn trong một quy tắc cập nhật.

**Nguồn:** Bài tập tuần 7 (2025–2026), bài 3; ghi chú bài giảng Bài 07, Mục 5.2, Bài tập 07.14.

**Trùng trang chiếu:** [Bài tập: nhận diện bộ ba bất ổn](lecture-07-xap-xi-ham.html#/6/10) và [trang lời giải](lecture-07-xap-xi-ham.html#/6/11).

::: exercise Bài tập 07.14 (Nhận diện bộ ba bất ổn)
Một phương pháp học giá trị có bộ ba bất ổn khi có đồng thời: xấp xỉ hàm (tham số dùng chung, một cập nhật đổi nhiều dự đoán); bootstrap (mục tiêu chứa ước lượng hiện tại); học khác chính sách (phân phối các chuyển dùng để cập nhật khác phân phối do chính sách đích sinh ra). Với mỗi quy tắc sau, xác định ba yếu tố; với (a)–(c), kết luận thêm có bảo đảm hội tụ theo Định lý 07.29 (TD(0) tuyến tính theo chính sách cố định) hay không.

- (a) TD(0) tuyến tính với chính sách cố định, dữ liệu sinh theo chính sách đó.
- (b) Sarsa tuyến tính với chính sách $\varepsilon$-tham lam $\pi_w$ theo $\hat q(\cdot,\cdot,w)$.
- (c) Q-learning tuyến tính.
- (d) Monte Carlo gradient tuyến tính với dữ liệu khác chính sách và lấy mẫu quan trọng (importance sampling).
:::

::: hint Gợi ý Bài tập 07.14
Ba câu kiểm: tham số có dùng chung không; mục tiêu có chứa ước lượng đang học không; phân phối dữ liệu có khác chính sách đích không. Định lý 07.29 còn đòi chính sách cố định.
:::

::: solution Lời giải Bài tập 07.14
Bảng dùng cùng cột với trang lời giải của trang chiếu.

| Quy tắc | Xấp xỉ hàm | Bootstrap | Khác chính sách | Kết luận |
| --- | --- | --- | --- | --- |
| (a) TD(0) | có | có | không | có bảo đảm, khi đủ các giả thiết còn lại |
| (b) Sarsa | có | có | không | không có bảo đảm chung: $\pi_w$ đổi theo $w$ |
| (c) Q-learning | có | có | có | không có bảo đảm chung: đủ ba yếu tố |
| (d) Monte Carlo | có | không | có | không đủ ba yếu tố |

**Câu (a).** Mục tiêu $R_{t+1}+\gamma x(S_{t+1})^\top w_n$ chứa $w_n$; dữ liệu và chính sách đích đều là $\pi$. Định lý 07.29 cho $w_n\to w_{\mathrm{TD}}$ hầu chắc chắn khi thêm chuỗi trạng thái tối giản (irreducible), không tuần hoàn (aperiodic), bài toán không kết thúc, $\gamma<1$, phần thưởng bị chặn, cột của $\Phi$ độc lập và bước Robbins–Monro.

**Câu (b).** Theo chính sách vì $A'$ do $\pi_w$ chọn, kể cả khi thăm dò. Chưa đủ ba yếu tố, nhưng $\pi_w$ đổi theo $w$ nên giả thiết "chính sách cố định" của Định lý 07.29 không thỏa; không có kết quả hội tụ chung (Nhận xét 07.34).

**Câu (c).** Dữ liệu theo chính sách hành vi $\varepsilon$-tham lam, còn mục tiêu dùng phép cực đại, tức chính sách đích tham lam: đủ ba yếu tố, không có bảo đảm chung. Mệnh đề 07.37 là ví dụ phân kỳ của TD(0) khác chính sách cùng ba yếu tố; Q-learning có phản ví dụ phân kỳ tương tự phản ví dụ của Baird (Sutton và Barto, 2018, §11.2, tr. 263). Bài tập 07.23 dựng một ví dụ phân kỳ trực tiếp cho Q-learning.

**Câu (d).** Lợi tức không bootstrap, nên không đủ ba yếu tố. Định lý 07.17 không áp dụng nguyên văn vì lợi tức không sinh theo $\pi$; lấy mẫu quan trọng (ghi chú Bài 06, Mục 6) nhân lợi tức với tích các tỉ số $\rho_t=\pi(A_t\mid S_t)/\pi_b(A_t\mid S_t)$ dọc quỹ đạo để sửa kỳ vọng, đổi lại phương sai lớn.

**Kiểm tra lại.** Chỉ (c) đủ ba yếu tố, phù hợp với bài giảng gốc (2025–2026, trang 37, 41). Hai lỗi thường gặp: coi Sarsa là khác chính sách vì có thăm dò; kết luận Sarsa có bảo đảm hội tụ vì chỉ có hai yếu tố, bỏ qua giả thiết chính sách cố định.
:::

### Bài tập 07.23. Q-learning bán gradient trên một mảnh MDP hai trạng thái

**Mức độ:** vận dụng. Mục tiêu học tập 5 và 6 của ghi chú: nhận diện bộ ba bất ổn, đối chiếu một ví dụ phân kỳ với giả thiết bị bỏ.

**Nguồn:** biến thể Q-learning của ví dụ $w\to2w$ trong Sutton và Barto (2018, §11.2, tr. 260), cùng hai vector đặc trưng và cùng hệ số tăng với Ví dụ 07.15 và Mệnh đề 07.37 của ghi chú; liên quan trang chiếu [Ví dụ: hai trạng thái khác chính sách](lecture-07-xap-xi-ham.html#/6/7). Số liệu sư phạm tự xây dựng.

::: exercise Bài tập 07.23 (Q-learning bán gradient trên một mảnh MDP hai trạng thái)
Một MDP gồm hai trạng thái không kết thúc $s_1$, $s_2$ và một trạng thái kết thúc. Tại $s_1$ chỉ có hành động $a_0$ (đi sang $s_2$). Tại $s_2$ có hai hành động: $a_1$ (về $s_1$) và $a_2$ (ra trạng thái kết thúc). Mọi chuyển tất định, mọi phần thưởng bằng $0$; $\gamma=0{,}9$. Giá trị hành động là $\hat q(s,a,w)=x(s,a)\,w$ với tham số một chiều $w\in\mathbb R$ và $x(s_1,a_0)=1$, $x(s_2,a_1)=2$, $x(s_2,a_2)=0$. Chính sách hành vi luôn chọn $a_2$ tại $s_2$, nên mỗi lượt gồm hai chuyển $(s_1,a_0,0,s_2)$ rồi $(s_2,a_2,0,\text{kết thúc})$. Q-learning bán gradient dùng mục tiêu $y=R$ khi chuyển vào trạng thái kết thúc và $y=R+\gamma\max_{a'}\hat q(S',a',w_n)$ khi không, cập nhật $w_{n+1}=w_n+\alpha\big(y-\hat q(S,A,w_n)\big)x(S,A)$ theo thứ tự hai chuyển của mỗi lượt, với $\alpha=0{,}1$. Trong bài này $w^{(k)}$ là tham số sau $k$ lượt, tức $w^{(k)}=w_{2k}$.

- (a) Chứng minh $q_*\equiv0$ và $w=0$ biểu diễn đúng $q_*$.
- (b) Với $w^{(0)}=1$, chứng minh rằng sau mỗi lượt $w$ nhân với $1+\alpha(2\gamma-1)$; tính $w^{(1)}$, $w^{(2)}$, $w^{(30)}$. Xác định mọi cặp $(\alpha,\gamma)$ với $\alpha>0$, $\gamma\in[0,1)$ để hệ số này lớn hơn $1$, và chính sách đích tham lam tại $s_2$ trong suốt quá trình.
- (c) Lặp lại (b) với $w^{(0)}=-1$.
- (d) Thay hàm tuyến tính bằng bảng $Q$ có ba ô, khởi tạo bằng dự đoán ban đầu của (b): $Q(s_1,a_0)=1$, $Q(s_2,a_1)=2$, $Q(s_2,a_2)=0$; cùng dữ liệu, $\gamma$, $\alpha$. Tính $Q(s_1,a_0)$ sau $k$ lượt và giới hạn của nó.
- (e) Giả sử dữ liệu do chính sách tham lam theo $\hat q(\cdot,\cdot,w)$ sinh ra, xuất phát từ $s_1$ với $w_0=1$. Chứng minh chuỗi chuyển là $s_1\to s_2\to s_1\to\cdots$ khi $w>0$; tính $w$ sau một vòng hai cập nhật và giới hạn của $w$.
- (f) So (b) với (e) bằng đại lượng $A=\sum_{(s,a)}\mu(s,a)\,x(s,a)\big(x(s,a)-\gamma\,x(s',a^*)\big)$, trong đó $\mu$ là tỉ lệ số lần mỗi cặp được cập nhật, $s'$ là trạng thái kế tiếp, $a^*$ là hành động tham lam tại $s'$, và số hạng $\gamma\,x(s',a^*)$ bằng $0$ khi $s'$ kết thúc. Nêu ba yếu tố của bộ ba bất ổn trong (b) và yếu tố bị bỏ ở (d), (e).
:::

::: hint Gợi ý Bài tập 07.23
Với $w>0$, $\max(2w,0)=2w$; với $w<0$, $\max(2w,0)=0$. Cập nhật tại $(s_2,a_2)$ nhân với $x(s_2,a_2)=0$. Với (e), mục tiêu tại $(s_2,a_1)$ là $\gamma\,\hat q(s_1,a_0,w)$ vì $s_1$ chỉ có một hành động.
:::

::: solution Lời giải Bài tập 07.23
**Câu (a).** Mọi phần thưởng bằng $0$, nên mọi lợi tức bằng $0$ và $q_\pi\equiv0$ với mọi chính sách $\pi$; do đó $q_*\equiv0$. Với $w=0$, $\hat q(s,a,0)=x(s,a)\cdot0=0$ ở cả ba cặp, nên lớp biểu diễn chứa $q_*$ và sai số xấp xỉ bằng $0$.

**Câu (b).** Xét lượt có tham số đầu $w>0$. Chuyển thứ nhất cập nhật cặp $(s_1,a_0)$:

$$
\begin{aligned}
\text{mục tiêu: }&y=0+\gamma\max\big(\hat q(s_2,a_1,w);\hat q(s_2,a_2,w)\big)\\
&\phantom{y}=\gamma\max(2w;0)=2\gamma w,\\
\text{sai số TD: }&\delta=2\gamma w-w=(2\gamma-1)w,\\
\text{tham số mới: }&w'=w+\alpha(2\gamma-1)w\cdot1\\
&\phantom{w'}=\big(1+\alpha(2\gamma-1)\big)w.
\end{aligned}
$$

Chuyển thứ hai vào trạng thái kết thúc nên $y=0$, $\delta=0-0=0$, và $x(s_2,a_2)=0$; tham số không đổi. Với $\gamma=0{,}9$, $\alpha=0{,}1$, hệ số là $1{,}08$, nên $w$ giữ dấu dương và $w^{(k)}=1{,}08^k$: $w^{(1)}=1{,}08$, $w^{(2)}=1{,}1664$, $w^{(30)}\approx10{,}06$. Hệ số $1+\alpha(2\gamma-1)$ lớn hơn $1$ khi và chỉ khi $2\gamma-1>0$, tức với mọi $\alpha>0$ và mọi $\gamma\in(\tfrac12,1)$; khi đó $w^{(k)}\to\infty$, dù $q_*$ biểu diễn được bằng $w=0$. Vì $w>0$, $\hat q(s_2,a_1,w)=2w>0=\hat q(s_2,a_2,w)$, nên chính sách đích tham lam luôn chọn $a_1$, trong khi chính sách hành vi luôn chọn $a_2$.

**Câu (c).** Với $w<0$, $\max(2w;0)=0$, nên mục tiêu tại $(s_1,a_0)$ là $0$, $\delta=-w$ và $w'=(1-\alpha)w=0{,}9w$. Từ $w^{(0)}=-1$: $w^{(1)}=-0{,}9$, $w^{(2)}=-0{,}81$, $w^{(30)}=-0{,}9^{30}\approx-0{,}042$; $w^{(k)}\to0$. Chính sách đích tham lam tại $s_2$ chọn $a_2$ ($0>2w$), trùng chính sách hành vi.

**Câu (d).** Ô $(s_2,a_2)$ có mục tiêu $0$ và giá trị đầu $0$, nên giữ $0$. Ô $(s_2,a_1)$ không bao giờ được cập nhật, giữ $2$. Ô $(s_1,a_0)$ có mục tiêu $0{,}9\max(2;0)=1{,}8$ ở mọi lượt. Gọi $Q^{(k)}$ là giá trị của ô này sau $k$ lượt:

$$
\begin{aligned}
1{,}8-Q^{(k+1)}&=0{,}9\big(1{,}8-Q^{(k)}\big),\\
Q^{(k)}&=1{,}8-0{,}8\cdot0{,}9^k\to1{,}8.
\end{aligned}
$$

Bảng cho $1{,}08$; $1{,}152$; … và bị chặn bởi $1{,}8$. Giới hạn khác $q_*(s_1,a_0)=0$ vì cặp $(s_2,a_1)$ không được ghé: bảo đảm dạng bảng cần mọi cặp được cập nhật vô hạn lần (ghi chú Bài 06, Mục 5).

**Câu (e).** Khi $w>0$, tại $s_2$ hành động tham lam là $a_1$, còn $s_1$ chỉ có $a_0$, nên chuỗi là $s_1\to s_2\to s_1\to\cdots$ và không kết thúc. Một vòng gồm hai cập nhật. Tại $(s_1,a_0)$:

$$
\begin{aligned}
\delta&=0{,}9\cdot2w-w=0{,}8w,\\
w'&=w+0{,}1\cdot0{,}8w=1{,}08w.
\end{aligned}
$$

Tại $(s_2,a_1)$, với mục tiêu $0{,}9\,\hat q(s_1,a_0,w')=0{,}9w'$:

$$
\begin{aligned}
\delta&=0{,}9w'-2w'=-1{,}1w',\\
w''&=w'+0{,}1\cdot(-1{,}1w')\cdot2=0{,}78w'.
\end{aligned}
$$

Sau một vòng $w$ nhân với $1{,}08\cdot0{,}78=0{,}8424$, nên từ $w_0=1$: $0{,}8424$ sau vòng một, khoảng $0{,}180$ sau mười vòng, và $w\to0=q_*$. Hệ số dương nên $w$ giữ dấu dương, đúng giả thiết dùng để xác định hành động tham lam. Chuỗi trên các cặp có chu kỳ $2$ và chính sách đổi theo $w$, nên Định lý 07.29 không áp dụng nguyên văn; kết luận ở đây đến từ phép tính trực tiếp.

**Câu (f).** Ở (b), mỗi lượt cập nhật hai cặp $(s_1,a_0)$ và $(s_2,a_2)$, mỗi cặp một lần; ở (e), mỗi vòng cập nhật $(s_1,a_0)$ và $(s_2,a_1)$, mỗi cặp một lần. Vì vậy $\mu$ gán $\tfrac12$ cho mỗi cặp được cập nhật. Với $w>0$, $a^*=a_1$ tại $s_2$. Mọi phần thưởng bằng $0$, nên hướng cập nhật trung bình là $-Aw$.

$$
\begin{aligned}
\text{(b): }A&=\tfrac12\cdot1\cdot(1-0{,}9\cdot2)+\tfrac12\cdot0\cdot(0-0)\\
&=-0{,}4<0,\\
\text{(e): }A&=\tfrac12\cdot1\cdot(1-0{,}9\cdot2)+\tfrac12\cdot2\cdot(2-0{,}9\cdot1)\\
&=-0{,}4+1{,}1=0{,}7>0.
\end{aligned}
$$

Cùng đặc trưng, cùng $\gamma$ và $\alpha$; chỉ phân phối cập nhật khác nhau. Với $A<0$, hướng trung bình $0{,}4w$ cùng dấu với $w$ và đẩy $w$ ra xa $0$; với $A>0$, hướng $-0{,}7w$ kéo $w$ về $0$. Với $w<0$ ở (c), $a^*=a_2$, nên $A=\tfrac12\cdot1\cdot(1-0)=\tfrac12>0$, khớp với hệ số $0{,}9$ mỗi lượt. Trong (b) có đủ ba yếu tố: xấp xỉ hàm, vì $w$ dùng chung cho $(s_1,a_0)$ và $(s_2,a_1)$, nên nâng $\hat q(s_1,a_0)$ một lượng thì $\hat q(s_2,a_1)$ tăng gấp đôi; bootstrap, vì mục tiêu chứa $\max_{a'}\hat q(s_2,a',w)$; khác chính sách, vì hành vi chọn $a_2$ còn mục tiêu dùng $a_1$, và cặp $(s_2,a_1)$ không bao giờ được cập nhật để kéo $w$ xuống. Câu (d) bỏ xấp xỉ hàm và giá trị bị chặn. Câu (e) bỏ học khác chính sách và $w\to0$.

**Diễn giải.** Trên cùng dữ liệu của (b), Sarsa dùng hành động kế tiếp thực sự chọn, nên mục tiêu tại $(s_1,a_0)$ là $0+\gamma\,\hat q(s_2,a_2,w)=0$ và $w\leftarrow0{,}9w$. Phép cực đại đưa giá trị của hành động không được ghé vào mục tiêu; ở Ví dụ 07.15 của ghi chú, cơ chế tương ứng là tỉ số lấy mẫu quan trọng của TD(0) dự đoán.

**Kiểm tra lại.** $w^{(1)}=1{,}08$ trùng $w_1$ của Ví dụ 07.15, vì hệ số $1+\alpha(2\gamma-1)$ giống Mệnh đề 07.37; ô bảng $Q^{(1)}=1+0{,}1\cdot(1{,}8-1)=1{,}08$ cũng bằng $w^{(1)}$ vì hai cách cùng xuất phát từ $\hat q(s_1,a_0)=1$. Ba lỗi thường gặp: lấy cực đại chỉ trên hành động mà hành vi chọn, cho mục tiêu $0$ và kết luận $w$ giảm; cho rằng cập nhật tại $(s_2,a_2)$ kéo $w$ về $0$, trong khi $x(s_2,a_2)=0$; quên rằng hành động tham lam phụ thuộc dấu của $w$, áp công thức của (b) cho $w^{(0)}=-1$.
:::

### Bài tập 07.24. Bước học Robbins–Monro trên dữ liệu Lunar Lander [Lập trình]

**Mức độ:** vận dụng [Lập trình]. Mục tiêu học tập 4 và 6 của ghi chú: kiểm điều kiện Robbins–Monro và điều kiện ổn định trên dữ liệu thật, phân biệt hai đích dự đoán.

**Nguồn:** notebook `thuc-hanh-lunarlander-xap-xi-tuyen-tinh.ipynb`, mục 6–8 (phần A, dự đoán); dạng bước học giảm dần lấy từ gợi mở 5 của mục 16, nơi nó được đề xuất cho phần B (điều khiển), ở đây áp cho phần A. Ghi chú bài giảng Bài 07, Định lý 07.17, Mệnh đề 07.25, 07.28, Tình huống 07.1. Số liệu là một lần chạy đã nhúng trong notebook.

::: exercise Bài tập 07.24 (Bước học Robbins–Monro trên dữ liệu Lunar Lander [Lập trình])
Notebook Lunar Lander dự đoán giá trị của một chính sách $\pi$ cố định từ $2\,000$ lượt huấn luyện gồm $546\,869$ chuyển; $42$ lượt bị cắt ngắn (truncation) ở $1\,000$ bước, tức bị dừng vì giới hạn số bước khi trạng thái chưa kết thúc; $504\,869$ chuyển thuộc các lượt kết thúc thật. Hệ số chiết khấu $\gamma=0{,}99$; đặc trưng Fourier bậc 3 có $d=156$ thành phần, bị chặn, và ma trận đặc trưng có hạng $156/156$ theo kết quả in ra của notebook. Thước đo $J_{\mathrm{kt}}$ là trung bình của $(G_t-\hat v(S_t,w))^2$ trên mọi thời điểm của các lượt kết thúc thật trong $500$ lượt kiểm tra ($7$ lượt kiểm tra bị cắt ngắn). Notebook dùng bước hằng $\alpha=\kappa/\mathbb E\lVert x(S)\rVert^2$ và một lượt qua dữ liệu theo thứ tự thời gian; lần chạy đã nhúng cho $J_{\mathrm{kt}}=2\,190{,}1$ với Monte Carlo ($\kappa=0{,}01$), $1\,855{,}2$ với TD(0) ($\kappa=0{,}03$), $1\,481{,}0$ với nghiệm Monte Carlo theo lô $w_{\mathrm{lô}}$, và $1\,612{,}8$ với nghiệm LSTD $w_{\mathrm{LSTD}}$ trên toàn bộ $546\,869$ chuyển. Ghi chú bài giảng và mục 15 của notebook dùng số $1\,622{,}2$, là LSTD chỉ trên các lượt kết thúc thật; bài này dùng $1\,612{,}8$ vì câu (c) rút mẫu từ toàn bộ dữ liệu.

- (a) Chứng minh dãy $\alpha_n=\kappa\big/\big(\mathbb E\lVert x(S)\rVert^2\,(1+n/n_0)\big)$, với $\kappa,n_0>0$, thỏa điều kiện Robbins–Monro.
- (b) Cài Monte Carlo gradient trong đó lần cập nhật thứ $n$ dùng một cặp $(S_t,G_t)$ rút đều, có hoàn lại, từ $504\,869$ cặp của các lượt kết thúc thật, với bước học của (a). Trước khi chạy, dùng Định lý 07.17 để xác định giới hạn của $w_n$. Chạy, rồi ghi $\lVert w_n-w_{\mathrm{lô}}\rVert$ và $J_{\mathrm{kt}}(w_n)$ tại các mốc số cập nhật.
- (c) Làm tương tự cho TD(0) bán gradient: rút đều từng chuyển $(S_t,R_{t+1},S_{t+1})$ trong $546\,869$ chuyển, với mục tiêu $R_{t+1}$ khi $S_{t+1}$ là trạng thái kết thúc thật và mục tiêu bootstrap ở bước cắt ngắn; so với $w_{\mathrm{LSTD}}$. Trước khi chạy, lấy ma trận $\hat A$ do hàm `lstd` của notebook trả về, kiểm điều kiện của Mệnh đề 07.28 cho $\hat A$ bằng số và dùng kết quả để dự đoán giới hạn.
- (d) Lập bảng $J_{\mathrm{kt}}$ của ba cách cho mỗi phương pháp: một lượt với bước hằng; rút mẫu với bước Robbins–Monro; nghiệm theo lô. Giải thích khoảng cách giữa cột thứ nhất và cột thứ ba bằng việc thuật toán chưa tới điểm đích của nó, và nói rõ khoảng cách đó có phải sai số ước lượng theo Định nghĩa 07.11 hay không.
:::

::: hint Gợi ý Bài tập 07.24
Tính trước ma trận đặc trưng dạng `float32` của mọi thời điểm cần dùng (khoảng $300$ MB cho $504\,869\times156$ phần tử) và vector $G_t$; rút chỉ số bằng `rng.integers`. Để chọn $\kappa$, $n_0$ và số cập nhật, sinh một tập tinh chỉnh $500$ lượt theo $\pi$ với các hạt giống ngẫu nhiên (random seed) $800000+i$ như mô tả ở mục 6 của notebook (notebook không sinh sẵn tập này); không chọn trên tập kiểm tra, và ghi mọi cấu hình đã thử. Với (c), Mệnh đề 07.28 dùng điều kiện $z^\top Az>0$ với mọi $z\ne0$; vì $z^\top\hat Az=z^\top\tfrac12(\hat A+\hat A^\top)z$, điều kiện đó kiểm được bằng trị riêng nhỏ nhất của phần đối xứng. Theo phân phối rút mẫu, $\mathbb E[\delta x]=(\hat b-\hat Aw)/N$, với $N$ là số chuyển.
:::

::: solution Lời giải Bài tập 07.24
**Câu (a).** Đặt $c=\kappa/\mathbb E\lVert x(S)\rVert^2>0$, nên $\alpha_n=c\,n_0/(n_0+n)$.

$$
\begin{aligned}
\sum_{n\ge0}\alpha_n&=c\,n_0\sum_{n\ge0}\frac1{n_0+n}=\infty,\\
\sum_{n\ge0}\alpha_n^2&=c^2n_0^2\sum_{n\ge0}\frac1{(n_0+n)^2}\\
&\le c^2n_0^2\Big(\frac1{n_0^2}+\int_{n_0}^\infty\frac{dt}{t^2}\Big)=c^2(1+n_0)<\infty .
\end{aligned}
$$

Chuỗi thứ nhất phân kỳ như chuỗi điều hòa; chuỗi thứ hai bị chặn bằng so sánh với tích phân.

**Câu (b).** Áp Định lý 07.17 cho bài toán thay thế: $\mu$ là phân phối đều trên $504\,869$ thời điểm, và mỗi cập nhật dùng một cặp $(S,G)$ rút độc lập từ phân phối đó. Trong bài toán thay thế, vai trò của $v_\pi(s)$ do trung bình có điều kiện thực nghiệm của $G$ khi biết $S=s$ đảm nhận; với quan sát liên tục, mỗi $S_t$ xuất hiện một lần nên trung bình đó bằng chính $G_t$. Chứng minh của Định lý 07.17 chỉ dùng $\mathbb E[x(S)x(S)^\top]$ và $\mathbb E[x(S)G]$, nên kết luận chuyển sang nghiệm của phương trình chuẩn. Kiểm năm giả thiết:

- giả thiết 1: dữ liệu cố định nên $\mu$ và phân phối có điều kiện của $G$ cố định;
- giả thiết 2: các mẫu độc lập nhờ rút có hoàn lại;
- giả thiết 3: đặc trưng bị chặn (hàm $\cos$ và cờ chân); $G$ bị chặn trên tập dữ liệu hữu hạn;
- giả thiết 4: $\hat\Sigma=\tfrac1N\sum_tx_tx_t^\top$ xác định dương, vì ma trận đặc trưng có hạng $156/156$;
- giả thiết 5: bước học thỏa Robbins–Monro theo câu (a).

Kết luận: $w_n$ hội tụ hầu chắc chắn tới điểm cực tiểu duy nhất của $\tfrac1N\sum_t(G_t-x_t^\top w)^2$, tức nghiệm của $\big(\sum_tx_tx_t^\top\big)w=\sum_tx_tG_t$. Nghiệm này khác $w_{\mathrm{lô}}$ của notebook một số hạng điều chuẩn $10^{-6}\operatorname{tr}(\cdot)/p$ thêm vào để giải ổn định, nên $J_{\mathrm{kt}}(w_n)$ tiến tới $J_{\mathrm{kt}}$ của nghiệm phương trình chuẩn, xấp xỉ $1\,481{,}0$. Định lý cho giới hạn, không cho tốc độ: theo các hướng ứng với trị riêng nhỏ của $\hat\Sigma$, sai lệch giảm chậm, nên sau số cập nhật hữu hạn $J_{\mathrm{kt}}$ có thể còn trên mức đó. Báo cáo cần cho thấy $\lVert w_n-w_{\mathrm{lô}}\rVert$ giảm theo các mốc.

**Câu (c).**

1. **Hướng trung bình.** Theo phân phối rút đều trên $N=546\,869$ chuyển, lập luận của Mệnh đề 07.25 cho hướng trung bình $(\hat b-\hat Aw)/N$, với $\hat A=\sum_tx_t(x_t-\gamma x_{t+1})^\top$, $\hat b=\sum_tx_tR_{t+1}$ và $x_{t+1}=0$ khi $S_{t+1}$ kết thúc thật.
2. **Điều kiện kiểm được.** Mệnh đề 07.28 dùng $z^\top Az>0$ với mọi $z\ne0$. Với $\hat A_{\mathrm s}=\tfrac12(\hat A+\hat A^\top)$, ta có $z^\top\hat Az=z^\top\hat A_{\mathrm s}z$, nên điều kiện tương đương $\lambda_{\min}(\hat A_{\mathrm s})>0$, tính bằng `np.linalg.eigvalsh`.
3. **Kết luận khi điều kiện thỏa.** Đặt $e=w-\hat A^{-1}\hat b$. Một bước của hệ trung bình cho $\lVert e-\tfrac{\alpha}N\hat Ae\rVert^2=\lVert e\rVert^2-\tfrac{2\alpha}Ne^\top\hat A_{\mathrm s}e+\tfrac{\alpha^2}{N^2}\lVert\hat Ae\rVert^2<\lVert e\rVert^2$ khi $e\ne0$ và $\alpha$ đủ nhỏ. Đây là vai trò của Mệnh đề 07.28 trong ý tưởng chứng minh Định lý 07.29. Cùng với mẫu độc lập, đặc trưng bị chặn và bước Robbins–Monro, kết quả xấp xỉ ngẫu nhiên với hàm Lyapunov $\lVert w-w^*\rVert^2$ (Bertsekas và Tsitsiklis, 1996, chương 4) cho $w_n\to\hat A^{-1}\hat b=w_{\mathrm{LSTD}}$ (sai khác số hạng điều chuẩn), và $J_{\mathrm{kt}}(w_n)$ tiến tới xấp xỉ $1\,612{,}8$, không tới $1\,481{,}0$: hai phương pháp có hai đích khác nhau.
4. **Vì sao phải kiểm bằng số.** Định lý 07.29 không áp dụng nguyên văn:
   - bài toán theo lượt, không phải không kết thúc;
   - trọng số là tần suất ghé thực nghiệm, không phải phân phối dừng, nên Bổ đề 07.27 không cho sẵn tính xác định dương;
   - quan sát thiếu địa hình nên tính Markov chưa chắc.

**Nhận xét.** Điều kiện yếu hơn là mọi trị riêng của $\hat A$ có phần thực dương, tức $-\hat A$ ổn định. Điều kiện ở bước 2 kéo theo điều kiện này, nhưng ngược lại thì không. Với điều kiện yếu hơn, $\lVert e\rVert^2$ có thể tăng ở một số bước và cần một hàm Lyapunov khác; phương pháp phương trình vi phân thường (ordinary differential equation, ODE) cho xấp xỉ ngẫu nhiên vẫn cho hội tụ (Borkar và Meyn, 2000). Nếu có trị riêng với phần thực âm, hệ trung bình phân kỳ theo hướng đó; nếu phần thực bằng $0$, hệ trung bình không co theo hướng đó. Trong hai trường hợp này không có bảo đảm.

**Câu (d).** Bảng có dạng sau; cột giữa điền từ lần chạy của người làm bài.

| Phương pháp | Một lượt, bước hằng | Rút mẫu, Robbins–Monro | Nghiệm theo lô |
| --- | --- | --- | --- |
| Monte Carlo | $2\,190{,}1$ | (đo được) | $1\,481{,}0$ |
| TD(0) | $1\,855{,}2$ | (đo được) | $1\,612{,}8$ |

Khoảng cách giữa cột thứ nhất và cột thứ ba là sai lệch do thuật toán chưa tới điểm đích của nó: bước hằng, chỉ một lượt, thứ tự mẫu theo thời gian. Cột giữa cho biết phần sai lệch còn lại sau số cập nhật đã chạy. Khoảng cách này không đúng là sai số ước lượng của Định nghĩa 07.11, vì hai lý do. Thứ nhất, $J_{\mathrm{kt}}$ đo trên tập kiểm tra, còn $w_{\mathrm{lô}}$ cực tiểu tiêu chí trên tập huấn luyện, nên $J_{\mathrm{kt}}(w_{\mathrm{lô}})$ không phải $\inf_wJ_{\mathrm{kt}}$, và về nguyên tắc hiệu có thể âm. Chỉ ở hàng Monte Carlo, và chỉ khi đo bằng tiêu chí huấn luyện, khoảng cách mới là sai số ước lượng của Định nghĩa 07.11 với $J_\mu$ thay bằng tiêu chí thực nghiệm. Thứ hai, ở hàng TD(0), $w_{\mathrm{LSTD}}$ là điểm cố định Bellman chiếu thực nghiệm, không cực tiểu tiêu chí bình phương nào; khoảng cách ở hàng này là khoảng cách tới điểm cố định đó. Chênh lệch giữa hai hàng ở cột thứ ba đến từ hai đích khác nhau.

**Kiểm tra lại.** Trước khi chạy dài, kiểm một cập nhật bằng tay như ô tính tay của mục 6, và kiểm $\hat A\,w_{\mathrm{LSTD}}\approx\hat b$. Bốn lỗi thường gặp: duyệt mẫu theo thứ tự thời gian trong lượt, làm mẫu phụ thuộc nhau và vi phạm giả thiết 2 của Định lý 07.17; chọn $\kappa$, $n_0$ trên tập kiểm tra; so $J_{\mathrm{kt}}$ của TD(0) với $1\,481{,}0$ thay cho $1\,612{,}8$; dùng lượt bị cắt ngắn trong Monte Carlo, hoặc gán giá trị $0$ ở bước cắt ngắn của TD(0).
:::

### Bài tập 07.25. Phân biệt phân kỳ với chính sách kém trên Flappy Bird [Lập trình]

**Mức độ:** vận dụng [Lập trình]. Mục tiêu học tập 5 và 6 của ghi chú: đọc $\lVert w\rVert$ và giá trị ước lượng trước khi kết luận về hội tụ hay phân kỳ.

**Nguồn:** notebook `thuc-hanh-flappybird-dieu-khien-tuyen-tinh.ipynb`, mục 3–6 và 10 (bảng thử nghiệm khi soạn được nhúng trong notebook); ghi chú bài giảng Bài 07, Nhận xét 07.39, 07.40, Tình huống 07.2. Bài tập 07.18 của ghi chú phân tích cùng cấu hình `four3` theo năm bước.

::: exercise Bài tập 07.25 (Phân biệt phân kỳ với chính sách kém trên Flappy Bird [Lập trình])
Trong notebook Flappy Bird, quan sát $12$ biến được thu về bốn đại lượng dẫn xuất $(\Delta x,\Delta y,v_y,\Delta y_2)$: khoảng cách ngang tới ống kế tiếp, độ lệch dọc của chim so với tâm khe, vận tốc dọc, độ lệch so với khe của ống sau đó. Mỗi đại lượng được chuẩn hóa về $[0,1]$, cho $z(s)\in[0,1]^4$ (mục 4 của notebook). Giá trị hành động là $\hat q(s,a,w)=x(s,a)^\top w$ với mã hóa bốn khối $x(s,a)=(\phi(s);\mathbf 1_a;\phi(s)\otimes\mathbf 1_a;1)$ và hai hành động, nên $d=3k+3$ và $\lVert x(s,a)\rVert^2=2\lVert\phi(s)\rVert^2+2$. Họ `four3` gồm $k=256$ hàm $\cos(\pi c^\top z(s))$. Họ `poly2` gồm hằng $1$, bốn thành phần $z_i$ và mười tích $z_iz_j$ với $i\le j$, tức $k=15$; họ này chưa có trong notebook. Phần thưởng mỗi bước thuộc $[-1,1]$; $\gamma=0{,}99$; bước học $\alpha=\kappa/\mathbb E\lVert x\rVert^2$ với $\kappa=0{,}5$. Bảng thử nghiệm khi soạn ($K=8\,000$ lượt huấn luyện) ghi các số sau. Trên `poly2`, ba hạt giống: $\lVert w\rVert$ lớn nhất $1\,895{,}1$ với Q-learning và $15{,}1$ với Sarsa, cả hai $0$ ống. Trên `four3`, sáu hạt giống: Q-learning $36{,}6$ ống (độ lệch chuẩn giữa các hạt giống $4{,}3$), $\lVert w\rVert$ lớn nhất $8{,}8$; Sarsa $29{,}7$ ống (độ lệch chuẩn $13{,}3$), $\lVert w\rVert$ lớn nhất $6{,}9$. Bảng phạm vi của ghi chú (Nhận xét 07.40) có hai dòng sau. Sarsa bán gradient: $\pi_w$ đổi theo $w$, không có kết quả hội tụ chung. Q-learning bán gradient: đủ bộ ba bất ổn, không có bảo đảm chung, có phản ví dụ phân kỳ.

- (a) Chứng minh $\lvert q_\pi(s,a)\rvert\le100$ với mọi chính sách $\pi$ và $\lvert\hat q(s,a,w)\rvert\le\lVert x(s,a)\rVert\,\lVert w\rVert$. Tính cận trên của $\lVert x(s,a)\rVert$ cho hai họ và ngưỡng của $\lVert w\rVert$ mà dưới đó chắc chắn $\lvert\hat q\rvert\le100$ ở mọi trạng thái; đọc bốn số $\lVert w\rVert$ của bảng thử nghiệm theo ngưỡng đó.
- (b) Trước khi chạy, viết một quy tắc xếp mỗi lần chạy vào một trong ba nhóm: có dấu hiệu phân kỳ; tham số bị chặn trong cửa sổ quan sát và chính sách tốt; tham số bị chặn trong cửa sổ quan sát nhưng chính sách chưa tốt. Quy tắc phải xếp được mọi lần chạy và nêu lý do cho từng ngưỡng; nó dùng $\lVert w_k\rVert$ theo lượt $k$, $\max\lvert\hat q\rvert$ trên các trạng thái tham chiếu `OBS_REF` của notebook và số ống trên `VALID_SEED`.
- (c) Cài `poly2`; huấn luyện Q-learning và Sarsa trên `poly2` và `four3` với ba hạt giống huấn luyện mỗi cấu hình, $K=8\,000$; ghi $\lVert w_k\rVert$ mỗi lượt và $\max\lvert\hat q\rvert$ mỗi $500$ lượt; xếp mười hai lần chạy theo quy tắc ở (b).
- (d) Đối chiếu kết quả với hai dòng của bảng phạm vi nêu trên và nêu điều mà mỗi nhóm cho phép và không cho phép kết luận.
:::

::: hint Gợi ý Bài tập 07.25
Với (a), $\lvert G_t\rvert\le\sum_j\gamma^j$, và mỗi thành phần của $\phi$ có trị tuyệt đối không quá $1$. Với (c), viết `make_poly2` theo mẫu `make_der` của mục 4 và kiểm `phi(obs).shape == (15,)`. Hàm `train_linear` chỉ ghi `score`, `total`, `wnorm`, `steps`; thêm vào vòng lặp lượt một phép tính $\max\lvert\hat q\rvert$ trên `OBS_REF` cứ $500$ lượt một lần. Mục 6 ghi khoảng $58$ giây cho $4\,000$ lượt `four3` khi soạn; mười hai lần chạy $8\,000$ lượt ước khoảng $15$–$30$ phút trên CPU, tùy họ đặc trưng và độ dài lượt, nên đo một lần chạy trước.
:::

::: solution Lời giải Bài tập 07.25
**Câu (a).** Vì $\lvert R_{t+1}\rvert\le1$, $\lvert G_t\rvert\le\sum_{j\ge0}0{,}99^j=100$, nên kỳ vọng $q_\pi(s,a)$ cũng thuộc $[-100,100]$. Theo bất đẳng thức Cauchy–Schwarz, $\lvert x(s,a)^\top w\rvert\le\lVert x(s,a)\rVert\,\lVert w\rVert$. Mọi thành phần của $\phi$ thuộc $[-1,1]$, nên $\lVert\phi\rVert^2\le k$.

| Họ | $k$ | cận $\lVert x\rVert^2$ | cận $\lVert x\rVert$ | ngưỡng $\lVert w\rVert$ |
| --- | --- | --- | --- | --- |
| `poly2` | $15$ | $32$ | $\approx5{,}657$ | $\approx17{,}68$ |
| `four3` | $256$ | $514$ | $\approx22{,}67$ | $\approx4{,}41$ |

Sarsa trên `poly2` có $\lVert w\rVert\le15{,}1<17{,}68$ trong cả ba lần chạy, nên $\lvert\hat q\rvert\le85{,}4$ ở mọi trạng thái: giá trị ước lượng nằm trong miền khả dĩ, và $0$ ống là chính sách kém với tham số bị chặn trong cửa sổ quan sát. Q-learning trên `poly2` có $\lVert w\rVert$ tới $1\,895{,}1$; cận khi đó là $10\,720$, không loại trừ giá trị ước lượng vượt xa $100$, nên phải đo trực tiếp $\max\lvert\hat q\rvert$. Hai số của `four3` vượt ngưỡng $4{,}41$, nhưng cận này thô; lần chạy đã nhúng với $K=4\,000$ cho $\max\lvert\hat q\rvert=14{,}4$ trên `OBS_REF` với Q-learning.

**Câu (b).** Một quy tắc hợp lệ, viết trước khi chạy, xét theo thứ tự:

1. **Có dấu hiệu phân kỳ** khi $\max\lvert\hat q\rvert$ trên `OBS_REF` vượt $100$ ở một mốc nào đó, hoặc $\lVert w_k\rVert$ tăng trên nửa sau của quá trình huấn luyện với $\lVert w_K\rVert\ge2\lVert w_{K/2}\rVert$. Lý do: theo (a), giá trị ngoài $[-100,100]$ không là giá trị của chính sách nào; ngưỡng gấp đôi là một lựa chọn, đủ lớn để không bắt nhầm dao động.
2. **Bị chặn, chính sách tốt** khi không thuộc nhóm 1 và số ống trung bình trên `VALID_SEED` không thấp hơn số ống của luật tay trên cùng các lượt quá $1{,}96$ lần sai số chuẩn (standard error, SE) của hiệu ghép cặp. Lý do: luật tay là mốc tham chiếu của notebook, và so ghép cặp loại phần biến thiên do dãy ống.
3. **Bị chặn, chính sách chưa tốt** trong mọi trường hợp còn lại.

Nhóm 3 là phần bù của hai nhóm đầu, nên mọi lần chạy đều được xếp. Các ngưỡng ngoài ngưỡng $100$ là lựa chọn, cần nêu trước khi xem kết quả.

**Câu (c).** Kết quả phụ thuộc lần chạy; bảng thử nghiệm chỉ cho dự đoán ban đầu. Theo bảng đó, Q-learning trên `poly2` là ứng viên của nhóm 1, Sarsa trên `poly2` là ứng viên của nhóm 3 (câu (a) loại tiêu chí $\max\lvert\hat q\rvert>100$, nhưng bảng không cho biết $\lVert w_K\rVert$ so với $\lVert w_{K/2}\rVert$), còn hai thuật toán trên `four3` là ứng viên của nhóm 2. Độ lệch chuẩn giữa các hạt giống $4{,}3$ và $13{,}3$ ống cho thấy từng hạt giống, nhất là với Sarsa, có thể rơi vào nhóm 3. Báo cáo gồm đồ thị $\lVert w_k\rVert$ theo $k$ (thang log) cho mười hai lần chạy, bảng $\max\lvert\hat q\rvert$ theo mốc, và nhóm của từng lần chạy.

**Câu (d).** Dòng Sarsa: không có kết quả chung, vì $\pi_w$ đổi theo $w$. Dòng Q-learning: đủ bộ ba bất ổn, không có bảo đảm chung, có phản ví dụ. Cả hai cấu hình còn dùng bước hằng (vi phạm Robbins–Monro) và mã hóa bốn khối không đủ hạng cột (Nhận xét 07.9). Vì vậy:

- nhóm 1 phù hợp với bộ ba bất ổn nhưng không chứng minh phân kỳ theo nghĩa giới hạn (Nhận xét 07.39);
- nhóm 2 không chứng minh hội tụ, vì không dòng nào của bảng cho bảo đảm và cửa sổ quan sát hữu hạn;
- nhóm 3 chỉ ra lớp hàm kém hoặc sai lệch do học chưa đủ, không phải bất ổn.

**Kiểm tra lại.** Kiểm `make_poly2` cho $15$ thành phần và $\lVert x(s,a)\rVert^2=2\lVert\phi\rVert^2+2\le32$ trên vài quan sát. Bốn lỗi thường gặp: so $\lVert w\rVert$ giữa hai họ đặc trưng có thang khác nhau; kết luận phân kỳ từ việc qua $0$ ống; kết luận hội tụ từ $\lVert w\rVert$ bị chặn trong $8\,000$ lượt; chọn quy tắc hoặc cấu hình bằng `TEST_SEED`.
:::

## Tài liệu tham khảo

- Tạ Việt Cường (2026). *Bài tập tuần 7 — Function Approximation* (2025–2026): bài 1 cho Bài tập 07.20, bài 3 cho 07.14, bài 4 cho 07.5, bài 5 cho 07.8 (a) và 07.22, bài 7 cho 07.10, bài 8 cho 07.11 và 07.13; bài 2 và bài 6 là Bài tập 07.9 và 07.6 của ghi chú bài giảng; phần C cho chuỗi năm trạng thái.
- Tạ Việt Cường (2026). *Lecture 07: Hàm xấp xỉ trong Reinforcement Learning*, bài giảng gốc (2025–2026), trang 22–45: chuỗi năm trạng thái (trang 40), điều kiện hội tụ của Monte Carlo (trang 34), bộ ba bất ổn (trang 37, 41).
- Sutton, R. S. và Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2: §9.3–9.4 cho Bài tập 07.5, 07.7, 07.8, 07.22; §9.6 cho bước học chuẩn hóa ở Bài tập 07.24; §11.2 (tr. 260, 263) và §11.3 cho Bài tập 07.14, 07.23.
- Bertsekas, D. P. và Tsitsiklis, J. N. (1996). *Neuro-Dynamic Programming*, chương 4: kết quả gradient ngẫu nhiên dùng trong Bài tập 07.21, 07.24.
- Borkar, V. S. và Meyn, S. P. (2000). The O.D.E. method for convergence of stochastic approximation and reinforcement learning. *SIAM Journal on Control and Optimization* 38(2): nhận xét về điều kiện trị riêng ở Bài tập 07.24.
- Ghi chú bài giảng Bài 07 và hai notebook thực hành Bài 07 (Lunar Lander, Flappy Bird): nguồn của mọi số liệu thực hành trong Bài tập 07.20–07.25.
