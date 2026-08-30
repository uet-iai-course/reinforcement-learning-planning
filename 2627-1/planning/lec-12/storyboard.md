# Storyboard Bài 12

## Bản đồ hành trình khái niệm

| cụm | chu trình | trang | đầu vào → sản phẩm | cốt lõi | linh hoạt |
|---|---|---|---|---:|---:|
| Định hướng | vị trí → mục tiêu | `L12-01`–`L12-03` | Bài 11 → câu hỏi mới của MARL | 6 | 0 |
| Trò chơi Markov và CTDE | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L12-04`–`L12-12`, gồm `L12-07B`; kiểm tại `X01` | MDP → joint action, miền/kiểu, MDP cảm sinh, reward, Nash, CTDE | 25 | 0 |
| COMA | vấn đề → trực giác → ví dụ → hình thức → ứng dụng/giới hạn → kiểm tra | `L12-13`–`L12-17`, `X02` | policy gradient → baseline phản thực | 15 | 0 |
| VDN/QMIX | vấn đề → trực giác → ví dụ → hình thức → thuật toán → ứng dụng/giới hạn → kiểm tra | `L12-18`–`L12-22B`; kiểm tại `X02` | action-value → IGM, mixer đơn điệu và bước TD từ replay | 15 | 0 |
| Actor–critic đa tác tử | cầu nối → vấn đề → hình thức → so sánh → thuật toán → giới hạn/kiểm tra | `L12-23`–`L12-28`, `X02` | DDPG/PPO → MADDPG, IPPO/MAPPO, HAPPO/HATRPO | 18 | 0 |
| Benchmark và framework | vấn đề → ví dụ → phạm vi bằng chứng → ứng dụng → kiểm tra | cốt lõi `L12-29`–`L12-34`; linh hoạt `L12-35`–`L12-37`; `X03` | hợp đồng thuật toán → chọn task và tái lập | 19 | 6 |
| Giao tiếp | vấn đề/ví dụ → trực giác → taxonomy → cơ chế → ứng dụng/giới hạn → kiểm tra | cốt lõi `L12-38`–`L12-42`; linh hoạt `L12-43`–`L12-44`; `X03` | CTDE → message availability và threat model | 10 | 4 |
| Kết | tổng hợp | `L12-45` | toàn bài → checklist đọc phương pháp | 2 | 0 |
| Bài tập | kiểm tra tách riêng | `X01`–`X03` sau `L12-45` | ba cụm kiến thức → lời giải có thể chấm | 0 | 30 phút ngoài phần trình chiếu |

Tuyến cốt lõi 110 phút gồm 42 trang và dùng phím Phải tại `L12-34` (`#/5/6`) để sang `L12-38` (`#/6/1`), rồi tại `L12-42` (`#/6/5`) để sang `L12-45` (`#/7/1`). Năm trang linh hoạt không nằm trong tuyến cốt lõi: dùng phím Xuống qua `L12-35`–`L12-37` (`#/5/7`–`#/5/9`) thêm 6 phút và `L12-43`–`L12-44` (`#/6/6`–`#/6/7`) thêm 4 phút. Sau kết luận, dùng phím Xuống qua `X01`–`X03` tại `#/7/2`–`#/7/4`, lần lượt 8, 12 và 10 phút. Tổng có 47 trang chính và 3 trang bài tập trong bảy mạch ngoài.

## Dữ kiện truyền giữa các bước

- Kích thước $|\mathcal A|=\prod_i|\mathcal A_i|$ ở `L12-06` giải thích nhu cầu phân rã tại `L12-18`–`L12-22` và được kiểm ở `X01`.
- Bộ miền $\mathcal S$, $\mathcal O_i$, $\mathcal A_i$, kiểu kernel và $\Delta(\cdot)$ được khóa ở `L12-07`; chuỗi $\tau_{t,i}$, giả thiết $\pi_{-i}(\mathbf a_{-i}\mid s)=\prod_{j\ne i}\pi_j(a_j\mid s)$ cùng $P_i^{\pi_{-i}}$, $r_i^{\pi_{-i}}$ được khóa ở `L12-07B` rồi giữ cho các thuật toán sau.
- Phân tách training/execution ở `L12-10` được dùng lại tại `L12-11`, `L12-17`, `L12-23`–`L12-26` và `L12-38`–`L12-43`.
- Bảng số $(0{,}25,0{,}75)$ và $(2,6)$ đi từ `L12-15` sang công thức `L12-16` rồi `X02`.
- Local argmax ở VDN `L12-19` chuẩn bị ví dụ đơn điệu `L12-20`, quan hệ tập hợp IGM `L12-21`, giới hạn `L12-22` và bước online/target TD ở `L12-22B`.
- Ratio PPO theo agent ở `L12-25` tạo vấn đề policy lệch khỏi rollout tại `L12-27`; ví dụ $1{,}1\widehat A$ chuẩn bị objective clipped và recurrence $M_{m+1}=r_m^{\mathrm{new}}M_m$ ở `L12-28`, rồi `X02` kiểm cả clipping lẫn multiplier.
- Các trục benchmark `L12-29` được áp vào ca `L12-30`–`L12-33`, bằng chứng `L12-34` và checklist `L12-37`.
- Ví dụ robot kho và phân biệt CTDE/message ở `L12-38` truyền $(\tau_B,m_{A\to B})$ sang taxonomy `L12-39`, rồi tách topology `L12-40` khỏi quyết định gửi `L12-41` trước khi xét nội dung và đường actor/critic ở `L12-42`–`L12-44`.

