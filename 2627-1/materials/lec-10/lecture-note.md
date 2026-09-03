# Bài 10 — TRPO và PPO

## Mục tiêu và kiến thức tiên quyết

- Phân biệt baseline Monte Carlo, actor–critic và ước lượng lợi thế tổng quát (GAE).
- Giải thích surrogate, phân kỳ Kullback–Leibler (KL) và natural gradient trong TRPO.
- Tính mục tiêu PPO-Clip theo đúng dấu của lợi thế và tỷ số.
- Kiểm tra lô dữ liệu (batch), các đại lượng đóng băng, hàm mất mát (loss) và chẩn đoán khi triển khai PPO.
- Phân biệt mô hình lý thuyết PPO-Clip với quy trình triển khai thực hành và nêu đúng phạm vi kết quả hội tụ.

Kiến thức tiên quyết: MDP, xấp xỉ hàm, DQN, hàm điểm (score function), định lý gradient chính sách và REINFORCE từ Bài 09. Nguồn chính là PDF 43 trang của Bài 10; metadata ghi “Part 1”, còn tên tệp nguồn ghi phần 2.

Chu trình PPO dùng xuyên suốt bài: thu dữ liệu theo chính sách cũ → tính và đóng băng lợi thế cùng đích giá trị → tối ưu nhiều epoch → đồng bộ chính sách cũ rồi thu lô mới.

## Bản đồ chủ đề

Mười hai chủ đề được chia thành bốn nhóm: cốt lõi (01, 03–09), cầu nối (02), bổ sung (10, 11) và đọc thêm (12).

| Mã | Nhóm và phạm vi | Vai trò, đầu vào → sản phẩm học tập | Vị trí và kết nối | Nguồn |
|---|---|---|---|---|
| 01 | Cốt lõi | REINFORCE và dữ liệu đổi → khóa mục tiêu, hàm điểm và chính sách sinh dữ liệu | Mở bài; Bài 09 → chủ đề 02 | tr. 4–10 |
| 02 | Cầu nối | Phương sai REINFORCE → baseline, critic và tín hiệu lợi thế | Sau 01, trước 03; lấp khoảng trống giữa REINFORCE và TD/GAE | tr. 11–13 |
| 03 | Cốt lõi | Critic và sai số TD → lợi thế GAE cùng hai mặt nạ | 02 → surrogate ở 04 | tr. 13 |
| 04 | Cốt lõi | Lợi thế và dữ liệu cũ → tỷ số, surrogate và giới hạn xấp xỉ | 03 → miền tin cậy TRPO ở 05 | tr. 14–16 |
| 05 | Cốt lõi | Ràng buộc KL → bước natural gradient và quy trình TRPO | 04 → động cơ đơn giản hóa ở 06 | tr. 17–20 |
| 06 | Cốt lõi | Tỷ số và dấu lợi thế → mục tiêu PPO-Clip theo từng trường hợp | 05 → hàm mất mát tổng ở 07 | tr. 20–22 |
| 07 | Cốt lõi | Lợi thế thô và đích giá trị → hai đường mất mát actor–critic | 06 → hợp đồng dữ liệu ở 08 | tr. 23 |
| 08 | Cốt lõi | Rollout nhiều môi trường → bộ đệm, lô con và dữ liệu biên | 07 → chẩn đoán ở 09 | tr. 24–25 |
| 09 | Cốt lõi | Log huấn luyện → chẩn đoán và so sánh TRPO/PPO có điều kiện | 08 → chi tiết triển khai ở 10 | tr. 26–28, 35–36 |
| 10 | Bổ sung | Khoảng trống giữa mục tiêu và cấu hình thực hành → danh mục lựa chọn triển khai | 09 → mô hình lý thuyết ở 11; có thể rút khi thiếu thời gian | tr. 29–36 |
| 11 | Bổ sung | Khoảng trống về phạm vi bảo đảm → kết quả điểm dừng có điều kiện | 08 và 10 → giới hạn, đọc thêm ở 12; không suy sang PPO thực hành | tr. 37–42; Jin–Li–Wang 2024 |
| 12 | Đọc thêm | Kết quả chính → PPO-Penalty và danh mục nguồn tự học | Kết bài; không mở thêm tuyến nội dung | tr. 38, 43 |

## Ký hiệu và quy ước

Trạng thái $S_t$, hành động $A_t$, phần thưởng $R_{t+1}$ nhận sau $A_t$. Return từ thời điểm $t$:

$$G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},\qquad J(\theta)=\mathbb E[G_0],\quad 0\le\gamma<1.$$

$V^\pi(s)=\mathbb E[G_t\mid S_t=s]$, $Q^\pi(s,a)=\mathbb E[G_t\mid S_t=s,A_t=a]$, $A^\pi=Q^\pi-V^\pi$. Chính sách cũ $\pi_{\mathrm{old}}=\pi_{\theta_{\mathrm{old}}}$ sinh dữ liệu; hàm điểm (score) là $\nabla_\theta\log\pi_\theta(a\mid s)$ được đạo hàm theo $\theta$ rồi đánh giá tại $\theta_{\mathrm{old}}$. Với mục tiêu $J=\mathbb E[G_0]$, ước lượng quỹ đạo mang hệ số $\gamma^tG_t\nabla\log\pi$. Mỗi đợt thu thập dài $H$ bước từ $N$ môi trường tạo lô $B=HN$; $T$ dành cho thời điểm episode kết thúc thật. Tỷ số $w_t(\theta)=\pi_\theta(A_t\mid S_t)/\pi_{\mathrm{old}}(A_t\mid S_t)$ yêu cầu chính sách cũ gán xác suất khác không cho hành động đã lấy mẫu.

<!-- note-topic-id: lec-10-topic-01 -->

## Từ REINFORCE đến vấn đề phân bố dữ liệu đổi

**Trực giác.** REINFORCE học trực tiếp chính sách $\pi_\theta(a\mid s)$ bằng gradient của $J(\theta)=\mathbb E[G_0]$. Vấn đề trung tâm: dữ liệu được thu dưới $\pi_{\theta_{\mathrm{old}}}$, nhưng sau mỗi cập nhật cả phân bố hành động lẫn phân bố trạng thái đều đổi; một bước lớn có thể cải thiện nhanh hoặc phá hủy hiệu năng (tr. 4–10).

**Hình thức.** Với quỹ đạo $\tau$, log-derivative trick cho

$$\nabla_\theta J(\theta)=\mathbb E_{\tau\sim\pi_\theta}\!\left[R(\tau)\sum_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)\right],$$

và định lý gradient chính sách tránh đạo hàm phân bố trạng thái. Theo quy ước $J=\mathbb E[G_0]$, ước lượng Monte Carlo trên một episode là

$$\widehat g_{\mathrm{MC}}=\sum_{t=0}^{T-1}\gamma^tG_t\,\left.\nabla_\theta\log\pi_\theta(A_t\mid S_t)\right|_{\theta=\theta_{\mathrm{old}}}.$$

Hệ số $\gamma^t$ theo quy ước $J=\mathbb E[G_0]$; phép suy ra đầy đủ nằm trong khối derivation bên dưới. Điểm cần nhấn: hàm điểm được đạo hàm theo biến $\theta$ rồi mới đánh giá tại $\theta_{\mathrm{old}}$; không đạo hàm biểu thức $\log\pi_{\theta_{\mathrm{old}}}$ vì $\theta_{\mathrm{old}}$ là hằng trong lô (tr. 6–10).

