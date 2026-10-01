# Storyboard mới Bài 04

Bài 04 — Giải MDP bằng quy hoạch động. Học phần Học tăng cường, học kỳ 1 năm học 2026–2027. Người học: sinh viên đại học đã học học máy, học sâu và thuật toán; tiên quyết dùng trực tiếp là MDP, xác suất có điều kiện, tổng chiết khấu, vector, chuẩn vô cùng được định nghĩa lại và hệ tuyến tính.

Vấn đề trung tâm: từ mô hình chuyển–thưởng đã biết, tính giá trị của một chính sách, cải thiện lựa chọn và tìm chính sách tối ưu có điều kiện kiểm chứng. Phần trình chiếu gồm **45 trang, 7 mạch, 120 phút**; thời gian đã gồm các câu kiểm tra riêng và chữa ngắn. **30 phút còn lại của buổi 150 phút dành cho chữa bài tập** theo nguồn; không tự tạo code demo vì PDF và tài liệu tuần 4 không có chương trình.

Đây là bản dàn bài mới, không dùng dàn bài cũ làm khung. Chỉ dẫn cụ thể của người dùng cho phép thay thứ tự nguồn để theo Sutton–Barto chương 4: đánh giá → cải thiện → lặp chính sách → lặp giá trị → bất đồng bộ/GPI/hiệu quả. Chủ đề và dữ kiện của PDF nguồn được bảo toàn qua ánh xạ đủ 38 trang. Kế hoạch đã được chấp nhận và triển khai ngày 2026-09-28. Năm vai đã rà độc lập cùng bản cố định; các sửa cục bộ sau rà được cập nhật trong hồ sơ này. Bằng chứng kiểm định và trạng thái rà lại nằm trong review-log.md.

## Bản đồ hành trình

| Mạch | Vai trò | Đầu vào | Đầu ra và đóng góp | Trang | Phút | Kiểm tra riêng |
|---|---|---|---|---|---:|---|
| A. Mở đầu | Thiết lập bài toán | MDP, xác suất có điều kiện và tổng chiết khấu | Mô hình hai trạng thái và nhu cầu đánh giá một chính sách cố định | L04-A01–L04-A05 | 10 | L04-A05 |
| B. Đánh giá chính sách | Phát triển kiến thức và luyện tập | Mô hình đã biết và chính sách cố định | Giá trị chính xác hoặc bảng có phần dư; làm đầu vào so sánh hành động | L04-B01–L04-B08 | 22 | L04-B08 |
| C. Cải thiện chính sách | Phát triển kiến thức và luyện tập | Giá trị của chính sách đã đánh giá | Chính sách mới không kém; nhu cầu đánh giá lại chính sách mới | L04-C01–L04-C07 | 20 | L04-C07 |
| D. Lặp chính sách | Phát triển thuật toán và luyện tập | Đánh giá, cải thiện, tính co theo chính sách | Chính sách ổn định và điều kiện tối ưu; giới hạn chi phí đánh giá đầy đủ | L04-D01–L04-D06 | 18 | L04-D06 |
| E. Lặp giá trị | Phát triển thuật toán và luyện tập | Lặp chính sách và nhu cầu cắt ngắn đánh giá | Cập nhật tối ưu, phần dư và chính sách trích; nhu cầu phân bổ công việc | L04-E01–L04-E08 | 22 | L04-E08 |
| F. Quy hoạch động trong thực hành | Tổ chức tính toán và giới hạn | Cập nhật kỳ vọng, lặp chính sách, lặp giá trị | Lịch cập nhật, điều kiện bao phủ, GPI và giới hạn mô hình | L04-F01–L04-F06 | 16 | L04-F06 |
| G. Tổng hợp và bài tập | Kết luận và vận dụng tổng hợp | Kết quả của sáu mạch trước | Kiểm tra nghiệm, so sánh phương pháp theo giả thiết; bài tập và tài liệu đọc | L04-G01–L04-G05 | 12 | L04-G04 |


Mạch A thiết lập quyết định cần tối ưu và dữ kiện. B cung cấp giá trị của một chính sách. C dùng giá trị đó để thay hành động. D lặp hai phép toán và xác định điều kiện tối ưu. E cắt ngắn đánh giá để xây cập nhật tối ưu có chứng nhận sai số. F thay lịch và xem giới hạn mô hình. G quay lại nghiệm, kiểm chứng và bài tập. Thứ tự này theo yêu cầu mới về chương 4, thay cấu trúc nguồn bắt đầu bằng toàn bộ hệ tối ưu Bellman.

## Chu trình của các cụm trọng tâm

| Cụm | Vấn đề | Trực giác | Ví dụ trước hình thức | Hình thức/quy trình | Ứng dụng sau hình thức | Kiểm tra | Phút |
|---|---|---|---|---|---|---|---:|
| Nhắc mô hình và tổng thưởng | L04-A03 | L04-A03–A04 | L04-A04 | L04-A03 nhắc tiên quyết; công thức tổng thưởng ở A05 là tiên quyết | Quỹ đạo cụ thể L04-A05 | L04-A05 | 10 |
| KN1 đánh giá | L04-B01 | L04-B01 | L04-B02 | L04-B03–B06; quy trình đủ B05 | L04-B07, giải hệ và đối chiếu bảng lặp | L04-B08 | 22 |
| KN2 cải thiện | L04-C01 | L04-C01 | L04-C02 | L04-C03–C05; quy tắc chọn đủ C04 | L04-C06, đổi chính sách rồi đánh giá lại | L04-C07 | 20 |
| KN3 lặp chính sách | L04-D01 | L04-D01 | L04-D02 | L04-D03; điều kiện D04–D05 | L04-D04, chứng nhận cặp $(b,b),(27,30)$ | L04-D06 | 18 |
| KN4 lặp giá trị | L04-E01 | L04-E01 | L04-E02 | L04-E03–E05; quy trình đủ E04 | L04-E06 lưới và E07 phần dư | L04-E08 | 22 |
| KN5 bất đồng bộ | L04-F01 | L04-F02 | L04-F02 | L04-F03 | L04-F03, kiểm phần dư sau lịch ngược trên lưới | L04-F06 | 9, gồm F01–F03 và phần lịch ở F06 |
| KN6 GPI, KN7 mô hình gộp | L04-F04–F05 tổng hợp giới hạn đã có | Sơ đồ hai quá trình F04; bốn biến F05 | PI/VI đã tính, 324 tổ hợp F05 | Định nghĩa GPI F04 và ánh xạ F05 | Phân loại PI/VI/bất đồng bộ và nêu mô hình còn thiếu | Phần mô hình ở L04-F06 | 7; tổng F là 16 |
| Tổng hợp và luyện tập | Thu hồi bài toán L04-G01 | Liên hệ hai quy trình L04-G01–G02 | Lưới nhiễu L04-G03 | Không thêm khái niệm trọng tâm | Lập kỳ vọng G03 và kiểm nghiệm G04 | L04-G04 | 12 |

Chu trình A và G được rút gọn có chủ ý: A chỉ nhắc kiến thức đã học và thiết lập nhu cầu; G không thêm định nghĩa. GPI là khái niệm hỗ trợ mô tả các quy trình đã thực hiện; ví dụ là chính các lần lặp đã học, không mở thuật toán mới. CartPole là ứng dụng điều kiện mô hình, không dạy thuật toán rời rạc hóa mới. Các bước “không áp dụng” ở G là định nghĩa/chứng minh mới, vì đưa thêm chúng sẽ phá chức năng kết luận.

