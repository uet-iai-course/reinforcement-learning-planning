# Dàn ý Bài 01: Giới thiệu Học tăng cường

## Mục tiêu và phạm vi

- Đối tượng: sinh viên đại học đã học học máy, học sâu và thuật toán.
- Phần trình chiếu chính: 120 phút. Phần bài tập: 30 phút chữa bài, thảo luận và giao tự kiểm tra.
- LLO1: giải thích tác tử học từ tương tác, phản hồi trễ và dữ liệu phụ thuộc thời gian.
- LLO2: phân biệt Học tăng cường với học có giám sát và không giám sát.
- LLO3: mô tả chính sách, hàm giá trị và mô hình tùy chọn.
- LLO4: biểu diễn Tic-tac-toe bằng trạng thái, hành động và phần thưởng.
- Chưa gán CLO vì bản nguồn dùng chuẩn đầu ra của học phần *Intelligent Agents and Robotics*. Cần đối chiếu đề cương Học tăng cường 2026–2027 trước khi gán.

## Bảy mạch ngoài

| Mạch | data-slide-id | Nội dung | Mục tiêu | Thời lượng |
|---|---|---|---|---:|
| 1. P+A+B | P00–P02, A00–A04, B00–B02 | Định hướng, tác tử học, giới hạn mô hình cố định, hai trường hợp tiêu biểu | LLO1 | 30 phút |
| 2. C | C00–C05 | Khung Học tăng cường và ba dạng tín hiệu học | LLO1, LLO2 | 22 phút |
| 3. D | D00–D03 | Phần thưởng và kết quả dài hạn | LLO1 | 18 phút |
| 4. E | E00–E02 | Chính sách, hàm giá trị, mô hình tùy chọn | LLO3 | 18 phút |
| 5. F | F00–F03 | Thăm dò và khai thác | LLO1, LLO3 | 14 phút |
| 6. G | G00–G04 | Tic-tac-toe | LLO3, LLO4 | 18 phút |
| 7. H+Z | H04–H07, Z00 | Bài tập: ôn tập, thảo luận, tự kiểm tra | LLO1–LLO4 | 30 phút |

Tổng trình chiếu chính (mạch 1–6): 120 phút. Mạch 7 là phần bài tập 30 phút. Phụ lục H00–H03 nằm trong stack dọc dưới Z00, không thuộc tuyến 150 phút.

Tuyến trình chiếu: P00–G04 → H04–H07 → Z00. Tại Z00, nhấn ↓ để mở H00–H03 khi cần đối chiếu thông tin trong bản nguồn.

## Phần 30 phút bài tập

| Trang | Hoạt động | Thời lượng |
|---|---|---:|
| H04 | Chữa câu hỏi về động cơ, tín hiệu và phản hồi trễ | 6 phút |
| H05 | Chữa câu hỏi về thành phần, đánh đổi và robot dọn nhà | 7 phút |
| H06 | Thảo luận tác tử tổng quát | 7 phút |
| H07 | Thảo luận mô hình thế giới | 7 phút |
| Z00 | Giao tự kiểm tra và tài liệu đọc | 3 phút |

Tổng: 30 phút. Không có code demo vì bản nguồn không có nội dung mã.

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
| cầu nối $h_t\leftrightarrow(S_t,\text{lượt})$ | Trong Tic-tac-toe quan sát đầy đủ, lịch sử $h_t$ rút gọn thành cặp (thế cờ $S_t$, lượt chơi); dùng ở E01, G00, G03. |
| $\pi(a\mid h_t)$ | Phân phối chọn hành động; chính sách có thể ngẫu nhiên. |
| $V^\pi(h_t)$ | Kỳ vọng của $G_t$ dưới chính sách $\pi$, theo ngẫu nhiên của chính sách và môi trường. |
| $a^*$ | Hành động khai thác một bước: $a^*\in\arg\max_{a\in\mathcal A(S_t)}\mathbb E_\pi[R_{t+1}+V^\pi(S_{t+1})\mid S_t,A_t=a]$; chỉ dùng ở G03. |
| $\widehat S_{t+1}$, $\widehat O_{t+1}$, $\widehat R_{t+1}$ | Dự báo của mô hình môi trường về trạng thái/quan sát kế tiếp và phần thưởng; dấu mũ biểu thị dự báo, không khẳng định đúng tuyệt đối. Dùng ở E02. |
| $R_{t+1}^{(a)}$ | Không dùng trong bản hiện hành; phần thưởng theo hành động được viết qua điều kiện $A_t=a$ trong kỳ vọng ở G03. |
| mô hình môi trường | Dự báo quan sát hoặc trạng thái kế tiếp và phần thưởng; thành phần tùy chọn. |
| $S_t$ | Trạng thái Tic-tac-toe ở bước $t$. |
| $\mathcal A(S_t)$ | Tập ô trống ở trạng thái $S_t$. |
| $A_t$ | Hành động thỏa $A_t\in\mathcal A(S_t)$. |

