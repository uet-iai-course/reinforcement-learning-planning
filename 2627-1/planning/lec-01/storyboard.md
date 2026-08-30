# Storyboard Bài 01: Giới thiệu Học tăng cường

## Bản đồ 7 mạch ngoài

HTML hiện hành có đúng 7 `<section>` ngoài, khớp giới hạn 5–7 mạch: mạch 1 gộp P+A+B (mở đầu), mạch 7 gộp H+Z (kết luận và bài tập). Tổng mạch 1–6 là 120 phút trình chiếu chính; mạch 7 là 30 phút bài tập. H00–H03 nằm trong stack dọc dưới Z00, không thuộc tuyến 150 phút.

| Mạch | Trang | Chức năng | Kết nối vào | Đầu ra | Đóng góp mục tiêu | Thời lượng |
|---|---|---|---|---|---|---:|
| 1. Mở đầu: P+A+B | P00–P02, A00–A04, B00–B02 | Đặt vấn đề, xác lập ngôn ngữ tác tử–môi trường, nêu giới hạn mô hình cố định, dẫn nhập hai trường hợp ứng dụng | Vào bài từ không có trang trước; P00 mở tuyến | Người học nêu được vì sao quyết định phải học từ tương tác và có hai ca ứng dụng để đối chiếu | LLO1 | 30 phút |
| 2. Tín hiệu học: C | C00–C05 | Xác định khung học và phân biệt ba dạng tín hiệu | Từ B02: hai ca đều học từ tương tác, cần biết tín hiệu nào hướng dẫn | Tiêu chí nhận dạng Học tăng cường qua tương tác, dữ liệu phụ thuộc thời gian, phản hồi trễ | LLO1, LLO2 | 22 phút |
| 3. Phần thưởng: D | D00–D03 | Hình thức hóa phần thưởng một bước và phần thưởng tích lũy | Từ C05: phản hồi trễ cần được định lượng | Công thức $G_t=\sum_{k=t+1}^{T}R_k$ và giả thuyết phần thưởng có điều kiện | LLO1 | 18 phút |
| 4. Thành phần: E | E00–E02 | Định nghĩa chính sách, hàm giá trị, mô hình tùy chọn | Từ D03: mục tiêu là cực đại hóa kỳ vọng của $G_t$, cần đại lượng điều khiển | $\pi(a\mid h_t)$, $V^\pi(h_t)$, phân biệt có mô hình và phi mô hình | LLO3 | 18 phút |
| 5. Thăm dò–khai thác: F | F00–F03 | Gắn đánh đổi thăm dò–khai thác vào chính sách vừa định nghĩa | Từ E02: chính sách và giá trị là công cụ để chọn hành động | Quyết định có dữ kiện thiếu được nêu tường minh | LLO1, LLO3 | 14 phút |
| 6. Tic-tac-toe: G | G00–G04 | Áp dụng toàn bộ khung vào một bài toán kiểm chứng được | Từ F03: cần một miền có luật rõ để đánh giá | Mô hình hóa trạng thái–hành động–thưởng và phép chọn khai thác một bước | LLO3, LLO4 | 18 phút |
| 7. Kết luận và bài tập: H+Z | H04–H07, Z00 | Chữa câu hỏi ôn tập, hai thảo luận mở rộng, giao tự kiểm tra | Từ G04: kiến thức đã khép, chuyển sang đánh giá và thảo luận | Câu trả lời ôn tập, hai thảo luận có giới hạn, nhiệm vụ tự kiểm tra | LLO1–LLO4 | 30 phút |

Phân bổ 30 phút mạch 7: H04 6 phút, H05 7 phút, H06 7 phút, H07 7 phút, Z00 3 phút. Không có code demo vì bản nguồn không có nội dung mã.

## Ánh xạ cụm trọng tâm

