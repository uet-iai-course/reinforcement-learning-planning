# Dàn ý Bài 08: Deep Q-Learning

## Phạm vi

- Nguồn chính: `RL-hk2-2025-2026/lecture8-dqn.pdf`, 36 trang.
- Không có tài liệu bài tập hay code demo đi kèm.
- Đối tượng: sinh viên đã học Q-learning dạng bảng, xấp xỉ hàm và bộ ba nguy hiểm.
- Đầu ra: 34 trang chính + 3 trang bài tập dọc = 37 mã trang; 120 phút chính gồm 110 phút tuyến cốt lõi và 10 phút linh hoạt; 30 phút chữa bài qua ba bài tập dọc (ngoài 120 phút chính, không tính là vượt giờ).

## Mục tiêu học tập

1. Phân biệt chính sách hành vi $\epsilon_{\mathrm{exp}}$-greedy với chính sách đích tham lam của Q-learning.
2. Mô tả giao diện DQN: quan sát hoặc biểu diễn trạng thái vào, vector $|\mathcal A|$ giá trị hành động ra.
3. Tính đích $y=R+\gamma(1-Z)\max Q_{\theta^-}$, phân biệt kết thúc MDP với cắt ngắn ngoài mô hình và lưu đúng quan sát cuối khi môi trường tự reset.
4. Truy dấu vòng thu thập, làm nóng replay, tần suất tối ưu, mini-batch, cập nhật mạng online và đồng bộ mạng mục tiêu sau bước tối ưu.
5. Viết đúng SGD, RMSprop và Adam theo từng tọa độ, đồng thời giới hạn vai trò của optimizer.
6. Giải thích replay và mạng mục tiêu giảm hai cơ chế bất ổn nhưng không tạo bảo đảm hội tụ.

## Bảy mạch ngoài (cấu trúc HTML)

HTML có đúng 7 section ngoài, độ sâu tối đa 2:

1. M1 — `L08-01`–`L08-06`: cầu nối từ bảng Q sang DQN; giữ mốc 7+13 phút bên trong M1 giữa `L08-03`/`L08-04`.
2. M2 — `L08-07`–`L08-10` + `X01`: giao diện mạng, hai mạng, đích bootstrap, loss và bài tính.
3. M3 — `L08-11`–`L08-21` + `X02`: vòng DQN, replay, hai cờ, giả mã, hợp đồng tensor và kiểm tra gradient.
4. M4 — `L08-22`–`L08-25`: gradient và ba bộ tối ưu (nhánh dọc linh hoạt).
5. M5 — `L08-26`: bảng so sánh và phạm vi chọn optimizer.
6. M6 — `L08-27`–`L08-30`: bất ổn, replay, mạng mục tiêu và deadly triad.
7. M7 — `L08-31`–`L08-34` + `X03`: pipeline Atari, kiểm tra tổng hợp, ablation và hợp đồng DQN.

`X01`–`X03` là 30 phút chữa bài ngoài 120 phút chính; không coi đây là lỗi thời lượng.

## Truy nguyên các trang bổ sung

- `L08-20` (hợp đồng tensor Atari): truy nguyên từ công thức loss `L08-17` và giao diện mạng `L08-07`; biến công thức thành shape/dtype/device cụ thể trước khi kiểm tra.
- `L08-21` (kiểm tra dấu gradient hai mẫu): truy nguyên từ ví dụ số `X01` và công thức loss; kiểm hướng cập nhật trước khi sửa giả mã.
- `X01` (bài tính đích, TD error, MSE, gradient): truy nguyên trực tiếp từ công thức đích và loss của nguồn.
- `X03` (bài ablation): truy nguyên từ hai cơ chế replay và mạng mục tiêu; dùng lại đúng hai cơ chế đã dạy và thu hồi bốn kết quả `L08-02`.

## Câu hỏi khám phá nguồn tr.36

Câu hỏi khám phá ở nguồn tr.36 không được đưa lên mặt trang vì đã có `L08-33` (kiểm tra tổng hợp bốn câu) và `X03` (ablation) phủ cùng mục tiêu kiểm; nội dung liên quan được đưa vào notes của `L08-33`. Không thêm câu hỏi mới lên mặt trang.

## Mạch nội dung (cụm khái niệm nhỏ hơn)

