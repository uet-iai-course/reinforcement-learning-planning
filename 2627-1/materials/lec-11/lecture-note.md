# Bài 11 — Các phương pháp gradient chính sách nâng cao

## Mục tiêu và kiến thức tiên quyết

- Tính được objective SPO và nhiễu SAM đúng dấu.
- Viết được target $n_t$ bước của A3C và phân biệt với A2C.
- Viết được target, Jacobian và hợp đồng replay của DDPG/MADDPG.
- Tính được target và phân biệt objective, cơ chế của SAC với TD3.
- Kiểm tra được support, occupancy, terminal/cutoff, mạng target, noise và dừng gradient.
- Nhận dạng cơ chế và giới hạn của D4PG, ACER, ACKTR, SVPG, IMPALA, PPG.

Tiên quyết từ Bài 10 (trang 4–43 của nguồn, không giảng lại): định lý gradient chính sách, REINFORCE, baseline, GAE, surrogate TRPO, PPO-Clip và các chi tiết triển khai PPO.

## Bản đồ chủ đề

| note-topic-id | chủ đề | nhóm | trang nguồn | thời lượng |
|---|---|---|---|---|
| `lec-11-topic-01` | Cầu nối từ PPO và hai tầng kết quả | cầu nối | 1–3, 4–43 | 7 phút |
| `lec-11-topic-02` | Tối ưu chính sách đơn giản (SPO) | cốt lõi | 44–47 | 12 phút |
| `lec-11-topic-03` | SAM+PPO và kiểm tra SPO/SAM | cốt lõi | 48–51 | 12 phút + 4 phút linh hoạt + 8 phút X01 |
| `lec-11-topic-04` | Actor–critic, A3C, A2C | cốt lõi | 53–54, 57–58 | 10 phút |
| `lec-11-topic-05` | Gradient chính sách khác chính sách | cốt lõi | 52, 55–56 | 8 phút |
| `lec-11-topic-06` | Định lý gradient chính sách tất định | cốt lõi | 59 | 7 phút |
| `lec-11-topic-07` | DDPG và hợp đồng replay/target | cốt lõi | 60–61 | 8 phút |
| `lec-11-topic-08` | D4PG, MADDPG và bài kiểm tra | cốt lõi + bổ sung | 62–64 | 10 + 12 (X02) phút |
| `lec-11-topic-09` | ACER và ACKTR | bổ sung | 65–67 | 6 phút |
| `lec-11-topic-10` | SAC và TD3 | cốt lõi | 68–71 | 18 phút |
| `lec-11-topic-11` | SVPG, IMPALA, PPG | bổ sung | 72–74 | 8 (+6 linh hoạt) phút |
| `lec-11-topic-12` | Bản đồ lựa chọn và bài tập tích hợp | cốt lõi | 75–77 | 4 + 10 (X03) phút |
| `lec-11-topic-13` | Năm phép kiểm và tuyến đọc tiếp | đọc thêm | 75–78 | — |

Tổng cốt lõi 110 phút, linh hoạt 10 phút, bài tập 30 phút (8 + 12 + 10).

## Ký hiệu và quy ước