F02 là ví dụ dẫn nhập đồng thời làm cụ thể vấn đề F01: một lượt quét có thể truyền thông tin nhanh hơn nếu giá trị mới được dùng ngay. Ví dụ đánh giá hai trạng thái truyền cơ chế đọc giá trị mới nhất, không truyền nguyên bảng $(1,2)$ sang $T_*$. Ví dụ lặp giá trị tại chỗ trên lưới truyền toán tử tối ưu và lịch $c_4,c_3,c_2,c_1$: $c_4$ nhận $10$, rồi $c_3$ nhận $\max\{-1,8\}=8$. F03 có ứng dụng sau hình thức: chạy lịch ngược đã nêu, cố định bảng cuối để xác nhận phần dư 0 và trích chính sách. F06 kiểm tra cả lịch bao phủ và mô hình; phân bổ 1 phút của câu kiểm tra cho lịch và 2 phút cho mô hình tạo tổng thời gian trong bảng trên.

### Dữ kiện và ký hiệu được truyền

| Cụm | Đầu vào và dữ kiện giữ nguyên | Sản phẩm học tập | Giới hạn cần bảo toàn |
|---|---|---|---|
| B | Bốn cạnh từ A04, $\pi_0=(a,a)$, $\gamma=0.9$, $V_0=0$ | Hai lượt tính và nghiệm $(10,11)$; phần dư gắn với bảng đúng | $V_k$ không phải $v_{\pi_k}$; chỉ số k không phải t |
| C | $v_{\pi_0}=(10,11)$ từ B07 | $q$ của cùng chính sách, $(a,b)$ và $(10,30)$ | Điểm 12.9 là tiếp tục theo chính sách cũ, khác 30 |
| D | $(a,b)$, $(10,30)$ và hành động b tại $s_0$ | Chuỗi PI đầy đủ, cặp chính sách–giá trị nhất quán | Đánh giá chính xác, giữ hòa; mọi kết luận hữu hạn có điều kiện |
| E | Cùng MDP hai trạng thái, bảng không, cơ chế nhìn trước | $(1,3)$ rồi $(2.7,5.7)$, toán tử và phần dư | $Q_V$ chỉ là ký hiệu phụ; max ở ngoài kỳ vọng |
| E lưới | $c_1\ldots c_5$, thưởng -1/10, biên trái, terminal 0 | Bảng nguồn, chính sách phải và kiểm $V_5=V_4$ | Thưởng nhận khi vào đích; không cộng tiếp sau kết thúc |
| F | Phép đánh giá/lặp giá trị đã học, lịch cập nhật chỉ định | Phân biệt đồng bộ/tại chỗ/bất đồng bộ; GPI và điều kiện mô hình | Không bỏ trạng thái; không suy Markov từ 324 ô |
| G | Bảng $(27,30)$; lưới thêm xác suất 0.8/0.1/0.1 | Kiểm chứng tối ưu và phép tính kỳ vọng có mô hình | Các quy ước bổ sung ở bài tập được nêu công khai |

## Đặc tả trực quan

| Tệp SVG dự kiến trong img/lec-04 | Trang dùng | Đối tượng và kết luận | Nguồn/quyết định |
|---|---|---|---|
| dp04-roadmap.svg | L04-A02 | Năm thành phần từ đánh giá đến tổ chức lịch cập nhật; nhãn đầu ra của từng thành phần | Sơ đồ hóa bản đồ nội dung đã duyệt, không thêm khái niệm |
| dp04-two-state.svg | L04-A04 và các ví dụ B–E | Hai nút, bốn cung, nhãn hành động/thưởng và gamma; chiều mũi tên phân biệt các nhánh | Vẽ lại NG1 tr. 17, không thay dữ kiện |
| dp04-expectation-backup.svg | L04-B01 | Trung bình theo chính sách rồi theo chuyển–thưởng; giá trị tiếp nối có nhãn | Vẽ sơ đồ cơ chế từ NG2 §4.1 |
| dp04-one-step-choice.svg | L04-C02 | Hai nhánh từ s1, phần thưởng 2/3, giá trị tiếp nối 10/11 | Vẽ lại quan hệ NG1 tr. 19, chỉ tiếp tục theo pi0 |
| dp04-policy-iteration.svg | L04-D01 | Hai thao tác nối chính sách và giá trị; nhãn đại lượng giữ cố định | Vẽ lại NG1 tr. 13, NG2 §4.3 |
| dp04-five-cell.svg | L04-E06,E08,F02–F03 | Năm ô, biên trái ở lại, c5 kết thúc; bốn mũi tên phải khi thể hiện chính sách | NG1 tr. 25,28; bổ sung biên thiếu đã ghi |
| dp04-update-order.svg | L04-F02 | Hai bảng hoặc một bảng với thứ tự đánh số; mũi tên giá trị mới được dùng tiếp | NG1 tr. 15; NG2 tr. 75,85 |
| dp04-gpi.svg | L04-F04 | Hai quá trình hướng tới $V=v_\pi$ và chính sách tham lam theo V | Sơ đồ khái niệm mới theo NG2 §4.6, không sao chép hình |
| dp04-cartpole-bins.svg | L04-F05 | Bốn biến liên tục, số khoảng 3/3/6/6, 324 ô; mô hình còn cần xác định | Vẽ kỹ thuật từ NG1 tr. 35–37 |
| dp04-stochastic-grid.svg | L04-G03 | Ba kết quả từ c4; xác suất, phần thưởng và terminal được ghi trên nhánh | NG3 tr. 1; quy ước bổ sung rõ |

Mọi SVG có `role="img"`, `title`/`desc` và mô tả thay thế cụ thể khi nhúng. Bảng số là HTML, công thức là KaTeX, không chụp raster. Không chỉ dùng màu để phân biệt hành động/lịch; dùng nhãn, mũi tên, nét và số thứ tự. Bài mới không sửa năm hình của ghi chú chuyên sâu đang dùng bộ số khác. Không tạo hình AI, không tải tài sản cốt lõi từ mạng.

## Quyết định theo từng trang

Nội dung, công thức và lời giải chi tiết ở outline.md. Các mục dưới đây ghi lý do tồn tại, sản phẩm và kết nối để kiểm định tuyến lập luận; nhãn và thời lượng chỉ là metadata kế hoạch.

### L04-A01 — Giải MDP bằng quy hoạch động

- **Chức năng và nhu cầu học tập:** Mở đầu. Quy hoạch động tính giá trị và chính sách từ mô hình môi trường đã biết.
- **Đầu vào và quan hệ với trang trước:** Tiên quyết Bài 03 và yêu cầu giải bài toán lập kế hoạch.
- **Sản phẩm và mục tiêu:** MT1–MT6; Quy hoạch động tính giá trị và chính sách từ mô hình môi trường đã biết.
- **Đầu ra cho trang sau:** Chủ đề lập kế hoạch được cụ thể hóa bằng chuỗi năng lực cần thực hiện.
- **Quyết định:** `sửa`. Cập nhật định danh học phần và học kỳ, giữ chủ đề nguồn.
- **Thời lượng:** 1 phút, trong tổng của mạch.

### L04-A02 — Nội dung và mục tiêu

