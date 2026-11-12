# Bài tập Bài 05 — Dự đoán phi mô hình

Tệp gồm tám bài, Bài tập 05.17–05.24, lấy từ bài tập của Sutton và Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, chương 2, 5 và 6; số trang là trang in của sách. Số hiệu nối tiếp Bài tập 05.1–05.16 của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html); các bài của ghi chú không chép lại ở đây. Các bài xếp theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Không bài nào trùng bài tập trên trang chiếu.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/1/1) | ghi chú: 05.1 |
| 2. Lợi tức và ước lượng Monte Carlo | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/2/1) | 05.17, 05.18, 05.19; ghi chú: 05.2–05.5 |
| 3. Sai phân thời gian TD(0) | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/3/1) | 05.20, 05.21; ghi chú: 05.6, 05.7, 05.16 |
| 4. Độ chệch, phương sai và hội tụ | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/4/1) | 05.22, 05.24; ghi chú: 05.8–05.11, 05.14 |
| 5. Dữ liệu cố định và cập nhật theo lô | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/5/1) | ghi chú: 05.12 |
| 6. Tổng kết và chuyển tiếp | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/6/1) | 05.23; ghi chú: 05.13, 05.15 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 05. Một chính sách Markov dừng $\pi$ được giữ cố định; môi trường là quá trình quyết định Markov (Markov decision process, MDP) dừng mà tác tử không biết. $R_{t+1}$ là phần thưởng của chuyển từ thời điểm $t$ sang $t+1$; $T$ là thời điểm kết thúc của lượt, $G_T=0$, và lợi tức là $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}=R_{t+1}+\gamma G_{t+1}$. Giá trị của mọi trạng thái kết thúc bằng $0$, cả với $v_\pi$ lẫn với bảng ước lượng $V$. Mục tiêu TD là $Y_t=R_{t+1}+\gamma V(S_{t+1})$, sai số TD là $\delta_t=Y_t-V(S_t)$, mục tiêu một bước lý tưởng là $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$, và độ chệch của mục tiêu $Y$ tại $s$ là $\operatorname{bias}(Y;s)=\mathbb E_\pi[Y\mid S_t=s]-v_\pi(s)$ với bảng giữ cố định (Định nghĩa 05.24). Số thập phân viết với dấu phẩy.

**Đi dạo ngẫu nhiên** (random walk; Sutton và Barto, 2018, Ví dụ 6.2, trang 125). Dữ kiện dùng ở Bài tập 05.20, 05.22 và 05.24, được nêu lại trong từng bài:

- năm trạng thái không kết thúc $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ xếp từ trái sang phải, với một trạng thái kết thúc bên trái $\mathrm A$ và một trạng thái kết thúc bên phải $\mathrm E$;
- mọi lượt bắt đầu ở $\mathrm C$; mỗi bước sang trái hoặc sang phải một ô với xác suất $1/2$;
- phần thưởng $+1$ khi lượt kết thúc bên phải, $0$ cho mọi chuyển khác; $\gamma=1$;
- giá trị thật là $v_\pi(\mathrm A),\ldots,v_\pi(\mathrm E)=1/6,2/6,3/6,4/6,5/6$;
- bảng TD(0) được khởi tạo $V(s)=0{,}5$ tại mọi trạng thái không kết thúc.

## Mức nhận biết

### Bài tập 05.17. Hai quy tắc lần ghé trong trò blackjack

**Mức độ:** nhận biết. Mục tiêu học tập 2 của ghi chú bài giảng; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 5.2, §5.1, trang 94; dữ kiện của Ví dụ 5.1, trang 93. Câu (a) tách từ lời giải của câu hỏi gốc.

::: exercise Bài tập 05.17 (Hai quy tắc lần ghé trong trò blackjack)
Trò blackjack của Sutton và Barto (2018, Ví dụ 5.1) là một MDP hữu hạn có lượt, mỗi ván là một lượt:

- lá hình tính $10$; át tính $1$ hoặc $11$; bộ bài coi như vô hạn, tức rút có hoàn lại;
- người chơi rút thêm từng lá (hit) hoặc dừng (stick); tổng vượt $21$ thì thua ngay;
- trạng thái gồm tổng điểm của người chơi ($12$–$21$), lá ngửa của nhà cái (át–$10$) và việc người chơi có giữ một át dùng được (usable ace) hay không, tổng cộng $200$ trạng thái; át dùng được là át tính $11$ mà tổng không vượt $21$, và khi có át như vậy thì nó luôn được tính $11$;
- phần thưởng $+1$, $-1$, $0$ khi thắng, thua, hòa, nhận ở cuối ván; mọi phần thưởng giữa ván bằng $0$; $\gamma=1$;
- chính sách cần đánh giá dừng khi tổng bằng $20$ hoặc $21$, ngược lại rút thêm.

Sách ước lượng $v_\pi$ bằng Monte Carlo lần ghé đầu tiên trên nhiều ván mô phỏng.

- (a) Chứng minh rằng trong một ván, không trạng thái nào xuất hiện hai lần.
- (b) Nếu dùng Monte Carlo mọi lần ghé thay cho lần ghé đầu tiên trên cùng các ván, kết quả có khác nhiều không? Giải thích bằng Định nghĩa 05.6.
:::

::: hint Gợi ý Bài tập 05.17
Theo dõi cặp (có át dùng được hay không, tổng điểm) qua mỗi lần rút. Xét riêng trường hợp lá mới làm tổng vượt $21$ khi đang có át dùng được.
:::

::: solution Lời giải Bài tập 05.17
**Câu (a).** Lá ngửa của nhà cái không đổi trong ván, nên chỉ cần theo dõi tổng $s$ và biến $u$, bằng $1$ khi có át dùng được và $0$ khi không. Giữa hai trạng thái liên tiếp, người chơi rút một lá có giá trị $c\in\{1,\ldots,10\}$, với át tính $c=1$. Có ba trường hợp:

- $u=1$ và $s+c\le21$: trạng thái mới là $(s+c,u=1)$, tổng tăng thực sự;
- $u=1$ và $s+c>21$: át chuyển sang tính $1$, trạng thái mới là $(s+c-10,u=0)$, với $12\le s+c-10\le21$ vì $22\le s+c\le31$;
- $u=0$: một át mới không thể tính $11$, vì $s+11\ge23$; nếu không thua, trạng thái mới là $(s+c,u=0)$, tổng tăng thực sự.

Như vậy $u$ không bao giờ tăng, và khi $u$ giữ nguyên thì tổng tăng thực sự. Mỗi lần rút hoặc làm $u$ giảm, hoặc giữ $u$ và làm $s$ tăng, nên không cặp $(s,u)$ nào lặp lại trong một ván.

**Câu (b).** Theo câu (a), số lần ghé $N_e(s)$ của mỗi trạng thái trong một ván bằng $0$ hoặc $1$. Theo Định nghĩa 05.6, khi $N_e(s)\le1$, quy tắc lần ghé đầu tiên và quy tắc mọi lần ghé chọn cùng một mẫu từ ván đó. Trên cùng các ván, hai quy tắc cho cùng tập mẫu tại mọi trạng thái, nên với cùng quy tắc bước học, hai bảng ước lượng trùng nhau hoàn toàn.

**Kiểm tra lại.** Từ $(13,u=1)$, rút lá $10$ cho $(13,u=0)$: tổng trở về $13$ nhưng trạng thái đã khác vì $u$ đổi. Lỗi thường gặp là chỉ nhìn tổng điểm rồi kết luận trạng thái có thể lặp lại.
:::

### Bài tập 05.18. Một trạng thái tự chuyển: hai ước lượng từ một lượt

**Mức độ:** nhận biết (câu (a)); tính toán (câu (b), (c)). Mục tiêu học tập 2 và 3 của ghi chú bài giảng; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 5.5, §5.5, trang 105. Câu (b) và (c) là phép tính thêm trên dữ kiện của bài.

::: exercise Bài tập 05.18 (Một trạng thái tự chuyển: hai ước lượng từ một lượt)
Một MDP có một trạng thái không kết thúc $s$ và một hành động. Từ $s$, với xác suất $p$ tác tử quay về $s$, với xác suất $1-p$ chuyển sang trạng thái kết thúc, trong đó $0\le p<1$. Mọi chuyển có phần thưởng $+1$; $\gamma=1$. Tác tử quan sát một lượt dài $10$ bước, với lợi tức $10$.

- (a) Tính ước lượng lần ghé đầu tiên và ước lượng mọi lần ghé của $v_\pi(s)$ từ riêng lượt này.
- (b) Tính $v_\pi(s)$ theo $p$ bằng phương trình Bellman kỳ vọng.
- (c) Gọi $N$ là số bước của một lượt. Tính theo $p$ kỳ vọng của mẫu lần ghé đầu tiên và kỳ vọng của trung bình các mẫu mọi lần ghé trong một lượt, rồi so mỗi kỳ vọng với $v_\pi(s)$.
:::

::: hint Gợi ý Bài tập 05.18
Lượt dài $N$ bước ghé $s$ tại $t=0,\ldots,N-1$, và $G_t=N-t$. Số bước $N$ có $\Pr(N=m)=p^{m-1}(1-p)$ với $m\ge1$.
:::

::: solution Lời giải Bài tập 05.18
**Câu (a).** Lượt ghé $s$ tại $t=0,1,\ldots,9$ và kết thúc tại $T=10$; mỗi bước có phần thưởng $1$, nên $G_t=10-t$. Lần ghé đầu tiên cho một mẫu $G_0=10$, nên ước lượng là $10$. Mọi lần ghé cho mười mẫu $10,9,\ldots,1$, với trung bình

$$
\frac{10+9+\cdots+1}{10}=\frac{55}{10}=5{,}5 .
$$

**Câu (b).** Phương trình Bellman kỳ vọng tại $s$ là $v_\pi(s)=p\bigl(1+v_\pi(s)\bigr)+(1-p)(1+0)=1+p\,v_\pi(s)$, nên

$$
v_\pi(s)=\frac1{1-p}.
$$

**Câu (c).** Mẫu lần ghé đầu tiên của một lượt là $G_0=N$, với $\mathbb E[N]=\sum_{m\ge1}m\,p^{m-1}(1-p)=1/(1-p)=v_\pi(s)$, đúng như Mệnh đề 05.7 với $k=1$. Trung bình các mẫu mọi lần ghé trong một lượt là

$$
\frac1N\sum_{t=0}^{N-1}(N-t)=\frac{N+1}2,
$$

có kỳ vọng

$$
\begin{aligned}
&\frac12\Bigl(\frac1{1-p}+1\Bigr)=\frac{2-p}{2(1-p)}\\
&\quad=v_\pi(s)-\frac{p}{2(1-p)} .
\end{aligned}
$$

Khi $p>0$, trung bình mọi lần ghé của một lượt chệch xuống một lượng $p/(2(1-p))$, như trạng thái $\mathrm C$ của Nhận xét 05.18. Với lượt ở câu (a), $(N+1)/2=5{,}5$, khớp con số đã tính.

**Kiểm tra lại.** Định lý 05.17 vẫn cho ước lượng mọi lần ghé qua nhiều lượt hội tụ về $v_\pi(s)$. Tổng các mẫu của một lượt là $Z=N(N+1)/2$; với $\mathbb E[N^2]=\operatorname{Var}(N)+(\mathbb E[N])^2=(1+p)/(1-p)^2$, ta có $\mathbb E[Z]=\bigl(\mathbb E[N^2]+\mathbb E[N]\bigr)/2=1/(1-p)^2$, và $\mathbb E[Z]/\mathbb E[N]=1/(1-p)=v_\pi(s)$. Lỗi thường gặp: lấy $G_t=10-t-1$ vì quên phần thưởng của chuyển vào trạng thái kết thúc; hoặc coi độ chệch của một lượt là bằng chứng mọi lần ghé không hội tụ.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 05.19. Trọng số của các mẫu khi bước học thay đổi

**Mức độ:** chứng minh. Mục tiêu học tập 3 của ghi chú bài giảng; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 2.4, §2.5, trang 33. Câu (b) và (c) là phép kiểm thêm trên công thức của bài.

