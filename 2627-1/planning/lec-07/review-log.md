# Nhật ký rà soát Bài 07

## Kiểm kê ban đầu

- Nguồn chính có 45 trang; phiếu bài tập có 3 trang và 8 bài.
- Không có notebook hoặc code demo liên quan trong nguồn.
- Các ảnh minh họa miền ứng dụng và sơ đồ được vẽ lại bằng tám SVG.
- Không dùng ảnh raster và không phụ thuộc tài nguyên mạng.

## Báo cáo lập kế hoạch

Tác tử lập kế hoạch đề nghị giữ Bài 07 trong một buổi. Phần tr. 5–20 lặp kiến thức hội tụ dạng bảng của Bài 06 và chứa một phác thảo chưa đủ chặt, nên được nén thành một cầu nối. Trọng tâm chuyển sang đặc trưng, MC/TD tuyến tính, Bellman chiếu, điều khiển và deadly triad. Kế hoạch 36 trang chính, ba trang bài tập dọc, 110 phút cốt lõi, 10 phút linh hoạt và 30 phút chữa bài đã được điều phối viên chấp nhận.

## Báo cáo ánh xạ nguồn ban đầu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | `L07-02` | Nguồn dùng lịch $\varepsilon_k=1/k$ như thể tự đủ cho GLIE và chuyển luật số lớn của chính sách cố định sang dãy chính sách thay đổi. | lecture-07.pdf, tr. 5–20. | Không trình bày phác thảo này như chứng minh; chỉ nhắc kết quả dạng bảng có điều kiện. |
| nghiêm trọng | `L07-12`–`L07-19` | Nguồn gọi chung cập nhật theo đích là bán gradient. | lecture-07.pdf, tr. 32–35. | Gọi MC là gradient đầy đủ khi $G_t$ không phụ thuộc $w$; chỉ gọi TD là bán gradient. |
| nghiêm trọng | `L07-17`, `L07-24` | Điều kiện hội tụ thiếu chính sách, phân phối lấy mẫu và tính dừng. | lecture-07.pdf, tr. 27, 34–36. | Nêu riêng trường hợp iid và chuỗi Markov trộn; giới hạn TD ở on-policy với chính sách cố định. |
| nghiêm trọng | `L07-10` | Vector đặc trưng hành động trong nguồn ghép các khối có kích thước không rõ. | lecture-07.pdf, tr. 31. | Dùng một mã hóa khối nhất quán $x(s,a)=e_a\otimes\phi(s)\in\mathbb R^{mp}$. |
| trung bình | `L07-27` | Chuỗi A–E không tự bảo đảm tối đa ba bước. | Phiếu bài tập, tr. 2. | Nêu chân trời cưỡng bức hoặc bổ sung thời gian vào trạng thái. |
| trung bình | `L07-32` | Cách diễn đạt nguồn có thể bị hiểu thành cả ba thành phần luôn gây phân kỳ. | lecture-07.pdf, tr. 41. | Dùng “có thể làm một số thuật toán TD phân kỳ”. |
| trung bình | `L07-34` | Bound mẫu ở trang kết thiếu thiết lập và thước đo sai số. | lecture-07.pdf, tr. 44. | Bỏ bound; giữ bảng phạm vi của các kết luận đã xây dựng. |

## Báo cáo phản biện học thuật ban đầu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | `L07-21`–`L07-24` | Phương trình Bellman chiếu dễ thành ký hiệu rời nếu thiếu $D$, $\Phi$, $P_\pi$, $r_\pi$ và giả thiết đủ hạng. | Phiếu bài tập, Bài 5 chỉ cho gợi ý $b-Aw$. | Định nghĩa toàn bộ đối tượng trước phương trình; nối $Aw=b$ với phép chiếu. |
| nghiêm trọng | `L07-28`–`L07-31` | Đặt Q-learning trước SARSA sẽ bỏ cầu nối từ TD theo chính sách. | SARSA dùng đúng mẫu mở rộng $(S,A,R,S',A')$ đã có từ Bài 06. | Dạy SARSA, tính một bước, rồi đổi đích sang cực đại của Q-learning. |
| trung bình | `L07-13` | “Return không chệch” có thể bị hiểu quá rộng. | $\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s)$ chỉ dưới đúng chính sách và return tồn tại. | Gắn phát biểu với chính sách cố định và không suy ra không chệch hữu hạn mẫu của $w$. |
| trung bình | `X02` | Phiếu gọi một lượt cập nhật là MC control nhưng không có bước cải thiện chính sách. | HW7 chỉ yêu cầu cập nhật $w$ trên quỹ đạo cố định. | Gọi đây là cập nhật giá trị hành động MC; ghi rõ chưa phải vòng control hoàn chỉnh. |
| trung bình | `L07-32`–`L07-34` | Công thức đúng riêng lẻ nhưng thiếu cầu nối từ khác chính sách sang bất ổn. | Q-learning dùng cực đại trong khi dữ liệu do hành vi sinh ra. | Đặt Q-learning ngay trước deadly triad và dùng ba câu chẩn đoán. |

