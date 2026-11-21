# Dàn ý Bài 10: TRPO và PPO

Bản hiện hành (2026-11-21, sau lượt sửa thứ hai theo năm vai rà), khớp bộ trang chiếu dựng lại `2627-1/lecture-10-trpo-va-ppo.html` (6 mạch, 88 trang; mạch 4 dựng lại theo đề xuất trình bày TRPO của tác giả, 2026-11-21) và `storyboard.md` (phần trước "Lịch sử (bản 2026-11-20)"). Phần DPO và học tăng cường từ phản hồi con người đã bỏ khỏi Bài 10 (người dùng 2026-11-21, `gop-y-tac-gia-deck-2026-11-20.md` mục #27); nội dung cắt lưu ở `dpo-chuyen-sang-bai-13.md` cho Bài 13. Dàn ý cũ (bảy, tám mạch, có Mục 7 DPO) giữ nguyên chữ ở cuối tệp, mục "Lịch sử (bản 2026-11-19)", chỉ để đối chiếu nhật ký.

## Phạm vi và nguồn

- Nguồn nội dung: ghi chú bài giảng đã sửa `materials/lec-10/lecture-note.md` (bỏ DPO, tổng kết là §7, Bài tập 10.23 là bài PPO-Clip trên chuỗi hai trạng thái); deck nguồn `RL-hk2-2025-2026/lecture10_policy_gradient_part2.pdf` (P1) giữ thứ tự ý chính: hai giới hạn của REINFORCE, đường cơ sở và lợi thế, GAE, hàm thay thế và miền tin cậy, TRPO, PPO.
- Quy tắc trình bày: TB1–TB33 và tinh chỉnh Đ1–Đ15 (`NGUYEN-TAC-HOC-PHAN.md` §3a), NT1–NT29 phần không bị thay, VP1–VP25.
- Câu chuyện của bài: `cau-chuyen-deck-2026-11-21.md`. Một ví dụ chung cho cả bài (TB25): chuỗi hai trạng thái, $\gamma=0{,}9$, chính sách $p_s=\sigma(\theta_s)$, $\theta=(0;\,\log2)$.
- Bài tập: `exercises.md` có Bài tập 10.13–10.17 và 10.22; ghi chú có 10.1–10.12 và 10.23; số 10.18–10.21 bỏ trống (BT4).
- Thời lượng: 120 phút trình chiếu trong 150 phút (P6); phút từng trang ở `storyboard.md` §5.

## Khung lý thuyết chung

- **Bài toán trung tâm** (ghi chú §1.1). (1) Ước lượng gradient chính sách có phương sai nhỏ mà kỳ vọng không đổi. (2) Dùng bước cập nhật dài, trên dữ liệu của chính sách cũ, mà hàm mục tiêu không giảm.
- **Đối tượng chung.** MDP hữu hạn, $\mu_0$, $P$; chính sách $\pi_\theta$, hàm điểm $\psi_\theta=\nabla_\theta\log\pi_\theta$; $v_\pi$, $q_\pi$, $A_\pi=q_\pi-v_\pi$; critic $\hat v(s,w)$, sai số TD $\delta_t$, GAE $\widehat A_t$; số lần thăm kỳ vọng có chiết khấu $\eta_\pi$, phân bố chiếm dụng $\nu^\pi=(1-\gamma)\eta_\pi$; hàm thay thế $\mathcal L_\pi(\pi')$, tỉ số chính sách $\rho$; $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$; ma trận Fisher $F$; $\mathcal L^{\mathrm{CPI}}$, $\mathcal L^{\mathrm{CLIP}}$, bộ đệm $\mathcal D$.
- **Giả thiết chung** (trang `L10-1-02`, Đ7): MDP hữu hạn, Markov; mọi chính sách cùng $P$, cùng $\mu_0$; $|R_{t+1}|\le R_{\max}$; $0\le\gamma<1$; chính sách Markov dừng, $\pi_\theta>0$, khả vi theo $\theta$. Mỗi kết quả ghi "giả thiết chung; thêm: …".
- **Chuỗi định nghĩa → kết quả → phương pháp.** Hai giới hạn của REINFORCE (phương sai $0{,}6925$; bước dài theo một lượt làm $J$ giảm) → đường cơ sở (Định nghĩa 10.1, Mệnh đề 10.2) → hàm lợi thế, gradient dạng lợi thế (Định nghĩa 10.4, Mệnh đề 10.5) → sai số TD với $v_\pi$ (Mệnh đề 10.8) → critic, actor (Định nghĩa 10.7) → lợi thế $n$ bước, GAE (Định nghĩa 10.11, 10.13, Mệnh đề 10.14, 10.15) → actor–critic với GAE → luồng 100 lượt, phân phối hành động và phân bố trạng thái (Ví dụ 10.11) → bổ đề chênh lệch hiệu năng (Định nghĩa 10.18, Bổ đề 10.19) → hàm thay thế, lấy mẫu quan trọng, tỉ số chính sách (Định nghĩa 10.21, Mệnh đề 10.22) → sai số dự báo và đoạn thẳng $\pi_t$ (Ví dụ 10.12) → bước tham số và thay đổi hành vi (Ví dụ 10.13), TV, KL (Định nghĩa 10.23) → bài toán miền tin cậy (Định nghĩa 10.24) → cơ sở lý thuyết: chặn cải thiện (Bổ đề 10.26, Định lý 10.27, Hệ quả 10.28, Mệnh đề 10.25, Hệ quả 10.30) → Fisher, gradient tự nhiên (Định nghĩa 10.32, Mệnh đề 10.33, 10.34) → TRPO (Thuật toán 10.37) → mục tiêu cắt (Định nghĩa 10.39, Mệnh đề 10.40) → PPO-Clip (Thuật toán 10.49).
- **Giới hạn áp dụng.** Đường cơ sở không phụ thuộc hành động đã chọn; critic sai làm sai số TD chệch; GAE không chệch cho gradient chỉ khi $\lambda=1$ trên lượt đầy đủ hoặc critic đúng; mọi bảo đảm của hàm thay thế và chặn cải thiện cần lợi thế, $\eta_\pi$ chính xác; TRPO chỉ bảo đảm trên bộ đệm; mục tiêu cắt không chặn KL; dữ liệu theo chính sách.

## Sáu mạch (deck dựng lại 2026-11-21)

HTML có 6 section ngoài (NT10). Mạch $k$ mở tại `#/k`; từ mạch 2, trang đầu là trang tiêu đề mạch `L10-k-00`, `id="mach-k"`. Mã trang theo `NGUYEN-TAC-HOC-PHAN.md` §5.

| Mạch | Tên (`h2`) | Dòng dẫn | Mục ghi chú | Đầu ra | Trang | Phút |
|---|---|---|---|---|---:|---:|
| 1 | Giới hạn của REINFORCE (mở đầu; bìa `L10-1-01`) | không có | Kiến thức tiên quyết, §1.1, Ví dụ 10.6 | chuỗi hai trạng thái, $J=1{,}4$, gradient $(0{,}2;\,0{,}3)$; phương sai $0{,}6925$; bước dài làm $J$ giảm; câu hỏi nhanh; hai câu hỏi | 11 | 17 |
| 2 | Đường cơ sở và hàm lợi thế | So lợi tức với giá trị của trạng thái giữ nguyên kỳ vọng của ước lượng gradient và giảm phương sai. | §2.1, §2.3, §2.4 | đường cơ sở, $A_\pi$, gradient dạng lợi thế, $\delta_t$ với $v_\pi$; phương sai $0{,}69\to0{,}20\to0$ | 11 | 18 |
| 3 | Ước lượng lợi thế: độ chệch và phương sai | Tổ hợp có trọng số các ước lượng lợi thế nhiều bước cân bằng độ chệch và phương sai. | §2.4 (critic), §3 | critic, actor, GAE, $\lambda$ cân bằng chệch và phương sai; thuật toán actor–critic với GAE | 13 | 21,5 |
| 4 | Hàm thay thế và miền tin cậy | Chính sách mới được đánh giá từ dữ liệu của chính sách cũ với sai số nhỏ khi hai chính sách gần nhau. | §4, §5 | luồng 100 lượt; bổ đề chênh lệch hiệu năng, hàm thay thế; bài toán miền tin cậy trước cơ sở lý thuyết (chặn cải thiện); hình học elip, gradient tự nhiên, TRPO | 29 | 37,5 |
| 5 | Tối ưu chính sách gần kề (PPO) | PPO cắt tỉ số chính sách để dùng lại một bộ đệm nhiều lần bằng gradient bậc một. | §6.1, §6.3 | mục tiêu cắt, PPO-Clip, so sánh TRPO–PPO, Bài tập 10.23 | 14 | 17 (+3,5 bài tập) |
| 6 | Tổng kết | Mỗi phương pháp của bài giảm phương sai hoặc giới hạn bước cập nhật dưới những giả thiết riêng. | §7 | sơ đồ neo cuối, câu trả lời có điều kiện, bảng kết quả, bảng phương pháp | 10 | 11 |
| **Tổng** | | | | | **88** | **122** |

"Nội dung" (`L10-1-08`) gồm sơ đồ neo `so-do-neo-m1.svg` và danh sách sáu mạch có liên kết `#/k`. Ngoại lệ số trang (88 trang thật, 87 trang đếm theo TB17) và hai ước lượng thời lượng (biên tập viên 122 phút; vai mạch truyện khoảng 145–155 phút) ghi ở `storyboard.md` §5, chờ tác giả; Bài tập 10.23 tính vào 30 phút bài tập. Mạch 1: câu hỏi nhanh `1-12` đứng giữa `1-04` và `1-05`. Mạch 6: câu trả lời câu 2 tách sang `6-18` ngay sau `6-11`.

## Bảng thuật ngữ Việt–Anh

Tên tiếng Anh trong ngoặc ở lần đầu trên mặt trang (VP2, NT21); các lần sau chỉ dùng tên tiếng Việt. Cột "lần đầu" là mã trang của deck hiện hành. Thuật ngữ đã có ở bài trước được nhắc lại, không kèm lại tên tiếng Anh.

| Tiếng Việt | Tiếng Anh | Quy ước | Lần đầu |
|---|---|---|---|
| hàm điểm | score function | $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$ | `L10-1-02` |
| giả thiết chung | — | tên của khối giả thiết dùng chung | `L10-1-02` |
| hệ số (của một bước) | — | số nhân với $\psi_t$ | `L10-1-02` |
| kỳ vọng; ước lượng không chệch; phương sai | expectation; unbiased estimator; variance | "kỳ vọng" cho biến ngẫu nhiên, "trung bình trên bộ đệm" cho mẫu hữu hạn (TB26) | `L10-1-02` |
| đường cơ sở | baseline | $b(s)$ | `L10-2-01` |
| hàm lợi thế, lợi thế | advantage function, advantage | $A_\pi$; ước lượng $\widehat A_t$ | `L10-2-06` |
| gradient dạng lợi thế | advantage form of the policy gradient | Mệnh đề 10.5(b) | `L10-2-09` |
| sai số TD | temporal-difference error | $\delta_t$, nhắc lại Bài 05 | `L10-2-07` |
| critic; actor; phương pháp actor–critic | critic; actor; actor–critic method | Định nghĩa 10.7; không dùng trước mạch 3 | `L10-3-01` |
| độ chệch | bias | kỳ vọng của ước lượng trừ đại lượng cần ước lượng | `L10-3-06` |
| tính chất tháp | tower property | kỳ vọng có điều kiện lồng nhau | `L10-2-10` |
| lợi tức $n$ bước; lợi thế $n$ bước | n-step return; n-step advantage | $G_{t:t+n}$, $\widehat A^{(n)}_t$; Bổ đề 10.12 trên trang | `L10-3-07` |
| lợi tức λ | λ-return | $G^\lambda_t$ | `L10-3-02` |
| ước lượng lợi thế tổng quát (GAE) | generalized advantage estimation | $\widehat A_t$, tham số $\lambda$ | `L10-3-02` |
| γ-just | γ-just | chỉ trong ghi chú diễn giả | `L10-3-09` |
| chính sách ứng viên | candidate policy | $\tilde\theta=(\log9;\,0)$, $\tilde\pi=(0{,}9;\,0{,}5)$ | `L10-4-01` |
| đoạn thẳng từ $\pi$ tới $\tilde\pi$ | — | $\pi_t=(1-t)\pi+t\tilde\pi$, $t\in[0,1]$ | `L10-4-01` |
| phân phối hành động; phân bố trạng thái | action distribution; state distribution | phân phối của hành động tại một trạng thái; tần suất gặp trạng thái (TB26, VP-RL-6) | `L10-4-27` |
| lợi thế của $\pi'$ so với $\pi$ | — | $A_\pi(s,\pi')$ | `L10-4-13` |
| bổ đề chênh lệch hiệu năng | performance difference lemma | Bổ đề 10.19 | `L10-4-02` |
| số lần thăm có chiết khấu | discounted visitation frequency | $\eta_\pi(s)=\sum_t\gamma^t\Pr_\pi(S_t=s,\,t<T)$ | `L10-4-02` |
| hàm thay thế | surrogate objective | $\mathcal L_\pi(\pi')$; $\Delta J$, $\Delta\mathcal L$ | `L10-4-03` |
| lấy mẫu quan trọng | importance sampling | như Định nghĩa 06.24 | `L10-4-11` |
| tỉ số chính sách; điều kiện hỗ trợ | probability ratio; support condition | $\rho(s,a)$, $\rho_t(\theta)$; "tỉ số", không "tỷ số"; $\pi'(a\mid s)\gt0\Rightarrow\pi(a\mid s)\gt0$ | `L10-4-11` |
| biến phân toàn phần (TV) | total variation distance | $D_{\mathrm{TV}}(q,q')$, $D_{\mathrm{TV}}(s)$ | `L10-4-12` |
| phân bố chiếm dụng | — (ghi chú không có tên tiếng Anh; không ghi trên deck) | $\nu^\pi=(1-\gamma)\eta_\pi$ | `L10-4-07` |
| chặn cải thiện | policy improvement bound | Hệ quả 10.28 ở `L10-4-21`, Định lý 10.27 ở `L10-4-06` | `L10-4-21` |
| phân kỳ Kullback–Leibler (KL); KL trung bình | Kullback–Leibler divergence | $D_{\mathrm{KL}}(s)$ chiều cũ‖mới; $\bar D_{\mathrm{KL}}=\sum_s\nu^\pi(s)D_{\mathrm{KL}}(s)$ | `L10-4-12` |
| bất đẳng thức Pinsker | Pinsker's inequality | tên riêng | `L10-4-20` |
| bổ đề dịch chuyển phân bố chiếm dụng | — | Bổ đề 10.26; ghi chú không có tên tiếng Anh | `L10-4-24` |
| miền tin cậy; bài toán miền tin cậy | trust region; trust region problem | bán kính $\kappa$ | `L10-4-07` |
| ma trận thông tin Fisher | Fisher information matrix | $F$ | `L10-4-22` |
| gradient tự nhiên | natural gradient | $F^{-1}g$; dòng "Ký hiệu:" trước mệnh đề | `L10-4-08` |
| tối ưu chính sách miền tin cậy (TRPO) | trust region policy optimization | sau lần đầu viết TRPO | `L10-4-09` |
| gradient liên hợp; tích Fisher–vector | conjugate gradient; Fisher–vector product | | `L10-4-09` |
| tìm kiếm lùi | backtracking line search | hệ số co $\zeta$ | `L10-4-09` |
| bộ đệm | buffer | $\mathcal D$ | `L10-4-09` |
| hàm thay thế mẫu; lặp chính sách bảo thủ (CPI) | sample surrogate; conservative policy iteration | $\mathcal L^{\mathrm{CPI}}$ | `L10-5-09` |
| mục tiêu cắt; bán kính cắt; đoạn phẳng | clipped surrogate objective; clip range | $\mathcal L^{\mathrm{CLIP}}$, $\epsilon$; đoạn phẳng là khoảng $\rho_t$ có gradient theo mẫu bằng $0$ | `L10-5-02` |
| vòng trong | inner loop | bước 3 của PPO-Clip, $K$ lần qua bộ đệm | `L10-5-05` |
| cải thiện đơn điệu | monotonic improvement | Hệ quả 10.30, $\mathcal M_k$ | `L10-4-29` |
| cực đại hóa qua hàm chặn dưới | minorize–maximize (MM) | chỉ ở ghi chú diễn giả | `L10-4-29` |
| tối ưu chính sách gần kề (PPO) | proximal policy optimization | tên mạch 5; tên tiếng Anh ở trang thuật toán | `L10-5-00`; `L10-5-07` |
| lô nhỏ; số lần qua bộ đệm; dừng sớm | mini-batch; epoch; early stopping | $M$; $K$; theo KL ước lượng trên bộ đệm | `L10-5-07` |

Thuật ngữ không dùng trên deck hiện hành (chỉ ở ghi chú): đường cơ sở có phương sai nhỏ nhất, PPO-Penalty, entropy, hàm mất mát tổng, approxKL, tỉ lệ cắt, phương sai được giải thích, cắt mất mát giá trị, điểm dừng, đoạn thu và cờ cắt ngắn (chỉ ở câu hỏi tự kiểm tra 4 và ghi chú diễn giả). Từ khẩu ngữ bị bỏ theo #11, #12 (TB26): "đoán/thật", "học dở", "dao động", "đi quá xa", "nơi chính sách tới", "trừ một mức".

## Quyết định ký hiệu

- Ví dụ chung: $p_s=\pi_\theta(1\mid s)=\sigma(\theta_s)$; mọi chính sách viết theo $\theta=(\theta_A;\,\theta_B)$ và đọc qua $(p_A;\,p_B)$.
- Phát biểu tổng quát dùng $\pi$ (cũ) và $\pi'$ (mới bất kỳ); chính sách ứng viên của ví dụ là $\tilde\theta$, $\tilde\pi$ (TB25).
- Mạch 4 dùng $\eta_\pi$ trên mặt trang cho bổ đề chênh lệch hiệu năng và hàm thay thế; $\nu^\pi=(1-\gamma)\eta_\pi$ dùng từ bài toán miền tin cậy (`L10-4-07`: KL trung bình, hàm mục tiêu dạng tỉ số), rồi ở bổ đề dịch chuyển, định lý chặn cải thiện và Fisher.
- Đoạn thẳng $\pi_t=(1-t)\pi+t\tilde\pi$, $t\in[0,1]$, trong tọa độ xác suất (`L10-4-01`); $t=0{,}25$ cho $(0{,}6;\,0{,}625)$.
- Critic sai của ví dụ: $\hat v=(1{,}4;\,1)$, giả định trên mặt trang. Bộ đệm chung của mạch 5: hai lượt $s_A\xrightarrow1s_B\xrightarrow2$, $s_A\xrightarrow2$, $\lambda=1$.
- $\epsilon$ là bán kính cắt, $\kappa$ là bán kính KL, $\zeta$ là hệ số co, $\delta_t$ chỉ là sai số TD; $\log$ tự nhiên; dấu phẩy thập phân, tọa độ ngăn bằng dấu chấm phẩy.

## Phân loại chủ đề

Phân loại bốn nhóm chỉ nằm ở đây, không vào ghi chú (GC-RL-12). Số mục theo ghi chú sau khi bỏ DPO (tổng kết là §7).

| `note-topic-id` | Phần ghi chú | Nhóm | Lý do ngắn |
|---|---|---|---|
| `lec-10-topic-01` | Kiến thức tiên quyết, Bảng ký hiệu | cầu nối | nhắc lại Bài 03–09 và kiến thức học máy |
| `lec-10-topic-02` | Mục tiêu, §1.1 | cầu nối | kết quả kế thừa, bài toán trung tâm hai phần |
| `lec-10-topic-03` | §2.1 Đường cơ sở | cốt lõi | |
| `lec-10-topic-04` | §2.2 Đường cơ sở có phương sai nhỏ nhất | bổ sung | Greensmith và cộng sự (2004) |
| `lec-10-topic-05` | §2.3 Hàm lợi thế | cốt lõi | |
| `lec-10-topic-06` | §2.4 Critic và actor–critic một bước | cốt lõi | |
| `lec-10-topic-07` | §3.1 Lợi tức n bước | cầu nối | nhắc lại Bài 07 cho GAE |
| `lec-10-topic-08` | §3.2 Lợi tức λ và GAE | cốt lõi | |
| `lec-10-topic-09` | §3.3 GAE trên đoạn thu | cốt lõi | |
| `lec-10-topic-10` | §4.1 Đánh giá chính sách mới trước khi chạy | cốt lõi | luồng 100 lượt, bổ đề chênh lệch hiệu năng |
| `lec-10-topic-11` | §4.2 Hàm thay thế | cốt lõi | lấy mẫu quan trọng, tỉ số chính sách |
| `lec-10-topic-25` | §4.3 Sai số dự báo theo độ dài bước | cốt lõi | đóng góp từng trạng thái, đoạn thẳng; mã dùng lại (quyết định 6 của điều phối viên, 2026-11-21) |
| `lec-10-topic-12` | §4.4 Đo thay đổi chính sách | cốt lõi | TV, KL; KL là thước đo của bài toán miền tin cậy (đổi từ cầu nối, 2026-11-21) |
| `lec-10-topic-14` | §4.5 Bài toán miền tin cậy | cốt lõi | đứng trước cơ sở lý thuyết (tinh chỉnh TB27) |
| `lec-10-topic-13` | §4.6 Cơ sở lý thuyết | cốt lõi | Pinsker, dịch chuyển, chặn cải thiện, cải thiện đơn điệu |
| `lec-10-topic-15` | §5.1 KL bậc hai và gradient tự nhiên | cốt lõi | |
| `lec-10-topic-16` | §5.2 TRPO thực hành | cốt lõi | |
| `lec-10-topic-17` | §6.1 PPO-Clip | cốt lõi | |
| `lec-10-topic-18` | §6.2 PPO-Penalty | cốt lõi | không lên deck hiện hành |
| `lec-10-topic-19` | §6.3 Hàm mất mát tổng và thuật toán PPO | cốt lõi | Thuật toán 10.49 |
| `lec-10-topic-20` | §6.4 Chẩn đoán và siêu tham số | cốt lõi | không lên deck hiện hành (TB4) |
| `lec-10-topic-21` | §6.5 Chi tiết cài đặt | cốt lõi | chỉ ở ghi chú diễn giả |
| `lec-10-topic-22` | §6.6 Hội tụ về điểm dừng của PPO-Clip | đọc thêm | Jin, Li và Wang (2024) |
| `lec-10-topic-23` | §7.1–7.5 Tổng kết | cầu nối | tổng hợp, không khái niệm mới |
| `lec-10-topic-24` | §7.6 Giới hạn còn lại | cầu nối | |

Tổng (sau khi bỏ DPO và dựng lại mạch 4, 2026-11-21): cốt lõi 18 (03, 05, 06, 08–21, 25), cầu nối 5 (01, 02, 07, 23, 24), bổ sung 1 (04), đọc thêm 1 (22). Mã `lec-10-topic-25` nay thuộc §4.3 của Bài 10 (quyết định 6 của điều phối viên, 2026-11-21); các mục DPO lấy mã của Bài 13 khi dựng bài đó. Hàng xếp theo thứ tự mục của ghi chú, nên mã không tăng dần.

## Ánh xạ trang ↔ khối ghi chú, hình, thời lượng

Bản hiện hành nằm ở `storyboard.md`: dòng "Ghi chú nguồn" của từng trang (§3), danh sách hình (§4), thời lượng (§5), đối chiếu mã trang cũ và mới (§6). Các bảng cùng loại trong phần lịch sử dưới đây dùng mã trang của các bản 2026-11-13 và 2026-11-19, không còn hiệu lực.

---

Mạch 3 có thêm `3-13` "Critic hồi quy về lợi tức λ" (mục tiêu $V^{\mathrm{targ}}_t=\widehat A_t+\hat v(S_t,w_{\mathrm{old}})=G^\lambda_t$ và bước cập nhật critic; góp ý tác giả #2, #3). Thuật toán TRPO (`4-09`, `4-26`) và PPO-Clip (`5-07`, `5-14`) tách hai trang để mọi đại lượng có công thức tại bước tính nó (góp ý tác giả #1).

Tiêu đề mạch 4 sau lượt sửa theo năm vai (2026-11-21, `ra-soat-mach4-2026-11-21.md` B2): `4-01` "Hướng làm $J$ tăng chưa cho biết độ dài bước", `4-04` "Sai số của dự báo trên đoạn thẳng là $-0{,}18t^2$", `4-28` "Cùng $\Delta\theta$, hai mức thay đổi phân phối hành động", `4-32` (mới, tách từ `4-07`) "Ví dụ: miền tin cậy $\kappa=0{,}01$ loại $\tilde\pi$", cụm lý thuyết mang tiền tố "Cơ sở lý thuyết: …" (`4-14`, `4-20`, `4-24`, `4-06`, `4-19` "… chặn cải thiện đúng nhưng lỏng", `4-29`), `4-31` "Hàm thay thế, miền tin cậy và gradient tự nhiên".

Mạch 4 dựng lại (2026-11-21) theo đề xuất trình bày TRPO của tác giả và `storyboard.md` §3 mạch 4: 29 trang (`4-07` tách thành `4-07` và `4-32` sau năm vai rà), thứ tự `4-00`, `4-01`, `4-27`, `4-13`, `4-02`, `4-03`, `4-11`, `4-16`, `4-04`, `4-10`, `4-17`, `4-28`, `4-12`, `4-07`, `4-32`, `4-21`, cụm cơ sở lý thuyết `4-14`, `4-20`, `4-24`, `4-06`, `4-19`, `4-29`, rồi `4-22`, `4-30`, `4-08`, `4-25`, `4-09`, `4-26`, `4-31`. Bỏ `4-05`, `4-15`, `4-18`, `4-23`. Chỗ lệch storyboard khi dựng: `storyboard.md` §10, mục "Ghi chú khi dựng mạch 4 (2026-11-21)".

# Lịch sử (bản 2026-11-19)

Phần dưới là dàn ý bản 2026-11-19 (bảy mạch, sau đó tám mạch có Mục 7 DPO), giữ nguyên chữ, mọi tiêu đề hạ một bậc. Không còn hiệu lực; chỉ để đối chiếu nhật ký rà.

## Dàn ý Bài 10: TRPO, PPO và DPO

Tên hiển thị đổi từ "TRPO và PPO" theo Q6 (2026-11-19); tên tệp `lecture-10-trpo-va-ppo.html` và mọi đường dẫn giữ nguyên.

### Bổ sung DPO (giai đoạn I.1, 2026-11-19)

- **Việc của lượt này.** Thêm mục `## 7. Tối ưu chính sách từ phản hồi ưu tiên` vào ghi chú, sau §6 (PPO); §7 cũ "Tổng kết và chuyển tiếp" thành `## 8. Tổng kết`, tiểu mục 7.1–7.6 thành 8.1–8.6 (Q3, GC-RL-15). Bổ sung vào bài đã có, không dựng lại bài; §1–§6 chỉ sửa đúng các chỗ liệt kê ở mục "Các chỗ sửa ngoài Mục 7 và Mục 8" dưới đây. Thứ tự sản phẩm: ghi chú → `exercises.md` → deck (BT-RL-9).
- **Đầu vào đã duyệt.** `prompt-bo-sung-dpo-bai-10.md` (bảng Q, Q1–Q9 "Theo đề xuất", tác giả 2026-11-19) và `ke-hoach-bo-sung-dpo.md` (kế hoạch A–C). Chỗ hai tệp khác nhau thì bảng Q thắng. Quy định học phần đã ghi: GC-RL-18 (trần 37 000 từ `prose`), BT-RL-10 (số bài tập), "P1, Bài 10, Mục 7 (riêng)" ở mục 3 của `NGUYEN-TAC-HOC-PHAN.md`.
- **Luận điểm trọng tâm (tác giả).** PPO trong RLHF và DPO xuất phát từ cùng một mục tiêu $\max_\pi\mathbb E_x\bigl[\mathbb E_{y\sim\pi}r(x,y)-\beta D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})\bigr]$ với $\pi_{\mathrm{ref}}$ cố định, nghiệm dạng đóng $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$. RLHF khớp một mô hình phần thưởng rồi chạy PPO với mẫu sinh trực tuyến; DPO đổi biến phần thưởng thành $\beta\log(\pi/\pi_{\mathrm{ref}})$, hàm phân hoạch triệt tiêu trong mô hình Bradley–Terry, còn lại một hàm mất mát phân loại trên dữ liệu ưu tiên cố định. Hai con đường trùng nhau chỉ dưới giả thiết của định lý tương đương. Hai mỏ neo khác nhau: $\pi_{\mathrm{old}}$ của PPO đổi sau mỗi vòng và giới hạn bước, $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$ ở Định nghĩa 10.43; $\pi_{\mathrm{ref}}$ của RLHF cố định và điều chuẩn nghiệm cuối, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$. Mọi phần của Mục 7 phục vụ luận điểm này; nó xuất hiện ở Định lý 10.57, Định lý 10.65, bảng so sánh §7.5, phần 6 của §8.3 và Tóm tắt chương.
- **Nguồn (Q1).** Không có trang chiếu nguồn và không giáo trình nào của GC-RL-5 trình bày chủ đề. Phạm vi và thứ tự theo mục lục giáo trình của học phần, Chương 13 (trang PDF 13, trang in xi, đã đối chiếu): 13.4 Học phần thưởng từ phản hồi ưu tiên (13.4.1, 13.4.2), 13.5 Học tăng cường từ phản hồi con người (13.5.1, 13.5.2), 13.6 Phương pháp căn chỉnh trực tiếp (13.6.1). Nội dung theo tám bài báo lưu ở `/data/tqlong/qa/sources/*-20261119/`, dẫn số phương trình, mục, định lý đã kiểm trong `extracted.md`; chỗ dẫn từng tiểu mục ở mục "Mục 7 của ghi chú". Ghi chú đã kiểm định là chuẩn nội dung duy nhất của mạch 7 deck.
- **Số hiệu (Q3, Q4).** Khối 10.52–10.70 (tiếp sau Nhận xét 10.51); Ví dụ 10.23–10.28; Tình huống 10.4–10.5; `note-topic-id` `lec-10-topic-25` … `-30` (chú thích 2026-11-21: phần DPO đã bỏ khỏi Bài 10; mã `lec-10-topic-25` được dùng lại cho §4.3 "Sai số dự báo theo độ dài bước", các mã còn lại không dùng); Bài tập củng cố mới 10.18–10.21 (ghi chú nhảy từ 10.12 sang 10.18, BT-RL-10); `exercises.md` giữ 10.13–10.17 và thêm Bài tập 10.22. Hai mã của phần kết, `lec-10-topic-23` và `-24`, giữ nguyên để không đổi `data-note-topic-id` của deck, nên mã chủ đề không theo thứ tự đọc.
- **Độ dài (Q2, GC-RL-18).** Mục mới 4 000–5 000 từ `prose`, các chỗ sửa khác không quá 2 800; ghi chú lên khoảng 36 600, trần 37 000. Ngân sách theo tiểu mục ở mục "Mục 7 của ghi chú".
- **Điểm dừng (Q9).** Sau I.3 (outline và phân tích nguồn), sau giai đoạn I, sau III.2 (storyboard).

### Phạm vi (Giai đoạn II, viết lại 2026-11-04)

- Nguồn chính của bộ trang chiếu: ghi chú bài giảng đã duyệt `materials/lec-10/lecture-note.md` (commit `1c9ef05`; commit `567c96c` chỉ bỏ mục "Bản đồ chủ đề" theo yêu cầu người dùng, ghi chú ngắn đi 63 dòng, số hiệu khối và mốc `note-topic-id` không đổi). Bộ trang chiếu tóm tắt ghi chú: cùng thuật ngữ, ký hiệu, giả thiết, ví dụ, số hiệu kết quả và thứ tự khái niệm, trừ các sai khác ghi ở mục "Sai khác có chủ ý".
- Nguồn bài giảng gốc: `RL-hk2-2025-2026/lecture10_policy_gradient_part2.pdf`, 43 trang (trang bìa ghi "Lecture 10: Overview on Policy Gradient Algorithms, Part 1"). Phần I (tr. 3–42) thuộc bài này; Phần II (A3C, DDPG, SAC, …) thuộc Bài 11 và chỉ xuất hiện trong một dòng nối ở trang cuối (dòng nối này bỏ theo Q8, 2026-11-19).
- Kế hoạch đã duyệt: kế hoạch bộ trang chiếu của điều phối viên (7 mạch, 101 trang), áp dụng phương án nén 11 cặp trang thành 90 trang; cổng storyboard (2026-11-04, hai lần) tách lại năm trang (`L10-110`, `L10-412`, `L10-510`, `L10-608`, `L10-710`), còn 95 trang; bản viết tách `L10-212b`, `L10-702b`, và đợt sửa D1 (sau năm báo cáo rà soát, 2026-11-04) tách `L10-412b`, `L10-502b`, `L10-611b`, `L10-617b`: **101 trang**, giữ phút từng mạch $12+23+14{,}5+22{,}5+13{,}5+25{,}5+9=120$. Ghi chú bài giảng dùng làm nguồn ở D1 là bản sau commit `9a5478a` (sửa ví dụ miền tin cậy sau Hệ quả 10.31 và Ví dụ 10.4). Mã trang đánh số liên tiếp; bảng đối chiếu mã kế hoạch → mã mới ở cuối `storyboard.md`.
- Bản cũ: bộ trang chiếu `lecture-10-trpo-va-ppo.html` (42 trang, mã `L10-01`…`L10-38`, `L10-37B`, `X01`–`X03`, ký hiệu $w_t$) và các tệp `outline.md`, `storyboard.md` cũ (còn trong git) viết trước chuẩn hiện hành; chỉ dùng để ghi quyết định so với bản cũ. `note-for-author.md` thuộc vòng soạn cũ, các cảnh báo của nó đã được ghi chú bài giảng mới xử lý; tệp này không phải đầu vào của vòng này.
- Bài tập: chưa có `materials/lec-10/exercises.md`. Trang "Bài tập về nhà và tài liệu đọc" ánh xạ Bài tập củng cố 10.1–10.12 của ghi chú theo mạch và liên kết viewer của ghi chú bài giảng. Cập nhật 2026-11-13: `exercises.md` có Bài tập 10.13–10.17 (làm lại 2026-11-12); `L10-709` chép bảng mạch của tệp đó (bảy hàng, tách cột tệp bài tập và cột ghi chú).
- Thời lượng: 120 phút trình chiếu; 30 phút còn lại chữa bài (lời giải đầy đủ của bài tập trên trang và bài về nhà). Sau bổ sung DPO: 135 phút trình chiếu, 15 phút chữa bài (Q7; mục "Phân bổ thời lượng").

### Khung lý thuyết chung

**Bài toán trung tâm** (ghi chú §1.1). Giảm phương sai của ước lượng gradient chính sách mà vẫn giữ kỳ vọng của nó, và dùng lại dữ liệu của $\pi_{\mathrm{old}}$ để chọn một bước cập nhật lớn mà chính sách mới không kém chính sách cũ. Hai nửa ứng với hai hàng của hình `img/lec-10/central-problem.svg`: hàng trên (mạch 2–3) chọn hệ số nhân với hàm điểm, hàng dưới (mạch 4–6) giới hạn độ lớn bước; hai hàng gặp nhau ở Thuật toán 10.49 (PPO kiểu actor–critic).

*Phần thứ ba (Q3, 2026-11-19).* Cuối đoạn bài toán trung tâm ở §1.1 thêm một câu, bản nháp (`no-ai-slop` Edit; tác tử soạn chỉnh lần cuối): "Khi phần thưởng chỉ được biết qua các phép so sánh ưu tiên, bài toán có thêm phần thứ ba: tìm chính sách cực đại hóa phần thưởng mà vẫn ở gần một chính sách tham chiếu cố định." Câu nêu bài toán, không nêu cách giải (bản nháp của kế hoạch A2 nêu luôn phép phạt KL; cách giải để dành cho Mục 7). Hình `central-problem.svg` thêm hàng thứ ba "Mục 7: phạt KL theo $\pi_{\mathrm{ref}}$ cố định; RLHF với PPO, DPO", nối vào khung PPO; đoạn đọc hình sau đó thêm một câu cho hàng này. Trên deck: một dòng của `L10-109`, câu thứ ba của `L10-110` (giai đoạn III). Bài toán trung tâm có ba phần ứng với ba hàng của hình: hàng trên (Mục 2–3), hàng dưới (Mục 4–6), hàng thứ ba (Mục 7); §8.3 trả lời bằng sáu phần.

**Đối tượng và ký hiệu chung** (bảng ký hiệu của ghi chú).

- MDP hữu hạn; $\mathcal S$ là tập trạng thái chưa kết thúc, $\mathcal A$ hữu hạn với $m$ hành động; $R_{t+1}$ nhận sau $A_t$; lượt kết thúc tại $T$, sau đó là trạng thái hấp thụ với $G_T=0$ và $v_\pi=q_\pi=A_\pi=0$; $\gamma\in[0,1)$ trong các định lý. Hành lang ngắn có $\gamma=1$, nằm ngoài giả thiết và chỉ dùng ở mạch 1–2.
- $\mu_0$ (Bài 09 viết $\rho_0$), $P(s'\mid s,a)$, $P_\pi$, $\Gamma_\pi=(I-\gamma P_\pi)^{-1}$.
- $\pi_\theta$, $\theta\in\mathbb R^d$; $\theta_{\mathrm{old}}$, $\pi_{\mathrm{old}}$ là tham số và chính sách sinh dữ liệu; $\psi_\theta=\nabla_\theta\log\pi_\theta$, $\psi_t$ ($=0$ khi $t\ge T$); $H_t$ lịch sử.
- $v_\pi$, $q_\pi$, $A_\pi=q_\pi-v_\pi$, $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$. Chữ $A$ hai vai: $A_t$ (chỉ số thời gian) là hành động; $A_\pi$, $\widehat A_t$ là lợi thế.
- $b(s)$ đường cơ sở; $\hat v(s,w)$ critic, $w_{\mathrm{old}}$, $\hat v_{\mathrm{old}}$; $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)-\hat v(S_t,w)$; cờ $Z_{t+1}$ (kết thúc của MDP), $U_{t+1}$ (cắt ngắn).
- $G_{t:t+n}$, $\widehat A^{(n)}_t$, $G^\lambda_t$, $\widehat A_t$ (GAE); từ mạch 6: $\widehat A^{\mathrm{raw}}_t$ (trước chuẩn hóa), $V^{\mathrm{targ}}_t=\widehat A^{\mathrm{raw}}_t+\hat v_{\mathrm{old}}(S_t)$.
- $\nu^\pi(s)=(1-\gamma)\sum_t\gamma^t\Pr_\pi(S_t=s,\,t<T)$ trên $\mathcal S$, khối $\le1$.
- $\rho_\theta(s,a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$, $\rho_t(\theta)$; $\mathcal L_{\theta_{\mathrm{old}}}$, $\mathcal L^{\mathrm{CPI}}$, $\mathcal L^{\mathrm{CLIP}}$, $\ell^{\mathrm{CLIP}}_t$ (cực đại hóa); $L(\theta,w)$, $L^V$ (cực tiểu hóa).
- $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$ (theo $\nu^{\mathrm{old}}$), $\widehat D$ (trung bình trên bộ đệm), $\mathcal H$; $\kappa$, $\kappa_{\mathrm{targ}}$; $\chi_{\pi'}$, $\bar\chi$; $F$, $g$, $\Delta$; $\epsilon$, $\beta$, $c_1$, $c_2$; $N$, $h$, $K$, $M$; $\mathcal D$, $\mathcal B$.
- Quy ước: $\log$ tự nhiên; dấu phẩy thập phân, tọa độ ngăn bằng dấu chấm phẩy $(0{,}2;\,0{,}3)$; kỳ vọng $\mathbb E_{S\sim\nu^\pi}$ (có chiết khấu) khác trung bình đều $\widehat{\mathbb E}_{\mathcal D}$ trên bộ đệm.
- Mục 7 (Q5, kế hoạch A5): $x$, $\mathcal X$ (lời nhắc); $y$, $\mathcal Y(x)$ (câu trả lời); $\pi_{\mathrm{ref}}$, $\theta_{\mathrm{ref}}$; $y_w$, $y_l$, $\mathcal D_{\mathrm{pref}}$ ($\mathcal D$ đã là bộ đệm), trung bình đều $\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}$; $\sigma(z)=1/(1+e^{-z})$; $r(x,y)$ (phần thưởng sinh dữ liệu, không viết $r^*$ vì dấu sao là "tối ưu"), $\hat r(x,y)$ (mô hình phần thưởng, theo khuôn $\hat v(s,w)$; $\phi$ đã là đặc trưng); $J_\beta$, $\pi^*_r$, $\mathcal Z_r(x)$ (hàm phân hoạch; $Z_{t+1}$ đã là cờ kết thúc); $r_\theta=\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$, $\Delta r_\theta$, $\tilde r_\theta=r-r_\theta$ (phần thưởng đã trừ KL); $L^{\mathrm{BT}}$, $L^{\mathrm{DPO}}$ (cực tiểu hóa, cùng họ $L^V$); $\mathcal V$ (tập token); $[r]$ (lớp tương đương). $\beta$ dùng chung: hệ số phạt KL theo $\pi_{\mathrm{old}}$ ở Mục 6.2, theo $\pi_{\mathrm{ref}}$ ở Mục 7 (Nhận xét 10.58 nói rõ). $x_k$, $y_k$, $\langle x,y\rangle_F$ của Thuật toán 10.36 và $y_t=V^{\mathrm{targ}}_t$ ở Mục 6.3 vào danh sách nghĩa cục bộ sau bảng ký hiệu. Không dùng $q$ (phân phối của Định nghĩa 10.23) cho tỉ lệ ưu tiên, $u$ (vector cục bộ Mục 5.1) cho hiệu logit, $\tau$ của IPO, $\gamma$ trộn tiền huấn luyện của Ouyang và cộng sự. Bảng tương ứng với ký hiệu bài báo ghi một lần sau bảng ký hiệu của ghi chú (kế hoạch A5).

**Ví dụ xuyên suốt.**

- *Bài toán một bước* (thẻ `img/lec-09/one-step-card.svg`): $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\theta=(\log2;\,0)$, $r=(3;\,0)$, $\nabla J=(\tfrac23;\,-\tfrac23)$, $v_\pi(s)=2$, $A_\pi(s,\cdot)=(1;\,-2)$. Dùng ở mạch 1, 2, 5, 6.
- *Chuỗi hai trạng thái* (`img/lec-10/two-state-chain.svg`): $\gamma=0{,}9$, $p_A=\tfrac12$, $p_B=\tfrac23$, $v_\pi=(1{,}4;\,2)$, $\nabla J=(0{,}2;\,0{,}3)$, $\nu^\pi=(0{,}1;\,0{,}045)$. Dùng ở mạch 2, 3, 4.
- *Hành lang ngắn* (`img/lec-09/short-corridor.svg`): $\gamma=1$, $p=\tfrac12$, $J=-12$, $\nabla J=(2;\,-2)$; chỉ ở mạch 1–2.
- *Bài toán một bước đọc thành lời nhắc và hai câu trả lời* (Mục 7, kế hoạch A7): trạng thái là lời nhắc $x$, hai hành động là $y_1$, $y_2$; $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ là chính sách softmax của Ví dụ 10.1 với $\theta_{\mathrm{ref}}=(\log2;\,0)$; $\beta=1$; sáu phép so sánh, bốn chọn $y_1$, hai chọn $y_2$. Số chính: $\hat r=(\log2;\,0)$, $L^{\mathrm{BT}}$ từ $0{,}6931$ xuống $0{,}6365$; $\mathcal Z=\tfrac53$, $\pi^*=(\tfrac45;\,\tfrac15)$, $\max J_1=\log\tfrac53=0{,}5108$; vòng PPO-Clip ($\epsilon=0{,}2$) dừng ở $0{,}8$; bước DPO đầu cho gradient $(-\tfrac16;\,\tfrac16)$, $\pi_\theta(y_1)=0{,}7362$, cực tiểu $(\tfrac45;\,\tfrac15)$. $(0{,}8;\,0{,}2)$ trùng $\pi'(\cdot\mid s_B)$ của Ví dụ 10.11, nên $D_{\mathrm{KL}}=0{,}04369$ đã có ở §4.3. Dùng ở mạch 7.

**Giả thiết chung.** (G1) $\mu_0$, $P$ không phụ thuộc $\theta$, trạng thái Markov; (G2) $\pi_\theta$ khả vi, miền hỗ trợ không đổi; (G3) $\lvert R\rvert\le R_{\max}$, $T\le T_{\max}$; (G4) softmax hoặc Gaussian phương sai cố định, đặc trưng bị chặn. Mạch 4–5 thêm: MDP hữu hạn, cùng $P$ và $\mu_0$, $\gamma<1$, chính sách Markov dừng, điều kiện hỗ trợ $\pi'>0\Rightarrow\pi>0$, lợi thế và phân bố chiếm dụng chính xác. Mọi kết quả dùng dữ liệu theo chính sách.

**Chuỗi định nghĩa → kết quả → phương pháp.** Hai giới hạn của REINFORCE (Ví dụ 10.1, 10.2) → đường cơ sở (Định nghĩa 10.1) → không làm chệch (Mệnh đề 10.2), đường cơ sở tối ưu (Mệnh đề 10.3) → hàm lợi thế (Định nghĩa 10.4) → gradient dạng lợi thế (Mệnh đề 10.5) → REINFORCE có đường cơ sở (Thuật toán 10.6) → critic, actor–critic (Định nghĩa 10.7) → $\mathbb E[\delta_t\mid s,a]=A_\pi$ khi critic đúng (Mệnh đề 10.8) → actor–critic một bước (Thuật toán 10.9) → lợi tức $n$ bước (Định nghĩa 10.11, Bổ đề 10.12) → lợi tức λ, GAE (Định nghĩa 10.13) → dạng tổng, truy hồi (Mệnh đề 10.14) → γ-just (Mệnh đề 10.15) → GAE trên đoạn thu (Thuật toán 10.16) → phân bố chiếm dụng (Định nghĩa 10.18) → chênh lệch hiệu năng (Bổ đề 10.19, Hệ quả 10.20) → hàm thay thế (Định nghĩa 10.21), khớp bậc một (Mệnh đề 10.22) → TV, KL, Pinsker (Định nghĩa 10.23, Mệnh đề 10.24) → chặn cải thiện (Định lý 10.26, Hệ quả 10.27; Bổ đề 10.25 trong chứng minh) → cải thiện đơn điệu (Hệ quả 10.29) → bài toán miền tin cậy (Định nghĩa 10.30, Hệ quả 10.31) → Fisher, KL bậc hai (Định nghĩa 10.32, Mệnh đề 10.33) → gradient tự nhiên (Mệnh đề 10.34) → gradient liên hợp, TRPO (Thuật toán 10.36, 10.37, Nhận xét 10.38) → PPO-Clip (Định nghĩa 10.39, Mệnh đề 10.40, 10.41, Nhận xét 10.42) → PPO-Penalty (Định nghĩa 10.43) → entropy, mất mát tổng, chẩn đoán (Định nghĩa 10.45–10.47, Mệnh đề 10.48) → PPO (Thuật toán 10.49) → chi tiết cài đặt (Nhận xét 10.50) → hội tụ về điểm dừng (Nhận xét 10.51, đọc thêm). Mục 7 (2026-11-19): bài toán sinh câu trả lời (Định nghĩa 10.52) → dữ liệu ưu tiên, Bradley–Terry (Định nghĩa 10.53) → hợp lý cực đại của mô hình phần thưởng (Mệnh đề 10.54) → mục tiêu có phạt KL (Định nghĩa 10.56) → nghiệm dạng đóng (Định lý 10.57, dùng Mệnh đề 10.24) → KL theo token (Bổ đề 10.59), gradient có phạt KL (Mệnh đề 10.60) → RLHF với PPO (Thuật toán 10.61, dùng Thuật toán 10.49) → đổi biến (Mệnh đề 10.63) → phần thưởng ngầm định, mất mát DPO (Định nghĩa 10.64) → tương đương (Định lý 10.65) → gradient DPO (Mệnh đề 10.66) → DPO (Thuật toán 10.67) → giới hạn của hai con đường (Nhận xét 10.69) → biến thể (Nhận xét 10.70, đọc thêm).

**Giới hạn áp dụng** (ghi chú §8.1–8.3, trước 2026-11-19 là §7.1–7.3; "Giả thiết hay bị bỏ quên").

- Đường cơ sở không được phụ thuộc hành động đã chọn khi biết $H_t$.
- Critic sai làm chệch actor–critic (Mệnh đề 10.8(b)).
- GAE γ-just chỉ khi $\lambda=1$ với lượt đầy đủ hoặc $\hat v=v_\pi$; γ-just không có nghĩa không chệch cho lợi thế.
- Mọi bảo đảm của mạch 4 cần lợi thế, $\nu^\pi$ và phép tối ưu chính xác, nên không áp dụng cho TRPO, PPO thực hành; TRPO thực hành chỉ bảo đảm KL trung bình mẫu $\le\kappa$ và hàm thay thế mẫu tăng.
- Mục tiêu cắt không chặn KL; approxKL không chệch chỉ khi $\theta$ không phụ thuộc các mẫu.
- Kết quả hội tụ của PPO-Clip chỉ nói về điểm dừng trong một mô hình đơn giản hóa.
- Mục 2–6: dữ liệu phải theo chính sách (giới hạn còn lại ở §8.6; câu "Bài 11 bỏ giới hạn này" bỏ theo Q8).
- Mục 7: nghiệm dạng đóng cần $\beta>0$ và chính sách chọn tự do theo $x$; miền hỗ trợ của nghiệm là miền hỗ trợ của $\pi_{\mathrm{ref}}$; DPO và RLHF trùng nghiệm chỉ dưới (H1)–(H4) của Định lý 10.65, với cực tiểu lấy trên mọi hàm phần thưởng và cùng dữ liệu, $\beta$, $\pi_{\mathrm{ref}}$; ưu tiên tất định làm (H4a) hỏng: cả hai hàm mất mát không có cực tiểu và cả hai con đường lý tưởng tiến tới chính sách tất định với mọi $\beta$; dữ liệu không nối mọi câu trả lời làm (H4b) hỏng: nghiệm không duy nhất, tập nghiệm của hai con đường vẫn trùng nhau; mô hình Bradley–Terry không phải giả thiết của Định lý 10.65; DPO dùng dữ liệu cố định, nên không đánh giá câu trả lời ngoài dữ liệu; RLHF với PPO dùng $\gamma=1$ trên MDP mức token, nằm ngoài giả thiết $\gamma<1$ của Mục 4.

**Trang bìa.** Tiêu đề `h1` "TRPO và PPO" (trùng tên ghi chú và `index.html`); dòng `h2` "Tối ưu chính sách miền tin cậy (TRPO) và tối ưu chính sách gần kề (PPO)" là dòng tiêu đề, không đếm âm tiết (quyết định của điều phối viên), để hai chữ viết tắt có tên đầy đủ ở lần đầu. Luận đề một câu, 30 âm tiết, không tên tiếng Anh: "Đường cơ sở giữ kỳ vọng của gradient; sai số hàm thay thế bị chặn theo khoảng cách chính sách, nên TRPO ràng buộc khoảng cách, PPO cắt tỉ số." Mặt bìa 49 âm tiết. (Bổ sung DPO: `h1` thành "TRPO, PPO và DPO" theo Q6; luận đề thêm vế về PPO và DPO cùng giải một bài toán khi có phạt KL theo chính sách tham chiếu cố định, bản nháp ở kế hoạch C3; việc của giai đoạn III.) Câu không dùng đề xuất "critic và GAE đổi phương sai lấy độ chệch" của kế hoạch, vì ghi chú chỉ nêu đánh đổi đó ở mức định tính và cấm khẳng định critic hay GAE luôn giảm phương sai; điều kiện "critic chỉ giữ kỳ vọng khi critic đúng" nằm trong ghi chú diễn giả của bìa và ở `L10-109`.

**Quy ước tên tiếng Anh.** Tên tiếng Anh và tên đầy đủ của chữ viết tắt ghi trong ngoặc ở lần đầu thuật ngữ xuất hiện trong một câu trên mặt trang, trừ bìa: luận đề không có tên tiếng Anh, và tên tiếng Anh của các thuật ngữ trong luận đề (đường cơ sở, hàm thay thế, tỉ số chính sách) ghi ở trang mục tiêu `L10-104`. Trang "Nội dung" và trang tiêu đề mạch giữ đúng tên mạch nên không chèn tên tiếng Anh; ký hiệu chưa được nêu ($\delta_t$, $\nu^\pi$, $\kappa$, $\rho_t$) không xuất hiện trước trang định nghĩa hoặc nhắc lại của nó.

### Mục tiêu học tập (trang `L10-104`)

Sáu dòng (sửa 2026-11-13 theo bảng phát hiện, trước đó năm dòng), mỗi dòng một sản phẩm kiểm được; ghi chú diễn giả nêu sản phẩm. Ánh xạ với bảy mục tiêu của ghi chú: dòng 1 ↔ mục tiêu 1–2; dòng 2 ↔ 3; dòng 3 ↔ 4 và nửa đầu của 5; dòng 4 ↔ nửa sau của 5; dòng 5 ↔ 6–7 (phần tính); dòng 6 ↔ 6–7 (phần chứng minh). Các sản phẩm của mục tiêu 2 (độ chệch của sai số TD khi critic sai), 6 (quy tắc PPO-Penalty) và 7 (một vòng PPO, phạm vi kết quả hội tụ của PPO-Clip) nêu trong ghi chú diễn giả, vì trang đã ở trần 80.

1. (Mạch 2) "Chứng minh đường cơ sở (baseline) không làm chệch; tính hai bước actor–critic." Sản phẩm: $\operatorname{Var}(X_b)=\tfrac49(b-1)^2$; $p_A$ từ $0{,}5$ lên $0{,}5436$; trong ghi chú diễn giả: $\mathbb E[\delta_0\mid s_A,1]=0{,}35\ne0{,}4$ khi critic sai.
2. (Mạch 3) "Tính ước lượng lợi thế tổng quát (GAE) trên đoạn thu (rollout) có cắt ngắn." Sản phẩm: $\widehat A_0=0{,}98$ và $3{,}572$.
3. (Mạch 4) "Chứng minh bổ đề chênh lệch hiệu năng (performance difference lemma); tính hàm thay thế (surrogate objective), chặn cải thiện." Sản phẩm: $\Delta J=0{,}296$, $\mathcal L-J=0{,}26$, cận chặn cải thiện $-0{,}892$. Tên tiếng Anh của chặn cải thiện ghi ở `L10-408`.
4. (Mạch 5) "Tính bước gradient tự nhiên (natural gradient), gradient liên hợp (conjugate gradient)." Sản phẩm: $\Delta^*=(0{,}15;\,-0{,}15)$; $\Delta=(0{,}05;\,0{,}1)$.
5. (Mạch 6) "Tính mục tiêu cắt (clipped objective), approxKL, tỉ lệ cắt (clip fraction)." Sản phẩm: $\mathcal L^{\mathrm{CLIP}}=0{,}2167$, approxKL $0{,}01737$, tỉ lệ cắt $\tfrac13$; quy tắc PPO-Penalty cho $\beta=2$ (ghi chú diễn giả).
6. (Mạch 6) "Chứng minh chặn dưới bi quan; approxKL không chệch." Sản phẩm: $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, trùng quanh $\theta_{\mathrm{old}}$ (Mệnh đề 10.41); $\mathbb E[(\rho-1)-\log\rho]=D_{\mathrm{KL}}$ khi $\theta$ không phụ thuộc mẫu (Mệnh đề 10.48).

Tổng 80 âm tiết theo `deck_check` (trần 80 của trang mục tiêu), 6 dòng, dòng dài nhất 19 âm tiết. Tên tiếng Anh "probability ratio" chuyển sang định nghĩa ở `L10-405`.

#### Mục tiêu học tập mới của ghi chú (bổ sung DPO, 2026-11-19)

Thêm hai mục sau mục tiêu 7 của ghi chú (GC16, VP21: bằng lời, không ký hiệu mới, không số hiệu khối; thuật ngữ theo bảng thuật ngữ dưới đây). Bản nháp đã qua `no-ai-slop` Edit; tác tử soạn chép vào ghi chú, chỉ chỉnh khi trái quy định:

8. **Phần thưởng từ dữ liệu ưu tiên và mục tiêu có phạt KL.** Ước lượng *mô hình phần thưởng* (reward model) từ *dữ liệu ưu tiên* (preference data) theo mô hình Bradley–Terry bằng hợp lý cực đại; chứng minh nghiệm dạng đóng của *mục tiêu có phạt KL* (KL-regularized objective) theo một *chính sách tham chiếu* (reference policy, reference model) cố định; mô tả ba giai đoạn của *học tăng cường từ phản hồi con người* (reinforcement learning from human feedback, RLHF) với PPO; phân biệt chính sách cũ của PPO với chính sách tham chiếu.
9. **Tối ưu ưu tiên trực tiếp.** Suy ra hàm mất mát của *tối ưu ưu tiên trực tiếp* (Direct Preference Optimization, DPO) bằng phép đổi biến giữa phần thưởng và chính sách; tính bằng tay một bước DPO; phát biểu các giả thiết để DPO và RLHF cho cùng chính sách tối ưu, và nêu hậu quả khi một giả thiết không thỏa.

Chỗ đổi so với kế hoạch A3: mục tiêu 8 dùng đúng thuật ngữ "mục tiêu có phạt KL" thay cho cụm "mục tiêu cực đại hóa phần thưởng có phạt KL"; bỏ tên tiếng Anh của mô hình Bradley–Terry (tên riêng); thêm "reference model" (VP2, mọi tên thông dụng). Mục tiêu 9 viết "cho cùng chính sách tối ưu": Định lý 10.65 nói về nghiệm, không nói về các bước lặp của PPO.

Ánh xạ: mục tiêu 8 ↔ §7.1–7.3 (Mệnh đề 10.54, Định lý 10.57, Thuật toán 10.61, Nhận xét 10.58); mục tiêu 9 ↔ §7.4–7.5 (Mệnh đề 10.63, Định lý 10.65, Thuật toán 10.67, Tình huống 10.5). Bài tập phủ mục tiêu ở mục "Bài tập: kế hoạch bổ sung DPO". Trên deck: trang mục tiêu tách thêm `L10-104b` vì chín mục tiêu vượt trần 80 âm tiết (Q7, QT4); storyboard chốt cách chia dòng.

#### Kiến thức tiên quyết thêm (bổ sung DPO)

Danh sách hiện có đã đủ cho Mục 7 về softmax, hàm điểm (Mệnh đề 09.16, 09.17), định lý gradient chính sách (Định lý 09.23), tính chất tháp (Bổ đề 09.21, 09.22); KL và Mệnh đề 10.24 nằm trong chương. Thêm một gạch đầu dòng kiến thức học máy và học sâu mà đối tượng đã học (GC-RL-16), phát biểu lại trong hai câu (kế hoạch A4):

- **Hồi quy logistic và mô hình ngôn ngữ tự hồi quy** (kiến thức học máy và học sâu). Với $\sigma(z)=1/(1+e^{-z})$, hồi quy logistic cực tiểu hóa trung bình của $-\log\sigma(z_i)$ trên các mẫu nhãn dương, với $\sigma'(z)=\sigma(z)\sigma(-z)$ và $1-\sigma(z)=\sigma(-z)$. Mô hình ngôn ngữ tự hồi quy gán cho chuỗi token $y=(a_0,\dots,a_{T-1})$ sau lời nhắc $x$ xác suất $\prod_t\pi(a_t\mid x,a_0,\dots,a_{t-1})$.

Câu quy ước đầu mục sửa dải số theo Q4: "Bài tập 10.13–10.17 và 10.22 thuộc tệp bài tập `exercises.md` của Bài 10." (Bài tập 10.18–10.21 thuộc ghi chú.)

### Tám mạch (bảy mạch tới 2026-11-19)

Bổ sung DPO (Q7, "P1, Bài 10, Mục 7 (riêng)"): HTML có 8 section ngoài, vượt khoảng 5–7 của NT10 theo yêu cầu cụ thể của tác giả (lý do ghi trong `storyboard.md` và `review-log.md` ở giai đoạn III). Mạch 7 mới mã `L10-D00` … `L10-D18`, `id="mach-7"`; "Tổng kết" giữ mã `L10-700` … `L10-710`, thành `id="mach-8"`. Số mạch $N$ trùng số mục $N$ của ghi chú với $N=2,\dots,8$. Đoạn dưới đây là quy ước của bản bảy mạch, giữ để đối chiếu.

HTML có đúng 7 section ngoài. Mạch $N$ mở tại `#/N`; từ mạch 2, trang đầu là trang tiêu đề mạch `L10-N00`, `id="mach-N"`. Số mạch $N$ trùng số mục $N$ của ghi chú với $N=2,\dots,7$; Mục 1 của ghi chú (một chủ đề, `lec-10-topic-02`) cùng phần tiên quyết vào mạch mở đầu, vì tách riêng sẽ thành 8 mạch, vượt khoảng 5–7.

| mạch | tên (trang tiêu đề mạch) | chức năng | đầu vào | đầu ra | đóng góp cho bài toán trung tâm | dòng dẫn (âm tiết) | từ khóa | phút |
|---|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu và hai giới hạn của REINFORCE (bìa là trang tiêu đề) | Ký hiệu, nhắc lại Bài 03–09, mục tiêu, nội dung; đo phương sai và tác hại của bước lớn; phát biểu bài toán | REINFORCE, (G1)–(G4), hàm điểm (Bài 09) | Hai nhu cầu: giảm phương sai giữ kỳ vọng; bước lớn bằng dữ liệu cũ | Phát biểu bài toán và khung hai hàng | — | — | 12 |
| 2 | Đường cơ sở, hàm lợi thế và actor–critic (`L10-200`) | Trừ đường cơ sở, đặt tên lợi thế, bootstrap bằng critic | $\operatorname{Var}$ tăng $\tfrac49\to\tfrac{16}9$ khi cộng $1$ vào phần thưởng | $\widehat g_b$ không chệch; $\nabla J$ dạng lợi thế; $\delta_t$ ước lượng lợi thế khi critic đúng; Thuật toán 10.6, 10.9 | Nửa thứ nhất, hai đầu Monte Carlo và một bước | "Muốn giảm phương sai mà giữ kỳ vọng của gradient, phải trừ khỏi lợi tức một mức không phụ thuộc hành động đã chọn." (24) | Đường cơ sở · Hàm lợi thế · Critic · Sai số sai phân thời gian · Actor–critic một bước (2026-11-13: tên đầy đủ thay "Sai số TD", vì viết tắt chỉ có tên đầy đủ từ `L10-212b`) | 23 |
| 3 | Ước lượng lợi thế tổng quát (`L10-300`) | Nối $\delta_t$ và $G_t-\hat v$ bằng $\lambda$; điều kiện γ-just; tính trên đoạn thu có cờ | Hai ước lượng $0{,}35$ và $1{,}7$ của cùng $A_\pi(s_A,1)=0{,}4$ | $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$, truy hồi lùi với $Z$, $U$, $V^{\mathrm{targ}}$ (Thuật toán 10.16) | Hoàn tất nửa thứ nhất; giao lợi thế cho mạch 6 | "Muốn chọn mức trung gian giữa sai số TD và lợi tức Monte Carlo, phải trộn các lợi tức nhiều bước bằng một tham số." (25, D1) | Lợi tức n bước · Lợi tức λ · GAE · Tính không chệch cho gradient · Đoạn thu | 14,5 |
| 4 | Hàm thay thế và chặn cải thiện (`L10-400`) | Chênh lệch hiệu năng, hàm thay thế, TV và KL, chặn cải thiện, miền tin cậy | Giới hạn thứ hai: dữ liệu cũ sau một bước | Bài toán miền tin cậy (Định nghĩa 10.30), mức giảm bị chặn khi giải chính xác (Hệ quả 10.31) | Căn cứ định lượng cho việc giới hạn bước | "Muốn dùng dữ liệu cũ cho một bước lớn, phải chặn sai số khi đánh giá chính sách mới bằng dữ liệu đó." (23) | Chênh lệch hiệu năng · Hàm thay thế · Phân kỳ KL · Chặn cải thiện · Miền tin cậy | 22,5 |
| 5 | TRPO và gradient tự nhiên (`L10-500`) | KL bậc hai, gradient tự nhiên, gradient liên hợp, tìm kiếm lùi | Bài toán miền tin cậy phi tuyến | Thuật toán 10.37; điều TRPO bảo đảm trên bộ đệm (Nhận xét 10.38) | Giải xấp xỉ bài toán của mạch 4 | "Muốn giải bài toán miền tin cậy với nhiều tham số, phải xấp xỉ KL bậc hai và tránh lập ma trận Fisher." (23) | Ma trận Fisher · Gradient tự nhiên · Gradient liên hợp · Tìm kiếm lùi | 13,5 |
| 6 | Tối ưu chính sách gần kề (PPO) (`L10-600`) | Mục tiêu cắt, PPO-Penalty, mất mát tổng, chẩn đoán, thuật toán, cài đặt, phạm vi lý thuyết | Chi phí bậc hai của TRPO; hàm thay thế mẫu tuyến tính theo $\rho_t$ | Thuật toán 10.49 với GAE và mục tiêu cắt; điều không được bảo đảm | Hai hàng gặp nhau | "Muốn giữ chính sách mới gần chính sách cũ bằng tối ưu bậc một, phải đưa giới hạn khoảng cách vào hàm mục tiêu." (24) | Mục tiêu cắt · PPO-Penalty · Hàm mất mát tổng · Đại lượng chẩn đoán · Chi tiết cài đặt | 25,5 |
| 7 (mới, 2026-11-19) | Tối ưu chính sách từ phản hồi ưu tiên (`L10-D00`) | Mô hình Bradley–Terry, mục tiêu có phạt KL và nghiệm dạng đóng, RLHF với PPO, DPO, so sánh hai con đường | Thuật toán 10.49; phạt KL của Định nghĩa 10.43; KL và Mệnh đề 10.24 | Định lý 10.57, 10.65; Thuật toán 10.61, 10.67; bảng so sánh | Phần thứ ba: cùng một phép phạt KL, mỏ neo cố định | bản nháp kế hoạch C1: "Cùng một mục tiêu có phạt KL được giải bằng PPO với mẫu trực tuyến hoặc bằng DPO trên dữ liệu cố định." (23; không khuôn "Muốn …, phải …", NT12) | Bradley–Terry · Phạt KL · RLHF với PPO · DPO · Hai mỏ neo | 22 |
| 8 (cũ 7) | Tổng kết (`L10-700`; tên cũ "Tổng kết và chuyển tiếp", đổi theo GC-RL-15, Q3) | Bảng kết quả–giả thiết, bảng phương pháp, bảng kết luận có bảo đảm, bài tổng hợp, trả lời bài toán, câu hỏi, bài về nhà; bỏ dòng nối Bài 11 (Q8) | Kết quả mạch 2–7 | Câu trả lời có điều kiện, sáu phần; giới hạn còn lại không trỏ bài sau | Tổng hợp, không khái niệm mới | dòng dẫn cũ "Muốn dùng đúng các phương pháp của bài, phải giữ giả thiết của từng kết quả." (16) viết lại ở giai đoạn III (NT12, QT5) | bỏ "Bài 11" (Q8); storyboard chốt | 9 |

Âm tiết đếm bằng số từ tách theo khoảng trắng, không tính KaTeX (công cụ đếm trong thư mục tạm của phiên). Tên mạch khác tiêu đề trang nội dung đầu mạch: `L10-201` "Mức so sánh của trạng thái", `L10-301` "Ví dụ: ba ước lượng lợi thế trên một lượt", `L10-401` "Dữ liệu cũ và chính sách mới", `L10-501` "Ví dụ: cùng một bước tham số, hai khoảng cách chính sách", `L10-601` "Giới hạn của TRPO", `L10-701` "Kết quả và giả thiết của bài".

Trang "Nội dung" (`L10-105`) liệt kê bảy tên theo cột "tên", mục 1 là "Mở đầu và hai giới hạn của REINFORCE". Sau bổ sung DPO: tám tên, liên kết `#/1` … `#/8`, mục 7 "Tối ưu chính sách từ phản hồi ưu tiên", mục 8 "Tổng kết". Phút của mạch 1–6 và 8 trong bảng trên là số của bản bảy mạch; số sau khi rút về 135 phút ở mục "Phân bổ thời lượng".

### Mục 7 của ghi chú: Tối ưu chính sách từ phản hồi ưu tiên (bổ sung 2026-11-19)

Tiêu đề `## 7. Tối ưu chính sách từ phản hồi ưu tiên` (Q3; cụm danh từ tiếng Việt, VP7, GC-RL-17). Mục đi theo mẫu GC-RL-1, mỗi khái niệm trọng tâm theo GC18 (bài toán → "Một cách trực quan" → định nghĩa → kết quả hoặc thuật toán, có ví dụ chạy tay trước → chứng minh → ví dụ → nhận xét); không bài tập cuối mục (BT-RL-6). Chi tiết từng khối, số liệu tính lại và chỗ dẫn đầy đủ ở kế hoạch A7, A8; mục này chốt cấu trúc, số hiệu và vai.

**Chỗ nối vào bài toán trung tâm.** Bài 10 xoay quanh việc giữ một chính sách mới gần một chính sách khác bằng khoảng cách KL: Mục 4–6 giữ $\pi_\theta$ gần $\pi_{\mathrm{old}}$ để hàm thay thế còn đáng tin trong một bước. Mục 7 dùng cùng công cụ với một mỏ neo khác: $\pi_{\mathrm{ref}}$ cố định trong cả quá trình học, và phạt KL quyết định nghiệm cuối. Đây là phần thứ ba của bài toán trung tâm (Q3, mục "Khung lý thuyết chung").

**Kết quả kế thừa và câu nối ở kết §6** (GC15, một phía, đặt sau đoạn "Cái giá của PPO …" của §6.6): Thuật toán 10.49 dùng phần thưởng $R_{t+1}$ do môi trường trả về; PPO-Penalty (Định nghĩa 10.43) phạt $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$ để giữ mỗi bước gần chính sách vừa sinh dữ liệu. Câu nối nêu điều còn thiếu (không có phần thưởng từ môi trường khi chỉ có so sánh), không dẫn số mục sau (VP20). Mục 7 mở thẳng bằng bài toán.

**Bài toán mở mục** (đoạn đầu §7.1, GC5, có số liệu; dữ kiện tự dựng viết "Giả sử …", VP18): một lời nhắc $x$, hai câu trả lời $y_1$, $y_2$ do $\pi_{\mathrm{ref}}(\cdot\mid x)=(\tfrac23;\,\tfrac13)$ sinh ra; không có hàm phần thưởng, chỉ có sáu lần người gán nhãn so sánh: bốn lần chọn $y_1$, hai lần chọn $y_2$.

**Câu hỏi của mục** (VP-RL-2, câu hỏi nghiên cứu được trả lời trong mục; đã qua `no-ai-slop` Edit; sửa từ bản nháp kế hoạch A2: "các phép so sánh này" thành "sáu phép so sánh này", "nếu nó phải gần" thành "nếu vẫn phải gần"):

> **Câu hỏi.** Từ sáu phép so sánh này, chính sách mới nên chọn mỗi câu trả lời với xác suất nào nếu vẫn phải gần chính sách tham chiếu, và có cần một vòng học tăng cường để tìm chính sách đó không?

**Câu trả lời của mục** (kết §7.5; phần 6 của §8.3): mô hình Bradley–Terry cho $\hat r=(\log2;\,0)$ (Mệnh đề 10.54); mục tiêu có phạt KL với $\beta=1$ có nghiệm $(\tfrac45;\,\tfrac15)$ (Định lý 10.57); PPO đi tới nghiệm đó bằng mẫu sinh trực tuyến (Ví dụ 10.27); DPO cực tiểu hóa một hàm mất mát phân loại trên sáu phép so sánh và cho cùng $(\tfrac45;\,\tfrac15)$ (Ví dụ 10.28, Định lý 10.65) khi các giả thiết của Định lý 10.65 thỏa; với ba so sánh cùng chọn $y_1$, giả thiết (H4a) hỏng: $L^{\mathrm{BT}}$ và $L^{\mathrm{DPO}}$ đều không có cực tiểu, và cả hai con đường lý tưởng đẩy xác suất của $y_2$ về $0$ với mọi $\beta$ (Tình huống 10.5); hai con đường chỉ khác nhau khi mô hình phần thưởng được điều chuẩn, theo lập luận của Gheshlaghi Azar và cộng sự (§4.2), không phải một định lý. (Sửa vòng 2: bản trước chỉ nói về DPO, gợi ý sai rằng RLHF tránh được.)

#### Bảng khối mới 10.52–10.70

Một bộ đếm chung tiếp sau Nhận xét 10.51 (GC19: số tăng theo thứ tự đọc; Bổ đề là công cụ, Mệnh đề là sự kiện hẹp, Định lý là kết quả chính). Mức chứng minh: "đầy đủ" là chứng minh trong khối `proof`, chia bước có nhãn, kết bằng $\square$; "không áp dụng" cho định nghĩa, thuật toán, nhận xét.

| Số | Loại | Tên (bản nháp) | Tiểu mục | Vai | Mức chứng minh |
|---|---|---|---|---|---|
| 10.52 | Định nghĩa | Bài toán sinh câu trả lời (dạng một bước; dạng mức token) | 7.1 | đặt bài toán; nối với bài toán một bước của Ví dụ 10.1 | — |
| 10.53 | Định nghĩa | Dữ liệu ưu tiên, mô hình Bradley–Terry | 7.1 | đối tượng trung tâm của 13.4.1; lớp tương đương $[r]$ | — |
| 10.54 | Mệnh đề | Hợp lý cực đại của mô hình phần thưởng | 7.1 | sự kiện hẹp: $L^{\mathrm{BT}}$, bất biến theo $f(x)$, cực tiểu $\log\frac k{n-k}$, không cực tiểu khi $k=n$ | đầy đủ (định nghĩa; chỉ hiệu xuất hiện; đạo hàm $\sigma(d)-k/n$ và tính lồi) |
| 10.55 | Nhận xét | Thu thập và chuẩn hóa dữ liệu ưu tiên | 7.1 | 13.4.2; nhầm lẫn: coi $\hat r$ là điểm tuyệt đối; số câu trả lời được xếp hạng viết $n_{\mathrm{xh}}$, không $K$ | — |
| 10.56 | Định nghĩa | Mục tiêu có phạt KL, chính sách tham chiếu | 7.2 | mục tiêu chung của hai con đường (luận điểm, mức 1) | — |
| 10.57 | Định lý | Nghiệm của mục tiêu có phạt KL | 7.2 | **kết quả chính thứ nhất**: nghiệm dạng đóng, điểm gặp; bốn phần GC-RL-7 | đầy đủ, ba bước, qua Mệnh đề 10.24(a) |
| 10.58 | Nhận xét | Hai mỏ neo, hai chiều KL | 7.2 | khái niệm với khái niệm (GC14): $\pi_{\mathrm{old}}$ của Định nghĩa 10.43 và $\pi_{\mathrm{ref}}$; chiều KL; luận điểm, mức 3 | — |
| 10.59 | Bổ đề | KL của câu trả lời bằng tổng KL theo token | 7.3 | công cụ cho Thuật toán 10.61, 10.67 | đầy đủ (quy tắc nhân, tính chất tháp) |
| 10.60 | Mệnh đề | Gradient của mục tiêu có phạt KL | 7.3 | nối Mục 6: gradient bằng gradient chính sách với phần thưởng đã trừ KL $\tilde r_{\theta_{\mathrm{old}}}$ | đầy đủ, ngắn (đạo hàm; số hạng thừa bằng $0$ theo Mệnh đề 09.17) |
| 10.61 | Thuật toán | RLHF với PPO | 7.3 | con đường thứ nhất (luận điểm, mức 2); khối GC-RL-7 đủ phần | — |
| 10.62 | Nhận xét | Tối ưu quá mức mô hình phần thưởng | 7.3 | 13.5.2; chỉ điều bài báo đo (VP6) | — |
| 10.63 | Mệnh đề | Đổi biến giữa phần thưởng và chính sách | 7.4 | bước then chốt của DPO: $\mathcal Z_r$ triệt tiêu; phần tử duy nhất của $[r]$ có dạng $r_\pi$ | đầy đủ |
| 10.64 | Định nghĩa | Phần thưởng ngầm định, hàm mất mát DPO | 7.4 | $r_\theta$, $\Delta r_\theta$, $L^{\mathrm{DPO}}=L^{\mathrm{BT}}(r_\theta)$ | — |
| 10.65 | Định lý | Tương đương giữa RLHF và DPO | 7.4 | **kết quả chính thứ hai** (luận điểm, mức 2–3); giả thiết (H1)–(H3), (H4a), (H4b); bốn phần GC-RL-7 | đầy đủ, bốn bước |
| 10.66 | Mệnh đề | Gradient của hàm mất mát DPO | 7.4 | trọng số $\sigma(-\Delta r_\theta)$; dùng ở Ví dụ 10.28 | đầy đủ, ngắn |
| 10.67 | Thuật toán | DPO | 7.4 | con đường thứ hai; khối GC-RL-7 đủ phần | — |
| 10.68 | Nhận xét | Đọc kết quả của DPO | 7.4 | dữ liệu sinh từ $\pi_{\mathrm{ref}}$; nhầm lẫn: DPO điều khiển hiệu, không bảo đảm xác suất của $y_w$ tăng | — |
| 10.69 | Nhận xét | Giới hạn của hai con đường | 7.5 | luận điểm, mức 3: điều kiện và khác biệt | — |
| 10.70 | Nhận xét | Biến thể và so sánh thực nghiệm | 7.6 | đọc thêm | — |

Ví dụ 10.23–10.28 và Tình huống 10.4–10.5 ghi theo tiểu mục dưới đây. Mỗi khối `example`, `application` chép lại đủ dữ kiện (GC23). Kế hoạch A8 dẫn Tình huống 10.5 và bài tập về dữ liệu không phủ (nay Bài tập 10.20) từ phần "Phạm vi" của Định lý 10.65 và từ kết §7.5; các khối đó đứng sau Mục 7 trong ghi chú, nên đây là tham chiếu tới phần sau (VP20, GC15). Cách viết: nêu phản ví dụ ngay tại chỗ bằng một câu có số (ba so sánh cùng chọn $y_1$; dữ liệu không chứa $y_3$), chỉ giữ số hiệu khi người đọc phải mở khối đó để lấy một con số. Ghi nguồn của Định lý 10.65 (Q3, QG8; sửa vòng 2 theo phân tích nguồn I.2, P-01, P-02): phát biểu là của học phần, ghép Định lý 1 và Mệnh đề 1 của Rafailov và cộng sự (2023) (Phụ lục A.6, giả thiết $\pi_{\mathrm{ref}}>0$, $\beta>0$), nửa đầu chứng minh Định lý 4.1 của Xu và cộng sự (2024), và Mệnh đề 4 của Gheshlaghi Azar và cộng sự (Phụ lục B, tr. 13; giả thiết tồn tại cực tiểu của mất mát Bradley–Terry, không cần mô hình Bradley–Terry đúng). (H4) là điều kiện nhận dạng mà chính DPO nêu là cần (tr. 6, "additional identifiability constraints"), không phải giả thiết tách từ "under mild assumptions": Phụ lục A.6 cho thấy "mild assumptions" chỉ là $\pi_{\mathrm{ref}}>0$ và $\beta>0$. Câu ghi `review-log.md` theo §2.3 của báo cáo phân tích nguồn. Tác tử rà toán kiểm; trong ghi chú chỉ một câu ở tài liệu tham khảo, không câu nguồn gốc tại chỗ (VP18).

Viết tắt nguồn dưới đây (kế hoạch A1): **DPO** Rafailov và cộng sự (2023); **IG** Ouyang và cộng sự (2022); **ST** Stiennon và cộng sự (2020); **ZI** Ziegler và cộng sự (2019); **CH** Christiano và cộng sự (2017); **IPO** Gheshlaghi Azar và cộng sự (2024); **XU** Xu và cộng sự (2024); **RQ** Rafailov, Hejna, Park, Finn (2024). "tr." là trang PDF của bản arXiv đã lưu.

#### 7.1 Dữ liệu ưu tiên và mô hình Bradley–Terry

- `note-topic-id`: `lec-10-topic-25` (cầu nối). Khoảng 900 từ. Mục lục 13.4.1, 13.4.2.
- **Nội dung, theo thứ tự.** Bài toán mở mục và "**Câu hỏi.**" (trên); Định nghĩa 10.52 (dạng (a) một bước: $s=x$, $a=y$, lượt dừng sau một hành động; dạng (b) mức token: $S_{t+1}=(S_t,A_t)$ tất định, phần thưởng chỉ ở bước cuối; cùng một chính sách, khác cách đếm bước); Ví dụ 10.23 (Dữ liệu ưu tiên trên bài toán một bước: sáu bộ ba, mỗi bộ một dòng, VP12; tỉ lệ $\tfrac23$; đặt trước định nghĩa, GC10); "Một cách trực quan": xác suất chọn tăng theo hiệu phần thưởng, chỉ hiệu có nghĩa; Định nghĩa 10.53; Mệnh đề 10.54 với chứng minh; Ví dụ 10.24 (Khớp mô hình phần thưởng: $d=\log2$, $L^{\mathrm{BT}}$ từ $0{,}6931$ xuống $0{,}6365$, $\hat r=(\log2;\,0)$, kiểm $\sigma(\log2)=\tfrac23$); Nhận xét 10.55; kết tiểu mục: có $\hat r$, chưa có chính sách.
- **Nguồn (Q1).** DPO §3, (1), (2), tr. 3; DPO Định nghĩa 1, Bổ đề 1, tr. 5, chứng minh Phụ lục A.5, tr. 17; CH §2.2.3, (1), tr. 5; IG §3.5, (1), tr. 8–9 (từ 4 đến 9 câu trả lời được xếp hạng, mọi cặp trong chúng thành một so sánh, cùng một phần tử lô; chuẩn hóa trung bình $0$); ST §3.4, tr. 6; ZI §2, tr. 3: (1) của ZI là mất mát chọn một trong bốn câu trả lời, $e^{r(x,y_b)}/\sum_ie^{r(x,y_i)}$, trùng Bradley–Terry chỉ khi có hai câu trả lời, nên dẫn như "dạng chọn một trong bốn, mở rộng của Bradley–Terry" hoặc chỉ dẫn ZI cho phép chuẩn hóa (trung bình $0$, phương sai $1$, tr. 3) (sửa vòng 2, P-08). Mệnh đề 10.54(c) ($k=n$) thêm IPO §4.2, tr. 4. Đối chiếu dạng mức token: RQ §3.1, tr. 3; ST chú thích 8, tr. 6; IG §3.5, tr. 9.
- **Ký hiệu trong Nhận xét 10.55** (sửa vòng 2, P-12). IG viết $K$ cho số câu trả lời được xếp hạng, nhưng $K$ đã là số epoch của PPO. Mọi chữ Latin đơn trong chương đã có nghĩa (kiểm 2026-11-19 trên ghi chú và `exercises.md`), nên dùng ký hiệu cục bộ $n_{\mathrm{xh}}$ (số câu trả lời được xếp hạng của một lời nhắc, cho $\binom{n_{\mathrm{xh}}}2$ so sánh), ghi vào danh sách nghĩa cục bộ sau bảng ký hiệu; hoặc viết bằng lời "từ 4 đến 9 câu trả lời, cho mọi cặp trong chúng" và không dùng chữ nào. Tác tử soạn chọn cách viết bằng lời nếu chữ chỉ xuất hiện một lần.
- **Ví dụ 10.24** (P-21): nửa câu nêu rằng ví dụ chọn $\hat r(x,y_2)=0$ để đọc số, theo Mệnh đề 10.54(b), khác cách chuẩn hóa của các bài báo ở Nhận xét 10.55.
- **Định nghĩa 10.52(b)** (P-14): độ dài tối đa $T_{\max}$ tính là kết thúc ($Z=1$), phần thưởng $\hat r$ cho cả câu trả lời đã cắt; đây là quy ước của học phần (ST, RQ chỉ nói kết thúc ở ký hiệu kết thúc), ghi `review-log.md`.
- **Phân loại.** Cầu nối: chuyển hồi quy logistic của học máy (GC-RL-16) sang phần thưởng; khoảng trống cụ thể là Thuật toán 10.49 cần $R_{t+1}$ mà bài toán chỉ có so sánh (GC-RL-12).

#### 7.2 Mục tiêu có phạt KL theo chính sách tham chiếu

- `note-topic-id`: `lec-10-topic-26` (cốt lõi). Khoảng 900 từ. Mục lục 13.5.2.
- **Nội dung, theo thứ tự.** Bài toán: với $\hat r=(\log2;\,0)$, chính sách cực đại hóa $\mathbb E\hat r$ là $(1;\,0)$, trong khi $\hat r$ chỉ được khớp trên câu trả lời của $\pi_{\mathrm{ref}}$; "Một cách trực quan": trả một chi phí cho mỗi đơn vị KL rời khỏi $\pi_{\mathrm{ref}}$; Ví dụ 10.25 (Ba chính sách trên bài toán một bước: $\pi_{\mathrm{ref}}$, tham lam $(1;\,0)$, $(0{,}8;\,0{,}2)$ với $J_1=0{,}4621$; $0{,}2877$; $0{,}5108$; trước định nghĩa); Định nghĩa 10.56; Định lý 10.57 (Giả thiết, Kết luận (a)–(d), Điều kiện áp dụng, Phạm vi; chứng minh ba bước; đoạn GC9 bỏ $\beta>0$ và bỏ "chọn tự do theo $x$"; "**Trong thực hành.**": $\mathcal Z_r(x)$ là tổng trên mọi chuỗi token, không tính được, nên định lý cho dạng nghiệm chứ không cho thuật toán); Ví dụ 10.26 (Nghiệm dạng đóng và vai trò của $\beta$: $\mathcal Z=\tfrac53$, $\pi^*=(\tfrac45;\,\tfrac15)$; $\beta=\tfrac12$ cho $(\tfrac89;\,\tfrac19)$, $\beta=2$ cho $(0{,}7388;\,0{,}2612)$; phần thưởng đã trừ KL bằng $0{,}5108$ ở cả hai câu trả lời); Nhận xét 10.58 (mở bằng câu hỏi nghiên cứu "Hệ số $\beta$ ở đây và $\beta$ của PPO-Penalty có cùng vai trò không?", trả lời ngay). Bổ đề 2 của DPO ($\pi^*_{r+f}=\pi^*_r$ khi $f$ chỉ phụ thuộc $x$) được chứng minh Mệnh đề 10.63(c) và Định lý 10.65 dùng: thêm phần (e) vào Định lý 10.57 hoặc một câu trong chứng minh, kèm chỗ dẫn (P-15).
- **Nguồn (Q1).** DPO (3), tr. 3; DPO (4), tr. 4, chứng minh Phụ lục A.1, (11)–(15), tr. 15–16; DPO Bổ đề 2, tr. 5; IG (2), tr. 9; ZI (2), tr. 3; ST §3.4, tr. 6 (vai của số hạng KL); ZI §2.2, tr. 3 (bộ điều khiển $\beta$ theo KL tới mô hình ban đầu, dùng trong Nhận xét 10.58). Mệnh đề 10.24(a) của ghi chú.
- **Lưu ý thứ tự.** Mục lục đặt 13.5.2 sau 13.5.1; ghi chú đặt mục tiêu có phạt KL trước RLHF vì đó là điểm chung của 13.5.2 và 13.6.1 (kế hoạch A1).

#### 7.3 RLHF với PPO

- `note-topic-id`: `lec-10-topic-27` (cốt lõi). Khoảng 900 từ. Mục lục 13.5.1, 13.5.2.
- **Nội dung, theo thứ tự.** Bài toán: tập câu trả lời quá lớn để tính $\mathcal Z_r(x)$, cần cực đại hóa $J_\beta$ bằng mẫu; Bổ đề 10.59 với chứng minh, rồi ví dụ hai token không đánh số (KL của chuỗi $0{,}240974=0{,}020136+0{,}6\cdot0{,}368064$; kế hoạch A7(10)); Mệnh đề 10.60 với chứng minh và hệ quả cho Mục 6 (gradient của hàm thay thế mẫu với lợi thế của $\tilde r_{\theta_{\mathrm{old}}}$ bằng $\nabla J_\beta$ tại $\theta_{\mathrm{old}}$, với lợi thế đúng); Ví dụ 10.27 (Hai vòng PPO trên phần thưởng đã trừ KL: vòng 1 lợi thế $\tfrac13\log2\,(1;\,1;\,-2)$, dừng ở $p=0{,}8=\tfrac23\cdot1{,}2$; vòng 2 lợi thế $0$; "**Diễn giải.**" về hai mỏ neo; chạy tay trước thuật toán, GC-RL-11); Thuật toán 10.61 (ba giai đoạn SFT, mô hình phần thưởng, PPO trên MDP mức token với $R_{t+1}=-\beta\log\frac{\pi_{\mathrm{old}}(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}+\mathbb 1\{t+1=T\}\hat r(x,y)$, $\gamma=1$; bốn mô hình trong bộ nhớ; điều kiện dừng là ngân sách; chi phí mỗi vòng; ghi rõ đây là khung chung, mỗi bài báo khác chi tiết); "**Trong thực hành.**" (GC-RL-9: $\pi_{\mathrm{ref}}$ là bản sao đóng băng của $\pi^{\mathrm{SFT}}$; $\gamma=1$ với độ dài bị chặn thỏa (G3), còn Mục 4 giả thiết $\gamma<1$; phần thưởng thưa cộng KL ở mọi bước; mỗi vòng sinh mẫu mới; một câu bằng lời, không đưa chữ $\gamma$ của bài báo: biến thể "PPO" của Ouyang và cộng sự cực đại hóa đúng $J_\beta$, còn các mô hình InstructGPT chính (PPO-ptx) cộng thêm một số hạng hợp lý trên dữ liệu tiền huấn luyện, nên không cực đại hóa đúng $J_\beta$ và Định lý 10.57 không áp dụng nguyên dạng cho chúng, sửa vòng 2, P-06); Nhận xét 10.62 (chỉ điều ST đo: với một phiên bản trước của mô hình phần thưởng (rm3), khi tối ưu mạnh hơn, ưu tiên thật của người gán nhãn giảm so với dự đoán; ST nêu hai vai của số hạng KL, ZI nêu thêm một vai riêng cho bài toán phong cách; các giá trị $\beta$ của từng bài ghi kèm tên bài, không so sánh với nhau vì thang phần thưởng khác nhau; P-19, P-23). Trong Thuật toán 10.61, $N$ đọc là số lời nhắc mỗi vòng, đúng vai số môi trường song song (P-20); $\pi_{\mathrm{ref}}\leftarrow\pi^{\mathrm{SFT}}$ là khung chung, không gắn chi tiết SFT trộn dữ liệu tiền huấn luyện của IG (P-16); dạng $R_{t+1}$ theo token là cách viết của học phần, đúng theo Bổ đề 10.59 và Mệnh đề 10.60, ghi `review-log.md` (P-13).
- **Nguồn (Q1).** IG §3.1 và Hình 2, tr. 3, 6; IG §3.5, tr. 8–9 (phạt KL theo từng token; hàm giá trị khởi tạo từ mô hình phần thưởng); IG Phụ lục C.4, tr. 42 ($\beta=0{,}02$, bán kính cắt $0{,}2$, một epoch trong, không chiết khấu khi tính GAE); ST §3.4 và chú thích 8, tr. 6; ST §4.3 và Hình 5, tr. 7–8 (tối ưu quá mức); ZI §2, quy trình bốn bước, tr. 3; ZI §2.2, tr. 3. IG (2), tr. 9 và C.4, tr. 42 (PPO-ptx). Đối chiếu: DPO §3, tr. 4 (dạng $r_\phi-\beta(\log\pi_\theta-\log\pi_{\mathrm{ref}})$ tối ưu bằng PPO); DPO chú thích 3, tr. 8 (KL chuỗi bằng tổng KL từng bước, cho Bổ đề 10.59); DPO §5.2, (10), tr. 6 (bài báo viết "Eq. 7", đúng là (4): nếu dẫn, dẫn (4), P-17); RQ §3.2, (2), tr. 3–4.

#### 7.4 Tối ưu ưu tiên trực tiếp

- `note-topic-id`: `lec-10-topic-28` (cốt lõi). Khoảng 1 200 từ. Mục lục 13.6.1.
- **Nội dung, theo thứ tự.** Bài toán: Thuật toán 10.61 giữ bốn mô hình và sinh mẫu ở mọi vòng, trong khi $\hat r$ chỉ dùng để đi tới $\pi^*_{\hat r}$; ví dụ đảo: từ $\pi^*=(\tfrac45;\,\tfrac15)$ và $\mathcal Z=\tfrac53$ đọc lại $\hat r=(\log2;\,0)$, hiệu $\log1{,}2-\log0{,}6=\log2$ không chứa $\mathcal Z$; "Một cách trực quan": mỗi chính sách xác định một phần thưởng mà nó là nghiệm; Mệnh đề 10.63 với chứng minh; Định nghĩa 10.64 (với hai câu trả lời, $\Delta r_\theta=\beta(\theta_1-\theta_2-\log2)$); Định lý 10.65 (bốn phần, chứng minh bốn bước; giả thiết và phản ví dụ theo đoạn "Định lý 10.65 sau vòng 2" dưới đây; một câu kết của luận điểm); Mệnh đề 10.66 với chứng minh (câu về bản bỏ trọng số chỉ viết "Rafailov và cộng sự viết rằng …", tr. 5, không dẫn Bảng 3: Bảng 3, tr. 22, là mẫu của phương pháp Unlikelihood, P-07); Ví dụ 10.28 (Một bước DPO tính tay: trọng số $\sigma(0)=\tfrac12$, gradient $(-\tfrac16;\,\tfrac16)$, $\pi_\theta(y_1)=0{,}7362$, $\Delta r_\theta=\tfrac13$, $L^{\mathrm{DPO}}$ từ $0{,}6931$ xuống $0{,}6514$; dãy bước 2–5; cực tiểu $(\tfrac45;\,\tfrac15)$ với $\min L^{\mathrm{DPO}}=0{,}6365=\min L^{\mathrm{BT}}$, trùng Ví dụ 10.26 và 10.27; hai bản cho cùng kết quả, GC-RL-11); Thuật toán 10.67 (đầu vào, đầu ra, giả thiết (H1)–(H2), khởi tạo $\theta\leftarrow\theta_{\mathrm{ref}}$, tham số, các bước, điều kiện dừng là số epoch, chi phí mỗi bộ ba; hai mô hình, không sinh mẫu, không critic); "**Trong thực hành.**" (GC-RL-9: $\pi_{\mathrm{ref}}$ là mô hình SFT; log-xác suất của chuỗi là tổng log-xác suất token theo Bổ đề 10.59; hai mô hình trong bộ nhớ; dữ liệu ưu tiên cố định; giá trị của DPO Phụ lục B); Nhận xét 10.68 (đẳng thức $\mathbb E_{\pi_{\mathrm{ref}}}r_\theta=-\beta D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)\le0$, số $-0{,}011855$ sau bước 1).
- **Nguồn (Q1).** DPO §4, (5), (6), (7), tr. 4; gradient, trọng số và "DPO outline", tr. 5; DPO §5.1, Định lý 1, tr. 6; Phụ lục A.2 (tr. 16), A.4 (21)–(22) (tr. 17), A.5 (tr. 17–18), A.6 phát biểu lại Định lý 1 với $\pi_{\mathrm{ref}}(y\mid x)>0$, $\beta>0$ và Mệnh đề 1 (tr. 18–19); Phụ lục B, tr. 20 ($\beta=0{,}1$, cỡ lô 64, RMSprop, tốc độ học $10^{-6}$); XU Định lý 4.1, nửa đầu chứng minh, Bảng 1, tr. 3–4; IPO Mệnh đề 1, tr. 4; IPO Mệnh đề 4, Phụ lục B, tr. 13 (cả hai chiều của tương đương, giả thiết tồn tại cực tiểu, không cần mô hình Bradley–Terry đúng); IPO Định lý 2, tr. 5 và Phụ lục A.2, tr. 13 (dữ liệu không phủ cho vô số nghiệm; nguồn cho (H4b) và Bài tập 10.20); DPO tr. 6 ("additional identifiability constraints"); RQ §5.4, (16), tr. 9 (Nhận xét 10.68).
- **Định lý 10.65 sau vòng 2** (phân tích nguồn I.2, P-01–P-04, P-09; điều phối viên đã kiểm). Giả thiết:
  - (H1) $\mathcal Y(x)$ hữu hạn và $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $x$, $y$;
  - (H2) $\beta>0$;
  - (H3) lớp chính sách gồm mọi phân phối có miền hỗ trợ đầy đủ trên $\mathcal Y(x)$, chọn tự do theo $x$;
  - (H4a) $L^{\mathrm{BT}}$, xét trên mọi hàm phần thưởng $\hat r$ trên các cặp $(x,y)$ (không giới hạn trong một lớp tham số), đạt cực tiểu;
  - (H4b) tập cực tiểu của $L^{\mathrm{BT}}$ là đúng một lớp $[\hat r]$;
  - và trong phát biểu: mọi lời nhắc $x$ trong miền hỗ trợ của $\mu_0$ có mặt trong $\mathcal D_{\mathrm{pref}}$; hai con đường dùng cùng $\mathcal D_{\mathrm{pref}}$, cùng $\beta$, cùng $\pi_{\mathrm{ref}}$.

  Mô hình Bradley–Terry không phải giả thiết: $L^{\mathrm{DPO}}(\pi)=L^{\mathrm{BT}}(r_\pi)$ là đẳng thức đại số (IPO Mệnh đề 4: "regardless of whether or not p∗ corresponds to a Bradley-Terry preference model"); Bradley–Terry chỉ cần để đọc $\hat r$ là ước lượng hợp lý cực đại (Mệnh đề 10.54). Kết luận: dưới (H1)–(H3) và (H4a), (a) $\pi^*_{\hat r}$ cực tiểu $L^{\mathrm{DPO}}$ với mọi cực tiểu $\hat r$ của $L^{\mathrm{BT}}$, và (c) $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$ (nửa đầu chứng minh Định lý 4.1 của XU; IPO Mệnh đề 4, chiều thuận); mọi cực tiểu của $L^{\mathrm{DPO}}$ có dạng $\pi^*_r$ với $r$ cực tiểu $L^{\mathrm{BT}}$ (IPO Mệnh đề 4, chiều ngược); thêm (H4b), (b) cực tiểu của $L^{\mathrm{DPO}}$ là duy nhất và bằng $\pi^*_{\hat r}$. Điều kiện đủ để kiểm (H4): với hai câu trả lời, $0<k<n$ (Mệnh đề 10.54(c)); với nhiều câu trả lời, mỗi cặp có cả hai kết quả và các cặp nối mọi câu trả lời (Tình huống 10.4). Không phát biểu điều kiện liên thông mạnh tổng quát (không có trong nguồn đã lưu). "Điều kiện áp dụng": cực tiểu hóa chính xác cả hai hàm mất mát và giải chính xác $J_\beta$. "Phạm vi": không nói về các bước lặp của PPO hay hạ gradient; khi (H4a) hỏng (ưu tiên tất định), cả hai hàm mất mát không có cực tiểu và cả hai con đường lý tưởng tiến tới chính sách tất định với mọi $\beta$; khi (H4b) hỏng (dữ liệu không phủ), nghiệm không duy nhất nhưng tập nghiệm của hai con đường trùng nhau.

  Phản ví dụ sau định lý (GC9, nêu tại chỗ bằng số, VP20):
  - bỏ (H1): ví dụ của học phần (P-03), $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac12;\,0)$, bốn so sánh chọn $y_1$, hai chọn $y_2$; mọi $(a;\,a\,2^{-1/\beta};\,1-a-a\,2^{-1/\beta})$ với $a>0$, $a(1+2^{-1/\beta})\le1$ cực tiểu $L^{\mathrm{DPO}}$, còn $\pi^*_{\hat r}(y_3)=0$ theo Định lý 10.57(d). Câu trả lời có $\pi_{\mathrm{ref}}=0$ không thể nằm trong $L^{\mathrm{DPO}}$ (phần thưởng ngầm định không xác định), nên ví dụ cũng có $y_3$ ngoài dữ liệu; nói rõ điều này. Tác tử rà toán kiểm. Không dùng Bảng 1 của XU làm phản ví dụ riêng cho (H1): bảng đó đồng thời hỏng (H3) (cực tiểu ở biên) và (H4) (một so sánh tất định); nếu dẫn, dẫn như ví dụ của Nhận xét 10.69(b);
  - bỏ (H4a): ba so sánh cùng chọn $y_1$ (dữ liệu của Tình huống 10.5), cả hai con đường không có nghiệm hữu hạn;
  - bỏ (H4b): dữ liệu không chứa $y_3$ (dữ liệu của Bài tập 10.20), vô số nghiệm;
  - bỏ (H3): lớp tham số không chứa $\pi^*_{\hat r}$.
- **Hình.** `img/lec-10/rlhf-dpo-hai-con-duong.svg` (mới) đặt ở đầu §7.4 hoặc §7.5 (tác tử soạn chọn một chỗ), có đoạn đọc hình.

#### 7.5 So sánh hai con đường và giới hạn

- `note-topic-id`: `lec-10-topic-29` (cốt lõi; luận điểm của tác giả). Khoảng 400 từ. Mục lục 13.6.1.
- **Nội dung, theo thứ tự.** Bảng so sánh `Tiêu chí | RLHF với PPO (Thuật toán 10.61) | DPO (Thuật toán 10.67)`, bảy hàng: mục tiêu ($\max J_\beta$, $\pi_{\mathrm{ref}}$ cố định, cả hai); đại lượng được tối ưu ($L^{\mathrm{BT}}$ rồi $\mathcal L^{\mathrm{CLIP}}$ với $\tilde r$ | $L^{\mathrm{DPO}}$); dữ liệu ($\mathcal D_{\mathrm{pref}}$ cộng mẫu trực tuyến từ $\pi_{\mathrm{old}}$ | chỉ $\mathcal D_{\mathrm{pref}}$, ngoại tuyến); mô hình trong bộ nhớ (bốn | hai); mỏ neo và chiều KL ($\pi_{\mathrm{ref}}$ trong mục tiêu, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$, thêm $\pi_{\mathrm{old}}$ của phép cắt | chỉ $\pi_{\mathrm{ref}}$, qua tỉ số trong $r_\theta$); điều kiện dừng (ngân sách vòng lặp | ngân sách epoch); bảo đảm (gradient đúng tại $\theta_{\mathrm{old}}$, Mệnh đề 10.60, không bảo đảm hội tụ | cực tiểu toàn cục trùng nghiệm RLHF dưới (H1)–(H4), Định lý 10.65). Nhận xét 10.69 ((a) cả hai dùng hàm mất mát Bradley–Terry (mô hình Bradley–Terry chỉ cần để đọc $\hat r$ là ước lượng hợp lý cực đại) và phụ thuộc miền hỗ trợ của $\pi_{\mathrm{ref}}$; (b) DPO không đánh giá câu trả lời ngoài dữ liệu, PPO đánh giá bằng $\hat r$ có thể sai ở đó (XU Định lý 4.1, Bảng 1 làm ví dụ ở đây); (c) ưu tiên tất định làm (H4a) hỏng: cả hai con đường lý tưởng không có nghiệm hữu hạn và cùng tiến tới chính sách tất định với mọi $\beta$; Gheshlaghi Azar và cộng sự (§4.2) lập luận rằng RLHF trong thực hành tránh được nhờ mô hình phần thưởng được điều chuẩn hoặc khớp chưa hết (CH §2.2.3: điều chuẩn $\ell_2$), lập luận chứ không phải định lý, phát biểu kèm tên bài; dữ liệu không phủ làm (H4b) hỏng, nghiệm không duy nhất; (d) không con đường nào thăm dò ngoài miền hỗ trợ của $\pi_{\mathrm{ref}}$). Trong bảng và nhận xét, "(H1)–(H4)" nghĩa là (H1)–(H3) cùng (H4a), (H4b). (Sửa vòng 2, P-04.) Kết mục (GC15, một phía): kết quả đã có, giới hạn còn lại; không dẫn số mục sau; trả lời "**Câu hỏi.**" của §7.1.
- **Nguồn (Q1).** DPO §1, tr. 2 và §6.1, tr. 8 (chỉ nửa câu "DPO and PPO optimize the same objective"; nửa sau về hiệu quả là kết quả thực nghiệm, không dẫn như sự thật, VP6); IPO §4.2, tr. 4; IPO §5.3 (tập $D_1$), tr. 8; IPO Định lý 2, tr. 5 và Phụ lục A.2, tr. 13; XU Định lý 4.1 và Bảng 1, tr. 3–4; RQ §5.4, (16), tr. 9; CH §2.2.3, tr. 5 (điều chuẩn $\ell_2$, dùng ở Nhận xét 10.69(c) và Tình huống 10.5).

#### 7.6 Đọc thêm: biến thể và so sánh thực nghiệm

- `note-topic-id`: `lec-10-topic-30` (đọc thêm). Khoảng 200 từ. Mục lục 13.6.
- **Nội dung.** Nhận xét 10.70, chỉ điều từng bài báo nêu, có tên bài (VP6): IPO, hàm mất mát bình phương (17) đưa hiệu log-tỉ số về $\tfrac1{2\tau}$, trên dữ liệu của Tình huống 10.5 cho $\pi(y_1)=\sigma(\log2+0{,}5)=0{,}7673$ thay cho $1$; cách đọc mức token của RQ; hai so sánh thực nghiệm (DPO §6.1, Hình 2: đường biên phần thưởng–KL trên bài toán sinh văn bản theo cảm xúc; XU: PPO với chuẩn hóa lợi thế, lô lớn và mô hình tham chiếu cập nhật bằng trung bình trượt vượt DPO trên các bài thử của họ; nửa câu: với cách cập nhật này mô hình tham chiếu không còn cố định, nên mục tiêu không còn là $J_\beta$ của Định nghĩa 10.56; không lặp lại việc XU gán kỹ thuật này cho Ouyang và cộng sự, vì IG C.4 chỉ nói trung bình trượt của trọng số, P-05), đo trên các bài toán khác nhau, không kết luận phương pháp nào tốt hơn. Không đưa $\mu$, $\rho$, $\Psi$ của IPO vào ghi chú; viết bằng lời (P-11).
- **Nguồn (Q1; sửa vòng 2, P-22).** IPO §5, tr. 5–7; (17), Thuật toán 1, §5.3.1 đều ở tr. 7; RQ §3.1, Định lý 1, (11), tr. 3, 6; DPO §6.1, Hình 2, tr. 7–8; XU tóm tắt, tr. 1 (kết luận chung) và ba yếu tố của PPO ở tr. 2 (phần giới thiệu) và §5, tr. 6, không ở tóm tắt.
- Trên deck chỉ ở ghi chú diễn giả của `L10-D15`, `L10-D16`.

#### Tình huống mới (mục "Tình huống áp dụng và ứng dụng", sau Tình huống 10.3)

- **Tình huống 10.4 (Chọn bản tóm tắt bằng dữ liệu ưu tiên)** (GC24): một bài đăng, ba bản tóm tắt do $\pi_{\mathrm{ref}}=(0{,}5;\,0{,}3;\,0{,}2)$ sinh ra, 45 phép so sánh (15 mỗi cặp: 10–5, 12–3, 10–5); mô hình hóa theo Định nghĩa 10.52(a), 10.53; kiểm (H1), (H4a), (H4b) bằng điều kiện đủ (mỗi cặp có cả hai kết quả, ba cặp nối ba câu trả lời); áp dụng Mệnh đề 10.54, Định lý 10.57, 10.65: $\hat r=(\log4;\,\log2;\,0)$, với $\beta=1$ nghiệm $(\tfrac57;\,\tfrac3{14};\,\tfrac1{14})$; giới hạn: một lời nhắc, ba câu trả lời; với mô hình ngôn ngữ phải đi qua Thuật toán 10.61 hoặc 10.67. Nguồn khung: ST (bài toán tóm tắt), số liệu tự dựng.
- **Tình huống 10.5 (Vi phạm giả thiết: ưu tiên tất định từ ít dữ liệu)** (GC-RL-8): phần thưởng thật $(\log2;\,0)$, ba so sánh cùng chọn $y_1$ (xác suất $\tfrac8{27}$); (H4a) hỏng vì $k=n$; DPO đẩy $\pi_\theta(y_1)\to1$ với mọi $\beta$, $J_1$ theo phần thưởng thật từ $0{,}5108$ xuống $0{,}2877$, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})\to\log\tfrac32=0{,}4055$ (bị chặn; đại lượng không bị chặn là $r_\theta(y_2)$). Con đường RLHF lý tưởng cũng vậy: $L^{\mathrm{BT}}$ không có cực tiểu, hiệu $\hat r(y_1)-\hat r(y_2)\to\infty$, và nghiệm có phạt KL tương ứng tiến tới $(1;\,0)$ với mọi $\beta$ (IPO §4.2, "for any τ"; IPO §5.3, $D_1$). Hai con đường chỉ khác nhau khi mô hình phần thưởng được điều chuẩn (CH §2.2.3), cho $\hat r$ hữu hạn và nghiệm có $\pi(y_2)>0$: lập luận của Gheshlaghi Azar và cộng sự (§4.2), không phải định lý, phát biểu kèm tên bài. Nêu nguyên nhân bằng giả thiết, không khuyến nghị ngoài nguồn. (Sửa vòng 2, P-04.)
- Chủ đề: hai tình huống không có mốc `note-topic-id` riêng (đứng trong mục Tình huống, như 10.1–10.3); khi ánh xạ deck, Tình huống 10.5 (`L10-D16`) mang `lec-10-topic-29`.

