# Storyboard Bài 04 — Giải MDP bằng quy hoạch động

Bản storyboard theo chuẩn 2026-10-12, khớp deck `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html` sau giai đoạn II. Deck có **78 trang trong 7 mạch** (sau vòng biên tập theo năm báo cáo rà soát), trình chiếu **120 phút**; 30 phút còn lại của buổi dành cho chữa bài tập và bài thực hành CartPole. Ghi chú bài giảng (`materials/lec-04/lecture-note.md`, commit `36e8a5b`) là nguồn chuẩn; mỗi trang dẫn tối đa một số hiệu kết quả của ghi chú. Bản storyboard trước (45 trang) được thay toàn bộ; lịch sử nằm trong `review-log.md`.

## Bản đồ mạch

| N | Mạch | Loại | Trang tiêu đề mạch | Chức năng riêng | Đầu vào từ mạch trước | Đầu ra cho mạch sau | Đóng góp cho vấn đề trung tâm | Trang | Phút |
|---|---|---|---|---|---|---|---|---:|---:|
| 1 | Mở đầu | mở đầu | L04-A01 (bìa) | Đặt bài toán lập kế hoạch, khung chung, ví dụ xuyên suốt | Bài 03: MDP, lợi tức, Bellman kỳ vọng | Mô hình hai trạng thái, $\pi_0$; nhu cầu tính kỳ vọng của tổng vô hạn | Phát biểu bài toán và câu trả lời có điều kiện | 9 | 10 |
| 2 | Đánh giá chính sách | phát triển kiến thức, thuật toán | L04-B00, `mach-2` | Tính $v_\pi$ bằng lượt quét, chứng minh hội tụ, dừng có chặn | Mô hình, $\pi_0$ | $v_{\pi_0}=(10,11)$; phần dư; $\theta=(1-\gamma)\kappa$ | Giá trị của một chính sách là điểm bất động của $T_\pi$ | 13 | 24 |
| 3 | Cải thiện chính sách | phát triển kiến thức | L04-C00, `mach-3` | Đổi hành động theo nhìn trước mà giá trị không giảm | $v_{\pi_0}$ | $\pi_1$, $v_{\pi_1}=(10,30)$; nhu cầu đánh giá lại | Bước tiến tới chính sách tốt hơn | 10 | 18 |
| 4 | Lặp chính sách | phát triển thuật toán | L04-D00, `mach-4` | Xen kẽ đánh giá chính xác và cải thiện; tối ưu của chính sách ổn định | Định lý cải thiện, $\pi_1$ | $(\mathrm b,\mathrm b)$, $(27,30)$, Bellman tối ưu; chi phí đánh giá đầy đủ | Nghiệm tối ưu trong lớp chính sách Markov dừng sau hữu hạn vòng | 10 | 18 |
| 5 | Lặp giá trị | phát triển thuật toán | L04-E00, `mach-5` | Gộp cải thiện vào lượt quét; tồn tại chính sách tối ưu; ngưỡng dừng | Bellman tối ưu, chi phí đánh giá | $T_*$, Định lý 04.25, ngưỡng $\theta$; chi phí một lượt quét | Thay chuỗi quyết định bằng điểm bất động của $T_*$ | 16 | 24,5 |
| 6 | Lịch cập nhật và giới hạn của mô hình bảng | ứng dụng, giới hạn | L04-F00, `mach-6` | Chi phí, tại chỗ, bất đồng bộ, GPI, CartPole | $T_*$, giới hạn lượt quét toàn bộ | Điều kiện lịch, điều kiện mô hình | Phạm vi áp dụng và cách tổ chức tính | 10 | 14 |
| 7 | Tổng kết và chuyển tiếp | kết luận | L04-G00, `mach-7` | Tổng kết theo giả thiết, bài tập tổng hợp, trả lời vấn đề trung tâm | Kết quả mạch 2–6 | Nhu cầu của Bài 05 | Kết luận có điều kiện | 10 | 11,5 |

Tổng 78 trang, 120 phút. Bảy mạch theo kế hoạch A1 (không gộp cải thiện với lặp chính sách, vì nguồn và Sutton và Barto tách hai mục).

