# Bài 04 — Giải MDP bằng quy hoạch động

Học tăng cường — Học kỳ 1, năm học 2026–2027

<!-- note-topic-id: lec-04-part-01 -->

## 1. Mục tiêu, giả thiết và mô hình hai trạng thái

### Mục tiêu và tiên quyết

Bài trước đã xây dựng quá trình quyết định Markov (MDP) cùng hàm giá trị và phương trình Bellman, đồng thời đánh giá giá trị của một chính sách cho trước. Bài này chuyển sang bài toán tối ưu: cho trước mô hình đầy đủ, tính giá trị dài hạn của mỗi chính sách và tìm chính sách tốt nhất. Ba năng lực cần đạt là: tính trọn một lượt đánh giá một chính sách, giải thích vì sao một lần đổi hành động làm giá trị tăng, và kiểm tra điều kiện dừng bằng ngưỡng sai số. Đây là nền tảng cho các thuật toán học khi mô hình chưa biết ở các bài sau.

Tiên quyết cần nhớ từ Bài 03 gồm hai điểm. Thứ nhất, dạng kỳ vọng của phương trình Bellman: giá trị của một trạng thái bằng kỳ vọng theo chính sách của phần thưởng nhận sau khi thực hiện hành động cộng giá trị tiếp diễn đã chiết khấu, với phần thưởng mang chỉ số $R_{t+1}$. Thứ hai, tổng thưởng chiết khấu $G_0 = R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots$, trong đó $\gamma \in [0,1)$ là hệ số chiết khấu; vì $\gamma < 1$ và phần thưởng bị chặn, chuỗi này hội tụ nên giá trị là một số hữu hạn xác định.

### Giả thiết làm việc và bảng ký hiệu