::: exercise Bài tập 05.19 (Trọng số của các mẫu khi bước học thay đổi)
Với $n\ge1$, một ước lượng được cập nhật theo quy tắc

$$
Q_{n+1}=Q_n+\alpha_n\bigl[R_n-Q_n\bigr],
$$

với giá trị đầu $Q_1$, các mẫu $R_1,R_2,\ldots$ và bước học $\alpha_n\in[0,1]$. Khi $\alpha_n=\alpha$ là hằng số, Sutton và Barto (2018, công thức (2.6), trang 32) cho

$$
\begin{aligned}
Q_{n+1}&=(1-\alpha)^nQ_1\\
&\quad+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}R_i .
\end{aligned}
$$

Trong ký hiệu của ghi chú, $R_i$ là mẫu lợi tức $g_i$ và $Q_{n+1}$ là ước lượng $V_n$ sau $n$ mẫu.

- (a) Với dãy $\alpha_n$ tùy ý, viết $Q_{n+1}$ thành tổng có trọng số của $Q_1,R_1,\ldots,R_n$, và chứng minh công thức.
- (b) Kiểm tra rằng công thức ở (a) cho lại (2.6) khi $\alpha_n=\alpha$, và cho trung bình mẫu $\frac1n\sum_{i=1}^nR_i$ khi $\alpha_n=1/n$.
- (c) Chứng minh tổng các trọng số ở (a) bằng $1$.
:::

::: hint Gợi ý Bài tập 05.19
Viết quy tắc thành $Q_{n+1}=(1-\alpha_n)Q_n+\alpha_nR_n$ rồi quy nạp theo $n$. Quy ước tích rỗng bằng $1$.
:::

::: solution Lời giải Bài tập 05.19
**Câu (a).** Ta chứng minh với mọi $n\ge1$,

$$
Q_{n+1}=w_0^{(n)}Q_1+\sum_{i=1}^nw_i^{(n)}R_i ,
$$

với các trọng số

$$
\begin{aligned}
w_0^{(n)}&=\prod_{k=1}^n(1-\alpha_k),\\
w_i^{(n)}&=\alpha_i\prod_{k=i+1}^n(1-\alpha_k),
\end{aligned}
$$

trong đó tích rỗng (khi $i=n$) bằng $1$.

*Cơ sở $n=1$.* $Q_2=(1-\alpha_1)Q_1+\alpha_1R_1$, tức $w_0^{(1)}=1-\alpha_1$ và $w_1^{(1)}=\alpha_1$.

*Bước quy nạp.* Giả sử công thức đúng với $n$. Thế vào $Q_{n+2}=(1-\alpha_{n+1})Q_{n+1}+\alpha_{n+1}R_{n+1}$: mỗi trọng số $w_0^{(n)},\ldots,w_n^{(n)}$ nhân thêm thừa số $1-\alpha_{n+1}$, nên tích trong đó kéo dài tới $k=n+1$ và cho đúng $w_0^{(n+1)},\ldots,w_n^{(n+1)}$; mẫu mới $R_{n+1}$ nhận trọng số $\alpha_{n+1}=w_{n+1}^{(n+1)}$, với tích rỗng bằng $1$. Vậy công thức đúng với $n+1$.

**Câu (b).** Khi $\alpha_k=\alpha$, $\prod_{k=1}^n(1-\alpha)=(1-\alpha)^n$ và $\alpha\prod_{k=i+1}^n(1-\alpha)=\alpha(1-\alpha)^{n-i}$, đúng (2.6). Khi $\alpha_k=1/k$, thừa số $k=1$ bằng $1-1=0$, nên $Q_1$ có trọng số $0$; với mẫu $R_i$,

$$
\frac1i\prod_{k=i+1}^n\frac{k-1}k=\frac1i\cdot\frac in=\frac1n ,
$$

nên $Q_{n+1}=\frac1n\sum_{i=1}^nR_i$, đúng Mệnh đề 05.9.

**Câu (c).** Lấy $Q_1=1$ và $R_i=1$ với mọi $i$: quy tắc cho $Q_{n+1}=Q_n+\alpha_n(1-Q_n)$, nên từ $Q_1=1$ ta có $Q_n=1$ với mọi $n$. Thế vào công thức ở (a), vế phải là tổng các trọng số, nên tổng này bằng $1$. Khi $\alpha_k\in[0,1]$, mọi trọng số không âm, nên $Q_{n+1}$ là một trung bình có trọng số.

**Kiểm tra lại.** Với $n=2$, $\alpha_1=0{,}5$, $\alpha_2=0{,}2$: $Q_3=0{,}4\,Q_1+0{,}4\,R_1+0{,}2\,R_2$, và $0{,}4+0{,}4+0{,}2=1$. Lỗi thường gặp là bắt đầu tích tại $k=i$ thay vì $k=i+1$, làm trọng số của $R_n$ thành $\alpha_n(1-\alpha_n)$ thay vì $\alpha_n$.
:::

### Bài tập 05.20. Lượt đầu tiên của TD(0) trên đi dạo ngẫu nhiên

**Mức độ:** tính toán. Mục tiêu học tập 4 của ghi chú bài giảng; mạch 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.3, §6.2, trang 126; dữ kiện của Ví dụ 6.2, trang 125. Câu (d) là phép tính thêm trên cùng dữ kiện.

::: exercise Bài tập 05.20 (Lượt đầu tiên của TD(0) trên đi dạo ngẫu nhiên)
Đi dạo ngẫu nhiên có năm trạng thái không kết thúc $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ từ trái sang phải, một trạng thái kết thúc bên trái $\mathrm A$ và một bên phải $\mathrm E$. Mọi lượt bắt đầu ở $\mathrm C$; mỗi bước sang trái hoặc sang phải một ô với xác suất $1/2$. Phần thưởng $+1$ khi lượt kết thúc bên phải, $0$ cho mọi chuyển khác; $\gamma=1$. TD(0) dùng bước hằng $\alpha=0{,}1$, bảng khởi tạo $V(s)=0{,}5$ tại mọi trạng thái không kết thúc. Sau lượt đầu tiên, chỉ $V(\mathrm A)$ thay đổi.

