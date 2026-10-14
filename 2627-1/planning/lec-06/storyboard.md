# Storyboard Bài 06: Điều khiển phi mô hình

Ngày lập lại: 2026-10-12, đợt sửa theo chuẩn 2026-10-12 (giai đoạn II); cập nhật cùng ngày sau vòng biên tập theo năm báo cáo rà soát (mục "Sửa sau rà soát năm vai" cuối tệp). Bản này thay storyboard ngày 29-09-2026 và khớp deck `lecture-06-dieu-khien-phi-mo-hinh.html` hiện tại: 75 trang, 7 mạch, 120 phút. Dàn bài, thuật ngữ và ánh xạ 30 trang nguồn ở [outline.md](outline.md); nhật ký ở [review-log.md](review-log.md). Số hiệu kết quả, ví dụ và bài tập theo ghi chú bài giảng đã commit `19323ad`. Mã trang chỉ dùng trong tệp quy trình.

Quy ước đếm mật độ: âm tiết đếm bằng `density.py` (từ tách theo khoảng trắng, bỏ tiêu đề, KaTeX, ghi chú diễn giả; nhãn và chữ trong bảng có tính). Script đếm mỗi hàng bảng là một dòng; theo `AGENTS.md`, một bảng dữ kiện được tính là một khối hiển thị, nên cột "dòng thực" dưới đây đếm bảng là một dòng.

## Bản đồ mạch

| N | Mạch, loại | Trang tiêu đề mạch | Chức năng riêng | Đầu vào từ mạch trước | Đầu ra cho mạch sau | Đóng góp cho vấn đề trung tâm | Trang | Phút |
|---|---|---|---|---|---|---|---:|---:|
| 1 | Mở đầu | A01 (bìa, không thêm trang "Mở đầu") | Nêu bài toán tại D, nhắc lại Bài 03–05, mục tiêu, nội dung, khung cập nhật chung | $q_\pi$, cải thiện tham lam, Monte Carlo, TD(0) | Nhu cầu ước lượng từng cặp và khung $Q\leftarrow Q+\alpha[Y-Q]$ | Đặt bài toán và câu trả lời có điều kiện | 6 | 8 |
| 2 | Phát triển kiến thức (khái niệm) | B00, `mach-2` | Bảng $Q$, chính sách $\varepsilon$-tham lam, cải thiện trong lớp $\varepsilon$-mềm | Bài toán tại D | Quy tắc chọn hành động có thăm dò; Mệnh đề 06.6 cần $q_\pi$ chính xác | Đối tượng cần học và cách thử mọi hành động | 13 | 21 |
| 3 | Phát triển kiến thức (thuật toán) | C00, `mach-3` | Thay $q_\pi$ bằng trung bình lợi tức theo lần ghé đầu tiên; Thuật toán 06.9 | Nhu cầu đo $q_\pi$ từ mẫu | Giới hạn: mọi cập nhật chờ lượt kết thúc | Câu trả lời khi có lượt kết thúc | 11 | 18 |
| 4 | Phát triển kiến thức (thuật toán) | D00, `mach-4` | Mục tiêu một bước theo hành động kế tiếp; Thuật toán 06.12; ba sự kiện dừng | Giới hạn chờ lượt; TD(0) | Mục tiêu Sarsa phụ thuộc hành động thăm dò | Câu trả lời khi lượt chưa kết thúc | 11 | 18 |
| 5 | Phát triển kiến thức (khái niệm và thuật toán) | E00, `mach-5` | Hành vi và đích; mục tiêu cực đại; Thuật toán 06.16; tàu đổ bộ | Mục tiêu Sarsa phụ thuộc thăm dò | Hai bảng sau hữu hạn mẫu, chưa có bảo đảm | Câu trả lời khi dữ liệu từ chính sách còn thăm dò, mục tiêu theo chính sách tham lam | 12 | 19,5 |
| 6 | Phát triển kiến thức và áp dụng | F00, `mach-6` | GLIE, Robbins–Monro theo cặp, Định lý 06.21–06.22, vai trò giả thiết | Bảng hữu hạn mẫu | Danh sách giả thiết để kiểm bài toán thực; điều khiển Monte Carlo không có định lý tương ứng (F08) | Điều kiện để $Q_t\to q_*$ | 12 | 19,5 |
| 7 | Kết luận | G00, `mach-7` | Bảng tổng kết, khung chung, bảng hội tụ, bài tập tổng hợp, trả lời vấn đề trung tâm | Toàn bài | Bài tập về nhà, Bài 07 | Kết luận có điều kiện tại D | 10 | 16 |

Tổng: 75 trang, 120 phút. Bảy mạch nằm trong khoảng 5–7.

## Cụm khái niệm và sáu bước

