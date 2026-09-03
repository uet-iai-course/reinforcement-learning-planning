# Bài 12 — Nhập môn Học tăng cường đa tác tử

## Mục tiêu và kiến thức tiên quyết

- Viết đúng hợp đồng trò chơi Markov dưới quan sát cục bộ, hành động chung, reward regime và cân bằng Nash.
- Giải thích huấn luyện tập trung, thực thi phân tán (CTDE) và phân biệt CTDE với giao tiếp khi chạy.
- Tính được baseline COMA, một bước TD của QMIX, target MADDPG và objective MAPPO/HAPPO.
- Chọn được benchmark theo hành động, quan sát, phần thưởng và số tác tử.
- Kiểm tra được giới hạn bằng chứng, phiên bản framework và hợp đồng giao tiếp.

Tiên quyết từ Bài 11 (không giảng lại): định lý gradient chính sách, actor–critic, DDPG, PPO-Clip. Nguồn là bản trích PPTX 54 trang, không có ghi chú và không có code demo; note không sinh code.

## Bản đồ chủ đề

| note-topic-id | chủ đề | nhóm | trang nguồn |
|---|---|---|---|
| `lec-12-topic-01` | Hai cách mở rộng MARL và MDP cảm sinh | cốt lõi | 4–5 |
| `lec-12-topic-02` | Hợp đồng trò chơi Markov, reward regime, Nash | cốt lõi | 6–9 |
| `lec-12-topic-03` | CTDE và phân biệt với giao tiếp khi chạy | cốt lõi | 8, 10 |
| `lec-12-topic-04` | COMA: gradient đa tác tử và baseline phản thực | cốt lõi | 12 |
| `lec-12-topic-05` | VDN và QMIX: phân rã giá trị, IGM, bước TD | cốt lõi | 14 |
| `lec-12-topic-06` | MADDPG: chain rule tất định, critic tập trung, target | cốt lõi | 13 |
| `lec-12-topic-07` | MAPPO/IPPO: tỷ số theo tác tử | cốt lõi | 15–16 |
| `lec-12-topic-08` | HAPPO/HATRPO: cập nhật tuần tự, multiplier | cốt lõi | 17–18 |
| `lec-12-topic-09` | Benchmark MARL | cốt lõi | 19–38 |
| `lec-12-topic-10` | Giao tiếp trong MARL | cốt lõi | 47–54 |
| `lec-12-topic-11` | Ôn policy gradient và actor–critic đơn tác tử | cầu nối | 12–13 |
| `lec-12-topic-12` | Ôn PPO đơn tác tử | cầu nối | 15–17 |
| `lec-12-topic-13` | Framework MARL: PyMARL/EPyMARL, MARLlib, HARL | bổ sung | 39–46 |
| `lec-12-topic-14` | AutoGen, Neural MMO, OpenAI Five | đọc thêm | 34–38 |
| `lec-12-topic-15` | Danh mục tài liệu tham khảo | đọc thêm | 12–54 |

Ngân sách thời gian. Tuyến chính 110 phút: mở bài và kết bài 8 phút; T1–T3 25 phút; T4 15 phút; T5 15 phút; T6–T8 18 phút; T9 19 phút; T10 10 phút. Phần linh hoạt 10 phút: topic-13 (B1, framework) 6 phút; phần tích hợp và mô hình đe dọa trong T10 4 phút. Bài tập X01–X03 dùng 30 phút ngoài phần trình chiếu. C1 và C2 được gộp vào cụm liên quan.

## Ký hiệu và quy ước

- $\mathcal N=\{1,\ldots,N\}$: tập tác tử; $\Delta(\mathcal X)$: tập phân phối trên $\mathcal X$.
- $S_t\in\mathcal S$: trạng thái môi trường; $O_{t,i}\in\mathcal O_i$: quan sát cục bộ.
- $\tau_{t,i}=(o_{0,i},a_{0,i},\ldots,a_{t-1,i},o_{t,i})\in\mathcal T_i$: lịch sử cục bộ của tác tử $i$.
- $\mathbf A_t\in\prod_i\mathcal A_i$: hành động chung; $|\mathcal A|=\prod_i|\mathcal A_i|$.
- $P:\mathcal S\times\mathcal A\to\Delta(\mathcal S)$: kernel chuyển tiếp nền; $\Omega:\mathcal S\to\Delta(\mathcal O)$: kernel quan sát.
- $r_i:\mathcal S\times\mathcal A\to\mathbb R$: phần thưởng của tác tử $i$; $\gamma\in[0,1]$.
- $\pi_i:\mathcal T_i\to\Delta(\mathcal A_i)$: policy phân tán; $\pi_{-i}$: policy của các tác tử khác.
- $P_i^{\pi_{-i}},r_i^{\pi_{-i}}$: chuyển tiếp và reward cảm sinh khi cố định $\pi_{-i}$.
- $Q(s,\mathbf a)$: critic tập trung chung trong COMA; $Q_i(x,\mathbf a)$: critic riêng của tác tử $i$ trong MADDPG, $x$ là input chung.
- $Q_i(\tau_i,a_i)$, $Q_{\mathrm{tot}}$: utility cục bộ và joint action-value trong VDN/QMIX.
- $\mu_i(o_i)$: actor tất định của MADDPG; $D_{\theta_i}\mu_i$: Jacobian actor.
- $\theta,\bar\theta$: tham số online và target; $m=1-d$: mặt nạ terminal thật ($d=1$ chỉ ở terminal).
- $r_{t,i}(\theta_i)$: tỷ số policy mới/cũ của tác tử $i$ trong MAPPO; $M_m$: multiplier HAPPO.
- Kỳ vọng $\mathbb E$ lấy theo phân phối đầu, kernel chuyển tiếp, kernel quan sát và joint policy, trừ khi nêu khác.

<!-- note-topic-id: lec-12-topic-01 -->

## Hai cách mở rộng MARL từ một tác tử

