# Bài tập Bài 06 — Điều khiển phi mô hình

Tệp gồm sáu bài, Bài tập 06.14–06.19, đánh số tiếp theo mười ba bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-06/lecture-note.md&deck=lecture-06-dieu-khien-phi-mo-hinh.html) (Bài tập 06.1–06.13) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập chương 5 và chương 6 của Sutton và Barto (2018); mỗi bài ghi số bài, mục và trang của sách, và dữ kiện được chép lại trong khối đề. Không bài nào trùng bài tập trên bộ trang chiếu. Các bài chia theo ba mức: nhận biết (06.14, 06.15); tính toán hoặc chứng minh (06.16–06.18); vận dụng vào bài toán Học tăng cường (06.19). Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/1/1) | — |
| 2. Giá trị hành động và thăm dò | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/2/1) | ghi chú: 06.1, 06.2, 06.8, 06.11 |
| 3. Điều khiển Monte Carlo | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/3/1) | 06.14, 06.16; ghi chú: 06.3 |
| 4. Sarsa và mục tiêu một bước | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/4/1) | 06.17, 06.19; ghi chú: 06.4 |
| 5. Q-learning và học khác chính sách | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/5/1) | 06.15, 06.18; ghi chú: 06.5, 06.10 |
| 6. Điều kiện hội tụ | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/6/1) | ghi chú: 06.6, 06.9, 06.12 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/7/1) | ghi chú: 06.7, 06.13 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 06. Tại bước $t$, tác tử ở trạng thái $S_t$, chọn hành động $A_t$, rồi nhận phần thưởng $R_{t+1}$ và trạng thái $S_{t+1}$. Một lượt kết thúc tại thời điểm $T$; lợi tức là $G_t=R_{t+1}+\gamma G_{t+1}$ với $G_T=0$. Bảng giá trị hành động $Q$ có một ô cho mỗi cặp hợp lệ $(s,a)$, và $Q(s,\cdot)=0$ tại mọi trạng thái kết thúc $s$ (Định nghĩa 06.1). Mục tiêu Sarsa và mục tiêu Q-learning là
$$
\begin{aligned}
Y_t^{\text{Sarsa}}&=R_{t+1}+\gamma\,Q(S_{t+1},A_{t+1}),\\
Y_t^{\text{Q}}&=R_{t+1}+\gamma\max_aQ(S_{t+1},a),
\end{aligned}
$$
cả hai bằng $R_{t+1}$ khi $S_{t+1}$ kết thúc (Định nghĩa 06.11, 06.15); cập nhật là $Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\,[Y_t-Q(S_t,A_t)]$.

Tương ứng với sách: sách dùng bước học hằng $\alpha$ trong hai thuật toán một bước, viết "average" cho trung bình số học, và đánh số các công thức theo chương (chẳng hạn (6.6) của sách). Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$.

## Mức nhận biết

### Bài tập 06.14. Sơ đồ dự phòng của Monte Carlo cho giá trị hành động

**Mức độ:** nhận biết; mục tiêu học tập 1 và 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 5.3, §5.2, trang 97; quy ước sơ đồ dự phòng, §3.5, trang 59, và §5.1, trang 94–95.

::: exercise Bài tập 06.14 (Sơ đồ dự phòng của Monte Carlo cho giá trị hành động)
Sơ đồ dự phòng (backup diagram) vẽ ở trên cùng nút gốc, tức nút được cập nhật, và vẽ bên dưới mọi chuyển cùng các nút lá có phần thưởng và giá trị ước lượng góp vào cập nhật. Vòng tròn rỗng là một trạng thái; chấm đặc nhỏ là một cặp trạng thái–hành động. Với phép ước lượng Monte Carlo cho $v_\pi$, nút gốc là một nút trạng thái, và bên dưới là toàn bộ quỹ đạo của đúng một lượt đã lấy mẫu, kết thúc ở trạng thái kết thúc.

- (a) Mô tả sơ đồ dự phòng của phép ước lượng Monte Carlo cho $q_\pi$: nút gốc, các nút bên dưới và nút cuối.
- (b) So với sơ đồ của Monte Carlo cho $v_\pi$, nêu phần nào của sơ đồ thay đổi và lý do.
:::