1. Cầu nối từ bảng Q sang DQN.
2. Giao diện mạng, khởi tạo mạng online/mục tiêu và mục tiêu bootstrap.
3. Bộ nhớ phát lại, mạng mục tiêu và giả mã hoàn chỉnh.
4. Gradient và ba bộ tối ưu.
5. Bất ổn, bộ ba nguy hiểm và phạm vi bảo đảm.
6. Pipeline Atari và kiểm tra tổng hợp.

## Ánh xạ nguồn

| trang nguồn | trang đích | quyết định | lý do |
|---|---|---|---|
| 1 | `L08-01` | giữ | Tiêu đề. |
| 2 | `L08-02` | sửa | Đổi dàn ý thành kết quả học tập. |
| 3 | `L08-04`–`L08-05` | tách | Tách loại thuật toán khỏi hành vi–đích. |
| 4 | `L08-04`, `L08-08`–`L08-09` | sửa | Chuẩn hóa chỉ số và thêm mặt nạ kết thúc. |
| 5 | `L08-04`, `L08-18`–`L08-19` | tách | Dùng cầu nối dạng bảng rồi xây giả mã DQN đầy đủ. |
| 6 | `L08-05`, `L08-33` | gộp | Hoàn tất vai trò khám phá và kiểm tra. |
| 7 | `L08-05` | sửa | Giới hạn kết luận hội tụ vào dạng bảng với giả thiết rõ. |
| 8–9 | `L08-06` | gộp, lược | Bỏ cận mẫu thiếu mô hình định lý; giữ vấn đề quy mô. |
| 10–11 | `L08-03`, `L08-06` | gộp, lược | Bỏ cận tuyến tính thiếu cấu trúc MDP và thuật toán cụ thể. |
| 12–13 | `L08-27`, `L08-30` | gộp, sửa | Nối bất ổn với bộ ba nguy hiểm; bỏ cách gọi quảng bá. |
| 14–15 | `L08-03`, `L08-07` | gộp | Giới hạn bảng và giao diện DQN. |
| 16 | `L08-07`–`L08-10`, `L08-17` | tách, sửa | Đặt phản ví dụ mục tiêu di động trước hai mạng; thêm mặt nạ, batch và dừng gradient. |
| 17 | `L08-07`, `L08-31` | gộp | MLP cho vector, CNN cho ảnh. |
| 18 | `L08-11`, `L08-18`–`L08-19` | tách, sửa | Vẽ lại vòng huấn luyện; bổ sung warmup, tần suất cập nhật và hai bộ đếm. |
| 19 | `L08-13`–`L08-16` | tách, sửa | Replay và target network là hai cơ chế riêng. |
| 20 | `L08-13`, `L08-17` | gộp, sửa | Chuẩn hóa $\theta,\theta^-$ và batch từ $\mathcal D$. |
| 21 | `L08-12`, `L08-18`–`L08-19`, `X02` | tách, sửa | Chuẩn hóa hai cờ, final observation khi autoreset và mặt nạ theo MDP đang mô hình hóa. |
| 22 | `L08-10`, `L08-22` | tách, sửa | Gradient chỉ qua giá trị đã gather từ mạng online; khai báo miền optimizer. |
| 23 | `L08-22`, `L08-26` | gộp | Thu hẹp vai trò optimizer. |
| 24 | `L08-23` | giữ, sửa | Công thức SGD và phạm vi. |
| 25 | `L08-24` | giữ, sửa | Nêu phép toán theo tọa độ và quy ước $\epsilon_{\mathrm{opt}}$. |
| 26 | `L08-25` | giữ, sửa | Sửa mẫu số Adam và bổ sung khởi tạo. |
| 27–28 | `L08-26` | gộp, sửa | Không tuyên bố phương pháp thắng tuyệt đối hay hội tụ nhanh. |
| 29 | `L08-07`, `L08-27` | tách, sắp xếp lại | Đặt phản ví dụ mục tiêu di động trước mạng mục tiêu; nối bất ổn với deadly triad. |
| 30 | `L08-14`, `L08-28` | sửa | Replay giảm tương quan, không tạo i.i.d. |
| 31 | `L08-29` | giữ, sửa | Mục tiêu đổi ở mốc đồng bộ. |
| 32 | `L08-13`–`L08-14` | gộp, sửa | Cơ chế và giới hạn của replay. |
| 33 | `L08-07`, `L08-15`–`L08-16` | tách, sắp xếp lại | Khai báo và khởi tạo hai mạng trước đích; sau đó nối đường gradient với đồng bộ cứng. |
| 34 | `L08-17` | giữ, sửa | Mục tiêu tích hợp có mặt nạ và stop-gradient. |
| 35 | `L08-31`–`L08-32` | tách, sửa | Bốn khung là lịch sử quan sát, không bảo đảm Markov. |
| 36 | `L08-33` | sửa | Chuyển thành kiểm tra tổng hợp có phạm vi. |

