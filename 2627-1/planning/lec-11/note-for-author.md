# Lưu ý cho người soạn và người dạy Bài 11

## Phân bổ

- Giữ 110 phút cốt lõi, 10 phút mở rộng và 30 phút bài tập.
- Phần linh hoạt gồm đúng 4 phút khai triển max–min/ca $g=0$ ở `L11-10` và 6 phút suy diễn V-trace ở `L11-39`. Nếu thiếu thời gian, cắt hai phần này trước. Không bỏ ca $A=0$ của SPO, dấu SAM, occupancy DPG, target DDPG/SAC/TD3 hoặc cloning KL của PPG.
- Ba bài tập dùng 8, 12 và 10 phút.

## Điểm cần nhấn

- Tầng core yêu cầu tính/viết: A3C–A2C, DDPG–MADDPG và SAC–TD3. D4PG, ACER, ACKTR, SVPG, IMPALA, PPG chỉ yêu cầu nhận dạng cơ chế và giới hạn.

- SPO: $0<\epsilon\le1$, $w\ge0$; nghiệm $1+\operatorname{sign}(A)\epsilon$ chỉ duy nhất khi $A\ne0$.
- SAM cực đại hóa reward nên nhiễu inner đi ngược gradient. Dùng $\xi$ cho nhiễu, không dùng epsilon clipping.
- SAM chỉ cho chiều thuận từ nhiễu tham số sang độ nhạy hành động cục bộ. Claim Gaussian dùng covariance cố định và ánh xạ bậc nhất; chiều bao phủ ngược cần đồng thời điều kiện rank và singular value. Chuyển tiếp/reward chỉ có trực giác hoặc bằng chứng thực nghiệm.
- Action importance sampling chỉ sửa phân phối hành động tại trạng thái cố định; luôn hỏi về occupancy và support.
- DPG dùng $D_\theta\mu\in\mathbb R^{d_a\times d_\theta}$ và $D_\theta\mu^\top\nabla_aQ$. Kỳ vọng $S\sim\mathcal D$ trong DDPG là surrogate replay thực hành, không phải định lý on-policy không chệch.
- D4PG ở mức nhận dạng: target phân phối $n$ bước, target network và projection $\Pi$ trước loss; không đo epistemic uncertainty.
- A3C dùng snapshot $\phi_{\mathrm{loc}}$, không phải target network. Terminal đặt $b_t=0$; cutoff chưa terminal đặt $b_t=1$. A2C đồng bộ không tự động tốt hơn.
- ACER chỉ định hướng qua support, truncation và residual correction; Retrace/trust region không triển khai. ACKTR chỉ hiển thị lõi K-FAC; damping và trust-region scaling nằm ở ghi chú.
- SAC hiện đại trong bài không dùng mạng $V$ riêng và giữ $\alpha$ cố định. Entropy đổi objective, không phải target correction.
- TD3: $\xi$ Gaussian được clip rồi action được clip; actor dùng $Q_1$; critic cập nhật mỗi bước, actor/targets mỗi $d$; behavior noise khác target smoothing.
- V-trace: $\rho$ nhân residual, $c$ truyền trace, $\gamma_t=\gamma m_t$ dừng tại terminal.
- SVPG trên mặt trang giả sử prior đều. PPG đóng băng policy trước pha và target value trong pha phụ trợ.

## Phạm vi và phần có thể đọc thêm

- Kết quả SAM+PPO chỉ được mô tả trong ba tác vụ MuJoCo và giao thức của paper; không ngoại suy thành bảo đảm phổ quát.
- SVPG, IMPALA và PPG là phần định hướng. Không triển khai giả mã đầy đủ hoặc benchmark trên lớp.
- Không biến bảng cuối nguồn thành khuyến nghị “default/best”. Dùng `L11-42` theo hai trục nguồn dữ liệu và loại actor; bài `X03` yêu cầu chọn họ rồi nêu tradeoff.
- Không chuẩn bị notebook vì nguồn không có code demo.

## Tự tính trước khi giảng

- SPO: $f(1{,}2,2)=2{,}2$; $f(0{,}8,-2)=-1{,}8$.
- SAM: $(-0{,}06,-0{,}08)$.
- Importance sampling: hai vế bằng $1{,}6$.
- TD3: target $4{,}6$ khi hai target critic là $4$ và $5{,}5$.
