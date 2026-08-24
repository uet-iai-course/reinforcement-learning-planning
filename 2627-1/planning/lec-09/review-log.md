# Nhật ký rà soát Bài 09

## Kiểm kê và sai khác nguồn

- Nguồn: `lecture09-ddqn-and-policy-gradient-part1.pdf`, 40 trang.
- Metadata nguồn ghi “Bài giảng 10: Policy Gradient”, trái với tên tệp và thứ tự học phần. Đầu ra dùng Bài 09; ghi nhận sai khác, không sao chép metadata sai.
- Trang 3–10 lặp DQN của Bài 08 nên gộp thành một cầu nối.
- Trang 12–13 mô tả xu hướng đánh giá cao nhưng không nêu Jensen và điều kiện dấu nghiêm; đã bổ sung ví dụ Rademacher và dấu $\ge$.
- Trang 15 thiếu mặt nạ kết thúc và dừng gradient; đã bổ sung.
- Trang 17–19 dùng kết luận mạnh về ổn định/chất lượng; đã chuyển thành cơ chế và giới hạn, nêu online–target còn tương quan.
- Trang 20–21 là Double Q-learning dạng bảng; đã tách khỏi Double DQN và thêm cập nhật terminal.
- Trang 26 ghi chính sách học phân phối trên trạng thái; đã sửa thành kernel phân phối hành động có điều kiện theo trạng thái.
- Trang 29 thiếu chuẩn hóa đầy đủ của softmax; đã viết tổng mẫu số.
- Trang 30 dùng chỉ số $s_1,r(s_1)$ không khớp quy ước chuyển tiếp; đã dùng $(S_t,A_t,R_{t+1})$ từ $t=0$.
- Trang 33 nói sai phân dùng cho chính sách bất kỳ; đã lược sau phản biện để dành chỗ cho giả thiết của đạo hàm chính sách.
- Trang 34 thiếu điều kiện xác suất dương và miền hỗ trợ; đã bổ sung.
- Trang 37–38 hỏi nhưng không cho hàm điểm Gaussian; đã bổ sung cho phương sai cố định.
- Trang 39 thiếu quy ước phân bố chiếm dụng; đã dùng dạng chiết khấu chuẩn hóa và hệ số $1/(1-\gamma)$.
- Trang 40 thiếu $\gamma^t$ theo mục tiêu $J=\mathbb E[G_0]$ và cập nhật tham số ngay trong episode; đã thu dưới $\theta_{old}$, cộng gradient rồi cập nhật một lần.
- Baseline và actor–critic chỉ ghi ở trang kết như nội dung bài tiếp theo.

## Sửa theo kiểm định storyboard

- `nghiêm trọng`: `X01` từng yêu cầu tính Double DQN trước khi công thức xuất hiện. Đã chuyển `X01` sau `L09-10`, nên bài kiểm tra đứng sau hình thức, ví dụ và giới hạn của thuật toán.
- `nghiêm trọng`: `L09-17` từng mở bằng ký hiệu kernel và `L09-28` từng nêu định lý trước suy diễn. Đã đặt trực giác lấy mẫu ở `L09-17`; ký hiệu độ đo chỉ còn trong ghi chú. Chuỗi mới là xác suất quỹ đạo `L09-28`, nhân quả/reward-to-go `L09-29`, rồi định lý occupancy `L09-30`.
- `nghiêm trọng`: mục tiêu episodic và occupancy vô hạn từng thiếu quy ước nối. Đã định nghĩa tiếp diễn hấp thụ sau $T$ với phần thưởng và $Q$ bằng không ở `L09-20`, rồi dùng đúng quy ước tại `L09-30`.
- `trung bình`: cầu nối từ Double DQN sang chính sách trực tiếp từng ngụ ý trộn hành động sửa được aliasing. `L09-16` nay tính rõ kỳ vọng $1/2$ trong ví dụ cân bằng, nêu trộn không tự sửa aliasing, và dùng khó khăn argmax trong miền hành động liên tục làm động cơ riêng.
- `trung bình`: chu trình Double Q-learning chưa gọi rõ bước ứng dụng. `L09-13` nay là ứng dụng số; storyboard ghi đây là chu trình rút gọn vì vấn đề chọn–đánh giá đã được thiết lập ở cụm trước.
- `trung bình`: các cụm thời lượng trong storyboard từng chồng lặp `L09-20`–`L09-27`. Đã tách thành năm cụm không chồng lặp, tổng đúng 110 phút cốt lõi, 10 phút linh hoạt và 30 phút bài tập.
- Sau đổi thứ tự, đã đồng bộ ánh xạ cho các trang bị ảnh hưởng và hai trang lân cận: `L09-04`–`L09-12`, `L09-14`–`L09-21`, `L09-26`–`L09-33` và ba trang bài tập.