::: hint Gợi ý Bài tập 06.14
Đại lượng được cập nhật là $Q(s,a)$, nên nút gốc ứng với một cặp. Lợi tức dùng trong cập nhật là tổng có chiết khấu của mọi phần thưởng từ cặp đó tới hết lượt (Định nghĩa 06.8).
:::

::: solution Lời giải Bài tập 06.14
**Câu (a).** Nút gốc là một chấm đặc, ứng với cặp $(s,a)$ được cập nhật. Bên dưới là quỹ đạo của một lượt đã lấy mẫu, xuất phát từ cặp đó: phần thưởng $R_{t+1}$ và trạng thái $S_{t+1}$ (vòng tròn rỗng), rồi cặp $(S_{t+1},A_{t+1})$ với $A_{t+1}$ chọn theo $\pi$ (chấm đặc), cứ thế xen kẽ trạng thái và cặp trạng thái–hành động cho tới nút cuối là trạng thái kết thúc $S_T$. Mỗi tầng chỉ có một nhánh, vì sơ đồ chỉ vẽ các chuyển đã xảy ra trong lượt. Mọi phần thưởng $R_{t+1},\dots,R_T$ trên đường đều góp vào lợi tức $G_t$ dùng để cập nhật $Q(s,a)$.

**Câu (b).** Chỉ nút gốc thay đổi: nút gốc là cặp $(s,a)$ thay cho trạng thái $s$, nên hành động đầu tiên đã cố định là $a$ và không được lấy theo $\pi$. Phần bên dưới vẫn là một quỹ đạo duy nhất kéo dài tới hết lượt, vì mục tiêu của Monte Carlo vẫn là lợi tức hoàn chỉnh. Sơ đồ này khớp với định nghĩa $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$: điều kiện $A_t=a$ cố định hành động đầu, còn $\pi$ quyết định các hành động từ $A_{t+1}$ trở đi.

**Kiểm tra lại.** Sơ đồ của Sarsa (sách, trang 129) cũng có gốc là một chấm đặc, nhưng dừng sau một chuyển ở cặp $(S_{t+1},A_{t+1})$, vì mục tiêu Sarsa chỉ dùng $R_{t+1}$ và $Q(S_{t+1},A_{t+1})$. Hai lỗi thường gặp: vẽ mọi hành động và mọi trạng thái kế tiếp có thể như sơ đồ của quy hoạch động, trong khi Monte Carlo chỉ dùng các chuyển đã lấy mẫu; và dừng sơ đồ sau một bước, trong khi lợi tức Monte Carlo cần mọi phần thưởng tới cuối lượt.
:::

### Bài tập 06.15. Lý do Q-learning là phương pháp khác chính sách

**Mức độ:** nhận biết; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.11, §6.5, trang 132; công thức (6.8) và thuật toán Q-learning, trang 131.

::: exercise Bài tập 06.15 (Lý do Q-learning là phương pháp khác chính sách)
Q-learning cập nhật sau mỗi chuyển $(S_t,A_t,R_{t+1},S_{t+1})$ theo
$$
\begin{aligned}
&Q(S_t,A_t)\\
&\leftarrow Q(S_t,A_t)+\alpha\Big[R_{t+1}\\
&\qquad+\gamma\max_aQ(S_{t+1},a)\\
&\qquad-Q(S_t,A_t)\Big],
\end{aligned}
$$
trong đó hành động $A_t$ được chọn theo một chính sách lập từ $Q$, chẳng hạn chính sách $\varepsilon$-tham lam. Chính sách hành vi $b$ là chính sách chọn các hành động được thực hiện; chính sách đích $\pi$ là chính sách có giá trị được bảng xấp xỉ; một phương pháp học khác chính sách (off-policy) khi $b$ có thể khác $\pi$ (Định nghĩa 06.14).

Giải thích vì sao Q-learning được xem là một phương pháp điều khiển khác chính sách.
:::

::: hint Gợi ý Bài tập 06.15
Xác định chính sách nào chọn $A_t$ và chính sách nào quyết định phần tiếp nối $\max_aQ(S_{t+1},a)$ trong mục tiêu.
:::

