# Storyboard Bài 01: Giới thiệu Học tăng cường

Bản sau vòng biên tập theo năm báo cáo rà soát (giai đoạn II, 2026-10-12): 70 trang, 7 mạch, 6 trang tiêu đề mạch. Âm tiết đo bằng `density.py` của đợt sửa (token theo khoảng trắng sau khi bỏ KaTeX, tiêu đề, ghi chú; dấu câu đứng sau công thức cũng bị đếm). Quyết định `giữ | sửa | gộp | tách | thêm | bỏ` so với deck 42 trang trước đợt sửa; cột "Vòng biên tập" ghi thay đổi sau rà soát và mã phát hiện (SV, RL, TOAN, PB, MACH).

## Bản đồ mạch

| Mạch | Loại | Trang tiêu đề mạch | Chức năng | Đầu vào | Đầu ra | Đóng góp cho vấn đề trung tâm | Phút |
|---|---|---|---|---|---|---|---:|
| 1. Mở đầu | mở đầu | P00 (bìa) | Luận đề, tiên quyết và quy ước, mục tiêu, nội dung, vấn đề trung tâm | — | Bài toán: chọn hành động khi đánh giá chỉ đến sau cả chuỗi | Câu trả lời có điều kiện của từng mạch | 8 |
| 2. Tác tử học từ tương tác | phát triển, khái niệm | AT (`mach-2`) | Vòng tương tác, trạng thái, quan sát, lịch sử; giới hạn mô hình cố định | Robot dọn dãy bốn ô | $S_t,O_t,A_t,R_{t+1},H_t$; nhu cầu học | Ai chọn, ai sinh dữ liệu, dữ liệu gồm gì | 18 |
| 3. Tín hiệu học và dữ liệu tương tác | phát triển, khái niệm | CT (`mach-3`) | Phần thưởng so với nhãn; thứ tự dữ liệu; thử và sai, phản hồi trễ | Vòng tương tác | Tiêu chí nhận dạng; nhu cầu đo hậu quả dài hạn | Tín hiệu là phần thưởng | 11 |
| 4. Phần thưởng và lợi tức | phát triển, khái niệm + kết quả | DT (`mach-4`) | Lượt, $T$, lợi tức, hệ thức đệ quy, giả thuyết phần thưởng | Phản hồi trễ | $G_t=R_{t+1}+G_{t+1}$; mục tiêu $\mathbb E[G_0]$ | Hậu quả dài hạn đo bằng $G_t$ | 16 |
| 5. Chính sách, hàm giá trị, mô hình và thăm dò | phát triển, khái niệm | ET (`mach-5`) | Chính sách, giá trị, mô hình; thăm dò và khai thác (cả trên Tic-tac-toe) | Lợi tức của một lượt | $\pi$, $v_\pi(h)$, mô hình, hành động tham lam | Tách chọn khỏi đánh giá; ít mẫu cần thăm dò | 27 |
| 6. Tic-tac-toe như một bài toán Học tăng cường | ứng dụng + kết quả | GT (`mach-6`) | Mô hình hóa, rút gọn lịch sử, phân tích một bước, nước khai thác một bước, học giá trị từ ván chơi | $\pi$, $v_\pi$, khai thác, thăm dò | Mệnh đề 01.20, $a^*=9$, $v_{\pi_u}(s)=\frac12$; cập nhật từ ván chơi | Chọn bằng một bước nhìn trước; khi thiếu mô hình thì học | 26 |
| 7. Tổng kết và chuyển tiếp | kết luận | ZT (`mach-7`) | Tổng kết có giả thiết, bài tổng hợp, kết luận song song với P03, tự kiểm tra, bài tập về nhà | Mọi kết quả | Năng lực mang sang Bài 02 | Trả lời có điều kiện, có số liệu | 14 |