Chu trình PPO gồm bốn bước: thu dữ liệu theo $\pi_{\mathrm{old}}$, tính rồi đóng băng lợi thế và đích, tối ưu nhiều epoch trên lô cố định, đồng bộ $\pi_{\mathrm{old}}\leftarrow\pi_\theta$.

**Ví dụ/ứng dụng.** Một quỹ đạo may mắn có thể chi phối toàn bộ gradient của lô; đây là lý do trực tiếp dẫn tới baseline và critic ở chủ đề sau (tr. 6–10).

::: derivation Từ log-derivative trick đến ước lượng có hệ số $\gamma^t$
Khởi điểm từ $J(\theta)=\mathbb E_{\tau\sim p_\theta}[R(\tau)]$. Đạo hàm dưới dấu tích phân:

$$\nabla_\theta J(\theta)=\int p_\theta(\tau)\nabla_\theta\log p_\theta(\tau)\,R(\tau)\,d\tau.$$

Vì động lực học môi trường không phụ thuộc $\theta$,

$$\nabla_\theta\log p_\theta(\tau)=\sum_{t=0}^{T-1}\nabla_\theta\log\pi_\theta(a_t\mid s_t).$$

Với $R(\tau)$ được tách theo return $G_t$ từ mỗi thời điểm và quy ước $J=\mathbb E[G_0]$, phần tín hiệu tại bước $t$ mang hệ số $\gamma^tG_t$, cho

$$\widehat g_{\mathrm{MC}}=\sum_{t=0}^{T-1}\gamma^tG_t\,\left.\nabla_\theta\log\pi_\theta(A_t\mid S_t)\right|_{\theta=\theta_{\mathrm{old}}}.$$

Điều kiện sử dụng: chính sách khả vi theo $\theta$, hỗ trợ hành động chứa hành động đã lấy mẫu, và tổng/tích phân–đạo hàm được phép đổi chỗ. Một quy ước mục tiêu khác sẽ cho estimator khác; không trộn hai quy ước trong cùng một phép suy diễn.
:::

**Giới hạn.** Bài không chứng minh lại toàn bộ định lý gradient chính sách; chỉ khóa mục tiêu, chỉ số $R_{t+1}$, định nghĩa $G_t$ và điểm đánh giá hàm điểm để mọi phép suy diễn sau nhất quán.


<!-- note-topic-id: lec-10-topic-02 -->

## Baseline và actor–critic

**Trực giác.** Một return lớn có thể do trạng thái thuận lợi, không chỉ do hành động vừa chọn. Baseline $b(S_t)$ loại phần chung này mà không đổi kỳ vọng gradient (tr. 11).

**Hình thức.** Estimator có baseline:

$$\widehat g_b=\sum_t\gamma^t\bigl(G_t-b(S_t)\bigr)\left.\nabla_\theta\log\pi_\theta(A_t\mid S_t)\right|_{\theta=\theta_{\mathrm{old}}}.$$

Nếu $b(S_t)$ không phụ thuộc hành động đã lấy mẫu khi điều kiện theo trạng thái, và các điều kiện tổng/tích phân–đạo hàm được thỏa (hỗ trợ cố định theo $\theta$), thì kỳ vọng hàm điểm nhân baseline bằng không:

$$\sum_a\pi_\theta(a\mid s)\,b(s)\,\nabla_\theta\log\pi_\theta(a\mid s)=b(s)\nabla_\theta\sum_a\pi_\theta(a\mid s)=0.$$

Với hành động liên tục, thay tổng bằng tích phân. Chọn $b(S_t)=V_\phi(S_t)$ đưa tín hiệu về dạng lợi thế — đây là cầu nối sang TD/GAE ở chủ đề kế tiếp. Trong hàm mất mát của actor, baseline/lợi thế được dừng gradient (ký hiệu $\operatorname{sg}$).

::: derivation Baseline không đổi kỳ vọng: hai trường hợp
Trường hợp Bernoulli (tr. 11): với $A\sim\operatorname{Bernoulli}(p)$, $p=0{,}25$, $b(s)=4$ và hàm điểm theo logit là $A-p$,

$$\mathbb E_A[4(A-p)]=4\bigl[0{,}25(0{,}75)+0{,}75(-0{,}25)\bigr]=4(0{,}1875-0{,}1875)=0.$$

Trường hợp tổng quát rời rạc, với $b(s)$ không phụ thuộc $a$:

$$\sum_a\pi_\theta(a\mid s)\,b(s)\,\nabla_\theta\log\pi_\theta(a\mid s)
=b(s)\sum_a\pi_\theta(a\mid s)\frac{\nabla_\theta\pi_\theta(a\mid s)}{\pi_\theta(a\mid s)}
=b(s)\,\nabla_\theta\sum_a\pi_\theta(a\mid s)=b(s)\,\nabla_\theta 1=0.$$

Bước đổi đạo hàm qua tổng cần điều kiện chính quy: hỗ trợ theo $a$ không đổi với $\theta$ và tổng hội tụ đều đủ tốt. Với hành động liên tục, thay tổng bằng tích phân với cùng điều kiện. Kết luận: kỳ vọng gradient giữ nguyên, nhưng phương sai của $\widehat g_b$ thường giảm mạnh vì phần chung $b(S_t)$ của return bị loại khỏi tín hiệu.
:::

**Ví dụ.** Actor–critic Monte Carlo: critic học từ đích $G_t$, tín hiệu actor $G_t-V_\phi(S_t)$. Nhánh bootstrap (TD/GAE): critic học từ đích có $V(S_{t+1})$, tín hiệu là $\widehat A_t$ từ TD hoặc GAE; đánh đổi là phụ thuộc bootstrap và critic. Đây là cầu nối sang cách ước lượng lợi thế bằng TD và GAE ở chủ đề kế tiếp. Quy ước của bài: "actor–critic bootstrap" chỉ tách nhánh TD/GAE khỏi nhánh Monte Carlo, không phải định nghĩa phổ quát (tr. 11–13).

**Giới hạn.** Baseline chỉ không đổi kỳ vọng khi không phụ thuộc hành động tại trạng thái; một critic học bằng đích Monte Carlo vẫn tạo được actor–critic, nên không đồng nhất "critic" với "bootstrap".


<!-- note-topic-id: lec-10-topic-03 -->

## Generalized Advantage Estimation (GAE)

**Trực giác.** Critic tạo sai phân thời gian (TD) $\delta_t$; GAE trộn nhiều tầm bootstrap để đánh đổi độ chệch với phương sai (tr. 13).

**Hình thức.** Sai số TD dùng bản critic khi thu rollout:

$$\delta_t=R_{t+1}+\gamma m_tV_{\mathrm{old}}(S_{t+1})-V_{\mathrm{old}}(S_t),$$

với $m_t$ là mặt nạ bootstrap, bằng $0$ chỉ ở terminal thật. Lợi thế thô:

$$\widehat A_t^{\mathrm{raw}}=\delta_t+(\gamma\lambda)\delta_{t+1}+(\gamma\lambda)^2\delta_{t+2}+\cdots,$$

