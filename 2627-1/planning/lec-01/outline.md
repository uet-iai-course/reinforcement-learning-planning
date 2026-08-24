# Dàn ý Bài 01: Giới thiệu Học tăng cường

## Mục tiêu và phạm vi

- Đối tượng: sinh viên đại học đã học học máy, học sâu và thuật toán.
- Phần trình chiếu P–G: 120 phút. H04–H07 và Z00: 30 phút chữa bài, thảo luận và giao tự kiểm tra.
- LLO1: giải thích tác tử học từ tương tác, phản hồi trễ và dữ liệu phụ thuộc thời gian.
- LLO2: phân biệt Học tăng cường với học có giám sát và không giám sát.
- LLO3: mô tả chính sách, hàm giá trị và mô hình tùy chọn.
- LLO4: biểu diễn Tic-tac-toe bằng trạng thái, hành động và phần thưởng.
- Chưa gán CLO vì bản nguồn dùng chuẩn đầu ra của học phần *Intelligent Agents and Robotics*. Cần đối chiếu đề cương Học tăng cường 2026–2027 trước khi gán.

## Dàn ý

| Cụm | Nội dung | Mục tiêu | Thời lượng |
|---|---|---|---:|
| 1 | Định hướng, tác tử học, giới hạn mô hình cố định và hai trường hợp | LLO1 | 34 phút |
| 2 | Khung Học tăng cường và ba dạng tín hiệu học | LLO1, LLO2 | 22 phút |
| 3 | Phần thưởng và kết quả dài hạn | LLO1 | 18 phút |
| 4 | Chính sách, hàm giá trị, mô hình tùy chọn | LLO3 | 14 phút |
| 5 | Thăm dò và khai thác | LLO1, LLO3 | 14 phút |
| 6 | Tic-tac-toe | LLO3, LLO4 | 18 phút |

Tổng sáu cụm P–G: 120 phút.

## Phần 30 phút cuối

| Trang | Hoạt động | Thời lượng |
|---|---|---:|
| H04 | Chữa câu hỏi về động cơ, tín hiệu và phản hồi trễ | 6 phút |
| H05 | Chữa câu hỏi về thành phần, đánh đổi và Tic-tac-toe | 7 phút |
| H06 | Thảo luận tác tử tổng quát | 7 phút |
| H07 | Thảo luận mô hình thế giới | 7 phút |
| Z00 | Giao tự kiểm tra và tài liệu đọc | 3 phút |

Tổng: 30 phút. Không có code demo vì bản nguồn không có nội dung mã. H00–H03 là phụ lục truy nguyên trong stack dọc dưới Z00 và không thuộc tuyến 150 phút.

Tuyến ngang: P00–G04 → H04–H07 → Z00. Tại Z00, nhấn ↓ để mở H00–H03 khi cần đối chiếu thông tin trong bản nguồn.

## Bảng thuật ngữ và ký hiệu

| Thuật ngữ hoặc ký hiệu | Cách dùng |
|---|---|
| Học tăng cường | Dùng cho *reinforcement learning*; viết đầy đủ ở lần đầu. |
| tác tử | Thực thể chọn hành động dựa trên thông tin hiện có. |
| môi trường | Hệ thống tiếp nhận hành động và phát sinh quan sát, phần thưởng. |
| $R_{t+1}\in\mathbb R$ | Phần thưởng sau hành động $A_t$ tại $S_t$. |
| $T$ | Chỉ số của trạng thái kết thúc trong nhiệm vụ hữu hạn. |
| $G_t=\sum_{k=t+1}^{T}R_k$ | Tổng phần thưởng từ sau bước $t$ đến khi kết thúc. |
| $H_t$, $h_t$ | Biến lịch sử ngẫu nhiên và lịch sử đã quan sát đến bước $t$. |
| $\pi(a\mid h_t)$ | Phân phối chọn hành động; chính sách có thể ngẫu nhiên. |
| $V^\pi(h_t)$ | Kỳ vọng của $G_t$ dưới chính sách $\pi$, theo ngẫu nhiên của chính sách và môi trường. |
| mô hình môi trường | Dự báo quan sát hoặc trạng thái kế tiếp và phần thưởng; thành phần tùy chọn. |
| $S_t$ | Trạng thái Tic-tac-toe ở bước $t$. |
| $\mathcal A(S_t)$ | Tập ô trống ở trạng thái $S_t$. |
| $A_t$ | Hành động thỏa $A_t\in\mathcal A(S_t)$. |

## Ánh xạ 45 trang nguồn

