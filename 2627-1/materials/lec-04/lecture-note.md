# Bài 04 — Ghi chú chuyên sâu về quy hoạch động

Học tăng cường — Học kỳ 1, năm học 2026–2027

Ghi chú bổ sung cho Bài 04 về giải quá trình quyết định Markov (MDP) bằng quy hoạch động. Nội dung gồm các phép tính chi tiết và chứng minh về đánh giá chính sách, cải thiện chính sách, tính co, tồn tại chính sách tối ưu và sai số dừng. Các ví dụ số ở đây độc lập với bộ trang chiếu: mô hình hai trạng thái và lưới năm ô dùng $\gamma=0{,}5$, còn bộ trang chiếu dùng $\gamma=0{,}9$. Phần thưởng và kết quả của từng ví dụ được xác định trong ghi chú; các phép tính chỉ dùng dữ kiện của cùng ví dụ. Ký hiệu và thuật ngữ thống nhất với bộ trang chiếu.

<!-- note-topic-id: lec-04-part-01 -->

## 1. Mục tiêu, giả thiết và mô hình hai trạng thái

### Mục tiêu và tiên quyết

Bài trước đã xây dựng quá trình quyết định Markov (MDP) cùng hàm giá trị và phương trình Bellman, đồng thời đánh giá giá trị của một chính sách cho trước. Bài toán tiếp theo là tối ưu trên mô hình đã biết: tính giá trị dài hạn của một chính sách và tìm chính sách tối ưu. Ghi chú phát triển ba năng lực: thực hiện một lượt đánh giá chính sách, chứng minh điều kiện để cải thiện hành động không làm giảm giá trị, và suy ra chặn sai số từ phần dư Bellman.

Hai tiên quyết từ Bài 03 là phương trình Bellman kỳ vọng và tổng thưởng chiết khấu. Theo phương trình Bellman kỳ vọng, giá trị của một trạng thái bằng kỳ vọng theo chính sách của phần thưởng nhận sau khi thực hiện hành động cộng giá trị tiếp diễn đã chiết khấu, với phần thưởng mang chỉ số $R_{t+1}$. Tổng thưởng chiết khấu $G_0 = R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots$, trong đó $\gamma \in [0,1)$ là hệ số chiết khấu; vì $\gamma < 1$ và phần thưởng bị chặn, chuỗi này hội tụ nên giá trị là một số hữu hạn xác định.

### Giả thiết làm việc và bảng ký hiệu