- $w_t = \pi_\theta(A_t\mid S_t)/\pi_{\mathrm{old}}(A_t\mid S_t)$: tỷ số policy mới/cũ trong SPO; $\epsilon$: tham số tỷ số SPO.
- $\xi_{\mathrm{adv}}$: nhiễu tham số đối nghịch của SAM; $\rho$: bán kính SAM trong không gian tham số.
- $\rho_t$: tỷ số importance sampling trong phần khác chính sách; $\beta$: behavior policy; $\pi$: target policy.
- $d_{\rho_0,\gamma}^{\mu}(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr(S_t=s)$: occupancy chiết khấu chuẩn hóa của policy tất định.
- $m_t$: mặt nạ terminal thật ($m_t=0$ tại terminal, $m_t=1$ tại cutoff chưa terminal).
- $\operatorname{sg}(x)$: coi $x$ là hằng số khi lấy đạo hàm; dừng gradient qua $x$.
- $\theta,\phi$: tham số actor và critic online; $\bar\theta,\bar\phi$: tham số target; $\phi_{\mathrm{loc}}$: snapshot critic cục bộ của worker A3C, không phải mạng target.
- $D_\theta\mu\in\mathbb R^{d_a\times d_\theta}$: Jacobian actor; gradient tham số dùng $D_\theta\mu^\top\nabla_aQ$.
- $\alpha$: nhiệt độ entropy trong SAC; $u=\pi/\beta$: tỷ số hành động trong ACER; $u_t=\pi/\mu$: tỷ số importance sampling trong V-trace; $c_\xi>0$: cận clip nhiễu target của TD3.

<!-- note-topic-id: lec-11-topic-01 -->

## Cầu nối từ PPO và hai tầng kết quả học tập

**Vấn đề.** Bài 10 kết thúc ở PPO với ba hợp đồng thực hành. Bài 11 thay từng thành phần của hợp đồng đó: mục tiêu tỷ số, hình học cập nhật, nguồn dữ liệu, critic, chính sách hành vi và kiến trúc phân tán.

**Trực giác.** Ba dữ kiện mang từ PPO sang: tỷ số $w_t=\pi_\theta(A_t\mid S_t)/\pi_{\mathrm{old}}(A_t\mid S_t)$; dấu lợi thế quyết định hướng cập nhật ($\widehat A_t>0$ tăng xác suất, $\widehat A_t<0$ giảm xác suất); batch cũ giữ $\log\pi_{\mathrm{old}}$, lợi thế và target cố định trong các epoch.

**Hai tầng kết quả học tập.**

- Tầng tính và viết: objective SPO và nhiễu SAM; target của A3C–A2C; target, Jacobian và replay của DDPG–MADDPG; target của SAC–TD3 cùng các phép kiểm support, terminal/cutoff, target/noise và dừng gradient.
- Tầng nhận dạng và giới hạn: D4PG, ACER, ACKTR, SVPG, IMPALA, PPG qua cơ chế, dữ liệu và phạm vi; không yêu cầu tái tạo thuật toán đầy đủ.

Trang 4–43 của nguồn chỉ là tiên quyết Bài 10; nội dung mới bắt đầu từ trang 44.

**Nguồn:** tr. 1–3; tr. 4–43 (tiên quyết Bài 10); tr. 44–77 (tổ chức lại theo tải học tập).

**Nối ra:** ba dữ kiện trên đủ để mở SPO ở topic kế tiếp.


<!-- note-topic-id: lec-11-topic-02 -->

## Tối ưu chính sách đơn giản (SPO)

**Vấn đề.** PPO-Clip có thể tắt gradient theo mẫu: khi tỷ số vượt biên clip theo hướng thuận lợi, mẫu đó ngừng đóng góp gradient policy. SPO giữ tính đơn giản bậc nhất nhưng ràng buộc tỷ số trực tiếp hơn.

**Trực giác.** Thay đoạn phẳng của clip bằng penalty bậc hai trên tỷ số. Với $A>0$, lực kéo đổi dấu sau $1+\epsilon$; với $A<0$, lực kéo đổi dấu trước $1-\epsilon$. Nghiệm nội suy là nghiệm của $\partial f/\partial w=0$, nên điều kiện $0<\epsilon\le1$ bảo đảm $w^*=1-\epsilon\ge0$ khi $A<0$ (tỷ số đích không âm). Tỷ số luôn được tính từ policy mới trên hành động của batch cũ.

**Ví dụ tính tay.** Cho $\epsilon=0{,}2$ và $f(w,A)=wA-\frac{|A|}{2\epsilon}(w-1)^2$:

- $A=2$: tỷ số đích $w^*=1{,}2$; $f(1{,}2,2)=2{,}4-0{,}2=2{,}2$.
- $A=-2$: tỷ số đích $w^*=0{,}8$; $f(0{,}8,-2)=-1{,}6-0{,}2=-1{,}8$.

Đây là giá trị objective một mẫu, không phải return môi trường.

**Hình thức.** Với $r_t(\theta)=\pi_\theta(a_t\mid s_t)/\pi_{\mathrm{old}}(a_t\mid s_t)$:

$$J_{\mathrm{SPO}}(\theta)=\mathbb E_t\!\left[r_t(\theta)\widehat A_t-\frac{|\widehat A_t|}{2\epsilon}\bigl(r_t(\theta)-1\bigr)^2\right].$$

Đạo hàm theo $w$: $\partial f/\partial w=A-\frac{|A|}{\epsilon}(w-1)$, nên với $A\ne0$ thì $w^*=1+\operatorname{sign}(A)\,\epsilon$ và đạo hàm bậc hai âm. Điều kiện $0<\epsilon\le1$ bảo đảm với $A<0$ rằng $w^*=1-\epsilon\ge0$, tức tỷ số đích không âm. Với $A=0$: $f(w,0)=0$ với mọi $w\ge0$, nghiệm không duy nhất. Với hành động liên tục nhiều chiều, $w$ dùng joint log-probability.

**Ứng dụng.** SPO chỉ thay hạng policy loss trong pipeline PPO; giữ batch cũ, critic, lợi thế và lịch cập nhật. Không tính lại lợi thế giữa các epoch trên cùng batch. Nguồn báo cáo SPO mạnh với kiến trúc lớn.

**Giới hạn.** Kết quả trên là thực nghiệm theo giao thức của paper, không phải bảo đảm tổng quát.

**Kiểm tra.** Với $\epsilon=0{,}2$, $A=2$: $w^*=1{,}2$; $A=-2$: $w^*=0{,}8$; $A=0$: mọi $w\ge0$.

**Nguồn:** tr. 44–47; Xie et al. (2025).

**Nối ra:** SPO sửa mục tiêu tỷ số; SAM sửa hình học cập nhật trong không gian tham số.


<!-- note-topic-id: lec-11-topic-03 -->

## SAM+PPO và kiểm tra SPO/SAM

**Vấn đề.** Hai tham số có return danh nghĩa gần nhau nhưng giá trị xấu nhất trong cùng bán kính có thể khác nhau. Tối thiểu hóa nhận biết độ sắc (Sharpness-Aware Minimization, SAM) ưu tiên vùng giữ return khi tham số bị nhiễu.

**Trực giác.** Đỉnh sắc: return cao danh nghĩa nhưng dễ sụp trong lân cận. Vùng phẳng: return cao trên cả lân cận bán kính $\rho$. SAM+PPO chuyển ý tưởng này sang không gian tham số policy.

**Ví dụ tính tay.** Cho $g=(3,4)$ và $\rho=0{,}1$: $\|g\|_2=5$, nên

$$\xi_{\mathrm{adv}}=-\rho\frac{g}{\|g\|_2}=-0{,}1\,(3/5,\,4/5)=(-0{,}06,\,-0{,}08).$$

Nhiễu đối nghịch đi ngược gradient reward; gradient cập nhật được đánh giá tại $\theta+\xi_{\mathrm{adv}}$. Ví dụ chỉ kiểm dấu, hướng và chuẩn; chưa chứng minh return sau cập nhật tăng.

**Hình thức.** SAM giải gần đúng bài toán

$$\max_\theta\ \min_{\|\xi\|_2\le\rho}J(\theta+\xi),\qquad \xi_{\mathrm{adv}}=-\rho\frac{g}{\|g\|_2},\quad g=\nabla_\theta J(\theta).$$

Ba bước: tính $g$ tại $\theta$; tạo $\xi_{\mathrm{adv}}$ theo phía làm giảm reward; coi $\xi_{\mathrm{adv}}$ cố định và cập nhật bằng $\nabla_\theta J(\theta+\xi_{\mathrm{adv}})$. Nếu $g=0$, hướng chuẩn hóa không xác định và cài đặt cần quy ước.

**Ứng dụng.** Actor tất định $\mu_\theta$ và Jacobian $D_\theta\mu$ sẽ được đặt nền ở topic 06. Nhiễu tham số chỉ cho độ nhạy hành động thuận:

$$\|\mu_{\theta+\xi}(s)-\mu_\theta(s)\|\ \lesssim\ \|D_\theta\mu_\theta(s)\|\,\|\xi\|.$$

Đi từ lân cận tham số đến bao phủ cục bộ nhiễu hành động cần: ánh xạ bậc nhất hợp lệ, Jacobian được chặn, đủ hạng và singular value nhỏ nhất được chặn xa 0; claim trong paper dùng policy Gaussian covariance cố định.

**Giới hạn.** Nó không chứng minh độ bền với mọi nhiễu trong một quả cầu hành động, và không có quan hệ hệ quả với thay đổi transition hoặc reward. Bằng chứng thực nghiệm giới hạn ở ba tác vụ MuJoCo dưới một giao thức cụ thể; không tạo bảo đảm cho mọi tác vụ, kiến trúc hoặc dạng dịch chuyển phân phối.

::: exercise X01 — SPO và SAM (8 phút)
1. Với $\epsilon=0{,}2$, tìm $w^*$ cho $A=2$, $A=-2$ và mô tả ca $A=0$.
2. Tính $\xi_{\mathrm{adv}}$ khi $g=(3,4)$, $\rho=0{,}1$.
3. Nêu đủ điều kiện để đi từ lân cận tham số đến bao phủ cục bộ nhiễu hành động.
:::

::: hint
Câu 1: giải $\partial f/\partial w=0$. Câu 2: chuẩn hóa $g$ rồi nhân $-\rho$. Câu 3: các điều kiện đi cùng nhau, không phải lựa chọn "Jacobian hoặc rank".
:::

::: solution
1. $w^*=1{,}2$ cho $A=2$; $w^*=0{,}8$ cho $A=-2$; khi $A=0$, $f(w,0)=0$ với mọi $w\ge0$.
2. $\|g\|_2=5$, $\xi_{\mathrm{adv}}=(-0{,}06,-0{,}08)$.
3. Cần ánh xạ bậc nhất hợp lệ, Jacobian được chặn, đủ hạng và singular value nhỏ nhất được chặn xa 0; policy Gaussian trong claim dùng covariance cố định. Các điều kiện chỉ cho liên hệ cục bộ; không suy ra độ bền với thay đổi transition hoặc reward.
:::

**Nguồn:** tr. 48–51; Lee & Yoon (2025); bài tập xây từ tr. 44–51.

**Nối ra:** sau cụm SPO/SAM, quay về actor–critic core trước khi mở replay.


<!-- note-topic-id: lec-11-topic-04 -->

## Actor–critic, A3C và A2C

**Vấn đề.** Return Monte Carlo có phương sai cao; cần tín hiệu dày hơn cho actor mà không phá tính vô chệch hoàn toàn.

**Trực giác.** Actor $\pi_\theta(a\mid s)$ chọn hành động; critic $V_\phi(s)$ ước lượng return tương lai và làm baseline. Critic biến phản hồi trễ thưa thành tín hiệu học dày hơn.

**Hình thức.** Hai mục tiêu riêng, có thể chia sẻ backbone:

$$\mathcal L_{\mathrm{actor}}=-\log\pi_\theta(A_t\mid S_t)\operatorname{sg}(\widehat A_t),\qquad \mathcal L_{\mathrm{critic}}=(V_\phi(S_t)-\operatorname{sg}(\widehat V_t))^2.$$

$\operatorname{sg}$ dừng gradient; lợi thế và target phải dừng gradient trên đúng đường. Tín hiệu bootstrap giảm phương sai nhưng đưa sai số critic vào actor.

**A3C.** Asynchronous Advantage Actor–Critic dùng snapshot critic cục bộ $\phi_{\mathrm{loc}}$ — bản tham số cục bộ của worker khi rollout, không phải mạng target cập nhật chậm. Đặt $n_t$ là số chuyển tiếp thực đến terminal hoặc cuối rollout; $m_t=1$ chỉ khi điểm cắt chưa terminal:

$$\widehat V_t^{(n)}=\sum_{k=0}^{n_t-1}\gamma^kR_{t+k+1}+\gamma^{n_t}m_t\operatorname{sg}\!\left(V_{\phi_{\mathrm{loc}}}(S_{t+n_t})\right),\qquad \widehat A_t=\widehat V_t^{(n)}-V_{\phi_{\mathrm{loc}}}(S_t).$$

Bootstrap dừng gradient; terminal đặt $m_t=0$ và không bootstrap qua reset; cutoff chưa terminal đặt $m_t=1$. Worker có thể rollout bằng bản tham số cũ; gradient đến server trễ, tạo staleness. Song song hóa giảm tương quan theo thời gian nhưng không làm các mẫu độc lập chỉ vì có nhiều worker.

**A2C.** Ghép rollout của nhiều môi trường thành một batch trước cập nhật, đồng bộ.

| | A3C | A2C |
|---|---|---|
| cập nhật | bất đồng bộ | đồng bộ |
| staleness giữa worker | có | loại |
| phần cứng | worker độc lập | vectorization thuận tiện |

A2C không mặc nhiên tốt hơn A3C; hai cách tổ chức đổi throughput, độ trễ và đặc tính batch.

**Kiểm tra.** Target A3C dùng $\phi_{\mathrm{loc}}$, mặt nạ $m_t$ đúng loại điểm cắt, và hạng bootstrap bị $\operatorname{sg}$.

**Nguồn:** tr. 53–54, 57–58; Konda & Tsitsiklis (2000); Mnih et al. (2016).

**Nối ra:** actor–critic on-policy là nền để thêm dữ liệu behavior khác target.


<!-- note-topic-id: lec-11-topic-05 -->

## Gradient chính sách khác chính sách

**Vấn đề.** On-policy chỉ dùng dữ liệu từ chính policy đang cập nhật. Muốn tái dùng replay, phải sửa sai khác phân phối giữa behavior policy $\beta$ sinh dữ liệu và target policy $\pi$ cần đánh giá.

**Trực giác.** Tỷ số hành động sửa phân phối có điều kiện tại một trạng thái cố định; nó không tự sửa phân bố trạng thái trong replay.

**Ví dụ tính tay.** Lấy mẫu quan trọng (IS) với $\beta=(0{,}5,0{,}5)$, $\pi=(0{,}8,0{,}2)$, $f=(2,0)$:

$$\mathbb E_\pi[f]=0{,}8\times2=1{,}6,$$
$$\mathbb E_\beta\!\left[\frac{\pi(A\mid s)}{\beta(A\mid s)}f(A)\right]=0{,}5\times1{,}6\times2+0{,}5\times0{,}4\times0=1{,}6.$$

Hai kỳ vọng bằng nhau tại $s$ cố định khi $\pi(a\mid s)>0\Rightarrow\beta(a\mid s)>0$.

**Hình thức.** Với $\rho_t=\pi_\theta(a_t\mid s_t)/\beta(a_t\mid s_t)$:

$$\mathbb E_{a\sim\pi}[f(a)]=\mathbb E_{a\sim\beta}\!\left[\frac{\pi(a\mid s)}{\beta(a\mid s)}f(a)\right].$$

Trọng số lớn gây phương sai cao; cắt hoặc truncate giảm phương sai nhưng tạo chệch.

**Ứng dụng và giới hạn.** Ba bài toán khác chính sách không đồng nhất: (i) quỹ đạo — tích tỷ số qua thời gian có thể tăng phương sai; (ii) replay actor–critic — target network không tự sửa occupancy mismatch; (iii) gradient tất định — định lý phải nêu rõ phân bố trạng thái. Action-IS không tự sửa trajectory/occupancy mismatch; identity một hành động không chứng minh replay hoàn toàn không chệch.

**Kiểm tra.** Trước khi dùng IS: kiểm support $\pi(a\mid s)>0\Rightarrow\beta(a\mid s)>0$; nếu $\beta$ không lấy mẫu một hành động mà $\pi$ dùng, tỷ số không thể khôi phục phần đó.

**Nguồn:** tr. 52, 55–56; Precup, Sutton & Singh (2000); Degris, White & Sutton (2012).

**Nối ra:** DPG ở topic kế chọn một hợp đồng occupancy cụ thể cho gradient tất định.


<!-- note-topic-id: lec-11-topic-06 -->

## Định lý gradient chính sách tất định (DPG)

**Vấn đề.** Với hành động liên tục, tích phân trên phân phối hành động nhiều chiều tốn kém. Actor tất định $a=\mu_\theta(s)$ tránh tích phân đó nhưng cần gradient đi qua critic khả vi theo hành động.

**Trực giác.** Ví dụ vô hướng trước: $\mu_\theta(s)=2\theta$, $\partial_aQ(s,a)=3$, nên theo chain rule $\partial_\theta Q(s,\mu_\theta(s))=2\times3=6$.

**Hình thức.** Với $D_\theta\mu_\theta(s)\in\mathbb R^{d_a\times d_\theta}$ và occupancy chuẩn hóa $d_{\rho_0,\gamma}^{\mu}$:

$$\nabla_\theta J(\theta)=\frac1{1-\gamma}\mathbb E_{S\sim d_{\rho_0,\gamma}^{\mu}}\!\left[D_\theta\mu_\theta(S)^\top\nabla_aQ^\mu(S,a)\big|_{a=\mu_\theta(S)}\right].$$

Kích thước: Jacobian actor $d_a\times d_\theta$; gradient $Q$ theo hành động $d_a$; chuyển vị nhân gradient cho vector $d_\theta$. Hệ số $1/(1-\gamma)$ biến mất nếu dùng occupancy không chuẩn hóa.

**Ứng dụng và giới hạn.** Actor tất định không tự khám phá; behavior policy cần noise hoặc cơ chế khám phá riêng. Định lý gắn với occupancy đã khai báo; đổi quy ước occupancy đổi hệ số.

**Kiểm tra.** Hai nhân tử cùng shape $d_a$; kết quả shape $d_\theta$; hệ số khớp quy ước occupancy.

**Nguồn:** tr. 59; Silver et al. (2014).

**Nối ra:** DDPG đưa định lý này vào mạng sâu với replay và target network.


<!-- note-topic-id: lec-11-topic-07 -->

## DDPG và hợp đồng replay/target

**Vấn đề.** DPG trên mạng sâu cần ổn định: dữ liệu cũ, target trôi và khám phá phải được tách rõ.

**Trực giác.** Hai việc khác nhau: thu dữ liệu bằng $A_t=\mu_\theta(S_t)+\zeta_t$ (behavior noise để khám phá); tạo target bằng $\mu_{\bar\theta}$ không có behavior noise. Noise làm mượt target của TD3 ở phần sau là cơ chế thứ ba, khác hai loại trên.

**Hình thức.** Trên replay $\mathcal D$:

$$y=R_{t+1}+\gamma m_tQ_{\bar\phi}(S_{t+1},\mu_{\bar\theta}(S_{t+1})),\qquad \mathcal L_Q=\mathbb E_{\mathcal D}[(Q_\phi-\operatorname{sg}(y))^2],$$

$$g_\theta^{\mathcal D}=\mathbb E_{S\sim\mathcal D}\!\left[D_\theta\mu_\theta(S)^\top\nabla_aQ_\phi(S,a)\big|_{a=\mu_\theta(S)}\right],\qquad D_\theta\mu\in\mathbb R^{d_a\times d_\theta}.$$

Kỳ vọng trên replay là surrogate off-policy thực hành, không phải ước lượng không chệch của định lý on-policy ở topic 06. Actor gradient đi qua critic online nhưng critic đứng yên trên đường actor; target actor/critic và $y$ đều dừng gradient.

**Thuật toán.** (1) lấy minibatch từ replay; (2) tính $y$ bằng hai mạng target; (3) cập nhật critic online theo bình phương sai số; (4) cập nhật actor online qua $Q_\phi$; (5) cập nhật mềm $\bar\theta\leftarrow\tau\theta+(1-\tau)\bar\theta$ và tương tự cho $\bar\phi$.

**Ứng dụng và giới hạn.** Tái sử dụng mẫu mạnh, hợp điều khiển liên tục; nhạy với lỗi critic và noise khám phá, có thể overestimate và khai thác artifact của critic. Không có bảo đảm ổn định tổng quát cho mạng sâu.

**Kiểm tra.** Behavior noise chỉ ở đường thu dữ liệu; target không mang noise hành vi; mọi đại lượng target bị $\operatorname{sg}$; mặt nạ $m_t$ là terminal thật.

**Nguồn:** tr. 60–61; Lillicrap et al. (2016).

**Nối ra:** D4PG và MADDPG mở rộng DDPG theo hai hướng khác nhau.


<!-- note-topic-id: lec-11-topic-08 -->

## D4PG, MADDPG và bài kiểm tra khác chính sách

**D4PG (mức nhận dạng).** Distributed Distributional DPG thêm actor phân tán, critic phân phối, return $n$ bước và replay ưu tiên. Target:

$$Y_t=\sum_{k=0}^{n_t-1}\gamma^kR_{t+k+1}+\gamma^{n_t}m_tZ_{\bar\phi}(S_{t+n_t},\mu_{\bar\theta}(S_{t+n_t})),$$

chiếu $\Pi Y_t$ lên support phân phối trước loss critic. $Z$ mô tả phân phối return aleatoric, không phải bất định tham số; phép chiếu phụ thuộc biểu diễn phân phối của critic.

**MADDPG (cốt lõi CTDE).** Huấn luyện tập trung, thực thi phân tán: actor $i$ chỉ nhận $o_i$; critic dùng trạng thái chung $x$ và mọi hành động.

$$\nabla_{\theta_i}J_i\approx\mathbb E_{\mathcal D}\!\left[D_{\theta_i}\mu_i(o_i)^\top\nabla_{a_i}Q_i(x,a_1,\ldots,a_n)\big|_{a_i=\mu_i(o_i)}\right],\qquad D_{\theta_i}\mu_i\in\mathbb R^{d_{a_i}\times d_{\theta_i}}.$$

Target dùng mọi target actor:

$$y_i=R_{i,t+1}+\gamma m_tQ_{i,\bar\phi_i}\!\left(x',\mu_{1,\bar\theta_1}(o'_1),\ldots,\mu_{n,\bar\theta_n}(o'_n)\right).$$

Replay lưu thông tin chung cần cho critic; mỗi actor chỉ nhận gradient qua thành phần hành động của mình; không thay hành động agent khác bằng hành động online trong target nếu thuật toán xác định dùng mạng target; mặt nạ terminal phản ánh quy ước episode chung hoặc terminal riêng.

**So sánh.**

| | D4PG | MADDPG |
|---|---|---|
| giới hạn | critic scalar và throughput | agent khác làm môi trường đổi |
| mở rộng | return distribution, actor phân tán | critic tập trung |
| thực thi | actor tất định | actor cục bộ từng agent |

Hai phương pháp cùng kế thừa deterministic actor–critic nhưng không hoán đổi mục đích: distributional critic không giải phối hợp đa agent; centralized critic không tự tạo phân phối return.

::: exercise X02 — Off-policy và DDPG (12 phút)
1. Kiểm support và tính ví dụ IS với $\beta=(0{,}5,0{,}5)$, $\pi=(0{,}8,0{,}2)$, $f=(2,0)$.
2. Với $d_a=2$, $d_\theta=5$, ghi shape $D_\theta\mu$ và $D_\theta\mu^\top\nabla_aQ$.
3. Tính target DDPG khi $R=1$, $\gamma=0{,}9$, $Q_{\bar\phi}=4$: một ca cutoff chưa terminal và một ca terminal.
:::

::: hint
Câu 1: kiểm $\beta(a\mid s)>0$ ở mọi hành động mà $\pi$ dùng. Câu 3: cutoff chưa terminal dùng $m=1$ và bootstrap từ quan sát cuối hợp lệ; terminal dùng $m=0$.
:::

::: solution
1. Support thỏa vì $\beta>0$ ở hai hành động; $\mathbb E_\pi[f]=\mathbb E_\beta[\rho f]=1{,}6$.
2. $D_\theta\mu\in\mathbb R^{2\times5}$; $D_\theta\mu^\top\nabla_aQ\in\mathbb R^{5}$.
3. Cutoff chưa terminal: $y=1+0{,}9\times4=4{,}6$; terminal: $y=1$. Kỳ vọng replay trong DDPG vẫn là surrogate thực hành, không biến thành định lý on-policy không chệch.
:::

**Nguồn:** tr. 62–64; Barth-Maron et al. (2018); Lowe et al. (2017); bài tập xây từ tr. 55–64.

**Nối ra:** hai cơ chế định hướng tiếp theo sửa replay (ACER) và độ cong (ACKTR).


<!-- note-topic-id: lec-11-topic-09 -->

## ACER và ACKTR

**ACER (mức nhận dạng).** Actor-Critic with Experience Replay dùng replay với truncated importance sampling và bù phần dư. Với support $\pi(a\mid s)>0\Rightarrow\beta(a\mid s)>0$, đặt $u=\pi/\beta$, ngưỡng $\bar c>0$, $c=\min(\bar c,u)$:

$$\mathbb E_\beta[uf]=\mathbb E_\beta[cf]+\mathbb E_\pi\!\left[\left(1-\frac{\bar c}{u}\right)_+f\right].$$

$f$ là hạng gradient hoặc tín hiệu cần hiệu chỉnh tại trạng thái cố định; với mẫu $\beta$ có xác suất dương thì $u$ xác định, và hạng correction bằng không theo miền positive-part khi $u=0$. Đây là identity định hướng; Retrace và trust-region của ACER không được trình bày.

**ACKTR (mức nhận dạng).** Actor Critic using Kronecker-Factored Trust Region dùng lõi K-FAC theo từng layer:

$$F_{\mathrm{layer}}\approx K_{\mathrm{in}}\otimes K_{\mathrm{out}},\qquad (F_{\mathrm{layer}}+\eta I)^{-1}g.$$

Actor dùng metric Fisher của policy; critic dùng xấp xỉ Gauss–Newton. Công thức chỉ là lõi K-FAC, chưa gồm damping, chuẩn hóa bước theo trust region và lịch cập nhật thống kê.

**So sánh.**

| | ACER | ACKTR |
|---|---|---|
| dữ liệu | replay khác chính sách | rollout actor–critic |
| cơ chế | truncated IS + correction | K-FAC curvature |
| rủi ro chính | phương sai, xấp xỉ correction | chi phí và sai số curvature |

ACER sửa sai khác phân phối hành động của replay; ACKTR sửa hình học bước cập nhật. Tên "trust region" hoặc "natural gradient" không làm hai thuật toán tương đương TRPO.

**Nguồn:** tr. 65–67; Wang et al. (2017); Wu et al. (2017).

**Nối ra:** quay lại core với hai họ continuous replay: SAC và TD3.


<!-- note-topic-id: lec-11-topic-10 -->

## SAC và TD3

**Vấn đề.** Hai bài toán khác nhau: SAC đổi objective — actor stochastic tối ưu return cùng entropy; TD3 giảm lỗi function approximation và overestimation của actor deterministic. Cả hai có thể dùng twin critics và replay; entropy không phải cơ chế sửa target.

**Trực giác.** Phần giao là phép min hai critic; policy và objective khác nhau. SAC lấy mẫu từ policy và dùng soft target trừ $\alpha\log\pi$; TD3 làm mượt target action và cập nhật actor/target trễ.

**Ví dụ tính tay.** Cho $R=1$, $\gamma=0{,}9$, $m=1$; sau khi tạo hành động target, hai critic cho $4$ và $5{,}5$:

$$y=1+0{,}9\min(4,5{,}5)=4{,}6.$$

Nếu chuyển tiếp kết thúc thật, $m=0$ và target bằng $1$. Ví dụ không chứng minh twin critics luôn đánh giá thấp hoặc tốt hơn; tác dụng thống kê cần xét qua dữ liệu và quá trình học.

**SAC (biến thể hiện đại, không cần mạng $V$ riêng).** Với $A'\sim\pi_\theta(\cdot\mid S')$:

$$y=R+\gamma m\left[\min_jQ_{\bar\phi_j}(S',A')-\alpha\log\pi_\theta(A'\mid S')\right],$$

$$\mathcal L_\pi=\mathbb E\!\left[\alpha\log\pi_\theta(A\mid S)-\min_jQ_{\phi_j}(S,A)\right].$$

$\alpha>0$ cố định trong bài; actor stochastic dùng reparameterization; target critic dừng gradient; critic đứng yên trên đường actor; automatic temperature tuning ngoài phạm vi bài.

**TD3.** Target policy smoothing và cập nhật trì hoãn:

$$\xi\sim\operatorname{clip}(\mathcal N(0,\sigma^2I),-c_\xi,c_\xi),\quad \widetilde A'=\operatorname{clip}(\mu_{\bar\theta}(S')+\xi,a_{\min},a_{\max}),$$

