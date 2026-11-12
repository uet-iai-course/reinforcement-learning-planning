# Bài tập Bài 02 — Giao diện tác tử–môi trường

Tệp gồm mười một bài, Bài tập 02.14–02.24, đánh số tiếp theo mười ba bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html) (Bài tập 02.1–02.13). Mọi bài lấy từ bài tập chương 3 của Sutton và Barto (2018); mỗi bài ghi số bài, mục và trang của sách, và dữ kiện được chép lại trong khối đề. Các bài chia theo ba mức: nhận biết (02.14, 02.15); tính toán hoặc chứng minh (02.16–02.21); vận dụng vào bài toán Học tăng cường (reinforcement learning) (02.22–02.24). Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/1/1) | — |
| 2. Vòng tương tác và tín hiệu thưởng | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/2/1) | 02.14; ghi chú: 02.1 |
| 3. Thông tin khả dụng và tính Markov | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/3/1) | ghi chú: 02.2, 02.3, 02.11 |
| 4. Quy tắc chọn hành động | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/4/1) | 02.20; ghi chú: 02.4, 02.13 |
| 5. Lợi tức, hàm giá trị và hàm động lực | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/5/1) | 02.15–02.19, 02.21, 02.22; ghi chú: 02.5–02.7, 02.9, 02.10(a), 02.12 |
| 6. Thiết kế phần thưởng | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/6/1) | 02.23, 02.24; ghi chú: 02.8, 02.10(b) |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/7/1) | — |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 02. Công thức của ghi chú được dẫn bằng số trong ngoặc, chẳng hạn (4.5); công thức của sách được ghi rõ "của sách". Tại thời điểm $t$, tác tử ở trạng thái $S_t$ và chọn hành động $A_t$; môi trường trả phần thưởng $R_{t+1}$ và trạng thái $S_{t+1}$, nên phần thưởng của chuyển từ $t$ sang $t+1$ mang chỉ số $t+1$ (Định nghĩa 02.1). Tập $\mathcal S$ gồm các trạng thái chưa kết thúc, $\mathcal S^+$ là $\mathcal S$ thêm các trạng thái kết thúc, $\mathcal A(s)$ là tập hành động hợp lệ tại $s$ và $\mathcal R$ là tập giá trị phần thưởng. Chính sách $\pi(a\mid s)$ là một phân phối trên $\mathcal A(s)$ với mỗi $s$ (Định nghĩa 02.8, với biểu diễn là trạng thái).

Với hệ số chiết khấu $\gamma\in[0,1]$ và lượt kết thúc tại $T<\infty$, lợi tức từ $t<T$ là
$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1},\qquad G_T=0 .
\tag{4.5}
$$
Với nhiệm vụ tiếp diễn ($T=\infty$), Định nghĩa 02.12 đòi thêm $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$ với mọi $t$, và
$$
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}.
\tag{4.6}
$$
Hệ thức truy hồi $G_t=R_{t+1}+\gamma G_{t+1}$ là Mệnh đề 02.13(a). Khi $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$, chuỗi (4.6) hội tụ tuyệt đối và
$$
\lvert G_t\rvert\le\frac{R_{\max}}{1-\gamma}
\tag{4.7}
$$
(Mệnh đề 02.13(b)). Khi $\gamma=1$ và một quỹ đạo không kết thúc, lợi tức của nó là giới hạn của tổng riêng khi giới hạn tồn tại, có thể bằng $\pm\infty$ (Mục 4.2 của ghi chú).

Hàm giá trị trạng thái là $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$, công thức (4.8), và giá trị của trạng thái kết thúc bằng $0$ (Định nghĩa 02.14). Hàm động lực là $p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$, công thức (4.9), xác định với $s\in\mathcal S$, $a\in\mathcal A(s)$, $s'\in\mathcal S^+$, $r\in\mathcal R$, và tổng theo mọi cặp $(s',r)$ bằng $1$. Từ $p$ suy ra xác suất chuyển $p(s'\mid s,a)=\sum_rp(s',r\mid s,a)$ và thưởng kỳ vọng một bước $r(s,a)=\sum_{s'}\sum_rr\,p(s',r\mid s,a)$ (Định nghĩa 02.16).

