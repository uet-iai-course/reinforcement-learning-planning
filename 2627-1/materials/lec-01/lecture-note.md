# Bài 01 — Giới thiệu Học tăng cường

## Mục tiêu và kiến thức tiên quyết

Sau bài này, người học làm được:

1. Giải thích tác tử học từ tương tác, phản hồi trễ và dữ liệu phụ thuộc thời gian.
2. Phân biệt Học tăng cường với học có giám sát và học không giám sát.
3. Mô tả vai trò của chính sách, hàm giá trị và mô hình môi trường tùy chọn.
4. Biểu diễn bài toán Tic-tac-toe bằng trạng thái, hành động và phần thưởng, và kiểm tra một quyết định bằng hàm giá trị.

Kiến thức cần dùng: xác suất cơ bản (biến ngẫu nhiên, kỳ vọng có điều kiện, phân phối đều), đại số tuyến tính cơ bản. Không cần kiến thức về thuật toán Học tăng cường; bài này chỉ xây dựng khung khái niệm và không trình bày thuật toán. Bản nguồn không có nội dung mã hoặc code demo, nên note cũng không có.

## Bản đồ chủ đề

### Tác tử học từ tương tác

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: đặt vấn đề — vì sao một tác tử phải học từ hậu quả của hành động thay vì dùng mô hình điều khiển cố định.
- Kết nối vào: không có; đây là điểm mở đầu.
- Kết nối ra: cung cấp ngôn ngữ tác tử–môi trường và hai ca ứng dụng dẫn nhập cho phần khung học.
- Nguồn: PPTX nguồn, trang 3–9, 16–17.

### Khung Học tăng cường và ba dạng tín hiệu

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: xác định khung học từ tương tác và phân biệt ba dạng tín hiệu học.
- Kết nối vào: hai ca ứng dụng dẫn nhập cho thấy cả hai đều học từ tương tác.
- Kết nối ra: tiêu chí nhận dạng Học tăng cường, dùng làm nền cho định nghĩa phần thưởng.
- Nguồn: PPTX nguồn, trang 19–21.

### Phần thưởng và kết quả dài hạn

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: định lượng phản hồi trễ bằng phần thưởng một bước và phần thưởng tích lũy.
- Kết nối vào: tiêu chí "phản hồi có thể trễ" từ khung học.
- Kết nối ra: đại lượng $G_t$ dùng để định nghĩa hàm giá trị.
- Nguồn: PPTX nguồn, trang 23–25.

### Chính sách, hàm giá trị và mô hình tùy chọn

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: đặt tên cho các thành phần điều khiển và đánh giá của tác tử.
- Kết nối vào: $G_t$ từ chủ đề phần thưởng.
- Kết nối ra: $\pi$ và $V^\pi$ dùng trực tiếp trong ví dụ Tic-tac-toe và trong đánh đổi thăm dò–khai thác.
- Nguồn: PPTX nguồn, trang 26.

### Thăm dò và khai thác

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: gắn đánh đổi giữa thu thập thông tin và dùng thông tin hiện có vào chính sách vừa định nghĩa.
- Kết nối vào: chính sách và ước lượng giá trị từ chủ đề thành phần.
- Kết nối ra: quyết định có dữ kiện thiếu được nêu tường minh, chuẩn bị cho ví dụ Tic-tac-toe.
- Nguồn: PPTX nguồn, trang 27.

### Mô hình hóa Tic-tac-toe

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: tổng hợp trạng thái, tập hành động hợp lệ, phần thưởng, chính sách, giá trị và thăm dò vào một bài toán kiểm chứng được.
- Kết nối vào: toàn bộ khung từ năm chủ đề trước.
- Kết nối ra: người học biểu diễn được một bài toán mới bằng các thành phần này.
- Nguồn: PPTX nguồn, trang 28–30.

### Cầu nối: từ lịch sử $h_t$ đến trạng thái $S_t$ trong Tic-tac-toe

- Nhóm: `cầu nối`.
- Vai trò trong mạch: định nghĩa $V^\pi$ dùng lịch sử $h_t$ vì bài chưa đưa giả thiết Markov; trong Tic-tac-toe quan sát đầy đủ, lịch sử rút gọn thành cặp (thế cờ $S_t$, lượt chơi), nên định nghĩa áp dụng trực tiếp vào ví dụ cuối.
- Kết nối vào: định nghĩa $V^\pi(h_t)$; kết nối ra: cách viết $V^\pi(S_t)$ ở ví dụ Tic-tac-toe.
- Nguồn: PPTX nguồn, trang 26, 29–30.

### Bổ sung: giới hạn mô hình điều khiển cố định

- Nhóm: `bổ sung`.
- Vai trò trong mạch: lấp khoảng trống "vì sao không dùng cách thiết kế điều khiển cũ" trong chủ đề tác tử học.
- Nguồn: PPTX nguồn, trang 6–9.

### Bổ sung: AlphaGo và thao tác robot