::: solution Lời giải Bài tập 06.15
Hành động được thực hiện do chính sách hành vi $b$ chọn, chẳng hạn chính sách $\varepsilon$-tham lam theo $Q$; $b$ vẫn thăm dò. Phần tiếp nối trong mục tiêu là $\max_aQ(S_{t+1},a)$, tức giá trị của hành động mà chính sách tham lam theo $Q$ sẽ chọn tại $S_{t+1}$, bất kể $b$ chọn gì ở bước sau. Vậy mục tiêu đánh giá chính sách đích $\pi$ là chính sách tham lam theo $Q$, và bảng xấp xỉ $q_*$ trực tiếp (sách, trang 131). Vì $b$ thăm dò còn $\pi$ thì không, hai chính sách khác nhau, nên Q-learning học khác chính sách.

Hành vi $b$ chỉ quyết định cặp $(S_t,A_t)$ nào được cập nhật. Ô được cập nhật đã lấy $A_t$ làm điều kiện, và phần tiếp nối được tính bằng phép cực đại trên bảng thay cho một hành động lấy mẫu từ $b$, nên Q-learning một bước không cần tỉ số lấy mẫu quan trọng (Nhận xét 06.17).

**Kiểm tra lại.** Với Sarsa, phần tiếp nối $Q(S_{t+1},A_{t+1})$ dùng đúng hành động $A_{t+1}$ do chính sách đang sinh dữ liệu chọn, nên $b=\pi$ và Sarsa học theo chính sách. Hai lỗi thường gặp: coi Q-learning là theo chính sách vì $b$ được lập từ chính bảng $Q$, trong khi mục tiêu vẫn đánh giá chính sách tham lam khác $b$; và cho rằng hành vi không ảnh hưởng tới kết quả học, trong khi $b$ quyết định cặp nào được cập nhật.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 06.16. Monte Carlo khởi đầu thăm dò với trung bình gia tăng

**Mức độ:** tính toán; mục tiêu học tập 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 5.4, §5.3, trang 99; mã giả Monte Carlo ES, trang 99; trung bình gia tăng, §2.4, trang 31.

::: exercise Bài tập 06.16 (Monte Carlo khởi đầu thăm dò với trung bình gia tăng)
Thuật toán Monte Carlo khởi đầu thăm dò (Monte Carlo with exploring starts, Monte Carlo ES) ước lượng chính sách tối ưu như sau.

**Khởi tạo.** Với mọi $s\in\mathcal S$ và $a\in\mathcal A(s)$: $\pi(s)\in\mathcal A(s)$ tùy ý; $Q(s,a)\in\mathbb R$ tùy ý; $\mathit{Returns}(s,a)$ là danh sách rỗng.

**Lặp mãi, mỗi vòng một lượt.**

1. Chọn ngẫu nhiên $S_0\in\mathcal S$ và $A_0\in\mathcal A(S_0)$ sao cho mọi cặp có xác suất dương.
2. Sinh một lượt từ $S_0,A_0$ theo $\pi$: $S_0,A_0,R_1,\dots,S_{T-1},A_{T-1},R_T$.
3. Đặt $G\leftarrow0$.
4. Với mỗi bước của lượt, $t=T-1,T-2,\dots,0$:
   - $G\leftarrow\gamma G+R_{t+1}$;
   - nếu cặp $(S_t,A_t)$ không xuất hiện trong $S_0,A_0,S_1,A_1,\dots,S_{t-1},A_{t-1}$: thêm $G$ vào $\mathit{Returns}(S_t,A_t)$; đặt $Q(S_t,A_t)\leftarrow\operatorname{average}(\mathit{Returns}(S_t,A_t))$, trung bình số học của danh sách; đặt $\pi(S_t)\leftarrow\operatorname*{arg\,max}_aQ(S_t,a)$.

Mã giả này giữ cho mỗi cặp danh sách mọi lợi tức đã nhận và tính lại trung bình của cả danh sách sau mỗi lợi tức mới.

- (a) Sửa mã giả để mỗi cặp chỉ giữ giá trị trung bình $Q(s,a)$ và một bộ đếm, cập nhật gia tăng theo $Q_{n+1}=Q_n+\tfrac1n\,[R_n-Q_n]$ của §2.4.
- (b) Chứng minh rằng sau khi cặp $(s,a)$ nhận $n\ge1$ lợi tức $g_1,\dots,g_n$, bản sửa cho $Q(s,a)=\tfrac1n\sum_{i=1}^ng_i$, đúng giá trị mà mã giả gốc tính, dù $Q(s,a)$ được khởi tạo tùy ý.
- (c) So sánh bộ nhớ và số phép tính của mỗi cập nhật giữa mã giả gốc và bản sửa, khi cặp đã nhận $n$ lợi tức.
:::