## Thuật ngữ và ký hiệu

| ký hiệu | nghĩa |
|---|---|
| $O_t$ | quan sát hoặc biểu diễn trạng thái đưa vào mạng |
| $S_t$ | trạng thái Markov khi giả thiết đủ quan sát được áp dụng |
| $A_t\in\mathcal A$ | hành động; DQN cơ bản cần $\mathcal A$ rời rạc hữu hạn |
| $R_{t+1}$ | phần thưởng sau khi thực hiện $A_t$ trong chỉ số thời gian |
| $Z_{t+1}$ | cờ kết thúc thật của MDP |
| $U_{t+1}$ | cờ cắt ngắn do cơ chế thu thập |
| $Q_\theta$ | mạng online, nhận gradient |
| $Q_{\theta^-}$ | mạng mục tiêu, giữ cố định giữa các lần đồng bộ |
| $\mathcal D$ | bộ nhớ phát lại |
| $\operatorname{sg}$ | dừng gradient qua đối số |
| $\epsilon_{\mathrm{exp}}$ | xác suất khám phá |
| $\epsilon_{\mathrm{opt}}$ | hằng số ổn định số trong optimizer |
| $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ | mẫu thứ $i$ sau khi lấy mini-batch, $i=1,\ldots,b$ |
| $b$ | số chuyển tiếp trong mini-batch |
| $t\in\mathbb N_0$ | bộ đếm bước môi trường |
| $k_{\mathrm{opt}}\in\mathbb N_0$ | bộ đếm bước tối ưu; tăng sau khi cập nhật $\theta$ |
| $N\in\mathbb N_+$ | dung lượng replay |
| $N_{\mathrm{start}}\in\mathbb N_+$ | số mẫu tối thiểu trước bước tối ưu đầu tiên, $b\le N_{\mathrm{start}}\le N$ |
| $F\in\mathbb N_+$ | số bước môi trường giữa hai lần tối ưu |
| $C\in\mathbb N_+$ | số bước tối ưu giữa hai lần đồng bộ cứng |
| $\gamma\in[0,1]$ | hệ số chiết khấu; dùng $\gamma=1$ chỉ khi episode kết thúc thích hợp và return hữu hạn |
| $\alpha_t>0$ | bước học dạng bảng; nếu phát biểu hội tụ, dãy bước phải thỏa Robbins–Monro theo từng cặp trạng thái–hành động |
| $\eta>0$ | tốc độ học của optimizer |
| $\rho,\beta_1,\beta_2\in[0,1)$ | hệ số moment của RMSprop và Adam |
| $\epsilon_{\mathrm{exp}}\in[0,1]$ | xác suất khám phá của chính sách hành vi |
| $\epsilon_{\mathrm{opt}}>0$ | hằng số ổn định số trong mẫu số optimizer |

Quy ước thời gian chỉ dùng khi tương tác với môi trường: $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$. Sau khi lấy mini-batch, dùng duy nhất $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ với $i=1,\ldots,b$; không trộn $i+1$ vào chỉ số batch.

## Phân bổ thời lượng

- 120 phút chính = 110 phút cốt lõi (cầu nối Q-learning, giao diện và hai mạng, đích/loss, replay, giả mã, bất ổn, Atari và tổng hợp) + 10 phút linh hoạt.
- 10 phút linh hoạt: từ `L08-22` đi xuống `L08-23`–`L08-25` để xem SGD, RMSprop và Adam. Tuyến ngang đi từ `L08-22` sang bảng so sánh `L08-26`.
- 30 phút chữa bài (ngoài 120 phút chính): `X01`, `X02`, `X03`, mỗi bài 10 phút.

## Tài sản SVG

`table-vs-dqn.svg`, `dqn-training-loop.svg`, `replay-buffer.svg`, `target-network-timeline.svg`, `dqn-computation-graph.svg`, `tensor-contract.svg`, `deadly-triad.svg`, `atari-pipeline.svg`.