- Nhóm: `bổ sung`.
- Vai trò trong mạch: hai trường hợp dẫn nhập cho thấy hai miền thực tế đòi hỏi học từ tương tác, trước khi khung hình thức xuất hiện.
- Nguồn: PPTX nguồn, trang 10–13, 22; Silver và cộng sự (2016).

### Bổ sung: giả thuyết phần thưởng

- Nhóm: `bổ sung`.
- Vai trò trong mạch: phát biểu có điều kiện về phạm vi của cách mã hóa mục tiêu bằng phần thưởng, kèm giới hạn.
- Nguồn: PPTX nguồn, trang 24–25.

### Đọc thêm

- Sutton, R. S. & Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, Chương 1.
- David Silver, *Introduction to Reinforcement Learning*, Lecture 1.
- Silver và cộng sự (2016), *Mastering the game of Go with deep neural networks and tree search*, Nature.
- Thảo luận không kết luận về tác tử tổng quát và mô hình thế giới: PPTX nguồn, trang 14–15, 43–44.

## Ký hiệu và quy ước

- Chỉ số thời gian $t = 0, 1, \ldots, T-1$; $T$ là chỉ số của trạng thái kết thúc trong nhiệm vụ hữu hạn.
- $S_t$: trạng thái tại bước $t$. $A_t$: hành động tại bước $t$. Trong Tic-tac-toe, $\mathcal A(S_t)$ là tập hành động hợp lệ tại $S_t$ và $A_t \in \mathcal A(S_t)$.
- $R_{t+1} \in \mathbb R$: phần thưởng môi trường trả sau hành động $A_t$; chỉ số gắn với chuyển tiếp vừa xảy ra.
- $G_t = \sum_{k=t+1}^{T} R_k$: tổng phần thưởng từ sau bước $t$ đến khi kết thúc. Bài này không dùng hệ số chiết khấu vì nguồn không đưa.
- $H_t$: lịch sử ngẫu nhiên đến bước $t$; $h_t$: một lịch sử đã quan sát. Kỳ vọng $\mathbb E_\pi[\,\cdot \mid H_t = h_t\,]$ lấy theo mọi nguồn ngẫu nhiên sau $h_t$: cách chính sách chọn hành động và cách môi trường (gồm đối thủ) sinh kết quả.
- $\pi(a \mid h_t)$: phân phối chọn hành động của chính sách; chính sách có thể ngẫu nhiên.
- $V^\pi(h_t) = \mathbb E_\pi[G_t \mid H_t = h_t]$: giá trị của lịch sử $h_t$ dưới chính sách $\pi$. Hàm giá trị luôn phụ thuộc chính sách đang được đánh giá.
- $V^\pi(S_T) = 0$: giá trị của trạng thái kết thúc bằng $0$; quy ước này dùng trong ví dụ Tic-tac-toe.
- Dấu mũ ($\widehat S_{t+1}$, $\widehat R_{t+1}$) biểu thị dự báo của mô hình, không khẳng định dự báo đúng.
- Bài này không phát biểu giả thiết Markov; mọi định nghĩa dùng lịch sử. Chỉ trong Tic-tac-toe quan sát đầy đủ, lịch sử được rút gọn thành $(S_t, \text{lượt})$.

<!-- note-topic-id: lec-01-topic-01 -->
## Tác tử học từ tương tác

**Vấn đề.** Một robot dọn nhà phải chọn hành động liên tục, nhưng tiêu chí đánh giá nó (nhà có sạch hay không) chỉ xuất hiện sau khi chuỗi hành động đã diễn ra. Thiết kế điều khiển cố định gặp giới hạn khi môi trường thay đổi; phần bổ sung cuối chủ đề trình bày chi tiết. Vấn đề cần giải quyết: tác tử phải cải thiện quyết định trong điều kiện không có hành động đúng cho từng bước.

**Trực giác.** Tác tử và môi trường tương tác theo vòng lặp: tác tử nhận quan sát và chọn hành động; môi trường tiếp nhận hành động, chuyển trạng thái và trả về quan sát cùng phần thưởng. Trạng thái mô tả tình huống thực; quan sát là dữ liệu tác tử nhận về tình huống đó, và hai đại lượng có thể khác nhau (vị trí thật của vật là trạng thái, ảnh camera có nhiễu là quan sát). Mỗi hành động làm đổi dữ liệu mà tác tử sẽ quan sát sau đó, nên hành vi tác tử tự quyết định phần nào dữ liệu học của chính nó.

**Ví dụ tính được.** Robot dọn nhà trong một phòng có ba ô. Ở bước $t=0$, robot ở ô 1 và chọn đi sang ô 2. Môi trường trả quan sát "ô 2 có ghế chắn" và phần thưởng $R_1 = 0$. Hành động này làm đổi tập hành động khả dụng ở bước sau: từ ô 2, robot không thể đi thẳng mà phải vòng. Sau ba bước, phần thưởng chỉ đến khi phòng được coi là sạch. Dãy quan sát và phần thưởng vì thế phụ thuộc thứ tự các hành động đã chọn; không thể tráo thứ tự các bước tương tác.

