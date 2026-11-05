# Bài tập Bài 10 — TRPO và PPO

Bộ bài tập gồm chín bài, phủ cả bảy mạch nội dung của bài học, ở ba mức: nhận biết (10.13, 10.14); tính toán hoặc chứng minh (10.15–10.19); vận dụng vào bài toán Học tăng cường (10.20, 10.21). Mười hai bài 10.1–10.12 thuộc mục "Bài tập củng cố" của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html) Bài 10, có gợi ý và lời giải tại đó, nên không chép lại; bảng dưới ghi chúng ở dạng "ghi chú: 10.k". Chín bài 10.13–10.21 chỉ có trong tệp này, tiếp nối bộ đếm Bài tập của ghi chú, và được xây dựng từ các bài tập và ví dụ của Sutton và Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2: Bài tập 3.15, 3.16, 5.13, 6.1, 7.6, 12.2, 12.8, 13.4, Ví dụ 13.1 và Hình 13.2. Sách không có bài tập về tối ưu chính sách miền tin cậy (Trust Region Policy Optimization, TRPO), gradient tự nhiên hay tối ưu chính sách gần kề (Proximal Policy Optimization, PPO); năm bài 10.13, 10.16, 10.17, 10.19, 10.21 mở rộng một bài tập của sách sang các đối tượng của Bài 10 và ghi rõ phần mở rộng ở dòng nguồn. Không bài nào trùng một trang bài tập của trang chiếu; bảng dưới dẫn thêm tới các trang bài tập trên trang chiếu, vốn trùng các bài củng cố 10.1, 10.5, 10.7, 10.8, 10.11, 10.12 và Tình huống 10.1–10.2 của ghi chú.