Tổng 120 phút. Ba cặp bài tập C05–C06, D04–D05, G04–G05 được chữa trong khối 30 phút bài tập, không tính vào 120 phút; trên lớp chỉ nêu đề. Các cặp còn lại (A05–A06, E03–E04, F03–F04, Z02–Z02b) chữa trên lớp, khoảng 3 phút mỗi cặp. Trang có thể bỏ khi thiếu giờ: B01, D03b, F02 (nội dung có trong ghi chú bài giảng). G03c không bỏ được: đây là trang duy nhất có $v_{\pi_u}(s)=\frac12$, dùng ở G00, Z03 (rà lại vòng 2, R2).

## Cụm khái niệm và thời lượng

| Cụm | Mạch | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Phút | Ghi chú bước |
|---|---|---|---|---|---|---|---|---:|---|
| Tác tử, môi trường, vòng tương tác | 2 | A00 | A01 | A00b | A01 (Định nghĩa 01.1) | A01d | A05–A06 | 7 | Ví dụ dẫn nhập A00b đứng trước trực giác, làm cụ thể "phần thưởng chỉ đến ở $R_4$" |
| Trạng thái, quan sát, lịch sử | 2 | A00 | A01c | A00b | A01c (Định nghĩa 01.2) | A01d | A05–A06 | 5 | Bài tập đặt ngay sau ứng dụng (MACH 3.1d) |
| Giới hạn mô hình cố định (phụ) | 2 | A03 (Nhu cầu:) | A03 (hình) | A03 | không áp dụng: nhận xét, không có định nghĩa | A04, B01 | B01 (câu hỏi, lời giải trong ghi chú) | 6 | Chu trình rút gọn |
| Ba dạng tín hiệu học | 3 | C00 | C00 (hình), C01 | C01 | C03, C04b (Định nghĩa 01.5) | C04c | C05–C06 (khối 30 phút) | 11 | |
| Phần thưởng, lượt, lợi tức, hệ thức đệ quy | 4 | D00 | D00 (Trực quan, $1=0+1$) | D00 | D01, D02, D02b (Định nghĩa 01.7, 01.8, Mệnh đề 01.9) | D02c | D04–D05 (khối 30 phút) | 12 | Bài tập đặt ngay sau ứng dụng (MACH 3.9) |
| Giả thuyết phần thưởng (phụ) | 4 | D03 (ghi chú) | D03 | D03b | D03 (Nhận xét 01.10) | D03b | D03b (Câu hỏi:) | 4 | Chu trình rút gọn |
| Chính sách | 5 | E00 | E01 | E00 (bằng lời) | E01 (Định nghĩa 01.11) | E00b | E03–E04 | 6 | $\pi_w,\pi_u,\pi_1$ được đặt tên ở E01 (PB 18) |
| Hàm giá trị | 5 | E00 | E00b | E00b | E01b (Định nghĩa 01.12) | G03 | E03–E04 | 7 | |
| Mô hình (phụ) | 5 | E02a (Nhu cầu:) | E02a | E02a | E02 (Định nghĩa 01.14) | G03d, Z02b | H04 câu 4 | 4 | |
| Thăm dò và khai thác | 5 | F00 | F00b | F00b | F01 (Định nghĩa 01.16) | F02 (Tic-tac-toe), G03e | F03–F04 | 10 | |
| Mô hình hóa Tic-tac-toe | 6 | G00 | G01 | G00 | G02, G02b (Định nghĩa 01.18) | G04–G05 (khối 30 phút) | G04–G05 | 9 | Bài tập đặt ngay sau G02b vì chỉ dùng Định nghĩa 01.18 và luật một bước (rà lại vòng 2, R1) |
| Phân tích một bước, nước khai thác một bước | 6 | G02c (cầu nối: giá trị viết trên thế cờ), G03 (Nhu cầu:) | G01, G03c | G03, G03c (Ví dụ 01.10) | G03b (Mệnh đề 01.20), G03d (Định nghĩa 01.21) | G03d ($a^*=9$), Z02b | H04 câu 3, Z02 | 12 | |
| Học giá trị thế cờ từ ván chơi (phụ) | 6 | G03d (Lưu ý: cần mô hình) | G03e (hình) | G03e (Hình 1.1 của Sutton và Barto) | không áp dụng: thuật toán thuộc Bài 05 | — | — | 5 | Chu trình rút gọn; quyết định điều phối viên |