trên rollout hữu hạn viết thành đệ quy $\widehat A_t^{\mathrm{raw}}=\delta_t+\gamma\lambda c_t\widehat A_{t+1}^{\mathrm{raw}}$. Hai mặt nạ có hai nhiệm vụ:

| ranh giới | $m_t$ (bootstrap) | $c_t$ (tiếp diễn GAE) |
|---|---|---|
| kết thúc MDP thật tại $T$ | 0 | 0 |
| truncation ngoại sinh hoặc cuối rollout $H$ có quan sát cuối hợp lệ | 1 | 0 |
| chuyển tiếp thường | 1 | 1 |

$\lambda=0$: phương sai thấp, chệch nhiều hơn; $\lambda$ gần $1$: gần Monte Carlo, ít chệch, phương sai cao hơn. PPO thực hành gần như luôn dùng GAE.

::: derivation Đệ quy GAE hữu hạn và hai mặt nạ
Trên rollout hữu hạn $H$ bước, chuỗi vô hạn $\widehat A_t^{\mathrm{raw}}=\sum_{l\ge0}(\gamma\lambda)^l\delta_{t+l}$ được viết thành đệ quy:

$$\widehat A_t^{\mathrm{raw}}=\delta_t+\gamma\lambda\,c_t\,\widehat A_{t+1}^{\mathrm{raw}},$$

tính ngược từ $t=H-1$ về $0$, với quy ước $\widehat A_H^{\mathrm{raw}}=0$. Hai mặt nạ có vai trò khác nhau:

- $m_t$ điều khiển **bootstrap trong $\delta_t$**: $m_t=0$ chỉ khi MDP kết thúc thật, khi đó không có trạng thái kế tiếp hợp lệ để đánh giá $V_{\mathrm{old}}$.
- $c_t$ điều khiển **tiếp diễn đệ quy GAE**: $c_t=0$ tại terminal, tại reset và tại cuối rollout, dừng truyền tín hiệu qua biên episode hoặc biên batch.

Truncation ngoại sinh (giới hạn thời gian nhân tạo, ví dụ hết $H$ bước trước $T$) chỉ bootstrap khi có quan sát cuối hợp lệ: đặt $m_t=1$ nhưng $c_t=0$, tức $\delta_t$ dùng $V_{\mathrm{old}}(S_H)$ còn đệ quy dừng. Nếu giới hạn thời gian là một phần của MDP — chẳng hạn thời gian còn lại nằm trong trạng thái — thì hết chân trời là terminal của bài toán và $m_t=0$.
:::

**Ví dụ.** $\gamma=0{,}9$, $\lambda=0{,}8$, $V(S_0)=2$, $V(S_1)=3$, $R_1=1$, $R_2=2$. Episode kết thúc thật tại $T=2$, tức $S_2$ là trạng thái cuối: $\delta_0=1{,}7$, $\delta_1=-1$, $\widehat A_0^{\mathrm{raw}}=0{,}98$. Rollout ngoại sinh dừng tại $H=2<T$ với $V(S_2)=4$: $\delta_1=2{,}6$, $\widehat A_0^{\mathrm{raw}}=3{,}572$.

**Giới hạn.** Chỉ truncation nhân tạo hoặc ngoại sinh có quan sát cuối hợp lệ mới bootstrap; nếu chân trời là một phần của MDP (thời gian còn lại nằm trong trạng thái) thì hết chân trời là terminal và $m_t=0$. Không mở TD($\lambda$) thành tuyến riêng.


<!-- note-topic-id: lec-10-topic-04 -->

## Vì sao cần miền tin cậy: surrogate và tỷ số

**Trực giác.** Surrogate khớp bậc nhất với $J$ tại $\theta_{\mathrm{old}}$ chỉ đáng tin trong lân cận của chính sách đã sinh dữ liệu. Bước quá nhỏ: dữ liệu còn đại diện nhưng cải thiện chậm; bước quá lớn: xác suất hành động và phân bố trạng thái đổi mạnh, xấp xỉ tuyến tính có thể dẫn sai hướng (tr. 14–16).

**Hình thức.** Định nghĩa tỷ số và surrogate bậc nhất:

$$w_t(\theta)=\frac{\pi_\theta(A_t\mid S_t)}{\pi_{\mathrm{old}}(A_t\mid S_t)},\qquad L_{\theta_{\mathrm{old}}}(\theta)=\mathbb E_t\bigl[w_t(\theta)\widehat A_t\bigr].$$

Nếu $\widehat A_t>0$: tăng xác suất của $A_t$; nếu $\widehat A_t<0$: giảm. Chuỗi lý luận gồm ba bước chuyển từ đẳng thức lý thuyết đến trung bình thực nghiệm, phải tường minh: (i) đẳng thức sai khác hiệu năng dùng kỳ vọng occupancy chiết khấu $d^\pi(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi(S_t=s)$; (ii) thay occupancy mới bằng occupancy cũ là xấp xỉ; (iii) trung bình thực nghiệm $\mathbb E_B[f]=B^{-1}\sum_{i=1}^Bf_i$ trên $B=HN$ mẫu. Trong surrogate lý thuyết, $\widehat A_t$ là $\widehat A^{\mathrm{raw}}$; TRPO thực hành giải gần đúng

$$\max_\theta\ \mathbb E_B\bigl[w_t\widehat A_t^{\mathrm{raw}}\bigr]\quad\text{s.t.}\quad\mathbb E_B\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}\|\pi_\theta)\bigr]\le\delta.$$

::: derivation Ba bước chuyển từ đẳng thức lý thuyết đến trung bình thực nghiệm trong chuỗi TRPO
Bước 1 (đẳng thức, dưới giả thiết): với hai chính sách có cùng phân bố đầu $\rho_0$, $0\le\gamma<1$ và khả năng nối episode bằng trạng thái hấp thụ phần thưởng không,

$$J(\pi')-J(\pi)=\frac{\mathbb E_{\mathrm{disc},\pi'}[A^\pi]}{1-\gamma},
\qquad \mathbb E_{\mathrm{disc},\pi}[f]=\mathbb E_{S\sim d^\pi,\,A\sim\pi}[f],$$

