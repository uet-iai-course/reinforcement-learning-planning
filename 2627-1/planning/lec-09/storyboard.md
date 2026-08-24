# Storyboard Bài 09

## Hành trình khái niệm

| cụm | chu trình | trang | đầu vào → sản phẩm | cốt lõi | linh hoạt |
|---|---|---|---|---:|---:|
| Cầu nối và sai lệch cực đại | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L09-01`–`L09-10`, `X01` | DQN → nhận dạng, tính và giảm liên hệ chọn–đánh giá | 32 phút | 0 |
| Hai ước lượng dạng bảng | chu trình rút gọn: trực giác → thuật toán → ứng dụng → so sánh → kiểm tra | `L09-11`–`L09-15` | Double DQN → Double Q-learning và cập nhật chéo | 11 phút | 5 phút |
| Chính sách trực tiếp | vấn đề → trực giác → ví dụ → hình thức → kiểm tra | `L09-16`–`L09-19` | giới hạn của aliasing và argmax liên tục → phân phối hành động | 14 phút | 0 |
| Mục tiêu và hàm điểm | vấn đề → trực giác → hình thức → ví dụ → ứng dụng → kiểm tra | `L09-20`–`L09-27`, `X02` | mục tiêu episodic → hàm điểm softmax và Gaussian | 27 phút | 5 phút |
| Gradient chính sách | hình thức → nhân quả → định lý → thuật toán → ứng dụng → kiểm tra | `L09-28`–`L09-33`, `X03` | tỷ số xác suất → reward-to-go → phân bố chiếm dụng → REINFORCE | 26 phút | 0 |

Các cột thời lượng không tính các trang `X`. Tuyến chính có 110 phút và phần linh hoạt có 10 phút, không chồng lặp cụm. Ba bài tập dọc có tổng 30 phút. Toàn bộ cầu nối tỷ số xác suất, nhân quả và phân bố chiếm dụng là cốt lõi. Phần linh hoạt gồm bảng so sánh ở `L09-14` và nhánh Gaussian ở `L09-26`–`L09-27`; sai phân hữu hạn đã bỏ.

## Truyền dữ kiện

- Ví dụ Rademacher từ `L09-05` đi vào `X01`; Jensen ở `L09-06` giải thích kết quả.
- Hai vector $Q_{\theta^-}=(5,4)$ và $Q_\theta=(3,6)$ đi từ bảng so sánh `L09-08` sang bài tập `X01`.
- Giao diện chọn–đánh giá ở `L09-07` được đối chiếu với cập nhật chéo ở `L09-11`–`L09-14`.
- Trực giác lấy mẫu ở `L09-17` và hai giao diện ở `L09-19` định kiểu cho softmax `L09-24` và Gaussian `L09-26`.
- Quy ước $(S_t,A_t,R_{t+1})$, $0\le\gamma&lt;1$ và $G_t$ ở `L09-20` được giữ nguyên trong định lý, ước lượng, thuật toán và bài tập.
- Hàm điểm ở `L09-23` đi qua hai ví dụ rồi thành nhân tử trong xác suất quỹ đạo `L09-28` và ước lượng `L09-31`.
- Đặc trưng softmax và xác suất $2/3$ đi từ `L09-25` đến cập nhật `L09-32`, rồi được tính lại ở `X03`.

## Chu trình trọng tâm

### Sai lệch cực đại và Double DQN

Vấn đề ở `L09-03`–`L09-04`; trực giác và ví dụ ở `L09-04`–`L09-05`; hình thức ở `L09-06`–`L09-07`; ứng dụng số và hợp đồng tensor ở `L09-08`–`L09-10`; kiểm tra ở `X01`, sau khi công thức Double DQN đã xuất hiện. `L09-10` chuyển nhẹ sang bài kiểm tra; `X01` mới chuyển sang hai bảng.

### Double Q-learning

Đây là chu trình rút gọn vì vấn đề chọn–đánh giá đã được thiết lập ở cụm trước. Trực giác ở `L09-11`; thuật toán ở `L09-12`; ứng dụng số ở `L09-13`; so sánh ở `L09-14`; kiểm tra ở `L09-15`. `L09-13` được đánh dấu rõ là ứng dụng, không chỉ là ví dụ số.

### Chính sách trực tiếp và hàm điểm

Vấn đề biểu diễn ở `L09-16`: chính sách tối ưu tất định có thể tồn tại trong MDP quan sát đầy đủ, còn chính sách trực tiếp cung cấp phân phối khả vi, lấy mẫu và hành động liên tục. Trực giác ở `L09-17`; ví dụ hai họ phân phối ở `L09-18`; hình thức và kiểm tra chuẩn hóa ở `L09-19`. Mục tiêu ở `L09-20`–`L09-21`; hợp đồng đạo hàm ở `L09-22`; hình thức hàm điểm ở `L09-23`, `L09-24`, `L09-26`; ví dụ ở `L09-25`, `L09-27`; kiểm tra ở `X02`.

### REINFORCE

Tỷ số xác suất ở `L09-28` viết đủ ba bước từ $\nabla J$ trước cầu nối nhân quả có điều kiện theo lịch sử ở `L09-29`. `L09-30` định nghĩa $Q^\pi$, xử lý chân trời qua trạng thái thời gian hoặc hấp thụ, rồi nối trọng số quỹ đạo với phân bố chiếm dụng. Thuật toán ở `L09-31`; ứng dụng softmax ở `L09-32`; kiểm tra ở `X03`; tổng hợp ở `L09-33`.

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
| `X01` | Tính max bias và hai đích sau khi đã có công thức. | kiểm tra | Sang hai bảng độc lập hơn. |
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
| `L09-28` | $\nabla J=\int G\nabla p=\mathbb E[G\nabla\log p]$. | hình thức | Dùng nhân quả. |
| `L09-29` | Kỳ vọng có điều kiện của hàm điểm bằng không cho tổng hoặc tích phân. | cầu nối nhân quả | Gom theo phân bố chiếm dụng. |
| `L09-30` | Trọng số $\gamma^t$ tạo phân bố chiếm dụng và nối $G_t$ với $Q^\pi$. | định lý | Thành ước lượng mẫu. |
| `L09-31` | Thu dưới $\theta_{old}$, cộng $\gamma^tG_t\psi_t$ rồi cập nhật. | thuật toán | Đi vào số. |
| `L09-32` | Cập nhật softmax tăng xác suất từ $2/3$ lên khoảng $0,710$. | ứng dụng | Kiểm cả tham số và xác suất. |
| `X03` | Tính tham số, xác suất mới và hướng đổi khi return âm. | kiểm tra | Chốt hợp đồng. |
| `L09-33` | Ba hợp đồng kết thúc bài. | tổng hợp | Cầu nối baseline và actor–critic. |