$$y=R+\gamma m\min_jQ_{\bar\phi_j}(S',\widetilde A'),\qquad J_\mu=\mathbb E_{\mathcal D}[Q_{\phi_1}(S,\mu_\theta(S))].$$

Cập nhật hai critic mỗi bước; cập nhật actor và các target mỗi $d$ bước critic. Actor objective dùng critic thứ nhất $Q_{\phi_1}$, không dùng min trong gradient actor. Behavior noise thu replay là đại lượng khác $\xi$ target smoothing; sau khi noise Gaussian được clip, hành động còn được clip theo miền action.

**So sánh.**

| | SAC | TD3 |
|---|---|---|
| actor | stochastic | deterministic |
| objective | return + entropy | return qua critic |
| khám phá | phân phối policy | behavior noise bên ngoài |
| target | soft value, twin critics | min twin critics + smoothing noise |
| nhịp actor | theo recipe SAC | trì hoãn mỗi $d$ bước critic |

Cùng dùng replay và twin critics không làm hai thuật toán tương đương: SAC tối ưu policy stochastic có entropy; TD3 dùng actor deterministic, noise khám phá bên ngoài khi thu dữ liệu, noise riêng khi làm mượt target và lịch cập nhật actor bị trì hoãn.

**Kiểm tra.** Tính target $y=1+0{,}9\min(4,5{,}5)=4{,}6$; terminal cho $y=1$; kiểm $\alpha\log\pi$ chỉ ở SAC và $\xi$ chỉ ở TD3.

