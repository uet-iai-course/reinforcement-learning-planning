# Bài 07: Xấp xỉ hàm trong Học tăng cường

## Phạm vi

- Nguồn chính: `RL-hk2-2025-2026/lecture-07.pdf`, 45 trang.
- Nguồn bài tập: `RL-hk2-2025-2026/resources/hw07-function-approximation.pdf`, 3 trang, 8 bài.
- Đối tượng: sinh viên đã học MDP, MC, TD(0), SARSA và Q-learning dạng bảng.
- Tiên quyết đại số tuyến tính: tích vô hướng có trọng số (dạng $u^TDv$), phép chiếu trực giao lên không gian con và trị riêng của ma trận; sinh viên cần dùng chúng ở phần Bellman chiếu.
- Phần trình chiếu: 120 phút, gồm 111 phút cốt lõi và 9 phút linh hoạt.
- Chữa bài: 30 phút ở ba trang dọc `X01`–`X03`, ngoài 120 phút chính.
- Không có code demo trong nguồn.
- Bảng phân loại nguồn tr. 4 (actor-critic/policy methods) được bỏ riêng vì ngoài phạm vi bài; ba điểm đối chiếu thuật toán ở tr. 3 (loại mục tiêu, theo hay khác chính sách, cách cải thiện chính sách) được nêu ở `L07-02`.

## Mục tiêu

Sau bài học, sinh viên có thể (khớp mặt trang `L07-03` và mục 1.2 của ghi chú bài giảng):

1. viết xấp xỉ tuyến tính $\hat v$, $\hat q$ theo đặc trưng, nêu miền và kích thước;
2. tính cập nhật Monte Carlo, TD(0) và Sarsa tuyến tính trên ví dụ số, gồm Bài 7 và Bài 8 của phiếu bài tập;
3. phân biệt gradient đầy đủ (Monte Carlo) với bán gradient (TD);
4. nêu điểm cố định Bellman chiếu $\Phi w=\Pi_D T_\pi(\Phi w)$ cùng giả thiết hội tụ;
5. phân biệt mục tiêu Sarsa và Q-learning; nhận diện bộ ba bất ổn (xấp xỉ hàm, bootstrap, học khác chính sách) trong một quy tắc cập nhật.

## Dàn ý theo sáu mạch và thời lượng

Sáu mạch chứa bảy cụm khái niệm: cụm so sánh MC–TD nằm cuối M4, nên không cần mạch thứ bảy.

| Mạch | Trang | Nội dung | Cốt lõi | Linh hoạt |
|---|---|---|---:|---:|
| M1 Mở đầu và đích học tập | `L07-01`–`L07-03` | Cầu nối dạng bảng, ba trục phân tích và kết quả học tập | 7 | 0 |
| M2 Nhu cầu xấp xỉ, đặc trưng, biểu diễn | `L07-04`–`L07-11` | Vấn đề bảng tra, chia sẻ tham số, ví dụ, tuyến tính và giới hạn đặc trưng | 21 | 2 |
| M3 MC tuyến tính | `L07-12`–`L07-17` | Phân loại đích, return, ví dụ, gradient, thuật toán và điều kiện | 19 | 2 |
| M4 TD, Bellman chiếu và so sánh MC–TD | `L07-18`–`L07-25` | Bootstrap, ví dụ số, bán gradient, thuật toán TD(0), phép chiếu, hội tụ và đối chiếu hai đích | 30 | 3 |
| M5 Điều khiển và SARSA tuyến tính | `L07-26`–`L07-30` | Giá trị hành động, chuỗi ví dụ, SARSA và cập nhật số | 18 | 1 |
| M6 Q-learning, deadly triad, phạm vi, kết luận | `L07-31`–`L07-36` | Đích Q-learning, bộ ba bất ổn, phạm vi lý thuyết, kết luận và kiểm tra | 16 | 1 |
| Tổng | 37 trang chính |  | 111 | 9 |
| Chữa bài (dọc, ngoài 120 phút) | `X01`–`X03` | Đạo hàm MC, MC tuần tự, SARSA tuần tự | 30 | 0 |

