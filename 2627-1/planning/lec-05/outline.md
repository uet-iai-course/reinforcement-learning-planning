# Dàn ý Bài 05: Dự đoán phi mô hình

## Mục tiêu và phạm vi

Sinh viên phân biệt giá trị thật $v_\pi$, ước lượng $V_t$, phần thưởng tích lũy $G_t$, đích $Y_t^{\mathrm{TD}}$ và sai số $\delta_t$; thực hiện Monte Carlo (MC) lần ghé đầu tiên và sai phân thời gian TD(0) dạng bảng; nêu điều kiện hội tụ đi cùng giả thiết; so sánh cơ chế chệch–phương sai mà không xếp hạng phổ quát.

Thiết lập: quy trình quyết định Markov (MDP) bảng hữu hạn, chưa biết mô hình; chính sách Markov dừng $\pi$ cố định; dữ liệu theo chính sách; phần thưởng bị chặn. MC dùng lượt kết thúc gần như chắc chắn và $V(\text{kết thúc})=0$. Không dạy điều khiển, khác chính sách, Q-learning, xấp xỉ hàm hoặc mã nguồn.

## Cấu trúc

| Phần | Trang | Nội dung |
|---|---|---|
| Định hướng | P00–P02 | Bài toán, giả thiết, đối tượng cần học |
| Monte Carlo | A00–A08 | Lượt mẫu, $G_t$, thuật toán đầy đủ, hai lượt trung bình mẫu, oracle, hai trục thiết kế |
| TD(0) | B00–B08 | Chuyển mẫu, đích, thuật toán đầy đủ, cập nhật tại chỗ, toán tử Bellman và bước học |
| So sánh | C00–C07 | Đi bộ dài, chỉ số, phạm vi tác động, cơ chế chệch–phương sai |
| Tổng hợp | D00–D01 | Bốn ý và cầu nối điều khiển |
| Bài tập dọc | X07,X03,X04 | Giải thích kết quả, phép cập nhật TD, chệch–phương sai |

Tệp có 31 trang chính và 3 trang bài tập dọc. Tuyến lõi là 108 phút; vùng đệm 12 phút dành cho A06 và phần hiện dần về $\gamma=1$ ở B07. Nhánh bài tập dùng 30 phút.

## Ánh xạ nguồn

| Nguồn | Đích | Quyết định |
|---|---|---|
| tr. 1–14 | P00–P01 | Lược ôn tập Bài 04; giữ cầu nối mô hình đã biết/chưa biết |
| tr. 15–16 | P01–P02 | Giữ, bổ sung giả thiết và kiểu đại lượng |
| tr. 17–23 | A00–A08 | Giữ MC; thêm giao diện thuật toán; áp dụng trọn trung bình mẫu trước $\alpha$ hằng; đặt oracle sau ước lượng |
| tr. 24–29 | B00–B08 | Đưa chuyển mẫu trước công thức; thêm giao diện thuật toán, định nghĩa $T^\pi$ và Robbins–Monro theo số lần cập nhật |
| tr. 30–31 | C00–C05 | Sửa số mũ và giá trị $0{,}970299$, $-0{,}99$; giải thích cơ chế chệch–phương sai có điều kiện |
| tr. 32–33 | C06–D01 | Giữ phạm vi và cầu nối, không dạy điều khiển |
| hw05 B7/B3/B4 | X07/X03/X04 | Nhánh dọc tự đủ; X07 chuyển từ tính lặp sang giải thích cơ chế |

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

## Tài sản SVG

- `short-walk.svg`: môi trường ngắn và nhiễu hành động.
- `design-grid.svg`: ma trận hai trục của Monte Carlo.
- `mc-td-timeline.svg`: thời điểm cập nhật trên cùng lượt.
- `long-walk.svg`: chỉ số phần thưởng và số mũ chiết khấu.