**Ngoại lệ số trang.** Quyết định chung mục 5 chấp nhận 60–70 trang khi phân bổ đủ 120 phút. Deck có 78 trang, vượt 8 trang so với mức trên, vì: sáu trang tiêu đề mạch (khoảng 0,5 phút mỗi trang), sáu trang lời giải tách ("…b") đọc nhanh, các trang tách để giữ trần mật độ, và ba trang thêm theo năm báo cáo rà soát (A01c, E05c, E06c; bỏ G03). Thời lượng từng trang cộng đủ 120 phút. **Có thể bỏ khi thiếu giờ** (nội dung còn trong ghi chú bài giảng): L04-B06c (Hệ quả 04.6), L04-E05c (chứng minh Định lý 04.25), L04-F04 (GPI), L04-F05b (Tình huống 04.1–04.2).

**Khối 30 phút ngoài phần trình chiếu:** chữa Bài tập 04.7–04.9 của ghi chú, phần còn lại của dãy năm ô trơn trượt ($V_2(\mathrm c_3)$, chọn $\theta$; Bài tập 04.13 của tệp bài tập) và bài thực hành CartPole (Bài tập 04.14, 04.15 của tệp bài tập). Bảy cặp bài tập có lời giải trên mặt trang (A05, B08/B08b, C07/C07b, D06/D06b, E08/E08b, F06/F06b, G04/G04b) nằm trong 120 phút.

## Cụm khái niệm và sáu bước

| Cụm | Dạng | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Phút |
|---|---|---|---|---|---|---|---|---:|
| Mô hình và lợi tức (rút gọn, nhắc Bài 03) | khái niệm | A03 | A04 (diễn giải trong ghi chú) | A04 | A01b, A01c (Nhắc lại, Ký hiệu) | A05 | A05 (lời giải fragment) | 10 |
| KN1 Đánh giá chính sách | thuật toán | B01 (Nhắc lại: giải hệ tốn $O(n^3)$; Nhu cầu: phép lặp rẻ hơn, dùng được khi thay trung bình bằng cực đại) | B01 (Trực quan., hình cập nhật kỳ vọng) | B02 (tính tay hai lượt quét, trước giả mã B05b) | B03, B04, B06, B06c, B05, B06b, B05b | B07 (giá trị chính xác, sai số $10\cdot0{,}9^k$) | B08/B08b (Bài tập 04.1, lời giải trên mặt trang) | 24 |
| KN2 Cải thiện chính sách | khái niệm | C01 | C01 (Trực quan.) | C02 (hai nhánh: 11 và 12,9) | C03, C04, C04b, C05 | C06 ($\pi_1$, $(10,30)$) | C07/C07b (Bài tập 04.2) | 18 |
| KN3 Lặp chính sách | thuật toán | D01 | D01 (hình chu trình) | D02 (tính tay ba vòng, trước giả mã D03) | D02b, D03, D05, D04, D04b | D04b (ghi chú) chứng nhận $(27,30)$; D05 (ghi chú) ví dụ ba vòng | D06/D06b (Bài tập 04.3) | 18 |
| KN4 Lặp giá trị | thuật toán | E01 (44 lượt quét, $O(n^3)$) | E01b | E02 (tính tay hai lượt quét, trước giả mã E04) | E03, E03b, E05b, E05c, E05, E07, E04 | E06, E06b (dãy năm ô), E06c (dãy năm ô trơn trượt: kỳ vọng nhiều nhánh) | E08/E08b (Bài tập 04.4) | 24,5 |
| KN5 Quy hoạch động bất đồng bộ | thuật toán | F01 (chi phí) và dòng "Nhu cầu:" của F02 | F02 (định nghĩa tại chỗ bằng lời, hình thứ tự cập nhật) | F02 (tính tay một lượt tại chỗ, trước F03) | F03, F03b | không áp dụng trên mặt trang: notebook chưa nhúng kết quả lịch bất đồng bộ; ghi chú diễn giả F06b nêu lịch theo quỹ đạo chỉ ghé 64/324 ô | F06/F06b (Bài tập 04.5) | 8 |
| KN6 GPI (rút gọn) | khái niệm phụ | F04 (ba thuật toán đã học) | F04 (hình hai quá trình) | không áp dụng: dùng lại ba thuật toán đã tính | F04 | không áp dụng | G07 không hỏi riêng; G02 đặt ba phương pháp cạnh nhau | 2 |
| KN7 Mô hình bảng của CartPole (ứng dụng giới hạn) | ứng dụng | F05 (trạng thái liên tục) | F05 (hình) | F05 (ô 71: $\approx1{,}559$) | không áp dụng: ánh xạ rời rạc hóa ở ghi chú | F05b (Tình huống 04.1–04.2) | G07 câu 3 | 4 |
| Tổng kết | kết luận | G00 | không áp dụng | G04 (tổng hợp) | không có khái niệm mới | G06 | G07 | 11,5 |

