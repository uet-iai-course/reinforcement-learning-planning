# Dàn ý Bài 10: TRPO và PPO

## Phạm vi và mục tiêu

Nguồn chính: `RL-hk2-2025-2026/lecture10_policy_gradient_part2.pdf`, 43 trang. Tiêu đề metadata ghi “Part 1”, còn nội dung tiếp nối Bài 09 và tập trung vào TRPO, PPO, GAE cùng các chi tiết triển khai. Tệp đích dùng tên nội dung `lecture-10-trpo-va-ppo.html`.

Đối tượng là sinh viên đại học đã biết quy trình quyết định Markov, xấp xỉ hàm, DQN, hàm điểm và REINFORCE. Sau bài, sinh viên có thể:

1. chứng minh baseline độc lập hành động không đổi kỳ vọng gradient;
2. phân biệt actor–critic dùng đích Monte Carlo với actor–critic TD/GAE;
3. tính GAE với mặt nạ kết thúc MDP và mặt nạ tiếp diễn rollout;
4. giải bài toán natural gradient hai chiều của TRPO;
5. tính PPO-Clip đúng cho cả hai dấu của lợi thế;
6. phân biệt lợi thế thô, lợi thế actor đã chuẩn hóa và target critic;
7. kiểm tra loss, schema batch, kích thước, đại lượng đóng băng và chẩn đoán PPO;
8. phân biệt kỳ vọng occupancy chiết khấu với trung bình đều trên batch;
9. nêu đúng phạm vi của kết quả hội tụ về điểm dừng.

Không có code demo vì nguồn không cung cấp chương trình. Các thuật toán A3C/A2C, DPG, DDPG, SAC, TD3, IMPALA, PPG, SPO và SAM+PPO không được mở thành tuyến nội dung riêng.

## Cấu trúc và thời lượng

| cụm | trang | phút cốt lõi | phút bổ sung |
|---|---|---:|---:|
| Cầu nối và REINFORCE | `L10-01`–`L10-05` | 12 | 0 |
| Baseline và actor–critic | `L10-06`–`L10-09` | 11 | 0 |
| GAE | `L10-10`–`L10-12` | 12 | 5 |
| TRPO | `L10-13`–`L10-20` | 25 | 0 |
| PPO-Clip và loss | `L10-21`–`L10-28` | 25 | 5 |
| Quy trình và triển khai | `L10-29`–`L10-35` | 14 | 0 |
| So sánh, lý thuyết và tổng kết | `L10-36`, `L10-37`, `L10-37B`, `L10-38` | 11 | 0 |
| Tổng | 39 trang chính | 110 | 10 |

Ba bài tập dọc `X01`, `X02`, `X03` dùng lần lượt 10, 8 và 12 phút, tổng 30 phút.

Phần linh hoạt gồm đúng hai mục: diễn giải sâu đồ thị và đánh đổi GAE ở `L10-10` (5 phút), khai triển shape và broadcasting ở `L10-28` (5 phút). Nhãn linh hoạt chỉ dùng trong planning, không đưa lên mặt trang chiếu hoặc ghi chú diễn giả.

Mốc ba tiết 50 phút: tiết 1 dừng sau `L10-16`; tiết 2 dừng sau `L10-32`; tiết 3 dùng khoảng 20 phút cho `L10-33`–`L10-38` kể cả `L10-37B`, và 30 phút cho `X01`–`X03`. Nếu trễ thêm sau khi đã bỏ 10 phút linh hoạt, nén lời giảng `L10-33`–`L10-34` và bảng so sánh `L10-36`; không bỏ schema batch, chẩn đoán định lượng hoặc hai trang lý thuyết.

## Ánh xạ nguồn