## Câu nối giữa các cụm

1. `L12-03` → `L12-04`: nhiều policy làm thay đổi bài toán cảm sinh, nên cần khóa mô hình trước khi chọn thuật toán.
2. `L12-12` → `L12-13`: trong bốn thách thức, COMA xử lý trực tiếp gán công dưới reward chung.
3. `L12-17` → `L12-18`: COMA giữ joint critic; phân rã giá trị chọn một cấu trúc khác để thực thi tham lam cục bộ.
4. `L12-22B` → `L12-23`: sau bước TD cho value decomposition rời rạc, MADDPG nối sang action liên tục và mixed tasks.
5. `L12-28` → `L12-29`: objective đúng chưa đủ; benchmark quyết định điều kết quả có thể chứng minh.
6. Tuyến cốt lõi `L12-34` → `L12-38`; tuyến đủ `L12-34` → `L12-35`–`L12-37` → `L12-38`: benchmark mô tả kênh môi trường, còn communication MARL thêm kênh giữa các tác tử.
7. Tuyến cốt lõi `L12-42` → `L12-45`; tuyến đủ `L12-42` → `L12-43`–`L12-44` → `L12-45`: kết luận luôn đứng trước bài tập.
8. `L12-45` → `X01`–`X03`: sau khi chốt checklist, người học chuyển sang cụm chữa bài tập tách riêng.

## Từng trang

