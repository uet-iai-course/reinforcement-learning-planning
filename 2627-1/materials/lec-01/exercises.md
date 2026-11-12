# Bài tập Bài 01 — Giới thiệu Học tăng cường

Tệp gồm năm bài, Bài tập 01.12–01.16, đánh số tiếp theo mười một bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-01/lecture-note.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html) (Bài tập 01.1–01.11) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập chương 1 và chương 2 của Sutton và Barto (2018); mỗi bài ghi số bài, mục và trang của sách, và dữ kiện được chép lại trong khối đề. Các bài chia theo ba mức: nhận biết (01.12); tính toán hoặc chứng minh (01.13); vận dụng vào bài toán Học tăng cường (reinforcement learning) (01.14–01.16). Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/1/1) | — |
| 2. Tác tử học từ tương tác | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/2/1) | 01.14; ghi chú: 01.1 |
| 3. Tín hiệu học và dữ liệu tương tác | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/3/1) | ghi chú: 01.2 |
| 4. Phần thưởng và lợi tức | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/4/1) | ghi chú: 01.3, 01.4, 01.10 |
| 5. Chính sách, hàm giá trị, mô hình và thăm dò | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/5/1) | 01.12, 01.13, 01.16; ghi chú: 01.5, 01.6, 01.9, 01.11 |
| 6. Tic-tac-toe như một bài toán Học tăng cường | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/6/1) | 01.14, 01.15, 01.16; ghi chú: 01.7, 01.8 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/7/1) | — |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 01. Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$.

**Bài toán chọn lặp lại một bước** (multi-armed bandit). Tác tử chọn lặp lại trong một tập hữu hạn hành động; mỗi lần chọn chỉ gồm một hành động và một phần thưởng. Với hành động $a$ đã được chọn $N(a)\ge1$ lần, ước lượng của $a$ là trung bình mẫu $\bar r(a)$ của các phần thưởng đã nhận khi chọn $a$. Hành động tham lam (greedy action) là hành động có ước lượng lớn nhất; khai thác (exploitation) là chọn một hành động tham lam, thăm dò (exploration) là chọn một hành động không tham lam (Định nghĩa 01.16). Chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy) chọn hành động tham lam với xác suất $1-\varepsilon$ và chọn đều trên mọi hành động, kể cả hành động tham lam, với xác suất $\varepsilon$ (ghi chú, Mục 4.4).

Tương ứng với sách: sách đánh số các lần chọn từ $1$ và viết $A_n$, $R_n$ cho hành động và phần thưởng của lần chọn thứ $n$. Để không lẫn với quy ước $R_{t+1}$ của ghi chú, tệp này viết $a_n$, $r_n$. Sách viết $Q_n(a)$ cho ước lượng của $a$ trước lần chọn thứ $n$; ước lượng này bằng $\bar r(a)$ khi $a$ đã được chọn, và bằng ước lượng ban đầu khi $a$ chưa được chọn.

**Tic-tac-toe.** Bàn $3\times3$, ô đánh số 1 đến 9 theo hàng, từ trái sang phải và từ trên xuống dưới. Tác tử là người chơi X; bàn cờ, luật chơi và đối thủ O là môi trường, và O chọn nước theo chính sách $\sigma(\cdot\mid\tilde s)$ (Định nghĩa 01.18). Chữ O không có chỉ số chỉ quân cờ của đối thủ, khác quan sát $O_t$.

**Người chơi Học tăng cường của Sutton và Barto (2018, §1.5).** Bài tập 01.14–01.16 dùng phương pháp sau, được nêu lại trong từng đề.

