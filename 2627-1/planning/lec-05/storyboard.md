# Storyboard Bài 05: Dự đoán phi mô hình

Cập nhật 2026-10-12, giai đoạn II của đợt sửa theo chuẩn 2026-10-12; sửa tiếp 2026-10-14 theo năm báo cáo rà soát (mục "Rà soát năm vai và biên tập" của `review-log.md`). Storyboard khớp deck `2627-1/lecture-05-du-doan-phi-mo-hinh.html` (70 trang, 6 mạch) và ghi chú bài giảng đã commit `e251162`. Nhãn mạch bằng chữ cái (A–E), mã trang và phút chỉ dùng trong tệp kế hoạch.

## Bản đồ mạch

| N | Mạch | Loại | Chức năng | Đầu vào từ mạch trước | Đầu ra cho mạch sau | Đóng góp cho vấn đề trung tâm | Trang tiêu đề | Phút |
|---|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu (A) | mở đầu | Đặt bài toán ước lượng $v_\pi$ từ lượt, ký hiệu, mục tiêu, khung cập nhật chung | Bài 03 ($v_\pi$, Bellman kỳ vọng), Bài 04 (quy hoạch động cần $P_\pi,r_\pi$) | Nhu cầu một mục tiêu cập nhật lấy từ dữ liệu | Phát biểu bài toán và năm câu trả lời có điều kiện | bìa L05-A01 | 8 |
| 2 | Lợi tức và ước lượng Monte Carlo (B) | phát triển kiến thức, thuật toán | Mục tiêu $G_t$, hai quy tắc lần ghé, trung bình gia tăng, bước hằng, thuật toán, hội tụ | Bài toán, khung cập nhật | Thuật toán 05.13, Định lý 05.16–05.17; giới hạn phải chờ lượt kết thúc | Câu trả lời khi có lượt hoàn chỉnh | L05-B00 (`mach-2`) | 34 |
| 3 | Sai phân thời gian TD(0) (C) | phát triển kiến thức, thuật toán | Mục tiêu một bước, sai số TD, thuật toán, trường hợp biên | Khung cập nhật, giới hạn của Monte Carlo | Bảng TD(0) trên $e_1$, $e_2$; Thuật toán 05.21 | Câu trả lời khi cần cập nhật sau mỗi chuyển | L05-C00 (`mach-3`) | 22 |
| 4 | Độ chệch, phương sai và hội tụ (D, phần đầu) | phát triển kiến thức, so sánh | Giá trị chuẩn; tách độ chệch, phương sai của mục tiêu; điều kiện hội tụ của TD(0) | Hai bảng trên cùng hai lượt | Mệnh đề 05.25, Định lý 05.28, 05.30 kèm giả thiết; nhu cầu xét dữ liệu cố định | Giả thiết nào bảo đảm mỗi phương pháp | L05-D00 (`mach-4`) | 26 |
| 5 | Dữ liệu cố định và cập nhật theo lô (D, phần sau) | phát triển kiến thức, thuật toán | Quét lại dữ liệu cố định; hai nghiệm theo hai tiêu chuẩn | Khung cập nhật, hai mục tiêu, giới hạn "dữ liệu mới" | Thuật toán 05.32, Mệnh đề 05.33–05.34 | Câu trả lời khi dữ liệu không tăng thêm | L05-DT (`mach-5`) | 14 |
| 6 | Tổng kết và chuyển tiếp (E) | kết luận | Đặt kết quả cạnh giả thiết; bài tập tổng hợp; trả lời bài toán; tự kiểm tra; bài tập về nhà | Mọi kết quả của mạch 2–5 | Lựa chọn có điều kiện; nhu cầu cải thiện chính sách (Bài 06) | Trả lời bài toán trung tâm | L05-E00 (`mach-6`) | 16 |

Số mạch là 6 (trong khoảng 5–7). Mạch D cũ được tách làm hai theo kế hoạch A1 và quyết định chung mục 8; trang tiêu đề mạch 5 mang mã `L05-DT` vì `L05-D00` đã dùng cho mạch 4. Trang "Nội dung" (L05-A02) liệt kê sáu mạch khớp số trên trang tiêu đề và chỉ số `#/N`.

## Cụm khái niệm và sáu bước

