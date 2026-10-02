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

## Bổ sung ánh xạ ghi chú–trang chiếu — 04-09-2026

- Reader DeepSeek V4 Flash đề xuất ánh xạ 16 topic phủ đủ 39 slide. Runtime `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, provider `OpenRouter`, reasoning none.
- Writer GLM đã thêm cùng bảng ánh xạ vào outline/storyboard. Runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, provider `OpenRouter`, reasoning minimal.
- HTML được gắn 39 `data-note-topic-id`, mỗi slide đúng một topic; cả 16 topic đều xuất hiện. Không đổi số trang, thứ tự, nội dung, công thức hoặc SVG.
- Tái rà mạch GLM: PASS, chỉ hai nhận xét nhẹ không cần sửa.
- Tái rà chuyên môn DeepSeek nêu một vấn đề trung bình ở `L07-34` vì mặt trang thiên về phạm vi lý thuyết/topic-12.
- Quyết định điều phối viên (không đổi): `data-note-topic-id` gắn cho toàn bộ slide kể cả notes; notes `L07-34` chứa duy nhất phần kết quả MDP tuyến tính và nguồn tr. 42–43, nên dùng topic-14 để giữ ánh xạ hai chiều; topic-12 đã có `L07-35`–`L07-36`; không thêm trang bổ sung vì sẽ mở rộng nhánh ngoài tuyến chính.
- Không còn lỗi chặn bàn giao hoặc nghiêm trọng.

## Tái kiểm cuối ánh xạ — 04-09-2026

- Chromium duyệt lại đủ 39 trang ở 1280×720 và 800×600: 39 mã trang duy nhất, 39 `data-note-topic-id`, đủ 16 chủ đề, không lỗi KaTeX, console, tài nguyên, bàn phím hoặc phần tử vượt khung trang hiện tại.
- Ba Design Files `lecture-07-xap-xi-ham.html`, `outline.md`, `storyboard.md` đã được ghi lại trong dự án Codex Slides `20260824191033-chuy-n-lecture-7-h-m-x-p-x-trong-h-c-t-n-6jd4` và đọc lại khớp từng byte với kho.
- Codex Slides trả handoff tới Design Files nhưng Codex in-editor Browser không có trong phiên này. Không tuyên bố đã rà trực quan bằng giao diện đó; ảnh Chromium cục bộ là bằng chứng hiển thị cuối.

## Rà soát từng trang và biên tập lại — 02-10-2026

Yêu cầu của người dùng: duyệt lần lượt từng trang Bài 07; với mỗi trang xác định trang muốn nói gì, vấn đề còn lại và đề xuất sửa; sửa để tiêu đề ngắn gọn, học thuật, mạch lập luận chặt, khái niệm không xuất hiện đột ngột; duyệt lại theo góc nhìn sinh viên; xong mỗi trang thì sửa mục ghi chú bài giảng tương ứng, gắn bài lên `index.html`, commit và push theo từng trang.

Vai trò (bằng chứng: lệnh gọi công cụ của phiên chính): điều phối là phiên chính, Claude Code, Opus 5.5, lập bảng rà soát sau khi đọc deck, ghi chú, dàn bài, storyboard, nguồn 45 trang và phiếu bài tập; biên tập là một Agent `fork` (kế thừa Opus 5.5 của phiên), tác tử duy nhất ghi tệp, được tiếp tục bằng SendMessage cho từng trang; hai tác tử rà soát chỉ đọc (Agent `fork`): toán học và RL; mạch lập luận, góc nhìn sinh viên kèm no-ai-slop Detect. Mức effort của phiên không xác nhận được từ trong phiên. Phiên điều phối khởi động lại trong lúc sửa L07-07: tác tử biên tập đầu bị ngắt (bốn sửa rà soát của L07-07 đã ghi vào cây làm việc), không tiếp tục được bằng SendMessage; từ đó dùng một tác tử biên tập fork mới (Opus 5.5) và hai tác tử rà soát fork mới cùng vai. Công cụ kiểm và ảnh chụp chuyển sang thư mục làm việc `.lec07-work/` ở gốc repo, bị `.gitignore` bỏ qua, xóa khi xong.

Quy ước dùng chung với Bài 05–06: "lợi tức" thay "return"; "mục tiêu" (mục tiêu cập nhật) thay "đích", giữ "chính sách đích"; "Sarsa", "$\varepsilon$-tham lam"; tiêu đề không viết tắt "MC"; trang kiểm tra có tiêu đề "Kiểm tra …"; trang thuật toán "Thuật toán …". Mỗi commit gồm deck, mục ghi chú bài giảng tương ứng và planning của đúng trang đó.

### Bước 0: chuyển sang hệ CSS dùng chung

Deck dùng `class="reveal lecture-deck"`; bỏ các luật CSS cục bộ trùng `lecture-slide.css` (cỡ chữ trang, màu tiêu đề, `.box`, `.grid2`, `.grid3`, `.card`, `.figure`, `.math-large`, `.check`, `.note-source`, bảng). Giữ tạm `.answer`, `.codebox`, `.compact`, `.warn`. Thêm `text-transform:none` cho KaTeX trong `h2` (tiêu đề L07-22 trước đó hiện "AW = B"). Bỏ plugin Markdown, giống Bài 06. L07-25 dùng `figure short`; X01 thu khoảng cách dọc cục bộ. Không đổi chữ.

Kiểm trình duyệt (Playwright, `reloadserver` cổng 8766, 39 trang, 1600×900 và 390×844): không lỗi console, không `.katex-error`, không yêu cầu mạng ngoài, không cuộn ngang. L07-32 hết tràn 46px nhờ luật `.figure` dùng chung. L07-17 còn đè chân trang 15px (trước là 7px), xử lý ở bước của trang này. Ảnh đã xem: L07-22, L07-32.

Quy ước số và vector của lượt này: dấu phẩy thập phân; vector có thành phần thập phân viết thành phần cách nhau bằng dấu chấm phẩy, ví dụ $(1;0{,}5)^T$; trong cùng một trang, mọi vector dùng cùng cách viết. Áp dụng từ L07-06; các trang còn dùng dấu phẩy phân tách (L07-14, L07-19, L07-30, X02, X03) được sửa khi tới lượt.

### Bảng từng trang

| Mã trang | Trang muốn nói gì | Vấn đề | Đề xuất và thay đổi | Quyết định | Thay đổi ghi chú bài giảng |
|---|---|---|---|---|---|
| L07-01 | Tên bài và nội dung chính | Thiếu dòng bài và học phần, tác giả nguồn, liên kết ghi chú như L06-A01; phụ đề liệt kê thuật ngữ rời ("sai phân thời gian và điều khiển") | Tiêu đề giữ "Xấp xỉ hàm trong Học tăng cường". Thêm "Bài 07 · Học tăng cường", dòng nội dung "Xấp xỉ tuyến tính theo đặc trưng, Monte Carlo, sai phân thời gian (TD), Sarsa và Q-learning", học kỳ, tác giả bài giảng nguồn, liên kết ghi chú bài giảng. Ghi chú diễn giả: một cập nhật đổi nhiều dự đoán; bảo đảm hội tụ dạng bảng phải xét lại; nguồn tr. 1, 21–23 (bỏ tr. 2–4 vì mục lục và bảng phân loại không dùng ở trang này). Thêm thẻ Bài 7 vào `index.html` với hai liên kết bài giảng và ghi chú | sửa | Tiêu đề "Bài 07. Xấp xỉ hàm trong Học tăng cường"; thêm dòng học phần và đoạn giới thiệu (lớp tuyến tính, MC và TD cho dự đoán, Sarsa và mục tiêu Q-learning, điều kiện bảo đảm) |
| L07-02 | Kết quả dạng bảng của Bài 05–06 và thay đổi khi dùng hàm tham số | Tiêu đề "Cầu nối từ bài toán dạng bảng" chung chung; câu "đã xây dựng … cùng các điều kiện phân tích riêng; tiên quyết gồm cả Q-learning" rối; ba điểm đối chiếu thuật toán của nguồn tr. 3 chỉ có trong ghi chú L07-03; ghi chú diễn giả là bình luận về nguồn | Cầu nối từ bài toán dạng bảng → Từ bảng giá trị đến hàm xấp xỉ. Thẻ "Bài 05–06": một giá trị riêng cho mỗi trạng thái hoặc cặp; hội tụ cần thăm mọi trạng thái (hoặc cặp) vô hạn lần, Robbins–Monro, GLIE với điều khiển Monte Carlo và Sarsa. Thẻ "Bài này": $\hat v$, $\hat q$ dùng chung $w$; một cập nhật đổi ước lượng ở nhiều trạng thái nên lập luận theo từng ô không áp dụng trực tiếp. Hộp: danh sách ba điểm đối chiếu theo tr. 3, bootstrap giải thích là mục tiêu chứa ước lượng hiện tại. Nhãn thẻ viết đậm đầu đoạn để trang vừa khung. Ghi chú diễn giả: lập luận dạng bảng dựa vào ước lượng riêng của từng cặp; dự đoán và điều khiển; bootstrap của TD(0) Bài 05; nguồn tr. 3, 5–20. Outline: ánh xạ tr. 3 sang trang này | sửa | Mục topic-13 thành "## 1. Mở đầu" với "### 1.1. Từ bảng giá trị đến hàm xấp xỉ"; viết lại theo mặt trang, thêm ba điểm đối chiếu và dự đoán/điều khiển; bỏ đoạn giới hạn bảng tra trùng mục sau; bài kiểm tra GLIE bỏ tham chiếu "Bước 1", "Bước 4" của phác thảo nguồn; bản đồ chủ đề đổi tên mục |
| L07-03 | Phạm vi và kết quả học tập của bài | Tiêu đề "Kết quả học tập" không có danh sách nội dung như L05-A02, L06-A02; bốn thẻ dùng viết tắt "MC", "SARSA" và mục tiêu chung chung ("Giải thích phương trình Bellman chiếu", "Triển khai SARSA"); ghi chú diễn giả lặp "ba trục" nay đã ở L07-02 | Kết quả học tập → Nội dung và mục tiêu. Bố cục theo L06-A02: trái danh sách sáu phần (năm phần nội dung và bài tập), phải thẻ "Mục tiêu học tập" với năm mục tiêu kiểm tra được. Ghi chú diễn giả: thứ tự dự đoán trước điều khiển, chuỗi năm trạng thái của Bài 06 cho ví dụ điều khiển và bài tập, phạm vi không chứng minh hội tụ Sarsa/Q-learning với xấp xỉ hàm và không xét actor-critic; nguồn tr. 2–4, 21–44. Outline: mục tiêu đổi thành năm mục khớp mặt trang | sửa | Chuyển mục "Mục tiêu và kiến thức tiên quyết" ở đầu ghi chú vào "### 1.2. Nội dung và mục tiêu" (cùng chỗ Bài 06 đặt mục tiêu, tránh hai danh sách mục tiêu); danh sách mục tiêu khớp mặt trang; tiên quyết ghi Bài 03–06, dùng "Sarsa" |
| L07-04 | Vì sao bảng tra không đủ khi không gian lớn | Tiêu đề dài, là câu khẳng định; bốn ý tách bộ nhớ và số mẫu thành hai dòng nhưng thiếu câu về ưu điểm của bảng (nguồn tr. 23); ý dữ liệu viết tắt "RL", "iid" chưa giải thích; câu hỏi trộn "trạng thái chưa từng gặp" với "lân cận"; ghi chú diễn giả chỉ một câu và dẫn "lecture-07.pdf" | Bảng tra không mở rộng theo không gian trạng thái → Giới hạn của bảng tra. Câu mở: bảng $V\approx v_\pi$, $Q\approx q_\pi$ dễ hiểu, dễ phân tích nhưng khó mở rộng (tr. 23). Ba ý theo tr. 22: không gian lớn hay liên tục; không tổng quát hóa; dữ liệu không độc lập cùng phân phối (iid) và không dừng, kèm lý do (mẫu trong lượt phụ thuộc nhau, phân phối trạng thái đổi theo chính sách). Câu hỏi: cập nhật ô của $s$ thay đổi gì ở ô của trạng thái gần $s$; đáp án "Không thay đổi; mỗi ô được cập nhật độc lập". Ghi chú diễn giả: phân biệt giới hạn bộ nhớ/số mẫu với thiếu tổng quát hóa; khó khăn thứ ba dẫn tới giả thiết lấy mẫu; câu nối sang hàm có tham số | sửa | Mục topic-01 thành "## 2. Nhu cầu xấp xỉ hàm" với "### 2.1. Giới hạn của bảng tra"; viết lại theo ba khó khăn trên mặt trang; chuyển đoạn hai lợi ích sang chủ đề chia sẻ tham số (đã có ở đó); bỏ "i.i.d."/"RL"; bài kiểm tra đổi thành so sánh số đại lượng cần học và cái giá của dùng chung tham số; bản đồ chủ đề đổi tên mục |
| L07-05 | Ý tưởng thay bảng bằng hàm có tham số | Tiêu đề "Một vector tham số thay cho nhiều ô" mô tả hình hơn là gọi tên khái niệm; mặt trang chưa viết $\hat v\approx v_\pi$, $\hat q\approx q_\pi$; thiếu ba lợi ích của nguồn tr. 23; hộp nói về "trạng thái chưa xuất hiện đúng dạng" mà không nêu hệ quả dẫn sang trang sau; alt hình chung chung | Một vector tham số thay cho nhiều ô → Hàm giá trị có tham số. Câu mở với $\hat v(s,w)\approx v_\pi(s)$, $\hat q(s,a,w)\approx q_\pi(s,a)$, $w\in\mathbb R^d$ dùng chung; giữ hình, alt mô tả hai khối; ba lợi ích theo tr. 23 thành hai dòng; hộp nối sang L07-06: một cập nhật có thể làm thay đổi dự đoán ở nhiều trạng thái. Ghi chú diễn giả: $x(s)$ định nghĩa ở trang sau; $d$ thường nhỏ hơn số trạng thái nhưng không bắt buộc; dự đoán ở trạng thái mới chưa chắc đúng; nguồn tr. 23. SVG `tabular-vs-parametric.svg` vẽ lại: nhãn lớn hơn, hộp "đặc trưng x(s)", nhãn $w$ trên mũi tên tới $\hat v(s,w)$, tiêu đề hộp "Hàm có tham số" | sửa | Mục topic-02 thành "## 3. Hàm có tham số dùng chung" với "### 3.1. Hàm giá trị có tham số"; ký hiệu $v_\pi$, $q_\pi$ thay $V^\pi$, $Q^\pi$; ba lợi ích, ghi chú về $x(s)$, $d$ và dự đoán ở trạng thái mới; câu về cập nhật làm đổi nhiều dự đoán và bộ ba bất ổn; bản đồ chủ đề đổi tên mục |
| L07-06 | Một cập nhật tại $s$ đổi dự đoán ở trạng thái khác qua $w$ dùng chung | Tiêu đề mô tả sự việc, không gọi tên khái niệm; quy tắc $\Delta w=\alpha e\,x(s)$ và "sai số mẫu giả định $e$" xuất hiện đột ngột; $\alpha=0{,}1$ không có trong dữ kiện; chưa nêu công thức mức lan; hình dùng $s_t$, $s_1$–$s_3$ không khớp ví dụ $s$, $s'$; ghi chú dẫn tr. 31 không liên quan | Một cập nhật đổi hai dự đoán → Tổng quát hóa qua tham số dùng chung. Câu mở nêu $\hat v(s,w)=x(s)^Tw$ và quy tắc sửa khi dự đoán thấp hơn mục tiêu một lượng $e$; dữ kiện đủ ($\alpha=0{,}1$); vector viết với dấu chấm phẩy; ba kết quả xếp dòng; hộp: $\Delta\hat v(s')=\alpha e\,x(s')^Tx(s)$ tỉ lệ với tích vô hướng. SVG `shared-parameter-effect.svg` vẽ lại theo đúng ví dụ (mẫu tại $s$, $e=2$, $\Delta w=\alpha e\,x(s)$, $w$ dùng chung, $\hat v(s)$: +0,4, $\hat v(s')$: +0,3), dạng dọc để đặt cạnh phép tính; nhãn khoảng 0,8 cỡ chữ thân. Ghi chú diễn giả: nguồn gốc quy tắc ở phần Monte Carlo, phép tính, sai lệch cũng lan, trường hợp trực giao; nguồn tr. 23, 32 | sửa | Thêm "### 3.2. Tổng quát hóa qua tham số dùng chung" với ví dụ và công thức lan truyền; bài kiểm tra $x(s_1)=x(s_2)$ (nhập nhằng, trùng L07-11) thay bằng bài tính $\Delta\hat v$ cho đặc trưng trực giao và tích vô hướng âm |
| L07-07 | Phát biểu bài toán dự đoán khi dùng hàm xấp xỉ | Tiêu đề "Thiết lập dự đoán theo chính sách" chung; $\mu$ gắn với "mục tiêu MC" trước khi có Monte Carlo; chưa nói $J_\mu$ dùng để làm gì và $v_\pi$ chưa biết; "quy trình quyết định Markov"; ghi chú dẫn tr. 32–36 rộng | Thiết lập dự đoán theo chính sách → Bài toán dự đoán với hàm xấp xỉ. Hai dòng thiết lập (MDP viết đầy đủ, phần thưởng bị chặn, $0\le\gamma<1$ hoặc mọi lượt kết thúc với xác suất 1; đặc trưng, tham số, dự đoán); "Chọn $w$ để $\hat v(\cdot,w)$ gần $v_\pi$" với $J_\mu$; $\mu$ là phân phối của các trạng thái dùng để học, thường là tần suất trạng thái khi chạy $\pi$; CSS cục bộ thu khoảng cách dọc để vừa khung; hộp: $v_\pi$ chưa biết nên phần sau thay $v_\pi(S_t)$ bằng mục tiêu cập nhật tính từ mẫu. Ghi chú diễn giả: đổi $\mu$ đổi nghiệm khi lớp hàm không chứa $v_\pi$; trường hợp liên tục; phân biệt $d_\pi$; nguồn tr. 23, 27, 34, $J_\mu$ bổ sung theo Sutton–Barto §9.2 | sửa | Mục topic-03 thành "## 4. Bài toán dự đoán và xấp xỉ tuyến tính" với "### 4.1. Bài toán dự đoán với hàm xấp xỉ"; nội dung cũ đặt dưới "### 4.2. Xấp xỉ tuyến tính" để viết lại ở bước L07-08; hai đoạn sẽ chuyển ở bước sau: khác biệt với học có giám sát sang mục của L07-12, mã hóa $e_a\otimes\psi$ sang mục của L07-10 (không dùng chú thích HTML vì trình xem hiển thị chúng thành chữ); bản đồ chủ đề đổi tên mục và nguồn |
| L07-08 | Định nghĩa xấp xỉ tuyến tính cho $\hat v$ và $\hat q$ | Thiếu $\hat q$ tuyến tính (nguồn tr. 24 có cả hai); không có câu nối từ tiêu chí $J_\mu$ sang chọn lớp hàm; ghi chú diễn giả chỉ nói kích thước; hình có nhiều lề trắng, nhãn kết quả "v̂" thiếu đối số | Giữ tiêu đề "Xấp xỉ tuyến tính". Câu mở: lớp hàm cho $\hat v$ là lớp tuyến tính theo tham số; công thức $\hat v=x(s)^Tw$, $\hat q=x(s,a)^Tw$; dòng kích thước $x(s),w\in\mathbb R^d$, tích là một số, $\nabla_w\hat v=x(s)$; gọi tên các lớp khác (nguồn tr. 25–26) không xét trong bài. `linear-pipeline.svg`: thu `viewBox` bỏ lề trắng, nhãn "v̂(s,w)", alt cụ thể. Ghi chú diễn giả: câu nối từ $J_\mu$, gradient không phụ thuộc $w$, lý do chọn lớp tuyến tính, $x(s,a)$ ở trang sau, không gian con $\{\hat v(\cdot,w)\}$, chi phí theo số thành phần khác 0. CSS cục bộ cỡ hình và khoảng cách | sửa | Viết lại "### 4.2. Xấp xỉ tuyến tính" khớp mặt trang (hai dạng, gradient, lý do chọn lớp, giới hạn không gian con); hai đoạn "Phân biệt với học có giám sát" và "Đặc trưng cho điều khiển" để cuối 4.2, sẽ chuyển ở bước L07-12 và L07-10; bài kiểm tra không gian con: lời giải dùng tổ hợp tuyến tính $aw_1+bw_2$ (bản cũ dùng tổ hợp lồi, không chứng minh được tính đóng) và định nghĩa $\Phi$ trước khi dùng |
| L07-09 | Đặc trưng phải được thiết kế theo miền bài toán | Tiêu đề "Đặc trưng phụ thuộc miền bài toán" là câu khẳng định; thiếu ví dụ vector đặc trưng và ba nhận xét của nguồn tr. 31; hộp dùng "return"; hình ba ô cao, chữ nhỏ | Đặc trưng phụ thuộc miền bài toán → Thiết kế đặc trưng. Ví dụ vector điều hướng (nguồn tr. 31) dạng cột, câu nêu vai trò thành phần hằng $1$; ba nhận xét theo tr. 31 ở cột phải; `feature-domains.svg` vẽ lại thành dải một hàng (`viewBox` 1120×200), nhãn lớn hơn, `desc`/alt nêu đại lượng từng miền. Ghi chú diễn giả: vai trò hệ số chặn, hình chỉ minh họa loại đại lượng (tr. 28–30), đặc trưng tốt giữ thông tin dự đoán lợi tức, nhập nhằng xét sau, câu nối sang đặc trưng cho $(s,a)$. CSS cục bộ: lưới .85fr/1.15fr, khối công thức cột ở .85em của `.math-large` (chữ KaTeX xấp xỉ cỡ chữ thân), hình cao tối đa 185px | sửa | Topic-04 thành "## 5. Đặc trưng và giới hạn biểu diễn" với "### 5.1. Thiết kế đặc trưng" (khớp tham chiếu "mục 5" ở 4.2): ví dụ vector, hệ số chặn, ba ví dụ miền, ba nhận xét, câu dẫn tới 5.2 và 5.3; bản đồ chủ đề đổi tên mục và kết nối ra |
| L07-10 | Đặc trưng cho cặp $(s,a)$ để xấp xỉ $\hat q$ | Tiêu đề "Một cách mã hóa giá trị hành động" chưa gọi tên khái niệm; deck thay định nghĩa nguồn $[\phi(s);\mathrm{onehot}(a);\phi(s)\otimes\mathrm{onehot}(a);1]$ bằng $e_a\otimes\phi(s)$ và ghi chú diễn giả nói hai thứ tự Kronecker "cho hai phân hoạch trọng số khác nhau" (sai: chỉ hoán vị tọa độ, cùng lớp hàm) | Một cách mã hóa giá trị hành động → Đặc trưng cho cặp trạng thái–hành động. Câu mở nối từ $\hat q=x(s,a)^Tw$; vector bốn khối theo nguồn tr. 31 kèm vai trò từng khối (phần chung, hằng số riêng của hành động, trọng số riêng trên $\phi(s)$, hệ số chặn chung); kích thước $p+m+mp+1$; ví dụ $\phi(s)\otimes e_1=(\phi_1;0;\phi_2;0)^T$ với $p=m=2$. Ghi chú diễn giả: tách $w$ thành bốn khối, $\hat q=\phi^T(w^{(1)}+u_a)+c_a+b$; không có khối Kronecker thì hành động tham lam như nhau ở mọi trạng thái; thứ tự Kronecker chỉ hoán vị tọa độ; đặc trưng ba chiều của ví dụ chuỗi; câu nối sang nhập nhằng | sửa (khôi phục định nghĩa nguồn) | Thêm "### 5.2. Đặc trưng cho cặp trạng thái–hành động" (định nghĩa, tích Kronecker, ví dụ, tách trọng số, vai trò khối, hoán vị tọa độ); bỏ đoạn $e_a\otimes\psi$ ở cuối 4.2. Outline hàng tr. 31 và note-for-author sửa theo |
| L07-11 | Nhập nhằng đặc trưng là giới hạn biểu diễn, không phải giới hạn dữ liệu | Tiêu đề "Nhập nhằng do đặc trưng" chưa kèm thuật ngữ nguồn; lập luận dừng ở hai trạng thái, chưa nối với lớp $\{\Phi w\}$ và khái niệm sai số xấp xỉ; ghi chú diễn giả một câu, thiếu câu nối sang phần Monte Carlo | Nhập nhằng do đặc trưng → Nhập nhằng đặc trưng (aliasing). Giữ phép suy $x(s_1)=x(s_2)\Rightarrow\hat v(s_1,w)=\hat v(s_2,w)\ \forall w$; thêm ví dụ đặc trưng hằng $x(s)=1$; hộp: mọi dự đoán nằm trong $\{\Phi w\}$ ($\Phi$ có hàng $x(s)^T$), sai số xấp xỉ là khoảng cách từ $v_\pi$ tới lớp này; câu hỏi giữ, đáp án thêm "muốn giảm phải đổi đặc trưng". Ghi chú diễn giả: chứng minh từ định nghĩa, $\Phi$ dùng lại ở phần Bellman chiếu; tách sai số xấp xỉ ($\min_w J_\mu$) với sai số ước lượng; câu nối sang mục tiêu cập nhật (nối hộp L07-07) | sửa | Thêm "### 5.3. Nhập nhằng đặc trưng (aliasing)" (phép suy, ví dụ, lớp $\{\Phi w\}$, hai loại sai số, câu nối) với bài kiểm tra mới: hai trạng thái cùng đặc trưng, $v_\pi=0$ và $2$, $\mu=\tfrac12$ mỗi trạng thái, dự đoán tốt nhất $c=1$, $J_\mu=\tfrac12$; bài $d_{\text{left}}$ chuyển về cuối 5.1; bản đồ chủ đề sửa kết nối ra |

### Phát hiện rà soát theo trang

| Mức độ | Trang | Vấn đề | Người rà | Quyết định | Trạng thái |
|---|---|---|---|---|---|
| trung bình | L07-01 (`index.html`, thẻ Bài 7) | Câu mô tả "Monte Carlo và TD(0) bán gradient" đọc thành Monte Carlo cũng dùng bán gradient | mạch (trung bình), toán (nhẹ) | "gradient Monte Carlo và bán gradient sai phân thời gian TD(0)" | đã sửa |
| nhẹ | L07-01 | Dòng nội dung thiếu Q-learning; "đặc trưng tuyến tính" dễ hiểu là đặc trưng là hàm tuyến tính | mạch | "Xấp xỉ tuyến tính theo đặc trưng, Monte Carlo, sai phân thời gian (TD), Sarsa và Q-learning" | đã sửa |
| trung bình | L07-02, ghi chú 1.1 | GLIE gán cho mọi phương pháp điều khiển; Q-learning dạng bảng chỉ cần thăm mọi cặp vô hạn lần và bước học Robbins–Monro | toán | "GLIE với điều khiển Monte Carlo và Sarsa" trên mặt trang và trong 1.1; ghi chú diễn giả nêu điều kiện của Q-learning dạng bảng | đã sửa |
| nhẹ | L07-02, ghi chú 1.1 | "thăm mọi cặp vô hạn lần" bỏ sót dự đoán theo trạng thái | toán, mạch | "thăm mọi trạng thái (hoặc cặp) vô hạn lần" | đã sửa |
| trung bình | L07-02 | Thẻ "Bài này": "Các bảo đảm hội tụ phải được xét lại" thiếu lý do | mạch | "Một cập nhật đổi ước lượng ở nhiều trạng thái, nên lập luận hội tụ theo từng ô không còn áp dụng trực tiếp" | đã sửa |
| nhẹ | L07-02, ghi chú 1.1 | Hộp ba điểm viết liền một đoạn, khó đọc; mục (2) diễn đạt khác thuật ngữ học theo/khác chính sách | mạch | Danh sách ba dòng mở bằng "Ba điểm đối chiếu Monte Carlo, TD, Sarsa và Q-learning trong bài:"; (2) "học theo chính sách hay khác chính sách". Để vừa khung, nhãn thẻ chuyển thành chữ đậm đầu đoạn và rút câu trong thẻ, không giảm cỡ chữ | đã sửa |
| nhẹ | Ghi chú 1 | Tên mục 1 trùng tên tiểu mục 1.1 | mạch | "## 1. Mở đầu", giữ "### 1.1. Từ bảng giá trị đến hàm xấp xỉ"; bản đồ chủ đề đổi theo | đã sửa |
| nhẹ | Ghi chú, phần tiên quyết | "quy trình quyết định Markov" sai thuật ngữ | mạch | "quá trình quyết định Markov" | đã sửa |
| nhẹ | L07-03, ghi chú 1.2, outline | Không có mục tiêu cho Q-learning | toán, mạch | Gộp mục tiêu cuối: "Phân biệt mục tiêu Sarsa và Q-learning; nhận diện bộ ba bất ổn (deadly triad)". Để vừa khung không giảm cỡ chữ, các mục tiêu trên mặt trang được rút còn một đến hai dòng ("trên ví dụ", "và giả thiết"); ghi chú 1.2 và outline giữ dạng đầy đủ | đã sửa |
| nhẹ | L07-03, ghi chú 1.2, outline | "gradient đầy đủ với bán gradient" chưa gắn với phương pháp | mạch | "gradient đầy đủ (Monte Carlo) với bán gradient (TD)" | đã sửa |
| nhẹ | L07-03 | Lần đầu "bộ ba bất ổn" trên mặt trang thiếu thuật ngữ gốc | mạch | Mục 5 danh sách xuống hai dòng khi thêm thuật ngữ, nên "(deadly triad)" đặt ở mục tiêu cuối trên mặt trang và trong ghi chú 1.2 | đã sửa |
| nhẹ | L07-04, ghi chú 2.1 | Ý 3 (dữ liệu không iid, không dừng) đặt cạnh hai giới hạn của bảng, dễ hiểu là khuyết điểm riêng của bảng | mạch | Mở ý bằng "Với mọi cách biểu diễn, dữ liệu…"; ghi chú 2.1 bỏ câu giải thích trùng | đã sửa |
| nhẹ | L07-04, ghi chú 2.1 | Câu mở dùng dấu hai chấm kiểu tiết lộ | mạch | "…cho từng trạng thái hoặc cặp trạng thái–hành động. Cách này dễ phân tích nhưng khó mở rộng." | đã sửa |
| nhẹ | L07-04, ghi chú 2.1 | "hai trạng thái gần nhau" chưa sát nguồn ("na ná nhau") | mạch | "hai trạng thái có tính chất giống nhau" | đã sửa |
| nhẹ | L07-05, ghi chú 3.1 | "một cập nhật làm thay đổi dự đoán ở nhiều trạng thái" phát biểu tuyệt đối; hộp trùng ý chia sẻ thông tin | toán, mạch | "có thể làm thay đổi"; ghi chú diễn giả và 3.1: xảy ra khi đặc trưng không trực giao, đặc trưng one-hot đưa mô hình về bảng tra; ý 2 đổi thành "Chia sẻ thông tin giữa các trạng thái", hộp giữ vai trò hệ quả nối sang trang sau | đã sửa |
| trung bình | L07-05 | Chữ trong hình khoảng 0.65 cỡ chữ thân | mạch | Vẽ lại SVG với nhãn 30–40 đơn vị trên khung 1060×280; hình cao tối đa 245px; ba lợi ích gộp thành hai dòng để lấy chỗ, không giảm cỡ chữ thân | đã sửa |
| trung bình | L07-05 | Hình không thể hiện $w$ trên đường tới $\hat v$; nhãn "x(s)" chưa gọi tên; tiêu đề hộp "Mô hình tham số" | mạch | Hộp "đặc trưng x(s)"; nhãn $w$ trên mũi tên tới $\hat v(s,w)$; tiêu đề "Hàm có tham số"; cập nhật `title`, `desc` và alt | đã sửa |
| nhẹ | Ghi chú 3.1 | Câu mở "Ý tưởng của nguồn…" vòng vo | mạch | "Thay bảng bằng một hàm có tham số (nguồn tr. 23):" | đã sửa |
| nhẹ | L07-06, ghi chú 3.2 | Sai lệch $e$ chỉ mô tả trường hợp dự đoán thấp hơn mục tiêu | mạch | "Với sai lệch $e$ = mục tiêu cập nhật − $\hat v(s,w)$, cộng vào $w$ lượng $\Delta w=\alpha e\,x(s)$"; ghi chú diễn giả nêu ví dụ $e=2>0$ | đã sửa |
| nhẹ | L07-06, ghi chú 3.2 | "tổ hợp tuyến tính của vector đặc trưng" chưa nói hệ số là $w$ | mạch | "tổ hợp tuyến tính các thành phần của $x(s)$ với hệ số $w$" | đã sửa |
| nhẹ | L07-06 và các trang có vector thập phân | Cách viết vector thập phân chưa thống nhất | mạch | Ghi quy ước dấu chấm phẩy ở đầu bảng từng trang; áp dụng dần ở L07-14, L07-19, L07-30, X02, X03 | đã ghi quy ước; các trang sau theo dõi |
| nhẹ | Ghi chú 3.1, 3.2 | Ý trực giao và one-hot đặt ở 3.1, trước ví dụ | mạch | Chuyển sang 3.2 sau công thức mức lan; 3.1 giữ một câu hệ quả | đã sửa |
| nhẹ | L07-06 (ghi chú diễn giả), ghi chú 3.2 | Câu chốt "Đó là cái giá của tổng quát hóa." | mạch | Gộp vào câu trước | đã sửa |
| nhẹ | L07-07, ghi chú 4.1 | Thiếu điều kiện để $v_\pi$ tồn tại; "lượt kết thúc với lợi tức hữu hạn" chưa chặt; dòng $S_t$, $R_{t+1}$, $\gamma$ dồn ý | toán, mạch | Ý 1 "…MDP có phần thưởng bị chặn"; ý 2 "$0\le\gamma<1$, hoặc mọi lượt kết thúc với xác suất 1"; bỏ dòng miền $S_t$, $R_{t+1}$ khỏi mặt trang (giữ trong 4.1); ghi chú nêu vai trò của điều kiện (nguồn tr. 7–8) | đã sửa |
| nhẹ | L07-07 (ghi chú diễn giả), ghi chú 4.1 | Dẫn Sutton–Barto chưa nói $J_\mu$ tương ứng đại lượng nào | toán | "tương ứng sai số giá trị $\overline{VE}$ ở Sutton và Barto, ấn bản 2, §9.2, thêm hệ số $\tfrac12$ để gọn đạo hàm" | đã sửa |
| trung bình | L07-07, ghi chú 4.1 | Không nói $\mu$ lấy từ đâu | mạch | "$\mu$ là phân phối của các trạng thái dùng để học, thường là tần suất trạng thái khi chạy $\pi$; $\mu(s)$ lớn được ưu tiên" | đã sửa |
| nhẹ | L07-07 (ghi chú diễn giả), ghi chú 4.1 | Thiếu câu nối vì sao cần $J_\mu$ | mạch | "Muốn sửa $w$ có hướng, cần một tiêu chí đo $\hat v$ gần $v_\pi$ đến đâu; $J_\mu$ là tiêu chí đó" | đã sửa |
| nhẹ | L07-08 | Câu mở chỉ nói lớp hàm cho $\hat v$ trong khi trang định nghĩa cả $\hat q$ | toán | "Lớp hàm cho $\hat v$ và $\hat q$ trong bài là lớp tuyến tính theo tham số…" | đã sửa |
| nhẹ | L07-08 | $x(s,a)$ xuất hiện trên mặt trang chưa có tên; ghi chú diễn giả trỏ "trang sau" trong khi đặc trưng cặp được xây dựng ở L07-10 | mạch | Dòng "$x(s),x(s,a),w\in\mathbb R^d$; $x(s,a)$ là đặc trưng của cặp trạng thái–hành động"; ghi chú diễn giả "được xây dựng ở phần thiết kế đặc trưng" | đã sửa |
| nhẹ | L07-08 | Đoạn cuối dồn kích thước, gradient và phạm vi các lớp khác | mạch | Gradient đưa vào dòng công thức lớn; dòng kích thước và dòng phạm vi tách riêng | đã sửa |
| nhẹ | L07-08 (ghi chú diễn giả) | Câu mở nói về trang ("Trang trước…; trang này…"); thiếu câu nối sang thiết kế đặc trưng | mạch (no-ai-slop) | "Sau tiêu chí $J_\mu$, cần chọn dạng của $\hat v$."; thêm câu: chất lượng xấp xỉ phụ thuộc việc đặc trưng $x$ được thiết kế theo miền bài toán | đã sửa |
| nhẹ | Ghi chú 4.2 | Tham chiếu "mục 5" cho thiết kế đặc trưng trong khi mục đó chưa đánh số | toán | Giữ; đánh số mục thiết kế đặc trưng là 5 ở bước L07-09 | theo dõi |
| trung bình | L07-09 | Câu mở chỉ giới thiệu ví dụ "của nguồn", chưa nêu luận điểm của trang | mạch | "Mô hình tuyến tính chỉ dùng thông tin trong $x(s)$, nên $x(s)$ phải chứa các đại lượng quyết định lợi tức. Ví dụ điều hướng (nguồn tr. 31):"; ý hệ số chặn chuyển vào ghi chú diễn giả | đã sửa |
| trung bình | L07-09 (`feature-domains.svg`) | Nhãn CartPole "x, ẋ, θ, θ̇" trùng ký hiệu vector đặc trưng $x$ | mạch | Nhãn chữ "vị trí, vận tốc xe; góc, vận tốc góc"; sửa `desc`, alt | đã sửa |
| nhẹ | L07-09 | "Nhập nhằng" chưa được giải thích trên mặt trang | mạch | Ba nhận xét rút thành một dòng mỗi ý để vừa khung, nên định nghĩa không đặt trên mặt trang; ghi chú diễn giả và ghi chú 5.1 nêu định nghĩa, trang L07-11 xét riêng | đã sửa (trong ghi chú) |
| nhẹ | L07-09 | Dải hình thiếu chú thích | mạch | Chú thích "Loại đại lượng thường dùng làm đặc trưng ở ba miền (nguồn tr. 28–30)."; hình cao tối đa 170px | đã sửa |
| nhẹ | review-log, hàng L07-09 | Mô tả "vẫn lớn hơn chữ thân" cho khối công thức .85em không đúng | toán | "chữ KaTeX xấp xỉ cỡ chữ thân" | đã sửa |
| trung bình | L07-10 | Hệ quả quan trọng (thiếu khối Kronecker thì hành động tham lam như nhau ở mọi trạng thái) chỉ có trong ghi chú diễn giả | mạch | Đưa lên mặt trang thành hộp; ví dụ $p=m=2$ chuyển vào ghi chú diễn giả (5.2 giữ ví dụ); kích thước $p+m+mp+1$ đưa vào câu mở | đã sửa |
| trung bình | L07-10 | Danh sách gán vai trò cho chính đặc trưng thay vì trọng số đi kèm | mạch | "$\phi(s)$ → trọng số $w^{(1)}$ dùng chung; $e_a$ → hằng số $c_a$; $\phi(s)\otimes e_a$ → trọng số $u_a$ riêng của $a$ trên $\phi(s)$; $1$ → hệ số chặn chung $b$"; thêm dòng $\hat q=\phi(s)^T(w^{(1)}+u_a)+c_a+b$ | đã sửa |
| nhẹ | L07-10 | Câu mở thiếu nghĩa của one-hot; vị trí dẫn nguồn | mạch | "mã one-hot $e_a$ (một thành phần bằng 1), nguồn (tr. 31) ghép bốn khối"; bỏ câu "Điều khiển cần $\hat q=x^Tw$" vì đã có ở L07-08, để vừa khung | đã sửa |
| nhẹ | L07-10 (ghi chú diễn giả), ghi chú 5.2 | Chưa nêu tính dư của mã hóa: khối $\phi(s)$ và $1$ là tổ hợp tuyến tính của khối Kronecker và $e_a$ | toán | Thêm: lớp hàm trùng với lớp của $[e_a;\phi(s)\otimes e_a]$, ma trận đặc trưng không đủ hạng cột, $w$ không duy nhất; hai khối dư giữ phần dùng chung | đã sửa |
| nhẹ | L07-27 (theo dõi) | Với đặc trưng $[d_{\text{trái}}(s);u(a);1]$, $\hat q(s,1)-\hat q(s,0)=-2w_2$ với mọi $s$, nên hành động tham lam như nhau ở B, C, D | toán | Nêu nhận xét này ở L07-27 và nối với hệ quả của L07-10 | theo dõi |
| nhẹ | L07-11 (ghi chú diễn giả), ghi chú 5.3 | "Sai số xấp xỉ là khoảng cách… tức $\min_w J_\mu$" đồng nhất khoảng cách với $J_\mu$ (thực ra $J_\mu$ là nửa bình phương khoảng cách) | toán | "được đo bằng $\min_w J_\mu(w)$, bằng một nửa bình phương khoảng cách (chuẩn trọng số $\mu$) từ $v_\pi$ tới lớp $\{\Phi w\}$"; lời giải bài kiểm tra nêu khoảng cách 1 | đã sửa |
| nhẹ | L07-11 | Câu hỏi nói "sai số này" chưa rõ loại; đáp án chưa đối chiếu với sai số ước lượng | mạch | "…có loại bỏ được sai số xấp xỉ không?"; đáp án "Không: đây là giới hạn của lớp hàm, khác sai số ước lượng vốn giảm khi thêm mẫu." ("muốn giảm phải đổi đặc trưng" chuyển vào ghi chú diễn giả) | đã sửa |
| nhẹ | L07-11 | Hộp chưa nói khoảng cách đo theo trọng số nào và $\Phi$ cần $\mathcal S$ hữu hạn | mạch | "($\mathcal S$ hữu hạn)" sau $\Phi$; "khoảng cách (theo trọng số $\mu$ của $J_\mu$)" | đã sửa |
| nhẹ | L07-11 (ghi chú diễn giả), ghi chú 5.3 | Câu nối mở bằng siêu ngôn ngữ ("Phần này đã xác định…", "Như hộp ở trang…") | mạch (no-ai-slop) | "Vì $v_\pi$ chưa biết, phần tiếp theo xác định mục tiêu cập nhật tính từ mẫu để học $w$." | đã sửa |