Ví dụ dẫn nhập: A04 làm cụ thể vấn đề A03; B02 truyền quy tắc $V_{k+1}(\mathrm s)=r+0{,}9V_k(\mathrm s_0)$ sang $T_\pi$ (B04) và sang Thuật toán 04.9 (B05b); C02 truyền phép "thưởng + $\gamma\cdot$ tiếp nối" sang $Q_V$ (C03); D02 truyền bảng ba vòng sang D02b, D03; E02 truyền cột "Cực đại" sang $T_*$ (E03) và hai lần lặp đầu của Thuật toán 04.28 (E04); F02 truyền cơ chế đọc giá trị mới nhất sang Thuật toán 04.31 (F03).

Mỗi thuật toán có tính tay trước giả mã và cho cùng kết quả với giả mã: B02 → B05b ($V_1$, $V_2$; dừng ở $k=44$ với $\theta=0{,}01$); D02 → D03 (ba vòng); E02 → E04 ($V_1=(1,3)$, $V_2=(2{,}7;5{,}7)$); F02 → F03 (lịch ngược cho $V_4$).

Các khái niệm phụ đi chu trình rút gọn có lý do: GPI chỉ gọi tên khuôn chung của ba thuật toán đã học; CartPole là ứng dụng của điều kiện mô hình, không dạy kỹ thuật rời rạc hóa mới; mạch tổng kết không đưa khái niệm mới.

## Thời lượng theo trang

| Mạch | Trang và phút | Tổng |
|---|---|---:|
| 1 | A01 0,5; A01b 1; A01c 1; A02 1; A02b 0,5; A03 2; A03b 1; A04 1,5; A05 1,5 | 10 |
| 2 | B00 0,5; B01 2; B02 2; B03 1,5; B04 2,5; B06 2,5; B06c 2; B07 2; B05 1,5; B06b 2; B05b 2; B08 2; B08b 1,5 | 24 |
| 3 | C00 0,5; C01 1,5; C02 2; C03 2; C04 2; C04b 2,5; C05 2,5; C06 2; C07 1,5; C07b 1,5 | 18 |
| 4 | D00 0,5; D01 1,5; D02 2; D02b 2; D03 2; D05 2; D04 2; D04b 2,5; D06 2; D06b 1,5 | 18 |
| 5 | E00 0,5; E01 1,5; E01b 1; E02 2; E03 2; E03b 1,5; E05b 2; E05c 2; E05 1,5; E07 2; E04 2; E06 1; E06b 1; E06c 1,5; E08 1,5; E08b 1,5 | 24,5 |
| 6 | F00 0,5; F01 1,5; F02 1,5; F03 1,5; F03b 1,5; F04 1,5; F05 1,5; F05b 1,5; F06 1,5; F06b 1,5 | 14 |
| 7 | G00 0,5; G01 1,5; G01b 1,5; G02 0,5; G02b 1; G04 1,5; G04b 1,5; G06 1,5; G07 1; G05 1 | 11,5 |

## Ngoại lệ mật độ

Số âm tiết đo bằng thuật toán của `density.py` (đếm cả dấu câu đứng sau công thức như một token). Sau rà lại vòng 2, 67/78 trang không bị gắn cờ; 11 trang có ngoại lệ (F03 nay đúng 60, không còn ngoại lệ). Đợt đồng bộ trang bài tập về nhà (2026-10-14) thêm ngoại lệ G05:

| Trang | Đo được | Trần áp dụng | Lý do |
|---|---|---|---|
| L04-A01 Bìa | 75 âm tiết, 6 dòng, dòng dài nhất 22 | không phải trang nội dung | Bìa gồm tên học phần, số bài, thuật ngữ gốc, câu luận đề hai câu do điều phối viên chốt, đơn vị |
| L04-A02 Mục tiêu học tập | 79, 5 dòng | 80 (trang mục tiêu) | Năm mục tiêu, mỗi mục tiêu kèm sản phẩm kiểm tra |
| L04-A02b Nội dung | 31, 7 dòng | 6 dòng | Bảy mạch; quyết định chung mục 5 cho phép 7 dòng |
| L04-A03 Vấn đề trung tâm | 74, 6 dòng | 80 (trang tổng quan, cùng loại với trang tổng kết) | Năm câu trả lời có điều kiện theo quyết định của điều phối viên (thêm điều kiện đánh giá chính xác, $v_*=T_*v_*$, chứng nhận chỉ thuộc MDP đã cho) |
| L04-G06 Trả lời vấn đề trung tâm | 79, 7 dòng | 80; 7 dòng | Viết song song từng dòng với A03 (brief mục 11) và có dòng "Nguồn:" bắt buộc |
| L04-G01, G01b Tổng kết | 74 và 80, ≤ 6 dòng | 80 (tổng kết) | Bảng ba cột kèm dòng giả thiết chung |
| L04-G02b Hội tụ | 77, 6 dòng | 80 (bảng so sánh) | Bảng bốn hàng và dòng giả thiết chung |
| L04-B00, E00, F00, G00 (trang tiêu đề mạch) | dòng dẫn 20–24 âm tiết | 25 (dòng dẫn trang tiêu đề mạch) | Script áp trần 20 cho mọi dòng; quy định riêng của trang tiêu đề mạch là ≤ 25 |
| L04-G05 Bài tập về nhà và tài liệu đọc | 63, 6 dòng, dòng dài nhất 17 | 80 (trang tổng kết) | Bảng bảy mạch hai hàng theo `exercises.md` (tệp bài tập; chỉ trong ghi chú), dòng tài liệu đọc, liên kết "Ghi chú bài giảng · Bài tập", dòng nối Bài 05; trước đợt sửa 60 âm tiết |
| L04-D05 Dừng hữu hạn | 67, 4 dòng | 60 | Hai câu chứng minh theo rà lại vòng 2 (TOAN): giá trị tăng nghiêm ngặt ở ít nhất một trạng thái nên dãy không lặp; số chính sách hữu hạn nên thuật toán dừng; giả thiết thêm $I_{\max}$ đủ lớn |

61 trang trên mức đích 40 nhưng không vượt trần (ngoài các ngoại lệ trên).

### Trang vượt trần trước khi sửa (số âm tiết trước → sau)

Số "sau" là số đo hiện tại (sau rà lại vòng 2).

| Trang cũ | Trước | Quyết định | Trang mới và số âm tiết sau |
|---|---:|---|---|
| A03 | 76 | tách | A01b 45; A01c 45; A03 74 (ngoại lệ); A03b 57 |
| B05 | 78 | tách | B05 49; B05b 59 |
| C01 | 83 | tách | C01 57; giá trị nhìn trước chuyển sang C03 49 |
| C04 | 84 | tách | C04 60; C04b 51 |
| D03 | 70 | sửa | D03 60 |
| D05 | 76 | sửa | D05 67 (ngoại lệ); phần đánh giá gần đúng chuyển sang D06 |
| E01 | 123 | tách | E01 45; E01b 55 |
| E04 | 71 | sửa | E04 59 |
| E06 | 65 | tách | E06 55; E06b 17 |
| F01 | 103 | sửa | F01 56 |
| F03 | 98 | tách | F03 60; F03b 60 |
| F06 | 74 | tách | F06 58; F06b 50 |
| G01 | 72 | sửa | G01 74; G01b 80 (trần 80) |
| G02 | 93 | tách | G02 45; G02b 77 (trần 80) |
| G05 | 100 | sửa | G05 63 (sau đồng bộ tệp bài tập 2026-10-14; ngoại lệ trần 80) |

Các trang cũ vượt về số dòng, dòng dài hoặc số khung (A02, A04, B01–B03, B07, B08, C05, C06, D01, D02, D06, E02, E08, F02, F04, F05, G04) đều đã đưa về ≤ 6 dòng, ≤ 20 âm tiết mỗi dòng, ≤ 3 công thức hiển thị và ≤ 1 khung; không dùng CSS thu chữ.

## Quyết định theo từng trang

Cột "Quyết định" so với deck trước đợt sửa (45 trang). Mã trang cũ được giữ khi nội dung còn; trang tách và trang lời giải nhận hậu tố `b`, `c`; trang tiêu đề mạch nhận mã `<tiền tố>00`. Thứ tự trình chiếu không theo thứ tự chữ cái của mã (ví dụ B06 đứng trước B05) vì thứ tự khái niệm theo ghi chú bài giảng.