**Nguồn:** tr. 68–71; Haarnoja et al. (2018); Fujimoto, van Hoof & Meger (2018).

**Nối ra:** ba cơ chế khảo sát tiếp theo: đa dạng policy, policy lag và tách pha policy–value.


<!-- note-topic-id: lec-11-topic-11 -->

## SVPG, IMPALA và PPG

Mức nhận dạng: mỗi phương pháp có một phương trình hoặc cơ chế định nghĩa; không yêu cầu triển khai đầy đủ.

**SVPG.** Stein Variational Policy Gradient huấn luyện một quần thể policy như các particle; kernel giữ đa dạng:

$$\Delta\theta_i=\frac1n\sum_{j=1}^n\left[k(\theta_j,\theta_i)\frac1\alpha\nabla_{\theta_j}J(\theta_j)+\nabla_{\theta_j}k(\theta_j,\theta_i)\right].$$

$\theta_i$ là particle policy; $k$ là kernel; $\alpha>0$ điều chỉnh khai thác–đa dạng; hệ số $1/n$ là quy ước trung bình và scale bước, không đổi hướng tổng. Công thức giả sử prior đều; với prior không đều, thêm gradient log-prior. Hữu ích khi khám phá và đa dạng policy quý giá, ví dụ reward thưa hoặc đa mode.

