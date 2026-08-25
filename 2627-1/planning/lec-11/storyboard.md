# Storyboard Bài 11

## Chu trình học tập

| cụm không chồng lặp | chu trình | trang | đầu vào → sản phẩm | cốt lõi | linh hoạt |
|---|---|---|---|---:|---:|
| Định hướng | mở → hai tầng mục tiêu → recap PPO | `L11-01`–`L11-03` | Bài 10 → hợp đồng $w$, dấu lợi thế, batch cũ | 7 | 0 |
| SPO và SAM | vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng → giới hạn | `L11-04`–`L11-12` | PPO → objective tỷ số và SAM đúng dấu | 24 | 4 tại `L11-10` |
| Actor–critic rồi khác chính sách | core → target → so sánh → replay → ví dụ → identity/giới hạn | `L11-16`–`L11-19`, `L11-13`–`L11-15` | actor–critic → A3C/A2C → off-policy | 18 | 0 |
| DPG và mở rộng | vấn đề/ví dụ → định lý → target → thuật toán → mở rộng | `L11-20`–`L11-28` | hành động liên tục → DDPG, D4PG và CTDE | 25 | 0 |
| Replay, độ cong, SAC/TD3 | correction/curvature → vấn đề → trực giác → ví dụ → hình thức → so sánh | `L11-29`–`L11-37` | ACER/ACKTR → hai họ continuous replay | 24 | 0 |
| Khảo sát | cơ chế định nghĩa → so sánh | `L11-38`–`L11-41` | SVPG/IMPALA/PPG → nhận dạng theo bài toán | 8 | 6 tại `L11-39` |
| Bản đồ và tổng hợp | bản đồ → kiểm tra đọc mới | `L11-42`–`L11-43` | toàn bài → quy tắc chọn và kiểm | 4 | 0 |

Các khoảng trên phủ đúng 43 trang chính, không chồng lặp: 110 phút cốt lõi và 10 phút linh hoạt. `X01`, `X02`, `X03` tách khỏi thời lượng trình chiếu, dùng lần lượt 8, 12 và 10 phút. Phần khảo sát dùng chu trình rút gọn vì không dạy giả mã đầy đủ.

## Truyền dữ kiện

- $\epsilon=0{,}2$, $A=\pm2$ đi từ `L11-06` qua công thức `L11-07` sang `X01`.
- $g=(3,4)$, $\rho=0{,}1$ đi từ `L11-09` qua thuật toán `L11-10` sang `X01`.
- Behavior/target support ở `L11-14` được dùng lại khi đọc ACER và IMPALA.
- Occupancy chuẩn hóa ở `L11-21` quyết định hệ số $1/(1-\gamma)$.
- Target/online/noise ở `L11-22`–`L11-24` được kế thừa bởi D4PG, MADDPG và TD3.
- Twin critics ở SAC và TD3 dùng cùng phép min nhưng khác policy và entropy.
- Các cơ chế ở `L11-38`–`L11-40` được đối chiếu trong `L11-41`, ánh xạ ở `L11-42` rồi áp dụng trong `X03`.

## Từng trang

