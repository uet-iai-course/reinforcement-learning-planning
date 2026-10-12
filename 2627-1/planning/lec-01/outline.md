# Dàn ý Bài 01: Giới thiệu Học tăng cường

Bản viết lại trong đợt sửa 2026-10-12 (giai đoạn II, bộ trang chiếu), khớp deck `2627-1/lecture-01-gioi-thieu-hoc-tang-cuong.html` sau vòng biên tập theo năm báo cáo rà soát (70 `data-slide-id`, 7 mạch) và ghi chú bài giảng đã commit `e860f53`. Bản cũ (42 trang, phụ lục H00–H03) không còn hiệu lực; lịch sử thay đổi nằm trong `review-log.md`.

## Mục tiêu và phạm vi

- Đối tượng: sinh viên đại học đã học xác suất cơ bản và học máy nhập môn.
- Thời lượng: 150 phút, trong đó deck 120 phút; 30 phút còn lại chữa bài tập (không có bài thực hành, không có code demo vì nguồn không có mã).
- Phạm vi: lượt hữu hạn, không chiết khấu ($\gamma=1$), không giả thiết Markov; lịch sử $H_t$ ghi trên quan sát (quyết định chung §2). Bài 02 bổ sung tính Markov và hệ số chiết khấu.
- Mục tiêu học tập (trang P01), mỗi mục tiêu một sản phẩm kiểm tra được:
  1. Mô tả bài toán bằng tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng: Bài tập 01.1 (A05–A06).
  2. Phân biệt phần thưởng với nhãn; nhận diện bài toán Học tăng cường: Bài tập 01.2 (C05–C06).
  3. Tính lợi tức $G_t$ của lượt hữu hạn, kể cả tính ngược: Bài tập 01.3, 01.4, 01.10 (D04–D05).
  4. Phân biệt chính sách, hàm giá trị, mô hình; tính $v_\pi$ từ định nghĩa: Bài tập 01.5, 01.9, 01.11 (E03–E04).
  5. Nhận diện thăm dò và khai thác khi ước lượng còn ít mẫu: Bài tập 01.6 (F03–F04).
  6. Mô hình hóa Tic-tac-toe; tính nước khai thác một bước: Bài tập 01.7, 01.8 (G04–G05), bài tổng hợp Z02–Z02b.

## Khung lý thuyết chung

- **Bài toán trung tâm:** chọn hành động khi đánh giá chỉ đến sau cả chuỗi hành động, trên dữ liệu do chính hành động sinh ra.
- **Đối tượng và ký hiệu chung:** bước $t=0,1,\dots$; lượt kết thúc tại $T\le L$; $S_t\in\mathcal S$, $O_t\in\mathcal O$, $A_t\in\mathcal A(S_t)$, $R_{t+1}\in\mathbb R$; lịch sử $H_t=(O_0,A_0,R_1,\dots,R_t,O_t)$; lợi tức $G_t=\sum_{k=t+1}^T R_k$, $G_T=0$; chính sách $\pi(a\mid h)$; giá trị $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$; $\mathbb E_\pi$ theo chính sách và luật môi trường, $\mathbb E$ chỉ theo luật môi trường khi hành động đã cố định.
- **Giả thiết:** luật của môi trường cố định (không phụ thuộc chính sách); lượt hữu hạn; phần thưởng bị chặn, thuộc tập hữu hạn trong các lượt nhiều bước; giá trị sau khi lượt kết thúc bằng $0$. Riêng Tic-tac-toe: quan sát đầy đủ, đối thủ theo chính sách cố định $\sigma(\cdot\mid\tilde s)$, chính sách của tác tử chỉ phụ thuộc thế cờ (ba điều kiện rút gọn, Nhận xét 01.19).
- **Chuỗi định nghĩa → kết quả → phương pháp:** vòng tương tác (Định nghĩa 01.1, 01.2) → tín hiệu học (Định nghĩa 01.5) → lợi tức (Định nghĩa 01.8) và hệ thức đệ quy (Mệnh đề 01.9) → chính sách, giá trị, mô hình (Định nghĩa 01.11, 01.12, 01.14), thăm dò và khai thác (Định nghĩa 01.16) → phân tích một bước (Mệnh đề 01.20) → nước khai thác một bước (Định nghĩa 01.21).
- **Giới hạn áp dụng:** giá trị trên lịch sử khó lưu trữ; giá trị theo quan sát có thể sai khi quan sát không đầy đủ; nước khai thác một bước phụ thuộc chính sách đang đánh giá, chưa chắc tối ưu và cần mô hình của đối thủ.

## Bảy mạch