Tương ứng với sách: hàm bốn đối số (3.2) của sách là (4.9); (3.7) của sách là (4.5) với $\gamma=1$; (3.8) của sách là (4.6); (3.9) của sách là Mệnh đề 02.13(a). Sách viết $r(s,a,s')$ cho phần thưởng kỳ vọng của chuyển từ $s$ sang $s'$ khi chọn $a$, và viết $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ với $t$ bất kỳ; dưới các giả thiết của Định nghĩa 02.14, giá trị này không phụ thuộc $t$ và bằng (4.8).

Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$.

## Mức nhận biết

### Bài tập 02.14. Ranh giới tác tử–môi trường khi lái xe

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.3, §3.1, trang 51.

::: exercise Bài tập 02.14 (Ranh giới tác tử–môi trường khi lái xe)
Xét bài toán lái xe. Hành động của người lái có thể được đặt ở bốn mức:

1. bàn đạp ga, vô lăng và phanh, nơi cơ thể người lái tiếp xúc với xe;
2. xa hơn, mô-men xoắn (torque) tác dụng lên bánh xe, nơi lốp tiếp xúc với mặt đường;
3. gần hơn, các lần co cơ điều khiển tay chân, nơi não tiếp xúc với cơ thể;
4. ở mức rất cao, lựa chọn nơi lái xe đến.

- (a) Với mỗi mức, nêu hành động $A_t$ và các thành phần thuộc môi trường.
- (b) Nêu căn cứ để đặt ranh giới tác tử–môi trường ở một mức thay vì mức khác.
- (c) Cho biết vị trí của ranh giới do một lý do nền tảng quyết định hay do người mô hình hóa chọn, và giải thích.
:::

::: hint Gợi ý Bài tập 02.14
Nhắc lại Định nghĩa 01.1 và đoạn sau nó: mọi thứ tác tử không điều khiển được thuộc môi trường, kể cả luật phần thưởng (Sutton và Barto, 2018, §3.1, trang 50).
:::

::: solution Lời giải Bài tập 02.14
**Câu (a).**

- Mức 1: $A_t$ gồm độ nhấn ga, góc vô lăng và lực phanh. Động cơ, hệ lái, lốp, mặt đường và các xe khác thuộc môi trường.
- Mức 2: $A_t$ là mô-men xoắn ở các bánh. Lốp, mặt đường và các xe khác thuộc môi trường.
- Mức 3: $A_t$ là tín hiệu co cơ. Cơ, xương và tay chân của người lái, bàn đạp, vô lăng và toàn bộ xe thuộc môi trường; Sutton và Barto (2018, §3.1, trang 50) xếp cơ, xương và giác quan của người hay động vật vào môi trường.
- Mức 4: $A_t$ là điểm đến. Mọi thao tác lái để tới điểm đó thuộc môi trường.

**Câu (b).** Ranh giới đặt ở giới hạn điều khiển tuyệt đối của tác tử: hành động là đại lượng tác tử đặt được tùy ý ở mỗi bước, còn mọi thứ tác tử không thay đổi được tùy ý thuộc môi trường (Định nghĩa 01.1; Sutton và Barto, 2018, §3.1, trang 50). Ranh giới đo giới hạn điều khiển, không đo hiểu biết: tác tử có thể biết rõ động lực học của xe mà xe vẫn thuộc môi trường. Trong giới hạn đó, mức được chọn phụ thuộc quyết định cần học: một tác tử chọn lộ trình đặt hành động ở mức 4, một tác tử điều khiển bàn đạp và vô lăng đặt hành động ở mức 1.

**Câu (c).** Không có mức đúng duy nhất. Theo Sutton và Barto (2018, §3.1, trang 50), ranh giới được xác định khi người mô hình hóa chọn trạng thái, hành động và phần thưởng, tức chọn bài toán quyết định cần giải. Trong một hệ phức tạp, nhiều tác tử có thể hoạt động cùng lúc, mỗi tác tử một ranh giới, và quyết định của tác tử cấp cao là một phần trạng thái của tác tử cấp thấp. Ví dụ: tác tử ở mức 4 chọn điểm đến, còn tác tử ở mức 1 nhận điểm đến đó như một phần trạng thái và điều khiển bàn đạp, vô lăng. Lựa chọn này vẫn bị ràng buộc bởi câu (b): hành động phải nằm trong giới hạn điều khiển tuyệt đối của tác tử, và cơ chế tính phần thưởng luôn ở phía môi trường.

**Kiểm tra lại.** Ở cả bốn mức, phần thưởng do môi trường tính, và tác tử chỉ quyết định $A_t$. Hai lỗi thường gặp: đặt ranh giới tại thân xe hay da của người lái theo ranh giới vật lý, trong khi động cơ, cơ và giác quan thuộc môi trường; và xếp cơ chế tính phần thưởng vào tác tử vì tác tử biết công thức tính.
:::

### Bài tập 02.15. Điều kiện tổng của hàm động lực trong nhiệm vụ có lượt

**Mức độ:** nhận biết; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.5, §3.3, trang 55; đẳng thức (3.3), §3.1, trang 49.

::: exercise Bài tập 02.15 (Điều kiện tổng của hàm động lực trong nhiệm vụ có lượt)
Ở §3.1 của sách, hàm động lực của một nhiệm vụ tiếp diễn thỏa
$$
\sum_{s'\in\mathcal S}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1
$$
với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$, đẳng thức (3.3) của sách. Trong nhiệm vụ có lượt, $\mathcal S$ là tập trạng thái chưa kết thúc và $\mathcal S^+$ là $\mathcal S$ thêm trạng thái kết thúc.

- (a) Viết lại đẳng thức trên cho nhiệm vụ có lượt.
- (b) Giải thích vì sao miền lấy tổng của $s'$ đổi, còn miền của $s$ giữ nguyên.
:::

::: hint Gợi ý Bài tập 02.15
Từ một trạng thái chưa kết thúc, bước kế tiếp có thể đưa tác tử vào trạng thái kết thúc; sau trạng thái kết thúc không còn hành động nào.
:::

::: solution Lời giải Bài tập 02.15
**Câu (a).** Với mọi $s\in\mathcal S$ và $a\in\mathcal A(s)$,
$$
\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1 .
$$

**Câu (b).** Với $s\in\mathcal S$ và $a\in\mathcal A(s)$, trạng thái kế tiếp $S_{t+1}$ có thể là trạng thái kết thúc, nên phân phối của cặp $(S_{t+1},R_{t+1})$ nằm trên $\mathcal S^+\times\mathcal R$. Tổng chỉ theo $s'\in\mathcal S$ bỏ sót xác suất vào trạng thái kết thúc và nhỏ hơn $1$ khi xác suất đó dương. Miền của $s$ vẫn là $\mathcal S$, vì lượt kết thúc khi môi trường vào trạng thái kết thúc và không còn hành động nào sau đó (Định nghĩa 02.1), nên $p(\cdot\mid s,a)$ không cần xác định khi $s$ là trạng thái kết thúc. Đẳng thức ở câu (a) là điều kiện tổng của Định nghĩa 02.16.

**Kiểm tra lại.** Trên mê cung $8\times8$ của ghi chú (Ví dụ 02.13), bước Đông từ $(7,6)$ cho cặp $(\mathrm G,-1)$ với xác suất $1$ và $\mathrm G\notin\mathcal S$: tổng theo $s'\in\mathcal S$ bằng $0$, tổng theo $s'\in\mathcal S^+$ bằng $1$. Hai lỗi thường gặp: đổi cả miền của $s$ thành $\mathcal S^+$, dù tại trạng thái kết thúc không có hành động nào; và kiểm điều kiện tổng riêng theo $s'$ với một giá trị $r$ cố định, thay cho tổng theo mọi cặp $(s',r)$.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 02.16. Hàm động lực của robot thu gom lon

**Mức độ:** tính toán; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.4, §3.1, trang 53; dữ kiện của Ví dụ 3.3, trang 52.

::: exercise Bài tập 02.16 (Hàm động lực của robot thu gom lon)
Ví dụ 3.3 của sách: một robot thu gom lon rỗng trong văn phòng. Trạng thái là mức pin, $\mathcal S=\{\text{cao},\text{thấp}\}$. Tập hành động là $\mathcal A(\text{cao})=\{\text{tìm},\text{chờ}\}$ và $\mathcal A(\text{thấp})=\{\text{tìm},\text{chờ},\text{sạc}\}$: "tìm" là chủ động tìm lon trong một khoảng thời gian, "chờ" là đứng yên chờ người mang lon tới, "sạc" là về trạm để sạc pin. Bảng của sách cho xác suất chuyển $p(s'\mid s,a)$ và phần thưởng kỳ vọng của chuyển $r(s,a,s')$, với $r_{\text{tìm}}>r_{\text{chờ}}$ là số lon kỳ vọng thu được khi tìm và khi chờ, và cũng là phần thưởng kỳ vọng:

| $s$ | $a$ | $s'$ | $p(s'\mid s,a)$ | $r(s,a,s')$ |
| --- | --- | --- | --- | --- |
| cao | tìm | cao | $\alpha$ | $r_{\text{tìm}}$ |
| cao | tìm | thấp | $1-\alpha$ | $r_{\text{tìm}}$ |
| thấp | tìm | cao | $1-\beta$ | $-3$ |
| thấp | tìm | thấp | $\beta$ | $r_{\text{tìm}}$ |
| cao | chờ | cao | $1$ | $r_{\text{chờ}}$ |
| cao | chờ | thấp | $0$ | – |
| thấp | chờ | cao | $0$ | – |
| thấp | chờ | thấp | $1$ | $r_{\text{chờ}}$ |
| thấp | sạc | cao | $1$ | $0$ |
| thấp | sạc | thấp | $0$ | – |

Hàng (thấp, tìm, cao) là trường hợp pin cạn: robot phải được cứu và pin được sạc lại lên mức cao. Giả sử thêm $0<\alpha<1$, $0<\beta<1$ và phần thưởng của mỗi chuyển bằng đúng giá trị $r(s,a,s')$ trong bảng.

- (a) Lập bảng với các cột $s$, $a$, $s'$, $r$, $p(s',r\mid s,a)$, mỗi hàng ứng với một bộ bốn có $p(s',r\mid s,a)>0$.
- (b) Từ bảng ở câu (a), tính $p(\text{cao}\mid\text{thấp},\text{tìm})$, $r(\text{thấp},\text{tìm})$ và $r(\text{cao},\text{tìm})$, rồi kiểm tra điều kiện tổng của Định nghĩa 02.16 cho cặp $(\text{thấp},\text{tìm})$.
:::

::: hint Gợi ý Bài tập 02.16
Mỗi hàng có xác suất dương của bảng sách cho đúng một giá trị phần thưởng, nên cho đúng một hàng của bảng mới với $p(s',r\mid s,a)=p(s'\mid s,a)$.
:::

::: solution Lời giải Bài tập 02.16
**Câu (a).** Bỏ ba hàng có xác suất $0$; mỗi hàng còn lại có một giá trị phần thưởng duy nhất:

| $s$ | $a$ | $s'$ | $r$ | $p(s',r\mid s,a)$ |
| --- | --- | --- | --- | --- |
| cao | tìm | cao | $r_{\text{tìm}}$ | $\alpha$ |
| cao | tìm | thấp | $r_{\text{tìm}}$ | $1-\alpha$ |
| thấp | tìm | cao | $-3$ | $1-\beta$ |
| thấp | tìm | thấp | $r_{\text{tìm}}$ | $\beta$ |
| cao | chờ | cao | $r_{\text{chờ}}$ | $1$ |
| thấp | chờ | thấp | $r_{\text{chờ}}$ | $1$ |
| thấp | sạc | cao | $0$ | $1$ |

**Câu (b).** Theo các công thức sau Định nghĩa 02.16, $p(s'\mid s,a)$ cộng xác suất của mọi cặp có cùng $s'$, còn $r(s,a)$ lấy trung bình phần thưởng với trọng số là xác suất của từng cặp $(s',r)$. Từ $(\text{thấp},\text{tìm})$, chỉ có $r=-3$ đi với $s'=\text{cao}$, nên $p(\text{cao}\mid\text{thấp},\text{tìm})=1-\beta$, và $r(\text{thấp},\text{tìm})$ bằng
$$
\begin{aligned}
&\beta\,r_{\text{tìm}}+(1-\beta)\cdot(-3)\\
&\quad=\beta\,r_{\text{tìm}}-3(1-\beta).
\end{aligned}
$$
Từ $(\text{cao},\text{tìm})$, cả hai kết cục cùng nhận $r_{\text{tìm}}$, nên $r(\text{cao},\text{tìm})=\alpha\,r_{\text{tìm}}+(1-\alpha)\,r_{\text{tìm}}=r_{\text{tìm}}$. Điều kiện tổng cho $(\text{thấp},\text{tìm})$: $\beta+(1-\beta)=1$.

**Kiểm tra lại.** Bảng mới có $10-3=7$ hàng, và tổng xác suất của từng cặp $(s,a)$ bằng $1$: $\alpha+(1-\alpha)$ cho $(\text{cao},\text{tìm})$, $\beta+(1-\beta)$ cho $(\text{thấp},\text{tìm})$, $1$ cho ba cặp còn lại. Ba lỗi thường gặp: giữ các hàng xác suất $0$; ghi $r_{\text{tìm}}$ cho hàng pin cạn thay cho $-3$; và ghi trạng thái kế tiếp của hàng pin cạn là thấp, quên rằng pin được sạc lại lên mức cao.
:::

### Bài tập 02.17. Lợi tức tính ngược

**Mức độ:** tính toán; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.8, §3.3, trang 56.

::: exercise Bài tập 02.17 (Lợi tức tính ngược)
Một lượt kết thúc tại $T=5$ với $\gamma=0{,}5$ và dãy phần thưởng $R_1=-1$, $R_2=2$, $R_3=6$, $R_4=3$, $R_5=2$.

- (a) Tính $G_0,G_1,\dots,G_5$.
- (b) Kiểm tra $G_0$ bằng cách cộng trực tiếp theo (4.5).
:::

::: hint Gợi ý Bài tập 02.17
Tính ngược từ $G_5=0$ bằng $G_t=R_{t+1}+\gamma G_{t+1}$ (Mệnh đề 02.13(a)).
:::

::: solution Lời giải Bài tập 02.17
**Câu (a).** Lượt kết thúc tại $T=5$, nên $G_5=0$. Theo Mệnh đề 02.13(a), $G_t=R_{t+1}+0{,}5\,G_{t+1}$:
$$
\begin{aligned}
G_4&=2+0{,}5\cdot0=2,\\
G_3&=3+0{,}5\cdot2=4,\\
G_2&=6+0{,}5\cdot4=8,\\
G_1&=2+0{,}5\cdot8=6,\\
G_0&=-1+0{,}5\cdot6=2.
\end{aligned}
$$

**Câu (b).** Theo (4.5) với $t=0$, $T=5$:
$$
\begin{aligned}
G_0&=-1+0{,}5\cdot2\\
&\quad+0{,}25\cdot6+0{,}125\cdot3\\
&\quad+0{,}0625\cdot2\\
&=-1+1+1{,}5\\
&\quad+0{,}375+0{,}125\\
&=2 .
\end{aligned}
$$

**Kiểm tra lại.** Hai cách cho cùng $G_0=2$. Hai lỗi thường gặp: bắt đầu từ $G_5=R_5=2$ thay cho $G_5=0$, khi đó phần thưởng $R_5$ bị đếm hai lần; và ghép $R_t$ với $G_t$, viết $G_t=R_t+\gamma G_{t+1}$, làm lệch mọi giá trị một bước và đòi một $R_0$ không tồn tại.
:::

### Bài tập 02.18. Lợi tức của phần thưởng hằng

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.10, §3.3, trang 56; đẳng thức (3.10), trang 55.

::: exercise Bài tập 02.18 (Lợi tức của phần thưởng hằng)
Trong một nhiệm vụ tiếp diễn, phần thưởng ở mọi bước bằng hằng số $+1$ và $0\le\gamma<1$. Sách viết, ở đẳng thức (3.10),
$$
G_t=\sum_{k=0}^{\infty}\gamma^k=\frac{1}{1-\gamma}.
$$

- (a) Chứng minh đẳng thức thứ hai qua tổng riêng của chuỗi.
- (b) Chứng minh lại $G_t=1/(1-\gamma)$ bằng hệ thức truy hồi của Mệnh đề 02.13(a), và nêu điều kiện mà cách này cần.
:::

::: hint Gợi ý Bài tập 02.18
Ở câu (a), đặt $Z_n=\sum_{k=0}^{n-1}\gamma^k$ và tính $Z_n-\gamma Z_n$. Ở câu (b), so sánh chuỗi phần thưởng tạo nên $G_{t+1}$ với chuỗi tạo nên $G_t$.
:::

::: solution Lời giải Bài tập 02.18
**Câu (a).** Với $n\ge1$,
$$
\begin{aligned}
Z_n-\gamma Z_n&=\sum_{k=0}^{n-1}\gamma^k-\sum_{k=1}^{n}\gamma^k\\
&=1-\gamma^n,
\end{aligned}
$$
vì mọi số hạng từ $\gamma^1$ tới $\gamma^{n-1}$ triệt tiêu. Do $\gamma\ne1$, $Z_n=(1-\gamma^n)/(1-\gamma)$. Với $0\le\gamma<1$, $\gamma^n\to0$ khi $n\to\infty$, nên $Z_n\to1/(1-\gamma)$. Tổng của chuỗi là giới hạn của tổng riêng, nên $\sum_{k=0}^{\infty}\gamma^k=1/(1-\gamma)$.

**Câu (b).** Phần thưởng bị chặn bởi $R_{\max}=1$ và $\gamma<1$, nên theo Mệnh đề 02.13(b), $G_t$ là một số hữu hạn. Chuỗi phần thưởng từ thời điểm $t+2$ trở đi cũng là $1,1,\dots$, nên $G_{t+1}=G_t$. Thế vào Mệnh đề 02.13(a):
$$
\begin{aligned}
&G_t=1+\gamma G_t\\
\iff{}&(1-\gamma)G_t=1\\
\iff{}&G_t=\frac{1}{1-\gamma}.
\end{aligned}
$$
Cách này cần biết trước $G_t$ hữu hạn. Với $\gamma=1$, phương trình $G=1+G$ không có nghiệm thực, và tổng riêng thứ $n$ bằng $n$, tiến về $+\infty$.

**Kiểm tra lại.** Với $\gamma=0$, công thức cho $G_t=1=R_{t+1}$; với $\gamma=0{,}9$, $G_t=10$. Hai lỗi thường gặp: dùng $\gamma^n\to0$ khi $\gamma=1$; và giải phương trình ở câu (b) mà không kiểm trước rằng $G_t$ hữu hạn.
:::

### Bài tập 02.19. Lợi tức của một chuỗi vô hạn

**Mức độ:** tính toán; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.9, §3.3, trang 56.

::: exercise Bài tập 02.19 (Lợi tức của một chuỗi vô hạn)
Với $\gamma=0{,}9$, dãy phần thưởng là $R_1=2$ rồi vô hạn số $7$, tức $R_k=7$ với mọi $k\ge2$.

- (a) Tính $G_1$ và $G_0$.
- (b) So sánh $G_1$ và $G_0$ với chặn (4.7), lấy $R_{\max}=7$.
:::

::: hint Gợi ý Bài tập 02.19
$G_1=\sum_{k\ge0}\gamma^kR_{k+2}$ chỉ gồm các số $7$; dùng kết quả của Bài tập 02.18 nhân với $7$.
:::

::: solution Lời giải Bài tập 02.19
**Câu (a).** Các phần thưởng $R_2,R_3,\dots$ đều bằng $7$, nên theo Bài tập 02.18,
$$
\begin{aligned}
G_1&=\sum_{k=0}^{\infty}0{,}9^k\cdot7\\
&=\frac{7}{1-0{,}9}=70 .
\end{aligned}
$$
Theo Mệnh đề 02.13(a), $G_0=R_1+\gamma G_1=2+0{,}9\cdot70=65$.

**Câu (b).** Chặn (4.7) là $R_{\max}/(1-\gamma)=7/0{,}1=70$. $G_1=70$ đạt đúng chặn, vì mọi phần thưởng sau $t=1$ bằng $R_{\max}$ (phần Phạm vi của Mệnh đề 02.13). $G_0=65<70$, vì $R_1=2<7$.

**Kiểm tra lại.** Cộng trực tiếp: $G_0=2+7\sum_{k\ge1}0{,}9^k=2+7\cdot\dfrac{0{,}9}{0{,}1}=2+63=65$. Hai lỗi thường gặp: tính $G_1$ có cả $R_1$, trong khi $G_1$ bắt đầu từ $R_2$; và viết $G_0=R_1+G_1=72$, quên nhân $\gamma$ vào $G_1$.
:::

### Bài tập 02.20. Kỳ vọng của phần thưởng kế tiếp theo chính sách và hàm động lực

**Mức độ:** tính toán; mục tiêu học tập 3 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.11, §3.5, trang 58; câu (b) dùng dữ kiện của Ví dụ 3.3, trang 52.

::: exercise Bài tập 02.20 (Kỳ vọng của phần thưởng kế tiếp theo chính sách và hàm động lực)
Trạng thái hiện tại là $S_t=s$, và tác tử chọn hành động theo một chính sách ngẫu nhiên $\pi(a\mid s)$ (Định nghĩa 02.8, với biểu diễn là trạng thái). Môi trường có hàm động lực $p(s',r\mid s,a)$ (Định nghĩa 02.16).

- (a) Viết $\mathbb E_\pi[R_{t+1}\mid S_t=s]$ theo $\pi$ và $p$.
- (b) Áp dụng cho robot thu gom lon của Ví dụ 3.3 của sách. Trạng thái là mức pin, cao hoặc thấp; $\mathcal A(\text{cao})=\{\text{tìm},\text{chờ}\}$, $\mathcal A(\text{thấp})=\{\text{tìm},\text{chờ},\text{sạc}\}$. Tìm từ mức cao: pin giữ mức cao với xác suất $\alpha$, xuống thấp với xác suất $1-\alpha$, cả hai trường hợp có phần thưởng kỳ vọng $r_{\text{tìm}}$. Tìm từ mức thấp: pin giữ mức thấp với xác suất $\beta$, phần thưởng kỳ vọng $r_{\text{tìm}}$; pin cạn với xác suất $1-\beta$, robot được cứu, pin được sạc lại lên mức cao và nhận $-3$. Chờ: mức pin giữ nguyên, phần thưởng kỳ vọng $r_{\text{chờ}}$. Sạc từ mức thấp: pin lên mức cao, nhận $0$. Ở đây $r_{\text{tìm}}>r_{\text{chờ}}$ là số lon kỳ vọng thu được khi tìm và khi chờ. Viết $\mathbb E_\pi[R_{t+1}\mid S_t=\text{cao}]$ và $\mathbb E_\pi[R_{t+1}\mid S_t=\text{thấp}]$ theo $\pi$, $\alpha$, $\beta$, $r_{\text{tìm}}$, $r_{\text{chờ}}$.
:::

::: hint Gợi ý Bài tập 02.20
Theo quy tắc nhân, $\Pr(A_t=a,S_{t+1}=s',R_{t+1}=r\mid S_t=s)=\pi(a\mid s)\,p(s',r\mid s,a)$.
:::

::: solution Lời giải Bài tập 02.20
**Câu (a).** Tác tử chọn $A_t=a$ với xác suất $\pi(a\mid s)$ (công thức (3.2) của ghi chú với $X_t=S_t$); khi đã biết $S_t=s$ và $A_t=a$, cặp $(S_{t+1},R_{t+1})$ có phân phối $p(\cdot,\cdot\mid s,a)$ theo (4.9). Vì vậy xác suất đồng thời trong gợi ý đúng, và theo định nghĩa kỳ vọng của biến rời rạc,
$$
\begin{aligned}
&\mathbb E_\pi[R_{t+1}\mid S_t=s]\\
&\quad=\sum_{a}\pi(a\mid s)\\
&\qquad\times\sum_{s'}\sum_{r}r\,p(s',r\mid s,a),
\end{aligned}
$$
với các tổng lấy theo $a\in\mathcal A(s)$, $s'\in\mathcal S^+$, $r\in\mathcal R$. Tổng hai lớp bên trong là $r(s,a)$ theo định nghĩa sau Định nghĩa 02.16, nên $\mathbb E_\pi[R_{t+1}\mid S_t=s]=\sum_a\pi(a\mid s)\,r(s,a)$.

**Câu (b).** Lấy kỳ vọng theo trạng thái kế tiếp, $r(s,a)=\sum_{s'}p(s'\mid s,a)\,r(s,a,s')$, với $r(s,a,s')$ là phần thưởng kỳ vọng của từng chuyển. Thưởng kỳ vọng một bước của từng cặp:

- $r(\text{cao},\text{tìm})=r_{\text{tìm}}$, vì cả hai kết cục của $(\text{cao},\text{tìm})$ cùng có phần thưởng kỳ vọng $r_{\text{tìm}}$;
- $r(\text{thấp},\text{tìm})=\beta\,r_{\text{tìm}}-3(1-\beta)$, trung bình của $r_{\text{tìm}}$ và $-3$ với trọng số $\beta$ và $1-\beta$;
- $r(\text{cao},\text{chờ})=r(\text{thấp},\text{chờ})=r_{\text{chờ}}$;
- $r(\text{thấp},\text{sạc})=0$.

Thế vào câu (a):
$$
\begin{aligned}
&\mathbb E_\pi[R_{t+1}\mid S_t=\text{cao}]\\
&\quad=\pi(\text{tìm}\mid\text{cao})\,r_{\text{tìm}}\\
&\qquad+\pi(\text{chờ}\mid\text{cao})\,r_{\text{chờ}},\\
&\mathbb E_\pi[R_{t+1}\mid S_t=\text{thấp}]\\
&\quad=\pi(\text{tìm}\mid\text{thấp})\\
&\qquad\times\bigl(\beta\,r_{\text{tìm}}-3(1-\beta)\bigr)\\
&\qquad+\pi(\text{chờ}\mid\text{thấp})\,r_{\text{chờ}}.
\end{aligned}
$$
Hành động sạc và xác suất $\alpha$ không có mặt trong kết quả, vì $r(\text{thấp},\text{sạc})=0$ và $r(\text{cao},\text{tìm})=r_{\text{tìm}}$.

**Kiểm tra lại.** Với chính sách luôn chờ ở cả hai mức pin, hai kỳ vọng đều bằng $r_{\text{chờ}}$, đúng phần thưởng kỳ vọng của hành động chờ. Hai lỗi thường gặp: lấy trung bình cộng các $r(s,a)$ thay cho trung bình có trọng số $\pi(a\mid s)$; và bỏ kết cục pin cạn ở $(\text{thấp},\text{tìm})$, cho $\beta\,r_{\text{tìm}}$ thay cho $\beta\,r_{\text{tìm}}-3(1-\beta)$.
:::

### Bài tập 02.21. Cộng một hằng số vào mọi phần thưởng của nhiệm vụ tiếp diễn

**Mức độ:** chứng minh; mục tiêu học tập 4 và 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.15, §3.5, trang 61; dữ kiện của Ví dụ 3.5, trang 60.

::: exercise Bài tập 02.21 (Cộng một hằng số vào mọi phần thưởng của nhiệm vụ tiếp diễn)
Ví dụ 3.5 của sách: lưới ô $5\times5$, mỗi ô là một trạng thái; bốn hành động Bắc, Nam, Đông, Tây đưa tác tử sang ô kề theo hướng đó một cách tất định. Hành động đưa tác tử ra ngoài lưới giữ nguyên vị trí và nhận $-1$. Tại ô đặc biệt $\mathrm A$, mọi hành động đưa tác tử tới ô $\mathrm A'$ và nhận $+10$; tại ô đặc biệt $\mathrm B$, mọi hành động đưa tác tử tới ô $\mathrm B'$ và nhận $+5$. Các bước khác nhận $0$. Đây là nhiệm vụ tiếp diễn với $\gamma=0{,}9$, lợi tức theo (4.6). Như vậy phần thưởng dương ở hai ô đặc biệt, âm khi đâm biên và bằng $0$ ở các bước còn lại. Cộng một hằng số $\kappa$ (sách viết $c$) vào mọi phần thưởng; ký hiệu $G'_t$ và $v'_\pi$ là lợi tức và giá trị sau khi cộng.

- (a) Chứng minh rằng với mọi chính sách $\pi$ và mọi trạng thái $s$, $v'_\pi(s)=v_\pi(s)+v_\kappa$ với một hằng số $v_\kappa$ không phụ thuộc $\pi$ và $s$; tính $v_\kappa$ theo $\kappa$ và $\gamma$.
- (b) Suy ra rằng phép cộng này không đổi hiệu giá trị giữa hai trạng thái dưới cùng một chính sách, cũng không đổi thứ tự giữa hai chính sách tại một trạng thái. Cho biết dấu của các phần thưởng có quan trọng không, hay chỉ khoảng cách giữa chúng.
- (c) Tính $v_\kappa$ với $\gamma=0{,}9$ của ví dụ.
:::

::: hint Gợi ý Bài tập 02.21
Tách $\sum_k\gamma^k(R_{k+1}+\kappa)$ thành hai chuỗi hội tụ tuyệt đối và dùng Bài tập 02.18 nhân với $\kappa$; sau đó lấy kỳ vọng.
:::

::: solution Lời giải Bài tập 02.21
**Câu (a).** Mọi phần thưởng cũ thỏa $\lvert R_{t+1}\rvert\le10$, nên phần thưởng mới bị chặn bởi $10+\lvert\kappa\rvert$, và theo Mệnh đề 02.13(b), cả $G_0$ lẫn $G'_0$ hội tụ tuyệt đối. Trên mọi quỹ đạo,
$$
\begin{aligned}
G'_0&=\sum_{k=0}^{\infty}\gamma^k\bigl(R_{k+1}+\kappa\bigr)\\
&=\sum_{k=0}^{\infty}\gamma^kR_{k+1}+\kappa\sum_{k=0}^{\infty}\gamma^k\\
&=G_0+\frac{\kappa}{1-\gamma}.
\end{aligned}
$$
Dòng thứ nhất là (4.6) với phần thưởng mới; dòng thứ hai tách hai chuỗi hội tụ tuyệt đối; dòng thứ ba dùng (4.6) và Bài tập 02.18. Phép cộng không đổi luật chuyển và chính sách, nên khi xuất phát tại $S_0=s$, dãy trạng thái và hành động có cùng phân phối như trước. Lấy kỳ vọng hai vế khi $S_0=s$; cả hai kỳ vọng hữu hạn theo (4.7), và $\mathbb E_\pi[G_0\mid S_0=s]=v_\pi(s)$ theo (4.8), nên
$$
v'_\pi(s)=v_\pi(s)+\frac{\kappa}{1-\gamma}.
$$
Vậy $v_\kappa=\kappa/(1-\gamma)$.

**Câu (b).** Với hai trạng thái $s$, $\tilde s$ và cùng chính sách $\pi$: $v'_\pi(s)-v'_\pi(\tilde s)=v_\pi(s)-v_\pi(\tilde s)$. Với hai chính sách $\pi$, $\pi'$ tại cùng $s$: $v'_\pi(s)-v'_{\pi'}(s)=v_\pi(s)-v_{\pi'}(s)$, nên thứ tự giữa hai chính sách giữ nguyên. Trong nhiệm vụ tiếp diễn, dấu của các phần thưởng không quan trọng; chỉ khoảng cách giữa chúng quyết định thứ tự. Chẳng hạn, với $\kappa=1$, các phần thưởng $-1$, $0$, $+5$, $+10$ thành $0$, $1$, $6$, $11$, và mọi thứ tự giữa các chính sách giữ nguyên.

**Câu (c).** $v_\kappa=\kappa/(1-0{,}9)=10\kappa$.

**Kiểm tra lại.** Nếu mọi phần thưởng cũ bằng $0$, câu (a) cho $v'_\pi=\kappa/(1-\gamma)$, đúng lợi tức của chuỗi hằng $\kappa$ theo Bài tập 02.18. Ba lỗi thường gặp: chỉ cộng $\kappa$ vào các phần thưởng khác $0$; quên chiết khấu, cho $v_\kappa=\kappa$; và áp kết luận cho nhiệm vụ có lượt, nơi số bước khác nhau giữa các quỹ đạo (Bài tập 02.24).
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 02.22. Bài toán giữ cột: lượt có chiết khấu và dạng tiếp diễn

**Mức độ:** vận dụng; mục tiêu học tập 4 và 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.6, §3.3, trang 56; dữ kiện của Ví dụ 3.4, trang 56.

::: exercise Bài tập 02.22 (Bài toán giữ cột: lượt có chiết khấu và dạng tiếp diễn)
Ví dụ 3.4 của sách (giữ cột trên xe, pole-balancing): tác tử tác dụng lực lên một xe chạy trên đường ray để giữ cây cột gắn bản lề trên xe không đổ. Thất bại xảy ra khi cột nghiêng quá một góc cho trước so với phương thẳng đứng hoặc khi xe chạy ra khỏi đường ray; sau mỗi lần thất bại, cột được dựng lại thẳng đứng. Sách nêu một cách mô hình hóa dạng tiếp diễn có chiết khấu: phần thưởng $-1$ ở mỗi bước thất bại và $0$ ở mọi bước khác.

Coi bài toán là nhiệm vụ có lượt, mỗi lượt kết thúc ở bước thất bại $T$, và vẫn dùng chiết khấu với $0<\gamma<1$: mọi phần thưởng bằng $0$, trừ $R_T=-1$.

- (a) Tính lợi tức $G_t$ với $0\le t<T$.
- (b) Trong dạng tiếp diễn, gọi $K_1<K_2<\cdots$ là các bước thất bại. Viết $G_t$ và nêu khác biệt với lợi tức ở câu (a).
- (c) Chứng minh rằng với $t$ cố định, lợi tức ở câu (a) tăng ngặt theo $T$. Cho biết lợi tức ở câu (a) ra sao khi $\gamma=1$.
:::

::: hint Gợi ý Bài tập 02.22
Phần thưởng $R_{t+k+1}$ có trọng số $\gamma^k$ trong $G_t$, nên phần thưởng của bước $T$ ứng với $k=T-t-1$.
:::

::: solution Lời giải Bài tập 02.22
**Câu (a).** Trong tổng (4.5) chỉ số hạng $k=T-t-1$ khác $0$:
$$
G_t=\gamma^{T-t-1}R_T=-\gamma^{T-t-1}.
$$

**Câu (b).** Theo (4.6), $R_j=-1$ khi $j$ là một bước thất bại và $R_j=0$ ở các bước khác, nên
$$
G_t=-\sum_{i:\,K_i>t}\gamma^{K_i-t-1}.
$$
Chuỗi hội tụ vì $\lvert R_j\rvert\le1$ và $\gamma<1$ (Mệnh đề 02.13(b)). Lợi tức có lượt chỉ tính lần thất bại đầu tiên sau $t$; lợi tức tiếp diễn có cùng số hạng đầu $-\gamma^{K_j-t-1}$, với $K_j$ là bước thất bại đầu tiên sau $t$, cộng thêm các số hạng âm của những lần thất bại về sau. Sách viết lợi tức dạng tiếp diễn liên hệ với $-\gamma^{K-1}$; với $K=T-t$ là số bước từ $t$ tới lần thất bại, kể cả bước thất bại, số hạng này là $-\gamma^{T-t-1}$ của câu (a).

**Câu (c).** Với $0<\gamma<1$, $\gamma^{T-t-1}$ giảm ngặt khi $T$ tăng, nên $-\gamma^{T-t-1}$ tăng ngặt: lượt giữ cột lâu hơn có lợi tức lớn hơn. Khi $\gamma=1$, $G_t=-1$ với mọi $T$, nên mọi lượt có cùng lợi tức và tiêu chí không phân biệt việc giữ cột lâu hay chóng thất bại; cách thưởng này của dạng có lượt cần $\gamma<1$.

**Kiểm tra lại.** Với $t=T-1$, câu (a) cho $G_{T-1}=-1=R_T$. Theo Mệnh đề 02.13(a), $G_{T-2}=R_{T-1}+\gamma G_{T-1}=0+\gamma\cdot(-1)=-\gamma$, khớp $-\gamma^{T-t-1}$ với $t=T-2$. Hai lỗi thường gặp: dùng trọng số $\gamma^{T-t}$ cho bước thất bại, lệch một bậc; và ở dạng tiếp diễn chỉ tính lần thất bại đầu tiên.
:::

### Bài tập 02.23. Robot thoát mê cung không cải thiện

**Mức độ:** vận dụng; mục tiêu học tập 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.7, §3.3, trang 56.

::: exercise Bài tập 02.23 (Robot thoát mê cung không cải thiện)
Một robot được thiết kế để chạy qua mê cung, nhận phần thưởng $+1$ ở bước thoát khỏi mê cung và $0$ ở mọi bước khác. Mỗi lần chạy qua mê cung là một lượt, kết thúc khi robot thoát, và mục tiêu là làm lớn nhất kỳ vọng của tổng phần thưởng $G_t=R_{t+1}+R_{t+2}+\cdots+R_T$ (đẳng thức (3.7) của sách, tức (4.5) với $\gamma=1$). Sau một thời gian chạy tác tử học, khả năng thoát khỏi mê cung của robot không được cải thiện.

- (a) Tính lợi tức $G_0$ của một lượt thoát sau $k$ bước, $k\ge1$, và lợi tức của một quỹ đạo không bao giờ thoát.
- (b) Giải thích nguyên nhân, và cho biết phần thưởng đã truyền đạt đúng điều người thiết kế muốn hay chưa.
:::

::: hint Gợi ý Bài tập 02.23
Viết chuỗi phần thưởng của một đường thoát dài $k$ bước, rồi xét những chính sách nào đạt kỳ vọng lợi tức lớn nhất.
:::

::: solution Lời giải Bài tập 02.23
**Câu (a).** Đường thoát dài $k$ bước có $k-1$ phần thưởng $0$ rồi phần thưởng $1$, nên $G_0=(k-1)\cdot0+1=1$ với mọi $k\ge1$. Quỹ đạo không bao giờ thoát có mọi tổng riêng bằng $0$, nên theo quy ước giới hạn tổng riêng, lợi tức bằng $0$.

**Câu (b).** Theo câu (a), lợi tức chỉ nhận hai giá trị $1$ và $0$, nên kỳ vọng lợi tức của một chính sách bằng xác suất thoát của nó. Mọi chính sách thoát với xác suất $1$, dù đường thoát ngắn hay dài, đều có kỳ vọng $1$, giá trị lớn nhất có thể. Khi tác tử đã đạt mức đó, tiêu chí không phân biệt đường ngắn với đường dài, nên việc học không có lý do rút ngắn đường. Phần thưởng chỉ truyền đạt "thoát khỏi mê cung", không truyền đạt "thoát nhanh". Muốn tác tử thoát nhanh, cách đánh giá phải làm đường ngắn có lợi tức lớn hơn, chẳng hạn phần thưởng $-1$ ở mỗi bước như mê cung $8\times8$ của ghi chú (Ví dụ 02.3), cho $G_0=-k$, hoặc chiết khấu với $\gamma<1$, cho $G_0=\gamma^{k-1}$.

**Kiểm tra lại.** Với $k=1$, $G_0=R_1=1$. Hai lỗi thường gặp: cho rằng phần thưởng trễ là nguyên nhân, trong khi với $\gamma<1$ cùng phần thưởng trễ đó đã phân biệt được độ dài đường; và dùng trọng số $\gamma^k$ cho phần thưởng ở bước thứ $k$, thay cho $\gamma^{k-1}$.
:::

### Bài tập 02.24. Cộng một hằng số vào mọi phần thưởng của nhiệm vụ có lượt

**Mức độ:** vận dụng; mục tiêu học tập 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.16, §3.5, trang 61.

::: exercise Bài tập 02.24 (Cộng một hằng số vào mọi phần thưởng của nhiệm vụ có lượt)
Xét một nhiệm vụ có lượt, chẳng hạn chạy mê cung, với hệ số chiết khấu $\gamma\in[0,1]$ và lượt kết thúc tại $T$. Cộng một hằng số $\kappa$ (sách viết $c$) vào mọi phần thưởng, kể cả phần thưởng của bước cuối; ký hiệu $G'_t$ là lợi tức sau khi cộng.

- (a) Chứng minh $G'_0=G_0+\kappa\sum_{k=0}^{T-1}\gamma^k$, tức $G'_0=G_0+\kappa T$ khi $\gamma=1$ và $G'_0=G_0+\kappa(1-\gamma^T)/(1-\gamma)$ khi $\gamma<1$.
- (b) Cho biết phép cộng này có làm thay đổi nhiệm vụ không, hay giữ nguyên nhiệm vụ như ở nhiệm vụ tiếp diễn (Bài tập 02.21), và giải thích.
- (c) Nêu một ví dụ.
:::

::: hint Gợi ý Bài tập 02.24
Tổng (4.5) với $t=0$ có đúng $T$ số hạng, và $T$ khác nhau giữa các quỹ đạo.
:::

::: solution Lời giải Bài tập 02.24
**Câu (a).** Theo (4.5) với $t=0$,
$$
\begin{aligned}
G'_0&=\sum_{k=0}^{T-1}\gamma^k\bigl(R_{k+1}+\kappa\bigr)\\
&=G_0+\kappa\sum_{k=0}^{T-1}\gamma^k .
\end{aligned}
$$
Tổng $\sum_{k=0}^{T-1}\gamma^k$ bằng $T$ khi $\gamma=1$ và bằng $(1-\gamma^T)/(1-\gamma)$ khi $\gamma<1$ (tổng hình học).

**Câu (b).** Phép cộng làm thay đổi nhiệm vụ khi độ dài lượt khác nhau giữa các quỹ đạo. Lượng cộng thêm $\kappa\sum_{k=0}^{T-1}\gamma^k$ phụ thuộc $T$, nên hai quỹ đạo dài khác nhau được dịch những lượng khác nhau, và thứ tự lợi tức giữa chúng, do đó thứ tự giữa các chính sách, có thể đổi. Với $\kappa>0$, quỹ đạo dài được cộng nhiều hơn; với $\kappa<0$, quỹ đạo ngắn được lợi. Trong nhiệm vụ tiếp diễn, lượng cộng thêm là hằng số $\kappa/(1-\gamma)$ cho mọi quỹ đạo (Bài tập 02.21), nên thứ tự giữ nguyên.

**Câu (c).** Mê cung $8\times8$ của ghi chú: phần thưởng $-1$ mỗi bước, kể cả bước vào đích $\mathrm G$, $\gamma=1$. Đường 16 bước có $G_0=-16$, đường 18 bước có $G_0=-18$ (Ví dụ 02.3), nên tác tử cực đại lợi tức chọn đường ngắn.

- $\kappa=1$: mọi phần thưởng bằng $0$. Theo câu (a), cả hai đường có $G'_0=0$; quỹ đạo luôn chọn Tây tại ô xuất phát $(0,2)$, tức đứng yên mãi, có mọi tổng riêng bằng $0$ và lợi tức $0$. Tiêu chí không còn ưu tiên việc tới $\mathrm G$.
- $\kappa=2$: mọi phần thưởng bằng $+1$. Đường 16 bước có $G'_0=-16+2\cdot16=16$, đường 18 bước có $-18+2\cdot18=18$, và quỹ đạo đứng yên mãi có tổng riêng $n\to+\infty$. Thứ tự giữa hai đường đảo ngược, và tác tử cực đại lợi tức không bao giờ tới $\mathrm G$.

**Kiểm tra lại.** Với $\kappa=2$, đường 16 bước gồm $16$ phần thưởng $+1$, cộng trực tiếp được $16$, khớp câu (a). Hai lỗi thường gặp: áp kết luận của Bài tập 02.21 cho nhiệm vụ có lượt, bỏ qua việc $T$ khác nhau giữa các quỹ đạo; và chỉ cộng $\kappa$ vào các bước chưa kết thúc, quên bước cuối, khi đó đường 16 bước với $\kappa=2$ cho $14$ thay cho $16$.
:::

## Tài liệu tham khảo

- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 3.3, §3.1, trang 51 (Bài tập 02.14); Bài tập 3.4, §3.1, trang 53, và Ví dụ 3.3, trang 52 (Bài tập 02.16, 02.20); Bài tập 3.5, §3.3, trang 55 (Bài tập 02.15); Bài tập 3.6–3.10, §3.3, trang 56, và Ví dụ 3.4, trang 56 (Bài tập 02.22, 02.23, 02.17, 02.19, 02.18); Bài tập 3.11, §3.5, trang 58 (Bài tập 02.20); Bài tập 3.15, 3.16, §3.5, trang 61, và Ví dụ 3.5, trang 60 (Bài tập 02.21, 02.24).