**IMPALA.** Kiến trúc actor–learner phân tán: behavior $\mu$ ở actor, learner policy $\pi$; cần $\pi(a\mid s)>0\Rightarrow\mu(a\mid s)>0$. V-trace:

$$u_t=\frac{\pi(A_t\mid S_t)}{\mu(A_t\mid S_t)},\quad \rho_t=\min(\bar\rho,u_t),\quad c_t=\min(\bar c,u_t),\quad \bar\rho\ge\bar c,$$

$$\delta_t=\rho_t[R_{t+1}+\gamma_tV(S_{t+1})-V(S_t)],\qquad \gamma_t=\gamma m_t.$$

$\rho_t$ sửa residual hiện tại; $c_t$ truyền trace; $m_t=0$ tại terminal. Target đầy đủ là $v_s=V(S_s)+\sum_{t=s}^{s+n-1}\bigl(\prod_{i=s}^{t-1}\gamma_ic_i\bigr)\delta_t$. Hai ngưỡng cắt đổi target; V-trace không phải trajectory importance sampling không cắt.

**PPG.** Phasic Policy Gradient tách pha policy (tối ưu kiểu PPO) và pha phụ trợ học value head với cloning KL:

$$\mathcal L_{\mathrm{joint}}=\mathcal L_{\mathrm{aux}}+\beta_{\mathrm{clone}}\,\mathbb E[D_{\mathrm{KL}}(\pi_{\mathrm{old}}\,\|\,\pi_\theta)].$$