| Trang nguồn | Nội dung nguồn | Trang đích | Quyết định và lý do |
|---:|---|---|---|
| 1 | Tiêu đề | P00 | Sửa tên học phần và niên khóa. |
| 2 | Dàn ý | P01–P02 | Tách mục tiêu và bản đồ để định hướng rõ. |
| 3 | Tiêu đề phần nền tảng | A00 | Giữ vai trò chuyển phần. |
| 4 | Tác tử học qua tương tác | A00–A01 | Sửa thành vòng tương tác có nhãn. |
| 5 | Điều kiện mô tả tác tử, ví dụ | A01 | Gộp thành bốn dữ kiện trong ghi chú. |
| 6 | Ghi nhớ, thích nghi, khái quát; điều khiển | A02–A03 | Tách nhu cầu khỏi cách tiếp cận. |
| 7 | Giới hạn robot dọn nhà | A04 | Giữ ví dụ, rút lời. |
| 8 | Không gian lớn, bất định | A04 | Gộp với giới hạn cùng cụm. |
| 9 | Cách tiếp cận Học tăng cường | A04, C01 | Tách động cơ và định nghĩa. |
| 10 | Tiến bộ gần đây, ảnh | B00 | Gộp thành trang dẫn cho hai trường hợp tiêu biểu. |
| 11 | Tiến bộ gần đây, ảnh | B01 | Thay ảnh bằng ca AlphaGo có nguồn. |
| 12 | Tiến bộ gần đây, thao tác robot | B02 | Vẽ lại cánh tay robot gắp và sắp xếp vật. |
| 13 | Tiến bộ gần đây, thao tác robot | B02 | Vẽ lại bàn tay robot đổi tư thế khối; không suy thêm thuật toán. |
| 14 | Học tăng cường và AGI | H06 | Chuyển thành thảo luận, không kết luận. |
| 15 | Tác tử nền tảng | H06–H07 | Gộp vào hai câu thảo luận có giới hạn. |
| 16 | Tiêu đề thành phần | C00 | Giữ chuyển phần và đổi tên cho đúng mạch. |
| 17 | Đặc điểm Học tăng cường | C01 | Giữ, biên tập ngắn. |
| 18 | Các lĩnh vực liên quan | C00 | Vẽ lại SVG. |
| 19 | Ba dạng học | C02–C04 | Tách để mỗi trang có một luận điểm. |
| 20 | Câu hỏi nhỏ | C03 | Gộp thành câu hỏi có đáp án trong ghi chú. |
| 21 | Khác biệt chính | C05 | Sửa thành tình huống nhận dạng bằng tương tác và phản hồi trễ. |
| 22 | Ví dụ tác tử | B01–B02, H06 | Phân bổ vào trò chơi, thao tác robot và thảo luận. |
| 23 | Định nghĩa phần thưởng | D00–D01 | Tách chuyển phần và định nghĩa. |
| 24 | Giả thuyết phần thưởng | D03 | Giữ với caveat mô hình hóa. |
| 25 | Hậu quả dài hạn | D02–D03 | Tách công thức tổng hữu hạn và ví dụ. |
| 26 | Ba thành phần | E00–E02 | Tách; sửa mô hình thành tùy chọn. |
| 27 | Thăm dò và khai thác | F00–F03 | Mở rộng thành chu trình có câu hỏi số. |
| 28 | Tic-tac-toe bằng tìm kiếm | G00–G01 | Vẽ lại bàn cờ và cây tìm kiếm. |
| 29 | Tic-tac-toe bằng Học tăng cường | G02–G03 | Sửa hành động và tập phần thưởng. |
| 30 | Hàm giá trị Tic-tac-toe | G03–G04 | Giữ, thêm kiểm tra mô hình hóa. |
| 31 | Tiêu đề thông tin học phần | H00 | Chuyển vào phụ lục dọc dưới Z00. |
| 32 | Tên, kế hoạch, CLO | H00–H01 | Chuyển ra phụ lục; bỏ mã CLO để không gán cho học phần hiện tại. |
| 33 | Lịch học | H02 | Gộp thành bản đồ SVG. |
| 34 | Tài liệu | H02, Z00 | Tách tài liệu dùng học và danh mục đọc. |
| 35 | Đánh giá | H03 | Giữ, ghi trạng thái chưa xác nhận. |
| 36 | Giảng viên và trợ giảng | P00, H00 | Bỏ tiểu sử khỏi mặt chiếu; không đủ căn cứ cho niên khóa mới. |
| 37 | Tiên quyết | H03 | Gộp với đánh giá. |
| 38 | Trắc nghiệm 1 | H04 | Chuyển thành câu hỏi ngắn và đặt liền sau G04. |
| 39 | Trắc nghiệm 2 | H04 | Gộp vào ôn tập 1. |
| 40 | Trắc nghiệm 3 | H04 | Gộp vào ôn tập 1. |
| 41 | Trắc nghiệm 4 | H05 | Gộp vào ôn tập 2. |
| 42 | Trắc nghiệm 5 | H05 | Gộp vào ôn tập 2. |
| 43 | Thảo luận robot tổng quát | H06 | Giữ, bỏ câu dẫn quảng bá. |
| 44 | Thảo luận mô hình thế giới và AGI | H07 | Giữ dạng thảo luận, không kết luận. |
| 45 | Cảm ơn | Z00 | Thay bằng tài liệu đọc, tự kiểm tra và chỉ dẫn mở phụ lục dọc. |

## Nguồn

- `RL-hk2-2025-2026/lecture1-introduction-to-RL.pptx`, 45 trang, tháng 02/2026.
- David Silver, *Introduction to Reinforcement Learning*: https://www.davidsilver.uk/wp-content/uploads/2020/03/intro_RL.pdf
- Sutton, R. S. & Barto, A. G. (2018), *Reinforcement Learning: An Introduction*: https://incompleteideas.net/book/the-book-2nd.html
- Silver et al. (2016), *Nature*: https://doi.org/10.1038/nature16961