Mỗi cụm theo thứ tự bắt buộc: vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng → kiểm tra. Bước gộp hoặc không áp dụng được ghi kèm lý do.

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/thuật toán | Ứng dụng | Kiểm tra | Ghi chú bước |
|---|---|---|---|---|---|---|---|
| 1. Tác tử học (A00–A04) | A00: robot dọn nhà phải chọn hành động khi hậu quả đến sau tương tác | A00: vòng tương tác tác tử–môi trường | A00: robot dọn nhà | A01: tách tác tử, môi trường, trạng thái, quan sát | A02–A03: ghi nhớ–thích nghi–khái quát; điều khiển mô hình cố định | A04: giới hạn mô hình cố định, hai khả năng có/phi mô hình | B00–B02 không phải bước kiểm tra của cụm này mà là trường hợp ứng dụng dẫn nhập, đặt sau A04 để cho thấy hai miền thực tế đòi hỏi học từ tương tác trước khi vào khung hình thức |
| 1b. Trường hợp ứng dụng dẫn nhập (B00–B02) | B00: hai miền thực tế nào đòi hỏi học từ tương tác | B00: trò chơi và tương tác vật lý đều cho phản hồi trễ | B01: AlphaGo; B02: thao tác robot | Không áp dụng — khái niệm hình thức chưa được định nghĩa, đây là dẫn nhập có chủ ý | B01–B02 chính là bước ứng dụng | B02: câu hỏi quan sát nào đổi sau mỗi thao tác, tiêu chí nào chỉ đánh giá sau cả chuỗi | Vai trò là dẫn nhập, không phải ví dụ đến muộn; cầu nối ra C00: hai ca đều học từ tương tác, phần sau xác định tín hiệu học |
| 2. Tín hiệu học (C00–C05) | C00: tín hiệu nào hướng dẫn tác tử khi không có hành động đúng từng bước | C01–C02: hành động hiện tại làm đổi dữ liệu sau; sơ đồ đối chiếu ba dạng tín hiệu | C05: tình huống robot chọn đường đi | C03–C04: học có giám sát và không giám sát | C05: nhận dạng Học tăng cường qua tương tác và phản hồi trễ | C05: vì sao không tráo thứ tự mẫu | C05 gộp ví dụ, ứng dụng và kiểm tra vì cùng dùng một tình huống để nhận dạng quan hệ phụ thuộc thời gian; C02 là sơ đồ đối chiếu, không phải ví dụ |
| 3. Phần thưởng (D00–D03) | D00: hậu quả của $A_t$ được đo bằng gì | D00: quỹ đạo $S_0,\ldots,S_4$ với cặp $A_t,R_{t+1}$ | D02: tính $G_0=0+0+0+1=1$ với $T=4$ | D01: định nghĩa $R_{t+1}\in\mathbb R$ sau $A_t$; D02: $G_t=\sum_{k=t+1}^{T}R_k$ | D03: cờ và robot dọn nhà | D03: nêu mục tiêu chưa được phản ánh bởi cách đặt phần thưởng | Bước kiểm tra gộp vào ứng dụng D03 vì mức phù hợp của phần thưởng là đối tượng cần đánh giá |
| 4. Thành phần (E00–E02) | E00: trong một thế cờ, tách hai việc chọn nước và đánh giá thế cờ | E00: hai nhiệm vụ khác nhau trên cùng một thế cờ | E00: một thế cờ Tic-tac-toe (luật đầy đủ ở G00, dẫn rõ trên trang) | E01: $\pi(a\mid h_t)$, $V^\pi(h_t)=\mathbb E_\pi[G_t\mid H_t=h_t]$; E02: mô hình dự báo $(\widehat S_{t+1},\widehat R_{t+1})$ | E02: phân biệt có mô hình và phi mô hình | E02: câu hỏi mô hình có bắt buộc không | Ứng dụng tổng hợp của cụm nằm ở G03 (cầu nối E01→G03, xem bảng trang); G03–G04 thuộc cụm 6, cụm 4 không đếm trùng thời lượng |
| 5. Thăm dò–khai thác (F00–F03) | F00: chọn nước đã đánh giá cao hay nước còn ít dữ liệu | F00: hai mục tiêu xung đột trong ngắn hạn | F03: bảng hai hành động A (20 lần, 0,60) và B (2 lần, 0,55) | F01–F02: định nghĩa thăm dò và khai thác; khai thác tương ứng chọn theo giá trị ước lượng, thăm dò tương ứng $\pi$ đặt xác suất khác không cho hành động ít dữ liệu | F03: quyết định khi chưa biết đủ | F03: nêu dữ kiện còn thiếu trước khi quyết định | Bước ví dụ gộp vào kiểm tra F03 vì bảng số vừa là ví dụ vừa là nhiệm vụ; ví dụ ngoài miền Tic-tac-toe được ghi lý do: cô lập đánh đổi khỏi luật trò chơi |
| 6. Tic-tac-toe (G00–G04) | G00: chọn nước hợp lệ để đạt kết quả cuối tốt, đối thủ chọn đều | G01: cây tìm kiếm đánh giá chuỗi nước đi | G02: cùng một thế cờ sinh các nước hợp lệ | G02: $S_t$, $\mathcal A(S_t)$, $A_t\in\mathcal A(S_t)$, thưởng $+1/0/-1$ theo góc nhìn tác tử | G03: so sánh thưởng tức thời cộng giá trị tiếp diễn dưới cùng $\pi$ | G04: kiểm tra mô hình hóa với ô 5 không hợp lệ | G03 là ứng dụng tổng hợp dùng định nghĩa E01; G04 là kiểm tra của cụm 6, không trùng chức năng với H05 (G04 tập trung mô hình hóa trạng thái–hành động–thưởng, H05 hỏi vai trò thành phần ở mức khái niệm) |