$\pi_{\mathrm{old}}$ trước pha và target value được đóng băng trong pha phụ trợ; cloning KL hạn chế làm méo policy trước pha.

**Tổng hợp.**

| phương pháp | bài toán | cơ chế nhận dạng |
|---|---|---|
| SVPG | đa dạng policy | gradient return + lực đẩy kernel |
| IMPALA | throughput và policy lag | actors phân tán + V-trace |
| PPG | can thiệp policy–value | hai pha + cloning KL |

Ba phương pháp nhắm ba bài toán khác nhau nên không xếp hạng hiệu năng.

**Nguồn:** tr. 72–74; Liu et al. (2017); Espeholt et al. (2018); Cobbe et al. (2021).

**Nối ra:** bản đồ tổng hợp đặt tất cả các họ cạnh nhau theo dữ liệu, actor và cơ chế.


<!-- note-topic-id: lec-11-topic-12 -->

## Bản đồ lựa chọn và bài tập tích hợp

| họ | dữ liệu | actor | cơ chế nhận dạng |
|---|---|---|---|
| A3C/A2C | rollout | stochastic | bất đồng bộ / đồng bộ |
| SPO/PPG | rollout | stochastic | objective tỷ số / hai pha |
| SAM/ACKTR | không do cơ chế xác định | không do cơ chế xác định | lân cận tham số / K-FAC |
| ACER/SAC | replay | stochastic | correction / entropy |
| DDPG/TD3/D4PG | replay | deterministic | target / twin-delayed / phân phối |
| MADDPG | replay + joint info | deterministic | CTDE |
| IMPALA | actor phân tán, lag | stochastic | V-trace |
| SVPG | quần thể | mỗi particle một policy | kernel repulsion |

