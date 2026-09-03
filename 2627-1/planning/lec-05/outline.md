# Dàn ý Bài 05: Dự đoán phi mô hình

## Mục tiêu và phạm vi

Sinh viên phân biệt giá trị thật $v_\pi$, ước lượng $V_t$, phần thưởng tích lũy $G_t$, đích $Y_t^{\mathrm{TD}}$ và sai số $\delta_t$; thực hiện Monte Carlo (MC) lần ghé đầu và sai phân thời gian TD(0) dạng bảng; nêu điều kiện hội tụ đi cùng giả thiết; so sánh cơ chế chệch–phương sai mà không xếp hạng phổ quát.

Thiết lập: quy trình quyết định Markov (MDP) bảng hữu hạn, chưa biết mô hình; chính sách Markov dừng $\pi$ cố định; dữ liệu theo chính sách; phần thưởng bị chặn. MC dùng lượt kết thúc gần như chắc chắn và $V(\text{kết thúc})=0$. Không dạy điều khiển, khác chính sách, Q-learning, xấp xỉ hàm hoặc mã nguồn.

## Cấu trúc

| Phần | Trang | Nội dung |
|---|---|---|
| Định hướng | P00–P02 | Bài toán, giả thiết, đối tượng cần học |
| Monte Carlo | A00–A08 | Lượt mẫu, $G_t$, thuật toán đầy đủ, hai lượt trung bình mẫu, giá trị chuẩn đối chiếu, hai trục thiết kế |
| TD(0) | B00–B08 | Chuyển mẫu, đích, thuật toán đầy đủ, cập nhật tại chỗ, toán tử Bellman và bước học |
| So sánh | C00–C07 | Đi bộ dài, chỉ số, phạm vi tác động, cơ chế chệch–phương sai |
| Tổng hợp | D00–D01 | Năm ý và cầu nối điều khiển |
| Bài tập dọc | X07,X03,X04 | Giải thích kết quả, phép cập nhật TD, chệch–phương sai |

Tệp có 31 trang chính và 3 trang bài tập dọc. Tuyến lõi là 108 phút; vùng đệm 12 phút dành cho A06 và phần hiện dần về $\gamma=1$ ở B07. Nhánh bài tập dùng 30 phút.

## Ánh xạ nguồn

| Nguồn | Đích | Quyết định |
|---|---|---|
| tr. 1–14 | P00 | Lược ôn tập Bài 04; tr. 1 cung cấp tên bài và cầu nối |
| tr. 15–16 | P00–P02 | Giữ cầu nối mô hình đã biết/chưa biết; bổ sung giả thiết và kiểu đại lượng |
| tr. 17–23 | A00–A08 | Giữ MC; thêm giao diện thuật toán; áp dụng trọn trung bình mẫu trước $\alpha$ hằng; đặt giá trị chuẩn đối chiếu sau ước lượng |
| tr. 24–29 | B00–B08 | Đưa chuyển mẫu trước công thức; thêm giao diện thuật toán, định nghĩa $T^\pi$ và Robbins–Monro theo số lần cập nhật |
| tr. 30–31 | C00–C05 | Sửa số mũ và giá trị $0{,}970299$, $-0{,}99$; giải thích cơ chế chệch–phương sai có điều kiện. C00 không dùng hai giá trị chuẩn của nguồn vì không tái tạo nhất quán từ mô hình đã nêu |
| tr. 32–33 | C06–C07, D01 | Giữ phạm vi, câu tự kiểm và cầu nối; không dạy điều khiển |
| hw05 B7/B3/B4 | X07/X03/X04 | Nhánh dọc tự đủ; X07 chuyển từ tính lặp sang giải thích cơ chế |
| hw05 Bài 1 | B05/C07 | Hấp thụ: phân biệt đích MC và đích TD một bước, thời điểm cập nhật |
| hw05 Bài 2 | P01–P02/B00 | Hấp thụ: bài toán dự đoán theo chính sách, chuyển mẫu trước công thức |
| hw05 Bài 6 | (lược) | Yêu cầu giải Bellman bằng mô hình đã biết; trùng Bài 04 và ngoài phạm vi phi mô hình |

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $v_\pi(s)$ | Giá trị thật của chính sách cố định |
| $V_t(s)$ | Ước lượng trước cập nhật ở bước $t$ |
| $G_t$ | Tổng phần thưởng chiết khấu đến kết thúc |
| $Y_t^{\mathrm{TD}}$ | $R_{t+1}+\gamma V_t(S_{t+1})$ |
| $\delta_t$ | $Y_t^{\mathrm{TD}}-V_t(S_t)$ |
| $N(s)$ | Số mẫu MC được nhận cho trạng thái $s$ |
| $n(s)$ | Số lần TD đã cập nhật trạng thái $s$ |
| $\alpha_n(s)$ | Bước học ở lần cập nhật thứ $n$ của trạng thái $s$ |
| $T^\pi$ | Toán tử kỳ vọng Bellman của chính sách $\pi$ |

