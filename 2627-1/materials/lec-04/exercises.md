# Bài tập Bài 04 — Giải MDP bằng quy hoạch động

Tệp gồm mười một bài, Bài tập 04.11–04.21, đánh số tiếp theo mười bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-04/lecture-note.md&deck=lecture-04-giai-mdp-bang-quy-hoach-dong.html) (Bài tập 04.1–04.10) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập chương 3 và chương 4 của Sutton và Barto (2018). Các bài chia theo ba mức: nhận biết (04.11–04.14); tính toán hoặc chứng minh (04.15–04.18); vận dụng vào bài toán Học tăng cường (reinforcement learning) (04.19–04.21). Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/1/1) | — |
| 2. Đánh giá chính sách | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/2/1) | 04.12, 04.15; ghi chú: 04.1 |
| 3. Cải thiện chính sách | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/3/1) | 04.11; ghi chú: 04.2 |
| 4. Lặp chính sách | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/4/1) | 04.16, 04.18, 04.19; ghi chú: 04.3 |
| 5. Lặp giá trị | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/5/1) | 04.13, 04.14, 04.17, 04.20, 04.21; ghi chú: 04.4, 04.8, 04.9 |
| 6. Lịch cập nhật và giới hạn của mô hình bảng | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/6/1) | ghi chú: 04.5, 04.7, 04.10 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/7/1) | ghi chú: 04.6 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 04; công thức của ghi chú được dẫn bằng số trong ngoặc, chẳng hạn (2.1), còn công thức của sách được ghi rõ "của sách". Tập $\mathcal S$ gồm các trạng thái chưa kết thúc, $s_{\mathrm{term}}$ là trạng thái kết thúc, $\mathcal A(s)$ là tập hành động hợp lệ tại $s$, và mô hình là $p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$. Lợi tức là $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$ (công thức (3.8) của sách). Mọi bảng giá trị bằng $0$ tại $s_{\mathrm{term}}$; phần thưởng của chính chuyển đi vào $s_{\mathrm{term}}$ vẫn được tính.

Các đại lượng dùng lại:

- giá trị nhìn trước một bước $Q_V(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr]$, công thức (2.1);
- toán tử Bellman đánh giá $(T_\pi V)(s)=\sum_a\pi(a\mid s)\,Q_V(s,a)$, công thức (1.1), và toán tử Bellman tối ưu $(T_*V)(s)=\max_aQ_V(s,a)$, công thức (4.1);
- phần dư tối ưu $\Delta_*(V)=\lVert T_*V-V\rVert_\infty$ và ngưỡng dừng $\theta=(1-\gamma)\kappa$ cho sai số cho phép $\kappa$ (Hệ quả 04.27);
- giá trị tối ưu $v_*(s)=\sup_{\pi}v_\pi(s)$ và $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_*(s')\bigr]$ (Định nghĩa 04.19).

Tương ứng với sách: (4.4) của sách là $v_\pi=T_\pi v_\pi$, tức (1.2); (4.5) của sách là lượt quét $V_{k+1}=T_\pi V_k$ của Định nghĩa 04.1; (4.10) của sách là lượt quét $V_{k+1}=T_*V_k$ của lặp giá trị (Định nghĩa 04.22). Sách viết $v_k$ cho bảng sau $k$ lượt quét; tệp này viết $V_k$ như ghi chú.

Ví dụ 4.1 và Ví dụ 4.3 của sách là nhiệm vụ có lượt, không chiết khấu ($\gamma=1$). Khi mọi lượt dưới chính sách $\pi$ kết thúc với xác suất $1$ từ mọi trạng thái, $v_\pi$ tồn tại và là nghiệm duy nhất của $v_\pi=T_\pi v_\pi$ (Sutton và Barto, 2018, §4.1, trang 74). Công thức (1.1), (2.1) và (4.1) vẫn dùng được với $\gamma=1$; các chặn của Hệ quả 04.8, 04.26, 04.27 dùng $\gamma<1$, nên nằm ngoài phạm vi của hai ví dụ này.

Số thập phân viết bằng dấu phẩy; khi một bảng có thành phần thập phân, các thành phần cách nhau bằng dấu chấm phẩy.

## Mức nhận biết

### Bài tập 04.11. Giá trị hành động trên lưới 4×4

**Mức độ:** nhận biết; mục tiêu học tập 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.1, §4.1, trang 76; dữ kiện của Ví dụ 4.1, trang 76, và Hình 4.1, trang 77.

::: exercise Bài tập 04.11 (Giá trị hành động trên lưới 4×4)
Lưới $4\times4$ có các trạng thái chưa kết thúc $1,\dots,14$ và một trạng thái kết thúc chiếm hai ô góc, xếp theo hàng như sau (ô kết thúc ghi T):

| | cột 1 | cột 2 | cột 3 | cột 4 |
|---|---|---|---|---|
| hàng 1 | T | $1$ | $2$ | $3$ |
| hàng 2 | $4$ | $5$ | $6$ | $7$ |
| hàng 3 | $8$ | $9$ | $10$ | $11$ |
| hàng 4 | $12$ | $13$ | $14$ | T |

Tại mỗi trạng thái có bốn hành động lên, xuống, phải, trái, chuyển xác định sang ô kề theo hướng đó; hành động đưa ra ngoài lưới giữ nguyên trạng thái. Mọi chuyển có phần thưởng $-1$ cho tới khi vào trạng thái kết thúc; $\gamma=1$. Chính sách $\pi$ là ngẫu nhiên đều, mỗi hành động có xác suất $\tfrac14$. Giá trị $v_\pi$ (Hình 4.1 của sách, $k=\infty$), xếp theo cùng vị trí:

| | cột 1 | cột 2 | cột 3 | cột 4 |
|---|---:|---:|---:|---:|
| hàng 1 | $0$ | $-14$ | $-20$ | $-22$ |
| hàng 2 | $-14$ | $-18$ | $-20$ | $-20$ |
| hàng 3 | $-20$ | $-20$ | $-18$ | $-14$ |
| hàng 4 | $-22$ | $-20$ | $-14$ | $0$ |

Tính $q_\pi(11,\text{xuống})$ và $q_\pi(7,\text{xuống})$.
:::

::: hint Gợi ý Bài tập 04.11
Với $V=v_\pi$, giá trị nhìn trước (2.1) cho $q_\pi$ (Mệnh đề 03.22). Mỗi chuyển ở đây xác định, nên tổng trong (2.1) chỉ còn một số hạng.
:::

::: solution Lời giải Bài tập 04.11
Vì chuyển xác định và $\gamma=1$, công thức (2.1) với $V=v_\pi$ cho $q_\pi(s,a)=-1+v_\pi(s')$, trong đó $s'$ là ô mà hành động $a$ đưa tới từ $s$.

- Từ $11$ (hàng 3, cột 4), đi xuống tới ô kết thúc ở hàng 4, cột 4, nên $q_\pi(11,\text{xuống})=-1+0=-1$.
- Từ $7$ (hàng 2, cột 4), đi xuống tới $11$, nên $q_\pi(7,\text{xuống})=-1+v_\pi(11)=-1+(-14)=-15$.

**Kiểm tra lại.** Theo Mệnh đề 03.23, $v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a)$. Tại $11$, bốn hành động lên, xuống, phải, trái dẫn tới $7$, ô kết thúc, $11$ và $10$, nên
$$
\begin{aligned}
&\tfrac14\bigl[(-1-20)+(-1+0)\\
&\quad+(-1-14)\\
&\quad+(-1-18)\bigr]\\
&=\tfrac14(-56)\\
&=-14=v_\pi(11).
\end{aligned}
$$
Tại $7$, bốn hành động dẫn tới $3$, $11$, $7$ và $6$, nên $\tfrac14\bigl[(-23)+(-15)+(-21)+(-21)\bigr]=-20=v_\pi(7)$. Lỗi thường gặp: cộng $v_\pi(11)$ vào giá trị nhìn trước của hành động xuống tại $11$, trong khi hành động đó đưa vào trạng thái kết thúc, nơi giá trị bằng $0$.
:::

### Bài tập 04.12. Phương trình Bellman và lượt quét cho giá trị hành động

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.3, §4.1, trang 76; đẳng thức (4.3)–(4.5) của sách, trang 74.

::: exercise Bài tập 04.12 (Phương trình Bellman và lượt quét cho giá trị hành động)
Với chính sách Markov dừng $\pi$ và mọi $s\in\mathcal S$, sách viết ba đẳng thức sau cho giá trị trạng thái. Đẳng thức (4.3) của sách:
$$
\begin{aligned}
&v_\pi(s)\\
&\quad=\mathbb E_\pi\bigl[R_{t+1}+\gamma v_\pi(S_{t+1})\\
&\qquad\mid S_t=s\bigr].
\end{aligned}
$$
Đẳng thức (4.4) của sách:
$$
\begin{aligned}
&v_\pi(s)\\
&\quad=\sum_a\pi(a\mid s)\\
&\qquad\times\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma v_\pi(s')\bigr].
\end{aligned}
$$
Lượt quét (4.5) của sách:
$$
\begin{aligned}
&V_{k+1}(s)\\
&\quad=\sum_a\pi(a\mid s)\\
&\qquad\times\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma V_k(s')\bigr].
\end{aligned}
$$
Viết ba đẳng thức tương ứng cho giá trị hành động $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$, với $s\in\mathcal S$, $a\in\mathcal A(s)$, và cho dãy bảng giá trị hành động $Q_k$.
:::

::: hint Gợi ý Bài tập 04.12
Bắt đầu từ $G_t=R_{t+1}+\gamma G_{t+1}$ với điều kiện $S_t=s$, $A_t=a$. Hành động $A_{t+1}$ được chọn theo $\pi(\cdot\mid S_{t+1})$, nên giá trị tiếp nối là trung bình của $q_\pi(S_{t+1},\cdot)$ với trọng số $\pi$.
:::

::: solution Lời giải Bài tập 04.12
Quy ước $q_\pi(s_{\mathrm{term}},a')=0$ và $Q_k(s_{\mathrm{term}},a')=0$, vì mọi phần thưởng sau khi vào trạng thái kết thúc bằng $0$.

**Dạng kỳ vọng, tương ứng (4.3) của sách.** Từ $G_t=R_{t+1}+\gamma G_{t+1}$ và tính Markov, khi đã biết $(S_{t+1},A_{t+1})=(s',a')$, kỳ vọng của $G_{t+1}$ là $q_\pi(s',a')$. Do đó
$$
\begin{aligned}
&q_\pi(s,a)\\
&\quad=\mathbb E_\pi\bigl[R_{t+1}\\
&\qquad+\gamma\,q_\pi(S_{t+1},A_{t+1})\\
&\qquad\mid S_t=s,A_t=a\bigr].
\end{aligned}
$$

**Dạng tổng, tương ứng (4.4) của sách.** Cặp $(S_{t+1},R_{t+1})$ có phân phối $p(\cdot,\cdot\mid s,a)$, và $A_{t+1}$ có phân phối $\pi(\cdot\mid S_{t+1})$, nên
$$
\begin{aligned}
&q_\pi(s,a)\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\Bigl[r\\
&\qquad+\gamma\sum_{a'}\pi(a'\mid s')\\
&\qquad\quad\times q_\pi(s',a')\Bigr].
\end{aligned}
$$
Vì $\sum_{a'}\pi(a'\mid s')\,q_\pi(s',a')=v_\pi(s')$ (Mệnh đề 03.23), đẳng thức này là $q_\pi=Q_{v_\pi}$ (Mệnh đề 03.22).

**Lượt quét, tương ứng (4.5) của sách.** Từ một bảng $Q_0$ bất kỳ trên các cặp $(s,a)$,
$$
\begin{aligned}
&Q_{k+1}(s,a)\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\Bigl[r\\
&\qquad+\gamma\sum_{a'}\pi(a'\mid s')\\
&\qquad\quad\times Q_k(s',a')\Bigr].
\end{aligned}
$$
Lấy hiệu với dạng tổng của $q_\pi$, phần thưởng triệt tiêu, và các trọng số $p$, $\pi$ không âm có tổng bằng $1$, nên $\max_{s,a}\lvert Q_{k+1}(s,a)-q_\pi(s,a)\rvert\le\gamma\max_{s,a}\lvert Q_k(s,a)-q_\pi(s,a)\rvert$, như Bước 2 của chứng minh Mệnh đề 04.4. Với $\gamma<1$, dãy $Q_k$ hội tụ về $q_\pi$.

**Kiểm tra lại.** Lấy trung bình hai vế của dạng tổng theo $\pi(\cdot\mid s)$ cho lại (4.4) của sách: $\sum_a\pi(a\mid s)\,q_\pi(s,a)=v_\pi(s)$. Lỗi thường gặp: viết $\max_{a'}q_\pi(s',a')$ thay cho trung bình theo $\pi(\cdot\mid s')$; đó là phương trình của $q_*$, không phải của $q_\pi$.
:::

### Bài tập 04.13. Liên hệ giữa giá trị tối ưu và chính sách tối ưu

**Mức độ:** nhận biết; mục tiêu học tập 2 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.25–3.28, §3.6, trang 67.

::: exercise Bài tập 04.13 (Liên hệ giữa giá trị tối ưu và chính sách tối ưu)
Xét MDP hữu hạn với mô hình bốn đối số $p(s',r\mid s,a)$, $0\le\gamma<1$, giá trị tối ưu $v_*$, giá trị hành động tối ưu $q_*$ và quy ước $v_*(s_{\mathrm{term}})=0$.

- (a) Viết $v_*$ theo $q_*$.
- (b) Viết $q_*$ theo $v_*$ và $p$.
- (c) Viết một chính sách tối ưu $\pi_*$ theo $q_*$.
- (d) Viết một chính sách tối ưu $\pi_*$ theo $v_*$ và $p$.
:::

::: hint Gợi ý Bài tập 04.13
Câu (a) và (b) là Định lý 04.25(c) và Định nghĩa 04.19. Câu (c) và (d) dùng Định lý 04.25(b): chính sách tham lam theo $v_*$ là tối ưu.
:::

::: solution Lời giải Bài tập 04.13
**Câu (a).** Theo Định lý 04.25(c), với mọi $s\in\mathcal S$,
$$
v_*(s)=\max_{a\in\mathcal A(s)}q_*(s,a).
$$

**Câu (b).** Theo Định nghĩa 04.19, với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$,
$$
\begin{aligned}
&q_*(s,a)\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma v_*(s')\bigr].
\end{aligned}
$$

**Câu (c).** Chọn tại mỗi $s$ một hành động
$$
\pi_*(s)\in\arg\max_{a\in\mathcal A(s)}q_*(s,a).
$$
Theo câu (b), $q_*(s,a)=Q_{v_*}(s,a)$, nên $\pi_*$ là chính sách tham lam theo $v_*$ và tối ưu theo Định lý 04.25(b). Khi tập $\arg\max$ có nhiều phần tử, mọi cách chọn đều tối ưu; một chính sách ngẫu nhiên tối ưu khi và chỉ khi nó chỉ đặt xác suất dương lên các hành động trong tập này (Bài tập 04.9(b)).

**Câu (d).** Thế câu (b) vào câu (c):
$$
\begin{aligned}
&\pi_*(s)\in\arg\max_{a\in\mathcal A(s)}\\
&\quad\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma v_*(s')\bigr].
\end{aligned}
$$
Đây là phép nhìn trước một bước theo $v_*$, nên cần mô hình $p$; câu (c) chọn hành động chỉ từ bảng $q_*$, không cần $p$.

**Kiểm tra lại.** Trên mô hình hai trạng thái của ghi chú (Ví dụ 04.11, Định lý 04.25), $q_*(\mathrm s_0,\cdot)=(25{,}3;\,27)$ và $q_*(\mathrm s_1,\cdot)=(26{,}3;\,30)$, nên câu (a) cho $v_*=(27,30)$ và câu (c) cho $\pi_*=(\mathrm b,\mathrm b)$. Lỗi thường gặp: viết $\pi_*(s)=\arg\max_aq_*(s,a)$ như một đẳng thức, trong khi $\arg\max$ là một tập và có thể có nhiều phần tử.
:::

### Bài tập 04.14. Lặp giá trị cho giá trị hành động

**Mức độ:** nhận biết; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.10, §4.4, trang 84; đẳng thức (4.10) của sách, trang 83.

::: exercise Bài tập 04.14 (Lặp giá trị cho giá trị hành động)
Lặp giá trị trên bảng giá trị trạng thái dùng quy tắc (4.10) của sách, tức (4.1) của ghi chú, với mọi $s\in\mathcal S$:
$$
\begin{aligned}
&V_{k+1}(s)\\
&\quad=\max_{a\in\mathcal A(s)}\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma V_k(s')\bigr].
\end{aligned}
$$
Viết quy tắc tương ứng $Q_{k+1}(s,a)$ cho bảng giá trị hành động, với $s\in\mathcal S$, $a\in\mathcal A(s)$.
:::

::: hint Gợi ý Bài tập 04.14
Trong quy tắc trên, phép cực đại chọn hành động đầu tiên. Với bảng giá trị hành động, hành động đầu tiên đã được ấn định; phép cực đại chuyển sang hành động tại trạng thái kế tiếp.
:::

::: solution Lời giải Bài tập 04.14
Với quy ước $\max_{a'}Q_k(s_{\mathrm{term}},a')=0$,
$$
\begin{aligned}
&Q_{k+1}(s,a)\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\Bigl[r\\
&\qquad+\gamma\max_{a'\in\mathcal A(s')}Q_k(s',a')\Bigr].
\end{aligned}
$$

Quy tắc này là lặp giá trị trên bảng trạng thái, viết lại. Đặt $V_k(s)=\max_aQ_k(s,a)$. Khi đó $Q_{k+1}=Q_{V_k}$ theo (2.1), và
$$
\begin{aligned}
V_{k+1}(s)&=\max_aQ_{k+1}(s,a)\\
&=\max_aQ_{V_k}(s,a)\\
&=(T_*V_k)(s).
\end{aligned}
$$
Theo Hệ quả 04.26, $V_k\to v_*$ khi $\gamma<1$. Lấy hiệu của $Q_{k+1}=Q_{V_k}$ và $q_*=Q_{v_*}$ (Định nghĩa 04.19), phần thưởng triệt tiêu, nên $\lvert Q_{k+1}(s,a)-q_*(s,a)\rvert\le\gamma\lVert V_k-v_*\rVert_\infty\to0$. Điểm bất động của quy tắc là phương trình Bellman tối ưu cho giá trị hành động của Định lý 04.25(c).

**Kiểm tra lại.** Nếu mỗi $\mathcal A(s')$ chỉ có một hành động, phép cực đại biến mất và quy tắc trùng lượt quét cho $q_\pi$ của Bài tập 04.12 với chính sách duy nhất. Lỗi thường gặp: đặt phép cực đại ngoài tổng theo $(s',r)$, viết $\max_{a'}\sum_{s',r}\cdots$; khi đó hành động tại bước sau được chọn trước khi biết trạng thái kế tiếp, và mỗi trạng thái kế tiếp không còn hành động tốt nhất riêng của nó.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 04.15. Thêm một trạng thái vào lưới 4×4

**Mức độ:** tính toán; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.2, §4.1, trang 76; dữ kiện của Ví dụ 4.1, trang 76, và Hình 4.1, trang 77.

::: exercise Bài tập 04.15 (Thêm một trạng thái vào lưới 4×4)
Dùng lưới $4\times4$ của Bài tập 04.11: các trạng thái chưa kết thúc $1,\dots,14$, bốn hành động xác định, đi ra ngoài lưới thì đứng yên, phần thưởng $-1$ mọi chuyển, $\gamma=1$, chính sách $\pi$ ngẫu nhiên đều, với giá trị

| | cột 1 | cột 2 | cột 3 | cột 4 |
|---|---:|---:|---:|---:|
| hàng 1 | $0$ | $-14$ | $-20$ | $-22$ |
| hàng 2 | $-14$ | $-18$ | $-20$ | $-20$ |
| hàng 3 | $-20$ | $-20$ | $-18$ | $-14$ |
| hàng 4 | $-22$ | $-20$ | $-14$ | $0$ |

Hàng 4 gồm, từ trái sang, $12$, $13$, $14$ và ô kết thúc. Thêm trạng thái $15$ ngay dưới $13$. Tại $15$, các hành động trái, lên, phải, xuống đưa tác tử tới $12$, $13$, $14$, $15$.

- (a) Các chuyển từ những trạng thái cũ giữ nguyên. Tính $v_\pi(15)$.
- (b) Đổi thêm động lực tại $13$: hành động xuống từ $13$ đưa tác tử tới $15$. Tính $v_\pi(15)$ trong trường hợp này.
:::

::: hint Gợi ý Bài tập 04.15
Ở (a), không trạng thái cũ nào đi tới $15$, nên phương trình của chúng không đổi. Ở (b), phương trình của $13$ chứa $v_\pi(15)$; thử giữ $v_\pi(13)=-20$ rồi kiểm cả hai phương trình.
:::

::: solution Lời giải Bài tập 04.15
**Câu (a).** Phương trình $v_\pi=T_\pi v_\pi$ của các trạng thái cũ không chứa $15$, nên bảng cũ vẫn là nghiệm của chúng. Phương trình tại $15$ là
$$
\begin{aligned}
&v_\pi(15)\\
&=-1+\tfrac14\bigl[v_\pi(12)+v_\pi(13)\\
&\quad+v_\pi(14)+v_\pi(15)\bigr]\\
&=-1+\tfrac14\bigl[-56+v_\pi(15)\bigr].
\end{aligned}
$$
Nhân hai vế với $4$: $3\,v_\pi(15)=-60$, nên $v_\pi(15)=-20$.

**Câu (b).** Chỉ phương trình của $13$ thay đổi: hành động xuống từ $13$ trước đây giữ nguyên $13$, nay đưa tới $15$. Phương trình mới là
$$
\begin{aligned}
&v_\pi(13)\\
&\quad=-1+\tfrac14\bigl[v_\pi(9)+v_\pi(12)\\
&\qquad+v_\pi(14)+v_\pi(15)\bigr].
\end{aligned}
$$
Thế bảng cũ cùng $v_\pi(15)=-20$: vế phải bằng $-1+\tfrac14(-20-22-14-20)=-1-19=-20=v_\pi(13)$. Phương trình tại $15$ không đổi so với câu (a) và vẫn đúng với $v_\pi(13)=-20$, $v_\pi(15)=-20$. Mọi phương trình khác không chứa $15$ và không đổi. Vậy bảng cũ cùng $v_\pi(15)=-20$ thỏa toàn bộ hệ.

Dưới chính sách ngẫu nhiên đều, từ mọi trạng thái có một đường tới ô kết thúc với xác suất dương sau không quá $3$ bước, nên mọi lượt kết thúc với xác suất $1$, và $v_\pi$ là nghiệm duy nhất của hệ (Sutton và Barto, 2018, §4.1, trang 74). Do đó $v_\pi(15)=-20$ trong cả hai trường hợp.

**Kiểm tra lại.** Ở (b), hành động xuống từ $13$ trước đây cho giá trị nhìn trước $-1+v_\pi(13)=-21$, nay cho $-1+v_\pi(15)=-21$: hai số bằng nhau, nên trung bình tại $13$ không đổi. Lỗi thường gặp: giải phương trình tại $15$ với vế phải chỉ gồm ba ô kề $12$, $13$, $14$, bỏ hành động xuống giữ nguyên $15$.
:::

### Bài tập 04.16. Chính sách tối ưu phụ thuộc hệ số chiết khấu

**Mức độ:** tính toán; mục tiêu học tập 1 và 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.22, §3.6, trang 66.

::: exercise Bài tập 04.16 (Chính sách tối ưu phụ thuộc hệ số chiết khấu)
Xét MDP tiếp diễn có ba trạng thái $\mathrm x_0$, $\mathrm x_1$, $\mathrm x_2$, mọi chuyển xác định. Chỉ trạng thái $\mathrm x_0$ có lựa chọn, giữa hai hành động $\mathrm{trai}$ và $\mathrm{phai}$; mỗi trạng thái còn lại có một hành động.

| Trạng thái | Hành động | Trạng thái kế tiếp | Phần thưởng |
|---|---|---|---:|
| $\mathrm x_0$ | $\mathrm{trai}$ | $\mathrm x_1$ | $+1$ |
| $\mathrm x_0$ | $\mathrm{phai}$ | $\mathrm x_2$ | $0$ |
| $\mathrm x_1$ | (duy nhất) | $\mathrm x_0$ | $0$ |
| $\mathrm x_2$ | (duy nhất) | $\mathrm x_0$ | $+2$ |

Có đúng hai chính sách xác định, $\pi_{\mathrm{trai}}$ và $\pi_{\mathrm{phai}}$. Xác định chính sách tối ưu khi $\gamma=0$, khi $\gamma=0{,}9$ và khi $\gamma=0{,}5$.
:::

::: hint Gợi ý Bài tập 04.16
Viết hệ $v=T_\pi v$ của từng chính sách và giải theo $v(\mathrm x_0)$. Mỗi chính sách lặp lại một chu kỳ hai bước từ $\mathrm x_0$.
:::

::: solution Lời giải Bài tập 04.16
**Giá trị của hai chính sách.** Với $\pi_{\mathrm{trai}}$, hệ (1.2) là $v(\mathrm x_0)=1+\gamma v(\mathrm x_1)$, $v(\mathrm x_1)=\gamma v(\mathrm x_0)$, $v(\mathrm x_2)=2+\gamma v(\mathrm x_0)$. Thế phương trình thứ hai vào phương trình thứ nhất: $v(\mathrm x_0)=1+\gamma^2v(\mathrm x_0)$. Với $\pi_{\mathrm{phai}}$, $v(\mathrm x_0)=\gamma v(\mathrm x_2)$ và $v(\mathrm x_2)=2+\gamma v(\mathrm x_0)$ cho $v(\mathrm x_0)=2\gamma+\gamma^2v(\mathrm x_0)$. Với $0\le\gamma<1$,
$$
\begin{aligned}
v_{\pi_{\mathrm{trai}}}(\mathrm x_0)&=\frac{1}{1-\gamma^2},\\
v_{\pi_{\mathrm{phai}}}(\mathrm x_0)&=\frac{2\gamma}{1-\gamma^2}.
\end{aligned}
$$
Ở cả hai chính sách, $v(\mathrm x_1)=\gamma v(\mathrm x_0)$ và $v(\mathrm x_2)=2+\gamma v(\mathrm x_0)$, nên chính sách có $v(\mathrm x_0)$ lớn hơn cũng không kém tại $\mathrm x_1$ và $\mathrm x_2$. Hai giá trị tại $\mathrm x_0$ có cùng mẫu số, nên chỉ cần so $1$ với $2\gamma$.

| $\gamma$ | $v_{\pi_{\mathrm{trai}}}(\mathrm x_0)$ | $v_{\pi_{\mathrm{phai}}}(\mathrm x_0)$ | Chính sách tối ưu |
|---|---:|---:|---|
| $0$ | $1$ | $0$ | $\pi_{\mathrm{trai}}$ |
| $0{,}9$ | $1/0{,}19\approx5{,}263$ | $1{,}8/0{,}19\approx9{,}474$ | $\pi_{\mathrm{phai}}$ |
| $0{,}5$ | $4/3$ | $4/3$ | cả hai |

Theo Định lý 04.25, có một chính sách Markov dừng, xác định tối ưu trên mọi chính sách; MDP này chỉ có hai chính sách như vậy, nên chính sách có giá trị lớn hơn ở mọi trạng thái là tối ưu. Khi $\gamma=0$, tác tử chỉ tính phần thưởng ngay sau hành động, nên chọn $+1$. Khi $\gamma=0{,}9$, phần thưởng $+2$ nhận sau một bước có giá trị hiện tại $1{,}8>1$. Khi $\gamma=0{,}5$, $2\gamma=1$: hai chính sách có cùng giá trị $(4/3;\,2/3;\,8/3)$ tại $(\mathrm x_0,\mathrm x_1,\mathrm x_2)$, cả hai đều tối ưu, và quy tắc phá hòa của Định nghĩa 04.12 quyết định chính sách mà lặp chính sách trả về.

**Kiểm tra lại.** Với $\gamma=0{,}9$, từ $v_{\pi_{\mathrm{phai}}}$: $v(\mathrm x_1)=0{,}9\cdot9{,}474\approx8{,}526$ và $v(\mathrm x_2)=2+0{,}9\cdot9{,}474\approx10{,}526$. Hai giá trị nhìn trước tại $\mathrm x_0$ là $1+0{,}9\cdot8{,}526\approx8{,}674$ cho $\mathrm{trai}$ và $0+0{,}9\cdot10{,}526\approx9{,}474$ cho $\mathrm{phai}$; cực đại bằng $v(\mathrm x_0)$, đúng phương trình (3.1). Lỗi thường gặp: chỉ so phần thưởng của bước đầu, $+1$ với $0$, và kết luận $\pi_{\mathrm{trai}}$ tối ưu với mọi $\gamma$.
:::

### Bài tập 04.17. Giá trị tối ưu của ô A trên lưới 5×5

**Mức độ:** tính toán; mục tiêu học tập 1 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.24, §3.6, trang 67; dữ kiện của Ví dụ 3.5, trang 60, và Hình 3.5, trang 65. Câu (b) là phép tính trên cùng dữ kiện.

::: exercise Bài tập 04.17 (Giá trị tối ưu của ô A trên lưới 5×5)
Lưới $5\times5$ có các ô $(i,j)$, hàng $i=0,\dots,4$ tính từ trên xuống, cột $j=0,\dots,4$ tính từ trái sang. Tại mỗi ô có bốn hành động bắc, nam, đông, tây, chuyển xác định sang ô kề. Hành động đưa ra ngoài lưới giữ nguyên ô và cho phần thưởng $-1$. Từ ô $\mathrm A=(0,1)$, mọi hành động cho phần thưởng $+10$ và đưa tác tử tới $\mathrm A'=(4,1)$; từ ô $\mathrm B=(0,3)$, mọi hành động cho $+5$ và đưa tới $\mathrm B'=(2,3)$. Mọi chuyển khác cho phần thưởng $0$. Nhiệm vụ là tiếp diễn với $\gamma=0{,}9$. Theo Hình 3.5 của sách, một chính sách tối ưu đi về phía bắc tại $(4,1)$, $(3,1)$, $(2,1)$, $(1,1)$, và giá trị tối ưu, làm tròn một chữ số thập phân, là

| | $j=0$ | $j=1$ | $j=2$ | $j=3$ | $j=4$ |
|---|---:|---:|---:|---:|---:|
| $i=0$ | $22{,}0$ | $24{,}4$ | $22{,}0$ | $19{,}4$ | $17{,}5$ |
| $i=1$ | $19{,}8$ | $22{,}0$ | $19{,}8$ | $17{,}8$ | $16{,}0$ |
| $i=2$ | $17{,}8$ | $19{,}8$ | $17{,}8$ | $16{,}0$ | $14{,}4$ |
| $i=3$ | $16{,}0$ | $17{,}8$ | $16{,}0$ | $14{,}4$ | $13{,}0$ |
| $i=4$ | $14{,}4$ | $16{,}0$ | $14{,}4$ | $13{,}0$ | $11{,}7$ |

- (a) Dùng chính sách tối ưu và $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$ để viết $v_*(\mathrm A)$ dưới dạng biểu thức, rồi tính tới ba chữ số thập phân.
- (b) Lặp giá trị đồng bộ chạy từ $V_0=0$. Dùng kết quả (a) và bảng trên, tính $\lVert V_0-v_*\rVert_\infty$, tìm số lượt quét $k$ nhỏ nhất để chặn của Hệ quả 04.26 không vượt $\kappa=0{,}1$, và nêu ngưỡng $\theta$ của Hệ quả 04.27 ứng với $\kappa=0{,}1$.
:::

::: hint Gợi ý Bài tập 04.17
Từ $\mathrm A$, quỹ đạo theo chính sách tối ưu lặp lại một chu kỳ: một bước nhảy tới $\mathrm A'$ rồi bốn bước về $\mathrm A$. Ở (b), $\lVert V_0-v_*\rVert_\infty=\max_s\lvert v_*(s)\rvert$.
:::

::: solution Lời giải Bài tập 04.17
**Câu (a).** Từ $\mathrm A$, bước đầu cho $R_1=+10$ và đưa tác tử tới $\mathrm A'=(4,1)$. Bốn bước về phía bắc qua $(3,1)$, $(2,1)$, $(1,1)$ tới $(0,1)=\mathrm A$ không đi ra ngoài lưới và không qua $\mathrm A$, $\mathrm B$ trước bước cuối, nên $R_2=\dots=R_5=0$. Sau đó chu kỳ năm bước lặp lại, nên
$$
\begin{aligned}
v_*(\mathrm A)&=10+\gamma^5v_*(\mathrm A),\\
v_*(\mathrm A)&=\frac{10}{1-\gamma^5}\\
&=\frac{10}{1-0{,}59049}\\
&=\frac{10}{0{,}40951}\approx24{,}419 .
\end{aligned}
$$

**Câu (b).** Mọi giá trị trong bảng dương và lớn nhất tại $\mathrm A$, nên $\lVert V_0-v_*\rVert_\infty=v_*(\mathrm A)\approx24{,}419$. Hệ quả 04.26 cho $\lVert V_k-v_*\rVert_\infty\le24{,}419\cdot0{,}9^k$. Điều kiện $24{,}419\cdot0{,}9^k\le0{,}1$ tương đương
$$
\begin{aligned}
k&\ge\frac{\ln(24{,}419/0{,}1)}{\ln(1/0{,}9)}\\
&=\frac{\ln244{,}19}{0{,}10536}\\
&\approx\frac{5{,}498}{0{,}10536}\approx52{,}2 .
\end{aligned}
$$
Kiểm hai giá trị kề: $24{,}419\cdot0{,}9^{52}\approx0{,}102>0{,}1$ và $24{,}419\cdot0{,}9^{53}\approx0{,}092\le0{,}1$, nên $k=53$. Hệ quả 04.27 cho ngưỡng $\theta=(1-0{,}9)\cdot0{,}1=0{,}01$: khi $\Delta_*(V)\le0{,}01$, bảng $V$ có sai số không quá $0{,}1$, mà không cần biết $v_*$.

**Kiểm tra lại.** Theo chính sách tối ưu, từ $\mathrm A'$ tác tử đi bốn bước về phía bắc với phần thưởng $0$ tới $\mathrm A$, nên $v_*(\mathrm A')=\gamma^4v_*(\mathrm A)=0{,}6561\cdot24{,}419\approx16{,}02$, khớp số $16{,}0$ ở ô $(4,1)$ của bảng. Lỗi thường gặp: dùng $24{,}4$ đã làm tròn trong bảng thay cho biểu thức $10/(1-\gamma^5)$, khi đó không có đủ ba chữ số thập phân.
:::

### Bài tập 04.18. Sửa giả mã lặp chính sách để bảo đảm dừng

**Mức độ:** chứng minh; mục tiêu học tập 2 và 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.4, §4.3, trang 82; giả mã lặp chính sách, trang 80.

::: exercise Bài tập 04.18 (Sửa giả mã lặp chính sách để bảo đảm dừng)
Sách trình bày lặp chính sách (dùng đánh giá chính sách lặp) như sau, với ngưỡng nhỏ $\theta>0$.

1. Khởi tạo: $V(s)\in\mathbb R$ và $\pi(s)\in\mathcal A(s)$ tùy ý với mọi $s\in\mathcal S$; $V(s_{\mathrm{term}})=0$.
2. Đánh giá chính sách: lặp lại các lượt quét; trong mỗi lượt, với mỗi $s\in\mathcal S$, gán $V(s)\leftarrow\sum_{s',r}p(s',r\mid s,\pi(s))\bigl[r+\gamma V(s')\bigr]$ tại chỗ; dừng khi thay đổi lớn nhất trong lượt nhỏ hơn $\theta$.
3. Cải thiện chính sách: đặt cờ ổn định là đúng. Với mỗi $s\in\mathcal S$: ghi $a_{\mathrm{cu}}\leftarrow\pi(s)$; gán $\pi(s)\leftarrow\arg\max_a\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr]$; nếu $a_{\mathrm{cu}}\ne\pi(s)$ thì đặt cờ ổn định là sai. Nếu cờ ổn định đúng, dừng và trả $V\approx v_*$, $\pi\approx\pi_*$; nếu không, quay lại bước 2.

Giả mã này có thể không bao giờ dừng nếu chính sách cứ đổi qua lại giữa hai hay nhiều chính sách tốt như nhau. Sửa giả mã để bảo đảm dừng.
:::

::: hint Gợi ý Bài tập 04.18
Lỗi nằm ở phép gán $\pi(s)\leftarrow\arg\max_a(\cdot)$ khi tập $\arg\max$ có nhiều phần tử. So bước 3 với Thuật toán 04.14 và quy tắc phá hòa của Định nghĩa 04.12; chứng minh dừng theo lập luận của Mệnh đề 04.18.
:::

::: solution Lời giải Bài tập 04.18
**Chỗ lỗi.** Khi tập $\arg\max$ tại $s$ có hai hành động, phép gán ở bước 3 có thể chọn hành động khác $a_{\mathrm{cu}}$ dù $a_{\mathrm{cu}}$ cũng đạt cực đại. Cờ ổn định khi đó bị đặt là sai mà giá trị không tăng ở đâu cả, và vòng sau có thể đổi trở lại; dãy chính sách đi vòng giữa các chính sách cùng giá trị.

**Giả mã đã sửa.** Thay bước 3 bằng: đặt cờ ổn định là đúng; với mỗi $s\in\mathcal S$, tính $Q(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr]$ cho mọi $a\in\mathcal A(s)$; **nếu $Q(s,\pi(s))<\max_aQ(s,a)$** thì gán $\pi(s)$ là phần tử đầu tiên của $\arg\max_aQ(s,a)$ theo một thứ tự cố định trên $\mathcal A(s)$ và đặt cờ ổn định là sai; nếu không, giữ $\pi(s)$. Đây là Thuật toán 04.14 với quy tắc phá hòa của Định nghĩa 04.12.

**Chứng minh dừng.** Giả sử bước 2 trả đúng $v_\pi$, như Thuật toán 04.17. Mỗi lần cờ ổn định bị đặt là sai, chính sách mới $\pi'$ khác $\pi$ chỉ tại các trạng thái mà $q_\pi(s,\pi(s))<\max_aq_\pi(s,a)$, nên (2.2) nghiêm ngặt tại các trạng thái đó; theo Định lý 04.13(a)–(c), $v_{\pi'}\ge v_\pi$ và lớn hơn nghiêm ngặt ở ít nhất một trạng thái. Như Bước 2 của chứng minh Mệnh đề 04.18, không chính sách nào lặp lại trong dãy; có $\prod_s\lvert\mathcal A(s)\rvert$ chính sách xác định, nên thuật toán dừng sau không quá chừng đó vòng. Khi dừng, $\pi(s)\in\arg\max_aq_\pi(s,a)$ tại mọi $s$, tức $\pi$ ổn định (Định nghĩa 04.16) và tối ưu (Định lý 04.25(d)).

**Trong thực hành.** Bước 2 của sách dừng ở ngưỡng $\theta$, nên $V$ chỉ xấp xỉ $v_\pi$, và hai giá trị bằng nhau về lý thuyết có thể lệch nhau do làm tròn. Cài đặt khi đó so với một dung sai nhỏ: giữ $\pi(s)$ khi $Q(s,\pi(s))\ge\max_aQ(s,a)-\epsilon$, như bài thực hành CartPole dùng $\epsilon=10^{-9}$. Chứng minh trên cần đánh giá chính xác và không bao phủ trường hợp này.

**Kiểm tra lại.** Trên MDP của Bài tập 04.16 với $\gamma=0{,}5$, hai hành động tại $\mathrm x_0$ có cùng giá trị nhìn trước $4/3$ theo giá trị của bất kỳ chính sách nào trong hai chính sách. Giả mã gốc có thể đổi $\pi(\mathrm x_0)$ ở mọi vòng; giả mã đã sửa giữ $\pi(\mathrm x_0)$ và dừng ngay ở vòng đầu.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 04.19. Lặp chính sách trên giá trị hành động

**Mức độ:** vận dụng; mục tiêu học tập 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.5, §4.3, trang 82; giả mã lặp chính sách, trang 80.

::: exercise Bài tập 04.19 (Lặp chính sách trên giá trị hành động)
Lặp chính sách của Thuật toán 04.17 (và giả mã của sách ở trang 80, chép ở Bài tập 04.18) tính $v_*$ bằng cách xen kẽ đánh giá $v_\pi$ và cải thiện tham lam theo $v_\pi$, trên MDP hữu hạn với mô hình $p(s',r\mid s,a)$ và $0\le\gamma<1$. Định nghĩa lặp chính sách cho giá trị hành động: viết một thuật toán đầy đủ tính $q_*$, tương tự thuật toán tính $v_*$, kèm điều kiện dừng, và giải thích vì sao thuật toán dừng tại $q_*$.
:::

::: hint Gợi ý Bài tập 04.19
Với chính sách xác định $\pi$, $v_\pi(s)=q_\pi(s,\pi(s))$ và $q_\pi=Q_{v_\pi}$. Bước đánh giá dùng phương trình Bellman của $q_\pi$ (Bài tập 04.12); bước cải thiện chọn $\arg\max_aq_\pi(s,a)$ với quy tắc phá hòa.
:::

::: solution Lời giải Bài tập 04.19
**Thuật toán.** Đầu vào: mô hình $p$, $\gamma\in[0,1)$, chính sách xác định $\pi_0$, một thứ tự cố định trên mỗi $\mathcal A(s)$. Quy ước $Q(s_{\mathrm{term}},\cdot)=0$.

1. Khởi tạo: $\pi\leftarrow\pi_0$.
2. Đánh giá chính sách: tìm bảng $Q$ trên mọi cặp $(s,a)$ thỏa
$$
\begin{aligned}
&Q(s,a)\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma Q(s',\pi(s'))\bigr]
\end{aligned}
$$
với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$, bằng cách giải hệ tuyến tính này, hoặc bằng các lượt quét $Q_{k+1}(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma Q_k(s',\pi(s'))\bigr]$ tới khi thay đổi lớn nhất đủ nhỏ, xuất phát từ bảng của vòng trước.
3. Cải thiện chính sách: đặt cờ ổn định là đúng. Với mỗi $s\in\mathcal S$, nếu $Q(s,\pi(s))<\max_aQ(s,a)$ thì gán $\pi(s)$ là phần tử đầu tiên của $\arg\max_aQ(s,a)$ theo thứ tự cố định và đặt cờ ổn định là sai.
4. Nếu cờ ổn định đúng, trả $Q$ và $\pi$; nếu không, quay lại bước 2.

**Vì sao đúng.** Giả sử bước 2 cho đúng nghiệm của hệ, như Thuật toán 04.17 giả sử đánh giá chính xác. Với $\pi$ xác định, nghiệm của bước 2 là $q_\pi$ (Bài tập 04.12 với $\pi(a'\mid s')=1$ khi $a'=\pi(s')$), và hệ có nghiệm duy nhất vì phép lặp ở bước 2 co hệ số $\gamma$ theo chuẩn cực đại trên các cặp. Vì $q_\pi=Q_{v_\pi}$ (Mệnh đề 03.22), bước 3 chọn đúng các hành động mà Thuật toán 04.14 chọn từ $v_\pi$. Do đó dãy chính sách trùng dãy của Thuật toán 04.17, và theo Mệnh đề 04.18, thuật toán dừng sau không quá $\prod_s\lvert\mathcal A(s)\rvert$ vòng tại một chính sách ổn định $\pi$. Theo Định lý 04.25(d), $\pi$ tối ưu, nên $v_\pi=v_*$ và $Q=q_\pi=Q_{v_*}=q_*$ (Định nghĩa 04.19).

**So với thuật toán tính $v_*$.** Bảng có $\sum_s\lvert\mathcal A(s)\rvert\le nm$ ô thay cho $n$ ô. Bước 2 vẫn cần mô hình $p$; một lượt quét với $\pi$ xác định có $nm$ ô, mỗi ô tổng trên tối đa $n$ trạng thái kế tiếp, nên tốn $O(n^2m)$ với mô hình đặc, bằng chi phí của Thuật toán 04.14. Bước 3 chỉ đọc bảng $Q$, tốn $O(nm)$ và không cần $p$, khác bước cải thiện theo $v_\pi$, nơi mỗi giá trị nhìn trước phải tính lại bằng (2.1).

**Kiểm tra lại.** Trên mô hình hai trạng thái của ghi chú với $\pi_0=(\mathrm a,\mathrm a)$, bước 2 cho $Q(\mathrm s_0,\cdot)=(10;\,9{,}9)$ và $Q(\mathrm s_1,\cdot)=(11;\,12{,}9)$, đúng các giá trị nhìn trước của Ví dụ 04.9, và bước 3 cho $(\mathrm a,\mathrm b)$ như Ví dụ 04.9. Lỗi thường gặp: ở bước 2 dùng $\max_{a'}Q(s',a')$ thay cho $Q(s',\pi(s'))$; khi đó bước 2 là lặp giá trị cho $q_*$ (Bài tập 04.14), không còn là đánh giá chính sách.
:::

### Bài tập 04.20. Hình dạng chính sách tối ưu của bài toán người đánh bạc

**Mức độ:** vận dụng; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.8, §4.4, trang 84; dữ kiện của Ví dụ 4.3 và Hình 4.3, trang 84.

::: exercise Bài tập 04.20 (Hình dạng chính sách tối ưu của bài toán người đánh bạc)
Một người đánh bạc đặt cược vào kết quả của các lần tung đồng xu. Khi đồng xu ra mặt ngửa, với xác suất $p_h=0{,}4$, người đó thắng số tiền bằng tiền cược; khi ra mặt sấp, người đó mất tiền cược. Ván kết thúc khi vốn đạt $100$ hoặc về $0$. Trạng thái là vốn $s\in\{1,\dots,99\}$, hành động là tiền cược nguyên $a\in\{0,1,\dots,\min(s,100-s)\}$. Phần thưởng bằng $+1$ ở chuyển đưa vốn tới $100$ và bằng $0$ ở mọi chuyển khác; $\gamma=1$. Khi đó $v_*(s)$ là xác suất đạt $100$ từ vốn $s$ dưới chính sách tối ưu. Hình 4.3 của sách vẽ một chính sách tối ưu: cược toàn bộ $50$ khi vốn là $50$, nhưng chỉ cược $1$ khi vốn là $51$; chính sách tối ưu không duy nhất.

Giải thích hình dạng của chính sách tối ưu: vì sao tại vốn $50$ người đó cược hết trong một lần tung, còn tại vốn $51$ thì không, và vì sao đó là một chính sách tốt.
:::

::: hint Gợi ý Bài tập 04.20
Với $p_h<0{,}5$, mỗi lần cược $a$ làm kỳ vọng của vốn giảm $(1-2p_h)a$. So giá trị nhìn trước của các mức cược tại vốn $50$ và $51$, dùng bảng $v_*$ tính bằng lặp giá trị ở Bài tập 04.21.
:::

::: solution Lời giải Bài tập 04.20
Mọi số dưới đây dùng $v_*$ tính bằng lặp giá trị (Bài tập 04.21) và đối chiếu với nghiệm hữu tỉ chính xác của hệ $v=T_\pi v$ cho chính sách cược $\min(s,100-s)$; chính sách này thỏa phương trình Bellman tối ưu tại mọi vốn. Một số giá trị: $v_*(2)\approx0{,}005164$, $v_*(25)=0{,}16$, $v_*(49)\approx0{,}376222$, $v_*(50)=0{,}4$, $v_*(51)\approx0{,}403098$, $v_*(52)\approx0{,}407746$, $v_*(75)=0{,}64$.

**Ít lần cược là có lợi.** Với $p_h=0{,}4$, một lần cược $a$ đổi vốn thành $s+a$ với xác suất $0{,}4$ và $s-a$ với xác suất $0{,}6$, nên kỳ vọng của vốn giảm $0{,}2a$. Một cách trực quan, mỗi lần tung đều bất lợi cho người đánh bạc, nên chính sách cược $\min(s,100-s)$ tới đích bằng ít lần tung nhất; chính sách này đạt $v_*$ tại mọi vốn. Tại các mốc $25$, $50$, $75$, một lần cược đưa vốn đúng tới một mốc khác hoặc tới $100$: $v_*(50)=0{,}4$, $v_*(25)=0{,}4^2=0{,}16$, $v_*(75)=0{,}4+0{,}6\cdot0{,}4=0{,}64$.

**Tại vốn $50$.** Cược $50$ cho giá trị nhìn trước $0{,}4\cdot1+0{,}6\cdot0=0{,}4=v_*(50)$. Mọi mức cược dương nhỏ hơn cho giá trị nhỏ hơn; mức tốt nhất trong số đó là $a=1$, với $0{,}4\,v_*(51)+0{,}6\,v_*(49)\approx0{,}161239+0{,}225733=0{,}386972<0{,}4$, và $a=49$ cho cùng giá trị. Mức cược $0$ cũng cho $0{,}4$ nhưng không làm ván tiến lên (xem phần kiểm tra lại). Vậy trong các mức cược dương, cược hết là hành động tối ưu duy nhất tại $50$.

**Tại vốn $51$.** Hai mức cược cho cùng giá trị. Với $a=49$:
$$
\begin{aligned}
&0{,}4\cdot1+0{,}6\,v_*(2)\\
&\quad\approx0{,}4+0{,}003098\\
&\quad=0{,}403098 .
\end{aligned}
$$
Với $a=1$:
$$
\begin{aligned}
&0{,}4\,v_*(52)+0{,}6\,v_*(50)\\
&\quad\approx0{,}163098+0{,}24\\
&\quad=0{,}403098 .
\end{aligned}
$$
Cả hai bằng $v_*(51)$, nên cả hai tối ưu. Cược $1$ là chính sách tốt vì vốn không xuống dưới $50$: nếu thua, người đánh bạc về đúng $50$, nơi còn nguyên cơ hội thắng $0{,}4$ bằng một lần cược hết; nếu thắng, vốn lên $52$. Khoản dư $1$ trên mốc $50$ được dùng để thử tiến lên mà không mất cơ hội ở mốc đó. Cược $49$ cho cùng xác suất thắng theo một đường khác: thắng ngay với xác suất $0{,}4$, hoặc về vốn $2$.

**Họ chính sách tối ưu.** Tính trên nghiệm chính xác, tập $\arg\max_{a\ge1}$ có ít nhất hai phần tử tại $72$ trên $99$ mức vốn. Một chính sách $\pi$ chỉ dùng mức cược dương kết thúc với xác suất $1$: mỗi lần ra mặt ngửa tăng vốn ít nhất $1$, nên từ mọi vốn, $99$ lần ra mặt ngửa liên tiếp kết thúc ván; biến cố này có xác suất ít nhất $p_h^{99}>0$ trong mỗi khối $99$ lần tung, nên ván kết thúc với xác suất $1$. Khi đó $v_\pi$ là nghiệm duy nhất của $v=T_\pi v$ (Sutton và Barto, 2018, §4.1, trang 74). Nếu tại mỗi vốn $\pi$ chọn một phần tử của tập cực đại thì $T_\pi v_*=v_*$, nên $v_\pi=v_*$. Vậy mỗi cách chọn như vậy cho một chính sách tối ưu, và chính sách tối ưu không duy nhất. Chọn mức cược dương nhỏ nhất trong tập cực đại cho cược $50$ tại $50$ và cược $1$ tại $51$, như Hình 4.3; hình răng cưa của đồ thị chính sách đến từ quy tắc chọn trong tập hòa này.

**Kiểm tra lại.** Mức cược $0$ luôn cho giá trị nhìn trước $0{,}4\,v_*(s)+0{,}6\,v_*(s)=v_*(s)$, nên cũng thuộc tập cực đại; nhưng chính sách luôn cược $0$ không bao giờ kết thúc và có giá trị $0$. Với $\gamma=1$, Định lý 04.25(b) không áp dụng, nên một chính sách tham lam theo $v_*$ chưa chắc tối ưu; phép trích chính sách phải bỏ mức cược $0$. Lỗi thường gặp: kết luận "tại $51$ phải cược $1$" từ Hình 4.3, trong khi cược $49$ cũng tối ưu.
:::

### Bài tập 04.21. Lặp giá trị cho bài toán người đánh bạc [Lập trình]

**Mức độ:** vận dụng; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 4.9, §4.4, trang 84; dữ kiện của Ví dụ 4.3 và Hình 4.3, trang 84.

::: exercise Bài tập 04.21 (Lặp giá trị cho bài toán người đánh bạc)
Dùng bài toán người đánh bạc của Bài tập 04.20: vốn $s\in\{1,\dots,99\}$, tiền cược $a\in\{0,1,\dots,\min(s,100-s)\}$, mặt ngửa với xác suất $p_h$ thì vốn tăng $a$, mặt sấp thì vốn giảm $a$, phần thưởng $+1$ khi vốn đạt $100$ và $0$ ở mọi chuyển khác, $\gamma=1$. Cài đặt lặp giá trị và giải bài toán với $p_h=0{,}25$ và $p_h=0{,}55$. Khi lập trình, có thể thêm hai trạng thái giả ứng với kết thúc ở vốn $0$ và $100$, với giá trị $0$ và $1$. Trình bày kết quả bằng đồ thị như Hình 4.3 của sách: giá trị theo vốn và chính sách cuối cùng theo vốn. Xác định kết quả có ổn định khi $\theta\to0$ hay không.
:::

::: hint Gợi ý Bài tập 04.21
Với $V(0)=0$ và $V(100)=1$ cố định, phần thưởng $+1$ đã nằm trong $V(100)$, nên $Q_V(s,a)=p_h\,V(s+a)+(1-p_h)\,V(s-a)$. Khi trích chính sách, chỉ xét $a\ge1$ (Bài tập 04.20, phần kiểm tra lại), và so chính sách trích ra ở nhiều giá trị $\theta$.
:::

::: solution Lời giải Bài tập 04.21
**Cài đặt.** Dùng Thuật toán 04.28 trên mảng $V$ gồm $101$ phần tử $V(0),\dots,V(100)$, với $V(0)=0$, $V(100)=1$ giữ cố định và $V(s)=0$ ban đầu tại $s=1,\dots,99$. Mỗi lượt quét giữ $V$ cố định, tính
$$
\begin{aligned}
&Q_V(s,a)=p_h\,V(s+a)\\
&\qquad+(1-p_h)\,V(s-a),\\
&W(s)=\max_aQ_V(s,a)
\end{aligned}
$$
với $s=1,\dots,99$, cực đại lấy trên $0\le a\le\min(s,100-s)$; đặt $\Delta=\max_s\lvert W(s)-V(s)\rvert$, dừng khi $\Delta\le\theta$, nếu không thì gán $V\leftarrow W$. Chính sách trích ra chọn mức cược dương nhỏ nhất đạt cực đại của $Q_V(s,\cdot)$ trên $a\ge1$.

**Kết quả với $p_h=0{,}25$.** Giá trị tại một số mức vốn:

| $s$ | $1$ | $2$ | $10$ | $25$ | $50$ | $51$ | $75$ | $99$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| $v_*(s)$ | $0{,}000073$ | $0{,}000291$ | $0{,}007085$ | $0{,}0625$ | $0{,}25$ | $0{,}250219$ | $0{,}4375$ | $0{,}837972$ |

Tại các mốc, $v_*(25)=p_h^2$, $v_*(50)=p_h$, $v_*(75)=p_h+(1-p_h)p_h$. Đồ thị giá trị tăng mạnh ngay trước các mốc $25$, $50$, $75$ và gần như phẳng ngay sau mỗi mốc, chẳng hạn $v_*(49)\approx0{,}19599$, $v_*(50)=0{,}25$, $v_*(51)\approx0{,}25022$; đồ thị chính sách có cùng hình răng cưa như Hình 4.3: cược $50$ tại $50$, cược $25$ tại $25$ và $75$, cược $1$ tại $51$. Lý do như Bài tập 04.20: với $p_h<0{,}5$, mỗi lần cược bất lợi, nên chính sách tối ưu dùng ít lần cược.

**Kết quả với $p_h=0{,}55$.** Lặp giá trị hội tụ về
$$
v_*(s)=\frac{1-(9/11)^s}{1-(9/11)^{100}},
$$
với $9/11=(1-p_h)/p_h$; chẳng hạn $v_*(1)\approx0{,}181818$, $v_*(2)\approx0{,}330579$, $v_*(10)\approx0{,}865569$, $v_*(25)\approx0{,}993374$, $v_*(50)\approx0{,}999956$. Đồ thị giá trị là đường lõm, tăng nhanh rồi tiến sát $1$. Chính sách trích ra cược $1$ tại mọi vốn; tính trên công thức chính xác, $a=1$ là mức cược dương duy nhất đạt cực đại tại mọi $s$, và công thức thỏa phương trình Bellman tối ưu. Với $p_h>0{,}5$, mỗi lần cược có lợi về kỳ vọng, nên chính sách tối ưu cược nhỏ để có nhiều lần tung.

**Độ ổn định khi $\theta\to0$.** Chạy lại với $\theta=10^{-4},10^{-6},\dots,10^{-12}$:

- Bảng giá trị ổn định. Với $p_h=0{,}25$, sai số so với nghiệm chính xác giảm cùng $\theta$, chẳng hạn khoảng $7{,}4\cdot10^{-5}$ khi $\theta=10^{-4}$. Vì $\gamma=1$, Hệ quả 04.27 không cho chặn $\Delta/(1-\gamma)$; với $p_h=0{,}55$ và $\theta=10^{-12}$, sai số còn khoảng $1{,}8\cdot10^{-10}$, lớn hơn $\theta$.
- Với $p_h=0{,}55$, chính sách trích ra là cược $1$ ở mọi vốn với mọi $\theta\le10^{-4}$.
- Với $p_h=0{,}25$, chính sách trích ra đổi tại một số mức vốn khi $\theta$ giảm, vì tại $72$ trên $99$ mức vốn có ít nhất hai mức cược cùng đạt cực đại (Bài tập 04.20). Sai số làm tròn và sai số lặp quyết định mức cược nào trong tập hòa có giá trị tính được lớn nhất. Mọi mức cược được chọn vẫn thuộc tập cực đại chính xác. Chính sách trích ra chỉ dùng mức cược dương, nên theo lập luận ở phần "Họ chính sách tối ưu" của Bài tập 04.20, mọi chính sách trích ra đều tối ưu; chỉ phần tử được chọn trong tập hòa thay đổi.

Muốn chính sách trích ra ổn định, so các giá trị nhìn trước với một dung sai, như bài thực hành CartPole: coi mọi $a$ thỏa $Q_V(s,a)\ge\max_{a'}Q_V(s,a')-\epsilon$ là đạt cực đại, rồi chọn theo một thứ tự cố định.

**Kiểm tra lại.** Với $p_h=0{,}55$, công thức thỏa $v_*(s)=0{,}55\,v_*(s+1)+0{,}45\,v_*(s-1)$, vì $r=9/11$ là nghiệm của $0{,}55r^2-r+0{,}45=0$. Lỗi thường gặp: để $a=0$ trong phép trích chính sách; vì $Q_V(s,0)=V(s)$ và tại điểm bất động $V(s)$ bằng cực đại, phép $\arg\max$ có thể trả $a=0$, cho một chính sách không bao giờ kết thúc.
:::

## Tài liệu tham khảo

- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 3.22, §3.6, trang 66 (Bài tập 04.16); Bài tập 3.24, §3.6, trang 67, Ví dụ 3.5, trang 60, và Hình 3.5, trang 65 (Bài tập 04.17); Bài tập 3.25–3.28, §3.6, trang 67 (Bài tập 04.13); Bài tập 4.1–4.3, §4.1, trang 76, Ví dụ 4.1 và Hình 4.1, trang 76–77, và §4.1, trang 74 (Bài tập 04.11, 04.15, 04.12); Bài tập 4.4, 4.5, §4.3, trang 82, và giả mã lặp chính sách, trang 80 (Bài tập 04.18, 04.19); Bài tập 4.8–4.10, §4.4, trang 84, Ví dụ 4.3 và Hình 4.3, trang 84, và (4.10), trang 83 (Bài tập 04.20, 04.21, 04.14).