- (a) Lượt đầu tiên đã kết thúc như thế nào?
- (b) Giải thích vì sao chỉ $V(\mathrm A)$ thay đổi.
- (c) Tính chính xác lượng thay đổi của $V(\mathrm A)$.
- (d) Nếu dùng Monte Carlo lần ghé đầu tiên với bước hằng $\alpha=0{,}1$ trên cùng lượt, những phần tử nào thay đổi, và thay đổi bao nhiêu?
:::

::: hint Gợi ý Bài tập 05.20
Tính sai số TD của một chuyển giữa hai trạng thái không kết thúc khi mọi giá trị đều bằng $0{,}5$, rồi của hai loại chuyển vào trạng thái kết thúc.
:::

::: solution Lời giải Bài tập 05.20
**Câu (b).** Khi mọi trạng thái không kết thúc có $V=0{,}5$, một chuyển giữa hai trạng thái không kết thúc có $\delta_t=0+1\cdot0{,}5-0{,}5=0$, nên không phần tử nào đổi và bảng vẫn bằng $0{,}5$ ở mọi trạng thái cho tới chuyển cuối của lượt. Chuyển cuối là chuyển vào trạng thái kết thúc, với giá trị tiếp nối $0$:

- từ $\mathrm E$ sang bên phải: $\delta_t=1+0-0{,}5=0{,}5$, chỉ $V(\mathrm E)$ đổi;
- từ $\mathrm A$ sang bên trái: $\delta_t=0+0-0{,}5=-0{,}5$, chỉ $V(\mathrm A)$ đổi.

Do đó chỉ một phần tử của bảng đổi sau lượt đầu, và đó là phần tử của trạng thái ngay trước trạng thái kết thúc.

**Câu (a).** Vì phần tử đổi là $V(\mathrm A)$, lượt đầu tiên kết thúc bên trái, bằng chuyển từ $\mathrm A$ vào trạng thái kết thúc, với lợi tức $0$.

**Câu (c).** $V(\mathrm A)$ thay đổi $\alpha\,\delta_t=0{,}1\cdot(-0{,}5)=-0{,}05$, từ $0{,}5$ xuống $0{,}45$.

**Câu (d).** Lượt kết thúc bên trái nên mọi lợi tức của lượt bằng $0$. Monte Carlo lần ghé đầu tiên cập nhật mọi trạng thái đã ghé, mỗi trạng thái một lần: $V(s)\leftarrow0{,}5+0{,}1\cdot(0-0{,}5)=0{,}45$. Lượt đi từ $\mathrm C$ tới bên trái nên đã ghé ít nhất $\mathrm C$, $\mathrm B$, $\mathrm A$; ba phần tử này, cùng $\mathrm D$, $\mathrm E$ nếu lượt có ghé, đều giảm $0{,}05$.

**Kiểm tra lại.** TD(0) đưa kết quả cuối lượt về trạng thái ngay trước trạng thái kết thúc, còn Monte Carlo đưa nó tới mọi trạng thái đã ghé, như ở Ví dụ 05.9 và 05.5 của ghi chú. Lỗi thường gặp: lấy giá trị tiếp nối của trạng thái kết thúc bằng $0{,}5$, cho $\delta_t=0$ ở chuyển cuối; hoặc cộng phần thưởng $+1$ cho lượt kết thúc bên trái.
:::

### Bài tập 05.21. Sai số Monte Carlo và sai số TD khi bảng thay đổi trong lượt

**Mức độ:** chứng minh. Mục tiêu học tập 4 và 5 của ghi chú bài giảng; mạch 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.1, §6.1, trang 121. Câu (b) áp dụng kết quả của câu (a) cho TD(0) dạng bảng.

::: exercise Bài tập 05.21 (Sai số Monte Carlo và sai số TD khi bảng thay đổi trong lượt)
Xét một lượt kết thúc tại $T$. Gọi $V_t$ là bảng dùng tại thời điểm $t$, cả trong sai số TD

$$
\delta_t=R_{t+1}+\gamma V_t(S_{t+1})-V_t(S_t)
$$

lẫn trong cập nhật TD(0) ở thời điểm $t$, với $V_t=0$ tại trạng thái kết thúc. Khi bảng giữ cố định trong cả lượt, $V_t=V$ với mọi $t$, sai số Monte Carlo là tổng các sai số TD (Bài tập 05.14 của ghi chú; Sutton và Barto, 2018, công thức (6.6)):

$$
G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k .
$$

- (a) Khi bảng thay đổi trong lượt, làm lại phép biến đổi trên để tìm lượng phải cộng thêm vào tổng các sai số TD cho bằng sai số Monte Carlo $G_t-V_t(S_t)$.
- (b) Với TD(0) dạng bảng, cập nhật ở thời điểm $k$ là $V_{k+1}(S_k)=V_k(S_k)+\alpha_k\delta_k$ và $V_{k+1}(s)=V_k(s)$ với $s\ne S_k$. Chứng minh rằng lượng thêm ở (a) chỉ có số hạng khác $0$ tại các tự chuyển $S_{k+1}=S_k$, và viết lượng đó theo $\alpha_k$, $\delta_k$.
:::

::: hint Gợi ý Bài tập 05.21
Trong bước $G_t-V_t(S_t)=\delta_t+\gamma\bigl[G_{t+1}-V_t(S_{t+1})\bigr]$, cộng và trừ $\gamma V_{t+1}(S_{t+1})$ để có sai số Monte Carlo ở thời điểm $t+1$.
:::

::: solution Lời giải Bài tập 05.21
**Câu (a).** Đặt $e_t=G_t-V_t(S_t)$ là sai số Monte Carlo và $c_k=V_{k+1}(S_{k+1})-V_k(S_{k+1})$ là thay đổi của giá trị tại $S_{k+1}$ do cập nhật ở thời điểm $k$. Với $t<T$, theo Mệnh đề 05.4 và định nghĩa của $\delta_t$,

$$
\begin{aligned}
e_t&=R_{t+1}+\gamma G_{t+1}-V_t(S_t)\\
&=\delta_t+\gamma\bigl[G_{t+1}-V_t(S_{t+1})\bigr]\\
&=\delta_t+\gamma c_t+\gamma e_{t+1}.
\end{aligned}
$$

