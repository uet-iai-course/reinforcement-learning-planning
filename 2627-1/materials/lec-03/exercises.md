# Bài tập Bài 03 — Quá trình quyết định Markov

Tệp gồm năm bài, Bài tập 03.15–03.19, đánh số tiếp theo mười bốn bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-03/lecture-note.md&deck=lecture-03-qua-trinh-quyet-dinh-markov.html) (Bài tập 03.1–03.14) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập chương 3 của Sutton và Barto (2018); mỗi bài ghi số bài, mục và trang của sách. Các bài chia theo ba mức: nhận biết (03.15, 03.16); tính toán hoặc chứng minh (03.17, 03.18); vận dụng vào bài toán Học tăng cường (03.19).

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/1/1) | — |
| 2. Trạng thái Markov và mô hình môi trường | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/1) | ghi chú: 03.1, 03.2 |
| 3. Lợi tức chiết khấu | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/3/1) | ghi chú: 03.3, 03.10 |
| 4. Chính sách và hàm giá trị | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/1) | ghi chú: 03.4, 03.5 |
| 5. Phương trình Bellman kỳ vọng | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/5/1) | 03.15–03.18; ghi chú: 03.6, 03.7, 03.11, 03.12 |
| 6. Đánh giá chính sách bằng hệ tuyến tính | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/1) | 03.19; ghi chú: 03.8, 03.9, 03.14 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/7/1) | ghi chú: 03.13 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 03; công thức của ghi chú được dẫn bằng số trong ngoặc, chẳng hạn (4.5), còn công thức của sách được ghi rõ "của sách". Môi trường là một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn $\bigl(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p\bigr)$ (Định nghĩa 03.7): $\mathcal S$ là tập trạng thái chưa kết thúc, $\mathcal S^+$ là $\mathcal S$ thêm các trạng thái kết thúc, $\mathcal A(s)$ là tập hành động hợp lệ tại $s$, $\mathcal R$ là tập phần thưởng hữu hạn. Hàm động lực bốn đối số là
$$
\begin{aligned}
&p(s',r\mid s,a)\\
&\quad=\Pr\bigl(S_{t+1}=s',R_{t+1}=r\\
&\qquad\quad\mid S_t=s,A_t=a\bigr),
\end{aligned}
$$
đúng mỗi khi sự kiện điều kiện có xác suất dương (1.4); xác suất chuyển và thưởng kỳ vọng một bước là $p(s'\mid s,a)=\sum_rp(s',r\mid s,a)$ và $r(s,a)=\sum_{s',r}r\,p(s',r\mid s,a)$ (Mệnh đề 03.6).

Chính sách $\pi$ là chính sách Markov dừng (Định nghĩa 03.13): tác tử theo $\pi$ tại thời điểm $t$ nếu $\Pr(A_t=a\mid H_t=h_t)=\pi(a\mid s)$ với mọi lịch sử $h_t$ có xác suất dương kết thúc ở $s$, công thức (3.1). Phần thưởng bị chặn, $\lvert R_{t+1}\rvert\le M$, và $0\le\gamma<1$; lợi tức $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$ thỏa $\lvert G_t\rvert\le M/(1-\gamma)$ (Mệnh đề 03.11) và $G_t=R_{t+1}+\gamma G_{t+1}$ (Bổ đề 03.18). Giá trị trạng thái $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$ lấy trên quá trình xuất phát tại $s$ (Định nghĩa 03.15); giá trị hành động $q_\pi(s,a)=\mathbb E_\pi[G_0\mid S_0=s,A_0=a]$ lấy trên quá trình ấn định $S_0=s$, $A_0=a$ rồi theo $\pi$ từ thời điểm $1$ (Định nghĩa 03.16). Giá trị tại trạng thái kết thúc bằng $0$.

Tương ứng với sách: hàm bốn đối số (3.2) của sách là (1.4); (3.8) của sách là (2.1); (3.12), (3.13) của sách viết $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ và $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ với $t$ bất kỳ, và theo Bổ đề 03.20(c), (d) hai kỳ vọng này bằng (3.3), (3.4) của ghi chú khi sự kiện điều kiện có xác suất dương; (3.14) của sách là (4.5).

Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}9$.

## Mức nhận biết

### Bài tập 03.15. Giá trị trạng thái theo giá trị hành động