**Hình thức.** Ba năng lực giải thích vì sao tác tử cần học: ghi nhớ (giữ kinh nghiệm đã quan sát), thích nghi (đổi hành vi khi môi trường đổi), khái quát (xử lý tình huống chưa gặp đúng dạng). Học tăng cường là khung chung trong đó tác tử tương tác với môi trường để thu nhận kinh nghiệm, hành động được định hình bởi một tín hiệu vô hướng từ môi trường, và tín hiệu này đến trễ trên một quỹ đạo dài. Bài này không đưa thuật toán cụ thể: bước "thuật toán" ở đây không áp dụng, vì nguồn chỉ xác lập khung chứ chưa định nghĩa cách cập nhật.

**Ứng dụng và giới hạn.** Hai ca ứng dụng dẫn nhập (AlphaGo và thao tác robot, xem bổ sung dưới đây) cho thấy nhu cầu học từ tương tác. Giới hạn: nguồn không cung cấp thuật toán hay số liệu cho hai ca này, nên không suy thêm chi tiết; các khái niệm hình thức (chính sách, hàm giá trị) mới được định nghĩa ở chủ đề sau.

**Kiểm tra.** Với robot dọn nhà khi vị trí đồ đạc thay đổi, năng lực nào trong ba năng lực trên là yêu cầu trực tiếp, và năng lực nào giúp xử lý bố trí mới chưa từng gặp?

::: solution
Trả lời: thích nghi là yêu cầu trực tiếp; khái quát giúp xử lý bố trí mới; ghi nhớ đơn thuần không đủ nếu trạng thái chưa từng xuất hiện.
:::

<!-- note-topic-id: lec-01-topic-09 -->
### Bổ sung: AlphaGo và thao tác robot

AlphaGo học cách đánh giá nước đi rồi kết hợp với tìm kiếm cây trong cờ vây (Silver và cộng sự, 2016). Thao tác robot học từ tương tác vật lý: quan sát (vị trí, tư thế, tiếp xúc) đổi sau mỗi thao tác, và tiêu chí (hoàn tất sắp xếp) chỉ đánh giá được sau cả chuỗi. Hai trường hợp này dẫn nhập cho hai miền thực tế đòi hỏi học từ tương tác, trước khi khung hình thức xuất hiện ở chủ đề sau.

<!-- note-topic-id: lec-01-topic-08 -->
### Bổ sung: giới hạn mô hình điều khiển cố định

Cách thiết kế điều khiển cũ mô hình hóa môi trường trước, rồi bộ điều khiển tối ưu hành động theo mô hình đó qua một hàm mục tiêu. Cách này gặp ba vấn đề: mô hình có thể sai khi môi trường đổi (đồ đạc di chuyển, vật thể chuyển động); không gian tìm kiếm quá lớn; và lập kế hoạch dưới bất định (ví dụ xe tự hành) khó thực hiện khi mô hình không bao phủ các tình huống thực. Học tăng cường là cách tiếp cận học từ tương tác thay cho mô hình cố định; tác tử có thể học cả mô hình hoặc học không cần mô hình tường minh, sự phân biệt này được định nghĩa ở chủ đề thành phần. Không kết luận rằng điều khiển cố định luôn thất bại; điểm đối chiếu là mô hình được cung cấp và giữ cố định.

<!-- note-topic-id: lec-01-topic-02 -->
## Khung Học tăng cường và ba dạng tín hiệu

**Vấn đề.** Hai ca ứng dụng vừa xét đều học từ tương tác. Cần xác định tín hiệu nào hướng dẫn tác tử khi không có hành động đúng cho từng bước, và tín hiệu đó khác gì tín hiệu của học có giám sát và học không giám sát.

**Trực giác.** Học tăng cường nghiên cứu cách tác tử chọn hành động để tối đa hóa kỳ vọng của tổng phần thưởng tích lũy. Ba đặc điểm định hình dữ liệu học: hành động ở bước $t$ làm đổi dữ liệu quan sát ở các bước sau; chuỗi mẫu không thỏa giả thiết độc lập và cùng phân phối (i.i.d.); phản hồi có thể đến sau nhiều hành động. Học tăng cường liên hệ với nhiều lĩnh vực: khoa học máy tính (học máy, robot học, trí tuệ nhân tạo), kỹ thuật (lý thuyết điều khiển), toán học (tối ưu, xác suất, hệ động lực), kinh tế học (lý thuyết quyết định, lý thuyết trò chơi), tâm lý học và thần kinh học (hệ phần thưởng, hành vi học). Trong học phần này, trọng tâm là mô hình toán, thuật toán và đánh giá tác tử.