| Cụm | Dạng | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Dữ kiện truyền tiếp | Ghi chú bước |
|---|---|---|---|---|---|---|---|---|---|
| Bài toán dự đoán, lợi tức | khái niệm | B01 (Nhu cầu) | B01 (Trực quan.) | B02 | B03 | B09c pha 1; ghi chú diễn giả B03 ($e_2$, $\gamma=0{,}9$) | E04 câu 1; B13 | $e_1$, $e_2$, $G_t$ | Ví dụ dẫn nhập B01 làm cụ thể bài toán của A03 |
| Lần ghé, kỳ vọng mẫu | khái niệm | B04 (Nhu cầu) | B04c (Trực quan.) | B04 (bảng, ví dụ dẫn nhập đặt cùng vấn đề) | B04 (Định nghĩa), B04c (Mệnh đề) | B05, B09 | B13 (a) | tập mẫu tại $\mathrm S$, $\mathrm X$ | Thứ tự vấn đề + ví dụ dẫn nhập → trực giác → hình thức |
| Ước lượng Monte Carlo, trung bình gia tăng | khái niệm, thuật toán con | B06 (Nhu cầu) | B06 (Diễn giải, trục số) | B06 | B05, B07 | B09 | B13 (a) | $V_3(\mathrm X)=1/3$ | B05 định nghĩa trung bình trước nhu cầu gia tăng; trực giác gộp với ví dụ trên B06 |
| Bước học hằng | khái niệm phụ | B08 (Nhu cầu) | gộp với ví dụ B08 (bảng) và ghi chú diễn giả | B08 | B08 (Mệnh đề) | B09 | B13 (b), D13 (b) | $-0{,}25$ tại $\mathrm X$ | Chu trình rút gọn: khái niệm phụ, trực giác trọng số nằm ở Ý nghĩa và ghi chú diễn giả |
| Thuật toán Monte Carlo | thuật toán | B01, A07 (cần ghép thành quy trình) | B01 (Trực quan.) | B09c (tính tay một lượt) | B10, B10b (đánh số bước như Thuật toán 05.13; bước 5 gói phép cập nhật trong điều kiện lần ghé) | B09 (đối chiếu), ghi chú diễn giả B10b (Lunar Lander) | B13 | bảng sau $e_1$, $e_2$ | Tính tay trước giả mã |
| Hội tụ Monte Carlo | kết quả | B12 (Nhu cầu) | B12 (Trực quan.) | B12 (ví dụ dẫn nhập) | B12c, B12d | ghi chú diễn giả B12d ($J$ của Lunar Lander) | E04 câu 3, D13 (b) | $\sigma^2=320/441$ | Ví dụ dẫn nhập đặt cùng vấn đề, trước trực giác |
| Mục tiêu TD, TD(0) | khái niệm, thuật toán | C02 (Nhu cầu: chuyển đầu của $e_2$, giới hạn Monte Carlo) | C02 (Trực quan.) | C03 (bảng sau $e_1$, chuyển đầu của $e_2$); C07 (tính tay một lượt) | C04; C05, C05b | C08, C06, C06c | C10, C10b | bảng $(0;\ 0{,}5)$, $(-0{,}375;\ 0{,}375)$ | C01 cũ gộp vào C02; C03 dùng kết quả của C07 và nói rõ nguồn trong ghi chú diễn giả |
| Độ chệch của mục tiêu | khái niệm, kết quả | D01, D02 (bảng nào gần $v_\pi$); D05 (Nhu cầu) | D05 (Trực quan.) | D05 | D05b | D07 (Trực quan: điểm bất động của $T_\pi$), ghi chú diễn giả D05b | E04 câu 2 | $-34/105$ | — |
| Phương sai của mục tiêu | kết quả | D03 (Nhu cầu: mục tiêu Monte Carlo chứa mọi chuyển còn lại) | D04b (cầu nối "thay bảng bằng $v_\pi$", Trực quan.) | D03, D04 (dẫn nhập), D06 | D06b | D06 (Diễn giải 84 %, 20 %) | D13 (a) | $\operatorname{Var}$ trên hai dãy | Ví dụ dẫn nhập D03–D04 trước trực giác D04b |
| Hội tụ TD(0) | kết quả | D07a (Nhu cầu: vừa tới đích vừa tắt nhiễu) | D07 (Trực quan: điểm bất động của $T_\pi$) | D07a (dẫn nhập) | D07 | ghi chú diễn giả D07 (Lunar Lander, $1/n$) | D13 (b), (c); E04 câu 3 | ba lịch bước | Ví dụ dẫn nhập trước trực giác |
| Cập nhật theo lô | thuật toán, kết quả | D08 (Nhu cầu) | D08 (Trực quan.) | D09 (tính tay lượt quét đầu) | D09b; D10, D11 | D09c, D10, D11 | D12, D12b | $V_1=(0;\ 3/4)$ | Tính tay trước giả mã |

Câu nối giữa các bước nằm trong ghi chú diễn giả của từng trang (kết quả kế thừa, giả thiết đổi, giới hạn dẫn tới nhu cầu sau).

## Trang tiêu đề mạch