| mã | luận điểm trung tâm | bước | nguồn |
|---|---|---|---|
| `L12-01` | MARL thêm phụ thuộc giữa nhiều chính sách. | mở | 1–3 |
| `L12-02` | MARL kế thừa VI/PI, DQN và actor–critic. | tiên quyết | 2 |
| `L12-03` | Kết quả học tập chia thành viết/tính và phân tích. | định hướng | 3, 11 |
| `L12-04` | MDP cảm sinh đổi khi $\pi_{-i}$ đổi dù $P$ nền cố định. | vấn đề | 4–5 |
| `L12-05` | Một bộ chọn joint action loại không dừng do nhiều bộ học nhưng nhận không gian quyết định lớn. | trực giác | 4–5 |
| `L12-06` | Joint action tăng theo tích; ví dụ cho $24$. | ví dụ | 6 |
| `L12-07` | Trò chơi Markov khóa miền và kiểu của state, observation, action, kernel, reward và discount. | hình thức | 6 |
| `L12-07B` | Lịch sử $\tau_i$ xác định miền actor; tích policy giả định hành động độc lập có điều kiện theo state, còn công thức cảm sinh chỉ dùng tổng trong trường hợp rời rạc, quan sát đầy đủ, policy Markov. | hình thức, ứng dụng | 4–6 |
| `L12-08` | Nash là điều kiện lệch đơn phương; tối ưu chung suy ra Nash chỉ được khẳng định dưới common payoff. | hình thức, giới hạn | 7 |
| `L12-09` | Common, zero-sum và general-sum dùng ba hợp đồng reward khác nhau. | ứng dụng | 7, 9 |
| `L12-10` | CTDE tách thông tin tập trung khi học khỏi actor cục bộ khi chạy. | trực giác | 8, 48–50 |
| `L12-11` | Bảng tham chiếu tới trước tách VDN khỏi QMIX và chỉ ra thành phần tập trung/phân tán. | bản đồ ứng dụng | 8, 12–16 |
| `L12-12` | Gán công, quan sát, parameter sharing/agent ID và dị thể là bốn trục khó. | tổng hợp | 10, 45 |
| `L12-13` | Reward chung không cô lập đóng góp; giá trị $Q=6$ mở ví dụ COMA nhất quán. | vấn đề | 12 |
| `L12-14` | Counterfactual baseline chỉ thay $a_i$, giữ $\mathbf a_{-i}$. | trực giác | 12 |
| `L12-15` | Bảng số cho baseline $5$ và advantage $1$. | ví dụ | 12 |
| `L12-16` | COMA dùng baseline có trọng số policy và score gradient cục bộ. | hình thức | 12 |
| `L12-17` | Phép tổng hành động và centralized critic giới hạn COMA; câu hỏi kiểm độ lớn phép tổng. | ứng dụng, giới hạn, kiểm tra | 12 |
| `L12-18` | Joint $Q$ phải cho phép thực thi tham lam cục bộ. | vấn đề | 14 |
| `L12-19` | VDN là phép cộng các utility cục bộ. | trực giác, hình thức | 14 |
| `L12-20` | Các utility vô hướng $q_1,q_2$ minh họa điều kiện mixer đơn điệu, không thay kiến trúc QMIX. | ví dụ | 14 |
| `L12-21` | QMIX dùng đơn điệu để bảo đảm tích các tập local argmax nằm trong tập global argmax, kể cả khi hòa. | hình thức | 14 |
| `L12-22` | QMIX giàu hơn VDN nhưng không biểu diễn joint $Q$ giảm theo utility cục bộ; câu hỏi kiểm điều kiện. | ứng dụng, giới hạn, kiểm tra | 14 |
| `L12-22B` | QMIX lấy replay, chọn next action bằng utility online, đánh giá bằng utility target cùng target mixer và chỉ backprop qua số hạng dự đoán online. | thuật toán | 14, 39–40 |
| `L12-23` | MADDPG định nghĩa $x$, $m$, tham số online/target, deterministic chain rule và joint target action; phạm vi còn gồm mixed tasks. | cầu nối, hình thức | 13 |
| `L12-24` | IPPO/MAPPO khác miền của value learner; cụm PPO/HAPPO trong bài giới hạn ở cooperative common-return. | vấn đề, phạm vi | 15–17 |
| `L12-25` | MAPPO dùng $\pi_{\theta_i}$ và tỷ số theo đúng action/history của từng tác tử trên batch cũ. | hình thức | 16 |
| `L12-26` | Centralized value không đổi input actor khi chạy; câu hỏi kiểm actor/critic contract. | so sánh, ứng dụng, kiểm tra | 15 |
| `L12-27` | Cập nhật một actor làm joint policy lệch khỏi policy tạo rollout; tỷ số $1{,}1$ cho actor kế surrogate $1{,}1\widehat A$. | vấn đề, trực giác, ví dụ | 17–18 |
| `L12-28` | HAPPO clip ratio của tác tử hiện tại với $M_m$ cố định rồi truyền $M_{m+1}=r_m^{\mathrm{new}}M_m$; có kiểm tra tại chỗ. | thuật toán, hình thức, kiểm tra | 17–18 |
| `L12-29` | Benchmark là gói giả thiết về thông tin, quyết định và tín hiệu. | vấn đề | 19–38 |
| `L12-30` | MPE/LBF kiểm phối hợp nhỏ nhưng khác reward mode. | ví dụ | 20–22 |
| `L12-31` | RWARE/gridworld làm lộ partial observation và cấu hình reward. | ví dụ | 23–24 |
| `L12-32` | MAMuJoCo và SMAC khác nhau ở action geometry. | ví dụ | 25–28 |
| `L12-33` | Football/many-agent kiểm khả năng mở rộng trong phạm vi lịch sử. | ví dụ, giới hạn | 29–38 |
| `L12-34` | Đường cong thiếu protocol không đủ để xếp hạng; câu kiểm tra đóng cụm benchmark trên cả tuyến cốt lõi. | phạm vi bằng chứng, kiểm tra | 21, 26, 28, 31, 38, 40, 42, 46 |
| `L12-35` | Framework ghép thuật toán, environment và hạ tầng theo phiên bản. | ứng dụng | 39–46 |
| `L12-36` | Các lớp framework đều có thể làm đổi kết quả. | trực giác | 44 |
| `L12-37` | Tái lập cần pin cấu hình, seed, budget và aggregation; câu hỏi kiểm sự khác biệt wrapper/action mask. | kiểm tra quy trình | 39–46 |
| `L12-38` | Ví dụ robot kho cho thấy message có thể đổi input actor khi chạy, còn CTDE không mặc nhiên có message. | vấn đề, ví dụ, trực giác | 47–49 |
| `L12-39` | Năm trục đặc tả kênh, trong đó topology tách khỏi quyết định gửi. | phân loại, hình thức | 49 |
| `L12-40` | Topology áp vào ví dụ để xác định các cặp gửi–nhận hợp lệ trước khi policy chọn gửi. | cơ chế, ứng dụng | 50 |
| `L12-41` | Communication policy chọn có gửi và khi nào trên topology đã có. | thuật toán | 51 |
| `L12-42` | Message có thể mang experience, hidden state hoặc intent; câu kiểm tra phân biệt topology với policy gửi. | hình thức, kiểm tra | 52 |
| `L12-43` | Actor phụ thuộc message thì kênh phải tồn tại khi chạy. | ứng dụng | 53 |
| `L12-44` | Bandwidth, lỗi, privacy và attack cần threat model. | giới hạn | 54 |
| `L12-45` | Sáu phép kiểm hợp nhất mô hình, thuật toán và bằng chứng. | tổng hợp | 4–54 |
| `X01` | Tính joint action/reward/MDP cảm sinh và bác bỏ Nash bằng lệch đơn phương có lợi. | kiểm tra | 4–10 |
| `X02` | Tính COMA, target QMIX, hạng clipped/recurrence HAPPO và đọc MADDPG. | kiểm tra | 12–18 |
| `X03` | Chọn benchmark và kiểm giao tiếp/tái lập. | kiểm tra | 20–54 |