Tổng kiểm tra: $7+23+21+(30+3)+19+17=120$ phút chính; $30+3$ là hai cụm TD và so sánh MC–TD cùng nằm trong M4. Chữa bài $8+10+12=30$ phút. Ngày 02-10-2026 tách thuật toán TD(0) sang `L07-20b`, lấy 1 phút linh hoạt của M4 từ phần trao đổi ở `L07-23` (6 → 5 phút); tổng mạch và tổng 120 phút không đổi.

## Ánh xạ nguồn

| Trang nguồn | Quyết định | Trang đích | Lý do |
|---:|---|---|---|
| 1–4 | giữ, gộp | `L07-01`–`L07-03` | Giữ tên bài, phạm vi và kết quả học tập; ba điểm đối chiếu tr. 3 đưa vào `L07-02`; bỏ trang mục lục lặp. |
| 5–20 | gộp, sửa | `L07-02` | Chỉ tóm tắt điều kiện hội tụ dạng bảng (thăm mọi cặp vô hạn lần, GLIE, Robbins–Monro); không lặp phác thảo chứng minh, vì bước chuyển từ chính sách cố định sang chính sách thay đổi trong nguồn chưa đủ chặt. |
| 21 | bỏ | — | Trang mục lục trung gian không tạo bước kiến thức. |
| 22–23 | giữ, tách | `L07-04`–`L07-06` | Tách vấn đề, mô hình tham số và cơ chế chia sẻ tham số. |
| 24–26 | giữ, gộp | `L07-08`, `L07-34`, `L07-36` | Dạy tuyến tính trong bài; chỉ nêu ranh giới với mô hình phi tuyến. |
| 27 | giữ, sửa | `L07-12`–`L07-13`, `L07-18` | Phân biệt rõ đích MC không phụ thuộc $w$ và đích TD phụ thuộc $w$. |
| 28–30 | giữ, vẽ lại | `L07-09` | Thay ảnh miền ứng dụng bằng SVG khái niệm, không dùng ảnh raster. |
| 31 | giữ, tách | `L07-09`–`L07-11`, `L07-27` | Giữ vector điều hướng và mã hóa bốn khối $[\phi(s);e_a;\phi(s)\otimes e_a;1]$ của nguồn; xác định đặc trưng ba chiều của chuỗi là một mã hóa khác. |
| 32 | sửa, tách | `L07-12`, `L07-15`, `L07-20` (câu hỏi "vì sao gọi là bán gradient") | Đặt ví dụ trước hình thức; MC là gradient đầy đủ, TD mới dùng bán gradient khi bỏ đạo hàm qua bootstrap. |
| 33–34 | giữ, sửa | `L07-13`–`L07-17` | Bổ sung giao diện thuật toán và điều kiện phân phối lấy mẫu. |
| 35–36 | giữ, mở rộng | `L07-18`–`L07-24` | Đặt hình học trước đại số; bổ sung điều kiện trực giao, $A$, $b$, $D$, $\Phi$, $P_\pi$, $r_\pi$ và giả thiết. |
| 37 | giữ, sửa | `L07-25` | Giữ so sánh có thể kiểm chứng; lược tuyên bố hiệu năng quá rộng. |
| 38–39 | giữ, sắp lại | `L07-26`, `L07-28`–`L07-31` | Đặt SARSA control trước; chỉ dùng Q-learning để phân biệt quy tắc đích và miền cực đại. |
| 40 | giữ, sửa | `L07-27`, `L07-30`, `X02`, `X03` | Nêu $\gamma=1$, lượt dài tối đa ba bước và vai trò chỉ sinh dữ liệu của $\varepsilon$ khi chuỗi đã cho. |
| 41 | giữ, sửa | `L07-32`–`L07-33` | Deadly triad có thể gây phân kỳ, không phải luôn gây phân kỳ. |
| 42–43 | gộp | `L07-34` | Không dạy chi tiết LSVI vì nguồn không đủ thiết lập; giữ ranh giới lý thuyết. |
| 44 | bỏ một phần | `L07-35`–`L07-36` | Bỏ bound $\widetilde O(d/\varepsilon^2)$ do thiếu mô hình và thước đo sai số. |
| 45 | giữ trong ghi chú | nhiều trang | Nguồn được đặt sát mệnh đề thay vì một trang tài liệu tham khảo dày. |
| HW 1–3 | chuyển sang tự học | `note-for-author.md`, ghi chú `L07-36` | Câu trình bày lặp với nội dung chính. |
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

