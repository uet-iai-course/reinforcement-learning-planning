# Bài 02 — Giao diện tác tử–môi trường

## Phạm vi và mục tiêu

- Nguồn chính: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 1–27.
- Nguồn bài tập: `RL-hk2-2025-2026/resources/hw02.pdf`, Bài 1, 2, 5, 6 và 10.
- Đối tượng: sinh viên đại học đã học học máy, học sâu và thuật toán.
- Phần trình chiếu chính: 120 phút, 36 trang; bài tập nằm ở nhánh dọc để dùng trong 30 phút chữa bài.
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

Bài có bảy mạch trình bày, trong đó mạch 1 mở bài và mạch 7 kết luận:

1. Định hướng: phạm vi, mục tiêu và bốn trục nội dung.
2. Giao diện tương tác: ranh giới tác tử–môi trường và chỉ số thời gian.
3. Tín hiệu học: ba nguồn tín hiệu, phụ thuộc dữ liệu và phản hồi trễ.
4. Thông tin: trạng thái, quan sát, tính Markov và quan sát một phần.
5. Vai trò quyết định: chính sách, phần thưởng tích lũy, hàm giá trị, mô hình, dự đoán và điều khiển.
6. Mê cung: đặc tả môi trường và hai giao diện quan sát.
7. Kết luận: tự kiểm tra, tuyến Bài 03 và nhánh bài tập.

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
| 9 | sửa | B04 | Không dùng $\pi$ và $G_t$ trước định nghĩa; thêm cầu nối tới phần hàm giá trị; giới hạn giả thuyết phần thưởng. |
| 10, 20 | gộp | D00 | Ba vai trò chỉ xuất hiện một lần; mô hình là tùy chọn. |
| 11 | bỏ | — | Trang chỉ có số trang. |
| 12–13 | bỏ | — | Phần thảo luận AGI và tranh luận ngoài lược đồ không còn trên slide; không gán vào C06/C07. |
| 14–15 | tách, sửa | A00, A02–A04 | Sửa vai trò và chỉ số $R_{t+1}$; đáp án A04 hiện bằng fragment. |
| 16 | sửa | C00 | Phân biệt $S_t,O_t,X_t$ và miền tương ứng. |
| 17 | tách, sửa | C02, C03 | Đưa ví dụ xe trước công thức; tiêu đề C03 là "Tính Markov theo trạng thái và hành động"; dùng $\mathcal H_t^S=h_t^S$ kết thúc ở $S_t=s$ và chỉ điều kiện trên biến cố có xác suất dương; notes phân biệt lịch sử trạng thái với lịch sử quan sát. |
| 18 | sửa | C04 | Quan sát đầy đủ không đồng nhất với định nghĩa MDP. |
| 19 | tách, sửa | C05, C06 | Giới thiệu đầy đủ tên POMDP trước khi dùng lịch sử/niềm tin. |
| 21 | tách | D02, D03 | Chính sách theo $X_t$ tổng quát; định nghĩa $\mathcal A(x)$ và chuẩn hóa. |
| 22 | tách, thêm | D04–D06 | Chốt $X_t=S_t$, chính sách Markov $\pi(a\mid s)$; đặt quỹ đạo thưởng cụ thể trước công thức $G_t$ và $v_\pi$; kiểm tra trực giác $\gamma=0,0{,}5,1$; notes nêu trường hợp tiếp diễn với tổng vô hạn, $\gamma<1$ dưới giả thiết phần thưởng bị chặn. |
| 23 | tách, sửa | D07, D07B | D07 dùng ví dụ $1/0$; D07B định nghĩa phân phối chuẩn hóa, $\mathcal R\subset\mathbb R$ và phân biệt $p$ với mô hình ước lượng $\hat p$. Tách để công thức không bị cắt ngang. |
| 24 | sửa, tách | D08, D09 | Bỏ $q_\pi$ chưa định nghĩa; phân biệt dự đoán với điều khiển; phát biểu giá trị $-7$ ghi $\gamma=1$ và nhiệm vụ kết thúc sau đúng 7 bước. |
| 25–26 | gộp, sửa | E00, E02 | Cố định bản đồ, tọa độ, tập hành động, thưởng khi vào đích và quy tắc va tường. |
| 27 | sửa, tách | C07, E03–E04 | Tách tính Markov khỏi việc tác tử biết mô hình; phân loại theo giao diện quan sát. |
| hw02 Bài 1 | giữ nguyên văn | X01 | Không thay nhiệm vụ cốt lõi. |
| hw02 Bài 2 | giữ nguyên văn | X02 | Không thay nhiệm vụ cốt lõi. |
| hw02 Bài 5 | giữ nhiệm vụ | X05 | Bài tập chính; nằm ở nhánh dọc, ngoài 120 phút. |
| hw02 Bài 6 | giữ nhiệm vụ | X06 | Bài tập chính; nằm ở nhánh dọc, ngoài 120 phút. |
| hw02 Bài 10 | giữ nhiệm vụ | X10 | Bài tập mở rộng; hợp lệ ngay sau topic 09, không cần $q_\pi$ hay Bellman. |
| trang 13 | chuyển, trả lời | D10 | Câu hỏi "mô hình thế giới" được trả lời sau khi định nghĩa mô hình ở D07; ghi rõ giới hạn dự báo cục bộ, sai số $\hat p$ và không suy diễn AGI. |

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
| $\mathcal R\subset\mathbb R$ | Tập giá trị phần thưởng; dùng trong điều kiện chuẩn hóa của mô hình. |
| $H_t$ | Lịch sử quan sát đến $O_t$. |
| $\mathcal H_t^S$ | Lịch sử trạng thái đến $S_t$; dùng riêng trong phát biểu Markov. |
| $\pi(a\mid x)$ | Xác suất chọn $a\in\mathcal A(x)$ khi $X_t=x$. |
| $G_t$ | Phần thưởng tích lũy có hệ số chiết khấu từ $R_{t+1}$. |
| $\gamma\in[0,1]$ | Hệ số giảm trọng số của phần thưởng ở xa. |
| $v_\pi(s)$ | Phần thưởng tích lũy kỳ vọng từ $s$ dưới chính sách Markov $\pi(a\mid s)$ trong phần D04–D09, nơi giả sử $X_t=S_t$. |
| $p(s',r\mid s,a)$ | Phân phối chung của trạng thái kế tiếp và phần thưởng trong trường hợp rời rạc; là động lực thật của môi trường, khác với mô hình ước lượng $\hat p$ của tác tử. |
| POMDP | Quá trình quyết định Markov quan sát một phần. |
| mô hình dự báo cục bộ có điều kiện | Mô hình của tác tử dự báo với từng cặp $(s,a)$: phân phối trạng thái và phần thưởng kế tiếp; khác "mô hình hoàn thiện về thế giới" ở phạm vi và độ tin cậy (xem D10). |
| dự đoán | Đánh giá một chính sách cố định. |
| điều khiển | Tìm hoặc cải thiện chính sách. |

## Ánh xạ note-topic-id → data-slide-id (hai chiều)

| note-topic-id | data-slide-id |
|---|---|
| `lec-02-topic-01` | B00, B02, B03, B04, B05 |
| `lec-02-topic-02` | A00, A02, A03, A04 |
| `lec-02-topic-03` | C00, C02, C03 |
| `lec-02-topic-04` | C04, C05, C06, C07 |
| `lec-02-topic-05` | D00 |
| `lec-02-topic-06` | D02, D03 |
| `lec-02-topic-07` | D04, D05, D06, D07, D07B |
| `lec-02-topic-08` | D08, D09 |
| `lec-02-topic-09` | E00, E02, E03, E04, E05 |
| `lec-02-topic-10` | A03, C02, C03 (cầu nối lịch sử → trạng thái Markov; không tạo C10) |
| `lec-02-topic-11` | D10 (một trang duy nhất, sau D07 trước D08) |
| `lec-02-topic-12` | Z00 (ghi chú đọc thêm và phân tuyến bài tập; không tạo trang riêng) |

Ánh xạ cho phép một trang hỗ trợ nhiều chủ đề liền kề; các mã P00–P02 là trang mở bài không gắn topic. Mỗi `data-slide-id` trong deck là duy nhất; topic-10 không tạo trang C10 vì nội dung cầu nối đã phủ trong A03 (lịch sử) và C02–C03 (tiêu chuẩn Markov).

Về thứ tự: deck giữ cụm topic-02 (giao diện tương tác, các trang A) trước topic-01 (tín hiệu học, các trang B), khác thứ tự note. Lý do: dựng ranh giới tác tử–môi trường và chỉ số thời gian trước, rồi mới so sánh ba tín hiệu học, để các so sánh tín hiệu có khung chỉ số đúng; thứ tự khác note nhưng không đổi logic nội dung.

## Tài liệu dùng để kiểm tra

- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, Chương 3.
- Silver, D., *Introduction to Reinforcement Learning*, Lecture 2 (https://www.davidsilver.uk/teaching/); phần Bellman của Lecture 2 thuộc Bài 03.
- `RL-hk2-2025-2026/resources/hw02.pdf`, Bài 1, 2, 5, 6 (bài tập chính) và Bài 10 (mở rộng).
- `2627-1/lecture-template.html` và `2627-1/lecture-style.css` cho cấu trúc và nền kỹ thuật.

## Điểm nối sang Bài 03

Bài 03 phân biệt chuỗi Markov, quá trình phần thưởng Markov và MDP; sau đó đóng gói $\mathcal S,\mathcal A,p,\gamma$ thành MDP và xây phương trình Bellman. E05 không lặp chi tiết tuyến này; Z00 là nơi mở bài kế tiếp. Nhánh dọc của Bài 02 chứa Bài 1, 2, 5, 6 (bài tập chính) và Bài 10 (mở rộng) của hw02; Bài 3, 4, 7, 8, 9 đòi hỏi MRP, $q_\pi$ hoặc Bellman, thuộc Bài 03 và sẽ được xử lý sau Bài 03. Phần Bellman của Silver Lecture 2 cũng bắt đầu từ Bài 03.