| Mã | Vị trí | Tên mạch | Dòng dẫn (âm tiết) | Từ khóa | Ghi chú diễn giả | Bước hành trình |
|---|---|---|---|---|---|---|
| L05-B00 | điểm vào mạch 2 | Lợi tức và ước lượng Monte Carlo | "Muốn ước lượng giá trị khi chưa biết mô hình, phải lấy trung bình lợi tức của các lượt đã kết thúc." (22) | Lượt · Lợi tức · Lần ghé · Trung bình gia tăng · Hội tụ | kế thừa $v_\pi=\mathbb E_\pi[G_t\mid S_t=s]$; nhiệm vụ: ước lượng bằng trung bình; đầu ra: khung cập nhật và giới hạn chờ lượt | ngoài hành trình khái niệm |
| L05-C00 | điểm vào mạch 3 | Sai phân thời gian TD(0) | "Muốn cập nhật trước khi lượt kết thúc, phải thay phần lợi tức chưa quan sát bằng giá trị ước lượng." (21) | Mục tiêu một bước · Sai số TD · Trạng thái kết thúc · Tự chuyển · Lượt bị cắt ngắn | kế thừa khung và hội tụ của Monte Carlo; nhiệm vụ: đổi mục tiêu; đầu ra: thuật toán, hai bảng | bước vấn đề của cụm TD(0), cùng C02 |
| L05-D00 | điểm vào mạch 4 | Độ chệch, phương sai và hội tụ | "Muốn so sánh Monte Carlo và TD(0), phải tách độ chệch, phương sai của mục tiêu và điều kiện hội tụ." (21) | Giá trị chuẩn · Độ chệch · Phương sai · Lịch bước học · Hội tụ | kế thừa hai bảng; nhiệm vụ: tách nguồn sai số; đầu ra: ba kết quả có giả thiết | ngoài hành trình khái niệm |
| L05-DT | điểm vào mạch 5 | Dữ liệu cố định và cập nhật theo lô | "Muốn dự đoán khi không thu thêm lượt, phải chọn tiêu chuẩn khớp dữ liệu trước khi quét lại." (19) | Cập nhật theo lô · Lượt quét · Khớp lợi tức · Quá trình phần thưởng Markov thực nghiệm | kế thừa giả thiết dữ liệu mới; nhiệm vụ: bỏ giả thiết đó; đầu ra: hai nghiệm, tiêu chuẩn | bước vấn đề của cụm theo lô, cùng D08 |
| L05-E00 | điểm vào mạch 6 | Tổng kết và chuyển tiếp | "Muốn chọn phương pháp dự đoán, phải nêu dữ liệu có sẵn, mục tiêu cập nhật và giả thiết của bảo đảm." (22) | Giả thiết không được bỏ · Lựa chọn phương pháp · Điều khiển phi mô hình | kế thừa mọi kết quả; nhiệm vụ: đặt cạnh giả thiết; đầu ra: lựa chọn, Bài 06 | ngoài hành trình khái niệm |

Mỗi trang tiêu đề mạch có quyết định `thêm`, lý do: chuẩn 2026-10-12 (`AGENTS.md` §"Trang tiêu đề mạch"). Ghi chú diễn giả của năm trang dài khoảng 70–100 âm tiết.

## Từng trang

Cột "Quyết định" so với deck trước đợt sửa (45 trang, 5 mạch). MT là mục tiêu học tập ở `outline.md`.

### Mạch 1. Mở đầu

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | Quyết định (lý do) |
|---|---|---|---|---|---|
| L05-A01 | bìa, tiêu đề mạch mở đầu | Nêu chủ đề, câu luận đề, đơn vị | — → A04 | — | sửa (câu luận đề trần thuật; thêm đơn vị; thuật ngữ gốc prediction, temporal difference, return) |
| L05-A04 | tiên quyết | Nhắc lại kết quả Bài 03–04 dùng trong bài; ký hiệu; giả thiết | A01 → A06 | tất cả | sửa (đổi chức năng thành "Tiên quyết và quy ước"; dòng Nhắc lại, Ký hiệu, Giả thiết) |
| L05-A06 | mục tiêu | Sáu mục tiêu kiểm tra được, ánh xạ bài tập trong ghi chú diễn giả | A04 → A02 | MT1–6 | thêm (A02 cũ gộp mục tiêu với nội dung) |
| L05-A02 | nội dung | Sáu mạch, số khớp `#/N` | A06 → A03 | — | sửa (thành "Nội dung"; tài liệu đọc trước chuyển vào ghi chú diễn giả để giữ ≤ 6 dòng) |
| L05-A03 | vấn đề trung tâm | Bài toán một dòng và câu trả lời có điều kiện của mạch 2–6 | A02 → A07 | MT6 | sửa (hai thẻ đầu vào chuyển vào ghi chú diễn giả; 2026-10-14: bỏ `learning-route.svg`; mỗi dòng có tiền tố điều kiện, dòng 4 "Bảng cố định:" song song E01) |
| L05-A07 | khung chung | Bốn dòng nêu cấu trúc cập nhật chung trước mạch nội dung | A03 → B00 | MT3, MT4 | thêm (khung chung theo `AGENTS.md`; 2026-10-14: gộp hai dòng đầu, thêm "TD một bước", "(batch updating)") |
| (L05-A05) | — | Câu hỏi kiểm tra mẫu chuyển | — | — | gộp (câu 1, 3 ứng với Bài tập 05.1 của ghi chú; ý "một mẫu chỉ là một kết quả" sang B01 ghi chú diễn giả) |