**Ví dụ tính được.** Một robot chọn đường đi: mỗi lựa chọn đổi vị trí và quan sát tiếp theo; robot chỉ nhận điểm khi hoàn tất nhiệm vụ. Nếu tráo thứ tự hai mẫu trong chuỗi tương tác, mẫu sau mô tả một tình huống không thể xảy ra sau mẫu trước, vì vị trí ở bước sau là hậu quả của hành động ở bước trước. Dữ liệu vì thế phụ thuộc thời gian.

**Hình thức.** Ba dạng tín hiệu học phân biệt nhau ở nguồn và thời điểm của tín hiệu:

- Học có giám sát: mỗi mẫu huấn luyện đi kèm tín hiệu mục tiêu trực tiếp; sai số dự đoán tính được ngay trên từng mẫu.
- Học không giám sát: dữ liệu không kèm nhãn mục tiêu cho từng mẫu; thuật toán tìm cấu trúc hoặc biểu diễn trong dữ liệu (ví dụ phân cụm theo độ tương tự).
- Học tăng cường: tín hiệu đến trễ, qua tương tác; không có hành động đúng cho từng bước, chỉ có phần thưởng.

Bốn khác biệt chính của Học tăng cường so với hai dạng còn lại: không có giám sát viên, chỉ có tín hiệu phần thưởng; phản hồi bị trễ; dữ liệu không i.i.d. và thứ tự thời gian có vai trò quyết định; hành động của tác tử có hậu quả lên dữ liệu sau này.

**Ứng dụng và giới hạn.** Tiêu chí nhận dạng: một bài toán là Học tăng cường khi tác tử tác động lên dữ liệu tương lai và chỉ nhận phản hồi sau một chuỗi hành động. Giới hạn: đây là đối chiếu khái quát; một hệ thống thực có thể kết hợp nhiều dạng học, và không đồng nhất mọi hoạt động trong lớp học với một loại học máy (chấm điểm một đáp án đúng đã biết là tín hiệu có giám sát, vì đáp án cung cấp mục tiêu trực tiếp cho từng mẫu).

**Kiểm tra.** Trong tình huống robot chọn đường đi ở trên, vì sao không được tráo thứ tự các mẫu, và dấu hiệu nào xác định đây là Học tăng cường?

::: solution
Trả lời: không tráo được vì quan sát ở bước sau là hậu quả của hành động ở bước trước; đây là Học tăng cường vì tác tử tác động lên dữ liệu tương lai và chỉ nhận phản hồi sau một chuỗi hành động.
:::

<!-- note-topic-id: lec-01-topic-03 -->
## Phần thưởng và kết quả dài hạn

**Vấn đề.** Phản hồi trễ cần được định lượng: hậu quả của hành động $A_t$ được đo bằng gì, khi phần thưởng đến từng bước nhưng mục tiêu nằm ở kết quả cuối?

**Trực giác.** Trên một quỹ đạo hữu hạn $S_0, S_1, \ldots, S_T$, mỗi chuyển tiếp mang một cặp $(A_t, R_{t+1})$: sau hành động $A_t$ tại $S_t$, môi trường trả phần thưởng $R_{t+1}$ và tác tử quan sát trạng thái tiếp theo. Phần thưởng một bước đánh giá chuyển tiếp vừa xảy ra, nhưng $A_t$ còn ảnh hưởng các phần thưởng sau đó.

**Ví dụ tính được.** Với $T = 4$ và dãy phần thưởng $R_1 = 0$, $R_2 = 0$, $R_3 = 0$, $R_4 = 1$ (chỉ bước kết thúc mang phần thưởng):

$$G_0 = R_1 + R_2 + R_3 + R_4 = 0 + 0 + 0 + 1 = 1.$$

Tương tự, $G_3 = R_4 = 1$, vì sau bước 3 chỉ còn phần thưởng kết thúc. Mỗi tổng gắn với một điểm bắt đầu trên quỹ đạo; cùng một dãy phần thưởng cho các giá trị $G_t$ khác nhau tại các $t$ khác nhau. Trong ví dụ này, $T = 4$ là chỉ số của trạng thái kết thúc; tổng quát, với trạng thái kết thúc $S_T$, phần thưởng tích lũy từ sau bước $t$ được định nghĩa bởi công thức ngay sau đây.

**Hình thức.** Với $t = 0, \ldots, T-1$, môi trường trả $R_{t+1} \in \mathbb R$ sau hành động $A_t$. Phần thưởng tích lũy từ sau bước $t$ đến khi kết thúc:

$$G_t = \sum_{k=t+1}^{T} R_k.$$

Công thức dùng nhiệm vụ hữu hạn và không đưa hệ số chiết khấu, vì nguồn không trình bày chiết khấu ở bài này. Mục tiêu của tác tử là chọn hành động để cực đại hóa tổng phần thưởng tương lai; hành động có thể có hậu quả dài hạn, và có khi hy sinh phần thưởng tức thời để nhận phần thưởng dài hạn lớn hơn (ví dụ: trong cờ, một nước hy sinh quân có thể dẫn tới thắng ván).