Không có thuật toán: nguồn không có thuật toán, ghi chú cũng không có khối `algorithm`.

## Từng trang

Âm tiết: trước đợt sửa → sau vòng biên tập ("—" khi trang mới).

### Mạch 1. Mở đầu (8 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| P00 | bìa, điểm vào mạch 1 | Luận đề, học phần, đơn vị, học kỳ | — → P01a | tất cả | sửa | — | 25 → 45 |
| P01a | tiên quyết | Nhắc lại kỳ vọng có điều kiện, kỳ vọng toàn phần, học có giám sát; ký hiệu; thuật ngữ tiếng Anh gom ở đây | P00 → P01 | 3, 4, 6 | thêm | thêm kỳ vọng toàn phần, thuật ngữ episode, reward, policy, return; bỏ $\gamma$, Markov khỏi mặt trang (PB 12, SV, RL) | — → 60 |
| P01 | mục tiêu | Sáu sản phẩm kiểm tra được | P01a → P02 | tất cả | sửa | ghi chú nêu sản phẩm (PB 31) | 80 → 77 (ngoại lệ trần 80) |
| P02 | nội dung | Bảy mạch đánh số | P01 → P03 | — | sửa | — | 63 → 44 (7 dòng, ngoại lệ quyết định chung §5) |
| P03 | vấn đề trung tâm | Bài toán và câu trả lời có điều kiện của mạch 2–6 | P02 → AT | tất cả | thêm | dòng 3, 5, 6 viết lại; dòng 6 nêu đủ giả thiết và "kỳ vọng" (MACH 3.15, PB 17, TOAN, RL) | — → 59 |

### Mạch 2. Tác tử học từ tương tác (18 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| AT | điểm vào mạch 2 | Tách tác tử khỏi môi trường, ghi lịch sử | P03 → A00 | 1 | thêm | dòng dẫn mới (MACH 3.1a); ghi chú viết lại | — → 39 |
| A00 | vấn đề + ví dụ dẫn nhập | Robot dọn dãy bốn ô | AT → A00b | 1 | sửa | nhu cầu riêng của mạch (MACH 3.1b); bỏ dòng lặp với hình (SV) | 16 → 30 |
| A00b | ví dụ | Một lượt tính tay (Ví dụ 01.1) | A00 → A01 | 1, 3 | thêm | dòng cuối thành "Diễn giải:" (PB 22) | — → 35 |
| A01 | trực giác + hình thức | Vòng tương tác (Định nghĩa 01.1) | A00b → A01c | 1 | sửa | — | 57 → 53 |
| A01c | trực giác + hình thức | Trạng thái, quan sát, lịch sử (Định nghĩa 01.2) | A01 → A01d | 1 | thêm | — | — → 59 |
| A01d | ứng dụng | $\mathcal S$, $\mathcal O$, $H_3$ của robot | A01c → A05 | 1 | thêm | — | — → 56 |
| A05 | kiểm tra | Bài tập 01.1 | A01d → A06 | 1 | thêm | dời lên sau A01d (MACH 3.1d); câu (c) theo ghi chú (SV, PB 32) | — → 58 |
| A06 | lời giải | Lời giải trên mặt trang | A05 → A03 | 1 | thêm | câu (c) sửa theo đề | — → 59 |
| A03 | vấn đề cụm phụ | Khi nào chương trình viết sẵn đủ | A06 → A04 | 1 | gộp A02 | thêm "Nhu cầu:" (MACH 3.1c, PB 24); hình ra hàng riêng, chữ SVG lớn hơn (SV) | 33 → 49 |
| A04 | ứng dụng cụm phụ | Ba giới hạn có số (Nhận xét 01.4) | A03 → B01 | 1 | sửa | kế hoạch vòng hở, luật ngẫu nhiên chưa biết, liệt kê không khả thi (RL, PB 14); hình ra hàng riêng | 53 → 56 |
| B01 | ứng dụng | AlphaGo và thao tác robot | A04 → CT | 1 | gộp B00–B02 | bỏ `.card` (SV); ghi chú AlphaGo sửa (RL); chữ SVG lớn hơn | 86 → 54 |