| Mạch | Tên (trùng trang "Nội dung" và trang tiêu đề mạch) | Trang tiêu đề | `id` | Trang | Số trang | Phút |
|---|---|---|---|---|---:|---:|
| 1 | Mở đầu | P00 (bìa) | — | P00, P01a, P01, P02, P03 | 5 | 8 |
| 2 | Tác tử học từ tương tác | AT | `mach-2` | AT, A00, A00b, A01, A01c, A01d, A05, A06, A03, A04, B01 | 11 | 18 |
| 3 | Tín hiệu học và dữ liệu tương tác | CT | `mach-3` | CT, C00, C01, C03, C04b, C04c, C05, C06 | 8 | 11 |
| 4 | Phần thưởng và lợi tức | DT | `mach-4` | DT, D00, D01, D02, D02b, D02c, D04, D05, D03, D03b | 10 | 16 |
| 5 | Chính sách, hàm giá trị, mô hình và thăm dò | ET | `mach-5` | ET, E00, E01, E00b, E01b, E03, E04, E02a, E02, F00, F00b, F01, F02, F03, F04 | 15 | 27 |
| 6 | Tic-tac-toe như một bài toán Học tăng cường | GT | `mach-6` | GT, G00, G01, G02, G02b, G04, G05, G02c, G03, G03c, G03b, G03d, G03e | 13 | 26 |
| 7 | Tổng kết và chuyển tiếp | ZT | `mach-7` | ZT, Z01, Z01b, Z02, Z02b, Z03, H04, Z00 | 8 | 14 |
| | | | | | **70** | **120** |

Ba cặp bài tập C05–C06, D04–D05, G04–G05 chữa trong khối 30 phút bài tập, không tính vào 120 phút (chi tiết trong `storyboard.md`).

Mã `<tiền tố>00` đều đã dùng cho trang nội dung trong bản cũ nên trang tiêu đề mạch dùng `<tiền tố>T` (quyết định chung §5). Mạch E và F của bản cũ gộp thành mạch 5 (quyết định chung §8).

## Bảng thuật ngữ Việt–Anh

| Tiếng Việt | Tiếng Anh | Lần đầu trên deck |
|---|---|---|
| Học tăng cường | reinforcement learning | P00 |
| tác tử | agent | A01 (ghi chú P00) |
| môi trường | environment | A01 |
| hành động | action | ghi chú P00 |
| trạng thái | state | A01c |
| quan sát | observation | A01c |
| lịch sử | history | A01c |
| phần thưởng | reward | P01a |
| lượt | episode | P01a |
| thời điểm kết thúc | — ($T$) | D01 |
| quỹ đạo | trajectory | D01 |
| lợi tức | return | P01a |
| giả thuyết phần thưởng | reward hypothesis | D03 |
| hệ số chiết khấu | discount factor | ghi chú P00, P01a |
| học có giám sát | supervised learning | C03 |
| học không giám sát | unsupervised learning | C03 |
| độc lập và cùng phân phối | independent and identically distributed, i.i.d. | ghi chú C03 |
| chính sách | policy | P01a |
| chính sách xác định | deterministic policy | E01 |
| thử và sai | trial-and-error | C04b |
| sai phân thời gian | temporal difference, TD | ghi chú D02b |
| bài toán dự đoán; bài toán điều khiển | prediction; control | ghi chú E01b; G03d |
| nước đi, phiên (của X) | move, turn | G00, G02 ("lượt" chỉ dùng cho episode) |
| hàm giá trị | value function | E01b |
| mô hình | model | E02 |
| lập kế hoạch | planning | E02 |
| phương pháp có mô hình | model-based | E02 |
| phương pháp phi mô hình | model-free | E02 |
| hành động tham lam | greedy action | F01 ("tham lam (greedy)") |
| khai thác | exploitation | F01 |
| thăm dò | exploration | F01 |
| tìm kiếm cây | tree search | B01 |
| cây trò chơi | game tree | G01 |
| quy tắc phá hòa | tie-breaking | G03d |
| trạng thái sau nước đi | afterstate | ghi chú G03d |

## Ký hiệu