::: hint Gợi ý Bài tập 06.16
Thay danh sách $\mathit{Returns}(s,a)$ bằng một số nguyên $N(s,a)$ bắt đầu từ $0$. Ở (b), quy nạp theo $n$ và chú ý giá trị của bước học khi $n=1$.
:::

::: solution Lời giải Bài tập 06.16
**Câu (a).** Phần khởi tạo thay "$\mathit{Returns}(s,a)$ là danh sách rỗng" bằng "$N(s,a)\leftarrow0$". Trong vòng lặp theo $t$, khi $(S_t,A_t)$ chưa xuất hiện ở các bước trước, ba dòng cập nhật thành
$$
\begin{aligned}
N(S_t,A_t)&\leftarrow N(S_t,A_t)+1,\\
Q(S_t,A_t)&\leftarrow Q(S_t,A_t)\\
&\quad+\frac{G-Q(S_t,A_t)}{N(S_t,A_t)},\\
\pi(S_t)&\leftarrow\operatorname*{arg\,max}_aQ(S_t,a).
\end{aligned}
$$
Bộ đếm tăng trước khi chia. Các bước còn lại, gồm điều kiện lần ghé đầu tiên và phép tính $G\leftarrow\gamma G+R_{t+1}$, giữ nguyên. Đây là bước 4 của Thuật toán 06.9, với khởi đầu thăm dò thay cho chính sách $\varepsilon$-tham lam.

**Câu (b).** Gọi $Q^{(n)}$ là giá trị của $Q(s,a)$ sau lợi tức thứ $n$ và $Q^{(0)}$ là giá trị khởi tạo tùy ý.

- Với $n=1$: bộ đếm bằng $1$, nên $Q^{(1)}=Q^{(0)}+(g_1-Q^{(0)})/1=g_1$; giá trị khởi tạo bị thay hẳn.
- Giả sử $Q^{(n-1)}=\tfrac1{n-1}\sum_{i=1}^{n-1}g_i$ với $n\ge2$. Khi đó
$$
\begin{aligned}
Q^{(n)}&=Q^{(n-1)}\\
&\quad+\frac{g_n-Q^{(n-1)}}{n}\\
&=\frac{(n-1)Q^{(n-1)}+g_n}{n}\\
&=\frac1n\sum_{i=1}^ng_i .
\end{aligned}
$$

Theo quy nạp, $Q^{(n)}$ bằng trung bình số học của $n$ lợi tức với mọi $n\ge1$, tức đúng $\operatorname{average}(\mathit{Returns}(s,a))$ của mã giả gốc (Mệnh đề 05.9).

**Câu (c).** Mã giả gốc giữ $n$ số cho cặp và tốn $n-1$ phép cộng và một phép chia để tính lại trung bình sau lợi tức thứ $n$; bộ nhớ của mọi cặp tăng theo tổng số lợi tức đã nhận. Bản sửa giữ hai số cho mỗi cặp, $Q(s,a)$ và $N(s,a)$, và mỗi cập nhật tốn một số phép tính cố định, không phụ thuộc $n$.

**Kiểm tra lại.** Với hai lợi tức $g_1,g_2$: $Q^{(1)}=g_1$ và $Q^{(2)}=g_1+(g_2-g_1)/2=(g_1+g_2)/2$. Ba lỗi thường gặp: chia cho $N+1$ hoặc tăng bộ đếm sau khi chia, như thể giá trị khởi tạo là một quan sát; dùng số lượt toàn cục thay cho bộ đếm của từng cặp; và bỏ điều kiện lần ghé đầu tiên khi sửa, làm thuật toán thành Monte Carlo mọi lần ghé.
:::

### Bài tập 06.17. Sai số Monte Carlo của giá trị hành động là tổng các sai lệch Sarsa

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.8, §6.4, trang 129; đẳng thức (6.6), §6.1, trang 121.