## Điều hướng RevealJS

| stack ngang | trang dọc | hash một-gốc | vai trò điều hướng |
|---:|---|---|---|
| 1 | `L12-01`–`L12-03` | `#/1/1`–`#/1/3` | mở và mục tiêu |
| 2 | `L12-04`–`L12-12`, gồm `L12-07B` | `#/2/1`–`#/2/10` | hợp đồng MARL |
| 3 | `L12-13`–`L12-22B` | `#/3/1`–`#/3/11` | COMA nối trực tiếp sang VDN/QMIX |
| 4 | `L12-23`–`L12-28` | `#/4/1`–`#/4/6` | actor–critic đa tác tử |
| 5 | `L12-29`–`L12-34`; đuôi linh hoạt `L12-35`–`L12-37` | `#/5/1`–`#/5/9` | tại `#/5/6`: Phải để cắt, Xuống để học phần linh hoạt |
| 6 | `L12-38`–`L12-42`; đuôi linh hoạt `L12-43`–`L12-44` | `#/6/1`–`#/6/7` | tại `#/6/5`: Phải để cắt, Xuống để học phần linh hoạt |
| 7 | `L12-45`, `X01`–`X03` | `#/7/1`–`#/7/4` | kết luận trước, rồi dùng Xuống để chữa bài tập |

## Sai khác có chủ ý

- Bổ sung ví dụ số ở `L12-06`, `L12-15`, `L12-20` và `X01`–`X03` bằng phép thế trực tiếp vào định nghĩa nguồn; không thêm kết quả thực nghiệm.
- Dời CTDE lên trước thuật toán để khóa miền thông tin trước COMA/QMIX/MADDPG/MAPPO.
- Đặt MADDPG sau QMIX như một cầu nối rút gọn từ Bài 11; không lặp toàn bộ DDPG.
- Thêm `L12-07B` để công thức MDP cảm sinh có miền và giả thiết đọc được; thêm `L12-22B` để kiến trúc QMIX nối tới một bước huấn luyện TD hoàn chỉnh.
- Đảo nội dung trong cặp `L12-27`–`L12-28` để vấn đề và trực giác tuần tự xuất hiện trước thủ tục; không đổi thứ tự mã trang hay phạm vi nguồn.
- Gộp 19 trang môi trường thành các trục chọn benchmark và ca đại diện; bỏ screenshot/plot thiếu dữ liệu gốc.
- Gộp framework thành ma trận và kiến trúc lớp; mọi nhận định về hỗ trợ được giới hạn theo tài liệu nguồn.
- Bỏ AutoGen khỏi mặt trang vì nó không mặc nhiên là MARL; ghi ranh giới trong ghi chú và nhật ký.
- Bổ sung ví dụ robot kho tại `L12-38` từ ngữ cảnh RWARE/grid trong nguồn để nối quan sát cục bộ với message khi thực thi; không thêm kết quả thực nghiệm.
- Đặt `X01`–`X03` sau `L12-45` trong mạch ngoài cuối; hai cụm linh hoạt là đuôi dọc để tuyến 110 phút dùng Phải và tuyến 120 phút dùng Xuống.

Danh mục 50 mã trang: `L12-01`, `L12-02`, `L12-03`, `L12-04`, `L12-05`, `L12-06`, `L12-07`, `L12-07B`, `L12-08`, `L12-09`, `L12-10`, `L12-11`, `L12-12`, `L12-13`, `L12-14`, `L12-15`, `L12-16`, `L12-17`, `L12-18`, `L12-19`, `L12-20`, `L12-21`, `L12-22`, `L12-22B`, `L12-23`, `L12-24`, `L12-25`, `L12-26`, `L12-27`, `L12-28`, `L12-29`, `L12-30`, `L12-31`, `L12-32`, `L12-33`, `L12-34`, `L12-35`, `L12-36`, `L12-37`, `L12-38`, `L12-39`, `L12-40`, `L12-41`, `L12-42`, `L12-43`, `L12-44`, `L12-45`, `X01`, `X02`, `X03`.