### Mục 8 của ghi chú: Tổng kết (đổi số từ §7, 2026-11-19)

`## 7. Tổng kết và chuyển tiếp` thành `## 8. Tổng kết` (GC-RL-15, Q3). Câu dẫn "Mỗi kết quả của Mục 2–6 đúng dưới một bộ giả thiết riêng." thành "Mục 2–7". Mốc `lec-10-topic-23` (trước 8.1) và `lec-10-topic-24` (trước 8.6) giữ nguyên. Không khái niệm mới.

| Cũ | Mới | Thay đổi |
|---|---|---|
| 7.1 Kết quả và giả thiết của bài | 8.1, giữ tên | thêm năm hàng: Mệnh đề 10.54, Định lý 10.57, Mệnh đề 10.60, Định lý 10.65, Mệnh đề 10.66 (nội dung từng ô ở kế hoạch A9); câu sau bảng "Sáu hàng đầu thuộc nửa giảm phương sai …, các hàng sau thuộc nửa giới hạn bước cập nhật" thêm "năm hàng cuối thuộc phần thứ ba (Mục 7)" |
| 7.2 So sánh bốn phương pháp | 8.2 So sánh sáu phương pháp | bảng phương pháp thêm hàng "RLHF với PPO (Thuật toán 10.61)" và "DPO (Thuật toán 10.67)"; câu "Cả bốn điều kiện dừng" thành "Cả sáu"; bảng bảo đảm thêm hàng "DPO (Định lý 10.65) — (H1)–(H3), (H4a), (H4b); cực tiểu trên mọi hàm phần thưởng; cùng dữ liệu, $\beta$, $\pi_{\mathrm{ref}}$ — mọi cực tiểu của $L^{\mathrm{DPO}}$ là $\pi^*_{\hat r}$"; hàng tương ứng của bảng 8.1 ghi cùng giả thiết |
| 7.3 Trả lời bài toán trung tâm | 8.3, giữ tên | "gồm năm phần" thành "gồm sáu phần"; thêm phần 6 (bản nháp ở kế hoạch A9): cùng mục tiêu có phạt KL theo $\pi_{\mathrm{ref}}$ cố định, nghiệm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57); PPO đi tới nghiệm bằng mẫu trực tuyến và bốn mô hình, DPO cực tiểu hóa hàm mất mát phân loại trên dữ liệu cố định; cùng chính sách dưới (H1)–(H4) (Định lý 10.65); với ưu tiên tất định cả hai con đường lý tưởng không có nghiệm hữu hạn và cùng tiến tới chính sách tất định với mọi $\beta$ (Tình huống 10.5). Sửa vòng 2 (P-04): bản nháp kế hoạch A9 "không khi ưu tiên tất định" sai, vì nói hai con đường khác nhau ở đó; cùng sửa ở Tóm tắt chương, `L10-D16`, `L10-708` |
| 7.4 Câu hỏi tự kiểm tra | 8.4, giữ tên | thêm câu 3 và lời giải ngắn: "Vì sao hệ số $\beta$ của PPO-Penalty không giữ chính sách gần $\pi_{\mathrm{ref}}$?" (lời giải: Định nghĩa 10.43 đo KL tới $\pi_{\mathrm{old}}$, đổi sau mỗi vòng; Nhận xét 10.58) |
| 7.5 Bài tập theo mục | 8.5, giữ tên | câu dẫn: "Bài tập củng cố 10.1–10.12 và 10.18–10.21 nằm ở cuối chương; bộ bài tập chính thức, Bài tập 10.13–10.17 và 10.22, nằm ở tệp bài tập Bài 10"; bảng thêm hàng `7. Tối ưu chính sách từ phản hồi ưu tiên | 10.18, 10.19, 10.20, 10.21 | 10.22`; hàng "7. Tổng kết và chuyển tiếp" thành `8. Tổng kết | 10.3 | —` |
| 7.6 Chuyển tiếp: Phần II và các biến thể mới | 8.6 Giới hạn còn lại (đã duyệt vòng 2; Q8) | xem dưới |

