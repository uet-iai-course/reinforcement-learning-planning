# Storyboard Bài 09

## Hành trình khái niệm

| cụm | chu trình | trang | đầu vào → sản phẩm | cốt lõi | linh hoạt |
|---|---|---|---|---:|---:|
| Cầu nối và sai lệch cực đại | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L09-01`–`L09-10`, `X01` | DQN → nhận dạng, tính và giảm liên hệ chọn–đánh giá | 32 phút | 0 |
| Hai ước lượng dạng bảng | chu trình rút gọn: trực giác → thuật toán → ứng dụng → so sánh → kiểm tra | `L09-11`–`L09-15` | Double DQN → Double Q-learning và cập nhật chéo | 11 phút | 5 phút |
| Chính sách trực tiếp | vấn đề → trực giác → ví dụ → hình thức → kiểm tra | `L09-16`–`L09-19` | giới hạn của aliasing và argmax liên tục → phân phối hành động | 14 phút | 0 |
| Mục tiêu và hàm điểm | vấn đề → trực giác → hình thức → ví dụ → ứng dụng → kiểm tra | `L09-20`–`L09-27`, `X02` | mục tiêu episodic → hàm điểm softmax và Gaussian | 27 phút | 5 phút |
| Gradient chính sách | hình thức → nhân quả → định lý → thuật toán → ứng dụng → kiểm tra | `L09-28`–`L09-33`, `X03` (gồm `L09-28A`, `L09-30A`) | tỷ số xác suất → reward-to-go → phân bố chiếm dụng → REINFORCE | 26 phút | 0 |

## Bản đồ sáu mạch ngoài

| mạch | range | chức năng | kết nối vào | đầu ra |
|---|---|---|---|---|
| 1 | `L09-01`–`L09-03` | Cầu nối từ DQN; quy ước $O=S$. | Bài 08 về DQN | Vấn đề sai lệch cực đại cho mạch 2. |
| 2 | `L09-04`–`L09-10`, `X01` | Nhận dạng, tính và giảm sai lệch cực đại. | Cơ chế còn thiếu ở mạch 1 | Nguyên tắc tách chọn–đánh giá cho mạch 3. |
| 3 | `L09-11`–`L09-15` | Double Q-learning dạng bảng, cập nhật chéo. | Nguyên tắc tách ở mạch 2 | Giới hạn argmax mở đường cho mạch 4. |
| 4 | `L09-16`–`L09-19` | Chính sách là phân phối; hai giao diện softmax/Gaussian. | Giới hạn argmax ở mạch 3 | Giao diện lấy mẫu khả vi cho mạch 5. |
| 5 | `L09-20`–`L09-27`, `X02` | Mục tiêu episodic, giả thiết, hàm điểm. | Giao diện chính sách ở mạch 4 | Hàm điểm softmax và Gaussian cho mạch 6. |
| 6 | `L09-28`–`L09-33` (gồm `L09-28A`, `L09-30A`), `X03` | Tỷ số xác suất, nhân quả, phân bố chiếm dụng, REINFORCE; đọc thêm sai phân hữu hạn. | Hàm điểm ở mạch 5 | Bốn hợp đồng kết bài và cầu nối sang Bài 10. |

Thứ tự vật lý trong mạch 6 là `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33` (thứ tự `lec-09-topic-10` → `lec-09-topic-12` → `lec-09-topic-11` → `lec-09-topic-14` → `lec-09-topic-13`). Lý do đổi thứ tự: giữ chu trình học tập REINFORCE (định lý → thuật toán → ứng dụng → kiểm tra) liền mạch trước khi vào phần mở rộng có thể lược, rồi chốt bằng trang tổng hợp `L09-33`.

Lý do thêm `L09-30A`: nội dung sai phân hữu hạn ở nguồn tr. 33 đã bị bỏ khỏi tuyến chính. Bản đồng bộ khôi phục thành trang “Đọc thêm: sai phân hữu hạn” ngoài tuyến chính, có thể lược, gồm một công thức xấp xỉ gradient và hai thẻ ưu điểm/giới hạn, nối từ hai cách viết gradient sang cầu nối Bài 10. Không thêm ảnh.

Tổng mã: 35 trang không mang mã X + 3 bài tập = 38 mã.

## Bảng note-topic-id → data-slide-id

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

Các cột thời lượng không tính các trang `X`. Tổng thời lượng vẫn 110 phút cốt lõi + 10 phút linh hoạt = 120 phút chính, cộng 30 phút chữa bài nằm ngoài 120 phút chính, không gọi là vượt giờ. Toàn bộ cầu nối tỷ số xác suất, nhân quả và phân bố chiếm dụng là cốt lõi, riêng `L09-30` và `L09-30A` là mở rộng có thể lược. Phần linh hoạt gồm bảng so sánh ở `L09-14` và nhánh Gaussian ở `L09-26`–`L09-27`; sai phân hữu hạn chỉ còn ở trang đọc thêm `L09-30A`.

## Truyền dữ kiện

- Ví dụ Rademacher từ `L09-05` đi vào `X01`; Jensen ở `L09-06` giải thích kết quả.
- Hai vector $Q_{\theta^-}=(2,7)$ và $Q_\theta=(4,1)$ đi từ bài tập `X01`; bộ số trên trang chiếu `L09-08` là $(5,4)$ và $(3,6)$, hai bộ khác nhau có chủ ý.
- Giao diện chọn–đánh giá ở `L09-07` được đối chiếu với cập nhật chéo ở `L09-11`–`L09-14`.
- Trực giác lấy mẫu ở `L09-17` và hai giao diện ở `L09-19` định kiểu cho softmax `L09-24` và Gaussian `L09-26`.
- Quy ước $(S_t,A_t,R_{t+1})$, $0\le\gamma&lt;1$ và $G_t$ ở `L09-20` được giữ nguyên trong định lý, ước lượng, thuật toán và bài tập.
- Hàm điểm ở `L09-23` đi qua hai ví dụ rồi thành nhân tử trong xác suất quỹ đạo `L09-28` và ước lượng `L09-31`.
- Đặc trưng softmax và xác suất $2/3$ đi từ `L09-25` đến cập nhật `L09-32`; `X03` đổi dấu return để kiểm một cập nhật mới, không chép lại đáp án.

## Chu trình trọng tâm

### Sai lệch cực đại và Double DQN

Vấn đề ở `L09-03`–`L09-04`; trực giác và ví dụ ở `L09-04`–`L09-05`; hình thức ở `L09-06`–`L09-07`; ví dụ số ở `L09-08`; kiểm tra ở `X01`; hợp đồng tensor ở `L09-09`; giới hạn ở `L09-10`, sau khi công thức Double DQN đã xuất hiện và bài tập đã kiểm cơ chế. `X01` kiểm cơ chế; `L09-10` chốt giới hạn rồi chuyển sang hai bảng.

### Double Q-learning

Đây là chu trình rút gọn vì vấn đề chọn–đánh giá đã được thiết lập ở cụm trước. Trực giác ở `L09-11`; thuật toán ở `L09-12`; ứng dụng số ở `L09-13`; so sánh ở `L09-14`; kiểm tra ở `L09-15`. `L09-13` được đánh dấu rõ là ứng dụng, không chỉ là ví dụ số.

### Chính sách trực tiếp và hàm điểm

Vấn đề biểu diễn ở `L09-16`: chính sách tối ưu tất định có thể tồn tại trong MDP quan sát đầy đủ, còn chính sách trực tiếp cung cấp phân phối khả vi, lấy mẫu và hành động liên tục. Trực giác ở `L09-17`; ví dụ hai họ phân phối ở `L09-18`; hình thức và kiểm tra chuẩn hóa ở `L09-19`. Mục tiêu ở `L09-20`–`L09-21`; hợp đồng đạo hàm ở `L09-22`; hình thức hàm điểm ở `L09-23`, `L09-24`, `L09-26`; ví dụ ở `L09-25`, `L09-27`; kiểm tra ở `X02`.

### REINFORCE

Tỷ số xác suất ở `L09-28` viết $J=\int G_0p_\theta d\tau$ rồi likelihood ratio; `L09-28A` tách phân tích quỹ đạo $p_\theta(\tau)=\rho_0\prod\pi_\theta P$ và $\nabla\log p=\sum_t\psi_t$, một luận điểm trung tâm nối sang `L09-29`. Hai trang lân cận quanh `L09-28A` đã rà: `L09-27` kết cụm hàm điểm, `L09-29` mở cầu nối nhân quả; ranh giới section 5→6 nằm giữa `X02` và `L09-28`. `L09-30` là phần mở rộng về phân bố chiếm dụng, có thể lược khi thiếu thời gian; `L09-30A` là trang đọc thêm sai phân hữu hạn, cũng có thể lược. Thuật toán ở `L09-31`; ứng dụng softmax ở `L09-32`; kiểm tra ở `X03`; tổng hợp ở `L09-33`. Thứ tự vật lý trong mạch 6 là `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33`: chu trình REINFORCE cốt lõi đi liền trước, phần mở rộng có thể lược nằm giữa `X03` và trang tổng hợp.

## Từng trang chiếu

| mã | luận điểm trung tâm | bước | câu nối |
|---|---|---|---|
| `L09-01` | Bài tách chọn–đánh giá rồi tối ưu chính sách. | mở | Nối từ DQN. |
| `L09-02` | Bốn kết quả kiểm chứng được. | định hướng | Chuyển vào cầu nối. |
| `L09-03` | Cơ chế ổn định DQN chưa sửa max bias. | vấn đề | Mở sai lệch. |
| `L09-04` | max chọn cả nhiễu thuận lợi. | trực giác | Dẫn tới ví dụ. |
| `L09-05` | Hai ước lượng không chệch tạo max lệch $0,5$. | ví dụ | Chuẩn bị Jensen. |
| `L09-06` | Jensen cho dấu không nghiêm. | hình thức | Cần tách hai vai trò. |
| `L09-07` | Online chọn, target đánh giá. | thuật toán | Đi vào ca số. |
| `L09-08` | DQN và DDQN cho 5,5 và 4,6. | ví dụ | Bổ sung hợp đồng. |
| `L09-09` | Miền, kích thước lô và đường gradient là một hợp đồng. | hình thức | Chốt thuật toán. |
| `L09-10` | Hai mạng sâu còn tương quan. | giới hạn | Kiểm lại cơ chế bằng số. |
| `X01` | Tính max bias và hai đích sau khi đã có công thức; bộ số mới $(2,7)$, $(4,1)$ cho $6{,}6$ và $2{,}6$. | kiểm tra | Sang hai bảng độc lập hơn. |
| `L09-11` | Double Q dùng cập nhật chéo. | trực giác | Viết công thức. |
| `L09-12` | Đích từng trường hợp chỉ lấy argmax khi không kết thúc. | thuật toán | Đi vào số. |
| `L09-13` | Áp dụng cập nhật cho $y=1,9$, $Q_1^{new}=3,79$. | ứng dụng | So sánh hai thuật toán. |
| `L09-14` | Double Q khác Double DQN. | so sánh | Kiểm hiểu. |
| `L09-15` | Bốn câu chốt học giá trị. | kiểm tra | Mở chính sách. |
| `L09-16` | Chính sách trực tiếp cho phân phối khả vi và miền liên tục; không sửa aliasing. | vấn đề, phạm vi | Xây giao diện lấy mẫu. |
| `L09-17` | Chính sách gán xác suất hoặc mật độ để lấy mẫu hành động. | trực giác | Chọn họ phân phối. |
| `L09-18` | Miền hành động quyết định họ phân phối. | ví dụ | So giao diện. |
| `L09-19` | Softmax và Gaussian có giao diện khác nhau. | hình thức, kiểm tra | Đặt mục tiêu học. |
| `L09-20` | $J$, $G_t$ và miền $0\le\gamma&lt;1$ dùng quy ước nhất quán. | vấn đề | Tối ưu theta. |
| `L09-21` | Gradient ascent tối ưu trực tiếp $J$. | hình thức | So với sai phân. |
| `L09-22` | Đạo hàm cần $\rho_0,P$ độc lập tham số, support cố định và khả tích. | giả thiết | Định nghĩa hàm điểm. |
| `L09-23` | Hàm điểm cần xác suất dương. | hình thức | Tính cho softmax. |
| `L09-24` | Hàm điểm softmax giữ $\phi$ cố định và nằm trong $\mathbb R^d$. | hình thức | Đi vào ví dụ. |
| `L09-25` | Hàm điểm chọn hành động 1 là $(1/3,-1/3)$. | ví dụ | Sang hành động liên tục. |
| `L09-26` | Hàm điểm Gaussian giữ $\phi,\sigma^2$ cố định và có kích thước $d$. | hình thức | Đi vào ví dụ. |
| `L09-27` | Hàm điểm Gaussian là $(1,5,3)$. | ví dụ | Kiểm hai họ. |
| `X02` | Tính hàm điểm và kiểm kỳ vọng bằng không. | kiểm tra | Sang tỷ số xác suất. |
| `L09-28` | $J=\int G_0p_\theta d\tau$ và $\nabla J=\mathbb E[G_0\nabla\log p]$. | hình thức | Tách phân tích quỹ đạo. |
| `L09-28A` | $p_\theta(\tau)=\rho_0\prod\pi_\theta P$ và $\nabla\log p=\sum_t\psi_t$. | hình thức | Dùng nhân quả. |
| `L09-29` | Kỳ vọng có điều kiện của hàm điểm bằng không cho tổng hoặc tích phân. | cầu nối nhân quả | Gom theo phân bố chiếm dụng. |
| `L09-30` | Mở rộng: trọng số $\gamma^t$ tạo phân bố chiếm dụng và nối $G_t$ với $Q^\pi$; có thể lược. | định lý | Thành ước lượng mẫu. |
| `L09-31` | Thu dưới $\theta_{old}$, cộng $\gamma^tG_t\psi_t$ rồi cập nhật. | thuật toán | Đi vào số. |
| `L09-32` | Cập nhật softmax tăng xác suất từ $2/3$ lên khoảng $0,710$. | ứng dụng | Kiểm cả tham số và xác suất. |
| `X03` | Tính tham số, xác suất mới khi return âm và return hai bước; giữ $\theta_{old}$. | kiểm tra | Sang phần mở rộng. |
| `L09-30A` | Đọc thêm: sai phân hữu hạn, xấp xỉ $\partial J/\partial\theta_k\approx[J(\theta+\epsilon u_k)-J(\theta)]/\epsilon$; ưu điểm không cần đạo hàm giải tích, giới hạn nhiễu và chi phí đánh giá; có thể lược. | đọc thêm | Nối hai cách viết gradient sang cầu nối Bài 10. |
| `L09-33` | Bốn hợp đồng cần giữ: sai lệch cực đại, Double DQN, chính sách, REINFORCE. | tổng hợp | Cầu nối baseline và actor–critic. |