### Mạch 2. Lợi tức và ước lượng Monte Carlo

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | Quyết định (lý do) |
|---|---|---|---|---|---|
| L05-B00 | điểm vào mạch 2 | Trang tiêu đề mạch | A07 → B01 | — | thêm |
| L05-B01 | vấn đề + ví dụ dẫn nhập + trực giác | Ví dụ xuyên suốt làm cụ thể bài toán; ý tưởng trung bình lợi tức | B00 → B02 | MT1 | sửa (tên "tàu đổ bộ thu nhỏ (còn gọi là dãy bốn ô)"; "(mô hình chỉ để kiểm tra)"; hai lượt chuyển vào ghi chú diễn giả và hình B02 để giữ trần) |
| L05-B02 | ví dụ | Lợi tức của $e_1$, $e_2$ trên hình | B01 → B03 | MT1 | sửa (thành trang ví dụ; định nghĩa lần ghé chuyển sang B04) |
| L05-B03 | hình thức | Định nghĩa lượt, lợi tức; truy hồi; lượt bị cắt ngắn (truncated episode) | B02 → B04 | MT1 | sửa (nhãn Định nghĩa, Mệnh đề, Chứng minh; bảng tính ngược chuyển vào ghi chú diễn giả; 2026-10-14: tên tiếng Anh "truncated episode" trên mặt trang) |
| L05-B04 | vấn đề + ví dụ + hình thức | Chọn mẫu khi trạng thái lặp lại; hai quy tắc | B03 → B04c | MT2 | tách (mệnh đề Markov sang B04c; thêm "(visit)", "(first-visit)", "(every-visit)") |
| L05-B04c | trực giác + kết quả | Mỗi mẫu có kỳ vọng $v_\pi(s)$ | B04 → B05 | MT2 | thêm (tách từ B04; Mệnh đề 05.7) |
| L05-B05 | hình thức | Định nghĩa ước lượng Monte Carlo | B04c → B06 | MT2, MT3 | sửa ("$g_i(s)$ là …"; bảng tổng chuyển vào B06) |
| L05-B06 | vấn đề + ví dụ | Nhu cầu cập nhật không lưu mẫu; hai cách tính | B05 → B07 | MT3 | sửa (tiêu đề "Ví dụ:"; nhãn "Yêu cầu:" thành "Nhu cầu:"; hai thẻ thành hai dòng) |
| L05-B07 | kết quả | Trung bình gia tăng; tên mục tiêu cập nhật, bước học | B06 → B08 | MT3 | sửa (một khối công thức; khung chung sang A07) |
| L05-B08 | vấn đề + ví dụ + kết quả | Bước hằng và trọng số mũ | B07 → B09 | MT3 | sửa (Mệnh đề 05.11 nội dòng; 2026-10-14: Nhu cầu "theo kịp môi trường thay đổi (ngoài giả thiết dừng)") |
| L05-B09 | ví dụ + ứng dụng | Bốn cấu hình trên hai lượt; Nhận xét hai trục | B08 → B09c | MT3 | sửa (thêm cột sau $e_2$, gộp B11 cũ; Nhận xét 05.12) |
| L05-B09c | ví dụ tính tay thuật toán | Một lượt Monte Carlo lần ghé đầu tiên, hai pha | B09 → B10 | MT3 | thêm (Ví dụ 05.6; tính tay trước giả mã) |
| L05-B10 | thuật toán (1/2) | Đầu vào, đầu ra, giả thiết, khởi tạo, bước 1–3 | B09c → B10b | MT3 | tách (giả mã > 8 dòng; 2026-10-14: đánh số bước như Thuật toán 05.13, bước con thụt lề, Giả thiết lên trang đầu) |
| L05-B10b | thuật toán (2/2) | Bước 4–6, lượt bị cắt | B10 → B12 | MT1, MT3 | thêm (2026-10-14: mở bằng "Trong vòng lặp của bước 1:"; bước 5 gói phép cập nhật trong điều kiện lần ghé, sửa lỗi nghiêm trọng TOAN) |
| (L05-B11) | — | Monte Carlo trên lượt thứ hai | — | — | gộp vào B09 (cùng số liệu Ví dụ 05.5) |
| L05-B12 | vấn đề + ví dụ dẫn nhập + trực giác | Sai số giảm theo $1/\sqrt n$; $11/21$ giải từ mô hình chỉ để đo sai số | B10b → B12c | MT3 | tách (B12 cũ 132 âm tiết; phần ví dụ mới theo Ví dụ 05.7) |
| L05-B12c | kết quả | Hội tụ của lần ghé đầu tiên, đủ giả thiết | B12 → B12d | MT3 | thêm (Định lý 05.16; 2026-10-14: nhãn Định nghĩa/Định lý, cùng chỉ số $n$, "cùng phân phối", "phần thưởng bị chặn", chứng minh vào ghi chú diễn giả) |
| L05-B12d | kết quả | Hội tụ của mọi lần ghé; chệch ở số lượt hữu hạn; bước hằng | B12c → B13 | MT3 | thêm (Định lý 05.17, Nhận xét 05.18–05.19; 2026-10-14: $\sigma^2$ có giả thiết mẫu độc lập cùng phân phối; "hầu chắc chắn" ra ngoài KaTeX; định nghĩa $J$ trong ghi chú diễn giả) |
| L05-B13 | kiểm tra (đề) | Chọn mẫu và bước hằng tại $\mathrm S$ với $\gamma=0{,}9$ | B12d → B13b | MT2, MT3 | sửa (2026-10-14: đổi dữ kiện để không lặp B04 và B08; đề trong một khung "Câu hỏi:") |
| L05-B13b | kiểm tra (lời giải) | Lời giải từng bước trên số mới | B13 → C00 | MT2, MT3 | thêm |