| mã | luận điểm | bước |
|---|---|---|
| `L11-01` | Một cầu nối từ PPO sang các biến thể nâng cao. | mở |
| `L11-02` | Tách tầng core phải tính/viết khỏi tầng định hướng chỉ nhận dạng. | định hướng |
| `L11-03` | Recap hiện rõ $w$, dấu lợi thế và batch cũ đóng băng. | tiên quyết |
| `L11-04` | PPO có vùng gradient bằng không theo mẫu. | vấn đề SPO |
| `L11-05` | Penalty tạo lực kéo về $1\pm\epsilon$ theo dấu lợi thế. | trực giác |
| `L11-06` | Hai ca $A=\pm2$ đặt tỷ số ở $1{,}2$ và $0{,}8$. | ví dụ |
| `L11-07` | Objective, đạo hàm, ca $A=0$ và phạm vi thay policy loss. | hình thức, ứng dụng |
| `L11-08` | Đỉnh sắc nhạy hơn vùng phẳng trong cùng bán kính tham số. | vấn đề, trực giác |
| `L11-09` | Gradient $(3,4)$ cho nhiễu $(-0{,}06,-0{,}08)$. | ví dụ |
| `L11-10` | Max–min, dấu $\xi$ và thuật toán SAM một bước. | hình thức, thuật toán |
| `L11-11` | Liên hệ tham số–hành động cần chặn Jacobian hoặc điều kiện hạng. | ứng dụng có điều kiện |
| `L11-12` | Bằng chứng SAM+PPO có phạm vi giao thức. | ứng dụng có giới hạn |
| `X01` | Tính SPO, SAM và nêu điều kiện thiếu. | kiểm tra |
| `L11-16` | Actor và critic có đường gradient riêng. | hình thức |
| `L11-17` | A3C dùng snapshot $\phi_{\mathrm{loc}}$, đúng $n_t$ và bootstrap detach; không có target network. | thuật toán |
| `L11-18` | A3C có gradient trễ bất đồng bộ. | giới hạn |
| `L11-19` | A2C gom rollout đồng bộ. | so sánh |
| `L11-13` | Replay tạo lệch hành động và trạng thái. | vấn đề off-policy |
| `L11-14` | Ví dụ IS cho $1{,}6$ xuất hiện trước identity và điều kiện support. | ví dụ, hình thức |
| `L11-15` | Trajectory IS, replay và DPG là ba bài toán khác. | giới hạn |
| `L11-20` | Bài toán hành động liên tục và ví dụ scalar $2\times3=6$ chuẩn bị DPG. | vấn đề, ví dụ |
| `L11-21` | DPG với occupancy chuẩn hóa cần hệ số. | định lý |
| `L11-22` | DDPG tách behavior noise khỏi target actor. | vấn đề, cơ chế |
| `L11-23` | DDPG dùng $D_\theta\mu^\top\nabla_aQ$ trên replay như surrogate off-policy thực hành. | hình thức |
| `L11-24` | DDPG phối hợp replay, bốn mạng và soft update. | thuật toán |
| `L11-25` | D4PG được nhận dạng bằng target phân phối $n$ bước và projection $\Pi$. | định hướng |
| `L11-26` | MADDPG core dùng CTDE và Jacobian chuyển vị đúng shape. | trực giác, hình thức |
| `L11-27` | Target MADDPG dùng mọi target actor. | thuật toán |
| `L11-28` | D4PG và MADDPG sửa hai giới hạn khác nhau. | so sánh |
| `X02` | Kiểm IS, kích thước DPG và noise DDPG. | kiểm tra |
| `L11-29` | ACER định hướng: support, tỷ số cắt và residual correction; Retrace/trust region không triển khai. | định hướng |
| `L11-30` | ACKTR định hướng: công thức chỉ là lõi K-FAC, còn damping/trust scaling ở ghi chú. | định hướng |
| `L11-31` | ACER sửa dữ liệu; ACKTR sửa hình học. | so sánh |
| `L11-32` | SAC đổi objective; TD3 xử lý lỗi critic/overestimation. | vấn đề |
| `L11-33` | Phần giao là min twin critics; entropy không phải target correction. | trực giác |
| `L11-34` | Twin target số cho $y=4{,}6$ trước công thức đầy đủ. | ví dụ |
| `L11-35` | SAC hiện đại không có mạng $V$ riêng; $\alpha$ cố định. | hình thức |
| `L11-36` | TD3 dùng noise clip rồi action clip, actor $Q_1$, critic mỗi bước và actor/target mỗi $d$. | thuật toán |
| `L11-37` | SAC stochastic/entropy khác TD3 deterministic/noise ngoài policy. | so sánh, ứng dụng |
| `L11-38` | SVPG giả sử prior đều, định nghĩa particle/kernel/$\alpha$ và lực đẩy. | định hướng |
| `L11-39` | V-trace định nghĩa $\mu,\pi,u,\rho,c,\gamma_t$ và vai trò residual/trace. | định hướng |
| `L11-40` | PPG dùng $L_{\mathrm{joint}}$, auxiliary value head, policy/target trước pha đóng băng. | định hướng |
| `L11-41` | Ba phương pháp trả lời ba bài toán. | so sánh |
| `L11-42` | Bản đồ nhiều thuộc tính, không coi các hàng là loại trừ. | tổng hợp |
| `X03` | Tính twin target rồi chọn ba scenario: continuous replay, CTDE và policy lag. | kiểm tra |
| `L11-43` | Năm phép kiểm cho phương pháp mới. | tổng hợp |
