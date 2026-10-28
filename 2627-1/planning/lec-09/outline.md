# Dàn ý Bài 09: Double DQN và gradient chính sách

## Phạm vi (đợt sửa 2026-10-28)

- Nguồn chính: `RL-hk2-2025-2026/lecture09-ddqn-and-policy-gradient-part1.pdf`, 40 trang. Trang tiêu đề của nguồn ghi "Bài giảng 10: Policy Gradient"; tên tệp và vị trí trong học phần xác định đây là Bài 09, nên đầu ra dùng số 09.
- Không có tài liệu bài tập hay mã đi kèm nguồn. Bài thực hành của Bài 08 (mục 7 và mục 15) có số đo dùng được cho Double DQN; Bài 09 chưa có `exercises.md` và chưa có bài thực hành riêng.
- Đối tượng: sinh viên đã học MDP, chính sách, lợi tức và hàm giá trị (Bài 03), Q-learning dạng bảng (Bài 06), xấp xỉ hàm (Bài 07) và DQN (Bài 08).
- Đầu ra của đợt sửa 2026-10-28: 7 mạch, 120 phút trên lớp ($8+15+30+15+22+20+10$) và 30 phút chữa bài. Danh sách trang theo mạch nằm trong `storyboard.md`, mục "Đợt sửa 2026-10-28: bản đồ bảy mạch".

## Khung lý thuyết chung

- **Vấn đề trung tâm.** Ước lượng không chệch từ mẫu hai đại lượng dùng để cập nhật: giá trị của hành động được chọn trong mục tiêu bootstrap của DQN, và gradient của $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ theo tham số chính sách.
- **Đối tượng và ký hiệu chung.** MDP quan sát đầy đủ ($O_t=S_t$), $\mathcal A$ hữu hạn ở mạch 2–3, hữu hạn hoặc $\mathbb R$ ở mạch 4–6; $R_{t+1}$ nhận sau $A_t$; $\gamma\in[0,1)$; lượt kết thúc tại $T$; $\rho_0$, $P$; $G_t$, $q_\pi$; ước lượng có nhiễu $\widehat Q_a$; chính sách $\pi_\theta$; hàm điểm $\psi_\theta$.
- **Giả thiết chung.** Ước lượng khả tích; ở mạch 3, ước lượng đánh giá không chệch và độc lập với ước lượng chọn (Double Q-learning chỉ thỏa ở dạng lý tưởng vì mỗi bảng bootstrap từ bảng kia; Double DQN chỉ gần thỏa); ở mạch 5–6, $\pi_\theta$ khả vi và dương trên mẫu, $\rho_0$ và $P$ không phụ thuộc $\theta$, phần thưởng và độ dài lượt bị chặn, đổi được thứ tự đạo hàm và tích phân (điều kiện đủ: đặc trưng bị chặn, cho cả softmax và Gaussian có $\sigma^2$ cố định; không đòi hàm điểm bị chặn vì hàm điểm Gaussian không bị chặn theo $a$).
- **Chuỗi định nghĩa → kết quả → phương pháp.** Phép cực đại trên ước lượng không chệch có nhiễu → $\mathbb E[\max_a\widehat Q_a]\ge\max_a\mathbb E[\widehat Q_a]$ (Jensen) → bản đánh giá không chệch và độc lập với bản chọn thì không chệch lên → Double Q-learning, Double DQN (chỉ gần độc lập) → giới hạn của chính sách tham lam theo $Q$ → chính sách tham số hóa $\pi_\theta$ → hàm mục tiêu $J$ và sai phân hữu hạn → hàm điểm, $\nabla\pi=\pi\psi$ → định lý gradient chính sách $\nabla J=\mathbb E[\sum_t\gamma^tG_t\psi_t]$ → REINFORCE.
- **Giới hạn áp dụng.** Double DQN không loại hết tương quan giữa hai mạng; bộ ước lượng kép có thể chệch âm. REINFORCE không chệch dưới các giả thiết trên nhưng có phương sai lớn và học theo chính sách, không dùng lại bộ nhớ phát lại khi không hiệu chỉnh; phương sai được xử lý ở Bài 10.

## Mục tiêu học tập (đợt sửa 2026-10-28)

Mỗi mục tiêu ứng với một mạch từ 2 đến 6 và một sản phẩm kiểm được.