### Mạch 3. Sai phân thời gian TD(0)

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | Quyết định (lý do) |
|---|---|---|---|---|---|
| L05-C00 | điểm vào mạch 3 | Trang tiêu đề mạch | B13b → C02 | — | thêm |
| L05-C02 | vấn đề + trực giác | Giới hạn của Monte Carlo ở chuyển đầu của $e_2$; thay phần chưa quan sát bằng ước lượng; mục tiêu bootstrap | C00 → C03 | MT4 | gộp (C01 cũ vào C02; 2026-10-14: Nhu cầu đổi sang $e_2$ cho khớp C03; vẽ lại `mc-td-targets.svg` nhãn lớn) |
| L05-C03 | ví dụ | Một bước TD(0) tính tay trên bảng sau $e_1$ | C02 → C04 | MT4 | sửa (2026-10-14: khuôn bảng TD cố định, nhãn ngoài KaTeX, "sai số TD (TD error)" lần đầu) |
| L05-C04 | hình thức | Định nghĩa mục tiêu TD, sai số TD | C03 → C07 | MT4 | sửa (nhãn Định nghĩa; "(TD error)") |
| L05-C07 | ví dụ tính tay thuật toán | TD(0) trên $e_1$ | C04 → C05 | MT4 | sửa (đặt trước giả mã theo Ví dụ 05.9; khuôn bảng cố định; 2026-10-14: "Tính …" và Diễn giải trên mặt trang) |
| L05-C05 | thuật toán (1/2) | Đầu vào, giả thiết, khởi tạo, bước 1–3 | C07 → C05b | MT4 | tách (2026-10-14: đánh số như Thuật toán 05.21, bước con thụt lề, Giả thiết lên trang đầu) |
| L05-C05b | thuật toán (2/2) | Bước 4–7, đọc rồi ghi, dừng giữa lượt | C05 → C08 | MT4 | thêm (2026-10-14: "Trong vòng lặp của bước 1:"; bước 6 gán $S$ khi mở lượt mới) |
| L05-C08 | ứng dụng | TD(0) trên $e_2$, đọc bảng đã ghi | C05b → C06 | MT4 | sửa (khuôn bảng cố định; 2026-10-14: hết tràn khung, cột Chuyển không ngắt dòng, Diễn giải một dòng trên mặt trang) |
| L05-C06 | ứng dụng | Hai chuyển thật của Lunar Lander | C08 → C06c | MT4 | sửa (Ví dụ 05.11; 2026-10-14: Nhu cầu, giới thiệu ô gộp $9216$, khuôn bảng TD cố định, Diễn giải) |
| L05-C06c | hình thức (nhận xét) | Trường hợp biên của bước đọc bảng | C06 → C10 | MT1, MT4 | thêm (Nhận xét 05.22) |
| (L05-C09) | — | Chi phí bộ nhớ và tính toán | — | — | bỏ (chuyển vào ghi chú diễn giả C05 và Nhận xét 05.23 của ghi chú bài giảng) |
| L05-C10 | kiểm tra (đề) | Một bước TD(0) với trạng thái kết thúc | C06c → C10b | MT4 | sửa (tiêu đề "Bài tập:"; khuôn bảng cố định) |
| L05-C10b | kiểm tra (lời giải) | Lời giải trên bảng | C10 → D00 | MT4 | thêm |

