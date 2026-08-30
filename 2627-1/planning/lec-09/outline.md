# Dàn ý Bài 09: Double DQN và gradient chính sách

## Phạm vi và mục tiêu

Nguồn chính: `RL-hk2-2025-2026/lecture09-ddqn-and-policy-gradient-part1.pdf`, 40 trang. Metadata trong trang tiêu đề ghi “Bài giảng 10: Policy Gradient”, còn tên tệp và vị trí học phần xác định đây là Bài 09; sai khác này được giữ trong nhật ký và tên đầu ra dùng số 09.

Đối tượng là sinh viên đại học đã biết Quy trình quyết định Markov, Q-learning, xấp xỉ hàm và DQN. Sau bài, sinh viên có thể:

1. giải thích và tính sai lệch cực đại;
2. viết đúng đích Double DQN có mặt nạ kết thúc và dừng gradient;
3. phân biệt Double DQN với Double Q-learning dạng bảng;
4. biểu diễn chính sách rời rạc hoặc liên tục như một phân phối hành động;
5. tính hàm điểm softmax và Gaussian có phương sai cố định;
6. truy dấu một bước REINFORCE theo mục tiêu episodic nhất quán.

Baseline và actor–critic chỉ được nhắc như cầu nối sang bài tiếp theo.

## Cấu trúc và thời lượng

| cụm | trang | phút cốt lõi | phút linh hoạt |
|---|---|---:|---:|
| Cầu nối DQN | `L09-01`–`L09-03` | 7 | 0 |
| Sai lệch cực đại và Double DQN | `L09-04`–`L09-10` | 25 | 0 |
| Double Q-learning | `L09-11`–`L09-15` | 11 | 5 |
| Chính sách là phân phối | `L09-16`–`L09-19` | 14 | 0 |
| Mục tiêu, giả thiết và hàm điểm | `L09-20`–`L09-27` | 27 | 5 |
| Định lý và REINFORCE | `L09-28`–`L09-33` (gồm `L09-28A`) | 26 | 0 |
| Tổng | 34 trang chính | 110 | 10 |

Ba bài tập dọc `X01`, `X02`, `X03` dùng lần lượt 10, 8 và 12 phút, tổng 30 phút. Tổng thời lượng chính là 120 phút (110 cốt lõi + 10 linh hoạt); 30 phút chữa bài tập nằm ngoài 120 phút chính, không tính là vượt giờ.

## Sáu mạch ngoài (section)

| mạch ngoài | range | chức năng |
|---|---|---|
| 1 | `L09-01`–`L09-03` | Cầu nối từ DQN và quy ước quan sát đầy đủ. |
| 2 | `L09-04`–`L09-10`, `X01` | Sai lệch cực đại, Double DQN và bài tập kiểm đích. |
| 3 | `L09-11`–`L09-15` | Double Q-learning dạng bảng và cập nhật chéo. |
| 4 | `L09-16`–`L09-19` | Chính sách trực tiếp, hai họ phân phối, hai giao diện. |
| 5 | `L09-20`–`L09-27`, `X02` | Mục tiêu episodic, giả thiết, hàm điểm softmax và Gaussian. |
| 6 | `L09-28`–`L09-33` (gồm `L09-28A`), `X03` | Tỷ số xác suất, nhân quả, phân bố chiếm dụng, REINFORCE. |

Tổng mã: 34 trang chính + 3 bài tập = 37 mã.

## Danh mục mã trang

`L09-01`, `L09-02`, `L09-03`, `L09-04`, `L09-05`, `L09-06`, `L09-07`, `L09-08`, `L09-09`, `L09-10`, `X01`, `L09-11`, `L09-12`, `L09-13`, `L09-14`, `L09-15`, `L09-16`, `L09-17`, `L09-18`, `L09-19`, `L09-20`, `L09-21`, `L09-22`, `L09-23`, `L09-24`, `L09-25`, `L09-26`, `L09-27`, `X02`, `L09-28`, `L09-28A`, `L09-29`, `L09-30`, `L09-31`, `L09-32`, `X03`, `L09-33`.

## Ánh xạ nguồn

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

## Thuật ngữ và ký hiệu

### Đối chiếu thuật ngữ Anh–Việt

| thuật ngữ Anh | cách dùng tiếng Việt trong bài |
|---|---|
| maximization bias | sai lệch cực đại; lần đầu ở `L09-04` |
| likelihood ratio | tỷ số xác suất; lần đầu ở `L09-28` |
| score function | hàm điểm; lần đầu ở `L09-23` |
| occupancy measure | phân bố chiếm dụng; lần đầu ở `L09-30` |
| reward-to-go | return từ thời điểm hiện về sau |

### Bảng ký hiệu

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

## Tài sản SVG

`dqn-stability.svg`, `maximization-bias.svg`, `dqn-vs-ddqn.svg`, `double-q-cross-update.svg`, `aliased-grid-policy.svg`, `policy-distributions.svg`, `softmax-score.svg`, `reinforce-trajectory.svg`.