## Bảng theo từng trang

Mỗi trang có một hàng: lý do tồn tại kiểm chứng được, nguồn, quyết định, kết nối từ trang trước và ra trang sau.

| ID | Lý do tồn tại (kiểm chứng được) | Nguồn | Quyết định | Kết nối từ trang trước | Kết nối ra trang sau |
|---|---|---|---|---|---|
| P00 | Xác lập tên bài, học kỳ và bối cảnh; người học cần biết đang ở đâu | Nguồn 1 | sửa tên học phần và niên khóa | Mở đầu tuyến | P01: mục tiêu học tập |
| P01 | Nêu bốn sản phẩm học tập quan sát được, làm tiêu chí hoàn thành | Nguồn 2, 17–30 | thêm | P00 | P02: bản đồ nội dung |
| P02 | Cho thấy tuyến nhu cầu–khung học–kiểm tra, rồi báo điểm bắt đầu ở nhu cầu học của tác tử | Nguồn 2 | sửa sau tái kiểm định | P01 | A00: mở mạch tác tử học (ranh giới mạch 1 nội bộ P→A) |
| A00 | Đặt vấn đề bằng robot dọn nhà và vòng tương tác trước khi tách thành phần | Nguồn 3–4, 7 | sửa | P02 (hai trang lân cận tại ranh giới P02/A00 cần rà lại sau đổi section) | A01: tách tác tử và môi trường |
| A01 | Phân biệt trạng thái với quan sát, tránh đồng nhất tình huống thực với dữ liệu nhận được | Nguồn 4–5 | gộp, sửa sau phản biện | A00 | A02: nhu cầu học |
| A02 | Ba năng lực ghi nhớ–thích nghi–khái quát giải thích vì sao tác tử phải học | Nguồn 6 | giữ | A01 | A03: cách tiếp cận điều khiển |
| A03 | Mô tả giả định mô hình được cung cấp và giữ cố định, làm đối tượng so sánh | Nguồn 6 | sửa sau phản biện | A02 | A04: giới hạn của mô hình cố định |
| A04 | Khép nhu cầu: môi trường đổi và không gian lớn; nêu hai khả năng có/phi mô hình | Nguồn 7–9 | gộp, sửa sau phản biện | A03 | B00 (hai trang lân cận tại ranh giới A04/B00 cần rà lại sau đổi section); câu nối: hai miền dưới đây cho thấy quyết định phải học từ tương tác |
| B00 | Báo trước hai trường hợp ứng dụng dẫn nhập dùng để đối chiếu học từ tương tác và phản hồi trễ | Nguồn 10–13 | sửa | A04 | B01: AlphaGo |
| B01 | Ca ứng dụng trò chơi: học cách đánh giá nước đi kết hợp tìm kiếm cây, có nguồn truy nguyên | Nguồn 11; Silver et al. 2016 | sửa sau phản biện | B00 | B02: thao tác robot |
| B02 | Ca ứng dụng tương tác vật lý, đặt câu hỏi và báo bước tiếp theo là xác định tín hiệu học chung | Nguồn 12–13 | sửa sau tái kiểm định | B01 | C00 (mạch 2): hai ca đều học từ tương tác, phần sau xác định tín hiệu học |
| C00 | Đặt nhu cầu xác định tín hiệu học khi không có hành động đúng từng bước | Nguồn 16, 18 | sửa | B02 | C01: khung học từ tương tác |
| C01 | Phát biểu khung học và quan hệ phụ thuộc thời gian của dữ liệu tương tác | Nguồn 9, 17 | sửa sau phản biện | C00 | C02: ba dạng tín hiệu |
| C02 | Đặt ba dạng tín hiệu cạnh nhau làm tiêu chí phân biệt | Nguồn 19 | sửa | C01 | C03: học có giám sát |
| C03 | Làm rõ nhãn mục tiêu trực tiếp, tránh gọi mọi phản hồi là phần thưởng | Nguồn 19–20 | tách | C02 | C04: học không giám sát |
| C04 | Hoàn chỉnh đối chiếu ba dạng học bằng dữ liệu không nhãn | Nguồn 19 | tách | C03 | C05: nhận dạng tín hiệu học |
| C05 | Tình huống robot chọn đường đi vừa là ví dụ vừa là kiểm tra quan hệ phụ thuộc thời gian và dấu hiệu nhận dạng Học tăng cường | Nguồn 21 | sửa sau phản biện | C04 | D00 (mạch 3): phản hồi trễ cần được định lượng |
| D00 | Quỹ đạo $S_0$ đến $S_4$ với cặp $A_t,R_{t+1}$ làm trực giác chỉ số trước công thức | Nguồn 23–25 | sửa sau phản biện | C05 | D01: định nghĩa phần thưởng |
| D01 | Định nghĩa $R_{t+1}$ sau $A_t$, miền chỉ số và trạng thái kết thúc $S_T$ | Nguồn 23 | sửa sau phản biện | D00 | D02: phần thưởng tích lũy |
| D02 | Ví dụ số $G_0=0+0+0+1=1$ với $T=4$ khớp hình trước khi khái quát | Nguồn 25 | sửa sau phản biện | D01 | D03: giả thuyết phần thưởng |
| D03 | Giả thuyết phần thưởng có điều kiện mô hình hóa, kèm giới hạn qua cờ và robot dọn nhà | Nguồn 6–8, 24–25 | sửa sau phản biện | D02 | E00 (mạch 4): mục tiêu là cực đại hóa kỳ vọng của $G_t$, cần đại lượng điều khiển |
| E00 | Một thế cờ đặt hai việc: chọn nước và đánh giá thế cờ, trước khi gọi tên thành phần | Nguồn 26, 29–30 | sửa | D03 | E01: chính sách và hàm giá trị |
| E01 | Định nghĩa $\pi(a\mid h_t)$ và $V^\pi(h_t)=\mathbb E_\pi[G_t\mid H_t=h_t]$ với nguồn ngẫu nhiên tường minh | Nguồn 26; David Silver, Lecture 1 | sửa sau phản biện | E00 | E02: mô hình môi trường; cầu nối E01→G03: trong Tic-tac-toe quan sát đầy đủ, lịch sử $h_t$ rút gọn thành cặp (thế cờ $S_t$, lượt chơi), nên $V^\pi$ dùng ở G03 là cùng một định nghĩa; kỳ vọng lấy theo cả $\pi$ và phân phối đều của đối thủ |
| E02 | Phân biệt có mô hình và phi mô hình bằng dự báo $(\widehat S_{t+1},\widehat R_{t+1})$; mô hình là tùy chọn | Nguồn 26 | sửa sau phản biện | E01 | F00 (mạch 5): chính sách và giá trị là công cụ chọn hành động |
| F00 | Tình huống chọn giữa nước đã đánh giá cao và nước ít dữ liệu đặt vấn đề đánh đổi | Nguồn 27 | sửa | E02 | F01: thăm dò |
| F01 | Mục tiêu và chi phí của thăm dò; không đồng nhất với ngẫu nhiên vô điều kiện | Nguồn 27 | tách | F00 | F02: khai thác |
| F02 | Mục tiêu và rủi ro của khai thác; nối với chọn theo giá trị ước lượng như G03 | Nguồn 27 | tách | F01 | F03: quyết định khi chưa biết đủ |
| F03 | Bảng giả định hai hành động kiểm tra đánh đổi; yêu cầu nêu dữ kiện còn thiếu | Nguồn 27 | thêm, sửa sau phản biện | F02 | G00 (mạch 6): cần một miền có luật rõ để đánh giá |
| G00 | Giới thiệu miền Tic-tac-toe với giả thiết đối thủ chọn đều trên nước hợp lệ | Nguồn 28 | sửa sau phản biện | F03 | G01: tìm kiếm trên cây |
| G01 | Một thế cờ cụ thể minh họa ba nhánh tìm kiếm hợp lệ, nền kiểm chứng được trước cách học | Nguồn 28 | sửa sau phản biện | G00 | G02: biểu diễn bài toán |
| G02 | Chốt hành động, phần thưởng và cầu nối $h_t\leftrightarrow(S_t,\text{lượt})$ cho trò chơi quan sát đầy đủ | Nguồn 29–30 | sửa sau tái kiểm định | G01 | G03: đánh giá thế cờ |
| G03 | Áp dụng kỳ vọng điều kiện; nêu trên mặt trang cầu nối lịch sử–trạng thái và nguồn ngẫu nhiên | Nguồn 26, 29–30 | sửa sau tái kiểm định | G02 | G04: kiểm tra mô hình hóa |
| G04 | Kiểm tra mô hình hóa khi đến lượt X và ô 5 không hợp lệ; không lặp chức năng H05 | Nguồn 26, 29–30 | sửa sau tái kiểm định | G03 | H04 (mạch 7): kiến thức đã khép, chuyển sang ôn tập |
| H04 | Gom câu hỏi về mô hình cố định, dữ liệu phụ thuộc thời gian và phản hồi trễ | Nguồn 38–40 | chuyển, sửa sau phản biện | G04 | H05: ôn tập thành phần |
| H05 | Gom câu hỏi về vai trò thành phần, đánh đổi và nhiệm vụ chuyển giao robot dọn nhà; hỏi vai trò ở mức khái niệm, khác G04 | Nguồn 41–42 | gộp | H04 | H06: chuyển từ kiểm tra khái niệm sang thảo luận mở |
| H06 | Báo chuyển từ ôn tập sang thảo luận, rồi xét tác tử tổng quát với giới hạn | Nguồn 14–15, 43 | sửa sau tái kiểm định | H05 | H07: mô hình thế giới |
| H07 | Thảo luận lợi ích và rủi ro của mô hình thế giới; phân biệt dự báo với quyết định | Nguồn 44 | sửa | H06 | Z00 (hai trang lân cận tại ranh giới H07/Z00 cần rà lại sau đổi section) |
| Z00 | Thu hồi ba dấu hiệu nhận dạng, giao tự kiểm tra, tài liệu đọc và lối vào phụ lục | Nguồn 34, 45 | sửa sau tái kiểm định | H07 | Kết thúc tuyến ngang; nhấn ↓ mở H00 |
| H00 | Đưa thông tin tổ chức chưa xác nhận vào nhánh dọc dưới Z00 để truy nguyên | Nguồn 31–32 | chuyển phụ lục dọc | Z00 ↓ | H01 |
| H01 | Lưu mô tả chuẩn đầu ra của học phần trong nguồn, không dùng mã CLO | Nguồn 32 | sửa | H00 | H02 |
| H02 | Lưu kế hoạch và tài liệu trong nguồn để đối chiếu, không coi là lịch hiện hành | Nguồn 33–34 | gộp | H01 | H03 |
| H03 | Lưu đánh giá và tiên quyết trong nguồn với trạng thái chưa áp dụng | Nguồn 35, 37 | gộp | H02 | Hết phụ lục |