## Kiểm tra số

### Bài 7

Return theo thứ tự $(D,0),(C,0),(B,0)$ là $(998,999,1000)$. Cập nhật tuần tự cho:

$$
w_1=(299.5,100.5,98.5)^T,
$$

$$
w_2=(339.7,120.6,118.6)^T,
$$

$$
w_3=(381.81,162.71,160.71)^T.
$$

Giá trị cuối là $\hat q(D,0)=1468.85$, $\hat q(C,0)=1087.04$, $\hat q(B,0)=705.23$.

### Bài 8

Ba cập nhật SARSA cho:

$$
w_1=(-0.2,0.6,-1.4)^T,
$$

$$
w_2=(-0.68,0.84,-1.64)^T,
$$

$$
w_3=(8.032,-2.064,1.264)^T.
$$

Giá trị cuối là $\hat q(D,0)=23.296$, $\hat q(C,1)=19.392$, $\hat q(D,1)=27.424$.

## Sai khác có chủ ý so với nguồn

1. Nén tr. 5–20 thành `L07-02` vì lặp Bài 06 và không đủ chặt để dùng như chứng minh.
2. Tách MC gradient đầy đủ khỏi bán gradient TD.
3. Bổ sung miền, kích thước, phân phối dừng, phép chiếu và điều kiện đủ hạng.
4. Đặt SARSA trước Q-learning để giữ thứ tự theo chính sách rồi khác chính sách.
5. Sửa deadly triad thành phát biểu khả năng, không phải kết quả tất định.
6. Bỏ bound mẫu ở tr. 44 vì nguồn thiếu thiết lập.
7. Không dạy chi tiết LSVI ở tr. 42 vì mệnh đề và trích dẫn không đủ để xây một cụm tự đủ.
8. Xem giới hạn ba bước của bài tập là chân trời cưỡng bức; nếu cần MDP dừng, trạng thái phải gồm chỉ số thời gian.

## Ngoại lệ

Không có ngoại lệ raster. Không có tài sản cốt lõi phụ thuộc mạng.

## Trạng thái rà soát

Bản nháp đầu đã được tạo để chuyển sang kiểm định storyboard và bốn vòng rà soát độc lập.

## Báo cáo kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | `L07-04`–`L07-11` | Cụm đặc trưng đặt ví dụ miền sau thiết lập và công thức, nên chu trình chưa có ví dụ cụ thể trước hình thức hóa. | Bản nháp đặt thiết lập và mô hình ở `L07-07`–`L07-08`, còn ví dụ đầu tiên ở `L07-09`. | Dùng `L07-06` làm ví dụ số về chia sẻ tham số trước thiết lập tổng quát. |
| nghiêm trọng | `L07-12`–`L07-17` | Cụm MC đặt phép đạo hàm và thuật toán trước ví dụ số. | Bản nháp có gradient ở `L07-14`, thuật toán ở `L07-15`, ví dụ ở `L07-16`. | Đặt ví dụ hướng sửa ở `L07-14`, gradient ở `L07-15`, thuật toán và kiểm tra ở `L07-16`. |
| nghiêm trọng | `L07-18`–`L07-24` | TD chưa có cập nhật số trước bán gradient; Bellman chiếu đi từ đại số sang trực giác nên khó theo dõi. | Bản nháp mở trực tiếp bằng công thức ở `L07-19`; $b-Aw$ đứng trước hình học chiếu nhưng không có ví dụ đơn giản. | Thêm một cập nhật TD số ở `L07-19`; dùng ví dụ chiếu hai chiều ở `L07-22` trước công thức tổng quát `L07-23`. |
| nghiêm trọng | `L07-26`–`L07-33` | Cầu nối từ điều khiển theo chính sách sang khác chính sách và bộ ba bất ổn chưa tạo tình huống cụ thể trước khi phân loại. | Q-learning được nêu như công thức rời ở `L07-31`; `L07-32` mới giải thích ba cơ chế. | Viết `L07-31` như biến đổi từ SARSA, chỉ ra ba cơ chế trên cùng tình huống rồi mới gọi tên và phân loại ở `L07-32`. |
| trung bình | toàn bài | Bảng thời lượng theo cụm bị chồng lấn ở `L07-31` và không chỉ rõ 10 phút linh hoạt thuộc khoảng nào. | Cụm điều khiển và cụm bất ổn đều tính `L07-31`; tổng theo hàng không truy nguyên được về 110 + 10. | Chia lại thành các khoảng trang rời nhau, ghi riêng cốt lõi và linh hoạt, kiểm tổng 120 phút. |
| trung bình | `L07-24`, `L07-33` | Một số cụm có kết luận nhưng thiếu kiểm tra trực tiếp ngay sau ứng dụng. | Câu kiểm tra Bellman nằm tận `L07-35`; chẩn đoán deadly triad chưa buộc áp dụng vào Q-learning vừa học. | Thêm câu kiểm tra tại `L07-24` và `L07-33`; giữ `L07-35` làm kiểm tra tổng hợp. |

