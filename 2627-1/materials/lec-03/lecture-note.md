# Bài 03 — Quá trình quyết định Markov

Học tăng cường · Học kỳ 1, 2026–2027 · Trường Đại học Công nghệ · Đại học Quốc gia Hà Nội

<!-- note-topic-id: lec-03-part-01 -->
## 1. Từ tương tác đến trạng thái Markov

Quá trình quyết định Markov (MDP) mô tả việc tác tử chọn hành động và nhận phản hồi từ môi trường qua nhiều bước. Bài học dùng robot thu gom lon để xây dựng mô hình xác suất, suy ra phương trình Bellman và tính giá trị của một cách điều khiển đã cho.

### Mục tiêu và kiến thức tiên quyết

Sau bài học, sinh viên cần mô tả được một bài toán bằng MDP, phân biệt quy luật môi trường với chính sách, suy ra Bellman từ tổng thưởng, rồi lập và giải một hệ giá trị nhỏ. Kiến thức cần có gồm xác suất có điều kiện, kỳ vọng, giải hệ tuyến tính và giao diện tác tử–môi trường ở Bài 02.

### Nội dung bài học

1. Từ tương tác đến trạng thái Markov
2. Mô hình xác suất của MDP
3. Phần thưởng và tổng thưởng
4. Chính sách và hàm giá trị
5. Phương trình Bellman
6. Đánh giá một chính sách từ mô hình
7. Tổng hợp và vận dụng

### Robot thu gom lon

Robot thu gom lon có hai mức pin: $\mathrm H$ là pin cao, $\mathrm L$ là pin thấp. Tại $\mathrm L$, robot có thể Tìm, Chờ hoặc Sạc. Mục tiêu của robot là thu gom lon lâu dài, tức tổng phần thưởng theo thời gian lớn nhất. Lựa chọn hiện tại thay đổi những lựa chọn có thể tiếp tục thực hiện sau đó: hành động Tìm có thể thu được lon nhưng cũng có thể làm cạn pin, buộc robot vào tình thế phải cứu hộ. Hành động Sạc dùng trọn một bước để phục hồi pin cao, nên robot phải cân bằng giữa thưởng ngắn hạn và trạng thái tương lai. Một bước là một chu kỳ quyết định, không nhất thiết một giây. Trước khi so sánh các lựa chọn, cần mô tả chính xác một bước tương tác.

### Mẫu đơn của một bước tương tác

Một kết quả đã xảy ra: từ pin cao, robot chọn Tìm, nhận 2 điểm và sang pin thấp:

$$(S_t,\,A_t,\,R_{t+1},\,S_{t+1})=(\mathrm H,\ \mathrm{tim},\ 2,\ \mathrm L).$$

Thời gian được đánh số $t=0,1,2,\ldots$. Trong bộ dữ liệu, $S_t$ là trạng thái tại thời điểm quyết định $t$, $A_t$ là hành động chọn tại đó. Phần thưởng mang chỉ số $t+1$ vì nó xuất hiện sau khi hành động $A_t$ được thực hiện. Theo quy ước của Sutton và Barto, chuỗi $S_0, A_0, R_1, S_1, A_1, R_2, S_2, \ldots$ xen kẽ trạng thái, hành động và phần thưởng. Ký hiệu ngắn $\mathrm{tim}$, $\mathrm{cho}$, $\mathrm{sac}$ là nhãn toán cho các hành động Tìm, Chờ, Sạc. Kết quả trên là một mẫu đơn lẻ làm ví dụ minh họa, chưa phải quy luật xác suất; lịch sử của robot nối các mẫu này theo thứ tự thời gian.

### Hai lịch sử, cùng trạng thái hiện tại

![Hai lịch sử quá khứ khác nhau nhập vào cùng trạng thái L, cùng chọn Tìm, rồi dẫn tới hai kết quả](img/lec-03/robot-p01-two-histories.svg)

Hai robot: một vừa tìm kiếm xong, một vừa chờ xong; cả hai giờ ở $\mathrm L$ và cùng chọn Tìm. Giả thiết của mô hình là phân phối của cặp trạng thái kế tiếp và phần thưởng không phụ thuộc vào việc robot vừa làm gì. Đây là giả thiết của mô hình lý tưởng, không phải khẳng định mức pin luôn đủ cho mọi robot thật: nếu vị trí cũng làm thay đổi cơ hội gặp lon thì trạng thái phải bổ sung vị trí.

### Tính Markov

