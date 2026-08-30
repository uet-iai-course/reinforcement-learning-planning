# Dàn ý Bài 06: Điều khiển phi mô hình

## Mục tiêu và phạm vi

Sinh viên phân biệt dự đoán với điều khiển, theo chính sách với khác chính sách; tạo chính sách $\varepsilon$-tham lam từ bảng $Q$; thực hiện MC control lần ghé đầu tiên, SARSA và Q-learning dạng bảng; giải thích vai trò của đích cập nhật, thăm dò, GLIE, độ phủ và bước học Robbins–Monro.

Thiết lập chính là MDP bảng hữu hạn, phần thưởng bị chặn. MC chỉ áp dụng khi lượt kết thúc gần chắc chắn và phần thưởng tích lũy hữu hạn. Bài toán theo lượt đặt giá trị trạng thái kết thúc bằng không. Các kết luận hội tụ của bài dùng $\gamma<1$ và chỉ áp dụng trên miền cặp khả đạt $\mathcal X_{\mathrm{reach}}$. Không dạy xấp xỉ hàm, DQN, policy gradient hoặc actor-critic; E03 chỉ nối sang nội dung xấp xỉ hàm của Bài 07. Không có code demo trong nguồn.

Sai khác nguồn: tr. 15 ghi môi trường "tối đa 3 bước" nhưng không nêu quy ước return nếu cắt trước trạng thái kết thúc, nên deck không dùng mệnh đề này. Sơ đồ B–C biểu diễn quan hệ chuyển tham lam theo bảng $Q_0$ thống nhất (ví dụ 2, $Q_0(D)=(1,0)$) khi bỏ bộ đếm giới hạn; lượt dùng trong deck kết thúc ở A sau đúng ba chuyển. Giả thiết MC tổng quát vẫn cần kết thúc gần chắc chắn.

## Cấu trúc

| Phần | Trang | Nội dung |
|---|---|---|
| Định hướng | P00–P03 | Từ dự đoán sang điều khiển, ký hiệu và vòng học |
| Chính sách và ví dụ chung | A00–A04 | $Q$, $\varepsilon$-tham lam, theo/khác chính sách, chuỗi năm trạng thái và quy tắc cố định lượt |
| MC control | B00–B06 | Return, thuật toán đầy đủ, hai bước học, cải thiện $\varepsilon$-mềm và GLIE |
| SARSA | C00–C05 | Ví dụ nhỏ, đích theo chính sách, thuật toán, lượt chung, kiểm tra và hội tụ |
| Q-learning và khác chính sách | D00–D07 | Ví dụ nhỏ, đích tham lam, thuật toán, lượt chung, hội tụ và TD(0) mở rộng |
| Tổng hợp | E00–E02 | So sánh, chi phí và chặn Hoeffding đúng phạm vi; E02 là trang linh hoạt |
| Kết luận và bài tập dọc | E03, X01–X03 | Giới hạn kết luận; tái tạo lượt, so SARSA–Q-learning và phản biện hội tụ |

Bộ trang chiếu có 34 trang chính và 3 trang bài tập dọc. Tuyến cốt lõi là 110 phút, không gồm D06, D07 hoặc E02. Ba trang này tạo nhánh linh hoạt đúng 10 phút. Ba bài tập dọc dùng 30 phút theo phân bổ 5–10–15 phút.

## Danh mục mã trang

- Định hướng: P00, P01, P02, P03.
- Chính sách và ví dụ chung: A00, A01, A02, A03, A04.
- MC control: B00, B01, B02, B03, B04, B05, B06.
- SARSA: C00, C01, C02, C03, C04, C05.
- Q-learning và khác chính sách: D00, D01, D02, D03, D04, D05, D06, D07.
- Tổng hợp: E00, E01, E02.
- Kết luận và bài tập dọc: E03, X01, X02, X03.

## Ánh xạ nguồn