- Người chơi cầm quân X và giữ một bảng $V$ gán cho mỗi thế cờ một ước lượng xác suất thắng của X từ thế cờ đó: $V=1$ ở thế cờ X có ba quân thẳng hàng; $V=0$ ở thế cờ O có ba quân thẳng hàng hoặc bàn đầy; mọi thế cờ khác có $V=0{,}5$ lúc đầu.
- Ở mỗi nước, người chơi xét các thế cờ sinh ra từ mỗi ô trống và tra $V$ của chúng. Phần lớn các nước, người chơi đánh nước dẫn tới thế cờ có $V$ lớn nhất (nước tham lam); thỉnh thoảng, người chơi chọn ngẫu nhiên một trong các nước còn lại (nước thăm dò).
- Sau mỗi nước tham lam, với $s$ là thế cờ trước nước đó và $s'$ là thế cờ sau nước đó,
  $$
  \begin{aligned}
  V(s)&\leftarrow V(s)\\
  &\quad+\alpha\big[V(s')-V(s)\big],
  \end{aligned}
  $$
  trong đó hệ số bước (step-size parameter) $\alpha$ là một số dương nhỏ. Nước thăm dò không dẫn tới cập nhật nào.
- Sách nêu (tr. 10): nếu $\alpha$ được giảm dần hợp lý theo thời gian, phương pháp hội tụ, với mọi đối thủ cố định, tới xác suất thắng thật từ mỗi thế cờ khi người chơi chơi tối ưu, và các nước người chơi đánh khi đó, trừ nước thăm dò, là nước tối ưu chống đối thủ này. Nếu $\alpha$ không giảm hết về $0$, người chơi cũng chơi tốt chống đối thủ đổi cách chơi chậm.

Xác suất thắng của X là kỳ vọng của lợi tức khi phần thưởng cuối ván là $1$ nếu X thắng và $0$ nếu X hòa hoặc thua. Cách đặt này khác cách đặt $+1$, $-1$, $0$ của Định nghĩa 01.18 ở chỗ hòa và thua có cùng giá trị.

## Mức nhận biết

### Bài tập 01.12. Xác suất chọn hành động tham lam

**Mức độ:** nhận biết; mục tiêu học tập 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 2.1, §2.2, trang 28.

::: exercise Bài tập 01.12 (Xác suất chọn hành động tham lam)
Trong cách chọn hành động $\varepsilon$-tham lam, tác tử chọn hành động tham lam theo ước lượng với xác suất $1-\varepsilon$; với xác suất $\varepsilon$, tác tử chọn ngẫu nhiên một hành động trong mọi hành động với xác suất bằng nhau, không phụ thuộc các ước lượng. Xét trường hợp có hai hành động và $\varepsilon=0{,}5$. Tính xác suất hành động tham lam được chọn.
:::

::: hint Gợi ý Bài tập 01.12
Hành động tham lam được chọn theo hai cách loại trừ nhau: ở bước tham lam, hoặc ở bước ngẫu nhiên khi phép chọn đều rơi vào chính nó.
:::

::: solution Lời giải Bài tập 01.12
Gọi $g$ là hành động tham lam. Với xác suất $1-\varepsilon$, tác tử chọn $g$. Với xác suất $\varepsilon$, tác tử chọn đều trên hai hành động, nên chọn $g$ với xác suất $\frac12$. Hai trường hợp loại trừ nhau, nên

$$
\begin{aligned}
\Pr(\text{chọn } g)&=(1-\varepsilon)+\varepsilon\cdot\tfrac12\\
&=0{,}5+0{,}25\\
&=0{,}75 .
\end{aligned}
$$

**Kiểm tra lại.** Hành động không tham lam chỉ được chọn ở bước ngẫu nhiên, với xác suất $\varepsilon\cdot\frac12=0{,}25$, và $0{,}75+0{,}25=1$. Trả lời $0{,}5=1-\varepsilon$ là quên rằng bước ngẫu nhiên cũng có thể chọn hành động tham lam. Vì bước ngẫu nhiên chọn mỗi hành động với xác suất dương, chính sách $\varepsilon$-tham lam với $\varepsilon>0$, khi có hành động không tham lam, là một chính sách có thăm dò theo Định nghĩa 01.16.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 01.13. Nhận ra bước thăm dò trong một dãy lựa chọn

**Mức độ:** tính toán; mục tiêu học tập 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 2.2, §2.3, trang 30.

::: exercise Bài tập 01.13 (Nhận ra bước thăm dò trong một dãy lựa chọn)
Xét bài toán chọn lặp lại một bước với bốn hành động $1$, $2$, $3$, $4$. Tác tử dùng cách chọn $\varepsilon$-tham lam: với xác suất $1-\varepsilon$ chọn một hành động có ước lượng lớn nhất (khi nhiều hành động cùng có ước lượng lớn nhất, chọn một hành động bất kỳ trong số đó); với xác suất $\varepsilon$ chọn đều trên cả bốn hành động. Ước lượng ban đầu của mọi hành động bằng $0$. Sau mỗi lần chọn, ước lượng của hành động vừa chọn là trung bình mẫu các phần thưởng đã nhận khi chọn hành động đó; ước lượng của hành động chưa được chọn vẫn bằng $0$. Năm lần chọn đầu tiên cho dãy hành động và phần thưởng sau:

| Lần chọn $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---:|---:|---:|---:|---:|
| Hành động $a_n$ | $1$ | $2$ | $2$ | $2$ | $3$ |
| Phần thưởng $r_n$ | $-1$ | $1$ | $-2$ | $2$ | $0$ |

- (a) Lập bảng ước lượng của bốn hành động trước mỗi lần chọn và tập hành động tham lam tương ứng.
- (b) Ở những lần chọn nào, trường hợp chọn ngẫu nhiên chắc chắn đã xảy ra.
- (c) Ở những lần chọn nào, trường hợp chọn ngẫu nhiên có thể đã xảy ra.
:::

::: hint Gợi ý Bài tập 01.13
Trước lần chọn thứ $n$, chỉ dùng các phần thưởng $r_1,\dots,r_{n-1}$. Ở câu (c), xét xem phép chọn đều trên bốn hành động có thể cho ra đúng hành động đã thấy hay không.
:::

::: solution Lời giải Bài tập 01.13
**Câu (a).** Hành động $1$ chỉ được chọn ở lần 1, nên từ lần 2 ước lượng của nó là $-1$. Hành động $2$ được chọn ở lần 2, 3, 4, nên ước lượng của nó là $1$ trước lần 3, $\frac{1+(-2)}2=-\frac12$ trước lần 4 và $\frac{1+(-2)+2}3=\frac13$ trước lần 5. Hành động $3$ và $4$ chưa được chọn trước lần 5, nên giữ ước lượng $0$.

| Lần chọn $n$ | Ước lượng của $1,2,3,4$ trước lần $n$ | Hành động tham lam | $a_n$ |
|---|---|---|---:|
| $1$ | $0;\ 0;\ 0;\ 0$ | $\{1,2,3,4\}$ | $1$ |
| $2$ | $-1;\ 0;\ 0;\ 0$ | $\{2,3,4\}$ | $2$ |
| $3$ | $-1;\ 1;\ 0;\ 0$ | $\{2\}$ | $2$ |
| $4$ | $-1;\ -\frac12;\ 0;\ 0$ | $\{3,4\}$ | $2$ |
| $5$ | $-1;\ \frac13;\ 0;\ 0$ | $\{2\}$ | $3$ |

**Câu (b).** Ở bước tham lam, tác tử chỉ chọn trong tập hành động tham lam. Ở lần 4, hành động $2$ không thuộc $\{3,4\}$; ở lần 5, hành động $3$ không thuộc $\{2\}$. Do đó trường hợp chọn ngẫu nhiên chắc chắn đã xảy ra ở lần 4 và lần 5.

**Câu (c).** Ở lần 1, 2, 3, hành động được chọn thuộc tập hành động tham lam, nên bước tham lam có thể đã cho ra nó. Phép chọn đều trên bốn hành động cũng cho ra mỗi hành động với xác suất $\frac14>0$, nên trường hợp chọn ngẫu nhiên cũng có thể đã xảy ra. Ở lần 4 và 5, theo câu (b), trường hợp này chắc chắn đã xảy ra. Vậy trường hợp chọn ngẫu nhiên có thể đã xảy ra ở cả năm lần chọn.

**Kiểm tra lại.** Ba phần thưởng của hành động $2$ là $1$, $-2$, $2$, có tổng $1$ và trung bình $\frac13$, khớp hàng cuối của bảng. Nếu bỏ qua ước lượng ban đầu $0$ của hành động chưa chọn, ở lần 2 hành động $1$ thành hành động tham lam duy nhất, và lần 2 bị xếp nhầm vào câu (b). Trả lời câu (c) chỉ bằng lần 4 và 5 là quên rằng bước ngẫu nhiên cũng có thể cho ra một hành động tham lam.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 01.14. Người chơi Tic-tac-toe tự chơi với chính nó

**Mức độ:** vận dụng; mục tiêu học tập 1 và 6.

**Nguồn:** Sutton và Barto (2018), Bài tập 1.1, §1.5, trang 12.

::: exercise Bài tập 01.14 (Người chơi Tic-tac-toe tự chơi với chính nó)
Người chơi Học tăng cường của Sutton và Barto (2018, §1.5) học như sau. Người chơi giữ một bảng $V$ gán cho mỗi thế cờ một ước lượng xác suất thắng của mình từ thế cờ đó: $V=1$ ở thế cờ mình có ba quân thẳng hàng, $V=0$ ở thế cờ đối thủ có ba quân thẳng hàng hoặc bàn đầy, $V=0{,}5$ ở mọi thế cờ khác lúc đầu. Phần lớn các nước, người chơi đánh nước dẫn tới thế cờ có $V$ lớn nhất (nước tham lam); thỉnh thoảng, người chơi chọn ngẫu nhiên một trong các nước còn lại (nước thăm dò). Sau mỗi nước tham lam từ thế cờ $s$ tới thế cờ $s'$, người chơi cập nhật $V(s)\leftarrow V(s)+\alpha\big[V(s')-V(s)\big]$ với hệ số bước $\alpha>0$ nhỏ. Sách nêu rằng khi $\alpha$ được giảm dần hợp lý, phương pháp hội tụ, với mọi đối thủ cố định, tới xác suất thắng thật khi người chơi chơi tối ưu, và các nước không thăm dò khi đó là nước tối ưu chống đối thủ này.

