# Bài 07: Xấp xỉ hàm trong Học tăng cường

## Phạm vi

- Nguồn chính: `RL-hk2-2025-2026/lecture-07.pdf`, 45 trang.
- Nguồn bài tập: `RL-hk2-2025-2026/resources/hw07-function-approximation.pdf`, 3 trang, 8 bài.
- Đối tượng: sinh viên đã học MDP, MC, TD(0), SARSA và Q-learning dạng bảng.
- Phần trình chiếu: 120 phút, gồm 110 phút cốt lõi và 10 phút linh hoạt.
- Chữa bài: 30 phút ở ba trang dọc `X01`–`X03`.
- Không có code demo trong nguồn.

## Mục tiêu

Sau bài học, sinh viên có thể:

1. giải thích giới hạn của bảng tra và cơ chế tổng quát hóa qua tham số dùng chung;
2. định nghĩa xấp xỉ tuyến tính cho $v_\pi$ và $q_\pi$, gồm miền và kích thước;
3. phân biệt gradient đầy đủ của MC với bán gradient của TD;
4. triển khai MC, TD(0), SARSA tuyến tính và phân biệt đích Q-learning;
5. giải thích điểm cố định $\Phi w=\Pi_D T_\pi(\Phi w)$ cùng các giả thiết;
6. nhận diện xấp xỉ hàm, bootstrap và học khác chính sách trong deadly triad;
7. tự tính các cập nhật tuần tự trong Bài 7 và Bài 8 của phiếu bài tập.

## Dàn ý và thời lượng

| Phần | Trang | Nội dung | Cốt lõi | Linh hoạt |
|---|---|---|---:|---:|
| Định hướng | `L07-01`–`L07-03` | Cầu nối dạng bảng và kết quả học tập | 7 | 0 |
| Nhu cầu và biểu diễn | `L07-04`–`L07-11` | Vấn đề bảng tra, chia sẻ tham số, ví dụ, tuyến tính và giới hạn đặc trưng | 21 | 2 |
| Đích học và Monte Carlo | `L07-12`–`L07-17` | Phân loại đích, return, ví dụ, gradient, thuật toán và điều kiện | 19 | 2 |
| TD và Bellman chiếu | `L07-18`–`L07-24` | Bootstrap, ví dụ số, bán gradient, hướng trung bình, phép chiếu và hội tụ | 26 | 4 |
| So sánh MC–TD | `L07-25` | Đối chiếu hai đích và đối tượng phân tích | 3 | 0 |
| Điều khiển | `L07-26`–`L07-30` | Giá trị hành động, chuỗi ví dụ, SARSA và cập nhật số | 18 | 1 |
| Khác chính sách, bất ổn và kết | `L07-31`–`L07-36` | Q-learning, deadly triad, phạm vi lý thuyết và kiểm tra | 16 | 1 |
| Tổng | 36 trang chính |  | 110 | 10 |
| Chữa bài | `X01`–`X03` | Đạo hàm MC, MC tuần tự, SARSA tuần tự | 30 | 0 |

## Ánh xạ nguồn

