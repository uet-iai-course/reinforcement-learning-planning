# Bài 02 — Giao diện tác tử–môi trường

Học tăng cường · Học kỳ 1, 2026–2027 · Trường Đại học Công nghệ · Đại học Quốc gia Hà Nội

<!-- note-topic-id: lec-02-part-01 -->

## 1. Bài toán ra quyết định tuần tự

Trong bài toán ra quyết định tuần tự, kết quả của hành động hiện tại ảnh hưởng đến những quyết định về sau.

### Mê cung và chuỗi quyết định

![Mê cung nguồn: lưới 8×8, các ô tô đậm là tường, điểm bắt đầu tại cột 0 hàng 2 (đánh dấu S), đích G nằm ngoài lưới bên phải, sau ô (7,6), với một lối đi từ S qua các ô trống tới G.](img/lec-02/source-maze.svg)

Nhiệm vụ là đi từ điểm bắt đầu tới đích. Một bước đi hợp lệ thay đổi vị trí và đường đi còn lại; nếu bước đi gặp tường thì tác tử đứng yên. Điểm bắt đầu nằm ở mép trái, tại cột 0 và hàng 2, với tọa độ đánh từ 0, hàng tăng xuống dưới. Đích nằm ngoài lưới bên phải, sau ô $(7,6)$, tại tọa độ $G=(8,6)$. Các ô tô đậm là tường. Ở mỗi bước tác tử chọn một trong bốn hướng Bắc, Đông, Nam, Tây; chọn hướng có tường hoặc ra ngoài biên thì đứng yên, trừ bước đi vào đích. Một hướng đi có thể dẫn vào ngõ cụt và buộc tác tử quay lại. Muốn đánh giá một lựa chọn, ta cần xét cả phần đường còn lại, vì vị trí mới quy định các chuyển tiếp có thể ở bước tiếp theo.

### Mục tiêu và kiến thức tiên quyết

Sau bài học, người học cần đạt ba mục tiêu: mô tả một bước tương tác giữa tác tử và môi trường bằng các tín hiệu quan sát, hành động và phần thưởng; phân biệt trạng thái của môi trường với thông tin quan sát mà tác tử nhận được; trình bày được vai trò của hàm giá trị và mô hình môi trường trong việc đánh giá và dự báo kết quả dài hạn.

Kiến thức tiên quyết gồm xác suất có điều kiện, kỳ vọng của một biến ngẫu nhiên và khái niệm tổng hữu hạn khi cộng một chuỗi phần thưởng.

### Nội dung bài học

Bài học gồm bảy phần:

1. Bài toán ra quyết định tuần tự
2. Tương tác và phần thưởng
3. Trạng thái và thông tin quan sát
4. Chính sách lựa chọn hành động
5. Hàm giá trị và mô hình môi trường
6. Phần thưởng định hướng hành vi
7. Tổng kết và tự kiểm tra

::: exercise Câu hỏi kiểm tra
1. Trong mê cung, mỗi bước tác tử chọn điều gì để di chuyển?

2. Hành động hiện tại ảnh hưởng đến lựa chọn về sau ra sao?

3. Nêu một tiêu chí để so sánh hai đường đi tới cùng đích.
:::

::: solution
1. Tác tử chọn một trong bốn hướng Bắc, Đông, Nam, Tây; chọn hướng có tường thì đứng yên.

2. Vị trí mới quy định các chuyển tiếp có thể ở bước tiếp theo.

3. Có thể dùng số bước khi mục tiêu là tới đích bằng ít bước nhất.
:::

<!-- note-topic-id: lec-02-part-02 -->

## 2. Tương tác và phần thưởng

### Tác tử và môi trường

Tác tử là bộ phận chọn hành động; môi trường nhận hành động, thay đổi tình huống và cung cấp phản hồi. Ví dụ: bộ điều khiển robot chọn tín hiệu điều khiển, còn cơ cấu cơ học và thế giới bên ngoài thuộc môi trường, trả về vị trí và lực đo được. Ranh giới giữa tác tử và môi trường phải được dùng nhất quán khi mô tả bài toán.

### Một bước tương tác

Xét một bước trong mê cung: tại $(0,2)$, tác tử quan sát tọa độ rồi chọn hướng Đông; môi trường chuyển tác tử sang $(1,2)$, trả phần thưởng $-1$ và tọa độ mới. Quan sát mô tả thông tin nhận được; phần thưởng đánh giá kết quả theo mục tiêu đã đặt. Hai tín hiệu có vai trò khác nhau.

Thứ tự tương tác: $t=0,1,2,\ldots$ đánh số bước tương tác. $O_t\in\mathcal O$ là quan sát, $A_t\in\mathcal A$ là hành động, $R_{t+1}\in\mathbb R$ là phần thưởng sau $A_t$. Tại bước $t$, tác tử có quan sát $O_t$ và chọn $A_t$; phản hồi của hành động đó là cặp $(O_{t+1},R_{t+1})$. Tập $\mathcal O$ chứa các quan sát có thể nhận, $\mathcal A$ chứa các hành động. Trong mê cung, quan sát là tọa độ và hành động là một trong bốn hướng.

![Dòng thời gian tương tác: tại mỗi mốc thời gian tác tử nhận quan sát rồi chọn hành động; sau hành động môi trường trả về phần thưởng và quan sát mới, nối tiếp qua các mốc thời gian liên tiếp.](img/lec-02/interaction-timeline.svg)

### Tín hiệu học

| Khung | Tín hiệu | Thời điểm |
| --- | --- | --- |
| Có giám sát | Nhãn đúng cho mỗi mẫu | Tại lúc học |
| Không giám sát | Không có nhãn | — |
| Tăng cường | Phần thưởng mỗi bước | Sau hành động |

Học có giám sát dùng nhãn mục tiêu gắn với mẫu; học không giám sát tìm cấu trúc khi không có nhãn mục tiêu; trong học tăng cường, phần thưởng được nhận qua tương tác. Phần thưởng không cho biết hành động đúng hay sai mà chỉ chấm điểm, và có thể được nhận ngay sau mỗi bước. Thưởng $-1$ sau một bước đi không chỉ ra hướng nào nên chọn; hành động còn thay đổi vị trí và dữ liệu mà tác tử sẽ gặp ở các bước tiếp theo.