trong đó $d^\pi(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi(S_t=s)$ là occupancy chiết khấu.

Bước 2 (xấp xỉ): vế trái chứa occupancy của $\pi'$, chưa biết. Thay bằng occupancy cũ $\pi$ và tái trọng số bằng tỷ số:

$$\frac{\mathbb E_{\mathrm{disc},\pi'}[A^\pi]}{1-\gamma}\ \approx\ \frac{\mathbb E_{\mathrm{disc},\pi}[wA^\pi]}{1-\gamma}.$$

Đây là xấp xỉ, không phải đẳng thức; sai số phụ thuộc độ dịch chuyển của phân bố trạng thái.

Bước 3 (trung bình batch): thay kỳ vọng occupancy chiết khấu bằng trung bình đều trên batch $B=HN$ mẫu, $\mathbb E_B[f]=B^{-1}\sum_{i=1}^Bf_i$. Ràng buộc KL cũng được giảm thành KL trung bình thực nghiệm $\mathbb E_B[D_{\mathrm{KL}}(\pi_{\mathrm{old}}\|\pi_\theta)]\le\delta$; đây không phải max-KL trong chặn lý thuyết của TRPO gốc và không đồng nhất với kỳ vọng occupancy chiết khấu của $J=\mathbb E[G_0]$.
:::

**Ví dụ.** Hai mẫu thu dưới $\pi_{\mathrm{old}}$: hành động có lợi $\widehat A^{\mathrm{raw}}=2$, xác suất $0{,}20\to0{,}24$ nên $w=1{,}2$, đóng góp $2{,}4$; hành động bất lợi $\widehat A^{\mathrm{raw}}=-1$, xác suất $0{,}50\to0{,}40$ nên $w=0{,}8$, đóng góp $-0{,}8$. Dữ liệu cũ vẫn cho biết hướng thay đổi.

**Giới hạn.** Tỷ số cần chính sách mới tuyệt đối liên tục theo chính sách cũ trên dữ liệu; mẫu có xác suất/mật độ cũ bằng không không thể được sửa bằng tỷ số. Tỷ số chỉ tái trọng số hành động có điều kiện; trạng thái vẫn từ phân bố cũ. KL trong ràng buộc là KL trung bình thực nghiệm trên batch, không phải max-KL trong chặn lý thuyết của TRPO gốc; không trình bày chứng minh performance-difference đầy đủ.


<!-- note-topic-id: lec-10-topic-05 -->

## TRPO như natural gradient

**Trực giác.** Ràng buộc KL được xấp xỉ cục bộ bằng dạng toàn phương theo ma trận Fisher: các tọa độ "độ cong" lớn phải nhận bước nhỏ hơn dù gradient thô có thể lớn. Đây là ellipsoid tin cậy quanh $\theta_{\mathrm{old}}$ (tr. 17–20).

**Hình thức.** Đặt $u(s,a)=\left.\nabla_\theta\log\pi_\theta(a\mid s)\right|_{\theta_{\mathrm{old}}}$. Phân biệt hai đại lượng:

$$F=\mathbb E_{S\sim B,\,A\sim\pi_{\mathrm{old}}}\bigl[uu^\top\bigr],\qquad \widehat F=\frac1B\sum_{i=1}^Bu_iu_i^\top\approx F.$$

$F$ là Hessian của average-KL (kỳ vọng hành động dưới $\pi_{\mathrm{old}}$ vẫn nằm trong biểu thức chính xác); $\widehat F$ là ước lượng Monte Carlo thay kỳ vọng hành động bằng mẫu đã lấy mẫu. Với $g=\nabla_\theta L_{\theta_{\mathrm{old}}}(\theta)\big|_{\theta_{\mathrm{old}}}$, bước natural gradient dạng đóng

$$\Delta^*=\sqrt{\frac{2\delta}{g^\top F^{-1}g}}\;F^{-1}g,$$

chỉ hợp lệ khi $F$ (hoặc $\widehat F+\eta I$ với damping $\eta>0$) xác định dương. TRPO thực hành: thu rollout, tính lợi thế (thường GAE), ước lượng $g$, dùng gradient liên hợp (CG) với tích Fisher–véc-tơ (FVP) để giải gần đúng $(\widehat F+\eta I)x=g$, co bước theo biên KL, rồi backtracking line search kiểm cả surrogate và KL thực nghiệm trước khi nhận bước.

::: derivation Natural gradient như bài toán ràng buộc bậc hai
Xấp xỉ KL cục bộ quanh $\theta_{\mathrm{old}}$:

$$D_{\mathrm{KL}}(\theta_{\mathrm{old}},\theta)\approx\frac12(\theta-\theta_{\mathrm{old}})^\top F(\theta-\theta_{\mathrm{old}}).$$

Bài toán ràng buộc tuyến tính hóa thành: tối đa $g^\top\Delta$ với $g=\nabla_\theta L_{\theta_{\mathrm{old}}}\big|_{\theta_{\mathrm{old}}}$, ràng buộc $\tfrac12\Delta^\top F\Delta\le\delta$. Lời giải bằng hệ Lagrange ($F$ xác định dương):

$$\Delta^*=\sqrt{\frac{2\delta}{g^\top F^{-1}g}}\;F^{-1}g,$$

thỏa ràng buộc chạm biên khi $g\ne0$. Đẳng thức Hessian–outer-product $F=\mathbb E[uu^\top]$ cần các điều kiện chính quy quen thuộc. Khi $\widehat F$ suy biến hoặc kém điều kiện, thêm damping $\eta>0$ và giải $(\widehat F+\eta I)x=g$: hệ trở thành xác định dương, điều kiện cần cho gradient liên hợp.

Bảng so sánh bước theo metric:

| | bước gradient thông thường | bước natural gradient |
|---|---|---|
| chuẩn | Euclid theo $\theta$ | chuẩn Fisher $\sqrt{\Delta^\top F\Delta}$ |
| hệ quả | mọi tọa độ nhận bước cùng scale | tọa độ "độ cong" cao nhận bước nhỏ hơn |
| chi phí | rẻ | cần FVP, CG, line search |
:::

**Ví dụ.** Giả sử ma trận Fisher $F=\operatorname{diag}(4,1)$ xác định dương, $g=(2,1)$ và $\delta=0{,}01$. Khi đó $F^{-1}g=(0{,}5,1)$, $g^\top F^{-1}g=2$, nên $\Delta^*=\sqrt{0{,}02/2}\,(0{,}5,1)=(0{,}05,0{,}1)$; kiểm tra $\tfrac12(\Delta^*)^\top F\Delta^*=0{,}01$. Fisher lớn theo tọa độ đầu làm bước ở tọa độ đó nhỏ hơn.

**Giới hạn.** Không dựng hay nghịch đảo $F$ tường minh trong mạng sâu; FVP tránh dựng $\widehat F$ nhưng mỗi lần nhân vẫn cần phép vi phân trên batch. Chi phí phụ thuộc số vòng CG, ngưỡng residual và số lần line search; cần báo cáo tolerance, damping, $\delta$ và tiêu chí nhận bước. Không cài đặt FVP bằng code trong phạm vi bài.


<!-- note-topic-id: lec-10-topic-06 -->

## PPO-Clip: mục tiêu có đoạn phẳng

**Trực giác.** TRPO tốn phép giải hệ bậc hai và line search. PPO giữ lô cũ, tỷ số $w_t$ và lợi thế, rồi sửa mục tiêu để loại bỏ lợi ích của thay đổi thuận lợi quá lớn — chỉ dùng tối ưu bậc nhất (tr. 20–22).

**Hình thức.** Tỷ số được tính lại ở mỗi lô con:

$$w_t(\theta)=\exp\bigl(\log\pi_\theta(A_t\mid S_t)-\log\pi_{\mathrm{old}}(A_t\mid S_t)\bigr),\qquad w_t(\theta_{\mathrm{old}})=1.$$

$\widehat A_t^{\mathrm{actor}}$ là lợi thế dùng cho actor; chủ đề 07 sẽ tách rõ lợi thế này khỏi đích của critic. Mục tiêu PPO-Clip theo từng mẫu:

$$\ell_t=\min\bigl(w_t\widehat A_t^{\mathrm{actor}},\operatorname{clip}(w_t,1-\epsilon,1+\epsilon)\widehat A_t^{\mathrm{actor}}\bigr),$$

tức

$$\ell_t=\begin{cases}\min(w_t,1+\epsilon)\,\widehat A_t^{\mathrm{actor}},&\widehat A_t^{\mathrm{actor}}\ge0,\\[2pt]\max(w_t,1-\epsilon)\,\widehat A_t^{\mathrm{actor}},&\widehat A_t^{\mathrm{actor}}<0.\end{cases}$$

PPO thực hành dùng trung bình đều $L_B^{\mathrm{clip}}=\mathbb E_B[\ell_t]$ trên $B=HN$ mẫu.

::: derivation Vì sao min tạo đoạn phẳng đúng phía cải thiện
Xét hai trường hợp của $\ell_t=\min(w\widehat A,\operatorname{clip}(w,1-\epsilon,1+\epsilon)\widehat A)$:

**$\widehat A\ge0$.** Nhân với số dương giữ thứ tự, nên $\min$ trên tích tương đương $\min$ trên tỷ số:

$$\ell_t=\min(w,1+\epsilon)\,\widehat A.$$

- Trong dải $[1-\epsilon,1+\epsilon]$: hạng dùng là $w\widehat A$, gradient theo $w$ giữ nguyên.
- $w>1+\epsilon$: hạng dùng là $(1+\epsilon)\widehat A$, hằng theo $\theta$, gradient bằng 0 — đoạn phẳng chặn việc tăng xác suất hành động có lợi quá mức.
- $w<1-\epsilon$: hạng dùng vẫn là $w\widehat A$, gradient vẫn phạt (không đoạn phẳng phía bất lợi).

**$\widehat A<0$.** Nhân với số âm đảo thứ tự, $\min$ trên tích thành $\max$ trên tỷ số:

$$\ell_t=\max(w,1-\epsilon)\,\widehat A.$$

- $w<1-\epsilon$: hạng dùng là $(1-\epsilon)\widehat A$, gradient bằng 0 — đoạn phẳng chặn việc giảm xác suất hành động bất lợi quá mức.
- $w>1+\epsilon$: hạng dùng vẫn là $w\widehat A$, gradient vẫn phạt.
- Trong dải: hạng dùng là $w\widehat A$.

Hai ca ngoài dải theo phía bất lợi: $(\widehat A,w)=(2,0{,}7)$ cho $\ell=1{,}4$ và $(\widehat A,w)=(-2,1{,}3)$ cho $\ell=-2{,}6$ — mẫu vẫn bị phạt như thường. Vì vậy đoạn phẳng chỉ xuất hiện ở phía cải thiện quá mức.
:::

**Ví dụ.** $\epsilon=0{,}2$. Hành động có lợi: $\widehat A^{\mathrm{actor}}=2$, $w=1{,}3$; không chặn $2{,}6$, bị chặn còn $\ell=1{,}2\times2=2{,}4$. Hành động bất lợi: $\widehat A^{\mathrm{actor}}=-2$, $w=0{,}7$; không chặn $-1{,}4$, bị chặn còn $\ell=0{,}8\times(-2)=-1{,}6$. Cả hai đi theo phía cải thiện.

**Giới hạn.** Phân tích theo dấu: với $\widehat A\ge0$, ngoài dải phía $w>1+\epsilon$ gradient bằng 0 (đoạn phẳng), phía $w<1-\epsilon$ vẫn giữ gradient phạt; với $\widehat A<0$, đoạn phẳng ở $w<1-\epsilon$ và phía $w>1+\epsilon$ vẫn phạt. Trong dải $[1-\epsilon,1+\epsilon]$, clipping không đổi hạng surrogate. Clipping không phải ràng buộc KL cứng: từng tỷ số có thể nằm trong khoảng nhưng KL toàn phân phối vẫn lớn; nhiều epoch SGD có thể đẩy chính sách xa batch ban đầu; không có bảo đảm đơn điệu chung.


<!-- note-topic-id: lec-10-topic-07 -->

## Hàm mất mát tổng: lợi thế actor và đích critic

**Trực giác.** Actor và critic dùng hai đường tín hiệu khác nhau từ cùng một batch: actor cần tín hiệu có scale ổn định, critic cần đích gần return thật. Không chuẩn hóa target critic theo lợi thế actor (tr. 23).

**Hình thức.** Ba đại lượng phải tách bạch:

- $\widehat A_t^{\mathrm{raw}}$: lợi thế thô từ GAE;
- $\widehat A_t^{\mathrm{actor}}=\operatorname{sg}\bigl((\widehat A_t^{\mathrm{raw}}-\mu_B)/(\sigma_B+\varepsilon_A)\bigr)$: chuẩn hóa trên batch, dừng gradient;
- $\widehat V_t=\operatorname{sg}\bigl(V_{\mathrm{old}}(S_t)+\widehat A_t^{\mathrm{raw}}\bigr)$: target critic thô, đóng băng.

Loss tổng:

$$\mathcal L=-\mathbb E_B[\ell_t]+c_V\,\mathbb E_B[(V_\phi(S_t)-\widehat V_t)^2]-c_H\,\mathbb E_B[\mathcal H(\pi_\theta)].$$

Gradient critic đi qua $V_\phi$ hiện tại, không đi qua $\widehat V_t$; gradient actor đi qua $\ell_t$ với $\widehat A^{\mathrm{actor}}$ đã dừng gradient.

**Ví dụ/ứng dụng.** Khi kiểm tra mã: nếu target critic bị thay bằng $V_{\mathrm{old}}+\widehat A^{\mathrm{actor}}$ (đã chuẩn hóa), critic học một mục tiêu khác với return và explained variance trở nên vô nghĩa.

::: example Đường gradient của ba nhóm đại lượng trong một epoch
Giả sử batch $B=HN$ đã thu xong và $\widehat A^{\mathrm{raw}}$ có trung bình $\mu_B$, độ lệch chuẩn $\sigma_B$. Với một mẫu có $\widehat A_t^{\mathrm{raw}}=\mu_B+2\sigma_B$:

- $\widehat A_t^{\mathrm{actor}}=(\mu_B+2\sigma_B-\mu_B)/(\sigma_B+\varepsilon_A)\approx2$, không đổi trong suốt $K$ epoch.
- $\widehat V_t=V_{\mathrm{old}}(S_t)+\mu_B+2\sigma_B$, cũng cố định.
- $\ell_t$ thay đổi qua từng minibatch vì $w_t(\theta)=\exp(\log\pi_\theta(A_t\mid S_t)-\log\pi_{\mathrm{old}}(A_t\mid S_t))$ được tính lại với $\theta$ hiện tại.

Do đó gradient của critic chỉ đi qua $V_\phi(S_t)$; gradient của actor đi qua $\log\pi_\theta$ trong $w_t$. Nếu mã cho gradient chảy qua $\widehat A^{\mathrm{actor}}$ hoặc $\widehat V_t$, hợp đồng "đóng băng" bị vi phạm và critic có thể tự củng cố ước lượng sai của chính nó.
:::

**Giới hạn.** $\mu_B,\sigma_B$ là trung bình và độ lệch chuẩn của lợi thế thô trên batch; $\varepsilon_A>0$ tránh chia cho không. Mọi đại lượng đóng băng phải tường minh trước $K$ epoch tối ưu.


<!-- note-topic-id: lec-10-topic-08 -->

## Đợt thu thập, bộ đệm và lô con

**Trực giác.** Một batch PPO là một hợp đồng dữ liệu: những gì lưu khi thu rollout, những gì suy ra rồi đóng băng, và những gì tính lại mỗi minibatch (tr. 24–25).

**Hình thức.** Kiểm shape từ rollout sang batch phẳng, $B=HN$:

| đại lượng | rollout | batch phẳng |
|---|---|---|
| quan sát | $[H,N,d_s]$ | $[B,d_s]$ |
| hành động rời rạc | $[H,N]$ | $[B]$ |
| hành động liên tục | $[H,N,d_a]$ | $[B,d_a]$ |
| $\log\pi_{\mathrm{old}},V_{\mathrm{old}},\widehat A^{\mathrm{raw}}$ | $[H,N]$ | $[B]$ |
| $\widehat A^{\mathrm{actor}},\widehat V$ | $[H,N]$ | $[B]$ |

Schema ba nhóm: **lưu khi thu** $S,A,R,S_{\mathrm{next}},m,c,\log\pi_{\mathrm{old}},V_{\mathrm{old}}$; **suy ra rồi đóng băng** $V_{\mathrm{boot}},\widehat A^{\mathrm{raw}},\widehat A^{\mathrm{actor}},\widehat V$; **tính lại mỗi minibatch** $\log\pi_\theta,V_\phi,w$, entropy và loss. Với hành động liên tục nhiều chiều, cộng log-probability theo chiều hành động để mỗi mẫu có một tỷ số vô hướng.

**Ví dụ/ứng dụng.** Trình tự một lần cập nhật PPO:

1. Thu $H$ bước từ $N$ môi trường, lưu $S,A,R,S_{\mathrm{next}},m,c$ cùng $\log\pi_{\mathrm{old}},V_{\mathrm{old}}$.
2. Tính $V_{\mathrm{boot}}$ từ `final_observation` (trước reset) cho truncation nhân tạo; tính $\delta_t$, $\widehat A^{\mathrm{raw}}$ ngược thời gian bằng hai mặt nạ.
3. Suy ra rồi đóng băng $\widehat A^{\mathrm{actor}}$ và $\widehat V_t$.
4. Shuffle thành minibatch; chạy $K$ epoch Adam; mỗi minibatch tính lại $\log\pi_\theta,V_\phi,w$ và loss.
5. Đồng bộ $\pi_{\mathrm{old}}\leftarrow\pi_\theta$, xóa buffer, thu batch mới.

Mẫu shape kiểm tra nhanh:

| kiểm tra | kỳ vọng |
|---|---|
| hành động rời rạc sau flatten | $[B]$ nguyên (chỉ số) |
| log-probability sau flatten | $[B]$ thực |
| $\widehat A^{\mathrm{raw}}$ tại bước $H-1$ với truncation | $\delta_{H-1}$ (vì $c_{H-1}=0$) |
| $\delta_{H-1}$ với terminal | $R_H-V_{\mathrm{old}}(S_{H-1})$ (vì $m_{H-1}=0$) |

**Giới hạn.** Trước minibatch đầu, $\theta=\theta_{\mathrm{old}}$ nên $w=1$; sau đó $w$ được tính lại với $\theta$ hiện tại. Không tính lại lợi thế hay target bằng critic đã đổi trong các epoch sau.


<!-- note-topic-id: lec-10-topic-09 -->

## Chẩn đoán, siêu tham số và so sánh TRPO/PPO

**Trực giác.** Reward tăng không đủ để kết luận huấn luyện khỏe; cần theo dõi độ dịch chuyển chính sách và chất lượng critic (tr. 26–28, 35–36).

**Hình thức.** Bốn chẩn đoán:

$$\operatorname{clipfrac}=\mathbb E_B[\mathbf 1\{|w_t-1|>\epsilon\}],\qquad \widehat D_{\mathrm{KL}}^{\mathrm{old}\|\theta}=\mathbb E_B[(w_t-1)-\log w_t],$$

$$\operatorname{EV}=1-\frac{\operatorname{Var}_B(\widehat V_t-V_\phi(S_t))}{\operatorname{Var}_B(\widehat V_t)},\qquad \text{entropy } \mathbb E_B[\mathcal H(\pi_\theta)].$$

Siêu tham số tương tác: $\epsilon$ (độ rộng clip) với learning rate và số epoch $K$; $K$ với KL và clipfrac; $\gamma,\lambda$ (tầm tín dụng GAE) với critic và độ dài rollout; $c_V,c_H$ với backbone dùng chung. Không đưa khoảng "điển hình" thành quy tắc chung.

**Ví dụ/ứng dụng.** So sánh có giới hạn:

| khía cạnh | TRPO | PPO-Clip |
|---|---|---|
| ràng buộc | empirical average-KL tường minh | clipping ngầm theo mẫu |
| tối ưu | FVP, CG, line search | SGD/Adam nhiều epoch |
| triển khai | phức tạp | đơn giản |
| rủi ro chính | chi phí kỹ thuật | hiệu ứng recipe ẩn |

**Ví dụ/ứng dụng.** Ba mẫu biểu hiện chẩn đoán:

| biểu hiện | clipfrac | $\widehat D_{\mathrm{KL}}$ | entropy | EV | đọc như |
|---|---|---|---|---|---|
| khỏe | thấp, ổn định | nhỏ, ổn định | giảm chậm | dương, tiến về 1 | bước vừa phải, critic khá |
| quá bước | tăng nhanh | tăng vọt | tụt | dao động | giảm learning rate hoặc $K$, dừng sớm theo KL |
| chính sách gần tất định | có thể thấp | có thể nhỏ sau khi đã sụp | gần 0 | tùy critic | sụp đổ khám phá; kiểm $c_H$ và thang hành động |

Mẫu thứ hai minh họa lỗi phổ biến: $w$ tại hành động đã lấy mẫu có thể nằm gọn trong dải trong khi KL toàn phân phối lớn, vì batch chỉ quan sát tập hữu hạn trạng thái–hành động.

**Giới hạn.** Clipfrac là tỷ lệ mẫu có tỷ số ngoài dải, không phải tỷ lệ mẫu nằm trên đoạn phẳng của objective (đoạn phẳng còn phụ thuộc dấu lợi thế). $\operatorname{EV}$ không xác định khi $\operatorname{Var}_B(\widehat V)=0$; không có ngưỡng chẩn đoán phổ quát. PPO không phải "TRPO bỏ CG": đó là một recipe thực hành khác.


<!-- note-topic-id: lec-10-topic-10 -->

## Chi tiết triển khai: biến thể và tiền xử lý

**Trực giác.** Engstrom et al. (2020) hỏi: phần tăng hiệu năng của PPO so với TRPO đến từ clipped objective hay từ chi tiết triển khai? Kết luận: các tối ưu cấp mã chiếm một phần lớn và có thể đổi cả động lực học huấn luyện (tr. 29–34).

**Hình thức.** Value clipping là một biến thể, không phải thành phần bắt buộc của PPO-Clip:

$$V_t^{\mathrm{clip}}=V_{\mathrm{old}}(S_t)+\operatorname{clip}(V_\phi(S_t)-V_{\mathrm{old}}(S_t),-\epsilon_V,\epsilon_V),$$
$$\mathcal L_t^V=\max\bigl((V_\phi-\widehat V_t)^2,(V_t^{\mathrm{clip}}-\widehat V_t)^2\bigr).$$

Các nhóm lựa chọn recipe: dữ liệu (chuẩn hóa quan sát, scale/clip reward, chuẩn hóa lợi thế); tối ưu (khởi tạo trực giao, lịch learning rate, clip chuẩn gradient, Adam); mạng (activation, khởi tạo, chia sẻ backbone).

**Ví dụ/ứng dụng.** Scale reward bằng độ lệch chuẩn chạy của return chiết khấu đổi scale target critic; khởi tạo trực giao đổi phân bố hành động sớm, và dữ liệu on-policy sớm ảnh hưởng mọi cập nhật sau.

**Ví dụ/ứng dụng.** Checklist tái lập một kết quả PPO (tr. 35–36):

| nhóm | trường cần ghi |
|---|---|
| dữ liệu | số môi trường, độ dài rollout, phân loại terminal/truncation, chuẩn hóa |
| mục tiêu | $\gamma,\lambda,\epsilon$, trọng số value và entropy, có value clipping |
| tối ưu | optimizer, learning rate và lịch, số epoch, minibatch, clip gradient |
| mạng | kiến trúc, activation, khởi tạo, chia sẻ backbone |
| đánh giá | seed, số lần chạy, chính sách đánh giá, khoảng bất định |
| chẩn đoán | KL, clipfrac, entropy, value loss, explained variance |

Khi bỏ một tối ưu cấp mã, chuẩn hóa phần thưởng, giảm dần tốc độ học và khởi tạo đều có thể làm đổi toàn bộ quỹ đạo huấn luyện. Vì vậy, chỉ quy khác biệt kết quả cho hàm mục tiêu sau khi đã đối chiếu đầy đủ quy trình triển khai.

**Giới hạn.** Khi bỏ các tối ưu cấp mã, một PPO tối giản có thể khác nhiều so với PPO chuẩn; khác biệt giữa PPO và TRPO có thể nhỏ hơn khác biệt giữa hai cài đặt PPO. Chỉ ghi tên thuật toán là không đủ để tái lập; không suy ra một lựa chọn luôn tốt trên mọi benchmark.


<!-- note-topic-id: lec-10-topic-11 -->

## Lý thuyết PPO-Clip: mô hình lý tưởng và kết quả điểm dừng

**Trực giác.** PPO-Clip mạnh trong thực nghiệm nhưng khó phân tích: tỷ số giữa hai chính sách là một biến ngẫu nhiên, toán tử clip không trơn, hàm điểm của mạng sâu có thể không bị chặn, và thuật toán xen kẽ đồng bộ $\pi_{\mathrm{old}}$ với nhiều bước tối ưu ở vòng trong (tr. 37–42).

**Hình thức.** Mô hình lý tưởng tách hai thang thời gian: vòng ngoài đồng bộ $\pi_{\mathrm{old}}$, thu dữ liệu và tạo ước lượng lợi thế cắt ngắn; vòng trong giữ old data cố định và áp nhiều cập nhật ngẫu nhiên lên surrogate. Jin, Li và Wang (2024) phân tích PPO-Clip lý tưởng hóa này. Đặt $V(\theta)=V^{\pi_\theta}(s_0)$ và $\theta_{n,1}$ là tham số đầu vòng trong ở vòng ngoài $n$; theo đúng Định lý 3.1 với các Giả thiết 3.1, 3.2, 3.4:

$$\liminf_{n\to\infty}\|\nabla V(\theta_{n,1})\|^2\le 8L\sqrt{|\mathcal A|}\,\limsup_{n\to\infty}\phi_n\quad\text{hầu chắc chắn},$$

trong đó $L$ là hằng số Lipschitz của gradient, $|\mathcal A|$ là số hành động rời rạc và $\phi_n$ chặn sai lệch do lấy mẫu và ước lượng. Vòng ngoài và vòng trong ở đây là bản lý tưởng hóa của chu trình thu thập–tối ưu trong chủ đề 08. Chỉ khi vế phải tiến về không mới có kết luận điểm dừng tương ứng.

**Ví dụ/ứng dụng.** Kết quả này cho thấy phép cắt ngưỡng không chỉ là quy tắc kinh nghiệm: cấu trúc min/clip không trơn vẫn có thể được phân tích bằng suy luận theo biến cố, dưới giả thiết trơn, thưởng bị chặn và lịch tốc độ học phù hợp.

**Giới hạn.** Không suy ra cực đại toàn cục, không đổi $\liminf$ thành hội tụ của toàn dãy, không gọi đây là hội tụ tham số, và không suy ra hội tụ của PPO thực hành với Adam, GAE chuẩn hóa, clipping gradient hay early stopping. Mô hình lý tưởng không tự bao gồm các chi tiết recipe.


<!-- note-topic-id: lec-10-topic-12 -->

## Đọc thêm: PPO-Penalty và danh mục nguồn

**Trực giác.** PPO-Clip không phải biến thể duy nhất; nhánh penalty đưa KL thẳng vào mục tiêu với hệ số thích ứng (tr. 38, 43).

**Hình thức.** PPO-Penalty tối ưu

$$\max_\theta\ \mathbb E_B[w_t\widehat A_t]-\beta\,\mathbb E_B\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}\|\pi_\theta)\bigr],$$