Đẳng thức thứ hai cộng và trừ $\gamma V_t(S_{t+1})$; đẳng thức thứ ba cộng và trừ $\gamma V_{t+1}(S_{t+1})$. Lặp truy hồi từ $t$ tới $T-1$, với $e_T=G_T-V_T(S_T)=0$:

$$
\begin{aligned}
G_t-V_t(S_t)&=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k\\
&\quad+\sum_{k=t}^{T-1}\gamma^{k-t+1}c_k .
\end{aligned}
$$

Lượng phải cộng thêm là tổng thứ hai. Số hạng $k=T-1$ của nó bằng $0$, vì $S_T$ là trạng thái kết thúc và mọi bảng bằng $0$ tại đó. Khi bảng không đổi, mọi $c_k=0$ và ta được lại (6.6).

**Câu (b).** Cập nhật ở thời điểm $k$ chỉ đổi phần tử $S_k$. Nếu $S_{k+1}\ne S_k$ thì $V_{k+1}(S_{k+1})=V_k(S_{k+1})$ và $c_k=0$. Nếu $S_{k+1}=S_k$ thì $c_k=V_{k+1}(S_k)-V_k(S_k)=\alpha_k\delta_k$. Gọi $K$ là tập các $k$ với $t\le k\le T-1$ và $S_{k+1}=S_k$. Do đó

$$
\begin{aligned}
e_t&=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k\\
&\quad+\sum_{k\in K}\gamma^{k-t+1}\alpha_k\delta_k .
\end{aligned}
$$

Một lượt không có tự chuyển thỏa (6.6) đúng chính xác, dù TD(0) sửa bảng sau mỗi chuyển.

**Kiểm tra lại.** Ví dụ 05.10 của ghi chú chạy TD(0) với $\alpha=0{,}5$, $\gamma=1$ trên lượt $\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$, không có tự chuyển, từ bảng $V_0(\mathrm S)=0$. Các sai số TD là $0{,}5$, $-0{,}25$, $-1{,}25$, có tổng $-1$, bằng $G_0-V_0(\mathrm S)=-1-0$. Lỗi thường gặp là đồng nhất $V_t(S_{t+1})$ với $V_{t+1}(S_{t+1})$ khi rút gọn tổng, như khi bảng cố định, làm mất số hạng hiệu chỉnh ở tự chuyển.
:::

### Bài tập 05.22. Giá trị thật, độ chệch và phương sai trên đi dạo ngẫu nhiên

**Mức độ:** tính toán. Mục tiêu học tập 5 của ghi chú bài giảng; mạch 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.6, §6.2, trang 126; dữ kiện của Ví dụ 6.2, trang 125. Câu (b) thay câu hỏi gốc về cách tác giả đã dùng bằng câu hỏi cách nào cho giá trị đúng, cách nào cho giá trị xấp xỉ; câu (c) và (d) là phép tính thêm trên cùng dữ kiện.

::: exercise Bài tập 05.22 (Giá trị thật, độ chệch và phương sai trên đi dạo ngẫu nhiên)
Đi dạo ngẫu nhiên có năm trạng thái không kết thúc $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ từ trái sang phải, một trạng thái kết thúc bên trái $\mathrm A$ và một bên phải $\mathrm E$. Mọi lượt bắt đầu ở $\mathrm C$; mỗi bước sang trái hoặc sang phải một ô với xác suất $1/2$. Phần thưởng $+1$ khi lượt kết thúc bên phải, $0$ cho mọi chuyển khác; $\gamma=1$. Sutton và Barto nêu giá trị thật $v_\pi(\mathrm A),\ldots,v_\pi(\mathrm E)=1/6,2/6,3/6,4/6,5/6$.

- (a) Mô tả ít nhất hai cách tính các giá trị này.
- (b) Cách nào trong số đó cho đúng các phân số trên, cách nào chỉ cho giá trị xấp xỉ?
- (c) Giữ cố định bảng $V(s)=0{,}5$ tại mọi trạng thái không kết thúc. Tính độ chệch $\operatorname{bias}(Y;\mathrm A)$ và $\operatorname{bias}(Y;\mathrm C)$ của mục tiêu TD bằng Mệnh đề 05.25.
- (d) Tính $\operatorname{Var}(G_t\mid S_t=\mathrm C)$ và $\operatorname{Var}(Y^*\mid S_t=\mathrm C)$, rồi kiểm tra Định lý 05.28.
:::

::: hint Gợi ý Bài tập 05.22
Với $\gamma=1$ và phần thưởng duy nhất là $+1$ khi kết thúc bên phải, lợi tức bằng $1$ hoặc $0$. Ở (c), trạng thái kết thúc có $V=v_\pi=0$.
:::

::: solution Lời giải Bài tập 05.22
**Câu (a).** *Cách thứ nhất: giải hệ Bellman kỳ vọng.* Với $v_\pi$ viết gọn là $v$,

$$
\begin{aligned}
v(\mathrm A)&=\tfrac12\cdot0+\tfrac12v(\mathrm B),\\
v(s)&=\tfrac12v(s^-)+\tfrac12v(s^+),\\
v(\mathrm E)&=\tfrac12v(\mathrm D)+\tfrac12(1+0),
\end{aligned}
$$

trong đó dòng giữa ứng với $s=\mathrm B,\mathrm C,\mathrm D$, và $s^-$, $s^+$ là ô bên trái và bên phải của $s$. Đánh số trạng thái kết thúc trái là $0$, $\mathrm A,\ldots,\mathrm E$ là $1,\ldots,5$, trạng thái kết thúc phải là $6$, và đặt hai số phụ $u_0=0$, $u_6=1$; $u_6$ gộp phần thưởng $+1$ của chuyển vào trạng thái kết thúc phải, còn giá trị của trạng thái kết thúc vẫn bằng $0$. Hệ trở thành $u_j=\tfrac12(u_{j-1}+u_{j+1})$ với $j=1,\ldots,5$, nên $u_{j+1}-u_j$ không đổi theo $j$ và $u_j=j/6$.