### Giả thuyết điểm thưởng

Giả thuyết điểm thưởng nêu rằng mọi mục tiêu có thể được mô tả bằng việc cực đại hóa kỳ vọng của phần thưởng tích lũy. Đây là một giả thuyết mô hình hóa, không phải định lý về mọi mục tiêu. Mục tiêu xét cả chuỗi phần thưởng, không chỉ phần thưởng ở bước hiện tại; kỳ vọng tính đến sự ngẫu nhiên của hành động và môi trường. Trong mê cung, thưởng $-1$ mỗi bước và dừng ở đích khiến đường đi ngắn hơn có tổng thưởng lớn hơn: mỗi đường đi hữu hạn nhận tổng thưởng bằng âm số bước, ví dụ một đường 16 bước cho $-16$ và một đường 18 bước cho $-18$. Cách gán thưởng cần phản ánh đúng mục tiêu của nhiệm vụ.

### Phản hồi trễ

Một ví dụ khác là trò chơi với ba kết quả: thắng, thua hoặc hòa. Các bước chưa kết thúc nhận thưởng $0$; khi kết thúc, thắng nhận $1$, thua nhận $-1$ và hòa nhận $0$. Chuỗi thưởng $0,\ldots,0,1$ minh họa một lượt thắng. Một hành động chưa nhận thưởng dương vẫn có thể góp phần dẫn tới kết quả xuất hiện nhiều bước sau. Trong mê cung, thưởng $-1$ được nhận ngay mỗi bước; phản hồi trễ không có nghĩa mọi phần thưởng đều chỉ xuất hiện khi kết thúc.

::: exercise Câu hỏi kiểm tra
1. Từ $(1,2)$ chọn Bắc đến $(1,1)$, thưởng $-1$, quan sát là tọa độ. Hãy ghi $A_t$, $R_{t+1}$, $O_{t+1}$.

2. Giả thuyết điểm thưởng nêu tiêu chí tối ưu nào cho tác tử?

3. Nhận $-1$ ngay có đủ để đánh giá hành động Bắc hay không?
:::

::: solution
1. $A_t$ là Bắc, $R_{t+1}=-1$, $O_{t+1}$ là tọa độ $(1,1)$.

2. Cực đại kỳ vọng phần thưởng tích lũy theo thời gian.

3. Chưa, vì hậu quả dài hạn của hành động chưa được xét.
:::

<!-- note-topic-id: lec-02-part-03 -->

## 3. Trạng thái và thông tin quan sát

### Trạng thái, quan sát và biểu diễn

Một tác tử đứng ở ô $(2,1)$ trong mê cung cố định. Cảm biến của tác tử không thấy toàn bộ bản đồ mà chỉ báo về bốn ô kề: phía Bắc là tường, phía Nam là tường, phía Đông và phía Tây là ô trống. Mã hóa bốn chỉ báo này theo thứ tự Bắc–Đông–Nam–Tây với 1 là tường và 0 là ô trống, ta nhận được bộ giá trị $(1,0,1,0)$. Ô $(3,1)$ cho cùng bốn chỉ báo, nên bộ mã này không đủ để suy ra vị trí thực: hai vị trí khác nhau có thể chia sẻ cùng một dữ liệu cảm biến.

![Ba lớp thông tin: trạng thái là vị trí (2,1) trên bản đồ, quan sát là bốn ô kề theo thứ tự Bắc–Đông–Nam–Tây, và biểu diễn nhị phân (1,0,1,0); vị trí (3,1) cho cùng quan sát và biểu diễn.](img/lec-02/state-observation-representation.svg)

Trạng thái $S_t\in\mathcal S$ là cấu hình môi trường mà mô hình đã chọn để mô tả tình huống; trong mê cung này, trạng thái là tọa độ ô, kể cả đích $G$. Quan sát $O_t\in\mathcal O$ là thông tin mà tác tử thực sự nhận được; trong ví dụ, đó là bốn chỉ báo kề. Biểu diễn $X_t\in\mathcal X$ là dữ liệu tác tử dùng để chọn hành động; ở đây là bộ mã nhị phân. Ba tập $\mathcal S$, $\mathcal O$, $\mathcal X$ lần lượt là miền trạng thái, miền quan sát và miền biểu diễn. Trạng thái là lựa chọn của người xây dựng mô hình: cùng một môi trường có thể được mô tả bằng các trạng thái khác nhau, và một mô tả có thể bỏ sót thông tin ảnh hưởng đến diễn biến tiếp theo.

Biểu diễn được tính từ thông tin khả dụng trước khi chọn hành động:

$$X_t = f_t\!\left(O_{0:t},\, A_{0:t-1},\, R_{1:t}\right)$$

với $O_{0:t}=(O_0,\ldots,O_t)$; các dãy hành động và phần thưởng viết tương tự. Chính thức,

$$f_t:\mathcal O^{t+1}\times\mathcal A^{t}\times\mathbb R^{t}\to\mathcal X$$

là hàm mã hóa tất định do tác tử chọn. Thứ tự thời gian: tại $t$, tác tử tính $X_t$ từ dữ liệu có trước khi chọn $A_t$; hành động và phần thưởng tương lai chưa được nhìn thấy. Tại $t=0$, dãy hành động và phần thưởng đều rỗng. Trường hợp đơn giản là $f_t$ chỉ phụ thuộc quan sát hiện tại, như mã hóa nhị phân bốn ô kề; trường hợp tổng quát là hàm của toàn bộ lịch sử. Quan sát có thể ngẫu nhiên, không đầy đủ; $X_t$ không bảo đảm khôi phục được $S_t$.

### Mẫu dữ liệu, lịch sử và quỹ đạo

Một mẫu dữ liệu một bước là $(o_t,a_t,o_{t+1},r_{t+1})$, với chữ thường chỉ giá trị cụ thể của các biến viết hoa; quan sát mới và phần thưởng đều đến sau hành động. Lịch sử trạng thái tới thời điểm $t$:

$$H_t=(S_0,A_0,R_1,S_1,\ldots,A_{t-1},R_t,S_t),$$

kết thúc ở trạng thái hiện tại, trước khi chọn hành động tiếp theo, với $H_0=(S_0)$. Quỹ đạo là toàn bộ một lượt tương tác hữu hạn kết thúc tại $T$, với $T$ là thời điểm dừng:

$$\tau=(S_0,A_0,R_1,S_1,\ldots,A_{T-1},R_T,S_T)=H_T.$$

Mẫu dùng quan sát, còn lịch sử và quỹ đạo ở đây dùng trạng thái môi trường; khi quan sát một phần, tác tử không nhất thiết biết chuỗi trạng thái này. Lịch sử thông tin tác tử nhận dùng trong $f_t$ khác với lịch sử trạng thái của môi trường.

### Quan sát đầy đủ và một phần

Quan sát đầy đủ là trường hợp từ quan sát hiện tại $O_t$ xác định được $S_t$, không cần thêm thông tin từ lịch sử; với quan sát một phần, một $O_t$ có thể phù hợp với nhiều $S_t$. Trong mê cung đã xét với bản đồ và luật cố định, trạng thái là tọa độ tác tử: hai vị trí $(2,1)$ và $(3,1)$ là hai trường hợp thay thế, không phải hai tác tử đồng thời. Nhận tọa độ chính xác giúp phân biệt hai trạng thái; với cảm biến bốn ô kề, cả hai đều báo Bắc và Nam là tường, Đông và Tây đi được, nên tác tử không nhận tọa độ thật. Quan sát đầy đủ không có nghĩa tác tử biết quy luật chuyển hoặc phần thưởng; khả năng xác định trạng thái từ quan sát cũng khác với việc trạng thái có đủ thông tin dự báo hay không. Biết trạng thái, do đó, không đồng nghĩa với biết mô hình hoặc biết tính Markov đã thỏa.

![So sánh quan sát đầy đủ, nơi tọa độ cho biết chính xác vị trí tác tử trên bản đồ, và quan sát một phần, nơi cảm biến bốn ô kề phù hợp với nhiều vị trí khác nhau.](img/lec-02/full-partial-observation.svg)

### Tính Markov

Trong mê cung cố định đã xét, cùng vị trí và hành động cho cùng ô kế tiếp và phần thưởng, không cần biết đường đã đi. Trực giác này được khái quát cho cả chuyển động ngẫu nhiên bằng phân phối có điều kiện: biết trạng thái và hành động thì lịch sử không cải thiện dự báo bước tới,