1. (Mạch 2) Tính độ chệch của phép cực đại trên các ước lượng không chệch có nhiễu; nêu khi nào hai vế của bất đẳng thức kỳ vọng bằng nhau. Sản phẩm: $\mathbb E[\max_a\widehat Q_a]=1/2$ với hai giá trị đúng bằng $0$, nhiễu $\pm1$ độc lập.
2. (Mạch 3) Tính mục tiêu DQN, mục tiêu Double DQN và một cập nhật Double Q-learning trên cùng mẫu chuyển; nêu vì sao mạng mục tiêu chỉ gần độc lập với mạng trực tuyến. Sản phẩm: $5{,}5$ và $4{,}6$ trên $Q_{\theta^-}(s',\cdot)=(5;\,4)$, $Q_\theta(s',\cdot)=(3;\,6)$; $Q_1(S,A)$ từ $4$ thành $4{,}06$.
3. (Mạch 4) Chọn họ phân phối của chính sách theo miền hành động; nêu bài toán mà chính sách ngẫu nhiên tốt hơn mọi chính sách tất định khi đặc trưng gộp trạng thái. Sản phẩm: so sánh trên lưới gộp trạng thái của nguồn (tr. 23–25).
4. (Mạch 5) Viết $J(\theta)$, ước lượng gradient bằng sai phân hữu hạn, tính hàm điểm softmax và Gaussian. Sản phẩm: $J=2$, sai phân $0{,}655$ so với $2/3$, $\psi_\theta(s,1)=(1/3;\,-1/3)$ trên bài toán một bước hai hành động.
5. (Mạch 6) Phát biểu định lý gradient chính sách với giả thiết; thực hiện một cập nhật REINFORCE. Sản phẩm: $\pi(1\mid s)$ từ $2/3$ lên $0{,}710$ với $\alpha=0{,}1$, $G_0=3$.

Mặt trang `L09-02` rút gọn năm mục này; ghi chú bài giảng giữ bản đầy đủ có sản phẩm.

## Bảy mạch (đợt sửa 2026-10-28)

HTML có đúng 7 section ngoài, độ sâu tối đa 2. Mạch $N$ mở tại `#/N`; từ mạch 2, trang đầu là trang tiêu đề mạch `L09-MNT`, `id="mach-N"` (tạo ở bước của mạch đó; sau C0 và bước mạch 1, các mạch 2–7 chưa có trang tiêu đề).

| mạch | tên (trang tiêu đề mạch) | dòng dẫn dự kiến (theo `CT-structure.md` §2.2, chốt ở bước của mạch) | phút |
|---|---|---|---:|
| 1 | Mở đầu (bìa là trang tiêu đề) | — | 8 |
| 2 | Độ chệch của phép cực đại (`L09-M2T`) | Muốn dùng phép cực đại trong mục tiêu bootstrap, phải biết nó lệch thế nào khi ước lượng có nhiễu. | 15 |
| 3 | Tách chọn và đánh giá (`L09-M3T`) | Muốn giảm độ chệch của phép cực đại, phải chọn hành động bằng một ước lượng và đánh giá bằng ước lượng khác. | 30 |
| 4 | Chính sách tham số hóa (`L09-M4T`) | Muốn chọn hành động liên tục hoặc ngẫu nhiên, phải học trực tiếp phân phối hành động $\pi_\theta$. | 15 |
| 5 | Hàm mục tiêu và hàm điểm (`L09-M5T`) | Muốn tăng $J(\theta)$ bằng bước gradient, phải tính được đạo hàm log xác suất của hành động đã lấy mẫu. | 22 |
| 6 | Gradient chính sách và REINFORCE (`L09-M6T`) | Muốn ước lượng gradient của $J$ từ các lượt đã thu, phải viết nó thành kỳ vọng theo quỹ đạo. | 20 |
| 7 | Tổng kết và chuyển tiếp (`L09-M7T`) | Muốn dùng đúng hai nhóm phương pháp, phải giữ các giả thiết của từng kết quả. | 10 |

Tên mạch 5 đổi từ "Mục tiêu và hàm điểm" (kế hoạch D1) thành "Hàm mục tiêu và hàm điểm": trong bài, "mục tiêu" là mục tiêu hồi quy $y_i$ (thuật ngữ Bài 08), còn $J(\theta)$ là hàm mục tiêu theo cách gọi của nguồn tr. 30.

