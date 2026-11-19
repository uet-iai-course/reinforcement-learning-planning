# Bài 11 — Lập kế hoạch dựa trên mô hình

## Mục tiêu học tập

Sau chương này, người học có thể:

1. **Mô hình và tính bất định.** Phân biệt mô hình phân phối với mô hình mẫu, lập kế hoạch nền với lập kế hoạch tại thời điểm quyết định; ước lượng mô hình bằng tần suất từ dữ liệu, tách bất định ngẫu nhiên khỏi bất định nhận thức và tính độ lệch chuẩn của xác suất ước lượng.
2. **Dyna.** Thực hiện bằng tay một bước thật của Dyna-Q gồm cập nhật trực tiếp, cập nhật mô hình và các cập nhật lập kế hoạch; nêu điều kiện hội tụ của Q-planning; giải thích vì sao mô hình sai cần thưởng thăm dò.
3. **Cập nhật kỳ vọng và cập nhật mẫu.** So sánh hai loại cập nhật theo số phép tính và sai số khi ngân sách tính toán nhỏ hơn hệ số phân nhánh.
4. **Rollout và tìm kiếm theo cây.** Phát biểu tính chất cải thiện của thuật toán rollout cùng giả thiết; tính số mô phỏng đủ cho một xác suất chọn sai cho trước; tính chỉ số cận tin cậy trên; thực hiện một vòng tìm kiếm theo cây Monte Carlo (Monte Carlo tree search, MCTS) qua bốn pha.
5. **Tối ưu kế hoạch bằng đạo hàm.** Tính gradient của chi phí kế hoạch theo chuỗi hành động qua mô hình khả vi bằng truy hồi ngược; thực hiện một bước hạ gradient và một vòng phương pháp entropy chéo; mô tả điều khiển dự báo theo chân trời lùi và chặn sai số dự báo tích lũy.
6. **Tùy chọn.** Định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của một tùy chọn; viết phương trình Bellman bán-MDP; thực hiện lặp giá trị và một cập nhật Q-learning với tùy chọn.
7. **Chọn cách dùng mô hình.** Với một bài toán cụ thể, chọn cách dùng mô hình phù hợp và kiểm các giả thiết mà bảo đảm của cách đó cần.

<!-- note-topic-id: lec-11-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `01.k`, …, `10.k` chỉ khối trong ghi chú Bài 01–10; `11.k` chỉ ghi chú này. Công thức đánh số theo mục, như (2.1) là công thức thứ nhất của Mục 2.