## Quyết định chỉnh sửa sau kiểm định storyboard

1. Giữ đủ 36 trang chính và ba trang dọc; không đổi `data-slide-id`.
2. Sửa `L07-06` thành ví dụ số về hai trạng thái dùng chung tham số. Cụm đặc trưng nay đi theo `L07-04` → `L07-05` → `L07-06` → `L07-07`–`L07-10` → `L07-11`.
3. Đổi vai trò `L07-14`–`L07-16`: ví dụ MC đứng trước gradient; thuật toán kết bằng câu kiểm tra và nối sang bài áp dụng `X02`.
4. Thêm cập nhật TD số ở `L07-19`, sau đó mới khái quát bán gradient và giao diện thuật toán ở `L07-20`.
5. Giữ $b-Aw$ ở `L07-21` như ứng dụng của cập nhật trung bình; bổ sung ví dụ chiếu hai chiều ở `L07-22` trước định nghĩa $\Pi_D$ ở `L07-23` và câu kiểm tra ở `L07-24`.
6. Viết lại `L07-31` thành đúng một biến đổi từ SARSA sang Q-learning; ba cơ chế xuất hiện trên cùng tình huống trước khi được phân loại tại `L07-32`. `L07-33` áp dụng lại phân loại cho Q-learning.
7. Chia thời lượng thành bảy khoảng không chồng lấn. Tổng cốt lõi là 110 phút; phần linh hoạt là 10 phút; ba bài dọc vẫn là 8 + 10 + 12 phút.
8. Rà lại hai trang lân cận của mọi vị trí đổi vai trò. Các câu nối `L07-12`–`L07-17`, `L07-18`–`L07-24` và `L07-29`–`L07-34` đã được cập nhật trong storyboard.

Các lỗi nghiêm trọng của vòng kiểm định storyboard đã được xử lý. Bản này chuyển sang bốn vòng rà soát độc lập; chưa coi mục này là kiểm định cuối.

## Hợp nhất bốn báo cáo độc lập

