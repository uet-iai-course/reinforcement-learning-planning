# Bài tập Bài 07 — Xấp xỉ hàm trong Học tăng cường

Tệp gồm chín bài, Bài tập 07.20–07.28, đánh số tiếp theo mười chín bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-07/lecture-note.md&deck=lecture-07-xap-xi-ham.html) (Bài tập 07.1–07.19) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập các chương 9, 10 và 11 của Sutton và Barto (2018); mỗi bài ghi số bài, mục và trang của sách. Không bài nào trùng bài tập trên bộ trang chiếu. Các bài chia theo ba mức: nhận biết (07.20–07.22); tính toán hoặc chứng minh (07.23–07.26); vận dụng vào bài toán Học tăng cường (reinforcement learning) (07.27, 07.28). Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-07-xap-xi-ham.html#/1/1) | — |
| 2. Hàm giá trị tuyến tính theo đặc trưng | [Mở phần](lecture-07-xap-xi-ham.html#/2/1) | 07.20–07.22; ghi chú: 07.1–07.3 |
| 3. Monte Carlo gradient với hàm xấp xỉ | [Mở phần](lecture-07-xap-xi-ham.html#/3/1) | 07.23–07.26; ghi chú: 07.4–07.6 |
| 4. TD(0) bán gradient và điểm cố định Bellman chiếu | [Mở phần](lecture-07-xap-xi-ham.html#/4/1) | ghi chú: 07.7–07.9 |
| 5. Sarsa bán gradient cho điều khiển | [Mở phần](lecture-07-xap-xi-ham.html#/5/1) | 07.27, 07.28; ghi chú: 07.10–07.12 |
| 6. Q-learning bán gradient và bộ ba bất ổn | [Mở phần](lecture-07-xap-xi-ham.html#/6/1) | 07.28; ghi chú: 07.13, 07.14 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-07-xap-xi-ham.html#/7/1) | ghi chú: 07.15–07.19 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 07. Công thức của ghi chú được dẫn bằng số trong ngoặc, chẳng hạn (2.1); công thức của sách được ghi rõ "của sách". Giá trị ước lượng là $\hat v(s,w)$ cho trạng thái và $\hat q(s,a,w)$ cho cặp trạng thái–hành động, với tham số dùng chung $w\in\mathbb R^d$. Xấp xỉ tuyến tính là $\hat v(s,w)=x(s)^\top w$ và $\hat q(s,a,w)=x(s,a)^\top w$, với vector đặc trưng (feature vector) $x(s)$ hoặc $x(s,a)$ chọn trước (Định nghĩa 07.1). Giá trị thật là $v_\pi$, $q_\pi$; lợi tức (return) $G_t$ thỏa $G_t=R_{t+1}+\gamma G_{t+1}$, $G_T=0$ ở thời điểm kết thúc $T$ của lượt (episode); giá trị tại trạng thái kết thúc bằng $0$.

Cập nhật tổng quát của chương với một mục tiêu cập nhật $U_t$ thay cho $v_\pi(S_t)$ là
$$
\begin{aligned}
w_{t+1}&=w_t+\alpha\,e_t\,\nabla_w\hat v(S_t,w_t),\\
e_t&=U_t-\hat v(S_t,w_t),
\end{aligned}
\tag{9.7}
$$
đánh số theo sách. Đây là (2.1) của ghi chú với $y_t=U_t$; sách đánh chỉ số tham số theo thời điểm $t$, ghi chú đánh theo số lần cập nhật $n$. Với hàm tuyến tính, $\nabla_w\hat v(S_t,w)=x(S_t)$, và Mệnh đề 07.2 cho biết một cập nhật $w'=w+\alpha e\,x(s)$ đổi dự đoán tại $s'$ một lượng $\alpha e\,x(s')^\top x(s)$. Khi $U_t$ không chứa $w$, (9.7) là cập nhật gradient đầy đủ (Định nghĩa 07.12); khi $U_t$ chứa $w$, nó là cập nhật bán gradient (semi-gradient) (Định nghĩa 07.21).

Sai số giá trị bình phương trung bình của sách là $\overline{\mathrm{VE}}(w)=\sum_s\mu(s)\big(v_\pi(s)-\hat v(s,w)\big)^2=2J_\mu(w)$, với $J_\mu$ của (1.3). Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$.

## Mức nhận biết

### Bài tập 07.20. Phương pháp dạng bảng là trường hợp riêng của xấp xỉ tuyến tính

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), Bài tập 9.1, §9.4, trang 209.

::: exercise Bài tập 07.20 (Phương pháp dạng bảng là trường hợp riêng của xấp xỉ tuyến tính)
Cho tập trạng thái hữu hạn $\mathcal S=\{s_1,\dots,s_N\}$. Phương pháp dạng bảng của Bài 05–06 lưu một số $V(s)$ cho mỗi trạng thái và, với một mục tiêu $U_t$, cập nhật $V(S_t)\leftarrow V(S_t)+\alpha\big[U_t-V(S_t)\big]$, các ô khác giữ nguyên. Xấp xỉ tuyến tính là $\hat v(s,w)=x(s)^\top w$, cập nhật theo (9.7).

- (a) Chỉ ra vector đặc trưng $x(s)$ và số chiều $d$ để mọi hàm $V:\mathcal S\to\mathbb R$ đều viết được dưới dạng $\hat v(\cdot,w)$.
- (b) Chứng minh rằng với đặc trưng đó, cập nhật (9.7) trùng cập nhật dạng bảng.
- (c) Nêu vector đặc trưng tương ứng cho bảng $Q$ với tập hành động $\mathcal A=\{a_1,\dots,a_m\}$.
:::

::: hint Gợi ý Bài tập 07.20
Mỗi thành phần của $w$ đóng vai một ô của bảng. Với (b), tính $\nabla_w\hat v(S_t,w)$ rồi xem thành phần nào của $w$ đổi.
:::

::: solution Lời giải Bài tập 07.20
**Câu (a).** Chọn $d=N$ và $x(s_i)=e_i$, vector đơn vị thứ $i$ của $\mathbb R^N$ (đặc trưng chỉ thị, one-hot). Khi đó $\hat v(s_i,w)=e_i^\top w=[w]_i$. Với một hàm $V$ cho trước, $w=\big(V(s_1),\dots,V(s_N)\big)$ cho $\hat v(\cdot,w)=V$.

**Câu (b).** Giả sử $S_t=s_i$. Ta có $\nabla_w\hat v(s_i,w)=e_i$, nên (9.7) thành
$$
w_{t+1}=w_t+\alpha\big[U_t-[w_t]_i\big]e_i .
$$
Chỉ thành phần thứ $i$ đổi, và $[w_{t+1}]_i=[w_t]_i+\alpha\big[U_t-[w_t]_i\big]$; mọi thành phần $j\ne i$ giữ nguyên. Đặt $V(s_j)=[w]_j$ thì đây đúng là cập nhật dạng bảng. Kết quả này là Hệ quả 07.3 của ghi chú: với $s'\ne s$, $x(s')^\top x(s)=0$, nên theo Mệnh đề 07.2 cập nhật không lan sang trạng thái khác.

**Câu (c).** Đánh số các cặp $(s_i,a_k)$ và chọn $d=Nm$, $x(s_i,a_k)=e_{(i,k)}$, vector đơn vị ứng với cặp đó. Khi đó $\hat q(s_i,a_k,w)=[w]_{(i,k)}$ là ô $Q(s_i,a_k)$ của bảng, và cập nhật tại $(S_t,A_t)$ chỉ đổi ô đó.

**Kiểm tra lại.** Với $N=2$, $w=(3;-1)$, $S_t=s_2$, $U_t=1$, $\alpha=0{,}5$: (9.7) cho $w_{t+1}=(3;-1)+0{,}5\cdot2\cdot(0;1)=(3;0)$, đúng bằng $V(s_2)\leftarrow-1+0{,}5\cdot(1-(-1))=0$ còn $V(s_1)=3$ giữ nguyên. Hai lỗi thường gặp: chọn một đặc trưng vô hướng $x(s_i)=i$, khi đó $\hat v(s_i,w)=iw$ chỉ biểu diễn được các hàm tỉ lệ với chỉ số trạng thái; chọn $d<N$, khi đó lớp biểu diễn là không gian con thực sự của $\mathbb R^N$ (Bài tập 07.2) và có hàm $V$ nằm ngoài lớp.
:::

### Bài tập 07.21. Số đặc trưng của cơ sở đa thức

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), Bài tập 9.2, §9.5.1, trang 211; công thức (9.17) của sách, cùng trang.

::: exercise Bài tập 07.21 (Số đặc trưng của cơ sở đa thức)
Mỗi trạng thái $s$ ứng với $k$ số thực $s_1,\dots,s_k$. Với số nguyên $n\ge0$, đặc trưng thứ $i$ của cơ sở đa thức bậc $n$ (order-$n$ polynomial basis) là
$$
x_i(s)=\prod_{j=1}^ks_j^{c_{i,j}},
$$
với mỗi $c_{i,j}$ là một số nguyên thuộc $\{0,1,\dots,n\}$ (công thức (9.17) của sách).

- (a) Giải thích vì sao (9.17) xác định $(n+1)^k$ đặc trưng phân biệt khi số chiều là $k$.
- (b) Liệt kê các đặc trưng khi $k=2$, $n=1$.
:::

::: hint Gợi ý Bài tập 07.21
Mỗi đặc trưng được xác định bởi bộ số mũ $(c_{i,1},\dots,c_{i,k})$. Đếm số bộ như vậy bằng quy tắc nhân.
:::

::: solution Lời giải Bài tập 07.21
**Câu (a).** Mỗi đặc trưng $x_i$ ứng với một bộ số mũ $c_i=(c_{i,1},\dots,c_{i,k})\in\{0,1,\dots,n\}^k$, và mỗi bộ cho một đặc trưng. Mỗi trong $k$ tọa độ có $n+1$ lựa chọn, nên theo quy tắc nhân có $(n+1)^k$ bộ. Hai bộ khác nhau cho hai đơn thức khác nhau, tức hai hàm khác nhau trên $\mathbb R^k$, vì một đa thức bằng $0$ tại mọi điểm của $\mathbb R^k$ thì mọi hệ số của nó bằng $0$. Do đó có đúng $(n+1)^k$ đặc trưng phân biệt.

**Câu (b).** Với $k=2$, $n=1$, bốn bộ số mũ $(0,0)$, $(1,0)$, $(0,1)$, $(1,1)$ cho
$$
x(s)=(1;\ s_1;\ s_2;\ s_1s_2),
$$
gồm $(1+1)^2=4$ đặc trưng, trong đó $s_1s_2$ biểu diễn tương tác của hai biến.

**Kiểm tra lại.** Với $k=1$, (9.17) cho $1,s,s^2,\dots,s^n$, tức $n+1$ đặc trưng, khớp $(n+1)^1$. Hai lỗi thường gặp: đếm $(n+1)k$ vì cộng số lựa chọn của các biến thay vì nhân; bỏ số mũ $0$, được $n^k$ và mất hằng số $1$ cùng mọi đơn thức không chứa một biến nào đó.
:::

### Bài tập 07.22. Bộ số mũ của một vector đặc trưng đa thức

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), Bài tập 9.3, §9.5.1, trang 211; công thức (9.17) của sách, cùng trang.

::: exercise Bài tập 07.22 (Bộ số mũ của một vector đặc trưng đa thức)
Mỗi trạng thái $s$ ứng với $k$ số thực $s_1,\dots,s_k$, và đặc trưng thứ $i$ của cơ sở đa thức bậc $n$ là $x_i(s)=\prod_{j=1}^ks_j^{c_{i,j}}$, với $c_{i,j}\in\{0,1,\dots,n\}$ (công thức (9.17) của sách). Xác định $n$ và các $c_{i,j}$ cho vector đặc trưng
$$
\begin{aligned}
x(s)=\big(&1;\ s_1;\ s_2;\ s_1s_2;\ s_1^2;\\
&s_2^2;\ s_1s_2^2;\ s_1^2s_2;\ s_1^2s_2^2\big).
\end{aligned}
$$
:::

::: hint Gợi ý Bài tập 07.22
Đọc số biến $k$ và số mũ lớn nhất trong vector; so số thành phần với $(n+1)^k$.
:::

::: solution Lời giải Bài tập 07.22
Vector chỉ chứa $s_1$, $s_2$, nên $k=2$. Số mũ lớn nhất của mỗi biến là $2$, nên $n=2$. Bộ số mũ $c_i=(c_{i,1},c_{i,2})$ của chín thành phần, theo thứ tự trong vector, là
$$
\begin{aligned}
&(0,0),\ (1,0),\ (0,1),\\
&(1,1),\ (2,0),\ (0,2),\\
&(1,2),\ (2,1),\ (2,2).
\end{aligned}
$$
Ví dụ, thành phần thứ bảy $s_1s_2^2$ có $c_{7,1}=1$, $c_{7,2}=2$.

**Kiểm tra lại.** Vector có $9=(2+1)^2$ thành phần, và chín bộ trên đều khác nhau, nên đây là toàn bộ cơ sở đa thức bậc $2$ với $k=2$ (Bài tập 07.21). Lỗi thường gặp: lấy $n$ bằng tổng số mũ lớn nhất, $n=4$ từ $s_1^2s_2^2$; trong (9.17), $n$ chặn số mũ của từng biến, không chặn tổng.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 07.23. Bước học cho mã hóa lưới ô bảy chiều

**Mức độ:** tính toán; mục tiêu học tập 1 và 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 9.5, §9.6, trang 223; quy tắc (9.19) của sách, cùng trang; mô tả mã hóa lưới ô ở §9.5.4, trang 217.

::: exercise Bài tập 07.23 (Bước học cho mã hóa lưới ô bảy chiều)
Mã hóa lưới ô (tile coding) dùng nhiều lớp lưới (tiling); mỗi lớp lưới là một phân hoạch của không gian trạng thái thành các ô (tile), nên mỗi trạng thái nằm trong đúng một ô của mỗi lớp lưới. Vector đặc trưng $x(s)$ có một thành phần nhị phân cho mỗi ô của mỗi lớp lưới, bằng $1$ khi $s$ nằm trong ô đó và bằng $0$ ở chỗ khác. Khi muốn học trong khoảng $\tau$ lần gặp các vector đặc trưng gần như nhau, sách đề xuất bước học của các phương pháp hạ gradient ngẫu nhiên tuyến tính
$$
\alpha=\big(\tau\,\mathbb E[x^\top x]\big)^{-1},
\tag{9.19}
$$
với $x$ là vector đặc trưng ngẫu nhiên lấy theo cùng phân phối với các vector đầu vào của cập nhật.

Một không gian trạng thái liên tục bảy chiều được mã hóa bằng lưới ô để ước lượng $\hat v(s,w)\approx v_\pi(s)$. Vì các chiều được cho là ít tương tác, mỗi chiều được chia riêng bằng tám lớp lưới sọc (stripe tiling), tổng cộng $7\times8=56$ lớp lưới. Để tính đến tương tác từng cặp, mỗi cặp trong $\binom72=21$ cặp chiều được chia đồng thời bằng ô chữ nhật, hai lớp lưới cho mỗi cặp. Tổng số lớp lưới là $21\times2+56=98$. Vì còn nhiễu cần lấy trung bình, việc học cần diễn ra dần dần, khoảng $10$ lần gặp cùng một vector đặc trưng trước khi gần tới tiệm cận. Xác định bước học $\alpha$ và giải thích.
:::

::: hint Gợi ý Bài tập 07.23
Đếm số thành phần bằng $1$ của $x(s)$; với vector nhị phân, $x(s)^\top x(s)$ bằng số đó. Sau đó dùng Mệnh đề 07.2 để đọc ý nghĩa của $\alpha\,x(s)^\top x(s)$.
:::

::: solution Lời giải Bài tập 07.23
**Tính $x^\top x$.** Mỗi trạng thái nằm trong đúng một ô của mỗi lớp lưới, và ô của các lớp lưới khác nhau là các thành phần khác nhau của $x(s)$. Do đó $x(s)$ có đúng $98$ thành phần bằng $1$, và vì các thành phần là $0$ hoặc $1$,
$$
x(s)^\top x(s)=98\quad\text{với mọi }s,
$$
nên $\mathbb E[x^\top x]=98$.

**Bước học.** Với $\tau=10$, (9.19) cho
$$
\alpha=\frac1{10\cdot98}=\frac1{980}\approx0{,}00102 .
$$

**Lý do.** Theo Mệnh đề 07.2, một cập nhật (9.7) tại $s$ với sai lệch $e=U_t-\hat v(s,w_t)$ đổi dự đoán tại $s$ một lượng $\alpha e\,x(s)^\top x(s)=e/10$. Nếu cùng vector đặc trưng gặp lại với cùng mục tiêu $U$, sai lệch sau mỗi lần nhân với $1-\tfrac1{10}=0{,}9$; sau $k$ lần, sai lệch còn $0{,}9^k$ lần ban đầu. Khi các mục tiêu có nhiễu, mỗi mục tiêu chỉ kéo dự đoán đi một phần mười sai lệch của nó, nên sau $k$ lần gặp, với dự đoán ban đầu $\hat v_0$,
$$
\begin{aligned}
\hat v_k&=0{,}9^k\hat v_0\\
&\quad+\textstyle\sum_{j=0}^{k-1}0{,}1\cdot0{,}9^{j}U_{k-j},
\end{aligned}
$$
trong đó $U_{k-j}$ là mục tiêu gặp cách đây $j$ lần.

**Kiểm tra lại.** $0{,}9^{10}\approx0{,}349$: sau mười lần, sai lệch còn khoảng một phần ba. Hai lỗi thường gặp: lấy $\alpha=1/10$, quên chia cho $x^\top x$; khi đó mỗi cập nhật dịch dự đoán $98/10=9{,}8$ lần sai lệch và vượt xa mục tiêu, như trường hợp $\alpha\lVert x\rVert^2=2{,}2>1$ của Ví dụ 07.13; lấy $x^\top x$ bằng tổng số ô của mọi lớp lưới thay vì số ô đang bật.
:::

### Bài tập 07.24. Bước học đưa sai lệch về không sau một cập nhật

**Mức độ:** chứng minh; mục tiêu học tập 1 và 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 9.6, §9.6, trang 223; công thức (9.7) của sách, §9.3, trang 202; quy tắc (9.19), trang 223.

::: exercise Bài tập 07.24 (Bước học đưa sai lệch về không sau một cập nhật)
Cho xấp xỉ tuyến tính $\hat v(s,w)=x(s)^\top w$ và cập nhật (9.7) $w_{t+1}=w_t+\alpha\big[U_t-\hat v(S_t,w_t)\big]\nabla_w\hat v(S_t,w_t)$. Bước học được chọn theo (9.19), $\alpha=\big(\tau\,\mathbb E[x^\top x]\big)^{-1}$. Chứng minh rằng nếu $\tau=1$ và $x(S_t)^\top x(S_t)=\mathbb E[x^\top x]$, thì sau một cập nhật sai lệch tại $S_t$ bằng $0$, tức $\hat v(S_t,w_{t+1})=U_t$.
:::

::: hint Gợi ý Bài tập 07.24
Với hàm tuyến tính, $\nabla_w\hat v(S_t,w)=x(S_t)$. Tính $x(S_t)^\top w_{t+1}$, hoặc dùng Mệnh đề 07.2 với $s'=S_t$.
:::

::: solution Lời giải Bài tập 07.24
Đặt $x=x(S_t)$ và $e=U_t-x^\top w_t$. Giả thiết $x^\top x=\mathbb E[x^\top x]$ cùng việc $\alpha$ xác định theo (9.19) cho $\mathbb E[x^\top x]>0$, nên $x\ne0$ và
$$
\alpha=\frac1{\mathbb E[x^\top x]}=\frac1{x^\top x}.
$$
Với hàm tuyến tính, (9.7) là $w_{t+1}=w_t+\alpha e\,x$. Nhân trái với $x^\top$:
$$
\begin{aligned}
\hat v(S_t,w_{t+1})&=x^\top w_t+\alpha e\,x^\top x\\
&=x^\top w_t+e\\
&=U_t .
\end{aligned}
$$
Dòng thứ nhất là Mệnh đề 07.2 với $s'=s=S_t$, dòng thứ hai thay $\alpha x^\top x=1$, dòng thứ ba dùng định nghĩa của $e$. Vậy sai lệch tại $S_t$ sau cập nhật là $U_t-\hat v(S_t,w_{t+1})=0$.

**Kiểm tra lại.** Với dữ kiện của Ví dụ 07.8, $x(S_t)=(2;1)$, $\lVert x(S_t)\rVert^2=5$, $w_n=(1;-1)$, $G_t=5$: chọn $\alpha=1/5$ cho $w_{n+1}=(1;-1)+0{,}2\cdot4\cdot(2;1)=(2{,}6;-0{,}2)$ và $\hat v(S_t,w_{n+1})=5{,}2-0{,}2=5=G_t$. Hai lỗi thường gặp: kết luận sai lệch bằng $0$ ở mọi trạng thái, trong khi dự đoán tại $s'\ne S_t$ đổi $\alpha e\,x(s')^\top x(S_t)$ và nói chung không tới mục tiêu của nó; áp kết luận cho trạng thái có $x(S_t)^\top x(S_t)\ne\mathbb E[x^\top x]$; khi đó $\alpha x(S_t)^\top x(S_t)\ne1$, và dự đoán dừng trước mục tiêu nếu tích này nhỏ hơn $1$, vượt qua mục tiêu nếu tích lớn hơn $1$ (Ví dụ 07.13).
:::

### Bài tập 07.25. Cập nhật cho một nơ-ron logistic

**Mức độ:** tính toán; mục tiêu học tập 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 9.7, cuối chương 9 (§9.12), trang 237; công thức (9.7) của sách, §9.3, trang 202; đơn vị bán tuyến tính và hàm logistic, §9.7, trang 224.

::: exercise Bài tập 07.25 (Cập nhật cho một nơ-ron logistic)
Một đơn vị bán tuyến tính (semi-linear unit) tính tổng có trọng số của các tín hiệu vào rồi áp một hàm phi tuyến, gọi là hàm kích hoạt (activation function). Mạng nơ-ron nhân tạo đơn giản nhất gồm một đơn vị bán tuyến tính với hàm logistic $f(z)=1/(1+e^{-z})$:
$$
\hat v(s,w)=f\big(w^\top x(s)\big).
$$
Dạng hàm giá trị này hay gặp trong các trò chơi kết thúc bằng thắng hoặc thua, khi giá trị của một trạng thái được hiểu là xác suất thắng. Từ (9.7), suy ra quy tắc học cho trường hợp này ở dạng không còn ký hiệu gradient.
:::

::: hint Gợi ý Bài tập 07.25
Tính $f'(z)$ và biểu diễn nó qua $f(z)$; sau đó dùng quy tắc chuỗi cho $\nabla_w f\big(w^\top x(s)\big)$.
:::

::: solution Lời giải Bài tập 07.25
**Đạo hàm của hàm logistic.** Với $f(z)=(1+e^{-z})^{-1}$,
$$
\begin{aligned}
f'(z)&=\frac{e^{-z}}{(1+e^{-z})^2}\\
&=\frac1{1+e^{-z}}\cdot\frac{e^{-z}}{1+e^{-z}}\\
&=f(z)\big(1-f(z)\big),
\end{aligned}
$$
vì $1-f(z)=e^{-z}/(1+e^{-z})$.

**Gradient.** Theo quy tắc chuỗi, $\nabla_w f\big(w^\top x(s)\big)=f'\big(w^\top x(s)\big)\,x(s)=\hat v(s,w)\big(1-\hat v(s,w)\big)x(s)$.

**Quy tắc học.** Thay vào (9.7), với $\hat v_t=\hat v(S_t,w_t)=1/\big(1+e^{-w_t^\top x(S_t)}\big)$:
$$
\begin{aligned}
w_{t+1}=w_t&+\alpha\big[U_t-\hat v_t\big]\\
&\cdot\hat v_t\,(1-\hat v_t)\,x(S_t),
\end{aligned}
$$
tức mỗi thành phần $[w]_i$ cộng thêm $\alpha\big[U_t-\hat v_t\big]\hat v_t(1-\hat v_t)[x(S_t)]_i$. So với cập nhật tuyến tính, cập nhật có thêm hệ số $\hat v_t(1-\hat v_t)\in(0,\tfrac14]$: khi $\hat v_t$ gần $0$ hoặc gần $1$, hệ số này nhỏ và tham số đổi ít dù sai lệch $U_t-\hat v_t$ lớn. Công thức đúng với mọi mục tiêu $U_t$; khi $U_t$ chứa $w$, như mục tiêu TD, cập nhật là bán gradient (Định nghĩa 07.21).

**Kiểm tra lại.** Tại $z=0$: $f(0)=\tfrac12$ và $f'(0)=\tfrac14=\tfrac12\cdot\tfrac12$. Hai lỗi thường gặp: bỏ hệ số $\hat v_t(1-\hat v_t)$, tức dùng nguyên cập nhật của hàm tuyến tính; viết $f'(z)=f(z)\big(1+f(z)\big)$ do sai dấu khi đạo hàm $e^{-z}$.
:::

### Bài tập 07.26. Sai số lợi tức và sai số giá trị

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 11.4, §11.6, trang 275; đẳng thức (11.24) của sách, cùng trang.

::: exercise Bài tập 07.26 (Sai số lợi tức và sai số giá trị)
Xét trường hợp theo chính sách (on-policy): trạng thái $S_t$ có phân phối $\mu$, và $G_t$ là lợi tức sau $S_t$ khi đi theo $\pi$, với $\mathbb E[G_t^2]<\infty$. Sai số giá trị là $\overline{\mathrm{VE}}(w)=\sum_s\mu(s)\big(v_\pi(s)-\hat v(s,w)\big)^2$. Sai số lợi tức bình phương trung bình (mean square return error) là kỳ vọng theo $\mu$ của bình phương sai lệch giữa ước lượng và lợi tức:
$$
\overline{\mathrm{RE}}(w)=\mathbb E\Big[\big(G_t-\hat v(S_t,w)\big)^2\Big].
$$

- (a) Chứng minh đẳng thức (11.24) của sách: $\overline{\mathrm{RE}}(w)=\overline{\mathrm{VE}}(w)+\mathbb E\Big[\big(G_t-v_\pi(S_t)\big)^2\Big]$.
- (b) Suy ra $\overline{\mathrm{RE}}$ và $\overline{\mathrm{VE}}$ có cùng tập điểm cực tiểu theo $w$.
:::

::: hint Gợi ý Bài tập 07.26
Viết $\overline{\mathrm{RE}}$ thành kỳ vọng theo trạng thái $s$ của kỳ vọng sai lệch bình phương khi biết $S_t=s$. Trong sai lệch, trừ rồi cộng giá trị thật $v_\pi(s)$, nhóm giá trị bị trừ với lợi tức và giá trị được cộng với ước lượng, rồi khai triển bình phương.
:::

::: solution Lời giải Bài tập 07.26
**Câu (a).** Cố định $s$ với $\mu(s)>0$ và đặt $a=G_t-v_\pi(s)$, $c=v_\pi(s)-\hat v(s,w)$, nên $G_t-\hat v(s,w)=a+c$. Khi biết $S_t=s$, $c$ là hằng số. Khai triển bình phương và lấy kỳ vọng có điều kiện $\mathbb E_s[\cdot]=\mathbb E[\cdot\mid S_t=s]$:
$$
\begin{aligned}
\mathbb E_s\big[(a+c)^2\big]&=\mathbb E_s[a^2]+c^2\\
&\quad+2c\,\mathbb E_s[a] .
\end{aligned}
$$
Dữ liệu theo chính sách nên $\mathbb E[G_t\mid S_t=s]=v_\pi(s)$ (Mệnh đề 07.13), tức $\mathbb E_s[a]=0$, và số hạng chéo bằng $0$. Lấy trung bình theo $\mu$ (kỳ vọng lặp): trung bình của $\mathbb E_s[a^2]$ là $\mathbb E\big[(G_t-v_\pi(S_t))^2\big]$, còn trung bình của $c^2=\big(v_\pi(s)-\hat v(s,w)\big)^2$ là $\overline{\mathrm{VE}}(w)$. Do đó
$$
\begin{aligned}
\overline{\mathrm{RE}}(w)&=\overline{\mathrm{VE}}(w)\\
&\quad+\mathbb E\Big[\big(G_t-v_\pi(S_t)\big)^2\Big].
\end{aligned}
$$

Đây là Bổ đề 07.16 của ghi chú, viết theo ký hiệu của sách: $\mathbb E\big[(G_t-v_\pi(s))^2\mid S_t=s\big]=\mathrm{Var}(G_t\mid S_t=s)$ và $\overline{\mathrm{VE}}=2J_\mu$.

**Câu (b).** Số hạng $\mathbb E\big[(G_t-v_\pi(S_t))^2\big]$ không chứa $w$ và hữu hạn vì $\mathbb E[G_t^2]<\infty$. Hai hàm $\overline{\mathrm{RE}}$ và $\overline{\mathrm{VE}}$ chỉ khác nhau một hằng số, nên $w^*$ cực tiểu hóa hàm này khi và chỉ khi nó cực tiểu hóa hàm kia. Với hàm tuyến tính và $\Sigma_\mu$ xác định dương, điểm cực tiểu chung là $w_{\mathrm{MC}}$ duy nhất của Định lý 07.17. $\overline{\mathrm{RE}}$ ước lượng được từ dữ liệu bằng trung bình mẫu của $(G_t-\hat v(S_t,w))^2$, còn $\overline{\mathrm{VE}}$ chứa $v_\pi$ chưa biết; đẳng thức (11.24) cho phép tìm điểm cực tiểu của $\overline{\mathrm{VE}}$ bằng cách cực tiểu hóa $\overline{\mathrm{RE}}$.

**Kiểm tra lại.** Khi lợi tức từ mỗi trạng thái là tất định, $G_t=v_\pi(S_t)$ và $\overline{\mathrm{RE}}=\overline{\mathrm{VE}}$. Hai lỗi thường gặp: cho rằng số hạng chéo bằng $0$ vì $G_t$ và $\hat v(S_t,w)$ độc lập, trong khi lý do đúng là $v_\pi(s)-\hat v(s,w)$ là hằng số khi biết $S_t=s$ và $\mathbb E[G_t-v_\pi(s)\mid S_t=s]=0$; áp đẳng thức cho lợi tức sinh bởi một chính sách hành vi khác $\pi$, khi đó $\mathbb E[G_t\mid S_t=s]$ nói chung khác $v_\pi(s)$ và số hạng chéo không triệt tiêu.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 07.27. Monte Carlo điều khiển với xấp xỉ hàm trên Mountain Car

**Mức độ:** vận dụng; mục tiêu học tập 2 và 6.

**Nguồn:** Sutton và Barto (2018), Bài tập 10.1, §10.2, trang 248; dữ kiện của Ví dụ 10.1 (Mountain Car), §10.1, trang 244–246.

::: exercise Bài tập 07.27 (Monte Carlo điều khiển với xấp xỉ hàm trên Mountain Car)
Sarsa bán gradient một bước theo lượt (Thuật toán 07.33) cập nhật sau mỗi chuyển
$$
\begin{aligned}
w&\leftarrow w+\alpha\,\delta\,\nabla_w\hat q(S,A,w),\\
\delta&=R+\gamma\hat q(S',A',w)\\
&\quad-\hat q(S,A,w),
\end{aligned}
$$
với mục tiêu $R$ thay cho $R+\gamma\hat q(S',A',w)$ khi $S'$ là trạng thái kết thúc, và chọn hành động $\varepsilon$-tham lam theo $\hat q(\cdot,\cdot,w)$. Chương 10 của sách không cho mã giả của phương pháp Monte Carlo nào.

Bài toán Mountain Car: một xe công suất yếu phải lên đỉnh một dốc cao. Trọng lực mạnh hơn động cơ, nên kể cả khi ga tối đa, xe không tăng tốc lên được đoạn dốc đứng; cách duy nhất là trước hết đi ra xa đích, lên sườn dốc đối diện bên trái, rồi ga tối đa để lấy đà lên đích. Phần thưởng bằng $-1$ ở mọi bước cho tới khi xe vượt qua vị trí đích trên đỉnh, và việc đó kết thúc lượt. Có ba hành động $A_t\in\{+1,-1,0\}$: ga tối đa về phía trước, ga tối đa lùi, không ga. Vị trí $p_t$ và vận tốc $\dot p_t$ cập nhật theo
$$
\begin{aligned}
\dot p_{t+1}&=\mathrm{bound}\big[\dot p_t+0{,}001A_t\\
&\qquad-0{,}0025\cos(3p_t)\big],\\
p_{t+1}&=\mathrm{bound}\big[p_t+\dot p_{t+1}\big],
\end{aligned}
$$
trong đó phép $\mathrm{bound}$ giữ $-1{,}2\le p_{t+1}\le0{,}5$ và $-0{,}07\le\dot p_{t+1}\le0{,}07$; khi $p_{t+1}$ chạm biên trái, $\dot p_{t+1}$ được đặt lại bằng $0$; khi chạm biên phải, xe tới đích. Mỗi lượt bắt đầu ở một vị trí ngẫu nhiên $p_0\in[-0{,}6,-0{,}4)$ với vận tốc $0$. Giá trị hành động là $\hat q(s,a,w)=w^\top x(s,a)$ với đặc trưng lưới ô; mọi giá trị hành động khởi tạo bằng $0$, cao hơn mọi giá trị thật (vì các giá trị thật đều âm), và $\varepsilon=0$. Trong lần chạy của sách (Hình 10.1), sau $428$ bước chưa lượt nào kết thúc; trong thời gian đó, các trạng thái đã ghé nhiều bị đánh giá thấp hơn các trạng thái chưa ghé, nên tác tử liên tục bị đẩy tới trạng thái mới cho tới khi tìm được đích.

- (a) Mô tả phương pháp Monte Carlo điều khiển với xấp xỉ hàm tương ứng.
- (b) Giải thích vì sao không cần cho mã giả riêng của phương pháp đó.
- (c) Mô tả hoạt động của phương pháp đó trên Mountain Car.
:::

::: hint Gợi ý Bài tập 07.27
Thay mục tiêu của Sarsa bằng lợi tức $G_t$, rồi xem cập nhật được thực hiện vào lúc nào. Với (c), xét chính sách mà tác tử dùng trong suốt lượt đầu khi $w$ chưa đổi.
:::

::: solution Lời giải Bài tập 07.27
**Câu (a).** Phương pháp dùng mục tiêu $U_t=G_t$ trong cập nhật
$$
\begin{aligned}
w&\leftarrow w+\alpha\,e_t\,\nabla_w\hat q(S_t,A_t,w),\\
e_t&=G_t-\hat q(S_t,A_t,w).
\end{aligned}
$$
Mỗi lượt được sinh trọn vẹn bằng chính sách $\varepsilon$-tham lam theo $\hat q(\cdot,\cdot,w)$ với $w$ giữ cố định; khi lượt kết thúc, tính lùi $G_t=R_{t+1}+\gamma G_{t+1}$ từ $G_T=0$, rồi cập nhật lần lượt tại $t=0,\dots,T-1$. Lượt sau dùng $w$ mới, nên chính sách được cải thiện giữa các lượt. $G_t$ không chứa $w$, nên đây là cập nhật gradient đầy đủ (Định nghĩa 07.12), không phải bán gradient.

**Câu (b).** Phương pháp này là Thuật toán 07.15 (Monte Carlo gradient, mọi lần ghé) với $x(S_t)$ thay bằng $x(S_t,A_t)$, ghép với bước chọn hành động $\varepsilon$-tham lam của Thuật toán 07.33. Không có bước nào mới so với hai thuật toán đó, nên mã giả riêng không thêm thông tin.

**Câu (c).** Trong lượt đầu, $w$ không đổi cho tới khi lượt kết thúc. Vì $\hat q\equiv0$ và $\varepsilon=0$, mọi hành động hòa nhau ở mọi trạng thái, nên chính sách trong suốt lượt đầu chỉ do quy tắc phá hòa quyết định.

Nếu chính sách do quy tắc phá hòa quyết định không đưa xe tới đích, lượt đầu không kết thúc và $w$ không đổi. Trường hợp này xảy ra khi quy tắc phá hòa luôn chọn cùng một hành động: lặp hai phương trình chuyển động của đề trong $10^5$ bước, từ $201$ vị trí đầu cách đều trong $[-0{,}6,-0{,}4)$ với vận tốc $0$, cả ba hành động hằng $A_t\equiv+1$, $A_t\equiv-1$, $A_t\equiv0$ đều không đưa xe tới $p=0{,}5$. Nếu quy tắc phá hòa chọn ngẫu nhiên, lượt chỉ kết thúc khi dãy hành động ngẫu nhiên tình cờ đưa xe tới đích, và $w$ không đổi trước thời điểm đó.

Cơ chế thăm dò của Sarsa cần cập nhật sau mỗi bước: khi $\hat q\approx0$, mục tiêu $-1+\gamma\hat q(S',A',w)\approx-1$ thấp hơn giá trị hiện tại của cặp vừa thử, nên tác tử bị đẩy sang trạng thái chưa ghé ngay trong lượt đầu, kéo dài ít nhất $428$ bước. Monte Carlo không có cơ chế này trong lượt đầu. Nếu lượt bị cắt ngắn ở một giới hạn số bước, Thuật toán 07.15 bỏ lượt đó vì lợi tức chưa đầy đủ, nên Monte Carlo không học được gì từ các lượt chưa tới đích. Vì vậy, trên Mountain Car, Monte Carlo không học được gì cho tới khi có lượt đầu tiên tới đích, trong khi Sarsa học từ bước đầu tiên.

**Kiểm tra lại.** Lập luận ở (c) dùng ba điều: Monte Carlo cập nhật sau khi lượt kết thúc (Thuật toán 07.15); với $w$ cố định, chính sách tham lam không đổi; và phép lặp hai phương trình chuyển động của đề cho ba hành động hằng. Hai lỗi thường gặp: gọi cập nhật Monte Carlo là bán gradient, trong khi $G_t$ không chứa $w$; cho rằng trong lượt đầu, giá trị khởi tạo lạc quan cũng gây thăm dò với Monte Carlo như với Sarsa, trong khi với Monte Carlo giá trị chỉ bị hạ sau khi lượt kết thúc.
:::

### Bài tập 07.28. Expected Sarsa bán gradient

**Mức độ:** vận dụng; mục tiêu học tập 2 và 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 10.2, §10.2, trang 248; quy tắc Expected Sarsa (6.9) của sách, §6.6, trang 133.

::: exercise Bài tập 07.28 (Expected Sarsa bán gradient)
Expected Sarsa dạng bảng giống Q-learning, nhưng thay phép cực đại trên các cặp kế tiếp bằng giá trị kỳ vọng theo xác suất chọn hành động của chính sách hiện tại $\pi$: ô $Q(S_t,A_t)$ được cộng thêm $\alpha\,\delta_t$, với
$$
\begin{gathered}
\delta_t=R_{t+1}+\gamma\bar Q_{t+1}-Q(S_t,A_t),\\
\bar Q_{t+1}=\textstyle\sum_a\pi(a\mid s')\,Q(s',a)
\end{gathered}
$$
với $s'=S_{t+1}$ (công thức (6.9) của sách). Sarsa bán gradient theo lượt là Thuật toán 07.33, và chính sách $\pi_w$ là chính sách $\varepsilon$-tham lam theo $\hat q(\cdot,\cdot,w)$ với $m$ hành động (Định nghĩa 07.31).

- (a) Viết mã giả cho Expected Sarsa bán gradient một bước cho bài toán điều khiển, với $\pi=\pi_w$.
- (b) Viết mục tiêu của (a) theo $\varepsilon$, $m$, $\sum_a\hat q(S_{t+1},a,w)$ và $\max_a\hat q(S_{t+1},a,w)$; suy ra mục tiêu khi $\varepsilon=0$.
:::

::: hint Gợi ý Bài tập 07.28
Thay $Q$ trong (6.9) bằng $\hat q(\cdot,\cdot,w)$ và thêm gradient như (9.7). Với (b), mỗi hành động nhận xác suất $\varepsilon/m$, phần $1-\varepsilon$ chia cho các hành động đạt cực đại.
:::

::: solution Lời giải Bài tập 07.28
**Câu (a).** Mục tiêu tại chuyển $(S,A,R,S')$ là $y=R$ khi $S'$ là trạng thái kết thúc, và $y=R+\gamma\bar q(S',w)$ khi $S'$ chưa kết thúc, với giá trị kỳ vọng của $\hat q$ tại $S'$ theo $\pi_w$
$$
\begin{aligned}
\bar q(S',w)&=\textstyle\sum_a\pi_w(a\mid S')\\
&\qquad\cdot\hat q(S',a,w).
\end{aligned}
$$
Mã giả:

- **Đầu vào.** Hàm $\hat q:\mathcal S\times\mathcal A\times\mathbb R^d\to\mathbb R$ khả vi theo $w$ (tuyến tính: $\hat q(s,a,w)=x(s,a)^\top w$); $\varepsilon$; $\gamma$; bước học $\alpha>0$; số lượt $K$.
- **Khởi tạo.** $w\leftarrow w_0$, ví dụ $w_0=0$.

1. Với mỗi lượt $1,\dots,K$: lấy trạng thái đầu $S$.
2. Chọn $A$ theo $\pi_w(\cdot\mid S)$, thực hiện $A$, nhận $R$, $S'$.
3. Nếu $S'$ kết thúc: $y\leftarrow R$. Ngược lại: tính $\hat q(S',a,w)$ với mọi $a$ bằng $w$ hiện tại, rồi $y\leftarrow R+\gamma\bar q(S',w)$.
4. $w\leftarrow w+\alpha\big[y-\hat q(S,A,w)\big]\nabla_w\hat q(S,A,w)$, với $y$ giữ cố định khi lấy đạo hàm; với hàm tuyến tính, $\nabla_w\hat q(S,A,w)=x(S,A)$.
5. Nếu $S'$ kết thúc: sang lượt mới. Ngược lại: $S\leftarrow S'$, quay lại bước 2.

Mục tiêu chứa $w$ qua $\hat q(S',a,w)$ và được giữ cố định khi lấy đạo hàm, nên đây là cập nhật bán gradient (Định nghĩa 07.21). Mục tiêu không dùng hành động kế tiếp, nên hành động tại $S'$ được chọn ở bước 2 của vòng sau bằng $w$ đã cập nhật, như Thuật toán 07.36 và khác Thuật toán 07.33. Bước 3 cần $m$ tích vô hướng.

**Câu (b).** Gọi $M=\max_a\hat q(S',a,w)$ và $\mathcal G$ là tập hành động đạt $M$. Theo Định nghĩa 07.31, $\pi_w(a\mid S')=\varepsilon/m+(1-\varepsilon)\mathbf 1\{a\in\mathcal G\}/\lvert\mathcal G\rvert$. Mọi hành động trong $\mathcal G$ có giá trị $M$, nên
$$
\begin{gathered}
\bar q(S',w)=\tfrac\varepsilon m\Sigma+(1-\varepsilon)M,\\
y=R+\gamma\big[\tfrac\varepsilon m\Sigma+(1-\varepsilon)M\big]
\end{gathered}
$$
khi $S'$ chưa kết thúc, với $\Sigma=\sum_a\hat q(S',a,w)$ và $M=\max_a\hat q(S',a,w)$. Với $\varepsilon=0$, $y=R+\gamma\max_a\hat q(S',a,w)$, đúng mục tiêu Q-learning (5.1). Với $\varepsilon>0$, mục tiêu là trung bình có trọng số của giá trị tham lam và giá trị trung bình của mọi hành động, không phụ thuộc hành động kế tiếp được chọn.

**Kiểm tra lại.** Trên mẫu thứ hai của Ví dụ 07.14, $(\mathrm C,1,-1,\mathrm D)$ với $w_1=(-0{,}2;0{,}6;-1{,}4)$, $\gamma=1$, $m=2$ và $\varepsilon=0{,}25$ như Bài tập 07.11: $\hat q(\mathrm D,\cdot,w_1)=(-1{,}4;-2{,}6)$, nên $\bar q(\mathrm D,w_1)=0{,}875\cdot(-1{,}4)+0{,}125\cdot(-2{,}6)=-1{,}55$, khớp $0{,}125\cdot(-4)+0{,}75\cdot(-1{,}4)=-1{,}55$ của (b), và $y=-2{,}55$, nằm giữa mục tiêu Sarsa $-3{,}6$ và mục tiêu Q-learning $-2{,}4$ của Ví dụ 07.14. Hai lỗi thường gặp: lấy kỳ vọng theo phân phối đều trên hành động thay vì theo $\pi_w$; tính $\hat q(S',a,w)$ bằng tham số sau cập nhật thay vì tham số trước cập nhật.
:::

## Tài liệu tham khảo

- Sutton, R. S. và Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: Bài tập 9.1, §9.4, trang 209 (Bài tập 07.20); Bài tập 9.2 và 9.3, §9.5.1, trang 211 (Bài tập 07.21, 07.22); Bài tập 9.5 và 9.6, §9.6, trang 223, cùng §9.5.4, trang 217 (Bài tập 07.23, 07.24); Bài tập 9.7, trang 237, cùng §9.7, trang 224 (Bài tập 07.25); Bài tập 11.4, §11.6, trang 275 (Bài tập 07.26); Bài tập 10.1 và 10.2, §10.2, trang 248, cùng Ví dụ 10.1, trang 244–246, và §6.6, trang 133 (Bài tập 07.27, 07.28).
- Ghi chú bài giảng Bài 07: Định nghĩa 07.1, 07.12, 07.21, 07.31; Mệnh đề 07.2, 07.13; Hệ quả 07.3; Bổ đề 07.16; Định lý 07.17; Thuật toán 07.15, 07.33, 07.36; Ví dụ 07.8, 07.13, 07.14; Bài tập 07.2, 07.11.