::: exercise Bài tập 06.17 (Sai số Monte Carlo của giá trị hành động là tổng các sai lệch Sarsa)
Xét một lượt $S_0,A_0,R_1,S_1,A_1,\dots,R_T,S_T$ kết thúc tại $T<\infty$, với lợi tức $G_t=R_{t+1}+\gamma G_{t+1}$ và $G_T=0$. Với bảng giá trị trạng thái $V$ có $V(S_T)=0$ và không thay đổi trong lượt, sai lệch TD $\delta^V_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$ thỏa đẳng thức (6.6) của sách:
$$
G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta^V_k .
$$

Với bảng giá trị hành động $Q$ có $Q(S_T,\cdot)=0$, sai lệch Sarsa là $\delta_t=R_{t+1}+\gamma Q(S_{t+1},A_{t+1})-Q(S_t,A_t)$, với quy ước $Q(S_T,A_T)=0$ vì không có hành động sau trạng thái kết thúc (sách, trang 129).

- (a) Giả sử $Q$ không thay đổi trong lượt. Chứng minh $G_t-Q(S_t,A_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$ với mọi $t=0,\dots,T-1$.
- (b) Chỉ ra bước nào của chứng minh dùng giả thiết $Q$ không thay đổi trong lượt.
:::

::: hint Gợi ý Bài tập 06.17
Cộng và trừ $\gamma Q(S_{t+1},A_{t+1})$ vào $G_t-Q(S_t,A_t)$, rồi dùng hệ thức truy hồi của lợi tức để đưa về cùng biểu thức tại $t+1$.
:::

::: solution Lời giải Bài tập 06.17
**Câu (a).** Đặt $e_t=G_t-Q(S_t,A_t)$ với $t=0,\dots,T$. Với $t\le T-1$,
$$
\begin{aligned}
e_t&=R_{t+1}+\gamma G_{t+1}\\
&\quad-Q(S_t,A_t)\\
&=\delta_t+\gamma G_{t+1}\\
&\quad-\gamma Q(S_{t+1},A_{t+1})\\
&=\delta_t+\gamma e_{t+1}.
\end{aligned}
$$
Dấu bằng thứ nhất dùng $G_t=R_{t+1}+\gamma G_{t+1}$; dấu bằng thứ hai cộng và trừ $\gamma Q(S_{t+1},A_{t+1})$ rồi dùng định nghĩa của $\delta_t$; dấu bằng thứ ba là định nghĩa của $e_{t+1}$. Vậy $e_t=\delta_t+\gamma e_{t+1}$ với $t=0,\dots,T-1$, và $e_T=G_T-Q(S_T,A_T)=0-0=0$.

Chứng minh $e_t=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k$ bằng quy nạp lùi theo $t$. Với $t=T-1$: $e_{T-1}=\delta_{T-1}+\gamma e_T=\delta_{T-1}$, khớp tổng một số hạng. Nếu đẳng thức đúng tại $t+1$, thì
$$
\begin{aligned}
e_t&=\delta_t+\gamma\sum_{k=t+1}^{T-1}\gamma^{k-t-1}\delta_k\\
&=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k .
\end{aligned}
$$

**Câu (b).** Giả thiết được dùng ở bước thay $\gamma Q(S_{t+1},A_{t+1})$ trong biểu thức của $e_t$ bằng cùng số hạng trong $\delta_t$ và trong $e_{t+1}$. Ba số hạng này phải đọc từ cùng một bảng. Nếu bảng được cập nhật sau mỗi chuyển, như trong Thuật toán 06.12, đặt $e_t=G_t-Q_t(S_t,A_t)$; khi đó $\delta_t$ dùng $Q_t(S_{t+1},A_{t+1})$ còn $e_{t+1}$ dùng $Q_{t+1}(S_{t+1},A_{t+1})$, nên
$$
\begin{aligned}
e_t&=\delta_t+\gamma e_{t+1}\\
&\quad+\gamma Q_{t+1}(S_{t+1},A_{t+1})\\
&\quad-\gamma Q_t(S_{t+1},A_{t+1}).
\end{aligned}
$$
Sarsa chỉ đổi ô $(S_t,A_t)$, nên số hạng thêm bằng $0$ trừ khi $(S_{t+1},A_{t+1})=(S_t,A_t)$; khi cặp lặp lại ngay ở bước kế, $\gamma>0$ và $\delta_t\ne0$, số hạng thêm bằng $\gamma\alpha_t\delta_t\ne0$ và đẳng thức không còn chính xác. Sách nêu rằng với bước học nhỏ, đẳng thức vẫn đúng xấp xỉ (sách, trang 121, cho trường hợp $V$).

**Kiểm tra lại.** Với $T=1$: $e_0=G_0-Q(S_0,A_0)=R_1-Q(S_0,A_0)$ và $\delta_0=R_1+\gamma\cdot0-Q(S_0,A_0)$, hai vế bằng nhau. Hai lỗi thường gặp: quên điều kiện $Q(S_T,\cdot)=0$, làm thừa số hạng $\gamma^{T-t}Q(S_T,A_T)$ ở cuối tổng; và dùng $\max_aQ(S_{t+1},a)$ thay cho $Q(S_{t+1},A_{t+1})$, khi đó các số hạng không triệt tiêu, trừ khi mọi $A_{t+1}$ đạt cực đại.
:::

### Bài tập 06.18. Q-learning và Sarsa khi chọn hành động tham lam

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.12, §6.5, trang 132; thuật toán Sarsa, trang 130, và Q-learning, trang 131.

::: exercise Bài tập 06.18 (Q-learning và Sarsa khi chọn hành động tham lam)
Hai thuật toán dùng cùng bước học $\alpha\in(0,1]$, cùng bảng khởi tạo với $Q(\text{kết thúc},\cdot)=0$, và cùng quy tắc chọn hành động: chọn hành động tham lam theo bảng hiện tại, phá hòa theo cùng một quy tắc tất định.

**Sarsa.** Mỗi lượt: khởi tạo $S$; chọn $A$ từ $S$ theo quy tắc trên. Với mỗi bước: thực hiện $A$, quan sát $R$, $S'$; chọn $A'$ từ $S'$ theo quy tắc trên; $Q(S,A)\leftarrow Q(S,A)+\alpha[R+\gamma Q(S',A')-Q(S,A)]$; $S\leftarrow S'$, $A\leftarrow A'$; dừng khi $S$ kết thúc.

**Q-learning.** Mỗi lượt: khởi tạo $S$. Với mỗi bước: chọn $A$ từ $S$ theo quy tắc trên; thực hiện $A$, quan sát $R$, $S'$; $Q(S,A)\leftarrow Q(S,A)+\alpha[R+\gamma\max_aQ(S',a)-Q(S,A)]$; $S\leftarrow S'$; dừng khi $S$ kết thúc.