| Ký hiệu | Nghĩa | Ghi chú |
|---|---|---|
| $t$, $T$, $L$ | bước; thời điểm kết thúc; số hành động tối đa | $T\le L$, $T$ ngẫu nhiên |
| $S_t$, $O_t$, $A_t$, $R_{t+1}$ | trạng thái, quan sát, hành động, phần thưởng | $R_{t+1}$ thuộc chuyển từ $t$ sang $t+1$ |
| $H_t$, $h$ | lịch sử trên quan sát; một giá trị | quyết định chung §2 |
| $G_t$ | lợi tức không chiết khấu | $G_T=0$ |
| $\pi(a\mid h)$; $\pi_1,\pi_u,\pi_w$ | chính sách; ba chính sách cụ thể | $\pi_1$: sạch thì phải, bẩn thì hút; $\pi_u$: chọn đều; $\pi_w$: thắng ngay nếu có |
| $v_\pi(h)$, $v_\pi(s)$ | giá trị trên lịch sử; trên thế cờ | thay $V^\pi$ của bản cũ |
| $\sigma(\cdot\mid\tilde s)$ | chính sách của đối thủ O | chọn đều |
| $\widehat S_{t+1}$, $\widehat R_{t+1}$ | dự báo của mô hình | |
| $N(a)$, $\bar r(a)$ | số lần thử; trung bình mẫu | |
| $a^*$ | nước khai thác một bước | |
| $\gamma$ | hệ số chiết khấu | không dùng; Bài 02 |

Tên hành động và quan sát (phải, trái, hút, sạch, bẩn) viết bằng chữ thường ngoài KaTeX trên deck để tránh cảnh báo phông KaTeX với ký tự tiếng Việt; ghi chú bài giảng dùng `\text{…}`.

## Ví dụ xuyên suốt

1. **Robot dọn dãy bốn ô** (số liệu sư phạm tự xây dựng, thu nhỏ từ robot dọn nhà của nguồn tr. 4–8): A00, A00b, A01d, A05–A06, C00, C01, C04c, C05, D00, D02, D02c, D03b, D04–D05, E01 ($\pi_1$), E03–E04, E02a, F00–F04 (hai chế độ hút), Z02–Z02b. Mỗi lần dùng trả lời một câu hỏi mới: lượt, trạng thái và quan sát, nhãn và phần thưởng, thứ tự dữ liệu, lợi tức, thiết kế phần thưởng, giá trị, mô hình, thăm dò, phân tích một bước.
2. **Thế cờ Tic-tac-toe bốn ô trống** $s$ (X ở 1, 5; O ở 2, 4, 8) và thế cờ hai ô trống $s'$ suy ra: E00, E00b, F02, G00–G03e. Bài tập G04–G05 dùng thế cờ $u$ khác.

## Ánh xạ nguồn (PPTX 45 trang) sang deck

| Trang nguồn | Nội dung | Trang đích | Quyết định |
|---:|---|---|---|
| 1 | Tiêu đề | P00 | sửa: thêm câu luận đề, đơn vị, học kỳ |
| 2 | Dàn ý | P01, P02 | sửa: mục tiêu gắn bài tập; nội dung đánh số 1–7 |
| 3–5 | Tác tử học qua tương tác | A00, A00b, A01, A01c, A01d | sửa: ví dụ robot có số trước định nghĩa |
| 6 | Ghi nhớ, thích nghi, khái quát; điều khiển | A03 | gộp A02 cũ vào A03 |
| 7–8 | Giới hạn mô hình cố định | A04 | giữ ba vấn đề, có số $3^5$, $3^{50}$ |
| 9 | Đặc điểm Học tăng cường | C00 (ghi chú), C04b | sửa |
| 10–13 | AlphaGo, thao tác robot | B01 | gộp B00–B02 cũ; dữ kiện chi tiết ở Bài tập 01.9, 01.11 |
| 14–15 | AGI, tác tử nền tảng | — | bỏ khỏi deck; thành Bài tập 01.16 [Tìm hiểu] |
| 16, 18 | Tiêu đề phần, lĩnh vực liên quan | CT | bỏ `rl-fields.svg` (ghi chú đã bỏ) |
| 17 | Hai đặc trưng: thử và sai, phản hồi trễ | C04b | thêm dòng "Hai đặc trưng" (rà soát RL) |
| 19 | Ba dạng học | C00 (hình), C03, C04b | tách định nghĩa |
| 20 | Câu hỏi nhỏ | C05 (d) | thành tình huống (d) |
| 21 | Khác biệt chính | C01, C04c | ví dụ đổi thứ tự và bốn khác biệt |
| 23–25 | Phần thưởng, giả thuyết, hậu quả dài hạn | D00–D03b | thêm hệ thức đệ quy, ví dụ chi phí, ví dụ bình hoa |
| 26 | Ba thành phần | E00–E01b, E02a, E02 | tách chính sách, giá trị, mô hình |
| 27 | Thăm dò và khai thác | F00–F04 | thêm ví dụ hai chế độ hút; F02 là ứng dụng trên Tic-tac-toe |
| 28 | Tic-tac-toe bằng tìm kiếm | G00, G01 | vẽ lại cây đủ bốn nhánh |
| 29–30 | Tic-tac-toe bằng Học tăng cường | G02–G03d, G03e | sửa tập hành động, chỉ số bước, giá trị sau nước thắng; Hình 1.1 (tr. 30) vẽ lại ở G03e |
| 31–37 | Thông tin học phần | — | bỏ (thông tin tổ chức chưa xác minh; quyết định chung §8) |
| 38–42 | Trắc nghiệm | H04 | thành "Câu hỏi tự kiểm tra" |
| 43–44 | Thảo luận | — | Bài tập 01.16 [Tìm hiểu] |
| 45 | Cảm ơn | Z00 | thay bằng bài tập về nhà và tài liệu đọc |