## Danh mục đầy đủ 40 mã trang

M1: `L07-01`, `L07-02`, `L07-03`. M2: `L07-04`, `L07-05`, `L07-06`, `L07-07`, `L07-08`, `L07-09`, `L07-10`, `L07-11`. M3: `L07-12`, `L07-13`, `L07-14`, `L07-15`, `L07-16`, `L07-17`. M4: `L07-18`, `L07-19`, `L07-20`, `L07-20b`, `L07-21`, `L07-22`, `L07-23`, `L07-24`, `L07-25`. M5: `L07-26`, `L07-27`, `L07-28`, `L07-30`, `L07-29` (thứ tự trình chiếu: một bước số trước thuật toán). M6: `L07-31`, `L07-32`, `L07-33`, `L07-34`, `L07-35`, `L07-36`. Dọc: `X01`, `X02`, `X03`.

## Ánh xạ hai chiều ghi chú–trang chiếu

Mỗi trang trong 40 trang chiếu (`L07-01`–`L07-36`, `L07-20b` và `X01`–`X03`) thuộc đúng một chủ đề; cả 16 chủ đề đều có trang tương ứng. Bảng dưới đây đối chiếu trực tiếp với thuộc tính `data-note-topic-id` trong HTML.

| Topic | Trang chiếu |
|---|---|
| `lec-07-topic-13` | `L07-01`, `L07-02`, `L07-03` |
| `lec-07-topic-01` | `L07-04` |
| `lec-07-topic-02` | `L07-05`, `L07-06` |
| `lec-07-topic-03` | `L07-07`, `L07-08` |
| `lec-07-topic-04` | `L07-09`, `L07-10`, `L07-11` |
| `lec-07-topic-05` | `L07-12` |
| `lec-07-topic-06` | `L07-13`, `L07-14`, `L07-15`, `L07-16` |
| `lec-07-topic-15` | `L07-17`, `X01` |
| `lec-07-topic-07` | `L07-18`, `L07-19`, `L07-20`, `L07-20b` |
| `lec-07-topic-08` | `L07-21`, `L07-22`, `L07-23`, `L07-24` |
| `lec-07-topic-09` | `L07-25` |
| `lec-07-topic-10` | `L07-26`, `L07-27`, `L07-28`, `L07-30`, `L07-29` |
| `lec-07-topic-11` | `L07-31`, `L07-32`, `L07-33` |
| `lec-07-topic-14` | `L07-34` |
| `lec-07-topic-12` | `L07-35`, `L07-36` |
| `lec-07-topic-16` | `X02`, `X03` |

## Tài sản trực quan

Bảy SVG được vẽ lại trong `2627-1/img/lec-07/`:

1. `tabular-vs-parametric.svg`;
2. `shared-parameter-effect.svg`;
3. `linear-pipeline.svg`;
4. `feature-domains.svg`;
5. `projected-bellman.svg`;
6. `five-state-features.svg`;
7. `deadly-triad.svg`.

Ngày 02-10-2026 xóa `mc-vs-td-targets.svg`: hình không đọc được khi đặt cùng bảng sáu hàng ở `L07-25`, nội dung trùng hàng "Mục tiêu" của bảng; tệp vẫn còn trong lịch sử git.

Không dùng ảnh raster, tài nguyên mạng hoặc tài sản ngoài bài.