### Mạch 3. Tín hiệu học và dữ liệu tương tác (11 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| CT | điểm vào mạch 3 | So phần thưởng với nhãn, thứ tự dữ liệu | B01 → C00 | 2 | thêm | ghi chú viết lại (PB 13) | — → 38 |
| C00 | vấn đề + trực giác | Nhãn ở ô 1 so với phần thưởng | CT → C01 | 2 | sửa | dòng cuối: phần thưởng chỉ đánh giá hành động đã chọn (PB 5, MACH 3.10) | 29 → 51 |
| C01 | trực giác + ví dụ | Đổi thứ tự mẫu (Ví dụ 01.2) | C00 → C03 | 2 | sửa | — | 59 → 56 |
| C03 | hình thức | Học có giám sát, không giám sát | C01 → C04b | 2 | gộp C03, C04 | ghi chú bỏ câu lặp (PB 31) | 74 → 52 |
| C04b | hình thức | Học tăng cường (Định nghĩa 01.5) | C03 → C04c | 2 | thêm | thêm thử và sai (trial-and-error), phản hồi trễ (RL) | — → 59 |
| C04c | ứng dụng | Bốn khác biệt (Nhận xét 01.6) | C04b → C05 | 2 | thêm | "bước thứ tư" → $R_4$ (SV) | — → 55 |
| C05 | kiểm tra | Bài tập 01.2 | C04c → C06 | 2 | sửa | (d) nêu việc tự chọn cách học (PB 23); chữa trong khối 30 phút | 49 → 58 |
| C06 | lời giải | Lời giải trên mặt trang | C05 → DT | 2 | thêm | khối 30 phút | — → 57 |

### Mạch 4. Phần thưởng và lợi tức (16 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| DT | điểm vào mạch 4 | Cộng phần thưởng đến hết lượt | C06 → D00 | 3 | thêm | ghi chú viết lại | — → 36 |
| D00 | vấn đề + trực giác + ví dụ | Tổng còn lại $1,1,1,1,0$; $1=0+1$ | DT → D01 | 3 | sửa | thêm dòng trực giác của hệ thức đệ quy (PB 8) | 9 → 48 |
| D01 | hình thức | Định nghĩa 01.7 | D00 → D02 | 3 | sửa | — | 32 → 56 |
| D02 | hình thức | Lợi tức (Định nghĩa 01.8) | D01 → D02b | 3 | sửa | — | 38 → 25 |
| D02b | kết quả | Mệnh đề 01.9 | D02 → D02c | 3 | thêm | Ý nghĩa trước Chứng minh, Lưu ý vào ghi chú (PB 20); thêm TD (RL) | — → 44 |
| D02c | ứng dụng | Ví dụ 01.4 với $L=4$ | D02b → D04 | 3 | thêm | đặt $L=4$, diễn giải so với hút trước (TOAN, RL, PB 4); lệch ghi chú tạm thời | — → 52 |
| D04 | kiểm tra | Bài tập 01.3 | D02c → D05 | 3 | thêm | dời lên sau D02c (MACH 3.9); khối 30 phút; 2026-10-14: thêm vế "không cản robot sang ô kế tiếp" vào dòng "Câu hỏi:" (20 âm tiết, đúng trần dòng) | — → 46 → 53 |
| D05 | lời giải | Lời giải trên mặt trang | D04 → D03 | 3 | thêm | khối 30 phút | — → 35 |
| D03 | cụm phụ | Giả thuyết phần thưởng (Nhận xét 01.10) | D05 → D03b | 3 | tách | "không phải định lý" (PB 29) | 76 → 59 |
| D03b | ví dụ + kiểm tra | Bình hoa (Ví dụ 01.5) | D03 → ET | 3 | thêm | có thể bỏ khi thiếu giờ | — → 59 |