với $\beta$ thích ứng để hạn chế KL quá lớn; PPO-Clip không có hạng KL tường minh hay ràng buộc cứng. Hai nhánh chia sẻ tỷ số $w_t$ và lợi thế, khác nhau ở cơ chế kiểm soát bước.

**Ví dụ/ứng dụng.** Danh mục tự đọc: Williams (1992) REINFORCE; Schulman et al. (2015) TRPO; Schulman et al. (2016) GAE; Schulman et al. (2017) PPO; Weng (2018) tổng quan họ gradient chính sách; Engstrom et al. (2020) Implementation Matters; Jin, Li & Wang (2024) stationary-point convergence của PPO-Clip; Xie et al. (2025) SPO; Lee & Yoon (2025) flat reward.

**Giới hạn.** Không mở A3C/A2C, DPG/DDPG, SAC/TD3, IMPALA/PPG, SPO hoặc SAM+PPO thành tuyến nội dung của bài; chúng chỉ là nhánh tiếp theo để tự đọc.


## Bài tập

::: exercise X01 — Baseline Bernoulli và GAE qua terminal/truncation
1. Với $A\sim\operatorname{Bernoulli}(p)$, $p=0{,}25$, $b(s)=4$ và hàm điểm theo logit là $A-p$, kiểm tra $\mathbb E[4(A-p)]=0$.
2. Với $\gamma=0{,}9$, $\lambda=0{,}8$, $V(S_0)=2$, $V(S_1)=3$, $R_1=1$, $R_2=2$: tính $\widehat A_0^{\mathrm{raw}}$ cho (a) episode kết thúc tại $T=2$ và (b) rollout ngoại sinh dừng tại $H=2<T$ với $V(S_2)=4$.
3. Nêu $(m_t,c_t)$ cho terminal, truncation ngoại sinh có quan sát cuối, và chân trời thuộc MDP.
:::