$$\begin{aligned}&\Pr(S_{t+1}=s',R_{t+1}=r\mid H_t=h,A_t=a)\\&\quad=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a),\end{aligned}$$

với $h$ là lịch sử kết thúc ở $s$, và $s'$, $r$ là giá trị trạng thái kế tiếp và phần thưởng. Vế trái dùng toàn bộ lịch sử, vế phải chỉ dùng trạng thái cuối và hành động hiện tại; tính Markov yêu cầu hai phân phối bằng nhau với mọi lịch sử có thể xảy ra kết thúc tại $s$. Tính chất này không xác định hành động tối ưu.

### Mở rộng trạng thái

Trạng thái được chọn và tính Markov là hai việc khác nhau: phải kiểm tra tính Markov, vì nó phụ thuộc vào cách trạng thái được định nghĩa. Nếu kết quả phụ thuộc vào việc có chìa khóa, tọa độ thôi chưa đủ và cần thêm biến chìa khóa vào trạng thái. Về nguyên tắc, mở rộng trạng thái $\tilde S_t=H_t$ phục hồi tính Markov: các lịch sử trước là tiền tố của lịch sử hiện tại, nên khi biết $\tilde S_t$ và hành động tiếp theo, không có thông tin quá khứ nào bị mất. Nhưng đây là kiến tạo lý thuyết, không phải giải pháp học hiệu quả: kích thước lịch sử tăng theo thời gian, không có bảo đảm về biểu diễn gọn với số chiều cố định, và cũng không tự động khôi phục trạng thái tiềm ẩn từ quan sát. Giữ một số hữu hạn quan sát gần nhất có thể bỏ thông tin quá khứ liên quan, nên không tự bảo đảm tính Markov.

::: exercise Câu hỏi kiểm tra
1. Phân loại ba quan sát: tọa độ chính xác; ảnh toàn mê cung thấy rõ tác tử; cảm biến bốn ô kề.

2. Nếu mở cửa phụ thuộc việc có chìa khóa, tọa độ còn đủ để mô tả trạng thái Markov không? Cần bổ sung gì?

3. Dùng toàn bộ lịch sử làm trạng thái có hạn chế thực hành gì? Ghép hữu hạn quan sát có bảo đảm Markov không?

4. Mẫu một bước, lịch sử $H_t$ và quỹ đạo $\tau$ khác nhau về phạm vi thông tin như thế nào?
:::

::: solution
1. Tọa độ và ảnh toàn bản đồ thấy rõ tác tử cho quan sát đầy đủ khi bản đồ, luật và quy ước tọa độ cố định; cảm biến bốn ô kề là quan sát một phần.

2. Chưa đủ; cần thêm trạng thái chìa khóa đã lấy hay chưa.

3. Lịch sử tăng theo thời gian, làm lưu trữ và học khó hơn. Ghép hữu hạn quan sát không bảo đảm Markov vì vẫn có thể bỏ thông tin quá khứ liên quan.

4. Mẫu chứa một chuyển tiếp; lịch sử trạng thái chứa các bước tới thời điểm hiện tại; quỹ đạo trạng thái hữu hạn chứa cả lượt tới khi kết thúc. Mẫu ở đây dùng quan sát; hai chuỗi còn lại dùng trạng thái.
:::

<!-- note-topic-id: lec-02-part-04 -->

## 4. Chính sách lựa chọn hành động

Chính sách là quy tắc chọn hành động cho từng đầu vào biểu diễn. Trong mê cung đã dùng từ đầu bài, mỗi mũi tên gán một hành động cho một vị trí; tại $(1,2)$, quy tắc minh họa chọn Bắc. Vị trí tự nó không quyết định hành động: một tác tử khác có thể chọn hành động khác dù nhận cùng tọa độ. Chính sách mô tả sự lựa chọn đó, còn mô hình môi trường mô tả kết quả khi thực hiện lựa chọn.

### Ví dụ về chính sách

Tại $x=(1,2)$, xét hai quy tắc chọn hành động:

| Quy tắc | Bắc | Đông | Nam | Tây |
|---|---|---|---|---|
| Luôn Bắc | $1$ | $0$ | $0$ | $0$ |
| Bắc hoặc Đông | $0{,}5$ | $0{,}5$ | $0$ | $0$ |

Các số là xác suất chọn. Trong ví dụ này, đầu vào của chính sách là tọa độ ô, nghĩa là biểu diễn trùng với trạng thái: $X_t=S_t$ và $x\in\mathcal X$. Môi trường cho phép chọn cả bốn hướng; chính sách quyết định xác suất của từng hướng. Chọn Đông gặp tường, giữ nguyên vị trí và vẫn nhận $-1$. Quy tắc thứ nhất luôn chọn Bắc; quy tắc thứ hai chọn Bắc hoặc Đông với xác suất bằng nhau. Tính ngẫu nhiên tự nó không bảo đảm chất lượng tốt hơn.

### Chính sách xác định

Với mỗi biểu diễn đầu vào, chính sách xác định chọn một hành động:

$$\pi:\mathcal X\to\mathcal A,\qquad A_t=\pi(X_t).$$

| $x$ | $\pi(x)$ |
|---|---|
| $(0,2)$ | Đông |
| $(1,2)$ | Bắc |
| $(1,1)$ | Đông |

$\mathcal X$ là tập biểu diễn quyết định, $\mathcal A$ là tập hành động. Bảng cho ba giá trị của cùng một chính sách; các vị trí còn lại cần được quy định khi dùng trên toàn mê cung. Ta xét chính sách không thay đổi theo thời gian. Chính sách là quy tắc đang dùng; thuật toán học là cách tạo hoặc thay đổi quy tắc đó.

### Chính sách ngẫu nhiên

Với $x\in\mathcal X$, chính sách cho một phân phối trên $\mathcal A$:

$$\pi(a\mid x)=\Pr(A_t=a\mid X_t=x),$$

với điều kiện

$$\pi(a\mid x)\ge 0,\qquad \sum_{a\in\mathcal A}\pi(a\mid x)=1.$$

Ví dụ từ bảng trước: $\pi(\text{Bắc}\mid(1,2))=0{,}5$. Với mỗi $x$ cố định, các xác suất phải không âm và cộng thành một. Chính sách xác định là trường hợp đặt xác suất một vào đúng một hành động. Nếu dùng trạng thái đầy đủ làm đầu vào, chọn $X_t=S_t$ và viết $\pi(a\mid s)$. Với quan sát một phần, đầu vào vẫn là biểu diễn mà tác tử thực sự có.

::: exercise Câu hỏi kiểm tra
1. Cho $\pi(\text{Bắc}\mid x)=0{,}2$, $\pi(\text{Đông}\mid x)=0{,}5$, $\pi(\text{Tây}\mid x)=0$. Tính $\pi(\text{Nam}\mid x)$.

2. Phân loại chính sách đó và giải thích lý do.

3. Chính sách xác định là trường hợp nào của phân phối hành động?
:::

::: solution
1. Vì các xác suất cộng thành một: $\pi(\text{Nam}\mid x)=1-0{,}2-0{,}5-0=0{,}3$.

2. Đây là chính sách ngẫu nhiên, vì nhiều hành động có xác suất dương.

3. Chính sách xác định là trường hợp một hành động có xác suất $1$ và các hành động khác $0$.
:::

<!-- note-topic-id: lec-02-part-05 -->

## 5. Hàm giá trị và mô hình môi trường

### Kết quả dài hạn của chính sách

Hai chính sách có thể nhận cùng thưởng tức thời nhưng tạo ra các đường đi dài khác nhau. Phần thưởng $-1$ ngay sau một bước không đủ để so sánh hai chính sách; cần xét cả chuỗi thưởng về sau. Ba thành phần có vai trò khác nhau: chính sách chọn hành động, hàm giá trị đánh giá kết quả dài hạn dưới một chính sách xác định trước, và mô hình dự báo phản hồi khi thực hiện một hành động.

### Ưu tiên dừng và tổng phần thưởng

Xét hai chuỗi thưởng $(2,0)$ và $(1,1)$. Nếu cộng trực tiếp, cả hai cho tổng $2$. Nếu trọng số của bước đầu là $1$ và bước sau là $0{,}5$, lợi ích của hai chuỗi lần lượt là $2$ và $1{,}5$: cách tính này ưu tiên chuỗi nhận nhiều thưởng hơn ở bước đầu.

Với chuỗi thưởng hữu hạn $a=(r_1,\ldots,r_n)$, một cách tính lợi ích là gán trọng số $w_i$ cho phần thưởng ở vị trí $i$:

$$U(a)=\sum_{i=1}^{n}w_i r_i.$$

Ký hiệu $a\succ b$ nghĩa là ưu tiên chuỗi $a$ hơn chuỗi $b$, tức $U(a)>U(b)$. Ký hiệu $[r,a]$ chỉ chuỗi nhận phần thưởng $r$ rồi tiếp tục với chuỗi $a$. Tính dừng của ưu tiên yêu cầu việc thêm cùng một phần thưởng vào đầu hai chuỗi không đổi thứ tự so sánh:

$$a\succ b\quad\Longleftrightarrow\quad[r,a]\succ[r,b].$$

Điều kiện áp dụng cho mọi cặp chuỗi hữu hạn số thực, kể cả khác độ dài, và mọi $r\in\mathbb R$. Đây là điều kiện về cách đánh giá chuỗi thưởng; tính Markov ở phần 3 là điều kiện về dự báo diễn biến của môi trường.

**Định lý.** Giả sử lợi ích có dạng cộng $U(a)=\sum_{i=1}^{n}w_i r_i$, dùng cùng một dãy trọng số cho mọi độ dài $n$, với $w_1=1$ và các trọng số dương, không tăng. Khi đó, tính dừng của ưu tiên buộc các trọng số có dạng

$$w_i=\gamma^{i-1},\qquad 0<\gamma\le1.$$

Hệ số $\gamma$ là tỉ số trọng số giữa hai bước liên tiếp, gọi là hệ số chiết khấu. Hai dạng thường dùng thuộc cùng một họ:

| Hệ số | Lợi ích |
|---|---|
| $\gamma=1$ | $U(a)=\sum_{i=1}^{n}r_i$ |
| $0<\gamma<1$ | $U(a)=\sum_{i=1}^{n}\gamma^{i-1}r_i$ |

::: proof Chứng minh
Xét hai chuỗi cùng độ dài $n$ và đặt $d_i=a_i-b_i$. Hiệu lợi ích trước và sau khi thêm cùng $r$ là

$$
\begin{aligned}
U(a)-U(b)&=\sum_{i=1}^{n}w_i d_i,\\
U([r,a])-U([r,b])&=\sum_{i=1}^{n}w_{i+1}d_i.
\end{aligned}
$$

Phần thưởng $r$ ở đầu triệt tiêu trong hiệu thứ hai. Tính dừng giữ nguyên cả hai chiều so sánh chặt. Vì vậy, nếu hai chuỗi ngang nhau trước khi thêm $r$, chúng cũng phải ngang nhau sau đó: nếu hiệu sau dương hoặc âm, chiều ngược của điều kiện dừng sẽ cho một so sánh chặt trước khi thêm $r$, trái với giả thiết ngang nhau. Do đó,

$$
\sum_{i=1}^{n}w_i d_i=0
\quad\Longrightarrow\quad
\sum_{i=1}^{n}w_{i+1}d_i=0.
$$

Với mỗi $j\ge2$, chọn $n\ge j$, đặt $d_1=w_j$, $d_j=-w_1$ và các tọa độ khác bằng $0$. Hiệu trước bằng $w_1w_j-w_jw_1=0$, nên

$$
w_2w_j-w_{j+1}w_1=0
\quad\Longrightarrow\quad
w_{j+1}=\frac{w_2}{w_1}w_j.
$$

Đặt $\gamma=w_2/w_1$. Truy hồi $w_{j+1}=\gamma w_j$ cũng đúng tại $j=1$ theo định nghĩa này. Vì $w_1=1$, suy ra $w_i=\gamma^{i-1}$. Dãy trọng số dùng chung cho mọi độ dài ngay từ giả thiết, nên $\gamma$ cũng dùng chung. Trọng số dương cho $\gamma>0$; trọng số không tăng cho $\gamma\le1$.

Ngược lại, với trọng số hình học và mọi chuỗi hữu hạn $a$,

$$U([r,a])=r+\gamma U(a).$$

Vì thế, kể cả khi $a,b$ khác độ dài,

$$U([r,a])-U([r,b])=\gamma\bigl(U(a)-U(b)\bigr).$$

Với $\gamma>0$, hiệu mới và hiệu cũ có cùng dấu. Điều kiện dừng được thỏa mãn.
:::

Với $\gamma=0{,}5$, việc thêm phần thưởng $r$ đẩy toàn bộ chuỗi cũ lùi một bước, nên các phần thưởng cũ được chiết khấu thêm một lần:

$$
\begin{aligned}
U([r,2,0])&=r+0{,}5\cdot2+0{,}25\cdot0=r+1,\\
U([r,1,1])&=r+0{,}5\cdot1+0{,}25\cdot1=r+0{,}75.
\end{aligned}
$$

Chuỗi đầu vẫn có lợi ích lớn hơn với mọi $r$.

Định lý giả sử trước dạng lợi ích cộng tuyến tính. Riêng tính dừng không suy ra dạng này. Chẳng hạn, đặt $\varnothing$ là chuỗi rỗng và định nghĩa

$$V(\varnothing)=0,\qquad V([r,a])=r+\bigl(V(a)\bigr)^3.$$

Hàm lập phương tăng ngặt nên cách tính này vẫn giữ mọi so sánh chặt khi thêm cùng $r$. Tuy nhiên, $V((0,x))=x^3$ không thể bằng $w_2x$ với một trọng số cố định cho mọi $x$.

Một biến đổi tăng ngặt của $U$ giữ cùng thứ tự ưu tiên giữa các chuỗi tất định. Với chuỗi thưởng ngẫu nhiên, đưa biến đổi đó vào kỳ vọng có thể đổi thứ tự đánh giá chính sách. Nếu bỏ giả thiết trọng số không tăng, $\gamma>1$ cũng thỏa tính dừng trên các chuỗi hữu hạn, kể cả khác độ dài. Trong bài này, tổng thưởng chỉ dùng $0\le\gamma\le1$.

Tại $\gamma=0$, lợi ích chỉ giữ phần thưởng đầu. Sau khi thêm cùng $r$, mọi chuỗi đều có lợi ích $r$, nên tương đương ưu tiên chặt không còn đúng. Giá trị này vẫn dùng được để định nghĩa mục tiêu chỉ xét phần thưởng tức thời.

### Phần thưởng tích lũy

Giả sử một quỹ đạo kết thúc sau đúng ba bước và mỗi bước nhận thưởng $-1$; với $\gamma=0{,}5$, các trọng số theo thứ tự là $1,\ 0{,}5,\ 0{,}25$, nên tổng thưởng tích lũy là
$$-1\cdot 1+(-1)\cdot 0{,}5+(-1)\cdot 0{,}25=-1{,}75.$$
Gọi $T$ là thời điểm kết thúc, $t<T$, và $\gamma\in[0,1]$ là hệ số chiết khấu:
$$G_t=\sum_{k=0}^{T-t-1}\gamma^k R_{t+k+1}.$$
$G_t$ là phần thưởng tích lũy kể từ sau hành động $A_t$; số hạng đầu là $R_{t+1}$. $G_T=0$: không còn thưởng sau khi kết thúc, điều này không xóa bỏ thưởng chuyển cuối vì $R_T$ đã nằm trong tổng tại $T-1$. Khi $\gamma=0$, chỉ giữ thưởng kế tiếp. Với nhiệm vụ tiếp diễn, tổng kéo dài vô hạn và được viết riêng:
$$G_t=\sum_{k=0}^{\infty}\gamma^k R_{t+k+1},\qquad 0\le\gamma<1.$$
Định nghĩa $R_{\max}\ge 0$ là hằng số sao cho $|R_{t+1}|\le R_{\max}$ với mọi $t$. Khi đó chặn
$$|G_t|\le\sum_{k=0}^{\infty}\gamma^k |R_{t+k+1}|\le R_{\max}\sum_{k=0}^{\infty}\gamma^k=\frac{R_{\max}}{1-\gamma}.$$
Chuỗi hình học $\sum_{k=0}^\infty\gamma^k$ với $0\le\gamma<1$ hội tụ, nên tổng hội tụ tuyệt đối.

### Giá trị kỳ vọng

Ví dụ giả định: từ $s$, dưới một chính sách cố định, môi trường chọn một trong hai nhánh kết thúc.

| Số bước còn lại | Xác suất | Tổng thưởng |
|---|---|---|
| $3$ | $0{,}5$ | $-3$ |
| $5$ | $0{,}5$ | $-5$ |

Thưởng $-1$ mỗi bước, $\gamma=1$: kỳ vọng bằng $0{,}5(-3)+0{,}5(-5)=-4$. Đây là môi trường giả định có hai nhánh, khác với mê cung chuyển xác định. Chính sách được giữ cố định; sự ngẫu nhiên nằm ở lựa chọn nhánh của môi trường. Kỳ vọng $-4$ là trung bình có trọng số, không nhất thiết là kết quả quan sát được trong một lượt: không quỹ đạo nào của ví dụ này có tổng đúng $-4$.

### Hàm giá trị trạng thái

Giữ cố định chính sách Markov $\pi(a\mid s)$ và động lực môi trường. Hàm giá trị trạng thái được định nghĩa bởi
$$v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s].$$
Kỳ vọng lấy trung bình trên hành động của chính sách và chuyển động của môi trường; hai nhánh trên cho $v_\pi(s)=-4$. Giả thiết: chọn $X_t=S_t$, $\pi$ Markov không đổi theo thời gian, môi trường Markov với quy luật cố định theo thời gian, và kỳ vọng hữu hạn. Với $\gamma=1$, thưởng bị chặn cùng với $\mathbb E_\pi[T-t\mid S_t=s]<\infty$ bảo đảm kỳ vọng hữu hạn; kết thúc với xác suất $1$ tự nó chưa đủ. Nếu có hạn chót cố định, cần đưa thời gian còn lại vào trạng thái hoặc dùng giá trị phụ thuộc thời gian. Kỳ vọng dưới $\pi$ không phải phép chọn chính sách tối ưu.

