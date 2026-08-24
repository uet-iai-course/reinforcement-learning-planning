# Storyboard Bài 01: Giới thiệu Học tăng cường

## Bản đồ hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức hoặc thuật toán | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Dữ kiện truyền | Câu nối | Thời lượng |
|---|---|---|---|---|---|---|---|---|---|---:|
| 1. Tác tử học | A00 | A00–A01 | A00, B01–B02 | A01 | A02–A04 | B02 | Học máy cơ bản → phân biệt trạng thái với quan sát, giải thích vòng tương tác và giới hạn mô hình cố định | robot, trạng thái, quan sát, hành động, mô hình | Robot đặt vấn đề; đối chiếu mô hình cố định với mô hình có thể học; thao tác robot kiểm tra chuỗi phản hồi. | 34 phút |
| 2. Tín hiệu học | C00 | C01 | C02 | C03–C04 | C05 | C05 | Ba dạng học máy → phân biệt nguồn tín hiệu và dữ liệu phụ thuộc thời gian | hành động, quan sát kế tiếp, nhãn, phần thưởng trễ | Tương tác làm dữ liệu sau phụ thuộc hành động trước; tình huống robot kiểm tra đúng quan hệ này. | 22 phút |
| 3. Phần thưởng | D00 | D00 | D02 | D01–D02 | D03 | D03 | Phản hồi trễ → tính tổng thưởng hữu hạn và nêu giới hạn mô hình hóa mục tiêu | $S_t$, $A_t$, $R_{t+1}$, $T$, $G_t$ | Quỹ đạo xác lập chỉ số; ví dụ $T=4$ dẫn tới giả thuyết có điều kiện. | 18 phút |
| 4. Chính sách, giá trị và mô hình | E00 | E01 | E00 | E01–E02 | E02, G03 | E02, G04 | Tic-tac-toe và tổng thưởng → phân biệt chọn ngẫu nhiên, đánh giá dưới một chính sách và dự báo môi trường | $h_t$, $\pi(a\mid h_t)$, $V^\pi$, quan sát hoặc trạng thái kế tiếp, phần thưởng | Hai việc trong một thế cờ được định nghĩa, rồi dùng cùng chính sách $\pi$ để so sánh các trạng thái kế tiếp. | 14 phút |
| 5. Thăm dò và khai thác | F00 | F00 | F00 | F01–F02 | F03 | F03 | Ước lượng từ kinh nghiệm → giải thích quyết định khi số lần thử khác nhau | nước đã đánh giá cao, nước ít dữ liệu, số lần thử, phần thưởng trung bình | Tình huống chọn nước đặt vấn đề; hai khái niệm dẫn tới bảng quyết định và kiểm tra. | 14 phút |
| 6. Tic-tac-toe | G00 | G01 | G02 | G02 | G03 | G04 | Luật trò chơi → mô hình hóa tác tử và nối chính sách với hàm giá trị | $S_t$, $\mathcal A(S_t)$, $A_t$, thưởng theo góc nhìn tác tử, $V^\pi$ | Cùng một thế cờ sinh ba nước hợp lệ; các trạng thái kế tiếp được đánh giá dưới cùng $\pi$. | 18 phút |

Sáu cụm P–G dùng 120 phút: P nằm trong thời lượng định hướng của cụm 1. H04–H07 và Z00 dùng 30 phút cuối để chữa câu hỏi, thảo luận và giao tự kiểm tra. Không có code demo vì bản nguồn không có nội dung mã. H00–H03 nằm trong stack dọc dưới Z00, chỉ dùng để truy nguyên và không thuộc tuyến 150 phút.

## Bảng theo từng trang