**Ứng dụng và giới hạn.** Ứng dụng: cách đặt phần thưởng quyết định hành vi tác tử. Trong cờ, kết quả cuối ván biểu diễn được bằng thắng, hòa hoặc thua. Trong robot dọn nhà, cần chọn tín hiệu phản ánh đúng kết quả dọn dẹp mong muốn; một mục tiêu như "không làm hỏng đồ vật" có thể bị bỏ sót nếu phần thưởng chỉ phản ánh việc hoàn tất nhiệm vụ. Giới hạn: giả thuyết phần thưởng (bổ sung dưới đây) là phát biểu mô hình hóa, không phải định lý rằng mọi mục tiêu đều được mã hóa đầy đủ bằng một số vô hướng.

**Kiểm tra.** Trên quỹ đạo với $T=4$ và $R_1 = 0$, $R_2 = 0$, $R_3 = 0$, $R_4 = 1$: tính $G_1$ và $G_3$.

::: solution
Trả lời: $G_1 = R_2 + R_3 + R_4 = 1$; $G_3 = R_4 = 1$.
:::

<!-- note-topic-id: lec-01-topic-10 -->
### Bổ sung: giả thuyết phần thưởng

Giả thuyết phần thưởng (reward hypothesis) phát biểu: mọi mục tiêu có thể được mô tả bằng cực đại hóa kỳ vọng của phần thưởng tích lũy. Phát biểu này có điều kiện: nó đúng cho các bài toán mà mục tiêu có thể mô hình hóa bằng một tín hiệu vô hướng tích lũy; mức độ phù hợp phụ thuộc cách đặt phần thưởng, và tín hiệu sai có thể tạo hành vi ngoài ý muốn. Kỳ vọng lấy theo nguồn ngẫu nhiên của chính sách và môi trường. Nguồn trình bày giả thuyết này ở dạng rộng; bản note giữ dạng có điều kiện như trên để tránh hiểu rằng mọi mục tiêu thực tế đều mã hóa được trọn vẹn.

<!-- note-topic-id: lec-01-topic-04 -->
## Chính sách, hàm giá trị và mô hình tùy chọn

**Vấn đề.** Mục tiêu là cực đại hóa kỳ vọng của $G_t$. Trong một thế cờ, tác tử phải tách hai việc: chọn nước đi và đánh giá thế cờ. Cần đặt tên cho các thành phần thực hiện hai việc này.

**Trực giác.** Trên cùng một thế cờ, chọn nước là một phép ánh xạ từ tình huống sang hành động; đánh giá thế cờ là một phép đo về kết quả tương lai. Hai nhiệm vụ khác nhau, và một tác tử có thể cần cả hai: chính sách cho biết làm gì, hàm giá trị cho biết một tình huống đáng giá bao nhiêu.

**Ví dụ tính được.** Ví dụ sau là dữ kiện giả định để tính tay, không phải số liệu thực nghiệm hay dữ kiện từ nguồn. Lấy một thế cờ Tic-tac-toe với ba ô trống (luật đầy đủ ở chủ đề Tic-tac-toe). Nếu chính sách chọn đều trên ba nước hợp lệ và mỗi nước dẫn tới một kết quả cuối với phần thưởng $+1$, $0$ hoặc $-1$ với xác suất bằng nhau, thì giá trị của thế cờ là trung bình của ba phần thưởng đó: $V^\pi = (1 + 0 + (-1))/3 = 0$. Nếu một nước dẫn chắc tới thắng, giá trị thế cờ sau nước đó là $+1$, cao hơn giá trị trước khi chọn.

**Hình thức.** Ba thành phần:

- **Chính sách** $\pi(a \mid h_t)$: phân phối chọn hành động; chính sách có thể ngẫu nhiên. Chính sách quyết định hành động nào được thực hiện.
- **Hàm giá trị** $V^\pi(h_t) = \mathbb E_\pi[G_t \mid H_t = h_t]$: kỳ vọng của phần thưởng tích lũy dưới chính sách $\pi$, theo mọi nguồn ngẫu nhiên sau $h_t$ (cách chính sách chọn hành động và cách môi trường sinh kết quả). Hàm giá trị là niềm tin về kết quả kỳ vọng của một tình huống.
- **Mô hình môi trường** (tùy chọn): dự báo quan sát hoặc trạng thái kế tiếp và phần thưởng sau một hành động, viết $(\widehat S_{t+1}, \widehat R_{t+1})$ hoặc $(\widehat O_{t+1}, \widehat R_{t+1})$. Tác tử có mô hình dùng dự báo để lập kế hoạch; tác tử phi mô hình học chính sách hoặc giá trị mà không cần mô hình chuyển tiếp tường minh.

Mô hình không bắt buộc trong mọi tác tử Học tăng cường; nó có thể được cung cấp hoặc học từ dữ liệu. Dấu mũ biểu thị dự báo, không khẳng định mô hình cho kết quả đúng tuyệt đối.