**§8.6 theo Q8.** Bỏ cả đoạn đầu (Phần II của bài giảng gốc, SPO, SAM+PPO, liên kết tới ghi chú Bài 11, ký hiệu $w_t$ của Bài 11) và câu "Bài 11 xử lý giới hạn này bằng bộ nhớ phát lại hoặc tỉ số với chính sách hành vi." Giữ đoạn giới hạn còn lại, không trỏ bài sau, và sửa cho đúng sau khi có Mục 7: câu "Giới hạn còn lại của chương là dữ liệu theo chính sách" chỉ đúng cho Mục 2–6 (Mệnh đề 10.2, 10.15 cần lượt do chính sách đang cập nhật sinh ra; Thuật toán 10.49 bỏ mỗi đoạn thu sau $K$ epoch). Thuật toán 10.67 dùng dữ liệu cố định, nên đoạn này thêm một câu cho Mục 7: DPO chỉ học trong miền hỗ trợ của $\pi_{\mathrm{ref}}$ và trên các câu trả lời có trong dữ liệu (Nhận xét 10.69(b), (d)). Câu nối tới Bài 11 mới chỉ thêm sau khi Bài 11 mới đã commit (Q8, GC15); điều phối viên báo phiên Bài 11. Tên "Chuyển tiếp: …" không còn đúng vì tiểu mục không chuyển tới bài nào; tên "Giới hạn còn lại" do outline đề xuất, điều phối viên đã duyệt (vòng 2).