| ID | Vai trò và lý do tồn tại | Nhu cầu giải quyết | Quan hệ trước → sau | Mục tiêu | Quyết định | Nguồn |
|---|---|---|---|---|---|---|
| P00 | Xác lập tên bài và bối cảnh học kỳ. | Người học cần biết phạm vi bài. | Mở đầu → mục tiêu. | — | sửa | Nguồn 1 |
| P01 | Nêu bốn sản phẩm học tập quan sát được. | Người học cần tiêu chí hoàn thành. | Tiêu đề → bản đồ. | LLO1–LLO4 | thêm | Nguồn 2, 17–30 |
| P02 | Cho thấy tuyến nhu cầu, khung học và kiểm tra. | Giảm tải định hướng. | Mục tiêu → tác tử. | LLO1–LLO4 | sửa | Nguồn 2 |
| A00 | Dùng robot dọn nhà để đặt vấn đề, vòng tương tác và trực giác phản hồi. | Cần một tình huống cụ thể trước khi tách các thành phần. | Bản đồ → tác tử và môi trường. | LLO1 | sửa | Nguồn 3–4, 7 |
| A01 | Phân biệt tác tử, môi trường, trạng thái và quan sát ở mức nhập môn. | Tránh đồng nhất tình huống thực với dữ liệu tác tử nhận. | Vòng tương tác → năng lực học. | LLO1 | gộp, sửa sau phản biện | Nguồn 4–5 |
| A02 | Áp dụng khung vào ba năng lực ghi nhớ, thích nghi và khái quát. | Giải thích vì sao tác tử phải học. | Thành phần → cách điều khiển cũ. | LLO1 | giữ | Nguồn 6 |
| A03 | Mô tả giả định mô hình được cung cấp và giữ cố định. | Cần đối tượng so sánh nhưng không loại trừ Học tăng cường có mô hình. | Nhu cầu → giới hạn. | LLO1 | sửa sau phản biện | Nguồn 6 |
| A04 | Nối giới hạn mô hình cố định với hai khả năng học có mô hình hoặc phi mô hình. | Khép nhu cầu mà không tạo đối lập sai. | Điều khiển → ca ứng dụng. | LLO1 | gộp, sửa sau phản biện | Nguồn 7–9 |
| B00 | Báo trước hai trường hợp dùng để đối chiếu học từ tương tác và phản hồi trễ. | Nguồn có bốn trang hình rời nhưng chưa nêu việc người học cần kiểm tra. | Nhu cầu → AlphaGo. | LLO1 | sửa | Nguồn 10–13 |
| B01 | Minh họa học kết hợp tìm kiếm ở AlphaGo, chưa dùng thuật ngữ thành phần chưa định nghĩa. | Cần ca có nguồn truy nguyên. | Dẫn ca → thao tác robot. | LLO1 | sửa sau phản biện | Nguồn 11; Silver et al. 2016 |
| B02 | Vẽ lại hai thao tác robot trong nguồn và kiểm tra quan sát cùng tiêu chí cuối chuỗi. | Giữ đúng miền ví dụ của trang 12–13. | AlphaGo → khung Học tăng cường. | LLO1 | sửa sau phản biện | Nguồn 12–13 |
| C00 | Đặt nhu cầu xác định tín hiệu học khi không có hành động đúng từng bước. | Cần vấn đề trước định nghĩa và đối chiếu. | Ca ứng dụng → khung học. | LLO1–LLO2 | sửa | Nguồn 16, 18 |
| C01 | Phát biểu khung học và quan hệ phụ thuộc thời gian của dữ liệu tương tác. | Chốt đối tượng nghiên cứu và tránh giả định mẫu độc lập. | Bối cảnh → đối chiếu tín hiệu. | LLO1 | sửa sau phản biện | Nguồn 9, 17 |
| C02 | Đặt ba dạng tín hiệu cạnh nhau. | Người học cần tiêu chí phân biệt. | Định nghĩa → hai dạng nền. | LLO2 | sửa | Nguồn 19 |
| C03 | Làm rõ nhãn mục tiêu trực tiếp. | Tránh gọi mọi phản hồi là phần thưởng. | So sánh → không giám sát. | LLO2 | tách | Nguồn 19–20 |
| C04 | Làm rõ dữ liệu không nhãn. | Hoàn chỉnh đối chiếu ba dạng học. | Có giám sát → khác biệt RL. | LLO2 | tách | Nguồn 19 |
| C05 | Kiểm tra vì sao không thể tráo thứ tự dữ liệu và cách nhận dạng Học tăng cường. | Đánh giá trực tiếp quan hệ phụ thuộc thời gian. | Không giám sát → phần thưởng. | LLO1–LLO2 | sửa sau phản biện | Nguồn 21 |
| D00 | Đặt quỹ đạo $S_0$ đến $S_4$ và cặp $A_t,R_{t+1}$ làm trực giác. | Xác lập chỉ số trước công thức. | Khác biệt → định nghĩa thưởng. | LLO1 | sửa sau phản biện | Nguồn 23–25 |
| D01 | Định nghĩa $R_{t+1}$ sau $A_t$, miền chỉ số và trạng thái kết thúc $S_T$. | Tránh lệch chỉ số phần thưởng. | Quỹ đạo → ví dụ tổng hữu hạn. | LLO1 | sửa sau phản biện | Nguồn 23 |
| D02 | Tính $G_0$ với $T=4$ từ $R_1,\ldots,R_4$. | Cần ví dụ số khớp hình trước khi khái quát mục tiêu. | Thưởng bước → giả thuyết. | LLO1 | sửa sau phản biện | Nguồn 25 |
| D03 | Phát biểu giả thuyết có điều kiện và nêu giới hạn thiết kế phần thưởng bằng robot giao vật. | Tránh khẳng định tuyệt đối và ví dụ ngoài mạch nguồn. | Tổng thưởng → thành phần. | LLO1 | sửa sau phản biện | Nguồn 24–25 |
| E00 | Dùng một thế cờ để đặt hai việc: chọn nước và đánh giá thế cờ. | Cần vấn đề cụ thể trước tên thành phần. | Phần thưởng → chính sách và giá trị. | LLO3 | sửa | Nguồn 26, 29–30 |
| E01 | Định nghĩa chính sách ngẫu nhiên và giá trị phụ thuộc chính sách trên lịch sử. | Xác định điều kiện hóa và nguồn ngẫu nhiên của kỳ vọng. | Vấn đề → mô hình tùy chọn. | LLO3 | sửa sau phản biện | Nguồn 26; David Silver, Lecture 1 |
| E02 | Phân biệt có mô hình và phi mô hình bằng dự báo quan sát hoặc trạng thái kế tiếp cùng phần thưởng. | Ngăn hiểu sai mô hình là bắt buộc hoặc chỉ dự báo trạng thái. | Vai trò → đánh đổi thông tin. | LLO3 | sửa sau phản biện | Nguồn 26 |
| F00 | Dùng lựa chọn giữa nước đã đánh giá cao và nước còn ít dữ liệu để đặt vấn đề, trực giác và ví dụ. | Tác tử chưa biết đủ về các hành động. | Thành phần → thăm dò. | LLO1, LLO3 | sửa | Nguồn 27 |
| F01 | Phát biểu mục tiêu và chi phí của thăm dò. | Tránh đồng nhất thăm dò với ngẫu nhiên. | Cân bằng → khai thác. | LLO3 | tách | Nguồn 27 |
| F02 | Phát biểu mục tiêu và rủi ro của khai thác. | Giải thích vì sao chọn tốt nhất hiện tại chưa đủ. | Thăm dò → bài số. | LLO3 | tách | Nguồn 27 |
| F03 | Dùng bảng giả định và yêu cầu nêu dữ kiện còn thiếu trước khi quyết định. | Đo hiểu biết về bất định mà không ngụ ý có đáp án duy nhất. | Khái niệm → Tic-tac-toe. | LLO3 | thêm, sửa sau phản biện | Nguồn 27 |
| G00 | Giới thiệu miền ví dụ và giả thiết đối thủ chọn đều trên nước hợp lệ. | Cần một bài toán nhỏ có điều kiện đánh giá rõ. | Đánh đổi → tìm kiếm. | LLO4 | sửa sau phản biện | Nguồn 28 |
| G01 | Dùng một thế cờ cụ thể để minh họa ba nhánh tìm kiếm hợp lệ. | Cần nền kiểm chứng được trước cách học. | Bàn cờ → biểu diễn RL. | LLO4 | sửa sau phản biện | Nguồn 28 |
| G02 | Chốt $\mathcal A(S_t)$ và thưởng theo góc nhìn tác tử, gồm thưởng 0 trước kết thúc. | Sửa lỗi nguồn và hoàn thiện kiểu đại lượng. | Tìm kiếm → giá trị. | LLO4 | sửa sau phản biện | Nguồn 29–30 |
| G03 | So sánh thưởng tức thời cộng giá trị tiếp diễn dưới cùng $\pi$, không dùng số tùy ý. | Cần ứng dụng kiểm chứng được của E01 và đúng quy ước trạng thái kết thúc. | Biểu diễn → kiểm tra. | LLO3–LLO4 | sửa sau phản biện | Nguồn 26, 29–30 |
| G04 | Kiểm tra đồng thời luật và vai trò thành phần. | Đo khả năng mô hình hóa. | Giá trị → ôn tập. | LLO3–LLO4 | thêm | Nguồn 26, 29–30 |
| H04 | Gom câu hỏi về mô hình cố định, dữ liệu phụ thuộc thời gian và phản hồi trễ. | Kiểm tra LLO1–LLO2 ngay sau ví dụ. | G04 → ôn tập thành phần. | LLO1–LLO2 | chuyển, sửa sau phản biện | Nguồn 38–40 |
| H05 | Gom câu hỏi về thành phần, đánh đổi và Tic-tac-toe. | Kiểm tra LLO3–LLO4. | Ôn tập 1 → thảo luận. | LLO3–LLO4 | gộp | Nguồn 41–42 |
| H06 | Chuyển AGI và robot tổng quát thành thảo luận có giới hạn. | Nguồn đưa kết luận quá mạnh. | Ôn tập → mô hình thế giới. | LLO1, LLO3 | sửa | Nguồn 14–15, 43 |
| H07 | Thảo luận lợi ích và rủi ro của mô hình thế giới. | Phân biệt dự báo với quyết định. | Robot tổng quát → tài liệu. | LLO3 | sửa | Nguồn 44 |
| Z00 | Thay trang cảm ơn bằng nguồn đọc, tự kiểm tra và lối vào phụ lục dọc. | Kết thúc bằng hành động học tập nhưng vẫn cho phép truy nguyên thông tin nguồn. | Thảo luận → kết thúc ngang; nhấn xuống để mở phụ lục. | LLO1–LLO4 | sửa | Nguồn 34, 45 |
| H00 | Đưa thông tin tổ chức chưa xác nhận vào nhánh dọc dưới Z00. | Cần truy nguyên mà không công bố chính sách cũ trên tuyến chính. | Z00 ↓ → chi tiết nguồn. | Không gán | chuyển phụ lục dọc | Nguồn 31–32 |
| H01 | Lưu mô tả chuẩn đầu ra của học phần trong nguồn, không dùng mã CLO. | Tránh gán chuẩn của học phần khác cho bài hiện tại. | Chuẩn đầu ra trong nguồn → kế hoạch nguồn. | Không gán | sửa | Nguồn 32 |
| H02 | Lưu kế hoạch và tài liệu trong nguồn để đối chiếu. | Giảm hai trang liệt kê và tránh coi là lịch hiện hành. | Chuẩn nguồn → đánh giá nguồn. | Không gán | gộp | Nguồn 33–34 |
| H03 | Lưu đánh giá và tiên quyết trong nguồn với trạng thái chưa áp dụng. | Tránh coi tỷ lệ nguồn là chính sách đã chốt. | Kế hoạch nguồn → hết phụ lục. | Không gán | gộp | Nguồn 35, 37 |