- (a) Xác định Q-learning có trùng hoàn toàn với Sarsa hay không.
- (b) Xác định hai thuật toán có luôn chọn cùng các hành động và thực hiện cùng các cập nhật trên cùng một môi trường hay không.
:::

::: hint Gợi ý Bài tập 06.18
So sánh mục tiêu của hai thuật toán tại một bước khi hai bảng đang bằng nhau. Sau đó xét thời điểm mỗi thuật toán chọn hành động tại $S'$: trước hay sau cập nhật, và cập nhật có đổi hàng $S'$ của bảng không.
:::

::: solution Lời giải Bài tập 06.18
**Câu (a).** Không. Giả sử hai thuật toán đang ở cùng $S$, cùng $A$ và cùng bảng $Q$. Sarsa chọn $A'$ tham lam từ bảng chưa cập nhật, nên $Q(S',A')=\max_aQ(S',a)$, và hai mục tiêu bằng nhau; khi $S'$ kết thúc, cả hai mục tiêu bằng $R$. Vậy hai thuật toán thực hiện cùng cập nhật tại bước này. Khác biệt nằm ở thời điểm chọn hành động tại $S'$: Sarsa đã cam kết thực hiện $A'$, chọn trước cập nhật, còn Q-learning chọn hành động tại $S'$ sau cập nhật, theo bảng đã cập nhật.

**Câu (b).** Cập nhật chỉ đổi ô $Q(S,A)$.