Giả sử thay vì chơi với một đối thủ chọn nước ngẫu nhiên, thuật toán trên tự chơi với chính nó: bên X và bên O mỗi bên dùng phương pháp trên với bảng $V$ riêng, và cả hai bên cùng học.

- (a) Điều gì xảy ra với các ước lượng $V$ của mỗi bên và với kết quả hội tụ mà sách nêu.
- (b) Thuật toán có học được một chính sách chọn nước khác với chính sách học được khi chơi với đối thủ chọn nước ngẫu nhiên không.
:::

::: hint Gợi ý Bài tập 01.14
Đối thủ của mỗi bên là bên kia, và bên kia chọn nước theo bảng $V$ của nó, bảng này đổi sau mỗi nước tham lam.
:::

::: solution Lời giải Bài tập 01.14
**Câu (a).** Với bên X, môi trường gồm bàn cờ, luật chơi và bên O; với bên O, môi trường gồm bàn cờ, luật chơi và bên X. Theo Định nghĩa 01.1, mỗi bên chỉ quyết định nước của chính mình, nên bên kia thuộc môi trường dù hai bên dùng cùng một thuật toán. Mỗi bên chọn nước theo bảng $V$ của mình, và bảng đó đổi sau mỗi nước tham lam, nên chính sách mà mỗi bên gặp ở đối thủ đổi từ ván này sang ván khác. Định nghĩa 01.18 đòi chính sách $\sigma$ của đối thủ cố định, và Định nghĩa 01.12 đòi luật của môi trường cố định; trong lúc hai bên còn học, cả hai giả thiết đều không thỏa.

