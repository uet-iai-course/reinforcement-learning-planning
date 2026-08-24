# Dàn ý Bài 04: Giải MDP bằng quy hoạch động

## Mục tiêu và phạm vi

Sinh viên có thể: liên hệ $v_*$ với $q_*$; viết Bellman tối ưu cho giá trị trạng thái và giá trị hành động; trích chính sách tham lam; thực hiện đánh giá, cải thiện, lặp chính sách và lặp giá trị; giải thích điều kiện hội tụ; chuyển phần dư Bellman thành chặn sai số và mất mát chính sách.

Tuyến chính gồm 38 trang, thiết kế cho 120 phút kể cả tương tác ngắn. Bốn trang bài tập dọc dùng cho 30 phút còn lại. Phạm vi là MDP hữu hạn, mô hình đã biết, phần thưởng bị chặn và $0\le\gamma<1$. Không dạy Monte Carlo, sai phân thời gian, Q-learning hoặc mã nguồn.

## Các phần

| Phần | Trang | Nội dung |
|---|---|---|
| Định hướng | P00–P02 | Đầu vào, đầu ra, giả thiết, không gian giá trị và chuẩn vô cùng |
| Bellman tối ưu | A02,A08,A00,A01,A03,A09,A05,A06 | Ví dụ tất định, $q_*$, $v_*$, $T^\pi$, $T_*$, tham lam và chu trình DP |
| Lặp chính sách | B00–B06,B08 | Ví dụ hai trạng thái, đánh giá, cải thiện và PI chính xác |
| Lặp giá trị | C00–C09 | Gridworld, lượt quét, VI, phần dư, chi phí và bất đồng bộ |
| Bảo đảm và giới hạn | D00–D08 | Tính co, tồn tại chính sách tối ưu, chặn phần dư, CartPole và tổng kết |
| Bài tập dọc | X09,X06,X04,X07 | Bài 9, 6, 4 và 7 của `hw3.pdf` |

## Ánh xạ nguồn

| Nguồn | Đích | Quyết định |
|---|---|---|
| 1–4 | P00–P02 | Giữ; bổ sung $\mathcal V$ và chuẩn vô cùng trước khi dùng. |
| 5–10 | A02,A08,A00,A01,A03,A09 | Đặt ví dụ tất định trước hình thức; dùng $\sup_\pi$; bổ sung $q_*$, Bellman $q_*$ và greedy. |
| 11–15 | A05–A06,B04–B05 | Gộp trang mục lục; thêm chặn sai số đánh giá và điều kiện công bằng. |
| 16–21 | B00–B06,B08 | Giữ ví dụ; thêm $q_{\pi_1}(s_0,b)=27$; chỉ giữ PI chính xác có đặc tả tái lập. |
| 22–29 | C00–C09 | Đưa Gridworld và lượt đầu trước VI; tách lượt cập nhật khỏi lượt kiểm phần dư; ghi chi phí chính xác. |
| 30–34 | C08,D00–D07 | Tách chứng minh cận trên, đạt cận, phần dư–sai số và sai số–mất mát. |
| 35–38 | D05,D08 | Gộp CartPole với kiểm tra mô hình; thêm trang quyết định tổng kết. |
| `hw3.pdf` B9/B6/B4/B7 | X09/X06/X04/X07 | Nhánh dọc; X09 chép đủ dữ kiện MDP và lời giải trong notes. |

## Sai khác nguồn cần truy nguyên

- $q_*$, Bellman $q_*$ và quy tắc tham lam được bổ sung để hoàn thiện cầu nối sang điều khiển. A08 dùng ký hiệu $a\triangleright\pi$: ép hành động đầu, rồi dùng chính sách tiếp diễn từ thời điểm một; không điều kiện hóa trên một hành động có thể có xác suất không.
- Định nghĩa kiểu $T^\pi,T_*:\mathcal V\to\mathcal V$ và chuẩn vô cùng được thêm vì chứng minh nguồn dùng chúng ngầm.
- Lặp chính sách sửa đổi được bỏ khỏi tuyến chính: nguồn không đặc tả đủ cách mang $v_0$ giữa các vòng, tiêu chuẩn dừng ngoài, phá hòa và bảo đảm. Bảo đảm của PI chính xác được giữ nguyên.
- C09 tính $w=T_*v$ để phần dư và chính sách tham lam dùng cùng bảng $v$; nếu chưa dừng, tái sử dụng $w$ làm bảng tiếp theo.
- D03–D07 mở các bước chứng minh mà nguồn lược để tránh phát biểu kết quả không có cầu nối.

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $\mathcal V=\mathbb R^{|\mathcal S|}$ | Không gian các hàm giá trị dạng véc-tơ |
| $\lVert v\rVert_\infty$ | $\max_s|v(s)|$ |
| $T^\pi:\mathcal V\to\mathcal V$ | Toán tử Bellman của chính sách Markov dừng |
| $T_*:\mathcal V\to\mathcal V$ | Toán tử Bellman tối ưu |
| $v_*,q_*$ | Giá trị trạng thái và giá trị hành động tối ưu |
| $\rho(v)$ | Phần dư $\lVert T_*v-v\rVert_\infty$ |
| $\pi_v$ | Chính sách tham lam theo đúng hàm $v$ |
| $\Pi$ | Mọi chính sách khả dụng; D03 chặn bằng chân trời hữu hạn |
| $C_{\mathrm{model}}$ | Chi phí một lượt duyệt mọi kết quả có xác suất dương |
| $\varepsilon_{\mathrm{step}}$ | Ngưỡng thay đổi giữa hai lượt đánh giá chính sách |
| $\varepsilon_{\mathrm{pol}}$ | Mục tiêu chặn mất mát chính sách |

## Tài sản

- `dp-cycle.svg`: chu trình đánh giá–cải thiện.
- `two-state.svg`: MDP hai trạng thái.
- `bellman-choice.svg`: phép cực đại trong sao lưu.
- `gridworld.svg`: Gridworld năm ô, dùng $\gamma=0{,}9$ trong HTML.
- `cartpole.svg`: lượng tử hóa và giới hạn thiếu mô hình.