### Mô hình chuyển trạng thái và phần thưởng

Trong mê cung, từ ô $(0,2)$ chọn hành động Đông, tác tử tới $(1,2)$ và nhận thưởng $-1$; đây là một cặp kết quả (trạng thái mới, phần thưởng) xảy ra với xác suất $1$.

Mô hình dự báo đồng thời trạng thái kế tiếp và phần thưởng. Với trạng thái và phần thưởng rời rạc, $s,s'\in\mathcal S$, $r\in\mathcal R$ với $\mathcal R$ là tập giá trị thưởng, trạng thái hiện tại $s$ chưa kết thúc và hành động hợp lệ $a\in\mathcal A(s)$. Trạng thái kế tiếp $s'$ có thể là trạng thái kết thúc:
$$P(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a),$$
với $P(s',r\mid s,a)\ge 0$ và $\sum_{s',r}P(s',r\mid s,a)=1$. Ví dụ vừa xét cho $P((1,2),-1\mid(0,2),\text{Đông})=1$. Không giả định trạng thái kế tiếp và phần thưởng độc lập; tổng xác suất lấy trên mọi cặp $(s',r)$ với $s,a$ cố định. Phân phối biên theo trạng thái luôn được định nghĩa:
$$P(s'\mid s,a)=\sum_r P(s',r\mid s,a);$$
định nghĩa này không yêu cầu kỳ vọng thưởng tồn tại. Ngược lại, thưởng trung bình
$$\bar r(s,a)=\sum_{s',r}r\,P(s',r\mid s,a)$$
cần kỳ vọng thưởng tồn tại và hữu hạn. Theo giả thiết Markov và quy luật không đổi theo thời gian, không cần điều kiện hóa thêm lịch sử hay chỉ số $t$. Ký hiệu dùng chữ hoa $P$, khác với chữ $p$ thường trong Sutton–Barto. Hàm giá trị đánh giá kết quả dài hạn; mô hình mô tả phản hồi một bước. Tác tử có thể biết hoặc ước lượng $P$, và ước lượng có thể sai; không phải mọi phương pháp học tăng cường đều xây dựng mô hình tường minh.

