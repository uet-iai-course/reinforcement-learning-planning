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

## Vòng hiện tại

Runtime: mọi vai (planner, source reader, storyboard reviewer và năm reviewer độc lập) đều dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.

### Planner

- Mức độ: `trung bình`.
- Trang: `L09-28`–`L09-30`, `X01`, `X03`, `L09-16`.
- Vấn đề: một slide `L09-28` gánh cả tỷ số xác suất lẫn khai triển $\nabla\log p$; X01 lặp số cũ; X03 trùng `L09-32`; cầu nối Double DQN → chính sách trực tiếp còn mỏng.
- Bằng chứng: storyboard cũ cho thấy `L09-28` quá dày; X03 trùng ví dụ cộng vector của `L09-32`.
- Quyết định: tách `L09-28` thành `L09-28` + `L09-28A` trong cùng section ngoài; đổi số X01 thành $r=1$, $\gamma=0{,}8$, $Q_{\theta^-}=(2,7)$, $Q_\theta=(4,1)$ (DQN $6{,}6$, DDQN $2{,}6$); đổi X03 sang $G_0=-3$, $\theta_{new}=(\log2-0{,}1,0{,}1)$, $\pi_{new}(1\mid s)\approx0{,}621$ và episode hai bước $R_1=1,R_2=2,\gamma=0{,}9$ cho $G_0=2{,}8$, $G_1=2$; thêm dòng cầu nối argmax → phân phối khả vi ở `L09-16`.

### Source reader

- Mức độ: `trung bình`.
- Trang: nguồn tr.39–40, `L09-30`, `L09-31`.
- Vấn đề: nguồn tr.40 dùng mục tiêu khác $J=E[G_0]$; occupancy cần thuật ngữ Anh lần đầu.
- Bằng chứng: đối chiếu trực tiếp tr.39–40 với quy ước $J=E[G_0]$ đã chốt.
- Quyết định: `L09-30` đổi tiêu đề “Mở rộng: phân bố chiếm dụng”, lần đầu kèm `occupancy measure`; `L09-31` notes ghi khác nguồn là sửa có chủ ý; không đưa metadata quy trình lên mặt slide.

### Storyboard reviewer

- Mức độ: `trung bình`.
- Trang: toàn storyboard, quanh `L09-28A` và ranh giới section.
- Vấn đề: cần bản đồ 6 mạch, cập nhật bảng cho `L09-28A`, X01/X03; `L09-30` phải đánh dấu là mở rộng có thể lược.
- Bằng chứng: bảng cũ chưa có `L09-28A`; tổng thời lượng phải giữ 110 cốt lõi + 10 linh hoạt + 30 chữa bài.
- Quyết định: cập nhật bản đồ và mọi bảng; rà hai trang lân cận quanh `L09-28A` và mọi ranh giới section; không ghi số phút trên mặt slide hay trong notes.

### Năm reviewer độc lập