::: hint
Câu 1: viết kỳ vọng theo hai giá trị của $A$. Câu 2: áp dụng $\delta_t=R_{t+1}+\gamma m_tV_{\mathrm{old}}(S_{t+1})-V_{\mathrm{old}}(S_t)$ rồi đệ quy $\widehat A_t^{\mathrm{raw}}=\delta_t+\gamma\lambda c_t\widehat A_{t+1}^{\mathrm{raw}}$ với $c$ bằng 0 ở bước cuối. Câu 3: chỉ truncation ngoại sinh có quan sát cuối hợp lệ mới bootstrap.
:::

::: solution
1. $\mathbb E[4(A-p)]=4[0{,}25(0{,}75)+0{,}75(-0{,}25)]=0$.
2. (a) Terminal: theo quy ước có hai chuyển tiếp $t=0,1$ và $S_2$ là trạng thái terminal ở $T=2$, dùng $m_0=1$: $\delta_0=1+0{,}9\cdot1\cdot3-2=1{,}7$; $\delta_1=2-3=-1$; $\widehat A_0^{\mathrm{raw}}=1{,}7+0{,}72(-1)=0{,}98$. (b) Truncation: $\delta_1=2+0{,}9\cdot4-3=2{,}6$; $\widehat A_0^{\mathrm{raw}}=1{,}7+0{,}72(2{,}6)=3{,}572$.
3. Terminal và chân trời thuộc MDP dùng $(m,c)=(0,0)$; truncation ngoại sinh có quan sát cuối dùng $(1,0)$.
:::

