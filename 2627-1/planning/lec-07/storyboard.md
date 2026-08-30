# Storyboard Bài 07

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/thuật toán | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Cốt lõi | Linh hoạt |
|---|---|---|---|---|---|---|---|---:|---:|
| Định hướng | `L07-01`, `L07-02` | `L07-02` | không áp dụng: chỉ nối từ Bài 06 | không áp dụng | `L07-03` xác định sản phẩm học tập | `L07-03` | kết quả dạng bảng → phạm vi mới | 7 | 0 |
| Xấp xỉ và đặc trưng | `L07-04` | `L07-05` | `L07-06` | `L07-07`, `L07-08`, `L07-10` | `L07-09`, `L07-11` | `L07-11` | bảng tra → mô hình tuyến tính có miền, kích thước và giới hạn biểu diễn | 21 | 2 |
| MC tuyến tính | `L07-12` | `L07-13` | `L07-14` | `L07-15`, `L07-16` | `L07-16`, `X02` | `L07-16`, `X01` | return $G_t$ → gradient đầy đủ và cập nhật tuần tự | 19 | 2 |
| TD tuyến tính và Bellman chiếu | `L07-18` | `L07-18` | `L07-19`; ví dụ hình học `L07-21` | `L07-20`, `L07-22`, `L07-23` | `L07-24` | `L07-24`, `L07-35` | chuyển tiếp một bước → bán gradient → hình chiếu → trực giao → điểm cố định | 26 | 4 |
| So sánh MC–TD | `L07-25` | `L07-25` | không áp dụng: tổng hợp hai cụm đã có ví dụ | không áp dụng | `L07-25` | `L07-25` | hai đích đã học → phân biệt đối tượng phân tích | 3 | 0 |
| Điều khiển | `L07-26` | `L07-26`, `L07-28` | `L07-27` | `L07-28`, `L07-29` | `L07-30` | `L07-28`, `X03` | đặc trưng $x(s,a)$ → SARSA với chính sách $\varepsilon$-greedy hiện hành | 18 | 1 |
| Khác chính sách và bất ổn | `L07-31` | phần mở đầu `L07-31` | so sánh đích trên mẫu `L07-30` | quy tắc đích ở `L07-31`; phân loại ở `L07-32` | `L07-33`, `L07-34` | `L07-31`, `L07-33`, `L07-35` | đổi hành động kế tiếp sang cực đại → nhận diện trường hợp cần phân tích riêng | 16 | 1 |

Các khoảng trang trên không chồng lấn. Tổng phần chính là 110 phút cốt lõi và 10 phút linh hoạt; tổng chữa bài là 30 phút (`X01`: 8, `X02`: 10, `X03`: 12). Ký hiệu $x$, $w$, $G_t$ và $\delta_t$ được truyền nguyên dạng từ ví dụ sang công thức và bài tập.

## Bản đồ từng trang