| Cụm; dạng; tiên quyết | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Dữ kiện truyền, bước gộp, câu nối | Phút |
|---|---|---|---|---|---|---|---|---:|
| Bảng $Q$ và $q_\pi$; khái niệm; $q_\pi$ Bài 03 | B00 (dòng dẫn), A05 (nhu cầu + ví dụ dẫn nhập $(\mathrm D,1,10,\mathrm E)$ làm cụ thể vấn đề "so sánh hai hành động từ mẫu") | B08 (hành động đầu cố định, tiếp nối theo $\pi_L$) | B01, B08 | B02 (Nhắc lại $q_\pi$, Định nghĩa 06.1, nhắc lại $q_*$) | B03 (ô $(\mathrm D,0)$ không nhận mẫu) | A05 (lời giải fragment), B07/B10 câu 3 | $q_{\pi_L}(\mathrm D,0)=998$ truyền từ B08 sang B02. Trực giác và ví dụ gộp ở B08. Năng lực: nhận diện thông tin trong mẫu, phân biệt $q_\pi$ với $Q$ | 8 |
| Chính sách $\varepsilon$-tham lam; khái niệm | B03 (nhu cầu thăm dò) | B04 (hai nhánh thăm dò/khai thác) | B04 | B05 (Định nghĩa 06.3, 06.4) | ghi chú diễn giả B05 (hàng bốn hành động của tàu đổ bộ); C04 | B07/B10 câu 1–2 | Hàng D $(0;1)$, $\varepsilon=\tfrac14$ truyền sang B05 | 5 |
| Cải thiện $\varepsilon$-tham lam; khái niệm (kết quả); định lý cải thiện Bài 04 | B11 (nhu cầu) | B11 (Trực quan: phần sàn chung) | B11 (một trạng thái, ba hành động) | B06 (Mệnh đề 06.6), B09 (chứng minh) | C06 (bước 1 của lượt sau là bước cải thiện) | B07/B10 câu 4 | Phút tăng 1 cho chứng minh B09. Ví dụ dẫn nhập đứng trước trực giác trên cùng trang; $q_\pi=(3;3;-1)$ dùng tiếp trong ghi chú diễn giả B06 cho phản ví dụ | 6 |
| Điều khiển Monte Carlo; thuật toán; Monte Carlo dự đoán Bài 05 | C00, C01 | C01 | C02 (tính tay một lượt), C04–C07 (tính tay lượt thăm dò) | C03 (Định nghĩa 06.8), C05–C06 (Thuật toán 06.9) | C10 (tàu đổ bộ: lượt bị cắt) | C08/C09 | Bước ví dụ của ý "lần ghé đầu tiên theo cặp" (một ô, hai hành động là hai cặp) gộp vào bài tập C08/C09; ghi chú diễn giả C03 nêu lượt D, C, D, C. Tính tay trước giả mã; $N(\mathrm D,1)=1$ và $998,999,1000$ truyền sang C06 (ghi chú diễn giả lần theo thuật toán) | 18 |
| Sarsa; thuật toán; TD(0) Bài 05 | D00, D01 | D01 | D02–D03 (hai bước đầu) | D04 (Định nghĩa 06.11), D05, D10 (Thuật toán 06.12) | D07 (mẫu vào trạng thái kết thúc, mẫu 5), D06 (ba sự kiện, tàu đổ bộ) | D08/D11 | Mẫu 2 truyền sang D04 và D10; mẫu 5 ($-1{,}28$) sang E06, G02 | 18 |
| Hành vi và đích; khái niệm | E00, E01 | E01 (hai vai) | E01 (mẫu 2) | E09 (Định nghĩa 06.14) | E07 (dữ liệu hành vi; một dòng về tỉ số $\rho$ của dự đoán TD(0) khác chính sách làm nhu cầu cho nhận xét) | E12 câu 3; G08 câu 4 | Ví dụ dẫn nhập mẫu 2 đặt cùng vấn đề | 4 |
| Q-learning; thuật toán | E01 | E02 (nhánh cực đại trên hình) | E02 (mẫu 1–2) | E03 (Định nghĩa 06.15), E04, E10 (Thuật toán 06.16) | E06 (so với Sarsa trên năm mẫu), E11 (tàu đổ bộ) | E08/E12 | Bảng nghiêng phải dùng cho cả hai lần chạy để mọi khác biệt đến từ mục tiêu; E11 đứng sát E08 vì cùng so hai mục tiêu trên một chuyển | 15,5 |
| GLIE; khái niệm | F12 (nhu cầu, $\gamma=0{,}9$) | F10 | F06 | F02 (Định nghĩa 06.18) | F08, F13 | F05/F09 câu b | Lịch $0{,}25$, $1/k$, $1/k^2$ truyền từ F06 sang ghi chú diễn giả F02 | 5 |
| Robbins–Monro theo cặp; khái niệm; Robbins–Monro theo trạng thái Bài 05 | F12 | F10, F03 (Ý nghĩa) | F07 | F03 (Định nghĩa 06.19) | F04, F08, F13 | F05/F09 câu c | Ví dụ đặt trước định nghĩa | 3 |
| Định lý hội tụ; kết quả | F12 | F10 (xấp xỉ ngẫu nhiên của toán tử co) | F12 (bỏ độ phủ) | F04, F08 (Định lý 06.21, 06.22) | F13, G03/G07 (tàu đổ bộ) | F05/F09, G08 | Chứng minh nằm ngoài phạm vi, dẫn nguồn trong ghi chú diễn giả; hàng $\gamma<1$ của F13 nêu hệ quả (toán tử không còn co), không phải phản ví dụ | 6,5 |

Mạch mở đầu và mạch kết luận nằm ngoài hành trình khái niệm (trừ A05, thuộc cụm đầu của mạch 2). Không có bước nào ghi `không áp dụng`; các bước gộp được ghi trong bảng.

## Trang tiêu đề mạch