### Mạch 4. Độ chệch, phương sai và hội tụ

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | Quyết định (lý do) |
|---|---|---|---|---|---|
| L05-D00 | điểm vào mạch 4 | Trang tiêu đề mạch | C10b → D01 | — | thêm |
| L05-D01 | vấn đề + ví dụ | Hai bảng trên cùng hai lượt; cần giá trị chuẩn | D00 → D02 | MT5 | sửa (tiêu đề "Ví dụ:"; hai gạch đầu dòng vào ghi chú diễn giả) |
| L05-D02 | ví dụ | Giá trị chuẩn và độ lệch | D01 → D05 | MT5 | sửa ("Nhắc lại:" Bellman kỳ vọng; bảng độ lệch giữ hàng sau $e_2$, hàng sau $e_1$ vào ghi chú diễn giả) |
| L05-D05 | vấn đề + trực giác + ví dụ | Kỳ vọng mục tiêu TD với bảng cố định | D02 → D05b | MT5 | tách (phần ví dụ của D05 cũ) |
| L05-D05b | hình thức + kết quả | Định nghĩa độ chệch; Mệnh đề 05.25; Monte Carlo không chệch có điều kiện | D05 → D03 | MT5 | thêm (2026-10-14: "luôn không chệch" thành câu có giả thiết Markov, $\pi$ cố định; chứng minh vào ghi chú diễn giả) |
| L05-D03 | vấn đề + ví dụ dẫn nhập | Dãy bảy ô | D05b → D04 | MT5 | sửa (tên "dãy bảy ô"; Nhu cầu) |
| L05-D04 | ví dụ dẫn nhập | Hai lợi tức khác xa từ cùng $\mathrm S$ | D03 → D04b | MT5 | sửa (tiêu đề "Ví dụ:"; một dòng Diễn giải) |
| L05-D04b | trực giác | Mục tiêu lý tưởng $Y^*$ | D04 → D06 | MT5 | thêm (bước trực giác còn thiếu; `target-randomness.svg`; 2026-10-14: dòng "Nhu cầu:" tách dao động khỏi độ chệch) |
| L05-D06 | ví dụ | Bảng phương sai trên hai dãy | D04b → D06b | MT5 | tách (phần bảng của D06 cũ) |
| L05-D06b | kết quả | Định lý phương sai, Lưu ý bảng đang học | D06 → D07a | MT5 | thêm (phần mệnh đề của D06 cũ) |
| L05-D07a | vấn đề + ví dụ dẫn nhập | Hai lịch bước học và bước hằng | D06b → D07 | MT5 | thêm (Ví dụ 05.19; 2026-10-14: Nhu cầu "vừa tới đích vừa tắt nhiễu", Diễn giải phương sai giới hạn của bước hằng thay hàng bảng) |
| L05-D07 | trực giác + kết quả | Định lý hội tụ TD(0) với giả thiết trên mặt trang | D07a → D13 | MT5 | sửa (2026-10-14: Trực quan nhắc lại $T_\pi V=r_\pi+\gamma P_\pi V$ (Bài 04) và điểm bất động; dòng "Lịch bước học Robbins–Monro:" trước công thức có $\alpha_n(s)\in[0,1]$) |
| L05-D13 | kiểm tra (đề) | Ba nhận định về phương sai, bước hằng, lịch bước | D07 → D13b | MT5 | thêm (nhận câu 2–3 của D12 cũ) |
| L05-D13b | kiểm tra (lời giải) | Lời giải có số | D13 → DT | MT5 | thêm |

### Mạch 5. Dữ liệu cố định và cập nhật theo lô

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | Quyết định (lý do) |
|---|---|---|---|---|---|
| L05-DT | điểm vào mạch 5 | Trang tiêu đề mạch (mã `T` vì `L05-D00` đã dùng) | D13b → D08 | — | thêm |
| L05-D08 | vấn đề + ví dụ dẫn nhập + trực giác | Tám lượt, hai cách đọc | DT → D09 | MT6 | sửa (tiêu đề "Ví dụ:"; Nhu cầu; Trực quan) |
| L05-D09 | ví dụ tính tay thuật toán | Lượt quét đầu | D08 → D09b | MT6 | tách (phần ví dụ của D09 cũ; bỏ CSS `.9em`) |
| L05-D09b | thuật toán | Quy trình cập nhật theo lô, ngưỡng $\theta$ | D09 → D09c | MT6 | thêm (phần quy trình của D09 cũ; $\varepsilon$ thành $\theta$) |
| L05-D09c | ứng dụng | Các lượt quét tiếp theo; ngưỡng dừng không đo sai số | D09b → D10 | MT6 | thêm (Ví dụ 05.22; nhận công thức đóng từ D11 cũ) |
| L05-D10 | kết quả | Nghiệm Monte Carlo theo lô | D09c → D11 | MT6 | sửa (nhãn Mệnh đề; điều kiện $\alpha N(s)<2$) |
| L05-D11 | kết quả | Nghiệm TD theo lô, quá trình phần thưởng Markov thực nghiệm | D10 → D12 | MT6 | sửa (2026-10-14: tách Ký hiệu và Giả thiết; thêm "mọi lượt của $\mathcal D$ kết thúc hoặc $\gamma<1$") |
| L05-D12 | kiểm tra (đề) | Lượt quét thứ ba; giải thích hai nghiệm | D11 → D12b | MT6 | sửa (giữ câu 1 của D12 cũ, thêm Bài tập 05.12; câu 2–3 sang D13) |
| L05-D12b | kiểm tra (lời giải) | Lời giải và Cách khác | D12 → E00 | MT6 | thêm |