| Mã | Luận điểm và bước học | Nguồn | Phút | Câu nối |
|---|---|---|---:|---|
| `L07-01` | Mở bài: thay bảng bằng hàm tham số. | tr. 1–4, 21–23 | 2 | Từ tên bài sang giới hạn của kết quả dạng bảng. |
| `L07-02` | Nêu giới hạn: kết quả dạng bảng không tự chuyển sang xấp xỉ. | tr. 5–20 | 3 | Xác định phần kiến thức mới cần xây dựng. |
| `L07-03` | Nêu sản phẩm học tập có thể kiểm tra. | tr. 21–44 | 2 | Ba trục phân tích (loại đích, quan hệ hành vi–đích, cách cải thiện chính sách) dẫn đường cho toàn bộ các mạch sau. |
| `L07-04` | Vấn đề: bộ nhớ, mẫu và thiếu tổng quát hóa. | tr. 22–23 | 3 | Dùng chung tham số để chia sẻ thông tin. |
| `L07-05` | Trực giác: một vector thay nhiều ô. | tr. 22–24 | 2 | Quan sát hệ quả của một cập nhật. |
| `L07-06` | Ví dụ số: một cập nhật đổi hai dự đoán qua tham số chung. | tr. 23, 31–32 | 3 | Khái quát ví dụ thành thiết lập dự đoán. |
| `L07-07` | Thiết lập dự đoán theo chính sách với phân phối MC $\mu$. | tr. 23, 27, 32–36 | 4 | Chọn lớp hàm tuyến tính. |
| `L07-08` | Hình thức: $\hat v=x^Tw$ và gradient. | tr. 24 | 3 | Đặc trưng x phải đến từ miền bài toán. |
| `L07-09` | Ví dụ đặc trưng trong ba miền. | tr. 28–31 | 3 | Mở rộng đặc trưng sang hành động. |
| `L07-10` | Hình thức: một mã hóa khối $e_a\otimes\phi(s)$ cho $q$. | tr. 31 | 3 | Kiểm tra giới hạn và các mã hóa khác. |
| `L07-11` | Kiểm tra: aliasing không mất đi khi thêm dữ liệu. | tr. 31 | 2 | Phân loại đích trước khi lấy gradient. |
| `L07-12` | Vấn đề: đích phụ thuộc tham số làm đổi đường đạo hàm. | tr. 32–35 | 3 | Xét đích không phụ thuộc $w$ trước. |
| `L07-13` | Trực giác và định nghĩa return MC. | tr. 27, 33–34 | 3 | Dùng một mẫu để xác định hướng sửa. |
| `L07-14` | Ví dụ số MC trước khi đạo hàm. | suy ra từ tr. 33 | 4 | Khái quát hướng sửa bằng gradient. |
| `L07-15` | Hình thức: MC là gradient đầy đủ. | tr. 32–34; HW4 | 4 | Đóng gói thành thuật toán. |
| `L07-16` | Thuật toán MC tuyến tính, ứng dụng chia sẻ và kiểm tra. | tr. 33–34; HW4, HW7 | 3 | Nêu điều kiện để lặp cập nhật có bảo đảm. |
| `L07-17` | Hai nhóm điều kiện MC–SGD; đủ hạng chỉ để có nghiệm tham số duy nhất. | tr. 27, 34 | 4 | Đổi đích sang bootstrap một bước. |
| `L07-18` | Vấn đề và trực giác TD: cập nhật sớm bằng dự đoán kế tiếp. | tr. 27, 35–36 | 4 | Tính một chuyển tiếp trước khi khái quát. |
| `L07-19` | Ví dụ số TD một bước, gồm chỉ số và hướng cập nhật. | suy ra từ tr. 35–36 | 4 | Khái quát thành bán gradient và thuật toán. |
| `L07-20` | Hình thức và giao diện thuật toán TD tuyến tính. | tr. 32, 35–36 | 4 | Xem ảnh Bellman có nằm trong lớp biểu diễn không. |
| `L07-21` | Trực giác và ví dụ hình học: Bellman đưa giá trị ra ngoài lớp biểu diễn. | HW5 | 4 | Chuyển phép chiếu thành điều kiện trực giao. |
| `L07-22` | Điều kiện trực giao và phép khai triển thành $Aw=b$. | HW5 | 4 | Viết điểm cố định chiếu. |
| `L07-23` | Hình thức: điểm cố định Bellman chiếu. | HW5 | 6 | Gắn phương trình với điều kiện hội tụ. |
| `L07-24` | Điều kiện dữ liệu, bước học và tính ổn định của hệ trung bình TD. | tr. 35–37; HW5–6 | 4 | So sánh đích MC và TD trước khi điều khiển. |
| `L07-25` | So sánh cấu trúc đích và đối tượng phân tích. | tr. 33–37 | 3 | Thay V bằng Q để chọn hành động. |
| `L07-26` | Vấn đề điều khiển và hai chính sách. | tr. 38–39 | 3 | Chọn đặc trưng hành động cho ví dụ. |
| `L07-27` | Ví dụ chuỗi, mã hóa ba chiều, $\gamma=1$ và chân trời hữu hạn. | HW7–8 | 5 | Dùng hành động kế tiếp thật trong SARSA. |
| `L07-28` | Trực giác SARSA với chính sách $\varepsilon$-greedy hiện hành. | tr. 38–39; HW8 | 3 | Viết thuật toán control đầy đủ. |
| `L07-29` | Thuật toán SARSA control, phá hòa và cảnh báo hội tụ. | tr. 38–39 | 4 | Thực hiện một bước số. |
| `L07-30` | Ví dụ bước đầu của HW8 với $\gamma=1$. | HW8 | 4 | So đích trên cùng mẫu khi thay hành động kế tiếp bằng cực đại. |
| `L07-31` | Quy tắc đích Q-learning, trường hợp kết thúc, miền cực đại và kiểm tra. | tr. 38–41 | 4 | Phân loại ba cơ chế của thiết lập khác chính sách. |
| `L07-32` | Hình thức hóa bộ ba bất ổn và mức khẳng định có điều kiện. | tr. 41 | 3 | Áp dụng phân loại vào Q-learning vừa xét. |
| `L07-33` | Ứng dụng và kiểm tra bằng ba câu chẩn đoán. | tr. 41–43 | 3 | Đặt kết luận vào đúng phạm vi lý thuyết. |
| `L07-34` | Ranh giới của bốn thiết lập. | tr. 34, 41–44 | 3 | Kiểm tra toàn bộ mạch suy luận. |
| `L07-35` | Kiểm tra tổng hợp năm bước. | tổng hợp | 2 | Nối các khái niệm sang bài học sâu. |
| `L07-36` | Kết: bảo đảm tuyến tính không tự chuyển sang Deep Q-Network. | tr. 26, 41–45 | 2 | Chuyển sang phần bài tập dọc. |
| `X01` | Chữa HW4: đạo hàm MC. | HW4 | 8 | Từ công thức sang cập nhật tuần tự. |
| `X02` | Chữa HW7: ba cập nhật MC. | HW7 | 10 | Giữ cùng đặc trưng cho SARSA. |
| `X03` | Chữa HW8: ba cập nhật SARSA. | HW8 | 12 | Kết thúc bằng kiểm tra chỉ số và terminal. |