Toàn bộ bài làm việc trong khung sau: tập trạng thái $\mathcal S$ hữu hạn với $n = |\mathcal S|$; mỗi trạng thái $s$ có tập hành động $\mathcal A(s)$ hữu hạn và khác rỗng, đặt $m = \max_s |\mathcal A(s)|$; xác suất chuyển và phân phối thưởng $p(s', r \mid s, a)$ được biết đầy đủ, bất biến theo thời gian; phần thưởng bị chặn; $0 \le \gamma < 1$. Vì mô hình cho biết đủ xác suất chuyển và phân phối thưởng, mọi kỳ vọng đều tính được trực tiếp trên giấy mà không cần lấy mẫu trải nghiệm.

| Ký hiệu | Ý nghĩa |
| --- | --- |
| $\pi(a \mid s)$ | chính sách Markov dừng: xác suất chọn hành động $a$ tại trạng thái $s$ |
| $G_0$ | tổng thưởng chiết khấu tính từ thời điểm khởi đầu |
| $v^\pi(s)$ | giá trị trạng thái của chính sách $\pi$: $v^\pi(s) = \mathbb E_\pi[\,G_0 \mid S_0 = s\,]$, kỳ vọng tính từ thời điểm khởi đầu |
| $q^\pi(s,a)$ | giá trị hành động: ấn định hành động đầu $a$ rồi theo $\pi$ từ bước sau, kể cả khi $\pi(a\mid s)=0$ |
| $Q_v(s,a)$ | điểm của hành động tính từ một bảng $v$ bất kỳ; với chính sách Markov dừng, $Q_{v^\pi} = q^\pi$ |
| $v_*, q_*$ | giá trị tối ưu, định nghĩa bằng $\sup$ trên lớp chính sách $\Pi$ |
| $T^\pi, T_*$ | hai toán tử Bellman nhận và trả bảng $v$, định nghĩa ở phần 2 |

Trong các tổng hiển thị dưới dạng $\sum_{s', r}$, phần thưởng $r$ chạy trên tập giá trị rời rạc mà $p(s', r \mid s, a)$ hỗ trợ. Lớp $\Pi$ ở định nghĩa tối ưu gồm mọi chính sách hợp lệ, kể cả chính sách phụ thuộc lịch sử; $v^\pi(s)$ được hiểu là giá trị khi khởi đầu tại trạng thái $s$. Định nghĩa tối ưu dùng $\sup$ trước, rồi mới chứng minh cực đại đạt được bằng tính co của toán tử ở phần sau.

### Bản đồ bài giảng

Lộ trình gồm bảy phần: (1) mục tiêu, giả thiết và mô hình hai trạng thái, (2) giá trị hành động, giá trị tối ưu và hai toán tử Bellman, (3) đánh giá một chính sách, (4) lặp chính sách, (5) lặp giá trị, (6) hội tụ và sai số, (7) tổng hợp và so sánh.

### Mô hình hai trạng thái

Mô hình làm việc có hai trạng thái $s_0, s_1$, mỗi trạng thái hai hành động $a, b$, mọi chuyển đều tất định:

| Từ | Hành động | Thưởng | Đến |
| --- | --- | --- | --- |
| $s_0$ | $a$ | $2$ | $s_0$ |
| $s_0$ | $b$ | $-1$ | $s_1$ |
| $s_1$ | $a$ | $5$ | $s_0$ |
| $s_1$ | $b$ | $10$ | $s_1$ |

Hệ số chiết khấu $\gamma = 0{,}5$. Bốn cạnh này sẽ được dùng lại liên tục trong cả bài.

![Mô hình hai trạng thái: a từ s0 nhận 2 và về s0; b từ s0 nhận −1 và tới s1; a từ s1 nhận 5 và về s0; b từ s1 nhận 10 và ở s1.](img/lec-04/two-state.svg)

### So sánh hai chính sách: 4 với 9

Cùng xuất phát từ $s_0$, xét hai chính sách. Chính sách thứ nhất luôn chọn $a$: mỗi bước nhận thưởng 2, chuỗi lặp vô hạn là cấp số nhân với mẫu số $1-\gamma$:

$$\frac{2}{1-0{,}5} = 4.$$

Chính sách thứ hai là $(b,b)$: chọn $b$ tại cả hai trạng thái. Từ $s_0$, bước đầu nhận $-1$ rồi chuyển tới $s_1$; mọi bước sau chọn $b$ ở $s_1$ và nhận thưởng $10$. Giá trị tiếp diễn tại $s_1$ của phần luôn chọn $b$ là

$$\frac{10}{1-0{,}5} = 20.$$

Phần này chiết khấu về thời điểm khởi đầu:

$$0{,}5 \cdot 20 = 10.$$

Tổng gồm phần thưởng đầu cộng phần tiếp diễn đã chiết khấu:

$$-1 + 10 = 9.$$

Ba số cần tách bạch: phần thưởng đầu ($-1$), phần tiếp diễn đã chiết khấu ($10 = 0{,}5 \cdot 20$, với $20$ là giá trị chưa chiết khấu tại $s_1$), và tổng ($9$). Chính sách thứ hai thua ở bước đầu nhưng thắng về dài hạn, vì hành động $b$ ở $s_1$ nhận thưởng 10 ở mọi bước. Đây mới là so sánh hai chính sách cụ thể; chưa chứng minh được rằng một trong hai là tối ưu trên toàn bộ lớp $\Pi$.

Đối chiếu: slide 1–5 của Bài 04.

::: exercise Câu hỏi kiểm tra
Dùng mô hình hai trạng thái với $\gamma = 0{,}5$. Cho trước giá trị của chính sách $\pi_0$ luôn chọn $a$: $v(s_0)=4$, $v(s_1)=7$ (phần 3 sẽ tính hai giá trị này từ mô hình). Tính giá trị của việc chọn $b$ tại $s_0$ rồi tiếp tục theo $\pi_0$; chỉ ra hai dữ kiện lấy từ mô hình dùng trong phép tính.
:::

::: hint
Giá trị của lựa chọn là phần thưởng trên cạnh cộng hệ số chiết khấu nhân giá trị tiếp diễn của trạng thái đến. Xác định trạng thái đến của cạnh $s_0 \xrightarrow{b}$.
:::

::: solution
Cạnh $s_0 \xrightarrow{b}$ cho thưởng $r = -1$ và chuyển đến $s_1$ với xác suất 1 — đây là hai dữ kiện lấy từ mô hình: thưởng trên cạnh và xác suất chuyển. Giá trị của lựa chọn:

$$-1 + 0{,}5 \cdot 7 = 2{,}5.$$

Kiểm lại vai trò các đại lượng: $-1$ là phần thưởng trên cạnh, $0{,}5$ là hệ số chiết khấu, $7$ là giá trị tiếp diễn $v(s_1)$ của chính sách $\pi_0$, $2{,}5$ là kết quả. Cả $7$ lẫn $2{,}5$ đều không phải phần thưởng nhận ngay.
:::

<!-- note-topic-id: lec-04-part-02 -->

## 2. Giá trị hành động, giá trị tối ưu và hai toán tử Bellman

### Tách hành động đầu và phần tiếp diễn

Mỗi lựa chọn tại một trạng thái gồm ba phần: hành động đầu, chuyển trạng thái, rồi một chính sách tiếp diễn từ trạng thái mới. Khi đánh giá một hành động cụ thể, ta giữ nguyên phần tiếp diễn theo chính sách đang xét $\pi$. Khi tìm giá trị tối ưu, phần tiếp diễn không bị ràng buộc nữa: từ trạng thái đến, ta được phép chọn chính sách tối ưu. Với chuyển trạng thái ngẫu nhiên, phải lấy kỳ vọng theo xác suất môi trường trước khi so sánh các hành động; tác tử không được chọn kết quả ngẫu nhiên. Cách tách này đặt tên cho phép tính áp dụng lên một bảng tiếp diễn bất kỳ.

### Bảng điểm $Q_v$ từ một bảng giá trị

Cho bảng tiếp diễn $v = (4, 7)$ của chính sách $\pi_0 = (a,a)$. Điểm của từng cặp (trạng thái, hành động) là thưởng ngay cộng giá trị tiếp diễn đã chiết khấu, lấy kỳ vọng theo xác suất chuyển:

$$Q_v(s,a) = \sum_{s', r} p(s', r \mid s, a)\,\bigl[\, r + \gamma v(s') \,\bigr].$$

Với mô hình tất định, bảng $Q_v$ là:

| $Q_v$ | $a$ | $b$ |
| --- | --- | --- |
| $s_0$ | $4$ | $2{,}5$ |
| $s_1$ | $7$ | $13{,}5$ |

Ô $Q_v(s_1, b) = 10 + 0{,}5 \cdot 7 = 13{,}5$ minh họa trọn một bước: thưởng 10 cộng $0{,}5$ lần giá trị tiếp diễn 7. Hai ô 4 và 7 trùng với $v$ vì đó là các hành động mà $\pi_0$ đã chọn, phần tiếp diễn quay lại chính bảng đang đánh giá.

### Định nghĩa $Q_v$ và quan hệ với $q^\pi$

Ký hiệu $Q_v$ gắn với một bảng $v$ cụ thể: nó là điểm của hành động tính từ bảng đó, chưa phải giá trị hành động của một chính sách. Ngược lại, $q^\pi(s,a)$ được định nghĩa bằng giá trị của quy trình: khởi đầu tại $s$, ấn định hành động đầu là $a$, rồi theo $\pi$ từ bước sau; quy ước này có nghĩa kể cả khi $\pi(a \mid s) = 0$. Chỉ với chính sách Markov dừng, khi bảng $v$ đúng bằng $v^\pi$, phần tiếp diễn theo $\pi$ quay lại chính bảng đang đánh giá, nên hai khái niệm trùng nhau qua bảng trạng thái:

$$Q_{v^\pi}(s,a) = q^\pi(s,a).$$

Với bảng $v = (4,7) = v^{\pi_0}$, bảng điểm vừa tính chính là $q^{\pi_0}$, chưa phải $q_*$.

### Giá trị tối ưu bằng supremum

Giả thiết hữu hạn, thưởng bị chặn và $\gamma < 1$ bảo đảm mọi giá trị hữu hạn. Định nghĩa giá trị tối ưu dùng cận trên nhỏ nhất trên lớp chính sách $\Pi$:

$$v_*(s) = \sup_{\pi \in \Pi} v^\pi(s), \qquad q_*(s,a) = \sup_{\pi \in \Pi} q^\pi(s,a).$$

Dùng $\sup$ trước khi chứng minh có chính sách đạt được nó; chứng minh dựa trên tính co của toán tử, trình bày ở phần 6. Tính chất Markov cho phép viết phần tiếp diễn bằng giá trị của trạng thái kế tiếp, dẫn tới quan hệ:

$$v_*(s) = \max_{a \in \mathcal A(s)} q_*(s,a).$$

### Phương trình Bellman tối ưu

Kết hợp quan hệ $v_*(s) = \max_a q_*(s,a)$ với khai triển kỳ vọng của $q_*$ theo phân phối chuyển, ta được phương trình Bellman tối ưu cho giá trị trạng thái:

$$v_*(s) = \max_a \sum_{s', r} p(s', r \mid s, a)\,\bigl[\, r + \gamma v_*(s') \,\bigr],$$

và cho giá trị hành động:

$$q_*(s,a) = \sum_{s', r} p(s', r \mid s, a)\,\bigl[\, r + \gamma \max_{a'} q_*(s', a') \,\bigr].$$

Phép tính có thứ tự: trước hết, với mỗi hành động, lấy kỳ vọng phần thưởng và giá trị tiếp diễn theo phân phối của môi trường; sau đó mới so các hành động và lấy cực đại. Trong công thức $q_*$, hành động đầu $a$ đã được ấn định; phép cực đại chỉ xuất hiện ở trạng thái kế tiếp, trên mọi hành động khả dĩ tại đó. So với phương trình Bellman kỳ vọng của Bài 03, điểm thay đổi duy nhất là thay trung bình theo chính sách $\pi$ bằng phép cực đại theo hành động. Đây là phương trình đặc trưng của giá trị tối ưu, chưa phải cách giải bằng cách thay số đã biết; sự tồn tại và tính duy nhất của nghiệm được chứng minh bằng tính co của toán tử ở phần 6.

### Phân biệt $\max$ và $\arg\max$

Hai ký hiệu cần tách bạch: $\max$ trả một con số, còn $\arg\max$ trả tập các hành động đạt con số đó. Chính sách tham lam theo $q_*$ vì vậy được viết bằng dấu thuộc tập:

$$\pi_*(s) \in \arg\max_a q_*(s,a).$$

Khi đã có $q_*$, chọn tại mỗi trạng thái một hành động trong tập ấy là đủ. Một chính sách tham lam theo bảng xấp xỉ có thể đã tối ưu, nhưng chỉ riêng phép chọn cực đại chưa chứng nhận điều đó. Biết đúng $q_*$ là một điều kiện đủ để cách chọn trên tạo ra chính sách tối ưu; phần 6 chứng minh kết quả này.

### Hai toán tử Bellman

Hai toán tử cùng nhận một bảng giá trị $v \in \mathcal V = \mathbb R^{|\mathcal S|}$ và cùng trả ra một bảng mới, khác nhau ở khối chọn hành động:

$$(T^\pi v)(s) = \sum_a \pi(a \mid s)\, Q_v(s,a), \qquad (T_* v)(s) = \max_a Q_v(s,a).$$

Toán tử $T^\pi$ lấy trung bình theo xác suất chính sách, nên nó giữ nguyên chính sách Markov dừng đang xét. Toán tử $T_*$ lấy cực đại theo từng hàng, tức chọn hành động tốt nhất theo chính bảng đang có. Điểm bất động của một toán tử là bảng không đổi sau phép tính: $v^\pi = T^\pi v^\pi$ và $v_* = T_* v_*$. Một lần cập nhật $T_*$ nói chung chưa cho ngay nghiệm tối ưu; tính co của toán tử ở phần sau bảo đảm lặp cập nhật hội tụ về $v_*$.

Đối chiếu: slide 6–12 của Bài 04.

::: exercise Câu hỏi kiểm tra
Vẫn với mô hình hai trạng thái, $\gamma = 0{,}5$, bảng $v = (4,7)$ và bảng $Q_v$ với ô $s_0$: $a$ cho 4, $b$ cho 2,5; ô $s_1$: $a$ cho 7, $b$ cho 13,5. Tính $T_* v$ và kết luận bảng $v$ đã phải giá trị tối ưu hay chưa. Ngoài ra, chính sách tham lam dựng theo bảng $Q_v$ này có được kết luận tối ưu ngay không?
:::

::: hint
Cực đại được lấy theo hành động trong từng hàng của bảng $Q_v$. Điểm bất động đòi hỏi toàn bảng không đổi. Lưu ý: hành động đạt cực đại theo bảng $Q_v$ hiện có chỉ là hành động tốt nhất theo bảng đang xét, chưa phải chứng nhận tối ưu của chính sách tham lam.
:::

::: solution
Từng hàng: $(T_* v)(s_0) = \max\{4,\ 2{,}5\} = 4$; $(T_* v)(s_1) = \max\{7,\ 13{,}5\} = 13{,}5$. Vậy $T_* v = (4,\ 13{,}5)$, khác với $(4,7)$, nên $v$ chưa phải $v_*$ vì chưa là điểm bất động của $T_*$. Kiểm lại: điểm bất động đòi hỏi $T_* v = v$ trên cả hai thành phần; thành phần $s_1$ đã sai lệch $13{,}5 - 7 = 6{,}5$.

Về chính sách tham lam: theo bảng $Q_v$, hành động được chọn là $a$ tại $s_0$ và $b$ tại $s_1$, tức chính sách $(a,b)$. Đây chỉ là hành động tốt nhất theo chính bảng $v = (4,7)$ đang có, mà $v$ chưa phải $v_*$, nên chưa được kết luận chính sách này tối ưu; tính tối ưu phải được kiểm chứng thêm. Phần 4 sẽ đánh giá lại chính sách này, còn phần 6 chứng minh điều kiện đủ khi biết đúng $q_*$.
:::

<!-- note-topic-id: lec-04-part-03 -->

## 3. Đánh giá giá trị của một chính sách cố định

### Đặt bài: giá trị dài hạn của $\pi_0=(a,a)$

Giữ nguyên mô hình hai trạng thái với $\gamma=0{,}5$ và bộ chuyển xác định đã thống nhất: $s_0\xrightarrow{a}s_0$ thưởng $2$, $s_0\xrightarrow{b}s_1$ thưởng $-1$, $s_1\xrightarrow{a}s_0$ thưởng $5$, $s_1\xrightarrow{b}s_1$ thưởng $10$. Ta chọn chính sách $\pi_0$ chọn hành động $a$ ở cả hai trạng thái. Vì $\pi_0$ cố định, tại mỗi trạng thái chỉ còn một hành động, nên kỳ vọng trên hành động biến mất và mỗi trạng thái cho đúng một phương trình Bellman: giá trị hiện tại bằng phần thưởng ngay cộng $\gamma$ nhân giá trị của trạng thái kế. Phần thưởng tương lai bị nhân $\gamma$ mỗi bước nên đóng góp của nó giảm dần theo cấp số nhân; chính sự giảm dần này khiến hệ phương trình có nghiệm hữu hạn và duy nhất.

### Hai phương trình Bellman và nghiệm chính xác

Đặt $x=v^{\pi_0}(s_0)$, $y=v^{\pi_0}(s_1)$. Theo các cạnh của mô hình:

$$x = 2 + 0{,}5\,x, \qquad y = 5 + 0{,}5\,x.$$

Phương trình thứ nhất chỉ chứa $x$ vì từ $s_0$ theo $a$ ta quay về chính $s_0$. Chuyển $0{,}5x$ sang vế trái: $x(1-0{,}5)=2$, tức $x=4$; đây là tổng cấp số nhân $2+0{,}5\cdot2+0{,}5^2\cdot2+\cdots$ với công bội $0{,}5$. Phương trình thứ hai dùng đúng cạnh $s_1\xrightarrow{a}s_0$, nên thay $x=4$: $y=5+0{,}5\cdot4=7$. Lỗi thường gặp là thay $x$ bằng $y$ ở đây; hãy theo đúng trạng thái kế của mô hình. Vậy

$$v^{\pi_0}=(4,\;7).$$

Cặp $(4,7)$ là nghiệm chính xác của hệ và sẽ là chuẩn đối chiếu khi ta xấp xỉ bằng lặp từ bảng $0$.

### Dạng ma trận và tính khả nghịch

Với quá trình quyết định Markov và chính sách Markov dừng $\pi$, gọi $P^\pi$ là ma trận chuyển cỡ $n\times n$ với

$$(P^\pi)_{ij}=\sum_a \pi(a\mid s_i)\sum_r p(s_j,r\mid s_i,a),$$

và $r^\pi$ là vectơ phần thưởng kỳ vọng cỡ $n$:

$$r^\pi(s_i)=\sum_a \pi(a\mid s_i)\sum_{j,r}p(s_j,r\mid s_i,a)\,r.$$

Khi $\pi$ xác định, $\pi(a\mid s_i)=1$ đúng trên $a=\pi(s_i)$, nên hai công thức rút gọn về $(P^\pi)_{ij}=\sum_r p(s_j,r\mid s_i,\pi(s_i))$ và $r^\pi(s_i)$ là phần thưởng kỳ vọng của hành động $\pi(s_i)$. Phương trình Bellman viết gọn là

$$v = r^\pi + \gamma P^\pi v \quad\Longleftrightarrow\quad (I-\gamma P^\pi)v = r^\pi.$$

$I$ là ma trận đơn vị cỡ $n\times n$. Trong ví dụ này $n=2$, $P^{\pi_0}=\begin{pmatrix}1&0\\1&0\end{pmatrix}$, $r^{\pi_0}=(2,5)$, và hệ $(I-0{,}5P^{\pi_0})v=r^{\pi_0}$ chính là hai phương trình trên. Ma trận $I-\gamma P^\pi$ luôn khả nghịch khi $0\le\gamma<1$. Chứng minh bằng không gian nghiệm: giả sử $(I-\gamma P^\pi)u=0$, tức $u=\gamma P^\pi u$. Đặt $\Delta=\max_i\lvert u_i\rvert$. Theo từng thành phần, $\lvert u_i\rvert=\gamma\lvert\sum_j (P^\pi)_{ij}u_j\rvert\le\gamma\sum_j(P^\pi)_{ij}\Delta=\gamma\Delta$, vì mỗi hàng của $P^\pi$ là phân phối xác suất. Lấy max theo $i$: $\Delta\le\gamma\Delta$, mà $\gamma<1$, nên $\Delta=0$, tức $u=0$. Nghiệm của hệ thuần nhất chỉ có nghiệm không, nên ma trận vuông $I-\gamma P^\pi$ đơn ánh, do đó khả nghịch; hệ $(I-\gamma P^\pi)v=r^\pi$ có nghiệm duy nhất $v=(I-\gamma P^\pi)^{-1}r^\pi$.

### Xấp xỉ bằng các lượt quét đồng bộ

Thay vì giải hệ, ta lặp toán tử $T^{\pi_0}$ từ bảng khởi tạo $v_0=(0,0)$, cập nhật đồng bộ: mọi trạng thái đều đọc giá trị từ bảng cũ $v_k$.

| Bảng | $v_0$ | $v_1$ | $v_2$ | $v^{\pi_0}$ |
|---|---|---|---|---|
| $s_0$ | $0$ | $2$ | $3$ | $4$ |
| $s_1$ | $0$ | $5$ | $6$ | $7$ |

Lượt một: $v_1(s_0)=2+0{,}5\cdot0=2$, $v_1(s_1)=5+0{,}5\cdot0=5$. Lượt hai: $v_2(s_0)=2+0{,}5\cdot2=3$, và $v_2(s_1)=5+0{,}5\cdot v_1(s_0)=5+0{,}5\cdot2=6$. Trong phép tính này ba đại lượng có vai trò khác nhau: thưởng tức thời $5$, giá trị cũ $v_1(s_0)=2$ lấy từ bảng trước, và kết quả $6$; nhầm thưởng với giá trị cũ là lỗi cần tránh. Dãy $(0,0)\to(2,5)\to(3,6)\to(3{,}5,6{,}5)\to\cdots$ tiến dần về $(4,7)$; mỗi lượt đưa bảng gần nghiệm hơn một bước chiết khấu, vì sai số mới bị chặn bởi $\gamma$ nhân sai số cũ sau mỗi lần áp dụng $T^{\pi_0}$.

![Mô hình theo chính sách luôn chọn a: s0 nhận thưởng 2 và trở về s0; s1 nhận thưởng 5 và chuyển về s0.](img/lec-04/policy-evaluation.svg)

### Hai lịch cập nhật: đồng bộ và tại chỗ

Cùng xuất phát từ $v_0=(0,0)$, hai lịch cho kết quả khác nhau ngay lượt đầu. Đồng bộ: cả hai trạng thái đọc bảng cũ, $s_1$ thấy $v_0(s_0)=0$ nên nhận $5$, cho $v_1=(2,5)$. Tại chỗ, theo thứ tự $s_0$ rồi $s_1$: cập nhật $s_0$ trước được $2$, rồi $s_1$ đọc ngay giá trị mới đó, nhận $5+0{,}5\cdot2=6$, cho $v_1=(2,6)$. Khác biệt một đơn vị đến hoàn toàn từ ô nguồn được dùng. Tại chỗ cho phép thông tin mới lan truyền trong cùng lượt, nhưng tốc độ hội tụ phụ thuộc vào mô hình và thứ tự cập nhật, không có bảo đảm chung rằng nó nhanh hơn đồng bộ. Điều bắt buộc với cả hai lịch: mỗi cập nhật dùng đúng phương trình Bellman với bảng hiện có, và mỗi trạng thái được cập nhật vô hạn lần; nếu một trạng thái bị bỏ qua mãi thì không còn bảo đảm hội tụ. Lịch cập nhật vô hạn lần mỗi trạng thái chỉ là lịch lý thuyết; với ngân sách lượt hữu hạn trong thực hành, kết quả trả về khác đi và phải được xử lý riêng.

### Quy trình đánh giá chính sách

Quy trình đầy đủ gồm các thành phần sau.

- **Đầu vào:** mô hình $p(s',r\mid s,a)$, chính sách $\pi$ cố định, ngưỡng $\theta>0$, ngân sách lượt $K\ge1$.
- **Khởi tạo:** bảng $v$ tùy ý; trạng thái kết thúc giữ giá trị $0$ vì không còn tương lai.
- **Một lượt:** tính đồng bộ $w=T^\pi v$; đo $\delta=\max_s\lvert w(s)-v(s)\rvert$.
- **Dừng:** nếu $\delta\le\theta$, trả $w$ với nhãn *đạt ngưỡng*; nếu đã dùng hết $K$ lượt, trả $w$ với nhãn *hết ngân sách*; còn lại gán $v=w$ và lặp.

Hai nhãn trả về phải phân biệt rõ: *hết ngân sách không chứng nhận sai số mong muốn*, vì điều kiện hội tụ thật sự là $\gamma<1$, không phải việc có đủ $K$. Về chi phí, với $n$ trạng thái, nhiều nhất $m$ hành động mỗi trạng thái và mô hình chuyển dày, mỗi lượt quét cho chính sách ngẫu nhiên tốn $O(n^2m)$ phép tính. Lưu ý quy ước: quy trình này trả bảng mới $w$; lặp giá trị ở phần sau sẽ trả bảng $v$ dùng để trích chính sách — hai quy ước không được tráo. Sai số của bảng trả về $w$ so với $v^\pi$ là $\lVert w-v^\pi\rVert_\infty$ và bị chặn bởi đại lượng $\delta$ cuối cùng nhân một hằng số phụ thuộc $\gamma$; việc thiết lập chặn đó được dành cho Phần 6.

::: exercise Câu hỏi kiểm tra
Cho $\pi_0=(a,a)$, $v_2=(3,6)$, $\gamma=0{,}5$. Tính $v_3=T^{\pi_0}v_2$ theo cập nhật đồng bộ. Vì sao phép cập nhật không có $\max$? Nếu đổi sang lịch tại chỗ với thứ tự $s_0$ rồi $s_1$, kết quả lượt này có đổi không?
:::

::: hint
Viết công thức Bellman cho từng trạng thái trước khi thay số, chú ý cả hai trạng thái đều kế tiếp $s_0$ theo $\pi_0$. Nhớ rằng cập nhật đồng bộ đọc toàn bộ từ $v_2$.
:::

::: solution
Cùng hành động $a$ ở cả hai trạng thái, nên $v_3(s_0)=2+0{,}5\cdot v_2(s_0)=2+1{,}5=3{,}5$ và $v_3(s_1)=5+0{,}5\cdot v_2(s_0)=5+1{,}5=6{,}5$; cả hai dòng đều đọc giá trị của $s_0$ vì đó là trạng thái kế theo chính sách. Vậy $v_3=(3{,}5,\;6{,}5)$. Kiểm lại bằng hệ: khoảng cách tới nghiệm $(4,7)$ đúng bằng một nửa khoảng cách của $v_2$, tức $(0{,}5,\;0{,}5)$, phù hợp tính co của $T^{\pi_0}$ với $\gamma=0{,}5$. Không có $\max$ vì $T^\pi$ đánh giá một chính sách đã cho: $\pi_0$ xác định duy nhất hành động $a$ tại mỗi trạng thái, không có gì để so sánh; $\max$ chỉ xuất hiện khi ta được chọn hành động tốt nhất. Với lịch tại chỗ, thứ tự $s_0$ rồi $s_1$: $s_0$ vẫn cho $3{,}5$ (đọc $v_2(s_0)=3$), rồi $s_1$ đọc giá trị vừa cập nhật $3{,}5$ thay vì $3$, nhận $5+0{,}5\cdot3{,}5=6{,}75$. Vậy kết quả lượt này đổi thành $(3{,}5,\;6{,}75)$ — khác biệt hoàn toàn do ô nguồn được dùng.
:::

Đối chiếu: slide 13–18 của Bài 04.

<!-- note-topic-id: lec-04-part-04 -->

## 4. Cải thiện chính sách và lặp chính sách

### Động lực: một hành động tốt hơn tại $s_1$

Bảng $v^{\pi_0}=(4,7)$ chưa nói $\pi_0$ là tốt nhất. Tại $s_1$, nếu buộc chọn $b$ đúng một lần rồi quay về theo $\pi_0$, kỳ vọng là

$$q^{\pi_0}(s_1,b)=10+0{,}5\cdot7=13{,}5>7=v^{\pi_0}(s_1).$$

Hai con số này không cùng bản chất: $7$ là giá trị của chính sách $\pi_0$, còn $13{,}5$ là giá trị khi buộc chọn $b$ một lần rồi tiếp tục theo $\pi_0$. Sai lầm thường gặp là coi $13{,}5$ là giá trị của chính sách mới. Chính sách mới $\pi_1$ chọn $b$ tại mọi lần đến $s_1$, nên đường đi của nó khác hẳn đường đi "một lần rồi quay về"; giá trị của $\pi_1$ tại $s_1$ là $20$ và phải được đánh giá riêng theo mô hình của $\pi_1$.

### Bước tham lam một bước nhìn trước

Tính $q^{\pi_0}$ tại cả hai trạng thái:

| | $a$ | $b$ |
|---|---|---|
| $s_0$ | $4$ — chọn | $2{,}5$ |
| $s_1$ | $7$ | $13{,}5$ — chọn |

Mỗi hàng được xét độc lập: tại $s_0$, $4>2{,}5$ nên giữ $a$; tại $s_1$, $13{,}5>7$ nên đổi sang $b$. Kết quả $\pi_0\to\pi_1=(a,b)$. Các số trong bảng là giá trị của hành động một lần rồi tiếp tục theo $\pi_0$, nên phần tiếp diễn vẫn theo $\pi_0$; giá trị của $\pi_1$ chưa được tính và phải tính lại từ đầu theo mô hình của $\pi_1$.

### Đánh giá lại $\pi_1$ và $\pi_2$

Với $\pi_1=(a,b)$, hệ Bellman là $x=2+0{,}5x$ (vì $s_0$ vẫn về $s_0$) cho $x=4$, và $y=10+0{,}5y$ (vì $s_1$ về chính nó) cho $y=20$; vậy $v^{\pi_1}=(4,20)$. Bước cải thiện tiếp theo so sánh trên bảng $v^{\pi_1}$: tại $s_0$, $q^{\pi_1}(s_0,b)=-1+0{,}5\cdot20=9>4=q^{\pi_1}(s_0,a)$, nên $\pi_2=(b,b)$. Đánh giá $\pi_2$: $y=10+0{,}5y=20$ và $x=-1+0{,}5\cdot20=9$, vậy $v^{\pi_2}=(9,20)$.

| Chính sách | $v(s_0)$ | $v(s_1)$ |
|---|---|---|
| $\pi_0=(a,a)$ | $4$ | $7$ |
| $\pi_1=(a,b)$ | $4$ | $20$ |
| $\pi_2=(b,b)$ | $9$ | $20$ |

Các giá trị giữ nguyên là đặc thù của ví dụ này, không phải quy luật chung. Từ $\pi_0$ sang $\pi_1$, tại $s_0$ hành động luôn là $a$ nên trạng thái tự vòng về chính nó, và mọi đường đi từ $s_0$ không bao giờ đến $s_1$ — nơi hành động đã đổi — nên $v(s_0)$ giữ nguyên $4$. Từ $\pi_1$ sang $\pi_2$, tại $s_1$ hành động luôn là $b$ nên trạng thái tự vòng về chính nó, và mọi đường đi từ $s_1$ không bao giờ đến $s_0$ — nơi hành động đã đổi — nên $v(s_1)$ giữ nguyên $20$. Nếu đường đi có thể đi qua trạng thái đã đổi hành động, kết luận này không còn đúng.

### Quy tắc tham lam với điều khoản giữ hòa

Quy tắc cải thiện cần phát biểu chặt để thuật toán tái lập được. Với $\pi$ xác định và bảng $v^\pi$, đặt

$$\pi'(s)\in\operatorname{argmax}_a Q_{v^\pi}(s,a),$$

kèm quy tắc hòa: nếu hành động cũ của $\pi$ thuộc argmax thì giữ hành động cũ; nếu không, chọn theo thứ tự cố định của tập hành động. Mọi so sánh dùng $v^\pi$ cũ, chưa cập nhật. Với $q^{\pi_0}$: tại $s_1$, $b$ thuộc argmax nên được chọn, còn hành động cũ $a$ không thuộc. Khi hai hành động đồng hạng, giữ hành động cũ ngăn thuật toán đổi qua lại giữa các chính sách tương đương qua các vòng lặp — nếu không có quy tắc này, không thể kết luận nghiêm ngặt rằng thuật toán không dao động vô hạn giữa các hành động bằng giá trị.

Trước khi chứng minh định lý, cần tính đơn điệu của toán tử: nếu $u\le v$ theo từng trạng thái thì $Q_u(s,a)\le Q_v(s,a)$ cho mọi $s,a$, vì $\gamma\ge0$ và các xác suất chuyển không âm; do đó $T^{\pi'}u\le T^{\pi'}v$ với mọi chính sách $\pi'$. Tính đơn điệu này là giả thiết được dùng ngay dưới đây.

### Định lý cải thiện chính sách

**Định lý.** Giả sử quá trình quyết định Markov hữu hạn, thưởng bị chặn, $0\le\gamma<1$; $\pi$ và $\pi'$ là chính sách Markov dừng xác định, và $\pi'$ tham lam theo $v^\pi$ với quy tắc giữ hòa. Khi đó $v^\pi\le v^{\pi'}$ theo từng trạng thái; nếu $\pi'$ khác $\pi$ thì tăng nghiêm ngặt ở ít nhất một trạng thái.

::: proof
Vì $\pi'$ chọn argmax của $Q_{v^\pi}$, ta có

$$T^{\pi'}v^\pi=\max_a Q_{v^\pi}(\cdot,a)\ge T^\pi v^\pi=v^\pi,$$

bất đẳng thức đúng vì hành động $\pi(s)$ là một ứng viên trong phép max tại mỗi trạng thái. Xét một trạng thái $s$ nơi $\pi'(s)\ne\pi(s)$: theo quy tắc giữ hòa, hành động cũ $\pi(s)$ không thuộc argmax, nên

$$(T^{\pi'}v^\pi)(s)=Q_{v^\pi}(s,\pi'(s))>Q_{v^\pi}(s,\pi(s))=(T^\pi v^\pi)(s)=v^\pi(s),$$

bất đẳng thức nghiêm ngặt tại $s$. Áp dụng $T^{\pi'}$ lặp lại và dùng tính đơn điệu vừa thiết lập:

$$v^\pi\le T^{\pi'}v^\pi\le (T^{\pi'})^2v^\pi\le\cdots$$

Sau $N$ bước, tại mỗi trạng thái đầu $s$,

$$((T^{\pi'})^Nv^\pi)(s)=\mathbb E_{\pi'}\!\left[\sum_{t=0}^{N-1}\gamma^t R_{t+1}+\gamma^N v^\pi(S_N)\,\middle|\,S_0=s\right].$$

Chọn $R_{\max}$ sao cho $|R|\le R_{\max}$. Với chuẩn $\lVert v\rVert_\infty=\max_s|v(s)|$, ta có $\lVert v^\pi\rVert_\infty\le R_{\max}/(1-\gamma)$, nên hạng đuôi có chuẩn không vượt $\gamma^N R_{\max}/(1-\gamma)$ và tiến về $0$ vì $0\le\gamma<1$. Do đó dãy hội tụ về $v^{\pi'}$, và chuyển qua giới hạn trong chuỗi bất đẳng thức cho $v^\pi\le v^{\pi'}$; tại mỗi trạng thái đã đổi hành động $s$, dùng khoảng cách nghiêm ngặt ở bước đầu đã thiết lập ở trên, ta có $v^{\pi'}(s)\ge (T^{\pi'}v^\pi)(s) > v^\pi(s)$.
:::

Hệ quả về tính nghiêm ngặt: khi $\pi'$ khác $\pi$, có ít nhất một trạng thái tăng giá trị nghiêm ngặt. Kết hợp với tính đơn điệu, mỗi lần đổi chính sách làm giá trị tăng nghiêm ngặt ở ít nhất một trạng thái, nên trong dãy chính sách của lặp chính sách không có chính sách nào lặp lại: nếu $\pi_j=\pi_i$ với $i<j$ thì $v^{\pi_i}\le v^{\pi_{i+1}}\le\cdots\le v^{\pi_j}=v^{\pi_i}$ buộc mọi bước giữa đều giữ nguyên giá trị, mâu thuẫn với tăng nghiêm ngặt. Không gian các chính sách xác định hữu hạn, cỡ $\prod_s\lvert\mathcal A(s)\rvert$ — trong ví dụ là $2\cdot2=4$ — nên thuật toán dừng sau hữu hạn vòng. Khi dừng với $\pi'=\pi$, ta có $T_*v^\pi=v^\pi$, tức thỏa phương trình tối ưu Bellman; chứng minh rằng giá trị này là tối ưu toàn cục sẽ ở Phần 6.

### Quy trình lặp chính sách

Thuật toán ghép hai khối đánh giá và cải thiện:

- **Đầu vào:** mô hình; ngân sách vòng lặp $K\ge1$; khởi tạo $\pi$ xác định.
- **Đánh giá chính xác:** giải $(I-\gamma P^\pi)v=r^\pi$, trong đó $I$ là ma trận đơn vị cỡ $n\times n$, $P^\pi$ là ma trận chuyển của $\pi$, $r^\pi$ là vectơ phần thưởng kỳ vọng.
- **Cải thiện:** tham lam trên bảng $Q$ vừa tính, giữ hòa theo quy tắc đã nêu, được $\pi'$.
- **Dừng:** nếu $\pi'=\pi$, trả $\pi$ và $v^\pi$. Nếu hết $K$ vòng, trả $\pi$ cùng $v^\pi$ với nhãn *chưa chứng nhận*; còn lại đặt $\pi=\pi'$ và lặp.

Hai điểm thực hiện quan trọng. Thứ nhất, đánh giá phải chính xác từng vòng: khi ngân sách cạn mà bước cải thiện vẫn đổi hành động, kết quả trả về là chính sách vừa được đánh giá cùng giá trị của nó — tuyệt đối không trả $\pi'$ chưa đánh giá ghép với bảng giá trị của chính sách cũ. Thứ hai, chi phí giải hệ tuyến tính cỡ $n$ là $O(n^3)$. Định lý cải thiện và lập luận hữu hạn ở trên giải thích vì sao dừng khi chính sách ổn định: với $\pi_2$, hành động $a$ cho $6{,}5$ tại $s_0$ và $9{,}5$ tại $s_1$, đều thấp hơn $9$ và $20$ của $b$, nên bước cải thiện giữ $\pi_2$. Bảo đảm dừng hữu hạn dựa trên đánh giá chính xác và quy tắc hòa, không suy rộng sang đánh giá bị cắt ngắn.

::: exercise Câu hỏi kiểm tra
Cho $v^{\pi_1}=(4,20)$. Hai giá trị $Q$ tại $s_0$ là gì? Chính sách sau cải thiện $\pi_2$ là gì? Vì sao cần giữ hành động cũ khi hai hành động hòa nhau?
:::

::: hint
Dùng bảng $v^{\pi_1}$ vừa đánh giá, chưa cập nhật, để tính $q^{\pi_1}(s_0,a)$ và $q^{\pi_1}(s_0,b)$ theo đúng cạnh chuyển và thưởng của mô hình.
:::

::: solution
Hành động $a$ từ $s_0$ về $s_0$ với thưởng $2$: $q^{\pi_1}(s_0,a)=2+0{,}5\cdot4=4$. Hành động $b$ từ $s_0$ đến $s_1$ với thưởng $-1$: $q^{\pi_1}(s_0,b)=-1+0{,}5\cdot20=9$. Vì $9>4$, chính sách sau cải thiện là $\pi_2=(b,b)$. Kiểm lại bằng định lý: $v^{\pi_2}=(9,20)\ge(4,20)=v^{\pi_1}$, tăng nghiêm ngặt đúng tại $s_0$ và giữ nguyên tại $s_1$ — không kết luận rằng cải thiện nghiêm ngặt tại mọi trạng thái. Mọi so sánh trên đều dùng $v^{\pi_1}$ cũ, chưa cập nhật. Về tiêu chí hòa: khi hai hành động đồng hạng, giữ hành động cũ ngăn thuật toán dao động giữa các chính sách tương đương qua các vòng lặp; nếu chọn tùy ý hành động đồng hạng, thuật toán có thể luân phiên giữa các chính sách có cùng giá trị mà không bao giờ dừng, nên quy tắc giữ hòa bảo đảm thuật toán tránh cách đổi chính sách này.
:::

Đối chiếu: slide 19–26 của Bài 04.

<!-- note-topic-id: lec-04-part-05 -->

## 5. Từ chi phí đánh giá đầy đủ sang lặp giá trị

### Chi phí đánh giá từng chính sách

Lặp chính sách gồm hai giai đoạn tách bạch: với chính sách $\pi$ hiện tại, giải hệ tuyến tính để có $v^\pi$, rồi tại mỗi trạng thái so sánh các hành động qua $Q_{v^\pi}(s,a)$ để cải thiện $\pi$. Việc giải đầy đủ hệ tuyến tính ở mỗi vòng có thể tốn kém khi số trạng thái lớn. Lặp giá trị chọn hướng khác: tại mỗi trạng thái, nhìn trước một bước trên bảng giá trị đang có, lấy kỳ vọng thưởng ngay cộng hệ số chiết khấu nhân giá trị bảng cũ, rồi lấy cực đại theo hành động. Nhờ vậy không cần hoàn thành đánh giá đầy đủ của một chính sách nào trước khi cải thiện; cực đại theo hành động đã gộp việc so sánh vào mỗi lượt cập nhật.

Lưới năm ô $c_1,\dots,c_5$ đủ nhỏ để tính tay toàn bộ. Quy ước dữ kiện: $\gamma=0{,}5$; bước thường thưởng $-1$ vì mỗi bước đi tốn một đơn vị; riêng chuyển $c_4\to c_5$ thưởng $24$; đi trái ở $c_1$ thì đứng nguyên tại chỗ và vẫn mất $-1$, nên đứng yên không phải lối thoát; $c_5$ là trạng thái kết thúc, sau khi vào đích quá trình dừng và không nhận thêm thưởng, do đó $v(c_5)=0$.

Đối chiếu: slide 27 của Bài 04.

![Lưới năm ô: thưởng −1 cho bước thường, thưởng 24 khi từ c4 vào đích c5; đi trái từ c1 giữ nguyên ô, giá trị đích bằng 0.](img/lec-04/gridworld.svg)

### Một lượt quét đầu tiên

Bảng khởi tạo là $v_0$ toàn số 0. Một lượt quét **đồng bộ** nghĩa là mọi trạng thái đều tính từ bảng cũ $v_0$, không dùng giá trị vừa cập nhật trong cùng lượt.

| Ô | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| $v_0$ | 0 | 0 | 0 | 0 | 0 |
| $v_1$ | $-1$ | $-1$ | $-1$ | 24 | 0 |

Tại $c_4$: đi phải nhận ngay $24$ cộng $\gamma$ nhân giá trị $c_5$ trong bảng cũ, tức $24+0{,}5\cdot 0=24$; đi trái chỉ được $-1$, nên cực đại là $24$. Ba ô còn lại không kề đích: mọi hành động đều dẫn tới ô có giá trị $0$ trong $v_0$, nên chúng chỉ ghi nhận chi phí bước đi $-1$. Việc các ô này chưa thấy đích không có nghĩa đường đi từ đó thiếu giá trị dài hạn; thông tin về phần thưởng $24$ cần thêm lượt quét mới truyền ngược tới.

Đối chiếu: slide 28 của Bài 04.

### Giá trị lan dần từ đích

Đọc bảng theo lượt $k$; mỗi lượt, ảnh hưởng của phần thưởng $24$ lùi thêm một ô về phía trái.

| $k$ | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | $-1$ | $-1$ | $-1$ | 24 | 0 |
| 2 | $-1{,}5$ | $-1{,}5$ | 11 | 24 | 0 |
| 3 | $-1{,}75$ | $4{,}5$ | 11 | 24 | 0 |
| 4 | $1{,}25$ | $4{,}5$ | 11 | 24 | 0 |
| 5 | $1{,}25$ | $4{,}5$ | 11 | 24 | 0 |

Các phép tính mẫu, luôn dùng bảng của lượt trước:

- $v_2(c_3)=-1+0{,}5\cdot 24=11$: lượt 2, $c_3$ nhìn thấy $c_4$ mang 24 trong $v_1$.
- $v_3(c_2)=-1+0{,}5\cdot 11=4{,}5$: lượt 3, $c_2$ nhận từ $c_3$.
- $v_4(c_1)=-1+0{,}5\cdot 4{,}5=1{,}25$: lượt 4, $c_1$ đọc $v_3(c_2)=4{,}5$.

Lượt 5 dùng bảng $v_4$. Tại $c_1$: đi trái tự khép, đọc $v_4(c_1)=1{,}25$, cho $-1+0{,}5\cdot 1{,}25=-0{,}375$; đi phải đọc $v_4(c_2)=4{,}5$, cho $-1+0{,}5\cdot 4{,}5=1{,}25$. Cực đại vẫn là $1{,}25$. Các ô còn lại cũng không đổi, nên $v_5=v_4$. Điểm bất động ở ví dụ này đến sau hữu hạn lượt vì mọi đường đi tối ưu tới đích $c_5$ trong ít hơn hoặc bằng 4 bước; không suy ra mọi quá trình quyết định Markov đều dừng chính xác sau hữu hạn lượt. Công thức tổng quát ở dưới giữ cùng chỉ số lượt và cùng quy ước dùng bảng cũ.

Đối chiếu: slide 29 của Bài 04.

### Quy tắc lặp giá trị

$$
v_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)\,\bigl[r+\gamma v_k(s')\bigr]
$$

Công thức khái quát đúng phép tính tay trên lưới: tại mỗi trạng thái, xét mọi hành động, lấy kỳ vọng của thưởng ngay cộng $\gamma$ nhân giá trị bảng cũ, rồi lấy cực đại. Đối chiếu: $v_2(c_3)$ dùng $v_1$, đi phải cho $-1+0{,}5\cdot 24=11$, đi trái cho $-1+0{,}5\cdot(-1)=-1{,}5$, nên $v_2(c_3)=\max\{-1{,}5,\,11\}=11$.

Hai điểm cần tách bạch. Thứ nhất, $k$ đếm lượt quét trên mô hình — mỗi lượt tính lại toàn bộ không gian trạng thái — không phải bước thời gian của một tập dữ liệu tương tác. Thứ hai, với $v_0=0$, có thể diễn giải $v_k$ là giá trị tối ưu khi còn đúng $k$ quyết định và giá trị cuối bằng 0; với khởi tạo khác, diễn giải này chỉ đúng nếu nói rõ thưởng cuối. $v_k$ không nhất thiết bằng giá trị dài hạn của một chính sách dừng nào.

Đối chiếu: slide 30 của Bài 04.

### Quy trình lặp giá trị có kiểm tra dừng

Đầu vào: mô hình $p(s',r\mid s,a)$, bảng khởi tạo $v_0$, ngưỡng phần dư $\theta>0$, ngân sách lượt $K\ge 1$. Một lượt gồm các bước sau, với bảng hiện tại $v$:

1. Tính bảng $Q_v(s,a)$ cho mọi cặp trạng thái–hành động; một lượt tính này phục vụ cả ba việc sau, không tính lặp hai lần.
2. Lấy $w(s)=\max_a Q_v(s,a)$ và $\pi_v(s)\in\arg\max_a Q_v(s,a)$, phá hòa theo thứ tự cố định.
3. Đo phần dư $\rho(v)=\max_s\lvert w(s)-v(s)\rvert$.
4. Nếu $\rho(v)\le\theta$: trả $v$, $\pi_v$, $\rho(v)$ với nhãn đạt ngưỡng. Nếu chưa đạt mà còn lượt: gán $v\leftarrow w$ rồi lặp. Nếu hết $K$ lượt: trả chính bảng $v$ đã kiểm cùng $\pi_v$, $\rho(v)$ và nhãn hết ngân sách.

Điểm dễ sai nằm ở nhánh dừng: khi hết ngân sách, trả $v$ — bảng đã được đo phần dư — chứ không âm thầm trả $w$ chưa được kiểm. $v$ là bảng đang kiểm, $w$ là bảng dự kiến sau lượt; hai vai trò này không hoán đổi. Trạng thái kết thúc luôn giữ giá trị 0. Chưa gọi $\theta$ là sai số giá trị; quan hệ giữa phần dư và sai số so với $v_*$ được lập ở phần sau.

Đối chiếu: slide 31 của Bài 04.

### Trích chính sách từ cùng bảng giá trị

$$
\pi_v(s)\in\arg\max_a Q_v(s,a),\qquad T^{\pi_v}v=T_*v
$$

Cùng một bảng $v_1=(-1,-1,-1,24,0)$ cấp dữ liệu cho hai nhánh. Nhánh tính điểm: tại $c_3$, đi trái nhìn trước sang $c_2$ cho $-1+0{,}5\cdot(-1)=-1{,}5$; đi phải sang $c_4$ cho $-1+0{,}5\cdot 24=11$; chọn phải. Số $11$ chính là $Q_{v_1}(c_3,a_R)$ với $a_R$ là hành động đi phải; đây là phép nhìn trước một bước từ $v_1$, chưa phải giá trị thật của chính sách vừa trích. Nhánh phần dư cũng dùng $v_1$: so $w(s)$ với $v_1(s)$ trên toàn bảng, $\rho(v_1)=\max_s\lvert w(s)-v_1(s)\rvert$.

Đồng nhất thức $T^{\pi_v}v=T_*v$ bảo đảm chính sách trích từ bảng $v$ chính là chính sách tham lam của phép cập nhật $T_*$: cực đại hóa theo hành động trong $T_*v$ và chọn $\pi_v$ từ $Q_v$ là cùng một phép tính. Quy ước đặt tên cần nhất quán: bảng $v$ đang kiểm, bảng $w$ sau cập nhật, chính sách $\pi_v$ trích từ $v$.

Đối chiếu: slide 32 của Bài 04.

### Chi phí của một lượt tính

Đặt $n=\lvert\mathcal S\rvert$ và $m=\max_s\lvert\mathcal A(s)\rvert$.

| Phương pháp | Thao tác mỗi lượt | Chi phí |
|---|---|---|
| Lặp giá trị, mô hình dày | Tính tổng theo trạng thái kế tiếp | $O(n^2m)$ |
| Lặp giá trị, mô hình thưa | Duyệt các nhánh có xác suất khác 0 | theo số nhánh |
| Lặp chính sách chính xác | Giải hệ dày trong bước đánh giá | $O(n^3)$ mỗi lần giải |

Một lượt lặp giá trị duyệt $n$ trạng thái, tối đa $m$ hành động tại mỗi trạng thái và $n$ trạng thái kế tiếp, nên tốn $O(n^2m)$. Chặn này giả định đã lưu xác suất chuyển $p(s'\mid s,a)$ và thưởng kỳ vọng $r(s,a)$, hoặc số nhánh thưởng cho mỗi bộ $(s,a,s')$ bị chặn. Mô hình thưa chỉ cần duyệt các nhánh có xác suất khác $0$. Lặp chính sách chính xác tốn $O(n^3)$ để giải hệ dày, rồi $O(n^2m)$ cho bước cải thiện.

Mô hình chuyển dày cần $O(n^2m)$ bộ nhớ. Ngoài mô hình, các bảng giá trị và chính sách cần $O(n)$; lưu toàn bộ $Q_v(s,a)$ cần thêm $O(nm)$. Có thể tính lần lượt các hành động và chỉ giữ cực đại để giảm bộ nhớ phụ xuống $O(n)$. Chi phí mỗi lượt chưa cho biết tổng thời gian: còn phải tính số lượt cần thiết, vốn khác nhau giữa hai thuật toán.

Đối chiếu: slide 33 của Bài 04.

::: exercise Câu hỏi kiểm tra
Cho lưới năm ô với $\gamma=0{,}5$, bước thường thưởng $-1$, chuyển $c_4\to c_5$ thưởng $24$, đi trái ở $c_1$ đứng yên, $c_5$ kết thúc với giá trị 0. Bảng hiện tại là $v_2=(-1{,}5,\,-1{,}5,\,11,\,24,\,0)$.

(a) Tính $v_3(c_1)$ và $v_3(c_2)$ theo cập nhật đồng bộ, nêu rõ điểm nhìn trước của mỗi hành động.

(b) Biết $v_4=(1{,}25,\,4{,}5,\,11,\,24,\,0)$, tính $\rho(v_3)$.

(c) Ô $c_4$ không đổi qua hai lượt. Điều đó đã đủ kết luận toàn thuật toán hội tụ chưa? Vì sao?
:::

::: hint
Trong mỗi phép tính chỉ được dùng bảng $v_2$, kể cả khi $v_3(c_1)$ đã có trong tay. Phần dư là chuẩn vô cùng của hiệu hai bảng trên toàn bộ năm ô, không chỉ các ô thay đổi.
:::

::: solution
(a) Tại $c_1$, hai hành động: đi trái tự khép đọc $v_2(c_1)=-1{,}5$, cho $-1+0{,}5\cdot(-1{,}5)=-1{,}75$; đi phải sang $c_2$ đọc $v_2(c_2)=-1{,}5$, cho $-1+0{,}5\cdot(-1{,}5)=-1{,}75$. Cực đại là $-1{,}75$, nên $v_3(c_1)=-1{,}75$. Tại $c_2$: đi trái sang $c_1$ đọc $v_2(c_1)=-1{,}5$, cho $-1{,}75$; đi phải sang $c_3$ đọc $v_2(c_3)=11$, cho $-1+0{,}5\cdot 11=4{,}5$. Cực đại là $4{,}5$, vậy $v_3(c_2)=4{,}5$. Kiểm lại: nếu lỡ dùng $v_3(c_1)=-1{,}75$ cho phép tính tại $c_2$ thì nhánh đi trái thành $-1+0{,}5\cdot(-1{,}75)=-1{,}875$, vẫn nhỏ hơn $4{,}5$ nên kết quả $v_3(c_2)$ không đổi — nhưng phép tính đó đã vi phạm quy ước đồng bộ và phải làm lại đúng quy trình.

(b) Vì $v_4=T_*v_3$, phần dư của $v_3$ là chuẩn vô cùng của hiệu hai bảng. Hiệu $v_4-v_3=(3,\,0,\,0,\,0,\,0)$, chỉ ô $c_1$ khác nhau, nên $\rho(v_3)=\lVert v_4-v_3\rVert_\infty=3$.

(c) Chưa đủ. $c_4$ giữ 24 qua hai lượt, nhưng $c_1$ và $c_2$ vẫn thay đổi giữa $v_2$ và $v_3$; phần dư $\rho(v_3)=3$ đo trên toàn bảng vẫn lớn. Đạt ngưỡng dừng phải kiểm phần dư trên toàn bộ bảng, không phải khi một ô riêng lẻ ổn định; còn hội tụ là tính chất của cả dãy giá trị, không kết luận được từ một lượt.
:::

Đối chiếu: slide 34 của Bài 04.

<!-- note-topic-id: lec-04-part-06 -->

## 6. Tính co của toán tử Bellman và các bảo đảm hội tụ

### Chuẩn vô cùng và khoảng cách giữa hai bảng giá trị

Trước khi nói về hội tụ, cần một cách đo khoảng cách giữa hai bảng giá trị. Với không gian giá trị $\mathcal V=\mathbb R^n$, mỗi bảng là một vectơ gồm $n=|\mathcal S|$ thành phần, chuẩn được dùng là chuẩn vô cùng:

$$\lVert u-v\rVert_\infty=\max_{s\in\mathcal S}\lvert u(s)-v(s)\rvert.$$

Hai bảng $u$ và $v$ ở đây không cần là giá trị của chính sách nào; chúng chỉ là hai bảng số bất kỳ. Xét MDP hai trạng thái với $\gamma=0{,}5$ và bộ số quen thuộc: $s_0,a$ trả $2$ về $s_0$; $s_0,b$ trả $-1$ về $s_1$; $s_1,a$ trả $5$ về $s_0$; $s_1,b$ trả $10$ về $s_1$. Lấy $u=(4,7)$ và $v=(8,9)$. Chênh lệch từng trạng thái là $4$ tại $s_0$ và $2$ tại $s_1$, nên $\lVert u-v\rVert_\infty=4$.

Áp dụng một lần toán tử Bellman tối ưu $T_*$ cho cả hai bảng. Tại $s_0$:

$$T_*v(s_0)=\max\{2+0{,}5\cdot 8,\,-1+0{,}5\cdot 9\}=\max\{6,\,3{,}5\}=6,$$

$$T_*u(s_0)=\max\{2+0{,}5\cdot 4,\,-1+0{,}5\cdot 7\}=\max\{4,\,2{,}5\}=4,$$

nên chênh còn $2$. Tại $s_1$:

$$T_*v(s_1)=\max\{5+0{,}5\cdot 8,\,10+0{,}5\cdot 9\}=\max\{9,\,14{,}5\}=14{,}5,$$

$$T_*u(s_1)=\max\{5+0{,}5\cdot 4,\,10+0{,}5\cdot 7\}=\max\{7,\,13{,}5\}=13{,}5,$$

nên chênh còn $1$. Kết quả: $\lVert T_*u-T_*v\rVert_\infty=2=\gamma\cdot 4$. Phần thưởng trùng nhau triệt tiêu trong phép trừ, chỉ còn phần chiết khấu nhân với chênh cũ, nên khoảng cách giảm đúng hệ số $\gamma$. Ví dụ này gợi ý một tính chất tổng quát, và tính chất đó cần được chứng minh cho mọi cặp bảng.

### Chứng minh tính co của $T_*$

Với $0\le\gamma<1$ và mọi $u,v\in\mathcal V$, khẳng định cần chứng minh là

$$\lVert T_*u-T_*v\rVert_\infty\le\gamma\,\lVert u-v\rVert_\infty.$$

Chứng minh đi qua hai bước. Bước một là bất đẳng thức giữa hai cực đại theo hành động:

$$\bigl\lvert\max_a x_a-\max_a y_a\bigr\rvert\le\max_a\lvert x_a-y_a\rvert.$$

Thật vậy, gọi $a^*$ là hành động đạt $\max_a x_a$. Khi đó $\max_a x_a-\max_a y_a=x_{a^*}-\max_a y_a\le x_{a^*}-y_{a^*}\le\max_a(x_a-y_a)\le\max_a\lvert x_a-y_a\rvert$; hoán vai trò $x$ và $y$ cho chiều ngược lại, gộp hai chiều được điều cần chứng minh.

Bước hai là so sánh hai đại lượng hành động $Q_u(s,a)$ và $Q_v(s,a)$. Với cùng cặp trạng thái–hành động, hai bảng chỉ khác phần tiếp diễn, vì phần thưởng nằm trong $p(s',r\mid s,a)$ là như nhau:

$$Q_u(s,a)-Q_v(s,a)=\gamma\sum_{s',r}p(s',r\mid s,a)\bigl[u(s')-v(s')\bigr].$$

Phần thưởng triệt tiêu trong phép trừ này, kể cả khi thưởng phụ thuộc kết quả chuyển. Lấy trị tuyệt đối và dùng bất đẳng thức tam giác, mỗi chênh $u(s')-v(s')$ bị chặn bởi $\lVert u-v\rVert_\infty$; các xác suất không âm và có tổng $1$ nên tổng trọng số bằng $1$, cho

$$\lvert Q_u(s,a)-Q_v(s,a)\rvert\le\gamma\lVert u-v\rVert_\infty.$$

Kết hợp hai bước: bất đẳng thức giữa hai cực đại truyền chặn ấy sang $T_*u(s)-T_*v(s)$; lấy cực đại trên các trạng thái cho $\lVert T_*u-T_*v\rVert_\infty\le\gamma\lVert u-v\rVert_\infty$.

Toán tử Bellman của một chính sách cố định $T^\pi$ thỏa chặn tương tự, với điều kiện $\pi$ là chính sách Markov dừng. Thay phép cực đại bằng trung bình theo $\pi(a\mid s)$, các trọng số vẫn không âm và tổng $1$, nên chặn $\gamma\lVert u-v\rVert_\infty$ được giữ nguyên. Điều kiện $0\le\gamma<1$ làm hệ số co nhỏ hơn $1$; khi $\gamma=0$, một lần cập nhật đã không phụ thuộc bảng đầu.

### Định lý Banach trong $\mathbb R^n$ với chuẩn vô cùng

Một ánh xạ $F$ trên không gian mét $(X,d)$ là co nếu tồn tại $\gamma\in[0,1)$ sao cho $d(Fx,Fy)\le\gamma\, d(x,y)$ với mọi $x,y$. Không gian $\mathbb R^n$ với chuẩn vô cùng là đầy đủ: mọi dãy Cauchy hội tụ trong không gian, vì hội tụ theo từng tọa độ trong $\mathbb R$ rồi lấy max các giới hạn. Định lý điểm bất động Banach phát biểu: mọi ánh xạ co trên không gian đầy đủ có đúng một điểm bất động $\bar v$ với $F\bar v=\bar v$, và dãy lặp $v_{k+1}=Fv_k$ hội tụ tới $\bar v$ từ mọi điểm khởi đầu.

Áp dụng cho $T_*$: tính co vừa chứng minh với $\gamma<1$ và tính đầy đủ của $(\mathcal V,\lVert\cdot\rVert_\infty)$ cho tồn tại điểm bất động duy nhất $\bar v$, tức $T_*\bar v=\bar v$. Tính duy nhất quan trọng vì nó cho phép nhận diện điểm bất động mà không cần biết trước nó là gì.

### $\bar v$ chặn mọi chính sách, kể cả phụ thuộc lịch sử

Cần chứng minh $v^\pi\le\bar v$ cho mọi chính sách trong lớp $\Pi$, trong đó lớp có thể gồm cả chính sách phụ thuộc lịch sử. Gọi $H_t=(S_0,A_0,R_1,\dots,S_t)$ là lịch sử đến thời điểm $t$; lưu ý $H_t$ không chứa $A_t$. Với $\pi$ bất kỳ trong lớp, kỳ vọng có điều kiện theo $H_t$ phải lấy trung bình theo phân phối của $A_t$ do chính sách sinh ra, rồi theo chuyển tiếp của môi trường:

$$\mathbb E_\pi\bigl[R_{t+1}+\gamma\bar v(S_{t+1})\mid H_t\bigr]=\sum_a\pi_t(a\mid H_t)\sum_{s',r}p(s',r\mid S_t,a)\bigl[r+\gamma\bar v(s')\bigr].$$

Với mỗi $a$ cố định, tổng trong ngoặc không vượt quá $\max_{a'}\sum_{s',r}p(s',r\mid S_t,a')[r+\gamma\bar v(s')]=T_*\bar v(S_t)=\bar v(S_t)$, vì $\bar v$ là điểm bất động của $T_*$. Trung bình trọng số $\pi_t(a\mid H_t)$ không âm và tổng $1$, nên

$$\mathbb E_\pi\bigl[R_{t+1}+\gamma\bar v(S_{t+1})\mid H_t\bigr]\le\bar v(S_t).$$

Nhân hai vế với $\gamma^t$ và lấy kỳ vọng khi khởi đầu tại $S_0=s$. Luật kỳ vọng lặp cho

$$\begin{aligned}
\gamma^t\mathbb E_\pi[R_{t+1}\mid S_0=s]
&\le\gamma^t\mathbb E_\pi[\bar v(S_t)\mid S_0=s]\\
&\quad-\gamma^{t+1}\mathbb E_\pi[\bar v(S_{t+1})\mid S_0=s].
\end{aligned}$$

Cộng từ $t=0$ đến $N-1$, các hạng giá trị ở giữa triệt tiêu từng cặp:

$$\mathbb E_\pi\!\left[\sum_{t=0}^{N-1}\gamma^t R_{t+1}+\gamma^N\bar v(S_N)\,\middle|\,S_0=s\right]\le\bar v(s).$$

Hạng đuôi có trị tuyệt đối không quá $\gamma^N\lVert\bar v\rVert_\infty$ và tiến về $0$ vì $\gamma<1$; tổng thưởng bị chặn nên trao đổi giới hạn và kỳ vọng hợp lệ. Kết quả là bất đẳng thức giá trị:

$$v^\pi(s)\le\bar v(s),\qquad v^\pi(s):=\mathbb E_\pi\bigl[G_0\mid S_0=s\bigr],\quad G_0=\sum_{t=0}^{\infty}\gamma^t R_{t+1}.$$

Định nghĩa $v^\pi$ qua tổng chiết khấu từ thời điểm $0$ với điều kiện $S_0=s$ là định nghĩa chuẩn cho mọi chính sách trong lớp $\Pi$, kể cả chính sách phụ thuộc lịch sử; lập luận trên chỉ dùng $T_*$ và tính Markov của môi trường, không gán toán tử $T^\pi$ cho lớp chính sách phụ thuộc lịch sử. Chặn $v^\pi\le\bar v$ do đó đúng cho toàn bộ lớp $\Pi$ trong định nghĩa tối ưu.

### Đạt cận trên bằng chính sách tham lam và kết luận $\bar v=v_*$

Cận trên $\bar v$ cần được đạt tới. Vì $\bar v$ là điểm bất động của $T_*$, tại mỗi trạng thái tồn tại hành động đạt cực đại trong $\max_a Q_{\bar v}(s,a)$. Chọn một hành động như vậy tại mỗi trạng thái, ta được chính sách Markov dừng xác định $\bar\pi$ tham lam theo $\bar v$, thỏa

$$T^{\bar\pi}\bar v=T_*\bar v=\bar v.$$

Toán tử $T^{\bar\pi}$ cũng co (đã chứng minh ở trên cho chính sách Markov dừng) và $\mathbb R^n$ đầy đủ, nên theo Banach nó có điểm bất động duy nhất; điểm bất động đó chính là $v^{\bar\pi}$, vì $v^{\bar\pi}$ thỏa phương trình Bellman đánh giá $v=T^\pi v$. Do $\bar v$ cũng là điểm bất động của $T^{\bar\pi}$, tính duy nhất cho

$$v^{\bar\pi}=\bar v.$$

Kết hợp hai kết quả: $\bar v$ chặn mọi chính sách và đạt được bởi $\bar\pi$, nên $\bar v$ là phần tử lớn nhất của $\{v^\pi:\pi\in\Pi\}$, tức $\bar v=v_*$, và $\bar\pi$ là chính sách tối ưu. Định nghĩa tối ưu dùng $\sup$ trước, và chứng minh này cho thấy $\sup$ đạt được.

### Hội tụ hình học của lặp giá trị

Tính co cho chặn hội tụ hình học. Vì $v_*$ là điểm bất động của $T_*$, áp dụng chặn co $k$ lần:

$$\lVert v_k-v_*\rVert_\infty=\lVert T_*^k v_0-T_*^k v_*\rVert_\infty\le\gamma^k\,\lVert v_0-v_*\rVert_\infty.$$

Để đọc số cụ thể, giả định sai số đầu $\lVert v_0-v_*\rVert_\infty=64$ với $\gamma=0{,}5$; đây là con số minh họa riêng, không lấy từ lưới năm ô. Chặn là $64\cdot(0{,}5)^k$. Điều kiện $64\cdot(0{,}5)^k<1$ tương đương $2^{6-k}<1$, tức $k>6$. Tại $k=6$, chặn bằng $1$, chưa nhỏ hơn $1$; tại $k=7$, chặn bằng $0{,}5$, đã đạt yêu cầu. Trục tung của hình dưới dùng thang $\log_2$ để hai mốc $1$ và $0{,}5$ đọc được rõ.

![Chặn sai số giảm từ 64 theo hệ số 0,5 mỗi lượt; bằng 1 ở lượt 6 và bằng 0,5 ở lượt 7, trục tung dùng thang logarit cơ số 2.](img/lec-04/convergence.svg)

Cần phân biệt chặn lý thuyết với thực nghiệm: bảy lượt là đủ theo chặn, không phải số lượt tối thiểu thực của mọi MDP. Hạn chế là $v_*$ chưa biết nên chặn chứa sai số ban đầu, khó dùng trực tiếp để dừng; phần dư dưới đây cung cấp một đại lượng đo được.

### Phần dư Bellman và ngưỡng dừng

Định nghĩa phần dư

$$\rho(v)=\lVert T_*v-v\rVert_\infty,$$

đo được trực tiếp từ bảng hiện có, trong khi sai số $e=\lVert v-v_*\rVert_\infty$ thì không. Suy diễn dùng bất đẳng thức tam giác:

$$\lVert v-v_*\rVert_\infty\le\lVert v-T_*v\rVert_\infty+\lVert T_*v-T_*v_*\rVert_\infty.$$

Hạng thứ nhất chính là $\rho(v)$. Hạng thứ hai bị chặn bởi $\gamma\lVert v-v_*\rVert_\infty$ nhờ tính co, vì $v_*$ là điểm bất động. Ghép lại:

$$e\le\rho(v)+\gamma e\;\Rightarrow\;(1-\gamma)e\le\rho(v)\;\Rightarrow\;e\le\frac{\rho(v)}{1-\gamma}.$$

Số cụ thể: với $\gamma=0{,}5$ và mục tiêu sai số $\varepsilon_v=0{,}2$, ngưỡng dừng trên phần dư là $\theta=(1-\gamma)\varepsilon_v=0{,}1$. Ngưỡng $0{,}1$ áp dụng cho phần dư, còn mức $0{,}2$ áp dụng cho sai số giá trị; hai mức này không tráo cho nhau. Nếu dùng bảng cập nhật $w=T^\pi v$ làm đánh giá chính sách $\pi$, đặt $\delta=\lVert T^\pi v-v\rVert_\infty$; vì $v^\pi$ là điểm bất động của $T^\pi$, tam giác và tính co cho $\lVert v-v^\pi\rVert_\infty\le\delta/(1-\gamma)$, do đó

$$\lVert w-v^\pi\rVert_\infty=\lVert T^\pi v-T^\pi v^\pi\rVert_\infty\le\gamma\lVert v-v^\pi\rVert_\infty\le\frac{\gamma\,\delta}{1-\gamma}.$$

Sai số của $w$ không vượt quá $\gamma$ lần sai số của $v$. Vì quy trình đánh giá trả bảng $w$, chặn tương ứng là $\gamma\delta/(1-\gamma)$.

### Giới hạn của mô hình dạng bảng: ví dụ CartPole

CartPole có trạng thái liên tục gồm vị trí $x$, vận tốc $\dot x$, góc $\theta$ và vận tốc góc $\dot\theta$. Chia $x$ và $\dot x$ mỗi biến thành $3$ khoảng, $\theta$ và $\dot\theta$ mỗi biến thành $6$ khoảng, số ô là

$$3\times 3\times 6\times 6=324,$$

tức một biểu diễn hữu hạn đủ để lập bảng. Nhưng rời rạc hóa chỉ tạo trạng thái gộp; nó chưa cung cấp hạt nhân chuyển và phần thưởng cho mô hình bảng, cũng chưa bảo đảm trạng thái gộp có tính Markov. Hình minh họa hai điểm liên tục khác nhau rơi vào cùng một ô: thông tin bị gộp mất.

![Hai trạng thái liên tục khác nhau của CartPole được gộp vào cùng một ô; mô hình chuyển và phần thưởng của ô vẫn cần được xác định.](img/lec-04/cartpole.svg)

Cần phân biệt hai loại sai số: sai số lặp giá trị trên mô hình đã cho (được chặn bởi $\rho(v)/(1-\gamma)$), và sai số do rời rạc hóa hoặc ước lượng mô hình. Tối ưu mô hình hữu hạn không tự chứng minh tối ưu trên môi trường liên tục, nên mọi bảo đảm như ngưỡng dừng phải kiểm tra lại miền áp dụng.

::: exercise Câu hỏi kiểm tra
MDP hữu hạn đã biết mô hình có phần dư $\rho(v)=0{,}15$ theo chuẩn vô cùng và $\gamma=0{,}5$. (a) Chặn sai số giá trị $e=\lVert v-v_*\rVert_\infty$ bằng bao nhiêu? (b) Kết quả đó đã bảo đảm ngưỡng $e\le 0{,}2$ chưa, và cần điều kiện gì trên $\rho(v)$ để bảo đảm? (c) Chứng minh phần dư còn dùng được khi $\gamma=1$ không? Giải thích từng bước.
:::

::: hint
Dùng chặn $e\le\rho(v)/(1-\gamma)$; nhớ rằng một cận trên không cho biết chiều ngược lại; kiểm tra giả thiết $\gamma<1$ được dùng ở đâu trong chứng minh tính co.
:::

::: solution
(a) Áp dụng trực tiếp: $e\le\rho(v)/(1-\gamma)=0{,}15/0{,}5=0{,}3$. (b) Chưa bảo đảm ngưỡng $0{,}2$: chặn cho biết $e\le 0{,}3$, sai số thực tế có thể nhỏ hơn $0{,}2$ nhưng chưa có bảo đảm. Muốn bảo đảm $e\le 0{,}2$ cần $\rho(v)\le(1-\gamma)\cdot 0{,}2=0{,}5\cdot 0{,}2=0{,}1$, tức phải lặp thêm cho tới khi phần dư không vượt $0{,}1$. Kiểm lại: nếu $\rho(v)=0{,}1$ thì $e\le 0{,}1/0{,}5=0{,}2$, đúng yêu cầu. (c) Không. Khi $\gamma=1$, hệ số co $\gamma$ không còn nhỏ hơn $1$ nên chứng minh tính co của $T_*$ mất giá trị; đồng thời mẫu số $1-\gamma$ bằng $0$ khiến công thức $e\le\rho(v)/(1-\gamma)$ không xác định. Chứng minh dựa trên giả thiết $\gamma<1$; bỏ giả thiết đó thì cần các giả thiết và lập luận khác, chẳng hạn các điều kiện bổ sung về chuyển tiếp và phần thưởng cùng một chứng minh hội tụ riêng; các trường hợp đó nằm ngoài phạm vi bài này.
:::

Đối chiếu: slide 35–41 của Bài 04.

<!-- note-topic-id: lec-04-part-07 -->

## 7. Chọn quy trình và đánh giá kết quả lập kế hoạch

### Bảng so sánh ba phương pháp

Ba quy trình của bài gom lại theo đầu ra cần tính:

| Phương pháp | Đầu vào | Bước chính | Đầu ra và dừng |
|---|---|---|---|
| Đánh giá chính sách | Mô hình $p,r$ và $\pi$ | Giải hệ hoặc lặp $T^\pi$ | $v^\pi$ hoặc ước lượng |
| Lặp chính sách | Mô hình | Đánh giá–cải thiện | $\pi_*,v_*$ khi ổn định |
| Lặp giá trị | Mô hình | Lặp $T_*$ | $v,\pi_v$ khi phần dư nhỏ |

Bảo đảm chung: mô hình đúng, hữu hạn, thưởng bị chặn và $0\le\gamma<1$. Nếu chỉ cần giá trị của một chính sách cho trước, đánh giá chính sách là đủ: lập hệ phương trình Bellman hoặc lặp toán tử $T^\pi$ cho tới khi hội tụ. Nếu cần chính sách tốt, có hai đường. Lặp chính sách đánh giá chính xác rồi cải thiện, giữ hành động cũ khi hòa, dừng khi chính sách không đổi nữa; nhánh này cho chứng nhận ổn định của chính sách. Lặp giá trị cập nhật bảng giá trị trực tiếp bằng $T_*$ và trích chính sách $\pi_v$ ở cuối, dừng khi phần dư nhỏ dưới ngưỡng hoặc khi hết ngân sách tính; nhánh hết ngân sách trả kết quả chưa chứng nhận đạt ngưỡng. Cả hai đều cần mô hình chuyển tiếp và thưởng, vì mọi phép tổng đều theo $p$. Khi mô hình không có, ba quy trình này không chạy được và ta phải chuyển sang học từ trải nghiệm; đó là nội dung của Bài 05.

### Lời giải cho bài toán hai trạng thái

Quay lại bài toán hai trạng thái ở mở đầu, với $\gamma=0{,}5$. Chính sách tối ưu là $\pi_*=(b,b)$ với giá trị $v_*=(9,20)$. Bảng $Q_{v_*}$ xác nhận điều đó:

| $Q_{v_*}$ | $a$ | $b$ |
|---|---|---|
| $s_0$ | $6{,}5$ | $\mathbf{9}$ |
| $s_1$ | $9{,}5$ | $\mathbf{20}$ |

Cực đại rơi ở $b$ tại cả hai trạng thái, nên $T_*v_*=v_*$: đây là chứng nhận Bellman. Kiểm tra từng ô. Tại $s_0$, chọn $b$ một lần rồi tiếp tục tối ưu:

$$Q_{v_*}(s_0,b)=-1+0{,}5\cdot 20=9,$$

còn chọn $a$ đưa hệ thống về $s_0$ với giá trị tối ưu $9$ chứ không phải $4$ của chính sách luôn chọn $a$, nên $Q_{v_*}(s_0,a)=2+0{,}5\cdot 9=6{,}5$. Tại $s_1$:

$$Q_{v_*}(s_1,b)=10+0{,}5\cdot 20=20,\qquad Q_{v_*}(s_1,a)=5+0{,}5\cdot 9=9{,}5.$$

Với $\gamma=0{,}5$, dãy thưởng $-1,10,10,\ldots$ cho giá trị $-1+0{,}5\cdot 20=9$ tại $s_0$. Giá trị ở $s_0$ tăng từ $4$ lên $9$ nhờ đổi quyết định dài hạn, trên cùng mô hình và hệ số chiết khấu. Kết luận này liên quan trực tiếp bảng phương pháp: bài toán có mô hình nên lặp giá trị hoặc lặp chính sách đều chạy được, và bảng $Q_{v_*}$ đúng là đầu ra cần kiểm khi trích chính sách từ bảng giá trị.

::: exercise Câu hỏi kiểm tra
MDP hữu hạn, mô hình chính xác, $\gamma=0{,}5$, lặp giá trị dừng với phần dư $\rho(v)=0{,}1$ theo chuẩn vô cùng và trích chính sách $\pi_v$. (a) Kết luận nào về $v$ được bảo đảm, kèm công thức? (b) Nhận định "$\pi_v$ chắc chắn tối ưu tuyệt đối" có đủ căn cứ chưa, vì sao? (c) Thuật toán nào cho chứng nhận chính sách ổn định khi đánh giá chính xác và giữ hòa?
:::

::: hint
Dùng $e\le\rho(v)/(1-\gamma)$ với $\rho=0{,}1$; phân biệt bảo đảm về giá trị gần đúng với chứng nhận tối ưu chính sách; nhớ quy tắc giữ hòa của lặp chính sách.
:::

::: solution
(a) Vì sai số giá trị bị chặn bởi phần dư với hệ số $1/(1-\gamma)$, ta có $\lVert v-v_*\rVert_\infty\le 0{,}1/0{,}5=0{,}2$. Kiểm lại chiều suy diễn: tam giác cho $e\le\rho+\gamma e$, chuyển vế được $e\le\rho/(1-\gamma)$; thay số cho $0{,}2$. (b) Chưa đủ căn cứ. Phần dư $0{,}1$ chỉ cho chặn sai số giá trị $0{,}2$; một bảng giá trị gần đúng không đồng nhất với chính sách tối ưu, nên $\pi_v$ có thể đã tối ưu nhưng chưa có bằng chứng. Một cách chứng nhận tối ưu là đánh giá chính sách chính xác rồi kiểm tra điều kiện $T_*v^\pi=v^\pi$; lặp chính sách là một phương pháp cung cấp cả hai yếu tố đó khi hội tụ ổn định, nhưng không phải phương pháp duy nhất. Chứng nhận Bellman trong ví dụ hai trạng thái ở trên vẫn có giá trị theo nghĩa này. (c) Lặp chính sách (policy iteration) đánh giá chính xác từng chính sách, cải thiện tham lam, giữ hành động cũ khi hòa, và dừng khi chính sách không đổi giữa hai lần cải thiện liên tiếp; lúc đó chính sách ổn định và là tối ưu trên mô hình đã cho.
:::

### Bài tập tự luyện

Trong [Bài tập tuần 3](../RL-hk2-2025-2026/resources/hw3.pdf), Bài 9 dùng MDP ba trạng thái và bộ dữ kiện riêng, với $\gamma=0{,}9$. Dùng đúng các cạnh chuyển và phần thưởng trong đề. Phần 1 yêu cầu lập công thức lặp giá trị, tính $V_1$ từ $V_0=0$ và chính sách tham lam tương ứng; phần 2 cho một chính sách ban đầu để lập hệ đánh giá rồi viết công thức cải thiện.

Bài 6 yêu cầu chứng minh dạng ma trận của phương trình đánh giá chính sách và tính khả nghịch của $I-\gamma P^\pi$. Bài 3 yêu cầu chứng minh sự tồn tại của chính sách tối ưu trong MDP hữu hạn; Bài 7 yêu cầu chứng minh tính đơn điệu của $T^\pi$ và $T_*$. Khi viết lại chứng minh, chỉ rõ mỗi giả thiết được dùng ở bước nào. Có thể đối chiếu các trang 20–24 và 31–34 của tài liệu bài giảng gốc.

Đối chiếu: slide 42–45 của Bài 04.

## Tài liệu tham khảo

- [Bộ slide Bài 04: Giải MDP bằng quy hoạch động](lecture-04-giai-mdp-bang-quy-hoach-dong.html), bản 45 trang dùng cho học kỳ 1, năm học 2026–2027. Đây là nguồn trực tiếp của ghi chú và các ví dụ số.
- Tạ Việt Cường, [lecture04-solving-MDP.pdf](../RL-hk2-2025-2026/lecture04-solving-MDP.pdf), 19-03-2026, đặc biệt tr. 6–10, 14, 17–25 và 31–37. Bộ slide hiện tại giữ cấu trúc mô hình hai trạng thái và lưới năm ô, đồng thời điều chỉnh phần thưởng và hệ số chiết khấu; các phép tính trong ghi chú dùng bộ số đã điều chỉnh.
- Tạ Việt Cường, [Bài tập tuần 3: Giải bài toán MDP](../RL-hk2-2025-2026/resources/hw3.pdf), 08-05-2026, tr. 1–2, Bài 3, 6, 7 và 9.