Xác suất thắng từ một thế cờ là xác suất thắng chống đối thủ đang chơi. Khi đối thủ đổi cách chơi, đại lượng này đổi theo, nên phép cập nhật $V(s)\leftarrow V(s)+\alpha[V(s')-V(s)]$ dịch $V(s)$ về phía một đại lượng đang đổi. Kết quả hội tụ của sách đòi một đối thủ cố định, nên không áp dụng được trong lúc hai bên còn học. Nếu từ một ván nào đó chính sách của bên O thôi thay đổi, thì từ ván đó bên X gặp một đối thủ cố định và kết quả hội tụ áp dụng được cho bên X; điều tương tự đúng khi đổi vai hai bên.

**Câu (b).** Chính sách học được phụ thuộc đối thủ. Chống một đối thủ cố định không hoàn hảo, các nước tối ưu tận dụng nước sai của chính đối thủ đó; sách nêu (tr. 11) rằng người chơi học được cách giăng bẫy nhiều nước đối với một đối thủ thiển cận. Khi tự chơi, đối thủ là bên kia, cũng đang học để thắng, nên các nước được học là nước tốt chống đối thủ đang học này. Hai chính sách chỉ trùng nhau khi, ở mọi thế cờ X gặp, nước tối ưu chống hai đối thủ là như nhau.

**Kiểm tra lại.** Coi bên kia là một phần của tác tử vì hai bên dùng cùng thuật toán là sai: mỗi bên chỉ điều khiển nước của mình. Áp nguyên kết quả hội tụ của §1.5 cho trường hợp tự chơi cũng sai, vì kết quả đó cần đối thủ cố định.
:::

### Bài tập 01.15. Đối xứng của bàn cờ Tic-tac-toe

**Mức độ:** vận dụng; mục tiêu học tập 4 và 6.

**Nguồn:** Sutton và Barto (2018), Bài tập 1.2, §1.5, trang 12.

::: exercise Bài tập 01.15 (Đối xứng của bàn cờ Tic-tac-toe)
Bàn $3\times3$ có ô đánh số 1 đến 9 theo hàng, từ trái sang phải và từ trên xuống dưới. Người chơi Học tăng cường của Sutton và Barto (2018, §1.5) cầm quân X và học như sau. Người chơi giữ một bảng $V$ gán cho mỗi thế cờ một ước lượng xác suất thắng của X từ thế cờ đó: $V=1$ ở thế cờ X có ba quân thẳng hàng, $V=0$ ở thế cờ O có ba quân thẳng hàng hoặc bàn đầy, $V=0{,}5$ ở mọi thế cờ khác lúc đầu. Phần lớn các nước, người chơi đánh nước dẫn tới thế cờ có $V$ lớn nhất; thỉnh thoảng, người chơi chọn ngẫu nhiên một trong các nước còn lại. Sau mỗi nước tham lam từ thế cờ $s$ tới thế cờ $s'$, người chơi cập nhật $V(s)\leftarrow V(s)+\alpha\big[V(s')-V(s)\big]$ với hệ số bước $\alpha>0$ nhỏ.