### Mạch 6. Tổng kết và chuyển tiếp

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | Quyết định (lý do) |
|---|---|---|---|---|---|
| L05-E00 | điểm vào mạch 6 | Trang tiêu đề mạch | D12b → E02 | — | thêm |
| L05-E02 | tổng kết (1/2) | Kết quả mạch 2 cạnh giả thiết | E00 → E02b | tất cả | tách (2026-10-14: tiêu đề "Kết quả và giả thiết không được bỏ"; dòng giả thiết chung) |
| L05-E02b | tổng kết (2/2) | Kết quả mạch 4–5 cạnh giả thiết | E02 → E02c | tất cả | thêm (2026-10-14: giả thiết đủ cho TD(0) và theo lô) |
| L05-E02c | khung chung | Quy tắc cập nhật, dữ liệu, điều kiện dừng của ba phương pháp | E02b → E02d | MT3, MT4, MT6 | thêm |
| L05-E02d | điều kiện hội tụ | Giả thiết không được bỏ và kết luận của bốn hàng phương pháp | E02c → E06 | MT3, MT5 | thêm (2026-10-14: giả thiết đủ theo TOAN; gộp hai hàng Monte Carlo $1/N(s)$) |
| L05-E06 | bài tập tổng hợp (đề) | Lượt $e_3$ cho cả hai phương pháp | E02d → E06b | MT3, MT4, MT5 | thêm (trùng Bài tập 05.8 của ghi chú) |
| L05-E06b | bài tập tổng hợp (lời giải) | Lời giải trên mặt trang | E06 → E01 | MT3, MT4, MT5 | thêm |
| L05-E01 | trả lời vấn đề trung tâm | Năm kết luận có điều kiện song song với A03, dòng Nguồn, nối Bài 06 | E06b → E04 | MT6 | sửa (2026-10-14: năm dòng 2–6 có số liệu; dòng 4 thu hồi cả độ chệch, phương sai ($Y^*$ bỏ $20\%$) và Robbins–Monro; câu nối Bài 06 ở dòng 6) |
| L05-E04 | tự kiểm tra | Bốn câu, mỗi câu một giả thiết hoặc phân biệt | E01 → E03 | MT1, MT3, MT5 | sửa (câu mở chuẩn; ba thẻ thành danh sách) |
| L05-E03 | bài tập về nhà, tài liệu đọc | Bảng `Mạch \| Bài tập` theo bảng mạch của `exercises.md` (số hiệu của tệp bài tập; bài chỉ trong ghi chú có nhãn "ghi chú:"); tài liệu đọc; liên kết "Ghi chú bài giảng · Bài tập" | E04 → — | tất cả | sửa (gộp E05; 2026-10-14: bỏ cột số hiệu dự kiến, thêm mạch 1, tách 5 và 6; 2026-10-14, đồng bộ bài tập về nhà: thêm 05.16–05.28 theo mạch, thay "Tệp bài tập: chưa có" bằng liên kết viewer `exercises.md`) |
| (L05-E05) | — | Tài liệu đọc | — | — | gộp vào E03 |

## Ngoại lệ mật độ

Đếm bằng `density.py` (âm tiết là từ tách theo khoảng trắng; dấu câu đứng sau công thức cũng bị tính). Sau đợt biên tập 2026-10-14 còn mười trang có dòng `<-- VƯỢT`, mỗi trang có lý do:

| Mã | Số đo | Lý do |
|---|---|---|
| L05-A06 | 80 âm tiết, 6 dòng | Trang mục tiêu, trần 80; sáu mục tiêu ứng với sáu sản phẩm kiểm tra |
| L05-B00, L05-C00, L05-D00, L05-E00 | dòng dẫn 21–22 âm tiết | Trang tiêu đề mạch: dòng dẫn theo quy định riêng ≤ 25 âm tiết; tổng 37–42 âm tiết |
| L05-E02 | 72 âm tiết, 6 dòng | Trang tổng kết, trần 80; bảng ba cột bắt buộc và dòng giả thiết cho hàng 2 và 4 |
| L05-E02b | 80 âm tiết, 6 dòng | Trang tổng kết, trần 80; giả thiết đủ cho TD(0) và theo lô, điều kiện bước học tách Monte Carlo và TD (trước: 66) |
| L05-E02d | 80 âm tiết, 6 dòng | Bảng hội tụ, trần 80; giả thiết đủ theo TOAN (trước: 76; bản nháp 99 được rút bằng dòng giả thiết chung và gộp hai hàng Monte Carlo) |
| L05-E01 | 78 âm tiết, 6 dòng | Trang trả lời vấn đề trung tâm xếp vào loại tổng kết (trần 80): năm dòng song song với A03, mỗi dòng một điều kiện và một số liệu, cùng dòng "Nguồn:" (trước: 60 với ba dòng) |

Các trang còn lại không vượt trần 60 âm tiết, 6 dòng, 20 âm tiết mỗi dòng, 3 công thức hiển thị. Đợt biên tập rút về trần các trang bị kéo dài khi thêm giả thiết: B01 (70 → 58), B04c (66 → 56, chứng minh vào ghi chú diễn giả), B10 (67 → 58), B10b (63 → 57), B12 (64 → 58), B12c (71 → 59), B12d (75 → 59), C03 (72 → 60), C05 (63 → 56), C05b (67 → 60), C06 (68 → 55), A03 (82 → 60), D11 (64 → 59); các số trước là bản nháp giữa đợt, sau khi thêm giả thiết. Không có trang nào được thu nhỏ chữ.