Các hàng không loại trừ nhau: D4PG vừa replay vừa phân tán; SVPG có thể bọc nhiều loại policy; SAM và ACKTR mô tả cách tối ưu, không ấn định dữ liệu hay actor. Lựa chọn là có điều kiện theo dữ liệu, actor, cập nhật và cơ chế sửa sai — không có khuyến nghị "mặc định tốt nhất" phổ quát.

::: exercise X03 — Tính target rồi chọn họ (10 phút)
1. TD3 có $R=2$, $\gamma=0{,}95$, $m=1$, hai target critic cho $3$ và $4$: tính $y$.
2. Continuous replay: chọn SAC hoặc TD3 và nêu tradeoff.
3. Đa tác tử cần CTDE: chọn họ nào?
4. Actor phân tán có policy lag: chọn cơ chế nào?
:::

::: hint
Câu 1 dùng phép min hai critic. Câu 3 cần critic tập trung khi huấn luyện và actor cục bộ khi chạy. Câu 4 phải nêu behavior $\mu$, learner $\pi$ và vai trò hai tỷ số cắt.
:::

::: solution
1. $y=2+0{,}95\min(3,4)=4{,}85$.
2. SAC khám phá bằng policy stochastic và entropy nhưng phải chọn $\alpha$; TD3 dùng actor deterministic, cần tune noise và lịch trễ $d$. Không có đáp án phổ quát.
3. MADDPG dùng CTDE.
4. IMPALA dùng V-trace: $\rho_t$ sửa residual, $c_t$ truyền trace.
:::