| Đề xuất | Quyết định | Cách xử lý |
|---|---|---|
| Sửa thứ tự tích Kronecker và không coi đó là mã hóa duy nhất. | chấp nhận | `L07-10` dùng $e_a\otimes\phi(s)$; `L07-27` được gọi rõ là đặc trưng ba chiều thiết kế trực tiếp cho $(s,a)$. |
| Nêu $\gamma=1$ cho hai bài tính. | chấp nhận | Bổ sung tại `L07-27`, `L07-30`, `X02` và `X03`. |
| Viết SARSA như thuật toán control với chính sách hiện hành. | chấp nhận | `L07-28`–`L07-29` nêu $\varepsilon$-greedy theo $\hat q(\cdot,\cdot,w)$, phá hòa, khởi tạo $S,A$, cập nhật chính sách qua $w$ và cảnh báo hội tụ. |
| Hạ mục tiêu Q-learning xuống phân biệt quy tắc đích. | chấp nhận | `L07-03` và outline được sửa; `L07-31` chỉ định nghĩa đích, miền cực đại, trường hợp kết thúc và so sánh trên mẫu `L07-30`. |
| Bỏ phát biểu hội tụ dạng bảng quá rộng. | chấp nhận | `L07-02` chỉ nhắc cập nhật và điều kiện phân tích riêng của Bài 06. |
| Tách $\mu$ của MC khỏi $d_\pi$ của TD và viết kỳ vọng có điều kiện. | chấp nhận | `L07-07`, `L07-13`, `L07-17`, `L07-34` và bảng ký hiệu đã đồng bộ. |
| Chỉ dùng đủ hạng để kết luận nghiệm tham số duy nhất. | chấp nhận | `L07-17`, `L07-23` và ghi chú `L07-24` phân biệt tồn tại dự đoán, khả nghịch và duy nhất của $w$. |
| Đặt trực giác Bellman trước $A,b$ và thêm điều kiện trực giao. | chấp nhận | Thứ tự mới là `L07-21` hình học, `L07-22` trực giao và $Aw=b$, `L07-23` điểm cố định chiếu. Storyboard và câu nối đã đổi theo. |
| Làm hai trang điều kiện hội tụ dễ học hơn. | chấp nhận | `L07-17` và `L07-24` dùng hai khối điều kiện; định nghĩa ổn định của $A$ được nêu ngắn trên trang và giải thích trong ghi chú. |
| Tăng cỡ chữ hiệu dụng của giả mã và bảng. | chấp nhận | Bảng dùng $0.94$ em trong trang có cỡ nền $0.82$ em; giả mã `L07-29` dùng $0.94$ em, cho cỡ hiệu dụng trên $0.75$ em. |
| Ẩn đáp số hai bài tính. | chấp nhận | Return, trọng số và dự đoán ở `X02`–`X03` nằm trong fragment. |
| Dùng $x(S,A)$ cho cập nhật giá trị hành động và giải thích $\varepsilon$. | chấp nhận | `X02` dùng đúng $x(S,A)$; ghi chú `L07-29` và `X03` nêu $\varepsilon=0.25$ không tham gia số học khi chuỗi đã cho. |
| Thu hẹp deadly triad và không hứa hội tụ cho bài kế tiếp. | chấp nhận | `L07-32`–`L07-33` giới hạn kết luận vào thiết lập học giá trị TD liên quan; `L07-36` nói rõ bảo đảm tuyến tính không tự chuyển sang mạng nơ-ron. |

Không có đề xuất nghiêm trọng hoặc trung bình nào bị từ chối. Giữ 36 trang chính và ba trang dọc; không đổi mã trang. Hai trang lân cận của các vùng `L07-07`–`L07-10`, `L07-17`–`L07-24` và `L07-27`–`L07-36` đã được rà lại về câu nối, ký hiệu và phạm vi kết luận.

## Trạng thái sau chỉnh sửa độc lập

Mọi lỗi nghiêm trọng đã được xử lý. Các thay đổi công thức và thuật toán cần qua một lượt tái kiểm tra toán học trước kiểm định cuối.

## Tái kiểm tra toán học và thuật toán

Tác tử rà toán độc lập xác nhận không còn lỗi từ mức trung bình trở lên. Các nội dung sau đã được kiểm tra lại: thứ tự $e_a\otimes\phi(s)$; cập nhật MC và TD; phương trình $Aw=b$ và điểm cố định Bellman chiếu; giao diện SARSA; đích Q-learning ở chuyển tiếp thường và chuyển tiếp kết thúc; toàn bộ số học của ví dụ TD, Bài 7 và Bài 8.

## Kiểm định cuối

- 39 mã trang duy nhất, 39 khối ghi chú và 39 mục storyboard; độ sâu `<section>` lớn nhất là 2.
- KaTeX nghiêm ngặt đọc 194 biểu thức, không có lỗi phân tích.
- Tám SVG hợp lệ về XML, có `role="img"`, `title`, `desc`; nhãn nhỏ nhất là 30 px.
- HTML và tám SVG trả HTTP 200 tại cổng 8765.
- Không có ảnh raster, tài nguyên mạng cốt lõi, mã trang, nhãn phân tuyến hoặc thời lượng lộ trên mặt trang và ghi chú.
- Cỡ chữ hiệu dụng của bảng và giả mã là khoảng 0,77 em, cao hơn ngưỡng 0,75 em.
- Năm tệp HTML/quy trình trong dự án Codex Slides khớp từng byte với bản trong kho.

Codex Slides đã được dùng làm dự án bền vững và kho Design Files, nhưng Codex Browser trong trình soạn thảo không khả dụng trong phiên này. Vì vậy chưa thể tuyên bố đã duyệt trực quan bằng Codex Slides hoặc kiểm tra tràn trang bằng Browser. Các kiểm tra RevealJS cục bộ, cấu trúc, công thức, đường dẫn và tài sản đã được thực hiện đầy đủ; giới hạn trực quan này không được che giấu.