**Mức độ:** nhận biết; mục tiêu học tập 3 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.12, §3.5, trang 58.

::: exercise Bài tập 03.15 (Giá trị trạng thái theo giá trị hành động)
Cho MDP hữu hạn, chính sách Markov dừng $\pi$, phần thưởng bị chặn và $0\le\gamma<1$. Với $s\in\mathcal S$, giá trị trạng thái $v_\pi(s)$ và các giá trị hành động $q_\pi(s,a)$, $a\in\mathcal A(s)$, định nghĩa như trong phần Hướng dẫn.

- (a) Viết một đẳng thức biểu diễn $v_\pi(s)$ qua $\pi(\cdot\mid s)$ và các $q_\pi(s,a)$, $a\in\mathcal A(s)$.
- (b) Nêu căn cứ của từng bước dẫn tới đẳng thức ở câu (a).
:::

::: hint Gợi ý Bài tập 03.15
Trong quá trình xuất phát tại $s$, nhóm các quỹ đạo theo hành động đầu $A_0$.
:::

::: solution Lời giải Bài tập 03.15
**Câu (a).**
$$
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,q_\pi(s,a).
$$

**Câu (b).** Xét quá trình xuất phát tại $s$, nên $H_0=(s)$ và tác tử theo $\pi$ từ thời điểm $0$.

- Áp dụng tầng hành động (4.3) của Bổ đề 03.19 với $X=G_0$, biến bị chặn bởi $M/(1-\gamma)$: $v_\pi(s)=\sum_a\pi(a\mid s)\,\mathbb E_\pi[G_0\mid S_0=s,A_0=a]$, tổng lấy trên các $a$ có $\pi(a\mid s)>0$.
- Với mỗi $a$ như vậy, Bổ đề 03.20(d) tại $t=0$ cho $\mathbb E_\pi[G_0\mid S_0=s,A_0=a]=q_\pi(s,a)$.
- Các $a$ có $\pi(a\mid s)=0$ góp số hạng $0\cdot q_\pi(s,a)=0$ vì $\lvert q_\pi(s,a)\rvert\le M/(1-\gamma)$, nên tổng lấy được trên toàn bộ $\mathcal A(s)$.

Ba bước này là chứng minh Mệnh đề 03.23, đẳng thức (4.7).

**Kiểm tra lại.** Trọng số là xác suất chính sách chọn từng hành động, có tổng $1$, nên $v_\pi(s)$ nằm giữa giá trị hành động nhỏ nhất và lớn nhất tại $s$. Hai lỗi thường gặp: thay trung bình bằng $\max_aq_\pi(s,a)$, tức là nhầm bài toán dự đoán với bài toán điều khiển (Nhận xét 03.25); dùng trọng số đều $1/\lvert\mathcal A(s)\rvert$ khi $\pi$ không chọn đều.
:::

### Bài tập 03.16. Giá trị hành động theo giá trị trạng thái

**Mức độ:** nhận biết; mục tiêu học tập 3 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.13, §3.5, trang 58.