- **Chức năng và nhu cầu học tập:** Bản đồ nội dung. Đánh giá chính sách cung cấp căn cứ cho cải thiện và các thuật toán điều khiển.
- **Đầu vào và quan hệ với trang trước:** Chủ đề lập kế hoạch được cụ thể hóa bằng chuỗi năng lực cần thực hiện.
- **Sản phẩm và mục tiêu:** MT1–MT6; Đánh giá chính sách cung cấp căn cứ cho cải thiện và các thuật toán điều khiển.
- **Đầu ra cho trang sau:** Chuỗi đánh giá và cải thiện cần bắt đầu từ dữ kiện mô hình và mục tiêu điều khiển.
- **Quyết định:** `sửa`. Thay mục lục nguồn bằng thứ tự chương 4 theo chỉ dẫn cụ thể của người dùng.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-A03 — Bài toán lập kế hoạch với mô hình đã biết

- **Chức năng và nhu cầu học tập:** Vấn đề trung tâm. Mô hình cho phép tính kỳ vọng của quyết định trước khi thực hiện tương tác.
- **Đầu vào và quan hệ với trang trước:** Chuỗi đánh giá và cải thiện cần bắt đầu từ dữ kiện mô hình và mục tiêu điều khiển.
- **Sản phẩm và mục tiêu:** MT1; Mô hình cho phép tính kỳ vọng của quyết định trước khi thực hiện tương tác.
- **Đầu ra cho trang sau:** Mô hình hữu hạn đã biết được biểu diễn bằng bốn chuyển tiếp của một ví dụ cụ thể.
- **Quyết định:** `gộp`. Ghép điều kiện áp dụng với bài toán cụ thể; nhắc tiên quyết trước khi tính.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-A04 — Mô hình hai trạng thái

- **Chức năng và nhu cầu học tập:** Ví dụ dẫn nhập. Bốn chuyển tiếp xác định đủ để so sánh lựa chọn hiện tại và phần thưởng tiếp nối.
- **Đầu vào và quan hệ với trang trước:** Mô hình hữu hạn đã biết được biểu diễn bằng bốn chuyển tiếp của một ví dụ cụ thể.
- **Sản phẩm và mục tiêu:** MT1; Bốn chuyển tiếp xác định đủ để so sánh lựa chọn hiện tại và phần thưởng tiếp nối.
- **Đầu ra cho trang sau:** Dữ kiện bốn chuyển tiếp đủ để kiểm tra một quỹ đạo theo chính sách cố định.
- **Quyết định:** `sửa`. Đưa ví dụ nguồn lên phần mở đầu để thiết lập dữ kiện dùng xuyên suốt.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-A05 — Kiểm tra dữ kiện và phần thưởng chiết khấu

- **Chức năng và nhu cầu học tập:** Kiểm tra mở đầu. Chính sách cố định và mô hình xác định hoàn toàn quỹ đạo trong ví dụ này.
- **Đầu vào và quan hệ với trang trước:** Dữ kiện bốn chuyển tiếp đủ để kiểm tra một quỹ đạo theo chính sách cố định.
- **Sản phẩm và mục tiêu:** MT1; Đúng thứ tự thưởng, hệ số chiết khấu và phân biệt thưởng với mô hình chuyển.
- **Đầu ra cho trang sau:** Tổng ba bước chưa bao gồm phần thưởng về sau; đánh giá cần một biểu diễn cho phần tiếp nối.
- **Quyết định:** `thêm`. Kiểm tra đúng tiên quyết và nhu cầu tính giá trị mà không đòi hỏi Bellman.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-B01 — Dự đoán giá trị của chính sách cố định

- **Chức năng và nhu cầu học tập:** Vấn đề và trực giác. Đánh giá chính sách cộng thưởng hiện tại với giá trị tiếp nối theo chính sách đó.
- **Đầu vào và quan hệ với trang trước:** Tổng ba bước chưa bao gồm phần thưởng về sau; đánh giá cần một biểu diễn cho phần tiếp nối.
- **Sản phẩm và mục tiêu:** MT2; Đánh giá chính sách cộng thưởng hiện tại với giá trị tiếp nối theo chính sách đó.
- **Đầu ra cho trang sau:** Giá trị tiếp nối được thay bằng bảng hiện có để thực hiện lượt tính đầu tiên.
- **Quyết định:** `tách`. Tách trực giác ra trước phương trình và thuật toán đánh giá.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-B02 — Hai lượt đánh giá từ bảng giá trị bằng không

- **Chức năng và nhu cầu học tập:** Ví dụ tính tay. Một lượt đồng bộ dùng cùng bảng cũ cho mọi trạng thái.
- **Đầu vào và quan hệ với trang trước:** Giá trị tiếp nối được thay bằng bảng hiện có để thực hiện lượt tính đầu tiên.
- **Sản phẩm và mục tiêu:** MT2; Một lượt đồng bộ dùng cùng bảng cũ cho mọi trạng thái.
- **Đầu ra cho trang sau:** Các phép tính một bước được khái quát thành giá trị chính xác và phương trình kỳ vọng.
- **Quyết định:** `thêm`. Bổ sung bước tính trước hình thức hóa; bảo toàn mô hình nguồn.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-B03 — Hàm giá trị và phương trình Bellman kỳ vọng

- **Chức năng và nhu cầu học tập:** Định nghĩa. Giá trị chính xác là kỳ vọng của tổng thưởng và thỏa quan hệ đệ quy một bước.
- **Đầu vào và quan hệ với trang trước:** Các phép tính một bước được khái quát thành giá trị chính xác và phương trình kỳ vọng.
- **Sản phẩm và mục tiêu:** MT2; Giá trị chính xác là kỳ vọng của tổng thưởng và thỏa quan hệ đệ quy một bước.
- **Đầu ra cho trang sau:** Nghiệm ở cả hai vế được thay bằng bảng hiện có để tạo toán tử cập nhật.
- **Quyết định:** `sửa`. Chuẩn hóa chỉ số dưới và đưa định nghĩa sau ví dụ tính.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-B04 — Toán tử đánh giá chính sách

- **Chức năng và nhu cầu học tập:** Hình thức và quy tắc cập nhật. Lặp đánh giá thay nghiệm chưa biết trong phương trình Bellman bằng bảng của lượt trước.
- **Đầu vào và quan hệ với trang trước:** Nghiệm ở cả hai vế được thay bằng bảng hiện có để tạo toán tử cập nhật.
- **Sản phẩm và mục tiêu:** MT2; Lặp đánh giá thay nghiệm chưa biết trong phương trình Bellman bằng bảng của lượt trước.
- **Đầu ra cho trang sau:** Quy tắc cập nhật cần quy định bảng đọc, bảng ghi và thời điểm dừng.
- **Quyết định:** `tách`. Định nghĩa riêng toán tử theo chính sách; toán tử tối ưu được hoãn tới lặp giá trị.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-B05 — Thuật toán đánh giá chính sách đồng bộ

- **Chức năng và nhu cầu học tập:** Quy trình đầy đủ. Hai bảng tách giá trị cũ và mới, còn phần dư kiểm tra độ chính xác của bảng được trả về.
- **Đầu vào và quan hệ với trang trước:** Quy tắc cập nhật cần quy định bảng đọc, bảng ghi và thời điểm dừng.
- **Sản phẩm và mục tiêu:** MT2; Hai bảng tách giá trị cũ và mới, còn phần dư kiểm tra độ chính xác của bảng được trả về.
- **Đầu ra cho trang sau:** Phần dư đo được cần được liên hệ với sai số so với nghiệm chính xác.
- **Quyết định:** `sửa`. Khôi phục đầu vào, đầu ra và dừng; thống nhất cách cập nhật với ví dụ.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-B06 — Hội tụ và sai số đánh giá