::: exercise Câu hỏi kiểm tra
1. Ba bước đều nhận $-1$, kết thúc sau bước thứ ba. Tính $G_t$ khi $\gamma=0{,}5$.
2. Phân biệt $G_t$ của một quỹ đạo với $v_\pi(s)$.
3. Mô hình dự báo $(0,2)$ chọn Đông tới $(1,2)$ với thưởng $0$, trong khi luật là $-1$ mỗi bước; thành phần nào sai?
4. So sánh $(2,0)$ và $(1,1)$ khi cộng trực tiếp và khi $\gamma=0{,}5$.
:::

::: solution
1. Với trọng số $1,\ 0{,}5,\ 0{,}25$: $G_t=-1-0{,}5-0{,}25=-1{,}75$.
2. $G_t$ là tổng thưởng trên một quỹ đạo cụ thể; $v_\pi(s)$ là kỳ vọng của tổng thưởng từ $s$ dưới chính sách cố định.
3. Thành phần sai là phần thưởng; chuyển tiếp trạng thái $(0,2)\to(1,2)$ là đúng.
4. Cộng trực tiếp: hai chuỗi cùng tổng $2$, ngang nhau. Với $\gamma=0{,}5$: $U(2,0)=2$ và $U(1,1)=1{,}5$, nên chuỗi đầu tốt hơn; chiết khấu cho phần thưởng đến sớm trọng số lớn hơn.
:::

