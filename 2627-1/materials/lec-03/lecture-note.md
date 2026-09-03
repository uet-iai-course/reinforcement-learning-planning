# Bài 03 — Quá trình quyết định Markov

## Mục tiêu và kiến thức tiên quyết

Sau bài học, người học có thể:

- Kiểm tra tính Markov của một phát biểu và kiểm tra tính hợp lệ của ma trận chuyển.
- Tính phần thưởng kỳ vọng $r(s)$ và phần thưởng tích lũy $G_t$ cho một quỹ đạo cụ thể.
- Lập và giải hệ phương trình Bellman cho MRP, kể cả điều kiện $\gamma = 1$.
- Tạo MRP cảm sinh từ MDP dưới một chính sách Markov dừng.
- Liên hệ $v_\pi$ và $q_\pi$, viết hai phương trình Bellman kỳ vọng.

Kiến thức tiên quyết: xác suất có điều kiện, kỳ vọng, đại số ma trận, và mô hình tác tử – môi trường đã học ở Bài 02.

## Bản đồ chủ đề

### Cốt lõi

- `lec-03-topic-01` Chuỗi Markov — nguồn: slide 31–33 — vai trò: lớp mô hình đầu tiên, đóng gói đồ thị Student — vào: mô hình Bài 02 — ra: ma trận $P$ cho MRP.
- `lec-03-topic-02` MRP — nguồn: slide 34–35 — vai trò: thêm phần thưởng và chiết khấu — vào: $P$ hợp lệ — ra: nền cho $G_t$ và giá trị.
- `lec-03-topic-04` Giá trị trạng thái — nguồn: slide 39–43 — vai trò: định nghĩa đại lượng cần đánh giá — vào: $G_t$ — ra: $v(s)$ cho Bellman.
- `lec-03-topic-05` Bellman MRP — nguồn: slide 44–46 — vai trò: phân rã giá trị một bước — vào: định nghĩa $v(s)$ — ra: hệ Bellman, dạng ma trận.
- `lec-03-topic-07` MDP và hạt nhân — nguồn: slide 49–51 — vai trò: thêm hành động, định nghĩa $p(s', r \mid s, a)$ — vào: MRP — ra: MRP cảm sinh dưới chính sách.
- `lec-03-topic-08` Chính sách — nguồn: slide 52 — vai trò: quy tắc chọn hành động — vào: hạt nhân chung — ra: chính sách cố định cho MRP cảm sinh.
- `lec-03-topic-10` $v_\pi$ — nguồn: slide 53 — vai trò: giá trị trạng thái trong MDP — vào: MRP cảm sinh — ra: so với $q_\pi$, Bellman kỳ vọng.
- `lec-03-topic-11` $q_\pi$ — nguồn: slide 53–54; hw02 Bài 7 — vai trò: giá trị theo hành động đầu — vào: $v_\pi$, hạt nhân — ra: hai Bellman kỳ vọng.
- `lec-03-topic-12` Bellman kỳ vọng — nguồn: slide 56–57; hw02 Bài 8 — vai trò: hai phương trình một bước nhìn trước — vào: quan hệ $v_\pi$–$q_\pi$ — ra: nền cho Bài 04 và phi mô hình.

### Cầu nối

- `lec-03-topic-03` $G_t$ sang kỳ vọng — nguồn: slide 36–40 — vai trò: biến dãy thưởng thành đại lượng so sánh — vào: $r(s)$, $\gamma$ — ra: kỳ vọng của $G_t$ là giá trị trạng thái.
- `lec-03-topic-09` Chính sách cố định sang MRP cảm sinh — nguồn: slide 52–53; hw02 Bài 4 — vai trò: trung bình hạt nhân theo $\pi$ — vào: $\pi$, hạt nhân — ra: $P^\pi, r^\pi$ dùng lại máy móc Bellman MRP.

### Bổ sung

- `lec-03-topic-06` Dạng ma trận/giải hệ/điều kiện $\gamma = 1$ — nguồn: slide 47–48 — vai trò: giải trực tiếp và chỉ ra giới hạn tính toán — vào: Bellman từng trạng thái — ra: lý do sang quy hoạch động ở Bài 04.

### Đọc thêm

- `lec-03-topic-13` Tổng kết và đường sang Bài 04/các phương pháp phi mô hình — nguồn: slide 58; hw02 Bài 3, 4, 7, 8 — vai trò: khái quát ba lớp mô hình — vào: toàn bộ chuỗi Markov → MRP → MDP — ra: Bài 04 quy hoạch động, các phương pháp phi mô hình.

## Ký hiệu và quy ước

- Miền trạng thái $\mathcal S$ hữu hạn; miền hành động $\mathcal A$ hữu hạn; thời gian $t = 0, 1, 2, \dots$
- $S_t, A_t, R_{t+1}$ là trạng thái, hành động tại $t$ và phần thưởng nhận sau khi chuyển.
- $P_{ss'} = \Pr(S_{t+1} = s' \mid S_t = s)$ là ma trận chuyển trong chuỗi Markov và MRP.
- $r(s) = \mathbb E[R_{t+1} \mid S_t = s]$ là phần thưởng kỳ vọng của trạng thái; với Student MRP, quy ước $R_{t+1} = r(S_t)$.
- $G_t$ là phần thưởng tích lũy chiết khấu bắt đầu từ $R_{t+1}$.
- $p(s', r \mid s, a)$ là **hạt nhân chung** của MDP: xác suất đồng thời nhận trạng thái kế $s'$ và phần thưởng $r$ khi thực hiện hành động $a$ tại $s$. Các tổng trong bài dùng miền thưởng rời rạc; nếu thưởng liên tục thì thay tổng bằng tích phân. Ký hiệu suy ra từ hạt nhân: $P^a_{ss'} = \sum_r p(s', r \mid s, a)$ và $R^a_s = \sum_{s', r} r\, p(s', r \mid s, a)$.
- $\pi(a \mid s) = \Pr(A_t = a \mid S_t = s)$ là chính sách Markov dừng (không phụ thuộc thời gian và lịch sử).
- $v_\pi, q_\pi$ là giá trị trạng thái và giá trị hành động dưới $\pi$.
- Phân phối trạng thái viết dạng véc-tơ cột $\mu_t$; $\mu_{t+1} = P^{\mathsf T}\mu_t$.
- Động lực là quy luật sinh trạng thái kế và phần thưởng từ thông tin hiện tại: $P$ mô tả động lực của chuỗi Markov/MRP, còn $p(s', r \mid s, a)$ mô tả động lực của MDP.

<!-- note-topic-id: lec-03-topic-01 -->
## Chuỗi Markov

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: lớp mô hình đầu tiên trong ba lớp (động lực → động lực có thưởng → động lực có hành động); đóng gói đồ thị Student thành mô hình có định nghĩa.
- Kết nối vào: mô hình tác tử – môi trường của Bài 02 và đồ thị Student với các mũi tên xác suất.
- Kết nối ra: ma trận chuyển $P$ hợp lệ là đầu vào trực tiếp của MRP.
- Nguồn: slide 31–33.

Tính Markov: trạng thái $S_t$ là Markov khi và chỉ khi

$$\Pr(S_{t+1} \mid S_t) = \Pr(S_{t+1} \mid S_1, \dots, S_t),$$

tức trạng thái hiện tại nắm giữ toàn bộ thông tin liên quan từ lịch sử. **Chuỗi Markov** (Markov process) là cặp $\langle \mathcal S, P \rangle$ với $\mathcal S$ hữu hạn và ma trận chuyển $P_{ss'} = \Pr(S_{t+1} = s' \mid S_t = s)$.

::: example Ví dụ quỹ đạo Student
Đồ thị Student có bảy trạng thái theo thứ tự quy ước C1, C2, C3, Pass, Pub, Facebook, Sleep. Một quỹ đạo mẫu bắt đầu từ C1:

C1 → C2 → C3 → Pub → C2 → Sleep.

Một lần chạy chỉ cho một quỹ đạo; toàn bộ động lực (mọi xác suất chuyển) được đóng gói trong ma trận $P$. Với đồ thị nguồn, ma trận đầy đủ (hàng ứng với trạng thái đang đứng, cột ứng với trạng thái kế, cùng thứ tự bảy trạng thái trên):

$$P = \begin{pmatrix}
0 & 0.5 & 0 & 0 & 0 & 0.5 & 0 \\
0 & 0 & 0.8 & 0 & 0 & 0 & 0.2 \\
0 & 0 & 0 & 0.6 & 0.4 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0.2 & 0.4 & 0.4 & 0 & 0 & 0 & 0 \\
0.1 & 0 & 0 & 0 & 0 & 0.9 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1
\end{pmatrix}.$$

Mỗi hàng của $P$ là một phân phối xác suất (tổng bằng 1), và Sleep là trạng thái hấp thụ (chuyển vào chính nó với xác suất 1).
:::

::: exercise Câu hỏi kiểm tra
Cho hàng của $P$ ứng với C3 là $(0, 0, 0, 0.6, 0.4, 0, 0)$ theo thứ tự C1, C2, C3, Pass, Pub, Facebook, Sleep. Hàng này có hợp lệ không, và ý nghĩa của nó là gì?
:::

::: hint
Kiểm tra tổng các phần tử của hàng và đọc ý nghĩa từng hệ số theo định nghĩa $P_{ss'}$.
:::

::: solution
Tổng là $0.6 + 0.4 = 1$, nên hàng hợp lệ. Ý nghĩa: từ C3, xác suất 0.6 qua Pass, xác suất 0.4 sang Pub; không bao giờ chuyển thẳng sang C1, C2, Facebook hay Sleep ngay từ C3.
:::

<!-- note-topic-id: lec-03-topic-02 -->
## MRP: quá trình Markov có phần thưởng

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: bổ sung phần thưởng và chiết khấu vào chuỗi Markov; vẫn chưa có hành động.
- Kết nối vào: ma trận $P$ hợp lệ và véc-tơ thưởng của Student.
- Kết nối ra: định nghĩa MRP để tính $G_t$ và giá trị trạng thái.
- Nguồn: slide 34–35.

Trước khi đóng gói, xét ví dụ trực quan: với Student MRP, véc-tơ thưởng theo thứ tự C1, C2, C3, Pass, Pub, Facebook, Sleep là $r = (-2, -2, -2, +10, +1, -1, 0)$, với quy ước $R_{t+1} = r(S_t)$ (thưởng phát sinh khi ở trạng thái đó).

**Định nghĩa.** Quá trình thưởng Markov (MRP) là bộ $\langle \mathcal S, P, R, \gamma \rangle$:

- $\mathcal S$ hữu hạn; $P$ là ma trận chuyển;
- $R$ là hàm thưởng, $R(s) = \mathbb E[R_{t+1} \mid S_t = s]$, tức $r(s)$;
- $\gamma \in [0, 1]$ là hệ số chiết khấu.

MRP là chuỗi Markov có thêm giá trị thưởng; không có hành động, động lực là cố định.

::: exercise Câu hỏi kiểm tra
Sự khác biệt giữa chuỗi Markov và MRP nằm ở những cấu phần nào, và quy ước $R_{t+1} = r(S_t)$ nói lên điều gì?
:::

::: hint
So sánh bộ ký hiệu của hai mô hình; chú ý chỉ số thời gian của phần thưởng.
:::

::: solution
Chuỗi Markov chỉ có $\langle \mathcal S, P \rangle$; MRP thêm hàm thưởng $R$ và hệ số chiết khấu $\gamma$. Quy ước $R_{t+1} = r(S_t)$ nghĩa là phần thưởng nhận ngay sau thời điểm $t$ được xác định bởi trạng thái đang đứng tại $t$, nên thưởng cũng là động lực cố định của trạng thái, không phụ thuộc cách đi.
:::

<!-- note-topic-id: lec-03-topic-03 -->
## Phần thưởng tích lũy $G_t$ và cầu nối sang kỳ vọng

- Nhóm: `cầu nối`.
- Vai trò trong mạch: biến dãy thưởng thành một đại lượng so sánh được giữa các trạng thái; chuẩn bị định nghĩa giá trị.
- Kết nối vào: $r(s)$, $\gamma$ và quỹ đạo mẫu của Student.
- Kết nối ra: $G_t$ để lấy kỳ vọng có điều kiện, ra giá trị trạng thái.
- Nguồn: slide 36–40.

$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}.$$

$\gamma$ là giá trị hiện tại của phần thưởng tương lai: $\gamma$ gần 0 ưu tiên thưởng sớm, $\gamma$ gần 1 cho kế hoạch dài hạn. Lý do dùng chiết khấu: ta ưu tiên thưởng sớm hơn thưởng muộn, và khi $\gamma < 1$ với thưởng bị chặn thì tổng trên chắc chắn hội tụ. Khi $\gamma = 1$, cần điều kiện hữu hạn (có trạng thái kết thúc hoặc quỹ đạo hữu hạn) thì $G_t$ mới xác định được.

::: example Ví dụ hai quỹ đạo Student với $\gamma = \tfrac12$
Với $\gamma = \tfrac12$ và $r = (-2, -2, -2, +10, +1, -1, 0)$:

- Quỹ đạo C1 → C2 → C3 → Pass → Sleep: $G_0 = -2 + \tfrac12(-2) + \tfrac14(-2) + \tfrac18 \cdot 10 = -2 -1 -0.5 + 1.25 = -2.25$.
- Quỹ đạo C1 → Facebook → Facebook → C1 → C2 → Sleep (thưởng −2 ở C1, −1 ở Facebook lần đầu, −1 ở Facebook lần hai, −2 ở C1, −2 ở C2): $G_0 = -2 + \tfrac12(-1) + \tfrac14(-1) + \tfrac18(-2) + \tfrac1{16}(-2) = -2 -0.5 -0.25 -0.25 -0.125 = -3.125$.

Hai quỹ đạo cho hai phần thưởng tích lũy khác nhau; giá trị của trạng thái phải là trung bình trên các quỹ đạo, tức kỳ vọng của $G_t$.
:::

::: exercise Câu hỏi kiểm tra
Với cùng quỹ đạo C1 → C2 → C3 → Pass → Sleep, tính $G_0$ khi $\gamma = 0$ và khi $\gamma = 1$.
:::

::: hint
Với $\gamma = 0$ chỉ còn số hạng đầu; với $\gamma = 1$ cộng thẳng tất cả.
:::

::: solution
$\gamma = 0$: $G_0 = r(\text{C1}) = -2$. $\gamma = 1$: $G_0 = -2 - 2 - 2 + 10 + 0 = +4$. Điều kiện $\gamma = 1$ ở đây an toàn vì quỹ đạo kết thúc tại Sleep.
:::

<!-- note-topic-id: lec-03-topic-04 -->
## Giá trị trạng thái

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: định nghĩa đại lượng cần đánh giá trong MRP; trước khi nói cách tính.
- Kết nối vào: $G_t$ từ chủ đề trước.
- Kết nối ra: $v(s)$ để phân rã một bước thành phương trình Bellman.
- Nguồn: slide 39–43.

Hàm giá trị ước lượng giá trị dài hạn của trạng thái $s$:

$$v(s) = \mathbb E[G_t \mid S_t = s].$$

Lưu ý: $v(s)$ do ma trận chuyển $P$, hàm thưởng và $\gamma$ của MRP quyết định. Vì một trạng thái có nhiều quỹ đạo với nhiều $G_t$ khác nhau, giá trị là trung bình có trọng số của chúng.

::: exercise Câu hỏi kiểm tra
Vì sao một quỹ đạo duy nhất không đủ để xác định $v(s)$, và đại lượng nào trong định nghĩa MRP quyết định trung bình đó?
:::

::: hint
Quay lại kết quả của chủ đề $G_t$: hai quỹ đạo Student cho hai giá trị khác nhau.
:::

::: solution
Vì từ một trạng thái có nhiều quỹ đạo với xác suất khác nhau, mỗi quỹ đạo cho một $G_t$ riêng (ví dụ $-2.25$ và $-3.125$ ở trên), nên $v(s)$ là kỳ vọng chứ không phải một giá trị duy nhất. Trung bình được quyết định bởi ma trận chuyển $P$, tức động lực của MRP.
:::

<!-- note-topic-id: lec-03-topic-05 -->
## Phương trình Bellman cho MRP

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: phân rã giá trị thành thưởng ngay lập tức và giá trị kế tiếp, biến định nghĩa kỳ vọng thành phương trình.
- Kết nối vào: định nghĩa $v(s)$ và quy tắc tính một bước trên đồ thị Student.
- Kết nối ra: hệ Bellman và dạng ma trận.
- Nguồn: slide 44–46.

Trước công thức, hãy nhìn trước một bước. Với Student MRP, $\gamma = 0.9$ và $r = (-2, -2, -2, +10, +1, -1, 0)$, dùng các giá trị tạm thời (chỉ là giả định để minh họa cách tính, chưa phải nghiệm): nếu tạm lấy $\tilde v(\text{C3}) = 4$ và $\tilde v(\text{Sleep}) = 0$ thì phép nhìn trước một bước tại C2 là

$$-2 + 0.9\big(0.8 \cdot 4 + 0.2 \cdot 0\big) = -2 + 0.9 \cdot 3.2 = 0.88.$$

Trực giác: giá trị của trạng thái bằng phần thưởng nhận ngay cộng phần giá trị tương lai đã chiết khấu và trung bình theo xác suất chuyển. Công thức dưới đây chính là cách tính trên, viết cho mọi trạng thái.

Hàm giá trị phân rã thành hai phần: phần thưởng ngay $R_{t+1}$ và giá trị kế tiếp $\gamma v(S_{t+1})$:

$$G_t = R_{t+1} + \gamma G_{t+1},$$

lấy kỳ vọng có điều kiện $S_t = s$:

$$v(s) = \mathbb E[R_{t+1} \mid S_t = s] + \gamma \mathbb E[v(S_{t+1}) \mid S_t = s] = r(s) + \gamma \sum_{s'} P_{ss'} v(s').$$

Đây là phương trình Bellman của MRP; chủ đề sau viết đồng thời phương trình cho mọi trạng thái.

::: derivation Suy diễn chi tiết
Bước 1: tách số hạng đầu của $G_t$:

$$G_t = R_{t+1} + \gamma \sum_{k=0}^\infty \gamma^k R_{t+k+2} = R_{t+1} + \gamma G_{t+1}.$$

Bước 2: lấy kỳ vọng có điều kiện $S_t = s$ và dùng tuyến tính của kỳ vọng:

$$\mathbb E[G_t \mid S_t = s] = \mathbb E[R_{t+1} \mid S_t = s] + \gamma \mathbb E[G_{t+1} \mid S_t = s].$$

Bước 3: viết $\mathbb E[G_{t+1} \mid S_t = s] = \sum_{s'} P_{ss'} \mathbb E[G_{t+1} \mid S_{t+1} = s'] = \sum_{s'} P_{ss'} v(s')$ theo tính Markov và luật xác suất toàn phần. Điều kiện sử dụng: định nghĩa $v$ tồn tại (tổng $G_t$ xác định) và $P$ là ma trận chuyển của MRP.
:::

::: exercise Câu hỏi kiểm tra
Giải thích ý nghĩa từng thành phần của $v(s) = r(s) + \gamma \sum_{s'} P_{ss'} v(s')$.
:::

::: hint
Nhận diện phần thưởng tức thời, phần chiết khấu, và trung bình theo xác suất chuyển.
:::

::: solution
$r(s)$ là phần thưởng kỳ vọng nhận ngay khi ở $s$; $\gamma$ chiết khấu giá trị tương lai; $\sum_{s'} P_{ss'} v(s')$ là giá trị kế tiếp được trung bình hóa theo xác suất chuyển từ $s$. Cả hai ghép lại thành "thưởng ngay cộng giá trị tiếp tục chiết khấu".
:::

<!-- note-topic-id: lec-03-topic-06 -->
## Dạng ma trận và giải hệ Bellman

- Nhóm: `bổ sung`.
- Vai trò trong mạch: viết Bellman đồng thời cho mọi trạng thái rồi giải trực tiếp; chỉ ra giới hạn của cách giải này.
- Kết nối vào: phương trình Bellman theo từng trạng thái.
- Kết nối ra: giới hạn tính toán là lý do phải sang MDP với phương pháp khác (quy hoạch động ở Bài 04).
- Nguồn: slide 47–48.

Cho $v, r$ là các véc-tơ cột $n$ phần tử, Bellman viết thành

$$v = r + \gamma P v \quad\Longrightarrow\quad (I - \gamma P) v = r \quad\Longrightarrow\quad v = (I - \gamma P)^{-1} r.$$

Điều kiện giải: với $\gamma < 1$, $I - \gamma P$ khả nghịch vì bán kính phổ $\rho(\gamma P) \le \gamma < 1$. Khi $\gamma = 1$, cần điều kiện hữu hạn: gọi $Q$ là ma trận chuyển giới hạn trên các trạng thái chưa kết thúc; nếu $Q$ là transient ($\rho(Q) < 1$, tức từ mọi trạng thái chưa kết thúc đều kết thúc gần như chắc chắn) thì $I - Q$ khả nghịch và kỳ vọng thời gian đến khi kết thúc hữu hạn, nên kỳ vọng return hữu hạn. Diễn giải đơn giản: với $\gamma = 1$, hệ có nghiệm duy nhất khi quỹ đạo kết thúc gần như chắc chắn với kỳ vọng thời gian hữu hạn.

::: example Ví dụ nghiệm Student
Với Student MRP và $\gamma = 0.9$, giải hệ $v = r + \gamma P v$ bằng nghịch đảo cho nghiệm (theo thứ tự C1, C2, C3, Pass, Pub, Facebook, Sleep):

$$v \approx (-5.013,\ 0.943,\ 4.087,\ 10,\ 1.908,\ -7.638,\ 0).$$

Kiểm tra tại Sleep: $v(\text{Sleep}) = 0 + 0.9 \cdot v(\text{Sleep}) \Rightarrow v(\text{Sleep}) = 0$. ✓
:::

::: exercise Câu hỏi kiểm tra
Vì sao giải trực tiếp $v = (I - \gamma P)^{-1} r$ không mở rộng tốt, và cần kiểm tra điều kiện gì trước khi áp dụng?
:::

::: hint
Nhớ độ phức tạp của nghịch đảo ma trận và vai trò của $\gamma$ với tính khả nghịch.
:::

::: solution
Độ phức tạp $O(N^3)$ nên chỉ khả thi với số trạng thái nhỏ; với MRP lớn phải dùng phương pháp lặp. Trước khi giải cần kiểm tra điều kiện khả nghịch: $\gamma < 1$, hoặc nếu $\gamma = 1$ thì $Q$ phải là transient ($\rho(Q) < 1$), tức quỹ đạo kết thúc gần như chắc chắn với kỳ vọng thời gian đến khi kết thúc hữu hạn.
:::

<!-- note-topic-id: lec-03-topic-07 -->
## MDP và hạt nhân chung $p(s', r \mid s, a)$

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mở lớp mô hình thứ ba bằng cách thêm hành động; định nghĩa ký hiệu chính của bài.
- Kết nối vào: MRP đã đóng gói; trực giác về lựa chọn được xây ngay dưới đây qua Student MDP.
- Kết nối ra: hạt nhân chung để lập MRP cảm sinh dưới chính sách.
- Nguồn: slide 49–51.

Trực giác trước định nghĩa: Student MDP cho phép chọn. Ở C1, học sinh chọn Study (tiến tới C2) hoặc Facebook; ở C3, chọn Study tới Sleep với thưởng $+10$, hoặc chọn Pub nhận $+1$ rồi qua nút ngẫu nhiên về C1, C2 hoặc C3. Mỗi lựa chọn dẫn tới một kết quả chuyển có xác suất và phần thưởng riêng. Cần một ký hiệu đóng gói "chọn $a$ tại $s$ thì gặp kết quả $s', r$ với xác suất nào" — đó là hạt nhân chung.

MRP đánh giá được động lực cố định nhưng không biểu diễn lựa chọn hành động. **Quá trình quyết định Markov (MDP)** là MRP có quyết định: môi trường được mô tả đầy đủ bằng **hạt nhân chung**

$$p(s', r \mid s, a) = \Pr(S_{t+1} = s',\ R_{t+1} = r \mid S_t = s,\ A_t = a).$$

Các ký hiệu suy ra từ hạt nhân:

- $P^a_{ss'} = \sum_{r} p(s', r \mid s, a)$: xác suất chuyển khi chọn $a$;
- $R^a_s = \sum_{s', r} r\, p(s', r \mid s, a)$: phần thưởng kỳ vọng khi chọn $a$.

::: example Ví dụ Racing Car
Một xe robot muốn đi thật xa, thật nhanh. Ba trạng thái: Cool, Warm, Overheated; hai hành động: Slow, Fast. Sáu kết quả chuyển tiếp (khớp với hình minh họa):

- Cool với Slow: ở lại Cool với $p = 1$, thưởng $+1$;
- Cool với Fast: tới Cool hoặc Warm, mỗi kết quả $p = 0.5$, thưởng $+2$;
- Warm với Slow: tới Cool hoặc Warm, mỗi kết quả $p = 0.5$, thưởng $+1$;
- Warm với Fast: vào Overheated với $p = 1$, thưởng $-10$ (kết thúc).

Lưu ý: phần thưởng $-10$ của Warm–Fast **thay thế** cho $+2$ của Fast, không cộng dồn. Overheated là trạng thái kết thúc: khi vào Overheated thì episode kết thúc. Mỗi kết quả trên cho một giá trị $p(s', r \mid s, a)$. Đây chính là dữ kiện để lập hệ Bellman ở chủ đề 12, với ví dụ ứng dụng Racing Car.
:::

::: exercise Câu hỏi kiểm tra
Từ hạt nhân $p(s', r \mid s, a)$, hãy viết công thức suy ra $P^a_{ss'}$ và giải thích vì sao nó là "biên hóa" theo $r$.
:::

::: hint
Cộng dồn xác suất trên toàn bộ giá trị phần thưởng có thể.
:::

::: solution
$P^a_{ss'} = \sum_r p(s', r \mid s, a)$. Đây là biên hóa: hạt nhân cho xác suất đồng thời của $(s', r)$, còn $P^a_{ss'}$ chỉ quan tâm trạng thái kế nên cộng trên mọi phần thưởng $r$ có thể xảy ra cùng $s'$. Kiểm tra: với mỗi $(s, a)$, $\sum_{s'} P^a_{ss'} = 1$.
:::

<!-- note-topic-id: lec-03-topic-08 -->
## Chính sách Markov dừng

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: quy tắc chọn hành động biến MDP (có nhiều cách đi) thành một động lực xác định.
- Kết nối vào: hạt nhân chung $p(s', r \mid s, a)$.
- Kết nối ra: chính sách cố định để tạo MRP cảm sinh.
- Nguồn: slide 52.

Chính sách $\pi$ là một phân phối trên hành động theo trạng thái:

$$\pi(a \mid s) = \Pr(A_t = a \mid S_t = s).$$

- Chính sách xác định hoàn toàn hành vi của tác tử trong MDP.
- Chính sách Markov chỉ phụ thuộc trạng thái hiện tại, không phụ thuộc lịch sử.
- **Chính sách dừng** (stationary): $\pi$ không đổi theo thời gian, cùng một phân phối tại mọi $t$.

::: exercise Câu hỏi kiểm tra
Cho MDP với hai hành động tại mỗi trạng thái. Nêu một chính sách Markov dừng cụ thể và giải thích vì sao nó xác định hoàn toàn hành vi của tác tử.
:::

::: hint
Gán một phân phối trên $\mathcal A$ cho mỗi $s$, và kiểm tra tính không đổi theo thời gian.
:::

::: solution
Ví dụ với Racing Car: $\pi(\text{Slow} \mid s) = 0.5$, $\pi(\text{Fast} \mid s) = 0.5$ tại cả Cool và Warm (chính sách đều trên các hành động khả dụng). Vì tại mỗi thời điểm và mỗi trạng thái, xác suất chọn hành động được cho sẵn như nhau, chuỗi $(S_t, A_t)$ có động lực xác định đầy đủ: hành vi của tác tử được xác định hoàn toàn dù hành động cụ thể vẫn ngẫu nhiên.
:::

<!-- note-topic-id: lec-03-topic-09 -->
## Chính sách cố định tạo MRP cảm sinh

- Nhóm: `cầu nối`.
- Vai trò trong mạch: cầu nối trung tâm giữa MDP và MRP: cố định chính sách, MDP trở thành MRP.
- Kết nối vào: chính sách Markov dừng và hạt nhân chung.
- Kết nối ra: $P^\pi, r^\pi$ để dùng lại toàn bộ máy móc Bellman của MRP.
- Nguồn: slide 52–53; hw02 Bài 4.

Trực giác qua ví dụ Racing Car: nếu xe ở Cool và chọn đều hai hành động ($\pi(\text{Slow} \mid \text{Cool}) = \pi(\text{Fast} \mid \text{Cool}) = 0.5$), thì xác suất ở lại Cool là $0.5 \cdot 1 + 0.5 \cdot 0.5 = 0.75$ và tới Warm là $0.5 \cdot 0 + 0.5 \cdot 0.5 = 0.25$; phần thưởng kỳ vọng là $r^\pi(\text{Cool}) = 0.5 \cdot 1 + 0.5 \cdot 2 = 1.5$. Chính xác là phép lấy trung bình dưới đây.

Dưới chính sách cố định $\pi$, xác suất chọn hành động tại $s$ đã biết, nên lấy trung bình hạt nhân theo $\pi$:

$$P^\pi_{ss'} = \sum_{a} \pi(a \mid s)\, P^a_{ss'} = \sum_a \pi(a \mid s) \sum_r p(s', r \mid s, a),$$

$$r^\pi(s) = \sum_a \pi(a \mid s)\, R^a_s = \sum_a \pi(a \mid s) \sum_{s', r} r\, p(s', r \mid s, a).$$

Khi đó $\langle \mathcal S, P^\pi, r^\pi, \gamma \rangle$ là một MRP, gọi là **MRP cảm sinh** (induced MRP).

::: derivation Suy diễn chi tiết
Bước 1: xác suất chuyển tổng quát dưới $\pi$ được tính bằng luật toàn phần trên hành động:

$$\Pr(S_{t+1} = s' \mid S_t = s) = \sum_a \Pr(A_t = a \mid S_t = s)\, \Pr(S_{t+1} = s' \mid S_t = s, A_t = a) = \sum_a \pi(a \mid s) P^a_{ss'}.$$

Bước 2: thay $P^a_{ss'} = \sum_r p(s', r \mid s, a)$ từ hạt nhân chung. Tương tự cho thưởng kỳ vọng:

$$\mathbb E[R_{t+1} \mid S_t = s] = \sum_a \pi(a \mid s) \sum_{s', r} r\, p(s', r \mid s, a) = r^\pi(s).$$

Bước 3: vì $\pi$ dừng, các đại lượng này không phụ thuộc $t$, đúng cấu trúc MRP. Điều kiện sử dụng: $\pi$ là chính sách Markov dừng; hạt nhân cho phép điều kiện hóa theo $(s, a)$.
:::

::: exercise Câu hỏi kiểm tra
Với Racing Car ở Cool, hành động Slow giữ xe ở Cool với xác suất 1, hành động Fast đưa tới Cool hoặc Warm mỗi kết quả 0.5. Với $\pi$ đều 0.5/0.5, hãy tính $P^\pi_{\text{Cool},\text{Warm}}$, $P^\pi_{\text{Cool},\text{Cool}}$ và kiểm tra tổng hàng.
:::

::: hint
Nhân xác suất chính sách với xác suất chuyển rồi cộng theo hành động.
:::

::: solution
$P^\pi_{\text{Cool},\text{Warm}} = 0.5 \cdot P^{\text{Slow}}_{\text{Cool},\text{Warm}} + 0.5 \cdot P^{\text{Fast}}_{\text{Cool},\text{Warm}} = 0.5 \cdot 0 + 0.5 \cdot 0.5 = 0.25$. Với $s' = \text{Cool}$: $P^\pi_{\text{Cool},\text{Cool}} = 0.5 \cdot 1 + 0.5 \cdot 0.5 = 0.75$. Kiểm tra: $0.75 + 0.25 = 1$, tổng hàng bằng 1. ✓
:::

<!-- note-topic-id: lec-03-topic-10 -->
## Hàm giá trị trạng thái $v_\pi$

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: định nghĩa giá trị trong MDP có chính sách, nối trực tiếp về giá trị MRP.
- Kết nối vào: MRP cảm sinh $P^\pi, r^\pi$.
- Kết nối ra: $v_\pi$ để so với $q_\pi$ và viết Bellman kỳ vọng.
- Nguồn: slide 53.

Hàm giá trị trạng thái của MDP là kỳ vọng phần thưởng tích lũy khi xuất phát từ $s$ rồi đi theo $\pi$:

$$v_\pi(s) = \mathbb E_\pi[G_t \mid S_t = s].$$

Vì chính sách cố định sinh ra MRP cảm sinh, $v_\pi$ chính là hàm giá trị của MRP đó, nên thỏa Bellman MRP:

$$v_\pi = r^\pi + \gamma P^\pi v_\pi.$$

::: exercise Câu hỏi kiểm tra
Vì sao $v_\pi$ thỏa $v_\pi = r^\pi + \gamma P^\pi v_\pi$, và khác gì so với $v(s)$ của MRP thuần?
:::

::: hint
Dùng kết luận của chủ đề MRP cảm sinh, rồi đối chiếu cấu trúc hai phương trình.
:::

::: solution
Vì dưới $\pi$, chuỗi trạng thái là một MRP với động lực $P^\pi$ và thưởng $r^\pi$, nên định nghĩa $v_\pi(s) = \mathbb E_\pi[G_t \mid S_t = s]$ trùng với định nghĩa giá trị của MRP, do đó thỏa đúng Bellman MRP $v_\pi = r^\pi + \gamma P^\pi v_\pi$. Khác biệt duy nhất là $P^\pi, r^\pi$ được trung bình hóa theo chính sách, còn MRP thuần cho sẵn từ đầu.
:::

<!-- note-topic-id: lec-03-topic-11 -->
## Hàm giá trị hành động $q_\pi$ và quan hệ với $v_\pi$

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: điều kiện hóa giá trị theo hành động đầu, hai cách nhìn giá trị trong MDP.
- Kết nối vào: $v_\pi$ và hạt nhân chung.
- Kết nối ra: hai dạng Bellman kỳ vọng (trạng thái và hành động).
- Nguồn: slide 53–54; hw02 Bài 7.

Hàm giá trị hành động là kỳ vọng phần thưởng tích lũy khi xuất phát từ $s$, chọn $a$, rồi đi theo $\pi$:

$$q_\pi(s, a) = \mathbb E_\pi[G_t \mid S_t = s, A_t = a].$$

Hai đại lượng liên hệ bằng cách lấy trung bình hoặc điều kiện hóa theo hành động:

$$v_\pi(s) = \sum_a \pi(a \mid s)\, q_\pi(s, a).$$

::: derivation Suy diễn chi tiết ($v_\pi$ theo $q_\pi$, hw02 Bài 7)
Bước 1: điều kiện hóa kỳ vọng theo giá trị của biến ngẫu nhiên $A_t$ tại $S_t = s$:

$$\mathbb E_\pi[G_t \mid S_t = s] = \sum_a \Pr(A_t = a \mid S_t = s)\, \mathbb E_\pi[G_t \mid S_t = s, A_t = a].$$

Bước 2: thay $\Pr(A_t = a \mid S_t = s) = \pi(a \mid s)$ và định nghĩa $q_\pi$:

$$v_\pi(s) = \sum_a \pi(a \mid s)\, q_\pi(s, a).$$

Điều kiện sử dụng: $\pi$ là phân phối trên $\mathcal A$ tại $s$ (các trọng số không âm, tổng bằng 1), nên đẳng thức là trung bình trọng số của $q_\pi$ theo chính sách.
:::

::: example Ví dụ kiểm quan hệ bằng số với Student
Với Student MDP và chính sách đều trên các hành động khả dụng tại mỗi trạng thái, $\gamma = 1$ (dữ kiện nguồn trang 54): tại C1 có hai hành động study và facebook với $q_\pi(\text{C1}, \text{facebook}) = -\tfrac{43}{13}$ và $q_\pi(\text{C1}, \text{study}) = \tfrac{9}{13}$, nên

$$v_\pi(\text{C1}) = 0.5 \cdot \tfrac{9}{13} + 0.5 \cdot \Big(-\tfrac{43}{13}\Big) = -\tfrac{17}{13}.$$

Cùng bộ dữ kiện, ta có: $v_\pi(\text{Facebook}) = -\tfrac{30}{13}$ và $v_\pi(\text{C2}) = \tfrac{35}{13}$. Giá trị $v_\pi(\text{C1}) = -\tfrac{17}{13}$ được kiểm lại bằng phương trình Bellman tại C1 (xem chủ đề 12). ✓
:::

::: exercise Câu hỏi kiểm tra
Nếu $\pi$ tập trung hoàn toàn vào một hành động $a^\ast$ tại $s$ (tức $\pi(a^\ast \mid s) = 1$), thì $v_\pi(s)$ bằng gì?
:::

::: hint
Tính trung bình trọng số khi chỉ có một trọng số khác 0.
:::

::: solution
$v_\pi(s) = 1 \cdot q_\pi(s, a^\ast) = q_\pi(s, a^\ast)$: khi chính sách tại $s$ là tất định, giá trị trạng thái trùng với giá trị của hành động duy nhất được chọn.
:::

<!-- note-topic-id: lec-03-topic-12 -->
## Phương trình Bellman kỳ vọng cho $v_\pi$ và $q_\pi$

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: tổng hợp máy móc điều kiện hóa thành hai phương trình một bước nhìn trước, có kiểm bằng số.
- Kết nối vào: quan hệ $v_\pi$–$q_\pi$ và dữ kiện Student MDP.
- Kết nối ra: nền cho quy hoạch động ở Bài 04 và các phương pháp phi mô hình sau.
- Nguồn: slide 56–57; hw02 Bài 8.

**Bellman kỳ vọng cho $v_\pi$** — điều kiện hóa trước theo chính sách, rồi theo môi trường:

$$v_\pi(s) = \sum_a \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a)\big(r + \gamma v_\pi(s')\big).$$

**Bellman kỳ vọng cho $q_\pi$** — giữ cố định cặp $(s, a)$ ở vế trái:

$$q_\pi(s, a) = \sum_{s', r} p(s', r \mid s, a)\big(r + \gamma v_\pi(s')\big) = \sum_{s', r} p(s', r \mid s, a)\Big(r + \gamma \sum_{a'} \pi(a' \mid s')\, q_\pi(s', a')\Big).$$

Đây là các phương trình **kỳ vọng** (trung bình theo $\pi$, không có phép lấy cực đại). Từng thành phần: $\pi(a \mid s)$ là trung bình hành động theo chính sách; $p(s', r \mid s, a)$ là trung bình kết quả theo môi trường; $r$ là thưởng ngay; $\gamma v_\pi(s')$ là giá trị kế tiếp chiết khấu.

::: example Ví dụ kiểm bằng số tại C1
Với Student MDP, chính sách đều, $\gamma = 1$, kiểm Bellman kỳ vọng của $v_\pi$ tại C1 bằng $q_\pi$:

$$v_\pi(\text{C1}) = \tfrac12 q_\pi(\text{C1}, \text{study}) + \tfrac12 q_\pi(\text{C1}, \text{facebook}) = \tfrac12 \cdot \tfrac{9}{13} + \tfrac12 \cdot \Big(-\tfrac{43}{13}\Big) = -\tfrac{17}{13},$$

trùng với giá trị khôi phục ở chủ đề 11. Phương trình $q_\pi$ giữ cố định $(s, a)$: ví dụ $q_\pi(\text{C1}, \text{facebook})$ không trung bình theo chính sách tại C1 vì hành động đầu đã cố định là facebook.
:::

::: exercise Câu hỏi kiểm tra
Viết phương trình Bellman kỳ vọng cho $v_\pi(s)$ và giải thích ý nghĩa của từng thành phần (hw02 Bài 8).
:::

::: hint
Đi từ $q_\pi$: trung bình theo chính sách rồi trung bình theo hạt nhân môi trường.
:::

::: solution
$v_\pi(s) = \sum_a \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a)\big(r + \gamma v_\pi(s')\big)$. Ý nghĩa: tổng ngoài lấy trung bình hành động theo xác suất chính sách $\pi(a \mid s)$; tổng trong lấy trung bình kết quả $(s', r)$ theo quy luật môi trường $p(s', r \mid s, a)$; $r$ là phần thưởng nhận ngay sau chuyển; $\gamma v_\pi(s')$ là giá trị chiết khấu của trạng thái kế. Đây là phương trình kỳ vọng nên không có phép lấy cực đại.
:::

<!-- note-topic-id: lec-03-topic-13 -->
## Tổng kết và cầu nối bài sau

- Nhóm: `đọc thêm`.
- Vai trò trong mạch: khái quát ba lớp mô hình và nối sang hai hướng phương pháp.
- Kết nối vào: toàn bộ chuỗi Markov → MRP → MDP và các quan hệ $v_\pi, q_\pi$.
- Kết nối ra: Bài 04 quy hoạch động; các bài sau phương pháp phi mô hình.
- Nguồn: slide 58; hw02 Bài 3, 4, 7, 8.

Ba lớp mô hình trả lời ba câu hỏi khác nhau: **chuỗi Markov** mô tả động lực; **MRP** thêm câu "trạng thái đáng giá bao nhiêu"; **MDP** thêm câu "nên chọn hành động nào". Các cầu nối quan trọng cần tự kiểm:

- Kiểm ma trận chuyển: mỗi hàng là một phân phối; xác định trạng thái hấp thụ (hw02 Bài 3).
- MRP cảm sinh: chính sách cố định $\pi$ biến MDP thành MRP với $P^\pi, r^\pi$ (hw02 Bài 4).
- Quan hệ giá trị: $v_\pi(s) = \sum_a \pi(a \mid s) q_\pi(s, a)$ (hw02 Bài 7, tự luyện).
- Bellman kỳ vọng cho $v_\pi$ và ý nghĩa từng thành phần (hw02 Bài 8).

::: exercise Câu hỏi kiểm tra
Xếp các khái niệm sau theo đúng thứ tự phụ thuộc: $q_\pi$, $P^\pi$, $v_\pi$, $p(s', r \mid s, a)$, $\pi(a \mid s)$, $G_t$.
:::

::: hint
Hỏi khái niệm nào được định nghĩa chỉ từ hạt nhân, khái niệm nào cần cả chính sách.
:::

::: solution
Thứ tự phụ thuộc: (1) $G_t$ — phần thưởng tích lũy chiết khấu, đã được định nghĩa ở MRP trước khi thêm hành động; (2) $p(s', r \mid s, a)$ — hạt nhân chung, định nghĩa MDP từ môi trường; (3) $\pi(a \mid s)$ — quy tắc chọn hành động; (4) $P^\pi$ (cùng $r^\pi$) — trung bình hạt nhân theo $\pi$, tạo MRP cảm sinh; (5) $v_\pi$ — kỳ vọng $G_t$ từ trạng thái; (6) $q_\pi$ — kỳ vọng $G_t$ từ cặp (trạng thái, hành động), liên hệ ngược về $v_\pi$ qua trung bình chính sách. Kiểm tra: mỗi khái niệm chỉ dùng các khái niệm đứng trước.
:::

## Tài liệu tham khảo

- Tạ Việt Cường, 2026, "Bài tập tuần 2 — MDP", Bài 3, 4, 7, 8.
- Slide bài giảng "Markov Decision Processes", trang 28–58 (Student MRP/MDP, Racing Car, Bellman, chính sách).
- Sutton & Barto, *Reinforcement Learning: An Introduction*, Chương 3.