| Nguồn | Đích | Quyết định |
|---|---|---|
| tr. 1–5 | P00–P01 | Gộp phần ôn dự đoán; giữ cầu nối MC/TD |
| tr. 6–9 | P01–P03,A00,A03 | Giữ vòng điều khiển, $Q$ và dữ liệu; sửa định nghĩa on/off-policy |
| tr. 10–11 | A01,B00–B06 | Tách $\varepsilon$-tham lam, thuật toán MC đầy đủ và GLIE; thêm giả thiết kết thúc |
| tr. 12–14 | C00–C02 | Giữ SARSA; bổ sung đầu vào, đầu ra, bộ đếm theo cặp, nhánh kết thúc, dừng và chi phí |
| tr. 15–18 | A03–A04,B03–B04,C00–C04,X01–X02 | Dùng một bảng $Q_0$ và một lượt chung; xác định quy tắc số là tất định, không phải bộ lấy mẫu; tính lại mọi cập nhật |
| tr. 19 | D06–D07 | Sửa thành TD(0) khác chính sách cho giá trị trạng thái với điều kiện hỗ trợ và tỉ số từng bước |
| tr. 20–21 | D00–D05 | Đặt ví dụ trước công thức Q-learning; bổ sung thuật toán đầy đủ, bộ đếm theo cặp và nhánh kết thúc |
| tr. 22–23 | E00,E03 | Thu hẹp về ba thuật toán bảng; bỏ danh mục DQN, policy gradient và actor-critic |
| tr. 24 | B05 | Sửa mệnh đề cải thiện và đặt sau ứng dụng MC |
| tr. 25–28 | B06,C05,D05,X03 | Tách GLIE, độ phủ và Robbins–Monro theo từng cặp; làm chặt phạm vi hội tụ |
| tr. 29 | E01–E02 | Sửa thành chặn Hoeffding điểm cho các return i.i.d. bị chặn; không suy sang điều khiển thích nghi |
| tr. 30 | E00,E03 | Giữ tổng hợp trong phạm vi bảng hữu hạn |

## Ký hiệu

| Ký hiệu | Nghĩa |
|---|---|
| $\mathcal X$ | $\{(s,a):s\in\mathcal S,\ a\in\mathcal A(s)\}$, tập các cặp trạng thái–hành động hợp lệ |
| $\mathcal X_{\mathrm{reach}}$ | Các cặp trong $\mathcal X$ có thể được ghé từ phân phối khởi đầu dưới cơ chế thăm dò đang xét |
| $A_{\max}$ | $\max_{s\in\mathcal S}|\mathcal A(s)|$, số hành động lớn nhất tại một trạng thái |
| $Q_t(s,a)$ | Bảng ước lượng trên $\mathcal X$ trước cập nhật thứ $t$ |
| $q_\pi(s,a)$, $q_*(s,a)$ | Giá trị hành động thật của $\pi$ và giá trị tối ưu |
| $g_Q(s)$ | Một hành động tham lam theo quy tắc phá hòa cố định |
| $m_s$ | $|\mathcal A(s)|$, số hành động tại trạng thái $s$ |
| $\mu_t$ | Chính sách hành vi tại chuyển $t$ |
| $\mu$ | Chính sách hành vi sinh dữ liệu |
| $\pi$ | Chính sách đích cần đánh giá hoặc tối ưu |
| $\rho_t$ | $\pi(A_t\mid S_t)/\mu(A_t\mid S_t)$ |
| $N(s,a)$, $N_k(s,a)$ | Bộ đếm cập nhật của cặp; giá trị của bộ đếm đến hết lượt $k$ |
| $\alpha_n(s,a)$ | Bước học ở lần cập nhật thứ $n$ của cặp $(s,a)$ |
| $Y_t^{\mathrm{SARSA}}$ | $R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$ |
| $Y_t^Q$ | $R_{t+1}+\gamma\max_aQ_t(S_{t+1},a)$ |

## Tài sản SVG

- `control-loop.svg`: vòng chính sách–trải nghiệm–bảng $Q$.
- `five-state-chain.svg`: môi trường A–E, hành động và phần thưởng.
- `greedy-induced-mrp.svg`: quan hệ chuyển tham lam theo bảng $Q_0$ thống nhất khi bỏ bộ đếm giới hạn; không phải MRP đầy đủ của môi trường có giới hạn thời gian.
- `shared-trace.svg`: lượt $D\to C\to B\to A$ và ba return.
- `target-comparison.svg`: so sánh đích MC, SARSA và Q-learning.