<!-- note-topic-id: lec-02-part-06 -->

## 6. Phần thưởng định hướng hành vi

### Mê cung và quy tắc thưởng

Mê cung mới này có hai hành lang. Mỗi đoạn nối hai nút là một bước; khoảng cách trên hình không biểu thị số bước. Tác tử chọn đi sang nút kề dọc hành lang, có thể quay lại trên các nút chưa kết thúc. Không có đường tắt xuyên tường giữa hai hành lang. Hố nằm trên hành lang trên hướng tới đích; vì vào hố là kết thúc, tác tử không thể đi xuyên qua hố để đến đích. Nhánh dưới đến đích sau sáu bước, nhánh trên gặp hố sau hai bước.

![Mê cung hai hành lang: nhánh trên gặp hố sau hai bước, nhánh dưới đến đích sau sáu bước, mỗi cạnh một bước](img/lec-02/incentive-maze.svg)

Quy ước thưởng: mỗi bước nhận $-\alpha$, kể cả bước cuối; đến đích cộng thêm $10$; vào hố không cộng thêm điểm. Đến đích hoặc vào hố thì dừng. Giả thiết $\gamma=1$, $\alpha\ge0$, chuyển động xác định.

### Điểm thưởng của hai lựa chọn

Từ điểm xuất phát, đường đến đích gồm năm bước nhận $-\alpha$ và bước cuối nhận $10-\alpha$:

$$G_{\text{đích}}=5(-\alpha)+(10-\alpha)=10-6\alpha.$$

Đường vào hố gồm hai bước, mỗi bước $-\alpha$:

$$G_{\text{hố}}=-2\alpha.$$

Ở trạng thái kết thúc, $G_T=0$: không còn thưởng tương lai. Điều này không có nghĩa phần thưởng bước cuối bằng 0 — phần thưởng ở bước cuối đã được tính vào tổng.

Để tìm tổng thưởng lớn nhất, chỉ cần so sánh hai đường ngắn nhất tới đích và hố. Với $\alpha>0$, mỗi bước thêm đóng góp $-\alpha$, nên đi vòng làm giảm tổng thưởng, còn đi mãi cho tổng $-\infty$. Với $\alpha=0$, mọi đường hữu hạn tới đích đều cho $10$, đi mãi cho $0$, nên không có ưu tiên riêng cho đường ngắn. Vì vậy, so sánh hai đường ngắn nhất cho phép tìm một chính sách tối ưu; khi $\alpha=0$, các đường vòng hữu hạn tới đích cũng tối ưu. Chỉ các chính sách có giá trị hữu hạn mới dùng được $v_\pi$ ở phần 5; đường không dừng với tổng $-\infty$ bị loại khi tìm tối ưu, nên không mâu thuẫn với giả thiết của kỳ vọng giá trị.

### Ngưỡng thay đổi hành vi

Bảng sau tính lại hai tổng khi $\alpha$ thay đổi, bản đồ và quy luật chuyển giữ nguyên:

| $\alpha$ | Đích: $10-6\alpha$ | Hố: $-2\alpha$ | Lựa chọn tối ưu |
|---|---|---|---|
| $0$ | $10$ | $0$ | Đến đích |
| $1$ | $4$ | $-2$ | Đến đích |
| $3$ | $-8$ | $-6$ | Vào hố |

Với $\alpha=3$, tác tử vào hố vì $-6>-8$. Đến đích vẫn nhận thêm $10$ nhưng sáu bước bị phạt tổng cộng $18$; vào hố chỉ bị phạt $6$. Tác tử tối ưu tổng thưởng chọn hố, dù mục tiêu của người thiết kế là đến đích.

![Tổng thưởng đường đến đích là 10 trừ 6 lần alpha, đường tới hố là âm 2 lần alpha. Hai đường giao tại alpha bằng 2,5, tổng thưởng âm 5.](img/lec-02/incentive-threshold.svg)

Ngưỡng đổi hành vi là nghiệm của $10-6\alpha=-2\alpha$, tức $\alpha=2{,}5$. Trên hình, đường liền ứng với đích, đường đứt ứng với hố. Với $0\le\alpha<2{,}5$, đường đến đích cho tổng thưởng lớn hơn. Tại $\alpha=2{,}5$, cả hai tổng bằng $-5$; chọn một trong hai đường, hoặc ngẫu nhiên giữa chúng, đều đạt cùng giá trị. Với $\alpha>2{,}5$, kết thúc sớm ở hố có lợi hơn. Ngưỡng phụ thuộc thưởng đích và chênh lệch số bước giữa hai đường.

### Phạt hố bổ sung

Giả sử vào hố bị phạt thêm $h\ge0$:

$$G_{\text{hố}}=-2\alpha-h,\qquad \alpha_{\text{ngưỡng}}=\frac{10+h}{4}.$$

Điều kiện ưu tiên đích là $10-6\alpha>-2\alpha-h$, tương đương $4\alpha<10+h$. Tăng $h$ mở rộng khoảng chi phí mà tác tử chọn đích, nhưng một mức $h$ hữu hạn không bảo đảm chọn đích với mọi $\alpha$ không bị chặn. Phạt mỗi bước khuyến khích rút ngắn đường đi đến trạng thái kết thúc được chọn; mức phạt mỗi bước quá cao khiến hố trở thành lựa chọn tối ưu. Với $\alpha=0$, đường vòng hữu hạn rồi đến đích vẫn được $10$, nên đường ngắn nhất không được ưu tiên riêng. Các kết luận này xét tác tử tối ưu tổng thưởng; trong quá trình học, tác tử có thể chưa tìm được chính sách tối ưu.

