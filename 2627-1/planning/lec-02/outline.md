# Bài 02 — Giao diện tác tử–môi trường

## Phạm vi và mục tiêu

- Nguồn chính: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 1–27.
- Nguồn bài tập: `RL-hk2-2025-2026/resources/hw02.pdf`, nguyên văn Bài 1–2.
- Đối tượng: sinh viên đại học đã học học máy, học sâu và thuật toán.
- Phần trình chiếu chính: 120 phút, 34 trang; hai bài tập nằm ở nhánh dọc để dùng trong 30 phút chữa bài.
- Điểm dừng: giao diện tác tử–môi trường, trạng thái và quan sát, tính Markov, ba vai trò của tác tử và ví dụ mê cung. Định nghĩa đầy đủ MDP bắt đầu ở Bài 03.

Sau bài học, sinh viên có thể:

1. viết đúng thứ tự $O_t,A_t,R_{t+1},O_{t+1}$;
2. phân biệt trạng thái môi trường $S_t$, quan sát $O_t$ và biểu diễn $X_t$;
3. phát biểu tính Markov bằng lịch sử trạng thái và hành động;
4. phân biệt quan sát đầy đủ với quan sát một phần;
5. định nghĩa chính sách trên biểu diễn quyết định, hàm giá trị và mô hình môi trường;
6. phân biệt bài toán dự đoán với điều khiển;
7. mô hình hóa mê cung bằng trạng thái, hành động, phần thưởng, quan sát và điều kiện dừng.

## Dàn ý

1. Giao diện tác tử–môi trường và chỉ số thời gian.
2. Tín hiệu học, phụ thuộc dữ liệu và phản hồi trễ.
3. Trạng thái, quan sát, tính Markov và POMDP.
4. Chính sách, phần thưởng tích lũy, hàm giá trị, mô hình, dự đoán và điều khiển.
5. Mê cung cố định và hai giao diện quan sát.

## Ánh xạ nguồn

| Trang nguồn | Quyết định | Trang đích | Lý do |
|---:|---|---|---|
| 1 | sửa | P00 | Cập nhật metadata và giới hạn thành Bài 02. |
| 2 | tách | P01, P02 | Tách mục tiêu đo được khỏi bản đồ nội dung. |
| 3 | gộp | P01, Z00 | Trang rà bài không có nội dung; thay bằng mục tiêu và tự kiểm tra. |
| 4 | sửa | A00 | Xác định ranh giới tác tử–môi trường. |
| 5 | bỏ | — | Hình thành tựu không kèm mệnh đề hoặc số liệu cần dạy. |
| 6 | bỏ | — | Nhận định về AGI không có căn cứ đủ trong nguồn. |
| 7 | gộp | B00 | So sánh ba tín hiệu bằng một hình; bỏ trang mở phần lặp. |
| 8 | tách | B02, B03 | Tách phụ thuộc dữ liệu khỏi phản hồi trễ. |
| 9 | sửa | B04 | Không dùng $\pi$ và $G_t$ trước định nghĩa; giới hạn giả thuyết phần thưởng. |
| 10, 20 | gộp | D00 | Ba vai trò chỉ xuất hiện một lần; mô hình là tùy chọn. |
| 11 | bỏ | — | Trang chỉ có số trang. |
| 12–13 | chuyển, lược | C06, C07 | Giữ biểu diễn và bộ nhớ; bỏ tranh luận AGI. |
| 14–15 | tách, sửa | A00, A02–A04 | Sửa vai trò và chỉ số $R_{t+1}$; đáp án A04 hiện bằng fragment. |
| 16 | sửa | C00 | Phân biệt $S_t,O_t,X_t$ và miền tương ứng. |
| 17 | tách, sửa | C02, C03 | Đưa ví dụ xe trước công thức; dùng $\mathcal H_t^S=h_t^S$ kết thúc ở $S_t=s$ và chỉ điều kiện trên biến cố có xác suất dương. |
| 18 | sửa | C04 | Quan sát đầy đủ không đồng nhất với định nghĩa MDP. |
| 19 | tách, sửa | C05, C06 | Giới thiệu đầy đủ tên POMDP trước khi dùng lịch sử/niềm tin. |
| 21 | tách | D02, D03 | Chính sách theo $X_t$ tổng quát; định nghĩa $\mathcal A(x)$ và chuẩn hóa. |
| 22 | tách, thêm | D04–D06 | Chốt $X_t=S_t$, chính sách Markov $\pi(a\mid s)$; đặt quỹ đạo thưởng cụ thể trước công thức $G_t$ và $v_\pi$. |
| 23 | sửa | D07 | Đặt chuyển tiếp mê cung tất định xác suất $1/0$ trước mô hình rời rạc và điều kiện chuẩn hóa. |
| 24 | sửa, tách | D08, D09 | Bỏ $q_\pi$ chưa định nghĩa; phân biệt dự đoán với điều khiển. |
| 25–26 | gộp, sửa | E00, E02 | Cố định bản đồ, tọa độ, tập hành động, thưởng khi vào đích và quy tắc va tường. |
| 27 | sửa, tách | C07, E03–E04 | Tách tính Markov khỏi việc tác tử biết mô hình; phân loại theo giao diện quan sát. |
| hw02 Bài 1 | giữ nguyên văn | X01 | Không thay nhiệm vụ cốt lõi. |
| hw02 Bài 2 | giữ nguyên văn | X02 | Không thay nhiệm vụ cốt lõi. |