### Mạch 5. Chính sách, hàm giá trị, mô hình và thăm dò (27 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| ET | điểm vào mạch 5 | Tách chọn khỏi đánh giá, ước lượng khi thiếu dữ liệu | D03b → E00 | 4, 5 | thêm | dòng dẫn bao cả cụm thăm dò (MACH 3.2) | — → 35 |
| E00 | vấn đề + ví dụ | Thế cờ $s$, hai quy tắc viết bằng lời (Ví dụ 01.6) | ET → E01 | 4 | sửa | tên $\pi_w,\pi_u$ chuyển sang E01 (PB 18); "phiên X" (RL, PB, SV) | 22 → 58 |
| E01 | trực giác + hình thức | Chính sách (Định nghĩa 01.11); chính sách xác định | E00 → E00b | 4 | tách | đặt tên $\pi_w,\pi_u,\pi_1$; thuật ngữ "chính sách xác định (deterministic policy)" (brief mục 5) | 32 → 59 |
| E00b | ví dụ | Giá trị thế cờ hai ô trống (Ví dụ 01.7) | E01 → E01b | 4 | thêm | "kỳ vọng của lợi tức" (SV) | — → 59 |
| E01b | hình thức | Hàm giá trị (Định nghĩa 01.12) | E00b → E03 | 4 | tách | ghi chú: cầu nối thế cờ–lịch sử (PB 6), dự đoán (RL) | — → 59 |
| E03 | kiểm tra | Bài tập 01.5 | E01b → E04 | 4 | thêm | (c) dùng $\pi_1$ đã đặt tên ở E01 | — → 53 |
| E04 | lời giải | Lời giải trên mặt trang | E03 → E02a | 4 | thêm | kết bằng số (PB 30) | — → 42 |
| E02a | vấn đề + ví dụ cụm mô hình | M1, M2 (Ví dụ 01.8) | E04 → E02 | 4 | thêm | M2 dự báo $\widehat R_3=1$ (SV, TOAN); ghi chú nối từ E04 (MACH 3.11) | — → 59 |
| E02 | hình thức | Định nghĩa 01.14 | E02a → F00 | 4 | sửa | "trạng thái hoặc lịch sử"; phi mô hình học chính sách hoặc hàm giá trị (RL, PB 19) | 62 → 58 |
| F00 | vấn đề | Hai chế độ hút, bài toán một bước | E02 → F00b | 5 | sửa | nhu cầu nối với phi mô hình; "Bài toán một bước, lặp lại" (MACH 3.2, PB 7, SV) | 17 → 56 |
| F00b | trực giác + ví dụ | Ví dụ 01.9 | F00 → F01 | 5 | thêm | khoảng viết phân số đúng và xấp xỉ (TOAN) | — → 52 |
| F01 | hình thức | Định nghĩa 01.16 | F00b → F02 | 5 | gộp F01, F02 cũ | thêm "(greedy)" (RL) | 64 → 46 |
| F02 | ứng dụng | Thăm dò và khai thác trong Tic-tac-toe (nguồn tr. 27) | F01 → F03 | 5 | sửa | đổi thành ứng dụng trên Tic-tac-toe, nối sang G03e (MACH 3.3, quyết định điều phối viên); có thể bỏ khi thiếu giờ | — → 48 |
| F03 | kiểm tra | Bài tập 01.6 | F02 → F04 | 5 | sửa | — | 46 → 54 |
| F04 | lời giải | Lời giải trên mặt trang | F03 → GT | 5 | thêm | khoảng xấp xỉ (TOAN) | — → 40 |