## Quy ước nội dung đã chốt trên HTML

- G03: kỳ vọng điều kiện $\mathbb E_\pi[\,\cdot\mid S_t,A_t=a\,]$; thưởng tức thời 0 cho nước chưa kết thúc, giá trị trạng thái kết thúc bằng 0.
- G04: bài kiểm tra mô hình hóa với ô 5 không hợp lệ; H05 có nhiệm vụ chuyển giao robot dọn nhà.
- G02: quy ước thưởng $+1/0/-1$ từ góc nhìn tác tử; $0$ ở bước chưa kết thúc và khi hòa.
- Mọi hình SVG có `alt`/`title`/`desc` mô tả; các câu nối giữa trang dẫn về nguồn tương ứng.

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
| 36 | Giảng viên và trợ giảng | H00 | Bỏ tiểu sử và nhân sự khỏi mặt chiếu; H00 chỉ lưu dấu rằng phụ lục có nguồn tổ chức chưa xác nhận. |
| 37 | Tiên quyết | H03 | Gộp với đánh giá. |
| 38 | Trắc nghiệm 1 | H04 | Chuyển thành câu hỏi ngắn và đặt liền sau G04. |
| 39 | Trắc nghiệm 2 | H04 | Gộp vào ôn tập 1. |
| 40 | Trắc nghiệm 3 | H04 | Gộp vào ôn tập 1. |
| 41 | Trắc nghiệm 4 | H05 | Gộp vào ôn tập 2. |
| 42 | Trắc nghiệm 5 | H05 | Gộp vào ôn tập 2. |
| 43 | Thảo luận robot tổng quát | H06 | Giữ, bỏ câu dẫn quảng bá. |
| 44 | Thảo luận mô hình thế giới và AGI | H07 | Giữ dạng thảo luận, không kết luận. |
| 45 | Cảm ơn | Z00 | Thay bằng tài liệu đọc, tự kiểm tra và chỉ dẫn mở phụ lục dọc. |

## Quyết định lược hoặc thay nội dung nguồn

- T5 (ví dụ cờ, xe tự hành, FinTech): chỉ giữ cờ và robot làm ví dụ xuyên suốt; FinTech không có chi tiết đủ để minh họa tín hiệu học trong phạm vi bài.
- T8 (Planning under uncertainty: xe tự hành, đăng ký môn học): gộp vào A04 dưới dạng "bất định và không gian lớn"; ví dụ đăng ký môn học không phục vụ mạch lập luận.
- T14 (RL as AGI, URL chat.openai.com): bỏ URL và hình chụp; chuyển thành thảo luận H06 vì không thể truy nguyên nội dung và không thuộc phạm vi khái niệm.
- T17 (lịch sử Bellman, thập niên 1950): lược khỏi mặt chiếu; chỉ giữ trong ghi chú C01 nếu cần.
- T22 (bốn ví dụ tác tử): phân bổ vào B01–B02 và H06; không giữ trang danh sách riêng.
- T23–T24 (ảnh raster từ lilianweng.github.io): thay bằng SVG quỹ đạo tự vẽ (D00) để đồng bộ phong cách và tránh phụ thuộc ảnh ngoài.
- T27 (ảnh UC Berkeley CS188): thay bằng SVG explore-exploit tự vẽ (F00).
- T29 (tập thưởng $\{1,0,-1,9\}$, hành động 1–9): "9" là lỗi đánh máy; thay bằng quy ước $+1/0/-1$ và tập hành động $\mathcal A(S_t)$ (G02), ghi rõ là lựa chọn mô hình hóa.
- T25 nêu cờ, sinh văn bản và đăng ký môn học. D03 giữ cờ và dùng lại robot dọn nhà từ T6–T8 để kiểm tra cách đặt phần thưởng; không thêm kịch bản giao hàng ngoài nguồn.
- URL và ảnh raster trong nguồn (mục Tài liệu, ảnh Pieter Abbeel, lilianweng, CS188): URL đầy đủ chỉ lưu trong outline và review-log, không đưa lên mặt chiếu; ảnh raster thay bằng SVG tự vẽ.
- Không khôi phục chi tiết ngoài phạm vi: lịch sử ngành, tiểu sử giảng viên, tỷ lệ đánh giá chi tiết chỉ nằm ở phụ lục H00–H03 với nhãn "trong nguồn, chưa xác nhận".

## Nguồn

- `RL-hk2-2025-2026/lecture1-introduction-to-RL.pptx`, 45 trang, tháng 02/2026.
- David Silver, *Introduction to Reinforcement Learning*: https://www.davidsilver.uk/wp-content/uploads/2020/03/intro_RL.pdf
- Sutton, R. S. & Barto, A. G. (2018), *Reinforcement Learning: An Introduction*: https://incompleteideas.net/book/the-book-2nd.html
- Silver et al. (2016), *Nature*: https://doi.org/10.1038/nature16961