- **Chức năng và nhu cầu học tập:** Bảo đảm có điều kiện. Chiết khấu nhỏ hơn 1 làm sai số đánh giá co lại và biến phần dư thành chặn sai số.
- **Đầu vào và quan hệ với trang trước:** Phần dư đo được cần được liên hệ với sai số so với nghiệm chính xác.
- **Sản phẩm và mục tiêu:** MT2; Chiết khấu nhỏ hơn 1 làm sai số đánh giá co lại và biến phần dư thành chặn sai số.
- **Đầu ra cho trang sau:** Bảo đảm hội tụ được đối chiếu với nghiệm giải trực tiếp của ví dụ nhỏ.
- **Quyết định:** `thêm`. Bổ sung bảo đảm ngay cạnh thuật toán; không gom toàn bộ lý thuyết ở cuối bài.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-B07 — Nghiệm đánh giá của chính sách ban đầu

- **Chức năng và nhu cầu học tập:** Ứng dụng và đối chiếu. Giải hệ Bellman cho nghiệm chính xác để đối chiếu bảng lặp.
- **Đầu vào và quan hệ với trang trước:** Bảo đảm hội tụ được đối chiếu với nghiệm giải trực tiếp của ví dụ nhỏ.
- **Sản phẩm và mục tiêu:** MT2; Giải hệ Bellman cho nghiệm chính xác để đối chiếu bảng lặp.
- **Đầu ra cho trang sau:** Nghiệm và bảng ước lượng cho phép kiểm tra riêng thao tác cập nhật và chặn sai số.
- **Quyết định:** `giữ`. Giữ phép tính nguồn và dùng nó để kiểm chứng thuật toán vừa xây dựng.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-B08 — Kiểm tra một lượt đánh giá

- **Chức năng và nhu cầu học tập:** Kiểm tra đánh giá chính sách. Kết quả đánh giá phụ thuộc việc giữ nguyên bảng ở vế phải.
- **Đầu vào và quan hệ với trang trước:** Nghiệm và bảng ước lượng cho phép kiểm tra riêng thao tác cập nhật và chặn sai số.
- **Sản phẩm và mục tiêu:** MT2; Tính đúng hai ô từ cùng $V_2$, lấy chuẩn đúng và gắn chặn với đúng bảng $V_2$.
- **Đầu ra cho trang sau:** Giá trị của chính sách cố định đã có; phần điều khiển cần so sánh các hành động khác.
- **Quyết định:** `thêm`. Đo khả năng tính và phân biệt bảng ước lượng với giá trị chính xác.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-C01 — Lựa chọn hành động từ giá trị tiếp nối

- **Chức năng và nhu cầu học tập:** Vấn đề và trực giác. Giá trị của chính sách hiện tại cho phép đánh giá một thay đổi hành động ở bước đầu.
- **Đầu vào và quan hệ với trang trước:** Giá trị của chính sách cố định đã có; phần điều khiển cần so sánh các hành động khác.
- **Sản phẩm và mục tiêu:** MT3; Giá trị của chính sách hiện tại cho phép đánh giá một thay đổi hành động ở bước đầu.
- **Đầu ra cho trang sau:** So sánh một thay đổi tại bước đầu được tính trên hai nhánh của trạng thái thứ hai.
- **Quyết định:** `tách`. Đưa đối tượng so sánh trước ký hiệu giá trị hành động.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-C02 — So sánh hành động tại trạng thái thứ hai

- **Chức năng và nhu cầu học tập:** Ví dụ tính tay. Tại $s_1$, hành động $b$ có giá trị nhìn trước lớn hơn khi dùng cùng giá trị tiếp nối.
- **Đầu vào và quan hệ với trang trước:** So sánh một thay đổi tại bước đầu được tính trên hai nhánh của trạng thái thứ hai.
- **Sản phẩm và mục tiêu:** MT3; Tại $s_1$, hành động $b$ có giá trị nhìn trước lớn hơn khi dùng cùng giá trị tiếp nối.
- **Đầu ra cho trang sau:** Hai giá trị nhìn trước xác định đối tượng được gọi là giá trị hành động theo chính sách.
- **Quyết định:** `tách`. Tách bước tính trước định nghĩa để tránh đồng nhất nhìn trước với giá trị chính sách mới.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-C03 — Giá trị hành động theo chính sách

- **Chức năng và nhu cầu học tập:** Định nghĩa và ánh xạ. Giá trị hành động cố định hành động đầu và cố định chính sách từ bước kế tiếp.
- **Đầu vào và quan hệ với trang trước:** Hai giá trị nhìn trước xác định đối tượng được gọi là giá trị hành động theo chính sách.
- **Sản phẩm và mục tiêu:** MT3; Giá trị hành động cố định hành động đầu và cố định chính sách từ bước kế tiếp.
- **Đầu ra cho trang sau:** Giá trị hành động cung cấp tiêu chí lựa chọn chính sách mới tại mọi trạng thái.
- **Quyết định:** `sửa`. Chuẩn hóa giá trị hành động và dời phương trình phụ vào ghi chú.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-C04 — Cải thiện chính sách bằng lựa chọn tham lam

- **Chức năng và nhu cầu học tập:** Quy tắc và định lý. Chọn hành động cực đại theo giá trị của chính sách cũ tạo chính sách không kém tại mọi trạng thái.
- **Đầu vào và quan hệ với trang trước:** Giá trị hành động cung cấp tiêu chí lựa chọn chính sách mới tại mọi trạng thái.
- **Sản phẩm và mục tiêu:** MT3; Chọn hành động cực đại theo giá trị của chính sách cũ tạo chính sách không kém tại mọi trạng thái.
- **Đầu ra cho trang sau:** Bảo đảm không giảm giá trị cần lập luận vượt ra ngoài một phép thử số.
- **Quyết định:** `sửa`. Nêu đủ đầu vào và điều kiện của định lý; bổ sung quy tắc phá hòa từ sách.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-C05 — Lập luận của định lý cải thiện chính sách

- **Chức năng và nhu cầu học tập:** Phác thảo chứng minh. Tính đơn điệu truyền lợi ích của lựa chọn một bước đến toàn bộ giá trị chính sách mới.
- **Đầu vào và quan hệ với trang trước:** Bảo đảm không giảm giá trị cần lập luận vượt ra ngoài một phép thử số.
- **Sản phẩm và mục tiêu:** MT3; Tính đơn điệu truyền lợi ích của lựa chọn một bước đến toàn bộ giá trị chính sách mới.
- **Đầu ra cho trang sau:** Tính đơn điệu cho phép áp dụng quy tắc trên toàn bộ mô hình hai trạng thái.
- **Quyết định:** `giữ`. Giữ phác thảo nguồn, đặt ngay sau định lý và nối với tính co đã chuẩn bị.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-C06 — Chính sách sau lần cải thiện đầu

- **Chức năng và nhu cầu học tập:** Ứng dụng. Cải thiện đồng thời tại hai trạng thái tạo $(a,b)$ và cần đánh giá lại giá trị.
- **Đầu vào và quan hệ với trang trước:** Tính đơn điệu cho phép áp dụng quy tắc trên toàn bộ mô hình hai trạng thái.
- **Sản phẩm và mục tiêu:** MT3; Cải thiện đồng thời tại hai trạng thái tạo $(a,b)$ và cần đánh giá lại giá trị.
- **Đầu ra cho trang sau:** Giá trị sau lần đổi chính sách cung cấp dữ kiện cho một lần lựa chọn mới.
- **Quyết định:** `thêm`. Khôi phục bước nguồn đã rút gọn; đây là đầu vào trực tiếp cho lần cải thiện kế tiếp.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-C07 — Kiểm tra lựa chọn theo giá trị chính sách

