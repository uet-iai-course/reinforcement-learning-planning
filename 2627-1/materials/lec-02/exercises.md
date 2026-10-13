# Bài tập Bài 02 — Giao diện tác tử–môi trường

Bộ bài tập chính thức của Bài 02 gồm hai mươi hai bài, đánh số chung với [ghi chú bài giảng](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html); tệp này chứa mười sáu bài. Bảy bài 02.1–02.5, 02.7 và 02.8 là bài tập trong thân ghi chú có trang "Bài tập" trên bộ trang chiếu: chúng giữ số hiệu và lời giải của ghi chú, đề bài được phát biểu lại với đủ dữ kiện, và dòng "Trùng trang chiếu" dẫn tới trang câu hỏi và trang lời giải. Chín bài 02.14–02.22 chỉ có ở tệp này; trong đó Bài tập 02.21 trùng bài tập tổng hợp của mạch 7. Lời giải của mọi bài trùng trang chiếu cho cùng kết quả với lời giải trên trang. Bài tập 02.6 và năm bài 02.9–02.13 của mục "Bài tập củng cố" chỉ có trong ghi chú; bảng dưới ghi chúng sau chữ "ghi chú". Trong tệp, các bài chia theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường (reinforcement learning).

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/1/1) | — |
| 2. Vòng tương tác và tín hiệu thưởng | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/2/1) | 02.1, 02.14 |
| 3. Thông tin khả dụng và tính Markov | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/3/1) | 02.2, 02.3, 02.15; [ghi chú](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html): 02.11 |
| 4. Quy tắc chọn hành động | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/4/1) | 02.4, 02.19; [ghi chú](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html): 02.13 |
| 5. Lợi tức, hàm giá trị và hàm động lực | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/5/1) | 02.5, 02.7, 02.16, 02.17; [ghi chú](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html): 02.6, 02.9, 02.10(a), 02.12 |
| 6. Thiết kế phần thưởng | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/6/1) | 02.8, 02.18, 02.20; [ghi chú](material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html): 02.10(b) |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-02-giao-dien-tac-tu-moi-truong.html#/7/1) | 02.21, 02.22 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 02; các công thức được dẫn bằng số trong đề được phát biểu lại dưới đây. Tác tử (agent) ở thời điểm $t$ có quan sát (observation) $O_t$ và chọn hành động (action) $A_t$; môi trường (environment), với trạng thái (state) $S_t$, trả phần thưởng (reward) $R_{t+1}$ và quan sát $O_{t+1}$. Bộ $(O_t,A_t,R_{t+1},O_{t+1})$ là một mẫu chuyển (transition), nên phần thưởng của chuyển từ $t$ sang $t+1$ mang chỉ số $t+1$ (Định nghĩa 02.1). Biểu diễn (representation) là dữ liệu tác tử tự tính để chọn hành động, một hàm tất định $f_t$ của dữ liệu khả dụng:
$$
X_t=f_t\bigl(O_{0:t},A_{0:t-1},R_{1:t}\bigr).
\tag{2.1}
$$
Môi trường được quan sát đầy đủ (full observability) khi có hàm $g$ với $S_t=g(O_t)$ ở mọi $t$, và được quan sát một phần (partial observability) khi một quan sát ứng với hai trạng thái khác nhau có thể xảy ra (Nhận xét 02.4). Với lịch sử trạng thái $H_t=(S_0,A_0,R_1,\dots,R_t,S_t)$, trạng thái có tính Markov (Markov property) khi, với mọi chính sách, mọi $t$, mọi lịch sử $h$ kết thúc tại $s$ và mọi $a$ với $\Pr(H_t=h,A_t=a)>0$,
$$
\begin{aligned}
&\Pr\bigl(S_{t+1}=s',R_{t+1}=r\mid H_t=h,A_t=a\bigr)\\
&\quad=\Pr\bigl(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a\bigr)
\end{aligned}
\tag{2.3}
$$
(Định nghĩa 02.5); định nghĩa áp cho mọi dãy biến được chọn làm trạng thái.

Một lượt (episode) kết thúc tại $T$; lợi tức (return) với hệ số chiết khấu (discount factor) $\gamma\in[0,1]$ là
$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1},\qquad G_T=0 .
\tag{4.5}
$$
Với nhiệm vụ tiếp diễn (continuing task), $T=\infty$, cần thêm $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$ với mọi $t$, và
$$
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}
\tag{4.6}
$$
(Định nghĩa 02.12). Hệ thức truy hồi $G_t=R_{t+1}+\gamma G_{t+1}$ là Mệnh đề 02.13(a). Khi $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$, chuỗi (4.6) hội tụ tuyệt đối và
$$
\lvert G_t\rvert\le\frac{R_{\max}}{1-\gamma}
\tag{4.7}
$$
(Mệnh đề 02.13(b)). Khi $\gamma=1$ và một quỹ đạo không kết thúc, lợi tức của nó là giới hạn của tổng riêng khi giới hạn tồn tại, có thể bằng $\pm\infty$ (Mục 4.2 của ghi chú).

Chính sách (policy) $\pi(a\mid x)$ là phân phối trên các hành động hợp lệ cho mỗi giá trị $x$ của biểu diễn $X_t$ (Định nghĩa 02.8). Hàm giá trị trạng thái (state-value function) là $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$, với kỳ vọng lấy theo cả chính sách và động lực của môi trường, và giá trị của trạng thái kết thúc bằng $0$ (Định nghĩa 02.14). Hàm động lực (dynamics function) là $p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$, công thức (4.9); từ nó suy ra xác suất chuyển (transition probability) $p(s'\mid s,a)=\sum_rp(s',r\mid s,a)$ và thưởng kỳ vọng một bước (expected reward) $r(s,a)=\sum_{s'}\sum_rr\,p(s',r\mid s,a)$ (Định nghĩa 02.16).

**Mê cung $8\times8$** (bài giảng gốc, trang 25–26). Ô ghi bằng tọa độ (cột, hàng), cả hai đánh số từ $0$, hàng tăng xuống dưới. Có 27 ô đi được: hàng $1$ gồm các cột $1$ tới $6$; hàng $2$ gồm các cột $0$, $1$, $4$, $6$; hàng $3$ gồm các cột $1$, $2$, $5$, $6$; hàng $4$ gồm các cột $2$, $3$, $5$; hàng $5$ gồm các cột $1$, $3$, $5$, $6$; hàng $6$ gồm các cột $1$, $2$, $3$, $4$, $6$, $7$; hàng $0$ và hàng $7$ toàn tường. Tác tử xuất phát tại $(0,2)$ và chọn Bắc, Đông, Nam hoặc Tây. Bước vào tường hoặc ra ngoài lưới giữ tác tử đứng yên, trừ bước Đông từ $(7,6)$, đưa tác tử vào đích $\mathrm G$ và kết thúc lượt. Mỗi bước nhận $-1$, kể cả bước vào $\mathrm G$. Mã bốn ô kề là bộ $(\text{Bắc},\text{Đông},\text{Nam},\text{Tây})\in\{0,1\}^4$, với chữ số $1$ khi bước theo hướng đó giữ tác tử đứng yên (Ví dụ 02.4).

**Mê cung đích–hố** (Ví dụ 02.14). Mười nút xếp thành một vòng khép kín. Hàng trên từ trái sang phải: xuất phát $\mathrm S$, một nút trống, hố $\mathrm H$, một nút trống, đích $\mathrm G$; hàng dưới có năm nút trống, nút đầu trái nối với $\mathrm S$, nút đầu phải nối với $\mathrm G$. Mỗi đoạn nối hai nút kề nhau là một bước; chuyển là tất định; $\mathrm H$ và $\mathrm G$ là trạng thái kết thúc. Đường ngắn nhất từ $\mathrm S$ tới $\mathrm H$ dài $2$ bước, tới $\mathrm G$ dài $6$ bước, và mọi đường tới $\mathrm G$ đi qua hàng dưới. Mỗi bước nhận $-c$ với chi phí $c\ge0$; bước vào $\mathrm G$ nhận thêm $+10$; bước vào $\mathrm H$ nhận thêm $-c_{\mathrm H}$ với $c_{\mathrm H}\ge0$, và $c_{\mathrm H}=0$ khi đề không nói gì. Với $\gamma=1$, ngưỡng của Mệnh đề 02.18 là $c^*=(10+c_{\mathrm H})/4$.

Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$; khi một bộ số có thành phần thập phân, các thành phần cách nhau bằng dấu chấm phẩy. Ngoài mê cung $8\times8$, chuỗi phần thưởng của Bài tập 02.17(b) và hành lang của Bài tập 02.19 (Sutton và Barto, 2018), mọi bộ số là số liệu sư phạm tự xây dựng. Lời giải nêu kết quả được dùng ở từng bước.

## Mức nhận biết

### Bài tập 02.1. Ghi một mẫu chuyển

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** ghi chú bài giảng, Mục 1.2 (Định nghĩa 02.1); mê cung $8\times8$ của bài giảng gốc, trang 25–26.

