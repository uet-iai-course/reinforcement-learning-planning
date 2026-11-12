# Bài tập Bài 09 — Double DQN và gradient chính sách

Bộ bài tập gồm sáu bài, Bài tập 09.12–09.17, lấy từ Bài tập 6.13, 13.1, 13.2, 13.3 và 13.5 của Sutton và Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, xếp theo ba mức: nhận biết (09.12, 09.13); tính toán hoặc chứng minh (09.14, 09.15); vận dụng vào bài toán Học tăng cường (09.16, 09.17). Bài tập 13.1 của sách được tách thành hai bài, 09.13 và 09.16. Mười một bài 09.1–09.11 thuộc mục "Bài tập củng cố" của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html) Bài 09, có gợi ý và lời giải tại đó; bảng dưới ghi chúng ở dạng "ghi chú: 09.k". Sáu bài của tệp này nối tiếp bộ đếm Bài tập của ghi chú và không trùng bài tập trên trang chiếu; bảng dưới dẫn thêm tới các trang bài tập trên trang chiếu, vốn trùng các bài củng cố 09.5, 09.8, 09.10 và 09.11.

Đề bài được phát biểu lại theo ký hiệu của ghi chú Bài 09, với dữ kiện chép lại trong khối đề bài.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/1/1) | — |
| 2. Độ chệch của phép cực đại | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/2/1) | [ghi chú: 09.1, 09.2](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html) |
| 3. Tách chọn và đánh giá | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/3/1) | 09.12; [ghi chú: 09.3, 09.11](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: mục tiêu DQN và Double DQN](lecture-09-double-dqn-va-gradient-chinh-sach.html#/3/7), trùng 09.11, lời giải trên cùng trang |
| 4. Chính sách tham số hóa | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/4/1) | 09.13, 09.16; [ghi chú: 09.4](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html) |
| 5. Hàm mục tiêu và hàm điểm | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/5/1) | 09.14, 09.16, 09.17; [ghi chú: 09.5, 09.6, 09.7](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: hàm điểm softmax và Gaussian](lecture-09-double-dqn-va-gradient-chinh-sach.html#/5/12), trùng 09.5 |
| 6. Gradient chính sách và REINFORCE | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/6/1) | 09.15, 09.17; [ghi chú: 09.8, 09.9](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: cập nhật REINFORCE](lecture-09-double-dqn-va-gradient-chinh-sach.html#/6/13) và [trang lời giải](lecture-09-double-dqn-va-gradient-chinh-sach.html#/6/14), trùng 09.8 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/7/1) | [ghi chú: 09.10](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: tổng hợp trên bài toán một bước](lecture-09-double-dqn-va-gradient-chinh-sach.html#/7/6) và [trang lời giải](lecture-09-double-dqn-va-gradient-chinh-sach.html#/7/7), trùng 09.10 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 09. Thời gian rời rạc $t=0,1,\dots$; phần thưởng $R_{t+1}$ nhận sau hành động $A_t$ tại trạng thái $S_t$; lượt kết thúc tại bước $T$; lợi tức từ bước $t$ là $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$. Giá trị hành động của chính sách $\pi$ là $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$, giá trị trạng thái là $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$, và giá trị tại trạng thái kết thúc bằng $0$. Chính sách tham số hóa $\pi_\theta$, $\theta\in\mathbb R^d$ (Định nghĩa 09.10); hàm mục tiêu $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ (Định nghĩa 09.14); hàm điểm (score function) $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$ (Định nghĩa 09.15), viết tắt $\psi_t=\psi_\theta(S_t,A_t)$; Sutton và Barto gọi $\nabla\ln\pi$ là vector đủ điều kiện (eligibility vector) và viết đặc trưng là $\mathbf x$, ghi chú viết $\phi$. Chính sách softmax với đặc trưng $\phi(s,a)\in\mathbb R^d$ là $\pi_\theta(a\mid s)=\exp\bigl(\phi(s,a)^\top\theta\bigr)/\sum_b\exp\bigl(\phi(s,b)^\top\theta\bigr)$ (Định nghĩa 09.11). REINFORCE (Thuật toán 09.25) cập nhật một lần mỗi lượt, $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\sum_t\gamma^tG_t\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$, với bước học $\alpha>0$. Số thập phân viết với dấu phẩy; vector viết $(x_1;\,x_2)$.

Chính sách $\epsilon$-tham lam theo một bảng $Q$ chọn đều một hành động với xác suất $\epsilon$, ngược lại chọn hành động có $Q$ lớn nhất. Với $\lvert\mathcal A\rvert$ hành động và một hành động tham lam duy nhất, hành động tham lam có xác suất $1-\epsilon+\epsilon/\lvert\mathcal A\rvert$, mỗi hành động khác có xác suất $\epsilon/\lvert\mathcal A\rvert$.

**Hành lang ngắn đảo hành động** (Sutton và Barto, 2018, Ví dụ 13.1, tr. 323), dùng ở Bài tập 09.13, 09.14 và 09.16. Bốn ô trên một hàng: $s_1$ (ô xuất phát), $s_2$, $s_3$ và ô đích $s_4$, nơi lượt kết thúc. Mỗi bước nhận phần thưởng $-1$; $\gamma=1$. Hai hành động: hành động 1 là "sang phải", hành động 2 là "sang trái". Ở $s_1$ và $s_3$ hành động có tác dụng thông thường: sang trái tại $s_1$ thì đứng yên, sang phải tại $s_3$ thì tới $s_4$. Ở $s_2$ hai hành động bị đảo: hành động 1 đưa về $s_1$, hành động 2 đưa tới $s_3$. Mọi ô có cùng đặc trưng: $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ với mọi $s$.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

Hình đọc từ trái sang phải; trong mỗi ô, dòng "1 →" và "2 →" ghi ô kế tiếp của hành động 1 và 2. Ô $s_2$ có viền nét đứt và nhãn "đảo hành động": ở đó hành động 1 đưa về bên trái.

**Chiết khấu trên hành lang ngắn.** Ghi chú dùng $0\le\gamma<1$; hành lang ngắn dùng $\gamma=1$. Khi chính sách chọn hành động 1 với cùng xác suất $p\in(0,1)$ ở mọi ô, từ mọi ô có một dãy tối đa ba bước tới đích với xác suất ít nhất $c=p^2(1-p)>0$ (từ $s_1$: hành động 1, 2, 1). Do đó $\Pr(T>3n)\le(1-c)^n$, lượt kết thúc hầu chắc chắn và $\mathbb E[T]<\infty$. Mỗi bước nhận $-1$, nên $J=v_\pi(s_1)=-\mathbb E[T]$, và các giá trị $v_\pi(s_i)$ thỏa phương trình Bellman một bước với $\gamma=1$.

## Mức nhận biết

### Bài tập 09.12. Double Expected Sarsa

**Mức độ:** nhận biết. Mục tiêu học tập 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.13, §6.7, tr. 136.

::: exercise Bài tập 09.12 (Double Expected Sarsa)
Expected Sarsa (còn gọi là Sarsa kỳ vọng) với chính sách mục tiêu $\pi$ cập nhật
$$
\begin{aligned}
Q(S,A)&\leftarrow Q(S,A)\\
&\quad+\alpha\bigl[y-Q(S,A)\bigr],
\end{aligned}
$$
với
$$
\begin{aligned}
y&=R+\gamma(1-Z)\\
&\quad\cdot\sum_a\pi(a\mid S')\,Q(S',a)
\end{aligned}
$$
trên mẫu chuyển $(S,A,R,S',Z)$, với $Z=1$ khi $S'$ là trạng thái kết thúc. Double Q-learning (Thuật toán 09.7) giữ hai bảng $Q_1$, $Q_2$; mỗi bước tung đồng xu để chọn bảng được cập nhật; bảng được cập nhật chọn hành động $a^*=\arg\max_aQ_1(S',a)$ (khi cập nhật $Q_1$), bảng kia đánh giá $Q_2(S',a^*)$.

- (a) Viết hai phương trình cập nhật của Double Expected Sarsa với chính sách mục tiêu $\epsilon$-tham lam: một khi cập nhật $Q_1$, một khi cập nhật $Q_2$. Nêu chính sách mục tiêu được xây từ bảng nào và kỳ vọng lấy theo giá trị của bảng nào.
- (b) Chứng tỏ rằng khi $\epsilon=0$ và hành động tham lam duy nhất, hai phương trình ở (a) trở thành Double Q-learning.
:::

::: hint Gợi ý Bài tập 09.12
Trong Double Q-learning, $\arg\max_aQ_1(S',a)$ là bước chọn và $Q_2(S',\cdot)$ là bước đánh giá. Trong Expected Sarsa, bước chọn là chính sách mục tiêu; chính sách này xây từ bảng được cập nhật, còn giá trị lấy từ bảng kia.
:::

::: solution Lời giải Bài tập 09.12
**Câu (a).** Gọi $\pi_1$, $\pi_2$ là các chính sách $\epsilon$-tham lam theo $Q_1$, $Q_2$. Khi đồng xu chọn $Q_1$:
$$
\begin{aligned}
e_1&=\sum_a\pi_1(a\mid S')\,Q_2(S',a),\\
y_1&=R+\gamma(1-Z)\,e_1,
\end{aligned}
$$
$$
\begin{aligned}
&Q_1(S,A)\leftarrow Q_1(S,A)\\
&\quad+\alpha\bigl[y_1-Q_1(S,A)\bigr].
\end{aligned}
$$
Khi đồng xu chọn $Q_2$, đổi vai hai bảng:
$$
\begin{aligned}
e_2&=\sum_a\pi_2(a\mid S')\,Q_1(S',a),\\
y_2&=R+\gamma(1-Z)\,e_2,
\end{aligned}
$$
$$
\begin{aligned}
&Q_2(S,A)\leftarrow Q_2(S,A)\\
&\quad+\alpha\bigl[y_2-Q_2(S,A)\bigr].
\end{aligned}
$$
Chính sách mục tiêu xây từ bảng được cập nhật (bước chọn); kỳ vọng lấy theo giá trị của bảng kia (bước đánh giá). Với $a^*_1=\arg\max_aQ_1(S',a)$ duy nhất, $e_1$ viết tường minh là
$$
\begin{aligned}
e_1&=(1-\epsilon)\,Q_2(S',a^*_1)\\
&\quad+\frac{\epsilon}{\lvert\mathcal A\rvert}\sum_aQ_2(S',a).
\end{aligned}
$$
Hành vi có thể là $\epsilon$-tham lam theo $Q_1+Q_2$, như Double Q-learning; hành vi không đi vào mục tiêu.

**Câu (b).** Với $\epsilon=0$, $\pi_1(a\mid S')=\mathbf 1\{a=a^*_1\}$, nên $\sum_a\pi_1(a\mid S')Q_2(S',a)=Q_2(S',a^*_1)$ và $y_1=R+\gamma(1-Z)Q_2\bigl(S',\arg\max_aQ_1(S',a)\bigr)$: đúng mục tiêu của Double Q-learning khi cập nhật $Q_1$ (Thuật toán 09.7, bước 2). Trường hợp cập nhật $Q_2$ có cùng lập luận khi đổi chỉ số $1$ và $2$.

**Kiểm tra lại.** Công thức tường minh ở (a) với $\epsilon=0$ cho lại (b). Hai lỗi thường gặp. Thứ nhất, xây $\pi_1$ từ $Q_2$: mục tiêu thành $\sum_a\pi_2(a\mid S')Q_2(S',a)$, tức Expected Sarsa một bảng trên $Q_2$, và một bảng vừa chọn vừa đánh giá. Thứ hai, dùng chính sách theo $Q_1+Q_2$ trong mục tiêu: bước chọn khi đó phụ thuộc cả bảng đánh giá, nên lập luận của Mệnh đề 09.4 không áp dụng.
:::

### Bài tập 09.13. Hành lang ngắn và chính sách tất định

**Mức độ:** nhận biết. Mục tiêu học tập 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 13.1, §13.1, tr. 324, phần thứ nhất; dữ kiện ở Ví dụ 13.1, tr. 323.

::: exercise Bài tập 09.13 (Hành lang ngắn và chính sách tất định)
Hành lang ngắn đảo hành động: bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 là "sang phải", hành động 2 là "sang trái". Ở $s_1$, $s_3$ hành động có tác dụng thông thường (sang trái tại $s_1$ thì đứng yên, sang phải tại $s_3$ thì tới $s_4$); ở $s_2$ hai hành động bị đảo: hành động 1 đưa về $s_1$, hành động 2 đưa tới $s_3$. Đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ với mọi $s$.

- (a) Chứng tỏ rằng mọi chính sách softmax với các đặc trưng này chọn hành động 1 với cùng một xác suất $p$ ở cả ba ô không kết thúc, và viết $p$ theo $\theta$.
- (b) Mô tả lượt sinh bởi chính sách tất định $p=1$ và bởi $p=0$. Lượt có kết thúc không? Tổng phần thưởng của $n$ bước đầu bằng bao nhiêu?
- (c) Một phương pháp giá trị hành động với $Q(s,a)=\phi(s,a)^\top w$ và hành vi $\epsilon$-tham lam, $\epsilon=0{,}1$, đạt được những giá trị $p$ nào khi có một hành động tham lam duy nhất? Chính sách softmax đạt được những giá trị $p$ nào?
:::

::: hint Gợi ý Bài tập 09.13
Viết $\pi_\theta(1\mid s)$ theo Định nghĩa 09.11: tử số và mẫu số không chứa $s$. Ở (b), lần theo ba bước đầu của lượt từ $s_1$.
:::

::: solution Lời giải Bài tập 09.13
**Câu (a).** Theo Định nghĩa 09.11,
$$
\begin{aligned}
\pi_\theta(1\mid s)&=\frac{e^{\theta_1}}{e^{\theta_1}+e^{\theta_2}}\\
&=\frac1{1+e^{-(\theta_1-\theta_2)}}.
\end{aligned}
$$
Biểu thức không chứa $s$ vì $\phi(s,a)$ không phụ thuộc $s$; do đó $p=\pi_\theta(1\mid s)$ như nhau ở $s_1$, $s_2$, $s_3$.

**Câu (b).** Với $p=1$: từ $s_1$ sang phải tới $s_2$, tại $s_2$ hành động 1 đưa về $s_1$, rồi lại $s_2$; lượt lặp $s_1,s_2,s_1,\dots$ và không tới $s_4$. Với $p=0$: tại $s_1$ sang trái thì đứng yên, lượt ở $s_1$ mãi. Trong cả hai trường hợp lượt không kết thúc, và tổng phần thưởng của $n$ bước đầu là $-n\to-\infty$. Giả thiết lượt kết thúc hầu chắc chắn của Định nghĩa 09.14 không thỏa; theo giới hạn trên, ta viết $J=-\infty$ cho cả hai chính sách.

**Câu (c).** Với $Q(s,a)=\phi(s,a)^\top w$, $Q(s,1)=w_1$ và $Q(s,2)=w_2$ ở mọi ô, nên hành động tham lam như nhau ở mọi ô. Khi $w_1>w_2$, $p=1-\epsilon+\epsilon/2=0{,}95$; khi $w_1<w_2$, $p=\epsilon/2=0{,}05$. Chính sách softmax đạt mọi $p\in(0,1)$, vì $\theta_1-\theta_2$ chạy trên $\mathbb R$.

**Kiểm tra lại.** Hai giá trị $0{,}95$ và $0{,}05$ là hai chính sách "chọn phải với xác suất cao $1-\epsilon/2$" và "chọn trái với cùng xác suất cao" mà Sutton và Barto nêu ở Ví dụ 13.1. Nhầm lẫn thường gặp: cho rằng chính sách tất định luôn đủ, như Định lý 04.25 bảo đảm cho MDP hữu hạn với $0\le\gamma<1$. Định lý đó cần chính sách được phép phụ thuộc trạng thái đầy đủ; ở đây đặc trưng gộp ba ô, như hai ô xám của Ví dụ 09.8.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 09.14. Hàm điểm của chính sách softmax tuyến tính

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 13.3, §13.3, tr. 329; đặc trưng ở (c) theo Ví dụ 13.1, tr. 323.

::: exercise Bài tập 09.14 (Hàm điểm của chính sách softmax tuyến tính)
Tập hành động $\mathcal A$ hữu hạn; đặc trưng $\phi(s,a)\in\mathbb R^d$ không phụ thuộc $\theta$; chính sách softmax với mức ưu tiên tuyến tính $h(s,a,\theta)=\phi(s,a)^\top\theta$:
$$
\begin{aligned}
\pi_\theta(a\mid s)&=\frac{e^{h_a}}{\sum_{b\in\mathcal A}e^{h_b}},\\
h_a&=\phi(s,a)^\top\theta.
\end{aligned}
$$

- (a) Chỉ dùng định nghĩa và phép tính vi phân sơ cấp, chứng minh
$$
\begin{aligned}
&\nabla_\theta\log\pi_\theta(a\mid s)\\
&\quad=\phi(s,a)\\
&\quad-\sum_{b\in\mathcal A}\pi_\theta(b\mid s)\,\phi(s,b).
\end{aligned}
$$
- (b) Suy ra $\sum_a\pi_\theta(a\mid s)\,\psi_\theta(s,a)=0$.
- (c) Với đặc trưng của hành lang ngắn, $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ ở mọi ô, và $p=\pi_\theta(1\mid s)$, tính $\psi_\theta(s,1)$, $\psi_\theta(s,2)$ theo $p$, kiểm (b), và tính hai hàm điểm tại $p=\tfrac12$.
:::

::: hint Gợi ý Bài tập 09.14
Với $h_b=\phi(s,b)^\top\theta$, lấy đạo hàm riêng theo một tọa độ $\theta_k$ của $\log\pi_\theta(a\mid s)=h_a-\log\sum_be^{h_b}$, với $\partial h_b/\partial\theta_k=\phi_k(s,b)$, rồi xếp các tọa độ thành vector.
:::

::: solution Lời giải Bài tập 09.14
**Câu (a).** Đặt $h_b=\phi(s,b)^\top\theta=\sum_{k=1}^d\phi_k(s,b)\theta_k$, nên $\partial h_b/\partial\theta_k=\phi_k(s,b)$. Lấy logarit của định nghĩa: $\log\pi_\theta(a\mid s)=h_a-\log\sum_be^{h_b}$. Đạo hàm riêng theo $\theta_k$, với quy tắc đạo hàm của $\log$ và của hàm mũ:
$$
\begin{aligned}
&\frac{\partial\log\pi_\theta(a\mid s)}{\partial\theta_k}\\
&\quad=\phi_k(s,a)-\frac{\sum_be^{h_b}\,\phi_k(s,b)}{\sum_ce^{h_c}}\\
&\quad=\phi_k(s,a)\\
&\qquad-\sum_b\pi_\theta(b\mid s)\,\phi_k(s,b).
\end{aligned}
$$
Dòng hai dùng $e^{h_b}/\sum_ce^{h_c}=\pi_\theta(b\mid s)$. Xếp $d$ tọa độ thành vector được đẳng thức cần chứng minh, tức Mệnh đề 09.16.

**Câu (b).** Nhân (a) với $\pi_\theta(a\mid s)$ rồi cộng theo $a$:
$$
\begin{aligned}
&\sum_a\pi_\theta(a\mid s)\,\psi_\theta(s,a)\\
&\quad=\sum_a\pi_\theta(a\mid s)\,\phi(s,a)\\
&\qquad-1\cdot\sum_b\pi_\theta(b\mid s)\,\phi(s,b)\\
&\quad=0,
\end{aligned}
$$
vì $\sum_a\pi_\theta(a\mid s)=1$. Đây là Mệnh đề 09.17 cho chính sách softmax.

**Câu (c).** Đặc trưng trung bình là $p(1;\,0)+(1-p)(0;\,1)=(p;\,1-p)$. Do đó
$$
\begin{aligned}
\psi_\theta(s,1)&=(1-p)(1;\,-1),\\
\psi_\theta(s,2)&=-p\,(1;\,-1).
\end{aligned}
$$
Kiểm (b): $p(1-p)(1;\,-1)-(1-p)p(1;\,-1)=(0;\,0)$. Tại $p=\tfrac12$: $\psi_\theta(s,1)=\bigl(\tfrac12;\,-\tfrac12\bigr)$, $\psi_\theta(s,2)=\bigl(-\tfrac12;\,\tfrac12\bigr)$.

**Kiểm tra lại.** Ở (c), hai hàm điểm cùng phương $(1;\,-1)$ vì chính sách chỉ phụ thuộc $\theta_1-\theta_2$; độ dài tỉ lệ với $1-p$ và $p$, nên hành động ít được chọn có hàm điểm dài hơn. Lỗi thường gặp: quên trừ đặc trưng trung bình, được $\psi_\theta(s,1)=(1;\,0)$ và kỳ vọng $(p;\,1-p)\ne0$; dùng trung bình đều $\tfrac1{\lvert\mathcal A\rvert}\sum_b\phi(s,b)$ thay cho trung bình theo $\pi_\theta$, được kỳ vọng $\bigl(p-\tfrac12\bigr)(1;\,-1)$, khác $0$ khi $p\ne\tfrac12$.
:::

### Bài tập 09.15. Định lý gradient chính sách có chiết khấu

**Mức độ:** chứng minh. Mục tiêu học tập 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 13.2, §13.3, tr. 328; khung phân phối theo chính sách tr. 199, phương trình (9.2); chứng minh định lý gradient chính sách tr. 325; (13.5) tr. 326; (13.8) tr. 327.

::: exercise Bài tập 09.15 (Định lý gradient chính sách có chiết khấu)
MDP có $\mathcal S$, $\mathcal A$ hữu hạn; trạng thái đầu $S_0\sim\rho_0$ (Sutton và Barto viết $h$); động lực $P(s',r\mid s,a)$ không phụ thuộc $\theta$; phần thưởng bị chặn; độ dài lượt $T\le T_{\max}$ dưới mọi $\pi_\theta$; $\gamma\in[0,1]$. Chính sách $\pi=\pi_\theta$ khả vi theo $\theta$. $J(\theta)=\sum_s\rho_0(s)\,v_\pi(s)$. Viết $P_\pi(s'\mid s)=\sum_a\pi(a\mid s)\sum_rP(s',r\mid s,a)$ và $\Pr(s\to x,k,\pi)$ cho xác suất ở trạng thái không kết thúc $x$ sau đúng $k$ bước, xuất phát từ $s$, dưới $\pi$. Với $\gamma=1$, Sutton và Barto (tr. 199) định nghĩa số lần thăm kỳ vọng $\eta(s)$ qua hệ
$$
\begin{aligned}
\eta(s)&=h(s)\\
&\quad+\sum_{\bar s}\eta(\bar s)\\
&\quad\cdot\sum_a\pi(a\mid\bar s)\,p(s\mid\bar s,a),
\end{aligned}
$$
và phát biểu định lý gradient chính sách $\nabla J\propto\sum_s\mu(s)\sum_a q_\pi(s,a)\nabla\pi(a\mid s)$ với $\mu$ là $\eta$ đã chuẩn hóa.

- (a) Đặt $g(s)=\sum_a\nabla_\theta\pi(a\mid s)\,q_\pi(s,a)$. Từ $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$ và $q_\pi(s,a)=\sum_{s',r}P(s',r\mid s,a)\bigl(r+\gamma v_\pi(s')\bigr)$, chứng minh $\nabla_\theta v_\pi(s)=g(s)+\gamma\sum_{s'}P_\pi(s'\mid s)\nabla_\theta v_\pi(s')$.
- (b) Lặp đẳng thức ở (a) để được $\nabla_\theta v_\pi(s)=\sum_x\sum_{k\ge0}\gamma^k\Pr(s\to x,k,\pi)\,g(x)$. Suy ra $\nabla_\theta J=\sum_x\eta_\gamma(x)\,g(x)$ với $\eta_\gamma(x)=\sum_s\rho_0(s)\sum_{k\ge0}\gamma^k\Pr(s\to x,k,\pi)$, và chứng minh $\eta_\gamma$ thỏa dạng có chiết khấu của hệ trên: $\eta_\gamma(x)=\rho_0(x)+\gamma\sum_{\bar x}\eta_\gamma(\bar x)P_\pi(x\mid\bar x)$ với mọi $x$ không kết thúc.
- (c) Suy ra $\nabla_\theta J=\mathbb E_\pi\bigl[\sum_{t=0}^{T-1}\gamma^tG_t\psi_t\bigr]$ và bước cập nhật REINFORCE tại bước $t$, $\theta\leftarrow\theta+\alpha\gamma^tG_t\psi_t$. Giải thích thừa số $\gamma^t$ đến từ đâu.
:::

::: hint Gợi ý Bài tập 09.15
(a) Quy tắc tích cho $\nabla(\pi q)$; $P$ và $r$ không phụ thuộc $\theta$. (b) Thay $\nabla v_\pi(s')$ ở vế phải bằng chính đẳng thức (a); sau $T_{\max}$ bước mọi lượt đã kết thúc. Với hệ của $\eta_\gamma$, tách hạng $k=0$ và dùng $\Pr(s\to x,k+1,\pi)=\sum_{\bar x}\Pr(s\to\bar x,k,\pi)P_\pi(x\mid\bar x)$. (c) Viết $\nabla\pi=\pi\psi$, đổi tổng theo $x$ thành kỳ vọng theo $S_k$, rồi dùng $\mathbb E[G_k\mid S_k,A_k]=q_\pi(S_k,A_k)$.
:::

::: solution Lời giải Bài tập 09.15
**Câu (a).** Theo quy tắc tích,
$$
\begin{aligned}
&\nabla_\theta v_\pi(s)\\
&=\sum_a\nabla_\theta\pi(a\mid s)\,q_\pi(s,a)\\
&\quad+\sum_a\pi(a\mid s)\,\nabla_\theta q_\pi(s,a)\\
&=g(s)+\gamma\sum_a\pi(a\mid s)\\
&\quad\cdot\sum_{s',r}P(s',r\mid s,a)\,\nabla_\theta v_\pi(s')\\
&=g(s)\\
&\quad+\gamma\sum_{s'}P_\pi(s'\mid s)\,\nabla_\theta v_\pi(s').
\end{aligned}
$$
Dòng hai dùng $\nabla_\theta q_\pi(s,a)=\gamma\sum_{s',r}P(s',r\mid s,a)\,\nabla_\theta v_\pi(s')$, vì $P$ và $r$ không phụ thuộc $\theta$; dòng ba gom tổng theo $a$ và $r$. Hạng ứng với $s'$ kết thúc bằng $0$ vì $v_\pi$ tại đó luôn bằng $0$.

**Câu (b).** Thế đẳng thức (a) cho $\nabla_\theta v_\pi(s')$ vào chính nó $K$ lần:
$$
\begin{aligned}
&\nabla_\theta v_\pi(s)\\
&=\sum_{k=0}^{K}\gamma^k\\
&\quad\cdot\sum_x\Pr(s\to x,k,\pi)\,g(x)\\
&\quad+\gamma^{K+1}\\
&\quad\cdot\sum_x\Pr(s\to x,K+1,\pi)\\
&\quad\cdot\nabla_\theta v_\pi(x),
\end{aligned}
$$
vì $\Pr(s\to x,k+1,\pi)=\sum_{\bar x}\Pr(s\to\bar x,k,\pi)P_\pi(x\mid\bar x)$ trên các trạng thái không kết thúc. Với $K+1\ge T_{\max}$, mọi lượt đã kết thúc, $\Pr(s\to x,K+1,\pi)=0$, nên phần dư bằng $0$ và tổng theo $k$ hữu hạn. Nhân với $\rho_0(s)$, cộng theo $s$ và đổi thứ tự các tổng hữu hạn: $\nabla_\theta J=\sum_s\rho_0(s)\nabla_\theta v_\pi(s)=\sum_x\eta_\gamma(x)\,g(x)$.

Hệ của $\eta_\gamma$: hạng $k=0$ là $\sum_s\rho_0(s)\Pr(s\to x,0,\pi)=\rho_0(x)$. Với các hạng $k\ge1$, dùng hệ thức truy hồi ở trên:
$$
\begin{aligned}
&\eta_\gamma(x)\\
&=\rho_0(x)+\sum_s\rho_0(s)\sum_{k\ge0}\gamma^{k+1}\\
&\quad\cdot\sum_{\bar x}\Pr(s\to\bar x,k,\pi)\\
&\quad\cdot P_\pi(x\mid\bar x)\\
&=\rho_0(x)\\
&\quad+\gamma\sum_{\bar x}\eta_\gamma(\bar x)\,P_\pi(x\mid\bar x).
\end{aligned}
$$
Với $\gamma=1$ và $P_\pi(x\mid\bar x)=\sum_a\pi(a\mid\bar x)p(x\mid\bar x,a)$, đây là hệ (9.2) của Sutton và Barto; thừa số $\gamma$ trong hạng thứ hai coi chiết khấu như việc lượt kết thúc với xác suất $1-\gamma$ ở mỗi bước.

**Câu (c).** Dùng $\nabla_\theta\pi=\pi\,\psi_\theta$ trên tập $\pi>0$ và $\sum_s\rho_0(s)\Pr(s\to x,k,\pi)=\Pr(S_k=x,\,k<T)$:
$$
\begin{aligned}
&\nabla_\theta J\\
&=\sum_{k\ge0}\gamma^k\\
&\quad\cdot\sum_x\Pr(S_k=x,\,k<T)\\
&\quad\cdot\sum_a\pi(a\mid x)\,q_\pi(x,a)\\
&\quad\cdot\psi_\theta(x,a)\\
&=\sum_{k\ge0}\gamma^k\,\mathbb E\bigl[\mathbf 1\{k<T\}\\
&\quad\cdot q_\pi(S_k,A_k)\,\psi_k\bigr]\\
&=\sum_{k\ge0}\gamma^k\\
&\quad\cdot\mathbb E\bigl[\mathbf 1\{k<T\}\,G_k\,\psi_k\bigr]\\
&=\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^tG_t\psi_t\Bigr].
\end{aligned}
$$
Dòng hai viết tổng theo $x$, $a$ thành kỳ vọng theo $(S_k,A_k)$, với $A_k\sim\pi(\cdot\mid S_k)$. Dòng ba dùng tính chất tháp: $\mathbf 1\{k<T\}\psi_k$ là hàm của $(S_k,A_k)$ và $\mathbb E[G_k\mid S_k,A_k]=q_\pi(S_k,A_k)$ theo tính Markov. Dòng bốn đổi tổng hữu hạn ($T\le T_{\max}$) với kỳ vọng. Mỗi lượt cho một mẫu $\sum_t\gamma^tG_t\psi_t$ của gradient; lấy từng hạng một được bước $\theta\leftarrow\theta+\alpha\gamma^tG_t\psi_t$, dạng (13.8) có thêm $\gamma^t$ như trong mã giả của Sutton và Barto (§13.3).

Thừa số $\gamma^t$ đến từ $\eta_\gamma$: trạng thái thăm ở bước $k$ được tính với trọng số $\gamma^k$, vì $J=\mathbb E[G_0]$ chiết khấu mọi phần thưởng từ bước $0$. Trọng số $\eta(s)$ trong đoạn đọc Hệ quả 09.24 của ghi chú là $\eta_\gamma$ ở đây. Với $\gamma=1$, $\eta_1=\eta$ là số lần thăm kỳ vọng, và $\nabla_\theta J=\sum_x\eta(x)\,g(x)$ tỉ lệ với $\sum_x\mu(x)\,g(x)$, hệ số tỉ lệ là $\sum_{x'}\eta(x')$: đó là (13.5).

**Kiểm tra lại.** Kết quả (c) trùng Định lý 09.23, chứng minh bằng đường khác: ghi chú đi qua $\nabla\log p_\theta(\tau)$ và bỏ phần thưởng quá khứ (Bổ đề 09.21, 09.22), bài này đi qua phương trình Bellman của $\nabla v_\pi$. Khi $\gamma<1$, $\eta_\gamma(x)=\nu^\pi_\gamma(x)/(1-\gamma)$ tại mọi trạng thái không kết thúc $x$, nên (b) là Hệ quả 09.24. Lỗi thường gặp: quên hạng $\pi\nabla q$ ở (a), tức coi $q_\pi$ không phụ thuộc $\theta$; bỏ $\gamma^k$ khi lặp, được $\eta_1$ thay cho $\eta_\gamma$, và hướng cập nhật không còn là gradient của $J$ khi $\gamma<1$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 09.16. Xác suất tối ưu trên hành lang ngắn

**Mức độ:** vận dụng. Mục tiêu học tập 3 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 13.1, §13.1, tr. 324, phần thứ hai; dữ kiện và các giá trị đối chiếu ở Ví dụ 13.1, tr. 323.

::: exercise Bài tập 09.16 (Xác suất tối ưu trên hành lang ngắn)
Hành lang ngắn đảo hành động: bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 "sang phải", hành động 2 "sang trái"; ở $s_1$, $s_3$ tác dụng thông thường (sang trái tại $s_1$ thì đứng yên, sang phải tại $s_3$ thì tới $s_4$); ở $s_2$ hai hành động bị đảo (hành động 1 về $s_1$, hành động 2 tới $s_3$). Chính sách chọn hành động 1 với cùng xác suất $p\in(0,1)$ ở mọi ô (Bài tập 09.13). Viết $v_i$ cho giá trị của ô $s_i$ dưới chính sách đó, $v_4=0$, và $J(p)=v_1$.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

- (a) Viết ba phương trình Bellman cho $v_1$, $v_2$, $v_3$.
- (b) Giải hệ để được $J(p)$ ở dạng đóng; kiểm tại $p=\tfrac12$.
- (c) Tìm biểu thức chính xác của xác suất tối ưu $p^*$ chọn "sang phải" và giá trị $J(p^*)$, rồi làm tròn hai chữ số thập phân.
- (d) Tính $J(0{,}95)$ và $J(0{,}05)$, giá trị của hai chính sách $\epsilon$-tham lam ở Bài tập 09.13(c), và so với $J(p^*)$.
:::

::: hint Gợi ý Bài tập 09.16
Mỗi phương trình có dạng: giá trị bằng $-1$ cộng trung bình theo $p$ của giá trị ô kế tiếp. Từ phương trình của $v_1$, biểu diễn $v_1$ theo $v_2$; từ phương trình của $v_3$, biểu diễn $v_3$ theo $v_2$; thế cả hai vào phương trình của $v_2$. Khi cực đại, viết $J=-2f(p)$ với $f>0$ rồi lấy đạo hàm của $\log f$.
:::

::: solution Lời giải Bài tập 09.16
**Câu (a).** Mỗi bước nhận $-1$; tại $s_1$, hành động 1 tới $s_2$, hành động 2 đứng yên; tại $s_2$, hành động 1 về $s_1$, hành động 2 tới $s_3$; tại $s_3$, hành động 1 tới $s_4$, hành động 2 về $s_2$:
$$
\begin{aligned}
v_1&=-1+p\,v_2+(1-p)\,v_1,\\
v_2&=-1+p\,v_1+(1-p)\,v_3,\\
v_3&=-1+p\cdot0+(1-p)\,v_2.
\end{aligned}
$$

**Câu (b).** Phương trình đầu cho $p\,v_1=-1+p\,v_2$, tức $v_1=v_2-\tfrac1p$. Thế $v_1$ và $v_3=-1+(1-p)v_2$ vào phương trình thứ hai:
$$
\begin{aligned}
v_2&=-1+p\Bigl(v_2-\frac1p\Bigr)\\
&\quad+(1-p)\\
&\quad\cdot\bigl(-1+(1-p)v_2\bigr)\\
&=-(3-p)\\
&\quad+\bigl[p+(1-p)^2\bigr]v_2,
\end{aligned}
$$
nên $v_2\bigl[1-p-(1-p)^2\bigr]=v_2\,p(1-p)=-(3-p)$ và $v_2=-\dfrac{3-p}{p(1-p)}$. Từ đó
$$
\begin{aligned}
J(p)=v_1&=-\frac{3-p}{p(1-p)}-\frac1p\\
&=-\frac{2(2-p)}{p(1-p)},
\end{aligned}
$$
và $v_3=-1+(1-p)v_2=-\dfrac3p$. Tại $p=\tfrac12$: $J=-\dfrac{2\cdot1{,}5}{0{,}25}=-12$, $v_2=-10$, $v_3=-6$. Kiểm phương trình thứ hai: $-1+\tfrac12(-12)+\tfrac12(-6)=-10$. Vì $J=-\mathbb E[T]$, chính sách $p=\tfrac12$ cần trung bình $12$ bước để tới đích.

**Câu (c).** Cực đại $J$ tương đương cực tiểu $f(p)=\dfrac{2-p}{p(1-p)}>0$. Đạo hàm của $\log f$ bằng $0$:
$$
-\frac1{2-p}-\frac1p+\frac1{1-p}=0 .
$$
Nhân hai vế với $p(1-p)(2-p)>0$:
$$
\begin{aligned}
0&=-p(1-p)\\
&\quad-(2-p)(1-p)\\
&\quad+p(2-p)\\
&=-p^2+4p-2,
\end{aligned}
$$
tức $p^2-4p+2=0$. Nghiệm trong $(0,1)$ là $p^*=2-\sqrt2\approx0{,}59$; nghiệm kia $2+\sqrt2>1$. Vì $J\to-\infty$ khi $p\to0$ và khi $p\to1$, và $p^*$ là điểm dừng duy nhất trong $(0,1)$, $p^*$ là điểm cực đại. Với $p^*(1-p^*)=(2-\sqrt2)(\sqrt2-1)=3\sqrt2-4$ và $2-p^*=\sqrt2$:
$$
\begin{aligned}
J(p^*)&=-\frac{2\sqrt2}{3\sqrt2-4}\\
&=-\frac{2\sqrt2\,(3\sqrt2+4)}{18-16}\\
&=-(6+4\sqrt2)\\
&\approx-11{,}66 .
\end{aligned}
$$

**Câu (d).** $J(0{,}95)=-\dfrac{2\cdot1{,}05}{0{,}95\cdot0{,}05}\approx-44{,}21$ và $J(0{,}05)=-\dfrac{2\cdot1{,}95}{0{,}05\cdot0{,}95}\approx-82{,}11$. Hai chính sách $\epsilon$-tham lam cần trung bình khoảng $44{,}2$ và $82{,}1$ bước để tới đích, so với khoảng $11{,}66$ bước của $p^*$. Chính sách đều $p=\tfrac12$ cần nhiều hơn $p^*$ khoảng $0{,}34$ bước.

**Kiểm tra lại.** Các giá trị $p^*\approx0{,}59$, $J(p^*)\approx-11{,}6$, và $J(0{,}95)$, $J(0{,}05)$ nhỏ hơn $-44$ và $-82$, khớp Ví dụ 13.1 của Sutton và Barto. Lỗi thường gặp: quên rằng sang trái tại $s_1$ giữ tác tử ở $s_1$, viết $v_1=-1+p\,v_2$ (bỏ hạng $(1-p)v_1$); đảo hai hành động ở $s_1$ thay vì $s_2$; quên rằng $p$ chung cho cả ba ô và tối ưu riêng từng ô.
:::

### Bài tập 09.17. Đơn vị Bernoulli–logistic

**Mức độ:** vận dụng. Mục tiêu học tập 3 và 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 13.5, §13.7, tr. 336; câu (b) và (c) ở đây là câu (c) và (b) của sách.

::: exercise Bài tập 09.17 (Đơn vị Bernoulli–logistic)
Một đơn vị Bernoulli–logistic (Bernoulli-logistic unit) là một nơ-ron ngẫu nhiên dùng trong một số mạng nơ-ron nhân tạo. Tại bước $t$, đầu vào của nó là vector đặc trưng $\phi(S_t)\in\mathbb R^d$ (Sutton và Barto viết $\mathbf x(S_t)$); đầu ra $A_t\in\{0,1\}$ có $\Pr(A_t=1)=P_t$, $\Pr(A_t=0)=1-P_t$. Gọi $h(s,0,\theta)$, $h(s,1,\theta)$ là mức ưu tiên của hai hành động tại $s$, với hiệu $h(s,1,\theta)-h(s,0,\theta)=\theta^\top\phi(s)$; chính sách là softmax theo mức ưu tiên, $\pi_\theta(a\mid s)=e^{h(s,a,\theta)}/\bigl(e^{h(s,0,\theta)}+e^{h(s,1,\theta)}\bigr)$. Ký hiệu hàm logistic là $\operatorname{sig}(z)=1/(1+e^{-z})$, để chữ $\sigma$ giữ nghĩa độ lệch chuẩn của chính sách Gaussian.

- (a) Chứng minh $P_t=\pi_\theta(1\mid S_t)=\operatorname{sig}\bigl(\theta^\top\phi(S_t)\bigr)$.
- (b) Đặt $P=\pi_\theta(1\mid s)$. Tính $\nabla_\theta\log\pi_\theta(a\mid s)$ cho $a=1$ và $a=0$, rồi viết thành một biểu thức theo $a$, $P$ và $\phi(s)$. Kiểm kỳ vọng của biểu thức này theo $A\sim\pi_\theta(\cdot\mid s)$ bằng $0$.
- (c) Viết cập nhật REINFORCE từ $\theta_t$ sang $\theta_{t+1}$ khi nhận lợi tức $G_t$, với bước học $\alpha$ và hệ số chiết khấu $\gamma$.
:::

::: hint Gợi ý Bài tập 09.17
(a) Chia tử và mẫu của softmax cho $e^{h(s,1,\theta)}$. (b) Tính đạo hàm của $\log P$ và $\log(1-P)$ theo $P$, dùng quy tắc dây chuyền qua $P$, gộp hai kết quả thành một biểu thức theo $a$ và $P$, rồi dùng quy tắc dây chuyền lần nữa qua $z=\theta^\top\phi(s)$, với $\operatorname{sig}'(z)=\operatorname{sig}(z)\bigl(1-\operatorname{sig}(z)\bigr)$.
:::

::: solution Lời giải Bài tập 09.17
**Câu (a).** Theo softmax,
$$
\begin{aligned}
\pi_\theta(1\mid s)&=\frac{e^{h(s,1,\theta)}}{e^{h(s,0,\theta)}+e^{h(s,1,\theta)}}\\
&=\frac{1}{1+e^{h(s,0,\theta)-h(s,1,\theta)}}\\
&=\frac1{1+e^{-\theta^\top\phi(s)}} .
\end{aligned}
$$
Với $s=S_t$ ta được $P_t=\operatorname{sig}\bigl(\theta^\top\phi(S_t)\bigr)$. Chỉ hiệu hai mức ưu tiên ảnh hưởng đến chính sách, vì cộng cùng một hằng vào mọi mức ưu tiên không đổi softmax.

**Câu (b).** Đặt $z=\theta^\top\phi(s)$, nên $P=\operatorname{sig}(z)$, $\partial P/\partial z=P(1-P)$ và $\nabla_\theta z=\phi(s)$. Với $a=1$: $\log\pi_\theta(1\mid s)=\log P$, nên
$$
\begin{aligned}
&\nabla_\theta\log\pi_\theta(1\mid s)\\
&\quad=\frac{P(1-P)}{P}\,\phi(s)\\
&\quad=(1-P)\,\phi(s).
\end{aligned}
$$
Với $a=0$: $\log\pi_\theta(0\mid s)=\log(1-P)$, nên
$$
\begin{aligned}
&\nabla_\theta\log\pi_\theta(0\mid s)\\
&\quad=-\frac{P(1-P)}{1-P}\,\phi(s)\\
&\quad=-P\,\phi(s).
\end{aligned}
$$
Hai trường hợp gộp thành
$$
\psi_\theta(s,a)=(a-P)\,\phi(s)
$$
với $a\in\{0,1\}$.
Kỳ vọng: $P(1-P)\phi(s)+(1-P)(-P)\phi(s)=0$, đúng Mệnh đề 09.17. Kết quả cũng là Mệnh đề 09.16 với $\phi(s,1)=\phi(s)$, $\phi(s,0)=0$: đặc trưng trung bình là $P\phi(s)$, nên $\psi_\theta(s,a)=\phi(s,a)-P\phi(s)$.

**Câu (c).** Theo Định lý 09.23, mẫu của gradient ứng với bước $t$ là $\gamma^tG_t\psi_t$. Thế (b) với $s=S_t$, $a=A_t$, $P=P_t$:
$$
\begin{aligned}
\theta_{t+1}&=\theta_t\\
&\quad+\alpha\,\gamma^t\,G_t\\
&\quad\cdot(A_t-P_t)\,\phi(S_t).
\end{aligned}
$$
Đây là dạng cập nhật sau từng bước trong mã giả của Sutton và Barto (§13.3), với $P_t$ tính bằng $\theta_t$. Thuật toán 09.25 cộng các hạng $\gamma^tG_t(A_t-P_t)\phi(S_t)$ trên cả lượt, với $P_t$ tính bằng $\theta_{\mathrm{old}}$ giữ cố định, rồi cập nhật một lần.

**Kiểm tra lại.** Với $G_t>0$ và $A_t=1$, hệ số $A_t-P_t=1-P_t>0$, nên bước dời $\theta$ theo $\phi(S_t)$ và $z=\theta^\top\phi(S_t)$ tăng một lượng $\alpha\gamma^tG_t(1-P_t)\lVert\phi(S_t)\rVert^2>0$: xác suất chọn lại $A_t=1$ tăng. Với $A_t=0$, hệ số là $-P_t$ và $z$ giảm. Lỗi thường gặp: dùng $a-P$ với $a\in\{1,2\}$ thay cho $\{0,1\}$; quên thừa số $\phi(s)$; quên $\gamma^t$ khi $\gamma<1$.
:::

## Tài liệu tham khảo

- Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018. §6.7, Bài tập 6.13 (tr. 136); §9.2, phương trình (9.2) (tr. 199); §13.1, Ví dụ 13.1 (tr. 323) và Bài tập 13.1 (tr. 324); §13.2–13.3, (13.5), (13.8), Bài tập 13.2 (tr. 325–328) và Bài tập 13.3 (tr. 329); §13.7, Bài tập 13.5 (tr. 336).
- Ghi chú bài giảng Bài 09: Định nghĩa 09.10, 09.11, 09.14, 09.15; Mệnh đề 09.4, 09.16, 09.17; Định lý 09.23; Hệ quả 09.24; Thuật toán 09.7, 09.25; Ví dụ 09.8.