::: exercise X02 — Bước natural gradient 2D
Cho $F=\operatorname{diag}(4,1)$, $g=(2,1)$, $\delta=0{,}01$ và $\eta=0$ (ví dụ giả sử $F$ xác định dương).
1. Tính $F^{-1}g$ và $g^\top F^{-1}g$.
2. Tính $\Delta^*=\sqrt{2\delta/(g^\top F^{-1}g)}\,F^{-1}g$.
3. Kiểm tra ràng buộc $\tfrac12(\Delta^*)^\top F\Delta^*\le\delta$ và giải thích tác dụng của $F$; nêu tiêu chí line search khi nhận bước.
:::

::: hint
Với $F$ chéo, nghịch đảo là lấy nghịch đảo từng đường chéo. Tiêu chí nhận bước cần đồng thời cải thiện surrogate và KL thực nghiệm trong biên.
:::

::: solution
1. $F^{-1}g=(0{,}5,1)$; $g^\top F^{-1}g=2\cdot0{,}5+1\cdot1=2$.
2. $\Delta^*=\sqrt{0{,}02/2}\,(0{,}5,1)=(0{,}05,0{,}1)$.
3. $\tfrac12(\Delta^*)^\top F\Delta^*=\tfrac12(4\cdot0{,}0025+0{,}01)=\tfrac12(0{,}01+0{,}01)=0{,}01\le0{,}01$: ràng buộc thỏa (chạm biên). Fisher làm bước nhỏ hơn ở tọa độ có độ cong lớn (tọa độ đầu) dù gradient thô ở đó không nhỏ hơn. Line search chỉ nhận ứng viên vừa tăng surrogate vừa có KL thực nghiệm $\le\delta$; ứng viên chỉ thỏa một trong hai tiêu chí bị từ chối.
:::