**Ứng dụng và giới hạn.** Ứng dụng tổng hợp của hai thành phần chính nằm ở ví dụ Tic-tac-toe (chủ đề cuối), nơi phép chọn nước dùng trực tiếp $\pi$ và $V^\pi$. Giới hạn: bài này chưa đưa giả thiết Markov, nên định nghĩa dùng lịch sử $h_t$; việc rút gọn lịch sử thành trạng thái chỉ hợp lệ trong các miền quan sát đầy đủ như Tic-tac-toe (xem cầu nối dưới đây).

**Kiểm tra.** Một tác tử có chính sách nhưng không có mô hình môi trường: nó có phải là tác tử Học tăng cường không?

::: solution
Trả lời: có; mô hình là thành phần tùy chọn, tác tử phi mô hình vẫn học chính sách hoặc giá trị từ tương tác.
:::

<!-- note-topic-id: lec-01-topic-07 -->
### Cầu nối: từ $V^\pi(h_t)$ đến $V^\pi(S_t)$

Định nghĩa $V^\pi(h_t) = \mathbb E_\pi[G_t \mid H_t = h_t]$ dùng lịch sử vì bài chưa phát biểu giả thiết Markov. Trong Tic-tac-toe, trò chơi quan sát đầy đủ: toàn bộ thông tin cần cho quyết định nằm trong thế cờ hiện tại và lượt chơi, nên lịch sử $h_t$ rút gọn thành cặp $(S_t, \text{lượt})$. Khi đó cách viết $V^\pi(S_t)$ ở ví dụ cuối là cùng một định nghĩa, chỉ đổi đối số từ lịch sử sang trạng thái. Kỳ vọng lấy theo cả chính sách $\pi$ và phân phối lựa chọn của đối thủ (trong ví dụ, đối thủ chọn đều trên các nước hợp lệ).

<!-- note-topic-id: lec-01-topic-05 -->
## Thăm dò và khai thác

**Vấn đề.** Chính sách và giá trị là công cụ chọn hành động. Nhưng khi ước lượng giá trị còn thiếu dữ liệu, tác tử phải chọn giữa nước đã được đánh giá cao và nước còn ít dữ liệu. Hai mục tiêu này xung đột trong ngắn hạn.

**Trực giác.** Thăm dò thu thập thêm thông tin về hậu quả hoặc giá trị của các lựa chọn; chi phí là phần thưởng ngắn hạn có thể thấp. Khai thác dùng hiểu biết hiện có để chọn hành động đang được đánh giá tốt nhất; rủi ro là nếu ước lượng còn thiếu dữ liệu, lựa chọn đang tốt nhất theo số liệu có thể chưa thật sự tốt nhất, và khai thác quá sớm giữ tác tử ở lựa chọn chưa tốt. Thăm dò không đồng nghĩa với chọn ngẫu nhiên vô điều kiện; mục đích là thu thập thông tin có ích cho quyết định sau.

**Ví dụ tính được.** Bảng sau là ví dụ giả định (không phải số liệu từ nguồn), dùng để cô lập đánh đổi khỏi luật trò chơi:

| Hành động | Số lần thử | Phần thưởng trung bình |
|---|---:|---:|
| A | 20 | 0,60 |
| B | 2 | 0,55 |

Khai thác một bước tương ứng chọn A, vì trung bình mẫu của A cao hơn. Thăm dò tương ứng thử thêm B, vì B chỉ được thử 2 lần nên độ bất định về giá trị thật của nó chưa được xác định. Không có đáp án duy nhất: quyết định phụ thuộc dữ kiện còn thiếu.

**Hình thức.** Trong khung chính sách: khai thác tương ứng chọn hành động theo giá trị ước lượng hiện có; thăm dò tương ứng để chính sách $\pi$ đặt xác suất khác không cho hành động còn ít dữ liệu. Bài này không định nghĩa thuật toán cân bằng hai mục tiêu; bước "thuật toán" không áp dụng, vì nguồn chỉ xác lập đánh đổi.

**Ứng dụng và giới hạn.** Ứng dụng: trong Tic-tac-toe, tác tử vừa cần tìm hiểu hậu quả của các nước ít thử, vừa cần dùng nước đang được đánh giá tốt. Giới hạn: ví dụ số ở trên là giả định để kiểm tra đánh đổi; kết luận nào về lựa chọn đúng đắn cần thêm dữ kiện về phân phối phần thưởng và số lượt còn lại.

**Kiểm tra.** Với bảng hai hành động ở trên, nêu ít nhất hai dữ kiện còn thiếu trước khi quyết định chọn A hay thử B.

::: solution
Trả lời (gợi ý): phân phối hoặc phương sai phần thưởng của mỗi hành động; số lượt còn lại; mục tiêu về rủi ro của tác tử.
:::

<!-- note-topic-id: lec-01-topic-06 -->
## Mô hình hóa Tic-tac-toe

