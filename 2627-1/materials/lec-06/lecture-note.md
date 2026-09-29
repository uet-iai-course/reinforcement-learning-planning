# Bài 06. Điều khiển phi mô hình

Học phần Học tăng cường · Học kỳ 1, năm học 2026–2027.

Điều khiển Monte Carlo (MC), Sarsa và Q-learning học giá trị hành động từ kinh nghiệm. Bài toán được xét có tập trạng thái và hành động hữu hạn, với giá trị được biểu diễn bằng bảng. Mỗi phương pháp được xác định qua dữ liệu quan sát, mục tiêu cập nhật và điều kiện bảo đảm hội tụ.

<!-- note-topic-id: lec-06-topic-01 -->
## 1. Bài toán điều khiển từ kinh nghiệm

### 1.1. Quyết định tại một trạng thái

Xét chuỗi năm trạng thái A–B–C–D–E. Mỗi lượt tương tác bắt đầu tại D. Tác tử cần chọn đi trái hoặc đi phải từ kinh nghiệm đã thu được. Đi phải từ D kết thúc ngay tại E và nhận thưởng 10. Đi trái mở ra một phần tiếp nối; kết quả của lựa chọn này còn phụ thuộc các hành động sau đó.

![Chuỗi A–B–C–D–E với D là trạng thái đầu; A và E kết thúc; nhãn cạnh chỉ hành động và phần thưởng nhận trên chuyển tiếp.](img/lec-06/chain-five-states.svg)

Tập trạng thái không kết thúc là $\mathcal S=\{B,C,D\}$. Tập có bổ sung trạng thái kết thúc là $\mathcal S^+=\{A,B,C,D,E\}$. Tại mỗi $s\in\mathcal S$, tập hành động hợp lệ là $\mathcal A(s)=\{0,1\}$: hành động 0 đi trái, hành động 1 đi phải. Chuyển trạng thái là tất định. Thưởng được nhận khi chuyển vào trạng thái kế tiếp:

| Trạng thái kế tiếp | Phần thưởng |
|---|---:|
| A | 1000 |
| E | 10 |
| B, C hoặc D | $-1$ |

Hệ số chiết khấu của ví dụ là $\gamma=1$. Lượt kết thúc khi vào A hoặc E; sau đó không có hành động trong lượt ấy. Giá trị tiếp nối tại trạng thái kết thúc bằng 0 vì phần thưởng cuối đã được nhận trên chuyển tiếp. Việc dừng ghi dữ liệu tại B, C hoặc D không biến trạng thái đó thành trạng thái kết thúc.

Mô hình này được công bố để kiểm tra phép tính. Các thuật toán phi mô hình chỉ sử dụng mẫu tương tác và tập hành động hợp lệ; chúng không dùng xác suất chuyển hay kỳ vọng phần thưởng để tính cập nhật.

### 1.2. Từ dự đoán đến điều khiển

Trong bài toán dự đoán, chính sách được cho trước và cần ước lượng giá trị của nó. Trong bài toán điều khiển, cách chọn hành động cũng cần được cải thiện. Một giá trị trạng thái mô tả kết quả trung bình khi tiếp tục theo chính sách, nhưng chưa tách riêng ảnh hưởng của từng hành động tại trạng thái ấy. Khi không biết mô hình chuyển, việc so sánh hành động cần các ước lượng theo cặp trạng thái–hành động.

Các tiên quyết gồm quá trình quyết định Markov (MDP), chính sách, kỳ vọng có điều kiện, giá trị trạng thái và lợi tức. Giả thiết Markov yêu cầu phân phối trạng thái kế tiếp và phần thưởng, khi đã biết trạng thái hiện tại và hành động, không còn phụ thuộc phần lịch sử trước đó. Bài học xét trạng thái được quan sát đầy đủ và động lực môi trường không đổi theo thời gian. Monte Carlo dự đoán dùng lợi tức của một lượt hoàn chỉnh; phương pháp sai phân thời gian (TD), với biến thể TD(0), dùng thưởng vừa nhận cùng một ước lượng giá trị tiếp nối.

Sau bài học, người học cần thực hiện được các công việc sau:

- Diễn giải giá trị hành động và phân biệt giá trị đúng với bảng ước lượng.
- Tính xác suất chọn hành động có thăm dò, kể cả khi nhiều hành động đồng hạng.
- Thực hiện MC lần ghé đầu, Sarsa và Q-learning trên dữ liệu đã cho.
- Giải thích vai trò của hành động kế tiếp, chính sách hành vi và trạng thái kết thúc.
- Kiểm tra các giả thiết về dữ liệu, bước học và thăm dò trước khi viện dẫn hội tụ.

### 1.3. Câu hỏi kiểm tra 1: thông tin trong một mẫu

::: exercise
Câu hỏi: Cho mẫu $(D,1,10,E)$. Xác định trạng thái đầu, hành động, phần thưởng và trạng thái kế tiếp. Mẫu này cung cấp dữ liệu quan sát nào về hành động trái tại D? Xác định số hành động còn thực hiện trong lượt.
:::

::: hint
Đọc bộ bốn theo thứ tự trạng thái, hành động, thưởng, trạng thái kế tiếp. Phân biệt một hành động đã được thực hiện với hành động chưa xuất hiện trong dữ liệu. Dùng quy ước kết thúc tại A và E.
:::

::: solution
Trạng thái đầu là D; hành động 1 đi phải; phần thưởng là 10; trạng thái kế tiếp là E. E kết thúc lượt, nên không còn hành động nào trong lượt.

Mẫu không chứa lần thực hiện hành động 0 tại D hoặc lợi tức sau hành động ấy. Thông tin mô hình của bài tập có thể được dùng cho một suy luận riêng, nhưng mẫu đi phải chưa phải một quan sát của hành động trái. Việc học để so sánh hai hành động cần giữ các ước lượng riêng cho hai cặp $(D,0)$ và $(D,1)$.
:::

Nguồn: Tạ Việt Cường, [Điều khiển phi mô hình](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf), tr. 3–7, 15–16; Sutton và Barto, [Reinforcement Learning: An Introduction, ấn bản 2](https://incompleteideas.net/book/the-book-2nd.html), §5.2 và §6.2.

<!-- note-topic-id: lec-06-topic-02 -->
## 2. Giá trị hành động và thăm dò

### 2.1. Hai ước lượng tại cùng trạng thái

Bảng $Q$ chứa một số thực cho mỗi cặp $(s,a)$ với $s\in\mathcal S$ và $a\in\mathcal A(s)$. Trong chuỗi A–E, bảng có sáu ô. Bảng khởi tạo I được dùng cho ví dụ MC tham lam và cho hai lần chạy riêng của Sarsa, Q-learning:

| Trạng thái | $Q_0(s,0)$: trái | $Q_0(s,1)$: phải |
|---|---:|---:|
| B | 0 | 1 |
| C | 1 | 0 |
| D | 0 | 1 |

Tại D, chọn hành động có giá trị lớn nhất trong bảng dẫn tới đi phải. Các số khởi tạo chưa phải quan sát và chưa xác định giá trị đúng. Nếu mọi lượt đều bắt đầu ở D rồi đi phải tới E, ô $(D,0)$ không nhận thêm dữ liệu. Trong biểu diễn bảng, cập nhật một cặp không trực tiếp thay đổi ước lượng của các cặp khác, dù các trạng thái có đặc điểm tương tự.

Xét riêng chính sách tiếp nối $\pi_L$, luôn chọn trái tại B, C và D. Nếu hành động đầu tại D là 0, phần tiếp nối theo $\pi_L$ tạo lượt D–C–B–A, với tổng phần thưởng $-1-1+1000=998$. Nếu hành động đầu tại D là 1, lượt kết thúc ngay tại E và nhận 10. Hai số này mô tả hai hành động đầu dưới cùng một chính sách tiếp nối; chúng khác các số khởi tạo trong bảng I.

### 2.2. Lợi tức và giá trị đúng

Trong một lượt, $S_t$ là trạng thái tại thời điểm $t$, $A_t$ là hành động được thực hiện và $R_{t+1}$ là phần thưởng nhận sau hành động ấy. $T$ là thời điểm kết thúc thật của lượt. Lợi tức từ thời điểm $t<T$ là

$$
G_t=\sum_{j=t}^{T-1}\gamma^{j-t}R_{j+1},\qquad G_T=0.
$$

Với $0\le\gamma\le1$, mỗi phần thưởng được nhân với hệ số chiết khấu theo số bước kể từ $t$. Khi dùng kỳ vọng ở $\gamma=1$, cần giả thiết lợi tức khả tích, tức $\mathbb E[|G_t|]<\infty$. Trong miền thưởng bị chặn và $0\le\gamma<1$, tổng chiết khấu bị chặn ngay cả khi quá trình tiếp tục vô hạn. Với bài toán tiếp tục, tổng được hiểu là chuỗi vô hạn; với bài toán kết thúc, có thể đặt các thưởng sau kết thúc bằng 0.

Chính sách $\pi(a\mid s)$ cho xác suất chọn hành động $a$ tại trạng thái $s$. Với một chính sách cố định theo thời gian, giá trị trạng thái và giá trị hành động lần lượt là

$$
v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],\qquad
q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

Trong $q_\pi(s,a)$, hành động đầu được cố định bằng $a$; các hành động sau được lấy theo $\pi$. Kỳ vọng bao gồm cả ngẫu nhiên của môi trường và của chính sách. Do đó

$$
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)q_\pi(s,a).
$$

$Q(s,a)$ là ước lượng được khởi tạo và cập nhật bằng dữ liệu. Ký hiệu chữ thường $q_\pi$ chỉ giá trị đúng của chính sách xác định. Trong miền bài toán có giá trị tối ưu hữu hạn, $q_*(s,a)=\sup_\pi q_\pi(s,a)$ là giá trị hành động tối ưu; các kết quả hội tụ tới $q_*$ ở phần sau được phát biểu trong miền hữu hạn có chiết khấu.

::: example
Với chính sách $\pi_L$, hai giá trị tại D là

$$
q_{\pi_L}(D,0)=998,\qquad q_{\pi_L}(D,1)=10.
$$

Sau hành động đầu cố định, chính sách $\pi_L$ dẫn tới kết thúc sau hữu hạn bước. Chính sách tham lam của bảng I lại đi từ B sang C và từ C về B. Vòng này nhận thưởng $-1$ ở mỗi bước. Với $\gamma=1$, lợi tức của vòng không khả tích và không cho một giá trị hữu hạn. Vì vậy không được gán 998 cho hành động trái tại D dưới chính sách tiếp nối tham lam của bảng I.
:::

![Chính sách tham lam từ bảng I tạo vòng B–C nhận thưởng âm; từ D đi phải tới E và kết thúc.](img/lec-06/greedy-chain.svg)

### 2.3. Đánh giá, cải thiện và thu thập dữ liệu

