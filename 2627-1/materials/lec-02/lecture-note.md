# Bài 02 — Giao diện tác tử–môi trường và các khái niệm MDP nền tảng

## Mục tiêu và kiến thức tiên quyết

Sau bài này, người học làm được:

1. Phân biệt Học tăng cường với học có giám sát và học không giám sát qua nguồn tín hiệu, độ trễ và phụ thuộc thời gian.
2. Mô tả đúng chu kỳ tác tử–môi trường và chỉ số $S_t, A_t, R_{t+1}$.
3. Phân biệt trạng thái với quan sát, phát biểu tính Markov và nhận dạng quan sát đầy đủ/một phần.
4. Định nghĩa chính sách, hàm giá trị và mô hình; phân biệt dự đoán với điều khiển.
5. Mô hình hóa mê cung bằng không gian trạng thái, hành động, chuyển tiếp, phần thưởng và điều kiện kết thúc.

Kiến thức tiên quyết: xác suất cơ bản (biến ngẫu nhiên, xác suất có điều kiện, kỳ vọng), tổng cấp số nhân và khái niệm hàm. Các kiến thức này được giải thích ngắn trước lần dùng đầu: xác suất có điều kiện và kỳ vọng được nhắc lại trước khi dùng ở topic 01 và topic 03; công thức tổng của cấp số nhân được nhắc lại trước khi dùng ở topic 07. Bài này không giả định người học đã biết phương trình Bellman; phương trình Bellman kỳ vọng/tối ưu, MRP và $q_\pi$ không thuộc nội dung cốt lõi của bài và sẽ được dạy ở bài sau.

## Bản đồ chủ đề

### Cốt lõi

| ID | Chủ đề | Nguồn | Bài tập |
|---|---|---|---|
| `lec-02-topic-01` | Tín hiệu học và giả thuyết phần thưởng | PPTX trang 4, 7–9 | hw02 Bài 1 |
| `lec-02-topic-02` | Giao diện tác tử–môi trường | PPTX trang 14–15 | — |
| `lec-02-topic-03` | Trạng thái, quan sát và tính Markov | PPTX trang 16–17 | — |
| `lec-02-topic-04` | Quan sát đầy đủ và quan sát một phần | PPTX trang 18–19, 27 | hw02 Bài 2 (dùng ở topic 04 để phân biệt quan sát và trạng thái) |
| `lec-02-topic-05` | Ba thành phần của tác tử | PPTX trang 10, 20 | — |
| `lec-02-topic-06` | Chính sách xác định và ngẫu nhiên | PPTX trang 21 | hw02 Bài 6 |
| `lec-02-topic-07` | Hàm giá trị và mô hình | PPTX trang 22–23 | hw02 Bài 5 |
| `lec-02-topic-08` | Dự đoán và điều khiển | PPTX trang 24 | — |
| `lec-02-topic-09` | Mê cung như bài toán tổng hợp | PPTX trang 25–27 | hw02 Bài 2 (được áp dụng tổng hợp ở topic này) |

### Cầu nối

| ID | Chủ đề | Nguồn |
|---|---|---|
| `lec-02-topic-10` | Từ lịch sử tới trạng thái Markov | PPTX trang 15–17 |

### Bổ sung

| ID | Chủ đề | Nguồn |
|---|---|---|
| `lec-02-topic-11` | Mô hình thế giới và giới hạn biểu diễn | PPTX trang 13, 19, 23 |

### Đọc thêm

| ID | Chủ đề | Nguồn |
|---|---|---|
| `lec-02-topic-12` | Tài liệu và bài tập mở rộng | Sutton & Barto (dẫn ở trang 15); Silver (dẫn ở trang 1); hw02 Bài 10 |

Thứ tự học: topic 01 → 02 → 10 → 03 → 04 → 05 → 06 → 07 → 11 → 08 → 09 → tự kiểm tra → 12. Topic 02 và 10 gộp thành một cụm vì cùng dùng lịch sử $H_t$; topic 05–08 gộp thành cụm thành phần tác tử; topic 09 là ứng dụng và kiểm tra tổng hợp của topic 02–08.

## Ký hiệu và quy ước