**Vấn đề.** Cần một miền có luật rõ để kiểm chứng toàn bộ khung vừa xây. Bài toán: chơi Tic-tac-toe với quân X, chống lại một đối thủ chọn đều trên các nước hợp lệ; chọn nước hợp lệ để đạt kết quả cuối tốt.

**Trực giác.** Có hai cách tiếp cận. Cách thứ nhất là tìm kiếm trên cây trò chơi: mỗi nút là một thế cờ, mỗi cạnh là một nước đi hợp lệ; tìm kiếm đánh giá các chuỗi nước đi có thể xảy ra. Cách thứ hai là học: xây dựng hàm giá trị để đánh giá thế cờ đầu vào, thay vì duyệt toàn bộ chuỗi nước đi. Hai cách dùng cùng dữ kiện luật chơi nhưng khác nhau ở chỗ cách thứ hai học từ tương tác.

**Ví dụ tính được.** Đến lượt X, bàn cờ còn trống các ô 3, 7 và 9. Tập hành động hợp lệ là $\mathcal A(S_t) = \{3, 7, 9\}$. Nếu tác tử đánh ô 5 (đã có quân), hành động đó không thuộc $\mathcal A(S_t)$ nên không hợp lệ. Nếu tác tử đánh ô 9 trống tạo đường chéo thắng, phần thưởng ngay là $R_{t+1} = +1$ và ván kết thúc; theo quy ước $V^\pi(S_T) = 0$, giá trị tương lai của trạng thái kết thúc bằng $0$. Hai nước còn lại có thưởng tức thời $0$ và giá trị phụ thuộc diễn biến tiếp theo dưới $\pi$.

**Hình thức.** Biểu diễn bài toán:

- Trạng thái $S_t$: cấu hình bàn cờ và lượt chơi tại bước $t$.
- Hành động $A_t \in \mathcal A(S_t)$, với $\mathcal A(S_t)$ là tập ô trống tại $S_t$. Tập hành động phụ thuộc trạng thái; một ô đã đánh không còn là hành động hợp lệ.
- Phần thưởng $R_{t+1}$, theo góc nhìn tác tử: $+1$ khi thắng; $-1$ khi thua; $0$ ở bước chưa kết thúc và $0$ khi hòa ở bước kết thúc.

Vì trò chơi quan sát đầy đủ, cầu nối từ chủ đề thành phần áp dụng trực tiếp: $h_t \leftrightarrow (S_t, \text{lượt})$, nên $V^\pi$ viết trên trạng thái. Trước khi viết phép chọn khai thác một bước, nối từ hai định nghĩa đã có: vì $G_t = R_{t+1} + G_{t+1}$ và $V^\pi(S_{t+1}) = \mathbb E_\pi[G_{t+1} \mid S_{t+1}]$, thay kỳ vọng vào tổng cho $R_{t+1} + V^\pi(S_{t+1})$. Bước này dùng hai giả thiết riêng của Tic-tac-toe: trạng thái gồm bàn cờ và lượt chơi là đủ thông tin cho quyết định, và chính sách của đối thủ phụ thuộc trạng thái. Đây không phải tuyên bố Bellman tổng quát cho phần trước của bài. Phép chọn khai thác một bước:

$$a^* \in \arg\max_{a \in \mathcal A(S_t)} \mathbb E_\pi\!\left[R_{t+1} + V^\pi(S_{t+1}) \mid S_t,\, A_t = a\right].$$

Kỳ vọng lấy theo chính sách $\pi$ hiện tại và phản hồi ngẫu nhiên của đối thủ (chọn đều trên nước hợp lệ). Đây là phép chọn khai thác một bước theo $V^\pi$; nó không phải hành động tối ưu nếu $V^\pi$ chưa là hàm giá trị tối ưu. Bài này không trình bày thuật toán học $V^\pi$; bước "thuật toán" không áp dụng vì nguồn chỉ nêu "có thể xây dựng hàm giá trị" mà không định nghĩa cách cập nhật.

**Ứng dụng và giới hạn.** Ứng dụng: mô hình hóa này là khuôn để biểu diễn một bài toán mới bằng trạng thái, hành động, phần thưởng, chính sách và hàm giá trị. Giới hạn: bản nguồn ghi hành động là số 1–9 và tập thưởng có giá trị "9"; giá trị "9" được xem là lỗi đánh máy, và hành động 1–9 không loại ô đã đánh. Bản note dùng quy ước thưởng $\{+1, 0, -1\}$ và tập hành động $\mathcal A(S_t)$; đây là lựa chọn mô hình hóa, không phải hệ quả bắt buộc của luật chơi, và sai khác so với nguồn cần ghi vào nhật ký rà soát.

**Kiểm tra.** Đến lượt X; bàn cờ khác ví dụ trên, còn trống các ô 2, 6 và 8. Tác tử chọn ô 5. Biểu diễn này sai ở đâu?