**"Ứng dụng" sau Tình huống 10.3 (Q8).** Hai gạch đầu dòng đều trỏ nội dung Bài 11 cũ (A2C, A3C, ACER, IMPALA, ACKTR, SAC; SPO, SAM+PPO), trong khi Bài 11 đang dựng lại thành "Lập kế hoạch dựa trên mô hình": bỏ cả đoạn "**Ứng dụng.**". Gạch thứ nhất không thuộc đúng danh sách của Q8 (không SPO, SAM+PPO, không "Bài 11 xử lý …") nhưng trỏ tới nội dung không còn trong kho (GC15). Điều phối viên đã duyệt (vòng 2). Tên mục `## Tình huống áp dụng và ứng dụng` giữ nguyên dù không còn đoạn "Ứng dụng": GC-RL-1 cố định tên mục của mẫu chương, và các tình huống 10.1–10.5 là ứng dụng của chương.

#### Các chỗ sửa ngoài Mục 7 và Mục 8 (kế hoạch A9, tóm tắt)

| Vị trí | Sửa | Căn cứ |
|---|---|---|
| Tiêu đề | `# Bài 10 — TRPO, PPO và DPO` | Q6 |
| Mục tiêu học tập | thêm mục tiêu 8, 9 (mục "Mục tiêu học tập mới của ghi chú") | GC16, VP21 |
| Kiến thức tiên quyết | câu quy ước số bài tập theo Q4; thêm gạch hồi quy logistic và mô hình ngôn ngữ | GC16, BT-RL-10 |
| Bảng ký hiệu | dòng mới, nghĩa mở rộng của $\beta$, nghĩa cục bộ của $x_k$, $y_k$, $y_t$, bảng tương ứng với bài báo (kế hoạch A5) | GC-RL-6, GC7, Q5 |
| §1.1 | câu phần thứ ba của bài toán trung tâm; hàng thứ ba của `central-problem.svg` và một câu đọc hình | Q3, GC-RL-2 |
| Kết §6.6 | câu nối một phía (mục "Mục 7 của ghi chú") | GC15 |
| Tình huống | thêm 10.4, 10.5; bỏ đoạn "Ứng dụng" (Q8) | GC24, GC-RL-8, Q8 |
| Tóm tắt chương | đoạn kể thêm luận điểm và số $(\tfrac45;\,\tfrac15)$; gạch Mục 7 trong "Định nghĩa và kết quả theo mục"; "Công thức cần nhớ" thêm $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$ và $L^{\mathrm{DPO}}$; "Giả thiết hay bị bỏ quên" thêm hai dòng ((H4a), (H4b): với ưu tiên tất định cả hai con đường suy biến, với dữ liệu không phủ nghiệm không duy nhất; hai mỏ neo) | GC-RL-3 |
| Bài tập củng cố | câu dẫn phủ chín mục tiêu; bốn bài 10.18–10.21 cuối "Mức vận dụng" | BT-RL-5, BT-RL-10 |
| Tài liệu tham khảo | "Hướng dẫn đọc thêm" thêm một câu về Mục 7; thêm tám mục 18–25 (kế hoạch A9; nơi công bố chỉ ghi khi đã kiểm); sửa vòng 2: mục 23 (Gheshlaghi Azar và cộng sự) dẫn "Mệnh đề 1, 4, §4.2, §5 (tr. 5–7), (17), Định lý 2, Phụ lục A.2, B: Mục 7.4–7.6, Tình huống 10.5", năm theo bản đã kiểm (arXiv v2, 2023) cho tới khi kiểm nơi công bố, và A1 của kế hoạch viết "2024" phải thống nhất (P-18); mục 21 (Ziegler và cộng sự) dẫn "(1) dạng chọn một trong bốn, (2), §2.2"; mục 24 (Xu và cộng sự) dẫn "Định lý 4.1, Bảng 1, tr. 2, §5"; mục 18 (DPO) không dẫn Bảng 3; câu ghi nguồn của Định lý 10.65 theo đoạn "Ghi nguồn của Định lý 10.65" ở mục 7; mục 1 "Mục 7: tr. 2–3, 28, 43" thành "Mục 8"; mục 17 bỏ phần SPO, SAM+PPO và "trình bày ở Bài 11" | GC25, Q1, Q8 |