## Rà soát số

- Rademacher: $(-1,-1)$ cho max $-1$; ba cặp còn lại cho max $1$; kỳ vọng $0,5$. SVG mới hiện đủ bốn kết quả và không dùng từ “luôn”.
- DQN: $1+0,9\max(5,4)=5,5$.
- Double DQN: online chọn hành động 2 từ $(3,6)$; target đánh giá 4; đích $4,6$.
- Double Q: $y_1=1+0,9(1)=1,9$; với $Q_1(S,A)=4$, $\alpha=0,1$, giá trị mới $3,79$.
- Softmax: $(1,0)-(2/3,1/3)=(1/3,-1/3)$.
- Gaussian: $(1,5-0)(1,2)=(1,5,3)$ khi $\sigma^2=1$.
- REINFORCE softmax: $\theta=(\log2,0)$, $G_0=3$, $\psi=(1/3,-1/3)$ cho $\widehat g=(1,-1)$; với $\alpha=0,1$, $\theta_{new}=(\log2+0,1,-0,1)$ và $\pi_{new}(1\mid s)\approx0,710$.

## Hợp nhất bốn báo cáo rà soát độc lập

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | `L09-04`–`L09-05` | Hình sai lệch ghi “luôn” trái ví dụ bốn kết quả. | Cặp $(-1,-1)$ cho cực đại $-1$. | Vẽ đủ bốn kết quả và ghi kết luận theo kỳ vọng. |
| nghiêm trọng | `L09-07`–`L09-09` | Chưa định nghĩa `sg`, còn lấy argmax trên terminal, thiếu miền và kích thước lô. | Công thức cũ dùng mặt nạ sau khi đã viết $a^*$ và trộn $O$ với $S$. | Dùng đích từng trường hợp, chuẩn hóa $O=S$, định nghĩa `sg`, miền $Q$ và dạng lô. |
| nghiêm trọng | `L09-16` | Hình aliasing có chữ tràn và ngụ ý trộn khôi phục quyết định. | Cùng biểu diễn phải tạo cùng phân phối dưới cùng chính sách. | Vẽ lại quan hệ cùng biểu diễn → cùng phân phối; nói rõ trộn không khôi phục trạng thái. |
| nghiêm trọng | `L09-28`–`L09-30` | Thiếu bước $\nabla J=\int G\nabla p=\mathbb E[G\nabla\log p]$ và dùng ngôn ngữ độc lập cho bước nhân quả. | Phần thưởng quá khứ được loại bằng kỳ vọng có điều kiện của hàm điểm, không phải độc lập. | Viết đủ tỷ số xác suất; định nghĩa lịch sử $H_t$ và dùng kỳ vọng lặp. |
| nghiêm trọng | `L09-22`, `L09-30` | Giả thiết định lý và định nghĩa $Q^\pi$ chưa đủ. | Cần $\rho_0,P$ độc lập $\theta$, support cố định, khả tích và xử lý chân trời. | Công bố giả thiết; định nghĩa $Q^\pi$ theo $G_t$; ghép thời gian vào trạng thái hoặc nối hấp thụ. |
| trung bình | `L09-16`–`L09-19` | Động cơ chính sách trực tiếp còn dựa quá nhiều vào aliasing; chuẩn hóa liên tục chỉ nằm trong ghi chú. | MDP quan sát đầy đủ có thể có chính sách tối ưu tất định. | Dùng phân phối khả vi, lấy mẫu và hành động liên tục làm động cơ; hiện cả tổng và tích phân chuẩn hóa. |
| trung bình | `L09-24`–`L09-27` | Thiếu miền của $\phi,\theta$ và kích thước hàm điểm. | Công thức dùng tích vô hướng nhưng không định kiểu. | Nêu $\phi,\theta\in\mathbb R^d$ và $\psi\in\mathbb R^d$. |
| trung bình | `L09-28`–`L09-31` | Cầu nối tỷ số xác suất bị xếp vào phần linh hoạt và liên hệ occupancy–ước lượng quỹ đạo chưa hiện. | Bỏ phần này làm định lý xuất hiện như công thức cần nhớ. | Đưa toàn bộ cầu nối vào tuyến cốt lõi; chỉ ra trọng số $\gamma^t$ tạo phân bố chiếm dụng. |
| trung bình | `L09-32`, `X03` | Ví dụ chỉ cộng vector, chưa áp dụng vào cùng chính sách softmax. | Không thấy tham số và xác suất hành động đổi ra sao. | Dùng lại đặc trưng softmax, tính $\theta_{new}$ và xác suất mới. |
| trung bình | toàn bài | Cỡ bảng và code sau nhân cỡ trang có thể dưới `0.75em`. | $0,82\times0,90=0,738$. | Tăng bảng lên `0.95em`, code lên `0.92em`. |