## Phạm vi rà lại sau đổi section

Việc gộp về 7 mạch ngoài làm đổi ranh giới tại ba điểm. Sau mỗi lần chỉnh sửa ảnh hưởng cấu trúc section, rà lại toàn bộ mạch và hai trang lân cận tại:

- P02/A00: ranh giới mạch mở đầu nội bộ (P → A), câu nối bản đồ sang tác tử học.
- A04/B00: ranh giới từ giới hạn mô hình cố định sang trường hợp ứng dụng dẫn nhập, câu nối "hai miền đòi hỏi học từ tương tác".
- H07/Z00: ranh giới mạch kết, câu nối thảo luận sang tài liệu đọc và tự kiểm tra, khâu thu hồi trọng tâm P02.

## Quy ước

- Mọi công thức Markdown dùng $...$; không dùng ký hiệu khác.
- Thuật ngữ theo bảng thuật ngữ trong outline: tác tử, môi trường, $R_{t+1}$, $G_t$, $h_t$, $\pi(a\mid h_t)$, $V^\pi(h_t)$, $\mathcal A(S_t)$, mô hình môi trường.
- Không tạo `quill.json`; mạch trạng thái/quan sát → dữ liệu thời gian → phần thưởng → chính sách/giá trị → Tic-tac-toe giữ liên tục theo Quill ở chế độ rà mạch.
- Không có code demo vì bản nguồn không có nội dung mã.
