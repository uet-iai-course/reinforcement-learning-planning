# Dàn ý Bài 11: Các phương pháp gradient chính sách nâng cao

## Phạm vi

Nguồn chính: `RL-hk2-2025-2026/lecture11_part3.pdf`, 78 trang. Trang 4–43 lặp Bài 10 nên chỉ tạo một cầu nối tiên quyết ở `L11-01`. Nội dung mới dùng trang 44–77; trang 78 cung cấp tài liệu tham khảo. Không có code demo.

Sau bài, kết quả học tập chia hai tầng:

**Tầng core — tính và viết được**

1. tính objective SPO và nhiễu SAM đúng dấu;
2. viết target $n_t$ bước của A3C và so sánh với A2C;
3. viết target, Jacobian–gradient và hợp đồng replay của DDPG/MADDPG;
4. tính target và phân biệt objective/cơ chế của SAC với TD3;
5. kiểm tra support, occupancy, terminal/cutoff, mạng target, noise và dừng gradient.

**Tầng định hướng — nhận dạng cơ chế và giới hạn**

- D4PG, ACER, ACKTR, SVPG, IMPALA và PPG;
- không yêu cầu triển khai đầy đủ các thuật toán định hướng.

## Thời lượng

| cụm | trang | nội dung giảng | linh hoạt |
|---|---|---:|---:|
| Định hướng | `L11-01`–`L11-03` | 7 phút | 0 |
| SPO và SAM+PPO | `L11-04`–`L11-12` | 24 phút | 4 phút |
| Actor–critic core rồi khác chính sách | `L11-16`–`L11-19`, `L11-13`–`L11-15` | 18 phút | 0 |
| DPG và các mở rộng | `L11-20`–`L11-28` | 25 phút | 0 |
| ACER, ACKTR, SAC, TD3 | `L11-29`–`L11-37` | 24 phút | 0 |
| SVPG, IMPALA, PPG | `L11-38`–`L11-41` | 8 phút | 6 phút |
| Bản đồ và tổng hợp | `L11-42`–`L11-43` | 4 phút | 0 |
| Tổng | 43 trang chính | 110 phút | 10 phút |

Các bài tập `X01`, `X02`, `X03` dùng 8, 12 và 10 phút, tổng 30 phút. Toàn buổi gồm 120 phút trình chiếu chính và 30 phút bài tập, tổng 150 phút.

## Ánh xạ toàn bộ nguồn

| trang nguồn | quyết định | trang đích | lý do |
|---|---|---|---|
| 1–3 | sửa, gộp | `L11-01`–`L11-02` | Giữ nhận diện và chuyển mục tiêu thành sản phẩm kiểm tra. |
| 4–43 | gộp | `L11-01` | Nội dung đã học ở Bài 10; chỉ giữ một cầu nối tiên quyết. |
| 44–47 | tách, sửa | `L11-04`–`L11-07`, `X01` | Đi theo vấn đề → trực giác → số $A=\pm2$ → objective/đạo hàm/$A=0$; SPO chỉ thay policy loss. |
| 48–51 | tách, sửa | `L11-08`–`L11-12`, `X01` | Đi theo sharp/flat → số $g=(3,4)$ → max–min/thuật toán → liên hệ có điều kiện → phạm vi bằng chứng. |
| 52 | dời cục bộ | `L11-13` | Dùng vấn đề khác chính sách sau khi đã dựng actor–critic core. |
| 53–54 | sửa | `L11-16` | Khóa đường gradient actor và critic. |
| 55–56 | tách, sửa | `L11-13`–`L11-15`, `X02` | Tách action IS khỏi trajectory/occupancy mismatch. |
| 57–58 | tách, sửa, dời trước off-policy | `L11-16`–`L11-19` | Actor–critic core đứng trước replay; A3C dùng snapshot $\phi_{\mathrm{loc}}$, target dừng tại $n_t$ và không dùng target network. |
| 59–61 | tách, sửa | `L11-20`–`L11-24`, `X02` | Đặt bài toán và ví dụ scalar trước định lý DPG; sau đó mới tách behavior/target và thuật toán DDPG. |
| 62–64 | tách, sửa | `L11-25`–`L11-28` | D4PG chỉ ở mức nhận dạng: target $n$ bước và projection $\Pi$; MADDPG là core CTDE với Jacobian đúng shape. |
| 65–67 | tách, sửa | `L11-29`–`L11-31` | ACER/ACKTR ở mức định hướng; nêu support/correction và lõi K-FAC, không trình bày như thuật toán đầy đủ. |
| 68–71 | tách, sửa | `L11-32`–`L11-37` | Sắp vấn đề → trực giác hai hướng → ví dụ twin target → SAC formal → TD3 mechanisms → so sánh policy/noise. |
| 72–74 | giữ, bổ sung | `L11-38`–`L11-41` | Mỗi phương pháp có một phương trình hoặc cơ chế định nghĩa; thêm cloning KL của PPG. |
| 75–77 | gộp, sửa | `L11-42`, `X03`, `L11-43` | Bản đồ thêm ACKTR/SVPG; X03 sau bản đồ yêu cầu chọn họ và tradeoff; kết bằng checklist. |
| 78 | giữ | ghi chú và nhật ký | Truy nguyên tài liệu gốc. |