Lịch sử tới thời điểm $t$ là $H_t=(S_0,A_0,R_1,\ldots,S_t)$. Với mọi phản hồi $(s',r)$:

$$\begin{aligned}&\Pr(S_{t+1}=s',R_{t+1}=r\mid H_t,A_t)\\&\quad=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t,A_t).\end{aligned}$$

Đẳng thức xét ở những điều kiện có thể xảy ra: lịch sử và cặp trạng thái–hành động đó phải có xác suất dương. Trạng thái $S_t$ giữ lại thông tin từ lịch sử có ảnh hưởng đến phân phối phản hồi. Trong ví dụ robot, mức pin là trạng thái lý tưởng hóa: nó giữ thông tin quá khứ có ảnh hưởng tới phân phối bước tới. Biết đúng trạng thái là đủ về thông tin, nhưng chưa có nghĩa là đã biết các con số xác suất trong phân phối ấy.

::: exercise Câu hỏi kiểm tra

1. Hành động $A_t$ tạo ra $R_t$ hay $R_{t+1}$?
2. Hai robot cùng pin thấp nhưng ở hai vị trí có cơ hội gặp lon khác nhau: chỉ dùng mức pin làm trạng thái đã đủ chưa?
3. Quan sát đúng trạng thái có đồng nghĩa biết xác suất chuyển không?
:::

::: solution
1. $R_{t+1}$: phần thưởng xuất hiện sau khi $A_t$ được thực hiện, nên mang chỉ số $t+1$ theo quy ước của Sutton và Barto.
2. Chưa đủ nếu vị trí thay đổi phân phối phản hồi; khi đó hai lịch sử cùng mức pin nhưng khác vị trí cho phân phối khác nhau, vi phạm tính Markov; cần bổ sung thông tin liên quan như vị trí vào trạng thái.
3. Không. Trạng thái là đầu vào của phân phối điều kiện; biết đầu vào không đồng nghĩa biết quy luật phản hồi có điều kiện, quy luật đó là phần mô hình còn thiếu. Bước tiếp theo là mô tả quy luật này bằng bảng các kết quả có thể xảy ra.
:::

<!-- note-topic-id: lec-03-part-02 -->
## 2. Mô hình xác suất của MDP

Phần trước chỉ quan sát một mẫu: từ pin cao, robot chọn Tìm rồi về pin thấp với thưởng 2. Một mẫu duy nhất không cho biết tần suất từng kết quả. Giả thiết ở đây: môi trường là ngẫu nhiên, thưởng cố định trên mỗi nhánh, và quy luật phản hồi không đổi theo thời gian. Mô hình xác suất phải mô tả mọi phản hồi có thể xảy ra sau mỗi cặp trạng thái–hành động, tức là cho cả trạng thái kế tiếp lẫn phần thưởng trong cùng một bước. Hành động đã được cố định; các xác suất mô tả phản hồi ngẫu nhiên của môi trường.

### Hai phản hồi của hành động Tìm

![Tìm từ L: L và thưởng 2 hoặc H và thưởng −3 do cứu hộ. Tìm từ H: H hoặc L, đều thưởng 2. Mỗi nhánh xác suất một phần hai.](img/lec-03/robot-p02-search-outcomes.svg)

Mỗi kết quả là một cặp trạng thái mới kèm thưởng. Từ pin thấp, Tìm giữ robot ở pin thấp và nhận 2 với xác suất $1/2$, hoặc pin cạn, robot được cứu hộ về pin cao và nhận $-3$ với xác suất $1/2$; hai xác suất cộng bằng 1. Từ pin cao, Tìm dẫn tới pin cao hoặc pin thấp, mỗi nơi $1/2$, đều nhận 2. Trạng thái kế tiếp và phần thưởng được rút thăm cùng nhau trong một bước, không phải hai lần độc lập. Ở pin thấp, biết thưởng là $-3$ là biết robot đã được cứu về pin cao; cứu hộ đã tính trọn trong một bước, không cộng thêm 2.

### Bảng phản hồi của robot

| Hiện tại | Hành động | Kế tiếp | Thưởng | Xác suất |
|---|---|---|---|---|
| Pin cao | Tìm | Pin cao | 2 | 1/2 |
| Pin cao | Tìm | Pin thấp | 2 | 1/2 |
| Pin cao | Chờ | Pin cao | 1 | 1 |
| Pin thấp | Tìm | Pin thấp | 2 | 1/2 |
| Pin thấp | Tìm | Pin cao (cứu hộ) | −3 | 1/2 |
| Pin thấp | Chờ | Pin thấp | 1 | 1 |
| Pin thấp | Sạc | Pin cao | 0 | 1 |

Bảng bảy hàng này chuyển cây phản hồi thành dữ liệu mô hình. Các hàng có cùng cặp hiện tại–hành động tạo thành một nhóm; tổng xác suất của mỗi nhóm bằng 1: hai hàng $1/2$ cộng lại là 1, hàng đơn có xác suất 1. Bảng chỉ ghi các kết quả có xác suất dương trong các cặp hợp lệ; cặp Pin cao–Sạc không hợp lệ nên không có hàng nào, vì Sạc chỉ có ở pin thấp. Tập hành động phụ thuộc mức pin: ở pin cao chỉ có Tìm và Chờ, ở pin thấp thêm Sạc. Chờ giữ nguyên mức pin và nhận 1; Sạc từ pin thấp chủ động đưa robot về pin cao và nhận 0, khác với cứu hộ thụ động nhận $-3$. Sách cho thưởng kỳ vọng trên nhánh; để xác định phân phối chung trong ví dụ số này, ta giả sử thưởng cố định trên mỗi nhánh.

### Định nghĩa hàm $p$

Gọi $\mathcal S$ là tập trạng thái, $\mathcal A(s)$ là tập hành động hợp lệ tại $s$, $\mathcal R$ là tập điểm thưởng; cả ba đều hữu hạn. Ví dụ đọc một dòng bảng: $p(\mathrm H,-3\mid \mathrm L,\mathrm{tim})=\tfrac12$ nghĩa là từ pin thấp, chọn Tìm, robot về pin cao với thưởng $-3$ với xác suất $1/2$. Hàm $p$ được định nghĩa:

$$\begin{aligned}&p(s',r\mid s,a)\\&\quad=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a).\end{aligned}$$

Bốn nhãn của một dòng bảng đặt vào đúng bốn vị trí của $p$: hiện tại là $s$, hành động là $a$, cả hai đứng sau vạch điều kiện và được cố định; kế tiếp là $s'$ trước dấu phẩy, thưởng là $r$ sau dấu phẩy, hai đại lượng này chạy trong tổng chuẩn hóa:

$$p(s',r\mid s,a)\ge 0,\qquad\sum_{s'\in\mathcal S}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1.$$

Điều kiện chuẩn hóa: với mỗi cặp hợp lệ, tổng mọi xác suất bằng 1: với L–Tìm thì $1/2+1/2=1$; với L–Chờ, hàng duy nhất có xác suất 1; mỗi xác suất không âm. Viết $p$ không có chỉ số thời gian nghĩa là thêm giả thiết quy luật phản hồi không đổi theo thời gian. Giả thiết này khác điều kiện Markov của phần 1: Markov nói phản hồi chỉ phụ thuộc trạng thái và hành động hiện tại, còn giả thiết mới nói bảng đó không thay đổi qua các bước. Chỉ số trong phương trình (3.2) của sách dùng $t-1,t$; ở đây dịch sang $t,t+1$ vì thưởng $R_{t+1}$ đến sau hành động $A_t$.

### Xác suất chuyển và thưởng trung bình

Vẫn cố định cặp pin thấp–Tìm. Xác suất về pin cao là $1/2$ vì trong bảng chỉ một hàng dẫn tới pin cao với trọng số $1/2$. Thưởng trung bình là trung bình có trọng số của hai mức thưởng:

$$\tfrac12\cdot 2+\tfrac12\cdot(-3)=-\tfrac12.$$

$-1/2$ là kỳ vọng; mỗi lần robot nhận 2 hoặc $-3$, không lần nào nhận đúng điểm đó. Hai đại lượng phái sinh từ cùng hạt nhân $p$:

$$p(s'\mid s,a)=\sum_{r\in\mathcal R}p(s',r\mid s,a),$$

$$r(s,a)=\mathbb E[R_{t+1}\mid S_t=s,A_t=a]=\sum_{s'\in\mathcal S}\sum_{r\in\mathcal R}r\,p(s',r\mid s,a).$$

Xác suất tới một trạng thái đích bằng tổng trọng số của các hàng dẫn tới đúng trạng thái đó; $r(s,a)$ là kỳ vọng của biến ngẫu nhiên $R_{t+1}$, có thể bằng $-1/2$ dù kết quả thực tế chỉ là 2 hoặc $-3$. Khi viết $p$ với ba đối số $p(s'\mid s,a)$, đó là xác suất chuyển đã cộng hết các mức thưởng của mọi hàng dẫn tới $s'$. Hai công thức lấy từ cùng hạt nhân $p$, không cần thêm dữ liệu mới.

### Các thành phần của MDP

| Thành phần | Ý nghĩa | Ở robot |
|---|---|---|
| $\mathcal S$ | Tập trạng thái | $\{\mathrm H,\mathrm L\}$ |
| $\mathcal A(s)$ | Tập hành động hợp lệ tại $s$, phụ thuộc mức pin | H: Tìm, Chờ; L: Tìm, Chờ, Sạc |
| $\mathcal R$ | Tập điểm thưởng hữu hạn | $\{-3,0,1,2\}$ |
| $p(s',r\mid s,a)$ | Bảng phản hồi, tổng mỗi nhóm bằng 1 | Bảy hàng đã lập |

$$\mathcal M=\bigl(\mathcal S,\ \{\mathcal A(s)\}_{s\in\mathcal S},\ \mathcal R,\ p\bigr).$$

Mỗi thành phần đã có nghĩa qua robot: hai trạng thái pin, hành động phụ thuộc mức pin, bốn điểm thưởng, và bảng phản hồi bảy hàng; trạng thái Markov, quy luật phản hồi không đổi theo thời gian. Bộ $\mathcal M$ mô tả môi trường; tiêu chuẩn cộng thưởng và cách chọn hành động cần được xác định thêm để đánh giá kết quả dài hạn. Do đó biết mô hình chưa tự xác định hành động tốt nhất.

::: exercise Câu hỏi kiểm tra

1. Đọc $p(\mathrm H,0\mid \mathrm L,\mathrm{sac})$; tổng xác suất sau L–Sạc bằng bao nhiêu?
2. Thưởng trung bình sau L–Tìm bằng bao nhiêu? Robot có lần nào nhận đúng điểm đó?
3. Nếu thưởng là $-3$ sau L–Tìm, trạng thái kế tiếp là gì? Thưởng và trạng thái mới có độc lập không?
:::

::: solution
1. $p(\mathrm H,0\mid \mathrm L,\mathrm{sac})=1$ vì hàng duy nhất của L–Sạc; tổng xác suất các phản hồi sau L–Sạc cũng bằng 1 theo điều kiện chuẩn hóa.
2. Thưởng trung bình là $\tfrac12\cdot 2+\tfrac12\cdot(-3)=-\tfrac12$; đó là kỳ vọng, không phải điểm robot luôn nhận, vì kết quả thực tế chỉ là 2 hoặc $-3$.
3. Trạng thái kế tiếp là pin cao; thưởng $-3$ xảy ra đúng khi được cứu hộ. Hai đại lượng không độc lập trong ví dụ này: rút thăm cho ra cặp (trạng thái mới, thưởng) cùng nhau, nên biết một thành phần suy ra được thông tin về thành phần kia.
:::

<!-- note-topic-id: lec-03-part-03 -->
## 3. Phần thưởng và tổng thưởng

Đại lượng cần đánh giá là tổng thưởng trên một quỹ đạo, được xây từ thưởng từng bước. Xét một đoạn đường đi: robot ở pin thấp sạc để về pin cao rồi hai lần tìm: Sạc làm pin cao nên bước tiếp theo có thể nhận $+2$, tìm từ pin cao có thể dẫn tới pin thấp. Trước khi cộng điểm cần phân biệt hai loại bài toán: có kết thúc tự nhiên hay còn tiếp diễn; hai trường hợp cho hai công thức tổng khác nhau.

### Nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn

$T$ là thời điểm kết thúc một lượt (episode) tại trạng thái kết thúc. Sau đích, dãy thưởng được đệm bằng 0: đây là quy ước toán học về trạng thái hấp thụ của chính lượt đã kết thúc, giúp viết công thức tổng thống nhất cho cả hai loại bài toán; các số 0 kéo dài biểu diễn toán học của lượt cũ, và phần thưởng của một lượt mới được tính trong một tổng riêng. Nhiệm vụ tiếp diễn không có $T$ hữu hạn: robot là nhiệm vụ tiếp diễn, nên $T=\infty$. Ba bước L→Sạc→H rồi tiếp tục hoạt động chỉ là một đoạn cắt ra, chưa phải một lượt hoàn chỉnh; cả việc được cứu hộ lẫn sạc pin đều tiếp tục cùng một nhiệm vụ đang chạy, không tạo ra ranh giới giữa các lượt. Thời điểm nhận thưởng quyết định trọng số của nó trong tổng.

### Điểm thưởng ở các thời điểm

![Hai đoạn ba thưởng: 0,2,2 và 1,1,1; trọng số tương ứng 1, 1/2, 1/4](img/lec-03/robot-p03-discounted-bands.svg)

Từ L, dãy $(0,2,2)$ là một tiền tố ba bước có thể xảy ra theo đường cụ thể L --Sạc/0--> H --Tìm/+2--> H --Tìm/+2--> L: Sạc nhận 0, hai lần Tìm từ pin cao mỗi lần nhận $+2$. Đây chỉ là một đường khả dĩ, không phải kết quả tất nhiên của việc chọn Sạc rồi Tìm hai lần: lần Tìm đầu có thể đưa robot về pin thấp, và lần Tìm tiếp theo từ pin thấp có thể phát sinh cứu hộ. Chờ ba lần giữ nguyên pin thấp nên dãy $(1,1,1)$ là tất định. Hệ số chiết khấu $\gamma=1/2$ làm trọng số giảm một nửa mỗi bước:

$$\begin{aligned}0+\frac12\cdot2+\frac14\cdot2&=\frac32,\\1+\frac12\cdot1+\frac14\cdot1&=\frac74.\end{aligned}$$

Thưởng đến muộn bị giảm giá theo $\gamma=1/2$. So sánh này chỉ đối chiếu hai dãy thưởng cụ thể, không suy ra chính sách nào tốt hơn: một tiền tố ba bước mẫu không quyết định giá trị toàn tương lai của chính sách.

### Tổng thưởng từ thời điểm hiện tại

$G_t$ là tổng thưởng chiết khấu sau thời điểm $t$, với $\gamma\in[0,1]$. Lượt kết thúc ở $T$:

$$G_t=\sum_{k=t+1}^{T}\gamma^{k-t-1}R_k.$$

Tiếp diễn hoặc đệm thưởng 0:

$$G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}.$$

$G_t$ cộng các thưởng nhận được sau thời điểm $t$, tức bắt đầu từ $R_{t+1}$ với trọng số $\gamma^0=1$. Trong tổng thứ nhất, chỉ số $k$ chạy trên thời điểm nên mũ là $k-t-1$; trong tổng thứ hai, chỉ số $k$ chạy trên khoảng cách nên mũ là $k$ và thưởng là $R_{t+k+1}$. Hai tổng cùng bắt đầu bằng $R_{t+1}$ và bằng nhau khi dãy thưởng được đệm 0 sau $T$, vì các số hạng $\gamma^{k}R_{t+k+1}$ với $k\ge T-t$ đều triệt tiêu. Việc đệm 0 sau $T$ là quy ước trạng thái hấp thụ của chính lượt đã kết thúc, không thêm quyết định hay phần thưởng mới của tác tử. Với bài có lượt, $\mathcal S$ gồm trạng thái chưa kết thúc; $\mathcal S^+$ thêm trạng thái kết thúc, và tại đó $G_T=0$ vì không còn thưởng nào sau $T$. $R_T$ có thể khác 0, còn $G_T=0$ đo phần thưởng nhận sau thời điểm $T$. Với robot tiếp diễn, dùng $\gamma<1$.

### Điều kiện để tổng thưởng hữu hạn

Nếu mọi thưởng bị chặn $|R_t|\le M$ và $0\le\gamma<1$ thì theo bất đẳng thức tam giác:

$$\lvert G_t\rvert\le\sum_{k=0}^{\infty}\gamma^k M=\frac{M}{1-\gamma},$$

vì $\sum_{k=0}^{\infty}\gamma^k=1/(1-\gamma)$ hội tụ khi $\gamma<1$. $M$ là cận trị tuyệt đối của phần thưởng từng bước, không phải một giá trị cụ thể. Robot có $M=\max_{r\in\mathcal R}|r|=3$ và $\gamma=1/2$, nên $|G_t|\le 6$ với mọi quỹ đạo; đây là cận trị tuyệt đối, không phải giá trị chính xác.

Giả thiết này cần cho phần Bellman sau: cận hữu hạn của trị tuyệt đối kéo theo kỳ vọng trị tuyệt đối hữu hạn, cho phép đổi thứ tự tổng và kỳ vọng, dùng tuyến tính và kỳ vọng lặp. Trường hợp $\gamma=1$ với bài có kết thúc: nếu thưởng bị chặn và kỳ vọng số bước tới kết thúc hữu hạn thì kỳ vọng tổng thưởng hữu hạn; chỉ gắn nhãn kết thúc cho một trạng thái chưa bảo đảm tác tử sẽ tới đó hoặc kỳ vọng thời gian tới đó hữu hạn.

::: exercise Câu hỏi kiểm tra

1. Robot về H sau Sạc có kết thúc nhiệm vụ không?
2. Với dãy ba thưởng $(0,2,2)$ và $\gamma=1/2$, điểm của đoạn là bao nhiêu? Nếu $\gamma=0$ thì còn số hạng nào?
3. Cận 6 ở phần trước có nghĩa mọi quỹ đạo của robot đều có tổng thưởng bằng 6 không?
:::

::: solution
1. Không: Sạc chủ động nhận 0 và nhiệm vụ tiếp diễn không có thời điểm kết thúc; về pin cao chỉ là thay đổi trạng thái.
2. Điểm của đoạn là $0+\frac12\cdot2+\frac14\cdot2=3/2$; khi $\gamma=0$, chỉ số hạng đầu còn lại, và nó bằng 0.
3. Không: 6 là cận trị tuyệt đối $|G_t|\le M/(1-\gamma)$ với $M=3$, $\gamma=1/2$, tức $-6\le G_t\le 6$ trên mọi quỹ đạo; tổng trên mỗi quỹ đạo nằm trong khoảng này, không nhất thiết bằng 6.
:::

<!-- note-topic-id: lec-03-part-04 -->
## 4. Chính sách và hàm giá trị

Tổng thưởng $G_t$ trên một quỹ đạo phụ thuộc vào cách robot chọn hành động ở từng thời điểm. Bảng xác suất phản hồi $p$ ở phần trước chỉ mô tả điều xảy ra *sau khi* một hành động đã được chọn; nó không nói gì về việc hành động đó được chọn theo quy tắc nào. Muốn nói đến trung bình của tổng thưởng trên nhiều quỹ đạo, trước hết phải cố định quy tắc chọn hành động. Quy tắc đó gọi là chính sách.

### Một cách điều khiển robot

| | Tìm | Chờ | Sạc |
|---|---|---|---|
| tại H | 1 | 0 | — |
| tại L | 0 | 1/2 | 1/2 |

(—: hành động không hợp lệ.)

Tại H chính sách luôn chọn Tìm; tại L nó chọn Chờ hoặc Sạc, mỗi hành động với xác suất một nửa. Đây là một cách điều khiển cố định dùng để đánh giá trong suốt phần này, chưa có khẳng định nào về hành vi tối ưu. Ô H–Sạc bị gạch thay vì ghi 0: 0 là xác suất của một hành động hợp lệ nhưng không được chọn, còn ô gạch nghĩa là cặp trạng thái–hành động nằm ngoài tập điều khiển. Tại H, quy tắc chọn hành động là tất định; tại L, quy tắc là ngẫu nhiên. Vì vậy chính sách trên toàn mô hình là chính sách ngẫu nhiên.

Từ phần này, các phép tính của robot dùng $\gamma=1/2$ và chính sách cố định trong bảng trên.

### Chính sách là phân phối trên hành động

Khái quát từ bảng trên, một chính sách là phân phối xác suất trên hành động tại mỗi trạng thái:

$$\pi(a\mid s)=\Pr(A_t=a\mid S_t=s),$$

với điều kiện chuẩn hóa

$$\pi(a\mid s)\ge 0,\qquad \sum_{a\in\mathcal A(s)}\pi(a\mid s)=1.$$

Ví dụ, từ ô L–Chờ của bảng, $\pi(\mathrm{cho}\mid \mathrm L)=1/2$. Trong bài này chính sách là **Markov** và **dừng**: nó chỉ phụ thuộc trạng thái hiện tại, không phụ thuộc lịch sử, và không đổi theo thời gian. Cần phân biệt hai tầng ngẫu nhiên: chính sách rút thăm hành động, môi trường quyết định phản hồi. Ký hiệu $\mathbb E_\pi$ lấy trung bình theo cả chính sách và môi trường. Cố định chính sách ngẫu nhiên không loại bỏ việc rút thăm hành động. Trong một bước, xác suất chọn hành động rồi nhận một cặp phản hồi là tích của xác suất chính sách và xác suất phản hồi có điều kiện. Xác suất của cả một đường đi là tích các hệ số tương ứng qua từng bước.

### Trung bình trên các nhánh quỹ đạo

Xét kỳ vọng của hai bước đầu khi xuất phát ở H, với $\gamma=1/2$:

$$G_0^{[2]}=R_1+\gamma R_2.$$

![Cây hai bước từ H: chọn Tìm thưởng 2; bước 1 tới H hoặc L mỗi nơi 1/2; nếu H, bước 2 Tìm thưởng 2 cho điểm 3 với xác suất 1/2; nếu L, Chờ hoặc Sạc mỗi 1/2 cho điểm 5/2 hoặc 2, xác suất mỗi nhóm 1/4](img/lec-03/robot-p04-two-step-tree.svg)

Xác suất của một đường đi hai bước là tích các xác suất chọn hành động và phản hồi qua cả hai bước. Nhánh Tìm ở bước hai dẫn tới H hoặc L với xác suất $1/2$ mỗi trạng thái, nhưng cả hai đều cho thưởng 2, nên cả hai nhánh con đều cho $G_0^{[2]}=2+\tfrac12\cdot 2=3$; nhóm hai trạng thái cuối này mang xác suất $(1/2)(1/2)+(1/2)(1/2)=1/2$. Nhánh Chờ: chọn Chờ với xác suất $1/2$, phản hồi tất định với hệ số 1, nên xác suất nhánh là $(1/2)(1/2)\cdot 1=1/4$ và $G_0^{[2]}=2+\tfrac12\cdot 1=5/2$. Nhánh Sạc tương tự có xác suất $1/4$ và $G_0^{[2]}=2+\tfrac12\cdot 0=2$. Nhãn 1 giữa H và Tìm ở bước hai là xác suất chính sách chọn Tìm, không phải hệ số nhân trả thưởng. Ba nhóm có trọng số $1/2,\,1/4,\,1/4$:

$$\mathbb E_\pi\!\left[G_0^{[2]}\mid S_0=\mathrm H\right]=\frac12\,3+\frac14\,\frac52+\frac14\,2=\frac{21}{8}.$$

Kết quả $21/8$ là kỳ vọng của đúng hai bước đầu, chưa phải giá trị toàn tương lai $v_\pi(\mathrm H)$.

### Giá trị trạng thái

Kỳ vọng của hai bước đầu chỉ xét một đoạn của mỗi quỹ đạo. Giá trị trạng thái mở rộng đối tượng lấy trung bình sang toàn bộ tương lai:

$$v_\pi(s)=\mathbb E_\pi\!\left[G_t\mid S_t=s\right].$$

Nghĩa là: xuất phát ở $s$, mọi hành động về sau đều được rút theo $\pi$, và $G_t$ gồm cả phần sau hai bước. $v_\pi(\mathrm H)$ là tổng thưởng kỳ vọng từ pin cao khi robot theo $\pi$. Đây là một hàm từ $\mathcal S$ vào $\mathbb R$; nếu có trạng thái kết thúc thì giá trị của nó bằng 0. $G_t$ thay đổi theo từng quỹ đạo, nhưng khi mô hình, chính sách và tiêu chuẩn tổng thưởng đã cố định, $v_\pi(s)$ là một số xác định; điều kiện hội tụ của chuỗi thưởng đã kiểm ở phần 3. Định nghĩa này để chính sách chọn cả hành động đầu; muốn đánh giá riêng một lựa chọn, cần đổi thí nghiệm.

### Ấn định hành động đầu tiên

![Ba thí nghiệm từ L với hành động đầu lần lượt bị ấn định là Tìm, Chờ, Sạc, rồi tiếp tục theo chính sách](img/lec-03/robot-p04-forced-first-action.svg)

Xuất phát ở L; lần lượt buộc hành động đầu là Tìm, Chờ hoặc Sạc. Sau phản hồi đầu tiên, cả ba thí nghiệm đều trở lại chính sách đã cho; chỉ hành động đầu tiên bị ấn định. Ở hàng Tìm, hai phản hồi của mô hình vẫn được giữ nguyên với xác suất $1/2$ mỗi nhánh; ấn định hành động không biến kết quả môi trường thành chắc chắn. Ấn định Tìm một lần vẫn có nghĩa dù chính sách không chọn Tìm ở L, vì thí nghiệm là một quy ước đánh giá, không phải mô tả hành vi thường ngày của chính sách. Mỗi thí nghiệm sinh một phân phối tổng thưởng với một kỳ vọng riêng.

### Giá trị hành động

Ấn định hành động đầu, rồi tiếp tục theo cùng chính sách:

$$q_\pi(s,a)=\mathbb E_\pi\!\left[G_t\mid S_t=s,\,A_t=a\right],
\qquad a\in\mathcal A(s).$$

So với $v_\pi(s)$, khác biệt duy nhất là cách xác định hành động đầu tiên: $v_\pi$ để chính sách chọn, $q_\pi$ ấn định hành động rồi để chính sách quyết định từ bước kế tiếp. Ký hiệu kỳ vọng điều kiện ở đây là quy ước của thí nghiệm, không phải phép chia cho $\Pr(A_t=a\mid S_t=s)$; do đó định nghĩa vẫn có nghĩa khi $\pi(a\mid s)=0$, chẳng hạn $q_\pi(\mathrm L,\mathrm{tim})$ dù $\pi(\mathrm{tim}\mid\mathrm L)=0$. Ngoài ra $q_\pi$ tính cả toàn bộ tương lai sau bước đầu, nên không đồng nhất với thưởng kỳ vọng tức thời $r(s,a)$. Phần 5 sẽ biểu diễn $v_\pi(s)$ bằng cách lấy trung bình các giá trị $q_\pi(s,a)$ theo xác suất chọn hành động.

::: exercise Câu hỏi kiểm tra

1. Thay cách chọn Chờ/Sạc ở L có làm thay đổi bảng $p$ không? Có thể làm thay đổi giá trị không?
2. $21/8$ vừa tính là kỳ vọng hai bước hay giá trị toàn tương lai?
3. Tính $q_\pi(\mathrm L,\mathrm{tim})$ nghĩa là buộc Tìm bao nhiêu lần trước khi trở lại $\pi$?
:::
::: solution
1. Bảng $p$ mô tả môi trường nên không đổi khi thay cách chọn hành động; nhưng phân phối quỹ đạo và giá trị có thể đổi, vì trọng số trên các nhánh phụ thuộc chính sách.
2. $21/8$ là kỳ vọng của đúng hai bước đầu, $G_0^{[2]}=R_1+\gamma R_2$, chưa phải giá trị toàn tương lai $v_\pi(\mathrm H)$.
3. Đúng một lần; sau phản hồi đầu tiên, thí nghiệm trở lại chính sách kể từ trạng thái kế tiếp, kể cả khi $\pi(\mathrm{tim}\mid\mathrm L)=0$. Đánh giá toàn bộ tương lai có thể dựa vào phần thưởng bước đầu và giá trị của trạng thái kế tiếp.
:::

<!-- note-topic-id: lec-03-part-05 -->
## 5. Phương trình Bellman

Định nghĩa kỳ vọng của tổng thưởng chiết khấu trên toàn tương lai chưa cho cách tính gọn: robot có thể tiếp tục hoạt động vô hạn. Ta thử nhóm các quỹ đạo theo bước đầu tiên, bắt đầu tại trạng thái pin thấp L. Mỗi nhóm gồm một phần thưởng ngay lập tức và một phần còn lại bắt đầu ở trạng thái kế tiếp; kỳ vọng của phần còn lại là $v_\pi$ tại trạng thái kế tiếp, dù giá trị số chưa biết. Nếu đẳng thức giữa giá trị và "thưởng ngay cộng giá trị phần còn lại" đúng cho mọi trạng thái, ta được một hệ phương trình thay vì một phép liệt kê vô hạn.

### Một bước từ pin thấp

Tại L, chính sách chọn Chờ hoặc Sạc mỗi $1/2$; $\gamma=1/2$.

![Từ L chọn Chờ với xác suất 1/2, nhận thưởng 1 và giữ L; hoặc Sạc với xác suất 1/2, nhận 0 rồi sang H; cả hai nhánh tiếp tục theo cùng chính sách](img/lec-03/robot-p05-low-battery-branches.svg)

$$\begin{aligned}
v_\pi(\mathrm L)&=\frac12\Bigl[1+\frac12 v_\pi(\mathrm L)\Bigr]\\
&\quad+\frac12\Bigl[0+\frac12 v_\pi(\mathrm H)\Bigr].
\end{aligned}$$

Ngoài ngoặc là xác suất hành động; trong ngoặc là thưởng ngay cộng phần tương lai chiết khấu. Nhánh Chờ: thưởng ngay $R_{t+1}=1$, pin giữ nguyên mức L nên phần còn lại chiết khấu là $\gamma v_\pi(\mathrm L)$. Nhánh Sạc: thưởng ngay $0$, pin lên H nên phần còn lại là $\gamma v_\pi(\mathrm H)$. Hai hệ số $1/2$ ngoài ngoặc đến từ $\pi(\mathrm{cho}\mid\mathrm L)=\pi(\mathrm{sac}\mid\mathrm L)=1/2$; hệ số $1/2$ trước $v_\pi$ là $\gamma$. Giá trị L xuất hiện ở cả hai vế vì Chờ giữ nguyên mức pin, nên đây là phương trình chứa ẩn ở hai vế; ta chưa giải nó.

### Tách phần thưởng tích lũy

::: derivation
$$\begin{aligned}
G_t&=R_{t+1}+\gamma R_{t+2}+\gamma^2 R_{t+3}+\cdots\\
&=R_{t+1}+\gamma\bigl(R_{t+2}+\gamma R_{t+3}+\cdots\bigr)\\
&=R_{t+1}+\gamma\, G_{t+1}.
\end{aligned}$$

Dòng 1 khai triển định nghĩa của $G_t$. Dòng 2 đặt $\gamma$ ra ngoài các số hạng từ bước thứ hai: $\gamma R_{t+2}+\gamma^2 R_{t+3}+\cdots=\gamma(R_{t+2}+\gamma R_{t+3}+\cdots)$. Dòng 3 nhận đúng tổng bắt đầu ở thời điểm $t+1$, tức $G_{t+1}$; số hạng đầu của $G_{t+1}$ là $R_{t+2}$, và sai số thường gặp là viết $G_{t+1}=R_{t+1}+\gamma R_{t+2}+\cdots$, lệch một chỉ số. Phép tách này thuần túy đại số trên một dãy thưởng đã cho: không dùng xác suất, không dùng chính sách, không dùng tính Markov. Lấy kỳ vọng giữ nguyên đẳng thức khi tổng khả tích.
:::

### Lấy trung bình theo hành động đầu

Các tổng theo $a$ chạy trên $\mathcal A(s)$; tổng theo $s'$ và $r$ chạy trên $\mathcal S$ và $\mathcal R$. Với bài có kết thúc, tổng trạng thái kế tiếp chạy trên $\mathcal S^+$ và giá trị tại trạng thái kết thúc bằng 0.

Từ định nghĩa giá trị và đẳng thức vừa chứng minh, tách kỳ vọng toàn phần theo hành động đầu:

$$\begin{aligned}
v_\pi(s)&=\mathbb E_\pi\bigl[R_{t+1}+\gamma G_{t+1}\mid S_t=s\bigr]\\
&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\\
&\quad\times\mathbb E_\pi\bigl[R_{t+1}+\gamma G_{t+1}\mid S_t=s,\,A_t=a\bigr].
\end{aligned}$$

Dấu bằng thứ hai là quy tắc kỳ vọng theo biến rời rạc $A_t$: kỳ vọng toàn phần thành tổng có trọng số $\pi(a\mid s)$; bên trong mỗi nhóm, mô hình vẫn ngẫu nhiên nên kỳ vọng chưa được tính. Đây là tầng kỳ vọng thứ nhất: trung bình theo hành động đầu, không phải chọn hành động có giá trị lớn nhất. Các hành động có trọng số $\pi(a\mid s)=0$ không đóng góp vào tổng, nhưng kỳ vọng sau hành động đó vẫn có định nghĩa riêng theo thí nghiệm hành động đầu đã ấn định. Trong ví dụ L, hai trọng số $1/2$ ngoài ngoặc chính là hai giá trị $\pi(a\mid s)$ đầu tiên của tổng này.

### Lấy trung bình theo phản hồi môi trường

Quy ước viết tắt: $s,a,s',r$ lần lượt là giá trị của $S_t,A_t,S_{t+1},R_{t+1}$. Ví dụ L–Tìm có hai cặp phản hồi $(\mathrm L,2)$ và $(\mathrm H,-3)$, mỗi cặp với xác suất $1/2$. Nhóm kỳ vọng theo cặp $(s',r)$:

$$\begin{aligned}
&\mathbb E_\pi\bigl[R_{t+1}+\gamma G_{t+1}\mid s,a\bigr]\\
&\quad=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma\,\mathbb E_\pi\bigl[G_{t+1}\mid s,a,s',r\bigr]\right].
\end{aligned}$$

Trong một nhóm, $R_{t+1}=r$ đã cố định nên $r$ ra khỏi kỳ vọng; tuyến tính đưa $\gamma$ ra ngoài. Ở ví dụ L–Tìm, tổng có hai số hạng:

$$\begin{aligned}
&\tfrac12\left[2+\gamma\,\mathbb E_\pi[G_{t+1}\mid \mathrm L,\mathrm{tim},\mathrm L,2]\right]\\
&\quad+\tfrac12\left[-3+\gamma\,\mathbb E_\pi[G_{t+1}\mid \mathrm L,\mathrm{tim},\mathrm H,-3]\right].
\end{aligned}$$

Chưa bỏ điều kiện $s,a,r$ trong kỳ vọng tương lai; chỉ các nhóm có xác suất dương cần kỳ vọng điều kiện riêng, còn nhóm xác suất 0 không cần điều kiện hóa. $p(s',r\mid s,a)$ là xác suất đồng thời của cặp $(s',r)$, không phải tích hai xác suất riêng; trọng số $\pi(a\mid s)\,p(s',r\mid s,a)$ là quy tắc nhân có điều kiện, không giả thiết độc lập giữa hành động và phản hồi.

### Từ trạng thái kế tiếp đến giá trị tương lai

Giả thiết: trạng thái Markov; chính sách chỉ phụ thuộc trạng thái; mô hình và chính sách không đổi theo thời gian.

::: derivation
$$\begin{aligned}
\mathbb E_\pi\bigl[G_{t+1}\mid s,a,s',r\bigr]
&=\mathbb E_\pi\bigl[G_{t+1}\mid S_{t+1}=s'\bigr]\\
&=v_\pi(s').
\end{aligned}$$

Dấu bằng thứ nhất là điểm duy nhất cần tính Markov, khác phép tách đại số của $G_t$: biết $s'$ đủ để mô tả phân phối tương lai khi các hành động sau đó theo cùng chính sách, nên điều kiện $s,a,r$ có thể bỏ. Dấu bằng thứ hai dùng tính dừng: mô hình và chính sách không đổi theo thời gian, nên kỳ vọng tương lai tại thời điểm $t+1$ dùng cùng hàm $v_\pi$ như tại thời điểm $t$. Khi $s'$ là trạng thái kết thúc, phần tương lai là 0 nên quy ước $v_\pi(s')=0$.
:::

Thế vào hai tầng trung bình:

$$\begin{aligned}
v_\pi(s)&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\\
&\quad\times\left[r+\gamma\, v_\pi(s')\right].
\end{aligned}$$

Đây là phương trình Bellman cho giá trị trạng thái. Kiểm tra bằng cây L: thay kỳ vọng tương lai bằng $v_\pi(\mathrm L)$ và $v_\pi(\mathrm H)$ ta nhận lại đúng hai ngoặc trong ví dụ pin thấp.

### Giá trị hành động từ phản hồi một bước

Ấn định Tìm tại L; hai phản hồi có xác suất $1/2$:

$$q_\pi(\mathrm L,\mathrm{tim})=\tfrac12\Bigl[2+\tfrac12 v_\pi(\mathrm L)\Bigr]+\tfrac12\Bigl[-3+\tfrac12 v_\pi(\mathrm H)\Bigr].$$

Áp dụng cùng cách tách với hành động đầu đã ấn định:

$$\begin{aligned}
q_\pi(s,a)&=\mathbb E_\pi\bigl[R_{t+1}+\gamma G_{t+1}\mid s,a\bigr]\\
&=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma\, v_\pi(s')\right].
\end{aligned}$$

Ở đây $v_\pi(s')$ đã lấy trung bình theo cùng chính sách từ $s'$, nên dạng $q$ theo $v$ không cần viết thêm tổng hành động tương lai.

Không nhân thêm $\pi(a\mid s)$ ở bước đầu vì $a$ đã được chọn; hệ số $1/2$ trong công thức ví dụ là xác suất của cặp phản hồi, không phải của hành động. Chính sách vẫn quyết định phần tương lai thông qua $v_\pi$: nếu sau đó chính sách đổi, $v_\pi(\mathrm L)$ và $v_\pi(\mathrm H)$ có thể đổi theo. Công thức tổng quát đúng cho mọi cặp hợp lệ $(s,a)$, kể cả khi $\pi(a\mid s)=0$.

### Giá trị trạng thái từ các giá trị hành động

Tại L, chính sách chọn hai hành động Chờ và Sạc, mỗi hành động với xác suất $1/2$:

$$v_\pi(\mathrm L)=\tfrac12\,q_\pi(\mathrm L,\mathrm{cho})+\tfrac12\,q_\pi(\mathrm L,\mathrm{sac}).$$

Viết lại bước kỳ vọng theo hành động đầu:

$$\begin{aligned}
v_\pi(s)&=\sum_a\pi(a\mid s)\,\mathbb E_\pi\bigl[G_t\mid s,a\bigr]\\
&=\sum_a\pi(a\mid s)\,q_\pi(s,a),
\end{aligned}$$

vì kỳ vọng có điều kiện $\mathbb E_\pi[G_t\mid s,a]$ chính là định nghĩa của $q_\pi(s,a)$. Tìm không đóng góp vào $v_\pi(\mathrm L)$ của chính sách này vì trọng số $\pi(\mathrm{tim}\mid\mathrm L)=0$, nhưng $q_\pi(\mathrm L,\mathrm{tim})$ vẫn được định nghĩa đầy đủ. Quan hệ $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$ đúng tại mọi trạng thái, nên có thể áp dụng nó tại trạng thái kế tiếp $s'$ để thay phần tương lai trong phương trình của $q$.

### Bellman kỳ vọng cho giá trị hành động

Tại $s'$, hành động được chọn ở thời điểm $t+1$ là $a'$, nên

$$v_\pi(s')=\sum_{a'\in\mathcal A(s')}\pi(a'\mid s')\,q_\pi(s',a').$$

Thế vào phương trình của $q_\pi$:

$$\begin{aligned}
q_\pi(s,a)&=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma\, v_\pi(s')\right]\\
&=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma\sum_{a'}\pi(a'\mid s')\,q_\pi(s',a')\right].
\end{aligned}$$

Nguồn: Sutton và Barto, ấn bản 2, bài tập 3.17, tr. 61.

$a$ là hành động đã thực hiện ở thời điểm $t$; $a'$ là hành động được chọn ở thời điểm $t+1$ tại $s'$, vì vậy dùng $\pi(a'\mid s')$. Chỉ có một hệ số $\gamma$ vì từ $t$ sang $t+1$ mới qua một bước; tổng ngoài mang xác suất phản hồi $p$, tổng trong mang xác suất chính sách $\pi$. Phép thế là thay $v_\pi(s')$ bằng trung bình có trọng số của các $q_\pi(s',a')$ ngay tại chỗ, không nhân thêm hệ số nào khác. Với trạng thái kết thúc, toàn bộ giá trị tương lai bằng 0 và không yêu cầu hành động tiếp theo thực tế.

::: exercise Câu hỏi kiểm tra

1. Số hạng đầu của $G_{t+1}$ là gì? Vì sao phép tách $G_t$ chưa cần Markov?
2. Ở bước nào trong suy diễn Bellman mới dùng tính Markov và chính sách dừng?
3. Trong $v_\pi(s)$, trọng số $\pi(a\mid s)\,p(s',r\mid s,a)$ mô tả điều gì? Vì sao phương trình của $q_\pi(s,a)$ không lấy trung bình hành động đầu lần nữa?
:::
::: solution
1. Số hạng đầu của $G_{t+1}$ là $R_{t+2}$; phép tách là đại số trên một dãy thưởng đã cho, không dùng xác suất hay giả thiết Markov.
2. Tính Markov và chính sách dừng được dùng khi thay kỳ vọng phần tương lai đã điều kiện hóa bằng $v_\pi(s')$, tức ở bước nhận diện $\mathbb E_\pi[G_{t+1}\mid s,a,s',r]=v_\pi(s')$.
3. Trọng số mô tả xác suất chọn hành động rồi nhận cặp phản hồi; đây là quy tắc nhân có điều kiện, không giả thiết độc lập giữa hành động và phản hồi. Với $q_\pi(s,a)$, hành động đầu đã được ấn định nên không lấy trung bình theo nó lần nữa. Các phương trình vẫn chứa giá trị chưa biết ở cả hai vế; với robot hai trạng thái, cần giải chúng đồng thời.
:::

<!-- note-topic-id: lec-03-part-06 -->
## 6. Đánh giá một chính sách từ mô hình

Mô hình phản hồi, chính sách và hệ số chiết khấu đã được xác định. Bài toán đánh giá chính sách cần tìm hai giá trị $v_\pi(\mathrm H)$ và $v_\pi(\mathrm L)$, giữ nguyên chính sách ở phần 4. Phương trình Bellman cho mỗi trạng thái tạo thành một hệ hai phương trình hai ẩn.

### Hệ Bellman của robot

Đặt $v_H=v_\pi(\mathrm H)$, $v_L=v_\pi(\mathrm L)$. Tại H luôn chọn Tìm; tại L chính sách chia đều Chờ và Sạc:

$$\begin{aligned}
v_H&=2+\frac12\left(\frac12v_H+\frac12v_L\right),\\[4pt]
v_L&=\frac12\left(1+\frac12v_L\right)+\frac12\left(0+\frac12v_H\right).
\end{aligned}$$

Phương trình thứ nhất đọc từ cây H: hành động Tìm có xác suất 1 theo chính sách, nhưng môi trường chia hai kết quả: về H hoặc về L, mỗi nhánh xác suất 1/2, thưởng 2. Phương trình thứ hai đọc từ cây L: chính sách chia hai hành động Chờ và Sạc, mỗi hành động xác suất 1/2; Chờ về L với thưởng 1, Sạc về H với thưởng 0, mỗi nhánh chuyển chắc chắn. Ở phương trình H, các hệ số $1/2$ trong ngoặc là xác suất chuyển và hệ số ngoài ngoặc là chiết khấu. Ở phương trình L, các hệ số ngoài ngoặc là xác suất hành động; hệ số trước mỗi giá trị tương lai là chiết khấu. Cả hai phương trình chứa cùng hai ẩn, nên hệ phải giải đồng thời. Thưởng 1 khi Chờ là thưởng một bước; $v_L$ còn tính cả phần tương lai đã chiết khấu.

### Giải hai phương trình giá trị

::: derivation
Khai triển hệ:

$$\begin{aligned}
v_H&=2+\tfrac14v_H+\tfrac14v_L,\\
v_L&=\tfrac12+\tfrac14v_H+\tfrac14v_L.
\end{aligned}$$

Ở phương trình H, $\gamma\cdot(1/2)=1/4$ cho từng nhánh; ở phương trình L, mỗi hành động có xác suất 1/2 và $\gamma=1/2$ nên cụm tương lai cũng có hệ số 1/4 cho mỗi trạng thái. Hai phương trình có cùng hệ số phần tương lai, nên trừ trực tiếp:

$$v_H-v_L=\tfrac32\quad\Rightarrow\quad v_H=v_L+\tfrac32.$$

Thế vào phương trình L:

$$v_L=\tfrac12+\tfrac14\left(v_L+\tfrac32\right)+\tfrac14v_L=\tfrac78+\tfrac12v_L,$$

suy ra $v_L=\tfrac74$ và $v_H=\tfrac{13}{4}$.
:::

Kiểm lại cả hai: $13/4=2+(1/4)(13/4+7/4)$ và $7/4=1/2+(1/4)(13/4+7/4)$, cả hai đúng. $13/4$ là giá trị toàn tương lai theo Bellman. $21/8$ chỉ là kỳ vọng của hai bước đầu từ H.

### Kiểm tra giá trị bằng các hành động

Từ hạt nhân chung, cộng các mức thưởng:

$$q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s').$$

Thay giá trị trạng thái vừa giải:

$$\begin{aligned}
q_\pi(\mathrm L,\mathrm{cho})&=1+\frac12\cdot\frac74=\frac{15}{8},\\
q_\pi(\mathrm L,\mathrm{sac})&=0+\frac12\cdot\frac{13}{4}=\frac{13}{8}.
\end{aligned}$$

Trung bình theo chính sách tại L, hai hành động mỗi cái xác suất 1/2:

$$v_\pi(\mathrm L)=\frac12\cdot\frac{15}{8}+\frac12\cdot\frac{13}{8}=\frac74.\;\checkmark$$

Kết quả trùng với $v_L$ vừa giải. Chờ một lần có giá trị cao hơn Sạc một lần khi cùng tiếp tục theo $\pi$, nhưng so sánh này chưa chứng minh chính sách tối ưu: phần tiếp diễn vẫn là chính sách đã cho. Vì cả hai hành động đều dẫn tới trạng thái kế tiếp chắc chắn, có thể gộp luôn các nhánh hành động và tính trực tiếp từ trạng thái sang trạng thái.

### Gộp các nhánh dưới chính sách

Cùng hệ Bellman đã giải có thể viết gọn bằng xác suất chuyển giữa các trạng thái và thưởng trung bình sau khi lấy trung bình theo quy tắc chọn hành động.

Tại H, Tìm chia hai kết quả về H hoặc về L, mỗi nhánh xác suất 1/2, thưởng 2, nên thưởng trung bình một bước là 2. Tại L, Chờ về L với xác suất 1/2 và thưởng 1, Sạc về H với xác suất 1/2 và thưởng 0, nên thưởng trung bình là $\tfrac12\cdot1+\tfrac12\cdot0=\tfrac12$.

| Hiện tại | Kế tiếp H | Kế tiếp L | Thưởng trung bình một bước |
|---|---|---|---|
| H | $1/2$ | $1/2$ | $2$ |
| L | $1/2$ | $1/2$ | $1/2$ |

Con số 1/2 ở cột Thưởng trung bình của hàng L là kỳ vọng thưởng của trạng thái, không phải thưởng thực tế của một nhánh cụ thể. Sau khi gộp, chính sách đã được lấy trung bình vào các trọng số, nhưng tính ngẫu nhiên của môi trường vẫn còn. Bảng này phụ thuộc chính sách cụ thể đang dùng; đổi chính sách thì tính lại. Việc chỉ còn trạng thái và chuyển tiếp dẫn đến tên gọi chuỗi Markov; giữ thêm thưởng thì được quá trình phần thưởng Markov.

### Chuỗi Markov và MRP dưới chính sách

Hai công thức chỉ lấy trung bình những đại lượng đã định nghĩa ở phần mô hình:

$$\begin{aligned}
P^\pi_{ss'}&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,p(s'\mid s,a),\\
r^\pi(s)&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,r(s,a).
\end{aligned}$$

$P^\pi_{ss'}$ cộng theo mọi hành động $a$ tại $s$, mỗi hành động với trọng số $\pi(a\mid s)$; $r^\pi(s)$ lấy trung bình thưởng kỳ vọng $r(s,a)$ cùng trọng số đó. Kiểm bằng hàng L của bảng đã gộp: $P^\pi_{LH}=P^\pi_{LL}=1/2$ và $r^\pi(L)=1/2$, đúng như bảng.

- Chuỗi Markov: cặp $(\mathcal S,P^\pi)$, trong đó phân phối trạng thái kế tiếp chỉ phụ thuộc trạng thái hiện tại.
- Quá trình phần thưởng Markov (MRP): bộ $(\mathcal S,P^\pi,r^\pi,\gamma)$.

Chính sách Markov dừng, sau khi gộp, làm phân phối phản hồi chỉ phụ thuộc trạng thái hiện tại, nên quá trình trạng thái vẫn Markov. $r^\pi$ chỉ lưu kỳ vọng thưởng cần cho bài toán giá trị, không mô tả đầy đủ phân phối thưởng; $\gamma$ nằm ngoài $r^\pi$, chỉ xuất hiện trong bộ MRP. Chuỗi Markov và MRP không có một quyết định hành động mới nào ngoài chính sách đã gộp. Phương trình Bellman của MRP chính là hệ hai phương trình đã giải ở trên.

### Bellman dưới dạng ma trận

Với $n$ trạng thái: $v,\,r^\pi\in\mathbb R^n$ là véc-tơ cột, $P^\pi\in\mathbb R^{n\times n}$, $I$ là ma trận đơn vị. Gộp hai nhóm số hạng trong Bellman:

$$v=r^\pi+\gamma P^\pi v
\quad\Longleftrightarrow\quad
(I-\gamma P^\pi)v=r^\pi.$$

Phép nhân $P^\pi v$ là các tổng có trọng số vừa học, không thêm quy tắc cập nhật mới. Với robot, chọn thứ tự trạng thái H, L:

$$P^\pi=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\qquad r^\pi=\begin{pmatrix}2\\1/2\end{pmatrix}.$$

Hàng đầu của ma trận hệ số, $3/4$ và $-1/4$, chính là phương trình H ở dạng $v_H-(1/4)v_H-(1/4)v_L=2$; hàng hai là phương trình L:

$$\begin{pmatrix}3/4&-1/4\\-1/4&3/4\end{pmatrix}
\begin{pmatrix}v_H\\v_L\end{pmatrix}
=\begin{pmatrix}2\\1/2\end{pmatrix}.$$

::: proof Tồn tại và duy nhất khi chiết khấu nhỏ hơn 1
Với véc-tơ $x$, đặt $\|x\|_\infty=\max_i|x_i|$. Với ma trận $B$, chuẩn tương ứng là $\|B\|_\infty=\max_i\sum_j|B_{ij}|$.

Ma trận $P^\pi$ có các phần tử không âm và tổng mỗi hàng bằng 1, nên $\|P^\pi\|_\infty=1$. Giả sử $0\le\gamma<1$.

*Tồn tại:* khai triển Neumann $v=\sum_{k\ge0}\gamma^k(P^\pi)^k r^\pi$ hội tụ vì $\|\gamma P^\pi\|_\infty=\gamma<1$; thay vào phương trình cho $v=r^\pi+\gamma P^\pi v$, nên nghiệm tồn tại.

*Duy nhất:* nếu có hai nghiệm $v,w$ thì

$$\|v-w\|_\infty=\|\gamma P^\pi(v-w)\|_\infty\le\gamma\|v-w\|_\infty,$$

vì phép nhân $P^\pi$ không làm tăng chuẩn vô cùng của véc-tơ; với $\gamma<1$, bất đẳng thức chỉ xảy ra khi $v=w$. Hệ số $\gamma<1$ mới tạo tính co; điều này không cho phép kết luận không điều kiện khi $\gamma=1$.
:::

Với ma trận đặc, giải hệ trực tiếp thường tốn $O(n^3)$ phép tính. Các phương pháp lặp để xử lý bài toán lớn hơn được học ở Bài 04.

::: exercise Câu hỏi kiểm tra

Cho lại $v_H=\tfrac{13}{4}$, $v_L=\tfrac{7}{4}$, $\gamma=\tfrac12$; hai nhánh L–Tìm: về L thưởng $2$ (xác suất $1/2$), về H thưởng $-3$ (xác suất $1/2$); chính sách tại L chia đều Chờ/Sạc; Chờ chắc chắn cho $(\mathrm L,1)$, Sạc cho $(\mathrm H,0)$.

1. Tính $q_\pi(\mathrm L,\mathrm{tim})$, dù chính sách đang dùng không chọn hành động đó tại L.
2. Từ bảng chính sách, tính hàng chuyển và thưởng trung bình của trạng thái L.
3. Nếu đổi chính sách, những đại lượng nào trong $p,\;P^\pi,\;r^\pi,\;v_\pi$ cần tính lại?
:::

::: solution
1. $q_\pi(\mathrm L,\mathrm{tim})=\tfrac12\left(2+\tfrac12\cdot\tfrac74\right)+\tfrac12\left(-3+\tfrac12\cdot\tfrac{13}{4}\right)=\tfrac12\cdot\tfrac{23}{8}+\tfrac12\cdot\left(-\tfrac{11}{8}\right)=\tfrac34$. Giá trị hành động được xác định đầy đủ bởi mô hình và $v$, kể cả khi $\pi(\mathrm{tim}\mid\mathrm L)=0$; hành động đầu bị ép bởi dữ kiện hai nhánh L–Tìm, còn chính sách ở các bước sau vẫn ảnh hưởng tới $q$ qua $v$.
2. Hàng L của $P^\pi$ là $(1/2,\,1/2)$ vì Chờ về L và Sạc về H, mỗi hành động xác suất 1/2; thưởng trung bình $r^\pi(L)=(1/2)\cdot1+(1/2)\cdot0=1/2$.
3. Giữ nguyên mô hình $p$ vì nó thuộc môi trường; phải tính lại $P^\pi$, $r^\pi$ và do đó $v_\pi$. Các giá trị có thể trùng hợp sau khi đổi chính sách, nhưng vẫn cần xét lại ba đại lượng phụ thuộc chính sách này.
:::

<!-- note-topic-id: lec-03-part-07 -->
## 7. Tổng hợp và vận dụng

Đầu bài, robot ở L chỉ cho ta biết các lựa chọn và tác động tức thời lên pin. Sau sáu phần, mỗi lựa chọn có thêm một con số: giá trị dài hạn khi thực hiện hành động đó trước rồi tiếp tục theo $\pi$. Ba giá trị hành động tại L là:

$$q_\pi(\mathrm L,\mathrm{tim})=\frac34,\qquad
q_\pi(\mathrm L,\mathrm{cho})=\frac{15}{8},\qquad
q_\pi(\mathrm L,\mathrm{sac})=\frac{13}{8}.$$

![Robot ở trạng thái pin thấp với ba nhánh hành động và ba giá trị hành động tương ứng](img/lec-03/robot-p07-three-actions-values.svg)

Ba giá trị này là kết quả của ví dụ xuyên suốt, không phải số liệu thực nghiệm trong sách. Giá trị $15/8$ được tính từ xác suất phản hồi, phần thưởng và giá trị trạng thái kế tiếp. Mô hình, chính sách và giá trị là ba đối tượng khác nhau; nhầm lẫn giữa chúng là lỗi thường gặp khi lập hệ phương trình.

### Đọc một quyết định bằng mô hình và giá trị

Xét nhánh L–Chờ: môi trường cho $p(\mathrm L,1\mid\mathrm L,\mathrm{cho})=1$: chỉ một cặp trạng thái–thưởng xảy ra, trở về chính L với $v_\pi(\mathrm L)=7/4$ và $\gamma=1/2$. Đối chiếu từng thành phần với công thức tổng quát:

$$q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)\left[r+\gamma v_\pi(s')\right].$$

Tổng chỉ còn một số hạng, nên

$$q_\pi(\mathrm L,\mathrm{cho}) = 1 + \frac12\cdot\frac74 = \frac{15}{8}.$$

Hai xác suất khác bản chất cần phân biệt: $\pi(\mathrm{cho}\mid\mathrm L)=1/2$ là xác suất chính sách chọn hành động; $p=1$ là xác suất phản hồi của môi trường khi hành động đã ấn định. Khi đánh giá một hành động cụ thể, không nhân $q$ với $1/2$; trọng số chính sách chỉ dùng lúc ghép các $q$ thành $v_\pi(\mathrm L)=\tfrac12\cdot\tfrac{15}{8}+\tfrac12\cdot\tfrac{13}{8}=\tfrac74$. Lỗi phổ biến là nhân thêm $1/2$ hoặc quên $\gamma$.

### Bài tập và bước tiếp theo

| Bài (hw02) | Nhiệm vụ | Kết quả cần viết |
|---|---|---|
| 3 | Kiểm tra ma trận ba trạng thái và lập Bellman | Hàng xác suất hợp lệ; hệ ba phương trình |
| 4 | Cố định chính sách, gộp MDP thành MRP | Công thức $P^\pi, r^\pi$ và giải thích phép trung bình |
| 7 | Nối $q$ với $v$ | Công thức trung bình theo chính sách |
| 8 | Giải thích Bellman cho $v_\pi$ | Ý nghĩa từng thành phần của phương trình giá trị |

Bài 3 và 4 dùng kết quả về ma trận chuyển và MRP ở phần 6. Bài 7 và 8 dùng các suy diễn giá trị ở phần 5. Bài 10 là bài tự luyện mô hình hóa, không bắt buộc. Bài 04 sẽ nghiên cứu cách tìm chính sách tốt hơn khi biết mô hình.

::: exercise Câu hỏi kiểm tra

1. Biết $p(s'\mid s,a)$, chính sách và hệ số chiết khấu đã đủ để tính giá trị trạng thái $v_\pi(s)$ chưa? Còn thiếu dữ kiện nào?
2. Một quỹ đạo có tổng thưởng khác $v_\pi(s)$ có mâu thuẫn với định nghĩa giá trị không?
3. $q_\pi(\mathrm L,\mathrm{cho})>q_\pi(\mathrm L,\mathrm{sac})$ đã chứng minh chính sách đang dùng là tối ưu chưa?
:::

::: solution
1. Chưa đủ. Với xác suất chuyển, chính sách và hệ số chiết khấu đã cho, cần thêm thưởng kỳ vọng $r(s,a)$ để viết Bellman. Có thể dùng hạt nhân chung $p(s',r\mid s,a)$ để cung cấp cả chuyển trạng thái và thưởng; chỉ có xác suất chuyển không cho biết phần thưởng kỳ vọng.
2. Không mâu thuẫn. Một tổng thưởng là kết quả của một quỹ đạo cụ thể; $v_\pi(s)$ là kỳ vọng trên mọi quỹ đạo, nên từng quỹ đạo có thể lệch khỏi giá trị.
3. Chưa. Phép so sánh chỉ xét hành động đầu rồi tiếp tục theo chính sách đã cho; nó không loại trừ việc thay đổi cả phần tiếp diễn. Bài 04 sẽ nghiên cứu việc thay đổi chính sách và mục tiêu tối ưu.
:::

### Tài liệu đọc

- R. S. Sutton và A. G. Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018, chương 3, §3.1–3.5, ví dụ 3.3, tr. 52–53; phương trình (3.2)–(3.5), (3.7)–(3.14); bài tập 3.12–3.13, 3.17–3.19 (Bellman cho $q$ là bài tập 3.17).
- Tạ Việt Cường, *Bài tập tuần 2 — MDP*, ngày 12/3/2026, bài 3, 4, 7, 8; bài 10 tùy chọn.

Ví dụ robot phỏng theo Sutton và Barto, ví dụ 3.3. Các xác suất $1/2$, mức thưởng Tìm bằng 2, Chờ bằng 1 và chính sách dùng để tính giá trị được chọn cho bài giảng. Sách mô tả thưởng kỳ vọng trên nhánh; bài giảng giả sử thưởng cố định trên từng nhánh để xác định đầy đủ phân phối chung.