- **Chức năng và nhu cầu học tập:** Kiểm tra cải thiện. Tham lam phải được tính theo giá trị của chính sách đang được cải thiện.
- **Đầu vào và quan hệ với trang trước:** Giá trị sau lần đổi chính sách cung cấp dữ kiện cho một lần lựa chọn mới.
- **Sản phẩm và mục tiêu:** MT3; Giữ cùng $v_{\pi_1}$ trong cả hai nhánh, tính đúng và giải thích bằng phần tiếp nối.
- **Đầu ra cho trang sau:** Lần cải thiện kế tiếp cho thấy nhu cầu lặp lại hai thao tác trên chính sách mới.
- **Quyết định:** `thêm`. Kiểm tra việc tái sử dụng bảng vừa đánh giá trước khi chuyển sang vòng lặp hoàn chỉnh.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-D01 — Lặp đánh giá và cải thiện chính sách

- **Chức năng và nhu cầu học tập:** Vấn đề và trực giác. Một lần cải thiện thay đổi giá trị, vì vậy quá trình phải lặp lại trên chính sách mới.
- **Đầu vào và quan hệ với trang trước:** Lần cải thiện kế tiếp cho thấy nhu cầu lặp lại hai thao tác trên chính sách mới.
- **Sản phẩm và mục tiêu:** MT4; Một lần cải thiện thay đổi giá trị, vì vậy quá trình phải lặp lại trên chính sách mới.
- **Đầu ra cho trang sau:** Chu trình tổng quát được lần theo bằng toàn bộ chuỗi chính sách và giá trị của ví dụ.
- **Quyết định:** `gộp`. Đặt chu trình tổng quát sau khi hai phép toán đã được học và kiểm tra.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-D02 — Quỹ đạo lặp chính sách trên hai trạng thái

- **Chức năng và nhu cầu học tập:** Ví dụ một lần lặp đầy đủ. Hai lần đổi chính sách đưa ví dụ từ $(a,a)$ đến $(b,b)$.
- **Đầu vào và quan hệ với trang trước:** Chu trình tổng quát được lần theo bằng toàn bộ chuỗi chính sách và giá trị của ví dụ.
- **Sản phẩm và mục tiêu:** MT4; Hai lần đổi chính sách đưa ví dụ từ $(a,a)$ đến $(b,b)$.
- **Đầu ra cho trang sau:** Chuỗi số được chuyển thành quy trình có đầu vào, đầu ra và điều kiện dừng rõ ràng.
- **Quyết định:** `sửa`. Mở rộng ví dụ bị rút gọn trong nguồn thành toàn bộ lần lặp có thể kiểm tra.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-D03 — Thuật toán lặp chính sách

- **Chức năng và nhu cầu học tập:** Quy trình đầy đủ. Lặp chính sách chính xác xen kẽ giải hệ Bellman và cải thiện với quy tắc phá hòa ổn định.
- **Đầu vào và quan hệ với trang trước:** Chuỗi số được chuyển thành quy trình có đầu vào, đầu ra và điều kiện dừng rõ ràng.
- **Sản phẩm và mục tiêu:** MT4; Lặp chính sách chính xác xen kẽ giải hệ Bellman và cải thiện với quy tắc phá hòa ổn định.
- **Đầu ra cho trang sau:** Kết quả không đổi chính sách được kiểm tra bằng điều kiện Bellman tối ưu.
- **Quyết định:** `sửa`. Bổ sung đầu ra nhất quán, ngân sách, phá hòa và phân biệt bảo đảm exact/approximate.
- **Thời lượng:** 4 phút, trong tổng của mạch.

### L04-D04 — Chính sách ổn định và nghiệm tối ưu

- **Chức năng và nhu cầu học tập:** Định lý và điều kiện điểm bất động. Chính sách tham lam theo chính giá trị của nó thỏa phương trình Bellman tối ưu.
- **Đầu vào và quan hệ với trang trước:** Kết quả không đổi chính sách được kiểm tra bằng điều kiện Bellman tối ưu.
- **Sản phẩm và mục tiêu:** MT4; Chính sách tham lam theo chính giá trị của nó thỏa phương trình Bellman tối ưu.
- **Đầu ra cho trang sau:** Điều kiện ổn định cần đi cùng lập luận dừng hữu hạn và độ chính xác đánh giá.
- **Quyết định:** `sửa`. Hoãn tối ưu Bellman tới khi người học đã thấy một chính sách ổn định.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-D05 — Dừng hữu hạn và đánh giá gần đúng

- **Chức năng và nhu cầu học tập:** Bảo đảm và giới hạn. Dừng hữu hạn của lặp chính sách cần đánh giá chính xác và tránh đổi hành động chỉ vì hòa.
- **Đầu vào và quan hệ với trang trước:** Điều kiện ổn định cần đi cùng lập luận dừng hữu hạn và độ chính xác đánh giá.
- **Sản phẩm và mục tiêu:** MT4; Dừng hữu hạn của lặp chính sách cần đánh giá chính xác và tránh đổi hành động chỉ vì hòa.
- **Đầu ra cho trang sau:** Một bảng gần đúng cung cấp trường hợp kiểm tra giới hạn của tiêu chuẩn ổn định.
- **Quyết định:** `sửa`. Khôi phục các giả thiết bị thiếu trong suy luận dừng của nguồn.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-D06 — Kiểm tra điều kiện dừng của lặp chính sách

- **Chức năng và nhu cầu học tập:** Kiểm tra lặp chính sách. Ổn định của chính sách chỉ có ý nghĩa cùng độ chính xác của bảng dùng để cải thiện.
- **Đầu vào và quan hệ với trang trước:** Một bảng gần đúng cung cấp trường hợp kiểm tra giới hạn của tiêu chuẩn ổn định.
- **Sản phẩm và mục tiêu:** MT4; Phân biệt đúng bảng $V$ với $v_\pi$ và dùng một so sánh giá trị đã biết để bác kết luận.
- **Đầu ra cho trang sau:** Chi phí đánh giá đầy đủ và giới hạn dừng gần đúng dẫn tới cập nhật điều khiển cắt ngắn.
- **Quyết định:** `thêm`. Kiểm tra một lỗi dừng có thể gặp khi dùng đánh giá gần đúng.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-E01 — Cắt ngắn đánh giá trong bài toán điều khiển

- **Chức năng và nhu cầu học tập:** Vấn đề và trực giác. Lặp giá trị chọn hành động tốt nhất trong mỗi cập nhật mà không hoàn tất đánh giá một chính sách.
- **Đầu vào và quan hệ với trang trước:** Chi phí đánh giá đầy đủ và giới hạn dừng gần đúng dẫn tới cập nhật điều khiển cắt ngắn.
- **Sản phẩm và mục tiêu:** MT5; Lặp giá trị chọn hành động tốt nhất trong mỗi cập nhật mà không hoàn tất đánh giá một chính sách.
- **Đầu ra cho trang sau:** Phép chọn nhánh lớn nhất được thử trên cùng bốn chuyển tiếp trước khi viết toán tử.
- **Quyết định:** `sửa`. Mở lặp giá trị bằng giới hạn chi phí của lặp chính sách trước công thức.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-E02 — Hai lượt lặp giá trị trên cùng mô hình