Lời giải đầy đủ của các bài tập trên trang chiếu thuộc 30 phút chữa bài, ngoài 120 phút trên lớp.

## Bảng thuật ngữ Việt–Anh

Kế thừa bảng thuật ngữ của Bài 06–08 (`planning/lec-08/outline.md`). Lần đầu xuất hiện trong mỗi tài liệu (trang chiếu, ghi chú bài giảng), viết tên tiếng Việt kèm tên tiếng Anh trong ngoặc; các lần sau chỉ dùng tên tiếng Việt.

| Tiếng Việt | Tiếng Anh | Quy ước |
|---|---|---|
| lượt | episode | |
| lợi tức | return | không để "return" trần trên mặt trang |
| mẫu chuyển | transition | |
| mạng trực tuyến | online network | $Q_\theta$; không để "online" trần; tên tiếng Anh ở `L09-01c` |
| mạng mục tiêu | target network | $Q_{\theta^-}$; không để "target" trần |
| đồng bộ | hard target update | $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu |
| mục tiêu (mục tiêu hồi quy) | target (regression target) | $y_i$; không dùng "đích" (commit `4328758` của Bài 08) |
| mặt nạ kết thúc | terminal mask | $(1-Z_i)$ |
| kết thúc; cắt ngắn | termination; truncation | cờ $Z$; cờ $U$ |
| bộ nhớ phát lại | experience replay; replay buffer | không để "replay" trần |
| dừng gradient | stop-gradient | $\operatorname{sg}$ |
| hàm mất mát | loss | $L_B$ |
| mini-batch | mini-batch | giữ như Bài 08 |
| bootstrap, mục tiêu bootstrap | bootstrap, bootstrap target | giữ như Bài 07–08 |
| học khác chính sách; học theo chính sách | off-policy; on-policy learning | |
| độ chệch của phép cực đại | maximization bias | không dùng "sai lệch cực đại" |
| ước lượng không chệch | unbiased estimator | |
| học kép; bộ ước lượng kép | double learning; double estimator | Sutton và Barto (2018), §6.7 |
| Double Q-learning, Double DQN | Double Q-learning, Double DQN | tên thuật toán, giữ nguyên |
| chính sách tham số hóa | parameterized policy | $\pi_\theta$ |
| chính sách ngẫu nhiên; chính sách tất định | stochastic policy; deterministic policy | |
| gộp trạng thái | state aliasing | |
| phân phối phân loại | categorical distribution | $\operatorname{Cat}$ |
| chính sách softmax; chính sách Gaussian | softmax policy; Gaussian policy | |
| hàm mục tiêu | objective function | $J(\theta)$; khác "mục tiêu" $y_i$ |
| tăng gradient | gradient ascent | $\theta\leftarrow\theta+\alpha\widehat g$ |
| sai phân hữu hạn | finite difference | |
| hàm điểm | score function | $\psi_\theta=\nabla_\theta\log\pi_\theta$ |
| tỉ số xác suất | likelihood ratio | viết "tỉ số" như Bài 08, không "tỷ số" |
| quỹ đạo; lịch sử | trajectory; history | $\tau$; $H_t$ |
| lợi tức từ thời điểm $t$ | reward-to-go | $G_t$ |
| định lý gradient chính sách | policy gradient theorem | |
| phân bố chiếm dụng | (discounted) state occupancy measure | ký hiệu chốt ở bước mạch 6 |
| đường cơ sở | baseline | chỉ ở dòng nối Bài 10 |
| actor–critic | actor–critic | tên phương pháp, giữ nguyên |
| hầu chắc chắn | almost surely | không dùng "gần như chắc chắn" |
| vector | vector | không dùng "véc-tơ" |

## Ký hiệu (đợt sửa 2026-10-28)

Bảng ký hiệu đầy đủ (27 hàng, ba cột) nằm trong ghi chú bài giảng, mục "Bảng ký hiệu". Các quyết định ký hiệu của đợt sửa:

- MDP quan sát đầy đủ, viết $S_t$; Bài 08 viết $O_t$ (dòng "Ký hiệu:" của `L09-01b`).
- Giá trị hành động đúng viết $q_\pi$ như Bài 03–08 (Định nghĩa 03.16); chữ hoa $Q$ dành cho ước lượng ($Q_\theta$, $Q_{\theta^-}$, $Q_1$, $Q_2$, $\widehat Q_a$). Bản trước dùng $Q^\pi$ ở `L09-30`; đổi khi sửa trang đó.
- Hàm động lực viết $P(s',r\mid s,a)$; chữ $p$ dành cho $p_\theta(\tau)$. Bài 03 viết $p$.
- $\theta$ có hai vai: tham số mạng trực tuyến ở mạch 2–3, tham số chính sách ở mạch 4–7; hai vai không xuất hiện trong cùng một công thức. Ghi trong ghi chú bài giảng sau bảng ký hiệu.
- Tọa độ vector có dấu phẩy thập phân ngăn bằng dấu chấm phẩy, ví dụ $(1{,}5;\,3)$ (kế hoạch D4).
- Phân bố chiếm dụng: $\nu^\pi_\gamma$, viết gọn $\nu^\pi$ (quyết định của điều phối viên ở R1); không dùng $d$ (số chiều của $\theta$) hay $\mu$ (trung bình Gaussian). Đã ghi vào bảng ký hiệu của ghi chú bài giảng; áp dụng ở mạch 6.
- Bài 03 viết $\mu$ cho phân phối đầu và $p$ cho hàm động lực; bài này viết $\rho_0$, $P$. Tương ứng nêu một lần sau bảng ký hiệu của ghi chú bài giảng và trong ghi chú diễn giả `L09-01b`.
- Giá trị đúng của hành động $a$ tại một trạng thái viết $q_a$ (chữ thường); ước lượng viết $\widehat Q_a$. `L09-03`, `L09-04` sửa theo ở bước mạch 2.

## Khái niệm và nơi giới thiệu ở mạch 1 (danh sách kiểm Concept của `quill`)

| khái niệm | xuất hiện đầu trên mặt trang | định nghĩa hoặc nhắc lại | phụ thuộc |
|---|---|---|---|
| MDP quan sát đầy đủ, $O_t=S_t$ | `L09-01b` | `L09-01b`, dòng "Ký hiệu:" | Bài 03, Bài 08 |
| $\mathcal A$, $m$, $R_{t+1}$, $T$, $\rho_0$, $P$ | `L09-01b` | `L09-01b`, bảng | Bài 03 |
| $Z_i$, $U_i$, mẫu chuyển của mini-batch | `L09-01b` | `L09-01b`, bảng; `L09-01c` (cắt ngắn vẫn bootstrap) | Bài 08 |
| mục tiêu DQN $y_i$, $L_B$, $\operatorname{sg}$, đồng bộ $\theta^-$ | `L09-01c` | `L09-01c`, "Nhắc lại:" | Bài 08, Định nghĩa 08.3, 08.4, 08.12 |
| chính sách $\pi$, $\mathbb E_\pi$, $G_t$, $q_\pi$ | `L09-01d` | `L09-01d`, "Nhắc lại:" | Bài 03, Định nghĩa 03.9, 03.13, 03.16 |
| bất đẳng thức Jensen | `L09-01d` | `L09-01d`, "Nhắc lại:" | xác suất |
| hàm điểm (score function) | `L09-01` (tên) | `L09-02c` dòng 5 (công thức); định nghĩa đầy đủ ở mạch 5 | $\pi_\theta$ |
| $J(\theta)$, $\pi_\theta$ | `L09-02` (tên trong mục tiêu) | `L09-02c` (hộp bài toán, dòng 4) | $G_0$, $\mathbb E_\pi$ |
| $\widehat Q_a$, $q_a$ | `L09-02c` dòng 2 | tại chỗ ("mỗi $\widehat Q_a$ không chệch cho $q_a$"); ghi chú diễn giả và ghi chú bài giảng gọi $q_a$ là giá trị đúng | — |

## Bảng note-topic-id → data-slide-id (cập nhật ở bước mạch 1)

| note-topic-id | data-slide-id |
|---|---|
| `lec-09-topic-16` | `L09-01`, `L09-02`, `L09-02b`, `L09-02c` |
| `lec-09-topic-15` | `L09-01b`, `L09-01c`, `L09-01d` |
| `lec-09-topic-01` | `L09-M2T`, `L09-03` |
| `lec-09-topic-02` | `L09-04`, `L09-05`, `L09-06` |
| `lec-09-topic-17` | `L09-M3T`, `L09-06b`, `L09-06c` |
| `lec-09-topic-03` | `L09-07`, `L09-08`, `L09-09`, `X01` |
| `lec-09-topic-04` | `L09-10` |
| `lec-09-topic-05` | `L09-11`–`L09-15` |
| `lec-09-topic-06` | `L09-M4T`, `L09-16`, `L09-16b`, `L09-17`–`L09-19` |
| `lec-09-topic-07` | `L09-20`–`L09-22` |
| `lec-09-topic-08` | `L09-23`–`L09-25`, `X02` |
| `lec-09-topic-09` | `L09-26`, `L09-27` |
| `lec-09-topic-10` | `L09-28`, `L09-28A`, `L09-29` |
| `lec-09-topic-11` | `L09-30` |
| `lec-09-topic-12` | `L09-31`, `L09-32`, `X03` |
| `lec-09-topic-13` | `L09-33` |
| `lec-09-topic-14` | `L09-30A` |

Mạch 2–7 giữ `data-note-topic-id` cũ cho tới bước của mạch đó. Hai mã mới cho mạch 1 theo cách deck 08 làm (`lec-08-topic-13` cho tiên quyết, `lec-08-topic-17` cho mở đầu), vì trình xem từ chối mã chủ đề lặp và `lec-09-topic-01` thuộc về trang `L09-03` ở mạch 2. Tổng sau bước mạch 1: 43 `data-slide-id` duy nhất, 16 chủ đề; sau bước mạch 2: 44 (thêm `L09-M2T`); sau bước mạch 3: 46 (thêm `L09-M3T`, `L09-06b`); sau R3: 47 (thêm `L09-06c`); sau bước mạch 4: 49 (thêm `L09-M4T`, `L09-16b`), 17 chủ đề (thêm `lec-09-topic-17` Ước lượng kép; `L09-09` chuyển từ topic-04 sang topic-03 vì thành trang thuật toán).

## Phân bổ thời lượng (đợt sửa 2026-10-28)

$8+15+30+15+22+20+10=120$ phút trên lớp; 30 phút chữa bài ngoài 120 phút. Phân bổ trong mạch 1: bìa 1, ba trang Tiên quyết và quy ước 3, Mục tiêu học tập 1, Nội dung 1, Vấn đề trung tâm 2.

## Tài sản SVG

`central-problem.svg` (mới ở bước mạch 1, dùng trong ghi chú bài giảng, Mục 1); `cartpole-overestimate.svg` (mới ở bước mạch 2, `L09-03` và Ví dụ 09.1); `maximization-bias.svg` vẽ lại ở bước mạch 2 (`L09-05`, Ví dụ 09.2); `dqn-stability.svg` đã xóa ở bước R2 vì không còn trang nào dùng; mạch 4: `aliased-grid-stochastic.svg` (mới), `aliased-grid-policy.svg`, `policy-distributions.svg` (vẽ lại theo nguồn tr. 23–28); mạch 3: `double-estimator.svg`, `ddqn-example.svg`, `double-q-example.svg` (mới), `dqn-vs-ddqn.svg`, `double-q-cross-update.svg` (vẽ lại); `dqn-vs-ddqn.svg`, `double-q-cross-update.svg`, `aliased-grid-policy.svg`, `policy-distributions.svg`, `softmax-score.svg`, `reinforce-trajectory.svg` (bản trước, sửa ở bước của trang dùng).

## Bản trước đợt sửa 2026-10-28

Các mục dưới đây mô tả bản trước đợt sửa (sáu section ngoài, 38 trang). Mục nào sai khác với cấu trúc mới được thay khi sửa trang tương ứng.


### Phạm vi và mục tiêu

Nguồn chính: `RL-hk2-2025-2026/lecture09-ddqn-and-policy-gradient-part1.pdf`, 40 trang. Metadata trong trang tiêu đề ghi “Bài giảng 10: Policy Gradient”, còn tên tệp và vị trí học phần xác định đây là Bài 09; sai khác này được giữ trong nhật ký và tên đầu ra dùng số 09.

Đối tượng là sinh viên đại học đã biết Quy trình quyết định Markov, Q-learning, xấp xỉ hàm và DQN. Sau bài, sinh viên có thể:

1. giải thích và tính sai lệch cực đại;
2. viết đúng đích Double DQN có mặt nạ kết thúc và dừng gradient;
3. phân biệt Double DQN với Double Q-learning dạng bảng;
4. biểu diễn chính sách rời rạc hoặc liên tục như một phân phối hành động;
5. tính hàm điểm softmax và Gaussian có phương sai cố định;
6. truy dấu một bước REINFORCE theo mục tiêu episodic nhất quán.

Baseline và actor–critic chỉ được nhắc như cầu nối sang bài tiếp theo.

### Cấu trúc và thời lượng

| cụm | trang | phút cốt lõi | phút linh hoạt |
|---|---|---:|---:|
| Cầu nối DQN | `L09-01`–`L09-03` | 7 | 0 |
| Sai lệch cực đại và Double DQN | `L09-04`–`L09-10` | 25 | 0 |
| Double Q-learning | `L09-11`–`L09-15` | 11 | 5 |
| Chính sách là phân phối | `L09-16`–`L09-19` | 14 | 0 |
| Mục tiêu, giả thiết và hàm điểm | `L09-20`–`L09-27` | 27 | 5 |
| Định lý và REINFORCE | `L09-28`–`L09-33` (gồm `L09-28A`, `L09-30A`) | 26 | 0 |
| Tổng | 35 trang không mang mã X | 110 | 10 |

Tổng thời lượng chính là 120 phút (110 cốt lõi + 10 linh hoạt). `L09-30A` là trang đọc thêm ngoài tuyến chính, có thể lược, không cộng thêm phút cốt lõi; 35 trang không mang mã X gồm cả `L09-28A` và `L09-30A`.

Ba bài tập dọc `X01`, `X02`, `X03` dùng lần lượt 10, 8 và 12 phút, tổng 30 phút. 30 phút chữa bài tập nằm ngoài 120 phút chính, không tính là vượt giờ.

### Sáu mạch ngoài (section)

| mạch ngoài | range | chức năng |
|---|---|---|
| 1 | `L09-01`–`L09-03` | Cầu nối từ DQN và quy ước quan sát đầy đủ. |
| 2 | `L09-04`–`L09-10`, `X01` | Sai lệch cực đại, Double DQN và bài tập kiểm đích. |
| 3 | `L09-11`–`L09-15` | Double Q-learning dạng bảng và cập nhật chéo. |
| 4 | `L09-16`–`L09-19` | Chính sách trực tiếp, hai họ phân phối, hai giao diện. |
| 5 | `L09-20`–`L09-27`, `X02` | Mục tiêu episodic, giả thiết, hàm điểm softmax và Gaussian. |
| 6 | `L09-28`–`L09-33` (gồm `L09-28A`, `L09-30A`), `X03` | Tỷ số xác suất, nhân quả, phân bố chiếm dụng, REINFORCE; đọc thêm sai phân hữu hạn. |

Thứ tự vật lý trong section ngoài cuối là `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33`, khớp thứ tự `lec-09-topic-10` → `lec-09-topic-12` → `lec-09-topic-11` → `lec-09-topic-14` → `lec-09-topic-13`. Lý do đổi thứ tự: gom khối REINFORCE cốt lõi (`L09-31`, `L09-32`, `X03`) ngay sau khối định lý để giữ mạch chu trình học tập liên tục, rồi đặt phần mở rộng có thể lược (`L09-30`, `L09-30A`) trước trang tổng hợp `L09-33` để khi thiếu thời gian có thể lược cả hai trang mở rộng mà không phá chu trình.

Lý do thêm `L09-30A` “Đọc thêm: sai phân hữu hạn”: trang nguồn 33 về sai phân hữu hạn đã bị bỏ khỏi tuyến chính để nhường chỗ cho giả thiết đổi đạo hàm–tích phân. Bản đồng bộ khôi phục nội dung này như một trang đọc thêm ngoài tuyến chính, có thể lược, gồm một công thức xấp xỉ gradient và hai thẻ ưu điểm/giới hạn, nối từ hai cách viết gradient (`L09-29`, `L09-30`) sang cầu nối Bài 10. Không thêm ảnh.

Tổng mã: 35 trang không mang mã X + 3 bài tập = 38 mã.

### Bảng note-topic-id → data-slide-id

| note-topic-id | data-slide-id |
|---|---|
| `lec-09-topic-01` | `L09-01`, `L09-02`, `L09-03` |
| `lec-09-topic-02` | `L09-04`, `L09-05`, `L09-06` |
| `lec-09-topic-03` | `L09-07`, `L09-08`, `X01` |
| `lec-09-topic-04` | `L09-09`, `L09-10` |
| `lec-09-topic-05` | `L09-11`–`L09-15` |
| `lec-09-topic-06` | `L09-16`–`L09-19` |
| `lec-09-topic-07` | `L09-20`–`L09-22` |
| `lec-09-topic-08` | `L09-23`–`L09-25`, `X02` |
| `lec-09-topic-09` | `L09-26`, `L09-27` |
| `lec-09-topic-10` | `L09-28`, `L09-28A`, `L09-29` |
| `lec-09-topic-11` | `L09-30` |
| `lec-09-topic-12` | `L09-31`, `L09-32`, `X03` |
| `lec-09-topic-13` | `L09-33` |
| `lec-09-topic-14` | `L09-30A` |

Tổng: 38 `data-slide-id` duy nhất, 38 `data-note-topic-id`, đủ 14 topic và 6 section ngoài.

### Danh mục mã trang

Thứ tự vật lý: `L09-01`, `L09-02`, `L09-03`, `L09-04`, `L09-05`, `L09-06`, `L09-07`, `L09-08`, `X01`, `L09-09`, `L09-10`, `L09-11`, `L09-12`, `L09-13`, `L09-14`, `L09-15`, `L09-16`, `L09-17`, `L09-18`, `L09-19`, `L09-20`, `L09-21`, `L09-22`, `L09-23`, `L09-24`, `L09-25`, `X02`, `L09-26`, `L09-27`, `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33`.

Thứ tự logic theo topic: `L09-01`–`L09-08`, `X01`, `L09-09`–`L09-19`, `L09-20`–`L09-25`, `X02`, `L09-26`–`L09-27`, `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33`.

### Ánh xạ nguồn

| trang nguồn | quyết định | trang đích | lý do |
|---|---|---|---|
| 1–2 | sửa | `L09-01`–`L09-02` | Sửa số bài trong metadata; mục tiêu hóa nội dung. |
| 3–10 | gộp | `L09-03` | DQN đã được trình bày đầy đủ ở Bài 08; chỉ giữ cầu nối và quy ước $O=S$. |
| 11–13 | tách, sửa | `L09-04`–`L09-06`, `X01` | Thêm ví dụ Rademacher và điều kiện dấu nghiêm của Jensen; đặt bài tập sau hình thức Double DQN. |
| 14–16 | giữ, sửa | `L09-07`–`L09-09` | Dùng đích từng trường hợp để không lấy argmax ở terminal; định nghĩa dừng gradient, miền và kích thước lô. |
| 17–19 | gộp, sửa | `L09-10` | Hạ mức khẳng định, nêu tương quan online–target. |
| 20–21 | tách, sửa | `L09-11`–`L09-15` | Viết đích từng trường hợp để không lấy argmax tại terminal; nêu ví dụ và khác biệt với Double DQN. |
| 22–25 | giữ, sửa | `L09-16` | Nêu chính sách tối ưu tất định có thể tồn tại trong MDP quan sát đầy đủ; dùng khả vi, lấy mẫu và hành động liên tục làm động cơ. |
| 26–29 | tách, sửa | `L09-17`–`L09-19` | Đặt trực giác lấy mẫu trước hình thức; bỏ ký hiệu độ đo khỏi mặt trang; phân biệt rời rạc/liên tục. |
| 30–32 | tách, sửa | `L09-20`–`L09-21` | Chuẩn hóa chỉ số quỹ đạo, miền $0\le\gamma&lt;1$ và mục tiêu episodic. |
| 33 | bỏ, thay cầu nối | `L09-22` | Bỏ sai phân hữu hạn để công bố giả thiết đổi đạo hàm–tích phân, support, khả tích và tính Markov. |
| 34 | giữ, sửa | `L09-23` | Thêm điều kiện xác suất dương và support. |
| 35–36 | tách, thêm | `L09-24`–`L09-25`, `X02` | Viết chuẩn hóa softmax và ví dụ số đầy đủ. |
| 37–38 | tách, thêm | `L09-26`–`L09-27`, `X02` | Bổ sung hàm điểm Gaussian với phương sai cố định. |
| 39 | sửa, tách | `L09-28`, `L09-28A`, `L09-29`, `L09-30` | Viết $J=\int G_0p_\theta d\tau$ rồi $\nabla J=\mathbb E[G_0\nabla\log p]$; tách phân tích quỹ đạo thành `L09-28A`; dùng kỳ vọng có điều kiện theo lịch sử; nối trọng số $\gamma^t$ với phân bố chiếm dụng. |
| 40 | sửa, tách | `L09-31`–`L09-33`, `X03` | Thu dưới $\theta_{old}$; áp dụng một cập nhật softmax và kiểm lại xác suất hành động. |
| 33 (đọc thêm) | thêm | `L09-30A` | Khôi phục sai phân hữu hạn (đã bỏ khỏi tuyến chính ở nguồn 33) thành trang đọc thêm ngoài tuyến chính, có thể lược: một công thức xấp xỉ gradient, ưu điểm không cần đạo hàm giải tích, giới hạn nhiễu và chi phí đánh giá khi số tham số lớn; nguồn tr. 33, nối từ hai cách viết gradient sang cầu nối Bài 10. |

### Thuật ngữ và ký hiệu

#### Đối chiếu thuật ngữ Anh–Việt

| thuật ngữ Anh | cách dùng tiếng Việt trong bài |
|---|---|
| maximization bias | sai lệch cực đại; lần đầu ở `L09-04` |
| likelihood ratio | tỷ số xác suất; lần đầu ở `L09-28` |
| score function | hàm điểm; lần đầu ở `L09-23` |
| occupancy measure | phân bố chiếm dụng; lần đầu ở `L09-30` |
| finite difference | sai phân hữu hạn; chỉ ở trang đọc thêm `L09-30A`, có thể lược |
| reward-to-go | return từ thời điểm hiện về sau |

#### Bảng ký hiệu

| ký hiệu | nghĩa |
|---|---|
| $Q_\theta$, $Q_{\theta^-}$ | mạng online nhận gradient và mạng mục tiêu |
| $O=h(S)$ | quan sát từ trạng thái; trong bài dùng quan sát đầy đủ $O=S$ |
| $Z_i\in\{0,1\}$ | cờ kết thúc MDP cho mẫu $i$ |
| $\operatorname{sg}(u)$ | bằng $u$ ở lượt thuận, đạo hàm bằng $0$ |
| $Q_1,Q_2$ | hai bảng riêng của Double Q-learning |
| $\pi_\theta(a\mid s)$ | xác suất hoặc mật độ của hành động $a$ tại trạng thái $s$ |
| $\phi(s,a)$, $\phi(s)$, $\theta$ | các véc-tơ trong $\mathbb R^d$; $\phi$ được giữ cố định trong các đạo hàm của bài |
| $\psi_\theta(s,a)$ | hàm điểm $\nabla_\theta\log\pi_\theta(a\mid s)$ |
| $\tau$ | quỹ đạo episodic |
| $T$ | thời điểm kết thúc, hữu hạn gần như chắc chắn |
| $G_t$ | return chiết khấu từ thời điểm $t$ |
| $J(\theta)$ | kỳ vọng của $G_0$ từ $S_0\sim\rho_0$ |
| $d_{\rho_0,\gamma}^{\pi}$ | phân bố chiếm dụng trạng thái chiết khấu đã chuẩn hóa; episode được nối bằng trạng thái hấp thụ có $Q=0$ |
| $\theta_{old}$ | tham số cố định trong khi thu một episode |

### Tài sản SVG

`dqn-stability.svg`, `maximization-bias.svg`, `dqn-vs-ddqn.svg`, `double-q-cross-update.svg`, `aliased-grid-policy.svg`, `policy-distributions.svg`, `softmax-score.svg`, `reinforce-trajectory.svg`.