Nhiều thế cờ trông khác nhau nhưng thực chất là một vì bàn cờ có đối xứng (symmetry): bốn phép quay quanh tâm (kể cả phép quay $0^\circ$) và bốn phép lật qua hàng giữa, cột giữa và hai đường chéo.

- (a) Sửa quá trình học trên như thế nào để tận dụng đối xứng.
- (b) Thay đổi đó cải thiện quá trình học ở những điểm nào.
- (c) Giả sử đối thủ không tận dụng đối xứng. Khi đó người chơi có nên tận dụng đối xứng không.
- (d) Có đúng là các thế cờ đối xứng với nhau nhất thiết có cùng giá trị không.
:::

::: hint Gợi ý Bài tập 01.15
Ở câu (c) và (d), giá trị của một thế cờ là xác suất thắng chống một đối thủ cụ thể. Xét một đối thủ chọn nước theo số hiệu của ô, vì số hiệu đổi qua phép đối xứng.
:::

::: solution Lời giải Bài tập 01.15
**Câu (a).** Ta gộp mỗi lớp thế cờ đối xứng với nhau thành một ô của bảng. Mỗi lớp có một đại diện cố định, chẳng hạn thế cờ đứng đầu theo một thứ tự cố định trong tám ảnh của nó qua tám phép đối xứng. Khi tra hoặc cập nhật $V$ của một thế cờ, người chơi dùng ô của đại diện. Khi xét các nước, người chơi tra $V$ của đại diện của thế cờ sau mỗi nước, nên hai nước dẫn tới hai thế cờ cùng lớp có cùng ước lượng.

**Câu (b).** Số ô của bảng bằng số lớp, nhỏ hơn số thế cờ, vì mỗi lớp có từ $1$ đến $8$ thế cờ và có lớp nhiều hơn một thế cờ, chẳng hạn bốn thế cờ chỉ có một quân X ở một góc. Mỗi lớp được cập nhật mỗi khi người chơi gặp bất kỳ thế cờ nào của lớp, nên số lần cập nhật của một lớp bằng tổng số lần gặp các thế cờ trong lớp. Kinh nghiệm ở một thế cờ được dùng cho các thế cờ đối xứng với nó mà người chơi chưa gặp.

**Câu (c) và (d).** Giá trị của một thế cờ là xác suất thắng chống đối thủ đang chơi, nên nó phụ thuộc chính sách $\sigma$ của đối thủ. Theo điều kiện 2 của Nhận xét 01.19, giá trị viết được trên thế cờ khi $\sigma$ chỉ phụ thuộc thế cờ. Muốn hai thế cờ đối xứng có cùng giá trị, cần thêm điều kiện: $\sigma$ không đổi qua phép đối xứng, tức đối thủ trả lời thế cờ ảnh bằng ảnh của nước nó trả lời thế cờ gốc. Nếu đối thủ không tận dụng đối xứng, điều kiện này có thể sai, và khi đó hai thế cờ đối xứng có thể có giá trị khác nhau. Ví dụ sau cho hai giá trị khác nhau.