## Ký hiệu

| ký hiệu | nghĩa |
|---|---|
| $w$ | tỷ số policy mới/cũ trong SPO |
| $\epsilon$ | tham số tỷ số SPO hoặc clipping khi ngữ cảnh xác định |
| $\xi_{\mathrm{adv}}$ | nhiễu tham số đối nghịch của SAM |
| $\rho$ | bán kính SAM; $\rho_t$ chỉ tỷ số importance trong phần khác chính sách |
| $\beta,\pi$ | behavior policy và target policy |
| $d_{\rho_0,\gamma}^{\mu}$ | occupancy chiết khấu chuẩn hóa của policy tất định |
| $m_t$ | mặt nạ terminal thật dùng chung trong A3C, D4PG, DDPG và các target liên quan |
| $\operatorname{sg}(x)$ | coi $x$ là hằng số khi lấy đạo hàm; dừng gradient qua $x$ |
| $\theta,\phi$ | tham số actor và critic online |
| $\bar\theta,\bar\phi$ | tham số actor và critic target |
| $u$ | tỷ số $u=\pi/\beta$ trong ACER |
| $u_t$ | tỷ số $u_t=\pi/\mu$ trong V-trace |
| $c_\xi$ | cận clip của nhiễu tham số $\xi$ trong TD3 |
| $\phi_{\mathrm{loc}}$ | snapshot critic cục bộ của worker A3C; không phải mạng target |
| $Z(s,a)$ | phân phối return trong D4PG |
| $D_\theta\mu$ | Jacobian actor, shape $d_a\times d_\theta$; gradient tham số dùng $D_\theta\mu^\top\nabla_aQ$ |
| $\mu,\pi,u_t$ | behavior actor, learner policy và tỷ số $u_t=\pi/\mu$ trong V-trace |

Tên viết tắt dùng nhất quán: Simple Policy Optimization (SPO, tối ưu chính sách đơn giản); Sharpness-Aware Minimization (SAM); Asynchronous/Advantage Actor–Critic (A3C/A2C); Deterministic Policy Gradient (DPG); Deep DPG (DDPG); Distributed Distributional DPG (D4PG); Multi-Agent DDPG (MADDPG); centralized training, decentralized execution (CTDE); Actor-Critic with Experience Replay (ACER); Actor Critic using Kronecker-Factored Trust Region (ACKTR); Soft Actor–Critic (SAC); Twin Delayed DDPG (TD3); Stein Variational Policy Gradient (SVPG); Importance Weighted Actor-Learner Architectures (IMPALA); Phasic Policy Gradient (PPG).

## SVG

`spo-ratio-field.svg`, `sam-parameter-neighborhood.svg`, `sam-claim-scope.svg`, `offpolicy-corrections.svg`, `a3c-a2c-workers.svg`, `dpg-chain-rule.svg`, `ddpg-data-targets.svg`, `d4pg-maddpg.svg`, `acer-acktr.svg`, `sac-td3-targets.svg`, `survey-three-methods.svg`.

## Danh mục mã trang

`L11-01`, `L11-02`, `L11-03`, `L11-04`, `L11-05`, `L11-06`, `L11-07`, `L11-08`, `L11-09`, `L11-10`, `L11-11`, `L11-12`, `X01`, `L11-16`, `L11-17`, `L11-18`, `L11-19`, `L11-13`, `L11-14`, `L11-15`, `L11-20`, `L11-21`, `L11-22`, `L11-23`, `L11-24`, `L11-25`, `L11-26`, `L11-27`, `L11-28`, `X02`, `L11-29`, `L11-30`, `L11-31`, `L11-32`, `L11-33`, `L11-34`, `L11-35`, `L11-36`, `L11-37`, `L11-38`, `L11-39`, `L11-40`, `L11-41`, `L11-42`, `X03`, `L11-43`.

## Ánh xạ note-topic-id → data-slide-id

| note-topic-id | data-slide-id |
|---|---|
| `lec-11-topic-01` | `L11-01`, `L11-02`, `L11-03` |
| `lec-11-topic-02` | `L11-04`, `L11-05`, `L11-06`, `L11-07` |
| `lec-11-topic-03` | `L11-08`, `L11-09`, `L11-10`, `L11-11`, `L11-12`, `X01` |
| `lec-11-topic-04` | `L11-16`, `L11-17`, `L11-18`, `L11-19` |
| `lec-11-topic-05` | `L11-13`, `L11-14`, `L11-15` |
| `lec-11-topic-06` | `L11-20`, `L11-21` |
| `lec-11-topic-07` | `L11-22`, `L11-23`, `L11-24` |
| `lec-11-topic-08` | `L11-25`, `L11-26`, `L11-27`, `L11-28`, `X02` |
| `lec-11-topic-09` | `L11-29`, `L11-30`, `L11-31` |
| `lec-11-topic-10` | `L11-32`, `L11-33`, `L11-34`, `L11-35`, `L11-36`, `L11-37` |
| `lec-11-topic-11` | `L11-38`, `L11-39`, `L11-40`, `L11-41` |
| `lec-11-topic-12` | `L11-42`, `X03` |
| `lec-11-topic-13` | `L11-43` |