### Bảng thuật ngữ Việt–Anh

Kế thừa bảng của Bài 09 (`planning/lec-09/outline.md`). Lần đầu xuất hiện trên mặt trang, viết tên tiếng Việt kèm tên tiếng Anh trong ngoặc; các lần sau chỉ dùng tên tiếng Việt. Cột "lần đầu" là trang dự kiến.

| Tiếng Việt | Tiếng Anh | Quy ước | lần đầu |
|---|---|---|---|
| đường cơ sở | baseline | $b(s)$; không để "baseline" trần | `L10-104` |
| hàm lợi thế, lợi thế | advantage function, advantage | $A_\pi$; ước lượng $\widehat A_t$ | `L10-102` ("lợi thế (advantage)"); `L10-207` ("hàm lợi thế (advantage function)") |
| critic; actor; phương pháp actor–critic | critic; actor; actor–critic method | tên giữ nguyên; định nghĩa theo Định nghĩa 10.7 (critic bootstrap từ $S_{t+1}$) | `L10-104`; định nghĩa ở `L10-212` |
| quá trình quyết định Markov (MDP) | Markov decision process | viết tắt sau lần đầu | `L10-103` (dòng (G1), 2026-11-13); `L10-102` chỉ còn tên cờ |
| sai số sai phân thời gian (sai số TD) | temporal-difference error | $\delta_t$ có mặt nạ $(1-Z_{t+1})$; $\delta$ không dùng cho nghĩa khác | `L10-212b` ("Nhắc lại:", tên đầy đủ kèm viết tắt, 2026-11-13); `L10-200` (từ khóa, tên đầy đủ) |
| cập nhật bán gradient | semi-gradient | | `L10-212` (ghi chú diễn giả) |
| lợi tức; lợi tức $n$ bước; lợi tức λ | return; n-step return; λ-return | $G_t$, $G_{t:t+n}$, $G^\lambda_t$ | `L10-103`; `L10-302`; `L10-303` |
| lợi tức λ cắt | truncated λ-return | chỉ trong ghi chú diễn giả | `L10-307` |
| ước lượng lợi thế tổng quát (GAE) | generalized advantage estimation | $\widehat A_t$, tham số $\lambda$ | `L10-104` |
| γ-just (không chệch cho gradient) | γ-just | thuật ngữ của Schulman và cộng sự (2016) | `L10-306` |
| đoạn thu | rollout | độ dài $h$ (bài báo PPO và nguồn tr. 24 viết $T$) | `L10-104` |
| kết thúc; cắt ngắn | termination; truncation | cờ $Z$; cờ $U$ | `L10-102` |
| bộ đệm | buffer | $\mathcal D$, $hN$ mẫu | `L10-507` |
| phân bố chiếm dụng (chiết khấu) | discounted occupancy distribution | $\nu^\pi$, chuẩn hóa trên $\mathcal S$, khối $\le1$ | `L10-403` |
| bổ đề chênh lệch hiệu năng | performance difference lemma | | `L10-104` |
| hàm thay thế | surrogate objective | $\mathcal L_{\theta_{\mathrm{old}}}$; không để "surrogate" trần | `L10-104` |
| tỉ số chính sách | probability ratio | $\rho_t(\theta)$; viết "tỉ số", không "tỷ số"; Bài 11 viết $w_t$ | `L10-405` (định nghĩa, có tên tiếng Anh từ 2026-11-13) |
| tỉ số lấy mẫu quan trọng | importance sampling ratio | nhắc lại Định nghĩa 06.24 | `L10-405` |
| biến phân toàn phần (TV) | total variation distance | $D_{\mathrm{TV}}$ | `L10-407` |
| phân kỳ Kullback–Leibler (KL) | Kullback–Leibler divergence | $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$, $\widehat D$; chiều cũ‖mới; trước `L10-407` mặt trang chỉ nói "khoảng cách giữa hai chính sách" | `L10-407` |
| chặn cải thiện (còn gọi là cận cải thiện) | policy improvement bound | tên tiếng Anh ở trang định nghĩa | `L10-104`; tên tiếng Anh ở `L10-408` |
| cực đại hóa qua hàm chặn dưới | minorize–maximize (MM) | chỉ trong ghi chú diễn giả | `L10-411` |
| miền tin cậy; bài toán miền tin cậy | trust region; trust region problem | bán kính $\kappa$ (là $\delta$ của Schulman và cộng sự, 2015) | `L10-412` |
| tối ưu chính sách miền tin cậy (TRPO) | Trust Region Policy Optimization | tên đầy đủ ở phụ đề bìa; sau đó viết TRPO | `L10-101` |
| ma trận thông tin Fisher | Fisher information matrix | $F$ | `L10-502` |
| gradient tự nhiên | natural gradient | $F^{-1}g$ | `L10-104` |
| gradient liên hợp | conjugate gradient | $\tilde g_k$, $\omega_k$, $\xi_k$ giới thiệu tại thuật toán | `L10-104` |
| tích Fisher–vector | Fisher–vector product | $v\mapsto Fv$ | `L10-506` |
| tìm kiếm lùi | backtracking line search | hệ số $\zeta$ | `L10-507` |
| tối ưu chính sách gần kề (PPO) | Proximal Policy Optimization | tên đầy đủ ở phụ đề bìa; sau đó viết PPO | `L10-101` |
| mục tiêu cắt; bán kính cắt | clipped objective; clip range | $\mathcal L^{\mathrm{CLIP}}$, $\epsilon$ | `L10-104`; `L10-603` |
| lặp chính sách bảo thủ (CPI) | conservative policy iteration | chỉ số trên $\mathcal L^{\mathrm{CPI}}$ | `L10-603` (mặt trang từ 2026-11-13) |
| chặn dưới bi quan | pessimistic bound | | `L10-606` |
| mục tiêu phạt KL; hệ số phạt thích nghi | KL-penalized objective; adaptive KL penalty coefficient | $\beta$, $\kappa_{\mathrm{targ}}$ | `L10-607` |
| entropy | entropy | $\mathcal H$; giữ nguyên | `L10-609` |
| hàm mất mát tổng; mất mát giá trị | total loss; value loss | $L(\theta,w)$; $L^V$ | `L10-609` |
| approxKL (KL xấp xỉ) | approximate KL | tên đại lượng chẩn đoán, giữ nguyên | `L10-104` (tên); định nghĩa ở `L10-611` |
| tỉ lệ cắt | clip fraction | không trùng tập mẫu có gradient bằng $0$ | `L10-104`; định nghĩa ở `L10-611` |
| phương sai được giải thích | explained variance | | `L10-611` |
| dừng sớm | early stopping | theo approxKL | `L10-613` |
| cắt mất mát giá trị | value function clipping | biến thể của Định nghĩa 10.46; công thức và $\epsilon$ trên mặt trang (D1) | `L10-617` |
| tối ưu mức mã | code-level optimization(s) | Engstrom và cộng sự (2020) | `L10-617` (dòng "Nhu cầu:") |
| điểm dừng | stationary point | $\nabla V(\theta)=0$; tên tiếng Anh trong ghi chú diễn giả (mặt trang ở trần 60 âm tiết) | `L10-618` |
| hầu chắc chắn | almost surely | không dùng "gần như chắc chắn" | `L10-618` |
| hai thang thời gian | two-timescale | mô hình của Jin, Li và Wang (2024); chỉ trong ghi chú diễn giả (D1) | `L10-618` |
| môi trường vector hóa | vectorized environments | $N$ môi trường song song; tên tiếng Anh trong ghi chú diễn giả | `L10-617b` |
| giả nghịch đảo | pseudoinverse (Moore–Penrose) | $F^+$ | `L10-503` |
| mini-batch; epoch | mini-batch; epoch | giữ như Bài 08–09 | `L10-606`; `L10-613` |
| hạ gradient ngẫu nhiên (SGD); Adam | stochastic gradient descent; Adam | | `L10-103` (ghi chú diễn giả) |
| bài toán nhiều cần gạt | multi-armed bandit | chỉ trong ghi chú diễn giả | `L10-201` |