## Ánh xạ ghi chú bài giảng sang deck

| `note-topic-id` | Chủ đề | Mục ghi chú | `data-slide-id` |
|---|---|---|---|
| `lec-01-topic-01` | Tác tử học từ tương tác | §1 | AT, A00–A01d, A05–A06 |
| `lec-01-topic-08` | Giới hạn của điều khiển với mô hình cố định | §1.4 | A03, A04, B01 |
| `lec-01-topic-02` | Tín hiệu học và dữ liệu tương tác | §2 | CT, C00–C06 |
| `lec-01-topic-03` | Phần thưởng và lợi tức | §3.1–3.3 | DT, D00–D02c, D04–D05 |
| `lec-01-topic-10` | Giả thuyết phần thưởng | §3.4 | D03, D03b |
| `lec-01-topic-04` | Chính sách, hàm giá trị và mô hình | §4.1–4.3 | ET, E00–E04, E02a, E02 |
| `lec-01-topic-05` | Thăm dò và khai thác | §4.4 | F00–F04 (F02 nối sang G03e) |
| `lec-01-topic-06` | Tic-tac-toe như một bài toán Học tăng cường | §5.1, 5.3–5.4 | GT, G00–G01, G02, G02b, G03–G05, G03e |
| `lec-01-topic-07` | Lịch sử và thế cờ trong Tic-tac-toe | §5.2 | G02c |
| `lec-01-topic-11` | Đọc thêm: tác tử nhiều nhiệm vụ và mô hình thế giới | Hướng dẫn đọc thêm | — (Bài tập 01.16) |

## Số hiệu kết quả dùng trên deck (theo ghi chú `e860f53`)

Mỗi trang dẫn tối đa một số hiệu kết quả, trong ghi chú diễn giả: Định nghĩa 01.1 (A01), 01.2 (A01c), 01.5 (C04b), 01.7 (D01), 01.8 (D02), 01.11 (E01), 01.12 (E01b), 01.14 (E02), 01.16 (F01), 01.18 (G02), 01.21 (G03d); Nhận xét 01.3 (A01d), 01.4 (A04), 01.6 (C04c), 01.10 (D03), 01.17 (F02), 01.19 (G02c), 01.22 (G03e); Mệnh đề 01.9 (D02b), 01.20 (G03b); Ví dụ 01.1 (A00b), 01.2 (C01), 01.3 (D00), 01.4 (D02c), 01.5 (D03b), 01.6 (E00), 01.7 (E00b), 01.8 (E02a), 01.9 (F00b), 01.10 (G03); Bài tập 01.1 (A05), 01.2 (C05), 01.3 (D04), 01.5 (E03), 01.6 (F03), 01.7 (G04), 01.9 (B01). Trang tổng kết Z01 không dẫn số hiệu; P01 ánh xạ mục tiêu sang số bài tập.

Lệch tạm thời với ghi chú: D02c dùng $L=4$ (Ví dụ 01.4 của ghi chú ghi $L=5$); deck dùng "phiên"/"nước đi" của X thay cho "lượt của X" trong §5.1 của ghi chú. Đề nghị sửa ghi chú trong `review-log.md`.

## Nguồn

- Bài giảng gốc (2025–2026), *Reinforcement Learning and Planning*, bài 1 (PPTX 45 trang, tệp không được theo dõi trong kho).
- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2: §1.1–1.5, §2.1–2.2, §3.1–3.5, §6.8, §8.1, §17.3.
- Silver, D. (2015), *Lectures on Reinforcement Learning*, bài 1.
- Silver, D. và cộng sự (2016), "Mastering the game of Go with deep neural networks and tree search", *Nature* 529.
- Goodfellow, I., Bengio, Y. và Courville, A. (2016), *Deep Learning*, §5.1.3.