### Mạch 1. Mở đầu

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-A01 | Giải MDP bằng quy hoạch động | Bìa, điểm vào mạch 1; câu luận đề nêu kết quả trung tâm | — → A01b | toàn bài | sửa: thêm luận đề, thuật ngữ gốc MDP, bỏ hộp nhiệm vụ |
| L04-A01b | Tiên quyết và quy ước | Nhắc lại MDP, lợi tức, chính sách Markov dừng, Bellman kỳ vọng | A01 → A01c | MT1–MT5 | thêm (tách từ A03 cũ và ghi chú của nó) |
| L04-A01c | Tiên quyết và quy ước | Ký hiệu miền, $P_\pi$, $r_\pi$, chỉ số, kỳ vọng | A01b → A02 | MT1–MT5 | thêm (vòng biên tập: tách để giữ trần khi thêm $P_\pi$, $r_\pi$ và chính sách Markov dừng) |
| L04-A02 | Mục tiêu học tập | Năm mục tiêu, mỗi mục tiêu một bài tập | A01c → A02b | MT1–MT5 | tách từ A02 cũ; ngoại lệ trần 80 |
| L04-A02b | Nội dung | Bảy mạch đánh số khớp `#/N` và trang tiêu đề mạch | A02 → A03 | — | thêm; ngoại lệ 7 dòng |
| L04-A03 | Vấn đề trung tâm | Bài toán một dòng và câu trả lời có điều kiện của mạch 2–6, hình lộ trình | A02b → A03b | toàn bài | sửa (tách từ A03 cũ) |
| L04-A03b | Cấu trúc một phép cập nhật quy hoạch động | Khung chung bốn thành phần của mọi thuật toán | A03 → A04 | MT5 | thêm (kế hoạch A2) |
| L04-A04 | Ví dụ: mô hình hai trạng thái | Ví dụ xuyên suốt; làm cụ thể vấn đề A03 | A03b → A05 | MT1 | sửa: tiêu đề, tên chữ đứng, gom dữ kiện |
| L04-A05 | Bài tập: lợi tức của chính sách ban đầu | Kiểm lợi tức và vai trò của mô hình; lời giải fragment | A04 → B00 | đầu vào | sửa: "Bài tập:", lời giải trên mặt trang |

### Mạch 2. Đánh giá chính sách

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-B00 | 2. Đánh giá chính sách | Điểm vào mạch 2; dòng dẫn nêu nhu cầu so sánh hành động; ngoài hành trình khái niệm | A05 → B01 | MT1 | thêm |
| L04-B01 | Giá trị dài hạn của chính sách cố định | Bước vấn đề và trực giác của KN1: tổng vô hạn, thay đuôi bằng bảng | B00 → B02 | MT1 | sửa: tiêu đề khác tên mạch, "Nhu cầu:", "Trực quan." |
| L04-B02 | Ví dụ: mô hình hai trạng thái, hai lượt quét | Tính tay trước giả mã; bảng cố định "Lượt quét \| $V_k(\mathrm s_0)$ \| $V_k(\mathrm s_1)$" | B01 → B03 | MT1 | sửa |
| L04-B03 | Phương trình Bellman kỳ vọng | Nhắc lại kết quả Bài 03, nối với quy tắc lượt quét | B02 → B04 | MT1 | sửa: "Nhắc lại:", hai khối công thức |
| L04-B04 | Toán tử Bellman đánh giá | Định nghĩa 04.1, lượt quét đồng bộ, điểm bất động, mục tiêu bootstrap | B03 → B06 | MT1 | sửa |
| L04-B06 | Tính co của toán tử đánh giá | Nhu cầu hội tụ, chuẩn vô cùng, ví dụ hai bảng, Mệnh đề 04.4 | B04 → B06c | MT1 | tách từ B06 cũ |
| L04-B06c | Hội tụ của đánh giá chính sách | Hệ quả 04.6: nghiệm duy nhất, tốc độ $\gamma^k$ | B06 → B07 | MT1 | thêm (tách từ B06 cũ; theo thứ tự ghi chú) |
| L04-B07 | Ví dụ: mô hình hai trạng thái, giá trị chính xác | Ứng dụng KN1: $(10,11)$, sai số $10\cdot0{,}9^k$ | B06c → B05 | MT1 | sửa |
| L04-B05 | Phần dư Bellman | Nhu cầu đại lượng dừng tính được; Định nghĩa 04.7; ví dụ $V_1$ | B07 → B06b | MT1 | tách từ B05 cũ |
| L04-B06b | Chặn sai số theo phần dư | Hệ quả 04.8, ngưỡng $\theta=(1-\gamma)\kappa$ | B05 → B05b | MT1 | tách từ B06 cũ |
| L04-B05b | Thuật toán đánh giá chính sách đồng bộ | Thuật toán 04.9 đủ đầu vào, đầu ra, khởi tạo, dừng | B06b → B08 | MT1 | tách từ B05 cũ |
| L04-B08 | Bài tập: lượt quét thứ ba và chặn sai số | Kiểm KN1 (Bài tập 04.1) | B05b → B08b | MT1 | tách từ B08 cũ |
| L04-B08b | Bài tập: lượt quét thứ ba và chặn sai số | Lời giải trên mặt trang | B08 → C00 | MT1 | thêm |