- **Chức năng và nhu cầu học tập:** Ví dụ tính tay. Phép cực đại thay việc giữ hành động của chính sách trong mỗi lượt đồng bộ.
- **Đầu vào và quan hệ với trang trước:** Phép chọn nhánh lớn nhất được thử trên cùng bốn chuyển tiếp trước khi viết toán tử.
- **Sản phẩm và mục tiêu:** MT5; Phép cực đại thay việc giữ hành động của chính sách trong mỗi lượt đồng bộ.
- **Đầu ra cho trang sau:** Phép cực đại từ bảng tùy ý cần ký hiệu riêng để phân biệt với giá trị hành động chính xác.
- **Quyết định:** `thêm`. Giữ ví dụ xuyên suốt để đối chiếu trực tiếp hai quy tắc cập nhật.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-E03 — Toán tử Bellman tối ưu

- **Chức năng và nhu cầu học tập:** Hình thức hóa. Toán tử tối ưu trả giá trị lớn nhất của các nhánh nhìn trước từ cùng một bảng.
- **Đầu vào và quan hệ với trang trước:** Phép cực đại từ bảng tùy ý cần ký hiệu riêng để phân biệt với giá trị hành động chính xác.
- **Sản phẩm và mục tiêu:** MT5; Toán tử tối ưu trả giá trị lớn nhất của các nhánh nhìn trước từ cùng một bảng.
- **Đầu ra cho trang sau:** Toán tử tối ưu được đặt trong vòng lặp và ghép với chính sách trích từ bảng trả về.
- **Quyết định:** `sửa`. Chuẩn hóa toán tử và phân biệt giá trị nhìn trước với giá trị hành động của chính sách.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-E04 — Thuật toán lặp giá trị đồng bộ

- **Chức năng và nhu cầu học tập:** Quy trình đầy đủ. Thuật toán trả bảng giá trị, chính sách tham lam theo chính bảng đó và phần dư kiểm chứng.
- **Đầu vào và quan hệ với trang trước:** Toán tử tối ưu được đặt trong vòng lặp và ghép với chính sách trích từ bảng trả về.
- **Sản phẩm và mục tiêu:** MT5; Thuật toán trả bảng giá trị, chính sách tham lam theo chính bảng đó và phần dư kiểm chứng.
- **Đầu ra cho trang sau:** Vòng lặp có tiêu chuẩn dừng cần bảo đảm rằng toán tử tiến tới đúng điểm bất động.
- **Quyết định:** `sửa`. Làm rõ đầu ra và chỉ số dừng, tránh lẫn mức thay đổi với phần dư của bảng mới.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-E05 — Tính co và hội tụ của lặp giá trị

- **Chức năng và nhu cầu học tập:** Định lý và phác thảo chứng minh. Cực đại theo hành động vẫn bảo toàn tính co khi hệ số chiết khấu nhỏ hơn 1.
- **Đầu vào và quan hệ với trang trước:** Vòng lặp có tiêu chuẩn dừng cần bảo đảm rằng toán tử tiến tới đúng điểm bất động.
- **Sản phẩm và mục tiêu:** MT5; Cực đại theo hành động vẫn bảo toàn tính co khi hệ số chiết khấu nhỏ hơn 1.
- **Đầu ra cho trang sau:** Bảo đảm của cập nhật tối ưu được áp dụng để đọc sự lan truyền giá trị trên lưới.
- **Quyết định:** `sửa`. Giữ kết quả nguồn và đặt sau thuật toán để trả lời nhu cầu bảo đảm.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-E06 — Lan truyền giá trị trên lưới năm ô

- **Chức năng và nhu cầu học tập:** Ứng dụng trực quan. Cập nhật đồng bộ lan truyền phần thưởng kết thúc lùi từng bước qua lưới.
- **Đầu vào và quan hệ với trang trước:** Bảo đảm của cập nhật tối ưu được áp dụng để đọc sự lan truyền giá trị trên lưới.
- **Sản phẩm và mục tiêu:** MT5; Cập nhật đồng bộ lan truyền phần thưởng kết thúc lùi từng bước qua lưới.
- **Đầu ra cho trang sau:** Lưới đã đạt điểm bất động ở $V_4$; mô hình hai trạng thái có bảng $V_1=(1,3)$ còn sai số dù chính sách trích đã tối ưu. Phần dư phân biệt hai tình huống.
- **Quyết định:** `gộp`. Ghép bốn trang nguồn thành một ứng dụng sau khi cơ chế đã rõ; dùng hình và bảng thay diễn giải lặp.
- **Vị trí trực quan sau kiểm ảnh:** Chú thích phép tính đặt ngay dưới bảng trong cột phải; hình và quy ước giữ ở cột trái. Chuyển nguyên nội dung để tránh chân trang và mũi tên điều hướng, không giảm cỡ chữ.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-E07 — Phần dư Bellman và ngưỡng sai số

- **Chức năng và nhu cầu học tập:** Ứng dụng bảo đảm. Ngưỡng phần dư xác định chặn sai số của chính bảng đang được trả về.
- **Đầu vào và quan hệ với trang trước:** Lưới đã đạt điểm bất động ở $V_4$; mô hình hai trạng thái có bảng $V_1=(1,3)$ còn sai số dù chính sách trích đã tối ưu. Phần dư phân biệt hai tình huống.
- **Sản phẩm và mục tiêu:** MT5; Ngưỡng phần dư xác định chặn sai số của chính bảng đang được trả về.
- **Đầu ra cho trang sau:** Quy tắc đồng bộ và quy ước kết thúc được kiểm tra bằng hai phép tính trên bảng đã cho.
- **Quyết định:** `thêm`. Biến tiêu chuẩn dừng nguồn thành chứng nhận có ý nghĩa định lượng.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-E08 — Kiểm tra cập nhật và trạng thái kết thúc

- **Chức năng và nhu cầu học tập:** Kiểm tra lặp giá trị. Mỗi lượt phải giữ giá trị kết thúc bằng không và dùng đúng bảng tiếp nối.
- **Đầu vào và quan hệ với trang trước:** Quy tắc đồng bộ và quy ước kết thúc được kiểm tra bằng hai phép tính trên bảng đã cho.
- **Sản phẩm và mục tiêu:** MT5; Tính đúng từ $V_2$, không dùng giá trị vừa cập nhật và đặt thưởng đúng trên chuyển tiếp.
- **Đầu ra cho trang sau:** Một lượt tính đúng vẫn có thể tốn kém; chi phí phụ thuộc số trạng thái và nhánh chuyển.
- **Quyết định:** `thêm`. Đo cơ chế cực đại, cập nhật đồng bộ và quy ước kết thúc.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-F01 — Chi phí của một lượt cập nhật

- **Chức năng và nhu cầu học tập:** Giới hạn và trực giác. Quét toàn bộ mô hình có thể chiếm phần lớn chi phí, nên cách phân bổ cập nhật cần được lựa chọn.
- **Đầu vào và quan hệ với trang trước:** Một lượt tính đúng vẫn có thể tốn kém; chi phí phụ thuộc số trạng thái và nhánh chuyển.
- **Sản phẩm và mục tiêu:** MT6; Quét toàn bộ mô hình có thể chiếm phần lớn chi phí, nên cách phân bổ cập nhật cần được lựa chọn.
- **Đầu ra cho trang sau:** Chi phí quét gợi nhu cầu dùng ngay giá trị mới và lựa chọn thứ tự cập nhật.
- **Quyết định:** `sửa`. Thay so sánh nhanh/chậm thiếu điều kiện bằng đơn vị công việc và giả thiết mô hình.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-F02 — Cập nhật tại chỗ và thứ tự trạng thái