**Nguồn:** tr. 75–77; bài tập tổng hợp tr. 63–76.

**Nối ra:** checklist năm phép kiểm gom các thao tác trên thành quy trình đọc thuật toán mới.


<!-- note-topic-id: lec-11-topic-13 -->

## Năm phép kiểm và tuyến đọc tiếp

Năm phép kiểm khi đọc một phương pháp mới:

1. Xác định behavior policy, target policy và support.
2. Viết target critic, mặt nạ terminal và đại lượng dừng gradient.
3. Viết actor gradient cùng miền và kích thước.
4. Tách cơ chế lý thuyết khỏi lựa chọn triển khai.
5. Giới hạn kết luận theo giả thiết và giao thức thực nghiệm.

X03 đã áp dụng bốn phép kiểm đầu; phép thứ năm giữ kết luận trong phạm vi nguồn.

## Tài liệu tham khảo

Nguồn sơ cấp phần II (theo cụm chủ đề):

- Konda & Tsitsiklis (2000). Actor–Critic Algorithms.
- Precup, Sutton & Singh (2000). Eligibility Traces for Off-Policy Policy Evaluation.
- Degris, White & Sutton (2012). Off-Policy Actor–Critics.
- Mnih et al. (2016). Asynchronous Methods for Deep Reinforcement Learning (A3C).
- Silver et al. (2014). Deterministic Policy Gradient Algorithms (DPG).
- Lillicrap et al. (2016). Continuous Control with Deep Reinforcement Learning (DDPG).
- Barth-Maron et al. (2018). Distributed Distributional Deterministic Policy Gradients (D4PG).
- Lowe et al. (2017). Multi-Agent Actor–Critic for Mixed Cooperative–Competitive Environments (MADDPG).
- Wang et al. (2017). Sample Efficient Actor–Critic with Experience Replay (ACER).
- Wu et al. (2017). Scalable Trust-Region Method for Deep RL using Kronecker-Factored Approximation (ACKTR).
- Haarnoja et al. (2018). Soft Actor–Critic Algorithms and Applications (SAC).
- Fujimoto, van Hoof & Meger (2018). Addressing Function Approximation Error in Actor–Critic Methods (TD3).
- Liu et al. (2017). Stein Variational Policy Gradient (SVPG).
- Espeholt et al. (2018). IMPALA: Scalable Distributed Deep-RL with Importance Weighted Actor–Learner Architectures.
- Cobbe et al. (2021). Phasic Policy Gradient (PPG).

Nguồn bài giảng: `lecture11_part3.pdf`, tr. 44–77 (nội dung mới), tr. 78 (tài liệu tham khảo phần I: Williams 1992; Schulman et al. 2015, 2016, 2017; Weng 2018; Engstrom et al. 2020; Jin, Li & Wang 2024; Xie et al. 2025; Lee & Yoon 2025).

**Nguồn:** tr. 75–77 (dùng lại để tổng kết); tr. 78 (tài liệu tham khảo phần I).