### Mạch 3. Cải thiện chính sách

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-C00 | 3. Cải thiện chính sách | Điểm vào mạch 3; dòng dẫn là bước vấn đề của KN2 | B08b → C01 | MT2 | thêm |
| L04-C01 | Phép đổi hành động tại một trạng thái | Vấn đề và trực giác của KN2 trên $\mathrm s_1$; thuật ngữ điều khiển | C00 → C02 | MT2 | tách từ C01 cũ (công thức chuyển sang C03) |
| L04-C02 | Ví dụ: hai nhánh hành động | Ví dụ 04.8: 11 và 12,9 | C01 → C03 | MT2 | sửa: bảng "Nhánh \| Thưởng \| Tiếp nối \| Nhìn trước" |
| L04-C03 | Giá trị nhìn trước một bước | Định nghĩa 04.11; nhắc lại $q_\pi$ | C02 → C04 | MT2 | sửa |
| L04-C04 | Chính sách tham lam | Định nghĩa 04.12 với quy tắc phá hòa | C03 → C04b | MT2 | tách từ C04 cũ |
| L04-C04b | Định lý cải thiện chính sách | Định lý 04.13 với giả thiết trên mặt trang | C04 → C05 | MT2 | tách từ C04 cũ |
| L04-C05 | Chứng minh: định lý cải thiện chính sách | Bốn bước: xác định, đơn điệu, lặp, giới hạn | C04b → C06 | MT2 | sửa |
| L04-C06 | Ví dụ: mô hình hai trạng thái, lần cải thiện thứ nhất | Ứng dụng KN2: $\pi_1$, $(10,30)$ | C05 → C07 | MT2 | sửa |
| L04-C07 | Bài tập: lần cải thiện thứ hai | Kiểm KN2 (Bài tập 04.2) | C06 → C07b | MT2 | tách từ C07 cũ |
| L04-C07b | Bài tập: lần cải thiện thứ hai | Lời giải trên mặt trang; cho $(\mathrm b,\mathrm b)$ dùng ở mạch 4 | C07 → D00 | MT2 | thêm |

### Mạch 4. Lặp chính sách

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-D00 | 4. Lặp chính sách | Điểm vào mạch 4; dòng dẫn là bước vấn đề của KN3 | C07b → D01 | MT3 | thêm |
| L04-D01 | Đánh giá lại sau mỗi lần cải thiện | Vấn đề, trực giác KN3; hình chu trình; thuật ngữ | D00 → D02 | MT3 | sửa: tiêu đề khác tên mạch, "Nhu cầu:" |
| L04-D02 | Ví dụ: mô hình hai trạng thái, ba vòng lặp chính sách | Tính tay ba vòng trước giả mã | D01 → D02b | MT3 | tách từ D02 cũ |
| L04-D02b | Chính sách ổn định | Định nghĩa 04.16 và kiểm tra bốn giá trị $q_{\pi_2}$ | D02 → D03 | MT3 | tách từ D02 cũ |
| L04-D03 | Thuật toán lặp chính sách | Thuật toán 04.17 | D02b → D05 | MT3 | sửa |
| L04-D04 | Giá trị tối ưu | Nhu cầu so với mọi chính sách, bốn giá trị, Định nghĩa 04.19 | D05 → D04b | MT3 | tách từ D04 cũ; bước vấn đề đã báo trước ở A03 |
| L04-D04b | Phương trình Bellman tối ưu | Định lý 04.20, "Ý nghĩa:", "Lưu ý:" dẫn sang định lý tồn tại; chứng minh và ví dụ $(27,30)$ trong ghi chú diễn giả | D04 → D06 | MT3 | tách từ D04 cũ (vòng biên tập: dòng chứng minh và ví dụ chuyển vào ghi chú để giữ trần) |
| L04-D05 | Dừng hữu hạn của lặp chính sách | Mệnh đề 04.18; đặt ngay sau D03 theo thứ tự ghi chú Mục 3.2 | D03 → D04 | MT3 | sửa (phần đánh giá gần đúng chuyển sang D06; vòng biên tập dời lên sau D03) |
| L04-D06 | Bài tập: kết luận dừng từ bảng gần đúng | Kiểm KN3 (Bài tập 04.3) | D04b → D06b | MT3 | tách từ D06 cũ |
| L04-D06b | Bài tập: kết luận dừng từ bảng gần đúng | Lời giải trên mặt trang | D06 → E00 | MT3 | thêm |