| Ký hiệu | Ý nghĩa |
|---|---|
| $t$ | Chỉ số thời gian; $t = 0, 1, 2, \ldots$; trong nhiệm vụ hữu hạn, $T$ là chỉ số của trạng thái kết thúc. |
| $S_t$ | Trạng thái môi trường tại bước $t$; $S_t \in \mathcal S$. |
| $A_t$ | Hành động tại bước $t$; $A_t \in \mathcal A$ (hoặc $A_t \in \mathcal A(s)$ khi tập hành động phụ thuộc trạng thái). |
| $R_{t+1}$ | Phần thưởng môi trường trả sau hành động $A_t$; $R_{t+1} \in \mathbb R$, chỉ số gắn với chuyển tiếp vừa xảy ra. |
| $H_t$ | Lịch sử đến bước $t$: $H_t = (S_0, A_0, R_1, S_1, \ldots, A_{t-1}, R_t, S_t)$. |
| $O_t$ | Quan sát tác tử nhận tại bước $t$; dùng riêng cho trường hợp quan sát một phần, không đồng nhất với $S_t$. |
| $\pi$ | Chính sách. |
| $G_t$ | Tổng phần thưởng chiết khấu. |
| $v_\pi(s)$ | Hàm giá trị trạng thái dưới $\pi$. |
| $P^a_{ss'}$, $R^a_s$ | Mô hình chuyển và thưởng của môi trường. |
| $\mathbb E_\pi[\cdot]$ | Kỳ vọng lấy theo mọi nguồn ngẫu nhiên sau điều kiện hóa: cách $\pi$ chọn hành động và cách môi trường sinh chuyển tiếp và phần thưởng. |

Quy ước chu kỳ (đã sửa so với nguồn, xem mục "Sai khác có chủ ý"): ở bước $t$, tác tử nhận $S_t$ và phần thưởng $R_t$ từ chuyển tiếp trước, rồi chọn $A_t$; môi trường nhận $A_t$, chuyển sang $S_{t+1}$ và phát $R_{t+1}$.

<!-- note-topic-id: lec-02-topic-01 -->
## Tín hiệu học và giả thuyết phần thưởng

**Vấn đề.** Tác tử phải chọn hành động liên tục nhưng không có nhãn "hành động đúng" cho từng bước. Cần xác định tín hiệu nào hướng dẫn việc chọn, và tín hiệu đó khác gì tín hiệu của học có giám sát và học không giám sát.

**Trực giác.** Trong học có giám sát, mỗi mẫu đi kèm đáp án đúng nên sai số tính được ngay trên từng mẫu. Trong học không giám sát, dữ liệu không kèm nhãn và thuật toán tìm cấu trúc bên trong. Trong Học tăng cường, tín hiệu duy nhất là phần thưởng: nó đến trễ sau một chuỗi hành động, và dữ liệu tương tác không thỏa giả thiết độc lập cùng phân phối (i.i.d.) vì hành động ở bước trước làm đổi tình huống ở bước sau.

**Ví dụ tính được.** Xét một tác tử điều hướng nhận phần thưởng $-1$ mỗi bước, kể cả bước đến đích. Đường đi dài 5 bước cho tổng phần thưởng $(-1) \times 5 = -5$; đường đi dài 3 bước cho $-3$. Tác tử không được nói "bước này đúng hay sai", nhưng so sánh tổng phần thưởng của hai đường cho biết đường nào tốt hơn. Tín hiệu học vì thế là một số vô hướng gắn với kết quả dài hạn, không phải nhãn từng bước.

**Hình thức.** Mục tiêu của tác tử là cực đại hóa kỳ vọng của tổng phần thưởng tích lũy:

$$\max_\pi \; \mathbb E_\pi[G_t].$$

Ở đây $G_t$ là tổng phần thưởng chiết khấu, được định nghĩa hình thức ở topic 07; tại đây chỉ cần hiểu là "tổng phần thưởng tích lũy trong tương lai".

Giả thuyết phần thưởng phát biểu: mọi mục tiêu có thể được mô tả bằng cực đại hóa kỳ vọng của phần thưởng tích lũy. Phát biểu này có điều kiện: nó đúng cho các bài toán mà mục tiêu mã hóa được bằng một tín hiệu vô hướng tích lũy; cách đặt phần thưởng sai có thể tạo hành vi ngoài ý muốn.

**Ứng dụng và giới hạn.** Tiêu chí nhận dạng Học tăng cường: tác tử tác động lên dữ liệu tương lai và chỉ nhận phản hồi sau một chuỗi hành động. Giới hạn: một hệ thống thực có thể kết hợp nhiều dạng học; giả thuyết phần thưởng là phát biểu mô hình hóa, không phải định lý rằng mọi mục tiêu đều mã hóa trọn vẹn.

**Kiểm tra.** Một hệ thống chấm điểm bài luận với đáp án chuẩn cho từng bài: đó là học có giám sát hay Học tăng cường? Vì sao?

::: solution
Trả lời: học có giám sát, vì đáp án chuẩn là tín hiệu mục tiêu trực tiếp cho từng mẫu, không phải phản hồi trễ qua tương tác. Học tăng cường chỉ có phần thưởng vô hướng đến sau chuỗi hành động và dữ liệu phụ thuộc thời gian.
:::

<!-- note-topic-id: lec-02-topic-02 -->
## Giao diện tác tử–môi trường

**Vấn đề.** Cần một khung hình thức chung mô tả mọi bài toán Học tăng cường: ai làm gì, tại thời điểm nào, và đại lượng nào đi theo hướng nào.

**Trực giác.** Tác tử và môi trường tương tác theo vòng lặp. Ở bước $t$: tác tử nhận $S_t$ và phần thưởng $R_t$ từ chuyển tiếp trước, rồi chọn $A_t$. Môi trường nhận $A_t$, chuyển sang $S_{t+1}$ và phát $R_{t+1}$. Vòng lặp lặp lại; mỗi vòng gồm một hành động của tác tử và một chuyển tiếp của môi trường.

**Ví dụ tính được.** Robot trong mê cung ở ô $(1,1)$ tại $t=0$: tác tử nhận $S_0 = (1,1)$ (chưa có $R_0$ vì chưa có chuyển tiếp trước), chọn $A_0 = $ Đông. Môi trường chuyển robot sang $(2,1)$ và phát $R_1 = -1$. Tại $t=1$, tác tử nhận $S_1 = (2,1)$ và $R_1 = -1$, chọn $A_1$. Lịch sử sau hai bước là $H_2 = (S_0, A_0, R_1, S_1, A_1, R_2, S_2)$.

**Hình thức.** Các đại lượng và miền của chúng:

- $S_t \in \mathcal S$: trạng thái môi trường tại bước $t$.
- $A_t \in \mathcal A$: hành động của tác tử tại bước $t$.
- $R_{t+1} \in \mathbb R$: phần thưởng môi trường phát sau hành động $A_t$.
- Lịch sử: $H_t = (S_0, A_0, R_1, S_1, \ldots, A_{t-1}, R_t, S_t)$.

Chỉ số của phần thưởng là $R_{t+1}$ chứ không phải $R_t$ vì phần thưởng gắn với chuyển tiếp do $A_t$ gây ra, tức kết quả của hành động vừa chọn.

**Ứng dụng và giới hạn.** Ứng dụng: khung này là khung đặc tả chung cho các bài toán Học tăng cường; một đặc tả đầy đủ thường gồm $\mathcal S$, $\mathcal A$, quy tắc chuyển tiếp, phần thưởng, cách quan sát (đầy đủ hay một phần), điều kiện kết thúc/tiếp diễn, và hệ số chiết khấu $\gamma$ khi phù hợp. Đây là khung đặc tả, không phải chứng minh rằng mọi bài toán đều đặc tả được trọn vẹn theo cách này. Giới hạn: khung chưa nói gì về cách tác tử quyết định; các thành phần quyết định ở topic 05–08.

**Kiểm tra.** Trong chu kỳ trên, vì sao phần thưởng sau hành động $A_t$ được viết là $R_{t+1}$ thay vì $R_t$?

::: solution
Trả lời: vì phần thưởng là kết quả của chuyển tiếp do $A_t$ gây ra, xảy ra cùng lúc với việc môi trường chuyển sang $S_{t+1}$; chỉ số $t+1$ gắn phần thưởng với chuyển tiếp vừa xảy ra, còn $R_t$ đã được tác tử nhận trước khi chọn $A_t$.
:::

<!-- note-topic-id: lec-02-topic-10 -->
## Cầu nối: từ lịch sử tới trạng thái Markov

Nguồn đặt lịch sử ở trang 15 rồi chuyển ngay sang tính Markov ở trang 17 mà không giải thích quan hệ giữa hai khái niệm. Khoảng trống cần lấp: khi nào có thể thay $H_t$ bằng $S_t$ trong điều kiện hóa?

Lịch sử $H_t$ chứa mọi thứ đã xảy ra, nên điều kiện hóa theo $H_t$ luôn đúng nhưng cồng kềnh: chiều dài của $H_t$ tăng theo thời gian và các lịch sử khác nhau gần như không lặp lại. Trạng thái $S_t$ hữu ích khi nó là bản tóm tắt đủ của lịch sử: mọi thông tin trong $H_t$ có ảnh hưởng đến tương lai đều đã nằm trong $S_t$. Khi đó, điều kiện hóa theo $S_t$ (và $A_t$) cho cùng kết quả dự báo như điều kiện hóa theo $H_t$ (và $A_t$), và ta viết được công thức Markov ở topic 03. Nếu $S_t$ bỏ sót thông tin liên quan (ví dụ vận tốc của vật thể khi động lực học phụ thuộc vận tốc), thay $H_t$ bằng $S_t$ làm mất thông tin và giả thiết Markov sai.

**Kiểm tra.** Một môi trường mà chuyển tiếp kế tiếp phụ thuộc cả vị trí lẫn vận tốc, nhưng trạng thái chỉ ghi vị trí. Có thể thay $H_t$ bằng $S_t$ trong điều kiện hóa không?

::: solution
Trả lời: không; $S_t$ bỏ sót vận tốc là thông tin liên quan đến tương lai, nên $S_t$ không phải bản tóm tắt đủ của $H_t$ và giả thiết Markov không thỏa khi điều kiện hóa chỉ theo $S_t$.
:::

<!-- note-topic-id: lec-02-topic-03 -->
## Trạng thái, quan sát và tính Markov

**Vấn đề.** Trạng thái môi trường và dữ liệu tác tử nhận về có thể khác nhau. Cần phân biệt hai đại lượng này và phát biểu điều kiện để tương lai chỉ phụ thuộc hiện tại.

**Trực giác.** Trạng thái là mô tả tình huống của môi trường; quan sát là dữ liệu tác tử nhận về tình huống đó. Vị trí thật của một vật là trạng thái; ảnh camera có nhiễu là quan sát. Khi quan sát đủ để xác định trạng thái, hai đại lượng trùng nhau; khi không, tác tử chỉ thấy một phần.

**Ví dụ tính được.** Một xe chạy trên đường: trạng thái gồm vị trí và vận tốc; camera chỉ cho ảnh, tức quan sát. Hai trạng thái khác nhau chỉ ở vận tốc có thể sinh cùng một ảnh, nên từ quan sát không suy ra được trạng thái. Ngược lại, trong cờ vây, thế cờ trên bàn là cả trạng thái lẫn quan sát.

**Hình thức.** Tính Markov phát biểu theo hai dạng:

- Dạng chuỗi trạng thái (như nguồn trang 17), với biến cố đầy đủ và lịch sử bắt đầu ở $S_0$:

$$\Pr(S_{t+1} \mid S_t) = \Pr(S_{t+1} \mid S_0, \ldots, S_t).$$

- Dạng có điều khiển, nối giao diện với tính Markov:

$$\Pr(S_{t+1}, R_{t+1} \mid H_t, A_t) = \Pr(S_{t+1}, R_{t+1} \mid S_t, A_t).$$

Sau khi tính Markov được thiết lập, dạng chuỗi trạng thái thường được viết tắt thành $\Pr(S_{t+1} \mid S_t) = \Pr(S_{t+1} \mid S_1, \ldots, S_t)$, như trong nguồn. Dạng thứ hai là cách nối giao diện tác tử–môi trường với tính Markov: phân phối của trạng thái và phần thưởng kế tiếp, sau khi đã chọn $A_t$, chỉ phụ thuộc $S_t$ chứ không phụ thuộc phần còn lại của lịch sử. Đây là giả thiết về môi trường, không phải về tác tử.

**Ứng dụng và giới hạn.** Ứng dụng: giả thiết Markov cho phép thay $H_t$ bằng $S_t$ trong mọi điều kiện hóa về sau (xem cầu nối topic 10), làm các định nghĩa gọn và tính được. Giới hạn: nhiều môi trường thực không Markov trên không gian trạng thái thô; cần mở rộng trạng thái hoặc dùng lịch sử.

**Kiểm tra.** Viết dạng có điều khiển của tính Markov và cho biết nó khác dạng chuỗi trạng thái ở điểm nào.

::: solution
Trả lời: $\Pr(S_{t+1}, R_{t+1} \mid H_t, A_t) = \Pr(S_{t+1}, R_{t+1} \mid S_t, A_t)$. Khác dạng chuỗi trạng thái ở chỗ có hành động $A_t$ trong điều kiện hóa và có cả phần thưởng $R_{t+1}$ trong vế trái; nó mô tả chuyển tiếp của môi trường sau hành động, không chỉ tiến trình trạng thái thuần túy.
:::

<!-- note-topic-id: lec-02-topic-04 -->
## Quan sát đầy đủ và quan sát một phần

**Vấn đề.** Tác tử có thể nhìn thấy toàn bộ trạng thái môi trường hoặc chỉ một phần; cần phát biểu tiêu chí phân biệt hai trường hợp vì chúng quyết định hình thức bài toán.

**Trực giác.** Trong cờ vây, thế cờ hiển thị đầy đủ: quan sát bằng trạng thái. Trong poker, lá bài của đối thủ là một phần trạng thái: quan sát chỉ là một phần. Hai trường hợp đòi hỏi cách tiếp cận khác nhau vì lượng thông tin cho quyết định khác nhau.

**Ví dụ tính được.** Trong mê cung (sẽ đặc tả ở topic 09), nếu tác tử nhận tọa độ ô hiện tại thì quan sát bằng trạng thái. Nếu tác tử chỉ nhận ảnh từ camera góc nhìn thứ nhất, hai ô khác nhau có thể cho cùng ảnh (tường giống nhau quanh mình), nên quan sát là một phần.

**Hình thức.** Quan sát đầy đủ: quan sát chứa đủ thông tin để khôi phục trạng thái Markov, tức từ $O_t$ (kết hợp với bộ nhớ tác tử nếu cần) xác định được $S_t$, hoặc tương đương, quan sát chứa đủ thông tin dự báo phân phối chuyển tiếp và phần thưởng kế tiếp; trong trường hợp đơn giản viết $O_t = S_t$. Quan sát một phần: không khôi phục được trạng thái Markov từ quan sát; $O_t$ là hàm của trạng thái (có thể nhiều–một) và nhiều trạng thái khác nhau cho cùng quan sát. Khi quan sát một phần, dùng ký hiệu $O_t$ cho quan sát và không đồng nhất $O_t$ với $S_t$.

Lưu ý về phạm vi: quan sát đầy đủ là một điều kiện thường đi kèm bài toán MDP, nhưng không tự nó là định nghĩa đầy đủ của MDP. Đặc tả hình thức của MDP (gồm không gian trạng thái, chuyển tiếp, phần thưởng và chính sách) được trình bày ở bài tiếp theo.

**Ứng dụng và giới hạn.** Ứng dụng: nhận dạng quan sát đầy đủ/một phần là bước đầu khi mô hình hóa một bài toán mới. Giới hạn: ranh giới phụ thuộc cách chọn trạng thái; cùng một bài toán có thể quan sát đầy đủ trên một không gian trạng thái giàu và một phần trên không gian thô.

**Kiểm tra.** Một robot chỉ nhận khoảng cách tới tường phía trước. Quan sát của nó đầy đủ hay một phần? Nếu môi trường chỉ có một hành lang thẳng không có đặc điểm phân biệt, câu trả lời đổi không?

::: solution
Trả lời: nói chung là một phần, vì nhiều vị trí khác nhau cho cùng khoảng cách. Trong hành lang thẳng không đặc điểm, nếu động lực học và phần thưởng chỉ phụ thuộc khoảng cách tới tường thì khoảng cách chứa đủ thông tin dự báo, nên trên không gian trạng thái rút gọn này quan sát đủ cho quyết định; đánh giá phải xét đủ thông tin dự báo, không chỉ kiểu dữ liệu.
:::

<!-- note-topic-id: lec-02-topic-05 -->
## Ba thành phần của tác tử

**Vấn đề.** Giao diện xác định tác tử làm gì (chọn $A_t$), nhưng chưa nói tác tử quyết định bằng cách nào. Cần đặt tên cho các thành phần bên trong tác tử.

**Trực giác.** Ba câu hỏi khác nhau: "làm gì bây giờ?", "tình huống này đáng giá bao nhiêu?", "nếu làm X thì chuyện gì xảy ra?". Mỗi câu hỏi tương ứng một thành phần: chính sách, hàm giá trị, mô hình.

**Ví dụ tính được.** Robot giao hàng: chính sách trả lời "ở ngã ba này, rẽ phải"; hàm giá trị trả lời "ô này còn cách đích khoảng 10 bước, mỗi bước thưởng $-1$, nên giá trị khoảng $-10$"; mô hình trả lời "nếu đi Đông từ ô $(2,3)$ thì sang ô $(3,3)$ và mất 1 điểm". Ba câu trả lời có thể tồn tại độc lập.

**Hình thức.**

- **Chính sách** $\pi$: ánh xạ từ trạng thái (hoặc quan sát) sang hành động hoặc phân phối hành động; quyết định hành vi.
- **Hàm giá trị**: đánh giá kết quả tương lai kỳ vọng của một trạng thái dưới một chính sách; đo độ tốt.
- **Mô hình**: dự báo chuyển tiếp và phần thưởng kế tiếp của môi trường; dùng để lập kế hoạch. Các đại lượng $P^a_{ss'}$ và $R^a_s$ của mô hình được định nghĩa ở topic 07.

Không phải mọi thuật toán Học tăng cường đều dùng cả ba: tác tử phi mô hình học chính sách hoặc giá trị mà không có mô hình tường minh; một số phương pháp chỉ học chính sách. Mô hình là thành phần tùy chọn.

**Ứng dụng và giới hạn.** Bản đồ vai trò này dùng để phân loại thuật toán ở các bài sau. Giới hạn: bài này mới định nghĩa vai trò, chưa định nghĩa cách học từng thành phần.

**Kiểm tra.** Một tác tử chỉ có chính sách, không có hàm giá trị và mô hình. Nó thiếu năng lực gì so với tác tử có đủ ba thành phần?

::: solution
Trả lời: thiếu khả năng đánh giá độ tốt của tình huống (hàm giá trị) và khả năng dự báo hậu quả hành động để lập kế hoạch (mô hình); nó vẫn chọn được hành động nhưng không đánh giá hay lập kế hoạch bằng các thành phần đó.
:::

<!-- note-topic-id: lec-02-topic-06 -->
## Chính sách xác định và ngẫu nhiên

**Vấn đề.** Chính sách cần được định nghĩa hình thức, gồm cả trường hợp chọn hành động ngẫu nhiên.

**Trực giác.** Ở một ngã ba, tác tử có thể luôn rẽ phải (quyết định cứng), hoặc tung đồng xu rồi rẽ trái hoặc phải với xác suất bằng nhau. Cả hai đều là cách chọn hành động hợp lệ; cái sau hữu ích khi cần thăm dò.

**Ví dụ tính được.** Ví dụ hai hành động với xác suất 0,5 trong nguồn; dữ kiện phần thưởng sau đây là ví dụ tự đặt, không phải dữ kiện nguồn. Tại trạng thái $s$, chính sách ngẫu nhiên chọn Bắc với xác suất $0{,}5$ và Đông với xác suất $0{,}5$; đặt thưởng Bắc $= 2$, Đông $= -1$. Kỳ vọng phần thưởng tức thời là $0{,}5 \times 2 + 0{,}5 \times (-1) = 0{,}5$. Tổng xác suất bằng $1$. Chính sách xác định tương ứng chọn Bắc với xác suất $1$.

**Hình thức.** Chính sách xác định và chính sách ngẫu nhiên là hai loại chính sách khác nhau, với hai ký hiệu riêng (không mâu thuẫn):

- Chính sách xác định: $\pi(s) = a$, một hàm từ trạng thái sang hành động; ký hiệu $\pi(s)$ chỉ dùng cho loại này.
- Chính sách ngẫu nhiên:

$$\pi(a \mid s) = \Pr(A_t = a \mid S_t = s), \qquad \sum_{a \in \mathcal A} \pi(a \mid s) = 1, \quad \pi(a \mid s) \ge 0.$$

Miền: $\pi(\cdot \mid s)$ là phân phối xác suất trên $\mathcal A(s)$ tại mỗi $s$; điều kiện chuẩn hóa là tổng xác suất trên các hành động hợp lệ bằng $1$. Chính sách xác định là trường hợp riêng với $\pi(a \mid s) \in \{0, 1\}$.

**Ứng dụng và giới hạn.** Ứng dụng: chính sách ngẫu nhiên hỗ trợ thăm dò và phá vỡ đối xứng; chính sách xác định gọn khi hành vi đã cố định. Giới hạn: chính sách ngẫu nhiên có thể mất phần thưởng ngắn hạn so với chọn hành động tốt nhất đã biết.

**Kiểm tra.** Với $\mathcal A(s) = \{\text{Bắc}, \text{Đông}\}$ và $\pi(\text{Bắc} \mid s) = 0{,}3$, giá trị $\pi(\text{Đông} \mid s)$ phải bằng bao nhiêu để $\pi$ là chính sách hợp lệ?

::: solution
Trả lời: $\pi(\text{Đông} \mid s) = 1 - 0{,}3 = 0{,}7$, vì tổng xác suất trên các hành động hợp lệ phải bằng $1$.
:::

<!-- note-topic-id: lec-02-topic-07 -->
## Hàm giá trị và mô hình

**Vấn đề.** Phần thưởng tức thời không đủ để so sánh tình huống: một ô có thưởng $0$ ngay nhưng gần đích có thể tốt hơn ô có thưởng nhỏ ngay nhưng xa đích. Cần đại lượng đo kết quả dài hạn và công cụ dự báo chuyển tiếp.

**Trực giác.** Tổng phần thưởng tương lai cần ưu tiên phần thưởng đến sớm. Hệ số chiết khấu $\gamma \in [0, 1)$ làm phần thưởng ở bước sau nhỏ dần: phần thưởng sau $k$ bước được tính bằng $\gamma^k$ lần. Kỳ vọng cần thiết vì tương lai không xác định: cả cách chính sách chọn hành động lẫn cách môi trường chuyển tiếp đều ngẫu nhiên.

**Ví dụ tính được.** Tính tay với $\gamma = 0{,}5$ và dãy phần thưởng $R_1 = 2$, $R_2 = 4$, các phần thưởng sau bằng $0$:

$$G_0 = R_1 + \gamma R_2 + \gamma^2 R_3 + \cdots = 2 + 0{,}5 \times 4 + 0 = 4.$$

Nếu đổi thứ tự thành $R_1 = 4$, $R_2 = 2$: $G_0 = 4 + 0{,}5 \times 2 = 5$. Phần thưởng đến sớm được chiết khấu ít nên có giá trị lớn hơn; đây là lý do thứ tự thời gian quan trọng.

**Hình thức.** Tổng phần thưởng chiết khấu phụ thuộc loại nhiệm vụ.

Nhiệm vụ tiếp diễn (không có điểm kết thúc): $G_t$ là chuỗi vô hạn,

$$G_t = \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}, \qquad 0 \le \gamma < 1,$$

với $R_{\max}$ là cận trên không âm của $|R_{t+1}|$ với mọi $t$.

Nhiệm vụ hữu hạn kết thúc ở bước $T$: tổng là hữu hạn,

$$G_t = \sum_{k=0}^{T-t-1} \gamma^k R_{t+k+1}, \qquad 0 \le \gamma \le 1.$$

Với nhiệm vụ tiếp diễn, $\gamma = 1$ có thể làm tổng phân kỳ, nên yêu cầu $\gamma < 1$. Điều kiện hội tụ: với $0 \le \gamma < 1$ và phần thưởng bị chặn, chuỗi $\sum_k \gamma^k R_{t+k+1}$ hội tụ tuyệt đối vì tổng hình học $\sum_{k=0}^{\infty} \gamma^k = \frac{1}{1-\gamma}$ với $0 \le \gamma < 1$; giá trị bị chặn bởi $R_{\max}/(1-\gamma)$.

Hàm giá trị trạng thái dưới chính sách $\pi$:

$$v_\pi(s) = \mathbb E_\pi\!\left[G_t \mid S_t = s\right] = \mathbb E_\pi\!\left[R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots \mid S_t = s\right].$$

Kỳ vọng $\mathbb E_\pi$ lấy theo chính sách $\pi$ (cách chọn hành động) và động lực môi trường (cách chuyển tiếp và phát thưởng). Hàm giá trị luôn phụ thuộc chính sách đang được đánh giá; đổi $\pi$ là đổi $v_\pi$.

Mô hình của môi trường gồm chuyển tiếp và thưởng:

$$P^a_{ss'} = \Pr(S_{t+1} = s' \mid S_t = s, A_t = a), \qquad R^a_s = \mathbb E\!\left[R_{t+1} \mid S_t = s, A_t = a\right].$$

Cả hai đều điều kiện hóa theo cặp (trạng thái, hành động); $P^a_{ss'}$ là phân phối xác suất trên $\mathcal S$ nên $\sum_{s'} P^a_{ss'} = 1$ với mỗi $(s, a)$.

Bài này không trình bày phương trình Bellman kỳ vọng hay tối ưu; quan hệ đệ quy của $v_\pi$ thuộc bài sau.

**Ứng dụng và giới hạn.** Ứng dụng: $v_\pi$ dùng để so sánh trạng thái và đánh giá chính sách; $P^a_{ss'}$ và $R^a_s$ dùng để lập kế hoạch khi biết trước động lực học. Giới hạn: tính $v_\pi$ chính xác đòi hỏi biết mô hình hoặc thu thập dữ liệu; bài này chỉ định nghĩa, chưa chỉ cách tính.

**Kiểm tra.** Với $\gamma = 0{,}5$, $R_1 = 0$, $R_2 = 8$, các phần thưởng sau bằng $0$: tính $G_0$. Nếu $\gamma = 0$ thì $G_0$ bằng bao nhiêu?

::: solution
Trả lời: $G_0 = 0 + 0{,}5 \times 8 = 4$. Với $\gamma = 0$: $G_0 = R_1 = 0$, vì mọi phần thưởng sau bước đầu bị triệt tiêu; $\gamma = 0$ tương ứng chỉ quan tâm phần thưởng tức thời.
:::

<!-- note-topic-id: lec-02-topic-11 -->
## Bổ sung: mô hình thế giới và giới hạn biểu diễn

Nguồn đặt câu hỏi về "mô hình thế giới" ở trang 13, trước khi định nghĩa mô hình ở trang 23, và không có khung trả lời. Sau khi đã có định nghĩa ở topic 07, câu hỏi trả lời được như sau.

Mô hình ở topic 07 là mô hình dự báo cục bộ có điều kiện: với mỗi cặp $(s, a)$, nó dự báo phân phối trạng thái kế tiếp và phần thưởng kỳ vọng. Đây là một công cụ tính toán, không phải "mô hình hoàn thiện về thế giới": nó chỉ đúng trong phạm vi các trạng thái và hành động đã đặc tả, chỉ dự báo một bước (trừ khi ghép nhiều bước), và mang sai số nếu được học từ dữ liệu. Một hệ thống có thể hành xử tốt mà không có mô hình tường minh (học chính sách hoặc giá trị trực tiếp từ tương tác), và một hệ thống có mô hình vẫn có thể lập kế hoạch kém nếu mô hình sai. Do đó không kết luận rằng trí tuệ nhân tạo tổng quát bắt buộc phải có mô hình tường minh; đây là lựa chọn thiết kế phụ thuộc bài toán và dữ liệu sẵn có.

**Kiểm tra.** Phân biệt "mô hình dự báo cục bộ có điều kiện" với "mô hình hoàn thiện về thế giới" bằng hai tiêu chí cụ thể.

::: solution
Trả lời: phạm vi — mô hình cục bộ chỉ dự báo với các cặp $(s,a)$ đã đặc tả, mô hình hoàn thiện phải bao quát mọi tình huống; độ tin cậy — mô hình cục bộ có sai số đo được và chỉ dự báo một bước, mô hình hoàn thiện được giả định đúng trên mọi độ dài kế hoạch. Nguồn không cung cấp cơ sở để khẳng định hệ AI bắt buộc cần mô hình tường minh.
:::

<!-- note-topic-id: lec-02-topic-08 -->
## Dự đoán và điều khiển

**Vấn đề.** Với các thành phần đã định nghĩa, có hai nhiệm vụ khác nhau cần phân biệt rõ để tránh nhầm khi đọc thuật toán ở các bài sau.

**Trực giác.** Đánh giá một cầu thủ cụ thể và tìm cầu thủ tốt nhất là hai việc khác nhau. Việc đầu giữ chính sách cố định rồi đo giá trị; việc thứ hai thay đổi chính sách để giá trị tăng.

**Ví dụ tính được.** Cho mê cung với thưởng $-1$ mỗi bước và một chính sách luôn đi Đông. Dự đoán: tính $v_\pi$ cho chính sách đó — kết quả có thể kém vì chính sách đâm vào tường. Điều khiển: đổi chính sách (ví dụ thêm rẽ khi gặp tường) để $v_\pi$ tăng. Cùng dữ kiện mê cung, hai nhiệm vụ cho hai câu hỏi khác nhau.

**Hình thức.**

- **Dự đoán** (evaluation): cho trước chính sách $\pi$, tính $v_\pi(s) = \mathbb E_\pi[G_t \mid S_t = s]$ cho các $s$. Đầu vào là $\pi$; đầu ra là hàm giá trị.
- **Điều khiển** (control): tìm hoặc cải thiện chính sách để đạt giá trị cao; đầu ra là một chính sách tốt hơn (trong phạm vi đã xét).

Không đồng nhất "chơi tốt nhất" với dự đoán: nếu chính sách chưa cố định thì chưa có gì để đánh giá; phải trước hết xác định $\pi$ đang xét hoặc chuyển sang bài toán điều khiển.

**Ứng dụng và giới hạn.** Ứng dụng: hầu hết thuật toán Học tăng cường xen kẽ hai nhiệm vụ này. Giới hạn: bài này chưa trình bày thuật toán cho cả hai; chỉ xác lập sự phân biệt.

**Kiểm tra.** Một người nói "tôi dùng dự đoán để tìm chính sách tốt nhất". Phát biểu đó sai ở đâu?

::: solution
Trả lời: dự đoán đánh giá một chính sách đã cho, không tìm chính sách; tìm chính sách tốt hơn là điều khiển. Nếu chính sách chưa cố định thì không có đối tượng để dự đoán.
:::

<!-- note-topic-id: lec-02-topic-09 -->
## Mê cung như bài toán tổng hợp

**Vấn đề.** Cần đặc tả một bài toán hoàn chỉnh bằng mọi khái niệm từ topic 02 đến topic 08, để kiểm tra rằng các định nghĩa dùng được cùng nhau.

**Trực giác.** Mê cung gồm các ô, tường và một ô đích. Tác tử đứng ở một ô, chọn một trong bốn hướng; môi trường di chuyển tác tử theo hướng đó nếu không gặp tường, trừ một điểm mỗi bước, và kết thúc khi đến đích.

**Ví dụ tính được.** Ví dụ sau là dữ kiện tự đặt để tính tay, với bố cục một hành lang ba ô: các ô $s_1, s_2, s_3$, tường hai đầu, đích là $s_3$, thưởng $R_{t+1} = -1$ mỗi bước, $\gamma = 1$ (nhiệm vụ hữu hạn; điều này được phép vì tổng chỉ có hữu hạn số hạng). Xét hai chính sách: (a) chính sách xác định luôn đi Đông; (b) chính sách chọn đều Đông/Tây tại $s_1$ và luôn đi Đông ở các ô khác.

Dưới chính sách (a): từ $s_1$ cần 2 bước tới đích, tổng phần thưởng $G_0 = (-1) + (-1) = -2$; từ $s_2$ cần 1 bước, $G_0 = -1$. Vậy $v_\pi(s_1) = -2$ và $v_\pi(s_2) = -1$ dưới chính sách này.

Dưới chính sách (b) tại $s_1$: với xác suất $0{,}5$ đi Đông tới $s_2$ (sau đó luôn Đông, còn $-1$), với xác suất $0{,}5$ đâm tường ở lại $s_1$ (chuỗi lặp); kỳ vọng khi đó không tính được bằng hai đường hữu hạn trên mà cần giải phương trình theo định nghĩa kỳ vọng, và bài này dừng ở việc chỉ ra rằng giá trị phụ thuộc chính sách.

**Hình thức.** Đặc tả mê cung:

- Không gian trạng thái: $\mathcal S$ là tập các ô không phải tường; $S_t$ là vị trí tác tử tại bước $t$.
- Hành động: $\mathcal A(s) = \{\text{Bắc}, \text{Đông}, \text{Nam}, \text{Tây}\}$ tại mỗi ô; quy tắc chuyển khi gặp tường: hành động hướng vào tường giữ tác tử ở nguyên chỗ, tức $P^a_{ss} = 1$ cho hành động $a$ hướng tường tại ô $s$ sát tường.
- Phần thưởng: $R_{t+1} = -1$ mỗi bước, kể cả bước đâm tường; mục tiêu là đến đích với ít bước nhất.
- Kết thúc: trạng thái đích là trạng thái kết thúc; nhiệm vụ hữu hạn kết thúc khi đến đích.

So sánh đầu vào: nếu tác tử nhận tọa độ ô đầy đủ thì quan sát bằng trạng thái (quan sát đầy đủ). Nếu tác tử chỉ nhận ảnh hoặc cảm biến góc nhìn thứ nhất, hai vị trí khác nhau có thể cho cùng dữ liệu cảm biến, nên quan sát có thể là một phần. Kết luận về đầy đủ hay một phần không dựa vào kiểu dữ liệu (tọa độ hay ảnh) mà phải xét đủ thông tin dự báo: dữ liệu đó có xác định được phân phối chuyển tiếp và phần thưởng kế tiếp hay không.

**Ứng dụng và giới hạn.** Ứng dụng: khuôn này dùng để mô hình hóa mọi bài toán điều hướng và là bài tập nền cho hw02. Giới hạn: nguồn trình bày mê cung kèm đồ thị chuyển và bảng đánh số trạng thái ở dạng hình; bản note không dùng ảnh raster và không suy diễn đường đi cụ thể từ hình khi không đọc chắc chắn được, nên ví dụ tính tay ở trên dùng bố cục tự đặt.

**Kiểm tra.** Trong mê cung ba ô ở ví dụ trên, tác tử ở $s_2$ dưới chính sách luôn đi Đông. Tính $G_0$ và cho biết vì sao $v_\pi(s_2) \neq v_\pi(s_1)$ dưới cùng chính sách.

::: solution
Trả lời: từ $s_2$, đi Đông một bước tới đích, $G_0 = -1$. Dưới chính sách luôn đi Đông, từ $s_1$ cần 2 bước nên $G_0 = -2$. Hai giá trị khác nhau vì khoảng cách tới đích khác nhau; $v_\pi$ đo kết quả dài hạn từ từng trạng thái, không phải một số chung cho cả mê cung.
:::

## Tổng kết bài

- Học tăng cường khác học có giám sát và học không giám sát ở tín hiệu phần thưởng trễ, dữ liệu phụ thuộc thời gian và việc tác tử tác động lên dữ liệu tương lai.
- Tác tử và môi trường trao đổi theo chu kỳ: tác tử nhận $S_t$ và $R_t$, chọn $A_t$; môi trường chuyển sang $S_{t+1}$ và phát $R_{t+1}$.
- Trạng thái hữu ích khi là bản tóm tắt đủ của lịch sử; khi đó tính Markov cho phép điều kiện hóa theo $S_t$ thay vì $H_t$.
- Tác tử gồm chính sách (quyết định), hàm giá trị (đánh giá) và mô hình (dự báo); ba thành phần không bắt buộc đồng thời.
- Dự đoán đánh giá một chính sách đã cho; điều khiển tìm chính sách tốt hơn — mê cung là bài toán tổng hợp để áp dụng cả các khái niệm trên.

## Tự kiểm tra và bài tập

Các câu sau tổng hợp nội dung bài; đáp án tách khỏi câu hỏi ở cuối mục.

1. Nêu ba khác biệt giữa Học tăng cường và học có giám sát. (hw02 Bài 1)
2. Một robot chỉ nhận tín hiệu sonar ba hướng trong mê cung. Trạng thái và quan sát của nó khác nhau thế nào, và bài toán là quan sát đầy đủ hay một phần? (hw02 Bài 2)
3. Viết cả hai dạng tính Markov và cho biết dạng nào gắn với giao diện tác tử–môi trường.
4. Giả sử phần thưởng bị chặn bởi $|R_{t+1}| \le 10$ tại mọi bước và $\gamma = 0{,}9$: giá trị lớn nhất có thể của $G_t$ là bao nhiêu? Căn cứ vào điều kiện gì?
5. Cho $R_1 = 1$, $R_2 = 2$, $R_3 = 4$, $\gamma = 0{,}5$, các phần thưởng sau bằng $0$: tính $G_0$ và $G_1$. (hw02 Bài 5)
6. Tại trạng thái $s$ với $\mathcal A(s) = \{\text{Bắc}, \text{Đông}, \text{Nam}\}$ và $\pi(\text{Bắc} \mid s) = 0{,}2$, $\pi(\text{Đông} \mid s) = 0{,}5$: tính $\pi(\text{Nam} \mid s)$ và cho biết đây là chính sách xác định hay ngẫu nhiên. (hw02 Bài 6)
7. Phân biệt dự đoán và điều khiển bằng một câu mỗi nhiệm vụ.
8. Đặc tả mê cung ở topic 09 bằng năm thành phần: $\mathcal S$, $\mathcal A(s)$, quy tắc chuyển khi gặp tường, phần thưởng và điều kiện kết thúc.
9. (Đọc thêm) hw02 Bài 10 yêu cầu làm gì, và nó xếp vào nhóm bài tập nào của bài này?

::: solution
Đáp án: (1) không có nhãn đúng từng mẫu, chỉ có phần thưởng; phản hồi trễ sau chuỗi hành động; dữ liệu không i.i.d. và phụ thuộc thời gian. (2) Trạng thái là vị trí thật trong mê cung; quan sát là ba số đo sonar; nhiều vị trí cho cùng ba số đo nên quan sát là một phần. (3) $\Pr(S_{t+1} \mid S_t) = \Pr(S_{t+1} \mid S_1, \ldots, S_t)$ và $\Pr(S_{t+1}, R_{t+1} \mid H_t, A_t) = \Pr(S_{t+1}, R_{t+1} \mid S_t, A_t)$; dạng thứ hai gắn với giao diện vì có $A_t$ và $R_{t+1}$. (4) $10/(1 - 0{,}9) = 100$, theo chặn trên của tổng hình học với phần thưởng bị chặn và $\gamma < 1$; giá trị lớn nhất $100$ đạt khi mọi phần thưởng tương lai đều bằng cận trên $10$. (5) $G_0 = 1 + 0{,}5 \times 2 + 0{,}25 \times 4 = 3$; $G_1 = 2 + 0{,}5 \times 4 = 4$. (6) $\pi(\text{Nam} \mid s) = 1 - 0{,}2 - 0{,}5 = 0{,}3$; chính sách ngẫu nhiên vì có hành động được chọn với xác suất nằm giữa $0$ và $1$. (7) Dự đoán: cho $\pi$, tính $v_\pi$. Điều khiển: tìm hoặc cải thiện $\pi$ để giá trị tăng. (8) $\mathcal S$ là tập ô không phải tường; $\mathcal A(s) = \{\text{Bắc}, \text{Đông}, \text{Nam}, \text{Tây}\}$; hành động hướng tường giữ nguyên vị trí; $R_{t+1} = -1$ mỗi bước; kết thúc khi đến ô đích. (9) Bài 10 yêu cầu chọn một bài toán thực tế và mô hình hóa bằng trạng thái, hành động, chuyển tiếp, phần thưởng cùng điều kiện kết thúc/tiếp diễn; các khái niệm này đã có trong bài, nên Bài 10 là bài tập mở rộng hợp lệ sau topic 09, không cần $q_\pi$ hay Bellman.
:::

<!-- note-topic-id: lec-02-topic-12 -->
## Đọc thêm

- Sutton, R. S. & Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, Chương 3 (được dẫn ở trang 15 của nguồn): đối chiếu khung tác tử–môi trường và quy ước chỉ số phần thưởng với bài này.
- David Silver, *Introduction to Reinforcement Learning*, Lecture 2 (slide được dẫn ở trang 1 của nguồn): cùng các khái niệm MDP với ví dụ khác; lưu ý bài này chưa đi tới phần Bellman của Lecture 2.
- hw02 Bài 10: bài tập mở rộng hợp lệ sau topic 09 — chọn một bài toán thực tế và mô hình hóa bằng trạng thái, hành động, chuyển tiếp, phần thưởng, điều kiện kết thúc/tiếp diễn; không yêu cầu $q_\pi$ hay Bellman và không cung cấp lời giải trong phạm vi bài này.
- hw02 Bài 1, 2, 5, 6: bài tập chính của bài; Bài 5 và 6 thuộc Bài 02 vì $\gamma$ và chính sách ngẫu nhiên có trong trang 21–22 cùng hw02; Bài 3, 4, 7, 8, 9 đòi hỏi MRP, $q_\pi$ hoặc Bellman, sẽ dùng sau khi các khái niệm đó được dạy.

## Sai khác có chủ ý so với nguồn

- **Sửa chu kỳ trang 15:** nguồn ghi/khó hiểu chu kỳ. Bản note dùng quy ước chuẩn: ở bước $t$, tác tử nhận $S_t$ và $R_t$ từ chuyển tiếp trước, chọn $A_t$; môi trường nhận $A_t$, chuyển sang $S_{t+1}$ và phát $R_{t+1}$; lịch sử $H_t = (S_0, A_0, R_1, S_1, \ldots, A_{t-1}, R_t, S_t)$.
- **Bổ sung điều kiện hội tụ cho tổng vô hạn:** nguồn đưa $G_t$ dạng chuỗi vô hạn mà không nêu điều kiện; bản note thêm $0 \le \gamma < 1$ cùng phần thưởng bị chặn cho nhiệm vụ tiếp diễn, và cho phép $0 \le \gamma \le 1$ với nhiệm vụ hữu hạn.
- **Sửa phát biểu MDP trang 18:** bản note không tuyên bố quan sát đầy đủ tự nó là định nghĩa đầy đủ của MDP; đặc tả hình thức MDP chuyển sang bài tiếp theo.
- **Chuyển câu hỏi mô hình thế giới:** câu hỏi ở trang 13 của nguồn xuất hiện trước định nghĩa mô hình trang 23; bản note chuyển nội dung này tới sau topic 07 (topic 11) để có khung trả lời.
- **Không dùng ảnh:** các trang 5–7, 9, 12, 19, 21, 27 của nguồn chứa nội dung dạng ảnh; bản note không dùng ảnh raster và không suy diễn dữ kiện từ ảnh, gồm đồ thị chuyển và bảng đánh số trạng thái mê cung ở trang 26–27.
- **Ví dụ mê cung tính tay:** bố cục ba ô là dữ kiện tự đặt để tính được, không phải bố cục trong nguồn; điều này được ghi rõ tại chỗ sử dụng.

## Tài liệu tham khảo

- Nguồn bài giảng: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 1–27 (slide chuyển thể từ davidsilver.uk/teaching/). Các trích dẫn "PPTX trang N" trong bài dùng số trang của tệp này.
- Nguồn bài tập: `RL-hk2-2025-2026/resources/hw02.pdf`, Bài 1, 2, 5, 6 (bài tập chính) và Bài 10 (đọc thêm).
- Sutton, R. S. & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). MIT Press. Chương 3. https://incompleteideas.net/book/the-book-2nd.html
- Silver, D. *Introduction to Reinforcement Learning*, Lecture 2. https://www.davidsilver.uk/teaching/
