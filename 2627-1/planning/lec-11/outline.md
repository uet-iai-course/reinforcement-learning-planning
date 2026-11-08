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

## Phân loại chủ đề (chuyển từ ghi chú, 2026-11-08)

Ngày 2026-11-04, người dùng quyết định bỏ mục "Bản đồ chủ đề" khỏi ghi chú bài giảng và giữ phân loại bốn nhóm trong `outline.md`; các chú thích `note-topic-id` vẫn nằm trong thân ghi chú. Mỗi hàng dưới đây chép từ mục "Bản đồ chủ đề" của ghi chú bản HEAD (`f86f4a0`) trước khi bỏ ngày 2026-11-08, theo thứ tự của bản đồ. Bản đồ chỉ có các cột `note-topic-id`, chủ đề, nhóm, trang nguồn, thời lượng: cột "Chủ đề" và "Nhóm" chép nguyên văn, cột "Nguồn" là cột "trang nguồn"; cột "Mạch" ghi tiêu đề mục ghi chú đứng ngay sau chú thích `note-topic-id`; hai cột "Vai trò trong mạch" và "Kết nối vào → ra" để "—" vì bản đồ không có.

| `note-topic-id` | Chủ đề | Nhóm | Mạch | Vai trò trong mạch | Kết nối vào → ra | Nguồn |
|---|---|---|---|---|---|---|
| `lec-11-topic-01` | Cầu nối từ PPO và hai tầng kết quả | cầu nối | `## Cầu nối từ PPO và hai tầng kết quả học tập` | — | — | tr. 1–3, 4–43 |
| `lec-11-topic-02` | Tối ưu chính sách đơn giản (SPO) | cốt lõi | `## Tối ưu chính sách đơn giản (SPO)` | — | — | tr. 44–47 |
| `lec-11-topic-03` | SAM+PPO và kiểm tra SPO/SAM | cốt lõi | `## SAM+PPO và kiểm tra SPO/SAM` | — | — | tr. 48–51 |
| `lec-11-topic-04` | Actor–critic, A3C, A2C | cốt lõi | `## Actor–critic, A3C và A2C` | — | — | tr. 53–54, 57–58 |
| `lec-11-topic-05` | Gradient chính sách khác chính sách | cốt lõi | `## Gradient chính sách khác chính sách` | — | — | tr. 52, 55–56 |
| `lec-11-topic-06` | Định lý gradient chính sách tất định | cốt lõi | `## Định lý gradient chính sách tất định (DPG)` | — | — | tr. 59 |
| `lec-11-topic-07` | DDPG và hợp đồng replay/target | cốt lõi | `## DDPG và hợp đồng replay/target` | — | — | tr. 60–61 |
| `lec-11-topic-08` | D4PG, MADDPG và bài kiểm tra | cốt lõi + bổ sung | `## D4PG, MADDPG và bài kiểm tra khác chính sách` | — | — | tr. 62–64 |
| `lec-11-topic-09` | ACER và ACKTR | bổ sung | `## ACER và ACKTR` | — | — | tr. 65–67 |
| `lec-11-topic-10` | SAC và TD3 | cốt lõi | `## SAC và TD3` | — | — | tr. 68–71 |
| `lec-11-topic-11` | SVPG, IMPALA, PPG | bổ sung | `## SVPG, IMPALA và PPG` | — | — | tr. 72–74 |
| `lec-11-topic-12` | Bản đồ lựa chọn và bài tập tích hợp | cốt lõi | `## Bản đồ lựa chọn và bài tập tích hợp` | — | — | tr. 75–77 |
| `lec-11-topic-13` | Năm phép kiểm và tuyến đọc tiếp | đọc thêm | `## Năm phép kiểm và tuyến đọc tiếp` | — | — | tr. 75–78 |

Cột "thời lượng" của bản đồ: `lec-11-topic-01` 7 phút; `lec-11-topic-02` 12 phút; `lec-11-topic-03` 12 phút + 4 phút linh hoạt + 8 phút X01; `lec-11-topic-04` 10 phút; `lec-11-topic-05` 8 phút; `lec-11-topic-06` 7 phút; `lec-11-topic-07` 8 phút; `lec-11-topic-08` 10 + 12 (X02) phút; `lec-11-topic-09` 6 phút; `lec-11-topic-10` 18 phút; `lec-11-topic-11` 8 (+6 linh hoạt) phút; `lec-11-topic-12` 4 + 10 (X03) phút; `lec-11-topic-13` —.

Câu cuối của bản đồ: "Tổng nội dung giảng 110 phút (96 phút cốt lõi và 14 phút bổ sung), linh hoạt 10 phút, bài tập 30 phút (8 + 12 + 10); toàn buổi 150 phút."

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