## Vòng writer theo brief chỉnh sửa

### Mô hình và nhà cung cấp

Runtime planner, source reader, storyboard reviewer, năm reviewer và writer đều dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.

### Tóm tắt năm báo cáo theo trường bắt buộc

| Báo cáo | Mức độ cao nhất | Phát hiện chính | Xử lý |
|---|---|---|---|
| Góc nhìn sinh viên | trung bình | Thiếu phần thưởng ở ví dụ, đáp án phân mảnh và giải thích hệ số 2 | Đã bổ sung ở `L07-06`, `L07-27`, `L07-36`, `X01`; giữ `L07-07` đúng vị trí nguồn |
| Chuyên gia Học tăng cường | trung bình | Thiếu dữ liệu tương quan/không dừng, đối chiếu độ chệch–phương sai và lý do lược bảng phân loại nguồn | Đã sửa `L07-04`, `L07-25` và ghi lý do trong outline |
| Toán học và thuật toán | nhẹ | Cần nói rõ $e=2$, thứ tự tích Kronecker và quy ước mọi-lần-ghé | Đã sửa `L07-06`, ghi chú `L07-10`, `L07-16`; toàn bộ số học đạt |
| Phản biện học thuật và giảng dạy | trung bình | Cần phân biệt đích SARSA/Q-learning trên mẫu cụ thể và nối $\Pi_I$ với $\Pi_D$ | Đã sửa `L07-21`, `L07-31`; bác phát hiện sai về X02 sau khi tính lại |
| Kết nối và mạch viết | trung bình | Bảy cụm chưa được ánh xạ rõ vào sáu mạch; ranh giới phần và bài tập dọc cần ghi tường minh | Đã lập bản đồ M1–M6 trong outline/storyboard và giữ X01–X03 dọc trong M6 |

### Hai dương tính giả

1. **Tổng phút:** reviewer báo bảng thời lượng sai, nhưng tổng đúng là $7+23+21+30+3+19+17=120$ và chữa bài $8+10+12=30$; bảng không cần sửa. Đây là dương tính giả.
2. **X02/HW7:** reviewer nghi sai đáp số, nhưng kiểm tra lại: $q(C,0;w_1)=2\cdot299{,}5+100{,}5+98{,}5=798$, nên $w_2=(339{,}7;120{,}6;118{,}6)$ và dãy hiện tại đúng. Đây là dương tính giả; đáp số X02 giữ nguyên. X03 cũng đúng với các sai số $-2;\,-1{,}2;\,14{,}52$.

### Nguồn tr. 42

Nguồn tr. 42 có nghi vấn về ký hiệu $H^3/H^4$ trong khai triển; deck đã lược phần này và không đưa khẳng định mới về nó lên mặt trang hay ghi chú.

### Kết quả writer

- HTML: đổi ranh giới sáu `<section>` ngoài thành sáu mạch M1–M6 đúng ranh giới brief; giữ 39 `data-slide-id` và thứ tự; sửa cục bộ `L07-02`, `L07-03`, `L07-04`, `L07-06`, `L07-10`, `L07-16`, `L07-17`, `L07-21`, `L07-25`, `L07-26`, `L07-27`, `L07-31`, `L07-34`, `L07-36`, `X01`; không đổi số học X02/X03; không tách `L07-29`; không di chuyển $J_\mu$ khỏi `L07-07`.
- Outline: sáu mạch đúng ranh giới, danh mục đủ 39 mã trang, tiên quyết đại số tuyến tính, lý do bỏ bảng phân loại tr. 4, bảy cụm trong sáu mạch.
- Storyboard: bản đồ sáu mạch với chức năng/kết nối vào/đầu ra/cụm/trang, hàng chữa bài 30 phút ngoài 120 phút, câu nối `L07-03` sửa theo ba trục, tổng 120+30 giữ đúng.
- Chưa tuyên bố render hoặc Codex Slides ở lượt writer.

## Tái kiểm và kiểm định bàn giao ngày 30-08-2026