- Nếu $S'\ne S$, hàng $S'$ không đổi, nên hành động tham lam tại $S'$ trước và sau cập nhật là một; hai thuật toán chọn cùng hành động.
- Nếu $S'=S$, cập nhật có thể đổi hành động tham lam của chính hàng $S$. Ví dụ: một trạng thái $s$ có hai hành động, $Q(s,0)=1$, $Q(s,1)=0$; hành động $0$ đưa tác tử về lại $s$ với phần thưởng $-2$; $\gamma=1$, $\alpha=1$. Sarsa chọn $A'=0$ trước cập nhật, mục tiêu là $-2+Q(s,0)=-1$; Q-learning có mục tiêu $-2+\max(1,0)=-1$. Cả hai đặt $Q(s,0)=-1$. Sau đó Sarsa thực hiện $A'=0$, còn Q-learning chọn theo hàng mới $(-1;\,0)$ và thực hiện hành động $1$.

Từ bước đó, hai quỹ đạo và hai dãy cập nhật tách nhau. Vậy hai thuật toán chọn cùng hành động và thực hiện cùng cập nhật trên mọi lượt mà mỗi chuyển có $S'\ne S$, hoặc có $S'=S$ nhưng cập nhật không đổi hành động tham lam của hàng $S$; trong trường hợp còn lại, chúng chọn hai hành động khác nhau tại bước đó.

**Kiểm tra lại.** Trong ví dụ, mục tiêu của cả hai là $-1$ và $Q(s,0)$ mới là $1+1\cdot(-1-1)=-1<0=Q(s,1)$, nên hành động tham lam của hàng $s$ đổi từ $0$ sang $1$. Hai lỗi thường gặp: kết luận "trùng hoàn toàn" chỉ từ việc hai mục tiêu bằng nhau, bỏ qua thời điểm chọn hành động; và cho rằng hai thuật toán khác nhau ở mọi bước, trong khi khi $S'\ne S$ chúng chọn cùng hành động (ghi chú, Mục 4.3).
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 06.19. Thế giới lưới có gió với nước đi của quân vua

**Mức độ:** vận dụng; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 6.9, §6.4, trang 131; dữ kiện của Ví dụ 6.5, trang 130.

::: exercise Bài tập 06.19 (Thế giới lưới có gió với nước đi của quân vua)
Thế giới lưới có gió (windy gridworld) gồm $7$ hàng và $10$ cột; đánh số hàng $1$ đến $7$ từ trên xuống và cột $1$ đến $10$ từ trái sang. Ô xuất phát S ở hàng $4$, cột $1$; ô đích G ở hàng $4$, cột $8$. Bốn hành động chuẩn là lên, xuống, phải, trái, mỗi hành động dời một ô. Ở mỗi bước, gió của cột chứa tác tử đẩy trạng thái kế tiếp lên trên thêm số ô ghi dưới cột đó:

| Cột | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Gió (số ô đẩy lên) | 0 | 0 | 0 | 1 | 1 | 1 | 2 | 2 | 1 | 0 |

Ví dụ: tác tử ở ô ngay bên phải G (hàng $4$, cột $9$) chọn trái thì tới ô ngay trên G (hàng $3$, cột $8$). Giả sử vị trí sau mỗi bước được giữ trong lưới: hàng hoặc cột vượt biên được đưa về biên gần nhất. Mỗi bước nhận phần thưởng $-1$ cho tới khi vào G; nhiệm vụ có lượt và không chiết khấu ($\gamma=1$). Trong Ví dụ 6.5 của sách, Sarsa dùng chính sách $\varepsilon$-tham lam với $\varepsilon=0{,}1$.