**Trùng trang chiếu:** [Bài tập: mẫu chuyển tại ô $(6,1)$](lecture-02-giao-dien-tac-tu-moi-truong.html#/2/6); câu hỏi và lời giải nằm trên cùng trang.

::: exercise Bài tập 02.1 (Ghi một mẫu chuyển)
Mê cung $8\times8$: bước vào tường hoặc ra ngoài lưới giữ tác tử đứng yên, phần thưởng $-1$ mỗi bước; quan sát là tọa độ (cột, hàng). Tác tử đi theo đường 16 bước, qua $(0,2)$, $(1,2)$, $(1,1)$, $(2,1)$, $(3,1)$, $(4,1)$, $(5,1)$, $(6,1)$, …, nên tại $t=7$ nó ở $(6,1)$. Ô $(6,2)$ trống, ô $(7,1)$ là tường.

- (a) Tại $t=7$ tác tử chọn Nam. Ghi mẫu chuyển $(O_7,A_7,R_8,O_8)$.
- (b) Nếu tại $t=7$ tác tử chọn Đông, ghi lại mẫu chuyển.
- (c) Phần thưởng của bước ở câu (a) mang chỉ số nào, và vì sao không phải $R_7$.
:::

::: hint Gợi ý Bài tập 02.1
Phần thưởng của chuyển từ $t$ sang $t+1$ mang chỉ số $t+1$. Đi vào tường thì đứng yên nhưng vẫn nhận phần thưởng.
:::

::: solution Lời giải Bài tập 02.1
**Câu (a).** $O_7=(6,1)$, $A_7=\text{Nam}$; ô $(6,2)$ trống nên tác tử tới đó, $R_8=-1$, $O_8=(6,2)$. Mẫu chuyển là $((6,1),\text{Nam},-1,(6,2))$.

**Câu (b).** Ô $(7,1)$ là tường, tác tử đứng yên: $((6,1),\text{Đông},-1,(6,1))$.

**Câu (c).** Chỉ số $8$, vì đây là chuyển từ $t=7$ sang $t=8$ (Định nghĩa 02.1); $R_7$ là phần thưởng của bước Đông từ $(5,1)$ ở $t=6$.

**Kiểm tra lại.** Hai mẫu chuyển ở (a) và (b) chỉ khác nhau ở hành động và quan sát sau; phần thưởng giống nhau. Hai lỗi thường gặp: ghi phần thưởng của $A_7$ là $R_7$, làm lệch mọi tổng về sau một bước; và bỏ mẫu chuyển ở câu (b) vì tác tử không đổi ô, trong khi bước đâm tường vẫn là một chuyển với $O_8=O_7$ và phần thưởng $-1$.
:::

### Bài tập 02.2. Mã bốn ô kề

**Mức độ:** nhận biết; mục tiêu học tập 2.

**Nguồn:** ghi chú bài giảng, Mục 2.1–2.4 (Ví dụ 02.4, Nhận xét 02.4); Bài tập tuần 2 (2025–2026), bài 2.

**Trùng trang chiếu:** [Bài tập: mã bốn ô kề](lecture-02-giao-dien-tac-tu-moi-truong.html#/3/8); câu hỏi và lời giải nằm trên cùng trang.

::: exercise Bài tập 02.2 (Mã bốn ô kề)
Mê cung $8\times8$, ô ghi bằng tọa độ (cột, hàng), hàng tăng xuống dưới. Ô đi được: hàng $1$ gồm các cột $1$ tới $6$; hàng $2$ gồm các cột $0$, $1$, $4$, $6$; hàng $3$ gồm các cột $1$, $2$, $5$, $6$; hàng $4$ gồm các cột $2$, $3$, $5$; hàng $0$ toàn tường; các ô còn lại của bốn hàng này là tường. Quan sát là mã bốn ô kề $(\text{Bắc},\text{Đông},\text{Nam},\text{Tây})$, với chữ số $1$ khi bước theo hướng đó giữ tác tử đứng yên và $0$ khi bước đưa tác tử sang ô khác. Theo Nhận xét 02.4, quan sát là đầy đủ khi có hàm $g$ với $S_t=g(O_t)$ ở mọi $t$, và là một phần khi một quan sát ứng với hai trạng thái khác nhau.

- (a) Tính mã tại $(1,2)$ và tại $(6,3)$.
- (b) Với trạng thái là tọa độ, phân loại hai cách quan sát, tọa độ và mã bốn ô kề, theo Nhận xét 02.4.
:::

::: hint Gợi ý Bài tập 02.2
Với mỗi ô, xét lần lượt bốn ô kề theo thứ tự Bắc, Đông, Nam, Tây. Ở câu (b), tìm hai ô trên hàng $1$ có cùng mã.
:::

::: solution Lời giải Bài tập 02.2
**Câu (a).** Tại $(1,2)$: Bắc $(1,1)$ trống, Đông $(2,2)$ tường, Nam $(1,3)$ trống, Tây $(0,2)$ trống; mã $(0,1,0,0)$. Tại $(6,3)$: Bắc $(6,2)$ trống, Đông $(7,3)$ tường, Nam $(6,4)$ tường, Tây $(5,3)$ trống; mã $(0,1,1,0)$.

**Câu (b).** Tọa độ cho quan sát đầy đủ, với $g$ là hàm đồng nhất. Mã bốn ô kề cho quan sát một phần: tại $(2,1)$, Bắc $(2,0)$ và Nam $(2,2)$ là tường, Đông $(3,1)$ và Tây $(1,1)$ trống; tại $(3,1)$, Bắc $(3,0)$ và Nam $(3,2)$ là tường, Đông $(4,1)$ và Tây $(2,1)$ trống. Hai ô cùng mã $(1,0,1,0)$, nên không có hàm $g$ nào.

**Kiểm tra lại.** Ô $(1,2)$ có ba hướng mã $0$, khớp việc nó nối $(0,2)$, $(1,1)$ và $(1,3)$. Hai lỗi thường gặp: đảo nghĩa hai chữ số, ghi $1$ cho hướng trống; và đọc $(1,2)$ là hàng $1$, cột $2$, trong khi tọa độ ghi theo thứ tự (cột, hàng).
:::

### Bài tập 02.14. Nhận diện tín hiệu học

**Mức độ:** nhận biết; câu (c) đòi tính lợi tức và đề xuất cách sửa, ở mức vận dụng; mục tiêu học tập 1.

**Nguồn:** Bài tập tuần 2 (2025–2026), bài 1; câu (c) theo Sutton và Barto (2018), Bài tập 3.7, trang 56.

::: exercise Bài tập 02.14 (Nhận diện tín hiệu học)
Xét ba tình huống.

1. Một mô hình phân loại ảnh được huấn luyện trên $10\,000$ ảnh, mỗi ảnh có nhãn "mèo" hoặc "chó".
2. Một thuật toán chia $5\,000$ khách hàng thành nhóm theo lịch sử mua hàng; không có nhãn nhóm nào cho trước.
3. Một robot hút bụi chọn hướng đi ở mỗi bước. Nó nhận phần thưởng $+1$ ở bước về tới trạm sạc và $0$ ở mọi bước khác; lượt kết thúc khi robot về tới trạm.

- (a) Với mỗi tình huống, xác định khung học (học có giám sát (supervised learning), học không giám sát (unsupervised learning) hoặc học tăng cường), loại tín hiệu và thời điểm nhận tín hiệu.
- (b) Giải thích vì sao tín hiệu ở tình huống 3 được xem là trễ.
- (c) Ở tình huống 3, tiêu chí là tổng phần thưởng của lượt, không chiết khấu. Sau nhiều lượt học, robot vẫn về được trạm nhưng không rút ngắn đường đi. Giải thích hiện tượng này bằng lợi tức của một đường về trạm dài $5$ bước và một đường dài $50$ bước, rồi nêu hai cách sửa cách đánh giá để đường ngắn có lợi tức lớn hơn.
:::

::: hint Gợi ý Bài tập 02.14
Nhắc lại Định nghĩa 01.5 và Nhận xét 01.6 (Mục 1.3 của ghi chú): phần thưởng chấm chuyển vừa xảy ra, không chỉ ra hành động đúng, và có thể đến trễ nhiều bước. Ở câu (c), viết chuỗi phần thưởng của một đường về trạm dài $k$ bước.
:::

::: solution Lời giải Bài tập 02.14
**Câu (a).**

- Tình huống 1 là học có giám sát: tín hiệu là nhãn đúng của từng ảnh, có sẵn trong dữ liệu trước khi học.
- Tình huống 2 là học không giám sát: không có nhãn; thuật toán tìm cấu trúc nhóm trong chính dữ liệu.
- Tình huống 3 là học tăng cường: tín hiệu là phần thưởng, đến sau mỗi hành động qua tương tác với môi trường.

**Câu (b).** Phần thưởng khác $0$ chỉ đến ở bước về tới trạm. Mọi hành động trước đó góp phần vào việc về tới trạm nhưng đều nhận $0$, nên phần thưởng ngay sau một hành động không cho biết hành động đó tốt hay xấu; tác dụng của hành động chỉ lộ ra ở cuối lượt (Nhận xét 01.6).

**Câu (c).** Đường về trạm dài $k$ bước có chuỗi phần thưởng gồm $k-1$ số $0$ rồi số $1$, nên với $\gamma=1$ và mọi $k\ge1$,
$$
G_0=(k-1)\cdot0+1=1 .
$$
Đường $5$ bước và đường $50$ bước cùng có lợi tức $1$, nên tiêu chí không ưu tiên đường ngắn và việc học không có lý do rút ngắn đường. Hai cách sửa:

- Phạt mỗi bước: thay phần thưởng bằng $-1$ ở mọi bước, kể cả bước về trạm, như mê cung $8\times8$. Hai đường có lợi tức $-5$ và $-50$.
- Chiết khấu với $\gamma<1$ (Định nghĩa 02.12): phần thưởng $+1$ ở bước thứ $k$ có trọng số $\gamma^{k-1}$, nên $G_0=\gamma^{k-1}$. Với $\gamma=0{,}9$, hai đường có lợi tức $0{,}9^4=0{,}6561$ và $0{,}9^{49}\approx0{,}0057$.

**Kiểm tra lại.** Với $k=1$, $G_0=1$ theo cả công thức $(k-1)\cdot0+1$ lẫn $\gamma^{k-1}$. Hai lỗi thường gặp: xếp tình huống 2 vào học có giám sát vì có "lịch sử mua hàng", trong khi lịch sử đó là dữ liệu đầu vào chứ không phải nhãn; và ở câu (c) dùng trọng số $\gamma^{k}$ cho bước thứ $k$, cho $0{,}9^5\approx0{,}59$ thay cho $0{,}6561$.
:::

### Bài tập 02.15. Quan sát đầy đủ và quan sát một phần

**Mức độ:** nhận biết; câu (c) đòi đề xuất một biểu diễn, ở mức vận dụng; mục tiêu học tập 2.

**Nguồn:** bài giảng gốc (2025–2026), trang 27 (câu đố phân loại năm tình huống); Bài tập tuần 2 (2025–2026), bài 2.

::: exercise Bài tập 02.15 (Quan sát đầy đủ và quan sát một phần)
Theo Nhận xét 02.4, môi trường được quan sát đầy đủ khi có hàm $g:\mathcal O\to\mathcal S^+$ với $S_t=g(O_t)$ ở mọi $t$, và được quan sát một phần khi có một quan sát ứng với hai trạng thái khác nhau có thể xảy ra; phân loại tương đối với biến được chọn làm trạng thái. Trong mỗi tình huống dưới, trạng thái là cấu hình mà luật của trò chơi hay của môi trường dùng tới.

1. Mê cung $8\times8$; tác tử nhận tọa độ (cột, hàng) của mình.
2. Mê cung $8\times8$; tác tử nhận ảnh toàn bản đồ, có vị trí xuất phát, đích và vị trí của tác tử.
3. Cờ vua, không tính đồng hồ thi đấu; tác tử là một người chơi, nhận toàn bộ bàn cờ và mọi nước đã đi của cả hai bên.
4. Một trò chơi trực tuyến như Liên Minh Huyền Thoại (League of Legends), Dota 2 hoặc CS:GO; tác tử là một người chơi, nhận hình ảnh trên màn hình của mình. Mỗi người chơi chỉ thấy phần bản đồ trong tầm nhìn của nhân vật hoặc đơn vị phe mình.
5. Robot hút bụi gia đình; tác tử là bộ điều khiển, nhận số đo của các cảm biến gắn trên robot, mỗi cảm biến chỉ đo vùng quanh robot.

- (a) Phân loại từng tình huống là quan sát đầy đủ hay quan sát một phần, và nêu lý do.
- (b) Ở tình huống 3, giả sử tác tử chỉ nhận ảnh bàn cờ hiện tại, không nhận các nước đã đi. Luật cờ vua chỉ cho nhập thành khi vua và xe tương ứng chưa từng di chuyển. Phân loại lại tình huống 3.
- (c) Ở tình huống 5, nêu một biểu diễn $X_t$ theo Định nghĩa 02.2 mà bộ điều khiển tính được, và cho biết biểu diễn đó có bảo đảm khôi phục được trạng thái hay không.
:::

::: hint Gợi ý Bài tập 02.15
Với mỗi tình huống, tìm hai trạng thái khác nhau cho cùng một quan sát; nếu quan sát xác định được mọi thành phần của trạng thái, viết hàm $g$.
:::

::: solution Lời giải Bài tập 02.15
**Câu (a).**

1. Quan sát đầy đủ. Bản đồ cố định, nên trạng thái là ô của tác tử, và $g$ là hàm đồng nhất.
2. Quan sát đầy đủ. Bản đồ cố định, và vị trí của tác tử đọc được từ ảnh; $g$ là phép đọc vị trí đó. Hai tình huống này khớp Mục 2.4 của ghi chú; trang 27 của bài giảng gốc chỉ nêu câu hỏi.
3. Quan sát đầy đủ. Từ bàn cờ và toàn bộ dãy nước đi, người chơi dựng lại được mọi thành phần mà luật dùng tới, trong đó có vị trí quân, bên đi, quyền nhập thành, khả năng bắt tốt qua đường, số lần lặp thế cờ và số nước kể từ lần bắt quân hoặc đi tốt gần nhất (luật 50 nước).
4. Quan sát một phần. Vị trí của một đối thủ ngoài tầm nhìn là một phần cấu hình mà luật trò chơi dùng tới. Hai cấu hình chỉ khác vị trí của đối thủ đó cho cùng hình ảnh trên màn hình.
5. Quan sát một phần. Lượng bụi và đồ vật ở phòng khác không có trong số đo; hai cấu hình chỉ khác nhau ở phòng khác cho cùng số đo.

**Câu (b).** Quan sát một phần. Xét hai ván cùng thế quân hiện tại, với vua trắng và xe trắng ở ô ban đầu: ở ván thứ nhất, vua chưa từng di chuyển; ở ván thứ hai, vua đã đi sang một ô rồi quay về. Hai cấu hình khác nhau ở quyền nhập thành, nên luật cho tập nước đi hợp lệ khác nhau, ngay ở bước này khi các ô giữa vua và xe trống và vua không bị chiếu, hoặc ở một bước về sau; hai cấu hình cho cùng ảnh bàn cờ. Không có hàm $g$ nào trên ảnh.

**Câu (c).** Một lựa chọn: $X_t$ gồm bản đồ chướng ngại dựng dần từ các số đo $O_{0:t}$ và các hành động $A_{0:t-1}$, vị trí ước lượng của robot trên bản đồ đó, và tập vùng đã đi qua. Biểu diễn này là một hàm của dữ liệu khả dụng theo (2.1), nên tính được. Nó không bảo đảm khôi phục được trạng thái: lượng bụi ở vùng chưa đi qua không có trong dữ liệu, nên hai cấu hình khác nhau ở vùng đó cho cùng $X_t$.

**Kiểm tra lại.** Kết luận ở tình huống 1 và câu (b) dùng cùng một tiêu chuẩn: tồn tại hay không hàm $g$ từ quan sát tới trạng thái. Hai lỗi thường gặp: coi quan sát là đầy đủ vì nó chứa nhiều dữ liệu, như một ảnh màn hình lớn, trong khi điều cần xét là đọc lại được trạng thái hay không; và đồng nhất quan sát đầy đủ với tính Markov. Trong mê cung có chìa khóa (Ví dụ 02.6), tọa độ được quan sát đầy đủ nhưng không có tính Markov.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 02.3. Trạng thái mở rộng của mê cung có chìa khóa

**Mức độ:** tính toán; mục tiêu học tập 2.

**Nguồn:** ghi chú bài giảng, Mục 2.5 (Ví dụ 02.6, Định nghĩa 02.5).

**Trùng trang chiếu:** [Bài tập: kiểm tra tính Markov](lecture-02-giao-dien-tac-tu-moi-truong.html#/3/12) và [trang lời giải](lecture-02-giao-dien-tac-tu-moi-truong.html#/3/13), câu (a). Câu (b) trên hai trang đó, về tính Markov của mã bốn ô kề, ứng với Bài tập 02.11 trong mục "Bài tập củng cố" của ghi chú.

::: exercise Bài tập 02.3 (Trạng thái mở rộng của mê cung có chìa khóa)
Mê cung có chìa khóa của Ví dụ 02.6: mê cung $8\times8$ với 27 ô đi được; chìa khóa ở ngõ cụt $(4,2)$, chỉ nối với $(4,1)$, được nhặt khi tác tử vào ô đó; bước Đông từ $(7,6)$ vào $\mathrm G$ chỉ thực hiện được khi đã có chìa khóa, nếu không thì tác tử đứng yên; mọi bước nhận $-1$; xuất phát tại $(0,2)$ chưa có chìa khóa. Trạng thái là cặp (ô, $k$) với $k=1$ khi đã có chìa khóa, $k=0$ khi chưa có.

- (a) Trạng thái nào trong $27\cdot2=54$ trạng thái chưa kết thúc không bao giờ xuất hiện khi xuất phát tại $(0,2)$.
- (b) Tính tổng phần thưởng của đường ngắn nhất từ $(0,2)$ tới $\mathrm G$, biết đường ngắn nhất khi không có cửa dài 16 bước, không qua $(4,2)$, và đi qua $(4,1)$ tại $t=5$.
:::

::: hint Gợi ý Bài tập 02.3
Ở câu (a), xét giá trị của $k$ ngay khi tác tử vào $(4,2)$. Ở câu (b), cửa buộc tác tử ghé $(4,2)$, và $(4,2)$ chỉ nối với $(4,1)$.
:::

::: solution Lời giải Bài tập 02.3
**Câu (a).** Trạng thái $((4,2),0)$: tác tử chỉ ở $(4,2)$ sau khi đi vào, và lúc đó đã nhặt chìa khóa. Còn $54-1=53$ trạng thái xuất hiện được.

**Câu (b).** Mọi đường tới $\mathrm G$ phải ghé $(4,2)$; mỗi lần ghé tốn ít nhất hai bước so với đường không ghé, vì $(4,2)$ chỉ nối với $(4,1)$. Đường 16 bước đi qua $(4,1)$; rẽ Nam vào $(4,2)$ tại đó rồi quay lại cho một đường dài đúng $16+2=18$ bước. Vậy đường ngắn nhất dài $18$ bước, tổng phần thưởng $-18$.

**Kiểm tra lại.** Đường 18 bước này là đường $h'$ của Ví dụ 02.6, tới $(7,6)$ tại $t=17$, thêm bước Đông cuối: $17+1=18$. Hai lỗi thường gặp: loại cả $((7,6),0)$, trong khi tác tử tới được $(7,6)$ trước khi nhặt chìa khóa; và trả lời $-16$ ở câu (b), quên rằng cửa buộc tác tử ghé $(4,2)$.
:::

### Bài tập 02.4. Chính sách ngẫu nhiên tại một ô

**Mức độ:** tính toán; mục tiêu học tập 3.

**Nguồn:** ghi chú bài giảng, Mục 3 (Định nghĩa 02.8, Ví dụ 02.8).

**Trùng trang chiếu:** [Bài tập: chính sách ngẫu nhiên tại một ô](lecture-02-giao-dien-tac-tu-moi-truong.html#/4/8); câu hỏi và lời giải nằm trên cùng trang.

::: exercise Bài tập 02.4 (Chính sách ngẫu nhiên tại một ô)
Mê cung $8\times8$, luật chuyển tất định, biểu diễn là tọa độ, $x=(1,2)$. Ô Đông $(2,2)$ là tường, nên bước Đông giữ tác tử tại $x$; các ô $(1,1)$ phía Bắc, $(1,3)$ phía Nam và $(0,2)$ phía Tây trống. Một chính sách cho $\pi(\text{Bắc}\mid x)=0{,}2$, $\pi(\text{Đông}\mid x)=0{,}5$, $\pi(\text{Tây}\mid x)=0$; tại $(1,1)$ nó chọn Đông với xác suất $0{,}9$ và Nam với xác suất $0{,}1$; tại $(1,3)$ nó luôn chọn Bắc.

- (a) Tính $\pi(\text{Nam}\mid x)$ và cho biết chính sách tại $x$ là xác định hay ngẫu nhiên.
- (b) Tính xác suất tác tử vẫn ở $x$ sau hai bước, xuất phát từ $x$.
:::

::: hint Gợi ý Bài tập 02.4
Ở câu (b), liệt kê các dãy hai hành động đưa tác tử trở về hoặc giữ tác tử ở $x$: đứng yên hai lần, hoặc đi rồi quay lại.
:::

::: solution Lời giải Bài tập 02.4
**Câu (a).** Theo (3.1), $\pi(\text{Nam}\mid x)=1-0{,}2-0{,}5-0=0{,}3$. Chính sách ngẫu nhiên, vì ba hành động có xác suất dương.

**Câu (b).** Ba cách giữ tác tử ở $x$ sau hai bước:

- Đông, Đông: đứng yên hai lần, xác suất $0{,}5\cdot0{,}5=0{,}25$;
- Bắc tới $(1,1)$ rồi Nam về $x$: $0{,}2\cdot0{,}1=0{,}02$;
- Nam tới $(1,3)$ rồi Bắc về $x$: $0{,}3\cdot1=0{,}3$.

Tổng là $0{,}25+0{,}02+0{,}3=0{,}57$.

**Kiểm tra lại.** Mọi dãy khác rời $x$: Đông rồi Bắc hoặc Nam, Bắc rồi Đông; tổng xác suất của chúng là $0{,}5\cdot0{,}5+0{,}2\cdot0{,}9=0{,}43=1-0{,}57$. Hai lỗi thường gặp: bỏ dãy Đông, Đông vì tưởng tác tử phải di chuyển, cho $0{,}32$; và dùng xác suất của chính sách tại $x$ cho bước thứ hai, trong khi bước đó được chọn tại ô mà môi trường vừa đưa tác tử tới.
:::

### Bài tập 02.5. Lợi tức chiết khấu và hệ thức truy hồi

**Mức độ:** tính toán; mục tiêu học tập 4.

**Nguồn:** ghi chú bài giảng, Mục 4.1–4.2 (Định lý 02.11, Định nghĩa 02.12, Mệnh đề 02.13).

**Trùng trang chiếu:** [Bài tập: lợi tức chiết khấu](lecture-02-giao-dien-tac-tu-moi-truong.html#/5/9); câu hỏi và lời giải nằm trên cùng trang.

::: exercise Bài tập 02.5 (Lợi tức chiết khấu và hệ thức truy hồi)
Một lượt kết thúc tại $T=4$ với $R_1=2$, $R_2=0$, $R_3=-1$, $R_4=4$.

- (a) Với $\gamma=0{,}5$, tính $G_3$, $G_2$, $G_1$, $G_0$ bằng Mệnh đề 02.13(a), $G_t=R_{t+1}+\gamma G_{t+1}$ với $G_4=0$, rồi kiểm tra $G_0$ bằng (4.5).
- (b) Với $\gamma=0{,}5$, thêm phần thưởng $r=-3$ vào đầu chuỗi, được chuỗi $(-3,2,0,-1,4)$. Ở đây $U(\sigma)$ là lợi tức chiết khấu của chuỗi phần thưởng $\sigma$ tính từ phần thưởng đầu tiên, và $[r,\sigma]$ là chuỗi có thêm $r$ ở đầu. Dùng hệ thức $U([r,\sigma])=r+\gamma U(\sigma)$ của Định lý 02.11, tính lợi tức của chuỗi mới mà không cộng lại từ đầu.
- (c) Tính $G_0$ của chuỗi ban đầu với $\gamma=0$ và $\gamma=1$.
:::

::: hint Gợi ý Bài tập 02.5
Bắt đầu từ $G_4=0$. Ở câu (b), $U(\sigma)$ của chuỗi ban đầu là $G_0$ của câu (a).
:::

::: solution Lời giải Bài tập 02.5
**Câu (a).** $G_3=4$; $G_2=-1+0{,}5\cdot4=1$; $G_1=0+0{,}5\cdot1=0{,}5$; $G_0=2+0{,}5\cdot0{,}5=2{,}25$. Theo (4.5): $2+0+0{,}25\cdot(-1)+0{,}125\cdot4=2{,}25$.

**Câu (b).** $-3+0{,}5\cdot2{,}25=-1{,}875$.

**Câu (c).** $\gamma=0$: $G_0=R_1=2$. $\gamma=1$: $G_0=2+0-1+4=5$.

**Kiểm tra lại.** Câu (b) cộng trực tiếp: $-3+0{,}5\cdot2+0+0{,}125\cdot(-1)+0{,}0625\cdot4=-1{,}875$. Hai lỗi thường gặp: nhân $\gamma$ vào cả $R_{t+1}$, chẳng hạn $G_3=0{,}5\cdot4=2$; và bắt đầu truy hồi từ $G_4=R_4$ thay cho $G_4=0$.
:::

### Bài tập 02.7. Hàm động lực của bước trượt

**Mức độ:** tính toán; mục tiêu học tập 4.

**Nguồn:** ghi chú bài giảng, Mục 4.5 (Định nghĩa 02.16); số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: hàm động lực của bước trượt](lecture-02-giao-dien-tac-tu-moi-truong.html#/5/15); câu hỏi và lời giải nằm trên cùng trang.

::: exercise Bài tập 02.7 (Hàm động lực của bước trượt)
Biến thể trơn của mê cung $8\times8$, trạng thái là tọa độ: tại $s=(0,2)$, bước Đông đưa tác tử tới $(1,2)$ với xác suất $0{,}8$ và giữ tác tử tại $(0,2)$ với xác suất $0{,}2$; mọi bước nhận $-1$. Viết $p(s',r\mid(0,2),\text{Đông})$ cho mọi cặp có xác suất dương, rồi tính $p(s'\mid(0,2),\text{Đông})$ và $r((0,2),\text{Đông})$, và kiểm tra điều kiện tổng của Định nghĩa 02.16.
:::

::: hint Gợi ý Bài tập 02.7
Dùng (4.9) và hai công thức suy ra sau Định nghĩa 02.16: $p(s'\mid s,a)=\sum_rp(s',r\mid s,a)$, $r(s,a)=\sum_{s'}\sum_rr\,p(s',r\mid s,a)$.
:::

::: solution Lời giải Bài tập 02.7
$p((1,2),-1\mid(0,2),\text{Đông})=0{,}8$ và $p((0,2),-1\mid(0,2),\text{Đông})=0{,}2$. Do đó $p((1,2)\mid(0,2),\text{Đông})=0{,}8$, $p((0,2)\mid(0,2),\text{Đông})=0{,}2$, và $r((0,2),\text{Đông})=(-1)\cdot0{,}8+(-1)\cdot0{,}2=-1$. Tổng $0{,}8+0{,}2=1$, nên bảng hợp lệ.

**Kiểm tra lại.** Mỗi trạng thái kế tiếp chỉ đi với một giá trị phần thưởng, nên $p(s'\mid s,a)$ trùng $p(s',-1\mid s,a)$. Hai lỗi thường gặp: kiểm điều kiện tổng riêng trên $s'$ với một giá trị $r$ cố định, thay cho tổng trên mọi cặp $(s',r)$; và cho rằng bước trượt không phải một chuyển vì tác tử không đổi ô. Khi bước trượt nhận $-2$ thay cho $-1$, xác suất chuyển giữ nguyên nhưng $r(s,a)$ đổi thành $-1{,}2$ (Bài tập 02.16).
:::

### Bài tập 02.16. Hàm động lực của bước trượt có phạt

**Mức độ:** tính toán; mục tiêu học tập 3 và 4.

**Nguồn:** số liệu sư phạm tự xây dựng trên mê cung $8\times8$; câu (d) theo Sutton và Barto (2018), Bài tập 3.11, trang 58.

::: exercise Bài tập 02.16 (Hàm động lực của bước trượt có phạt)
Biến thể trơn của mê cung $8\times8$, xét tại ô $s=(0,2)$. Ô Bắc $(0,1)$ và ô Nam $(0,3)$ là tường, ô phía Tây nằm ngoài lưới, ô Đông $(1,2)$ trống. Bước Đông đưa tác tử tới $(1,2)$ với xác suất $0{,}8$ và nhận $-1$; với xác suất $0{,}2$ bánh xe trượt, tác tử đứng yên tại $(0,2)$ và nhận $-2$. Bước Bắc, Nam hoặc Tây giữ tác tử tại $(0,2)$ với xác suất $1$ và nhận $-1$. Trạng thái là tọa độ ô.

- (a) Viết $p(s',r\mid(0,2),\text{Đông})$ cho mọi cặp $(s',r)$ có xác suất dương, rồi tính $p(s'\mid(0,2),\text{Đông})$ và $r((0,2),\text{Đông})$.
- (b) Khi biết $S_t=(0,2)$ và $A_t=\text{Đông}$, kiểm tra $S_{t+1}$ và $R_{t+1}$ có độc lập với nhau hay không.
- (c) Một bảng mô hình ghi $p((1,2),-1\mid(0,2),\text{Đông})=0{,}8$ và $p((1,2),-2\mid(0,2),\text{Đông})=0{,}3$. Cho biết bảng này có hợp lệ theo Định nghĩa 02.16 hay không.
- (d) Tác tử theo chính sách $\pi(\text{Đông}\mid(0,2))=0{,}7$ và $\pi(\text{Bắc}\mid(0,2))=\pi(\text{Nam}\mid(0,2))=\pi(\text{Tây}\mid(0,2))=0{,}1$. Viết $\mathbb E_\pi[R_{t+1}\mid S_t=s]$ theo $\pi$ và $p$, rồi tính giá trị đó tại $s=(0,2)$ và xác suất $\Pr_\pi(S_{t+1}=(1,2)\mid S_t=(0,2))$.
:::

::: hint Gợi ý Bài tập 02.16
Ở câu (a), dùng (4.9) và hai công thức suy ra sau Định nghĩa 02.16. Ở câu (b), so sánh $\Pr(S_{t+1}=(1,2),R_{t+1}=-1)$ với tích hai xác suất biên. Ở câu (d), theo quy tắc nhân, $\Pr(A_t=a,S_{t+1}=s',R_{t+1}=r\mid S_t=s)=\pi(a\mid s)\,p(s',r\mid s,a)$.
:::

::: solution Lời giải Bài tập 02.16
**Câu (a).** Hai kết cục có xác suất dương:
$$
\begin{aligned}
p((1,2),-1\mid(0,2),\text{Đông})&=0{,}8,\\
p((0,2),-2\mid(0,2),\text{Đông})&=0{,}2 .
\end{aligned}
$$
Mỗi trạng thái kế tiếp đi với đúng một giá trị phần thưởng, nên $p((1,2)\mid(0,2),\text{Đông})=0{,}8$ và $p((0,2)\mid(0,2),\text{Đông})=0{,}2$. Thưởng kỳ vọng một bước là
$$
r((0,2),\text{Đông})=0{,}8\cdot(-1)+0{,}2\cdot(-2)=-1{,}2 .
$$

**Câu (b).** Biên của trạng thái kế tiếp: $\Pr(S_{t+1}=(1,2))=0{,}8$. Biên của phần thưởng: $\Pr(R_{t+1}=-1)=0{,}8$, vì $-1$ chỉ đi với $(1,2)$. Tích hai biên là $0{,}64$, khác xác suất đồng thời $0{,}8$. Vậy $S_{t+1}$ và $R_{t+1}$ không độc lập; khi biết $(S_t,A_t)$, phần thưởng là một hàm của trạng thái kế tiếp.

**Câu (c).** Không hợp lệ. Hai số đã cho có tổng $0{,}8+0{,}3=1{,}1>1$, trái với điều kiện $\sum_{s'}\sum_rp(s',r\mid s,a)=1$ của Định nghĩa 02.16.

**Câu (d).** Lấy tổng theo $a$, $s'$, $r$ của quy tắc nhân trong gợi ý:
$$
\begin{aligned}
\mathbb E_\pi[R_{t+1}\mid S_t=s]
&=\sum_a\pi(a\mid s)\sum_{s'}\sum_rr\,p(s',r\mid s,a)\\
&=\sum_a\pi(a\mid s)\,r(s,a).
\end{aligned}
$$
Dòng thứ nhất là quy tắc nhân; dòng thứ hai dùng định nghĩa của $r(s,a)$.
Tại $(0,2)$: $r((0,2),\text{Đông})=-1{,}2$ theo câu (a), và ba hành động còn lại có thưởng kỳ vọng $-1$. Do đó
$$
\mathbb E_\pi[R_{t+1}\mid S_t=(0,2)]=0{,}7\cdot(-1{,}2)+0{,}3\cdot(-1)=-1{,}14 .
$$
Chỉ bước Đông đưa tác tử tới $(1,2)$, nên $\Pr_\pi(S_{t+1}=(1,2)\mid S_t=(0,2))=0{,}7\cdot0{,}8=0{,}56$.

**Kiểm tra lại.** Ba kết cục của câu (d) là (Đông, $(1,2)$, $-1$) với xác suất $0{,}56$, (Đông, $(0,2)$, $-2$) với $0{,}14$, và một trong ba hành động còn lại với $0{,}3$; tổng $1$, và kỳ vọng tính thẳng là $-0{,}56-0{,}28-0{,}3=-1{,}14$. Xác suất chuyển ở câu (a) giống hệt trường hợp bước trượt nhận $-1$ (Bài tập 02.7), nhưng $r(s,a)$ đổi từ $-1$ thành $-1{,}2$, nên $p(s'\mid s,a)$ không xác định được $r(s,a)$. Ba lỗi thường gặp: lấy trung bình cộng hai giá trị phần thưởng, $-1{,}5$, thay cho trung bình có trọng số; kết luận độc lập vì $p(s'\mid s,a)$ không đổi; bỏ ba hành động khác Đông ở câu (d), cho $-0{,}84$.
:::

### Bài tập 02.17. Lợi tức của nhiệm vụ tiếp diễn

**Mức độ:** tính toán và chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.9 và 3.10, trang 56; câu (d) dùng chuỗi đổi dấu ở đầu Mục 4.1 của ghi chú.

::: exercise Bài tập 02.17 (Lợi tức của nhiệm vụ tiếp diễn)
Xét nhiệm vụ tiếp diễn ($T=\infty$) với $\gamma\in[0,1)$ và phần thưởng bị chặn; lợi tức theo (4.6), $G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$.

- (a) Giả sử $R_{t+k+1}=\beta$ với mọi $k\ge0$, trong đó $\beta\in\mathbb R$ là hằng số. Chứng minh $G_t=\beta/(1-\gamma)$ bằng hai cách: qua tổng riêng, và qua Mệnh đề 02.13(a).
- (b) Với $\gamma=0{,}9$, $R_1=2$ và $R_k=7$ với mọi $k\ge2$, tính $G_1$ và $G_0$.
- (c) So sánh $G_1$ của câu (b) với chặn (4.7), lấy $R_{\max}=7$.
- (d) Với $\gamma=0{,}9$ và chuỗi đổi dấu $R_k=(-1)^{k+1}$, tức $1,-1,1,-1,\dots$, tính $G_0$ và $G_1$, kiểm tra hệ thức truy hồi giữa chúng, và giải thích vì sao với $\gamma=1$ lợi tức của chuỗi này không xác định.
:::

::: hint Gợi ý Bài tập 02.17
Tổng riêng $n$ số hạng đầu là một tổng hình học. Ở cách thứ hai của câu (a), chuỗi phần thưởng tạo nên $G_{t+1}$ giống chuỗi tạo nên $G_t$. Ở câu (d), $\gamma^k(-1)^k=(-\gamma)^k$.
:::

::: solution Lời giải Bài tập 02.17
**Câu (a).** *Cách thứ nhất.* Tổng riêng $n$ số hạng đầu là
$$
\begin{aligned}
\sum_{k=0}^{n-1}\gamma^k\beta
&=\beta\,\frac{1-\gamma^n}{1-\gamma}\\
&\longrightarrow\frac{\beta}{1-\gamma}\quad(n\to\infty).
\end{aligned}
$$
Dòng thứ nhất là tổng hình học với $\gamma\ne1$; giới hạn ở dòng thứ hai đúng vì $0\le\gamma<1$ nên $\gamma^n\to0$.
Vậy $G_t=\beta/(1-\gamma)$; với $\gamma=0$, công thức cho $G_t=\beta=R_{t+1}$, khớp quy ước $\gamma^0=1$.

*Cách thứ hai.* Mệnh đề 02.13(b) bảo đảm chuỗi hội tụ. Chuỗi phần thưởng từ $t+2$ trở đi cũng là $\beta,\beta,\dots$, nên $G_{t+1}=G_t$. Thế vào Mệnh đề 02.13(a):
$$
G_t=\beta+\gamma G_t\iff(1-\gamma)G_t=\beta\iff G_t=\frac{\beta}{1-\gamma}.
$$
Cách này cần biết trước chuỗi hội tụ; khi $\gamma=1$, phương trình $G=\beta+G$ vô nghiệm với $\beta\ne0$ và không cho lợi tức.

**Câu (b).** Từ $t=1$, các phần thưởng $R_2,R_3,\dots$ đều bằng $7$, nên theo câu (a), $G_1=7/(1-0{,}9)=70$. Theo Mệnh đề 02.13(a), $G_0=R_1+\gamma G_1=2+0{,}9\cdot70=65$.

**Câu (c).** Chặn (4.7) là $R_{\max}/(1-\gamma)=7/0{,}1=70$. $G_1=70$ đạt đúng chặn, vì mọi phần thưởng sau $t=1$ bằng $R_{\max}$ (phần Phạm vi của Mệnh đề 02.13); $G_0=65$ nhỏ hơn chặn vì $R_1=2<7$.

**Câu (d).** Với $t=0$, $R_{k+1}=(-1)^k$, nên
$$
G_0=\sum_{k=0}^{\infty}(-\gamma)^k=\frac{1}{1+\gamma}=\frac{1}{1{,}9}=\frac{10}{19}\approx0{,}526 .
$$
Với $t=1$, $R_{k+2}=-(-1)^k$, nên $G_1=-10/19\approx-0{,}526$. Hệ thức truy hồi: $R_1+\gamma G_1=1-0{,}9\cdot\frac{10}{19}=\frac{19-9}{19}=\frac{10}{19}=G_0$. Với $\gamma=1$, tổng riêng là $1,0,1,0,\dots$, dao động và không có giới hạn, nên (4.6) không xác định; đây là lý do Định nghĩa 02.12 đòi $\gamma<1$ cho nhiệm vụ tiếp diễn.

**Kiểm tra lại.** Ở câu (b), cộng thẳng: $2+7\sum_{k\ge1}0{,}9^k=2+7\cdot\frac{0{,}9}{0{,}1}=2+63=65$. Hai lỗi thường gặp: tính $G_1$ có cả $R_1$, trong khi $G_1$ bắt đầu từ $R_2$; và viết $G_0=R_1+G_1=72$, quên nhân $\gamma$ vào $G_1$.
:::

### Bài tập 02.18. Cộng một hằng số vào mọi phần thưởng

**Mức độ:** chứng minh; mục tiêu học tập 4 và 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.15 và 3.16, trang 61; ví dụ ở câu (b) và (c) dùng mê cung đích–hố (Ví dụ 02.14, 02.15) và mê cung $8\times8$.

::: exercise Bài tập 02.18 (Cộng một hằng số vào mọi phần thưởng)
Cho một môi trường thỏa các giả thiết của Định nghĩa 02.14 và một hằng số $\beta\in\mathbb R$. Môi trường mới giống hệt môi trường cũ, trừ phần thưởng: mỗi phần thưởng $R_{t+1}$ được thay bằng $R'_{t+1}=R_{t+1}+\beta$. Ký hiệu $G'_t$ và $v'_\pi$ là lợi tức và giá trị trong môi trường mới.

- (a) Nhiệm vụ tiếp diễn, $\gamma<1$, $\lvert R_{t+1}\rvert\le R_{\max}$. Chứng minh $v'_\pi(s)=v_\pi(s)+\beta/(1-\gamma)$ với mọi chính sách $\pi$ và mọi trạng thái $s$. Suy ra hiệu giá trị giữa hai trạng thái, và thứ tự giữa hai chính sách tại mỗi trạng thái, không đổi.
- (b) Nhiệm vụ có lượt (episodic task), lượt kết thúc tại $T<\infty$. Chứng minh $G'_0=G_0+\beta(1-\gamma^T)/(1-\gamma)$ khi $\gamma<1$ và $G'_0=G_0+\beta T$ khi $\gamma=1$. Áp dụng cho mê cung đích–hố với $c=0$, $c_{\mathrm H}=0$, $\gamma=1$ và $\beta=-3$: tính lại lợi tức của hai đường ngắn nhất và cho biết tác tử tối ưu đổi hành vi thế nào.
- (c) Trên mê cung $8\times8$ ($-1$ mỗi bước, $\gamma=1$), cộng $\beta=1$, rồi $\beta=2$, vào mọi phần thưởng. Với mỗi trường hợp, tính lợi tức của đường 16 bước tới $\mathrm G$ và của quỹ đạo luôn chọn Tây tại $(0,2)$, tức đứng yên mãi; nêu hệ quả đối với tác tử cực đại lợi tức.
:::

::: hint Gợi ý Bài tập 02.18
Ở câu (a), tách $\sum_k\gamma^k(R_{k+1}+\beta)$ thành hai chuỗi hội tụ tuyệt đối và dùng Bài tập 02.17(a); sau đó lấy kỳ vọng. Ở câu (b), tổng chỉ có $T$ số hạng, và $T$ khác nhau giữa các quỹ đạo.
:::

::: solution Lời giải Bài tập 02.18
**Câu (a).** Phần thưởng mới bị chặn bởi $R_{\max}+\lvert\beta\rvert$, nên $G'_0$ hội tụ tuyệt đối theo Mệnh đề 02.13(b). Hai chuỗi $\sum_k\gamma^kR_{k+1}$ và $\sum_k\gamma^k\beta$ cũng hội tụ tuyệt đối, nên được tách:
$$
\begin{aligned}
G'_0&=\sum_{k=0}^{\infty}\gamma^k\bigl(R_{k+1}+\beta\bigr)\\
&=\sum_{k=0}^{\infty}\gamma^kR_{k+1}+\sum_{k=0}^{\infty}\gamma^k\beta\\
&=G_0+\frac{\beta}{1-\gamma}.
\end{aligned}
$$
Dòng thứ nhất là (4.6) trong môi trường mới; dòng thứ hai tách hai chuỗi hội tụ tuyệt đối; dòng thứ ba dùng Bài tập 02.17(a).
Chính sách và xác suất chuyển không đổi, nên khi xuất phát tại $S_0=s$, dãy trạng thái và hành động có cùng phân phối như trong môi trường cũ; đẳng thức trên đúng trên mọi quỹ đạo. Lấy kỳ vọng hai vế, với $\mathbb E_\pi[\lvert G_0\rvert\mid S_0=s]<\infty$ theo giả thiết của Định nghĩa 02.14:
$$
v'_\pi(s)=\mathbb E_\pi\bigl[G_0\mid S_0=s\bigr]+\frac{\beta}{1-\gamma}=v_\pi(s)+\frac{\beta}{1-\gamma}.
$$
Với hai trạng thái $s$, $\tilde s$: $v'_\pi(s)-v'_\pi(\tilde s)=v_\pi(s)-v_\pi(\tilde s)$. Với hai chính sách $\pi$, $\pi'$ tại cùng $s$: $v'_\pi(s)-v'_{\pi'}(s)=v_\pi(s)-v_{\pi'}(s)$, nên thứ tự giữa hai chính sách giữ nguyên. Trong nhiệm vụ tiếp diễn, cộng cùng một hằng số vào mọi phần thưởng không đổi thứ tự giữa các chính sách, nên dấu của từng phần thưởng không quyết định hành vi.

**Câu (b).** Tổng có đúng $T$ số hạng:
$$
G'_0=\sum_{k=0}^{T-1}\gamma^k\bigl(R_{k+1}+\beta\bigr)=G_0+\beta\sum_{k=0}^{T-1}\gamma^k ,
$$
và $\sum_{k=0}^{T-1}\gamma^k$ bằng $(1-\gamma^T)/(1-\gamma)$ khi $\gamma<1$, bằng $T$ khi $\gamma=1$. Lượng cộng thêm phụ thuộc $T$, nên hai quỹ đạo dài khác nhau được dịch khác nhau và thứ tự giữa chúng có thể đổi.

Trên mê cung đích–hố với $c=0$, $c_{\mathrm H}=0$: đường tới $\mathrm G$ có $T=6$ và $G_0=10$; đường vào $\mathrm H$ có $T=2$ và $G_0=0$; tác tử tối ưu tới đích. Cộng $\beta=-3$; chỉ số dưới $\mathrm G$, $\mathrm H$ là điểm kết thúc của đường:
$$
\begin{aligned}
G'_{\mathrm G}&=10+(-3)\cdot6=-8,\\
G'_{\mathrm H}&=0+(-3)\cdot2=-6 .
\end{aligned}
$$
Đường vào hố có lợi tức lớn hơn, nên tác tử tối ưu đổi sang hố. Phần thưởng mới bằng $-3$ mỗi bước cộng $+10$ khi vào $\mathrm G$, tức trường hợp $c=3$ của Ví dụ 02.15; theo Mệnh đề 02.18, $3>c^*=2{,}5$.

**Câu (c).** Đường 16 bước có $G_0=-16$.

- $\beta=1$: mọi phần thưởng bằng $0$. Đường 16 bước có $G'_0=-16+16=0$; quỹ đạo đứng yên mãi có mọi tổng riêng bằng $0$, nên lợi tức $0$. Hai quỹ đạo ngang nhau: tiêu chí không còn ưu tiên việc tới $\mathrm G$.
- $\beta=2$: mọi phần thưởng bằng $+1$. Đường 16 bước có $G'_0=-16+32=16$; quỹ đạo đứng yên mãi có tổng riêng $n\to+\infty$. Tác tử cực đại lợi tức không bao giờ tới $\mathrm G$. Đây là trường hợp phần thưởng dương mỗi bước đã bị loại ở gạch đầu dòng "Bỏ $c\ge0$" sau Mệnh đề 02.18.

**Kiểm tra lại.** Với $R_{t+1}\equiv0$, câu (a) cho $v'_\pi=\beta/(1-\gamma)$, đúng giá trị của chuỗi hằng $\beta$ (Bài tập 02.17(a)). Ở câu (b), cộng tay từng bước của đường tới đích: năm bước $-3$ và bước cuối $-3+10=7$ cho $-15+7=-8$. Hai lỗi thường gặp: áp kết luận của câu (a) cho nhiệm vụ có lượt, bỏ qua việc $T$ khác nhau giữa các quỹ đạo; và chỉ cộng $\beta$ vào các bước chưa kết thúc, quên bước cuối, khi đó đường vào hố cho $-3$ thay cho $-6$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 02.8. Phạt hố bổ sung

**Mức độ:** vận dụng; mục tiêu học tập 5.

**Nguồn:** ghi chú bài giảng, Mục 5.2 (Mệnh đề 02.18).

**Trùng trang chiếu:** [Bài tập: phạt hố bổ sung](lecture-02-giao-dien-tac-tu-moi-truong.html#/6/7); câu hỏi và lời giải nằm trên cùng trang.

::: exercise Bài tập 02.8 (Phạt hố bổ sung)
Mê cung đích–hố của Ví dụ 02.14: đường ngắn nhất từ $\mathrm S$ tới $\mathrm G$ dài $6$ bước, tới $\mathrm H$ dài $2$ bước; tác tử có thể đi vòng; mỗi bước nhận $-c$ với $c\ge0$; vào $\mathrm G$ thêm $+10$; vào $\mathrm H$ thêm $-c_{\mathrm H}$ với $c_{\mathrm H}\ge0$; $\gamma=1$; chuyển tất định. Theo Mệnh đề 02.18, tác tử tối ưu tới đích khi $c<c^*=(10+c_{\mathrm H})/4$.

- (a) Với $c=3$, tìm điều kiện của $c_{\mathrm H}$ để tác tử tối ưu tới đích; nếu $c_{\mathrm H}$ nguyên, $c_{\mathrm H}$ nhỏ nhất là bao nhiêu.
- (b) Với $c_{\mathrm H}=4$, tìm mọi $c\ge0$ để tác tử tối ưu tới đích.
:::

::: hint Gợi ý Bài tập 02.8
Dùng (5.1), hoặc so sánh trực tiếp $10-6c$ với $-2c-c_{\mathrm H}$.
:::

::: solution Lời giải Bài tập 02.8
**Câu (a).** Cần $10-18>-6-c_{\mathrm H}$, tức $c_{\mathrm H}>2$; theo (5.1), $c^*=(10+c_{\mathrm H})/4>3$ cũng cho $c_{\mathrm H}>2$. Với $c_{\mathrm H}=2$, hai lợi tức bằng nhau, cùng $-8$. Nếu $c_{\mathrm H}$ nguyên thì $c_{\mathrm H}\ge3$.

**Câu (b).** $c^*=(10+4)/4=3{,}5$, nên tác tử tối ưu tới đích khi $0\le c<3{,}5$.

**Kiểm tra lại.** Tại $c=3{,}5$, $c_{\mathrm H}=4$: đích $10-21=-11$, hố $-7-4=-11$, ngang nhau như (5.1) dự báo. Hai lỗi thường gặp: cộng $c_{\mathrm H}$ thay vì trừ, viết lợi tức vào hố là $-2c+c_{\mathrm H}$; và nhận $c_{\mathrm H}=2$ ở câu (a), trong khi tại đó hai đường ngang nhau và tác tử tối ưu không nhất thiết tới đích.
:::

### Bài tập 02.21. Mê cung đích–hố có chiết khấu

**Mức độ:** vận dụng; mục tiêu học tập 4 và 5.

**Nguồn:** số liệu sư phạm tự xây dựng trên mê cung đích–hố (Ví dụ 02.14, Mệnh đề 02.18).

**Trùng trang chiếu:** [Bài tập: mê cung đích–hố có chiết khấu](lecture-02-giao-dien-tac-tu-moi-truong.html#/7/4) và [trang lời giải](lecture-02-giao-dien-tac-tu-moi-truong.html#/7/5), câu (a) và (b); câu (c) chỉ có ở tệp này.

::: exercise Bài tập 02.21 (Mê cung đích–hố có chiết khấu)
Mê cung đích–hố của Ví dụ 02.14: mười nút xếp thành vòng; đường ngắn nhất từ $\mathrm S$ tới $\mathrm H$ dài $2$ bước, tới $\mathrm G$ dài $6$ bước; chuyển tất định, tác tử có thể đi vòng. Mỗi bước nhận $-c$ với $c\ge0$, kể cả bước cuối; bước vào $\mathrm G$ nhận thêm $+10$; bước vào $\mathrm H$ không nhận thêm gì. Hệ số chiết khấu $\gamma=0{,}9$.

- (a) Tính lợi tức $G_0$ từ $\mathrm S$ của hai đường ngắn nhất với $c=1$ và với $c=3$; cho biết đường được chọn trong mỗi trường hợp.
- (b) Tìm ngưỡng $c^*$ tại đó hai đường ngắn nhất có cùng lợi tức, và so với $c^*=2{,}5$ khi $\gamma=1$.
- (c) Giải thích vì sao với $\gamma=0{,}9$ và $c\ge0$, chỉ cần so sánh hai đường ngắn nhất: xét các đường dài hơn tới cùng điểm kết thúc, quỹ đạo không kết thúc và chính sách ngẫu nhiên.
:::

::: hint Gợi ý Bài tập 02.21
Mệnh đề 02.18 giả thiết $\gamma=1$, nên không dùng trực tiếp (5.1) được. $m$ bước $-c$ cho $-c(1-\gamma^m)/(1-\gamma)$; phần thưởng $+10$ ở bước thứ sáu nhân $\gamma^5$.
:::

::: solution Lời giải Bài tập 02.21
**Ba trọng số.** Với $\gamma=0{,}9$: $0{,}9^5=0{,}59049$ và $0{,}9^6=0{,}531441$, nên
$$
\begin{aligned}
\frac{1-0{,}9^6}{0{,}1}&=4{,}68559\approx4{,}686,\\
10\cdot0{,}9^5&=5{,}9049\approx5{,}905,\\
1+0{,}9&=1{,}9 .
\end{aligned}
$$

**Hai lợi tức.** Đường tới $\mathrm G$ gồm sáu bước $-c$, bước cuối thêm $+10$ với trọng số $\gamma^5$; đường vào $\mathrm H$ gồm hai bước $-c$. Chỉ số dưới $\mathrm G$, $\mathrm H$ là điểm kết thúc của đường, không phải thời điểm; cả hai là $G_0$ từ $\mathrm S$:
$$
\begin{aligned}
G_{\mathrm G}&=5{,}905-4{,}686\,c,\\
G_{\mathrm H}&=-1{,}9\,c .
\end{aligned}
$$

**Câu (a).** Với $c=1$: $G_{\mathrm G}=5{,}9049-4{,}68559\approx1{,}22>-1{,}9=G_{\mathrm H}$, chọn đích. Với $c=3$: $G_{\mathrm G}=5{,}9049-14{,}05677\approx-8{,}15<-5{,}7=G_{\mathrm H}$, chọn hố.

**Câu (b).** Cho hai lợi tức bằng nhau:
$$
\begin{aligned}
5{,}905-4{,}686\,c&=-1{,}9\,c\\
\iff 2{,}786\,c&=5{,}905\\
\iff c^*&=\frac{5{,}905}{2{,}786}\approx2{,}12 .
\end{aligned}
$$
Ngưỡng thấp hơn $2{,}5$ của trường hợp $\gamma=1$. Chiết khấu làm phần thưởng đích giảm từ $10$ xuống $5{,}905$, còn chênh lệch chi phí giữa hai đường giảm từ $4$ xuống $2{,}786$. Riêng việc chênh lệch chi phí giảm sẽ đẩy ngưỡng lên $10/2{,}786\approx3{,}59$; ngưỡng giảm vì phần thưởng đích giảm theo tỉ lệ lớn hơn ($0{,}59$ so với $0{,}70$).

**Câu (c).** Lập luận theo Bước 1–3 của chứng minh Mệnh đề 02.18, với lợi tức chiết khấu.

- Đường tới $\mathrm G$ dài $k\ge6$ bước có $G_0=-c(1-\gamma^k)/(1-\gamma)+10\gamma^{k-1}$. Với $c\ge0$, cả hai số hạng không tăng theo $k$, nên lớn nhất tại $k=6$.
- Đường vào $\mathrm H$ dài $k\ge2$ bước có $G_0=-c(1-\gamma^k)/(1-\gamma)\le-c(1+\gamma)=-1{,}9\,c$.
- Quỹ đạo không kết thúc có $G_0=-c/(1-\gamma)=-10c$; với $c>0$, số này nhỏ hơn $-1{,}9\,c$; với $c=0$, nó bằng $0<5{,}905$.
- Vậy mọi quỹ đạo có $G_0\le M=\max\{G_{\mathrm G},G_{\mathrm H}\}$, nên mọi chính sách, kể cả ngẫu nhiên, có lợi tức kỳ vọng không vượt $M$, và một trong hai chính sách đi thẳng đạt $M$.

**Kiểm tra lại.** Tại $c^*\approx2{,}1198$ (tính với các trọng số chưa làm tròn): $G_{\mathrm G}=5{,}9049-4{,}68559\cdot2{,}1198\approx-4{,}028$ và $G_{\mathrm H}=-1{,}9\cdot2{,}1198\approx-4{,}028$. Hai lỗi thường gặp: dùng thẳng (5.1), cho $2{,}5$; và nhân $+10$ với $\gamma^6$ thay cho $\gamma^5$, cho $10\cdot0{,}9^6\approx5{,}314$ và ngưỡng sai $\approx1{,}91$.
:::

### Bài tập 02.19. Hành lang ba ô với hành động đảo chiều

**Mức độ:** vận dụng; mục tiêu học tập 2 và 3.

**Nguồn:** Sutton và Barto (2018), §13.1, Ví dụ 13.1, trang 323; Bài tập tuần 2 (2025–2026), bài 6.

::: exercise Bài tập 02.19 (Hành lang ba ô với hành động đảo chiều)
Một hành lang có ba ô chưa kết thúc $1,2,3$ từ trái sang phải; đích $\mathrm G$ ở bên phải ô $3$. Có hai hành động, Trái và Phải. Ở ô $1$ và ô $3$, hai hành động có tác dụng thông thường; Trái ở ô $1$ giữ tác tử tại ô $1$. Ở ô $2$, tác dụng bị đảo: Phải đưa tác tử về ô $1$, Trái đưa tác tử sang ô $3$. Mỗi bước nhận $-1$, $\gamma=1$, xuất phát tại ô $1$. Cảm biến cho cùng một quan sát ở cả ba ô.

- (a) Tác tử dùng luôn quan sát làm biểu diễn, nên $X_t$ là hằng số. Chỉ ra rằng cả hai chính sách xác định trên $X_t$ đều không tới $\mathrm G$.
- (b) Với chính sách ngẫu nhiên chọn Phải với xác suất $p\in(0,1)$, gọi $V_i$ là số bước kỳ vọng từ ô $i$ tới $\mathrm G$. Viết hệ ba phương trình, giải ra $V_1$ theo $p$, và tính lợi tức kỳ vọng từ ô $1$ khi $p=0{,}5$.
- (c) Tìm $p$ làm $V_1$ nhỏ nhất và giá trị nhỏ nhất đó.
- (d) Giải thích vì sao bài toán cần chính sách ngẫu nhiên khi biểu diễn là quan sát hiện tại, theo Nhận xét 02.4 và Định nghĩa 02.8.
- (e) Tác tử dùng cửa sổ hai quan sát $X_t=(O_t,A_{t-1},O_{t-1})$, với $X_0=(O_0,\varnothing,\varnothing)$. Tìm một chính sách xác định trên biểu diễn này đưa tác tử từ ô $1$ tới $\mathrm G$, số bước tương ứng, và so với câu (c).
:::

::: hint Gợi ý Bài tập 02.19
Phương trình cho ô $1$ là $V_1=1+pV_2+(1-p)V_1$; ở ô $2$, Phải đưa về ô $1$. Ở câu (c), đạo hàm của $V_1(p)$ bằng $0$ dẫn tới một phương trình bậc hai. Ở câu (e), mọi quan sát như nhau, nên phần thông tin mới của $X_t$ là hành động $A_{t-1}$.
:::

::: solution Lời giải Bài tập 02.19
**Câu (a).** Luôn Phải: ô $1\to$ ô $2\to$ ô $1\to\cdots$, không bao giờ tới ô $3$. Luôn Trái: tác tử đứng yên ở ô $1$ mãi. Cả hai quỹ đạo không kết thúc, với tổng riêng $-n$, nên theo quy ước giới hạn tổng riêng, lợi tức là $-\infty$.

**Câu (b).** Theo luật chuyển,
$$
\begin{aligned}
V_1&=1+pV_2+(1-p)V_1,\\
V_2&=1+pV_1+(1-p)V_3,\\
V_3&=1+p\cdot0+(1-p)V_2 .
\end{aligned}
$$
Phương trình đầu cho $V_1=1/p+V_2$; phương trình cuối cho $V_3=1+(1-p)V_2$. Thế vào phương trình giữa:
$$
\begin{aligned}
V_2&=1+p\Bigl(\frac1p+V_2\Bigr)+(1-p)\bigl(1+(1-p)V_2\bigr)\\
&=3-p+\bigl(p+(1-p)^2\bigr)V_2 .
\end{aligned}
$$
Dòng thứ nhất thế $V_1$ và $V_3$; dòng thứ hai gom các số hạng. Vì $1-p-(1-p)^2=p(1-p)$, ta được $V_2=\dfrac{3-p}{p(1-p)}$ và
$$
V_1=\frac1p+\frac{3-p}{p(1-p)}=\frac{4-2p}{p(1-p)}.
$$
Với $p=0{,}5$: $V_1=3/0{,}25=12$, nên lợi tức kỳ vọng từ ô $1$ là $-12$.

**Câu (c).** Đạo hàm của $V_1(p)=(4-2p)/(p-p^2)$ bằng $0$ khi $-2(p-p^2)-(4-2p)(1-2p)=0$, tức $p^2-4p+2=0$. Nghiệm trong $(0,1)$ là $p=2-\sqrt2\approx0{,}586$; $V_1\to\infty$ khi $p\to0$ hoặc $p\to1$, nên đây là điểm nhỏ nhất. Khi đó $p(1-p)=3\sqrt2-4$ và
$$
V_1=\frac{2\sqrt2}{3\sqrt2-4}=6+4\sqrt2\approx11{,}66 .
$$
Kết quả khớp Sutton và Barto (2018, trang 323): xác suất tốt nhất khoảng $0{,}59$, giá trị khoảng $-11{,}6$.

**Câu (d).** Ba ô cho cùng quan sát, nên môi trường được quan sát một phần (Nhận xét 02.4), và mọi chính sách trên $X_t$ chọn cùng một phân phối ở cả ba ô (Định nghĩa 02.8). Ô $2$ cần hành động ngược với ô $1$ và ô $3$, nên mọi chính sách xác định thất bại theo câu (a); chính sách ngẫu nhiên trộn hai hành động và tới đích với xác suất $1$, với số bước kỳ vọng nhỏ nhất $6+4\sqrt2$.

**Câu (e).** Vì $O_t$ không đổi, $X_t$ phân biệt được các bước chỉ qua $A_{t-1}$. Chọn chính sách: tại $X_0$ chọn Phải; khi $A_{t-1}$ là Phải, chọn Trái; khi $A_{t-1}$ là Trái, chọn Phải. Từ ô $1$: Phải tới ô $2$; Trái ở ô $2$ đưa tác tử sang ô $3$; Phải ở ô $3$ đưa tác tử vào $\mathrm G$. Lượt dài $3$ bước, lợi tức $-3$, bằng khoảng cách từ ô $1$ tới $\mathrm G$, nên không chính sách nào ngắn hơn. Bộ nhớ một hành động thay cho tính ngẫu nhiên và giảm số bước kỳ vọng từ khoảng $11{,}66$ xuống $3$, như cửa sổ hai quan sát trong Tình huống 02.2.

**Kiểm tra lại.** Với $p=0{,}5$: $V_2=10$, $V_3=1+0{,}5\cdot10=6$, và phương trình giữa cho $1+0{,}5\cdot12+0{,}5\cdot6=10=V_2$. Hai lỗi thường gặp. Thứ nhất, viết phương trình của ô $2$ theo tác dụng thông thường, $V_2=1+pV_3+(1-p)V_1$: ở $p=0{,}5$ lỗi này không đổi kết quả vì hai hành động được chọn đều, nhưng mô hình sai cho $p=1$ là tốt nhất với $3$ bước, trái với câu (a). Thứ hai, quên vòng đứng yên ở ô $1$ khi chọn Trái.
:::

### Bài tập 02.20. Hai cách thưởng cho bài toán giữ cột

**Mức độ:** vận dụng; mục tiêu học tập 4 và 5.

**Nguồn:** Sutton và Barto (2018), Ví dụ 3.4 và Bài tập 3.6, trang 56; bài toán CartPole của bài thực hành Bài 04. Cách A thưởng cả bước thất bại, như Bài tập 02.12(b); Ví dụ 3.4 chỉ thưởng các bước không thất bại, nên lợi tức ở đó thiếu số hạng $\gamma^{T-t-1}$ của bước thất bại.

::: exercise Bài tập 02.20 (Hai cách thưởng cho bài toán giữ cột)
Bài toán giữ cột trên xe (pole-balancing), dạng của CartPole trong bài thực hành Bài 04: một lượt kết thúc ở bước thất bại, khi cột đổ quá một góc cho trước hoặc xe ra khỏi đường ray. Lượt có $T\ge1$ bước, và bước thứ $T$ là bước thất bại. Xét hai cách thưởng.

**Cách A.** $+1$ ở mọi bước, kể cả bước thất bại, tức $R_k=1$ với $k=1,\dots,T$.

**Cách B.** $0$ ở mọi bước, trừ $-1$ ở bước thất bại, tức $R_T=-1$ và $R_k=0$ với $k<T$.

Trả lời các câu sau.

- (a) Với $\gamma\in[0,1)$ và $0\le t<T$, viết $G_t$ theo $T-t$ cho mỗi cách.
- (b) Với $t$ cố định và $\gamma\in(0,1)$, chứng minh cả hai lợi tức tăng theo $T$. Cho biết điều gì xảy ra với cách B khi $\gamma=1$.
- (c) Với $\gamma=0{,}9$, tính $G_0$ của hai lượt dài $T=10$ và $T=30$ theo mỗi cách.
- (d) Dạng tiếp diễn: sau mỗi lần thất bại, cột được dựng lại và tương tác không kết thúc; phần thưởng là $-1$ ở mỗi bước thất bại và $0$ ở các bước khác. Gọi $K_1<K_2<\cdots$ là các bước thất bại. Viết $G_t$ theo các $K_i$, rồi tính $G_0$ với $\gamma=0{,}9$ khi $K_i=20i$, và so với $G_0$ của cách B cho lượt kết thúc ở lần thất bại thứ nhất, $T=20$.
:::

::: hint Gợi ý Bài tập 02.20
Phần thưởng $R_{t+k+1}$ có trọng số $\gamma^k$, nên phần thưởng của bước thứ $T$ có trọng số $\gamma^{T-t-1}$ trong $G_t$. Ở câu (d), cộng các số hạng $-\gamma^{K_i-t-1}$ với $K_i>t$ và dùng tổng hình học theo $i$.
:::

::: solution Lời giải Bài tập 02.20
**Câu (a).** Cách A có $T-t$ phần thưởng $+1$ sau thời điểm $t$:
$$
G_t=\sum_{k=0}^{T-t-1}\gamma^k=\frac{1-\gamma^{T-t}}{1-\gamma}.
$$
Cách B chỉ có một phần thưởng khác $0$, $R_T=-1$, ứng với chỉ số $k=T-t-1$:
$$
G_t=-\gamma^{T-t-1}.
$$

**Câu (b).** Với $0<\gamma<1$, $\gamma^{T-t}$ và $\gamma^{T-t-1}$ giảm ngặt khi $T$ tăng. Do đó $(1-\gamma^{T-t})/(1-\gamma)$ tăng ngặt và $-\gamma^{T-t-1}$ tăng ngặt theo $T$: cả hai cách xếp lượt giữ cột lâu hơn lên trên. Khi $\gamma=1$, cách A cho $G_t=T-t$, vẫn tăng theo $T$, còn cách B cho $G_t=-1$ với mọi $T$: mọi lượt có cùng lợi tức, và tiêu chí không ưu tiên việc giữ cột lâu. Cách B chỉ dùng được với $\gamma<1$.

**Câu (c).** Với $\gamma=0{,}9$, theo câu (a) với $t=0$:

| $T$ | Cách A: $(1-0{,}9^T)/0{,}1$ | Cách B: $-0{,}9^{T-1}$ |
| --- | --- | --- |
| $10$ | $6{,}513$ | $-0{,}387$ |
| $30$ | $9{,}576$ | $-0{,}047$ |

Cả hai cách cho lượt $T=30$ lợi tức lớn hơn lượt $T=10$.

**Câu (d).** Mỗi bước thất bại $K_i>t$ đóng góp $-1$ với trọng số $\gamma^{K_i-t-1}$:
$$
G_t=-\sum_{i:\,K_i>t}\gamma^{K_i-t-1}.
$$
Với $t=0$, $K_i=20i$ và $\gamma=0{,}9$:
$$
\begin{aligned}
G_0&=-\sum_{i=1}^{\infty}0{,}9^{20i-1}\\
&=-\frac{0{,}9^{19}}{1-0{,}9^{20}}\\
&\approx-\frac{0{,}1351}{0{,}8784}\approx-0{,}154 .
\end{aligned}
$$
Cách B với $T=20$ cho $-0{,}9^{19}\approx-0{,}135$. Hiệu $-0{,}019$ đến từ các lần thất bại sau lần đầu: dạng có lượt kết thúc ở lần thất bại thứ nhất, dạng tiếp diễn tính mọi lần thất bại với trọng số giảm dần.

**Kiểm tra lại.** Với $t=T-1$, cả hai công thức của câu (a) cho $G_{T-1}=R_T$: $1$ ở cách A và $-1$ ở cách B. Theo hệ thức truy hồi ở cách B, $G_{T-2}=0+\gamma\cdot(-1)=-\gamma$, khớp $-\gamma^{T-t-1}$ với $t=T-2$. Hai lỗi thường gặp: dùng trọng số $\gamma^{T-t}$ cho bước thất bại, cho $-0{,}9^{10}\approx-0{,}349$ thay cho $-0{,}387$ khi $T=10$; và bỏ các lần thất bại sau ở câu (d). Với $T=20$, cách A cho $(1-0{,}9^{20})/0{,}1\approx8{,}784$, khớp Bài tập 02.12(b) của ghi chú.
:::

### Bài tập 02.22. Mô hình hóa đèn giao thông tại một ngã tư

**Mức độ:** vận dụng; mục tiêu học tập 1, 2 và 4.

**Nguồn:** Bài tập tuần 2 (2025–2026), bài 10 (lĩnh vực giao thông); số liệu sư phạm tự xây dựng.

::: exercise Bài tập 02.22 (Mô hình hóa đèn giao thông tại một ngã tư)
Một bộ điều khiển đèn tại ngã tư có hai hướng, Bắc–Nam (viết tắt BN) và Đông–Tây (viết tắt DT). Ở mỗi bước điều khiển, đúng một hướng có đèn xanh; tại $t=0$, hướng BN xanh. Mỗi hướng có một hàng xe chờ dài $0$, $1$ hoặc $2$ xe. Một bước diễn ra theo thứ tự:

1. Bộ điều khiển chọn hành động $a_1$ (Giữ: giữ pha xanh hiện tại) hoặc $a_2$ (Đổi: chuyển pha xanh sang hướng kia).
2. Nếu chọn $a_1$ và hàng của hướng đang xanh có xe, một xe của hướng đó đi qua ngã tư. Nếu chọn $a_2$, bước này là đèn vàng, không xe nào đi qua, và hướng kia xanh từ bước sau.
3. Ở mỗi hướng, một xe mới đến với xác suất $0{,}5$, độc lập giữa hai hướng và giữa các bước. Xe đến khi hàng đã có $2$ xe thì rẽ sang đường khác và không được tính.
4. Phần thưởng là âm tổng số xe đang chờ ở hai hướng sau bước đó.

Bộ điều khiển nhận độ dài hai hàng chờ từ camera và biết pha xanh hiện tại. Tương tác không kết thúc; $\gamma=0{,}9$. Trong bài này, $q_{\mathrm{BN}}$, $q_{\mathrm{DT}}$ là độ dài hai hàng chờ và $e\in\{\mathrm{BN},\mathrm{DT}\}$ là hướng đang xanh.

- (a) Xác định ranh giới tác tử–môi trường, tập trạng thái và số phần tử, tập hành động, và kiểu nhiệm vụ.
- (b) Chứng minh rằng nếu chỉ chọn trạng thái là cặp $(q_{\mathrm{BN}},q_{\mathrm{DT}})$, không có $e$, thì trạng thái đó không có tính Markov theo (2.3).
- (c) Với $s=(q_{\mathrm{BN}},q_{\mathrm{DT}},e)=(1,2,\mathrm{BN})$, viết $p(s',r\mid s,a)$ cho $a=a_1$ và $a=a_2$, rồi tính $r(s,a_1)$ và $r(s,a_2)$.
- (d) Tính chặn (4.7) của $\lvert G_t\rvert$. Giải thích vì sao so sánh hai hành động ở câu (c) chỉ bằng thưởng kỳ vọng một bước là chưa đủ.
- (e) Thay camera bằng cảm biến ở vạch dừng, chỉ báo mỗi hướng có xe chờ hay không. Phân loại quan sát theo Nhận xét 02.4 và đề xuất một biểu diễn theo (2.1) có dùng dữ liệu quá khứ.
- (f) Nêu hai khó khăn khi dùng mô hình này với dữ liệu thực, mỗi khó khăn gắn với một giả thiết của Định nghĩa 02.5, 02.14 hoặc 02.16, hoặc với cách gán phần thưởng.
:::

::: hint Gợi ý Bài tập 02.22
Ở câu (b), tìm hai lịch sử cùng độ dài, cùng kết thúc ở cặp $(1,1)$ và cùng phần thưởng, nhưng khác hướng đang xanh, rồi so sánh dự báo của hành động $a_1$. Ở câu (c), áp bước 2 trước bước 3; hàng DT đã đầy nên không đổi.
:::

::: solution Lời giải Bài tập 02.22
**Câu (a).** Tác tử là bộ điều khiển, chỉ chọn $a_1$ hoặc $a_2$. Đèn, dòng xe đến và đi, camera và cơ chế tính phần thưởng thuộc môi trường (Định nghĩa 01.1). Trạng thái là $s=(q_{\mathrm{BN}},q_{\mathrm{DT}},e)$ với $q_{\mathrm{BN}},q_{\mathrm{DT}}\in\{0,1,2\}$, nên $\lvert\mathcal S\rvert=3\cdot3\cdot2=18$, và không có trạng thái kết thúc. Tập hành động là $\mathcal A(s)=\{a_1,a_2\}$ ở mọi $s$. Đây là nhiệm vụ tiếp diễn; Định nghĩa 02.12 cần $\gamma<1$ và phần thưởng bị chặn, và cả hai thỏa vì $\gamma=0{,}9$, $\lvert R_{t+1}\rvert\le4$. Camera cho độ dài hai hàng và bộ điều khiển biết $e$, nên $X_t=S_t$ và môi trường được quan sát đầy đủ. Luật của một bước chỉ dùng $q_{\mathrm{BN}}$, $q_{\mathrm{DT}}$, $e$, hành động và các xe mới đến, vốn độc lập với quá khứ, nên trạng thái này có tính Markov.

**Câu (b).** Đặt $Y_t=(q_{\mathrm{BN}},q_{\mathrm{DT}})$. Định nghĩa 02.5 đòi (2.3) với mọi chính sách; xét chính sách chọn $a_1$ và $a_2$ mỗi hành động với xác suất $0{,}5$, và tương tác bắt đầu với $Y_0=(1,1)$, hướng BN xanh. Hai lịch sử cùng độ dài:

- $h$: $A_0=a_2$, không xe nào đến; $Y_1=(1,1)$, $R_1=-2$, và từ $t=1$ hướng DT xanh.
- $h'$: $A_0=a_1$, một xe BN đi qua, một xe BN đến, không xe DT nào đến; $Y_1=(1,1)$, $R_1=-2$, và hướng BN vẫn xanh.

Mỗi lịch sử có xác suất $0{,}5\cdot0{,}25>0$. Chọn $A_1=a_1$. Sau $h$, một xe DT đi qua và hàng BN vẫn có ít nhất $1$ xe, nên $\Pr(Y_2=(0,1),R_2=-1\mid H_1=h,A_1=a_1)=0$. Sau $h'$, một xe BN đi qua, cặp thành $(0,1)$, và không xe nào đến với xác suất $0{,}25$, nên xác suất tương ứng là $0{,}25$. Hai lịch sử kết thúc ở cùng $Y_1=(1,1)$, cùng hành động, nhưng cho hai dự báo khác nhau, nên không có vế phải nào của (2.3) chỉ phụ thuộc $Y_1$ và $A_1$. Thêm $e$ vào trạng thái sửa được lỗi này, như bit $k$ trong mê cung có chìa khóa (Ví dụ 02.6).

**Câu (c).** Với $a_1$: xe BN duy nhất đi qua, hàng BN còn $0$; hàng DT đầy nên giữ $2$; sau đó hàng BN nhận một xe với xác suất $0{,}5$.
$$
\begin{aligned}
p((1,2,\mathrm{BN}),-3\mid s,a_1)&=0{,}5,\\
p((0,2,\mathrm{BN}),-2\mid s,a_1)&=0{,}5,
\end{aligned}
$$
nên $r(s,a_1)=0{,}5\cdot(-3)+0{,}5\cdot(-2)=-2{,}5$. Với $a_2$: không xe nào đi qua, hướng DT xanh từ bước sau; hàng BN lên $2$ xe với xác suất $0{,}5$.
$$
\begin{aligned}
p((2,2,\mathrm{DT}),-4\mid s,a_2)&=0{,}5,\\
p((1,2,\mathrm{DT}),-3\mid s,a_2)&=0{,}5,
\end{aligned}
$$
nên $r(s,a_2)=-3{,}5$.

**Câu (d).** Tổng số xe chờ không vượt $4$, nên $\lvert R_{t+1}\rvert\le R_{\max}=4$ và theo (4.7), $\lvert G_t\rvert\le4/(1-0{,}9)=40$. Thưởng một bước nghiêng về $a_1$, chênh $1$. Hành động còn quyết định trạng thái kế tiếp: sau $a_1$, hàng DT vẫn đầy và vẫn đỏ; sau $a_2$, hàng DT được phục vụ từ bước sau. Theo Mệnh đề 02.13(a), $G_t=R_{t+1}+\gamma G_{t+1}$, nên lợi tức kỳ vọng sau mỗi hành động còn phụ thuộc giá trị của các trạng thái kế tiếp $(1,2,\mathrm{BN})$, $(0,2,\mathrm{BN})$, $(2,2,\mathrm{DT})$, $(1,2,\mathrm{DT})$ dưới chính sách dùng về sau. Bài 03 viết phép so sánh này thành phương trình Bellman.

**Câu (e).** Cảm biến cho $O_t=(o_{\mathrm{BN}},o_{\mathrm{DT}})$, với chữ số của một hướng bằng $1$ khi hàng của hướng đó có ít nhất một xe và bằng $0$ khi hàng trống; bộ điều khiển vẫn biết $e$. Hai trạng thái $(1,2,\mathrm{BN})$ và $(2,2,\mathrm{BN})$ cho cùng quan sát $(1,1)$, nên môi trường được quan sát một phần (Nhận xét 02.4). Một biểu diễn theo (2.1): $X_t$ gồm $O_t$, $e$, và với mỗi hướng, số bước liên tiếp gần nhất mà cảm biến của hướng đó báo có xe. Biểu diễn này tính được từ $O_{0:t}$ và $A_{0:t-1}$, nhưng không bảo đảm phân biệt $q=1$ với $q=2$: khi một hướng đang đỏ và cảm biến của hướng đó luôn báo có xe, một lịch sử với $q=1$ và một lịch sử với $q=2$ có thể cho cùng dãy quan sát.

**Câu (f).** Bốn khó khăn có thể nêu:

- Xác suất xe đến đổi theo giờ trong ngày: môi trường không dừng, trái giả thiết của Định nghĩa 02.14 và 02.16. Đưa giờ vào trạng thái sửa được, nhưng tập trạng thái lớn lên.
- Xe đến theo đoàn từ ngã tư trước, nên không độc lập giữa các bước: dự báo xe đến phụ thuộc quá khứ, và $(q_{\mathrm{BN}},q_{\mathrm{DT}},e)$ mất tính Markov (Định nghĩa 02.5); cần thêm biến, chẳng hạn pha đèn của ngã tư trước.
- Hàng chờ thực dài hơn $2$ xe, nên luật "xe thứ ba rẽ đi" sai với dữ liệu và hàm động lực $p$ của mô hình (Định nghĩa 02.16) không khớp môi trường thật. Nới giới hạn lên $50$ xe mỗi hướng cho $\lvert\mathcal S\rvert=51\cdot51\cdot2=5\,202$.
- Phần thưởng không tính xe bị rẽ đi, nên một chính sách để một hàng đầy lâu không bị phạt cho số xe phải rẽ; cần thêm một số hạng phạt cho xe bị rẽ, cùng loại rủi ro của Nhận xét 02.19.

**Kiểm tra lại.** Ở câu (c), mỗi hành động có hai kết cục với tổng xác suất $1$, và trạng thái kế tiếp ghi cả $e$. Ở câu (b), lịch sử $h'$ đúng: sau $a_1$ cặp thành $(0,1)$, một xe BN đến cho $(1,1)$ và phần thưởng $-2$. Hai lỗi thường gặp: cho một xe đi qua trong bước đèn vàng, làm $r(s,a_2)$ thành $-2{,}5$, bằng $r(s,a_1)$; và cho hàng DT lên $3$ xe.
:::

## Tài liệu tham khảo

- **Bài giảng gốc.** Tạ Việt Cường (2025–2026), *Lecture 2: Markov Decision Process*: mê cung $8\times8$ ở trang 25–26; câu đố phân loại quan sát đầy đủ và quan sát một phần ở trang 27 (Bài tập 02.15).
- **Bài tập tuần 2 (2025–2026).** Bài 1 (Bài tập 02.14), bài 2 (Bài tập 02.15), bài 5 (Bài tập 02.10 trong ghi chú), bài 6 (Bài tập 02.19), bài 10 (Bài tập 02.22). Bài 3, 4, 7, 8, 9 cần quá trình quyết định Markov (Markov decision process, MDP) và phương trình Bellman của Bài 03.
- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2: Ví dụ 3.4 và Bài tập 3.6, 3.7, 3.9, 3.10, trang 56 (Bài tập 02.14, 02.17, 02.20); Bài tập 3.11, trang 58 (Bài tập 02.16); Bài tập 3.15, 3.16, trang 61 (Bài tập 02.18); §13.1, Ví dụ 13.1, trang 323 (Bài tập 02.19).
