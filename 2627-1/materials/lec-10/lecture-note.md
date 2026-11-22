# Bài 10 — TRPO và PPO

## Mục tiêu học tập

Sau chương này, người học có thể:

1. **Đường cơ sở.** Chứng minh rằng trừ khỏi lợi tức một *đường cơ sở* (baseline) phụ thuộc trạng thái không làm chệch ước lượng gradient chính sách; tìm đường cơ sở hằng có phương sai nhỏ nhất trên bài toán một bước.
2. **Lợi thế và actor–critic.** Định nghĩa *hàm lợi thế* (advantage function), *critic* và *phương pháp actor–critic*; chứng minh rằng sai số sai phân thời gian (sai số TD) có kỳ vọng có điều kiện bằng lợi thế khi hàm giá trị đúng, và tính độ chệch khi hàm giá trị sai; tính bằng tay hai bước actor–critic một bước.
3. **Ước lượng lợi thế tổng quát.** Chứng minh rằng *ước lượng lợi thế tổng quát* (generalized advantage estimation, GAE) bằng tổng chiết khấu các sai số TD; phân biệt tính không chệch cho gradient với tính không chệch cho lợi thế; tính GAE trên một *đoạn thu* (rollout) có cờ kết thúc và cờ cắt ngắn.
4. **Chênh lệch hiệu năng và hàm thay thế.** Phân biệt phân phối hành động với phân bố trạng thái; phát biểu và chứng minh *bổ đề chênh lệch hiệu năng* (performance difference lemma); tính *hàm thay thế* (surrogate objective), so với mức thay đổi thật của hàm mục tiêu và giải thích vì sao sai số tăng theo bình phương độ dài bước; chứng minh hàm thay thế khớp hàm mục tiêu về giá trị và gradient tại tham số cũ.
5. **Miền tin cậy và gradient tự nhiên.** Lập bài toán *miền tin cậy* (trust region) và phát biểu *chặn cải thiện* cùng các giả thiết của nó; xấp xỉ *phân kỳ Kullback–Leibler* (Kullback–Leibler divergence, KL) bằng *ma trận thông tin Fisher* (Fisher information matrix); tính bằng tay bước *gradient tự nhiên* (natural gradient) và hai vòng *gradient liên hợp* (conjugate gradient) của phương pháp tối ưu chính sách miền tin cậy (Trust Region Policy Optimization, TRPO).
6. **Mục tiêu cắt và mục tiêu phạt của PPO.** Tính *mục tiêu cắt* (clipped objective) của phương pháp tối ưu chính sách gần kề (Proximal Policy Optimization, PPO) theo dấu của lợi thế; chứng minh mục tiêu cắt không vượt mục tiêu không cắt và trùng giá trị, gradient với nó tại tham số cũ; áp dụng quy tắc điều chỉnh hệ số phạt KL của *PPO-Penalty*.
7. **Một vòng PPO đầy đủ.** Mô tả một vòng PPO (thu đoạn, GAE, chuẩn hóa lợi thế, $K$ epoch) và phân biệt đại lượng giữ cố định với đại lượng tính lại; tính *approxKL* và *tỉ lệ cắt* (clip fraction) trên một mini-batch; chứng minh approxKL không chệch khi tham số không phụ thuộc mẫu; nêu phạm vi của kết quả hội tụ của *PPO-Clip*.

<!-- note-topic-id: lec-10-topic-01 -->
## Kiến thức tiên quyết

Số hiệu `03.k`, …, `09.k` chỉ khối trong ghi chú Bài 03–09. Bài tập 10.13–10.17 và 10.22 thuộc tệp bài tập `exercises.md` của Bài 10.

- **Tính Markov, giá trị hành động theo giá trị trạng thái** (Bổ đề 03.20, Mệnh đề 03.22, 03.23). Với chính sách Markov dừng $\pi$, khi biết lịch sử tới $S_t=s$ và $A_t=a$, phần tương lai của lượt chỉ phụ thuộc $(s,a)$, và lợi tức $G_t$ có kỳ vọng $q_\pi(s,a)$. Giá trị hành động và giá trị trạng thái liên hệ bởi
  $$\begin{aligned}&q_\pi(s,a)=r(s,a)\\&\quad+\gamma\sum_{s'}P(s'\mid s,a)\,v_\pi(s'),\\&v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a),\end{aligned}$$
  trong đó $r(s,a)$ là phần thưởng kỳ vọng của một bước và $v_\pi=0$ tại trạng thái kết thúc.
- **Dạng ma trận** (Định nghĩa 03.26, Định lý 03.28). Trên tập $\mathcal S=\{s_1,\dots,s_n\}$ các trạng thái chưa kết thúc, ma trận chuyển dưới $\pi$ là $(P_\pi)_{ss'}=\sum_a\pi(a\mid s)P(s'\mid s,a)$; mỗi hàng không âm và có tổng không quá $1$, phần còn thiếu là xác suất đi tới trạng thái kết thúc. Với $0\le\gamma<1$, ma trận $I-\gamma P_\pi$ khả nghịch và có khai triển $(I-\gamma P_\pi)^{-1}=\sum_{k\ge0}\gamma^kP_\pi^k$.
- **Cải thiện chính sách** (Định lý 04.13). Cho $\pi$ Markov dừng với giá trị chính xác $v_\pi$, và $\pi'$ Markov dừng xác định thỏa $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$. Khi đó (a) $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s$; (b) bất đẳng thức là nghiêm ngặt tại $s$ nếu điều kiện nghiêm ngặt tại $s$.
- **Sai số TD và cập nhật bán gradient** (Định nghĩa 05.20, Mệnh đề 05.27, Bài tập 05.14; Định nghĩa 07.19, 07.21, Thuật toán 07.22). Sai số TD (temporal-difference error) của hàm giá trị $V$ là $\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$, với $V=0$ tại trạng thái kết thúc; khi $V=v_\pi$, $\mathbb E_\pi[\delta_t\mid S_t=s]=0$. Nếu $V$ giữ cố định trong cả lượt thì $G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$. Với hàm giá trị tham số hóa $\hat v(s,w)$, cập nhật bán gradient (semi-gradient) $w\leftarrow w+\alpha\,\delta_t\nabla_w\hat v(S_t,w)$ coi mục tiêu $R_{t+1}+\gamma\hat v(S_{t+1},w)$ là hằng.
- **Tỉ số lấy mẫu quan trọng** (importance sampling ratio; Định nghĩa 06.24). Với chính sách đích $\pi$ và chính sách hành vi thỏa điều kiện hỗ trợ (mọi hành động có xác suất dương dưới $\pi$ cũng có xác suất dương dưới chính sách hành vi), tỉ số một bước là thương của xác suất chọn $A_t$ dưới $\pi$ và dưới chính sách hành vi. Trong chương này, chính sách hành vi luôn là chính sách $\pi_{\mathrm{old}}$ đã sinh dữ liệu, và chữ $b$ dành cho đường cơ sở.
- **Cờ kết thúc, cờ cắt ngắn, mất mát mini-batch, dừng gradient và bộ tối ưu** (Định nghĩa 08.4, 08.6, 08.10, 08.12, 08.16, 08.18). Cờ kết thúc (termination flag) $Z_{t+1}\in\{0,1\}$ bằng $1$ khi và chỉ khi quá trình quyết định Markov (Markov decision process, MDP) kết thúc tại bước $t+1$. Cờ cắt ngắn (truncation flag) $U_{t+1}\in\{0,1\}$ bằng $1$ khi việc thu thập dừng vì một giới hạn không thuộc MDP; mục tiêu bootstrap chỉ nhân với mặt nạ $(1-Z_{t+1})$. Phép dừng gradient (stop-gradient) $\operatorname{sg}$ giữ giá trị và cho đạo hàm $0$; hạ gradient ngẫu nhiên (stochastic gradient descent, SGD) và Adam cực tiểu hóa trung bình mất mát trên mini-batch.
- **Chính sách tham số hóa, softmax, hàm mục tiêu** (Định nghĩa 09.10, 09.11, 09.14). Chính sách tham số hóa $\pi_\theta(a\mid s)$ là một phân phối trên $\mathcal A$ với mỗi $s$, khả vi theo $\theta\in\mathbb R^d$. Chính sách softmax với đặc trưng $\phi(s,a)$ là $\pi_\theta(a\mid s)=\exp(\phi(s,a)^\top\theta)/\sum_{a'}\exp(\phi(s,a')^\top\theta)$. Hàm mục tiêu là $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ với $G_0=\sum_{t=0}^{T-1}\gamma^tR_{t+1}$, kỳ vọng lấy theo $S_0\sim\mu_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$ và động lực $P$.
- **Hàm điểm** (Định nghĩa 09.15, Mệnh đề 09.16, 09.17). Hàm điểm (score function) là $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$. Khi miền hỗ trợ của $\pi_\theta(\cdot\mid s)$ không phụ thuộc $\theta$, $\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}[c\,\psi_\theta(s,A)]=0$ với mọi $c$ không phụ thuộc $A$. Với softmax hai hành động, đặc trưng đơn vị và $p=\pi_\theta(1\mid s)$, ta có $\psi_\theta(s,1)=(1-p)(1;\,-1)$ và $\psi_\theta(s,2)=-p\,(1;\,-1)$.
- **Quỹ đạo, lịch sử, phần thưởng quá khứ** (Định nghĩa 09.20, Bổ đề 09.21, 09.22). Lịch sử $H_t=(S_0,A_0,R_1,\dots,R_t,S_t)$ gồm mọi thứ đã quan sát khi chọn $A_t$. Với quy ước $\psi_t=\psi_\theta(S_t,A_t)$ khi $t<T$ và $\psi_t=0$ khi $t\ge T$, ta có $\mathbb E[\psi_t\mid H_t]=0$, nên phần thưởng quá khứ $\sum_{k<t}\gamma^kR_{k+1}$ nhân $\psi_t$ có kỳ vọng $0$. Hai tính chất của kỳ vọng có điều kiện được dùng: tính chất tháp (tower property) $\mathbb E\bigl[\mathbb E[X\mid Y]\bigr]=\mathbb E[X]$, và $\mathbb E[WX\mid Y]=W\,\mathbb E[X\mid Y]$ khi $W$ là hàm của $Y$.
- **Định lý gradient chính sách** (Định lý 09.23, Hệ quả 09.24). Bốn giả thiết của định lý là:
  - (G1) phân phối đầu $\mu_0$ và động lực $P$ không phụ thuộc $\theta$, trạng thái có tính Markov;
  - (G2) với mọi $s$, $\pi_\theta(\cdot\mid s)$ khả vi theo $\theta$ và có miền hỗ trợ không đổi theo $\theta$;
  - (G3) $\lvert R_{t+1}\rvert\le R_{\max}$ và độ dài lượt $T\le T_{\max}$ hầu chắc chắn;
  - (G4) $\pi_\theta$ là chính sách softmax, hoặc Gaussian với phương sai cố định, có đặc trưng bị chặn.

  Dưới (G1)–(G4), gradient của hàm mục tiêu có hai dạng
  $$\begin{aligned}&\nabla_\theta J(\theta)\\&\quad=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_t\Bigr]\\&\quad=\frac1{1-\gamma}\,\mathbb E_{\substack{S\sim\nu^\pi\\A\sim\pi_\theta(\cdot\mid S)}}\bigl[q_\pi(S,A)\\&\qquad\times\psi_\theta(S,A)\bigr],\end{aligned}$$
  với $\pi=\pi_\theta$ và phân bố chiếm dụng chiết khấu (discounted occupancy distribution) $\nu^\pi(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi(S_t=s)$. Dạng thứ hai (Hệ quả 09.24) cần thêm MDP hữu hạn ($\mathcal S$ và $\mathcal A$ hữu hạn), chính sách Markov dừng và một trạng thái hấp thụ (absorbing state) sau khi lượt kết thúc, nơi $q_\pi=0$.
- **REINFORCE** (Thuật toán 09.25, Hệ quả 09.26, Nhận xét 09.27; Ví dụ 09.20, 09.21). REINFORCE thu một lượt bằng $\pi_{\theta_{\mathrm{old}}}$, tính $\widehat g=\sum_t\gamma^tG_t\psi_t$ tại $\theta_{\mathrm{old}}$ rồi cập nhật $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\widehat g$. Dưới (G1)–(G4), $\mathbb E[\widehat g\mid\theta_{\mathrm{old}}]=\nabla_\theta J(\theta_{\mathrm{old}})$. Bỏ trọng số $\gamma^t$ làm kỳ vọng của ước lượng khác $\nabla J$ khi $\gamma<1$.

## Bảng ký hiệu

Mỗi chữ giữ một nghĩa trong cả chương, trừ chữ $A$ và vài nghĩa cục bộ, nêu ngay sau bảng.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $S_t$; $\mathcal A$, $A_t$, $m$ | tập trạng thái chưa kết thúc, trạng thái ở bước $t$; tập hành động, hành động ở bước $t$, số hành động | hữu hạn trong các chứng minh dạng ma trận; $m\in\mathbb N_+$ |
| $R_{t+1}$, $r(s,a)$ | phần thưởng nhận sau $A_t$; phần thưởng kỳ vọng của cặp $(s,a)$ | $\mathbb R$, $\lvert R_{t+1}\rvert\le R_{\max}$ |
| $\gamma$, $T$, $G_t$ | hệ số chiết khấu; bước kết thúc của lượt; lợi tức từ bước $t$ | $[0,1)$ trong các định lý; biến ngẫu nhiên |
| $\mu_0$, $P(s'\mid s,a)$, $P_\pi$, $\Gamma_\pi$ | phân phối trạng thái đầu; xác suất chuyển; ma trận chuyển dưới $\pi$ trên $\mathcal S$; ma trận $(I-\gamma P_\pi)^{-1}$ | phân phối trên $\mathcal S$; $[0,1]$; $\mathbb R^{n\times n}$ |
| $\pi_\theta$, $\theta$, $d$; $\theta_{\mathrm{old}}$, $\pi_{\mathrm{old}}$; $\phi(s,a)$ | chính sách tham số hóa, tham số, số chiều; tham số và chính sách đã sinh dữ liệu; đặc trưng của chính sách softmax | $\theta\in\mathbb R^d$; $\mathbb R^d$ |
| $\operatorname{sg}$ | dừng gradient | toán tử trong đồ thị tính |
| $H_t$ | lịch sử $(S_0,A_0,R_1,\dots,R_t,S_t)$, đã biết khi chọn $A_t$ | dãy hữu hạn |
| $J(\theta)$, $\psi_\theta(s,a)$, $\psi_t$ | hàm mục tiêu; hàm điểm; viết gọn của $\psi_\theta(S_t,A_t)$, bằng $0$ khi $t\ge T$ | $\mathbb R$; $\mathbb R^d$ |
| $v_\pi$, $q_\pi$, $A_\pi$, $A_{\mathrm{old}}$; $A_\pi(s,\pi')$ | giá trị trạng thái, giá trị hành động, lợi thế $q_\pi-v_\pi$, lợi thế của $\pi_{\mathrm{old}}$; kỳ vọng của $A_\pi(s,A)$ khi $A\sim\pi'(\cdot\mid s)$ | hàm thực |
| $b(s)$ | đường cơ sở | $\mathcal S\to\mathbb R$, bị chặn |
| $\hat v(s,w)$, $w$, $w_{\mathrm{old}}$, $\hat v_{\mathrm{old}}$ | hàm giá trị tham số hóa (critic từ Mục 2.4); tham số của nó; tham số lúc thu dữ liệu; viết gọn của $\hat v(\cdot,w_{\mathrm{old}})$ | $\mathbb R$; $\mathbb R^{d'}$ |
| $\delta_t$ | sai số TD có mặt nạ $(1-Z_{t+1})$ | $\mathbb R$ |
| $G_{t:t+n}$, $\widehat A^{(n)}_t$, $G^\lambda_t$, $\widehat A_t$ | lợi tức $n$ bước, lợi thế $n$ bước, lợi tức λ (λ-return), ước lượng lợi thế (GAE ở Mục 3; lợi thế đưa vào mục tiêu cắt, có thể đã chuẩn hóa, từ Mục 6.3) | $\mathbb R$ |
| $\widehat A^{\mathrm{raw}}_t$, $V^{\mathrm{targ}}_t$ | lợi thế GAE trước chuẩn hóa; mục tiêu của critic $\widehat A^{\mathrm{raw}}_t+\hat v_{\mathrm{old}}(S_t)$ | $\mathbb R$ |
| $\lambda$ | tham số của GAE | $[0,1]$ |
| $Z_{t+1}$, $U_{t+1}$ | cờ kết thúc của MDP, cờ cắt ngắn | $\{0,1\}$ |
| $\nu^\pi$, $\nu^{\mathrm{old}}$, $\eta_\pi(s)$ | phân bố chiếm dụng chiết khấu chuẩn hóa, xét trên $\mathcal S$; viết gọn của $\nu^{\pi_{\mathrm{old}}}$; $\eta_\pi(s)=\sum_t\gamma^t\Pr_\pi(S_t=s,\,t<T)$, số lần thăm có chiết khấu (kỳ vọng, không chuẩn hóa), bằng $\nu^\pi(s)/(1-\gamma)$ khi $\gamma<1$ và xác định cả khi $\gamma=1$ nếu $\mathbb E[T]<\infty$; viết $\eta(s)$ khi chính sách đã rõ | khối $\nu^\pi(\mathcal S)\le1$; $[0,\infty)$ |
| $\rho_\theta(s,a)$, $\rho_t(\theta)$ | tỉ số chính sách $\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$; giá trị tại mẫu, $\rho_\theta(S_t,A_t)$ | $[0,\infty)$ |
| $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$, $\mathcal L_\pi(\pi')$, $\mathcal L^{\mathrm{CPI}}$, $\mathcal L^{\mathrm{CLIP}}$, $\ell^{\mathrm{CLIP}}_t$ | hàm thay thế, viết theo tham số hoặc theo chính sách (cùng một đại lượng với $\pi=\pi_{\theta_{\mathrm{old}}}$, $\pi'=\pi_\theta$); hai hàm thay thế mẫu trên dữ liệu; số hạng cắt của một mẫu (đều được cực đại hóa) | $\mathbb R$ |
| $L(\theta,w)$, $L^V$ | hàm mất mát tổng và mất mát giá trị (đều được cực tiểu hóa) | $\mathbb R$ |
| $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$, $\widehat D$, $\mathcal H$ | biến phân toàn phần, KL tại một trạng thái, KL trung bình (kỳ vọng của KL theo phân bố chiếm dụng), KL trung bình trên bộ đệm, entropy | $[0,1]$; $[0,\infty]$ |
| $\kappa$, $\kappa_{\mathrm{targ}}$; $\chi_{\pi'}$, $\bar\chi$ | bán kính miền tin cậy; KL mục tiêu của PPO-Penalty; hai hằng của chặn cải thiện | $(0,\infty)$; $[0,\infty)$ |
| $F$, $g$, $\Delta$ | ma trận Fisher; gradient của hàm thay thế tại $\theta_{\mathrm{old}}$; bước $\theta-\theta_{\mathrm{old}}$ | $\mathbb R^{d\times d}$; $\mathbb R^d$; $\mathbb R^d$ |
| $\epsilon$, $\beta$, $c_1$, $c_2$ | bán kính cắt; hệ số phạt KL theo $\pi_{\mathrm{old}}$ (Mục 6.2); hai trọng số mất mát | $(0,1)$; $(0,\infty)$; $[0,\infty)$ |
| $N$, $h$, $K$, $M$, $E$; $\mathcal D$, $\mathcal B$, $\widehat{\mathbb E}_{\mathcal D}$ | số môi trường, độ dài đoạn thu, số epoch, cỡ mini-batch, số lượt của Thuật toán 10.6 và 10.9; bộ đệm $hN$ mẫu, tập chỉ số của một mini-batch, trung bình đều trên bộ đệm | $\mathbb N_+$; tập |
| $\alpha$, $\alpha_\theta$, $\alpha_w$ | bước học | $(0,\infty)$ |
| $\sigma$ | hàm logistic $\sigma(z)=1/(1+e^{-z})$ | $\mathbb R\to(0,1)$ |

Quy ước đọc bảng gồm các điểm sau.

- $R_{t+1}$ gắn với chuyển từ bước $t$ sang bước $t+1$. Sau bước kết thúc $T$, lượt ở trong một trạng thái hấp thụ có phần thưởng $0$, nên $G_T=0$ và mọi giá trị, lợi thế tại đó bằng $0$. Ký hiệu $\log$ chỉ logarit tự nhiên. Khi tọa độ của véc-tơ có dấu phẩy thập phân, các tọa độ được ngăn bằng dấu chấm phẩy, như $(0{,}2;\,0{,}3)$.
- Chữ $A$ có hai vai. $A_t$, có chỉ số thời gian, là hành động; $A_\pi$, có chỉ số chính sách, và $\widehat A_t$, có dấu mũ, là lợi thế. Hai vai luôn được phân biệt bằng chỉ số hoặc dấu mũ, như trong $A_\pi(S_t,A_t)$.
- Một số chữ có thêm một nghĩa cục bộ, nêu tại khối dùng nó:
  - $e_A$, $e_B$, $e_s$ là véc-tơ đơn vị, còn $e(s)=\hat v(s,w)-v_\pi(s)$ là sai số critic (Mệnh đề 10.8, Bài tập 10.5);
  - $I$ là ma trận đơn vị, còn trong Thuật toán 10.9 là thừa số $\gamma^t$;
  - $p$, $p_A$, $p_B$ là xác suất chọn hành động 1 trong các ví dụ hai hành động, còn $p_k$ là hướng liên hợp của Thuật toán 10.36;
  - $n$ là số trạng thái, số bước của lợi tức $n$ bước, và là hình chiếu trong chứng minh Mệnh đề 10.34;
  - $x_k$, $y_k$ là bước lặp và tích $Fp_k$ của Thuật toán 10.36, $x$ trong $\langle x,f\rangle$ là vector của chứng minh Định lý 10.27, $\sigma(x)$ ở Ví dụ 10.2 có biến $x$ thực, và $y_t$ là mục tiêu $V^{\mathrm{targ}}_t$ ở Định nghĩa 10.47;
  - $\Delta J$, $\Delta\mathcal L$, $\Delta p$, $\Delta_P$, $\Delta_\pi$ là các hiệu, khác bước $\Delta$;
  - $V$, $V'$, $C_k$ là ký hiệu cục bộ của Thuật toán 10.16 và Hệ quả 10.30, còn $V(\theta)$, $C$, $n$ trong Nhận xét 10.51 theo ký hiệu của bài báo được dẫn.
- Kỳ vọng $\mathbb E_{S\sim\nu^\pi}$ có trọng số chiết khấu $(1-\gamma)\gamma^t$ theo thời điểm thăm. Ký hiệu $\widehat{\mathbb E}_{\mathcal D}$ chỉ trung bình đều trên các mẫu của một bộ đệm $\mathcal D$, một đại lượng tính từ mẫu hữu hạn.
- Bài 09 viết phân phối đầu là $\rho_0$; ở đây viết $\mu_0$ vì chữ $\rho$ dành cho tỉ số chính sách. Sutton và Barto (2018, Chương 13) viết chính sách là $\pi(a\mid s,\boldsymbol\theta)$ và hai bước học là $\alpha^{\boldsymbol\theta}$, $\alpha^{\mathbf w}$; ở đây viết $\pi_\theta(a\mid s)$, $\alpha_\theta$, $\alpha_w$, còn $\hat v(s,w)$ giữ nguyên.
- Ký hiệu của các bài báo: $\rho_\pi$ của Schulman và cộng sự (2015) là $\eta$, bán kính $\delta$ là $\kappa$; tỉ số $r_t(\theta)$ của Schulman và cộng sự (2017) là $\rho_t(\theta)$, độ dài đoạn $T$ là $h$; phần thưởng $r_t$ là $R_{t+1}$.
- Ứng với giáo trình *Học máy thống kê*: $v_\pi$, $q_\pi$ là $V^\pi$, $Q^\pi$.

---

## 1. Hai giới hạn của REINFORCE

<!-- note-topic-id: lec-10-topic-02 -->
### 1.1 Kết quả kế thừa và bài toán trung tâm

Bài 09 kết thúc với thuật toán REINFORCE (Thuật toán 09.25). Thuật toán thu một lượt bằng chính sách $\pi_{\theta_{\mathrm{old}}}$, tính lợi tức $G_t$ của từng bước, rồi cập nhật tham số theo ước lượng
$$\widehat g=\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_{\theta_{\mathrm{old}}}(S_t,A_t).$$
Mỗi hàm điểm được nhân với lợi tức đến sau nó và với trọng số chiết khấu $\gamma^t$. Dưới các giả thiết (G1)–(G4) của Định lý 09.23, Hệ quả 09.26 cho $\mathbb E[\widehat g\mid\theta_{\mathrm{old}}]=\nabla_\theta J(\theta_{\mathrm{old}})$, nghĩa là mỗi lượt cho một mẫu không chệch của gradient; Ví dụ 09.21 cho thấy bỏ trọng số $\gamma^t$ làm mất tính chất này khi $\gamma<1$. Tính không chệch là một khẳng định về kỳ vọng theo phân phối của lượt. Hai ví dụ sau đo điều xảy ra trên từng lượt.

![Thẻ dữ kiện bài toán một bước, chính sách softmax, hai hành động: bảng hai cột cho a bằng 1 và a bằng 2, đặc trưng phi của s, a bằng (1; 0) và (0; 1); xác suất pi theta bằng 2/3 và 1/3; phần thưởng r bằng 3 và 0. Dòng dưới: theta bằng (log 2; 0), lượt dừng sau A 0.](img/lec-09/one-step-card.svg)

::: example Ví dụ 10.1 (Phương sai của REINFORCE trên bài toán một bước)
**Dữ kiện.** Một trạng thái $s$, hai hành động, lượt dừng sau hành động đầu tiên. Chính sách softmax với đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$ và $\theta=(\log2;\,0)$, nên $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$. Phần thưởng $r(1)=3$, $r(2)=0$. Hàm điểm $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$ (Mệnh đề 09.16). Vì $T=1$, ước lượng REINFORCE là $\widehat g=G_0\,\psi_\theta(s,A_0)$ với $G_0=r(A_0)$.

**Phân phối của $\widehat g$.** Với xác suất $\tfrac23$, $A_0=1$ và $\widehat g=3\,(\tfrac13;\,-\tfrac13)=(1;\,-1)$. Với xác suất $\tfrac13$, $A_0=2$ và $\widehat g=(0;\,0)$. Kỳ vọng là $\tfrac23(1;\,-1)=(\tfrac23;\,-\tfrac23)$, bằng gradient đúng $\nabla_\theta J$.

**Phương sai.** Ta đo phương sai của một véc-tơ ngẫu nhiên $X$ bằng tổng phương sai các tọa độ, $\operatorname{Var}(X)=\mathbb E\lVert X-\mathbb EX\rVert^2$. Mỗi tọa độ của $\widehat g$ có mô men bậc hai $\tfrac23\cdot1=\tfrac23$ và phương sai $\tfrac23-\tfrac49=\tfrac29$, nên $\operatorname{Var}(\widehat g)=\tfrac49$.

**Cộng một hằng vào phần thưởng.** Với $r=(4;\,1)$, $\widehat g=4\,(\tfrac13;\,-\tfrac13)=(\tfrac43;\,-\tfrac43)$ với xác suất $\tfrac23$ và $\widehat g=(-\tfrac23;\,\tfrac23)$ với xác suất $\tfrac13$. Tọa độ thứ nhất có kỳ vọng $\tfrac23\cdot\tfrac43-\tfrac13\cdot\tfrac23=\tfrac23$, nên gradient không đổi. Mô men bậc hai của mỗi tọa độ là $\tfrac23\cdot\tfrac{16}9+\tfrac13\cdot\tfrac49=\tfrac43$, phương sai là $\tfrac43-\tfrac49=\tfrac89$, và $\operatorname{Var}(\widehat g)=\tfrac{16}9$.

**Diễn giải.** Trên bài toán một bước, cộng $1$ vào phần thưởng làm $J$ tăng đúng $1$ với mọi $\theta$, nên giữ nguyên gradient và chính sách tốt nhất; tổng phương sai thì tăng gấp bốn. Phương sai của REINFORCE vì vậy phụ thuộc vào mức chung của phần thưởng, một đại lượng không ảnh hưởng tới việc chọn hành động.

**Kiểm tra lại.** $\operatorname{Var}(\widehat g)=\mathbb E\lVert\widehat g\rVert^2-\lVert\nabla_\theta J\rVert^2$. Với $r=(3;\,0)$: $\tfrac23\cdot2-\tfrac89=\tfrac49$. Với $r=(4;\,1)$: $\tfrac23\cdot\tfrac{32}9+\tfrac13\cdot\tfrac89-\tfrac89=\tfrac{64+8-24}{27}=\tfrac{16}9$.
:::

Ví dụ sau cho thấy hậu quả của phương sai lớn trên từng lượt: mỗi lượt cho một hướng cập nhật khác, và có lượt cho hướng ngược chiều gradient.

::: example Ví dụ 10.2 (Ba lượt REINFORCE trên hành lang ngắn)
**Dữ kiện.** Hành lang ngắn đảo hành động (Sutton và Barto, 2018, Ví dụ 13.1): bốn ô $s_1$ (xuất phát), $s_2$, $s_3$, $s_4$ (đích, kết thúc lượt); phần thưởng $-1$ mỗi bước; $\gamma=1$. Hành động 1 là "sang phải", hành động 2 là "sang trái"; ở $s_2$ hai hành động bị đảo; sang trái tại $s_1$ thì đứng yên. Mọi ô có cùng đặc trưng $\phi(s,1)=(1;\,0)$, $\phi(s,2)=(0;\,1)$, nên chính sách softmax chọn hành động 1 với cùng xác suất $p=\pi_\theta(1\mid s)=\sigma(\theta_1-\theta_2)$ ở mọi ô, với hàm logistic $\sigma(x)=1/(1+e^{-x})$. Tại $\theta=(0;\,0)$: $p=\tfrac12$, $\psi_\theta(s,1)=(\tfrac12;\,-\tfrac12)$, $\psi_\theta(s,2)=(-\tfrac12;\,\tfrac12)$. Bước học $\alpha=0{,}1$.

**Hàm mục tiêu.** Viết $v_i=v_\pi(s_i)$ với $i=1,2,3$; đích có giá trị $0$. Theo động lực của hành lang, tại $s_1$ hành động 1 tới $s_2$ và hành động 2 đứng yên; tại $s_2$ hành động 1 về $s_1$ và hành động 2 tới $s_3$; tại $s_3$ hành động 1 tới đích và hành động 2 về $s_2$. Với phần thưởng $-1$ và $\gamma=1$, Mệnh đề 03.22 và 03.23 cho hệ
$$\begin{aligned}v_1&=-1+p\,v_2+(1-p)\,v_1,\\v_2&=-1+p\,v_1+(1-p)\,v_3,\\v_3&=-1+(1-p)\,v_2.\end{aligned}$$
Ta khử từng ẩn.

- Phương trình thứ nhất cho $p\,v_1=-1+p\,v_2$, tức $v_1=v_2-\tfrac1p$.
- Phương trình thứ ba cho $v_3$ theo $v_2$: $v_3=-1+(1-p)\,v_2$.
- Thế hai biểu thức vào phương trình thứ hai: $v_2=-1+p\,v_2-1-(1-p)+(1-p)^2v_2$, tức $\bigl[1-p-(1-p)^2\bigr]v_2=-(3-p)$.
- Vì $1-p-(1-p)^2=(1-p)\bigl(1-(1-p)\bigr)=p(1-p)$, ta được $v_2=-\dfrac{3-p}{p(1-p)}$.
- Lượt xuất phát từ $s_1$, nên $J(p)=v_1=v_2-\tfrac1p$.

Do đó
$$\begin{aligned}J(p)&=-\frac{(3-p)+(1-p)}{p(1-p)}\\&=-\frac{2(2-p)}{p(1-p)}.\end{aligned}$$

Tại $p=\tfrac12$: $v_2=-2{,}5/0{,}25=-10$, $v_1=J(\tfrac12)=-12$ và $v_3=-1+\tfrac12\cdot(-10)=-6$.

**Gradient đúng.** Đặt $N(p)=2-p$ và $D(p)=p(1-p)$, nên $J=-2N/D$ và
$$\begin{aligned}J'(p)&=-2\,\frac{N'D-ND'}{D^2}\\&=2\,\frac{D+N(1-2p)}{D^2}.\end{aligned}$$
Tại $p=\tfrac12$: $1-2p=0$ và $D=\tfrac14$, nên $J'(\tfrac12)=2\cdot\tfrac14\big/\tfrac1{16}=8$. Vì $p=\sigma(\theta_1-\theta_2)$ và $\sigma'=\sigma(1-\sigma)$, ta có $\partial p/\partial\theta_1=-\partial p/\partial\theta_2=p(1-p)=\tfrac14$; quy tắc dây chuyền cho $\nabla_\theta J=J'(\tfrac12)\cdot\tfrac14\cdot(1;\,-1)=(2;\,-2)$.

**Giá trị tốt nhất.** $J'(p)=0$ khi $D+N(1-2p)=p(1-p)+(2-p)(1-2p)=p^2-4p+2=0$. Nghiệm trong $(0,1)$ là $p^*=2-\sqrt2\approx0{,}586$, với $J(p^*)\approx-11{,}66$. Vì $J(p)\to-\infty$ khi $p\to0$ và khi $p\to1$, đây là giá trị lớn nhất của $J$.

**Ba lượt.** Mỗi lượt đi theo động lực của hành lang tới đích $s_4$, nên $G_t=-(T-t)$. Mỗi hành động được chọn với xác suất $\tfrac12$, nên lượt dài $T$ bước có xác suất $(\tfrac12)^T$.

| Lượt | Hành động | Trạng thái | $T$ | Xác suất | $G_0,\dots,G_{T-1}$ |
|---|---|---|---|---|---|
| (a) | $1,2,1$ | $s_1,s_2,s_3$ | $3$ | $\tfrac18$ | $-3,-2,-1$ |
| (b) | $2,1,2,1$ | $s_1,s_1,s_2,s_3$ | $4$ | $\tfrac1{16}$ | $-4,-3,-2,-1$ |
| (c) | $1,1,1,2,1$ | $s_1,s_2,s_1,s_2,s_3$ | $5$ | $\tfrac1{32}$ | $-5,\dots,-1$ |

**Ước lượng.** Với $\gamma=1$, $\widehat g=\sum_tG_t\psi_t$. Bước chọn hành động 1 có tọa độ thứ nhất của hàm điểm bằng $\tfrac12$, bước chọn hành động 2 có tọa độ đó bằng $-\tfrac12$, và tọa độ thứ hai luôn ngược dấu tọa độ thứ nhất. Tọa độ thứ nhất của $\widehat g$ là

- lượt (a): $\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)=-1$;
- lượt (b): $-\tfrac12(-4)+\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)=1$;
- lượt (c): $\tfrac12(-5-4-3-1)-\tfrac12(-2)=-6{,}5+1=-5{,}5$.

Ba lượt cho $\widehat g=(-1;\,1)$, $(1;\,-1)$ và $(-5{,}5;\,5{,}5)$, trong khi $\nabla_\theta J=(2;\,-2)$: lượt (b) cùng chiều gradient, hai lượt (a) và (c) ngược chiều.

**Cập nhật theo lượt (c).** Bước tăng gradient cho

- hướng: $\alpha\widehat g=(-0{,}55;\,0{,}55)$;
- tham số mới: $\theta=(0;\,0)+(-0{,}55;\,0{,}55)=(-0{,}55;\,0{,}55)$;
- xác suất mới: $p=\sigma(\theta_1-\theta_2)=\sigma(-1{,}1)\approx0{,}25$.

Hàm mục tiêu giảm từ $J(0{,}5)=-12$ xuống $J\approx-18{,}7$.

**Diễn giải.** Mọi phần thưởng âm nên mọi $G_t<0$, và mỗi hành động đã chọn bị giảm xác suất theo $\lvert G_t\rvert$. Hướng của một lượt vì vậy do các hành động nó đã chọn quyết định. Lượt (a) chọn hành động 1 ở hai bước có $\lvert G_t\rvert$ cộng lại bằng $4$, lớn hơn $2$ của bước chọn hành động 2, nên đẩy $p$ xuống. Lượt (b) chọn hành động 2 ở hai bước có $\lvert G_t\rvert$ cộng lại bằng $6$, lớn hơn tổng $4$ của hai bước chọn hành động 1, nên đẩy $p$ lên. Lượt (c) chọn hành động 1 bốn lần, nên $p$ giảm từ $0{,}5$ xuống $0{,}25$, xa dần giá trị tốt nhất $p^*\approx0{,}59$.

**Kiểm tra lại.** Với $p=\sigma(-1{,}1)=0{,}24974$: $p(1-p)=0{,}18737$ và $2(2-p)=3{,}50052$, nên $J=-3{,}50052/0{,}18737=-18{,}68$.
:::

![Hành lang ngắn đảo hành động: bốn ô s 1 (xuất phát), s 2, s 3, s 4 (đích). Ô s 1: hành động 1 tới s 2, hành động 2 đứng yên. Ô s 2, viền nét đứt đậm, ghi đảo hành động: hành động 1 về s 1, hành động 2 tới s 3. Ô s 3: hành động 1 tới s 4, hành động 2 về s 2. Ô s 4 tô xám: đích, kết thúc lượt. Mỗi bước phần thưởng âm 1; mọi ô cùng đặc trưng nên chọn hành động 1 với cùng xác suất p.](img/lec-09/short-corridor.svg)

Trên hình, lượt (c) của Ví dụ 10.2 đi $s_1\to s_2\to s_1\to s_2\to s_3\to s_4$; lần chọn "sang phải" tại ô viền nét đứt $s_2$ đưa tác tử lùi về $s_1$.

Trên Breakout, notebook thực hành thứ hai của Bài 09 cho thấy REINFORCE chỉ học được một hành vi gần hằng sau $10^6$ bước, khi nhiều lượt có $\widehat g=0$ (Tình huống 10.3).

Giới hạn thứ hai nằm ở cách dùng dữ liệu. Hệ quả 09.26 cần lượt do chính $\pi_{\theta_{\mathrm{old}}}$ sinh ra, nên sau một bước cập nhật, lượt vừa dùng thuộc về chính sách cũ và không còn cho mẫu không chệch của gradient tại tham số mới. REINFORCE vì vậy dùng mỗi lượt cho đúng một bước. Muốn mỗi lượt đem lại nhiều tiến bộ hơn, chúng ta cần bước lớn hơn; nhưng bước lớn đổi chính sách, chính sách mới thăm các trạng thái theo một phân bố khác, và kết quả có thể tệ đi (bài giảng gốc, tr. 4, 14). Trên hành lang của Ví dụ 10.2, ta tính một bước theo đúng gradient $(2;\,-2)$ từ $\theta=(0;\,0)$ với hai bước học:

- $\alpha=0{,}05$ cho $\theta=(0{,}1;\,-0{,}1)$, $p=\sigma(0{,}2)\approx0{,}55$, chưa tới $p^*\approx0{,}59$, và $J\approx-11{,}72$, tức $J$ tăng;
- $\alpha=0{,}5$ cho $\theta=(1;\,-1)$, $p=\sigma(2)\approx0{,}88$, vượt qua $p^*\approx0{,}59$, và $J\approx-21{,}3$, tức $J$ giảm khoảng $9{,}3$.

Cùng một hướng đúng, bước nhỏ làm $J$ tăng còn bước lớn làm $J$ giảm, vì $J$ chỉ gần tuyến tính trong một lân cận nhỏ của chính sách cũ.

Hai giới hạn này dẫn tới **bài toán trung tâm của chương**: giảm phương sai của ước lượng gradient mà vẫn giữ kỳ vọng của nó, và dùng lại dữ liệu từ chính sách cũ $\pi_{\mathrm{old}}$ cho các bước cập nhật hiệu quả, đồng thời kiểm soát nguy cơ suy giảm hiệu năng.

![Hai hàng khung nối bằng mũi tên. Hàng trên, viền liền, nhãn phương sai của ước lượng gradient: khung đường cơ sở và critic, với G t trừ v mũ của S t và sai số TD delta t (Mục 2), dẫn tới khung GAE, A mũ t bằng tổng theo k của (gamma lambda) mũ k nhân delta t cộng k (Mục 3). Hàng dưới, viền nét đứt, nhãn độ lớn bước cập nhật: khung hàm thay thế và chặn cải thiện (Mục 4), dẫn tới khung TRPO, KL trung bình không vượt kappa (Mục 5), rồi khung PPO, cắt tỉ số rho t vào đoạn từ 1 trừ epsilon đến 1 cộng epsilon (Mục 6). Hai hàng gặp nhau ở khung cuối, viền đậm: Thuật toán 10.49, PPO kiểu actor–critic, GAE cho lợi thế và mục tiêu cắt cho chính sách.](img/lec-10/central-problem.svg)

Trên hình, các mục xếp thành hai hàng, mỗi hàng trả lời một phần của bài toán trung tâm. Hàng trên giảm phương sai: ở Mục 2, chúng ta trừ đường cơ sở và bootstrap từ một hàm giá trị học được; ở Mục 3, chúng ta trộn các ước lượng nhiều bước thành GAE. Hàng dưới giới hạn bước cập nhật: ở Mục 4, chúng ta dự báo mức thay đổi của $J$ bằng hàm thay thế và giới hạn khoảng cách giữa hai chính sách bằng KL; ở Mục 5, chúng ta giải bài toán có ràng buộc KL; ở Mục 6, chúng ta thay ràng buộc bằng phép cắt tỉ số. Hai hàng gặp nhau ở thuật toán PPO, nơi lợi thế ước lượng bằng GAE đi vào mục tiêu cắt.

---

## 2. Đường cơ sở, hàm lợi thế và actor–critic

Trong ước lượng $\widehat g$ của Ví dụ 10.1, mỗi hàm điểm được nhân với cả lợi tức, kể cả phần chung mà mọi hành động đều nhận. Để giảm phương sai mà không đổi kỳ vọng, chúng ta trừ khỏi $G_t$ một mức so sánh không phụ thuộc hành động đã chọn.

<!-- note-topic-id: lec-10-topic-03 -->
### 2.1 Đường cơ sở

Về mặt ý tưởng, một hành động tốt là hành động cho lợi tức cao hơn mức thường đạt được tại trạng thái đó, nên ta so mỗi lợi tức $G_t$ với một mức $b(S_t)$ của trạng thái và chỉ dùng phần chênh lệch $G_t-b(S_t)$. Trong một MDP, mức so sánh phải thay đổi theo trạng thái (Sutton và Barto, 2018, §13.4, tr. 329): ở trạng thái mà mọi hành động đều có giá trị cao, mức so sánh phải cao thì mới phân biệt được hành động tốt hơn với hành động kém hơn. Ví dụ sau cho thấy phép trừ tác động lên kỳ vọng và phương sai.

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

**Diễn giải.** Mọi đường cơ sở hằng giữ nguyên kỳ vọng. Phương sai $\tfrac49(b-1)^2$ nhỏ nhất tại $b=1$ chứ không tại $v_\pi(s)=2$, và bằng $\tfrac{16}9$ tại $b=3$. Cộng hằng $c$ vào mọi phần thưởng và vào đường cơ sở giữ nguyên hiệu $r(A)-b$. Vì vậy, một đường cơ sở dịch theo mức chung của phần thưởng, như $v_\pi(s)$, khử ảnh hưởng của phép cộng hằng. Ước lượng với $r=(4;\,1)$ và $b=0$ của Ví dụ 10.1 chính là ước lượng với $r=(3;\,0)$ và $b=-1$, có tổng phương sai $\tfrac49(-1-1)^2=\tfrac{16}9$.

**Kiểm tra lại.** Với $b=3$: $X_3=0$ khi $A=1$ và $X_3=(2;\,-2)$ khi $A=2$; mỗi tọa độ có mô men bậc hai $\tfrac13\cdot4=\tfrac43$, phương sai $\tfrac43-\tfrac49=\tfrac89$, tổng $\tfrac{16}9=\tfrac49(3-1)^2$.
:::

Ví dụ 10.3 trừ cùng một hằng ở mọi mẫu. Trong một lượt nhiều bước, mức so sánh thay đổi theo trạng thái, và có thể phụ thuộc mọi thông tin đã có trước khi chọn hành động. Định nghĩa sau gom cả hai trường hợp.

::: definition Định nghĩa 10.1 (Đường cơ sở và ước lượng có đường cơ sở)
Cho chính sách tham số hóa $\pi_\theta$ và một lượt $S_0,A_0,R_1,\dots,S_T$ sinh bởi $\pi_\theta$, với lịch sử $H_t$ và hàm điểm $\psi_t$ như ở Bài 09 ($\psi_t=0$ khi $t\ge T$).

Một *đường cơ sở* (baseline) là một hàm bị chặn $b:\mathcal S\to\mathbb R$. Ước lượng có đường cơ sở của gradient là
$$\widehat g_b=\sum_{t=0}^{T-1}\gamma^t\bigl(G_t-b(S_t)\bigr)\psi_t .$$

Một *đường cơ sở ngẫu nhiên* là một dãy biến ngẫu nhiên thực bị chặn $B_0,B_1,\dots$ sao cho, với mỗi $t<T$, khi biết $(H_t,B_t)$ hành động $A_t$ vẫn có phân phối $\pi_\theta(\cdot\mid S_t)$. Ước lượng tương ứng là $\widehat g_B=\sum_{t=0}^{T-1}\gamma^t(G_t-B_t)\psi_t$.
:::

Hệ số của $\psi_t$ trong $\widehat g_b$ là chênh lệch giữa lợi tức thực nhận và mức so sánh của trạng thái $S_t$. Với $b\equiv0$, $\widehat g_b$ là ước lượng REINFORCE của Thuật toán 09.25. Ví dụ về đường cơ sở ngẫu nhiên: $\hat v(S_t,w)$ với $w$ giữ cố định trong lượt, hoặc trung bình $G_0$ của các lượt khác, độc lập với lượt đang xét. Lợi tức $G_t$ của chính lượt không là đường cơ sở, vì nó phụ thuộc $A_t$.

Mệnh đề sau cho thấy phép trừ không đổi kỳ vọng, với cùng lập luận đã dùng cho phần thưởng quá khứ trong Bổ đề 09.22.

::: proposition Mệnh đề 10.2 (Đường cơ sở không làm chệch)
**Giả thiết.** (G1)–(G4) của Định lý 09.23; $b:\mathcal S\to\mathbb R$ thỏa $\lvert b(s)\rvert\le\bar b$ với mọi $s$.

**Kết luận.**
$$\begin{aligned}&\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^t\,b(S_t)\,\psi_t\Bigr]=0,\\&\text{do đó}\quad\mathbb E_{\pi_\theta}[\widehat g_b]=\nabla_\theta J(\theta).\end{aligned}$$

**Điều kiện áp dụng.** Lượt sinh bởi $\pi_\theta$, mọi hàm điểm tính tại cùng $\theta$, và $b$ giữ cố định trong suốt lượt. Kết luận giữ nguyên khi thay $b(S_t)$ bằng một đường cơ sở ngẫu nhiên $B_t$ của Định nghĩa 10.1.

**Phạm vi.** Bảo đảm thuộc về kỳ vọng; một đường cơ sở có thể làm phương sai tăng, như $b=3$ trong Ví dụ 10.3.
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

Theo Mệnh đề 10.2, nếu mức trừ khỏi mỗi lợi tức chỉ phụ thuộc thông tin có trước khi chọn hành động thì kỳ vọng của bước cập nhật giữ nguyên; phép trừ chỉ đổi cách các mẫu phân tán quanh kỳ vọng. Ba giả thiết có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "đường cơ sở không phụ thuộc hành động": trên bài toán một bước, đặt $b(S_0,A_0)=r(A_0)$. Khi đó $G_0-b=0$ ở mọi lượt, nên $\widehat g_b\equiv0\ne(\tfrac23;\,-\tfrac23)$. Chọn $b=G_t$ của chính lượt cho cùng kết quả.
- Bỏ "lượt sinh bởi $\pi_\theta$": nếu hành động của bài toán một bước được chọn đều, mỗi hành động với xác suất $\tfrac12$, thì $\mathbb E[b\,\psi_\theta(s,A)]=b\bigl(\tfrac12(\tfrac13;\,-\tfrac13)+\tfrac12(-\tfrac23;\,\tfrac23)\bigr)=b\,(-\tfrac16;\,\tfrac16)$, khác $0$ khi $b\ne0$.
- Bỏ "đường cơ sở bị chặn": nếu $B_0$ có phân phối Cauchy chuẩn, độc lập với $A_0$, thì $B_0\psi_0$ không khả tích và kỳ vọng trong kết luận không xác định.

Hai giả thiết đầu được dùng ở Bước 2, nơi phân phối có điều kiện của $A_t$ phải là $\pi_\theta(\cdot\mid S_t)$; giả thiết bị chặn được dùng ở Bước 3 để áp dụng tính chất tháp. Một nhầm lẫn thường gặp là đòi đường cơ sở độc lập với hành động. $b(S_t)$ và $A_t$ nói chung không độc lập, vì cả hai phụ thuộc $S_t$; điều chứng minh cần là $b$ không phụ thuộc $A_t$ khi đã biết lịch sử $H_t$.

::: example Ví dụ 10.4 (Đường cơ sở trên lượt năm bước của Ví dụ 10.2)
**Dữ kiện.** Hành lang ngắn của Ví dụ 10.2: bốn ô $s_1,\dots,s_4$, phần thưởng $-1$ mỗi bước, $\gamma=1$, hai hành động bị đảo ở $s_2$; $p=\tfrac12$, $\psi_\theta(s,1)=(\tfrac12;\,-\tfrac12)$, $\psi_\theta(s,2)=(-\tfrac12;\,\tfrac12)$, $\nabla_\theta J=(2;\,-2)$. Lượt (c): hành động $1,1,1,2,1$, trạng thái $s_1,s_2,s_1,s_2,s_3$, lợi tức $G_t=-5,-4,-3,-2,-1$. Đường cơ sở là $b=v_\pi$ tại $p=\tfrac12$.

**Giá trị trạng thái.** Với $p=\tfrac12$, Mệnh đề 03.22 và 03.23 cho hệ
$$\begin{aligned}v(s_1)&=-1+\tfrac12v(s_2)+\tfrac12v(s_1),\\v(s_2)&=-1+\tfrac12v(s_1)+\tfrac12v(s_3),\\v(s_3)&=-1+\tfrac12v(s_2),\end{aligned}$$
trong đó số hạng thiếu ở phương trình thứ ba là đích, có giá trị $0$. Phương trình thứ nhất cho $v(s_1)=v(s_2)-2$, phương trình thứ ba cho $v(s_3)=\tfrac12v(s_2)-1$; thế vào phương trình thứ hai được $v(s_2)=-2{,}5+\tfrac34v(s_2)$, tức $v_\pi=(-12;\,-10;\,-6)$.

**Chênh lệch.** $G_t-v_\pi(S_t)$ lần lượt là $-5+12$, $-4+10$, $-3+12$, $-2+10$, $-1+6$, tức $7,6,9,8,5$.

**Ước lượng.** Tọa độ thứ nhất của $\widehat g_b$ là $\tfrac12(7+6+9+5)-\tfrac12\cdot8=13{,}5-4=9{,}5$, nên $\widehat g_b=(9{,}5;\,-9{,}5)$, cùng chiều $\nabla_\theta J=(2;\,-2)$.

**Diễn giải.** Với $\gamma=1$ và phần thưởng $-1$ mỗi bước, $-G_t$ là số bước còn lại của lượt từ bước $t$, còn $-v_\pi(S_t)$ là số bước còn lại kỳ vọng từ trạng thái $S_t$. Do đó chênh lệch $G_t-v_\pi(S_t)$ dương đúng khi lượt về đích sớm hơn kỳ vọng từ $S_t$. Trên lượt này, cả năm chênh lệch đều dương, nên mọi hành động đã chọn được tăng xác suất; bốn lần tăng cho hành động 1 thắng một lần tăng cho hành động 2. Kết quả thuộc về lượt này. Cùng phép tính cho tọa độ thứ nhất bằng $3$ trên lượt (a) và $-1$ trên lượt (b): lượt (b) cùng chiều gradient khi chưa trừ đường cơ sở, và thành ngược chiều sau khi trừ. Trên ba lượt, đường cơ sở sửa chiều của lượt (a) và (c) và làm lượt (b) ngược chiều: nó không làm mọi lượt cùng chiều gradient, điều nó giữ là kỳ vọng (Mệnh đề 10.2). Một lượt dài hơn $12$ bước cho chênh lệch âm ở bước đầu.

**Kiểm tra lại.** $v_\pi(s_1)=-12=J(\tfrac12)$, đúng với $J(p)=-2(2-p)/\bigl(p(1-p)\bigr)$ của Ví dụ 10.2. Thay $v_\pi$ vào phương trình thứ hai: $-1+\tfrac12(-12)+\tfrac12(-6)=-10$.
:::

Hành lang có $\gamma=1$ và độ dài lượt không bị chặn, nên không thỏa (G3). Tuy vậy, từ mọi ô, lượt về đích trong ba bước kế tiếp với xác suất ít nhất $(\tfrac12)^3$, nên $\Pr(T>3k)\le(\tfrac78)^k$ và $T$ có mọi mô men hữu hạn. Ngoài ra $\mathbb E[T]=-J(\tfrac12)=12$ (Ví dụ 10.2). Do đó Hệ quả 09.26 vẫn cho $\mathbb E[\widehat g]=(2;\,-2)$. Với $\lvert b\rvert\le\bar b=12$ và $\lVert\psi\rVert\le c_\psi=\tfrac{\sqrt2}2$, ta có $\sum_{t<T}\lvert b(S_t)\rvert\,\lVert\psi_t\rVert\le\bar b\,c_\psi\,T$; *định lý hội tụ trội* (dominated convergence theorem) cho phép đổi kỳ vọng với tổng theo $t$, và Bước 2 của chứng minh Mệnh đề 10.2 cho mỗi số hạng đường cơ sở kỳ vọng $0$. Do đó $\mathbb E[\widehat g_b]=\mathbb E[\widehat g]=(2;\,-2)$.

**Trong thực hành.** Đường cơ sở là đầu ra của một mạng $\hat v(s,w)$ học song song với chính sách. Để áp dụng Mệnh đề 10.2, ta giữ $w$ cố định khi tính các hệ số $G_t-\hat v(S_t,w)$ của một lượt và dừng gradient (Định nghĩa 08.12) qua các hệ số đó khi lấy gradient theo $\theta$, để bước cập nhật chính sách không đi vào $w$. Giả thiết dữ liệu theo chính sách vẫn giữ nguyên như ở REINFORCE: lượt phải do chính $\pi_\theta$ sinh ra.

<!-- note-topic-id: lec-10-topic-04 -->
### 2.2 Đường cơ sở có phương sai nhỏ nhất

Trong Ví dụ 10.3, giá trị trạng thái $v_\pi(s)=2$ không làm phương sai nhỏ nhất.

**Câu hỏi.** Đường cơ sở hằng nào cho phương sai nhỏ nhất?

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

Đọc bằng lời, $b^*$ là trung bình của phần thưởng với trọng số $\pi_\theta(a\mid s)\lVert\psi_\theta(s,a)\rVert^2$ cho hành động $a$, còn $v_\pi(s)=\mathbb E[R]$ là kỳ vọng của phần thưởng theo $\pi_\theta(\cdot\mid s)$; hai số trùng nhau khi mọi hành động có cùng $\lVert\psi_\theta(s,a)\rVert$. Trên Ví dụ 10.3, $\lVert\psi_\theta(s,1)\rVert^2=\tfrac29$ và $\lVert\psi_\theta(s,2)\rVert^2=\tfrac89$, nên
$$\begin{aligned}b^*&=\frac{\tfrac23\cdot3\cdot\tfrac29}{\tfrac23\cdot\tfrac29+\tfrac13\cdot\tfrac89}=\frac{4/9}{4/9}\\&=1\ne v_\pi(s)=2,\end{aligned}$$
và $k_2=\tfrac49$ khớp hệ số của công thức $\tfrac49(b-1)^2$. Hành động 2, hiếm hơn, có hàm điểm dài gấp đôi và phần thưởng $0$, nên kéo $b^*$ xuống dưới $v_\pi(s)$.

Hai giả thiết của Mệnh đề 10.3 có vai trò riêng.

- Bỏ "$\mathbb E\lVert\psi\rVert^2>0$": khi tập hành động chỉ có một phần tử, $\psi\equiv0$, mọi $b$ cho phương sai $0$ và công thức của $b^*$ có dạng $0/0$.
- Bỏ "$b$ không phụ thuộc $A$": $b=R$ cho $X_b\equiv0$, phương sai $0$ nhưng kỳ vọng $0\ne g$; phép cực tiểu hóa phương sai chỉ có nghĩa trên các đường cơ sở không làm chệch.

Giả thiết thứ hai được dùng ở Bước 1, nơi kỳ vọng không phụ thuộc $b$; giả thiết thứ nhất được dùng ở Bước 3, nơi hệ số của $b^2$ phải dương.

Greensmith, Bartlett và Baxter (2004, §5, Định lý 13, tr. 1489–1490, và Hệ quả 15, tr. 1491–1492) chứng minh một dạng tổng quát cho bài toán phần thưởng trung bình trên chuỗi Markov ergodic: đường cơ sở tối ưu theo trạng thái là trung bình của lợi tức với trọng số $\lVert\psi\rVert^2$, nói chung khác $v_\pi$.

**Trong thực hành.** Sutton và Barto (2018, §13.4, tr. 329) gọi ước lượng $\hat v(S_t,w)$ của giá trị trạng thái là một lựa chọn tự nhiên cho đường cơ sở: $v_\pi$ học được bằng hồi quy lợi tức về trạng thái như ở Bài 05 và Bài 07, còn $b^*$ cần trọng số $\lVert\psi_\theta\rVert^2$, thay đổi theo $\theta$.

<!-- note-topic-id: lec-10-topic-05 -->
### 2.3 Hàm lợi thế

Với đường cơ sở $b=v_\pi$, hệ số của $\psi_t$ trong ước lượng là $G_t-v_\pi(S_t)$; trên lượt của Ví dụ 10.4, các hệ số này là $7,6,9,8,5$. Theo Bổ đề 03.20(d), khi biết lịch sử và $A_t=a$, lợi tức $G_t$ có kỳ vọng $q_\pi(S_t,a)$, nên hệ số có kỳ vọng có điều kiện $q_\pi(S_t,a)-v_\pi(S_t)$. Một cách trực quan, hiệu này đo hành động $a$ tốt hơn hay kém hơn bao nhiêu so với việc chọn hành động theo chính $\pi$ tại trạng thái đó.

::: definition Định nghĩa 10.4 (Hàm lợi thế)
Cho chính sách Markov dừng $\pi$ với giá trị trạng thái $v_\pi$ và giá trị hành động $q_\pi$. *Hàm lợi thế* (advantage function) của $\pi$ là
$$\begin{aligned}&A_\pi(s,a)=q_\pi(s,a)-v_\pi(s),\\&s\in\mathcal S,\ a\in\mathcal A,\end{aligned}$$
với quy ước $A_\pi=0$ tại trạng thái hấp thụ sau khi lượt kết thúc.
:::

$A_\pi(s,a)>0$ nghĩa là thực hiện $a$ tại $s$ rồi theo $\pi$ cho lợi tức kỳ vọng lớn hơn theo $\pi$ ngay từ $s$. Vì $v_\pi(s)$ không phụ thuộc $a$, $A_\pi(s,\cdot)$ và $q_\pi(s,\cdot)$ xếp các hành động theo cùng thứ tự, và điều kiện $q_\pi(s,\pi'(s))\ge v_\pi(s)$ của Định lý 04.13 chính là $A_\pi(s,\pi'(s))\ge0$. $A_\pi$ là đại lượng đúng của $\pi$; các đại lượng như $G_t-\hat v(S_t,w)$ là ước lượng của nó.

Mệnh đề sau viết lại Hệ quả 09.24 với $A_\pi$ ở vị trí của $q_\pi$. Dạng quỹ đạo của kết luận (b) là hệ quả của Mệnh đề 10.2 với đường cơ sở $b=v_\pi$: phép trừ $v_\pi(S_t)$ không đổi kỳ vọng của ước lượng, và hệ số còn lại, $G_t-v_\pi(S_t)$, có kỳ vọng có điều kiện bằng lợi thế. Kết luận (a) dùng Mệnh đề 03.23.

::: proposition Mệnh đề 10.5 (Tính chất của lợi thế, gradient dạng lợi thế)
**Giả thiết.**

- Cho (a): MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, chính sách Markov dừng $\pi$, như Mệnh đề 03.23.
- Cho (b): (G1)–(G4), MDP hữu hạn, chính sách Markov dừng $\pi=\pi_\theta$ và trạng thái hấp thụ sau khi lượt kết thúc, như Hệ quả 09.24.

**Kết luận.**

- (a) $\sum_a\pi(a\mid s)A_\pi(s,a)=0$ với mọi $s\in\mathcal S$.
- (b) (Dạng quỹ đạo là hệ quả của Mệnh đề 10.2 với $b=v_\pi$.) Gradient của hàm mục tiêu có hai dạng
$$\begin{aligned}&\nabla_\theta J(\theta)\\&=\mathbb E_{\pi_\theta}\Bigl[\sum_{t=0}^{T-1}\gamma^t\\&\qquad\times A_\pi(S_t,A_t)\,\psi_t\Bigr]\\&=\frac1{1-\gamma}\\&\quad\times\mathbb E_{\substack{S\sim\nu^\pi\\A\sim\pi_\theta(\cdot\mid S)}}\bigl[A_\pi(S,A)\\&\qquad\times\psi_\theta(S,A)\bigr].\end{aligned}$$

**Điều kiện áp dụng.** $A_\pi$ và $\nu^\pi$ là của chính chính sách đang được lấy gradient, $\pi=\pi_\theta$.

**Phạm vi.** Đẳng thức (b) có hằng chính xác $1/(1-\gamma)$; mệnh đề không cho cách ước lượng $A_\pi$.
:::

::: proof
**Bước 1 (kết luận a).** Theo Mệnh đề 03.23, $\sum_a\pi(a\mid s)q_\pi(s,a)=v_\pi(s)$, nên $\sum_a\pi(a\mid s)A_\pi(s,a)=v_\pi(s)-v_\pi(s)\sum_a\pi(a\mid s)=0$.

**Bước 2 (Mệnh đề 10.2 với $b=v_\pi$).** Giá trị $v_\pi$ bị chặn bởi $T_{\max}R_{\max}$ theo (G3), nên $v_\pi$ là một đường cơ sở theo Định nghĩa 10.1, và Mệnh đề 10.2 áp dụng với $b=v_\pi$. Với quy ước $\psi_t=0$ khi $t\ge T$, ta được
$$\begin{aligned}&\nabla_\theta J(\theta)\\&=\sum_{t=0}^{T_{\max}-1}\gamma^t\,\mathbb E\bigl[(G_t-v_\pi(S_t))\psi_t\bigr].\end{aligned}$$

**Bước 3 (tính chất tháp theo $(H_t,A_t)$).** Cố định $t$. Cả $v_\pi(S_t)$ và $\psi_t$ là hàm của $(H_t,A_t)$, nên ra ngoài kỳ vọng có điều kiện theo $(H_t,A_t)$:
$$\begin{aligned}&\mathbb E\bigl[(G_t-v_\pi(S_t))\psi_t\bigr]\\&=\mathbb E\bigl[(\mathbb E[G_t\mid H_t,A_t]\\&\qquad-v_\pi(S_t))\psi_t\bigr].\end{aligned}$$

**Bước 4 (tính Markov).** Với chính sách Markov dừng, Bổ đề 03.20(d) cho $\mathbb E[G_t\mid H_t,A_t]=q_\pi(S_t,A_t)$ trên $\{t<T\}$; trên $\{t\ge T\}$, $\psi_t=0$. Thế vào Bước 3, dùng $q_\pi-v_\pi=A_\pi$ (Định nghĩa 10.4) rồi cộng theo $t$ như ở Bước 2:
$$\begin{aligned}&\nabla_\theta J(\theta)\\&=\sum_{t=0}^{T_{\max}-1}\gamma^t\,\mathbb E\bigl[A_\pi(S_t,A_t)\psi_t\bigr]\\&=\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^tA_\pi(S_t,A_t)\psi_t\Bigr].\end{aligned}$$

**Bước 5 (dạng chiếm dụng).** Theo Hệ quả 09.24, $\nabla_\theta J=\frac1{1-\gamma}\mathbb E_{S\sim\nu^\pi,A\sim\pi_\theta}[q_\pi(S,A)\psi_\theta(S,A)]$. Với mỗi $s$, Mệnh đề 09.17 với $c=v_\pi(s)$ cho $\sum_a\pi_\theta(a\mid s)v_\pi(s)\psi_\theta(s,a)=0$; trừ đại lượng này trong kỳ vọng theo $A$ được dạng thứ hai của (b). $\square$
:::

Mệnh đề 10.5(b) nói rằng hướng tăng của $J$ là kỳ vọng của tổng các hàm điểm, mỗi hàm điểm nhân với lợi thế của hành động đã chọn; phép thay $q_\pi$ bằng $A_\pi$ không đổi kết quả vì phần bị trừ, $v_\pi(s)$, là hằng theo hành động.

Hai điều kiện của mệnh đề có vai trò riêng.

- Bỏ "$A_\pi$ là của chính $\pi_\theta$": trên bài toán một bước, lợi thế của chính sách đều $\pi'=(\tfrac12;\,\tfrac12)$ là $A_{\pi'}=(3-1{,}5;\,0-1{,}5)=(1{,}5;\,-1{,}5)$, và $\sum_a\pi_\theta(a\mid s)A_{\pi'}(s,a)=\tfrac23\cdot1{,}5-\tfrac13\cdot1{,}5=0{,}5\ne0$: kết luận (a) không còn đúng.
- Bỏ "$\gamma<1$": thừa số $1/(1-\gamma)$ không xác định. Dạng quỹ đạo vẫn dùng được khi $T$ có đuôi hình học, như trên hành lang ngắn, nhờ hội tụ trội như ở đoạn sau Ví dụ 10.4; khi gom theo trạng thái, trọng số là số lần thăm kỳ vọng không chuẩn hóa $\eta(s)=\sum_t\Pr(S_t=s)$.

Bước 1 dùng Mệnh đề 03.23 cho chính $\pi$; Bước 2 dùng Mệnh đề 10.2, cần (G1)–(G4); Bước 4 dùng Bổ đề 03.20(d), cần chính sách Markov dừng.

::: example Ví dụ 10.5 (Lợi thế trên bài toán một bước)
**Dữ kiện.** Như Ví dụ 10.1: một trạng thái, $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$, $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$, lượt dừng sau một hành động.

**Lợi thế.** Lượt kết thúc sau hành động đầu tiên, nên $q_\pi(s,a)=r(a)$, tức $q_\pi=(3;\,0)$; $v_\pi(s)=2$; $A_\pi(s,\cdot)=(1;\,-2)$.

**Gradient.** Với $T=1$, chỉ có số hạng $t=0$ và $\gamma^0=1$:
$$\begin{aligned}&\tfrac23\cdot1\cdot(\tfrac13;\,-\tfrac13)\\&\quad+\tfrac13\cdot(-2)\cdot(-\tfrac23;\,\tfrac23)\\&\quad=(\tfrac29;\,-\tfrac29)+(\tfrac49;\,-\tfrac49)\\&\quad=(\tfrac23;\,-\tfrac23).\end{aligned}$$
Ở dạng chiếm dụng, $\nu^\pi(s)=1-\gamma$ vì trạng thái chỉ được thăm ở $t=0$, nên thừa số $1/(1-\gamma)$ bị khử và $\gamma$ không xuất hiện.

**Kiểm tra lại.** Kết luận (a): $\tfrac23\cdot1+\tfrac13\cdot(-2)=0$. Với $r=(4;\,1)$ của Ví dụ 10.1, $q_\pi=(4;\,1)$, $v_\pi(s)=3$ và $A_\pi$ vẫn là $(1;\,-2)$.
:::

Thay $v_\pi$ chưa biết bằng một hàm giá trị học được, ta có thuật toán sau, phỏng theo hộp giả mã của Sutton và Barto (2018, §13.4, tr. 330). Ví dụ 10.4 tính bằng tay phép cập nhật chính sách của thuật toán với đường cơ sở $v_\pi$ và $\gamma=1$, dù thuật toán giả thiết $\gamma<1$.

::: algorithm Thuật toán 10.6 (REINFORCE có đường cơ sở)
**Đầu vào.** Chính sách tham số hóa khả vi $\pi_\theta$; hàm giá trị tham số hóa khả vi $\hat v(s,w)$, $w\in\mathbb R^{d'}$; bước học $\alpha_\theta>0$, $\alpha_w>0$; $\gamma\in[0,1)$; số lượt $E$.

**Đầu ra.** Tham số $\theta$ và $w$ sau $E$ lượt.

**Giả thiết.** (G1)–(G4) cho chính sách; $\hat v(\cdot,w)$ bị chặn với mỗi $w$.

**Khởi tạo.** $\theta$ và $w$ tùy ý, chẳng hạn $w=0$.

**Lặp $E$ lần, mỗi lần một lượt:**

1. $\theta_{\mathrm{old}}\leftarrow\theta$, $w_{\mathrm{old}}\leftarrow w$. Thu một lượt $S_0,A_0,R_1,\dots,S_T$ với $A_t\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid S_t)$.
2. $G_T=0$; với $t=T-1,\dots,0$: $G_t=R_{t+1}+\gamma G_{t+1}$.
3. Cập nhật hàm giá trị: $w\leftarrow w_{\mathrm{old}}+\alpha_w\sum_{t=0}^{T-1}\bigl(G_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\nabla_w\hat v(S_t,w_{\mathrm{old}})$.
4. Cập nhật chính sách: $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_{t=0}^{T-1}\gamma^t\bigl(G_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$.

**Điều kiện dừng.** Sau $E$ lượt.

**Chi phí mỗi bước.** Một lần tính $\hat v$ và gradient của nó theo $w$, một hàm điểm; bộ nhớ $O(T)$ để lưu lượt.
:::

Bước 3 hồi quy $\hat v$ về lợi tức Monte Carlo, không có trọng số $\gamma^t$; bước 4 có $\gamma^t$ như Thuật toán 09.25. Thuật toán giữ $w_{\mathrm{old}}$ cố định trong cả lượt, nên đường cơ sở là một hàm cố định của trạng thái như Mệnh đề 10.2 yêu cầu.

**Trong thực hành.** Bước 3 là một bước hạ gradient của mất mát bình phương $\tfrac12\sum_t\bigl(G_t-\hat v(S_t,w)\bigr)^2$ tại $w_{\mathrm{old}}$, với $\hat v$ là một mạng hoặc một bộ xấp xỉ tuyến tính. Với $\hat v$ tùy ý, Mệnh đề 10.2 bảo đảm Thuật toán 10.6 không chệch cho gradient, nhưng hệ số $G_t-\hat v(S_t,w)$ bị chệch như một ước lượng của lợi thế: theo Bổ đề 03.20(d),
$$\begin{aligned}&\mathbb E\bigl[G_t-\hat v(S_t,w)\mid H_t,A_t\bigr]\\&\quad=A_\pi(S_t,A_t)+v_\pi(S_t)-\hat v(S_t,w).\end{aligned}$$
Trên bài toán một bước với $\hat v(s)=1$, kỳ vọng của hệ số khi chọn hành động 1 là $3-1=2$, trong khi $A_\pi(s,1)=1$. Phần chệch $v_\pi(S_t)-\hat v(S_t,w)$ giống nhau cho mọi hành động tại cùng trạng thái, nên bị khử khi nhân với hàm điểm và lấy kỳ vọng theo hành động.

<!-- note-topic-id: lec-10-topic-06 -->
### 2.4 Critic và actor–critic một bước

Thuật toán 10.6 chỉ cập nhật khi lượt đã kết thúc, vì $G_t$ cần mọi phần thưởng sau bước $t$. Hàm $\hat v$ của nó đánh giá trạng thái đầu $S_t$ của bước chuyển, trước khi hành động được chọn, nên đặt mức so sánh nhưng không đánh giá hành động $A_t$ (Sutton và Barto, 2018, §13.5, tr. 331). Về mặt ý tưởng, nếu áp $\hat v$ cả cho trạng thái thứ hai $S_{t+1}$, thì $R_{t+1}+\gamma\hat v(S_{t+1},w)$ ước lượng lợi tức sau một bước, và so nó với $\hat v(S_t,w)$ cho biết hành động vừa thực hiện tốt hơn hay kém hơn mức mong đợi. Để làm rõ ý này, chúng ta dùng chuỗi hai trạng thái sau.

::: example Ví dụ 10.6 (Chuỗi hai trạng thái)
**Dữ kiện.** Hai trạng thái chưa kết thúc $s_A$ (xuất phát, $\mu_0(s_A)=1$) và $s_B$; hai hành động; $\gamma=0{,}9$.

- Tại $s_A$: hành động 1 chuyển sang $s_B$ với phần thưởng $0$; hành động 2 kết thúc lượt với phần thưởng $1$.
- Tại $s_B$: hành động 1 kết thúc với phần thưởng $3$; hành động 2 kết thúc với phần thưởng $0$.

Chính sách có một tham số cho mỗi trạng thái, $\theta=(\theta_A;\,\theta_B)$, và $p_s=\pi_\theta(1\mid s)=\sigma(\theta_s)$ với $\sigma(x)=1/(1+e^{-x})$; đây là chính sách softmax (Định nghĩa 09.11) với logit $\theta_s$ cho hành động 1 và $0$ cho hành động 2. Theo Mệnh đề 09.16, $\psi_\theta(s,1)=(1-p_s)e_s$ và $\psi_\theta(s,2)=-p_se_s$, với $e_A=(1;\,0)$, $e_B=(0;\,1)$. Chính sách đang xét: $\theta=(0;\,\log2)$, tức $p_A=\sigma(0)=\tfrac12$, $p_B=\sigma(\log2)=\tfrac23$.

**Hàm mục tiêu.** Mọi lượt bắt đầu ở $s_A$ và rẽ theo hành động đầu tiên.

- Với xác suất $1-p_A$, lượt chọn hành động 2 tại $s_A$ và kết thúc ngay: $G_0=1$.
- Với xác suất $p_A$, lượt sang $s_B$ với $R_1=0$. Tại $s_B$, hành động 1 (xác suất $p_B$) cho $R_2=3$ và $G_0=0+0{,}9\cdot3=2{,}7$; hành động 2 (xác suất $1-p_B$) cho $G_0=0$.

Do đó
$$\begin{aligned}J&=(1-p_A)\cdot1+p_Ap_B\cdot2{,}7\\&\quad+p_A(1-p_B)\cdot0\\&=2{,}7\,p_Ap_B+1-p_A,\end{aligned}$$
và tại chính sách đang xét, $J=2{,}7\cdot\tfrac12\cdot\tfrac23+\tfrac12=0{,}9+0{,}5=1{,}4$.

**Giá trị.** Theo Mệnh đề 03.22 và 03.23: $v_\pi(s_B)=\tfrac23\cdot3=2$; $q_\pi(s_A,1)=0+0{,}9\cdot2=1{,}8$; $q_\pi(s_A,2)=1$; $v_\pi(s_A)=\tfrac12\cdot1{,}8+\tfrac12\cdot1=1{,}4=J$.

**Lợi thế.** $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$ và $A_\pi(s_B,\cdot)=(3-2;\,0-2)=(1;\,-2)$.

**Gradient tính trực tiếp.** Lấy đạo hàm $J=2{,}7\,p_Ap_B+1-p_A$ theo $p_A$, $p_B$ rồi nhân với $\mathrm dp_s/\mathrm d\theta_s=p_s(1-p_s)$:
$$\begin{aligned}\frac{\partial J}{\partial\theta_A}&=p_A(1-p_A)(2{,}7p_B-1)\\&=0{,}25\cdot0{,}8=0{,}2,\\\frac{\partial J}{\partial\theta_B}&=p_A\cdot2{,}7\cdot p_B(1-p_B)\\&=0{,}5\cdot2{,}7\cdot\tfrac29=0{,}3.\end{aligned}$$

**Gradient theo Mệnh đề 10.5(b).** Bước $t=0$ ở $s_A$ đóng góp $\tfrac12\cdot0{,}4\cdot0{,}5\,e_A+\tfrac12(-0{,}4)(-0{,}5)\,e_A=0{,}2\,e_A$. Bước $t=1$ ở $s_B$, xảy ra với xác suất $p_A=\tfrac12$ và trọng số $\gamma=0{,}9$, đóng góp $0{,}9\cdot\tfrac12\bigl(\tfrac23\cdot1\cdot\tfrac13+\tfrac13(-2)(-\tfrac23)\bigr)e_B=0{,}45\cdot\tfrac23\,e_B=0{,}3\,e_B$. Tổng là $(0{,}2;\,0{,}3)$, khớp cách tính trực tiếp.

**Ba loại lượt.** Mọi lượt thuộc một trong ba loại. Bảng sau ghi tọa độ $\theta_A$ của ba ước lượng gradient trên mỗi loại: REINFORCE, với hệ số $G_t$; ước lượng có đường cơ sở $b=v_\pi$, với hệ số $G_t-v_\pi(S_t)$; và ước lượng với hệ số là sai số TD $\delta_t=R_{t+1}+\gamma v_\pi(S_{t+1})-v_\pi(S_t)$ của hàm giá trị đúng (Định nghĩa 05.20). Tọa độ $\theta_A$ chỉ nhận đóng góp của bước $t=0$, nên bằng hệ số tại $s_A$ nhân $\psi_\theta(s_A,A_0)=\pm0{,}5$.

| Loại lượt | Xác suất | $G_0$ | REINFORCE | trừ $v_\pi$ | $\delta_t$ |
|---|---|---|---|---|---|
| $s_A\xrightarrow1s_B\xrightarrow1$ | $\tfrac13$ | $2{,}7$ | $1{,}35$ | $0{,}65$ | $0{,}2$ |
| $s_A\xrightarrow1s_B\xrightarrow2$ | $\tfrac16$ | $0$ | $0$ | $-0{,}7$ | $0{,}2$ |
| $s_A\xrightarrow2$ | $\tfrac12$ | $1$ | $-0{,}5$ | $0{,}2$ | $0{,}2$ |
| kỳ vọng | | | $0{,}2$ | $0{,}2$ | $0{,}2$ |
| phương sai | | | $0{,}6925$ | $0{,}2025$ | $0$ |

Ở dòng đầu, REINFORCE cho $2{,}7\cdot0{,}5=1{,}35$, trừ $v_\pi$ cho $(2{,}7-1{,}4)\cdot0{,}5=0{,}65$, và $\delta_0=0+0{,}9\cdot2-1{,}4=0{,}4$ cho $0{,}4\cdot0{,}5=0{,}2$. Ở dòng thứ ba, hàm điểm bằng $-0{,}5$: REINFORCE cho $1\cdot(-0{,}5)=-0{,}5$, trừ $v_\pi$ cho $(1-1{,}4)(-0{,}5)=0{,}2$, và $\delta_0=1-1{,}4=-0{,}4$ cho $0{,}2$. Ở dòng thứ hai, $G_0=0$ cho $0$, trừ $v_\pi$ cho $(0-1{,}4)\cdot0{,}5=-0{,}7$, và $\delta_0=0{,}4$ cho $0{,}2$. Phương sai của cột REINFORCE là $\tfrac13\cdot1{,}35^2+\tfrac12\cdot0{,}5^2-0{,}2^2=0{,}6925\approx0{,}69$; của cột trừ $v_\pi$ là $\tfrac13\cdot0{,}65^2+\tfrac16\cdot0{,}7^2+\tfrac12\cdot0{,}2^2-0{,}2^2=0{,}2025\approx0{,}20$.

Cả ba cột có kỳ vọng $0{,}2$, đúng tọa độ $\theta_A$ của gradient. Ở cột REINFORCE, lượt $s_A\xrightarrow2$ xảy ra một nửa số lần và đẩy $p_A$ xuống: phần thưởng $1$ dương làm tăng xác suất hành động 2, dù $q_\pi(s_A,2)=1<v_\pi(s_A)=1{,}4$. Xác suất một lượt cho tọa độ $\theta_A$ âm là $\tfrac12$ ở cột REINFORCE, $\tfrac16$ ở cột trừ $v_\pi$ và $0$ ở cột cuối. Cột trừ $v_\pi$ làm lượt $s_A\xrightarrow1s_B\xrightarrow2$ xấu đi, từ $0$ xuống $-0{,}7$, nhưng phương sai của cả cột giảm từ $0{,}6925$ xuống $0{,}2025$. Ở tọa độ $\theta_B$, ba cột cho $(0{,}9;\,0;\,0)$, $(0{,}3;\,1{,}2;\,0)$ và $(0{,}3;\,1{,}2;\,0)$ trên ba loại lượt, cùng kỳ vọng $0{,}3$ và cùng phương sai $0{,}18$; hai cột sau trùng nhau vì lượt kết thúc ngay sau $s_B$, nên $G_1-v_\pi(s_B)=\delta_1$.

**Bước dài theo ước lượng của một lượt.** Một lượt $s_A\xrightarrow2$, loại lượt có xác suất $\tfrac12$, cho ước lượng REINFORCE $\widehat g=G_0\,\psi_\theta(s_A,2)=1\cdot(-0{,}5)\,e_A=(-0{,}5;\,0)$, ngược dấu tọa độ $\theta_A$ của gradient $(0{,}2;\,0{,}3)$. Bước $\theta\leftarrow\theta+\alpha\widehat g$ chỉ đổi $\theta_A$ thành $-0{,}5\alpha$ và giữ $p_B=\tfrac23$, nên $J=2{,}7\cdot\tfrac23\,p_A+1-p_A=1+0{,}8\,p_A$:

- $\alpha=1$: $\theta_A=-0{,}5$, $p_A=\sigma(-0{,}5)\approx0{,}378$, $J\approx1{,}30$;
- $\alpha=2$: $\theta_A=-1$, $p_A=\sigma(-1)\approx0{,}27$, $J\approx1{,}22$;
- $\alpha\to\infty$: $\theta_A\to-\infty$, $p_A\to0$ và $J\to1$; đây là giá trị giới hạn, không ứng với $\theta$ hữu hạn nào.

Bước càng dài thì $J$ càng giảm khỏi $1{,}4$, tới mức giảm $0{,}4$ ở giới hạn, khi chính sách bỏ hẳn hành động 1 tại $s_A$.

**Kiểm tra lại.** Kết luận (a) của Mệnh đề 10.5: $\tfrac12\cdot0{,}4+\tfrac12(-0{,}4)=0$ và $\tfrac23\cdot1+\tfrac13(-2)=0$. Ở dạng chiếm dụng, $\nu^\pi(s_A)=0{,}1$, $\nu^\pi(s_B)=0{,}1\cdot0{,}9\cdot\tfrac12=0{,}045$, và $\tfrac1{0{,}1}(0{,}1\cdot0{,}2;\,0{,}045\cdot\tfrac23)=(0{,}2;\,0{,}3)$.
:::

![Chuỗi hai trạng thái. Ô s A, ghi xuất phát và p A bằng xác suất chọn hành động 1, có hai cung: hành động 1 sang ô s B với phần thưởng 0; hành động 2 tới ô kết thúc tô xám với phần thưởng 1. Ô s B, ghi p B, có hai cung tới ô kết thúc: hành động 1 với phần thưởng 3, hành động 2 với phần thưởng 0. Góc dưới ghi gamma bằng 0,9 và chính sách cũ p A bằng 1/2, p B bằng 2/3.](img/lec-10/two-state-chain.svg)

Trên hình, chỉ cung "hành động 1 tại $s_A$" dẫn tới trạng thái thứ hai, nên mọi lượt dài $1$ hoặc $2$ bước, và lợi thế tại $s_A$ phụ thuộc $s_B$ qua $q_\pi(s_A,1)=\gamma v_\pi(s_B)$.

Trên chuỗi này, với một hàm giá trị $\hat v$, ta đánh giá được bước chuyển $s_A\to s_B$ bằng hành động 1 ngay sau một bước: lấy phần thưởng $0$ cộng giá trị chiết khấu của $s_B$ rồi so với $\hat v(s_A)$. Với $\hat v=v_\pi=(1{,}4;\,2)$, phép so sánh cho $0+0{,}9\cdot2-1{,}4=0{,}4=A_\pi(s_A,1)$, như cột cuối của bảng ba loại lượt trong Ví dụ 10.6. Với $\hat v=(1{,}4;\,1)$, đúng ở $s_A$ nhưng đánh giá thấp $s_B$, phép so sánh cho $0+0{,}9\cdot1-1{,}4=-0{,}5$, và hành động 1 bị coi là kém hơn mức mong đợi. Định nghĩa sau gọi tên hai thành phần của cách đánh giá này.

::: definition Định nghĩa 10.7 (Critic, actor, phương pháp actor–critic)
Cho chính sách tham số hóa $\pi_\theta$, hàm giá trị tham số hóa $\hat v(s,w)$ với $w\in\mathbb R^{d'}$, và một bước chuyển $(S_t,A_t,R_{t+1},S_{t+1},Z_{t+1})$ sinh bởi $\pi_\theta$.

Hàm $\hat v(\cdot,w)$ gọi là *critic* khi nó đánh giá hành động $A_t$ qua mục tiêu bootstrap
$$R_{t+1}+\gamma\,(1-Z_{t+1})\,\hat v(S_{t+1},w),$$
tức qua giá trị ước lượng của trạng thái thứ hai $S_{t+1}$ của bước chuyển.

Chính sách $\pi_\theta$ gọi là *actor*.

*Phương pháp actor–critic* (actor–critic method) cập nhật $\theta$ theo một hệ số lập từ mục tiêu bootstrap của critic, và cập nhật $w$ để $\hat v(\cdot,w)$ xấp xỉ giá trị của chính sách hiện tại.
:::

Mục tiêu bootstrap trong định nghĩa là lợi tức một bước, với $\hat v(S_{t+1},w)$ thay cho phần lợi tức sau bước $t+1$, và mặt nạ $(1-Z_{t+1})$ bằng $0$ khi $S_{t+1}$ là trạng thái kết thúc. Theo Sutton và Barto (2018, §13.5, tr. 331), phép bootstrap này phân biệt critic với đường cơ sở. Hàm $\hat v$ của Thuật toán 10.6 chỉ đánh giá trạng thái $S_t$, trước khi hành động được chọn, nên REINFORCE có đường cơ sở không là phương pháp actor–critic, dù có một chính sách và một hàm giá trị học được. Phương pháp actor–critic đôi khi còn được gọi là advantage actor–critic (A2C) (Sutton và Barto, 2018, tr. 338).

Để so mục tiêu bootstrap với giá trị của trạng thái đầu, ta lập sai số TD với critic $\hat v(\cdot,w)$ và mặt nạ kết thúc của Bài 08:
$$\begin{aligned}\delta_t&=R_{t+1}+\gamma\,(1-Z_{t+1})\,\hat v(S_{t+1},w)\\&\quad-\hat v(S_t,w).\end{aligned}$$
Mục tiêu một bước $R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)$ là mục tiêu TD(0) của Định nghĩa 07.19. Mệnh đề sau cho biết $\delta_t$ ước lượng gì.

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

Mệnh đề 10.8(a) nói rằng với critic đúng, sai số TD của một bước là ước lượng không chệch của lợi thế của hành động vừa thực hiện. Trên Ví dụ 10.6 với critic đúng $\hat v=(1{,}4;\,2)$, mọi chuyển là tất định: chọn hành động 1 tại $s_A$ cho $\delta_0=0+0{,}9\cdot2-1{,}4=0{,}4=A_\pi(s_A,1)$, chọn hành động 2 cho $\delta_0=1-1{,}4=-0{,}4$, và chọn hành động 1 tại $s_B$ cho $\delta_1=3-2=1=A_\pi(s_B,1)$. Một nhầm lẫn thường gặp là điều kiện theo trạng thái thay vì theo cặp trạng thái–hành động: với critic đúng, $\mathbb E[\delta_t\mid S_t=s]=\sum_a\pi(a\mid s)A_\pi(s,a)=0$ (Mệnh đề 05.27, Mệnh đề 10.5(a)), nên $\delta_t$ chỉ đánh giá hành động khi lấy điều kiện theo cả $A_t$.

Hai giả thiết của mệnh đề có vai trò riêng.

- Bỏ "critic đúng": trên bài toán một bước với $\hat v(s)=1$ trong khi $v_\pi(s)=2$, ta có $\delta_0=R_1-1$, nên $\mathbb E[\delta_0\mid A_0=1]=2\ne A_\pi(s,1)=1$ và $\mathbb E[\delta_0\mid A_0=2]=-1\ne-2$. Theo (b), độ chệch là $-e(s)=1$ cho cả hai hành động; trong lượt nhiều bước, số hạng $\gamma\sum_{s'}P(s'\mid s,a)e(s')$ làm độ chệch khác nhau giữa các hành động.
- Bỏ "mặt nạ chỉ tắt ở trạng thái kết thúc": nếu bỏ mặt nạ và trạng thái kết thúc của Ví dụ 10.6 được gán giá trị $\hat v=1$, thì với critic đúng trên $\mathcal S$, hành động 2 tại $s_A$ cho $\delta_0=1+0{,}9-1{,}4=0{,}5$, trong khi $A_\pi(s_A,2)=-0{,}4$.

Bước 1 dùng tính Markov và mặt nạ, Bước 2 dùng Mệnh đề 03.22, còn điều kiện critic đúng chỉ dùng ở (a). Sutton và Barto (2018, §13.5, tr. 331) nêu rằng độ chệch này không do bootstrap gây ra: critic học bằng Monte Carlo nhưng chưa hội tụ cũng cho actor bị chệch, đúng như số hạng $e$ trong (b). Ví dụ sau thực hiện hai bước actor–critic với một critic chưa đúng.

::: example Ví dụ 10.7 (Hai bước actor–critic bằng tay)
**Dữ kiện.** Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_s=\sigma(\theta_s)$, $\psi_\theta(s,1)=(1-p_s)e_s$; ban đầu $\theta=(0;\,\log2)$, $p_A=\tfrac12$, $p_B=\tfrac23$. Critic dạng bảng $\hat v(s,w)=w_s$ với $w=(w_A;\,w_B)=(1{,}4;\,1)$, đúng ở $s_A$ và đánh giá thấp $s_B$, vì $v_\pi=(1{,}4;\,2)$; ta có $\nabla_w\hat v(s,w)=e_s$. Bước học $\alpha_w=0{,}5$, $\alpha_\theta=1$. Ở mỗi bước $t$, critic tính $\delta_t$ và cập nhật $w$; actor dùng cùng $\delta_t$, nhân với thừa số $I=\gamma^t$, đóng vai trọng số $\gamma^t$ của Định lý 09.23. Lượt: $S_0=s_A$, $A_0=1$, $R_1=0$, $S_1=s_B$, $Z_1=0$; $A_1=1$, $R_2=3$, kết thúc, $Z_2=1$.

**Bước $t=0$, $I=1$.** Critic:

- mục tiêu $R_1+\gamma(1-Z_1)w_B=0+0{,}9\cdot1=0{,}9$;
- sai lệch $\delta_0=0{,}9-w_A=-0{,}5$;
- giá trị mới $w_A=1{,}4+0{,}5\cdot(-0{,}5)=1{,}15$.

Actor:

- hướng $I\,\delta_0\,\psi_\theta(s_A,1)=1\cdot(-0{,}5)\cdot0{,}5\,e_A=-0{,}25\,e_A$;
- tham số mới $\theta_A=0+1\cdot(-0{,}25)=-0{,}25$;
- xác suất mới $p_A=\sigma(-0{,}25)\approx0{,}438$.

**Bước $t=1$, $I=\gamma=0{,}9$.** Critic:

- mục tiêu $R_2+\gamma(1-Z_2)\hat v(S_2,w)=3+0=3$, vì mặt nạ bằng $0$;
- sai lệch $\delta_1=3-w_B=2$;
- giá trị mới $w_B=1+0{,}5\cdot2=2$.

Actor:

- hướng $I\,\delta_1\,\psi_\theta(s_B,1)=0{,}9\cdot2\cdot\tfrac13\,e_B=0{,}6\,e_B$;
- tham số mới $\theta_B=\log2+0{,}6=1{,}2931$;
- xác suất mới $p_B=\sigma(1{,}2931)\approx0{,}785$.

**Diễn giải.** Sai số $\delta_0=-0{,}5$ âm dù $A_\pi(s_A,1)=0{,}4>0$: critic đánh giá thấp $s_B$, nên hành động 1 tại $s_A$ bị giảm xác suất, $p_A$ từ $0{,}5$ xuống $0{,}438$. Theo Mệnh đề 10.8(b) với $e=\hat v-v_\pi=(0;\,-1)$, độ chệch của $\delta_0$ là $\gamma e(s_B)-e(s_A)=-0{,}9$, và $0{,}4-0{,}9=-0{,}5$. Sai số $\delta_1=2$ dương, nên $p_B$ tăng từ $0{,}667$ lên $0{,}785$; sau bước này $w_B=2=v_\pi(s_B)$.

**Kiểm tra lại.** $\sigma(-0{,}25)=1/(1+e^{0{,}25})=1/(1+1{,}2840)=0{,}4378$; $\theta_B=0{,}6931+0{,}6=1{,}2931$ và $\sigma(1{,}2931)=1/(1+e^{-1{,}2931})=1/(1+0{,}2744)=0{,}7847$.
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

Thuật toán 10.9 thay $G_t$ của Thuật toán 10.6 bằng lợi tức một bước, theo (13.12)–(13.14) của Sutton và Barto (2018, §13.5); critic là TD(0) bán gradient (Thuật toán 07.22). Ví dụ 10.7 là hai vòng lặp của nó.

::: remark Nhận xét 10.10 (Đường cơ sở và critic; nhầm lẫn thường gặp)
1. Một nhầm lẫn thường gặp là coi mọi phương pháp có hàm giá trị học được là actor–critic theo Định nghĩa 10.7. Ước lượng của Thuật toán 10.6 không chệch với mọi $\hat v$ cố định (Mệnh đề 10.2); ước lượng của actor–critic chệch khi critic sai (ý 3).
2. Trong cập nhật actor, $\delta_t$ là một hệ số đã dừng gradient: gradient của actor không đi vào $w$. Trong cập nhật critic, mục tiêu được coi là hằng.
3. Mệnh đề 10.2 không áp dụng cho $\delta_t$: phần $-\hat v(S_t,w)$ là một đường cơ sở hợp lệ, nhưng $R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)$ (thay cho $G_t$) có kỳ vọng có điều kiện $q_\pi(S_t,A_t)+\gamma\,\mathbb E[(1-Z_{t+1})\,e(S_{t+1})\mid S_t,A_t]$, nên ước lượng gradient bị chệch khi critic sai.
:::

**Trong thực hành.** Critic là một mạng $\hat v(s,w)$, và hai cập nhật của Thuật toán 10.9 được cài đặt bằng hai hàm mất mát: $-I\operatorname{sg}(\delta_t)\log\pi_\theta(A_t\mid S_t)$ cho actor và $\tfrac12\bigl(\operatorname{sg}(R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w))-\hat v(S_t,w)\bigr)^2$ cho critic. Khi lượt bị cắt ngắn ($U_{t+1}=1$, $Z_{t+1}=0$), mục tiêu vẫn bootstrap từ quan sát cuối của lượt (Định nghĩa 08.6). Với xấp xỉ hàm, critic không bằng $v_\pi$, nên theo Mệnh đề 10.8(b) actor nhận một hệ số chệch ở mọi bước. Mỗi bước chuyển chỉ dùng một lần vì dữ liệu phải theo chính sách hiện tại.

Hệ số Monte Carlo $G_t-\hat v(S_t,w)$ không làm chệch gradient nhưng chứa mọi phần thưởng đến cuối lượt; sai số TD $\delta_t$ chỉ chứa một phần thưởng nhưng chệch khi critic sai. Sutton và Barto (2018, §13.5, tr. 331) nêu rằng lợi tức một bước thường có phương sai nhỏ hơn lợi tức thực, đổi lại có độ chệch, và mức chệch điều chỉnh được bằng lợi tức $n$ bước. Trong Mục 3, chúng ta nối hai đầu này bằng một tham số $\lambda$.

---

## 3. Ước lượng lợi thế tổng quát

Trên chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$ của Ví dụ 10.7, xét hai lượt cùng bắt đầu bằng hành động 1 ở $s_A$; tại $s_B$, lượt thứ nhất chọn hành động 1 (phần thưởng $3$, xác suất $\tfrac23$), lượt thứ hai chọn hành động 2 (phần thưởng $0$, xác suất $\tfrac13$). Lợi thế đúng là $A_\pi(s_A,1)=0{,}4$. Sai số TD cho $\delta_0=0+0{,}9\cdot1-1{,}4=-0{,}5$ ở cả hai lượt: hai giá trị bằng nhau nhưng sai dấu. Hệ số Monte Carlo $G_0-\hat v(s_A)$ cho $2{,}7-1{,}4=1{,}3$ ở lượt thứ nhất và $0-1{,}4=-1{,}4$ ở lượt thứ hai: kỳ vọng $\tfrac23\cdot1{,}3-\tfrac13\cdot1{,}4=0{,}4$ đúng, nhưng hai giá trị cách nhau $2{,}7$.

<!-- note-topic-id: lec-10-topic-07 -->
### 3.1 Lợi tức n bước

Giữa TD một bước và Monte Carlo có các phương pháp dùng vài phần thưởng thực nhận rồi thay phần còn lại của lợi tức bằng giá trị ước lượng của trạng thái đạt tới (Sutton và Barto, 2018, §7.1, tr. 142). Về mặt ý tưởng, dùng càng nhiều phần thưởng thực thì càng ít phụ thuộc critic, nhưng càng chịu nhiều ngẫu nhiên của lượt. Ví dụ sau đặt ba lựa chọn cạnh nhau trên hai lượt.

::: example Ví dụ 10.8 (Ba ước lượng lợi thế trên hai lượt của chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_A=\tfrac12$, $p_B=\tfrac23$; $v_\pi=(1{,}4;\,2)$ và lợi thế đúng $A_\pi(s_A,1)=0{,}4$. Critic cố định $\hat v=(1{,}4;\,1)$. Hai lượt cùng có $S_0=s_A$, $A_0=1$, $R_1=0$, $S_1=s_B$ và kết thúc tại $T=2$: lượt (i) có $A_1=1$, $R_2=3$, xác suất có điều kiện $\tfrac23$; lượt (ii) có $A_1=2$, $R_2=0$, xác suất $\tfrac13$.

**Sai số TD.** $\delta_0=0+0{,}9\cdot1-1{,}4=-0{,}5$ ở cả hai lượt; $\delta_1=3-1=2$ ở lượt (i) và $\delta_1=0-1=-1$ ở lượt (ii), vì mặt nạ tắt ở bước cuối.

**Ba ước lượng của $A_\pi(s_A,1)$.**

- Một bước: $R_1+\gamma\hat v(S_1)-\hat v(S_0)=\delta_0=-0{,}5$ ở cả hai lượt.
- Hai bước, ở đây trùng Monte Carlo vì $T=2$: $R_1+\gamma R_2-\hat v(S_0)$, tức $0{,}9\cdot3-1{,}4=1{,}3$ ở lượt (i) và $0-1{,}4=-1{,}4$ ở lượt (ii).
- Trộn hai ước lượng trên với trọng số $1-\lambda$ và $\lambda$, $\lambda=0{,}5$: $0{,}5\cdot(-0{,}5)+0{,}5\cdot1{,}3=0{,}4$ ở lượt (i) và $0{,}5\cdot(-0{,}5)+0{,}5\cdot(-1{,}4)=-0{,}95$ ở lượt (ii).

| Ước lượng | Lượt (i), $\tfrac23$ | Lượt (ii), $\tfrac13$ | Kỳ vọng | Khoảng cách | Phương sai |
|---|---|---|---|---|---|
| một bước | $-0{,}5$ | $-0{,}5$ | $-0{,}5$ | $0$ | $0$ |
| trộn, $\lambda=0{,}5$ | $0{,}4$ | $-0{,}95$ | $-0{,}05$ | $1{,}35$ | $0{,}405$ |
| hai bước | $1{,}3$ | $-1{,}4$ | $0{,}4$ | $2{,}7$ | $1{,}62$ |

Cột "khoảng cách" là hiệu hai giá trị trên hai lượt. Với hai giá trị có xác suất $\tfrac23$ và $\tfrac13$, phương sai bằng $\tfrac23\cdot\tfrac13$ nhân bình phương khoảng cách: $\tfrac29\cdot1{,}35^2=0{,}405$ và $\tfrac29\cdot2{,}7^2=1{,}62$.

**Diễn giải.** Ước lượng một bước như nhau trên hai lượt, nhưng có kỳ vọng $-0{,}5$, chệch $-0{,}9$ so với $0{,}4$ và sai dấu, vì critic đánh giá thấp $s_B$. Ước lượng hai bước có kỳ vọng đúng $0{,}4$, nhưng hai giá trị cách nhau $2{,}7$. Ước lượng trộn nằm giữa: độ chệch $-0{,}45$, khoảng cách $1{,}35$. Tổng quát, với $\lambda\in[0,1]$, hai giá trị là $-0{,}5+1{,}8\lambda$ và $-0{,}5-0{,}9\lambda$, kỳ vọng là $-0{,}5+0{,}9\lambda$, nên độ chệch là $-0{,}9(1-\lambda)$, khoảng cách là $2{,}7\lambda$ và phương sai là $\tfrac29(2{,}7\lambda)^2=1{,}62\lambda^2$. Với $\lambda=0{,}5$, lượt (i) cho đúng $0{,}4$ chỉ do trùng hợp; kỳ vọng theo hai lượt là $-0{,}05$.

**Kiểm tra lại.** $1{,}3=-0{,}5+0{,}9\cdot2$ và $-1{,}4=-0{,}5+0{,}9\cdot(-1)$, tức $\delta_0+\gamma\delta_1$; $0{,}4=-0{,}5+0{,}45\cdot2$ và $-0{,}95=-0{,}5+0{,}45\cdot(-1)$, tức $\delta_0+\gamma\lambda\,\delta_1$ với $\gamma\lambda=0{,}45$.
:::

Các đẳng thức ở dòng kiểm tra lại có chung một lý do: mọi ước lượng ở đây là tổng có trọng số của các sai số TD. Định nghĩa và bổ đề sau phát biểu điều này cho mọi $n$.

::: definition Định nghĩa 10.11 (Lợi tức $n$ bước, lợi thế $n$ bước)
Cho một lượt kết thúc tại $T$, một critic $\hat v(\cdot,w)$ với $w$ cố định, và $n\in\mathbb N_+$. *Lợi tức $n$ bước* (n-step return) từ bước $t<T$ là
$$\begin{aligned}&G_{t:t+n}=\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}\\&\quad+\gamma^n\hat v(S_{t+n},w)\\&\qquad\text{nếu }t+n<T,\\&G_{t:t+n}=G_t\quad\text{nếu }t+n\ge T.\end{aligned}$$
*Lợi thế $n$ bước* là $\widehat A^{(n)}_t=G_{t:t+n}-\hat v(S_t,w)$.
:::

Lợi tức $n$ bước dùng $n$ phần thưởng thực rồi bootstrap từ giá trị ước lượng của trạng thái đạt tới sau $n$ bước. Khi lượt kết thúc trước bước $t+n$, không còn gì để bootstrap và lợi tức $n$ bước là lợi tức thực. Trường hợp $n=1$ là mục tiêu TD(0) của Định nghĩa 05.20 và 07.19; trường hợp $n\ge T-t$ là lợi tức Monte Carlo. Lợi thế $n$ bước dùng $\hat v(S_t,w)$ làm đường cơ sở, như Thuật toán 10.6.

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

Bổ đề 10.12 tổng quát hóa Bài tập 05.14, trường hợp $n\ge T-t$. Giả thiết critic cố định chỉ được dùng ở Bước 2: nếu $\hat v(S_{t+1})$ trong $\delta_t$ và trong $\delta_{t+1}$ được tính với hai tham số khác nhau, hai số hạng không triệt tiêu và tổng sai lệch khỏi $\widehat A^{(n)}_t$ đúng bằng $\gamma$ nhân hiệu hai giá trị đó. Giả thiết mặt nạ được dùng ở Bước 3: nếu trạng thái kết thúc được gán $\hat v(S_T)\ne0$ mà không có mặt nạ, tổng có thêm $\gamma^{T-t}\hat v(S_T)$.

<!-- note-topic-id: lec-10-topic-08 -->
### 3.2 Lợi tức λ và ước lượng lợi thế tổng quát

Ví dụ 10.8 trộn hai lợi tức với trọng số $1-\lambda$ và $\lambda$. Sutton và Barto (2018, §12.1, tr. 288) nhận xét rằng mọi trung bình lồi của các lợi tức $n$ bước đều là một mục tiêu hợp lệ, và chọn một họ trung bình riêng: lợi tức $n$ bước nhận trọng số tỉ lệ với $\lambda^{n-1}$, chuẩn hóa bằng $1-\lambda$ để tổng các trọng số bằng $1$. Về mặt ý tưởng, so với lợi tức Monte Carlo, trung bình này nhân phần thưởng thứ $k$ sau bước $t$, tức $R_{t+k}$, với $\lambda^{k-1}$ và thay phần còn lại bằng giá trị ước lượng của critic; $\lambda$ nhỏ dựa nhiều vào critic, $\lambda$ gần $1$ dựa nhiều vào phần thưởng thực nhận.

::: definition Định nghĩa 10.13 (Lợi tức λ và ước lượng lợi thế tổng quát)
Cho lượt, critic và lợi tức $n$ bước như Định nghĩa 10.11, và $\lambda\in[0,1)$. *Lợi tức λ* (λ-return) từ bước $t<T$ là
$$\begin{aligned}&G^\lambda_t\\&\quad=(1-\lambda)\sum_{n=1}^{\infty}\lambda^{n-1}G_{t:t+n}\\&\quad=(1-\lambda)\sum_{n=1}^{T-t-1}\lambda^{n-1}G_{t:t+n}\\&\qquad+\lambda^{T-t-1}G_t,\end{aligned}$$
và với $\lambda=1$ đặt $G^1_t=G_t$, tức dạng thứ hai với $\lambda=1$. *Ước lượng lợi thế tổng quát* (generalized advantage estimation, GAE) với tham số $(\gamma,\lambda)$ là
$$\widehat A_t=G^\lambda_t-\hat v(S_t,w).$$
:::

Hai dạng của $G^\lambda_t$ bằng nhau vì mọi $n\ge T-t$ cho cùng lợi tức $G_t$, và tổng trọng số của chúng là $(1-\lambda)\sum_{n\ge T-t}\lambda^{n-1}=\lambda^{T-t-1}$. Trọng số $(1-\lambda)\lambda^{n-1}$ giảm theo cấp số nhân và cộng lại bằng $1$, nên $G^\lambda_t$ là một trung bình của các lợi tức $n$ bước. Với $\lambda=0$, chỉ lợi tức một bước có trọng số khác $0$ và $\widehat A_t=\delta_t$; với $\lambda=1$, $\widehat A_t=G_t-\hat v(S_t,w)$ là hệ số Monte Carlo của Thuật toán 10.6. Như vậy GAE chứa cả hai đầu của Mục 2. Trong Ví dụ 10.8, $T-t-1=1$ tại $t=0$, nên trên lượt (i), $G^\lambda_0=0{,}5\,G_{0:1}+0{,}5\,G_0=0{,}5\cdot0{,}9+0{,}5\cdot2{,}7=1{,}8$ và $\widehat A_0=1{,}8-1{,}4=0{,}4$.

![Hai biểu đồ cột cạnh nhau. Trái: trọng số (1 trừ lambda) nhân lambda mũ n trừ 1 của lợi tức n bước, với lambda bằng 0,8 và n từ 1 đến 6: 0,2; 0,16; 0,128; 0,102; 0,082; 0,066; một cột cuối tô sọc, lambda mũ 6 bằng 0,262, ghi phần trọng số còn lại dồn vào lợi tức thực khi lượt kết thúc. Phải: trọng số (gamma lambda) mũ k của sai số TD delta t cộng k trong GAE, với gamma bằng 0,9 và lambda bằng 0,8, k từ 0 đến 5: 1; 0,72; 0,518; 0,373; 0,269; 0,193.](img/lec-10/gae-weights.svg)

Hình dùng $\gamma=0{,}9$, $\lambda=0{,}8$. Nửa trái của hình là trọng số của từng lợi tức $n$ bước trong $G^\lambda_t$; cột sọc là phần $\lambda^{T-t-1}$ dồn vào lợi tức thực, ở đây với $T-t-1=6$. Nửa phải là trọng số $(\gamma\lambda)^k$ của sai số TD thứ $k$ trong dạng tổng của mệnh đề sau. Hai nửa mô tả cùng một ước lượng theo hai cách đếm.

::: proposition Mệnh đề 10.14 (Dạng tổng, hai đầu mút và truy hồi của GAE)
**Giả thiết.** Lượt kết thúc tại $T$; critic cố định trong cả lượt; $\delta_k$ như Bổ đề 10.12, $\delta_k=0$ với $k\ge T$; $\lambda\in[0,1]$.

**Kết luận.**

- (a) $\widehat A_t=\sum_{k=0}^{T-t-1}(\gamma\lambda)^k\,\delta_{t+k}$ với mọi $t<T$.
- (b) Với $\lambda=0$, $\widehat A_t=\delta_t$; với $\lambda=1$, $\widehat A_t=G_t-\hat v(S_t,w)$.
- (c) Đặt $\widehat A_T=0$; khi đó $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$ với $t=T-1,\dots,0$.

**Điều kiện áp dụng.** Cùng một $w$ cho mọi sai số TD của lượt.

**Phạm vi.** Đồng nhất thức trên từng lượt.
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

Dạng tổng (a) là (16) của Schulman và cộng sự (2016); truy hồi (c) cho phép tính mọi $\widehat A_t$ của một lượt bằng một lượt quét lùi. Trên lượt (i) của Ví dụ 10.8, truy hồi của lợi tức λ, $G^\lambda_t=R_{t+1}+\gamma\bigl[(1-\lambda)\hat v(S_{t+1})+\lambda G^\lambda_{t+1}\bigr]$ (Sutton và Barto, 2018, Bài tập 12.1), cho $G^\lambda_1=3$ và $G^\lambda_0=0+0{,}9(0{,}5\cdot1+0{,}5\cdot3)=1{,}8$, khớp $\widehat A_0+\hat v(s_A)=(-0{,}5+0{,}45\cdot2)+1{,}4=1{,}8$ của (a).

Còn lại câu hỏi của Mục 2: GAE có làm chệch ước lượng gradient không. Schulman và cộng sự (2016, Định nghĩa 1) gọi một ước lượng lợi thế là *γ-just* nếu thay lợi thế đúng bằng nó trong công thức gradient không đổi kỳ vọng. Mệnh đề sau cho hai điều kiện đủ.

::: proposition Mệnh đề 10.15 (GAE và gradient: tính không chệch theo nghĩa γ-just)
**Giả thiết.** MDP hữu hạn; (G1)–(G4); chính sách Markov dừng $\pi=\pi_\theta$ và trạng thái hấp thụ sau khi lượt kết thúc; critic $\hat v$ là một hàm bị chặn, cố định, của trạng thái; $\widehat A_t$ là GAE tính trên cả lượt tới khi kết thúc.

**Kết luận.** Với mỗi $t$, nếu (a) $\lambda=1$, hoặc (b) $\hat v=v_\pi$ trên $\mathcal S$ và $\lambda\in[0,1]$ tùy ý, thì
$$\begin{aligned}&\mathbb E\bigl[\widehat A_t\,\psi_t\bigr]\\&\quad=\mathbb E\bigl[A_\pi(S_t,A_t)\,\psi_t\bigr],\\&\text{do đó}\\&\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^t\widehat A_t\,\psi_t\Bigr]=\nabla_\theta J(\theta).\end{aligned}$$

**Điều kiện áp dụng.** Lượt kết thúc trong dữ liệu, không bị cắt giữa chừng; các hàm điểm tính tại tham số đã sinh lượt.

**Phạm vi.** Bảo đảm thuộc về ước lượng gradient; kỳ vọng có điều kiện $\mathbb E[\widehat A_t\mid S_t,A_t]$ có thể khác $A_\pi(S_t,A_t)$ (Ví dụ 10.9). Với $\lambda<1$ và $\hat v\ne v_\pi$, mệnh đề không cho bảo đảm nào.
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

Đọc bằng lời, GAE không làm chệch gradient khi nó là hệ số Monte Carlo trừ một đường cơ sở ($\lambda=1$), hoặc khi mọi sai số TD đều có kỳ vọng có điều kiện bằng lợi thế ($\hat v=v_\pi$). Đây là Mệnh đề 1 của Schulman và cộng sự (2016, chứng minh ở Phụ lục B). Hai điều kiện có vai trò riêng.

- Bỏ cả hai điều kiện: với $\lambda=0{,}5$ và $\hat v=(1{,}4;\,1)$ trên chuỗi hai trạng thái, tọa độ $\theta_A$ của $\mathbb E[\widehat A_0\psi_0]$ là $0{,}0875$, khác giá trị đúng $0{,}2$ (Ví dụ 10.9 dưới đây).
- Bỏ "lượt kết thúc trong dữ liệu": nếu lượt của chuỗi bị cắt ngay khi tới $s_B$ và bootstrap bằng $\hat v(s_B)=1$, thì kể cả với $\lambda=1$, $\widehat A_0=\delta_0$, tức $-0{,}5$ khi chọn hành động 1 và $-0{,}4$ khi chọn hành động 2, và tọa độ $\theta_A$ của kỳ vọng là $-0{,}025\ne0{,}2$.

Bước 1 dùng $\lambda=1$ cùng lượt đầy đủ, để $\widehat A_t$ là $G_t$ trừ một đường cơ sở; Bước 3–4 dùng $\hat v=v_\pi$ qua Mệnh đề 10.8(a). Một nhầm lẫn thường gặp là đọc mệnh đề thành "GAE với $\lambda=1$ là ước lượng không chệch của lợi thế". Ví dụ sau cho thấy điều đó sai.

::: example Ví dụ 10.9 (Kỳ vọng và gradient của GAE trên chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái như Ví dụ 10.8: $\gamma=0{,}9$, $p_A=\tfrac12$, $p_B=\tfrac23$, $v_\pi=(1{,}4;\,2)$, critic cố định $\hat v=(1{,}4;\,1)$; lợi thế đúng $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$ và $A_\pi(s_B,\cdot)=(1;\,-2)$; hàm điểm $\psi_\theta(s_A,1)=0{,}5\,e_A$, $\psi_\theta(s_A,2)=-0{,}5\,e_A$, $\psi_\theta(s_B,1)=\tfrac13e_B$, $\psi_\theta(s_B,2)=-\tfrac23e_B$; gradient đúng $(0{,}2;\,0{,}3)$ (Ví dụ 10.6).

**Hành động 1 tại $s_A$.** $\delta_0=-0{,}5$ là tất định; $\delta_1=R_2-1$ có kỳ vọng $\tfrac23\cdot3-1=1$. Theo Mệnh đề 10.14(a), $\mathbb E[\widehat A_0\mid s_A,1]=-0{,}5+0{,}9\lambda\cdot1$, tức $-0{,}5$; $-0{,}05$; $0{,}4$ với $\lambda=0$; $0{,}5$; $1$, so với $A_\pi(s_A,1)=0{,}4$.

**Hành động 2 tại $s_A$.** Lượt kết thúc với phần thưởng $1$, nên $\widehat A_0=\delta_0=1-1{,}4=-0{,}4$ với mọi $\lambda$, bằng $A_\pi(s_A,2)$.

**Bước $t=1$ tại $s_B$.** Lượt kết thúc sau bước này, nên $\widehat A_1=\delta_1=R_2-1$ với mọi $\lambda$: $\mathbb E[\widehat A_1\mid s_B,1]=2$ và $\mathbb E[\widehat A_1\mid s_B,2]=-1$, so với $A_\pi(s_B,\cdot)=(1;\,-2)$.

**Gradient.** Tọa độ $\theta_A$ của $\mathbb E[\widehat A_0\psi_0]$ là $\tfrac12\cdot\mathbb E[\widehat A_0\mid s_A,1]\cdot0{,}5+\tfrac12\cdot(-0{,}4)\cdot(-0{,}5)=-0{,}025+0{,}225\lambda$, tức $-0{,}025$; $0{,}0875$; $0{,}2$ với $\lambda=0$; $0{,}5$; $1$. Tọa độ $\theta_B$ của $\mathbb E[\gamma\widehat A_1\psi_1]$ là $0{,}9\cdot\tfrac12\bigl(\tfrac23\cdot2\cdot\tfrac13+\tfrac13\cdot(-1)\cdot(-\tfrac23)\bigr)=0{,}45\cdot\tfrac23=0{,}3$ với mọi $\lambda$.

**Diễn giải.** Tại $s_B$, với mọi $\lambda$, kể cả $\lambda=1$, lợi thế ước lượng chệch $+1$ ở cả hai hành động; phần chệch bị khử khi nhân với hàm điểm có kỳ vọng $0$, nên tọa độ $\theta_B$ của gradient đúng dù lợi thế sai. Tại $s_A$ với $\lambda<1$, độ chệch là $-0{,}9(1-\lambda)$ ở hành động 1 và $0$ ở hành động 2, nên không bị khử; với $\lambda=0$, tọa độ $\theta_A$ âm, ngược dấu giá trị đúng $0{,}2$. Với $\lambda=1$, $\widehat A_0=G_0-\hat v(s_A)$ không chệch vì $\hat v(s_A)=v_\pi(s_A)$.

**Kiểm tra lại.** Giá trị đúng: $0{,}5\cdot0{,}4\cdot0{,}5+0{,}5\cdot(-0{,}4)(-0{,}5)=0{,}2$ và $0{,}45\bigl(\tfrac23\cdot1\cdot\tfrac13+\tfrac13\cdot(-2)(-\tfrac23)\bigr)=0{,}3$.
:::

**Trong thực hành.** Critic học được không bằng $v_\pi$, và các cài đặt dùng $\lambda<1$, nên Mệnh đề 10.15 không bảo đảm ước lượng gradient bằng GAE là γ-just. Schulman và cộng sự (2016, §3) nêu định tính một đánh đổi giữa độ chệch và phương sai theo $\lambda$: GAE với $\lambda=1$ γ-just bất kể critic nhưng có phương sai cao vì là tổng của nhiều số hạng, còn GAE với $\lambda=0$ chệch khi critic sai nhưng thường có phương sai thấp hơn nhiều.

<!-- note-topic-id: lec-10-topic-09 -->
### 3.3 GAE trên đoạn thu

Mệnh đề 10.14 giả sử có cả lượt. Dữ liệu của PPO gồm các *đoạn thu* (rollout) độ dài $h$ trên $N$ môi trường chạy song song: trong một đoạn, một lượt có thể kết thúc, bị cắt ngắn vì giới hạn thời gian, hoặc còn dở ở biên đoạn. Về mặt ý tưởng, bước cuối của mỗi lượt trong đoạn thuộc một trong hai loại: kết thúc thật, khi phần tương lai bằng $0$; cắt ngắn hoặc dừng ở biên đoạn, khi phần tương lai còn nhưng không được thu, nên được thay bằng giá trị ước lượng của critic. Ví dụ sau cho thấy kết quả phụ thuộc cờ nào dùng ở đâu.

::: example Ví dụ 10.10 (Kết thúc và cắt ngắn)
**Dữ kiện.** Đoạn hai bước của một môi trường, $\gamma=0{,}9$, $\lambda=0{,}8$; $R_1=1$, $R_2=2$; critic cũ cho $\hat v(S_0)=2$, $\hat v(S_1)=3$; $Z_1=U_1=0$. Hai trường hợp sau bước $2$: (i) $S_2$ là trạng thái kết thúc, $Z_2=1$; (ii) lượt bị cắt ở bước $2$ vì giới hạn thời gian, $U_2=1$, $Z_2=0$, và critic cho quan sát cuối $S_2$ giá trị $\hat v(S_2)=4$.

**Bước $t=0$.** $\delta_0=1+0{,}9\cdot3-2=1{,}7$ trong cả hai trường hợp.

**Trường hợp (i).** Mặt nạ tắt: $\delta_1=2-3=-1$, $\widehat A_1=-1$, và $\widehat A_0=1{,}7+0{,}72\cdot(-1)=0{,}98$.

**Trường hợp (ii).** Mặt nạ không tắt: $\delta_1=2+0{,}9\cdot4-3=2{,}6$, $\widehat A_1=2{,}6$, và $\widehat A_0=1{,}7+0{,}72\cdot2{,}6=3{,}572$.

**Diễn giải.** Cùng phần thưởng, cùng critic, hai cờ cho hai kết quả cách nhau $2{,}592$. Ở (ii), trạng thái $S_2$ vẫn có tương lai, nên giá trị của nó đi vào sai số TD.

**Kiểm tra lại.** Ở (ii), $\widehat A_0+\hat v(S_0)=5{,}572$ phải bằng *lợi tức λ cắt* (truncated λ-return) tại bước $2$ của Sutton và Barto (2018, (12.9)): $G_{0:1}=1+0{,}9\cdot3=3{,}7$, $G_{0:2}=1+0{,}9\cdot2+0{,}81\cdot4=6{,}04$, và $0{,}2\cdot3{,}7+0{,}8\cdot6{,}04=5{,}572$.
:::

Trên chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$, giả sử lượt bị cắt vì giới hạn thời gian ngay khi vừa tới $s_B$: $U_1=1$, $Z_1=0$. Trạng thái $s_B$ còn tương lai, nên sai số TD của bước $0$ giữ phần bootstrap, $\delta_0=0+0{,}9\cdot1-1{,}4=-0{,}5$, như trường hợp (ii). Ghi nhầm bước cắt thành kết thúc, $Z_1=1$, xóa phần đó và cho $\delta_0=0-1{,}4=-1{,}4$.

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

Với $w$ cố định, $V^{\mathrm{targ}}_t$ là lợi tức λ cắt tại biên gần nhất của bước $t$, tức kết thúc, cắt ngắn hoặc biên đoạn (Sutton và Barto, 2018, (12.9)–(12.10), tr. 296–297); Ví dụ 10.10(ii) là trường hợp $h=2$. Hai bước của Ví dụ 10.10 là hai vòng của bước 3.

Ghép Thuật toán 10.9 và 10.16 cho phương pháp actor–critic với GAE. Thuật toán 10.9 cập nhật sau từng bước với hệ số $\delta_t$; ở đây chúng ta chờ hết lượt, hoặc hết đoạn thu, rồi dùng hệ số $\widehat A_t$. Với chính sách $\pi_\theta$, critic $\hat v(s,w)$, $\gamma\in[0,1)$, $\lambda\in[0,1]$ và hai bước học $\alpha_\theta$, $\alpha_w$, mỗi vòng gồm bốn việc:

1. **Thu lượt.** Thu một lượt $S_0,A_0,R_1,\dots,S_T$ bằng $\pi_\theta$ và giữ $w_{\mathrm{old}}=w$.
2. **Ước lượng lợi thế.** Tính $\delta_t$ với $\hat v(\cdot,w_{\mathrm{old}})$, đặt $\widehat A_T=0$ và tính lùi $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$ (Mệnh đề 10.14(c); trên đoạn thu, Thuật toán 10.16).
3. **Cập nhật actor.** $\theta\leftarrow\theta+\alpha_\theta\sum_t\gamma^t\widehat A_t\,\psi_\theta(S_t,A_t)$.
4. **Cập nhật critic.** Hồi quy $\hat v(S_t,w)$ về mục tiêu $V^{\mathrm{targ}}_t=\widehat A_t+\hat v(S_t,w_{\mathrm{old}})$; một bước hạ gradient là $w\leftarrow w_{\mathrm{old}}+\alpha_w\sum_t\bigl(V^{\mathrm{targ}}_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\nabla_w\hat v(S_t,w_{\mathrm{old}})$.

Với $\lambda=1$, hệ số $\widehat A_t=G_t-\hat v(S_t,w_{\mathrm{old}})$ và vòng lặp là Thuật toán 10.6. Với $\lambda=0$, hệ số là $\delta_t$, như Thuật toán 10.9, nhưng mọi cập nhật dùng cùng $w_{\mathrm{old}}$ và diễn ra sau khi thu xong lượt.

Trên lượt (i) của Ví dụ 10.8 ($s_A\xrightarrow1s_B\xrightarrow1$, critic $\hat v=(1{,}4;\,1)$), với $\lambda=0{,}5$, $\alpha_\theta=1$, $\alpha_w=0{,}5$ và $\theta=(0;\,\log2)$ như Ví dụ 10.7, một vòng cho:

- lợi thế: $\widehat A_1=\delta_1=2$ và $\widehat A_0=-0{,}5+0{,}9\cdot0{,}5\cdot2=0{,}4$;
- actor tại $s_A$: $\theta_A=0+1\cdot0{,}4\cdot0{,}5=0{,}2$, $p_A=\sigma(0{,}2)\approx0{,}550$;
- actor tại $s_B$, với trọng số $\gamma=0{,}9$: $\theta_B=\log2+0{,}9\cdot2\cdot\tfrac13=\log2+0{,}6$, $p_B=\sigma(1{,}293)\approx0{,}785$;
- critic: mục tiêu $V^{\mathrm{targ}}_0=0{,}4+1{,}4=1{,}8$ và $V^{\mathrm{targ}}_1=2+1=3$, nên $w=(1{,}4+0{,}5\cdot0{,}4;\,1+0{,}5\cdot2)=(1{,}6;\,2)$.

Sau vòng này $J=2{,}7\cdot0{,}550\cdot0{,}785+0{,}450\approx1{,}615$. Trên cùng lượt, với $\lambda=0$ (Ví dụ 10.7), $\widehat A_0=-0{,}5$ và $p_A$ giảm xuống $0{,}438$.

::: remark Nhận xét 10.17 (Vai trò của $\gamma$ và các nhầm lẫn)
1. Ước lượng gradient của TRPO và PPO tỉ lệ với $\sum_t\widehat A_t\psi_t$, không có trọng số $\gamma^t$. Kỳ vọng của nó, khi GAE γ-just, là $\mathbb E\bigl[\sum_tA_\pi(S_t,A_t)\psi_t\bigr]$, tức $g^\gamma$ của Schulman và cộng sự (2016, (6)), không phải $\nabla_\theta J$ (Ví dụ 09.21; Nota và Thomas, 2020).
2. Ghi một bước cắt ngắn thành kết thúc, $Z=1$, xóa phần bootstrap $\gamma\hat v$ của quan sát cuối: mục tiêu của critic mất giá trị của tương lai, và actor bị phạt ở các bước gần giới hạn thời gian dù chúng không khác các bước khác.
3. Trên đoạn thu, Mệnh đề 10.15(a) không áp dụng cho các lượt bị cắt ở biên, vì $\widehat A_t$ khi đó bootstrap từ $\hat v(S_h)$.
:::

**Trong thực hành.** Bộ đệm lưu các mảng cỡ $h\times N$ cho $R$, $Z$, $U$, $V$, cộng giá trị của các quan sát cuối khi cắt ngắn và $N$ giá trị tại biên đoạn; Thuật toán 10.16 chạy độc lập trên từng cột môi trường. Mục tiêu $V^{\mathrm{targ}}_t$ dùng lợi thế trước khi chuẩn hóa, vì nó là một lợi tức λ.

GAE (Mệnh đề 10.14, Thuật toán 10.16) và mọi ước lượng khác của Mục 2–3 vẫn cần dữ liệu của chính sách đang được cập nhật, nên giới hạn thứ hai của Mục 1 còn nguyên: sau một bước, dữ liệu đã cũ. Trong Mục 4, chúng ta tìm một công thức chính xác cho mức thay đổi $J(\pi')-J(\pi)$ rồi xấp xỉ nó bằng dữ liệu của $\pi$.

---

## 4. Hàm thay thế và miền tin cậy

Trên chuỗi hai trạng thái của Ví dụ 10.6, chính sách cũ $\pi$ có $\theta=(0;\,\log2)$, tức $p_A=\tfrac12$, $p_B=\tfrac23$, $J(\pi)=1{,}4$, và $\nabla_\theta J=(0{,}2;\,0{,}3)$. Gradient không cho độ dài bước, như trên hành lang ngắn của Mục 1. Xét ứng viên $\tilde\pi$ với $\tilde\theta=(\log9;\,0)$, tức $\tilde p_A=0{,}9$, $\tilde p_B=0{,}5$; ứng viên này giảm $p_B$, nên không nằm trên hướng gradient. Theo $J=2{,}7p_Ap_B+1-p_A$, $J(\tilde\pi)=1{,}315<1{,}4$, nhưng tác tử chỉ biết điều đó sau khi chạy $\tilde\pi$.

**Câu hỏi.** Từ bộ đệm đã thu bằng $\pi$, đánh giá một ứng viên như $\tilde\pi$ trước khi chạy nó thế nào?

**Câu hỏi.** Phép đánh giá đó đáng tin đến khoảng cách nào giữa hai chính sách?

![Vòng phản hồi bốn khung. Khung một: pi old sinh dữ liệu S t, A t, R t+1, trạng thái theo nu mũ pi old. Khung hai: ước lượng lợi thế A mũ t, tính bước từ theta old tới theta. Khung ba: chính sách mới pi theta. Khung bốn: pi theta thăm trạng thái theo nu mũ pi theta, khác nu mũ pi old. Mũi tên nét đứt từ khung bốn về khung một: dữ liệu theo nu mũ pi theta chỉ có sau khi chạy pi theta.](img/lec-10/policy-update-feedback.svg)

Trên hình, mũi tên nét đứt cho thấy phân bố trạng thái của chính sách mới chỉ quan sát được sau khi cập nhật.

<!-- note-topic-id: lec-10-topic-10 -->
### 4.1 Đánh giá chính sách mới trước khi chạy

Đổi chính sách đổi cả hành động tại mỗi trạng thái lẫn các trạng thái mà lượt đi qua, như ví dụ sau.

::: example Ví dụ 10.11 (Hai chính sách mới trên chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_s=\sigma(\theta_s)$ và $J=2{,}7p_Ap_B+1-p_A$. Chính sách cũ $\pi$: $(p_A;\,p_B)=(\tfrac12;\,\tfrac23)$, $J(\pi)=1{,}4$. Hai chính sách mới: $\pi'$ với $(p'_A;\,p'_B)=(0{,}6;\,0{,}8)$, và $\tilde\pi$ với $\tilde\theta=(\log9;\,0)$, $(\tilde p_A;\,\tilde p_B)=(0{,}9;\,0{,}5)$.

**Giá trị thật.** $v_{\pi'}(s_B)=0{,}8\cdot3=2{,}4$ và $J(\pi')=0{,}6\cdot0{,}9\cdot2{,}4+0{,}4\cdot1=1{,}696$, nên $J(\pi')-J(\pi)=0{,}296$. Với $\tilde\pi$: $v_{\tilde\pi}(s_B)=1{,}5$ và $J(\tilde\pi)=0{,}9\cdot0{,}9\cdot1{,}5+0{,}1=1{,}315$, nên $J(\tilde\pi)-J(\pi)=-0{,}085$.

**Luồng 100 lượt.** Mỗi lượt rẽ theo hành động tại $s_A$, rồi theo hành động tại $s_B$ nếu tới đó. Số lượt kỳ vọng trong $100$ lượt là $100$ nhân xác suất của nhánh:

| Chính sách | tới $s_B$ | nhận $3$ tại $s_B$ | nhận $0$ tại $s_B$ | nhận $1$ tại $s_A$ |
|---|---|---|---|---|
| $\pi=(0{,}5;\,\tfrac23)$ | $50$ | $33\tfrac13$ | $16\tfrac23$ | $50$ |
| $\tilde\pi=(0{,}9;\,0{,}5)$ | $90$ | $45$ | $45$ | $10$ |

Chẳng hạn $100\cdot\tfrac12\cdot\tfrac23=33\tfrac13$; làm tròn tới số nguyên, chính sách cũ cho $33$ và $17$ lượt ở hai nhánh tại $s_B$.

**Diễn giải.** $\tilde\pi$ tới $s_B$ nhiều hơn $\pi$, nhưng tại đó chọn hành động 1 ít hơn: số lượt nhận $0$ tăng từ khoảng $17$ lên $45$.

**Kiểm tra lại.** Phần thưởng $3$ ở bước 1 có giá trị $\gamma\cdot3=2{,}7$. Theo bảng, $J(\tilde\pi)=\tfrac1{100}(45\cdot2{,}7+10\cdot1)=1{,}315$ và $J(\pi)=\tfrac1{100}(33\tfrac13\cdot2{,}7+50\cdot1)=1{,}4$.
:::

Ví dụ 10.11 cho thấy hai thay đổi khác loại khi chuyển từ $\pi$ sang $\tilde\pi$.

- *Phân phối hành động* tại một trạng thái: tại $s_B$, xác suất chọn hành động 1 giảm từ $\tfrac23$ xuống $\tfrac12$.
- *Phân bố trạng thái*: tỉ lệ lượt tới $s_B$ tăng từ $50\%$ lên $90\%$.

Khác với học có giám sát, nơi tập dữ liệu cố định, trong Học tăng cường chính sách mới đổi cả phân bố của các trạng thái mà tác tử sẽ gặp.

Với chính sách $\pi$ và một chính sách khác $\pi'$, đặt $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$, kỳ vọng của $A_\pi(s,A)$ khi $A\sim\pi'(\cdot\mid s)$. Vì $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)q_\pi(s,a)-v_\pi(s)$, đại lượng này là mức tăng lợi tức kỳ vọng khi tại $s$ chọn hành động theo $\pi'$ rồi từ bước sau theo $\pi$, so với theo $\pi$ ngay từ $s$. Trên chuỗi, với $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$ (Ví dụ 10.6):

- $A_\pi(s_A,\pi')=0{,}6\cdot0{,}4+0{,}4\cdot(-0{,}4)=0{,}08$ và $A_\pi(s_B,\pi')=0{,}8\cdot1+0{,}2\cdot(-2)=0{,}4$;
- $A_\pi(s_A,\tilde\pi)=0{,}9\cdot0{,}4+0{,}1\cdot(-0{,}4)=0{,}32$ và $A_\pi(s_B,\tilde\pi)=0{,}5\cdot1+0{,}5\cdot(-2)=-0{,}5$.

Một cách trực quan, nếu chính sách mới chọn hành động có lợi thế dương ở những trạng thái nó hay thăm, thì nó tốt hơn chính sách cũ. Cộng theo bước thời gian, bước $1$ ở $s_B$ có trọng số $\gamma$ nhân xác suất tới $s_B$:

- Với $\pi'$: $0{,}08+0{,}9\cdot0{,}6\cdot0{,}4=0{,}296$.
- Với $\tilde\pi$: $0{,}32+0{,}9\cdot0{,}9\cdot(-0{,}5)=0{,}32-0{,}405=-0{,}085$.

Hai tổng bằng đúng mức thay đổi thật. Mỗi tổng gồm ba thành phần: tần suất chính sách mới thăm mỗi trạng thái, phân phối hành động mới, và lợi thế cũ. Để viết phép cộng này cho MDP tổng quát, chúng ta cần phân bố chiếm dụng trên các trạng thái chưa kết thúc.

::: definition Định nghĩa 10.18 (Phân bố chiếm dụng trên tập trạng thái chưa kết thúc)
Cho MDP hữu hạn với tập trạng thái chưa kết thúc $\mathcal S=\{s_1,\dots,s_n\}$, phân phối đầu $\mu_0$ trên $\mathcal S$, $0\le\gamma<1$, và chính sách Markov dừng $\pi$. *Phân bố chiếm dụng chiết khấu* của $\pi$ là
$$\begin{aligned}&\nu^\pi(s)\\&=(1-\gamma)\sum_{t\ge0}\gamma^t\\&\quad\times\Pr_\pi(S_t=s,\ t<T),\\&s\in\mathcal S .\end{aligned}$$
Ở dạng véc-tơ hàng, $\nu^{\pi\top}=(1-\gamma)\,\mu_0^\top\Gamma_\pi$ với $\Gamma_\pi=(I-\gamma P_\pi)^{-1}$. Tổng khối lượng xác suất của nó, gọi tắt là khối, là $\nu^\pi(\mathcal S)=\sum_{s\in\mathcal S}\nu^\pi(s)=1-\mathbb E_\pi[\gamma^T]\le1$, với quy ước $\gamma^T=0$ khi lượt không kết thúc. Với hàm $f$ trên $\mathcal S$, viết $\mathbb E_{S\sim\nu^\pi}[f(S)]=\sum_{s\in\mathcal S}\nu^\pi(s)f(s)$.
:::

Theo tính Markov, $\Pr_\pi(S_{t+1}=s',\,t+1<T)=\sum_{s\in\mathcal S}\Pr_\pi(S_t=s,\,t<T)\,(P_\pi)_{ss'}$, nên véc-tơ hàng của các xác suất này là $\mu_0^\top P_\pi^t$; Định lý 03.28 cho $\sum_t\gamma^tP_\pi^t=\Gamma_\pi$. Khối bằng $(1-\gamma)\mathbb E_\pi\bigl[\sum_{t<T}\gamma^t\bigr]=\mathbb E_\pi[1-\gamma^T]$.

Trên $\mathcal S$, $\nu^\pi$ trùng phân bố $\nu^\pi_\gamma$ của Hệ quả 09.24, phân bố này dồn phần khối $1-\nu^\pi(\mathcal S)$ vào trạng thái hấp thụ. Tại đó $q_\pi=A_\pi=0$ và mọi khoảng cách giữa hai chính sách bằng $0$, nên các kỳ vọng của chương, như Mệnh đề 10.5(b), không đổi. Trên chuỗi, $\nu^\pi=(0{,}1;\,0{,}1\cdot0{,}9\cdot p_A)=(0{,}1;\,0{,}045)$, khối $0{,}145=1-(0{,}5\cdot0{,}9+0{,}5\cdot0{,}81)$; $\nu^{\pi'}=(0{,}1;\,0{,}054)$ và $\nu^{\tilde\pi}=(0{,}1;\,0{,}081)$.

Bổ đề sau, theo Kakade và Langford (2002, Bổ đề 6.1), là dạng tổng quát của phép cộng theo bước thời gian trên chuỗi.

::: lemma Bổ đề 10.19 (Chênh lệch hiệu năng)
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

Bổ đề nói rằng mức cải thiện của $\pi'$ so với $\pi$ là tổng chiết khấu của lợi thế của $\pi$ nhưng cộng dọc các quỹ đạo của $\pi'$. Với số lần thăm có chiết khấu
$$\begin{aligned}\eta_{\pi'}(s)&=\sum_{t\ge0}\gamma^t\Pr_{\pi'}(S_t=s,\,t<T)\\&=\frac{\nu^{\pi'}(s)}{1-\gamma},\end{aligned}$$
kết luận của bổ đề có dạng
$$J(\pi')-J(\pi)=\sum_{s\in\mathcal S}\eta_{\pi'}(s)\,A_\pi(s,\pi').$$
Mỗi lần $\pi'$ thăm $s$, tính với trọng số $\gamma^t$, đóng góp $A_\pi(s,\pi')$. Trên Ví dụ 10.11, $\eta_{\pi'}=(1;\,0{,}54)$ và $\eta_{\tilde\pi}=(1;\,0{,}81)$ cho đúng hai tổng $0{,}296$ và $-0{,}085$ ở trên. Hai giả thiết có vai trò riêng.

- Bỏ "cùng $\mu_0$": nếu $\pi'$ xuất phát từ $s_B$ còn $\pi$ từ $s_A$ trên chuỗi hai trạng thái, vế trái là $2{,}4-1{,}4=1$, còn vế phải tính trên quỹ đạo của $\pi'$ từ $s_B$ là $A_\pi(s_B,\pi')=0{,}4=v_{\pi'}(s_B)-v_\pi(s_B)$.
- Bỏ "cùng động lực $P$": nếu $\pi'$ chạy trong một môi trường khác, Bước 2 không còn đúng vì $\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t,A_t]$ không còn bằng $q_\pi(S_t,A_t)$.

Bước 2 dùng cùng $P$ và tính Markov; Bước 4 dùng cùng $\mu_0$ và phần thưởng bị chặn; $\gamma<1$ được dùng ở Bước 4 và Bước 5. Nhầm lẫn thường gặp là đổi vai hai chính sách: với $\pi'$, lấy xác suất tới $s_B$ của $\pi$ thay cho của $\pi'$ cho $0{,}08+0{,}9\cdot0{,}5\cdot0{,}4=0{,}26$, lệch $0{,}036$ so với $0{,}296$.

**Trong thực hành.** Đẳng thức của Bổ đề 10.19 là chuẩn để đo sai số của mọi phép xấp xỉ chỉ dùng dữ liệu cũ.

Lấy $\mu_0$ tập trung tại một trạng thái, ta được tiêu chuẩn cải thiện chính sách cho cả $\pi'$ ngẫu nhiên.

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

Định lý 04.13(a)–(b) là trường hợp $\pi'$ xác định: khi đó $A_\pi(s,\pi')=q_\pi(s,\pi'(s))-v_\pi(s)$, và điều kiện $q_\pi(s,\pi'(s))\ge v_\pi(s)$ của Định lý 04.13 chính là $A_\pi(s,\pi')\ge0$. Trên Ví dụ 10.11, $A_\pi(s_A,\pi')=0{,}08$ và $A_\pi(s_B,\pi')=0{,}4$ đều dương, và đúng là $v_{\pi'}=(1{,}696;\,2{,}4)>v_\pi=(1{,}4;\,2)$.

Trong vế phải của Bổ đề 10.19, lợi thế $A_\pi$ ước lượng được từ dữ liệu của $\pi$ (Mục 2–3) và $\pi'(\cdot\mid s)$ là của ứng viên. Đại lượng chưa biết là $\eta_{\pi'}$: khi không có mô hình, nó chỉ ước lượng được từ các lượt của $\pi'$.

<!-- note-topic-id: lec-10-topic-11 -->
### 4.2 Hàm thay thế

Bổ đề 10.19 cho mức thay đổi thật $\Delta J=J(\pi')-J(\pi)=\sum_s\eta_{\pi'}(s)\,A_\pi(s,\pi')$. Về mặt ý tưởng, chúng ta thay đúng một đại lượng, $\eta_{\pi'}$ bằng $\eta_\pi$, và giữ nguyên lợi thế cũ cùng phân phối hành động mới:
$$\Delta\mathcal L=\sum_{s\in\mathcal S}\eta_\pi(s)\,A_\pi(s,\pi').$$
$\Delta\mathcal L$ là mức tăng của $J$ nếu tác tử vẫn gặp các trạng thái với tần suất như trước. Trên chuỗi, $\eta_\pi=(1;\,0{,}45)$; với $\pi'$, $\Delta\mathcal L=0{,}08+0{,}45\cdot0{,}4=0{,}26$, so với $\Delta J=0{,}296$; với $\tilde\pi$, $\Delta\mathcal L=0{,}32+0{,}45\cdot(-0{,}5)=0{,}095$, so với $\Delta J=-0{,}085$.

Bộ đệm chứa hành động chọn theo $\pi$, còn $A_\pi(s,\pi')$ là kỳ vọng theo $\pi'(\cdot\mid s)$. Phép *lấy mẫu quan trọng* (importance sampling) nhân lợi thế của mỗi hành động đã lấy mẫu với tỉ số lấy mẫu quan trọng của Định nghĩa 06.24:
$$\begin{aligned}&\sum_a\pi'(a\mid s)A_\pi(s,a)\\&\quad=\sum_a\pi(a\mid s)\,\frac{\pi'(a\mid s)}{\pi(a\mid s)}\,A_\pi(s,a),\end{aligned}$$
đúng khi $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$.

::: definition Định nghĩa 10.21 (Tỉ số chính sách, hàm thay thế)
Cho chính sách cũ $\pi_{\mathrm{old}}=\pi_{\theta_{\mathrm{old}}}$ với lợi thế $A_{\mathrm{old}}=A_{\pi_{\mathrm{old}}}$ và phân bố chiếm dụng $\nu^{\mathrm{old}}=\nu^{\pi_{\mathrm{old}}}$, và chính sách $\pi_\theta$. *Hàm thay thế* (surrogate objective) là
$$\begin{aligned}&\mathcal L_{\theta_{\mathrm{old}}}(\theta)\\&=J(\theta_{\mathrm{old}})\\&\quad+\frac1{1-\gamma}\sum_{s\in\mathcal S}\nu^{\mathrm{old}}(s)\\&\qquad\times A_{\mathrm{old}}(s,\pi_\theta).\end{aligned}$$
*Tỉ số chính sách* (probability ratio) tại cặp $(s,a)$ với $\pi_{\mathrm{old}}(a\mid s)>0$ là $\rho_\theta(s,a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$; với mẫu $(S_t,A_t)$, $A_t\sim\pi_{\mathrm{old}}(\cdot\mid S_t)$, viết
$$\rho_t(\theta)=\frac{\pi_\theta(A_t\mid S_t)}{\pi_{\mathrm{old}}(A_t\mid S_t)}.$$
Khi $\pi_\theta$ thỏa điều kiện hỗ trợ $\pi_\theta(a\mid s)>0\Rightarrow\pi_{\mathrm{old}}(a\mid s)>0$, hàm thay thế viết được ở *dạng tỉ số*
$$\begin{aligned}&\mathcal L_{\theta_{\mathrm{old}}}(\theta)\\&=J(\theta_{\mathrm{old}})\\&\quad+\frac1{1-\gamma}\,\mathbb E_{\substack{S\sim\nu^{\mathrm{old}}\\A\sim\pi_{\mathrm{old}}(\cdot\mid S)}}\bigl[\rho_\theta(S,A)\\&\qquad\times A_{\mathrm{old}}(S,A)\bigr].\end{aligned}$$
:::

Khi viết theo chính sách, với $\pi=\pi_{\mathrm{old}}$ và $\pi'=\pi_\theta$, ta ký hiệu cùng đại lượng đó là $\mathcal L_\pi(\pi')$. Theo $\eta_\pi=\nu^\pi/(1-\gamma)$,
$$\begin{aligned}\mathcal L_\pi(\pi')&=J(\pi)+\sum_{s\in\mathcal S}\eta_\pi(s)\,A_\pi(s,\pi')\\&=J(\pi)+\Delta\mathcal L.\end{aligned}$$
Ngoài $\pi'(\cdot\mid s)$, mọi đại lượng ở vế phải là của $\pi$, nên $\mathcal L_\pi(\pi')$ tính được mà không chạy $\pi'$.

Trên bộ đệm $\mathcal D$ gồm $N$ mẫu của $\pi_{\mathrm{old}}$, với lợi thế ước lượng $\widehat A_t$, dạng tỉ số cho *mục tiêu mẫu*
$$\widehat{\mathcal L}(\theta)=\frac1N\sum_{t=1}^N\rho_t(\theta)\,\widehat A_t.$$
Nếu các trạng thái được lấy theo phân bố chuẩn hóa $\nu^{\mathrm{old}}/\nu^{\mathrm{old}}(\mathcal S)$ và $\widehat A_t=A_{\mathrm{old}}(S_t,A_t)$, thì $\mathbb E[\widehat{\mathcal L}(\theta)]=\frac{1-\gamma}{\nu^{\mathrm{old}}(\mathcal S)}\,\Delta\mathcal L$, một bội dương của $\Delta\mathcal L$. Bộ đệm thực tế lấy trung bình đều, không có trọng số $\gamma^t$.

Bảng sau tóm tắt ba thành phần.

| Thành phần | Trong $\Delta J$ | Trong $\Delta\mathcal L$ | Trên bộ đệm của $\pi$ |
|---|---|---|---|
| phân bố trạng thái | $\eta_{\pi'}$ | $\eta_\pi$ | chưa hiệu chỉnh: trạng thái gặp theo $\pi$ |
| phân phối hành động | $\pi'(\cdot\mid s)$ | $\pi'(\cdot\mid s)$ | đã hiệu chỉnh bằng tỉ số $\rho_\theta(s,a)$ |
| lợi thế | $A_\pi$ | $A_\pi$ | ước lượng bằng critic hoặc GAE |

**Câu hỏi.** Vì sao tỉ số chính sách không biến hàm thay thế thành mức thay đổi thật của $J$? Tỉ số chỉ hiệu chỉnh phân phối hành động; phân bố trạng thái vẫn là của $\pi$. Với $\tilde\pi$, $\Delta\mathcal L$ vẫn tính $s_B$ với số lần thăm $0{,}45$ của $\pi$ thay cho $0{,}81$.

Mệnh đề sau so $\mathcal L_{\theta_{\mathrm{old}}}$ với $J$ tại $\theta_{\mathrm{old}}$.

::: proposition Mệnh đề 10.22 (Khớp giá trị và gradient tại $\theta_{\mathrm{old}}$)
**Giả thiết.** (G1)–(G4) tại $\theta_{\mathrm{old}}$; tập hành động hữu hạn; $\pi_{\mathrm{old}}(a\mid s)>0$ với mọi $s,a$, như với chính sách softmax; các giả thiết của Hệ quả 09.24.

**Kết luận.** $\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}})=J(\theta_{\mathrm{old}})$ và $\nabla_\theta\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}})=\nabla_\theta J(\theta_{\mathrm{old}})$.

**Điều kiện áp dụng.** $\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ là các đại lượng chính xác của $\pi_{\mathrm{old}}$.

**Phạm vi.** Khớp đến bậc một tại một điểm; mệnh đề không cho cận sai số với bước hữu hạn.
:::

::: proof
**Bước 1 (giá trị).** Tại $\theta=\theta_{\mathrm{old}}$, $A_{\mathrm{old}}(s,\pi_{\mathrm{old}})=\sum_a\pi_{\mathrm{old}}(a\mid s)A_{\mathrm{old}}(s,a)=0$ theo Mệnh đề 10.5(a), nên tổng trong Định nghĩa 10.21 bằng $0$.

**Bước 2 (gradient).** Trong dạng tổng của Định nghĩa 10.21, $\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ không phụ thuộc $\theta$, và các tổng theo $s$, $a$ hữu hạn, nên
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

Kiểm trên chuỗi hai trạng thái: với $\pi'$ của Ví dụ 10.11, dạng tỉ số tại $s_A$ cho $0{,}5\cdot\tfrac{0{,}6}{0{,}5}\cdot0{,}4+0{,}5\cdot\tfrac{0{,}4}{0{,}5}\cdot(-0{,}4)=0{,}08$, và $\mathcal L-J=\tfrac1{0{,}1}(0{,}1\cdot0{,}08+0{,}045\cdot0{,}4)=0{,}26=\Delta\mathcal L$. Gradient của $\mathcal L$ theo $(\theta_A;\,\theta_B)$ tại $\theta_{\mathrm{old}}$ là $\tfrac1{0{,}1}\bigl(0{,}1\cdot0{,}2;\,0{,}045\cdot\tfrac23\bigr)=(0{,}2;\,0{,}3)$, bằng gradient tính trực tiếp của Ví dụ 10.6.

Hai giả thiết của mệnh đề có vai trò riêng.

- Bỏ "$\pi_{\mathrm{old}}(a\mid s)>0$": nếu $\pi_{\mathrm{old}}$ chọn chắc chắn hành động 1 tại $s_B$, dữ liệu không có hành động 2, và dạng tỉ số bỏ mất số hạng $\pi_\theta(2\mid s_B)A_{\mathrm{old}}(s_B,2)$; Bước 2 cũng cần $\pi_\theta>0$ để viết $\nabla_\theta\pi_\theta=\pi_\theta\psi_\theta$.
- Bỏ "$\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ chính xác": với lợi thế ước lượng, Bước 1 và Bước 2 mất căn cứ. Trên chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$ và $\lambda=0$, kỳ vọng của lợi thế ước lượng là $(-0{,}5;\,-0{,}4)$ tại $s_A$ và $(2;\,-1)$ tại $s_B$, nên $\sum_a\pi_{\mathrm{old}}(a\mid s)\widehat A(s,a)$ bằng $-0{,}45$ và $1$. Tổng theo $\eta_\pi$ là $1\cdot(-0{,}45)+0{,}45\cdot1=0$, nên giá trị vẫn khớp, nhưng gradient lệch: $\nabla\widehat{\mathcal L}=\bigl(1\cdot\tfrac14(-0{,}5+0{,}4);\,0{,}45\cdot\tfrac29\cdot3\bigr)=(-0{,}025;\,0{,}3)\ne\nabla J=(0{,}2;\,0{,}3)$.

**Trong thực hành.** Mục tiêu mẫu $\widehat{\mathcal L}$ dùng $\widehat A_t$ của Thuật toán 10.16 và $\rho_t(\theta)=\exp\bigl(\log\pi_\theta(A_t\mid S_t)-\log\pi_{\mathrm{old}}(A_t\mid S_t)\bigr)$, tính từ log-xác suất đã lưu khi thu. Một lần thu cho giá trị của $\widehat{\mathcal L}$ tại mọi $\theta$, nên dùng được cho nhiều bước tối ưu.

<!-- note-topic-id: lec-10-topic-25 -->
### 4.3 Sai số dự báo theo độ dài bước

Với $\tilde\pi=(0{,}9;\,0{,}5)$, hàm thay thế dự báo $J$ tăng $0{,}095$, còn $J$ thật giảm $0{,}085$, dù lợi thế chính xác. Bảng sau tách hai số theo trạng thái.

| Trạng thái | $A_\pi(s,\tilde\pi)$ | dự báo $\eta_\pi(s)A_\pi(s,\tilde\pi)$ | thực tế $\eta_{\tilde\pi}(s)A_\pi(s,\tilde\pi)$ |
|---|---|---|---|
| $s_A$ | $0{,}32$ | $1\cdot0{,}32=0{,}32$ | $1\cdot0{,}32=0{,}32$ |
| $s_B$ | $-0{,}5$ | $0{,}45\cdot(-0{,}5)=-0{,}225$ | $0{,}81\cdot(-0{,}5)=-0{,}405$ |
| tổng | | $\Delta\mathcal L=0{,}095$ | $\Delta J=-0{,}085$ |

Hai cột chỉ khác ở $s_B$: số lần thăm tăng từ $0{,}45$ lên $0{,}81$, và $A_\pi(s_B,\tilde\pi)=-0{,}5<0$. Với mọi $\pi'$, trừ $\Delta\mathcal L$ khỏi $\Delta J$ của Bổ đề 10.19 cho sai số
$$\begin{aligned}&\Delta J-\Delta\mathcal L\\&\quad=\sum_{s\in\mathcal S}\bigl(\eta_{\pi'}(s)-\eta_\pi(s)\bigr)\,A_\pi(s,\pi').\end{aligned}$$
Mỗi số hạng là mức thay đổi của số lần thăm tại $s$ nhân với mức tăng lợi tức kỳ vọng của mỗi lần thăm. Với $\tilde\pi$, sai số là $(0{,}81-0{,}45)\cdot(-0{,}5)=-0{,}18$; với $\pi'$, là $(0{,}54-0{,}45)\cdot0{,}4=0{,}036$. Ví dụ sau đo sai số theo độ dài bước.

::: example Ví dụ 10.12 (Độ dài bước trên đoạn thẳng từ $\pi$ tới $\tilde\pi$)
**Dữ kiện.** Chuỗi hai trạng thái, $\gamma=0{,}9$, $J=2{,}7p_Ap_B+1-p_A$. Chính sách cũ $\pi=(\tfrac12;\,\tfrac23)$ với $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$, $\eta_\pi=(1;\,0{,}45)$. Ứng viên $\tilde\pi=(0{,}9;\,0{,}5)$.

**Hai mức thay đổi với mọi chính sách mới.** Đặt $\Delta p_A=p'_A-\tfrac12$ và $\Delta p_B=p'_B-\tfrac23$. Với hai hành động, $A_\pi(s_A,\pi')=0{,}4p'_A-0{,}4(1-p'_A)=0{,}8\,\Delta p_A$ và $A_\pi(s_B,\pi')=p'_B-2(1-p'_B)=3\,\Delta p_B$, nên
$$\begin{aligned}\Delta\mathcal L&=0{,}8\,\Delta p_A+0{,}45\cdot3\,\Delta p_B\\&=0{,}8\,\Delta p_A+1{,}35\,\Delta p_B.\end{aligned}$$
Khai triển $J=2{,}7p_Ap_B+1-p_A$ quanh $(\tfrac12;\,\tfrac23)$ cho
$$\begin{aligned}\Delta J&=0{,}8\,\Delta p_A+1{,}35\,\Delta p_B\\&\quad+2{,}7\,\Delta p_A\,\Delta p_B.\end{aligned}$$
Hàm thay thế là đúng phần bậc nhất của $\Delta J$. Phần còn lại, $2{,}7\,\Delta p_A\Delta p_B=\gamma\,\Delta p_A\,A_\pi(s_B,\pi')$, là sai số ở trên, vì $\eta_{\pi'}(s_B)-\eta_\pi(s_B)=\gamma\,\Delta p_A$.

**Đoạn thẳng.** Các chính sách $p'_A=\tfrac12+0{,}4t$, $p'_B=\tfrac23-\tfrac t6$ với $t\in[0,1]$ đi từ $\pi$ ($t=0$) tới $\tilde\pi$ ($t=1$) trong tọa độ xác suất. Thế $\Delta p_A=0{,}4t$ và $\Delta p_B=-\tfrac t6$:

- dự báo: $\Delta\mathcal L=0{,}8\cdot0{,}4t-1{,}35\cdot\tfrac t6=0{,}32t-0{,}225t=0{,}095t$;
- phần bậc hai: $2{,}7\cdot0{,}4t\cdot\bigl(-\tfrac t6\bigr)=-0{,}18t^2$;
- thực tế: $\Delta J=0{,}095t-0{,}18t^2$.

**Bảng theo độ dài bước.**

| $t$ | chính sách $(p'_A;\,p'_B)$ | dự báo $\Delta\mathcal L$ | thực tế $\Delta J$ | sai số $\lvert\Delta J-\Delta\mathcal L\rvert=0{,}18t^2$ |
|---|---|---|---|---|
| $0$ | $(0{,}5;\,\tfrac23)$ | $0$ | $0$ | $0$ |
| $0{,}25$ | $(0{,}6;\,0{,}625)$ | $0{,}02375$ | $0{,}0125$ | $0{,}01125$ |
| $0{,}5$ | $(0{,}7;\,\tfrac7{12})$ | $0{,}0475$ | $0{,}0025$ | $0{,}045$ |
| $1$ | $(0{,}9;\,0{,}5)$ | $0{,}095$ | $-0{,}085$ | $0{,}18$ |

Chính sách tại $t=0{,}25$ có tham số $\theta=(\log1{,}5;\,\log\tfrac53)$.

**Diễn giải.** Dự báo tăng theo $t$, sai số tăng theo $t^2$: nhân đôi độ dài bước thì sai số tăng bốn lần. $\Delta J$ lớn nhất, khoảng $0{,}0125$, tại $t=\tfrac{0{,}095}{0{,}36}\approx0{,}26$, và bằng $0$ tại $t=\tfrac{19}{36}\approx0{,}53$.

**Kiểm tra lại.** Tại $(0{,}6;\,0{,}625)$: $J=2{,}7\cdot0{,}375+0{,}4=1{,}4125$. Tại $(0{,}7;\,\tfrac7{12})$: $J=2{,}7\cdot0{,}7\cdot\tfrac7{12}+0{,}3=1{,}4025$. Tại $\tilde\pi$: $J=1{,}315$. Ba hiệu với $1{,}4$ là $0{,}0125$, $0{,}0025$, $-0{,}085$, khớp cột $\Delta J$.
:::

Hàm thay thế là một mô hình cục bộ của $J$: khớp đến bậc một tại chính sách cũ (Mệnh đề 10.22), trên đoạn thẳng của Ví dụ 10.12, sai số bằng $0{,}18t^2$. Để giữ chính sách mới gần chính sách cũ, chúng ta cần một thước đo khoảng cách giữa hai chính sách.

<!-- note-topic-id: lec-10-topic-12 -->
### 4.4 Đo thay đổi chính sách

Thuật toán cập nhật tham số $\theta$, nhưng cùng một thay đổi tham số có thể gây những thay đổi hành vi rất khác nhau.

::: example Ví dụ 10.13 (Cùng một bước tham số, hai mức thay đổi chính sách)
**Dữ kiện.** Một trạng thái, hai hành động; chính sách chọn hành động 1 với xác suất $p=\sigma(\theta)$, $\theta\in\mathbb R$. Bước cập nhật tăng $\theta$ thêm $1$, từ hai điểm xuất phát: $\theta=0$ và $\theta=5$.

**Tại $\theta=0$.** $p=\sigma(0)=0{,}5$, $p'=\sigma(1)=0{,}7311$, nên $\Delta p=0{,}2311$.

**Tại $\theta=5$.** $p=\sigma(5)=0{,}99331$, $p'=\sigma(6)=0{,}99753$, nên $\Delta p=0{,}0042$.

**Diễn giải.** Cùng bước $\Delta\theta=1$ đổi xác suất ở điểm thứ nhất gấp khoảng $55$ lần ở điểm thứ hai, vì hàm sigmoid dốc nhất tại $0$. Ràng buộc trên $\lVert\theta-\theta_{\mathrm{old}}\rVert_2$ vì vậy không đo mức thay đổi hành vi.

**Kiểm tra lại.** $\sigma(1)=1/(1+e^{-1})=0{,}7311$ và $0{,}2311/0{,}0042\approx55$.
:::

Về mặt ý tưởng, khác biệt giữa hai phân phối hành động đo được bằng lượng xác suất phải chuyển giữa chúng, hoặc bằng kỳ vọng của log-tỉ số hai xác suất.

::: definition Định nghĩa 10.23 (Biến phân toàn phần và phân kỳ Kullback–Leibler)
Cho hai phân phối $q$, $q'$ trên tập hành động hữu hạn $\mathcal A$. Khoảng cách *biến phân toàn phần* (total variation distance, TV) là
$$\begin{aligned}&D_{\mathrm{TV}}(q,q')\\&\quad=\tfrac12\sum_{a\in\mathcal A}\lvert q(a)-q'(a)\rvert .\end{aligned}$$
*Phân kỳ Kullback–Leibler* (Kullback–Leibler divergence) của $q$ đối với $q'$ là
$$\begin{aligned}&D_{\mathrm{KL}}(q\Vert q')\\&\quad=\sum_{a:\,q(a)>0}q(a)\log\frac{q(a)}{q'(a)},\end{aligned}$$
bằng $+\infty$ nếu có $a$ với $q(a)>0=q'(a)$. Với hai chính sách $\pi$, $\pi'$, viết $D_{\mathrm{TV}}(s)=D_{\mathrm{TV}}(\pi'(\cdot\mid s),\pi(\cdot\mid s))$, và $D_{\mathrm{KL}}(s)$ cho KL tại $s$, với chiều cũ‖mới hoặc mới‖cũ ghi tại chỗ dùng; KL trung bình, tức kỳ vọng của KL theo phân bố chiếm dụng của chính sách cũ, là
$$\begin{aligned}&\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\\&\quad=\mathbb E_{S\sim\nu^{\mathrm{old}}}\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid S)\\&\qquad\qquad\Vert\pi_\theta(\cdot\mid S))\bigr].\end{aligned}$$
:::

$D_{\mathrm{TV}}$ đối xứng, nằm trong $[0,1]$, và bằng hiệu lớn nhất giữa xác suất mà hai phân phối gán cho cùng một tập hành động, $\max_{\mathcal E\subseteq\mathcal A}\lvert q(\mathcal E)-q'(\mathcal E)\rvert$. Với hai hành động, $D_{\mathrm{TV}}=\lvert\Delta p\rvert$, nên hai bước của Ví dụ 10.13 có $D_{\mathrm{TV}}$ bằng $0{,}2311$ và $0{,}0042$.

$D_{\mathrm{KL}}$ không đối xứng và có thể vô hạn. Với $q=\pi_{\mathrm{old}}(\cdot\mid s)$ và $q'=\pi_\theta(\cdot\mid s)$, $D_{\mathrm{KL}}(q\Vert q')=\mathbb E_{A\sim\pi_{\mathrm{old}}(\cdot\mid s)}[-\log\rho_\theta(s,A)]$, nên KL gắn với tỉ số chính sách của Định nghĩa 10.21. Ở Ví dụ 10.13, $D_{\mathrm{KL}}(\pi\Vert\pi')=0{,}5\log\frac{0{,}5}{0{,}7311}+0{,}5\log\frac{0{,}5}{0{,}2689}=0{,}1201$ tại $\theta=0$ và $0{,}00245$ tại $\theta=5$.

Tại $s_A$ của chuỗi, ba chính sách $\pi$, $\pi'$, $\tilde\pi$ cho ba phân phối Bernoulli:

| phân phối tại $s_A$ | $D_{\mathrm{TV}}$ | $D_{\mathrm{KL}}(\pi\Vert\cdot)$ |
|---|---|---|
| $\pi$: $(0{,}5;\,0{,}5)$ | $0$ | $0$ |
| $\pi'$: $(0{,}6;\,0{,}4)$ | $0{,}1$ | $0{,}5\log\tfrac{0{,}5}{0{,}6}+0{,}5\log\tfrac{0{,}5}{0{,}4}=0{,}0204$ |
| $\tilde\pi$: $(0{,}9;\,0{,}1)$ | $0{,}4$ | $0{,}5\log\tfrac{0{,}5}{0{,}9}+0{,}5\log\tfrac{0{,}5}{0{,}1}=\log\tfrac53\approx0{,}5108$ |

Khi TV tăng bốn lần, KL tăng khoảng $25$ lần. Theo chiều ngược, $D_{\mathrm{KL}}(\tilde\pi\Vert\pi)=0{,}368\ne0{,}5108$.

Tại $s_B$, với $\pi(\cdot\mid s_B)=(\tfrac23;\,\tfrac13)$ và $\pi'(\cdot\mid s_B)=(0{,}8;\,0{,}2)$: $D_{\mathrm{TV}}=\tfrac2{15}\approx0{,}1333$, $D_{\mathrm{KL}}(\pi\Vert\pi')=0{,}04873$ và $D_{\mathrm{KL}}(\pi'\Vert\pi)=0{,}04369$. Khi $\tilde p_A\to1$, chính sách mới gần như bỏ hành động 2 tại $s_A$: $D_{\mathrm{KL}}(\pi\Vert\tilde\pi)\to+\infty$, trong khi $D_{\mathrm{TV}}\to0{,}5$.

Trên chuỗi, $\nu^{\mathrm{old}}=(0{,}1;\,0{,}045)$, nên $\bar D_{\mathrm{KL}}=0{,}1\,D_{\mathrm{KL}}(s_A)+0{,}045\,D_{\mathrm{KL}}(s_B)$, KL theo chiều cũ‖mới:

- Với $\pi'$: $D_{\mathrm{KL}}(s)=(0{,}02041;\,0{,}04873)$, nên $\bar D_{\mathrm{KL}}=0{,}002041+0{,}002193=0{,}004234$.
- Với $\tilde\pi$: $D_{\mathrm{KL}}(s_B)=\tfrac23\log\tfrac43+\tfrac13\log\tfrac23\approx0{,}0566$, nên $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}5108+0{,}045\cdot0{,}0566\approx0{,}0536$.

<!-- note-topic-id: lec-10-topic-14 -->
### 4.5 Bài toán miền tin cậy

Về mặt ý tưởng, chúng ta cực đại hóa dự báo của hàm thay thế trong tập các chính sách có KL trung bình so với chính sách cũ không vượt một bán kính $\kappa$.

::: definition Định nghĩa 10.24 (Bài toán miền tin cậy)
Cho chính sách cũ $\pi_{\mathrm{old}}$ thỏa $\pi_{\mathrm{old}}(a\mid s)>0$ với mọi $s,a$, lớp chính sách tham số hóa $\{\pi_\theta\}$ chứa $\pi_{\mathrm{old}}$, và bán kính $\kappa>0$. *Bài toán miền tin cậy* (trust region problem) là
$$\begin{aligned}&\max_\theta\\&\mathbb E_{\substack{S\sim\nu^{\mathrm{old}}\\A\sim\pi_{\mathrm{old}}(\cdot\mid S)}}\bigl[\rho_\theta(S,A)\\&\quad\times A_{\mathrm{old}}(S,A)\bigr]\\&\text{với ràng buộc}\\&\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\le\kappa .\end{aligned}$$
Tập $\{\theta:\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\le\kappa\}$ gọi là *miền tin cậy*.
:::

Hàm mục tiêu chọn hành vi mới có dự báo tốt nhất; ràng buộc giữ chính sách mới gần chính sách đã sinh dữ liệu. Vì $\pi_{\mathrm{old}}>0$, điều kiện hỗ trợ luôn thỏa, nên theo dạng tỉ số của Định nghĩa 10.21, hàm mục tiêu là $(1-\gamma)\bigl(\mathcal L_{\theta_{\mathrm{old}}}(\theta)-J(\theta_{\mathrm{old}})\bigr)$. Dạng (14) của Schulman và cộng sự (2015), bỏ thừa số $1/(1-\gamma)$ và thay $A$ bằng $Q$, có cùng nghiệm khi bán kính được quy đổi theo khối $\nu^\pi(\mathcal S)$.

Trên đoạn thẳng của Ví dụ 10.12, với $\kappa=0{,}01$, KL trung bình bằng $0{,}0022$ tại $t=0{,}25$, $0{,}0094$ tại $t=0{,}5$ và $0{,}0536$ tại $t=1$. Miền tin cậy chứa các điểm $t\le0{,}515$: tại $t=0{,}515$, $\bar D_{\mathrm{KL}}=0{,}01$, $\Delta\mathcal L\approx0{,}049$ và $\Delta J\approx0{,}0012>0$. Trên đoạn này, $\Delta\mathcal L=0{,}095t$ tăng theo $t$, nên trong các chính sách trên đoạn, điểm tốt nhất là biên $t=0{,}515$; ứng viên $\tilde\pi$ nằm ngoài miền.

Khi $A_\pi$, $\nu^\pi$ chính xác, cùng $P$, $\mu_0$ và $\gamma<1$, giới hạn KL kiểm soát sai số qua ba mắt xích:

1. KL trung bình nhỏ thì TV kỳ vọng theo $\nu^\pi$ nhỏ: tại mỗi trạng thái, $D_{\mathrm{TV}}(s)\le\sqrt{D_{\mathrm{KL}}(s)/2}$, với KL theo chiều nào cũng được (bất đẳng thức Pinsker, Mệnh đề 10.25(b)), rồi lấy kỳ vọng và dùng bất đẳng thức Jensen;
2. TV kỳ vọng theo $\nu^\pi$ nhỏ thì phân bố chiếm dụng ít thay đổi (Bổ đề 10.26);
3. phân bố chiếm dụng ít thay đổi thì sai số trong đẳng thức của Mục 4.3 nhỏ (Định lý 10.27).

Ghép ba mắt xích được cận (Hệ quả 10.28)
$$\Delta J\ge\Delta\mathcal L-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\tfrac12\bar D_{\mathrm{KL}}},$$
với $\chi_{\pi'}=\max_s\lvert A_\pi(s,\pi')\rvert$ và $\bar D_{\mathrm{KL}}=\mathbb E_{S\sim\nu^\pi}[D_{\mathrm{KL}}(S)]$. Cận chứng nhận cải thiện chỉ khi mức tăng dự báo lớn hơn phạt. TRPO thực hành ràng buộc KL trên mẫu và giải gần đúng, nên thỏa ràng buộc chưa đủ để $J$ tăng.

KL trung bình $\bar D_{\mathrm{KL}}$ lấy trọng số $\nu^\pi$, với tổng bằng khối $\nu^\pi(\mathcal S)=0{,}145$, không bằng $1$. Trên bộ đệm, KL trung bình là trung bình đều $\widehat D=\widehat{\mathbb E}_{\mathcal D}[D_{\mathrm{KL}}(S_t)]$ trên các trạng thái đã thu. Với $\tilde\pi$, $D_{\mathrm{KL}}(s)=(0{,}511;\,0{,}0566)$, và ba cách lấy trọng số cho ba giá trị:

- trọng số $\nu^\pi=(0{,}1;\,0{,}045)$: $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}511+0{,}045\cdot0{,}0566=0{,}0536$;
- trọng số $\nu^\pi$ chuẩn hóa, $(0{,}1;\,0{,}045)/0{,}145=(0{,}690;\,0{,}310)$: $0{,}690\cdot0{,}511+0{,}310\cdot0{,}0566\approx0{,}37$;
- tần suất mẫu: mỗi lượt của $\pi$ thăm $s_A$ một lần và thăm $s_B$ với xác suất $p_A=0{,}5$, nên tần suất là $(\tfrac23;\,\tfrac13)$ và $\widehat D=\tfrac23\cdot0{,}511+\tfrac13\cdot0{,}0566\approx0{,}36$.

Chuẩn hóa chia $\bar D_{\mathrm{KL}}$ cho khối; đó là phép quy đổi bán kính theo khối $\nu^\pi(\mathcal S)$ của dạng (14) ở trên. Bộ đệm không có trọng số chiết khấu, nên tần suất mẫu còn khác $\nu^\pi$ chuẩn hóa: $s_B$ chỉ được thăm ở bước $1$, nên trong $\nu^\pi$ nó mang thêm thừa số $\gamma=0{,}9$, và tỉ lệ $\nu^\pi(s_B)/\nu^\pi(s_A)$ bằng $0{,}45$, còn tỉ lệ số lần thăm trên bộ đệm bằng $0{,}5$. TRPO thực hành áp bán kính $\kappa$ lên $\widehat D$, nên cùng một số $\kappa$ ứng với hai miền khác nhau: trên đoạn thẳng của Ví dụ 10.12, $\bar D_{\mathrm{KL}}\le0{,}01$ chứa các điểm $t\le0{,}515$, còn $\widehat D\le0{,}01$ với tần suất $(\tfrac23;\,\tfrac13)$ chỉ chứa các điểm $t\le0{,}206$.

<!-- note-topic-id: lec-10-topic-13 -->
### 4.6 Cơ sở lý thuyết

::: proposition Mệnh đề 10.25 (Hai tính chất của KL)
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

Kết luận (a) cho phép dùng KL như một độ đo khác biệt: nó bằng $0$ đúng khi hai chính sách trùng nhau tại trạng thái đó. Kết luận (b) chuyển một ràng buộc trên KL thành ràng buộc trên TV. Với $\pi'$, tại $s_B$, $\tfrac2{15}=0{,}1333\le\sqrt{0{,}04873/2}=0{,}1561$; tại $s_A$, $0{,}1\le\sqrt{0{,}02041/2}=0{,}1010$. Với bước dài $\tilde\pi$, tại $s_A$, $0{,}4\le\sqrt{0{,}511/2}\approx0{,}505$; tại $s_B$, $\tfrac16\approx0{,}1667\le\sqrt{0{,}0566/2}\approx0{,}1683$.

Một cách trực quan, nếu tại mọi trạng thái $\pi'$ chọn hành động gần như $\pi$, thì hai chính sách thăm các trạng thái với tần suất gần nhau; khác biệt nhỏ ở mỗi bước tích lũy dọc lượt, nên sai lệch giữa hai phân bố chiếm dụng có thêm thừa số $\gamma/(1-\gamma)$. Bổ đề sau chặn sai lệch đó bằng TV trung bình theo $\nu^\pi$.

::: lemma Bổ đề 10.26 (Dịch chuyển phân bố chiếm dụng)
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

Sự kết thúc được dùng ở hai chỗ, Bước 1 và Bước 5, và cả hai chỉ làm các tổng nhỏ đi: xác suất đi tới trạng thái kết thúc không còn nằm trong $P_\pi$. Trên Ví dụ 10.11, $D_{\mathrm{TV}}(s_A)=0{,}1$, $D_{\mathrm{TV}}(s_B)=\tfrac2{15}$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}1\cdot0{,}1+0{,}045\cdot\tfrac2{15}=0{,}016$; vế trái là $\lvert0{,}1-0{,}1\rvert+\lvert0{,}054-0{,}045\rvert=0{,}009$, vế phải là $18\cdot0{,}016=0{,}288$.

Ghép Bổ đề 10.19, hàm thay thế và Bổ đề 10.26 cho cận dưới của mức cải thiện, gọi là *chặn cải thiện* (còn gọi là cận cải thiện; policy improvement bound).

::: theorem Định lý 10.27 (Chặn cải thiện)
**Giả thiết.** Như Bổ đề 10.19: MDP hữu hạn, cùng $P$ và $\mu_0$, $\lvert R_{t+1}\rvert\le R_{\max}$, $0\le\gamma<1$, $\pi$ và $\pi'$ Markov dừng.

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

**Bước 3 (hàm thay thế).** Theo dạng tổng của Định nghĩa 10.21, với $\pi_{\mathrm{old}}=\pi$ và $\pi_\theta=\pi'$, $\frac1{1-\gamma}\langle\nu,\bar a\rangle=\mathcal L_\pi(\pi')-J(\pi)$.

**Bước 4 (bất đẳng thức Hölder).** $\langle\nu'-\nu,\bar a\rangle\ge-\sum_s\lvert\nu'(s)-\nu(s)\rvert\,\lvert\bar a(s)\rvert\ge-\lVert\nu'-\nu\rVert_1\,\chi_{\pi'}$.

**Bước 5 (Bổ đề 10.26).** Ghép các bước:
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
Đẳng thức ghép Bước 1–3, bất đẳng thức thứ nhất là Bước 4, bất đẳng thức thứ hai là Bổ đề 10.26. $\square$
:::

Định lý nói rằng mức cải thiện thật không nhỏ hơn mức cải thiện dự báo trừ một phạt tỉ lệ với kỳ vọng theo $\nu^\pi$ của khoảng cách TV giữa hai chính sách. Khi $\pi'$ gần $\pi$, phạt nhỏ; khi $\pi'$ xa, phạt có thể lớn hơn mọi mức tăng dự báo. Các giả thiết có vai trò riêng.

- Bỏ "$\gamma<1$": trên hành lang ngắn, $\gamma=1$ làm thừa số $2\gamma/(1-\gamma)^2$ vô hạn và $\nu$ không xác định; định lý không áp dụng.
- Bỏ "lợi thế và phân bố chính xác": nếu $\mathcal L$ được thay bằng một ước lượng mẫu, vế phải có thêm sai số ước lượng mà định lý không kiểm soát, nên cận không còn chứng nhận được cải thiện.

Định lý không cần điều kiện hỗ trợ $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$, vì Bước 3 dùng dạng tổng của hàm thay thế. Điều kiện đó chỉ cần cho dạng tỉ số, dạng ước lượng được từ dữ liệu, như phản ví dụ thứ nhất sau Mệnh đề 10.22.

Bước 1 dùng các giả thiết của Bổ đề 10.19; Bước 5 dùng $\gamma<1$ và sự kết thúc qua Bổ đề 10.26. Achiam và cộng sự (2017, Hệ quả 1, (5)) phát biểu cùng cận.

**Trong thực hành.** Không đại lượng nào của cận tính được từ một bộ đệm: $\chi_{\pi'}$ cần lợi thế chính xác tại mọi trạng thái, còn bộ đệm chỉ cho trung bình đều thay cho kỳ vọng theo $\nu^\pi$. Với $\gamma=0{,}99$, thừa số $2\gamma/(1-\gamma)^2$ bằng $19\,800$. Cận chỉ cho biết đại lượng cần kiểm soát: khoảng cách giữa hai chính sách theo phân bố trạng thái của chính sách cũ.

::: example Ví dụ 10.14 (Chặn cải thiện trên chuỗi hai trạng thái)
**Dữ kiện.** Chuỗi hai trạng thái, $\gamma=0{,}9$, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$, $\nu^\pi=(0{,}1;\,0{,}045)$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$. Bước của Ví dụ 10.11: $p'_A=0{,}6$, $p'_B=0{,}8$, $\Delta J=0{,}296$, $\mathcal L-J=0{,}26$, $A_\pi(s,\pi')=(0{,}08;\,0{,}4)$, $D_{\mathrm{TV}}=(0{,}1;\,\tfrac2{15})$. Bước dài $\tilde\pi$ của Ví dụ 10.11: $\tilde p_A=0{,}9$, $\tilde p_B=0{,}5$, $\Delta J=-0{,}085$, $\mathcal L-J=0{,}095$, $A_\pi(s,\tilde\pi)=(0{,}32;\,-0{,}5)$, $D_{\mathrm{TV}}=(0{,}4;\,\tfrac16)$.

**Bước của Ví dụ 10.11.** $\chi_{\pi'}=0{,}4$ và $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}016$, nên phạt là $\frac{2\cdot0{,}9\cdot0{,}4}{0{,}01}\cdot0{,}016=1{,}152$, lớn hơn $0{,}26$; cận dưới là $0{,}26-1{,}152=-0{,}892$, không chứng nhận được cải thiện dù $\Delta J=0{,}296>0$.

**Bước dài $\tilde\pi$.** Hằng của định lý và phạt:

- $\chi_{\tilde\pi}=\max(0{,}32;\,0{,}5)=0{,}5$, nên $\dfrac{2\gamma\chi_{\tilde\pi}}{(1-\gamma)^2}=\dfrac{2\cdot0{,}9\cdot0{,}5}{0{,}01}=90$;
- $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}1\cdot0{,}4+0{,}045\cdot\tfrac16=0{,}04+0{,}0075=0{,}0475$;
- phạt $90\cdot0{,}0475=4{,}275$ và cận dưới $0{,}095-4{,}275=-4{,}18$.

Cận đúng, vì $-4{,}18\le\Delta J=-0{,}085$, nhưng rất lỏng: phạt lớn gấp $45$ lần mức tăng $0{,}095$ mà hàm thay thế báo.

**Bước nhỏ chỉ đổi $s_B$.** Lấy $p'_A=\tfrac12$, $p'_B=\tfrac23+\Delta p$ với bước $\Delta p>0$. Khi đó $\Delta J=0{,}5\cdot0{,}9\cdot3\Delta p=1{,}35\Delta p$. Vì $p_A$ không đổi, $\nu(s_B)$ không đổi, nên hàm thay thế chính xác: $A_\pi(s_A,\pi')=0$, $A_\pi(s_B,\pi')=(\tfrac23+\Delta p)\cdot1+(\tfrac13-\Delta p)(-2)=3\Delta p$, và $\mathcal L-J=\tfrac1{0{,}1}\cdot0{,}045\cdot3\Delta p=1{,}35\Delta p$. Cận vẫn phạt: $\chi_{\pi'}=3\Delta p$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}045\Delta p$, phạt $\frac{2\cdot0{,}9\cdot3\Delta p}{0{,}01}\cdot0{,}045\Delta p=24{,}3(\Delta p)^2$. Cận dương khi và chỉ khi $1{,}35\Delta p>24{,}3(\Delta p)^2$, tức $\Delta p<1{,}35/24{,}3\approx0{,}0556$.

**Diễn giải.** Cận chỉ chứng nhận được các bước $\Delta p<0{,}0556$, kể cả khi hàm thay thế chính xác: phạt của Định lý 10.27 không dùng thông tin rằng $\nu(s_B)$ không đổi, vì cận phải đúng cho mọi MDP và mọi $\pi'$.

**Kiểm tra lại.** $\Delta p=0{,}05$: $0{,}0675-0{,}06075=0{,}00675>0$; $\Delta p=0{,}06$: $0{,}081-0{,}08748=-0{,}00648<0$.
:::

Hệ quả sau đổi phạt sang KL trung bình bằng bất đẳng thức Pinsker.

::: corollary Hệ quả 10.28 (Chặn cải thiện dạng KL trung bình)
**Giả thiết.** Như Định lý 10.27.

**Kết luận.** Với $\bar D_{\mathrm{KL}}=\mathbb E_{S\sim\nu^\pi}[D_{\mathrm{KL}}(S)]$, lấy theo một trong hai chiều $D_{\mathrm{KL}}(\pi\Vert\pi')$ hoặc $D_{\mathrm{KL}}(\pi'\Vert\pi)$ tại mỗi trạng thái,
$$\begin{aligned}&J(\pi')-J(\pi)\\&\quad\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]\\&\qquad-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\tfrac12\,\bar D_{\mathrm{KL}}}.\end{aligned}$$

**Điều kiện áp dụng.** Như Định lý 10.27: $A_\pi$ và $\nu^\pi$ là các đại lượng chính xác của $\pi$.

**Phạm vi.** Cận yếu hơn Định lý 10.27, vì Bước 1 và Bước 2 của chứng minh đều là bất đẳng thức; đổi lại, phạt viết theo KL, đại lượng mà các phương pháp miền tin cậy ràng buộc.
:::

::: proof
**Bước 1 (Pinsker theo trạng thái).** Mệnh đề 10.25(b) cho $D_{\mathrm{TV}}(s)\le\sqrt{D_{\mathrm{KL}}(s)/2}$ với mỗi $s$ và với cả hai chiều KL.

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

**Bước 3 (ghép).** Bước 1 và Bước 2 cho $\mathbb E_\nu[D_{\mathrm{TV}}]\le\sum_s\nu^\pi(s)\sqrt{x_s}\le\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$. Thay vào Định lý 10.27, với hệ số của phạt không âm, được kết luận. $\square$
:::

Achiam và cộng sự (2017, Hệ quả 3) phát biểu cùng kết quả với chiều $D_{\mathrm{KL}}(\pi'\Vert\pi)$; Bước 1 cho phép dùng cả chiều $D_{\mathrm{KL}}(\pi\Vert\pi')$ mà TRPO ràng buộc.

Trên bước $\pi'$ của Ví dụ 10.14, KL theo chiều cũ‖mới là $(0{,}02041;\,0{,}04873)$, $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}02041+0{,}045\cdot0{,}04873=0{,}004234$, và phạt là $72\sqrt{0{,}002117}=3{,}31$; theo chiều mới‖cũ, $\bar D_{\mathrm{KL}}=0{,}003980$ và phạt là $3{,}21$. Cả hai lớn hơn phạt dạng TV $1{,}152$. Với bước dài $\tilde\pi$ của Ví dụ 10.14, KL theo chiều cũ‖mới là $(0{,}511;\,0{,}0566)$, $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}511+0{,}045\cdot0{,}0566\approx0{,}0536$, phạt là $90\sqrt{0{,}0536/2}\approx14{,}7$ và cận là $0{,}095-14{,}7\approx-14{,}6$, lỏng hơn cận $-4{,}18$ dạng TV.

::: remark Nhận xét 10.29 (Định lý 1 của Schulman và cộng sự, 2015)
Schulman và cộng sự (2015, Định lý 1) chứng minh một cận cùng loại với khoảng cách TV lớn nhất theo trạng thái, $D^{\max}_{\mathrm{TV}}=\max_sD_{\mathrm{TV}}(s)$:
$$\begin{aligned}J(\pi^\prime)&\ge\mathcal L_\pi(\pi^\prime)\\&\quad-\frac{4\bar\chi\gamma}{(1-\gamma)^2}\bigl(D^{\max}_{\mathrm{TV}}\bigr)^2 .\end{aligned}$$
Chứng minh nằm ngoài phạm vi học phần; bài báo chứng minh bằng ghép cặp (coupling) hai chính sách (Phụ lục A) hoặc bằng lý thuyết nhiễu loạn (Phụ lục B). Trên Ví dụ 10.14, $\bar\chi=2$: bước của Ví dụ 10.11 có $D^{\max}_{\mathrm{TV}}=\tfrac2{15}$ và phạt $\frac{4\cdot2\cdot0{,}9}{0{,}01}\cdot\bigl(\tfrac2{15}\bigr)^2=12{,}8$; bước nhỏ có phạt $720(\Delta p)^2$, dương khi $\Delta p<0{,}001875$. Trên ví dụ này, cận dạng lớn nhất lỏng hơn cận dạng kỳ vọng của Định lý 10.27.
:::

Định lý 10.27 cho một hàm của $\pi'$ nằm dưới $J(\pi')$ ở mọi nơi. Về mặt ý tưởng, nếu hàm đó còn chạm $J$ tại chính sách hiện tại, thì mọi bước làm hàm đó tăng cũng làm $J$ tăng.

::: corollary Hệ quả 10.30 (Cải thiện đơn điệu qua hàm chặn dưới)
**Giả thiết.** Như Định lý 10.27 cho mỗi cặp $(\pi_k,\pi)$, với $\pi$ chạy trong một lớp chính sách chứa $\pi_k$. Đặt $\bar\chi_k=\max_{s,a}\lvert A_{\pi_k}(s,a)\rvert$, $C_k=\frac{2\gamma\bar\chi_k}{(1-\gamma)^2}$ và
$$\begin{aligned}&\mathcal M_k(\pi)=\mathcal L_{\pi_k}(\pi)\\&\quad-C_k\,\mathbb E_{S\sim\nu^{\pi_k}}\bigl[D_{\mathrm{TV}}(\pi(\cdot\mid S),\\&\qquad\qquad\pi_k(\cdot\mid S))\bigr].\end{aligned}$$

**Kết luận.** Nếu $\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)$, đặc biệt nếu $\pi_{k+1}$ cực đại hóa $\mathcal M_k$ trên lớp chính sách, thì $J(\pi_{k+1})\ge J(\pi_k)$.

**Điều kiện áp dụng.** $A_{\pi_k}$ và $\nu^{\pi_k}$ tính chính xác; phép cực đại hóa, hoặc ít nhất điều kiện không giảm của $\mathcal M_k$, được kiểm chính xác.

**Phạm vi.** Bảo đảm $J$ không giảm qua các vòng lặp; không bảo đảm hội tụ tới chính sách tối ưu, và không áp dụng khi các đại lượng trên được ước lượng.
:::

::: proof
**Bước 1 ($\mathcal M_k$ nằm dưới $J$).** Với mọi $\pi$ trong lớp, $\chi_\pi\le\bar\chi_k$, nên Định lý 10.27 cho $J(\pi)\ge\mathcal M_k(\pi)$.

**Bước 2 (chạm tại $\pi_k$).** $\mathcal L_{\pi_k}(\pi_k)=J(\pi_k)$ vì $A_{\pi_k}(s,\pi_k)=0$ (Mệnh đề 10.5(a)), và phạt bằng $0$ vì $D_{\mathrm{TV}}(s)=0$ tại mọi $s$; do đó $\mathcal M_k(\pi_k)=J(\pi_k)$.

**Bước 3 (ghép).** $J(\pi_{k+1})\ge\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)=J(\pi_k)$, theo Bước 1, giả thiết, rồi Bước 2. $\square$
:::

Schulman và cộng sự (2015, §3), theo Hunter và Lange (2004), gọi cách lặp này là một thuật toán *cực đại hóa qua hàm chặn dưới* (minorize–maximize, MM).

Trên chuỗi hai trạng thái, $\bar\chi_k=2$ nên $C_k=\frac{2\cdot0{,}9\cdot2}{0{,}01}=360$. Với hai hành động, $A_\pi(s,\pi')=(p'_s-p_s)\bigl(A_\pi(s,1)-A_\pi(s,2)\bigr)$ có trị tuyệt đối $D_{\mathrm{TV}}(s)\,a_s$ với $a_s=\lvert A_\pi(s,1)-A_\pi(s,2)\rvert$, nên
$$
\begin{aligned}
&\mathcal M_k(\pi')-\mathcal M_k(\pi_k)\\
&\quad\le\textstyle\sum_{s}\nu(s)\,D_{\mathrm{TV}}(s)\,c_s,\\
&c_s=\frac{a_s}{1-\gamma}-C_k.
\end{aligned}
$$
Hệ số $c_s$ là $8-360$ tại $s_A$ và $30-360$ tại $s_B$. Mọi bước khác $\pi_k$ đều làm $\mathcal M_k$ giảm, nên thuật toán đứng yên tại $\pi_k$, và kết luận của Hệ quả 10.30 đúng một cách tầm thường; với hệ số phạt mà lý thuyết khuyến nghị, bước cập nhật rất nhỏ (Schulman và cộng sự, 2015, §4).

Hai điều kiện của Hệ quả 10.30 có vai trò riêng.

- Bỏ "đánh giá chính xác": thay $A_{\pi_k}$ và $\nu^{\pi_k}$ bằng ước lượng thì Bước 1 không còn cho $J\ge\mathcal M_k$, vì Định lý 10.27 cần các đại lượng chính xác.
- Bỏ "$\mathcal M_k$ không giảm": hệ quả không bảo đảm gì cho một bước làm $\mathcal M_k$ giảm, như mọi bước khác $\pi_k$ trên chuỗi hai trạng thái; $J$ vẫn có thể tăng, như bước của Ví dụ 10.11 với $\Delta J=0{,}296$.

Để cho phép bước lớn, Schulman và cộng sự (2015, §4, (11)–(12)) thay phạt bằng ràng buộc KL lớn nhất theo trạng thái, rồi thay KL lớn nhất bằng KL trung bình, một xấp xỉ mà bài báo gọi là kinh nghiệm (heuristic); kết quả là bài toán của Định nghĩa 10.24. Bài toán đó không bảo đảm $J$ tăng; hệ quả sau cho biết nó bảo đảm gì.

::: corollary Hệ quả 10.31 (Mức giảm tối đa của bước miền tin cậy)
**Giả thiết.** Như Định lý 10.27 với $\pi=\pi_k$; $\pi_{k+1}$ là nghiệm chính xác của bài toán của Định nghĩa 10.24 với $\pi_{\mathrm{old}}=\pi_k$, trên một lớp chính sách chứa $\pi_k$.

**Kết luận.**
$$\begin{aligned}&J(\pi_{k+1})-J(\pi_k)\\&\quad\ge-\frac{\sqrt{2\kappa}\,\gamma\,\chi_{\pi_{k+1}}}{(1-\gamma)^2}.\end{aligned}$$

**Điều kiện áp dụng.** Kỳ vọng và KL trung bình lấy theo $\nu^{\pi_k}$ có chiết khấu, với lợi thế chính xác, và bài toán được giải chính xác.

**Phạm vi.** Cận cho mức giảm tối đa, không bảo đảm cải thiện; cận nhỏ khi $\kappa$ nhỏ.
:::

::: proof
**Bước 1 (mục tiêu tối ưu không âm).** $\pi_k$ thuộc lớp chính sách và thỏa ràng buộc vì $\bar D_{\mathrm{KL}}(\pi_k\Vert\pi_k)=0$; giá trị mục tiêu tại $\pi_k$ là $\sum_s\nu^{\pi_k}(s)A_{\pi_k}(s,\pi_k)=0$ (Mệnh đề 10.5(a)). Nghiệm tối ưu có giá trị không nhỏ hơn, nên $\mathcal L_{\pi_k}(\pi_{k+1})-J(\pi_k)\ge0$.

**Bước 2 (chặn phạt).** Ràng buộc cho $\bar D_{\mathrm{KL}}\le\kappa$ theo chiều $\pi_k\Vert\pi_{k+1}$. Hệ quả 10.28 với chiều này cho
$$\begin{aligned}&J(\pi_{k+1})-J(\pi_k)\\&\quad\ge0-\frac{2\gamma\chi_{\pi_{k+1}}}{(1-\gamma)^2}\sqrt{\tfrac\kappa2}\\&\quad=-\frac{\sqrt{2\kappa}\,\gamma\,\chi_{\pi_{k+1}}}{(1-\gamma)^2},\end{aligned}$$
vì $2\sqrt{\kappa/2}=\sqrt{2\kappa}$. $\square$
:::

Hệ quả 10.31 là Mệnh đề 1 của Achiam và cộng sự (2017, (9)), viết cho chiều KL của TRPO. Trên Ví dụ 10.14, lấy $\kappa=0{,}004234$, đúng bằng KL trung bình của bước của Ví dụ 10.11. Nghiệm chính xác của bài toán là $p_A\approx0{,}571$, $p_B\approx0{,}824$, với $\chi_{\pi_{k+1}}=\max_s\lvert A_{\pi_k}(s,\pi_{k+1})\rvert\approx\max(0{,}057;\,0{,}472)=0{,}472$, nên cận là $-\sqrt{0{,}008468}\cdot0{,}9\cdot0{,}472/0{,}01\approx-3{,}91$; mức tăng thật là $\Delta J\approx0{,}299$. Hằng $\chi$ ở đây thuộc về nghiệm, không phải $\chi_{\pi'}=0{,}4$ của bước $\pi'$.

Bỏ giả thiết "nghiệm chính xác" thì Bước 1 không còn cho $\mathcal L_{\pi_k}(\pi_{k+1})\ge J(\pi_k)$. Một nhầm lẫn thường gặp là áp hệ quả cho TRPO như được cài đặt, vốn dùng trung bình đều trên mẫu, lợi thế ước lượng, KL bậc hai và nghiệm gần đúng, nên giả thiết của hệ quả không thỏa.

**Trong thực hành.** Hệ quả 10.30 và 10.31 giải thích dạng của TRPO: cực đại hóa hàm thay thế ước lượng từ dữ liệu cũ trong một miền KL trung bình bán kính $\kappa$. Với mạng nơ-ron và dữ liệu hữu hạn, lợi thế, phân bố chiếm dụng và nghiệm chỉ có gần đúng, nên $\kappa$ là một siêu tham số.

Bài toán của Định nghĩa 10.24 cho bước lớn với mức giảm tối đa bị chặn (Hệ quả 10.31), nhưng là một bài toán tối ưu phi tuyến có ràng buộc trên $\theta$.

---

## 5. TRPO và gradient tự nhiên

Trên chuỗi hai trạng thái, ràng buộc của Định nghĩa 10.24 là $0{,}1\,D_{\mathrm{KL}}(s_A)+0{,}045\,D_{\mathrm{KL}}(s_B)\le\kappa$, một hàm phi tuyến của $(\theta_A;\,\theta_B)$; trong bài toán tổng quát, $\theta\in\mathbb R^d$ với $d$ lớn, và cả hàm mục tiêu lẫn ràng buộc chỉ ước lượng được từ mẫu, nên chúng ta cần một bài toán xấp xỉ.

<!-- note-topic-id: lec-10-topic-15 -->
### 5.1 KL bậc hai và gradient tự nhiên

Gần $\theta_{\mathrm{old}}$, Mệnh đề 10.22 cho hàm thay thế xấp xỉ bậc một $\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}}+\Delta)\approx J(\theta_{\mathrm{old}})+g^\top\Delta$, với $g=\nabla_\theta J(\theta_{\mathrm{old}})$. KL trung bình bằng $0$ và có gradient bằng $0$ tại $\theta_{\mathrm{old}}$, nên cần xấp xỉ bậc hai theo $\Delta$.

Một cách trực quan, trong mặt phẳng của bước $\Delta$, các đường đồng mức của $g^\top\Delta$ là những đường thẳng vuông góc với $g$. Trong một hình tròn Euclid tâm gốc, điểm tốt nhất nằm trên biên theo đúng hướng $g$. Ràng buộc KL bậc hai là một elip: hẹp theo hướng mà một bước nhỏ đã đổi chính sách nhiều, rộng theo hướng KL ít nhạy. Điểm tốt nhất trong elip là điểm biên chạm đường đồng mức cao nhất, nên hướng tới nó nghiêng khỏi $g$ về phía trục rộng; đó là gradient tự nhiên.

Hai KL $0{,}1201$ và $0{,}00245$ của Ví dụ 10.13 khác nhau vì độ cong của KL đổi theo điểm xuất phát. Định nghĩa sau đo độ cong đó trên mọi trạng thái.

::: definition Định nghĩa 10.32 (Ma trận thông tin Fisher)
Cho chính sách $\pi_{\theta_{\mathrm{old}}}$ trên tập hành động hữu hạn, với hàm điểm $\psi=\psi_{\theta_{\mathrm{old}}}$ và phân bố chiếm dụng $\nu^{\mathrm{old}}$. *Ma trận thông tin Fisher* (Fisher information matrix) trung bình theo $\nu^{\mathrm{old}}$ là
$$\begin{aligned}&F(\theta_{\mathrm{old}})\\&\quad=\mathbb E_{\substack{S\sim\nu^{\mathrm{old}}\\A\sim\pi_{\mathrm{old}}(\cdot\mid S)}}\bigl[\psi_{\theta_{\mathrm{old}}}(S,A)\\&\qquad\quad\times\psi_{\theta_{\mathrm{old}}}(S,A)^\top\bigr]\\&\quad\in\mathbb R^{d\times d}.\end{aligned}$$
Với một trạng thái $s$ cố định, $F_s=\mathbb E_{A\sim\pi_{\mathrm{old}}(\cdot\mid s)}[\psi\psi^\top]$ là ma trận Fisher của phân phối $\pi_{\mathrm{old}}(\cdot\mid s)$, và $F=\sum_s\nu^{\mathrm{old}}(s)F_s$.
:::

$F$ đối xứng và nửa xác định dương, vì $v^\top Fv=\mathbb E[(v^\top\psi)^2]\ge0$ với mọi $v$; nó không nhất thiết xác định dương, vì $v^\top Fv=0$ khi $v^\top\psi=0$ với mọi cặp trạng thái–hành động. Với chính sách Bernoulli logit của Ví dụ 10.13, $\psi=1-p$ với xác suất $p$ và $\psi=-p$ với xác suất $1-p$, nên $F_s=p(1-p)^2+(1-p)p^2=p(1-p)$. Ma trận $F$ đo độ nhạy của phân phối hành động theo tham số; mệnh đề sau cho thấy nó chính là Hessian của KL trung bình tại $\theta_{\mathrm{old}}$.

::: proposition Mệnh đề 10.33 (KL trung bình bậc hai)
**Giả thiết.** Tập hành động hữu hạn; $\pi_\theta(a\mid s)>0$ và khả vi liên tục hai lần theo $\theta$ với mọi $s,a$; $\nu^{\mathrm{old}}$ giữ cố định. Đặt $\bar D(\theta)=\sum_{s\in\mathcal S}\nu^{\mathrm{old}}(s)\,D_{\mathrm{KL}}\bigl(\pi_{\mathrm{old}}(\cdot\mid s)\Vert\pi_\theta(\cdot\mid s)\bigr)$.

**Kết luận.** $\bar D(\theta_{\mathrm{old}})=0$, $\nabla\bar D(\theta_{\mathrm{old}})=0$ và $\nabla^2\bar D(\theta_{\mathrm{old}})=F(\theta_{\mathrm{old}})$. Do đó
$$\begin{aligned}&\bar D(\theta_{\mathrm{old}}+\Delta)\\&\quad=\tfrac12\Delta^\top F\Delta+o(\lVert\Delta\rVert^2).\end{aligned}$$

**Điều kiện áp dụng.** Phân bố trạng thái không đổi theo $\theta$, như trong ràng buộc của Định nghĩa 10.24.

**Phạm vi.** Xấp xỉ địa phương; với bước hữu hạn, KL thật khác dạng bậc hai, như Ví dụ 10.13.
:::

::: proof
**Bước 1 (giá trị).** Tại $\theta=\theta_{\mathrm{old}}$, mỗi $D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid s)\Vert\pi_{\mathrm{old}}(\cdot\mid s))=0$ theo Mệnh đề 10.25(a).

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

Quanh chính sách cũ, miền tin cậy KL gần đúng là elip $\tfrac12\Delta^\top F\Delta\le\kappa$. Ở Ví dụ 10.13, $F=p(1-p)$ bằng $0{,}25$ tại $\theta=0$ và $0{,}00665$ tại $\theta=5$, nên xấp xỉ bậc hai $\tfrac12p(1-p)\cdot1^2$ là $0{,}125$ và $0{,}00332$, cùng bậc độ lớn với KL thật $0{,}1201$ và $0{,}00245$; với bước dài $1$ trên logit, xấp xỉ bậc hai lệch KL thật $0{,}0049$ tại $\theta=0$ và $0{,}00087$ tại $\theta=5$.

Bỏ giả thiết $\pi_\theta>0$ thì Bước 2–3 mất căn cứ, vì $\log\pi_\theta$ và $\psi_\theta$ cần xác định: nếu một xác suất tiến về $0$ trong khi $\pi_{\mathrm{old}}$ của hành động đó dương, KL tiến ra vô cùng và không có khai triển nào. KL theo chiều ngược, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{old}})$, có cùng giá trị, gradient và Hessian tại $\theta_{\mathrm{old}}$, nên hai chiều KL có cùng xấp xỉ bậc hai $\tfrac12\Delta^\top F\Delta$.

::: example Ví dụ 10.15 (Ma trận Fisher của bài toán một bước)
**Dữ kiện.** Bài toán một bước: chính sách softmax với $\theta=(\log2;\,0)$, $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$. Đặt $u=(1;\,-1)$, nên $\psi_\theta(s,1)=\tfrac13u$ và $\psi_\theta(s,2)=-\tfrac23u$.

**Ma trận Fisher tại $s$.**
$$\begin{aligned}F_s&=\tfrac23\cdot\tfrac19\,uu^\top+\tfrac13\cdot\tfrac49\,uu^\top\\&=\tfrac29\,uu^\top=\tfrac29\begin{pmatrix}1&-1\\-1&1\end{pmatrix}.\end{aligned}$$

**Suy biến.** $F_s(1;\,1)=0$, nên $F_s$ suy biến với hạt nhân (kernel, null space) $\operatorname{span}\{(1;\,1)\}$. Cộng cùng một hằng vào hai logit giữ nguyên chính sách softmax, nên KL bằng $0$ dọc hướng $(1;\,1)$.

**Kiểm tra lại.** Phần tử $(1,1)$: $\tfrac23\cdot\tfrac19+\tfrac13\cdot\tfrac49=\tfrac6{27}=\tfrac29$.
:::

Thay hai xấp xỉ vào bài toán miền tin cậy được bài toán của mệnh đề sau, cho bước *gradient chính sách tự nhiên* (natural policy gradient) của Kakade (2002) (Schulman và cộng sự, 2015, §7, (17)).

::: proposition Mệnh đề 10.34 (Bước gradient tự nhiên)
**Giả thiết.** $g\in\mathbb R^d$, $g\ne0$; $F\in\mathbb R^{d\times d}$ đối xứng, nửa xác định dương; $\kappa>0$. Xét bài toán
$$\begin{aligned}&\max_{\Delta\in\mathbb R^d}\ g^\top\Delta\\&\text{với ràng buộc}\quad\tfrac12\Delta^\top F\Delta\le\kappa .\end{aligned}$$

**Kết luận.**

- (a) Nếu $F$ xác định dương, bài toán có nghiệm duy nhất $\Delta^*=\sqrt{\dfrac{2\kappa}{g^\top F^{-1}g}}\,F^{-1}g$, với giá trị tối ưu $\sqrt{2\kappa\,g^\top F^{-1}g}$.
- (b) Nếu $F$ suy biến và $g\in\operatorname{range}F$, kết luận (a) đúng khi thay $F^{-1}$ bằng giả nghịch đảo (pseudoinverse) $F^+$, và tập nghiệm là $\Delta^*+\ker F$.
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

Bước tối ưu gồm hai quyết định:

- hướng: $F^{-1}g$, gọi là *gradient tự nhiên* (natural gradient);
- độ dài: hệ số $\sqrt{2\kappa/(g^\top F^{-1}g)}$, đưa bước tới biên của miền tin cậy bậc hai.

Gradient thường $g$ là hướng tăng nhanh nhất khi đo bước bằng chuẩn Euclid, $F^{-1}g$ khi đo bằng $\lVert\cdot\rVert_F$. Nhân $g$ với một hằng dương không đổi $\Delta^*$, nên thừa số $1/(1-\gamma)$ trong hàm thay thế không ảnh hưởng; chỉ thang của $F$ quyết định độ dài bước.

Giả thiết $g\in\operatorname{range}F$ của (b) luôn thỏa khi $g$ và $F$ được tính với cùng phân bố của $(S,A)$. Thật vậy, $F=\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)\,\psi(s,a)\psi(s,a)^\top$ với trọng số dương trên miền $\nu^{\mathrm{old}}(s)\pi_{\mathrm{old}}(a\mid s)>0$, nên $\operatorname{range}F$ là không gian sinh bởi các hàm điểm $\psi(s,a)$ trên miền đó. Gradient $g=\tfrac1{1-\gamma}\sum_s\nu^{\mathrm{old}}(s)\sum_a\pi_{\mathrm{old}}(a\mid s)A_{\mathrm{old}}(s,a)\psi(s,a)$ là một tổ hợp tuyến tính của chính các véc-tơ đó. Trường hợp (c) có thể xảy ra khi $g$ và $F$ lấy trên hai tập trạng thái khác nhau.

::: example Ví dụ 10.16 (Bước gradient tự nhiên trên bài toán một bước)
**Dữ kiện.** Bài toán một bước của Ví dụ 10.15: $r=(3;\,0)$, $\theta=(\log2;\,0)$, $g=\nabla_\theta J=(\tfrac23;\,-\tfrac23)=\tfrac23u$ với $u=(1;\,-1)$, $F_s=\tfrac29uu^\top$. Ràng buộc là KL tại chính trạng thái $s$, $\tfrac12\Delta^\top F_s\Delta\le\kappa$, với $\kappa=0{,}01$.

**Giả nghịch đảo.** $u^\top u=2$, nên $(uu^\top)^+=uu^\top/4$ và $F_s^+=\tfrac92\cdot\tfrac14uu^\top=\tfrac98uu^\top$. Kiểm giả thiết: $g\perp(1;\,1)$, nên $g\in\operatorname{range}F_s$.

**Hướng và độ dài.** $F_s^+g=\tfrac98\cdot\tfrac23\cdot2\,u=(1{,}5;\,-1{,}5)$ và $g^\top F_s^+g=\tfrac23\cdot1{,}5\cdot2=2$. Hệ số độ dài là $\sqrt{2\cdot0{,}01/2}=0{,}1$, nên $\Delta^*=(0{,}15;\,-0{,}15)$.

**Chính sách mới.** $\theta=(\log2+0{,}15;\,-0{,}15)$, $p_1=2/(2+e^{-0{,}3})=0{,}7297$, và $J=3p_1=2{,}189$, tăng từ $2$. KL thật theo chiều cũ‖mới là $0{,}009644$ và theo chiều mới‖cũ là $0{,}009269$, so với giá trị bậc hai $\kappa=0{,}01$.

**Kiểm tra lại.** $\tfrac12\Delta^{*\top}F_s\Delta^*=\tfrac12\cdot\tfrac29\cdot(0{,}3)^2=0{,}01$. Mọi $\Delta^*+c(1;\,1)$ cho cùng chính sách, đúng như tập nghiệm của Mệnh đề 10.34(b).
:::

Trên chuỗi hai trạng thái, tại $\theta=(0;\,\log2)$ và với $\kappa=0{,}01$, mỗi trạng thái có một tham số nên $F$ chéo. Với $F_s=p_s(1-p_s)$ và $\nu^\pi=(0{,}1;\,0{,}045)$, $F=\operatorname{diag}(0{,}1\cdot\tfrac14;\,0{,}045\cdot\tfrac29)=\operatorname{diag}(0{,}025;\,0{,}01)$. Với $g=(0{,}2;\,0{,}3)$ của Ví dụ 10.6:

- $F^{-1}g=(8;\,30)$ và $g^\top F^{-1}g=0{,}2\cdot8+0{,}3\cdot30=10{,}6$;
- tỉ trọng hai thành phần, tính theo tổng giá trị tuyệt đối: $g$ cho $\tfrac{0{,}2}{0{,}5}=40\%$ và $60\%$, còn $F^{-1}g$ cho $\tfrac8{38}\approx21\%$ và $\tfrac{30}{38}\approx79\%$;
- hệ số độ dài $\sqrt{2\cdot0{,}01/10{,}6}\approx0{,}0434$, nên $\Delta^*\approx(0{,}35;\,1{,}30)$;
- chính sách mới $p_A=\sigma(0{,}35)\approx0{,}586$, $p_B=\sigma(\log2+1{,}30)\approx0{,}880$, với KL trung bình thật theo chiều cũ‖mới $\approx0{,}0085\le\kappa$ và $J\approx1{,}807$, tăng $0{,}407$, khoảng $29\%$.

Gradient tự nhiên dồn bước về $\theta_B$. Với một logit mỗi trạng thái, $g_s=\eta_\pi(s)\,p_s(1-p_s)\bigl(A_\pi(s,1)-A_\pi(s,2)\bigr)$ và $F_{ss}=\nu(s)\,p_s(1-p_s)$, nên $(F^{-1}g)_s=\bigl(A_\pi(s,1)-A_\pi(s,2)\bigr)/(1-\gamma)$, tức $0{,}8/0{,}1=8$ và $3/0{,}1=30$. Vì $g_s=F_{ss}(F^{-1}g)_s$ với $(F_{AA};\,F_{BB})=(0{,}025;\,0{,}01)$, thành phần $s_B$ của $g$ bị nhân với thừa số nhỏ hơn, chủ yếu do $\nu(s_B)=0{,}045<0{,}1$; gradient tự nhiên chia cho $F_{ss}$ nên bỏ thừa số này, chỉ còn chênh lệch lợi thế (Kakade, 2002). Tỉ trọng chỉ so hướng, không so độ dài bước.

Bước theo $g$, co về cùng bán kính bậc hai, là $\Delta\approx(0{,}649;\,0{,}973)$; nó cho $p\approx(0{,}657;\,0{,}841)$, KL thật $0{,}0093$ và $J\approx1{,}835$, cao hơn $1{,}807$. Bước gradient tự nhiên là $\Delta^*=(0{,}3475;\,1{,}3031)$. Bảng sau so hai bước trên ba tầng:

- tầng 1: hiệu năng thật $J$;
- tầng 2: mức tăng $\Delta\mathcal L=0{,}8\,\Delta p_A+1{,}35\,\Delta p_B$ của hàm thay thế (Ví dụ 10.12), tính chính xác;
- tầng 3: mức tăng tuyến tính $g^\top\Delta$, đại lượng mà Mệnh đề 10.34 cực đại hóa với ràng buộc $\tfrac12\Delta^\top F\Delta\le\kappa$.

| Tầng | Đại lượng | Theo $g$ | Theo $F^{-1}g$ |
|---|---|---|---|
| 1 | $J$ | $1{,}835$ | $1{,}807$ |
| 2 | $\Delta\mathcal L$ | $0{,}361$ | $0{,}357$ |
| 3 | $g^\top\Delta$ | $0{,}422$ | $0{,}460$ |

Gradient tự nhiên là nghiệm của bài toán ở tầng 3, nên cho giá trị lớn hơn ở tầng đó. Tầng 2 thay $g^\top\Delta$ bằng hàm thay thế thật, tuyến tính theo $\Delta p_s$ nhưng phi tuyến theo $\theta$ vì $p_s=\sigma(\theta_s)$. Tầng 1 cộng thêm sai số $2{,}7\,\Delta p_A\,\Delta p_B$ do phân bố trạng thái thay đổi: $0{,}074$ cho bước theo $g$ và $0{,}050$ cho bước gradient tự nhiên. Ở tầng 2 và tầng 1, bước theo $g$ cho giá trị lớn hơn. Nghiệm của bài toán xấp xỉ cục bộ vì vậy không nhất thiết tốt nhất cho hàm thay thế hay cho $J$. Ưu điểm của gradient tự nhiên là độ dài bước đo trên phân phối hành động, nên không phụ thuộc cách tham số hóa.

::: remark Nhận xét 10.35 (Ma trận Fisher suy biến)
Với chính sách softmax, hướng cộng cùng một hằng vào mọi logit của một trạng thái nằm trong $\ker F$; khi các trạng thái có tham số chung, hạt nhân có thể nhỏ hơn. Giả nghịch đảo chọn nghiệm có chuẩn nhỏ nhất trong $\Delta^*+\ker F$. Mọi nghiệm cho cùng giá trị của mô hình bậc hai; với softmax có tham số riêng cho từng trạng thái, các nghiệm cho đúng cùng một chính sách trên các trạng thái có $\nu^{\mathrm{old}}(s)>0$.
:::

**Trong thực hành.** Bộ đệm không có trọng số chiết khấu của $\nu^{\mathrm{old}}$, và $\Delta^*$ chỉ thỏa ràng buộc bậc hai: ở Ví dụ 10.16, KL thật là $0{,}009644$ so với $\kappa=0{,}01$.

<!-- note-topic-id: lec-10-topic-16 -->
### 5.2 TRPO thực hành

Với mạng nơ-ron, $d$ có thể lên tới hàng triệu, nên lập ma trận $F\in\mathbb R^{d\times d}$ cần $O(d^2)$ bộ nhớ và nghịch đảo nó cần $O(d^3)$ phép tính (Schulman và cộng sự, 2015, Phụ lục C). Hệ phương trình $Fx=g$ vẫn giải gần đúng được nếu chỉ tính được tích $v\mapsto Fv$.

Phương pháp *gradient liên hợp* (conjugate gradient) làm đúng việc đó: nó cực tiểu hóa mô hình bậc hai $\tfrac12x^\top Fx-g^\top x$, có gradient $Fx-g$ triệt tiêu đúng tại nghiệm của $Fx=g$.

Hai hướng $p$, $p'$ gọi là *liên hợp* (conjugate) đối với $F$ nếu $p^\top Fp'=0$. Về mặt ý tưởng, phương pháp cực tiểu hóa mô hình lần lượt theo các hướng đôi một liên hợp, nên bước theo hướng sau giữ nguyên phần cực tiểu đã đạt theo các hướng trước. Ví dụ sau chạy hai vòng.

::: example Ví dụ 10.17 (Hai vòng gradient liên hợp)
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

Trên hình là miền tin cậy bậc hai của Ví dụ 10.17. Elip hẹp theo trục thứ nhất, nơi $F$ lớn. Gradient $g=(2;\,1)$ nghiêng về trục thứ nhất, còn bước tối ưu $(0{,}05;\,0{,}1)$ nghiêng về trục thứ hai, nơi elip rộng.

::: algorithm Thuật toán 10.36 (Gradient liên hợp với tích Fisher–vector)
**Đầu vào.** Hàm $v\mapsto Fv$; véc-tơ $g$; số vòng tối đa $k_{\max}$; ngưỡng $\varepsilon_{\mathrm{cg}}>0$.

**Đầu ra.** Nghiệm gần đúng $x\approx F^{-1}g$ và số $\tau\approx x^\top Fx$.

**Giả thiết.** $F$ đối xứng, nửa xác định dương; $g\in\operatorname{range}F$.

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

Thuật toán là Thuật toán 5.2 của Nocedal và Wright (2006, tr. 112). Với $F$ xác định dương và số học chính xác, thuật toán cho nghiệm đúng sau không quá $d$ vòng (Nocedal và Wright, 2006, Định lý 5.1, tr. 103), và số vòng không vượt số giá trị riêng phân biệt của $F$ (Định lý 5.4, tr. 115 của cùng sách); $F=\operatorname{diag}(4;\,1)$ có hai giá trị riêng nên Ví dụ 10.17 dừng sau hai vòng.

Số $\tau$ bằng $x^\top Fx$ trong số học chính xác: $x_K=\sum_{k<K}\omega_kp_k$, các hướng liên hợp nên $x_K^\top Fx_K=\sum_{k<K}\omega_k^2\,p_k^\top Fp_k$, và $\omega_k\,p_k^\top Fp_k=\tilde g_k^\top\tilde g_k$. Trên Ví dụ 10.17, $\tau_2=\tfrac5{17}\cdot5+0{,}85\cdot\tfrac{180}{289}=1{,}4706+0{,}5294=2=x_2^\top Fx_2$. Schulman và cộng sự (2015, Phụ lục C, C.1) dùng $k_{\max}=10$ vòng và tính tích Fisher–vector trên khoảng $10\%$ dữ liệu, để tổng chi phí các tích này xấp xỉ chi phí một lần tính gradient.

Khi tích $Fv$ tính trên một tập con, $F$ chỉ sinh từ hàm điểm tại các trạng thái của tập con; với $d$ lớn hơn nhiều số mẫu, $g$ nói chung không thuộc $\operatorname{range}F$, và nghiệm sau $k_{\max}$ vòng chỉ là một hướng gần đúng. *Tìm kiếm lùi* (backtracking line search) của Thuật toán 10.37 kiểm lại KL và hàm thay thế trước khi nhận bước.

::: algorithm Thuật toán 10.37 (TRPO với lợi thế GAE)
**Đầu vào.** Chính sách $\pi_\theta$, critic $\hat v(s,w)$; bán kính $\kappa>0$; hệ số co $\zeta\in(0,1)$ và số lần co tối đa $j_{\max}$; số môi trường $N$, độ dài đoạn $h$; $\gamma$, $\lambda$; tham số của Thuật toán 10.36.

**Đầu ra.** Tham số $\theta$, $w$ sau số vòng lặp đã định.

**Giả thiết.** Chính sách khả vi hai lần, $\pi_\theta>0$; dữ liệu mỗi vòng do $\pi_{\mathrm{old}}$ sinh ra.

**Mỗi vòng lặp:**

1. $\theta_{\mathrm{old}}\leftarrow\theta$, $w_{\mathrm{old}}\leftarrow w$. Thu $h$ bước trên mỗi môi trường bằng $\pi_{\mathrm{old}}$, lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$ và cả phân phối $\pi_{\mathrm{old}}(\cdot\mid S_t)$, với chính sách softmax là các logit; bộ đệm $\mathcal D$ gồm $hN$ mẫu.
2. Theo Thuật toán 10.16, tính lùi trên đoạn, với $\widehat A_h=0$ và $\hat v(S_{t+1},w_{\mathrm{old}})$ lấy ở quan sát cuối khi $U_{t+1}=1$:
   - $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w_{\mathrm{old}})-\hat v(S_t,w_{\mathrm{old}})$;
   - $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})(1-U_{t+1})\widehat A_{t+1}$;
   - $V^{\mathrm{targ}}_t=\widehat A_t+\hat v(S_t,w_{\mathrm{old}})$.
3. Với $\widehat{\mathcal L}(\theta)=\widehat{\mathbb E}_{\mathcal D}[\rho_t(\theta)\widehat A_t]$ và $\widehat D(\theta)=\widehat{\mathbb E}_{\mathcal D}\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid S_t)\Vert\pi_\theta(\cdot\mid S_t))\bigr]$, tính $g=\nabla\widehat{\mathcal L}(\theta_{\mathrm{old}})=\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$.
4. Giải $Fx=g$ gần đúng bằng Thuật toán 10.36, với $F$ là Hessian của $\widehat D$ tại $\theta_{\mathrm{old}}$.
5. Bước đầy đủ: $\Delta_0=\sqrt{2\kappa/(x^\top Fx)}\;x$.
6. *Tìm kiếm lùi*: với $j=0,1,\dots,j_{\max}$, đặt $\theta=\theta_{\mathrm{old}}+\zeta^j\Delta_0$ và nhận giá trị $j$ đầu tiên thỏa $\widehat{\mathcal L}(\theta)>\widehat{\mathcal L}(\theta_{\mathrm{old}})$ và $\widehat D(\theta)\le\kappa$; nếu không có $j$ nào, giữ $\theta=\theta_{\mathrm{old}}$.
7. Cập nhật critic: vài bước hạ gradient trên $\widehat{\mathbb E}_{\mathcal D}\bigl[(\hat v(S_t,w)-V^{\mathrm{targ}}_t)^2\bigr]$.

**Điều kiện dừng.** Sau số vòng lặp hoặc số bước môi trường đã định.

**Chi phí mỗi vòng lặp.** $hN$ bước môi trường; một gradient; $k_{\max}$ tích Fisher–vector; tối đa $j_{\max}+1$ lần tính $\widehat{\mathcal L}$ và $\widehat D$ trên dữ liệu.
:::

Bước 5 là công thức của Schulman và cộng sự (2015, Phụ lục C): với $x\approx F^{-1}g$, bước đó là $\Delta^*$ của Mệnh đề 10.34, và $x^\top Fx$ là số $\tau$ của Thuật toán 10.36. Ví dụ 10.17 thực hiện bước 4–5 bằng tay; Ví dụ 10.16 cho thấy một bước như vậy làm $J$ tăng từ $2$ lên $2{,}189$ với KL thật $0{,}009644\le\kappa$, nên bước 6 nhận ngay $j=0$.

Bài báo TRPO gốc (Schulman và cộng sự, 2015, §5) ước lượng $Q_{\theta_{\mathrm{old}}}$ bằng lợi tức Monte Carlo và không dùng critic; bước 3–6 theo bài báo này. Bước 2 theo cách Schulman và cộng sự (2016) ghép TRPO với GAE.

**Trong thực hành.** Bước 6 cần thiết vì hàm thay thế và KL thật là phi tuyến; nó kiểm hai đại lượng mẫu, không kiểm $J$, vì chính sách mới chưa chạy.

::: remark Nhận xét 10.38 (Những gì TRPO thực hành mất so với Định lý 10.27)
So với các giả thiết của Định lý 10.27 và Hệ quả 10.30, Thuật toán 10.37 thay đổi năm điểm:

- trung bình đều trên bộ đệm thay cho kỳ vọng theo $\nu^{\mathrm{old}}$ có chiết khấu;
- lợi thế ước lượng bằng GAE thay cho $A_{\mathrm{old}}$ chính xác;
- hàm thay thế bậc một và KL bậc hai thay cho hai hàm thật;
- gradient liên hợp dừng sau $k_{\max}$ vòng, cho nghiệm gần đúng;
- ràng buộc KL trung bình thay cho phạt TV với hằng của lý thuyết.

Điều còn lại sau tìm kiếm lùi là hai bất đẳng thức trên chính bộ đệm: KL trung bình mẫu không vượt $\kappa$, và hàm thay thế mẫu tăng.
:::

TRPO chọn từ một bộ đệm một bước lớn theo hướng gradient tự nhiên, độ dài do bán kính KL quyết định, và kiểm bước trên mẫu trước khi nhận. Cái giá là khoảng mười tích Fisher–vector, một lượt tìm kiếm lùi và một bộ máy bậc hai riêng cho mỗi vòng lặp; Schulman và cộng sự (2017, §1) nêu thêm rằng TRPO tương đối phức tạp và không tương thích với kiến trúc có nhiễu, như dropout, hoặc dùng chung tham số giữa chính sách và hàm giá trị. Trong Mục 6, chúng ta đưa giới hạn khoảng cách vào chính hàm mục tiêu để tối ưu bằng phương pháp bậc một.

---

## 6. Tối ưu chính sách gần kề (PPO)

Trên bài toán một bước, bước TRPO của Ví dụ 10.16 đã cần giả nghịch đảo của ma trận Fisher và một phép kiểm KL thật. Schulman và cộng sự (2017, §1, §3) giữ mục tiêu của TRPO, dùng lại dữ liệu từ chính sách cũ để thực hiện các bước cập nhật hiệu quả, đồng thời kiểm soát nguy cơ suy giảm hiệu năng, nhưng chỉ dùng tối ưu bậc một: viết một hàm mục tiêu cực đại hóa được bằng vài epoch SGD hoặc Adam trên mini-batch mà không thưởng cho việc đẩy tỉ số chính sách ra xa $1$.

<!-- note-topic-id: lec-10-topic-17 -->
### 6.1 PPO-Clip

Gọi $\mathcal L^{\mathrm{CPI}}(\theta)=\widehat{\mathbb E}_{\mathcal D}[\rho_t(\theta)\widehat A_t]$ là hàm thay thế mẫu của Mục 4.2, bỏ hằng $J(\theta_{\mathrm{old}})$ (CPI: *phương pháp lặp chính sách bảo thủ*, conservative policy iteration, của Kakade và Langford, 2002). Mỗi mẫu đóng góp $\rho_t\widehat A_t$, nên với lợi thế dương, $\mathcal L^{\mathrm{CPI}}$ tăng tuyến tính khi $\rho_t$ tăng, dù chính sách mới đã rời xa vùng mà Mệnh đề 10.22 bảo đảm khớp.

Trên chuỗi hai trạng thái với lợi thế đúng $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$ và $A_\pi(s_B,\cdot)=(1;\,-2)$, ta có $A_\pi(s_A,\pi')=0{,}8p_A-0{,}4$ và $A_\pi(s_B,\pi')=3p_B-2$. Cả hai tăng, nên mọi trung bình có trọng số dương của chúng, gồm trung bình đều trên bộ đệm và hàm thay thế $\mathcal L_\pi(\pi')$ của Mục 4.2, đạt cực đại không ràng buộc tại $(p_A;\,p_B)=(1;\,1)$, với $J=2{,}7$, chính sách tối ưu. Tại điểm này $\mathcal L_\pi(\pi')-J(\pi)=0{,}85$, trong khi $J$ tăng $1{,}3$: sai số lớn, nhưng không đổi hướng cập nhật. Trên chuỗi, với lợi thế đúng, tối ưu $\mathcal L^{\mathrm{CPI}}$ tới biên không làm $J$ giảm. Tổng quát, rủi ro của việc tối ưu $\mathcal L^{\mathrm{CPI}}$ quá lâu đến từ hai nguồn: sai số của hàm thay thế khi chính sách mới rời xa chính sách cũ, được Định lý 10.27 chặn theo TV, và lợi thế ước lượng sai dấu.

Về mặt ý tưởng, mục tiêu cần ngừng thưởng cho một mẫu khi tỉ số của nó đã vượt một ngưỡng theo hướng có lợi. Xét hai mẫu tại $s_B$, với chính sách cũ $(\tfrac23;\,\tfrac13)$, lợi thế đúng và $\epsilon=0{,}2$:

- hành động 1, $A=+1$: đóng góp vào $\mathcal L^{\mathrm{CPI}}$ là $\rho$, nên việc tăng xác suất của hành động 1 được thưởng mãi; PPO-Clip ngừng thưởng khi $\rho>1+\epsilon=1{,}2$, với đóng góp $\ell=\min(\rho,\,1{,}2)\cdot1$;
- hành động 2, $A=-2$: đóng góp là $-2\rho$, nên việc giảm xác suất của hành động 2 làm số hạng bớt âm; PPO-Clip ngừng thưởng khi $\rho<1-\epsilon=0{,}8$, với đóng góp $\ell=\min(-2\rho,\,-1{,}6)$.

Bảng sau tính hai đóng góp tại bốn tỉ số, với $\rho_{s_B}(1)=1{,}5p_B$ và $\rho_{s_B}(2)=3(1-p_B)$. Cột $a$ ghi hành động ($A=+1$ khi $a=1$, $A=-2$ khi $a=2$), cột $\rho A$ ghi đóng góp vào $\mathcal L^{\mathrm{CPI}}$ và cột $\ell$ ghi đóng góp vào mục tiêu cắt.

| $a$ | $\rho$ | $p_B$ | $\rho A$ | $\ell$ |
|---|---|---|---|---|
| 1 | $1{,}3$ | $0{,}867$ | $1{,}3$ | $1{,}2$ |
| 1 | $0{,}7$ | $0{,}467$ | $0{,}7$ | $0{,}7$ |
| 2 | $0{,}7$ | $0{,}767$ | $-1{,}4$ | $-1{,}6$ |
| 2 | $1{,}3$ | $0{,}567$ | $-2{,}6$ | $-2{,}6$ |

Quy tắc rút ra từ bảng: phép cắt chỉ bỏ phần cải thiện dự báo vượt ngưỡng theo hướng có lợi, ở dòng thứ nhất và dòng thứ ba; khi tỉ số thay đổi theo hướng bất lợi, ở dòng thứ hai và dòng thứ tư, đóng góp giữ nguyên $\rho A$. Hai trường hợp gộp thành một công thức cho mọi dấu của lợi thế, $\ell=\min\bigl(\rho A,\ \operatorname{clip}(\rho,1-\epsilon,1+\epsilon)A\bigr)$, với $\operatorname{clip}(x,l,u)=\min(\max(x,l),u)$.

**Câu hỏi.** Vì sao lấy $\min$ với $\rho A$ thay vì chỉ dùng $\operatorname{clip}(\rho,1-\epsilon,1+\epsilon)A$? Số hạng chỉ cắt che tín hiệu ở hướng bất lợi: ở dòng cuối của bảng, nó cho $1{,}2\cdot(-2)=-2{,}4$ thay cho $-2{,}6$, và ở dòng thứ hai, $0{,}8$ thay cho $0{,}7$. Phép $\min$ chọn giá trị bảo thủ hơn trong hai giá trị, nên chỉ phần thưởng của cập nhật vượt ngưỡng theo hướng có lợi bị bỏ.

Ví dụ sau cộng ba mẫu có đúng tần suất của chính sách cũ, trên bài toán một bước có cùng chính sách cũ và cùng lợi thế đúng như $s_B$.

::: example Ví dụ 10.18 (Hai hàm thay thế mẫu trên bài toán một bước)
**Dữ kiện.** Bài toán một bước với chính sách cũ $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $r=(3;\,0)$. Bộ đệm ba mẫu, hành động $1,1,2$, đúng tần suất của $\pi_{\mathrm{old}}$, với lợi thế $\widehat A=(1;\,1;\,-2)$, là lợi thế đúng của Ví dụ 10.5. *Bán kính cắt* (clipping parameter, clip range) $\epsilon=0{,}2$. Chính sách mới chọn hành động 1 với xác suất $p$, nên $\rho(1)=p/\tfrac23=1{,}5p$ và $\rho(2)=(1-p)/\tfrac13=3(1-p)$.

**Mục tiêu không cắt.** $\mathcal L^{\mathrm{CPI}}(p)=\tfrac13\bigl[1{,}5p+1{,}5p-2\cdot3(1-p)\bigr]=3p-2$. Ở đây $\mathcal L^{\mathrm{CPI}}$ bằng đúng $J(p)-J_{\mathrm{old}}=3p-2$, vì chỉ có một bước và tần suất mẫu trùng $\pi_{\mathrm{old}}$.

**Mục tiêu cắt.** Hai mẫu hành động 1 có lợi thế dương nên bị chặn trên ở $\rho=1{,}2$, tức $p=0{,}8$; mẫu hành động 2 có lợi thế âm nên bị chặn dưới ở $\rho=0{,}8$, tức $p=0{,}7\overline3$. Do đó

- khi $p\le0{,}7\overline3$: $\mathcal L^{\mathrm{CLIP}}(p)=3p-2$;
- khi $0{,}7\overline3<p\le0{,}8$: $\mathcal L^{\mathrm{CLIP}}(p)=\tfrac13(3p-1{,}6)=p-0{,}5\overline3$;
- khi $p\ge0{,}8$: $\mathcal L^{\mathrm{CLIP}}(p)=\tfrac13(2{,}4-1{,}6)=0{,}2\overline6$.

**Diễn giải.** Hai mục tiêu trùng nhau tới $p=0{,}7\overline3$; sau đó mục tiêu cắt tăng chậm hơn, và từ $p=0{,}8$ nó hằng, nên gradient bằng $0$ và không còn động lực tăng $p$.

**Kiểm tra lại.** Tại $p=0{,}75$: $\mathcal L^{\mathrm{CLIP}}=0{,}2167$ và $\mathcal L^{\mathrm{CPI}}=0{,}25$. Tại $p=0{,}7\overline3$, cả hai khúc đầu bằng $0{,}2$, nên $\mathcal L^{\mathrm{CLIP}}$ liên tục.
:::

![Đồ thị theo p từ 0,5 đến 0,9. Đường thẳng nét đứt: L CPI bằng 3p trừ 2. Đường gấp khúc nét liền: L CLIP, trùng 3p trừ 2 tới p bằng 0,733, sau đó bằng p trừ 0,533 tới p bằng 0,8, rồi nằm ngang ở 0,267. Hai đường thẳng đứng mảnh đánh dấu p bằng 0,733 (mẫu hành động 2 chạm rho bằng 0,8) và p bằng 0,8 (mẫu hành động 1 chạm rho bằng 1,2). Điểm p bằng 2/3 ghi chính sách cũ, nơi hai đường trùng nhau.](img/lec-10/ppo-one-step-plateau.svg)

Trên hình, đường gấp khúc nằm dưới đường thẳng ở mọi $p$, trùng nó quanh chính sách cũ $p=\tfrac23$, và trở nên nằm ngang từ $p=0{,}8$. Hai mốc gấp ứng với hai lúc một nhóm mẫu chạm biên của khoảng cắt. Với ba mẫu tại $s_B$, hành động $1,1,2$, mục tiêu cắt theo $p_B$ trùng $\mathcal L^{\mathrm{CLIP}}$ của Ví dụ 10.18 và nằm ngang từ $p_B=0{,}8$. Định nghĩa sau viết mục tiêu cắt cho bộ đệm tổng quát.

::: definition Định nghĩa 10.39 (Mục tiêu PPO-Clip)
Cho bộ đệm $\mathcal D$ các mẫu $(S_t,A_t,\widehat A_t)$ do $\pi_{\mathrm{old}}$ sinh ra, tỉ số $\rho_t(\theta)$ của Định nghĩa 10.21 và bán kính cắt $\epsilon\in(0,1)$. Với $\operatorname{clip}(x,l,u)=\min(\max(x,l),u)$, số hạng cắt của mẫu $t$ là
$$\begin{aligned}&\ell^{\mathrm{CLIP}}_t(\theta)\\&=\min\bigl(\rho_t(\theta)\widehat A_t,\\&\quad\operatorname{clip}(\rho_t(\theta),1-\epsilon,1+\epsilon)\,\widehat A_t\bigr).\end{aligned}$$
*Mục tiêu PPO-Clip* và *mục tiêu không cắt* là
$$\begin{aligned}\mathcal L^{\mathrm{CLIP}}(\theta)&=\widehat{\mathbb E}_{\mathcal D}\bigl[\ell^{\mathrm{CLIP}}_t(\theta)\bigr],\\\mathcal L^{\mathrm{CPI}}(\theta)&=\widehat{\mathbb E}_{\mathcal D}\bigl[\rho_t(\theta)\widehat A_t\bigr].\end{aligned}$$
:::

Mệnh đề sau viết lại phép $\min$ theo dấu của lợi thế, tổng quát hóa hai trường hợp của bảng tại $s_B$.

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

Đọc bằng lời: với lợi thế dương, mục tiêu thưởng cho việc tăng xác suất của hành động chỉ tới khi tỉ số đạt $1+\epsilon$; với lợi thế âm, nó thưởng cho việc giảm xác suất chỉ tới khi tỉ số đạt $1-\epsilon$. Phía bất lợi không bị cắt: một hành động có lợi thế dương mà xác suất đã giảm, $\rho_t<1-\epsilon$, vẫn nhận đủ gradient kéo xác suất trở lại. Một nhầm lẫn thường gặp là cho rằng mọi mẫu ngoài khoảng cắt có gradient bằng $0$; theo (d), điều đó chỉ đúng khi tỉ số ra ngoài theo hướng có lợi. Tại hai điểm gấp, vi phân tự động trả về gradient của một trong hai nhánh.

![Hai khung cạnh nhau, trục hoành rho, epsilon bằng 0,2. Khung trái, A mũ dương: l CLIP bằng A mũ nhân min(rho; 1,2), đường tăng tuyến tính tới rho bằng 1,2 rồi nằm ngang; vùng nằm ngang tô sọc ghi gradient bằng 0. Điểm tròn tại rho bằng 1,3 trên đoạn ngang, giá trị 2,4; điểm vuông tại rho bằng 0,7 trên đoạn dốc, giá trị 1,4. Khung phải, A mũ âm: l CLIP bằng A mũ nhân max(rho; 0,8), đường nằm ngang tới rho bằng 0,8 rồi giảm tuyến tính; vùng nằm ngang tô sọc ghi gradient bằng 0. Điểm tròn tại rho bằng 0,7 trên đoạn ngang, giá trị âm 1,6; điểm vuông tại rho bằng 1,3 trên đoạn dốc, giá trị âm 2,6. Đường nét đứt mảnh ở cả hai khung là A mũ nhân rho.](img/lec-10/ppo-clipping-signs.svg)

Hình trên được vẽ theo Hình 1 của Schulman và cộng sự (2017), với $\epsilon=0{,}2$ và bốn mẫu của ví dụ sau. Vùng tô sọc là tập có gradient bằng $0$ của Mệnh đề 10.40(d), nằm bên phải trong khung lợi thế dương và bên trái trong khung lợi thế âm; điểm tròn nằm trên đoạn phẳng, điểm vuông nằm trên đoạn dốc.

::: example Ví dụ 10.19 (Bốn mẫu)
**Dữ kiện.** $\epsilon=0{,}2$; bốn mẫu $(\widehat A;\,\rho)$: $(2;\,1{,}3)$, $(-2;\,0{,}7)$, $(2;\,0{,}7)$, $(-2;\,1{,}3)$.

**Tính.**

- $(2;\,1{,}3)$: $\min(2{,}6;\,2{,}4)=2{,}4$; lợi thế dương và $\rho>1{,}2$, nên mẫu nằm trên đoạn phẳng, gradient bằng $0$.
- $(-2;\,0{,}7)$: $\min(-1{,}4;\,-1{,}6)=-1{,}6$; lợi thế âm và $\rho<0{,}8$, đoạn phẳng, gradient bằng $0$.
- $(2;\,0{,}7)$: $\min(1{,}4;\,1{,}6)=1{,}4$; phía bất lợi, gradient $2\cdot0{,}7\,\psi\ne0$.
- $(-2;\,1{,}3)$: $\min(-2{,}6;\,-2{,}4)=-2{,}6$; phía bất lợi, gradient $-2\cdot1{,}3\,\psi\ne0$.

**Kiểm tra lại.** Theo dạng theo dấu: $2\min(1{,}3;\,1{,}2)=2{,}4$, $-2\max(0{,}7;\,0{,}8)=-1{,}6$, $2\min(0{,}7;\,1{,}2)=1{,}4$, $-2\max(1{,}3;\,0{,}8)=-2{,}6$.
:::

**Câu hỏi.** Phép cắt ngăn cập nhật vượt ngưỡng theo hướng có lợi, nhưng nó có sửa được lợi thế ước lượng sai dấu không? Xét chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$ của Mục 3 và $\lambda=1$. Giả sử bộ đệm chỉ có hai lượt: $s_A\xrightarrow1s_B\xrightarrow2$, với lợi tức $0$, và $s_A\xrightarrow2$, với lợi tức $1$; bộ đệm này xảy ra với xác suất $2\cdot\tfrac16\cdot\tfrac12=\tfrac16$. Lợi thế ước lượng là $0-1{,}4=-1{,}4$ cho hành động 1 tại $s_A$, $1-1{,}4=-0{,}4$ cho hành động 2 tại $s_A$ và $0-1=-1$ cho hành động 2 tại $s_B$, trong khi lợi thế đúng là $0{,}4$, $-0{,}4$ và $-2$.

Tại $s_A$, critic đúng, $\hat v(s_A)=v_\pi(s_A)=1{,}4$, nên ước lượng với $\lambda=1$ không chệch; lợi thế của hành động 1 sai dấu do phương sai của lợi tức một lượt, không do critic. Với $\rho_{s_A}(1)=2p_A$, $\rho_{s_A}(2)=2(1-p_A)$, $\rho_{s_B}(2)=3(1-p_B)$, mục tiêu không cắt tại $s_A$ là $\tfrac12\bigl[2p_A\cdot(-1{,}4)+2(1-p_A)\cdot(-0{,}4)\bigr]=-0{,}4-p_A$, và tại $s_B$ là $-3(1-p_B)$. Cực đại hóa không ràng buộc đẩy $p_A$ về $0$ và $p_B$ về $1$; mục tiêu tiến tới cận trên của nó khi $\theta_A\to-\infty$, $\theta_B\to+\infty$, và không tham số hữu hạn nào đạt cận này. Ở giới hạn đó $J=2{,}7\cdot0\cdot1+1-0=1{,}000$, tức $J$ giảm $0{,}4$ so với $J(\pi_{\mathrm{old}})=1{,}400$.

Với mục tiêu cắt và $\epsilon=0{,}2$: tại $s_A$, mỗi mẫu có trọng số $\tfrac12$ và cả hai lợi thế ước lượng đều âm, nên theo Mệnh đề 10.40(b), mục tiêu cắt là $\tfrac12\bigl[-1{,}4\max(2p_A;\,0{,}8)-0{,}4\max(2-2p_A;\,0{,}8)\bigr]$. Khi $p_A$ giảm từ $\tfrac12$, mẫu hành động 1 chạm biên $\rho=0{,}8$ tại $p_A=0{,}4$; dưới mức đó, chỉ mẫu hành động 2 còn đổi, theo hướng bất lợi và không bị cắt, nên mục tiêu cắt tại $s_A$ lớn nhất ở $p_A=0{,}4$. Tại $s_B$, mẫu duy nhất đóng góp $-\max(3-3p_B;\,0{,}8)$, nằm ngang từ $p_B=\tfrac{11}{15}\approx0{,}733$. Vòng trong dừng ở $(0{,}4;\,\tfrac{11}{15})$, với $J=2{,}7\cdot0{,}4\cdot\tfrac{11}{15}+0{,}6=1{,}392$: trong ví dụ này, $J$ giảm $0{,}008$, thay cho $0{,}4$ khi không cắt. Phép cắt không sửa lợi thế sai dấu và không bảo đảm $J$ tăng. Phép cắt loại bỏ động lực cải thiện dự báo vượt ngưỡng theo hướng có lợi. Trong ví dụ tối ưu lý tưởng hóa này, cơ chế đó tạo ra điểm dừng sớm hơn, nhưng không áp đặt giới hạn cứng lên độ dài bước cập nhật chính sách. Các giá trị $J=1{,}000$ và $J=1{,}392$ ứng với nghiệm của bài toán tối ưu lý tưởng hóa trên bộ đệm nhỏ này: $J=1{,}000$ tại chính sách giới hạn mà phép cực đại hóa mục tiêu không cắt tiến tới, còn $J=1{,}392$ tại điểm dừng của phép tăng gradient chính xác trên mục tiêu cắt, xuất phát từ chính sách cũ. Một số hữu hạn bước Adam cho điểm khác.

Từ $p_B=\tfrac{11}{15}$, phần của mục tiêu cắt tại $s_B$ hằng bằng $-0{,}8$, nên mọi $p_B\ge\tfrac{11}{15}$ cho cùng giá trị mục tiêu và gradient bằng $0$. Với $p_A=0{,}4$, KL tại $s_B$ theo chiều cũ‖mới và $J=2{,}7\cdot0{,}4\,p_B+0{,}6$ trên đoạn đó là:

- $p_B=\tfrac{11}{15}$: KL $\approx0{,}011$, $J=1{,}392$;
- $p_B=0{,}85$: KL $\approx0{,}104$, $J=1{,}518$;
- $p_B=0{,}95$: KL $\approx0{,}396$, $J=1{,}626$.

Mục tiêu cắt không phân biệt ba chính sách này, và nó dừng vòng trong ở $p_B=\tfrac{11}{15}$ dù $\partial J/\partial p_B=2{,}7\cdot0{,}4=1{,}08>0$. PPO-Clip cắt đóng góp của từng mẫu vào hàm mục tiêu và không đặt ràng buộc nào lên chính sách mới: trên cả đoạn, đóng góp của mẫu tại $s_B$ giữ giá trị $-0{,}8$, còn KL tại $s_B$ tăng từ $0{,}011$ lên $0{,}396$ khi các bước khác đẩy $p_B$ đi tiếp (Nhận xét 10.42). Sự gần nhau của hai chính sách là tính chất của toàn bộ phân phối hành động tại các trạng thái liên quan, đo bằng $D_{\mathrm{TV}}(s)$ hay $D_{\mathrm{KL}}(s)$ (Định nghĩa 10.23). Các tỉ số $\rho_t$ chỉ cho xác suất mới của những cặp $(S_t,A_t)$ có trong mẫu, nên vài tỉ số gần $1$ không suy ra được TV nhỏ.

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

**Bước 3 (kết luận c).** Tại $\theta_{\mathrm{old}}$, mọi $\rho_t=1$, nằm trong khoảng mở $(1-\epsilon,1+\epsilon)$. Vì $\pi_{\mathrm{old}}(A_t\mid S_t)>0$ và $\pi_\theta$ liên tục, mỗi $\rho_t$ liên tục theo $\theta$; bộ đệm hữu hạn nên có một lân cận $\mathcal N$ của $\theta_{\mathrm{old}}$ trên đó mọi $\rho_t\in(1-\epsilon,1+\epsilon)$. Theo Bước 2, trên $\mathcal N$ mọi $\ell^{\mathrm{CLIP}}_t=\rho_t\widehat A_t$, nên hai mục tiêu trùng nhau trên $\mathcal N$, kéo theo cùng giá trị và cùng gradient tại $\theta_{\mathrm{old}}$. Giá trị là $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t]$ vì $\rho_t=1$; gradient là $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$ vì $\nabla\rho_t=\rho_t\psi_t$. $\square$
:::

Kết luận (a) là lý do Schulman và cộng sự (2017, §3) gọi $\mathcal L^{\mathrm{CLIP}}$ là một *chặn dưới bi quan* (pessimistic bound) của mục tiêu không cắt: mục tiêu cắt bỏ phần tăng của $\mathcal L^{\mathrm{CPI}}$ khi tỉ số ra ngoài khoảng theo hướng có lợi, nhưng giữ phần giảm khi tỉ số đi theo hướng bất lợi.

Kết luận (c) là dạng mẫu của Mệnh đề 10.22: trên bộ đệm, $\mathcal L^{\mathrm{CLIP}}$ và $\mathcal L^{\mathrm{CPI}}$ khớp nhau đến bậc một tại $\theta_{\mathrm{old}}$, như $\mathcal L$ khớp $J$. Trên Ví dụ 10.18, hai mục tiêu trùng nhau trên $p\le0{,}7\overline3$, một lân cận của $p=\tfrac23$. Hai giả thiết của (c) có vai trò riêng.

- Bỏ "$\pi_{\mathrm{old}}(A_t\mid S_t)>0$": tỉ số không xác định.
- Bỏ "bộ đệm hữu hạn": mỗi mẫu có một lân cận riêng, và giao của vô hạn lân cận có thể chỉ còn điểm $\theta_{\mathrm{old}}$, nên một lân cận chung cho mọi mẫu có thể không tồn tại.

**Trong thực hành.** Theo kết luận (c), bước gradient đầu tiên của mỗi lần cập nhật, trên mini-batch đầu tiên của epoch đầu tiên, trùng đúng bước trên $\mathcal L^{\mathrm{CPI}}$ (Engstrom và cộng sự, 2020, §4). Điều này cho một phép kiểm cài đặt: ở bước đó mọi $\rho_t$ phải bằng $1$ trong sai số làm tròn, và một tỉ số lệch khỏi $1$ quá sai số làm tròn cho thấy log-xác suất cũ hoặc quan sát được lưu không khớp với lần tính lại.

::: remark Nhận xét 10.42 (Cắt tỉ số và khoảng cách KL)
1. Mục tiêu cắt chỉ loại động lực đẩy tỉ số của từng mẫu ra ngoài khoảng; nó không ngăn tỉ số ra ngoài. Sau vài bước, tỉ số có thể vượt khoảng vì ba lý do:
   - một bước trên mẫu này đổi xác suất của mẫu khác cùng trạng thái hoặc có đặc trưng gần;
   - các mini-batch khác nhau kéo tham số theo các hướng khác nhau;
   - quán tính của Adam tiếp tục đẩy tham số sau khi gradient đã bằng $0$.
2. Không có cận nào cho KL giữa $\pi_\theta$ và $\pi_{\mathrm{old}}$ suy ra từ Mệnh đề 10.41. Engstrom và cộng sự (2020, §4) đo được rằng tỉ số vượt khoảng cắt trong cả PPO và PPO không có các *tối ưu mức mã* (code-level optimizations), và rằng mức thay đổi chính sách phụ thuộc cách tối ưu mục tiêu cắt hơn là chính mục tiêu.
:::

Chúng ta đã dùng ba đại lượng khác nhau để đánh giá một chính sách mới $\pi'$.

| Đại lượng | Ý nghĩa | Trọng số trạng thái |
|---|---|---|
| $\Delta J$ | thay đổi hiệu năng thực khi chạy $\pi'$ | $\eta_{\pi'}$ (Bổ đề 10.19) |
| $\Delta\mathcal L$ | thay đổi dự báo theo phân bố trạng thái cũ | $\eta_{\pi_{\mathrm{old}}}$ |
| $\mathcal L^{\mathrm{CLIP}}$ | mục tiêu bi quan theo từng mẫu, tối ưu trên dữ liệu đã thu | trung bình đều trên bộ đệm |

Trên cùng dữ liệu và cùng trọng số, $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, vì bất đẳng thức đúng trên từng mẫu (Mệnh đề 10.41(a)). Giữa $\Delta\mathcal L$ và $\Delta J$ không có thứ tự tổng quát: với $\pi'$ của Ví dụ 10.11, $\Delta\mathcal L=0{,}26<\Delta J=0{,}296$, còn với $\tilde\pi$, $\Delta\mathcal L=0{,}095>\Delta J=-0{,}085$. Với $\tilde\pi=(0{,}9;\,0{,}5)$, $\epsilon=0{,}2$ và tần suất hành động của $\pi_{\mathrm{old}}$ tại mỗi trạng thái, $\rho_{s_A}=(1{,}8;\,0{,}2)$, nên phần của mục tiêu cắt tại $s_A$ là
$$\begin{aligned}\ell_{s_A}&=\tfrac12\min(0{,}72;\,0{,}48)\\&\quad+\tfrac12\min(-0{,}08;\,-0{,}32)\\&=0{,}24-0{,}16=0{,}08.\end{aligned}$$
Tại $s_B$, $\rho_{s_B}=(0{,}75;\,1{,}5)$, cả hai mẫu đổi theo hướng bất lợi nên không bị cắt, và $\ell_{s_B}=A_\pi(s_B,\tilde\pi)=-0{,}5$. Với lợi thế đúng, tổng không cắt $\sum_s\eta_\pi(s)A_\pi(s,\tilde\pi)$ chính là $\Delta\mathcal L$. Phiên bản cắt trên cùng trọng số $\eta_\pi=(1;\,0{,}45)$ là $\sum_s\eta_\pi(s)\ell_s=0{,}08+0{,}45\cdot(-0{,}5)=-0{,}145$, nhỏ hơn cả $\Delta\mathcal L=0{,}095$ và $\Delta J=-0{,}085$. Trung bình đều trên bộ đệm cũng khác trọng số chiếm dụng có chiết khấu: trên chuỗi, mỗi lượt thăm $s_A$ một lần và $s_B$ trung bình $0{,}5$ lần, nên tỉ lệ trọng số $s_B/s_A$ trên bộ đệm là $0{,}5$, còn trong $\eta_{\pi_{\mathrm{old}}}=(1;\,0{,}45)$ là $0{,}45$. Với tần suất trạng thái $(\tfrac23;\,\tfrac13)$ của bộ đệm, trung bình đều tại $\tilde\pi$ cho $\mathcal L^{\mathrm{CPI}}=\tfrac23\cdot0{,}32+\tfrac13\cdot(-0{,}5)\approx0{,}047$ và $\mathcal L^{\mathrm{CLIP}}=\tfrac23\cdot0{,}08+\tfrac13\cdot(-0{,}5)\approx-0{,}113$, khác hai tổng theo $\eta_\pi$.

<!-- note-topic-id: lec-10-topic-18 -->
### 6.2 PPO-Penalty

Một cách khác để giữ chính sách mới gần chính sách cũ là phạt trực tiếp KL trong hàm mục tiêu, gần với hàm $\mathcal M_k$ của Hệ quả 10.30 hơn là với bài toán có ràng buộc. Khó khăn là chọn hệ số phạt: theo Schulman và cộng sự (2017, §2.2), một hệ số $\beta$ cố định khó cho kết quả tốt trên nhiều bài toán, hoặc ngay trong một bài toán khi đặc điểm của nó đổi trong quá trình học. Vì vậy bài báo (§4) điều chỉnh hệ số sau mỗi lần cập nhật, gọi là *hệ số phạt thích nghi* (adaptive KL penalty coefficient).

Về mặt ý tưởng, phạt KL biến khoảng cách giữa hai chính sách thành một chi phí: bước nào làm KL tăng nhiều thì phải đem lại mức tăng tương ứng của hàm thay thế mẫu. Ví dụ sau thực hiện một lần điều chỉnh hệ số phạt.

::: example Ví dụ 10.20 (Một lần điều chỉnh hệ số phạt trên bài toán một bước)
**Dữ kiện.** Bài toán một bước và bộ đệm của Ví dụ 10.18: chính sách cũ $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$; ba mẫu, hành động $1,1,2$, lợi thế $\widehat A=(1;\,1;\,-2)$; $p$ là xác suất chọn hành động 1 của chính sách mới. Hệ số phạt hiện tại $\beta=1$, KL đích $\kappa_{\mathrm{targ}}=0{,}01$. Quy tắc của Schulman và cộng sự (2017, §4): sau một lần cập nhật, gọi $\widehat D$ là KL trung bình trên bộ đệm theo chiều cũ‖mới; nếu $\widehat D<\kappa_{\mathrm{targ}}/1{,}5=0{,}00667$ thì $\beta\leftarrow\beta/2$, nếu $\widehat D>1{,}5\,\kappa_{\mathrm{targ}}=0{,}015$ thì $\beta\leftarrow2\beta$. Xét hai kết quả của lần cập nhật: (i) $p=0{,}75$; (ii) $p=0{,}7$.

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

Với $\beta$ cố định, $\mathcal L^{\mathrm{KLPEN}}$ có cùng dạng với hàm phạt $D^{\max}_{\mathrm{KL}}$ trong Thuật toán 1 của Schulman và cộng sự (2015), với KL trung bình mẫu thay cho KL lớn nhất và $\beta$ thay cho hằng $4\bar\chi\gamma/(1-\gamma)^2$; quy tắc điều chỉnh đưa KL đo được về gần $\kappa_{\mathrm{targ}}$, nên $\kappa_{\mathrm{targ}}$ đóng vai bán kính $\kappa$ của TRPO.

::: remark Nhận xét 10.44 (Phạm vi của PPO-Penalty)
1. PPO-Penalty không có bảo đảm $J$ tăng sau một lần cập nhật: $\beta$ không phải hằng của Hệ quả 10.30, và mục tiêu là trung bình mẫu với lợi thế ước lượng, nên các giả thiết của hệ quả đó không thỏa. Schulman và cộng sự (2017, §4) ghi rằng các hằng $1{,}5$ và $2$ được chọn theo kinh nghiệm, và thuật toán không nhạy với chúng; KL sau một lần cập nhật đôi khi khác xa $\kappa_{\mathrm{targ}}$, và $\beta$ điều chỉnh lại nhanh.
2. Trong thí nghiệm MuJoCo của bài báo (Bảng 1), cấu hình cắt với $\epsilon=0{,}2$ cho điểm chuẩn hóa trung bình cao nhất trong các cấu hình được thử, kể cả các cấu hình phạt KL cố định và thích nghi; bài báo ghi rằng phạt KL cho kết quả kém hơn mục tiêu cắt trong các thí nghiệm của họ và giữ nó như một phương pháp đối chứng.
:::

**Trong thực hành.** PPO-Penalty tối ưu $\mathcal L^{\mathrm{KLPEN}}$ bằng vài epoch Adam trên mini-batch của cùng một bộ đệm, như vòng lặp PPO đầy đủ ở Thuật toán 10.49, rồi tính $\widehat D$ trên bộ đệm để cập nhật $\beta$. KL tại mỗi $S_t$ tính dạng đóng từ hai phân phối hành động, nên bộ đệm lưu phân phối của $\pi_{\mathrm{old}}$ trên mọi hành động, không chỉ log-xác suất của $A_t$.

<!-- note-topic-id: lec-10-topic-19 -->
### 6.3 Hàm mất mát tổng và thuật toán PPO

Thuật toán PPO huấn luyện chính sách và critic cùng lúc; khi hai mạng dùng chung tham số, Schulman và cộng sự (2017, §5) gộp hai mục tiêu vào một hàm mất mát duy nhất. Hàm đó có thêm một số hạng khuyến khích chính sách giữ ngẫu nhiên, đo bằng *entropy*. Về mặt ý tưởng, ba số hạng của hàm mất mát ứng với ba việc trên cùng bộ đệm:

- tăng mục tiêu cắt của actor;
- hồi quy critic về lợi tức λ cắt, như Mục 3.3, qua *mất mát giá trị* (value loss);
- giữ chính sách đủ ngẫu nhiên để còn thăm dò, qua số hạng *thưởng entropy* (entropy bonus).

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

Từ đây, $\widehat A^{\mathrm{raw}}_t$ là đầu ra $\widehat A_t$ của Thuật toán 10.16, còn $\widehat A_t$ chỉ lợi thế đưa vào $\mathcal L^{\mathrm{CLIP}}$, đã chuẩn hóa hoặc không. Hàm $L$ là (9) của Schulman và cộng sự (2017), đổi dấu để cực tiểu hóa. Biến thể cắt mất mát giá trị (Engstrom và cộng sự, 2020, §3) dùng chính $\epsilon$ của tỉ số.

*Chuẩn hóa lợi thế* (advantage normalization) là một lựa chọn cài đặt: trừ trung bình là trừ một đường cơ sở hằng của mini-batch, chia độ lệch chuẩn là đổi thang của bước. Vì trung bình và độ lệch chuẩn được tính từ chính mini-batch, hệ số của mỗi mẫu phụ thuộc cả hành động của mẫu đó, nên điều kiện "đường cơ sở không phụ thuộc hành động" của Mệnh đề 10.2 không thỏa.

::: example Ví dụ 10.21 (Một mini-batch tính tay)
**Dữ kiện.** Bài toán một bước, $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\hat v_{\mathrm{old}}(s)=2$. Mini-batch ba mẫu: hành động $1,1,2$, phần thưởng $3,3,0$, $\widehat A^{\mathrm{raw}}=(1;\,1;\,-2)$, $V^{\mathrm{targ}}=(3;\,3;\,0)$. Tham số hiện tại cho $p=\pi_\theta(1\mid s)=0{,}75$ và $\hat v(s,w)=2{,}2$. Hệ số $\epsilon=0{,}2$, $c_1=1$, $c_2=0{,}01$ (Schulman và cộng sự, 2017, Bảng 5). Không chuẩn hóa lợi thế.

**Tỉ số và mục tiêu cắt.** $\rho=(1{,}5\cdot0{,}75;\,1{,}5\cdot0{,}75;\,3\cdot0{,}25)=(1{,}125;\,1{,}125;\,0{,}75)$. Hai mẫu đầu có lợi thế dương và $\rho<1{,}2$, nên $\ell=1{,}125$; mẫu thứ ba có lợi thế âm và $\rho<0{,}8$, nên bị cắt: $\ell=-2\cdot0{,}8=-1{,}6$. Do đó $\mathcal L^{\mathrm{CLIP}}=(1{,}125+1{,}125-1{,}6)/3=0{,}2167$.

**Gradient của actor.** Theo logit $(\theta_1;\,\theta_2)$, $\mathcal L^{\mathrm{CLIP}}=p-0{,}5\overline3$ trên khúc này (Ví dụ 10.18), nên gradient là $p(1-p)(1;\,-1)=(0{,}1875;\,-0{,}1875)$; mẫu thứ ba không đóng góp. Gradient của $\mathcal L^{\mathrm{CPI}}=3p-2$ là $(0{,}5625;\,-0{,}5625)$.

**Mất mát giá trị, entropy, mất mát tổng.** $L^V=\bigl((2{,}2-3)^2+(2{,}2-3)^2+(2{,}2-0)^2\bigr)/3=(0{,}64+0{,}64+4{,}84)/3=2{,}04$; $\mathcal H(0{,}75;\,0{,}25)=0{,}5623$; và
$$\begin{aligned}&L=-0{,}2167+1\cdot2{,}04\\&\quad-0{,}01\cdot0{,}5623\\&\quad=1{,}8177.\end{aligned}$$

**Hai ước lượng KL.** Từng mẫu, $-\log\rho=(-0{,}1178;\,-0{,}1178;\,0{,}2877)$, hai số đầu âm, còn $(\rho-1)-\log\rho=(0{,}0072;\,0{,}0072;\,0{,}0377)$, mọi số không âm. Trung bình của dạng thứ hai là $0{,}01737$; tỉ lệ mẫu có $\lvert\rho-1\rvert>0{,}2$ là $1/3$.

**Chuẩn hóa.** Nếu chuẩn hóa lợi thế với độ lệch chuẩn tổng thể $\sqrt2$ của $(1;\,1;\,-2)$, ta được $\widehat A=(0{,}7071;\,0{,}7071;\,-1{,}4142)$; dấu không đổi, nên tập mẫu bị cắt không đổi.

**Kiểm tra lại.** $\partial(3p-2)/\partial\theta_1=3p(1-p)=0{,}5625$ và $\partial(p-0{,}5\overline3)/\partial\theta_1=p(1-p)=0{,}1875$.
:::

Hai ước lượng KL và tỉ lệ cắt ở cuối Ví dụ 10.21 là các đại lượng mà cài đặt PPO ghi lại sau mỗi mini-batch. Định nghĩa sau cho công thức.

::: definition Định nghĩa 10.47 (Đại lượng chẩn đoán)
Trên mini-batch với tập chỉ số $\mathcal B$ và tỉ số $\rho_i=\rho_i(\theta)$:

- *approxKL* (approximate KL; Huang và cộng sự, 2022) là $\dfrac1{\lvert\mathcal B\rvert}\sum_{i\in\mathcal B}\bigl[(\rho_i-1)-\log\rho_i\bigr]$; dạng $\dfrac1{\lvert\mathcal B\rvert}\sum_i(-\log\rho_i)$ cũng được dùng;
- *tỉ lệ cắt* (clip fraction) là $\dfrac1{\lvert\mathcal B\rvert}\,\#\{i\in\mathcal B:\lvert\rho_i-1\rvert>\epsilon\}$;
- *tỉ lệ cắt có tác dụng* (active clipping fraction) là $\dfrac{n_++n_-}{\lvert\mathcal B\rvert}$, với $n_+=\#\{i:\widehat A_i>0,\ \rho_i>1+\epsilon\}$ và $n_-=\#\{i:\widehat A_i<0,\ \rho_i<1-\epsilon\}$;
- entropy trung bình là $\dfrac1{\lvert\mathcal B\rvert}\sum_{i\in\mathcal B}\mathcal H\bigl(\pi_\theta(\cdot\mid S_i)\bigr)$;
- mất mát giá trị là $L^V(w)$ của Định nghĩa 10.46, lấy trung bình trên $\mathcal B$.

Trên cả bộ đệm, với mục tiêu $y_t=V^{\mathrm{targ}}_t$ và dự đoán $\hat y_t=\hat v_{\mathrm{old}}(S_t)$, *phương sai được giải thích* (explained variance) là $1-\operatorname{Var}(y-\hat y)/\operatorname{Var}(y)$, với phương sai mẫu trên bộ đệm.
:::

Tỉ lệ cắt đếm mẫu có tỉ số ngoài khoảng, bất kể dấu của lợi thế. Tỉ lệ cắt có tác dụng chỉ đếm mẫu trên đoạn phẳng, tức tập có gradient bằng $0$ của Mệnh đề 10.40(d), nên không vượt tỉ lệ cắt. Một mẫu ra ngoài khoảng theo hướng bất lợi được tính vào tỉ lệ cắt nhưng vẫn giữ gradient. Phương sai được giải thích bằng $1$ khi critic dự đoán đúng mọi mục tiêu, bằng $0$ khi critic dự đoán một hằng, và âm khi phần dư biến thiên nhiều hơn chính mục tiêu.

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

**Bước 3 (kết luận b).** Với $x=\rho>0$, Bước 1 của chứng minh Mệnh đề 10.25 cho $x-1-\log x\ge0$, dấu bằng khi và chỉ khi $x=1$. $\square$
:::

Dạng $(\rho-1)-\log\rho$ không âm trên từng mẫu, nên trung bình của nó cũng không âm; trung bình của dạng $-\log\rho$ có thể âm. Trên Ví dụ 10.21, tần suất mẫu trùng $\pi_{\mathrm{old}}$, nên cả hai trung bình bằng đúng KL thật tại $p=0{,}75$, là $0{,}01737$. Ba giả thiết có vai trò riêng.

- Bỏ (ii): với $\pi_{\mathrm{old}}(\cdot\mid s)=(1;\,0)$ và $\pi_\theta(\cdot\mid s)=(0{,}9;\,0{,}1)$, mọi mẫu là hành động 1 và $\rho=0{,}9$, nên $\mathbb E[\rho]=0{,}9<1$ và $\mathbb E[(\rho-1)-\log\rho]=-0{,}1+0{,}10536=0{,}00536$, nhỏ hơn KL thật $0{,}10536$: dạng $(\rho-1)-\log\rho$ chệch xuống.
- Bỏ (i): có mẫu với $\rho=0$, $\log\rho$ không xác định, và KL bằng $+\infty$.
- Bỏ "$\theta$ không phụ thuộc mẫu": với ba hành động và $\pi_{\mathrm{old}}$ đều, nếu sau khi thấy $A=a$ ta chọn $\pi_\theta$ gán $\tfrac13$ cho $a$, $\tfrac12$ và $\tfrac16$ cho hai hành động còn lại, thì $\rho=1$ ở mọi mẫu và approxKL bằng $0$, trong khi KL thật bằng $\tfrac13\bigl(\log\tfrac23+\log2\bigr)=0{,}0959$.

![Sơ đồ dữ liệu của một vòng PPO. Bên trái, N môi trường xếp chồng, mỗi môi trường chạy h bước bằng pi old, tạo lưới h nhân N mẫu. Mũi tên sang bộ đệm D gồm hN mẫu, mỗi mẫu lưu S t, A t, R t+1, Z t+1, U t+1, log pi old, v mũ old. Mũi tên sang khung GAE tính A mũ raw và V targ. Mũi tên sang vòng lặp K epoch: xáo D, chia mini-batch cỡ M, mỗi mini-batch một bước Adam trên L. Mũi tên cong quay về bên trái ghi theta old gán bằng theta.](img/lec-10/ppo-data-pipeline.svg)

Trên hình, dữ liệu đi từ trái sang phải: thu một lần bằng $\pi_{\mathrm{old}}$ trên $N$ môi trường, tính GAE một lần, rồi dùng lại trong $K$ epoch; mỗi epoch đi qua $\lceil hN/M\rceil$ mini-batch. Mũi tên quay về chỉ được đi sau khi hết $K$ epoch.

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
| $\mathcal D$, $\log\pi_{\mathrm{old}}(A_t\mid S_t)$, $\widehat A^{\mathrm{raw}}_t$, $V^{\mathrm{targ}}_t$, $\hat v_{\mathrm{old}}(S_t)$ | $\log\pi_\theta(A_t\mid S_t)$, $\rho_t(\theta)$, $\hat v(S_t,w)$, $\mathcal H(\pi_\theta(\cdot\mid S_t))$, $L(\theta,w)$ và gradient của nó |

Thuật toán 10.49 là Thuật toán 1 của Schulman và cộng sự (2017) với các bước của bài giảng gốc (tr. 24–25) và các cờ của Mục 3.3. Cột trái của bảng tính một lần từ dữ liệu của $\pi_{\mathrm{old}}$; cột phải phụ thuộc tham số hiện tại.

Từ mini-batch thứ hai, $\theta\ne\theta_{\mathrm{old}}$, nên dữ liệu đã là dữ liệu khác chính sách. Tỉ số $\rho_t$ hiệu chỉnh phân phối hành động tại mỗi trạng thái, còn phân bố trạng thái vẫn là của $\pi_{\mathrm{old}}$, như trong hàm thay thế của Mục 4.2. PPO dùng lại bộ đệm vừa thu trong $K$ epoch, rồi bỏ nó và thu bộ đệm mới bằng chính sách vừa cập nhật; mọi tỉ số lấy mẫu số là $\pi_{\mathrm{old}}$, chính sách duy nhất đã sinh bộ đệm. Cách dùng dữ liệu này khác với học khác chính sách trên bộ nhớ phát lại, như ở DQN, nơi bộ đệm lịch sử trộn dữ liệu của nhiều chính sách cũ.

Với hành động nhiều chiều có các thành phần độc lập, log-xác suất của hành động là tổng log-xác suất các thành phần, cộng trước khi lập tỉ số. Ví dụ 10.21 là một mini-batch của bước 3.

**Trong thực hành.** Thuật toán 10.49 giải quyết giới hạn thứ hai của Mục 1 theo cách sau: mỗi lần thu $hN$ bước cho $K\lceil hN/M\rceil$ bước gradient thay vì một. Bảo đảm còn lại chỉ ở mức Mệnh đề 10.41: mục tiêu cắt không tạo động lực đẩy tỉ số ra ngoài khoảng. Lợi thế từ GAE với critic học được không có bảo đảm γ-just (Mệnh đề 10.15; Ví dụ 10.9 cho một trường hợp chệch), và Adam, mini-batch, chuẩn hóa lợi thế không có trong các kết quả của Mục 4.

<!-- note-topic-id: lec-10-topic-20 -->
### 6.4 Đọc chẩn đoán và chọn siêu tham số

Sau mỗi vòng PPO, các kết quả của Mục 4–6 không bảo đảm bước vừa chạy đủ nhỏ và critic đã học được, vì Mệnh đề 10.41 không chặn KL và lợi thế chỉ là ước lượng. Về mặt ý tưởng, mỗi đại lượng chẩn đoán của Định nghĩa 10.47 trả lời một câu hỏi về vòng cập nhật vừa chạy (bài giảng gốc, tr. 27).

| Đại lượng | Ý nghĩa | Tín hiệu cần chú ý |
|---|---|---|
| approxKL | mức thay đổi của chính sách trong vòng cập nhật | cao so với ngưỡng mục tiêu; có thể dừng sớm các epoch còn lại |
| tỉ lệ cắt | tỉ lệ mẫu có tỉ số ngoài khoảng cắt | lớn và kéo dài qua nhiều vòng: nhiều mẫu chịu tác động của phép cắt |
| tỉ lệ cắt có tác dụng | tỉ lệ mẫu trên đoạn phẳng, có gradient riêng bằng $0$ | lớn: phần lớn mini-batch không còn đóng góp gradient cho actor |
| entropy | mức ngẫu nhiên của chính sách | giảm quá nhanh: thăm dò bị thu hẹp |
| phương sai được giải thích | mức critic dự đoán được lợi tức | thấp hoặc âm |
| mất mát giá trị | sai số bình phương của critic so với $V^{\mathrm{targ}}$ | lớn so với số hạng của actor khi hai mạng dùng chung tham số |

Giả sử một mini-batch bốn mẫu có $\rho=(1{,}05;\,1{,}18;\,1{,}24;\,0{,}70)$, dấu lợi thế $(+;\,-;\,+;\,+)$ và $\epsilon=0{,}2$. Hai mẫu $1{,}24$ và $0{,}70$ nằm ngoài $[0{,}8;\,1{,}2]$, nên tỉ lệ cắt là $2/4=50\%$. Chỉ mẫu thứ ba nằm trên đoạn phẳng, vì lợi thế dương và $\rho=1{,}24>1{,}2$. Mẫu thứ tư có lợi thế dương và $\rho=0{,}70<0{,}8$, một thay đổi bất lợi, nên vẫn giữ gradient. Tỉ lệ cắt có tác dụng là $1/4=25\%$. Các số hạng $(\rho-1)-\log\rho$ là $(0{,}0012;\,0{,}0145;\,0{,}0249;\,0{,}0567)$, nên approxKL, trung bình của bốn số hạng, xấp xỉ $0{,}0243$. Nếu bốn mẫu này vừa được dùng để cập nhật $\theta$, giả thiết "$\theta$ không phụ thuộc mẫu" của Mệnh đề 10.48 không thỏa, nên $0{,}0243$ là một giá trị chẩn đoán không có bảo đảm không chệch.

Một dấu hiệu bất ổn thường gặp gồm phần thưởng tăng trong thời gian ngắn, KL tăng vọt, entropy sụp và chính sách ngừng thăm dò. Ví dụ sau tiếp tục Ví dụ 10.21 sau vài mini-batch.

::: example Ví dụ 10.22 (Chẩn đoán trên đoạn phẳng)
**Dữ kiện.** Như Ví dụ 10.21: bài toán một bước, $\pi_{\mathrm{old}}(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, mini-batch hành động $1,1,2$, $\widehat A=(1;\,1;\,-2)$, $\epsilon=0{,}2$, $V^{\mathrm{targ}}=(3;\,3;\,0)$. Sau vài mini-batch, $p=0{,}85$.

**Tỉ số và gradient.** $\rho=(1{,}275;\,1{,}275;\,0{,}45)$. Hai mẫu đầu có lợi thế dương và $\rho>1{,}2$, mẫu thứ ba có lợi thế âm và $\rho<0{,}8$: mọi mẫu nằm trên đoạn phẳng, gradient của $\mathcal L^{\mathrm{CLIP}}$ bằng $0$, và $\mathcal L^{\mathrm{CLIP}}=0{,}2\overline6$ như Ví dụ 10.18.

**Chẩn đoán.** Tỉ lệ cắt là $3/3$; approxKL là $0{,}1042$, bằng KL thật tại $p=0{,}85$. Với mini-batch chỉ có một mẫu hành động 1: $-\log\rho=-\log1{,}275=-0{,}2430<0$, trong khi $(\rho-1)-\log\rho=0{,}0321\ge0$.

**Phương sai được giải thích.** Với critic đúng $\hat v_{\mathrm{old}}=2$: $y=(3;\,3;\,0)$ có $\operatorname{Var}(y)=2$, $y-\hat y=(1;\,1;\,-2)$ có phương sai $2$, nên phương sai được giải thích bằng $0$.

**Diễn giải.** KL $0{,}1042$ lớn gấp sáu lần KL $0{,}01737$ của Ví dụ 10.21, dù mục tiêu cắt đã phẳng từ $p=0{,}8$: tham số vẫn đi vào đoạn phẳng, chẳng hạn nhờ quán tính của Adam hoặc các mini-batch khác (Nhận xét 10.42). Phương sai được giải thích bằng $0$ với một critic đúng, vì chỉ có một trạng thái và mọi biến thiên của mục tiêu đến từ hành động; giá trị thấp không có nghĩa critic sai.

**Kiểm tra lại.** $\tfrac23\log\frac{2/3}{0{,}85}+\tfrac13\log\frac{1/3}{0{,}15}=0{,}1042$; $0{,}275-0{,}2430=0{,}0321$.
:::

Các giá trị trong bảng sau lấy từ bài báo PPO, cộng hai chi tiết từ Huang và cộng sự (2022).

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
| Cắt chuẩn gradient (gradient norm clipping); hằng ổn định số của Adam | $0{,}5$; $10^{-5}$ (Huang và cộng sự, 2022) | $0{,}5$; $10^{-5}$ (Huang và cộng sự, 2022) |

Bảng sau so TRPO và PPO theo điều mỗi phương pháp bảo đảm.

| Tiêu chí | TRPO (Thuật toán 10.37) | PPO (Thuật toán 10.49) |
|---|---|---|
| Cách giữ gần chính sách cũ | ràng buộc KL trung bình mẫu $\le\kappa$ | cắt tỉ số trong mục tiêu (hoặc phạt KL) |
| Chi phí mỗi vòng lặp | $k_{\max}$ tích Fisher–vector, tìm kiếm lùi | $K\lceil hN/M\rceil$ bước gradient |
| Điều được bảo đảm trên bộ đệm | KL trung bình mẫu $\le\kappa$, hàm thay thế mẫu tăng | không có cận KL |
| Giả thiết lý thuyết còn thiếu | lợi thế, $\nu^{\mathrm{old}}$, nghiệm chính xác (Nhận xét 10.38) | như TRPO, thêm cắt thay ràng buộc (Nhận xét 10.42) |

<!-- note-topic-id: lec-10-topic-21 -->
### 6.5 Chi tiết cài đặt

Engstrom và cộng sự (2020) đặt câu hỏi mà bài giảng gốc (tr. 29) nhắc lại: mức cải thiện của PPO so với TRPO đến từ mục tiêu cắt, hay từ các chi tiết ở mức mã không có trong mô tả thuật toán. Một ví dụ nhỏ cho thấy một chi tiết như vậy đổi hành vi của critic.

::: example Ví dụ 10.23 (Cắt mất mát giá trị trên một mẫu)
**Dữ kiện.** Biến thể cắt mất mát giá trị của Định nghĩa 10.46 với $\hat v_{\mathrm{old}}(s)=2$, $\epsilon=0{,}2$, critic hiện tại $\hat v(s,w)=2{,}5$; khoảng cắt là $[1{,}8;\,2{,}2]$, nên $\operatorname{clip}(2{,}5;\,1{,}8;\,2{,}2)=2{,}2$.

**Mẫu (i), $V^{\mathrm{targ}}=3$.** Không cắt: $(2{,}5-3)^2=0{,}25$; cắt: $(2{,}2-3)^2=0{,}64$. Giá trị lớn hơn là $0{,}64$, từ nhánh cắt, không phụ thuộc $\hat v$, nên gradient theo $\hat v$ bằng $0$: critic không được kéo tiếp về $3$.

**Mẫu (ii), $V^{\mathrm{targ}}=0$.** Không cắt: $6{,}25$; cắt: $4{,}84$. Giá trị lớn hơn là nhánh không cắt, gradient theo $\hat v$ là $2\cdot(2{,}5-0)=5$.

**Diễn giải.** Ở mẫu (i), critic đã vượt khỏi khoảng cắt theo hướng của mục tiêu và bị dừng, vì $3$ gần $2{,}5$ hơn $2{,}2$; ở mẫu (ii), critic đi sai hướng và vẫn nhận gradient. Với phép cắt, critic cực tiểu hóa $\max$ của hai bình phương, khác $L^V$.

**Kiểm tra lại.** $\max(0{,}25;\,0{,}64)=0{,}64$ và $\max(6{,}25;\,4{,}84)=6{,}25$.
:::

::: remark Nhận xét 10.50 (Chi tiết cài đặt và kết quả loại bỏ)
Bảng sau đối chiếu danh sách kiểm của bài giảng gốc (tr. 36) với 13 chi tiết cốt lõi của Huang và cộng sự (2022) và 9 tối ưu mức mã của Engstrom và cộng sự (2020, §3), theo thành phần mà mỗi chi tiết thay đổi.

| Chi tiết | Thành phần bị thay đổi |
|---|---|
| Môi trường vector hóa (vectorized environments), $N$ môi trường song song | dữ liệu |
| Chuẩn hóa và cắt quan sát | dữ liệu (đầu vào của mạng) |
| Chuẩn hóa phần thưởng theo độ lệch chuẩn của lợi tức chiết khấu chạy; cắt phần thưởng | mục tiêu (hàm phần thưởng thực sự được tối ưu) |
| Chuẩn hóa lợi thế theo mini-batch | mục tiêu của actor (thang và đường cơ sở) |
| Cắt mất mát giá trị | mục tiêu của critic |
| Hệ số entropy $c_2$ | mục tiêu của actor |
| Khởi tạo trực giao (orthogonal initialization), nhân hệ số theo lớp; hàm kích hoạt tanh | bộ tối ưu (điểm xuất phát) và mạng |
| Ủ bước học (learning rate annealing); hằng ổn định số $10^{-5}$ của Adam | bộ tối ưu |
| Cắt chuẩn gradient toàn cục ở $0{,}5$ | bộ tối ưu |
| Xáo bộ đệm, $K$ epoch, cỡ mini-batch $M$ | bộ tối ưu và cách dùng lại dữ liệu |
| Dừng sớm theo approxKL | bộ tối ưu |
| Mạng chung hay tách cho chính sách và critic | mạng và mục tiêu (qua $c_1$) |

Engstrom và cộng sự (2020, §5–6) rút ra ba kết luận định tính từ thí nghiệm loại bỏ (ablation study) của họ:

- các tối ưu mức mã giải thích phần lớn mức cải thiện phần thưởng của PPO so với TRPO trong thí nghiệm của họ;
- PPO bỏ phép cắt nhưng giữ các tối ưu mức mã, khi siêu tham số được tinh chỉnh đủ, thường đạt mức của PPO chuẩn;
- các tối ưu mức mã quyết định tính chất miền tin cậy mà thuật toán thực sự giữ được (§4).

Chuẩn hóa và cắt phần thưởng làm thuật toán tối ưu một hàm mục tiêu khác $J$ của MDP ban đầu, vì phần thưởng bị chia cho một đại lượng đổi theo thời gian. Vì vậy, một báo cáo kết quả của PPO cần ghi đủ các chi tiết cài đặt trong bảng trên (bài giảng gốc, tr. 36).
:::

<!-- note-topic-id: lec-10-topic-22 -->
### 6.6 Đọc thêm: hội tụ về điểm dừng của PPO-Clip

Bài giảng gốc (tr. 37) nêu bốn khó khăn khi phân tích PPO-Clip:

- mục tiêu chứa tỉ số của hai chính sách ngẫu nhiên;
- phép cắt không trơn;
- hàm điểm có thể không bị chặn;
- thuật toán xen kẽ việc đồng bộ $\pi_{\mathrm{old}}$ với các bước tối ưu bên trong.

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

Chứng minh nằm ngoài phạm vi học phần. Ý tưởng: Bổ đề 3.1 của bài báo lập một bất đẳng thức đệ quy cho $V^*-V(\theta_{n,1})$, tương tự phân tích của phương pháp gradient ngẫu nhiên, trong đó các bước trong vòng được tách thành phần gradient đúng, phần sai số do cắt và do độ chệch $\varphi_n$, và một hiệu martingale.
:::

Khi $\varphi_n>0$, Định lý 3.1 chỉ nói về lim inf, tức có một dãy con với $\lVert\nabla V\rVert^2$ tiến vào khoảng $[0,\,C\sqrt{\lvert\mathcal A\rvert}\limsup\varphi_n]$. Bài báo không khẳng định dãy tham số hội tụ, và (§4) ghi rằng chưa biết có suy ra được tính tối ưu dưới các điều kiện này hay không.

Mô hình được phân tích khác PPO của Thuật toán 10.49 ở nhiều điểm: GAE với critic học được cho $\varphi_n>0$; Adam, xáo mini-batch và chuẩn hóa lợi thế nằm ngoài mô hình; bài báo viết mục tiêu dạng $\min\{\rho,\operatorname{clip}(\rho)\}\,\tilde A$ và coi gradient bằng $0$ ngoài khoảng cắt ở cả hai phía, khác dạng theo dấu của Mệnh đề 10.40.

Cái giá của PPO là không còn cận KL (Nhận xét 10.42), hành vi thực tế phụ thuộc chi tiết cài đặt (Nhận xét 10.50), và kết quả hội tụ hiện có chỉ nói về điểm dừng của một mô hình đơn giản hóa (Nhận xét 10.51).

---

## 7. Tổng kết

Mỗi kết quả của Mục 2–6 đúng dưới một bộ giả thiết riêng.

<!-- note-topic-id: lec-10-topic-23 -->
### 7.1 Kết quả và giả thiết của bài

Bảng sau đặt mỗi kết quả chính cạnh giả thiết mà thiếu nó thì công thức sai nghĩa hoặc kết luận vượt quá điều đã chứng minh.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Đường cơ sở không làm chệch (Mệnh đề 10.2) | $b$ không phụ thuộc $A_t$ khi biết $H_t$; lượt sinh bởi $\pi_\theta$; (G1)–(G4) | $\mathbb E\bigl[\sum_t\gamma^t(G_t-b(S_t))\psi_t\bigr]=\nabla J$ |
| Đường cơ sở tối ưu (Mệnh đề 10.3) | một bước, $b$ hằng, $\mathbb E\lVert\psi\rVert^2>0$ | $b^*=\mathbb E[R\lVert\psi\rVert^2]/\mathbb E\lVert\psi\rVert^2$ |
| Gradient dạng lợi thế (Mệnh đề 10.5(b); dạng quỹ đạo là hệ quả của Mệnh đề 10.2) | lợi thế và $\nu^\pi$ của chính $\pi_\theta$ | $\nabla J=\frac1{1-\gamma}\mathbb E_{\nu^\pi,\pi_\theta}[A_\pi\psi]$ |
| Sai số TD và lợi thế (Mệnh đề 10.8) | critic cố định; mặt nạ chỉ ở kết thúc; điều kiện theo $(S_t,A_t)$ | $\mathbb E[\delta_t\mid S_t,A_t]=A_\pi+\gamma\mathbb E[(1-Z_{t+1})e(S_{t+1})\mid S_t,A_t]-e(S_t)$ |
| Dạng tổng của GAE (Mệnh đề 10.14) | critic cố định trong lượt | $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$ |
| GAE và gradient (Mệnh đề 10.15) | $\lambda=1$ với lượt đầy đủ, hoặc $\hat v=v_\pi$ | $\mathbb E[\widehat A_t\psi_t]=\mathbb E[A_\pi\psi_t]$; không chệch cho lợi thế thì không |
| Chênh lệch hiệu năng (Bổ đề 10.19) | cùng $P$, cùng $\mu_0$; $\gamma<1$ | $J(\pi')-J(\pi)=\frac1{1-\gamma}\sum_s\nu^{\pi'}(s)A_\pi(s,\pi')=\sum_s\eta_{\pi'}(s)A_\pi(s,\pi')$ |
| Khớp bậc một (Mệnh đề 10.22) | $\nu^{\mathrm{old}}$, $A_{\mathrm{old}}$ chính xác; $\pi_{\mathrm{old}}>0$ | $\mathcal L=J$ và $\nabla\mathcal L=\nabla J$ tại $\theta_{\mathrm{old}}$ |
| Chặn cải thiện (Định lý 10.27, Hệ quả 10.28) | như Bổ đề 10.19; $\gamma<1$ | $J'-J\ge[\mathcal L-J]-\frac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\mathbb E_\nu[D_{\mathrm{TV}}]$, hoặc $\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$ thay cho $\mathbb E_\nu[D_{\mathrm{TV}}]$ |
| Cải thiện đơn điệu (Hệ quả 10.30) | đánh giá và cực đại hóa chính xác | $J(\pi_{k+1})\ge\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)=J(\pi_k)$ |
| Bước miền tin cậy (Hệ quả 10.31) | nghiệm chính xác theo $\nu^{\pi_k}$ | $J_{k+1}-J_k\ge-\sqrt{2\kappa}\,\gamma\chi/(1-\gamma)^2$ |
| KL bậc hai (Mệnh đề 10.33) | $\nu^{\mathrm{old}}$ cố định; $\pi_\theta>0$, khả vi hai lần | $\bar D\approx\tfrac12\Delta^\top F\Delta$ |
| Gradient tự nhiên (Mệnh đề 10.34) | $g\in\operatorname{range}F$ | $\Delta^*=\sqrt{2\kappa/(g^\top F^+g)}\,F^+g$ |
| Mục tiêu cắt (Mệnh đề 10.40, 10.41) | lợi thế cố định; $\pi_{\mathrm{old}}>0$ | gradient $0$ trên $\{\widehat A>0,\rho>1+\epsilon\}\cup\{\widehat A<0,\rho<1-\epsilon\}$; $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, trùng quanh $\theta_{\mathrm{old}}$ |
| approxKL (Mệnh đề 10.48) | mẫu theo $\pi_{\mathrm{old}}$; $\theta$ không phụ thuộc mẫu; miền hỗ trợ của $\pi_\theta$ nằm trong miền hỗ trợ của $\pi_{\mathrm{old}}$, và $\pi_\theta>0$ trên miền hỗ trợ của $\pi_{\mathrm{old}}$ | $\mathbb E[(\rho-1)-\log\rho]=D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$, mỗi số hạng $\ge0$ |

Sáu hàng đầu thuộc phần giảm phương sai của bài toán trung tâm, chín hàng sau thuộc phần giới hạn bước cập nhật.

### 7.2 So sánh bốn phương pháp

| Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng |
|---|---|---|---|
| REINFORCE có đường cơ sở (Thuật toán 10.6) | $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_t\gamma^t(G_t-\hat v(S_t,w_{\mathrm{old}}))\psi_t$; hồi quy $\hat v$ về $G_t$ | một lượt đầy đủ của $\pi_{\mathrm{old}}$, dùng một lần | sau $E$ lượt |
| Actor–critic một bước (Thuật toán 10.9) | $\theta\leftarrow\theta+\alpha_\theta I\delta\psi$; $w\leftarrow w+\alpha_w\delta\nabla_w\hat v$ | từng bước chuyển của chính sách hiện tại, dùng một lần | sau $E$ lượt |
| TRPO (Thuật toán 10.37) | bước $\sqrt{2\kappa/(x^\top Fx)}\,x$ với $x\approx F^{-1}g$, tìm kiếm lùi | $hN$ mẫu của $\pi_{\mathrm{old}}$, một bước cập nhật | sau số vòng lặp đã định |
| PPO (Thuật toán 10.49) | bước Adam trên $L(\theta,w)$ của mỗi mini-batch | $hN$ mẫu của $\pi_{\mathrm{old}}$, $K$ epoch | sau số vòng lặp; tùy chọn dừng sớm theo approxKL |

Cả bốn điều kiện dừng trong bảng là ngân sách, không phải tiêu chuẩn hội tụ. Bảng sau ghi các kết luận có bảo đảm.

| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Lặp chính sách với $\mathcal M_k$ (Hệ quả 10.30) | lợi thế, $\nu^{\pi_k}$ và phép cực đại hóa chính xác | $J$ không giảm qua các vòng |
| Bài toán miền tin cậy (Hệ quả 10.31) | nghiệm chính xác theo $\nu^{\pi_k}$ | mức giảm của $J$ không quá $\sqrt{2\kappa}\gamma\chi/(1-\gamma)^2$ |
| PPO-Clip trong mô hình của Jin, Li và Wang (Nhận xét 10.51) | MDP hữu hạn; Giả thiết 3.1, 3.2, 3.4; mô hình hai thang không Adam, không mini-batch | $\liminf_n\lVert\nabla V(\theta_{n,1})\rVert^2\le C\sqrt{\lvert\mathcal A\rvert}\limsup_n\varphi_n$ hầu chắc chắn |

### 7.3 Trả lời bài toán trung tâm

Câu trả lời cho bài toán trung tâm gồm năm phần, mỗi phần đúng dưới một điều kiện.

1. Trừ một đường cơ sở không phụ thuộc hành động đã chọn giữ kỳ vọng và có thể giảm phương sai (Mệnh đề 10.2, 10.3); thay lợi tức bằng mục tiêu bootstrap của critic giảm số phần thưởng ngẫu nhiên trong ước lượng nhưng làm chệch khi critic sai (Định nghĩa 10.7, Mệnh đề 10.8).
2. GAE nối hai đầu bằng tham số $\lambda$, và chỉ bảo đảm gradient không chệch khi $\lambda=1$ với lượt đầy đủ hoặc khi critic đúng (Mệnh đề 10.14, 10.15).
3. Hàm thay thế đánh giá chính sách mới bằng dữ liệu cũ, đúng đến bậc một (Mệnh đề 10.22), với sai số bị chặn theo khoảng cách TV hoặc KL trung bình (Định lý 10.27, Hệ quả 10.28); bước miền tin cậy giải chính xác có mức giảm bị chặn (Hệ quả 10.31).
4. TRPO giải xấp xỉ bài toán miền tin cậy bằng gradient tự nhiên và gradient liên hợp, và chỉ bảo đảm KL trung bình mẫu không vượt $\kappa$ (Mệnh đề 10.34, Nhận xét 10.38).
5. PPO dùng lại dữ liệu từ chính sách cũ để thực hiện các bước cập nhật hiệu quả, đồng thời kiểm soát nguy cơ suy giảm hiệu năng: mỗi đoạn thu được dùng trong $K$ epoch với một mục tiêu cắt là chặn dưới của hàm thay thế mẫu (Mệnh đề 10.41), hoặc với phạt KL có hệ số thích nghi (Định nghĩa 10.43), không có cận KL; kết quả hội tụ hiện có chỉ nói về điểm dừng trong một mô hình đơn giản hóa (Nhận xét 10.51).

### 7.4 Câu hỏi tự kiểm tra

Trả lời các câu hỏi sau bằng phép tính trên các ví dụ của chương.

1. Trên chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$ và $\lambda=0{,}8$, hai lượt (i), (ii) của Ví dụ 10.8 cho hệ số GAE tại bước $0$ bằng bao nhiêu? Kỳ vọng của hệ số đó chệch bao nhiêu so với lợi thế đúng $0{,}4$?
2. Trên chuỗi hai trạng thái, với chính sách mới $p'_A=0{,}6$, $p'_B=0{,}7$, hàm thay thế dự báo mức tăng của $J$ thấp hơn hay cao hơn mức tăng thật, và sai số bằng bao nhiêu?
3. Trên bài toán một bước của Ví dụ 10.18, với bộ đệm ba mẫu và bán kính cắt $\epsilon=0{,}1$, mục tiêu cắt hết tăng từ $p$ nào?
4. Trên chuỗi hai trạng thái, bước tới $(0{,}5;\,1)$ chỉ đổi $p_B$. Vì sao hàm thay thế dự báo đúng mức tăng của $J$, dù bước xa chính sách cũ?

Lời giải ngắn.

1. Với $\gamma\lambda=0{,}72$: lượt (i) cho $-0{,}5+0{,}72\cdot2=0{,}94$, lượt (ii) cho $-0{,}5-0{,}72=-1{,}22$; kỳ vọng $\tfrac23\cdot0{,}94-\tfrac13\cdot1{,}22=0{,}22$, độ chệch $-0{,}18=-0{,}9(1-\lambda)$ (Ví dụ 10.8).
2. Thấp hơn. Với $\Delta p_A=0{,}1$, $\Delta p_B=\tfrac1{30}$, hàm thay thế cho $\mathcal L-J=0{,}08+0{,}045=0{,}125$, còn $\Delta J=0{,}125+2{,}7\cdot0{,}1\cdot\tfrac1{30}=0{,}134$, sai số $0{,}009$; vì $\Delta p_A$ và $\Delta p_B$ cùng dấu nên phần bậc hai $2{,}7\,\Delta p_A\Delta p_B$ dương (Ví dụ 10.12).
3. Mẫu hành động 2 chạm $\rho=0{,}9$ tại $p=0{,}7$, nhưng hai mẫu hành động 1 còn tăng tới $\rho=1{,}1$, tức $p=\tfrac23\cdot1{,}1\approx0{,}733$; từ đó mục tiêu cắt bằng hằng $\tfrac13(2\cdot1{,}1-2\cdot0{,}9)=0{,}1\overline3$ (Ví dụ 10.18, Mệnh đề 10.40).
4. $\Delta p_A=0$, nên chính sách mới tới $s_B$ với cùng xác suất $0{,}5$ như chính sách cũ, và phần bậc hai $2{,}7\,\Delta p_A\Delta p_B$ bằng $0$: $\Delta J=\mathcal L-J=1{,}35\cdot\tfrac13=0{,}45$ (Ví dụ 10.12, 10.14). Trên chuỗi, sai số của hàm thay thế là $2{,}7\,\Delta p_A\Delta p_B$, nên hàm thay thế chỉ sai khi chính sách mới đổi cả xác suất tới $s_B$ lẫn chính sách tại $s_B$; đổi riêng $p_A$ hay riêng $p_B$ đều cho đúng $\Delta J$.

### 7.5 Bài tập theo mục

Bài tập củng cố 10.1–10.12 và 10.23 nằm ở cuối chương; bộ bài tập chính thức, Bài tập 10.13–10.17 và 10.22, nằm ở [tệp bài tập Bài 10](material-viewer.html?doc=materials/lec-10/exercises.md&deck=lecture-10-trpo-va-ppo.html). Bảng sau ghi hai loại bài tập theo mục.

| Mục | Bài tập | Tệp bài tập |
|---|---|---|
| 1. Hai giới hạn của REINFORCE | — | 10.22 |
| 2. Đường cơ sở, lợi thế, actor–critic | 10.1, 10.4, 10.5, 10.10 | 10.14 |
| 3. GAE | 10.6, 10.7 | 10.13, 10.15 |
| 4. Hàm thay thế và miền tin cậy | 10.11 | 10.16 |
| 5. TRPO và gradient tự nhiên | 10.8, 10.9 | 10.17 |
| 6. PPO | 10.2, 10.12, 10.23 | 10.14 |
| 7. Tổng kết | 10.3 | — |

<!-- note-topic-id: lec-10-topic-24 -->
### 7.6 Giới hạn còn lại

Ở Mục 2–6, giới hạn còn lại là dữ liệu theo chính sách: Mệnh đề 10.2 và 10.15 cần lượt do chính sách đang cập nhật sinh ra, và Thuật toán 10.49 bỏ mỗi đoạn thu sau $K$ epoch.

---

## Tình huống áp dụng và ứng dụng

::: application Tình huống 10.1 (PPO trên CartPole: GAE ở bước cắt ngắn)
**Bài toán.** Huấn luyện PPO trên CartPole với giới hạn $500$ bước (Định nghĩa 08.6): mỗi bước giữ được cột cho phần thưởng $1$; $\gamma=0{,}99$, $\lambda=0{,}95$. Một lượt giữ cột đủ $500$ bước; critic cũ cho $\hat v_{\mathrm{old}}\equiv95$ ở mọi trạng thái của lượt, kể cả quan sát cuối. Giá trị đúng của chuỗi phần thưởng $1$ không kết thúc là $100$.

**Mô hình hóa.** Bộ đệm của Thuật toán 10.49 lưu các mảng $h\times N$ cho $R$, $Z$, $U$, $\hat v_{\mathrm{old}}$, cùng giá trị của quan sát cuối ở bước cắt. Lượt này kết thúc vì giới hạn thời gian, không vì MDP: $U_{500}=1$, $Z_{500}=0$. Tình huống dùng Mệnh đề 10.14(c), bước 2–3 của Thuật toán 10.16 và Thuật toán 10.49.

**Kiểm giả thiết.** Thuật toán 10.16 cần $Z$ chỉ ghi kết thúc của MDP và giá trị bootstrap lấy ở quan sát cuối trước khi môi trường tự đặt lại: thỏa. Mệnh đề 10.15 không áp dụng: $\lambda=0{,}95<1$ loại (a), critic hằng $95$ khác $v_\pi$ loại (b), và lượt bị cắt ở bước $500$. Ước lượng gradient dùng GAE ở đây không có bảo đảm γ-just.

**Tính.** $\delta_{499}=1+0{,}99\cdot95-95=0{,}05$; vì $U_{500}=1$, $\widehat A_{499}=\delta_{499}=0{,}05$. Bước trước: $\delta_{498}=0{,}05$ và $\widehat A_{498}=0{,}05+0{,}99\cdot0{,}95\cdot0{,}05=0{,}0970$.

**Diễn giải.** Gần giới hạn thời gian, lợi thế ước lượng nhỏ và dương, giống mọi bước khác của lượt, nên các bước cuối không bị coi là thất bại. Critic nhận mục tiêu $V^{\mathrm{targ}}_{498}=95{,}097$, kéo nó về phía $100$.

**Giới hạn.** Trên một lần huấn luyện thật, $\hat v$ đổi theo trạng thái, nên $\widehat A_{498}$ phụ thuộc giá trị của critic tại hai quan sát cuối.
:::

::: application Tình huống 10.2 (Vi phạm giả thiết: coi cắt ngắn là kết thúc)
**Bài toán.** Cùng dữ kiện với Tình huống 10.1: CartPole, giới hạn $500$ bước, phần thưởng $1$ mỗi bước, $\gamma=0{,}99$, $\lambda=0{,}95$, $\hat v_{\mathrm{old}}\equiv95$. Một bản cài đặt ghi $Z_{500}=1$ khi lượt chạm giới hạn thời gian.

**Kiểm giả thiết.** Giả thiết "$Z$ chỉ ghi kết thúc của MDP" của Định nghĩa 08.4 và Thuật toán 10.16 bị vi phạm, nên kết luận của Mệnh đề 10.8 và Thuật toán 10.16 không áp dụng: sai số TD ở bước cuối thiếu phần bootstrap.

**Tính.** $\delta_{499}=1-95=-94$, và $\widehat A_{498}=0{,}05+0{,}9405\cdot(-94)=-88{,}36$, so với $0{,}0970$ ở Tình huống 10.1.

**Hậu quả.** Mỗi hành động ở các bước gần giới hạn bị coi là dẫn tới kết thúc với giá trị $0$, nên actor giảm xác suất của chính những hành động đã giữ cột thành công, và critic học mục tiêu $1$ cho trạng thái cuối, khác mục tiêu của trạng thái giống hệt ở giữa lượt. Với cờ sai, thuật toán học như thể lượt kết thúc thật ở bước $500$; vì trạng thái không chứa chỉ số thời gian, bài toán đó không còn tính Markov trên trạng thái quan sát.
:::

::: application Tình huống 10.3 (Breakout: đối chiếu notebook Bài 09)
**Bài toán.** Notebook thực hành thứ hai của Bài 09 (`thuc-hanh-double-dqn-reinforce-breakout.ipynb`, mục 8) cho kết quả sau $10^6$ bước. Với $\alpha=10^{-5}$, chính sách tham lam của hai lần chạy REINFORCE chọn sang phải ở mọi bước và đạt $2{,}43$ điểm; khi lấy mẫu, sang phải chiếm $63\%$ và $75\%$ số bước. Với $\alpha=10^{-4}$, entropy còn $0{,}006$ và điểm bằng $0$ ở mốc ghi đầu tiên. DQN và Double DQN đạt $42$–$66$ điểm ở bốn trong sáu lần chạy cùng ngân sách. Trên Breakout, phần thưởng thưa và nhiều lượt có $\widehat g=0$.

**Kiểm giả thiết.** Mệnh đề 10.2 cần (G1)–(G4), lượt sinh bởi $\pi_\theta$ và đường cơ sở không phụ thuộc hành động; một critic $\hat v(S_t,w)$ giữ cố định trong lượt thỏa điều kiện cuối. Tuy vậy, theo notebook (mục 9), các giả thiết sau không thỏa:

- (G1): mỗi lượt kết thúc khi mất một mạng, nên trạng thái đầu của các mạng sau phụ thuộc $\theta$;
- (G1), tính Markov: quan sát bốn khung chỉ gần Markov;
- phần thưởng của MDP gốc: phần thưởng bị cắt về dấu.

Mệnh đề 10.2 chỉ áp dụng cho bài toán đã lý tưởng hóa.

**Phân tích có điều kiện.** Đường cơ sở và critic giữ kỳ vọng của ước lượng (Mệnh đề 10.2) và có thể giảm phương sai (Mệnh đề 10.3); PPO (Thuật toán 10.49) cho dùng lại mỗi đoạn thu trong nhiều bước. Khi một lượt không có phần thưởng nào, mọi $G_t=0$ và hệ số là $-\hat v(S_t,w)$: với $\hat v$ gần $v_\pi$, lượt đó làm giảm xác suất các hành động đã chọn so với các lượt có điểm, khác REINFORCE không đường cơ sở, nơi $\widehat g=0$. Tuy vậy, khi chính sách gần như không bao giờ nhận phần thưởng thì $v_\pi\approx0$, $\hat v\approx0$, hệ số gần $0$, và không công cụ nào của chương cho biết hành động nào dẫn tới phần thưởng. Số hạng entropy của Định nghĩa 10.46 chỉ ngăn chính sách trở nên tất định. Tìm ra phần thưởng là bài toán thăm dò, nằm ngoài phạm vi các kết quả trên.

**Giới hạn.** Các số $2{,}43$ và $42$–$66$ đo REINFORCE, DQN và Double DQN; để so PPO với chúng, cần chạy PPO với cùng ngân sách $10^6$ bước và cùng các lần chạy.
:::

## Tóm tắt chương

Chúng ta bắt đầu từ hai giới hạn của REINFORCE: trên bài toán một bước, tổng phương sai của ước lượng tăng từ $\tfrac49$ lên $\tfrac{16}9$ khi cộng $1$ vào mọi phần thưởng (Ví dụ 10.1); trên hành lang ngắn, ba lượt cho tọa độ thứ nhất của ước lượng bằng $-1$, $1$ và $-5{,}5$, trong khi gradient đúng có tọa độ đó bằng $2$ (Ví dụ 10.2), và một bước lớn theo đúng gradient kéo $J$ từ $-12$ xuống khoảng $-21{,}3$. Trừ một đường cơ sở giữ kỳ vọng (Mệnh đề 10.2): trên chuỗi hai trạng thái, trừ $v_\pi$ giữ kỳ vọng $0{,}2$ của tọa độ $\theta_A$ và giảm phương sai từ $0{,}6925$ xuống $0{,}2025$ (Ví dụ 10.6); trên bài toán một bước, đường cơ sở tối ưu là $b^*=1\ne v_\pi=2$ (Mệnh đề 10.3). Critic đánh giá hành động qua mục tiêu bootstrap (Định nghĩa 10.7), với sai số TD có kỳ vọng có điều kiện bằng lợi thế khi critic đúng (Mệnh đề 10.8); critic $(1{,}4;\,1)$, đánh giá thấp $s_B$, cho $\delta_0=-0{,}5$ dù lợi thế bằng $0{,}4$ (Ví dụ 10.7). GAE trộn các ước lượng $n$ bước bằng trọng số $(\gamma\lambda)^k$; với critic đó và $\lambda=0{,}5$, độ chệch là $-0{,}45$, thay cho $-0{,}9$ của ước lượng một bước, và khoảng cách giữa hai lượt là $1{,}35$, thay cho $2{,}7$ của hệ số Monte Carlo (Ví dụ 10.8); GAE không làm chệch gradient khi $\lambda=1$ với lượt đầy đủ hoặc khi critic đúng (Mệnh đề 10.14, 10.15). Trên chuỗi hai trạng thái, bổ đề chênh lệch hiệu năng cho $\Delta J=0{,}296$ còn hàm thay thế cho $0{,}26$ (Ví dụ 10.11, Bổ đề 10.19, Mệnh đề 10.22); với bước dài tới $(0{,}9;\,0{,}5)$, $\Delta\mathcal L=0{,}095$ còn $\Delta J=-0{,}085$, vì sai số tăng theo bình phương độ dài bước (Ví dụ 10.12). Vì vậy chúng ta cực đại hóa hàm thay thế trong một miền KL trung bình (Định nghĩa 10.24); Định lý 10.27 chặn sai số theo khoảng cách TV, và bước miền tin cậy có mức giảm bị chặn (Hệ quả 10.31). TRPO giải bài toán đó xấp xỉ bằng gradient tự nhiên và gradient liên hợp (Mệnh đề 10.34, Thuật toán 10.37), còn PPO thay ràng buộc bằng mục tiêu cắt, một chặn dưới của hàm thay thế mẫu (Mệnh đề 10.41, Thuật toán 10.49); trên chuỗi hai trạng thái, với bộ đệm hai lượt có lợi thế ước lượng sai dấu, nghiệm tối ưu lý tưởng hóa của mục tiêu cắt làm $J$ giảm $0{,}008$, thay cho $0{,}4$ khi không cắt; kết quả này riêng cho ví dụ đó (Mục 6.1). PPO cũng có thể thay ràng buộc bằng phạt KL với hệ số thích nghi (Định nghĩa 10.43). Không phương pháp thực hành nào giữ được bảo đảm đơn điệu, và kết quả hội tụ hiện có cho PPO-Clip chỉ nói về điểm dừng của một mô hình đơn giản hóa (Nhận xét 10.51).

**Định nghĩa và kết quả theo mục.**

- Mục 2: Định nghĩa 10.1 (đường cơ sở), Mệnh đề 10.2 (không chệch), Mệnh đề 10.3 (đường cơ sở tối ưu), Định nghĩa 10.4 (lợi thế), Mệnh đề 10.5 (gradient dạng lợi thế), Thuật toán 10.6 (REINFORCE có đường cơ sở), Định nghĩa 10.7 (critic, actor, actor–critic), Mệnh đề 10.8 (sai số TD và lợi thế), Thuật toán 10.9 (actor–critic một bước), Nhận xét 10.10 (đường cơ sở và critic).
- Mục 3: Định nghĩa 10.11 (lợi tức $n$ bước), Bổ đề 10.12 (tổng sai số TD), Định nghĩa 10.13 (lợi tức λ, GAE), Mệnh đề 10.14 (dạng tổng, truy hồi), Mệnh đề 10.15 (γ-just), Thuật toán 10.16 (GAE trên đoạn thu), Nhận xét 10.17 (vai trò của $\gamma$, cắt ngắn).
- Mục 4: Định nghĩa 10.18 (phân bố chiếm dụng), Bổ đề 10.19 (chênh lệch hiệu năng), Hệ quả 10.20 (cải thiện cho chính sách ngẫu nhiên), Định nghĩa 10.21 (hàm thay thế), Mệnh đề 10.22 (khớp bậc một), Định nghĩa 10.23 (TV, KL), Định nghĩa 10.24 (miền tin cậy), Mệnh đề 10.25 (KL không âm, Pinsker), Bổ đề 10.26 (dịch chuyển phân bố chiếm dụng), Định lý 10.27 (chặn cải thiện), Hệ quả 10.28 (chặn dạng KL), Nhận xét 10.29 (cận dạng lớn nhất), Hệ quả 10.30 (cải thiện đơn điệu), Hệ quả 10.31 (mức giảm tối đa).
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
&\quad+\tfrac1{1-\gamma}\textstyle\sum_s\nu^{\mathrm{old}}(s)A_{\mathrm{old}}(s,\pi_\theta),\\
&\Delta J-\Delta\mathcal L\\
&\quad=\textstyle\sum_s\bigl(\eta_{\pi'}(s)-\eta_\pi(s)\bigr)A_\pi(s,\pi'),\\
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
- Hệ quả 10.30 và 10.31 cần đánh giá và tối ưu chính xác.
- Mục tiêu cắt không chặn KL giữa hai chính sách.
- approxKL không chệch chỉ khi tham số không phụ thuộc các mẫu dùng để tính nó.
- Điều kiện hỗ trợ có hai chiều: $\pi_\theta>0\Rightarrow\pi_{\mathrm{old}}>0$ cho dạng tỉ số của hàm thay thế, và $\pi_\theta>0$ trên miền hỗ trợ của $\pi_{\mathrm{old}}$ cho KL hữu hạn.

---

## Bài tập củng cố

Các bài phủ bảy mục tiêu học tập: mục tiêu 1 (Bài tập 10.1, 10.4), 2 (10.5, 10.10), 3 (10.6, 10.7), 4 (10.11, 10.23), 5 (10.3, 10.8, 10.9, 10.11), 6 (10.2, 10.12, 10.23), 7 (10.2, 10.3, 10.12).

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
Đối chiếu từng câu với Hệ quả 10.30, Nhận xét 10.38, 10.42, 10.50, 10.51.
:::

::: solution
**Câu (a).** Sai. Hệ quả 10.30 cần lợi thế, phân bố chiếm dụng và phép cực đại hóa chính xác; Thuật toán 10.37 dùng ước lượng, trung bình đều, xấp xỉ bậc hai và gradient liên hợp dừng sớm (Nhận xét 10.38).

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
Chuỗi hai trạng thái: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; $p_A=\tfrac12$, $p_B=\tfrac23$; $v_\pi=(1{,}4;\,2)$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$; $\psi_\theta(s_A,1)=0{,}5\,e_A$, $\psi_\theta(s_A,2)=-0{,}5\,e_A$. Critic cố định $\hat v=(1{,}4;\,1)$. Dùng Mệnh đề 10.8(b), tính $\mathbb E[\delta_0\mid s_A,a]$ cho hai hành động, và tọa độ $\theta_A$ của $\mathbb E[\delta_0\psi_0]$; so với giá trị đúng $0{,}2$.
:::

::: hint
$e=\hat v-v_\pi=(0;\,-1)$; hành động 1 dẫn tới $s_B$ chắc chắn, hành động 2 dẫn tới trạng thái kết thúc, nơi $e=0$.
:::

::: solution
**Hành động 1.** Độ chệch $\gamma e(s_B)-e(s_A)=0{,}9\cdot(-1)-0=-0{,}9$, nên $\mathbb E[\delta_0\mid s_A,1]=0{,}4-0{,}9=-0{,}5$.

**Hành động 2.** Độ chệch $0-e(s_A)=0$, nên $\mathbb E[\delta_0\mid s_A,2]=-0{,}4$.

**Gradient.** $\tfrac12\cdot(-0{,}5)\cdot0{,}5+\tfrac12\cdot(-0{,}4)\cdot(-0{,}5)=-0{,}125+0{,}1=-0{,}025$, ngược dấu giá trị đúng $0{,}2$.

**Kiểm tra lại.** Tính trực tiếp: $\delta_0=0+0{,}9\cdot1-1{,}4=-0{,}5$ và $\delta_0=1-1{,}4=-0{,}4$. Hai độ chệch khác nhau, $-0{,}9$ và $0$, nên không bị khử khi nhân với hàm điểm. Lỗi thường gặp là cho rằng critic đúng ở $s_A$ thì $\delta_0$ không chệch tại $s_A$; độ chệch của hành động 1 đến từ sai số $e(s_B)$ của trạng thái kế.
:::

::: exercise Bài tập 10.6 (Truy hồi của lợi tức λ và lợi tức λ cắt)
Cho critic cố định và $\lambda\in[0,1)$.

- (a) Từ Định nghĩa 10.11 và 10.13, chứng minh $G^\lambda_t=R_{t+1}+\gamma\bigl[(1-\lambda)\hat v(S_{t+1})+\lambda G^\lambda_{t+1}\bigr]$, với quy ước $G^\lambda_T=0$ và $\hat v(S_T)=0$ (Sutton và Barto, 2018, Bài tập 12.1).
- (b) Với lợi tức λ cắt tại $h$, $G^\lambda_{t:h}=(1-\lambda)\sum_{n=1}^{h-t-1}\lambda^{n-1}G_{t:t+n}+\lambda^{h-t-1}G_{t:h}$, chứng minh $G^\lambda_{t:h}=\hat v(S_t)+\sum_{i=t}^{h-1}(\gamma\lambda)^{i-t}\delta_i$ (Sutton và Barto, 2018, (12.10), Bài tập 12.5).
- (c) Kiểm câu (a) trên hai lượt của Ví dụ 10.8: $\gamma=0{,}9$, $\lambda=0{,}5$, $\hat v=(1{,}4;\,1)$, $R_1=0$, $R_2=3$ hoặc $R_2=0$, kết thúc tại $T=2$.
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

**Câu (c).** Với $R_2=3$: $G^\lambda_1=3$, $G^\lambda_0=0+0{,}9(0{,}5\cdot1+0{,}5\cdot3)=1{,}8$, và $1{,}8-1{,}4=0{,}4=\delta_0+\gamma\lambda\delta_1=-0{,}5+0{,}45\cdot2$. Với $R_2=0$: $G^\lambda_1=0$, $G^\lambda_0=0+0{,}9(0{,}5\cdot1+0{,}5\cdot0)=0{,}45$, và $0{,}45-1{,}4=-0{,}95=-0{,}5+0{,}45\cdot(-1)$.

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
- (d) Giải thích vì sao dùng $\eta$ chứ không dùng $\nu^\pi$, và vì sao Định lý 10.27 không áp dụng.
:::

::: hint
$q_\pi(s,a)=-1+v_\pi(\text{ô kế})$ với ô kế theo động lực của hành lang; $\eta$ thỏa $\eta=e_1+\eta P_\pi$ trên ba ô chưa kết thúc.
:::

::: solution
**Câu (a).** $s_1$: hành động 1 tới $s_2$, $q=-11$; hành động 2 đứng yên, $q=-13$; $A=(1;\,-1)$. $s_2$: hành động 1 về $s_1$, $q=-13$; hành động 2 tới $s_3$, $q=-7$; $A=(-3;\,3)$. $s_3$: hành động 1 tới đích, $q=-1$; hành động 2 về $s_2$, $q=-11$; $A=(5;\,-5)$.

**Câu (b).** Hệ $\eta_1=1+\tfrac12\eta_1+\tfrac12\eta_2$, $\eta_2=\tfrac12\eta_1+\tfrac12\eta_3$, $\eta_3=\tfrac12\eta_2$ cho $\eta=(6;\,4;\,2)$; tổng $12$ bằng độ dài lượt kỳ vọng.

**Câu (c).** Tại mỗi ô, $\sum_a\pi A\psi_1=\tfrac14\bigl(A(s,1)-A(s,2)\bigr)$: $0{,}5$; $-1{,}5$; $2{,}5$. Tọa độ thứ nhất là $6\cdot0{,}5+4\cdot(-1{,}5)+2\cdot2{,}5=2$, khớp.

**Câu (d).** Với $\gamma=1$, $\nu^\pi$ không xác định vì thừa số $1-\gamma=0$; dạng quỹ đạo của Mệnh đề 10.5(b) gom theo trạng thái cho trọng số $\eta$ không chuẩn hóa. Định lý 10.27 cần $\gamma<1$.

**Kiểm tra lại.** Mệnh đề 10.5(a) tại mỗi ô: $\tfrac12(1-1)=0$, $\tfrac12(-3+3)=0$, $\tfrac12(5-5)=0$.
:::

::: exercise Bài tập 10.11 (Đánh giá một bước cập nhật trên chuỗi hai trạng thái)
Chuỗi hai trạng thái của Ví dụ 10.6 với $\gamma=0{,}9$, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$, $J=1{,}4$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$, $\nu^\pi=(0{,}1;\,0{,}045)$. Chính sách đề xuất $\pi''$: $p''_A=0{,}55$, $p''_B=0{,}7$. Tính:

- (a) $J(\pi'')$ và $\Delta J$;
- (b) $\mathcal L-J$;
- (c) cận của Định lý 10.27;
- (d) KL trung bình theo chiều cũ‖mới, và xét xem $\pi''$ có thuộc miền tin cậy với $\kappa=0{,}001$ không;
- (e) phạt của Hệ quả 10.28.
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

**Kiểm tra lại.** Bổ đề 10.19: $0{,}04+0{,}9\cdot0{,}55\cdot0{,}1=0{,}0895=\Delta J$. Bước làm $J$ tăng $0{,}0895$ dù cận bằng $-0{,}032$, nên cận bảo thủ trên bước này.
:::

::: exercise Bài tập 10.12 (Kiểm một mini-batch PPO)
Cho $\epsilon=0{,}2$, bốn mẫu có $\log\rho=(0{,}1;\,-0{,}3;\,0{,}25;\,-0{,}05)$, $\widehat A=(2;\,-1;\,-1;\,0{,}5)$, và ngưỡng dừng sớm approxKL bằng $0{,}015$.

- (a) Tính $\rho$, $\ell^{\mathrm{CLIP}}$ và $\mathcal L^{\mathrm{CLIP}}$.
- (b) Tính tỉ lệ cắt và xác định các mẫu có gradient bằng $0$.
- (c) Tính hai dạng approxKL và quyết định có dừng sớm không.
- (d) Nếu thay mục tiêu cắt bằng PPO-Penalty với $\beta=1$, $\kappa_{\mathrm{targ}}=0{,}01$, và KL dạng đóng trung bình trên bộ đệm sau lần cập nhật là $0{,}018$, tính $\beta$ theo quy tắc của Định nghĩa 10.43; tính lại $\beta$ khi KL đó bằng $0{,}008$.
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

::: exercise Bài tập 10.23 (Một vòng PPO-Clip trên chuỗi hai trạng thái)
Chuỗi hai trạng thái của Ví dụ 10.6: tại $s_A$, hành động 1 sang $s_B$ với phần thưởng $0$, hành động 2 kết thúc với phần thưởng $1$; tại $s_B$, hành động 1 kết thúc với phần thưởng $3$, hành động 2 kết thúc với phần thưởng $0$; $\gamma=0{,}9$; mỗi trạng thái có một tham số, $p_s=\sigma(\theta_s)$. Chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$ có $J=1{,}4$, $\nu^{\mathrm{old}}=(0{,}1;\,0{,}045)$ và lợi thế đúng $A_{\mathrm{old}}(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_{\mathrm{old}}(s_B,\cdot)=(1;\,-2)$. Một vòng PPO-Clip với $\epsilon=0{,}2$ dùng lợi thế đúng, giữ cố định; tại mỗi trạng thái, các mẫu có đúng tần suất hành động của $\pi_{\mathrm{old}}$; vòng trong tăng $\mathcal L^{\mathrm{CLIP}}$ từ $\pi_{\mathrm{old}}$ tới đầu đoạn phẳng. Với $\rho_s(a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$, phần của mục tiêu cắt tại $s$ là
$$\begin{aligned}\ell_s&=\sum_a\pi_{\mathrm{old}}(a\mid s)\\&\quad\times\min\bigl(\rho_s(a)A_{\mathrm{old}}(s,a),\\&\qquad\operatorname{clip}(\rho_s(a),0{,}8,1{,}2)\\&\qquad\quad\times A_{\mathrm{old}}(s,a)\bigr).\end{aligned}$$

- (a) Viết $\ell_{s_A}$ theo $p_A$ và $\ell_{s_B}$ theo $p_B$, rồi tìm chính sách $\pi'$ nơi vòng trong dừng.
- (b) Tính mức tăng mà hàm thay thế dự báo, $\mathcal L_{\pi_{\mathrm{old}}}(\pi')-J(\pi_{\mathrm{old}})$, và mức tăng thật $\Delta J=J(\pi')-J(\pi_{\mathrm{old}})$.
- (c) Tính $\tfrac1{1-\gamma}\sum_s\nu^{\mathrm{old}}(s)\,\ell_s(\pi')$ và xếp ba số của (b), (c) theo thứ tự tăng.
- (d) Dùng đẳng thức $\Delta J=0{,}8\,\Delta p_A+1{,}35\,\Delta p_B+2{,}7\,\Delta p_A\Delta p_B$ của Ví dụ 10.12, giải thích vì sao hàm thay thế dự báo thấp hơn mức tăng thật.
:::

::: hint
Tham số của hai trạng thái tách nhau, nên vòng trong tăng từng $\ell_s$ riêng. Theo Mệnh đề 10.40, mẫu có lợi thế dương đóng góp $A\min(\rho,1+\epsilon)$, mẫu có lợi thế âm đóng góp $A\max(\rho,1-\epsilon)$; khi $p_s$ tăng, tìm lúc từng nhóm mẫu chạm biên.
:::

::: solution
**Câu (a).** Tại $s_A$, $\rho(1)=2p_A$ và $\rho(2)=2(1-p_A)$, nên với $p_A\ge\tfrac12$,
$$\begin{aligned}\ell_{s_A}&=0{,}2\min(2p_A;\,1{,}2)\\&\quad-0{,}2\max(2-2p_A;\,0{,}8).\end{aligned}$$
Hai nhóm mẫu chạm biên cùng lúc tại $p_A=0{,}6$. Trên $[\tfrac12;\,0{,}6]$, $\ell_{s_A}=0{,}8p_A-0{,}4$ tăng; từ $p_A=0{,}6$, $\ell_{s_A}=0{,}24-0{,}16=0{,}08$ là hằng.

Tại $s_B$, $\rho(1)=1{,}5p_B$ và $\rho(2)=3(1-p_B)$, nên với $p_B\ge\tfrac23$,
$$\begin{aligned}\ell_{s_B}&=\tfrac23\min(1{,}5p_B;\,1{,}2)\\&\quad-\tfrac23\max(3-3p_B;\,0{,}8).\end{aligned}$$
Mẫu hành động 2 chạm $\rho=0{,}8$ tại $p_B=0{,}7\overline3$, mẫu hành động 1 chạm $\rho=1{,}2$ tại $p_B=0{,}8$. Do đó $\ell_{s_B}=3p_B-2$ trên $[\tfrac23;\,0{,}7\overline3]$, $\ell_{s_B}=p_B-0{,}5\overline3$ trên $[0{,}7\overline3;\,0{,}8]$, và $\ell_{s_B}=0{,}8-0{,}5\overline3=0{,}2\overline6$ từ $p_B=0{,}8$.

Vòng trong dừng tại $\pi'$: $p'_A=0{,}6$, $p'_B=0{,}8$, đúng chính sách $\pi'$ của Ví dụ 10.11.

**Câu (b).** $A_{\mathrm{old}}(s_A,\pi')=0{,}6\cdot0{,}4-0{,}4\cdot0{,}4=0{,}08$ và $A_{\mathrm{old}}(s_B,\pi')=0{,}8\cdot1-0{,}2\cdot2=0{,}4$, nên $\mathcal L-J=10(0{,}1\cdot0{,}08+0{,}045\cdot0{,}4)=0{,}26$. $J(\pi')=2{,}7\cdot0{,}6\cdot0{,}8+0{,}4=1{,}696$, nên $\Delta J=0{,}296$.

**Câu (c).** $10(0{,}1\cdot0{,}08+0{,}045\cdot0{,}2\overline6)=0{,}08+0{,}12=0{,}2$. Thứ tự là $0{,}2<0{,}26<0{,}296$. Số $0{,}2$ là tổng theo $\eta_{\pi_{\mathrm{old}}}=(1;\,0{,}45)$, $0{,}08+0{,}45\cdot0{,}2\overline6$. Bất đẳng thức thứ nhất là Mệnh đề 10.41(a) áp cho từng mẫu, với lợi thế đúng và cùng trọng số $\eta_{\pi_{\mathrm{old}}}$ cho hai tổng: tại $s_B$, mẫu hành động 2 có $\rho=0{,}6<0{,}8$ nên được tính như $\rho=0{,}8$, đóng góp $-\tfrac23\cdot0{,}8=-0{,}5\overline3$ thay cho $-\tfrac23\cdot0{,}6=-0{,}4$. Bất đẳng thức thứ hai riêng cho ví dụ này (Câu (d)).

**Câu (d).** Với $\Delta p_A=0{,}1$ và $\Delta p_B=\tfrac2{15}$, hàm thay thế là phần bậc nhất $0{,}08+0{,}18=0{,}26$, và phần bậc hai là $2{,}7\cdot0{,}1\cdot\tfrac2{15}=0{,}036>0$. Chính sách mới tới $s_B$ nhiều hơn chính sách cũ ($0{,}6$ so với $0{,}5$), và tại $s_B$ nó tốt hơn chính sách cũ, $A_{\mathrm{old}}(s_B,\pi')=0{,}4>0$; hàm thay thế giữ tần suất thăm cũ nên bỏ mất phần đóng góp $0{,}9\cdot0{,}1\cdot0{,}4=0{,}036$ của các lần thăm thêm.

**Kiểm tra lại.** Bổ đề 10.19: $0{,}08+0{,}9\cdot0{,}6\cdot0{,}4=0{,}296$. Hai lỗi thường gặp: dừng ở $p_B=0{,}7\overline3$, nơi chỉ mẫu hành động 2 chạm biên, trong khi hai mẫu hành động 1 còn gradient dương; và bỏ phép cắt, khi đó $\ell_{s_B}=3p_B-2$ tăng mãi và đẩy $p_B$ về $1$.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

**Hướng dẫn đọc thêm.** Sutton và Barto (2018), §13.4–13.5, trình bày đường cơ sở và actor–critic một bước với hộp giả mã mà Thuật toán 10.6 và 10.9 dựa vào; §7.1 và §12.1–12.3 trình bày lợi tức $n$ bước và lợi tức λ, cơ sở của Mục 3. Các phần TRPO, GAE, PPO không có trong sách; đọc Schulman và cộng sự (2015, §2–3, Phụ lục C), (2016, §2–3) và (2017, §3–5). Chặn cải thiện dạng kỳ vọng theo Achiam và cộng sự (2017, §5, phụ lục); chi tiết cài đặt theo Huang và cộng sự (2022) và Engstrom và cộng sự (2020).

**Tài liệu tham khảo.**

1. Tạ Việt Cường. *Lecture 10: Overview on Policy Gradient Algorithms, Part 1* (lecture10_policy_gradient_part2.pdf, 43 trang), học phần AIT3007, 2025–2026. Mục 1: tr. 3–4, 9–10, 14; Mục 2: tr. 5, 8, 11–13; Mục 3: tr. 13, 24; Mục 4: tr. 4, 14–16; Mục 5: tr. 17–19; Mục 6: tr. 19–42; Mục 7: tr. 2–3, 28, 43.
2. Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018. §7.1 (tr. 142–144): Mục 3.1. §12.1 (tr. 288–291, Bài tập 12.1 tr. 290), §12.3 (tr. 295–297, (12.9)–(12.10), Bài tập 12.5): Mục 3.2–3.3. §13.3 (tr. 326–329), §13.4 (tr. 329–331, hộp tr. 330), §13.5 (tr. 331–332, (13.12)–(13.14), hộp tr. 332), ghi chú thư mục tr. 338: Mục 2.
3. Kakade, S., Langford, J. "Approximately Optimal Approximate Reinforcement Learning." *ICML* 2002, 267–274. Bổ đề 6.1: Bổ đề 10.19.
4. Kakade, S. "A Natural Policy Gradient." *NIPS* 14, 2002. Dẫn theo Schulman và cộng sự (2015, §7): Mục 5.1.
5. Schulman, J., Levine, S., Moritz, P., Jordan, M., Abbeel, P. "Trust Region Policy Optimization." *ICML* 2015 (arXiv 1502.05477). (1), (3), Định lý 1, §3 Thuật toán 1, (11)–(14), §5, §7, Phụ lục A–C: Mục 4–5.
6. Schulman, J., Moritz, P., Levine, S., Jordan, M., Abbeel, P. "High-Dimensional Continuous Control Using Generalized Advantage Estimation." *ICLR* 2016 (arXiv 1506.02438). §2 (6), Định nghĩa 1, Mệnh đề 1 (Phụ lục B), §3 (11)–(18): Mục 3; TRPO với GAE và critic: Thuật toán 10.37.
7. Schulman, J., Wolski, F., Dhariwal, P., Radford, A., Klimov, O. "Proximal Policy Optimization Algorithms." arXiv 1707.06347, 2017. (6)–(9), §3–4, Thuật toán 1, Bảng 1, 3, 5: Mục 6.
8. Achiam, J., Held, D., Tamar, A., Abbeel, P. "Constrained Policy Optimization." *ICML* 2017. Định lý 1, Hệ quả 1, 3, Mệnh đề 1, (7): Mục 4.6.
9. Greensmith, E., Bartlett, P. L., Baxter, J. "Variance Reduction Techniques for Gradient Estimates in Reinforcement Learning." *JMLR* 5 (2004): 1471–1530. §5, Định lý 13 (tr. 1489–1490), Hệ quả 15 (tr. 1491–1492): Mục 2.2.
10. Nocedal, J., Wright, S. J. *Numerical Optimization*, ấn bản 2, Springer, 2006. Thuật toán 5.2 (tr. 112), Định lý 5.1 (tr. 103), Định lý 5.4 (tr. 115): Mục 5.2.
11. Cover, T. M., Thomas, J. A. *Elements of Information Theory*, ấn bản 2, Wiley, 2006. Bổ đề 11.6.1 (tr. 370): Mệnh đề 10.25(b).
12. Hunter, D. R., Lange, K. "A Tutorial on MM Algorithms." *The American Statistician* 58(1) (2004): 30–37. Dẫn theo Schulman và cộng sự (2015, §3): Mục 4.6.
13. Engstrom, L., Ilyas, A., Santurkar, S., Tsipras, D., Janoos, F., Rudolph, L., Madry, A. "Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO." *ICLR* 2020. §3–6: Mục 6.1, 6.5.
14. Huang, S., Dossa, R. F. J., Raffin, A., Kanervisto, A., Wang, W. "The 37 Implementation Details of Proximal Policy Optimization." *ICLR Blog Track*, 2022: Mục 6.3–6.5.
15. Jin, R., Li, S., Wang, B. "On Stationary Point Convergence of PPO-Clip." *ICLR* 2024. §2.1, §3.1–3.3, Giả thiết 3.1–3.4, Định lý 3.1–3.3: Mục 6.6.
16. Nota, C., Thomas, P. S. "Is the Policy Gradient a Gradient?" *AAMAS* 2020: Nhận xét 10.17.
17. Weng, L. "Policy Gradient Algorithms." Blog, 2018: tài liệu đọc chung cho Mục 2–6.