Tất cả đề xuất trên đã áp dụng. Sai phân hữu hạn ở nguồn trang 33 bị lược để dành thời gian cốt lõi cho giả thiết và suy diễn định lý. Không có đề xuất nghiêm trọng hoặc trung bình nào bị từ chối.

## Sửa ba vấn đề trung bình sau rà lại

- `L09-20`: đã khai báo $0\le\gamma&lt;1$ trước khi dùng tổng vô hạn và phân bố chiếm dụng.
- `L09-12`: đã chuyển đích Double Q-learning sang dạng từng trường hợp; chỉ định nghĩa $a^*$ khi $Z=0$.
- `L09-29`: đã viết kỳ vọng có điều kiện tổng quát theo $A_t\mid H_t$; ghi rõ tổng cho hành động rời rạc và tích phân cho hành động liên tục.
- Chỉnh nhẹ: $Z$ có kiểu Boolean thay vì gộp vào $\mathbb R^b$; $\pi_\theta(a\mid s)\ge0$ xuất hiện cùng điều kiện chuẩn hóa; $\phi$ được giữ cố định tại hai họ chính sách.

## Tài sản và ngoại lệ

Tám hình kỹ thuật được vẽ lại thành SVG trong `img/lec-09/`. Không dùng ảnh raster, tài nguyên mạng hoặc tài sản sinh bởi AI. Không có ngoại lệ cần người dùng duyệt.

## Kiểm định sau sửa storyboard

- Cấu trúc: 33 trang chính và 3 trang dọc; độ sâu `section` tối đa là hai.
- Có 36 mã duy nhất, 36 ghi chú diễn giả và đủ 36 mục tương ứng trong storyboard.
- Nội dung hiển thị không chứa mã nội bộ, phân tuyến hoặc thời lượng.
- KaTeX chế độ nghiêm đã đọc 158 biểu thức; không có lỗi cú pháp.
- Tám SVG hợp lệ theo bộ phân tích XML, có `role="img"`, `title`, `desc`; cỡ nhãn nhỏ nhất khai báo là 30 px. Hai SVG đã sửa được kết xuất bằng ImageMagick để kiểm chữ tràn, cắt nhãn và thông điệp.
- Mọi `src` là tệp cục bộ và trả HTTP 200 tại cổng 8765; không có ảnh raster hoặc URL mạng.
- Không có cỡ chữ CSS dưới `0.75em`; không phát hiện mẫu từ cấm trong kiểm tra `$no-ai-slop`.
- Chưa kiểm tra tràn trang bằng trình duyệt đồ họa; bước kiểm định trực quan cuối vẫn phải thực hiện hoặc ghi rõ giới hạn công cụ.

## Tái kiểm tra toán học và kiểm định cuối

- Tác tử rà soát toán học và thuật toán đã kiểm tra lại bản sửa cuối; không còn vấn đề từ mức `trung bình` trở lên.
- Máy chủ cục bộ trả HTTP 200 cho tệp HTML và cả tám SVG tại cổng 8765.
- `git diff --check` không phát hiện lỗi khoảng trắng.
- Bản HTML và bốn tệp quy trình đã được đưa vào Design Files của dự án Codex Slides và đối chiếu từng byte với tệp trong kho.
- Codex Slides Browser không khả dụng trong phiên này. Vì vậy chưa thể tuyên bố đã rà trực quan bằng Codex Slides; giới hạn còn lại là kiểm tra tràn, chồng lấn và khả năng đọc bằng trình duyệt đồ họa.
