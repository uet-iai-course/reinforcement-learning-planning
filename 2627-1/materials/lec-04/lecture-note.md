# Bài 04 — Giải MDP bằng quy hoạch động

## Mục tiêu và kiến thức tiên quyết

- Phát biểu bài toán tối ưu trên MDP hữu hạn và phương trình Bellman tối ưu cho $v_*, q_*$.
- Trình bày hai thuật toán quy hoạch động: lặp chính sách và lặp giá trị, kèm giả mã và điều kiện dừng.
- Chứng minh hai bảo đảm chính: tồn tại chính sách tối ưu dừng, xác định; hội tụ của lặp giá trị và dừng hữu hạn của lặp chính sách.
- Tự tính lại các ví dụ MDP hai trạng thái, Gridworld năm ô và Bài 9 phần 1 của hw3.
- Kiến thức tiên quyết: nội dung Bài 03 về MDP, phần thưởng tích lũy, $v^\pi, q^\pi$ và Bellman kỳ vọng.
- Giả thiết xuyên suốt: MDP hữu hạn; mỗi trạng thái có ít nhất một hành động; biết hạt nhân $p(s',r\mid s,a)$; phần thưởng bị chặn; $0\le\gamma<1$.

## Ký hiệu và quy ước

- $\mathcal S$ tập trạng thái hữu hạn, $\mathcal A$ tập hành động hữu hạn, $\gamma\in[0,1)$.
- Hạt nhân chuyển: $p(s',r\mid s,a)$; ở đây $r$ là giá trị của biến phần thưởng ngẫu nhiên, phân biệt với hàm phần thưởng kỳ vọng $r(s,a)=\sum_{s',r}p(s',r\mid s,a)\,r$.
- Phần thưởng tích lũy: $G_t=\sum_{k=0}^{\infty}\gamma^k R_{t+1+k}$; $v^\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$; $q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$.
- Chính sách $\pi(a\mid s)$; chính sách xác định viết $\pi(s)\in\mathcal A$.
- Chuẩn vô cùng trên không gian hàm giá trị: $\|v\|_\infty=\max_{s\in\mathcal S}|v(s)|$.
- Toán tử Bellman: $T^\pi$ theo chính sách, $T_*$ tối ưu; định nghĩa ở topic 04.

## Bản đồ chủ đề

### Cốt lõi

- `lec-04-topic-01` — Bài toán, giả thiết, ôn Bellman kỳ vọng.
- `lec-04-topic-03` — $v_*, q_*$, Bellman tối ưu, chính sách tham lam.
- `lec-04-topic-05` — Lặp chính sách trên MDP hai trạng thái.
- `lec-04-topic-07` — Thuật toán lặp chính sách và định lý cải thiện.
- `lec-04-topic-08` — Gridworld và các lượt lặp giá trị.
- `lec-04-topic-09` — Giả mã lặp giá trị và trích chính sách.
- `lec-04-topic-11` — Bất đẳng thức cực đại, $T_*$ co, hội tụ hình học.
- `lec-04-topic-12` — Điểm bất động chặn mọi chính sách, tồn tại tối ưu, dừng hữu hạn.

### Cầu nối

- `lec-04-topic-02` — Từ đánh giá chính sách sang tối ưu; micro-example nối $q_*$ với $v_*$.
- `lec-04-topic-04` — Không gian $\mathcal V$, chuẩn vô cùng, toán tử và điểm bất động.
- `lec-04-topic-06` — Đánh giá chính sách lặp, đồng bộ và điều kiện công bằng.
- `lec-04-topic-13` — Phần dư $\rho(v)$, chặn sai số và mất mát.

### Bổ sung

- `lec-04-topic-10` — Đồng bộ/bất đồng bộ, chi phí một lượt, so sánh PI–VI.
- `lec-04-topic-14` — CartPole rời rạc, giới hạn của DP dạng bảng.

### Đọc thêm

- `lec-04-topic-15` — Hướng đọc chứng minh chi tiết và giới hạn không gian liên tục.

### Danh sách 15 topic

1. `lec-04-topic-01` — cốt lõi — Bài toán, giả thiết, ôn Bellman kỳ vọng.
2. `lec-04-topic-02` — cầu nối — Từ đánh giá đến tối ưu; micro-example tất định.
3. `lec-04-topic-03` — cốt lõi — $v_*, q_*$, Bellman tối ưu, tham lam.
4. `lec-04-topic-04` — cầu nối — Không gian $\mathcal V$, chuẩn vô cùng, $T^\pi, T_*$.
5. `lec-04-topic-05` — cốt lõi — PI trên MDP hai trạng thái.
6. `lec-04-topic-06` — cầu nối — Đánh giá chính sách lặp, đồng bộ/bất đồng bộ.
7. `lec-04-topic-07` — cốt lõi — Thuật toán PI, cải thiện, dừng hữu hạn.
8. `lec-04-topic-08` — cốt lõi — Gridworld và các lượt VI.
9. `lec-04-topic-09` — cốt lõi — Giả mã VI, đầu vào/đầu ra/dừng, trích chính sách.
10. `lec-04-topic-10` — bổ sung — Đồng bộ/bất đồng bộ, chi phí, so sánh PI–VI.
11. `lec-04-topic-11` — cốt lõi — Bất đẳng thức cực đại, $T_*$ co, Banach, hội tụ hình học.
12. `lec-04-topic-12` — cốt lõi — Điểm bất động chặn mọi chính sách, tồn tại tối ưu.
13. `lec-04-topic-13` — cầu nối — Phần dư $\rho(v)$, chặn sai số và mất mát.
14. `lec-04-topic-14` — bổ sung — CartPole rời rạc và giới hạn DP dạng bảng.
15. `lec-04-topic-15` — đọc thêm — Hướng đọc chứng minh và giới hạn liên tục.

<!-- note-topic-id: lec-04-topic-01 -->
## Bài toán MDP và ôn Bellman kỳ vọng

- Nhóm: cốt lõi.
- Vai trò trong mạch: đặt bài toán tối ưu trên MDP và khôi phục nền tảng Bellman kỳ vọng từ Bài 03.
- Kết nối vào: định nghĩa MDP, phần thưởng tích lũy, $v^\pi, q^\pi$ ở Bài 03.
- Kết nối ra: nhu cầu tìm chính sách tối ưu dẫn sang topic 02 và 03.
- Nguồn: PDF nguồn trang 1–6.

### Vấn đề

Cho MDP hữu hạn $\mathcal M=(\mathcal S,\mathcal A,p,r,\gamma)$ với hạt nhân $p(s',r\mid s,a)$ biết trước, phần thưởng bị chặn và $0\le\gamma<1$. Phần thưởng bị chặn cùng với $\gamma<1$ làm chuỗi chiết khấu hội tụ, nên giá trị $v^\pi(s)$ luôn hữu hạn. Cần tìm chính sách $\pi$ làm cực đại tổng phần thưởng chiết khấu kỳ vọng từ mọi trạng thái. Đây là bài toán lập kế hoạch khi mô hình đã biết.

### Trực giác

Giá trị của một trạng thái bằng phần thưởng tức thời cộng với giá trị tương lai đã chiết khấu. Bellman kỳ vọng mô tả đẳng thức tự nhất quán này khi chính sách cố định. Nếu biết chính xác giá trị của mọi trạng thái, việc chọn hành động tốt trở nên khả thi; vấn đề là giá trị phụ thuộc vào chính sách đang dùng.

### Ví dụ tính được

::: example Ví dụ tính được
MDP một trạng thái $s$, một hành động $a$, chuyển về $s$ với phần thưởng xác định bằng $1$, $\gamma=0.9$. Với chính sách luôn chọn $a$: $v^\pi(s)=1+0.9\,v^\pi(s)$, suy ra $v^\pi(s)=10$. Kiểm tra: $1+0.9\cdot 10=10$.
:::

### Hình thức

Bellman kỳ vọng cho chính sách $\pi$:

$$v^\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v^\pi(s')\bigr],$$

$$q^\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)\Bigl[r+\gamma\sum_{a'}\pi(a'\mid s')\,q^\pi(s',a')\Bigr].$$

Liên hệ: $v^\pi(s)=\sum_a\pi(a\mid s)\,q^\pi(s,a)$. Dạng ma trận: $v^\pi=r^\pi+\gamma P^\pi v^\pi$. Lưu ý $r$ trong $p(s',r\mid s,a)$ là giá trị của biến phần thưởng ngẫu nhiên; hàm thưởng kỳ vọng là $r(s,a)$.

### Ứng dụng và giới hạn

Bellman kỳ vọng giải bài toán đánh giá chính sách với chính sách đã cho. Nó chưa trả lời chính sách nào tốt nhất; hệ phương trình tuyến tính theo $\pi$ không cho biết cách cải thiện $\pi$.

::: exercise Câu hỏi kiểm tra
Với MDP một trạng thái ở ví dụ trên, nếu phần thưởng là $2$ và $\gamma=0.5$, tính $v^\pi(s)$.
:::

::: hint
Giải $v=2+0.5v$.
:::

::: solution
$v^\pi(s)=2/(1-0.5)=4$. Kiểm tra: $2+0.5\cdot 4=4$.
:::

<!-- note-topic-id: lec-04-topic-02 -->
## Từ đánh giá chính sách sang tối ưu

- Nhóm: cầu nối.
- Vai trò trong mạch: chuyển từ hệ Bellman tuyến tính theo $\pi$ sang hệ bất đẳng thức cực đại; dùng micro-example tất định để nối $q_*$ với $v_*$.
- Kết nối vào: Bellman kỳ vọng ở topic 01.
- Kết nối ra: định nghĩa $v_*, q_*$ và Bellman tối ưu ở topic 03.
- Nguồn: PDF nguồn trang 7–8. Micro-example là ví dụ xây dựng từ công thức nguồn, trình bày trong deck phụ.

### Vấn đề

Đánh giá chính sách cho biết một chính sách tốt đến đâu. Cần một cách nói về chính sách tốt nhất và một phương trình mà nghiệm của nó chính là giá trị tối ưu.

### Trực giác

Nếu tại mỗi bước được chọn hành động tốt nhất, phép lấy trung bình theo $\pi$ trong Bellman kỳ vọng được thay bằng phép cực đại theo $a$. Micro-example tất định dưới đây cho thấy $q_*$ và $v_*$ khớp nhau thế nào khi chỉ có một hành động tối ưu.

### Ví dụ tính được

::: example Micro-example tất định (xây dựng từ công thức nguồn)
Hai trạng thái $s_0,s_1$, một hành động $a$ duy nhất, tất định: $s_0\xrightarrow{a}(r=1,s_0)$, $s_1\xrightarrow{a}(r=2,s_0)$, $\gamma=0.9$. Vì chỉ có một hành động, $\max_a q_*(s,a)=q_*(s,a)$ và $v_*(s)=q_*(s,a)$. Giải: $v_*(s_0)=1+0.9v_*(s_0)=10$; $v_*(s_1)=2+0.9\cdot 10=11$. Khi thêm hành động $b$ từ $s_0$ cho $(r=0,s_1)$, ta có $q_*(s_0,b)=0+0.9\cdot 11=9.9<10$, nên $v_*(s_0)=\max\{10,9.9\}=10$ vẫn giữ nguyên và chính sách tham lam chọn $a$. Ví dụ cho thấy trực tiếp các phép tính xác định $v_*(s)=\max_a q_*(s,a)$ và hành động đạt cực đại.
:::

### Hình thức

Định nghĩa giá trị tối ưu:

$$v_*(s)=\max_\pi v^\pi(s),\qquad q_*(s,a)=\max_\pi q^\pi(s,a).$$

Khi biết $q_*$, chính sách tối ưu lấy bằng tham lam: $\pi_*(s)\in\arg\max_a q_*(s,a)$.

### Ứng dụng và giới hạn

Định nghĩa này hợp lệ nhưng chưa tự chứng minh $v_*$ đạt được bởi một chính sách cụ thể. Việc chứng minh tồn tại nằm ở topic 12; trước đó không tuyên bố tính tối ưu của chính sách tham lam.

::: exercise Câu hỏi kiểm tra
Trong micro-example, nếu hành động $b$ từ $s_0$ cho $(r=2,s_1)$ thay vì $(r=0,s_1)$, hành động nào là tối ưu tại $s_0$?
:::

::: hint
So sánh $q_*(s_0,a)$ với $2+0.9\,v_*(s_1)$.
:::

::: solution
Đặt $v_0=v_*(s_0)$ và $v_1=v_*(s_1)$. Khi đó

$$v_0=\max\{1+0.9v_0,\;2+0.9v_1\},\qquad v_1=2+0.9v_0.$$

Nếu chọn nhánh $b$ thì $v_0=2+0.9v_1=2+0.9(2+0.9v_0)=3.8+0.81v_0$. Suy ra $v_0=20$ và $v_1=2+0.9\cdot20=20$. Kiểm tra nhánh $a$: $1+0.9\cdot20=19<20$. Vậy $b$ tối ưu tại $s_0$.
:::

<!-- note-topic-id: lec-04-topic-03 -->
## Giá trị tối ưu và Bellman tối ưu

- Nhóm: cốt lõi.
- Vai trò trong mạch: phát biểu hệ phương trình mà nghiệm của nó là $v_*, q_*$; đây là hạt nhân của toàn bài.
- Kết nối vào: định nghĩa $v_*, q_*$ ở topic 02.
- Kết nối ra: toán tử $T_*$ ở topic 04 và thuật toán lặp giá trị ở topic 08–09.
- Nguồn: PDF nguồn trang 7–9.

### Vấn đề

Cần một hệ phương trình đặc trưng cho $v_*$ mà không cần liệt kê mọi chính sách, vì số chính sách có thể rất lớn.

### Trực giác

Nếu mọi trạng thái sau đều đã tối ưu, thì ở trạng thái hiện tại chỉ cần chọn hành động cho tổng $r+\gamma v_*(s')$ lớn nhất. Nói cách khác, nếu đã biết $v_*(s')$ cho mọi $s'$, thì hành động đầu tiên phải cực đại hóa kỳ vọng $r+\gamma v_*(s')$. Đây là nguyên lý tối ưu của quy hoạch động.

### Hình thức

Bellman tối ưu:

$$v_*(s)=\max_a\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_*(s')\bigr],$$

$$q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)\Bigl[r+\gamma\max_{a'}q_*(s',a')\Bigr].$$

Khác Bellman kỳ vọng: phép trung bình theo $\pi$ được thay bằng phép cực đại theo hành động. Chính sách tham lam: $\pi_*(s)\in\arg\max_a q_*(s,a)$.

### Ứng dụng và giới hạn

Hệ này là nền của lặp giá trị. Vì chứa phép cực đại, hệ không tuyến tính; không thể giải bằng nghịch đảo ma trận như đánh giá chính sách. Tính tối ưu của nghiệm được bảo đảm sau khi chứng minh tồn tại và hội tụ (topic 11–12).

::: exercise Câu hỏi kiểm tra
Viết Bellman tối ưu cho micro-example hai trạng thái ở topic 02: tại $s_0$, hành động $a$ tất định cho $(1,s_0)$, hành động $b$ tất định cho $(2,s_1)$; tại $s_1$, hành động $a$ tất định cho $(2,s_0)$; $\gamma=0.9$.
:::

::: hint
Áp dụng $\max$ lên hai biểu thức $r+\gamma v_*(s')$ tương ứng.
:::

::: solution
$v_*(s_0)=\max\{1+0.9v_*(s_0),\;2+0.9v_*(s_1)\}$; $v_*(s_1)=2+0.9v_*(s_0)$. Nghiệm: $v_*(s_1)=2+0.9v_*(s_0)$, thay vào: $v_*(s_0)=\max\{1+0.9v_*(s_0),\;3.8+0.81v_*(s_0)\}$. Nhánh thứ hai cho $v_*(s_0)=20$ và $v_*(s_1)=20$; kiểm tra nhánh thứ nhất: $1+18=19<20$. Vậy $v_*(s_0)=v_*(s_1)=20$.
:::

<!-- note-topic-id: lec-04-topic-04 -->
## Không gian giá trị, chuẩn vô cùng và toán tử Bellman

- Nhóm: cầu nối.
- Vai trò trong mạch: dựng khung hàm học để chứng minh hội tụ; định nghĩa $T^\pi, T_*$ và điểm bất động.
- Kết nối vào: Bellman kỳ vọng và Bellman tối ưu ở topic 01, 03.
- Kết nối ra: tính co và hội tụ ở topic 11; đánh giá lặp ở topic 06.
- Nguồn: PDF nguồn trang 10, 30–32; hw3.pdf Bài 7.

### Vấn đề

Các phương trình Bellman là đẳng thức giữa hàm trên $\mathcal S$. Để nói về hội tụ cần một không gian mét và các toán tử tác động trên đó.

### Trực giác

Xem một bảng giá trị như một điểm trong không gian vector $\mathbb R^{|\mathcal S|}$. Mỗi lần cập nhật Bellman là một ánh xạ biến bảng này thành bảng khác; hội tụ nghĩa là dãy các điểm ổn định tại một điểm bất động.

### Hình thức

Không gian $\mathcal V=\{v:\mathcal S\to\mathbb R\}$ với chuẩn vô cùng $\|v\|_\infty=\max_s|v(s)|$. Toán tử theo chính sách:

$$(T^\pi v)(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v(s')\bigr].$$

Toán tử tối ưu:

$$(T_* v)(s)=\max_a\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v(s')\bigr].$$

Nhận xét: $v^\pi$ là điểm bất động của $T^\pi$; $v_*$ là điểm bất động của $T_*$; quy hoạch động là lặp các toán tử Bellman tới khi ổn định.

::: proof Bổ đề đơn điệu của $T^\pi$ và $T_*$ (hw3 Bài 7)
Nếu $u\le v$ theo từng điểm thì với mỗi $a$, tổng $\sum_{s',r}p(s',r\mid s,a)[r+\gamma u(s')]\le\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$ vì $\gamma\ge 0$ và trọng số $p$ không âm. Kỳ vọng theo $\pi$ bảo toàn bất đẳng thức nên $T^\pi u\le T^\pi v$; lấy cực đại và dùng bất đẳng thức cực đại (nếu $f_a\le g_a$ với mọi $a$ thì $\max_a f_a\le\max_a g_a$) được $T_*u\le T_*v$.
:::

### Ứng dụng và giới hạn

Khung này cho phép dùng định lý điểm bất động (Banach) khi chứng minh hội tụ. Nó đòi hỏi $\gamma<1$; với $\gamma=1$ toán tử không co và phân tích phải đổi hẳn.

::: exercise Câu hỏi kiểm tra
Tính $(T_* v)(s_0)$ cho micro-example topic 02 (hai hành động, $v_*(s_1)=20$) khi bảng đầu vào là $v(s_0)=0, v(s_1)=10$.
:::

::: hint
Tính hai nhánh $r+\gamma v(s')$ rồi lấy cực đại.
:::

::: solution
Nhánh $a$: $1+0.9\cdot 0=1$; nhánh $b$: $2+0.9\cdot 10=11$. Vậy $(T_* v)(s_0)=11$.
:::

<!-- note-topic-id: lec-04-topic-05 -->
## Lặp chính sách trên MDP hai trạng thái

- Nhóm: cốt lõi.
- Vai trò trong mạch: ví dụ tính được trọn vẹn một chu trình đánh giá–cải thiện của PI.
- Kết nối vào: Bellman kỳ vọng (topic 01) và ý tưởng tham lam (topic 03).
- Kết nối ra: thuật toán PI tổng quát ở topic 07.
- Nguồn: PDF nguồn trang 17–19.

### Vấn đề

Cho MDP hai trạng thái, hai hành động, $\gamma=0.9$, chuyển tất định: $s_0\xrightarrow{a}(1,s_0)$, $s_0\xrightarrow{b}(0,s_1)$, $s_1\xrightarrow{a}(2,s_0)$, $s_1\xrightarrow{b}(3,s_1)$. Chạy PI từ $\pi_0=(a,a)$ và tìm chính sách tối ưu.

### Trực giác

Đánh giá chính sách hiện tại bằng hệ tuyến tính, rồi ở mỗi trạng thái so sánh $q^\pi(s,a)$ với $q^\pi(s,b)$ để đổi quyết định nếu có lợi.

### Ví dụ tính được

::: example Tính lại từng bước
Đánh giá $\pi_0=(a,a)$:

$$v^{\pi_0}(s_0)=1+0.9\,v^{\pi_0}(s_0)\Rightarrow v^{\pi_0}(s_0)=10,$$
$$v^{\pi_0}(s_1)=2+0.9\cdot 10=11.$$

Cải thiện theo $v^{\pi_0}$:

- Tại $s_0$: $q^{\pi_0}(s_0,a)=1+0.9\cdot 10=10$; $q^{\pi_0}(s_0,b)=0+0.9\cdot 11=9.9$. Chọn $a$.
- Tại $s_1$: $q^{\pi_0}(s_1,a)=2+0.9\cdot 10=11$; $q^{\pi_0}(s_1,b)=3+0.9\cdot 11=12.9$. Chọn $b$.

Chính sách mới $\pi_1=(a,b)$. Đánh giá:

$$v^{\pi_1}(s_0)=1+0.9\,v^{\pi_1}(s_0)\Rightarrow v^{\pi_1}(s_0)=10,\qquad v^{\pi_1}(s_1)=3+0.9\cdot 10=30.$$

Cải thiện tiếp: $q^{\pi_1}(s_0,a)=10$; $q^{\pi_1}(s_0,b)=0+0.9\cdot 30=27$. Chọn $b$, được $\pi_2=(b,b)$. Đánh giá: $v^{\pi_2}(s_1)=3+0.9\,v^{\pi_2}(s_1)=30$; $v^{\pi_2}(s_0)=0+0.9\cdot 30=27$. Cải thiện từ $\pi_2$ không đổi chính sách, nên $\pi_2$ tối ưu với $v^{\pi_2}=(27,30)$.
:::

### Hình thức

Mỗi vòng PI gồm hai phép toán: giải $v^\pi=r^\pi+\gamma P^\pi v^\pi$ và lấy $\pi'(s)\in\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v^\pi(s')]$.

### Ứng dụng và giới hạn

Ví dụ cho thấy PI có thể cần nhiều hơn một vòng cải thiện trước khi dừng. Chi phí đánh giá trọn vẹn một chính sách là điểm yếu trên không gian trạng thái lớn.

::: exercise Câu hỏi kiểm tra
Tính $v^{\pi_1}(s_1)$ nếu $\gamma=0.5$ thay vì $0.9$, giữ $\pi_1=(a,b)$.
:::

::: hint
Giải $v(s_0)=1+0.5v(s_0)$ trước.
:::

::: solution
$v^{\pi_1}(s_0)=2$; $v^{\pi_1}(s_1)=3+0.5\cdot 2=4$.
:::

<!-- note-topic-id: lec-04-topic-06 -->
## Đánh giá chính sách lặp

- Nhóm: cầu nối.
- Vai trò trong mạch: trình bày cách tính gần đúng $v^\pi$ bằng lặp toán tử $T^\pi$; nối toán tử với bước đánh giá của PI.
- Kết nối vào: toán tử $T^\pi$ ở topic 04.
- Kết nối ra: bước đánh giá trong PI (topic 07) và dạng cập nhật của VI (topic 08).
- Nguồn: PDF nguồn trang 14–15.

### Vấn đề

Giải hệ $v^\pi=r^\pi+\gamma P^\pi v^\pi$ bằng nghịch đảo ma trận tốn $O(|\mathcal S|^3)$. Cần cách lặp rẻ hơn và dễ phân tích.

### Trực giác

Bắt đầu từ $v_0$ bất kỳ, thường bằng $0$; mỗi lượt áp dụng $T^\pi$ làm bảng giá trị nhìn xa thêm một lớp về tương lai. Sai số so với $v^\pi$ giảm theo $\gamma$ mỗi lượt.

### Hình thức

Cập nhật đồng bộ:

$$v_{k+1}(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_k(s')\bigr],$$

tức $v_{k+1}=T^\pi v_k$. Vì $T^\pi$ co với hệ số $\gamma$, $v_k\to v^\pi$ từ mọi $v_0$. Chặn đánh giá: nếu sau một lượt $\|v_{j+1}-v_j\|_\infty\le\varepsilon_{\text{step}}$, chuỗi hình học cho $\|v_{j+1}-v^\pi\|_\infty\le\gamma\,\varepsilon_{\text{step}}/(1-\gamma)$. Đây là chặn đánh giá chất lượng bảng trả về, không bảo đảm lặp chính sách sửa đổi dừng hữu hạn; dừng hữu hạn chỉ được bảo đảm với đánh giá chính xác ở topic 07. Dạng bất đồng bộ: cập nhật từng trạng thái và dùng ngay giá trị mới cho các cập nhật kế tiếp; hội tụ vẫn bảo đảm nếu lịch cập nhật là công bằng, tức mỗi trạng thái được cập nhật vô hạn lần.

### Ứng dụng và giới hạn

Trong PI, đánh giá chính xác của mỗi chính sách là điều kiện của bảo đảm dừng hữu hạn sẽ phát biểu ở topic 07 và chứng minh ở topic 12; thay đánh giá chính xác bằng đánh giá lặp dừng sớm chỉ cho một xấp xỉ, và xấp xỉ này chưa được phân tích ở đây. Lịch không công bằng có thể làm một nhóm trạng thái bị bỏ lại và giá trị không ổn định.

::: exercise Câu hỏi kiểm tra
Với MDP topic 05 và $\pi=(a,a)$, $v_0=0$, tính $v_1$ và $v_2$ theo cập nhật đồng bộ.
:::

::: hint
Áp dụng công thức với $v_0=0$ rồi với $v_1$.
:::

::: solution
$v_1(s_0)=1$, $v_1(s_1)=2$. $v_2(s_0)=1+0.9\cdot 1=1.9$; $v_2(s_1)=2+0.9\cdot 1=2.9$. Dãy tiến về $(10,11)$.
:::

<!-- note-topic-id: lec-04-topic-07 -->
## Thuật toán lặp chính sách

- Nhóm: cốt lõi.
- Vai trò trong mạch: thuật toán PI chính xác, định lý cải thiện và bảo đảm dừng hữu hạn.
- Kết nối vào: đánh giá lặp (topic 06) và ví dụ hai trạng thái (topic 05).
- Kết nối ra: chứng minh tồn tại tối ưu và dừng hữu hạn ở topic 12.
- Nguồn: PDF nguồn trang 20–21, 33.

### Vấn đề

Cần một quy trình lặp giữa đánh giá và cải thiện, kèm bảo đảm dừng tại chính sách tối ưu.

### Trực giác

Cải thiện tham lam theo $v^\pi$ không bao giờ làm chính sách tệ hơn; số chính sách xác định hữu hạn nên chuỗi cải thiện nghiêm ngặt không thể kéo dài vô hạn.

### Thuật toán

Lặp chính sách:

1. Khởi tạo chính sách $\pi$ bất kỳ.
2. Đánh giá chính sách để thu được $v^\pi$ (giải hệ hoặc lặp $T^\pi$).
3. Cải thiện: $\pi'(s)\in\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v^\pi(s')]$.
4. Nếu $\pi'=\pi$ thì dừng; ngược lại đặt $\pi\leftarrow\pi'$ và lặp lại.

Khi có nhiều hành động đạt cực đại, phá hòa bằng thứ tự cố định để thuật toán xác định. Bảo đảm dừng hữu hạn dưới đây yêu cầu bước đánh giá đạt đúng $v^\pi$; đánh giá dừng sớm thuộc biến thể chưa được phân tích ở đây.

### Chứng minh ý chính

::: proof Định lý cải thiện chính sách
Nếu $\pi'$ tham lam theo $v^\pi$ thì $v^{\pi'}(s)\ge v^\pi(s)$ với mọi $s$. Ý tưởng: vì $\pi'$ tham lam, $T^{\pi'}v^\pi=T_*v^\pi\ge T^\pi v^\pi=v^\pi$. Áp dụng tính đơn điệu của $T^{\pi'}$ nhiều lần: $(T^{\pi'})^k v^\pi\to v^{\pi'}$ khi $k\to\infty$, và bất đẳng thức được bảo toàn qua mỗi lần áp dụng, nên $v^{\pi'}\ge v^\pi$.
:::

Hệ quả: dãy $v^{\pi_k}$ không giảm theo từng điểm. Số chính sách xác định dừng là hữu hạn; lập luận chỉ cần tính hữu hạn của tập chính sách. Tổng quát, số chính sách xác định là tích theo $s$ của $|\mathcal A(s)|$; khi mọi trạng thái có cùng tập hành động thì rút thành $|\mathcal A|^{|\mathcal S|}$ (sửa so với nguồn trang 33, nơi ghi $|\mathcal A|\,|\mathcal S|$). Vì không thể cải thiện nghiêm ngặt vô hạn lần, PI dừng sau hữu hạn bước tại một chính sách ổn định; kết hợp với topic 12, chính sách đó tối ưu.

### Ứng dụng và giới hạn

PI dừng hữu hạn là bảo đảm mạnh hơn hội tụ tiệm cận của VI. Giới hạn: mỗi vòng phải đánh giá trọn một chính sách; với $|\mathcal S|$ lớn chi phí này đáng kể.

::: exercise Câu hỏi kiểm tra
Trong ví dụ topic 05, dãy chính sách là $\pi_0=(a,a)\to\pi_1=(a,b)\to\pi_2=(b,b)$. Kiểm tra bất đẳng thức $v^{\pi_1}\ge v^{\pi_0}$ và $v^{\pi_2}\ge v^{\pi_1}$ theo từng thành phần.
:::

::: hint
So sánh $(10,30)$ với $(10,11)$ rồi $(27,30)$ với $(10,30)$.
:::

::: solution
$(10,30)\ge(10,11)$ đúng; $(27,30)\ge(10,30)$ đúng. Cả hai bước cải thiện đều không làm giảm giá trị ở bất kỳ trạng thái nào, đúng định lý.
:::

<!-- note-topic-id: lec-04-topic-08 -->
## Gridworld năm ô và các lượt lặp giá trị

- Nhóm: cốt lõi.
- Vai trò trong mạch: ví dụ tính được cho VI, cho thấy giá trị lan truyền ngược về phía khởi đầu.
- Kết nối vào: Bellman tối ưu (topic 03) và toán tử $T_*$ (topic 04).
- Kết nối ra: giả mã VI ở topic 09 và trích chính sách.
- Nguồn: PDF nguồn trang 23–28.

### Vấn đề

Năm ô thẳng hàng $c_1,\dots,c_5$; $c_5$ là trạng thái kết thúc; hành động Left, Right; mỗi bước thường thưởng $-1$; từ $c_4$ sang $c_5$ thưởng $+10$; $\gamma=0.9$. Chạy VI từ $v_0=0$ và đọc ra chính sách tối ưu.

### Trực giác

Không đánh giá trọn một chính sách trước; mỗi lượt cập nhật gộp đánh giá và cải thiện bằng phép cực đại. Thông tin về phần thưởng $+10$ lan truyền ngược một ô mỗi lượt.

### Ví dụ tính được

::: example Bảng giá trị theo lượt
Khởi tạo $v_0=(0,0,0,0,0)$. Cập nhật $v_{k+1}(c_i)=\max_a[r+\gamma v_k(s')]$ với trạng thái kết thúc giữ $0$:

| $k$ | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | $-1$ | $-1$ | $-1$ | 10 | 0 |
| 2 | $-1.9$ | $-1.9$ | 8 | 10 | 0 |
| 3 | $-2.71$ | 6.2 | 8 | 10 | 0 |
| 4 | 4.58 | 6.2 | 8 | 10 | 0 |

Ở lượt đầu, $\gamma v_0=0$ nên mỗi ô chỉ thấy phần thưởng tức thời. Kiểm tra vài ô: $v_2(c_3)=-1+0.9\cdot 10=8$; $v_3(c_2)=-1+0.9\cdot 8=6.2$; $v_4(c_1)=-1+0.9\cdot 6.2=4.58$. Sau vòng 1 chỉ $c_4$ thấy lợi ích $+10$; các ô còn lại mới thấy chi phí $-1$. Giá trị tốt lan truyền ngược dần.
:::

### Hình thức

Cập nhật VI chính là $v_{k+1}=T_*v_k$ viết theo hạt nhân. Bảng trên là các lượt áp dụng $T_*$ liên tiếp.

### Ứng dụng và giới hạn

Ví dụ quy mô nhỏ minh họa cơ chế cập nhật Bellman. Trên không gian lớn, mỗi lượt vẫn phải quét mọi cặp trạng thái–hành động, chi phí mô hình một lượt được bàn ở topic 10.

::: exercise Câu hỏi kiểm tra
Tính $v_5(c_1)$ nếu tiếp tục một lượt nữa từ bảng $v_4$.
:::

::: hint
$v_5(c_1)=-1+0.9\,v_4(c_2)$ vì đi phải là tối ưu.
:::

::: solution
$v_5(c_1)=-1+0.9\cdot 6.2=4.58$, không đổi so với $v_4(c_1)$; bảng đã ổn định.
:::

<!-- note-topic-id: lec-04-topic-09 -->
## Giả mã lặp giá trị

- Nhóm: cốt lõi.
- Vai trò trong mạch: thuật toán VI đầy đủ với đầu vào, đầu ra, điều kiện dừng và bước trích chính sách.
- Kết nối vào: cập nhật Bellman tối ưu ở topic 08.
- Kết nối ra: phân tích hội tụ ở topic 11 và phần dư ở topic 13.
- Nguồn: PDF nguồn trang 23–24, 28.

### Vấn đề

Chuyển công thức cập nhật thành thuật toán có điều kiện dừng rõ ràng và cách đọc ra chính sách từ bảng giá trị.

### Thuật toán

Lặp giá trị:

1. Khởi tạo $v_0(s)$, thường lấy $0$.
2. Lặp cho mọi trạng thái: $v_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_k(s')]$.
3. Dừng khi $\max_s|v_{k+1}(s)-v_k(s)|<\theta$.
4. Trích xuất chính sách: $\pi(s)\in\arg\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_{k+1}(s')]$.

Đầu vào: hạt nhân $p$, $\gamma$, ngưỡng $\theta$, khởi tạo $v_0$. Đầu ra: bảng giá trị gần đúng và chính sách tham lam. Điều kiện dừng dựa trên độ biến thiên giữa hai lượt; ý nghĩa sai số của tiêu chí này nằm ở topic 13.

### Ứng dụng và giới hạn

Trên Gridworld, bảng $v_4=[4.58,6.2,8,10,0]$ là $v_*$ trong chính ví dụ này, vì một lượt $T_*$ kế tiếp cho kết quả không đổi (topic 08). Chính sách trích từ $v_*$: tại $c_4$ đi phải để nhận ngay $+10$; tại $c_3$ đi phải vì $-1+0.9\cdot 10=8$; tại $c_2$ đi phải vì $-1+0.9\cdot 8=6.2$; tại $c_1$ đi phải vì $-1+0.9\cdot 6.2=4.58$. Cả bốn trạng thái đều đi phải. Giới hạn: dừng theo $\theta$ cho giá trị gần đúng, chưa chắc chính sách tối ưu nếu $\theta$ quá lớn.

::: exercise Câu hỏi kiểm tra
Với Gridworld trên, nếu $\gamma=0.5$, tính $v_2(c_3)$ và cho biết chính sách tại $c_3$ sau hai lượt.
:::

::: hint
Dùng $v_1(c_4)=10$ với $\gamma=0.5$.
:::

::: solution
$v_2(c_3)=-1+0.5\cdot 10=4$; đi phải. Nhánh trái cho $-1+0.5\cdot(-1)=-1.5<4$.
:::

<!-- note-topic-id: lec-04-topic-10 -->
## Đồng bộ, bất đồng bộ và so sánh PI–VI

- Nhóm: bổ sung.
- Vai trò trong mạch: bổ sung chi tiết triển khai và so sánh hai thuật toán dưới giả thiết rõ ràng.
- Kết nối vào: cập nhật đồng bộ (topic 06) và VI (topic 08–09).
- Kết nối ra: lựa chọn thuật toán trong bài tập thực hành.
- Nguồn: PDF nguồn trang 15, 24, 29.

### Vấn đề

Cập nhật đồng bộ tính toàn bộ $v_{k+1}$ từ cùng một bảng $v_k$; cập nhật bất đồng bộ dùng ngay giá trị mới cho các trạng thái cập nhật sau. Cần biết khi nào mỗi dạng hợp lệ và hai thuật toán PI–VI khác nhau thế nào về chi phí.

### Trực giác

Bất đồng bộ cho phép thông tin lan truyền nhanh hơn trong nhiều bài toán vì giá trị mới được khai thác ngay. Đồng bộ dễ mô tả và dễ phân tích hội tụ; trong bài này trình bày lý thuyết chủ yếu theo dạng đồng bộ.

### Hình thức

Điều kiện công bằng cho bất đồng bộ: mỗi trạng thái được cập nhật vô hạn lần trong lịch. Khi đó dãy cập nhật vẫn hội tụ về điểm bất động tương ứng. Đặt $C_{\text{model}}=O\bigl(\sum_s\sum_a|\operatorname{supp} p_{s,a}|\bigr)$: chi phí truy vấn mô hình cho một phép quét toàn bộ cặp trạng thái–hành động với hạt nhân. Một lượt cập nhật $T_*$ tốn $C_{\text{model}}$. Đánh giá chính sách chính xác bằng giải hệ đặc tốn $O(|\mathcal S|^3)$, rồi cộng một phép quét cải thiện tốn $C_{\text{model}}$ cho mỗi vòng PI. Đánh giá lặp tốn số lượt quét nhân $C_{\text{model}}$ cho mỗi lượt.

### So sánh PI–VI

| Tiêu chí | Lặp chính sách | Lặp giá trị |
|---|---|---|
| Ý tưởng | Đánh giá rồi cải thiện | Cập nhật trực tiếp theo Bellman tối ưu |
| Mỗi vòng lặp | Tốn $O(|\mathcal S|^3)+C_{\text{model}}$ nếu đánh giá chính xác | Một lượt $T_*$ tốn $C_{\text{model}}$ |
| Số vòng lặp | Không đổi chính sách thì dừng; không có chặn chung | Số lượt tới ngưỡng phụ thuộc $\gamma$, $\theta$ và bài toán |
| Trung gian | Có chính sách rõ ràng | Chủ yếu theo dõi bảng giá trị |

Bảng trên mang tính điều kiện theo chi phí đã nêu; không khẳng định thuật toán nào tuyệt đối nhanh hay rẻ nếu thiếu giả thiết về bài toán cụ thể.

### Ứng dụng và giới hạn

Chọn PI khi cần chính sách trung gian rõ ràng và chấp nhận chi phí giải hệ mỗi vòng; chọn VI khi muốn mỗi lượt chỉ tốn một phép quét $T_*$. Bài 4 của hw3 hỏi về ảnh hưởng của hai dạng cập nhật: với lịch công bằng, cả hai đều hội tụ về cùng điểm bất động; không tuyên bố ảnh hưởng đến tính tối ưu nếu thiếu lịch công bằng.

::: exercise Câu hỏi kiểm tra
Nêu một tình huống mà cập nhật bất đồng bộ hội tụ chậm hơn đồng bộ.
:::

::: hint
Xét lịch cập nhật hợp lệ nhưng dồn nhiều lượt vào một vùng trạng thái.
:::

::: solution
Nếu lịch vẫn công bằng nhưng liên tục cập nhật lại một nhóm trạng thái trước khi quay lại phần còn lại, thông tin từ phần xa chỉ lan truyền sau nhiều lượt; tổng thời gian tới ngưỡng $\theta$ có thể dài hơn đồng bộ, dù kết quả hội tụ như nhau.
:::

<!-- note-topic-id: lec-04-topic-11 -->
## Tính co của $T_*$ và hội tụ của lặp giá trị

- Nhóm: cốt lõi.
- Vai trò trong mạch: chứng minh nền tảng cho hội tụ của VI.
- Kết nối vào: toán tử $T_*$ và chuẩn vô cùng ở topic 04.
- Kết nối ra: tồn tại chính sách tối ưu ở topic 12 và phần dư ở topic 13.
- Nguồn: PDF nguồn trang 30–32.

### Vấn đề

Công thức cập nhật chưa đủ để bảo đảm tìm được nghiệm đúng. Cần chứng minh $v_k$ thực sự tiến tới $v_*$ từ mọi khởi tạo.

### Trực giác

Phép cực đại là liên tục và không phóng đại khoảng cách quá hệ số $\gamma$; mỗi lần áp dụng $T_*$ kéo hai bảng giá trị lại gần nhau.

### Chứng minh

::: proof Định lý 2: $T_*$ co
Bước 1, toán tử theo hành động cố định $a$: với $u\le v$ theo từng điểm, $\sum_{s',r}p(s',r\mid s,a)[r+\gamma u(s')]\le\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$ vì $\gamma\ge 0$. Bước 2, bất đẳng thức cực đại: nếu $f_a\le g_a$ với mọi $a$ thì $\max_a f_a\le\max_a g_a$. Do đó $T_*$ đơn điệu. Bước 3, co: đặt $d=\|u-v\|_\infty$; khi đó $u\le v+d\mathbf 1$, nên $T_*u\le T_*(v+d\mathbf 1)=T_*v+\gamma d\mathbf 1$ vì phần cộng hằng số bị chiết khấu bởi $\gamma$. Đối xứng: $\|T_*u-T_*v\|_\infty\le\gamma\|u-v\|_\infty$.
:::

Với $0\le\gamma<1$, $T_*$ là ánh xạ co trên không gian đầy đủ $\mathbb R^{|\mathcal S|}$ với chuẩn vô cùng; theo nguyên lý điểm bất động Banach, $T_*$ có đúng một điểm bất động. Vì $v_*=T_*v_*$, điểm bất động đó là $v_*$.

::: proof Hội tụ hình học
Từ $v_{k+1}=T_*v_k$ và $v_*=T_*v_*$:

$$\|v_{k+1}-v_*\|_\infty\le\gamma\|v_k-v_*\|_\infty,$$

quy nạp: $\|v_k-v_*\|_\infty\le\gamma^k\|v_0-v_*\|_\infty$. Vì $\gamma<1$, $v_k\to v_*$ từ mọi $v_0$. Sai số giảm hình học theo hệ số $\gamma$; $\gamma$ càng gần 1, hội tụ càng chậm.
:::

### Ứng dụng và giới hạn

Đây là bảo đảm toàn cục, độc lập với khởi tạo. Giới hạn: tốc độ chỉ hình học với hệ số $\gamma$; khi $\gamma\approx 1$ số lượt cần thiết tăng lớn.

::: exercise Câu hỏi kiểm tra
Với $\gamma=0.9$ và $\|v_0-v_*\|_\infty=100$, cần ít nhất bao nhiêu lượt để $\|v_k-v_*\|_\infty<1$?
:::

::: hint
Giải $0.9^k\cdot 100<1$, tức $0.9^k<10^{-2}$.
:::

::: solution
$k\ln 0.9<-2\ln 10$, $k>2\ln 10/(-\ln 0.9)\approx 4.6052/0.10536\approx 43.7$, vậy cần $k=44$ lượt.
:::

<!-- note-topic-id: lec-04-topic-12 -->
## Tồn tại chính sách tối ưu và dừng hữu hạn của PI

- Nhóm: cốt lõi.
- Vai trò trong mạch: kết luận lý thuyết trung tâm; điểm bất động của $T_*$ chặn mọi chính sách và chính sách tham lam đạt cận.
- Kết nối vào: tính co (topic 11), định lý cải thiện (topic 07).
- Kết nối ra: phần dư và mất mát ở topic 13.
- Nguồn: PDF nguồn trang 9, 21, 31–33.

### Vấn đề

Bellman tối ưu có nghiệm $v_*$, nhưng cần chứng minh tồn tại chính sách xác định đạt $v_*$ và PI dừng tại chính sách đó.

### Trực giác

Nếu $v$ là điểm bất động của $T_*$ thì không chính sách nào vượt qua $v$; do đó chính sách tham lam theo $v_*$ đạt đúng $v_*$.

### Chứng minh

::: proof Điểm bất động chặn mọi chính sách
Giả sử $v=T_*v$. Với mọi chính sách $\pi$ và mọi $s$: $T^\pi v\le T_*v=v$. Áp dụng tính đơn điệu của $T^\pi$ lặp lại: $(T^\pi)^k v\le v$ với mọi $k$; lấy giới hạn $k\to\infty$ được $v^\pi\le v$. Vậy $v$ chặn trên mọi $v^\pi$.
:::

::: proof Chính sách tham lam đạt cận và tồn tại tối ưu
Lấy $\pi_v$ tham lam theo $v_*$: $T^{\pi_v}v_*=T_*v_*=v_*$. Vì $v_*$ là điểm bất động duy nhất của $T^{\pi_v}$ (toán tử co), $v^{\pi_v}=v_*$. Kết hợp với chặn trên: $v^{\pi_v}=v_*=\max_\pi v^\pi$, tức $\pi_v$ tối ưu. Tính hữu hạn: với mỗi trạng thái, tập hành động hữu hạn nên $\max_a q_*(s,a)$ luôn đạt được; chọn hành động cực đại ở từng trạng thái cho một chính sách tối ưu dừng, xác định $\pi_*$ với $v^{\pi_*}=v_*$.
:::

::: proof PI dừng hữu hạn
Mỗi bước cải thiện cho $v^{\pi_{k+1}}\ge v^{\pi_k}$ theo từng điểm. Số chính sách xác định là $|\Pi_{\text{det}}|=\prod_s|\mathcal A(s)|$; khi mọi trạng thái có cùng tập hành động thì rút thành $|\mathcal A|^{|\mathcal S|}$, luôn hữu hạn. Chuỗi không giảm theo từng điểm trên tập hữu hạn không thể cải thiện nghiêm ngặt vô hạn lần, nên PI dừng sau hữu hạn bước tại chính sách ổn định; chính sách đó thỏa $T^\pi v^\pi=T_*v^\pi$, do đó tối ưu.
:::

### Ứng dụng và giới hạn

Ba bảo đảm trong MDP hữu hạn chiết khấu: tồn tại chính sách tối ưu; VI hội tụ về $v_*$; PI dừng hữu hạn tại chính sách tối ưu. Giới hạn: lập luận hữu hạn không cho biết số vòng PI nhiều hay ít; điều đó phụ thuộc bài toán.

::: exercise Câu hỏi kiểm tra
Trong ví dụ topic 05, kiểm tra $\pi_2=(b,b)$ thỏa $T^{\pi_2}v^{\pi_2}=T_*v^{\pi_2}$.
:::

::: hint
Tính $T_*v^{\pi_2}$ từ $v^{\pi_2}=(27,30)$.
:::

::: solution
Tại $s_0$: $\max\{1+0.9\cdot 27,\;0+0.9\cdot 30\}=\max\{25.3,27\}=27$; tại $s_1$: $\max\{2+0.9\cdot 27,\;3+0.9\cdot 30\}=\max\{26.3,30\}=30$. Cả hai khớp $v^{\pi_2}$, nên $T^{\pi_2}v^{\pi_2}=T_*v^{\pi_2}=v^{\pi_2}$: $\pi_2$ tối ưu.
:::

<!-- note-topic-id: lec-04-topic-13 -->
## Phần dư, chặn sai số và mất mát chính sách

- Nhóm: cầu nối.
- Vai trò trong mạch: định lượng khoảng cách giữa bảng lặp dừng sớm và tối ưu; nối tiêu chí dừng $\theta$ với chất lượng chính sách.
- Kết nối vào: hội tụ hình học (topic 11) và trích chính sách (topic 09).
- Kết nối ra: thực hành chọn $\theta$; đọc thêm ở topic 15.
- Nguồn: PDF nguồn trang 24, 32, 34.

### Vấn đề

VI dừng khi $\Delta_k=\max_s|v_{k+1}(s)-v_k(s)|<\theta$. Cần biết $\|v_k-v_*\|_\infty$ và mức mất mát của chính sách tham lam $\pi_v$ trích từ cùng bảng $v_k$.

### Trực giác

Nếu một lượt cập nhật gần như không đổi bảng, bảng đã gần điểm bất động; khoảng cách còn lại bị chặn bởi phần dư chia cho $(1-\gamma)$.

### Hình thức

Đặt phần dư $\rho(v)=\|v-T_*v\|_\infty$ và $\pi_v$ là chính sách tham lam theo cùng bảng $v$. Hai chặn:

$$\|v-v_*\|_\infty\le\frac{\rho(v)}{1-\gamma},$$

$$\|v_*-v^{\pi_v}\|_\infty\le\frac{2\gamma\,\rho(v)}{(1-\gamma)^2}.$$

Chặn thứ nhất: $\|v-v_*\|_\infty\le\|v-T_*v\|_\infty+\|T_*v-T_*v_*\|_\infty\le\rho+\gamma\|v-v_*\|_\infty$.

Với chặn thứ hai, đặt $L=\|v_*-v^{\pi_v}\|_\infty$, $e=\|v-v_*\|_\infty$ và dùng $T^{\pi_v}v=T_*v$:

$$
\begin{aligned}
L
&=\|T_*v_*-T^{\pi_v}v^{\pi_v}\|_\infty\\
&\le \|T_*v_*-T_*v\|_\infty
  +\|T^{\pi_v}v-T^{\pi_v}v^{\pi_v}\|_\infty\\
&\le \gamma e+\gamma\|v-v^{\pi_v}\|_\infty\\
&\le \gamma e+\gamma(e+L).
\end{aligned}
$$

Do đó $L\le 2\gamma e/(1-\gamma)\le 2\gamma\rho(v)/(1-\gamma)^2$. Vì $\rho(v_k)=\Delta_k<\theta$ khi VI dừng, hai chặn định lượng sai số giá trị và mất mát của chính sách theo $\theta,\gamma$. Ứng dụng: để bảo đảm mất mát chính sách $L\le\varepsilon_{\text{pol}}$, chọn ngưỡng $\theta\le\varepsilon_{\text{pol}}(1-\gamma)^2/(2\gamma)$ với $\gamma>0$.

### Ứng dụng và giới hạn

Cho phép chọn $\theta$ có căn cứ. Giới hạn: khi $\gamma\approx 1$, mẫu số $(1-\gamma)^2$ làm chặn mất mát nở rất nhanh; chặn là cận trên, không phải giá trị đúng.

::: exercise Câu hỏi kiểm tra
Với $\gamma=0.9$, $\theta=0.1$, ước lượng chặn trên $\|v_k-v_*\|_\infty$ và $\|v_*-v^{\pi_v}\|_\infty$ khi VI dừng.
:::

::: hint
Dùng $\rho\le\theta$ trong hai công thức.
:::

::: solution
$\|v_k-v_*\|_\infty\le 0.1/0.1=1$; $\|v_*-v^{\pi_v}\|_\infty\le 2\cdot 0.9\cdot 0.1/0.01=18$.
:::

<!-- note-topic-id: lec-04-topic-14 -->
## CartPole rời rạc và giới hạn của DP dạng bảng

- Nhóm: bổ sung.
- Vai trò trong mạch: cho thấy cách đưa môi trường liên tục về khuôn khổ MDP hữu hạn và các giới hạn kèm theo.
- Kết nối vào: toàn bộ lý thuyết DP cho MDP hữu hạn ở các topic trước.
- Kết nối ra: nhu cầu phương pháp không biết mô hình ở Bài 05.
- Nguồn: PDF nguồn trang 35–38.

### Vấn đề

CartPole có trạng thái gốc liên tục $s=(x,\dot x,\theta,\dot\theta)$ với hai hành động Left, Right. Không gian liên tục nên không áp dụng trực tiếp DP dạng bảng.

### Trực giác

Rời rạc hóa từng thành phần bằng các khoảng rời rạc (bin); mỗi tổ hợp khoảng là một trạng thái của MDP hữu hạn, sau đó áp dụng Bellman, VI hoặc PI như thường.

### Ví dụ tính được

::: example Đếm trạng thái
Chia $x$ thành 3 khoảng, $\dot x$ thành 3 khoảng, $\theta$ thành 6 khoảng, $\dot\theta$ thành 6 khoảng. Trạng thái rời rạc $s_d=(b_x,b_{\dot x},b_\theta,b_{\dot\theta})$ và số trạng thái $3\times 3\times 6\times 6=324$.
:::

### Hình thức và giới hạn

Ưu điểm: đưa môi trường liên tục về MDP hữu hạn; áp dụng được Bellman, VI, PI; dễ dùng trong giảng dạy. Hạn chế: bùng nổ số trạng thái khi tăng số khoảng; sai số xấp xỉ khi lượng tử hóa quá thô; cần mô hình chuyển hoặc mô phỏng để ước lượng xác suất chuyển. Ví dụ này là cầu nối từ lý thuyết MDP hữu hạn sang các bài toán học tăng cường gần thực tế; khi mô hình không có sẵn, cần phương pháp khác ở Bài 05.

::: exercise Câu hỏi kiểm tra
Nếu chia mỗi thành phần thành 10 khoảng, số trạng thái là bao nhiêu?
:::

::: hint
Nhân số khoảng bốn thành phần.
:::

::: solution
$10^4=10000$ trạng thái, tăng gần 31 lần so với 324; minh họa bùng nổ trạng thái.
:::

<!-- note-topic-id: lec-04-topic-15 -->
## Đọc thêm và hướng tự học

- Nhóm: đọc thêm.
- Vai trò trong mạch: mở rộng chiều sâu chứng minh và chỉ ra giới hạn của khung hữu hạn.
- Kết nối vào: các định lý ở topic 07, 11, 12.
- Kết nối ra: bài tập hw3 Bài 8, Bài 10 và các bài sau trong khóa học.
- Nguồn: PDF nguồn trang 21, 31–34; `hw3.pdf` Bài 8 và Bài 10.

### Nội dung đọc thêm

- Đọc lại phần chứng minh định lý cải thiện chính sách (trang 21) và tính co của $T_*$ (trang 31) theo từng bước; đối chiếu với các khối proof ở topic 07 và 11.
- Đọc phần sai số và tiêu chuẩn dừng (trang 34) cùng với topic 13 để hiểu vai trò của $\theta$ và $\gamma$.
- `hw3.pdf` Bài 8: bàn về MDP với môi trường và hành động liên tục; những gì phải thay đổi khi chứng minh hội tụ của lặp chính sách trong trường hợp đó. Đây là giới hạn không gian liên tục của khung DP hữu hạn.
- `hw3.pdf` Bài 10: môi trường sáu trạng thái trên đường thẳng với nhiễu tại $B$, số bước tối đa 5, $\gamma=0.5$. Bài 10 thuộc các bài sau của khóa học; phần nội dung liên quan đến Monte Carlo và Q-learning không nằm trong phạm vi Bài 04 và sẽ được trình bày ở bài tương ứng. Ở đây chỉ khuyến nghị đọc phát biểu bài toán như một ví dụ môi trường hữu hạn nhỏ.

### Giới hạn

Không trình bày Monte Carlo, sai phân thời gian, Q-learning hoặc code demo trong Bài 04. Các hướng đọc chỉ định phạm vi và thứ tự, không thay thế chứng minh trong bài.

::: exercise Câu hỏi kiểm tra
Với hw3 Bài 8, nêu hai điểm phải thay đổi khi $\mathcal S$ và $\mathcal A$ liên tục.
:::

::: hint
Nghĩ về phép cực đại theo $a$ và về khối chứng minh dùng tính hữu hạn.
:::

::: solution
Phép $\max_a$ trên tập liên tục có thể không đạt được hoặc không dễ tính, cần điều kiện compact và liên tục; lập luận dừng hữu hạn của PI dựa trên đếm số chính sách hữu hạn, không còn áp dụng trực tiếp và cần tiêu chí khác như hội tụ theo chuẩn hoặc xấp xỉ.
:::

## Bài tập 30 phút

### Bài 9 phần 1 (hw3): lặp giá trị một lượt trên MDP ba trạng thái

MDP: $\mathcal S=\{s_0,s_1,s_2\}$, $\mathcal A=\{a,b\}$, $\gamma=0.9$. Động học: từ $s_0$, hành động $a$ cho $0.5:(1,s_0)$ và $0.5:(-1,s_2)$; hành động $b$ cho $0.5:(0,s_1)$ và $0.5:(2,s_2)$. Từ $s_1$: $a$ tất định $(2,s_0)$, $b$ tất định $(-1,s_1)$. Từ $s_2$: $a$ tất định $(2,s_1)$, $b$ tất định $(0,s_0)$. Chỉ hành động từ $s_0$ có tính ngẫu nhiên 50/50.

Công thức lặp giá trị:

$$V_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V_k(s')\bigr].$$

Với $V_0(s_0)=V_0(s_1)=V_0(s_2)=0$, $\gamma V_0=0$ nên $V_1(s)=\max_a\mathbb E[r\mid s,a]$:

- $V_1(s_0)$: nhánh $a$: $0.5\cdot 1+0.5\cdot(-1)=0$; nhánh $b$: $0.5\cdot 0+0.5\cdot 2=1$. Vậy $V_1(s_0)=1$, tham lam chọn $b$.
- $V_1(s_1)$: nhánh $a$: $2$; nhánh $b$: $-1$. Vậy $V_1(s_1)=2$, tham lam chọn $a$.
- $V_1(s_2)$: nhánh $a$: $2$; nhánh $b$: $0$. Vậy $V_1(s_2)=2$, tham lam chọn $a$.

Kết quả: $V_1=(1,2,2)$; chính sách tham lam: $b$ tại $s_0$, $a$ tại $s_1$, $a$ tại $s_2$, tức $(b,a,a)$. Phần 2 là bài tự học, dùng PI ở topic 05–07, không tính trong 12 phút dành cho Bài 9 phần 1 trên lớp; tổng nhánh bài tập vẫn là 30 phút.

### Bài 6 (hw3): dạng ma trận của đánh giá chính sách

Với chính sách $\pi$, $v^\pi=r^\pi+\gamma P^\pi v^\pi$ trong đó $(r^\pi)(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\,r$ và $(P^\pi)(s,s')=\sum_a\pi(a\mid s)\sum_r p(s',r\mid s,a)$. Suy ra $(I-\gamma P^\pi)v^\pi=r^\pi$. Khi $0\le\gamma<1$: $P^\pi$ là ma trận chuyển hàng, mọi giá trị riêng $|\lambda|\le 1$, nên mọi giá trị riêng của $I-\gamma P^\pi$ có môđun $|1-\gamma\lambda|\ge 1-\gamma>0$; định thức khác không, do đó khả nghịch và $v^\pi=(I-\gamma P^\pi)^{-1}r^\pi$.

### Bài 4 (hw3): đồng bộ và bất đồng bộ

Đồng bộ: tính toàn bộ $v_{k+1}$ từ cùng một bảng $v_k$. Bất đồng bộ: cập nhật trạng thái nào xong dùng luôn cho trạng thái kế tiếp. Ảnh hưởng đến hội tụ của lặp giá trị: đồng bộ hội tụ theo phân tích co ở topic 11; bất đồng bộ vẫn hội tụ nếu lịch cập nhật công bằng, tức mỗi trạng thái được cập nhật vô hạn lần. Không tuyên bố ảnh hưởng đến tính tối ưu nếu thiếu lịch công bằng.

### Bài 7 (hw3): tính đơn điệu của $T^\pi, T_*$

Nếu $u(s)\le v(s)$ với mọi $s$, thì với mỗi $a$:

$$\sum_{s',r}p(s',r\mid s,a)[r+\gamma u(s')]\le\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$$

vì $\gamma\ge 0$ và trọng số $p$ không âm, tổng bằng 1. Lấy trung bình theo $\pi$ cho $T^\pi u\le T^\pi v$; lấy cực đại và dùng bất đẳng thức cực đại cho $T_*u\le T_*v$.

## Tài liệu tham khảo

- Tạ Việt Cường, 2026, "Giải bài toán MDPs với Quy hoạch động", Week 04 — Học tăng cường và lập kế hoạch, PDF nguồn trang 1–38.
- Tạ Việt Cường, 2026, "Bài tập tuần 3 — Giải bài toán MDP" (`hw3.pdf`): Bài 4, Bài 6, Bài 7, Bài 9, Bài 10.
- Ghi chú bổ sung: micro-example ở topic 02 được xây dựng từ công thức nguồn trang 7–8 và trình bày trong deck phụ; bảng so sánh PI–VI ở topic 10 tái cấu trúc từ trang 29; phần sửa lỗi nguồn trang 33 về số chính sách xác định $|\mathcal A|^{|\mathcal S|}$ đã nêu tại topic 07 và 12.

## Tóm tắt

- Bellman tối ưu với phép cực đại theo hành động là hạt nhân của bài toán giải MDP; $v_*(s)=\max_a q_*(s,a)$ và chính sách tham lam theo $q_*$ là tối ưu.
- Quy hoạch động giải MDP bằng cập nhật Bellman lặp: lặp chính sách đánh giá rồi cải thiện; lặp giá trị cập nhật trực tiếp theo $T_*$.
- Hội tụ được bảo đảm nhờ $T_*$ co với hệ số $\gamma$ trong chuẩn vô cùng: $\|v_k-v_*\|_\infty\le\gamma^k\|v_0-v_*\|_\infty$; PI dừng hữu hạn nhờ tính đơn điệu của cải thiện và tính hữu hạn của tập chính sách.
- Phần dư $\rho(v)$ cho hai chặn thực hành: $\|v-v_*\|_\infty\le\rho/(1-\gamma)$ và mất mát $\|v_*-v^{\pi_v}\|_\infty\le 2\gamma\rho/(1-\gamma)^2$ với $\pi_v$ tham lam theo cùng $v$.
- DP cần mô hình và không gian hữu hạn; CartPole rời rạc minh họa cả khả năng áp dụng và giới hạn bùng nổ trạng thái, dẫn sang Bài 05 về phương pháp không biết mô hình.