Đánh giá chính sách cập nhật ước lượng giá trị từ dữ liệu. Cải thiện chính sách thay đổi phân phối chọn hành động theo các ước lượng ấy. Chính sách mới tiếp tục sinh dữ liệu, nên cách chọn hành động quyết định các ô nào của bảng được cập nhật.

![Vòng điều khiển gồm dữ liệu tương tác, cập nhật bảng Q, xác định chính sách và tương tác tiếp với môi trường.](img/lec-06/control-loop.svg)

Thăm dò tạo cơ hội quan sát các hành động chưa được ưu tiên. Tại D của bảng I, dành xác suất $\varepsilon=1/4$ để chọn đều trong hai hành động; với xác suất $1-\varepsilon=3/4$, chọn hành động cực đại 1. Khi đó

$$
\Pr(A=0\mid D)=\frac14\frac12=\frac18,
\qquad
\Pr(A=1\mid D)=\frac34+\frac14\frac12=\frac78.
$$

Nhánh thăm dò chọn trong toàn bộ tập hành động, nên cũng có thể chọn hành động cực đại. Quy tắc xác suất này sử dụng các lần lấy mẫu ngẫu nhiên thích hợp; dãy số tất định ngắn trong một bài tính chỉ cung cấp dữ kiện để thực hiện thao tác.

### 2.4. Chính sách $\varepsilon$-tham lam

Đặt $m(s)=|\mathcal A(s)|$ và gọi tập hành động đạt cực đại của hàng $s$ là

$$
\mathcal G_Q(s)=\operatorname*{arg\,max}_{a\in\mathcal A(s)}Q(s,a).
$$

Quy ước chia đều phần khai thác giữa các hành động đồng hạng cho phân phối

$$
\pi_\varepsilon(a\mid s)
=\frac{\varepsilon}{m(s)}
+(1-\varepsilon)\frac{\mathbf 1\{a\in\mathcal G_Q(s)\}}{|\mathcal G_Q(s)|},
\qquad 0\le\varepsilon\le1.
$$

Ký hiệu $\mathbf1\{E\}$ bằng 1 khi mệnh đề $E$ đúng và bằng 0 khi sai. Thành phần chọn đều có tổng $\varepsilon$; thành phần khai thác có tổng $1-\varepsilon$. Mỗi xác suất không âm và tổng bằng 1. Nếu hai hành động đồng hạng, mỗi hành động có xác suất $1/2$ với mọi $\varepsilon$ theo quy ước này.

Một chính sách thuộc lớp $\varepsilon$-mềm nếu

$$
\pi(a\mid s)\ge\frac{\varepsilon}{m(s)}
\quad\forall s\in\mathcal S,\ a\in\mathcal A(s).
$$

Chính sách $\varepsilon$-tham lam ở trên thuộc lớp này. Một chính sách $\varepsilon$-mềm bất kỳ còn có thể phân bổ phần xác suất dư cho các hành động không cực đại. Với $\varepsilon>0$, điều kiện mềm cho mỗi hành động xác suất dương khi trạng thái đã được ghé; khả năng đạt tới trạng thái cần được xét riêng.

### 2.5. Cải thiện trong lớp chính sách mềm

Xét MDP hữu hạn, có động lực không đổi theo thời gian, có phần thưởng bị chặn và $0\le\gamma<1$. Cố định cùng $\varepsilon\in[0,1)$. Cho $\pi$ là chính sách $\varepsilon$-mềm và biết chính xác $q_\pi$. Nếu $\pi'$ là chính sách $\varepsilon$-tham lam theo $q_\pi$, thì