- Hai tác tử chỉ đọc tái kiểm sau writer đều chạy qua OpenRouter với `requested_model=observed_model=z-ai/glm-5.3-flash`. Tác tử toán học tính lại độc lập X02, X03 và toàn bộ ví dụ số; không có lỗi chặn, nghiêm trọng hoặc trung bình. Tác tử kết nối xác nhận sáu mạch M1–M6, 39 mã trang, độ sâu 2 và các ranh giới phần đều nối được.
- Hai dương tính giả được giữ làm bằng chứng: tổng thời lượng chính bằng 120 phút; X02 đúng vì $q(C,0;w_1)=798$.
- Sau kiểm tra ảnh, `L07-27`, `L07-31` và `X01` được rút gọn cục bộ để chừa khoảng an toàn ở mép dưới. Không đổi công thức, kết quả số, thứ tự hoặc vai trò trong mạch.
- Kiểm tra tĩnh đạt: sáu `<section>` ngoài, 39 `data-slide-id` duy nhất, 39 ghi chú, đủ 39 mã trong outline và storyboard; tám SVG phân tích XML được, có `role="img"`, `title`, `desc`; mọi tham chiếu cục bộ tồn tại; không có ảnh raster hoặc phụ thuộc mạng cốt lõi.
- Lệnh `python3 -m reloadserver 8765` không khả dụng trong môi trường. Dùng bản sao webroot an toàn không chứa `.env` với `python3 -m http.server 8765`; Chromium duyệt đủ 39 trang ở 1280 × 720 và 800 × 600, tạo 78 ảnh kiểm tra, không có lỗi console, lỗi trang, yêu cầu hỏng hoặc lỗi điều hướng bàn phím. Cảnh báo hình học tự động còn lại chỉ đến từ hộp bao KaTeX và tiêu đề bị biến đổi theo tỉ lệ; đối chiếu trực tiếp toàn bộ ảnh không thấy tràn hoặc chồng lấn.
- Bản cuối đã được tự kiểm theo `no-ai-slop/eval.md`: không còn lời dẫn rỗng, câu hỏi tu từ, khẩu hiệu hoặc kết luận lặp. Rà theo Quill xác nhận thuật ngữ, ký hiệu và câu chuyển liên tục; không tạo `quill.json`.
- Dự án Codex Slides bền vững `20260824191033-chuy-n-lecture-7-h-m-x-p-x-trong-h-c-t-n-6jd4` vẫn ở trạng thái draft với 0 trang dựng. Năm Design Files `lecture-07-xap-xi-ham.html`, `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` đã được đồng bộ và đọc lại khớp chính xác với kho. Codex Browser không có trong phiên nên không thể duyệt trực quan bằng giao diện Codex Slides; kiểm tra Chromium cục bộ là bằng chứng trực quan chính.

## Giai đoạn ghi chú bài giảng — 03-09-2026

### Phạm vi và điều phối

- Ghi chú dùng nguồn chính `RL-hk2-2025-2026/lecture-07.pdf` (45 trang) và phiếu `resources/hw07-function-approximation.pdf` (8 bài). Không có code demo trong nguồn.
- Reader DeepSeek lập kế hoạch bằng `plan/12/600/16000`, phân tích nguồn bằng `source/20/600/20000`, và hợp nhất phạm vi bằng `recheck/8/600/16000`. Runtime thành công đều trả `requested_model=observed_model=deepseek/deepseek-v3.2`, provider `OpenRouter`.
- Writer GLM tạo bản đầu bằng `write/20/600/32000`; một phản hồi `finish_reason=error` được cầu nối phục hồi, rồi hoàn tất ở vòng 8. Runtime trả `requested_model=observed_model=z-ai/glm-5.3-flash`, provider `OpenRouter`.
- Phạm vi được chấp nhận gồm 16 chủ đề: 12 cốt lõi, một cầu nối Bài 06, hai chủ đề bổ sung và một chủ đề thực hành. Phần chính 120 phút; chữa bài 30 phút. Tr. 5–20 chỉ là cầu nối ngắn; kết quả MDP tuyến tính tr. 42 chỉ nêu hướng nghiên cứu; không thêm ví dụ ngoài nguồn.

### Năm báo cáo độc lập cho bản ghi chú đầu