### Mạch 5. Lặp giá trị

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-E00 | 5. Lặp giá trị | Điểm vào mạch 5; dòng dẫn nêu giới hạn của lặp chính sách | D06b → E01 | MT4 | thêm |
| L04-E01 | Chi phí của đánh giá đầy đủ | Vấn đề KN4: 44 lượt quét, $O(n^3)$, tham lam đúng sớm | E00 → E01b | MT4 | tách từ E01 cũ |
| L04-E01b | Ý tưởng lặp giá trị | Trực giác KN4 và thuật ngữ | E01 → E02 | MT4 | tách từ E01 cũ |
| L04-E02 | Ví dụ: mô hình hai trạng thái, hai lượt quét lặp giá trị | Tính tay trước giả mã | E01b → E03 | MT4 | sửa |
| L04-E03 | Toán tử Bellman tối ưu | Định nghĩa 04.22, phần dư tối ưu | E02 → E03b | MT4 | sửa |
| L04-E03b | Tính co của toán tử tối ưu | Mệnh đề 04.24 với ví dụ đạt dấu bằng | E03 → E05b | MT4 | thêm (tách từ E05 cũ) |
| L04-E05b | Tồn tại chính sách tối ưu | Định lý 04.25: $v_*$ là điểm bất động, tối ưu trên mọi chính sách; Hệ quả; dạng $q_*$ | E03b → E05c | MT4 | thêm (deck cũ chỉ nêu trong ghi chú diễn giả; ghi chú bài giảng có Định lý 04.25) |
| L04-E05c | Chứng minh: tồn tại chính sách tối ưu | Bốn bước: Banach, tham lam đạt, Markov chặn chính sách nhớ lịch sử, qua giới hạn; có thể bỏ khi thiếu giờ | E05b → E05 | MT4 | thêm (vòng biên tập, theo PB) |
| L04-E05 | Hội tụ của lặp giá trị | Hệ quả 04.26 với hình `dp04-convergence-bound.svg` (chữ hình đã phóng) | E05c → E07 | MT4 | sửa |
| L04-E07 | Chặn sai số theo phần dư tối ưu | Hệ quả 04.27, ngưỡng, ví dụ $V_1$, $V_{55}$ | E05 → E04 | MT4 | sửa (đưa lên trước dãy năm ô) |
| L04-E04 | Thuật toán lặp giá trị đồng bộ | Thuật toán 04.28 | E07 → E06 | MT4 | sửa |
| L04-E06 | Ví dụ: dãy năm ô | Dữ kiện ví dụ thứ hai có trạng thái kết thúc | E04 → E06b | MT4 | tách từ E06 cũ |
| L04-E06b | Ví dụ: dãy năm ô, bốn lượt quét | Ứng dụng KN4 | E06 → E06c | MT4 | tách từ E06 cũ |
| L04-E06c | Ví dụ: dãy năm ô trơn trượt | Kỳ vọng theo $p$ với ba kết quả chuyển tại $\mathrm c_4$ (7,8 và 0,1) | E06b → E08 | MT4 | thêm (chuyển phần đầu của G03 cũ, theo RL, PB, MACH) |
| L04-E08 | Bài tập: điểm bất động trên dãy năm ô | Kiểm KN4 (Bài tập 04.4) | E06c → E08b | MT4 | tách từ E08 cũ |
| L04-E08b | Bài tập: điểm bất động trên dãy năm ô | Lời giải trên mặt trang | E08 → F00 | MT4 | thêm |