| Trang nguồn | Quyết định | Trang đích | Lý do |
|---:|---|---|---|
| 1–4 | giữ, gộp | `L07-01`, `L07-03` | Giữ tên bài, phạm vi và kết quả học tập; bỏ trang mục lục lặp. |
| 5–20 | gộp, sửa | `L07-02` | Hội tụ dạng bảng đã có ở Bài 06; phác thảo nguồn chuyển từ chính sách cố định sang chính sách thay đổi chưa đủ chặt. |
| 21 | bỏ | — | Trang mục lục trung gian không tạo bước kiến thức. |
| 22–23 | giữ, tách | `L07-04`–`L07-06` | Tách vấn đề, mô hình tham số và cơ chế chia sẻ tham số. |
| 24–26 | giữ, gộp | `L07-08`, `L07-34`, `L07-36` | Dạy tuyến tính trong bài; chỉ nêu ranh giới với mô hình phi tuyến. |
| 27 | giữ, sửa | `L07-12`–`L07-13`, `L07-18` | Phân biệt rõ đích MC không phụ thuộc $w$ và đích TD phụ thuộc $w$. |
| 28–30 | giữ, vẽ lại | `L07-09` | Thay ảnh miền ứng dụng bằng SVG khái niệm, không dùng ảnh raster. |
| 31 | sửa, tách | `L07-10`–`L07-11`, `L07-27` | Dùng $e_a\otimes\phi(s)$ cho mã hóa khối; xác định đặc trưng ba chiều của chuỗi là một mã hóa khác. |
| 32 | sửa, tách | `L07-12`, `L07-15`, `L07-20` | Đặt ví dụ trước hình thức; MC là gradient đầy đủ, TD mới dùng bán gradient khi bỏ đạo hàm qua bootstrap. |
| 33–34 | giữ, sửa | `L07-13`–`L07-17` | Bổ sung giao diện thuật toán và điều kiện phân phối lấy mẫu. |
| 35–36 | giữ, mở rộng | `L07-18`–`L07-24` | Đặt hình học trước đại số; bổ sung điều kiện trực giao, $A$, $b$, $D$, $\Phi$, $P_\pi$, $r_\pi$ và giả thiết. |
| 37 | giữ, sửa | `L07-25` | Giữ so sánh có thể kiểm chứng; lược tuyên bố hiệu năng quá rộng. |
| 38–39 | giữ, sắp lại | `L07-26`, `L07-28`–`L07-31` | Đặt SARSA control trước; chỉ dùng Q-learning để phân biệt quy tắc đích và miền cực đại. |
| 40 | giữ, sửa | `L07-27`, `L07-30`, `X02`, `X03` | Nêu $\gamma=1$, chân trời cưỡng bức và vai trò chỉ sinh dữ liệu của $\varepsilon$ khi chuỗi đã cho. |
| 41 | giữ, sửa | `L07-32`–`L07-33` | Deadly triad có thể gây phân kỳ, không phải luôn gây phân kỳ. |
| 42–43 | gộp | `L07-34` | Không dạy chi tiết LSVI vì nguồn không đủ thiết lập; giữ ranh giới lý thuyết. |
| 44 | bỏ một phần | `L07-35`–`L07-36` | Bỏ bound $\widetilde O(d/\varepsilon^2)$ do thiếu mô hình và thước đo sai số. |
| 45 | giữ trong ghi chú | nhiều trang | Nguồn được đặt sát mệnh đề thay vì một trang tài liệu tham khảo dày. |
| HW 1–3 | chuyển sang tự học | `note-for-author.md` | Câu trình bày lặp với nội dung chính. |
| HW 4 | giữ | `X01` | Bài đạo hàm trực tiếp. |
| HW 5–6 | linh hoạt/tự học | `L07-21`–`L07-24`, `note-for-author.md` | Nội dung đã được giải thích trong phần Bellman chiếu và điều kiện bước học. |
| HW 7 | giữ, tính lại | `X02` | Chữa cập nhật MC tuần tự. |
| HW 8 | giữ, tính lại | `L07-30`, `X03` | Chuẩn bị một bước trong bài chính và chữa đủ ba bước. |

## Thuật ngữ và ký hiệu

| Ký hiệu | Nghĩa và miền |
|---|---|
| $x(s)\in\mathbb R^d$ | vector đặc trưng trạng thái |
| $x(s,a)\in\mathbb R^d$ | vector đặc trưng cặp trạng thái–hành động |
| $w\in\mathbb R^d$ | vector tham số dùng chung |
| $\hat v(s,w)=x(s)^Tw$ | xấp xỉ giá trị trạng thái |
| $\hat q(s,a,w)=x(s,a)^Tw$ | xấp xỉ giá trị hành động |
| $\mu$ | phân phối trọng số hoặc lấy mẫu cố định của mục tiêu MC |
| $d_\pi$ | phân phối dừng của chuỗi theo chính sách $\pi$ |
| $D=\operatorname{diag}(d_\pi)$ | ma trận trọng số cho tích vô hướng và phép chiếu |
| $\Phi\in\mathbb R^{|\mathcal S|\times d}$ | ma trận có hàng $s$ là $x(s)^T$ |
| $P_\pi$, $r_\pi$ | ma trận chuyển và vector phần thưởng kỳ vọng theo $\pi$ |
| $T_\pi v=r_\pi+\gamma P_\pi v$ | toán tử Bellman theo chính sách |
| $\Pi_D$ | phép chiếu trực giao lên $\operatorname{col}(\Phi)$ theo chuẩn $D$ |
| $G_t$ | return từ thời điểm $t$ đến cuối lượt |
| $\delta_t$ | sai số TD của một chuyển tiếp |

## Tài sản trực quan

Tám SVG được vẽ lại trong `2627-1/img/lec-07/`:

1. `tabular-vs-parametric.svg`;
2. `shared-parameter-effect.svg`;
3. `linear-pipeline.svg`;
4. `feature-domains.svg`;
5. `projected-bellman.svg`;
6. `mc-vs-td-targets.svg`;
7. `five-state-features.svg`;
8. `deadly-triad.svg`.

Không dùng ảnh raster, tài nguyên mạng hoặc tài sản ngoài bài.
