# Bài 10 — TRPO và PPO

## Mục tiêu học tập

Sau chương này, người học có thể:

1. **Đường cơ sở.** Chứng minh rằng trừ khỏi lợi tức một *đường cơ sở* (baseline) phụ thuộc trạng thái không làm chệch ước lượng gradient chính sách; tìm đường cơ sở hằng có phương sai nhỏ nhất trên bài toán một bước.
2. **Lợi thế và actor–critic.** Định nghĩa *hàm lợi thế* (advantage function), *critic* và *phương pháp actor–critic*; chứng minh rằng sai số sai phân thời gian (sai số TD) có kỳ vọng có điều kiện bằng lợi thế khi hàm giá trị đúng, và tính độ chệch khi hàm giá trị sai; thực hiện bằng tay hai bước actor–critic một bước.
3. **Ước lượng lợi thế tổng quát.** Chứng minh rằng *ước lượng lợi thế tổng quát* (generalized advantage estimation, GAE) bằng tổng chiết khấu các sai số TD; phân biệt tính không chệch cho gradient với tính không chệch cho lợi thế; tính GAE trên một *đoạn thu* (rollout) có cờ kết thúc và cờ cắt ngắn.
4. **Hiệu hiệu năng và hàm thay thế.** Phát biểu và chứng minh *bổ đề hiệu hiệu năng* (performance difference lemma); tính *hàm thay thế* (surrogate objective) và so với mức thay đổi thật của hàm mục tiêu; chứng minh hàm thay thế khớp hàm mục tiêu về giá trị và gradient tại tham số cũ.
5. **Chặn cải thiện và gradient tự nhiên.** Phát biểu *chặn cải thiện* cùng các giả thiết của nó và suy ra bài toán *miền tin cậy* (trust region); xấp xỉ *phân kỳ Kullback–Leibler* (Kullback–Leibler divergence, KL) bằng *ma trận thông tin Fisher* (Fisher information matrix); tính bằng tay bước *gradient tự nhiên* (natural gradient) và hai vòng *gradient liên hợp* (conjugate gradient) của phương pháp tối ưu chính sách miền tin cậy (Trust Region Policy Optimization, TRPO).
6. **Mục tiêu cắt và mục tiêu phạt của PPO.** Tính *mục tiêu cắt* (clipped objective) của phương pháp tối ưu chính sách gần kề (Proximal Policy Optimization, PPO) theo dấu của lợi thế và chỉ ra miền có gradient bằng $0$; chứng minh mục tiêu cắt không vượt mục tiêu không cắt, trùng giá trị và gradient tại tham số cũ; áp dụng quy tắc điều chỉnh hệ số phạt KL của *PPO-Penalty*.
7. **Một vòng PPO đầy đủ.** Mô tả một vòng PPO gồm thu đoạn, tính GAE, chuẩn hóa lợi thế, $K$ epoch tối ưu và các đại lượng chẩn đoán; phân biệt đại lượng giữ cố định với đại lượng tính lại; tính *approxKL* và *tỉ lệ cắt* (clip fraction) trên một mini-batch; chứng minh approxKL là ước lượng không chệch của KL khi tham số không phụ thuộc các mẫu dùng để lấy trung bình; nêu đúng phạm vi của kết quả hội tụ của *PPO-Clip* và vai trò của các chi tiết cài đặt.

<!-- note-topic-id: lec-10-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `09.k` chỉ ghi chú Bài 09, trừ Bài tập 09.11–09.20 thuộc tệp bài tập `exercises.md` của Bài 09; tương tự, `03.k`, …, `08.k` chỉ ghi chú Bài 03–08. Mỗi kết quả dưới đây được phát biểu lại ở dạng dùng được ngay.

- **Tính Markov, giá trị hành động theo giá trị trạng thái** (Bổ đề 03.20, Mệnh đề 03.22, 03.23). Với chính sách Markov dừng $\pi$, khi biết lịch sử tới $S_t=s$ và $A_t=a$, phần tương lai của lượt chỉ phụ thuộc $(s,a)$, và lợi tức $G_t$ có kỳ vọng $q_\pi(s,a)$. Giá trị hành động và giá trị trạng thái liên hệ bởi
  $$\begin{aligned}&q_\pi(s,a)=r(s,a)\\&\quad+\gamma\sum_{s'}P(s'\mid s,a)\,v_\pi(s'),\\&v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a),\end{aligned}$$
  trong đó $r(s,a)$ là phần thưởng kỳ vọng của một bước và $v_\pi=0$ tại trạng thái kết thúc.
- **Dạng ma trận** (Định nghĩa 03.26, Định lý 03.28). Trên tập $\mathcal S=\{s_1,\dots,s_n\}$ các trạng thái chưa kết thúc, ma trận chuyển dưới $\pi$ là $(P_\pi)_{ss'}=\sum_a\pi(a\mid s)P(s'\mid s,a)$; mỗi hàng không âm và có tổng không quá $1$, phần còn thiếu là xác suất đi tới trạng thái kết thúc. Với $0\le\gamma<1$, ma trận $I-\gamma P_\pi$ khả nghịch và có khai triển $(I-\gamma P_\pi)^{-1}=\sum_{k\ge0}\gamma^kP_\pi^k$.
- **Cải thiện chính sách** (Định lý 04.13). Cho $\pi$ Markov dừng với giá trị chính xác $v_\pi$, và $\pi'$ Markov dừng xác định thỏa $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$. Khi đó (a) $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s$; (b) bất đẳng thức là nghiêm ngặt tại $s$ nếu điều kiện nghiêm ngặt tại $s$.
- **Sai số TD và cập nhật bán gradient** (Định nghĩa 05.20, Mệnh đề 05.27, Bài tập 05.14; Định nghĩa 07.19, 07.21, Thuật toán 07.22). Sai số TD (temporal-difference error) của hàm giá trị $V$ là $\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$, với $V=0$ tại trạng thái kết thúc; khi $V=v_\pi$, $\mathbb E_\pi[\delta_t\mid S_t=s]=0$. Nếu $V$ giữ cố định trong cả lượt thì $G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$. Với hàm giá trị tham số hóa $\hat v(s,w)$, cập nhật bán gradient (semi-gradient) $w\leftarrow w+\alpha\,\delta_t\nabla_w\hat v(S_t,w)$ coi mục tiêu $R_{t+1}+\gamma\hat v(S_{t+1},w)$ là hằng.
- **Tỉ số lấy mẫu quan trọng** (Định nghĩa 06.24). Với chính sách đích $\pi$ và chính sách hành vi thỏa điều kiện hỗ trợ (mọi hành động có xác suất dương dưới $\pi$ cũng có xác suất dương dưới chính sách hành vi), tỉ số một bước là thương của xác suất chọn $A_t$ dưới $\pi$ và dưới chính sách hành vi. Trong chương này, chính sách hành vi luôn là chính sách $\pi_{\mathrm{old}}$ đã sinh dữ liệu, và chữ $b$ dành cho đường cơ sở.
- **Cờ kết thúc, cờ cắt ngắn, mất mát mini-batch, dừng gradient và bộ tối ưu** (Định nghĩa 08.4, 08.6, 08.10, 08.12, 08.16, 08.18). Cờ kết thúc $Z_{t+1}\in\{0,1\}$ bằng $1$ khi và chỉ khi quá trình quyết định Markov (Markov decision process, MDP) kết thúc tại bước $t+1$. Cờ cắt ngắn $U_{t+1}\in\{0,1\}$ bằng $1$ khi việc thu thập dừng vì một giới hạn không thuộc MDP, chẳng hạn giới hạn $500$ bước của CartPole; mục tiêu bootstrap chỉ nhân với mặt nạ $(1-Z_{t+1})$. Phép dừng gradient $\operatorname{sg}$ giữ giá trị và cho đạo hàm $0$; hạ gradient ngẫu nhiên (stochastic gradient descent, SGD) và Adam cực tiểu hóa trung bình mất mát trên mini-batch.
- **Chính sách tham số hóa, softmax, hàm mục tiêu** (Định nghĩa 09.10, 09.11, 09.14). Chính sách tham số hóa $\pi_\theta(a\mid s)$ là một phân phối trên $\mathcal A$ với mỗi $s$, khả vi theo $\theta\in\mathbb R^d$. Chính sách softmax với đặc trưng $\phi(s,a)$ là $\pi_\theta(a\mid s)=\exp(\phi(s,a)^\top\theta)/\sum_{a'}\exp(\phi(s,a')^\top\theta)$. Hàm mục tiêu là $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ với $G_0=\sum_{t=0}^{T-1}\gamma^tR_{t+1}$, kỳ vọng lấy theo $S_0\sim\mu_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$ và động lực $P$.
- **Hàm điểm** (Định nghĩa 09.15, Mệnh đề 09.16, 09.17). Hàm điểm (score function) là $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$. Khi miền hỗ trợ của $\pi_\theta(\cdot\mid s)$ không phụ thuộc $\theta$, $\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}[c\,\psi_\theta(s,A)]=0$ với mọi $c$ không phụ thuộc $A$. Với softmax hai hành động, đặc trưng đơn vị và $p=\pi_\theta(1\mid s)$, ta có $\psi_\theta(s,1)=(1-p)(1;\,-1)$ và $\psi_\theta(s,2)=-p\,(1;\,-1)$.
- **Quỹ đạo, lịch sử, phần thưởng quá khứ** (Định nghĩa 09.20, Bổ đề 09.21, 09.22). Lịch sử $H_t=(S_0,A_0,R_1,\dots,R_t,S_t)$ gồm mọi thứ đã quan sát khi chọn $A_t$. Với quy ước $\psi_t=\psi_\theta(S_t,A_t)$ khi $t<T$ và $\psi_t=0$ khi $t\ge T$, ta có $\mathbb E[\psi_t\mid H_t]=0$, nên phần thưởng quá khứ $\sum_{k<t}\gamma^kR_{k+1}$ nhân $\psi_t$ có kỳ vọng $0$. Hai tính chất của kỳ vọng có điều kiện được dùng: tính chất tháp $\mathbb E\bigl[\mathbb E[X\mid Y]\bigr]=\mathbb E[X]$, và $\mathbb E[WX\mid Y]=W\,\mathbb E[X\mid Y]$ khi $W$ là hàm của $Y$.
- **Định lý gradient chính sách** (Định lý 09.23, Hệ quả 09.24). Bốn giả thiết của định lý là:
  - (G1) phân phối đầu $\mu_0$ và động lực $P$ không phụ thuộc $\theta$, trạng thái có tính Markov;
  - (G2) với mọi $s$, $\pi_\theta(\cdot\mid s)$ khả vi theo $\theta$ và có miền hỗ trợ không đổi theo $\theta$;
  - (G3) $\lvert R_{t+1}\rvert\le R_{\max}$ và độ dài lượt $T\le T_{\max}$ hầu chắc chắn;
  - (G4) $\pi_\theta$ là chính sách softmax, hoặc Gaussian với phương sai cố định, có đặc trưng bị chặn.

  Dưới (G1)–(G4), gradient của hàm mục tiêu có hai dạng
  $$\begin{aligned}&\nabla_\theta J(\theta)\\&\quad=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_t\Bigr]\\&\quad=\frac1{1-\gamma}\,\mathbb E_{\substack{S\sim\nu^\pi\\A\sim\pi_\theta(\cdot\mid S)}}\bigl[q_\pi(S,A)\\&\qquad\times\psi_\theta(S,A)\bigr],\end{aligned}$$
  với $\pi=\pi_\theta$ và phân bố chiếm dụng chiết khấu (discounted occupancy distribution) $\nu^\pi(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi(S_t=s)$. Dạng thứ hai cần thêm chính sách Markov dừng và một trạng thái hấp thụ sau khi lượt kết thúc, nơi $q_\pi=0$.
- **REINFORCE** (Thuật toán 09.25, Hệ quả 09.26, Nhận xét 09.27; Ví dụ 09.20, 09.21). REINFORCE thu một lượt bằng $\pi_{\theta_{\mathrm{old}}}$, tính $\widehat g=\sum_t\gamma^tG_t\psi_t$ tại $\theta_{\mathrm{old}}$ rồi cập nhật $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\widehat g$. Dưới (G1)–(G4), $\mathbb E[\widehat g\mid\theta_{\mathrm{old}}]=\nabla_\theta J(\theta_{\mathrm{old}})$. Bỏ trọng số $\gamma^t$ làm kỳ vọng của ước lượng lệch khỏi $\nabla J$ khi $\gamma<1$.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một ví dụ hoặc một chứng minh được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương, trừ chữ $A$, có hai vai được nêu ngay sau bảng. Các ký hiệu riêng của một thuật toán, như $\tilde g_k$, $\omega_k$, $\xi_k$, $\tau_k$ của gradient liên hợp, được giới thiệu trong khối của thuật toán đó.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $S_t$; $\mathcal A$, $A_t$, $m$ | tập trạng thái chưa kết thúc, trạng thái ở bước $t$; tập hành động, hành động ở bước $t$, số hành động | hữu hạn trong các chứng minh dạng ma trận; $m\in\mathbb N_+$ |
| $R_{t+1}$, $r(s,a)$ | phần thưởng nhận sau $A_t$; phần thưởng kỳ vọng của cặp $(s,a)$ | $\mathbb R$, $\lvert R_{t+1}\rvert\le R_{\max}$ |
| $\gamma$, $T$, $G_t$ | hệ số chiết khấu; bước kết thúc của lượt; lợi tức từ bước $t$ | $[0,1)$ trong các định lý; biến ngẫu nhiên |
| $\mu_0$, $P(s'\mid s,a)$, $P_\pi$, $\Gamma_\pi$ | phân phối trạng thái đầu; xác suất chuyển; ma trận chuyển dưới $\pi$ trên $\mathcal S$; ma trận $(I-\gamma P_\pi)^{-1}$ | phân phối trên $\mathcal S$; $[0,1]$; $\mathbb R^{n\times n}$ |
| $\pi_\theta$, $\theta$, $d$; $\theta_{\mathrm{old}}$, $\pi_{\mathrm{old}}$; $\phi(s,a)$ | chính sách tham số hóa, tham số, số chiều; tham số và chính sách đã sinh dữ liệu; đặc trưng của chính sách softmax | $\theta\in\mathbb R^d$; $\mathbb R^d$ |
| $\sigma$; $\operatorname{sg}$ | hàm logistic $\sigma(x)=1/(1+e^{-x})$; dừng gradient | $\mathbb R\to(0,1)$; toán tử trong đồ thị tính |
| $H_t$ | lịch sử $(S_0,A_0,R_1,\dots,R_t,S_t)$, đã biết khi chọn $A_t$ | dãy hữu hạn |
| $p$, $p_A$, $p_B$ | xác suất chọn hành động 1 trong các ví dụ hai hành động | $(0,1)$ |
| $J(\theta)$, $\psi_\theta(s,a)$, $\psi_t$ | hàm mục tiêu; hàm điểm; viết gọn của $\psi_\theta(S_t,A_t)$, bằng $0$ khi $t\ge T$ | $\mathbb R$; $\mathbb R^d$ |
| $v_\pi$, $q_\pi$, $A_\pi$; $A_\pi(s,\pi')$ | giá trị trạng thái, giá trị hành động, lợi thế $q_\pi-v_\pi$; lợi thế trung bình của $\pi'$ so với $\pi$ tại $s$ | hàm thực |
| $b(s)$ | đường cơ sở | $\mathcal S\to\mathbb R$, bị chặn |
| $\hat v(s,w)$, $w$, $w_{\mathrm{old}}$, $\hat v_{\mathrm{old}}$ | hàm giá trị tham số hóa (critic từ Mục 2.4); tham số của nó; tham số lúc thu dữ liệu; viết gọn của $\hat v(\cdot,w_{\mathrm{old}})$ | $\mathbb R$; $\mathbb R^{d'}$ |
| $\delta_t$ | sai số TD có mặt nạ $(1-Z_{t+1})$ | $\mathbb R$ |
| $G_{t:t+n}$, $\widehat A^{(n)}_t$, $G^\lambda_t$, $\widehat A_t$ | lợi tức $n$ bước, lợi thế $n$ bước, lợi tức λ (λ-return), ước lượng lợi thế (GAE ở Mục 3; lợi thế đưa vào mục tiêu cắt, có thể đã chuẩn hóa, từ Mục 6.3) | $\mathbb R$ |
| $\widehat A^{\mathrm{raw}}_t$, $V^{\mathrm{targ}}_t$ | lợi thế GAE trước chuẩn hóa; mục tiêu của critic $\widehat A^{\mathrm{raw}}_t+\hat v_{\mathrm{old}}(S_t)$ | $\mathbb R$ |
| $\lambda$ | tham số của GAE | $[0,1]$ |
| $Z_{t+1}$, $U_{t+1}$ | cờ kết thúc của MDP, cờ cắt ngắn | $\{0,1\}$ |
| $\nu^\pi$, $\eta(s)$ | phân bố chiếm dụng chiết khấu chuẩn hóa, xét trên $\mathcal S$; số lần thăm kỳ vọng có chiết khấu, không chuẩn hóa | khối $\nu^\pi(\mathcal S)\le1$; $[0,\infty)$ |
| $\rho_\theta(s,a)$, $\rho_t(\theta)$ | tỉ số chính sách $\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$; giá trị tại mẫu, $\rho_\theta(S_t,A_t)$ | $[0,\infty)$ |
| $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$, $\mathcal L^{\mathrm{CPI}}$, $\mathcal L^{\mathrm{CLIP}}$, $\ell^{\mathrm{CLIP}}_t$ | hàm thay thế; hai hàm thay thế mẫu trên dữ liệu; số hạng cắt của một mẫu (đều được cực đại hóa) | $\mathbb R$ |
| $L(\theta,w)$, $L^V$ | hàm mất mát tổng và mất mát giá trị (đều được cực tiểu hóa) | $\mathbb R$ |
| $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$, $\widehat D$, $\mathcal H$ | biến phân toàn phần, KL tại một trạng thái, KL trung bình theo phân bố chiếm dụng, KL trung bình trên bộ đệm, entropy | $[0,1]$; $[0,\infty]$ |
| $\kappa$, $\kappa_{\mathrm{targ}}$; $\chi_{\pi'}$, $\bar\chi$ | bán kính miền tin cậy; KL mục tiêu của PPO-Penalty; hai hằng của chặn cải thiện | $(0,\infty)$; $[0,\infty)$ |
| $F$, $g$, $\Delta$ | ma trận Fisher; gradient của hàm thay thế tại $\theta_{\mathrm{old}}$; bước $\theta-\theta_{\mathrm{old}}$ | $\mathbb R^{d\times d}$; $\mathbb R^d$; $\mathbb R^d$ |
| $\epsilon$, $\beta$, $c_1$, $c_2$ | bán kính cắt; hệ số phạt KL; hai trọng số mất mát | $(0,1)$; $(0,\infty)$; $[0,\infty)$ |
| $N$, $h$, $K$, $M$, $E$; $\mathcal D$, $\mathcal B$ | số môi trường, độ dài đoạn thu, số epoch, cỡ mini-batch, số lượt của Thuật toán 10.6 và 10.9; bộ đệm $hN$ mẫu, tập chỉ số của một mini-batch | $\mathbb N_+$; tập |
| $\alpha$, $\alpha_\theta$, $\alpha_w$ | bước học | $(0,\infty)$ |

Quy ước đọc bảng gồm các điểm sau.

- $R_{t+1}$ gắn với chuyển từ bước $t$ sang bước $t+1$. Sau bước kết thúc $T$, lượt ở trong một trạng thái hấp thụ có phần thưởng $0$, nên $G_T=0$ và mọi giá trị, lợi thế tại đó bằng $0$. Ký hiệu $\log$ chỉ logarit tự nhiên. Khi tọa độ của véc-tơ có dấu phẩy thập phân, các tọa độ được ngăn bằng dấu chấm phẩy, như $(0{,}2;\,0{,}3)$.
- Chữ $A$ có hai vai. $A_t$, có chỉ số thời gian, là hành động; $A_\pi$, có chỉ số chính sách, và $\widehat A_t$, có dấu mũ, là lợi thế. Bài giảng gốc và các bài báo về TRPO, GAE, PPO đều dùng chữ $A$ cho lợi thế, nên chúng ta giữ chữ này; hai vai luôn được phân biệt bằng chỉ số hoặc dấu mũ, như trong $A_\pi(S_t,A_t)$.
- Có hai loại trung bình. Kỳ vọng lý thuyết $\mathbb E_{S\sim\nu^\pi}$ có trọng số chiết khấu $(1-\gamma)\gamma^t$ theo thời điểm thăm. Trung bình thực hành $\widehat{\mathbb E}_{\mathcal D}$ là trung bình đều trên các mẫu của một bộ đệm $\mathcal D$. Hai đại lượng khác nhau.
- Bài 09 viết phân phối đầu là $\rho_0$; ở đây viết $\mu_0$ vì chữ $\rho$ dành cho tỉ số chính sách. Sutton và Barto (2018, Chương 13) viết chính sách là $\pi(a\mid s,\boldsymbol\theta)$ và hai bước học là $\alpha^{\boldsymbol\theta}$, $\alpha^{\mathbf w}$; ở đây viết $\pi_\theta(a\mid s)$, $\alpha_\theta$, $\alpha_w$, còn $\hat v(s,w)$ giữ nguyên.
- Ký hiệu của các bài báo ứng với ký hiệu của chương như sau:
  - $\rho_\pi$ của Schulman và cộng sự (2015) là $\eta=\nu^\pi/(1-\gamma)$, bán kính $\delta$ của bài báo đó là $\kappa$, hằng $\epsilon$ trong Định lý 1 của bài báo đó là $\bar\chi$;
  - tỉ số $r_t(\theta)$ của Schulman và cộng sự (2017) là $\rho_t(\theta)$, độ dài đoạn $T$ của bài báo này và của bài giảng gốc (tr. 24) là $h$;
  - phần thưởng $r_t$ của các bài báo về GAE và PPO là $R_{t+1}$;
  - phân bố $d^\pi$ của bài giảng gốc và của Achiam và cộng sự (2017) là $\nu^\pi$, hằng $\epsilon^{\pi'}$ của Achiam và cộng sự là $\chi_{\pi'}$.
- Ứng với giáo trình *Học máy thống kê*: $v_\pi$, $q_\pi$ là $V^\pi$, $Q^\pi$.
- Số liệu trong các ví dụ là số liệu sư phạm tự xây dựng, trừ các số đo lấy từ notebook thực hành của Bài 09 và bảng siêu tham số của bài báo PPO, có ghi nguồn tại chỗ dùng.

---

## Bản đồ chủ đề (bốn nhóm)

Mỗi chủ đề có một mã. Cột "Nguồn trang" ghi trang của bài giảng gốc (`lecture10_policy_gradient_part2.pdf`, 43 trang) và mục của sách hoặc bài báo; cột "Mục" ghi mục của chương. Tình huống áp dụng, tóm tắt chương và bài tập củng cố thuộc `lec-10-topic-23`, dù đứng sau Mục 7.6.

### Nhóm cầu nối

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-10-topic-01` | Kiến thức tiên quyết, ký hiệu, quy ước về phân bố chiếm dụng | tr. 5–8; ghi chú Bài 03–09 | Phát biểu lại các kết quả của Bài 03–09 được dùng; đổi ký hiệu $s_t$, $r_t$, $d^\pi$, $V^\pi$ của bài giảng gốc sang ký hiệu của học phần | Vào: Bài 03–09 → Ra: danh sách tiên quyết, bảng ký hiệu, quy ước đọc | phần đầu |
| `lec-10-topic-02` | Hai giới hạn của REINFORCE và bài toán trung tâm | tr. 3–4, 9–10, 14 | Định lượng phương sai của REINFORCE và tác hại của một bước lớn bằng hai ví dụ tính tay, với trọng số $\gamma^t$ của Thuật toán 09.25 | Vào: Định lý 09.23, Hệ quả 09.26 → Ra: bài toán trung tâm, cấu trúc chương | 1 |
| `lec-10-topic-07` | Lợi tức $n$ bước và lợi thế $n$ bước | Sutton và Barto §7.1, §12.1; Bài tập 05.14 | Các bài trước chỉ có dạng Monte Carlo của tổng sai số TD; GAE được xây từ lợi tức $n$ bước | Vào: sai số TD, critic → Ra: lợi thế $n$ bước bằng tổng sai số TD | 3.1 |
| `lec-10-topic-12` | Biến phân toàn phần, phân kỳ KL, bất đẳng thức Pinsker | Cover và Thomas (2006) Bổ đề 11.6.1; Achiam và cộng sự (2017) | Hai khoảng cách giữa phân phối hành động, dùng trong chặn cải thiện, TRPO và PPO, chưa được định nghĩa ở các bài trước | Vào: hàm thay thế → Ra: KL không âm, Pinsker | 4.3 |
| `lec-10-topic-23` | Tổng kết, tình huống áp dụng, tóm tắt, bài tập | tr. 28, 42; notebook Bài 09 | Đặt mỗi kết quả cạnh giả thiết của nó và trả lời bài toán trung tâm có điều kiện | Vào: Mục 1–6 → Ra: bảng tổng kết, ba tình huống áp dụng, mười hai bài tập | 7.1–7.5, cuối chương |

### Nhóm cốt lõi

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-10-topic-03` | Đường cơ sở phụ thuộc trạng thái | tr. 11; Sutton và Barto §13.4 | Giảm phương sai mà giữ kỳ vọng của ước lượng gradient | Vào: Định lý 09.23, Mệnh đề 09.17 → Ra: ước lượng có đường cơ sở không chệch | 2.1 |
| `lec-10-topic-05` | Hàm lợi thế; REINFORCE có đường cơ sở | tr. 5, 8, 11; Sutton và Barto §13.4 | Đặt tên cho đại lượng mà mọi phương pháp sau ước lượng | Vào: đường cơ sở, Hệ quả 09.24 → Ra: gradient dạng lợi thế, thuật toán REINFORCE có đường cơ sở | 2.3 |
| `lec-10-topic-06` | Critic, actor, sai số TD, actor–critic một bước | tr. 12–13; Sutton và Barto §13.5 | Thay lợi tức Monte Carlo bằng mục tiêu một bước | Vào: hàm lợi thế, sai số TD → Ra: kỳ vọng của sai số TD, thuật toán actor–critic một bước | 2.4 |
| `lec-10-topic-08` | Lợi tức λ và GAE | tr. 13; Schulman và cộng sự (2016) §3; Sutton và Barto §12.1 | Điều chỉnh giữa sai số TD một bước và lợi tức Monte Carlo | Vào: lợi thế $n$ bước → Ra: dạng tổng, truy hồi, tính không chệch cho gradient | 3.2 |
| `lec-10-topic-09` | GAE trên đoạn thu | tr. 24; Sutton và Barto §12.3 | Tính GAE trên dữ liệu có biên đoạn, kết thúc và cắt ngắn | Vào: GAE, cờ $Z$, $U$ → Ra: thuật toán tính lùi, mục tiêu của critic | 3.3 |
| `lec-10-topic-10` | Bổ đề hiệu hiệu năng | tr. 4, 14–15; Kakade và Langford (2002) | Đẳng thức chính xác cho $J(\pi')-J(\pi)$ | Vào: hàm lợi thế, dạng ma trận → Ra: hiệu hiệu năng, cải thiện chính sách cho chính sách ngẫu nhiên | 4.1 |
| `lec-10-topic-11` | Tỉ số chính sách và hàm thay thế | tr. 15; Schulman và cộng sự (2015) | Đánh giá chính sách mới bằng dữ liệu của chính sách cũ | Vào: hiệu hiệu năng → Ra: hàm thay thế khớp $J$ đến bậc một | 4.2 |
| `lec-10-topic-13` | Chặn cải thiện | tr. 14, 16; Achiam và cộng sự (2017) | Căn cứ định lượng cho việc giới hạn độ lớn bước cập nhật | Vào: hàm thay thế, KL, TV → Ra: cận dưới của $J(\pi')-J(\pi)$ | 4.4 |
| `lec-10-topic-14` | Cải thiện đơn điệu và bài toán miền tin cậy | tr. 16; Schulman và cộng sự (2015) §3 | Từ cận dưới sang bài toán tối ưu của TRPO | Vào: chặn cải thiện → Ra: bài toán miền tin cậy | 4.5 |
| `lec-10-topic-15` | KL bậc hai, ma trận Fisher, gradient tự nhiên | tr. 17; Schulman và cộng sự (2015) §7 | Giải xấp xỉ bài toán miền tin cậy | Vào: bài toán miền tin cậy → Ra: bước theo hướng $F^{-1}g$ | 5.1 |
| `lec-10-topic-16` | TRPO thực hành | tr. 18–19; Nocedal và Wright (2006) Chương 5 | Tính bước mà không lập ma trận Fisher | Vào: gradient tự nhiên → Ra: thuật toán TRPO | 5.2 |
| `lec-10-topic-17` | PPO-Clip | tr. 20–22, 35; Schulman và cộng sự (2017) §3 | Thay ràng buộc KL bằng mục tiêu cắt tỉ số, tối ưu bằng phương pháp bậc một | Vào: hàm thay thế, TRPO → Ra: dạng theo dấu, chặn dưới bi quan | 6.1 |
| `lec-10-topic-18` | PPO-Penalty | tr. 38; Schulman và cộng sự (2017) §4 | Biến thể phạt KL với hệ số thích nghi | Vào: KL, PPO-Clip → Ra: quy tắc điều chỉnh $\beta$ | 6.2 |
| `lec-10-topic-19` | Hàm mất mát tổng, chẩn đoán, thuật toán PPO | tr. 23–25, 27, 35; Schulman và cộng sự (2017) Thuật toán 1 | Ghép actor, critic và GAE thành một vòng lặp | Vào: GAE trên đoạn thu, PPO-Clip → Ra: thuật toán PPO, approxKL | 6.3 |
| `lec-10-topic-20` | Đọc chẩn đoán, siêu tham số, so sánh TRPO với PPO | tr. 26–28, 35; Schulman và cộng sự (2017) Bảng 3, 5 | Đọc trạng thái huấn luyện và chọn cấu hình có nguồn | Vào: thuật toán PPO → Ra: bảng siêu tham số, bảng so sánh | 6.4 |
| `lec-10-topic-21` | Chi tiết cài đặt và kết quả loại bỏ | tr. 29–34, 36; Engstrom và cộng sự (2020); Huang và cộng sự (2022) | Đọc PPO như một công thức cài đặt; kết luận định tính về vai trò của từng chi tiết | Vào: thuật toán PPO → Ra: bảng chi tiết và thành phần bị thay đổi | 6.5 |

### Nhóm bổ sung

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-10-topic-04` | Đường cơ sở có phương sai nhỏ nhất | Greensmith, Bartlett và Baxter (2004) §5 | Bài giảng gốc (tr. 11) và Sutton và Barto (§13.4) không định lượng mức giảm phương sai; đường cơ sở tối ưu nói chung khác $v_\pi$ | Vào: đường cơ sở → Ra: công thức của đường cơ sở tối ưu trên bài toán một bước | 2.2 |

### Nhóm đọc thêm

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra | Mục |
|---|---|---|---|---|---|
| `lec-10-topic-22` | Hội tụ về điểm dừng của PPO-Clip | tr. 37, 39–42; Jin, Li và Wang (2024) | Phạm vi của tuyên bố lý thuyết về PPO; phát biểu, không chứng minh | Vào: PPO-Clip → Ra: kết quả có giả thiết và phạm vi | 6.6 |
| `lec-10-topic-24` | Phần II của bài giảng gốc và các biến thể mới | tr. 2–3, 43 | Định vị các phương pháp thuộc Bài 11 | Vào: tổng kết → Ra: chuyển sang Bài 11 | 7.6 |

### Bảy phần của chương

Chúng ta đi qua bảy phần sau.

1. Hai giới hạn của REINFORCE: hai ví dụ định lượng và bài toán trung tâm (`lec-10-topic-02`); phần đầu chương, gồm kiến thức tiên quyết và ký hiệu, là `lec-10-topic-01`.
2. Đường cơ sở, hàm lợi thế và actor–critic: đường cơ sở không làm chệch, đường cơ sở có phương sai nhỏ nhất, hàm lợi thế, actor–critic một bước (`lec-10-topic-03`, `lec-10-topic-04`, `lec-10-topic-05`, `lec-10-topic-06`).
3. Ước lượng lợi thế tổng quát: lợi tức $n$ bước, lợi tức λ và GAE, GAE trên đoạn thu (`lec-10-topic-07`, `lec-10-topic-08`, `lec-10-topic-09`).
4. Hàm thay thế và chặn cải thiện: bổ đề hiệu hiệu năng, hàm thay thế, khoảng cách giữa hai chính sách, chặn cải thiện, bài toán miền tin cậy (`lec-10-topic-10` đến `lec-10-topic-14`).
5. TRPO và gradient tự nhiên: KL bậc hai, ma trận Fisher, gradient liên hợp, tìm kiếm lùi (`lec-10-topic-15`, `lec-10-topic-16`).
6. Tối ưu chính sách gần kề: PPO-Clip, PPO-Penalty, thuật toán PPO, chẩn đoán, chi tiết cài đặt, hội tụ về điểm dừng (`lec-10-topic-17` đến `lec-10-topic-22`).
7. Tổng kết và chuyển tiếp: kết quả và giả thiết, so sánh phương pháp, chuyển sang Bài 11 (`lec-10-topic-23`, `lec-10-topic-24`); tình huống áp dụng, tóm tắt và bài tập cuối chương thuộc `lec-10-topic-23`.

Đọc trước: Sutton và Barto (2018), §13.4–13.5 và §12.1–12.3; Schulman và cộng sự (2017), §3–5.

---

## 1. Hai giới hạn của REINFORCE

<!-- note-topic-id: lec-10-topic-02 -->
### 1.1 Kết quả kế thừa và bài toán trung tâm

Bài 09 kết thúc với thuật toán REINFORCE (Thuật toán 09.25). Thuật toán thu một lượt bằng chính sách $\pi_{\theta_{\mathrm{old}}}$, tính lợi tức $G_t$ của từng bước, rồi cập nhật tham số theo ước lượng
$$\widehat g=\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_{\theta_{\mathrm{old}}}(S_t,A_t).$$
Mỗi hàm điểm được nhân với lợi tức đến sau nó và với trọng số chiết khấu $\gamma^t$. Dưới các giả thiết (G1)–(G4) của Định lý 09.23, Hệ quả 09.26 cho $\mathbb E[\widehat g\mid\theta_{\mathrm{old}}]=\nabla_\theta J(\theta_{\mathrm{old}})$, nghĩa là mỗi lượt cho một mẫu không chệch của gradient; Ví dụ 09.21 cho thấy bỏ trọng số $\gamma^t$ làm mất tính chất này khi $\gamma<1$. Tính không chệch là một khẳng định về trung bình trên nhiều lượt. Hai ví dụ sau đo điều xảy ra trên từng lượt.

![Thẻ dữ kiện bài toán một bước, chính sách softmax, hai hành động: bảng hai cột cho a bằng 1 và a bằng 2, đặc trưng phi của s, a bằng (1; 0) và (0; 1); xác suất pi theta bằng 2/3 và 1/3; phần thưởng r bằng 3 và 0. Dòng dưới: theta bằng (log 2; 0), lượt dừng sau A 0.](img/lec-09/one-step-card.svg)

Thẻ trên là bài toán một bước của Bài 09: một trạng thái, hai hành động, lượt dừng sau hành động đầu tiên.

::: example Ví dụ 10.1 (Phương sai của REINFORCE trên bài toán một bước)
**Dữ kiện.** Một trạng thái $s$, hai hành động, lượt dừng sau hành động đầu tiên. Chính sách softmax với đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ và $\theta=(\log2;\,0)$, nên $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$. Phần thưởng $r(1)=3$, $r(2)=0$. Hàm điểm $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$ (Mệnh đề 09.16). Vì $T=1$, ước lượng REINFORCE là $\widehat g=G_0\,\psi_\theta(s,A_0)$ với $G_0=r(A_0)$.

**Phân phối của $\widehat g$.** Với xác suất $\tfrac23$, $A_0=1$ và $\widehat g=3\,(\tfrac13;\,-\tfrac13)=(1;\,-1)$. Với xác suất $\tfrac13$, $A_0=2$ và $\widehat g=(0;\,0)$. Kỳ vọng là $\tfrac23(1;\,-1)=(\tfrac23;\,-\tfrac23)$, bằng gradient đúng $\nabla_\theta J$.

**Phương sai.** Ta đo phương sai của một véc-tơ ngẫu nhiên $X$ bằng tổng phương sai các tọa độ, $\operatorname{Var}(X)=\mathbb E\lVert X-\mathbb EX\rVert^2$. Mỗi tọa độ của $\widehat g$ có mô men bậc hai $\tfrac23\cdot1=\tfrac23$ và phương sai $\tfrac23-\tfrac49=\tfrac29$, nên $\operatorname{Var}(\widehat g)=\tfrac49$.

**Cộng một hằng vào phần thưởng.** Với $r=(4;\,1)$, $\widehat g=4\,(\tfrac13;\,-\tfrac13)=(\tfrac43;\,-\tfrac43)$ với xác suất $\tfrac23$ và $\widehat g=(-\tfrac23;\,\tfrac23)$ với xác suất $\tfrac13$. Tọa độ thứ nhất có kỳ vọng $\tfrac23\cdot\tfrac43-\tfrac13\cdot\tfrac23=\tfrac23$, nên gradient không đổi. Mô men bậc hai của mỗi tọa độ là $\tfrac23\cdot\tfrac{16}9+\tfrac13\cdot\tfrac49=\tfrac43$, phương sai là $\tfrac43-\tfrac49=\tfrac89$, và $\operatorname{Var}(\widehat g)=\tfrac{16}9$.

**Diễn giải.** Trên bài toán một bước, cộng $1$ vào phần thưởng làm $J$ tăng đúng $1$ với mọi $\theta$, nên không đổi gradient và không đổi chính sách tốt nhất; tổng phương sai thì tăng gấp bốn. Phương sai của REINFORCE vì vậy phụ thuộc vào mức chung của phần thưởng, một đại lượng không ảnh hưởng tới việc chọn hành động.

**Kiểm tra lại.** $\operatorname{Var}(\widehat g)=\mathbb E\lVert\widehat g\rVert^2-\lVert\nabla_\theta J\rVert^2$. Với $r=(3;\,0)$: $\tfrac23\cdot2-\tfrac89=\tfrac49$. Với $r=(4;\,1)$: $\tfrac23\cdot\tfrac{32}9+\tfrac13\cdot\tfrac89-\tfrac89=\tfrac{64+8-24}{27}=\tfrac{16}9$.
:::

Ví dụ sau cho thấy hậu quả của phương sai lớn trên một lượt: bước cập nhật có thể ngược chiều gradient.

::: example Ví dụ 10.2 (Một lượt REINFORCE đi ngược chiều gradient trên hành lang ngắn)
**Dữ kiện.** Hành lang ngắn đảo hành động (Sutton và Barto, 2018, Ví dụ 13.1; Bài tập 09.20): bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc lượt); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 là "sang phải", hành động 2 là "sang trái"; ở $s_2$ hai hành động bị đảo; sang trái tại $s_1$ thì đứng yên. Mọi ô có cùng đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, nên chính sách softmax chọn hành động 1 với cùng xác suất $p=\pi_\theta(1\mid s)$ ở mọi ô. Tại $\theta=(0;\,0)$: $p=\tfrac12$, $\psi_\theta(s,1)=(\tfrac12;\,-\tfrac12)$, $\psi_\theta(s,2)=(-\tfrac12;\,\tfrac12)$. Hàm mục tiêu là $J(p)=-2(2-p)/\bigl(p(1-p)\bigr)$, nên $J(\tfrac12)=-12$. Vì $J'(\tfrac12)=8$ và $\partial p/\partial\theta_1=-\partial p/\partial\theta_2=p(1-p)=\tfrac14$, gradient đúng là $\nabla_\theta J=(2;\,-2)$ (Bài tập 09.20 trong tệp bài tập của Bài 09). Hành lang có $\gamma=1$ và độ dài lượt không bị chặn, nên không thỏa (G3); đoạn sau Ví dụ 10.4 nêu căn cứ để ước lượng REINFORCE vẫn không chệch trên hành lang. Bước học $\alpha=0{,}1$.

**Lượt.** Các hành động $A_0,\dots,A_4=1,1,1,2,1$ cho dãy trạng thái $s_1,s_2,s_1,s_2,s_3$ rồi tới đích $s_4$, nên $T=5$ và $G_t=-(5-t)$, tức $-5,-4,-3,-2,-1$.

**Ước lượng.** Với $\gamma=1$, $\widehat g=\sum_tG_t\psi_t$. Bốn bước chọn hành động 1 có tọa độ thứ nhất của hàm điểm bằng $\tfrac12$, bước $t=3$ chọn hành động 2 có tọa độ đó bằng $-\tfrac12$, nên tọa độ thứ nhất của $\widehat g$ là
$$
\begin{aligned}
&\tfrac12(-5-4-3-1)\\
&\quad+\bigl(-\tfrac12\bigr)(-2)\\
&\quad=-6{,}5+1\\
&\quad=-5{,}5.
\end{aligned}
$$
Tọa độ thứ hai ngược dấu, nên $\widehat g=(-5{,}5;\,5{,}5)$, ngược chiều $\nabla_\theta J=(2;\,-2)$.

**Cập nhật.** Bước tăng gradient cho

- hướng: $\alpha\widehat g=(-0{,}55;\,0{,}55)$;
- tham số mới: $\theta=(0;\,0)+(-0{,}55;\,0{,}55)=(-0{,}55;\,0{,}55)$;
- xác suất mới: $p=\sigma(\theta_1-\theta_2)=\sigma(-1{,}1)=0{,}2497$, với hàm logistic $\sigma(x)=1/(1+e^{-x})$.

Hàm mục tiêu giảm từ $J(0{,}5)=-12$ xuống $J(0{,}2497)=-18{,}68$.

**Diễn giải.** Mọi phần thưởng âm nên mọi $G_t<0$, và mỗi hành động đã chọn bị giảm xác suất theo $\lvert G_t\rvert$. Lượt này chọn hành động 1 bốn lần, nên $p$ giảm từ $0{,}5$ xuống $0{,}25$, xa dần giá trị tốt nhất $p^*=2-\sqrt2\approx0{,}59$ (Bài tập 09.14 trong tệp bài tập của Bài 09). Ước lượng không chệch vẫn có thể cho một bước ngược chiều gradient trên một lượt cụ thể. Bài giảng gốc (tr. 10) nêu hiện tượng này bằng câu "một lượt may hoặc rủi có thể chi phối gradient".

**Kiểm tra lại.** Với $p=0{,}24974$: $p(1-p)=0{,}18737$ và $2(2-p)=3{,}50052$, nên $J=-3{,}50052/0{,}18737=-18{,}68$.
:::

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

Trên hình, lượt của Ví dụ 10.2 đi $s_1\to s_2\to s_1\to s_2\to s_3\to s_4$; lần chọn "sang phải" tại ô viền nét đứt $s_2$ đưa tác tử lùi về $s_1$.

Trên Breakout, notebook thực hành thứ hai của Bài 09 cho thấy REINFORCE chỉ học được một hành vi gần hằng sau $10^6$ bước, khi nhiều lượt có $\widehat g=0$; Tình huống 10.3 tách phần hiện tượng mà đường cơ sở và critic xử lý được khỏi phần thuộc về thăm dò.

Giới hạn thứ hai nằm ở cách dùng dữ liệu. Hệ quả 09.26 cần lượt do chính $\pi_{\theta_{\mathrm{old}}}$ sinh ra, nên sau một bước cập nhật, lượt vừa dùng thuộc về chính sách cũ và không còn cho mẫu không chệch của gradient tại tham số mới. REINFORCE vì vậy dùng mỗi lượt cho đúng một bước. Muốn mỗi lượt đem lại nhiều tiến bộ hơn, chúng ta cần bước lớn hơn; nhưng bước lớn đổi chính sách, chính sách mới thăm các trạng thái theo một phân bố khác, và kết quả có thể tệ đi (bài giảng gốc, tr. 4, 14). Trên hành lang của Ví dụ 10.2, ta tính một bước theo đúng gradient $(2;\,-2)$ từ $\theta=(0;\,0)$ với hai bước học:

- $\alpha=0{,}1$ cho $\theta=(0{,}2;\,-0{,}2)$, $p=\sigma(0{,}4)=0{,}5987$ và $J=-11{,}66$, tức $J$ tăng;
- $\alpha=0{,}5$ cho $\theta=(1;\,-1)$, $p=\sigma(2)=0{,}8808$, vượt qua $p^*\approx0{,}59$, và $J=-21{,}32$, tức $J$ giảm $9{,}32$.

Cùng một hướng đúng, bước nhỏ làm $J$ tăng còn bước lớn làm $J$ giảm, vì $J$ chỉ gần tuyến tính trong một lân cận nhỏ của chính sách cũ.

Hai giới hạn này dẫn tới **bài toán trung tâm của chương**: giảm phương sai của ước lượng gradient mà vẫn giữ kỳ vọng của nó, và dùng lại dữ liệu của $\pi_{\mathrm{old}}$ để chọn một bước cập nhật lớn mà chính sách mới không kém chính sách cũ.

![Hai hàng khung nối bằng mũi tên. Hàng trên, viền liền, nhãn phương sai của ước lượng gradient: khung đường cơ sở và critic, với G t trừ v mũ của S t và sai số TD delta t (Mục 2), dẫn tới khung GAE, A mũ t bằng tổng theo k của (gamma lambda) mũ k nhân delta t cộng k (Mục 3). Hàng dưới, viền nét đứt, nhãn độ lớn bước cập nhật: khung hàm thay thế và chặn cải thiện (Mục 4), dẫn tới khung TRPO, KL trung bình không vượt kappa (Mục 5), rồi khung PPO, cắt tỉ số rho t vào đoạn từ 1 trừ epsilon đến 1 cộng epsilon (Mục 6). Hai hàng gặp nhau ở khung cuối, viền đậm: Thuật toán 10.49, PPO kiểu actor–critic, GAE cho lợi thế và mục tiêu cắt cho chính sách.](img/lec-10/central-problem.svg)

Trên hình, các mục xếp thành hai chuỗi, mỗi chuỗi trả lời một nửa của bài toán trung tâm. Hàng trên giảm phương sai: ở Mục 2, chúng ta trừ đường cơ sở và bootstrap từ một hàm giá trị học được; ở Mục 3, chúng ta trộn các ước lượng nhiều bước thành GAE. Hàng dưới giới hạn bước cập nhật: ở Mục 4, chúng ta chặn mức thay đổi của $J$ theo khoảng cách giữa hai chính sách; ở Mục 5, chúng ta giải bài toán có ràng buộc KL; ở Mục 6, chúng ta thay ràng buộc bằng phép cắt tỉ số. Hai hàng gặp nhau ở thuật toán PPO, nơi lợi thế ước lượng bằng GAE đi vào mục tiêu cắt.

Chúng ta trả lời bài toán theo từng mục; mỗi câu trả lời dưới đây đúng dưới một điều kiện.

- **Mục 2.** Trừ khỏi lợi tức một đường cơ sở không phụ thuộc hành động đã chọn không đổi kỳ vọng của ước lượng gradient; với hàm giá trị bằng $v_\pi$, sai số TD có kỳ vọng có điều kiện bằng lợi thế.
- **Mục 3.** GAE là tổng các sai số TD với trọng số $(\gamma\lambda)^k$; ước lượng gradient dùng GAE không chệch khi $\lambda=1$ với lượt đầy đủ, hoặc khi hàm giá trị bằng $v_\pi$.
- **Mục 4.** Với lợi thế và phân bố chiếm dụng chính xác, $J(\pi')-J(\pi)$ không nhỏ hơn mức tăng mà một xấp xỉ từ dữ liệu cũ dự báo, trừ một số hạng tăng theo khoảng cách trung bình giữa hai chính sách; bước miền tin cậy giải chính xác với bán kính $\kappa$ làm $J$ giảm không quá một hằng nhân $\sqrt\kappa$.
- **Mục 5.** Nếu khoảng cách giữa hai chính sách được xấp xỉ bậc hai, thì bước tốt nhất đi theo hướng gradient tự nhiên; gradient liên hợp và tìm kiếm lùi (backtracking line search) tính bước này mà không lập ma trận bậc hai, và chỉ bảo đảm KL trung bình trên mẫu không vượt $\kappa$.
- **Mục 6.** Mục tiêu cắt tỉ số là cận dưới của mục tiêu không cắt, trùng giá trị và gradient tại tham số cũ, và tối ưu được bằng Adam trên mini-batch; đổi lại, không còn cận lý thuyết nào cho KL.

Như vậy, chúng ta đã định lượng hai giới hạn của REINFORCE. Tổng phương sai của ước lượng tăng từ $\tfrac49$ lên $\tfrac{16}9$ chỉ vì cộng một hằng vào phần thưởng (Ví dụ 10.1), và một lượt cụ thể có thể cho bước ngược chiều gradient (Ví dụ 10.2); hai hiện tượng này không mâu thuẫn với Hệ quả 09.26, vì tính không chệch chỉ nói về trung bình. Ngay cả bước theo đúng gradient trên hành lang cũng làm $J$ giảm từ $-12$ xuống $-21{,}32$ khi $\alpha=0{,}5$. Trong Mục 2, chúng ta xử lý giới hạn thứ nhất bằng cách so mỗi lợi tức với một mức chung của trạng thái, và chứng minh rằng phép so sánh này không làm chệch ước lượng.

---

## 2. Đường cơ sở, hàm lợi thế và actor–critic

Trong ước lượng $\widehat g$ của Ví dụ 10.1, mỗi hàm điểm được nhân với cả lợi tức, kể cả phần chung mà mọi hành động đều nhận; phần chung đó không phân biệt hành động tốt với hành động kém, nhưng làm các mẫu dao động, và cộng $1$ vào phần thưởng đưa tổng phương sai từ $\tfrac49$ lên $\tfrac{16}9$. Để giảm phương sai mà không đổi kỳ vọng, chúng ta trừ khỏi $G_t$ một mức so sánh không phụ thuộc hành động đã chọn, tìm mức tốt nhất trên bài toán một bước, đặt tên cho đại lượng còn lại sau phép trừ, rồi thay lợi tức Monte Carlo bằng một hàm giá trị học được để cập nhật ngay sau từng bước.

<!-- note-topic-id: lec-10-topic-03 -->
### 2.1 Đường cơ sở

Về mặt ý tưởng, một hành động tốt là hành động cho lợi tức cao hơn mức thường đạt được tại trạng thái đó, nên ta so mỗi lợi tức $G_t$ với một mức $b(S_t)$ của trạng thái và chỉ dùng phần chênh lệch $G_t-b(S_t)$. Sutton và Barto (2018, §13.4, tr. 329) liên hệ ý này với bài toán nhiều cần gạt (multi-armed bandit), nơi mức so sánh là một số, và giải thích vì sao trong một MDP mức so sánh phải thay đổi theo trạng thái: ở trạng thái mà mọi hành động đều có giá trị cao, mức so sánh phải cao thì mới phân biệt được hành động tốt hơn với hành động kém hơn. Ví dụ sau cho thấy phép trừ tác động lên kỳ vọng và phương sai.

::: example Ví dụ 10.3 (Ba đường cơ sở trên bài toán một bước)
**Dữ kiện.** Như Ví dụ 10.1: một trạng thái $s$, lượt dừng sau một hành động, $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$, $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$, gradient đúng $(\tfrac23;\,-\tfrac23)$. Giá trị trạng thái là $v_\pi(s)=\tfrac23\cdot3=2$. Với một hằng $b$, ước lượng có đường cơ sở là $X_b=\bigl(r(A)-b\bigr)\psi_\theta(s,A)$, $A\sim\pi_\theta(\cdot\mid s)$.

**Kỳ vọng.** Với mọi $b$,
$$
\begin{aligned}
&\mathbb E[X_b]\\
&\quad=\tfrac23(3-b)\,\psi_\theta(s,1)\\
&\qquad+\tfrac13(0-b)\,\psi_\theta(s,2)\\
&\quad=\tfrac23\cdot3\,\psi_\theta(s,1)\\
&\qquad-b\bigl(\tfrac23\psi_\theta(s,1)\\
&\qquad\quad+\tfrac13\psi_\theta(s,2)\bigr)\\
&\quad=(\tfrac23;\,-\tfrac23)-b\,(0;\,0).
\end{aligned}
$$
Đẳng thức cuối dùng $\tfrac23\cdot\tfrac13+\tfrac13\cdot(-\tfrac23)=0$, tức kỳ vọng của hàm điểm bằng $0$ (Mệnh đề 09.17).

**Ba đường cơ sở.**

- $b=0$: $X_0$ là ước lượng REINFORCE của Ví dụ 10.1, tổng phương sai $\tfrac49$.
- $b=2=v_\pi(s)$: $X_2=(\tfrac13;\,-\tfrac13)$ với xác suất $\tfrac23$ và $X_2=(-2)(-\tfrac23;\,\tfrac23)=(\tfrac43;\,-\tfrac43)$ với xác suất $\tfrac13$. Mỗi tọa độ có mô men bậc hai $\tfrac23\cdot\tfrac19+\tfrac13\cdot\tfrac{16}9=\tfrac23$ và phương sai $\tfrac23-\tfrac49=\tfrac29$, nên tổng phương sai vẫn là $\tfrac49$.
- $b=1$: $X_1=2\,(\tfrac13;\,-\tfrac13)=(\tfrac23;\,-\tfrac23)$ khi $A=1$ và $X_1=(-1)(-\tfrac23;\,\tfrac23)=(\tfrac23;\,-\tfrac23)$ khi $A=2$. Mọi mẫu bằng gradient, nên tổng phương sai bằng $0$.

**Công thức chung.** Với $\lVert\psi_\theta(s,1)\rVert^2=\tfrac29$, $\lVert\psi_\theta(s,2)\rVert^2=\tfrac89$ và $\lVert(\tfrac23;\,-\tfrac23)\rVert^2=\tfrac89$,
$$
\begin{aligned}
&\operatorname{Var}(X_b)\\
&\quad=\mathbb E\lVert X_b\rVert^2-\tfrac89\\
&\quad=\tfrac23(3-b)^2\cdot\tfrac29\\
&\qquad+\tfrac13\,b^2\cdot\tfrac89-\tfrac89\\
&\quad=\tfrac{4(9-6b+b^2)+8b^2-24}{27}\\
&\quad=\tfrac49(b-1)^2.
\end{aligned}
$$

**Diễn giải.** Mọi đường cơ sở hằng giữ nguyên kỳ vọng; phương sai nhỏ nhất tại $b=1$, không tại $v_\pi(s)=2$, và $b=3$ làm phương sai tăng lên $\tfrac{16}9$. Cộng hằng $c$ vào mọi phần thưởng và vào đường cơ sở cho cùng hiệu $r(A)-b$, nên một đường cơ sở dịch theo mức chung của phần thưởng, như $v_\pi(s)$, khử ảnh hưởng của phép cộng hằng. Ước lượng với $r=(4;\,1)$ và $b=0$ của Ví dụ 10.1 chính là ước lượng với $r=(3;\,0)$ và $b=-1$, có tổng phương sai $\tfrac49(-1-1)^2=\tfrac{16}9$.

**Kiểm tra lại.** Với $b=3$: $X_3=0$ khi $A=1$ và $X_3=(2;\,-2)$ khi $A=2$; mỗi tọa độ có mô men bậc hai $\tfrac13\cdot4=\tfrac43$, phương sai $\tfrac43-\tfrac49=\tfrac89$, tổng $\tfrac{16}9=\tfrac49(3-1)^2$.
:::

Ví dụ 10.3 trừ cùng một hằng ở mọi mẫu. Trong một lượt nhiều bước, mức so sánh thay đổi theo trạng thái, và có thể phụ thuộc mọi thông tin đã có trước khi chọn hành động. Định nghĩa sau gom cả hai trường hợp.

::: definition Định nghĩa 10.1 (Đường cơ sở và ước lượng có đường cơ sở)
Cho chính sách tham số hóa $\pi_\theta$ và một lượt $S_0,A_0,R_1,\dots,S_T$ sinh bởi $\pi_\theta$, với lịch sử $H_t$ và hàm điểm $\psi_t$ như ở Bài 09 ($\psi_t=0$ khi $t\ge T$).

Một *đường cơ sở* (baseline) là một hàm bị chặn $b:\mathcal S\to\mathbb R$. Ước lượng có đường cơ sở của gradient là
$$\widehat g_b=\sum_{t=0}^{T-1}\gamma^t\bigl(G_t-b(S_t)\bigr)\psi_t .$$

Một *đường cơ sở ngẫu nhiên* là một dãy biến ngẫu nhiên thực bị chặn $B_0,B_1,\dots$ sao cho, với mỗi $t<T$, khi biết $(H_t,B_t)$ hành động $A_t$ vẫn có phân phối $\pi_\theta(\cdot\mid S_t)$. Ước lượng tương ứng là $\widehat g_B=\sum_{t=0}^{T-1}\gamma^t(G_t-B_t)\psi_t$.
:::

Hệ số của $\psi_t$ trong $\widehat g_b$ là chênh lệch giữa lợi tức thực nhận và mức so sánh của trạng thái $S_t$. Với $b\equiv0$, $\widehat g_b$ là ước lượng REINFORCE của Thuật toán 09.25; khi $\gamma=1$, nó là cập nhật (13.11) của Sutton và Barto (2018, §13.4). Định nghĩa đường cơ sở ngẫu nhiên viết thành điều kiện toán học ý của Sutton và Barto (2018, tr. 329): "đường cơ sở có thể là một biến ngẫu nhiên, miễn là không thay đổi theo hành động". Ví dụ, $\hat v(S_t,w)$ với $w$ giữ cố định trong lượt, hoặc trung bình $G_0$ của các lượt khác, độc lập với lượt đang xét. Lợi tức $G_t$ của chính lượt không là đường cơ sở, vì nó phụ thuộc $A_t$.

Mệnh đề sau cho thấy phép trừ không đổi kỳ vọng, với cùng lập luận đã dùng cho phần thưởng quá khứ trong Bổ đề 09.22.

::: proposition Mệnh đề 10.2 (Đường cơ sở không làm chệch)
**Giả thiết.** (G1)–(G4) của Định lý 09.23; $b:\mathcal S\to\mathbb R$ thỏa $\lvert b(s)\rvert\le\bar b$ với mọi $s$.

**Kết luận.**
$$\begin{aligned}&\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^t\,b(S_t)\,\psi_t\Bigr]=0,\\&\text{do đó}\quad\mathbb E_{\pi_\theta}[\widehat g_b]=\nabla_\theta J(\theta).\end{aligned}$$

**Điều kiện áp dụng.** Lượt sinh bởi $\pi_\theta$, mọi hàm điểm tính tại cùng $\theta$, và $b$ giữ cố định trong suốt lượt. Kết luận giữ nguyên khi thay $b(S_t)$ bằng một đường cơ sở ngẫu nhiên $B_t$ của Định nghĩa 10.1.

**Phạm vi.** Mệnh đề nói về kỳ vọng, không nói về phương sai; một đường cơ sở có thể làm phương sai tăng, như $b=3$ trong Ví dụ 10.3.
:::

::: proof
**Bước 1 (tách ước lượng).** Theo Định nghĩa 10.1, $\widehat g_b=\widehat g-\sum_{t=0}^{T-1}\gamma^tb(S_t)\psi_t$, trong đó $\widehat g$ là ước lượng REINFORCE. Hệ quả 09.26, hệ quả của Định lý 09.23, cho $\mathbb E[\widehat g]=\nabla_\theta J(\theta)$, nên chỉ cần chứng minh tổng thứ hai có kỳ vọng $0$. Với quy ước $\psi_t=0$ khi $t\ge T$ và giả thiết $T\le T_{\max}$ của (G3), tổng theo $t$ từ $0$ đến $T-1$ bằng tổng theo $t$ từ $0$ đến $T_{\max}-1$, một tổng có số số hạng cố định.

**Bước 2 (kỳ vọng có điều kiện của một số hạng).** Cố định $t<T_{\max}$. Trên sự kiện $\{t\ge T\}$, xác định bởi $H_t$, số hạng bằng $0$. Trên $\{t<T\}$, khi biết $H_t$, trạng thái $S_t$ đã xác định và $A_t\sim\pi_\theta(\cdot\mid S_t)$, vì chính sách Markov và trạng thái Markov theo (G1). Do đó
$$
\begin{aligned}
&\mathbb E\bigl[b(S_t)\,\psi_t\mid H_t\bigr]\\
&=b(S_t)\,\mathbb E[\psi_t\mid H_t]\\
&=b(S_t)\sum_a\pi_\theta(a\mid S_t)\,\psi_\theta(S_t,a)\\
&=0.
\end{aligned}
$$
Đẳng thức thứ nhất dùng việc $b(S_t)$ là hàm của $H_t$; đẳng thức thứ hai dùng $A_t\sim\pi_\theta(\cdot\mid S_t)$; đẳng thức thứ ba là Mệnh đề 09.17, cần (G2).

**Bước 3 (lấy kỳ vọng và cộng theo $t$).** Theo (G4), $\psi_t$ khả tích (bị chặn với softmax, có mọi mô men với Gaussian), nên $\lvert b(S_t)\psi_t\rvert\le\bar b\lVert\psi_t\rVert$ khả tích. Tính chất tháp cho $\mathbb E[\gamma^tb(S_t)\psi_t]=\gamma^t\,\mathbb E\bigl[\mathbb E[b(S_t)\psi_t\mid H_t]\bigr]=0$. Cộng $T_{\max}$ số hạng được kỳ vọng của tổng bằng $0$, và cùng Bước 1 được $\mathbb E[\widehat g_b]=\nabla_\theta J(\theta)$.

Với đường cơ sở ngẫu nhiên $B_t$, Bước 2 điều kiện theo $(H_t,B_t)$ thay cho $H_t$: theo Định nghĩa 10.1, khi biết $(H_t,B_t)$ hành động $A_t$ vẫn có phân phối $\pi_\theta(\cdot\mid S_t)$, nên cùng chuỗi đẳng thức cho $\mathbb E[B_t\psi_t\mid H_t,B_t]=0$. $\square$
:::

Mệnh đề 10.2 nói rằng trừ khỏi mỗi lợi tức một mức chỉ phụ thuộc thông tin có trước khi chọn hành động không làm lệch hướng trung bình của bước cập nhật; phép trừ chỉ đổi cách các mẫu phân tán quanh kỳ vọng. Ba giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "đường cơ sở không phụ thuộc hành động": trên bài toán một bước, đặt $b(S_0,A_0)=r(A_0)$. Khi đó $G_0-b=0$ ở mọi lượt, nên $\widehat g_b\equiv0\ne(\tfrac23;\,-\tfrac23)$. Chọn $b=G_t$ của chính lượt cho cùng kết quả. Theo ghi chú thư mục của Sutton và Barto (2018, tr. 338), Thomas và Brunskill (2017) lập luận rằng đường cơ sở phụ thuộc hành động vẫn dùng được mà không gây chệch, theo một cách xây dựng khác với Định nghĩa 10.1.
- Bỏ "lượt sinh bởi $\pi_\theta$": nếu hành động của bài toán một bước được chọn đều, mỗi hành động với xác suất $\tfrac12$, thì $\mathbb E[b\,\psi_\theta(s,A)]=b\bigl(\tfrac12(\tfrac13;\,-\tfrac13)+\tfrac12(-\tfrac23;\,\tfrac23)\bigr)=b\,(-\tfrac16;\,\tfrac16)$, khác $0$ khi $b\ne0$.
- Bỏ "đường cơ sở bị chặn": nếu $B_0$ có phân phối Cauchy chuẩn, độc lập với $A_0$, thì $B_0\psi_0$ không khả tích và kỳ vọng trong kết luận không xác định.

Hai giả thiết đầu được dùng ở Bước 2, nơi phân phối có điều kiện của $A_t$ phải là $\pi_\theta(\cdot\mid S_t)$; giả thiết bị chặn được dùng ở Bước 3 để áp dụng tính chất tháp. Một nhầm lẫn thường gặp là đòi đường cơ sở độc lập với hành động. $b(S_t)$ và $A_t$ nói chung không độc lập, vì cả hai phụ thuộc $S_t$; điều chứng minh cần là $b$ không phụ thuộc $A_t$ khi đã biết lịch sử $H_t$.

Mệnh đề 10.2 mở rộng Định lý 09.23 mà không thêm giả thiết về môi trường; với $b\equiv0$ ta trở lại định lý đó. Bổ đề 09.22 dùng cùng lập luận cho phần thưởng quá khứ, và Mệnh đề 10.2 áp dụng lập luận ấy cho mọi đại lượng bị chặn xác định trước khi chọn $A_t$.

::: example Ví dụ 10.4 (Đường cơ sở trên lượt hành lang của Ví dụ 10.2)
**Dữ kiện.** Hành lang ngắn của Ví dụ 10.2: bốn ô $s_1,\dots,s_4$, phần thưởng $-1$ mỗi bước, $\gamma=1$, hai hành động bị đảo ở $s_2$; $p=\tfrac12$, $\psi_\theta(s,1)=(\tfrac12;\,-\tfrac12)$, $\psi_\theta(s,2)=(-\tfrac12;\,\tfrac12)$, $\nabla_\theta J=(2;\,-2)$. Lượt: hành động $1,1,1,2,1$, trạng thái $s_1,s_2,s_1,s_2,s_3$, lợi tức $G_t=-5,-4,-3,-2,-1$. Đường cơ sở là $b=v_\pi$ tại $p=\tfrac12$.

**Giá trị trạng thái.** Với $p=\tfrac12$, Mệnh đề 03.22 và 03.23 cho hệ
$$\begin{aligned}v(s_1)&=-1+\tfrac12v(s_2)+\tfrac12v(s_1),\\v(s_2)&=-1+\tfrac12v(s_1)+\tfrac12v(s_3),\\v(s_3)&=-1+\tfrac12v(s_2),\end{aligned}$$
trong đó số hạng thiếu ở phương trình thứ ba là đích, có giá trị $0$. Phương trình thứ nhất cho $v(s_1)=v(s_2)-2$, phương trình thứ ba cho $v(s_3)=\tfrac12v(s_2)-1$; thế vào phương trình thứ hai được $v(s_2)=-2{,}5+\tfrac34v(s_2)$, tức $v_\pi=(-12;\,-10;\,-6)$.

**Chênh lệch.** $G_t-v_\pi(S_t)$ lần lượt là $-5+12$, $-4+10$, $-3+12$, $-2+10$, $-1+6$, tức $7,6,9,8,5$.

**Ước lượng.** Tọa độ thứ nhất của $\widehat g_b$ là $\tfrac12(7+6+9+5)-\tfrac12\cdot8=13{,}5-4=9{,}5$, nên $\widehat g_b=(9{,}5;\,-9{,}5)$, cùng chiều $\nabla_\theta J=(2;\,-2)$.

**Diễn giải.** Lượt kết thúc sau $5$ bước, ít hơn mức trung bình $-J(\tfrac12)=12$ bước, nên mọi chênh lệch đều dương và mọi hành động đã chọn được tăng xác suất; bốn lần tăng cho hành động 1 thắng một lần tăng cho hành động 2. Kết quả thuộc về lượt này; một lượt dài hơn $12$ bước cho chênh lệch âm ở bước đầu.

**Kiểm tra lại.** $v_\pi(s_1)=-12=J(\tfrac12)$, đúng với $J(p)=-2(2-p)/\bigl(p(1-p)\bigr)$ của Ví dụ 10.2. Thay $v_\pi$ vào phương trình thứ hai: $-1+\tfrac12(-12)+\tfrac12(-6)=-10$.
:::

Hành lang không thỏa (G3), vì độ dài lượt không bị chặn, nên Mệnh đề 10.2 không áp dụng nguyên văn. Hai kết luận cần cho Ví dụ 10.2 và 10.4 vẫn đúng.

- $\mathbb E[\widehat g]=\nabla_\theta J=(2;\,-2)$: theo đoạn quy ước chiết khấu trước Bài tập 09.11 trong tệp bài tập của Bài 09, trên hành lang $T$ có đuôi hình học và mọi mô men hữu hạn, nên Hệ quả 09.26 vẫn đúng.
- Số hạng đường cơ sở có kỳ vọng $0$: với $\lvert b\rvert\le\bar b=12$ và $\lVert\psi\rVert\le c_\psi=\tfrac{\sqrt2}2$, ta có $\sum_{t<T}\lvert b(S_t)\rvert\,\lVert\psi_t\rVert\le\bar b\,c_\psi\,T$ với $\mathbb E[T]=12<\infty$. Định lý hội tụ trội cho phép đổi kỳ vọng với tổng vô hạn theo $t$, và Bước 2 của chứng minh Mệnh đề 10.2 cho mỗi số hạng kỳ vọng $0$.

Do đó $\mathbb E[\widehat g_b]=\mathbb E[\widehat g]=(2;\,-2)$ trên hành lang.

**Trong thực hành.** Đường cơ sở là đầu ra của một mạng $\hat v(s,w)$ học song song với chính sách. Để Mệnh đề 10.2 áp dụng, $w$ được giữ cố định trong khi tính các hệ số $G_t-\hat v(S_t,w)$ của một lượt, và hệ số đó được dừng gradient (Định nghĩa 08.12) khi lấy gradient theo $\theta$, để bước cập nhật chính sách không đi vào $w$. Giả thiết dữ liệu theo chính sách vẫn giữ nguyên như ở REINFORCE: lượt phải do chính $\pi_\theta$ sinh ra.

<!-- note-topic-id: lec-10-topic-04 -->
### 2.2 Đường cơ sở có phương sai nhỏ nhất

Ví dụ 10.3 cho thấy giá trị trạng thái $v_\pi(s)=2$ không làm phương sai nhỏ nhất, còn $b=1$ đưa phương sai về $0$.

**Câu hỏi.** Đường cơ sở hằng nào cho phương sai nhỏ nhất, và vì sao nó khác $v_\pi(s)$?

Về mặt ý tưởng, tổng phương sai là một hàm bậc hai của $b$ với hệ số bậc hai dương, nên có đúng một cực tiểu. Mệnh đề sau tìm cực tiểu này cho bài toán một bước.

::: proposition Mệnh đề 10.3 (Đường cơ sở hằng có phương sai nhỏ nhất, bài toán một bước)
**Giả thiết.** Một trạng thái $s$, lượt dừng sau một hành động $A\sim\pi_\theta(\cdot\mid s)$ trên tập hữu hạn $\mathcal A$; phần thưởng $R$ bị chặn và có phân phối có thể phụ thuộc $A$; hàm điểm $\psi=\psi_\theta(s,A)$ thỏa $\mathbb E\lVert\psi\rVert^2>0$. Với $b\in\mathbb R$, đặt $X_b=(R-b)\psi$ và $\operatorname{Var}(X_b)=\mathbb E\lVert X_b-\mathbb EX_b\rVert^2$.

**Kết luận.** $\operatorname{Var}(X_b)$ là hàm bậc hai lồi ngặt của $b$, đạt nhỏ nhất duy nhất tại
$$\begin{aligned}b^*&=\frac{\mathbb E\bigl[R\,\lVert\psi\rVert^2\bigr]}{\mathbb E\bigl[\lVert\psi\rVert^2\bigr]},\\\operatorname{Var}(X_b)&=\operatorname{Var}(X_{b^*})\\&\quad+\mathbb E\lVert\psi\rVert^2\,(b-b^*)^2 .\end{aligned}$$

**Điều kiện áp dụng.** $b$ là một hằng, không phụ thuộc $A$; hành động lấy mẫu từ $\pi_\theta$.

**Phạm vi.** Bài toán một bước và đường cơ sở hằng. Với lượt nhiều bước, phương sai của tổng có thêm hiệp phương sai giữa các bước, và mệnh đề không mô tả đường cơ sở tối ưu cho tổng đó.
:::

::: proof
**Bước 1 (kỳ vọng không phụ thuộc $b$).** $\mathbb E[X_b]=\mathbb E[R\psi]-b\,\mathbb E[\psi]=\mathbb E[R\psi]$, vì $\mathbb E[\psi]=0$ theo Mệnh đề 09.17. Đặt $g=\mathbb E[R\psi]$; véc-tơ này không phụ thuộc $b$.

**Bước 2 (khai triển theo $b$).** Khai triển $\lVert X_b-g\rVert^2=\lVert X_b\rVert^2-2g^\top X_b+\lVert g\rVert^2$ và lấy kỳ vọng được $\operatorname{Var}(X_b)=\mathbb E\lVert X_b\rVert^2-\lVert g\rVert^2$. Các kỳ vọng đều hữu hạn vì $R$ bị chặn và $\psi$ chỉ nhận hữu hạn giá trị. Do đó
$$
\begin{aligned}
&\operatorname{Var}(X_b)\\
&\quad=\mathbb E\bigl[(R-b)^2\lVert\psi\rVert^2\bigr]-\lVert g\rVert^2\\
&\quad=b^2\,\mathbb E\lVert\psi\rVert^2\\
&\qquad-2b\,\mathbb E\bigl[R\lVert\psi\rVert^2\bigr]\\
&\qquad+\mathbb E\bigl[R^2\lVert\psi\rVert^2\bigr]-\lVert g\rVert^2 .
\end{aligned}
$$

**Bước 3 ($b^*$ là cực tiểu duy nhất).** Đặt $k_2=\mathbb E\lVert\psi\rVert^2>0$ và $k_1=\mathbb E[R\lVert\psi\rVert^2]$. Phần phụ thuộc $b$ là $k_2b^2-2k_1b=k_2(b-k_1/k_2)^2-k_1^2/k_2$, một hàm bậc hai có hệ số dương. Hàm này đạt nhỏ nhất duy nhất tại $b^*=k_1/k_2$, và hiệu $\operatorname{Var}(X_b)-\operatorname{Var}(X_{b^*})$ bằng $k_2(b-b^*)^2$. $\square$
:::

Đọc bằng lời, $b^*$ là trung bình của phần thưởng với trọng số $\pi_\theta(a\mid s)\lVert\psi_\theta(s,a)\rVert^2$ cho hành động $a$, còn $v_\pi(s)=\mathbb E[R]$ là trung bình với trọng số $\pi_\theta(a\mid s)$; hai số trùng nhau khi mọi hành động có cùng $\lVert\psi_\theta(s,a)\rVert$. Trên Ví dụ 10.3, $\lVert\psi_\theta(s,1)\rVert^2=\tfrac29$ và $\lVert\psi_\theta(s,2)\rVert^2=\tfrac89$, nên
$$\begin{aligned}b^*&=\frac{\tfrac23\cdot3\cdot\tfrac29}{\tfrac23\cdot\tfrac29+\tfrac13\cdot\tfrac89}=\frac{4/9}{4/9}\\&=1\ne v_\pi(s)=2,\end{aligned}$$
và $k_2=\tfrac49$ khớp hệ số của công thức $\tfrac49(b-1)^2$. Hành động 2, hiếm hơn, có hàm điểm dài gấp đôi và phần thưởng $0$, nên kéo $b^*$ xuống dưới $v_\pi(s)$.

Hai giả thiết của Mệnh đề 10.3 có vai trò riêng.

- Bỏ "$\mathbb E\lVert\psi\rVert^2>0$": khi tập hành động chỉ có một phần tử, $\psi\equiv0$, mọi $b$ cho phương sai $0$ và công thức của $b^*$ có dạng $0/0$.
- Bỏ "$b$ không phụ thuộc $A$": $b=R$ cho $X_b\equiv0$, phương sai $0$ nhưng kỳ vọng $0\ne g$; phép cực tiểu hóa phương sai chỉ có nghĩa trên các đường cơ sở không làm chệch.

Giả thiết thứ hai được dùng ở Bước 1, nơi kỳ vọng không phụ thuộc $b$; giả thiết thứ nhất được dùng ở Bước 3, nơi hệ số của $b^2$ phải dương.

Greensmith, Bartlett và Baxter (2004, §5, Định lý 13, tr. 1489–1490, và Hệ quả 15, tr. 1491–1492) chứng minh một dạng tổng quát cho bài toán phần thưởng trung bình trên chuỗi Markov ergodic: đường cơ sở tối ưu theo trạng thái là trung bình của lợi tức với trọng số $\lVert\psi\rVert^2$. Thiết lập đó khác ước lượng theo lượt có chiết khấu của chương, nên chúng ta chỉ dùng kết luận định tính: đường cơ sở tối ưu nói chung khác $v_\pi$.

**Trong thực hành.** Sutton và Barto (2018, §13.4, tr. 329) gọi ước lượng $\hat v(S_t,w)$ của giá trị trạng thái là một lựa chọn tự nhiên cho đường cơ sở: $v_\pi$ học được bằng hồi quy lợi tức về trạng thái như ở Bài 05 và Bài 07, còn $b^*$ cần trọng số $\lVert\psi_\theta\rVert^2$, thay đổi theo $\theta$. Trên bài toán một bước, khoảng cách từ đường cơ sở tới $b^*$ chỉ làm tăng phương sai thêm $\mathbb E\lVert\psi\rVert^2(b-b^*)^2$ (Mệnh đề 10.3) và không làm chệch (Mệnh đề 10.2).

<!-- note-topic-id: lec-10-topic-05 -->
### 2.3 Hàm lợi thế

Với đường cơ sở $b=v_\pi$, hệ số của $\psi_t$ trong ước lượng là $G_t-v_\pi(S_t)$; trên lượt của Ví dụ 10.4, các hệ số này là $7,6,9,8,5$. Theo Bổ đề 03.20(d), khi biết lịch sử và $A_t=a$, lợi tức $G_t$ có kỳ vọng $q_\pi(S_t,a)$, nên hệ số có kỳ vọng có điều kiện $q_\pi(S_t,a)-v_\pi(S_t)$. Một cách trực quan, hiệu này đo hành động $a$ tốt hơn hay kém hơn bao nhiêu so với việc chọn hành động theo chính $\pi$ tại trạng thái đó. Đại lượng này có tên riêng.

::: definition Định nghĩa 10.4 (Hàm lợi thế)
Cho chính sách Markov dừng $\pi$ với giá trị trạng thái $v_\pi$ và giá trị hành động $q_\pi$. *Hàm lợi thế* (advantage function) của $\pi$ là
$$\begin{aligned}&A_\pi(s,a)=q_\pi(s,a)-v_\pi(s),\\&s\in\mathcal S,\ a\in\mathcal A,\end{aligned}$$
với quy ước $A_\pi=0$ tại trạng thái hấp thụ sau khi lượt kết thúc.
:::

$A_\pi(s,a)>0$ nghĩa là thực hiện $a$ tại $s$ rồi theo $\pi$ cho lợi tức kỳ vọng lớn hơn theo $\pi$ ngay từ $s$. Vì $v_\pi(s)$ không phụ thuộc $a$, $A_\pi(s,\cdot)$ và $q_\pi(s,\cdot)$ xếp các hành động theo cùng thứ tự, và điều kiện $q_\pi(s,\pi'(s))\ge v_\pi(s)$ của Định lý 04.13 chính là $A_\pi(s,\pi'(s))\ge0$. $A_\pi$ là đại lượng đúng của $\pi$; các đại lượng như $G_t-\hat v(S_t,w)$ là ước lượng của nó.

Mệnh đề sau dùng Mệnh đề 03.23 và Mệnh đề 10.2 để viết lại Hệ quả 09.24 với $A_\pi$ ở vị trí của $q_\pi$.

::: proposition Mệnh đề 10.5 (Tính chất của lợi thế, gradient dạng lợi thế)
**Giả thiết.**

- Cho (a): MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, chính sách Markov dừng $\pi$, như Mệnh đề 03.23.
- Cho (b): (G1)–(G4), chính sách Markov dừng $\pi=\pi_\theta$ và trạng thái hấp thụ sau khi lượt kết thúc, như Hệ quả 09.24.

**Kết luận.**

- (a) $\sum_a\pi(a\mid s)A_\pi(s,a)=0$ với mọi $s\in\mathcal S$.
- (b) Gradient của hàm mục tiêu có hai dạng
$$\begin{aligned}&\nabla_\theta J(\theta)\\&=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^t\\&\qquad\times A_\pi(S_t,A_t)\,\psi_t\Bigr]\\&=\frac1{1-\gamma}\\&\quad\times\mathbb E_{\substack{S\sim\nu^\pi\\A\sim\pi_\theta(\cdot\mid S)}}\bigl[A_\pi(S,A)\\&\qquad\times\psi_\theta(S,A)\bigr].\end{aligned}$$

**Điều kiện áp dụng.** $A_\pi$ và $\nu^\pi$ là của chính chính sách đang được lấy gradient, $\pi=\pi_\theta$.

**Phạm vi.** Đẳng thức (b) có hằng chính xác $1/(1-\gamma)$; mệnh đề không cho cách ước lượng $A_\pi$.
:::

::: proof
**Bước 1 (kết luận a).** Theo Mệnh đề 03.23, $\sum_a\pi(a\mid s)q_\pi(s,a)=v_\pi(s)$, nên $\sum_a\pi(a\mid s)A_\pi(s,a)=v_\pi(s)-v_\pi(s)\sum_a\pi(a\mid s)=0$.

**Bước 2 (dạng quỹ đạo).** Giá trị $v_\pi$ bị chặn bởi $T_{\max}R_{\max}$ theo (G3), nên Mệnh đề 10.2 áp dụng với $b=v_\pi$. Với quy ước $\psi_t=0$ khi $t\ge T$,
$$
\begin{aligned}
&\nabla_\theta J(\theta)\\
&=\sum_{t=0}^{T_{\max}-1}\gamma^t\,\mathbb E\bigl[(G_t-v_\pi(S_t))\psi_t\bigr]\\
&=\sum_{t=0}^{T_{\max}-1}\gamma^t\,\mathbb E\bigl[(\mathbb E[G_t\mid H_t,A_t]\\
&\qquad-v_\pi(S_t))\psi_t\bigr]\\
&=\sum_{t=0}^{T_{\max}-1}\gamma^t\,\mathbb E\bigl[(q_\pi(S_t,A_t)\\
&\qquad-v_\pi(S_t))\psi_t\bigr]\\
&=\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^tA_\pi(S_t,A_t)\psi_t\Bigr].
\end{aligned}
$$
Đẳng thức thứ nhất là Mệnh đề 10.2 với $b=v_\pi$. Đẳng thức thứ hai dùng tính chất tháp theo $(H_t,A_t)$ và đưa $v_\pi(S_t)$, $\psi_t$, đều là hàm của $(H_t,A_t)$, ra ngoài kỳ vọng có điều kiện. Đẳng thức thứ ba là Bổ đề 03.20(d), đẳng thức cuối là Định nghĩa 10.4.

**Bước 3 (dạng chiếm dụng).** Theo Hệ quả 09.24, $\nabla_\theta J=\frac1{1-\gamma}\mathbb E_{S\sim\nu^\pi,A\sim\pi_\theta}[q_\pi(S,A)\psi_\theta(S,A)]$. Với mỗi $s$, Mệnh đề 09.17 với $c=v_\pi(s)$ cho $\sum_a\pi_\theta(a\mid s)v_\pi(s)\psi_\theta(s,a)=0$; trừ đại lượng này trong kỳ vọng theo $A$ được dạng thứ hai của (b). $\square$
:::

Mệnh đề 10.5(b) nói rằng hướng tăng của $J$ là trung bình của các hàm điểm, mỗi hàm điểm nhân với lợi thế của hành động đã chọn; phép thay $q_\pi$ bằng $A_\pi$ không đổi kết quả vì phần bị trừ, $v_\pi(s)$, là hằng theo hành động. Bài giảng gốc (tr. 8) viết đẳng thức dưới dạng tỉ lệ; với $\nu^\pi$ chuẩn hóa, hằng tỉ lệ đúng bằng $1/(1-\gamma)$.

Hai điều kiện của mệnh đề có vai trò riêng.

- Bỏ "$A_\pi$ là của chính $\pi_\theta$": trên bài toán một bước, lợi thế của chính sách đều $\pi'=(\tfrac12;\,\tfrac12)$ là $A_{\pi'}=(3-1{,}5;\,0-1{,}5)=(1{,}5;\,-1{,}5)$, và $\sum_a\pi_\theta(a\mid s)A_{\pi'}(s,a)=\tfrac23\cdot1{,}5-\tfrac13\cdot1{,}5=0{,}5\ne0$: kết luận (a) không còn đúng.
- Bỏ "$\gamma<1$": thừa số $1/(1-\gamma)$ không xác định. Dạng quỹ đạo vẫn dùng được khi $T$ có đuôi hình học, như trên hành lang ngắn, nhờ hội tụ trội như ở đoạn sau Ví dụ 10.4; gom theo trạng thái cho trọng số là số lần thăm kỳ vọng $\eta(s)=\sum_t\Pr(S_t=s)$ không chuẩn hóa.

Bước 1 dùng Mệnh đề 03.23 cho chính $\pi$; Bước 2 dùng Bổ đề 03.20(d), cần chính sách Markov dừng, và Mệnh đề 10.2, cần (G1)–(G4).

::: example Ví dụ 10.5 (Lợi thế trên bài toán một bước)
**Dữ kiện.** Như Ví dụ 10.1: một trạng thái, $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$, $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$, lượt dừng sau một hành động.

**Lợi thế.** Lượt kết thúc sau hành động đầu tiên, nên $q_\pi(s,a)=r(a)$, tức $q_\pi=(3;\,0)$; $v_\pi(s)=2$; $A_\pi(s,\cdot)=(1;\,-2)$.

**Gradient.** Với $T=1$, chỉ có số hạng $t=0$ và $\gamma^0=1$:
$$\begin{aligned}&\tfrac23\cdot1\cdot(\tfrac13;\,-\tfrac13)\\&\quad+\tfrac13\cdot(-2)\cdot(-\tfrac23;\,\tfrac23)\\&\quad=(\tfrac29;\,-\tfrac29)+(\tfrac49;\,-\tfrac49)\\&\quad=(\tfrac23;\,-\tfrac23).\end{aligned}$$
Ở dạng chiếm dụng, $\nu^\pi(s)=1-\gamma$ vì trạng thái chỉ được thăm ở $t=0$, nên thừa số $1/(1-\gamma)$ bị khử và $\gamma$ không xuất hiện.

**Kiểm tra lại.** Kết luận (a): $\tfrac23\cdot1+\tfrac13\cdot(-2)=0$. Với $r=(4;\,1)$ của Ví dụ 10.1, $q_\pi=(4;\,1)$, $v_\pi(s)=3$ và $A_\pi$ vẫn là $(1;\,-2)$.
:::

Thay $v_\pi$ chưa biết bằng một hàm giá trị học được, ta có thuật toán sau, theo hộp giả mã của Sutton và Barto (2018, §13.4, tr. 330). Ví dụ 10.4 tính bằng tay phép cập nhật chính sách của thuật toán với đường cơ sở $v_\pi$ và $\gamma=1$, ngoài giả thiết $\gamma<1$ của thuật toán.

::: algorithm Thuật toán 10.6 (REINFORCE có đường cơ sở)
**Đầu vào.** Chính sách tham số hóa khả vi $\pi_\theta$; hàm giá trị tham số hóa khả vi $\hat v(s,w)$, $w\in\mathbb R^{d'}$; bước học $\alpha_\theta>0$, $\alpha_w>0$; $\gamma\in[0,1)$; số lượt $E$.

**Đầu ra.** Tham số $\theta$ và $w$ sau $E$ lượt.

**Giả thiết.** (G1)–(G4) cho chính sách; $\hat v(\cdot,w)$ bị chặn với mỗi $w$.

**Khởi tạo.** $\theta$ và $w$ tùy ý, chẳng hạn $w=0$.

**Với mỗi lượt $n=1,\dots,E$:**

1. $\theta_{\mathrm{old}}\leftarrow\theta$, $w_{\mathrm{old}}\leftarrow w$. Thu một lượt $S_0,A_0,R_1,\dots,S_T$ với $A_t\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid S_t)$.
2. $G_T=0$; với $t=T-1,\dots,0$: $G_t=R_{t+1}+\gamma G_{t+1}$.
3. Cập nhật hàm giá trị: $w\leftarrow w_{\mathrm{old}}+\alpha_w\sum_{t=0}^{T-1}\bigl(G_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\nabla_w\hat v(S_t,w_{\mathrm{old}})$.
4. Cập nhật chính sách: $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_{t=0}^{T-1}\gamma^t\bigl(G_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$.

**Điều kiện dừng.** Sau $E$ lượt.

**Chi phí mỗi bước.** Một lần tính $\hat v$ và gradient của nó theo $w$, một hàm điểm; bộ nhớ $O(T)$ để lưu lượt.
:::

Bước 3 hồi quy $\hat v$ về lợi tức Monte Carlo, không có trọng số $\gamma^t$; bước 4 có $\gamma^t$ như Thuật toán 09.25. Thuật toán giữ $w_{\mathrm{old}}$ cố định trong cả lượt, nên đường cơ sở là một hàm cố định của trạng thái như Mệnh đề 10.2 yêu cầu; hộp giả mã của Sutton và Barto cập nhật $w$ và $\theta$ ngay trong vòng lặp theo $t$, khác cách này ở các số hạng bậc hai theo bước học.

**Trong thực hành.** Bước 3 là một bước hạ gradient của mất mát bình phương $\tfrac12\sum_t\bigl(G_t-\hat v(S_t,w)\bigr)^2$ tại $w_{\mathrm{old}}$, với $\hat v$ là một mạng hoặc một bộ xấp xỉ tuyến tính. Thuật toán vẫn cần lượt kết thúc trước khi cập nhật và dùng mỗi lượt một lần, như REINFORCE.

Với $\hat v$ tùy ý, Mệnh đề 10.2 bảo đảm Thuật toán 10.6 không chệch cho gradient, nhưng hệ số $G_t-\hat v(S_t,w)$ bị chệch như một ước lượng của lợi thế: theo Bổ đề 03.20(d),
$$\begin{aligned}&\mathbb E\bigl[G_t-\hat v(S_t,w)\mid H_t,A_t\bigr]\\&\quad=A_\pi(S_t,A_t)+v_\pi(S_t)-\hat v(S_t,w).\end{aligned}$$
Trên bài toán một bước với $\hat v(s)=1$, kỳ vọng của hệ số khi chọn hành động 1 là $3-1=2$, trong khi $A_\pi(s,1)=1$. Phần chệch $v_\pi(S_t)-\hat v(S_t,w)$ giống nhau cho mọi hành động tại cùng trạng thái, nên bị khử khi nhân với hàm điểm và lấy kỳ vọng theo hành động.

<!-- note-topic-id: lec-10-topic-06 -->
### 2.4 Critic và actor–critic một bước

Thuật toán 10.6 chỉ cập nhật khi lượt đã kết thúc, vì $G_t$ cần mọi phần thưởng sau bước $t$. Hàm $\hat v$ của nó đánh giá trạng thái đầu $S_t$ của bước chuyển, trước khi hành động được chọn, nên đặt mức so sánh nhưng không đánh giá hành động $A_t$ (Sutton và Barto, 2018, §13.5, tr. 331). Về mặt ý tưởng, nếu áp $\hat v$ cả cho trạng thái thứ hai $S_{t+1}$, thì $R_{t+1}+\gamma\hat v(S_{t+1},w)$ ước lượng lợi tức sau một bước, và so nó với $\hat v(S_t,w)$ cho biết hành động vừa thực hiện tốt hơn hay kém hơn mức mong đợi. Để làm rõ ý này, chúng ta dùng chuỗi hai trạng thái sau.

::: example Ví dụ 10.6 (Chuỗi hai trạng thái)
**Dữ kiện.** Hai trạng thái chưa kết thúc $s_A$ (xuất phát, $\mu_0(s_A)=1$) và $s_B$; hai hành động; $\gamma=0{,}9$.

- Tại $s_A$: hành động 1 chuyển sang $s_B$ với phần thưởng $0$; hành động 2 kết thúc lượt với phần thưởng $1$.
- Tại $s_B$: hành động 1 kết thúc với phần thưởng $3$; hành động 2 kết thúc với phần thưởng $0$.

Chính sách có một tham số cho mỗi trạng thái, $\theta=(\theta_A;\,\theta_B)$, và $p_s=\pi_\theta(1\mid s)=\sigma(\theta_s)$ với $\sigma(x)=1/(1+e^{-x})$; đây là chính sách softmax (Định nghĩa 09.11) với logit $\theta_s$ cho hành động 1 và $0$ cho hành động 2. Theo Mệnh đề 09.16, $\psi_\theta(s,1)=(1-p_s)e_s$ và $\psi_\theta(s,2)=-p_se_s$, với $e_A=(1;\,0)$, $e_B=(0;\,1)$. Chính sách đang xét: $\theta=(0;\,\log2)$, tức $p_A=\tfrac12$, $p_B=\tfrac23$.

**Giá trị.** Theo Mệnh đề 03.22 và 03.23: $v_\pi(s_B)=\tfrac23\cdot3=2$; $q_\pi(s_A,1)=0+0{,}9\cdot2=1{,}8$; $q_\pi(s_A,2)=1$; $v_\pi(s_A)=\tfrac12\cdot1{,}8+\tfrac12\cdot1=1{,}4=J$.

**Lợi thế.** $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$ và $A_\pi(s_B,\cdot)=(3-2;\,0-2)=(1;\,-2)$.

**Gradient tính trực tiếp.** $J=p_A\cdot0{,}9\cdot3p_B+(1-p_A)\cdot1$ và $\mathrm dp_s/\mathrm d\theta_s=p_s(1-p_s)$, nên
$$\begin{aligned}\frac{\partial J}{\partial\theta_A}&=p_A(1-p_A)(2{,}7p_B-1)\\&=0{,}25\cdot0{,}8=0{,}2,\\\frac{\partial J}{\partial\theta_B}&=p_A\cdot2{,}7\cdot p_B(1-p_B)\\&=0{,}5\cdot2{,}7\cdot\tfrac29=0{,}3.\end{aligned}$$

**Gradient theo Mệnh đề 10.5(b).** Bước $t=0$ ở $s_A$ đóng góp $\tfrac12\cdot0{,}4\cdot0{,}5\,e_A+\tfrac12(-0{,}4)(-0{,}5)\,e_A=0{,}2\,e_A$. Bước $t=1$ ở $s_B$, xảy ra với xác suất $p_A=\tfrac12$ và trọng số $\gamma=0{,}9$, đóng góp $0{,}9\cdot\tfrac12\bigl(\tfrac23\cdot1\cdot\tfrac13+\tfrac13(-2)(-\tfrac23)\bigr)e_B=0{,}45\cdot\tfrac23\,e_B=0{,}3\,e_B$. Tổng là $(0{,}2;\,0{,}3)$, khớp cách tính trực tiếp.

**Kiểm tra lại.** Kết luận (a) của Mệnh đề 10.5: $\tfrac12\cdot0{,}4+\tfrac12(-0{,}4)=0$ và $\tfrac23\cdot1+\tfrac13(-2)=0$. Ở dạng chiếm dụng, $\nu^\pi(s_A)=0{,}1$, $\nu^\pi(s_B)=0{,}1\cdot0{,}9\cdot\tfrac12=0{,}045$, và $\tfrac1{0{,}1}(0{,}1\cdot0{,}2;\,0{,}045\cdot\tfrac23)=(0{,}2;\,0{,}3)$.
:::

![Chuỗi hai trạng thái. Ô s A, ghi xuất phát và p A bằng xác suất chọn hành động 1, có hai cung: hành động 1 sang ô s B với phần thưởng 0; hành động 2 tới ô kết thúc tô xám với phần thưởng 1. Ô s B, ghi p B, có hai cung tới ô kết thúc: hành động 1 với phần thưởng 3, hành động 2 với phần thưởng 0. Góc dưới ghi gamma bằng 0,9 và chính sách cũ p A bằng 1/2, p B bằng 2/3.](img/lec-10/two-state-chain.svg)

Trên hình, chỉ cung "hành động 1 tại $s_A$" dẫn tới trạng thái thứ hai, nên mọi lượt dài $1$ hoặc $2$ bước, và lợi thế tại $s_A$ phụ thuộc $s_B$ qua $q_\pi(s_A,1)=\gamma v_\pi(s_B)$.

Trên chuỗi này, với một hàm giá trị $\hat v=(1;\,1{,}5)$, bước chuyển $s_A\to s_B$ bằng hành động 1 có thể được đánh giá ngay sau một bước: phần thưởng $0$ cộng giá trị chiết khấu của $s_B$ là $0+0{,}9\cdot1{,}5=1{,}35$, lớn hơn $\hat v(s_A)=1$, nên hành động 1 tốt hơn mức mong đợi. Thuật toán 10.6 phải chờ lượt kết thúc để có $G_0$. Định nghĩa sau gọi tên hai thành phần của cách đánh giá này.

::: definition Định nghĩa 10.7 (Critic, actor, phương pháp actor–critic)
Cho chính sách tham số hóa $\pi_\theta$, hàm giá trị tham số hóa $\hat v(s,w)$ với $w\in\mathbb R^{d'}$, và một bước chuyển $(S_t,A_t,R_{t+1},S_{t+1},Z_{t+1})$ sinh bởi $\pi_\theta$.

Hàm $\hat v(\cdot,w)$ gọi là *critic* khi nó đánh giá hành động $A_t$ qua mục tiêu bootstrap
$$R_{t+1}+\gamma\,(1-Z_{t+1})\,\hat v(S_{t+1},w),$$
tức qua giá trị ước lượng của trạng thái thứ hai $S_{t+1}$ của bước chuyển.

Chính sách $\pi_\theta$ gọi là *actor*.

*Phương pháp actor–critic* (actor–critic method) cập nhật $\theta$ theo một hệ số lập từ mục tiêu bootstrap của critic, và cập nhật $w$ để $\hat v(\cdot,w)$ xấp xỉ giá trị của chính sách hiện tại.
:::

Mục tiêu bootstrap trong định nghĩa là lợi tức một bước, với $\hat v(S_{t+1},w)$ thay cho phần lợi tức sau bước $t+1$, và mặt nạ $(1-Z_{t+1})$ bằng $0$ khi $S_{t+1}$ là trạng thái kết thúc. Theo Sutton và Barto (2018, §13.5, tr. 331), phép bootstrap này phân biệt critic với đường cơ sở. Hàm $\hat v$ của Thuật toán 10.6 chỉ đánh giá trạng thái $S_t$, trước khi hành động được chọn, nên REINFORCE có đường cơ sở không là phương pháp actor–critic, dù có một chính sách và một hàm giá trị học được. Bài giảng gốc (tr. 12) dùng tên actor–critic theo nghĩa rộng hơn, cho mọi phương pháp có hai thành phần đó; ghi chú thư mục của Sutton và Barto (2018, tr. 338) ghi rằng phương pháp actor–critic đôi khi được gọi là advantage actor–critic (A2C).

Để so mục tiêu bootstrap với giá trị của trạng thái đầu, ta lập sai số TD với critic $\hat v(\cdot,w)$ và mặt nạ kết thúc của Bài 08:
$$\begin{aligned}\delta_t&=R_{t+1}+\gamma\,(1-Z_{t+1})\,\hat v(S_{t+1},w)\\&\quad-\hat v(S_t,w).\end{aligned}$$
Mục tiêu một bước $R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)$ là mục tiêu TD(0) của Định nghĩa 07.19; mặt nạ $(1-Z_{t+1})$ thay cho quy ước "$\hat v=0$ tại trạng thái kết thúc" của Sutton và Barto. Mệnh đề sau cho biết $\delta_t$ ước lượng gì.

::: proposition Mệnh đề 10.8 (Sai số TD và lợi thế)
**Giả thiết.** MDP hữu hạn có tính Markov, phần thưởng bị chặn, $0\le\gamma<1$; chính sách Markov dừng $\pi$; critic $\hat v(\cdot,w)$ là một hàm cố định của trạng thái; $Z_{t+1}=1$ khi và chỉ khi $S_{t+1}$ là trạng thái kết thúc. Đặt $e(s)=\hat v(s,w)-v_\pi(s)$ với $s\in\mathcal S$.

**Kết luận.** Với mọi $t$, mọi $s\in\mathcal S$ và $a\in\mathcal A$ sao cho $\Pr(S_t=s,A_t=a)>0$:

- (a) nếu $\hat v(\cdot,w)=v_\pi$ trên $\mathcal S$ thì $\mathbb E[\delta_t\mid S_t=s,A_t=a]=A_\pi(s,a)$;
- (b) tổng quát,
  $$\begin{aligned}&\mathbb E[\delta_t\mid S_t=s,A_t=a]\\&=A_\pi(s,a)\\&\quad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,e(s')\\&\quad-e(s).\end{aligned}$$

**Điều kiện áp dụng.** $w$ không phụ thuộc chuyển $(R_{t+1},S_{t+1})$ của bước đang xét; cờ $Z$ chỉ ghi kết thúc của MDP, không ghi cắt ngắn.

**Phạm vi.** Mệnh đề nói về kỳ vọng có điều kiện của một bước; nó không nói về phương sai của $\delta_t$ và không cho biết critic học được có tiến tới $v_\pi$ hay không.
:::

::: proof
**Bước 1 (kỳ vọng của mục tiêu một bước).** Khi biết $S_t=s$, $A_t=a$, cặp $(R_{t+1},S_{t+1})$ có phân phối của động lực tại $(s,a)$, không phụ thuộc phần lịch sử trước đó (Bổ đề 03.20(a) với một bước). Mặt nạ bằng $0$ đúng khi $S_{t+1}$ là trạng thái kết thúc, nên
$$\begin{aligned}&\mathbb E\bigl[R_{t+1}\\&\quad+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)\\&\quad\bigm| S_t=s,A_t=a\bigr]\\&=r(s,a)\\&\quad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,\hat v(s',w).\end{aligned}$$

**Bước 2 (tách critic thành giá trị đúng và sai số).** Thay $\hat v=v_\pi+e$ trên $\mathcal S$:
$$
\begin{aligned}
&r(s,a)\\
&\quad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,\hat v(s',w)\\
&\quad=r(s,a)\\
&\qquad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,v_\pi(s')\\
&\qquad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,e(s')\\
&\quad=q_\pi(s,a)\\
&\qquad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,e(s').
\end{aligned}
$$
Đẳng thức thứ hai dùng Mệnh đề 03.22; tổng trong mệnh đề đó chạy cả trên trạng thái kết thúc, nơi $v_\pi=0$, nên bằng tổng trên $\mathcal S$.

**Bước 3 (trừ giá trị của trạng thái hiện tại).** Khi biết $S_t=s$, số hạng $\hat v(s,w)=v_\pi(s)+e(s)$ là hằng. Trừ nó khỏi kết quả của Bước 2 và dùng Định nghĩa 10.4 được (b); (a) là trường hợp $e\equiv0$. $\square$
:::

Mệnh đề 10.8(a) nói rằng với critic đúng, sai số TD của một bước là ước lượng không chệch của lợi thế của hành động vừa thực hiện. Trên Ví dụ 10.6 với critic đúng $\hat v=(1{,}4;\,2)$, mọi chuyển là tất định: chọn hành động 1 tại $s_A$ cho $\delta_0=0+0{,}9\cdot2-1{,}4=0{,}4=A_\pi(s_A,1)$, chọn hành động 2 cho $\delta_0=1-1{,}4=-0{,}4$, và chọn hành động 1 tại $s_B$ cho $\delta_1=3-2=1=A_\pi(s_B,1)$. Một nhầm lẫn thường gặp là điều kiện theo trạng thái thay vì theo cặp trạng thái–hành động: với critic đúng, $\mathbb E[\delta_t\mid S_t=s]=\sum_a\pi(a\mid s)A_\pi(s,a)=0$ (Mệnh đề 05.27, Mệnh đề 10.5(a)), nên $\delta_t$ chỉ đánh giá hành động khi đặt cạnh hành động đã chọn.

Hai giả thiết của mệnh đề có vai trò riêng.

- Bỏ "critic đúng": trên bài toán một bước với $\hat v(s)=1$ trong khi $v_\pi(s)=2$, ta có $\delta_0=R_1-1$, nên $\mathbb E[\delta_0\mid A_0=1]=2\ne A_\pi(s,1)=1$ và $\mathbb E[\delta_0\mid A_0=2]=-1\ne-2$. Theo (b), độ chệch là $-e(s)=1$ cho cả hai hành động; trong lượt nhiều bước, số hạng $\gamma\sum_{s'}P(s'\mid s,a)e(s')$ làm độ chệch khác nhau giữa các hành động.
- Bỏ "mặt nạ chỉ tắt ở trạng thái kết thúc": nếu bỏ mặt nạ và trạng thái kết thúc của Ví dụ 10.6 được gán giá trị $\hat v=1$, thì với critic đúng trên $\mathcal S$, hành động 2 tại $s_A$ cho $\delta_0=1+0{,}9-1{,}4=0{,}5$, trong khi $A_\pi(s_A,2)=-0{,}4$.

Bước 1 dùng tính Markov và mặt nạ, Bước 2 dùng Mệnh đề 03.22, còn điều kiện critic đúng chỉ dùng ở (a). Sutton và Barto (2018, §13.5, tr. 331) nêu rằng độ chệch này không do bootstrap gây ra: critic học bằng Monte Carlo nhưng chưa hội tụ cũng cho actor bị chệch, đúng như số hạng $e$ trong (b). Ví dụ sau thực hiện hai bước actor–critic với một critic chưa đúng.

::: example Ví dụ 10.7 (Hai bước actor–critic bằng tay)
**Dữ kiện.** Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_s=\sigma(\theta_s)$, $\psi_\theta(s,1)=(1-p_s)e_s$; ban đầu $\theta=(0;\,\log2)$, $p_A=\tfrac12$, $p_B=\tfrac23$. Critic dạng bảng $\hat v(s,w)=w_s$ với $w=(w_A;\,w_B)=(1;\,1{,}5)$, nên $\nabla_w\hat v(s,w)=e_s$. Bước học $\alpha_w=0{,}5$, $\alpha_\theta=1$. Ở mỗi bước $t$, critic tính $\delta_t$ và cập nhật $w$; actor dùng cùng $\delta_t$, nhân với thừa số $I=\gamma^t$, đóng vai trọng số $\gamma^t$ của Định lý 09.23. Lượt: $S_0=s_A$, $A_0=1$, $R_1=0$, $S_1=s_B$, $Z_1=0$; $A_1=1$, $R_2=3$, kết thúc, $Z_2=1$.

**Bước $t=0$, $I=1$.** Critic:

- mục tiêu $R_1+\gamma(1-Z_1)w_B=0+0{,}9\cdot1{,}5=1{,}35$;
- sai lệch $\delta_0=1{,}35-w_A=0{,}35$;
- giá trị mới $w_A=1+0{,}5\cdot0{,}35=1{,}175$.

Actor:

- hướng $I\,\delta_0\,\psi_\theta(s_A,1)=1\cdot0{,}35\cdot0{,}5\,e_A=0{,}175\,e_A$;
- tham số mới $\theta_A=0+1\cdot0{,}175=0{,}175$;
- xác suất mới $p_A=\sigma(0{,}175)=0{,}5436$.

**Bước $t=1$, $I=\gamma=0{,}9$.** Critic:

- mục tiêu $R_2+\gamma(1-Z_2)\hat v(S_2,w)=3+0=3$, vì mặt nạ bằng $0$;
- sai lệch $\delta_1=3-w_B=1{,}5$;
- giá trị mới $w_B=1{,}5+0{,}5\cdot1{,}5=2{,}25$.

Actor:

- hướng $I\,\delta_1\,\psi_\theta(s_B,1)=0{,}9\cdot1{,}5\cdot\tfrac13\,e_B=0{,}45\,e_B$;
- tham số mới $\theta_B=\log2+0{,}45=1{,}1431$;
- xác suất mới $p_B=\sigma(1{,}1431)=0{,}7583$.

**Diễn giải.** Cả hai sai số TD đều dương: mỗi hành động cho kết quả tốt hơn critic dự đoán, nên xác suất chọn lại nó tăng. Sai số $\delta_0=0{,}35$ khác lợi thế $A_\pi(s_A,1)=0{,}4$ vì critic chưa đúng, như Mệnh đề 10.8(b) mô tả.

**Kiểm tra lại.** $\sigma(0{,}175)=1/(1+e^{-0{,}175})=1/(1+0{,}8395)=0{,}5436$ và $\sigma(1{,}1431)=1/(1+0{,}3188)=0{,}7583$. Hai xác suất của các hành động đã chọn đều tăng, đúng dấu của $\delta_0$, $\delta_1$.
:::

![Sơ đồ một bước chuyển: S t, hành động A t, phần thưởng R t+1, trạng thái S t+1 và cờ Z t+1. Khung critic v mũ của s, w tính v mũ tại S t và tại S t+1. Nút sai số TD: delta t bằng R t+1 cộng gamma nhân (1 trừ Z t+1) nhân v mũ của S t+1, trừ v mũ của S t; phần mục tiêu R t+1 cộng gamma (1 trừ Z t+1) v mũ của S t+1 nằm trong khung nét đứt ghi dừng gradient. Từ delta t có hai mũi tên: tới critic, ghi w cộng alpha w nhân delta t nhân gradient theo w của v mũ tại S t; tới actor pi theta, ghi theta cộng alpha theta nhân I nhân delta t nhân psi theta tại S t, A t.](img/lec-10/actor-critic-advantage.svg)

Trên hình, critic cho hai giá trị, tại $S_t$ và tại $S_{t+1}$, để lập $\delta_t$; khung nét đứt đánh dấu mục tiêu được dừng gradient, như cập nhật bán gradient của Định nghĩa 07.21. Cùng một số $\delta_t$ làm sai lệch cho critic và làm hệ số của hàm điểm cho actor, ở vị trí của $G_t-\hat v(S_t,w)$ trong Thuật toán 10.6.

::: algorithm Thuật toán 10.9 (Actor–critic một bước)
**Đầu vào.** Chính sách tham số hóa khả vi $\pi_\theta$; critic khả vi $\hat v(s,w)$; bước học $\alpha_\theta>0$, $\alpha_w>0$; $\gamma\in[0,1)$; số lượt $E$.

**Đầu ra.** Tham số $\theta$ và $w$ sau $E$ lượt.

**Giả thiết.** Môi trường trả cờ kết thúc $Z$ sau mỗi bước; hành động được chọn bằng chính sách hiện tại.

**Khởi tạo.** $\theta$ và $w$ tùy ý, chẳng hạn $w=0$.

**Với mỗi lượt:** quan sát trạng thái đầu $S$, đặt $I\leftarrow1$, rồi lặp các bước sau cho tới khi lượt kết thúc.

1. Chọn $A\sim\pi_\theta(\cdot\mid S)$; thực hiện $A$, quan sát $R$, $S'$, $Z$.
2. $\delta\leftarrow R+\gamma(1-Z)\hat v(S',w)-\hat v(S,w)$.
3. Critic: $w\leftarrow w+\alpha_w\,\delta\,\nabla_w\hat v(S,w)$.
4. Actor: $\theta\leftarrow\theta+\alpha_\theta\,I\,\delta\,\psi_\theta(S,A)$.
5. $I\leftarrow\gamma I$; $S\leftarrow S'$.

**Điều kiện dừng.** Sau $E$ lượt.

**Chi phí mỗi bước.** Hai lần tính $\hat v$, một gradient của $\hat v$ theo $w$ và một hàm điểm; bộ nhớ không phụ thuộc độ dài lượt.
:::

Thuật toán 10.9 thay $G_t$ của Thuật toán 10.6 bằng lợi tức một bước, theo (13.12)–(13.14) của Sutton và Barto (2018, §13.5); thừa số $I=\gamma^t$ đóng vai trọng số $\gamma^t$ của Định lý 09.23, critic là TD(0) bán gradient (Thuật toán 07.22), và thuật toán cập nhật ngay sau từng bước mà không lưu lượt. Ví dụ 10.7 là hai vòng lặp của nó.

::: remark Nhận xét 10.10 (Đường cơ sở và critic; nhầm lẫn thường gặp)
1. Một nhầm lẫn thường gặp là coi mọi phương pháp có hàm giá trị học được là actor–critic theo Định nghĩa 10.7. Ước lượng của Thuật toán 10.6 không chệch với mọi $\hat v$ cố định (Mệnh đề 10.2), còn ước lượng của actor–critic thì không (ý 3 dưới đây).
2. Trong cập nhật actor, $\delta_t$ là một hệ số đã dừng gradient: gradient của actor không đi vào $w$. Trong cập nhật critic, mục tiêu được coi là hằng.
3. Mệnh đề 10.2 không áp dụng cho $\delta_t$: phần $-\hat v(S_t,w)$ là một đường cơ sở hợp lệ, nhưng $R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)$ thay cho $G_t$ có kỳ vọng có điều kiện $q_\pi(S_t,A_t)+\gamma\,\mathbb E[(1-Z_{t+1})\,e(S_{t+1})\mid S_t,A_t]$, nên ước lượng gradient bị chệch khi critic sai.
:::

**Trong thực hành.** Critic là một mạng $\hat v(s,w)$, và hai cập nhật của Thuật toán 10.9 được cài đặt bằng hai hàm mất mát: $-I\operatorname{sg}(\delta_t)\log\pi_\theta(A_t\mid S_t)$ cho actor và $\tfrac12\bigl(\operatorname{sg}(R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w))-\hat v(S_t,w)\bigr)^2$ cho critic. Khi lượt bị cắt ngắn ($U_{t+1}=1$, $Z_{t+1}=0$), mục tiêu vẫn bootstrap từ quan sát cuối của lượt (Định nghĩa 08.6). Với xấp xỉ hàm, critic không bằng $v_\pi$, nên theo Mệnh đề 10.8(b) actor nhận một hệ số chệch ở mọi bước; mỗi bước chuyển chỉ dùng một lần vì dữ liệu phải theo chính sách hiện tại.

Như vậy, chúng ta có hai cách ước lượng lợi thế cho actor, dựa trên gradient dạng lợi thế của Mệnh đề 10.5. Hệ số $G_t-\hat v(S_t,w)$ của Thuật toán 10.6 cho ước lượng gradient không chệch với mọi hàm giá trị cố định (Mệnh đề 10.2), với phương sai phụ thuộc đường cơ sở (Mệnh đề 10.3), nhưng chứa mọi phần thưởng đến cuối lượt. Sai số TD $\delta_t$ của phương pháp actor–critic (Định nghĩa 10.7, Thuật toán 10.9) chỉ chứa một phần thưởng và có kỳ vọng có điều kiện bằng lợi thế khi critic đúng (Mệnh đề 10.8), nhưng bị chệch khi critic sai. Sutton và Barto (2018, §13.5, tr. 331) nêu rằng lợi tức một bước thường có phương sai nhỏ hơn lợi tức thực, đổi lại có độ chệch, và mức chệch điều chỉnh được bằng lợi tức $n$ bước. Trong Mục 3, chúng ta nối hai đầu này bằng một tham số $\lambda$.

*Nguồn: bài giảng gốc lecture10_policy_gradient_part2.pdf (2025–2026), trang 3–14; Sutton và Barto (2018), §13.3–13.5; Greensmith, Bartlett và Baxter (2004), §5; Thomas và Brunskill (2017).*

---

## 3. Ước lượng lợi thế tổng quát

Trên chuỗi hai trạng thái với critic chưa đúng $\hat v=(1;\,1{,}5)$, lượt $s_A\xrightarrow{1}s_B\xrightarrow{1}$ kết thúc cho sai số TD $\delta_0=0{,}35$ và hệ số Monte Carlo $G_0-\hat v(s_A)=0+0{,}9\cdot3-1=1{,}7$, trong khi lợi thế đúng là $A_\pi(s_A,1)=0{,}4$. Ta lần lượt xét lợi tức $n$ bước, lợi tức λ cùng điều kiện để ước lượng không làm chệch gradient, và cách tính trên đoạn thu.

<!-- note-topic-id: lec-10-topic-07 -->
### 3.1 Lợi tức n bước

Sutton và Barto (2018, §7.1, tr. 142) mở chương về phương pháp $n$ bước bằng câu hỏi về các phương pháp nằm giữa TD một bước và Monte Carlo: dùng vài phần thưởng thực nhận rồi thay phần còn lại của lợi tức bằng giá trị ước lượng của trạng thái đạt tới. Về mặt ý tưởng, dùng càng nhiều phần thưởng thực thì càng ít phụ thuộc critic, nhưng càng chịu nhiều ngẫu nhiên của lượt. Ví dụ sau đặt ba lựa chọn cạnh nhau trên cùng một lượt.

::: example Ví dụ 10.8 (Ba ước lượng lợi thế trên một lượt của chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_A=\tfrac12$, $p_B=\tfrac23$; lợi thế đúng $A_\pi(s_A,1)=0{,}4$. Critic cố định $\hat v=(1;\,1{,}5)$. Lượt: $S_0=s_A$, $A_0=1$, $R_1=0$, $S_1=s_B$, $A_1=1$, $R_2=3$, kết thúc tại $T=2$.

**Sai số TD.** $\delta_0=0+0{,}9\cdot1{,}5-1=0{,}35$ và $\delta_1=3-1{,}5=1{,}5$, vì mặt nạ tắt ở bước cuối.

**Ba ước lượng của $A_\pi(s_A,1)$.**

- Một bước: $R_1+\gamma\hat v(S_1)-\hat v(S_0)=\delta_0=0{,}35$.
- Hai bước, ở đây trùng Monte Carlo vì $T=2$: $R_1+\gamma R_2-\hat v(S_0)=0+0{,}9\cdot3-1=1{,}7$.
- Trộn hai ước lượng trên với trọng số $1-\lambda$ và $\lambda$, $\lambda=0{,}8$: $0{,}2\cdot0{,}35+0{,}8\cdot1{,}7=1{,}43$.

**Diễn giải.** Ba số khác nhau trên cùng một lượt, và không số nào bằng $0{,}4$. So sánh trên một lượt không cho biết kỳ vọng của từng ước lượng.

**Kiểm tra lại.** $1{,}7=0{,}35+0{,}9\cdot1{,}5=\delta_0+\gamma\delta_1$ và $1{,}43=\delta_0+0{,}72\,\delta_1$, với $0{,}72=\gamma\lambda$.
:::

Hai đẳng thức ở dòng kiểm tra lại có chung một lý do: mọi ước lượng ở đây là tổng có trọng số của các sai số TD. Định nghĩa và bổ đề sau phát biểu điều này cho mọi $n$.

::: definition Định nghĩa 10.11 (Lợi tức $n$ bước, lợi thế $n$ bước)
Cho một lượt kết thúc tại $T$, một critic $\hat v(\cdot,w)$ với $w$ cố định, và $n\in\mathbb N_+$. *Lợi tức $n$ bước* (n-step return) từ bước $t<T$ là
$$\begin{aligned}&G_{t:t+n}=\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}\\&\quad+\gamma^n\hat v(S_{t+n},w)\\&\qquad\text{nếu }t+n<T,\\&G_{t:t+n}=G_t\quad\text{nếu }t+n\ge T.\end{aligned}$$
*Lợi thế $n$ bước* là $\widehat A^{(n)}_t=G_{t:t+n}-\hat v(S_t,w)$.
:::

Lợi tức $n$ bước dùng $n$ phần thưởng thực rồi bootstrap từ giá trị ước lượng của trạng thái đạt tới sau $n$ bước. Khi lượt kết thúc trước bước $t+n$, không còn gì để bootstrap và lợi tức $n$ bước là lợi tức thực; quy ước này nằm ngay trong định nghĩa, như (7.1) và (12.1) của Sutton và Barto (2018, tr. 143, 289). Trường hợp $n=1$ là mục tiêu TD(0) của Định nghĩa 05.20 và 07.19; trường hợp $n\ge T-t$ là lợi tức Monte Carlo. Lợi thế $n$ bước dùng $\hat v(S_t,w)$ làm đường cơ sở, như Thuật toán 10.6.

Bổ đề sau, theo cùng quy ước $\delta_k=0$ khi $k\ge T$, viết lợi thế $n$ bước thành tổng của $n$ sai số TD đầu tiên.

::: lemma Bổ đề 10.12 (Lợi thế $n$ bước bằng tổng sai số TD)
**Giả thiết.** Lượt kết thúc tại $T$; critic $\hat v(\cdot,w)$ với $w$ giữ cố định trong cả lượt; $\delta_k=R_{k+1}+\gamma(1-Z_{k+1})\hat v(S_{k+1},w)-\hat v(S_k,w)$ với $k<T$, và $\delta_k=0$ với $k\ge T$.

**Kết luận.** Với mọi $t<T$ và mọi $n\ge1$,
$$\widehat A^{(n)}_t=\sum_{k=0}^{n-1}\gamma^k\,\delta_{t+k}.$$

**Điều kiện áp dụng.** Mọi sai số TD dùng cùng một tham số $w$; $Z_{k+1}=1$ khi và chỉ khi $k+1=T$.

**Phạm vi.** Đẳng thức là đồng nhất thức trên từng lượt, không phải phát biểu về kỳ vọng.
:::

::: proof
**Bước 1 (cắt tổng).** Đặt $\bar n=\min(n,T-t)\ge1$. Các số hạng có $k\ge\bar n$ thỏa $t+k\ge T$ nên bằng $0$; do đó $\sum_{k=0}^{n-1}\gamma^k\delta_{t+k}=\sum_{k=0}^{\bar n-1}\gamma^k\delta_{t+k}$. Với $k\le\bar n-2$, bước $t+k+1<T$ nên $Z_{t+k+1}=0$.

**Bước 2 (tổng lồng nhau).** Thay định nghĩa của $\delta_{t+k}$ và tách ba tổng:
$$
\begin{aligned}
&\sum_{k=0}^{\bar n-1}\gamma^k\delta_{t+k}\\
&=\sum_{k=0}^{\bar n-1}\gamma^kR_{t+k+1}\\
&\quad+\sum_{k=0}^{\bar n-1}\gamma^{k+1}(1-Z_{t+k+1})\\
&\qquad\times\hat v(S_{t+k+1})\\
&\quad-\sum_{k=0}^{\bar n-1}\gamma^k\hat v(S_{t+k})\\
&=\sum_{k=0}^{\bar n-1}\gamma^kR_{t+k+1}\\
&\quad+\sum_{j=1}^{\bar n}\gamma^{j}(1-Z_{t+j})\hat v(S_{t+j})\\
&\quad-\sum_{j=0}^{\bar n-1}\gamma^j\hat v(S_{t+j})\\
&=\sum_{k=0}^{\bar n-1}\gamma^kR_{t+k+1}\\
&\quad+\gamma^{\bar n}(1-Z_{t+\bar n})\hat v(S_{t+\bar n})\\
&\quad-\hat v(S_t).
\end{aligned}
$$
Đẳng thức thứ hai đổi chỉ số $j=k+1$ ở tổng giữa; đẳng thức thứ ba dùng $Z_{t+j}=0$ với $1\le j\le \bar n-1$ (Bước 1), nên các số hạng $j=1,\dots,\bar n-1$ của hai tổng sau triệt tiêu.

**Bước 3 (hai trường hợp).** Nếu $t+n<T$ thì $\bar n=n$, $Z_{t+n}=0$, và vế phải là $\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}+\gamma^n\hat v(S_{t+n})-\hat v(S_t)=G_{t:t+n}-\hat v(S_t)$. Nếu $t+n\ge T$ thì $\bar n=T-t$, $Z_T=1$, và vế phải là $\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}-\hat v(S_t)=G_t-\hat v(S_t)$, bằng $G_{t:t+n}-\hat v(S_t)$ theo Định nghĩa 10.11. $\square$
:::

Bổ đề 10.12 tổng quát hóa Bài tập 05.14, trường hợp $n\ge T-t$, và là Bài tập 7.1 của Sutton và Barto (2018, tr. 143); Schulman và cộng sự (2016, (11)–(14)) viết cùng tổng lồng nhau với $r_t$ thay cho $R_{t+1}$. Giả thiết critic cố định là chỗ dùng duy nhất ở Bước 2: nếu $\hat v(S_{t+1})$ trong $\delta_t$ và trong $\delta_{t+1}$ được tính với hai tham số khác nhau, hai số hạng không triệt tiêu và tổng sai lệch khỏi $\widehat A^{(n)}_t$ đúng bằng $\gamma$ nhân hiệu hai giá trị đó. Giả thiết mặt nạ được dùng ở Bước 3: nếu trạng thái kết thúc được gán $\hat v(S_T)\ne0$ mà không có mặt nạ, tổng có thêm $\gamma^{T-t}\hat v(S_T)$.

<!-- note-topic-id: lec-10-topic-08 -->
### 3.2 Lợi tức λ và ước lượng lợi thế tổng quát

Ví dụ 10.8 trộn hai lợi tức với trọng số $1-\lambda$ và $\lambda$. Sutton và Barto (2018, §12.1, tr. 288) nhận xét rằng mọi trung bình lồi của các lợi tức $n$ bước đều là một mục tiêu hợp lệ, và chọn một họ trung bình riêng: lợi tức $n$ bước nhận trọng số tỉ lệ với $\lambda^{n-1}$, chuẩn hóa bằng $1-\lambda$ để tổng các trọng số bằng $1$. Về mặt ý tưởng, trung bình này dùng phần thưởng thứ $k$ sau bước $t$, tức $R_{t+k}$, với trọng số $\lambda^{k-1}$ so với lợi tức Monte Carlo, và thay phần còn lại bằng giá trị ước lượng của critic; $\lambda$ nhỏ dựa nhiều vào critic, $\lambda$ gần $1$ dựa nhiều vào phần thưởng thực nhận.

::: definition Định nghĩa 10.13 (Lợi tức λ và ước lượng lợi thế tổng quát)
Cho lượt, critic và lợi tức $n$ bước như Định nghĩa 10.11, và $\lambda\in[0,1)$. *Lợi tức λ* (λ-return) từ bước $t<T$ là
$$\begin{aligned}&G^\lambda_t\\&\quad=(1-\lambda)\sum_{n=1}^{\infty}\lambda^{n-1}G_{t:t+n}\\&\quad=(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}\\&\qquad+\lambda^{T-t-1}G_t,\end{aligned}$$
và với $\lambda=1$ đặt $G^1_t=G_t$, tức dạng thứ hai với $\lambda=1$. *Ước lượng lợi thế tổng quát* (generalized advantage estimation, GAE) với tham số $(\gamma,\lambda)$ là
$$\widehat A_t=G^\lambda_t-\hat v(S_t,w).$$
:::

Hai dạng của $G^\lambda_t$ bằng nhau vì mọi $n\ge T-t$ cho cùng lợi tức $G_t$, và tổng trọng số của chúng là $(1-\lambda)\sum_{n\ge T-t}\lambda^{n-1}=\lambda^{T-t-1}$; dạng thứ hai là (12.3) của Sutton và Barto (2018, tr. 290). Trọng số $(1-\lambda)\lambda^{n-1}$ giảm theo cấp số nhân và cộng lại bằng $1$, nên $G^\lambda_t$ là một trung bình của các lợi tức $n$ bước. Với $\lambda=0$, chỉ lợi tức một bước có trọng số khác $0$ và $\widehat A_t=\delta_t$; với $\lambda=1$, $\widehat A_t=G_t-\hat v(S_t,w)$ là hệ số Monte Carlo của Thuật toán 10.6. Như vậy GAE chứa cả hai đầu của Mục 2. Trong Ví dụ 10.8, $T-t-1=1$ tại $t=0$, nên $G^\lambda_0=0{,}2\,G_{0:1}+0{,}8\,G_0=0{,}2\cdot1{,}35+0{,}8\cdot2{,}7=2{,}43$ và $\widehat A_0=1{,}43$.

![Hai biểu đồ cột cạnh nhau. Trái: trọng số (1 trừ lambda) nhân lambda mũ n trừ 1 của lợi tức n bước, với lambda bằng 0,8 và n từ 1 đến 6: 0,2; 0,16; 0,128; 0,102; 0,082; 0,066; một cột cuối tô sọc, lambda mũ 6 bằng 0,262, ghi phần trọng số còn lại dồn vào lợi tức thực khi lượt kết thúc. Phải: trọng số (gamma lambda) mũ k của sai số TD delta t cộng k trong GAE, với gamma bằng 0,9 và lambda bằng 0,8, k từ 0 đến 5: 1; 0,72; 0,518; 0,373; 0,269; 0,193.](img/lec-10/gae-weights.svg)

Nửa trái của hình là trọng số của từng lợi tức $n$ bước trong $G^\lambda_t$, tương tự Hình 12.2 của Sutton và Barto (2018) với số của chương; cột sọc là phần $\lambda^{T-t-1}$ dồn vào lợi tức thực, ở đây với $T-t-1=6$. Nửa phải là trọng số $(\gamma\lambda)^k$ của sai số TD thứ $k$ trong dạng tổng của mệnh đề sau. Hai nửa mô tả cùng một ước lượng theo hai cách đếm.

::: proposition Mệnh đề 10.14 (Dạng tổng, hai đầu mút và truy hồi của GAE)
**Giả thiết.** Lượt kết thúc tại $T$; critic cố định trong cả lượt; $\delta_k$ như Bổ đề 10.12, $\delta_k=0$ với $k\ge T$; $\lambda\in[0,1]$.

**Kết luận.**

- (a) $\widehat A_t=\sum_{k=0}^{T-t-1}(\gamma\lambda)^k\,\delta_{t+k}$ với mọi $t<T$.
- (b) Với $\lambda=0$, $\widehat A_t=\delta_t$; với $\lambda=1$, $\widehat A_t=G_t-\hat v(S_t,w)$.
- (c) Đặt $\widehat A_T=0$; khi đó $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$ với $t=T-1,\dots,0$.

**Điều kiện áp dụng.** Cùng một $w$ cho mọi sai số TD của lượt.

**Phạm vi.** Đồng nhất thức trên từng lượt; mệnh đề không nói gì về kỳ vọng hay phương sai.
:::

::: proof
**Bước 1 (thay lợi thế $n$ bước, $\lambda<1$).** Vì $(1-\lambda)\sum_{n\ge1}\lambda^{n-1}=1$, ta có $\widehat A_t=(1-\lambda)\sum_{n\ge1}\lambda^{n-1}\bigl(G_{t:t+n}-\hat v(S_t)\bigr)=(1-\lambda)\sum_{n\ge1}\lambda^{n-1}\widehat A^{(n)}_t$. Bổ đề 10.12 thay mỗi $\widehat A^{(n)}_t$ bằng $\sum_{k=0}^{n-1}\gamma^k\delta_{t+k}$.

**Bước 2 (đổi thứ tự lấy tổng).** Chỉ hữu hạn sai số TD khác $0$ (các $k<T-t$), và $\sum_n\lambda^{n-1}$ hội tụ tuyệt đối, nên được đổi thứ tự:
$$
\begin{aligned}
&\widehat A_t\\
&=(1-\lambda)\sum_{n=1}^{\infty}\lambda^{n-1}\sum_{k=0}^{n-1}\gamma^k\delta_{t+k}\\
&=\sum_{k=0}^{T-t-1}\gamma^k\delta_{t+k}\\
&\quad\times(1-\lambda)\sum_{n=k+1}^{\infty}\lambda^{n-1}\\
&=\sum_{k=0}^{T-t-1}(\gamma\lambda)^k\,\delta_{t+k},
\end{aligned}
$$
trong đó đẳng thức cuối dùng $(1-\lambda)\sum_{n\ge k+1}\lambda^{n-1}=\lambda^k$. Đây là (a) khi $\lambda<1$.

**Bước 3 (hai đầu mút).** Với $\lambda=0$, (a) chỉ còn số hạng $k=0$, tức $\delta_t$. Với $\lambda=1$, Định nghĩa 10.13 cho $\widehat A_t=G_t-\hat v(S_t)$, và Bổ đề 10.12 với $n=T-t$ cho $G_t-\hat v(S_t)=\sum_{k=0}^{T-t-1}\gamma^k\delta_{t+k}$, chính là (a) với $\lambda=1$. Trường hợp này phải xử lý riêng vì thừa số $1-\lambda$ ở Bước 1 bằng $0$.

**Bước 4 (truy hồi).** Tách số hạng $k=0$ của (a): $\widehat A_t=\delta_t+\gamma\lambda\sum_{k=1}^{T-t-1}(\gamma\lambda)^{k-1}\delta_{t+k}=\delta_t+\gamma\lambda\,\widehat A_{t+1}$, với tổng của $\widehat A_{T}$ rỗng nên $\widehat A_T=0$. Khi $Z_{t+1}=1$ thì $t+1=T$ và $\widehat A_{t+1}=0$, nên nhân thêm $(1-Z_{t+1})$ không đổi kết quả. $\square$
:::

Dạng tổng (a) là (16) của Schulman và cộng sự (2016) và lời giải Bài tập 12.3 của Sutton và Barto (2018, tr. 295); truy hồi (c) cho phép tính mọi $\widehat A_t$ của một lượt bằng một lượt quét lùi. Trên Ví dụ 10.8, truy hồi của lợi tức λ, $G^\lambda_t=R_{t+1}+\gamma\bigl[(1-\lambda)\hat v(S_{t+1})+\lambda G^\lambda_{t+1}\bigr]$ (Sutton và Barto, 2018, Bài tập 12.1), cho $G^\lambda_1=3$ và $G^\lambda_0=0+0{,}9(0{,}2\cdot1{,}5+0{,}8\cdot3)=2{,}43$, khớp $\widehat A_0=0{,}35+0{,}72\cdot1{,}5=1{,}43$ của (a).

Còn lại câu hỏi của Mục 2: GAE có làm chệch ước lượng gradient không. Schulman và cộng sự (2016, Định nghĩa 1) gọi một ước lượng lợi thế là *γ-just* nếu thay lợi thế đúng bằng nó trong công thức gradient không đổi kỳ vọng. Mệnh đề sau cho hai điều kiện đủ.

::: proposition Mệnh đề 10.15 (GAE và gradient: tính không chệch theo nghĩa γ-just)
**Giả thiết.** MDP hữu hạn; (G1)–(G4); chính sách Markov dừng $\pi=\pi_\theta$ và trạng thái hấp thụ sau khi lượt kết thúc; critic $\hat v$ là một hàm bị chặn, cố định, của trạng thái; $\widehat A_t$ là GAE tính trên cả lượt tới khi kết thúc.

**Kết luận.** Với mỗi $t$, nếu (a) $\lambda=1$, hoặc (b) $\hat v=v_\pi$ trên $\mathcal S$ và $\lambda\in[0,1]$ tùy ý, thì
$$\begin{aligned}&\mathbb E\bigl[\widehat A_t\,\psi_t\bigr]\\&\quad=\mathbb E\bigl[A_\pi(S_t,A_t)\,\psi_t\bigr],\\&\text{do đó}\\&\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^t\widehat A_t\,\psi_t\Bigr]=\nabla_\theta J(\theta).\end{aligned}$$

**Điều kiện áp dụng.** Lượt kết thúc trong dữ liệu, không bị cắt giữa chừng; các hàm điểm tính tại tham số đã sinh lượt.

**Phạm vi.** Mệnh đề nói về gradient: nó không khẳng định $\mathbb E[\widehat A_t\mid S_t,A_t]=A_\pi(S_t,A_t)$. Với $\lambda<1$ và $\hat v\ne v_\pi$, mệnh đề không cho bảo đảm nào.
:::

::: proof
**Bước 1 (trường hợp a).** Với $\lambda=1$, $\widehat A_t=G_t-\hat v(S_t)$ theo Mệnh đề 10.14(b). Tính chất tháp theo $(H_t,A_t)$ và Bổ đề 03.20(d) cho $\mathbb E[G_t\psi_t]=\mathbb E[q_\pi(S_t,A_t)\psi_t]$. Bước 2–3 của chứng minh Mệnh đề 10.2, áp dụng với đường cơ sở $\hat v$ rồi với $v_\pi$, cho $\mathbb E[\hat v(S_t)\psi_t]=0=\mathbb E[v_\pi(S_t)\psi_t]$. Trừ hai đẳng thức được $\mathbb E[\widehat A_t\psi_t]=\mathbb E[(q_\pi-v_\pi)(S_t,A_t)\psi_t]=\mathbb E[A_\pi(S_t,A_t)\psi_t]$.

**Bước 2 (trường hợp b, tách theo $k$).** Với $\hat v=v_\pi$, Mệnh đề 10.14(a) cho $\widehat A_t=\sum_{k\ge0}(\gamma\lambda)^k\delta_{t+k}$, một tổng có không quá $T_{\max}$ số hạng khác $0$ theo (G3). Ta tính $\mathbb E[\delta_{t+k}\psi_t]$ cho từng $k$.

**Bước 3 (các số hạng $k\ge1$ bằng $0$).** Cố định $k\ge1$. Hàm điểm $\psi_t$ là hàm của $(H_t,A_t)$, nằm trong lịch sử $H_{t+k}$; sự kiện $\{t+k<T\}$ cũng xác định bởi $H_{t+k}$. Theo tính Markov, kỳ vọng của $\delta_{t+k}$ khi biết $(H_{t+k},A_{t+k})$ chỉ phụ thuộc $(S_{t+k},A_{t+k})$, nên Mệnh đề 10.8(a) áp dụng:
$$
\begin{aligned}
&\mathbb E[\delta_{t+k}\psi_t]\\
&=\mathbb E\bigl[\psi_t\\
&\quad\times\mathbb E[\delta_{t+k}\mid H_{t+k},A_{t+k}]\bigr]\\
&=\mathbb E\bigl[\psi_t\,\mathbb 1\{t+k<T\}\\
&\quad\times A_\pi(S_{t+k},A_{t+k})\bigr]\\
&=\mathbb E\bigl[\psi_t\,\mathbb 1\{t+k<T\}\\
&\quad\times\mathbb E[A_\pi(S_{t+k},A_{t+k})\mid H_{t+k}]\bigr]\\
&=0.
\end{aligned}
$$
Đẳng thức thứ nhất dùng tính chất tháp, vì $\psi_t$ là hàm của $H_{t+k}$; đẳng thức thứ hai là Mệnh đề 10.8(a); đẳng thức thứ ba dùng tính chất tháp theo $H_{t+k}$. Đẳng thức cuối dùng Mệnh đề 10.5(a): $\mathbb E[A_\pi(S_{t+k},A_{t+k})\mid H_{t+k}]=\sum_a\pi(a\mid S_{t+k})A_\pi(S_{t+k},a)=0$.

**Bước 4 (số hạng $k=0$).** Cùng lập luận với $k=0$ dừng ở đẳng thức thứ hai: $\mathbb E[\delta_t\psi_t]=\mathbb E[\psi_tA_\pi(S_t,A_t)]$, vì $\psi_t$ là hàm của $(H_t,A_t)$ và $\psi_t=0$ khi $t\ge T$. Cộng Bước 3 và Bước 4 được kết luận cho trường hợp (b).

**Bước 5 (cộng theo $t$).** Các đại lượng bị chặn hoặc khả tích theo (G3)–(G4), nên nhân với $\gamma^t$ và cộng theo $t<T_{\max}$ được $\mathbb E\bigl[\sum_t\gamma^t\widehat A_t\psi_t\bigr]=\mathbb E\bigl[\sum_t\gamma^tA_\pi(S_t,A_t)\psi_t\bigr]=\nabla_\theta J(\theta)$ theo Mệnh đề 10.5(b). $\square$
:::

Đọc bằng lời, GAE không làm chệch gradient khi nó là hệ số Monte Carlo trừ một đường cơ sở ($\lambda=1$), hoặc khi mọi sai số TD đều có kỳ vọng có điều kiện bằng lợi thế ($\hat v=v_\pi$). Đây là Mệnh đề 1 của Schulman và cộng sự (2016, chứng minh ở Phụ lục B), ứng với $Q_t=G_t$ khi $\lambda=1$ và với $Q_t=\widehat A_t+v_\pi(S_t)$ khi $\hat v=v_\pi$. Hai điều kiện có vai trò riêng.

- Bỏ cả hai điều kiện: với $\lambda=0{,}8$ và $\hat v=(1;\,1{,}5)$ trên chuỗi hai trạng thái, tọa độ $\theta_A$ của $\mathbb E[\widehat A_0\psi_0]$ là $0{,}1775$, khác giá trị đúng $0{,}2$ (Ví dụ 10.9 dưới đây).
- Bỏ "lượt kết thúc trong dữ liệu": nếu lượt của chuỗi bị cắt sau bước $0$ và bootstrap bằng $\hat v(s_B)=1{,}5$, thì kể cả với $\lambda=1$, $\widehat A_0=\delta_0$, và tọa độ $\theta_A$ của kỳ vọng là $0{,}0875\ne0{,}2$.

Bước 1 dùng $\lambda=1$ cùng lượt đầy đủ, để $\widehat A_t$ là $G_t$ trừ một đường cơ sở; Bước 3–4 dùng $\hat v=v_\pi$ qua Mệnh đề 10.8(a). Một nhầm lẫn thường gặp là đọc mệnh đề thành "GAE với $\lambda=1$ là ước lượng không chệch của lợi thế". Ví dụ sau cho thấy điều đó sai.

::: example Ví dụ 10.9 (Kỳ vọng và gradient của GAE trên chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái như Ví dụ 10.8: $\gamma=0{,}9$, $p_A=\tfrac12$, $p_B=\tfrac23$, critic cố định $\hat v=(1;\,1{,}5)$; lợi thế đúng $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$; hàm điểm tại $s_A$: $\psi_\theta(s_A,1)=0{,}5\,e_A$, $\psi_\theta(s_A,2)=-0{,}5\,e_A$; tọa độ $\theta_A$ của gradient đúng tại bước $0$ là $0{,}2$ (Ví dụ 10.6). Tại $s_B$, phần thưởng kỳ vọng là $\tfrac23\cdot3=2$.

**Hành động 1 tại $s_A$.** $\delta_0=0{,}35$ là tất định; $\delta_1=R_2-1{,}5$ có kỳ vọng $0{,}5$. Theo Mệnh đề 10.14(a), $\mathbb E[\widehat A_0\mid s_A,1]=0{,}35+0{,}9\lambda\cdot0{,}5=0{,}35+0{,}45\lambda$, tức $0{,}35$; $0{,}71$; $0{,}8$ với $\lambda=0$; $0{,}8$; $1$, so với $A_\pi(s_A,1)=0{,}4$.

**Hành động 2 tại $s_A$.** Lượt kết thúc với phần thưởng $1$, nên $\widehat A_0=\delta_0=1-1=0$ với mọi $\lambda$, so với $A_\pi(s_A,2)=-0{,}4$.

**Gradient.** Tọa độ $\theta_A$ của $\mathbb E[\widehat A_0\psi_0]$ là $\tfrac12\cdot\mathbb E[\widehat A_0\mid s_A,1]\cdot0{,}5+\tfrac12\cdot0\cdot(-0{,}5)$, tức $0{,}0875$; $0{,}1775$; $0{,}2$ với $\lambda=0$; $0{,}8$; $1$.

**Diễn giải.** Với $\lambda=1$, độ chệch của $\widehat A_0$ là $+0{,}4$ cho cả hai hành động, nên bị khử khi nhân với hàm điểm có kỳ vọng $0$, và gradient đúng dù lợi thế sai. Với $\lambda<1$, độ chệch khác nhau giữa hai hành động, chẳng hạn $-0{,}05$ và $+0{,}4$ khi $\lambda=0$, nên không bị khử.

**Kiểm tra lại.** Giá trị đúng: $0{,}5\cdot0{,}4\cdot0{,}5+0{,}5\cdot(-0{,}4)(-0{,}5)=0{,}2$.
:::

**Trong thực hành.** Critic học được không bằng $v_\pi$, và các cài đặt dùng $\lambda<1$, nên Mệnh đề 10.15 không bảo đảm ước lượng gradient bằng GAE là γ-just. Schulman và cộng sự (2016, §3) nêu định tính một đánh đổi giữa độ chệch và phương sai theo $\lambda$: GAE với $\lambda=1$ γ-just bất kể critic nhưng có phương sai cao vì là tổng của nhiều số hạng, còn GAE với $\lambda=0$ chệch khi critic sai nhưng thường có phương sai thấp hơn nhiều; $\lambda\in(0,1)$ cân bằng hai đầu. Bài giảng gốc (tr. 13) nêu cùng đánh đổi này. Schulman và cộng sự (2016, §3) cũng ghi rằng, về thực nghiệm, giá trị $\lambda$ tốt thường nhỏ hơn hẳn giá trị $\gamma$ tốt.

<!-- note-topic-id: lec-10-topic-09 -->
### 3.3 GAE trên đoạn thu

Mệnh đề 10.14 giả sử có cả lượt. Dữ liệu của PPO gồm các *đoạn thu* (rollout) độ dài $h$ trên $N$ môi trường chạy song song: trong một đoạn, một lượt có thể kết thúc, bị cắt ngắn vì giới hạn thời gian, hoặc còn dở ở biên đoạn. Bài giảng gốc (tr. 24) viết GAE như một tổng vô hạn, không có cờ. Về mặt ý tưởng, bước cuối của mỗi lượt trong đoạn thuộc một trong hai loại: kết thúc thật, khi phần tương lai bằng $0$; cắt ngắn hoặc dừng ở biên đoạn, khi phần tương lai còn nhưng không được thu, nên được thay bằng giá trị ước lượng của critic. Ví dụ sau cho thấy cờ nào được dùng ở đâu quyết định kết quả.

::: example Ví dụ 10.10 (Kết thúc và cắt ngắn)
**Dữ kiện.** Đoạn hai bước của một môi trường, $\gamma=0{,}9$, $\lambda=0{,}8$; $R_1=1$, $R_2=2$; critic cũ cho $\hat v(S_0)=2$, $\hat v(S_1)=3$; $Z_1=U_1=0$. Hai trường hợp sau bước $2$: (i) $S_2$ là trạng thái kết thúc, $Z_2=1$; (ii) lượt bị cắt ở bước $2$ vì giới hạn thời gian, $U_2=1$, $Z_2=0$, và critic cho quan sát cuối $S_2$ giá trị $\hat v(S_2)=4$.

**Bước $t=0$.** $\delta_0=1+0{,}9\cdot3-2=1{,}7$ trong cả hai trường hợp.

**Trường hợp (i).** Mặt nạ tắt: $\delta_1=2-3=-1$, $\widehat A_1=-1$, và $\widehat A_0=1{,}7+0{,}72\cdot(-1)=0{,}98$.

**Trường hợp (ii).** Mặt nạ không tắt: $\delta_1=2+0{,}9\cdot4-3=2{,}6$, $\widehat A_1=2{,}6$, và $\widehat A_0=1{,}7+0{,}72\cdot2{,}6=3{,}572$.

**Diễn giải.** Cùng phần thưởng, cùng critic, hai cờ cho hai kết quả cách nhau $2{,}592$. Ở (ii), trạng thái $S_2$ vẫn có tương lai, nên giá trị của nó đi vào sai số TD.

**Kiểm tra lại.** Ở (ii), $\widehat A_0+\hat v(S_0)=5{,}572$ phải bằng *lợi tức λ cắt* (truncated λ-return) tại bước $2$ của Sutton và Barto (2018, (12.9)): $G_{0:1}=1+0{,}9\cdot3=3{,}7$, $G_{0:2}=1+0{,}9\cdot2+0{,}81\cdot4=6{,}04$, và $0{,}2\cdot3{,}7+0{,}8\cdot6{,}04=5{,}572$.
:::

![Quan sát O t, qua hành động A t và phần thưởng R t+1, tới quan sát O t+1. Nhánh trên, khung viền liền: Z t+1 bằng 1, MDP kết thúc, mục tiêu y t bằng R t+1. Nhánh dưới, khung viền nét đứt: U t+1 bằng 1 và Z t+1 bằng 0, hết giới hạn bước, mục tiêu y t bằng R t+1 cộng gamma nhân max của Q theta trừ tại O t+1.](img/lec-08/termination-truncation.svg)

Hình của Bài 08 tách hai nhánh của một bước cuối. Nhánh viền liền ứng với trường hợp (i): mục tiêu chỉ còn phần thưởng. Nhánh nét đứt ứng với trường hợp (ii): mục tiêu giữ phần bootstrap; ở đây phần bootstrap là $\gamma\hat v(S_2)$ thay cho phép cực đại của DQN. Thuật toán sau ghi các quy tắc này cho một đoạn thu tổng quát.

::: algorithm Thuật toán 10.16 (Tính GAE lùi trên đoạn thu)
**Đầu vào.** Với mỗi môi trường và mỗi $t=0,\dots,h-1$: $R_{t+1}$, $Z_{t+1}$, $U_{t+1}$ và $V_t=\hat v(S_t,w_{\mathrm{old}})$. Với mỗi $t$ có $U_{t+1}=1$: giá trị $V'_{t+1}=\hat v(S^{\mathrm{cuối}}_{t+1},w_{\mathrm{old}})$ của quan sát cuối của lượt bị cắt, trước khi môi trường tự đặt lại. Giá trị $V_h=\hat v(S_h,w_{\mathrm{old}})$ tại biên đoạn. Tham số $\gamma$, $\lambda$.

**Đầu ra.** $\widehat A_t$ và mục tiêu của critic $V^{\mathrm{targ}}_t$, $t=0,\dots,h-1$.

**Giả thiết.** $w_{\mathrm{old}}$ giữ cố định trong cả phép tính; $Z$ chỉ ghi kết thúc của MDP.

**Các bước** (cho từng môi trường):

1. Nếu $Z_h=0$ và $U_h=0$, coi bước cuối như cắt ngắn: đặt $U_h\leftarrow1$ và $V'_h\leftarrow V_h$.
2. Với $t=0,\dots,h-1$: giá trị kế là $V^{\mathrm{next}}_{t+1}=V'_{t+1}$ nếu $U_{t+1}=1$, ngược lại $V^{\mathrm{next}}_{t+1}=V_{t+1}$; sai số TD là $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})V^{\mathrm{next}}_{t+1}-V_t$.
3. Đặt $\widehat A_h=0$; với $t=h-1,\dots,0$: $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})(1-U_{t+1})\widehat A_{t+1}$.
4. $V^{\mathrm{targ}}_t=\widehat A_t+V_t$.

**Điều kiện dừng.** Sau khi quét hết đoạn.

**Chi phí.** $O(hN)$ phép tính và bộ nhớ, cộng $N$ lần tính critic tại biên đoạn và một lần cho mỗi bước bị cắt.
:::

Bước 2 dùng mặt nạ $(1-Z_{t+1})$ cho sai số TD, như Bài 08: chỉ kết thúc thật mới bỏ phần bootstrap. Bước 3 dùng thêm $(1-U_{t+1})$ cho truy hồi, vì sau một bước cắt ngắn hoặc ở biên đoạn, bước kế trong bộ đệm thuộc lượt khác hoặc chưa được thu. Giá trị bootstrap sau một bước cắt là giá trị của quan sát cuối của lượt cũ, không phải của quan sát đầu lượt mới mà môi trường trả về sau khi tự đặt lại.

Với $w$ cố định, $V^{\mathrm{targ}}_t$ là lợi tức λ cắt tại biên gần nhất của bước $t$ (kết thúc, cắt ngắn hoặc biên đoạn), theo (12.9)–(12.10) và Bài tập 12.5 của Sutton và Barto (2018, tr. 296–297); Ví dụ 10.10(ii) là trường hợp $h=2$. Hai bước của Ví dụ 10.10 là hai vòng của bước 3.

::: remark Nhận xét 10.17 (Vai trò của $\gamma$ và các nhầm lẫn)
1. Ước lượng thực hành thường là $\sum_t\widehat A_t\psi_t$, không có trọng số $\gamma^t$. Kỳ vọng của nó, khi GAE γ-just, là $\mathbb E\bigl[\sum_tA_\pi(S_t,A_t)\psi_t\bigr]$, tức $g^\gamma$ của Schulman và cộng sự (2016, (6)), không phải $\nabla_\theta J$ (Ví dụ 09.21; Nota và Thomas, 2020). Bài báo GAE coi $\gamma$ là một tham số giảm phương sai cho bài toán không chiết khấu (§2).
2. Ghi một bước cắt ngắn thành kết thúc, $Z=1$, xóa phần bootstrap $\gamma\hat v$ của quan sát cuối: mục tiêu của critic mất giá trị của tương lai, và actor bị phạt ở các bước gần giới hạn thời gian dù chúng không khác các bước khác.
3. Trên đoạn thu, Mệnh đề 10.15(a) không áp dụng cho các lượt bị cắt ở biên, vì $\widehat A_t$ khi đó bootstrap từ $\hat v(S_h)$.
:::

**Trong thực hành.** Bộ đệm lưu các mảng cỡ $h\times N$ cho $R$, $Z$, $U$, $V$, cộng giá trị của các quan sát cuối khi cắt ngắn và $N$ giá trị tại biên đoạn; Thuật toán 10.16 chạy độc lập trên từng cột môi trường. Mục tiêu $V^{\mathrm{targ}}_t$ dùng lợi thế trước khi chuẩn hóa, vì nó là một lợi tức λ.

Như vậy, Bổ đề 10.12 viết lợi thế $n$ bước thành tổng sai số TD, Định nghĩa 10.13 trộn mọi lợi tức $n$ bước thành lợi tức λ, và Mệnh đề 10.14 đưa GAE về một tổng có trọng số $(\gamma\lambda)^k$ tính được bằng truy hồi lùi; Thuật toán 10.16 thêm hai cờ $Z$, $U$ để tính trên đoạn thu. Mệnh đề 10.15 chỉ bảo đảm gradient không chệch khi $\lambda=1$ với lượt đầy đủ hoặc khi critic đúng. Mọi ước lượng của Mục 2–3 vẫn cần dữ liệu của chính sách đang được cập nhật, nên giới hạn thứ hai của Mục 1 còn nguyên: sau một bước, dữ liệu đã cũ. Trong Mục 4, chúng ta tìm một công thức chính xác cho mức thay đổi $J(\pi')-J(\pi)$ rồi xấp xỉ nó bằng dữ liệu của $\pi$.

*Nguồn: bài giảng gốc lecture10_policy_gradient_part2.pdf (2025–2026), trang 13, 24; Sutton và Barto (2018), §7.1, §12.1–12.3; Schulman và cộng sự (2016), §2–3, Phụ lục B.*

---

## 4. Hàm thay thế và chặn cải thiện

Trên chuỗi hai trạng thái, các lượt thu bằng chính sách $p_A=\tfrac12$, $p_B=\tfrac23$ cho mẫu không chệch của gradient $(0{,}2;\,0{,}3)$ tại chính sách đó (Hệ quả 09.26), nhưng không cho biết $J$ của chính sách $p'_A=0{,}6$, $p'_B=0{,}8$ nếu không chạy chính sách này. Muốn dùng lại dữ liệu của $\pi_{\mathrm{old}}$ cho một bước lớn, chúng ta cần đánh giá một chính sách ứng viên $\pi'$ trước khi chạy nó, và biết sai số của phép đánh giá đó phụ thuộc thế nào vào khoảng cách giữa $\pi'$ và $\pi_{\mathrm{old}}$. Hình dưới tóm tắt khó khăn.

![Vòng phản hồi bốn khung nối bằng mũi tên. Khung một: chính sách pi old sinh dữ liệu S t, A t, R t+1, với trạng thái phân bố theo nu mũ pi old. Khung hai: từ dữ liệu, ước lượng lợi thế A mũ t và tính bước cập nhật theta old thành theta. Khung ba: chính sách mới pi theta. Khung bốn: pi theta thăm trạng thái theo phân bố nu mũ pi theta, khác nu mũ pi old. Mũi tên nét đứt từ khung bốn quay về khung một ghi: dữ liệu theo nu mũ pi theta chỉ có sau khi chạy pi theta.](img/lec-10/policy-update-feedback.svg)

Trên hình, các mũi tên đi theo một vòng cập nhật. Dữ liệu dùng để chọn bước cập nhật được thu theo phân bố trạng thái của chính sách cũ, còn chất lượng của chính sách mới phụ thuộc phân bố trạng thái của chính nó; mũi tên nét đứt cho thấy phân bố thứ hai chỉ quan sát được sau khi đã cập nhật.

<!-- note-topic-id: lec-10-topic-10 -->
### 4.1 Bổ đề hiệu hiệu năng

Với chính sách $\pi$ và một chính sách khác $\pi'$, đặt $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$: lợi thế trung bình, đo bằng lợi thế của $\pi$, khi chọn hành động theo $\pi'$ tại $s$. Một cách trực quan, nếu $\pi'$ chọn hành động có lợi thế dương ở những trạng thái nó hay thăm, thì $\pi'$ tốt hơn $\pi$. Ví dụ sau kiểm trực giác này.

::: example Ví dụ 10.11 (Đổi chính sách trên chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$. Chính sách cũ $\pi$: $p_A=\tfrac12$, $p_B=\tfrac23$, với $J(\pi)=1{,}4$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$. Chính sách mới $\pi'$: $p'_A=0{,}6$, $p'_B=0{,}8$.

**Giá trị thật.** $v_{\pi'}(s_B)=0{,}8\cdot3=2{,}4$ và $J(\pi')=0{,}6\cdot0{,}9\cdot2{,}4+0{,}4\cdot1=1{,}696$, nên $\Delta J=J(\pi')-J(\pi)=0{,}296$.

**Lợi thế trung bình theo $\pi'$.** $A_\pi(s_A,\pi')=0{,}6\cdot0{,}4+0{,}4\cdot(-0{,}4)=0{,}08$ và $A_\pi(s_B,\pi')=0{,}8\cdot1+0{,}2\cdot(-2)=0{,}4$.

**Cộng theo bước thời gian.** Bước $0$ ở $s_A$; bước $1$ ở $s_B$ với xác suất $p'_A=0{,}6$ dưới $\pi'$ và trọng số $\gamma$: $0{,}08+0{,}9\cdot0{,}6\cdot0{,}4=0{,}296$, đúng bằng $\Delta J$.

**Dùng xác suất của chính sách cũ.** Nếu thay xác suất tới $s_B$ của $\pi'$ bằng của $\pi$, $p_A=0{,}5$: $0{,}08+0{,}9\cdot0{,}5\cdot0{,}4=0{,}26$, lệch $0{,}036$ so với $\Delta J$.

**Kiểm tra lại.** $1{,}696-1{,}4=0{,}296$; độ lệch $0{,}036=0{,}9\cdot(0{,}6-0{,}5)\cdot0{,}4$.
:::

Đẳng thức trong Ví dụ 10.11 cộng lợi thế trên các trạng thái mà $\pi'$ thăm, mỗi lần thăm ở bước $t$ có trọng số $\gamma^t$. Để viết nó cho MDP tổng quát, chúng ta cần phân bố chiếm dụng trên đúng các trạng thái chưa kết thúc.

::: definition Định nghĩa 10.18 (Phân bố chiếm dụng trên tập trạng thái chưa kết thúc)
Cho MDP hữu hạn với tập trạng thái chưa kết thúc $\mathcal S=\{s_1,\dots,s_n\}$, phân phối đầu $\mu_0$ trên $\mathcal S$, $0\le\gamma<1$, và chính sách Markov dừng $\pi$. *Phân bố chiếm dụng chiết khấu* của $\pi$ là
$$\begin{aligned}&\nu^\pi(s)\\&=(1-\gamma)\sum_{t\ge0}\gamma^t\\&\quad\times\Pr_\pi(S_t=s,\ t<T),\\&s\in\mathcal S .\end{aligned}$$
Ở dạng véc-tơ hàng, $\nu^{\pi\top}=(1-\gamma)\,\mu_0^\top\Gamma_\pi$ với $\Gamma_\pi=(I-\gamma P_\pi)^{-1}$. Tổng khối lượng xác suất của nó, gọi tắt là khối, là $\nu^\pi(\mathcal S)=\sum_{s\in\mathcal S}\nu^\pi(s)=1-\mathbb E_\pi[\gamma^T]\le1$, với quy ước $\gamma^T=0$ khi lượt không kết thúc. Với hàm $f$ trên $\mathcal S$, viết $\mathbb E_{S\sim\nu^\pi}[f(S)]=\sum_{s\in\mathcal S}\nu^\pi(s)f(s)$.
:::

Dạng véc-tơ suy ra trong một dòng. Theo tính Markov, $\Pr_\pi(S_{t+1}=s',\,t+1<T)=\sum_{s\in\mathcal S}\Pr_\pi(S_t=s,\,t<T)\,(P_\pi)_{ss'}$, nên véc-tơ hàng của các xác suất này là $\mu_0^\top P_\pi^t$; Định lý 03.28 cho $\sum_t\gamma^tP_\pi^t=\Gamma_\pi$. Khối bằng $(1-\gamma)\mathbb E_\pi\bigl[\sum_{t<T}\gamma^t\bigr]=\mathbb E_\pi[1-\gamma^T]$.

Trên $\mathcal S$, $\nu^\pi$ trùng phân bố $\nu^\pi_\gamma$ của Hệ quả 09.24; Hệ quả 09.24 tính cả trạng thái hấp thụ sau khi lượt kết thúc, nơi dồn phần khối $1-\nu^\pi(\mathcal S)$. Tại trạng thái đó $q_\pi=A_\pi=0$ và mọi khoảng cách giữa hai chính sách bằng $0$, nên mọi kỳ vọng của chương, như Mệnh đề 10.5(b), không đổi khi chuyển từ cách viết này sang cách viết kia. Trên chuỗi hai trạng thái, $\nu^\pi(s_A)=0{,}1$ và $\nu^\pi(s_B)=0{,}1\cdot0{,}9\cdot p_A=0{,}045$, khối $0{,}145=1-(0{,}5\cdot0{,}9+0{,}5\cdot0{,}81)$, vì lượt dài $1$ hoặc $2$ bước với xác suất $\tfrac12$; với $\pi'$ của Ví dụ 10.11, $\nu^{\pi'}=(0{,}1;\,0{,}054)$.

Bổ đề sau, theo Kakade và Langford (2002, Bổ đề 6.1), là dạng tổng quát của phép cộng trong Ví dụ 10.11.

::: lemma Bổ đề 10.19 (Hiệu hiệu năng)
**Giả thiết.** MDP hữu hạn với cùng động lực $P$ cho mọi chính sách, $\lvert R_{t+1}\rvert\le R_{\max}$, $0\le\gamma<1$; $\pi$ và $\pi'$ là hai chính sách Markov dừng; cùng một phân phối đầu $\mu_0$ tùy ý. Viết $J_{\mu_0}(\pi)=\mathbb E_\pi[G_0]$ với $S_0\sim\mu_0$.

**Kết luận.**
$$\begin{aligned}&J_{\mu_0}(\pi^\prime)-J_{\mu_0}(\pi)\\&\quad=\mathbb E_{\pi^\prime}\Bigl[\sum_{t=0}^{T-1}\gamma^tA_\pi(S_t,A_t)\Bigr]\\&\quad=\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^{\pi^\prime}(s)\,A_\pi(s,\pi^\prime).\end{aligned}$$
Khi $\mu_0$ tập trung tại $s$, tức $\mu_0(s)=1$, vế trái là $v_{\pi'}(s)-v_\pi(s)$.

**Điều kiện áp dụng.** Lợi thế là của $\pi$, chính sách cũ; quỹ đạo và phân bố chiếm dụng là của $\pi'$, chính sách mới.

**Phạm vi.** Đẳng thức chính xác; vế phải cần quỹ đạo của $\pi'$, nên không tính được chỉ từ dữ liệu của $\pi$.
:::

::: proof
**Bước 1 (một bước).** Với $s\in\mathcal S$ và mọi $a$, Mệnh đề 03.22 và quy ước $v_\pi=0$ tại trạng thái kết thúc cho
$$\begin{aligned}&A_\pi(s,a)=r(s,a)\\&\quad+\gamma\sum_{s'\in\mathcal S}P(s'\mid s,a)\,v_\pi(s')\\&\quad-v_\pi(s).\end{aligned}$$
Đẳng thức không chứa $\pi'$.

**Bước 2 (tính chất tháp trên quỹ đạo của $\pi'$).** Quy ước $v_\pi(S_T)=0$. Trên sự kiện $\{t<T\}$, khi biết $(H_t,A_t)$, cặp $(R_{t+1},S_{t+1})$ có phân phối $P(\cdot\mid S_t,A_t)$, không phụ thuộc chính sách đang chạy (cùng $P$, tính Markov, Bổ đề 03.20(a)). Do đó $\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})\mid H_t,A_t]$ là vế phải của Bước 1 cộng $v_\pi(S_t)$, và
$$\begin{aligned}&\mathbb E_{\pi'}\bigl[\mathbb 1\{t<T\}A_\pi(S_t,A_t)\bigr]\\&\quad=\mathbb E_{\pi'}\bigl[\mathbb 1\{t<T\}\bigl(R_{t+1}\\&\qquad+\gamma v_\pi(S_{t+1})-v_\pi(S_t)\bigr)\bigr].\end{aligned}$$

**Bước 3 (tổng lồng nhau tới $K$).** Với $K$ hữu hạn, trên từng quỹ đạo,
$$
\begin{aligned}
&\sum_{t=0}^{K-1}\gamma^t\mathbb 1\{t<T\}\bigl(R_{t+1}\\
&\qquad+\gamma v_\pi(S_{t+1})-v_\pi(S_t)\bigr)\\
&\quad=\sum_{t<\min(K,T)}\gamma^tR_{t+1}\\
&\qquad+\sum_{t<\min(K,T)}\bigl(\gamma^{t+1}v_\pi(S_{t+1})\\
&\qquad\quad-\gamma^tv_\pi(S_t)\bigr)\\
&\quad=\sum_{t<\min(K,T)}\gamma^tR_{t+1}\\
&\qquad+\gamma^{\min(K,T)}v_\pi(S_{\min(K,T)})\\
&\qquad-v_\pi(S_0).
\end{aligned}
$$
Đẳng thức thứ hai là tổng lồng nhau; số hạng giữa bằng $0$ khi $T\le K$ vì $v_\pi(S_T)=0$, và bằng $\gamma^Kv_\pi(S_K)$ khi $T>K$.

**Bước 4 (qua giới hạn).** Theo Định lý 03.28, $\lvert v_\pi\rvert\le R_{\max}/(1-\gamma)$, nên $\lvert A_\pi\rvert\le2R_{\max}/(1-\gamma)$ và số hạng $\gamma^Kv_\pi(S_K)$ tiến về $0$. Hai vế của Bước 3 bằng nhau trên từng quỹ đạo và bị chặn đều theo $K$ bởi $2R_{\max}/(1-\gamma)^2$. Lấy kỳ vọng hai vế, dùng Bước 2 cho từng số hạng của vế trái, rồi cho $K\to\infty$ nhờ định lý hội tụ trội, ta được
$$\begin{aligned}&\mathbb E_{\pi^\prime}\Bigl[\sum_{t<T}\gamma^tA_\pi(S_t,A_t)\Bigr]\\&\quad=\mathbb E_{\pi^\prime}[G_0]-\mathbb E_{S_0\sim\mu_0}[v_\pi(S_0)]\\&\quad=J_{\mu_0}(\pi^\prime)-J_{\mu_0}(\pi).\end{aligned}$$
Đẳng thức cuối dùng giả thiết hai chính sách có cùng $\mu_0$, nên $\mathbb E_{\mu_0}[v_\pi(S_0)]=J_{\mu_0}(\pi)$.

**Bước 5 (dạng chiếm dụng).** Khi biết $S_t=s$ trên $\{t<T\}$, $A_t\sim\pi'(\cdot\mid s)$, nên $\mathbb E_{\pi'}[\mathbb 1\{t<T\}A_\pi(S_t,A_t)]=\sum_{s\in\mathcal S}\Pr_{\pi'}(S_t=s,\,t<T)\,A_\pi(s,\pi')$. Chuỗi theo $t$ hội tụ tuyệt đối và tổng theo $s$ hữu hạn, nên đổi thứ tự được và
$$\begin{aligned}&\sum_{t\ge0}\gamma^t\sum_{s\in\mathcal S}\Pr_{\pi'}(S_t=s,\,t<T)\\&\qquad\times A_\pi(s,\pi')\\&\quad=\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^{\pi'}(s)\,A_\pi(s,\pi')\end{aligned}$$
theo Định nghĩa 10.18. $\square$
:::

Bổ đề nói rằng mức cải thiện của $\pi'$ so với $\pi$ là tổng chiết khấu của lợi thế, tính bằng lợi thế của $\pi$ nhưng cộng dọc các quỹ đạo của $\pi'$. Kiểm trên Ví dụ 10.11 ở dạng chiếm dụng: $\tfrac1{0{,}1}(0{,}1\cdot0{,}08+0{,}054\cdot0{,}4)=0{,}296$. Hai giả thiết có vai trò riêng.

- Bỏ "cùng $\mu_0$": nếu $\pi'$ xuất phát từ $s_B$ còn $\pi$ từ $s_A$ trên chuỗi hai trạng thái, vế trái là $2{,}4-1{,}4=1$, còn vế phải tính trên quỹ đạo của $\pi'$ từ $s_B$ là $A_\pi(s_B,\pi')=0{,}4=v_{\pi'}(s_B)-v_\pi(s_B)$.
- Bỏ "cùng động lực $P$": nếu $\pi'$ chạy trong một môi trường khác, Bước 2 không còn đúng vì $\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t,A_t]$ không còn bằng $q_\pi(S_t,A_t)$.

Bước 2 dùng cùng $P$ và tính Markov; Bước 4 dùng cùng $\mu_0$ và phần thưởng bị chặn; $\gamma<1$ được dùng ở Bước 4 và Bước 5. Nhầm lẫn thường gặp là đổi vai hai chính sách: lấy trung bình theo $\nu^\pi$ thay cho $\nu^{\pi'}$ thì được $0{,}26$ thay cho $0{,}296$ trên Ví dụ 10.11, tức hàm thay thế của Mục 4.2, không phải đẳng thức.

**Trong thực hành.** Vế phải của Bổ đề 10.19 cần quỹ đạo của $\pi'$ và lợi thế chính xác của $\pi$, nên không tính được từ bộ đệm của $\pi_{\mathrm{old}}$ trước khi chạy $\pi'$. Bổ đề được dùng để đo sai số của mọi xấp xỉ chỉ dùng dữ liệu cũ, như độ lệch $0{,}036$ của Ví dụ 10.11.

Lấy $\mu_0$ tập trung tại một trạng thái cho một tiêu chuẩn cải thiện chính sách không cần $\pi'$ xác định.

::: corollary Hệ quả 10.20 (Cải thiện chính sách cho chính sách mới ngẫu nhiên)
**Giả thiết.** Như Bổ đề 10.19, và $A_\pi(s,\pi')\ge0$ với mọi $s\in\mathcal S$.

**Kết luận.**

- (a) $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s\in\mathcal S$.
- (b) Nếu thêm $A_\pi(s_0,\pi')>0$ thì $v_{\pi'}(s_0)>v_\pi(s_0)$.

**Điều kiện áp dụng.** $A_\pi$ là lợi thế chính xác của $\pi$, tính trên mọi trạng thái của $\mathcal S$.

**Phạm vi.** Điều kiện đủ cho cải thiện tại mọi trạng thái; hệ quả không cho mức cải thiện.
:::

::: proof
Áp dụng Bổ đề 10.19 với $\mu_0$ tập trung tại $s$ và dạng tách theo $t$ của Bước 5: $v_{\pi'}(s)-v_\pi(s)=\sum_{t\ge0}\gamma^t\sum_{s'}\Pr_{\pi'}(S_t=s',\,t<T\mid S_0=s)\,A_\pi(s',\pi')$. Mọi số hạng không âm theo giả thiết, nên (a) đúng. Số hạng $t=0$ bằng $A_\pi(s,\pi')$ vì $S_0=s$; với $s=s_0$ số hạng này dương, nên (b) đúng. $\square$
:::

Định lý 04.13(a)–(b) là trường hợp $\pi'$ xác định: khi đó $A_\pi(s,\pi')=q_\pi(s,\pi'(s))-v_\pi(s)$, và điều kiện $q_\pi(s,\pi'(s))\ge v_\pi(s)$ của Định lý 04.13 chính là $A_\pi(s,\pi')\ge0$. Hệ quả 10.20 mở rộng kết quả đó cho $\pi'$ ngẫu nhiên. Trên Ví dụ 10.11, $A_\pi(s_A,\pi')=0{,}08$ và $A_\pi(s_B,\pi')=0{,}4$ đều dương, và đúng là $v_{\pi'}=(1{,}696;\,2{,}4)>v_\pi=(1{,}4;\,2)$.

<!-- note-topic-id: lec-10-topic-11 -->
### 4.2 Tỉ số chính sách và hàm thay thế

Bổ đề 10.19 cần $\nu^{\pi'}$, phân bố trạng thái của chính sách chưa chạy. Ví dụ 10.11 cho thấy giữ phân bố trạng thái của chính sách cũ và chỉ đổi phân phối hành động thì sai $0{,}036$ trên mức thật $0{,}296$. Về mặt ý tưởng, phép xấp xỉ này dùng được vì trung bình theo hành động của $\pi_\theta$ tính được từ hành động của $\pi_{\mathrm{old}}$ bằng tỉ số lấy mẫu quan trọng (Định nghĩa 06.24), nên mọi đại lượng của nó ước lượng được từ dữ liệu cũ.

::: definition Định nghĩa 10.21 (Tỉ số chính sách, hàm thay thế)
Cho chính sách cũ $\pi_{\mathrm{old}}=\pi_{\theta_{\mathrm{old}}}$ với lợi thế $A_{\mathrm{old}}=A_{\pi_{\mathrm{old}}}$ và phân bố chiếm dụng $\nu^{\mathrm{old}}=\nu^{\pi_{\mathrm{old}}}$, và chính sách $\pi_\theta$ thỏa điều kiện hỗ trợ $\pi_\theta(a\mid s)>0\Rightarrow\pi_{\mathrm{old}}(a\mid s)>0$. *Tỉ số chính sách* (probability ratio) tại cặp $(s,a)$ với $\pi_{\mathrm{old}}(a\mid s)>0$ là $\rho_\theta(s,a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$; với mẫu $(S_t,A_t)$, $A_t\sim\pi_{\mathrm{old}}(\cdot\mid S_t)$, viết $\rho_t(\theta)=\rho_\theta(S_t,A_t)$, tức
$$\rho_t(\theta)=\frac{\pi_\theta(A_t\mid S_t)}{\pi_{\mathrm{old}}(A_t\mid S_t)}.$$
*Hàm thay thế* (surrogate objective) là
$$\begin{aligned}&\mathcal L_{\theta_{\mathrm{old}}}(\theta)\\&=J(\theta_{\mathrm{old}})\\&\quad+\frac1{1-\gamma}\,\mathbb E_{\substack{S\sim\nu^{\mathrm{old}}\\A\sim\pi_{\mathrm{old}}(\cdot\mid S)}}\bigl[\rho_\theta(S,A)\\&\qquad\times A_{\mathrm{old}}(S,A)\bigr]\\&=J(\theta_{\mathrm{old}})\\&\quad+\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^{\mathrm{old}}(s)\\&\qquad\times A_{\mathrm{old}}(s,\pi_\theta).\end{aligned}$$
:::

Đẳng thức giữa hai dạng là phép lấy mẫu quan trọng tại từng trạng thái: $\sum_a\pi_{\mathrm{old}}(a\mid s)\frac{\pi_\theta(a\mid s)}{\pi_{\mathrm{old}}(a\mid s)}A_{\mathrm{old}}(s,a)=\sum_a\pi_\theta(a\mid s)A_{\mathrm{old}}(s,a)$, đúng nhờ điều kiện hỗ trợ.

So với Bổ đề 10.19, hàm thay thế chỉ thay $\nu^{\pi_\theta}$ bằng $\nu^{\mathrm{old}}$; khi viết theo chính sách, ta cũng ký hiệu $\mathcal L_\pi(\pi')$. Tỉ số $\rho_t$ là tỉ số lấy mẫu quan trọng của Định nghĩa 06.24 với chính sách hành vi $\pi_{\mathrm{old}}$ và chính sách đích $\pi_\theta$. Bài giảng gốc (tr. 15) viết kỳ vọng $\mathbb E_t$ mà không nêu phân phối của trạng thái; ở đây phân phối đó là $\nu^{\mathrm{old}}$, có chiết khấu. Hàm $L_{\pi}$ của Schulman và cộng sự (2015, (3)) là cùng đại lượng, viết với độ đo không chuẩn hóa $\nu^{\mathrm{old}}/(1-\gamma)$.

Mệnh đề sau dùng Mệnh đề 10.5 để so $\mathcal L_{\theta_{\mathrm{old}}}$ với $J$ tại $\theta_{\mathrm{old}}$.

::: proposition Mệnh đề 10.22 (Khớp giá trị và gradient tại $\theta_{\mathrm{old}}$)
**Giả thiết.** (G1)–(G4) tại $\theta_{\mathrm{old}}$; tập hành động hữu hạn; $\pi_{\mathrm{old}}(a\mid s)>0$ với mọi $s,a$, như với chính sách softmax; các giả thiết của Hệ quả 09.24.

**Kết luận.** $\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}})=J(\theta_{\mathrm{old}})$ và $\nabla_\theta\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}})=\nabla_\theta J(\theta_{\mathrm{old}})$.

**Điều kiện áp dụng.** $\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ là các đại lượng chính xác của $\pi_{\mathrm{old}}$.

**Phạm vi.** Khớp đến bậc một tại một điểm; mệnh đề không cho cận sai số với bước hữu hạn.
:::

::: proof
**Bước 1 (giá trị).** Tại $\theta=\theta_{\mathrm{old}}$, $A_{\mathrm{old}}(s,\pi_{\mathrm{old}})=\sum_a\pi_{\mathrm{old}}(a\mid s)A_{\mathrm{old}}(s,a)=0$ theo Mệnh đề 10.5(a), nên tổng trong Định nghĩa 10.21 bằng $0$.

**Bước 2 (gradient).** Trong dạng thứ hai của Định nghĩa 10.21, $\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ không phụ thuộc $\theta$, và các tổng theo $s$, $a$ hữu hạn, nên
$$
\begin{aligned}
&\nabla_\theta\mathcal L_{\theta_{\mathrm{old}}}(\theta)\big|_{\theta_{\mathrm{old}}}\\
&=\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^{\mathrm{old}}(s)\\
&\quad\times\sum_a\nabla_\theta\pi_\theta(a\mid s)\big|_{\theta_{\mathrm{old}}}\\
&\qquad\times A_{\mathrm{old}}(s,a)\\
&=\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^{\mathrm{old}}(s)\\
&\quad\times\sum_a\pi_{\mathrm{old}}(a\mid s)\\
&\qquad\times\psi_{\theta_{\mathrm{old}}}(s,a)\,A_{\mathrm{old}}(s,a)\\
&=\nabla_\theta J(\theta_{\mathrm{old}}).
\end{aligned}
$$
Đẳng thức thứ hai dùng $\nabla_\theta\pi_\theta=\pi_\theta\psi_\theta$ trên tập $\pi_\theta>0$; đẳng thức thứ ba là Mệnh đề 10.5(b), với $\nu^{\mathrm{old}}$ trùng phân bố của Hệ quả 09.24 trên $\mathcal S$ và trạng thái hấp thụ không đóng góp (Định nghĩa 10.18). $\square$
:::

Hàm thay thế và hàm mục tiêu có cùng giá trị và cùng tiếp tuyến tại tham số cũ, nên một bước đủ nhỏ theo hướng tăng của $\mathcal L$ cũng làm $J$ tăng; với bước hữu hạn, hai hàm tách nhau.

Kiểm trên chuỗi hai trạng thái: với $\pi'$ của Ví dụ 10.11, dạng tỉ số tại $s_A$ cho $0{,}5\cdot\tfrac{0{,}6}{0{,}5}\cdot0{,}4+0{,}5\cdot\tfrac{0{,}4}{0{,}5}\cdot(-0{,}4)=0{,}08$, và $\mathcal L-J=\tfrac1{0{,}1}(0{,}1\cdot0{,}08+0{,}045\cdot0{,}4)=0{,}26$, như ở Ví dụ 10.11. Gradient của $\mathcal L$ theo $(\theta_A;\,\theta_B)$ tại $\theta_{\mathrm{old}}$ là $\tfrac1{0{,}1}\bigl(0{,}1\cdot0{,}2;\,0{,}045\cdot\tfrac23\bigr)=(0{,}2;\,0{,}3)$, bằng gradient tính trực tiếp của Ví dụ 10.6.

Hai giả thiết của mệnh đề có vai trò riêng.

- Bỏ "$\pi_{\mathrm{old}}(a\mid s)>0$": nếu $\pi_{\mathrm{old}}$ chọn chắc chắn hành động 1 tại $s_B$, dữ liệu không có hành động 2, và dạng tỉ số bỏ mất số hạng $\pi_\theta(2\mid s_B)A_{\mathrm{old}}(s_B,2)$; Bước 2 cũng cần $\pi_\theta>0$ để viết $\nabla_\theta\pi_\theta=\pi_\theta\psi_\theta$.
- Bỏ "$\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ chính xác": với lợi thế ước lượng, Bước 1 không còn đúng. Trên chuỗi hai trạng thái với critic $\hat v=(1;\,1{,}5)$ và $\lambda=0$, kỳ vọng của lợi thế ước lượng tại $s_A$ là $(0{,}35;\,0)$, nên $\sum_a\pi_{\mathrm{old}}(a\mid s_A)\widehat A(s_A,a)=0{,}175\ne0$ và $\mathcal L(\theta_{\mathrm{old}})\ne J(\theta_{\mathrm{old}})$.

**Trong thực hành.** Trên một đoạn thu của $\pi_{\mathrm{old}}$, kỳ vọng trong $\mathcal L$ được thay bằng trung bình đều $\widehat{\mathbb E}_{\mathcal D}[\rho_t(\theta)\widehat A_t]$, với $\widehat A_t$ của Thuật toán 10.16 và $\rho_t(\theta)=\exp\bigl(\log\pi_\theta(A_t\mid S_t)-\log\pi_{\mathrm{old}}(A_t\mid S_t)\bigr)$ tính từ log-xác suất đã lưu khi thu. Hai thay thế này có giá: trung bình đều không có trọng số $\gamma^t$ của $\nu^{\mathrm{old}}$, và lợi thế là ước lượng. Đổi lại, cùng một bộ dữ liệu cho giá trị của $\mathcal L$ tại mọi $\theta$, nên có thể thực hiện nhiều bước tối ưu trên một lần thu.

<!-- note-topic-id: lec-10-topic-12 -->
### 4.3 Khoảng cách giữa hai chính sách

Sai số $0{,}036$ của Ví dụ 10.11 đến từ hiệu $\nu^{\pi'}-\nu^\pi$, và hiệu này đến từ khác biệt giữa hai phân phối hành động tại mỗi trạng thái. Để chặn sai số, chúng ta cần đo khác biệt đó. Về mặt ý tưởng, có hai cách đo: lượng xác suất phải chuyển để biến phân phối hành động này thành phân phối kia, và trung bình của log-tỉ số hai xác suất. Định nghĩa sau đưa vào hai cách đo này.

::: definition Định nghĩa 10.23 (Biến phân toàn phần và phân kỳ Kullback–Leibler)
Cho hai phân phối $q$, $q'$ trên tập hành động hữu hạn $\mathcal A$. Khoảng cách *biến phân toàn phần* (total variation distance, TV) là
$$\begin{aligned}&D_{\mathrm{TV}}(q,q')\\&\quad=\tfrac12\sum_{a\in\mathcal A}\lvert q(a)-q'(a)\rvert .\end{aligned}$$
*Phân kỳ Kullback–Leibler* (Kullback–Leibler divergence) của $q$ đối với $q'$ là
$$\begin{aligned}&D_{\mathrm{KL}}(q\Vert q')\\&\quad=\sum_{a:\,q(a)>0}q(a)\log\frac{q(a)}{q'(a)},\end{aligned}$$
bằng $+\infty$ nếu có $a$ với $q(a)>0=q'(a)$. Với hai chính sách $\pi$, $\pi'$, viết $D_{\mathrm{TV}}(s)=D_{\mathrm{TV}}(\pi'(\cdot\mid s),\pi(\cdot\mid s))$, và $D_{\mathrm{KL}}(s)$ cho KL tại $s$, với chiều cũ‖mới hoặc mới‖cũ ghi tại chỗ dùng; KL trung bình theo phân bố chiếm dụng của chính sách cũ là
$$\begin{aligned}&\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\\&\quad=\mathbb E_{S\sim\nu^{\mathrm{old}}}\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid S)\\&\qquad\qquad\Vert\pi_\theta(\cdot\mid S))\bigr].\end{aligned}$$
:::

$D_{\mathrm{TV}}$ đối xứng, nằm trong $[0,1]$, và bằng hiệu lớn nhất giữa xác suất mà hai phân phối gán cho cùng một tập hành động, $\max_{E\subseteq\mathcal A}\lvert q(E)-q'(E)\rvert$. $D_{\mathrm{KL}}$ không đối xứng và có thể vô hạn; nó là kỳ vọng theo $q$ của log-tỉ số. Với $q=\pi_{\mathrm{old}}(\cdot\mid s)$ và $q'=\pi_\theta(\cdot\mid s)$, $D_{\mathrm{KL}}(q\Vert q')=\mathbb E_{A\sim\pi_{\mathrm{old}}(\cdot\mid s)}[-\log\rho_\theta(s,A)]$, nên KL gắn trực tiếp với tỉ số chính sách của Định nghĩa 10.21. Tại $s_B$ của Ví dụ 10.11, với $\pi(\cdot\mid s_B)=(\tfrac23;\,\tfrac13)$ và $\pi'(\cdot\mid s_B)=(0{,}8;\,0{,}2)$: $D_{\mathrm{TV}}=\tfrac2{15}\approx0{,}1333$, $D_{\mathrm{KL}}(\pi\Vert\pi')=0{,}04873$ và $D_{\mathrm{KL}}(\pi'\Vert\pi)=0{,}04369$; hai chiều KL khác nhau.

::: proposition Mệnh đề 10.24 (Hai tính chất của KL)
**Giả thiết.** $q$, $q'$ là hai phân phối trên tập hữu hạn $\mathcal A$.

**Kết luận.**

- (a) $D_{\mathrm{KL}}(q\Vert q')\ge0$, với dấu bằng khi và chỉ khi $q=q'$.
- (b) Bất đẳng thức Pinsker: $D_{\mathrm{TV}}(q,q')\le\sqrt{D_{\mathrm{KL}}(q\Vert q')/2}$; vì $D_{\mathrm{TV}}$ đối xứng, bất đẳng thức cũng đúng với $D_{\mathrm{KL}}(q'\Vert q)$.

**Điều kiện áp dụng.** Logarit tự nhiên.

**Phạm vi.** (b) chỉ cho cận trên của $D_{\mathrm{TV}}$; không có cận ngược tổng quát.
:::

::: proof
**Bước 1 (bất đẳng thức logarit).** Hàm $f(x)=x-1-\log x$ trên $(0,\infty)$ có $f'(x)=1-1/x$, âm khi $x<1$ và dương khi $x>1$, nên $f(x)\ge f(1)=0$, dấu bằng khi và chỉ khi $x=1$. Tức là $\log x\le x-1$.

**Bước 2 (kết luận a).** Nếu có $a$ với $q(a)>0=q'(a)$ thì $D_{\mathrm{KL}}=+\infty>0$. Ngược lại, áp dụng Bước 1 với $x=q'(a)/q(a)$ trên miền $\{q>0\}$:
$$
\begin{aligned}
&-D_{\mathrm{KL}}(q\Vert q')\\
&\quad=\sum_{a:\,q(a)>0}q(a)\log\frac{q'(a)}{q(a)}\\
&\quad\le\sum_{a:\,q(a)>0}q(a)\Bigl(\frac{q'(a)}{q(a)}-1\Bigr)\\
&\quad=\sum_{a:\,q(a)>0}q'(a)-1\\
&\quad\le0 .
\end{aligned}
$$
Dấu bằng cần $q'(a)=q(a)$ trên $\{q>0\}$ (Bước 1) và $\sum_{q(a)>0}q'(a)=1$, tức $q'=q$; ngược lại $q'=q$ cho $D_{\mathrm{KL}}=0$.

**Bước 3 (kết luận b, ý tưởng chứng minh).** Chứng minh đầy đủ nằm ngoài phạm vi học phần; xem Cover và Thomas (2006, Bổ đề 11.6.1, tr. 370), nơi sách dùng logarit cơ số $2$ nên hằng số viết là $1/(2\ln2)$, và Achiam và cộng sự (2017, (7)). Ta gộp các hành động thành hai nhóm, $\{a:q(a)>q'(a)\}$ và phần bù. Phép gộp giữ nguyên $D_{\mathrm{TV}}$ và không làm $D_{\mathrm{KL}}$ tăng, theo bất đẳng thức xử lý dữ liệu cho KL (Cover và Thomas, 2006). Do đó chỉ cần chứng minh bất đẳng thức cho phân phối trên hai điểm, $p\log\frac p{p'}+(1-p)\log\frac{1-p}{1-p'}\ge2(p-p')^2$, bằng cách khảo sát hiệu hai vế như một hàm của $p'$. $\square$
:::

Kết luận (a) cho phép dùng KL như một độ đo khác biệt: nó bằng $0$ đúng khi hai chính sách trùng nhau tại trạng thái đó. Kết luận (b) cho phép chuyển một ràng buộc trên KL thành ràng buộc trên TV. Tại $s_B$ của Ví dụ 10.11, $\tfrac2{15}=0{,}1333\le\sqrt{0{,}04873/2}=0{,}1561$; tại $s_A$, $0{,}1\le\sqrt{0{,}02041/2}=0{,}1010$, gần dấu bằng vì hai phân phối gần nhau.

<!-- note-topic-id: lec-10-topic-13 -->
### 4.4 Chặn cải thiện

Trên Ví dụ 10.11, sai số của hàm thay thế là $\frac1{1-\gamma}\sum_s\bigl(\nu^{\pi'}(s)-\nu^\pi(s)\bigr)A_\pi(s,\pi')=\tfrac1{0{,}1}(0{,}054-0{,}045)\cdot0{,}4=0{,}036$. Sai số này nhỏ khi $\nu^{\pi'}$ gần $\nu^\pi$ và lợi thế trung bình nhỏ. Một cách trực quan, nếu tại mọi trạng thái $\pi'$ chọn hành động gần như $\pi$, thì hai chính sách thăm các trạng thái với tần suất gần nhau; khác biệt nhỏ ở mỗi bước tích lũy dọc lượt, nên sai lệch giữa hai phân bố chiếm dụng có thêm thừa số $\gamma/(1-\gamma)$. Bổ đề sau chặn khoảng cách giữa hai phân bố chiếm dụng bằng khoảng cách TV trung bình giữa hai chính sách.

::: lemma Bổ đề 10.25 (Dịch chuyển phân bố chiếm dụng)
**Giả thiết.** MDP hữu hạn với tập trạng thái chưa kết thúc $\mathcal S$, $0\le\gamma<1$; $\pi$, $\pi'$ Markov dừng, cùng $\mu_0$ và $P$; $\nu=\nu^\pi$, $\nu'=\nu^{\pi'}$ theo Định nghĩa 10.18.

**Kết luận.**
$$\begin{aligned}&\lVert\nu'-\nu\rVert_1\\&\quad\le\frac{2\gamma}{1-\gamma}\,\mathbb E_{S\sim\nu}\bigl[D_{\mathrm{TV}}(S)\bigr],\\&\lVert x\rVert_1=\sum_{s\in\mathcal S}\lvert x(s)\rvert .\end{aligned}$$

**Điều kiện áp dụng.** Chuẩn và kỳ vọng lấy trên $\mathcal S$; trạng thái kết thúc không được tính.

**Phạm vi.** Cận theo TV trung bình dưới $\nu$, phân bố của chính sách cũ.
:::

::: proof
Ký hiệu $\Gamma=\Gamma_\pi$, $\bar\Gamma=\Gamma_{\pi'}$, $\Delta_P=P_{\pi'}-P_\pi$, $\Delta_\pi(a\mid s)=\pi'(a\mid s)-\pi(a\mid s)$; mọi véc-tơ phân bố là véc-tơ hàng. Với ma trận $X$, đặt $\lVert X\rVert_\infty=\max_i\sum_j\lvert X_{ij}\rvert$, chuẩn tổng hàng.

**Bước 1 (chặn $\bar\Gamma$).** Mọi phần tử của $P_{\pi'}$ không âm và mỗi hàng có tổng không quá $1$, vì phần còn thiếu là xác suất đi tới trạng thái kết thúc; do đó $\lVert P_{\pi'}\rVert_\infty\le1$. Theo Định lý 03.28, $\bar\Gamma=\sum_{t\ge0}\gamma^tP_{\pi'}^t$, nên $\lVert\bar\Gamma\rVert_\infty\le\sum_t\gamma^t\lVert P_{\pi'}\rVert^t_\infty\le\frac1{1-\gamma}$.

**Bước 2 (hiệu hai nghịch đảo).** $\Gamma^{-1}-\bar\Gamma^{-1}=(I-\gamma P_\pi)-(I-\gamma P_{\pi'})=\gamma\Delta_P$. Nhân trái với $\Gamma$ và nhân phải với $\bar\Gamma$: $\bar\Gamma-\Gamma=\gamma\,\Gamma\Delta_P\bar\Gamma$.

**Bước 3 (hiệu hai phân bố).** Theo Định nghĩa 10.18,
$$
\begin{aligned}
&\nu'^\top-\nu^\top\\
&=(1-\gamma)\,\mu_0^\top(\bar\Gamma-\Gamma)\\
&=\gamma\,(1-\gamma)\,\mu_0^\top\Gamma\,\Delta_P\,\bar\Gamma\\
&=\gamma\,\nu^\top\Delta_P\,\bar\Gamma.
\end{aligned}
$$
Đẳng thức thứ hai dùng Bước 2, đẳng thức thứ ba dùng Định nghĩa 10.18.

**Bước 4 (chuẩn của tích).** Với véc-tơ hàng $x$ và ma trận $X$,
$$
\begin{aligned}
\lVert x^\top X\rVert_1
&=\sum_j\Bigl\lvert\sum_ix_iX_{ij}\Bigr\rvert\\
&\le\sum_i\lvert x_i\rvert\sum_j\lvert X_{ij}\rvert\\
&\le\lVert x\rVert_1\lVert X\rVert_\infty.
\end{aligned}
$$
Đẳng thức là định nghĩa chuẩn $1$, bất đẳng thức thứ nhất là bất đẳng thức tam giác, bất đẳng thức thứ hai là định nghĩa chuẩn tổng hàng. Cùng Bước 1 và Bước 3: $\lVert\nu'-\nu\rVert_1\le\frac{\gamma}{1-\gamma}\lVert\nu^\top\Delta_P\rVert_1$.

**Bước 5 (chặn $\nu^\top\Delta_P$).** Thành phần $s'$ của $\nu^\top\Delta_P$ là $\sum_s\nu(s)\sum_a\Delta_\pi(a\mid s)P(s'\mid s,a)$. Do đó
$$
\begin{aligned}
&\lVert\nu^\top\Delta_P\rVert_1\\
&\le\sum_{s\in\mathcal S}\nu(s)\sum_a\lvert\Delta_\pi(a\mid s)\rvert\\
&\qquad\times\sum_{s'\in\mathcal S}P(s'\mid s,a)\\
&\le\sum_{s\in\mathcal S}\nu(s)\sum_a\lvert\Delta_\pi(a\mid s)\rvert\\
&=2\,\mathbb E_{S\sim\nu}[D_{\mathrm{TV}}(S)].
\end{aligned}
$$
Bất đẳng thức thứ nhất là bất đẳng thức tam giác; bất đẳng thức thứ hai dùng $\sum_{s'\in\mathcal S}P(s'\mid s,a)\le1$; đẳng thức cuối là Định nghĩa 10.23.

**Bước 6 (cận của bổ đề).** Bước 4 và Bước 5 cho $\lVert\nu'-\nu\rVert_1\le\frac{\gamma}{1-\gamma}\cdot2\,\mathbb E_\nu[D_{\mathrm{TV}}]$. $\square$
:::

Sự kết thúc được dùng ở hai chỗ, Bước 1 và Bước 5, và cả hai chỉ làm các tổng nhỏ đi: xác suất đi tới trạng thái kết thúc không còn nằm trong $P_\pi$. Achiam và cộng sự (2017, phụ lục, Bổ đề 3, (25)) chứng minh cùng cận với véc-tơ cột và chuẩn tổng cột. Trên Ví dụ 10.11, $D_{\mathrm{TV}}(s_A)=0{,}1$, $D_{\mathrm{TV}}(s_B)=\tfrac2{15}$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}1\cdot0{,}1+0{,}045\cdot\tfrac2{15}=0{,}016$; vế trái là $\lvert0{,}1-0{,}1\rvert+\lvert0{,}054-0{,}045\rvert=0{,}009$, vế phải là $18\cdot0{,}016=0{,}288$.

Ghép Bổ đề 10.19, hàm thay thế và Bổ đề 10.25 cho cận dưới của mức cải thiện, gọi là *chặn cải thiện* (còn gọi là cận cải thiện; policy improvement bound).

::: theorem Định lý 10.26 (Chặn cải thiện)
**Giả thiết.** Như Bổ đề 10.19: MDP hữu hạn, cùng $P$ và $\mu_0$, $\lvert R_{t+1}\rvert\le R_{\max}$, $0\le\gamma<1$, $\pi$ và $\pi'$ Markov dừng; thêm điều kiện hỗ trợ $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$.

**Kết luận.** Với $\chi_{\pi'}=\max_{s\in\mathcal S}\lvert A_\pi(s,\pi')\rvert$,
$$\begin{aligned}&J(\pi')-J(\pi)\\&\quad\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\&\qquad-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\\&\qquad\quad\times\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}(S)\bigr].\end{aligned}$$
Vì $\chi_{\pi'}\le\bar\chi=\max_{s,a}\lvert A_\pi(s,a)\rvert$, cận vẫn đúng khi thay $\chi_{\pi'}$ bằng $\bar\chi$.

**Điều kiện áp dụng.** $A_\pi$ và $\nu^\pi$ là các đại lượng chính xác của $\pi$.

**Phạm vi.** Cận một phía; cận trên đối xứng, với dấu cộng, có cùng chứng minh (Achiam và cộng sự, 2017, Định lý 1). Thừa số $1/(1-\gamma)^2$ làm cận rất bảo thủ khi $\gamma$ gần $1$: với $\gamma=0{,}9$, thừa số là $100$.
:::

::: proof
Đặt $\bar a(s)=A_\pi(s,\pi')$ và $\langle x,f\rangle=\sum_{s\in\mathcal S}x(s)f(s)$.

**Bước 1 (đẳng thức chính xác).** Bổ đề 10.19: $J(\pi')-J(\pi)=\frac1{1-\gamma}\langle\nu',\bar a\rangle$, với $\nu'=\nu^{\pi'}$.

**Bước 2 (tách).** $\langle\nu',\bar a\rangle=\langle\nu,\bar a\rangle+\langle\nu'-\nu,\bar a\rangle$, với $\nu=\nu^\pi$.

**Bước 3 (hàm thay thế).** Theo Định nghĩa 10.21, với $\pi_{\mathrm{old}}=\pi$ và $\pi_\theta=\pi'$, điều kiện hỗ trợ cho $\frac1{1-\gamma}\langle\nu,\bar a\rangle=\mathcal L_\pi(\pi')-J(\pi)$.

**Bước 4 (bất đẳng thức Hölder).** $\langle\nu'-\nu,\bar a\rangle\ge-\sum_s\lvert\nu'(s)-\nu(s)\rvert\,\lvert\bar a(s)\rvert\ge-\lVert\nu'-\nu\rVert_1\,\chi_{\pi'}$.

**Bước 5 (Bổ đề 10.25).** Ghép các bước:
$$
\begin{aligned}
&J(\pi')-J(\pi)\\
&=\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\
&\quad+\tfrac1{1-\gamma}\langle\nu'-\nu,\bar a\rangle\\
&\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\
&\quad-\tfrac{\chi_{\pi'}}{1-\gamma}\lVert\nu'-\nu\rVert_1\\
&\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\
&\quad-\tfrac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\,\mathbb E_{S\sim\nu}[D_{\mathrm{TV}}(S)].
\end{aligned}
$$
Đẳng thức ghép Bước 1–3, bất đẳng thức thứ nhất là Bước 4, bất đẳng thức thứ hai là Bổ đề 10.25. $\square$
:::

Định lý nói rằng mức cải thiện thật không nhỏ hơn mức cải thiện mà hàm thay thế dự báo, trừ một phạt tỉ lệ với khoảng cách TV trung bình giữa hai chính sách. Khi $\pi'$ gần $\pi$, phạt nhỏ và hàm thay thế đáng tin; khi $\pi'$ xa, phạt có thể lớn hơn mọi mức tăng dự báo. Các giả thiết có vai trò riêng.

- Bỏ "$\gamma<1$": trên hành lang ngắn, $\gamma=1$ làm thừa số $2\gamma/(1-\gamma)^2$ vô hạn và $\nu$ không xác định; định lý không áp dụng.
- Bỏ "lợi thế và phân bố chính xác": nếu $\mathcal L$ được thay bằng một ước lượng mẫu, vế phải có thêm sai số ước lượng mà định lý không kiểm soát, nên cận không còn chứng nhận được cải thiện.
- Bỏ "điều kiện hỗ trợ": cận viết theo dạng thứ hai của Định nghĩa 10.21, $\sum_a\pi'(a\mid s)A_\pi(s,a)$, vẫn đúng; dạng tỉ số, dạng duy nhất ước lượng được từ dữ liệu của $\pi$, mất hiệu lực ở Bước 3, như ví dụ sau Mệnh đề 10.22 với $\pi_{\mathrm{old}}$ chọn chắc chắn hành động 1 tại $s_B$.

Bước 1 dùng các giả thiết của Bổ đề 10.19; Bước 5 dùng $\gamma<1$ và sự kết thúc qua Bổ đề 10.25. Achiam và cộng sự (2017, Hệ quả 1, (5)) phát biểu cùng cận; bài giảng gốc (tr. 14, 16) chỉ nêu động cơ "đừng đi quá xa", không cho cận.

**Trong thực hành.** Không đại lượng nào của cận tính được từ một bộ đệm: $\chi_{\pi'}$ cần lợi thế chính xác tại mọi trạng thái, còn $\nu^\pi$ là kỳ vọng có chiết khấu trong khi bộ đệm chỉ cho trung bình đều trên các trạng thái đã thăm. Với $\gamma=0{,}99$, thừa số $2\gamma/(1-\gamma)^2$ bằng $19\,800$. Vì vậy cận được dùng để chọn đại lượng cần kiểm soát, là khoảng cách trung bình giữa hai chính sách theo phân bố trạng thái của chính sách cũ.

::: example Ví dụ 10.12 (Chặn cải thiện trên chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái, $\gamma=0{,}9$, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$, $\nu^\pi=(0{,}1;\,0{,}045)$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$. Bước của Ví dụ 10.11: $p'_A=0{,}6$, $p'_B=0{,}8$, $\Delta J=0{,}296$, $\mathcal L-J=0{,}26$, $A_\pi(s,\pi')=(0{,}08;\,0{,}4)$, $D_{\mathrm{TV}}=(0{,}1;\,\tfrac2{15})$.

**Bước của Ví dụ 10.11.** $\chi_{\pi'}=0{,}4$ và $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}016$, nên phạt là $\frac{2\cdot0{,}9\cdot0{,}4}{0{,}01}\cdot0{,}016=1{,}152$, lớn hơn $0{,}26$; cận dưới là $0{,}26-1{,}152=-0{,}892$, không chứng nhận được cải thiện dù $\Delta J=0{,}296>0$.

**Bước nhỏ chỉ đổi $s_B$.** Lấy $p'_A=\tfrac12$, $p'_B=\tfrac23+\Delta p$ với bước $\Delta p>0$. Khi đó $\Delta J=0{,}5\cdot0{,}9\cdot3\Delta p=1{,}35\Delta p$. Vì $p_A$ không đổi, $\nu(s_B)$ không đổi, nên hàm thay thế chính xác: $A_\pi(s_A,\pi')=0$, $A_\pi(s_B,\pi')=(\tfrac23+\Delta p)\cdot1+(\tfrac13-\Delta p)(-2)=3\Delta p$, và $\mathcal L-J=\tfrac1{0{,}1}\cdot0{,}045\cdot3\Delta p=1{,}35\Delta p$. Cận vẫn phạt: $\chi_{\pi'}=3\Delta p$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}045\Delta p$, phạt $\frac{2\cdot0{,}9\cdot3\Delta p}{0{,}01}\cdot0{,}045\Delta p=24{,}3(\Delta p)^2$. Cận dương khi và chỉ khi $1{,}35\Delta p>24{,}3(\Delta p)^2$, tức $\Delta p<1{,}35/24{,}3\approx0{,}0556$.

**Diễn giải.** Cận chỉ chứng nhận được những bước rất nhỏ, kể cả khi hàm thay thế không sai chút nào: phạt của Định lý 10.26 không dùng thông tin rằng $\nu(s_B)$ không đổi, vì cận phải đúng cho mọi MDP và mọi $\pi'$.

**Kiểm tra lại.** $\Delta p=0{,}05$: $0{,}0675-0{,}06075=0{,}00675>0$; $\Delta p=0{,}06$: $0{,}081-0{,}08748=-0{,}00648<0$.
:::

Các phương pháp miền tin cậy ràng buộc KL. Hệ quả sau đổi phạt sang KL trung bình bằng bất đẳng thức Pinsker.

::: corollary Hệ quả 10.27 (Chặn cải thiện dạng KL trung bình)
**Giả thiết.** Như Định lý 10.26.

**Kết luận.** Với $\bar D_{\mathrm{KL}}=\mathbb E_{S\sim\nu^\pi}[D_{\mathrm{KL}}(S)]$, lấy theo một trong hai chiều $D_{\mathrm{KL}}(\pi\Vert\pi')$ hoặc $D_{\mathrm{KL}}(\pi'\Vert\pi)$ tại mỗi trạng thái,
$$\begin{aligned}&J(\pi')-J(\pi)\\&\quad\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\&\qquad-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\tfrac12\,\bar D_{\mathrm{KL}}}.\end{aligned}$$

**Điều kiện áp dụng.** Như Định lý 10.26: $A_\pi$ và $\nu^\pi$ là các đại lượng chính xác của $\pi$.

**Phạm vi.** Cận yếu hơn Định lý 10.26, vì Bước 1 và Bước 2 của chứng minh đều là bất đẳng thức; đổi lại, phạt viết theo KL, đại lượng mà các phương pháp miền tin cậy ràng buộc.
:::

::: proof
**Bước 1 (Pinsker theo trạng thái).** Mệnh đề 10.24(b) cho $D_{\mathrm{TV}}(s)\le\sqrt{D_{\mathrm{KL}}(s)/2}$ với mỗi $s$ và với cả hai chiều KL.

**Bước 2 (Jensen với khối không quá $1$).** Đặt $x_s=D_{\mathrm{KL}}(s)/2$ và $\bar\nu=\nu^\pi(\mathcal S)\le1$ (Định nghĩa 10.18). Nếu $\bar\nu=0$, hai vế dưới đây bằng $0$. Nếu $\bar\nu>0$, các trọng số $\nu^\pi(s)/\bar\nu$ tạo thành một phân phối, và hàm căn bậc hai lõm, nên
$$
\begin{aligned}
&\sum_s\nu^\pi(s)\sqrt{x_s}\\
&=\bar\nu\sum_s\frac{\nu^\pi(s)}{\bar\nu}\sqrt{x_s}\\
&\le\bar\nu\sqrt{\sum_s\frac{\nu^\pi(s)}{\bar\nu}x_s}\\
&=\sqrt{\bar\nu}\,\sqrt{\sum_s\nu^\pi(s)x_s}\\
&\le\sqrt{\sum_s\nu^\pi(s)x_s}.
\end{aligned}
$$
Bất đẳng thức thứ nhất là bất đẳng thức Jensen, bất đẳng thức thứ hai dùng $\bar\nu\le1$.

**Bước 3 (ghép).** Bước 1 và Bước 2 cho $\mathbb E_\nu[D_{\mathrm{TV}}]\le\sum_s\nu^\pi(s)\sqrt{x_s}\le\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$. Thay vào Định lý 10.26, với hệ số của phạt không âm, được kết luận. $\square$
:::

Achiam và cộng sự (2017, Hệ quả 3) phát biểu cùng kết quả với chiều $D_{\mathrm{KL}}(\pi'\Vert\pi)$; Bước 1 cho phép dùng cả chiều $D_{\mathrm{KL}}(\pi\Vert\pi')$ mà TRPO ràng buộc. Bước 2 cần $\bar\nu\le1$ vì $\nu^\pi$ chỉ xét trên trạng thái chưa kết thúc; với cách viết của Hệ quả 09.24, phần khối còn lại nằm ở trạng thái hấp thụ, nơi $D_{\mathrm{KL}}=0$, và Jensen áp dụng trực tiếp.

Trên bước của Ví dụ 10.12, KL theo chiều cũ‖mới là $(0{,}02041;\,0{,}04873)$, $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}02041+0{,}045\cdot0{,}04873=0{,}004234$, và phạt là $72\sqrt{0{,}002117}=3{,}31$; theo chiều mới‖cũ, $\bar D_{\mathrm{KL}}=0{,}003980$ và phạt là $3{,}21$. Cả hai lớn hơn phạt dạng TV $1{,}152$.

::: remark Nhận xét 10.28 (Định lý 1 của Schulman và cộng sự, 2015)
Schulman và cộng sự (2015, Định lý 1) chứng minh một cận cùng loại với độ lệch TV lớn nhất theo trạng thái, $D^{\max}_{\mathrm{TV}}=\max_sD_{\mathrm{TV}}(s)$:
$$\begin{aligned}J(\pi^\prime)&\ge\mathcal L_\pi(\pi^\prime)\\&\quad-\frac{4\bar\chi\gamma}{(1-\gamma)^2}\bigl(D^{\max}_{\mathrm{TV}}\bigr)^2 .\end{aligned}$$
Chứng minh nằm ngoài phạm vi học phần; bài báo cho hai chứng minh, bằng ghép cặp (coupling) hai chính sách (Phụ lục A) và bằng lý thuyết nhiễu loạn (Phụ lục B), cách sau gần với cách ma trận của Bổ đề 10.25. Trên Ví dụ 10.12, $\bar\chi=2$: bước của Ví dụ 10.11 có $D^{\max}_{\mathrm{TV}}=\tfrac2{15}$ và phạt $\frac{4\cdot2\cdot0{,}9}{0{,}01}\cdot\bigl(\tfrac2{15}\bigr)^2=12{,}8$; bước nhỏ có phạt $720(\Delta p)^2$, dương khi $\Delta p<0{,}001875$. Trên ví dụ này, cận dạng lớn nhất lỏng hơn cận dạng trung bình của Định lý 10.26.
:::

<!-- note-topic-id: lec-10-topic-14 -->
### 4.5 Cải thiện đơn điệu và bài toán miền tin cậy

Định lý 10.26 cho một hàm của $\pi'$ nằm dưới $J(\pi')$ ở mọi nơi. Về mặt ý tưởng, nếu hàm đó còn chạm $J$ tại chính sách hiện tại, thì mọi bước làm hàm đó tăng cũng làm $J$ tăng.

::: corollary Hệ quả 10.29 (Cải thiện đơn điệu qua hàm chặn dưới)
**Giả thiết.** Như Định lý 10.26 cho mỗi cặp $(\pi_k,\pi)$, với $\pi$ chạy trong một lớp chính sách chứa $\pi_k$. Đặt $\bar\chi_k=\max_{s,a}\lvert A_{\pi_k}(s,a)\rvert$, $C_k=\frac{2\gamma\bar\chi_k}{(1-\gamma)^2}$ và
$$\begin{aligned}&\mathcal M_k(\pi)=\mathcal L_{\pi_k}(\pi)\\&\quad-C_k\,\mathbb E_{S\sim\nu^{\pi_k}}\bigl[D_{\mathrm{TV}}(\pi(\cdot\mid S),\\&\qquad\qquad\pi_k(\cdot\mid S))\bigr].\end{aligned}$$

**Kết luận.** Nếu $\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)$, đặc biệt nếu $\pi_{k+1}$ cực đại hóa $\mathcal M_k$ trên lớp chính sách, thì $J(\pi_{k+1})\ge J(\pi_k)$.

**Điều kiện áp dụng.** $A_{\pi_k}$ và $\nu^{\pi_k}$ tính chính xác; phép cực đại hóa, hoặc ít nhất điều kiện không giảm của $\mathcal M_k$, được kiểm chính xác.

**Phạm vi.** Bảo đảm $J$ không giảm qua các vòng lặp; không bảo đảm hội tụ tới chính sách tối ưu, và không áp dụng khi các đại lượng trên được ước lượng.
:::

::: proof
**Bước 1 ($\mathcal M_k$ nằm dưới $J$).** Với mọi $\pi$ trong lớp, $\chi_\pi\le\bar\chi_k$, nên Định lý 10.26 cho $J(\pi)\ge\mathcal M_k(\pi)$.

**Bước 2 (chạm tại $\pi_k$).** $\mathcal L_{\pi_k}(\pi_k)=J(\pi_k)$ vì $A_{\pi_k}(s,\pi_k)=0$ (Mệnh đề 10.5(a)), và phạt bằng $0$ vì $D_{\mathrm{TV}}(s)=0$ tại mọi $s$; do đó $\mathcal M_k(\pi_k)=J(\pi_k)$.

**Bước 3 (ghép).** $J(\pi_{k+1})\ge\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)=J(\pi_k)$, theo Bước 1, giả thiết, rồi Bước 2. $\square$
:::

Hàm $\mathcal M_k$ nằm dưới $J$ và chạm $J$ tại $\pi_k$; theo thuật ngữ của Hunter và Lange (2004), được Schulman và cộng sự (2015, §3) dẫn, đây là một thuật toán *cực đại hóa qua hàm chặn dưới* (minorize–maximize, MM). Thuật toán 1 của Schulman và cộng sự (2015) dùng cùng lập luận với phạt $D^{\max}_{\mathrm{KL}}$ và hằng $4\bar\chi\gamma/(1-\gamma)^2$.

Trên chuỗi hai trạng thái, $\bar\chi_k=2$ nên $C_k=\frac{2\cdot0{,}9\cdot2}{0{,}01}=360$. Với hai hành động, $A_\pi(s,\pi')=(p'_s-p_s)\bigl(A_\pi(s,1)-A_\pi(s,2)\bigr)$ có trị tuyệt đối $D_{\mathrm{TV}}(s)\,a_s$ với $a_s=\lvert A_\pi(s,1)-A_\pi(s,2)\rvert$, nên
$$
\begin{aligned}
&\mathcal M_k(\pi')-\mathcal M_k(\pi_k)\\
&\quad\le\textstyle\sum_{s}\nu(s)\,D_{\mathrm{TV}}(s)\,c_s,\\
&c_s=\frac{a_s}{1-\gamma}-C_k.
\end{aligned}
$$
Hệ số $c_s$ là $8-360$ tại $s_A$ và $30-360$ tại $s_B$. Mọi bước khác $\pi_k$ đều làm $\mathcal M_k$ giảm, nên thuật toán đứng yên tại $\pi_k$, và kết luận của Hệ quả 10.29 đúng một cách tầm thường. Schulman và cộng sự (2015, §4) nêu cùng hiện tượng: với hệ số phạt mà lý thuyết khuyến nghị, bước cập nhật rất nhỏ.

Hai điều kiện của Hệ quả 10.29 có vai trò riêng.

- Bỏ "đánh giá chính xác": thay $A_{\pi_k}$ và $\nu^{\pi_k}$ bằng ước lượng thì Bước 1 không còn cho $J\ge\mathcal M_k$, vì Định lý 10.26 cần các đại lượng chính xác.
- Bỏ "$\mathcal M_k$ không giảm": một bước làm $\mathcal M_k$ giảm, như mọi bước khác $\pi_k$ trên chuỗi hai trạng thái, không còn được hệ quả bảo đảm, dù $J$ có thể vẫn tăng, như bước của Ví dụ 10.11 với $\Delta J=0{,}296$.

Schulman và cộng sự (2015, §4) thay phạt bằng một ràng buộc, để cho phép bước lớn mà vẫn kiểm soát được khoảng cách.

::: definition Định nghĩa 10.30 (Bài toán miền tin cậy)
Cho chính sách cũ $\pi_{\mathrm{old}}$, lớp chính sách tham số hóa $\{\pi_\theta\}$ chứa $\pi_{\mathrm{old}}$, và bán kính $\kappa>0$. *Bài toán miền tin cậy* (trust region problem) là
$$\begin{aligned}&\max_\theta\\&\mathbb E_{\substack{S\sim\nu^{\mathrm{old}}\\A\sim\pi_{\mathrm{old}}(\cdot\mid S)}}\bigl[\rho_\theta(S,A)\\&\quad\times A_{\mathrm{old}}(S,A)\bigr]\\&\text{với ràng buộc}\\&\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\le\kappa .\end{aligned}$$
Tập $\{\theta:\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\le\kappa\}$ gọi là *miền tin cậy*.
:::

Hàm mục tiêu là $(1-\gamma)\bigl(\mathcal L_{\theta_{\mathrm{old}}}(\theta)-J(\theta_{\mathrm{old}})\bigr)$, nên bài toán cực đại hóa hàm thay thế trong một lân cận đo bằng KL trung bình theo chiều cũ‖mới; bài giảng gốc (tr. 16) mô tả cùng bài toán bằng lời. Schulman và cộng sự (2015) đi tới bài toán này qua ba bước:

- thay phạt bằng ràng buộc KL lớn nhất, phương trình (11);
- thay KL lớn nhất bằng KL trung bình, phương trình (12), mà bài báo gọi là một xấp xỉ heuristic;
- viết lại thành kỳ vọng, phương trình (14), bỏ thừa số $1/(1-\gamma)$ và thay $A$ bằng $Q$.

Các thay đổi ở bước cuối chỉ đổi mục tiêu một hằng số dương hoặc một hằng cộng, nên không đổi nghiệm. Khác với $\mathcal M_k$, bài toán không bảo đảm $J$ tăng; hệ quả sau cho biết nó bảo đảm gì.

::: corollary Hệ quả 10.31 (Mức giảm tối đa của bước miền tin cậy)
**Giả thiết.** Như Định lý 10.26 với $\pi=\pi_k$; $\pi_{k+1}$ là nghiệm chính xác của bài toán của Định nghĩa 10.30 với $\pi_{\mathrm{old}}=\pi_k$, trên một lớp chính sách chứa $\pi_k$.

**Kết luận.**
$$\begin{aligned}&J(\pi_{k+1})-J(\pi_k)\\&\quad\ge-\frac{\sqrt{2\kappa}\,\gamma\,\chi_{\pi_{k+1}}}{(1-\gamma)^2}.\end{aligned}$$

**Điều kiện áp dụng.** Kỳ vọng và KL trung bình lấy theo $\nu^{\pi_k}$ có chiết khấu, với lợi thế chính xác, và bài toán được giải chính xác.

**Phạm vi.** Cận cho mức giảm tối đa, không bảo đảm cải thiện; cận nhỏ khi $\kappa$ nhỏ.
:::

::: proof
**Bước 1 (mục tiêu tối ưu không âm).** $\pi_k$ thuộc lớp chính sách và thỏa ràng buộc vì $\bar D_{\mathrm{KL}}(\pi_k\Vert\pi_k)=0$; giá trị mục tiêu tại $\pi_k$ là $\sum_s\nu^{\pi_k}(s)A_{\pi_k}(s,\pi_k)=0$ (Mệnh đề 10.5(a)). Nghiệm tối ưu có giá trị không nhỏ hơn, nên $\mathcal L_{\pi_k}(\pi_{k+1})-J(\pi_k)\ge0$.

**Bước 2 (chặn phạt).** Ràng buộc cho $\bar D_{\mathrm{KL}}\le\kappa$ theo chiều $\pi_k\Vert\pi_{k+1}$. Hệ quả 10.27 với chiều này cho
$$\begin{aligned}&J(\pi_{k+1})-J(\pi_k)\\&\quad\ge0-\frac{2\gamma\chi_{\pi_{k+1}}}{(1-\gamma)^2}\sqrt{\tfrac\kappa2}\\&\quad=-\frac{\sqrt{2\kappa}\,\gamma\,\chi_{\pi_{k+1}}}{(1-\gamma)^2},\end{aligned}$$
vì $2\sqrt{\kappa/2}=\sqrt{2\kappa}$. $\square$
:::

Hệ quả 10.31 là Mệnh đề 1 của Achiam và cộng sự (2017, (9)), viết cho chiều KL của TRPO. Nó cho thấy bán kính $\kappa$ điều khiển trực tiếp mức giảm tối đa của $J$, với điều kiện bài toán được giải chính xác. Trên Ví dụ 10.12, nếu $\kappa=0{,}004234$, đúng bằng KL trung bình của bước của Ví dụ 10.11, và $\chi=0{,}4$, cận là $-\sqrt{0{,}008468}\cdot0{,}9\cdot0{,}4/0{,}01=-3{,}31$, trùng phạt của Hệ quả 10.27 trên cùng bước.

Giả thiết "nghiệm chính xác" có vai trò quyết định. Bỏ giả thiết này, Bước 1 không còn cho $\mathcal L_{\pi_k}(\pi_{k+1})\ge J(\pi_k)$, và cận không còn áp dụng. Một nhầm lẫn thường gặp là áp hệ quả cho TRPO như được cài đặt: TRPO thực hành lấy trung bình đều trên mẫu thay cho $\nu^{\pi_k}$, dùng lợi thế ước lượng, xấp xỉ KL bậc hai và giải gần đúng, nên giả thiết này không thỏa.

**Trong thực hành.** Hệ quả 10.29 và 10.31 giải thích dạng của TRPO: cực đại hóa hàm thay thế ước lượng từ dữ liệu cũ, trong một miền KL trung bình bán kính $\kappa$. Lợi thế, phân bố chiếm dụng và nghiệm của bài toán chỉ có gần đúng với mạng nơ-ron và dữ liệu hữu hạn, nên $\kappa$ được chọn như một siêu tham số.

Như vậy, Bổ đề 10.19 cho đẳng thức chính xác của $J(\pi')-J(\pi)$ theo quỹ đạo của $\pi'$, Mệnh đề 10.22 cho một hàm thay thế tính được từ dữ liệu của $\pi$ và khớp $J$ đến bậc một, và Định lý 10.26 cùng Hệ quả 10.27 chặn sai số của hàm thay thế bằng khoảng cách TV hoặc KL trung bình giữa hai chính sách. Hệ quả 10.29 suy ra một thuật toán cải thiện đơn điệu nhưng gần như không bước, còn bài toán miền tin cậy của Định nghĩa 10.30 cho bước lớn với mức giảm tối đa bị chặn (Hệ quả 10.31). Bài toán đó vẫn là một bài toán tối ưu phi tuyến có ràng buộc trên $\theta$, chưa có cách giải. Trong Mục 5, chúng ta giải xấp xỉ bài toán này.

*Nguồn: bài giảng gốc lecture10_policy_gradient_part2.pdf (2025–2026), trang 4, 14–16; Kakade và Langford (2002), Bổ đề 6.1; Schulman và cộng sự (2015), §2–4, Định lý 1, Phụ lục A–B; Achiam và cộng sự (2017), Định lý 1, Hệ quả 1, 3, Mệnh đề 1, Bổ đề 3; Cover và Thomas (2006), Bổ đề 11.6.1; Hunter và Lange (2004).*

---

## 5. TRPO và gradient tự nhiên

Trên chuỗi hai trạng thái, ràng buộc của Định nghĩa 10.30 là $0{,}1\,D_{\mathrm{KL}}(s_A)+0{,}045\,D_{\mathrm{KL}}(s_B)\le\kappa$, với KL theo chiều cũ‖mới là một hàm phi tuyến của $(\theta_A;\,\theta_B)$; trong bài toán tổng quát, $\theta\in\mathbb R^d$ với $d$ lớn, và cả hàm mục tiêu lẫn ràng buộc chỉ ước lượng được từ mẫu. Gần $\theta_{\mathrm{old}}$, Mệnh đề 10.22 cho hàm thay thế một xấp xỉ bậc một, $\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}}+\Delta)\approx J(\theta_{\mathrm{old}})+g^\top\Delta$ với $g=\nabla_\theta J(\theta_{\mathrm{old}})$. Chúng ta cần thêm một xấp xỉ của ràng buộc KL theo bước $\Delta$, rồi giải bài toán xấp xỉ một cách hiệu quả khi $d$ lớn.

<!-- note-topic-id: lec-10-topic-15 -->
### 5.1 KL bậc hai và gradient tự nhiên

Về mặt ý tưởng, độ dài của một bước cập nhật cần được đo bằng mức thay đổi của phân phối hành động mà bước đó gây ra, vì ràng buộc của bài toán miền tin cậy là một ràng buộc trên KL. Ví dụ sau cho thấy vì sao ràng buộc đó không thể là một quả cầu Euclid trong không gian tham số.

::: example Ví dụ 10.13 (Cùng một bước tham số, hai khoảng cách chính sách)
**Dữ kiện.** Một trạng thái, hai hành động, chính sách chọn hành động 1 với xác suất $p=\sigma(\theta)$, $\theta\in\mathbb R$. Bước cập nhật tăng $\theta$ thêm $1$. Hai điểm xuất phát: $p=0{,}5$ và $p=0{,}99$.

**Tại $p=0{,}5$.** $\theta=0$, $p'=\sigma(1)=0{,}7311$, và $D_{\mathrm{KL}}(\text{cũ}\Vert\text{mới})=0{,}5\log\frac{0{,}5}{0{,}7311}+0{,}5\log\frac{0{,}5}{0{,}2689}=0{,}1201$.

**Tại $p=0{,}99$.** $\theta=\log99$, $p'=\sigma(\log99+1)=0{,}99630$, và $D_{\mathrm{KL}}(\text{cũ}\Vert\text{mới})=0{,}00366$.

**Diễn giải.** Cùng một bước Euclid trên tham số đổi chính sách theo KL nhiều gấp khoảng $33$ lần ở điểm thứ nhất so với điểm thứ hai. Khoảng cách Euclid giữa hai tham số không đo được mức thay đổi của chính sách.

**Kiểm tra lại.** Tại $p=0{,}5$, hai số hạng của KL là $0{,}5\log\frac{0{,}5}{0{,}7311}=-0{,}1899$ và $0{,}5\log\frac{0{,}5}{0{,}2689}=0{,}3101$, tổng $0{,}1201$.
:::

Hai KL của Ví dụ 10.13 khác nhau vì độ cong của KL theo tham số đổi theo điểm xuất phát. Định nghĩa sau đo độ cong đó và gom nó cho mọi trạng thái.

::: definition Định nghĩa 10.32 (Ma trận thông tin Fisher)
Cho chính sách $\pi_{\theta_{\mathrm{old}}}$ trên tập hành động hữu hạn, với hàm điểm $\psi=\psi_{\theta_{\mathrm{old}}}$ và phân bố chiếm dụng $\nu^{\mathrm{old}}$. *Ma trận thông tin Fisher* (Fisher information matrix) trung bình theo $\nu^{\mathrm{old}}$ là
$$\begin{aligned}&F(\theta_{\mathrm{old}})\\&\quad=\mathbb E_{\substack{S\sim\nu^{\mathrm{old}}\\A\sim\pi_{\mathrm{old}}(\cdot\mid S)}}\bigl[\psi_{\theta_{\mathrm{old}}}(S,A)\\&\qquad\quad\times\psi_{\theta_{\mathrm{old}}}(S,A)^\top\bigr]\\&\quad\in\mathbb R^{d\times d}.\end{aligned}$$
Với một trạng thái $s$ cố định, $F_s=\mathbb E_{A\sim\pi_{\mathrm{old}}(\cdot\mid s)}[\psi\psi^\top]$ là ma trận Fisher của phân phối $\pi_{\mathrm{old}}(\cdot\mid s)$, và $F=\sum_s\nu^{\mathrm{old}}(s)F_s$.
:::

$F$ đối xứng và nửa xác định dương, vì $v^\top Fv=\mathbb E[(v^\top\psi)^2]\ge0$ với mọi $v$; nó không nhất thiết xác định dương, vì $v^\top Fv=0$ khi $v^\top\psi=0$ với mọi cặp trạng thái–hành động. Với chính sách Bernoulli logit của Ví dụ 10.13, $\psi=1-p$ với xác suất $p$ và $\psi=-p$ với xác suất $1-p$, nên $F_s=p(1-p)^2+(1-p)p^2=p(1-p)$. Ma trận $F$ đo độ nhạy của phân phối hành động theo tham số; mệnh đề sau cho thấy nó chính là Hessian của KL trung bình tại $\theta_{\mathrm{old}}$, ma trận mà Schulman và cộng sự (2015, Phụ lục C) gọi là ma trận Fisher.

::: proposition Mệnh đề 10.33 (KL trung bình bậc hai)
**Giả thiết.** Tập hành động hữu hạn; $\pi_\theta(a\mid s)>0$ và khả vi liên tục hai lần theo $\theta$ với mọi $s,a$; $\nu^{\mathrm{old}}$ giữ cố định. Đặt $\bar D(\theta)=\sum_{s\in\mathcal S}\nu^{\mathrm{old}}(s)\,D_{\mathrm{KL}}\bigl(\pi_{\mathrm{old}}(\cdot\mid s)\Vert\pi_\theta(\cdot\mid s)\bigr)$.

**Kết luận.** $\bar D(\theta_{\mathrm{old}})=0$, $\nabla\bar D(\theta_{\mathrm{old}})=0$ và $\nabla^2\bar D(\theta_{\mathrm{old}})=F(\theta_{\mathrm{old}})$. Do đó
$$\begin{aligned}&\bar D(\theta_{\mathrm{old}}+\Delta)\\&\quad=\tfrac12\Delta^\top F\Delta+o(\lVert\Delta\rVert^2).\end{aligned}$$

**Điều kiện áp dụng.** Phân bố trạng thái không đổi theo $\theta$, như trong ràng buộc của Định nghĩa 10.30.

**Phạm vi.** Xấp xỉ địa phương; với bước hữu hạn, KL thật khác dạng bậc hai, như Ví dụ 10.13.
:::

::: proof
**Bước 1 (giá trị).** Tại $\theta=\theta_{\mathrm{old}}$, mỗi $D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid s)\Vert\pi_{\mathrm{old}}(\cdot\mid s))=0$ theo Mệnh đề 10.24(a).

**Bước 2 (gradient).** Viết $\bar D(\theta)=\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)\bigl[\log\pi_{\mathrm{old}}(a\mid s)-\log\pi_\theta(a\mid s)\bigr]$. Số hạng thứ nhất không phụ thuộc $\theta$, nên
$$
\begin{aligned}
&\nabla\bar D(\theta_{\mathrm{old}})\\
&\quad=-\sum_s\nu^{\mathrm{old}}(s)\\
&\qquad\times\sum_a\pi_{\mathrm{old}}(a\mid s)\,\psi_{\theta_{\mathrm{old}}}(s,a)\\
&\quad=-\sum_s\nu^{\mathrm{old}}(s)\\
&\qquad\times\nabla_\theta\Bigl(\sum_a\pi_\theta(a\mid s)\Bigr)\Big|_{\theta_{\mathrm{old}}}\\
&\quad=0,
\end{aligned}
$$
trong đó đẳng thức thứ hai dùng $\pi_\theta\psi_\theta=\nabla_\theta\pi_\theta$ tại $\theta_{\mathrm{old}}$ và đổi gradient với tổng hữu hạn, đẳng thức thứ ba dùng $\sum_a\pi_\theta(a\mid s)=1$.

**Bước 3 (Hessian).** Lấy đạo hàm $\psi_\theta=\nabla\pi_\theta/\pi_\theta$ thêm một lần: $\nabla^2\log\pi_\theta=\nabla^2\pi_\theta/\pi_\theta-\psi_\theta\psi_\theta^\top$. Do đó
$$
\begin{aligned}
&\nabla^2\bar D(\theta_{\mathrm{old}})\\
&=-\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)\\
&\quad\times\Bigl(\frac{\nabla^2\pi_\theta(a\mid s)}{\pi_{\mathrm{old}}(a\mid s)}\\
&\qquad-\psi\psi^\top\Bigr)\Big|_{\theta_{\mathrm{old}}}\\
&=-\sum_s\nu^{\mathrm{old}}(s)\\
&\quad\times\nabla^2\Bigl(\sum_a\pi_\theta(a\mid s)\Bigr)\Big|_{\theta_{\mathrm{old}}}\\
&\quad+\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)\\
&\qquad\times\psi\psi^\top\\
&=0+F(\theta_{\mathrm{old}}),
\end{aligned}
$$
vì $\nabla^2$ của hằng $1$ bằng $0$, và tổng còn lại là Định nghĩa 10.32.

**Bước 4 (khai triển Taylor).** $\bar D$ khả vi liên tục hai lần, nên khai triển Taylor bậc hai tại $\theta_{\mathrm{old}}$ cùng Bước 1–3 cho $\bar D(\theta_{\mathrm{old}}+\Delta)=0+0^\top\Delta+\tfrac12\Delta^\top F\Delta+o(\lVert\Delta\rVert^2)$. $\square$
:::

Mệnh đề nói rằng, quanh chính sách cũ, KL trung bình là một dạng toàn phương của bước với ma trận $F$: miền tin cậy KL gần đúng là một elip mà hình dạng do $F$ quyết định, không phải một quả cầu. Ở Ví dụ 10.13, $F=p(1-p)$ bằng $0{,}25$ tại $p=0{,}5$ và $0{,}0099$ tại $p=0{,}99$, nên xấp xỉ bậc hai $\tfrac12p(1-p)\cdot1^2$ là $0{,}125$ và $0{,}00495$, cùng bậc độ lớn với KL thật $0{,}1201$ và $0{,}00366$; với bước dài $1$ trên logit, số hạng bậc cao đã đáng kể.

Bỏ giả thiết $\pi_\theta>0$ thì Bước 2–3 mất căn cứ, vì $\log\pi_\theta$ và $\psi_\theta$ cần xác định: nếu một xác suất tiến về $0$ trong khi $\pi_{\mathrm{old}}$ của hành động đó dương, KL tiến ra vô cùng và không có khai triển nào. KL theo chiều ngược, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{old}})$, có cùng giá trị, gradient và Hessian tại $\theta_{\mathrm{old}}$, nên ở bậc hai chiều KL không quan trọng.

::: example Ví dụ 10.14 (Ma trận Fisher của bài toán một bước)
**Dữ kiện.** Bài toán một bước: chính sách softmax với $\theta=(\log2;\,0)$, $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$. Đặt $u=(1;\,-1)$, nên $\psi_\theta(s,1)=\tfrac13u$ và $\psi_\theta(s,2)=-\tfrac23u$.

**Ma trận Fisher tại $s$.**
$$\begin{aligned}F_s&=\tfrac23\cdot\tfrac19\,uu^\top+\tfrac13\cdot\tfrac49\,uu^\top\\&=\tfrac29\,uu^\top=\tfrac29\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.\end{aligned}$$

**Suy biến.** $F_s(1;\,1)=0$, nên $F_s$ suy biến với hạt nhân $\operatorname{span}\{(1;\,1)\}$. Cộng cùng một hằng vào hai logit không đổi chính sách softmax, nên hướng $(1;\,1)$ không làm KL thay đổi ở mọi bậc.

**Kiểm tra lại.** Phần tử $(1,1)$: $\tfrac23\cdot\tfrac19+\tfrac13\cdot\tfrac49=\tfrac6{27}=\tfrac29$.
:::

Với xấp xỉ bậc một của hàm thay thế và xấp xỉ bậc hai của KL, bài toán miền tin cậy trở thành bài toán của mệnh đề sau. Schulman và cộng sự (2015, §7, (17)) chỉ ra rằng *gradient chính sách tự nhiên* (natural policy gradient) của Kakade (2002) là đúng trường hợp riêng này của bài toán (12) trong bài báo của họ.

::: proposition Mệnh đề 10.34 (Bước gradient tự nhiên)
**Giả thiết.** $g\in\mathbb R^d$, $g\ne0$; $F\in\mathbb R^{d\times d}$ đối xứng, nửa xác định dương; $\kappa>0$. Xét bài toán
$$\begin{aligned}&\max_{\Delta\in\mathbb R^d}\ g^\top\Delta\\&\text{với ràng buộc}\quad\tfrac12\Delta^\top F\Delta\le\kappa .\end{aligned}$$

**Kết luận.**

- (a) Nếu $F$ xác định dương, bài toán có nghiệm duy nhất $\Delta^*=\sqrt{\dfrac{2\kappa}{g^\top F^{-1}g}}\,F^{-1}g$, với giá trị tối ưu $\sqrt{2\kappa\,g^\top F^{-1}g}$.
- (b) Nếu $F$ suy biến và $g\in\operatorname{range}F$, kết luận (a) đúng khi thay $F^{-1}$ bằng giả nghịch đảo $F^+$, và tập nghiệm là $\Delta^*+\ker F$.
- (c) Nếu $g\notin\operatorname{range}F$, bài toán không bị chặn trên.

**Điều kiện áp dụng.** $g$ và $F$ được tính tại cùng $\theta_{\mathrm{old}}$; $F$ là Hessian của đúng KL được ràng buộc.

**Phạm vi.** Nghiệm của bài toán xấp xỉ; bước $\Delta^*$ có thể vi phạm ràng buộc KL thật và có thể làm hàm thay thế thật giảm.
:::

::: proof
**Bước 1 (tích trong theo $F$).** Khi $F$ xác định dương, $\langle x,y\rangle_F=x^\top Fy$ là một tích trong với chuẩn $\lVert x\rVert_F=\sqrt{x^\top Fx}$, và $g^\top\Delta=(F^{-1}g)^\top F\Delta=\langle F^{-1}g,\Delta\rangle_F$.

**Bước 2 (cận trên, kết luận a).** Với mọi $\Delta$ thỏa ràng buộc,
$$
\begin{aligned}
&g^\top\Delta\\
&=\langle F^{-1}g,\Delta\rangle_F\\
&\le\lVert F^{-1}g\rVert_F\,\lVert\Delta\rVert_F\\
&=\sqrt{g^\top F^{-1}g}\,\sqrt{\Delta^\top F\Delta}\\
&\le\sqrt{g^\top F^{-1}g}\,\sqrt{2\kappa}.
\end{aligned}
$$
Bất đẳng thức thứ nhất là Cauchy–Schwarz, bất đẳng thức thứ hai dùng ràng buộc.

**Bước 3 (đạt cận và duy nhất).** $\Delta^*$ thỏa $\tfrac12\Delta^{*\top}F\Delta^*=\tfrac12\cdot\frac{2\kappa}{g^\top F^{-1}g}\,g^\top F^{-1}g=\kappa$ và $g^\top\Delta^*=\sqrt{2\kappa\,g^\top F^{-1}g}$, nên đạt cận của Bước 2. Ngược lại, một nghiệm phải biến cả hai bất đẳng thức của Bước 2 thành đẳng thức: Cauchy–Schwarz chặt khi và chỉ khi $\Delta=cF^{-1}g$ với $c\ge0$, và ràng buộc chặt cho $c^2g^\top F^{-1}g=2\kappa$; do đó $\Delta=\Delta^*$.

**Bước 4 (kết luận c).** Với $F$ đối xứng, $\operatorname{range}F$ là phần bù trực giao của $\ker F$. Nếu $g\notin\operatorname{range}F$, hình chiếu $n$ của $g$ lên $\ker F$ khác $0$, và $g^\top n=\lVert n\rVert^2>0$. Bước $\Delta=tn$ thỏa ràng buộc với mọi $t>0$, vì $Fn=0$, và $g^\top\Delta=t\lVert n\rVert^2\to\infty$.

**Bước 5 (kết luận b).** Nếu $g\in\operatorname{range}F$ thì $g\perp\ker F$. Tách $\Delta=\Delta_r+\Delta_k$ với $\Delta_r\in\operatorname{range}F$, $\Delta_k\in\ker F$: khi đó $g^\top\Delta=g^\top\Delta_r$ và $\Delta^\top F\Delta=\Delta_r^\top F\Delta_r$. Trên không gian con $\operatorname{range}F$, $F$ xác định dương và $F^+$ là nghịch đảo của nó, nên Bước 1–3 áp dụng cho $\Delta_r$ với $F^{-1}$ thay bằng $F^+$; $\Delta_k$ tùy ý. $\square$
:::

Mệnh đề nói rằng bước tối ưu đi theo hướng $F^{-1}g$, gọi là *gradient tự nhiên* (natural gradient), với độ dài chọn sao cho KL bậc hai đúng bằng $\kappa$. Gradient thường $g$ là hướng tăng nhanh nhất khi đo bước bằng chuẩn Euclid; $F^{-1}g$ là hướng tăng nhanh nhất khi đo bằng $\lVert\cdot\rVert_F$, tức bằng KL bậc hai.

Nhân $g$ với một hằng dương không đổi $\Delta^*$, nên các thừa số như $1/(1-\gamma)$ trong hàm thay thế không ảnh hưởng; chỉ thang của $F$, tức KL nào bị ràng buộc, quyết định độ dài bước.

Giả thiết $g\in\operatorname{range}F$ của (b) luôn thỏa khi $g$ và $F$ được tính với cùng phân bố của $(S,A)$. Thật vậy, $F=\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)\,\psi(s,a)\psi(s,a)^\top$ với trọng số dương trên miền $\nu^{\mathrm{old}}(s)\pi_{\mathrm{old}}(a\mid s)>0$, nên $\operatorname{range}F$ là không gian sinh bởi các hàm điểm $\psi(s,a)$ trên miền đó. Gradient $g=\tfrac1{1-\gamma}\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)A_{\mathrm{old}}(s,a)\psi(s,a)$ là một tổ hợp tuyến tính của chính các véc-tơ đó. Trường hợp (c) có thể xảy ra khi $g$ và $F$ lấy trên hai tập trạng thái khác nhau.

::: example Ví dụ 10.15 (Bước gradient tự nhiên trên bài toán một bước)
**Dữ kiện.** Bài toán một bước của Ví dụ 10.14: $r=(3;\,0)$, $\theta=(\log2;\,0)$, $g=\nabla_\theta J=(\tfrac23;\,-\tfrac23)=\tfrac23u$ với $u=(1;\,-1)$, $F_s=\tfrac29uu^\top$. Ràng buộc là KL tại chính trạng thái $s$, $\tfrac12\Delta^\top F_s\Delta\le\kappa$, với $\kappa=0{,}01$.

**Giả nghịch đảo.** $u^\top u=2$, nên $(uu^\top)^+=uu^\top/4$ và $F_s^+=\tfrac92\cdot\tfrac14uu^\top=\tfrac98uu^\top$. Kiểm giả thiết: $g\perp(1;\,1)$, nên $g\in\operatorname{range}F_s$.

**Hướng và độ dài.** $F_s^+g=\tfrac98\cdot\tfrac23\cdot2\,u=(1{,}5;\,-1{,}5)$ và $g^\top F_s^+g=\tfrac23\cdot1{,}5\cdot2=2$. Hệ số độ dài là $\sqrt{2\cdot0{,}01/2}=0{,}1$, nên $\Delta^*=(0{,}15;\,-0{,}15)$.

**Chính sách mới.** $\theta=(\log2+0{,}15;\,-0{,}15)$, $p_1=2/(2+e^{-0{,}3})=0{,}7297$, và $J=3p_1=2{,}189$, tăng từ $2$. KL thật theo chiều cũ‖mới là $0{,}009644$ và theo chiều mới‖cũ là $0{,}009269$, so với giá trị bậc hai $\kappa=0{,}01$.

**Kiểm tra lại.** $\tfrac12\Delta^{*\top}F_s\Delta^*=\tfrac12\cdot\tfrac29\cdot(0{,}3)^2=0{,}01$. Mọi $\Delta^*+c(1;\,1)$ cho cùng chính sách, đúng như tập nghiệm của Mệnh đề 10.34(b).
:::

Trong Ví dụ 10.15, chỉ có một trạng thái, nên $F=\nu^{\mathrm{old}}(s)F_s$ và ràng buộc trên KL trung bình chỉ khác ràng buộc tại $s$ một hằng số; ví dụ dùng ràng buộc tại $s$ để $\kappa$ có nghĩa KL của chính sách tại trạng thái đó.

::: remark Nhận xét 10.35 (Ma trận Fisher suy biến)
Với chính sách softmax, mỗi trạng thái đóng góp vào $\ker F$ hướng cộng cùng một hằng vào mọi logit của trạng thái đó; khi các trạng thái có tham số chung, hạt nhân có thể nhỏ hơn. Giả nghịch đảo chọn nghiệm có chuẩn nhỏ nhất trong $\Delta^*+\ker F$. Mọi nghiệm cho cùng giá trị của mô hình bậc hai; với softmax có tham số riêng cho từng trạng thái, các nghiệm cho đúng cùng một chính sách trên các trạng thái có $\nu^{\mathrm{old}}(s)>0$.
:::

**Trong thực hành.** Khi $g$ và $F$ được ước lượng bằng trung bình đều trên cùng một bộ đệm, tại cùng $\theta_{\mathrm{old}}$, lập luận sau Mệnh đề 10.34 cho $g\in\operatorname{range}F$.

<!-- note-topic-id: lec-10-topic-16 -->
### 5.2 TRPO thực hành

Với mạng nơ-ron, $d$ có thể lên tới hàng triệu, nên lập ma trận $F\in\mathbb R^{d\times d}$ cần $O(d^2)$ bộ nhớ và nghịch đảo nó cần $O(d^3)$ phép tính; Schulman và cộng sự (2015, Phụ lục C) mô tả chi phí này là quá đắt (prohibitively costly) về tính toán và bộ nhớ. Hệ phương trình $Fx=g$ vẫn giải gần đúng được nếu chỉ tính được tích $v\mapsto Fv$.

Phương pháp *gradient liên hợp* (conjugate gradient) làm đúng việc đó: nó cực tiểu hóa mô hình bậc hai $\tfrac12x^\top Fx-g^\top x$, có gradient $Fx-g$ triệt tiêu đúng tại nghiệm của $Fx=g$.

Hai hướng $p$, $p'$ gọi là *liên hợp* (conjugate) đối với $F$ nếu $p^\top Fp'=0$. Về mặt ý tưởng, phương pháp cực tiểu hóa mô hình lần lượt theo các hướng đôi một liên hợp, nên bước theo hướng sau không làm hỏng phần cực tiểu đã đạt theo các hướng trước. Ví dụ sau chạy hai vòng.

::: example Ví dụ 10.16 (Hai vòng gradient liên hợp)
**Dữ kiện.** $F=\operatorname{diag}(4;\,1)$, $g=(2;\,1)$, điểm xuất phát $x_0=0$, $\kappa=0{,}01$. Quy ước của Nocedal và Wright (2006, Thuật toán 5.2): $\tilde g_k=Fx_k-g$ là gradient của mô hình $\tfrac12x^\top Fx-g^\top x$ tại $x_k$; hướng đầu $p_0=-\tilde g_0$; độ dài bước $\omega_k=\tilde g_k^\top\tilde g_k/(p_k^\top Fp_k)$; hệ số liên hợp $\xi_{k+1}=\tilde g_{k+1}^\top\tilde g_{k+1}/(\tilde g_k^\top\tilde g_k)$. Ba công thức cập nhật là
$$
\begin{aligned}
x_{k+1}&=x_k+\omega_kp_k,\\
\tilde g_{k+1}&=\tilde g_k+\omega_kFp_k,\\
p_{k+1}&=-\tilde g_{k+1}+\xi_{k+1}p_k.
\end{aligned}
$$

**Vòng $0$.** $\tilde g_0=-g=(-2;\,-1)$, $p_0=(2;\,1)$, $Fp_0=(8;\,1)$, $\omega_0=5/17$. Khi đó $x_1=x_0+\omega_0p_0=(\tfrac{10}{17};\,\tfrac5{17})$ và $\tilde g_1=\tilde g_0+\omega_0Fp_0=(\tfrac6{17};\,-\tfrac{12}{17})$.

**Vòng $1$.** $\xi_1=\frac{180/289}{5}=\tfrac{36}{289}$, $p_1=-\tilde g_1+\xi_1p_0=(-\tfrac{30}{289};\,\tfrac{240}{289})$, $\omega_1=\frac{180/289}{61\,200/289^2}=0{,}85$. Khi đó $x_2=x_1+0{,}85\,p_1=(0{,}5;\,1)$ và $\tilde g_2=0$: thuật toán dừng.

**Bước miền tin cậy.** $x_2^\top Fx_2=x_2^\top g=2$, nên hệ số độ dài là $\sqrt{2\kappa/2}=0{,}1$ và $\Delta=(0{,}05;\,0{,}1)$.

**Kiểm tra lại.** $Fx_2=(4\cdot0{,}5;\,1\cdot1)=g$, và $\tfrac12\Delta^\top F\Delta=\tfrac12(4\cdot0{,}0025+0{,}01)=0{,}01=\kappa$. Hai hướng liên hợp: $p_0^\top Fp_1=\tfrac{1}{289}(8\cdot(-30)+1\cdot240)=0$.
:::

![Mặt phẳng tọa độ của bước Delta. Elip tâm gốc tọa độ, phương trình một nửa Delta chuyển vị F Delta bằng 0,01 với F bằng diag(4; 1), bán trục 0,0707 theo trục thứ nhất và 0,1414 theo trục thứ hai. Mũi tên nét liền từ gốc theo hướng gradient g bằng (2; 1). Mũi tên nét đứt từ gốc tới điểm (0,05; 0,1) trên biên elip, ghi bước gradient tự nhiên F mũ trừ 1 g nhân 0,1. Hai mũi tên lệch hướng nhau.](img/lec-10/trpo-trust-region.svg)

Trên hình là miền tin cậy bậc hai của Ví dụ 10.16. Elip hẹp theo trục thứ nhất, nơi $F$ lớn, tức nơi một bước nhỏ đã đổi chính sách nhiều. Gradient $g=(2;\,1)$ nghiêng về trục thứ nhất, còn bước tối ưu $(0{,}05;\,0{,}1)$ nghiêng về trục thứ hai, nơi elip rộng.

Trên chuỗi hai trạng thái, $\nu^{\mathrm{old}}=(0{,}1;\,0{,}045)$, $p_A(1-p_A)=\tfrac14$ và $p_B(1-p_B)=\tfrac29$ cho $F=\operatorname{diag}(0{,}025;\,0{,}01)$; cùng $g=(0{,}2;\,0{,}3)$ của Ví dụ 10.6, $F^{-1}g=(8;\,30)$. Gradient tự nhiên dồn bước về $\theta_B$, vì $s_B$ ít được thăm nên đổi $\theta_B$ ít làm đổi KL trung bình.

::: algorithm Thuật toán 10.36 (Gradient liên hợp với tích Fisher–vector)
**Đầu vào.** Hàm $v\mapsto Fv$; véc-tơ $g$; số vòng tối đa $k_{\max}$; ngưỡng $\varepsilon_{\mathrm{cg}}>0$.

**Đầu ra.** Nghiệm gần đúng $x\approx F^{-1}g$ và số $\tau\approx x^\top Fx$.

**Giả thiết.** $F$ đối xứng, nửa xác định dương; $g\in\operatorname{range}F$, được bảo đảm khi $g$ và $F$ tính trên cùng các trạng thái.

**Khởi tạo.** $x_0=0$, $\tilde g_0=-g$, $p_0=g$, $\tau_0=0$.

**Với $k=0,1,\dots,k_{\max}-1$:**

1. $y_k=Fp_k$; $\omega_k=\tilde g_k^\top\tilde g_k/(p_k^\top y_k)$.
2. $x_{k+1}=x_k+\omega_kp_k$; $\tilde g_{k+1}=\tilde g_k+\omega_ky_k$; $\tau_{k+1}=\tau_k+\omega_k\,\tilde g_k^\top\tilde g_k$.
3. Nếu $\lVert\tilde g_{k+1}\rVert\le\varepsilon_{\mathrm{cg}}$, dừng.
4. $\xi_{k+1}=\tilde g_{k+1}^\top\tilde g_{k+1}/(\tilde g_k^\top\tilde g_k)$; $p_{k+1}=-\tilde g_{k+1}+\xi_{k+1}p_k$.

**Tích Fisher–vector.** $Fv=\nabla_\theta\bigl((\nabla_\theta\widehat D(\theta))^\top v\bigr)\big|_{\theta_{\mathrm{old}}}$, với $\widehat D$ là KL trung bình trên một tập con của dữ liệu; theo Mệnh đề 10.33, đây là tích Hessian–vector của KL tại $\theta_{\mathrm{old}}$, tính bằng hai lần vi phân tự động mà không lập $F$.

**Điều kiện dừng.** Sau $k_{\max}$ vòng hoặc khi phần dư nhỏ hơn ngưỡng; trả về $x=x_{k+1}$ và $\tau=\tau_{k+1}$ của vòng cuối.

**Chi phí mỗi vòng.** Một tích $Fv$, cỡ một lần tính gradient, cộng $O(d)$ phép tính véc-tơ.
:::

Thuật toán là Thuật toán 5.2 của Nocedal và Wright (2006, tr. 112) với ký hiệu của chương: $\tilde g_k$, $\omega_k$, $\xi_k$ thay cho $r_k$, $\alpha_k$, $\beta_k$ của sách, vì $r$, $\alpha$, $\beta$ đã có nghĩa khác trong chương. Với $F$ xác định dương và số học chính xác, thuật toán cho nghiệm đúng sau không quá $d$ vòng (Nocedal và Wright, 2006, Định lý 5.1, tr. 103). Nếu $F$ có $r$ giá trị riêng phân biệt, số vòng không quá $r$ (Định lý 5.4, tr. 115 của cùng sách); $F=\operatorname{diag}(4;\,1)$ có hai giá trị riêng nên Ví dụ 10.16 dừng sau hai vòng.

Số $\tau$ bằng $x^\top Fx$ trong số học chính xác: $x_K=\sum_{k<K}\omega_kp_k$, các hướng liên hợp nên $x_K^\top Fx_K=\sum_{k<K}\omega_k^2\,p_k^\top Fp_k$, và $\omega_k\,p_k^\top Fp_k=\tilde g_k^\top\tilde g_k$. Trên Ví dụ 10.16, $\tau_2=\tfrac5{17}\cdot5+0{,}85\cdot\tfrac{180}{289}=1{,}4706+0{,}5294=2=x_2^\top Fx_2$. Schulman và cộng sự (2015, Phụ lục C, C.1) dùng $k_{\max}=10$ vòng và tính tích Fisher–vector trên khoảng $10\%$ dữ liệu, để tổng chi phí các tích này xấp xỉ chi phí một lần tính gradient. Khi tích $Fv$ tính trên một tập con như vậy, $F$ chỉ sinh từ hàm điểm tại các trạng thái của tập con, và với $d$ lớn hơn nhiều số mẫu, $g$ nói chung không nằm trong $\operatorname{range}F$: giả thiết của Thuật toán 10.36 không được bảo đảm, nghiệm sau $k_{\max}$ vòng chỉ là một hướng gần đúng, và tìm kiếm lùi của Thuật toán 10.37 kiểm lại KL và hàm thay thế trước khi nhận bước.

::: algorithm Thuật toán 10.37 (TRPO với lợi thế GAE)
**Đầu vào.** Chính sách $\pi_\theta$, critic $\hat v(s,w)$; bán kính $\kappa>0$; hệ số co $\zeta\in(0,1)$ và số lần co tối đa $j_{\max}$; số môi trường $N$, độ dài đoạn $h$; $\gamma$, $\lambda$; tham số của Thuật toán 10.36.

**Đầu ra.** Tham số $\theta$, $w$ sau số vòng lặp đã định.

**Giả thiết.** Chính sách khả vi hai lần, $\pi_\theta>0$; dữ liệu mỗi vòng do $\pi_{\mathrm{old}}$ sinh ra.

**Mỗi vòng lặp:**

1. $\theta_{\mathrm{old}}\leftarrow\theta$, $w_{\mathrm{old}}\leftarrow w$. Thu $h$ bước trên mỗi môi trường bằng $\pi_{\mathrm{old}}$, lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$; bộ đệm $\mathcal D$ gồm $hN$ mẫu.
2. Tính $\widehat A_t$ và $V^{\mathrm{targ}}_t$ bằng Thuật toán 10.16.
3. Với $\widehat{\mathcal L}(\theta)=\widehat{\mathbb E}_{\mathcal D}[\rho_t(\theta)\widehat A_t]$ và $\widehat D(\theta)=\widehat{\mathbb E}_{\mathcal D}\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid S_t)\Vert\pi_\theta(\cdot\mid S_t))\bigr]$, tính $g=\nabla\widehat{\mathcal L}(\theta_{\mathrm{old}})=\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$.
4. Giải $Fx=g$ gần đúng bằng Thuật toán 10.36, với $F$ là Hessian của $\widehat D$ tại $\theta_{\mathrm{old}}$.
5. Bước đầy đủ: $\Delta_0=\sqrt{2\kappa/(x^\top Fx)}\;x$.
6. *Tìm kiếm lùi*: với $j=0,1,\dots,j_{\max}$, đặt $\theta=\theta_{\mathrm{old}}+\zeta^j\Delta_0$ và nhận giá trị $j$ đầu tiên thỏa $\widehat{\mathcal L}(\theta)>\widehat{\mathcal L}(\theta_{\mathrm{old}})$ và $\widehat D(\theta)\le\kappa$; nếu không có $j$ nào, giữ $\theta=\theta_{\mathrm{old}}$.
7. Cập nhật critic: vài bước hạ gradient trên $\widehat{\mathbb E}_{\mathcal D}\bigl[(\hat v(S_t,w)-V^{\mathrm{targ}}_t)^2\bigr]$.

**Điều kiện dừng.** Sau số vòng lặp hoặc số bước môi trường đã định.

**Chi phí mỗi vòng lặp.** $hN$ bước môi trường; một gradient; $k_{\max}$ tích Fisher–vector; tối đa $j_{\max}+1$ lần tính $\widehat{\mathcal L}$ và $\widehat D$ trên dữ liệu.
:::

Bước 5 là công thức hệ số độ dài của Schulman và cộng sự (2015, Phụ lục C): với $x\approx F^{-1}g$, bước $\sqrt{2\kappa/(x^\top Fx)}\,x$ là $\Delta^*$ của Mệnh đề 10.34, và $x^\top Fx$ là số $\tau$ của Thuật toán 10.36. Ví dụ 10.16 thực hiện bước 4–5 bằng tay; Ví dụ 10.15 cho thấy một bước như vậy làm $J$ tăng từ $2$ lên $2{,}189$ với KL thật $0{,}009644\le\kappa$, nên bước 6 nhận ngay $j=0$.

Các thành phần của thuật toán đến từ hai nguồn. Bài báo TRPO gốc (Schulman và cộng sự, 2015, §5) ước lượng $Q_{\theta_{\mathrm{old}}}$ bằng lợi tức Monte Carlo theo hai sơ đồ thu dữ liệu, single path và vine, và không dùng critic; bước 3–6 theo bài báo này. Bước 2 và bước 7, lợi thế GAE với một critic học bằng hồi quy, theo cách Schulman và cộng sự (2016) ghép TRPO với GAE, cũng là cách bài giảng gốc (tr. 18) mô tả TRPO. Bài báo đó khớp critic bằng hồi quy có ràng buộc miền tin cậy, giải bằng gradient liên hợp (§5); bước 7 ở đây dùng vài bước hạ gradient trên cùng mất mát bình phương.

**Trong thực hành.** Chính sách và critic là hai mạng riêng; $g$ và các tích Fisher–vector được tính bằng vi phân tự động trên bộ đệm, không lập ma trận nào cỡ $d\times d$. Bước 6 cần thiết vì hàm thay thế và KL thật là phi tuyến: bài báo co bước theo cấp số nhân (shrink exponentially) tới khi hàm thay thế tăng và ràng buộc KL thỏa. Nhận xét sau liệt kê các giả thiết của lý thuyết mà thuật toán vi phạm.

::: remark Nhận xét 10.38 (Những gì TRPO thực hành mất so với Định lý 10.26)
So với các giả thiết của Định lý 10.26 và Hệ quả 10.29, Thuật toán 10.37 thay đổi năm điểm:

- trung bình đều trên bộ đệm thay cho kỳ vọng theo $\nu^{\mathrm{old}}$ có chiết khấu;
- lợi thế ước lượng bằng GAE thay cho $A_{\mathrm{old}}$ chính xác;
- hàm thay thế bậc một và KL bậc hai thay cho hai hàm thật;
- gradient liên hợp dừng sau $k_{\max}$ vòng, cho nghiệm gần đúng;
- ràng buộc KL trung bình thay cho phạt TV với hằng của lý thuyết.

Điều còn lại sau tìm kiếm lùi là hai bất đẳng thức trên chính bộ đệm: KL trung bình mẫu không vượt $\kappa$, và hàm thay thế mẫu tăng.
:::

Như vậy, Mệnh đề 10.33 đưa ràng buộc KL về dạng toàn phương với ma trận Fisher, Mệnh đề 10.34 giải bài toán xấp xỉ bằng bước gradient tự nhiên, và Thuật toán 10.36–10.37 tính bước đó bằng gradient liên hợp và tìm kiếm lùi mà không lập $F$. Cái giá là mỗi vòng lặp cần khoảng mười tích Fisher–vector, một lượt tìm kiếm lùi và một bộ máy bậc hai riêng cho chính sách; Schulman và cộng sự (2017, §1) nêu thêm rằng TRPO tương đối phức tạp và không tương thích với kiến trúc có nhiễu, như dropout, hoặc dùng chung tham số giữa chính sách và hàm giá trị. Trong Mục 6, chúng ta đưa giới hạn khoảng cách vào chính hàm mục tiêu.

*Nguồn: bài giảng gốc lecture10_policy_gradient_part2.pdf (2025–2026), trang 17–19; Schulman và cộng sự (2015), §5–7, Phụ lục C, C.1; Schulman và cộng sự (2016), §5–6; Kakade (2002), theo Schulman và cộng sự (2015); Nocedal và Wright (2006), Chương 5.*

---

## 6. Tối ưu chính sách gần kề (PPO)

Trên bài toán một bước, bước TRPO của Ví dụ 10.15 đã cần giả nghịch đảo của ma trận Fisher và một phép kiểm KL thật. Schulman và cộng sự (2017, §1, §3) đặt mục tiêu giữ ý "không đi quá xa chính sách cũ" nhưng chỉ dùng tối ưu bậc một: viết một hàm mục tiêu mà cực đại hóa nó bằng vài epoch SGD hoặc Adam trên mini-batch không tạo động lực đẩy tỉ số chính sách ra xa $1$ (bài giảng gốc, tr. 19–20). Chúng ta xây hàm mục tiêu đó, một biến thể phạt KL, thuật toán đầy đủ kiểu actor–critic, cách đọc các đại lượng chẩn đoán, vai trò của chi tiết cài đặt và phạm vi của kết quả lý thuyết hiện có.

<!-- note-topic-id: lec-10-topic-17 -->
### 6.1 PPO-Clip

Hàm thay thế mẫu $\widehat{\mathbb E}_{\mathcal D}[\rho_t(\theta)\widehat A_t]$ tăng tuyến tính theo tỉ số: với lợi thế dương, đẩy $\rho_t$ lên mãi luôn làm nó tăng, dù chính sách mới đã rời xa vùng mà Mệnh đề 10.22 bảo đảm khớp. Về mặt ý tưởng, ta cắt phần thưởng của việc đẩy tỉ số ra ngoài một khoảng $[1-\epsilon,1+\epsilon]$, nhưng giữ nguyên phần phạt khi tỉ số đi theo hướng bất lợi. Ví dụ sau so hai mục tiêu trên bài toán một bước.

::: example Ví dụ 10.17 (Hai hàm thay thế mẫu trên bài toán một bước)
**Dữ kiện.** Bài toán một bước với chính sách cũ $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$. Bộ đệm ba mẫu, hành động $1,1,2$, đúng tần suất của $\pi_{\mathrm{old}}$, với lợi thế $\widehat A=(1;\,1;\,-2)$, là lợi thế đúng của Ví dụ 10.5. *Bán kính cắt* $\epsilon=0{,}2$. Chính sách mới chọn hành động 1 với xác suất $p$, nên $\rho(1)=p/\tfrac23=1{,}5p$ và $\rho(2)=(1-p)/\tfrac13=3(1-p)$.

**Mục tiêu không cắt.** $\mathcal L^{\mathrm{CPI}}(p)=\tfrac13\bigl[1{,}5p+1{,}5p-2\cdot3(1-p)\bigr]=3p-2$. Ở đây $\mathcal L^{\mathrm{CPI}}$ bằng đúng $J(p)-J_{\mathrm{old}}=3p-2$, vì chỉ có một bước và tần suất mẫu trùng $\pi_{\mathrm{old}}$.

**Mục tiêu cắt.** Hai mẫu hành động 1 có lợi thế dương nên bị chặn trên ở $\rho=1{,}2$, tức $p=0{,}8$; mẫu hành động 2 có lợi thế âm nên bị chặn dưới ở $\rho=0{,}8$, tức $p=0{,}7\overline3$. Do đó

- khi $p\le0{,}7\overline3$: $\mathcal L^{\mathrm{CLIP}}(p)=3p-2$;
- khi $0{,}7\overline3<p\le0{,}8$: $\mathcal L^{\mathrm{CLIP}}(p)=\tfrac13(3p-1{,}6)=p-0{,}5\overline3$;
- khi $p\ge0{,}8$: $\mathcal L^{\mathrm{CLIP}}(p)=\tfrac13(2{,}4-1{,}6)=0{,}2\overline6$.


**Diễn giải.** Hai mục tiêu trùng nhau tới $p=0{,}7\overline3$; sau đó mục tiêu cắt tăng chậm hơn, và từ $p=0{,}8$ nó hằng, nên gradient bằng $0$ và không còn động lực tăng $p$.

**Kiểm tra lại.** Tại $p=0{,}75$: $\mathcal L^{\mathrm{CLIP}}=0{,}2167$ và $\mathcal L^{\mathrm{CPI}}=0{,}25$. Tại $p=0{,}7\overline3$, cả hai khúc đầu bằng $0{,}2$, nên $\mathcal L^{\mathrm{CLIP}}$ liên tục.
:::

![Đồ thị theo p từ 0,5 đến 0,9. Đường thẳng nét đứt: L CPI bằng 3p trừ 2. Đường gấp khúc nét liền: L CLIP, trùng 3p trừ 2 tới p bằng 0,733, sau đó bằng p trừ 0,533 tới p bằng 0,8, rồi nằm ngang ở 0,267. Hai đường thẳng đứng mảnh đánh dấu p bằng 0,733 (mẫu hành động 2 chạm rho bằng 0,8) và p bằng 0,8 (mẫu hành động 1 chạm rho bằng 1,2). Điểm p bằng 2/3 ghi chính sách cũ, nơi hai đường trùng nhau.](img/lec-10/ppo-one-step-plateau.svg)

Trên hình, đường gấp khúc nằm dưới đường thẳng ở mọi $p$, trùng nó quanh chính sách cũ $p=\tfrac23$, và trở nên nằm ngang từ $p=0{,}8$. Hai mốc gấp ứng với hai lúc một nhóm mẫu chạm biên của khoảng cắt. Định nghĩa sau viết mục tiêu cắt cho bộ đệm tổng quát.

::: definition Định nghĩa 10.39 (Mục tiêu PPO-Clip)
Cho bộ đệm $\mathcal D$ các mẫu $(S_t,A_t,\widehat A_t)$ do $\pi_{\mathrm{old}}$ sinh ra, tỉ số $\rho_t(\theta)$ của Định nghĩa 10.21 và bán kính cắt $\epsilon\in(0,1)$. Với $\operatorname{clip}(x,l,u)=\min(\max(x,l),u)$, số hạng cắt của mẫu $t$ là
$$\begin{aligned}&\ell^{\mathrm{CLIP}}_t(\theta)\\&=\min\bigl(\rho_t(\theta)\widehat A_t,\\&\quad\operatorname{clip}(\rho_t(\theta),1-\epsilon,1+\epsilon)\,\widehat A_t\bigr).\end{aligned}$$
*Mục tiêu PPO-Clip* và *mục tiêu không cắt* là
$$\begin{aligned}\mathcal L^{\mathrm{CLIP}}(\theta)&=\widehat{\mathbb E}_{\mathcal D}\bigl[\ell^{\mathrm{CLIP}}_t(\theta)\bigr],\\\mathcal L^{\mathrm{CPI}}(\theta)&=\widehat{\mathbb E}_{\mathcal D}\bigl[\rho_t(\theta)\widehat A_t\bigr].\end{aligned}$$
:::

$\mathcal L^{\mathrm{CPI}}$ là hàm thay thế mẫu của Mục 4.2, bỏ hằng $J(\theta_{\mathrm{old}})$; chỉ số CPI theo Schulman và cộng sự (2017, (6)) chỉ *phương pháp lặp chính sách bảo thủ* (conservative policy iteration) của Kakade và Langford (2002). Phép $\min$ lấy giá trị nhỏ hơn giữa mục tiêu không cắt và mục tiêu đã cắt tỉ số; mệnh đề sau viết lại nó theo dấu của lợi thế.

::: proposition Mệnh đề 10.40 (Dạng theo dấu của lợi thế)
**Giả thiết.** $\epsilon\in(0,1)$; $\rho_t(\theta)>0$ khả vi theo $\theta$, với $\nabla_\theta\rho_t=\rho_t\,\psi_\theta(S_t,A_t)$.

**Kết luận.**

- (a) Nếu $\widehat A_t>0$ thì $\ell^{\mathrm{CLIP}}_t=\widehat A_t\min(\rho_t,1+\epsilon)$.
- (b) Nếu $\widehat A_t<0$ thì $\ell^{\mathrm{CLIP}}_t=\widehat A_t\max(\rho_t,1-\epsilon)$.
- (c) Nếu $\widehat A_t=0$ thì $\ell^{\mathrm{CLIP}}_t=0$.
- (d) Gradient của $\ell^{\mathrm{CLIP}}_t$ theo $\theta$ bằng $0$ trên tập $\{\widehat A_t>0,\ \rho_t>1+\epsilon\}\cup\{\widehat A_t<0,\ \rho_t<1-\epsilon\}$, và bằng $\widehat A_t\rho_t\psi_\theta(S_t,A_t)$ trên phần còn lại, trừ các điểm $\rho_t=1\pm\epsilon$, nơi hàm có thể không khả vi.

**Điều kiện áp dụng.** $\widehat A_t$ giữ cố định khi lấy gradient.

**Phạm vi.** Mệnh đề nói về từng mẫu; trên một mini-batch, gradient là trung bình của các gradient mẫu.
:::

::: proof
**Bước 1 (trường hợp a).** Nhân với $\widehat A_t>0$ giữ thứ tự, nên $\ell^{\mathrm{CLIP}}_t=\widehat A_t\min\bigl(\rho_t,\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\bigr)$. Xét ba khoảng:

- $\rho_t<1-\epsilon$: $\operatorname{clip}=1-\epsilon>\rho_t$, nên $\min=\rho_t$;
- $1-\epsilon\le\rho_t\le1+\epsilon$: $\operatorname{clip}=\rho_t$, nên $\min=\rho_t$;
- $\rho_t>1+\epsilon$: $\operatorname{clip}=1+\epsilon<\rho_t$, nên $\min=1+\epsilon$.

Trong cả ba khoảng, $\min=\min(\rho_t,1+\epsilon)$.

**Bước 2 (trường hợp b).** Nhân với $\widehat A_t<0$ đảo thứ tự, nên $\ell^{\mathrm{CLIP}}_t=\widehat A_t\max\bigl(\rho_t,\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\bigr)$; cùng ba khoảng cho $\max=\max(\rho_t,1-\epsilon)$.

**Bước 3 (trường hợp c).** Cả hai đối số của $\min$ bằng $0$.

**Bước 4 (gradient).** Với $\widehat A_t>0$: trên $\{\rho_t<1+\epsilon\}$, $\ell^{\mathrm{CLIP}}_t=\widehat A_t\rho_t$ có gradient $\widehat A_t\nabla\rho_t=\widehat A_t\rho_t\psi_\theta$; trên $\{\rho_t>1+\epsilon\}$, $\ell^{\mathrm{CLIP}}_t=\widehat A_t(1+\epsilon)$ là hằng nên có gradient $0$. Với $\widehat A_t<0$, lập luận đối xứng với $\{\rho_t<1-\epsilon\}$ là tập có gradient $0$. Hai tập này mở theo $\theta$ vì $\rho_t$ liên tục. $\square$
:::

Đọc bằng lời: với lợi thế dương, mục tiêu thưởng cho việc tăng xác suất của hành động chỉ tới khi tỉ số đạt $1+\epsilon$; với lợi thế âm, nó thưởng cho việc giảm xác suất chỉ tới khi tỉ số đạt $1-\epsilon$. Phía bất lợi không bị cắt: một hành động có lợi thế dương mà xác suất đã giảm, $\rho_t<1-\epsilon$, vẫn nhận đủ gradient kéo xác suất trở lại. Nhận xét của bài giảng gốc (tr. 22) rằng một mẫu "ngoài vùng cắt" có gradient bằng $0$ cần đúng điều kiện dấu của kết luận (d). Tại hai điểm gấp, vi phân tự động trả về gradient của một trong hai nhánh.

![Hai khung cạnh nhau, trục hoành rho, epsilon bằng 0,2. Khung trái, A mũ dương: l CLIP bằng A mũ nhân min(rho; 1,2), đường tăng tuyến tính tới rho bằng 1,2 rồi nằm ngang; vùng nằm ngang tô sọc ghi gradient bằng 0. Điểm tròn tại rho bằng 1,3 trên đoạn ngang, giá trị 2,4; điểm vuông tại rho bằng 0,7 trên đoạn dốc, giá trị 1,4. Khung phải, A mũ âm: l CLIP bằng A mũ nhân max(rho; 0,8), đường nằm ngang tới rho bằng 0,8 rồi giảm tuyến tính; vùng nằm ngang tô sọc ghi gradient bằng 0. Điểm tròn tại rho bằng 0,7 trên đoạn ngang, giá trị âm 1,6; điểm vuông tại rho bằng 1,3 trên đoạn dốc, giá trị âm 2,6. Đường nét đứt mảnh ở cả hai khung là A mũ nhân rho.](img/lec-10/ppo-clipping-signs.svg)

Hình trên được vẽ theo Hình 1 của Schulman và cộng sự (2017), với $\epsilon=0{,}2$ và bốn mẫu của ví dụ sau. Vùng tô sọc là tập có gradient bằng $0$ của Mệnh đề 10.40(d), nằm bên phải trong khung lợi thế dương và bên trái trong khung lợi thế âm; điểm tròn nằm trên đoạn phẳng, điểm vuông nằm trên đoạn dốc.

::: example Ví dụ 10.18 (Bốn mẫu)
**Dữ kiện.** $\epsilon=0{,}2$; bốn mẫu $(\widehat A;\,\rho)$: $(2;\,1{,}3)$, $(-2;\,0{,}7)$, $(2;\,0{,}7)$, $(-2;\,1{,}3)$.

**Tính.**

- $(2;\,1{,}3)$: $\min(2{,}6;\,2{,}4)=2{,}4$; lợi thế dương và $\rho>1{,}2$, nên mẫu nằm trên đoạn phẳng, gradient bằng $0$.
- $(-2;\,0{,}7)$: $\min(-1{,}4;\,-1{,}6)=-1{,}6$; lợi thế âm và $\rho<0{,}8$, đoạn phẳng, gradient bằng $0$.
- $(2;\,0{,}7)$: $\min(1{,}4;\,1{,}6)=1{,}4$; phía bất lợi, gradient $2\cdot0{,}7\,\psi\ne0$.
- $(-2;\,1{,}3)$: $\min(-2{,}6;\,-2{,}4)=-2{,}6$; phía bất lợi, gradient $-2\cdot1{,}3\,\psi\ne0$.

**Kiểm tra lại.** Theo dạng theo dấu: $2\min(1{,}3;\,1{,}2)=2{,}4$, $-2\max(0{,}7;\,0{,}8)=-1{,}6$, $2\min(0{,}7;\,1{,}2)=1{,}4$, $-2\max(1{,}3;\,0{,}8)=-2{,}6$.
:::

Mệnh đề sau so mục tiêu cắt với mục tiêu không cắt.

::: proposition Mệnh đề 10.41 (Chặn dưới bi quan và khớp tại $\theta_{\mathrm{old}}$)
**Giả thiết.** Như Mệnh đề 10.40; bộ đệm hữu hạn; $\pi_{\mathrm{old}}(A_t\mid S_t)>0$ với mọi mẫu, và $\pi_\theta(a\mid s)$ liên tục theo $\theta$.

**Kết luận.**

- (a) $\ell^{\mathrm{CLIP}}_t\le\rho_t\widehat A_t$ với mọi $\theta$, nên $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$.
- (b) Dấu bằng ở (a) cho mẫu $t$ xảy ra khi và chỉ khi $\widehat A_t=0$, hoặc $\widehat A_t>0$ và $\rho_t\le1+\epsilon$, hoặc $\widehat A_t<0$ và $\rho_t\ge1-\epsilon$.
- (c) $\mathcal L^{\mathrm{CLIP}}$ và $\mathcal L^{\mathrm{CPI}}$ trùng nhau trên một lân cận của $\theta_{\mathrm{old}}$; do đó chúng có cùng giá trị $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t]$ và cùng gradient $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$ tại $\theta_{\mathrm{old}}$.

**Điều kiện áp dụng.** Lợi thế cố định; cùng bộ đệm cho hai mục tiêu.

**Phạm vi.** Cận dưới cho mục tiêu mẫu, không phải cho $J$; mệnh đề không chặn khoảng cách giữa $\pi_\theta$ và $\pi_{\mathrm{old}}$ sau nhiều bước.
:::

::: proof
**Bước 1 (kết luận a).** $\ell^{\mathrm{CLIP}}_t$ là $\min$ của hai số, trong đó có $\rho_t\widehat A_t$, nên không vượt $\rho_t\widehat A_t$. Lấy trung bình đều trên bộ đệm giữ bất đẳng thức.

**Bước 2 (kết luận b).** Theo Mệnh đề 10.40: với $\widehat A_t>0$, $\widehat A_t\min(\rho_t,1+\epsilon)=\widehat A_t\rho_t$ khi và chỉ khi $\rho_t\le1+\epsilon$; với $\widehat A_t<0$, $\widehat A_t\max(\rho_t,1-\epsilon)=\widehat A_t\rho_t$ khi và chỉ khi $\rho_t\ge1-\epsilon$; với $\widehat A_t=0$, hai vế bằng $0$.

**Bước 3 (kết luận c).** Tại $\theta_{\mathrm{old}}$, mọi $\rho_t=1$, nằm trong khoảng mở $(1-\epsilon,1+\epsilon)$. Vì $\pi_{\mathrm{old}}(A_t\mid S_t)>0$ và $\pi_\theta$ liên tục, mỗi $\rho_t$ liên tục theo $\theta$; bộ đệm hữu hạn nên có một lân cận $U$ của $\theta_{\mathrm{old}}$ trên đó mọi $\rho_t\in(1-\epsilon,1+\epsilon)$. Theo Bước 2, trên $U$ mọi $\ell^{\mathrm{CLIP}}_t=\rho_t\widehat A_t$, nên hai mục tiêu trùng nhau trên $U$, kéo theo cùng giá trị và cùng gradient tại $\theta_{\mathrm{old}}$. Giá trị là $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t]$ vì $\rho_t=1$; gradient là $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$ vì $\nabla\rho_t=\rho_t\psi_t$. $\square$
:::

Kết luận (a) là lý do Schulman và cộng sự (2017, §3) gọi $\mathcal L^{\mathrm{CLIP}}$ là một *chặn dưới bi quan* (pessimistic bound) của mục tiêu không cắt: mục tiêu cắt bỏ phần tăng của $\mathcal L^{\mathrm{CPI}}$ khi tỉ số ra ngoài khoảng theo hướng có lợi, nhưng giữ phần giảm khi tỉ số đi theo hướng bất lợi.

Kết luận (c) là dạng mẫu của Mệnh đề 10.22: trên bộ đệm, $\mathcal L^{\mathrm{CLIP}}$ và $\mathcal L^{\mathrm{CPI}}$ khớp nhau đến bậc một tại $\theta_{\mathrm{old}}$, như $\mathcal L$ khớp $J$. Trên Ví dụ 10.17, hai mục tiêu trùng nhau trên $p\le0{,}7\overline3$, một lân cận của $p=\tfrac23$. Hai giả thiết của (c) có vai trò riêng.

- Bỏ "$\pi_{\mathrm{old}}(A_t\mid S_t)>0$": tỉ số không xác định.
- Bỏ "bộ đệm hữu hạn": mỗi mẫu có một lân cận riêng, và giao của vô hạn lân cận có thể chỉ còn điểm $\theta_{\mathrm{old}}$, nên một lân cận chung cho mọi mẫu có thể không tồn tại.

**Trong thực hành.** Theo kết luận (c), bước gradient đầu tiên của mỗi lần cập nhật, trên mini-batch đầu tiên của epoch đầu tiên, trùng đúng bước trên $\mathcal L^{\mathrm{CPI}}$ (Engstrom và cộng sự, 2020, §4); bài giảng gốc (tr. 35) viết rằng bước đầu "giống" bước không cắt, còn ở đây hai bước bằng nhau. Điều này cho một phép kiểm cài đặt: ở bước đó mọi $\rho_t$ phải bằng $1$ trong sai số làm tròn, và một tỉ số lệch rõ khỏi $1$ cho thấy log-xác suất cũ hoặc quan sát được lưu không khớp với lần tính lại.

::: remark Nhận xét 10.42 (Cắt tỉ số và khoảng cách KL)
1. Mục tiêu cắt chỉ loại động lực đẩy tỉ số của từng mẫu ra ngoài khoảng; nó không ngăn tỉ số ra ngoài. Sau vài bước, tỉ số có thể vượt khoảng vì ba lý do:
   - một bước trên mẫu này đổi xác suất của mẫu khác cùng trạng thái hoặc có đặc trưng gần;
   - các mini-batch khác nhau kéo tham số theo các hướng khác nhau;
   - quán tính của Adam tiếp tục đẩy tham số sau khi gradient đã bằng $0$.
2. Không có cận nào cho KL giữa $\pi_\theta$ và $\pi_{\mathrm{old}}$ suy ra từ Mệnh đề 10.41. Engstrom và cộng sự (2020, §4) đo được rằng tỉ số vượt khoảng cắt trong cả PPO và PPO không có các *tối ưu mức mã* (code-level optimizations), và rằng mức thay đổi chính sách phụ thuộc cách tối ưu mục tiêu cắt hơn là chính mục tiêu. Với siêu tham số tốt, cả PPO, PPO không có tối ưu mức mã và TRPO đều giữ được KL trung bình nhỏ, nhưng diễn biến KL của hai biến thể PPO khác nhau.
:::

<!-- note-topic-id: lec-10-topic-18 -->
### 6.2 PPO-Penalty

Một cách khác để giữ chính sách mới gần chính sách cũ là phạt trực tiếp KL trong hàm mục tiêu, gần với hàm $\mathcal M_k$ của Hệ quả 10.29 hơn là với bài toán có ràng buộc. Khó khăn là chọn hệ số phạt: theo Schulman và cộng sự (2017, §2.2), một hệ số $\beta$ cố định khó cho kết quả tốt trên nhiều bài toán, hoặc ngay trong một bài toán khi đặc điểm của nó đổi trong quá trình học. Vì vậy bài báo (§4) điều chỉnh hệ số sau mỗi lần cập nhật, gọi là *hệ số phạt thích nghi* (adaptive KL penalty coefficient).

Về mặt ý tưởng, phạt KL biến khoảng cách giữa hai chính sách thành một chi phí: bước nào làm KL tăng nhiều thì phải đem lại mức tăng tương ứng của hàm thay thế mẫu. Hệ số phạt được điều chỉnh sau mỗi lần cập nhật theo KL đo được: KL lớn hơn một mức đích thì lần sau phạt nặng hơn, nhỏ hơn mức đích thì lần sau phạt nhẹ hơn. Ví dụ sau thực hiện một lần điều chỉnh như vậy.

::: example Ví dụ 10.19 (Một lần điều chỉnh hệ số phạt trên bài toán một bước)
**Dữ kiện.** Bài toán một bước và bộ đệm của Ví dụ 10.17: chính sách cũ $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$; ba mẫu, hành động $1,1,2$, lợi thế $\widehat A=(1;\,1;\,-2)$; $p$ là xác suất chọn hành động 1 của chính sách mới. Hệ số phạt hiện tại $\beta=1$, KL đích $\kappa_{\mathrm{targ}}=0{,}01$. Quy tắc của Schulman và cộng sự (2017, §4): sau một lần cập nhật, gọi $\widehat D$ là KL trung bình trên bộ đệm theo chiều cũ‖mới; nếu $\widehat D<\kappa_{\mathrm{targ}}/1{,}5=0{,}00667$ thì $\beta\leftarrow\beta/2$, nếu $\widehat D>1{,}5\,\kappa_{\mathrm{targ}}=0{,}015$ thì $\beta\leftarrow2\beta$. Xét hai kết quả của lần cập nhật: (i) $p=0{,}75$; (ii) $p=0{,}7$.

**Trường hợp (i), $p=0{,}75$.** Ba mẫu cùng trạng thái $s$, nên $\widehat D$ là KL tại $s$:
$$
\begin{aligned}
\widehat D&=\tfrac23\log\frac{2/3}{0{,}75}+\tfrac13\log\frac{1/3}{0{,}25}\\
&=-0{,}07852+0{,}09589\\
&=0{,}01737.
\end{aligned}
$$
Vì $0{,}01737>0{,}015$, hệ số mới là $\beta=2$.

**Trường hợp (ii), $p=0{,}7$.** $\widehat D=\tfrac23\log\frac{2/3}{0{,}7}+\tfrac13\log\frac{1/3}{0{,}3}=-0{,}03253+0{,}03512=0{,}00259$. Vì $0{,}00259<0{,}00667$, hệ số mới là $\beta=0{,}5$.

**Diễn giải.** Ở (i), lần cập nhật đi xa hơn mức đích, nên lần sau mỗi đơn vị KL bị phạt gấp đôi; ở (ii), lần cập nhật quá thận trọng, nên lần sau phạt nhẹ đi một nửa.

**Kiểm tra lại.** Ở (i), $\log\frac{2/3}{0{,}75}=\log\frac89=-0{,}11778$ và $\log\frac43=0{,}28768$, nên $\widehat D=\tfrac23(-0{,}11778)+\tfrac13(0{,}28768)=0{,}01737$.
:::

Định nghĩa sau viết mục tiêu và quy tắc điều chỉnh cho bộ đệm tổng quát.

::: definition Định nghĩa 10.43 (PPO-Penalty với hệ số phạt thích nghi)
Cho bộ đệm $\mathcal D$, hệ số phạt $\beta>0$ và KL mục tiêu $\kappa_{\mathrm{targ}}>0$. Với mỗi mẫu, đặt
$$\begin{aligned}&D_t(\theta)\\&=D_{\mathrm{KL}}\bigl(\pi_{\mathrm{old}}(\cdot\mid S_t)\Vert\pi_\theta(\cdot\mid S_t)\bigr).\end{aligned}$$
*Mục tiêu phạt KL* (KL-penalized objective) là
$$\begin{aligned}&\mathcal L^{\mathrm{KLPEN}}(\theta)\\&=\widehat{\mathbb E}_{\mathcal D}\bigl[\rho_t(\theta)\widehat A_t-\beta\,D_t(\theta)\bigr].\end{aligned}$$
Sau mỗi lần cập nhật, gồm vài epoch tối ưu $\mathcal L^{\mathrm{KLPEN}}$, tính KL trung bình trên bộ đệm $\widehat D(\theta)=\widehat{\mathbb E}_{\mathcal D}[D_t(\theta)]$, như ở Thuật toán 10.37, và đặt

- $\beta\leftarrow\beta/2$ nếu $\widehat D(\theta)<\kappa_{\mathrm{targ}}/1{,}5$;
- $\beta\leftarrow2\beta$ nếu $\widehat D(\theta)>1{,}5\,\kappa_{\mathrm{targ}}$;
- giữ $\beta$ trong trường hợp còn lại.

Hệ số mới được dùng cho lần cập nhật sau.
:::

KL trong định nghĩa là KL đúng giữa hai phân phối hành động tại $S_t$, tính dạng đóng với chính sách softmax, không phải một ước lượng từ hành động mẫu. Với $\beta$ cố định, $\mathcal L^{\mathrm{KLPEN}}$ có cùng dạng với hàm phạt $D^{\max}_{\mathrm{KL}}$ trong Thuật toán 1 của Schulman và cộng sự (2015), với KL trung bình mẫu thay cho KL lớn nhất và $\beta$ thay cho hằng $4\bar\chi\gamma/(1-\gamma)^2$; quy tắc điều chỉnh đưa KL đo được về gần $\kappa_{\mathrm{targ}}$, nên $\kappa_{\mathrm{targ}}$ đóng vai bán kính $\kappa$ của TRPO. Trong Ví dụ 10.19, trường hợp (i) là trường hợp thứ hai của quy tắc, trường hợp (ii) là trường hợp thứ nhất.

::: remark Nhận xét 10.44 (Phạm vi của PPO-Penalty)
1. PPO-Penalty không có bảo đảm $J$ tăng sau một lần cập nhật: $\beta$ không phải hằng của Hệ quả 10.29, và mục tiêu là trung bình mẫu với lợi thế ước lượng, nên các giả thiết của hệ quả đó không thỏa. Schulman và cộng sự (2017, §4) ghi rằng các hằng $1{,}5$ và $2$ được chọn theo kinh nghiệm (heuristically), và thuật toán không nhạy với chúng; KL sau một lần cập nhật đôi khi khác xa $\kappa_{\mathrm{targ}}$, và $\beta$ điều chỉnh lại nhanh.
2. Trong thí nghiệm MuJoCo của bài báo (Bảng 1), cấu hình cắt với $\epsilon=0{,}2$ cho điểm chuẩn hóa trung bình cao nhất trong các cấu hình được thử, kể cả các cấu hình phạt KL cố định và thích nghi; bài báo ghi rằng phạt KL cho kết quả kém hơn mục tiêu cắt trong các thí nghiệm của họ và giữ nó như một phương pháp đối chứng.
:::

**Trong thực hành.** PPO-Penalty tối ưu $\mathcal L^{\mathrm{KLPEN}}$ bằng vài epoch Adam trên mini-batch của cùng một bộ đệm, như vòng lặp PPO đầy đủ ở Thuật toán 10.49 (Mục 6.3), rồi tính $\widehat D$ trên bộ đệm để cập nhật $\beta$. KL tại mỗi $S_t$ tính dạng đóng từ hai phân phối hành động, nên bộ đệm lưu phân phối của $\pi_{\mathrm{old}}$ trên mọi hành động, không chỉ log-xác suất của $A_t$.

<!-- note-topic-id: lec-10-topic-19 -->
### 6.3 Hàm mất mát tổng và thuật toán PPO

PPO thường huấn luyện chính sách và critic cùng lúc, đôi khi với một mạng dùng chung tham số, nên cần một hàm mất mát duy nhất. Hàm đó có thêm một số hạng khuyến khích chính sách giữ ngẫu nhiên, đo bằng *entropy*. Về mặt ý tưởng, ba số hạng của hàm mất mát ứng với ba việc trên cùng bộ đệm: tăng mục tiêu cắt của actor, hồi quy critic về lợi tức λ, và giữ chính sách đủ ngẫu nhiên để còn thăm dò.

::: definition Định nghĩa 10.45 (Entropy của chính sách)
Entropy của phân phối hành động $\pi(\cdot\mid s)$ trên tập hữu hạn $\mathcal A$ là
$$\begin{aligned}&\mathcal H\bigl(\pi(\cdot\mid s)\bigr)\\&\quad=-\sum_{a\in\mathcal A}\pi(a\mid s)\log\pi(a\mid s),\end{aligned}$$
với quy ước $0\log0=0$.
:::

Entropy bằng $0$ khi chính sách tất định tại $s$ và lớn nhất, bằng $\log m$, khi chính sách đều. Với $\mathcal U$ là phân phối đều trên $m$ hành động, Định nghĩa 10.23 cho $D_{\mathrm{KL}}(q\Vert\mathcal U)=\sum_aq(a)\log\bigl(m\,q(a)\bigr)=\log m-\mathcal H(q)$, nên tăng entropy là kéo chính sách về phía phân phối đều. Ví dụ, $\mathcal H(\tfrac23;\,\tfrac13)=0{,}6365$ và $\mathcal H(0{,}75;\,0{,}25)=0{,}5623$.

::: definition Định nghĩa 10.46 (Hàm mất mát tổng)
Cho bộ đệm với $\widehat A^{\mathrm{raw}}_t$ và $V^{\mathrm{targ}}_t=\widehat A^{\mathrm{raw}}_t+\hat v_{\mathrm{old}}(S_t)$ của Thuật toán 10.16, giữ cố định; critic $\hat v(s,w)$; hệ số $c_1,c_2\ge0$. *Hàm mất mát tổng* (được cực tiểu hóa) là
$$\begin{aligned}&L(\theta,w)=-\mathcal L^{\mathrm{CLIP}}(\theta)\\&\quad+c_1L^V(w)\\&\quad-c_2\,\widehat{\mathbb E}_{\mathcal D}\bigl[\mathcal H(\pi_\theta(\cdot\mid S_t))\bigr],\\&L^V(w)\\&\quad=\widehat{\mathbb E}_{\mathcal D}\bigl[(\hat v(S_t,w)-V^{\mathrm{targ}}_t)^2\bigr].\end{aligned}$$
Biến thể *cắt mất mát giá trị* (value function clipping) thay số hạng trong $L^V$ bằng
$$\begin{aligned}&\max\bigl[(\hat v(S_t,w)-V^{\mathrm{targ}}_t)^2,\\&\qquad(\hat v^{\mathrm{clip}}_t-V^{\mathrm{targ}}_t)^2\bigr],\end{aligned}$$
với giá trị cắt $\hat v^{\mathrm{clip}}_t=\operatorname{clip}\bigl(\hat v(S_t,w),\,\hat v_{\mathrm{old}}(S_t)-\epsilon,\,\hat v_{\mathrm{old}}(S_t)+\epsilon\bigr)$.
Lợi thế dùng trong $\mathcal L^{\mathrm{CLIP}}$ có thể được chuẩn hóa, $\widehat A_t=(\widehat A^{\mathrm{raw}}_t-\bar A_{\mathcal B})/s_{\mathcal B}$ với trung bình $\bar A_{\mathcal B}$ và độ lệch chuẩn $s_{\mathcal B}$ trên mini-batch hoặc trên cả bộ đệm; $V^{\mathrm{targ}}_t$ luôn dùng $\widehat A^{\mathrm{raw}}_t$.
:::

Từ đây, $\widehat A^{\mathrm{raw}}_t$ là đầu ra $\widehat A_t$ của Thuật toán 10.16, còn $\widehat A_t$ chỉ lợi thế đưa vào $\mathcal L^{\mathrm{CLIP}}$, đã chuẩn hóa hoặc không. Hàm $L$ là (9) của Schulman và cộng sự (2017), đổi dấu để cực tiểu hóa (bài giảng gốc, tr. 23). Số hạng thứ nhất là mục tiêu của actor; số hạng thứ hai hồi quy critic về lợi tức λ cắt, như Mục 3.3; số hạng thứ ba thưởng cho entropy.

Biến thể cắt mất mát giá trị (bài giảng gốc, tr. 30; Engstrom và cộng sự, 2020, §3) dùng chính $\epsilon$ của tỉ số. Theo Huang và cộng sự (2022, chi tiết 9), Engstrom và cộng sự không thấy bằng chứng biến thể này giúp ích, còn Andrychowicz và cộng sự (2021) cho rằng nó có thể làm giảm hiệu năng.

Chuẩn hóa lợi thế là một lựa chọn cài đặt: trừ trung bình là trừ một đường cơ sở hằng của mini-batch, chia độ lệch chuẩn là đổi thang của bước. Vì trung bình và độ lệch chuẩn được tính từ chính mini-batch, hệ số của mỗi mẫu phụ thuộc cả hành động của mẫu đó, nên điều kiện "đường cơ sở không phụ thuộc hành động" của Mệnh đề 10.2 không thỏa.

::: example Ví dụ 10.20 (Một mini-batch tính tay)
**Dữ kiện.** Bài toán một bước, $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\hat v_{\mathrm{old}}(s)=2$. Mini-batch ba mẫu: hành động $1,1,2$, phần thưởng $3,3,0$, $\widehat A^{\mathrm{raw}}=(1;\,1;\,-2)$, $V^{\mathrm{targ}}=(3;\,3;\,0)$. Tham số hiện tại cho $p=\pi_\theta(1\mid s)=0{,}75$ và $\hat v(s,w)=2{,}2$. Hệ số $\epsilon=0{,}2$, $c_1=1$, $c_2=0{,}01$ (Schulman và cộng sự, 2017, Bảng 5). Không chuẩn hóa lợi thế.

**Tỉ số và mục tiêu cắt.** $\rho=(1{,}5\cdot0{,}75;\,1{,}5\cdot0{,}75;\,3\cdot0{,}25)=(1{,}125;\,1{,}125;\,0{,}75)$. Hai mẫu đầu có lợi thế dương và $\rho<1{,}2$, nên $\ell=1{,}125$; mẫu thứ ba có lợi thế âm và $\rho<0{,}8$, nên bị cắt: $\ell=-2\cdot0{,}8=-1{,}6$. Do đó $\mathcal L^{\mathrm{CLIP}}=(1{,}125+1{,}125-1{,}6)/3=0{,}2167$.

**Gradient của actor.** Theo logit $(\theta_1;\,\theta_2)$, $\mathcal L^{\mathrm{CLIP}}=p-0{,}5\overline3$ trên khúc này (Ví dụ 10.17), nên gradient là $p(1-p)(1;\,-1)=(0{,}1875;\,-0{,}1875)$; mẫu thứ ba không đóng góp. Gradient của $\mathcal L^{\mathrm{CPI}}=3p-2$ là $(0{,}5625;\,-0{,}5625)$.

**Mất mát giá trị, entropy, mất mát tổng.** $L^V=\bigl((2{,}2-3)^2+(2{,}2-3)^2+(2{,}2-0)^2\bigr)/3=(0{,}64+0{,}64+4{,}84)/3=2{,}04$; $\mathcal H(0{,}75;\,0{,}25)=0{,}5623$; và
$$\begin{aligned}&L=-0{,}2167+1\cdot2{,}04\\&\quad-0{,}01\cdot0{,}5623\\&\quad=1{,}8177.\end{aligned}$$

**Hai ước lượng KL.** Từng mẫu, $-\log\rho=(-0{,}1178;\,-0{,}1178;\,0{,}2877)$, hai số đầu âm, còn $(\rho-1)-\log\rho=(0{,}0072;\,0{,}0072;\,0{,}0377)$, mọi số không âm. Trung bình của dạng thứ hai là $0{,}01737$; tỉ lệ mẫu có $\lvert\rho-1\rvert>0{,}2$ là $1/3$.

**Chuẩn hóa.** Nếu chuẩn hóa lợi thế với độ lệch chuẩn tổng thể $\sqrt2$ của $(1;\,1;\,-2)$, ta được $\widehat A=(0{,}7071;\,0{,}7071;\,-1{,}4142)$; dấu không đổi, nên tập mẫu bị cắt không đổi.

**Kiểm tra lại.** $\partial(3p-2)/\partial\theta_1=3p(1-p)=0{,}5625$ và $\partial(p-0{,}5\overline3)/\partial\theta_1=p(1-p)=0{,}1875$.
:::

Hai ước lượng KL và tỉ lệ cắt ở cuối Ví dụ 10.20 là các đại lượng mà cài đặt PPO ghi lại sau mỗi mini-batch; bài giảng gốc (tr. 25, 27) chỉ liệt kê tên của chúng. Định nghĩa sau cho công thức.

::: definition Định nghĩa 10.47 (Đại lượng chẩn đoán)
Trên mini-batch với tập chỉ số $\mathcal B$ và tỉ số $\rho_i=\rho_i(\theta)$:

- *approxKL* (approximate KL) là $\dfrac1{\lvert\mathcal B\rvert}\sum_{i\in\mathcal B}\bigl[(\rho_i-1)-\log\rho_i\bigr]$; dạng $\dfrac1{\lvert\mathcal B\rvert}\sum_i(-\log\rho_i)$ cũng được dùng;
- *tỉ lệ cắt* (clip fraction) là $\dfrac1{\lvert\mathcal B\rvert}\,\#\{i\in\mathcal B:\lvert\rho_i-1\rvert>\epsilon\}$;
- entropy trung bình là $\dfrac1{\lvert\mathcal B\rvert}\sum_{i\in\mathcal B}\mathcal H\bigl(\pi_\theta(\cdot\mid S_i)\bigr)$;
- mất mát giá trị là $L^V(w)$ của Định nghĩa 10.46, lấy trung bình trên $\mathcal B$.

Trên cả bộ đệm, với mục tiêu $y_t=V^{\mathrm{targ}}_t$ và dự đoán $\hat y_t=\hat v_{\mathrm{old}}(S_t)$, *phương sai được giải thích* (explained variance) là $1-\operatorname{Var}(y-\hat y)/\operatorname{Var}(y)$, với phương sai mẫu trên bộ đệm.
:::

Các đại lượng này nằm trong nhóm "biến gỡ lỗi" của Huang và cộng sự (2022). Bài viết đó cũng gợi ý dạng $(\rho-1)-\log\rho$ cho approxKL. Tỉ lệ cắt đếm mẫu có tỉ số ngoài khoảng, bất kể dấu của lợi thế; nó khác tỉ lệ mẫu có gradient bằng $0$, vốn phụ thuộc dấu theo Mệnh đề 10.40(d). Phương sai được giải thích bằng $1$ khi critic dự đoán đúng mọi mục tiêu, bằng $0$ khi critic dự đoán một hằng, và âm khi phần dư biến thiên nhiều hơn chính mục tiêu.

Bài giảng gốc (tr. 27) dùng các đại lượng này làm tín hiệu theo dõi: approxKL cho biết bước cập nhật có quá lớn không, tỉ lệ cắt cho biết bao nhiêu mẫu ở vùng bị cắt, entropy cho biết việc thăm dò có đang sụp không, phương sai được giải thích cho biết critic dự đoán lợi tức tốt đến đâu, và mất mát giá trị cho biết critic có chi phối bước cập nhật không. Nguồn nêu một mẫu bất ổn thường gặp: phần thưởng tăng trong thời gian ngắn, KL tăng vọt, entropy sụp, và chính sách ngừng thăm dò.

::: proposition Mệnh đề 10.48 (approxKL không chệch và không âm)
**Giả thiết.** Tại trạng thái $s$, $A\sim\pi_{\mathrm{old}}(\cdot\mid s)$ trên tập hữu hạn; $\theta$ cố định, không phụ thuộc mẫu $A$; hai điều kiện miền hỗ trợ:

- (i) $\pi_\theta(a\mid s)>0$ với mọi $a$ thuộc miền hỗ trợ của $\pi_{\mathrm{old}}(\cdot\mid s)$;
- (ii) miền hỗ trợ của $\pi_\theta(\cdot\mid s)$ nằm trong miền hỗ trợ của $\pi_{\mathrm{old}}(\cdot\mid s)$.

Đặt $\rho=\pi_\theta(A\mid s)/\pi_{\mathrm{old}}(A\mid s)$.

**Kết luận.**

- (a) $\mathbb E\bigl[(\rho-1)-\log\rho\bigr]=D_{\mathrm{KL}}\bigl(\pi_{\mathrm{old}}(\cdot\mid s)\Vert\pi_\theta(\cdot\mid s)\bigr)$.
- (b) $(\rho-1)-\log\rho\ge0$ với mọi mẫu, dấu bằng khi và chỉ khi $\rho=1$.

**Điều kiện áp dụng.** Mẫu lấy từ $\pi_{\mathrm{old}}$, và $\theta$ được chọn trước khi rút mẫu, chẳng hạn khi approxKL tính trên mẫu mới hoặc trên một mini-batch chưa dùng để cập nhật $\theta$. Điều kiện (ii) cùng chiều điều kiện hỗ trợ của Định nghĩa 06.24, điều kiện (i) theo chiều ngược lại; chính sách softmax thỏa cả hai.

**Phạm vi.** Khi $\theta$ không phụ thuộc mẫu, kết luận (a) cho tính không chệch tại từng trạng thái, và trung bình trên một mini-batch là ước lượng không chệch của KL trung bình theo phân bố trạng thái của mini-batch. Trong Thuật toán 10.49, từ epoch thứ hai $\theta$ đã được tối ưu trên chính các mẫu dùng để tính approxKL, và ngay ở epoch đầu $\theta$ có thể đã được cập nhật trên các bước chuyển sau $A_i$ của cùng lượt, vốn phụ thuộc $A_i$; khi đó approxKL là một đại lượng chẩn đoán không có bảo đảm không chệch. Kết luận (b) đúng trên từng mẫu trong mọi trường hợp.
:::

::: proof
**Bước 1 (kỳ vọng của $\rho-1$).** Vì $\theta$ không phụ thuộc $A$, kỳ vọng lấy theo $A\sim\pi_{\mathrm{old}}(\cdot\mid s)$ với $\pi_\theta$ cố định:
$$
\begin{aligned}
&\mathbb E[\rho]\\
&=\sum_{a:\,\pi_{\mathrm{old}}(a\mid s)>0}\pi_{\mathrm{old}}(a\mid s)\\
&\quad\times\frac{\pi_\theta(a\mid s)}{\pi_{\mathrm{old}}(a\mid s)}\\
&=\sum_{a:\,\pi_{\mathrm{old}}(a\mid s)>0}\pi_\theta(a\mid s)\\
&=1.
\end{aligned}
$$
Đẳng thức thứ nhất là định nghĩa kỳ vọng, đẳng thức thứ hai rút gọn $\pi_{\mathrm{old}}(a\mid s)$, đẳng thức thứ ba dùng (ii): $\pi_\theta$ không có khối ngoài miền hỗ trợ của $\pi_{\mathrm{old}}$. Do đó $\mathbb E[\rho-1]=0$.

**Bước 2 (kỳ vọng của $-\log\rho$).** $\mathbb E[-\log\rho]=\sum_a\pi_{\mathrm{old}}(a\mid s)\log\frac{\pi_{\mathrm{old}}(a\mid s)}{\pi_\theta(a\mid s)}=D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid s)\Vert\pi_\theta(\cdot\mid s))$, hữu hạn vì $\pi_\theta>0$ trên miền hỗ trợ của $\pi_{\mathrm{old}}$ theo (i). Cộng với Bước 1 được (a).

**Bước 3 (kết luận b).** Với $x=\rho>0$, Bước 1 của chứng minh Mệnh đề 10.24 cho $x-1-\log x\ge0$, dấu bằng khi và chỉ khi $x=1$. $\square$
:::

Cả hai dạng approxKL có kỳ vọng bằng KL dưới các giả thiết của mệnh đề, vì $\rho-1$ có kỳ vọng $0$; dạng $(\rho-1)-\log\rho$ còn không âm trên từng mẫu, nên trung bình của nó không bao giờ âm, điều mà dạng $-\log\rho$ không bảo đảm. Trên Ví dụ 10.20, tần suất mẫu trùng $\pi_{\mathrm{old}}$, nên cả hai trung bình bằng đúng KL thật tại $p=0{,}75$, là $0{,}01737$. Ba giả thiết có vai trò riêng.

- Bỏ (ii): với $\pi_{\mathrm{old}}(\cdot\mid s)=(1;\,0)$ và $\pi_\theta(\cdot\mid s)=(0{,}9;\,0{,}1)$, mọi mẫu là hành động 1 và $\rho=0{,}9$, nên $\mathbb E[\rho]=0{,}9<1$ và $\mathbb E[(\rho-1)-\log\rho]=-0{,}1+0{,}10536=0{,}00536$, nhỏ hơn KL thật $0{,}10536$: dạng $(\rho-1)-\log\rho$ chệch xuống.
- Bỏ (i): có mẫu với $\rho=0$, $\log\rho$ không xác định, và KL bằng $+\infty$.
- Bỏ "$\theta$ không phụ thuộc mẫu": với ba hành động và $\pi_{\mathrm{old}}$ đều, nếu sau khi thấy $A=a$ ta chọn $\pi_\theta$ gán $\tfrac13$ cho $a$, $\tfrac12$ và $\tfrac16$ cho hai hành động còn lại, thì $\rho=1$ ở mọi mẫu và approxKL bằng $0$, trong khi KL thật bằng $\tfrac13\bigl(\log\tfrac23+\log2\bigr)=0{,}0959$.

![Sơ đồ dữ liệu của một vòng PPO. Bên trái, N môi trường xếp chồng, mỗi môi trường chạy h bước bằng pi old, tạo lưới h nhân N mẫu. Mũi tên sang bộ đệm D gồm hN mẫu, mỗi mẫu lưu S t, A t, R t+1, Z t+1, U t+1, log pi old, v mũ old. Mũi tên sang khung GAE tính A mũ raw và V targ. Mũi tên sang vòng lặp K epoch: xáo D, chia mini-batch cỡ M, mỗi mini-batch một bước Adam trên L. Mũi tên cong quay về bên trái ghi theta old gán bằng theta.](img/lec-10/ppo-data-pipeline.svg)

Trên hình, dữ liệu đi từ trái sang phải: dữ liệu được thu một lần bằng $\pi_{\mathrm{old}}$ trên $N$ môi trường, tính GAE một lần, rồi dùng lại trong $K$ epoch; mỗi epoch đi qua $\lceil hN/M\rceil$ mini-batch. Mũi tên quay về chỉ được đi sau khi hết $K$ epoch.

::: algorithm Thuật toán 10.49 (PPO kiểu actor–critic)
**Đầu vào.** Chính sách $\pi_\theta$, critic $\hat v(s,w)$; $N$, $h$, $K$, $M$; $\gamma$, $\lambda$, $\epsilon$, $c_1$, $c_2$; bước học $\alpha$ của Adam; tùy chọn ngưỡng approxKL để dừng sớm.

**Đầu ra.** Tham số $\theta$, $w$ sau số vòng lặp đã định.

**Giả thiết.** $\pi_\theta>0$ trên mọi hành động, như với softmax; môi trường trả cờ $Z$, $U$ và quan sát cuối khi cắt ngắn.

**Mỗi vòng lặp:**

1. $\theta_{\mathrm{old}}\leftarrow\theta$, $w_{\mathrm{old}}\leftarrow w$. Thu $h$ bước trên mỗi môi trường bằng $\pi_{\mathrm{old}}$, lưu $S_t$, $A_t$, $R_{t+1}$, $Z_{t+1}$, $U_{t+1}$, $\log\pi_{\mathrm{old}}(A_t\mid S_t)$, $\hat v_{\mathrm{old}}(S_t)$ và giá trị của quan sát cuối ở mỗi bước cắt ngắn.
2. Tính $\widehat A^{\mathrm{raw}}_t$ và $V^{\mathrm{targ}}_t$ bằng Thuật toán 10.16.
3. Với mỗi epoch $1,\dots,K$: xáo $\mathcal D$, chia thành các mini-batch $\mathcal B$ cỡ $M$; với mỗi mini-batch:
   - (tùy chọn) chuẩn hóa lợi thế trên mini-batch;
   - tính lại $\log\pi_\theta(A_i\mid S_i)$, tỉ số $\rho_i$ bằng $\exp$ của hiệu hai log-xác suất, $\hat v(S_i,w)$ và $\mathcal H(\pi_\theta(\cdot\mid S_i))$;
   - thực hiện một bước Adam trên $L(\theta,w)$ của Định nghĩa 10.46, lấy trung bình trên $\mathcal B$;
   - ghi approxKL và tỉ lệ cắt (Định nghĩa 10.47); (tùy chọn) dừng các epoch còn lại nếu approxKL vượt ngưỡng.

**Điều kiện dừng.** Sau số vòng lặp hoặc số bước môi trường đã định.

**Chi phí mỗi vòng lặp.** $hN$ bước môi trường và $K\lceil hN/M\rceil$ bước gradient.
:::

| Giữ cố định trong cả $K$ epoch | Tính lại ở mỗi mini-batch |
|---|---|
| $\log\pi_{\mathrm{old}}(A_t\mid S_t)$, $\widehat A^{\mathrm{raw}}_t$, $V^{\mathrm{targ}}_t$, $\hat v_{\mathrm{old}}(S_t)$ | $\log\pi_\theta(A_t\mid S_t)$, $\rho_t(\theta)$, $\hat v(S_t,w)$, $\mathcal H(\pi_\theta(\cdot\mid S_t))$ |

Thuật toán 10.49 là Thuật toán 1 của Schulman và cộng sự (2017) với các bước của bài giảng gốc (tr. 24–25) và các cờ của Mục 3.3. Bảng trên tách hai loại đại lượng: cột trái được tính một lần từ dữ liệu của $\pi_{\mathrm{old}}$, cột phải phụ thuộc tham số hiện tại.

Từ mini-batch thứ hai, $\theta\ne\theta_{\mathrm{old}}$, nên dữ liệu đã là dữ liệu khác chính sách; bài giảng gốc (tr. 24) gọi việc này là "dùng lại mẫu". Tỉ số $\rho_t$ hiệu chỉnh phân phối hành động tại mỗi trạng thái, còn phân bố trạng thái vẫn là của $\pi_{\mathrm{old}}$, như trong hàm thay thế của Mục 4.2.

Với hành động nhiều chiều có các thành phần độc lập, log-xác suất của hành động là tổng log-xác suất các thành phần, cộng trước khi lập tỉ số. Ví dụ 10.20 là một mini-batch của bước 3.

**Trong thực hành.** Thuật toán 10.49 giải quyết giới hạn thứ hai của Mục 1 theo cách sau: mỗi lần thu $hN$ bước cho $K\lceil hN/M\rceil$ bước gradient thay vì một. Bảo đảm còn lại chỉ ở mức Mệnh đề 10.41: mục tiêu cắt không tạo động lực đẩy tỉ số ra ngoài khoảng. Lợi thế từ GAE với critic học được không có bảo đảm γ-just (Mệnh đề 10.15; Ví dụ 10.9 cho một trường hợp chệch), và Adam, mini-batch, chuẩn hóa lợi thế không có trong các kết quả của Mục 4. approxKL và tỉ lệ cắt được ghi để phát hiện bước cập nhật đi quá xa.

<!-- note-topic-id: lec-10-topic-20 -->
### 6.4 Đọc chẩn đoán và chọn siêu tham số

Ví dụ sau tiếp tục Ví dụ 10.20 sau vài mini-batch.

::: example Ví dụ 10.21 (Chẩn đoán trên đoạn phẳng)
**Dữ kiện.** Như Ví dụ 10.20: bài toán một bước, $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, mini-batch hành động $1,1,2$, $\widehat A=(1;\,1;\,-2)$, $\epsilon=0{,}2$, $V^{\mathrm{targ}}=(3;\,3;\,0)$. Sau vài mini-batch, $p=0{,}85$.

**Tỉ số và gradient.** $\rho=(1{,}275;\,1{,}275;\,0{,}45)$. Hai mẫu đầu có lợi thế dương và $\rho>1{,}2$, mẫu thứ ba có lợi thế âm và $\rho<0{,}8$: mọi mẫu nằm trên đoạn phẳng, gradient của $\mathcal L^{\mathrm{CLIP}}$ bằng $0$, và $\mathcal L^{\mathrm{CLIP}}=0{,}2\overline6$ như Ví dụ 10.17.

**Chẩn đoán.** Tỉ lệ cắt là $3/3$; approxKL là $0{,}1042$, bằng KL thật tại $p=0{,}85$. Với mini-batch chỉ có một mẫu hành động 1: $-\log\rho=-\log1{,}275=-0{,}2430<0$, trong khi $(\rho-1)-\log\rho=0{,}0321\ge0$.

**Phương sai được giải thích.** Với critic đúng $\hat v_{\mathrm{old}}=2$: $y=(3;\,3;\,0)$ có $\operatorname{Var}(y)=2$, $y-\hat y=(1;\,1;\,-2)$ có phương sai $2$, nên phương sai được giải thích bằng $0$.

**Diễn giải.** Tỉ lệ cắt $3/3$ ở đây trùng với gradient của mục tiêu cắt bằng $0$, nhưng hai đại lượng nói chung khác nhau: một mẫu có lợi thế dương và $\rho<0{,}8$ được đếm vào tỉ lệ cắt mà vẫn có gradient. KL $0{,}1042$ lớn gấp sáu lần KL $0{,}01737$ của Ví dụ 10.20, dù mục tiêu cắt đã phẳng từ $p=0{,}8$: tham số vẫn đi vào đoạn phẳng, chẳng hạn nhờ quán tính của Adam hoặc các mini-batch khác (Nhận xét 10.42). Phương sai được giải thích bằng $0$ với một critic đúng, vì chỉ có một trạng thái và mọi biến thiên của mục tiêu đến từ hành động; giá trị thấp không có nghĩa critic sai.

**Kiểm tra lại.** $\tfrac23\log\frac{2/3}{0{,}85}+\tfrac13\log\frac{1/3}{0{,}15}=0{,}1042$; $0{,}275-0{,}2430=0{,}0321$.
:::

Các giá trị trong bảng sau lấy từ bài báo PPO, cộng hai chi tiết từ Huang và cộng sự (2022); bảng siêu tham số của bài giảng gốc (tr. 26) không ghi nguồn.

| Siêu tham số | MuJoCo (Schulman và cộng sự, 2017, Bảng 3) | Atari (Schulman và cộng sự, 2017, Bảng 5) |
|---|---|---|
| Độ dài đoạn $h$ | $2048$ | $128$ |
| Số môi trường $N$ | không ghi trong bảng | $8$ |
| Bước học Adam $\alpha$ | $3\cdot10^{-4}$ | $2{,}5\cdot10^{-4}$ nhân hệ số giảm tuyến tính từ $1$ về $0$ |
| Số epoch $K$ | $10$ | $3$ |
| Cỡ mini-batch $M$ | $64$ | $32\cdot8$ |
| $\gamma$; $\lambda$ | $0{,}99$; $0{,}95$ | $0{,}99$; $0{,}95$ |
| Bán kính cắt $\epsilon$ | Bảng 1 thử $0{,}1$; $0{,}2$; $0{,}3$ | $0{,}1$ nhân cùng hệ số giảm |
| $c_1$; $c_2$ | không dùng chung tham số, không thưởng entropy (§6.1) | $1$; $0{,}01$ |
| Cắt chuẩn gradient; hằng ổn định số của Adam | $0{,}5$; $10^{-5}$ (Huang và cộng sự, 2022) | $0{,}5$; $10^{-5}$ (Huang và cộng sự, 2022) |

Bảng so sánh sau viết lại bảng của bài giảng gốc (tr. 28) theo điều mỗi phương pháp bảo đảm.

| Tiêu chí | TRPO (Thuật toán 10.37) | PPO (Thuật toán 10.49) |
|---|---|---|
| Cách giữ gần chính sách cũ | ràng buộc KL trung bình mẫu $\le\kappa$ | cắt tỉ số trong mục tiêu (hoặc phạt KL) |
| Chi phí mỗi vòng lặp | $k_{\max}$ tích Fisher–vector, tìm kiếm lùi | $K\lceil hN/M\rceil$ bước gradient |
| Điều được bảo đảm trên bộ đệm | KL trung bình mẫu $\le\kappa$, hàm thay thế mẫu tăng | không có cận KL |
| Giả thiết lý thuyết còn thiếu | lợi thế, $\nu^{\mathrm{old}}$, nghiệm chính xác (Nhận xét 10.38) | như TRPO, thêm cắt thay ràng buộc (Nhận xét 10.42) |

<!-- note-topic-id: lec-10-topic-21 -->
### 6.5 Chi tiết cài đặt

Engstrom và cộng sự (2020) đặt câu hỏi mà bài giảng gốc (tr. 29) nhắc lại: mức cải thiện của PPO so với TRPO đến từ mục tiêu cắt, hay từ các chi tiết ở mức mã không có trong mô tả thuật toán. Một ví dụ nhỏ cho thấy một chi tiết như vậy đổi hành vi của critic.

::: example Ví dụ 10.22 (Cắt mất mát giá trị trên một mẫu)
**Dữ kiện.** Biến thể cắt mất mát giá trị của Định nghĩa 10.46 với $\hat v_{\mathrm{old}}(s)=2$, $\epsilon=0{,}2$, critic hiện tại $\hat v(s,w)=2{,}5$; khoảng cắt là $[1{,}8;\,2{,}2]$, nên $\operatorname{clip}(2{,}5;\,1{,}8;\,2{,}2)=2{,}2$.

**Mẫu (i), $V^{\mathrm{targ}}=3$.** Không cắt: $(2{,}5-3)^2=0{,}25$; cắt: $(2{,}2-3)^2=0{,}64$. Giá trị lớn hơn là $0{,}64$, từ nhánh cắt, không phụ thuộc $\hat v$, nên gradient theo $\hat v$ bằng $0$: critic không được kéo tiếp về $3$.

**Mẫu (ii), $V^{\mathrm{targ}}=0$.** Không cắt: $6{,}25$; cắt: $4{,}84$. Giá trị lớn hơn là nhánh không cắt, gradient theo $\hat v$ là $2\cdot(2{,}5-0)=5$.

**Diễn giải.** Ở mẫu (i), critic đã vượt khỏi khoảng cắt theo hướng của mục tiêu và bị dừng, dù $3$ gần $2{,}5$ hơn $2{,}2$; ở mẫu (ii), critic đi sai hướng và vẫn nhận gradient. Với phép cắt, critic cực tiểu hóa $\max$ của hai bình phương, khác $L^V$.

**Kiểm tra lại.** $\max(0{,}25;\,0{,}64)=0{,}64$ và $\max(6{,}25;\,4{,}84)=6{,}25$.
:::

::: remark Nhận xét 10.50 (Chi tiết cài đặt và kết quả loại bỏ)
Bảng sau đối chiếu danh sách kiểm của bài giảng gốc (tr. 36) với 13 chi tiết cốt lõi của Huang và cộng sự (2022) và 9 tối ưu mức mã của Engstrom và cộng sự (2020, §3), theo thành phần mà mỗi chi tiết thay đổi.

| Chi tiết | Thành phần bị thay đổi |
|---|---|
| Môi trường vector hóa, $N$ môi trường song song | dữ liệu |
| Chuẩn hóa và cắt quan sát | dữ liệu (đầu vào của mạng) |
| Chuẩn hóa phần thưởng theo độ lệch chuẩn của lợi tức chiết khấu chạy; cắt phần thưởng | mục tiêu (hàm phần thưởng thực sự được tối ưu) |
| Chuẩn hóa lợi thế theo mini-batch | mục tiêu của actor (thang và đường cơ sở) |
| Cắt mất mát giá trị | mục tiêu của critic |
| Hệ số entropy $c_2$ | mục tiêu của actor |
| Khởi tạo trực giao, nhân hệ số theo lớp; hàm kích hoạt tanh | bộ tối ưu (điểm xuất phát) và mạng |
| Ủ bước học; hằng ổn định số $10^{-5}$ của Adam | bộ tối ưu |
| Cắt chuẩn gradient toàn cục ở $0{,}5$ | bộ tối ưu |
| Xáo bộ đệm, $K$ epoch, cỡ mini-batch $M$ | bộ tối ưu và cách dùng lại dữ liệu |
| Dừng sớm theo approxKL | bộ tối ưu |
| Mạng chung hay tách cho chính sách và critic | mạng và mục tiêu (qua $c_1$) |

Engstrom và cộng sự (2020, §5–6) rút ra ba kết luận định tính từ thí nghiệm loại bỏ của họ:

- các tối ưu mức mã giải thích phần lớn mức cải thiện phần thưởng của PPO so với TRPO trong thí nghiệm của họ;
- PPO bỏ phép cắt nhưng giữ các tối ưu mức mã, khi siêu tham số được tinh chỉnh đủ, thường đạt mức của PPO chuẩn;
- các tối ưu mức mã quyết định tính chất miền tin cậy mà thuật toán thực sự giữ được (§4).

Chuẩn hóa và cắt phần thưởng làm thuật toán tối ưu một hàm mục tiêu khác $J$ của MDP ban đầu, vì phần thưởng bị chia cho một đại lượng đổi theo thời gian. Vì vậy, một báo cáo kết quả của PPO cần ghi đủ các chi tiết cài đặt trong bảng trên (bài giảng gốc, tr. 36).
:::

<!-- note-topic-id: lec-10-topic-22 -->
### 6.6 Đọc thêm: hội tụ về điểm dừng của PPO-Clip

Bài giảng gốc (tr. 37) nêu bốn khó khăn khi phân tích PPO-Clip: mục tiêu chứa tỉ số của hai chính sách ngẫu nhiên, phép cắt không trơn, hàm điểm có thể không bị chặn, và thuật toán xen kẽ việc đồng bộ $\pi_{\mathrm{old}}$ với các bước tối ưu bên trong. Nhận xét sau phát biểu một kết quả gần đây cùng mô hình mà nó dựa vào.

::: remark Nhận xét 10.51 (Kết quả của Jin, Li và Wang, 2024)
**Mô hình.** MDP chiết khấu với tập trạng thái và tập hành động hữu hạn, trạng thái đầu cố định $s_0$, hàm mục tiêu $V(\theta)=v_{\pi_\theta}(s_0)$ (§2.1). Thuật toán được phân tích có hai thang thời gian (§3.1): vòng ngoài thứ $n$ đồng bộ chính sách cũ bằng tham số đầu vòng, $\theta_{n,1}$; vòng trong thực hiện một số cố định bước gradient trên cùng một ước lượng của mục tiêu cắt tính từ dữ liệu của chính sách cũ, không xáo mini-batch, không dùng Adam; lợi thế ước lượng bị cắt về đoạn có độ dài tỉ lệ với $\max\lvert r\rvert/(1-\gamma)$. Một dãy $\varphi_n$ chặn độ chệch của ước lượng ở vòng $n$; $\varphi_n=0$ khi ước lượng bằng Monte Carlo tới hết lượt.

**Giả thiết.**

- Giả thiết 3.1: $\pi_\theta(a\mid s)$ có gradient Lipschitz theo $\theta$, không đòi hàm điểm bị chặn.
- Giả thiết 3.2: phần thưởng bị chặn.
- Giả thiết 3.3: bước học vòng trong thỏa điều kiện kiểu Robbins–Monro, tổng vô hạn và tổng bình phương hữu hạn.
- Giả thiết 3.4: tổng bước học vô hạn và tổng bước học trong một vòng ngoài tiến về $0$.

**Kết luận.** Định lý 3.1 (tr. 7): dưới Giả thiết 3.1, 3.2, 3.4,
$$\begin{aligned}&\liminf_{n\to\infty}\lVert\nabla V(\theta_{n,1})\rVert^2\\&\quad\le C\,\sqrt{\lvert\mathcal A\rvert}\ \limsup_{n\to\infty}\varphi_n\\&\quad\text{hầu chắc chắn},\end{aligned}$$
với $C$ bằng $8$ lần một hằng số được xác định trong Bổ đề 3.1 của bài báo. Định lý 3.2 (tr. 8): thêm Giả thiết 3.3 và $\varphi_n=0$ từ một vòng nào đó thì $\nabla V(\theta_n)\to0$ hầu chắc chắn. Định lý 3.3 (tr. 9) cho tốc độ của trung bình có trọng số của $\mathbb E\lVert\nabla V\rVert^2$.

Chứng minh nằm ngoài phạm vi học phần. Ý tưởng: Bổ đề 3.1 của bài báo lập một bất đẳng thức đệ quy cho $V^*-V(\theta_{n,1})$, tương tự phân tích của phương pháp gradient ngẫu nhiên, trong đó các bước trong vòng được tách thành phần gradient đúng, phần sai số do cắt và do độ chệch $\varphi_n$, và một hiệu martingale; phân tích tỉ số và phép cắt là một bước trong chứng minh của bổ đề này, còn bảng ở trang 41 của bài giảng gốc xếp nó cùng hàng với các giả thiết.
:::

Khi $\varphi_n=0$ từ một vòng nào đó, Định lý 3.2 cho $\nabla V(\theta_n)\to0$ hầu chắc chắn. Khi $\varphi_n>0$, Định lý 3.1 chỉ nói về lim inf, tức có một dãy con với $\lVert\nabla V\rVert^2$ tiến vào khoảng $[0,\,C\sqrt{\lvert\mathcal A\rvert}\limsup\varphi_n]$. Bài báo không khẳng định dãy tham số hội tụ, và (§4) ghi rằng chưa biết có suy ra được tính tối ưu dưới các điều kiện này hay không.

Mô hình được phân tích khác PPO của Thuật toán 10.49 ở nhiều điểm: GAE với critic học được cho $\varphi_n>0$; Adam, xáo mini-batch và chuẩn hóa lợi thế nằm ngoài mô hình. Bài báo viết mục tiêu dưới dạng $\min\{\rho,\operatorname{clip}(\rho)\}\,\tilde A$, với phép $\min$ lấy trên tỉ số trước khi nhân với lợi thế, và trong Bổ đề 3.1 coi gradient bằng $0$ ngoài khoảng cắt ở cả hai phía, bất kể dấu của lợi thế; cả hai khác dạng theo dấu của Mệnh đề 10.40.

Như vậy, Định nghĩa 10.39 thay ràng buộc KL của TRPO bằng một mục tiêu cắt tối ưu được bằng phương pháp bậc một; Mệnh đề 10.40–10.41 cho biết mục tiêu đó là chặn dưới của hàm thay thế mẫu, trùng nó quanh $\theta_{\mathrm{old}}$, và có gradient bằng $0$ đúng trên các đoạn phẳng theo dấu. Định nghĩa 10.43 cho biến thể phạt KL với hệ số thích nghi. Định nghĩa 10.46 ghép actor, critic và entropy thành một hàm mất mát, Mệnh đề 10.48 cho một đại lượng chẩn đoán không âm, không chệch khi tham số không phụ thuộc mẫu, và Thuật toán 10.49 dùng lại mỗi đoạn thu trong $K$ epoch. Cái giá là không còn cận KL (Nhận xét 10.42), hành vi thực tế phụ thuộc chi tiết cài đặt (Nhận xét 10.50), và kết quả hội tụ hiện có chỉ nói về điểm dừng của một mô hình đơn giản hóa (Nhận xét 10.51). Trong Mục 7, chúng ta đặt các kết quả này cạnh giả thiết của chúng và trả lời bài toán trung tâm.

*Nguồn: bài giảng gốc lecture10_policy_gradient_part2.pdf (2025–2026), trang 19–42; Schulman và cộng sự (2017), §1–6, Bảng 1, 3, 5; Engstrom và cộng sự (2020), §3–6; Huang và cộng sự (2022); Jin, Li và Wang (2024), §2–4.*

---

## 7. Tổng kết và chuyển tiếp

<!-- note-topic-id: lec-10-topic-23 -->
### 7.1 Kết quả và giả thiết của bài

Bảng sau đặt mỗi kết quả chính cạnh giả thiết mà thiếu nó thì công thức sai nghĩa hoặc kết luận vượt quá điều đã chứng minh.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Đường cơ sở không làm chệch (Mệnh đề 10.2) | $b$ không phụ thuộc $A_t$ khi biết $H_t$; lượt sinh bởi $\pi_\theta$; (G1)–(G4) | $\mathbb E\bigl[\sum_t\gamma^t(G_t-b(S_t))\psi_t\bigr]=\nabla J$ |
| Đường cơ sở tối ưu (Mệnh đề 10.3) | một bước, $b$ hằng, $\mathbb E\lVert\psi\rVert^2>0$ | $b^*=\mathbb E[R\lVert\psi\rVert^2]/\mathbb E\lVert\psi\rVert^2$ |
| Gradient dạng lợi thế (Mệnh đề 10.5) | lợi thế và $\nu^\pi$ của chính $\pi_\theta$ | $\nabla J=\frac1{1-\gamma}\mathbb E_{\nu^\pi,\pi_\theta}[A_\pi\psi]$ |
| Sai số TD và lợi thế (Mệnh đề 10.8) | critic cố định; mặt nạ chỉ ở kết thúc; điều kiện theo $(S_t,A_t)$ | $\mathbb E[\delta_t\mid S_t,A_t]=A_\pi+\gamma\mathbb E[(1-Z_{t+1})e(S_{t+1})\mid S_t,A_t]-e(S_t)$ |
| Dạng tổng của GAE (Mệnh đề 10.14) | critic cố định trong lượt | $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$ |
| GAE và gradient (Mệnh đề 10.15) | $\lambda=1$ với lượt đầy đủ, hoặc $\hat v=v_\pi$ | $\mathbb E[\widehat A_t\psi_t]=\mathbb E[A_\pi\psi_t]$; không chệch cho lợi thế thì không |
| Hiệu hiệu năng (Bổ đề 10.19) | cùng $P$, cùng $\mu_0$; $\gamma<1$ | $J(\pi')-J(\pi)=\frac1{1-\gamma}\sum_s\nu^{\pi'}(s)A_\pi(s,\pi')$ |
| Khớp bậc một (Mệnh đề 10.22) | $\nu^{\mathrm{old}}$, $A_{\mathrm{old}}$ chính xác; $\pi_{\mathrm{old}}>0$ | $\mathcal L=J$ và $\nabla\mathcal L=\nabla J$ tại $\theta_{\mathrm{old}}$ |
| Chặn cải thiện (Định lý 10.26, Hệ quả 10.27) | như Bổ đề 10.19; $\gamma<1$; điều kiện hỗ trợ | $J'-J\ge[\mathcal L-J]-\frac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\mathbb E_\nu[D_{\mathrm{TV}}]$, hoặc $\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$ thay cho $\mathbb E_\nu[D_{\mathrm{TV}}]$ |
| Cải thiện đơn điệu (Hệ quả 10.29) | đánh giá và cực đại hóa chính xác | $J(\pi_{k+1})\ge\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)=J(\pi_k)$ |
| Bước miền tin cậy (Hệ quả 10.31) | nghiệm chính xác theo $\nu^{\pi_k}$ | $J_{k+1}-J_k\ge-\sqrt{2\kappa}\,\gamma\chi/(1-\gamma)^2$ |
| KL bậc hai (Mệnh đề 10.33) | $\nu^{\mathrm{old}}$ cố định; $\pi_\theta>0$, khả vi hai lần | $\bar D\approx\tfrac12\Delta^\top F\Delta$ |
| Gradient tự nhiên (Mệnh đề 10.34) | $g\in\operatorname{range}F$ | $\Delta^*=\sqrt{2\kappa/(g^\top F^+g)}\,F^+g$ |
| Mục tiêu cắt (Mệnh đề 10.40, 10.41) | lợi thế cố định; $\pi_{\mathrm{old}}>0$ | gradient $0$ trên $\{\widehat A>0,\rho>1+\epsilon\}\cup\{\widehat A<0,\rho<1-\epsilon\}$; $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, trùng quanh $\theta_{\mathrm{old}}$ |
| approxKL (Mệnh đề 10.48) | mẫu theo $\pi_{\mathrm{old}}$; $\theta$ không phụ thuộc mẫu; miền hỗ trợ của $\pi_\theta$ nằm trong miền hỗ trợ của $\pi_{\mathrm{old}}$, và $\pi_\theta>0$ trên miền hỗ trợ của $\pi_{\mathrm{old}}$ | $\mathbb E[(\rho-1)-\log\rho]=D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$, mỗi số hạng $\ge0$ |

Sáu hàng đầu thuộc nửa giảm phương sai của bài toán trung tâm, các hàng sau thuộc nửa giới hạn bước cập nhật.

### 7.2 So sánh bốn phương pháp

| Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng |
|---|---|---|---|
| REINFORCE có đường cơ sở (Thuật toán 10.6) | $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_t\gamma^t(G_t-\hat v(S_t,w_{\mathrm{old}}))\psi_t$; hồi quy $\hat v$ về $G_t$ | một lượt đầy đủ của $\pi_{\mathrm{old}}$, dùng một lần | sau $E$ lượt |
| Actor–critic một bước (Thuật toán 10.9) | $\theta\leftarrow\theta+\alpha_\theta I\delta\psi$; $w\leftarrow w+\alpha_w\delta\nabla_w\hat v$ | từng bước chuyển của chính sách hiện tại, dùng một lần | sau $E$ lượt |
| TRPO (Thuật toán 10.37) | bước $\sqrt{2\kappa/(x^\top Fx)}\,x$ với $x\approx F^{-1}g$, tìm kiếm lùi | $hN$ mẫu của $\pi_{\mathrm{old}}$, một bước cập nhật | sau số vòng lặp đã định |
| PPO (Thuật toán 10.49) | bước Adam trên $L(\theta,w)$ của mỗi mini-batch | $hN$ mẫu của $\pi_{\mathrm{old}}$, $K$ epoch | sau số vòng lặp; tùy chọn dừng sớm theo approxKL |

Không điều kiện dừng nào trong bảng là tiêu chuẩn hội tụ; cả bốn là ngân sách. Bảng sau ghi các kết luận có bảo đảm.

| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Lặp chính sách với $\mathcal M_k$ (Hệ quả 10.29) | lợi thế, $\nu^{\pi_k}$ và phép cực đại hóa chính xác | $J$ không giảm qua các vòng |
| Bài toán miền tin cậy (Hệ quả 10.31) | nghiệm chính xác theo $\nu^{\pi_k}$ | mức giảm của $J$ không quá $\sqrt{2\kappa}\gamma\chi/(1-\gamma)^2$ |
| PPO-Clip trong mô hình của Jin, Li và Wang (Nhận xét 10.51) | MDP hữu hạn; Giả thiết 3.1, 3.2, 3.4; mô hình hai thang không Adam, không mini-batch | $\liminf_n\lVert\nabla V(\theta_{n,1})\rVert^2\le C\sqrt{\lvert\mathcal A\rvert}\limsup_n\varphi_n$ hầu chắc chắn |

### 7.3 Trả lời bài toán trung tâm

Bài toán trung tâm có hai nửa: giảm phương sai của ước lượng gradient mà giữ kỳ vọng, và dùng lại dữ liệu của $\pi_{\mathrm{old}}$ cho một bước lớn mà chính sách mới không kém đi. Mỗi câu trả lời dưới đây đúng dưới một điều kiện.

1. Trừ một đường cơ sở không phụ thuộc hành động đã chọn giữ kỳ vọng và có thể giảm phương sai (Mệnh đề 10.2, 10.3); thay lợi tức bằng mục tiêu bootstrap của critic giảm số phần thưởng ngẫu nhiên trong ước lượng nhưng làm chệch khi critic sai (Định nghĩa 10.7, Mệnh đề 10.8).
2. GAE nối hai đầu bằng tham số $\lambda$, và chỉ bảo đảm gradient không chệch khi $\lambda=1$ với lượt đầy đủ hoặc khi critic đúng (Mệnh đề 10.14, 10.15).
3. Hàm thay thế đánh giá chính sách mới bằng dữ liệu cũ, đúng đến bậc một (Mệnh đề 10.22), với sai số bị chặn theo khoảng cách TV hoặc KL trung bình (Định lý 10.26, Hệ quả 10.27); bước miền tin cậy giải chính xác có mức giảm bị chặn (Hệ quả 10.31).
4. TRPO giải xấp xỉ bài toán miền tin cậy bằng gradient tự nhiên và gradient liên hợp, và chỉ bảo đảm KL trung bình mẫu không vượt $\kappa$ (Mệnh đề 10.34, Nhận xét 10.38).
5. PPO dùng lại mỗi đoạn thu trong $K$ epoch với một mục tiêu cắt là chặn dưới của hàm thay thế mẫu (Mệnh đề 10.41), hoặc với phạt KL có hệ số thích nghi (Định nghĩa 10.43), không có cận KL; kết quả hội tụ hiện có chỉ nói về điểm dừng trong một mô hình đơn giản hóa (Nhận xét 10.51).

*Nguồn: Sutton và Barto (2018), §13.4–13.5; Schulman và cộng sự (2015, 2016, 2017); Achiam và cộng sự (2017); Jin, Li và Wang (2024).*

### 7.4 Câu hỏi tự kiểm tra

Trả lời các câu hỏi sau và nêu kết quả đã dùng.

1. Vì sao $G_t-\hat v(S_t,w)$ cho ước lượng gradient không chệch với mọi critic cố định, nhưng là ước lượng chệch của lợi thế khi $\hat v\ne v_\pi$?
2. Trong bước nhỏ của Ví dụ 10.12, vì sao hàm thay thế cho đúng $\Delta J$, trong khi chặn cải thiện vẫn phạt?
3. Tỉ lệ cắt bằng $3/3$ có nghĩa mọi mẫu có gradient bằng $0$ không?
4. TRPO thực hành có bảo đảm $J$ không giảm không?

Lời giải ngắn.

1. Phần chệch $v_\pi(S_t)-\hat v(S_t,w)$ không phụ thuộc hành động nên bị khử khi nhân với hàm điểm (Mệnh đề 10.2), nhưng vẫn còn trong kỳ vọng có điều kiện của hệ số.
2. Bước chỉ đổi chính sách tại $s_B$, nên phân bố trạng thái không đổi và Bổ đề 10.19 trùng hàm thay thế; phạt của Định lý 10.26 không dùng thông tin này.
3. Không. Tỉ lệ cắt đếm $\lvert\rho-1\rvert>\epsilon$ bất kể dấu, còn tập gradient bằng $0$ phụ thuộc dấu của lợi thế (Mệnh đề 10.40(d), Định nghĩa 10.47).
4. Không. Bảo đảm đơn điệu cần đánh giá và cực đại hóa chính xác (Hệ quả 10.29), điều Thuật toán 10.37 không có (Nhận xét 10.38).

### 7.5 Bài tập theo mục

Mười hai bài tập củng cố của chương nằm ở mục "Bài tập củng cố" cuối tệp, theo ba mức, mỗi bài có gợi ý và lời giải.

| Mục | Bài tập |
|---|---|
| 2. Đường cơ sở, lợi thế, actor–critic | 10.1, 10.4, 10.5, 10.10 |
| 3. GAE | 10.6, 10.7 |
| 4. Hàm thay thế và chặn cải thiện | 10.11 |
| 5. TRPO và gradient tự nhiên | 10.8, 10.9 |
| 6. PPO | 10.2, 10.12 |
| Mục 4–6, các kết quả có bảo đảm | 10.3 |

<!-- note-topic-id: lec-10-topic-24 -->
### 7.6 Chuyển tiếp: Phần II và các biến thể mới

Phần II của bài giảng gốc (tr. 3) và hai biến thể mới của PPO, SPO (Xie, 2025) và SAM+PPO (Lee và Yoon, 2025), được trình bày ở [ghi chú Bài 11](material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-cac-phuong-phap-gradient-chinh-sach-nang-cao.html); khảo sát của Weng (2018) là tài liệu đọc chung cho cả hai bài. Bài 11 ký hiệu tỉ số chính sách $\rho_t(\theta)$ của chương này là $w_t$, và dùng chữ $\rho_t$ cho tỉ số giữa chính sách đích và chính sách hành vi khi dữ liệu khác chính sách.

Bài 11 giữ tỉ số và lợi thế của chương này, rồi thay lần lượt từng thành phần:

- mục tiêu tỉ số: SPO thay đoạn phẳng của phép cắt bằng một phạt bậc hai;
- bước tối ưu: SAM+PPO lấy gradient tại tham số bị nhiễu đối nghịch;
- nguồn dữ liệu và critic: A3C, A2C, gradient chính sách khác chính sách, ACER, IMPALA;
- chính sách tất định: DPG, DDPG, D4PG, MADDPG, TD3;
- hình học của bước và entropy trong mục tiêu: ACKTR, SAC.

Giới hạn còn lại của chương là dữ liệu theo chính sách: Mệnh đề 10.2 và 10.15 cần lượt do chính sách đang cập nhật sinh ra, và Thuật toán 10.49 bỏ mỗi đoạn thu sau $K$ epoch. Bài 11 xử lý giới hạn này ở các mục "Gradient chính sách khác chính sách", "DDPG và hợp đồng replay/target", "ACER và ACKTR" (phần ACER) và phần IMPALA của mục "SVPG, IMPALA và PPG", nơi bộ nhớ phát lại hoặc tỉ số với chính sách hành vi thay cho dữ liệu của $\pi_{\mathrm{old}}$.

---

## Tình huống áp dụng và ứng dụng

Tình huống 10.1 và 10.2 dùng số liệu sư phạm; Tình huống 10.3 dùng các số đo trong notebook thực hành thứ hai của Bài 09.

::: application Tình huống 10.1 (PPO trên CartPole: GAE ở bước cắt ngắn)
**Bài toán.** Huấn luyện PPO trên CartPole với giới hạn $500$ bước (Định nghĩa 08.6): mỗi bước giữ được cột cho phần thưởng $1$; $\gamma=0{,}99$, $\lambda=0{,}95$. Một lượt giữ cột đủ $500$ bước; critic cũ cho $\hat v_{\mathrm{old}}\equiv95$ ở mọi trạng thái của lượt, kể cả quan sát cuối. Giá trị đúng của chuỗi phần thưởng $1$ không kết thúc là $100$.

**Mô hình hóa.** Bộ đệm của Thuật toán 10.49 lưu các mảng $h\times N$ cho $R$, $Z$, $U$, $\hat v_{\mathrm{old}}$, cùng giá trị của quan sát cuối ở bước cắt. Lượt này kết thúc vì giới hạn thời gian, không vì MDP: $U_{500}=1$, $Z_{500}=0$.

**Kiểm giả thiết.** Thuật toán 10.16 cần $Z$ chỉ ghi kết thúc của MDP và giá trị bootstrap lấy ở quan sát cuối trước khi môi trường tự đặt lại: thỏa. Mệnh đề 10.15 không áp dụng: $\lambda=0{,}95<1$ loại (a), critic hằng $95$ khác $v_\pi$ loại (b), và lượt bị cắt ở bước $500$. Ước lượng gradient dùng GAE ở đây không có bảo đảm γ-just.

**Tính.** $\delta_{499}=1+0{,}99\cdot95-95=0{,}05$; vì $U_{500}=1$, $\widehat A_{499}=\delta_{499}=0{,}05$. Bước trước: $\delta_{498}=0{,}05$ và $\widehat A_{498}=0{,}05+0{,}99\cdot0{,}95\cdot0{,}05=0{,}0970$.

**Diễn giải.** Gần giới hạn thời gian, lợi thế ước lượng nhỏ và dương, giống mọi bước khác của lượt, nên các bước cuối không bị coi là thất bại. Critic nhận mục tiêu $V^{\mathrm{targ}}_{498}=95{,}097$, kéo nó về phía $100$.

**Giới hạn.** Trên một lần huấn luyện thật, $\hat v$ đổi theo trạng thái, nên $\widehat A_{498}$ phụ thuộc giá trị của critic tại hai quan sát cuối. Tình huống dùng Mệnh đề 10.14(c), bước 2–3 của Thuật toán 10.16 và Thuật toán 10.49.
:::

::: application Tình huống 10.2 (Vi phạm giả thiết: coi cắt ngắn là kết thúc)
**Bài toán.** Cùng dữ kiện với Tình huống 10.1: CartPole, giới hạn $500$ bước, phần thưởng $1$ mỗi bước, $\gamma=0{,}99$, $\lambda=0{,}95$, $\hat v_{\mathrm{old}}\equiv95$. Một bản cài đặt ghi $Z_{500}=1$ khi lượt chạm giới hạn thời gian.

**Kiểm giả thiết.** Giả thiết "$Z$ chỉ ghi kết thúc của MDP" của Định nghĩa 08.4 và Thuật toán 10.16 bị vi phạm, nên kết luận của Mệnh đề 10.8 và Thuật toán 10.16 không áp dụng: sai số TD ở bước cuối thiếu phần bootstrap.

**Tính.** $\delta_{499}=1-95=-94$, và $\widehat A_{498}=0{,}05+0{,}9405\cdot(-94)=-88{,}36$, so với $0{,}0970$ ở Tình huống 10.1.

**Hậu quả.** Mỗi hành động ở các bước gần giới hạn bị coi là dẫn tới kết thúc với giá trị $0$, nên actor giảm xác suất của chính những hành động đã giữ cột thành công, và critic học mục tiêu $1$ cho trạng thái cuối, sai lệch với các trạng thái giống hệt ở giữa lượt. Với cờ sai, thuật toán giải một MDP có kết thúc tại bước $500$.
:::

::: application Tình huống 10.3 (Breakout: đối chiếu notebook Bài 09)
**Bài toán.** Notebook thực hành thứ hai của Bài 09 (`thuc-hanh-double-dqn-reinforce-breakout.ipynb`, mục 8) cho kết quả sau $10^6$ bước. Với $\alpha=10^{-5}$, chính sách tham lam của hai lần chạy REINFORCE chọn sang phải ở mọi bước và đạt $2{,}43$ điểm; khi lấy mẫu, sang phải chiếm $63\%$ và $75\%$ số bước. Với $\alpha=10^{-4}$, entropy còn $0{,}006$ và điểm bằng $0$ ở mốc ghi đầu tiên. DQN và Double DQN đạt $42$–$66$ điểm ở bốn trong sáu lần chạy cùng ngân sách. Trên Breakout, phần thưởng thưa và nhiều lượt có $\widehat g=0$.

**Kiểm giả thiết.** Mệnh đề 10.2 cần (G1)–(G4), lượt sinh bởi $\pi_\theta$ và đường cơ sở không phụ thuộc hành động; một critic $\hat v(S_t,w)$ giữ cố định trong lượt thỏa điều kiện cuối. Tuy vậy, theo notebook (mục 9), (G1) không thỏa: mỗi lượt kết thúc khi mất một mạng, nên trạng thái đầu của các mạng sau phụ thuộc $\theta$; quan sát bốn khung chỉ gần Markov, và phần thưởng bị cắt về dấu. Mệnh đề 10.2 chỉ áp dụng cho bài toán đã lý tưởng hóa.

**Phân tích có điều kiện.** Đường cơ sở và critic giữ kỳ vọng của ước lượng (Mệnh đề 10.2) và có thể giảm phương sai (Mệnh đề 10.3); PPO (Thuật toán 10.49) cho dùng lại mỗi đoạn thu trong nhiều bước. Khi một lượt không có phần thưởng nào, mọi $G_t=0$, hệ số $G_t-\hat v(S_t,w)=-\hat v(S_t,w)$ chỉ phản ánh sai số của critic, và không công cụ nào của chương cung cấp thông tin về hành động dẫn tới phần thưởng. Số hạng entropy của Định nghĩa 10.46 chỉ ngăn chính sách trở nên tất định; trong notebook, với $\alpha=10^{-4}$, entropy sụp về $0{,}006$. Tìm ra phần thưởng là bài toán thăm dò, nằm ngoài phạm vi các kết quả trên.

**Giới hạn.** Các số $2{,}43$ và $42$–$66$ đo REINFORCE, DQN và Double DQN; để so PPO với chúng, cần chạy PPO với cùng ngân sách $10^6$ bước và cùng các lần chạy.
:::

**Ứng dụng.**

- Bài 11 dùng lợi thế và lợi tức $n$ bước trong A2C và A3C, dùng tỉ số với chính sách hành vi khi dữ liệu khác chính sách trong ACER và IMPALA, dùng ma trận Fisher trong ACKTR, và đưa entropy vào mục tiêu trong SAC.
- SPO ở Bài 11 thay mục tiêu cắt của Định nghĩa 10.39 bằng một mục tiêu tỉ số khác; SAM+PPO giữ mục tiêu cắt và đổi bước tối ưu, đánh giá gradient tại tham số bị nhiễu; cả hai giữ khung Thuật toán 10.49.

## Tóm tắt chương

Chúng ta bắt đầu từ hai giới hạn của REINFORCE: trên bài toán một bước, tổng phương sai của ước lượng tăng từ $\tfrac49$ lên $\tfrac{16}9$ khi cộng $1$ vào mọi phần thưởng (Ví dụ 10.1); trên hành lang ngắn, một lượt cho bước ngược chiều gradient (Ví dụ 10.2), và một bước lớn theo đúng gradient kéo $J$ từ $-12$ xuống $-21{,}32$. Trừ một đường cơ sở giữ kỳ vọng (Mệnh đề 10.2), với đường cơ sở tối ưu $b^*=1\ne v_\pi=2$ trên bài toán một bước (Mệnh đề 10.3). Critic đánh giá hành động qua mục tiêu bootstrap (Định nghĩa 10.7), với sai số TD có kỳ vọng có điều kiện bằng lợi thế khi critic đúng (Mệnh đề 10.8); GAE trộn các ước lượng $n$ bước bằng trọng số $(\gamma\lambda)^k$, không làm chệch gradient khi $\lambda=1$ với lượt đầy đủ hoặc khi critic đúng (Mệnh đề 10.14, 10.15). Trên chuỗi hai trạng thái, bổ đề hiệu hiệu năng cho $\Delta J=0{,}296$ còn hàm thay thế cho $0{,}26$ (Bổ đề 10.19, Mệnh đề 10.22); Định lý 10.26 chặn sai số này theo khoảng cách TV trung bình, dẫn tới bài toán miền tin cậy (Định nghĩa 10.30, Hệ quả 10.31). TRPO giải bài toán đó xấp xỉ bằng gradient tự nhiên và gradient liên hợp (Mệnh đề 10.34, Thuật toán 10.37); PPO thay ràng buộc bằng mục tiêu cắt, một chặn dưới của hàm thay thế mẫu (Mệnh đề 10.41, Thuật toán 10.49), hoặc bằng phạt KL với hệ số thích nghi (Định nghĩa 10.43). Không phương pháp thực hành nào giữ được bảo đảm đơn điệu; kết quả hội tụ hiện có cho PPO-Clip, trong một mô hình đơn giản hóa, cho gradient tiến về $0$ khi ước lượng lợi thế không chệch và chỉ cho cận của $\liminf\lVert\nabla V\rVert^2$ khi có độ chệch (Nhận xét 10.51). Bài 11 bỏ ràng buộc dữ liệu theo chính sách bằng gradient chính sách khác chính sách và bộ nhớ phát lại.

**Định nghĩa và kết quả theo mục.**

- Mục 2: Định nghĩa 10.1 (đường cơ sở), Mệnh đề 10.2 (không chệch), Mệnh đề 10.3 (đường cơ sở tối ưu), Định nghĩa 10.4 (lợi thế), Mệnh đề 10.5 (gradient dạng lợi thế), Thuật toán 10.6 (REINFORCE có đường cơ sở), Định nghĩa 10.7 (critic, actor, actor–critic), Mệnh đề 10.8 (sai số TD và lợi thế), Thuật toán 10.9 (actor–critic một bước), Nhận xét 10.10 (đường cơ sở và critic).
- Mục 3: Định nghĩa 10.11 (lợi tức $n$ bước), Bổ đề 10.12 (tổng sai số TD), Định nghĩa 10.13 (lợi tức λ, GAE), Mệnh đề 10.14 (dạng tổng, truy hồi), Mệnh đề 10.15 (γ-just), Thuật toán 10.16 (GAE trên đoạn thu), Nhận xét 10.17 (vai trò của $\gamma$, cắt ngắn).
- Mục 4: Định nghĩa 10.18 (phân bố chiếm dụng), Bổ đề 10.19 (hiệu hiệu năng), Hệ quả 10.20 (cải thiện cho chính sách ngẫu nhiên), Định nghĩa 10.21 (hàm thay thế), Mệnh đề 10.22 (khớp bậc một), Định nghĩa 10.23 (TV, KL), Mệnh đề 10.24 (KL không âm, Pinsker), Bổ đề 10.25 (dịch chuyển phân bố chiếm dụng), Định lý 10.26 (chặn cải thiện), Hệ quả 10.27 (chặn dạng KL), Nhận xét 10.28 (cận dạng lớn nhất), Hệ quả 10.29 (cải thiện đơn điệu), Định nghĩa 10.30 (miền tin cậy), Hệ quả 10.31 (mức giảm tối đa).
- Mục 5: Định nghĩa 10.32 (Fisher), Mệnh đề 10.33 (KL bậc hai), Mệnh đề 10.34 (gradient tự nhiên), Nhận xét 10.35 (Fisher suy biến), Thuật toán 10.36 (gradient liên hợp), Thuật toán 10.37 (TRPO), Nhận xét 10.38 (giả thiết bị vi phạm).
- Mục 6: Định nghĩa 10.39 (PPO-Clip), Mệnh đề 10.40 (dạng theo dấu), Mệnh đề 10.41 (chặn dưới bi quan), Nhận xét 10.42 (cắt tỉ số và KL), Định nghĩa 10.43 (PPO-Penalty), Nhận xét 10.44 (phạm vi của PPO-Penalty), Định nghĩa 10.45–10.47 (entropy, hàm mất mát, chẩn đoán), Mệnh đề 10.48 (approxKL), Thuật toán 10.49 (PPO), Nhận xét 10.50 (chi tiết cài đặt), Nhận xét 10.51 (hội tụ về điểm dừng).

**Công thức cần nhớ.**

$$
\begin{aligned}
&\widehat g_b=\textstyle\sum_{t=0}^{T-1}\gamma^t\bigl(G_t-b(S_t)\bigr)\psi_t,\\
&A_\pi(s,a)=q_\pi(s,a)-v_\pi(s),\\
&\delta_t=R_{t+1}\\
&\quad+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)\\
&\quad-\hat v(S_t,w),\\
&\widehat A_t=\delta_t\\
&\quad+\gamma\lambda(1-Z_{t+1})(1-U_{t+1})\widehat A_{t+1},\\
&J(\pi')-J(\pi)\\
&\quad=\tfrac1{1-\gamma}\textstyle\sum_s\nu^{\pi'}(s)A_\pi(s,\pi'),\\
&\mathcal L_{\theta_{\mathrm{old}}}(\theta)=J(\theta_{\mathrm{old}})\\
&\quad+\tfrac1{1-\gamma}\mathbb E_{\nu^{\mathrm{old}},\pi_{\mathrm{old}}}[\rho_\theta A_{\mathrm{old}}],\\
&J(\pi')-J(\pi)\\
&\quad\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\
&\quad\quad-\tfrac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}],\\
&\Delta^*=\sqrt{2\kappa/(g^\top F^{-1}g)}\,F^{-1}g,\\
&\ell^{\mathrm{CLIP}}_t=\min\bigl(\rho_t\widehat A_t,\\
&\quad\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\widehat A_t\bigr),\\
&L=-\mathcal L^{\mathrm{CLIP}}+c_1L^V\\
&\quad-c_2\widehat{\mathbb E}[\mathcal H],\\
&\text{approxKL}\\
&\quad=\tfrac1{\lvert\mathcal B\rvert}\textstyle\sum_{i\in\mathcal B}\bigl[(\rho_i-1)-\log\rho_i\bigr].
\end{aligned}
$$

**Giả thiết hay bị bỏ quên.**

- Đường cơ sở không được phụ thuộc hành động đã chọn.
- GAE không chệch cho gradient (γ-just) không có nghĩa là không chệch cho lợi thế.
- Kỳ vọng theo $\nu^\pi$ có chiết khấu khác trung bình đều trên bộ đệm.
- Cờ $Z$ chỉ ghi kết thúc của MDP, không ghi cắt ngắn.
- Hệ quả 10.29 và 10.31 cần đánh giá và tối ưu chính xác.
- Mục tiêu cắt không chặn KL giữa hai chính sách.
- approxKL không chệch chỉ khi tham số không phụ thuộc các mẫu dùng để tính nó.
- Điều kiện hỗ trợ có hai chiều: $\pi_\theta>0\Rightarrow\pi_{\mathrm{old}}>0$ cho hàm thay thế, và $\pi_\theta>0$ trên miền hỗ trợ của $\pi_{\mathrm{old}}$ cho KL hữu hạn.

---

## Bài tập củng cố

Các bài tập xếp theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Mỗi bài nêu lại đủ dữ kiện và có gợi ý, lời giải. Các bài phủ bảy mục tiêu học tập: mục tiêu 1 (Bài tập 10.1, 10.4), 2 (10.5, 10.10), 3 (10.6, 10.7), 4 (10.11), 5 (10.3, 10.8, 10.9, 10.11), 6 (10.2, 10.12), 7 (10.2, 10.3, 10.12).

### Mức nhận biết

::: exercise Bài tập 10.1 (Đường cơ sở hợp lệ)
Trong ước lượng $\widehat g_b=\sum_t\gamma^t(G_t-B_t)\psi_t$ trên một lượt sinh bởi $\pi_\theta$, xét bốn lựa chọn cho $B_t$:

- (a) $\hat v(S_t,w)$ với $w$ giữ cố định trong lượt;
- (b) trung bình $G_0$ của các lượt khác trong cùng batch, độc lập với lượt đang xét;
- (c) $B_t=r(A_t)$ trên bài toán một bước với $\pi_\theta=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$;
- (d) $B_t=G_t$ của chính lượt.

Xác định lựa chọn nào giữ $\mathbb E[\widehat g_b]=\nabla_\theta J$, và nêu kết quả đã dùng.
:::

::: hint
Kiểm điều kiện của Định nghĩa 10.1: khi biết $(H_t,B_t)$, hành động $A_t$ có còn phân phối $\pi_\theta(\cdot\mid S_t)$ không.
:::

::: solution
**Câu (a), (b).** Hợp lệ. $\hat v(S_t,w)$ là hàm của $H_t$; trung bình của các lượt khác độc lập với lượt đang xét. Trong cả hai trường hợp, khi biết $(H_t,B_t)$, $A_t$ vẫn có phân phối $\pi_\theta(\cdot\mid S_t)$, nên Mệnh đề 10.2 áp dụng.

**Câu (c).** Không hợp lệ: $G_0-B_0=r(A_0)-r(A_0)=0$ ở mọi lượt, nên $\widehat g_b\equiv0\ne(\tfrac23;\,-\tfrac23)$.

**Câu (d).** Không hợp lệ: $G_t-B_t=0$, nên $\widehat g_b\equiv0$; $G_t$ phụ thuộc $A_t$.

**Kiểm tra lại.** Lỗi thường gặp là dùng trung bình $G_0$ của cả batch, kể cả lượt đang xét; khi đó $B_t$ chứa phần thưởng đến sau $A_t$ của chính lượt đó.
:::

::: exercise Bài tập 10.2 (Dấu, cắt và gradient bằng 0)
Với $\epsilon=0{,}2$ và năm mẫu $(\widehat A;\,\rho)$: $(1;\,1{,}3)$, $(1;\,0{,}7)$, $(-1;\,1{,}3)$, $(-1;\,0{,}7)$, $(0{,}5;\,1{,}1)$, tính $\ell^{\mathrm{CLIP}}$ của từng mẫu, tỉ lệ cắt, và tỉ lệ mẫu có gradient bằng $0$.
:::

::: hint
Dùng dạng theo dấu của Mệnh đề 10.40 và định nghĩa tỉ lệ cắt của Định nghĩa 10.47.
:::

::: solution
**Số hạng cắt.** $1\cdot\min(1{,}3;\,1{,}2)=1{,}2$; $1\cdot\min(0{,}7;\,1{,}2)=0{,}7$; $-1\cdot\max(1{,}3;\,0{,}8)=-1{,}3$; $-1\cdot\max(0{,}7;\,0{,}8)=-0{,}8$; $0{,}5\cdot\min(1{,}1;\,1{,}2)=0{,}55$.

**Tỉ lệ cắt.** Bốn mẫu đầu có $\lvert\rho-1\rvert=0{,}3>0{,}2$, mẫu cuối có $0{,}1$: tỉ lệ $4/5$.

**Gradient bằng $0$.** Chỉ mẫu 1 ($\widehat A>0$, $\rho>1{,}2$) và mẫu 4 ($\widehat A<0$, $\rho<0{,}8$): tỉ lệ $2/5$.

**Kiểm tra lại.** Mẫu 2 và mẫu 3 bị đếm vào tỉ lệ cắt nhưng nằm ở phía bất lợi, nên vẫn có gradient; nhầm hai tỉ lệ là lỗi thường gặp.
:::

::: exercise Bài tập 10.3 (Điều gì được bảo đảm)
Phân loại đúng hoặc sai, nêu kết quả và giả thiết quyết định.

- (a) TRPO như Thuật toán 10.37 cải thiện $J$ đơn điệu.
- (b) Mỗi lần cập nhật PPO-Clip giữ KL trung bình giữa hai chính sách không vượt $\epsilon$.
- (c) Jin, Li và Wang (2024) chứng minh PPO như cài đặt thực hành hội tụ tới chính sách tối ưu.
- (d) Trong thí nghiệm của Engstrom và cộng sự (2020), PPO bỏ phép cắt nhưng giữ các tối ưu mức mã có thể đạt mức của PPO chuẩn.
:::

::: hint
Đối chiếu từng câu với Hệ quả 10.29, Nhận xét 10.38, 10.42, 10.50, 10.51.
:::

::: solution
**Câu (a).** Sai. Hệ quả 10.29 cần lợi thế, phân bố chiếm dụng và phép cực đại hóa chính xác; Thuật toán 10.37 dùng ước lượng, trung bình đều, xấp xỉ bậc hai và gradient liên hợp dừng sớm (Nhận xét 10.38).

**Câu (b).** Sai. Mục tiêu cắt không chặn KL; tỉ số có thể ra ngoài khoảng sau vài bước (Nhận xét 10.42).

**Câu (c).** Sai. Kết quả chỉ nói về gradient: khi $\varphi_n=0$ từ một vòng nào đó, $\nabla V(\theta_n)\to0$ (Định lý 3.2 của bài báo); khi có độ chệch $\varphi_n>0$, chỉ có cận cho lim inf của $\lVert\nabla V\rVert^2$ (Định lý 3.1). Cả hai cho một mô hình hai thang không có Adam và mini-batch (Nhận xét 10.51), và không nói về chính sách tối ưu.

**Câu (d).** Đúng, ở mức định tính và khi siêu tham số được tinh chỉnh đủ (Nhận xét 10.50).

**Kiểm tra lại.** Ở câu (b), $\epsilon$ là bán kính cắt của tỉ số; KL không xuất hiện trong mục tiêu cắt. Lỗi thường gặp là đọc $\epsilon$ như bán kính KL của TRPO.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 10.4 (Đường cơ sở tối ưu khi cộng hằng)
Bài toán một bước với $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$, phần thưởng $r=(4;\,1)$.

- (a) Tính tổng phương sai của $(r(A)-b)\psi_\theta(s,A)$ theo $b$.
- (b) Tìm $b^*$, so phương sai tại $b^*$ với tại $b=v_\pi(s)$ và $b=0$.
- (c) Chứng minh rằng với phần thưởng $r+c$, đường cơ sở tối ưu là $b^*(r)+c$ và phương sai tại đó không đổi.
:::

::: hint
Dùng $\operatorname{Var}(X_b)=\mathbb E\lVert X_b\rVert^2-\lVert g\rVert^2$ như chứng minh Mệnh đề 10.3, với $\lVert\psi_\theta(s,1)\rVert^2=\tfrac29$, $\lVert\psi_\theta(s,2)\rVert^2=\tfrac89$.
:::

::: solution
**Câu (a).** $\mathbb E\lVert X_b\rVert^2=\tfrac23(4-b)^2\tfrac29+\tfrac13(1-b)^2\tfrac89=\tfrac{4(4-b)^2+8(1-b)^2}{27}$ và $\lVert g\rVert^2=\tfrac89$. Khai triển: $\tfrac{12b^2-48b+72-24}{27}=\tfrac49(b-2)^2$.

**Câu (b).** $b^*=2$ với phương sai $0$; $v_\pi(s)=\tfrac23\cdot4+\tfrac13\cdot1=3$ cho $\tfrac49$; $b=0$ cho $\tfrac{16}9$.

**Câu (c).** Theo Mệnh đề 10.3, $b^*(r+c)=\mathbb E[(R+c)\lVert\psi\rVert^2]/\mathbb E\lVert\psi\rVert^2=b^*(r)+c$. Với $b=b^*(r)+c$, $X_b=(R+c-b^*(r)-c)\psi=(R-b^*(r))\psi$, cùng phân phối với trường hợp gốc, nên phương sai không đổi.

**Kiểm tra lại.** Với $r=(3;\,0)$, $b^*=1$; cộng $c=1$ cho $b^*=2$, khớp câu (b). Lỗi thường gặp là cho rằng $v_\pi(s)$ là đường cơ sở tối ưu.
:::

::: exercise Bài tập 10.5 (Độ chệch của sai số TD khi critic sai)
Chuỗi hai trạng thái: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_A=\tfrac12$, $p_B=\tfrac23$; $v_\pi=(1{,}4;\,2)$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$; $\psi_\theta(s_A,1)=0{,}5\,e_A$, $\psi_\theta(s_A,2)=-0{,}5\,e_A$. Critic cố định $\hat v=(1;\,1{,}5)$. Dùng Mệnh đề 10.8(b), tính $\mathbb E[\delta_0\mid s_A,a]$ cho hai hành động, và tọa độ $\theta_A$ của $\mathbb E[\delta_0\psi_0]$; so với giá trị đúng $0{,}2$.
:::

::: hint
$e=\hat v-v_\pi=(-0{,}4;\,-0{,}5)$; hành động 1 dẫn tới $s_B$ chắc chắn, hành động 2 dẫn tới trạng thái kết thúc, nơi $e=0$.
:::

::: solution
**Hành động 1.** Độ chệch $\gamma e(s_B)-e(s_A)=0{,}9\cdot(-0{,}5)+0{,}4=-0{,}05$, nên $\mathbb E[\delta_0\mid s_A,1]=0{,}4-0{,}05=0{,}35$.

**Hành động 2.** Độ chệch $0-e(s_A)=0{,}4$, nên $\mathbb E[\delta_0\mid s_A,2]=-0{,}4+0{,}4=0$.

**Gradient.** $\tfrac12\cdot0{,}35\cdot0{,}5+\tfrac12\cdot0\cdot(-0{,}5)=0{,}0875\ne0{,}2$.

**Kiểm tra lại.** Tính trực tiếp: $\delta_0=0+0{,}9\cdot1{,}5-1=0{,}35$ và $\delta_0=1-1=0$. Hai độ chệch khác nhau, nên không bị khử khi nhân với hàm điểm.
:::

::: exercise Bài tập 10.6 (Truy hồi của lợi tức λ và lợi tức λ cắt)
Cho critic cố định và $\lambda\in[0,1)$.

- (a) Từ Định nghĩa 10.11 và 10.13, chứng minh $G^\lambda_t=R_{t+1}+\gamma\bigl[(1-\lambda)\hat v(S_{t+1})+\lambda G^\lambda_{t+1}\bigr]$, với quy ước $G^\lambda_T=0$ và $\hat v(S_T)=0$ (Sutton và Barto, 2018, Bài tập 12.1).
- (b) Với lợi tức λ cắt tại $h$, $G^\lambda_{t:h}=(1-\lambda)\sum_{n=1}^{h-t-1}\lambda^{n-1}G_{t:t+n}+\lambda^{h-t-1}G_{t:h}$, chứng minh $G^\lambda_{t:h}=\hat v(S_t)+\sum_{i=t}^{h-1}(\gamma\lambda)^{i-t}\delta_i$ (Sutton và Barto, 2018, (12.10), Bài tập 12.5).
- (c) Kiểm câu (a) trên lượt của Ví dụ 10.8: $\gamma=0{,}9$, $\lambda=0{,}8$, $\hat v=(1;\,1{,}5)$, $R_1=0$, $R_2=3$, kết thúc tại $T=2$.
:::

::: hint
(a) Với $n\ge2$, $G_{t:t+n}=R_{t+1}+\gamma G_{t+1:t+n}$, cả khi lượt kết thúc trước $t+n$. (b) Lặp lại chứng minh của Mệnh đề 10.14 với $h$ ở vị trí của $T$.
:::

::: solution
**Câu (a).** Tách số hạng $n=1$, $G_{t:t+1}=R_{t+1}+\gamma\hat v(S_{t+1})$, và dùng $G_{t:t+n}=R_{t+1}+\gamma G_{t+1:t+n}$ với $n\ge2$:
$$
\begin{aligned}
&G^\lambda_t\\
&=(1-\lambda)\bigl[R_{t+1}+\gamma\hat v(S_{t+1})\bigr]\\
&\quad+(1-\lambda)\sum_{n\ge2}\lambda^{n-1}\bigl[R_{t+1}\\
&\qquad+\gamma G_{t+1:t+n}\bigr]\\
&=R_{t+1}+\gamma(1-\lambda)\hat v(S_{t+1})\\
&\quad+\gamma\lambda(1-\lambda)\\
&\qquad\times\sum_{m\ge1}\lambda^{m-1}G_{t+1:t+1+m}\\
&=R_{t+1}\\
&\quad+\gamma\bigl[(1-\lambda)\hat v(S_{t+1})\\
&\qquad+\lambda G^\lambda_{t+1}\bigr].
\end{aligned}
$$
Đẳng thức thứ hai dùng $(1-\lambda)\sum_{n\ge1}\lambda^{n-1}=1$ cho các số hạng $R_{t+1}$ và đổi chỉ số $m=n-1$. Khi $t+1=T$, mọi $G_{t:t+n}$ bằng $R_T$, khớp quy ước $\hat v(S_T)=G^\lambda_T=0$.

**Câu (b).** Giả sử $T>h$, nên $Z_{t+k}=0$ với $t+k\le h$. Nếu $T\le h$, thay $h$ bằng $T$; khi đó $G_{t:T}=G_t$ và kết quả là Mệnh đề 10.14(a). Với $1\le n\le h-t$, Bổ đề 10.12 áp dụng cho đoạn kết thúc ở $h$ cho $G_{t:t+n}-\hat v(S_t)=\sum_{k=0}^{n-1}\gamma^k\delta_{t+k}$. Các trọng số của $G^\lambda_{t:h}$ cộng bằng $1$, vì $(1-\lambda)\sum_{n=1}^{h-t-1}\lambda^{n-1}+\lambda^{h-t-1}=(1-\lambda^{h-t-1})+\lambda^{h-t-1}=1$. Do đó
$$
\begin{aligned}
&G^\lambda_{t:h}-\hat v(S_t)\\
&=(1-\lambda)\sum_{n=1}^{h-t-1}\lambda^{n-1}\\
&\quad\times\bigl(G_{t:t+n}-\hat v(S_t)\bigr)\\
&\quad+\lambda^{h-t-1}\bigl(G_{t:h}-\hat v(S_t)\bigr)\\
&=(1-\lambda)\sum_{n=1}^{h-t-1}\lambda^{n-1}\sum_{k=0}^{n-1}\gamma^k\delta_{t+k}\\
&\quad+\lambda^{h-t-1}\sum_{k=0}^{h-t-1}\gamma^k\delta_{t+k}\\
&=\sum_{k=0}^{h-t-1}\gamma^k\delta_{t+k}\\
&\quad\times\Bigl[(1-\lambda)\sum_{n=k+1}^{h-t-1}\lambda^{n-1}\\
&\qquad+\lambda^{h-t-1}\Bigr]\\
&=\sum_{k=0}^{h-t-1}(\gamma\lambda)^k\delta_{t+k}.
\end{aligned}
$$
Đẳng thức thứ nhất dùng tổng trọng số bằng $1$, đẳng thức thứ hai là Bổ đề 10.12, đẳng thức thứ ba đổi thứ tự hai tổng hữu hạn. Đẳng thức cuối dùng $(1-\lambda)\sum_{n=k+1}^{h-t-1}\lambda^{n-1}=\lambda^k-\lambda^{h-t-1}$, nên hệ số trong ngoặc vuông là $\lambda^k$; với $k=h-t-1$, tổng theo $n$ rỗng và hệ số là $\lambda^{h-t-1}=\lambda^k$. Khác tổng vô hạn của Mệnh đề 10.14, phần dư $\lambda^{h-t-1}$ ở đây đến từ lợi tức $n$ bước cuối $G_{t:h}$, bootstrap từ $\hat v(S_h)$.

**Câu (c).** $G^\lambda_1=3$, $G^\lambda_0=0+0{,}9(0{,}2\cdot1{,}5+0{,}8\cdot3)=2{,}43$, và $2{,}43-1=1{,}43=\delta_0+\gamma\lambda\delta_1$.

**Kiểm tra lại.** Lỗi thường gặp ở (a) là quên rằng phần dư $\lambda^{T-t-1}$ dồn vào lợi tức thực; ở (b) là dùng $\hat v$ đã cập nhật giữa các bước, khi đó các số hạng không triệt tiêu.
:::

::: exercise Bài tập 10.7 (GAE trên đoạn thu có cả cắt ngắn và kết thúc)
Một môi trường, đoạn bốn bước, $\gamma=0{,}9$, $\lambda=0{,}8$. Lượt thứ nhất gồm $t=0,1$ và bị cắt sau bước $1$: $U_2=1$, $Z_2=0$, quan sát cuối có $\hat v=4$. Lượt thứ hai bắt đầu ở $S_2$ và kết thúc sau bước $3$: $Z_4=1$. Các cờ còn lại bằng $0$. $R_{1:4}=(1;\,2;\,0;\,3)$ và $\hat v_{\mathrm{old}}(S_0),\dots,\hat v_{\mathrm{old}}(S_3)=(2;\,3;\,1;\,2)$. Tính $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$ bằng Thuật toán 10.16.
:::

::: hint
Ở bước $1$, giá trị kế là của quan sát cuối, không phải của $S_2$; truy hồi bị ngắt ở $U_2=1$ và ở $Z_4=1$.
:::

::: solution
**Sai số TD.** $\delta_0=1+0{,}9\cdot3-2=1{,}7$; $\delta_1=2+0{,}9\cdot4-3=2{,}6$; $\delta_2=0+0{,}9\cdot2-1=0{,}8$; $\delta_3=3-2=1$.

**Truy hồi lùi.** $\widehat A_3=1$; $\widehat A_2=0{,}8+0{,}72\cdot1=1{,}52$; $\widehat A_1=2{,}6$ vì $U_2=1$; $\widehat A_0=1{,}7+0{,}72\cdot2{,}6=3{,}572$.

**Mục tiêu critic.** $V^{\mathrm{targ}}=(5{,}572;\,5{,}6;\,2{,}52;\,3)$.

**Kiểm tra lại.** Hai lỗi thường gặp: bootstrap bằng $\hat v(S_2)=1$ của lượt mới cho $\delta_1=2+0{,}9-3=-0{,}1$; không ngắt truy hồi ở $U_2$ cho $\widehat A_1=2{,}6+0{,}72\cdot1{,}52=3{,}6944$. $\widehat A_0$ trùng Ví dụ 10.10(ii).
:::

::: exercise Bài tập 10.8 (Gradient liên hợp và bước TRPO)
Cho $F=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $g=(1;\,0)$, $\kappa=0{,}01$. Chạy Thuật toán 10.36 từ $x_0=0$ với quy ước $\tilde g_k=Fx_k-g$, tính số $\tau=x^\top Fx$ của thuật toán và bước $\Delta=\sqrt{2\kappa/\tau}\,x$, kiểm $\tfrac12\Delta^\top F\Delta$, và giải thích vì sao thuật toán dừng sau đúng hai vòng.
:::

::: hint
$\tilde g_0=-g$, $p_0=g$, $\omega_k=\tilde g_k^\top\tilde g_k/(p_k^\top Fp_k)$; các giá trị riêng của $F$ là $3$ và $1$.
:::

::: solution
**Vòng $0$.** $\tilde g_0=(-1;\,0)$, $p_0=(1;\,0)$, $Fp_0=(2;\,1)$, $\omega_0=\tfrac12$, $x_1=(0{,}5;\,0)$, $\tilde g_1=(-1;\,0)+\tfrac12(2;\,1)=(0;\,0{,}5)$.

**Vòng $1$.** $\xi_1=0{,}25$, $p_1=(0;\,-0{,}5)+0{,}25(1;\,0)=(0{,}25;\,-0{,}5)$, $Fp_1=(0;\,-0{,}75)$, $\omega_1=0{,}25/0{,}375=\tfrac23$, $x_2=(\tfrac23;\,-\tfrac13)$, $\tilde g_2=0$.

**Bước.** $\tau_2=\omega_0\tilde g_0^\top\tilde g_0+\omega_1\tilde g_1^\top\tilde g_1=\tfrac12\cdot1+\tfrac23\cdot0{,}25=\tfrac23$, bằng $x_2^\top Fx_2=g^\top x_2=\tfrac23$ vì $Fx_2=g$. Hệ số độ dài là $\sqrt{0{,}02/(2/3)}=\sqrt{0{,}03}=0{,}1732$, $\Delta=(0{,}1155;\,-0{,}0577)$, và $\tfrac12\Delta^\top F\Delta=0{,}01$.

**Số vòng.** $F$ có hai giá trị riêng phân biệt, nên theo Nocedal và Wright (2006, Định lý 5.4) gradient liên hợp dừng sau không quá hai vòng; $\tilde g_1=(0;\,0{,}5)\ne0$ nên thuật toán không dừng sau một vòng.

**Kiểm tra lại.** $Fx_2=(\tfrac43-\tfrac13;\,\tfrac23-\tfrac23)=(1;\,0)=g$. Lỗi thường gặp là đổi dấu phần dư giữa hai quy ước $Fx-g$ và $g-Fx$ giữa chừng.
:::

::: exercise Bài tập 10.9 (KL ngược có cùng Hessian)
Với các giả thiết của Mệnh đề 10.33, chứng minh rằng $\tilde D(\theta)=\sum_s\nu^{\mathrm{old}}(s)D_{\mathrm{KL}}(\pi_\theta(\cdot\mid s)\Vert\pi_{\mathrm{old}}(\cdot\mid s))$ có giá trị $0$, gradient $0$ và Hessian $F$ tại $\theta_{\mathrm{old}}$. Kiểm trên chính sách Bernoulli logit $p=\sigma(\theta)$ tại một trạng thái: Hessian bằng $p(1-p)$.
:::

::: hint
Viết $\tilde D=\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_\theta(a\mid s)\bigl[\log\pi_\theta(a\mid s)-\log\pi_{\mathrm{old}}(a\mid s)\bigr]$ và lấy đạo hàm theo quy tắc tích.
:::

::: solution
**Giá trị.** Tại $\theta_{\mathrm{old}}$, log-tỉ số bằng $0$.

**Gradient.** $\nabla\tilde D=\sum_s\nu^{\mathrm{old}}(s)\sum_a\nabla\pi_\theta\bigl[\log(\pi_\theta/\pi_{\mathrm{old}})+1\bigr]$. Tại $\theta_{\mathrm{old}}$, ngoặc vuông bằng $1$, nên $\nabla\tilde D=\sum_s\nu^{\mathrm{old}}(s)\nabla\sum_a\pi_\theta=0$.

**Hessian.** $\nabla^2\tilde D=\sum_s\nu^{\mathrm{old}}(s)\sum_a\bigl[\nabla^2\pi_\theta\bigl(\log(\pi_\theta/\pi_{\mathrm{old}})+1\bigr)+\nabla\pi_\theta\nabla\pi_\theta^\top/\pi_\theta\bigr]$. Tại $\theta_{\mathrm{old}}$: số hạng đầu là $\sum_s\nu^{\mathrm{old}}(s)\nabla^2\sum_a\pi_\theta=0$, số hạng sau là $\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}\psi\psi^\top=F$.

**Bernoulli.** $\psi=1-p$ với xác suất $p$, $\psi=-p$ với xác suất $1-p$, nên $F=p(1-p)^2+(1-p)p^2=p(1-p)$.

**Kiểm tra lại.** Tại $p=0{,}5$ và bước $+1$ trên logit, KL theo chiều ngược là $0{,}7311\log\frac{0{,}7311}{0{,}5}+0{,}2689\log\frac{0{,}2689}{0{,}5}=0{,}1110$, cùng bậc với $\tfrac12\cdot0{,}25=0{,}125$; hai chiều KL khác nhau ở bậc ba.
:::

### Mức vận dụng

::: exercise Bài tập 10.10 (Gradient dạng lợi thế trên hành lang ngắn)
Hành lang ngắn của Ví dụ 10.2: bốn ô, phần thưởng $-1$ mỗi bước, $\gamma=1$, hai hành động bị đảo ở $s_2$, $p=\tfrac12$ ở mọi ô, $v_\pi=(-12;\,-10;\,-6)$, $\psi_\theta(s,1)=(\tfrac12;\,-\tfrac12)$, $\psi_\theta(s,2)=(-\tfrac12;\,\tfrac12)$.

- (a) Tính $A_\pi(s,\cdot)$ tại ba ô.
- (b) Tính số lần thăm kỳ vọng $\eta(s)=\sum_t\Pr(S_t=s)$.
- (c) Tính tọa độ thứ nhất của $\nabla_\theta J=\sum_s\eta(s)\sum_a\pi(a\mid s)A_\pi(s,a)\psi_\theta(s,a)$ và so với $\nabla_\theta J=(2;\,-2)$ của Ví dụ 10.2.
- (d) Giải thích vì sao dùng $\eta$ chứ không dùng $\nu^\pi$, và vì sao Định lý 10.26 không áp dụng.
:::

::: hint
$q_\pi(s,a)=-1+v_\pi(\text{ô kế})$ với ô kế theo động lực của hành lang; $\eta$ thỏa $\eta=e_1+\eta P_\pi$ trên ba ô chưa kết thúc.
:::

::: solution
**Câu (a).** $s_1$: hành động 1 tới $s_2$, $q=-11$; hành động 2 đứng yên, $q=-13$; $A=(1;\,-1)$. $s_2$: hành động 1 về $s_1$, $q=-13$; hành động 2 tới $s_3$, $q=-7$; $A=(-3;\,3)$. $s_3$: hành động 1 tới đích, $q=-1$; hành động 2 về $s_2$, $q=-11$; $A=(5;\,-5)$.

**Câu (b).** Hệ $\eta_1=1+\tfrac12\eta_1+\tfrac12\eta_2$, $\eta_2=\tfrac12\eta_1+\tfrac12\eta_3$, $\eta_3=\tfrac12\eta_2$ cho $\eta=(6;\,4;\,2)$; tổng $12$ bằng độ dài lượt kỳ vọng.

**Câu (c).** Tại mỗi ô, $\sum_a\pi A\psi_1=\tfrac14\bigl(A(s,1)-A(s,2)\bigr)$: $0{,}5$; $-1{,}5$; $2{,}5$. Tọa độ thứ nhất là $6\cdot0{,}5+4\cdot(-1{,}5)+2\cdot2{,}5=2$, khớp.

**Câu (d).** Với $\gamma=1$, $\nu^\pi$ không xác định vì thừa số $1-\gamma=0$; dạng quỹ đạo của Mệnh đề 10.5(b) gom theo trạng thái cho trọng số $\eta$ không chuẩn hóa. Định lý 10.26 cần $\gamma<1$.

**Kiểm tra lại.** Mệnh đề 10.5(a) tại mỗi ô: $\tfrac12(1-1)=0$, $\tfrac12(-3+3)=0$, $\tfrac12(5-5)=0$.
:::

::: exercise Bài tập 10.11 (Đánh giá một bước cập nhật trên chuỗi hai trạng thái)
Chuỗi hai trạng thái của Ví dụ 10.6 với $\gamma=0{,}9$, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$, $J=1{,}4$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$, $\nu^\pi=(0{,}1;\,0{,}045)$. Chính sách đề xuất $\pi''$: $p''_A=0{,}55$, $p''_B=0{,}7$. Tính:

- (a) $J(\pi'')$ và $\Delta J$;
- (b) $\mathcal L-J$;
- (c) cận của Định lý 10.26;
- (d) KL trung bình theo chiều cũ‖mới, và xét xem $\pi''$ có thuộc miền tin cậy với $\kappa=0{,}001$ không;
- (e) phạt của Hệ quả 10.27.
:::

::: hint
$J=p_A\cdot0{,}9\cdot3p_B+(1-p_A)$; $A_\pi(s,\pi'')=\sum_a\pi''(a\mid s)A_\pi(s,a)$.
:::

::: solution
**Câu (a).** $J(\pi'')=0{,}55\cdot2{,}7\cdot0{,}7+0{,}45=1{,}4895$, $\Delta J=0{,}0895$.

**Câu (b).** $A_\pi(s_A,\pi'')=0{,}55\cdot0{,}4-0{,}45\cdot0{,}4=0{,}04$, $A_\pi(s_B,\pi'')=0{,}7-0{,}6=0{,}1$; $\mathcal L-J=10(0{,}1\cdot0{,}04+0{,}045\cdot0{,}1)=0{,}085$.

**Câu (c).** $D_{\mathrm{TV}}=(0{,}05;\,0{,}0333)$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}0065$, $\chi=0{,}1$; phạt $\tfrac{2\cdot0{,}9\cdot0{,}1}{0{,}01}\cdot0{,}0065=0{,}117$; cận $0{,}085-0{,}117=-0{,}032$.

**Câu (d).** KL theo trạng thái $0{,}005025$ và $0{,}002593$; $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}005025+0{,}045\cdot0{,}002593=0{,}000619\le0{,}001$: bước thuộc miền tin cậy, dù cận không chứng nhận cải thiện.

**Câu (e).** $18\sqrt{0{,}000619/2}=0{,}317$.

**Kiểm tra lại.** Bổ đề 10.19: $0{,}04+0{,}9\cdot0{,}55\cdot0{,}1=0{,}0895=\Delta J$. Bước thực sự cải thiện $J$; cận âm chỉ cho thấy nó bảo thủ.
:::

::: exercise Bài tập 10.12 (Kiểm một mini-batch PPO)
Cho $\epsilon=0{,}2$, bốn mẫu có $\log\rho=(0{,}1;\,-0{,}3;\,0{,}25;\,-0{,}05)$, $\widehat A=(2;\,-1;\,-1;\,0{,}5)$, và ngưỡng dừng sớm approxKL bằng $0{,}015$.

- (a) tính $\rho$, $\ell^{\mathrm{CLIP}}$ và $\mathcal L^{\mathrm{CLIP}}$;
- (b) tính tỉ lệ cắt và xác định các mẫu có gradient bằng $0$;
- (c) tính hai dạng approxKL và quyết định có dừng sớm không;
- (d) nếu thay mục tiêu cắt bằng PPO-Penalty với $\beta=1$, $\kappa_{\mathrm{targ}}=0{,}01$, và KL dạng đóng trung bình trên bộ đệm sau lần cập nhật là $0{,}018$, tính $\beta$ theo quy tắc của Định nghĩa 10.43; tính lại $\beta$ khi KL đó bằng $0{,}008$.
:::

::: hint
Dạng $-\log\rho$ trung bình có thể bằng $0$ dù chính sách đã đổi; dùng dạng $(\rho-1)-\log\rho$ của Định nghĩa 10.47. Ở (d), so KL với $\kappa_{\mathrm{targ}}/1{,}5$ và $1{,}5\,\kappa_{\mathrm{targ}}$.
:::

::: solution
**Câu (a).** $\rho=(1{,}1052;\,0{,}7408;\,1{,}2840;\,0{,}9512)$.

Các số hạng cắt là $2\min(1{,}1052;\,1{,}2)=2{,}2103$; $-\max(0{,}7408;\,0{,}8)=-0{,}8$; $-\max(1{,}2840;\,0{,}8)=-1{,}2840$; $0{,}5\cdot0{,}9512=0{,}4756$. $\mathcal L^{\mathrm{CLIP}}=0{,}1505$.

**Câu (b).** Mẫu 2 và 3 có $\lvert\rho-1\rvert>0{,}2$: tỉ lệ cắt $2/4$. Gradient bằng $0$ chỉ ở mẫu 2; mẫu 3 ở phía bất lợi.

**Câu (c).** Trung bình $-\log\rho=0$; trung bình $(\rho-1)-\log\rho=0{,}0203>0{,}015$, nên dừng sớm.

**Câu (d).** Hai ngưỡng là $0{,}01/1{,}5=0{,}00667$ và $1{,}5\cdot0{,}01=0{,}015$. KL $0{,}018>0{,}015$ cho $\beta=2$; KL $0{,}008$ nằm giữa hai ngưỡng nên giữ $\beta=1$.

**Kiểm tra lại.** Mọi số hạng $(\rho-1)-\log\rho$ đều không âm (Mệnh đề 10.48); dựa vào dạng $-\log\rho$ ở đây sẽ bỏ qua một bước đã đi xa. Ở (d), lỗi thường gặp là so KL trực tiếp với $\kappa_{\mathrm{targ}}$ thay cho hai ngưỡng.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

**Hướng dẫn đọc thêm.** Sutton và Barto (2018), §13.4–13.5, trình bày đường cơ sở và actor–critic một bước với hộp giả mã mà Thuật toán 10.6 và 10.9 dựa vào; §7.1 và §12.1–12.3 trình bày lợi tức $n$ bước và lợi tức λ, cơ sở của Mục 3. Các phần TRPO, GAE, PPO không có trong sách; đọc Schulman và cộng sự (2015, §2–3, Phụ lục C), (2016, §2–3) và (2017, §3–5). Chặn cải thiện dạng trung bình theo Achiam và cộng sự (2017, §5, phụ lục); chi tiết cài đặt theo Huang và cộng sự (2022) và Engstrom và cộng sự (2020).

**Tài liệu tham khảo.**

1. Tạ Việt Cường. *Lecture 10: Overview on Policy Gradient Algorithms, Part 1* (lecture10_policy_gradient_part2.pdf, 43 trang), học phần AIT3007, 2025–2026. Mục 1: tr. 3–4, 9–10, 14; Mục 2: tr. 5, 8, 11–13; Mục 3: tr. 13, 24; Mục 4: tr. 4, 14–16; Mục 5: tr. 17–19; Mục 6: tr. 19–42; Mục 7: tr. 2–3, 28, 43.
2. Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018. §7.1 (tr. 142–144, (7.1), Bài tập 7.1 tr. 143): Mục 3.1. §12.1 (tr. 288–291, (12.1)–(12.3), Hình 12.2, Bài tập 12.1 tr. 290), §12.2 (Bài tập 12.3 tr. 295), §12.3 (tr. 295–297, (12.9)–(12.10), Bài tập 12.5): Mục 3.2–3.3. §13.3 (tr. 326–329), §13.4 (tr. 329–331, (13.10)–(13.11), hộp tr. 330), §13.5 (tr. 331–332, (13.12)–(13.14), hộp tr. 332), ghi chú thư mục tr. 338: Mục 2.
3. Kakade, S., Langford, J. "Approximately Optimal Approximate Reinforcement Learning." *ICML* 2002, 267–274. Bổ đề 6.1: Bổ đề 10.19.
4. Kakade, S. "A Natural Policy Gradient." *NIPS* 14, 2002. Dẫn theo Schulman và cộng sự (2015, §7): Mục 5.1.
5. Schulman, J., Levine, S., Moritz, P., Jordan, M., Abbeel, P. "Trust Region Policy Optimization." *ICML* 2015 (arXiv 1502.05477). (1), (3), Định lý 1, §3 Thuật toán 1, (11)–(14), §5, §7, Phụ lục A–C: Mục 4–5.
6. Schulman, J., Moritz, P., Levine, S., Jordan, M., Abbeel, P. "High-Dimensional Continuous Control Using Generalized Advantage Estimation." *ICLR* 2016 (arXiv 1506.02438). §2 (6), Định nghĩa 1, Mệnh đề 1 (Phụ lục B), §3 (11)–(18): Mục 3; TRPO với GAE và critic: Thuật toán 10.37.
7. Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. "Proximal Policy Optimization Algorithms." arXiv 1707.06347, 2017. (6)–(9), §3–4, Thuật toán 1, Bảng 1, 3, 5: Mục 6.
8. Achiam, J., Held, D., Tamar, A., Abbeel, P. "Constrained Policy Optimization." *ICML* 2017. Định lý 1, Hệ quả 1, 3, Mệnh đề 1, (7), phụ lục Bổ đề 3: Mục 4.3–4.5.
9. Greensmith, E., Bartlett, P. L., Baxter, J. "Variance Reduction Techniques for Gradient Estimates in Reinforcement Learning." *JMLR* 5 (2004): 1471–1530. §5, Định lý 13 (tr. 1489–1490), Hệ quả 15 (tr. 1491–1492): Mục 2.2.
10. Nocedal, J., Wright, S. J. *Numerical Optimization*, ấn bản 2, Springer, 2006. Thuật toán 5.2 (tr. 112), Định lý 5.1 (tr. 103), Định lý 5.4 (tr. 115): Mục 5.2.
11. Cover, T. M., Thomas, J. A. *Elements of Information Theory*, ấn bản 2, Wiley, 2006. Bổ đề 11.6.1 (tr. 370): Mệnh đề 10.24(b).
12. Hunter, D. R., Lange, K. "A Tutorial on MM Algorithms." *The American Statistician* 58(1) (2004): 30–37. Dẫn theo Schulman và cộng sự (2015, §3): Mục 4.5.
13. Engstrom, L., Ilyas, A., Santurkar, S., Tsipras, D., Janoos, F., Rudolph, L., Madry, A. "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO." *ICLR* 2020. §3–6: Mục 6.1, 6.5.
14. Huang, S., Dossa, R. F. J., Raffin, A., Kanervisto, A., Wang, W. "The 37 Implementation Details of Proximal Policy Optimization." *ICLR Blog Track*, 2022: Mục 6.3–6.5.
15. Andrychowicz, M. và cộng sự. "What Matters in On-Policy Reinforcement Learning? A Large-Scale Empirical Study." *ICLR* 2021. Dẫn theo Huang và cộng sự (2022): Định nghĩa 10.46.
16. Jin, R., Li, S., Wang, B. "On Stationary Point Convergence of PPO-Clip." *ICLR* 2024. §2.1, §3.1–3.3, Giả thiết 3.1–3.4, Định lý 3.1–3.3: Mục 6.6.
17. Nota, C., Thomas, P. S. "Is the Policy Gradient a Gradient?" *AAMAS* 2020: Nhận xét 10.17.
18. Thomas, P. S., Brunskill, E. "Policy Gradient Methods for Reinforcement Learning with Function Approximation and Action-Dependent Baselines." arXiv 1706.06643, 2017. Dẫn theo ghi chú thư mục của Sutton và Barto (2018, tr. 338): Mục 2.1.
19. Weng, L. "Policy Gradient Algorithms." Blog, 2018: tài liệu đọc chung cho Bài 10 và Bài 11, Mục 7.6. Xie (2025), SPO; Lee và Yoon (2025), SAM+PPO: Mục 7.6, trình bày ở Bài 11.