Giả sử O chọn đều trên các ô trống, trừ khi còn đúng ba ô trống thì đánh ô trống có số nhỏ nhất, và X đánh nước cho xác suất thắng lớn nhất. Xét thế cờ $w$: X ở ô 1, 5, 6; O ở ô 2, 4, 8; các ô 3, 7, 9 trống; đến phiên O. Đây là thế cờ của Ví dụ 01.10 sau nước $a=6$ của X. Theo bảng của Ví dụ 01.10, các dòng $a=6$:

- O đánh 3: X đánh 9 và thắng;
- O đánh 7: X đánh 9 và thắng;
- O đánh 9: X đánh 3 thì O thắng, X đánh 7 thì hòa, nên X không thắng được.

Ở $w$ còn ba ô trống, nên O đánh ô 3, ô nhỏ nhất, và xác suất thắng của X từ $w$ bằng $1$.

Phép lật qua đường chéo 3–5–7 đổi chỗ các ô $1\leftrightarrow9$, $2\leftrightarrow6$, $4\leftrightarrow8$ và giữ nguyên ô 3, 5, 7. Ảnh $w'$ của $w$ có X ở ô 9, 5, 2; O ở ô 6, 8, 4; các ô 7, 3, 1 trống. Ở $w'$ cũng còn ba ô trống, nên O đánh ô 1, ảnh của ô 9. Diễn biến từ đó là ảnh của diễn biến "O đánh 9" từ $w$, nên X không thắng được và xác suất thắng của X từ $w'$ bằng $0$. Hai thế cờ đối xứng $w$ và $w'$ có giá trị $1$ và $0$. Cả hai xảy ra được với xác suất dương dưới đối thủ này, vì trước khi còn ba ô trống O chọn đều: $w$ sau dãy O2, X1, O4, X5, O8, X6 và $w'$ sau dãy O6, X9, O8, X5, O4, X2. Nếu O chọn đều trên các ô trống, cả hai có cùng xác suất thắng $\frac13(1+1+0)=\frac23$.

Vậy câu (d) có câu trả lời là không. Với câu (c), khi đối thủ không chơi đối xứng, gộp $w$ và $w'$ vào một ô của bảng buộc người chơi dùng một ước lượng cho hai giá trị khác nhau, và người chơi không còn khai thác được chỗ khác nhau đó. Người chơi chỉ nên gộp các thế cờ đối xứng khi chính sách của đối thủ không đổi qua phép đối xứng.

**Kiểm tra lại.** Ở $w'$, kiểm tra trực tiếp: sau khi O đánh ô 1, các ô 3 và 7 trống; X đánh 3 thì O đánh 7 và có cột 1–4–7, X đánh 7 thì O đánh 3 và ván hòa. Kết quả khớp ảnh của dòng "O đánh 9". Coi đối xứng của bàn cờ là đủ để hai thế cờ cùng giá trị là quên rằng giá trị còn phụ thuộc đối thủ.
:::

### Bài tập 01.16. Người chơi Tic-tac-toe luôn tham lam

**Mức độ:** vận dụng; mục tiêu học tập 5 và 6.

**Nguồn:** Sutton và Barto (2018), Bài tập 1.3, §1.5, trang 12–13.

::: exercise Bài tập 01.16 (Người chơi Tic-tac-toe luôn tham lam)
Người chơi Học tăng cường của Sutton và Barto (2018, §1.5) cầm quân X và giữ một bảng $V$ gán cho mỗi thế cờ một ước lượng xác suất thắng của X: $V=1$ ở thế cờ X có ba quân thẳng hàng, $V=0$ ở thế cờ O có ba quân thẳng hàng hoặc bàn đầy, $V=0{,}5$ ở mọi thế cờ khác lúc đầu. Người chơi không tham lam của sách phần lớn các nước đánh nước dẫn tới thế cờ có $V$ lớn nhất, và thỉnh thoảng chọn ngẫu nhiên một trong các nước còn lại (nước thăm dò). Sau mỗi nước tham lam từ thế cờ $s$ tới thế cờ $s'$, người chơi cập nhật $V(s)\leftarrow V(s)+\alpha\big[V(s')-V(s)\big]$ với hệ số bước $\alpha>0$ nhỏ; nước thăm dò không dẫn tới cập nhật nào. Sách nêu rằng khi $\alpha$ được giảm dần hợp lý, người chơi này hội tụ, với mọi đối thủ cố định, tới xác suất thắng thật khi chơi tối ưu, và các nước người chơi đánh khi đó, trừ nước thăm dò, là nước tối ưu chống đối thủ này.