- **Chức năng và nhu cầu học tập:** Ví dụ dẫn nhập và trực giác. Giá trị vừa tính có thể được dùng ngay, làm kết quả một lượt phụ thuộc thứ tự cập nhật.
- **Đầu vào và quan hệ với trang trước:** Chi phí quét gợi nhu cầu dùng ngay giá trị mới và lựa chọn thứ tự cập nhật.
- **Sản phẩm và mục tiêu:** MT6; Giá trị vừa tính có thể được dùng ngay, làm kết quả một lượt phụ thuộc thứ tự cập nhật.
- **Đầu ra cho trang sau:** Cơ chế dùng giá trị mới nhất được giữ; ví dụ lưới dùng $T_*$ dẫn tới lặp giá trị bất đồng bộ, khác ví dụ đánh giá hai trạng thái dùng $T_{\pi_0}$.
- **Quyết định:** `sửa`. Sửa cách nguồn gọi tại chỗ và bất đồng bộ như đồng nghĩa; nối bằng ví dụ kiểm tra được.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-F03 — Lặp giá trị bất đồng bộ

- **Chức năng và nhu cầu học tập:** Quy trình và điều kiện sử dụng. Bất đồng bộ cho phép chọn trạng thái cập nhật linh hoạt nhưng phải tiếp tục cập nhật mọi trạng thái.
- **Đầu vào và quan hệ với trang trước:** Cơ chế dùng giá trị mới nhất được giữ; ví dụ lưới dùng $T_*$ dẫn tới lặp giá trị bất đồng bộ, khác ví dụ đánh giá hai trạng thái dùng $T_{\pi_0}$.
- **Sản phẩm và mục tiêu:** MT6; Bất đồng bộ cho phép chọn trạng thái cập nhật linh hoạt nhưng phải tiếp tục cập nhật mọi trạng thái.
- **Đầu ra cho trang sau:** Các lịch khác nhau được đặt trong quan hệ chung giữa đánh giá và cải thiện.
- **Quyết định:** `thêm`. Bổ sung quy trình bất đồng bộ và điều kiện hội tụ từ chương 4.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-F04 — Lặp chính sách tổng quát

- **Chức năng và nhu cầu học tập:** Khái niệm hỗ trợ và ứng dụng phân loại. Các phương pháp quy hoạch động phối hợp đánh giá và cải thiện với mức hoàn tất khác nhau.
- **Đầu vào và quan hệ với trang trước:** Các lịch khác nhau được đặt trong quan hệ chung giữa đánh giá và cải thiện.
- **Sản phẩm và mục tiêu:** MT6; Các phương pháp quy hoạch động phối hợp đánh giá và cải thiện với mức hoàn tất khác nhau.
- **Đầu ra cho trang sau:** Các cách tổ chức cập nhật vẫn cần biểu diễn trạng thái hữu hạn và mô hình đã biết. CartPole có trạng thái liên tục, nên việc tạo biểu diễn hữu hạn còn phải xét ảnh hưởng của gộp trạng thái.
- **Quyết định:** `thêm`. Bổ sung khái niệm hỗ trợ của chương 4 để nối các thuật toán, không tạo một thuật toán mới.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-F05 — Rời rạc hóa và mô hình CartPole

- **Chức năng và nhu cầu học tập:** Ứng dụng giới hạn. Rời rạc hóa giảm biểu diễn liên tục về bảng hữu hạn nhưng chưa cung cấp mô hình Markov phù hợp.
- **Đầu vào và quan hệ với trang trước:** Các cách tổ chức cập nhật vẫn cần biểu diễn trạng thái hữu hạn và mô hình đã biết. CartPole có trạng thái liên tục, nên việc tạo biểu diễn hữu hạn còn phải xét ảnh hưởng của gộp trạng thái.
- **Sản phẩm và mục tiêu:** MT6; Rời rạc hóa giảm biểu diễn liên tục về bảng hữu hạn nhưng chưa cung cấp mô hình Markov phù hợp.
- **Đầu ra cho trang sau:** Các điều kiện về lịch và mô hình được kiểm tra bằng hai trường hợp thiếu dữ kiện.
- **Quyết định:** `gộp`. Giữ đầy đủ giới hạn nguồn trong một ứng dụng; sửa hàm ý rời rạc hóa tự tạo MDP chính xác.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-F06 — Kiểm tra lịch cập nhật và dữ kiện mô hình

- **Chức năng và nhu cầu học tập:** Kiểm tra quy hoạch động thực hành. Lịch cập nhật và mô hình hợp lệ là hai điều kiện độc lập của phép giải.
- **Đầu vào và quan hệ với trang trước:** Các điều kiện về lịch và mô hình được kiểm tra bằng hai trường hợp thiếu dữ kiện.
- **Sản phẩm và mục tiêu:** MT6; Nêu đúng điều kiện lịch, hậu quả số ở $s_1$ và phân biệt biểu diễn trạng thái với mô hình.
- **Đầu ra cho trang sau:** Những điều kiện sử dụng được thu hồi cùng nghiệm của bài toán hai trạng thái.
- **Quyết định:** `thêm`. Đánh giá khả năng xác định điều kiện thiếu trong ứng dụng thực hành.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-G01 — Kết quả của bài toán lập kế hoạch

- **Chức năng và nhu cầu học tập:** Tổng hợp theo vấn đề mở đầu. Mô hình hai trạng thái có chính sách tối ưu $(b,b)$ với giá trị $(27,30)$.
- **Đầu vào và quan hệ với trang trước:** Những điều kiện sử dụng được thu hồi cùng nghiệm của bài toán hai trạng thái.
- **Sản phẩm và mục tiêu:** MT1–MT5; Mô hình hai trạng thái có chính sách tối ưu $(b,b)$ với giá trị $(27,30)$.
- **Đầu ra cho trang sau:** Hai thuật toán cho cùng nghiệm nhưng yêu cầu so sánh cấu trúc công việc và độ chính xác.
- **Quyết định:** `sửa`. Kết luận quay lại bài toán đầu, đối chiếu đầu ra thay vì chỉ nhắc mục lục.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-G02 — Lựa chọn phương pháp và điều kiện áp dụng

- **Chức năng và nhu cầu học tập:** Tổng hợp so sánh. So sánh phương pháp phải dùng cùng đơn vị công việc và cùng yêu cầu độ chính xác.
- **Đầu vào và quan hệ với trang trước:** Hai thuật toán cho cùng nghiệm nhưng yêu cầu so sánh cấu trúc công việc và độ chính xác.
- **Sản phẩm và mục tiêu:** MT4–MT6; So sánh phương pháp phải dùng cùng đơn vị công việc và cùng yêu cầu độ chính xác.
- **Đầu ra cho trang sau:** So sánh kỳ vọng và mô hình được vận dụng khi chuyển tiếp của lưới trở thành ngẫu nhiên.
- **Quyết định:** `sửa`. Thay phát biểu so sánh thiếu điều kiện trong nguồn bằng tiêu chí có thể kiểm tra.
- **Thời lượng:** 2 phút, trong tổng của mạch.

### L04-G03 — Bài tập lưới có chuyển tiếp ngẫu nhiên

- **Chức năng và nhu cầu học tập:** Bài tập tổng hợp được chuẩn bị. Kỳ vọng trong cập nhật phải ghép xác suất với phần thưởng của chuyển thực tế.
- **Đầu vào và quan hệ với trang trước:** So sánh kỳ vọng và mô hình được vận dụng khi chuyển tiếp của lưới trở thành ngẫu nhiên.
- **Sản phẩm và mục tiêu:** MT2, MT5; Mỗi tổng đủ ba kết quả, thưởng gắn với chuyển thực tế và giữ đích bằng 0.
- **Đầu ra cho trang sau:** Bài tập dùng kỳ vọng dẫn tới kiểm tra tổng hợp cách chứng nhận nghiệm từ mô hình.
- **Quyết định:** `sửa`. Hoàn thiện bài tập nguồn đang thiếu quy ước và yêu cầu; không tạo chương trình mới.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-G04 — Kiểm tra nghiệm và chứng nhận tối ưu