**Vấn đề.** Trong RL đơn tác tử, $P(s'\mid s,\mathbf a)$ cố định. Khi nhiều tác tử cùng học, dữ liệu mà một tác tử nhìn thấy đổi theo policy của các tác tử khác.

**Trực giác.** Hai góc nhìn: (i) gộp mọi tác tử thành một siêu tác tử điều khiển hành động chung trên kernel nền $P$ cố định; quá trình nhìn từ bộ học duy nhất này là dừng, nhưng không gian quyết định tăng theo tích; (ii) nhìn theo từng tác tử với hành động nhỏ hơn, nhưng MDP cảm sinh $P_i^{\pi_{-i}}$ thay đổi khi $\pi_{-i}$ đổi. Tính không dừng đến từ các chính sách đang học, không bắt buộc đến từ môi trường nền.

**Ví dụ tính tay.** Ba tác tử có lần lượt $2,3,4$ hành động: $|\mathcal A|=2\times3\times4=24$. Với $N$ tác tử cùng $K$ hành động, $|\mathcal A|=K^N$; với $N=10$, $K=5$: $5^{10}=9\,765\,625$.

**Hình thức.** Với hành động rời rạc, quan sát đầy đủ và joint policy phân rã:

$$P_i^{\pi_{-i}}(s'\mid s,a_i)=\sum_{\mathbf a_{-i}}P(s'\mid s,(a_i,\mathbf a_{-i}))\prod_{j\ne i}\pi_j(a_j\mid s),\qquad r_i^{\pi_{-i}}(s,a_i)=\sum_{\mathbf a_{-i}}r_i(s,(a_i,\mathbf a_{-i}))\prod_{j\ne i}\pi_j(a_j\mid s).$$

Tích policy giả định hành động cục bộ độc lập có điều kiện theo $s$; nếu có tương quan chung, thay tích bằng phân phối joint có điều kiện. Với hành động liên tục, thay tổng bằng tích phân.

**Ứng dụng và giới hạn.** Góc nhìn siêu tác tử không làm dữ liệu độc lập hay giảm kích thước joint action; các họ phân rã giá trị và centralized critic giữ cấu trúc đa tác tử thay vì liệt kê. Dưới quan sát cục bộ, quá trình nhìn chỉ qua $s$ không nhất thiết là MDP đối với tác tử.

**Kiểm tra.** Khi $\pi_{-i}$ đổi, $P$ và $r$ nền không bắt buộc đổi; đổi là $P_i^{\pi_{-i}}$ và $r_i^{\pi_{-i}}$.

**Nguồn:** tr. 4–6; Littman (1994).

**Nối ra:** hợp đồng trò chơi Markov ở topic kế chính thức hóa các miền này.

<!-- note-topic-id: lec-12-topic-02 -->

## Hợp đồng trò chơi Markov, reward regime và Nash

**Vấn đề.** Cần một hợp đồng duy nhất nêu rõ ai thấy gì, ai chọn gì, ai được gì.

**Trực giác.** Mỗi bước, môi trường phát quan sát cho từng tác tử; mỗi tác tử trả một hành động cục bộ; môi trường chuyển trạng thái và trả phần thưởng riêng cho từng tác tử.

**Hình thức.**

$$G=(\mathcal N,\mathcal S,\{\mathcal O_i\},\{\mathcal A_i\},P,\Omega,\{r_i\},\gamma),\qquad \mathcal A=\prod_i\mathcal A_i,\quad \mathcal O=\prod_i\mathcal O_i.$$

Lịch sử cục bộ $\tau_{t,i}\in\mathcal T_i$ và policy phân tán $\pi_i:\mathcal T_i\to\Delta(\mathcal A_i)$. Với phân phối đầu $\rho_0$ và chân trời $H$:

$$J_i(\boldsymbol\pi)=\mathbb E_{\rho_0,\boldsymbol\pi,P,\Omega}\!\left[\sum_{t=0}^{H-1}\gamma^t r_i(S_t,\mathbf A_t)\right].$$

Cân bằng Nash: $J_i(\pi_i^*,\pi_{-i}^*)\ge J_i(\pi_i,\pi_{-i}^*)$ với mọi $i$ và mọi $\pi_i$; lệch đơn phương của một tác tử không tăng return của chính tác tử đó.

**Reward regime.**

| regime | điều kiện |
|---|---|
| hợp tác hoàn toàn | $r_1=\cdots=r_N=r$ |
| zero-sum | $\sum_i r_i(s,\mathbf a)=0$ (constant-sum: tổng là hằng số) |
| general-sum | $\mathbf r=(r_1,\ldots,r_N)\in\mathbb R^N$ |

Với hơn hai tác tử, zero-sum không có nghĩa mọi cặp đều đối kháng.

**Ứng dụng và giới hạn.** Trong trò chơi hợp tác hoàn toàn, joint policy tối đa hóa return chung là một cân bằng Nash; chiều ngược lại không nhất thiết đúng. Quan hệ "tối ưu chung suy ra Nash" chỉ được dùng với common payoff. Self-play là cách sinh dữ liệu trong trò chơi cạnh tranh, không phải một loại reward riêng.

**Kiểm tra.** Nếu $J_i(\pi_i^*,\pi_{-i}^*)=5$ nhưng một lệch đơn phương cho $5{,}4$, thì $\boldsymbol\pi^*$ không phải Nash.

**Nguồn:** tr. 6–9; Littman (1994).

**Nối ra:** CTDE ở topic kế là hợp đồng về miền thông tin trên nền hợp đồng này.

<!-- note-topic-id: lec-12-topic-03 -->

## CTDE và phân biệt với giao tiếp khi chạy

**Vấn đề.** Muốn dùng thông tin chung khi học mà vẫn thực thi phân tán khi chạy.

**Trực giác.** CTDE là hợp đồng về miền thông tin: critic hoặc mixer có thể dùng trạng thái và hành động chung trong huấn luyện; actor chỉ dùng $\tau_i$ khi chạy. CTDE không bắt buộc các tác tử gửi thông điệp khi chạy.

**Hình thức.** Bản đồ các hiện thân CTDE:

| họ | thành phần tập trung | thành phần phân tán |
|---|---|---|
| COMA | critic $Q(s,\mathbf a)$ | actor $\pi_i(a_i\mid\tau_i)$ |
| MADDPG | critic $Q_i(x,\mathbf a)$ | actor tất định $\mu_i(o_i)$ |
| VDN | tổng $Q_{\mathrm{tot}}$ khi học | $Q_i(\tau_i,a_i)$ để chọn tham lam |
| QMIX | mixer $Q_{\mathrm{tot}}(\cdot,s)$ khi học | $Q_i(\tau_i,a_i)$ để chọn tham lam |
| MAPPO | value tập trung khi học | actor cục bộ |

**Ứng dụng và giới hạn.** Nếu actor nhận message, message phải thật sự có ở execution; đó là giao tiếp khi chạy, một phụ thuộc riêng ngoài CTDE (chi tiết ở topic 10). Bốn trục gây khó đi kèm: gán công, đồng nhất và chia sẻ tham số (thêm agent ID/vai trò khi actor phải phân biệt tác tử), quan sát cục bộ, khác biệt tác tử.

**Kiểm tra.** Actor thấy $s$ khi học nhưng chỉ thấy $\tau_i$ khi chạy là vi phạm hợp đồng CTDE; chỉ value learner được dùng thông tin tập trung.

**Nguồn:** tr. 8, 10; Foerster et al. (2018); Buşoniu, Babuška & De Schutter (2010).

**Nối ra:** qua cầu nối ôn policy gradient, COMA ở topic 04 là hiện thân CTDE đầu tiên trên mạch thuật toán.

<!-- note-topic-id: lec-12-topic-11 -->

## Cầu nối: policy gradient và actor–critic đơn tác tử

**Vấn đề.** Nguồn trang 12 mở COMA bằng "Recall the policy gradient theorem in the single agent settings", nhưng bản trích mất ký hiệu công thức. Cần tái lập trước khi mở rộng.

**Hình thức.** Với policy $\pi_\theta$ và return $J(\theta)$:

$$\nabla_\theta J=\mathbb E_{\pi_\theta}\!\left[\nabla_\theta\log\pi_\theta(A_t\mid S_t)\,\widehat A_t\right].$$

Actor–critic thêm critic $V_\phi$ làm baseline; advantage $\widehat A_t$ thay return Monte Carlo để giảm phương sai. Hai thành phần này là nguyên liệu trực tiếp của COMA (critic tập trung + score function cục bộ) và MADDPG (bản tất định của cùng cấu trúc).

**Nguồn:** tr. 12–13; Foerster et al. (2018); Lowe et al. (2017).

**Nối ra:** COMA ở topic 04 giữ đúng cấu trúc score function, chỉ đổi baseline và miền thông tin của critic; MADDPG ở topic 06 là bản tất định của cùng cấu trúc, sẽ gặp sau nhánh giá trị rời rạc.

<!-- note-topic-id: lec-12-topic-04 -->

## COMA: gradient đa tác tử và baseline phản thực

**Vấn đề.** Phạm vi: hợp tác hoàn toàn, return chung, hành động rời rạc. Reward chung không nói tác tử nào đóng góp; nếu mọi actor nhận cùng tín hiệu $Q(s,\mathbf a)$, gán công bị mất.

**Trực giác.** Giữ $\mathbf a_{-i}$ cố định và so hành động đã chọn của tác tử $i$ với các hành động thay thế của chính tác tử đó. Đây là phép so phản thực. Trọng số của từng lựa chọn phản thực là xác suất dưới chính policy của tác tử $i$.

**Ví dụ tính tay.** Giữ $a_{-i}$ cố định; tác tử $i$ có hai hành động:

| $a_i'$ | $\pi_i(a_i'\mid\tau_i)$ | $Q(s,(a_{-i},a_i'))$ |
|---|---|---|
| trái | $0{,}25$ | $2$ |
| phải | $0{,}75$ | $6$ |

$$b_i=0{,}25\times2+0{,}75\times6=5.$$

Hành động thực là "phải": $A_i^{\mathrm{COMA}}=6-5=1$; nếu là "trái": $A_i^{\mathrm{COMA}}=2-5=-3$. Ví dụ chỉ thế số vào công thức, không phải dữ liệu thực nghiệm.

**Hình thức.**

$$b_i(s_t,\mathbf a_{t,-i})=\sum_{a_i'}\pi_i(a_i'\mid\tau_{t,i})\,Q\bigl(s_t,(\mathbf a_{t,-i},a_i')\bigr),$$

$$A_i^{\mathrm{COMA}}(s_t,\mathbf a_t)=Q(s_t,\mathbf a_t)-b_i(s_t,\mathbf a_{t,-i}),$$

$$g=\mathbb E\!\left[\sum_t\gamma^t\sum_i\nabla_{\theta_i}\log\pi_i(a_{t,i}\mid\tau_{t,i})\,A_i^{\mathrm{COMA}}(s_t,\mathbf a_t)\right].$$

Baseline phụ thuộc $s_t$ và $\mathbf a_{t,-i}$ nhưng không phụ thuộc hành động thực của $i$ sau khi lấy kỳ vọng, nên không làm thay đổi kỳ vọng score-function gradient trong điều kiện chuẩn. Bỏ trọng số $\pi_i$ trong tổng sẽ cho một đại lượng khác.

**Ứng dụng và giới hạn.** Phải đánh giá $Q$ cho mọi hành động thay thế của tác tử $i$; critic tập trung cần thông tin chung khi học; đường cơ sở xử lý gán công cục bộ, không loại bỏ mọi nguồn phương sai. Nếu $|\mathcal A_i|$ tăng từ $5$ lên $100$, tổng baseline phải đánh giá $100$ hành động thay thế; với hành động liên tục, phép tổng chính xác trở nên khó.

**Kiểm tra.** Với bảng trên: $b_i=5$; $A_i^{\mathrm{COMA}}=1$ cho "phải"; baseline có trọng số policy; actor khi chạy vẫn chỉ dùng $\tau_i$.

**Nguồn:** tr. 12; Foerster et al. (2018).

**Nối ra:** COMA trả giá bằng critic và tổng hành động; cụm kế đổi sang phân rã giá trị để thực thi tham lam cục bộ.

<!-- note-topic-id: lec-12-topic-05 -->

## VDN và QMIX: phân rã giá trị, IGM và một bước TD

**Vấn đề.** Phạm vi: hợp tác hoàn toàn, return chung, hành động rời rạc. Khi chạy, mỗi tác tử chỉ có $\tau_i$, nhưng $Q_{\mathrm{tot}}(\boldsymbol\tau,\mathbf a,s)$ phải cho quyết định tham lam chung khớp với các quyết định tham lam cục bộ.

**Trực giác.** VDN chọn hợp đồng đơn giản nhất: cộng các giá trị cục bộ. QMIX nới hợp đồng bằng mixer đơn điệu phụ thuộc trạng thái, đổi tính giàu biểu diễn lấy bằng ràng buộc đơn điệu.

**Ví dụ tính tay.** Hai tác tử có utility $Q_1=(1,3)$, $Q_2=(2,5)$ (các giá trị không âm); $q_1=3$, $q_2=5$ tại các cực đại cục bộ:

$$Q_{\mathrm{tot}}=2q_1+q_2+0{,}1q_1q_2=6+5+1{,}5=12{,}5.$$

Trên miền không âm, hai đạo hàm riêng đều dương: tăng từng utility thì $Q_{\mathrm{tot}}$ không giảm, nên tổ hợp cực đại cục bộ cũng là cực đại chung trong lớp đang xét.

**Hình thức.** VDN:

$$Q_{\mathrm{tot}}(\boldsymbol\tau,\mathbf a)=\sum_{i=1}^{N}Q_i(\tau_i,a_i),\qquad \prod_{i=1}^{N}\arg\max_{a_i}Q_i(\tau_i,a_i)=\arg\max_{\mathbf a}\sum_{i=1}^{N}Q_i(\tau_i,a_i).$$

Đẳng thức tập hợp giữ cả khi có nhiều hành động đồng cực đại. QMIX:

$$Q_{\mathrm{tot}}(\boldsymbol\tau,\mathbf a,s)=f_{\mathrm{mix}}(Q_1,\ldots,Q_N;s),\qquad \frac{\partial Q_{\mathrm{tot}}}{\partial Q_i}\ge0,$$

$$\prod_{i=1}^{N}\arg\max_{a_i\in\mathcal A_i}Q_i(\tau_i,a_i)\ \subseteq\ \arg\max_{\mathbf a\in\mathcal A}Q_{\mathrm{tot}}(\boldsymbol\tau,\mathbf a,s).$$

Argmax là tập khi có hòa, nên viết quan hệ bao hàm tập hợp, không viết hai argmax như các vector bằng nhau. Điều kiện đơn điệu không nghiêm có thể cho thêm joint maximizer ngoài tích các local argmax, nên dùng $\subseteq$ thay vì đẳng thức. State $s$ chỉ đi vào mixer/hypernetwork khi học; hypernetwork sinh trọng số không âm để áp điều kiện đơn điệu.

**Thuật toán (một bước TD của QMIX).** Lấy từ replay một mẫu $(\boldsymbol\tau_t,s_t,\mathbf a_t,r_t,\boldsymbol\tau_{t+1},s_{t+1},d_t)$ với reward chung; đặt $m_t=1-d_t$, $d_t=1$ chỉ ở terminal thật:

$$a_{t+1,i}^{*}\in\arg\max_{a_i\in\mathcal A_i^{\mathrm{avail}}}Q_i(\tau_{t+1,i},a_i;\theta),$$

$$y_t=r_t+\gamma m_t\,Q_{\mathrm{tot}}^{-}(\boldsymbol\tau_{t+1},\mathbf a_{t+1}^{*},s_{t+1};\bar\theta),\qquad \mathcal L(\theta)=\mathbb E\bigl[(y_t-Q_{\mathrm{tot}}(\boldsymbol\tau_t,\mathbf a_t,s_t;\theta))^2\bigr].$$

Double-Q: utility online chọn $\mathbf a_{t+1}^{*}$; utility target và mixer target đánh giá. Loss chỉ backprop qua $Q_{\mathrm{tot}}(\boldsymbol\tau_t,\mathbf a_t,s_t;\theta)$; argmax là phép chọn rời rạc và dừng gradient; $y_t$ dừng gradient. Cutoff chưa terminal có $d_t=0$ nên mask vẫn giữ bootstrap. Cập nhật target stack theo chu kỳ hoặc trung bình Polyak đúng cấu hình.

**Ví dụ kiểm công thức target.** $r=1{,}5$, $\gamma=0{,}9$, $m=1$, target $Q_{\mathrm{tot}}^{-}=4$: $y=1{,}5+0{,}9\times1\times4=5{,}1$. Nếu online $Q_{\mathrm{tot}}(\boldsymbol\tau_t,\mathbf a_t,s_t;\theta)=4{,}6$ thì sai số bình phương $(5{,}1-4{,}6)^2=0{,}25$. Ở terminal thật, $d=1$ nên $m=0$ và $y=r=1{,}5$; mask loại bỏ hẳn hạng bootstrap.

**Ứng dụng và giới hạn.** VDN dễ tối ưu và thực thi phân tán nhưng không biểu diễn tương tác phi cộng; QMIX giàu hơn (mixer phi tuyến, phụ thuộc trạng thái) nhưng không biểu diễn mọi joint $Q$ có tương tác không đơn điệu. Một joint $Q$ giảm khi $Q_1$ tăng vi phạm đạo hàm không âm. Không kết luận QMIX luôn tốt hơn VDN; điều đó phụ thuộc task, tối ưu và giao thức benchmark.

**Kiểm tra.** Ví dụ trên: $Q_{\mathrm{tot}}=12{,}5$; quan hệ $\subseteq$ đúng cả khi có hòa; terminal thật đặt $m_t=0$, cutoff chưa terminal đặt $m_t=1$.

**Nguồn:** tr. 14; Sunehag et al. (2018); Rashid et al. (2020).

**Nối ra:** sau giá trị rời rạc, mạch kế nối từ DDPG của Bài 11 sang hành động liên tục và mixed tasks.

<!-- note-topic-id: lec-12-topic-06 -->

## MADDPG: chain rule tất định, critic tập trung, target

**Vấn đề.** Hành động liên tục và mixed tasks: cần actor tất định từng tác tử với critic tập trung, và target không được trộn hành động online với hành động target.

**Trực giác.** Mỗi tác tử $i$ có critic riêng $Q_{i,\phi_i}(x,\mathbf a)$ trên input chung $x$ (joint observation hoặc state) và mọi hành động; actor cục bộ $\mu_i(o_i)$ chỉ thấy quan sát của mình. Dữ liệu thu bằng policy khám phá, chẳng hạn thêm nhiễu vào actor tất định; target actor chỉ tạo hành động trong target.

**Ví dụ số về shape.** Với $d_{a_i}=2$, $d_{\theta_i}=5$: $D_{\theta_i}\mu_i\in\mathbb R^{2\times5}$, $\nabla_{a_i}Q_i\in\mathbb R^{2}$, nên $D_{\theta_i}\mu_i^\top\nabla_{a_i}Q_i\in\mathbb R^{5}$. Gradient đi qua critic theo đúng thành phần hành động của tác tử $i$.

**Hình thức.**

$$\nabla_{\theta_i}J=\mathbb E_{\mathcal D}\!\left[D_{\theta_i}\mu_i(o_i)^\top\nabla_{a_i}Q_{i,\phi_i}(x,a_1,\ldots,a_N)\right]_{a_i=\mu_i(o_i)},$$

$$y_i=r_i+\gamma m\,Q_{i,\bar\phi_i}\!\left(x',\mu_{1,\bar\theta_1}(o_1'),\ldots,\mu_{N,\bar\theta_N}(o_N')\right).$$

Đây là chain rule tất định, không phải score function ngẫu nhiên. Target dùng mọi target actor $\mu_{j,\bar\theta_j}$; không thay hành động tác tử khác bằng hành động online trong target. $m=1-d$ với $d$ là terminal thật; time-limit truncation chưa terminal không đặt $m=0$. Critic online của $i$ tối thiểu hóa bình phương sai số với $y_i$ đã dừng gradient.

**Ứng dụng và giới hạn.** MADDPG còn bao phủ mixed cooperative–competitive tasks, trong khi các họ rời rạc ở trên tập trung hợp tác. Kỳ vọng trên replay là surrogate thực hành, không phải định lý on-policy không chệch.

**Kiểm tra.** Actor dùng $o_i$; critic dùng $x,\mathbf a$; critic đích dùng $x'$ và mọi target actor; $m$ là terminal thật.

**Nguồn:** tr. 13; Lowe et al. (2017).

**Nối ra:** từ actor tất định sang on-policy stochastic: cầu nối PPO ở topic kế ôn lại tỷ số và clip trước khi vào MAPPO.

<!-- note-topic-id: lec-12-topic-12 -->

## Cầu nối: PPO đơn tác tử

**Vấn đề.** MAPPO/IPPO/HAPPO là mở rộng trực tiếp của PPO/TRPO; nguồn trang 15–17 không nhắc lại PPO.

**Hình thức.** Với tỷ số $w_t=\pi_\theta(a_t\mid s_t)/\pi_{\mathrm{old}}(a_t\mid s_t)$:

$$L^{\mathrm{clip}}=\mathbb E_t\!\left[\min\!\left(w_t\widehat A_t,\ \operatorname{clip}(w_t,1-\epsilon,1+\epsilon)\widehat A_t\right)\right].$$

Ba dữ kiện mang sang MARL: tỷ số mới/cũ; dấu lợi thế quyết định hướng cập nhật; batch cũ giữ $\log\pi_{\mathrm{old}}$, lợi thế và target cố định trong các epoch. MAPPO thêm chỉ số tác tử vào tỷ số; HAPPO thêm multiplier tuần tự.

**Nguồn:** tr. 15–17; Yu et al. (2022); Kuba et al. (2021/2022).

**Nối ra:** ba dữ kiện trên đủ để đọc topic 07 và 08.

<!-- note-topic-id: lec-12-topic-07 -->

## MAPPO/IPPO: tỷ số theo tác tử

**Vấn đề.** PPO đơn tác tử có một policy và một tỷ số; đa tác tử có $N$ policy, mỗi policy thấy lịch sử riêng, nên tỷ số phải mang chỉ số tác tử.

**Trực giác.** IPPO và MAPPO khác nhau chỉ ở miền của bộ học giá trị: IPPO dùng thông tin cục bộ, MAPPO dùng hàm giá trị tập trung khi học. Actor khi chạy vẫn dùng thông tin cục bộ trong cả hai.

**Ví dụ số.** Tác tử $i$ có $r_{t,i}(\theta_i)=1{,}3$, $\widehat A_t=2$, $\epsilon=0{,}2$: nhánh min là $\min(1{,}3\times2,\ \operatorname{clip}(1{,}3,0{,}8,1{,}2)\times2)=\min(2{,}6,\ 2{,}4)=2{,}4$. Advantage được tính dưới policy cũ và giữ cố định qua các epoch; triển khai có thể chuẩn hóa nó trên batch đã cố định.

**Hình thức.**

$$r_{t,i}(\theta_i)=\frac{\pi_{\theta_i}(a_{t,i}\mid\tau_{t,i})}{\pi_{\theta_{i,\mathrm{old}}}(a_{t,i}\mid\tau_{t,i})},$$

$$L^{\mathrm{clip}}=\mathbb E_{t,i}\!\left[\min\!\left(r_{t,i}(\theta_i)\widehat A_t,\ \operatorname{clip}(r_{t,i}(\theta_i),1-\epsilon,1+\epsilon)\widehat A_t\right)\right].$$

Tỷ số dùng hành động, lịch sử và tham số của đúng tác tử $i$. Nếu actor chia sẻ tham số, $\theta_i$ trỏ cùng một bộ tham số nhưng dữ liệu vẫn mang chỉ số agent/role khi cần. Centralized value learner tạo target và advantage chung khi học; nó không trở thành đầu vào actor khi chạy.

**Ứng dụng và giới hạn.** Phạm vi chọn trong bài: IPPO/MAPPO/HAPPO dùng hợp tác với return chung; MADDPG còn bao phủ mixed tasks. Đây là giới hạn sư phạm, không phải giới hạn tổng quát của mọi biến thể. Kết quả một benchmark không tạo thứ hạng chung giữa IPPO, MAPPO và các họ khác.

**Kiểm tra.** Actor thấy $s$ khi học nhưng chỉ thấy $\tau_i$ khi chạy: vi phạm miền input actor; chỉ value learner được dùng thông tin tập trung.

**Nguồn:** tr. 15–16; de Witt et al. (2020); Yu et al. (2022).

**Nối ra:** cập nhật đồng thời $N$ actor làm đổi bài toán của nhau; HAPPO xử lý tuần tự.

<!-- note-topic-id: lec-12-topic-08 -->

## HAPPO/HATRPO: cập nhật tuần tự và multiplier

**Vấn đề.** Sau khi actor $i_1$ đổi, joint policy không còn là policy đã tạo rollout; surrogate của các actor kế phải hiệu chỉnh theo actor đã đổi.

**Trực giác.** Chọn một hoán vị $i_1,\ldots,i_N$; cập nhật lần lượt và truyền ảnh hưởng qua một multiplier. Rollout và joint $\widehat A$ được tính một lần dưới policy cũ; không thu lại dữ liệu sau từng actor. Ví dụ: tỷ số của actor đầu là $1{,}1$ thì surrogate của actor kế dùng $1{,}1\widehat A$.

**Ví dụ tính tay.** $M_2=2{,}2$, $r_2(\theta)=1{,}3$, $\epsilon=0{,}2$: hạng clipped là $\min(1{,}3\times2{,}2,\ 1{,}2\times2{,}2)=\min(2{,}86,\ 2{,}64)=2{,}64$. Nếu $r_2^{\mathrm{new}}=0{,}9$ thì $M_3=0{,}9\times2{,}2=1{,}98$.

**Hình thức.** Đặt $M_1=\widehat A$. Khi cập nhật tác tử $i_m$, giữ $M_m$ cố định:

$$r_m(\theta)=\frac{\pi_{\theta}^{i_m}(a_{i_m}\mid\tau_{i_m})}{\pi_{\mathrm{old}}^{i_m}(a_{i_m}\mid\tau_{i_m})},$$

$$L_m^{\mathrm{clip}}=\mathbb E\!\left[\min\!\left(r_m(\theta)M_m,\ \operatorname{clip}(r_m(\theta),1-\epsilon,1+\epsilon)M_m\right)\right],$$

$$r_m^{\mathrm{new}}=r_m(\theta_m^*),\qquad M_{m+1}=r_m^{\mathrm{new}}M_m.$$

Không tái tính GAE hay thu rollout sau từng actor. Hoán vị ngẫu nhiên chỉ là một cách chọn thứ tự; hoán vị cần độ bao phủ thích hợp, không chỉ được gọi là "unbiased". Với advantage âm, nhánh min có tác dụng khác nên không suy luận kết quả clip chỉ bằng cắt ratio. HATRPO giữ nguyên cơ chế cập nhật tuần tự và multiplier như trên, nhưng thay objective clip bằng ràng buộc trust region (giới hạn KL giữa policy mới và cũ của từng actor trong bước cập nhật của actor đó); phần này không triển khai thêm chi tiết ở mức nguồn. Contour "reward tăng theo từng hướng 1D nhưng giảm theo hướng joint" chỉ giữ như động cơ định tính, không dùng làm claim định lượng.

**Ứng dụng và giới hạn.** Objective đúng chưa đủ để so thuật toán; so sánh cần benchmark và giao thức đánh giá khớp (topic kế).

**Kiểm tra.** $M_m=2$, $r_m^{\mathrm{new}}=0{,}9$ cho $M_{m+1}=1{,}8$; $M_m$ cố định khi tối ưu actor hiện tại.

**Nguồn:** tr. 17–18; Kuba et al. (2021/2022).

**Nối ra:** từ thuật toán sang bằng chứng: benchmark khóa giả thiết trước khi so.

<!-- note-topic-id: lec-12-topic-09 -->

## Benchmark MARL

**Vấn đề.** Objective đúng chưa đủ; so sánh chỉ có nghĩa khi các trục thông tin, quyết định, tín hiệu và giao thức đánh giá khớp.

**Trực giác.** Benchmark là một gói giả thiết: quan sát đầy đủ hay cục bộ, có global state khi học hay không; hành động rời rạc hay liên tục, đồng nhất hay khác vai trò, số tác tử; reward chung hay riêng, dày hay thưa, chân trời và tiêu chí dừng.

**Ví dụ.** Chọn benchmark cho hành động liên tục và quan sát cục bộ: MAMuJoCo chia các khớp của hệ điều khiển liên tục cho nhiều tác tử; phải khóa cách chia khớp và cấu hình quan sát. Ngược lại, SMAC là vi mô chiến đấu StarCraft II với quan sát cục bộ và hành động rời rạc.

| môi trường | đặc điểm cần ghi | phạm vi bằng chứng |
|---|---|---|
| MPE | 2D; task hợp tác, cạnh tranh và mixed | Lowe et al. (2017) |
| LBF | gridworld; quan sát đầy đủ hoặc cục bộ; reward mode phụ thuộc cấu hình | Christianos et al. (2020) |
| RWARE | robot giao hàng; hành động rời rạc; reward shared hoặc individual theo cấu hình | kho RWARE trong nguồn |
| Minigrid / MARLGrid | lưới kiểm soát tường, mục tiêu, tầm nhìn, reward riêng | nguồn tr. 24 |
| MAMuJoCo | khớp liên tục chia cho tác tử | Kuba et al. (2021) |
| SMAC | StarCraft II; quan sát cục bộ; hành động rời rạc; hơn 20 scenario | Samvelyan et al. (2019) |
| Unity / Google Football | đội, self-play, state hoặc image observation | Kurach et al. (2020) |
| MAgent | grid, nhiều tác tử; 22–1000 là cấu hình nguồn, không phải giới hạn platform | nguồn tr. 32 |
| Pogema | quan sát cục bộ, goal sparse, tránh va chạm; 1–512 là cấu hình nguồn | nguồn tr. 33 |

**Ứng dụng và giới hạn.** Đường cong thiếu giao thức không đủ để xếp hạng: cần seed, metric, cửa sổ tổng hợp và uncertainty; cùng số bước môi trường, compute và cách tune; phiên bản environment, map và reward mode; tách kết quả do paper báo cáo khỏi phép so sánh mới. Hai đường cong khác seed và ngân sách tương tác không đủ để xếp hạng. Không dựng lại đường cong thiếu dữ liệu gốc; không dùng bar chart thiếu protocol để suy rộng.

**Kiểm tra.** Trước khi dùng một benchmark, ghi đủ ba trục thông tin–quyết định–tín hiệu và giao thức đánh giá.

**Nguồn:** tr. 19–38.

**Nối ra:** tuyến cốt lõi đi thẳng từ benchmark sang giao tiếp ở topic 10; nhánh linh hoạt đi qua framework MARL ở topic 13 rồi quay lại giao tiếp.

<!-- note-topic-id: lec-12-topic-13 -->

## Bổ sung: framework MARL

| framework | vai trò trong nguồn | ví dụ |
|---|---|---|
| PyMARL | codebase cho SMAC | IQL, VDN, COMA, QMIX |
| EPyMARL | mở rộng thuật toán và môi trường | IPPO/MAPPO, MADDPG; MPE, LBF, RWARE |
| MARLlib | lớp MARL trên RLlib | actor–critic, phân rã giá trị |
| HARL | tác tử dị thể | HAPPO, MAPPO, HATD3; SMAC, MAMuJoCo, GRF |

Một framework có nhiều lớp: wrapper, batching, replay, masking, evaluation, logging. Đổi một lớp có thể làm thay đổi kết quả dù tên thuật toán giữ nguyên; hỗ trợ hiện tại phải kiểm tra theo phiên bản hoặc commit. Danh sách kiểm tái lập: cố định environment, map, wrapper, chế độ phần thưởng; ghi quan sát/trạng thái và hành động khả dụng; khóa seed, số bước, tài nguyên và lịch đánh giá; ghi batch/rollout/replay, bộ tối ưu, cách cập nhật mạng đích; báo trung bình, độ phân tán, số lần chạy và quy tắc chọn checkpoint. Hai kho cùng ghi "QMIX" nhưng khác wrapper và action mask: tên thuật toán không đủ để so kết quả.

**Nguồn:** tr. 39–46; Samvelyan et al. (2019); Papoudakis et al. (2020); Hu et al. (2023); Zhong et al. (2023).

**Nối ra:** quay lại mạch chính ở giao tiếp (topic 10); phục vụ mục tiêu 5 khi kiểm tra phiên bản framework.

<!-- note-topic-id: lec-12-topic-10 -->

## Giao tiếp trong MARL

**Vấn đề.** Benchmark khóa quan sát từ môi trường; khi thực thi, tác tử có thể cần kênh tác tử–tác tử. CTDE không mặc nhiên tạo message passing.

**Trực giác.** Ví dụ robot kho: robot A thấy lối đi bị chặn ngoài tầm nhìn của robot B và gửi "lối 3 bị chặn" trước khi B chọn hướng. Chỉ CTDE: actor B dùng $\tau_B$, thông tin chung chỉ vào critic khi học. Actor có giao tiếp: actor B dùng $(\tau_B,m_{A\to B})$; message phải có khi thực thi.

**Hình thức.** Năm trục đặc tả kênh giao tiếp:

| trục | câu hỏi |
|---|---|
| topology | cặp gửi–nhận nào được phép nối? |
| quyết định gửi | có gửi ở bước này không, theo lịch hay theo cổng? |
| nội dung | quan sát, biểu diễn ẩn hay ý định? |
| tích hợp | tổng, attention, RNN; vào actor, critic hay cả hai? |
| ràng buộc | băng thông, nhiễu, độ trễ, riêng tư và tấn công? |

Topology (kết nối đầy đủ, lân cận, qua tác tử đại diện) chỉ xác định các cạnh hợp lệ; policy giao tiếp quyết định có dùng cạnh đó ở thời điểm này hay không. Chu kỳ $T$ chỉ là ràng buộc tần suất, không phải định nghĩa full communication. Nội dung ở ba mức: kinh nghiệm cục bộ $(o_{t,i},a_{t,i},r_{t,i},o_{t+1,i})$; biểu diễn ẩn $h_{t,i}$; ý định tương lai. Nếu actor phụ thuộc thông điệp, giao thức gửi, nhận và kết hợp phải hoạt động khi thực thi; thông điệp chỉ vào critic là thông tin phụ trợ khi huấn luyện.

**Ứng dụng và giới hạn.** Bảo toàn riêng tư nghĩa là hạn chế điều tác tử khác có thể suy ra về dữ liệu, mục tiêu hoặc tham số nhạy cảm. Không tuyên bố một cơ chế an toàn nếu chưa nêu năng lực kẻ tấn công và cơ chế bảo vệ; attention là một phép kết hợp, không tự giải quyết băng thông hoặc độ bền trước nhiễu.

**Kiểm tra.** Topology xác định cạnh hợp lệ; policy quyết định có dùng cạnh đó ở bước hiện tại.

**Nguồn:** tr. 47–54; Zhu, Dastani & Wang (2022/2024); Singh, Jain & Sukhbaatar (2018); Agarwal, Kumar & Sycara (2019); Kim, Park & Sung (2020).

**Nối ra:** checklist sáu phép kiểm ở phần kết thu hồi cả mạch giao tiếp.

<!-- note-topic-id: lec-12-topic-14 -->

## Đọc thêm: AutoGen, Neural MMO, OpenAI Five

- **AutoGen** (tr. 34): framework ứng dụng agent LLM; không mặc nhiên là MARL vì không mặc nhiên huấn luyện policy bằng RL.
- **Neural MMO** (tr. 35): many-agent, chân trời dài, nhiều vai trò; mùa giải 2023 là sự kiện đã kết thúc, con số gắn với mùa giải và cấu hình được báo cáo, không phải giới hạn hệ thống.
- **OpenAI Five** (tr. 36–38): Dota 2, self-play, action phân rã thành nhiều thành phần rời rạc để tránh liệt kê một joint action khổng lồ; tại sự kiện Arena 18–21/4/2019, OpenAI Five thắng 7.215 trên tổng 7.257 trận, tương ứng tỷ lệ 99,421%. Con số này thuộc đúng sự kiện đã ghi, không suy rộng sang các trận đấu hay cấu hình khác.

Ba ca này là ghi chú lịch sử, không nằm trên mạch thuật toán chính.

**Nguồn:** tr. 34–38.

<!-- note-topic-id: lec-12-topic-15 -->

## Tài liệu tham khảo

- Foerster, J., et al. (2018). Counterfactual multi-agent policy gradients. AAAI; tr. 8, 12.
- Lowe, R., et al. (2017). Multi-agent actor-critic for mixed cooperative-competitive environments. NeurIPS; tr. 13, 20–21.
- Rashid, T., et al. (2020). Monotonic value function factorisation for deep multi-agent reinforcement learning. JMLR; tr. 14.
- Sunehag, P., et al. (2018). Value-Decomposition Networks; tr. 14.
- de Witt, C. S., et al. (2020). Deep multi-agent reinforcement learning for decentralized continuous cooperative control. arXiv:2003.06709; tr. 15–16.
- Yu, C., et al. (2022). The surprising effectiveness of PPO in cooperative multi-agent games. NeurIPS; tr. 15–16, 31.
- Kuba, J. G., et al. (2021). Trust region policy optimisation in multi-agent reinforcement learning. arXiv:2109.11251; tr. 17–18, 26.
- Littman, M. (1994). Markov games as a framework for multi-agent reinforcement learning; tr. 6–7.
- Buşoniu, L., Babuška, R., & De Schutter, B. (2010). Multi-agent reinforcement learning: An overview; tr. 10.
- Christianos, F., Schäfer, L., & Albrecht, S. (2020). Shared experience actor-critic. NeurIPS; tr. 22.
- Samvelyan, M., et al. (2019). The StarCraft multi-agent challenge. arXiv:1902.04043; tr. 27–28.
- Kurach, K., et al. (2020). Google Research Football: A Novel Reinforcement Learning Environment. AAAI; tr. 31.
- Papoudakis, G., et al. (2020). Benchmarking multi-agent deep RL algorithms; tr. 41.
- Hu, J., et al. (2023). MARLlib; tr. 43.
- Zhong, Y., et al. (2023). HARL; tr. 45.
- Zhu, Dastani & Wang (2022/2024). Survey on communication in MARL; tr. 49.
- Singh, Jain & Sukhbaatar (2018); Agarwal, Kumar & Sycara (2019); Kim, Park & Sung (2020); tr. 50–53.

## Bài tập

::: exercise X01: Hợp đồng MARL (8 phút)
1. Tính $|\mathcal A|$ cho $10$ tác tử, mỗi tác tử có $5$ hành động.
2. Viết điều kiện zero-sum cho ba tác tử.
3. Critic thấy $s,\mathbf a$ khi học; actor chỉ thấy $\tau_i$ khi chạy. Đây là hợp đồng nào?
4. Nêu đại lượng cảm sinh đổi khi $\pi_{-i}$ đổi.
5. Nếu $J_i(\pi_i^*,\pi_{-i}^*)=5$ nhưng một lệch đơn phương cho $5{,}4$, $\boldsymbol\pi^*$ có là Nash không?
:::

::: hint
Câu 1 dùng tích Descartes. Câu 4: phân biệt kernel nền với đại lượng cảm sinh. Câu 5: giữ $\pi_{-i}$ cố định và kiểm tra lệch đơn phương.
:::

::: solution
1. $5^{10}=9{.}765.625$.
2. $r_1(s,\mathbf a)+r_2(s,\mathbf a)+r_3(s,\mathbf a)=0$.
3. CTDE: thông tin tập trung chỉ ở pha huấn luyện, actor phân tán khi thực thi.
4. $P_i^{\pi_{-i}}$ và $r_i^{\pi_{-i}}$ đổi; $P$ và $r$ nền không bắt buộc đổi.
5. Không phải Nash: giữ $\pi_{-i}^*$ cố định, tác tử $i$ tăng return bằng lệch đơn phương.
:::

::: exercise X02: Cập nhật các thuật toán MARL (12 phút)
1. Tính baseline COMA với xác suất $(0{,}25,0{,}75)$, $Q=(2,6)$ và advantage của hành động "phải".
2. Trong QMIX double-Q, mạng nào chọn $\mathbf a_{t+1}^{*}$, mạng nào đánh giá và mask nằm ở đâu? Với $r=1{,}5$, $\gamma=0{,}9$, $m=1$, target $Q_{\mathrm{tot}}^{-}=4$ và online $Q_{\mathrm{tot}}=4{,}6$: tính $y$ và sai số bình phương; nếu terminal thật ($m=0$), $y$ bằng bao nhiêu?
3. HAPPO có $M_2=2{,}2$, $r_2(\theta)=1{,}3$, $\epsilon=0{,}2$. Tính hạng clipped; nếu $r_2^{\mathrm{new}}=0{,}9$, tính $M_3$.
4. Nêu input actor, critic và critic đích của MADDPG.
:::

::: hint
Câu 1: baseline là kỳ vọng có trọng số policy. Câu 2: phân biệt đường chọn và đường đánh giá. Câu 3: tính cả hai nhánh của min rồi lấy nhỏ hơn.
:::

::: solution
1. $b=0{,}25\times2+0{,}75\times6=5$; $A^{\mathrm{COMA}}=6-5=1$.
2. Utility online chọn $\mathbf a_{t+1}^{*}$; utility target và target mixer đánh giá; mask $\gamma m_t$ che bootstrap, $m_t=0$ chỉ ở terminal thật. Số: $y=1{,}5+0{,}9\times1\times4=5{,}1$; sai số bình phương $(5{,}1-4{,}6)^2=0{,}25$; terminal thật $m=0$ nên $y=r=1{,}5$.
3. Hạng clip $=\min(1{,}3\times2{,}2,\ 1{,}2\times2{,}2)=2{,}64$; $M_3=0{,}9\times2{,}2=1{,}98$.
4. Actor dùng $o_i$; critic dùng $x,\mathbf a$; critic đích dùng $x'$ và mọi target actor $\mu_{j,\bar\theta_j}(o_j')$.
:::

::: exercise X03: Benchmark, framework và giao tiếp (10 phút)
1. Chọn benchmark để kiểm hành động liên tục và quan sát cục bộ; nêu hai thuộc tính phải khóa.
2. Một actor dùng thông điệp từ lân cận. Thông điệp cần có ở pha nào?
3. Phân biệt kết nối đầy đủ với gửi mỗi $T$ bước.
4. Nêu ba trường bắt buộc để so hai đường cong MARL.
:::

::: hint
Câu 1: trả lời theo hợp đồng (hành động, quan sát, cấu hình), không theo tên môi trường. Câu 3: một trục xác định người nhận, một trục xác định tần suất.
:::

::: solution
1. Ví dụ MAMuJoCo; phải khóa cách chia khớp cho tác tử và cấu hình quan sát. Đáp án khác được chấp nhận nếu nêu đúng hành động, quan sát và cấu hình.
2. Khi thực thi: nếu actor phụ thuộc thông điệp, giao thức gửi, nhận và kết hợp phải hoạt động ở pha chạy.
3. Kết nối đầy đủ xác định các cặp gửi–nhận hợp lệ; gửi mỗi $T$ bước là ràng buộc tần suất trên policy quyết định gửi.
4. Cần seed, thước đo cùng độ phân tán, và ngân sách tương tác/giao thức đánh giá khớp.
:::

## Sáu phép kiểm khi đọc một phương pháp MARL

1. Viết state, observation/history, joint action và reward cho từng tác tử.
2. Tách kernel nền khỏi MDP cảm sinh đang đổi.
3. Ghi thông tin có ở huấn luyện và thực thi.
4. Viết target, baseline, ratio và đường gradient đúng chỉ số.
5. Nêu cấu trúc giúp thực thi phân tán và lớp hàm bị loại.
6. Giới hạn kết luận theo benchmark, protocol và phiên bản framework.
