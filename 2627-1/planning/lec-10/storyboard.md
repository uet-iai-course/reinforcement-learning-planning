# Storyboard Bài 10

## Hành trình khái niệm và thời lượng

Các khoảng thời gian dưới đây không chồng lặp. Tuyến cốt lõi dùng 110 phút; hai phần linh hoạt dùng 10 phút; ba bài tập dọc dùng 30 phút riêng.

| cụm | chu trình | trang | đầu vào → sản phẩm | cốt lõi | linh hoạt |
|---|---|---|---|---:|---:|
| Cầu nối và REINFORCE | vấn đề chung → quy ước → cầu nối | `L10-01`–`L10-05` | Bài 09 → score đúng tại $\theta_{\mathrm{old}}$ | 12 phút | 0 |
| Baseline và actor–critic | vấn đề → trực giác → ví dụ/hình thức → ứng dụng → kiểm tra | `L10-06`–`L10-09`, `X01` | REINFORCE → baseline đúng và ranh giới bootstrap | 11 phút | 0 |
| GAE | trực giác/vấn đề → hình thức → ví dụ/ứng dụng → kiểm tra | `L10-10`–`L10-12`, `X01` | TD residual → lợi thế thô qua terminal và truncation ngoại sinh | 12 phút | 5 phút tại `L10-10` |
| TRPO | vấn đề → trực giác → ví dụ → hình thức → thuật toán → ứng dụng/kiểm tra | `L10-13`–`L10-20`, `X02` | dữ liệu cũ → bước natural gradient có kiểm surrogate và KL | 25 phút | 0 |
| PPO-Clip và loss | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L10-21`–`L10-28` | tỷ số $w_t$ → lợi thế actor, target critic và loss | 25 phút | 5 phút tại `L10-28` |
| PPO thực hành | vấn đề → cơ chế → ứng dụng → kiểm tra | `L10-29`–`L10-35`, `X03` | batch on-policy → schema, chẩn đoán và kiểm toán | 14 phút | 0 |
| So sánh, lý thuyết và tổng kết | so sánh → mô hình → kết quả có điều kiện → tổng hợp | `L10-36`, `L10-37`, `L10-37B`, `L10-38` | thuật toán thực hành → kết luận có phạm vi | 11 phút | 0 |

`X01`, `X02`, `X03` dùng lần lượt 10, 8 và 12 phút. `X01` là trang nối chung hai cụm baseline–actor–critic và GAE, nên xuất hiện ở cả hai hàng nhưng chỉ tính 10 phút một lần. Các nhãn linh hoạt chỉ tồn tại trong planning; không hiển thị trên trang chiếu hoặc trong ghi chú diễn giả.

## Truyền dữ kiện

- Mục tiêu $J=\mathbb E[G_0]$ ở `L10-04` quyết định hệ số $\gamma^t$ và điểm đánh giá score ở `L10-05`–`L10-06`.
- Bernoulli $p=0{,}25$ và baseline $b=4$ đi từ `L10-07` sang `X01`.
- Hai mặt nạ $(m_t,c_t)$ ở `L10-11` được dùng trong hai ca số ở `L10-12` và `X01`.
- Hai mẫu $(\widehat A^{\mathrm{raw}},w)$ ở `L10-15` chuẩn bị cho surrogate và bài toán TRPO ở `L10-16`.
- $F=\operatorname{diag}(4,1)$, $g=(2,1)$, $\delta=0{,}01$ đi từ `L10-18` sang `X02`.
- Tỷ số $w_t$ và lợi thế đóng băng đi từ `L10-15` qua TRPO, PPO và pipeline.
- Hai ca $\widehat A^{\mathrm{actor}}$ bị chặn ở `L10-23` được khái quát thành công thức ở `L10-24` và bảng trong/ngoài dải ở `L10-25`.
- `L10-27` truyền $\widehat A^{\mathrm{raw}}$ sang hai nhánh: chuẩn hóa thành $\widehat A^{\mathrm{actor}}$ và cộng $V_{\mathrm{old}}$ thành target $\widehat V$.
- $T$ ký hiệu thời điểm episode kết thúc; kích thước $[H,N,\cdot]$ và $B=HN$ ở `L10-28` đi vào schema, minibatch và bài kiểm toán `X03`.

## Ánh xạ topic – slide

Phân nhóm chủ đề: cốt lõi gồm 01, 03–09; cầu nối gồm 02; bổ sung gồm 10–11; đọc thêm gồm 12. Chủ đề 02 nối vấn đề phương sai của REINFORCE với TD/GAE; chủ đề 10 nối mục tiêu với cấu hình triển khai; chủ đề 11 giới hạn kết quả lý thuyết của PPO-Clip.

Bảng ánh xạ hai chiều giữa 12 topic ghi chú và 42 section slide (đồng bộ `data-note-topic-id` trong deck):

| topic | slide |
|---|---|
| `lec-10-topic-01` | `L10-01`, `L10-02`, `L10-03`, `L10-04`, `L10-05` |
| `lec-10-topic-02` | `L10-06`, `L10-07`, `L10-08`, `L10-09` |
| `lec-10-topic-03` | `L10-10`, `L10-11`, `L10-12`, `X01` |
| `lec-10-topic-04` | `L10-13`, `L10-14`, `L10-15`, `L10-16` |
| `lec-10-topic-05` | `L10-17`, `L10-18`, `L10-19`, `L10-20`, `X02` |
| `lec-10-topic-06` | `L10-21`, `L10-22`, `L10-23`, `L10-24`, `L10-25`, `L10-26` |
| `lec-10-topic-07` | `L10-27` |
| `lec-10-topic-08` | `L10-28`, `L10-29`, `L10-30` |
| `lec-10-topic-09` | `L10-31`, `L10-32`, `X03`, `L10-36` |
| `lec-10-topic-10` | `L10-33`, `L10-34`, `L10-35` |
| `lec-10-topic-11` | `L10-37`, `L10-37B` |
| `lec-10-topic-12` | `L10-38` |

Tổng: 12 topic ↔ 42 slide, mỗi slide thuộc đúng một topic.

## Quyết định cho các bước gộp

- `L10-03` chỉ nêu vấn đề chung về phân bố dữ liệu đổi; chu trình baseline bắt đầu từ phương sai của REINFORCE ở `L10-05`–`L10-06`.
- Baseline và actor–critic dùng chung vấn đề phương sai; `L10-08` tách rõ chỗ bootstrap bắt đầu.
- GAE dùng `L10-12` vừa là ví dụ vừa là ứng dụng vì hai ca tách terminal của MDP khỏi truncation ngoại sinh có quan sát cuối.
- PPO thực hành dùng chu trình rút gọn vì công thức đã hoàn thành ở cụm trước; kiểm tra tích hợp nằm ở `X03`, sau checklist tái lập `L10-35`.
- Phần lý thuyết tách mô hình vòng ngoài–vòng trong ở `L10-37` khỏi kết quả có điều kiện ở `L10-37B`; không suy rộng sang PPO thực hành với Adam và GAE.

## Từng trang chiếu

| mã | luận điểm trung tâm | bước | câu nối |
|---|---|---|---|
| `L10-01` | Bài nối lợi thế, miền tin cậy và cập nhật gần. | mở | Từ REINFORCE sang PPO. |
| `L10-02` | Bốn sản phẩm có thể kiểm tra. | định hướng | Bắt đầu từ dữ liệu đổi. |
| `L10-03` | Cập nhật chính sách làm phân bố dữ liệu đổi. | vấn đề chung | Khóa quy ước trước khi sửa tín hiệu và bước. |
| `L10-04` | Chỉ số reward, return và giá trị nhất quán với mục tiêu. | hình thức nền | Dùng quy ước đó cho REINFORCE. |
| `L10-05` | Score được đạo hàm theo $\theta$ rồi đánh giá tại $\theta_{\mathrm{old}}$. | cầu nối, vấn đề baseline | Giảm phương sai bằng baseline. |
| `L10-06` | Baseline loại phần return chung theo trạng thái. | trực giác, dự đoán | Kiểm tính không chệch. |
| `L10-07` | Chứng minh baseline bằng $b(s)\nabla\sum_a\pi(a\mid s)=0$; nêu điều kiện liên tục. | ví dụ, hình thức | So hai kiểu actor–critic. |
| `L10-08` | Actor–critic có thể học critic bằng đích Monte Carlo hoặc bootstrap. | so sánh, quy ước | Đưa critic cũ vào TD residual. |
| `L10-09` | $V_{\mathrm{old}}(S_t)$ và $V_{\mathrm{old}}(S_{t+1})$ tạo TD residual. | ứng dụng, thuật toán | Trộn nhiều tầm bằng GAE. |
| `L10-10` | $\lambda$ tạo lợi thế thô; $T$ và $H$ có vai trò khác nhau. | trực giác | Cần công thức hữu hạn đúng rollout. |
| `L10-11` | $m_t$ và $c_t$ tách terminal khỏi truncation ngoại sinh có quan sát cuối. | hình thức | Tính hai ca số. |
| `L10-12` | Episode kết thúc tại $T$ và rollout ngoại sinh dừng tại $H<T$ cho lợi thế thô khác nhau. | ví dụ, ứng dụng | Kiểm lại trong bài tập. |
| `X01` | Tính baseline và GAE qua hai ranh giới. | kiểm tra | Chuyển từ tín hiệu sang giới hạn bước. |
| `L10-13` | Surrogate mất độ tin cậy khi bước quá lớn. | vấn đề | Hình dung miền chỉ nên tin xấp xỉ. |
| `L10-14` | Ellipsoid Fisher biểu diễn miền tin cậy cục bộ. | trực giác | Dùng dữ liệu cũ để xét hướng. |
| `L10-15` | Hai mẫu cho thấy $w\widehat A$ thưởng đúng hướng thay đổi. | ví dụ | Khái quát bằng đẳng thức và surrogate. |
| `L10-16` | Identity dùng occupancy mới; xấp xỉ dùng occupancy cũ; bài toán dùng $\mathbb E_B$ và average-KL. | hình thức | Xấp xỉ cục bộ bài toán. |
| `L10-17` | $F$ là Hessian average-KL/kỳ vọng chính xác; $\widehat F$ là ước lượng Monte Carlo từ batch. | hình thức/thuật toán | Dùng ca hai chiều. |
| `L10-18` | Với $F$ SPD và $\eta=0$, bước $(0{,}05,0{,}1)$ chạm biên quadratic. | ví dụ số, ứng dụng | Mạng sâu cần hệ damped. |
| `L10-19` | CG giải $(\widehat F+\eta I)x=g$ SPD, có residual/max-iteration; FVP và line search quyết định chi phí. | thuật toán | Áp dụng tiêu chí nhận bước. |
| `L10-20` | Chỉ ứng viên tăng surrogate và thỏa KL mới được nhận. | ứng dụng, kiểm tra | PPO bỏ phép giải bậc hai. |
| `X02` | Giải và kiểm bước natural gradient. | kiểm tra | Mở PPO. |
| `L10-21` | PPO cần cập nhật gần bằng tối ưu bậc nhất. | vấn đề | Quan sát tỷ số quanh một. |
| `L10-22` | $w$ chỉ là tỷ số tại hành động mẫu; bằng một trước minibatch đầu. | trực giác | Tính hai mẫu đại diện. |
| `L10-23` | Hai lợi thế actor đại diện cho phía cải thiện bị chặn. | ví dụ | Khái quát phép tính. |
| `L10-24` | PPO-Clip dùng $\mathbb E_B$, một surrogate thực hành khác kỳ vọng chiết khấu. | hình thức | Xét trong và ngoài dải. |
| `L10-25` | Trong dải giữ surrogate; ngoài dải chỉ phía thuận lợi có đoạn phẳng. | ứng dụng | Kiểm giới hạn của clipping. |
| `L10-26` | Clipping không tạo hard-KL hay đơn điệu chung. | kiểm tra, giới hạn | Ghép các hạng loss. |
| `L10-27` | Actor dùng lợi thế chuẩn hóa; critic dùng target thô, tách gradient đúng đường. | thuật toán | Kiểm kích thước dữ liệu. |
| `L10-28` | Hành động rời rạc có shape $[H,N]\to[B]$; $V_{\mathrm{boot}}$ dùng quan sát cuối trước reset. | hình thức, ứng dụng | Đi vào pipeline. |
| `L10-29` | PPO tái dùng $B=HN$ mẫu và giữ `final_observation`; $w$ đổi theo tham số hiện tại. | cơ chế | Khóa đúng dữ kiện của batch. |
| `L10-30` | Schema tách đại lượng lưu, suy ra–đóng băng và tính lại; reset observation không dùng bootstrap. | hợp đồng | Theo dõi độ lệch bằng chẩn đoán. |
| `L10-31` | clipfrac đếm tỷ số ngoài dải, không đếm riêng đoạn phẳng; approxKL và EV có phép giảm rõ. | ứng dụng | Đọc cùng siêu tham số. |
| `L10-32` | $\epsilon$, epoch và learning rate tương tác. | ứng dụng | Tách biến thể value clipping. |
| `L10-33` | Value clipping là lựa chọn triển khai. | giới hạn | Mở các chi tiết còn lại. |
| `L10-34` | Tiền xử lý và khởi tạo đổi động lực học. | ứng dụng | Chuyển thành checklist. |
| `L10-35` | Báo cáo đầy đủ recipe mới cho phép tái lập. | tổng hợp thực hành | Kiểm toán một batch cụ thể. |
| `X03` | Tính $w=e^{0{,}2}$; kiểm shape rời rạc, bootstrap biên cuối và nghĩa đúng của clipfrac. | kiểm tra | So sánh cơ chế TRPO và PPO. |
| `L10-36` | TRPO và PPO kiểm soát bước bằng cơ chế khác nhau. | so sánh | Giới hạn kết luận lý thuyết. |
| `L10-37` | Mô hình lý thuyết tách vòng ngoài–vòng trong và Clip–Penalty. | hình thức lý thuyết | Nêu kết quả có điều kiện. |
| `L10-37B` | Định lý 3.1 chặn $\liminf\|\nabla V\|^2$ bằng sai lệch $\phi_n$ trong mô hình PPO-Clip lý tưởng. | kết luận, giới hạn | Chốt hợp đồng. |
| `L10-38` | Bốn hợp đồng nối công thức với triển khai. | tổng hợp | Kết thúc bài. |