::: exercise Bài tập 03.16 (Giá trị hành động theo giá trị trạng thái)
Cho MDP hữu hạn với hàm động lực bốn đối số $p(s',r\mid s,a)$, chính sách Markov dừng $\pi$, phần thưởng bị chặn và $0\le\gamma<1$. Giá trị trạng thái tại trạng thái kết thúc bằng $0$.

- (a) Viết một đẳng thức biểu diễn $q_\pi(s,a)$, với $s\in\mathcal S$, $a\in\mathcal A(s)$, qua $v_\pi$ và hàm động lực bốn đối số $p$.
- (b) Nêu căn cứ của từng bước dẫn tới đẳng thức ở câu (a), và chỉ ra chỗ chính sách $\pi$ có mặt trong đẳng thức.
:::

::: hint Gợi ý Bài tập 03.16
Trong quá trình ấn định $(s,a)$, tách $G_0=R_1+\gamma G_1$ rồi nhóm các quỹ đạo theo phản hồi đầu $(S_1,R_1)$.
:::

::: solution Lời giải Bài tập 03.16
**Câu (a).**
$$
\begin{aligned}
&q_\pi(s,a)\\
&\quad=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma\,v_\pi(s')\bigr].
\end{aligned}
$$

**Câu (b).** Xét quá trình ấn định $(s,a)$: $S_0=s$, $A_0=a$, phản hồi theo $p$, hành động theo $\pi$ từ thời điểm $1$.

- Theo Bổ đề 03.18, $G_0=R_1+\gamma G_1$ trên mọi quỹ đạo.
- Theo quy tắc sinh quỹ đạo của Định nghĩa 03.7 với $H_0=(s)$, $A_0=a$, cặp $(S_1,R_1)$ nhận giá trị $(s',r)$ với xác suất $p(s',r\mid s,a)$. Kỳ vọng toàn phần theo $(S_1,R_1)$ cho trọng số đó, và trong nhóm $\{S_1=s',R_1=r\}$ số hạng $R_1=r$ đi ra ngoài kỳ vọng.
- Lịch sử $H_1=(s,a,r,s')$ kết thúc ở $s'$ và quá trình theo $\pi$ từ thời điểm $1$, nên khi $s'\in\mathcal S$ và $p(s',r\mid s,a)>0$, Bổ đề 03.20(b) tại thời điểm $1$ cho $\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]=v_\pi(s')$. Khi $s'$ là trạng thái kết thúc, $G_1=0=v_\pi(s')$. Các số hạng có $p(s',r\mid s,a)=0$ bằng $0$.

Ba bước này là Bước 1 của chứng minh Mệnh đề 03.22. Chính sách không có trọng số nào ở bước đầu, vì hành động đầu đã bị ấn định; $\pi$ chỉ có mặt qua các giá trị $v_\pi(s')$ của trạng thái kế tiếp.

**Kiểm tra lại.** Gom tổng theo $r$ và theo $s'$ bằng (1.5), (1.6) cho dạng thứ hai của (4.6), $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s')$. Ba lỗi thường gặp: thêm thừa số $\pi(a\mid s)$ trước tổng; viết $v_\pi(s)$ thay cho $v_\pi(s')$; quên hệ số $\gamma$ trước giá trị của trạng thái kế tiếp.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 03.17. Hai sơ đồ cập nhật một tầng

**Mức độ:** chứng minh; mục tiêu học tập 3 và 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.18 và 3.19, §3.5, trang 62.

::: exercise Bài tập 03.17 (Hai sơ đồ cập nhật một tầng)
Cho MDP hữu hạn với hàm động lực bốn đối số $p(s',r\mid s,a)$, chính sách Markov dừng $\pi$, phần thưởng bị chặn và $0\le\gamma<1$. Xét một thời điểm $t$.

- (a) Giá trị của một trạng thái phụ thuộc giá trị của các hành động có thể chọn tại đó và xác suất chính sách chọn từng hành động. Sơ đồ tương ứng có gốc là $s$, ba nhánh ứng với các hành động $a_1$, $a_2$, $a_3$, mỗi nhánh được chọn với xác suất $\pi(a\mid s)$, và lá của nhánh $a$ mang giá trị $q_\pi(s,a)$. Xét một quá trình trong đó tác tử theo $\pi$ ở mọi thời điểm. Với $s\in\mathcal S$ có $\Pr_\pi(S_t=s)>0$, viết $v_\pi(s)$ dưới dạng kỳ vọng của $q_\pi(S_t,A_t)$ khi biết $S_t=s$, với kỳ vọng lấy khi tác tử theo $\pi$. Sau đó viết đẳng thức thứ hai, trong đó kỳ vọng được khai triển theo $\pi(a\mid s)$ và không còn ký hiệu kỳ vọng.
- (b) Giá trị của một hành động phụ thuộc phần thưởng kỳ vọng ở bước kế tiếp và tổng kỳ vọng của các phần thưởng còn lại. Sơ đồ tương ứng có gốc là cặp $(s,a)$, ba nhánh ứng với ba trạng thái kế tiếp $s'_1$, $s'_2$, $s'_3$ cùng phần thưởng $r_1$, $r_2$, $r_3$, và lá của nhánh $s'$ mang giá trị $v_\pi(s')$. Xét một quá trình của MDP trong đó tác tử chọn hành động theo một quy tắc bất kỳ dựa trên lịch sử, và $s\in\mathcal S$, $a\in\mathcal A(s)$ sao cho $\Pr(S_t=s,A_t=a)>0$. Viết $q_\pi(s,a)$ dưới dạng kỳ vọng của $R_{t+1}+\gamma\,v_\pi(S_{t+1})$ khi biết $S_t=s$, $A_t=a$; kỳ vọng này không lấy điều kiện tác tử theo $\pi$. Sau đó viết đẳng thức thứ hai theo $p(s',r\mid s,a)$, không còn ký hiệu kỳ vọng.
:::

::: hint Gợi ý Bài tập 03.17
Ở mỗi câu, biến ngẫu nhiên trong kỳ vọng là hàm của một cặp biến nhận hữu hạn giá trị: $(S_t,A_t)$ ở câu (a), $(S_{t+1},R_{t+1})$ ở câu (b). Tìm phân phối có điều kiện của cặp đó.
:::

::: solution Lời giải Bài tập 03.17
**Câu (a).**
$$
\begin{aligned}
v_\pi(s)&=\mathbb E_\pi\bigl[q_\pi(S_t,A_t)\mid S_t=s\bigr]\\
&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,q_\pi(s,a).
\end{aligned}
$$

Khi biết $S_t=s$, biến $q_\pi(S_t,A_t)$ bằng $q_\pi(s,A_t)$, nên kỳ vọng của nó là $\sum_a\Pr_\pi(A_t=a\mid S_t=s)\,q_\pi(s,a)$. Theo (3.1), $\Pr_\pi(A_t=a\mid H_t=h_t)=\pi(a\mid s)$ với mọi lịch sử $h_t$ có xác suất dương kết thúc ở $s$; lấy trung bình theo các lịch sử đó, với trọng số $\Pr_\pi(H_t=h_t\mid S_t=s)$ có tổng $1$, được $\Pr_\pi(A_t=a\mid S_t=s)=\pi(a\mid s)$. Vậy kỳ vọng bằng vế phải. Vế phải bằng $v_\pi(s)$ theo Mệnh đề 03.23 (Bài tập 03.15).

Kỳ vọng phải lấy khi tác tử theo $\pi$, vì phân phối của $A_t$ khi biết $S_t=s$ chính là $\pi(\cdot\mid s)$.

**Câu (b).**
$$
\begin{aligned}
&q_\pi(s,a)\\
&\quad=\mathbb E\bigl[R_{t+1}+\gamma\,v_\pi(S_{t+1})\\
&\qquad\quad\mid S_t=s,A_t=a\bigr]\\
&\quad=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma\,v_\pi(s')\bigr].
\end{aligned}
$$

Biến $R_{t+1}+\gamma\,v_\pi(S_{t+1})$ là hàm của $(S_{t+1},R_{t+1})$. Theo (1.4) của Định nghĩa 03.4, với mọi cách chọn hành động của tác tử, khi $\Pr(S_t=s,A_t=a)>0$ cặp này có phân phối có điều kiện $p(\cdot,\cdot\mid s,a)$. Do đó kỳ vọng ở giữa bằng vế phải, dù tác tử chọn các hành động tới thời điểm $t$ theo quy tắc nào; vì thế kỳ vọng không mang chỉ số $\pi$, và đẳng thức đúng cả khi $\pi(a\mid s)=0$. Chính sách chỉ có mặt qua hàm $v_\pi$. Vế phải bằng $q_\pi(s,a)$ theo đẳng thức thứ nhất của (4.6) (Mệnh đề 03.22, Bài tập 03.16).

**Kiểm tra lại.** Lấy trung bình đẳng thức của câu (b) theo $\pi(a\mid s)$ và dùng câu (a) cho $v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma\,v_\pi(S_{t+1})\mid S_t=s]$, tức là (4.5). Lỗi thường gặp: bỏ điều kiện $A_t=a$ ở câu (b); kỳ vọng khi đó là $v_\pi(s)$ theo (4.5), không phải $q_\pi(s,a)$.
:::

### Bài tập 03.18. Phương trình Bellman cho giá trị hành động

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.17, §3.5, trang 61; đẳng thức (3.14) của sách, trang 59.

::: exercise Bài tập 03.18 (Phương trình Bellman cho giá trị hành động)
Cho MDP hữu hạn với hàm động lực bốn đối số $p(s',r\mid s,a)$, chính sách Markov dừng $\pi$, phần thưởng bị chặn và $0\le\gamma<1$. Với giá trị trạng thái, sách viết chuỗi đẳng thức (3.14): với $s\in\mathcal S$,
$$
\begin{aligned}
&v_\pi(s)\\
&\quad=\mathbb E_\pi[G_t\mid S_t=s]\\
&\quad=\mathbb E_\pi[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
&\quad=\sum_a\pi(a\mid s)\\
&\qquad\times\sum_{s'}\sum_rp(s',r\mid s,a)\\
&\qquad\times\Bigl[r+\gamma\,\mathbb E_\pi[G_{t+1}\\
&\qquad\qquad\mid S_{t+1}=s']\Bigr]\\
&\quad=\sum_a\pi(a\mid s)\\
&\qquad\times\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\bigl[r+\gamma\,v_\pi(s')\bigr].
\end{aligned}
$$
Sơ đồ cập nhật của $q_\pi$ có gốc là cặp $(s,a)$; tầng cạnh trên mang $p(s',r\mid s,a)$ và dẫn tới các trạng thái kế tiếp $s'$; tầng cạnh dưới mang $\pi(a'\mid s')$ và dẫn tới các cặp $(s',a')$.

Viết phương trình Bellman cho giá trị hành động: biểu diễn $q_\pi(s,a)$, với $s\in\mathcal S$, $a\in\mathcal A(s)$, qua các giá trị $q_\pi(s',a')$ của các cặp kế tiếp. Trình bày thành một chuỗi đẳng thức tương tự (3.14) của sách, xuất phát từ định nghĩa của $q_\pi(s,a)$, và nêu căn cứ của từng đẳng thức.
:::

::: hint Gợi ý Bài tập 03.18
So với (3.14) của sách, hai tầng kỳ vọng đổi thứ tự: tầng phản hồi đi trước, vì hành động đầu đã cố định; tầng hành động đi sau, tại trạng thái kế tiếp $s'$.
:::

::: solution Lời giải Bài tập 03.18
Làm việc trên quá trình ấn định $(s,a)$ của Định nghĩa 03.16: $S_0=s$, $A_0=a$, phản hồi theo $p$, hành động theo $\pi$ từ thời điểm $1$. Mọi lợi tức bị chặn bởi $M/(1-\gamma)$ (Mệnh đề 03.11), nên mọi kỳ vọng dưới đây tồn tại. Viết $h_1=(s,a,r,s')$. Chuỗi đẳng thức là
$$
\begin{aligned}
&q_\pi(s,a)\\
&\quad=\mathbb E_\pi[G_0\mid S_0=s,A_0=a]\\
&\quad=\mathbb E_\pi[R_1+\gamma G_1\\
&\qquad\quad\mid S_0=s,A_0=a]\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\\
&\quad\times\Bigl[r+\gamma\,\mathbb E_\pi\bigl[G_1\mid H_1=h_1\bigr]\Bigr]\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\Bigl[r+\gamma\sum_{a'}\pi(a'\mid s')\\
&\qquad\qquad\times\mathbb E_\pi\bigl[G_1\\
&\qquad\quad\mid H_1=h_1,A_1=a'\bigr]\Bigr]\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\\
&\qquad\times\Bigl[r+\gamma\sum_{a'}\pi(a'\mid s')\\
&\qquad\qquad\times q_\pi(s',a')\Bigr].
\end{aligned}
$$

Căn cứ của năm đẳng thức, theo thứ tự từ trên xuống:

1. Định nghĩa (3.4).
2. Bổ đề 03.18.
3. Kỳ vọng toàn phần theo $(S_1,R_1)$ với trọng số $p(s',r\mid s,a)$ từ quy tắc sinh quỹ đạo của Định nghĩa 03.7; trong nhóm $\{S_1=s',R_1=r\}$, $R_1=r$ đi ra ngoài kỳ vọng. Bước này trùng Bước 1 của chứng minh Mệnh đề 03.22.
4. Với $s'\in\mathcal S$ và $p(s',r\mid s,a)>0$, quá trình theo $\pi$ tại thời điểm $1$ và lịch sử $H_1=(s,a,r,s')$ kết thúc ở $s'$, nên tầng hành động (4.3) của Bổ đề 03.19, với $X=G_1$, cho tổng theo $a'$ với trọng số $\pi(a'\mid s')$, lấy trên các $a'$ có $\pi(a'\mid s')>0$.
5. Với mỗi $a'$ như vậy và mỗi $(s',r)$ có $p(s',r\mid s,a)>0$, sự kiện $\{H_1=(s,a,r,s'),A_1=a'\}$ có xác suất dương và quá trình theo $\pi$ từ thời điểm $2$, nên Bổ đề 03.20(d) tại $t=1$ cho kỳ vọng bằng $q_\pi(s',a')$.

Khi $s'$ là trạng thái kết thúc, $G_1=0$ và tổng trong ngoặc được quy ước bằng $0$. Các số hạng có $p(s',r\mid s,a)=0$ hoặc $\pi(a'\mid s')=0$ bằng $0$ vì $q_\pi$ hữu hạn, nên các tổng lấy được trên toàn bộ $\mathcal S^+$, $\mathcal R$ và $\mathcal A(s')$. Kết quả là (4.8) của Hệ quả 03.24; ghi chú thu được (4.8) bằng cách thế (4.7) vào (4.6), còn chuỗi trên đi thẳng từ định nghĩa.

**Kiểm tra lại.** Theo Bài tập 03.15, $\sum_{a'}\pi(a'\mid s')\,q_\pi(s',a')=v_\pi(s')$, nên vế phải trở thành đẳng thức thứ nhất của (4.6). Hai lỗi thường gặp: dùng trọng số $\pi(a\mid s)$ của hành động đầu thay cho $\pi(a'\mid s')$; đặt tầng chính sách ra ngoài tầng phản hồi như trong (4.5).
:::

## Vận dụng vào bài toán Học tăng cường

### Bài tập 03.19. Kiểm tra phương trình Bellman trên lưới 5×5

**Mức độ:** vận dụng; mục tiêu học tập 4 và 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 3.14, §3.5, trang 60; dữ kiện của Ví dụ 3.5 và Hình 3.2, trang 60.

::: exercise Bài tập 03.19 (Kiểm tra phương trình Bellman trên lưới 5×5)
Ví dụ 3.5 của sách: lưới $5\times5$, mỗi ô là một trạng thái, nhiệm vụ tiếp diễn. Ở mỗi ô có bốn hành động bắc, nam, đông, tây, đưa tác tử sang ô kề theo hướng đó một cách tất định. Phần thưởng và các bước nhảy:

- hành động đi ra ngoài lưới giữ nguyên ô và cho phần thưởng $-1$;
- ở ô $\mathrm A$ (hàng 1, cột 2), mọi hành động đưa tới ô $\mathrm A'$ (hàng 5, cột 2) với phần thưởng $+10$;
- ở ô $\mathrm B$ (hàng 1, cột 4), mọi hành động đưa tới ô $\mathrm B'$ (hàng 3, cột 4) với phần thưởng $+5$;
- mọi bước khác cho phần thưởng $0$.

Tác tử chọn mỗi hành động với xác suất $1/4$ ở mọi ô, và $\gamma=0{,}9$. Hình 3.2 của sách cho giá trị $v_\pi$ của chính sách này, làm tròn tới một chữ số thập phân (hàng 1 ở trên cùng, cột 1 ở bên trái):

| | cột 1 | cột 2 | cột 3 | cột 4 | cột 5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| hàng 1 | $3{,}3$ | $8{,}8$ | $4{,}4$ | $5{,}3$ | $1{,}5$ |
| hàng 2 | $1{,}5$ | $3{,}0$ | $2{,}3$ | $1{,}9$ | $0{,}5$ |
| hàng 3 | $0{,}1$ | $0{,}7$ | $0{,}7$ | $0{,}4$ | $-0{,}4$ |
| hàng 4 | $-1{,}0$ | $-0{,}4$ | $-0{,}4$ | $-0{,}6$ | $-1{,}2$ |
| hàng 5 | $-1{,}9$ | $-1{,}3$ | $-1{,}2$ | $-1{,}4$ | $-2{,}0$ |

- (a) Phương trình Bellman (4.5) phải đúng tại mọi ô. Kiểm tra bằng số rằng phương trình này đúng tại ô giữa (hàng 3, cột 3), có giá trị $+0{,}7$, với bốn ô kề có giá trị $+2{,}3$, $+0{,}4$, $-0{,}4$ và $+0{,}7$.
- (b) Kiểm tra tương tự tại ô góc dưới bên trái (hàng 5, cột 1).
- (c) Giả sử mỗi số trong bảng lệch giá trị đúng không quá $0{,}05$. Tìm một cận cho hiệu giữa vế trái và vế phải của (4.5) khi thế các số trong bảng vào, rồi kết luận về sai lệch tìm được ở câu (a) và câu (b).
:::

::: hint Gợi ý Bài tập 03.19
Mỗi hành động có xác suất $1/4$ và phản hồi tất định, nên vế phải của (4.5) là trung bình của bốn số $r+0{,}9\,v_\pi(s')$. Hành động đi ra ngoài lưới có $s'$ là chính ô đang xét.
:::

::: solution Lời giải Bài tập 03.19
**Câu (a).** Từ ô giữa, bốn hành động đưa tới bốn ô kề với phần thưởng $0$. Vế phải của (4.5) là
$$
\begin{aligned}
&\tfrac14\cdot0{,}9\cdot(2{,}3+0{,}4-0{,}4+0{,}7)\\
&\quad=0{,}225\cdot3{,}0\\
&\quad=0{,}675,
\end{aligned}
$$
và $0{,}675$ làm tròn tới một chữ số thập phân là $0{,}7$, bằng giá trị trong bảng.

**Câu (b).** Từ ô hàng 5, cột 1, hành động nam và tây đi ra ngoài lưới: mỗi hành động cho phần thưởng $-1$ và giữ nguyên ô, có giá trị $-1{,}9$. Hành động bắc tới ô hàng 4, cột 1, giá trị $-1{,}0$; hành động đông tới ô hàng 5, cột 2, giá trị $-1{,}3$; cả hai cho phần thưởng $0$. Vế phải của (4.5) là
$$
\begin{aligned}
&\tfrac14\bigl[2\,(-1+0{,}9\cdot(-1{,}9))\\
&\qquad+0{,}9\cdot(-1{,}0)\\
&\qquad+0{,}9\cdot(-1{,}3)\bigr]\\
&\quad=\tfrac14\bigl[-5{,}42-0{,}9-1{,}17\bigr]\\
&\quad=-1{,}8725,
\end{aligned}
$$
làm tròn là $-1{,}9$, bằng giá trị trong bảng.

**Câu (c).** Gọi $\tilde v=v_\pi+e$ là bảng làm tròn, với $\lvert e(s)\rvert\le0{,}05$ ở mọi ô. Giá trị đúng thỏa (4.5), nên hiệu giữa vế trái và vế phải khi thế $\tilde v$ tại ô $s$ là
$$
e(s)-0{,}9\sum_a\tfrac14\,e(s'_a),
$$
trong đó $s'_a$ là ô tới khi chọn $a$. Bốn trọng số $\tfrac14$ có tổng $1$, nên trị tuyệt đối của hiệu không quá
$$
0{,}05+0{,}9\cdot0{,}05=0{,}095.
$$
Sai lệch ở câu (a) là $\lvert0{,}7-0{,}675\rvert=0{,}025$ và ở câu (b) là $\lvert-1{,}9-(-1{,}8725)\rvert=0{,}0275$, đều nhỏ hơn $0{,}095$. Vậy bảng làm tròn thỏa (4.5) trong phạm vi sai số làm tròn.

**Kiểm tra lại.** Ở ô góc có hai hướng đi ra ngoài lưới, nên số hạng $-1+0{,}9\,v_\pi(s)$ xuất hiện hai lần và $r_\pi=-\tfrac12$. Hai lỗi thường gặp: bỏ phần $0{,}9\,v_\pi(s)$ của chính ô đó khi đi ra ngoài lưới, chỉ giữ phần thưởng $-1$; nhân $0{,}9$ cả vào phần thưởng.
:::

## Tài liệu tham khảo

- R. S. Sutton và A. G. Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: Bài tập 3.12 và 3.13, §3.5, trang 58 (Bài tập 03.15, 03.16); Bài tập 3.18 và 3.19, §3.5, trang 62 (Bài tập 03.17); Bài tập 3.17, §3.5, trang 61, cùng đẳng thức (3.14), trang 59 (Bài tập 03.18); Bài tập 3.14, Ví dụ 3.5 và Hình 3.2, §3.5, trang 60 (Bài tập 03.19).