::: exercise X03 — Kiểm toán một batch PPO
1. Với rollout $H$ bước, $N$ môi trường, ghi shape của hành động rời rạc và log-probability trong batch phẳng.
2. Cho $\log\pi_\theta=-0{,}9$ và $\log\pi_{\mathrm{old}}=-1{,}1$: tính $w$.
3. Với $\epsilon=0{,}2$ và $\widehat A^{\mathrm{actor}}=2$: tính hạng PPO-Clip khi $w=1{,}3$ và khi $w=0{,}7$; lặp lại với $\widehat A^{\mathrm{actor}}=-2$.
4. Tại biên cuối rollout, chọn dữ liệu bootstrap cho terminal và cho truncation nhân tạo.
5. Giải thích ý nghĩa của clipfrac cao và phản ứng có điều kiện khi KL tăng kèm entropy giảm.
:::

::: hint
Câu 2: $w=\exp(\log\pi_\theta-\log\pi_{\mathrm{old}})$. Câu 3: áp dụng công thức theo dấu lợi thế. Câu 4: nhớ `final_observation` được lưu trước reset. Câu 5: clipfrac đo tỷ số ngoài dải, không đo đoạn phẳng.
:::

::: solution
1. $B=HN$; hành động rời rạc và log-probability đều có shape $[B]$.
2. $w=e^{-0{,}9-(-1{,}1)}=e^{0{,}2}\approx1{,}221$.
3. $\widehat A=2$: $w=1{,}3>1{,}2$ nằm ngoài dải phía cải thiện nên $\ell=(1{,}2)(2)=2{,}4$; $w=0{,}7<0{,}8$ cũng ngoài dải nhưng ở phía bất lợi nên mục tiêu không bị làm phẳng, giữ $\ell=0{,}7\cdot2=1{,}4$. $\widehat A=-2$: $w=0{,}7<0{,}8$ ngoài dải phía cải thiện nên $\ell=(0{,}8)(-2)=-1{,}6$; $w=1{,}3>1{,}2$ ngoài dải nhưng phía bất lợi nên $\ell=1{,}3\cdot(-2)=-2{,}6$.
4. Terminal: không bootstrap, $(m,c)=(0,0)$. Truncation nhân tạo: bootstrap từ $V_{\mathrm{old}}$ của `final_observation` lưu trước reset, $(m,c)=(1,0)$; không dùng quan sát reset.
5. Clipfrac cao chỉ nói nhiều tỷ số nằm ngoài $[1-\epsilon,1+\epsilon]$, không đồng nghĩa mọi mẫu ở đoạn phẳng (còn phụ thuộc dấu lợi thế). Nếu KL tăng kèm entropy giảm, có thể giảm learning rate, giảm số epoch $K$ hoặc dừng sớm theo KL; phản ứng là có điều kiện, không có ngưỡng chung.
:::

## Tài liệu tham khảo

- Williams, R. J. (1992). Simple statistical gradient-following algorithms for connectionist reinforcement learning.
- Schulman et al. (2015). Trust Region Policy Optimization, Eq. 1–7.
- Schulman et al. (2016). High-Dimensional Continuous Control Using Generalized Advantage Estimation.
- Schulman et al. (2017). Proximal Policy Optimization Algorithms.
- Weng, L. (2018). Policy Gradient Algorithms, Lil'Log.
- Engstrom et al. (2020). Implementation Matters in Deep Policy Gradients: A Case Study on PPO and TRPO.
- Jin, R., Li, S., & Wang, B. (2024). On Stationary Point Convergence of PPO-Clip, ICLR 2024, Định lý 3.1 và Giả thiết 3.1, 3.2, 3.4.
- Xie et al. (2025). Simple Policy Optimization.
- Lee & Yoon (2025). Flat Reward in Policy Parameter Space Implies Robust Reinforcement Learning.
- Nguồn bài giảng: PDF Bài 10, tr. 1–43; đường dẫn chính xác được lưu trong nhật ký rà soát.