**Phần mới của Mục 7** (2026-11-19; GC-RL-13, VP2–VP4, kế hoạch A10, Q5). Đã kiểm theo kế hoạch A10: ghi chú, bài tập, deck Bài 01–10 không dùng các thuật ngữ này với nghĩa khác trong Bài 10. Cột "lần đầu" ghi chỗ trong ghi chú; trang deck theo kế hoạch C2, storyboard chốt (mục tiêu học tập ở `L10-104b` có thể là lần đầu trên deck của nhiều thuật ngữ).

| Tiếng Việt | Tiếng Anh | Quy ước | lần đầu |
|---|---|---|---|
| lời nhắc; câu trả lời | prompt; response, completion | $x$, $\mathcal X$; $y$, $\mathcal Y(x)$ (Q5) | §7.1; `L10-D01` |
| token; tập token | token; vocabulary | giữ "token" như "entropy", "critic" | §7.1 (Định nghĩa 10.52(b)); `L10-D08` |
| MDP mức token | token-level MDP | Định nghĩa 10.52(b) | §7.1 |
| dữ liệu ưu tiên; phép so sánh ưu tiên | preference data; pairwise comparison | $\mathcal D_{\mathrm{pref}}$, bộ ba $(x,y_w,y_l)$; theo mục lục 13.4.2 | Mục tiêu 8; §7.1; `L10-D01` |
| câu trả lời được chọn, bị loại | preferred, dispreferred completion (chosen, rejected) | $y_w$, $y_l$ | §7.1 (Định nghĩa 10.53) |
| mô hình Bradley–Terry | Bradley–Terry model | tên riêng, không dịch | Mục tiêu 8; §7.1; `L10-D02` |
| mô hình phần thưởng | reward model | $\hat r$; theo mục lục 13.4.1 | Mục tiêu 8; §7.1; `L10-D02` |
| ước lượng hợp lý cực đại | maximum likelihood estimation | Mệnh đề 10.54; kiến thức học máy (GC-RL-16) | §7.1 |
| lớp tương đương của phần thưởng | reward equivalence class | $[r]=\{r+f:\ f\text{ chỉ phụ thuộc }x\}$ | §7.1 (Định nghĩa 10.53) |
| chính sách tham chiếu | reference policy, reference model | $\pi_{\mathrm{ref}}$, cố định trong cả Mục 7; trong Bài 10 chỉ có nghĩa này | Mục tiêu 8; §7.2; `L10-D04` |
| mục tiêu có phạt KL | KL-regularized objective, KL-constrained reward maximization | $J_\beta$; luôn kèm "theo chính sách tham chiếu" khi có thể nhầm với phạt KL của PPO-Penalty (xem quy ước dưới bảng) | Mục tiêu 8; §7.2; `L10-D04` |
| hàm phân hoạch | partition function | $\mathcal Z_r(x)$ | §7.2 (Định lý 10.57); `L10-D05` |
| nghiệm dạng đóng | closed-form solution | $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$ | §7.2; `L10-D05` |
| tinh chỉnh có giám sát (SFT) | supervised fine-tuning | $\pi^{\mathrm{SFT}}$ | §7.3 (Thuật toán 10.61); `L10-D08` |
| học tăng cường từ phản hồi con người (RLHF) | reinforcement learning from human feedback | theo mục lục 13.5 (không "phản hồi của con người"); sau lần đầu viết RLHF | Mục tiêu 8; §7.3; `L10-D08` |
| phần thưởng đã trừ KL | KL-penalized reward | $\tilde r_\theta=r-\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$ | §7.3 (Mệnh đề 10.60); `L10-D08` |
| phạt KL theo từng token | per-token KL penalty | Ouyang và cộng sự (2022, §3.5) | §7.3 (Bổ đề 10.59) |
| tối ưu quá mức mô hình phần thưởng | reward model over-optimization (overoptimization) | theo mục lục 13.5.2 | §7.3 (Nhận xét 10.62) |
| tối ưu ưu tiên trực tiếp (DPO) | Direct Preference Optimization | tên đầy đủ ở lần đầu, sau đó DPO | Mục tiêu 9; §7.4; `L10-D10` |
| phương pháp căn chỉnh trực tiếp; căn chỉnh | direct alignment methods; alignment | theo mục lục 13.6 | §7.4 |
| đổi biến phần thưởng | reparameterization | Mệnh đề 10.63; "Kỹ thuật." trên `L10-D10` nếu storyboard dùng (kế hoạch C6) | §7.4; `L10-D10` |
| phần thưởng ngầm định | implicit reward | $r_\theta$, hiệu $\Delta r_\theta$ | §7.4 (Định nghĩa 10.64); `L10-D11` |
| ưu tiên tất định | deterministic preference | $\Pr(y_1\succ y_2\mid x)=1$ | §7.5 (Nhận xét 10.69); `L10-D16` |
| ngoại tuyến; trực tuyến | offline; online | dữ liệu cố định; mẫu sinh trong khi học | §7.3–7.5; `L10-D15` |
| tối ưu ưu tiên đồng nhất (IPO) | Identity Preference Optimization, ΨPO | chỉ ở §7.6 | §7.6 (ghi chú diễn giả `L10-D15`, `L10-D16`) |

Quy ước cho phần mới:

- **Hai tên gần nhau.** Hàng "mục tiêu phạt KL; hệ số phạt thích nghi" (PPO-Penalty, KL-penalized objective, chiều cũ‖mới, theo $\pi_{\mathrm{old}}$) và "mục tiêu có phạt KL" (Mục 7, KL-regularized objective, chiều $\pi\Vert\pi_{\mathrm{ref}}$) chỉ khác chữ "có". Ghi chú hiện viết "phạt KL" cho PPO-Penalty (§6.2, §8.3, Tóm tắt), không dùng cụm "mục tiêu phạt KL"; deck dùng cụm đó một lần (`L10-607`). Quy ước: trong Mục 7, ở lần đầu của mỗi tiểu mục và ở mọi chỗ so sánh với PPO-Penalty, viết đủ "mục tiêu có phạt KL theo chính sách tham chiếu"; khi nói tới PPO-Penalty trong Mục 7 và Mục 8, viết "phạt KL theo chính sách cũ (PPO-Penalty)". Người rà văn phong kiểm quy ước này (VP4).
- **"Mỏ neo"** là từ tiếng Việt của học phần cho chính sách mà phép phạt KL giữ chính sách mới ở gần ($\pi_{\mathrm{old}}$ hoặc $\pi_{\mathrm{ref}}$); không kèm tên tiếng Anh; định nghĩa bằng lời ở Nhận xét 10.58 trước khi dùng ở Ví dụ 10.27 và bảng §7.5.
- Hàng "phân kỳ Kullback–Leibler (KL)" ở bảng trên: chiều cũ‖mới cho Mục 4–6; Mục 7 dùng chiều $\pi_\theta\Vert\pi_{\mathrm{ref}}$ (Định nghĩa 10.56), nêu rõ ở Nhận xét 10.58.
- Thuật ngữ bỏ hoặc không dùng: "prompt", "reward model", "reference model" để trần; "phản hồi của con người"; "đáp án"; $r^*$, $Z(x)$, $r_\phi$, $\mathcal D$ cho dữ liệu ưu tiên, $\tau$ cho hệ số KL.

Thuật ngữ bỏ của bộ trang chiếu cũ: "surrogate", "truncation", "rollout", "batch", "value clipping", "clip fraction" để trần; "hợp đồng"; $\widehat A^{\mathrm{actor}}$; $w_t$; $d^\pi$, $\mathbb E_{\mathrm{disc},\pi}$, $\mathbb E_B$; $m_t$, $c_t$ (thay bằng $1-Z_{t+1}$, $(1-Z_{t+1})(1-U_{t+1})$); $H$ cho độ dài đoạn (thay bằng $h$).

### Quyết định ký hiệu

- Phân phối đầu $\mu_0$ (Bài 09: $\rho_0$), nêu ở `L10-102` và trong ghi chú diễn giả.
- Tỉ số $\rho_t(\theta)$, $\rho_\theta(s,a)$; Bài 11 viết $w_t$ cho tỉ số này và $\rho_t$ cho tỉ số với chính sách hành vi, nêu trong ghi chú diễn giả `L10-709`.
- $\epsilon$ (bán kính cắt), $\kappa$ (bán kính KL), $\kappa_{\mathrm{targ}}$ (PPO-Penalty), $\varepsilon_{\mathrm{cg}}$ (ngưỡng gradient liên hợp, chỉ trong thuật toán); $\delta_t$ chỉ là sai số TD.
- $T$ là bước kết thúc lượt; $h$ là độ dài đoạn thu.
- $b$ là đường cơ sở; $\beta$ là hệ số phạt; chính sách hành vi luôn là $\pi_{\mathrm{old}}$.
- $\sigma$ là hàm logistic; độ lệch chuẩn mini-batch viết $s_{\mathcal B}$.
- Chiều KL: ràng buộc TRPO, $D_t$ của PPO-Penalty và approxKL đều là cũ‖mới.
- Không viết $A$ trần cho lợi thế.
- Mục 7 (2026-11-19, Q5): $\mathcal Z_r(x)$ cho hàm phân hoạch ($Z_{t+1}$ là cờ kết thúc); $\mathcal D_{\mathrm{pref}}$ ($\mathcal D$ là bộ đệm); $\hat r$ cho mô hình phần thưởng ($\phi$ là đặc trưng); $r$ cho phần thưởng sinh dữ liệu, không $r^*$; $\beta$ dùng chung với PPO-Penalty, nghĩa mở rộng trong bảng ký hiệu; $\sigma(z)$ cho hàm logistic ($\sigma(x)$ cục bộ ở Ví dụ 10.2 giữ nguyên); $\Delta r_\theta$ cho hiệu phần thưởng ngầm định, $\theta_1-\theta_2$ cho hiệu logit; số cặp $n$, số cặp chọn $y_1$ là $k$, cục bộ trong Mệnh đề 10.54 và bài tập. Chỉ số dưới $r$ của $\pi^*_r$, $\mathcal Z_r$ bỏ khi phần thưởng rõ từ ngữ cảnh.
- Số câu trả lời được xếp hạng cho một lời nhắc (IG viết $K$): $K$ đã là số epoch và mọi chữ Latin đơn trong chương đã có nghĩa, nên dùng ký hiệu cục bộ $n_{\mathrm{xh}}$ (chỉ trong Nhận xét 10.55, ghi vào danh sách nghĩa cục bộ), hoặc viết bằng lời (sửa vòng 2, P-12). Cũng không dùng $\mu$, $\rho$, $\Psi$ của IPO và $f$ theo nghĩa toán tử chiếu của DPO (8) hay của XU; bảng tương ứng với bài báo ghi thêm $\rho$ của IPO, $f$ của DPO (8) và XU, cặp $\theta/\phi$ ngược của IG, ST, và một câu cảnh báo: DPO đặt dấu mũ cho phần thưởng ngầm định ($\hat r_\theta$), học phần đặt dấu mũ cho mô hình phần thưởng tường minh ($\hat r$) (P-11, mục 5 của báo cáo phân tích nguồn).
- Chiều KL của Mục 7: $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ (mới‖tham chiếu), ngược chiều cũ‖mới của TRPO, PPO-Penalty, approxKL.

### Ánh xạ hai chiều `note-topic-id` ↔ `data-slide-id`

**Chủ đề → trang.**

| `note-topic-id` | nhóm | khối của ghi chú | trang |
|---|---|---|---|
| `lec-10-topic-01` | cầu nối | Kiến thức tiên quyết, Bảng ký hiệu, Quy ước đọc | `L10-102`, `L10-103` |
| `lec-10-topic-02` | cầu nối | Mục tiêu, Bảy phần, §1.1, Ví dụ 10.1, 10.2, hình cấu trúc | `L10-101`, `L10-104`–`L10-110` |
| `lec-10-topic-03` | cốt lõi | §2.1, Ví dụ 10.3, Định nghĩa 10.1, Mệnh đề 10.2, Ví dụ 10.4, Bài tập 10.1 | `L10-200`–`L10-206`, `L10-210` |
| `lec-10-topic-04` | bổ sung | §2.2, Mệnh đề 10.3 | một dòng "Lưu ý:" trên `L10-202` (thuộc tính của trang là `topic-03`) |
| `lec-10-topic-05` | cốt lõi | §2.3, Định nghĩa 10.4, Mệnh đề 10.5, Ví dụ 10.5, Thuật toán 10.6 | `L10-207`–`L10-209` |
| `lec-10-topic-06` | cốt lõi | §2.4, Ví dụ 10.6, 10.7, Định nghĩa 10.7, Mệnh đề 10.8, Thuật toán 10.9, Nhận xét 10.10, Bài tập 10.5 | `L10-211`–`L10-216` (kể cả `L10-212b`) |
| `lec-10-topic-07` | cầu nối | §3.1, Ví dụ 10.8, Định nghĩa 10.11, Bổ đề 10.12 | `L10-300`–`L10-302` |
| `lec-10-topic-08` | cốt lõi | §3.2, Định nghĩa 10.13, Mệnh đề 10.14, 10.15, Ví dụ 10.9 | `L10-303`–`L10-306` |
| `lec-10-topic-09` | cốt lõi | §3.3, Ví dụ 10.10, Thuật toán 10.16, Nhận xét 10.17, Bài tập 10.7 | `L10-307`–`L10-309` |
| `lec-10-topic-10` | cốt lõi | §4.1, Ví dụ 10.11, Định nghĩa 10.18, Bổ đề 10.19, Hệ quả 10.20 | `L10-400`–`L10-404` |
| `lec-10-topic-11` | cốt lõi | §4.2, Định nghĩa 10.21, Mệnh đề 10.22 | `L10-405`, `L10-406` |
| `lec-10-topic-12` | cầu nối | §4.3, Định nghĩa 10.23, Mệnh đề 10.24 | `L10-407` |
| `lec-10-topic-13` | cốt lõi | §4.4, Bổ đề 10.25, Định lý 10.26, Ví dụ 10.12, Hệ quả 10.27 | `L10-408`–`L10-410` |
| `lec-10-topic-14` | cốt lõi | §4.5, Hệ quả 10.29, Định nghĩa 10.30, Hệ quả 10.31, Bài tập 10.11 | `L10-411`–`L10-414` (kể cả `L10-412b`) |
| `lec-10-topic-15` | cốt lõi | §5.1, Ví dụ 10.13–10.15, Định nghĩa 10.32, Mệnh đề 10.33, 10.34, Nhận xét 10.35 | `L10-500`–`L10-504` (kể cả `L10-502b`) |
| `lec-10-topic-16` | cốt lõi | §5.2, Ví dụ 10.16, Thuật toán 10.36, 10.37, Nhận xét 10.38, Bài tập 10.8 | `L10-505`–`L10-510` |
| `lec-10-topic-17` | cốt lõi | §6.1, Ví dụ 10.17, 10.18, Định nghĩa 10.39, Mệnh đề 10.40, 10.41, Nhận xét 10.42 | `L10-600`–`L10-606` |
| `lec-10-topic-18` | cốt lõi | §6.2, Ví dụ 10.19, Định nghĩa 10.43, Nhận xét 10.44 (và câu (d) của Bài tập 10.12) | `L10-607`, `L10-608` |
| `lec-10-topic-19` | cốt lõi | §6.3, Định nghĩa 10.45–10.47, Ví dụ 10.20, Mệnh đề 10.48, Thuật toán 10.49, Bài tập 10.12 | `L10-609`–`L10-613` (kể cả `L10-611b`), `L10-619`, `L10-620` |
| `lec-10-topic-20` | cốt lõi | §6.4, Ví dụ 10.21, bảng siêu tham số, bảng so sánh | `L10-614`–`L10-616` |
| `lec-10-topic-21` | cốt lõi | §6.5, Ví dụ 10.22, Nhận xét 10.50 | `L10-617`, `L10-617b` |
| `lec-10-topic-22` | đọc thêm | §6.6, Nhận xét 10.51 | `L10-618` |
| `lec-10-topic-23` | cầu nối | §8.1–8.5 (trước 2026-11-19 là §7.1–7.5), Tình huống 10.1, 10.2 | `L10-700`–`L10-710` (kể cả `L10-702b`; sau bổ sung DPO thêm `L10-702c`, tùy chọn `L10-703b`) |
| `lec-10-topic-24` | cầu nối (trước 2026-11-19: đọc thêm) | §8.6 (trước là §7.6) | trước Q8: một dòng nối Bài 11 trên `L10-710`; sau Q8 dòng này bỏ, giới hạn còn lại nêu trong ghi chú diễn giả `L10-710` (storyboard chốt; thuộc tính của trang là `topic-23`) |
| `lec-10-topic-25` | cầu nối | §7.1, Định nghĩa 10.52, 10.53, Mệnh đề 10.54, Nhận xét 10.55, Ví dụ 10.23, 10.24 | dự kiến `L10-D00`–`L10-D03` |
| `lec-10-topic-26` | cốt lõi | §7.2, Định nghĩa 10.56, Định lý 10.57, Nhận xét 10.58, Ví dụ 10.25, 10.26; Bài tập 10.18 | dự kiến `L10-D04`–`L10-D07`, `L10-D17`, `L10-D18` |
| `lec-10-topic-27` | cốt lõi | §7.3, Bổ đề 10.59, Mệnh đề 10.60, Thuật toán 10.61, Nhận xét 10.62, Ví dụ 10.27 | dự kiến `L10-D08`, `L10-D09` |
| `lec-10-topic-28` | cốt lõi | §7.4, Mệnh đề 10.63, Định nghĩa 10.64, Định lý 10.65, Mệnh đề 10.66, Thuật toán 10.67, Nhận xét 10.68, Ví dụ 10.28 | dự kiến `L10-D10`–`L10-D14` |
| `lec-10-topic-29` | cốt lõi | §7.5, bảng so sánh, Nhận xét 10.69; Tình huống 10.5 | dự kiến `L10-D15`, `L10-D16` |
| `lec-10-topic-30` | đọc thêm | §7.6, Nhận xét 10.70 | chỉ ghi chú diễn giả `L10-D15`, `L10-D16` (thuộc tính của trang là `topic-29`) |

**Trang → chủ đề.** Mỗi trang mang đúng một `data-note-topic-id` theo bảng trên; trang tiêu đề mạch mang chủ đề của khái niệm đầu tiên trong mạch (`L10-200` → `topic-03`, `L10-300` → `topic-07`, `L10-400` → `topic-10`, `L10-500` → `topic-15`, `L10-600` → `topic-17`, `L10-700` → `topic-23`). Đủ 24/24 chủ đề: 22 chủ đề có trang mang thuộc tính; `topic-04` (bổ sung) và `topic-24` (đọc thêm) mỗi chủ đề một dòng. Mọi chủ đề cốt lõi (03, 05, 06, 08–11, 13–21) có ít nhất một trang nội dung. Tổng 101 `data-slide-id` duy nhất (kiểm bằng Playwright ở D1). `L10-705`, `L10-706` (Tình huống 10.1, 10.2) mang `topic-23` dù trong ghi chú các tình huống đứng sau mốc `topic-24`: hai trang là bài tổng hợp của mạch kết luận, và ghi chú cũng xếp tình huống vào `topic-23`; liên kết từ trang chiếu sang ghi chú vì vậy mở §7, không mở mục tình huống. Cột "nhóm" lấy từ bản đồ chủ đề của commit `1c9ef05` (đã bỏ khỏi ghi chú ở `567c96c`) để kiểm độ phủ. Bài tập 10.11 phủ chủ đề 10–14, gán `topic-14` vì đứng cuối mạch; Bài tập 10.12 phủ 17–19, gán `topic-19`.

**Bổ sung DPO (2026-11-19).** Cột trang của `topic-25` … `-30` là dự kiến theo kế hoạch C2; storyboard (giai đoạn III.1) chốt. Trang tiêu đề mạch `L10-D00` mang `topic-25`. Bài tập 10.18 (trên trang `L10-D17`, `L10-D18`) gán `topic-26`, chủ đề của Định lý 10.57 mà bài dùng. Mọi chủ đề cốt lõi mới (26–29) có ít nhất một trang nội dung; `topic-30` (đọc thêm) chỉ ở ghi chú diễn giả. `L10-104b` (tách từ `L10-104`) mang `topic-02`. Tổng sau bổ sung: 30 chủ đề, 120–123 `data-slide-id`. `topic-24` đổi nhóm sang cầu nối vì sau Q8 tiểu mục chỉ còn đoạn giới hạn còn lại của chương, không còn nội dung đọc thêm (SPO, SAM+PPO); điều phối viên đã duyệt (vòng 2).

### Phân loại chủ đề

GC-RL-12, GC17: phân loại bốn nhóm chỉ nằm ở đây, không vào ghi chú. Nhóm của `topic-01` … `-23` lấy từ cột "nhóm" của bảng ánh xạ (bản đồ chủ đề của commit `1c9ef05`); `topic-24` đổi nhóm theo Q8; `topic-25` … `-30` theo kế hoạch A6. Mục 7 không áp quy định "nội dung dựa chủ yếu vào bài báo xếp `bổ sung`" ("P1, Bài 10, Mục 7 (riêng)"): tác giả yêu cầu DPO là nội dung của bài và mục lục giáo trình đặt nó ở 13.4–13.6.

| `note-topic-id` | Phần ghi chú | Nhóm | Lý do ngắn |
|---|---|---|---|
| `lec-10-topic-01` | Kiến thức tiên quyết, Bảng ký hiệu | cầu nối | nhắc lại Bài 03–09 và kiến thức học máy |
| `lec-10-topic-02` | Mục tiêu, §1.1 | cầu nối | kết quả kế thừa, bài toán trung tâm ba phần |
| `lec-10-topic-03` | §2.1 Đường cơ sở | cốt lõi | |
| `lec-10-topic-04` | §2.2 Đường cơ sở có phương sai nhỏ nhất | bổ sung | Greensmith và cộng sự (2004) |
| `lec-10-topic-05` | §2.3 Hàm lợi thế | cốt lõi | |
| `lec-10-topic-06` | §2.4 Critic và actor–critic một bước | cốt lõi | |
| `lec-10-topic-07` | §3.1 Lợi tức n bước | cầu nối | nhắc lại Bài 07 cho GAE |
| `lec-10-topic-08` | §3.2 Lợi tức λ và GAE | cốt lõi | |
| `lec-10-topic-09` | §3.3 GAE trên đoạn thu | cốt lõi | |
| `lec-10-topic-10` | §4.1 Bổ đề chênh lệch hiệu năng | cốt lõi | |
| `lec-10-topic-11` | §4.2 Tỉ số chính sách và hàm thay thế | cốt lõi | |
| `lec-10-topic-12` | §4.3 Khoảng cách giữa hai chính sách | cầu nối | TV, KL, Pinsker; Mệnh đề 10.24 dùng lại ở Định lý 10.57 |
| `lec-10-topic-13` | §4.4 Chặn cải thiện | cốt lõi | |
| `lec-10-topic-14` | §4.5 Cải thiện đơn điệu và miền tin cậy | cốt lõi | |
| `lec-10-topic-15` | §5.1 KL bậc hai và gradient tự nhiên | cốt lõi | |
| `lec-10-topic-16` | §5.2 TRPO thực hành | cốt lõi | |
| `lec-10-topic-17` | §6.1 PPO-Clip | cốt lõi | |
| `lec-10-topic-18` | §6.2 PPO-Penalty | cốt lõi | mỏ neo $\pi_{\mathrm{old}}$, đối chiếu ở Nhận xét 10.58 |
| `lec-10-topic-19` | §6.3 Hàm mất mát tổng và thuật toán PPO | cốt lõi | Thuật toán 10.49 dùng trong Thuật toán 10.61 |
| `lec-10-topic-20` | §6.4 Chẩn đoán và siêu tham số | cốt lõi | |
| `lec-10-topic-21` | §6.5 Chi tiết cài đặt | cốt lõi | |
| `lec-10-topic-22` | §6.6 Hội tụ về điểm dừng của PPO-Clip | đọc thêm | Jin, Li và Wang (2024) |
| `lec-10-topic-23` | §8.1–8.5 Tổng kết | cầu nối | tổng hợp, không khái niệm mới |
| `lec-10-topic-24` | §8.6 Giới hạn còn lại | cầu nối (trước: đọc thêm) | sau Q8 chỉ còn giới hạn của chương; điều phối viên đã duyệt (vòng 2) |
| `lec-10-topic-25` | §7.1 Dữ liệu ưu tiên và mô hình Bradley–Terry | cầu nối | chuyển hồi quy logistic (học máy) sang phần thưởng; khoảng trống: Thuật toán 10.49 cần $R_{t+1}$ mà bài toán chỉ có so sánh; nguồn DPO §3, CH §2.2.3 |
| `lec-10-topic-26` | §7.2 Mục tiêu có phạt KL theo chính sách tham chiếu | cốt lõi | Định lý 10.57, luận điểm mức 1 |
| `lec-10-topic-27` | §7.3 RLHF với PPO | cốt lõi | Thuật toán 10.61, luận điểm mức 2 |
| `lec-10-topic-28` | §7.4 Tối ưu ưu tiên trực tiếp | cốt lõi | Định lý 10.65, Thuật toán 10.67 |
| `lec-10-topic-29` | §7.5 So sánh hai con đường và giới hạn | cốt lõi | bảng so sánh, luận điểm mức 3 |
| `lec-10-topic-30` | §7.6 Biến thể và so sánh thực nghiệm | đọc thêm | IPO, cách đọc mức token của DPO (RQ), so sánh thực nghiệm DPO §6.1 và XU |

Tổng: cốt lõi 20 (03, 05, 06, 08–11, 13–21, 26–29), cầu nối 7 (01, 02, 07, 12, 23–25), bổ sung 1 (04), đọc thêm 2 (22, 30). Trong các chủ đề cốt lõi của Mục 7, các giá trị thực nghiệm của bài báo (Nhận xét 10.55, 10.62; giá trị Phụ lục B của DPO trong "Trong thực hành") là chi tiết thực hành của chủ đề, không tách thành chủ đề riêng. Dạng mức token của Định nghĩa 10.52(b) và Bổ đề 10.59 thuộc chủ đề cốt lõi vì Thuật toán 10.61, 10.67 dùng chúng; cách đọc DPO như hàm $Q$ mức token của RQ thuộc `topic-30`.

### Bài tập: kế hoạch bổ sung DPO (2026-11-19)

Số hiệu theo Q4 và BT-RL-10: `exercises.md` giữ 10.13–10.17; bốn bài mới của ghi chú là 10.18–10.21, cuối "Mức vận dụng" của "Bài tập củng cố", sau Bài tập 10.12 (ghi chú nhảy từ 10.12 sang 10.18); Sutton và Barto (2018) Bài tập 2.9 thành Bài tập 10.22 trong `exercises.md`. Mỗi bài của ghi chú: một `hint`, một `solution` chia "**Câu (a).**", kết bằng "**Kiểm tra lại.**", đề tự chứa (GC23, BT-RL-5). Đề, lời giải và số đã tính lại ở kế hoạch B2 (số hiệu cũ của kế hoạch ghi trong ngoặc).