- **Chức năng và nhu cầu học tập:** Kiểm tra tổng hợp. Một nghiệm điều khiển được kiểm tra bằng hành động tham lam và phần dư Bellman cùng giả thiết.
- **Đầu vào và quan hệ với trang trước:** Bài tập dùng kỳ vọng dẫn tới kiểm tra tổng hợp cách chứng nhận nghiệm từ mô hình.
- **Sản phẩm và mục tiêu:** MT3–MT6; Đúng bốn điểm, đúng phần dư của bảng đã cho, nêu giả thiết và phân biệt mẫu với mô hình đầy đủ.
- **Đầu ra cho trang sau:** Năng lực kiểm chứng được củng cố bằng các mục đọc và bài tập gắn với chương 4.
- **Quyết định:** `thêm`. Đo việc nối giá trị, chính sách, hội tụ và mô hình trong cùng một kết luận.
- **Thời lượng:** 3 phút, trong tổng của mạch.

### L04-G05 — Tài liệu đọc và bài tập tiếp nối

- **Chức năng và nhu cầu học tập:** Kết luận và đọc thêm. Chương 4 củng cố quan hệ giữa đánh giá, cải thiện và các cách tổ chức cập nhật.
- **Đầu vào và quan hệ với trang trước:** Năng lực kiểm chứng được củng cố bằng các mục đọc và bài tập gắn với chương 4.
- **Sản phẩm và mục tiêu:** MT1–MT6; Chương 4 củng cố quan hệ giữa đánh giá, cải thiện và các cách tổ chức cập nhật.
- **Đầu ra cho trang sau:** Bài học kết thúc bằng nhiệm vụ tính và đọc đã có tiên quyết; không mở thuật toán mới.
- **Quyết định:** `thêm`. Gắn đọc thêm với phần đã học và nguồn xác minh; giữ 30 phút chữa bài, không tự tạo code demo.
- **Thời lượng:** 2 phút, trong tổng của mạch.


## Rủi ro triển khai và điều kiện chấp nhận

- E06 chứa lưới, bảng bốn lượt và quy ước; dùng hình gọn phía trên, bảng lớn, dời phép tính nhánh và kiểm điểm bất động vào notes. Nếu cần tách vì tràn, phải cân lại 45 trang/120 phút và ghi quyết định, không thu nhỏ chữ dưới chuẩn.
- D03 và E04 cần giả mã đủ đầu vào/ra nhưng không nhồi diễn giải. Các giới hạn đánh giá gần đúng và phần dư có trang riêng, chỉ giữ quy tắc hoạt động trên trang giả mã.
- D04 phát biểu tối ưu trước chứng minh co tối ưu; nói đúng là kết quả đã có căn cứ NG2, không tuyên bố ví dụ là chứng minh. E05 hoàn thiện căn cứ tính duy nhất. C05 chỉ cần co theo chính sách đã có ở B06.
- F04 là khuôn tổng hợp, không phát biểu hội tụ cho mọi lịch xấp xỉ. F05 không coi lượng tử hóa tự tạo MDP chính xác. Nội dung công khai tránh các nhãn điều phối và thời lượng.
- Ở giai đoạn lập kế hoạch ngày 2026-09-28, HTML/SVG mới chưa được dựng. Sau triển khai và năm báo cáo độc lập, các quyết định sửa cục bộ đã được cập nhật trong hồ sơ này; kiểm định cuối phải xác nhận bản sau sửa và các ranh giới bị ảnh hưởng.


## Đồng bộ sau năm báo cáo độc lập — 2026-09-28

Giữ nguyên 45 mã, thứ tự, bảy mạch và 120 phút. Các quyết định sửa dưới đây dùng dữ kiện hiện có; không thêm trang hay code demo.

| Trang/cụm | Quyết định và lý do | Dữ kiện/kết nối cần rà lại |
|---|---|---|
| A02 | `sửa`: mục tiêu so sánh các cách tổ chức tính toán khớp nhiệm vụ đã có | MT6 giữ nguyên; không thêm tình huống đánh giá lên trang |
| A03, B04, B07 | `sửa`: khai báo miền chưa kết thúc và tổng gồm đích | Bảng mở rộng bằng 0; ma trận trên trạng thái chưa kết thúc; thưởng vào đích vẫn tính |
| B03–B06 | `sửa`: tính chính sách ngẫu nhiên trong notes B04 sau định nghĩa toán tử; đặt độ lệch 0,9 ở cuối notes trước định nghĩa phần dư B05 | Trung bình hai hành động cho (0,5;2,5); quay lại chính sách ban đầu để so hai bảng (1,2) và (1,9;2,9); B06 liên hệ độ lệch đo được với sai số |
| B04, G01 | `sửa`: gọi tên bootstrapping rồi thu hồi ở kết luận | Cơ chế dùng ước lượng tiếp nối khác với yêu cầu có mô hình để tính đầy đủ kỳ vọng |
| D01 | `sửa`: nhãn giá trị trong SVG dùng chỉ số dưới đúng | Quan hệ đánh giá–cải thiện và đại lượng cố định không đổi |
| E06–E08 | `sửa`: gọi tên mô hình khi đổi ví dụ, nêu trái/phải và phân biệt lưới đã đạt điểm bất động với bảng hai trạng thái còn sai số | E07 ghi mô hình hai trạng thái; E08 ghi lưới năm ô; ngưỡng phần dư là điều kiện đủ |
| F02–F03 | `sửa`: gọi rõ lặp giá trị tại chỗ và lặp giá trị bất đồng bộ | Cơ chế đọc giá trị mới được truyền; toán tử đánh giá cho 2,9 khác toán tử tối ưu cho 3 ở cùng bảng (1,0) |
| F04–F05 | `sửa`: đưa câu nối về biểu diễn hữu hạn và mô hình đã biết vào notes F04 | Giới hạn gộp CartPole dùng cùng giả thiết, F06 kiểm điều kiện mô hình |
| E06, G03 | `sửa`: bỏ bình luận công việc biên soạn khỏi sản phẩm | Quy ước biên trái, thưởng theo chuyển thực tế và lý do bổ sung vẫn lưu trong hồ sơ này và nhật ký |
| G03 | `sửa`: nêu trái/phải và lặp giá trị đồng bộ từ bảng không | Giữ xác suất 0,8/0,1/0,1 và lời giải 7,8; 4,436 |
| Ghi chú chuyên sâu | `sửa`: thống nhất bảng trả và ngân sách của đánh giá/lặp giá trị với deck | K đếm số lần nhận bảng mới; I_max đếm vòng lặp chính sách; giữ hệ quả riêng cho W và bộ số gamma=0,5 |

Cụm phần dư theo chu trình rút gọn trong đánh giá: nhu cầu dừng từ B04; ví dụ độ lệch 0,9 cuối notes B04; chuẩn/phần dư và quy trình B05; chặn có điều kiện B06; áp dụng đối chiếu nghiệm B07; kiểm B08. Trình tự của mạch B không đổi. Báo cáo quyết định chi tiết và trạng thái rà lại nằm trong review-log.md.