| Vai rà | Mức độ cao nhất | Phát hiện và bằng chứng | Quyết định |
|---|---|---|---|
| Góc nhìn sinh viên — GLM | nghiêm trọng | Bài 8 sai ngay từ $w_1$; ký hiệu $v_{\hat{}}$, $q_{\hat{}}$ khó đọc; kết luận đứng trước phần thực hành. | Chấp nhận; tính lại toàn bộ Bài 8, chuẩn hoá thành $\hat v$, $\hat q$, chuyển kết luận xuống cuối. |
| Chuyên gia Học tăng cường — DeepSeek | nghiêm trọng | Cập nhật và đích điều khiển cần phân biệt đánh giá với cải thiện chính sách; phạm vi kết quả hiện đại bị nói rộng hơn thiết lập nguồn. | Chấp nhận; đổi tên Bài 7 thành một bước đánh giá trong quá trình điều khiển và thu hẹp kết quả hiện đại. |
| Toán học và thuật toán — DeepSeek | nghiêm trọng | Bài 8 sai số học; lời giải gradient có chỗ giữ ký hiệu tạm; số chiều lớp hàm thiếu điều kiện hạng. | Chấp nhận; tự tính lại từ mẫu gốc, viết gradient đầy đủ và sửa số chiều thành $\operatorname{rank}(\Phi)\le d$. Bác đáp số thay thế $w_3=(7.52,-2.24,1.04)$ vì không khớp phép cập nhật trực tiếp. |
| Phản biện học thuật và giảng dạy — DeepSeek | nghiêm trọng | Cầu nối giữa kết quả tuyến tính, thực hành và kết luận chưa đúng thứ tự; một số bảo đảm thiếu giới hạn thiết lập. | Chấp nhận; dùng thứ tự bộ ba bất ổn → MDP tuyến tính → thực hành → kết luận và gắn giả thiết vào từng bảo đảm. |
| Kết nối và mạch viết — GLM | nghiêm trọng | Trùng mã `lec-07-topic-05`, tên chủ đề và kết nối vào–ra của chủ đề 14–16 chưa khớp; tiếng Anh dày. | Chấp nhận; sửa thành 16 mã duy nhất, đồng bộ bản đồ chủ đề, câu nối và thuật ngữ tiếng Việt. |

Các lượt GLM hoàn tất ở vòng 3. Reviewer DeepSeek ban đầu đọc nhiều tệp đã chạm giới hạn gọi công cụ ở 5 hoặc 8 vòng. Lượt chạy lại chỉ cấp đúng một note và yêu cầu một lần đọc đã hoàn tất mà không đổi model. Không dùng worker mặc định thay thế.

### Chỉnh sửa và quyết định

- Bài 8 được tính lại: $w_1=(-0.2,0.6,-1.4)^\top$, $w_2=(-0.68,0.84,-1.64)^\top$, $w_3=(8.032,-2.064,1.264)^\top$; các giá trị cuối là $23.296$, $19.392$, $27.424$.
- Lời giải gradient TD dùng $e(w)=R_{t+1}+\gamma x(S_{t+1})^\top w-x(S_t)^\top w$; bước hạ gradient đầy đủ giữ $e(w)[x(S_t)-\gamma x(S_{t+1})]$, còn TD bỏ số hạng tại trạng thái kế.
- Bỏ khẳng định độ phức tạp mẫu $\tilde O(d/\varepsilon^2)$ và các suy rộng về tối ưu cực tiểu–cực đại vì nguồn không cung cấp thiết lập đủ.
- Đồng bộ ký hiệu đặc trưng thành $x$, chuẩn hoá $\hat v$, $\hat q$, và chuyển phần kết luận xuống sau hai bài tính tay.
- Hai lượt writer sửa rộng `write/20/600/20000` và `write/12/600/12000` dừng ở `finish_reason=length` trước khi ghi. Điều phối viên không tăng tiếp ngân sách; các sửa được chia thành khối hẹp, kiểm diff và giao reviewer độc lập tái kiểm. Kinh nghiệm này đã được mã hoá thành preset `patch/6/300/7000` trong commit `95169a3`.

### Tái rà sau chỉnh sửa

- Reviewer toán DeepSeek dùng nguyên preset `recheck/6/600/10000`, chỉ đọc note một lần và hoàn tất ở vòng 2 sau 128,6 giây. Runtime: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider `OpenRouter`. Báo cáo xác nhận ký hiệu, gradient MC/TD, Bellman chiếu, giả thiết hội tụ và toàn bộ số học Bài 7–8 đúng; không còn lỗi chặn bàn giao hoặc nghiêm trọng.
- Reviewer mạch GLM dùng `recheck/6/600/10000`, chỉ đọc note một lần và hoàn tất ở vòng 2 sau 57,3 giây. Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider `OpenRouter`. Báo cáo xác nhận 16 chủ đề, thứ tự, tổng 120 phút và kết luận sau thực hành; sáu lỗi nhẹ về tên, chỉ số và chính tả đã được sửa. Nhận xét ngày tháng là dương tính giả: tháng 4-2026 đã qua tại thời điểm rà tháng 9-2026.
- Bản cuối có 16 mã chủ đề duy nhất và 17 bộ `exercise`–`hint`–`solution`; chỉ dùng `$...$`, `$$...$$`. Nội dung đã tự kiểm theo `no-ai-slop/eval.md`; rà Quill xác nhận thứ tự và thuật ngữ liên tục, không tạo `quill.json`.

