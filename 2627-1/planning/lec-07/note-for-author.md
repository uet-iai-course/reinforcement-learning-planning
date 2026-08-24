# Ghi chú cho người soạn Bài 07

Tệp này giữ các chỉ dẫn biên tập không được đưa lên mặt trang chiếu hoặc vào ghi chú diễn giả.

## Nhịp giảng

- Giữ `L07-02` ngắn. Không giảng lại chứng minh hội tụ MC control hoặc SARSA dạng bảng.
- Dùng `L07-06` để chuẩn bị cả lợi ích tổng quát hóa và rủi ro giao thoa. Hai ý này phải đi cùng nhau.
- Ở `L07-12`, yêu cầu sinh viên xác định đích có phụ thuộc $w$ trước khi dùng từ “gradient” hay “bán gradient”. Giữ ví dụ `L07-14` trước phép đạo hàm `L07-15`.
- Ở TD, tính trọn mẫu `L07-19` trước khi viết bán gradient tổng quát ở `L07-20`. Kiểm tra cả hai dự đoán dùng cùng $w_t$.
- Ở Bellman chiếu, giữ đúng thứ tự: hình học `L07-21` → trực giao và $Aw=b$ ở `L07-22` → điểm cố định `L07-23`.
- Giữ SARSA trước Q-learning. Nếu đổi thứ tự, cầu nối từ TD dự đoán sang điều khiển sẽ mất.
- Không mở rộng `L07-34` thành bài giảng về LSVI hoặc mạng nơ-ron. Phần đó cần nguồn và giả thiết riêng.

## Điểm dễ nói sai

- Phát biểu đúng là $\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s)$ dưới chính sách cố định và khi return tồn tại; không suy ra $w$ hữu hạn mẫu không chệch.
- Dùng $\mu$ cho phân phối của mục tiêu MC và $d_\pi$ cho phân phối dừng trong TD.
- MC dùng gradient đầy đủ của mất mát mẫu vì $G_t$ không phụ thuộc $w$.
- TD dùng bán gradient vì bỏ đường đạo hàm qua dự đoán bootstrap trong đích.
- Điểm cố định TD là $\Phi w=\Pi_DT_\pi(\Phi w)$, không nhất thiết là phép chiếu trực tiếp của $v_\pi$.
- Bảo đảm TD tuyến tính được nêu trong bài là theo chính sách, với chính sách cố định, chuỗi dừng và hệ trung bình ổn định. Đủ hạng chủ yếu bảo đảm nghiệm tham số duy nhất.
- SARSA control dùng chính sách $\varepsilon$-greedy hiện hành suy ra từ $\hat q(\cdot,\cdot,w)$; sau cập nhật $w$, chính sách có thể đổi.
- Deadly triad là cảnh báo cho thiết lập học giá trị TD có bootstrap, xấp xỉ hàm và lấy mẫu khác chính sách; không kết luận mọi thuật toán hoặc Deep Q-Network đều phân kỳ.
- Một quỹ đạo cố định trong Bài 7 chỉ minh họa cập nhật giá trị hành động MC. Chưa có bước cải thiện chính sách nên chưa phải một vòng MC control đầy đủ.

## Đáp số cần giữ cố định

- Bài 7: $G=(998,999,1000)$; $w_{\mathrm{cuối}}=(381.81,162.71,160.71)^T$; các dự đoán $(1468.85,1087.04,705.23)$ theo thứ tự $(D,0),(C,0),(B,0)$.
- Bài 8: $w_1=(-0.2,0.6,-1.4)^T$, $w_2=(-0.68,0.84,-1.64)^T$, $w_3=(8.032,-2.064,1.264)^T$; các dự đoán cuối $(23.296,19.392,27.424)$ theo thứ tự $(D,0),(C,1),(D,1)$.
- Cả hai bài dùng $\gamma=1$. Trong Bài 8, $\varepsilon=0.25$ không tham gia số học vì chuỗi hành động đã được cho.

## Phần có thể rút khi thiếu thời gian

- Rút phần thảo luận sau ví dụ ở `L07-16` và điều kiện lấy mẫu Markov ở `L07-17`.
- Ở `L07-22`, có thể chỉ nêu điều kiện trực giao rồi chỉ ra hai cụm $A$ và $b$; không triển khai phép nhân ma trận trên lớp.
- Rút câu hỏi mở ở `L07-33` và bảng phân loại ở `L07-34` xuống một ví dụ mỗi hàng.
- Không bỏ `L07-12`, `L07-14`, `L07-15`, `L07-19`, `L07-20`, `L07-23`, `L07-28`, `L07-31` hoặc `L07-32`; chúng giữ ví dụ trước hình thức và các phân biệt dễ nhầm.

## Bài tự học

- Phiếu bài tập Bài 1–3: dùng để ôn giới hạn bảng tra, so sánh MC–TD và deadly triad.
- Bài 5: yêu cầu sinh viên hoàn chỉnh phép biến đổi từ $\mathbb E[\delta_tx(S_t)]=b-Aw$ đến phương trình Bellman chiếu.
- Bài 6: yêu cầu giải thích riêng vai trò của hai tổng Robbins–Monro.

## Kiểm tra biên tập

- Không thêm mã trang, nhãn phân tuyến hoặc thời lượng vào mặt trang và ghi chú.
- Không dùng “bán gradient MC”.
- Phân biệt mã hóa khối $e_a\otimes\phi(s)$ ở `L07-10` với đặc trưng ba chiều được thiết kế trực tiếp cho $(s,a)$ ở `L07-27`.
- Với giá trị hành động, cập nhật tuyến tính dùng $x(S_t,A_t)$, không dùng $x(S_t)$.
- Nếu sửa một công thức TD hoặc SARSA, phải tính lại toàn bộ ví dụ số phụ thuộc công thức đó.
- Nội dung hiển thị và ghi chú đã được viết bằng câu ngắn, trực tiếp; khi sửa, kiểm lại theo `no-ai-slop/eval.md` và giữ thuật ngữ nhất quán theo mạch Quill.