*Cách thứ hai: xác suất kết thúc bên phải.* Vì $\gamma=1$ và phần thưởng khác $0$ duy nhất là $+1$ khi kết thúc bên phải, $G_t$ bằng $1$ khi lượt kết thúc bên phải và $0$ khi kết thúc bên trái, nên $v_\pi(s)$ là xác suất kết thúc bên phải khi xuất phát từ $s$. Xác suất này thỏa cùng hệ $u_j=\tfrac12(u_{j-1}+u_{j+1})$ với $u_0=0$, $u_6=1$, theo việc tách bước đầu.

*Cách thứ ba: lặp đánh giá chính sách* $V\leftarrow T_\pi V$ của Bài 04 từ một bảng bất kỳ. *Cách thứ tư: Monte Carlo*, lấy trung bình lợi tức của nhiều lượt mô phỏng từ mỗi trạng thái.

**Câu (b).** Hai cách đầu giải đúng hệ tuyến tính, nên cho chính xác $j/6$. Lặp đánh giá chính sách cho giá trị xấp xỉ sau mỗi số bước hữu hạn và hội tụ về $j/6$ khi số bước tăng, vì từ mọi trạng thái lượt kết thúc hầu chắc chắn (ghi chú, đoạn sau Định lý 05.30; Bertsekas và Tsitsiklis, 1996, chương 2). Monte Carlo cho một trung bình mẫu, có độ lệch chuẩn $\sigma(s)/\sqrt n$ sau $n$ lượt (Định lý 05.16). Các phân số đúng $1/6,\ldots,5/6$ nhận được từ hai cách đầu.

**Câu (c).** Theo Mệnh đề 05.25 với $\gamma=1$, $\operatorname{bias}(Y;s)=\mathbb E_\pi\bigl[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s\bigr]$. Từ $\mathrm A$, trạng thái kế tiếp là trạng thái kết thúc trái, với hiệu $0-0=0$, hoặc $\mathrm B$, với hiệu $0{,}5-2/6=1/6$:

$$
\operatorname{bias}(Y;\mathrm A)=\tfrac12\cdot0+\tfrac12\cdot\tfrac16=\tfrac1{12}.
$$

Từ $\mathrm C$, trạng thái kế tiếp là $\mathrm B$, với hiệu $1/6$, hoặc $\mathrm D$, với hiệu $0{,}5-4/6=-1/6$:

$$
\begin{aligned}
&\operatorname{bias}(Y;\mathrm C)\\
&\quad=\tfrac12\cdot\tfrac16-\tfrac12\cdot\tfrac16=0 .
\end{aligned}
$$

Tại $\mathrm C$, độ lệch của bảng ở hai trạng thái kế tiếp bù trừ nhau trong kỳ vọng, đúng trường hợp của Hệ quả 05.26(c), dù $V\ne v_\pi$ ở cả $\mathrm B$ và $\mathrm D$.

**Câu (d).** Từ $\mathrm C$, $G_t\in\{0,1\}$ với $\Pr(G_t=1)=v_\pi(\mathrm C)=1/2$, nên $\operatorname{Var}(G_t\mid S_t=\mathrm C)=\tfrac12\cdot\tfrac12=\tfrac14$. Mục tiêu lý tưởng là $Y^*=0+v_\pi(S_{t+1})$, bằng $2/6$ hoặc $4/6$ với xác suất $1/2$ mỗi giá trị, nên

$$
\begin{aligned}
&\operatorname{Var}(Y^*\mid S_t=\mathrm C)\\
&\quad=\tfrac12\cdot\tfrac12\cdot\Bigl(\tfrac46-\tfrac26\Bigr)^2=\tfrac1{36}.
\end{aligned}
$$

Ta có $1/36\le1/4$, khớp Định lý 05.28; phần do phần đuôi sau chuyển đầu là $1/4-1/36=2/9$, tức $8/9$ phương sai của $G_t$.

**Kiểm tra lại.** $\mathbb E[Y^*\mid S_t=\mathrm C]=\tfrac12\bigl(\tfrac26+\tfrac46\bigr)=\tfrac12=v_\pi(\mathrm C)$, và phương trình của $\mathrm E$: $\tfrac12\cdot\tfrac46+\tfrac12=\tfrac56$. Lỗi thường gặp: quên trạng thái kết thúc trái khi tính độ chệch tại $\mathrm A$, cho $1/6$ thay vì $1/12$; hoặc quên phần thưởng $+1$ trong phương trình của $\mathrm E$, cho $v(\mathrm E)=\tfrac12v(\mathrm D)$ và nghiệm $v\equiv0$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 05.23. Lái xe về nhà từ tòa nhà mới

**Mức độ:** vận dụng. Mục tiêu học tập 5 và 6 của ghi chú bài giảng; mạch 6.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.2, §6.1, trang 123; dữ kiện của Ví dụ 6.1, trang 122. Câu (a) là phép tính thêm trên dữ kiện của ví dụ.

::: exercise Bài tập 05.23 (Lái xe về nhà từ tòa nhà mới)
Mỗi ngày một người lái xe từ nơi làm việc về nhà và dự đoán thời gian còn lại. Trạng thái là một chặng của chuyến đi; phần thưởng của một chuyển là số phút của chặng vừa đi; $\gamma=1$, nên lợi tức tại một trạng thái là thời gian thực tế còn lại, và giá trị là thời gian còn lại kỳ vọng. Một chuyến đi ghi lại như sau, với $V$ là dự đoán thời gian còn lại tại mỗi trạng thái:

| Trạng thái | Thời gian đã đi (phút) | $V$: dự đoán thời gian còn lại (phút) |
| --- | --- | --- |
| rời văn phòng | $0$ | $30$ |
| tới xe, trời mưa | $5$ | $35$ |
| ra khỏi đường cao tốc | $20$ | $15$ |
| đường phụ, sau xe tải | $30$ | $10$ |
| vào phố nhà | $40$ | $3$ |
| về tới nhà | $43$ | $0$ |