### Kiểm định trình xem ghi chú

- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại với `/usr/bin/python3: No module named reloadserver`.
- Dùng bản sao webroot cô lập trong `/tmp`, không chứa `.env`, và máy chủ `python3 -m http.server 8765 --bind 127.0.0.1` làm phương án dự phòng.
- Chromium duyệt từ liên kết duy nhất trên `index.html` ở 1280 × 720 và 390 × 844. Cả hai khung có 397 biểu thức KaTeX, 17 bài tập, 17 lời giải, 34 khối đóng/mở; không có lỗi KaTeX, console, trang, tài nguyên, tràn ngang hoặc phần tử tràn ngoài vùng chứa. Phím Enter mở được khối lời giải.
- Ảnh toàn trang ở hai kích thước đã được điều phối viên xem trực tiếp. Một công thức đặc trưng nội dòng ban đầu gây tràn ở 390 px; sau khi chuyển thành công thức khối và rút nhãn sang tiếng Việt, kiểm định chạy lại đạt.
- Codex Slides không chạy được trong môi trường hiện tại vì Node.js là `v18.19.1`, thấp hơn yêu cầu Node.js 20 của tiện ích. Vì vậy không tuyên bố đã rà bản ghi chú bằng Codex Slides; bằng chứng trực quan là hai lượt Chromium cục bộ.

## Đồng bộ deck sau khi chốt ghi chú — 03-09-2026

- Reviewer mạch GLM đối chiếu `lecture-note.md` với `lecture-07-xap-xi-ham.html` bằng `review/8/600/12000`, hoàn tất ở vòng 2 sau 166,5 giây. Runtime trả `requested_model=observed_model=z-ai/glm-5.3-flash`, provider `OpenRouter`. Công cụ đọc giới hạn 400 dòng mỗi lượt nên báo cáo chỉ bao phủ 400 dòng đầu của note nhưng đọc đủ deck; điều phối viên không dùng báo cáo này làm bằng chứng cho phần note còn lại.
- Báo cáo xác nhận toàn bộ số học trên 39 trang đúng. Một lỗi nghiêm trọng được chấp nhận: note phát biểu lại hội tụ dạng bảng rộng hơn phạm vi đã duyệt cho `L07-02`. Note đã được hạ thành cầu nối điều kiện, không lặp phác thảo tr. 5–20. Hai lỗi trung bình được sửa: phát biểu phương sai TD được giới hạn bằng “thường” trong thiết lập quen thuộc; ký hiệu chính sách tham lam ở `L07-26` đổi từ $g_w$ sang $\pi_w$ để khớp note. Hai lỗi nhẹ được sửa bằng cách thêm $\mu$ và dùng cùng mã hoá khối $e_a\otimes\psi(s)$.
- Reviewer toán/RL DeepSeek tái kiểm vùng note vừa đổi bằng `recheck/6/600/10000`, hoàn tất ở vòng 2 sau 63,0 giây. Runtime trả `requested_model=observed_model=deepseek/deepseek-v3.2`, provider `OpenRouter`; không còn lỗi nghiêm trọng. Đề xuất thêm một kết luận phương sai bị chặn không được áp dụng vì nguồn không cung cấp đủ giả thiết và phát biểu hiện tại đã đúng phạm vi.
- Không đổi số trang, thứ tự, ranh giới phần hoặc luận điểm trung tâm. Deck vẫn có sáu `<section>` ngoài, 39 mã trang duy nhất, 39 ghi chú và tám SVG. Tám SVG phân tích XML được, có `role="img"`, `title`, `desc`; không có ảnh raster hoặc tài nguyên mạng.
- Dùng lại webroot cô lập tại cổng 8765. Chromium duyệt đủ 39 trang ở 1280 × 720 và 800 × 600: không lỗi console, KaTeX, tràn chữ, chồng lấn hoặc phần tử vượt khung. Ảnh `L07-26` ở hai kích thước đã được điều phối viên xem trực tiếp; ký hiệu $\pi_w$ hiển thị đúng.
- `reloadserver` và Codex Slides có cùng giới hạn đã ghi ở pha note. Không tuyên bố đã rà thay đổi này bằng Codex Slides.
