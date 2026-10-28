# Bài tập Bài 09 — Double DQN và gradient chính sách

Bộ bài tập gồm mười bài, phủ năm mạch nội dung 2–6 của bài học, ở ba mức: nhận biết (09.11, 09.12); tính toán hoặc chứng minh (09.13–09.17); vận dụng vào bài toán Học tăng cường (09.18–09.20). Mười bài 09.1–09.10 thuộc mục "Bài tập củng cố" của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html) Bài 09, có gợi ý và lời giải tại đó, nên không chép lại; bảng dưới ghi chúng ở dạng "ghi chú: 09.k". Tệp này là bộ bài tập chính thức của bài, xây dựng từ các bài tập và ví dụ của Sutton và Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2: Bài tập 6.13, 13.1, 13.2, 13.3, 13.5, Ví dụ 6.7 (Hình 6.5) và Ví dụ 13.1 (Hình 13.1). Mười bài 09.11–09.20 chỉ có trong tệp này, tiếp nối bộ đếm Bài tập của ghi chú; không bài nào trùng một trang bài tập của trang chiếu. Bảng dưới dẫn thêm tới các trang bài tập trên trang chiếu, vốn trùng các bài củng cố 09.3, 09.5, 09.8 và 09.10.

Đề bài được phát biểu lại theo ký hiệu của ghi chú Bài 09, với dữ kiện tự đủ và câu hỏi bổ sung có số; mọi số trong lời giải đã được tính lại.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/1/1) | — |
| 2. Độ chệch của phép cực đại | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/2/1) | 09.11, 09.18; [ghi chú: 09.1, 09.2 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html) |
| 3. Tách chọn và đánh giá | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/3/1) | 09.11, 09.13, 09.18; [ghi chú: 09.3 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: mục tiêu DQN và Double DQN](lecture-09-double-dqn-va-gradient-chinh-sach.html#/3/7), lời giải trên cùng trang |
| 4. Chính sách tham số hóa | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/4/1) | 09.12, 09.14, 09.16; [ghi chú: 09.4 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html) |
| 5. Hàm mục tiêu và hàm điểm | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/5/1) | 09.15, 09.16, 09.20; [ghi chú: 09.5, 09.6, 09.7 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: hàm điểm softmax và Gaussian](lecture-09-double-dqn-va-gradient-chinh-sach.html#/5/12), trùng 09.5 |
| 6. Gradient chính sách và REINFORCE | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/6/1) | 09.16, 09.17, 09.19, 09.20; [ghi chú: 09.8, 09.9 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: cập nhật REINFORCE](lecture-09-double-dqn-va-gradient-chinh-sach.html#/6/13) và [trang lời giải](lecture-09-double-dqn-va-gradient-chinh-sach.html#/6/14), trùng 09.8 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-09-double-dqn-va-gradient-chinh-sach.html#/7/1) | [ghi chú: 09.10 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-09/lecture-note.md&deck=lecture-09-double-dqn-va-gradient-chinh-sach.html); trang [Bài tập: tổng hợp trên bài toán một bước](lecture-09-double-dqn-va-gradient-chinh-sach.html#/7/6) và [trang lời giải](lecture-09-double-dqn-va-gradient-chinh-sach.html#/7/7), trùng 09.10 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 09. Thời gian rời rạc $t=0,1,\dots$; phần thưởng $R_{t+1}$ nhận sau hành động $A_t$ tại trạng thái $S_t$; lượt kết thúc tại bước $T$; lợi tức từ bước $t$ là $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$ với hệ số chiết khấu $\gamma$. Hàm giá trị hành động của chính sách $\pi$ là $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$, của chính sách tối ưu là $q_*$. Chính sách tham số hóa $\pi_\theta$, $\theta\in\mathbb R^d$ (Định nghĩa 09.10); hàm mục tiêu $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ (Định nghĩa 09.14); hàm điểm (score function) $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$ (Định nghĩa 09.15), viết tắt $\psi_t=\psi_\theta(S_t,A_t)$; $\log$ là logarit tự nhiên. Chính sách softmax với đặc trưng $\phi(s,a)\in\mathbb R^d$ (Định nghĩa 09.11) có hàm điểm $\psi_\theta(s,a)=\phi(s,a)-\sum_b\pi_\theta(b\mid s)\phi(s,b)$ (Mệnh đề 09.16). Theo Định lý 09.23, dưới các giả thiết (G1)–(G4) của ghi chú, $\nabla_\theta J=\mathbb E_{\pi_\theta}\bigl[\sum_{t=0}^{T-1}\gamma^tG_t\psi_t\bigr]$; REINFORCE (Thuật toán 09.25) cập nhật một lần mỗi lượt, $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\sum_t\gamma^tG_t\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$, với bước $\alpha>0$.

Chính sách $\epsilon$-tham lam theo một bảng $Q$ chọn đều một hành động với xác suất $\epsilon$, ngược lại chọn hành động có $Q$ lớn nhất, phá hòa chia đều. Với $\lvert\mathcal A\rvert$ hành động và một hành động tham lam duy nhất, hành động tham lam có xác suất $1-\epsilon+\epsilon/\lvert\mathcal A\rvert$, mỗi hành động khác có xác suất $\epsilon/\lvert\mathcal A\rvert$.

Hai môi trường của Sutton và Barto (2018) dùng ở nhiều bài; bài nào dùng chúng đều nêu lại dữ kiện trong khối đề bài.

- **MDP độ chệch cực đại** (Sutton và Barto, 2018, Ví dụ 6.7). Hai trạng thái không kết thúc $s_{\mathrm A}$, $s_{\mathrm B}$; lượt luôn bắt đầu ở $s_{\mathrm A}$. Tại $s_{\mathrm A}$ có hai hành động: "phải" ($a_{\mathrm R}$) kết thúc lượt ngay với phần thưởng $0$; "trái" ($a_{\mathrm L}$) chuyển sang $s_{\mathrm B}$ với phần thưởng $0$. Tại $s_{\mathrm B}$ có $m$ hành động $b_1,\dots,b_m$; mọi hành động kết thúc lượt với phần thưởng lấy từ phân phối chuẩn $\mathcal N(-0{,}1;\,1)$, trung bình $-0{,}1$, phương sai $1$, độc lập giữa các lần. Không chiết khấu, $\gamma=1$.
- **Hành lang ngắn đảo hành động** (Sutton và Barto, 2018, Ví dụ 13.1). Bốn ô trên một hàng: $s_1$ (ô xuất phát), $s_2$, $s_3$ và ô đích $s_4$, nơi lượt kết thúc. Mỗi bước nhận phần thưởng $-1$; $\gamma=1$. Hai hành động: hành động 1 là "sang phải", hành động 2 là "sang trái". Ở $s_1$ và $s_3$ hành động có tác dụng thông thường; sang trái tại $s_1$ thì đứng yên; sang phải tại $s_3$ thì tới $s_4$. Ở $s_2$ hai hành động bị đảo: hành động 1 đưa về $s_1$, hành động 2 đưa tới $s_3$. Mọi ô có cùng đặc trưng: $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ với mọi $s$, nên chính sách softmax chọn hành động 1 với cùng xác suất $p=\pi_\theta(1\mid s)$ ở cả ba ô.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

Hình đọc từ trái sang phải; trong mỗi ô, dòng "1 →" và "2 →" ghi ô kế tiếp của hành động 1 và 2. Ô $s_2$ có viền nét đứt và nhãn "đảo hành động": ở đó hành động 1 đưa về bên trái.

**Quy ước chiết khấu.** Ghi chú bài giảng dùng $\gamma<1$ và phát biểu Định lý 09.23, Hệ quả 09.26 dưới (G1)–(G4), trong đó (G3) đòi phần thưởng bị chặn và độ dài lượt $T\le T_{\max}$. Theo nguồn, hai môi trường trên dùng $\gamma=1$. MDP độ chệch cực đại có $T\le2$ và chỉ dùng cho Q-learning, nên không cần thêm điều kiện. Trên hành lang ngắn, độ dài lượt không bị chặn, nhưng khi $0<p<1$ thì từ mọi ô có một dãy tối đa ba bước tới đích với xác suất ít nhất $c=p^2(1-p)>0$ (từ $s_1$: hành động 1, 2, 1). Do đó $\Pr(T>3n)\le(1-c)^n$: $T$ hữu hạn hầu chắc chắn, có đuôi hình học và mọi mô men hữu hạn, nên $J=-\mathbb E[T]$ hữu hạn. Kết luận của Định lý 09.23 và Hệ quả 09.26 vẫn đúng ở đây, chứng minh theo đường của Bài tập 09.17 với chuỗi thay cho tổng hữu hạn. Tập trạng thái hữu hạn và lượt kết thúc hầu chắc chắn, nên giá trị $v_\pi$ là nghiệm duy nhất của một hệ phương trình tuyến tính hữu hạn với hệ số khả vi theo $\theta$, do đó khả vi theo $\theta$; phần dư khi lặp phương trình Bellman của $\nabla_\theta v_\pi$ dần về $0$ theo cấp số nhân. Với phần thưởng $-1$ mỗi bước, $\lvert G_t\rvert\le T$, và hàm điểm softmax ở đây có chuẩn không quá $\sqrt2$; nên $\mathbb E\bigl[\sum_t\lvert G_t\rvert\,\lVert\psi_t\rVert\bigr]\le\sqrt2\,\mathbb E[T^2]<\infty$, đủ để đổi tổng theo $t$ với kỳ vọng. Khi $p\in\{0,1\}$, lượt không kết thúc (Bài tập 09.12).

Mọi bộ số không ghi nguồn là số liệu sư phạm tự xây dựng. Kết quả mô phỏng nêu trong lời giải là kết quả một lần chạy của người soạn, ghi rõ cấu hình và hạt giống ngẫu nhiên (seed); chúng thay đổi theo hạt giống, nên chỉ dùng để đối chiếu định tính. Số thập phân viết với dấu phẩy; vector viết $(x_1;\,x_2)$. Số hiệu "Định nghĩa 09.k", "Mệnh đề 09.k", "Định lý 09.k", "Thuật toán 09.k", "Ví dụ 09.k" chỉ khối của ghi chú bài giảng Bài 09.

## Mức nhận biết

### Bài tập 09.11. MDP độ chệch cực đại

**Mức độ:** nhận biết. Mục tiêu học tập: nhận ra độ chệch của phép cực đại trong mục tiêu Q-learning trên một MDP cụ thể và cách mục tiêu kép tách chọn với đánh giá.

**Nguồn:** Sutton và Barto (2018), §6.7, Ví dụ 6.7; ghi chú bài giảng Bài 09, Mục 2 (Định nghĩa 09.1, Mệnh đề 09.2) và Mục 3 (Thuật toán 09.7); bộ số ở (b), (c) tự xây dựng.

::: exercise Bài tập 09.11 (MDP độ chệch cực đại)
Xét MDP độ chệch cực đại (theo Sutton và Barto, 2018, Ví dụ 6.7). Hai trạng thái không kết thúc $s_{\mathrm A}$, $s_{\mathrm B}$; lượt bắt đầu ở $s_{\mathrm A}$. Tại $s_{\mathrm A}$: "phải" ($a_{\mathrm R}$) kết thúc lượt với phần thưởng $0$; "trái" ($a_{\mathrm L}$) chuyển sang $s_{\mathrm B}$ với phần thưởng $0$. Tại $s_{\mathrm B}$ có $m=4$ hành động $b_1,\dots,b_4$, mỗi hành động kết thúc lượt với phần thưởng $\mathcal N(-0{,}1;\,1)$. $\gamma=1$.

- (a) Tính $q_*(s_{\mathrm B},b_j)$, $q_*(s_{\mathrm A},a_{\mathrm L})$, $q_*(s_{\mathrm A},a_{\mathrm R})$ và chính sách tối ưu tại $s_{\mathrm A}$. Một tác tử $\epsilon$-tham lam với $\epsilon=0{,}1$ chọn "trái" tại $s_{\mathrm A}$ với xác suất nhỏ nhất bao nhiêu?
- (b) Sau một số lượt, bảng Q-learning có $Q(s_{\mathrm B},\cdot)=(0{,}35;\,-0{,}62;\,-0{,}08;\,-0{,}41)$ và $Q(s_{\mathrm A},a_{\mathrm R})=0$. Tính mục tiêu Q-learning của cặp $(s_{\mathrm A},a_{\mathrm L})$. Mục tiêu này lớn hơn hay nhỏ hơn $q_*(s_{\mathrm A},a_{\mathrm L})$? Nếu $Q(s_{\mathrm A},a_{\mathrm L})$ tiến tới mục tiêu này, hành động tham lam tại $s_{\mathrm A}$ là gì?
- (c) Double Q-learning giữ hai bảng; tại $s_{\mathrm B}$, $Q_1(s_{\mathrm B},\cdot)=(0{,}35;\,-0{,}62;\,-0{,}08;\,-0{,}41)$ và $Q_2(s_{\mathrm B},\cdot)=(-0{,}30;\,0{,}12;\,-0{,}25;\,0{,}05)$. Tính mục tiêu của $(s_{\mathrm A},a_{\mathrm L})$ khi cập nhật $Q_1$ và khi cập nhật $Q_2$. Nêu mệnh đề của ghi chú cho biết khi nào mục tiêu kép không chệch lên, và giả thiết nào của mệnh đề chỉ gần thỏa ở đây.
:::

::: hint Gợi ý Bài tập 09.11
Với $\gamma=1$ và phần thưởng $0$ khi sang $s_{\mathrm B}$, $q_*(s_{\mathrm A},a_{\mathrm L})=\max_jq_*(s_{\mathrm B},b_j)$. Mục tiêu Q-learning là $R+\gamma\max_bQ(S',b)$; mục tiêu khi cập nhật $Q_1$ chọn bằng $Q_1$ và đánh giá bằng $Q_2$ (Thuật toán 09.7).
:::

::: solution Lời giải Bài tập 09.11
**Câu (a).** Mọi hành động tại $s_{\mathrm B}$ kết thúc lượt với phần thưởng trung bình $-0{,}1$, nên $q_*(s_{\mathrm B},b_j)=-0{,}1$ với mọi $j$. Từ đó $q_*(s_{\mathrm A},a_{\mathrm L})=0+1\cdot(-0{,}1)=-0{,}1$ và $q_*(s_{\mathrm A},a_{\mathrm R})=0$; chính sách tối ưu chọn "phải". Tác tử $\epsilon$-tham lam với "phải" là hành động tham lam vẫn chọn "trái" với xác suất $\epsilon/2=0{,}05$; đó là mức nhỏ nhất, cũng là mức $5\%$ mà nguồn ghi là tối ưu với $\epsilon=0{,}1$.

**Câu (b).** Mục tiêu: $0+1\cdot\max_jQ(s_{\mathrm B},b_j)=0{,}35$, lớn hơn $q_*(s_{\mathrm A},a_{\mathrm L})=-0{,}1$ một lượng $0{,}45$. Khi $Q(s_{\mathrm A},a_{\mathrm L})$ tiến tới $0{,}35>0=Q(s_{\mathrm A},a_{\mathrm R})$, hành động tham lam tại $s_{\mathrm A}$ là "trái", hành động sai. Ước lượng $0{,}35$ của $b_1$ cao vì nhiễu; phép cực đại chọn đúng ước lượng bị nhiễu đẩy lên (Mệnh đề 09.2: kỳ vọng của cực đại không nhỏ hơn cực đại của các kỳ vọng).

**Câu (c).** Cập nhật $Q_1$: chọn $b^*=\arg\max_jQ_1(s_{\mathrm B},b_j)=b_1$, đánh giá bằng $Q_2(s_{\mathrm B},b_1)=-0{,}30$; mục tiêu $-0{,}30$. Cập nhật $Q_2$: chọn $b^*=\arg\max_jQ_2(s_{\mathrm B},b_j)=b_2$, đánh giá bằng $Q_1(s_{\mathrm B},b_2)=-0{,}62$; mục tiêu $-0{,}62$. Cả hai mục tiêu âm, nên "trái" không được ưu tiên. Theo Mệnh đề 09.4, khi bản đánh giá không chệch và độc lập với bản chọn, giá trị báo cáo không chệch lên; hai bảng học từ hai nửa dữ liệu khác nhau, chỉ gần thỏa giả thiết độc lập.

**Kiểm tra lại.** Ở (b), mục tiêu bằng giá trị lớn nhất của hàng $Q(s_{\mathrm B},\cdot)$, không phải trung bình của hàng ($-0{,}19$). Nhầm lẫn thường gặp: ở (c) dùng cùng một bảng để chọn và đánh giá, được lại $0{,}35$ hoặc $0{,}12$; hoặc đánh giá bằng $Q_2$ tại hành động $\arg\max Q_2$, tức Q-learning trên bảng $Q_2$.
:::

### Bài tập 09.12. Hành lang ngắn và chính sách tất định

**Mức độ:** nhận biết. Mục tiêu học tập: nhận ra giới hạn của chính sách tham lam theo $Q$ khi đặc trưng gộp các trạng thái, và vai trò của chính sách ngẫu nhiên.

**Nguồn:** Sutton và Barto (2018), §13.1, Ví dụ 13.1; ghi chú bài giảng Bài 09, Mục 4 (Ví dụ 09.8, 09.9, Định nghĩa 09.11).

::: exercise Bài tập 09.12 (Hành lang ngắn và chính sách tất định)
Xét hành lang ngắn đảo hành động (theo Sutton và Barto, 2018, Ví dụ 13.1). Bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 là "sang phải", hành động 2 là "sang trái". Ở $s_1$, $s_3$ hành động có tác dụng thông thường (sang trái tại $s_1$ thì đứng yên); ở $s_2$ hai hành động bị đảo: hành động 1 đưa về $s_1$, hành động 2 đưa tới $s_3$. Đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ với mọi $s$.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

- (a) Chứng tỏ rằng mọi chính sách softmax với các đặc trưng này chọn hành động 1 với cùng một xác suất $p$ ở cả ba ô, và viết $p$ theo $\theta$.
- (b) Mô tả lượt sinh bởi chính sách tất định $p=1$ và bởi $p=0$. Lượt có kết thúc không? Giá trị $J$ của mỗi chính sách là bao nhiêu?
- (c) Một phương pháp giá trị hành động với $Q(s,a)=\phi(s,a)^\top w$ và hành vi $\epsilon$-tham lam, $\epsilon=0{,}1$, đạt được những giá trị $p$ nào? Chính sách softmax đạt được những giá trị $p$ nào?
:::

::: hint Gợi ý Bài tập 09.12
Viết $\pi_\theta(1\mid s)$ theo Định nghĩa 09.11: tử số và mẫu số không chứa $s$. Ở (b), lần theo ba bước đầu của lượt từ $s_1$.
:::

::: solution Lời giải Bài tập 09.12
**Câu (a).** Theo Định nghĩa 09.11, $\pi_\theta(1\mid s)=\dfrac{e^{\theta_1}}{e^{\theta_1}+e^{\theta_2}}=\dfrac1{1+e^{-(\theta_1-\theta_2)}}$. Biểu thức không chứa $s$ vì $\phi(s,a)$ không phụ thuộc $s$; do đó $p=\pi_\theta(1\mid s)$ như nhau ở $s_1$, $s_2$, $s_3$.

**Câu (b).** Với $p=1$: $s_1\to s_2$ (sang phải), rồi tại $s_2$ hành động 1 đưa về $s_1$, rồi lại $s_2$; lượt lặp $s_1,s_2,s_1,\dots$ mãi, không tới $s_4$. Với $p=0$: tại $s_1$ sang trái thì đứng yên; lượt ở $s_1$ mãi. Lượt không kết thúc, nên giả thiết lượt kết thúc hầu chắc chắn của Định nghĩa 09.14 không thỏa và $J$ không xác định theo nghĩa thông thường. Tổng của $n$ bước đầu là $-n\to-\infty$; theo nghĩa giới hạn đó, viết $J=-\infty$ cho cả hai chính sách.

**Câu (c).** Với $Q(s,a)=\phi(s,a)^\top w$, $Q(s,1)=w_1$ và $Q(s,2)=w_2$ ở mọi ô, nên hành động tham lam như nhau ở mọi ô. Khi $w_1>w_2$, $p=1-\epsilon/2=0{,}95$; khi $w_1<w_2$, $p=\epsilon/2=0{,}05$; khi $w_1=w_2$, phá hòa đều cho $p=0{,}5$, nhưng điểm hòa không bền khi $w$ được cập nhật. Chính sách softmax đạt mọi $p\in(0,1)$, vì $\theta_1-\theta_2$ chạy trên $\mathbb R$. Bài tập 09.14 tìm $p$ tốt nhất.

**Kiểm tra lại.** Nhầm lẫn thường gặp: cho rằng chính sách tất định luôn đủ vì MDP có chính sách tối ưu tất định. Kết quả đó cần chính sách được phép phụ thuộc trạng thái đầy đủ; ở đây đặc trưng gộp ba ô, giống ô xám của Ví dụ 09.8.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 09.13. Double Expected Sarsa

**Mức độ:** tính toán. Mục tiêu học tập: áp dụng ý tưởng tách chọn và đánh giá cho một thuật toán điều khiển khác Q-learning, viết quy tắc cập nhật và tính một bước.

**Nguồn:** Sutton và Barto (2018), §6.7, Bài tập 6.13; Sutton và Barto (2018), §6.6 (Expected Sarsa); ghi chú bài giảng Bài 09, Mục 3 (Mệnh đề 09.4, Thuật toán 09.7); bộ số ở (c) tự xây dựng.

::: exercise Bài tập 09.13 (Double Expected Sarsa)
(Theo Sutton và Barto, 2018, Bài tập 6.13.) Expected Sarsa (còn gọi là Sarsa kỳ vọng; Sutton và Barto, 2018, §6.6) với chính sách mục tiêu $\pi$ cập nhật $Q(S,A)\leftarrow Q(S,A)+\alpha\bigl[R+\gamma(1-Z)\sum_a\pi(a\mid S')Q(S',a)-Q(S,A)\bigr]$ trên mẫu chuyển $(S,A,R,S',Z)$, với $Z=1$ khi $S'$ là trạng thái kết thúc. Double Q-learning (Thuật toán 09.7) giữ hai bảng $Q_1$, $Q_2$; mỗi bước tung đồng xu để chọn bảng được cập nhật; bảng được cập nhật chọn hành động, bảng kia đánh giá.

- (a) Viết hai phương trình cập nhật của Double Expected Sarsa với chính sách mục tiêu $\epsilon$-tham lam: một khi cập nhật $Q_1$, một khi cập nhật $Q_2$. Nêu rõ chính sách mục tiêu được xây từ bảng nào và kỳ vọng lấy theo giá trị của bảng nào.
- (b) Chứng tỏ khi $\epsilon=0$, hai phương trình ở (a) trở thành Double Q-learning (khi hành động tham lam duy nhất).
- (c) Tập hành động tại $S'$ có ba phần tử; $S'$ không kết thúc. $Q_1(S',\cdot)=(2;\,5;\,4)$, $Q_2(S',\cdot)=(3;\,1;\,6)$, $Q_1(S,A)=2$, $Q_2(S,A)=3$, $R=1$, $\gamma=0{,}9$, $\alpha=0{,}1$, $\epsilon=0{,}3$. Tính mục tiêu, sai số và giá trị mới trong hai trường hợp đồng xu. So mục tiêu khi cập nhật $Q_1$ với mục tiêu Expected Sarsa một bảng dùng $Q_1$ cho cả chính sách lẫn giá trị.
:::

::: hint Gợi ý Bài tập 09.13
Trong Double Q-learning, $\arg\max_aQ_1(S',a)$ là bước chọn và $Q_2(S',\cdot)$ là bước đánh giá. Với Expected Sarsa, bước chọn là chính sách $\epsilon$-tham lam, nên chính sách được xây từ bảng được cập nhật, còn giá trị lấy từ bảng kia. Với $\epsilon=0{,}3$ và ba hành động, hành động tham lam có xác suất $0{,}8$, mỗi hành động khác $0{,}1$.
:::

::: solution Lời giải Bài tập 09.13
**Câu (a).** Gọi $\pi_1$, $\pi_2$ là các chính sách $\epsilon$-tham lam theo $Q_1$, $Q_2$. Khi đồng xu chọn $Q_1$:
$$
\begin{aligned}
e_1&=\sum_a\pi_1(a\mid S')\,Q_2(S',a),\\
y_1&=R+\gamma(1-Z)\,e_1,\\
Q_1(S,A)&\leftarrow Q_1(S,A)\\
&\quad+\alpha\bigl[y_1-Q_1(S,A)\bigr].
\end{aligned}
$$
Khi đồng xu chọn $Q_2$, đổi vai trò hai bảng:
$$
\begin{aligned}
e_2&=\sum_a\pi_2(a\mid S')\,Q_1(S',a),\\
y_2&=R+\gamma(1-Z)\,e_2,\\
Q_2(S,A)&\leftarrow Q_2(S,A)\\
&\quad+\alpha\bigl[y_2-Q_2(S,A)\bigr].
\end{aligned}
$$
Chính sách mục tiêu xây từ bảng được cập nhật (bước chọn); kỳ vọng lấy theo giá trị của bảng kia (bước đánh giá). Hành vi có thể là $\epsilon$-tham lam theo $Q_1+Q_2$, như Double Q-learning; hành vi không vào mục tiêu.

**Câu (b).** Với $\epsilon=0$ và hành động tham lam $a^*_1=\arg\max_aQ_1(S',a)$ duy nhất, $\pi_1(a\mid S')=\mathbf 1\{a=a^*_1\}$, nên $\sum_a\pi_1(a\mid S')Q_2(S',a)=Q_2(S',a^*_1)$: đúng mục tiêu của Double Q-learning khi cập nhật $Q_1$. Trường hợp cập nhật $Q_2$ tương tự.

**Câu (c).** Cập nhật $Q_1$: hành động tham lam theo $Q_1(S',\cdot)=(2;\,5;\,4)$ là hành động 2, nên $\pi_1(\cdot\mid S')=(0{,}1;\,0{,}8;\,0{,}1)$. Kỳ vọng theo $Q_2$: $0{,}1\cdot3+0{,}8\cdot1+0{,}1\cdot6=1{,}7$. Mục tiêu $1+0{,}9\cdot1{,}7=2{,}53$; sai số $2{,}53-2=0{,}53$; $Q_1(S,A)\leftarrow2+0{,}1\cdot0{,}53=2{,}053$.

Cập nhật $Q_2$: hành động tham lam theo $Q_2(S',\cdot)=(3;\,1;\,6)$ là hành động 3, nên $\pi_2(\cdot\mid S')=(0{,}1;\,0{,}1;\,0{,}8)$. Kỳ vọng theo $Q_1$: $0{,}1\cdot2+0{,}1\cdot5+0{,}8\cdot4=3{,}9$. Mục tiêu $1+0{,}9\cdot3{,}9=4{,}51$; sai số $4{,}51-3=1{,}51$; $Q_2(S,A)\leftarrow3+0{,}1\cdot1{,}51=3{,}151$.

So sánh: Expected Sarsa một bảng với $Q_1$ cho mục tiêu $1+0{,}9\,(0{,}1\cdot2+0{,}8\cdot5+0{,}1\cdot4)=1+0{,}9\cdot4{,}6=5{,}14$, cao hơn mục tiêu kép $2{,}53$ một lượng $2{,}61$. Bảng $Q_1$ xếp hành động 2 cao nhất, còn $Q_2$ đánh giá nó thấp nhất; mục tiêu một bảng dùng chính ước lượng đã thắng phép chọn để đánh giá.

**Kiểm tra lại.** Với $\epsilon=0$, mục tiêu khi cập nhật $Q_1$ là $1+0{,}9\cdot Q_2(S',2)=1{,}9$, khớp câu (b). Hai lỗi thường gặp: xây $\pi_1$ từ $Q_2$, được $1+0{,}9\,(0{,}1\cdot3+0{,}1\cdot1+0{,}8\cdot6)=5{,}68$, tức Expected Sarsa một bảng trên $Q_2$; dùng chính sách theo $Q_1+Q_2$ trong mục tiêu, khi đó bước chọn phụ thuộc cả bảng đánh giá và lập luận của Mệnh đề 09.4 không áp dụng.
:::

### Bài tập 09.14. Xác suất tối ưu trên hành lang ngắn

**Mức độ:** tính toán. Mục tiêu học tập: viết phương trình Bellman cho một chính sách ngẫu nhiên, giải dạng đóng $J$ theo tham số và cực đại hóa.

**Nguồn:** Sutton và Barto (2018), §13.1, Ví dụ 13.1 và Bài tập 13.1; ghi chú bài giảng Bài 09, Mục 4 (Ví dụ 09.9) và Mục 5 (Định nghĩa 09.14).

::: exercise Bài tập 09.14 (Xác suất tối ưu trên hành lang ngắn)
(Theo Sutton và Barto, 2018, Bài tập 13.1.) Hành lang ngắn đảo hành động: bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 "sang phải", hành động 2 "sang trái"; ở $s_1$, $s_3$ tác dụng thông thường (sang trái tại $s_1$ thì đứng yên, sang phải tại $s_3$ thì tới $s_4$); ở $s_2$ hai hành động bị đảo (hành động 1 về $s_1$, hành động 2 tới $s_3$). Chính sách chọn hành động 1 với cùng xác suất $p\in(0,1)$ ở mọi ô (Bài tập 09.12). Viết $v_i$ cho giá trị của ô $s_i$ dưới chính sách đó, $v_4=0$.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

- (a) Viết ba phương trình Bellman cho $v_1$, $v_2$, $v_3$.
- (b) Giải hệ để được $J(p)=v_1$ ở dạng đóng; kiểm tại $p=\tfrac12$.
- (c) Tìm $p^*$ cực đại $J$ và giá trị $J(p^*)$ ở dạng đóng, rồi làm tròn hai chữ số thập phân.
- (d) Tính $J(0{,}95)$ và $J(0{,}05)$, giá trị của hai chính sách $\epsilon$-tham lam ở Bài tập 09.12(c), và so với $J(p^*)$.
:::

::: hint Gợi ý Bài tập 09.14
Mỗi phương trình có dạng: giá trị bằng $-1$ cộng trung bình theo $p$ của giá trị ô kế tiếp. Từ phương trình của $v_1$, biểu diễn $v_1$ theo $v_2$; từ phương trình của $v_3$, biểu diễn $v_3$ theo $v_2$; thế cả hai vào phương trình của $v_2$. Khi cực đại, viết $J=-c\,f(p)$ với hằng $c>0$ và $f>0$, rồi lấy đạo hàm của $\log f$.
:::

::: solution Lời giải Bài tập 09.14
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
&\quad+(1-p)\bigl(-1+(1-p)v_2\bigr)\\
&=-1+p\,v_2-1-(1-p)\\
&\quad+(1-p)^2v_2 ,
\end{aligned}
$$
nên $v_2\bigl[1-p-(1-p)^2\bigr]=v_2\,p(1-p)=-(3-p)$ và $v_2=-\dfrac{3-p}{p(1-p)}$. Từ đó
$$
\begin{aligned}
J(p)=v_1&=-\frac{3-p}{p(1-p)}-\frac1p\\
&=-\frac{2(2-p)}{p(1-p)},
\end{aligned}
$$
và $v_3=-1+(1-p)v_2=-\dfrac3p$.
Tại $p=\tfrac12$: $J=-\dfrac{2\cdot1{,}5}{0{,}25}=-12$, $v_2=-10$, $v_3=-6$. Kiểm phương trình thứ hai: $-1+\tfrac12(-12)+\tfrac12(-6)=-10$.

**Câu (c).** Cực đại $J$ tương đương cực tiểu $f(p)=\dfrac{2-p}{p(1-p)}>0$. Đạo hàm của $\log f$:
$$
-\frac1{2-p}-\frac1p+\frac1{1-p}=0 .
$$
Nhân hai vế với $p(1-p)(2-p)>0$:
$$
\begin{aligned}
0&=-p(1-p)-(2-p)(1-p)\\
&\quad+p(2-p)\\
&=-p^2+4p-2 ,
\end{aligned}
$$
tức $p^2-4p+2=0$. Nghiệm trong $(0,1)$ là $p^*=2-\sqrt2\approx0{,}59$ (nghiệm kia $2+\sqrt2>1$). Vì $J\to-\infty$ khi $p\to0$ và khi $p\to1$, và $p^*$ là điểm dừng duy nhất trong $(0,1)$, $p^*$ là điểm cực đại. Với $p^*(1-p^*)=(2-\sqrt2)(\sqrt2-1)=3\sqrt2-4$ và $2-p^*=\sqrt2$:
$$
\begin{aligned}
J(p^*)&=-\frac{2\sqrt2}{3\sqrt2-4}\\
&=-\frac{2\sqrt2\,(3\sqrt2+4)}{18-16}\\
&=-(6+4\sqrt2)\approx-11{,}66 .
\end{aligned}
$$

**Câu (d).** $J(0{,}95)=-\dfrac{2\cdot1{,}05}{0{,}95\cdot0{,}05}\approx-44{,}21$; $J(0{,}05)=-\dfrac{2\cdot1{,}95}{0{,}05\cdot0{,}95}\approx-82{,}11$. Hai chính sách $\epsilon$-tham lam cần trung bình khoảng $44$ và $82$ bước để tới đích, so với khoảng $11{,}66$ bước của $p^*$. Chính sách đều $p=\tfrac12$ chỉ kém $p^*$ khoảng $0{,}34$ bước.

**Kiểm tra lại.** Các giá trị $p^*\approx0{,}59$, $J(p^*)\approx-11{,}6$, $J(0{,}95)\approx-44$ và $J(0{,}05)\approx-82$ khớp các số mà nguồn nêu ở Ví dụ 13.1 ($0{,}59$; $-11{,}6$; $-44$; $-82$). Lỗi thường gặp: quên rằng sang trái tại $s_1$ vẫn tốn một bước, viết $v_1=-1+p\,v_2$, được $J$ sai; hoặc đảo hai hành động ở $s_1$ thay vì $s_2$.
:::

### Bài tập 09.15. Hàm điểm softmax với mức ưu tiên tổng quát

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập: dẫn hàm điểm của chính sách softmax khi mức ưu tiên là một hàm khả vi bất kỳ của $\theta$, và tính trên ba hành động.

**Nguồn:** Sutton và Barto (2018), §13.1 và Bài tập 13.3, mở rộng sang mức ưu tiên phi tuyến; ghi chú bài giảng Bài 09, Mục 5 (Mệnh đề 09.16, 09.17); bộ số ở (c), (d) tự xây dựng.

::: exercise Bài tập 09.15 (Hàm điểm softmax với mức ưu tiên tổng quát)
(Theo Sutton và Barto, 2018, Bài tập 13.3, mở rộng.) Tập hành động $\mathcal A$ hữu hạn. Với mỗi $s$, $a$, mức ưu tiên $h(s,a,\theta)$ là một hàm khả vi của $\theta\in\mathbb R^d$, chẳng hạn đầu ra của một mạng nơ-ron. Chính sách softmax theo mức ưu tiên là
$$
\pi_\theta(a\mid s)=\frac{\exp h(s,a,\theta)}{\sum_{b\in\mathcal A}\exp h(s,b,\theta)} .
$$

- (a) Chứng minh $\psi_\theta(s,a)=\nabla_\theta h(s,a,\theta)-\sum_b\pi_\theta(b\mid s)\,\nabla_\theta h(s,b,\theta)$.
- (b) Suy ra Mệnh đề 09.16 khi $h(s,a,\theta)=\phi(s,a)^\top\theta$.
- (c) Ba hành động, $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, $\phi(s,3)=(1;\,1)$, mức ưu tiên tuyến tính, $\theta=(\log2;\,0)$. Tính $\pi_\theta(\cdot\mid s)$, ba hàm điểm, và kiểm $\sum_a\pi_\theta(a\mid s)\psi_\theta(s,a)=0$. Sau bước $\theta\leftarrow\theta+0{,}5\,\psi_\theta(s,2)$, tính lại $\pi_\theta(\cdot\mid s)$.
- (d) Hai hành động, $\theta\in\mathbb R$, mức ưu tiên phi tuyến $h(s,1,\theta)=\theta^2$, $h(s,2,\theta)=\theta$. Tính $\pi_\theta(\cdot\mid s)$ và hai hàm điểm tại $\theta=1$; kiểm kỳ vọng của hàm điểm bằng $0$.
:::

::: hint Gợi ý Bài tập 09.15
$\log\pi_\theta(a\mid s)=h(s,a,\theta)-\log\sum_b\exp h(s,b,\theta)$. Đạo hàm của $\log\sum_b e^{h_b}$ theo $\theta$ là $\sum_b\frac{e^{h_b}}{\sum_c e^{h_c}}\nabla_\theta h_b$.
:::

::: solution Lời giải Bài tập 09.15
**Câu (a).** Viết $h_b=h(s,b,\theta)$. Lấy logarit: $\log\pi_\theta(a\mid s)=h_a-\log\sum_be^{h_b}$. Theo quy tắc dây chuyền,
$$
\begin{aligned}
\nabla_\theta\log\sum_be^{h_b}&=\frac{\sum_be^{h_b}\nabla_\theta h_b}{\sum_ce^{h_c}}\\
&=\sum_b\pi_\theta(b\mid s)\,\nabla_\theta h_b ,
\end{aligned}
$$
nên $\psi_\theta(s,a)=\nabla_\theta h_a-\sum_b\pi_\theta(b\mid s)\nabla_\theta h_b$. Hàm điểm là gradient của mức ưu tiên của $a$ trừ trung bình theo $\pi_\theta$ của các gradient mức ưu tiên.

**Câu (b).** Với $h(s,a,\theta)=\phi(s,a)^\top\theta$, $\nabla_\theta h(s,a,\theta)=\phi(s,a)$, nên $\psi_\theta(s,a)=\phi(s,a)-\sum_b\pi_\theta(b\mid s)\phi(s,b)$, đúng Mệnh đề 09.16.

**Câu (c).** Mức ưu tiên $\phi(s,a)^\top\theta$: $\log2$, $0$, $\log2$; lũy thừa: $2$, $1$, $2$; nên $\pi_\theta(\cdot\mid s)=(0{,}4;\,0{,}2;\,0{,}4)$. Đặc trưng trung bình: $0{,}4(1;\,0)+0{,}2(0;\,1)+0{,}4(1;\,1)=(0{,}8;\,0{,}6)$. Hàm điểm:
$$
\begin{aligned}
\psi_\theta(s,1)&=(0{,}2;\,-0{,}6),\\
\psi_\theta(s,2)&=(-0{,}8;\,0{,}4),\\
\psi_\theta(s,3)&=(0{,}2;\,0{,}4).
\end{aligned}
$$
Kỳ vọng: tọa độ đầu $0{,}4\cdot0{,}2-0{,}2\cdot0{,}8+0{,}4\cdot0{,}2=0$; tọa độ sau $-0{,}4\cdot0{,}6+0{,}2\cdot0{,}4+0{,}4\cdot0{,}4=0$.

Bước $0{,}5\,\psi_\theta(s,2)=(-0{,}4;\,0{,}2)$ cho $\theta=(\log2-0{,}4;\,0{,}2)$. Mức ưu tiên mới: $\log2-0{,}4$, $0{,}2$, $\log2-0{,}2$; lũy thừa: $2e^{-0{,}4}\approx1{,}3406$, $e^{0{,}2}\approx1{,}2214$, $2e^{-0{,}2}\approx1{,}6375$; tổng $\approx4{,}1995$. Vậy $\pi_\theta(\cdot\mid s)\approx(0{,}319;\,0{,}291;\,0{,}390)$: xác suất của hành động 2 tăng từ $0{,}2$ lên khoảng $0{,}291$.

**Câu (d).** Tại $\theta=1$: $h(s,1,1)=1$, $h(s,2,1)=1$, nên $\pi_\theta(\cdot\mid s)=(\tfrac12;\,\tfrac12)$. Gradient mức ưu tiên: $\partial_\theta\theta^2=2$, $\partial_\theta\theta=1$; trung bình $\tfrac12\cdot2+\tfrac12\cdot1=1{,}5$. Hàm điểm: $\psi_\theta(s,1)=2-1{,}5=0{,}5$, $\psi_\theta(s,2)=1-1{,}5=-0{,}5$. Kỳ vọng $\tfrac12\cdot0{,}5+\tfrac12\cdot(-0{,}5)=0$. Hai hành động có cùng xác suất nhưng hàm điểm khác $0$: tăng $\theta$ làm mức ưu tiên của hành động 1 tăng nhanh hơn.

**Kiểm tra lại.** Ở (c), hành động 3 có đặc trưng bằng tổng hai đặc trưng kia nhưng hàm điểm $(0{,}2;\,0{,}4)$ không bằng tổng $\psi_\theta(s,1)+\psi_\theta(s,2)=(-0{,}6;\,-0{,}2)$, vì phần trừ đi là đặc trưng trung bình, không cộng theo hành động. Lỗi thường gặp: quên trừ đặc trưng trung bình; dùng trung bình đều $\tfrac13\sum_b\phi(s,b)$ thay cho trung bình theo $\pi_\theta$, được kỳ vọng khác $0$. Ở (d), nhầm lẫn thường gặp: cho rằng hai hành động cùng xác suất thì hàm điểm bằng $0$.
:::

### Bài tập 09.16. Đơn vị Bernoulli–logistic

**Mức độ:** tính toán. Mục tiêu học tập: nhận ra chính sách hai hành động dạng hồi quy logistic là trường hợp riêng của softmax, tính hàm điểm và một bước REINFORCE.

**Nguồn:** Sutton và Barto (2018), §13.3 và Bài tập 13.5; ghi chú bài giảng Bài 09, Mục 4 (Định nghĩa 09.11), Mục 5 (Mệnh đề 09.16, 09.17), Mục 6 (Thuật toán 09.25); bộ số ở (d) tự xây dựng.

::: exercise Bài tập 09.16 (Đơn vị Bernoulli–logistic)
(Theo Sutton và Barto, 2018, Bài tập 13.5.) Một đơn vị Bernoulli–logistic nhận đặc trưng trạng thái $\phi(S_t)\in\mathbb R^d$ và trả hành động $A_t\in\{0,1\}$ với $\Pr(A_t=1)=P_t$, $\Pr(A_t=0)=1-P_t$. Mức ưu tiên của hai hành động là $h(s,0,\theta)$, $h(s,1,\theta)$, với hiệu $h(s,1,\theta)-h(s,0,\theta)=\theta^\top\phi(s)$; chính sách là softmax theo mức ưu tiên.

- (a) Chứng minh $P_t=\pi_\theta(1\mid S_t)=\dfrac{1}{1+\exp\bigl(-\theta^\top\phi(S_t)\bigr)}$, tức hàm logistic $\operatorname{sig}(z)=1/(1+e^{-z})$ (ký hiệu $\operatorname{sig}$ để tránh trùng với độ lệch chuẩn $\sigma$ của chính sách Gaussian) tại $z=\theta^\top\phi(S_t)$.
- (b) Đặt $P=\pi_\theta(1\mid s)$. Tính $\psi_\theta(s,a)$ cho $a=1$ và $a=0$, rồi viết thành một biểu thức theo $a$, $P$ và $\phi(s)$. Kiểm kỳ vọng của hàm điểm theo $A\sim\pi_\theta(\cdot\mid s)$ bằng $0$.
- (c) Viết bước cập nhật REINFORCE của $\theta$ tại bước $t$ của một lượt, với lợi tức $G_t$, bước $\alpha$ và chiết khấu $\gamma$.
- (d) $\phi(s)=(1;\,-2)$, $\theta=(0{,}5;\,0{,}5)$, $\alpha=0{,}1$. Tại bước $t=0$ ở trạng thái $s$, đơn vị trả $A_0=1$ và lợi tức $G_0=2$. Tính $P_0$, $\psi_\theta(s,1)$, $\theta$ sau một bước theo (c), và $\pi_\theta(1\mid s)$ mới.
:::

::: hint Gợi ý Bài tập 09.16
(a) Chia tử và mẫu của softmax cho $\exp h(s,1,\theta)$. (b) $\log P$ và $\log(1-P)$ có đạo hàm theo $z$ lần lượt là $1-P$ và $-P$, vì $\operatorname{sig}'(z)=\operatorname{sig}(z)\bigl(1-\operatorname{sig}(z)\bigr)$; nhân với $\nabla_\theta z=\phi(s)$.
:::

::: solution Lời giải Bài tập 09.16
**Câu (a).** Theo softmax,
$$
\begin{aligned}
\pi_\theta(1\mid s)&=\frac{e^{h(s,1,\theta)}}{e^{h(s,0,\theta)}+e^{h(s,1,\theta)}}\\
&=\frac{1}{1+e^{h(s,0,\theta)-h(s,1,\theta)}}\\
&=\frac1{1+e^{-\theta^\top\phi(s)}} .
\end{aligned}
$$
Chỉ hiệu hai mức ưu tiên ảnh hưởng đến chính sách, vì cộng cùng một hằng vào mọi mức ưu tiên không đổi softmax.

**Câu (b).** Đặt $z=\theta^\top\phi(s)$, $P=\operatorname{sig}(z)$. Với $a=1$: $\psi_\theta(s,1)=\dfrac{\operatorname{sig}'(z)}{\operatorname{sig}(z)}\nabla_\theta z=(1-P)\,\phi(s)$. Với $a=0$: $\psi_\theta(s,0)=\dfrac{-\operatorname{sig}'(z)}{1-\operatorname{sig}(z)}\nabla_\theta z=-P\,\phi(s)$. Gộp lại:
$$
\psi_\theta(s,a)=(a-P)\,\phi(s),\qquad a\in\{0,1\}.
$$
Kỳ vọng: $P(1-P)\phi(s)+(1-P)(-P)\phi(s)=0$, đúng Mệnh đề 09.17. Kết quả cũng suy từ Mệnh đề 09.16 với $\phi(s,1)=\phi(s)$, $\phi(s,0)=0$: $\psi_\theta(s,a)=\phi(s,a)-P\phi(s)$.

**Câu (c).** Theo Định lý 09.23, mẫu của gradient tại bước $t$ là $\gamma^tG_t\psi_t$, nên
$$
\theta_{t+1}=\theta_t+\alpha\,\gamma^t\,G_t\,(A_t-P_t)\,\phi(S_t).
$$
Thuật toán 09.25 cộng các hạng này trên cả lượt với $\theta_{\mathrm{old}}$ giữ cố định rồi cập nhật một lần; dạng thuật toán trong Sutton và Barto (2018, §13.3) cập nhật ngay sau mỗi bước, với $\theta$ hiện tại.

**Câu (d).** $z=0{,}5\cdot1+0{,}5\cdot(-2)=-0{,}5$; $P_0=\operatorname{sig}(-0{,}5)=1/(1+e^{0{,}5})\approx0{,}3775$. $\psi_\theta(s,1)=(1-0{,}3775)(1;\,-2)\approx(0{,}6225;\,-1{,}2449)$. Bước: $\alpha\gamma^0G_0\psi=0{,}1\cdot2\cdot(0{,}6225;\,-1{,}2449)\approx(0{,}1245;\,-0{,}2490)$, nên $\theta\approx(0{,}6245;\,0{,}2510)$. Mới: $z\approx0{,}6245-2\cdot0{,}2510=0{,}1225$, $\pi_\theta(1\mid s)=\operatorname{sig}(0{,}1225)\approx0{,}5306$, tăng từ $0{,}3775$.

**Kiểm tra lại.** Với $G_0>0$ và $A_0=1$, bước làm $P$ tăng, đúng chiều. Nếu $A_0=0$ với cùng $G_0=2$, hàm điểm là $-0{,}3775\,(1;\,-2)$ và bước làm $P$ giảm. Lỗi thường gặp: dùng $a-P$ với $a\in\{1,2\}$ thay vì $\{0,1\}$; quên thừa số $\phi(s)$; dùng $P$ sau cập nhật trong hàm điểm.
:::

### Bài tập 09.17. Định lý gradient chính sách có chiết khấu theo phương trình Bellman

**Mức độ:** chứng minh. Mục tiêu học tập: chứng minh dạng phân bố chiếm dụng có chiết khấu của định lý gradient chính sách bằng phương trình Bellman, không qua xác suất quỹ đạo, và suy ra thừa số $\gamma^t$ trong REINFORCE.

**Nguồn:** Sutton và Barto (2018), §13.2–13.3 và Bài tập 13.2; ghi chú bài giảng Bài 09, Mục 6 (Định lý 09.23, Hệ quả 09.24, Thuật toán 09.25).

::: exercise Bài tập 09.17 (Định lý gradient chính sách có chiết khấu theo phương trình Bellman)
(Theo Sutton và Barto, 2018, Bài tập 13.2.) MDP có $\mathcal S$, $\mathcal A$ hữu hạn, trạng thái đầu cố định $s_0$, động lực $P(s',r\mid s,a)$ (Sutton và Barto viết $p(s',r\mid s,a)$) không phụ thuộc $\theta$, phần thưởng bị chặn và độ dài lượt $T\le T_{\max}$ dưới mọi $\pi_\theta$; $\gamma\in[0,1]$. Chính sách $\pi_\theta(a\mid s)$ khả vi theo $\theta$. $J(\theta)=v_{\pi_\theta}(s_0)$; giá trị tại trạng thái kết thúc bằng $0$. Viết $\pi=\pi_\theta$ và $\Pr(s\to x,k,\pi)$ cho xác suất ở trạng thái không kết thúc $x$ sau đúng $k$ bước, xuất phát từ $s$, dưới $\pi$.

- (a) Đặt $g(s)=\sum_a\nabla_\theta\pi(a\mid s)\,q_\pi(s,a)$. Từ $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$ và $q_\pi(s,a)=\sum_{s',r}P(s',r\mid s,a)\bigl(r+\gamma v_\pi(s')\bigr)$, chứng minh $\nabla_\theta v_\pi(s)=g(s)+\gamma\sum_{s'}P_\pi(s'\mid s)\nabla_\theta v_\pi(s')$, với $P_\pi(s'\mid s)=\sum_a\pi(a\mid s)\sum_rP(s',r\mid s,a)$.
- (b) Lặp đẳng thức ở (a) để được $\nabla_\theta v_\pi(s)=\sum_x\sum_{k\ge0}\gamma^k\Pr(s\to x,k,\pi)\,g(x)$, rồi suy ra $\nabla_\theta J=\sum_x\eta_\gamma(x)\sum_a\nabla_\theta\pi(a\mid x)\,q_\pi(x,a)$ với $\eta_\gamma(x)=\sum_{k\ge0}\gamma^k\Pr(s_0\to x,k,\pi)$.
- (c) Suy ra $\nabla_\theta J=\mathbb E_\pi\bigl[\sum_{t=0}^{T-1}\gamma^tG_t\psi_t\bigr]$ và bước cập nhật REINFORCE tại bước $t$, $\theta\leftarrow\theta+\alpha\gamma^tG_t\psi_t$. Giải thích thừa số $\gamma^t$ đến từ đâu.
:::

::: hint Gợi ý Bài tập 09.17
(a) Quy tắc tích cho $\nabla(\pi q)$; $P$ và $r$ không phụ thuộc $\theta$. (b) Thay $\nabla v_\pi(s')$ ở vế phải bằng chính đẳng thức (a); sau $T_{\max}$ bước mọi lượt đã kết thúc. (c) Viết $\nabla\pi=\pi\psi$, đổi tổng theo $x$ thành kỳ vọng theo $S_k$, rồi dùng $\mathbb E[G_k\mid S_k,A_k]=q_\pi(S_k,A_k)$.
:::

::: solution Lời giải Bài tập 09.17
**Câu (a).** Theo quy tắc tích,
$$
\begin{aligned}
\nabla_\theta v_\pi(s)
&=\sum_a\nabla_\theta\pi(a\mid s)\,q_\pi(s,a)\\
&\quad+\sum_a\pi(a\mid s)\,\nabla_\theta q_\pi(s,a)\\
&=g(s)+\gamma\sum_a\pi(a\mid s)\\
&\qquad\cdot\sum_{s',r}P(s',r\mid s,a)\,\nabla_\theta v_\pi(s')\\
&=g(s)+\gamma\sum_{s'}P_\pi(s'\mid s)\,\nabla_\theta v_\pi(s').
\end{aligned}
$$
Đẳng thức thứ hai dùng $\nabla_\theta q_\pi(s,a)=\sum_{s',r}P(s',r\mid s,a)\,\gamma\nabla_\theta v_\pi(s')$, vì $P$ và $r$ không phụ thuộc $\theta$; đẳng thức thứ ba gom tổng theo $a$ và $r$. Hạng ứng với $s'$ kết thúc bằng $0$ vì $v_\pi$ tại đó luôn bằng $0$.

**Câu (b).** Thế đẳng thức (a) cho $\nabla_\theta v_\pi(s')$ vào chính nó $K$ lần:
$$
\begin{aligned}
\nabla_\theta v_\pi(s)&=\sum_{k=0}^{K}\gamma^k\sum_x\Pr(s\to x,k,\pi)\,g(x)\\
&\quad+\gamma^{K+1}\sum_x\Pr(s\to x,K+1,\pi)\\
&\qquad\cdot\nabla_\theta v_\pi(x),
\end{aligned}
$$
vì $\Pr(s\to x,k+1,\pi)=\sum_{x'}\Pr(s\to x',k,\pi)P_\pi(x\mid x')$ trên các trạng thái không kết thúc. Với $K+1\ge T_{\max}$, mọi lượt đã kết thúc, $\Pr(s\to x,K+1,\pi)=0$, nên phần dư bằng $0$ và tổng theo $k$ hữu hạn. Đặt $s=s_0$ và đổi thứ tự hai tổng: $\nabla_\theta J=\sum_x\eta_\gamma(x)\,g(x)$, đúng biểu thức cần chứng minh.

**Câu (c).** Dùng $\nabla_\theta\pi=\pi\psi_\theta$ trên tập $\pi>0$ và $\Pr(s_0\to x,k,\pi)=\Pr(S_k=x,\,k<T)$:
$$
\begin{aligned}
\nabla_\theta J
&=\sum_{k\ge0}\gamma^k\sum_x\Pr(S_k=x,\,k<T)\\
&\qquad\cdot\sum_a\pi(a\mid x)\,q_\pi(x,a)\,\psi_\theta(x,a)\\
&=\sum_{k\ge0}\gamma^k\,\mathbb E\bigl[\mathbf 1\{k<T\}\,q_\pi(S_k,A_k)\,\psi_k\bigr]\\
&=\sum_{k\ge0}\gamma^k\,\mathbb E\bigl[\mathbf 1\{k<T\}\,G_k\,\psi_k\bigr]\\
&=\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^tG_t\psi_t\Bigr].
\end{aligned}
$$
Đẳng thức thứ hai viết tổng theo $x$, $a$ thành kỳ vọng theo $(S_k,A_k)$, với $A_k\sim\pi(\cdot\mid S_k)$. Đẳng thức thứ ba dùng tính chất tháp: $\mathbf 1\{k<T\}\psi_k$ là hàm của $(S_k,A_k)$ và $\mathbb E[G_k\mid S_k,A_k]=q_\pi(S_k,A_k)$ theo tính Markov; tổng hữu hạn vì $T\le T_{\max}$. Mỗi lượt cho mẫu $\sum_t\gamma^tG_t\psi_t$; lấy một hạng một lần được bước $\theta\leftarrow\theta+\alpha\gamma^tG_t\psi_t$, dạng thuật toán trong Sutton và Barto (2018, §13.3).

Thừa số $\gamma^t$ đến từ $\eta_\gamma$: trạng thái thăm ở bước $k$ được tính với trọng số $\gamma^k$, vì $J=v_\pi(s_0)$ chiết khấu mọi phần thưởng từ bước $0$. Với $\gamma=1$, $\eta_1(x)$ là số lần thăm $x$ kỳ vọng trong một lượt, và (b) trở thành $\nabla_\theta J=\sum_x\eta_1(x)\sum_a\nabla_\theta\pi(a\mid x)\,q_\pi(x,a)$, dạng định lý gradient chính sách mà Sutton và Barto (2018, §13.2) phát biểu cho trường hợp không chiết khấu, ở đó viết dưới dạng tỉ lệ với phân phối thăm đã chuẩn hóa.

**Kiểm tra lại.** Kết quả (c) trùng Định lý 09.23, chứng minh bằng đường khác: ghi chú đi qua $\nabla\log p_\theta(\tau)$ và bỏ phần thưởng quá khứ, bài này đi qua phương trình Bellman của $\nabla v_\pi$. Khi $\gamma<1$, $\eta_\gamma(x)=\nu^\pi_\gamma(x)/(1-\gamma)$ tại mọi trạng thái không kết thúc $x$, nên (b) là Hệ quả 09.24. Lỗi thường gặp: quên hạng $\pi\nabla q$ ở (a), tức coi $q_\pi$ không phụ thuộc $\theta$; bỏ $\gamma^k$ khi lặp, được $\eta_1$ thay cho $\eta_\gamma$, và hướng cập nhật không còn là gradient của $J$ khi $\gamma<1$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 09.18. Q-learning và Double Q-learning trên MDP độ chệch cực đại

**Mức độ:** vận dụng (lập trình). Mục tiêu học tập: đo tác động của độ chệch của phép cực đại lên chính sách học được và kiểm tác dụng của học kép trên một MDP nhỏ.

**Nguồn:** Sutton và Barto (2018), §6.7, Ví dụ 6.7 và Hình 6.5; ghi chú bài giảng Bài 09, Mục 2–3 (Mệnh đề 09.2, 09.4, Thuật toán 09.7). Kết quả số trong lời giải là một lần chạy của người soạn.

::: exercise Bài tập 09.18 (Q-learning và Double Q-learning trên MDP độ chệch cực đại)
(Theo Sutton và Barto, 2018, Ví dụ 6.7 và Hình 6.5.) MDP độ chệch cực đại: lượt bắt đầu ở $s_{\mathrm A}$; tại $s_{\mathrm A}$, "phải" ($a_{\mathrm R}$) kết thúc với phần thưởng $0$, "trái" ($a_{\mathrm L}$) sang $s_{\mathrm B}$ với phần thưởng $0$; tại $s_{\mathrm B}$ có $m$ hành động, mỗi hành động kết thúc với phần thưởng $\mathcal N(-0{,}1;\,1)$; $\gamma=1$. Mọi giá trị khởi tạo bằng $0$; hành vi $\epsilon$-tham lam với $\epsilon=0{,}1$, phá hòa ngẫu nhiên; $\alpha=0{,}1$.

Khung chương trình bằng Python, chỉ dùng thư viện chuẩn. Hàm `egreedy` chọn đều với xác suất `eps`, ngược lại chọn một chỉ số có giá trị lớn nhất, phá hòa đều. Hàm `update_left` thực hiện một bước cập nhật của cặp $(s_{\mathrm A},a_{\mathrm L})$: `q_left` là giá trị hiện tại, `q_b_eval` là hàng giá trị dùng để đánh giá tại $s_{\mathrm B}$, `b_star` là chỉ số hành động được chọn tại $s_{\mathrm B}$. Trong `run`, `Q1["A"]` có hai phần tử (chỉ số `0` là "trái", `1` là "phải"), `Q1["B"]` có $m$ phần tử, `Q2` chỉ dùng khi `double=True`; `left[e]` bằng `True` khi lượt `e` chọn "trái" tại $s_{\mathrm A}$.

```python
import random

def egreedy(values, eps, rng):
    if rng.random() < eps:
        return rng.randrange(len(values))
    best = max(values)
    return rng.choice([i for i, v in enumerate(values) if v == best])

def update_left(q_left, q_b_eval, b_star, alpha):
    ...

def run(double, m, episodes, rng, eps=0.1, alpha=0.1):
    Q1 = {"A": [0.0, 0.0], "B": [0.0] * m}
    Q2 = {"A": [0.0, 0.0], "B": [0.0] * m}
    left = []
    for e in range(episodes):
        ...
    return left

QB1 = [0.35, -0.62, -0.08, -0.41]
QB2 = [-0.30, 0.12, -0.25, 0.05]
assert abs(update_left(0.0, QB1, 0, 0.1) - 0.035) < 1e-12
assert abs(update_left(0.0, QB2, 0, 0.1) - (-0.030)) < 1e-12
```

Hai câu `assert` là hai bước tính tay của Bài tập 09.11 với $\alpha=0{,}1$ và $Q_1(s_{\mathrm A},a_{\mathrm L})=0$: câu đầu là bước Q-learning ($b^*=b_1$, đánh giá bằng $Q_1$, giá trị mới $0{,}035$); câu sau là bước Double Q-learning cập nhật $Q_1$ ($b^*=b_1$ chọn bằng $Q_1$, đánh giá bằng $Q_2$, giá trị mới $-0{,}030$).

- (a) Hoàn thiện `run` cho Q-learning (`double=False`, hành vi theo $Q_1$) và Double Q-learning (`double=True`, hành vi $\epsilon$-tham lam theo $Q_1+Q_2$, mục tiêu theo Thuật toán 09.7). Lưu ý cập nhật cặp $(s_{\mathrm A},a_{\mathrm L})$ dùng mẫu chuyển sang $s_{\mathrm B}$ trước khi chọn hành động tại $s_{\mathrm B}$.
- (b) Viết `update_left` sao cho hai câu `assert` đúng, rồi dùng nó trong `run`. Với $m=10$, chạy $300$ lượt, lặp $1000$ lần chạy, vẽ tỉ lệ chọn "trái" tại $s_{\mathrm A}$ theo chỉ số lượt cho hai thuật toán, cùng đường $5\%$.
- (c) Lặp lại (b) với $m\in\{1;\,2;\,100\}$. Nêu xu hướng của tỉ lệ chọn "trái" ở $50$ lượt cuối theo $m$ cho mỗi thuật toán và giải thích bằng Mệnh đề 09.2.
:::

::: hint Gợi ý Bài tập 09.18
Mục tiêu Q-learning của $(s_{\mathrm A},a_{\mathrm L})$ là $0+\max_bQ_1(s_{\mathrm B},b)$; của $(s_{\mathrm A},a_{\mathrm R})$ là $0$. Với Double Q-learning, tung đồng xu cho từng lần cập nhật; bảng được cập nhật chọn $b^*$ tại $s_{\mathrm B}$, bảng kia cho giá trị. Tại $s_{\mathrm B}$, mục tiêu là phần thưởng vừa nhận vì lượt kết thúc. Tỉ lệ ở mỗi lượt là trung bình của `left[e]` trên các lần chạy.
:::

::: solution Lời giải Bài tập 09.18
**Câu (a).** Phần thân vòng lặp, cho Q-learning: chọn $a$ bằng `egreedy(Q1["A"], ...)`. Nếu $a$ là "phải", cập nhật $Q_1(s_{\mathrm A},a_{\mathrm R})\leftarrow Q_1(s_{\mathrm A},a_{\mathrm R})+\alpha(0-Q_1(s_{\mathrm A},a_{\mathrm R}))$ và kết thúc lượt. Nếu $a$ là "trái", cập nhật $Q_1(s_{\mathrm A},a_{\mathrm L})\leftarrow Q_1(s_{\mathrm A},a_{\mathrm L})+\alpha\bigl(0+\max_bQ_1(s_{\mathrm B},b)-Q_1(s_{\mathrm A},a_{\mathrm L})\bigr)$, chọn $b$ $\epsilon$-tham lam theo $Q_1(s_{\mathrm B},\cdot)$, lấy $r\sim\mathcal N(-0{,}1;\,1)$ bằng `rng.gauss(-0.1, 1.0)` và cập nhật $Q_1(s_{\mathrm B},b)\leftarrow Q_1(s_{\mathrm B},b)+\alpha(r-Q_1(s_{\mathrm B},b))$. Với Double Q-learning, mỗi lần cập nhật tung đồng xu; nhánh $Q_1$ dùng mục tiêu $0+Q_2(s_{\mathrm B},\arg\max_bQ_1(s_{\mathrm B},b))$ tại $s_{\mathrm A}$ và $r$ tại $s_{\mathrm B}$; nhánh $Q_2$ đổi vai trò. Hàm `update_left` trả `q_left + alpha * (0 + q_b_eval[b_star] - q_left)`; Q-learning gọi nó với `q_b_eval = Q1["B"]` và `b_star` là chỉ số lớn nhất của `Q1["B"]`, Double Q-learning gọi với hàng của bảng kia. Kiểm tay: $0+0{,}1\,(0+0{,}35-0)=0{,}035$ và $0+0{,}1\,(0-0{,}30-0)=-0{,}030$.

**Câu (b).** Kết quả định tính cần thấy: Q-learning nhanh chóng chọn "trái" ở phần lớn lượt, vượt xa $5\%$, rồi giảm chậm; Double Q-learning bắt đầu quanh $50\%$ do phá hòa ở các giá trị khởi tạo bằng $0$, rồi giảm nhanh về gần $5\%$. Một lần chạy của người soạn ($m=10$, $1000$ lần chạy, hạt giống `random.Random(2026)` cho Q-learning và `random.Random(2027)` cho Double Q-learning): Q-learning đạt đỉnh khoảng $94\%$ quanh lượt $18$ và còn khoảng $13\%$ ở lượt $251$–$300$; Double Q-learning có đỉnh khoảng $53\%$ ở các lượt đầu và khoảng $6\%$ ở lượt $251$–$300$. Hình 6.5 của nguồn, trung bình trên $10\,000$ lần chạy, có cùng dạng: Q-learning lên gần $90\%$ ở các lượt đầu rồi giảm dần, Double Q-learning bắt đầu từ khoảng $50\%$ rồi giảm nhanh về gần $5\%$. Nguồn không nêu $m$; độ cao đỉnh phụ thuộc $m$ như câu (c).

**Câu (c).** Lần chạy của người soạn ($1000$ lần chạy mỗi cấu hình, cùng hai hạt giống) cho tỉ lệ chọn "trái" ở lượt $251$–$300$: Q-learning khoảng $7\%$, $8\%$, $13\%$, $95\%$ với $m=1$, $2$, $10$, $100$; Double Q-learning khoảng $6\%$–$7\%$ với mọi $m$. Theo Mệnh đề 09.2, $\mathbb E[\max_bQ(s_{\mathrm B},b)]\ge\max_bq_*(s_{\mathrm B},b)=-0{,}1$, và độ chệch tăng khi số hành động nhiễu tăng: với $m=1$ không có phép cực đại thật sự, nên không có độ chệch của phép cực đại; với $m=100$, giá trị cực đại của trăm ước lượng nhiễu giữ $Q(s_{\mathrm A},a_{\mathrm L})$ trên $0$ suốt $300$ lượt. Mục tiêu kép đánh giá hành động thắng bằng bảng kia, nên không chệch lên theo Mệnh đề 09.4 khi hai bảng gần độc lập.

**Kiểm tra lại.** Xác suất chọn "trái" của hành vi $\epsilon$-tham lam với $\epsilon=0{,}1$ trên hai hành động không nhỏ hơn $5\%$. Trên $1000$ lần chạy, tỉ lệ đo được ở một lượt có sai số chuẩn khoảng $\sqrt{0{,}05\cdot0{,}95/1000}\approx0{,}7$ điểm phần trăm, nên vài lượt ở $4{,}5\%$ là bình thường; một đường nằm dưới khoảng $3{,}6\%$ (hai sai số chuẩn) qua nhiều lượt liên tiếp là dấu hiệu lỗi. Lỗi thường gặp: cập nhật $(s_{\mathrm A},a_{\mathrm L})$ sau khi đã cập nhật $Q(s_{\mathrm B},\cdot)$ bằng phần thưởng của chính lượt đó (đổi thứ tự so với thuật toán); trong Double Q-learning, dùng cùng một bảng để chọn và đánh giá; khởi tạo ngẫu nhiên thay vì bằng $0$, làm mất hiện tượng phá hòa ở lượt đầu.
:::

### Bài tập 09.19. REINFORCE trên hành lang ngắn

**Mức độ:** vận dụng (lập trình). Mục tiêu học tập: cài đặt REINFORCE với chính sách softmax trên một môi trường có đặc trưng gộp trạng thái, đối chiếu với giá trị tối ưu tính ở Bài tập 09.14 và quan sát ảnh hưởng của bước $\alpha$.

**Nguồn:** Sutton và Barto (2018), §13.3, Ví dụ 13.1 và Hình 13.1; ghi chú bài giảng Bài 09, Mục 6 (Thuật toán 09.25, Hệ quả 09.26). Kết quả số trong lời giải là một lần chạy của người soạn.

::: exercise Bài tập 09.19 (REINFORCE trên hành lang ngắn)
(Theo Sutton và Barto, 2018, Ví dụ 13.1 và Hình 13.1.) Hành lang ngắn đảo hành động: ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích); phần thưởng $-1$ mỗi bước; $\gamma=1$; hành động 1 "sang phải", hành động 2 "sang trái"; ở $s_2$ hai hành động bị đảo; sang trái tại $s_1$ thì đứng yên. Chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ ở mọi ô, nên $p=\pi_\theta(1\mid s)=1/(1+e^{-(\theta_1-\theta_2)})$. Khởi tạo $\theta_0=(0;\,\log19)$, tức $p=0{,}05$. Lượt bị cắt sau $1000$ bước nếu chưa tới đích (cắt ngắn, không phải kết thúc của MDP).

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

Khung chương trình bằng Python, chỉ dùng thư viện chuẩn. Hàm `step(s, a)` nhận ô `s` thuộc `{1, 2, 3}` và hành động `a` thuộc `{1, 2}`, trả ô kế tiếp, với `4` là đích. Hàm `grad_estimate(actions, p)` nhận dãy hành động của một lượt sinh với xác suất `p` không đổi và trả hai tọa độ của $\widehat g=\sum_tG_t\psi_t$. Hàm `reinforce` giữ `p` cố định trong cả lượt ($\theta_{\mathrm{old}}$) và trả danh sách $G_0$ của các lượt cùng $\theta$ cuối.

```python
import math, random

def step(s, a):
    ...

def grad_estimate(actions, p):
    ...

def reinforce(alpha, episodes, rng, theta0=(0.0, math.log(19)), cap=1000):
    theta = list(theta0)
    returns = []
    for e in range(episodes):
        p = 1 / (1 + math.exp(-(theta[0] - theta[1])))
        ...
    return returns, theta

pairs = [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
assert [step(s, a) for s, a in pairs] == [2, 1, 1, 3, 4, 2]
g = grad_estimate([1, 1, 1, 2, 1], 0.5)
assert len(g) == 2 and all(math.isclose(x, y) for x, y in zip(g, (-5.5, 5.5)))
```

- (a) Hoàn thiện `step` và `reinforce` theo Thuật toán 09.25: sinh cả lượt bằng $\theta_{\mathrm{old}}$, tính $G_t$ từ cuối lượt, $\widehat g=\sum_tG_t\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$, rồi $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\widehat g$. Hai câu `assert` kiểm phép đảo hành động ở $s_2$ và lượt tính tay của Bài tập 09.20: tại $p=\tfrac12$, lượt có hành động $1,1,1,2,1$ cho $\widehat g=(-5{,}5;\,5{,}5)$.
- (b) Với $\alpha\in\{2^{-12};\,2^{-13};\,2^{-14}\}$, chạy $1000$ lượt, lặp $100$ lần chạy, vẽ $G_0$ trung bình theo chỉ số lượt cùng đường $J(p^*)=-(6+4\sqrt2)\approx-11{,}66$ của Bài tập 09.14. Báo cáo $G_0$ trung bình ở $100$ lượt cuối và $p$ cuối, kèm sai số chuẩn trên các lần chạy.
- (c) Đổi sang cập nhật sau từng bước, như dạng thuật toán trong Sutton và Barto (2018, §13.3): trong vòng lặp theo $t$, tính $\psi$ bằng $\theta$ hiện tại và cập nhật $\theta\leftarrow\theta+\alpha G_t\psi_t$ ngay. So hai cách với $\alpha=2^{-12}$; giải thích khác biệt bằng điều kiện của Hệ quả 09.26.
:::

::: hint Gợi ý Bài tập 09.19
Với hai hành động và đặc trưng đơn vị, $\psi_\theta(s,1)=(1-p)(1;\,-1)$ và $\psi_\theta(s,2)=-p\,(1;\,-1)$, nên chỉ cần cộng một số vô hướng $c=\sum_tG_t\,(\mathbf 1\{A_t=1\}-p)$ rồi đặt $\widehat g=c\,(1;\,-1)$. Với $\gamma=1$ và phần thưởng $-1$, $G_t=-(T-t)$.
:::

::: solution Lời giải Bài tập 09.19
**Câu (a).** `step`: tại $s=1$, hành động 1 cho $2$, hành động 2 cho $1$; tại $s=2$, hành động 1 cho $1$, hành động 2 cho $3$; tại $s=3$, hành động 1 cho $4$, hành động 2 cho $2$. Trong `reinforce`: sinh lượt với $p$ cố định tới khi $s=4$ hoặc đủ `cap` bước; với $T$ là độ dài lượt, $G_t=-(T-t)$; $c=\sum_tG_t(\mathbf 1\{A_t=1\}-p)$; cập nhật $\theta_1\leftarrow\theta_1+\alpha c$, $\theta_2\leftarrow\theta_2-\alpha c$. Lượt tính tay: $c=\tfrac12(-5-4-3-1)+\tfrac12\cdot2=-5{,}5$, khớp Bài tập 09.20.

**Câu (b).** Kết quả định tính cần thấy: cả ba bước đi từ $G_0$ quanh $-80$ (giá trị $J(0{,}05)\approx-82{,}1$) về phía $-12$; bước lớn hơn tiến nhanh hơn, và với $\alpha=2^{-14}$, sau $1000$ lượt $G_0$ mới tới khoảng $-15$; không đường nào vượt $-11{,}66$ ngoài dao động do lấy mẫu. Một lần chạy của người soạn (hạt giống `random.Random(100 + k)` với $\alpha=2^{-k}$, $100$ lần chạy), trung bình trên các lần chạy, trong ngoặc là sai số chuẩn: $G_0$ trung bình ở lượt $901$–$1000$ là $-11{,}87$ ($0{,}11$), $-12{,}50$ ($0{,}11$), $-15{,}10$ ($0{,}14$) với $k=12$, $13$, $14$; $p$ cuối là $0{,}550$ ($0{,}004$), $0{,}470$ ($0{,}003$), $0{,}343$ ($0{,}002$), so với $p^*\approx0{,}586$. Ở gần $p^*$, $J$ rất phẳng: $J(0{,}5)=-12$ chỉ kém $J(p^*)$ khoảng $0{,}34$, nên $G_0$ gần tối ưu không đòi hỏi $p$ sát $p^*$.

**Câu (c).** Cập nhật trong lượt dùng $\theta$ đã đổi ở các bước trước để tính $\psi$, trong khi lượt được sinh bởi $\theta$ cũ; tổng các bước không còn là $\alpha$ nhân một mẫu của $\nabla_\theta J(\theta_{\mathrm{old}})$, vì Hệ quả 09.26 cần lượt sinh bởi $\pi_{\theta_{\mathrm{old}}}$ và $\theta_{\mathrm{old}}$ giữ cố định cả lượt. Trong một lượt, $\theta$ trôi khỏi $\theta_{\mathrm{old}}$ một lượng có chuẩn không quá $\alpha\sum_t\lvert G_t\rvert\,\lVert\psi_t\rVert\le\sqrt2\,\alpha T^2$, vì $\lvert G_t\rvert\le T$ và $\lVert\psi_t\rVert\le\sqrt2$; đây là cận trên, không phải độ trôi thực. Hai cách gần nhau khi cận này nhỏ so với $1$, tức khi $p$ thay đổi không đáng kể trong một lượt; với $p$ gần $0$ hoặc $1$, lượt kéo dài tới $1000$ bước, cận $\sqrt2\,\alpha T^2$ với $T=1000$, $\alpha=2^{-12}$ khoảng $345$, nên không còn gì bảo đảm hai cách gần nhau, và các bước trong lượt kéo $\theta$ đi xa $\theta_{\mathrm{old}}$. Một lần chạy của người soạn với $\alpha=2^{-12}$ (hạt giống `random.Random(212)`, $100$ lần chạy): $5$ lần chạy kết thúc với $p>0{,}9$, lượt lặp $s_1,s_2$ tới khi bị cắt ở $1000$ bước, và $G_0$ trung bình ở $100$ lượt cuối khoảng $-61$; với $\alpha=2^{-13}$ không lần chạy nào như vậy. Cách cập nhật một lần mỗi lượt với $\alpha=2^{-12}$ không có lần chạy nào $p>0{,}9$ trong $100$ lần chạy.

**Kiểm tra lại.** $G_0$ trung bình không thể vượt $J(p^*)\approx-11{,}66$ ngoài sai số lấy mẫu; nếu vượt rõ, kiểm lại phép đảo hành động ở $s_2$. Lỗi thường gặp: cập nhật $\theta_2$ cùng dấu với $\theta_1$; tính $G_t$ từ đầu lượt thay vì từ cuối; quên cắt lượt, khiến chương trình không dừng khi $p$ gần $0$ hoặc $1$ (Bài tập 09.12(b)).
:::

### Bài tập 09.20. Gradient đúng và một mẫu REINFORCE trên hành lang ngắn

**Mức độ:** vận dụng. Mục tiêu học tập: so một ước lượng REINFORCE trên một lượt với gradient đúng, phân biệt không chệch với chính xác trên từng lượt, và ước lượng số lượt cần để trung bình đủ tin cậy.

**Nguồn:** Sutton và Barto (2018), §13.1 và §13.3 (Ví dụ 13.1); ghi chú bài giảng Bài 09, Mục 5–6 (Mệnh đề 09.16, Định lý 09.23, Hệ quả 09.26); lượt ở (b) tự xây dựng; độ lệch chuẩn ở (d) từ mô phỏng của người soạn.

::: exercise Bài tập 09.20 (Gradient đúng và một mẫu REINFORCE trên hành lang ngắn)
Hành lang ngắn đảo hành động: ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích); phần thưởng $-1$ mỗi bước; $\gamma=1$; hành động 1 "sang phải", hành động 2 "sang trái"; ở $s_2$ hai hành động bị đảo; sang trái tại $s_1$ thì đứng yên. Chính sách softmax với $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ ở mọi ô, $\theta=(0;\,0)$, nên $p=\pi_\theta(1\mid s)=\tfrac12$. Theo Bài tập 09.14, $J(p)=-\dfrac{2(2-p)}{p(1-p)}$.

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

- (a) Tính $\nabla_\theta J$ tại $\theta=(0;\,0)$ bằng quy tắc dây chuyền qua $p$.
- (b) Một lượt có hành động $A_0,\dots,A_4=1,1,1,2,1$. Ghi dãy trạng thái, tính $G_t$, $\psi_t$ và $\widehat g=\sum_tG_t\psi_t$.
- (c) Với $\alpha=0{,}1$, tính $\theta$ và $p$ sau bước $\theta\leftarrow\theta+\alpha\widehat g$, rồi tính $J$ tại $p$ mới. So chiều của $\widehat g$ với $\nabla_\theta J$ và giải thích vì sao điều này không mâu thuẫn với Hệ quả 09.26.
- (d) Một lần chạy của người soạn, $400\,000$ lượt tại $\theta=(0;\,0)$ với hạt giống `random.Random(1)`, cho tọa độ đầu của $\widehat g$ trung bình khoảng $1{,}96$ và độ lệch chuẩn khoảng $27$. Cần khoảng bao nhiêu lượt để sai số chuẩn của trung bình tọa độ đầu không quá $0{,}5$? Nêu một cách giảm số lượt đó.
:::

::: hint Gợi ý Bài tập 09.20
(a) Lấy đạo hàm $J(p)$ theo $p$ bằng quy tắc thương, rồi nhân với $\mathrm dp/\mathrm d\theta$; với $p=1/(1+e^{-(\theta_1-\theta_2)})$, đạo hàm của $p$ theo $\theta_1-\theta_2$ là $p(1-p)$. (b) $\psi_\theta(s,1)=\phi(s,1)-\bigl(\tfrac12;\,\tfrac12\bigr)$. (d) Sai số chuẩn là độ lệch chuẩn chia cho căn bậc hai của số lượt.
:::

::: solution Lời giải Bài tập 09.20
**Câu (a).** Viết $J(p)=-2\,\dfrac{2-p}{p-p^2}$. Theo quy tắc thương,
$$
\begin{aligned}
J'(p)&=-2\,\frac{-(p-p^2)-(2-p)(1-2p)}{(p-p^2)^2}\\
&=\frac{2(p^2-4p+2)}{\bigl(p(1-p)\bigr)^2},
\end{aligned}
$$
trong đó tử số: $(p-p^2)+(2-p)(1-2p)=p-p^2+2-5p+2p^2=p^2-4p+2$. Tử số bằng $0$ tại $p^*=2-\sqrt2$, khớp Bài tập 09.14. Tại $p=\tfrac12$: $J'(\tfrac12)=\dfrac{2\cdot0{,}25}{0{,}0625}=8$, và $\dfrac{\mathrm dp}{\mathrm d\theta}=p(1-p)(1;\,-1)=\tfrac14(1;\,-1)$. Vậy $\nabla_\theta J=8\cdot\tfrac14(1;\,-1)=(2;\,-2)$: tăng $\theta_1$, giảm $\theta_2$, tức tăng $p$ về phía $p^*\approx0{,}59$.

**Câu (b).** Dãy: $s_1\xrightarrow{1}s_2\xrightarrow{1}s_1\xrightarrow{1}s_2\xrightarrow{2}s_3\xrightarrow{1}s_4$; $T=5$. Lợi tức $G_t=-(5-t)$: $-5$, $-4$, $-3$, $-2$, $-1$. Đặc trưng trung bình $(\tfrac12;\,\tfrac12)$, nên $\psi_\theta(s,1)=(\tfrac12;\,-\tfrac12)$, $\psi_\theta(s,2)=(-\tfrac12;\,\tfrac12)$. Tọa độ đầu của $\widehat g$:
$$
\begin{aligned}
&\tfrac12\bigl(-5-4-3-1\bigr)+\bigl(-\tfrac12\bigr)(-2)\\
&=-6{,}5+1=-5{,}5 ,
\end{aligned}
$$
và tọa độ sau ngược dấu: $\widehat g=(-5{,}5;\,5{,}5)$.

**Câu (c).** $\theta=(0;\,0)+0{,}1\,(-5{,}5;\,5{,}5)=(-0{,}55;\,0{,}55)$; $p=1/(1+e^{1{,}1})\approx0{,}250$; $J(0{,}250)\approx-18{,}68$, kém $J(0{,}5)=-12$. $\widehat g$ ngược chiều $\nabla_\theta J$. Hệ quả 09.26 nói $\mathbb E[\widehat g]=\nabla_\theta J$, không nói mỗi lượt cho đúng chiều. Mọi phần thưởng âm, nên mọi $G_t<0$ và mỗi hành động đã chọn bị giảm xác suất theo $\lvert G_t\rvert$; lượt này chọn hành động 1 bốn lần, nên $p$ giảm. Chiều $(2;\,-2)$ chỉ xuất hiện khi lấy trung bình trên nhiều lượt, như câu (d).

**Câu (d).** Cần $27/\sqrt n\le0{,}5$, tức $n\ge(27/0{,}5)^2=2916$ lượt. Độ lệch chuẩn $27$ gấp khoảng $13$ lần giá trị đúng $2$. Một cách giảm: trừ một đường cơ sở $b(s)$ khỏi $G_t$; theo Mệnh đề 09.17, $\mathbb E[b(S_t)\psi_t\mid S_t]=0$, nên kỳ vọng không đổi, trong khi phần âm chung của mọi $G_t$ bị loại (Bài 10).

**Kiểm tra lại.** $\mathbb E[\widehat g]=\nabla_\theta J=(2;\,-2)$; trung bình mô phỏng $1{,}96$ với sai số chuẩn $27/\sqrt{400\,000}\approx0{,}04$ cách $2$ khoảng một sai số chuẩn. Lỗi thường gặp: nhân mọi $\psi_t$ với $G_0=-5$, được $-5\bigl(4\cdot\tfrac12-\tfrac12\bigr)=-7{,}5$ cho tọa độ đầu; tính $\psi$ của hành động 2 bằng $(0;\,1)$ mà quên trừ đặc trưng trung bình.
:::

## Tài liệu tham khảo

- Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. §6.7, Ví dụ 6.7, Hình 6.5, Bài tập 6.13 (Bài tập 09.11, 09.13, 09.18); §13.1–13.3, Ví dụ 13.1, Hình 13.1, Bài tập 13.1, 13.2, 13.3, 13.5 (Bài tập 09.12, 09.14–09.17, 09.19, 09.20).
- van Hasselt, H. "Double Q-learning." *Advances in Neural Information Processing Systems* 23, 2010 (Bài tập 09.13, 09.18).
- Williams, R. J. "Simple statistical gradient-following algorithms for connectionist reinforcement learning." *Machine Learning* 8 (1992): 229–256 (đơn vị Bernoulli–logistic và REINFORCE, Bài tập 09.16, 09.19).
- Ghi chú bài giảng Bài 09, Mục 2–6, cho mọi số hiệu Định nghĩa, Mệnh đề, Định lý, Thuật toán và Ví dụ dẫn trong tệp.