### Mạch 6. Tic-tac-toe như một bài toán Học tăng cường (26 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| GT | điểm vào mạch 6; bước vấn đề của cụm phân tích một bước | Tách kỳ vọng lợi tức thành phần thưởng và giá trị kế tiếp | F04 → G00 | 6 | thêm | dòng dẫn mới (MACH 3.4, PB 16); từ khóa có "Mô hình hóa", "Học từ ván chơi" (vòng 2, R8) | — → 40 |
| G00 | vấn đề + ví dụ | "Ví dụ: thế cờ bốn ô trống": thế cờ $s$, phiên đi, $\mathcal A(s)$ | GT → G01 | 6 | sửa | "Nhắc lại:" thế cờ $s$ (MACH 3.12); "phiên X", "số nước X đã đi"; tiêu đề đổi (vòng 2, R1) | 45 → 52 |
| G01 | trực giác | Cây trò chơi, 10 nhánh, nhìn một bước | G00 → G02 | 6 | sửa | thêm hai dòng (PB 11, MACH 3.13) | 28 → 42 |
| G02 | hình thức | Định nghĩa 01.18 | G01 → G02b | 6 | sửa | định nghĩa $\tilde s$ (PB 10, SV) | 41 → 58 |
| G02b | hình thức | Luật một bước | G02 → G04 | 6 | thêm | Lưu ý rút (PB 25) | — → 56 |
| G02c | cầu nối vào cụm phân tích một bước | Ba điều kiện rút gọn (Nhận xét 01.19) | G05 → G03 | 6 | thêm | dời sau G04–G05 (vòng 2, R1) | — → 55 |
| G04 | kiểm tra | Bài tập 01.7 | G02b → G05 | 6 | sửa | dời lên sau G02b (MACH 3.5, vòng 2 R1); khối 30 phút | 52 → 55 |
| G05 | lời giải | Lời giải trên mặt trang | G04 → G02c | 6 | thêm | khối 30 phút | — → 53 |
| G03 | vấn đề + ví dụ | Bảng kỳ vọng bốn nước (Ví dụ 01.10) | G02c → G03c | 6 | sửa | "Nhu cầu:" (PB 1) nêu lại thế cờ $s$ ngay trong dòng (vòng 2, R1; gộp với "Nhắc lại" để giữ 6 dòng); phân số lớn (SV) | 13 → 34 |
| G03c | ví dụ, tiếp | $v_{\pi_u}(s)=\frac12$ | G03 → G03b | 6 | thêm | không bỏ được (vòng 2, R2) | — → 49 |
| G03b | kết quả | Mệnh đề 01.20 | G03c → G03d | 6 | thêm | ghi chú: kỳ vọng khi $\pi(a\mid h)=0$ (TOAN) | — → 38 |
| G03d | hình thức + ứng dụng | Định nghĩa 01.21 | G03b → G03e | 6 | thêm | "Giả thiết:", "Dạng khác:" trên lịch sử (TOAN, PB 9, SV); ghi chú $\gamma\lt1$, điều khiển (RL) | — → 56 |
| G03e | trực giác cụm phụ | Học giá trị thế cờ từ các ván đã chơi; Hình 1.1 vẽ lại | G03d → ZT | 6 | thêm | phát hiện nghiêm trọng RL, quyết định điều phối viên | — → 50 |

### Mạch 7. Tổng kết và chuyển tiếp (14 phút)