Nước đi của quân vua (King's moves) thêm bốn hành động chéo: lên-phải, lên-trái, xuống-phải, xuống-trái, mỗi hành động dời một hàng và một cột trước khi gió tác động.

- (a) Tính số bước nhỏ nhất của một lượt từ S tới G với bốn hành động, với tám hành động của quân vua, và với chín hành động gồm tám hành động trên cộng hành động đứng yên, chỉ để gió dời tác tử.
- (b) Trả lời câu hỏi của sách: thêm bốn nước chéo cải thiện được bao nhiêu, và thêm hành động thứ chín có cải thiện thêm không.
:::

::: hint Gợi ý Bài tập 06.19
Ở (a), mỗi hành động đổi cột nhiều nhất một đơn vị, còn gió chỉ đổi hàng; G cách S bảy cột. Với bốn hành động, liệt kê đường đi bằng tìm kiếm theo chiều rộng trên $70$ ô, hoặc lần theo đường đi phải dọc hàng trên cùng.
:::

::: solution Lời giải Bài tập 06.19
**Câu (a).** Ghi vị trí theo (hàng, cột).

- Bốn hành động: $15$ bước, khớp giá trị nhỏ nhất mà sách nêu ở Ví dụ 6.5. Một đường đi ngắn nhất là phải chín lần, $(4,1)\to(4,2)\to(4,3)\to(4,4)\to(3,5)\to(2,6)\to(1,7)\to(1,8)\to(1,9)\to(1,10)$ (gió đẩy lên từ cột $4$, ở hàng $1$ thì giữ tại biên); xuống bốn lần tới $(5,10)$; trái hai lần, $(5,10)\to(5,9)\to(4,8)$. Tìm kiếm theo chiều rộng trên $70$ ô không cho đường nào ngắn hơn.
- Tám hành động: $7$ bước. Cận dưới: mỗi hành động đổi cột nhiều nhất một đơn vị và gió không đổi cột, nên từ cột $1$ tới cột $8$ cần ít nhất $7$ bước. Cận này đạt được: phải, phải, rồi xuống-phải năm lần, $(4,1)\to(4,2)\to(4,3)\to(5,4)\to(5,5)\to(5,6)\to(5,7)\to(4,8)$. Ở cột $4$, $5$, $6$, nước xuống-phải và gió $1$ triệt tiêu nhau theo hàng; ở cột $7$, gió $2$ đẩy tác tử từ hàng $5+1$ lên hàng $4$.
- Chín hành động: vẫn $7$ bước, vì hành động đứng yên không đổi cột, nên cận dưới $7$ vẫn đúng và đường đi trên vẫn dùng được.

**Câu (b).** Bốn nước chéo giảm số bước nhỏ nhất từ $15$ xuống $7$, ít hơn $8$ bước. Hành động đứng yên không giảm được dưới $7$, vì cận dưới theo số cột vẫn giữ nguyên; nó chỉ thêm $70$ ô vào bảng cần học, từ $70\cdot8=560$ lên $70\cdot9=630$ ô. Số bước nhỏ nhất là độ dài lượt của chính sách tối ưu; Sarsa $\varepsilon$-tham lam còn thực hiện các bước thăm dò, nên với bốn hành động sách ghi độ dài lượt trung bình khoảng $17$ bước, hơn mức nhỏ nhất $15$ hai bước (Ví dụ 6.5).

**Kiểm tra lại.** Đường đi tám hành động, từng bước: $(4,3)$, gió cột $3$ bằng $0$, xuống-phải tới $(5,4)$; ở cột $4$, gió $1$: $5+1-1=5$, tới $(5,5)$; tương tự ở cột $5$ tới $(5,6)$ và ở cột $6$ tới $(5,7)$; ở cột $7$, gió $2$: $5+1-2=4$, tới $(4,8)=\text{G}$. Hai lỗi thường gặp: dùng gió của cột đích thay cho cột hiện tại, trái với ví dụ trong đề; và đọc độ dài trung bình của các lượt $\varepsilon$-tham lam như độ dài của chính sách học được.
:::

## Tài liệu tham khảo

- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 5.3, §5.2, trang 97, cùng quy ước sơ đồ dự phòng ở §3.5, trang 59, và §5.1, trang 94–95 (Bài tập 06.14); Bài tập 5.4 và mã giả Monte Carlo ES, §5.3, trang 99, cùng công thức (2.3), §2.4, trang 31 (Bài tập 06.16); Bài tập 6.8, §6.4, trang 129, và đẳng thức (6.6), §6.1, trang 121 (Bài tập 06.17); Bài tập 6.9, §6.4, trang 131, và Ví dụ 6.5, trang 130 (Bài tập 06.19); Bài tập 6.11, 6.12, §6.5, trang 132, cùng các thuật toán Sarsa và Q-learning, trang 130–131 (Bài tập 06.15, 06.18).
- [Ghi chú bài giảng Bài 06](material-viewer.html?doc=materials/lec-06/lecture-note.md&deck=lecture-06-dieu-khien-phi-mo-hinh.html): ký hiệu và các số hiệu được dẫn trong đề và lời giải.