Các kết quả trong ghi chú dùng các giả thiết sau: tập trạng thái chưa kết thúc $\mathcal S$ hữu hạn với $n = |\mathcal S|$; mỗi trạng thái $s$ có tập hành động $\mathcal A(s)$ hữu hạn và khác rỗng, đặt $m = \max_s |\mathcal A(s)|$; xác suất chuyển và phân phối thưởng $p(s', r \mid s, a)$ được biết đầy đủ, bất biến theo thời gian; phần thưởng bị chặn; $0 \le \gamma < 1$. Vì mô hình cho biết đủ xác suất chuyển và phân phối thưởng, các kỳ vọng trong cập nhật được tính trực tiếp từ mô hình.

Nếu có trạng thái kết thúc $s_{\mathrm{term}}$, đặt $\mathcal S^+=\mathcal S\cup\{s_{\mathrm{term}}\}$. Trong các tổng theo trạng thái kế tiếp, $s'$ chạy trên $\mathcal S^+$; nếu không có kết thúc, $\mathcal S^+=\mathcal S$. Bảng giá trị có $n=|\mathcal S|$ thành phần và được mở rộng bằng giá trị $0$ tại trạng thái kết thúc. Hạng tiếp diễn tại trạng thái này luôn bằng $0$, không lấy cực đại trên tập hành động kết thúc. Sau khi quá trình tương tác kết thúc, các phần thưởng về sau được quy ước bằng $0$ để viết tổng thưởng vô hạn.

| Ký hiệu | Ý nghĩa |
| --- | --- |
| $\pi(a \mid s)$ | chính sách Markov dừng: xác suất chọn hành động $a$ tại trạng thái $s$ |
| $G_0$ | tổng thưởng chiết khấu tính từ thời điểm khởi đầu |
| $v_\pi(s)$ | giá trị trạng thái của chính sách $\pi$: $v_\pi(s) = \mathbb E_\pi[\,G_0 \mid S_0 = s\,]$, kỳ vọng tính từ thời điểm khởi đầu |
| $q_\pi(s,a)$ | giá trị hành động: ấn định hành động đầu $a$ rồi theo $\pi$ từ bước sau, kể cả khi $\pi(a\mid s)=0$ |
| $Q_V(s,a)$ | điểm của hành động tính từ một bảng $V$ bất kỳ; với chính sách Markov dừng, $Q_{v_\pi} = q_\pi$ |
| $v_*, q_*$ | giá trị tối ưu, định nghĩa bằng $\sup$ trên lớp chính sách $\Pi$ |
| $T_\pi, T_*$ | hai toán tử Bellman nhận và trả bảng $V$, định nghĩa ở phần 2 |
| $V$, $V_k$, $W$ | bảng giá trị bất kỳ, bảng sau $k$ lượt cập nhật đồng bộ và bảng mới tạm; khác với giá trị chính xác $v_\pi$ hoặc $v_*$ |
| $\Delta_\pi(V)$, $\Delta_*(V)$ | phần dư Bellman của bảng $V$ đối với $T_\pi$ và $T_*$ |
| $\eta$, $\varepsilon$ | ngưỡng phần dư và sai số giá trị yêu cầu |
| $K$ | số nguyên không âm, giới hạn số lần nhận bảng mới trong đánh giá chính sách và lặp giá trị |
| $I_{\max}$ | số nguyên dương, giới hạn số vòng đánh giá–cải thiện trong lặp chính sách |

Trong các tổng hiển thị dưới dạng $\sum_{s', r}$, phần thưởng $r$ chạy trên tập giá trị rời rạc mà $p(s', r \mid s, a)$ hỗ trợ. Lớp $\Pi$ ở định nghĩa tối ưu gồm mọi chính sách hợp lệ, kể cả chính sách phụ thuộc lịch sử; $v_\pi(s)$ được hiểu là giá trị khi khởi đầu tại trạng thái $s$. Định nghĩa tối ưu dùng $\sup$ trước, rồi mới chứng minh cực đại đạt được bằng tính co của toán tử ở phần sau.

### Cấu trúc ghi chú

Ghi chú gồm bảy phần: (1) mục tiêu, giả thiết và mô hình hai trạng thái, (2) giá trị hành động, giá trị tối ưu và hai toán tử Bellman, (3) đánh giá một chính sách, (4) lặp chính sách, (5) lặp giá trị, (6) hội tụ và sai số, (7) tổng hợp và so sánh.

### Mô hình hai trạng thái

Mô hình làm việc có hai trạng thái $s_0, s_1$, mỗi trạng thái hai hành động $a, b$, mọi chuyển đều xác định:

| Từ | Hành động | Thưởng | Đến |
| --- | --- | --- | --- |
| $s_0$ | $a$ | $2$ | $s_0$ |
| $s_0$ | $b$ | $-1$ | $s_1$ |
| $s_1$ | $a$ | $5$ | $s_0$ |
| $s_1$ | $b$ | $10$ | $s_1$ |

Hệ số chiết khấu $\gamma = 0{,}5$. Bốn cạnh này được dùng trong các phép đánh giá và cải thiện chính sách dưới đây.

![Mô hình hai trạng thái: a từ s0 nhận 2 và về s0; b từ s0 nhận −1 và tới s1; a từ s1 nhận 5 và về s0; b từ s1 nhận 10 và ở s1.](img/lec-04/two-state.svg)

### Giá trị của hai chính sách tại trạng thái khởi đầu

Cùng xuất phát từ $s_0$, xét hai chính sách. Chính sách thứ nhất luôn chọn $a$: mỗi bước nhận thưởng 2, chuỗi lặp vô hạn là cấp số nhân với mẫu số $1-\gamma$:

$$\frac{2}{1-0{,}5} = 4.$$

Chính sách thứ hai là $(b,b)$: chọn $b$ tại cả hai trạng thái. Từ $s_0$, bước đầu nhận $-1$ rồi chuyển tới $s_1$; mọi bước sau chọn $b$ ở $s_1$ và nhận thưởng $10$. Giá trị tiếp diễn tại $s_1$ của phần luôn chọn $b$ là

$$\frac{10}{1-0{,}5} = 20.$$

Phần này chiết khấu về thời điểm khởi đầu:

$$0{,}5 \cdot 20 = 10.$$

Tổng gồm phần thưởng đầu cộng phần tiếp diễn đã chiết khấu:

$$-1 + 10 = 9.$$

Ba đại lượng của tổng thưởng là phần thưởng đầu ($-1$), phần tiếp diễn đã chiết khấu ($10 = 0{,}5 \cdot 20$, với $20$ là giá trị chưa chiết khấu tại $s_1$), và tổng ($9$). Chính sách thứ hai có phần thưởng đầu thấp hơn nhưng giá trị dài hạn cao hơn, vì hành động $b$ ở $s_1$ nhận thưởng 10 ở mọi bước. Đây mới là so sánh hai chính sách cụ thể; chưa chứng minh được rằng một trong hai là tối ưu trên toàn bộ lớp $\Pi$.

Khái niệm liên quan: mô hình MDP và tổng thưởng chiết khấu; Sutton–Barto, chương 3, §3.1 và §3.3.

::: exercise Câu hỏi:
Dùng mô hình hai trạng thái với $\gamma = 0{,}5$. Cho trước giá trị của chính sách $\pi_0$ luôn chọn $a$: $v_{\pi_0}(s_0)=4$, $v_{\pi_0}(s_1)=7$ (phần 3 sẽ tính hai giá trị này từ mô hình). Tính giá trị của việc chọn $b$ tại $s_0$ rồi tiếp tục theo $\pi_0$; chỉ ra hai dữ kiện lấy từ mô hình dùng trong phép tính.
:::

::: hint
Giá trị của lựa chọn là phần thưởng trên cạnh cộng hệ số chiết khấu nhân giá trị tiếp diễn của trạng thái đến. Xác định trạng thái đến của cạnh $s_0 \xrightarrow{b}$.
:::

::: solution
Cạnh $s_0 \xrightarrow{b}$ cho thưởng $r = -1$ và chuyển đến $s_1$ với xác suất 1. Hai dữ kiện này xác định phần thưởng và trạng thái kế tiếp của phép tính. Giá trị của lựa chọn:

$$-1 + 0{,}5 \cdot 7 = 2{,}5.$$

Trong phép tính, $-1$ là phần thưởng trên cạnh, $0{,}5$ là hệ số chiết khấu, $7$ là giá trị tiếp diễn $v_{\pi_0}(s_1)$, $2{,}5$ là kết quả. Cả $7$ lẫn $2{,}5$ đều không phải phần thưởng nhận ngay.
:::

<!-- note-topic-id: lec-04-part-02 -->

## 2. Giá trị hành động, giá trị tối ưu và hai toán tử Bellman

### Tách hành động đầu và phần tiếp diễn

Mỗi lựa chọn tại một trạng thái gồm ba phần: hành động đầu, chuyển trạng thái, rồi một chính sách tiếp diễn từ trạng thái mới. Giá trị của một hành động giữ phần tiếp diễn theo chính sách đang xét $\pi$. Giá trị tối ưu xét phần tiếp diễn tốt nhất có thể từ trạng thái kế tiếp. Với chuyển trạng thái ngẫu nhiên, phải lấy kỳ vọng theo xác suất môi trường trước khi so sánh các hành động; tác tử không được chọn kết quả ngẫu nhiên. Phép nhìn trước một bước cũng có thể tính trên một bảng giá trị tiếp diễn bất kỳ.

### Bảng điểm $Q_V$ từ một bảng giá trị

Cho bảng tiếp diễn $V = (4, 7)$ của chính sách $\pi_0 = (a,a)$. Điểm của từng cặp (trạng thái, hành động) là thưởng ngay cộng giá trị tiếp diễn đã chiết khấu, lấy kỳ vọng theo xác suất chuyển:

$$Q_V(s,a) = \sum_{s', r} p(s', r \mid s, a)\,\bigl[\, r + \gamma V(s') \,\bigr].$$

Với mô hình xác định, bảng $Q_V$ là:

| $Q_V$ | $a$ | $b$ |
| --- | --- | --- |
| $s_0$ | $4$ | $2{,}5$ |
| $s_1$ | $7$ | $13{,}5$ |

Ô $Q_V(s_1, b) = 10 + 0{,}5 \cdot 7 = 13{,}5$ minh họa trọn một bước: thưởng 10 cộng $0{,}5$ lần giá trị tiếp diễn 7. Hai ô 4 và 7 trùng với $V$ vì đó là các hành động mà $\pi_0$ đã chọn, phần tiếp diễn quay lại chính bảng đang đánh giá.

### Định nghĩa $Q_V$ và quan hệ với $q_\pi$

Ký hiệu $Q_V$ gắn với một bảng $V$ cụ thể: nó là điểm của hành động tính từ bảng đó, chưa phải giá trị hành động của một chính sách. Ngược lại, $q_\pi(s,a)$ được định nghĩa bằng giá trị của quy trình: khởi đầu tại $s$, ấn định hành động đầu là $a$, rồi theo $\pi$ từ bước sau; quy ước này có nghĩa kể cả khi $\pi(a \mid s) = 0$. Chỉ với chính sách Markov dừng, khi bảng $V$ đúng bằng $v_\pi$, phần tiếp diễn theo $\pi$ quay lại chính bảng đang đánh giá, nên hai khái niệm trùng nhau qua bảng trạng thái:

$$Q_{v_\pi}(s,a) = q_\pi(s,a).$$

Với bảng $V = (4,7) = v_{\pi_0}$, bảng điểm vừa tính chính là $q_{\pi_0}$, chưa phải $q_*$.

### Giá trị tối ưu và cận trên nhỏ nhất

Giả thiết hữu hạn, thưởng bị chặn và $\gamma < 1$ bảo đảm mọi giá trị hữu hạn. Định nghĩa giá trị tối ưu dùng cận trên nhỏ nhất trên lớp chính sách $\Pi$:

$$v_*(s) = \sup_{\pi \in \Pi} v_\pi(s), \qquad q_*(s,a) = \sup_{\pi \in \Pi} q_\pi(s,a).$$

Dùng $\sup$ trước khi chứng minh có chính sách đạt được nó; chứng minh dựa trên tính co của toán tử, trình bày ở phần 6. Tính chất Markov cho phép viết phần tiếp diễn bằng giá trị của trạng thái kế tiếp, dẫn tới quan hệ:

$$v_*(s) = \max_{a \in \mathcal A(s)} q_*(s,a).$$

### Phương trình Bellman tối ưu

Kết hợp quan hệ $v_*(s) = \max_a q_*(s,a)$ với khai triển kỳ vọng của $q_*$ theo phân phối chuyển cho phương trình Bellman tối ưu của giá trị trạng thái:

$$v_*(s) = \max_a \sum_{s', r} p(s', r \mid s, a)\,\bigl[\, r + \gamma v_*(s') \,\bigr],$$

và cho giá trị hành động:

$$q_*(s,a) = \sum_{s', r} p(s', r \mid s, a)\,\bigl[\, r + \gamma \max_{a'} q_*(s', a') \,\bigr].$$

Phép tính có thứ tự: trước hết, với mỗi hành động, lấy kỳ vọng phần thưởng và giá trị tiếp diễn theo phân phối của môi trường; sau đó mới so các hành động và lấy cực đại. Trong công thức $q_*$, hành động đầu $a$ đã được ấn định; phép cực đại chỉ xuất hiện ở trạng thái kế tiếp, trên mọi hành động khả dĩ tại đó. So với phương trình Bellman kỳ vọng của Bài 03, trung bình theo chính sách $\pi$ được thay bằng cực đại theo hành động, đồng thời giá trị tiếp diễn $v_\pi$ được thay bằng $v_*$. Đây là phương trình đặc trưng của giá trị tối ưu, chưa phải cách giải bằng cách thay số đã biết; sự tồn tại và tính duy nhất của nghiệm được chứng minh bằng tính co của toán tử ở phần 6.

### Phân biệt $\max$ và $\arg\max$

Phép $\max$ trả một con số, còn $\arg\max$ trả tập các hành động đạt con số đó. Chính sách tham lam theo $q_*$ vì vậy được viết bằng dấu thuộc tập:

$$\pi_*(s) \in \arg\max_a q_*(s,a).$$

Khi đã có $q_*$, chọn tại mỗi trạng thái một hành động trong tập ấy là đủ. Một chính sách tham lam theo bảng xấp xỉ có thể đã tối ưu, nhưng chỉ riêng phép chọn cực đại chưa chứng nhận điều đó. Biết đúng $q_*$ là một điều kiện đủ để cách chọn trên tạo ra chính sách tối ưu; phần 6 chứng minh kết quả này.

### Hai toán tử Bellman

Hai toán tử cùng nhận một bảng giá trị $V \in \mathcal V = \mathbb R^{|\mathcal S|}$ và cùng trả ra một bảng mới, khác nhau ở khối chọn hành động:

$$(T_\pi V)(s) = \sum_a \pi(a \mid s)\, Q_V(s,a), \qquad (T_* V)(s) = \max_a Q_V(s,a).$$

Toán tử $T_\pi$ lấy trung bình theo xác suất chính sách, nên nó giữ nguyên chính sách Markov dừng đang xét. Toán tử $T_*$ lấy cực đại theo từng hàng, tức chọn hành động tốt nhất theo chính bảng đang có. Điểm bất động của một toán tử là bảng không đổi sau phép tính: $v_\pi = T_\pi v_\pi$ và $v_* = T_* v_*$. Một lần cập nhật $T_*$ nói chung chưa cho ngay nghiệm tối ưu; tính co của toán tử ở phần sau bảo đảm lặp cập nhật hội tụ về $v_*$.

Khái niệm liên quan: giá trị hành động và Bellman tối ưu; Sutton–Barto, §3.5–3.6, tr. 58–65.

::: exercise Câu hỏi:
Vẫn với mô hình hai trạng thái, $\gamma = 0{,}5$, bảng $V = (4,7)$ và bảng $Q_V$ với ô $s_0$: $a$ cho 4, $b$ cho 2,5; ô $s_1$: $a$ cho 7, $b$ cho 13,5. Tính $T_* V$ và kết luận bảng $V$ đã phải giá trị tối ưu hay chưa. Ngoài ra, chính sách tham lam dựng theo bảng $Q_V$ này có được kết luận tối ưu ngay không?
:::

::: hint
Cực đại được lấy theo hành động trong từng hàng của bảng $Q_V$. Điểm bất động đòi hỏi toàn bảng không đổi. Hành động đạt cực đại theo bảng $Q_V$ hiện có chỉ là hành động tốt nhất theo bảng đang xét, chưa phải chứng nhận tối ưu của chính sách tham lam.
:::

::: solution
Từng hàng: $(T_* V)(s_0) = \max\{4,\ 2{,}5\} = 4$; $(T_* V)(s_1) = \max\{7,\ 13{,}5\} = 13{,}5$. Vậy $T_* V = (4,\ 13{,}5)$, khác với $(4,7)$, nên $V$ chưa phải $v_*$ vì chưa là điểm bất động của $T_*$. Điểm bất động đòi hỏi $T_* V = V$ trên cả hai thành phần; thành phần $s_1$ đã sai lệch $13{,}5 - 7 = 6{,}5$.

Về chính sách tham lam: theo bảng $Q_V$, hành động được chọn là $a$ tại $s_0$ và $b$ tại $s_1$, tức chính sách $(a,b)$. Đây chỉ là hành động tốt nhất theo chính bảng $V = (4,7)$ đang có, mà $V$ chưa phải $v_*$, nên chưa được kết luận chính sách này tối ưu; tính tối ưu phải được kiểm chứng thêm. Phần 4 sẽ đánh giá lại chính sách này, còn phần 6 chứng minh điều kiện đủ khi biết đúng $q_*$.
:::

<!-- note-topic-id: lec-04-part-03 -->

## 3. Đánh giá giá trị của một chính sách cố định

### Giá trị dài hạn của $\pi_0=(a,a)$

Giữ nguyên mô hình hai trạng thái với $\gamma=0{,}5$ và bộ chuyển xác định đã thống nhất: $s_0\xrightarrow{a}s_0$ thưởng $2$, $s_0\xrightarrow{b}s_1$ thưởng $-1$, $s_1\xrightarrow{a}s_0$ thưởng $5$, $s_1\xrightarrow{b}s_1$ thưởng $10$. Xét chính sách $\pi_0$ chọn hành động $a$ ở cả hai trạng thái. Vì $\pi_0$ cố định, tại mỗi trạng thái chỉ còn một hành động, nên kỳ vọng trên hành động biến mất và mỗi trạng thái cho đúng một phương trình Bellman: giá trị hiện tại bằng phần thưởng ngay cộng $\gamma$ nhân giá trị của trạng thái kế. Phần thưởng tương lai bị nhân $\gamma$ mỗi bước nên đóng góp của nó giảm dần theo cấp số nhân; chính sự giảm dần này khiến hệ phương trình có nghiệm hữu hạn và duy nhất.

### Hai phương trình Bellman và nghiệm chính xác

Đặt $x=v_{\pi_0}(s_0)$, $y=v_{\pi_0}(s_1)$. Theo các cạnh của mô hình:

$$x = 2 + 0{,}5\,x, \qquad y = 5 + 0{,}5\,x.$$

Phương trình thứ nhất chỉ chứa $x$ vì từ $s_0$ theo $a$ quá trình quay về chính $s_0$. Chuyển $0{,}5x$ sang vế trái: $x(1-0{,}5)=2$, tức $x=4$; đây là tổng cấp số nhân $2+0{,}5\cdot2+0{,}5^2\cdot2+\cdots$ với công bội $0{,}5$. Phương trình thứ hai dùng đúng cạnh $s_1\xrightarrow{a}s_0$, nên thay $x=4$: $y=5+0{,}5\cdot4=7$. Giá trị tiếp diễn là $x$ vì trạng thái kế tiếp là $s_0$; thay bằng $y$ sẽ tương ứng với một chuyển tiếp khác. Vậy

$$v_{\pi_0}=(4,\;7).$$

Cặp $(4,7)$ là nghiệm chính xác của hệ và sẽ là chuẩn đối chiếu cho phép đánh giá lặp từ bảng $0$.

### Dạng ma trận và tính khả nghịch

Với quá trình quyết định Markov và chính sách Markov dừng $\pi$, gọi $P_\pi$ là ma trận chuyển giữa các trạng thái chưa kết thúc, cỡ $n\times n$, với $s_i,s_j\in\mathcal S$ và

$$(P_\pi)_{ij}=\sum_a \pi(a\mid s_i)\sum_r p(s_j,r\mid s_i,a),$$

và $r_\pi$ là vectơ phần thưởng kỳ vọng cỡ $n$:

$$r_\pi(s_i)=\sum_a \pi(a\mid s_i)\sum_{s'\in\mathcal S^+,r}p(s',r\mid s_i,a)\,r.$$

Khi $\pi$ xác định, $\pi(a\mid s_i)=1$ đúng trên $a=\pi(s_i)$, nên hai công thức rút gọn về $(P_\pi)_{ij}=\sum_r p(s_j,r\mid s_i,\pi(s_i))$ và $r_\pi(s_i)$ là phần thưởng kỳ vọng của hành động $\pi(s_i)$. Phương trình Bellman viết gọn là

$$V = r_\pi + \gamma P_\pi V \quad\Longleftrightarrow\quad (I-\gamma P_\pi)V = r_\pi.$$

$I$ là ma trận đơn vị cỡ $n\times n$. Trong ví dụ này $n=2$, $P_{\pi_0}=\begin{pmatrix}1&0\\1&0\end{pmatrix}$, $r_{\pi_0}=(2,5)$, và hệ $(I-0{,}5P_{\pi_0})V=r_{\pi_0}$ chính là hai phương trình trên. Ma trận $I-\gamma P_\pi$ luôn khả nghịch khi $0\le\gamma<1$. Chứng minh bằng không gian nghiệm: giả sử $(I-\gamma P_\pi)U=0$, tức $U=\gamma P_\pi U$. Đặt $\Delta=\max_i\lvert U_i\rvert$. Theo từng thành phần, $\lvert U_i\rvert=\gamma\lvert\sum_j (P_\pi)_{ij}U_j\rvert\le\gamma\sum_j(P_\pi)_{ij}\Delta\le\gamma\Delta$, vì các phần tử của $P_\pi$ không âm và tổng mỗi hàng không vượt $1$. Phần xác suất thiếu, nếu có, là xác suất chuyển vào trạng thái kết thúc. Lấy cực đại theo $i$: $\Delta\le\gamma\Delta$, mà $\gamma<1$, nên $\Delta=0$, tức $U=0$. Nghiệm của hệ thuần nhất chỉ có nghiệm không, nên ma trận vuông $I-\gamma P_\pi$ đơn ánh, do đó khả nghịch; hệ $(I-\gamma P_\pi)V=r_\pi$ có nghiệm duy nhất $V=v_\pi=(I-\gamma P_\pi)^{-1}r_\pi$.

### Xấp xỉ bằng các lượt quét đồng bộ

Đánh giá lặp áp dụng toán tử $T_{\pi_0}$ từ bảng khởi tạo $V_0=(0,0)$, cập nhật đồng bộ: mọi trạng thái đều đọc giá trị từ bảng cũ $V_k$.

| Bảng | $V_0$ | $V_1$ | $V_2$ | $v_{\pi_0}$ |
|---|---|---|---|---|
| $s_0$ | $0$ | $2$ | $3$ | $4$ |
| $s_1$ | $0$ | $5$ | $6$ | $7$ |

Lượt một: $V_1(s_0)=2+0{,}5\cdot0=2$, $V_1(s_1)=5+0{,}5\cdot0=5$. Lượt hai: $V_2(s_0)=2+0{,}5\cdot2=3$, và $V_2(s_1)=5+0{,}5\cdot V_1(s_0)=5+0{,}5\cdot2=6$. Ba đại lượng trong phép tính là thưởng tức thời $5$, giá trị cũ $V_1(s_0)=2$ lấy từ bảng trước, và giá trị mới $6$. Dãy $(0,0)\to(2,5)\to(3,6)\to(3{,}5,6{,}5)\to\cdots$ tiến dần về $(4,7)$; sai số mới bị chặn bởi $\gamma$ nhân sai số cũ sau mỗi lần áp dụng $T_{\pi_0}$.

![Mô hình theo chính sách luôn chọn a: s0 nhận thưởng 2 và trở về s0; s1 nhận thưởng 5 và chuyển về s0.](img/lec-04/policy-evaluation.svg)

### Hai lịch cập nhật: đồng bộ và tại chỗ

Cùng xuất phát từ $V_0=(0,0)$, hai lịch cho kết quả khác nhau ngay lượt đầu. Đồng bộ: cả hai trạng thái đọc bảng cũ, phép tính tại $s_1$ dùng $V_0(s_0)=0$ nên cho $5$, cho $V_1=(2,5)$. Tại chỗ, theo thứ tự $s_0$ rồi $s_1$: cập nhật $s_0$ trước được $2$, rồi $s_1$ đọc ngay giá trị mới đó, nhận $5+0{,}5\cdot2=6$, cho bảng $V=(2,6)$. Khác biệt một đơn vị đến hoàn toàn từ ô nguồn được dùng. Tại chỗ cho phép thông tin mới lan truyền trong cùng lượt, nhưng tốc độ hội tụ phụ thuộc vào mô hình và thứ tự cập nhật, không có bảo đảm chung rằng nó nhanh hơn đồng bộ. Điều bắt buộc với cả hai lịch: mỗi cập nhật dùng đúng phương trình Bellman với bảng hiện có, và mỗi trạng thái được cập nhật vô hạn lần; nếu một trạng thái bị bỏ qua mãi thì không còn bảo đảm hội tụ. Lịch cập nhật vô hạn lần mỗi trạng thái chỉ là lịch lý thuyết; với ngân sách lượt hữu hạn trong thực hành, kết quả trả về khác đi và phải được xử lý riêng.

### Quy trình đánh giá chính sách

Đầu vào gồm mô hình $p(s',r\mid s,a)$, chính sách $\pi$ cố định, $0\le\gamma<1$, ngưỡng phần dư $\eta>0$ và ngân sách $K$ là số nguyên không âm. $K$ đếm số lần nhận bảng mới, không đếm riêng các phép tính dùng để kiểm phần dư.

1. Khởi tạo $V=0$, bộ đếm $k=0$; giữ giá trị trạng thái kết thúc bằng $0$.
2. Tính đồng bộ $W=T_\pi V$ từ bảng $V$ cố định; đo $\Delta=\lVert W-V\rVert_\infty=\Delta_\pi(V)$.
3. Nếu $\Delta\le\eta$, trả $(V,\Delta)$ với nhãn *đạt ngưỡng*. Nếu $k=K$ mà $\Delta>\eta$, trả $(V,\Delta)$ với nhãn *hết ngân sách, chưa đạt ngưỡng*.
4. Nếu $\Delta>\eta$ và $k<K$, nhận $V\leftarrow W$, tăng $k\leftarrow k+1$ rồi lặp từ bước 2.

Sau lần nhận bảng thứ $K$, bước 2 áp dụng $T_\pi$ thêm một lần để đo phần dư của chính bảng cuối. Với $K=0$, thuật toán kiểm và trả bảng khởi tạo. Mọi nhánh dừng đều trả $V$ đã đo phần dư; $W$ là bảng tạm dùng cho phép kiểm. Sai số của bảng trả được chặn bởi $\lVert V-v_\pi\rVert_\infty\le \Delta_\pi(V)/(1-\gamma)$, chứng minh ở phần 6. Nhãn hết ngân sách không chứng nhận sai số mong muốn.

Cập nhật dùng giá trị tiếp nối ước lượng để xây mục tiêu mới; cơ chế này được gọi là bootstrapping. Hội tụ của dãy đánh giá dùng các giả thiết đã nêu, trong đó $\gamma<1$; ngân sách hữu hạn chỉ giới hạn số bảng được nhận. Với $n$ trạng thái, nhiều nhất $m$ hành động mỗi trạng thái và mô hình chuyển đặc, mỗi phép áp dụng $T_\pi$ cho chính sách ngẫu nhiên tốn $O(n^2m)$ phép tính khi đã gộp phần thưởng kỳ vọng hoặc số kết quả thưởng trên mỗi nhánh bị chặn. Thuật toán nhận tối đa $K$ bảng mới và dùng tối đa $K+1$ phép áp dụng toán tử, kể cả kiểm phần dư cuối.

::: exercise Câu hỏi:
Cho $\pi_0=(a,a)$, $V_2=(3,6)$, $\gamma=0{,}5$. Tính $V_3=T_{\pi_0}V_2$ theo cập nhật đồng bộ. Vì sao phép cập nhật không có $\max$? Nếu đổi sang lịch tại chỗ với thứ tự $s_0$ rồi $s_1$, kết quả lượt này có đổi không?
:::

::: hint
Viết công thức Bellman cho từng trạng thái trước khi thay số, với trạng thái kế tiếp $s_0$ ở cả hai phương trình theo $\pi_0$. Cập nhật đồng bộ đọc toàn bộ từ $V_2$.
:::

::: solution
Cùng hành động $a$ ở cả hai trạng thái, nên $V_3(s_0)=2+0{,}5\cdot V_2(s_0)=2+1{,}5=3{,}5$ và $V_3(s_1)=5+0{,}5\cdot V_2(s_0)=5+1{,}5=6{,}5$; cả hai dòng đều đọc giá trị của $s_0$ vì đó là trạng thái kế theo chính sách. Vậy $V_3=(3{,}5,\;6{,}5)$. Khoảng cách tới nghiệm $(4,7)$ đúng bằng một nửa khoảng cách của $V_2$, tức $(0{,}5,\;0{,}5)$, phù hợp tính co của $T_{\pi_0}$ với $\gamma=0{,}5$. Không có $\max$ vì $T_\pi$ đánh giá một chính sách đã cho: $\pi_0$ xác định duy nhất hành động $a$ tại mỗi trạng thái, nên phép cập nhật chỉ lấy kỳ vọng theo chính sách; phép $\max$ xuất hiện khi tối ưu theo hành động. Với lịch tại chỗ, thứ tự $s_0$ rồi $s_1$: $s_0$ vẫn cho $3{,}5$ (đọc $V_2(s_0)=3$), rồi $s_1$ đọc giá trị vừa cập nhật $3{,}5$ thay vì $3$, nhận $5+0{,}5\cdot3{,}5=6{,}75$. Vậy kết quả lượt này đổi thành $(3{,}5,\;6{,}75)$, do phép tính tại $s_1$ dùng giá trị vừa cập nhật.
:::

Thuật toán liên quan: đánh giá chính sách; Sutton–Barto, §4.1, tr. 74–76.

<!-- note-topic-id: lec-04-part-04 -->

## 4. Cải thiện chính sách và lặp chính sách

### Cải thiện hành động tại $s_1$

Bảng $v_{\pi_0}=(4,7)$ chưa nói $\pi_0$ là tốt nhất. Tại $s_1$, nếu buộc chọn $b$ đúng một lần rồi quay về theo $\pi_0$, kỳ vọng là

$$q_{\pi_0}(s_1,b)=10+0{,}5\cdot7=13{,}5>7=v_{\pi_0}(s_1).$$

Hai giá trị tương ứng với hai quy trình: $7$ là giá trị của chính sách $\pi_0$, còn $13{,}5$ là giá trị khi buộc chọn $b$ một lần rồi tiếp tục theo $\pi_0$. Sai lầm thường gặp là coi $13{,}5$ là giá trị của chính sách mới. Chính sách mới $\pi_1$ chọn $b$ tại mọi lần đến $s_1$, nên đường đi của nó khác hẳn đường đi "một lần rồi quay về"; giá trị của $\pi_1$ tại $s_1$ là $20$ và phải được đánh giá riêng theo mô hình của $\pi_1$.

### Cải thiện bằng phép nhìn trước một bước

Tính $q_{\pi_0}$ tại cả hai trạng thái:

| | $a$ | $b$ |
|---|---|---|
| $s_0$ | $4$ (chọn) | $2{,}5$ |
| $s_1$ | $7$ | $13{,}5$ (chọn) |

Mỗi hàng được xét độc lập: tại $s_0$, $4>2{,}5$ nên giữ $a$; tại $s_1$, $13{,}5>7$ nên đổi sang $b$. Kết quả $\pi_0\to\pi_1=(a,b)$. Các số trong bảng là giá trị của hành động một lần rồi tiếp tục theo $\pi_0$, nên phần tiếp diễn vẫn theo $\pi_0$; giá trị của $\pi_1$ chưa được tính và phải tính lại từ đầu theo mô hình của $\pi_1$.

### Đánh giá lại $\pi_1$ và $\pi_2$

Với $\pi_1=(a,b)$, hệ Bellman là $x=2+0{,}5x$ (vì $s_0$ vẫn về $s_0$) cho $x=4$, và $y=10+0{,}5y$ (vì $s_1$ về chính nó) cho $y=20$; vậy $v_{\pi_1}=(4,20)$. Bước cải thiện tiếp theo so sánh trên bảng $v_{\pi_1}$: tại $s_0$, $q_{\pi_1}(s_0,b)=-1+0{,}5\cdot20=9>4=q_{\pi_1}(s_0,a)$, nên $\pi_2=(b,b)$. Đánh giá $\pi_2$: $y=10+0{,}5y=20$ và $x=-1+0{,}5\cdot20=9$, vậy $v_{\pi_2}=(9,20)$.

| Chính sách $\pi$ | $v_\pi(s_0)$ | $v_\pi(s_1)$ |
|---|---|---|
| $\pi_0=(a,a)$ | $4$ | $7$ |
| $\pi_1=(a,b)$ | $4$ | $20$ |
| $\pi_2=(b,b)$ | $9$ | $20$ |

Các giá trị giữ nguyên là đặc thù của ví dụ này, không phải quy luật chung. Từ $\pi_0$ sang $\pi_1$, tại $s_0$ hành động luôn là $a$ nên trạng thái tự vòng về chính nó, và mọi đường đi từ $s_0$ không bao giờ đến trạng thái đã đổi hành động $s_1$, nên $v_\pi(s_0)$ giữ nguyên $4$. Từ $\pi_1$ sang $\pi_2$, tại $s_1$ hành động luôn là $b$ nên trạng thái tự vòng về chính nó, và mọi đường đi từ $s_1$ không bao giờ đến trạng thái đã đổi hành động $s_0$, nên $v_\pi(s_1)$ giữ nguyên $20$. Nếu đường đi có thể đi qua trạng thái đã đổi hành động, kết luận này không còn đúng.

### Quy tắc tham lam với điều khoản giữ hòa

Quy tắc cải thiện cần phát biểu chặt để thuật toán tái lập được. Với $\pi$ xác định và bảng $v_\pi$, đặt

$$\pi'(s)\in\operatorname{argmax}_a Q_{v_\pi}(s,a),$$

kèm quy tắc hòa: nếu hành động cũ của $\pi$ thuộc argmax thì giữ hành động cũ; nếu không, chọn theo thứ tự cố định của tập hành động. Mọi so sánh dùng $v_\pi$ cũ, chưa cập nhật. Với $q_{\pi_0}$: tại $s_1$, $b$ thuộc argmax nên được chọn, còn hành động cũ $a$ không thuộc. Khi hai hành động đồng hạng, giữ hành động cũ ngăn thuật toán đổi qua lại giữa các chính sách tương đương qua các vòng lặp; nếu không có quy tắc này, không thể kết luận nghiêm ngặt rằng thuật toán không dao động vô hạn giữa các hành động bằng giá trị.

Trước khi chứng minh định lý, cần tính đơn điệu của toán tử: nếu $U\le V$ theo từng trạng thái thì $Q_U(s,a)\le Q_V(s,a)$ cho mọi $s,a$, vì $\gamma\ge0$ và các xác suất chuyển không âm; do đó $T_{\pi'}U\le T_{\pi'}V$ với mọi chính sách $\pi'$. Định lý cải thiện sử dụng tính đơn điệu này để truyền bất đẳng thức qua các lần cập nhật.

### Định lý cải thiện chính sách

**Định lý.** Giả sử quá trình quyết định Markov hữu hạn, thưởng bị chặn, $0\le\gamma<1$; $\pi$ và $\pi'$ là chính sách Markov dừng xác định, và $\pi'$ tham lam theo $v_\pi$ với quy tắc giữ hòa. Khi đó $v_\pi\le v_{\pi'}$ theo từng trạng thái; nếu $\pi'$ khác $\pi$ thì tăng nghiêm ngặt ở ít nhất một trạng thái.

::: proof
Vì $\pi'$ chọn một hành động cực đại của $Q_{v_\pi}$,

$$T_{\pi'}v_\pi=\max_a Q_{v_\pi}(\cdot,a)\ge T_\pi v_\pi=v_\pi,$$

bất đẳng thức đúng vì hành động $\pi(s)$ là một ứng viên trong phép max tại mỗi trạng thái. Xét một trạng thái $s$ nơi $\pi'(s)\ne\pi(s)$: theo quy tắc giữ hòa, hành động cũ $\pi(s)$ không thuộc argmax, nên

$$(T_{\pi'}v_\pi)(s)=Q_{v_\pi}(s,\pi'(s))>Q_{v_\pi}(s,\pi(s))=(T_\pi v_\pi)(s)=v_\pi(s),$$

bất đẳng thức nghiêm ngặt tại $s$. Áp dụng $T_{\pi'}$ lặp lại và dùng tính đơn điệu vừa thiết lập:

$$v_\pi\le T_{\pi'}v_\pi\le (T_{\pi'})^2v_\pi\le\cdots$$

Sau $N$ bước, tại mỗi trạng thái đầu $s$,

$$((T_{\pi'})^Nv_\pi)(s)=\mathbb E_{\pi'}\!\left[\sum_{t=0}^{N-1}\gamma^t R_{t+1}+\gamma^N v_\pi(S_N)\,\middle|\,S_0=s\right].$$

Chọn $R_{\max}$ sao cho $|R|\le R_{\max}$. Với chuẩn $\lVert V\rVert_\infty=\max_s|V(s)|$, $\lVert v_\pi\rVert_\infty\le R_{\max}/(1-\gamma)$, nên hạng đuôi có chuẩn không vượt $\gamma^N R_{\max}/(1-\gamma)$ và tiến về $0$ vì $0\le\gamma<1$. Do đó dãy hội tụ về $v_{\pi'}$, và chuyển qua giới hạn trong chuỗi bất đẳng thức cho $v_\pi\le v_{\pi'}$; tại mỗi trạng thái đã đổi hành động $s$, dùng khoảng cách nghiêm ngặt ở bước đầu đã thiết lập ở trên, $v_{\pi'}(s)\ge (T_{\pi'}v_\pi)(s) > v_\pi(s)$.
:::

Hệ quả về tính nghiêm ngặt: khi $\pi'$ khác $\pi$, có ít nhất một trạng thái tăng giá trị nghiêm ngặt. Kết hợp với tính đơn điệu, mỗi lần đổi chính sách làm giá trị tăng nghiêm ngặt ở ít nhất một trạng thái, nên trong dãy chính sách của lặp chính sách không có chính sách nào lặp lại: nếu $\pi_j=\pi_i$ với $i<j$ thì $v_{\pi_i}\le v_{\pi_{i+1}}\le\cdots\le v_{\pi_j}=v_{\pi_i}$ buộc mọi bước giữa đều giữ nguyên giá trị, mâu thuẫn với tăng nghiêm ngặt. Không gian các chính sách xác định hữu hạn, cỡ $\prod_s\lvert\mathcal A(s)\rvert$ (trong ví dụ là $2\cdot2=4$), nên thuật toán dừng sau hữu hạn vòng. Khi dừng với $\pi'=\pi$, $T_*v_\pi=v_\pi$, tức thỏa phương trình tối ưu Bellman; chứng minh rằng giá trị này là tối ưu toàn cục sẽ ở Phần 6.

### Quy trình lặp chính sách

Thuật toán ghép hai khối đánh giá và cải thiện:

- **Đầu vào:** mô hình; ngân sách vòng lặp $I_{\max}\ge1$; khởi tạo $\pi$ xác định.
- **Đánh giá chính xác:** giải $(I-\gamma P_\pi)V=r_\pi$ để thu được $V=v_\pi$, trong đó $I$ là ma trận đơn vị cỡ $n\times n$, $P_\pi$ là ma trận chuyển của $\pi$, $r_\pi$ là vectơ phần thưởng kỳ vọng.
- **Cải thiện:** tính $Q_{v_\pi}$ rồi chọn hành động tham lam theo bảng này, giữ hòa theo quy tắc đã nêu, được $\pi'$.
- **Dừng:** nếu $\pi'=\pi$, trả $\pi$ và $v_\pi$. Nếu hết $I_{\max}$ vòng, trả $\pi$ cùng $v_\pi$ với nhãn *chưa chứng nhận*; còn lại đặt $\pi=\pi'$ và lặp.

Quy trình này đánh giá chính xác ở từng vòng. Khi hết ngân sách mà bước cải thiện vẫn đổi hành động, đầu ra là chính sách vừa được đánh giá và giá trị của chính sách đó. Chính sách $\pi'$ chưa đánh giá phải được ghép với giá trị riêng sau một bước đánh giá tiếp theo. Giải hệ tuyến tính đặc cỡ $n$ có chi phí $O(n^3)$. Định lý cải thiện và lập luận hữu hạn ở trên giải thích vì sao dừng khi chính sách ổn định: với $\pi_2$, hành động $a$ cho $6{,}5$ tại $s_0$ và $9{,}5$ tại $s_1$, đều thấp hơn $9$ và $20$ của $b$, nên bước cải thiện giữ $\pi_2$. Bảo đảm dừng hữu hạn dựa trên đánh giá chính xác và quy tắc hòa, không suy rộng sang đánh giá bị cắt ngắn.

::: exercise Câu hỏi:
Cho $v_{\pi_1}=(4,20)$. Hai giá trị $Q$ tại $s_0$ là gì? Chính sách sau cải thiện $\pi_2$ là gì? Vì sao cần giữ hành động cũ khi hai hành động hòa nhau?
:::

::: hint
Dùng bảng $v_{\pi_1}$ vừa đánh giá, chưa cập nhật, để tính $q_{\pi_1}(s_0,a)$ và $q_{\pi_1}(s_0,b)$ theo đúng cạnh chuyển và thưởng của mô hình.
:::

::: solution
Hành động $a$ từ $s_0$ về $s_0$ với thưởng $2$: $q_{\pi_1}(s_0,a)=2+0{,}5\cdot4=4$. Hành động $b$ từ $s_0$ đến $s_1$ với thưởng $-1$: $q_{\pi_1}(s_0,b)=-1+0{,}5\cdot20=9$. Vì $9>4$, chính sách sau cải thiện là $\pi_2=(b,b)$. Định lý cải thiện cho $v_{\pi_2}=(9,20)\ge(4,20)=v_{\pi_1}$, tăng nghiêm ngặt đúng tại $s_0$ và giữ nguyên tại $s_1$; điều này không có nghĩa rằng cải thiện nghiêm ngặt tại mọi trạng thái. Mọi so sánh trên đều dùng $v_{\pi_1}$ cũ, chưa cập nhật. Về tiêu chí hòa: khi hai hành động đồng hạng, giữ hành động cũ ngăn thuật toán dao động giữa các chính sách tương đương qua các vòng lặp; nếu chọn tùy ý hành động đồng hạng, thuật toán có thể luân phiên giữa các chính sách có cùng giá trị mà không bao giờ dừng, nên quy tắc giữ hòa bảo đảm thuật toán tránh cách đổi chính sách này.
:::

Thuật toán liên quan: cải thiện và lặp chính sách; Sutton–Barto, §4.2–4.3, tr. 76–82. Quy tắc giữ hòa gắn với Bài tập 4.4.

<!-- note-topic-id: lec-04-part-05 -->

## 5. Lặp giá trị

### Chi phí đánh giá từng chính sách

Lặp chính sách gồm hai giai đoạn tách bạch: với chính sách $\pi$ hiện tại, giải hệ tuyến tính để có $v_\pi$, rồi tại mỗi trạng thái so sánh các hành động qua $Q_{v_\pi}(s,a)$ để cải thiện $\pi$. Việc giải đầy đủ hệ tuyến tính ở mỗi vòng có thể tốn kém khi số trạng thái lớn. Lặp giá trị chọn hướng khác: tại mỗi trạng thái, nhìn trước một bước trên bảng giá trị đang có, lấy kỳ vọng thưởng ngay cộng hệ số chiết khấu nhân giá trị bảng cũ, rồi lấy cực đại theo hành động. Nhờ vậy không cần hoàn thành đánh giá đầy đủ của một chính sách nào trước khi cải thiện; cực đại theo hành động đã gộp việc so sánh vào mỗi lượt cập nhật.

Lưới năm ô $c_1,\dots,c_5$ đủ nhỏ để tính tay toàn bộ. Quy ước dữ kiện: $\gamma=0{,}5$; bước thường thưởng $-1$ vì mỗi bước đi tốn một đơn vị; riêng chuyển $c_4\to c_5$ thưởng $24$; đi trái ở $c_1$ thì đứng nguyên tại chỗ và vẫn mất $-1$, nên hành động này vẫn chịu chi phí bước đi; $c_5$ là trạng thái kết thúc, sau khi vào đích quá trình dừng và không nhận thêm thưởng, do đó $V(c_5)=v_*(c_5)=0$.

![Lưới năm ô: thưởng −1 cho bước thường, thưởng 24 khi từ c4 vào đích c5; đi trái từ c1 giữ nguyên ô, giá trị đích bằng 0.](img/lec-04/gridworld.svg)

### Một lượt quét đầu tiên

Bảng khởi tạo là $V_0$ toàn số 0. Một lượt quét đồng bộ nghĩa là mọi trạng thái đều tính từ bảng cũ $V_0$, không dùng giá trị vừa cập nhật trong cùng lượt.

| Ô | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| $V_0$ | 0 | 0 | 0 | 0 | 0 |
| $V_1$ | $-1$ | $-1$ | $-1$ | 24 | 0 |

Tại $c_4$: đi phải nhận ngay $24$ cộng $\gamma$ nhân giá trị $c_5$ trong bảng cũ, tức $24+0{,}5\cdot 0=24$; đi trái chỉ được $-1$, nên cực đại là $24$. Ba ô còn lại không kề đích: mọi hành động đều dẫn tới ô có giá trị $0$ trong $V_0$, nên chúng chỉ ghi nhận chi phí bước đi $-1$. Giá trị tại ba ô này chưa phản ánh phần thưởng vào đích; ảnh hưởng của phần thưởng $24$ được truyền tới chúng qua các lượt quét tiếp theo.

Cơ chế liên quan: cập nhật đồng bộ bằng toán tử Bellman tối ưu; Sutton–Barto, §4.4, công thức (4.10).

### Giá trị lan dần từ đích

Ở lượt $k$, ảnh hưởng của phần thưởng $24$ lùi thêm một ô về phía trái.

| $k$ | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | $-1$ | $-1$ | $-1$ | 24 | 0 |
| 2 | $-1{,}5$ | $-1{,}5$ | 11 | 24 | 0 |
| 3 | $-1{,}75$ | $4{,}5$ | 11 | 24 | 0 |
| 4 | $1{,}25$ | $4{,}5$ | 11 | 24 | 0 |
| 5 | $1{,}25$ | $4{,}5$ | 11 | 24 | 0 |

Các phép tính mẫu, luôn dùng bảng của lượt trước:

- $V_2(c_3)=-1+0{,}5\cdot 24=11$: lượt 2 dùng $V_1(c_4)=24$.
- $V_3(c_2)=-1+0{,}5\cdot 11=4{,}5$: lượt 3 dùng $V_2(c_3)=11$.
- $V_4(c_1)=-1+0{,}5\cdot 4{,}5=1{,}25$: lượt 4 dùng $V_3(c_2)=4{,}5$.

Lượt 5 dùng bảng $V_4$. Tại $c_1$: đi trái tự khép, đọc $V_4(c_1)=1{,}25$, cho $-1+0{,}5\cdot 1{,}25=-0{,}375$; đi phải đọc $V_4(c_2)=4{,}5$, cho $-1+0{,}5\cdot 4{,}5=1{,}25$. Cực đại vẫn là $1{,}25$. Các ô còn lại cũng không đổi, nên $V_5=V_4$. Với bộ số và khởi tạo bằng không này, phép kiểm trực tiếp $V_5=V_4$ xác nhận điểm bất động sau bốn lượt. Các đường đi tối ưu đến $c_5$ trong nhiều nhất bốn bước. Tính chất dừng chính xác sau hữu hạn lượt không suy rộng sang mọi mô hình hoặc mọi khởi tạo. Công thức tổng quát ở dưới giữ cùng chỉ số lượt và cùng quy ước dùng bảng cũ.

### Quy tắc lặp giá trị

$$
V_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)\,\bigl[r+\gamma V_k(s')\bigr]
$$

Công thức khái quát đúng phép tính tay trên lưới: tại mỗi trạng thái, xét mọi hành động, lấy kỳ vọng của thưởng ngay cộng $\gamma$ nhân giá trị bảng cũ, rồi lấy cực đại. Đối chiếu: $V_2(c_3)$ dùng $V_1$, đi phải cho $-1+0{,}5\cdot 24=11$, đi trái cho $-1+0{,}5\cdot(-1)=-1{,}5$, nên $V_2(c_3)=\max\{-1{,}5,\,11\}=11$.

Chỉ số $k$ đếm lượt quét trên mô hình; mỗi lượt tính lại toàn bộ bảng trạng thái. Chỉ số thời gian tương tác là $t$. Với $V_0=0$, có thể diễn giải $V_k$ là giá trị tối ưu khi còn đúng $k$ quyết định và giá trị cuối bằng 0; với khởi tạo khác, diễn giải này chỉ đúng nếu nói rõ thưởng cuối. $V_k$ không nhất thiết bằng giá trị dài hạn của một chính sách dừng nào.

Thuật toán liên quan: lặp giá trị; Sutton–Barto, §4.4, tr. 82–84.

### Quy trình lặp giá trị có kiểm tra dừng

Đầu vào gồm mô hình $p(s',r\mid s,a)$, $0\le\gamma<1$, ngưỡng phần dư $\eta>0$ và ngân sách $K$ là số nguyên không âm. Khởi tạo $V=0$, bộ đếm $k=0$; trạng thái kết thúc luôn giữ giá trị $0$. $K$ đếm số lần nhận bảng mới, cùng quy ước với đánh giá chính sách.

1. Tính $Q_V(s,a)$ cho mọi cặp trạng thái chưa kết thúc–hành động từ cùng bảng $V$ cố định.
2. Đặt $W(s)=\max_a Q_V(s,a)$ và $\pi_V(s)\in\arg\max_a Q_V(s,a)$, phá hòa theo thứ tự cố định.
3. Đo $\Delta=\lVert W-V\rVert_\infty=\Delta_*(V)$. Nếu $\Delta\le\eta$, trả $(V,\pi_V,\Delta)$ với nhãn *đạt ngưỡng*. Nếu $k=K$ mà $\Delta>\eta$, trả cùng bộ ba với nhãn *hết ngân sách, chưa đạt ngưỡng*.
4. Nếu $\Delta>\eta$ và $k<K$, nhận $V\leftarrow W$, tăng $k\leftarrow k+1$ rồi lặp từ bước 1.

Sau lần nhận bảng thứ $K$, thuật toán tính lại $Q_V$, $\pi_V$ và $\Delta_*(V)$ từ chính bảng cuối trước khi trả. Với $K=0$, bảng khởi tạo được kiểm và dùng để trích chính sách. Bảng $W$ chỉ phục vụ phép kiểm hiện tại hoặc được nhận ở bước 4; phần dư vừa đo thuộc $V$. Như vậy bảng công bố, chính sách trích và phần dư luôn cùng dùng một $V$. Mỗi bảng $Q_V$ phục vụ cả cập nhật dự kiến, trích chính sách và kiểm phần dư. Ngưỡng $\eta$ áp dụng cho phần dư; phần 6 thiết lập chặn sai số giá trị từ phần dư này. Thuật toán dùng tối đa $K+1$ phép áp dụng toán tử, kể cả phép kiểm cuối, và nhận tối đa $K$ bảng mới.

### Trích chính sách từ cùng bảng giá trị

$$
\pi_V(s)\in\arg\max_a Q_V(s,a),\qquad T_{\pi_V}V=T_*V
$$

Cùng một bảng $V_1=(-1,-1,-1,24,0)$ cấp dữ liệu cho hai nhánh. Nhánh tính giá trị nhìn trước: tại $c_3$, đi trái nhìn trước sang $c_2$ cho $-1+0{,}5\cdot(-1)=-1{,}5$; đi phải sang $c_4$ cho $-1+0{,}5\cdot 24=11$; chọn phải. Số $11$ chính là $Q_{V_1}(c_3,a_R)$ với $a_R$ là hành động đi phải; đây là phép nhìn trước một bước từ $V_1$, chưa phải giá trị thật của chính sách vừa trích. Nhánh phần dư cũng dùng $V_1$: so $W(s)$ với $V_1(s)$ trên toàn bảng, $\Delta_*(V_1)=\max_s\lvert W(s)-V_1(s)\rvert$.

Đồng nhất thức $T_{\pi_V}V=T_*V$ bảo đảm chính sách trích từ bảng $V$ chính là chính sách tham lam của phép cập nhật $T_*$: cực đại hóa theo hành động trong $T_*V$ và chọn $\pi_V$ từ $Q_V$ là cùng một phép tính. Trong quy trình, $V$ là bảng đang kiểm, $W$ là bảng cập nhật dự kiến và $\pi_V$ được trích từ $V$.

Khái niệm liên quan: chính sách tham lam theo bảng giá trị; Sutton–Barto, §4.2 và §4.4.

### Chi phí của một lượt tính

Đặt $n=\lvert\mathcal S\rvert$ và $m=\max_s\lvert\mathcal A(s)\rvert$.

| Phương pháp | Thao tác mỗi lượt | Chi phí |
|---|---|---|
| Lặp giá trị, mô hình đặc | Tính tổng theo trạng thái kế tiếp | $O(n^2m)$ |
| Lặp giá trị, mô hình thưa | Duyệt các nhánh có xác suất khác 0 | theo số nhánh |
| Lặp chính sách chính xác | Giải hệ đặc trong bước đánh giá | $O(n^3)$ mỗi lần giải |

Một lượt lặp giá trị duyệt $n$ trạng thái, tối đa $m$ hành động tại mỗi trạng thái và $n$ trạng thái kế tiếp, nên tốn $O(n^2m)$. Chặn này giả định đã lưu xác suất chuyển $p(s'\mid s,a)$ và thưởng kỳ vọng $r(s,a)$, hoặc số nhánh thưởng cho mỗi bộ $(s,a,s')$ bị chặn. Mô hình thưa chỉ cần duyệt các nhánh có xác suất khác $0$. Lặp chính sách chính xác tốn $O(n^3)$ để giải hệ đặc, rồi $O(n^2m)$ cho bước cải thiện.

Mô hình chuyển đặc cần $O(n^2m)$ bộ nhớ. Ngoài mô hình, các bảng giá trị và chính sách cần $O(n)$; lưu toàn bộ $Q_V(s,a)$ cần thêm $O(nm)$. Có thể tính lần lượt các hành động và chỉ giữ cực đại để giảm bộ nhớ phụ xuống $O(n)$. Chi phí mỗi lượt chưa cho biết tổng thời gian: còn phải tính số lượt cần thiết, vốn khác nhau giữa hai thuật toán.

Phân tích chi phí sử dụng cách đếm phép toán ở trên; đối chiếu phạm vi hiệu quả của quy hoạch động trong Sutton–Barto, §4.7, tr. 87–88.

::: exercise Câu hỏi:
Cho lưới năm ô với $\gamma=0{,}5$, bước thường thưởng $-1$, chuyển $c_4\to c_5$ thưởng $24$, đi trái ở $c_1$ đứng yên, $c_5$ kết thúc với giá trị 0. Bảng hiện tại là $V_2=(-1{,}5,\,-1{,}5,\,11,\,24,\,0)$.

(a) Tính $V_3(c_1)$ và $V_3(c_2)$ theo cập nhật đồng bộ, nêu rõ giá trị nhìn trước của mỗi hành động.

(b) Biết $V_4=(1{,}25,\,4{,}5,\,11,\,24,\,0)$, tính $\Delta_*(V_3)$.

(c) Ô $c_4$ không đổi qua hai lượt. Điều đó đã đủ kết luận toàn thuật toán hội tụ chưa? Vì sao?
:::

::: hint
Trong mỗi phép tính chỉ được dùng bảng $V_2$, kể cả khi $V_3(c_1)$ đã được tính. Phần dư là chuẩn vô cùng của hiệu hai bảng trên toàn bộ năm ô, không chỉ các ô thay đổi.
:::

::: solution
(a) Tại $c_1$, hai hành động: đi trái tự khép đọc $V_2(c_1)=-1{,}5$, cho $-1+0{,}5\cdot(-1{,}5)=-1{,}75$; đi phải sang $c_2$ đọc $V_2(c_2)=-1{,}5$, cho $-1+0{,}5\cdot(-1{,}5)=-1{,}75$. Cực đại là $-1{,}75$, nên $V_3(c_1)=-1{,}75$. Tại $c_2$: đi trái sang $c_1$ đọc $V_2(c_1)=-1{,}5$, cho $-1{,}75$; đi phải sang $c_3$ đọc $V_2(c_3)=11$, cho $-1+0{,}5\cdot 11=4{,}5$. Cực đại là $4{,}5$, vậy $V_3(c_2)=4{,}5$. Nếu dùng $V_3(c_1)=-1{,}75$ cho phép tính tại $c_2$ thì nhánh đi trái thành $-1+0{,}5\cdot(-1{,}75)=-1{,}875$, vẫn nhỏ hơn $4{,}5$ nên kết quả $V_3(c_2)$ không đổi. Phép tính đó vẫn vi phạm quy ước đồng bộ vì sử dụng giá trị mới trong cùng lượt.

(b) Vì $V_4=T_*V_3$, phần dư của $V_3$ là chuẩn vô cùng của hiệu hai bảng. Hiệu $V_4-V_3=(3,\,0,\,0,\,0,\,0)$, chỉ ô $c_1$ khác nhau, nên $\Delta_*(V_3)=\lVert V_4-V_3\rVert_\infty=3$.

(c) Chưa đủ. $c_4$ giữ 24 qua hai lượt, nhưng $c_1$ và $c_2$ vẫn thay đổi giữa $V_2$ và $V_3$; phần dư $\Delta_*(V_3)=3$ đo trên toàn bảng vẫn lớn. Đạt ngưỡng dừng phải kiểm phần dư trên toàn bộ bảng, không phải khi một ô riêng lẻ ổn định; còn hội tụ là tính chất của cả dãy giá trị, không kết luận được từ một lượt.
:::

<!-- note-topic-id: lec-04-part-06 -->

## 6. Tính co của toán tử Bellman và các bảo đảm hội tụ

### Chuẩn vô cùng và khoảng cách giữa hai bảng giá trị

Khoảng cách giữa hai bảng giá trị được đo bằng độ chênh lệch lớn nhất trên các trạng thái. Với không gian giá trị $\mathcal V=\mathbb R^n$, mỗi bảng là một vectơ gồm $n=|\mathcal S|$ thành phần, chuẩn được dùng là chuẩn vô cùng:

$$\lVert U-V\rVert_\infty=\max_{s\in\mathcal S}\lvert U(s)-V(s)\rvert.$$

Hai bảng $U$ và $V$ ở đây không cần là giá trị của chính sách nào; chúng chỉ là hai bảng số bất kỳ. Xét MDP hai trạng thái với $\gamma=0{,}5$ và bộ số của ghi chú: $s_0,a$ trả $2$ về $s_0$; $s_0,b$ trả $-1$ về $s_1$; $s_1,a$ trả $5$ về $s_0$; $s_1,b$ trả $10$ về $s_1$. Lấy $U=(4,7)$ và $V=(8,9)$. Chênh lệch từng trạng thái là $4$ tại $s_0$ và $2$ tại $s_1$, nên $\lVert U-V\rVert_\infty=4$.

Áp dụng một lần toán tử Bellman tối ưu $T_*$ cho cả hai bảng. Tại $s_0$:

$$T_*V(s_0)=\max\{2+0{,}5\cdot 8,\,-1+0{,}5\cdot 9\}=\max\{6,\,3{,}5\}=6,$$

$$T_*U(s_0)=\max\{2+0{,}5\cdot 4,\,-1+0{,}5\cdot 7\}=\max\{4,\,2{,}5\}=4,$$

nên chênh còn $2$. Tại $s_1$:

$$T_*V(s_1)=\max\{5+0{,}5\cdot 8,\,10+0{,}5\cdot 9\}=\max\{9,\,14{,}5\}=14{,}5,$$

$$T_*U(s_1)=\max\{5+0{,}5\cdot 4,\,10+0{,}5\cdot 7\}=\max\{7,\,13{,}5\}=13{,}5,$$

nên chênh còn $1$. Kết quả: $\lVert T_*U-T_*V\rVert_\infty=2=\gamma\cdot 4$. Phần thưởng trùng nhau triệt tiêu trong phép trừ, chỉ còn phần chiết khấu nhân với chênh cũ, nên khoảng cách giảm đúng hệ số $\gamma$. Ví dụ này gợi ý một tính chất tổng quát, và tính chất đó cần được chứng minh cho mọi cặp bảng.

### Chứng minh tính co của $T_*$

Với $0\le\gamma<1$ và mọi $U,V\in\mathcal V$, khẳng định cần chứng minh là

$$\lVert T_*U-T_*V\rVert_\infty\le\gamma\,\lVert U-V\rVert_\infty.$$

Chứng minh đi qua hai bước. Bước một là bất đẳng thức giữa hai cực đại theo hành động:

$$\bigl\lvert\max_a x_a-\max_a y_a\bigr\rvert\le\max_a\lvert x_a-y_a\rvert.$$

Thật vậy, gọi $a^*$ là hành động đạt $\max_a x_a$. Khi đó $\max_a x_a-\max_a y_a=x_{a^*}-\max_a y_a\le x_{a^*}-y_{a^*}\le\max_a(x_a-y_a)\le\max_a\lvert x_a-y_a\rvert$; hoán vai trò $x$ và $y$ cho chiều ngược lại, gộp hai chiều được điều cần chứng minh.

Bước hai là so sánh hai đại lượng hành động $Q_U(s,a)$ và $Q_V(s,a)$. Với cùng cặp trạng thái–hành động, hai bảng chỉ khác phần tiếp diễn, vì phần thưởng nằm trong $p(s',r\mid s,a)$ là như nhau:

$$Q_U(s,a)-Q_V(s,a)=\gamma\sum_{s',r}p(s',r\mid s,a)\bigl[U(s')-V(s')\bigr].$$

Phần thưởng triệt tiêu trong phép trừ này, kể cả khi thưởng phụ thuộc kết quả chuyển. Lấy trị tuyệt đối và dùng bất đẳng thức tam giác, mỗi chênh $U(s')-V(s')$ bị chặn bởi $\lVert U-V\rVert_\infty$; các xác suất không âm và có tổng $1$ nên tổng trọng số bằng $1$, cho

$$\lvert Q_U(s,a)-Q_V(s,a)\rvert\le\gamma\lVert U-V\rVert_\infty.$$

Kết hợp hai bước: bất đẳng thức giữa hai cực đại truyền chặn ấy sang $T_*U(s)-T_*V(s)$; lấy cực đại trên các trạng thái cho $\lVert T_*U-T_*V\rVert_\infty\le\gamma\lVert U-V\rVert_\infty$.

Toán tử Bellman của một chính sách cố định $T_\pi$ thỏa chặn tương tự, với điều kiện $\pi$ là chính sách Markov dừng. Thay phép cực đại bằng trung bình theo $\pi(a\mid s)$, các trọng số vẫn không âm và tổng $1$, nên chặn $\gamma\lVert U-V\rVert_\infty$ được giữ nguyên. Điều kiện $0\le\gamma<1$ làm hệ số co nhỏ hơn $1$; khi $\gamma=0$, một lần cập nhật đã không phụ thuộc bảng đầu.

### Định lý Banach trong $\mathbb R^n$ với chuẩn vô cùng

Một ánh xạ $F$ trên không gian mét $(X,d)$ là co nếu tồn tại $\gamma\in[0,1)$ sao cho $d(Fx,Fy)\le\gamma\, d(x,y)$ với mọi $x,y$. Không gian $\mathbb R^n$ với chuẩn vô cùng là đầy đủ: mọi dãy Cauchy hội tụ trong không gian, vì hội tụ theo từng tọa độ trong $\mathbb R$ và số tọa độ là hữu hạn. Định lý điểm bất động Banach phát biểu: mọi ánh xạ co trên không gian đầy đủ có đúng một điểm bất động $\bar V$ với $F\bar V=\bar V$, và dãy lặp $V_{k+1}=FV_k$ hội tụ tới $\bar V$ từ mọi điểm khởi đầu.

Áp dụng cho $T_*$: tính co vừa chứng minh với $\gamma<1$ và tính đầy đủ của $(\mathcal V,\lVert\cdot\rVert_\infty)$ cho tồn tại điểm bất động duy nhất $\bar V$, tức $T_*\bar V=\bar V$. Mọi bảng thỏa $T_*V=V$ đều phải bằng $\bar V$. Hai mục tiếp theo chứng minh $\bar V=v_*$.

### $\bar V$ chặn mọi chính sách, kể cả phụ thuộc lịch sử

Cần chứng minh $v_\pi\le\bar V$ cho mọi chính sách trong lớp $\Pi$, trong đó lớp có thể gồm cả chính sách phụ thuộc lịch sử. Gọi $H_t=(S_0,A_0,R_1,\dots,S_t)$ là lịch sử đến thời điểm $t$, trước khi chọn hành động $A_t$. Với $\pi$ bất kỳ trong lớp, kỳ vọng có điều kiện theo $H_t$ phải lấy trung bình theo phân phối của $A_t$ do chính sách sinh ra, rồi theo chuyển tiếp của môi trường. Khai triển dưới đây áp dụng khi $S_t\in\mathcal S$; tại trạng thái kết thúc, phần thưởng và giá trị tiếp diễn đều bằng $0$.

$$\mathbb E_\pi\bigl[R_{t+1}+\gamma\bar V(S_{t+1})\mid H_t\bigr]=\sum_a\pi_t(a\mid H_t)\sum_{s',r}p(s',r\mid S_t,a)\bigl[r+\gamma\bar V(s')\bigr].$$

Với mỗi $a$ cố định, tổng trong ngoặc không vượt quá $\max_{a'}\sum_{s',r}p(s',r\mid S_t,a')[r+\gamma\bar V(s')]=T_*\bar V(S_t)=\bar V(S_t)$, vì $\bar V$ là điểm bất động của $T_*$. Trung bình trọng số $\pi_t(a\mid H_t)$ không âm và tổng $1$, nên

$$\mathbb E_\pi\bigl[R_{t+1}+\gamma\bar V(S_{t+1})\mid H_t\bigr]\le\bar V(S_t).$$

Nhân hai vế với $\gamma^t$ và lấy kỳ vọng khi khởi đầu tại $S_0=s$. Luật kỳ vọng lặp cho

$$\begin{aligned}
\gamma^t\mathbb E_\pi[R_{t+1}\mid S_0=s]
&\le\gamma^t\mathbb E_\pi[\bar V(S_t)\mid S_0=s]\\
&\quad-\gamma^{t+1}\mathbb E_\pi[\bar V(S_{t+1})\mid S_0=s].
\end{aligned}$$

Cộng từ $t=0$ đến $N-1$, các hạng giá trị ở giữa triệt tiêu từng cặp:

$$\mathbb E_\pi\!\left[\sum_{t=0}^{N-1}\gamma^t R_{t+1}+\gamma^N\bar V(S_N)\,\middle|\,S_0=s\right]\le\bar V(s).$$

Hạng đuôi có trị tuyệt đối không quá $\gamma^N\lVert\bar V\rVert_\infty$ và tiến về $0$ vì $\gamma<1$; tổng thưởng bị chặn nên trao đổi giới hạn và kỳ vọng hợp lệ. Kết quả là bất đẳng thức giá trị:

$$v_\pi(s)\le\bar V(s),\qquad v_\pi(s):=\mathbb E_\pi\bigl[G_0\mid S_0=s\bigr],\quad G_0=\sum_{t=0}^{\infty}\gamma^t R_{t+1}.$$

Định nghĩa $v_\pi$ qua tổng chiết khấu từ thời điểm $0$ với điều kiện $S_0=s$ là định nghĩa chuẩn cho mọi chính sách trong lớp $\Pi$, kể cả chính sách phụ thuộc lịch sử; lập luận trên chỉ dùng $T_*$ và tính Markov của môi trường, không gán toán tử $T_\pi$ cho lớp chính sách phụ thuộc lịch sử. Chặn $v_\pi\le\bar V$ do đó đúng cho toàn bộ lớp $\Pi$ trong định nghĩa tối ưu.

### Đạt cận trên bằng chính sách tham lam và kết luận $\bar V=v_*$

Cận trên $\bar V$ cần được đạt tới. Vì $\bar V$ là điểm bất động của $T_*$, tại mỗi trạng thái tồn tại hành động đạt cực đại trong $\max_a Q_{\bar V}(s,a)$. Chọn một hành động như vậy tại mỗi trạng thái tạo ra chính sách Markov dừng xác định $\bar\pi$ tham lam theo $\bar V$, thỏa

$$T_{\bar\pi}\bar V=T_*\bar V=\bar V.$$

Toán tử $T_{\bar\pi}$ cũng co (đã chứng minh ở trên cho chính sách Markov dừng) và $\mathbb R^n$ đầy đủ, nên theo Banach nó có điểm bất động duy nhất; điểm bất động đó chính là $v_{\bar\pi}$, vì $v_{\bar\pi}$ thỏa phương trình Bellman đánh giá $v_{\bar\pi}=T_{\bar\pi}v_{\bar\pi}$. Do $\bar V$ cũng là điểm bất động của $T_{\bar\pi}$, tính duy nhất cho

$$v_{\bar\pi}=\bar V.$$

Kết hợp hai kết quả: $\bar V$ chặn mọi chính sách và đạt được bởi $\bar\pi$, nên $\bar V$ là phần tử lớn nhất của $\{v_\pi:\pi\in\Pi\}$, tức $\bar V=v_*$, và $\bar\pi$ là chính sách tối ưu. Định nghĩa tối ưu dùng $\sup$ trước, và chứng minh này cho thấy $\sup$ đạt được.

### Hội tụ hình học của lặp giá trị

Tính co cho chặn hội tụ hình học. Vì $v_*$ là điểm bất động của $T_*$, áp dụng chặn co $k$ lần:

$$\lVert V_k-v_*\rVert_\infty=\lVert T_*^k V_0-T_*^k v_*\rVert_\infty\le\gamma^k\,\lVert V_0-v_*\rVert_\infty.$$

Xét ví dụ số có sai số đầu $\lVert V_0-v_*\rVert_\infty=64$ và $\gamma=0{,}5$; đây là con số minh họa riêng, không lấy từ lưới năm ô. Chặn là $64\cdot(0{,}5)^k$. Điều kiện $64\cdot(0{,}5)^k<1$ tương đương $2^{6-k}<1$, tức $k>6$. Tại $k=6$, chặn bằng $1$, chưa nhỏ hơn $1$; tại $k=7$, chặn bằng $0{,}5$, đã đạt yêu cầu. Trục tung của hình dưới dùng thang $\log_2$ để hai mốc $1$ và $0{,}5$ đọc được rõ.

![Chặn sai số giảm từ 64 theo hệ số 0,5 mỗi lượt; bằng 1 ở lượt 6 và bằng 0,5 ở lượt 7, trục tung dùng thang logarit cơ số 2.](img/lec-04/convergence.svg)

Cần phân biệt chặn lý thuyết với thực nghiệm: bảy lượt là đủ theo chặn, không phải số lượt tối thiểu thực của mọi MDP. Hạn chế là $v_*$ chưa biết nên chặn chứa sai số ban đầu, khó dùng trực tiếp để dừng; phần dư dưới đây cung cấp một đại lượng đo được.

### Phần dư Bellman và ngưỡng dừng

Định nghĩa phần dư

$$\Delta_*(V)=\lVert T_*V-V\rVert_\infty,$$

đo được trực tiếp từ bảng hiện có, trong khi sai số $e=\lVert V-v_*\rVert_\infty$ thì không. Suy diễn dùng bất đẳng thức tam giác:

$$\lVert V-v_*\rVert_\infty\le\lVert V-T_*V\rVert_\infty+\lVert T_*V-T_*v_*\rVert_\infty.$$

Hạng thứ nhất chính là $\Delta_*(V)$. Hạng thứ hai bị chặn bởi $\gamma\lVert V-v_*\rVert_\infty$ nhờ tính co, vì $v_*$ là điểm bất động. Ghép lại:

$$e\le \Delta_*(V)+\gamma e\;\Rightarrow\;(1-\gamma)e\le \Delta_*(V)\;\Rightarrow\;e\le\frac{\Delta_*(V)}{1-\gamma}.$$

Số cụ thể: với $\gamma=0{,}5$ và mục tiêu sai số $\varepsilon=0{,}2$, ngưỡng dừng trên phần dư là $\eta=(1-\gamma)\varepsilon=0{,}1$. Ngưỡng $0{,}1$ áp dụng cho phần dư, còn mức $0{,}2$ áp dụng cho sai số giá trị; hai mức này không tráo cho nhau. Nếu dùng bảng cập nhật $W=T_\pi V$ làm đánh giá chính sách $\pi$, đặt $\Delta_\pi(V)=\lVert T_\pi V-V\rVert_\infty$; vì $v_\pi$ là điểm bất động của $T_\pi$, tam giác và tính co cho $\lVert V-v_\pi\rVert_\infty\le \Delta_\pi(V)/(1-\gamma)$, do đó

$$\lVert W-v_\pi\rVert_\infty=\lVert T_\pi V-T_\pi v_\pi\rVert_\infty\le\gamma\lVert V-v_\pi\rVert_\infty\le\frac{\gamma\,\Delta_\pi(V)}{1-\gamma}.$$

Sai số của $W$ không vượt quá $\gamma$ lần sai số của $V$. Đây là hệ quả cho bảng sau cập nhật, cũng áp dụng cho biến thể chọn trả $W$. Quy trình chính ở phần 3 trả $V$ đã đo phần dư, nên dùng chặn $\Delta_\pi(V)/(1-\gamma)$.

### Giới hạn của mô hình dạng bảng: ví dụ CartPole

CartPole có trạng thái liên tục gồm vị trí $x$, vận tốc $\dot x$, góc $\theta$ và vận tốc góc $\dot\theta$. Chia $x$ và $\dot x$ mỗi biến thành $3$ khoảng, $\theta$ và $\dot\theta$ mỗi biến thành $6$ khoảng, số ô là

$$3\times 3\times 6\times 6=324,$$

tức một biểu diễn hữu hạn đủ để lập bảng. Nhưng rời rạc hóa chỉ tạo trạng thái gộp; nó chưa cung cấp hạt nhân chuyển và phần thưởng cho mô hình bảng, cũng chưa bảo đảm trạng thái gộp có tính Markov. Hình minh họa hai điểm liên tục khác nhau rơi vào cùng một ô: thông tin bị gộp mất.

![Hai trạng thái liên tục khác nhau của CartPole được gộp vào cùng một ô; mô hình chuyển và phần thưởng của ô vẫn cần được xác định.](img/lec-04/cartpole.svg)

Cần phân biệt hai loại sai số: sai số lặp giá trị trên mô hình đã cho (được chặn bởi $\Delta_*(V)/(1-\gamma)$), và sai số do rời rạc hóa hoặc ước lượng mô hình. Tối ưu mô hình hữu hạn không tự chứng minh tối ưu trên môi trường liên tục, nên mọi bảo đảm như ngưỡng dừng phải kiểm tra lại miền áp dụng.

::: exercise Câu hỏi:
MDP hữu hạn đã biết mô hình có phần dư $\Delta_*(V)=0{,}15$ theo chuẩn vô cùng và $\gamma=0{,}5$. (a) Chặn sai số giá trị $e=\lVert V-v_*\rVert_\infty$ bằng bao nhiêu? (b) Kết quả đó đã bảo đảm ngưỡng $e\le 0{,}2$ chưa? Nêu một điều kiện đủ trên $\Delta_*(V)$ theo chặn phần dư. (c) Chứng minh phần dư còn dùng được khi $\gamma=1$ không? Giải thích từng bước.
:::

::: hint
Dùng chặn $e\le \Delta_*(V)/(1-\gamma)$; một cận trên không cho biết chiều ngược lại; xác định bước sử dụng giả thiết $\gamma<1$ trong chứng minh tính co.
:::

::: solution
(a) Áp dụng trực tiếp: $e\le \Delta_*(V)/(1-\gamma)=0{,}15/0{,}5=0{,}3$. (b) Chưa bảo đảm ngưỡng $0{,}2$: chặn cho biết $e\le 0{,}3$, sai số thực tế có thể nhỏ hơn $0{,}2$ nhưng chưa có bảo đảm. Một điều kiện đủ để bảo đảm $e\le 0{,}2$ bằng chặn này là $\Delta_*(V)\le(1-\gamma)\cdot 0{,}2=0{,}5\cdot 0{,}2=0{,}1$. Để đạt chứng nhận theo chặn đang dùng, tiếp tục lặp cho tới khi phần dư không vượt $0{,}1$. Nếu $\Delta_*(V)=0{,}1$ thì $e\le 0{,}1/0{,}5=0{,}2$, đúng yêu cầu. (c) Không. Khi $\gamma=1$, bất đẳng thức trên không còn bảo đảm hệ số co nhỏ hơn $1$; đồng thời mẫu số $1-\gamma$ bằng $0$ khiến công thức $e\le \Delta_*(V)/(1-\gamma)$ không xác định. Chứng minh dựa trên giả thiết $\gamma<1$; bỏ giả thiết đó thì cần các giả thiết và lập luận khác, chẳng hạn các điều kiện bổ sung về chuyển tiếp và phần thưởng cùng một chứng minh hội tụ riêng; các trường hợp đó nằm ngoài phạm vi bài này.
:::

<!-- note-topic-id: lec-04-part-07 -->

## 7. Chọn quy trình và đánh giá kết quả lập kế hoạch

### Bảng so sánh ba phương pháp

Ba quy trình được phân biệt theo đầu vào và đầu ra:

| Phương pháp | Đầu vào | Bước chính | Đầu ra và dừng |
|---|---|---|---|
| Đánh giá chính sách | Mô hình $p(s',r\mid s,a)$ và $\pi$ | Giải hệ hoặc lặp $T_\pi$ | $v_\pi$ hoặc ước lượng |
| Lặp chính sách | Mô hình | Đánh giá–cải thiện | $\pi_*,v_*$ khi ổn định |
| Lặp giá trị | Mô hình | Lặp $T_*$ | $V,\pi_V$ khi phần dư nhỏ |

Bảo đảm chung: mô hình đúng, hữu hạn, thưởng bị chặn và $0\le\gamma<1$. Nếu chỉ cần giá trị của một chính sách cho trước, đánh giá chính sách là đủ: lập hệ phương trình Bellman hoặc lặp toán tử $T_\pi$ cho tới khi hội tụ. Nếu cần chính sách tốt, có hai đường. Lặp chính sách đánh giá chính xác rồi cải thiện, giữ hành động cũ khi hòa, dừng khi chính sách không đổi nữa; nhánh này cho chứng nhận ổn định của chính sách. Lặp giá trị cập nhật bảng giá trị trực tiếp bằng $T_*$ và trích chính sách $\pi_V$ ở cuối, dừng khi phần dư nhỏ dưới ngưỡng hoặc khi hết ngân sách tính; nhánh hết ngân sách trả kết quả chưa chứng nhận đạt ngưỡng. Cả hai đều cần mô hình chuyển tiếp và thưởng, vì mọi phép tổng đều theo $p$. Khi mô hình không có, ba quy trình này không chạy được theo dạng cập nhật kỳ vọng đã nêu. Các phương pháp học từ trải nghiệm xử lý trường hợp không có mô hình đầy đủ. Yêu cầu biết mô hình để tính kỳ vọng và cơ chế bootstrapping từ ước lượng tiếp nối là hai đặc điểm riêng; dùng ước lượng tiếp nối không tự đòi hỏi mô hình đầy đủ.

### Lời giải cho bài toán hai trạng thái

Quay lại bài toán hai trạng thái ở mở đầu, với $\gamma=0{,}5$. Chính sách tối ưu là $\pi_*=(b,b)$ với giá trị $v_*=(9,20)$. Bảng $Q_{v_*}$ xác nhận điều đó:

| $Q_{v_*}$ | $a$ | $b$ |
|---|---|---|
| $s_0$ | $6{,}5$ | $\mathbf{9}$ |
| $s_1$ | $9{,}5$ | $\mathbf{20}$ |

Cực đại rơi ở $b$ tại cả hai trạng thái, nên $T_*v_*=v_*$: đây là chứng nhận Bellman. Tại $s_0$, chọn $b$ một lần rồi tiếp tục tối ưu:

$$Q_{v_*}(s_0,b)=-1+0{,}5\cdot 20=9,$$

còn chọn $a$ đưa hệ thống về $s_0$ với giá trị tối ưu $9$ chứ không phải $4$ của chính sách luôn chọn $a$, nên $Q_{v_*}(s_0,a)=2+0{,}5\cdot 9=6{,}5$. Tại $s_1$:

$$Q_{v_*}(s_1,b)=10+0{,}5\cdot 20=20,\qquad Q_{v_*}(s_1,a)=5+0{,}5\cdot 9=9{,}5.$$

Với $\gamma=0{,}5$, dãy thưởng $-1,10,10,\ldots$ cho giá trị $-1+0{,}5\cdot 20=9$ tại $s_0$. Giá trị ở $s_0$ tăng từ $4$ lên $9$ nhờ đổi quyết định dài hạn, trên cùng mô hình và hệ số chiết khấu. Kết luận này liên quan trực tiếp bảng phương pháp: bài toán có mô hình nên lặp giá trị hoặc lặp chính sách đều chạy được, và bảng $Q_{v_*}$ đúng là đầu ra cần kiểm khi trích chính sách từ bảng giá trị.

::: exercise Câu hỏi:
MDP hữu hạn, mô hình chính xác, $\gamma=0{,}5$, lặp giá trị dừng với phần dư $\Delta_*(V)=0{,}1$ theo chuẩn vô cùng và trích chính sách $\pi_V$. (a) Kết luận nào về $V$ được bảo đảm, kèm công thức? (b) Nhận định "$\pi_V$ chắc chắn tối ưu tuyệt đối" có đủ căn cứ chưa, vì sao? (c) Thuật toán nào cho chứng nhận chính sách ổn định khi đánh giá chính xác và giữ hòa?
:::

::: hint
Dùng $e\le \Delta_*(V)/(1-\gamma)$ với $\Delta_*(V)=0{,}1$; phân biệt bảo đảm về giá trị gần đúng với chứng nhận tối ưu chính sách; áp dụng quy tắc giữ hòa của lặp chính sách.
:::

::: solution
(a) Vì sai số giá trị bị chặn bởi phần dư với hệ số $1/(1-\gamma)$, $\lVert V-v_*\rVert_\infty\le 0{,}1/0{,}5=0{,}2$. Bất đẳng thức tam giác cho $e\le \Delta_*(V)+\gamma e$, chuyển vế được $e\le \Delta_*(V)/(1-\gamma)$; thay số cho $0{,}2$. (b) Chưa đủ căn cứ. Phần dư $0{,}1$ chỉ cho chặn sai số giá trị $0{,}2$; một bảng giá trị gần đúng không đồng nhất với chính sách tối ưu, nên $\pi_V$ có thể đã tối ưu nhưng chưa có bằng chứng. Một cách chứng nhận tối ưu là đánh giá chính sách chính xác rồi kiểm tra điều kiện $T_*v_\pi=v_\pi$; lặp chính sách là một phương pháp cung cấp cả hai yếu tố đó khi hội tụ ổn định, nhưng không phải phương pháp duy nhất. Chứng nhận Bellman trong ví dụ hai trạng thái ở trên vẫn có giá trị theo nghĩa này. (c) Lặp chính sách đánh giá chính xác từng chính sách, cải thiện tham lam, giữ hành động cũ khi hòa, và dừng khi chính sách không đổi giữa hai lần cải thiện liên tiếp; lúc đó chính sách ổn định và là tối ưu trên mô hình đã cho.
:::

### Bài tập tự luyện

Trong [Bài tập tuần 3](../RL-hk2-2025-2026/resources/hw3.pdf), Bài 9 dùng MDP ba trạng thái và bộ dữ kiện riêng, với $\gamma=0{,}9$. Dùng đúng các cạnh chuyển và phần thưởng trong đề. Phần 1 yêu cầu lập công thức lặp giá trị, tính $V_1$ từ $V_0=0$ và chính sách tham lam tương ứng; phần 2 cho một chính sách ban đầu để lập hệ đánh giá rồi viết công thức cải thiện.

Bài 6 yêu cầu chứng minh dạng ma trận của phương trình đánh giá chính sách và tính khả nghịch của $I-\gamma P_\pi$. Bài 3 yêu cầu chứng minh sự tồn tại của chính sách tối ưu trong MDP hữu hạn; Bài 7 yêu cầu chứng minh tính đơn điệu của $T_\pi$ và $T_*$. Khi viết lại chứng minh, chỉ rõ mỗi giả thiết được dùng ở bước nào. Các lập luận tương ứng nằm trong các mục về dạng ma trận, định lý cải thiện và điểm bất động của ghi chú này.

## Tài liệu tham khảo

- Richard S. Sutton và Andrew G. Barto, [Reinforcement Learning: An Introduction, ấn bản 2](http://incompleteideas.net/book/RLbook2020.pdf), chương 3, §3.1, §3.3–3.6; chương 4, §4.1–4.7, tr. 73–88. Các mục này cung cấp định nghĩa và thuật toán; ghi chú trình bày thêm các bước chứng minh và các ví dụ số riêng.
- [Bộ trang chiếu Bài 04: Giải MDP bằng quy hoạch động](lecture-04-giai-mdp-bang-quy-hoach-dong.html), học kỳ 1, năm học 2026–2027. Bộ trang chiếu và ghi chú dùng chung ký hiệu, nhưng có cấu trúc và bộ dữ kiện ví dụ riêng.
- Tạ Việt Cường, [lecture04-solving-MDP.pdf](../RL-hk2-2025-2026/lecture04-solving-MDP.pdf), tr. 6–10, 14, 17–25 và 31–37. Mô hình hai trạng thái và lưới năm ô của ghi chú có cấu trúc chuyển tiếp tương ứng với nguồn; phần thưởng và hệ số chiết khấu đã được điều chỉnh thành bộ dữ kiện bổ sung được khai báo trong từng ví dụ.
- Tạ Việt Cường, [Bài tập tuần 3: Giải bài toán MDP](../RL-hk2-2025-2026/resources/hw3.pdf), Bài 3, 6, 7 và 9, tr. 1–2 trong tài liệu bốn trang.