Các trang vượt trần trước đợt sửa (số âm tiết, dòng, âm tiết tối đa mỗi dòng theo `density.py`) và trang sau sửa:

| Trang cũ | Trước | Quyết định | Sau |
|---|---|---|---|
| A02 | 64; 7 dòng | tách | A02 35; A06 80 (ngoại lệ) |
| A03 | 80; 10 dòng | sửa | 60; 6 dòng |
| A04 | 56; 7 dòng | sửa | 58; 6 dòng |
| A05 | 68; dòng 22 | gộp | — |
| B01 | 58; dòng 31 | sửa | 50; dòng 20 |
| B04 | 105; 7 dòng; dòng 33 | tách | B04 59; B04c 59 |
| B06 | 53; dòng 27 | sửa | 53; dòng 16 |
| B08 | 72; dòng 32 | sửa | 46 |
| B10 | 77; 7 dòng | tách | B10 59; B10b 58 |
| B12 | 132; 11 dòng; dòng 38 | tách | B12 60; B12c 60; B12d 58 |
| C05 | 84; 9 dòng | tách | C05 60; C05b 58 |
| C06 | 61; 10 dòng | sửa, thêm C06c | C06 51; C06c 51 |
| C09 | 87; 7 dòng | bỏ | — |
| C10 | 48; 7 dòng | tách | C10 39; C10b 28 |
| D01 | 84; 7 dòng; dòng 28 | sửa | 52; 6 dòng |
| D02 | 61; dòng 25 | sửa | 49 |
| D05 | 72; dòng 27 | tách | D05 53; D05b 59 |
| D07 | 68; 8 dòng; dòng 29 | sửa, thêm D07a | D07 58; D07a 36 |
| D08 | 68; 7 dòng; dòng 30 | sửa | 47; 6 dòng |
| D09 | 94; 12 dòng | tách | D09 55; D09b 56; D09c 50 |
| D12 | 98; dòng 25 | tách | D12 44; D12b 48; D13 60; D13b 51 |
| E01 | 89; dòng 21 | sửa | 78 (ngoại lệ, trần 80) |
| E02 | 122; 8 dòng; dòng 39 | tách | E02 59; E02b 66; E02c 38; E02d 76 |
| E03 | 88; 11 dòng | sửa, gộp E05; đồng bộ `exercises.md` (2026-10-14) | 54; 6 dòng; sau đồng bộ 62; 6 dòng; dòng dài nhất 15 (ngoại lệ trang tổng kết, trần 80: bảng sáu mạch phải liệt kê đủ số hiệu của tệp bài tập và ghi chú, phần lớn là số hiệu) |
| E04 | 65; 7 dòng | sửa | 49 |
| E05 | 78 | gộp | — |

Trước: 45 trang, 36 dòng vượt, 22 trang trên 60 âm tiết. Sau (đo 2026-10-14): 70 trang, 10 dòng vượt đều có ngoại lệ (A06, B00, C00, D00, E00, E02, E02b, E02d, E01), 5 trang trên 60 âm tiết (A06, E02, E02b, E02d, E01, đều trần 80). Sau đồng bộ bài tập về nhà (2026-10-14): thêm E03 ($62$ âm tiết, trần 80 của trang tổng kết).

## Thời lượng

| Mạch | Trang | Phút | Ghi chú |
|---|---:|---:|---|
| 1 | 6 | 8 | mục tiêu và nội dung đọc nhanh |
| 2 | 19 | 34 | bài tập B13 khoảng 4 phút |
| 3 | 12 | 22 | bài tập C10 khoảng 3 phút |
| 4 | 14 | 26 | bài tập D13 khoảng 4 phút |
| 5 | 9 | 14 | lời giải D12b khoảng 2 phút (đề giải trong khối 30 phút) |
| 6 | 10 | 16 | lời giải E06b khoảng 2 phút (đề giải trong khối 30 phút); bảng tổng kết đọc nhanh |
| Tổng | 70 | 120 | 30 phút ngoài trình chiếu cho chữa bài tập và notebook |

Khối 30 phút ngoài trình chiếu: sinh viên tự giải D12 (a) và bài tập tổng hợp E06 trước khi xem lời giải D12b, E06b (khoảng 15 phút), rồi chạy minh họa notebook Lunar Lander (khoảng 15 phút). Trong 120 phút trình chiếu, D12b và E06b chỉ được đọc lời giải (khoảng 2 phút mỗi cặp); B13/B13b, C10/C10b, D13/D13b được giải trên lớp trong phần phút của mạch.

Trang có thể bỏ khi thiếu giờ (giao tự đọc), theo thứ tự ưu tiên: L05-B12d (phần Lưu ý), L05-C06, L05-D09c, L05-B04c (chứng minh nằm trong ghi chú diễn giả); nội dung đầy đủ nằm trong ghi chú bài giảng.