Giả sử người chơi tham lam, tức luôn đánh nước dẫn tới thế cờ mà nó đánh giá tốt nhất, và vẫn cập nhật như trên.

- (a) Người chơi tham lam có thể học chơi tốt hơn, hoặc kém hơn, người chơi không tham lam không.
- (b) Những vấn đề gì có thể xảy ra.
:::

::: hint Gợi ý Bài tập 01.16
Xét những thế cờ mà người chơi tham lam không bao giờ đi tới, và ước lượng của chúng sau nhiều ván. So với Nhận xét 01.17.
:::

::: solution Lời giải Bài tập 01.16
**Câu (a).** Cả hai khả năng đều có. Kết quả hội tụ mà sách nêu dành cho người chơi có thăm dò; người chơi tham lam không có bảo đảm đó, và câu (b) chỉ ra cơ chế khiến nó học chơi kém hơn. Ngược lại, nếu thứ tự các ước lượng của người chơi tham lam xếp nước tối ưu cao nhất ở mọi thế cờ nó gặp, nó đánh nước tối ưu ở mọi nước. Người chơi không tham lam, kể cả sau khi hội tụ, vẫn đánh nước thăm dò, tức nước khác nước có ước lượng lớn nhất. Ở thế cờ có nước tối ưu duy nhất, nước thăm dò cho xác suất thắng nhỏ hơn, nên trong trường hợp này người chơi tham lam có xác suất thắng lớn hơn.

**Câu (b).** Người chơi tham lam chỉ cập nhật $V$ dọc các nước tham lam của nó. Một thế cờ chỉ đi tới được bằng một nước mà người chơi không bao giờ đánh thì không bao giờ được cập nhật, và giữ ước lượng ban đầu $0{,}5$ hoặc một ước lượng cũ. Giả sử sau vài ván đầu, ước lượng của nước tối ưu thấp hơn ước lượng của một nước khác, chẳng hạn vì một ván thua làm giảm ước lượng của nó. Chừng nào ước lượng của nước kia còn lớn hơn, người chơi tham lam không đánh nước tối ưu, nên ước lượng sai của nước tối ưu không được cập nhật. Đây là hiện tượng khai thác quá sớm của Nhận xét 01.17: như ở Ví dụ 01.9, nếu luôn chọn A thì ước lượng của B mãi dựa trên hai mẫu. Ngoài ra, nước khai thác một bước theo các ước lượng hiện có không bảo đảm tối ưu (Nhận xét 01.22).

**Kiểm tra lại.** Kết luận "người chơi tham lam luôn kém hơn" là sai: nó kém hơn khi các ước lượng xếp sai thứ tự nước và không được sửa, nhưng đánh đúng mọi nước khi các ước lượng xếp đúng. Kết luận "nước thăm dò không cần thiết vì không dẫn tới cập nhật" cũng sai: theo sách (tr. 9 và chú thích Hình 1.1), chính nước thăm dò không dẫn tới cập nhật, nhưng nó đưa người chơi tới những thế cờ mà nước tham lam không dẫn tới, và các nước tham lam sau đó cập nhật ước lượng ở những thế cờ này.
:::

## Tài liệu tham khảo

- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §1.5 (tr. 8–13) cho phương pháp học Tic-tac-toe và Bài tập 1.1–1.3 (tr. 12–13), dùng ở Bài tập 01.14–01.16; §2.2 (tr. 27–28), Bài tập 2.1, dùng ở Bài tập 01.12; §2.3 (tr. 30), Bài tập 2.2, dùng ở Bài tập 01.13.
- Ghi chú bài giảng Bài 01 cho các kết quả được dùng trong lời giải: Định nghĩa 01.1, 01.12, 01.16, 01.18; Nhận xét 01.17, 01.19, 01.22; Ví dụ 01.9, 01.10.