| ID | Vị trí, bước | Lý do tồn tại | Nối trước → sau | Mục tiêu | Quyết định | Vòng biên tập | Âm tiết |
|---|---|---|---|---|---|---|---|
| ZT | điểm vào mạch 7 | Giữ đủ giả thiết | G03e → Z01 | tất cả | thêm | ghi chú viết lại | — → 37 |
| Z01 | tổng kết (1/2) | Tương tác, tín hiệu học, lợi tức, giá trị | ZT → Z01b | 1–4 | thêm | thêm hàng ba dạng tín hiệu học; cột "Công thức hoặc thuật toán"; công thức không ngắt (MACH 3.8, SV, TOAN, RL) | — → 56 |
| Z01b | tổng kết (2/2) | Thăm dò, phân tích một bước, nước khai thác | Z01 → Z02 | 5, 6 | thêm | giả thiết dạng lịch sử và dạng thế cờ tách rõ; dòng viết tắt (MACH 3.7, TOAN, SV) | — → 59 |
| Z02 | bài tổng hợp | Robot từ ô 2, $L=3$, $\pi_u$ | Z01b → Z02b | 1, 3, 4 | thêm | (d) ghi "theo $v_{\pi_u}$, dạng trên lịch sử" | — → 58 |
| Z02b | lời giải | $\frac1{27}$; $0,\frac19,0$ | Z02 → Z03 | 1, 3, 4 | thêm | — | — → 54 |
| Z03 | trả lời vấn đề trung tâm | Năm dòng song song với P03, có số liệu; "Nguồn:" | Z02b → H04 | tất cả | thêm | viết lại (MACH 3.8, brief mục 11); giới hạn thứ tư trong ghi chú (MACH 3.6) | — → 59 |
| H04 | câu hỏi tự kiểm tra | Bốn câu nối các mạch | Z03 → Z00 | 1, 3, 4, 6 | sửa | câu 1, 2, 3 đổi (SV, MACH 3.5, 3.14, PB 27) | 106 → 60 |
| Z00 | bài tập về nhà | Bảng `Mạch \| Bài tập` theo bảng mạch của `exercises.md` (mạch 2–7; hàng "Chỉ trong ghi chú" cho 01.9–01.11); liên kết "Ghi chú bài giảng · Bài tập"; liên kết Bài 02 | H04 → — | tất cả | sửa | 2026-10-14: đồng bộ với `exercises.md` (thêm 01.12–01.16, cột mạch 7, liên kết tệp bài tập thay "Tệp bài tập: chưa có") | 82 → 57 → 71 (ngoại lệ trần 80) |

## Ngoại lệ mật độ

| Trang | Đo được | Trần áp dụng | Lý do |
|---|---|---|---|
| P01 | 77 âm tiết, 6 dòng | 80 (trang mục tiêu) | Sáu mục tiêu theo ghi chú bài giảng |
| P02 | 44 âm tiết, 7 dòng | 7 dòng khi bài có 7 mạch (quyết định chung §5) | Mỗi mạch một dòng |
| Z00 | 71 âm tiết, 6 dòng, tối đa 16 âm tiết mỗi dòng | 80 (bảng bài tập của mạch kết luận, nhóm trang tổng kết) | Bảng mạch–bài tập hai hàng cho mạch 2–7: mười ba bài của `exercises.md` và ba bài chỉ trong ghi chú; số hiệu và bốn dấu "—" tính là âm tiết. Trước 57, sau 71 |

Mọi trang còn lại ≤ 60 âm tiết, ≤ 6 dòng, ≤ 20 âm tiết mỗi dòng, ≤ 3 công thức hiển thị. 57/70 trang trên đích 40 (trung bình 51,3 sau đợt đồng bộ Z00 ngày 2026-10-14); không trang nào dùng CSS thu chữ.

## Quyết định thiết kế ghi lại (chuyển từ ghi chú diễn giả)

- Giả thuyết phần thưởng không có hàng trong bảng tổng kết vì là giả thuyết mô hình hóa, không phải kết quả.
- Thế cờ $s$ là số liệu sư phạm tự xây dựng (thế cờ của nguồn tr. 28–29 đã kết thúc).
- Hình 1.1 của Sutton và Barto (nguồn tr. 30) vẽ lại theo chiều ngang trong `tictactoe-learning.svg` để chữ đủ lớn trên khung 16:9; giữ đúng các nút a–g, e*, đường chấm cho nước không đi, hai mũi tên cập nhật c→a và g→e, không cập nhật sau nước thăm dò.
- AT dòng dẫn theo MACH 3.1a; nhu cầu "mô hình viết sẵn sai" giữ ở A03–A04 theo thứ tự nguồn.