### Mạch 6. Lịch cập nhật và giới hạn của mô hình bảng

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-F00 | 6. Lịch cập nhật và giới hạn của mô hình bảng | Điểm vào mạch 6 | E08b → F01 | MT5 | thêm |
| L04-F01 | Chi phí một lượt quét | Vấn đề KN5: Nhận xét 04.30 với số liệu CartPole | F00 → F02 | MT5 | sửa |
| L04-F02 | Ví dụ: cập nhật tại chỗ | Nhu cầu, định nghĩa bằng lời và tính tay trên hai mô hình | F01 → F03 | MT5 | sửa |
| L04-F03 | Thuật toán lặp giá trị bất đồng bộ | Thuật toán 04.31 | F02 → F03b | MT5 | tách từ F03 cũ |
| L04-F03b | Hội tụ của quy hoạch động bất đồng bộ | Định lý 04.32 với giả thiết vô hạn lần trên mặt trang | F03 → F04 | MT5 | tách từ F03 cũ |
| L04-F04 | Lặp chính sách tổng quát | Định nghĩa 04.34, bảng mức hoàn tất đánh giá | F03b → F05 | MT5 | sửa |
| L04-F05 | Ví dụ: CartPole rời rạc hóa | 324 ô, $\hat p$, hai lượt quét tại ô 71 | F04 → F05b | MT5 | sửa: thêm số liệu notebook (Ví dụ 04.18) |
| L04-F05b | Chính sách tối ưu của CartPole rời rạc hóa | Ứng dụng: Tình huống 04.1–04.2, khoảng cách giữa MDP ước lượng và môi trường | F05 → F06 | MT5 | thêm (sai lệch so với A3, ghi trong review-log) |
| L04-F06 | Bài tập: lịch bỏ sót một trạng thái | Kiểm KN5 (Bài tập 04.5) | F05b → F06b | MT5 | tách từ F06 cũ (câu CartPole chuyển sang G07) |
| L04-F06b | Bài tập: lịch bỏ sót một trạng thái | Lời giải trên mặt trang | F06 → G00 | MT5 | thêm |

### Mạch 7. Tổng kết và chuyển tiếp

| Mã | Tiêu đề | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định |
|---|---|---|---|---|---|
| L04-G00 | 7. Tổng kết và chuyển tiếp | Điểm vào mạch 7 | F06b → G01 | toàn bài | thêm |
| L04-G01 | Tổng kết | Bảng `Kết quả \| Giả thiết không được bỏ \| Công thức hoặc thuật toán`, ba hàng đầu | G00 → G01b | MT1–MT2 | sửa (thay G01 cũ) |
| L04-G01b | Tổng kết | Bốn hàng sau của bảng tổng kết (Mệnh đề 04.18, Định lý 04.25, Hệ quả 04.27, Định lý 04.32) | G01 → G02 | MT3–MT5 | thêm (tách để giữ ≤ 6 dòng) |
| L04-G02 | So sánh các phương pháp quy hoạch động | Bảng `Phương pháp \| Quy tắc cập nhật \| Dữ liệu dùng \| Điều kiện dừng` | G01b → G02b | MT3–MT5 | sửa |
| L04-G02b | Hội tụ của các phương pháp quy hoạch động | Bảng `Phương pháp \| Giả thiết không được bỏ \| Kết luận` | G02 → G04 | MT3–MT5 | tách từ G02 cũ |
| L04-G04 | Bài tập: chứng nhận nghiệm tối ưu | Bài tập tổng hợp (Bài tập 04.6) | G02b → G04b | MT3–MT5 | tách từ G04 cũ (câu 3 cũ chuyển sang G07) |
| L04-G04b | Bài tập: chứng nhận nghiệm tối ưu | Lời giải trên mặt trang | G04 → G06 | MT3–MT5 | thêm |
| L04-G06 | Trả lời vấn đề trung tâm | Kết luận có điều kiện và dòng "Nguồn:" | G04b → G07 | toàn bài | thêm |
| L04-G07 | Câu hỏi tự kiểm tra | Bốn câu, mỗi câu kiểm một giả thiết hoặc phân biệt | G06 → G05 | toàn bài | thêm |
| L04-G05 | Bài tập về nhà và tài liệu đọc | Bảng `Mạch \| Bài tập` theo `exercises.md`: hàng "Tệp bài tập" (mạch 1: 04.16; 2: 04.1, 04.10; 3: 04.2, 04.17; 4: 04.3, 04.12; 5: 04.4, 04.11, 04.13; 6: 04.5, 04.14, 04.15; 7: 04.6) và hàng "Chỉ trong ghi chú" (mạch 5: 04.7, 04.8; 6: 04.9); tài liệu đọc; liên kết viewer "Ghi chú bài giảng · Bài tập"; dòng nối Bài 05; 63 âm tiết (trần 80) | G07 → — | toàn bài | sửa (2026-10-14: đồng bộ với `exercises.md`) |

Bài tập có lời giải trên mặt trang: A05 (fragment), B08b, C07b, D06b, E08b, F06b, G04b. G03 (bài tự làm) đã bỏ khỏi deck trong vòng biên tập: phần đầu thành ví dụ E06c, phần còn lại thành Bài tập 04.13 của tệp bài tập.