## Tài sản SVG

| Tệp | Vai trò |
|---|---|
| `agent-environment-loop.svg` | Vòng tương tác với chỉ số đúng. |
| `interaction-timeline.svg` | Thứ tự $O_t,A_t,R_{t+1},O_{t+1}$. |
| `learning-signals.svg` | Ba nguồn tín hiệu học. |
| `delayed-feedback.svg` | Phản hồi trễ và quy công trạng. |
| `state-observation.svg` | Phân biệt $S_t,O_t,X_t$. |
| `markov-summary.svg` | Ví dụ hai xe cùng vị trí nhưng khác vận tốc. |
| `observability.svg` | Quan sát xác định trạng thái và quan sát nhập nhằng. |
| `rl-components.svg` | Chính sách, giá trị và mô hình tùy chọn; không dùng $q_\pi$. |
| `prediction-control.svg` | Dự đoán giữ $\pi$; điều khiển cải thiện $\pi$. |
| `maze-mdp.svg` | Mê cung cố định và quy ước thưởng. |
| `maze-observations.svg` | Tọa độ so với ảnh cục bộ. |

## Thuật ngữ và ký hiệu

| Ký hiệu/thuật ngữ | Nghĩa và quy ước |
|---|---|
| $S_t\in\mathcal S$ | Trạng thái môi trường ở bước $t$. |
| $O_t\in\mathcal O$ | Quan sát tác tử nhận ở bước $t$. |
| $X_t\in\mathcal X$ | Biểu diễn dùng để quyết định; trường hợp đầy đủ có thể chọn $X_t=S_t$. |
| $A_t\in\mathcal A(X_t)$ | Hành động hợp lệ tại biểu diễn hiện tại. |
| $R_{t+1}\in\mathbb R$ | Phần thưởng sinh sau $A_t$. |
| $H_t$ | Lịch sử quan sát đến $O_t$. |
| $\mathcal H_t^S$ | Lịch sử trạng thái đến $S_t$; dùng riêng trong phát biểu Markov. |
| $\pi(a\mid x)$ | Xác suất chọn $a\in\mathcal A(x)$ khi $X_t=x$. |
| $G_t$ | Phần thưởng tích lũy có hệ số chiết khấu từ $R_{t+1}$. |
| $\gamma\in[0,1]$ | Hệ số giảm trọng số của phần thưởng ở xa. |
| $v_\pi(s)$ | Phần thưởng tích lũy kỳ vọng từ $s$ dưới chính sách Markov $\pi(a\mid s)$ trong phần D04–D09, nơi giả sử $X_t=S_t$. |
| $p(s',r\mid s,a)$ | Phân phối chung của trạng thái kế tiếp và phần thưởng trong trường hợp rời rạc. |
| POMDP | Quá trình quyết định Markov quan sát một phần. |
| dự đoán | Đánh giá một chính sách cố định. |
| điều khiển | Tìm hoặc cải thiện chính sách. |

## Tài liệu dùng để kiểm tra

- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, Chương 3.
- `RL-hk2-2025-2026/resources/hw02.pdf`, Bài 1–2.
- `2627-1/lecture-template.html` và `2627-1/lecture-style.css` cho cấu trúc và nền kỹ thuật.

## Điểm nối sang Bài 03

Bài 03 phân biệt chuỗi Markov, quá trình phần thưởng Markov và MDP; sau đó đóng gói $\mathcal S,\mathcal A,p,\gamma$ thành MDP và xây phương trình Bellman.
