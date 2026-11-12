# Bài tập Bài 08 — Deep Q-Learning

Tệp gồm hai bài mức tính toán hoặc chứng minh, Bài tập 08.8 và 08.9, lấy từ Sutton và Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2; số trang là trang in của sách. Số hiệu nối tiếp Bài tập 08.1–08.7 ở mục "Bài tập củng cố" của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-deep-q-learning.html) Bài 08; bảy bài đó có gợi ý và lời giải trong ghi chú và không chép lại ở đây. Bài tập mức nhận biết là bốn câu hỏi của mục "Câu hỏi tự kiểm tra" trong ghi chú; bài tập vận dụng là Bài tập 08.2–08.4 của ghi chú. Bốn bài 08.1–08.4 còn có trang đề bài và trang lời giải trên trang chiếu, và bảng dưới dẫn tới các trang đó; hai bài của tệp này không trùng trang chiếu nào. Lời giải dẫn định nghĩa và mệnh đề theo số hiệu của ghi chú.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-08-deep-q-learning.html#/1/1) | — |
| 2. Mạng giá trị hành động và mục tiêu hồi quy | [Mở phần](lecture-08-deep-q-learning.html#/2/1) | ghi chú: 08.1, 08.4 |
| 3. Bộ nhớ phát lại | [Mở phần](lecture-08-deep-q-learning.html#/3/1) | 08.9; ghi chú: 08.6 |
| 4. Hàm mất mát và thuật toán DQN | [Mở phần](lecture-08-deep-q-learning.html#/4/1) | ghi chú: 08.1, 08.2, 08.4, 08.7; trang [Bài tập: một mini-batch](lecture-08-deep-q-learning.html#/4/5) và [trang lời giải](lecture-08-deep-q-learning.html#/4/6); trang [Bài tập: lỗi cài đặt mục tiêu DQN](lecture-08-deep-q-learning.html#/4/13) và [trang lời giải](lecture-08-deep-q-learning.html#/4/14) |
| 5. Bộ tối ưu theo gradient | [Mở phần](lecture-08-deep-q-learning.html#/5/1) | 08.8; ghi chú: 08.5 (a) |
| 6. Bất ổn và phạm vi bảo đảm của DQN | [Mở phần](lecture-08-deep-q-learning.html#/6/1) | ghi chú: 08.3, 08.5 (b); trang [Bài tập: thí nghiệm loại bỏ](lecture-08-deep-q-learning.html#/6/6) và [trang lời giải](lecture-08-deep-q-learning.html#/6/7) |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-08-deep-q-learning.html#/7/1) | ghi chú: 08.4; trang [Bài tập: một bước DQN trên CartPole](lecture-08-deep-q-learning.html#/7/6) và [trang lời giải](lecture-08-deep-q-learning.html#/7/7) |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 08; số thập phân viết bằng dấu phẩy. Hai bài giữ ký hiệu của Sutton và Barto ở các chỗ sau.

- Bài tập 08.8 xét bài toán máy đánh bạc nhiều tay (multi-armed bandit) của Sutton và Barto, Chương 2: $R_n$ là phần thưởng thứ $n$ nhận được khi chọn một hành động cố định, $Q_n$ là ước lượng giá trị của hành động đó trước khi xử lý $R_n$, $\alpha$ là bước học hằng. Hệ số $\beta_n$ trong (2.8) là một bước học, khác hai hệ số suy giảm $\beta_1$, $\beta_2$ của Adam (Định nghĩa 08.18).
- Bài tập 08.9 xét bài toán dự đoán theo lượt: $S_t$, $A_t$, $R_{t+1}$ là trạng thái, hành động, phần thưởng; $T$ là bước cuối của lượt; $\pi$ là chính sách đích và $\mu$ là chính sách hành vi sinh dữ liệu (Sutton và Barto viết $b$; ghi chú Bài 08 dùng $b$ cho cỡ mini-batch). Tỉ số lấy mẫu quan trọng (importance sampling ratio) viết $\rho_{t:h}$ theo (7.10); $\rho_{t:t}$ là tỉ số $\rho_t$ của Bài 06–07, khác hệ số suy giảm $\rho$ của RMSprop. Hàm giá trị xấp xỉ $\hat v(s,w)$ khả vi theo vector trọng số $w\in\mathbb R^d$, với $\hat v(\text{kết thúc},\cdot)=0$; $w$ đóng vai của $\theta$ trong ghi chú.

## Mức tính toán hoặc chứng minh

### Bài tập 08.8. Bước học hằng không có độ lệch khởi tạo

**Mức độ:** chứng minh. Mục tiêu học tập 4 của ghi chú (RMSprop và Adam theo từng tọa độ): trung bình trượt có trọng số mũ và phép hiệu chỉnh lệch của Adam.

**Nguồn:** Sutton và Barto (2018), Bài tập 2.7, §2.6, tr. 35; công thức (2.5), (2.6) ở §2.5, tr. 32.

::: exercise Bài tập 08.8 (Bước học hằng không có độ lệch khởi tạo)
Xét một hành động cố định của bài toán máy đánh bạc nhiều tay. Gọi $R_1,R_2,\dots$ là các phần thưởng lần lượt nhận được khi chọn hành động này, $Q_1$ là ước lượng ban đầu và $Q_{n+1}$ là ước lượng sau khi xử lý $R_n$. Với bước học hằng $\alpha\in(0,1]$, cập nhật (2.5)
$$
Q_{n+1}=Q_n+\alpha\bigl[R_n-Q_n\bigr]
$$
cho công thức (2.6)
$$
\begin{aligned}
Q_{n+1}&=(1-\alpha)^nQ_1\\
&\quad+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}R_i,
\end{aligned}
$$
nên khi $\alpha<1$, $Q_{n+1}$ phụ thuộc giá trị khởi tạo $Q_1$: bước học hằng có độ lệch khởi tạo (initial bias). Trung bình mẫu không có độ lệch này nhưng có thể cho kết quả kém trên bài toán không dừng. Để tránh độ lệch của bước học hằng mà vẫn giữ ưu điểm của nó trên bài toán không dừng, ta xử lý phần thưởng thứ $n$ bằng cập nhật $Q_{n+1}=Q_n+\beta_n\bigl[R_n-Q_n\bigr]$ với bước học (2.8)
$$
\beta_n=\frac{\alpha}{\bar o_n},
$$
trong đó $\bar o_n$ là một vết của số $1$ (trace of one) xuất phát từ $\bar o_0=0$ và thỏa (2.9) với mọi $n>0$:
$$
\bar o_n=\bar o_{n-1}+\alpha\bigl(1-\bar o_{n-1}\bigr).
$$

- (a) Tìm dạng đóng của $\bar o_n$ và chứng tỏ $\beta_n$ xác định với mọi $n\ge1$.
- (b) Làm phép phân tích như phép dẫn tới (2.6) để chứng minh $Q_{n+1}$ là một trung bình có trọng số giảm theo hàm mũ của độ cũ (exponential recency-weighted average) của $R_1,\dots,R_n$, không có độ lệch khởi tạo.
:::

::: hint Gợi ý Bài tập 08.8
Với (a), viết phương trình (2.9) cho đại lượng $1-\bar o_n$. Với (b), tính $\beta_1$ trước, rồi biểu diễn $1-\beta_k$ qua $\bar o_{k-1}$ và $\bar o_k$; tích các thừa số $1-\beta_k$ sẽ rút gọn liên tiếp.
:::

::: solution Lời giải Bài tập 08.8
**Câu (a).** Lấy $1$ trừ hai vế của (2.9) rồi đặt thừa số chung $1-\bar o_{n-1}$:
$$
1-\bar o_n=(1-\alpha)\bigl(1-\bar o_{n-1}\bigr).
$$
Vì $1-\bar o_0=1$, quy nạp cho $1-\bar o_n=(1-\alpha)^n$, tức
$$
\bar o_n=1-(1-\alpha)^n .
$$
Với $\alpha\in(0,1]$, $0\le1-\alpha<1$, nên $\alpha\le\bar o_n\le1$ với mọi $n\ge1$; mẫu số của (2.8) dương và $\beta_n$ xác định. Khi $n\to\infty$, $\bar o_n\to1$ nếu $\alpha<1$, và $\bar o_n=1$ với mọi $n$ nếu $\alpha=1$; trong cả hai trường hợp, $\beta_n\to\alpha$.

**Câu (b).** *Bước học đầu tiên.* $\bar o_1=\alpha$, nên $\beta_1=\alpha/\alpha=1$ và $Q_2=Q_1+1\cdot(R_1-Q_1)=R_1$: giá trị $Q_1$ bị xóa ngay ở lần cập nhật đầu.

*Thừa số $1-\beta_k$.* Theo (2.9), $\bar o_k-\alpha=\bar o_{k-1}+\alpha(1-\bar o_{k-1})-\alpha=(1-\alpha)\,\bar o_{k-1}$, nên
$$
\begin{aligned}
1-\beta_k&=\frac{\bar o_k-\alpha}{\bar o_k}\\
&=(1-\alpha)\,\frac{\bar o_{k-1}}{\bar o_k}.
\end{aligned}
$$

*Khai triển.* Viết cập nhật thành $Q_{k+1}=(1-\beta_k)Q_k+\beta_kR_k$ và đặt $P_i=\prod_{k=i+1}^n(1-\beta_k)$ với $0\le i\le n$, quy ước $P_n=1$. Thế liên tiếp như phép dẫn tới (2.6) cho
$$
Q_{n+1}=P_0Q_1+\sum_{i=1}^n\beta_iP_iR_i .
$$
Theo thừa số vừa tính, tích rút gọn liên tiếp, nên với $0\le i\le n$,
$$
P_i=(1-\alpha)^{n-i}\,\frac{\bar o_i}{\bar o_n}.
$$
Với $i=0$, $P_0=(1-\alpha)^n\bar o_0/\bar o_n=0$, nên hệ số của $Q_1$ bằng $0$. Với $1\le i\le n$, trọng số của $R_i$ là
$$
\begin{aligned}
\beta_iP_i&=\frac{\alpha}{\bar o_i}(1-\alpha)^{n-i}\,\frac{\bar o_i}{\bar o_n}\\
&=\frac{\alpha(1-\alpha)^{n-i}}{1-(1-\alpha)^n}.
\end{aligned}
$$

*Kết luận.* Các trọng số không âm (dương khi $\alpha<1$), trọng số của $R_i$ bằng $1-\alpha$ nhân trọng số của $R_{i+1}$, tức giảm theo hàm mũ của độ cũ $n-i$ như trong (2.6), và vì $\alpha\sum_{j=0}^{n-1}(1-\alpha)^j=1-(1-\alpha)^n$, tổng của chúng là
$$
\begin{aligned}
\sum_{i=1}^n\beta_iP_i&=\frac{\alpha\sum_{j=0}^{n-1}(1-\alpha)^j}{1-(1-\alpha)^n}\\
&=1 .
\end{aligned}
$$
Vậy
$$
Q_{n+1}=\sum_{i=1}^n\frac{\alpha(1-\alpha)^{n-i}}{1-(1-\alpha)^n}\,R_i
$$
là một trung bình có trọng số mũ của $R_1,\dots,R_n$ và không phụ thuộc $Q_1$. So với (2.6), các trọng số của $R_i$ trong (2.6) có tổng $1-(1-\alpha)^n$, phần còn lại $(1-\alpha)^n$ thuộc về $Q_1$; phép chia cho $\bar o_n$ chuẩn hóa lại tổng đó về $1$. Khi $n$ lớn, $\bar o_n\to1$ và các trọng số tiến tới các trọng số của (2.6), nên cách cập nhật này giữ khả năng bám theo bài toán không dừng của bước học hằng.

*Liên hệ với Adam.* Xét Adam có hệ số suy giảm thứ nhất bằng $1-\alpha$ (Định nghĩa 08.18 viết hệ số này là $\beta_1$) và thay $R_\ell$ bằng một tọa độ $g_\ell$ của gradient. Với $Q_1=0$, (2.6) cho $Q_{n+1}=\alpha\sum_{\ell=1}^n(1-\alpha)^{n-\ell}g_\ell$, đúng là $m_n$ của Adam với $m_0=0$, và $\bar o_n=1-(1-\alpha)^n$ là mẫu số của $\hat m_n$. Cách cập nhật của bài cho $Q_{n+1}=\hat m_n$: phép hiệu chỉnh lệch của Adam chính là phép chia cho vết $\bar o_n$.

**Kiểm tra lại.** Với $\alpha=0{,}5$: $\bar o_1=0{,}5$, $\beta_1=1$, $Q_2=R_1$; $\bar o_2=0{,}75$, $\beta_2=2/3$, nên $Q_3=R_1+\tfrac23(R_2-R_1)=\tfrac13R_1+\tfrac23R_2$, khớp công thức trọng số $\alpha(1-\alpha)^{n-i}/(1-(1-\alpha)^n)$ với $n=2$: $\tfrac{0{,}25}{0{,}75}=\tfrac13$ và $\tfrac{0{,}5}{0{,}75}=\tfrac23$. Ba lỗi thường gặp: viết $\bar o_n=n\alpha$, bỏ thừa số $1-\bar o_{n-1}$ trong (2.9); quên rằng $\beta_1=1$ và giữ lại một hệ số khác $0$ của $Q_1$; kết luận các trọng số bằng nhau như trung bình mẫu, trong khi tỉ số hai trọng số liền nhau là $1-\alpha$.
:::

### Bài tập 08.9. TD $n$ bước khác chính sách ở dạng bán gradient

**Mức độ:** tính toán. Mục tiêu học tập 2 và 3 của ghi chú: mục tiêu nhiều bước trên dữ liệu khác chính sách cần tỉ số lấy mẫu quan trọng; mục tiêu bootstrap được giữ là hằng khi lấy gradient.

**Nguồn:** Sutton và Barto (2018), Bài tập 11.1, §11.1, tr. 259; công thức (7.1) ở §7.1, tr. 143; (7.9), (7.10) ở §7.3, tr. 148; (9.15), (9.16) ở §9.4, tr. 209; (11.1)–(11.3) ở §11.1, tr. 258.

::: exercise Bài tập 08.9 (TD $n$ bước khác chính sách ở dạng bán gradient)
Xét bài toán dự đoán theo lượt: dữ liệu do chính sách hành vi $\mu$ sinh ra, cần ước lượng $v_\pi$ của chính sách đích $\pi$; $T$ là bước cuối của lượt và $n\ge1$ là số bước. Dạng bảng của TD $n$ bước khác chính sách (off-policy $n$-step TD) là cập nhật (7.9), với $0\le t<T$:
$$
\begin{aligned}
V_{t+n}(S_t)&=V_{t+n-1}(S_t)\\
&\quad+\alpha\,\rho_{t:t+n-1}\\
&\qquad\times\bigl[G_{t:t+n}\\
&\qquad\quad-V_{t+n-1}(S_t)\bigr].
\end{aligned}
$$
Trong đó $\rho_{t:h}$ là tỉ số lấy mẫu quan trọng (7.10)
$$
\rho_{t:h}=\prod_{k=t}^{\min(h,T-1)}\frac{\pi(A_k\mid S_k)}{\mu(A_k\mid S_k)},
$$
và $G_{t:t+n}$ là lợi tức $n$ bước (7.1): khi $t+n<T$,
$$
\begin{aligned}
G_{t:t+n}&=R_{t+1}+\gamma R_{t+2}+\dots\\
&\quad+\gamma^{n-1}R_{t+n}\\
&\quad+\gamma^nV_{t+n-1}(S_{t+n}),
\end{aligned}
$$
còn $G_{t:t+n}=G_t$ khi $t+n\ge T$. Với hàm giá trị xấp xỉ $\hat v(s,w)$ khả vi theo $w\in\mathbb R^d$, $\hat v(\text{kết thúc},\cdot)=0$, dạng bán gradient theo chính sách của TD $n$ bước là cập nhật (9.15), với $0\le t<T$:
$$
\begin{aligned}
w_{t+n}&=w_{t+n-1}\\
&\quad+\alpha\bigl[G_{t:t+n}\\
&\qquad\quad-\hat v(S_t,w_{t+n-1})\bigr]\\
&\qquad\times\nabla\hat v(S_t,w_{t+n-1}),
\end{aligned}
$$
trong đó $V_{t+n-1}(S_{t+n})$ ở (7.1) được thay bằng $\hat v(S_{t+n},w_{t+n-1})$ (9.16). Dạng bán gradient khác chính sách của TD một bước là cập nhật (11.2)
$$
w_{t+1}=w_t+\alpha\,\rho_t\,\delta_t\,\nabla\hat v(S_t,w_t),
$$
với $\rho_t=\rho_{t:t}=\pi(A_t\mid S_t)/\mu(A_t\mid S_t)$ (11.1) và sai số TD (11.3)
$$
\begin{aligned}
\delta_t&=R_{t+1}+\gamma\hat v(S_{t+1},w_t)\\
&\quad-\hat v(S_t,w_t).
\end{aligned}
$$

- (a) Đưa (7.9) về dạng bán gradient, kèm định nghĩa lợi tức $n$ bước dùng trong cập nhật.
- (b) Chứng tỏ với $n=1$, cập nhật ở (a) trùng (11.2)–(11.3), kể cả ở bước cuối $t=T-1$.
:::

::: hint Gợi ý Bài tập 08.9
Làm như phép chuyển từ TD $n$ bước dạng bảng sang (9.15): thay cập nhật một ô của mảng $V$ bằng cập nhật vector $w$ theo hướng $\nabla\hat v(S_t,\cdot)$, thay mọi giá trị $V_{t+n-1}(\cdot)$ bằng $\hat v(\cdot,w_{t+n-1})$, và giữ nguyên hệ số $\rho_{t:t+n-1}$ của (7.9).
:::

::: solution Lời giải Bài tập 08.9
**Câu (a).** Cập nhật bán gradient của TD $n$ bước khác chính sách là, với $0\le t<T$,
$$
\begin{aligned}
w_{t+n}&=w_{t+n-1}\\
&\quad+\alpha\,\rho_{t:t+n-1}\bigl[G_{t:t+n}\\
&\qquad\quad-\hat v(S_t,w_{t+n-1})\bigr]\\
&\qquad\times\nabla\hat v(S_t,w_{t+n-1}),
\end{aligned}
$$
với $\rho_{t:t+n-1}=\prod_{k=t}^{\min(t+n-1,T-1)}\pi(A_k\mid S_k)/\mu(A_k\mid S_k)$ theo (7.10). Lợi tức $n$ bước là
$$
\begin{aligned}
G_{t:t+n}&=\sum_{k=1}^{n}\gamma^{k-1}R_{t+k}\\
&\quad+\gamma^n\hat v(S_{t+n},w_{t+n-1})
\end{aligned}
$$
khi $t+n<T$, và $G_{t:t+n}=G_t=\sum_{k=t+1}^{T}\gamma^{k-t-1}R_k$ khi $t+n\ge T$.
Căn cứ của từng thay đổi:

- Cập nhật của (7.9) chỉ đổi ô $V(S_t)$; ở dạng xấp xỉ, ô đó là $\hat v(S_t,w)$, và cập nhật đi theo hướng $\nabla\hat v(S_t,w_{t+n-1})$ như (9.15).
- Giá trị bootstrap $V_{t+n-1}(S_{t+n})$ trở thành $\hat v(S_{t+n},w_{t+n-1})$, như (9.16). $G_{t:t+n}$ phụ thuộc $w_{t+n-1}$ qua số hạng này, nhưng được giữ là hằng khi lấy gradient; đó là nghĩa của chữ "bán gradient", cùng quy ước với phép dừng gradient của Định nghĩa 08.12.
- Hệ số $\rho_{t:t+n-1}$ giữ nguyên. Nó gồm các thừa số của $A_t,\dots,A_{t+n-1}$, vì giá trị trạng thái $v_\pi(S_t)$ lấy kỳ vọng theo cả hành động $A_t$, và mọi hành động đó do $\mu$ chọn. Khi $t+n>T$, tích dừng ở $k=T-1$.

**Câu (b).** Với $n=1$, $\rho_{t:t}=\pi(A_t\mid S_t)/\mu(A_t\mid S_t)=\rho_t$ theo (11.1). Khi $t+1<T$, $G_{t:t+1}=R_{t+1}+\gamma\hat v(S_{t+1},w_t)$. Khi $t=T-1$, $G_{t:t+1}=G_{T-1}=R_T$; vì $S_T$ là trạng thái kết thúc và $\hat v(\text{kết thúc},\cdot)=0$, ta cũng có $R_T=R_T+\gamma\hat v(S_T,w_{T-1})$. Trong cả hai trường hợp, $G_{t:t+1}-\hat v(S_t,w_t)=\delta_t$ của (11.3), nên
$$
w_{t+1}=w_t+\alpha\,\rho_t\,\delta_t\,\nabla\hat v(S_t,w_t),
$$
đúng là (11.2).

Ở Bài 08, mục tiêu một bước của DQN viết cho giá trị hành động. Khi đó $A_t$ là đối số điều kiện của $Q(S_t,A_t)$, nên mục tiêu một bước không cần tỉ số nào (Mệnh đề 08.8), và ở dạng $n$ bước, tích tỉ số của Sutton và Barto, (11.6), tr. 259, bắt đầu từ $t+1$ thay cho $t$.

**Kiểm tra lại.** Khi $\pi=\mu$, mọi tỉ số bằng $1$ và cập nhật ở (a) trở về (9.15)–(9.16). Ba lỗi thường gặp: bắt đầu tích tỉ số từ $k=t+1$, là chỉ số của dạng giá trị hành động, nên bỏ mất thừa số của $A_t$; lấy gradient qua cả $\hat v(S_{t+n},w_{t+n-1})$ trong $G_{t:t+n}$, khi đó cập nhật không còn là bán gradient; dùng $w_t$ thay cho $w_{t+n-1}$ trong cập nhật thực hiện ở thời điểm $t+n$.
:::

## Tài liệu tham khảo

- Sutton, R. S. và Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: Bài tập 2.7, §2.6, tr. 35, cùng (2.5), (2.6), §2.5, tr. 32 (Bài tập 08.8); Bài tập 11.1, §11.1, tr. 259, cùng (7.1), tr. 143, (7.9), (7.10), tr. 148, (9.15), (9.16), tr. 209, (11.1)–(11.3), tr. 258, (11.6), tr. 259 (Bài tập 08.9).
- Kingma, D. P. và Ba, J. (2015). Adam: A Method for Stochastic Optimization. *ICLR*: phép hiệu chỉnh lệch dùng trong lời giải Bài tập 08.8.
- Ghi chú bài giảng Bài 08: Bài tập 08.1–08.7, Định nghĩa 08.12, 08.18, Mệnh đề 08.8.