Dự đoán là đánh giá một chính sách cố định. Trong ví dụ chuyển động và chính sách xác định này, ta tính tổng thưởng của đường đi do chính sách tạo ra. Điều khiển là tìm hoặc cải thiện chính sách; ở đây, ta so sánh các đường đi để chọn chính sách có tổng thưởng cao nhất.

::: exercise Câu hỏi kiểm tra
1. Với $\alpha=2$, tác tử chọn đích hay hố? Tính hai tổng thưởng.

2. Với $\alpha=3$, mức phạt hố bổ sung $h$ phải thỏa điều kiện nào để tác tử ưu tiên đến đích?

3. Với $\alpha=0$, phần thưởng có khuyến khích đường ngắn nhất không?
:::

::: solution
1. Đích cho $10-12=-2$; hố cho $-4$. Tác tử chọn đích.

2. Cần $-8>-6-h$, tức $h>2$. Với $h=2$, hai lựa chọn ngang nhau. Nếu $h$ nguyên thì $h\ge3$.

3. Không. Mọi đường hữu hạn tới đích đều nhận tổng $10$, kể cả đường vòng.
:::

### Khuyến khích và chế tài

Cơ chế thưởng và phạt ở đây tương tự cách xã hội định hướng hành vi. Khuyến khích tạo lợi ích cho hành vi phù hợp với mục tiêu xã hội, pháp luật và chuẩn mực đạo đức; chế tài áp dụng hậu quả bất lợi đối với vi phạm để răn đe và hạn chế hành vi đó. Trong mê cung, mức phạt mỗi bước quyết định tác tử chọn đích hay hố; chính sách xã hội và pháp luật cũng dùng lợi ích và chế tài để làm hành vi phù hợp hấp dẫn hơn, hành vi vi phạm kém hấp dẫn hơn.

Cơ chế thưởng, phạt có thể tạo hành vi lách quy định hoặc hệ quả ngoài ý muốn (cực đại điểm thưởng tích luỹ). Cơ chế cần được đánh giá qua hành vi thực tế mà nó tạo ra, kể cả hành vi đối phó.

Phép liên hệ chỉ xét vai trò của khuyến khích. Pháp luật và đạo đức còn xét quyền, nghĩa vụ và công bằng. Con người còn hành động vì niềm tin, nghĩa vụ và quan hệ xã hội. Hành vi hợp pháp không tự động đồng nghĩa với hành vi hợp đạo đức; pháp luật còn bảo vệ quyền, đặt ra nghĩa vụ, thủ tục, trách nhiệm và giới hạn cho việc thực thi chế tài.

<!-- note-topic-id: lec-02-part-07 -->

## 7. Tổng kết và tự kiểm tra

Bảng ghép các thành phần của bài toán trong mê cung:

| Thành phần | Trong mê cung |
|---|---|
| $S_t, O_t, X_t$ | Vị trí thật; dữ liệu nhận được; biểu diễn dùng để quyết định |
| Chính sách $\pi$ | Chọn hướng đi từ thông tin sẵn có |
| $R_{t+1}, G_t, v_\pi$ | Thưởng từng bước; tổng thưởng; kỳ vọng theo chính sách |
| Mô hình môi trường | Dự báo vị trí kế tiếp và phần thưởng |

Với mê cung quan sát đầy đủ, có thể chọn vị trí hiện tại làm biểu diễn để quyết định. Với quan sát cục bộ, biểu diễn có thể cần thêm thông tin từ lịch sử. Chính sách chọn hành động; hàm giá trị đánh giá kết quả dài hạn theo chính sách; mô hình dự báo phản hồi của môi trường.

::: exercise Câu hỏi kiểm tra
1. Cùng một quan sát có thể khác trạng thái không?

2. Thưởng $-1$ mỗi bước có chỉ ra hành động tốt nhất ngay không?

3. Biết mô hình có đồng nghĩa biết chính sách tốt nhất không?
:::

::: solution
1. Có, ví dụ $(2,1)$ và $(3,1)$ cho cùng quan sát bốn ô kề.

2. Không, cần xét hậu quả dài hạn của các lựa chọn.

3. Không, vẫn cần giải bài toán lựa chọn trên mô hình đó.
:::

### Bài tập và tài liệu đọc

Bài tập tuần 2: Bài 1, 2, 5, 6 về tín hiệu học, đặc tả mê cung, chiết khấu, chính sách ngẫu nhiên; Bài 10 yêu cầu chọn một ứng dụng thực tế rồi nêu trạng thái, hành động, chuyển động, thưởng, điều kiện kết thúc và các khó khăn khi mô hình hóa. Các giả thiết về thông tin và phần thưởng quyết định cách mô hình hóa. Bài 3, 4, 7, 8, 9 trong cùng tập hw02 để dành sau khi học Bài 03.

Bài 03 sẽ trình bày mô hình đầy đủ: mô hình quyết định Markov và phương trình Bellman.

Tài liệu đọc:

- Tạ Việt Cường, bài giảng 2–3 "MDPs with Key Concepts" (lecture2-3-MDPswithKeyConcepts.pptx), trang 1–27.
- Tập bài tập hw02, bài 1, 2, 5, 6, 10.
- Sutton và Barto (2018), [*Reinforcement Learning: An Introduction*](https://incompleteideas.net/book/the-book-2nd.html), ấn bản 2, chương 3, mục 3.1–3.5. Ký hiệu $P$ là cách ký hiệu của slide; sách dùng $p$.
- Berkeley CS188, bài 09 (2026), [*Markov Decision Processes*](https://inst.eecs.berkeley.edu/~cs188/sp26/assets/lectures/cs188-sp26-lec09.pdf), trang 22 "Stationary Preferences".
- Shakerinava và Ravanbakhsh (2022), [*Utility Theory for Sequential Decision Making*](https://proceedings.mlr.press/v162/shakerinava22a.html). Bài báo nghiên cứu các tiên đề về ưu tiên giữa những phân phối quỹ đạo.