Mười phút linh hoạt nằm trong các khoảng không chồng lấn: `L07-04`–`L07-11` (2), `L07-12`–`L07-17` (2), `L07-18`–`L07-25` (4), `L07-26`–`L07-30` (1), `L07-31`–`L07-36` (1). Có thể rút phần trao đổi ở `L07-06`, `L07-16`, `L07-22`, `L07-23`, `L07-30` và `L07-33`. Không hiển thị phân tuyến hoặc thời lượng trên trang chiếu và ghi chú.

## Bản đồ sáu mạch

Bảy cụm khái niệm được chứa trong sáu mạch; cụm so sánh MC–TD nằm cuối M4.

| Mạch | Chức năng | Kết nối vào | Đầu ra | Cụm chứa | Trang |
|---|---|---|---|---|---|
| M1 | Mở đầu, cầu nối từ dạng bảng, ba trục phân tích và đích học tập | Kết quả dạng bảng của Bài 06 | Ba trục dùng xuyên bài và kỳ vọng học tập | Định hướng | `L07-01`–`L07-03` |
| M2 | Lý do cần xấp xỉ, chia sẻ tham số, đặc trưng và giới hạn biểu diễn | Ba trục của M1 | Lớp hàm tuyến tính với miền, kích thước và giới hạn rõ | Xấp xỉ và đặc trưng | `L07-04`–`L07-11` |
| M3 | Phân loại đích, MC tuyến tính từ ví dụ đến thuật toán và điều kiện | Lớp hàm của M2 | Thuật toán MC tuyến tính và điều kiện SGD | MC tuyến tính | `L07-12`–`L07-17` |
| M4 | TD(0), bán gradient, Bellman chiếu và so sánh MC–TD | Đích MC của M3 | Điểm cố định Bellman chiếu; bảng so sánh hai đích | TD tuyến tính và Bellman chiếu; so sánh MC–TD (cuối mạch) | `L07-18`–`L07-25` |
| M5 | Điều khiển: giá trị hành động, SARSA tuyến tính và cập nhật số | Điểm cố định và so sánh của M4 | Thuật toán SARSA control và một bước số | Điều khiển | `L07-26`–`L07-30` |
| M6 | Q-learning, deadly triad, phạm vi lý thuyết, kết luận và chữa bài dọc | SARSA của M5 | Phân biệt đích max, chẩn đoán bất ổn, ranh giới lý thuyết | Khác chính sách và bất ổn | `L07-31`–`L07-36` |

## Hàng chữa bài trong hành trình

Ba trang dọc `X01`–`X03` là hàng chữa bài 30 phút, nằm ngoài 120 phút chính: `X01` (8 phút) đạo hàm MC, `X02` (10 phút) cập nhật MC tuần tự, `X03` (12 phút) ba bước SARSA. Các trang dọc nằm trong M6 về vị trí trình chiếu nhưng thời lượng chữa bài không tính vào 120 phút chính.