| trang nguồn | quyết định | trang đích | lý do |
|---|---|---|---|
| 1–3 | sửa, gộp | `L10-01`–`L10-02` | Xác định kết quả học tập; lược danh sách thuật toán ngoài phạm vi. |
| 4–5 | giữ, sửa | `L10-03`–`L10-04` | Giữ vấn đề phân bố đổi; chuẩn hóa reward thành $R_{t+1}$. |
| 6–10 | gộp, sửa | `L10-05` | Bài 09 đã suy diễn theorem; giữ REINFORCE, thêm $\gamma^t$ theo $J=\mathbb E[G_0]$ và đánh giá $\nabla_\theta\log\pi_\theta$ tại $\theta_{\mathrm{old}}$. |
| 11 | tách, sửa | `L10-06`–`L10-07`, `X01` | Thêm chứng minh rời rạc, điều kiện tích phân liên tục, dừng gradient và ví dụ $b=4$. |
| 12 | sửa | `L10-08`–`L10-09` | Phân biệt actor–critic Monte Carlo với actor–critic TD/GAE; nêu quy ước cục bộ của bài. |
| 13 | tách, sửa | `L10-10`–`L10-12`, `X01` | Thêm lợi thế thô, mặt nạ terminal/truncation ngoại sinh, đệ quy hữu hạn và ví dụ số. |
| 14 | tách, sửa | `L10-13`–`L10-14` | Đặt vấn đề bước cập nhật phá chính sách, rồi mới cho trực giác miền tin cậy bằng SVG. |
| 15 | tách, sửa | `L10-15`–`L10-16` | Đưa ví dụ nhỏ và điều kiện hỗ trợ trước; sau đó nối identity, old-occupancy approximation và empirical average-KL. |
| 16 | gộp, sửa | `L10-16` | Định nghĩa $\mathbb E_{\mathrm{disc},\pi}$ và $\mathbb E_B$; nêu cùng $\rho_0$, $\gamma&lt;1$, trạng thái hấp thụ zero-reward và nguồn TRPO gốc. |
| 17 | tách, sửa | `L10-17`–`L10-18`, `X02` | Phân biệt $F$ là Hessian KL/kỳ vọng score outer product với $\widehat F$ Monte Carlo; ví dụ $\eta=0$ giả sử SPD. |
| 18–19 | gộp, sửa | `L10-19`–`L10-20` | CG giải hệ $\widehat F+\eta I$ SPD, có residual/max-iteration và chi phí FVP; line search áp dụng hai tiêu chí nhận bước. |
| 20–22 | tách, sửa | `L10-21`–`L10-26` | Đi theo vấn đề → trực giác tỷ số và đoạn phẳng → hai số đại diện → công thức từng dấu → trong/ngoài dải → giới hạn hard-KL. |
| 23 | sửa | `L10-27` | Tách $\widehat A^{\mathrm{raw}}$, $\widehat A^{\mathrm{actor}}$ và $\widehat V$; giữ target critic thô và dừng gradient đúng đường. |
| 24–25 | tách, sửa | `L10-28`–`L10-30`, `X03` | Thêm shape hành động rời rạc/liên tục, schema lưu/suy ra/tính lại và hợp đồng `final_observation` trước reset ở biên rollout. |
| 26–28 | gộp, sửa | `L10-31`–`L10-32`, `L10-36` | Nêu chẩn đoán, tương tác siêu tham số và so sánh có giới hạn. |
| 29–30 | giữ, sửa | `L10-33` | Ghi value clipping là biến thể, không phải định nghĩa PPO. |
| 31–34 | gộp, sửa | `L10-34`–`L10-35` | Giữ nhóm lựa chọn triển khai; hạ mức khẳng định thực hành. |
| 35–36 | gộp, sửa | `L10-31`, `L10-35` | Định nghĩa clipfrac, approxKL, explained variance và chuyển checklist thành trường tái lập. |
| 37–42 | tách, sửa | `L10-37`, `L10-37B` | Tách mô hình vòng ngoài–vòng trong/PPO-Penalty khỏi kết quả điểm dừng có điều kiện; không tuyên bố PPO thực hành hội tụ. |
| 43 | giữ, sửa nguồn | ghi chú nguồn toàn bài | Giữ Williams; Schulman et al.; Engstrom et al.; dẫn chính xác Jin, Li và Wang, ICLR 2024, Định lý 3.1 và Giả thiết 3.1, 3.2, 3.4. |

## Thuật ngữ và ký hiệu

| ký hiệu | nghĩa |
|---|---|
| $R_{t+1}$ | phần thưởng nhận sau hành động $A_t$ |
| $G_t$ | return chiết khấu từ thời điểm $t$ |
| $m_t$ | mặt nạ bootstrap: bằng $0$ chỉ khi MDP kết thúc thật |
| $c_t$ | mặt nạ tiếp diễn GAE: bằng $0$ tại terminal, reset hoặc cuối rollout |
| $\widehat A_t^{\mathrm{raw}}$ | lợi thế thô từ GAE, trước chuẩn hóa |
| $\widehat A_t^{\mathrm{actor}}$ | lợi thế thô được chuẩn hóa trên batch và dừng gradient |
| $\widehat V_t$ | $\operatorname{sg}(V_{\mathrm{old}}(S_t)+\widehat A_t^{\mathrm{raw}})$, target critic đóng băng |
| $w_t(\theta)$ | tỷ số $\pi_\theta(A_t\mid S_t)/\pi_{\mathrm{old}}(A_t\mid S_t)$ |
| $\mathbb E_{\mathrm{disc},\pi}$ | kỳ vọng theo occupancy chiết khấu đã chuẩn hóa và hành động từ $\pi$ |
| $\mathbb E_B$ | trung bình đều trên $B=HN$ mẫu thực hành |
| $F$ | Fisher lý tưởng: Hessian average-KL và kỳ vọng score outer product trên hành động từ $\pi_{\mathrm{old}}$ |
| $\widehat F$ | ước lượng Monte Carlo $B^{-1}\sum_tu_tu_t^\top$ dùng trong FVP/CG |
| $V_{\mathrm{boot}}$ | $V_{\mathrm{old}}(S_H)\in\mathbb R^N$ từ quan sát cuối trước reset; không dùng quan sát reset |
| $\delta$ | bán kính KL của TRPO |
| $\epsilon$ | nửa độ rộng clipping của PPO |
| $T$ | thời điểm episode kết thúc |
| $H,N,B$ | độ dài rollout, số môi trường và $B=HN$ mẫu |

## Tài sản SVG

- `policy-update-feedback.svg`: vòng phản hồi chính sách–dữ liệu;
- `actor-critic-advantage.svg`: actor, môi trường, critic và lợi thế;
- `gae-bias-variance.svg`: trục $\lambda$ và đánh đổi;
- `trpo-trust-region.svg`: ellipsoid Fisher và bước cục bộ;
- `ppo-clipping-signs.svg`: hai nhánh theo dấu lợi thế;
- `ppo-data-pipeline.svg`: rollout, buffer, GAE và minibatch;
- `ppo-diagnostics.svg`: bốn chẩn đoán triển khai.