| mức độ | trang chiếu | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L09-28` | Góc nhìn sinh viên: ba công thức dày trên một trang nhỏ. | Trang cũ đồng thời chứa likelihood ratio, tích xác suất quỹ đạo và tổng log-gradient. | Tách thành `L09-28` và `L09-28A`; giữ mỗi trang một luận điểm. |
| trung bình | `L09-13`, `L09-07`, `X01` | Chuyên gia Học tăng cường: quy ước chỉ số hành động cần rõ; điều kiện $Z_i=0$ đặt cạnh argmax dễ đọc nhầm; X01 lặp số cũ. | Ví dụ toán dùng hành động 1/2 trong khi tensor có thể đánh số từ 0; đáp án X01 trùng `L09-08`. | Ghi quy ước trong notes `L09-09`, sửa câu điều kiện `L09-07`, đổi X01 sang $6{,}6$ / $2{,}6$. |
| nhẹ | `L09-09`, `L09-29`, `L09-30` | Rà toán: không có lỗi; cần làm rõ vai trò phòng thủ của `sg` và hai bước suy diễn. | Mọi ví dụ, $\gamma^t$, occupancy và kích thước đều được tính lại đúng. | Giữ công thức; bổ sung dòng $G_0=G_{<t}+\gamma^tG_t$ và trực giác occupancy. |
| trung bình | `L09-29`, `L09-30` | Phản biện học thuật: cầu nối nhân quả và dạng occupancy thiếu bước trung gian hiển thị. | Kết quả đúng nhưng lập luận chủ yếu nằm trong notes. | Thêm phân rã return ở `L09-29`; đổi `L09-30` thành mở rộng có trực giác và có thể lược. |
| nhẹ | `L09-16`, `L09-33`, `X01`, `X03` | Kết nối và mạch viết: động cơ chuyển sang chính sách và thu hồi hook còn mờ; hai bài tập lặp ví dụ. | Cầu nối argmax chỉ ở notes; kết luận chưa nhắc sai lệch cực đại. | Thêm cầu nối trên `L09-16`, thu hồi phép max trên `L09-33`, đổi dữ kiện X01/X03. |

### Hai dương tính giả

- 120+30: một reviewer báo tổng thời lượng vượt 120 phút vì cộng cả 30 phút chữa X01–X03 vào giờ chính. Đây là dương tính giả: 120 phút chính = 110 cốt lõi + 10 linh hoạt; 30 phút chữa bài nằm ngoài 120 phút chính, không phải vượt giờ.
- Gợi ý thời lượng trong notes: một reviewer đề xuất ghi số phút từng cụm vào notes để dễ trình bài. Đây cũng là dương tính giả: quy ước hiện hành cấm mã nội bộ, phân tuyến và thời lượng trên mặt slide lẫn trong notes; đề xuất bị bác bỏ.

### Kết luận vòng

- Đã áp dụng: tách `L09-28`, thêm `L09-28A` (phân tích $p_\theta(\tau)=\rho_0\prod\pi_\theta P$ và $\nabla\log p=\sum_t\psi_t$; một luận điểm trung tâm, notes nối sang `L09-29`), sửa X01/X03, thêm cầu nối `L09-16`, các sửa thuật ngữ lần đầu (maximization bias ở `L09-04`, likelihood ratio ở `L09-28`, occupancy measure ở `L09-30`).
- Chưa tuyên bố render, HTTP, recheck hoặc Codex Slides cho vòng này; các bước kiểm định trực quan và tái kiểm còn phải thực hiện riêng.

## Tài sản và ngoại lệ

Tám hình kỹ thuật được vẽ lại thành SVG trong `img/lec-09/`. Không dùng ảnh raster, tài nguyên mạng hoặc tài sản sinh bởi AI. Không có ngoại lệ cần người dùng duyệt.

## Kiểm định sau sửa storyboard

- Cấu trúc cuối: 34 trang chính và 3 trang bài tập, tổng 37 mã duy nhất; 37 ghi chú diễn giả; 6 `section` ngoài và độ sâu `section` tối đa là hai.
- Mọi mã trang xuất hiện trong HTML, outline và storyboard; nội dung hiển thị không chứa mã nội bộ, phân tuyến hoặc thời lượng.
- Tám SVG hợp lệ, có `role="img"`, `title` và `desc`; mọi tham chiếu tài sản đều cục bộ. Không có ảnh raster, URL mạng hoặc đường dẫn hỏng.
- Hai reviewer tái kiểm độc lập chạy song song qua OpenRouter. Cả hai có `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`. Rà toán xác nhận lại X01, `L09-28`–`L09-32` và X03; rà mạch xác nhận đủ 6 mạch, mọi ranh giới và hai trang lân cận quanh `L09-28A`. Không còn lỗi từ mức `trung bình` trở lên.
- Các sửa nhẹ sau tái kiểm: viết tường minh lịch sử $H_t$, thêm câu dẫn vào `L09-28A`, đồng bộ cách ghi phạm vi và số trang. Gợi ý giải thích thêm chỉ số hành động/đẳng thức chiếm dụng được giữ trong ghi chú hoặc bác bỏ khi không cần cho tính đúng.

## Tái kiểm tra toán học và kiểm định cuối

- `python3 -m reloadserver 8765` không chạy vì môi trường không cài mô-đun `reloadserver`; dùng `python3 -m http.server 8765 --bind 127.0.0.1` làm máy chủ cục bộ thay thế.
- Chromium duyệt đủ 37 trang ở hai khung 1280 × 720 và 800 × 600, tạo 74 ảnh chụp. Không có lỗi console, lỗi trang hoặc yêu cầu tài nguyên thất bại; điều hướng ngang/dọc bằng bàn phím đúng.
- Kiểm tra hình học và ảnh chụp phát hiện công thức `L09-28` bị cắt bên phải. Công thức đã được tách thành ba dòng và toàn bộ 74 lượt kiểm tra được chạy lại; lỗi không tái xuất hiện. Các cảnh báo còn lại chỉ là hộp KaTeX hoặc H1 vượt hộp nội bộ vài pixel, không vượt khung trang và không thấy tràn/chồng lấn trên ảnh.
- Biên tập cuối theo `no-ai-slop/eval.md` không phát hiện lời dẫn rỗng, tổng kết lặp, câu quảng bá hoặc nhịp câu máy móc. Rà mạch theo Quill xác nhận thuật ngữ, ký hiệu và đầu ra–đầu vào của 6 mạch liên tục; không tạo `quill.json`.
- Bốn Design Files của dự án Codex Slides B09 đã được cập nhật và đọc ngược lại; HTML, outline, storyboard và review-log khớp từng byte với tệp trong kho tại thời điểm đồng bộ. Không dùng chức năng render lại bộ RevealJS trong Codex Slides.
