# Bài tập Bài 10 — TRPO và PPO

Tệp gồm năm bài, Bài tập 10.13–10.17, đánh số tiếp theo mười hai bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html) (Bài tập 10.1–10.12) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập của Sutton và Barto (2018), ghi số bài, mục và trang. Các bài chia theo hai mức: nhận biết (10.13); tính toán hoặc chứng minh (10.14–10.17). Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-10-trpo-va-ppo.html#/1/1) | — |
| 2. Đường cơ sở, hàm lợi thế và actor–critic | [Mở phần](lecture-10-trpo-va-ppo.html#/2/1) | 10.14; ghi chú: 10.1, 10.4, 10.5, 10.10 |
| 3. Ước lượng lợi thế tổng quát | [Mở phần](lecture-10-trpo-va-ppo.html#/3/1) | 10.13, 10.15; ghi chú: 10.6, 10.7 |
| 4. Hàm thay thế và chặn cải thiện | [Mở phần](lecture-10-trpo-va-ppo.html#/4/1) | 10.16; ghi chú: 10.11 |
| 5. TRPO và gradient tự nhiên | [Mở phần](lecture-10-trpo-va-ppo.html#/5/1) | 10.17; ghi chú: 10.8, 10.9 |
| 6. Tối ưu chính sách gần kề (PPO) | [Mở phần](lecture-10-trpo-va-ppo.html#/6/1) | 10.14; ghi chú: 10.2, 10.12 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-10-trpo-va-ppo.html#/7/1) | ghi chú: 10.3 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 10; công thức của sách được ghi rõ "của sách". Thời gian rời rạc $t=0,1,\dots$; tại bước $t$, trạng thái $S_t$, hành động $A_t$, phần thưởng $R_{t+1}$; lượt kết thúc tại bước $T$, và lợi tức là $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$, $G_T=0$. Lịch sử $H_t=(S_0,A_0,R_1,\dots,R_t,S_t)$ gồm mọi thứ đã quan sát khi chọn $A_t$ (Định nghĩa 09.20, Bổ đề 09.21). Như ghi chú, sau bước $T$ lượt ở một trạng thái hấp thụ có phần thưởng $0$, và mọi hàm giá trị bằng $0$ tại đó.

Với hàm giá trị $\hat v(\cdot,w)$ có $w$ cố định, sai số TD (temporal-difference error) là $\delta_t=R_{t+1}+\gamma\hat v(S_{t+1},w)-\hat v(S_t,w)$, với $\hat v(S_T,w)=0$; khi đó $\delta_t$ trùng sai số TD có mặt nạ $(1-Z_{t+1})$ của ghi chú. Đây là (6.5) và (12.6) của sách.

Hai bài 10.14 và 10.16 dùng dữ liệu do chính sách hành vi $\pi_{\mathrm{old}}$ sinh ra để đánh giá chính sách đích $\pi_\theta$, trên một quá trình quyết định Markov (Markov decision process, MDP) có tập trạng thái và tập hành động hữu hạn. Tỉ số một bước là
$$\rho_t=\frac{\pi_\theta(A_t\mid S_t)}{\pi_{\mathrm{old}}(A_t\mid S_t)},$$
như Định nghĩa 10.21, và điều kiện hỗ trợ $\pi_\theta(a\mid s)>0\Rightarrow\pi_{\mathrm{old}}(a\mid s)>0$ luôn được giả thiết. Miền hỗ trợ của $\pi_{\mathrm{old}}(\cdot\mid s)$ viết $\mathcal A^{\mathrm{old}}_s=\{a:\pi_{\mathrm{old}}(a\mid s)>0\}$. Tích các tỉ số từ bước $t$ tới bước $k$ viết $\rho_{t:k}=\prod_{j=t}^{k}\rho_j$. Quy ước $\rho_j=1$ khi $j\ge T$. Sách viết chính sách hành vi là $b$ và chính sách đích là $\pi$; ở đây chữ $b$ dành cho đường cơ sở, như ghi chú, nên hai chính sách là $\pi_{\mathrm{old}}$ và $\pi_\theta$. Sách gọi $\nabla\ln\pi(a\mid s,\boldsymbol\theta)$ là véc-tơ đủ điều kiện (eligibility vector); ghi chú gọi đại lượng này là hàm điểm $\psi_\theta(s,a)$ (Định nghĩa 09.15).

Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$; véc-tơ có tọa độ thập phân viết $(x_1;\,x_2)$.

## Mức nhận biết

### Bài tập 10.13. Chu kỳ bán rã của trọng số trong lợi tức λ

**Mức độ:** nhận biết; mục tiêu học tập 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 12.2, §12.1, trang 290; đẳng thức (12.3) và Hình 12.2, trang 290.

::: exercise Bài tập 10.13 (Chu kỳ bán rã của trọng số trong lợi tức λ)
Trong lợi tức λ (Định nghĩa 10.13), lợi tức $n$ bước $G_{t:t+n}$ nhận trọng số $(1-\lambda)\lambda^{n-1}$, $n=1,2,\dots$, với $0<\lambda<1$. Tham số $\lambda$ cho biết dãy trọng số này giảm nhanh đến đâu, tức thuật toán dựa trên lợi tức λ nhìn xa bao nhiêu bước về tương lai khi lập cập nhật. Tốc độ giảm cũng có thể đo bằng một hằng số thời gian, gọi là *chu kỳ bán rã* (half-life) $\tau_\lambda$: thời gian mà sau đó dãy trọng số còn một nửa giá trị ban đầu.

- (a) Viết phương trình liên hệ $\lambda$ và $\tau_\lambda$, rồi giải ra $\tau_\lambda$.
- (b) Theo (12.3) của sách, $\lambda=0$ cho mục tiêu một bước $G_{t:t+1}$ và $\lambda=1$ cho lợi tức Monte Carlo $G_t$. Tìm giới hạn của $\tau_\lambda$ khi $\lambda\to0^+$ và khi $\lambda\to1^-$, và đối chiếu với hai trường hợp đó.
:::

::: hint Gợi ý Bài tập 10.13
Giá trị ban đầu của dãy là trọng số của $n=1$; sau $\tau$ bước, trọng số bị nhân thêm $\lambda^{\tau}$. Lấy logarit tự nhiên hai vế.
:::

::: solution Lời giải Bài tập 10.13
**Câu (a).** Trọng số ban đầu là $(1-\lambda)\lambda^0=1-\lambda$. Mỗi bước, trọng số bị nhân với $\lambda$, nên sau $\tau$ bước nó bằng $(1-\lambda)\lambda^{\tau}$. Chu kỳ bán rã thỏa
$$\begin{aligned}&(1-\lambda)\lambda^{\tau_\lambda}=\tfrac12(1-\lambda),\\&\text{tức}\quad\lambda^{\tau_\lambda}=\tfrac12 .\end{aligned}$$
Lấy logarit tự nhiên: $\tau_\lambda\ln\lambda=-\ln2$. Vì $0<\lambda<1$ nên $\ln\lambda<0$, và
$$\tau_\lambda=\frac{\ln2}{\ln(1/\lambda)} .$$
Ngược lại, $\lambda=2^{-1/\tau_\lambda}$. Chu kỳ bán rã nói chung không là số nguyên; nó đo thời gian theo cùng đơn vị với chỉ số bước.

**Câu (b).** Khi $\lambda\to0^+$, $\ln(1/\lambda)\to+\infty$, nên $\tau_\lambda\to0$: gần như toàn bộ trọng số dồn vào $G_{t:t+1}$, khớp trường hợp $\lambda=0$ là phương pháp TD một bước. Khi $\lambda\to1^-$, $\ln(1/\lambda)\to0^+$, nên $\tau_\lambda\to+\infty$: trọng số giảm rất chậm, các lợi tức nhiều bước có trọng số gần nhau, và trong (12.3) phần $\lambda^{T-t-1}$ dồn vào lợi tức thực tăng về $1$, khớp trường hợp $\lambda=1$ là phương pháp Monte Carlo.

Cùng lập luận áp dụng cho trọng số $(\gamma\lambda)^k$ của sai số TD $\delta_{t+k}$ trong GAE (Mệnh đề 10.14(a)), với $\gamma\lambda$ ở vị trí của $\lambda$: chu kỳ bán rã là $\ln2/\ln\bigl(1/(\gamma\lambda)\bigr)$.

**Kiểm tra lại.** Với $\lambda=\tfrac12$, $\tau_\lambda=\ln2/\ln2=1$: sau một bước, trọng số giảm từ $\tfrac12$ xuống $\tfrac14$. Hai lỗi thường gặp: viết $\tau_\lambda=\ln2/\ln\lambda$, được một số âm; và lấy giá trị ban đầu là $1$ thay cho $1-\lambda$ rồi giải $(1-\lambda)\lambda^{\tau}=\tfrac12$, khi đó kết quả phụ thuộc cả thừa số chuẩn hóa $1-\lambda$, không còn là chu kỳ bán rã của dãy.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 10.14. Biến điều khiển không đổi kỳ vọng của lợi tức

**Mức độ:** chứng minh; mục tiêu học tập 1 và 7.

**Nguồn:** Sutton và Barto (2018), Bài tập 7.6, §7.4, trang 151; đẳng thức (7.13), trang 150, và (7.14), trang 151.

::: exercise Bài tập 10.14 (Biến điều khiển không đổi kỳ vọng của lợi tức)
Dữ liệu do chính sách hành vi $\pi_{\mathrm{old}}$ sinh ra trên một MDP có tập trạng thái và tập hành động hữu hạn, với phần thưởng $\lvert R_{t+1}\rvert\le R_{\max}$; chính sách đích là $\pi_\theta$, với tỉ số $\rho_t=\pi_\theta(A_t\mid S_t)/\pi_{\mathrm{old}}(A_t\mid S_t)$ và điều kiện hỗ trợ $\pi_\theta(a\mid s)>0\Rightarrow\pi_{\mathrm{old}}(a\mid s)>0$. $V$ là một hàm giá trị trạng thái cố định, $Q$ là một bảng giá trị hành động cố định, và $\bar V(s)=\sum_a\pi_\theta(a\mid s)\,Q(s,a)$ như (7.8) của sách. Chân trời $h$ là một số nguyên cố định. Sau bước kết thúc $T$, lượt ở trạng thái hấp thụ với $R_{t+1}=0$ và $\rho_t=1$ khi $t\ge T$, và $V$, $Q$, $\bar V$ bằng $0$ tại đó; với quy ước này, hai đẳng thức dưới đây xác định với mọi $t<h$.

Lợi tức $n$ bước khác chính sách của giá trị trạng thái, (7.13) của sách, là
$$\begin{aligned}G_{t:h}&=\rho_t\bigl(R_{t+1}\\&\qquad+\gamma G_{t+1:h}\bigr)\\&\quad+(1-\rho_t)V(S_t),\\G_{h:h}&=V(S_h).\end{aligned}$$
Lợi tức $n$ bước khác chính sách của giá trị hành động, (7.14) của sách, là
$$\begin{aligned}G_{t:h}&=R_{t+1}+\gamma\rho_{t+1}G_{t+1:h}\\&\quad+\gamma\bigl(\bar V(S_{t+1})\\&\qquad-\rho_{t+1}Q(S_{t+1},A_{t+1})\bigr),\end{aligned}$$
với $G_{h:h}=Q(S_h,A_h)$. Số hạng $(1-\rho_t)V(S_t)$ trong (7.13) và số hạng $\gamma\bigl(\bar V(S_{t+1})-\rho_{t+1}Q(S_{t+1},A_{t+1})\bigr)$ trong (7.14) gọi là *biến điều khiển* (control variate).

- (a) Chứng minh rằng với mọi $t$, $\mathbb E[\rho_t\mid H_t]=1$ và $\mathbb E[\rho_tQ(S_t,A_t)\mid H_t]=\bar V(S_t)$.
- (b) Gọi $\tilde G_{t:h}$ là lợi tức lập theo (7.13) nhưng bỏ biến điều khiển: $\tilde G_{t:h}=\rho_t\bigl(R_{t+1}+\gamma\tilde G_{t+1:h}\bigr)$, $\tilde G_{h:h}=V(S_h)$. Chứng minh $\mathbb E[G_{t:h}\mid H_t]=\mathbb E[\tilde G_{t:h}\mid H_t]$ với mọi $t\le h$.
- (c) Gọi $\tilde G_{t:h}$ là lợi tức lập theo (7.14) nhưng bỏ biến điều khiển: $\tilde G_{t:h}=R_{t+1}+\gamma\rho_{t+1}\tilde G_{t+1:h}$, $\tilde G_{h:h}=Q(S_h,A_h)$. Chứng minh $\mathbb E[G_{t:h}\mid H_t,A_t]=\mathbb E[\tilde G_{t:h}\mid H_t,A_t]$ với mọi $t\le h$.
:::

::: hint Gợi ý Bài tập 10.14
Khi biết $H_t$ với $t<T$, hành động $A_t$ có phân phối $\pi_{\mathrm{old}}(\cdot\mid S_t)$, và mẫu số của $\rho_t$ khử xác suất này. Ở (b) và (c), đặt $D_t=G_{t:h}-\tilde G_{t:h}$, viết truy hồi của $D_t$ theo $D_{t+1}$, rồi quy nạp lùi từ $D_h=0$ bằng tính chất tháp.
:::

::: solution Lời giải Bài tập 10.14
**Câu (a).** Nếu $t\ge T$ thì $\rho_t=1$ và $Q$, $\bar V$ bằng $0$ tại trạng thái hấp thụ, nên hai đẳng thức đúng. Xét $t<T$. Khi biết $H_t$, trạng thái $S_t=s$ đã xác định và $A_t\sim\pi_{\mathrm{old}}(\cdot\mid s)$, vì chính sách hành vi là Markov. Với một hàm $f$ bất kỳ trên tập hành động,
$$
\begin{aligned}
&\mathbb E[\rho_tf(A_t)\mid H_t]\\
&=\sum_{a\in\mathcal A^{\mathrm{old}}_s}\pi_{\mathrm{old}}(a\mid s)\\
&\qquad\times\frac{\pi_\theta(a\mid s)}{\pi_{\mathrm{old}}(a\mid s)}f(a)\\
&=\sum_{a\in\mathcal A^{\mathrm{old}}_s}\pi_\theta(a\mid s)f(a)\\
&=\sum_a\pi_\theta(a\mid s)f(a).
\end{aligned}
$$
Đẳng thức thứ nhất là định nghĩa kỳ vọng có điều kiện; đẳng thức thứ hai rút gọn $\pi_{\mathrm{old}}(a\mid s)$; đẳng thức thứ ba dùng điều kiện hỗ trợ: mọi hành động có $\pi_{\mathrm{old}}(a\mid s)=0$ cũng có $\pi_\theta(a\mid s)=0$. Với $f\equiv1$ được $\mathbb E[\rho_t\mid H_t]=1$; với $f(a)=Q(s,a)$ được $\mathbb E[\rho_tQ(S_t,A_t)\mid H_t]=\bar V(S_t)$. Mọi tỉ số bị chặn bởi $\max\{\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s):\pi_{\mathrm{old}}(a\mid s)>0\}$, một số hữu hạn vì các tập hữu hạn. Phần thưởng bị chặn bởi $R_{\max}$, và $V$, $Q$ là các bảng hữu hạn, nên mọi kỳ vọng dưới đây hữu hạn.

**Câu (b).** Đặt $D_t=G_{t:h}-\tilde G_{t:h}$. Khi đó $D_h=V(S_h)-V(S_h)=0$, và trừ hai truy hồi được, với $t<h$,
$$D_t=\gamma\rho_tD_{t+1}+(1-\rho_t)V(S_t).$$
Ta chứng minh $\mathbb E[D_t\mid H_t]=0$ bằng quy nạp lùi từ $t=h$. Giả sử $\mathbb E[D_{t+1}\mid H_{t+1}]=0$. Vì $\rho_t$ là hàm của $(S_t,A_t)$, nằm trong $H_{t+1}$, và $H_t$ là một phần của $H_{t+1}$, tính chất tháp cho
$$
\begin{aligned}
&\mathbb E[\gamma\rho_tD_{t+1}\mid H_t]\\
&=\gamma\,\mathbb E\bigl[\rho_t\,\mathbb E[D_{t+1}\mid H_{t+1}]\bigm|H_t\bigr]\\
&=0 .
\end{aligned}
$$
Số hạng còn lại là biến điều khiển; $V(S_t)$ là hàm của $H_t$, nên theo (a), $\mathbb E[(1-\rho_t)V(S_t)\mid H_t]=V(S_t)\bigl(1-\mathbb E[\rho_t\mid H_t]\bigr)=0$. Cộng hai phần được $\mathbb E[D_t\mid H_t]=0$, tức $\mathbb E[G_{t:h}\mid H_t]=\mathbb E[\tilde G_{t:h}\mid H_t]$.

**Câu (c).** Đặt $D_t=G_{t:h}-\tilde G_{t:h}$. Khi đó $D_h=Q(S_h,A_h)-Q(S_h,A_h)=0$, và với $t<h$,
$$
\begin{aligned}
D_t&=\gamma\rho_{t+1}D_{t+1}\\
&\quad+\gamma\bigl(\bar V(S_{t+1})\\
&\qquad-\rho_{t+1}Q(S_{t+1},A_{t+1})\bigr).
\end{aligned}
$$
Ta chứng minh $\mathbb E[D_t\mid H_t,A_t]=0$ bằng quy nạp lùi. Giả sử $\mathbb E[D_{t+1}\mid H_{t+1},A_{t+1}]=0$. Vì $\rho_{t+1}$ là hàm của $(H_{t+1},A_{t+1})$ và $(H_t,A_t)$ là một phần của $H_{t+1}$, tính chất tháp cho $\mathbb E[\gamma\rho_{t+1}D_{t+1}\mid H_t,A_t]=\gamma\,\mathbb E\bigl[\rho_{t+1}\mathbb E[D_{t+1}\mid H_{t+1},A_{t+1}]\bigm|H_t,A_t\bigr]=0$. Với biến điều khiển, (a) ở bước $t+1$ cho $\mathbb E\bigl[\bar V(S_{t+1})-\rho_{t+1}Q(S_{t+1},A_{t+1})\bigm|H_{t+1}\bigr]=\bar V(S_{t+1})-\bar V(S_{t+1})=0$, rồi tính chất tháp theo $H_{t+1}$ cho kỳ vọng $0$ khi biết $(H_t,A_t)$. Do đó $\mathbb E[D_t\mid H_t,A_t]=0$.

Ở (7.14), hành động đầu $A_t$ không nhân với tỉ số, vì điều kiện lấy theo $(H_t,A_t)$; tỉ số chỉ áp cho các hành động sau nó. Đẳng thức $\mathbb E[\rho_t\mid H_t]=1$ của (a) cũng là Bước 1 của chứng minh Mệnh đề 10.48; lấy đạo hàm theo $\theta$ tại $\theta=\theta_{\mathrm{old}}$ hai vế của $\sum_a\pi_{\mathrm{old}}(a\mid s)\rho_\theta(s,a)=1$ được $\sum_a\pi_{\mathrm{old}}(a\mid s)\psi_{\theta_{\mathrm{old}}}(s,a)=0$, đẳng thức mà Mệnh đề 10.2 dùng cho đường cơ sở.

**Kiểm tra lại.** Khi $\pi_\theta=\pi_{\mathrm{old}}$, mọi $\rho_t=1$: biến điều khiển của (7.13) bằng $0$ ở mọi mẫu, còn biến điều khiển của (7.14) là $\gamma\bigl(\bar V(S_{t+1})-Q(S_{t+1},A_{t+1})\bigr)$, có kỳ vọng $0$ khi biết $S_{t+1}$ vì $\bar V(S_{t+1})$ là trung bình của $Q(S_{t+1},\cdot)$ theo chính chính sách sinh $A_{t+1}$. Hai lỗi thường gặp: viết $\mathbb E[\rho_tG_{t+1:h}]=\mathbb E[\rho_t]\,\mathbb E[G_{t+1:h}]$, sai vì $G_{t+1:h}$ phụ thuộc $A_t$ qua $S_{t+1}$, nên chứng minh phải đi qua tính chất tháp; và bỏ điều kiện hỗ trợ, khi đó tổng ở (a) thiếu các hành động có $\pi_{\mathrm{old}}(a\mid s)=0<\pi_\theta(a\mid s)$ và $\mathbb E[\rho_t\mid H_t]<1$.
:::

### Bài tập 10.15. Sai số của lợi tức λ là tổng sai số TD

**Mức độ:** chứng minh; mục tiêu học tập 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 12.3, §12.2, trang 295; đẳng thức (12.4), trang 290, (12.6), trang 293, và (6.6), §6.1, trang 121.

::: exercise Bài tập 10.15 (Sai số của lợi tức λ là tổng sai số TD)
Một lượt $S_0,A_0,R_1,\dots,S_T$ kết thúc tại bước $T$. Hàm giá trị $\hat v(\cdot,w)$ có $w$ cố định trong cả lượt và $\hat v(S_T,w)=0$; sai số TD là $\delta_t=R_{t+1}+\gamma\hat v(S_{t+1},w)-\hat v(S_t,w)$, (12.6) của sách. Với $\lambda\in[0,1]$, lợi tức λ $G^\lambda_t$ của Định nghĩa 10.13 thỏa hệ thức truy hồi của Bài tập 10.6(a) (Bài tập 12.1 của sách; với $\lambda=1$, hệ thức là $G_t=R_{t+1}+\gamma G_{t+1}$):
$$\begin{aligned}G^\lambda_t&=R_{t+1}\\&\quad+\gamma\bigl[(1-\lambda)\hat v(S_{t+1},w)\\&\qquad+\lambda G^\lambda_{t+1}\bigr],\\G^\lambda_T&=0 .\end{aligned}$$
Thuật toán lợi tức λ ngoại tuyến (off-line λ-return algorithm), (12.4) của sách, cập nhật $w_{t+1}=w_t+\alpha\bigl[G^\lambda_t-\hat v(S_t,w_t)\bigr]\nabla\hat v(S_t,w_t)$ ở cuối lượt, với $t=0,\dots,T-1$; đại lượng trong ngoặc vuông là sai số của thuật toán.

- (a) Chứng minh rằng với $w$ cố định,
$$\begin{aligned}&G^\lambda_t-\hat v(S_t,w)\\&\quad=\sum_{k=t}^{T-1}(\gamma\lambda)^{k-t}\delta_k,\end{aligned}$$
theo mẫu chứng minh của (6.6) trong sách: $G_t-V(S_t)=\delta_t+\gamma\bigl(G_{t+1}-V(S_{t+1})\bigr)$, rồi lặp lại tới cuối lượt.
- (b) Viết đẳng thức ở (a) khi $\lambda=0$ và khi $\lambda=1$, và đối chiếu trường hợp $\lambda=1$ với (6.6).
:::

::: hint Gợi ý Bài tập 10.15
Trong vế phải của hệ thức truy hồi, cộng và trừ $\gamma\lambda\hat v(S_{t+1},w)$ để tách ra $\delta_t$.
:::

::: solution Lời giải Bài tập 10.15
**Câu (a).** Viết gọn $V(s)=\hat v(s,w)$ và đặt $E_t=G^\lambda_t-V(S_t)$. Với $t<T$,
$$
\begin{aligned}
E_t&=R_{t+1}\\
&\quad+\gamma(1-\lambda)V(S_{t+1})\\
&\quad+\gamma\lambda G^\lambda_{t+1}-V(S_t)\\
&=\bigl[R_{t+1}+\gamma V(S_{t+1})\\
&\qquad-V(S_t)\bigr]\\
&\quad+\gamma\lambda\bigl[G^\lambda_{t+1}\\
&\qquad-V(S_{t+1})\bigr]\\
&=\delta_t+\gamma\lambda E_{t+1}.
\end{aligned}
$$
Đẳng thức thứ nhất là hệ thức truy hồi của $G^\lambda_t$. Đẳng thức thứ hai cộng và trừ $\gamma\lambda V(S_{t+1})$, vì $\gamma(1-\lambda)V(S_{t+1})=\gamma V(S_{t+1})-\gamma\lambda V(S_{t+1})$. Đẳng thức thứ ba là định nghĩa của $\delta_t$ và của $E_{t+1}$; ở đây hai lần xuất hiện của $V(S_{t+1})$, trong $\delta_t$ và trong $E_{t+1}$, dùng cùng $w$. Tại bước cuối, $E_T=G^\lambda_T-V(S_T)=0-0=0$. Lặp hệ thức $E_t=\delta_t+\gamma\lambda E_{t+1}$ từ $t$ tới $T-1$:
$$
\begin{aligned}
E_t&=\delta_t+\gamma\lambda\delta_{t+1}+\dots\\
&\quad+(\gamma\lambda)^{T-1-t}\delta_{T-1}\\
&\quad+(\gamma\lambda)^{T-t}E_T\\
&=\sum_{k=t}^{T-1}(\gamma\lambda)^{k-t}\delta_k .
\end{aligned}
$$
Vế trái là ước lượng lợi thế tổng quát $\widehat A_t$ của Định nghĩa 10.13, nên kết quả trùng Mệnh đề 10.14(a) và trường hợp $h\ge T$ của Bài tập 10.6(b). Ở đây kết quả được chứng minh bằng truy hồi theo mẫu (6.6).

**Câu (b).** Với $\lambda=0$, chỉ còn số hạng $k=t$: $G^0_t-V(S_t)=\delta_t$, vì $G^0_t=G_{t:t+1}=R_{t+1}+\gamma V(S_{t+1})$ là mục tiêu TD một bước. Với $\lambda=1$, $G^1_t=G_t$ và đẳng thức thành
$$G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k ,$$
đúng là (6.6) của sách. Như vậy (6.6) là trường hợp $\lambda=1$, và hệ thức $E_t=\delta_t+\gamma\lambda E_{t+1}$ thay thừa số $\gamma$ của (6.6) bằng $\gamma\lambda$.

**Kiểm tra lại.** Trên lượt của Ví dụ 10.8, Bài tập 10.6(c) đã tính hai vế của (a) và được cùng giá trị $1{,}43$. Hai lỗi thường gặp: tính các $\delta_k$ với $w$ đã cập nhật trong lượt, khi đó $V(S_{t+1})$ trong $\delta_t$ và trong $E_{t+1}$ khác nhau và tổng có thêm các số hạng hiệu chỉnh như Bài tập 6.1 của sách; và gán giá trị $c\ne0$ cho trạng thái kết thúc trong $\delta_{T-1}$ mà vẫn dùng $G^\lambda_T=0$, khi đó $E_{T-1}=\delta_{T-1}-\gamma c$ và tổng sai số TD lớn hơn vế trái đúng $(\gamma\lambda)^{T-1-t}\gamma c$.
:::

### Bài tập 10.16. Các tỉ số sau một phần thưởng có kỳ vọng bằng 1

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 5.13, §5.9, trang 115; đẳng thức (5.11)–(5.14), trang 114.

::: exercise Bài tập 10.16 (Các tỉ số sau một phần thưởng có kỳ vọng bằng 1)
Lượt do chính sách hành vi $\pi_{\mathrm{old}}$ sinh ra trên một MDP có tập trạng thái và tập hành động hữu hạn, phần thưởng $\lvert R_{t+1}\rvert\le R_{\max}$, và kết thúc tại $T\le T_{\max}$ hầu chắc chắn. Chính sách đích $\pi_\theta$ thỏa điều kiện hỗ trợ; $\rho_k=\pi_\theta(A_k\mid S_k)/\pi_{\mathrm{old}}(A_k\mid S_k)$ khi $k<T$, $\rho_k=1$ và $R_{k+1}=0$ khi $k\ge T$, nên $\rho_{t:T-1}=\rho_{t:T_{\max}-1}$. Mọi kỳ vọng lấy theo lượt của $\pi_{\mathrm{old}}$.

Số hạng đầu của lợi tức có trọng số trong lấy mẫu quan trọng, (5.12) của sách, là
$$\begin{aligned}&\rho_{t:T-1}R_{t+1}\\&=\frac{\pi_\theta(A_t\mid S_t)}{\pi_{\mathrm{old}}(A_t\mid S_t)}\cdots\\&\quad\times\frac{\pi_\theta(A_{T-1}\mid S_{T-1})}{\pi_{\mathrm{old}}(A_{T-1}\mid S_{T-1})}\,R_{t+1}.\end{aligned}$$
Sách nhận xét rằng mỗi thừa số đứng sau phần thưởng có kỳ vọng $1$, (5.13) của sách:
$$\begin{aligned}&\mathbb E\Bigl[\frac{\pi_\theta(A_k\mid S_k)}{\pi_{\mathrm{old}}(A_k\mid S_k)}\Bigr]\\&=\sum_a\pi_{\mathrm{old}}(a\mid S_k)\\&\qquad\times\frac{\pi_\theta(a\mid S_k)}{\pi_{\mathrm{old}}(a\mid S_k)}\\&=\sum_a\pi_\theta(a\mid S_k)=1,\end{aligned}$$
và khẳng định (5.14) của sách:
$$\mathbb E[\rho_{t:T-1}R_{t+1}]=\mathbb E[\rho_{t:t}R_{t+1}] .$$

- (a) Trình bày các bước suy ra (5.14) từ (5.12).
- (b) Lặp lại lập luận cho số hạng thứ $k$ để được $\mathbb E[\rho_{t:T-1}R_{t+k}]=\mathbb E[\rho_{t:t+k-1}R_{t+k}]$, $k\ge1$, rồi suy ra $\mathbb E[\rho_{t:T-1}G_t]=\mathbb E[\tilde G_t]$ với
$$\tilde G_t=\sum_{k=1}^{T-t}\gamma^{k-1}\rho_{t:t+k-1}R_{t+k}.$$
:::

::: hint Gợi ý Bài tập 10.16
Viết (5.13) thành kỳ vọng có điều kiện: $\mathbb E[\rho_k\mid H_k]=1$. Bóc từng tỉ số từ thừa số cuối $\rho_{T_{\max}-1}$ về $\rho_{t+1}$, mỗi lần dùng tính chất tháp theo $H_k$.
:::

::: solution Lời giải Bài tập 10.16
**Câu (a).** Bước thứ nhất là viết (5.13) cho đúng điều kiện cần dùng. Với $k<T$, khi biết lịch sử $H_k$, trạng thái $S_k$ đã xác định và $A_k\sim\pi_{\mathrm{old}}(\cdot\mid S_k)$, nên
$$\begin{aligned}\mathbb E[\rho_k\mid H_k]&=\sum_{a\in\mathcal A^{\mathrm{old}}_{S_k}}\pi_\theta(a\mid S_k)\\&=1,\end{aligned}$$
trong đó đẳng thức cuối dùng điều kiện hỗ trợ. Với $k\ge T$, $\rho_k=1$. Vậy $\mathbb E[\rho_k\mid H_k]=1$ với mọi $k$. Mọi tỉ số bị chặn vì các tập hữu hạn, và $\lvert R_{t+1}\rvert\le R_{\max}$, nên các kỳ vọng dưới đây hữu hạn.

Bước thứ hai là bóc thừa số cuối. Cố định $t$ và lấy $k$ với $t+1\le k\le T_{\max}-1$. Phần thưởng $R_{t+1}$ và tích $\rho_{t:k-1}$ là hàm của $H_k$, vì chúng chỉ chứa các trạng thái, hành động và phần thưởng tới bước $k$. Theo tính chất tháp,
$$
\begin{aligned}
&\mathbb E[\rho_{t:k}R_{t+1}]\\
&=\mathbb E\bigl[\rho_{t:k-1}R_{t+1}\\
&\qquad\times\mathbb E[\rho_k\mid H_k]\bigr]\\
&=\mathbb E[\rho_{t:k-1}R_{t+1}].
\end{aligned}
$$
Bước thứ ba là lặp lại với $k=T_{\max}-1,T_{\max}-2,\dots,t+1$:
$$\begin{aligned}&\mathbb E[\rho_{t:T-1}R_{t+1}]\\&=\mathbb E[\rho_{t:T_{\max}-1}R_{t+1}]\\&=\mathbb E[\rho_{t:t}R_{t+1}],\end{aligned}$$
tức (5.14). Thừa số $\rho_t$ không bóc được, vì $R_{t+1}$ phụ thuộc $A_t$: $R_{t+1}$ không là hàm của $H_t$, nên tính chất tháp theo $H_t$ không tách được $\rho_t$ khỏi $R_{t+1}$. Đây là lý do sách nói chỉ thừa số đầu và phần thưởng có liên hệ với nhau.

**Câu (b).** Với $k\ge1$, $R_{t+k}$ và $\rho_{t:j-1}$ là hàm của $H_j$ khi $j\ge t+k$. Bóc các thừa số $\rho_j$ với $j=T_{\max}-1,\dots,t+k$ như ở (a) được
$$\mathbb E[\rho_{t:T-1}R_{t+k}]=\mathbb E[\rho_{t:t+k-1}R_{t+k}] .$$
Theo (5.11) của sách, $\rho_{t:T-1}G_t=\sum_{k=1}^{T-t}\gamma^{k-1}\rho_{t:T-1}R_{t+k}$. Vì $R_{t+k}=0$ khi $t+k>T$, tổng này bằng tổng hữu hạn theo $k=1,\dots,T_{\max}-t$ với số số hạng cố định, nên được lấy kỳ vọng từng số hạng:
$$
\begin{aligned}
&\mathbb E[\rho_{t:T-1}G_t]\\
&=\sum_{k=1}^{T_{\max}-t}\gamma^{k-1}\\
&\qquad\times\mathbb E[\rho_{t:t+k-1}R_{t+k}]\\
&=\mathbb E[\tilde G_t].
\end{aligned}
$$
Trong $\tilde G_t$, phần thưởng $R_{t+k}$ chỉ nhân với các tỉ số của những hành động chọn trước nó.

**Kiểm tra lại.** Khi $\pi_\theta=\pi_{\mathrm{old}}$, mọi tỉ số bằng $1$ và hai vế của (5.14) cùng bằng $\mathbb E[R_{t+1}]$. Khi lượt chỉ có một bước, $T=1$ và $t=0$, tích $\rho_{0:T-1}$ chỉ có $\rho_0$, nên (5.14) là đẳng thức hiển nhiên. Hai lỗi thường gặp: dùng $\mathbb E[\rho_k]=1$ không điều kiện rồi viết $\mathbb E[\rho_{t:k}R_{t+1}]=\mathbb E[\rho_{t:k-1}R_{t+1}]\,\mathbb E[\rho_k]$, một phép tách cần tính độc lập mà bài không có; và bóc cả $\rho_t$, được $\mathbb E[\rho_{t:T-1}R_{t+1}]=\mathbb E[R_{t+1}]$, sai vì kỳ vọng bên phải lấy theo hành động của $\pi_{\mathrm{old}}$ chứ không theo $\pi_\theta$.
:::

### Bài tập 10.17. Hàm điểm và ma trận Fisher của chính sách Gaussian

**Mức độ:** tính toán; mục tiêu học tập 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 13.4, §13.7, trang 336; đẳng thức (13.19), trang 335, và (13.20), trang 336.

::: exercise Bài tập 10.17 (Hàm điểm và ma trận Fisher của chính sách Gaussian)
Với hành động thực $a\in\mathbb R$, chính sách Gaussian (13.19) của sách có mật độ
$$\begin{aligned}&\pi(a\mid s,\theta)\\&=\frac1{\sigma(s,\theta)\sqrt{2\pi}}\\&\quad\times\exp\Bigl(-\frac{(a-\mu(s,\theta))^2}{2\sigma(s,\theta)^2}\Bigr),\end{aligned}$$
trong đó chữ $\pi$ trong $\sqrt{2\pi}$ là số $\pi\approx3{,}14159$. Tham số chia thành hai phần, $\theta=(\theta_\mu;\,\theta_\sigma)$, và theo (13.20) của sách,
$$\begin{aligned}\mu(s,\theta)&=\theta_\mu^\top x_\mu(s),\\\sigma(s,\theta)&=\exp\bigl(\theta_\sigma^\top x_\sigma(s)\bigr),\end{aligned}$$
với $x_\mu(s)$, $x_\sigma(s)$ là các véc-tơ đặc trưng của trạng thái.

- (a) Chứng minh rằng hàm điểm có hai phần
$$\begin{aligned}&\nabla_{\theta_\mu}\ln\pi(a\mid s,\theta)\\&\quad=\frac{a-\mu(s,\theta)}{\sigma(s,\theta)^2}\,x_\mu(s),\end{aligned}$$
$$\begin{aligned}&\nabla_{\theta_\sigma}\ln\pi(a\mid s,\theta)\\&\quad=\Bigl(\frac{(a-\mu(s,\theta))^2}{\sigma(s,\theta)^2}-1\Bigr)\\&\qquad\times x_\sigma(s).\end{aligned}$$
- (b) Với trạng thái $s$ cố định và $A\sim\pi(\cdot\mid s,\theta)$, tính ma trận Fisher $F_s=\mathbb E[\psi\psi^\top]$ của Định nghĩa 10.32, với $\psi$ là hàm điểm của câu (a) tại $A$ và kỳ vọng lấy theo mật độ thay cho tổng trên tập hành động hữu hạn. Viết $F_s$ thành ba khối: khối $\theta_\mu\theta_\mu$, khối $\theta_\sigma\theta_\sigma$ và khối chéo.
:::

::: hint Gợi ý Bài tập 10.17
(a) $\ln\pi=-\ln\sigma-\tfrac12\ln(2\pi)-\dfrac{(a-\mu)^2}{2\sigma^2}$, và $\ln\sigma=\theta_\sigma^\top x_\sigma(s)$. (b) Đặt $Z=(A-\mu)/\sigma$; khi đó $Z$ có phân phối chuẩn tắc, với $\mathbb EZ=\mathbb EZ^3=0$, $\mathbb EZ^2=1$, $\mathbb EZ^4=3$.
:::

::: solution Lời giải Bài tập 10.17
**Câu (a).** Mật độ dương với mọi $a$, nên $\nabla\pi/\pi=\nabla\ln\pi$ theo quy tắc đạo hàm hàm hợp. Lấy logarit của (13.19):
$$\begin{aligned}&\ln\pi(a\mid s,\theta)\\&=-\ln\sigma-\tfrac12\ln(2\pi)\\&\quad-\frac{(a-\mu)^2}{2\sigma^2},\end{aligned}$$
viết gọn $\mu=\mu(s,\theta)$, $\sigma=\sigma(s,\theta)$.

Phần $\theta_\mu$ chỉ đi vào $\mu=\theta_\mu^\top x_\mu(s)$, còn $\sigma$ không phụ thuộc $\theta_\mu$. Đây là tình huống của Mệnh đề 09.18 với $\phi(s)=x_\mu(s)$, nên $\nabla_{\theta_\mu}\ln\pi=\dfrac{a-\mu}{\sigma^2}\,x_\mu(s)$.

Phần $\theta_\sigma$ chỉ đi vào $\sigma=e^{\omega}$ với $\omega=\theta_\sigma^\top x_\sigma(s)$. Bài tập 09.7(a) cho $\partial\ln\pi/\partial\omega=(a-\mu)^2/\sigma^2-1$. Quy tắc hàm hợp với $\nabla_{\theta_\sigma}\omega=x_\sigma(s)$ cho
$$\begin{aligned}&\nabla_{\theta_\sigma}\ln\pi\\&=\Bigl(\frac{(a-\mu)^2}{\sigma^2}-1\Bigr)x_\sigma(s).\end{aligned}$$

**Câu (b).** Với $Z=(A-\mu)/\sigma$, câu (a) cho hai phần của hàm điểm
$$\begin{aligned}\psi_\mu&=\frac Z\sigma\,x_\mu(s),\\\psi_\sigma&=(Z^2-1)\,x_\sigma(s).\end{aligned}$$
Các véc-tơ $x_\mu(s)$, $x_\sigma(s)$ và số $\sigma$ không ngẫu nhiên khi $s$ cố định, nên chỉ cần các mô men của $Z$:

- khối $\theta_\mu\theta_\mu$: $\mathbb E[\psi_\mu\psi_\mu^\top]=\dfrac{\mathbb EZ^2}{\sigma^2}\,x_\mu x_\mu^\top=\dfrac1{\sigma^2}\,x_\mu x_\mu^\top$;
- khối $\theta_\sigma\theta_\sigma$: $\mathbb E[(Z^2-1)^2]=\mathbb EZ^4-2\,\mathbb EZ^2+1=3-2+1=2$, nên $\mathbb E[\psi_\sigma\psi_\sigma^\top]=2\,x_\sigma x_\sigma^\top$;
- khối chéo: $\mathbb E[\psi_\mu\psi_\sigma^\top]=\dfrac{\mathbb EZ^3-\mathbb EZ}{\sigma}\,x_\mu x_\sigma^\top=0$.

Vậy $F_s$ có hai khối trên đường chéo,
$$\begin{aligned}F_{\mu\mu}&=\sigma^{-2}\,x_\mu(s)x_\mu(s)^\top,\\F_{\sigma\sigma}&=2\,x_\sigma(s)x_\sigma(s)^\top,\end{aligned}$$
và hai khối ngoài đường chéo bằng $0$. Mỗi khối có hạng không quá $1$, nên khi số chiều của $\theta$ lớn hơn $2$, $F_s$ suy biến, như Nhận xét 10.35 mô tả cho softmax. Một bước $\Delta$ chỉ đổi $\theta_\mu$ làm trung bình đổi $\Delta\mu=x_\mu(s)^\top\Delta_\mu$ và giữ nguyên $\sigma$. KL giữa hai phân phối chuẩn cùng phương sai $\sigma^2$ là $(\Delta\mu)^2/(2\sigma^2)$, đúng bằng $\tfrac12\Delta^\top F_s\Delta$. Do đó, với cùng một mức đổi trung bình, chính sách có $\sigma$ nhỏ đổi nhiều hơn theo KL.

**Kiểm tra lại.** Hàm điểm có kỳ vọng $0$, như Mệnh đề 09.17: $\mathbb E[\psi_\mu]=\mathbb EZ\,x_\mu/\sigma=0$ và $\mathbb E[\psi_\sigma]=(\mathbb EZ^2-1)\,x_\sigma=0$. Ba lỗi thường gặp: quên số hạng $-\ln\sigma$ của hằng chuẩn hóa, được $\frac{(a-\mu)^2}{\sigma^2}x_\sigma$ thay cho $\bigl(\frac{(a-\mu)^2}{\sigma^2}-1\bigr)x_\sigma$; lấy đạo hàm theo $\sigma$ thay cho $\theta_\sigma$, được thêm thừa số $1/\sigma$; và dùng $\mathbb EZ^4=1$, được khối $\theta_\sigma\theta_\sigma$ bằng $0$.
:::

## Tài liệu tham khảo

- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 5.13 và (5.11)–(5.14), §5.9, trang 114–115 (Bài tập 10.16); (6.6), §6.1, trang 121 (Bài tập 10.15); Bài tập 7.6, (7.13) và (7.14), §7.4, trang 150–151 (Bài tập 10.14); Bài tập 12.2 và (12.3), §12.1, trang 290 (Bài tập 10.13); Bài tập 12.3, §12.2, trang 295, cùng (12.4), trang 290, và (12.6), trang 293 (Bài tập 10.15); Bài tập 13.4, (13.19) và (13.20), §13.7, trang 335–336 (Bài tập 10.17).