$$
v_{\pi'}(s)\ge v_\pi(s)\qquad\forall s\in\mathcal S.
$$

::: proof
Với mỗi trạng thái $s$, đặt

$$
w(a\mid s)=\frac{\pi(a\mid s)-\varepsilon/m(s)}{1-\varepsilon}.
$$

Do $\pi$ là $\varepsilon$-mềm, các trọng số $w(a\mid s)$ không âm. Tổng của chúng bằng $(1-\varepsilon)/(1-\varepsilon)=1$. Bởi trung bình có trọng số không vượt giá trị lớn nhất,

$$
\begin{aligned}
\sum_a\pi'(a\mid s)q_\pi(s,a)
&=\frac{\varepsilon}{m(s)}\sum_aq_\pi(s,a)
 +(1-\varepsilon)\max_aq_\pi(s,a)\\
&\ge\frac{\varepsilon}{m(s)}\sum_aq_\pi(s,a)
 +(1-\varepsilon)\sum_aw(a\mid s)q_\pi(s,a)\\
&=\sum_a\pi(a\mid s)q_\pi(s,a)=v_\pi(s).
\end{aligned}
$$

Để suy từ bất đẳng thức một bước sang giá trị toàn bộ phần tiếp nối, đặt $P(s'\mid s,a)$ là xác suất chuyển và $\bar r(s,a)=\mathbb E[R_{t+1}\mid S_t=s,A_t=a]$ là thưởng kỳ vọng. Với một hàm bị chặn $u$ trên trạng thái, quy ước $u=0$ tại trạng thái kết thúc và định nghĩa toán tử Bellman của $\pi'$:

$$
(T^{\pi'}u)(s)=\sum_a\pi'(a\mid s)
\left[\bar r(s,a)+\gamma\sum_{s'\in\mathcal S^+}P(s'\mid s,a)u(s')\right].
$$

Phương trình Bellman của $q_\pi$ cho $(T^{\pi'}v_\pi)(s)=\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$. Toán tử bảo toàn thứ tự vì các hệ số xác suất và $\gamma$ không âm. Đặt $u_0=v_\pi$ và $u_{j+1}=T^{\pi'}u_j$. Từ $u_1\ge u_0$, quy nạp cho $u_{j+1}\ge u_j\ge v_\pi$.

Với hai hàm bị chặn $u,z$ và chuẩn cực đại $\|u\|_\infty=\max_s|u(s)|$, tổng xác suất bằng 1 cho

$$
\|T^{\pi'}u-T^{\pi'}z\|_\infty\le\gamma\|u-z\|_\infty.
$$

Vì $\gamma<1$, các lần lặp hội tụ tới điểm bất động duy nhất $v_{\pi'}$. Lấy giới hạn trong $u_j\ge v_\pi$ suy ra $v_{\pi'}\ge v_\pi$.

Khi $\varepsilon=1$, mọi xác suất phải bằng $1/m(s)$ để vừa thỏa cận dưới vừa có tổng 1. Hai chính sách đều là chính sách đều, nên có đẳng thức. Trường hợp này được xử lý riêng, không chia cho $1-\varepsilon$.
:::

Mệnh đề sử dụng giá trị chính xác $q_\pi$. Một bảng $Q$ từ mẫu có thể xếp sai thứ tự hành động, nên mệnh đề chưa chứng minh mỗi cập nhật mẫu làm tăng giá trị thật. Khi giữ $\varepsilon>0$, việc cải thiện diễn ra trong lớp chính sách mềm tương ứng; giá trị tốt nhất trong lớp ấy có thể thấp hơn giá trị tối ưu trên toàn bộ chính sách.

### 2.6. Câu hỏi kiểm tra 2: xác suất và đối tượng ước lượng

::: exercise
Câu hỏi: Cho $Q(D,0)=0$, $Q(D,1)=1$ và $\varepsilon=1/4$.

1. Tính xác suất của mỗi hành động theo quy tắc $\varepsilon$-tham lam.
2. Tính lại khi hai ô đều bằng 1 và phần khai thác chia đều.
3. Diễn giải hành động đầu và chính sách tiếp nối trong $q_\pi(D,0)$.
4. Xác định bảng khởi tạo đã đủ căn cứ để áp dụng mệnh đề cải thiện chính sách hay chưa.
:::

::: hint
Tách xác suất của nhánh thăm dò và nhánh khai thác. Trong định nghĩa $q_\pi$, phân biệt hành động được điều kiện hóa với các hành động tiếp theo. Đối chiếu giả thiết giá trị chính xác và miền chiết khấu của mệnh đề.
:::

::: solution
Khi hành động 1 cực đại duy nhất, phân phối là $(1/8,7/8)$. Khi đồng hạng, mỗi hành động nhận $\varepsilon/2+(1-\varepsilon)/2=1/2$.

$q_\pi(D,0)$ cố định hành động đầu bằng 0 và dùng $\pi$ cho mọi hành động tiếp theo. Bảng khởi tạo chưa được xác nhận bằng $q_\pi$, nên chưa đủ để áp dụng mệnh đề cải thiện. Ngoài ra, mệnh đề đã nêu dùng $\gamma<1$, còn chuỗi minh họa dùng $\gamma=1$; áp dụng một kết quả không chiết khấu cần giả thiết riêng.
:::

Nguồn: Tạ Việt Cường, [bài giảng nguồn](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf), tr. 6–7, 11, 15–17, 24; Sutton và Barto, [giáo trình](https://incompleteideas.net/book/the-book-2nd.html), §§5.2–5.4, tr. 96–103. Quy ước chia đều giữa các cực đại được nêu tường minh để xử lý đồng hạng.

<!-- note-topic-id: lec-06-topic-03 -->
## 3. Điều khiển Monte Carlo

### 3.1. Giá trị hành động từ lượt hoàn chỉnh

Một lượt hoàn chỉnh cung cấp lợi tức sau mỗi cặp trạng thái–hành động đã xuất hiện. MC dùng các lợi tức ấy để cập nhật $Q$, rồi xác định chính sách cho lượt tiếp theo. Chính sách sinh hành động được giữ cố định trong từng lượt, nên lợi tức sau hành động đầu đánh giá chính phần tiếp nối theo chính sách đã sinh dữ liệu. Đây là điều khiển theo chính sách.

Với bảng I, chọn tham lam tại D tạo lượt D–E, có lợi tức 10. Đặt $N(D,1)=0$ trước khi nhận mẫu, trong đó $N(s,a)$ đếm số lợi tức thực sự dùng cho cặp $(s,a)$. Sau mẫu đầu, $N(D,1)=1$ và

$$
Q(D,1)=1+\frac{10-1}{1}=10.
$$

Các ô khác giữ nguyên. Giá trị khởi tạo 1 không phải một mẫu quan sát; lấy trung bình $(1+10)/2$ sẽ thêm một quan sát không có trong dữ liệu.

### 3.2. Lần ghé đầu theo cặp và trung bình mẫu

Lần ghé đầu của $(s,a)$ là thời điểm nhỏ nhất $t$ trong lượt thỏa $(S_t,A_t)=(s,a)$. Hai lần ghé cùng một trạng thái nhưng chọn hai hành động khác nhau thuộc hai cặp khác nhau. Với MC lần ghé đầu, mỗi cặp đóng góp nhiều nhất một lợi tức trong một lượt.

Lợi tức được tính lùi từ thời điểm kết thúc:

$$
G_T=0,\qquad G_t=R_{t+1}+\gamma G_{t+1},\quad t=T-1,\ldots,0.
$$

Nếu $t$ là lần ghé đầu của $(s,a)$, cập nhật

$$
\begin{aligned}
N(s,a)&\leftarrow N(s,a)+1,\\
Q(s,a)&\leftarrow Q(s,a)+\frac{G_t-Q(s,a)}{N(s,a)}.
\end{aligned}
$$

Bộ đếm tăng trước phép chia. Việc tính lợi tức theo thứ tự ngược không đổi nghĩa của lần ghé đầu: chỉ số nhỏ nhất theo thời gian vẫn quyết định mẫu được dùng.

::: derivation
Gọi $g_1,\ldots,g_n$ là các lợi tức đã chọn cho một cặp qua những lượt có cặp ấy. Với $N_0=0$, cập nhật đầu tiên cho $Q^{(1)}=g_1$. Giả sử sau $n-1$ mẫu, $Q^{(n-1)}=(g_1+\cdots+g_{n-1})/(n-1)$. Khi nhận mẫu thứ $n$,

$$
Q^{(n)}=Q^{(n-1)}+\frac{g_n-Q^{(n-1)}}n
=\frac{(n-1)Q^{(n-1)}+g_n}n
=\frac1n\sum_{i=1}^ng_i.
$$

Ở đây chỉ số trong ngoặc đếm số lợi tức của cặp đang xét. Nó không phải số lượt toàn cục. Đẳng thức chứng minh dạng trung bình số học của cập nhật; bảo đảm thống kê còn phụ thuộc quá trình sinh các lợi tức.
:::

### 3.3. Lấy mẫu từ dãy số của bài tập

Ví dụ tiếp theo dùng bảng II riêng, giữ hai hàng B, C của bảng I và đổi hàng D:

| Trạng thái | $Q_0(s,0)$ | $Q_0(s,1)$ |
|---|---:|---:|
| B | 0 | 1 |
| C | 1 | 0 |
| D | 1 | 0 |

Cho $\varepsilon=1/4$, $x_0=1$ và

$$
x_j=(2x_{j-1}+1)\bmod5,\qquad u_j=\frac{x_j+1}{5},\quad j=1,2,\ldots.
$$

Chỉ số $j$ đếm số đã tiêu thụ, khác thời điểm tương tác $t$. Với mỗi lần chọn hành động, đọc một số $u$. Nếu $u>1/4$, chọn hành động cực đại. Nếu $u\le1/4$, đọc thêm một số: chọn trái khi số bổ sung không vượt $1/2$, chọn phải trong trường hợp còn lại. Các hàng được dùng ở đây có cực đại duy nhất.

| Trạng thái | Số quyết định nhánh | Số bổ sung | Hành động |
|---|---:|---:|---|
| D | $u_1=4/5$ | Không dùng | 0, cực đại |
| C | $u_2=3/5$ | Không dùng | 0, cực đại |
| B | $u_3=1/5$ | $u_4=2/5$ | 0, thăm dò |

Dãy trạng thái bộ sinh là $x_1=3,x_2=2,x_3=0,x_4=1$. Quy tắc tiêu thụ số cho lượt D–C–B–A. Dãy tất định này có chu kỳ, không tạo các mẫu đều độc lập và không chứng minh độ phủ dài hạn của thuật toán.

### 3.4. Quy trình MC qua nhiều lượt

Đầu vào gồm môi trường lấy mẫu, tập hành động hợp lệ, phân phối trạng thái đầu $d_0$ trên $\mathcal S$, hệ số $\gamma$, bảng hữu hạn $Q_0$, lịch $0<\varepsilon_k\le1$ và ngân sách $K$ lượt hoàn chỉnh, với $K$ là số nguyên dương. Các chính sách được dùng phải sinh lượt kết thúc gần chắc chắn và có lợi tức khả tích. Đầu ra là bảng $Q$ cùng chính sách mềm hiện hành từ bảng ấy.

1. Khởi tạo một lần $Q\leftarrow Q_0$ và $N(s,a)\leftarrow0$ cho mọi cặp hợp lệ.
2. Với mỗi lượt $k=1,\ldots,K$, đặt lại quỹ đạo và ánh xạ chỉ số ghé đầu $f$; giữ nguyên $Q,N$ đã tích lũy. Ký hiệu $Q^{[k]}$ là bảng trước lượt. Cố định $\pi_k$ bằng chính sách $\varepsilon_k$-tham lam theo $Q^{[k]}$, rồi lấy $S_0\sim d_0$.
3. Tại thời điểm $t$ của lượt, lấy $A_t\sim\pi_k(\cdot\mid S_t)$, thực hiện hành động và nhận $R_{t+1},S_{t+1}$. Lưu chuyển tiếp. Nếu cặp $(S_t,A_t)$ chưa có trong $f$, đặt $f(S_t,A_t)=t$. Lặp tới trạng thái kết thúc; gọi thời điểm đó là $T$. Bảng và chính sách không đổi trong lúc thu thập.
4. Đặt $G_T=0$ và tính $G_t$ theo truy hồi lùi. Với mỗi cặp xuất hiện trong lượt, dùng duy nhất lợi tức $G_{f(s,a)}$, tăng $N(s,a)$ rồi áp dụng cập nhật trung bình mẫu.
5. Tạo chính sách $\varepsilon_k$-tham lam theo bảng mới. Nếu còn lượt, bước 2 dùng $\varepsilon_{k+1}$ cùng bảng giữ lại; nếu $k=K$, trả bảng và chính sách vừa tạo.

Cải thiện sau lượt không thay đổi chính sách đã sinh lượt vừa hoàn tất. Một tiền tố bị cắt tại trạng thái chưa kết thúc không đủ cho quy trình MC dùng lợi tức hoàn chỉnh này.

Đặt $M=\sum_{s\in\mathcal S}m(s)$ là số cặp hợp lệ. Lưu $Q,N$, quỹ đạo và $f$ cần bộ nhớ $O(M+T)$ cho lượt hiện tại. Với phép tra cứu chỉ số ghé đầu trong thời gian hằng, tính lợi tức và chọn mẫu cần $O(T)$; chi phí tìm cực đại để chọn hoặc cập nhật chính sách được cộng riêng. Ngân sách $K$ xác định điểm dừng thực hành, không phải chứng nhận hội tụ.

### 3.5. Cập nhật từ lượt D–C–B–A

![Lượt D–C–B–A gồm ba hành động trái, nhận thưởng âm một, âm một và một nghìn; lợi tức lần lượt là 998, 999 và 1000.](img/lec-06/episode-return.svg)

Với $\gamma=1$, tính từ cuối lượt cho $G_2=1000$, $G_1=999$ và $G_0=998$. Mỗi cặp xuất hiện một lần. Khởi tạo $N_0=0$ cho bảng II, kết quả sau lượt là

| Trạng thái | $Q(s,0)$ | $Q(s,1)$ | $N(s,0)$ | $N(s,1)$ |
|---|---:|---:|---:|---:|
| B | 1000 | 1 | 1 | 0 |
| C | 999 | 0 | 1 | 0 |
| D | 998 | 0 | 1 | 0 |

Chính sách mềm từ bảng mới ưu tiên trái tại D. Kết quả này là một cập nhật từ dữ liệu; nó chưa chứng nhận giá trị chính sách tăng sau từng mẫu. Các lợi tức ở những lượt khác nhau có thể được sinh bởi những chính sách khác nhau.

### 3.6. Câu hỏi kiểm tra 3: lần ghé đầu và mọi lần ghé

::: exercise
Câu hỏi: Cho lượt D–C–D–C–B–A với dãy hành động $0,1,0,0,0$, dãy thưởng $-1,-1,-1,-1,1000$ và $\gamma=1$. Với $N_0(D,0)=0$, tính $Q(D,0)$ và $N(D,0)$ sau MC lần ghé đầu. Tính lại nếu dùng mọi lần ghé với trung bình mẫu.
:::

::: hint
Đánh số thời điểm từ 0. Tính lợi tức lùi, sau đó chọn các thời điểm có đúng cặp $(D,0)$. Lần ghé đầu được xác định theo chiều thời gian, dù lợi tức được tính theo chiều ngược.
:::

::: solution
Các lợi tức theo thứ tự thời gian là $996,997,998,999,1000$. Cặp $(D,0)$ xuất hiện tại $t=0$ và $t=2$, với lợi tức tương ứng 996 và 998.

MC lần ghé đầu dùng mẫu 996, nên $Q(D,0)=996$ và $N(D,0)=1$. MC mọi lần ghé dùng cả hai mẫu, nên $Q(D,0)=(996+998)/2=997$ và $N(D,0)=2$. Giá trị khởi tạo không tính thành mẫu. Tại C, hai lần ghé dùng hai hành động khác nhau; $(C,1)$ và $(C,0)$ được xử lý thành hai cặp riêng.
:::

Nguồn: Tạ Việt Cường, [bài giảng nguồn](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf), tr. 10–11, 15–17; Sutton và Barto, [giáo trình](https://incompleteideas.net/book/the-book-2nd.html), tr. 93, 99–103. Quy ước tiêu thụ số được làm rõ để xác định duy nhất lượt của bài tập; thuật toán chính dùng lần ghé đầu theo cặp.

<!-- note-topic-id: lec-06-topic-04 -->
## 4. Sarsa: cập nhật theo hành động kế tiếp

### 4.1. Mục tiêu một bước khi lượt chưa kết thúc

Sau chuyển D–C, phần thưởng $-1$ đã được quan sát nhưng phần cuối lượt chưa có. MC còn thiếu lợi tức hoàn chỉnh. Sarsa thay phần tiếp nối chưa quan sát bằng giá trị ước lượng của hành động đã chọn tại C. Một cập nhật vì thế có thể thực hiện trước khi biết toàn bộ kết quả của lượt.

Các phép tính Sarsa và Q-learning dưới đây dùng $\gamma=1$, bước học $\alpha=0.8=4/5$ và hai bản sao riêng của bảng I:

| Trạng thái | $Q_0(s,0)$ | $Q_0(s,1)$ |
|---|---:|---:|
| B | 0 | 1 |
| C | 1 | 0 |
| D | 0 | 1 |

Năm mẫu được cho trước như sau. Ký hiệu $S,A,R,S',A'$ rút gọn cho trạng thái hiện tại, hành động, thưởng vừa nhận, trạng thái kế tiếp và hành động kế tiếp.

| Mẫu | $S$ | $A$ | $R$ | $S'$ | $A'$ của Sarsa |
|---:|---|---:|---:|---|---|
| 1 | D | 0 | $-1$ | C | 0 |
| 2 | C | 0 | $-1$ | B | 0 |
| 3 | B | 0 | 1000 | A | Không có |
| 4 | D | 1 | 10 | E | Không có |
| 5 | D | 0 | $-1$ | C | 0 |

Ba mẫu đầu thuộc lượt D–C–B–A. Mẫu 4 thuộc lượt mới D–E. Mẫu 5 thuộc một lượt mới nữa, có dữ liệu hiện tại dừng ở C. Sau A và E, trạng thái đầu được đặt lại về D; bảng giá trị được giữ. C ở mẫu 5 vẫn chưa kết thúc.

Các hành động này là dữ kiện để tính, không phải quỹ đạo duy nhất suy ra từ $\varepsilon=1/4$ hay từ dãy số trong phần MC. Chúng đều có xác suất dương dưới một hành vi $\varepsilon$-tham lam với $\varepsilon>0$. Đối chiếu hai thuật toán trên cùng các mẫu là đối chiếu có điều kiện trên dữ liệu; hai quá trình học không vì thế có cùng phân phối quỹ đạo.

### 4.2. Hai bước tính đầu tiên

Ở mẫu 1, Sarsa nhận thưởng $-1$ rồi dùng giá trị $Q(C,0)=1$ của hành động kế tiếp đã chọn. Mục tiêu là $-1+1=0$, bằng giá trị cũ $Q(D,0)=0$, nên ô này giữ nguyên.

Ở mẫu 2, hành động kế tiếp tại B là 0, có giá trị $Q(B,0)=0$. Mục tiêu bằng $-1+0=-1$. So với ước lượng hiện tại $Q(C,0)=1$, sai lệch bằng $-2$, cho

$$
Q(C,0)\leftarrow1+0.8(-1-1)=-0.6.
$$

![Mục tiêu Sarsa cho chuyển từ cặp C, trái tới B dùng hành động trái đã chọn tại B, có giá trị bằng 0; mục tiêu bằng âm một.](img/lec-06/sarsa-target.svg)

Giá trị $Q(B,1)=1$ không tham gia mục tiêu này vì hành động 1 chưa được chọn để tiếp tục lượt. Mọi giá trị phía bên phải được đọc trước khi đổi ô $(C,0)$.

### 4.3. Quy tắc cập nhật

Ký hiệu $Q_t$ là bảng ngay trước cập nhật tại bước tương tác $t$. Nếu trạng thái kế tiếp chưa kết thúc, chọn $A_{t+1}$ theo chính sách từ $Q_t$ và đặt

$$
Y_t=
\begin{cases}
R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1}), & S_{t+1}\in\mathcal S,\\
R_{t+1}, & S_{t+1}\text{ kết thúc}.
\end{cases}
$$

Với bước học $\alpha_t\in(0,1]$, cập nhật

$$
\begin{aligned}
\delta_t&=Y_t-Q_t(S_t,A_t),\\
Q_{t+1}(S_t,A_t)&=Q_t(S_t,A_t)+\alpha_t\delta_t.
\end{aligned}
$$

Các ô khác giữ nguyên. $Y_t$ là mục tiêu cập nhật; $\delta_t$ là sai lệch giữa mục tiêu ấy với ước lượng hiện hành, chưa phải sai số thật so với $q_\pi$ hoặc $q_*$. Tên Sarsa gắn với bộ năm $(S_t,A_t,R_{t+1},S_{t+1},A_{t+1})$.

Chính sách chọn hành động trong tương tác cũng chọn hành động của phần tiếp nối trong mục tiêu, nên Sarsa là phương pháp theo chính sách. $A_{t+1}$ được lấy trước cập nhật; nếu tiếp tục tương tác, phải thực hiện chính hành động đã lấy. Chọn lại từ bảng mới có thể làm hành động được thực hiện khác với hành động đã dùng trong mục tiêu.

Tại trạng thái kết thúc, không lấy $A_{t+1}$. Mục tiêu chỉ bằng phần thưởng vừa nhận. Phần thưởng khi vào A hoặc E không được cộng lần nữa như một giá trị tiếp nối.

### 4.4. Quy trình Sarsa với ngân sách cập nhật

Đầu vào gồm môi trường lấy mẫu, tập hành động, phân phối đầu $d_0$ trên $\mathcal S$, $\gamma$, bảng hữu hạn $Q_0$, lịch thăm dò, lịch bước học và ngân sách $H$ cập nhật, với $H$ là số nguyên dương. Đầu ra là bảng $Q$ cùng chính sách $\varepsilon$-tham lam hiện hành. Ký hiệu $h$ đếm số cập nhật đã thực hiện trên toàn bộ các lượt; $n(s,a)$ đếm riêng số cập nhật đã hoàn thành của cặp $(s,a)$.

1. Đặt $Q\leftarrow Q_0$, $h\leftarrow0$ và $n(s,a)\leftarrow0$. Lấy trạng thái đầu $S\sim d_0$ và hành động $A$ theo chính sách mềm từ bảng hiện tại.
2. Trước khi thực hiện $A$, chọn bước học $\alpha_{n(S,A)+1}(S,A)$ từ thông tin đã có. Chỉ số $n(S,A)+1$ là số thứ tự của cập nhật sắp thực hiện. Thực hiện $A$ và nhận $R,S'$.
3. Nếu $S'$ chưa kết thúc, lấy một lần $A'$ theo chính sách từ bảng $Q$ chưa cập nhật, rồi tính $Y=R+\gamma Q(S',A')$. Nếu $S'$ kết thúc, đặt $Y=R$ và không chọn $A'$.
4. Đọc giá trị cũ của ô $(S,A)$ và cập nhật $Q(S,A)\leftarrow Q(S,A)+\alpha_{n(S,A)+1}(S,A)[Y-Q(S,A)]$. Tăng $n(S,A)$ và $h$ lên 1.
5. Nếu $h=H$, trả bảng và chính sách hiện hành. Nếu còn ngân sách và $S'$ chưa kết thúc, đặt $(S,A)\leftarrow(S',A')$ rồi về bước 2. Nếu còn ngân sách và $S'$ kết thúc, lấy trạng thái đầu mới cùng hành động đầu theo bảng hiện tại, rồi về bước 2; giữ $Q$ và các bộ đếm.

Ở cập nhật cuối, nếu $S'$ chưa kết thúc thì vẫn cần lấy $A'$ để tạo mục tiêu. Ngân sách có thể dừng trước khi hành động ấy được thực hiện, nhưng không xóa giá trị tiếp nối. Kết thúc lượt là sự kiện của môi trường; hết ngân sách là điểm dừng của thuật toán.

Bộ nhớ bảng và các bộ đếm là $O(M)$. Khi đã có $A'$, việc tạo mục tiêu chỉ cần một lần tra cứu giá trị. Chọn hành động $\varepsilon$-tham lam bằng cách duyệt hàng có thể tốn $O(m(S'))$. Sarsa không cần lưu cả lượt để cập nhật.

### 4.5. Bảng Sarsa sau từng mẫu

Mỗi hàng dưới đây dùng bảng sau các mẫu trước đó trong chính lần chạy Sarsa:

| Mẫu | Ô cập nhật | Giá trị cũ | $Y$ | $\delta$ | Giá trị mới |
|---:|---|---:|---:|---:|---:|
| 1 | $(D,0)$ | 0 | 0 | 0 | 0 |
| 2 | $(C,0)$ | 1 | $-1$ | $-2$ | $-0.6$ |
| 3 | $(B,0)$ | 0 | 1000 | 1000 | 800 |
| 4 | $(D,1)$ | 1 | 10 | 9 | 8.2 |
| 5 | $(D,0)$ | 0 | $-1.6$ | $-1.6$ | $-1.28$ |

Mẫu 3 chuyển vào A, cho $0+0.8(1000-0)=800$. Mẫu 4 chuyển vào E, cho $1+0.8(10-1)=8.2$. Mẫu 5 dùng giá trị đã cập nhật $Q(C,0)=-0.6$, nên mục tiêu bằng $-1-0.6=-1.6$.

Mỗi ô của ba cột trạng thái trong bảng sau ghi cặp giá trị theo thứ tự hành động $(0,1)$:

| Sau mẫu | Hàng B | Hàng C | Hàng D |
|---:|---|---|---|
| 0: khởi tạo | $(0,1)$ | $(1,0)$ | $(0,1)$ |
| 1 | $(0,1)$ | $(1,0)$ | $(0,1)$ |
| 2 | $(0,1)$ | $(-0.6,0)$ | $(0,1)$ |
| 3 | $(800,1)$ | $(-0.6,0)$ | $(0,1)$ |
| 4 | $(800,1)$ | $(-0.6,0)$ | $(0,8.2)$ |
| 5 | $(800,1)$ | $(-0.6,0)$ | $(-1.28,8.2)$ |

Các số thập phân đều chính xác: $-0.6=-3/5$, $8.2=41/5$, $-1.28=-32/25$. Bảng cuối ưu tiên phải tại D. Năm mẫu chỉ xác định bảng hiện tại; chúng chưa chứng nhận chính sách tối ưu.

### 4.6. Câu hỏi kiểm tra 4: cập nhật từ tiền tố

::: exercise
Câu hỏi: Sau bốn mẫu, cho $Q(D,0)=0$, $Q(C,0)=-0.6$ và mẫu thứ năm $(D,0,-1,C,0)$, với $\gamma=1$, $\alpha=0.8$.

1. Tính $Y$, $\delta$ và giá trị mới của $Q(D,0)$.
2. Xác định thời điểm lấy $A'$ và hành động phải dùng nếu tiếp tục tương tác.
3. Giải thích ảnh hưởng của việc hết ngân sách tới phần giá trị tiếp nối tại C.
:::

::: hint
Dùng giá trị tại C sau bốn mẫu, không dùng lại bảng khởi tạo. Phân biệt trạng thái chưa kết thúc với điểm dừng thu thập dữ liệu.
:::

::: solution
Mục tiêu $Y=-1+(-0.6)=-1.6$; sai lệch $\delta=-1.6-0=-1.6$; do đó cập nhật $Q(D,0)\leftarrow0+0.8(-1.6)=-1.28$.

$A'=0$ được chọn trước cập nhật. Nếu tiếp tục tương tác, thực hiện chính hành động đó. Nếu ngân sách kết thúc sau cập nhật, không cần thực hiện $A'$. Trong cả hai trường hợp, C vẫn là trạng thái không kết thúc và mục tiêu vẫn chứa $Q(C,0)$. MC dùng lợi tức hoàn chỉnh chưa thể cập nhật từ riêng tiền tố D–C này.
:::

Nguồn: Tạ Việt Cường, [bài giảng nguồn](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf), tr. 12–15, 18; Sutton và Barto, [giáo trình](https://incompleteideas.net/book/the-book-2nd.html), §6.4, tr. 129–130. Năm mẫu và ranh giới lượt được công bố đầy đủ để bài tính có đầu vào xác định.

<!-- note-topic-id: lec-06-topic-05 -->
## 5. Q-learning: tách hành vi và mục tiêu

### 5.1. Hai vai của chính sách

Ở mẫu 2, Sarsa dùng hành động trái tại B vì đó là hành động đã chọn để tiếp tục. Hành vi thăm dò có thể chọn một hành động chưa đạt cực đại của bảng. Nếu mục tiêu học dùng giá trị cực đại tại trạng thái kế tiếp, hành động tạo dữ liệu và hành động dùng để xác định đích có thể khác nhau.

Chính sách hành vi $b$ chọn các hành động tương tác với môi trường. Chính sách đích $\pi$ mô tả cách lựa chọn được đánh giá hoặc cải thiện. Trong Q-learning một bước, hành vi sinh mẫu, còn đích là lựa chọn tham lam từ bảng hiện hành. Vì hai vai được tách, Q-learning là phương pháp khác chính sách.

![Chính sách hành vi chọn hành động và sinh mẫu môi trường; bảng Q dùng mẫu chuyển cùng cực đại tại trạng thái kế tiếp để tạo mục tiêu cập nhật.](img/lec-06/behavior-target.svg)

### 5.2. Mục tiêu cực đại trên cùng dữ liệu

Đặt lại bảng I cho một lần chạy Q-learning riêng. Mẫu 1 vẫn có mục tiêu $-1+\max(1,0)=0$, nên $Q(D,0)$ giữ nguyên. Trước mẫu 2, hàng B vẫn bằng $(0,1)$. Q-learning dùng giá trị lớn nhất bằng 1, cho

$$
Y=-1+\max(0,1)=0,\qquad
Q(C,0)\leftarrow1+0.8(0-1)=0.2.
$$

![Mục tiêu Q-learning cho cùng chuyển từ C tới B dùng giá trị cực đại 1 trong hàng B; mục tiêu bằng 0 dù hành động tiếp theo trong dữ liệu là trái.](img/lec-06/q-learning-target.svg)

Sarsa cho $-0.6$ tại cùng ô vì dùng giá trị của hành động 0 đã chọn. Q-learning cho $0.2$ vì dùng cực đại của hàng B. Giá trị cực đại này thuộc bảng ước lượng, chưa phải giá trị tốt nhất thật của trạng thái B.

### 5.3. Quy tắc Q-learning

Với $Q_t$ là bảng trước cập nhật, đặt

$$
Y_t=
\begin{cases}
R_{t+1}+\gamma\displaystyle\max_{a\in\mathcal A(S_{t+1})}Q_t(S_{t+1},a),
& S_{t+1}\in\mathcal S,\\
R_{t+1}, & S_{t+1}\text{ kết thúc}.
\end{cases}
$$

Sau đó dùng

$$
Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)
+\alpha_t\left[Y_t-Q_t(S_t,A_t)\right].
$$

Các ô khác giữ nguyên. Bộ bốn $(S_t,A_t,R_{t+1},S_{t+1})$ đủ để tạo mục tiêu; không cần hành động kế tiếp đã lấy mẫu. Toàn bộ phép cực đại và giá trị cũ trong vế phải đều dùng cùng bảng $Q_t$.

Q-learning tính trực tiếp cực đại trên các hành động hợp lệ. Nó không dùng một hành động kế tiếp lấy từ $b$ để ước lượng kỳ vọng dưới chính sách đích, nên cập nhật một bước này không cần tỉ số lấy mẫu quan trọng. Điều kiện dữ liệu đúng môi trường và có độ phủ vẫn cần được kiểm tra.

### 5.4. Quy trình Q-learning

Đầu vào gồm môi trường lấy mẫu, tập hành động, phân phối đầu $d_0$ trên $\mathcal S$, $\gamma$, bảng hữu hạn $Q_0$, quy tắc hành vi $b$, lịch bước học và ngân sách $H$ cập nhật. $b$ có thể được xây dựng bằng quy tắc $\varepsilon$-tham lam từ bảng hiện hành. Đầu ra gồm bảng $Q$ và chính sách tham lam rút từ bảng. Nếu còn tương tác, hành vi có thể tiếp tục thăm dò.

1. Đặt $Q\leftarrow Q_0$, $h\leftarrow0$, $n(s,a)\leftarrow0$ và lấy $S\sim d_0$.
2. Chọn $A$ theo $b$ ở trạng thái $S$. Chọn bước học $\alpha_{n(S,A)+1}(S,A)$ từ thông tin hiện có trước mẫu. Thực hiện hành động, nhận $R,S'$.
3. Nếu $S'$ chưa kết thúc, tính $Y=R+\gamma\max_{a\in\mathcal A(S')}Q(S',a)$ từ bảng chưa cập nhật. Nếu $S'$ kết thúc, đặt $Y=R$.
4. Cập nhật ô $(S,A)$ theo quy tắc Q-learning, rồi tăng $n(S,A)$ và $h$ lên 1.
5. Nếu $h=H$, trả bảng và chính sách tham lam hiện hành. Nếu còn ngân sách, đặt $S\leftarrow S'$ khi chưa kết thúc hoặc lấy trạng thái đầu mới khi đã kết thúc; giữ bảng và bộ đếm, rồi về bước 2.

Hành động thực hiện sau cập nhật vẫn do $b$ chọn. Việc dừng ở một trạng thái chưa kết thúc không xóa số hạng cực đại trong mục tiêu cuối. Bộ nhớ là $O(M)$; tìm trực tiếp cực đại tại $S'$ cần $O(m(S'))$, ngoài chi phí chọn hành vi. Không cần lưu cả lượt.

### 5.5. Bảng Q-learning sau từng mẫu

Lần chạy này bắt đầu lại từ bảng I và dùng đúng năm mẫu đã công bố ở phần Sarsa. Giá trị mới từ một mẫu chỉ được chuyển sang các mẫu sau trong chính bảng Q-learning.

| Mẫu | Ô cập nhật | Giá trị cũ | $Y$ | $\delta$ | Giá trị mới |
|---:|---|---:|---:|---:|---:|
| 1 | $(D,0)$ | 0 | 0 | 0 | 0 |
| 2 | $(C,0)$ | 1 | 0 | $-1$ | 0.2 |
| 3 | $(B,0)$ | 0 | 1000 | 1000 | 800 |
| 4 | $(D,1)$ | 1 | 10 | 9 | 8.2 |
| 5 | $(D,0)$ | 0 | $-0.8$ | $-0.8$ | $-0.64$ |

Trước mẫu 5, hàng C bằng $(0.2,0)$. Do đó

$$
Y=-1+\max(0.2,0)=-0.8,
\qquad Q(D,0)\leftarrow0+0.8(-0.8)=-0.64.
$$

Bảng đầy đủ sau mỗi mẫu, với các cặp giá trị ghi theo thứ tự hành động $(0,1)$, là

| Sau mẫu | Hàng B | Hàng C | Hàng D |
|---:|---|---|---|
| 0: khởi tạo | $(0,1)$ | $(1,0)$ | $(0,1)$ |
| 1 | $(0,1)$ | $(1,0)$ | $(0,1)$ |
| 2 | $(0,1)$ | $(0.2,0)$ | $(0,1)$ |
| 3 | $(800,1)$ | $(0.2,0)$ | $(0,1)$ |
| 4 | $(800,1)$ | $(0.2,0)$ | $(0,8.2)$ |
| 5 | $(800,1)$ | $(0.2,0)$ | $(-0.64,8.2)$ |

Các số $0.2=1/5$ và $-0.64=-16/25$ là chính xác. Khác biệt với Sarsa xuất hiện ở mục tiêu dùng hàng B cho mẫu 2, rồi truyền từ giá trị tại C về D ở mẫu 5. Hai mẫu chuyển vào A và E có cùng mục tiêu trong cả hai thuật toán.

### 5.6. Điều kiện sử dụng dữ liệu hành vi

Mẫu chuyển và thưởng phải phản ánh động lực của MDP theo cặp được cập nhật. Dữ liệu từ một hành vi khác có thể phục vụ Q-learning trong cùng môi trường; dữ liệu từ một động lực khác cần được phân tích riêng. Phát lại vô hạn một tập mẫu hữu hạn không tự khôi phục đúng phân phối chuyển của môi trường và không tự thỏa giả thiết lấy mẫu của định lý hội tụ.

Trong đánh giá khác chính sách nói chung, điều kiện hỗ trợ hành động yêu cầu $\pi(a\mid s)>0$ kéo theo $b(a\mid s)>0$. Điều kiện này đảm bảo một hành động đích có thể được lấy mẫu khi đã ở $s$. Để học toàn bảng còn cần đạt tới và cập nhật các cặp cần học đủ lâu. Nhãn khác chính sách tự nó chưa xác định một ưu thế hiệu quả mẫu trên mọi bài toán.

### 5.7. Câu hỏi kiểm tra 5: so sánh hai mục tiêu

::: exercise
Câu hỏi: Cho cùng một bảng có $Q(B,0)=800$, $Q(B,1)=1$, chuyển $(C,0,-1,B)$ và $\gamma=1$. Sarsa đã chọn $A'=1$.

1. Tính mục tiêu Sarsa và mục tiêu Q-learning.
2. Nêu điều kiện để hai mục tiêu trùng nhau tại một trạng thái chưa kết thúc, khi dùng cùng bảng, cùng thưởng và $\gamma=1$.
:::

::: hint
Sarsa phải dùng hành động $A'=1$ đã cho. Q-learning dùng cực đại của hàng B. So sánh hai số hạng tiếp nối mà không đổi hành động trong dữ liệu.
:::

::: solution
Mục tiêu Sarsa là $-1+Q(B,1)=0$. Mục tiêu Q-learning là $-1+\max(800,1)=799$.

Với trạng thái kế tiếp chưa kết thúc và $\gamma=1$, hai mục tiêu bằng nhau khi

$$
Q(S',A')=\max_{a\in\mathcal A(S')}Q(S',a),
$$

tức $A'\in\mathcal G_Q(S')$. Không cần cực đại duy nhất. Khi chuyển vào trạng thái kết thúc, cả hai dùng mục tiêu bằng thưởng và thuộc nhánh riêng. Trùng mục tiêu ở một bước chưa suy ra hai quá trình có cùng quỹ đạo hoặc cùng chính sách hành vi trong giới hạn.
:::

Nguồn: Tạ Việt Cường, [bài giảng nguồn](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf), tr. 8, 19–21, 28; Sutton và Barto, [giáo trình](https://incompleteideas.net/book/the-book-2nd.html), tr. 103–105 và §6.5, tr. 131. Khởi tạo Q-learning dùng bảng I để đối chiếu mục tiêu trên cùng dữ kiện với Sarsa.

<!-- note-topic-id: lec-06-topic-06 -->
## 6. Điều kiện bảo đảm hội tụ

### 6.1. Miền của kết quả lý thuyết

Các bảng sau năm mẫu kiểm tra được cơ chế cập nhật. Hội tụ tới giá trị tối ưu là kết luận về một quá trình học dài hạn và cần giả thiết bổ sung. Kết quả ở đây xét MDP hữu hạn, có động lực không đổi theo thời gian, phần thưởng bị chặn, $0\le\gamma<1$, biểu diễn dạng bảng và $Q_0$ hữu hạn.

Mẫu trạng thái kế tiếp và phần thưởng, có điều kiện theo lịch sử đã quan sát cùng cặp hiện tại, phải tuân theo động lực của MDP. Mọi cặp không kết thúc cần học được cập nhật vô hạn lần gần chắc chắn. Các bước học được chọn từ thông tin có trước mẫu dùng cho cập nhật và thỏa điều kiện theo từng cặp ở mục 6.3.

Ví dụ chuỗi A–E dùng $\gamma=1$ và bước học $0.8$ để tính tay, nên không thuộc phát biểu có chiết khấu này. Sự tồn tại của A và E chưa đảm bảo mọi chính sách đều kết thúc; vòng B–C đã cho một trường hợp ngược lại. Các kết quả không chiết khấu cần giả thiết hấp thụ và kiểm soát lợi tức riêng. Hết ngân sách chỉ trả một bảng hiện hành.

### 6.2. Tham lam trong giới hạn với thăm dò vô hạn

Với hai hành động và một cực đại duy nhất, $\varepsilon=1/4$ giữ xác suất chọn cực đại bằng $7/8$. Cho $\varepsilon$ giảm về 0 làm xác suất ấy tiến về 1. Tuy nhiên, hành động ít được chọn và các trạng thái cần qua nhiều bước thăm dò vẫn phải nhận đủ dữ liệu.

Điều kiện **tham lam trong giới hạn với thăm dò vô hạn (GLIE)** bao gồm hai yêu cầu. Dùng $t$ làm chỉ số tương tác toàn bộ quá trình; $C_t(s,a)$ đếm số lần thăm cặp đến bước $t$. Với $Q_t$ là bảng trước cập nhật, đặt

$$
\mathcal G_t(s)=\operatorname*{arg\,max}_{a\in\mathcal A(s)}Q_t(s,a).
$$

Gọi $\pi_t$ là quy tắc chọn hành động theo chính bảng hiện hành ấy. Trong phạm vi các cặp cần học, yêu cầu gần chắc chắn

$$
C_t(s,a)\longrightarrow\infty,
\qquad
\sum_{a\in\mathcal G_t(s)}\pi_t(a\mid s)\longrightarrow1.
$$

Yêu cầu thứ nhất là độ phủ vô hạn. Yêu cầu thứ hai là khối xác suất tập trung trên các hành động cực đại của bảng hiện hành. Nó cho phép đồng hạng và không bắt buộc chính sách hội tụ tới một hành động duy nhất. Trong Sarsa, quy tắc từ $Q_t$ chọn $A_{t+1}$ trước cập nhật, còn $A_t$ đã được chọn ở bước trước.

Với MC, $k$ là chỉ số lượt, $Q^{[k]}$ là bảng trước lượt và $\pi_k$ được giữ suốt lượt. Phiên bản GLIE theo lượt dùng bộ đếm lần thăm, tập cực đại và chính sách tại cùng thời điểm trước lượt. Bộ đếm lần thăm $C$ khác $N$ đếm lợi tức MC được chọn.

Đối với chính sách $\varepsilon_k$-tham lam, $\varepsilon_k\to0$ đảm bảo yêu cầu tham lam trong giới hạn. Nó chưa chứng minh thăm vô hạn. Lịch $\varepsilon_k=1/k$ theo lượt cũng cần kiểm tra khả năng đạt tới trạng thái và phân phối khởi đầu; giảm xác suất thăm dò ở mỗi trạng thái chưa đảm bảo một chuỗi các hành động thăm dò cần thiết xảy ra vô hạn lần.

### 6.3. Bước học theo từng cặp

Với một cặp $(s,a)$, đánh số $n=1,2,\ldots$ theo các lần cập nhật riêng của cặp đó. Điều kiện Robbins–Monro được dùng ở đây là

$$
0<\alpha_n(s,a)\le1,
\qquad
\sum_{n=1}^\infty\alpha_n(s,a)=\infty,
\qquad
\sum_{n=1}^\infty\alpha_n(s,a)^2<\infty.
$$

Tổng thứ nhất không cho ảnh hưởng tích lũy của các mẫu mới kết thúc quá sớm. Tổng bình phương hữu hạn kiểm soát phần nhiễu tích lũy trong các định lý đang xét. Hai điều kiện này là thành phần của một chứng minh hội tụ, không phải tiêu chuẩn xác nhận hội tụ sau hữu hạn bước.

Lịch $\alpha_n=1/n$ có tổng điều hòa phân kỳ và tổng bình phương hội tụ. Với $\alpha_n=0.8$, mỗi số hạng bình phương là $0.64$, nên tổng bình phương phân kỳ.

::: example
Giả sử một cặp chỉ được cập nhật tại các thời điểm toàn cục $t_n=2^n$. Nếu dùng lịch toàn cục $\alpha_t=1/t$, tổng bước học thực sự nhận bởi cặp ấy là

$$
\sum_{n=1}^\infty\alpha_{t_n}=\sum_{n=1}^\infty2^{-n}=1<\infty.
$$

Vì vậy việc $\sum_t1/t$ phân kỳ trên toàn bộ quá trình chưa đủ để suy điều kiện theo từng cặp. Với bộ đếm đã hoàn thành $n(s,a)$ cập nhật, bước tiếp theo dùng $1/[n(s,a)+1]$ nếu chọn lịch nghịch đảo số cập nhật.
:::

### 6.4. Bảo đảm cho Sarsa và Q-learning

Dưới các giả thiết nền ở mục 6.1, mọi cặp được cập nhật vô hạn gần chắc chắn và bước học theo cặp thỏa mục 6.3, Q-learning hội tụ

$$
Q_t(s,a)\longrightarrow q_*(s,a)
$$

gần chắc chắn với mọi cặp hợp lệ.

Chính sách hành vi có thể tiếp tục thăm dò vì mục tiêu Q-learning đã dùng cực đại. Hành vi vẫn phải duy trì độ phủ và sinh mẫu đúng động lực có điều kiện.

Sarsa có cùng kết luận khi bổ sung điều kiện chính sách trở nên tham lam theo bảng hiện hành. Cùng với thăm vô hạn, đây là điều kiện GLIE tương ứng. Với $\varepsilon>0$ cố định và một cực đại duy nhất, khối xác suất trên cực đại chưa tiến tới 1, nên không áp dụng được kết luận này của Sarsa.

Các kết quả được đối chiếu với [Singh và cộng sự, Định lý 1, tr. 294–295](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/2000-singh-littmansingh98convergence.pdf) và [Watkins–Dayan, định lý Q-learning, tr. 282](https://www.ece.uvic.ca/~bctill/papers/learning/Watkins_Dayan_1992.pdf). Khi có nhiều hành động tối ưu đồng hạng, hội tụ của bảng không bắt buộc phân phối hành động phải hội tụ tới một chính sách duy nhất.

Với MC, trung bình mẫu khi đánh giá một chính sách cố định và mệnh đề cải thiện khi biết $q_\pi$ chính xác là hai kết quả riêng. Trong điều khiển, lượt $k$ được sinh bởi $\pi_k$; các lợi tức từ các lượt khác nhau không tự có cùng kỳ vọng $q_\pi$ cố định. Hai yêu cầu GLIE không thay thế chứng minh cho một biến thể MC cụ thể. Các bảo đảm chuyên biệt phải khớp thuật toán, cách khởi đầu và lịch cập nhật, như các biến thể trong [Tsitsiklis, On the Convergence of Optimistic Policy Iteration](https://www.jmlr.org/papers/volume3/tsitsiklis02a/tsitsiklis02a.pdf), tr. 60, 66–67, 72.

### 6.5. Câu hỏi kiểm tra 6: phạm vi áp dụng định lý

::: exercise
Câu hỏi: Giả sử MDP hữu hạn, có động lực không đổi theo thời gian, thưởng bị chặn, $\gamma=0.9$, $Q_0$ hữu hạn; mẫu đúng môi trường và mọi cặp được cập nhật vô hạn. Xác định trường hợp đủ điều kiện cho kết luận hội tụ tới $q_*$ đã nêu và giả thiết còn thiếu trong các trường hợp còn lại:

| Trường hợp | Thuật toán và hành vi | Bước học theo cặp |
|---|---|---|
| a | Q-learning, $\varepsilon$-tham lam với $\varepsilon=0.25$ | $\alpha_n=1/n$ |
| b | Sarsa, $\varepsilon$-tham lam với $\varepsilon=0.25$ | $\alpha_n=1/n$ |
| c | Sarsa với GLIE | $\alpha_n=0.8$ |

Các trạng thái xét có hai hành động; ở trường hợp b có trạng thái giữ một cực đại duy nhất.
:::

::: hint
Kiểm riêng điều kiện bước học và yêu cầu đối với hành vi của từng thuật toán. Trong trường hợp b, tính khối xác suất trên cực đại. Trong trường hợp c, xét tổng bình phương bước học.
:::

::: solution
Trường hợp a thỏa các điều kiện đã nêu: lịch $1/n$ thỏa hai tổng và Q-learning không yêu cầu hành vi trở nên tham lam.

Trường hợp b thiếu yêu cầu tham lam trong giới hạn. Tại trạng thái có cực đại duy nhất, khối xác suất trên cực đại bằng $7/8$, không tiến tới 1.

Trường hợp c vi phạm tổng bình phương hữu hạn vì $\sum_n0.8^2=\infty$. Trong b và c, định lý đang xét chưa áp dụng; thiếu một giả thiết không chứng minh thuật toán chắc chắn phân kỳ.
:::

Nguồn: Tạ Việt Cường, [bài giảng nguồn](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf), tr. 25–28; Sutton và Barto, [giáo trình](https://incompleteideas.net/book/the-book-2nd.html), tr. 99–103, 129–131. Định nghĩa GLIE và điều kiện dài hạn theo Singh và cộng sự, tr. 290–295, 302–304; trường hợp không chiết khấu cần giả thiết riêng như Watkins–Dayan, tr. 285–286.

<!-- note-topic-id: lec-06-topic-07 -->
## 7. Tổng hợp, bài tập và đọc thêm

### 7.1. Chọn phương pháp theo dữ liệu và mục tiêu

Ba phương pháp đều học bảng giá trị hành động, nhưng dùng dữ liệu và mục tiêu khác nhau:

| Phương pháp | Dữ liệu cần cho cập nhật | Mục tiêu | Thời điểm cập nhật |
|---|---|---|---|
| MC theo chính sách, lần ghé đầu | Lượt hoàn chỉnh | $G_t$ | Sau lượt |
| Sarsa | Bộ năm trạng thái, hành động, thưởng, trạng thái tiếp, hành động tiếp | $R+\gamma Q(S',A')$ | Sau một chuyển và chọn $A'$ |
| Q-learning | Bộ bốn trạng thái, hành động, thưởng, trạng thái tiếp | $R+\gamma\max_aQ(S',a)$ | Sau một chuyển |

Hai mục tiêu TD trong bảng áp dụng khi trạng thái kế tiếp chưa kết thúc. Khi kết thúc, cả hai chỉ dùng $R$. MC lưu thêm quỹ đạo để tính lợi tức; Sarsa và Q-learning không cần chờ hoặc lưu toàn bộ lượt.

Quyết định tại D sau các dữ liệu đã xét là:

| Lần chạy | Hàng D, theo thứ tự $(0,1)$ | Hành động cực đại |
|---|---|---|
| MC tham lam, bảng I, lượt D–E | $(0,10)$ | Phải |
| MC, bảng II, lượt D–C–B–A | $(998,0)$ | Trái |
| Sarsa, bảng I, năm mẫu | $(-1.28,8.2)$ | Phải |
| Q-learning, bảng I, cùng năm mẫu | $(-0.64,8.2)$ | Phải |

Mỗi hàng phải được gắn với đúng khởi tạo và dữ liệu. Hai lần chạy MC dùng dữ liệu khác nhau và một lần dùng bảng đầu khác, nên bảng tổng hợp chưa tạo phép so sánh công bằng về hiệu quả học. Sarsa và Q-learning có cùng dữ liệu nhưng dùng mục tiêu khác. Một lựa chọn cực đại từ bảng hữu hạn mẫu chưa chứng nhận chính sách tối ưu.

### 7.2. Câu hỏi kiểm tra 7: lựa chọn có điều kiện

::: exercise
Câu hỏi: Chọn MC, Sarsa hoặc Q-learning phù hợp với từng yêu cầu và giải thích bằng dữ liệu cùng mục tiêu cập nhật.

1. Dùng lợi tức hoàn chỉnh và thay chính sách sau lượt.
2. Cập nhật trong lượt bằng giá trị của hành động thực sự sẽ thực hiện.
3. Có mẫu $(S,A,R,S')$ từ hành vi còn thăm dò và muốn dùng cực đại của bảng làm mục tiêu tiếp nối.

Với trường hợp 3, nêu hai điều kiện cần kiểm trước khi viện dẫn hội tụ tới $q_*$.
:::

::: hint
Đối chiếu thời điểm có đủ dữ liệu và cách tạo phần tiếp nối. Với bảo đảm dài hạn, kiểm số cập nhật của từng cặp và các tổng bước học, cùng miền giả thiết của định lý.
:::

::: solution
Trường hợp 1 phù hợp với MC theo chính sách, lần ghé đầu; cần lượt kết thúc thật và bộ đếm đúng theo các lợi tức được chọn. Trường hợp 2 phù hợp với Sarsa; cần lấy $A'$ trước cập nhật và giữ để thực hiện nếu còn tương tác. Trường hợp 3 phù hợp với Q-learning; mục tiêu trực tiếp dùng cực đại từ bảng.

Hai điều kiện cần kiểm là mọi cặp cần học được cập nhật vô hạn gần chắc chắn và bước học thỏa hai tổng Robbins–Monro theo cặp. Để dùng định lý còn cần MDP hữu hạn, có động lực không đổi theo thời gian, thưởng bị chặn, $\gamma<1$, $Q_0$ hữu hạn, mẫu đúng động lực có điều kiện và bước học được chọn từ thông tin có trước mẫu. Một bộ dữ liệu đầy đủ có thể dùng cho nhiều thuật toán; các yêu cầu trên xác định cả dữ liệu lẫn loại mục tiêu.
:::

### 7.3. Bài 10 trong bộ bài tập: MC và Q-learning trên sáu trạng thái

Bài tập này dùng môi trường riêng A–B–C–D–E–F, với A và F kết thúc, mỗi lượt bắt đầu tại D. Tập trạng thái không kết thúc là $\{B,C,D,E\}$; tại mỗi trạng thái có hai hành động 0: trái và 1: phải. Hệ số chiết khấu là $\gamma=1/2$.

Các chuyển thông thường đi một ô theo hướng của hành động. Riêng hành động trái tại B dẫn tới A với xác suất 0.9 và ở lại B với xác suất 0.1. Thưởng được xác định theo trạng thái đi tới: vào A nhận 10, vào F nhận $-2$, vào B, C, D hoặc E nhận $-1$. Bảng đầu riêng của bài tập là

| Trạng thái | $Q_0(s,0)$ | $Q_0(s,1)$ |
|---|---:|---:|
| B | $-1$ | 1 |
| C | 0 | 2 |
| D | 1 | 0 |
| E | 1 | 5 |

Hai lượt quan sát, viết mỗi chuyển theo thứ tự $(S,A,R,S')$, là

$$
\begin{aligned}
\tau_1:\quad &(D,0,-1,C),\ (C,0,-1,B),\\
             &(B,0,-1,B),\ (B,0,10,A),\\
\tau_2:\quad &(D,1,-1,E),\ (E,1,-2,F).
\end{aligned}
$$

Bài gốc giới hạn mỗi lượt ở năm bước. Hai lượt đã cho dài bốn và hai bước, đều kết thúc thật tại A hoặc F trước giới hạn. Vì vậy các lợi tức sau đây được tính từ các lượt hoàn chỉnh. Những dữ kiện này không dùng lại hệ số chiết khấu, phần thưởng hay bảng đầu của chuỗi A–E.

::: exercise
Câu hỏi: Với hai bản sao riêng của bảng đầu trên:

1. Cập nhật MC lần ghé đầu theo cặp trên $\tau_1$ rồi $\tau_2$, với mọi bộ đếm ban đầu bằng 0. Tính riêng ô $(B,0)$ nếu thay bằng mọi lần ghé.
2. Đặt lại bảng đầu và cập nhật Q-learning với $\alpha=1$ qua cả sáu mẫu theo thứ tự đã cho. Trình bày giá trị mới của mỗi ô được cập nhật và bảng cuối.
:::

::: hint
Ở lượt thứ nhất, cặp $(B,0)$ xuất hiện hai lần, với hai lợi tức khác nhau. MC lần ghé đầu chọn lần có chỉ số nhỏ hơn. Với Q-learning và $\alpha=1$, giá trị mới bằng mục tiêu; mục tiêu phải dùng bảng hiện hành trước từng mẫu, kể cả chuyển tự quay về B.
:::

::: solution
Với lượt $\tau_1$, tính lùi cho

$$
\begin{aligned}
G_3&=10,\\
G_2&=-1+\tfrac12\cdot10=4,\\
G_1&=-1+\tfrac12\cdot4=1,\\
G_0&=-1+\tfrac12\cdot1=-\tfrac12.
\end{aligned}
$$

Lần ghé đầu của $(B,0)$ là $t=2$, có lợi tức 4. Lần thứ hai có lợi tức 10 và không được dùng trong MC lần ghé đầu. Với lượt $\tau_2$, hai lợi tức là $-1+(1/2)(-2)=-2$ và $-2$.

Sau cả hai lượt, MC lần ghé đầu cho

| Trạng thái | $Q(s,0)$ | $Q(s,1)$ | $N(s,0)$ | $N(s,1)$ |
|---|---:|---:|---:|---:|
| B | 4 | 1 | 1 | 0 |
| C | 1 | 2 | 1 | 0 |
| D | $-1/2$ | $-2$ | 1 | 1 |
| E | 1 | $-2$ | 0 | 1 |

Những ô chưa có mẫu giữ giá trị khởi tạo và bộ đếm 0. Nếu dùng mọi lần ghé, riêng ô $(B,0)$ nhận hai mẫu 4 và 10, nên bằng 7 với bộ đếm 2.

Q-learning bắt đầu lại từ bảng đầu riêng của bài tập. Vì $\alpha=1$, kết quả mỗi mẫu là

| Mẫu | Ô cập nhật | Mục tiêu và giá trị mới |
|---:|---|---|
| 1: D đến C | $(D,0)$ | $-1+\tfrac12\max(0,2)=0$ |
| 2: C đến B | $(C,0)$ | $-1+\tfrac12\max(-1,1)=-\tfrac12$ |
| 3: B ở lại B | $(B,0)$ | $-1+\tfrac12\max(-1,1)=-\tfrac12$ |
| 4: B đến A | $(B,0)$ | $10$ |
| 5: D đến E | $(D,1)$ | $-1+\tfrac12\max(1,5)=\tfrac32$ |
| 6: E đến F | $(E,1)$ | $-2$ |

Ở mẫu 3, hàng B trong vế phải vẫn là hàng trước cập nhật: $(-1,1)$. Mẫu 4 mới thay ô $(B,0)$ bằng 10. Bảng cuối Q-learning là

| Trạng thái | $Q(s,0)$ | $Q(s,1)$ |
|---|---:|---:|
| B | 10 | 1 |
| C | $-1/2$ | 2 |
| D | 0 | $3/2$ |
| E | 1 | $-2$ |

Xác suất 0.9 và 0.1 mô tả nguồn sinh chuyển ngẫu nhiên. Với các mẫu đã cho, Q-learning sử dụng kết quả chuyển thực sự quan sát được; không thay mẫu bằng kỳ vọng theo hai xác suất đó.
:::

Nguồn: Tạ Việt Cường, [Bài tập tuần 3, Bài 10](../RL-hk2-2025-2026/resources/hw3.pdf), tr. 2–3. Phần trên giải các yêu cầu MC và Q-learning dạng bảng.

### 7.4. Đọc thêm: dự đoán TD(0) khác chính sách

Phần này xét dự đoán giá trị trạng thái của một chính sách đích $\pi$ cố định. Dữ liệu được sinh bởi chính sách hành vi $b$. Xét MDP hữu hạn, có động lực không đổi theo thời gian, thưởng bị chặn và $0\le\gamma<1$. Bảng $V_t(s)$ ước lượng $v_\pi(s)$; đặt giá trị tại trạng thái kết thúc bằng 0.

Để hiệu chỉnh phân phối hành động, yêu cầu

$$
\pi(a\mid s)>0\ \Longrightarrow\ b(a\mid s)>0.
$$

Với hành động thực sự lấy từ $b$, định nghĩa tỉ số lấy mẫu quan trọng

$$
\rho_t=\frac{\pi(A_t\mid S_t)}{b(A_t\mid S_t)}.
$$

Mẫu có $b(A_t\mid S_t)>0$, nên mẫu số được xác định. Các hành động có xác suất hành vi bằng 0 không được lấy mẫu. Điều kiện hỗ trợ đảm bảo không thiếu hành động có khối xác suất dương dưới chính sách đích.

Dạng cập nhật nhân tỉ số vào mục tiêu là

$$
V_{t+1}(S_t)=V_t(S_t)+\alpha_t
\left\{\rho_t\left[R_{t+1}+\gamma V_t(S_{t+1})\right]-V_t(S_t)\right\}.
$$

Các ô khác giữ nguyên. Khi trạng thái kế tiếp kết thúc, số hạng $V_t(S_{t+1})$ bằng 0. Công thức cập nhật bảng giá trị trạng thái $V$, nên thuộc dự đoán TD(0) khác chính sách. Sarsa trong phần chính cập nhật bảng giá trị hành động $Q$ và dùng hành động kế tiếp.

::: proof
Gọi $\mathcal F_t$ là thông tin có trước khi lấy $A_t$, gồm trạng thái hiện tại, bảng $V_t$ và các phân phối hành động đang dùng. Điều kiện hóa theo $\mathcal F_t$ và $S_t=s$ giữ cố định các đại lượng này. Đặt

$$
Y_t=R_{t+1}+\gamma V_t(S_{t+1}).
$$

Động lực môi trường theo cặp cho

$$
\begin{aligned}
\mathbb E_b[\rho_tY_t\mid\mathcal F_t,S_t=s]
&=\sum_{a:b(a\mid s)>0}b(a\mid s)\frac{\pi(a\mid s)}{b(a\mid s)}
\mathbb E[Y_t\mid\mathcal F_t,S_t=s,A_t=a]\\
&=\sum_a\pi(a\mid s)
\left[\bar r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)V_t(s')\right]\\
&=(T^\pi V_t)(s).
\end{aligned}
$$

$P$ và $\bar r$ lần lượt là xác suất chuyển và thưởng kỳ vọng; chúng chỉ dùng trong lập luận kỳ vọng, không phải đầu vào cần biết của cập nhật. $T^\pi$ là toán tử Bellman của chính sách cố định $\pi$. Điều kiện hỗ trợ cho phép đổi tổng trên hỗ trợ của $b$ thành tổng theo $\pi$. Do đó

$$
\mathbb E_b[\rho_tY_t-V_t(s)\mid\mathcal F_t,S_t=s]
=(T^\pi V_t)(s)-V_t(s).
$$

Đồng thời,

$$
\mathbb E_b[\rho_t\mid\mathcal F_t,S_t=s]
=\sum_{a:b(a\mid s)>0}\pi(a\mid s)=1.
$$

Vì vậy dạng nhân tỉ số vào toàn bộ sai lệch cũng thỏa

$$
\mathbb E_b[\rho_t(Y_t-V_t(s))\mid\mathcal F_t,S_t=s]
=(T^\pi V_t)(s)-V_t(s).
$$

Hai gia số chưa nhân bước học khác nhau trên từng mẫu:

$$
[\rho_tY_t-V_t(s)]-\rho_t[Y_t-V_t(s)]
=(\rho_t-1)V_t(s).
$$

Hiệu này có kỳ vọng có điều kiện bằng 0. Hai gia số chưa nhân bước học có cùng kỳ vọng có điều kiện nhưng có nhiễu khác nhau; đẳng thức không cho một thứ tự phương sai chung.
:::

Kỳ vọng vừa tính là sai lệch Bellman của bảng hiện hành $V_t$. Khi $V_t$ chưa bằng $v_\pi$, mục tiêu một bước không tự là ước lượng không chệch của giá trị thật $v_\pi(s)$. Chứng minh kỳ vọng một bước cũng chưa tự chứng minh hội tụ của một quá trình đổi chính sách hoặc dùng xấp xỉ hàm.

Điều kiện hỗ trợ để định nghĩa tỉ số khác với việc trạng thái cần đánh giá được ghé và cập nhật đủ lâu. Q-learning một bước ở phần chính tạo mục tiêu bằng cực đại trực tiếp nên không cần hiệu chỉnh một hành động kế tiếp lấy từ hành vi bằng tỉ số này.

Nguồn: công thức cập nhật $V$ nhân tỉ số vào riêng mục tiêu trong [bài giảng nguồn, tr. 19](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf); đối chiếu dạng nhân toàn bộ sai lệch với Sutton và Barto, [giáo trình](https://incompleteideas.net/book/the-book-2nd.html), §7.3, công thức (7.9)–(7.10), tr. 148, khi số bước bằng 1.

### 7.5. Đọc thêm: sai số đánh giá một chính sách cố định

Cố định một chính sách $\pi$ và phân phối trạng thái đầu $d_0$. Mục tiêu đánh giá là đại lượng vô hướng

$$
J_{d_0}(\pi)=\mathbb E_{S_0\sim d_0,\pi}[G_0].
$$

Nếu $d_0$ tập trung tại một trạng thái $s$, đại lượng này bằng $v_\pi(s)$. Trong mục này, $n$ là số lượt đánh giá độc lập, khác số cập nhật theo cặp ở phần bước học. Cố định $n\ge1$ trước khi lấy dữ liệu. Mỗi lượt bắt đầu độc lập theo cùng $d_0$, thực hiện cùng $\pi$ và được quan sát hoàn chỉnh. Gọi $G^{(i)}$ là lợi tức ngẫu nhiên từ đầu lượt thứ $i$, với $i=1,\ldots,n$. Ước lượng là

$$
\widehat J_n=\frac1n\sum_{i=1}^nG^{(i)}.
$$

Giả sử có các số hữu hạn $L,U$ sao cho $L\le G^{(i)}\le U$ gần chắc chắn và đặt độ rộng $B=U-L>0$. Với sai số $\eta>0$, bất đẳng thức Hoeffding hai phía cho

$$
\Pr\left\{\left|\widehat J_n-J_{d_0}(\pi)\right|>\eta\right\}
\le2\exp\left(-\frac{2n\eta^2}{B^2}\right).
$$

Đặt $\delta\in(0,1)$ là cận xác suất vi phạm chặn sai số; ký hiệu này khác sai lệch TD $\delta_t$. Với xác suất ít nhất $1-\delta$,

$$
\left|\widehat J_n-J_{d_0}(\pi)\right|
\le B\sqrt{\frac{\log(2/\delta)}{2n}}.
$$

::: proof
Các biến $G^{(i)}$ độc lập, có cùng kỳ vọng $J_{d_0}(\pi)$ và mỗi biến nằm trong đoạn độ rộng $B$. Áp dụng Hoeffding cho tổng $\sum_{i=1}^nG^{(i)}$ với độ lệch $n\eta$ cho đuôi trên:

$$
\Pr\left\{\sum_{i=1}^nG^{(i)}-nJ_{d_0}(\pi)>n\eta\right\}
\le\exp\left(-\frac{2(n\eta)^2}{\sum_{i=1}^n B^2}\right)
=\exp\left(-\frac{2n\eta^2}{B^2}\right).
$$

Áp dụng tương tự cho các biến $-G^{(i)}$ cho đuôi dưới. Cộng hai xác suất cho chặn hai phía. Giải phương trình $2\exp(-2n\eta^2/B^2)=\delta$ theo $\eta$ cho bán kính sai số đã nêu.

Muốn bán kính không vượt mức $\eta$ cho trước, chọn số nguyên $n$ thỏa

$$
n\ge\left\lceil\frac{B^2}{2\eta^2}\log\frac2\delta\right\rceil.
$$

Nếu $B=0$, lợi tức là hằng số và trung bình bằng kỳ vọng; không cần dùng biểu thức có mẫu số $B^2$.
:::

Độ rộng phải được tính từ khoảng lợi tức, không chỉ từ một cận trị tuyệt đối của phần thưởng. Với $0\le\gamma<1$, chuỗi hình học cho các lựa chọn sau:

| Giả thiết phần thưởng | Khoảng chứa lợi tức | Độ rộng dùng được |
|---|---|---|
| $0\le R\le R_{\max}$ | $[0,R_{\max}/(1-\gamma)]$ | $B=R_{\max}/(1-\gamma)$ |
| $\lvert R\rvert\le R_{\max}$ | $[-R_{\max}/(1-\gamma),R_{\max}/(1-\gamma)]$ | $B=2R_{\max}/(1-\gamma)$ |

Vì vậy cận thưởng có dấu làm độ rộng được bảo đảm lớn gấp đôi so với giả thiết thưởng không âm cùng $R_{\max}$. Với $\gamma=1$, công thức chia cho $1-\gamma$ không áp dụng. Nếu mọi lượt dài không quá một số cố định $H$ và $|R|\le R_{\max}$, có thể dùng khoảng $[-HR_{\max},HR_{\max}]$. Chỉ biết kết thúc gần chắc chắn, khi độ dài lượt không bị chặn, chưa đảm bảo một độ rộng lợi tức hữu hạn. Vì thế chặn chiết khấu trên không được áp ngầm cho chuỗi A–E có $\gamma=1$.

Các phần thưởng bên trong một lượt có thể phụ thuộc nhau. Yêu cầu độc lập ở đây đặt lên các lợi tức hoàn chỉnh $G^{(i)}$ của những lượt khác nhau. Nhiều lần ghé trong cùng một lượt không tự cung cấp các mẫu độc lập. Nếu chính sách đổi giữa các lượt, các kỳ vọng không còn nhất thiết bằng cùng $J_{d_0}(\pi)$.

Chặn đánh giá một chính sách tại số lượt $n$ cố định không xác định số mẫu cần để tìm chính sách tối ưu hoặc học thích nghi toàn bảng $Q$. Nó cũng không tự đúng đồng thời tại mọi thời điểm dừng phụ thuộc dữ liệu. Số lượt $n$ khác số chuyển môi trường; số chuyển đã thu là tổng độ dài các lượt. Với một quá trình tiếp tục, việc cắt tổng lợi tức tại một số bước hữu hạn còn tạo sai số cắt ngắn cần kiểm riêng.

Nguồn: [Hoeffding, Probability Inequalities for Sums of Bounded Random Variables](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf), Định lý 2, tr. 16; đại lượng đánh giá và giả thiết làm rõ cho chặn trong [bài giảng nguồn, tr. 29](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf).

### 7.6. Tài liệu học tiếp

Sutton và Barto, [Reinforcement Learning: An Introduction, ấn bản 2](https://incompleteideas.net/book/the-book-2nd.html), §§5.2–5.4 trình bày giá trị hành động, điều khiển Monte Carlo và chính sách mềm; §§6.4–6.5 trình bày Sarsa và Q-learning. Đối với mỗi thuật toán, việc đối chiếu cần giữ đủ đầu vào, mục tiêu, thời điểm chọn hành động và nhánh trạng thái kết thúc.

Các bài tính trong [bài giảng nguồn, tr. 16–18 và 21](../RL-hk2-2025-2026/lecture-06-model-free-control.pdf) và [Bài 10 của bộ bài tập](../RL-hk2-2025-2026/resources/hw3.pdf) cung cấp dữ liệu để tái thực hiện các cập nhật. Các bảng và lời giải ở trên chỉ rõ khởi tạo, thứ tự mẫu và các giả thiết dùng cho từng kết quả.