- (a) Giữ cố định các dự đoán trong bảng. Tính sai số Monte Carlo $G_t-V(S_t)$ và sai số TD $\delta_t$ tại năm trạng thái không kết thúc, rồi kiểm tra đẳng thức của Bài tập 05.14 tại $t=0$.
- (b) Người này đã lái xe về nhà rất nhiều lần, rồi chuyển tới một tòa nhà mới với bãi đỗ xe mới, nhưng vẫn vào đường cao tốc ở chỗ cũ, và bắt đầu học dự đoán cho tòa nhà mới. Giải thích vì sao, ít nhất lúc đầu, cập nhật TD cho các trạng thái mới, xét trung bình, tốt hơn cập nhật Monte Carlo. Nêu giả thiết của lập luận.
- (c) Điều tương tự có thể xảy ra trong tình huống ban đầu, khi chưa chuyển chỗ làm, không? Trả lời kèm điều kiện.
:::

::: hint Gợi ý Bài tập 05.23
Ở (a), các phần thưởng là $5,15,10,10,3$. Ở (b), so độ chệch và phương sai của hai mục tiêu tại một trạng thái mới mà trạng thái kế tiếp đã có ước lượng tốt (Mệnh đề 05.25, Định lý 05.28).
:::

::: solution Lời giải Bài tập 05.23
**Câu (a).** Phần thưởng của năm chuyển là $(R_1,\ldots,R_5)=(5,15,10,10,3)$, nên lợi tức là $(G_0,\ldots,G_4)=(43,38,23,13,3)$. Với $V=(30,35,15,10,3)$ và $V=0$ tại "về tới nhà":

| $t$ | Trạng thái | $G_t-V(S_t)$ | $\delta_t=R_{t+1}+V(S_{t+1})-V(S_t)$ |
| --- | --- | --- | --- |
| $0$ | rời văn phòng | $43-30=13$ | $5+35-30=10$ |
| $1$ | tới xe, trời mưa | $38-35=3$ | $15+15-35=-5$ |
| $2$ | ra khỏi đường cao tốc | $23-15=8$ | $10+10-15=5$ |
| $3$ | đường phụ, sau xe tải | $13-10=3$ | $10+3-10=3$ |
| $4$ | vào phố nhà | $3-3=0$ | $3+0-3=0$ |

Tại $t=0$: $10-5+5+3+0=13=G_0-V(S_0)$, đúng đẳng thức của Bài tập 05.14 với $\gamma=1$.

**Câu (b).** Giả thiết: trạng thái là Markov, tức thời gian còn lại kỳ vọng từ chỗ vào đường cao tốc không phụ thuộc người lái xuất phát từ tòa nhà nào. Khi đó các trạng thái từ chỗ vào đường cao tốc trở đi là trạng thái cũ, đã được học qua nhiều chuyến, nên $V$ tại đó gần $v_\pi$. Xét một trạng thái mới $s$ mà trạng thái kế tiếp $s'$ là trạng thái cũ:

- mục tiêu TD là $R_{t+1}+V(s')$; theo Mệnh đề 05.25, độ chệch của nó là $\mathbb E_\pi[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s]$, gần $0$ vì $V$ gần $v_\pi$ ở trạng thái kế tiếp, và bằng $0$ khi $V=v_\pi$ ở mọi trạng thái kế tiếp (Hệ quả 05.26(b)); dao động của nó chỉ đến từ chặng đầu, như mục tiêu lý tưởng $Y^*$;
- mục tiêu Monte Carlo là thời gian thực tế còn lại $G_t$, không chệch nhưng chịu thêm dao động của mọi chặng sau (mưa, xe tải); theo Định lý 05.28, $\operatorname{Var}(Y^*\mid S_t=s)\le\operatorname{Var}(G_t\mid S_t=s)$.

Hai mục tiêu có kỳ vọng gần nhau, còn mục tiêu TD dao động ít hơn, nên với cùng bước học, cập nhật TD đưa $V(s)$ về gần $v_\pi(s)$ hơn cập nhật Monte Carlo, xét trung bình. Cập nhật TD còn có ngay sau chặng đầu, không phải chờ về tới nhà.

**Câu (c).** Có, tại những trạng thái mà ước lượng ở trạng thái kế tiếp đã gần giá trị thật, cụ thể khi $\operatorname{bias}(Y;s)^2+\operatorname{Var}(Y\mid S_t=s)<\operatorname{Var}(G_t\mid S_t=s)$ (Mệnh đề 05.25, Nhận xét 05.29): độ chệch của mục tiêu TD bằng độ lệch trung bình của bảng ở trạng thái kế tiếp, còn phần dao động mà nó bỏ qua là dao động của các chặng sau. Khi bảng ở trạng thái kế tiếp còn sai nhiều, mục tiêu TD chệch theo độ lệch đó, và Nhận xét 05.29 cho thấy nó có thể có sai số bình phương trung bình lớn hơn mục tiêu Monte Carlo.

**Kiểm tra lại.** Ở (a), tổng các sai số TD từ $t=2$ là $5+3+0=8=G_2-V(S_2)$. Lỗi thường gặp: lấy cột "thời gian đã đi" làm phần thưởng thay cho độ dài từng chặng; hoặc kết luận TD luôn tốt hơn Monte Carlo mà không nêu điều kiện về ước lượng ở trạng thái kế tiếp và tính Markov.
:::

### Bài tập 05.24. Sai số của TD tăng lại với bước học lớn

**Mức độ:** vận dụng. Mục tiêu học tập 5 của ghi chú bài giảng; mạch 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.5, §6.2, trang 126; dữ kiện của Ví dụ 6.2, trang 125. Câu (a) là phép tính thêm trên dữ kiện của ví dụ.

::: exercise Bài tập 05.24 (Sai số của TD tăng lại với bước học lớn)
Đi dạo ngẫu nhiên có năm trạng thái không kết thúc $\mathrm A,\mathrm B,\mathrm C,\mathrm D,\mathrm E$ từ trái sang phải, một trạng thái kết thúc bên trái $\mathrm A$ và một bên phải $\mathrm E$. Mọi lượt bắt đầu ở $\mathrm C$; mỗi bước sang trái hoặc sang phải một ô với xác suất $1/2$. Phần thưởng $+1$ khi lượt kết thúc bên phải, $0$ cho mọi chuyển khác; $\gamma=1$; giá trị thật $v_\pi(\mathrm A),\ldots,v_\pi(\mathrm E)=1/6,\ldots,5/6$. TD(0) chạy với bước hằng $\alpha\in\{0{,}05;\ 0{,}1;\ 0{,}15\}$, bảng khởi tạo $V(s)=0{,}5$ tại mọi trạng thái không kết thúc. Sai số được đo bằng căn bậc hai của trung bình bình phương (root mean square, RMS) của $V-v_\pi$ trên năm trạng thái, rồi lấy trung bình qua $100$ lần chạy, sau mỗi lượt trong $100$ lượt. Sutton và Barto ghi nhận rằng đường sai số RMS của TD giảm rồi tăng lại, rõ nhất ở các bước học lớn.

- (a) Tính sai số RMS của bảng khởi tạo.
- (b) Giải thích nguyên nhân sai số giảm rồi tăng lại, và vì sao hiện tượng rõ hơn khi $\alpha$ lớn.
- (c) Hiện tượng này có luôn xảy ra không, hay phụ thuộc cách khởi tạo bảng?
:::

::: hint Gợi ý Bài tập 05.24
Tại mỗi trạng thái, tách sai số bình phương trung bình qua các lần chạy thành bình phương độ chệch cộng phương sai, rồi xét mỗi phần thay đổi thế nào theo số lượt. Dùng kết quả của Bài tập 05.20(b) cho bảng còn phẳng.
:::

::: solution Lời giải Bài tập 05.24
**Câu (a).** Sai số của bảng khởi tạo tại $\mathrm A,\ldots,\mathrm E$ là $0{,}5-j/6$, tức $(1/3,\ 1/6,\ 0,\ -1/6,\ -1/3)$. Trung bình bình phương là $\bigl(\tfrac19+\tfrac1{36}+0+\tfrac1{36}+\tfrac19\bigr)/5=\tfrac1{18}$, nên sai số RMS ban đầu là $1/\sqrt{18}\approx0{,}236$.

**Câu (b).** Gọi $V_n(s)$ là giá trị tại $s$ sau $n$ lượt; $V_n(s)$ ngẫu nhiên vì mỗi lần chạy sinh các lượt khác nhau. Tại mỗi trạng thái, sai số bình phương trung bình qua các lần chạy tách thành hai phần:

$$
\begin{aligned}
&\mathbb E\bigl[(V_n(s)-v_\pi(s))^2\bigr]\\
&\quad=\bigl(\mathbb E[V_n(s)]-v_\pi(s)\bigr)^2\\
&\qquad+\operatorname{Var}\bigl(V_n(s)\bigr).
\end{aligned}
$$

*Phương sai.* Mọi lần chạy bắt đầu từ cùng bảng $V\equiv0{,}5$, nên phương sai ban đầu bằng $0$. Theo Bài tập 05.20(b), khi bảng còn phẳng, sai số TD của mọi chuyển giữa hai trạng thái không kết thúc bằng $0$; bảng chỉ bắt đầu thay đổi từ $\mathrm A$ và $\mathrm E$, rồi lan dần vào trong, nên phương sai tích lũy dần qua các lượt. Với bước hằng, phương sai không tiến về $0$: các giá trị dao động mãi theo kết quả của các lượt gần nhất (Sutton và Barto, 2018, trang 125). Trong trường hợp mẫu độc lập cùng phân phối của Nhận xét 05.19, mức giới hạn của phương sai là $\alpha\sigma^2/(2-\alpha)$, tăng theo $\alpha$.

*Độ chệch.* Phần độ chệch ban đầu nhỏ: $0$ tại $\mathrm C$, $1/6$ tại $\mathrm B$, $\mathrm D$, $1/3$ tại $\mathrm A$, $\mathrm E$. Mỗi cập nhật TD kéo bảng về phía $v_\pi$: với bảng đã biết, kỳ vọng của sai số TD tại $s$ là phần dư Bellman $(T_\pi V)(s)-V(s)$ (Mệnh đề 05.27). Do đó phần độ chệch giảm nhanh trong các lượt đầu.

Sai số là tổng của một phần ban đầu nhỏ và một phần tăng từ $0$, nên đường giảm rồi tăng mà sách ghi nhận có nghĩa như sau. Lúc đầu phần độ chệch giảm nhanh hơn phần phương sai tăng, nên sai số giảm; sau đó độ chệch không giảm thêm mà phương sai còn tăng, nên sai số tăng lại tới một mức dương. Với $\alpha$ lớn, mỗi cập nhật dịch bảng nhiều hơn nên độ chệch giảm nhanh hơn, và mức phương sai cao hơn, nên đoạn tăng lại rõ hơn.

**Câu (c).** Hiện tượng phụ thuộc cách khởi tạo. Nếu bảng khởi tạo đúng $v_\pi$ ở mọi trạng thái, sai số ban đầu bằng $0$, tức đã ở mức nhỏ nhất có thể, nên đường sai số chỉ tăng từ $0$ lên một mức dương. Với $V\equiv0{,}5$, độ chệch ban đầu nhỏ nhưng khác $0$, và đường sai số giảm rồi tăng như ở (b).

**Kiểm tra lại.** Ở (b), công thức tách cho sai số ban đầu bằng $1/18$ khi lấy trung bình trên năm trạng thái, vì phương sai ban đầu bằng $0$; khớp (a). Lỗi thường gặp là giải thích phần tăng lại bằng việc TD phân kỳ: sai số dừng ở một mức hữu hạn, dương khi bước học là hằng số.
:::

## Tài liệu tham khảo

- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 2.4 (§2.5, trang 33), 5.2 (§5.1, trang 94), 5.5 (§5.5, trang 105), 6.1 (§6.1, trang 121), 6.2 (§6.1, trang 123), 6.3, 6.5 và 6.6 (§6.2, trang 126); Ví dụ 5.1 (trang 93), 6.1 (trang 122), 6.2 (trang 125).
- Bertsekas, D. P. và Tsitsiklis, J. N. (1996), *Neuro-Dynamic Programming*, Athena Scientific, chương 2: hội tụ của đánh giá chính sách khi $\gamma=1$ và mọi lượt kết thúc hầu chắc chắn (Bài tập 05.22).