| Số | Tên (bản nháp) | Mức | Mục tiêu | Kiến thức cuối cần | Nội dung và số chính | Trên deck |
|---|---|---|---|---|---|---|
| 10.18 (kế hoạch 10.13) | Nghiệm có phạt KL trên ba câu trả lời | vận dụng | 8 | §7.2 (Định lý 10.57) | $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, $r=(\log2;\,0;\,0)$; (a) $\beta=1$: $\mathcal Z=\tfrac32$, $\pi^*=(\tfrac23;\,\tfrac16;\,\tfrac16)$, $\max J_1=\log\tfrac32$; (b) phần thưởng ngầm định $r-\log\tfrac32\in[r]$; (c) $\beta=\tfrac12$: $\pi^*=(0{,}8;\,0{,}1;\,0{,}1)$ | (a)–(b) trên `L10-D17` (đề), `L10-D18` ("Lời giải:"); (c) trong ghi chú diễn giả |
| 10.19 (kế hoạch 10.14) | Hàm mất mát DPO với hai câu trả lời | vận dụng | 9 | §7.4 (Định lý 10.65, Mệnh đề 10.66) | (a) cực tiểu khi $\beta(\theta_1-\theta_2-\log2)=\log\frac k{n-k}$, trùng $\pi^*_{\hat r}$; (b) $n=5$, $k=4$: $\pi=(\tfrac89;\,\tfrac19)$, gradient $(-0{,}3;\,0{,}3)$, sau một bước $\pi_\theta(y_1)=0{,}7847$; (c) $k=n$: không cực tiểu | bài về nhà |
| 10.20 (kế hoạch 10.15) | Dữ liệu không phủ một câu trả lời | vận dụng | 9 (giả thiết (H4b) của Định lý 10.65) | §7.4–7.5 | $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, sáu so sánh chỉ giữa $y_1$, $y_2$; mọi $\pi$ có $\pi(y_1)=4\pi(y_2)$ là cực tiểu; KL của ba cực tiểu $0{,}0566$; $0{,}0328$; $0{,}1657$; con đường RLHF cho $\pi^*\propto(1;\,\tfrac14;\,\tfrac14e^c)$ phụ thuộc $\hat r(y_3)=c$. Sửa vòng 2 (P-04): câu (c) kết luận (H4a) thỏa, (H4b) hỏng; khi $c$ chạy trên $\mathbb R$, $\pi^*(y_3)$ phủ cả $(0;\,1)$, nên tập nghiệm của hai con đường **trùng nhau** và không duy nhất, không phải "hai con đường khác nhau"; đề câu (c) sửa thành yêu cầu chỉ ra hai tập nghiệm bằng nhau; câu "Kiểm tra lại" giữ. Nguồn đối chiếu (chỉ ở `review-log.md`): IPO Phụ lục A.2 | bài về nhà |
| 10.21 (kế hoạch 10.16) | Hai mỏ neo khi bán kính cắt nhỏ | vận dụng | 8 (phân biệt chính sách cũ và chính sách tham chiếu) | §7.3 (Ví dụ 10.27) | như Ví dụ 10.27 với $\epsilon=0{,}1$, đề nêu rõ cách cực đại hóa (tới biên đầu tiên của đoạn phẳng, Q4); dãy $p$: $0{,}7333$; $0{,}8067$; $0{,}7260$; $J_1$: $0{,}4979$; $0{,}5107$; $0{,}4950$ | bài về nhà |
| 10.22 (`exercises.md`) | Softmax hai hành động và hàm logistic | nhận biết | 8 | §7.1 (Định nghĩa 10.53) | Sutton và Barto (2018), Bài tập 2.9, §2.8, tr. 37; đề dịch sát câu của sách, không thêm câu nối Bradley–Terry vào đề (BT-RL-1); câu nối với Định nghĩa 10.53 chỉ trong lời giải; "Hướng dẫn và ký hiệu" thêm một đoạn ($H_t(a)$ của sách, logit $\theta$ của ghi chú) | bài về nhà; hàng mạch 7 của `L10-709` |

**Phủ mục tiêu học tập** (BT9, GC26):

| Mục tiêu | Kết quả hoặc ví dụ của ghi chú | Bài tập của ghi chú | `exercises.md` |
|---|---|---|---|
| 1–7 | như hiện có | như câu dẫn hiện có | 10.13–10.17, không đổi |
| 8 | Mệnh đề 10.54, Định lý 10.57, Mệnh đề 10.60, Thuật toán 10.61; Ví dụ 10.23–10.27 | 10.18, 10.21 | 10.22 (nhận biết) |
| 9 | Mệnh đề 10.63, Định lý 10.65, Mệnh đề 10.66, Thuật toán 10.67; Ví dụ 10.28; Tình huống 10.4, 10.5 | 10.19, 10.20 | — (các giáo trình của BT-RL-1 không có bài về DPO; ghi lý do vào `review-log.md`) |

Câu dẫn mới của "Bài tập củng cố": "Các bài phủ chín mục tiêu học tập: mục tiêu 1 (…), …, 7 (…), 8 (10.18, 10.21), 9 (10.19, 10.20)." Phần nhận biết của mục tiêu 8, 9 do Bài tập 10.22 và câu hỏi tự kiểm tra mới ở §8.4 đảm nhận; không thêm bài nhận biết vào ghi chú, vì đặt giữa "Mức nhận biết" làm số không tăng theo thứ tự đọc (kế hoạch B2, QB3).

`exercises.md` (giai đoạn II): đoạn mở nêu sáu bài, dải 10.13–10.17 và 10.22, và rằng mục tiêu 9 dựa vào bài của ghi chú; bảng `Mạch | Mở phần | Bài tập` thêm hàng `7. Tối ưu chính sách từ phản hồi ưu tiên | #/7/1 | 10.22; ghi chú: 10.18–10.21`, hàng cuối thành `8. Tổng kết | #/8/1 | ghi chú: 10.3`; liên kết `#/7/1`, `#/8/1` kiểm lại sau deck (BT-RL-9). Không đổi số nào đã có. Bảng `L10-709`: hàng mạch 7 ghi `10.22` (tệp bài tập) và `10.18 (trên lớp), 10.19, 10.20, 10.21` (ghi chú).

**Số hiệu đã chốt (điều phối viên, vòng 2).** Bốn bài 10.13–10.16 của kế hoạch thành 10.18–10.21 theo thứ tự; bài bán kính cắt là Bài tập 10.21. Ô "Đề xuất" của Q4 viết "đánh lại thành 10.20 theo thứ tự mới": đó là lỗi chép của điều phối viên, không phải quyết định khác; tác tử sau không theo câu chữ đó.

### Sai khác có chủ ý

**So với ghi chú bài giảng** (cần điều phối viên ghi `review-log.md`).

1. Ví dụ 10.9 (`L10-305`) đặt trước Mệnh đề 10.15 (`L10-306`); ghi chú đặt sau. Lý do: ví dụ đi trước phát biểu trong hành trình khái niệm; ví dụ chỉ dùng $\delta_t$, $\widehat A_t$ đã có ở `L10-302`–`L10-304`.
2. Mệnh đề 10.3 (`topic-04`) thu thành một dòng "Lưu ý:" trên `L10-202`; chứng minh và phạm vi chỉ trong ghi chú diễn giả. Lý do: chủ đề bổ sung, phương án nén.
3. Chứng minh Mệnh đề 10.14 thu thành một dòng "Chứng minh." trên `L10-304`; chứng minh Bổ đề 10.12 chỉ trong ghi chú diễn giả `L10-302` (D1, để có chỗ cho dòng "Trực quan."). Lý do: phương án nén; các bước đầy đủ ở ghi chú bài giảng.
4. Bổ đề 10.25 không có trang riêng: phát biểu trong bước cuối của `L10-409` (chứng minh chặn cải thiện); số kiểm $0{,}009\le0{,}288$ trong ghi chú diễn giả `L10-408`. Lý do: phương án nén.
5. Định nghĩa 10.18 gộp với Bổ đề 10.19 (`L10-403`), Hệ quả 10.20 chỉ trong ghi chú diễn giả. Lý do: phương án nén, rút theo cổng storyboard. Đợt sửa D1 tách các trang kết quả quá tải: Định nghĩa 10.30 (`L10-412`) và Hệ quả 10.31 (`L10-412b`); Định nghĩa 10.32 (`L10-502`) và Mệnh đề 10.33 (`L10-502b`); Định nghĩa 10.47 (`L10-611`, kèm dạng $-\log\rho$ và phương sai được giải thích; entropy trung bình và mất mát giá trị chỉ trong ghi chú diễn giả) và Mệnh đề 10.48 (`L10-611b`). Hệ quả 10.29 ở `L10-411`; Ví dụ 10.19 (`L10-607`) và Định nghĩa 10.43 (`L10-608`) ở hai trang, ví dụ trước quy tắc.
6. Nhận xét 10.42 thành dòng "Lưu ý:" của `L10-606`; Nhận xét 10.44 thành dòng "Lưu ý:" của `L10-608`; Nhận xét 10.35 vào `L10-504`; Nhận xét 10.10 và 10.17 chỉ trong ghi chú diễn giả (`L10-215`, `L10-308`); Nhận xét 10.28 chỉ trong ghi chú diễn giả `L10-408`.
7. Biến thể cắt mất mát giá trị (cuối Định nghĩa 10.46) trình bày ở `L10-617` cùng Ví dụ 10.22, không ở `L10-609`; D1 đặt ví dụ này (`L10-617`) trước bảng của Nhận xét 10.50 (`L10-617b`), đúng thứ tự Ví dụ 10.22 → Nhận xét 10.50 của ghi chú.
8. Tình huống 10.3 (Breakout) không lên mặt trang; số đo notebook không trình chiếu như số đo của PPO. Câu (e) của Bài tập 10.11 ($0{,}317$) chỉ trong ghi chú diễn giả `L10-414`.
9. Bài tập 10.1, 10.5, 10.7, 10.8, 10.11(a)–(d), 10.12 và Tình huống 10.1–10.2 lên mặt trang làm bài tập có lời giải; câu (d) của Bài tập 10.12 (PPO-Penalty) đặt ở `L10-608`, ngay sau định nghĩa, còn (a)–(c) ở `L10-619`–`L10-620`; các bài còn lại là bài về nhà (bảng `Mạch | Bài tập` ở `L10-709` trùng bảng §7.5 của ghi chú, sáu hàng như ghi chú).
10. `L10-207` đặt phần đầu của Ví dụ 10.5 (bài toán một bước, $q_\pi=(3;\,0)$, $v_\pi=2$) ngay sau dòng trực quan, trước Định nghĩa 10.4; ghi chú đi theo thứ tự Định nghĩa 10.4 → Mệnh đề 10.5 → Ví dụ 10.5. Lý do: ví dụ đi trước định nghĩa trong hành trình khái niệm; chuỗi suy luận không đổi. (Vai mạch, vòng D1.)
11. `L10-408` phát biểu Hệ quả 10.27 (dạng KL) ngay sau Định lý 10.26, trước Ví dụ 10.12 (`L10-410`); ghi chú đặt Ví dụ 10.12 trước Hệ quả 10.27. Lý do: một trang kết quả giữ định lý và hệ quả dạng KL cạnh nhau; ví dụ chỉ dùng dạng TV trên mặt trang, dạng KL ở ghi chú diễn giả. (Vai mạch, vòng D1.)
12. `L10-612` (đường dữ liệu, bảng "giữ cố định / tính lại", ở ghi chú đứng sau Thuật toán 10.49) đứng trước `L10-613` (Thuật toán 10.49). Lý do: trang đóng vai trực giác của cụm thuật toán PPO, trước giả mã. (Vai mạch, vòng D1.)
13. Số hiệu của ghi chú đứng trong nhãn của trang phát biểu kết quả ("**Mệnh đề 10.2.**"), một số hiệu mỗi trang; khi trang có hai kết quả, chỉ kết quả chính mang số (`L10-302` Định nghĩa 10.11; `L10-403` Bổ đề 10.19; `L10-407` Định nghĩa 10.23; `L10-408` Định lý 10.26), số hiệu còn lại ở ghi chú diễn giả. (Quyết định E2.)

**So với bài giảng gốc** (theo ánh xạ của ghi chú).

1. Tr. 5–8 (ôn REINFORCE, định lý gradient chính sách) thành trang nhắc lại `L10-103`; tr. 1–2 thành bìa và mục tiêu.
2. Tr. 24 (GAE trên đoạn thu) đưa lên mạch 3 (`L10-307`–`L10-309`), trước phần PPO, vì thuật toán GAE lùi là tiên quyết của Thuật toán 10.49.
3. Tr. 38 (PPO-Penalty) đưa lên ngay sau PPO-Clip (`L10-607`), vì ghi chú đặt hai biến thể cạnh nhau.
4. Tr. 26 (bảng siêu tham số không ghi nguồn) thay bằng Bảng 3 và Bảng 5 của Schulman và cộng sự (2017) (`L10-615`).
5. Tr. 29–34, 36 (chi tiết cài đặt) nén vào `L10-617`; tr. 35 (chẩn đoán miền tin cậy) chia cho `L10-606`, `L10-611`.
6. Tr. 37, 39–42 (lý thuyết PPO-Clip) nén vào trang đọc thêm `L10-618`; kết luận theo Jin, Li và Wang (2024), có giả thiết và phạm vi.
7. Bổ sung không có trong nguồn, theo ghi chú: hai ví dụ dẫn nhập định lượng (tr. 9–10, 14 chỉ nêu bằng lời), đường cơ sở tối ưu (Greensmith và cộng sự, 2004), chứng minh bổ đề chênh lệch hiệu năng (Kakade và Langford, 2002), chặn cải thiện dạng trung bình (Achiam và cộng sự, 2017), gradient liên hợp (Nocedal và Wright, 2006), approxKL và mệnh đề không chệch.

### Nguồn theo trang

| trang nguồn | nội dung | trang đích |
|---|---|---|
| 1–3 | bìa, mục tiêu, dàn ý | `L10-101`, `L10-104`, `L10-105` |
| 4 | bức tranh chung, bước lớn đổi phân bố trạng thái | `L10-108`, `L10-109`, `L10-401` |
| 5 | ký hiệu | `L10-102` |
| 6–10 | hàm mục tiêu, định lý gradient chính sách, REINFORCE | `L10-103`, `L10-106`, `L10-107` |
| 11 | đường cơ sở | `L10-201`–`L10-206`, `L10-209`, `L10-210` |
| 12 | actor–critic | `L10-211`–`L10-216` |
| 13 | GAE | `L10-301`–`L10-306` |
| 14 | vì sao cần TRPO | `L10-108`, `L10-401`, `L10-408` |
| 15 | chênh lệch hiệu năng, hàm thay thế | `L10-402`–`L10-406`, `L10-413`, `L10-414` |
| 16 | bài toán ràng buộc của TRPO | `L10-408`, `L10-410`, `L10-411`, `L10-412`, `L10-412b` |
| 17 | KL bậc hai, gradient tự nhiên | `L10-501`–`L10-504` (kể cả `L10-502b`) |
| 18–19 | TRPO thực hành, chi phí | `L10-505`–`L10-509`, `L10-601` |
| 20–22 | PPO-Clip, gradient sau khi cắt | `L10-601`–`L10-606` |
| 23 | hàm mất mát tổng | `L10-609`, `L10-610` |
| 24 | thu dữ liệu, GAE trên đoạn | `L10-307`–`L10-309`, `L10-612`, `L10-613` |
| 25 | vòng tối ưu PPO | `L10-613` |
| 26 | siêu tham số (thay bằng bảng có nguồn) | `L10-615` |
| 27 | chẩn đoán | `L10-611`, `L10-614` |
| 28 | so sánh TRPO và PPO | `L10-616`, `L10-703` |
| 29–34, 36 | chi tiết cài đặt | `L10-617`, `L10-617b` |
| 35 | chẩn đoán miền tin cậy | `L10-606`, `L10-611b` |
| 37, 39–42 | lý thuyết PPO-Clip | `L10-618`, `L10-704` |
| 38 | PPO-Penalty | `L10-607`, `L10-608` |
| 43 | tài liệu tham khảo | `L10-707`, `L10-710` |

Mạch 7 (`L10-D00` … `L10-D18`) không có trang nguồn: nguồn là Mục 7 của ghi chú đã kiểm định ("P1, Bài 10, Mục 7 (riêng)"); chỗ dẫn bài báo theo tiểu mục ở mục "Mục 7 của ghi chú".

### Hình

| hình | trạng thái | trang |
|---|---|---|
| `img/lec-10/central-problem.svg` | đã duyệt (ghi chú) | `L10-110` |
| `img/lec-10/two-state-chain.svg` | đã duyệt | `L10-211` (lưới hai cột, dữ kiện phần thưởng và chính sách ghi thành chữ bên cạnh, quyết định E5); bản nhỏ ở `L10-301` (dữ kiện cần dùng ghi trong dòng chữ); bản viết bỏ hình nhỏ ở `L10-402` |
| `img/lec-10/actor-critic-advantage.svg` | đã duyệt | `L10-212b` |
| `img/lec-10/gae-weights.svg` | đã duyệt | `L10-303` |
| `img/lec-10/policy-update-feedback.svg` | đã duyệt | `L10-401` |
| `img/lec-10/trpo-trust-region.svg` | đã duyệt | `L10-505` |
| `img/lec-10/ppo-one-step-plateau.svg` | đã duyệt | `L10-602` |
| `img/lec-10/ppo-clipping-signs.svg` | đã duyệt | `L10-605` |
| `img/lec-10/ppo-data-pipeline.svg` | đã duyệt | `L10-612` |
| `img/lec-09/one-step-card.svg` | dùng lại | `L10-106`, `L10-202`, `L10-504` (bản viết bỏ ở `L10-610`) |
| `img/lec-09/short-corridor.svg` | dùng lại | `L10-107` |
| `img/lec-08/termination-truncation.svg` | không dùng (D1 bỏ khỏi `L10-307`: nhãn mục tiêu DQN gây nhầm, bảng đủ dữ kiện; mô tả hai cờ ở ghi chú diễn giả) | — |
| `img/lec-10/gae-bias-variance.svg`, `img/lec-10/ppo-diagnostics.svg` | đã xóa | không trang nào tham chiếu (khẳng định không căn cứ; thay bằng bảng) |

Không vẽ hình mới. Các phép tính lặp dùng bảng HTML cố định thay hình (xem `storyboard.md`, mục "Khuôn bảng cố định").

**Bổ sung DPO (2026-11-19, kế hoạch A11).** SVG vẽ bằng script trong `tools/courses/rl-plan/2627-1/img/lec-10/`, xuất vào `2627-1/img/lec-10/`; không raster (VP10, GC12); công thức đầy đủ ở KaTeX, trong hình chỉ nhãn ngắn (NT25).

| hình | trạng thái | ghi chú; trang |
|---|---|---|
| `img/lec-10/central-problem.svg` | sửa | thêm hàng thứ ba "Mục 7: phạt KL theo $\pi_{\mathrm{ref}}$ cố định; RLHF với PPO, DPO" nối vào khung PPO; alt sửa theo; §1.1; `L10-110` |
| `img/lec-10/rlhf-dpo-hai-con-duong.svg` | mới | từ $\mathcal D_{\mathrm{pref}}$ hai nhánh: nhánh trên nét liền, mô hình phần thưởng (Mệnh đề 10.54) → PPO với $\pi_{\mathrm{ref}}$, critic, mẫu trực tuyến (Thuật toán 10.61); nhánh dưới nét đứt, $L^{\mathrm{DPO}}$ với $\pi_{\mathrm{ref}}$ (Thuật toán 10.67); hai nhánh gặp ở khung đậm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57, 10.65); số mô hình trong bộ nhớ 4 và 2; §7.4 hoặc §7.5; trên deck `L10-D15` là bảng, hình chỉ thay hai hàng khi bảng vượt trần (QT7) |
| `img/lec-10/muc-tieu-phat-kl.svg` | mới, tùy chọn | $J_1(p)$ trên $(0;\,1)$, cực đại $0{,}5108$ tại $p=0{,}8$; ba điểm $\pi_{\mathrm{ref}}$, $(0{,}8;\,0{,}2)$, tham lam; đường nét đứt $\mathbb E\hat r=p\log2$; Ví dụ 10.26; `L10-D07` |

### Phân bổ thời lượng

| mạch | trang | số trang | phút |
|---|---|---:|---:|
| 1 | `L10-101`–`L10-110` | 10 | 12 |
| 2 | `L10-200`–`L10-216` | 18 | 23 |
| 3 | `L10-300`–`L10-309` | 10 | 14,5 |
| 4 | `L10-400`–`L10-414` | 16 | 22,5 |
| 5 | `L10-500`–`L10-510` | 12 | 13,5 |
| 6 | `L10-600`–`L10-620` | 23 | 25,5 |
| 7 | `L10-700`–`L10-710` | 12 | 9 |
| **Tổng** | | **101** | **120** |

Phút từng trang nằm trong `storyboard.md`.

**Sau bổ sung DPO (Q7, kế hoạch C4; thời lượng chỉ ghi ở planning, GC17, NT27).** Deck 135 phút, chữa bài 15 phút (tổng 150). Thêm mạch 7 (22 phút) và khoảng 1 phút cho các bảng tổng kết mở rộng thành 143; rút 8 phút mà không bỏ trang: trang lời giải `L10-414`, `L10-510`, `L10-620`, `L10-706` chuyển sang phần chữa bài (4 phút); trang chứng minh `L10-205`, `L10-404`, `L10-409` từ 4,5 xuống 3; trang chi tiết cài đặt và đọc thêm `L10-614`, `L10-615`, `L10-617`, `L10-617b`, `L10-618` từ 4,5 xuống 2,5; `L10-505` từ 2 xuống 1,5. Phân bổ dự kiến (phút trang cũ theo bảng trang của `storyboard.md`; storyboard chốt):

| mạch | trang | số trang | phút | đổi |
|---|---|---:|---:|---|
| 1 | `L10-101`–`L10-110`, thêm `L10-104b` | 11 | 12 | `L10-104b` lấy phút từ `L10-104` |
| 2 | `L10-200`–`L10-216` | 18 | 22,5 | `L10-205` −0,5 |
| 3 | `L10-300`–`L10-309` | 10 | 14,5 | — |
| 4 | `L10-400`–`L10-414` | 16 | 20,5 | `L10-404`, `L10-409` −0,5 mỗi trang; `L10-414` −1 |
| 5 | `L10-500`–`L10-510` | 12 | 12 | `L10-505` −0,5; `L10-510` −1 |
| 6 | `L10-600`–`L10-620` | 23 | 22,5 | `L10-614`–`L10-618` −2; `L10-620` −1 |
| 7 (mới) | `L10-D00`–`L10-D18` | 19 | 22 | kế hoạch C2 |
| 8 | `L10-700`–`L10-710`, thêm `L10-702c` (và `L10-703b` nếu cần) | 13–14 | 9 | `L10-706` −1; bảng mở rộng +1 |
| **Tổng** | | **122–123** | **135** | |

Số trang 120–123 theo kế hoạch C4 (101 + 19 + tối đa ba trang tách); bảng trên tính cả `L10-104b` và `L10-702c`, nên 122, thêm `L10-703b` thì 123. Mạch 7 có 19 trang, $0{,}5+1+1{,}5+1+1+1{,}5+1{,}5+1+1{,}5+1{,}5+1+1{,}5+1{,}5+1{,}5+1+1{,}5+1+1+1=22$ phút (kế hoạch C2).