| Mã, `id` | Vị trí | Tên mạch / dòng dẫn (âm tiết) | Từ khóa | Ghi chú diễn giả: kế thừa → nhiệm vụ → đầu ra | Bước hành trình | Quyết định |
|---|---|---|---|---|---|---|
| B00, `mach-2` | điểm vào mạch 2 (#/2/1) | Giá trị hành động và thăm dò / "Muốn so sánh hai hành động tại D khi thiếu mô hình, phải ước lượng giá trị từng cặp và thử cả hai." (23) | Bảng giá trị hành động · Thăm dò · Chính sách ε-tham lam · Cải thiện chính sách | $q_\pi$, định lý cải thiện → lập bảng theo cặp, thăm dò, cải thiện ε-tham lam → bảng $Q$ và quy tắc chọn hành động | `vấn đề` của cụm bảng $Q$ | thêm |
| C00, `mach-3` | điểm vào mạch 3 (#/3/1) | Điều khiển Monte Carlo / "Muốn ước lượng giá trị cặp từ lượt hoàn chỉnh, phải gắn lợi tức với lần ghé đầu tiên của cặp." (21) | Lần ghé đầu tiên · Bộ đếm lợi tức · Trung bình gia tăng · Chính sách cố định trong lượt | Mệnh đề 06.6 cần $q_\pi$ → trung bình lợi tức theo cặp → Thuật toán 06.9 và giới hạn chờ lượt | `vấn đề` của cụm Monte Carlo | thêm |
| D00, `mach-4` | điểm vào mạch 4 (#/4/1) | Sarsa và mục tiêu một bước / "Muốn cập nhật trước khi lượt kết thúc, phải thay lợi tức chưa quan sát bằng giá trị của hành động kế tiếp." (23) | Mục tiêu một bước · Bộ năm của mẫu chuyển · Trạng thái kết thúc · Ngân sách cập nhật | giới hạn chờ lượt, TD(0) → mục tiêu một bước → Sarsa và phụ thuộc vào hành động thăm dò | `vấn đề` của cụm Sarsa | thêm |
| E00, `mach-5` | điểm vào mạch 5 (#/5/1) | Q-learning và học khác chính sách / "Muốn học giá trị chính sách tham lam từ dữ liệu còn thăm dò, phải dùng cực đại của hàng kế tiếp." (22) | Mục tiêu cực đại · Học khác chính sách · Bộ bốn của mẫu chuyển · Dữ liệu hành vi | mục tiêu Sarsa phụ thuộc thăm dò → tách hành vi và đích, mục tiêu cực đại → Q-learning, câu hỏi hội tụ | `vấn đề` của cụm hành vi–đích và Q-learning | thêm |
| F00, `mach-6` | điểm vào mạch 6 (#/6/1) | Điều kiện hội tụ / "Muốn bảng hội tụ tới giá trị hành động tối ưu, phải kiểm độ phủ, lịch thăm dò và lịch bước học." (21, không KaTeX) | Độ phủ · Tham lam trong giới hạn · Robbins–Monro theo cặp · Hội tụ hầu chắc chắn | hội tụ TD(0) Bài 05, bảng hữu hạn mẫu → điều kiện thăm dò, bước học, hai định lý → danh sách giả thiết cho tàu đổ bộ | `vấn đề` của cụm GLIE, Robbins–Monro, định lý | thêm |
| G00, `mach-7` | điểm vào mạch 7 (#/7/1) | Tổng kết và chuyển tiếp / "Muốn trả lời bài toán tại D, phải đối chiếu dữ liệu, mục tiêu cập nhật và giả thiết hội tụ." (21) | Giả thiết không được bỏ · Khung cập nhật chung · Bài toán tàu đổ bộ · Xấp xỉ hàm | sản phẩm của bài → tổng kết, áp dụng, trả lời vấn đề trung tâm → Bài 07 | ngoài hành trình khái niệm | thêm |

Tên mạch khác tiêu đề trang nội dung đầu tiên của mạch (A05, C01, D01, E01, F12, G05). Không có định nghĩa, công thức trung tâm, hình hay mã trên mặt trang tiêu đề mạch; dòng dẫn và từ khóa không chứa KaTeX (ε viết bằng ký tự thường ở B00). Dòng dẫn dài 20–23 âm tiết (giới hạn 25); script `density.py` gắn cờ dòng trên 20 âm tiết, đây là ngoại lệ theo quy định riêng của trang tiêu đề mạch.

## Từng trang

Cột "MT" là mục tiêu học tập; cột "Quyết định" ghi `giữ | sửa | gộp | tách | thêm | bỏ` so với deck 29-09-2026 và lý do. Mọi trang nội dung có ghi chú diễn giả 40–150 âm tiết (không tính dòng nguồn).

### Mạch 1. Mở đầu

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| A01 | #/1/1 | Bìa; luận đề nêu cơ chế trung tâm (ba phương pháp khác ở mục tiêu cập nhật) | — → A07 | tất cả | sửa: thêm luận đề, đơn vị theo quyết định chung §5, bỏ tên tác giả nguồn và liên kết trên bìa |
| A07 | #/1/2 | Nhắc lại $q_\pi$, $v_\pi$, cải thiện tham lam; ký hiệu dùng xuyên bài | A01 → A02 | MT1 | thêm (kế hoạch A2); nhận phần nhắc lại của A04 cũ |
| A02 | #/1/3 | Năm mục tiêu đánh giá được, trùng ghi chú | A07 → A08 | tất cả | tách: A02 cũ gộp mục tiêu và mục lục |
| A08 | #/1/4 | Nội dung bảy mạch, số và tên khớp trang tiêu đề mạch | A02 → A03 | — | thêm (tách từ A02 cũ) |
| A03 | #/1/5 | Vấn đề trung tâm và câu trả lời có điều kiện của mạch 2–6; hình dãy năm ô | A08 → A09 | tất cả | sửa: đổi từ "Chuỗi năm trạng thái"; thêm danh sách đánh số 2–6 |
| A09 | #/1/6 | Khung chung $Q\leftarrow Q+\alpha_t[Y_t-Q]$ trước mạch nội dung đầu | A03 → B00 | MT4 | thêm (kế hoạch A2) |
| A04 cũ | — | Nhắc lại dự đoán/điều khiển | — | — | bỏ (gộp): nhắc lại sang A07, phân biệt dự đoán/điều khiển sang ghi chú diễn giả B00, B03 |

### Mạch 2. Giá trị hành động và thăm dò

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| B00 | #/2/1 | Điểm vào mạch 2 | A09 → A05 | — | thêm |
| A05 | #/2/2 | Nhu cầu so sánh hai hành động từ mẫu; ví dụ dẫn nhập; lời giải fragment | B00 → B01 | MT1 | sửa, chuyển từ mạch mở đầu sang đầu mạch 2 (kế hoạch A3); trùng Bài tập 06.1 |
| B01 | #/2/3 | Ví dụ bảng khởi tạo: số khởi tạo chưa là quan sát | A05 → B08 | MT1 | sửa: tách câu vấn đề sang A05, tiêu đề "Ví dụ: …" |
| B08 | #/2/4 | Trực giác và ví dụ cho $q_\pi$: hành động đầu cố định | B01 → B02 | MT1 | thêm (kế hoạch A3) |
| B02 | #/2/5 | Nhắc lại $q_\pi$; Định nghĩa 06.1; nhắc lại $q_*$ | B08 → B03 | MT1 | sửa: chuyển thành nhắc lại, thêm nhãn |
| B03 | #/2/6 | Nhu cầu thăm dò; hình vòng điều khiển | B02 → B04 | MT2 | sửa: mở bằng "Nhu cầu:", tách khung thành hai câu |
| B04 | #/2/7 | Ví dụ xác suất tại D; nhầm lẫn $\varepsilon$ với xác suất hành động khác | B03 → B05 | MT2 | sửa: tiêu đề "Ví dụ:", bỏ hai card |
| B05 | #/2/8 | Định nghĩa 06.3, 06.4 | B04 → B11 | MT2 | sửa: thêm nhãn "Định nghĩa.", bỏ khung |
| B11 | #/2/9 | Nhu cầu, ví dụ một bước, trực quan phần sàn trước mệnh đề | B05 → B06 | MT2 | thêm (sai lệch kế hoạch: kế hoạch để phép kiểm số trong ghi chú diễn giả; ghi chú đã có Ví dụ 06.5) |
| B06 | #/2/10 | Mệnh đề 06.6 với giả thiết, kết luận, ý nghĩa | B11 → B09 | MT2 | tách: chứng minh sang B09 |
| B09 | #/2/11 | Chứng minh từng bước | B06 → B07 | MT2 | thêm |
| B07 | #/2/12 | Bài tập có lời giải mẫu (đề Bài tập 06.2) | B09 → B10 | MT1, MT2 | sửa: đổi số liệu sang Bài tập 06.2 của ghi chú ($\varepsilon=0{,}2$; hàng $(4;1;1)$) |
| B10 | #/2/13 | Lời giải trên mặt trang | B07 → C00 | MT1, MT2 | thêm |

### Mạch 3. Điều khiển Monte Carlo

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| C00 | #/3/1 | Điểm vào mạch 3 | B10 → C01 | — | thêm |
| C01 | #/3/2 | Nhu cầu đo $q_\pi$ từ lượt; nhắc lại Monte Carlo dự đoán; trực quan | C00 → C02 | MT3 | sửa: tiêu đề mới, bỏ chuỗi mũi tên và hình lặp |
| C02 | #/3/3 | Tính tay một lượt tham lam; bộ đếm từ 0 | C01 → C03 | MT3 | sửa: tiêu đề "Ví dụ:", bỏ hình vòng B–C (chuyển sang ghi chú diễn giả B02, F13) |
| C03 | #/3/4 | Định nghĩa 06.8; trung bình gia tăng | C02 → C04 | MT3 | sửa: nhắc lại Bài 05, nhãn định nghĩa |
| C04 | #/3/5 | Sinh lượt thăm dò bằng dãy số cho trước | C03 → C07 | MT2, MT3 | sửa: công thức đồng dư sang ghi chú diễn giả, bảng gọn |
| C07 | #/3/6 | Cập nhật lần ghé đầu tiên trên lượt D→C→B→A | C04 → C05 | MT3 | sửa: tiêu đề "Ví dụ:", bố cục hình–bảng |
| C05 | #/3/7 | Thuật toán 06.9: đầu vào, đầu ra, giả thiết, ngân sách | C07 → C06 | MT3, MT5 | sửa: nhãn "Thuật toán.", lịch $1/k$ sang ghi chú diễn giả |
| C06 | #/3/8 | Năm bước của thuật toán | C05 → C10 | MT3 | sửa: chi phí sang ghi chú diễn giả |
| C10 | #/3/9 | Ứng dụng: lượt bị cắt của tàu đổ bộ; Nhận xét 06.10 | C06 → C08 | MT3, MT5 | thêm (sai lệch kế hoạch: bước ứng dụng của cụm Monte Carlo còn yếu trong kế hoạch A4) |
| C08 | #/3/10 | Bài tập có lời giải mẫu (Bài tập 06.3) | C10 → C09 | MT3 | sửa: tiêu đề "Bài tập:" |
| C09 | #/3/11 | Lời giải trên mặt trang | C08 → D00 | MT3 | thêm |

### Mạch 4. Sarsa và mục tiêu một bước

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| D00 | #/4/1 | Điểm vào mạch 4 | C09 → D01 | — | thêm |
| D01 | #/4/2 | Nhu cầu cập nhật trước khi lượt kết thúc; nhắc lại TD(0); trực quan | D00 → D02 | MT4 | sửa: tiêu đề không dùng "Từ…sang…", bỏ hai card và khung |
| D02 | #/4/3 | Dữ kiện năm mẫu dùng chung | D01 → D03 | MT4 | sửa: bỏ bảng khởi tạo thứ hai và chú thích dài |
| D03 | #/4/4 | Tính tay mẫu 1–2 trước định nghĩa | D02 → D04 | MT4 | sửa: tiêu đề "Ví dụ:", hình và chuỗi `aligned` |
| D04 | #/4/5 | Định nghĩa 06.11; học theo chính sách | D03 → D05 | MT4 | sửa: nhãn "Định nghĩa." |
| D05 | #/4/6 | Thuật toán 06.12: đầu vào, đầu ra, giả thiết, khởi tạo, dừng | D04 → D10 | MT4 | tách (D05 cũ 91 âm tiết) |
| D10 | #/4/7 | Năm bước của Sarsa; thứ tự chọn $A'$ | D05 → D07 | MT4 | thêm (phần thứ hai của D05 cũ) |
| D07 | #/4/8 | Ứng dụng quy trình cho mẫu 3–5; trạng thái kết thúc | D10 → D06 | MT4 | sửa (sai lệch kế hoạch: thêm mẫu 5 vào ví dụ vì bài tập D08 dùng $\alpha=0{,}5$ theo ghi chú) |
| D06 | #/4/9 | Nhận xét 06.13: kết thúc lượt, cắt ngắn, hết ngân sách; tàu đổ bộ | D07 → D08 | MT4, MT5 | sửa (sai lệch kế hoạch: bước 4–6 của giả mã vào D10; trang này thành bảng ba sự kiện) |
| D08 | #/4/10 | Bài tập có lời giải mẫu (Bài tập 06.4) | D06 → D11 | MT4 | sửa: dùng $\alpha=0{,}5$ và bốn câu của ghi chú |
| D11 | #/4/11 | Lời giải trên mặt trang; đối chiếu $\alpha=0{,}8$ | D08 → E00 | MT4 | thêm |

### Mạch 5. Q-learning và học khác chính sách

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| E00 | #/5/1 | Điểm vào mạch 5 | D11 → E01 | — | thêm |
| E01 | #/5/2 | Nhu cầu học giá trị tham lam khi hành vi thăm dò; ví dụ mẫu 2; trực quan hai vai | E00 → E09 | MT4 | tách: định nghĩa sang E09 |
| E09 | #/5/3 | Định nghĩa 06.14; hình hai đường | E01 → E02 | MT4 | thêm (phần định nghĩa của E01 cũ) |
| E02 | #/5/4 | Tính tay mẫu 1–2 với mục tiêu cực đại | E09 → E03 | MT4 | sửa: tiêu đề "Ví dụ:", hình và `aligned` |
| E03 | #/5/5 | Định nghĩa 06.15; bộ bốn (điều kiện trùng mục tiêu chuyển vào ghi chú diễn giả) | E02 → E04 | MT4 | sửa: nhãn, công thức gọn |
| E04 | #/5/6 | Thuật toán 06.16: đầu vào, đầu ra, giả thiết, khởi tạo | E03 → E10 | MT4 | tách (E04 cũ 88 âm tiết) |
| E10 | #/5/7 | Bốn bước của Q-learning; chọn hành động sau cập nhật | E04 → E06 | MT4 | thêm (gộp bước của E04, E05 cũ) |
| E05 cũ | — | Kết thúc và chi phí của Q-learning | — | — | bỏ (gộp): bước vào E10, chi phí vào ghi chú diễn giả E04 (sai lệch kế hoạch: kế hoạch giữ E05) |
| E06 | #/5/8 | So sánh Sarsa và Q-learning trên năm mẫu | E10 → E07 | MT4 | sửa: bố cục bảng và chữ hai cột |
| E07 | #/5/9 | Tỉ số lấy mẫu quan trọng của dự đoán TD(0) khác chính sách; Nhận xét 06.17: Q-learning một bước không cần, vẫn cần độ phủ | E06 → E11 | MT4, MT5 | sửa: "Giả thiết:" thay nhãn ngoài danh sách, bỏ hình lặp |
| E11 | #/5/10 | Ứng dụng trên một chuyển của tàu đổ bộ (Ví dụ 06.13); đứng sát bài tập E08 vì cùng so hai mục tiêu trên một chuyển (thứ tự theo ghi chú: Nhận xét 06.17 trước Ví dụ 06.13) | E07 → E08 | MT4 | thêm (kế hoạch A3, khuyến nghị); dời sau E07 ở vòng biên tập |
| E08 | #/5/11 | Bài tập có lời giải mẫu (Bài tập 06.5) | E11 → E12 | MT4 | sửa: tiêu đề, thêm câu 3 của ghi chú |
| E12 | #/5/12 | Lời giải trên mặt trang | E08 → F00 | MT4 | thêm |

### Mạch 6. Điều kiện hội tụ

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| F00 | #/6/1 | Điểm vào mạch 6 | E12 → F12 | — | thêm |
| F12 | #/6/2 | Nhu cầu; ví dụ dẫn nhập $\gamma=0{,}9$: ô không được thử không tới $q_*$ | F00 → F10 | MT5 | thêm (sai lệch kế hoạch: theo đoạn mở Mục 5 của ghi chú, thay vai vấn đề của F01 cũ) |
| F10 | #/6/3 | Trực giác chung của hai định lý | F12 → F06 | MT5 | thêm (ghi chú Mục 5.1; kế hoạch A4 ghi thiếu trực giác) |
| F06 | #/6/4 | Ví dụ khối xác suất tham lam và số lần thử | F10 → F02 | MT5 | thêm (tách từ F02 cũ; thêm lịch $1/k^2$ theo Ví dụ 06.14) |
| F02 | #/6/5 | Định nghĩa 06.18 | F06 → F07 | MT5 | sửa: bỏ card, ví dụ sang F06 |
| F07 | #/6/6 | Ví dụ cặp được cập nhật thưa; nhắc lại Bài 05 | F02 → F03 | MT5 | thêm (tách từ F03 cũ) |
| F03 | #/6/7 | Định nghĩa 06.19 | F07 → F04 | MT5 | sửa: ví dụ sang F07, thêm "Ý nghĩa:" |
| F01 cũ | — | Giả thiết chung của các định lý | — | — | bỏ (gộp): giả thiết nền lên mặt F04, F08, G06; Nhận xét 06.20 và vị trí dãy năm ô vào ghi chú diễn giả F04 và F13 (sai lệch kế hoạch: kế hoạch giữ F01) |
| F04 | #/6/8 | Định lý 06.21 với giả thiết quyết định trên mặt trang | F03 → F08 | MT5 | tách (F04 cũ 99 âm tiết) |
| F08 | #/6/9 | Định lý 06.22; dòng trên mặt trang: điều khiển Monte Carlo trộn lợi tức nhiều $\pi_k$, chưa có định lý hội tụ tổng quát (nguồn trong ghi chú diễn giả) | F04 → F13 | MT5 | thêm |
| F13 | #/6/10 | Ứng dụng: vai trò của từng giả thiết qua năm phản ví dụ | F08 → F05 | MT5 | thêm (sai lệch kế hoạch: theo danh sách "Bỏ giả thiết" của ghi chú) |
| F05 | #/6/11 | Bài tập có lời giải mẫu (Bài tập 06.6) | F13 → F09 | MT5 | sửa: tiêu đề, giả thiết gọn |
| F09 | #/6/12 | Lời giải trên mặt trang | F05 → G00 | MT5 | thêm |

### Mạch 7. Tổng kết và chuyển tiếp

| Mã | Vị trí | Lý do tồn tại, nhu cầu được giải quyết | Trước → sau | MT | Quyết định |
|---|---|---|---|---|---|
| G00 | #/7/1 | Điểm vào mạch 7 | F09 → G05 | — | thêm |
| G05 | #/7/2 | "Kết quả về giá trị hành động và thăm dò": bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` cho ba khái niệm | G00 → G09 | tất cả | thêm |
| G09 | #/7/3 | "Kết quả về ba thuật toán": cùng bảng cho ba thuật toán | G05 → G01 | tất cả | thêm (tách G05 vì tràn khung 16:9; kế hoạch cho phép tách hai trang) |
| G01 | #/7/4 | Bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng` | G09 → G06 | MT4, MT5 | sửa: theo khuôn của AGENTS |
| G06 | #/7/5 | Bảng `Phương pháp | Giả thiết không được bỏ | Kết luận` | G01 → G03 | MT5 | thêm |
| G03 | #/7/6 | Bài tập tổng hợp trên tàu đổ bộ | G06 → G07 | MT3–MT5 | sửa: dữ kiện LunarLander theo kế hoạch A2 |
| G07 | #/7/7 | Lời giải trên mặt trang | G03 → G02 | MT3–MT5 | thêm |
| G02 | #/7/8 | Trả lời vấn đề trung tâm có điều kiện: nhắc lại bài toán tại D, bảng ba hàng D có cột khởi tạo (nghiêng trái/phải), dòng "Nguồn:" | G07 → G08 (câu nối ở cuối ghi chú G07 và đầu ghi chú G02) | tất cả | sửa |
| G08 | #/7/9 | Câu hỏi tự kiểm tra (lời giải trong ghi chú diễn giả) | G02 → G04 | MT1, MT4, MT5 | thêm |
| G04 | #/7/10 | Bài tập về nhà, tài liệu đọc, liên kết viewer ghi chú bài giảng và bài tập, nối sang Bài 07 | G08 → — | tất cả | sửa: bỏ liên kết tới PDF nguồn, bảng `Mạch | Bài tập`; 2026-10-14 đồng bộ với `exercises.md` |

## Bài tập trên trang chiếu

| Trang đề / lời giải | Bài tập trong ghi chú | Loại | Năng lực đo |
|---|---|---|---|
| A05 (fragment) | 06.1 | lời giải mẫu trên mặt trang | đọc thông tin của mẫu |
| B07 / B10 | 06.2 | lời giải mẫu trên mặt trang | tính phân phối, phân biệt $q_\pi$ và $Q$, điều kiện Mệnh đề 06.6 |
| C08 / C09 | 06.3 | lời giải mẫu trên mặt trang | lần ghé đầu tiên theo cặp, bộ đếm |
| D08 / D11 | 06.4 | lời giải mẫu trên mặt trang | cập nhật Sarsa, thứ tự chọn $A'$, ba sự kiện |
| E08 / E12 | 06.5 | lời giải mẫu trên mặt trang | so sánh hai mục tiêu |
| F05 / F09 | 06.6 | lời giải mẫu trên mặt trang | kiểm giả thiết hội tụ |
| G03 / G07 | Tình huống 06.1 của ghi chú; Bài tập 06.17 của `exercises.md` | bài tập tổng hợp, lời giải trên mặt trang | chọn phương pháp, kiểm giả thiết trên bài toán thực |
| G08 | — | tự làm; lời giải trong ghi chú diễn giả | bốn giả thiết hoặc phân biệt |

Khi `exercises.md` lặp các bài 06.1–06.6, lời giải phải trùng kết quả trên trang chiếu và dẫn tới cả trang đề và trang lời giải.

Bảng `Mạch | Bài tập` trên G04 (đồng bộ 2026-10-14) ghi số của `exercises.md` theo bảng mạch của tệp, rồi sau "ghi chú:" các bài chỉ có trong mục Bài tập củng cố của ghi chú: mạch 2: 06.1, 06.2, 06.14; ghi chú: 06.8, 06.11; mạch 3: 06.3, 06.13; mạch 4: 06.4, 06.15; mạch 5: 06.5, 06.13; ghi chú: 06.10; mạch 6: 06.6, 06.16; ghi chú: 06.9, 06.12; mạch 7: 06.17; ghi chú: 06.7 (06.7 phân loại ba thuật toán theo dữ liệu, hành vi và đích, khớp bảng G01). Bài tập 06.13 thuộc cả mạch 3 và mạch 5 vì so Monte Carlo với Q-learning trên cùng dãy sáu ô. Dòng "Tệp bài tập: chưa có" được thay bằng liên kết viewer `material-viewer.html?doc=materials/lec-06/exercises.md&deck=lecture-06-dieu-khien-phi-mo-hinh.html` cạnh liên kết ghi chú bài giảng.

## Mật độ: trang vượt trần trước khi sửa

Số đo trước lấy từ deck 29-09-2026 (bản sao `deck06-old.html` trong scratchpad của phiên), số đo sau lấy từ deck hiện tại, cùng `density.py`. Trước: 45 trang, 30 trang bị script gắn cờ, 21 trang trên 60 âm tiết, 3 trang trên 90 (D02, D05, F04: trên 1,5 lần trần). Sau: 75 trang, không trang nội dung nào trên 60 âm tiết; 4 trang trên 60 đều thuộc nhóm trần 80 (A02, F13, G06, G04).

| Mã cũ | Âm tiết / dòng trước | Quyết định | Trang mới: âm tiết / dòng sau |
|---|---|---|---|
| A02 | 74 / 11 | tách | A02: 73 / 5; A08: 34 / 7 |
| A04 | 73 / 10 | bỏ (gộp) | nhắc lại sang A07: 54 / 5; phân biệt dự đoán/điều khiển sang ghi chú diễn giả B00 |
| B01 | 90 / 10 | tách | A05: 54 / 5; B01: 52 / 8 |
| B03 | 47 / 2 | sửa | B03: 43 / 3 |
| B06 | 61 / 4 | tách | B06: 50 / 4; B09: 40 / 4 |
| B07 | 59 / 5 | tách | B07: 55 / 5; B10: 36 / 6 |
| C01 | 50 / 2 | sửa | C01: 58 / 5 |
| C04 | 63 / 9 | sửa | C04: 57 / 8 |
| C07 | 34 / 7 | sửa | C07: 34 / 6 |
| C05 | 86 / 5 | tách | C05: 56 / 5; C06: 51 / 6 |
| D01 | 62 / 6 | sửa | D01: 47 / 4 |
| D02 | 105 / 13 | sửa | D02: 42 / 8 |
| D04 | 36 / 2 | sửa | D04: 49 / 4 |
| D05 | 91 / 5 | tách | D05: 56 / 6; D10: 52 / 5 |
| D06 | 85 / 5 | sửa | bước 4–6 sang D10: 52 / 5; D06 thành bảng ba sự kiện: 59 / 6 (bảng so sánh) |
| D07 | 54 / 8 | sửa | D07: 50 / 5 |
| E01 | 66 / 3 | tách | E01: 57 / 5; E09: 48 / 4 |
| E04 | 88 / 5 | tách | E04: 50 / 5; E10: 47 / 5 |
| E05 | 69 / 7 | bỏ (gộp) | bước vào E10: 47 / 5; chi phí vào ghi chú diễn giả E04 |
| E06 | 47 / 8 | sửa | E06: 52 / 4 |
| E07 | 40 / 2 | sửa | E07: 48 / 4 |
| E08 | 44 / 5 | tách | E08: 52 / 5; E12: 46 / 5 |
| F01 | 70 / 7 | bỏ (gộp) | giả thiết nền lên F04: 51 / 4, F08: 51 / 4; nhu cầu sang F12: 38 / 4 |
| F02 | 71 / 5 | tách | F06: 56 / 7; F02: 59 / 5 |
| F04 | 99 / 6 | tách | F04: 51 / 4; F08: 51 / 4 |
| F05 | 84 / 7 | tách | F05: 58 / 6; F09: 39 / 5 |
| G01 | 81 / 7 | sửa | G01: 56 / 6 |
| G02 | 63 / 6 | sửa | G02: 58 / 7 |
| G03 | 80 / 5 | tách | G03: 56 / 6; G07: 44 / 5 |
| G04 | 72 / 7 | sửa | G04: 63 / 10 |

| Mã | Âm tiết | Dòng (script) | Dòng thực | Lý do cờ / ngoại lệ |
|---|---:|---:|---:|---|
| A02 | 73 | 5 | 5 | trang mục tiêu, trần 80 |
| A08 | 34 | 7 | 7 | trang nội dung bảy mạch; quyết định chung §5 cho phép 7 dòng |
| B00 | 41 | 2 | 3 | trang tiêu đề mạch: dòng dẫn 23 âm tiết ≤ 25 |
| B01 | 51 | 8 | 4 | bảng dữ kiện 3 hàng tính một khối; 51 ≤ 60 |
| C00 | 42 | 2 | 3 | trang tiêu đề mạch: dòng dẫn ≤ 25 |
| C04 | 57 | 8 | 5 | bảng dữ kiện tính một khối; 57 ≤ 60 |
| D00 | 43 | 2 | 3 | trang tiêu đề mạch: dòng dẫn ≤ 25 |
| D02 | 42 | 8 | 3 | bảng năm mẫu tính một khối; 42 ≤ 60 |
| E00 | 43 | 2 | 3 | trang tiêu đề mạch: dòng dẫn 22 ≤ 25 |
| E11 | 42 | 7 | 5 | bảng hai thuật toán tính một khối; 42 ≤ 60 |
| F00 | 40 | 2 | 3 | trang tiêu đề mạch: dòng dẫn 21 ≤ 25 |
| F06 | 60 | 7 | 5 | bảng ba lịch tính một khối; 60 ≤ 60 (trước vòng biên tập 56; thêm dòng "Xác định …" và định nghĩa "khối cực đại") |
| F13 | 79 | 6 | 1 | bảng so sánh năm giả thiết, trần 80 (trước vòng biên tập 70; hàng $\gamma<1$ dài hơn theo quyết định của điều phối viên) |
| G00 | 41 | 2 | 3 | trang tiêu đề mạch: dòng dẫn 21 ≤ 25 |
| G01 | 67 | 6 | 3 | bảng so sánh ba phương pháp, trần 80 (thêm theo/khác chính sách) |
| G06 | 74 | 5 | 2 | bảng hội tụ của mạch kết luận, trần 80 |
| G02 | 77 | 8 | 5 | ngoại lệ: trang trả lời vấn đề trung tâm thuộc nhóm tổng kết có bảng so sánh, trần 80 (trước vòng biên tập 58; thêm dòng "Bài toán:" và cột "Khởi tạo" theo quyết định của điều phối viên) |
| G04 | 72 | 10 | 4 | trang tổng kết bài tập về nhà, trần 80; bảng sáu hàng tính một khối (61 trước đợt đồng bộ 2026-10-14; thêm số 06.13–06.17 và nhãn "ghi chú:") |

Bảng trên là các trang `density.py` còn gắn cờ sau vòng biên tập và lý do được phép; không trang nội dung nào vượt 60, không trang nào vượt 80. `density.py` đếm cả dấu câu đứng riêng sau khi bỏ KaTeX (ví dụ ", ;"), nên số âm tiết thật thấp hơn vài đơn vị ở các trang nhiều công thức. Trung vị 52 âm tiết; 64/75 trang trên đích 40 (trước vòng biên tập 62/75, trung vị 50). Các trang định nghĩa, định lý và thuật toán giữ đủ giả thiết quyết định trên mặt trang theo `AGENTS.md` §"Trang phát biểu kết quả". Không dùng lớp hay thuộc tính thu nhỏ chữ; deck không còn khối `<style>` cục bộ (quy tắc KaTeX trong tiêu đề đã nằm trong `lecture-slide.css`).

## Thời lượng

Mở đầu 8 phút; mạch 2: 21; mạch 3: 18; mạch 4: 18; mạch 5: 19,5; mạch 6: 19,5; mạch 7: 16. Tổng 120 phút; phút từng trang ở [outline.md](outline.md). Mỗi trang tiêu đề mạch 0,5 phút. Vòng biên tập thêm 1 phút cho chứng minh B09 (1,5 → 2,5) và lấy lại 0,5 phút ở E11 (2 → 1,5), 0,5 phút ở F13 (2 → 1,5).

- **Cặp bài tập và khối 30 phút.** Trong 120 phút, các trang đề B07, C08, D08, E08, F05 chỉ được đọc đề (1,5 phút) và các trang lời giải B10, C09, D11, E12, F09 được trình bày như lời giải mẫu; thời gian sinh viên tự làm năm cặp này thuộc khối 30 phút chữa bài và thực hành. Bài tập tổng hợp G03/G07 và lời giải fragment ở A05 làm trên lớp.
- **Trang có thể lướt khi thiếu giờ:** C10 (lượt bị cắt của tàu đổ bộ), E11 (một chuyển của tàu đổ bộ), F13 (vai trò từng giả thiết; ghi chú diễn giả giữ nội dung). Ba trang này cộng 4,5 phút.
- 30 phút còn lại của ba tiết dành cho phần tự làm của năm cặp bài tập trên và bài thực hành LunarLander đã có.

## Sửa sau rà soát năm vai (2026-10-12)

Mọi trang dưới đây giữ mã, quyết định là `sửa` (trừ dòng dời chỗ); chi tiết từng phát hiện và lý do từ chối ở `review-log.md`, mục "Rà soát năm vai và biên tập (giai đoạn II)".

| Mã | Thay đổi | Nhu cầu được giải quyết |
|---|---|---|
| A07 | Ba dòng "Nhắc lại:" theo Bài 03, 04 ($q_*=T_*q_*$, $T_*$ co), 05 (Monte Carlo, TD(0), Robbins–Monro theo trạng thái); ký hiệu $d_0$ | Điểm xuất phát của lập luận và ký hiệu dùng ở C05, D05, E04 có trên mặt trang |
| A03 | Dòng 3–5 viết lại ("Lượt hoàn chỉnh", "Giữa lượt", "Dữ liệu từ chính sách còn thăm dò, mục tiêu theo chính sách tham lam"); nhãn SVG phóng 1,3 lần | Không dùng thuật ngữ hành vi/đích trước Định nghĩa 06.14 |
| A09 | Dòng nhắc lại Bài 05 với $\pi$ cố định; dòng lý do chuyển từ $V$ sang $Q$ | Cầu nối A09 → mạch 2 bằng lý do, không chỉ bằng ký hiệu |
| B01, B02, B05, B06, B09, B07, B10, B11 | Diễn giải B01 nêu điều kiện đi trái liên tục; "(action value)" ở B02; MDP đủ tên tiếng Anh, Ý nghĩa đọc kết quả bằng lời (B06); $w_a=w(a\mid s)$ và dòng $q_\pi=r+\gamma\sum p\,v_\pi$ (B09); câu 2, 4 của B07; bỏ câu kết lặp ở B10; "Một trạng thái" ở B11; câu nối B05 → B11 trong ghi chú diễn giả | Phát hiện SV, TOAN, PB, MACH, RL |
| C02, C03, C04, C06, C07, C10 | Ghi chú C02 trỏ sang C03, ghi chú C03 nối sang C04, ghi chú C04 nêu nguồn bảng nghiêng trái và thăm dò ở B; số thập phân ở C04; "Mỗi cặp có $f(s,a)$ xác định" (C06); nhãn SVG C07 phóng 1,3 lần; C10 không nhắc Sarsa trên mặt trang | Sợi ô $(\mathrm D,0)$ và thứ tự khái niệm |
| D03, D04, D05, D06, D07, D08 | D03 thành hàng hình riêng + bảng `Mẫu | Ô | Y | δ | Giá trị mới`, tiêu đề "Sarsa ở mẫu 1–2"; "sai số TD (TD error, Bài 05)", bỏ vế "học theo chính sách" (D04); "$\varepsilon$ hoặc lịch $\varepsilon_t$", định nghĩa $n(s,a)$, $h$ trên mặt trang (D05); nhận xét và ô "Hết ngân sách" của D06; tiêu đề D07 "Sarsa ở mẫu 3–5", "0+0,8·(…)"; câu 4 của D08 dùng động từ | Phát hiện SV, PB, TOAN, RL |
| E00, E01, E02, E03, E04, E06, E09, E12 | Dòng dẫn, từ khóa E00; Nhu cầu "giá trị của $(\mathrm C,0)$ khi từ B trở đi…" và "chính sách sinh dữ liệu" (E01); E02 cùng bố cục với D03, thêm $\gamma=1$; dòng điều kiện trùng mục tiêu của E03 chuyển vào ghi chú; "điều khiển Monte Carlo" (E09); kết luận có số ở E12 | Thuật ngữ trước định nghĩa; song song Sarsa/Q-learning |
| E07 | Thêm hai dòng về tỉ số $\rho$ của dự đoán TD(0) khác chính sách; gộp hai dòng giả thiết; dời lên trước E11 | Nhận xét 06.17 có nhu cầu trên mặt trang; thứ tự theo ghi chú |
| E11 | Thêm dòng "Tính …"; dời xuống sau E07 | Khuôn trang ví dụ |
| F00, F02, F06, F07, F08, F12, F13, F05 | Dòng dẫn F00 không KaTeX; tên tiếng Anh GLIE và "(độ phủ)" trên mặt F02, dòng lịch ví dụ chuyển vào ghi chú; F06 "khối cực đại" và số thập phân; F07 dòng "Tính …"; F08 thêm dòng điều khiển Monte Carlo; F12 dòng "Nhắc lại:"; F13 hàng $\gamma<1$ thành hệ quả, "mục tiêu độc lập"; F05 câu hỏi dùng động từ | Phát hiện RL 2, MACH T4, TOAN, PB |
| G00, G05, G09, G01, G06, G03, G07, G02, G08, G04 | Dòng dẫn và từ khóa G00; tiêu đề theo đối tượng G05/G09; G01 thêm theo/khác chính sách; G06 thứ tự hàng Monte Carlo–Sarsa–Q-learning, "bài không nêu định lý tới $q_*$"; G07 nêu nghĩa của ± và hiệu ghép cặp chứa 0; G02 dòng "Bài toán:" và cột "Khởi tạo"; G08 câu 3 mới; G04 chỉ ghi Bài tập 06.1–06.12 | Thu hồi đầu ra mạch 5, mạch 6 và bài toán tại D |