::: solution
Trả lời: tập hành động hợp lệ là $\{2, 6, 8\}$, nên chọn ô 5 không hợp lệ. Ba giá trị thưởng khi ván kết thúc là $+1$, $0$, $-1$ tương ứng thắng, hòa, thua. Với một thế cờ kế tiếp, hàm giá trị đánh giá kết quả tương lai dưới chính sách; chính sách chọn nước.
:::

## Nội dung tự học

- Đọc Sutton và Barto (2018), Chương 1, đối chiếu cách trình bày tác tử–môi trường và phần thưởng tích lũy với bài này.
- Xem David Silver, Lecture 1, để thấy cùng khung khái niệm được trình bày với các ví dụ khác.
- Đọc tóm tắt Silver và cộng sự (2016) về AlphaGo để đối chiếu hai vai trò "đánh giá nước đi" và "chọn hành động" với chính sách và hàm giá trị.
- Tự kiểm tra: mô tả một bài toán mới (không phải Tic-tac-toe) bằng tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng, chính sách và hàm giá trị; kiểm tra rằng tập hành động phụ thuộc trạng thái và phần thưởng phản ánh đúng mục tiêu.

## Bài kiểm tra

1. Giới hạn của điều khiển với mô hình cố định trong ví dụ robot dọn nhà là gì? (Gợi ý: môi trường đổi; không gian tìm kiếm lớn.)
2. Vì sao dữ liệu tương tác phụ thuộc thứ tự thời gian? (Gợi ý: hành động hiện tại làm đổi trạng thái và quan sát tiếp theo.)
3. Phản hồi trễ ảnh hưởng việc đánh giá hành động như thế nào? (Gợi ý: hành động sớm chỉ được đánh giá sau khi quan sát hậu quả về sau.)
4. Chính sách, hàm giá trị và mô hình có vai trò gì? Mô hình có bắt buộc không? (Gợi ý: chọn hành động; đánh giá tương lai; dự báo thay đổi; tùy chọn.)
5. Thăm dò khác khai thác ở mục tiêu trước mắt nào? (Gợi ý: thu thập thông tin so với dùng hiểu biết hiện có.)
6. Nhiệm vụ chuyển giao: mô hình hóa robot dọn nhà bằng trạng thái, quan sát, hành động và phần thưởng. (Gợi ý: nêu rõ thông tin nào thuộc trạng thái thực, dữ liệu nào là quan sát, tập hành động nào khả dụng và phần thưởng phản ánh mục tiêu nào; nhiều mô hình được chấp nhận nếu bốn thành phần nhất quán.)

::: solution
Lời giải tóm tắt: (1) mô hình có thể sai khi môi trường đổi hoặc không bao phủ không gian lớn; (2) hành động hiện tại làm đổi trạng thái và quan sát tiếp theo, nên các mẫu không thể tráo tùy ý; (3) hành động sớm chỉ được đánh giá sau khi quan sát hậu quả về sau; (4) chính sách chọn hành động, hàm giá trị đánh giá tương lai, mô hình dự báo thay đổi và là tùy chọn; (5) thăm dò thu thập thông tin, khai thác dùng hiểu biết hiện có; (6) xem gợi ý ở câu 6, chấp nhận mọi mô hình nhất quán giữa bốn thành phần.
:::

## Thảo luận mở rộng (không kết luận)

- **Tác tử tổng quát:** so sánh robot dọn nhà chuyên biệt với robot đa nhiệm về môi trường, dữ liệu tương tác và khả năng chuyển giao. Nguồn trang 14–15 và 43–44 nêu một quan điểm gắn Học tăng cường với AGI và foundation agent; bài này không kiểm chứng quan điểm đó, và không suy từ thành tích ở một nhiệm vụ sang trí tuệ tổng quát.
- **Mô hình thế giới:** mô hình môi trường cho phép dự báo hậu quả và thử kế hoạch mà không thực thi mọi hành động; sai số tích lũy có thể dẫn tới kế hoạch kém. Phân biệt khả năng dự báo với khả năng chọn hành động. Không có cơ sở từ nguồn để khẳng định AGI bắt buộc phải có mô hình thế giới.

## Tài liệu tham khảo

- Sutton, R. S. & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. Chương 1. https://incompleteideas.net/book/the-book-2nd.html
- Silver, D. *Introduction to Reinforcement Learning*, Lecture 1. https://www.davidsilver.uk/teaching/
- Silver, D. và cộng sự (2016). *Mastering the game of Go with deep neural networks and tree search*. Nature. https://doi.org/10.1038/nature16961
- Nguồn bài giảng: `RL-hk2-2025-2026/lecture1-introduction-to-RL.pptx`, 45 trang, tháng 02/2026 (Ta Viet Cuong, HMI laboratory, UET; slide chuyển thể từ davidsilver.uk/teaching/). Các trích dẫn "PPTX nguồn, trang N" trong bài dùng số trang của tệp này.