- **Mô hình, lập kế hoạch, thăm dò** (Định nghĩa 01.14, 01.16). Mô hình cho dự báo $(\widehat S_{t+1},\widehat R_{t+1})$ hoặc phân phối của chúng khi biết trạng thái và hành động; lập kế hoạch là dùng mô hình để chọn hành động bằng cách xét trước diễn biến tương lai. Khi chọn lặp lại trong tập hữu hạn hành động, $N(a)$ là số lần đã chọn $a$, $\bar r(a)$ là trung bình mẫu phần thưởng của $a$; thăm dò là chọn hành động không tham lam theo $\bar r$.
- **MDP hữu hạn, động lực, giá trị** (Định nghĩa 03.4, 03.7, 03.9, 03.13; Mệnh đề 03.6, 03.22, 03.23; Bổ đề 03.20; Định lý 03.21, 03.28). $p(s',r\mid s,a)$ cho $p(s'\mid s,a)$, $r(s,a)$; $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$ và $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$. Với chính sách Markov dừng, phần tương lai khi biết lịch sử tới $S_t=s$ có cùng phân phối với quá trình xuất phát tại $s$; với $0\le\gamma<1$, $v_\pi$ là nghiệm duy nhất của phương trình Bellman kỳ vọng.
- **Toán tử Bellman và ánh xạ co** (Định nghĩa 04.1, 04.22; Bổ đề 04.23; Mệnh đề 04.4, 04.24; Định lý 04.5, 04.25). $\lvert\max_ax_a-\max_ay_a\rvert\le\max_a\lvert x_a-y_a\rvert$ trên tập chỉ số hữu hạn. Ánh xạ co hệ số $\beta<1$ theo chuẩn vô cùng có điểm bất động duy nhất $\bar V$ và $\lVert V_k-\bar V\rVert_\infty\le\beta^k\lVert V_0-\bar V\rVert_\infty$. Toán tử Bellman tối ưu là $(T_*V)(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]$, một ánh xạ co hệ số $\gamma$; $v_*$ là điểm bất động duy nhất của nó, $v_*(s)=\max_aq_*(s,a)$ và $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma\max_{a'}q_*(s',a')]$; chính sách tham lam theo $v_*$ tối ưu trên mọi chính sách, kể cả phụ thuộc lịch sử.
- **Cải thiện chính sách** (Định lý 04.13). Nếu $\pi$ Markov dừng có giá trị chính xác và $\pi'$ Markov dừng xác định thỏa $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$, thì $v_{\pi'}\ge v_\pi$, nghiêm ngặt tại $s$ khi điều kiện nghiêm ngặt tại $s$.
- **Lặp giá trị** (Thuật toán 04.28, 04.31; Định lý 04.32). Lặp giá trị cần mô hình phân phối đã biết; bản bất đồng bộ hội tụ về $v_*$ với lịch tùy ý khi mỗi trạng thái được cập nhật vô hạn lần.
- **Trung bình mẫu, mô hình thực nghiệm** (Định nghĩa 05.8; Mệnh đề 05.9, 05.34). $V_n=V_{n-1}+(g_n-V_{n-1})/n$; nghiệm TD theo lô là nghiệm của MDP thực nghiệm có $\hat r$, $\hat P$ là tần suất tính từ dữ liệu.
- **Q-learning và hội tụ** (Định nghĩa 06.3, 06.15, 06.19; Thuật toán 06.16; Nhận xét 06.20; Định lý 06.21). Chính sách $\varepsilon$-tham lam theo $Q$ chọn đều ngẫu nhiên một hành động với xác suất $\varepsilon$, còn lại chọn một hành động cực đại $Q(s,\cdot)$. Mục tiêu Q-learning là $R+\gamma\max_{a'}Q(S',a')$, bằng $R$ khi $S'$ kết thúc. Dưới các giả thiết nền (MDP hữu hạn, động lực dừng, phần thưởng bị chặn, $0\le\gamma<1$, mẫu có điều kiện theo lịch sử và cặp đang cập nhật có phân phối $p(\cdot,\cdot\mid s,a)$), khi mọi cặp được cập nhật vô hạn lần với chính sách hành vi tùy ý và bước học thỏa Robbins–Monro theo cặp, $Q_t\to q_*$ hầu chắc chắn.
- **Bất đẳng thức Hoeffding** (Mệnh đề 06.26; Hoeffding, 1963). Nếu $X_1,\dots,X_n$ độc lập và $X_i\in[a_i,b_i]$ hầu chắc chắn thì với mọi $t>0$
  $$\begin{aligned}&\Pr\Bigl\{\textstyle\sum_iX_i-\mathbb E\sum_iX_i\ge t\Bigr\}\\&\quad\le\exp\Bigl(-\frac{2t^2}{\sum_i(b_i-a_i)^2}\Bigr),\end{aligned}$$
  và cùng chặn cho biến cố $\le-t$; Mệnh đề 06.26 là dạng hai phía cho lợi tức cùng phân phối.
- **Bộ nhớ phát lại, hạ gradient** (Định nghĩa 08.7, 08.15, 08.16). Bộ nhớ phát lại giữ $N$ mẫu chuyển gần nhất và rút đều; hạ gradient với tốc độ học $\eta>0$ cập nhật $\theta\leftarrow\theta-\eta g$.
- **Đoạn thu, lợi tức $n$ bước** (Định nghĩa 10.11; Bài 10, Mục 3.3). Đoạn thu (rollout) của Bài 10 là một đoạn dữ liệu nhiều bước thu bằng chính sách hiện hành; lợi tức $n$ bước dùng $n$ phần thưởng thật rồi bootstrap.
- **Giải tích và xác suất.** Quy tắc dây chuyền; phương sai của trung bình các biến độc lập; bất đẳng thức hợp (union bound) $\Pr(\bigcup_iE_i)\le\sum_i\Pr(E_i)$; chuỗi hình học $\sum_{j\ge1}x^{j-1}=1/(1-x)$ với $\lvert x\rvert<1$.

## Bảng ký hiệu

Bảng gồm ký hiệu dùng xuyên suốt chương; mỗi chữ giữ một nghĩa trong cả chương, còn ký hiệu cục bộ được giới thiệu tại chỗ.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái không kết thúc; thêm trạng thái kết thúc | tập hữu hạn (Mục 1–3, 5) |
| $\mathcal A(s)$ | tập hành động hợp lệ tại $s$ | tập hữu hạn khác rỗng |
| $t$, $T$ | chỉ số bước; thời điểm kết thúc lượt | $\{0,1,\dots\}$; nguyên dương hoặc $\infty$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động, phần thưởng của chuyển từ $t$ sang $t+1$ | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathbb R$ |
| $p(s',r\mid s,a)$; $p(s'\mid s,a)$, $r(s,a)$ | động lực thật; xác suất chuyển, phần thưởng kỳ vọng | phân phối; $[0,1]$; $\mathbb R$ |
| $\hat p(s'\mid s,a)$, $\hat r(s,a)$ | mô hình học được (mô hình đếm ở Mục 2) | phân phối trên $\mathcal S^+$; $\mathbb R$ |
| $C(s,a)$, $C(s,a,s')$ | số lần thử thật cặp $(s,a)$; số lần trong đó đi tới $s'$ | $\{0,1,\dots\}$ |
| $\gamma$ | hệ số chiết khấu | $[0,1)$ |
| $\pi$, $\pi_0$ | chính sách; chính sách cơ sở của rollout | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $v_\pi$, $q_\pi$, $v_*$, $q_*$ | giá trị thật của $\pi$; giá trị tối ưu | hàm thực |
| $Q$ | bảng giá trị hành động đang học hoặc đang lập kế hoạch | $\mathbb R$ trên mỗi cặp hợp lệ |
| $\alpha$, $\varepsilon$ | bước học; tham số của chính sách $\varepsilon$-tham lam | $(0,1]$; $[0,1]$ |
| $n$ | số cập nhật lập kế hoạch sau mỗi bước thật | số nguyên không âm |
| $\kappa$, $\ell(s,a)$ | hệ số thưởng thăm dò; số bước thật kể từ lần thử gần nhất của $(s,a)$ | $\kappa>0$; $\{0,1,\dots\}$ |
| $b$ | hệ số phân nhánh: số trạng thái kế có xác suất dương | số nguyên dương |
| $m$ | số mô phỏng cho mỗi hành động của thuật toán rollout | số nguyên dương |
| $N(s)$, $N(s,a)$, $W(s,a)$, $\bar Q(s,a)$ | số lần thăm nút, cạnh trên cây; tổng lợi tức; trung bình $W/N$ | $\{0,1,\dots\}$; $\mathbb R$ |
| $c_{\mathrm{ucb}}$, $D$ | hằng số thăm dò của quy tắc cận tin cậy trên; độ sâu cắt của mô phỏng (rollout, tìm kiếm theo cây) | $c_{\mathrm{ucb}}>0$; nguyên dương, với rollout có thể $\infty$ |
| $x_t$, $u_t$; $f$, $\hat f$ | trạng thái, hành động liên tục của Mục 4; động lực thật, mô hình | $\mathbb R$; $\mathbb R\times\mathbb R\to\mathbb R$ |
| $h$, $c(x,u)$, $J$ | chân trời; chi phí mỗi bước; chi phí của một kế hoạch | nguyên dương; $\mathbb R_{\ge0}$; $\mathbb R^h\to\mathbb R$ |
| $\eta$; $\bar e$, $e_k$, $L$ | tốc độ học; chặn sai số một bước của mô hình, sai số dự báo $k$ bước, hằng số Lipschitz | dương; $\mathbb R_{\ge0}$; $L\ge0$ |
| $\omega$, $\Omega(s)$; $\mathcal I_\omega$, $\pi_\omega$, $\beta_\omega$ | tùy chọn, tập tùy chọn dùng được tại $s$; tập khởi đầu, chính sách, hàm kết thúc | $\mathcal I_\omega\subseteq\mathcal S$; $\beta_\omega:\mathcal S^+\to[0,1]$ |
| $\tau$; $r(s,\omega)$, $p(s'\mid s,\omega)$ | thời điểm kết thúc của tùy chọn; hai phần của mô hình tùy chọn | $\{1,2,\dots\}$; $\mathbb R$; $[0,\gamma]$ |
| $\mu$, $v_\mu$, $v_\Omega$ | chính sách phân cấp; giá trị của nó; giá trị tối ưu trên tập tùy chọn | phân phối trên $\Omega(s)$; hàm thực |

Quy ước đọc bảng gồm các điểm sau.

- $R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$; giá trị của trạng thái kết thúc bằng $0$ trong hàm thật, bảng và mô hình.
- $\mathbb E_\pi$ lấy theo $\pi$ và động lực thật; bất đẳng thức giữa hai hàm hiểu theo từng trạng thái.
- $k$ và $j$ là chỉ số cục bộ, nghĩa nêu tại chỗ.
- Tên ô viết chữ đứng ($\mathrm A$, …, $\mathrm Z$), hành động viết bằng mũi tên. Dấu thập phân là dấu phẩy; tọa độ ngăn bằng dấu chấm phẩy, như $(-0{,}8;\,-0{,}4)$.
- Tương ứng với Sutton và Barto (2018): $c$ của (2.10) viết là $c_{\mathrm{ucb}}$, $\tau$ của Dyna-Q+ viết là $\ell(s,a)$. Sách viết tùy chọn là $\langle\pi_\omega,\gamma_\omega\rangle$ và gọi $\gamma_\omega$ là hàm kết thúc; tùy chọn kết thúc với xác suất $1-\gamma_\omega$, nên $\beta_\omega=1-\gamma_\omega$. Sách viết chính sách phân cấp là $\pi$; chương viết $\mu$ như Sutton, Precup và Singh (1999).
- Tương ứng với giáo trình *Học máy thống kê*: $v_\pi$ là $V^\pi$, $p(s'\mid s,a)$ là $T(s,a,s')$.

---

## 1. Bài toán lập kế hoạch với mô hình học được

<!-- note-topic-id: lec-11-topic-02 -->
### 1.1 Kết quả kế thừa và bài toán trung tâm

Q-learning dạng bảng hội tụ hầu chắc chắn tới $q_*$ khi mọi cặp được cập nhật vô hạn lần và bước học thỏa Định nghĩa 06.19, dưới các giả thiết nền của Nhận xét 06.20 (Định lý 06.21). Mỗi mẫu chuyển thật đi vào đúng một cập nhật rồi bị bỏ. Lặp giá trị bất đồng bộ thì không cần bước thật nào: khi biết mô hình và mỗi trạng thái được cập nhật vô hạn lần, nó hội tụ tới $v_*$ với lịch tùy ý (Định lý 04.32). Ví dụ sau là môi trường xuyên suốt của chương.

::: example Ví dụ 11.1 (Mê cung hai phòng)
**Bố cục.** Tám ô xếp hai hàng: hàng trên $\mathrm A$, $\mathrm B$, $\mathrm C$, $\mathrm D$; hàng dưới $\mathrm E$, $\mathrm F$, $\mathrm K$, $\mathrm Z$. Tường ngăn $\mathrm B$ với $\mathrm C$; cạnh $\mathrm F$–$\mathrm K$ là cửa giữa phòng trái $\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$ và phòng phải $\{\mathrm C,\mathrm D,\mathrm K\}$ cùng ô đích $\mathrm Z$, là trạng thái kết thúc. Lượt bắt đầu ở $\mathrm A$.

**Động lực.** Tại mọi ô không kết thúc, $\mathcal A(s)=\{\uparrow,\downarrow,\leftarrow,\rightarrow\}$. Với xác suất $0{,}8$ tác tử sang ô kề theo hướng đã chọn; nếu hướng đó đụng tường hoặc biên thì tác tử ở yên. Với xác suất $0{,}2$ tác tử trượt và ở yên. Phần thưởng bằng $+1$ cho chuyển vào $\mathrm Z$ và $0$ cho mọi chuyển khác; $\gamma=0{,}9$.

**Giá trị tối ưu.** Gọi $d(s)$ là số bước đi đúng tối thiểu từ $s$ tới $\mathrm Z$: $d=1$ tại $\mathrm K$, $\mathrm D$; $d=2$ tại $\mathrm F$, $\mathrm C$; $d=3$ tại $\mathrm B$, $\mathrm E$; $d=4$ tại $\mathrm A$. Đi theo đường ngắn nhất, một ô ở khoảng cách $d$ có giá trị $v(d)$ thỏa
$$\begin{aligned}v(1)&=0{,}8+0{,}18\,v(1),\\v(d)&=0{,}72\,v(d-1)\\&\quad+0{,}18\,v(d),\quad d\ge2,\end{aligned}$$
với $0{,}18=0{,}2\gamma$ (trượt) và $0{,}72=0{,}8\gamma$ (đi đúng), nên $v(1)=0{,}8/0{,}82$ và $v(d)=(0{,}72/0{,}82)\,v(d-1)$:

| $s$ | $\mathrm K$, $\mathrm D$ | $\mathrm F$, $\mathrm C$ | $\mathrm B$, $\mathrm E$ | $\mathrm A$ |
|---|---:|---:|---:|---:|
| $v_*(s)$ | $0{,}9756$ | $0{,}8566$ | $0{,}7522$ | $0{,}6604$ |

**Kiểm tra lại.** Phương trình Bellman tối ưu tại $\mathrm F$ (Định lý 04.25(c)) cho bốn giá trị hành động:

- $q_*(\mathrm F,\rightarrow)=0{,}72\cdot0{,}975610+0{,}18\cdot0{,}856633=0{,}856633$;
- $q_*(\mathrm F,\downarrow)=0{,}9\cdot0{,}856633=0{,}770970$, vì $\downarrow$ đụng biên;
- $q_*(\mathrm F,\uparrow)=q_*(\mathrm F,\leftarrow)=0{,}72\cdot0{,}752166+0{,}18\cdot0{,}856633=0{,}695753$.

Cực đại đạt tại $\rightarrow$ và bằng $v_*(\mathrm F)$; các ô khác kiểm tương tự.
:::

![Lưới hai hàng: A, B, C, D trên; E, F, K, Z dưới. Tường giữa B và C, cửa giữa F và K, Z là đích. Giá trị tối ưu: K, D 0,9756; F, C 0,8566; B, E 0,7522; A 0,6604; đi đúng 0,8, trượt 0,2.](img/lec-11/me-cung-hai-phong.svg)

Trên hình, giá trị giảm theo khoảng cách tới $\mathrm Z$, mỗi bước nhân $0{,}72/0{,}82=0{,}8780$; hai ô cùng khoảng cách có cùng giá trị.

Giả sử lượt thật thứ nhất gồm năm mẫu chuyển $(S,A,R,S')$:

1. $(\mathrm A,\rightarrow,0,\mathrm A)$, một lần trượt;
2. $(\mathrm A,\rightarrow,0,\mathrm B)$;
3. $(\mathrm B,\downarrow,0,\mathrm F)$;
4. $(\mathrm F,\rightarrow,0,\mathrm K)$;
5. $(\mathrm K,\rightarrow,+1,\mathrm Z)$.

Q-learning với bảng khởi tạo $Q\equiv0$, $\alpha=0{,}5$, $\gamma=0{,}9$ có mục tiêu bằng $0$ ở bốn bước đầu, vì mọi phần thưởng bằng $0$ và mọi giá trị kế bằng $0$. Ở bước thứ năm, mục tiêu là $1$ vì $\mathrm Z$ kết thúc, nên $Q(\mathrm K,\rightarrow)=0+0{,}5\cdot1=0{,}5$. Bốn mẫu chuyển còn lại đã cho biết "$\mathrm F$ dẫn tới $\mathrm K$", "$\mathrm B$ dẫn tới $\mathrm F$", nhưng Q-learning không dùng lại chúng; giá trị của $\mathrm K$ chỉ lan về $\mathrm F$ khi tác tử đi qua $\mathrm F$ ở một lượt sau.

Trên mê cung Dyna của Sutton và Barto (2018, Ví dụ 8.1, tr. 164), tác tử không lập kế hoạch cần khoảng 25 lượt để gần tối ưu. Tác tử làm 50 cập nhật lập kế hoạch sau mỗi bước thật chỉ cần khoảng 3 lượt. Mô hình học từ các mẫu đã thu thì sai ở nhiều chỗ: sau lượt thứ nhất, $(\mathrm A,\rightarrow)$ mới được thử hai lần, một lần trượt, nên tần suất tới $\mathrm B$ là $0{,}5$ thay vì $0{,}8$; các cặp tại $\mathrm C$ chưa được thử.

**Bài toán trung tâm của chương.** Tác tử đi ít bước thật và học mô hình từ các bước đó. Sau mỗi bước thật, tác tử cập nhật giá trị hoặc chạy mô phỏng trên mô hình. Dùng mô hình thế nào để chọn hành động tốt hơn Q-learning (Bài 06) sau cùng số bước thật? Khi mô hình sai, kết quả nào còn đúng?

<!-- note-topic-id: lec-11-topic-03 -->
### 1.2 Ba cách dùng mô hình

Về mặt ý tưởng, Dyna-Q, tìm kiếm theo cây và lập kế hoạch với tùy chọn có chung cấu trúc "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách" (Sutton và Barto, 2018, §8.1, tr. 160). Tối ưu kế hoạch bằng đạo hàm bỏ khâu giá trị và tối ưu trực tiếp chuỗi hành động trên kinh nghiệm mô phỏng. Các phương pháp khác nhau ở hai điểm: lúc nào gọi mô hình, và giá trị tính ra dùng cho trạng thái nào:

- **Cập nhật bảng giá trị cho nhiều trạng thái trong lúc hành động.** Giữa hai bước thật, tác tử áp quy tắc Q-learning lên mẫu từ mô hình.
- **Tìm kiếm từ trạng thái hiện tại lúc ra quyết định.** Đứng ở $S_t$, tác tử thử trước các diễn biến bắt đầu từ $S_t$ rồi chọn $A_t$: dựng cây khi hành động rời rạc, tối ưu chuỗi hành động bằng đạo hàm khi hành động liên tục.
- **Gộp nhiều bước thành tùy chọn.** Một tùy chọn như "đi tới cửa" là chính sách con chạy nhiều bước; lập kế hoạch trên tùy chọn làm giá trị lan qua mê cung trong ít vòng lặp hơn.

![Dòng mô hình, kinh nghiệm mô phỏng, cập nhật, giá trị, chính sách; vòng trên là kinh nghiệm thật cho học mô hình và, qua học trực tiếp, cho giá trị. Bốn khối dưới: hành động liên tục (gradient, entropy chéo, điều khiển dự báo) nối thẳng từ kinh nghiệm mô phỏng, không qua giá trị; hành động rời rạc (rollout, tìm kiếm theo cây); lập kế hoạch nền (Dyna-Q); tùy chọn. Hai khối đầu là lập kế hoạch tại thời điểm quyết định.](img/lec-11/cau-truc-chuong.svg)

Hình đọc từ trái sang phải theo dòng "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách". Vòng phía trên lấy ý từ sơ đồ ở Sutton và Barto (2018, tr. 162): kinh nghiệm thật vừa cập nhật giá trị, vừa cải thiện mô hình. Bốn khối phía dưới thể hiện ba cách dùng mô hình; cách tìm kiếm lúc ra quyết định chiếm hai khối bên trái, chia theo loại hành động. Khối hành động liên tục nối thẳng từ kinh nghiệm mô phỏng, vì tối ưu kế hoạch không đi qua bảng giá trị.

Như vậy, Q-learning bỏ phí bốn trong năm mẫu chuyển của lượt thứ nhất, và Định lý 06.21 chỉ bảo đảm hội tụ khi số bước thật tiến ra vô hạn. Muốn dùng lại các mẫu đã có, chúng ta cần biết mô hình là gì, ước lượng nó từ dữ liệu ra sao, và nó sai đến đâu sau hữu hạn lần thử.

---

## 2. Tính bất định của môi trường và lập kế hoạch nền

<!-- note-topic-id: lec-11-topic-04 -->
### 2.1 Mô hình phân phối và mô hình mẫu

Trên mê cung hai phòng, $(\mathrm F,\rightarrow)$ sang $\mathrm K$ với xác suất $0{,}8$ hoặc ở yên với xác suất $0{,}2$. Muốn cập nhật $Q(\mathrm F,\rightarrow)$ mà không đi thêm bước thật, tác tử hỏi mô hình, và mô hình có thể trả cả bảng xác suất hoặc chỉ một kết cục rút theo bảng đó.

Một cách trực quan, với mười hai con xúc xắc, một mô hình liệt kê mọi tổng cùng xác suất của chúng, mô hình kia chỉ tung thử và báo một tổng (Sutton và Barto, 2018, §8.1, tr. 159). Để làm rõ trên mê cung, xem ví dụ sau.

::: example Ví dụ 11.2 (Mô hình phân phối và mô hình mẫu của $(\mathrm F,\rightarrow)$)
**Dữ kiện.** Mê cung hai phòng (Ví dụ 11.1): tại $\mathrm F$, hành động $\rightarrow$ sang $\mathrm K$ với xác suất $0{,}8$, ở yên với xác suất $0{,}2$, phần thưởng $0$; $\gamma=0{,}9$. Bảng sau lượt thứ nhất: $\max_aQ(\mathrm K,a)=0{,}5$, $\max_aQ(\mathrm F,a)=0$.

**Mô hình phân phối.** Mô hình trả $\{\mathrm K:0{,}8;\ \mathrm F:0{,}2\}$ với phần thưởng $0$. Mục tiêu kỳ vọng là
$$0{,}9\,(0{,}8\cdot0{,}5+0{,}2\cdot0)=0{,}36.$$

**Mô hình mẫu.** Mô hình trả một trạng thái kế rút theo các xác suất trên: mẫu $\mathrm K$ cho mục tiêu $0{,}45$, mẫu $\mathrm F$ cho $0$.

**Kiểm tra lại.** Trung bình của mục tiêu mẫu là $0{,}8\cdot0{,}45+0{,}2\cdot0=0{,}36$, bằng mục tiêu kỳ vọng.
:::

::: definition Định nghĩa 11.1 (Mô hình phân phối, mô hình mẫu, kinh nghiệm mô phỏng)
Cho một MDP với tập trạng thái $\mathcal S^+$ và tập hành động $\mathcal A(s)$.

- **Mô hình phân phối** (distribution model) là một hàm gán cho mỗi cặp hợp lệ $(s,a)$ một phân phối $\hat p(\cdot,\cdot\mid s,a)$ trên các cặp (trạng thái kế, phần thưởng).
- **Mô hình mẫu** (sample model) là một thủ tục nhận $(s,a)$ và trả một cặp $(R,S')$ rút ngẫu nhiên theo một phân phối $\hat p(\cdot,\cdot\mid s,a)$ nào đó, độc lập với các lần gọi trước.
- **Kinh nghiệm mô phỏng** (simulated experience) là dãy mẫu chuyển $(s,a,R,S')$ sinh từ mô hình, phân biệt với kinh nghiệm thật sinh từ môi trường.
:::

Mô hình phân phối và mô hình mẫu là hai cách hiện thực mô hình của Định nghĩa 01.14. Từ mô hình phân phối luôn rút được mẫu, nên mọi mô hình phân phối cho một mô hình mẫu. Mô hình mẫu dễ xây dựng hơn, ví dụ một trình mô phỏng (Sutton và Barto, 2018, tr. 160). Mô hình tất định thuộc cả hai loại. Nhầm lẫn thường gặp là đồng nhất mô hình với môi trường: $\hat p$ có thể khác $p$.

::: definition Định nghĩa 11.2 (Lập kế hoạch nền, lập kế hoạch tại thời điểm quyết định)
**Lập kế hoạch trong không gian trạng thái** (state-space planning) là một thủ tục nhận một mô hình và trả hoặc cải thiện một chính sách, bằng các cập nhật giá trị trên kinh nghiệm mô phỏng.

- **Lập kế hoạch nền** (background planning) cải thiện một bảng giá trị hoặc chính sách cho nhiều trạng thái trước khi tác tử gặp chúng.
- **Lập kế hoạch tại thời điểm quyết định** (decision-time planning) bắt đầu sau khi quan sát $S_t$ và kết thúc khi chọn xong $A_t$; đầu ra là $A_t$.
:::

Hai cách khác nhau ở trạng thái mà phép tính hướng tới (Sutton và Barto, 2018, §8.8, tr. 180–181): lập kế hoạch nền chia phép tính cho mọi trạng thái nó cập nhật; lập kế hoạch tại thời điểm quyết định dồn phép tính vào trạng thái hiện tại, phù hợp khi có thời gian suy nghĩ trước mỗi bước. Trên mê cung, cập nhật $Q(\mathrm F,\rightarrow)$ khi đứng ở $\mathrm A$ là lập kế hoạch nền; thử trước các hành động khi đứng ở $\mathrm F$ là loại thứ hai.

::: remark Nhận xét 11.3 (Quy hoạch động là lập kế hoạch nền với mô hình phân phối)
Thuật toán 04.28 và 04.31 dùng mô hình phân phối đã biết để cập nhật mọi trạng thái trước khi tác tử gặp chúng, nên quy hoạch động là lập kế hoạch nền. Ở chương này, $\hat p$ được học từ ít mẫu thật và có sai số.
:::

<!-- note-topic-id: lec-11-topic-05 -->
### 2.2 Mô hình đếm và hai loại bất định

Sau lượt thứ nhất trên mê cung, $(\mathrm A,\rightarrow)$ đã được thử hai lần: một lần sang $\mathrm B$, một lần trượt. Tần suất cho ước lượng $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$, trong khi xác suất thật là $0{,}8$.

Một cách trực quan, có hai nguồn bất định: việc trượt là thuộc tính của môi trường, còn sai lệch giữa $\hat p$ và $p$ do ít dữ liệu và thu hẹp khi số lần thử tăng.

Sutton và Barto (2018, §8.3, tr. 166) nêu ba nguyên nhân làm mô hình sai:

- môi trường ngẫu nhiên và chỉ có ít mẫu;
- xấp xỉ hàm chưa tốt;
- môi trường thay đổi.

Bảng đếm sau lượt thứ nhất thuộc nguyên nhân thứ nhất.

::: example Ví dụ 11.3 (Bảng đếm sau lượt thứ nhất)
**Dữ kiện.** Lượt thật thứ nhất trên mê cung hai phòng (Ví dụ 11.1): $(\mathrm A,\rightarrow,0,\mathrm A)$, $(\mathrm A,\rightarrow,0,\mathrm B)$, $(\mathrm B,\downarrow,0,\mathrm F)$, $(\mathrm F,\rightarrow,0,\mathrm K)$, $(\mathrm K,\rightarrow,+1,\mathrm Z)$.

**Đếm.** $C(\mathrm A,\rightarrow)=2$ với $C(\mathrm A,\rightarrow,\mathrm A)=C(\mathrm A,\rightarrow,\mathrm B)=1$; ba cặp $(\mathrm B,\downarrow)$, $(\mathrm F,\rightarrow)$, $(\mathrm K,\rightarrow)$ mỗi cặp có một lần thử; mọi cặp khác có $C=0$.

**Tần suất.** $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=\hat p(\mathrm A\mid\mathrm A,\rightarrow)=1/2$; $\hat p(\mathrm F\mid\mathrm B,\downarrow)=\hat p(\mathrm K\mid\mathrm F,\rightarrow)=\hat p(\mathrm Z\mid\mathrm K,\rightarrow)=1$, và $\hat r(\mathrm K,\rightarrow)=1$. Với các cặp có $C=0$, tần suất chưa xác định.

**Kiểm tra lại.** $2+1+1+1=5$ lần thử, bằng số mẫu của lượt.
:::

::: definition Định nghĩa 11.4 (Mô hình đếm)
Cho các mẫu chuyển thật đã thu. Với mỗi cặp hợp lệ $(s,a)$ có $C(s,a)\ge1$, **mô hình đếm** (count-based model, còn gọi là maximum-likelihood model) là
$$\begin{aligned}\hat p(s'\mid s,a)&=\frac{C(s,a,s')}{C(s,a)},\\\hat r(s,a)&=\frac{1}{C(s,a)}\\&\quad\times\sum_{i=1}^{C(s,a)}R^{(i)}(s,a),\end{aligned}\tag{2.1}$$
trong đó $C(s,a)$ là số lần thử $(s,a)$, $C(s,a,s')$ là số lần trong đó trạng thái kế là $s'\in\mathcal S^+$, và $R^{(1)}(s,a),\dots$ là các phần thưởng đã nhận. Với cặp có $C(s,a)=0$, mô hình chưa xác định.
:::

Mô hình đếm thay xác suất chuyển bằng tần suất, như Sutton và Barto (2018, §8.4, tr. 170) dùng cho môi trường ngẫu nhiên; đó là phép tính của MDP thực nghiệm ở Mệnh đề 05.34, đếm theo cặp thay vì theo trạng thái. Mô hình đếm là mô hình phân phối; rút một mẫu theo nó tương đương rút đều một lần thử cũ của cặp.

**Câu hỏi.** Tần suất $\hat p$ dao động quanh $p$ đến mức nào khi $C(s,a)$ nhỏ? Mệnh đề sau trả lời bằng phương sai.

::: proposition Mệnh đề 11.5 (Kỳ vọng và phương sai của xác suất ước lượng)
**Giả thiết.** Cặp $(s,a)$ được thử $C=C(s,a)\ge1$ lần, với $C$ cố định trước khi thử. Các trạng thái kế $S'_1,\dots,S'_C$ độc lập và cùng phân phối $p(\cdot\mid s,a)$, tức môi trường dừng và có tính Markov. Cố định $s'\in\mathcal S^+$ và đặt $p=p(s'\mid s,a)$.

**Kết luận.** Với $\hat p=C(s,a,s')/C$,
$$\mathbb E\,\hat p=p,\qquad \operatorname{Var}\hat p=\frac{p(1-p)}C.\tag{2.2}$$

**Điều kiện áp dụng.** Số lần thử $C$ không phụ thuộc kết quả của các lần thử.

**Phạm vi.** Mệnh đề cho kỳ vọng và phương sai của xác suất ước lượng $\hat p(s'\mid s,a)$ tại một cặp $(s,a)$. Nó không chặn sai số của các giá trị $Q$ mà lập kế hoạch tính trên mô hình.
:::

::: proof
**Bước 1 (tổng các biến Bernoulli).** Đặt $Y_i=\mathbb 1\{S'_i=s'\}$. Theo giả thiết, $Y_1,\dots,Y_C$ độc lập, mỗi biến nhận giá trị $1$ với xác suất $p$, nên $\mathbb EY_i=p$ và $\operatorname{Var}Y_i=p-p^2=p(1-p)$. Ta có $C(s,a,s')=\sum_iY_i$.

**Bước 2 (kỳ vọng).** Do tính tuyến tính của kỳ vọng và các $Y_i$ cùng phân phối, $\mathbb E\hat p=\frac1C\sum_i\mathbb EY_i=p$.

**Bước 3 (phương sai).** Do các $Y_i$ độc lập và $C$ cố định, phương sai của tổng bằng tổng các phương sai, nên
$$\begin{aligned}\operatorname{Var}\hat p&=\frac1{C^2}\sum_{i=1}^C\operatorname{Var}Y_i\\&=\frac{p(1-p)}C.\qquad\square\end{aligned}$$
:::

Ước lượng không chệch, với độ lệch chuẩn $\sqrt{p(1-p)/C}$ giảm theo $1/\sqrt C$. Mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "cùng phân phối": nếu xác suất trượt đổi giữa chừng, $\hat p$ trộn hai xác suất khác nhau.
- Bỏ "$C$ cố định trước": giả sử tác tử thử $(\mathrm A,\rightarrow)$ tới lần trượt đầu tiên rồi dừng. Mọi lần trước lần trượt đó đều tới $\mathrm B$, nên ước lượng lúc dừng là $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=(C-1)/C$, với $\Pr\{C=k\}=0{,}8^{k-1}\cdot0{,}2$. Dùng chuỗi $\sum_{k\ge1}x^k/k=-\ln(1-x)$ với $x=0{,}8$, ta được $\mathbb E[1/C]=\tfrac{0{,}2}{0{,}8}\ln5=0{,}4024$, nên $\mathbb E\hat p=1-\tfrac14\ln5=0{,}5976$, khác $p=0{,}8$.

Bước 2 của chứng minh dùng tính cùng phân phối; Bước 3 dùng tính độc lập và $C$ cố định.

::: example Ví dụ 11.4 (Hai loại bất định trên $(\mathrm F,\rightarrow)$)
**Dữ kiện.** Tại $(\mathrm F,\rightarrow)$ của mê cung hai phòng, xác suất thật sang $\mathrm K$ là $p=0{,}8$. Giả sử sau bốn lượt nữa, $C(\mathrm F,\rightarrow)=5$ với $4$ lần tới $\mathrm K$.

**Ước lượng.** $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=4/5=0{,}8$.

**Độ lệch chuẩn của ước lượng.** Theo (2.2), $\sqrt{0{,}16/C}$ với $p(1-p)=0{,}16$:

| $C(\mathrm F,\rightarrow)$ | $2$ | $5$ | $50$ |
|---|---:|---:|---:|
| $\sqrt{0{,}16/C}$ | $0{,}2828$ | $0{,}1789$ | $0{,}0566$ |

**Diễn giải.** Phương sai của một lần thử, $p(1-p)=0{,}16$, không đổi theo $C$. Độ lệch chuẩn của ước lượng giảm từ $0{,}2828$ xuống $0{,}0566$.

**Kiểm tra lại.** $0{,}16/2=0{,}08$ và $\sqrt{0{,}08}=0{,}2828$.
:::

::: definition Định nghĩa 11.6 (Bất định ngẫu nhiên, bất định nhận thức)
Xét một cặp $(s,a)$ với $C=C(s,a)$ lần thử và mô hình đếm của Định nghĩa 11.4.

- **Bất định ngẫu nhiên** (aleatoric uncertainty) của trạng thái kế là độ phân tán của một lần chuyển thật, đo bằng $p(s'\mid s,a)\bigl(1-p(s'\mid s,a)\bigr)$ với mỗi $s'$; nó không phụ thuộc $C$.
- **Bất định nhận thức** (epistemic uncertainty) là độ phân tán của ước lượng mô hình quanh giá trị thật, đo bằng $\operatorname{Var}\hat p(s'\mid s,a)=p(s'\mid s,a)\bigl(1-p(s'\mid s,a)\bigr)/C$ với mỗi $s'$; với cặp chưa thử ($C=0$), bất định nhận thức là toàn bộ sự không biết về $p(\cdot\mid s,a)$.
:::

Hai đại lượng cùng xuất hiện trong (2.2): bất định ngẫu nhiên là tử số $p(1-p)$, bất định nhận thức là $\operatorname{Var}\hat p=p(1-p)/C$. Chua và cộng sự (2018, §4) mô tả bất định ngẫu nhiên là phần vốn có của hệ, bất định nhận thức là phần do thiếu dữ liệu, mất đi khi dữ liệu vô hạn. Môi trường tất định không có bất định ngẫu nhiên nhưng vẫn có bất định nhận thức ở mọi cặp chưa thử. Nhầm lẫn thường gặp là coi $\hat p(\mathrm F\mid\mathrm B,\downarrow)=1$ sau một lần thử là chắc chắn. Với $C=1$, độ lệch chuẩn của $\hat p$ bằng $0{,}4$ khi $p=0{,}8$.

**Trong thực hành.** Bảng đếm chỉ dùng được với ít trạng thái và hành động rời rạc. Khi mô hình là một mạng nơ-ron, công thức (2.2) không áp dụng được, và bất định nhận thức phải đo bằng cách khác.

<!-- note-topic-id: lec-11-topic-06 -->
### 2.3 Tập mô hình

Một cách đo bất định nhận thức không cần công thức là huấn luyện nhiều mô hình trên các tập dữ liệu khác nhau một chút và xem các dự báo phân tán đến đâu, như ví dụ sau.

::: example Ví dụ 11.5 (Tập ba mô hình tại $(\mathrm A,\rightarrow)$)
**Dữ kiện.** Sau lượt thứ nhất (Ví dụ 11.3), dữ liệu của $(\mathrm A,\rightarrow)$ gồm hai trạng thái kế $\{\mathrm A,\mathrm B\}$; dữ liệu của $(\mathrm B,\downarrow)$ gồm một trạng thái kế $\{\mathrm F\}$.

**Ba mô hình.** Giả sử ba lần lấy lại mẫu có hoàn lại (bootstrap resampling) cỡ $2$ từ $\{\mathrm A,\mathrm B\}$ cho $\{\mathrm A,\mathrm A\}$, $\{\mathrm A,\mathrm B\}$, $\{\mathrm B,\mathrm B\}$. Ba mô hình đếm tương ứng cho $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0$; $0{,}5$; $1$.

**Độ phân tán.** Trung bình là $0{,}5$; độ lệch chuẩn không hiệu chỉnh (chia cho số mô hình) của ba dự báo là $\sqrt{(0{,}25+0+0{,}25)/3}=0{,}4082$.

**Cặp một mẫu.** Với $(\mathrm B,\downarrow)$, mọi lần lấy lại mẫu từ $\{\mathrm F\}$ đều cho $\{\mathrm F\}$, nên ba mô hình cùng cho $\hat p(\mathrm F\mid\mathrm B,\downarrow)=1$ và độ phân tán bằng $0$.

**Kiểm tra lại.** $\sqrt{1/6}=0{,}4082$.
:::

::: remark Nhận xét 11.7 (Tập mô hình)
Một **tập mô hình** (ensemble of models, model ensemble) gồm nhiều mô hình, mỗi mô hình học trên một tập dữ liệu lấy lại mẫu có hoàn lại từ dữ liệu thật. Độ phân tán giữa các dự báo đo bất định nhận thức: gần vùng có dữ liệu các mô hình dự báo gần nhau, xa vùng đó chúng tách xa nhau (Chua và cộng sự, 2018, §4 và chú thích Hình 1). Ở cặp chỉ có một mẫu, tập mô hình báo độ phân tán $0$ (Ví dụ 11.5), trong khi $\operatorname{Var}\hat p=0{,}16$ khi $p=0{,}8$.
:::

<!-- note-topic-id: lec-11-topic-07 -->
### 2.4 Q-planning và kiến trúc Dyna

Sau lượt thứ nhất, bảng Q-learning chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$, trong khi mô hình đếm của Ví dụ 11.3 đã biết $(\mathrm F,\rightarrow)$ dẫn tới $\mathrm K$. Muốn giá trị của $\mathrm K$ lan về $\mathrm F$ ngay, tác tử phải cập nhật $(\mathrm F,\rightarrow)$ mà không đi lại qua $\mathrm F$.

Về mặt ý tưởng, quy tắc của Q-learning chỉ cần một mẫu $(s,a,R,S')$, không hỏi mẫu đến từ đâu; áp nó lên mẫu do mô hình sinh, ta được một phương pháp lập kế hoạch.

::: example Ví dụ 11.6 (Một cập nhật Q-planning)
**Dữ kiện.** Bảng sau lượt thứ nhất: $Q\equiv0$ trừ $Q(\mathrm K,\rightarrow)=0{,}5$; $\alpha=0{,}5$, $\gamma=0{,}9$. Cặp được chọn là $(\mathrm F,\rightarrow)$; mô hình mẫu trả $(R,S')=(0,\mathrm K)$.

**Cập nhật.**

- mục tiêu: $0+0{,}9\cdot\max_aQ(\mathrm K,a)=0{,}9\cdot0{,}5=0{,}45$;
- sai lệch: $0{,}45-Q(\mathrm F,\rightarrow)=0{,}45$;
- giá trị mới: $Q(\mathrm F,\rightarrow)=0+0{,}5\cdot0{,}45=0{,}225$.

**Kiểm tra lại.** Với $\alpha=0{,}5$, giá trị mới là trung bình của $Q$ cũ và mục tiêu: $(0+0{,}45)/2=0{,}225$.
:::

::: algorithm Thuật toán 11.8 (Q-planning một bước, chọn ngẫu nhiên, dạng bảng)
**Đầu vào.** Mô hình mẫu xác định ở mọi cặp hợp lệ; $\gamma\in[0,1)$.

**Đầu ra.** Bảng $Q$.

**Giả thiết.** Hữu hạn cặp hợp lệ; mô hình không đổi.

**Khởi tạo.** $Q(s,a)$ tùy ý với mọi cặp hợp lệ; $Q=0$ tại trạng thái kết thúc.

**Tham số.** Lịch bước học $\alpha$; ngân sách số cập nhật.

**Lặp:**

1. Chọn ngẫu nhiên một cặp hợp lệ $(S,A)$ trong mọi cặp hợp lệ.
2. Gọi mô hình mẫu với $(S,A)$, nhận $(R,S')$.
3. $Q(S,A)\leftarrow Q(S,A)+\alpha\bigl[R+\gamma\max_{a'}Q(S',a')-Q(S,A)\bigr]$.

**Điều kiện dừng.** Hết ngân sách cập nhật.

**Chi phí mỗi bước.** Một lần gọi mô hình và $O(\max_s\lvert\mathcal A(s)\rvert)$ phép so sánh cho $\max_{a'}$.
:::

Thuật toán 11.8 là hộp Q-planning của Sutton và Barto (2018, §8.1, tr. 161). Ví dụ 11.6 là một lần chạy bước 1–3 tại một cặp đã có mẫu; trên cặp chưa thử, mô hình đếm chưa xác định, nên Thuật toán 11.8 cần mô hình cho sẵn ở mọi cặp. Gọi MDP có động lực $\hat p$ là MDP của mô hình, và $\hat q_*$ là giá trị hành động tối ưu của nó.

::: proposition Mệnh đề 11.9 (Hội tụ của Q-planning)
**Giả thiết.** Mô hình mẫu cố định, xác định ở mọi cặp hợp lệ, với phân phối $\hat p(\cdot,\cdot\mid s,a)$ có phần thưởng bị chặn; $0\le\gamma<1$; mỗi cặp hợp lệ được chọn ở bước 1 vô hạn lần, hầu chắc chắn; bước học của mỗi cặp thỏa điều kiện Robbins–Monro theo cặp (Định nghĩa 06.19).

**Kết luận.** Với mọi cặp hợp lệ, $Q(s,a)\to\hat q_*(s,a)$ hầu chắc chắn, trong đó $\hat q_*$ là giá trị hành động tối ưu của MDP của mô hình.

**Điều kiện áp dụng.** Mô hình không đổi trong lúc lập kế hoạch.

**Phạm vi.** Khi $\hat p\ne p$, giới hạn $\hat q_*$ khác $q_*$. Mệnh đề không chặn khoảng cách đó.
:::

::: proof
**Bước 1 (giả thiết nền).** MDP của mô hình là MDP hữu hạn, có động lực dừng vì mô hình cố định, phần thưởng bị chặn và $0\le\gamma<1$: đó là giả thiết nền của Nhận xét 06.20.

**Bước 2 (phân phối của mẫu).** Mô hình mẫu trả $(R,S')$ theo $\hat p(\cdot,\cdot\mid S,A)$, độc lập với các lần gọi trước, nên có điều kiện theo lịch sử và cặp đang cập nhật, mẫu có phân phối $\hat p(\cdot,\cdot\mid S,A)$.

**Bước 3 (Định lý 06.21).** Bước 3 của thuật toán là quy tắc của Thuật toán 06.16. Định lý 06.21 phát biểu cho cập nhật dọc quỹ đạo với chính sách hành vi tùy ý, còn ở đây cặp được rút ngẫu nhiên. Giả thiết nền về mẫu của Nhận xét 06.20 chỉ đòi phân phối của mẫu khi biết lịch sử và cặp đang cập nhật, và chứng minh của Định lý 06.21 (Bertsekas và Tsitsiklis, 1996, §5.6) không dùng việc các cặp nối thành quỹ đạo. Vì vậy kết luận giữ nguyên khi cặp được chọn ngẫu nhiên, độc lập với các mẫu, miễn mọi cặp được cập nhật vô hạn lần và bước học thỏa Định nghĩa 06.19. Theo Bước 1, 2 và giả thiết, $Q\to\hat q_*$ hầu chắc chắn. $\square$
:::

Mệnh đề là Định lý 06.21 áp cho MDP của mô hình; Sutton và Barto (2018, tr. 161) nêu cùng nhận định bằng lời. Hai giả thiết về mô hình có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "mô hình xác định ở mọi cặp": nếu mô hình chưa xác định tại $(\mathrm C,\cdot)$, $Q(\mathrm C,\cdot)$ giữ giá trị khởi tạo.
- Bỏ "mô hình cố định": nếu $\hat p$ đổi sau mỗi bước thật, không có một $\hat q_*$ duy nhất để hội tụ tới.

Bước 1 của chứng minh dùng giả thiết mô hình cố định; Bước 3 dùng giả thiết mọi cặp được chọn vô hạn lần.

**Trong thực hành.** Mô hình mẫu là một từ điển các lần thử theo cặp hoặc một chương trình mô phỏng. Mệnh đề 11.9 không cần mô hình đúng. Với mô hình học từ ít mẫu, bảng $Q$ vẫn hội tụ tới $\hat q_*$ của mô hình đó, kể cả khi chính sách tham lam theo $\hat q_*$ kém trong môi trường thật.

Khi mô hình phải học dần, chúng ta xen kẽ ba việc sau mỗi bước thật: cập nhật bảng từ mẫu thật, cập nhật mô hình, rồi làm vài cập nhật lập kế hoạch, như ví dụ sau.

::: example Ví dụ 11.7 (Lượt thứ nhất của Dyna-Q, $n=2$)
**Dữ kiện.** Mê cung hai phòng; $Q\equiv0$; $\alpha=0{,}5$, $\gamma=0{,}9$; mô hình tất định lưu kết quả gần nhất của mỗi cặp đã thử; $n=2$. Lượt thật: $(\mathrm A,\rightarrow,0,\mathrm A)$, $(\mathrm A,\rightarrow,0,\mathrm B)$, $(\mathrm B,\downarrow,0,\mathrm F)$, $(\mathrm F,\rightarrow,0,\mathrm K)$, $(\mathrm K,\rightarrow,+1,\mathrm Z)$.

**Bốn bước đầu.** Mọi mục tiêu, thật hay mô phỏng, bằng $0$, nên $Q$ không đổi. Mô hình ghi $\mathrm{Model}(\mathrm A,\rightarrow)=(0,\mathrm A)$ ở bước 1, rồi ghi đè thành $(0,\mathrm B)$ ở bước 2.

**Bước thứ năm, cập nhật trực tiếp.**

- mục tiêu: $1$, vì $\mathrm Z$ kết thúc;
- sai lệch: $1-0=1$;
- giá trị mới: $Q(\mathrm K,\rightarrow)=0+0{,}5\cdot1=0{,}5$.

**Cập nhật mô hình.** $\mathrm{Model}(\mathrm K,\rightarrow)=(+1,\mathrm Z)$.

**Hai cập nhật lập kế hoạch.** Giả sử bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$.

- $(\mathrm F,\rightarrow)$: mục tiêu $0+0{,}9\cdot0{,}5=0{,}45$; sai lệch $0{,}45$; giá trị mới $0{,}225$.
- $(\mathrm K,\rightarrow)$: mục tiêu $1$; sai lệch $1-0{,}5=0{,}5$; giá trị mới $0{,}5+0{,}25=0{,}75$.

**So sánh.** Với $n=0$ (Q-learning), sau lượt thứ nhất chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$; với $n=2$, bảng có thêm $Q(\mathrm F,\rightarrow)=0{,}225$. Trên mê cung của Sutton và Barto (2018, Hình 8.3, tr. 165), với $n=50$, chính sách tham lam đã phủ phần lớn mê cung ở giữa lượt thứ hai, khi tác tử không lập kế hoạch mới học được một bước.

**Thứ tự cập nhật.** Đảo thứ tự hai cập nhật lập kế hoạch: $(\mathrm K,\rightarrow)$ trước cho $0{,}75$, rồi $(\mathrm F,\rightarrow)$ cho $0{,}5\cdot0{,}9\cdot0{,}75=0{,}3375$. Thứ tự cập nhật đổi kết quả.

**Kiểm tra lại.** $0{,}5\cdot0{,}45=0{,}225$ và $0{,}5+0{,}5\cdot(1-0{,}5)=0{,}75$.
:::

::: algorithm Thuật toán 11.10 (Dyna-Q dạng bảng)
**Đầu vào.** Môi trường; $\gamma\in[0,1)$.

**Đầu ra.** Bảng $Q$ và mô hình $\mathrm{Model}$.

**Giả thiết.** Môi trường tất định: mỗi cặp $(s,a)$ cho đúng một kết cục $(R,S')$.

**Khởi tạo.** $Q(s,a)$ tùy ý, $Q=0$ tại trạng thái kết thúc; $\mathrm{Model}(s,a)$ rỗng với mọi cặp.

**Tham số.** $\alpha$, $\varepsilon$, $n$, ngân sách bước thật.

**Lặp, mỗi vòng một bước thật:**

1. (a) $S\leftarrow$ trạng thái hiện tại, hoặc trạng thái đầu nếu lượt trước vừa kết thúc.
2. (b) $A\leftarrow$ hành động $\varepsilon$-tham lam theo $Q(S,\cdot)$.
3. (c) Thực hiện $A$, quan sát $R$, $S'$.
4. (d) Cập nhật trực tiếp: $Q(S,A)\leftarrow Q(S,A)+\alpha\bigl[R+\gamma\max_{a'}Q(S',a')-Q(S,A)\bigr]$.
5. (e) Cập nhật mô hình: $\mathrm{Model}(S,A)\leftarrow(R,S')$.
6. (f) Lặp $n$ lần: chọn ngẫu nhiên một trạng thái $\tilde S$ đã gặp và một hành động $\tilde A$ đã thử tại $\tilde S$; $(\tilde R,\tilde S')\leftarrow\mathrm{Model}(\tilde S,\tilde A)$; cập nhật $Q(\tilde S,\tilde A)$ bằng quy tắc của bước (d) với $(\tilde S,\tilde A,\tilde R,\tilde S')$.

**Điều kiện dừng.** Hết ngân sách bước thật.

**Chi phí mỗi bước.** $O\bigl((n+1)\max_s\lvert\mathcal A(s)\rvert\bigr)$ phép tính mỗi bước thật.
:::

Thuật toán 11.10 là hộp Dyna-Q của Sutton và Barto (2018, §8.2, tr. 164). Ba bước cuối có tên riêng:

- bước (d) là học tăng cường trực tiếp (direct reinforcement learning, direct RL);
- bước (e) là học mô hình (model learning);
- bước (f) gồm điều khiển tìm kiếm (search control), tức việc chọn cặp, cùng một lần Q-planning.

Ví dụ 11.7 là một lượt của thuật toán với $n=2$.

![Kiến trúc Dyna: kinh nghiệm thật đi vào học trực tiếp, bước (d), tới giá trị và chính sách, và vào học mô hình, bước (e). Từ mô hình, điều khiển tìm kiếm chọn cặp, kinh nghiệm mô phỏng đi vào lập kế hoạch, bước (f). Chính sách cho hành động trở lại môi trường.](img/lec-11/kien-truc-dyna.svg)

Hình vẽ lại ý của Sutton và Barto (2018, Hình 8.1, tr. 163): hai đường đi vào khối giá trị, mẫu thật qua bước (d) và mẫu mô phỏng qua bước (f), dùng cùng một quy tắc cập nhật.

::: remark Nhận xét 11.11 (Dyna-Q, bộ nhớ phát lại và bảo đảm)
- **Về cấu trúc.** Với mô hình tất định, bước (f) giống rút một mẫu từ bộ nhớ phát lại (Định nghĩa 08.7), nhưng mô hình gộp mẫu theo cặp và chỉ giữ kết quả gần nhất.
- **Về bảo đảm.** Bước (f) chỉ chọn cặp đã thử (Sutton và Barto, 2018, tr. 163), nên cặp chưa thử giữ giá trị khởi tạo mà vẫn đi vào $\max_{a'}Q(S',a')$. Mô hình còn đổi sau mỗi bước thật. Giả thiết của Mệnh đề 11.9 không thỏa, nên bảng đạt được phụ thuộc cả dãy bước thật.
:::

**Trong thực hành.** Giả thiết tất định của Thuật toán 11.10 bị vi phạm khi môi trường có trượt, như mê cung hai phòng. Với môi trường ngẫu nhiên, bước (e) cập nhật bảng đếm của Định nghĩa 11.4 và bước (f) rút $(\tilde R,\tilde S')$ theo $\hat p$, như mô hình đếm mà Sutton và Barto (2018, §8.4, tr. 170) dùng cho môi trường ngẫu nhiên. Độ lệch chuẩn của $\hat p$ khi đó giảm theo $1/\sqrt{C(s,a)}$ (Mệnh đề 11.5). Tham số $n$ cho phép đổi phép tính lấy bước thật: $n$ càng lớn, tác tử càng cần ít lượt thật để gần tối ưu (Sutton và Barto, 2018, Hình 8.2, tr. 165).

<!-- note-topic-id: lec-11-topic-08 -->
### 2.5 Mô hình sai và thưởng thăm dò

Khi môi trường đổi, mô hình học từ các bước đã qua mô tả môi trường cũ, như ví dụ sau.

::: example Ví dụ 11.8 (Mê cung đổi cửa)
**Dữ kiện.** Mê cung hai phòng, tác tử Dyna-Q với mô hình tất định. Giả sử sau 3 000 bước thật, cửa $\mathrm F$–$\mathrm K$ bị chặn, còn tường $\mathrm B$–$\mathrm C$ được dỡ.

**Mô hình quá lạc quan.** Mô hình cũ ghi $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$. Tác tử theo chính sách tham lam tới $\mathrm F$, chọn $\rightarrow$ và ở yên; bước (e) ghi $(\mathrm F,\rightarrow)\mapsto(0,\mathrm F)$ và các cập nhật lập kế hoạch hạ $Q(\mathrm F,\rightarrow)$ (tương tự Ví dụ 8.2 của Sutton và Barto, 2018, tr. 166).

**Mô hình quá bi quan.** Mô hình cũ ghi $(\mathrm B,\rightarrow)\mapsto(0,\mathrm B)$, vì trước khi đổi, $\rightarrow$ tại $\mathrm B$ đụng tường. Chính sách tham lam không chọn $\rightarrow$ tại $\mathrm B$, nên mô hình không được sửa (tương tự Ví dụ 8.3, tr. 167).

**Kiểm tra lại.** Sau khi cửa bị chặn, mọi đường từ $\mathrm A$ tới $\mathrm Z$ đi qua cạnh $\mathrm B$–$\mathrm C$, nên tác tử chỉ tới đích khi thử $\rightarrow$ tại $\mathrm B$; đường ngắn nhất $\mathrm A\to\mathrm B\to\mathrm C\to\mathrm D\to\mathrm Z$ dài $4$, như đường cũ.
:::

Một cách trực quan, chính sách tham lam tự kiểm lại mô hình lạc quan vì nó đi tới chỗ mô hình hứa nhiều, và không kiểm lại mô hình bi quan vì nó tránh chỗ mô hình hứa ít. Muốn kiểm lại cặp bi quan, tác tử cộng vào phần thưởng mô phỏng một lượng tăng theo thời gian kể từ lần thử gần nhất, như ví dụ sau.

::: example Ví dụ 11.9 (Một cập nhật Dyna-Q+)
**Dữ kiện.** Mê cung đổi cửa (Ví dụ 11.8), mô hình ghi $(\mathrm B,\rightarrow)\mapsto(0,\mathrm B)$; cặp này chưa được thử lại trong $\ell(\mathrm B,\rightarrow)=400$ bước thật; $\kappa=0{,}01$; $Q(\mathrm B,\rightarrow)=0{,}54$; $\max_aQ(\mathrm B,a)=Q(\mathrm B,\downarrow)=0{,}6$; $\alpha=0{,}5$, $\gamma=0{,}9$.

**Thưởng thăm dò.** $\kappa\sqrt{\ell}=0{,}01\cdot20=0{,}2$.

**Cập nhật lập kế hoạch.**

- mục tiêu: $0+0{,}2+0{,}9\cdot0{,}6=0{,}74$;
- sai lệch: $0{,}74-0{,}54=0{,}2$;
- giá trị mới: $Q(\mathrm B,\rightarrow)=0{,}54+0{,}5\cdot0{,}2=0{,}64$.

**Diễn giải.** $0{,}64>0{,}6$, nên hành động tham lam tại $\mathrm B$ đổi sang $\rightarrow$; tác tử thử lại bức tường và phát hiện lối mở.

**Kiểm tra lại.** Không có thưởng, mục tiêu là $0{,}9\cdot0{,}6=0{,}54$ và sai lệch bằng $0$: cặp đã ở điểm bất động của mô hình, nên các cập nhật lập kế hoạch của Dyna-Q không đổi $Q(\mathrm B,\rightarrow)$; chỉ bước thăm dò $\varepsilon$-tham lam mới đưa tác tử thử lại cặp này.
:::

::: definition Định nghĩa 11.12 (Thưởng thăm dò của Dyna-Q+)
Cho hệ số $\kappa>0$ và với mỗi cặp $(s,a)$, số bước thật $\ell(s,a)$ kể từ lần thử thật gần nhất của cặp. **Dyna-Q+** là Thuật toán 11.10 với các thay đổi sau:

- sau mỗi bước thật $(S,A)$, đặt $\ell(S,A)=0$ và tăng $\ell$ của mọi cặp khác thêm $1$;
- **thưởng thăm dò** (exploration bonus): ở bước (f), phần thưởng mô phỏng $\tilde R$ được thay bằng $\tilde R+\kappa\sqrt{\ell(\tilde S,\tilde A)}$;
- bước (f) chọn cả những hành động chưa từng thử tại một trạng thái đã gặp;
- khi khởi tạo, mô hình của một hành động chưa thử cho tác tử ở yên tại trạng thái đó với phần thưởng $0$.
:::

Thưởng thăm dò chỉ đi vào cập nhật lập kế hoạch; hai thay đổi cuối lấy từ chú thích 1 của Sutton và Barto (2018, tr. 168). Ví dụ 11.9 là một lần chạy bước (f) của Dyna-Q+.

::: remark Nhận xét 11.13 (Thăm dò trong lập kế hoạch)
Với thưởng thăm dò, MDP mà bước (f) lập kế hoạch có phần thưởng $\hat r(s,a)+\kappa\sqrt{\ell(s,a)}$, thay đổi theo thời gian và khác $\hat r$. Bảng của Dyna-Q+ vì vậy không còn ước lượng $\hat q_*$ của mô hình, và Mệnh đề 11.9 không áp dụng. Khác chính sách $\varepsilon$-tham lam vốn thử ngẫu nhiên, thưởng thăm dò hướng tác tử tới cặp đã lâu chưa thử.
:::

<!-- note-topic-id: lec-11-topic-09 -->
### 2.6 Cập nhật kỳ vọng và cập nhật mẫu

Theo mô hình đếm của Ví dụ 11.3, $(\mathrm A,\rightarrow)$ có hai trạng thái kế đồng khả năng. Dyna-Q cập nhật cặp này bằng một mẫu; lặp giá trị cập nhật bằng cả phân phối. Chúng ta cần biết mỗi loại cập nhật tốn bao nhiêu lần đánh giá và cho mục tiêu gì.

Một cách trực quan, cập nhật kỳ vọng hỏi mô hình mọi kết cục rồi lấy trung bình, nên mục tiêu không có phương sai nhưng tốn nhiều phép tính; cập nhật mẫu chỉ hỏi một kết cục, rẻ hơn nhưng có nhiễu. Để làm rõ, xem ví dụ sau.

::: example Ví dụ 11.10 (Cập nhật kỳ vọng và cập nhật mẫu tại $(\mathrm A,\rightarrow)$)
**Dữ kiện.** Mô hình đếm $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=\hat p(\mathrm A\mid\mathrm A,\rightarrow)=0{,}5$, phần thưởng $0$; giả sử $\max_aQ(\mathrm B,a)=0{,}6$, $\max_aQ(\mathrm A,a)=0{,}4$; $\gamma=0{,}9$.

**Cập nhật kỳ vọng.** Mục tiêu $0{,}9(0{,}5\cdot0{,}6+0{,}5\cdot0{,}4)=0{,}45$; phép tính cần $\max_aQ$ tại hai trạng thái kế, tức hai lần đánh giá.

**Cập nhật mẫu.** Mẫu $\mathrm B$ cho mục tiêu $0{,}9\cdot0{,}6=0{,}54$; mẫu $\mathrm A$ cho $0{,}9\cdot0{,}4=0{,}36$; mỗi mẫu một lần đánh giá.

**Kiểm tra lại.** Nếu hai cập nhật mẫu liên tiếp rút được $\mathrm B$ rồi $\mathrm A$, với $\alpha_1=1$, $\alpha_2=\tfrac12$, thì $Q=(0{,}54+0{,}36)/2=0{,}45$, trùng cập nhật kỳ vọng.
:::

::: definition Định nghĩa 11.14 (Cập nhật kỳ vọng, cập nhật mẫu, hệ số phân nhánh)
Cho mô hình $\hat p$ và bảng $Q$. Với cặp $(s,a)$:

- **cập nhật kỳ vọng** (expected update) đặt
  $$\begin{aligned}&Q(s,a)\leftarrow{}\\&\ \sum_{s',r}\hat p(s',r\mid s,a)\\&\ \times\bigl[r+\gamma\max_{a'}Q(s',a')\bigr];\end{aligned}\tag{2.3}$$
- **cập nhật mẫu** (sample update) rút $(R,S')\sim\hat p(\cdot,\cdot\mid s,a)$ và đặt
  $$\begin{aligned}&Q(s,a)\leftarrow Q(s,a)\\&\ +\alpha\bigl[R+\gamma\max_{a'}Q(S',a')\\&\ -Q(s,a)\bigr];\end{aligned}\tag{2.4}$$
- **hệ số phân nhánh** (branching factor) $b$ của $(s,a)$ là số trạng thái kế $s'$ có $\hat p(s'\mid s,a)>0$.

Một lần đánh giá là một lần tính $\max_{a'}Q(s',a')$ tại một trạng thái kế.
:::

Sutton và Barto (2018, §8.5, Hình 8.6) vẽ hai loại cập nhật này bằng sơ đồ cập nhật ngược (backup diagram). Cập nhật kỳ vọng cần mô hình phân phối, cập nhật mẫu chỉ cần mô hình mẫu (Định nghĩa 11.1). Theo Ví dụ 11.2, mục tiêu mẫu có trung bình bằng mục tiêu kỳ vọng, nên hai loại khác nhau ở chi phí và phương sai: cập nhật kỳ vọng tốn $b$ lần đánh giá và cho đúng mục tiêu kỳ vọng, cập nhật mẫu tốn một lần và cho mục tiêu có phương sai.

**Câu hỏi.** Sau $k$ cập nhật mẫu, sai số còn lại bao nhiêu so với một cập nhật kỳ vọng tốn $b$ lần đánh giá? Sutton và Barto (2018, tr. 174) xét $b$ trạng thái kế đồng khả năng, lấy sai số ban đầu bằng $1$, và cho sai số sau $k$ cập nhật mẫu là $\sqrt{(b-1)/(bk)}$. Mệnh đề sau nêu các giả thiết xác suất mà dưới đó công thức này đúng: phần (b) coi các giá trị kế như $b$ số rút độc lập có phương sai $1$.

::: proposition Mệnh đề 11.15 (Sai số của trung bình các cập nhật mẫu)
**Giả thiết.** Phần thưởng bằng $0$; giá trị kế $y_{s'}=\gamma\max_{a'}Q(s',a')$ cố định; mục tiêu kỳ vọng $\bar y=\sum_{s'}\hat p(s'\mid s,a)y_{s'}$. Rút $k\ge1$ trạng thái kế độc lập theo $\hat p(\cdot\mid s,a)$, bước học $\alpha_j=1/j$ ở cập nhật thứ $j$.

**Kết luận.**

- (a) Với mọi giá trị cố định của các $y_{s'}$, sau $k$ cập nhật, $Q_k=\frac1k\sum_{j=1}^ky_{S'_j}$ và $\mathbb E(Q_k-\bar y)^2=\sigma^2/k$, với $\sigma^2=\sum_{s'}\hat p(s'\mid s,a)(y_{s'}-\bar y)^2$.
- (b) Nếu thêm: có $b$ trạng thái kế đồng khả năng, và các giá trị $y_1,\dots,y_b$ là biến ngẫu nhiên độc lập, cùng kỳ vọng, phương sai $1$, độc lập với việc rút mẫu, thì $\mathbb E\sigma^2=(b-1)/b$ và sai số căn bình phương trung bình là
$$\sqrt{\mathbb E(Q_k-\bar y)^2}=\sqrt{\frac{b-1}{bk}}.\tag{2.5}$$

**Điều kiện áp dụng.** Bảng $Q$ tại các trạng thái kế không đổi trong suốt $k$ cập nhật. Khi so với cập nhật kỳ vọng, mỗi lần đánh giá có cùng chi phí, nên $k$ cập nhật mẫu tốn bằng $k/b$ cập nhật kỳ vọng.

**Phạm vi.** Mệnh đề mô tả một cặp với giá trị kế cố định. Cập nhật kỳ vọng có sai số $0$ sau $b$ lần đánh giá. Sutton và Barto (2018, tr. 174) đặt sai số trước cập nhật đầu bằng $1$ để chuẩn hóa; (2.5) mô tả các điểm $k\ge1$ của đường cong.
:::

::: proof
**Bước 1 (trung bình).** Với $\alpha_1=1$, $Q_1=y_{S'_1}$; theo Mệnh đề 05.9, bước học $1/j$ cho $Q_k=\frac1k\sum_{j=1}^ky_{S'_j}$.

**Bước 2 (phần (a)).** Với các $y_{s'}$ cố định, các $y_{S'_j}$ độc lập, cùng phân phối, kỳ vọng $\bar y$, phương sai $\sigma^2$, nên trung bình của chúng có kỳ vọng $\bar y$ và phương sai $\sigma^2/k$.

**Bước 3 (phần (b)).** Với $\hat p=1/b$ ở mỗi trạng thái kế, $\bar y=\frac1b\sum_iy_i$ và $\sigma^2=\frac1b\sum_{i=1}^b(y_i-\bar y)^2$. Gọi $m$ là kỳ vọng chung của các $y_i$. Khai triển quanh $m$:
$$\begin{aligned}\sum_{i=1}^b(y_i-\bar y)^2&=\sum_{i=1}^b(y_i-m)^2\\&\quad-b(\bar y-m)^2.\end{aligned}$$
Vì các $y_i$ độc lập, phương sai $1$, ta có $\mathbb E\sum_i(y_i-m)^2=b$ và $\mathbb E(\bar y-m)^2=\operatorname{Var}\bar y=1/b$, nên
$$\mathbb E\sigma^2=\frac{b-(b\cdot1/b)}b=\frac{b-1}b.$$
Phần (a) đúng với mọi giá trị cố định của các $y_i$, nên đúng có điều kiện theo $y$: $\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k$. Lấy kỳ vọng theo $y$ cho $\mathbb E(Q_k-\bar y)^2=(b-1)/(bk)$, rồi lấy căn bậc hai. $\square$
:::

Các giả thiết của mệnh đề có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "giá trị kế cố định": các mục tiêu mẫu không còn cùng phân phối, nên Bước 2 không dùng được.
- Bỏ "$\alpha_j=1/j$": với bước học hằng $\alpha$, $Q_k$ là trung bình có trọng số giảm theo hàm mũ, và phương sai không tiến về $0$.
- Bỏ "cùng kỳ vọng" ở (b): nếu $y_i$ có kỳ vọng $m_i$ với trung bình $\bar m$, cùng phép khai triển cho $\mathbb E\sigma^2=(b-1)/b+\frac1b\sum_i(m_i-\bar m)^2$, lớn hơn $(b-1)/b$ khi các $m_i$ khác nhau.

::: example Ví dụ 11.11 (Sai số của cập nhật mẫu)
**Dữ kiện.** Mô hình của Mệnh đề 11.15(b).

**Tính.** Theo (2.5):

| $b$ | $k$ | $\sqrt{(b-1)/(bk)}$ | số lần đánh giá của cập nhật mẫu | của cập nhật kỳ vọng |
|---:|---:|---:|---:|---:|
| $2$ | $1$ | $0{,}7071$ | $1$ | $2$ |
| $100$ | $10$ | $0{,}3146$ | $10$ | $100$ |
| $100$ | $100$ | $0{,}0995$ | $100$ | $100$ |

**Diễn giải.** Với $b=100$, một phần mười chi phí của cập nhật kỳ vọng đưa sai số về $0{,}3146$; cập nhật kỳ vọng chưa xong thì chưa cho giá trị mới.

**Kiểm tra lại.** $99/1000=0{,}099$ và $\sqrt{0{,}099}=0{,}3146$.
:::

![Sai số theo số lần đánh giá chia cho b, từ 0 đến 2: ba đường cập nhật mẫu căn của (b trừ 1) chia (b k) với b bằng 2, 10, 100; bậc thang cập nhật kỳ vọng ở mức 1 tới hoành độ 1 rồi về 0.](img/lec-11/cap-nhat-ky-vong-va-mau.svg)

Trên hình, hoành độ $1$ là chi phí của một cập nhật kỳ vọng; với $b$ lớn, đường cập nhật mẫu đã rơi gần hết trước hoành độ đó (Sutton và Barto, 2018, Hình 8.7, tr. 174).

::: remark Nhận xét 11.16 (Điều kiện ưu tiên cập nhật mẫu)
Cập nhật mẫu có lợi khi hệ số phân nhánh lớn và có quá nhiều trạng thái để giải chính xác trong ngân sách cho trước (Sutton và Barto, 2018, tr. 174). Khi $b$ nhỏ, như $b=2$ ở $(\mathrm A,\rightarrow)$, một cập nhật kỳ vọng chỉ tốn gấp đôi một cập nhật mẫu và cho sai số $0$ thay vì $0{,}7071$.
:::

**Trong thực hành.** Với mô hình mẫu là một chương trình mô phỏng, tác tử chỉ dùng được cập nhật mẫu, và $b$ có thể rất lớn. Bảng $Q$ thay đổi trong lúc lập kế hoạch, nên giả thiết "giá trị kế cố định" của Mệnh đề 11.15 không thỏa.

<!-- note-topic-id: lec-11-topic-10 -->
### 2.7 Đọc thêm: phân bổ các cập nhật

Thuật toán 11.8 và 11.10 chọn cặp cập nhật ngẫu nhiên, trong khi Ví dụ 11.7 cho thấy cập nhật $(\mathrm K,\rightarrow)$ trước $(\mathrm F,\rightarrow)$ cho $0{,}3375$ thay vì $0{,}225$.

::: remark Nhận xét 11.17 (Quét ưu tiên)
**Quét ưu tiên** (prioritized sweeping) cập nhật trước cặp có sai lệch dự kiến lớn nhất, rồi đưa các cặp dẫn tới trạng thái vừa đổi giá trị vào hàng đợi (Sutton và Barto, 2018, §8.4, tr. 168–171). Giá trị vì vậy lan ngược từ đích, như thứ tự $(\mathrm K,\rightarrow)$ rồi $(\mathrm F,\rightarrow)$ cho $0{,}3375$ ở Ví dụ 11.7. Định lý 04.32 chỉ bảo đảm hội tụ khi mọi trạng thái được cập nhật vô hạn lần. Quét ưu tiên với ngưỡng $\theta$ bỏ qua các cặp có ưu tiên nhỏ, nên không tự thỏa điều kiện đó.
:::

::: remark Nhận xét 11.18 (Lấy mẫu theo quỹ đạo)
**Lấy mẫu theo quỹ đạo** (trajectory sampling) chọn cặp cập nhật bằng cách mô phỏng lượt theo chính sách hiện tại, tức theo phân phối theo chính sách (on-policy distribution); trên các bài toán sinh ngẫu nhiên của thí nghiệm, cách này cải thiện nhanh hơn phân bổ đều ở giai đoạn đầu và chậm hơn về lâu dài, với lợi thế lớn hơn khi nhiều trạng thái và hệ số phân nhánh nhỏ (Sutton và Barto, 2018, §8.6, Hình 8.8).
:::

::: theorem Định lý 11.19 (Hội tụ của RTDP)
**Giả thiết.** Bài toán có kết thúc, không chiết khấu; lượt bắt đầu ngẫu nhiên trong tập trạng thái đầu và kết thúc ở đích hấp thụ; giá trị đầu tại đích bằng $0$ và không nhỏ hơn giá trị tối ưu ở nơi khác; từ mọi trạng thái đầu có chính sách tới đích với xác suất $1$; phần thưởng ngoài đích âm ngặt.

**Kết luận.** Quy hoạch động thời gian thực (real-time dynamic programming, RTDP), lặp giá trị bất đồng bộ trên quỹ đạo tham lam, hội tụ với xác suất $1$ tới chính sách tối ưu trên các trạng thái liên quan.

**Điều kiện áp dụng.** Mô hình phân phối đúng.

**Phạm vi.** Mê cung hai phòng không thỏa hai giả thiết: có chiết khấu $\gamma=0{,}9$ và phần thưởng ngoài đích bằng $0$. Chứng minh nằm ngoài phạm vi học phần; xem Barto, Bradtke và Singh (1995), dẫn theo Sutton và Barto (2018, §8.7, tr. 178).
:::

Như vậy, chúng ta có mô hình đếm và phương sai của nó (Mệnh đề 11.5), Q-planning hội tụ tới $\hat q_*$ khi mô hình cố định và xác định ở mọi cặp (Mệnh đề 11.9), Dyna-Q (Thuật toán 11.10) và sai số của cập nhật mẫu (Mệnh đề 11.15). Tuy nhiên, lập kế hoạch nền tốn phép tính cho mọi trạng thái được chọn, kể cả những trạng thái như $\mathrm A$, $\mathrm B$, $\mathrm E$ mà đường ngắn nhất từ $\mathrm F$ tới $\mathrm Z$ không đi qua. Tác tử đứng ở một trạng thái chỉ cần chọn tốt một hành động tại đó, nên chỉ cần tính các diễn biến bắt đầu từ trạng thái này.

---

## 3. Tìm kiếm theo cây Monte Carlo

<!-- note-topic-id: lec-11-topic-11 -->
### 3.1 Lập kế hoạch tại thời điểm quyết định và thuật toán rollout

Tác tử đứng ở $\mathrm F$, có một mô hình mẫu đúng và một chính sách cơ sở $\pi_0$ chọn mỗi mũi tên với xác suất $1/4$. Từ $\mathrm F$, $\pi_0$ chỉ có giá trị $0{,}2016$, so với $v_*(\mathrm F)=0{,}8566$.

Một cách trực quan, tác tử thử từng hành động tại $\mathrm F$ trong mô hình, đi tiếp theo $\pi_0$ tới hết lượt, lặp lại nhiều lần và lấy trung bình lợi tức, một ước lượng của $q_{\pi_0}(\mathrm F,a)$. Để so ước lượng đó với giá trị chính xác, xem ví dụ sau.

::: example Ví dụ 11.12 (Rollout tại $\mathrm F$ với chính sách ngẫu nhiên đều)
**Dữ kiện.** Mê cung hai phòng (trượt $0{,}2$, phần thưởng $+1$ khi vào $\mathrm Z$, $\gamma=0{,}9$); $\pi_0(a\mid s)=1/4$. Phần ước lượng dùng $m=2$ mô phỏng cho mỗi hành động, không cắt ($D=\infty$): với $\pi_0$ ngẫu nhiên đều, lượt kết thúc với xác suất $1$.

**Giá trị của $\pi_0$.** Giải hệ đánh giá chính sách bảy phương trình (Định lý 03.28). Mỗi phương trình có dạng $v_{\pi_0}(s)=\tfrac14\sum_aq_{\pi_0}(s,a)$, với $q_{\pi_0}(s,a)$ tính như ở bước sau; chẳng hạn tại $\mathrm F$, với $v$ viết tắt $v_{\pi_0}$,
$$\begin{aligned}v(\mathrm F)&=\tfrac14\bigl[0{,}72\,v(\mathrm K)+0{,}9\,v(\mathrm F)\\&\quad+0{,}72\,v(\mathrm B)+0{,}72\,v(\mathrm E)\\&\quad+3\cdot0{,}18\,v(\mathrm F)\bigr].\end{aligned}$$
Nghiệm là

| $s$ | $\mathrm A$ | $\mathrm B$ | $\mathrm C$ | $\mathrm D$ | $\mathrm E$ | $\mathrm F$ | $\mathrm K$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $v_{\pi_0}(s)$ | $0{,}0890$ | $0{,}1137$ | $0{,}4270$ | $0{,}6019$ | $0{,}1137$ | $0{,}2016$ | $0{,}4893$ |

**Giá trị hành động tại $\mathrm F$.** Theo Mệnh đề 03.22, $q_{\pi_0}(\mathrm F,a)=0{,}72\,v_{\pi_0}(s_a)+0{,}18\,v_{\pi_0}(\mathrm F)$, $s_a$ là ô $a$ dẫn tới:

- $\rightarrow$: $0{,}72\cdot0{,}489270+0{,}18\cdot0{,}201554=0{,}3886$;
- $\downarrow$, đụng biên: $0{,}9\cdot0{,}201554=0{,}1814$;
- $\uparrow$: $0{,}72\cdot0{,}113683+0{,}18\cdot0{,}201554=0{,}1181$; $\leftarrow$ cho cùng giá trị vì $v_{\pi_0}(\mathrm E)=v_{\pi_0}(\mathrm B)$.

**Hai mô phỏng cho mỗi hành động.** Giả sử mô hình mẫu cho các mô phỏng sau, mỗi mô phỏng chạy tới khi vào $\mathrm Z$. Phần thưởng khác $0$ duy nhất là $+1$ khi vào $\mathrm Z$, nên mô phỏng vào $\mathrm Z$ ở bước $j$ có lợi tức $\gamma^{j-1}$.

| $a$ | mô phỏng 1: bước vào $\mathrm Z$, lợi tức | mô phỏng 2: bước vào $\mathrm Z$, lợi tức | $\bar G(a)$ |
|---|---|---|---:|
| $\rightarrow$ | $2$ ($\mathrm F\to\mathrm K\to\mathrm Z$), $0{,}9$ | $13$, $\gamma^{12}=0{,}2824$ | $0{,}5912$ |
| $\downarrow$ | $3$ ($\mathrm F\to\mathrm F\to\mathrm K\to\mathrm Z$), $0{,}81$ | $21$, $\gamma^{20}=0{,}1216$ | $0{,}4658$ |
| $\uparrow$ | $6$ ($\mathrm F\to\mathrm B\to\mathrm A\to\mathrm B\to\mathrm F\to\mathrm K\to\mathrm Z$), $0{,}5905$ | $26$, $\gamma^{25}=0{,}0718$ | $0{,}3311$ |
| $\leftarrow$ | $9$, $\gamma^8=0{,}4305$ | $31$, $\gamma^{30}=0{,}0424$ | $0{,}2364$ |

**Chọn.** $\bar G(\rightarrow)=0{,}5912$ lớn nhất, nên thuật toán chọn $A_t=\rightarrow$, trùng hành động tham lam theo $q_{\pi_0}(\mathrm F,\cdot)$. Hai mô phỏng mỗi hành động cho ước lượng còn lệch nhiều: $\bar G(\rightarrow)-q_{\pi_0}(\mathrm F,\rightarrow)=0{,}2027$.

**Kiểm tra lại.** $v_{\pi_0}(\mathrm F)=\tfrac14(0{,}3886+0{,}1814+2\cdot0{,}1181)=0{,}2016$, đúng phương trình Bellman kỳ vọng tại $\mathrm F$; $(0{,}9+0{,}28243)/2=0{,}5912$.
:::

::: algorithm Thuật toán 11.20 (Thuật toán rollout)
**Đầu vào.** Mô hình mẫu; chính sách Markov dừng $\pi_0$, gọi là **chính sách cơ sở** (base policy); trạng thái hiện tại $s$; $\gamma\in[0,1)$.

**Đầu ra.** Hành động $A_t\in\mathcal A(s)$.

**Giả thiết.** $\mathcal A(s)$ hữu hạn; mô hình mẫu trả $(R,S')$ độc lập giữa các lần gọi.

**Khởi tạo.** $\bar G(a)=0$ với mọi $a\in\mathcal A(s)$.

**Tham số.** Số mô phỏng $m\ge1$ cho mỗi hành động; độ sâu cắt (truncation depth) $D\in\{1,2,\dots\}\cup\{\infty\}$, với $D=\infty$ chỉ khi lượt kết thúc với xác suất $1$.

**Lặp,** với mỗi $a\in\mathcal A(s)$:

1. Với $i=1,\dots,m$: đặt $S_0=s$, $A_0=a$, $G_i(a)=0$; với $k=0,1,\dots$, gọi mô hình mẫu với $(S_k,A_k)$, nhận $(R_{k+1},S_{k+1})$, cộng $\gamma^kR_{k+1}$ vào $G_i(a)$; dừng mô phỏng khi $S_{k+1}$ là trạng thái kết thúc hoặc $k+1=D$, nếu không thì rút $A_{k+1}\sim\pi_0(\cdot\mid S_{k+1})$.
2. $\bar G(a)=\frac1m\sum_{i=1}^mG_i(a)$.

Sau vòng lặp:

3. Chọn $A_t\in\arg\max_a\bar G(a)$, phá hòa theo một quy tắc cố định.

**Điều kiện dừng.** Đủ $m$ mô phỏng cho mỗi hành động.

**Chi phí mỗi bước.** Với $D$ hữu hạn, mỗi quyết định gọi mô hình nhiều nhất $\lvert\mathcal A(s)\rvert\,m\,D$ lần, tức $O(\lvert\mathcal A(s)\rvert\,m\,D)$; với $D=\infty$, số lần gọi bằng tổng độ dài các mô phỏng.
:::

Ví dụ 11.12 là một lần chạy Thuật toán 11.20 tại $\mathrm F$ với $m=2$, $D=\infty$. Gọi **chính sách rollout** (rollout policy) là chính sách $\pi_{\mathrm{ro}}$ với $\pi_{\mathrm{ro}}(s)\in\arg\max_{a\in\mathcal A(s)}q_{\pi_0}(s,a)$ tại mọi $s$, phá hòa theo cùng quy tắc cố định. Khi mô hình mẫu đúng, mô phỏng không bị cắt (lượt kết thúc với xác suất $1$) và $m\to\infty$, $\bar G(a)\to q_{\pi_0}(s,a)$ hầu chắc chắn theo luật số lớn, nên thuật toán xấp xỉ $\pi_{\mathrm{ro}}(s)$. Với mô hình sai, $\bar G(a)$ tiến tới giá trị của $\pi_0$ trên MDP của mô hình.

Thuật toán rollout là lập kế hoạch tại thời điểm quyết định (Định nghĩa 11.2). Sutton và Barto (2018, §8.10) gọi $\pi_0$ là "rollout policy"; chúng ta theo cách gọi của Bertsekas và dùng tên chính sách rollout cho $\pi_{\mathrm{ro}}$. "Thuật toán rollout" cũng khác "đoạn thu (rollout)" của Bài 10, là dữ liệu thu để học.

**Câu hỏi.** Chính sách rollout có tốt hơn một chính sách cơ sở kém như ngẫu nhiên đều không? Mệnh đề sau trả lời: không kém hơn, khi $q_{\pi_0}$ chính xác.

::: proposition Mệnh đề 11.21 (Tính chất cải thiện của rollout)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$. Chính sách cơ sở $\pi_0$ Markov dừng với giá trị chính xác $q_{\pi_0}$, $v_{\pi_0}$. Chính sách $\pi_{\mathrm{ro}}$ Markov dừng xác định, tham lam theo $q_{\pi_0}$ tại mọi trạng thái.

**Kết luận.** $v_{\pi_{\mathrm{ro}}}(s)\ge v_{\pi_0}(s)$ với mọi $s$; bất đẳng thức nghiêm ngặt tại $s$ khi $\max_aq_{\pi_0}(s,a)>v_{\pi_0}(s)$.

**Điều kiện áp dụng.** Giá trị $q_{\pi_0}$ dùng để chọn hành động là giá trị chính xác, không phải trung bình của một số hữu hạn mô phỏng.

**Phạm vi.** Mệnh đề chỉ so $\pi_{\mathrm{ro}}$ với $\pi_0$, không bảo đảm $\pi_{\mathrm{ro}}$ tối ưu. Khi $q_{\pi_0}$ tính trên một mô hình sai, kết luận áp cho MDP của mô hình.
:::

::: proof
**Bước 1 (điều kiện của Định lý 04.13).** Với mọi $s$, vì $\pi_{\mathrm{ro}}(s)$ đạt cực đại và cực đại không nhỏ hơn trung bình có trọng số,
$$\begin{aligned}&q_{\pi_0}(s,\pi_{\mathrm{ro}}(s))\\&\quad=\max_aq_{\pi_0}(s,a)\\&\quad\ge\textstyle\sum_a\pi_0(a\mid s)q_{\pi_0}(s,a)\\&\quad=v_{\pi_0}(s).\end{aligned}$$
Đẳng thức cuối là liên hệ giữa $v_{\pi_0}$ và $q_{\pi_0}$ của chính sách Markov dừng (Mệnh đề 03.23).

**Bước 2 (Định lý 04.13).** Với $\pi_0$ Markov dừng có giá trị chính xác và $\pi_{\mathrm{ro}}$ Markov dừng xác định thỏa Bước 1, Định lý 04.13(a) cho $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$, và 04.13(b) cho bất đẳng thức nghiêm ngặt tại $s$ khi Bước 1 nghiêm ngặt tại $s$. $\square$
:::

Thực hiện rollout ở mọi trạng thái gặp trên đường là thực hiện $\pi_{\mathrm{ro}}$. Sutton và Barto (2018, tr. 184) so rollout với một bước cải thiện của lặp chính sách; vì rollout chỉ đổi hành động tại trạng thái hiện tại, sách cũng so nó với một bước lặp giá trị bất đồng bộ. Bertsekas (2020, Mệnh đề 5.4.2) phát biểu tính chất này dưới dạng chi phí. Hai giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "$q_{\pi_0}$ chính xác": với $m=1$, một lần mô phỏng may mắn của $\uparrow$ có thể cho $\bar G(\uparrow)>\bar G(\rightarrow)$, và hành động chọn tại $\mathrm F$ kém hơn cả trung bình của $\pi_0$.
- Bỏ "$\pi_0$ Markov dừng": với $\pi_0$ phụ thuộc lịch sử, đẳng thức cuối của Bước 1 không còn.

::: example Ví dụ 11.13 (Chính sách rollout trên cả mê cung)
**Dữ kiện.** Mê cung hai phòng, $\pi_0$ ngẫu nhiên đều, với

| $s$ | $\mathrm A$ | $\mathrm B$ | $\mathrm C$ | $\mathrm D$ | $\mathrm E$ | $\mathrm F$ | $\mathrm K$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $v_{\pi_0}(s)$ | $0{,}0890$ | $0{,}1137$ | $0{,}4270$ | $0{,}6019$ | $0{,}1137$ | $0{,}2016$ | $0{,}4893$ |

**Quy tắc.** Theo Mệnh đề 03.22, $q_{\pi_0}(s,a)=0{,}72\,v_{\pi_0}(s_a)+0{,}18\,v_{\pi_0}(s)$ khi $a$ dẫn tới ô $s_a\ne\mathrm Z$; $q_{\pi_0}(s,a)=0{,}8+0{,}18\,v_{\pi_0}(s)$ khi $a$ dẫn vào $\mathrm Z$; $q_{\pi_0}(s,a)=0{,}9\,v_{\pi_0}(s)$ khi $a$ đụng tường hoặc biên. Chẳng hạn $q_{\pi_0}(\mathrm A,\downarrow)=0{,}72\cdot0{,}1137+0{,}18\cdot0{,}0890=0{,}0979$.

**Tham lam theo $q_{\pi_0}$.** Tại từng ô:

- $\mathrm A$: $\downarrow$ hoặc $\rightarrow$, hòa ở $0{,}0979$; $\mathrm B$: $\downarrow$ ($0{,}1656$); $\mathrm E$: $\rightarrow$ ($0{,}1656$);
- $\mathrm F$: $\rightarrow$ ($0{,}3886$); $\mathrm K$: $\rightarrow$ ($0{,}8881$);
- $\mathrm C$: $\rightarrow$ ($0{,}5102$, so với $\downarrow$ là $0{,}4291$); $\mathrm D$: $\downarrow$ ($0{,}9083$).

**Diễn giải.** Mọi lựa chọn là một bước của đường ngắn nhất, nên $\pi_{\mathrm{ro}}$ có giá trị $v_*$: tại $\mathrm F$, từ $0{,}2016$ lên $0{,}8566$, vượt xa bảo đảm "không giảm" của Mệnh đề 11.21.

**Kiểm tra lại.** $q_{\pi_0}(\mathrm C,\rightarrow)=0{,}72\cdot0{,}601855+0{,}18\cdot0{,}426962=0{,}5102$.
:::

Mệnh đề 11.21 cần $q_{\pi_0}$ chính xác, còn thuật toán rollout chỉ có trung bình của $m$ mô phỏng. **Câu hỏi.** Cần bao nhiêu mô phỏng để trung bình không đảo thứ tự hai hành động? Mệnh đề sau chặn xác suất đảo thứ tự theo $m$.

::: proposition Mệnh đề 11.22 (Xác suất chọn sai của rollout với $m$ mô phỏng)
**Giả thiết.** Mô hình mẫu đúng. Tại trạng thái $s$, hai hành động $a$, $a'$ có $\Delta=q_{\pi_0}(s,a)-q_{\pi_0}(s,a')>0$. Thuật toán 11.20 chạy $m$ mô phỏng cho mỗi hành động, với $m$ cố định trước; mô phỏng chạy tới trạng thái kết thúc, không cắt ($D=\infty$, lượt kết thúc với xác suất $1$); $2m$ lợi tức mô phỏng độc lập, mỗi lợi tức nằm trong một đoạn độ rộng $B$.

**Kết luận.**
$$\begin{aligned}&\Pr\bigl\{\bar G(a')\ge\bar G(a)\bigr\}\\&\quad\le\exp\Bigl(-\frac{m\Delta^2}{B^2}\Bigr).\end{aligned}\tag{3.1}$$

**Điều kiện áp dụng.** Chặn (3.1) so một cặp hành động; với nhiều hơn hai hành động, bất đẳng thức hợp cho chặn xác suất không chọn hành động tốt nhất bằng tổng các chặn (3.1).

**Phạm vi.** Không áp dụng khi $m$ được chọn theo kết quả mô phỏng, như dừng sớm khi một hành động dẫn rõ. Khi cắt ở độ sâu $D$ hữu hạn, mỗi lợi tức mô phỏng có kỳ vọng $q^D_{\pi_0}(s,a)$, kỳ vọng của lợi tức trong $D$ bước đầu, và (3.1) đúng với $\Delta^D=q^D_{\pi_0}(s,a)-q^D_{\pi_0}(s,a')$ thay $\Delta$.
:::

::: proof
**Bước 1 (đưa về một tổng).** Với các lợi tức mô phỏng $G_i(a)$, $G_i(a')$, đặt
$$Z=\sum_{i=1}^mG_i(a')-\sum_{i=1}^mG_i(a).$$
Biến cố $\bar G(a')\ge\bar G(a)$ là $Z\ge0$. Vì mô hình đúng, mỗi $G_i(a)$ có kỳ vọng $q_{\pi_0}(s,a)$, nên $\mathbb EZ=-m\Delta$.

**Bước 2 (Hoeffding một phía).** $Z$ là tổng của $2m$ biến độc lập, với $m$ cố định trước, mỗi biến trong một đoạn độ rộng $B$, nên tổng bình phương độ rộng là $2mB^2$. Biến cố $Z\ge0$ là $Z-\mathbb EZ\ge m\Delta$, và bất đẳng thức Hoeffding với $t=m\Delta$ cho
$$\begin{aligned}&\Pr\{Z\ge0\}\\&\quad\le\exp\Bigl(-\frac{2m^2\Delta^2}{2mB^2}\Bigr)\\&\quad=\exp\Bigl(-\frac{m\Delta^2}{B^2}\Bigr).\ \square\end{aligned}$$
:::

::: example Ví dụ 11.14 (Số mô phỏng của rollout)
**Dữ kiện.** $q_{\pi_0}(\mathrm F,\rightarrow)=0{,}388554$, $q_{\pi_0}(\mathrm F,\downarrow)=0{,}181398$ (Ví dụ 11.12). Lợi tức nằm trong $[0,1]$ vì phần thưởng khác $0$ duy nhất là $+1$ khi vào $\mathrm Z$, nên $B=1$.

**Khoảng cách.** $\Delta=0{,}2072$ và $\Delta^2=0{,}0429$.

**Số mô phỏng.** Để vế phải của (3.1) không vượt $0{,}05$, cần $m\Delta^2\ge\ln20$, tức $m\ge\ln20/\Delta^2=2{,}9957/0{,}0429=69{,}8$. Với $m=70$, chặn bằng $\exp(-70\Delta^2)=0{,}0496$.

**So sánh.** Với $m=50$, chặn bằng $0{,}1170$. Nếu cắt ở $D=20$, $q^{20}_{\pi_0}(\mathrm F,\rightarrow)=0{,}3792$, $q^{20}_{\pi_0}(\mathrm F,\downarrow)=0{,}1670$, nên $\Delta^{20}=0{,}2122$ và với $m=70$, chặn bằng $\exp(-70\,(\Delta^{20})^2)=0{,}0428$.

**Kiểm tra lại.** $70\cdot0{,}042913=3{,}0039$ và $e^{-3{,}0039}=0{,}0496\le0{,}05$.
:::

**Trong thực hành.** Các mô phỏng độc lập chạy song song được. Khi lượt dài, mô phỏng được cắt sớm và cộng một giá trị ước lượng (Sutton và Barto, 2018, tr. 185), nên lợi tức không còn là mẫu không chệch của $q_{\pi_0}$. Thời gian cho mỗi quyết định giới hạn số mô phỏng $m$.

<!-- note-topic-id: lec-11-topic-12 -->
### 3.2 Chọn hành động theo cận tin cậy trên

Thuật toán rollout chia đều $m$ mô phỏng cho bốn hành động tại $\mathrm F$, kể cả $\uparrow$ có giá trị $0{,}1181$, kém xa $\rightarrow$. Với $\Delta=q_{\pi_0}(\mathrm F,\rightarrow)-q_{\pi_0}(\mathrm F,\uparrow)=0{,}2704$, sau $m$ mô phỏng mỗi hành động, (3.1) cho xác suất $\bar G(\uparrow)\ge\bar G(\rightarrow)$ không quá $\exp(-0{,}0731\,m)$, nên phần lớn mô phỏng dành cho $\uparrow$ không đổi quyết định.

Một cách trực quan, lựa chọn hành động tại $\mathrm F$ là một bài toán chọn lặp lại một bước (multi-armed bandit) theo Định nghĩa 01.16. Một quy tắc tốt ưu tiên hành động có trung bình cao, hoặc còn ít mẫu nên trung bình có thể sai nhiều, như ví dụ sau.

::: example Ví dụ 11.15 (Quy tắc cận tin cậy trên, hai hành động)
**Dữ kiện.** Bài toán chọn lặp lại một bước. Sau $8$ lần chọn, hành động 1 có $\bar r(1)=0{,}6$, $N(1)=6$; hành động 2 có $\bar r(2)=0{,}4$, $N(2)=2$; $c_{\mathrm{ucb}}=1$. Lần chọn kế tiếp là bước $t=9$, và $\ln9=2{,}1972$.

**Quy tắc.** Ở bước $t$, chỉ số của $a$ là $\bar r(a)+c_{\mathrm{ucb}}\sqrt{\ln t/N(a)}$; số hạng thứ hai lớn khi $a$ ít được chọn. Hành động có chỉ số lớn nhất được chọn.

**Chỉ số.**

- hành động 1: $0{,}6+\sqrt{2{,}1972/6}=0{,}6+0{,}6051=1{,}2051$;
- hành động 2: $0{,}4+\sqrt{2{,}1972/2}=0{,}4+1{,}0481=1{,}4481$.

**Diễn giải.** Hành động 2 được chọn dù trung bình thấp hơn, vì hai mẫu chưa đủ để loại nó.

**Kiểm tra lại.** $\sqrt{0{,}3662}=0{,}6051$ và $\sqrt{1{,}0986}=1{,}0481$.
:::

::: definition Định nghĩa 11.23 (Quy tắc cận tin cậy trên)
Trong bài toán chọn lặp lại một bước với tập hành động hữu hạn, ở bước $t\ge1$, gọi $N(a)$ là số lần đã chọn $a$ trước bước $t$ và $\bar r(a)$ là trung bình mẫu của các phần thưởng đó. Với hằng số $c_{\mathrm{ucb}}>0$, **quy tắc cận tin cậy trên** (upper confidence bound, UCB) chọn
$$\begin{aligned}A_t\in\arg\max_a\Bigl[&\bar r(a)\\&+c_{\mathrm{ucb}}\sqrt{\frac{\ln t}{N(a)}}\Bigr],\end{aligned}\tag{3.2}$$
với quy ước hành động có $N(a)=0$ có chỉ số bằng $+\infty$.
:::

Số hạng thứ hai giảm khi $N(a)$ tăng và tăng chậm theo $t$ khi $a$ không được chọn. Quy tắc (3.2) là công thức (2.10) của Sutton và Barto (2018, §2.7, tr. 35). **UCB1** của Auer, Cesa-Bianchi và Fischer (2002, Hình 1, tr. 237) khác (3.2) ở ba điểm:

- $c_{\mathrm{ucb}}=\sqrt2$;
- $\ln(t-1)$ thay $\ln t$, với $t-1$ là tổng số lần đã chọn;
- bước khởi tạo chọn mỗi hành động một lần, ứng với quy ước $N(a)=0$.

Szepesvári (2010, §4.2.1) viết cùng quy tắc cho phần thưởng trong $[-R,R]$.

::: theorem Định lý 11.24 (Bảo đảm của UCB1)
**Giả thiết.** Có $K>1$ hành động; phần thưởng của mỗi hành động độc lập, cùng phân phối theo thời gian, độc lập giữa các hành động, nhận giá trị trong $[0,1]$. Đặt $\nu_a$ là kỳ vọng phần thưởng của $a$, $\nu^*=\max_a\nu_a$, $\Delta_a=\nu^*-\nu_a$, $N_t(a)$ là số lần chọn $a$ trong $t$ bước đầu.

**Kết luận.**

- (i) Với mọi hành động $a$ có $\Delta_a>0$, số lần chọn kỳ vọng thỏa $\mathbb E[N_t(a)]\le\dfrac{8\ln t}{\Delta_a^2}+1+\dfrac{\pi^2}3$.
- (ii) Hối tiếc (regret) kỳ vọng sau $t$ bước thỏa
$$\begin{aligned}&\nu^*t-\textstyle\sum_a\nu_a\mathbb E[N_t(a)]\\&\quad\le8\textstyle\sum_{a:\Delta_a>0}\dfrac{\ln t}{\Delta_a}\\&\qquad+\Bigl(1+\dfrac{\pi^2}3\Bigr)\textstyle\sum_a\Delta_a.\end{aligned}$$

**Điều kiện áp dụng.** Quy tắc là UCB1: (3.2) với $c_{\mathrm{ucb}}=\sqrt2$, $\ln(t-1)$ ở chỗ $\ln t$, và bước khởi tạo chọn mỗi hành động một lần.

**Phạm vi.** Không áp dụng khi phân phối phần thưởng đổi theo thời gian (Sutton và Barto, 2018, tr. 36). Chứng minh nằm ngoài phạm vi học phần; xem Auer, Cesa-Bianchi và Fischer (2002, Định lý 1, tr. 237 và chứng minh tr. 242–243).
:::

Theo (ii), hối tiếc tăng theo $\ln t$. Hối tiếc bằng $\sum_a\Delta_a\,\mathbb E[N_t(a)]$, vì mỗi lần chọn $a$ mất $\Delta_a$ phần thưởng kỳ vọng; nhân chặn (i), vốn có $\Delta_a^2$ ở mẫu số, với $\Delta_a$ cho số hạng $8\ln t/\Delta_a$ của (ii).

Ý tưởng chứng minh: khi $a$ đã được chọn ít nhất $8\ln t/\Delta_a^2$ lần, bất đẳng thức Chernoff–Hoeffding chặn xác suất chỉ số của $a$ vượt chỉ số của hành động tốt nhất.

Hai giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "phân phối không đổi": nếu từ bước $1\,000$ hành động 2 tốt lên, $N(2)$ đã lớn làm số hạng thăm dò nhỏ, và quy tắc chậm phát hiện thay đổi.
- Bỏ "phần thưởng trong $[0,1]$": với phần thưởng trong $[0,100]$, hằng số $\sqrt2$ quá nhỏ so với độ phân tán.

**Trong thực hành.** Khi quy tắc này chọn hành động cho các mô phỏng tại một trạng thái, mỗi "phần thưởng" là lợi tức của một mô phỏng. Lợi tức đó phụ thuộc các lựa chọn ở bước sau, vốn đang thay đổi, nên giả thiết "cùng phân phối theo thời gian" không thỏa (Kocsis và Szepesvári, 2006, §2.2).

<!-- note-topic-id: lec-11-topic-13 -->
### 3.3 Bốn pha của tìm kiếm theo cây Monte Carlo

Thuật toán rollout chỉ giữ trung bình lợi tức của các hành động ở gốc; kết quả của các mô phỏng trước không hướng các mô phỏng sau (Sutton và Barto, 2018, tr. 185).

Một cách trực quan, tác tử giữ một cây gốc $\mathrm F$ với bốn quy tắc:

- mỗi cạnh ghi số lần thăm và tổng lợi tức;
- trong cây, cạnh được chọn bằng chỉ số cận tin cậy trên;
- ngoài cây, mô phỏng theo $\pi_0$;
- sau mỗi mô phỏng, cây mọc thêm một nút.

Ví dụ sau là một vòng như vậy.

::: example Ví dụ 11.16 (Một vòng tìm kiếm theo cây Monte Carlo tại $\mathrm F$, $c_{\mathrm{ucb}}=1$)
**Dữ kiện.** Mê cung hai phòng, mô hình mẫu đúng, chính sách cơ sở $\pi_0$ ngẫu nhiên đều, $\gamma=0{,}9$, độ sâu cắt $D=20$. Giả sử lần chọn $\uparrow$ và lần chọn $\leftarrow$ trước đó đều trượt, nên $\mathrm B$ và $\mathrm E$ ở độ sâu $1$ chưa có trong cây. Sau tám vòng lặp, các lợi tức đã nhận là $\gamma,\gamma^2,\gamma^6,\gamma^6$ qua $\rightarrow$; $\gamma^4,\gamma^6$ qua $\downarrow$; $\gamma^{11}$ qua $\uparrow$; $\gamma^{15}$ qua $\leftarrow$, nên thống kê các cạnh gốc là:

| cạnh | $N(\mathrm F,a)$ | $W(\mathrm F,a)$ | $\bar Q(\mathrm F,a)$ | $\sqrt{\ln8/N}$ | chỉ số |
|---|---:|---:|---:|---:|---:|
| $\rightarrow$ | $4$ | $2{,}7729$ | $0{,}6932$ | $0{,}7210$ | $1{,}4142$ |
| $\downarrow$ | $2$ | $1{,}1875$ | $0{,}5938$ | $1{,}0197$ | $1{,}6134$ |
| $\uparrow$ | $1$ | $0{,}3138$ | $0{,}3138$ | $1{,}4420$ | $1{,}7558$ |
| $\leftarrow$ | $1$ | $0{,}2059$ | $0{,}2059$ | $1{,}4420$ | $1{,}6479$ |

với $N(\mathrm F)=8$.

**Chọn.** Cạnh $\uparrow$ có chỉ số lớn nhất, $1{,}7558$.

**Mở rộng.** Giả sử mô hình mẫu trả $\mathrm B$ cho $(\mathrm F,\uparrow)$, xác suất $0{,}8$; cây thêm nút $\mathrm B$ với mọi thống kê bằng $0$.

**Mô phỏng.** Từ $\mathrm B$, theo $\pi_0$; giả sử dãy là $\mathrm B\xrightarrow{\downarrow}\mathrm F\xrightarrow{\rightarrow}\mathrm K\xrightarrow{\rightarrow}\mathrm Z$, không trượt. Tính từ cạnh gốc, phần thưởng là $0,0,0,1$, nên $G=\gamma^3=0{,}729$; bốn bước ít hơn $D$, nên không bị cắt.

**Cập nhật ngược.**

- $N(\mathrm F,\uparrow)=2$, $W(\mathrm F,\uparrow)=0{,}3138+0{,}729=1{,}0428$, $\bar Q(\mathrm F,\uparrow)=0{,}5214$;
- $N(\mathrm F)=9$;
- nút $\mathrm B$ giữ mọi thống kê bằng $0$, kể cả $N(\mathrm B)=0$, vì chưa cạnh nào ra từ $\mathrm B$ được đi trong cây; đoạn mô phỏng ngoài cây không được lưu.

**Hành động thật.** Nếu hết ngân sách, tác tử chọn cạnh có $N$ lớn nhất: $\rightarrow$, $N=4$.

**Kiểm tra lại.** $\ln8/4=0{,}5199$ và $\sqrt{0{,}5199}=0{,}7210$; $0{,}9+0{,}81+2\cdot0{,}531441=2{,}772882$; $1{,}042811/2=0{,}5214$.
:::

![Bốn khung tại gốc F: chọn cạnh mũi tên lên, chỉ số 1,7558, ba dòng dưới mỗi cạnh là N, Q trung bình, chỉ số UCT; mở rộng nút B; mô phỏng B, F, K, Z, lợi tức 0,729; cập nhật ngược N bằng 2, W bằng 1,0428, Q trung bình 0,5214, N của F bằng 9, N của B bằng 0.](img/lec-11/mcts-bon-pha.svg)

Hình đọc từ trái sang phải theo bốn pha của Ví dụ 11.16; đoạn chấm ngoài cây chỉ góp lợi tức $0{,}729$ rồi bị bỏ.

::: definition Định nghĩa 11.25 (Cây tìm kiếm, chính sách cây, thống kê cạnh)
Cho trạng thái gốc $s_0$ và một mô hình mẫu.

- **Cây tìm kiếm** gồm các nút, mỗi nút là một trạng thái gặp trong mô phỏng ở một độ sâu tính từ gốc; mỗi cạnh $(s,a)$ ứng với $a\in\mathcal A(s)$.
- **Thống kê cạnh**: số lần đi qua $N(s,a)$, tổng lợi tức $W(s,a)$ tính từ cạnh đó, trung bình $\bar Q=W/N$; $N(s)=\sum_aN(s,a)$.
- **Chính sách cây** (tree policy) chọn tại nút $s$ cạnh có **chỉ số UCT** lớn nhất (UCT: upper confidence bounds applied to trees, cận tin cậy trên áp cho cây),
$$\bar Q(s,a)+c_{\mathrm{ucb}}\sqrt{\frac{\ln N(s)}{N(s,a)}},\tag{3.3}$$
với cạnh có $N(s,a)=0$ được chọn trước. Ngoài cây, pha mô phỏng chọn hành động theo chính sách cơ sở $\pi_0$ của Thuật toán 11.20.
:::

Chỉ số (3.3) là quy tắc (3.2) áp ở mỗi nút, với $N(s)$, số lần đã qua nút, ở vị trí $t-1$ như UCB1. Kocsis và Szepesvári (2006) viết số hạng thăm dò là $2C_p\sqrt{\ln t/k}$, với $t$ là số lần thăm nút và $k$ là số lần chọn cạnh, ứng với $c_{\mathrm{ucb}}=2C_p$ (§2.2), và coi nút là cặp (trạng thái, độ sâu) như Định nghĩa 11.25 (§2.3). Sutton và Barto (2018, §8.11, Hình 8.10) gọi chính sách ngoài cây là rollout policy; ở đây đó là chính sách cơ sở $\pi_0$.

::: algorithm Thuật toán 11.26 (Tìm kiếm theo cây Monte Carlo với UCT)
**Đầu vào.** Trạng thái hiện tại $s_0$; mô hình mẫu; chính sách cơ sở $\pi_0$; $\gamma\in[0,1)$.

**Đầu ra.** Hành động $A_t$ tại $s_0$.

**Giả thiết.** Tập hành động hữu hạn tại mọi trạng thái; mô hình mẫu trả $(R,S')$ cho mọi cặp hợp lệ.

**Khởi tạo.** Cây chỉ có nút gốc $s_0$, mọi thống kê bằng $0$.

**Tham số.** Hằng số $c_{\mathrm{ucb}}>0$; ngân sách số vòng lặp; độ sâu cắt $D$.

**Lặp, mỗi vòng một mô phỏng:**

1. **Chọn.** Từ gốc, đi xuống theo (3.3), gọi mô hình mẫu ở mỗi cạnh, tới một trạng thái chưa có trong cây, trạng thái kết thúc, hoặc độ sâu $D$.
2. **Mở rộng.** Nếu trạng thái đó không kết thúc và độ sâu nhỏ hơn $D$, thêm nó vào cây với thống kê bằng $0$.
3. **Mô phỏng.** Từ nút mới, theo $\pi_0$, tới trạng thái kết thúc hoặc tới tổng độ sâu $D$.
4. **Cập nhật ngược** (backup). Với mỗi cạnh $(s,a)$ đã đi trong cây ở độ sâu $j$, với $G_j$ là lợi tức chiết khấu tính từ cạnh đó: $N(s,a)\leftarrow N(s,a)+1$, $W(s,a)\leftarrow W(s,a)+G_j$, $N(s)\leftarrow N(s)+1$.

**Điều kiện dừng.** Hết ngân sách vòng lặp; trả $A_t$ là cạnh gốc có $N(s_0,a)$ lớn nhất, hoặc có $\bar Q(s_0,a)$ lớn nhất.

**Chi phí mỗi bước.** Mỗi vòng gọi mô hình nhiều nhất $D$ lần; bộ nhớ tăng một nút.
:::

Bốn bước là bốn pha của Sutton và Barto (2018, §8.11, tr. 187): chọn (selection), mở rộng (expansion), mô phỏng (simulation), cập nhật ngược (backup). Sau khi thực hiện $A_t$, cây con của trạng thái kế có thể được giữ lại. Khi cây chỉ có gốc và chính sách cây chọn đều, thuật toán trở về thuật toán rollout.

**Trong thực hành.** Mô hình mẫu phải nhanh (Sutton và Barto, 2018, tr. 185). Thống kê chỉ lưu ở các nút quanh trạng thái hiện tại, nên không cần xấp xỉ hàm giá trị trên toàn không gian (tr. 188).

<!-- note-topic-id: lec-11-topic-14 -->
### 3.4 Bảo đảm của UCT và giá trị học được

Ở gốc của Thuật toán 11.26, lợi tức mô phỏng đổi theo thời gian, nên Định lý 11.24 không áp dụng trực tiếp. Trên mê cung, do trượt, một lượt còn có thể dài tùy ý, nên mô phỏng bị cắt ở độ sâu $D$.

Một cách trực quan, ở mỗi nút UCT giải một bài toán chọn lặp lại có trung bình trôi dần, vì lựa chọn ở các nút bên dưới đang thay đổi. Khi các nút sâu hơn ổn định, trung bình ở nút trên cũng ổn định, và quy tắc cận tin cậy trên ở gốc dồn dần mô phỏng vào hành động tốt nhất của bài toán cắt. Phép cắt ở độ sâu $D$ chỉ bỏ phần lợi tức sau bước $D$, phần này có hệ số $\gamma^D$.

Với chính sách $\pi$, đặt
$$\begin{aligned}v^D_\pi(s)&=\mathbb E_\pi\Bigl[\sum_{t=0}^{\min(D,T)-1}\gamma^tR_{t+1}\\&\qquad\Bigm|S_0=s\Bigr],\\v^D_*(s)&=\sup_\pi v^D_\pi(s),\end{aligned}$$
là giá trị của bài toán cắt ở độ sâu $D$, cận trên lấy trên mọi chính sách.

::: theorem Định lý 11.27 (Tính nhất quán của UCT cho bài toán cắt)
**Giả thiết.** Tập hành động hữu hạn; mô hình mẫu đúng; bài toán cắt ở độ sâu $D$.

- Với (a): mỗi phần thưởng nằm trong $[0,1]$, nên lợi tức của bài toán cắt nằm trong $[0,D]$. Thuật toán là UCT của Kocsis và Szepesvári (2006): chỉ số (3.3) áp ở mọi nút (trạng thái, độ sâu) tới độ sâu $D$, mỗi vòng đi từ gốc tới độ sâu $D$ hoặc tới trạng thái kết thúc, với $c_{\mathrm{ucb}}=\sqrt2\,D$, tức hệ số thăm dò của UCB1 nhân $D$, tương đương chia mọi phần thưởng cho $D$ rồi dùng UCB1. Hành động tối ưu của bài toán cắt tại gốc là duy nhất.
- Với (b): phần thưởng không âm, và lợi tức của mọi lượt, cắt hay không, nằm trong $[0,1]$.

**Kết luận.**

- (a) Xác suất UCT chọn ở gốc một hành động khác hành động tối ưu của bài toán cắt tiến về $0$ khi số vòng lặp tiến ra vô hạn.
- (b) Với mọi chính sách Markov dừng $\pi$ và mọi $s$,
$$\begin{aligned}0\le v_\pi(s)-v^D_\pi(s)&\le\gamma^D,\\0\le v_*(s)-v^D_*(s)&\le\gamma^D.\end{aligned}$$

**Điều kiện áp dụng.** Mê cung hai phòng thỏa giả thiết về phần thưởng của (a) và (b), vì phần thưởng khác $0$ duy nhất là $+1$ khi vào $\mathrm Z$. Với $D=20$, $\gamma^{20}=0{,}1216$, và (a) cần $c_{\mathrm{ucb}}=20\sqrt2=28{,}28$.

**Phạm vi.** Kết luận (a) là tiệm cận, không cho số vòng lặp cần thiết. Khi mô hình sai, định lý chỉ nói về bài toán cắt trên MDP của mô hình. Hệ số $c_{\mathrm{ucb}}=1$ của Ví dụ 11.16 không thỏa giả thiết của (a).
:::

::: proof
**Phần (a).** Chứng minh nằm ngoài phạm vi học phần. Kocsis và Szepesvári (2006, Định lý 6) cho phác thảo; Kocsis, Szepesvári và Willemson (2006, Định lý 7) cho chứng minh đầy đủ trên cây trò chơi có phần thưởng ở lá. Ý tưởng: quy nạp theo $D$; với $D=1$ là UCB1; với $D>1$, ở gốc UCT là UCB1 trên một dãy lợi tức không dừng có kỳ vọng hội tụ nhờ giả thiết quy nạp.

**Phần (b), bước 1 (hiệu của hai giá trị).** Với $\pi$ Markov dừng, hiệu hai lợi tức là phần thưởng từ bước $D$, chỉ có khi $D<T$:
$$\begin{aligned}&v_\pi(s)-v^D_\pi(s)\\&\quad=\mathbb E_\pi\Bigl[\mathbb 1\{D<T\}\\&\qquad\times\textstyle\sum_{t\ge D}\gamma^tR_{t+1}\Bigm|S_0=s\Bigr]\\&\quad=\gamma^D\,\mathbb E_\pi\bigl[\mathbb 1\{D<T\}\,v_\pi(S_D)\\&\qquad\bigm|S_0=s\bigr].\end{aligned}$$
Đẳng thức thứ hai dùng Bổ đề 03.20.

**Bước 2 (chặn hai phía cho $\pi$).** Vì lợi tức nằm trong $[0,1]$, $0\le v_\pi(S_D)\le1$, nên vế phải của Bước 1 nằm trong $[0,\gamma^D]$.

**Bước 3 (chặn dưới cho $v_*$).** Với mọi $\pi$, phần thưởng không âm nên lợi tức cắt không vượt lợi tức đầy đủ trên từng lượt, do đó $v^D_\pi(s)\le v_\pi(s)\le v_*(s)$ (Định lý 04.25(b)); lấy cận trên theo $\pi$ được $v^D_*(s)\le v_*(s)$.

**Bước 4 (chặn trên cho $v_*$).** Gọi $\pi_*$ là một chính sách tối ưu Markov dừng xác định (Định lý 04.25(b)). Theo Bước 2 với $\pi=\pi_*$,
$$\begin{aligned}v_*(s)-v^D_*(s)&\le v_{\pi_*}(s)-v^D_{\pi_*}(s)\\&\le\gamma^D,\end{aligned}$$
trong đó bất đẳng thức đầu dùng $v^D_*(s)\ge v^D_{\pi_*}(s)$. $\square$
:::

Trên mê cung với $D=20$, (b) cho $0\le v_*-v^D_*\le0{,}1216$. Kocsis và Szepesvári (2006, đoạn sau chứng minh Định lý 6) nêu kết quả mở rộng được cho MDP chiết khấu bằng cách cắt ở một chân trời hiệu dụng. Thuật toán 11.26 là biến thể thực hành của UCT: cây mọc mỗi vòng một nút, và ngoài cây mô phỏng theo $\pi_0$. Kết luận (a) không được chứng minh cho biến thể này.

Các giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "lợi tức trong $[0,1]$": với phần thưởng $+10$ khi vào $\mathrm Z$, chặn của (b) thành $10\gamma^D$ (Bước 2).
- Bỏ "phần thưởng không âm": lợi tức cắt có thể lớn hơn lợi tức đầy đủ, và Bước 3 không còn.
- Bỏ "mô hình đúng": UCT hội tụ tới hành động tối ưu của MDP của mô hình, không của môi trường thật.

::: remark Nhận xét 11.28 (Xác suất tiên nghiệm và giá trị học được trong AlphaGo Zero)
AlphaGo Zero bỏ pha mô phỏng: một mạng nơ-ron cho giá trị nút lá thay lợi tức mô phỏng, và cho xác suất tiên nghiệm $P(s,a)$ dùng trong chính sách cây (Sutton và Barto, 2018, §16.6.2, tr. 447–450). Chính sách cây là một biến thể của PUCT (Silver và cộng sự, 2017, phần Phương pháp, mục "Select"):
$$\begin{aligned}&a\in\arg\max_a\bigl[\bar Q(s,a)\\&\qquad+U(s,a)\bigr],\\&U(s,a)=c_{\mathrm{puct}}P(s,a)\\&\qquad\times\frac{\sqrt{\sum_{a'}N(s,a')}}{1+N(s,a)},\end{aligned}$$
với hằng số $c_{\mathrm{puct}}>0$: ban đầu ưu tiên xác suất tiên nghiệm cao, về sau ưu tiên giá trị cao.
:::

**Trong thực hành.** Khi trạng thái chỉ quan sát được một phần hoặc mô hình là một mạng học được, Mệnh đề 11.22 và Định lý 11.27 mất giả thiết "mô hình đúng". Giá trị $q_{\pi_0}$ tính trên mô hình khi đó là giá trị trên MDP của mô hình, nên Mệnh đề 11.21 chỉ so hai chính sách trên mô hình.

Như vậy, với mô hình đúng, rollout không làm giảm giá trị (Mệnh đề 11.21), và tại $\mathrm F$, $m=70$ mô phỏng mỗi hành động giữ xác suất xếp $\downarrow$ trên $\rightarrow$ không quá $0{,}0496$ (Mệnh đề 11.22, Ví dụ 11.14). UCT nhất quán cho bài toán cắt (Định lý 11.27). Cả hai cần tập hành động hữu hạn. Với hành động liên tục, như độ dịch chuyển lệnh cho một chiếc xe trên đường ray, cây không liệt kê được các cạnh. Nếu mô hình khả vi, đạo hàm của chi phí theo hành động chỉ ra hướng sửa kế hoạch.

---

## 4. Tối ưu kế hoạch dựa trên đạo hàm

<!-- note-topic-id: lec-11-topic-15 -->
### 4.1 Bài toán tối ưu kế hoạch trên mô hình khả vi

Một chiếc xe trên đường ray cách vị trí cần giữ hai đơn vị; mỗi bước, tác tử ra lệnh một độ dịch chuyển bất kỳ trên trục số.

Một cách trực quan, khi có mô hình, tác tử chọn cả chuỗi hành động một lần: chạy thử chuỗi trên mô hình, đọc tổng chi phí, rồi sửa chuỗi cho chi phí giảm. Để làm rõ, xem ví dụ sau.

::: example Ví dụ 11.17 (Xe trên đường ray: kế hoạch không làm gì)
**Dữ kiện.** Vị trí $x_t\in\mathbb R$ của xe, mốc $0$ là vị trí cần giữ; hành động $u_t\in\mathbb R$ là độ dịch chuyển lệnh cho bước $t$. Mô hình $\hat f(x,u)=x+u$. Chi phí mỗi bước $c(x_{t+1},u_t)=x_{t+1}^2+u_t^2$; chân trời $h=2$; không chiết khấu; $x_0=2$. Chi phí của kế hoạch $(u_0,u_1)$ trên mô hình là
$$\begin{aligned}&J(u_0,u_1)=x_1^2+u_0^2+x_2^2+u_1^2,\\&x_1=x_0+u_0,\quad x_2=x_1+u_1.\end{aligned}$$

**Tính.** Với $(u_0,u_1)=(0;\,0)$: $x_1=x_2=2$, nên $J=4+0+4+0=8$.

**Kiểm tra lại.** Hai số hạng vị trí bằng $x_0^2=4$, hai số hạng hành động bằng $0$.
:::

Bài toán dùng chi phí $c\ge0$; cực tiểu tổng chi phí tương đương cực đại tổng phần thưởng $-c$.

::: definition Định nghĩa 11.29 (Bài toán tối ưu kế hoạch chân trời $h$, phép bắn)
Cho trạng thái đầu $x_0\in\mathbb R$, mô hình tất định $\hat f:\mathbb R\times\mathbb R\to\mathbb R$, chi phí mỗi bước $c:\mathbb R\times\mathbb R\to\mathbb R_{\ge0}$ và chân trời $h\ge1$. **Bài toán tối ưu kế hoạch** (trajectory optimization) là
$$\begin{aligned}&\min_{u_0,\dots,u_{h-1}\in\mathbb R}J(u_{0:h-1}),\\&J=\sum_{t=0}^{h-1}c(x_{t+1},u_t),\end{aligned}\tag{4.1}$$
trong đó các trạng thái được thế bằng $x_{t+1}=\hat f(x_t,u_t)$ từ $x_0$. Cách viết $J$ chỉ theo chuỗi hành động, với trạng thái tính bằng mô hình, gọi là **phép bắn** (shooting), hay phép bắn đơn (single shooting).
:::

Lời giải của (4.1) là một chuỗi hành động cho một trạng thái đầu, gọi là kế hoạch vòng hở (open-loop), khác một chính sách Markov dừng (Định nghĩa 03.13). Ví dụ 11.17 là (4.1) với $h=2$. Giải (4.1) bằng đạo hàm của $J$ theo chuỗi hành động là tối ưu kế hoạch dựa trên đạo hàm (gradient-based planning).

<!-- note-topic-id: lec-11-topic-16 -->
### 4.2 Đạo hàm qua mô hình

Muốn hạ gradient trên (4.1), tác tử cần $\partial J/\partial u_t$; mỗi $u_t$ ảnh hưởng tới chi phí bước $t$ và, qua mô hình, mọi trạng thái sau.

Một cách trực quan, mỗi $u_t$ đẩy xe một đoạn, và đoạn đẩy đó còn nằm trong mọi vị trí sau; đạo hàm theo $u_t$ cộng ảnh hưởng trực tiếp lên chi phí bước $t$ với ảnh hưởng truyền qua các vị trí sau. Với $h=2$, ta khai triển $J$ rồi lấy đạo hàm, như ví dụ sau.

::: example Ví dụ 11.18 (Một bước hạ gradient)
**Dữ kiện.** Xe trên đường ray (Ví dụ 11.17): $\hat f(x,u)=x+u$, $c=x_{t+1}^2+u_t^2$, $h=2$, $x_0=2$, kế hoạch ban đầu $(0;\,0)$ với $J=8$; tốc độ học $\eta=0{,}1$.

**Khai triển.** $J=(x_0+u_0)^2+u_0^2+(x_0+u_0+u_1)^2+u_1^2$, nên

- $\partial J/\partial u_0=2(x_0+u_0)+2u_0+2(x_0+u_0+u_1)$, tại $(0;\,0)$ bằng $4+0+4=8$;
- $\partial J/\partial u_1=2(x_0+u_0+u_1)+2u_1$, tại $(0;\,0)$ bằng $4$.

**Bước hạ gradient.** $u\leftarrow(0;\,0)-0{,}1\,(8;\,4)=(-0{,}8;\,-0{,}4)$. Khi đó $x_1=1{,}2$, $x_2=0{,}8$, và $J=1{,}44+0{,}64+0{,}64+0{,}16=2{,}88$.

**Kiểm tra lại.** $J$ giảm từ $8$ xuống $2{,}88$.
:::

Với $h$ lớn, lan truyền ngược (backpropagation) qua đồ thị tính của $J$ cho mọi đạo hàm trong một lượt ngược.

::: proposition Mệnh đề 11.30 (Gradient theo chuỗi hành động bằng truy hồi ngược)
**Giả thiết.** $\hat f$ và $c$ khả vi liên tục; $x_1,\dots,x_h$ tính từ $x_0$ và $u_{0:h-1}$ bằng $x_{t+1}=\hat f(x_t,u_t)$.

**Kết luận.** Định nghĩa $\lambda_t$ bằng **truy hồi ngược** (backward recursion)
$$\begin{aligned}\lambda_h&=\frac{\partial c(x_h,u_{h-1})}{\partial x_h},\\\lambda_t&=\frac{\partial c(x_t,u_{t-1})}{\partial x_t}\\&\quad+\lambda_{t+1}\frac{\partial\hat f(x_t,u_t)}{\partial x_t},\\&\quad t=h-1,\dots,1.\end{aligned}\tag{4.2}$$
Khi đó, với $t=0,\dots,h-1$,
$$\begin{aligned}\frac{\partial J}{\partial u_t}&=\frac{\partial c(x_{t+1},u_t)}{\partial u_t}\\&\quad+\lambda_{t+1}\frac{\partial\hat f(x_t,u_t)}{\partial u_t},\end{aligned}\tag{4.3}$$
trong đó $\partial c/\partial u_t$ là đạo hàm riêng theo đối số thứ hai.

**Điều kiện áp dụng.** Các trạng thái $x_1,\dots,x_h$ của lượt xuôi được lưu lại; khi đó một lượt xuôi và một lượt ngược cần $O(h)$ lần tính đạo hàm của $\hat f$ và $c$.

**Phạm vi.** Gradient (4.3) tính trên mô hình $\hat f$, không trên hệ thật. Khi $\hat f$ phi tuyến, $J$ có thể không lồi, và điểm có gradient bằng $0$ có thể chỉ là một điểm dừng địa phương.
:::

::: proof
**Bước 1 (chi phí còn lại).** Với $t=1,\dots,h$ và các hành động cố định, đặt
$$\begin{aligned}\Lambda_t(x_t)&=c(x_t,u_{t-1})\\&\quad+\Lambda_{t+1}\bigl(\hat f(x_t,u_t)\bigr),\\\Lambda_{h+1}&\equiv0.\end{aligned}$$
Cần chứng minh $\lambda_t=\mathrm d\Lambda_t/\mathrm dx_t$.

**Bước 2 (quy nạp ngược).** Với $t=h$, $\Lambda_h=c(x_h,u_{h-1})$, nên $\mathrm d\Lambda_h/\mathrm dx_h=\lambda_h$. Giả sử $\mathrm d\Lambda_{t+1}/\mathrm dx_{t+1}=\lambda_{t+1}$. Quy tắc dây chuyền cho
$$\begin{aligned}\frac{\mathrm d\Lambda_t}{\mathrm dx_t}&=\frac{\partial c(x_t,u_{t-1})}{\partial x_t}\\&\quad+\lambda_{t+1}\frac{\partial\hat f(x_t,u_t)}{\partial x_t}\\&=\lambda_t.\end{aligned}$$

**Bước 3 (đạo hàm theo $u_t$).** Tách $J=\sum_{j<t}c(x_{j+1},u_j)+\Lambda_{t+1}(x_{t+1})$, với $x_{t+1}=\hat f(x_t,u_t)$. Tổng đầu không phụ thuộc $u_t$, vì $x_1,\dots,x_t$ chỉ phụ thuộc $u_0,\dots,u_{t-1}$. Trong $\Lambda_{t+1}(x_{t+1})=c(x_{t+1},u_t)+\Lambda_{t+2}(x_{t+2})$, $u_t$ tác động theo hai đường: trực tiếp qua đối số thứ hai của $c$, và qua $x_{t+1}=\hat f(x_t,u_t)$. Quy tắc dây chuyền cho
$$\begin{aligned}\frac{\partial J}{\partial u_t}&=\frac{\partial c(x_{t+1},u_t)}{\partial u_t}\\&\quad+\frac{\mathrm d\Lambda_{t+1}}{\mathrm dx_{t+1}}\frac{\partial\hat f(x_t,u_t)}{\partial u_t},\end{aligned}$$
và Bước 2 cho (4.3). $\square$
:::

Mệnh đề là lan truyền ngược viết cho một chuỗi thời gian; $\lambda_t$ là đạo hàm của chi phí còn lại theo trạng thái. Với trạng thái và hành động là vector, $\partial\hat f/\partial x_t$, $\partial\hat f/\partial u_t$ là ma trận Jacobi. Khi mô hình không khả vi, như mô hình bảng hay trình mô phỏng hộp đen, mệnh đề không dùng được.

**Bản truy hồi ngược của Ví dụ 11.18.** Với $\hat f(x,u)=x+u$, $\partial\hat f/\partial x=\partial\hat f/\partial u=1$. Tại $(0;\,0)$: $x_1=x_2=2$; $\lambda_2=2x_2=4$; $\lambda_1=2x_1+\lambda_2=8$; $\partial J/\partial u_1=2u_1+\lambda_2=4$; $\partial J/\partial u_0=2u_0+\lambda_1=8$. Gradient $(8;\,4)$ trùng kết quả khai triển.

::: algorithm Thuật toán 11.31 (Tối ưu kế hoạch bằng hạ gradient)
**Đầu vào.** $x_0$; mô hình khả vi $\hat f$; chi phí khả vi $c$; chân trời $h$.

**Đầu ra.** Kế hoạch $u_{0:h-1}$.

**Giả thiết.** $\hat f$ và $c$ khả vi liên tục.

**Khởi tạo.** Kế hoạch ban đầu $u_{0:h-1}$, chẳng hạn $u\equiv0$.

**Tham số.** Tốc độ học $\eta>0$; ngưỡng dừng $\theta>0$; ngân sách số vòng.

**Lặp:**

1. Lượt xuôi: tính $x_{t+1}=\hat f(x_t,u_t)$ với $t=0,\dots,h-1$ và $J$.
2. Lượt ngược: tính $\lambda_h,\dots,\lambda_1$ theo (4.2) và $\nabla J$ theo (4.3).
3. Cập nhật $u\leftarrow u-\eta\nabla J$.

**Điều kiện dừng.** $\lVert\nabla J\rVert\le\theta$ hoặc hết ngân sách.

**Chi phí mỗi bước.** $O(h)$ lần gọi $\hat f$ và $O(h)$ lần tính đạo hàm của $\hat f$, $c$.
:::

::: example Ví dụ 11.19 (Kế hoạch tối ưu)
**Dữ kiện.** Xe trên đường ray, $\hat f(x,u)=x+u$, $c=x_{t+1}^2+u_t^2$, $h=2$, $x_0=2$. Hai đạo hàm riêng của $J$:

- $\partial J/\partial u_0=2(x_0+u_0)+2u_0+2(x_0+u_0+u_1)$;
- $\partial J/\partial u_1=2(x_0+u_0+u_1)+2u_1$.

**Điểm dừng.** Với $x_0=2$, hai đạo hàm bằng $0$ cho $4+3u_0+u_1=0$ và $2+u_0+2u_1=0$. Từ phương trình sau, $u_0=-2-2u_1$; thế vào phương trình đầu được $-2-5u_1=0$, nên $u_1=-0{,}4$ và $u_0=-1{,}2$.

**Chi phí.** $x_1=0{,}8$, $x_2=0{,}4$, $J^*=0{,}64+1{,}44+0{,}16+0{,}16=2{,}40$.

**Cực tiểu toàn cục.** $J$ là hàm bậc hai với ma trận Hessian $\begin{pmatrix}6&2\\2&4\end{pmatrix}$, có định thức $20>0$ và vết dương, nên xác định dương; điểm dừng là cực tiểu toàn cục.

**Kiểm tra lại.** Bước hạ gradient của Ví dụ 11.18 đưa $J$ về $2{,}88$, còn cách tối ưu $0{,}48$.
:::

PILCO (probabilistic inference for learning control) tính giải tích gradient của chi phí dài hạn theo tham số chính sách qua mô hình quá trình Gauss (Gaussian process) (Deisenroth và Rasmussen, 2011, §2.3).

**Trong thực hành.** Khi $\hat f$ là một mạng nơ-ron, lượt ngược của Thuật toán 11.31 là lan truyền ngược tự động qua $h$ bản của mạng. Mệnh đề 11.30 cho gradient của chi phí tính trên mô hình. Khi mô hình sai dọc quỹ đạo dự báo, gradient đó không bảo đảm chi phí trên môi trường thật giảm.

<!-- note-topic-id: lec-11-topic-17 -->
### 4.3 Điều khiển dự báo theo chân trời lùi

Kế hoạch $(-1{,}2;\,-0{,}4)$ của Ví dụ 11.19 tính một lần từ $x_0=2$; nếu xe trôi khác dự báo, bước thứ hai vẫn thực hiện $u_1=-0{,}4$.

Một cách trực quan, tác tử chỉ thực hiện hành động đầu của kế hoạch, quan sát vị trí thật rồi lập kế hoạch lại, nên sai lệch ở bước trước được tính tới ngay ở bước sau, như ví dụ sau.

::: example Ví dụ 11.20 (Điều khiển dự báo trên mô hình)
**Dữ kiện.** Xe trên đường ray, mô hình $\hat f(x,u)=x+u$, $c=x_{t+1}^2+u_t^2$, $h=2$; kế hoạch tối ưu từ $x_0=2$ là $(-1{,}2;\,-0{,}4)$ (Ví dụ 11.19).

**Luật lập kế hoạch lại.** Với trạng thái đầu $x_0$ tổng quát, hai đạo hàm bằng $0$ cho $2x_0+3u_0+u_1=0$ và $x_0+u_0+2u_1=0$. Hệ này tuyến tính thuần nhất theo $(x_0,u_0,u_1)$, nên nghiệm tỉ lệ với $x_0$: $u_1=-0{,}2x_0$, $u_0=-0{,}6x_0$. Lập kế hoạch lại từ vị trí $x_t$ và chỉ thực hiện hành động đầu cho luật $u_t=-0{,}6x_t$.

**Quỹ đạo khi hệ thật trùng mô hình.** $x_{t+1}=x_t-0{,}6x_t=0{,}4x_t$: $2;\ 0{,}8;\ 0{,}32;\ 0{,}128$. Vòng kín co với hệ số $0{,}4<1$.

**Kiểm tra lại.** Giải lại (4.1) từ $x_1=0{,}8$ cho $u^*_0=-0{,}48=-0{,}6\cdot0{,}8$, đúng luật trên; $0{,}8\cdot0{,}4=0{,}32$.
:::

::: definition Định nghĩa 11.32 (Điều khiển dự báo theo chân trời lùi)
**Điều khiển dự báo** (model predictive control, MPC), còn gọi là điều khiển theo chân trời lùi (receding horizon control), tại mỗi bước $t$:

- quan sát trạng thái thật $x_t$;
- giải bài toán (4.1) với trạng thái đầu $x_t$ và chân trời $h$, được kế hoạch $u^*_{0:h-1}(x_t)$;
- thực hiện $u_t=u^*_0(x_t)$ và bỏ phần còn lại của kế hoạch.
:::

Điều khiển dự báo là lập kế hoạch tại thời điểm quyết định (Định nghĩa 11.2) cho hành động liên tục, cùng vai với rollout và tìm kiếm theo cây (Bertsekas, 2019, §2.5.1). Ánh xạ $x_t\mapsto u^*_0(x_t)$ là một chính sách vòng kín (closed-loop); ở Ví dụ 11.20, đó là $u_t=-0{,}6x_t$. Bertsekas (2020, §3.1) chứng minh ổn định cho bài toán có ràng buộc cuối $x_{t+h}=0$ và điều kiện điều khiển được có ràng buộc. Bài toán (4.1) không có ràng buộc đó, nên với xe trên đường ray ta kiểm trực tiếp hệ số co.

::: algorithm Thuật toán 11.33 (Điều khiển dự báo)
**Đầu vào.** Môi trường; mô hình khả vi $\hat f$; chi phí $c$; chân trời $h$.

**Đầu ra.** Dãy hành động $u_0,u_1,\dots$

**Giả thiết.** Quan sát được $x_t$ tại mỗi bước.

**Khởi tạo.** Kế hoạch ban đầu cho bộ giải, chẳng hạn $u\equiv0$.

**Tham số.** Tham số của Thuật toán 11.31 ($\eta$, $\theta$, ngân sách); số bước điều khiển.

**Lặp, mỗi vòng một bước thật:**

1. Quan sát $x_t$.
2. Chạy Thuật toán 11.31 từ $x_t$, được $u^*_{0:h-1}$.
3. Thực hiện $u_t=u^*_0$ trên môi trường.

**Điều kiện dừng.** Hết số bước điều khiển.

**Chi phí mỗi bước.** Một lần chạy Thuật toán 11.31, tức số vòng hạ gradient nhân $O(h)$.
:::

Ví dụ 11.20 là Thuật toán 11.33 với bộ giải chính xác.

<!-- note-topic-id: lec-11-topic-18 -->
### 4.4 Bắn ngẫu nhiên và phương pháp entropy chéo

Thuật toán 11.31 cần mô hình khả vi, và có thể dừng ở một điểm dừng địa phương, tùy điểm khởi tạo.

Một cách trực quan, tác tử có thể chỉ dùng lượt xuôi: rút nhiều kế hoạch, đánh giá $J$ trên mô hình, giữ kế hoạch tốt, rồi rút tiếp quanh các kế hoạch tốt, như ví dụ sau.

::: example Ví dụ 11.21 (Bắn ngẫu nhiên và một vòng entropy chéo)
**Dữ kiện.** Xe trên đường ray (Ví dụ 11.17), $x_0=2$, $J^*=2{,}40$. Giả sử bốn kế hoạch ứng viên rút từ phân phối ban đầu:

| ứng viên | $(u_0;\,u_1)$ | $x_1$; $x_2$ | $J$ |
|---|---|---|---:|
| 1 | $(0;\,0)$ | $2$; $2$ | $8$ |
| 2 | $(-1;\,0)$ | $1$; $1$ | $3$ |
| 3 | $(-1;\,-0{,}5)$ | $1$; $0{,}5$ | $2{,}5$ |
| 4 | $(-2;\,0)$ | $0$; $0$ | $4$ |

**Bắn ngẫu nhiên.** Chọn ứng viên có $J$ nhỏ nhất: ứng viên 3, $J=2{,}5$, cách tối ưu $0{,}1$.

**Một vòng entropy chéo.** Giữ hai mẫu ưu tú, ứng viên 3 và 2. Trung bình mới theo từng tọa độ là $(-1;\,-0{,}25)$, độ lệch chuẩn không hiệu chỉnh (chia cho số mẫu ưu tú) theo từng tọa độ là $(0;\,0{,}25)$; vòng sau rút quanh trung bình này.

**Diễn giải.** Độ lệch chuẩn $0$ ở tọa độ $u_0$ làm phân phối suy biến: mọi mẫu của vòng sau có $u_0=-1$, trong khi $u^*_0=-1{,}2$.

**Kiểm tra lại.** Ứng viên 4: $x_1=0$, $x_2=0$, $J=0+4+0+0=4$.
:::

::: algorithm Thuật toán 11.34 (Tối ưu kế hoạch bằng phương pháp entropy chéo)
**Đầu vào.** $x_0$; mô hình $\hat f$ gọi được; chi phí $c$; chân trời $h$.

**Đầu ra.** Kế hoạch $u_{0:h-1}$.

**Giả thiết.** Tính được $J$ bằng một lượt xuôi.

**Khởi tạo.** Trung bình $\bar u\in\mathbb R^h$ và độ lệch chuẩn $\sigma\in\mathbb R^h_{>0}$ của phân phối chuẩn theo tọa độ.

**Tham số.** Số mẫu $M$; số mẫu ưu tú $M_{\mathrm e}<M$; số vòng.

**Lặp:**

1. Rút $M$ kế hoạch $u^{(i)}\sim\mathcal N(\bar u,\operatorname{diag}\sigma^2)$.
2. Tính $J(u^{(i)})$ trên mô hình bằng lượt xuôi.
3. Giữ $M_{\mathrm e}$ kế hoạch có $J$ nhỏ nhất, gọi là **mẫu ưu tú** (elite samples).
4. Đặt $\bar u$ và $\sigma$ bằng trung bình và độ lệch chuẩn không hiệu chỉnh (chia cho $M_{\mathrm e}$) theo tọa độ của các mẫu ưu tú.

**Điều kiện dừng.** Hết số vòng; trả $\bar u$ hoặc mẫu ưu tú tốt nhất.

**Chi phí mỗi bước.** $M$ lượt xuôi, tức $Mh$ lần gọi $\hat f$; không cần đạo hàm.
:::

Thuật toán 11.34 là **phương pháp entropy chéo** (cross-entropy method, CEM). **Bắn ngẫu nhiên** (random shooting) là bước 1–3 của thuật toán chạy một lần, không cập nhật $\bar u$, $\sigma$. Thuật toán 11.34 có thể thay Thuật toán 11.31 ở bước 2 của Thuật toán 11.33, như PETS (probabilistic ensembles with trajectory sampling) của Chua và cộng sự (2018, §5, Thuật toán 1).

::: remark Nhận xét 11.35 (So sánh tối ưu bằng đạo hàm và bằng lấy mẫu)
| Tiêu chí | Hạ gradient (Thuật toán 11.31) | Entropy chéo (Thuật toán 11.34) |
|---|---|---|
| yêu cầu về mô hình | khả vi | chỉ cần gọi được |
| số lần gọi mô hình mỗi vòng | $h$ cho lượt xuôi, cộng lượt ngược | $Mh$ |
| cực tiểu địa phương | có thể dừng ở điểm dừng địa phương, tùy điểm khởi tạo | mẫu rải rộng có thể thoát, khi $\sigma$ chưa co |
:::

**Trong thực hành.** Phương pháp entropy chéo chỉ cần gọi mô hình, nên dùng được với trình mô phỏng hộp đen và mô hình không khả vi. Mỗi bước của điều khiển dự báo khi đó tốn $M$ lượt xuôi cho mỗi vòng entropy chéo. Khi $\sigma$ co về $0$ ở một tọa độ, nghiệm bị giữ ở giá trị đó như Ví dụ 11.21.

<!-- note-topic-id: lec-11-topic-19 -->
### 4.5 Sai số mô hình tích lũy

Mọi kế hoạch trên tính trên mô hình $\hat f(x,u)=x+u$. Giả sử đường ray thật hơi nghiêng: hệ thật là $f(x,u)=1{,}2x+u$, và dự báo $k$ bước lệch dần khỏi quỹ đạo thật.

Một cách trực quan, mỗi bước dự báo cộng thêm sai số một bước của mô hình, còn hệ thật khuếch đại sai số đã có; sai số tích lũy (compounding error) vì vậy có thể tăng theo cấp số nhân của số bước, như ví dụ sau.

::: example Ví dụ 11.22 (Sai số tích lũy của mô hình)
**Dữ kiện.** Hệ thật $f(x,u)=1{,}2x+u$, mô hình $\hat f(x,u)=x+u$, $x_0=2$, kế hoạch $u\equiv0$.

**Dự báo và thật.** Mô hình dự báo $\hat x_k=2$ với mọi $k$; hệ thật cho $x_k=2\cdot1{,}2^k$. Sai số dự báo $e_k=\lvert x_k-\hat x_k\rvert=2(1{,}2^k-1)$:

| $k$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---:|---:|---:|---:|---:|
| $e_k$ | $0{,}4$ | $0{,}88$ | $1{,}456$ | $2{,}1472$ | $2{,}9766$ |

**Kiểm tra lại.** $e_2=2(1{,}44-1)=0{,}88$; sai số một bước tại trạng thái dự báo $\hat x=2$ là $\lvert1{,}2\cdot2-2\rvert=0{,}4$.
:::

![Sai số e k theo k từ 1 đến 5: 0,4; 0,88; 1,456; 2,1472; 2,9766, nằm trên đường chặn 0,4 nhân (1,2 mũ k trừ 1) chia 0,2; đường chấm k nhân 0,4 để so sánh.](img/lec-11/sai-so-tich-luy.svg)

Trên hình, các điểm $e_k$ nằm trên đường chặn nét đứt và tách khỏi đường $k\bar e$ từ $k=2$, vì sai số được nhân $L=1{,}2$ ở mỗi bước.

::: proposition Mệnh đề 11.36 (Chặn sai số dự báo $k$ bước)
**Giả thiết.** Hệ thật $f$ Lipschitz theo $x$ với hằng số $L$: $\lvert f(x,u)-f(y,u)\rvert\le L\lvert x-y\rvert$ với mọi $x,y,u$. Cùng $x_0$ và cùng chuỗi hành động $u_0,u_1,\dots$; $x_{j+1}=f(x_j,u_j)$ và $\hat x_{j+1}=\hat f(\hat x_j,u_j)$, $\hat x_0=x_0$. Sai số một bước tại các trạng thái dự báo thỏa $\lvert f(\hat x_j,u_j)-\hat f(\hat x_j,u_j)\rvert\le\bar e$ với $j<k$.

**Kết luận.** $e_k=\lvert x_k-\hat x_k\rvert$ thỏa
$$\begin{aligned}e_k&\le\bar e\sum_{j=0}^{k-1}L^j\\&=\begin{cases}\bar e\,\dfrac{L^k-1}{L-1},&L\ne1,\\[4pt]k\,\bar e,&L=1.\end{cases}\end{aligned}\tag{4.4}$$

**Điều kiện áp dụng.** Chuỗi hành động cố định trước, tức kế hoạch vòng hở.

**Phạm vi.** Khi $L>1$, chặn tăng theo cấp số nhân của $k$. Không áp dụng trực tiếp cho vòng kín, vì khi đó hành động phụ thuộc trạng thái và hai quỹ đạo nhận hành động khác nhau.
:::

::: proof
**Bước 1 (một bước).** Thêm và bớt $f(\hat x_j,u_j)$:
$$\begin{aligned}e_{j+1}&=\lvert f(x_j,u_j)-\hat f(\hat x_j,u_j)\rvert\\&\le\lvert f(x_j,u_j)-f(\hat x_j,u_j)\rvert\\&\quad+\lvert f(\hat x_j,u_j)-\hat f(\hat x_j,u_j)\rvert\\&\le Le_j+\bar e.\end{aligned}$$
Bất đẳng thức đầu là bất đẳng thức tam giác; bất đẳng thức sau dùng tính Lipschitz cho số hạng thứ nhất và giả thiết sai số một bước tại $\hat x_j$ cho số hạng thứ hai.

**Bước 2 (quy nạp).** $e_0=0$. Nếu $e_j\le\bar e\sum_{i<j}L^i$ thì Bước 1 cho $e_{j+1}\le\bar e\sum_{i<j}L^{i+1}+\bar e=\bar e\sum_{i\le j}L^i$. Tổng cấp số nhân cho dạng đóng của (4.4). $\square$
:::

Ở Ví dụ 11.22, $\bar e=0{,}4$, $L=1{,}2$, và (4.4) cho $2(1{,}2^k-1)$, trùng $e_k$: chặn đạt dấu bằng. Sai số một bước lấy trên trạng thái dự báo $\hat x_j$. Trên quỹ đạo thật, sai số một bước $\lvert f(x,0)-\hat f(x,0)\rvert=0{,}2x$ tăng theo $x$, và tại $x_5=4{,}9766$ bằng $0{,}9953$, lớn hơn $\bar e=0{,}4$. Khi bỏ giả thiết "chuỗi hành động cố định", hai quỹ đạo dùng hai chuỗi hành động khác nhau, và Bước 1 không còn đúng.

::: example Ví dụ 11.23 (Vòng hở và điều khiển dự báo với mô hình sai)
**Dữ kiện.** Hệ thật $f(x,u)=1{,}2x+u$, mô hình $\hat f(x,u)=x+u$, $x_0=2$, chi phí và chân trời như Ví dụ 11.17. Kế hoạch tối ưu trên mô hình $(-1{,}2;\,-0{,}4)$, luật dự báo $u=-0{,}6x$ (Ví dụ 11.19, 11.20).

**Vòng hở trên hệ thật.** $x_1=1{,}2\cdot2-1{,}2=1{,}2$, mô hình dự báo $0{,}8$; $x_2=1{,}2\cdot1{,}2-0{,}4=1{,}04$, mô hình dự báo $0{,}4$.

**Điều khiển dự báo trên hệ thật.** $x_{t+1}=1{,}2x_t-0{,}6x_t=0{,}6x_t$: $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$.

**Diễn giải.** Vòng hở để xe ở $1{,}04$ thay vì $0{,}4$; vòng kín co về $0$ với hệ số $0{,}6$ dù mô hình sai, vì mỗi bước giải lại từ vị trí thật.

**Kiểm tra lại.** $0{,}72\cdot0{,}6=0{,}432$.
:::

![Vị trí x theo bước t từ 0 đến 3, từ x bằng 2: kế hoạch trên mô hình 0,8; 0,4; vòng hở trên hệ thật 1,2; 1,04; điều khiển dự báo mô hình đúng 0,8; 0,32; 0,128; mô hình sai 1,2; 0,72; 0,432.](img/lec-11/xe-tren-duong-ray.svg)

Trên hình, vòng hở tách khỏi kế hoạch từ bước 1; hai đường điều khiển dự báo cùng về mốc, với hệ số $0{,}4$ khi mô hình đúng và $0{,}6$ khi mô hình sai.

::: remark Nhận xét 11.37 (Tính bất định khi lập kế hoạch liên tục)
PETS lập kế hoạch qua một tập mô hình (Nhận xét 11.7; Chua và cộng sự, 2018, §4–5); PILCO đưa bất định của mô hình vào dự báo dài hạn (Deisenroth và Rasmussen, 2011, §2.2).
:::

**Trong thực hành.** Chân trời $h$ dài làm sai số tích lũy (4.4) lớn. Gradient qua $h$ lần nhân $\partial\hat f/\partial x$ có thể bùng nổ hoặc tiêu biến, như với phụ thuộc dài hạn trong mạng hồi quy (Goodfellow, Bengio và Courville, 2016). Điều khiển dự báo giữ $h$ ngắn và giải lại ở mỗi bước.

Như vậy, gradient qua mô hình (Mệnh đề 11.30) và điều khiển dự báo (Định nghĩa 11.32) xử lý hành động liên tục ở bước thời gian nhỏ, với cái giá là sai số tích lũy (Mệnh đề 11.36) và chi phí tăng theo $h$. Mọi phương pháp tới đây quyết định theo từng hành động một bước của MDP, gọi là bước gốc: lặp giá trị đẩy giá trị lùi một bước sau mỗi lượt quét, Q-planning sau mỗi cập nhật, còn kế hoạch nhìn xa $h$ bước phải tối ưu $h$ hành động. Chúng ta cần một đơn vị hành động kéo dài nhiều bước để lập kế hoạch xa mà số lượt quét, số cập nhật hay chân trời không tăng theo cùng tỉ lệ.

---

## 5. Học tăng cường phân cấp

<!-- note-topic-id: lec-11-topic-20 -->
### 5.1 Tùy chọn và chính sách phân cấp

Trên mê cung, lặp giá trị đồng bộ từ $V_0\equiv0$ cho $V(\mathrm A)=0$ sau ba lượt quét và $V(\mathrm A)=0{,}6103$ sau sáu lượt quét, còn cách $v_*(\mathrm A)=0{,}6604$.

Về mặt ý tưởng, cùng một MDP có thể nhìn ở nhiều thang thời gian (Sutton và Barto, 2018, §17.2, tr. 461). Chẳng hạn, người đi trong tòa nhà nghĩ theo "ra cửa phòng", không theo từng bước chân. Hai chính sách con "đi tới cửa", "đi tới đích", mỗi chính sách chạy tới khi xong việc, cho phép một quyết định thô thay nhiều quyết định mịn. Học tăng cường phân cấp (hierarchical reinforcement learning) dùng các quyết định thô đó. Việc gộp nhiều bước thời gian thành một quyết định gọi là trừu tượng thời gian (temporal abstraction).

::: example Ví dụ 11.24 (Hai tùy chọn trên mê cung hai phòng)
**Dữ kiện.** Mê cung hai phòng: hàng trên $\mathrm A$, $\mathrm B$, $\mathrm C$, $\mathrm D$; hàng dưới $\mathrm E$, $\mathrm F$, $\mathrm K$, $\mathrm Z$; tường giữa $\mathrm B$ và $\mathrm C$; cửa $\mathrm F$–$\mathrm K$; đi đúng với xác suất $0{,}8$, trượt và ở yên với xác suất $0{,}2$; $\mathrm Z$ là đích.

**Tùy chọn đi tới cửa, $\omega_1$.** $\mathcal I_{\omega_1}=\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$; chính sách $\mathrm A,\mathrm E,\mathrm F\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$; $\beta_{\omega_1}=0$ trong phòng trái, $\beta_{\omega_1}=1$ ở các ô khác, nên tùy chọn kết thúc khi tới $\mathrm K$.

**Tùy chọn đi tới đích, $\omega_2$.** $\mathcal I_{\omega_2}=\{\mathrm C,\mathrm D,\mathrm K\}$; chính sách $\mathrm C,\mathrm K\mapsto\rightarrow$, $\mathrm D\mapsto\downarrow$; $\beta_{\omega_2}=0$ trên $\mathcal I_{\omega_2}$, $\beta_{\omega_2}=1$ ở các ô khác, nên tùy chọn kết thúc khi vào $\mathrm Z$.

**Kiểm tra lại.** Mỗi chính sách đi theo đường ngắn nhất trong phòng của nó; trượt chỉ làm tác tử ở yên, nên tùy chọn tới đích của nó với xác suất $1$.
:::

![Hai tùy chọn trên mê cung: phòng trái, omega 1 đi tới cửa, mũi tên A, E, F sang phải, B xuống, hệ số p của K: F 0,8780, B và E 0,7710, A 0,6769; phòng phải, omega 2 đi tới đích, C, K sang phải, D xuống, r: K, D 0,9756, C 0,8566.](img/lec-11/tuy-chon-hai-phong.svg)

Trên hình, mỗi phòng là miền của một tùy chọn, mũi tên trong ô là $\pi_\omega$; con số cạnh ô là mô hình của tùy chọn: hệ số $p$ của việc tới $\mathrm K$ ở phòng trái, phần thưởng kỳ vọng $r$ ở phòng phải.

::: definition Định nghĩa 11.38 (Tùy chọn)
Một **tùy chọn** (option) trên MDP là bộ ba $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$ gồm:

- **tập khởi đầu** (initiation set) $\mathcal I_\omega\subseteq\mathcal S$: các trạng thái mà tùy chọn được bắt đầu;
- **chính sách** $\pi_\omega(a\mid s)$, Markov dừng;
- **hàm kết thúc** (termination function, termination condition) $\beta_\omega:\mathcal S^+\to[0,1]$, với $\beta_\omega=1$ tại trạng thái kết thúc.

Bắt đầu ở $S_0\in\mathcal I_\omega$, tùy chọn chọn $A_t\sim\pi_\omega(\cdot\mid S_t)$, rồi kết thúc tại $t+1$ với xác suất $\beta_\omega(S_{t+1})$; **thời điểm kết thúc** $\tau\ge1$ là bước đầu tiên nó kết thúc. Giả thiết $\{s:\beta_\omega(s)<1\}\subseteq\mathcal I_\omega$: nơi tùy chọn có thể tiếp tục thì nó cũng có thể bắt đầu.
:::

Mỗi hành động một bước (primitive action) $a$ là một tùy chọn với $\mathcal I=\{s:a\in\mathcal A(s)\}$, $\pi(s)=a$, $\beta\equiv1$ (Sutton, Precup và Singh, 1999, §2, tr. 186–187; Sutton và Barto, 2018, tr. 462 viết $\gamma_\omega\equiv0$), nên tùy chọn tổng quát hóa hành động. Một tùy chọn có thể không kết thúc: nếu $\pi_{\omega_1}(\mathrm A)=\leftarrow$, đụng biên, và $\beta_{\omega_1}(\mathrm A)=0$, tùy chọn bắt đầu ở $\mathrm A$ ở yên tại $\mathrm A$ mãi mãi. Vì vậy mô hình tùy chọn chỉ được định nghĩa cho tùy chọn kết thúc với xác suất $1$.

::: definition Định nghĩa 11.39 (Chính sách phân cấp, giá trị của chính sách phân cấp)
Cho một tập tùy chọn và $\Omega(s)=\{\omega:s\in\mathcal I_\omega\}\ne\emptyset$ với mọi $s\in\mathcal S$.

- **Chính sách phân cấp** (hierarchical policy) $\mu$ gán cho mỗi $s$ một phân phối $\mu(\cdot\mid s)$ trên $\Omega(s)$. Ở mỗi **thời điểm chọn**, tại $s$, tác tử rút $\omega\sim\mu(\cdot\mid s)$ và chạy $\omega$ tới khi kết thúc, lúc đó là thời điểm chọn tiếp theo.
- **Giá trị** của $\mu$ là $v_\mu(s)=\mathbb E_\mu[G_0\mid S_0=s]$, lợi tức tính trên các bước gốc; $q_\mu(s,\omega)$ là kỳ vọng đó khi tùy chọn đầu tiên là $\omega$.
:::

Chính sách mà $\mu$ sinh ra trên MDP gốc nói chung không Markov theo trạng thái: hành động tiếp theo phụ thuộc tùy chọn nào đang chạy (Sutton, Precup và Singh, 1999, tr. 187). Khi $\Omega(s)$ chỉ gồm hành động một bước, $v_\mu$ là $v_\pi$ của Định nghĩa 03.15.

<!-- note-topic-id: lec-11-topic-21 -->
### 5.2 Mô hình tùy chọn và bán-MDP

Muốn lập kế hoạch với $\omega_1$, $\omega_2$, tác tử cần biết mỗi tùy chọn cho bao nhiêu phần thưởng và đưa tới đâu, kèm chiết khấu theo số bước.

Một cách trực quan, mô hình của một tùy chọn đóng vai mô hình một bước của hành động: nó cho biết chạy hết tùy chọn thì nhận bao nhiêu phần thưởng chiết khấu và kết thúc ở đâu, còn chiết khấu theo số bước được gộp vào hệ số chuyển. Để làm rõ, xem ví dụ sau.

::: example Ví dụ 11.25 (Mô hình của hai tùy chọn)
**Dữ kiện.** Mê cung hai phòng, trượt với xác suất $0{,}2$, phần thưởng $+1$ khi vào $\mathrm Z$, $\gamma=0{,}9$. Tùy chọn $\omega_1$ chạy trong phòng trái $\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$ theo đường ngắn nhất ($\mathrm A,\mathrm E,\mathrm F\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$) và kết thúc khi tới $\mathrm K$; tùy chọn $\omega_2$ chạy trong phòng phải $\{\mathrm C,\mathrm D,\mathrm K\}$ ($\mathrm C,\mathrm K\mapsto\rightarrow$, $\mathrm D\mapsto\downarrow$) và kết thúc khi vào $\mathrm Z$.

**Một bước đi đúng.** Cần đúng $j$ lần thử với xác suất $0{,}2^{j-1}\cdot0{,}8$, nên thừa số chiết khấu kỳ vọng là
$$\begin{aligned}\rho&=\sum_{j\ge1}\gamma^j\,0{,}2^{j-1}\,0{,}8\\&=\frac{0{,}8\gamma}{1-0{,}2\gamma}=\frac{0{,}72}{0{,}82}\\&=0{,}8780.\end{aligned}$$
Các bước đi đúng liên tiếp độc lập, nên $d$ bước đi đúng cho $\mathbb E[\gamma^\tau]=\rho^d$.

**Tùy chọn $\omega_1$.** Phần thưởng trên đường trong phòng trái bằng $0$, nên $r(s,\omega_1)=0$. Tùy chọn luôn kết thúc ở $\mathrm K$:

- $p(\mathrm K\mid\mathrm F,\omega_1)=\rho=0{,}8780$;
- $p(\mathrm K\mid\mathrm B,\omega_1)=p(\mathrm K\mid\mathrm E,\omega_1)=\rho^2=0{,}7710$;
- $p(\mathrm K\mid\mathrm A,\omega_1)=\rho^3=0{,}6769$.

**Tùy chọn $\omega_2$.** Phần thưởng $+1$ đến ở bước $\tau$, nên $r(\mathrm K,\omega_2)=r(\mathrm D,\omega_2)=\mathbb E[\gamma^{\tau-1}]=0{,}8/0{,}82=0{,}9756$ và $r(\mathrm C,\omega_2)=\rho\cdot0{,}9756=0{,}8566$; tùy chọn chỉ kết thúc ở $\mathrm Z$, có giá trị $0$.

**Kiểm tra lại.** $\rho^3\cdot0{,}9756=0{,}6604=v_*(\mathrm A)$: chạy $\omega_1$ rồi $\omega_2$ từ $\mathrm A$ là đi theo đường ngắn nhất.
:::

::: definition Định nghĩa 11.40 (Mô hình tùy chọn)
Cho tùy chọn $\omega$ kết thúc với xác suất $1$ và $s\in\mathcal I_\omega$. **Mô hình tùy chọn** (option model) gồm hai phần:
$$\begin{aligned}&r(s,\omega)\\&\ =\mathbb E\bigl[R_1+\dots+\gamma^{\tau-1}R_\tau\\&\qquad\bigm|S_0=s,\omega\bigr],\\&p(s'\mid s,\omega)\\&\ =\sum_{k\ge1}\gamma^k\Pr\{S_k=s',\tau=k\\&\qquad\mid S_0=s,\omega\},\ s'\in\mathcal S^+.\end{aligned}\tag{5.1}$$
:::

Đây là (17.2)–(17.3) của Sutton và Barto (2018, tr. 462) và (6)–(7) của Sutton, Precup và Singh (1999, tr. 189). Phần $p$ đã chứa chiết khấu: với hành động một bước, nó là xác suất chuyển nhân $\gamma$; ở Ví dụ 11.25, $p(\mathrm K\mid\mathrm F,\omega_1)=0{,}8780$ trong khi xác suất tới $\mathrm K$ bằng $1$.

::: proposition Mệnh đề 11.41 (Tổng hệ số chuyển của mô hình tùy chọn)
**Giả thiết.** Tùy chọn $\omega$ kết thúc với xác suất $1$; $0\le\gamma<1$.

**Kết luận.** Với mọi $s\in\mathcal I_\omega$,
$$\begin{aligned}&\sum_{s'\in\mathcal S^+}p(s'\mid s,\omega)\\&\quad=\mathbb E\bigl[\gamma^\tau\mid S_0=s,\omega\bigr]\le\gamma.\end{aligned}$$

**Điều kiện áp dụng.** Tổng lấy trên $\mathcal S^+$, kể cả trạng thái kết thúc.

**Phạm vi.** Với $0<\gamma<1$, dấu bằng xảy ra khi và chỉ khi $\tau=1$ hầu chắc chắn.
:::

::: proof
**Bước 1 (đổi thứ tự tổng).** Theo (5.1), tổng theo $s'$ rồi theo $k$ cho
$$\begin{aligned}&\sum_{s'}p(s'\mid s,\omega)\\&\quad=\sum_{k\ge1}\gamma^k\Pr\{\tau=k\}\\&\quad=\mathbb E[\gamma^\tau],\end{aligned}$$
trong đó đẳng thức thứ hai dùng $\Pr\{\tau<\infty\}=1$.

**Bước 2 (chặn).** Vì $\tau\ge1$ và $0\le\gamma<1$, $\gamma^\tau\le\gamma$, nên $\mathbb E[\gamma^\tau]\le\gamma$. $\square$
:::

Ở Ví dụ 11.25, $\sum_{s'}p(s'\mid\mathrm A,\omega_1)=0{,}6769\le0{,}9$. Nếu vẫn tính (5.1) cho một tùy chọn có thể không kết thúc, tổng ở Bước 1 thiếu phần xác suất của biến cố $\tau=\infty$: nó bằng $\sum_{k\ge1}\gamma^k\Pr\{\tau=k\}\le\gamma\Pr\{\tau<\infty\}$, vẫn không vượt $\gamma$.

**Câu hỏi.** Với mô hình (5.1), giá trị của một chính sách phân cấp có thỏa một phương trình Bellman như $v_\pi$ không? Định lý sau trả lời có, với tùy chọn Markov.

::: theorem Định lý 11.42 (Phương trình Bellman cho chính sách phân cấp)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$. Mỗi tùy chọn có $\pi_\omega$ Markov dừng, $\beta_\omega$ chỉ phụ thuộc trạng thái, và kết thúc với xác suất $1$ từ mọi trạng thái của $\mathcal I_\omega$. Chính sách phân cấp $\mu$ chỉ phụ thuộc trạng thái tại mỗi thời điểm chọn.

**Kết luận.** Với mọi $s\in\mathcal S$,
$$\begin{aligned}&v_\mu(s)=\sum_{\omega\in\Omega(s)}\mu(\omega\mid s)\\&\quad\times\Bigl[r(s,\omega)\\&\qquad+\sum_{s'\in\mathcal S^+}p(s'\mid s,\omega)\,v_\mu(s')\Bigr],\end{aligned}\tag{5.2}$$
với $v_\mu=0$ tại trạng thái kết thúc.

**Điều kiện áp dụng.** Mỗi tùy chọn được chạy tới khi kết thúc, không bị ngắt giữa chừng (Định nghĩa 11.39).

**Phạm vi.** Chứng minh dưới đây dùng $\beta_\omega$ chỉ phụ thuộc trạng thái. Sutton, Precup và Singh (1999, (8), tr. 190 và Định lý 1) phát biểu (5.2) cho cả tùy chọn bán-Markov, có chính sách và điều kiện kết thúc phụ thuộc lịch sử từ lúc tùy chọn bắt đầu.
:::

::: proof
Cố định $s$ và một tùy chọn $\omega\in\Omega(s)$ được chọn tại $S_0=s$.

**Bước 1 (tách lợi tức tại $\tau$).** Vì $\tau<\infty$ hầu chắc chắn,
$$G_0=\sum_{t=0}^{\tau-1}\gamma^tR_{t+1}+\gamma^\tau G_\tau.$$

**Bước 2 (phần đầu).** Theo (5.1), kỳ vọng của tổng đầu khi biết $S_0=s$ và $\omega$ là $r(s,\omega)$.

**Bước 3 (phần sau).** Phân hoạch theo các biến cố $\{\tau=k,S_k=s'\}$ với $k\ge1$, $s'\in\mathcal S^+$; trên biến cố đó, $G_\tau=G_k$. Vì $\pi_\omega$ Markov và $\beta_\omega$ chỉ phụ thuộc trạng thái, biến cố $\{\tau=k\}$ được xác định bởi lịch sử $H_k$ tới bước $k$ cùng các lần rút kết thúc tới bước $k$. Cố định một lịch sử như vậy với $\tau=k$ và $S_k=s'$. Từ bước $k$, tác tử rút tùy chọn mới theo $\mu(\cdot\mid s')$ và chạy tiếp, nên quy tắc chọn hành động từ bước $k$ chỉ phụ thuộc phần lịch sử bắt đầu từ $k$. Lập luận của Bổ đề 03.20 chỉ dùng tính Markov của động lực, nên lập luận đó, áp tại thời điểm cố định $k$, cho phần tương lai từ bước $k$ cùng phân phối với quá trình theo $\mu$ xuất phát tại $s'$. Do đó $\mathbb E[G_k\mid\tau=k,H_k,S_k=s']=v_\mu(s')$; lấy kỳ vọng theo các lịch sử được $\mathbb E[G_\tau\mid\tau=k,S_k=s']=v_\mu(s')$, và
$$\begin{aligned}&\mathbb E[\gamma^\tau G_\tau\mid S_0=s,\omega]\\&\ =\sum_{k\ge1}\sum_{s'}\gamma^k\\&\quad\times\Pr\{\tau=k,S_k=s'\}\,v_\mu(s')\\&\ =\sum_{s'}p(s'\mid s,\omega)\,v_\mu(s').\end{aligned}$$
Đẳng thức sau là (5.1); đổi thứ tự tổng được phép vì $v_\mu$ bị chặn.

**Bước 4 (gom theo $\mu$).** Tùy chọn đầu tiên được rút theo $\mu(\cdot\mid s)$, nên lấy trung bình của Bước 2 và Bước 3 theo $\mu(\omega\mid s)$ cho (5.2). $\square$
:::

Định lý mở rộng Định lý 03.21 từ hành động sang tùy chọn: số hạng trong ngoặc là $q_\mu(s,\omega)$, và chiết khấu nằm trong $p$, nên tùy chọn dài ngắn khác nhau được so trên cùng thang thời gian gốc. Khi $\Omega(s)$ chỉ gồm hành động một bước, (5.2) là phương trình Bellman kỳ vọng của Định lý 03.21, với $\gamma$ nằm trong $p$.

Hai giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "kết thúc với xác suất $1$": không có $\tau$ hữu hạn để tách lợi tức ở Bước 1.
- Bỏ "$\mu$ chỉ phụ thuộc trạng thái": phần sau $\tau$ phụ thuộc lịch sử, và Bước 3 không cho $v_\mu(S_\tau)$.

::: remark Nhận xét 11.43 (Bán-MDP)
Ở các thời điểm chọn, quá trình là một **quá trình quyết định bán-Markov** (semi-Markov decision process, SMDP), gọi tắt là bán-MDP: trạng thái kế và thời gian lưu trú ngẫu nhiên $\tau$ phụ thuộc trạng thái và tùy chọn hiện tại. Với mọi MDP và mọi tập tùy chọn, quá trình đó là một bán-MDP (Sutton, Precup và Singh, 1999, Định lý 1, tr. 188); lý thuyết tổng quát có trong Puterman (1994).
:::

**Trong thực hành.** Mô hình tùy chọn (5.1) được tính bằng đánh giá $\pi_\omega$ trên mô hình một bước, hoặc ước lượng từ các lần chạy thật. Khi tùy chọn bị ngắt trước $\tau$ hoặc chính sách cấp trên dùng lịch sử, giả thiết của Định lý 11.42 bị vi phạm.

<!-- note-topic-id: lec-11-topic-22 -->
### 5.3 Lập kế hoạch ở nhiều mức trừu tượng thời gian

Thay trung bình theo $\mu$ trong (5.2) bằng cực đại theo $\omega$, ta được một phép lặp giá trị trên tùy chọn, như ví dụ sau.

::: example Ví dụ 11.26 (Lặp giá trị với tùy chọn)
**Dữ kiện.** Mô hình hai tùy chọn trên mê cung hai phòng (Ví dụ 11.25): $r(s,\omega_1)=0$ và $\omega_1$ chỉ kết thúc ở $\mathrm K$, với $p(\mathrm K\mid\mathrm F,\omega_1)=0{,}8780$, $p(\mathrm K\mid\mathrm B,\omega_1)=p(\mathrm K\mid\mathrm E,\omega_1)=0{,}7710$, $p(\mathrm K\mid\mathrm A,\omega_1)=0{,}6769$; $\omega_2$ chỉ kết thúc ở $\mathrm Z$, với $r(\mathrm K,\omega_2)=r(\mathrm D,\omega_2)=0{,}9756$, $r(\mathrm C,\omega_2)=0{,}8566$. $\Omega(s)=\{\omega_1\}$ ở phòng trái, $\Omega(s)=\{\omega_2\}$ ở phòng phải; $V_0\equiv0$. Mỗi vòng đặt $V_{k+1}(s)=\max_{\omega\in\Omega(s)}[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)V_k(s')]$.

**Vòng 1.** Phòng phải: $V_1(\mathrm K)=V_1(\mathrm D)=0{,}9756$, $V_1(\mathrm C)=0{,}8566$; phòng trái: $V_1=p\cdot V_0(\mathrm K)=0$.

**Vòng 2.** Phòng trái: $V_2(\mathrm F)=0{,}8780\cdot0{,}9756=0{,}8566$; $V_2(\mathrm B)=V_2(\mathrm E)=0{,}7710\cdot0{,}9756=0{,}7522$; $V_2(\mathrm A)=0{,}6769\cdot0{,}9756=0{,}6604$.

**Vòng 3.** Không đổi; bảng trùng $v_*$ của Ví dụ 11.1.

**So sánh.** Lặp giá trị đồng bộ trên hành động một bước, cũng từ $V_0\equiv0$:

| lượt quét | $V(\mathrm K)$ | $V(\mathrm F)$ | $V(\mathrm B)$ | $V(\mathrm A)$ |
|---:|---:|---:|---:|---:|
| 1 | $0{,}8000$ | $0$ | $0$ | $0$ |
| 2 | $0{,}9440$ | $0{,}5760$ | $0$ | $0$ |
| 3 | $0{,}9699$ | $0{,}7834$ | $0{,}4147$ | $0$ |
| 4 | $0{,}9746$ | $0{,}8393$ | $0{,}6387$ | $0{,}2986$ |
| 5 | $0{,}9754$ | $0{,}8528$ | $0{,}7193$ | $0{,}5136$ |
| 6 | $0{,}9756$ | $0{,}8558$ | $0{,}7435$ | $0{,}6103$ |

**Kiểm tra lại.** Lượt quét 2 tại $\mathrm K$: $0{,}8+0{,}18\cdot0{,}8=0{,}944$; tại $\mathrm F$: $0{,}72\cdot0{,}8=0{,}576$. Với tùy chọn, hai vòng cho đúng $v_*(\mathrm A)=0{,}6604$, vì hai tùy chọn đi theo đường ngắn nhất.
:::

::: theorem Định lý 11.44 (Hội tụ của lặp giá trị với tùy chọn)
**Giả thiết.** Như Định lý 11.42 cho mọi tùy chọn của tập; $\Omega(s)$ hữu hạn, khác rỗng với mọi $s\in\mathcal S$; mô hình tùy chọn (5.1) đúng.

**Kết luận.** Với hàm $V$ trên $\mathcal S^+$, $V=0$ tại trạng thái kết thúc, đặt
$$\begin{aligned}&(T_\Omega V)(s)\\&\quad=\max_{\omega\in\Omega(s)}\Bigl[r(s,\omega)\\&\qquad+\sum_{s'}p(s'\mid s,\omega)V(s')\Bigr].\end{aligned}$$

- (a) $T_\Omega$ là ánh xạ co hệ số $\gamma$ theo chuẩn vô cùng.
- (b) Với mọi $V_0$, dãy $V_{k+1}=T_\Omega V_k$ hội tụ tới điểm bất động duy nhất $v_\Omega$ của $T_\Omega$, và $\lVert V_k-v_\Omega\rVert_\infty\le\gamma^k\lVert V_0-v_\Omega\rVert_\infty$.
- (c) $v_\Omega$ là giá trị của chính sách phân cấp tốt nhất trên $\Omega$; $v_\Omega\le v_*$, và nếu $\Omega(s)\supseteq\mathcal A(s)$ với mọi $s$ thì $v_\Omega=v_*$.

**Điều kiện áp dụng.** Mô hình tùy chọn được tính hoặc học trước khi lặp.

**Phạm vi.** Khi $\Omega$ chỉ gồm tùy chọn nhiều bước, $v_\Omega$ có thể nhỏ hơn ngặt $v_*$.
:::

::: proof
**Phần (a), bước 1 (cực đại).** Với hai hàm $V$, $W$ và mỗi $s$, vì $\Omega(s)$ hữu hạn, Bổ đề 04.23 cho
$$\begin{aligned}&\lvert(T_\Omega V)(s)-(T_\Omega W)(s)\rvert\\&\quad\le\max_{\omega\in\Omega(s)}\Bigl\lvert\sum_{s'}p(s'\mid s,\omega)\\&\qquad\times\bigl(V(s')-W(s')\bigr)\Bigr\rvert.\end{aligned}$$

**Bước 2 (hệ số co).** Vì $p\ge0$ và theo Mệnh đề 11.41,
$$\begin{aligned}&\Bigl\lvert\sum_{s'}p(s'\mid s,\omega)\\&\qquad\times\bigl(V(s')-W(s')\bigr)\Bigr\rvert\\&\quad\le\sum_{s'}p(s'\mid s,\omega)\,\lVert V-W\rVert_\infty\\&\quad\le\gamma\lVert V-W\rVert_\infty.\end{aligned}$$
Lấy cực đại theo $s$ được $\lVert T_\Omega V-T_\Omega W\rVert_\infty\le\gamma\lVert V-W\rVert_\infty$.

**Phần (b).** Theo (a) và Định lý 04.5 với hệ số co $\gamma<1$.

**Phần (c).** Dẫn nguồn: Sutton và Barto (2018, §17.2, tr. 463) nêu lặp giá trị với tùy chọn hội tụ tới chính sách phân cấp tốt nhất, và tới chính sách tối ưu khi tập tùy chọn chứa mọi hành động một bước; Sutton, Precup và Singh (1999, (10), tr. 190; (13), tr. 191) định nghĩa $v_\Omega$ là giá trị tốt nhất trên các chính sách phân cấp và cho $\lim_kV_k=v_\Omega$. Ý tưởng cho hai vế sau: như Bước 3 của chứng minh Định lý 11.42, $r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)v_*(s')$ là giá trị của việc chạy $\omega$ rồi theo chính sách tối ưu, nên không vượt $v_*(s)$ (Định lý 04.25(b)); vậy $T_\Omega v_*\le v_*$, và vì $T_\Omega$ đơn điệu, $v_\Omega\le v_*$. Khi $\Omega(s)\supseteq\mathcal A(s)$, $T_\Omega v_*\ge T_*v_*=v_*$, nên $v_*$ là điểm bất động $v_\Omega$. $\square$
:::

Khi $\Omega(s)=\mathcal A(s)$, $T_\Omega$ là $T_*$ của Định nghĩa 04.22 và (a) là Mệnh đề 04.24. Với tùy chọn nhiều bước, tổng hệ số chuyển không bằng $\gamma$ mà chỉ bị chặn bởi $\gamma$ (Mệnh đề 11.41), nên chứng minh đi qua Bổ đề 04.23 thay vì dùng nguyên văn Mệnh đề 04.24. Hệ số co của $T_\Omega$ vẫn là $\gamma$. Ví dụ 11.26 hội tụ nhanh vì mỗi vòng đi qua cả một phòng. Trên mê cung, hai tùy chọn đi đúng đường ngắn nhất nên $v_\Omega=v_*$ dù $\Omega(s)$ không chứa hành động một bước.

Các giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ:

- Bỏ "$\Omega(s)\supseteq\mathcal A(s)$": nếu phòng trái chỉ có một tùy chọn đi về $\mathrm A$ và kết thúc ở $\mathrm A$, tác tử không ra khỏi phòng trái, nên $v_\Omega=0<v_*$ ở đó.
- Bỏ "mô hình tùy chọn đúng": phép lặp hội tụ tới điểm bất động của $T_\Omega$ trên mô hình sai, miễn mô hình đó có hệ số không âm với tổng không vượt $\gamma$ (Phần (a), (b) của chứng minh).
- Bỏ "kết thúc với xác suất $1$": nếu vẫn tính (5.1) cho tùy chọn như vậy, Bước 2 của (a) vẫn đúng vì $\sum_{s'}p(s'\mid s,\omega)\le\gamma\Pr\{\tau<\infty\}\le\gamma$, nhưng Bước 1 của chứng minh Định lý 11.42 không còn $\tau$ hữu hạn để tách lợi tức, và tùy chọn không trả lại thời điểm chọn.

::: algorithm Thuật toán 11.45 (Lặp giá trị với tùy chọn)
**Đầu vào.** Mô hình tùy chọn $r(s,\omega)$, $p(s'\mid s,\omega)$ với mọi $s$ và $\omega\in\Omega(s)$.

**Đầu ra.** Bảng $V\approx v_\Omega$ và chính sách phân cấp tham lam theo $V$.

**Giả thiết.** Như Định lý 11.44; đặc biệt $\Omega(s)$ hữu hạn, khác rỗng.

**Khởi tạo.** $V_0$ tùy ý, $V_0=0$ tại trạng thái kết thúc.

**Tham số.** Ngưỡng dừng $\theta>0$.

**Lặp, mỗi vòng một lượt quét:**

1. Với mọi $s\in\mathcal S$: $V_{k+1}(s)\leftarrow(T_\Omega V_k)(s)$.
2. $\Delta_k\leftarrow\lVert V_{k+1}-V_k\rVert_\infty$.

**Điều kiện dừng.** $\Delta_k\le\theta$, như Thuật toán 04.28 với $T_\Omega$ thay $T_*$.

**Chi phí mỗi bước.** Mỗi lượt quét tốn $O\bigl(\sum_s\lvert\Omega(s)\rvert\cdot\lvert\mathcal S^+\rvert\bigr)$ phép tính.
:::

Ví dụ 11.26 là ba lượt quét của thuật toán. Khi so chi phí với lặp giá trị một bước, cần cộng cả phép tính mô hình tùy chọn: mỗi tùy chọn đòi một bài toán đánh giá $\pi_\omega$. Sutton, Precup và Singh (1999, tr. 195) nêu rằng tùy chọn nhiều bước không chắc làm giảm tổng chi phí lập kế hoạch. Khi không có mô hình tùy chọn, tác tử học giá trị tùy chọn từ các lần chạy thật.

::: example Ví dụ 11.27 (Một cập nhật Q-learning bán-MDP)
**Dữ kiện.** Tại $\mathrm B$, tác tử chạy $\omega_1$, kết thúc ở $\mathrm K$ sau $k=3$ bước, có một lần trượt, phần thưởng trên đường bằng $0$. Giả sử $Q(\mathrm B,\omega_1)=0$, $\max_{\omega'}Q(\mathrm K,\omega')=Q(\mathrm K,\omega_2)=0{,}9$, $\alpha=0{,}5$, $\gamma=0{,}9$.

**Cập nhật.**

- mục tiêu: $0+\gamma^3\cdot0{,}9=0{,}729\cdot0{,}9=0{,}6561$;
- sai lệch: $0{,}6561-0=0{,}6561$;
- giá trị mới: $Q(\mathrm B,\omega_1)=0+0{,}5\cdot0{,}6561=0{,}32805$.

**Kiểm tra lại.** Chiết khấu là $\gamma^k$ theo số bước thật. Dùng $\gamma$ một lần cho cả tùy chọn cho mục tiêu $0{,}81$ và giá trị mới $0{,}405$, là một nhầm lẫn thường gặp.
:::

::: algorithm Thuật toán 11.46 (Q-learning bán-MDP)
**Đầu vào.** Tập tùy chọn với $\Omega(s)$ hữu hạn, khác rỗng; môi trường; $\gamma\in[0,1)$.

**Đầu ra.** Bảng $Q(s,\omega)$.

**Giả thiết.** Mọi tùy chọn kết thúc với xác suất $1$.

**Khởi tạo.** $Q(s,\omega)$ tùy ý; $Q=0$ tại trạng thái kết thúc.

**Tham số.** Bước học $\alpha$; $\varepsilon$ của chính sách $\varepsilon$-tham lam trên tùy chọn; số lượt.

**Lặp, mỗi vòng một lần chạy tùy chọn:**

1. Tại trạng thái $s$ của thời điểm chọn, chọn $\omega\in\Omega(s)$ theo chính sách $\varepsilon$-tham lam với $Q(s,\cdot)$.
2. Chạy $\omega$ tới khi kết thúc sau $k$ bước ở $S_k$, ghi các phần thưởng $R_1,\dots,R_k$.
3. Cập nhật
$$\begin{aligned}&Q(s,\omega)\leftarrow Q(s,\omega)\\&\ +\alpha\Bigl[\sum_{j=1}^k\gamma^{j-1}R_j\\&\ +\gamma^k\max_{\omega'\in\Omega(S_k)}Q(S_k,\omega')\\&\ -Q(s,\omega)\Bigr].\end{aligned}\tag{5.3}$$
4. $s\leftarrow S_k$; nếu $S_k$ kết thúc, bắt đầu lượt mới.

**Điều kiện dừng.** Hết số lượt.

**Chi phí mỗi bước.** $O(\lvert\Omega(S_k)\rvert)$ mỗi lần chạy tùy chọn.
:::

Thuật toán 11.46 là Q-learning bán-MDP (SMDP Q-learning). Mục tiêu của (5.3) là một mẫu của số hạng trong ngoặc của (5.2), với cực đại thay trung bình: tổng chiết khấu trên đường là mẫu không chệch của $r(s,\omega)$, còn $\gamma^k\mathbb 1\{S_k=s'\}$, với $S_k$ là trạng thái nơi tùy chọn dừng, là mẫu không chệch của $p(s'\mid s,\omega)$. Khi mọi tùy chọn là hành động một bước, $k=1$ và (5.3) là quy tắc của Thuật toán 06.16; thành phần đổi là tổng chiết khấu trên đường và thừa số $\gamma^k$ thay $\gamma$. Sutton, Precup và Singh (1999, §3.2, tr. 195–196) trình bày thuật toán này, do Bradtke và Duff (1995) đề xuất, và nêu rằng ước lượng hội tụ dưới các điều kiện tương tự Q-learning thông thường, dẫn theo tài liệu [52] của bài báo.

**Trong thực hành.** Tùy chọn thường do người thiết kế viết, như "đi tới cửa", hoặc được học. Tùy chọn viết cho một mục tiêu cũ có thể cho $v_\Omega<v_*$. Mô hình tùy chọn cũng phải học hoặc tính. Khi mô hình tùy chọn sai, chứng minh của Định lý 11.44(a), (b) chỉ cho hội tụ tới điểm bất động của $T_\Omega$ trên mô hình sai, miễn mô hình đó có hệ số không âm với tổng không vượt $\gamma$.

<!-- note-topic-id: lec-11-topic-23 -->
### 5.4 Đọc thêm: học mô hình tùy chọn

::: remark Nhận xét 11.47 (Học mô hình tùy chọn và học trong tùy chọn)
Mỗi phần của (5.1) là một hàm giá trị tổng quát (general value function, GVF), với tín hiệu tích lũy là phần thưởng hoặc chỉ báo "kết thúc tại $s'$" và chiết khấu dừng khi tùy chọn kết thúc (Sutton và Barto, 2018, §17.1, tr. 459–461); học nó từ bước của chính sách khác $\pi_\omega$ là học khác chính sách. Với tùy chọn Markov có chính sách tất định, Q-learning trong tùy chọn một bước (one-step intra-option Q-learning) hội tụ với xác suất $1$ tới giá trị tối ưu trên tập tùy chọn khi mọi hành động được thực hiện ở mọi trạng thái vô hạn lần và bước học thỏa điều kiện Robbins–Monro (Sutton, Precup và Singh, 1999, Định lý 3, tr. 205).
:::

Như vậy, mô hình tùy chọn (Định nghĩa 11.40) cho phương trình Bellman của chính sách phân cấp (Định lý 11.42), và lặp giá trị với tùy chọn hội tụ với hệ số co $\gamma$ tới $v_\Omega$ (Định lý 11.44): trên mê cung, hai vòng cho $v_*(\mathrm A)=0{,}6604$, trong khi lặp giá trị một bước sau sáu lượt quét mới đạt $0{,}6103$. Cái giá là phải tính hoặc học mô hình tùy chọn. Định lý 11.44 chỉ bảo đảm $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$.

---

<!-- note-topic-id: lec-11-topic-24 -->
## 6. Tổng kết

### 6.1 So sánh bốn cách dùng mô hình

Bảng tách tìm kiếm lúc ra quyết định của Mục 1.2 thành hai hàng theo loại hành động: rời rạc (Mục 3) và liên tục (Mục 4).

| Phương pháp | Mô hình cần có | Khi nào tính | Đầu ra | Bảo đảm (số hiệu) | Sai số mô hình ảnh hưởng thế nào |
|---|---|---|---|---|---|
| Dyna-Q (Thuật toán 11.10) | mô hình mẫu học từ bước thật | nền | bảng $Q$ | Q-planning hội tụ tới $\hat q_*$ khi mô hình cố định, xác định ở mọi cặp (Mệnh đề 11.9); Dyna-Q không thỏa giả thiết đó (Nhận xét 11.11) | tới $\hat q_*$ của mô hình sai; cặp bi quan cần thưởng thăm dò |
| Tìm kiếm theo cây Monte Carlo (Thuật toán 11.26) | mô hình mẫu nhanh, hành động hữu hạn | tại thời điểm quyết định | $A_t$ | rollout không giảm giá trị (Mệnh đề 11.21); UCT với $c_{\mathrm{ucb}}=\sqrt2D$ nhất quán cho bài toán cắt (Định lý 11.27(a)); Thuật toán 11.26 không có bảo đảm này | Mệnh đề 11.21, 11.22, Định lý 11.27 đúng cho MDP của mô hình |
| Hạ gradient, điều khiển dự báo (Thuật toán 11.31, 11.33) | mô hình khả vi | tại thời điểm quyết định | $u_t$ | gradient đúng trên mô hình (Mệnh đề 11.30) | vòng hở: sai số theo (4.4) (Mệnh đề 11.36) |
| Lặp giá trị với tùy chọn (Thuật toán 11.45) | mô hình tùy chọn | nền | $v_\Omega$, $\mu$ | hội tụ tới $v_\Omega$; $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$ (Định lý 11.44) | tới điểm bất động của $T_\Omega$ trên mô hình sai |
### 6.2 Trả lời bài toán trung tâm

Các phép tính lập kế hoạch dưới đây chỉ chạy trên mô hình, nên không tốn thêm bước thật nào.

1. **Lập kế hoạch nền.** Q-planning hội tụ tới $\hat q_*$ của mô hình khi mô hình cố định và xác định ở mọi cặp (Mệnh đề 11.9). Sau mỗi bước thật, Dyna-Q làm thêm $n$ cập nhật lập kế hoạch trên các cặp đã thử: hai cập nhật sau lượt thứ nhất cho $Q(\mathrm F,\rightarrow)=0{,}225$, trong khi Q-learning cho $0$ (Ví dụ 11.7). Dyna-Q không thỏa giả thiết của Mệnh đề 11.9: mô hình thay đổi sau mỗi bước thật và chỉ có ở các cặp đã thử (Nhận xét 11.11). Với môi trường ngẫu nhiên, Dyna-Q cần mô hình đếm (Định nghĩa 11.4), với độ lệch chuẩn của $\hat p$ giảm theo $1/\sqrt{C(s,a)}$ (Mệnh đề 11.5). Với môi trường thay đổi, Dyna-Q cần thưởng thăm dò (Định nghĩa 11.12).
2. **Lập kế hoạch tại thời điểm quyết định.** Với $q_{\pi_0}$ chính xác, rollout không làm giảm giá trị (Mệnh đề 11.21). Trên mê cung, chính sách rollout đưa giá trị tại $\mathrm F$ từ $0{,}2016$ lên $0{,}8566=v_*(\mathrm F)$ (Ví dụ 11.13). Tại $\mathrm F$, với $m=70$, xác suất chọn $\downarrow$ thay vì $\rightarrow$ không vượt $0{,}0496$ (Mệnh đề 11.22, Ví dụ 11.14). UCT chọn sai hành động ở gốc với xác suất tiến về $0$ khi mô hình đúng, bài toán cắt ở $D=20$ và hệ số thăm dò của UCB1 nhân $D$ (Định lý 11.27(a)). Giá trị tối ưu của bài toán cắt lệch $v_*$ không quá $\gamma^{20}=0{,}1216$ (Định lý 11.27(b)).
3. **Tối ưu kế hoạch bằng đạo hàm.** Với mô hình khả vi, truy hồi ngược cho gradient của chi phí trên mô hình (Mệnh đề 11.30). Một bước hạ gradient giảm chi phí của xe từ $8$ xuống $2{,}88$, tối ưu là $2{,}40$ (Ví dụ 11.18, 11.19).
4. **Tùy chọn.** Hai tùy chọn cho đúng $v_*(\mathrm A)=0{,}6604$ sau hai vòng, so với $0{,}6103$ sau sáu lượt quét một bước (Ví dụ 11.26). Lặp giá trị với tùy chọn hội tụ tới $v_\Omega\le v_*$, với dấu bằng khi $\Omega(s)\supseteq\mathcal A(s)$ (Định lý 11.44). Mô hình tùy chọn phải được tính hoặc học trước (Mục 5.2).
5. **Khi mô hình sai.** Mệnh đề 11.9, 11.21, 11.22 và Định lý 11.27 đúng cho MDP của mô hình, không cho môi trường thật. Q-planning hội tụ tới $\hat q_*$ của mô hình sai, còn rollout và tìm kiếm theo cây chọn hành động tốt trên mô hình. Mệnh đề 11.30 cho gradient của chi phí trên mô hình, nên gradient đó không bảo đảm chi phí trên môi trường thật giảm. Lặp giá trị với tùy chọn hội tụ tới điểm bất động của $T_\Omega$ trên mô hình sai, miễn mô hình đó có hệ số không âm với tổng không vượt $\gamma$ (chứng minh Định lý 11.44(a), (b)). Với hệ thật $x'=1{,}2x+u$, điều khiển dự báo thiết kế trên mô hình $x+u$ vẫn co về $0$ với hệ số $0{,}6$ (Ví dụ 11.23). Chỉ hai kết quả đo sai số của mô hình. Mệnh đề 11.5 cho phương sai $p(1-p)/C(s,a)$ của xác suất ước lượng $\hat p(s'\mid s,a)$ tại một cặp. Mệnh đề 11.36 chặn sai số dự báo vòng hở theo (4.4) khi chuỗi hành động cố định.

### 6.3 Câu hỏi tự kiểm tra

Trả lời các câu hỏi sau và nêu kết quả đã dùng.

1. Mệnh đề 11.9 bảo đảm hội tụ tới $q_*$ của môi trường hay của mô hình, dưới giả thiết nào? Tới $\hat q_*$ của mô hình, khi mô hình cố định và xác định ở mọi cặp.
2. Vì sao tập mô hình không thấy bất định ở cặp chỉ có một mẫu? Mọi tập lấy lại từ một mẫu đều trùng mẫu đó (Nhận xét 11.7), trong khi $\operatorname{Var}\hat p=p(1-p)$ với $C=1$ (Mệnh đề 11.5).
3. Mệnh đề 11.21 còn áp dụng không khi $q_{\pi_0}$ thay bằng trung bình của $m=5$ mô phỏng? Không: giả thiết "$q_{\pi_0}$ chính xác" bị vi phạm. Mệnh đề 11.22 chỉ cho $\Pr\{\bar G(\downarrow)\ge\bar G(\rightarrow)\}\le\exp(-5\Delta^2)=0{,}8069$, còn tổng các chặn cho bốn hành động theo bất đẳng thức hợp vượt $1$.
4. Khi tập tùy chọn không chứa hành động một bước, lặp giá trị với tùy chọn hội tụ tới đâu? Tới $v_\Omega$, điểm bất động của $T_\Omega$ (Định lý 11.44(b)), với $v_\Omega\le v_*$ và có thể nhỏ hơn ngặt (Định lý 11.44(c)).

<!-- note-topic-id: lec-11-topic-25 -->
## Tình huống áp dụng và ứng dụng

::: application Tình huống 11.1 (Điều khiển dự báo cho xe trên đường ray với mô hình học bằng bình phương tối thiểu)
**Bài toán.** Xe trên đường ray có hệ thật $x'=1{,}2x+u$, chưa biết; chi phí $x_{t+1}^2+u_t^2$, $h=2$, $x_0=2$. Tác tử thu ba mẫu $(x,u,x')$: $(2;\,0;\,2{,}4)$, $(1;\,-1;\,0{,}2)$, $(0;\,1;\,1)$, rồi dùng điều khiển dự báo trên mô hình học được.

**Mô hình hóa.** Lớp mô hình $\hat f(x,u)=\hat a_1x+\hat a_2u$, học bằng bình phương tối thiểu; tình huống dùng Định nghĩa 11.29, 11.32, điểm dừng của (4.1) và Thuật toán 11.33.

**Kiểm giả thiết.** Lớp mô hình tuyến tính chứa hệ thật và dữ liệu không nhiễu, nên bình phương tối thiểu tìm đúng hệ thật khi hệ phương trình chuẩn có nghiệm duy nhất; mô hình tuyến tính khả vi như Mệnh đề 11.30 cần.

**Tính mô hình.** Các tổng: $\sum x^2=5$, $\sum xu=-1$, $\sum u^2=2$, $\sum xx'=5$, $\sum ux'=0{,}8$. Hệ phương trình chuẩn
$$\begin{aligned}5\hat a_1-\hat a_2&=5,\\-\hat a_1+2\hat a_2&=0{,}8\end{aligned}$$
có định thức $9\ne0$ và nghiệm $\hat a_1=1{,}2$, $\hat a_2=1$.

**Tính luật điều khiển.** Với $\hat f(x,u)=\hat a_1x+u$, $h=2$, ta cực tiểu lần lượt theo $u_1$ rồi theo $u_0$. Với $x_1$ cố định, $(\hat a_1x_1+u_1)^2+u_1^2$ có đạo hàm $2(\hat a_1x_1+u_1)+2u_1$, bằng $0$ tại $u_1=-\hat a_1x_1/2$, với giá trị nhỏ nhất $\hat a_1^2x_1^2/2$. Chi phí còn lại là $(1+\hat a_1^2/2)x_1^2+u_0^2$ với $x_1=\hat a_1x_0+u_0$; đạo hàm theo $u_0$ bằng $0$ cho
$$u^*_0=-\frac{(1+\hat a_1^2/2)\,\hat a_1}{2+\hat a_1^2/2}\,x_0.$$
Với $\hat a_1=1$, công thức cho $-0{,}6x_0$, khớp Ví dụ 11.20. Với $\hat a_1=1{,}2$: $u=-1{,}72\cdot1{,}2/2{,}72\cdot x=-0{,}7588x$.

**Diễn giải.** Vòng kín trên hệ thật là $x_{t+1}=0{,}4412x_t$: $2;\ 0{,}8824;\ 0{,}3893;\ 0{,}1717$, co nhanh hơn hệ số $0{,}6$ của luật thiết kế trên mô hình sai (Ví dụ 11.23).

**Giới hạn.** Ba mẫu đủ vì dữ liệu không nhiễu và lớp mô hình đúng. Với nhiễu hoặc hệ phi tuyến, mô hình học được có sai số, và sai số dự báo vòng hở tích lũy theo (4.4).
:::

::: application Tình huống 11.2 (Dyna-Q với mô hình tất định trên mê cung có trượt)
**Bài toán.** Tác tử chạy Dyna-Q (Thuật toán 11.10) trên mê cung hai phòng (Ví dụ 11.1: trượt với xác suất $0{,}2$, $\gamma=0{,}9$) và lập kế hoạch nhiều lần trên mô hình hiện có.

**Kiểm giả thiết.** Thuật toán 11.10 giả thiết môi trường tất định; mê cung có trượt, nên giả thiết **không thỏa**: mô hình lưu kết cục gần nhất của mỗi cặp là một mô hình tất định sai.

**Áp dụng.** Giả sử mọi cặp đã được thử và mô hình đứng yên trong lúc lập kế hoạch, nên Mệnh đề 11.9 áp dụng cho MDP của mô hình.

- Nếu kết cục gần nhất trên đường ngắn nhất đều là "đi đúng", mô hình là mê cung không trượt, với giá trị $\gamma^{d-1}$: $1$; $0{,}9$; $0{,}81$; $0{,}729$ tại khoảng cách $1$–$4$, so với giá trị thật $0{,}9756$; $0{,}8566$; $0{,}7522$; $0{,}6604$; tại $\mathrm A$ mô hình đánh giá cao hơn $0{,}0686$.
- Nếu kết cục gần nhất của $(\mathrm A,\rightarrow)$ là trượt, mô hình ghi $(\mathrm A,\rightarrow)\mapsto(0,\mathrm A)$ và tác tử chọn $\downarrow$ tại $\mathrm A$, vẫn thuộc một đường ngắn nhất.

**Diễn giải.** Giới hạn của Mệnh đề 11.9 là $\hat q_*$ của mô hình sai: giá trị bỏ qua trượt nên quá lạc quan, và lựa chọn phụ thuộc kết cục của lần thử cuối. Cách sửa là mô hình đếm (Định nghĩa 11.4), có độ lệch chuẩn $\sqrt{p(1-p)/C(s,a)}$ (Mệnh đề 11.5).

**Giới hạn.** Nếu kết cục cuối của $(\mathrm F,\rightarrow)$ là trượt, mô hình coi cửa là tường, và mọi giá trị của phòng trái trên mô hình bằng $0$.
:::

**Ứng dụng.** Tìm kiếm theo cây Monte Carlo cùng mạng chính sách và mạng giá trị là thành phần lập kế hoạch của AlphaGo; AlphaGo Zero dùng tìm kiếm theo cây với một mạng có hai đầu ra (Sutton và Barto, 2018, §16.6). Tập mô hình cùng entropy chéo trong điều khiển dự báo là thành phần của PETS (Chua và cộng sự, 2018, §5–6).

<!-- note-topic-id: lec-11-topic-26 -->
## Tóm tắt chương

Q-learning dùng mỗi mẫu thật một lần rồi bỏ. Một mô hình học từ các mẫu thật cho phép dùng lại chúng. Mô hình đếm ước lượng động lực bằng tần suất và tách bất định nhận thức khỏi bất định ngẫu nhiên (Định nghĩa 11.4, 11.6, Mệnh đề 11.5). Q-planning trên một mô hình cố định, xác định ở mọi cặp, hội tụ tới $\hat q_*$ (Mệnh đề 11.9). Dyna-Q xen kẽ học mô hình với Q-planning sau mỗi bước thật (Thuật toán 11.10), nên mô hình đổi theo dữ liệu và Dyna-Q nằm ngoài giả thiết của Mệnh đề 11.9 (Nhận xét 11.11). Khi môi trường đổi, thưởng thăm dò buộc tác tử thử lại cặp mà mô hình đánh giá thấp (Định nghĩa 11.12). Rollout và tìm kiếm theo cây dồn phép tính vào trạng thái hiện tại (Mệnh đề 11.21, 11.22, Định lý 11.27). Với hành động liên tục, gradient qua mô hình và điều khiển dự báo tối ưu trực tiếp chuỗi hành động trên mô hình thay vì dựng cây (Mệnh đề 11.30, Định nghĩa 11.32). Cái giá là sai số tích lũy (Mệnh đề 11.36). Tùy chọn gộp nhiều bước thành một quyết định. Giá trị của chính sách phân cấp vẫn thỏa một phương trình Bellman (Định lý 11.42), và toán tử $T_\Omega$ của lặp giá trị với tùy chọn vẫn là ánh xạ co hệ số $\gamma$ (Định lý 11.44). Mệnh đề 11.9, 11.21, 11.22 và Định lý 11.27 đúng cho MDP của mô hình, không cho môi trường thật. Với mô hình tùy chọn sai, lặp giá trị với tùy chọn hội tụ tới điểm bất động của $T_\Omega$ trên mô hình đó, miễn mô hình có hệ số không âm với tổng không vượt $\gamma$ (chứng minh Định lý 11.44(a), (b)). Chỉ hai kết quả đo sai số của mô hình: Mệnh đề 11.5 cho phương sai của xác suất ước lượng $\hat p(s'\mid s,a)$ tại một cặp, và Mệnh đề 11.36 chặn sai số dự báo vòng hở.

**Định nghĩa và kết quả theo mục.**

- Mục 2: Định nghĩa 11.1, 11.2, 11.4, 11.6 và Mệnh đề 11.5 (mô hình, bất định), Thuật toán 11.8, 11.10 và Mệnh đề 11.9 (Q-planning, Dyna-Q), Định nghĩa 11.12 (Dyna-Q+), 11.14 và Mệnh đề 11.15 (cập nhật mẫu), Định lý 11.19 (RTDP).
- Mục 3: Thuật toán 11.20 và Mệnh đề 11.21, 11.22 (rollout), Định nghĩa 11.23 và Định lý 11.24 (UCB1), Định nghĩa 11.25, Thuật toán 11.26 và Định lý 11.27 (tìm kiếm theo cây).
- Mục 4: Định nghĩa 11.29, Mệnh đề 11.30, Thuật toán 11.31 (gradient qua mô hình), Định nghĩa 11.32, Thuật toán 11.33 (điều khiển dự báo), Thuật toán 11.34 (entropy chéo), Mệnh đề 11.36 (sai số tích lũy).
- Mục 5: Định nghĩa 11.38–11.40 và Mệnh đề 11.41 (tùy chọn, mô hình tùy chọn), Định lý 11.42 (Bellman phân cấp), Định lý 11.44 và Thuật toán 11.45 (lặp giá trị với tùy chọn), Thuật toán 11.46 (Q-learning bán-MDP).

**Công thức cần nhớ.**

- Mô hình đếm và phương sai của tần suất, (2.1), (2.2):
  $$\begin{aligned}\hat p(s'\mid s,a)&=\frac{C(s,a,s')}{C(s,a)},\\\operatorname{Var}\hat p&=\frac{p(1-p)}{C}.\end{aligned}$$
- Cập nhật lập kế hoạch của Dyna-Q+ (Định nghĩa 11.12):
  $$\begin{aligned}&Q(\tilde S,\tilde A)\leftarrow Q(\tilde S,\tilde A)\\&\quad+\alpha\bigl[\tilde R+\kappa\sqrt{\ell(\tilde S,\tilde A)}\\&\quad+\gamma\max_{a'}Q(\tilde S',a')\\&\quad-Q(\tilde S,\tilde A)\bigr].\end{aligned}$$
- Sai số sau $k$ cập nhật mẫu, (2.5):
  $$\sqrt{\mathbb E(Q_k-\bar y)^2}=\sqrt{\frac{b-1}{bk}}.$$
- Xác suất đảo thứ tự của rollout, (3.1):
  $$\begin{aligned}&\Pr\{\bar G(a')\ge\bar G(a)\}\\&\quad\le\exp\Bigl(-\frac{m\Delta^2}{B^2}\Bigr).\end{aligned}$$
- Chính sách cây UCT, (3.3):
  $$\begin{aligned}a\in\arg\max_a\Bigl[&\bar Q(s,a)\\&+c_{\mathrm{ucb}}\sqrt{\frac{\ln N(s)}{N(s,a)}}\Bigr].\end{aligned}$$
- Truy hồi ngược, (4.2), (4.3):
  $$\begin{aligned}\lambda_t&=\partial_{x_t}c(x_t,u_{t-1})\\&\quad+\lambda_{t+1}\,\partial_{x_t}\hat f(x_t,u_t),\\\frac{\partial J}{\partial u_t}&=\partial_{u_t}c(x_{t+1},u_t)\\&\quad+\lambda_{t+1}\,\partial_{u_t}\hat f(x_t,u_t).\end{aligned}$$
- Sai số dự báo vòng hở, (4.4), với $L\ne1$:
  $$e_k\le\bar e\,\frac{L^k-1}{L-1}.$$
- Mô hình tùy chọn, (5.1):
  $$\begin{aligned}&r(s,\omega)=\mathbb E\Bigl[\textstyle\sum_{t<\tau}\gamma^tR_{t+1}\Bigr],\\&p(s'\mid s,\omega)\\&\quad=\textstyle\sum_k\gamma^k\Pr\{S_k=s',\tau=k\}.\end{aligned}$$
- Phương trình Bellman của chính sách phân cấp, (5.2):
  $$\begin{aligned}v_\mu(s)&=\textstyle\sum_\omega\mu(\omega\mid s)\bigl[r(s,\omega)\\&\quad+\textstyle\sum_{s'}p(s'\mid s,\omega)\\&\qquad\times v_\mu(s')\bigr].\end{aligned}$$
- Q-learning bán-MDP, (5.3):
  $$\begin{aligned}&Q(s,\omega)\leftarrow Q(s,\omega)\\&\quad+\alpha\Bigl[\textstyle\sum_{j=1}^k\gamma^{j-1}R_j\\&\quad+\gamma^k\max_{\omega'}Q(S_k,\omega')\\&\quad-Q(s,\omega)\Bigr].\end{aligned}$$

**Giả thiết hay bị bỏ quên.**

- Mệnh đề 11.9: mô hình cố định, xác định ở mọi cặp. Giới hạn là $\hat q_*$, không phải $q_*$.
- Thuật toán 11.10: môi trường tất định. Với trượt, mô hình lưu kết cục gần nhất là một mô hình sai (Tình huống 11.2).
- Mệnh đề 11.21: $q_{\pi_0}$ chính xác.
- Mệnh đề 11.22: $m$ chọn trước, mô phỏng độc lập, không bị cắt.
- Định lý 11.24: phần thưởng trong $[0,1]$, phân phối không đổi theo thời gian.
- Định lý 11.27: mô hình mẫu đúng, chân trời hữu hạn $D$, hệ số thăm dò nhân $D$. Phần (a) được chứng minh cho UCT của Kocsis và Szepesvári, không cho Thuật toán 11.26. Sai số cắt là $\gamma^{20}=0{,}1216$.
- Mệnh đề 11.36: chuỗi hành động cố định, sai số đo trên quỹ đạo dự báo.
- Định lý 11.42, 11.44: tùy chọn kết thúc với xác suất $1$. Định lý 11.44 bảo đảm $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$.
- Thuật toán 11.46: chiết khấu bằng $\gamma^k$ theo số bước thật.

---

<!-- note-topic-id: lec-11-topic-27 -->
## Bài tập củng cố

Các bài phủ bảy mục tiêu học tập:

- mục tiêu 1: Bài tập 11.1, 11.2, 11.10;
- mục tiêu 2: Bài tập 11.4;
- mục tiêu 3: Bài tập 11.1;
- mục tiêu 4: Bài tập 11.5, 11.8;
- mục tiêu 5: Bài tập 11.6, 11.11;
- mục tiêu 6: Bài tập 11.3, 11.7, 11.10;
- mục tiêu 7: Bài tập 11.9, 11.10, 11.11.

### Mức nhận biết

::: exercise Bài tập 11.1 (Phân loại cách dùng mô hình)
Xét bốn thủ tục: (1) lặp giá trị đồng bộ (Thuật toán 04.28); (2) bước (f) của Dyna-Q; (3) tìm kiếm theo cây Monte Carlo; (4) điều khiển dự báo với mô hình khả vi $\hat f$.

- (a) Thủ tục nào cần mô hình phân phối, thủ tục nào chỉ cần mô hình mẫu?
- (b) Thủ tục nào là lập kế hoạch nền, thủ tục nào là lập kế hoạch tại thời điểm quyết định?
- (c) Với $b=50$ trạng thái kế, một cập nhật kỳ vọng và một cập nhật mẫu tốn bao nhiêu lần đánh giá $\max_aQ$?
- (d) Dưới giả thiết của Mệnh đề 11.15(b) với $b=50$, tính sai số sau $k=5$ cập nhật mẫu và so chi phí của chúng với một cập nhật kỳ vọng.
:::

::: hint
Dùng Định nghĩa 11.1, 11.2, 11.14 và (2.5); mô hình tất định thuộc cả hai loại.
:::

::: solution
**Câu (a).** (1) phân phối; (2), (3) mẫu; (4) mô hình tất định, vừa là mô hình phân phối suy biến vừa là mô hình mẫu.

**Câu (b).** (1), (2) nền; (3), (4) tại thời điểm quyết định.

**Câu (c).** $50$ và $1$.

**Câu (d).** Theo (2.5), $\sqrt{49/(50\cdot5)}=\sqrt{0{,}196}=0{,}4427$. Năm cập nhật mẫu tốn $5$ lần đánh giá, một phần mười chi phí của một cập nhật kỳ vọng, và đã đưa sai số từ $1$ xuống $0{,}4427$.

**Kiểm tra lại.** Lỗi thường gặp là xếp Dyna-Q vào lập kế hoạch tại thời điểm quyết định vì nó chạy sau mỗi bước thật. Bước (f) cập nhật các cặp chọn ngẫu nhiên, nên Dyna-Q là lập kế hoạch nền.
:::

::: exercise Bài tập 11.2 (Hai loại bất định)
Mê cung hai phòng trượt với xác suất $0{,}2$. Xác định đúng hay sai, giải thích một câu: (a) thêm dữ liệu cho $(\mathrm F,\rightarrow)$ làm giảm xác suất trượt; (b) sau một lần thử $(\mathrm B,\downarrow)\to\mathrm F$, $\hat p(\mathrm F\mid\mathrm B,\downarrow)=1$ nên cặp này hết bất định; (c) môi trường tất định không có bất định nhận thức; (d) với $C(s,a)=8$ và $p=0{,}5$, độ lệch chuẩn của $\hat p$ bằng $0{,}1768$.
:::

::: hint
Tách $p(1-p)$ khỏi $p(1-p)/C$ (Định nghĩa 11.6, Mệnh đề 11.5).
:::

::: solution
**Câu (a).** Sai: trượt là bất định ngẫu nhiên; dữ liệu chỉ làm $\hat p$ gần $0{,}8$ hơn.

**Câu (b).** Sai: với $C=1$, độ lệch chuẩn của $\hat p$ là $\sqrt{p(1-p)}=0{,}4$ khi $p=0{,}8$.

**Câu (c).** Sai: cặp chưa thử vẫn có kết cục chưa biết.

**Câu (d).** Đúng: theo (2.2), $\sqrt{p(1-p)/C}=\sqrt{0{,}25/8}=\sqrt{0{,}03125}=0{,}1768$.

**Kiểm tra lại.** Quên chia cho $C$ ở (d) cho $0{,}5$.
:::

::: exercise Bài tập 11.3 (Hành động và tùy chọn)
Tùy chọn $\omega_1$: $\mathcal I=\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$; $\mathrm A,\mathrm E,\mathrm F\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$; kết thúc tại $\mathrm K$; trượt với xác suất $0{,}2$. (a) Viết hành động $\downarrow$ thành tùy chọn $\langle\mathcal I,\pi,\beta\rangle$. (b) Tìm $\tau$ nhỏ nhất khi $\omega_1$ bắt đầu ở $\mathrm F$, ở $\mathrm A$, và xác suất đạt giá trị đó. (c) Đổi $\pi_{\omega_1}(\mathrm A)=\leftarrow$, giữ $\beta_{\omega_1}=0$ trong phòng trái: tùy chọn bắt đầu ở $\mathrm A$ có kết thúc không, kết quả nào không còn áp dụng?
:::

::: hint
Hành động là tùy chọn kết thúc sau đúng một bước.
:::

::: solution
**Câu (a).** $\mathcal I=\mathcal S$, $\pi(s)=\downarrow$, $\beta\equiv1$.

**Câu (b).** Từ $\mathrm F$, một bước đi đúng tới $\mathrm K$, nên $\tau$ nhỏ nhất là $1$, đạt khi lần đầu không trượt, xác suất $0{,}8$. Từ $\mathrm A$, đường $\mathrm A\to\mathrm B\to\mathrm F\to\mathrm K$ cần ba bước đi đúng, nên $\tau$ nhỏ nhất là $3$, đạt khi ba lần thử liên tiếp đều không trượt; các lần thử độc lập, nên xác suất là $0{,}8^3=0{,}512$.

**Câu (c).** Không kết thúc: $\leftarrow$ tại $\mathrm A$ đụng biên. Mệnh đề 11.41 và Định lý 11.42 không áp dụng.

**Kiểm tra lại.** Lấy $\tau=4$ từ $\mathrm A$ là đếm nhầm bước vào $\mathrm Z$ của $\omega_2$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 11.4 (Bước thật đầu của lượt thứ hai trong Dyna-Q)
Sau Ví dụ 11.7: $Q(\mathrm K,\rightarrow)=0{,}75$, $Q(\mathrm F,\rightarrow)=0{,}225$, ô khác bằng $0$; mô hình ghi $(\mathrm A,\rightarrow)\mapsto(0,\mathrm B)$, $(\mathrm B,\downarrow)\mapsto(0,\mathrm F)$, $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$, $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$; $\alpha=0{,}5$, $\gamma=0{,}9$, $n=2$. Bước thật là $(\mathrm A,\rightarrow,0,\mathrm B)$; bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm B,\downarrow)$. (a) Tính các ô thay đổi. (b) Nêu điều kiện để Q-planning trên một mô hình hội tụ tới $\hat q_*$, và giải thích vì sao Dyna-Q trong bài này không thỏa điều kiện đó.
:::

::: hint
Ghi mục tiêu, sai lệch, giá trị mới cho từng cập nhật, theo thứ tự; với (b), dùng Mệnh đề 11.9.
:::

::: solution
**Câu (a), cập nhật trực tiếp.** Mục tiêu $0{,}9\max_aQ(\mathrm B,a)=0$; $Q(\mathrm A,\rightarrow)$ giữ $0$.

**Tại $(\mathrm F,\rightarrow)$.** Mục tiêu $0{,}675$; sai lệch $0{,}45$; giá trị mới $0{,}45$.

**Tại $(\mathrm B,\downarrow)$.** Mục tiêu $0{,}9\cdot0{,}45=0{,}405$; sai lệch $0{,}405$; giá trị mới $0{,}2025$.

**Câu (b).** Theo Mệnh đề 11.9, mô hình phải cố định, xác định ở mọi cặp, mọi cặp được chọn vô hạn lần và bước học thỏa Robbins–Monro. Ở đây mô hình chỉ xác định ở bốn cặp đã thử và đổi sau mỗi bước thật (Nhận xét 11.11); bước học hằng $\alpha=0{,}5$ không thỏa Định nghĩa 06.19.

**Kiểm tra lại.** Đảo thứ tự hai cặp: $(\mathrm B,\downarrow)$ trước có mục tiêu $0{,}9\cdot0{,}225=0{,}2025$ và giá trị mới $0{,}10125$. Vậy thứ tự đổi kết quả.
:::

::: exercise Bài tập 11.5 (Vòng tìm kiếm theo cây Monte Carlo tiếp theo)
Sau Ví dụ 11.16, các cạnh gốc tại $\mathrm F$ có: $\rightarrow$: $N=4$, $\bar Q=0{,}6932$; $\downarrow$: $N=2$, $\bar Q=0{,}5938$; $\uparrow$: $N=2$, $\bar Q=0{,}5214$; $\leftarrow$: $N=1$, $W=0{,}2059$; $N(\mathrm F)=9$; $c_{\mathrm{ucb}}=1$, $\gamma=0{,}9$. (a) Cạnh nào được chọn? (b) Mở rộng ra $\mathrm E$ và mô phỏng $\mathrm E\to\mathrm F\to\mathrm K\to\mathrm Z$ không trượt: tính thống kê mới của cạnh đó.
:::

::: hint
Dùng (3.3) với $\ln9$.
:::

::: solution
**Câu (a).** $\ln9=2{,}1972$; theo (3.3) với $c_{\mathrm{ucb}}=1$, các chỉ số là $0{,}6932+\sqrt{2{,}1972/4}=0{,}6932+0{,}7412=1{,}4344$; $0{,}5938+1{,}0481=1{,}6419$; $0{,}5214+1{,}0481=1{,}5696$ (cộng từ giá trị chưa làm tròn $0{,}521405+1{,}048147=1{,}569552$); $0{,}2059+1{,}4823=1{,}6882$. Chọn $\leftarrow$.

**Câu (b).** Tính từ cạnh gốc, đường $\mathrm F\to\mathrm E\to\mathrm F\to\mathrm K\to\mathrm Z$ có bốn bước, phần thưởng $+1$ ở bước cuối, nên $G=\gamma^3=0{,}729$; cạnh $\leftarrow$: $N=2$, $W=0{,}2059+0{,}729=0{,}9349$, $\bar Q=0{,}4674$; $N(\mathrm F)=10$; nút $\mathrm E$ giữ $N(\mathrm E)=0$.

**Kiểm tra lại.** Dùng $\ln8$ của vòng trước là lỗi thường gặp.
:::

::: exercise Bài tập 11.6 (Kế hoạch hai bước từ $x_0=1$)
Mô hình $\hat f(x,u)=x+u$, chi phí $x_{t+1}^2+u_t^2$, $h=2$, $x_0=1$. (a) Tính gradient tại $(0;\,0)$ bằng khai triển và bằng truy hồi ngược. (b) Thực hiện một bước $\eta=0{,}1$. (c) Tìm kế hoạch tối ưu và $J^*$.
:::

::: hint
So với Ví dụ 11.18, 11.19.
:::

::: solution
**Câu (a).** Tại $(0;\,0)$: $x_1=x_2=1$, $J=1+0+1+0=2$. Khai triển: $\partial J/\partial u_0=2(x_0+u_0)+2u_0+2(x_0+u_0+u_1)=2+0+2=4$ và $\partial J/\partial u_1=2(x_0+u_0+u_1)+2u_1=2$. Truy hồi ngược (4.2), (4.3): $\lambda_2=2x_2=2$, $\lambda_1=2x_1+\lambda_2=4$, $\partial J/\partial u_1=2u_1+\lambda_2=2$, $\partial J/\partial u_0=2u_0+\lambda_1=4$. Hai cách cho cùng gradient $(4;\,2)$.

**Câu (b).** $u=(0;\,0)-0{,}1\,(4;\,2)=(-0{,}4;\,-0{,}2)$, $x_1=0{,}6$, $x_2=0{,}4$, $J=0{,}36+0{,}16+0{,}16+0{,}04=0{,}72$.

**Câu (c).** Hai đạo hàm bằng $0$ cho $2+3u_0+u_1=0$ và $1+u_0+2u_1=0$. Từ phương trình sau, $u_0=-1-2u_1$; thế vào phương trình đầu được $-1-5u_1=0$, nên $u_1=-0{,}2$, $u_0=-0{,}6$. Khi đó $x_1=0{,}4$, $x_2=0{,}2$, $J^*=0{,}16+0{,}36+0{,}04+0{,}04=0{,}6$.

**Kiểm tra lại.** $J$ bậc hai thuần nhất, $x_0$ bằng nửa Ví dụ 11.19, nên $J^*=2{,}40/4$.
:::

::: exercise Bài tập 11.7 (Mô hình tùy chọn khi trượt nhiều hơn)
Mê cung hai phòng với xác suất trượt $\delta=0{,}5$ (trượt thì ở yên), phần thưởng $+1$ khi vào $\mathrm Z$, $\gamma=0{,}9$. Tùy chọn $\omega_1$ chạy trong phòng trái $\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$ với $\mathrm A,\mathrm E,\mathrm F\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$ và kết thúc khi tới $\mathrm K$; tùy chọn $\omega_2$ chạy trong phòng phải $\{\mathrm C,\mathrm D,\mathrm K\}$ với $\mathrm C,\mathrm K\mapsto\rightarrow$, $\mathrm D\mapsto\downarrow$ và kết thúc khi vào $\mathrm Z$. (a) Chứng minh thừa số của một bước đi đúng là $\rho=(1-\delta)\gamma/(1-\delta\gamma)$. (b) Tính $p(\mathrm K\mid\mathrm B,\omega_1)$, $r(\mathrm K,\omega_2)$ và giá trị của $\mathrm B$ theo "$\omega_1$ rồi $\omega_2$". (c) Kiểm Mệnh đề 11.41.
:::

::: hint
Số lần thử của một bước đi đúng có phân phối hình học.
:::

::: solution
**Câu (a).** Bước đi đúng xảy ra ở lần thử thứ $j$ với xác suất $\delta^{j-1}(1-\delta)$, và khi đó đã qua $j$ bước, nên
$$\begin{aligned}\rho&=\sum_{j\ge1}\gamma^j\delta^{j-1}(1-\delta)\\&=\frac{(1-\delta)\gamma}{1-\delta\gamma},\end{aligned}$$
theo chuỗi hình học với $\lvert\delta\gamma\rvert<1$.

**Câu (b).** $\rho=0{,}45/0{,}55=0{,}8182$. Từ $\mathrm B$, $\omega_1$ cần hai bước đi đúng ($\mathrm B\to\mathrm F\to\mathrm K$), độc lập, nên $p(\mathrm K\mid\mathrm B,\omega_1)=\rho^2=0{,}6694$. Từ $\mathrm K$, phần thưởng $+1$ đến ở bước $\tau$, nên $r(\mathrm K,\omega_2)=\mathbb E[\gamma^{\tau-1}]=\rho/\gamma=(1-\delta)/(1-\delta\gamma)=0{,}5/0{,}55=0{,}9091$. Theo (5.2) với $\mu$ chọn $\omega_1$ ở phòng trái và $\omega_2$ ở phòng phải, $r(\mathrm B,\omega_1)=0$ và $v_\mu(\mathrm K)=r(\mathrm K,\omega_2)$ vì $\omega_2$ kết thúc ở $\mathrm Z$ có giá trị $0$; do đó $v_\mu(\mathrm B)=0+p(\mathrm K\mid\mathrm B,\omega_1)\,v_\mu(\mathrm K)=0{,}6694\cdot0{,}9091=0{,}6086$.

**Câu (c).** $\omega_1$ chỉ kết thúc ở $\mathrm K$, nên $\sum_{s'}p(s'\mid\mathrm B,\omega_1)=0{,}6694\le0{,}9$.

**Kiểm tra lại.** $\delta=0{,}2$ cho lại $\rho=0{,}8780$.
:::

::: exercise Bài tập 11.8 (Số mô phỏng của rollout với bốn hành động)
Tại $\mathrm F$, $q_{\pi_0}(\mathrm F,\cdot)$: $\rightarrow$ $0{,}388554$; $\downarrow$ $0{,}181398$; $\uparrow$, $\leftarrow$ $0{,}118131$; lợi tức trong $[0,1]$. (a) Chứng minh: với hành động tốt nhất $a^*$ duy nhất, xác suất thuật toán rollout không chọn $a^*$ không vượt $\sum_{a\ne a^*}\exp(-m\Delta_a^2/B^2)$. (b) Tìm $m$ nhỏ nhất để chặn này không vượt $0{,}05$.
:::

::: hint
Bất đẳng thức hợp và Mệnh đề 11.22.
:::

::: solution
**Câu (a).** Không chọn $a^*$ kéo theo $\bar G(a)\ge\bar G(a^*)$ với một $a\ne a^*$; bất đẳng thức hợp và (3.1) cho chặn.

**Câu (b).** $\Delta=0{,}2072$, $\Delta'=0{,}2704$; chặn $\exp(-m\Delta^2)+2\exp(-m\Delta'^2)$ bằng $0{,}0616$ ($m=70$), $0{,}0507$ ($m=74$), $0{,}0483$ ($m=75$). Vậy $m=75$.

**Kiểm tra lại.** Với hai hành động, $m=70$ đã đủ (Ví dụ 11.14).
:::

### Mức vận dụng

::: exercise Bài tập 11.9 (Chọn cách dùng mô hình)
Giả sử có ba bài toán: (a) trò chơi bàn cờ hai người, luật biết đầy đủ, hành động rời rạc; (b) cánh tay robot với mô hình khả vi học từ dữ liệu, hành động liên tục; (c) robot giao hàng trong tòa nhà nhiều phòng, lượt dài hàng nghìn bước, có sẵn kỹ năng "đi tới cửa". Với mỗi bài toán, chọn một phương pháp của chương, nêu kết quả bảo đảm (số hiệu) và một giả thiết cần kiểm.
:::

::: hint
Xét loại hành động, loại mô hình và độ dài chân trời.
:::

::: solution
**Câu (a).** Tìm kiếm theo cây Monte Carlo (Định lý 11.27): chân trời hữu hạn, lợi tức trong $[0,1]$; trò chơi hai người nằm ngoài giả thiết MDP một tác tử.

**Câu (b).** Điều khiển dự báo với gradient qua mô hình (Mệnh đề 11.30): sai số tích lũy theo $h$ (Mệnh đề 11.36).

**Câu (c).** Lặp giá trị với tùy chọn (Định lý 11.44): tùy chọn kết thúc với xác suất $1$; $\Omega(s)\supseteq\mathcal A(s)$ để bảo đảm đạt $v_*$.

**Kiểm tra lại.** Chọn Dyna-Q dạng bảng cho (b) là sai, vì bảng không dùng được với hành động liên tục.
:::

::: exercise Bài tập 11.10 (Mô hình đếm và tùy chọn trên mê cung hai phòng)
Mê cung hai phòng ($\gamma=0{,}9$, phần thưởng $+1$ khi vào $\mathrm Z$, không đi đúng thì ở yên). Giả sử $C(\mathrm B,\downarrow)=4$ với $3$ lần tới $\mathrm F$; $C(\mathrm F,\rightarrow)=10$ với $8$ lần tới $\mathrm K$; $C(\mathrm K,\rightarrow)=5$ với $4$ lần tới $\mathrm Z$. (a) Tính mô hình đếm và độ lệch chuẩn ước lượng của $\hat p(\mathrm F\mid\mathrm B,\downarrow)$. Tùy chọn $\omega_1$ đi $\mathrm B\mapsto\downarrow$, $\mathrm F\mapsto\rightarrow$ trong phòng trái và kết thúc khi tới $\mathrm K$; tùy chọn $\omega_2$ đi $\mathrm K\mapsto\rightarrow$ và kết thúc khi vào $\mathrm Z$. (b) Tính $p(\mathrm K\mid\mathrm B,\omega_1)$, $r(\mathrm K,\omega_2)$ trên mô hình đếm. (c) Tính $\hat v(\mathrm B)$ theo "$\omega_1$ rồi $\omega_2$". (d) So với $v_*(\mathrm B)=0{,}7522$ và với $0{,}81$ của mô hình tất định (Tình huống 11.2). (e) Tại $\mathrm B$, tác tử chạy $\omega_1$ trên mê cung thật, tới $\mathrm K$ sau $k=2$ bước, phần thưởng trên đường bằng $0$; với $Q(\mathrm B,\omega_1)=0$, $\max_{\omega'}Q(\mathrm K,\omega')=0{,}9756$, $\alpha=0{,}5$, thực hiện một cập nhật (5.3).
:::

::: hint
Một bước đi đúng với xác suất $\hat p$ có thừa số $\hat p\gamma/(1-(1-\hat p)\gamma)$.
:::

::: solution
**Câu (a).** Theo (2.1): $\hat p(\mathrm F\mid\mathrm B,\downarrow)=3/4=0{,}75$, $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=8/10=0{,}8$, $\hat p(\mathrm Z\mid\mathrm K,\rightarrow)=4/5=0{,}8$. Thay $p$ chưa biết bằng $\hat p=0{,}75$ trong (2.2), độ lệch chuẩn ước lượng là $\sqrt{0{,}75\cdot0{,}25/4}=0{,}2165$.

**Câu (b).** Với gợi ý, bước $\mathrm B\to\mathrm F$ có thừa số $0{,}75\cdot0{,}9/(1-0{,}25\cdot0{,}9)=0{,}675/0{,}775=0{,}8710$, bước $\mathrm F\to\mathrm K$ có thừa số $0{,}72/0{,}82=0{,}8780$. Hai bước độc lập, nên $p(\mathrm K\mid\mathrm B,\omega_1)=0{,}8710\cdot0{,}8780=0{,}7648$. Từ $\mathrm K$, $r(\mathrm K,\omega_2)=\hat p/(1-(1-\hat p)\gamma)=0{,}8/0{,}82=0{,}9756$.

**Câu (c).** $\hat v(\mathrm B)=0{,}764752\cdot0{,}975610=0{,}7461$.

**Câu (d).** Sai số $-0{,}0061$ đến từ bất định nhận thức ở cặp có $4$ mẫu; mô hình tất định sai $+0{,}0578$, sai số hệ thống không giảm khi thêm dữ liệu.

**Câu (e).** Mục tiêu $0+\gamma^2\cdot0{,}9756=0{,}81\cdot0{,}9756=0{,}7902$; sai lệch $0{,}7902$; giá trị mới $Q(\mathrm B,\omega_1)=0{,}5\cdot0{,}7902=0{,}3951$.

**Kiểm tra lại.** $\hat p(\mathrm F\mid\mathrm B,\downarrow)=0{,}8$ cho lại $0{,}7522$.
:::

::: exercise Bài tập 11.11 (Điều khiển dự báo với mô hình sai)
Luật $u=-0{,}6x$ thiết kế trên mô hình $x+u$ (Ví dụ 11.20); hệ thật $x'=ax+u$. (a) Với $a=1{,}2$; $1{,}5$; $1{,}7$, tính hệ số vòng kín và ba bước từ $x_0=2$. (b) Tìm mọi $a$ để vòng kín co về $0$. (c) Giải thích vì sao vòng kín chịu được một mức sai số mô hình còn vòng hở thì không.
:::

::: hint
Vòng kín là $x_{t+1}=(a-0{,}6)x_t$.
:::

::: solution
**Câu (a).** $0{,}6$: $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$. $0{,}9$: $2;\ 1{,}8;\ 1{,}62;\ 1{,}458$. $1{,}1$: $2;\ 2{,}2;\ 2{,}42;\ 2{,}662$, phân kỳ.

**Câu (b).** Vòng kín $x_{t+1}=(a-0{,}6)x_t$ co về $0$ với mọi $x_0$ khi và chỉ khi $\lvert a-0{,}6\rvert<1$, tức $-0{,}4<a<1{,}6$.

**Câu (c).** Điều khiển dự báo giải lại từ trạng thái thật mỗi bước, nên sai số không cộng dồn qua một chuỗi hành động cố định như (4.4). Tuy nhiên, luật vẫn thiết kế trên mô hình sai, nên vòng kín chỉ co khi $-0{,}4<a<1{,}6$ (câu (b)); với $a=1{,}7$ nó phân kỳ như câu (a). Vòng hở giữ chuỗi hành động, nên sai số dự báo bị nhân với $L=\lvert a\rvert$ qua mỗi bước và tích lũy như (4.4).

**Kiểm tra lại.** $a=1$ cho hệ số $0{,}4$ của Ví dụ 11.20.
:::

<!-- note-topic-id: lec-11-topic-28 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

**Hướng dẫn đọc thêm.** Sutton và Barto (2018), Chương 8, là cơ sở của Mục 1–3; §2.7 cho quy tắc cận tin cậy trên; §17.2 cho tùy chọn. Tùy chọn và bán-MDP được trình bày đầy đủ trong Sutton, Precup và Singh (1999); rollout và điều khiển dự báo trong Bertsekas (2019). Tối ưu kế hoạch qua mô hình học được và tập mô hình: Chua và cộng sự (2018); tìm kiếm chính sách qua mô hình xác suất: Deisenroth và Rasmussen (2011).

**Tài liệu tham khảo.**

1. Tạ Việt Cường, Trần Quốc Long. *Giáo trình Học tăng cường và lập kế hoạch*, Chương 11 và mục 4.3.1, 4.3.2, 4.7: phạm vi và thứ tự.
2. Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018. §2.7 (tr. 35–36): Mục 3.2. §8.1–8.8 (tr. 159–181): Mục 1–2. §8.9–8.11 (tr. 182–188): Mục 3. §16.6 (tr. 441–450): Nhận xét 11.28, Ứng dụng. §17.1–17.2 (tr. 459–464): Mục 5.
3. Bertsekas, D. P. *Reinforcement Learning and Optimal Control*, Athena Scientific, 2019. §2.4, §2.5.1, §5.1.2: Mục 3.1, 4.3.
4. Bertsekas, D. P. *Rollout, Policy Iteration, and Distributed Reinforcement Learning*, Athena Scientific, 2020. §3.1, Mệnh đề 5.4.2: Mục 3.1, 4.3.
5. Szepesvári, C. *Algorithms for Reinforcement Learning*, Morgan & Claypool, 2010. §4.2.1: Mục 3.2.
6. Puterman, M. L. *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley, 1994. Chương về bán-MDP: Mục 5.2.
7. Goodfellow, I., Bengio, Y., Courville, A. *Deep Learning*, MIT Press, 2016. Lan truyền ngược, phụ thuộc dài hạn: Mục 4.
8. Hoeffding, W. "Probability Inequalities for Sums of Bounded Random Variables." *Journal of the American Statistical Association* 58 (1963): Mục 3.1.
9. Auer, P., Cesa-Bianchi, N., Fischer, P. "Finite-time Analysis of the Multiarmed Bandit Problem." *Machine Learning* 47 (2002): 235–256. Hình 1, Định lý 1 (tr. 237): Mục 3.2.
10. Kocsis, L., Szepesvári, C. "Bandit Based Monte-Carlo Planning." *ECML* 2006, LNCS 4212, tr. 282–293. §2.2–2.4, Định lý 6; Kocsis, L., Szepesvári, C., Willemson, J. "Improved Monte-Carlo Search", báo cáo kỹ thuật, 2006, Định lý 7: Mục 3.3–3.4.
11. Barto, A. G., Bradtke, S. J., Singh, S. P. "Learning to Act Using Real-Time Dynamic Programming." *Artificial Intelligence* 72 (1995): Mục 2.7.
12. Sutton, R. S., Precup, D., Singh, S. "Between MDPs and semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning." *Artificial Intelligence* 112 (1999): 181–211. tr. 186–205: Mục 5.
13. Chua, K., Calandra, R., McAllister, R., Levine, S. "Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models." *NeurIPS* 2018. §4–6: Mục 2.2–2.3, 4.4–4.5.
14. Deisenroth, M. P., Rasmussen, C. E. "PILCO: A Model-Based and Data-Efficient Approach to Policy Search." *ICML* 2011. §2.2–2.3: Mục 4.
15. Silver, D. và cộng sự. "Mastering the Game of Go without Human Knowledge." *Nature* 550 (2017): 354–359. Phần Phương pháp, mục "Select": Nhận xét 11.28.
16. Bertsekas, D. P., Tsitsiklis, J. N. *Neuro-Dynamic Programming*, Athena Scientific, 1996. §5.6: chứng minh Mệnh đề 11.9.
17. Bradtke, S. J., Duff, M. O. "Reinforcement Learning Methods for Continuous-Time Markov Decision Problems." *Advances in Neural Information Processing Systems 7*, MIT Press, 1995: 393–400. Mục 5.3.