Đề bài được phát biểu lại theo ký hiệu của ghi chú Bài 10, với dữ kiện tự đủ và câu hỏi bổ sung có số. Các chữ viết tắt trong tệp: TD là sai phân thời gian (temporal difference), GAE là ước lượng lợi thế tổng quát (generalized advantage estimation), KL là phân kỳ Kullback–Leibler (Kullback–Leibler divergence), MDP là quá trình quyết định Markov (Markov decision process).

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-10-trpo-va-ppo.html#/1/1) | 10.14 |
| 2. Đường cơ sở, hàm lợi thế và actor–critic | [Mở phần](lecture-10-trpo-va-ppo.html#/2/1) | 10.14, 10.15, 10.16, 10.20, 10.21; [ghi chú: 10.1, 10.4, 10.5, 10.10 (mục Bài tập củng cố, cuối ghi chú)](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html#bai-tap-cung-co); trang [Bài tập: đường cơ sở hợp lệ](lecture-10-trpo-va-ppo.html#/2/11), trùng 10.1, và [Bài tập: sai số TD khi critic sai](lecture-10-trpo-va-ppo.html#/2/18), trùng 10.5, lời giải trên cùng trang |
| 3. Ước lượng lợi thế tổng quát | [Mở phần](lecture-10-trpo-va-ppo.html#/3/1) | 10.13, 10.15, 10.18; [ghi chú: 10.6, 10.7 (mục Bài tập củng cố, cuối ghi chú)](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html#bai-tap-cung-co); trang [Bài tập: GAE trên đoạn thu](lecture-10-trpo-va-ppo.html#/3/10), trùng 10.7, lời giải trên cùng trang |
| 4. Hàm thay thế và chặn cải thiện | [Mở phần](lecture-10-trpo-va-ppo.html#/4/1) | 10.16, 10.17, 10.18; [ghi chú: 10.11 (mục Bài tập củng cố, cuối ghi chú)](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html#bai-tap-cung-co); trang [Bài tập: đánh giá một bước cập nhật](lecture-10-trpo-va-ppo.html#/4/15) và [trang lời giải](lecture-10-trpo-va-ppo.html#/4/16), trùng 10.11 |
| 5. TRPO và gradient tự nhiên | [Mở phần](lecture-10-trpo-va-ppo.html#/5/1) | 10.19; [ghi chú: 10.8, 10.9 (mục Bài tập củng cố, cuối ghi chú)](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html#bai-tap-cung-co); trang [Bài tập: gradient liên hợp và bước TRPO](lecture-10-trpo-va-ppo.html#/5/11) và [trang lời giải](lecture-10-trpo-va-ppo.html#/5/12), trùng 10.8 |
| 6. Tối ưu chính sách gần kề (PPO) | [Mở phần](lecture-10-trpo-va-ppo.html#/6/1) | 10.16, 10.19, 10.21; [ghi chú: 10.2, 10.12 (mục Bài tập củng cố, cuối ghi chú)](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html#bai-tap-cung-co); trang [Bài tập: kiểm một mini-batch PPO](lecture-10-trpo-va-ppo.html#/6/22) và [trang lời giải](lecture-10-trpo-va-ppo.html#/6/23), trùng 10.12 (a)–(c) |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-10-trpo-va-ppo.html#/7/1) | 10.21; [ghi chú: 10.3 (mục Bài tập củng cố, cuối ghi chú)](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html#bai-tap-cung-co); trang [Bài tập: GAE ở bước cắt ngắn trên CartPole](lecture-10-trpo-va-ppo.html#/7/7) và [trang lời giải](lecture-10-trpo-va-ppo.html#/7/8), trùng Tình huống 10.1–10.2 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 10. Thời gian rời rạc $t=0,1,\dots$; phần thưởng $R_{t+1}$ nhận sau hành động $A_t$ tại trạng thái $S_t$; lượt kết thúc tại bước $T$; lợi tức $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$, với $G_T=0$. Cờ kết thúc $Z_{t+1}=1$ khi và chỉ khi MDP kết thúc tại bước $t+1$; cờ cắt ngắn $U_{t+1}=1$ khi việc thu dừng vì một giới hạn không thuộc MDP. Với critic $\hat v$, sai số TD là $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1})-\hat v(S_t)$, và $\delta_t=0$ khi $t\ge T$. Hàm điểm $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$, viết gọn $\psi_t=\psi_\theta(S_t,A_t)$. Lợi thế $A_\pi(s,a)=q_\pi(s,a)-v_\pi(s)$ và lợi thế trung bình $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$ (Định nghĩa 10.4, Mục 4.1). GAE với tham số $(\gamma,\lambda)$ là $\widehat A_t=\sum_{k\ge0}(\gamma\lambda)^k\delta_{t+k}$ (Định nghĩa 10.13, Mệnh đề 10.14). KL của hai phân phối theo Định nghĩa 10.23.

Khi dữ liệu do chính sách $\pi$ sinh ra và được dùng để đánh giá chính sách $\pi'$, tỉ số một bước là $\rho_t=\pi'(A_t\mid S_t)/\pi(A_t\mid S_t)$, như Định nghĩa 10.21 với $\pi_{\mathrm{old}}=\pi$, $\pi_\theta=\pi'$; điều kiện hỗ trợ $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$ luôn được giả thiết. Tích các tỉ số từ bước $t$ tới bước $k$ viết $\rho_{t:k}=\prod_{j=t}^{k}\rho_j$, theo Sutton và Barto (2018, §5.5), với quy ước $\rho_j=1$ khi $j\ge T$. Chữ $b$ dành cho đường cơ sở, như ghi chú.

Ba môi trường dùng ở nhiều bài; bài nào dùng chúng đều nêu lại dữ kiện trong khối đề bài.

- **Bài toán một bước** (Ví dụ 10.1). Một trạng thái $s$, hai hành động, lượt dừng sau hành động đầu tiên. Chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\theta=(\log2;\,0)$, nên $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$; phần thưởng $r(1)=3$, $r(2)=0$; hàm điểm $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$; $J=2$, $\nabla_\theta J=(\tfrac23;\,-\tfrac23)$.
- **Chuỗi hai trạng thái** (Ví dụ 10.6). Hai trạng thái chưa kết thúc $s_A$ (xuất phát) và $s_B$; $\gamma=0{,}9$. Tại $s_A$: hành động 1 sang $s_B$ với phần thưởng $0$; hành động 2 kết thúc lượt với phần thưởng $1$. Tại $s_B$: hành động 1 kết thúc với phần thưởng $3$; hành động 2 kết thúc với phần thưởng $0$. Viết $p_s$ cho xác suất chọn hành động 1 tại $s$. Chính sách cũ $\pi$: $p_A=\tfrac12$, $p_B=\tfrac23$, với $v_\pi=(1{,}4;\,2)$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$, $\nu^\pi=(0{,}1;\,0{,}045)$. Chính sách mới $\pi'$ của Ví dụ 10.11: $p'_A=0{,}6$, $p'_B=0{,}8$, với $J(\pi')=1{,}696$ và $J(\pi')-J(\pi)=0{,}296$.
- **Hành lang ngắn đảo hành động** (Sutton và Barto, 2018, Ví dụ 13.1; Ví dụ 10.2). Bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc lượt); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 là "sang phải", hành động 2 là "sang trái"; sang trái tại $s_1$ thì đứng yên; ở $s_2$ hai hành động bị đảo: hành động 1 về $s_1$, hành động 2 tới $s_3$. Mọi ô có cùng đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, nên chính sách softmax chọn hành động 1 với cùng xác suất $p=1/\bigl(1+e^{-(\theta_1-\theta_2)}\bigr)$ ở mọi ô, và $\psi_\theta(s,1)=(1-p)(1;\,-1)$, $\psi_\theta(s,2)=-p\,(1;\,-1)$. Độ dài lượt kỳ vọng là $\mathbb E_p[T]=2(2-p)/\bigl(p(1-p)\bigr)$, nên $J(p)=-\mathbb E_p[T]$, với $J(\tfrac12)=-12$, $p^*=2-\sqrt2\approx0{,}586$, $J(p^*)\approx-11{,}66$; tại $p=\tfrac12$, $\nabla_\theta J=(2;\,-2)$ và $v_\pi=(-12;\,-10;\,-6)$ trên $s_1,s_2,s_3$.

![Chuỗi hai trạng thái. Ô s A, ghi xuất phát và p A bằng xác suất chọn hành động 1, có hai cung: hành động 1 sang ô s B với phần thưởng 0; hành động 2 tới ô kết thúc tô xám với phần thưởng 1. Ô s B, ghi p B, có hai cung tới ô kết thúc: hành động 1 với phần thưởng 3, hành động 2 với phần thưởng 0. Góc dưới ghi gamma bằng 0,9 và chính sách cũ p A bằng 1/2, p B bằng 2/3.](img/lec-10/two-state-chain.svg)

Trên hình chuỗi hai trạng thái, chỉ cung "hành động 1 tại $s_A$" dẫn tới trạng thái thứ hai, nên mọi lượt dài $1$ hoặc $2$ bước.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

Hình hành lang đọc từ trái sang phải; trong mỗi ô, dòng "1 →" và "2 →" ghi ô kế tiếp của hành động 1 và 2. Ô $s_2$ có viền nét đứt và nhãn "đảo hành động".

**Quy ước chiết khấu.** Các định lý của ghi chú dùng $\gamma<1$ và độ dài lượt bị chặn. Chuỗi hai trạng thái có $\gamma=0{,}9$ và $T\le2$, nên thỏa cả hai. Hành lang ngắn có $\gamma=1$ và độ dài lượt không bị chặn; khi $0<p<1$, $T$ có đuôi hình học và mọi mô men hữu hạn, nên các kết luận về kỳ vọng của Mệnh đề 10.2 và Hệ quả 09.26 vẫn đúng, theo đoạn sau Ví dụ 10.4 của ghi chú. Vì vậy, trên hành lang, Thuật toán 10.6 được dùng với $\gamma=1$, như Ví dụ 10.4 của ghi chú. Bài 10.21 dùng $\gamma=0{,}99$.

**Chữ $\sigma$.** Ghi chú viết hàm logistic là $\sigma$. Trong tệp này, theo Sutton và Barto (2018, (13.19)) và Định nghĩa 09.12, chữ $\sigma$ chỉ độ lệch chuẩn của chính sách Gaussian (Bài tập 10.19); hàm logistic được viết đầy đủ, $1/(1+e^{-x})$.

Mọi bộ số không ghi nguồn là số liệu sư phạm tự xây dựng. Kết quả mô phỏng nêu trong lời giải ghi rõ cấu hình, mã và hạt giống ngẫu nhiên (seed), nên tái lập được. Số thập phân viết với dấu phẩy; véc-tơ viết $(x_1;\,x_2)$. Số hiệu "Định nghĩa 10.k", "Mệnh đề 10.k", "Thuật toán 10.k", "Ví dụ 10.k" chỉ khối của ghi chú bài giảng Bài 10.

## Mức nhận biết

### Bài tập 10.13. Chu kỳ bán rã của trọng số trong lợi tức λ và GAE

**Mức độ:** nhận biết. Mục tiêu học tập: đọc tham số $\lambda$ và tích $\gamma\lambda$ thành một số bước, và xác định những bước nào của một đoạn thu dựa nhiều vào critic ở biên đoạn.

**Nguồn:** Sutton và Barto (2018), §12.1, Bài tập 12.2, tr. 290, mở rộng sang trọng số $(\gamma\lambda)^k$ của GAE và độ dài đoạn $h$ của PPO; ghi chú bài giảng Bài 10, Mục 3.2–3.3 (Định nghĩa 10.13, Mệnh đề 10.14, Thuật toán 10.16) và bảng siêu tham số ở Mục 6.4 (theo Schulman và cộng sự, 2017, Bảng 3, 5).

::: exercise Bài tập 10.13 (Chu kỳ bán rã của trọng số trong lợi tức λ và GAE)
(Theo Sutton và Barto, 2018, Bài tập 12.2, mở rộng.) Trong lợi tức λ, lợi tức $n$ bước nhận trọng số $(1-\lambda)\lambda^{n-1}$; trong GAE, sai số TD $\delta_{t+k}$ nhận trọng số $(\gamma\lambda)^k$ (Mệnh đề 10.14(a)). *Chu kỳ bán rã* (half-life) của một dãy trọng số $x^k$, $0<x<1$, là số $\tau$ thỏa $x^\tau=\tfrac12$: sau $\tau$ bước, trọng số còn một nửa giá trị ban đầu.

- (a) Viết $\tau$ theo $\lambda$ cho dãy trọng số của lợi tức λ. Tính $\tau$ với $\lambda=0{,}8$ và $\lambda=0{,}95$.
- (b) Tính chu kỳ bán rã của dãy $(\gamma\lambda)^k$ của GAE trong hai cấu hình: $\gamma=0{,}9$, $\lambda=0{,}8$ (chuỗi hai trạng thái của ghi chú); $\gamma=0{,}99$, $\lambda=0{,}95$ (siêu tham số của bài báo PPO). Tính thêm tổng trọng số $\sum_{k\ge0}(\gamma\lambda)^k$ trong hai cấu hình.
- (c) Một đoạn thu độ dài $h$ không chứa bước kết thúc hay cắt ngắn nào. Tại bước $t<h$, Thuật toán 10.16 chỉ cộng các sai số TD $\delta_t,\dots,\delta_{h-1}$, và $\delta_{h-1}$ dùng giá trị ước lượng $\hat v(S_h)$ làm mục tiêu (bootstrap). Chứng minh rằng, so với tổng vô hạn $\sum_{k\ge0}(\gamma\lambda)^k\delta_{t+k}$, phần trọng số bị bỏ chiếm tỉ lệ $(\gamma\lambda)^{h-t}$ của tổng trọng số. Với $\gamma=0{,}99$, $\lambda=0{,}95$, tính tỉ lệ này khi $h-t=20$ và $h-t=100$, xác định số bước cuối của mỗi đoạn có tỉ lệ bị bỏ vượt $\tfrac12$, và tính tỉ lệ các bước đó trong một đoạn với hai độ dài đoạn của bài báo PPO, $h=2048$ (MuJoCo) và $h=128$ (Atari) (Schulman và cộng sự, 2017, Bảng 3, 5; bảng siêu tham số ở Mục 6.4 của ghi chú).
:::

::: hint Gợi ý Bài tập 10.13
Lấy logarit hai vế của $x^\tau=\tfrac12$. Ở (c), tổng của chuỗi hình học $\sum_{k\ge m}x^k$ là $x^m/(1-x)$.
:::

::: solution Lời giải Bài tập 10.13
**Câu (a).** Trọng số $(1-\lambda)\lambda^{n-1}$ giảm theo thừa số $\lambda$ mỗi bước. Từ $\lambda^\tau=\tfrac12$ được
$$\tau=\frac{\log2}{\log(1/\lambda)}.$$
Với $\lambda=0{,}8$: $\tau=0{,}6931/0{,}2231=3{,}11$ bước. Với $\lambda=0{,}95$: $\tau=0{,}6931/0{,}0513=13{,}51$ bước.

**Câu (b).** Thay $\lambda$ bằng $x=\gamma\lambda$.

- $\gamma=0{,}9$, $\lambda=0{,}8$: $x=0{,}72$, $\tau=0{,}6931/0{,}3285=2{,}11$ bước; tổng trọng số $1/(1-0{,}72)=3{,}57$.
- $\gamma=0{,}99$, $\lambda=0{,}95$: $x=0{,}9405$, $\tau=0{,}6931/0{,}0613=11{,}30$ bước; tổng trọng số $1/(1-0{,}9405)=16{,}81$.

Với cấu hình của bài báo PPO, $\delta_{t+11}$ còn khoảng một nửa trọng số của $\delta_t$, và các sai số TD xa hơn khoảng $11$ bước đóng góp ít hơn nửa trọng số ban đầu.

**Câu (c).** Tổng trọng số của mọi sai số TD là $\sum_{k\ge0}x^k=1/(1-x)$; phần bị bỏ ứng với $k\ge h-t$ có tổng $x^{h-t}/(1-x)$. Tỉ lệ là
$$\frac{x^{h-t}/(1-x)}{1/(1-x)}=x^{h-t}=(\gamma\lambda)^{h-t}.$$
Với $x=0{,}9405$: $0{,}9405^{20}=0{,}293$ và $0{,}9405^{100}=0{,}0022$. Tỉ lệ vượt $\tfrac12$ khi $h-t<11{,}30$, tức ở $11$ bước cuối của đoạn: $0{,}9405^{11}=0{,}509$ còn $0{,}9405^{12}=0{,}479$. Ở các bước này, hơn một nửa tổng trọng số của các sai số TD thuộc các bước sau biên đoạn, và Thuật toán 10.16 thay toàn bộ phần đó bằng giá trị bootstrap $\hat v(S_h)$. Với $h=2048$, đó là $11$ trong $2048$ bước, khoảng $0{,}5\%$; với $h=128$, là $11$ trong $128$ bước, khoảng $8{,}6\%$.

**Kiểm tra lại.** Với $\lambda=0{,}5$, chu kỳ bán rã phải bằng đúng $1$ bước: $\log2/\log2=1$. Lỗi thường gặp: dùng $\log\lambda$ thay cho $\log(1/\lambda)$, được $\tau$ âm; ở (b) dùng $\lambda$ thay cho $\gamma\lambda$, được $13{,}51$ thay cho $11{,}30$ bước; ở (c) coi tỉ lệ bị bỏ là $(\gamma\lambda)^{h-t-1}$, tức tính cả $\delta_{h-1}$ vào phần bị bỏ dù nó nằm trong đoạn.
:::

### Bài tập 10.14. Cộng một hằng vào phần thưởng và trừ một đường cơ sở

**Mức độ:** nhận biết. Mục tiêu học tập: phân biệt phép cộng hằng vào phần thưởng, có thể đổi bài toán khi độ dài lượt phụ thuộc chính sách, với phép trừ đường cơ sở khỏi lợi tức, không đổi kỳ vọng của ước lượng gradient.

**Nguồn:** Sutton và Barto (2018), §3.5, Bài tập 3.15 và 3.16, tr. 61; Ví dụ 13.1, tr. 323; ghi chú bài giảng Bài 10, Mục 1 (Ví dụ 10.1, 10.2) và Mục 2.1 (Định nghĩa 10.1, Mệnh đề 10.2); bộ số ở (b), (c) lấy từ Ví dụ 10.2.

::: exercise Bài tập 10.14 (Cộng một hằng vào phần thưởng và trừ một đường cơ sở)
(Theo Sutton và Barto, 2018, Bài tập 3.15 và 3.16.) Cộng một hằng $c$ vào mọi phần thưởng của một bài toán; viết $J_c$ cho hàm mục tiêu mới.

- (a) Bài toán một bước: một trạng thái, hai hành động, lượt dừng sau hành động đầu tiên, $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$. Hàm điểm $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$. Viết $J_c$ theo $J$ và kết luận về $\nabla_\theta J_c$. Theo Ví dụ 10.3, với phần thưởng $r$, ước lượng có đường cơ sở hằng $b$, $(r(A)-b)\psi_\theta(s,A)$, có tổng phương sai $\tfrac49(b-1)^2$. Dùng công thức này, tính tổng phương sai của ước lượng REINFORCE $(r(A)+c)\psi_\theta(s,A)$ khi $c=-1$ và $c=2$.
- (b) Hành lang ngắn đảo hành động: bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích); phần thưởng $-1$ mỗi bước; $\gamma=1$; ở $s_2$ hai hành động bị đảo; chính sách chọn hành động 1 với cùng xác suất $p$ ở mọi ô, với độ dài lượt kỳ vọng $\mathbb E_p[T]=2(2-p)/\bigl(p(1-p)\bigr)$. Viết $J_c(p)$ theo $\mathbb E_p[T]$. Xác định chính sách tốt nhất khi $c=0$, $c=1$ và $c=2$. Tại $p=\tfrac12$, biết $\nabla_\theta J=(2;\,-2)$ khi $c=0$; tính $\nabla_\theta J_c$.
- (c) Trên hành lang với $p=\tfrac12$, lượt có hành động $1,1,1,2,1$ có $T=5$ và lợi tức $G_t=-(5-t)$. Viết lợi tức $G^c_t$ sau phép cộng hằng. Giải thích vì sao $G^c_t$ không có dạng $G_t-b(S_t)$ với một đường cơ sở $b$ của Định nghĩa 10.1.
- (d) Bài toán liên tục, không kết thúc, với $\gamma<1$ (Bài tập 3.15 của sách): cộng $c$ vào mọi phần thưởng làm giá trị của mọi trạng thái tăng bao nhiêu? Tính với $c=1$, $\gamma=0{,}9$.
:::

::: hint Gợi ý Bài tập 10.14
Ở (a), $r(A)+c=r(A)-(-c)$. Lợi tức mới là $G^c_t=G_t+c\sum_{k=t}^{T-1}\gamma^{k-t}$. Khi $T$ cố định, phần cộng thêm là một hằng; khi $T$ phụ thuộc các hành động, nó phụ thuộc chính sách.
:::

::: solution Lời giải Bài tập 10.14
**Câu (a).** Lượt luôn dài đúng một bước, nên $G^c_0=r(A_0)+c$ và $J_c(\theta)=J(\theta)+c$ với mọi $\theta$. Do đó $\nabla_\theta J_c=\nabla_\theta J=(\tfrac23;\,-\tfrac23)$ và chính sách tốt nhất không đổi. Ước lượng REINFORCE với phần thưởng $r+c$ là $(r(A)-(-c))\psi_\theta(s,A)$, tức ước lượng với phần thưởng $r$ và đường cơ sở $b=-c$, nên có tổng phương sai $\tfrac49(-c-1)^2=\tfrac49(c+1)^2$:

- $c=-1$: phần thưởng $(2;\,-1)$, tổng phương sai $0$;
- $c=2$: phần thưởng $(5;\,2)$, tổng phương sai $\tfrac49\cdot9=4$.

Kỳ vọng không đổi; phép cộng hằng chỉ đổi phương sai: $0$ khi $c=-1$, $4$ khi $c=2$, so với $\tfrac49$ khi $c=0$.

**Câu (b).** Mỗi bước nhận $c-1$, nên $G^c_0=(c-1)T$ và
$$\begin{aligned}J_c(p)&=(c-1)\,\mathbb E_p[T]\\&=(c-1)\frac{2(2-p)}{p(1-p)}.\end{aligned}$$
Ba trường hợp:

- $c=0$: $J_0=-\mathbb E_p[T]$, cực đại tại $p^*=2-\sqrt2\approx0{,}586$, với $J_0(p^*)\approx-11{,}66$.
- $c=1$: mọi phần thưởng bằng $0$, nên $J_1\equiv0$ với mọi $p\in(0,1)$; mọi chính sách như nhau.
- $c=2$: $J_2=\mathbb E_p[T]$, tăng không bị chặn khi $p\to0$ hoặc $p\to1$, nên không có chính sách tốt nhất trong $(0,1)$; tác tử được thưởng cho việc không bao giờ tới đích.

Vì $J_c=(1-c)J_0$, ta có $\nabla_\theta J_c=(1-c)(2;\,-2)$: bằng $(1;\,-1)$ khi $c=\tfrac12$, bằng $0$ khi $c=1$, và bằng $(-2;\,2)$ khi $c=2$, tức đẩy $p$ ra xa $p^*$.

**Câu (c).** Với $\gamma=1$, $G^c_t=G_t+c(T-t)=(c-1)(5-t)$, tức $5(c-1),4(c-1),\dots,c-1$. Phần cộng thêm $c(T-t)$ là $c$ nhân số bước còn lại của lượt, nên phụ thuộc các hành động $A_t,A_{t+1},\dots$ chọn sau khi đã biết $H_t$. Một đường cơ sở theo Định nghĩa 10.1 phải xác định trước khi chọn $A_t$, nên $-c(T-t)$ không là đường cơ sở, và Mệnh đề 10.2 không áp dụng. Tóm lại, trên hành lang, trừ một đường cơ sở chỉ đổi hệ số của $\psi_t$ và giữ nguyên $J$, còn cộng $c$ vào phần thưởng đổi $J$ thành $J_c=(1-c)J_0$.

**Câu (d).** Lượt không kết thúc, nên mọi giá trị tăng đúng $\sum_{k\ge0}\gamma^kc=c/(1-\gamma)$, như nhau ở mọi trạng thái và với mọi chính sách; thứ tự giữa các chính sách không đổi. Với $c=1$, $\gamma=0{,}9$: mọi giá trị tăng $10$.

**Kiểm tra lại.** Ở (a) với $c=2$, tính trực tiếp: $\widehat g=(\tfrac53;\,-\tfrac53)$ với xác suất $\tfrac23$ và $(-\tfrac43;\,\tfrac43)$ với xác suất $\tfrac13$; mỗi tọa độ có mô men bậc hai $\tfrac{50}{27}+\tfrac{16}{27}=\tfrac{22}9$ và phương sai $\tfrac{22}9-\tfrac49=2$, tổng $4$. Ở (b), tại $p=\tfrac12$ và $c=2$: $J_2=12$, đúng bằng $-J_0(\tfrac12)$. Lỗi thường gặp: áp kết luận của (a) hoặc (d) cho bài toán có kết thúc với độ dài lượt phụ thuộc chính sách; coi $G^c_t$ là $G_t$ trừ đường cơ sở hằng $-c$, trong khi phần cộng thêm là $c(T-t)$, không phải $c$.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 10.15. Tổng sai số TD khi critic thay đổi trong lượt

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập: viết chính xác phần chênh lệch giữa hệ số Monte Carlo và tổng sai số TD khi critic được cập nhật trong lượt, và nhận ra vì sao Thuật toán 10.16 giữ $w_{\mathrm{old}}$ cố định.

**Nguồn:** Sutton và Barto (2018), §6.1, Bài tập 6.1 và đẳng thức (6.6), tr. 121; ghi chú bài giảng Bài 10, Mục 2.4 (Ví dụ 10.7, Thuật toán 10.9) và Mục 3.1–3.3 (Bổ đề 10.12, Mệnh đề 10.14, Thuật toán 10.16); critic dùng chung tham số ở (b) tự xây dựng.

::: exercise Bài tập 10.15 (Tổng sai số TD khi critic thay đổi trong lượt)
(Theo Sutton và Barto, 2018, Bài tập 6.1.) Một lượt $S_0,A_0,R_1,\dots,S_T$ kết thúc tại $T$. Critic được cập nhật sau mỗi bước: $V_t$ là bảng giá trị dùng ở bước $t$, với $V_t=0$ tại trạng thái kết thúc, và sai số TD ở bước $t$ là
$$\begin{aligned}\delta_t&=R_{t+1}\\&\quad+\gamma(1-Z_{t+1})V_t(S_{t+1})\\&\quad-V_t(S_t).\end{aligned}$$
Khi mọi $V_t$ bằng nhau, Bổ đề 10.12 (với $n\ge T-t$) cho $G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$.

- (a) Chứng minh rằng với $V_t$ thay đổi,
$$\begin{aligned}&G_t-V_t(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k\\&\quad+\sum_{k=t}^{T-2}\gamma^{k-t+1}\\&\qquad\times\bigl[V_{k+1}(S_{k+1})\\&\qquad\quad-V_k(S_{k+1})\bigr].\end{aligned}$$
- (b) Chuỗi hai trạng thái: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$; $\gamma=0{,}9$. Lượt: $S_0=s_A$, $A_0=1$, $R_1=0$, $S_1=s_B$, $A_1=1$, $R_2=3$, kết thúc tại $T=2$. Critic dùng chung một tham số cho hai trạng thái, $V(s_A)=V(s_B)=w$, khởi tạo $w=1$, cập nhật TD(0) bán gradient $w\leftarrow w+\alpha_w\delta_t$ sau mỗi bước với $\alpha_w=0{,}5$. Tính $\delta_0$, $\delta_1$, hai giá trị của $w$, rồi kiểm đẳng thức (a) tại $t=0$.
- (c) Lặp lại (b) với critic dạng bảng của Ví dụ 10.7: $V_0=(V(s_A);\,V(s_B))=(1;\,1{,}5)$, bước $t$ chỉ cập nhật giá trị của $S_t$ với $\alpha_w=0{,}5$. Tính số hạng hiệu chỉnh ở (a). Với critic dạng bảng tổng quát và $\alpha_w>0$, xác định điều kiện cần và đủ để số hạng hiệu chỉnh thứ $k$ khác $0$.
- (d) Trong ba thuật toán 10.6, 10.9, 10.16 của ghi chú, xác định thuật toán nào lập mọi hệ số của một lượt hoặc một đoạn ($G_t-\hat v(S_t)$ hoặc $\delta_t$) với cùng một critic. Với critic tuyến tính $\hat v(s,w)=w^\top x(s)$ cập nhật TD(0) bán gradient $w\leftarrow w+\alpha_w\delta_tx(S_t)$ sau mỗi bước, viết số hạng hiệu chỉnh thứ $k$ của (a) theo $\alpha_w$, $\delta_k$, $x(S_k)$, $x(S_{k+1})$.
:::

::: hint Gợi ý Bài tập 10.15
Viết $G_t=R_{t+1}+\gamma G_{t+1}$ với $t<T-1$, rồi cộng và trừ $\gamma V_t(S_{t+1})$ và $\gamma V_{t+1}(S_{t+1})$, theo đúng mẫu của đẳng thức (6.6) trong sách. Bước cuối $t=T-1$ có $G_T=0$ và mặt nạ $1-Z_T=0$.
:::

::: solution Lời giải Bài tập 10.15
**Câu (a).** Đặt $E_t=G_t-V_t(S_t)$. Với $t\le T-2$, bước $t+1$ chưa kết thúc nên $Z_{t+1}=0$, và
$$
\begin{aligned}
E_t&=R_{t+1}+\gamma G_{t+1}-V_t(S_t)\\
&=\delta_t+\gamma\bigl[G_{t+1}-V_t(S_{t+1})\bigr]\\
&=\delta_t+\gamma E_{t+1}+\gamma V_{t+1}(S_{t+1})\\
&\quad-\gamma V_t(S_{t+1}).
\end{aligned}
$$
Đẳng thức thứ nhất là $G_t=R_{t+1}+\gamma G_{t+1}$; đẳng thức thứ hai cộng và trừ $\gamma V_t(S_{t+1})$ rồi dùng định nghĩa của $\delta_t$ với $Z_{t+1}=0$; đẳng thức thứ ba cộng và trừ $\gamma V_{t+1}(S_{t+1})$. Tại $t=T-1$: $Z_T=1$ và $G_T=0$, nên $E_{T-1}=R_T-V_{T-1}(S_{T-1})=\delta_{T-1}$. Lặp truy hồi từ $t$ tới $T-1$, mỗi bước nhân thêm $\gamma$, được đẳng thức cần chứng minh. Số hạng hiệu chỉnh thứ $k$ là $\gamma^{k-t+1}$ nhân lượng thay đổi của giá trị tại $S_{k+1}$ do bước cập nhật thứ $k$ gây ra.

**Câu (b).** Bước $t=0$: $\delta_0=0+0{,}9\cdot1-1=-0{,}1$, rồi $w=1+0{,}5\cdot(-0{,}1)=0{,}95$. Bước $t=1$: mặt nạ tắt, $\delta_1=3-0{,}95=2{,}05$, rồi $w=0{,}95+0{,}5\cdot2{,}05=1{,}975$. Kiểm tại $t=0$:

- vế trái: $G_0-V_0(s_A)=0{,}9\cdot3-1=1{,}7$;
- tổng sai số TD: $\delta_0+0{,}9\,\delta_1=-0{,}1+1{,}845=1{,}745$;
- hiệu chỉnh: $0{,}9\bigl[V_1(s_B)-V_0(s_B)\bigr]=0{,}9\,(0{,}95-1)=-0{,}045$.

Tổng $1{,}745-0{,}045=1{,}7$, khớp vế trái. Cập nhật tại $s_A$ đổi cả giá trị tại $s_B$ vì hai trạng thái dùng chung $w$.

**Câu (c).** Bước $t=0$ chỉ đổi $V(s_A)$ thành $1+0{,}5\cdot0{,}35=1{,}175$, nên $V_1(s_B)=V_0(s_B)=1{,}5$ và số hạng hiệu chỉnh bằng $0$. Kiểm: $\delta_0=0{,}35$, $\delta_1=3-1{,}5=1{,}5$, $\delta_0+0{,}9\,\delta_1=1{,}7=G_0-V_0(s_A)$. Tổng quát, bước $k$ của critic dạng bảng chỉ đổi giá trị tại $S_k$, một lượng $\alpha_w\delta_k$, nên $V_{k+1}(S_{k+1})-V_k(S_{k+1})=\alpha_w\delta_k\mathbb 1\{S_{k+1}=S_k\}$. Số hạng hiệu chỉnh thứ $k$ khác $0$ khi và chỉ khi $S_{k+1}=S_k$ và $\delta_k\ne0$, tức lượt ở lại đúng trạng thái vừa được cập nhật, như hành động 2 tại $s_1$ của hành lang ngắn. Quay lại một trạng thái sau khi đã rời nó, như lượt $s_1\to s_2\to s_1$, không tạo hiệu chỉnh.

**Câu (d).** Thuật toán 10.6 không tính $\delta_t$; nó dùng hệ số Monte Carlo $G_t-\hat v(S_t,w_{\mathrm{old}})$, bằng $\sum_k\gamma^{k-t}\delta_k$ với cùng $w_{\mathrm{old}}$ theo Bổ đề 10.12. Thuật toán 10.16 tính mọi $\delta_t$ của đoạn với cùng $w_{\mathrm{old}}$. Ở hai thuật toán này, mọi số hạng hiệu chỉnh bằng $0$, và Bổ đề 10.12, Mệnh đề 10.14 đúng chính xác. Thuật toán 10.9 cập nhật $w$ sau mỗi bước. Với critic tuyến tính, $w_{k+1}-w_k=\alpha_w\delta_kx(S_k)$, nên
$$\begin{aligned}&V_{k+1}(S_{k+1})-V_k(S_{k+1})\\&\quad=\alpha_w\delta_k\,x(S_k)^\top x(S_{k+1}),\end{aligned}$$
và số hạng hiệu chỉnh thứ $k$ là $\gamma^{k-t+1}\alpha_w\delta_k\,x(S_k)^\top x(S_{k+1})$, tỉ lệ với $\alpha_w$. Critic dạng bảng là trường hợp $x(s)$ là véc-tơ đơn vị của $s$, khi đó $x(S_k)^\top x(S_{k+1})=\mathbb 1\{S_{k+1}=S_k\}$, khớp (c); critic dùng chung tham số của (b) có $x\equiv1$. Nếu GAE được tính bằng truy hồi lùi trên các $\delta_t$ lấy từ nhiều phiên bản của critic, đẳng thức của Mệnh đề 10.14(a) không còn chính xác; với $\lambda=1$, tổng $\sum_k\gamma^{k-t}\delta_k$ lệch khỏi $G_t-V_t(S_t)$ đúng bằng trừ tổng các số hạng hiệu chỉnh trên.

**Kiểm tra lại.** Khi $\alpha_w=0$, mọi $V_t$ bằng nhau và (a) trở về Bổ đề 10.12. Lỗi thường gặp: dùng $V_{t+1}(S_{t+1})$ thay cho $V_t(S_{t+1})$ trong $\delta_t$, được $\delta_0=0+0{,}9\cdot0{,}95-1=-0{,}145$ ở (b); đổi dấu số hạng hiệu chỉnh, được $1{,}745+0{,}045=1{,}79\ne1{,}7$.
:::

### Bài tập 10.16. Biến điều khiển, đường cơ sở và phép dịch lợi thế trong PPO

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập: chứng minh rằng biến điều khiển của lấy mẫu quan trọng theo từng quyết định không đổi kỳ vọng, nối kết quả này với đường cơ sở và với hàm thay thế, rồi kiểm rằng mục tiêu cắt của PPO không có tính chất đó.

**Nguồn:** Sutton và Barto (2018), §7.4, Bài tập 7.6 và các đẳng thức (7.13), (7.14), tr. 150–151; mở rộng sang hàm thay thế $\mathcal L^{\mathrm{CPI}}$ và mục tiêu cắt $\mathcal L^{\mathrm{CLIP}}$ ở (c), (d); ghi chú bài giảng Bài 10, Mục 2.1 (Mệnh đề 10.2), Mục 4.2 (Định nghĩa 10.21), Mục 6.1 (Ví dụ 10.17, Định nghĩa 10.39, Mệnh đề 10.40) và Mục 6.3 (Định nghĩa 10.46).

::: exercise Bài tập 10.16 (Biến điều khiển, đường cơ sở và phép dịch lợi thế trong PPO)
(Theo Sutton và Barto, 2018, Bài tập 7.6, mở rộng.) Dữ liệu do chính sách $\pi$ sinh ra; chính sách đích là $\pi'$, với tỉ số $\rho_t=\pi'(A_t\mid S_t)/\pi(A_t\mid S_t)$ và điều kiện hỗ trợ. $Q$ là một bảng giá trị hành động cố định và $\bar V(s)=\sum_a\pi'(a\mid s)Q(s,a)$. Lợi tức $n$ bước khác chính sách của giá trị hành động, kết thúc ở chân trời $h$, có dạng (7.14) của sách:
$$\begin{aligned}G_{t:h}&=R_{t+1}+\gamma\rho_{t+1}G_{t+1:h}\\&\quad+\gamma\bigl[\bar V(S_{t+1})\\&\qquad-\rho_{t+1}Q(S_{t+1},A_{t+1})\bigr],\end{aligned}$$
trong đó số hạng trong ngoặc vuông là *biến điều khiển* (control variate). Dạng giá trị trạng thái (7.13) của sách, với critic cố định $\hat v$, là
$$\begin{aligned}G_{t:h}&=\rho_t\bigl(R_{t+1}+\gamma G_{t+1:h}\bigr)\\&\quad+(1-\rho_t)\hat v(S_t),\end{aligned}$$
với $t<h<T$ và $G_{h:h}=\hat v(S_h)$; số hạng $(1-\rho_t)\hat v(S_t)$ là biến điều khiển của dạng này.

- (a) Chứng minh rằng với mọi $t+1<T$, $\mathbb E\bigl[\rho_{t+1}Q(S_{t+1},A_{t+1})\mid H_{t+1}\bigr]=\bar V(S_{t+1})$, rồi suy ra biến điều khiển không đổi kỳ vọng của lợi tức khi biết $(S_t,A_t)$. Chứng minh rằng biến điều khiển $(1-\rho_t)\hat v(S_t)$ của dạng (7.13) có kỳ vọng $0$ khi biết $H_t$.
- (b) Mở rộng sang hàm thay thế. Với $\pi=\pi_{\mathrm{old}}$, $\pi'=\pi_\theta$ và một hàm $c:\mathcal S\to\mathbb R$ bị chặn, chứng minh rằng thay $A_{\mathrm{old}}(s,a)$ bằng $A_{\mathrm{old}}(s,a)+c(s)$ trong Định nghĩa 10.21 cộng vào $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$ một hằng không phụ thuộc $\theta$. So sánh lập luận với chứng minh Mệnh đề 10.2.
- (c) Bài toán một bước với $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$; bộ đệm ba mẫu, hành động $1,1,2$, lợi thế $\widehat A=(1;\,1;\,-2)$ (Ví dụ 10.17). Chính sách mới chọn hành động 1 với xác suất $p$. Cộng $c=2$ vào mọi lợi thế, được $\widehat A^c=(3;\,3;\,0)$. Tính $\mathcal L^{\mathrm{CPI}}$ với $\widehat A^c$ theo $p$ và so sánh với $\mathcal L^{\mathrm{CPI}}(p)=3p-2$ của Ví dụ 10.17.

Theo Ví dụ 10.17, với lợi thế $\widehat A$, $\epsilon=0{,}2$ và $p_1=0{,}7\overline3$, mục tiêu cắt là
$$\begin{aligned}&\mathcal L^{\mathrm{CLIP}}(p)\\&=\begin{cases}3p-2,&p\le p_1,\\p-0{,}5\overline3,&p_1<p\le0{,}8,\\0{,}2\overline6,&p\ge0{,}8.\end{cases}\end{aligned}$$

- (d) Với cùng bộ đệm và $\epsilon=0{,}2$, tính $\mathcal L^{\mathrm{CLIP}}$ với $\widehat A^c$ theo $p$ trên $[\tfrac23,1)$, và so sánh với $\mathcal L^{\mathrm{CLIP}}(p)+2$. Tính đạo hàm theo $p$ của hai mục tiêu tại $p=0{,}75$.
:::

::: hint Gợi ý Bài tập 10.16
Khi biết $H_{t+1}$, hành động $A_{t+1}$ có phân phối $\pi(\cdot\mid S_{t+1})$, và $\pi$ trong mẫu số khử $\pi$ của phép lấy kỳ vọng. Ở (d), dùng Mệnh đề 10.40: với lợi thế bằng $0$, số hạng cắt bằng $0$ với mọi tỉ số.
:::

::: solution Lời giải Bài tập 10.16
**Câu (a).** Cố định $t+1<T$. Khi biết $H_{t+1}$, trạng thái $S_{t+1}$ đã xác định và $A_{t+1}\sim\pi(\cdot\mid S_{t+1})$. Viết $s=S_{t+1}$:
$$
\begin{aligned}
&\mathbb E\bigl[\rho_{t+1}Q(s,A_{t+1})\mid H_{t+1}\bigr]\\
&=\sum_{a:\,\pi(a\mid s)>0}\pi(a\mid s)\\
&\qquad\times\frac{\pi'(a\mid s)}{\pi(a\mid s)}\,Q(s,a)\\
&=\sum_a\pi'(a\mid s)\,Q(s,a)\\
&=\bar V(s).
\end{aligned}
$$
Đẳng thức thứ hai dùng điều kiện hỗ trợ: các hành động bị bỏ ở tổng thứ nhất có $\pi'(a\mid s)=0$. Do đó biến điều khiển có kỳ vọng $0$ khi biết $H_{t+1}$; theo tính chất tháp, kỳ vọng của nó khi biết $(S_t,A_t)$, một phần của $H_{t+1}$, cũng bằng $0$, và $\mathbb E[G_{t:h}\mid S_t,A_t]=\mathbb E[R_{t+1}+\gamma\rho_{t+1}G_{t+1:h}\mid S_t,A_t]$. Với dạng (7.13), áp dụng cùng phép tính với $Q(s,a)\equiv\hat v(s)$: $\mathbb E[\rho_t\mid H_t]=\sum_a\pi'(a\mid S_t)=1$, nên $\mathbb E[(1-\rho_t)\hat v(S_t)\mid H_t]=\hat v(S_t)(1-1)=0$.

**Câu (b).** Theo dạng tỉ số của Định nghĩa 10.21, phần thêm vào $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$ là
$$
\begin{aligned}
&\frac1{1-\gamma}\sum_s\nu^{\mathrm{old}}(s)\,c(s)\\
&\quad\times\mathbb E_{A\sim\pi_{\mathrm{old}}}\bigl[\rho_\theta(s,A)\bigr]\\
&=\frac1{1-\gamma}\sum_s\nu^{\mathrm{old}}(s)\,c(s),
\end{aligned}
$$
vì $\mathbb E_{A\sim\pi_{\mathrm{old}}(\cdot\mid s)}[\rho_\theta(s,A)]=1$ như ở (a). Phần này không phụ thuộc $\theta$, nên mọi $\theta$ có cùng gradient và cực đại của hàm thay thế không đổi. Lấy gradient tại $\theta_{\mathrm{old}}$, nơi $\nabla_\theta\rho_\theta=\psi_{\theta_{\mathrm{old}}}$, được $\mathbb E[c(S)\psi(S,A)]=0$: đúng bước 2 của chứng minh Mệnh đề 10.2. Biến điều khiển của lấy mẫu quan trọng và đường cơ sở của gradient chính sách dựa trên cùng một đẳng thức, $\mathbb E_\pi[\rho]=1$ và đạo hàm của nó $\mathbb E_\pi[\psi]=0$.

**Câu (c).** Tỉ số $\rho(1)=p/\tfrac23=1{,}5p$ và $\rho(2)=(1-p)/\tfrac13=3(1-p)$. Với $\widehat A^c$:
$$\begin{aligned}\mathcal L^{\mathrm{CPI}}_c(p)&=\tfrac13\bigl[3\cdot1{,}5p\cdot2+0\bigr]\\&=3p.\end{aligned}$$
So với $3p-2$: hiệu bằng đúng $2$ với mọi $p$. Trung bình mẫu của tỉ số là $\tfrac13(1{,}5p+1{,}5p+3(1-p))=1$ với mọi $p$, vì tần suất hành động trong bộ đệm trùng $\pi_{\mathrm{old}}$; trên một bộ đệm có tần suất khác $\pi_{\mathrm{old}}$, hiệu chỉ bằng $2$ theo kỳ vọng.

**Câu (d).** Với $\widehat A^c=(3;\,3;\,0)$, mẫu thứ ba có số hạng cắt bằng $0$ (Mệnh đề 10.40(c)); hai mẫu đầu bị chặn trên ở $\rho=1{,}2$, tức $p=0{,}8$. Do đó
$$\mathcal L^{\mathrm{CLIP}}_c(p)=\begin{cases}3p,&p\le0{,}8,\\2{,}4,&p\ge0{,}8,\end{cases}$$
với $2{,}4=\tfrac23\cdot3\cdot1{,}2$.
So sánh:

| $p$ | $\mathcal L^{\mathrm{CLIP}}+2$ | $\mathcal L^{\mathrm{CLIP}}_c$ |
| --- | --- | --- |
| $0{,}7$ | $2{,}1$ | $2{,}1$ |
| $0{,}75$ | $2{,}2167$ | $2{,}25$ |
| $0{,}85$ | $2{,}2667$ | $2{,}4$ |

Hai mục tiêu trùng nhau khi $p\le0{,}7\overline3$ và tách nhau sau đó. Tại $p=0{,}75$, đạo hàm theo $p$ là $1$ với lợi thế gốc và $3$ với lợi thế đã dịch; theo logit $\theta_1$, nhân với $p(1-p)=0{,}1875$, được $0{,}1875$ và $0{,}5625$. Với lợi thế gốc, mẫu hành động 2 có lợi thế âm và đã chạm $\rho=0{,}8$ nên ngừng phạt; với lợi thế đã dịch, mẫu đó có lợi thế $0$ và không còn vai trò, nên hai mẫu còn lại kéo $p$ lên với độ dốc của $\mathcal L^{\mathrm{CPI}}$. Phép cắt phụ thuộc dấu của từng lợi thế, nên phép dịch hằng đổi tập mẫu bị cắt và đổi gradient của mục tiêu PPO-Clip, dù nó chỉ cộng một hằng vào $\mathcal L^{\mathrm{CPI}}$.

**Kiểm tra lại.** Tại $p=\tfrac23$, mọi tỉ số bằng $1$, và hai mục tiêu ở (d) cùng bằng $2$, khớp Mệnh đề 10.41(c). Lỗi thường gặp: ở (a) quên điều kiện hỗ trợ, khi đó $\mathbb E[\rho\mid H]$ có thể nhỏ hơn $1$; ở (d) cắt mẫu có lợi thế $0$ ở $\rho=0{,}8$ như một mẫu lợi thế âm, được $\mathcal L^{\mathrm{CLIP}}_c$ sai khi $p>0{,}7\overline3$; suy từ (c) rằng chuẩn hóa lợi thế bằng cách trừ trung bình không đổi bước cập nhật của PPO-Clip.
:::

### Bài tập 10.17. Lấy mẫu quan trọng theo quỹ đạo và hàm thay thế

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập: viết hiệu hiệu năng $J(\pi')-J(\pi)$ thành một kỳ vọng trên dữ liệu của $\pi$ bằng tích các tỉ số, và nhận ra hàm thay thế là đại lượng thu được khi bỏ các tỉ số của những bước trước.

**Nguồn:** Sutton và Barto (2018), §5.9, Bài tập 5.13 và các đẳng thức (5.12)–(5.14), tr. 114–115; mở rộng sang Bổ đề 10.19 và hàm thay thế ở (b)–(d); ghi chú bài giảng Bài 10, Mục 4.1–4.2 (Ví dụ 10.11, Bổ đề 10.19, Định nghĩa 10.21).

::: exercise Bài tập 10.17 (Lấy mẫu quan trọng theo quỹ đạo và hàm thay thế)
(Theo Sutton và Barto, 2018, Bài tập 5.13, mở rộng.) Lượt sinh bởi chính sách $\pi$, kết thúc tại $T\le T_{\max}$; chính sách đích $\pi'$ thỏa điều kiện hỗ trợ; $\rho_t=\pi'(A_t\mid S_t)/\pi(A_t\mid S_t)$, $\rho_{t:k}=\prod_{j=t}^k\rho_j$, với $\rho_j=1$ khi $j\ge T$.

- (a) Cho $X_t$ là một hàm bị chặn của $(H_t,A_t,R_{t+1})$, bằng $0$ khi $t\ge T$. Chứng minh rằng $\mathbb E_\pi[\rho_{0:T_{\max}-1}X_t]=\mathbb E_\pi[\rho_{0:t}X_t]$: các tỉ số của những bước sau $t$ có kỳ vọng $1$. Đẳng thức này mở rộng (5.14) của sách, $\mathbb E[\rho_{t:T-1}R_{t+1}]=\mathbb E[\rho_{t:t}R_{t+1}]$, bằng cùng lập luận.
- (b) Dùng (a) và Bổ đề 10.19 để chứng minh
$$\begin{aligned}&J(\pi')-J(\pi)\\&=\mathbb E_\pi\Bigl[\sum_{t=0}^{T-1}\gamma^t\rho_{0:t}\\&\qquad\times A_\pi(S_t,A_t)\Bigr],\end{aligned}$$
và chứng minh rằng bỏ các tỉ số $\rho_{0:t-1}$, tức thay $\rho_{0:t}$ bằng $\rho_t$, được đúng $\mathcal L_\pi(\pi')-J(\pi)$ của Định nghĩa 10.21.
- (c) Chuỗi hai trạng thái: $\gamma=0{,}9$; tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$. Chính sách cũ $\pi$: $p_A=\tfrac12$, $p_B=\tfrac23$, với $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$. Chính sách mới $\pi'$: $p'_A=0{,}6$, $p'_B=0{,}8$. Liệt kê ba loại lượt của $\pi$ cùng xác suất và các tỉ số. Với mỗi loại lượt, tính $Y=\sum_t\gamma^t\rho_{0:t}A_\pi(S_t,A_t)$ và $Y'=\sum_t\gamma^t\rho_tA_\pi(S_t,A_t)$. Tính $\mathbb E[Y]$, $\mathbb E[Y']$ và so sánh với $\Delta J=0{,}296$, $\mathcal L-J=0{,}26$ của Ví dụ 10.11.
- (d) Tính phương sai của $Y$ và $Y'$ trên một lượt. Nêu đánh đổi giữa hai ước lượng, và giải thích vì sao đánh đổi này nặng hơn khi lượt dài.
:::

::: hint Gợi ý Bài tập 10.17
(a) Bóc từng tỉ số từ bước cuối: khi biết $H_k$, $\mathbb E[\rho_k\mid H_k]=1$, như (5.13) của sách. (b) Với $f$ là hàm của $(H_t,A_t)$, $\mathbb E_{\pi'}[f]=\mathbb E_\pi[\rho_{0:t}f]$, vì xác suất của lịch sử dưới hai chính sách chỉ khác nhau ở các thừa số chính sách. Ở (c), lượt chọn hành động 2 tại $s_A$ chỉ có một bước.
:::

::: solution Lời giải Bài tập 10.17
**Câu (a).** Với $k>t$, $X_t$ và $\rho_{0:k-1}$ là hàm của $H_k$, còn $\mathbb E[\rho_k\mid H_k]=1$: khi $k<T$, $\mathbb E[\rho_k\mid H_k]=\sum_a\pi(a\mid S_k)\frac{\pi'(a\mid S_k)}{\pi(a\mid S_k)}=1$ nhờ điều kiện hỗ trợ; khi $k\ge T$, $\rho_k=1$. Do đó
$$
\begin{aligned}
&\mathbb E[\rho_{0:k}X_t]=\mathbb E\bigl[\rho_{0:k-1}X_t\\
&\qquad\times\mathbb E[\rho_k\mid H_k]\bigr]\\
&=\mathbb E[\rho_{0:k-1}X_t].
\end{aligned}
$$
Đẳng thức thứ nhất là tính chất tháp theo $H_k$. Áp dụng lần lượt với $k=T_{\max}-1,\dots,t+1$ được $\mathbb E[\rho_{0:T_{\max}-1}X_t]=\mathbb E[\rho_{0:t}X_t]$. Các kỳ vọng hữu hạn vì $X_t$ bị chặn và, với tập trạng thái, hành động hữu hạn, mỗi tỉ số bị chặn.

**Câu (b).** Xác suất của lịch sử $(H_t,A_t)$ dưới $\pi'$ là xác suất dưới $\pi$ nhân $\rho_{0:t}$, vì $\mu_0$ và động lực $P$ như nhau và chỉ các thừa số $\pi'(A_j\mid S_j)$ thay cho $\pi(A_j\mid S_j)$, $j\le t$. Do đó, với $f_t=\mathbb 1\{t<T\}\gamma^tA_\pi(S_t,A_t)$, $\mathbb E_{\pi'}[f_t]=\mathbb E_\pi[\rho_{0:t}f_t]$. Cộng theo $t<T_{\max}$ và dùng Bổ đề 10.19 được đẳng thức cần chứng minh.

Khi chỉ giữ $\rho_t$: khi biết $H_t$ trên $\{t<T\}$, $\mathbb E_\pi[\rho_tA_\pi(S_t,A_t)\mid H_t]=\sum_a\pi'(a\mid S_t)A_\pi(S_t,a)=A_\pi(S_t,\pi')$, nên
$$
\begin{aligned}
&\mathbb E_\pi\Bigl[\sum_{t<T}\gamma^t\rho_t\\
&\qquad\times A_\pi(S_t,A_t)\Bigr]\\
&=\sum_{t\ge0}\gamma^t\sum_{s\in\mathcal S}\Pr_\pi(S_t=s,\,t<T)\\
&\qquad\times A_\pi(s,\pi')\\
&=\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^\pi(s)\,A_\pi(s,\pi'),
\end{aligned}
$$
theo Định nghĩa 10.18; đây là $\mathcal L_\pi(\pi')-J(\pi)$ theo dạng thứ hai của Định nghĩa 10.21. Phân bố trạng thái vẫn là của $\pi$, vì các tỉ số $\rho_{0:t-1}$ của những bước dẫn tới $S_t$ đã bị bỏ.

**Câu (c).** Các tỉ số: $\rho_0=0{,}6/0{,}5=1{,}2$ khi $A_0=1$ và $0{,}4/0{,}5=0{,}8$ khi $A_0=2$; $\rho_1=0{,}8/\tfrac23=1{,}2$ khi $A_1=1$ và $0{,}2/\tfrac13=0{,}6$ khi $A_1=2$. Ba loại lượt, ghi bằng dãy hành động, gồm:

- $A_0=2$: kết thúc sau một bước, xác suất $\tfrac12$, $\rho_0=0{,}8$;
- $A_0,A_1=1,1$: xác suất $\tfrac12\cdot\tfrac23=\tfrac13$, $\rho_0=\rho_1=1{,}2$;
- $A_0,A_1=1,2$: xác suất $\tfrac12\cdot\tfrac13=\tfrac16$, $\rho_0=1{,}2$, $\rho_1=0{,}6$.

Giá trị của $Y$ và $Y'$:

| $A_0,A_1$ | $Y$ | $Y'$ |
| --- | --- | --- |
| $2$ | $-0{,}32$ | $-0{,}32$ |
| $1,1$ | $1{,}776$ | $1{,}56$ |
| $1,2$ | $-0{,}816$ | $-0{,}6$ |

Chẳng hạn, ở lượt $1,1$, $Y=1{,}2\cdot0{,}4+0{,}9\cdot1{,}2\cdot1{,}2\cdot1=0{,}48+1{,}296=1{,}776$ và $Y'=0{,}48+0{,}9\cdot1{,}2\cdot1=1{,}56$. Kỳ vọng:

- $\mathbb E[Y]=\tfrac12(-0{,}32)+\tfrac13\cdot1{,}776+\tfrac16(-0{,}816)=-0{,}16+0{,}592-0{,}136=0{,}296=\Delta J$;
- $\mathbb E[Y']=-0{,}16+0{,}52-0{,}1=0{,}26=\mathcal L-J$.

Hiệu $0{,}036$ đến từ số hạng $t=1$: $\mathbb E[Y]$ có $0{,}9\cdot0{,}6\cdot0{,}4=0{,}216$, còn $\mathbb E[Y']$ có $0{,}9\cdot0{,}5\cdot0{,}4=0{,}18$; tỉ số $\rho_0$ bị bỏ chính là tỉ số giữa xác suất tới $s_B$ dưới hai chính sách, $0{,}6/0{,}5$.

**Câu (d).** Mô men bậc hai: $\mathbb E[Y^2]=\tfrac12\cdot0{,}1024+\tfrac13\cdot3{,}1542+\tfrac16\cdot0{,}6659=1{,}2136$ và $\mathbb E[Y'^2]=\tfrac12\cdot0{,}1024+\tfrac13\cdot2{,}4336+\tfrac16\cdot0{,}36=0{,}9224$. Phương sai: $\operatorname{Var}(Y)=1{,}2136-0{,}296^2=1{,}1260$ và $\operatorname{Var}(Y')=0{,}9224-0{,}26^2=0{,}8548$. Ước lượng $Y$ không chệch cho $\Delta J$ nhưng có phương sai lớn hơn; $Y'$ có phương sai nhỏ hơn nhưng ước lượng $\mathcal L-J$, lệch khỏi $\Delta J$ một lượng mà Định lý 10.26 chặn theo khoảng cách giữa hai chính sách. Ở bước $t$, $Y$ nhân lợi thế với tích $t+1$ tỉ số. Mỗi tỉ số có $\mathbb E[\rho_k^2\mid H_k]=\sum_a\pi'(a\mid S_k)^2/\pi(a\mid S_k)\ge1$, dấu bằng khi hai chính sách trùng nhau tại $S_k$; trên chuỗi này, $\mathbb E[\rho_0^2]=\tfrac12\cdot1{,}44+\tfrac12\cdot0{,}64=1{,}04$. Theo tính chất tháp, nếu mọi lượt dài hơn $t$ bước và $\mathbb E[\rho_k^2\mid H_k]\ge c>1$ với mọi $k\le t$ thì $\mathbb E[\rho_{0:t}^2]\ge c^{t+1}$, nên phương sai của $Y$ có thể tăng theo cấp số nhân của độ dài lượt. Hàm thay thế giữ mỗi số hạng với một tỉ số duy nhất.

**Kiểm tra lại.** Khi $\pi'=\pi$, mọi tỉ số bằng $1$, $Y=Y'=\sum_t\gamma^tA_\pi(S_t,A_t)$, và $\mathbb E[Y]=0$ theo Mệnh đề 10.5(a). Lỗi thường gặp: ở (c) dùng $\rho_0$ của hành động 1 cho cả lượt chọn hành động 2; ở (b) cho rằng bỏ $\rho_{0:t-1}$ chỉ làm tăng phương sai mà không đổi kỳ vọng, trong khi nó đổi phân bố trạng thái từ $\nu^{\pi'}$ sang $\nu^\pi$.
:::

### Bài tập 10.18. Lợi tức λ khác chính sách với biến điều khiển

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập: viết lợi tức λ khác chính sách thành tổng sai số TD có trọng số bởi các tỉ số, nhận ra GAE là trường hợp tỉ số bằng $1$, và kiểm tính không chệch khi $\lambda=1$.

**Nguồn:** Sutton và Barto (2018), §12.9, Bài tập 12.8 và các đẳng thức (12.22)–(12.24), tr. 309, với $\gamma_t=\gamma$ và $\lambda_t=\lambda$ không đổi; ghi chú bài giảng Bài 10, Mục 3.2 (Định nghĩa 10.13, Mệnh đề 10.14) và Mục 4.2 (Định nghĩa 10.21); bộ số ở (c), (d) tự xây dựng trên chuỗi hai trạng thái.

::: exercise Bài tập 10.18 (Lợi tức λ khác chính sách với biến điều khiển)
(Theo Sutton và Barto, 2018, Bài tập 12.8.) Lượt sinh bởi $\pi$, kết thúc tại $T$; chính sách đích $\pi'$; $\rho_t=\pi'(A_t\mid S_t)/\pi(A_t\mid S_t)$; critic $\hat v$ cố định trong cả lượt; $\lambda\in[0,1]$. Lợi tức λ khác chính sách được định nghĩa lùi từ $G^{\lambda s}_T=0$:
$$\begin{aligned}G^{\lambda s}_t&=\rho_t\Bigl(R_{t+1}+\gamma(1-Z_{t+1})\\&\qquad\times\bigl[(1-\lambda)\hat v(S_{t+1})\\&\qquad\quad+\lambda G^{\lambda s}_{t+1}\bigr]\Bigr)\\&\quad+(1-\rho_t)\hat v(S_t).\end{aligned}$$

- (a) Đặt $D_t=G^{\lambda s}_t-\hat v(S_t)$. Chứng minh $D_t=\rho_t\delta_t+\gamma\lambda\rho_t(1-Z_{t+1})D_{t+1}$, rồi suy ra dạng (12.24) của sách, đúng chính xác khi critic cố định:
$$D_t=\rho_t\sum_{k=t}^{T-1}\delta_k\prod_{i=t+1}^{k}\gamma\lambda\rho_i .$$
- (b) Chứng minh rằng khi $\pi'=\pi$, $D_t$ là GAE của Mệnh đề 10.14.
- (c) Chuỗi hai trạng thái: $\gamma=0{,}9$; tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$. Dữ liệu từ $\pi$: $p_A=\tfrac12$, $p_B=\tfrac23$; chính sách đích $\pi'$: $p'_A=0{,}6$, $p'_B=0{,}8$; critic $\hat v=(1;\,1{,}5)$; $\lambda=0{,}8$. Với lượt $s_A\xrightarrow{1}s_B\xrightarrow{1}$ (phần thưởng $0$ rồi $3$), tính $\rho_0$, $\rho_1$, $\delta_0$, $\delta_1$, $D_1$, $D_0$ bằng truy hồi ở (a), và so $D_0$ với GAE $\widehat A_0=1{,}43$ của Ví dụ 10.8.
- (d) Với $\lambda=1$, tính $G^{\lambda s}_0$ trên cả ba loại lượt của $\pi$ và kỳ vọng của nó dưới $\pi$. So sánh với $v_{\pi'}(s_A)=J(\pi')=1{,}696$. Lặp lại phép tính kỳ vọng với $\lambda=0{,}8$.
:::

::: hint Gợi ý Bài tập 10.18
(a) Trừ $\hat v(S_t)$ khỏi hai vế, rồi cộng và trừ $\rho_t\gamma(1-Z_{t+1})\lambda\hat v(S_{t+1})$ trong ngoặc. (d) Lượt chọn hành động 2 tại $s_A$ kết thúc ngay, nên $G^{\lambda s}_0=\rho_0\cdot1+(1-\rho_0)\hat v(s_A)$.
:::

::: solution Lời giải Bài tập 10.18
**Câu (a).** Trừ $\hat v(S_t)$ khỏi định nghĩa, viết gọn $m=1-Z_{t+1}$:
$$
\begin{aligned}
D_t&=\rho_t\bigl(R_{t+1}\\
&\qquad+\gamma m(1-\lambda)\hat v(S_{t+1})\\
&\qquad+\gamma m\lambda G^{\lambda s}_{t+1}\bigr)-\rho_t\hat v(S_t)\\
&=\rho_t\bigl(R_{t+1}+\gamma m\hat v(S_{t+1})\\
&\qquad-\hat v(S_t)\bigr)\\
&\quad+\rho_t\gamma\lambda m\bigl(G^{\lambda s}_{t+1}\\
&\qquad-\hat v(S_{t+1})\bigr)\\
&=\rho_t\delta_t+\gamma\lambda\rho_t\,m\,D_{t+1}.
\end{aligned}
$$
Đẳng thức thứ nhất gộp $\hat v(S_t)-\rho_t\hat v(S_t)$ với $-\hat v(S_t)$; đẳng thức thứ hai cộng và trừ $\rho_t\gamma m\lambda\hat v(S_{t+1})$; đẳng thức thứ ba là định nghĩa của $\delta_t$ và $D_{t+1}$. Với $t+1<T$, $m=1$; với $t=T-1$, $m=0$ và $D_{T-1}=\rho_{T-1}\delta_{T-1}$. Lặp truy hồi:
$$
\begin{aligned}
D_t&=\rho_t\delta_t+\gamma\lambda\rho_t\rho_{t+1}\delta_{t+1}\\
&\quad+(\gamma\lambda)^2\rho_t\rho_{t+1}\rho_{t+2}\\
&\qquad\times\delta_{t+2}+\cdots,
\end{aligned}
$$
dừng ở $k=T-1$, đúng dạng cần chứng minh. Đẳng thức chính xác vì mọi $\delta_k$ dùng cùng $\hat v$; khi critic đổi giữa các bước, Bài tập 10.15 cho thấy xuất hiện thêm các số hạng hiệu chỉnh.

**Câu (b).** Với $\pi'=\pi$, mọi $\rho_i=1$, nên $D_t=\sum_{k=t}^{T-1}(\gamma\lambda)^{k-t}\delta_k$, là Mệnh đề 10.14(a); truy hồi ở (a) trở thành Mệnh đề 10.14(c). Định nghĩa của $G^{\lambda s}_t$ khi đó là truy hồi của lợi tức λ (Bài tập 10.6(a) của ghi chú).

**Câu (c).** $\rho_0=0{,}6/0{,}5=1{,}2$, $\rho_1=0{,}8/\tfrac23=1{,}2$; $\delta_0=0+0{,}9\cdot1{,}5-1=0{,}35$, $\delta_1=3-1{,}5=1{,}5$. Truy hồi lùi:

- $D_1=\rho_1\delta_1=1{,}2\cdot1{,}5=1{,}8$, vì $Z_2=1$;
- $D_0=1{,}2\cdot0{,}35+0{,}72\cdot1{,}2\cdot1{,}8=0{,}42+1{,}5552=1{,}9752$.

GAE theo chính sách cũ là $1{,}43$; hai tỉ số $1{,}2$ cho thấy lượt này có khả năng xảy ra dưới $\pi'$ cao hơn dưới $\pi$, nên nó được nhân trọng số lớn hơn. Kiểm bằng định nghĩa: $G^{\lambda s}_1=1{,}2\cdot3-0{,}2\cdot1{,}5=3{,}3$ và $G^{\lambda s}_0=1{,}2\cdot0{,}9\,(0{,}2\cdot1{,}5+0{,}8\cdot3{,}3)-0{,}2\cdot1=2{,}9752$, nên $D_0=2{,}9752-1=1{,}9752$.

**Câu (d).** Với $\lambda=1$, ba loại lượt ghi bằng dãy hành động $A_0,A_1$ như Bài tập 10.17(c); các tỉ số là $\rho_0=0{,}8$ khi $A_0=2$, $\rho_0=1{,}2$ khi $A_0=1$, $\rho_1=1{,}2$ khi $A_1=1$ và $\rho_1=0{,}6$ khi $A_1=2$:

| $A_0,A_1$ | $\Pr_\pi$ | $G^{\lambda s}_1$ | $G^{\lambda s}_0$ |
| --- | --- | --- | --- |
| $2$ | $\tfrac12$ | — | $1$ |
| $1,1$ | $\tfrac13$ | $3{,}3$ | $3{,}364$ |
| $1,2$ | $\tfrac16$ | $0{,}6$ | $0{,}448$ |

Ở lượt thứ nhất, $G^{\lambda s}_0=0{,}8\cdot1+0{,}2\cdot1=1$; ở lượt thứ hai, $G^{\lambda s}_0=1{,}2\cdot0{,}9\cdot3{,}3-0{,}2\cdot1=3{,}364$; ở lượt thứ ba, $G^{\lambda s}_1=0{,}6\cdot0+0{,}4\cdot1{,}5=0{,}6$ và $G^{\lambda s}_0=1{,}2\cdot0{,}9\cdot0{,}6-0{,}2=0{,}448$. Kỳ vọng: $\tfrac12\cdot1+\tfrac13\cdot3{,}364+\tfrac16\cdot0{,}448=0{,}5+1{,}1213+0{,}0747=1{,}696=v_{\pi'}(s_A)$, dù critic $\hat v=(1;\,1{,}5)$ sai. Với $\lambda=1$, mỗi tầng của định nghĩa là lợi tức một bước có lấy mẫu quan trọng cộng biến điều khiển $(1-\rho_t)\hat v(S_t)$ có kỳ vọng $0$ (Bài tập 10.16(a)), nên lập luận lùi từ bước cuối cho kỳ vọng bằng giá trị của $\pi'$. Với $\lambda=0{,}8$, kỳ vọng là $1{,}5988\ne1{,}696$: phần $(1-\lambda)\hat v(S_{t+1})$ đưa sai số của critic vào kỳ vọng, giống trường hợp đúng chính sách, nơi Mệnh đề 10.15 chỉ cho bảo đảm khi $\lambda=1$ hoặc critic đúng.

**Kiểm tra lại.** Khi $\rho_0=\rho_1=1$ ở (c), $D_0=0{,}35+0{,}72\cdot1{,}5=1{,}43$, khớp Ví dụ 10.8. Lỗi thường gặp: trong truy hồi của (a), nhân $D_{t+1}$ với $\gamma\lambda\rho_t\rho_{t+1}$ thay cho $\gamma\lambda\rho_t$, tức đếm $\rho_{t+1}$ hai lần dù $D_{t+1}$ đã chứa nó, được $D_0=0{,}42+0{,}72\cdot1{,}44\cdot1{,}8=2{,}2862$ ở (c); quên biến điều khiển $(1-\rho_t)\hat v(S_t)$, khi đó lượt có $\rho_t=0$ cho mục tiêu $0$ thay vì giữ nguyên $\hat v(S_t)$.
:::

### Bài tập 10.19. Chính sách Gaussian: hàm điểm, ma trận Fisher, bước gradient tự nhiên và tỉ số PPO

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập: chứng minh dạng hàm điểm của chính sách Gaussian có độ lệch chuẩn học được, dùng nó để lập ma trận Fisher và bước gradient tự nhiên, rồi đo tỉ số chính sách của PPO trên hành động thực.

**Nguồn:** Sutton và Barto (2018), §13.7, Bài tập 13.4 và các đẳng thức (13.19), (13.20), tr. 335–336; mở rộng sang ma trận Fisher, bước gradient tự nhiên và tỉ số của PPO ở (b)–(d), với kỳ vọng theo mật độ thay cho tổng trên tập hành động hữu hạn của Định nghĩa 10.32; ghi chú bài giảng Bài 10, Mục 5.1 (Định nghĩa 10.32, Mệnh đề 10.33, 10.34), Mục 6.1 (Định nghĩa 10.39, Mệnh đề 10.40) và Định nghĩa 09.12 của Bài 09; bộ số ở (b)–(d) tự xây dựng.

::: exercise Bài tập 10.19 (Chính sách Gaussian: hàm điểm, ma trận Fisher, bước gradient tự nhiên và tỉ số PPO)
(Theo Sutton và Barto, 2018, Bài tập 13.4, mở rộng.) Hành động thực, $\mathcal A=\mathbb R$. Tham số chia hai phần, $\theta=(\theta_\mu;\,\theta_\sigma)$, và chính sách có mật độ Gaussian
$$\begin{aligned}&\pi_\theta(a\mid s)\\&=\frac{1}{\sigma\sqrt{2\pi}}\exp\Bigl(-\frac{(a-\mu)^2}{2\sigma^2}\Bigr),\end{aligned}$$
với trung bình $\mu=\mu(s,\theta)=\theta_\mu^\top x_\mu(s)$ và độ lệch chuẩn $\sigma=\sigma(s,\theta)=\exp\bigl(\theta_\sigma^\top x_\sigma(s)\bigr)$; $x_\mu(s)$, $x_\sigma(s)$ là hai véc-tơ đặc trưng của trạng thái.

- (a) Chứng minh hai phần của hàm điểm:
$$\begin{aligned}&\nabla_{\theta_\mu}\log\pi_\theta(a\mid s)\\&=\frac{a-\mu}{\sigma^2}\,x_\mu(s),\\&\nabla_{\theta_\sigma}\log\pi_\theta(a\mid s)\\&=\Bigl(\frac{(a-\mu)^2}{\sigma^2}-1\Bigr)x_\sigma(s).\end{aligned}$$
- (b) Từ đây xét một trạng thái với $x_\mu(s)=x_\sigma(s)=1$, nên $\theta=(\theta_\mu;\,\theta_\sigma)\in\mathbb R^2$, $\mu=\theta_\mu$, $\sigma=e^{\theta_\sigma}$. Chính sách cũ có $\theta_{\mathrm{old}}=(0;\,0)$, tức $\mu=0$, $\sigma=1$. Tính ma trận Fisher $F=\mathbb E_{A\sim\pi_{\mathrm{old}}}\bigl[\psi\psi^\top\bigr]$ tại $\theta_{\mathrm{old}}$, biết các mô men của phân phối chuẩn $\mathbb E[(A-\mu)^2]=\sigma^2$, $\mathbb E[(A-\mu)^3]=0$, $\mathbb E[(A-\mu)^4]=3\sigma^4$.
- (c) Gradient của hàm thay thế ước lượng tại $\theta_{\mathrm{old}}$ là $g=(1;\,0{,}5)$; bán kính miền tin cậy $\kappa=0{,}01$. Tính bước gradient tự nhiên $\Delta^*$ của Mệnh đề 10.34, $\mu$ và $\sigma$ mới. KL giữa hai phân phối chuẩn có dạng đóng
$$\begin{aligned}&D_{\mathrm{KL}}\bigl(\mathcal N(\mu_1,\sigma_1^2)\\&\qquad\Vert\mathcal N(\mu_2,\sigma_2^2)\bigr)\\&=\log\frac{\sigma_2}{\sigma_1}\\&\quad+\frac{\sigma_1^2+(\mu_1-\mu_2)^2}{2\sigma_2^2}-\frac12 .\end{aligned}$$
Tính KL thật theo chiều cũ‖mới và mới‖cũ, và so sánh với giá trị bậc hai $\tfrac12\Delta^{*\top}F\Delta^*$.
- (d) Bộ đệm có ba hành động lấy từ chính sách cũ, $a=0{,}5$, $a=2$, $a=-2$, đều có lợi thế dương. Với chính sách mới ở (c), tính tỉ số $\rho(a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$ của ba mẫu. Với $\epsilon=0{,}2$, mẫu nào nằm trên đoạn phẳng của mục tiêu cắt? Tìm giới hạn của $\rho(a)$ khi $\lvert a\rvert\to\infty$.
:::

::: hint Gợi ý Bài tập 10.19
(a) $\log\pi_\theta(a\mid s)=-\log\sigma-\tfrac12\log(2\pi)-(a-\mu)^2/(2\sigma^2)$, với $\log\sigma=\theta_\sigma^\top x_\sigma(s)$. (b) Phần tử ngoài đường chéo chứa mô men bậc ba. (c) $F$ chéo nên $F^{-1}g$ tính theo từng tọa độ. (d) $\log\rho(a)=-\log\sigma-\dfrac{(a-\mu)^2}{2\sigma^2}+\dfrac{a^2}{2}$ khi chính sách cũ là $\mathcal N(0,1)$.
:::

::: solution Lời giải Bài tập 10.19
**Câu (a).** Lấy logarit của mật độ:
$$\begin{aligned}&\log\pi_\theta(a\mid s)\\&=-\theta_\sigma^\top x_\sigma(s)-\tfrac12\log(2\pi)\\&\quad-\frac{(a-\mu)^2}{2}e^{-2\theta_\sigma^\top x_\sigma(s)}.\end{aligned}$$
Theo $\theta_\mu$: chỉ số hạng cuối phụ thuộc $\theta_\mu$, qua $\mu=\theta_\mu^\top x_\mu(s)$, và $\nabla_{\theta_\mu}\bigl[-(a-\mu)^2/(2\sigma^2)\bigr]=\dfrac{a-\mu}{\sigma^2}\,x_\mu(s)$. Theo $\theta_\sigma$: số hạng đầu cho $-x_\sigma(s)$; số hạng cuối có $\nabla_{\theta_\sigma}e^{-2\theta_\sigma^\top x_\sigma(s)}=-2\sigma^{-2}x_\sigma(s)$, nên cho $\dfrac{(a-\mu)^2}{\sigma^2}x_\sigma(s)$. Cộng lại được phần thứ hai. Phần theo $\theta_\mu$ là hàm điểm của chính sách Gaussian với phương sai cố định của Bài 09; phần theo $\theta_\sigma$ dương khi hành động rơi xa trung bình hơn một độ lệch chuẩn, nên một lợi thế dương ở hành động đó làm $\sigma$ tăng.

**Câu (b).** Tại $\theta_{\mathrm{old}}$, $\psi(a)=\bigl(a;\,a^2-1\bigr)$. Ba phần tử của $F$:

- $F_{\mu\mu}=\mathbb E[A^2]/\sigma^4=1$;
- $F_{\mu\sigma}=\mathbb E[A(A^2-1)]=\mathbb E[A^3]-\mathbb E[A]=0$;
- $F_{\sigma\sigma}=\mathbb E[(A^2-1)^2]=\mathbb E[A^4]-2\mathbb E[A^2]+1=3-2+1=2$.

Vậy $F=\begin{pmatrix}1&0\\0&2\end{pmatrix}$, xác định dương. Với $\sigma$ tổng quát, $F=\operatorname{diag}(1/\sigma^2;\,2)$: hướng của trung bình được đo theo đơn vị $\sigma$, còn hướng của $\log\sigma$ có độ cong không đổi.

**Câu (c).** $F^{-1}g=(1;\,0{,}25)$ và $g^\top F^{-1}g=1+0{,}5\cdot0{,}25=1{,}125$. Theo Mệnh đề 10.34(a), hệ số độ dài là $\sqrt{2\cdot0{,}01/1{,}125}=0{,}1333$, nên
$$\Delta^*=(0{,}1333;\,0{,}0333),$$
tức $\mu=0{,}1333$ và $\sigma=e^{0{,}0333}=1{,}0339$. Giá trị bậc hai: $\tfrac12(0{,}1333^2+2\cdot0{,}0333^2)=\tfrac12(0{,}01778+0{,}00222)=0{,}01$. KL thật:

- cũ‖mới, với $\mu_1=0$, $\sigma_1=1$, $\mu_2=0{,}1333$, $\sigma_2=1{,}0339$: $0{,}0333+\dfrac{1+0{,}01778}{2\cdot1{,}0689}-0{,}5=0{,}0333+0{,}4761-0{,}5=0{,}00940$;
- mới‖cũ: $-0{,}0333+\dfrac{1{,}0689+0{,}01778}{2}-0{,}5=0{,}01003$.

Hai chiều KL lệch khỏi $\kappa=0{,}01$ chưa tới $6\%$ và lệch nhau ở bậc ba, như với chính sách softmax (Ví dụ 10.15). Bước gradient thường $\alpha g$ đi theo hướng $(2;\,1)$; bước tự nhiên đi theo hướng $(4;\,1)$, vì $F$ phạt hướng của $\theta_\sigma$ gấp đôi hướng của $\theta_\mu$.

**Câu (d).** Với $\mu=0{,}1333$, $\sigma=1{,}0339$, $\sigma^2=1{,}0689$, ta có $\log\rho=-0{,}0333-(a-\mu)^2/(2\sigma^2)+a^2/2$. Số hạng $(a-\mu)^2/(2\sigma^2)$ bằng $0{,}0629$, $1{,}6299$, $2{,}1288$ tại $a=0{,}5$, $2$, $-2$, nên:

| $a$ | $\log\rho$ | $\rho$ |
| --- | --- | --- |
| $0{,}5$ | $0{,}0288$ | $1{,}029$ |
| $2$ | $0{,}3368$ | $1{,}400$ |
| $-2$ | $-0{,}1621$ | $0{,}850$ |

Lợi thế của cả ba mẫu dương, nên theo Mệnh đề 10.40(a), mẫu $a=2$, với $\rho=1{,}400>1{,}2$, nằm trên đoạn phẳng và có gradient bằng $0$; mẫu $a=0{,}5$ ở trong khoảng cắt; mẫu $a=-2$, với $\rho=0{,}850$, cũng ở trong khoảng, không bị cắt. Khi $\lvert a\rvert\to\infty$,
$$\begin{aligned}&\log\rho(a)\\&=-\log\sigma+\frac{a^2}{2}\Bigl(1-\frac1{\sigma^2}\Bigr)\\&\quad+\frac{a\mu}{\sigma^2}-\frac{\mu^2}{2\sigma^2},\end{aligned}$$
với $1-1/\sigma^2=0{,}0645>0$, nên $\rho(a)\to\infty$. KL của bước chỉ khoảng $0{,}0094$, nhưng tỉ số của các mẫu ở đuôi phân phối không bị chặn. Do đó, trên hành động thực, ràng buộc KL không giữ được mọi tỉ số trong $[1-\epsilon,1+\epsilon]$.

**Kiểm tra lại.** Tại $\theta_{\mathrm{old}}$, hàm điểm có kỳ vọng $0$: $\mathbb E[A]=0$ và $\mathbb E[A^2-1]=0$, đúng Mệnh đề 09.17. Lỗi thường gặp: ở (a) lấy đạo hàm theo $\sigma$ thay vì theo $\theta_\sigma$, được $\bigl((a-\mu)^2/\sigma^2-1\bigr)/\sigma$; ở (b) quên số hạng $+1$, được $F_{\sigma\sigma}=1$ và bước $\Delta^*$ sai; ở (d) bỏ thừa số chuẩn hóa $1/\sigma$ của mật độ, làm $\log\rho$ lệch $0{,}0333$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 10.20. REINFORCE có đường cơ sở trên hành lang ngắn

**Mức độ:** vận dụng (lập trình). Mục tiêu học tập: cài đặt REINFORCE có đường cơ sở theo hai cách cập nhật, đo tác dụng của đường cơ sở lên tốc độ học, và kiểm điều kiện của Mệnh đề 10.2 cùng điều kiện ổn định của bước học critic trên một môi trường có độ dài lượt thay đổi.

**Nguồn:** Sutton và Barto (2018), §13.4, hộp giả mã "REINFORCE with Baseline" và Hình 13.2, tr. 330–331, Ví dụ 13.1, tr. 323; ghi chú bài giảng Bài 10, Mục 2.1–2.3 (Định nghĩa 10.1, Mệnh đề 10.2, Ví dụ 10.4, Thuật toán 10.6); Bài tập 09.19 của tệp bài tập Bài 09 cho REINFORCE trên cùng môi trường. Kết quả số trong lời giải lấy từ mã tham chiếu ở lời giải (a) với các hạt giống ghi tại chỗ.

::: exercise Bài tập 10.20 (REINFORCE có đường cơ sở trên hành lang ngắn)
(Theo Sutton và Barto, 2018, §13.4 và Hình 13.2.) Hành lang ngắn đảo hành động: ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích); phần thưởng $-1$ mỗi bước; $\gamma=1$; hành động 1 "sang phải", hành động 2 "sang trái"; ở $s_2$ hai hành động bị đảo; sang trái tại $s_1$ thì đứng yên. Chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ ở mọi ô, nên $p=\pi_\theta(1\mid s)=1/\bigl(1+e^{-(\theta_1-\theta_2)}\bigr)$, $\psi_\theta(s,1)=(1-p)(1;\,-1)$, $\psi_\theta(s,2)=-p\,(1;\,-1)$. Khởi tạo $\theta_0=(0;\,\log19)$, tức $p=0{,}05$. Đường cơ sở là critic một tham số $\hat v(s,w)=w$ ở mọi ô, như sách dùng cho Hình 13.2, khởi tạo $w=0$. Lượt bị cắt sau $1000$ bước nếu chưa tới đích. Với $T$ là độ dài lượt, $G_t=-(T-t)$. Thuật toán 10.6 được dùng với $\gamma=1$, theo quy ước chiết khấu ở phần Hướng dẫn và ký hiệu.

Hai cách cập nhật sau một lượt:

- *Cập nhật theo từng bước* (hộp giả mã của sách): với $t=0,\dots,T-1$, tính $\delta=G_t-w$, rồi $w\leftarrow w+\alpha_w\delta$ và $\theta\leftarrow\theta+\alpha_\theta\,\delta\,\psi_\theta(S_t,A_t)$, với $\psi$ tính tại $\theta$ hiện tại.
- *Cập nhật một lần* (Thuật toán 10.6): giữ $\theta_{\mathrm{old}}$, $w_{\mathrm{old}}$ cố định trong cả lượt, rồi $w\leftarrow w_{\mathrm{old}}+\alpha_w\sum_t(G_t-w_{\mathrm{old}})$ và $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_t(G_t-w_{\mathrm{old}})\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$.

Khung chương trình bằng Python, chỉ dùng thư viện chuẩn. Hàm `step(s, a)` trả ô kế tiếp, với `4` là đích. Hàm `per_step_update` thực hiện một bước của cách thứ nhất cho một cặp $(G_t,A_t)$; hàm `batch_update` thực hiện cách thứ hai cho dãy hành động `actions` của một lượt; cả hai trả `(theta, w)` mới. Hàm `run` sinh mỗi hành động bằng `1 if rng.random() < p else 2`, với `mode` bằng `"per_step"` hoặc `"batch"`, và trả danh sách $G_0$ của các lượt, $\theta$ và $w$ cuối. Một lần chạy được coi là *tràn số* khi `math.exp` báo `OverflowError` hoặc một trong $\theta_1$, $\theta_2$, $w$ không còn hữu hạn sau một lần cập nhật; khi đó `run` dừng và trả `None`.

```python
import math, random

def step(s, a):
    ...

def prob1(theta):
    return 1 / (1 + math.exp(-(theta[0] - theta[1])))

def per_step_update(theta, w, G, a, alpha_theta, alpha_w):
    ...

def batch_update(theta, w, actions, alpha_theta, alpha_w):
    ...

def run(mode, alpha_theta, alpha_w, episodes, rng,
        theta0=(0.0, math.log(19)), cap=1000):
    ...

th, w = per_step_update([0.0, 0.0], 0.0, -5, 1, 2**-9, 2**-6)
assert math.isclose(w, -0.078125)
assert math.isclose(th[0], -0.0048828125)
th, w = batch_update([0.0, 0.0], -10.0, [1, 1, 1, 2, 1],
                     2**-9, 2**-9)
assert math.isclose(th[0], 0.0185546875)
assert math.isclose(w, -9.931640625)
```

Mỗi cấu hình gồm $100$ lần chạy, mỗi lần $1000$ lượt, gọi `run` liên tiếp với cùng một bộ sinh `rng = random.Random(seed)`. Với mỗi cấu hình, báo cáo $G_0$ trung bình trên các lượt $1$–$100$, $101$–$200$, $901$–$1000$, $p$ và $w$ cuối, mỗi đại lượng lấy trung bình trên các lần chạy không tràn số, kèm sai số chuẩn.

- (a) Hoàn thiện ba hàm và `run`. Kiểm hai bước tính tay ứng với bốn câu `assert`: bước đầu của cách thứ nhất tại $\theta=(0;\,0)$, $w=0$, $G_0=-5$, $A_0=1$, $\alpha_\theta=2^{-9}$, $\alpha_w=2^{-6}$; và cách thứ hai trên lượt $1,1,1,2,1$ tại $\theta=(0;\,0)$ với $w_{\mathrm{old}}=-10$, $\alpha_\theta=\alpha_w=2^{-9}$.
- (b) Chạy cách thứ nhất với $\alpha_\theta=2^{-9}$, $\alpha_w=2^{-6}$ (bước học của Hình 13.2), hạt giống $2026$, và REINFORCE không đường cơ sở cập nhật theo từng bước ($\alpha_\theta=2^{-13}$, $\alpha_w=0$, nên $w\equiv0$), hạt giống $2027$. So sánh các kết quả với $J(p^*)=-(6+4\sqrt2)\approx-11{,}66$.
- (c) Chạy cách thứ hai với $\alpha_\theta=2^{-9}$ và hai bước học critic: $\alpha_w=2^{-6}$, hạt giống $2028$; $\alpha_w=2^{-9}$, hạt giống $2029$. Báo cáo số lần chạy tràn số. Giải thích kết quả bằng thừa số của $w_{\mathrm{old}}$ trong cập nhật của critic. Với $\alpha_w=2^{-9}$, chạy thêm các hạt giống $1,\dots,10$ và đếm các lần chạy *bị kẹt*, tức mọi lượt trong $100$ lượt cuối đều bị cắt ở $1000$ bước; giải thích hiện tượng này.
- (d) Xác định cách nào thỏa hai điều kiện "đường cơ sở giữ cố định trong suốt lượt" và "mọi hàm điểm tính tại cùng $\theta$" của Mệnh đề 10.2. Xác định điểm dừng $w^*$ của cập nhật critic ở cách thứ hai theo số lần thăm kỳ vọng $\eta(s)$ và $v_\pi$, tính $w^*$ tại $p^*$ với $\eta=(5{,}828;\,4{,}121;\,1{,}707)$ và $v_\pi=(-11{,}657;\,-9{,}950;\,-5{,}121)$, rồi so với $w$ cuối của (c).
:::

::: hint Gợi ý Bài tập 10.20
Với hai hành động và đặc trưng đơn vị, chỉ cần một số vô hướng $\delta\,(\mathbb 1\{a=1\}-p)$: cộng nó vào $\theta_1$ và trừ khỏi $\theta_2$ sau khi nhân bước học. Ở (c), viết cập nhật của critic thành $w\leftarrow(1-\alpha_wT)\,w_{\mathrm{old}}+\alpha_w\sum_tG_t$, và xét hàm điểm khi $p$ gần $0$ hoặc $1$. Ở (d), dùng $\mathbb E\bigl[\sum_{t<T}G_t\bigr]=\mathbb E\bigl[\sum_{t<T}v_\pi(S_t)\bigr]$.
:::

::: solution Lời giải Bài tập 10.20
**Câu (a).** Mã tham chiếu:

```python
import math, random

def step(s, a):
    if s == 1:
        return 2 if a == 1 else 1
    if s == 2:
        return 1 if a == 1 else 3
    return 4 if a == 1 else 2

def prob1(theta):
    return 1 / (1 + math.exp(-(theta[0] - theta[1])))

def per_step_update(theta, w, G, a, alpha_theta, alpha_w):
    p = prob1(theta)
    delta = G - w
    c = delta * ((1 if a == 1 else 0) - p)
    return ([theta[0] + alpha_theta * c, theta[1] - alpha_theta * c],
            w + alpha_w * delta)

def batch_update(theta, w, actions, alpha_theta, alpha_w):
    p, T = prob1(theta), len(actions)
    c = sum((-(T - t) - w) * ((1 if a == 1 else 0) - p)
            for t, a in enumerate(actions))
    s = sum(-(T - t) - w for t in range(T))
    return ([theta[0] + alpha_theta * c, theta[1] - alpha_theta * c],
            w + alpha_w * s)

def run(mode, alpha_theta, alpha_w, episodes, rng,
        theta0=(0.0, math.log(19)), cap=1000):
    theta, w, returns = list(theta0), 0.0, []
    try:
        for _ in range(episodes):
            p, s, actions = prob1(theta), 1, []
            while s != 4 and len(actions) < cap:
                a = 1 if rng.random() < p else 2
                actions.append(a)
                s = step(s, a)
            T = len(actions)
            returns.append(-T)
            if mode == "per_step":
                for t, a in enumerate(actions):
                    theta, w = per_step_update(theta, w, -(T - t), a,
                                               alpha_theta, alpha_w)
            else:
                theta, w = batch_update(theta, w, actions,
                                        alpha_theta, alpha_w)
            if not all(math.isfinite(x) for x in (*theta, w)):
                return None
    except OverflowError:
        return None
    return returns, theta, w

def experiment(mode, alpha_theta, alpha_w, seed):
    rng = random.Random(seed)
    return [run(mode, alpha_theta, alpha_w, 1000, rng)
            for _ in range(100)]
```

Hai bước tính tay:

- cách thứ nhất: $\delta=-5$, $w=-5/64=-0{,}078125$, $c=-5\cdot0{,}5=-2{,}5$, $\theta_1=-2{,}5/512=-0{,}0048828125$;
- cách thứ hai: $G_t-w_{\mathrm{old}}=5,6,7,8,9$, $c=0{,}5(5+6+7+9)-0{,}5\cdot8=9{,}5$, $\theta_1=9{,}5/512=0{,}0185546875$, $w=-10+35/512=-9{,}931640625$.

Lượt thứ hai là lượt của Ví dụ 10.4 với đường cơ sở hằng $-10$ thay cho $v_\pi$.

**Câu (b).** Kết quả (không lần chạy nào tràn số), trong ngoặc là sai số chuẩn trên $100$ lần chạy:

| lượt | đường cơ sở | REINFORCE |
| --- | --- | --- |
| $1$–$100$ | $-20{,}23$ ($0{,}48$) | $-47{,}45$ ($0{,}73$) |
| $101$–$200$ | $-12{,}20$ ($0{,}13$) | $-25{,}75$ ($0{,}52$) |
| $901$–$1000$ | $-12{,}07$ ($0{,}10$) | $-12{,}42$ ($0{,}09$) |
| $p$ cuối | $0{,}603$ ($0{,}009$) | $0{,}486$ ($0{,}003$) |

Ba hàng đầu là $G_0$ trung bình trên các lượt ghi ở cột đầu. Cột thứ hai là REINFORCE có đường cơ sở, với $\alpha_\theta=2^{-9}$, $\alpha_w=2^{-6}$, hạt giống $2026$; cột thứ ba dùng $\alpha_\theta=2^{-13}$, hạt giống $2027$. Đường có đường cơ sở tới gần $-12$ sau khoảng $100$ lượt, còn REINFORCE cần vài trăm lượt; sau $1000$ lượt cả hai ở gần $-12$, không vượt $J(p^*)\approx-11{,}66$ quá sai số lấy mẫu. Hình 13.2 của nguồn, trung bình trên $100$ lần chạy, có cùng dạng. Theo chú thích Hình 13.2, $2^{-13}$ là bước học tốt nhất của REINFORCE không đường cơ sở, tới lũy thừa gần nhất của $2$; với đường cơ sở, bước học chính sách lớn gấp $2^4=16$ lần vẫn học ổn định trong $100$ lần chạy trên. Không có đường cơ sở, mọi $G_t$ đều âm và lớn, nên một bước lớn trên một lượt dài đẩy $p$ đi xa theo hướng của riêng lượt đó (Ví dụ 10.2); với $G_t-w$, các hệ số quanh $0$ và có cả hai dấu.

**Câu (c).** Kết quả:

- $\alpha_w=2^{-6}$, hạt giống $2028$: $16$ lần chạy tràn số, ở lần cập nhật sau một lượt trong khoảng từ lượt thứ $7$ đến lượt thứ $272$; trước khi tràn, mỗi lần chạy này đã có ít nhất bốn lượt dài hơn $128$ bước, trong đó ít nhất một lượt bị cắt ở $1000$ bước. Trên $84$ lần chạy còn lại, $G_0$ trung bình là $-18{,}15$ ($0{,}45$), $-11{,}79$ ($0{,}12$), $-11{,}92$ ($0{,}12$) ở ba nhóm lượt; $p$ cuối $0{,}578$ ($0{,}008$), $w$ cuối $-10{,}51$ ($0{,}50$).
- $\alpha_w=2^{-9}$, hạt giống $2029$: không lần chạy nào tràn số; $G_0$ trung bình là $-22{,}42$ ($3{,}03$), $-11{,}80$ ($0{,}09$), $-11{,}98$ ($0{,}11$); $p$ cuối $0{,}580$ ($0{,}008$), $w$ cuối $-10{,}33$ ($0{,}14$).

Cập nhật critic của cách thứ hai là
$$\begin{aligned}w&\leftarrow(1-\alpha_wT)\,w_{\mathrm{old}}\\&\quad+\alpha_w\sum_{t<T}G_t .\end{aligned}$$
Thừa số $1-\alpha_wT$ có trị tuyệt đối nhỏ hơn $1$ khi và chỉ khi $T<2/\alpha_w$. Với $\alpha_w=2^{-6}$, ngưỡng là $128$ bước; ở đầu quá trình học, $p=0{,}05$ cho $\mathbb E[T]\approx82$ và nhiều lượt dài hàng trăm bước, nên $\lvert1-\alpha_wT\rvert$ lên tới $1000/64-1\approx14{,}6$. Mỗi lượt như vậy nhân $w$ với một thừa số lớn và đổi dấu nó, hệ số $G_t-w$ lớn theo, và $\theta$ tràn số sau một chuỗi lượt dài. Với $\alpha_w=2^{-9}$, ngưỡng là $1024$ bước, vượt giới hạn cắt $1000$. Cách thứ nhất nhân $w$ với $1-\alpha_w\in(0,1)$ ở mỗi bước, nên ổn định với mọi độ dài lượt.

Với $\alpha_w=2^{-9}$ và các hạt giống $1,\dots,10$, không lần chạy nào tràn số, nhưng $6$ trong $1000$ lần chạy bị kẹt: $4$ lần với $p$ cuối gần $0$ (hạt giống $5$, $6$, $7$, $9$) và $2$ lần với $p$ cuối gần $1$ (hạt giống $2$, $10$). Ở các lượt đầu, $w$ còn gần $0$, nên hệ số $G_t-w$ gần bằng $G_t$, và bước $\alpha_\theta=2^{-9}$, lớn gấp $16$ lần bước tốt nhất của REINFORCE, có thể đẩy $p$ về gần $0$ hoặc $1$ sau một lượt dài. Khi $p$ gần $0$, tác tử đứng yên ở $s_1$; khi $p$ gần $1$, tác tử đi qua lại giữa $s_1$ và $s_2$; cả hai trường hợp đều chạm giới hạn $1000$ bước ở mọi lượt. Hàm điểm $\psi=(\mathbb 1\{a=1\}-p)(1;\,-1)$ gần $0$ ở hành động gần như chắc chắn được chọn, nên $\theta$ hầu như không đổi và lần chạy không thoát ra. Hạt giống $8$ có thêm một lần chạy thoát chậm: $40$ trong $100$ lượt cuối vẫn bị cắt ở $1000$ bước và $p$ cuối là $0{,}246$, nên trung bình của hạt giống đó ở lượt $901$–$1000$ là $-16{,}18$ ($4{,}16$). Một lần chạy bị kẹt có $G_0=-1000$ ở mọi lượt, nên trung bình trên $100$ lần chạy của hạt giống đó lệch khoảng $-10$ và sai số chuẩn tăng lên khoảng $10$; khi báo cáo, cần ghi số lần chạy bị kẹt bên cạnh trung bình.

**Câu (d).** Chỉ cách thứ hai thỏa cả hai điều kiện. Ở cách thứ nhất, giá trị $w$ dùng tại bước $t$ đã được cập nhật bằng $G_0,\dots,G_{t-1}$ của chính lượt, mà các lợi tức này chứa phần thưởng đến sau $A_t$; do đó $B_t=w$ phụ thuộc $A_t$ và các hành động sau đó, và điều kiện của Định nghĩa 10.1 không thỏa. Ngoài ra $\psi$ được tính tại $\theta$ đã đổi trong lượt, trong khi lượt được sinh bởi $\theta$ đầu lượt. Hai sự phụ thuộc này đi qua các bước cập nhật trong lượt, nên nhỏ khi $\alpha_w$ và $\alpha_\theta$ nhỏ.

Điểm dừng của cập nhật critic ở cách thứ hai thỏa $\mathbb E\bigl[\sum_{t<T}(G_t-w^*)\bigr]=0$. Theo tính chất tháp, $\mathbb E[G_t\mid S_t]=v_\pi(S_t)$, nên
$$\begin{aligned}w^*&=\frac{\mathbb E\bigl[\sum_{t<T}v_\pi(S_t)\bigr]}{\mathbb E[T]}\\&=\frac{\sum_s\eta(s)\,v_\pi(s)}{\sum_s\eta(s)} .\end{aligned}$$
Tại $p^*$: tử số $5{,}828\cdot(-11{,}657)+4{,}121\cdot(-9{,}950)+1{,}707\cdot(-5{,}121)=-117{,}68$, mẫu số $11{,}657=\mathbb E[T]$, nên $w^*\approx-10{,}10$. Giá trị $-10{,}33$ ($0{,}14$) của (c) gần $w^*$; phần chênh đến từ việc $p$ cuối thay đổi giữa các lần chạy và $w$ vẫn dao động theo từng lượt. Đường cơ sở hằng không bằng $v_\pi(s)$ ở ô nào, nhưng vẫn không làm chệch (Mệnh đề 10.2).

**Kiểm tra lại.** $G_0$ trung bình của các lần chạy không bị kẹt không vượt $J(p^*)\approx-11{,}66$ quá sai số lấy mẫu. Lỗi thường gặp: cập nhật $\theta$ bằng $\delta$ tính sau khi đã cập nhật $w$, khác hộp giả mã; dùng $\psi$ tại $\theta$ mới trong cách thứ hai; tính $G_t$ từ đầu lượt thay vì từ cuối lượt; quên cắt lượt ở $1000$ bước, khiến chương trình không dừng khi $p$ gần $0$ hoặc $1$; dùng một bộ sinh mới cho mỗi lần chạy, khiến số liệu không khớp các số trên.
:::

### Bài tập 10.21. Thiết kế, dịch và đổi thang phần thưởng khi huấn luyện PPO trên CartPole

**Mức độ:** vận dụng. Mục tiêu học tập: so hai thiết kế phần thưởng của một bài toán có kết thúc qua hàm mục tiêu $J$, đánh giá các phép biến đổi phần thưởng và lợi thế trong một cài đặt PPO, và phân biệt phép biến đổi đổi bài toán với phép biến đổi chỉ đổi thang của bước.

**Nguồn:** Sutton và Barto (2018), §3.5, Bài tập 3.15 và 3.16, tr. 61, mở rộng sang một thiết kế phần thưởng thứ hai, mục tiêu cắt của PPO và chuẩn hóa phần thưởng, lợi thế; ghi chú bài giảng Bài 10, Mục 6.1 (Định nghĩa 10.39, Mệnh đề 10.40), Mục 6.3 (Định nghĩa 10.46), Mục 6.5 (Nhận xét 10.50) và Tình huống 10.1; dữ kiện CartPole theo Tình huống 10.1; các chính sách $\pi_L$ và thiết kế phần thưởng thứ hai ở (b) tự xây dựng.

::: exercise Bài tập 10.21 (Thiết kế, dịch và đổi thang phần thưởng khi huấn luyện PPO trên CartPole)
(Theo Sutton và Barto, 2018, Bài tập 3.15 và 3.16, mở rộng.) CartPole: mỗi bước giữ được cột cho phần thưởng $1$, kể cả bước cột đổ; lượt của MDP kết thúc ($Z=1$) khi cột đổ; giới hạn $500$ bước là cắt ngắn ($U=1$), không thuộc MDP; $\gamma=0{,}99$, $\lambda=0{,}95$, $\epsilon=0{,}2$. Xét các chính sách $\pi_L$ giữ cột đúng $L$ bước rồi để cột đổ, $T=L$, và chính sách $\pi_\infty$ không bao giờ để cột đổ, trong MDP không có giới hạn thời gian.

- (a) Tính $J(\pi_{10})$, $J(\pi_{100})$, $J(\pi_\infty)$.
- (b) Một thiết kế phần thưởng khác cho phần thưởng $0$ ở mọi bước, trừ bước cột đổ nhận $-1$; viết $J'$ cho hàm mục tiêu tương ứng. Tính $J'(\pi_{10})$, $J'(\pi_{100})$, $J'(\pi_\infty)$. Chứng minh rằng với mọi chính sách, $J=(1+\gamma J')/(1-\gamma)$, và suy ra hai thiết kế có cùng thứ tự chính sách. Thiết kế thứ hai bằng thiết kế gốc cộng hằng $c=-1$ rồi thêm phạt $-1$ ở bước cột đổ; theo Bài tập 10.14(b), phép cộng hằng $c=-1$ riêng nó làm mọi chính sách có cùng giá trị. Xác định thành phần nào của thiết kế thứ hai giữ lại thứ tự.
- (c) Một bản cài đặt chia mọi phần thưởng cho một hằng $\varsigma_0>0$. Chứng minh thứ tự của các chính sách theo $J$ không đổi. Chứng minh số hạng cắt có tính thuần nhất dương, $\ell^{\mathrm{CLIP}}_t$ với lợi thế $k\widehat A_t$ bằng $k\,\ell^{\mathrm{CLIP}}_t$ với lợi thế $\widehat A_t$, với mọi $k>0$, và suy ra chia mọi lợi thế cho một hằng dương không đổi tập cực đại của $\mathcal L^{\mathrm{CLIP}}$.
- (d) Nhận xét 10.50 ghi rằng chuẩn hóa phần thưởng chia cho độ lệch chuẩn chạy của lợi tức chiết khấu. Một sinh viên đề xuất trừ thêm trung bình chạy của phần thưởng, khởi tạo ở $0$, trước khi chia. Xác định giá trị mà trung bình chạy này tiến tới trên CartPole với thiết kế gốc, và hậu quả đối với tín hiệu học của PPO. So sánh với chuẩn hóa lợi thế theo mini-batch của Định nghĩa 10.46 và xác định phép nào đổi bài toán, phép nào chỉ đổi mục tiêu cắt.
:::

::: hint Gợi ý Bài tập 10.21
Với phần thưởng $1$ mỗi bước và $T=L$, $J(\pi_L)=\sum_{t=0}^{L-1}\gamma^t=(1-\gamma^L)/(1-\gamma)$. Ở (b), trên một lượt kết thúc tại $T$, lợi tức của thiết kế thứ hai là $-\gamma^{T-1}$; viết $\gamma^T=\gamma\cdot\gamma^{T-1}$. Ở (c), xét riêng hai dấu của $\widehat A_t$ theo Mệnh đề 10.40.
:::

::: solution Lời giải Bài tập 10.21
**Câu (a).** $J(\pi_L)=(1-0{,}99^L)/0{,}01$:

- $J(\pi_{10})=(1-0{,}9044)/0{,}01=9{,}56$;
- $J(\pi_{100})=(1-0{,}3660)/0{,}01=63{,}40$;
- $J(\pi_\infty)=1/0{,}01=100$.

Giữ cột càng lâu, $J$ càng lớn.

**Câu (b).** Trên lượt kết thúc tại $T$, chỉ phần thưởng $R_T=-1$ khác $0$, nên $G'_0=-\gamma^{T-1}$; khi cột không bao giờ đổ, $G'_0=0$. Do đó $J'(\pi_{10})=-0{,}99^9=-0{,}9135$, $J'(\pi_{100})=-0{,}99^{99}=-0{,}3697$, $J'(\pi_\infty)=0$, cùng thứ tự với (a).

Với thiết kế gốc, $G_0=(1-\gamma^T)/(1-\gamma)$ khi $T<\infty$ và $G_0=1/(1-\gamma)$ khi $T=\infty$. Vì $\gamma^T=\gamma\cdot\gamma^{T-1}=-\gamma G'_0$, ta có trên mọi lượt
$$G_0=\frac{1+\gamma G'_0}{1-\gamma},$$
kể cả khi $T=\infty$, vì khi đó $G'_0=0$. Lấy kỳ vọng hai vế theo một chính sách bất kỳ được $J=(1+\gamma J')/(1-\gamma)$. Đây là một hàm affine tăng của $J'$, với hệ số $\gamma/(1-\gamma)=99>0$, nên hai thiết kế xếp mọi cặp chính sách theo cùng thứ tự và có cùng chính sách tối ưu. Kiểm với $\pi_{100}$: $(1-0{,}99\cdot0{,}3697)/0{,}01=63{,}40$.

Thành phần giữ lại thứ tự là phạt $-1$ ở bước cột đổ. Phép cộng $c=-1$ đưa mọi phần thưởng về $0$, nên $J_{-1}\equiv0$ (Bài tập 10.14(b)); phạt ở bước kết thúc có giá trị chiết khấu $-\gamma^{T-1}$, tăng theo độ dài lượt, nên lượt dài hơn vẫn được ưu tiên.

**Câu (c).** Phần thưởng $r/\varsigma_0$ cho lợi tức $G_t/\varsigma_0$ trên mọi lượt, nên hàm mục tiêu mới bằng $J(\pi)/\varsigma_0$ với mọi $\pi$; chia cho một số dương giữ thứ tự. Với $k>0$: nếu $\widehat A_t>0$ thì $k\widehat A_t>0$ và theo Mệnh đề 10.40(a), số hạng cắt là $k\widehat A_t\min(\rho_t,1+\epsilon)$; nếu $\widehat A_t<0$, theo (b) của mệnh đề, số hạng cắt là $k\widehat A_t\max(\rho_t,1-\epsilon)$; nếu $\widehat A_t=0$, cả hai bằng $0$. Trong cả ba trường hợp, số hạng cắt với lợi thế $k\widehat A_t$ bằng $k$ lần số hạng cắt với lợi thế $\widehat A_t$. Lấy trung bình trên bộ đệm: $\mathcal L^{\mathrm{CLIP}}$ của $k\widehat A$ bằng $k$ lần $\mathcal L^{\mathrm{CLIP}}$ của $\widehat A$, nên hai mục tiêu có cùng tập cực đại; gradient chỉ nhân với $k$, tương đương đổi bước học. Phép chia cho một hằng giữ bài toán; khi $\varsigma_0$ là độ lệch chuẩn chạy, đổi theo thời gian, hàm được tối ưu đổi theo từng giai đoạn của quá trình học, như Nhận xét 10.50 ghi.

**Câu (d).** Với thiết kế gốc, mọi phần thưởng thu được đều bằng $1$, nên trung bình chạy khởi tạo ở $0$ tăng dần về $1$ và phần thưởng sau khi trừ giảm dần về $0$. Theo Bài tập 10.14(b) với $c=-1$, khi đó mọi chính sách có cùng giá trị; với critic học đúng giá trị $0$, mọi sai số TD và mọi lợi thế GAE bằng $0$, nên mục tiêu cắt không còn gradient và PPO không học. Trước đó, phần thưởng đã trừ còn dương nhưng nhỏ dần, nên tín hiệu ưu tiên lượt dài yếu dần theo thời gian. Phép trừ trung bình của phần thưởng vì vậy đổi bài toán.

Chuẩn hóa lợi thế theo mini-batch trừ trung bình của $\widehat A^{\mathrm{raw}}$ và chia cho độ lệch chuẩn sau khi GAE đã được tính trên phần thưởng gốc, nên:

- giá trị của các chính sách theo $J$ không đổi;
- phép chia chỉ đổi thang của bước, theo (c);
- phép trừ đổi tập mẫu bị cắt của $\mathcal L^{\mathrm{CLIP}}$ (Bài tập 10.16(d)), và không là đường cơ sở đúng nghĩa vì trung bình được tính từ chính mini-batch (Mục 6.3 của ghi chú).

Tóm lại, trừ trung bình của phần thưởng đổi bài toán, còn chuẩn hóa lợi thế chỉ đổi mục tiêu cắt và thang của bước.

**Kiểm tra lại.** Ở (b), $J'(\pi_{500})=-0{,}99^{499}=-0{,}0066$ nằm giữa $J'(\pi_{100})$ và $J'(\pi_\infty)$, và $(1-0{,}99\cdot0{,}0066)/0{,}01=99{,}34=J(\pi_{500})$. Lỗi thường gặp: áp kết luận "cộng hằng không đổi chính sách tối ưu" của bài toán liên tục (Bài tập 3.15 của sách, giá trị tăng $c/(1-\gamma)$) cho CartPole; viết $G'_0=-\gamma^T$ thay cho $-\gamma^{T-1}$, khi đó đẳng thức ở (b) sai một thừa số $\gamma$; coi phép chia cho độ lệch chuẩn chạy như chia cho một hằng; cho rằng $\mathcal L^{\mathrm{CLIP}}$ thuần nhất với mọi $k$, trong khi với $k<0$ dấu của lợi thế đổi và hai nhánh $\min$, $\max$ đổi chỗ.
:::

## Tài liệu tham khảo

- Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018. §3.5, Bài tập 3.15, 3.16, tr. 61 (Bài tập 10.14, 10.21); §5.5, ký hiệu $\rho_{t:T-1}$, và §5.9, (5.12)–(5.14), Bài tập 5.13, tr. 114–115 (Bài tập 10.17); §6.1, (6.6), Bài tập 6.1, tr. 121 (Bài tập 10.15); §7.4, (7.13), (7.14), Bài tập 7.6, tr. 150–151 (Bài tập 10.16); §12.1, Bài tập 12.2, tr. 290 (Bài tập 10.13); §12.9, (12.22)–(12.24), Bài tập 12.8, tr. 309 (Bài tập 10.18); Ví dụ 13.1, tr. 323, và §13.4, hộp giả mã REINFORCE có đường cơ sở, Hình 13.2, tr. 330–331 (Bài tập 10.20); §13.7, (13.19), (13.20), Bài tập 13.4, tr. 335–336 (Bài tập 10.19).
- Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. "Proximal Policy Optimization Algorithms." arXiv 1707.06347, 2017. Bảng 3, 5, theo bảng siêu tham số ở Mục 6.4 của ghi chú (Bài tập 10.13).
- Ghi chú bài giảng Bài 10, Mục 1–6 và Tình huống 10.1, cho mọi số hiệu Định nghĩa, Mệnh đề, Bổ đề, Thuật toán, Ví dụ và Bài tập 10.1–10.12 dẫn trong tệp; Bài tập 09.19 của tệp bài tập Bài 09 và Định nghĩa 09.12 của ghi chú Bài 09.