## Bản đồ note tự học

Note tự học tại `materials/lec-05/lecture-note.md` dùng 15 chủ đề duy nhất `lec-05-topic-01..15`. Nhãn bắt buộc gồm: cốt lõi (01, 02, 03, 04, 06, 07, 08, 09, 12, 13, 15), cầu nối (05, 10, 11), bổ sung (14), và đọc thêm (ôn MDP, quy hoạch động ở tr. 1–14 cùng tài liệu tham khảo; không có topic ID). Bốn mạch nội dung là Đặt bài (01), Monte Carlo (02–06), TD(0) (07–11), So sánh và tổng hợp (12–15). Mỗi chủ đề ghi vai trò, kết nối vào/ra, nguồn trang và đi theo mạch vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng/giới hạn → exercise + hint + solution. Note không thêm code demo, không dùng hai giá trị $0{,}829$ và $0{,}992$, không xếp hạng phương sai MC–TD vô điều kiện, và tách trung bình mẫu khỏi $\alpha$ hằng.

### Ánh xạ 15 topic sang data-slide-id

| Topic | Slide | Ghi chú |
|---|---|---|
| 01 | P00, P01, P02 | Đặt bài, giả thiết, $v_\pi$ vs $V_t$ |
| 02 | A00, A01 | Lượt $e_1$, $G_t$, chỉ số $\gamma^k$ |
| 03 | A02 | Thuật toán MC lần ghé đầu đầy đủ |
| 04 | A03 | Hai lượt, trung bình mẫu $(1,1)\to(0,0)$ |
| 05 | A04 | Giá trị chuẩn đối chiếu $11/21$, $19/21$ |
| 06 | A05, A06, A08 | Hai trục; A06 là vùng đệm mọi lần ghé |
| 07 | B00, B01 | Chuyển mẫu, $Y_t^{\mathrm{TD}}$, $\delta_t$ |
| 08 | B02 | Thuật toán TD(0) đầy đủ |
| 09 | B03, B04, B05, B08 | Tính tay hai lượt, cập nhật tại chỗ và so thời điểm cập nhật |
| 10 | B06 | $T^\pi$, kỳ vọng $\delta_t$ |
| 11 | A07, B07 | Giả thiết hội tụ, $\gamma<1$ và $\gamma=1$ theo lượt |
| 12 | C00, C01, C05 | Đi bộ dài, $\gamma^3=0{,}970299$, $-\gamma=-0{,}99$ |
| 13 | C02, C03 | Cơ chế chệch–phương sai có điều kiện |
| 14 | C04, C06 | Tiêu chí chọn, giới hạn, phạm vi |
| 15 | D00, D01, X07, X03, X04 | Tổng hợp, cầu nối, bài tập dọc |

### Ánh xạ hw05

| Bài tập | Topic | Quyết định |
|---|---|---|
| hw05 B7 | topic 04, 06, 09, 15 (X07) | Chuyển từ lặp phép tính sang giải thích ba kết quả |
| hw05 B3 | topic 07, 08, 15 (X03) | Bổ sung số để tự đủ; dùng $\alpha_{n(s)}(s)=0{,}1$ |
| hw05 B4 | topic 13, 15 (X04) | Cơ chế có điều kiện, không xếp hạng phổ quát |
| hw05 Bài 1 | topic 06, 07 | Hấp thụ: đích MC vs đích TD, thời điểm cập nhật |
| hw05 Bài 2 | topic 01, 07 | Hấp thụ: quan sát bốn đại lượng, học từ mẫu |
| hw05 Bài 5 | topic 06 | Hấp thụ: ba cách cập nhật và điều kiện hội tụ chung |
| hw05 Bài 6 | (lược) | Giải Bellman khi biết mô hình, trùng Bài 04, ngoài phạm vi phi mô hình |

## Tài sản SVG

- `short-walk.svg`: môi trường ngắn và nhiễu hành động.
- `design-grid.svg`: ma trận hai trục của Monte Carlo.
- `mc-td-timeline.svg`: thời điểm cập nhật trên cùng lượt.
- `long-walk.svg`: chỉ số phần thưởng và số mũ chiết khấu.
