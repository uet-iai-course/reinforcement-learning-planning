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

## Giai đoạn lecture note — 03/09/2026

### Kiểm kê, bản đồ chủ đề và runtime

- Nguồn: `RL-hk2-2025-2026/lecture09-ddqn-and-policy-gradient-part1.pdf`,
  40 trang. Metadata ghi “Bài giảng 10”, nhưng tên tệp, thứ tự học phần và bộ
  trang chiếu hiện có xác định đầu ra là Bài 09; giữ sai khác này trong nhật ký.
- Plan reader: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider
  OpenRouter, `plan/12/600/16000`; hoàn tất vòng 11 sau 232,45 giây.
- Source reader: cùng model/provider, cấu hình cũ `source/20/600/24000`; hoàn
  tất vòng 21 sau 544,73 giây, bao phủ đủ 40 trang. Lượt này lặp cùng khoảng đọc
  và tạo prompt 82.874 token; vì vậy preset từ bài này là `14/600/18000` và cầu
  nối chặn tool call trùng hệt đã thành công.
- Reviewer hợp nhất bản đồ: cùng model/provider, `review/8/600/12000`; hoàn tất
  vòng 2 sau 110,16 giây. Phạm vi chốt 14 chủ đề: 9 cốt lõi, 2 cầu nối, 2 bổ
  sung và 1 đọc thêm. Topic-04 ngăn phát biểu quá mức về Double DQN; topic-11
  nối dạng quỹ đạo với phân bố chiếm dụng; topic-13 chỉ báo trước Bài 10;
  topic-14 nằm ngoài tuyến chính.
- Writer note: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider
  OpenRouter, `write/20/900/32000`; ghi 31.630 byte ở vòng 3, sửa một ID thừa và
  hoàn tất vòng 5 sau 389,50 giây. Writer nhận đúng ba đầu vào cô lập.

### Năm báo cáo độc lập

| vai | model | runtime | phát hiện chính | quyết định |
|---|---|---:|---|---|
| Góc nhìn sinh viên | GLM | 44,29 giây | Hai đáp án topic-03 và topic-08 mâu thuẫn/mơ hồ; dải trang tham khảo thiếu tr. 3–4. | Sửa đủ. |
| Chuyên gia Học tăng cường | DeepSeek | 95,70 giây | PASS; gợi ý làm rõ câu hoán đổi mạng. | Sửa câu bằng hai đích 6,4 và 3,7. |
| Toán học–thuật toán | DeepSeek | 198,14 giây | PASS; ví dụ, giả thiết, $\gamma^t$ và phân bố chiếm dụng đúng. | Giữ công thức. |
| Phản biện học thuật–giảng dạy | DeepSeek | 81,55 giây | PASS; trình tự và cầu nối đủ. | Không đổi cấu trúc. |
| Kết nối–mạch viết/no-ai-slop | GLM | 47,64 giây | Hai lỗi nghiêm trọng trùng với vai sinh viên; nguồn topic-07 và chỉ dẫn biên tập cần sửa. | Sửa đủ. |

- Writer sửa tuần tự dùng GLM `patch/6/300/7000`; một phản hồi chạm giới hạn
  token nhưng cơ chế retry tiếp tục đúng model. Mười phép sửa được thử, ba phép
  sai chuỗi cũ thất bại rồi được sửa lại thành công; worker hoàn tất vòng 6 sau
  245,14 giây. Diff được điều phối viên kiểm trực tiếp, không dựa vào lời tóm tắt.
- Tái kiểm toán DeepSeek `recheck/6/600/10000` hoàn tất vòng 3 sau 86,42 giây,
  PASS. Tái kiểm mạch GLM phát hiện mâu thuẫn “ba/bốn/hai hợp đồng”, lặp câu có
  thể lược và thuật ngữ `collapse`; writer GLM `patch` sửa tám vị trí ở vòng 3
  và hoàn tất vòng 4 sau 37,99 giây.
- Tái kiểm mạch cuối GLM cùng profile hoàn tất vòng 3 sau 64,58 giây, PASS: bốn
  hợp đồng, 14 ID, bảy mạch, 120 phút và phân cấp X01–X03 đều nhất quán.

### Kiểm định tĩnh và quyết định công bố

- Kiểm định cục bộ: đúng một H1; 14 `note-topic-id` duy nhất; 304 biểu thức
  KaTeX parse ở strict mode; ba khối exercise, hint và solution; directive cân
  bằng; không có mã slide hoặc mẫu nội bộ.
- Không có code demo trong nguồn nên không tạo chương trình hoặc notebook.
- Lecture note không dùng ảnh raster. Tám SVG của deck hiện có không bị đổi ở
  giai đoạn note.
- Theo yêu cầu cụ thể của `prompt_lecture_note_deck.md`, thẻ index dùng hai nhóm
  “Bài giảng” và “Ghi chú bài giảng”; yêu cầu này thay thế quy tắc một liên kết
  duy nhất trong AGENTS.md cho bài đang xử lý.
- Codex Slides không được dùng trong giai đoạn note hiện tại vì runtime đang có
  Node.js 18.19.1, thấp hơn mức 20 của tiện ích. Không tuyên bố đã rà note bằng
  Codex Slides; kiểm định viewer cục bộ được thực hiện riêng trước commit.
- `python3 -m reloadserver 8765` vẫn không khả dụng do thiếu mô-đun. Để không
  phục vụ `.env`, kiểm định dùng bản sao tối thiểu trong `/tmp` và fallback
  `python3 -m http.server 8765 --bind 127.0.0.1`.
- Chromium mở liên kết từ thẻ Bài 09 ở 1280×720 và 800×600. Cả hai lượt hiển
  thị đúng tiêu đề, 14 heading cấp hai, 28 heading cấp ba, 304 công thức KaTeX,
  6 khối tương tác, liên kết quay lại đúng deck; không lỗi console, tài nguyên
  hỏng hoặc tràn ngang.

## Đồng bộ bộ trang chiếu với lecture note — 03/09/2026

Mục này thay thế các con số 37 trang/34 trang chính của vòng deck cũ ghi ở
phía trên; lịch sử cũ được giữ nguyên làm tham chiếu.

### Bằng chứng kiểm định cuối

- Bản đồng bộ note–deck hiện có 38 mã duy nhất: 35 mã L và 3 mã X; 38 notes;
  14 topic; 6 section ngoài; độ sâu section tối đa 2.
- Storyboard reviewer DeepSeek dùng `storyboard/10/600/12000`, hoàn tất vòng 11
  sau 225,26 giây, PASS.
- Năm reviewer độc lập: sinh viên GLM 164,43 giây, PASS và nêu ba lỗi cục bộ;
  chuyên gia RL DeepSeek 179,80 giây, PASS; toán DeepSeek lần đầu lỗi HTTP 400
  vì một kết quả search dài 2.024.384 ký tự làm yêu cầu ước lượng 562.425 token
  vượt cửa sổ 163.840; sau commit cầu nối `92a6eab`, chạy lại đúng model với
  `review/8/600/12000`, hoàn tất vòng 3 sau 86,23 giây, PASS; phản biện học
  thuật DeepSeek 207,89 giây, PASS; mạch viết GLM 125,88 giây, PASS và nêu ba
  lỗi mô tả nhẹ.
- Writer bản đồng bộ HTML GLM hoàn tất vòng 6 sau 328,86 giây; writer planning
  GLM vòng 6 sau 162,58 giây. Writer sửa lần một GLM `patch/6/300/7000` hoàn
  tất vòng 5 sau 74,76 giây; writer sửa lần hai cùng profile hoàn tất vòng 4
  sau 38,11 giây. Mọi lượt có requested_model=observed_model và provider
  OpenRouter.
- Tái rà toán DeepSeek `recheck/6/600/10000` hoàn tất vòng 5 sau 95,02 giây,
  PASS. Tái rà mạch GLM cùng profile hoàn tất vòng 3 sau 104,18 giây, nêu ba
  lệch nhẹ; sau sửa, tái rà mạch cuối hoàn tất vòng 3 sau 83,57 giây, PASS.
- Điều phối viên phát hiện một vế cũ còn đảo câu nối `X01`–`L09-10` dù lượt rà
  trước báo PASS. Writer GLM `patch/6/300/7000` sửa một lần thay thế, hoàn tất
  vòng 3 sau 24,17 giây. Reviewer mạch GLM tái rà đúng hai đoạn ở vòng 2 sau
  19,74 giây, PASS cho tuyến `L09-06`–`L09-07` → `L09-08` → `X01` → `L09-09`
  → `L09-10` → `L09-11`.
- Sửa đã áp dụng: thêm topic-14 qua `L09-30A`; đồng bộ đầy đủ 14 topic; đặt
  X01/X02 đúng topic và thứ tự; thêm `Z=0` ở X01; đổi ba chuỗi `G_{<t}` thành
  thực thể HTML `G_{&lt;t}`; làm rõ “35 trang không mang mã X”; sửa các câu nối
  L09-10 và storyboard.
- Kiểm định tĩnh: 38 slide, 6 section ngoài, 38 notes, 14 topic, 8 SVG XML hợp
  lệ có role/title/desc; không tài sản thiếu, raster hay URL mạng; cấu hình
  RevealJS bắt buộc và plugin cục bộ đúng; `git diff --check` sạch. Nội dung
  hiển thị không lộ mã nội bộ, topic, workflow hoặc thời lượng.
- `python3 -m reloadserver 8765` thất bại chính xác vì `No module named
  reloadserver`. Fallback dùng bản sao tối thiểu trong `/tmp` và
  `python3 -m http.server 8765 --bind 127.0.0.1`, không phục vụ `.env`.
- Chromium duyệt đủ 38 trang tại 1280×720 và 800×600: HTTP 200, 0
  console/page/request error, 0 KaTeX error, 0 tràn ngoài khung slide; bàn phím
  chuyển từ h=0 sang h=1. Ảnh L09-29, L09-30A và L09-33 được xem trực tiếp ở cả
  hai khung, không thấy chữ nhỏ bất thường, chồng lấn hoặc cắt công thức.
- Biên tập cuối theo `no-ai-slop/eval.md` không phát hiện khẩu hiệu, lời dẫn
  rỗng, kết luận lặp hoặc nhịp câu máy móc. Rà liên tục theo Quill dựa trên bản
  đồ 6 mạch và hai lượt reviewer mạch cuối; không tạo `quill.json`.
- Codex Slides không khả dụng vì Node.js 18.19.1 thấp hơn yêu cầu 20. Không
  tuyên bố đã rà bằng Codex Slides trong vòng hiện tại.
- Index Bài 09 đã có cả liên kết bài giảng và ghi chú; không cần đổi index ở
  giai đoạn đồng bộ deck.

### Năm báo cáo/tái rà độc lập

- Góc nhìn sinh viên — `z-ai/glm-5.3-flash`, OpenRouter: PASS. Cần sửa ký tự
  ba lần `<` thô trong ký hiệu `G_{<t}` tại `L09-29`; bổ sung giả thiết `Z=0`
  trên mặt bài tập `X01`; bỏ câu thời lượng lặp trong outline.
- Chuyên gia Học tăng cường — `deepseek/deepseek-v3.2`, OpenRouter: PASS, không
  có lỗi bắt buộc.
- Độ chính xác toán học và thuật toán — `deepseek/deepseek-v3.2`, OpenRouter:
  lần đầu lỗi HTTP 400 vì kết quả search 2.024.384 ký tự làm yêu cầu khoảng
  562.425 token; chạy lại cùng model sau bản vá cầu nối, hoàn tất vòng 3 trong
  86 giây và PASS, không có lỗi bắt buộc.
- Phản biện học thuật và giảng dạy — `deepseek/deepseek-v3.2`, OpenRouter:
  PASS, không có lỗi bắt buộc.
- Kết nối và mạch viết — `z-ai/glm-5.3-flash`, OpenRouter: PASS. Sửa thứ tự
  logic để `X01` nằm sau `L09-08` và trước `L09-09`; thay cách gọi “35 trang
  chính” vì `L09-30A` được ghi là ngoài tuyến chính.

### Bản vá được duyệt và bản vá bổ sung

1. Trong HTML, tại `L09-29`, đổi cả ba lần `G_{<t}` thành `G_{&lt;t}` để HTML
   không diễn giải `<t` như thẻ. Không thay công thức toán học.
2. Trong HTML, tại `X01`, thêm `$Z=0$` vào câu dữ kiện trước hai vector Q.
3. Trong outline, bỏ câu lặp “Tổng thời lượng chính...” ở đoạn sau bảng; giữ
   một mô tả đầy đủ về 120 + 30 phút.
4. Trong outline và storyboard, thay “35 trang chính” bằng “35 trang không mang
   mã X” hoặc cách tương đương chính xác; vẫn giữ tổng 38 mã.
5. Trong outline, sửa thứ tự logic thành `L09-01`–`L09-08`, `X01`,
   `L09-09`–`L09-19`, ...; không đổi thứ tự vật lý.
6. Bản vá bổ sung sau tái rà mạch: ghi chú `L09-10` thay “bài tập kế tiếp” bằng
   tham chiếu ngược tự nhiên tới `X01` (không hiển thị mã nội bộ); storyboard
   cụm sai lệch cực đại ghi đúng thứ tự `L09-06`–`L09-07` → `L09-08` → `X01` →
   `L09-09` → `L09-10`; outline đặt `X02` sau `L09-25` và trước `L09-26`.

## Đợt sửa 2026-10-28 — rà từng trang, trang tiêu đề mạch, giảm chữ

Phạm vi: deck `lecture-09-double-dqn-va-gradient-chinh-sach.html`, SVG trong `img/lec-09/`, ghi chú bài giảng `materials/lec-09/lecture-note.md`, `outline.md`, `storyboard.md`, `note-for-author.md`, thẻ Bài 9 trong `index.html`. Yêu cầu của người dùng: duyệt lần lượt từng trang; tiêu đề ngắn gọn, học thuật; mạch lập luận chặt; khái niệm không xuất hiện đột ngột; giảm chữ, bỏ giải thích dài dòng và văn nói; dùng hình nhắc lại ví dụ tại chỗ thay cho lời nhắc trang trước; sửa xong mỗi trang thì sửa phần tương ứng của ghi chú bài giảng; gắn Bài 09 lên `index.html`. Quy trình: ba rà soát chỉ đọc trên bản đóng băng (38 trang, 6 section ngoài, không trang tiêu đề mạch) → kế hoạch sửa của điều phối viên (D1–D7) → biên tập theo bước C0, rồi từng trang của từng mạch → điều phối viên duyệt sau mỗi mạch → rà lại chỉ đọc trên mạch đó → commit.

### Vai và mô hình

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà cấu trúc–mạch (kèm `no-ai-slop` Detect, `quill` làm danh sách kiểm) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Rà sinh viên–mật độ–trực quan (kèm kiểm Playwright) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Rà RL–toán (kèm đối chiếu ghi chú bài giảng, tính lại số) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập (tác tử duy nhất ghi tệp; `no-ai-slop` Edit) | Agent `general-purpose` | `claude-opus-5-5` | high | có |
| Điều phối viên (lập kế hoạch, duyệt, commit) | phiên chính | `claude-opus-5-5` | — | commit |

Mô hình và mức suy luận của các tác tử con ghi theo brief của điều phối viên; điều phối viên đối chiếu với lời gọi công cụ. Ba báo cáo nằm trong thư mục `review/` của scratchpad phiên: `CT-structure.md`, `SV-student.md`, `TH-math.md`; kế hoạch là `PLAN-decisions.md`.

Ghi chú về các vòng trước: bộ trang chiếu, ghi chú bài giảng và các vòng rà soát ghi ở các mục trên của nhật ký này được soạn và rà bằng mô hình qua OpenRouter (`z-ai/glm-5.3-flash`, `deepseek/deepseek-v3.2`). Theo quy định hiện hành (`CLAUDE.md`, `AGENTS.md` mục "Điều phối mô hình trong dự án"), OpenRouter không còn là tác tử hợp lệ, nên các kết luận "PASS" của các vòng đó không được tính là kiểm định cho đợt này. Nội dung cũ của nhật ký được giữ nguyên.

### Kết luận của ba rà soát

- Cấu trúc–mạch (CT): sáu mạch, không có mạch tổng kết, không trang tiêu đề mạch; thiếu trang Tiên quyết, Nội dung, Vấn đề trung tâm; không có khung lý thuyết chung (hai nửa nối bằng "rồi"); mạch 2 và 3 chia theo thuật toán thay vì theo chức năng; ba trang đứng sai chỗ so với nguồn (`L09-22`, `L09-30`, `L09-30A`); định lý gradient chính sách bị hạ thành "Mở rộng… có thể lược"; ví dụ lưới gộp trạng thái của nguồn tr. 23–25 bị đảo thông điệp; thuật ngữ lệch Bài 06–08 ("đích", "sai lệch cực đại", "online", "return"). Đề xuất bảy mạch, khung "ước lượng từ mẫu và độ chệch", hai ví dụ xuyên suốt.
- Sinh viên–mật độ (SV): `L09-16` tràn khung (chặn bàn giao), `L09-19` tràn; `L09-16` và `L09-33` vượt trần; mục tiêu DQN không được nhắc lại trên mặt trang; $\tau$, $p_\theta$ dùng trước khi định nghĩa; `X02` hỏi hàm điểm Gaussian trước khi dạy; bài tập dựa vào trí nhớ ví dụ trước; dấu phẩy thập phân lẫn dấu phẩy phân cách tọa độ; nhãn SVG tràn khung; ghi chú diễn giả có chỉ dẫn giảng viên, "Đáp án". Mọi số liệu đúng.
- RL–toán (TH): mọi ví dụ số đúng; nghiêm trọng: kết luận về gộp trạng thái của `L09-16` trái nguồn, `X02` dùng công thức chưa dạy; trung bình: hệ số $(1-\gamma)$ sai trong ghi chú bài giảng, định lý gradient chính sách không có trang kết quả gắn nhãn, điều kiện đổi đạo hàm và kỳ vọng mơ hồ, "đích", không phân biệt theo chính sách và khác chính sách, cờ $U$ biến mất, hướng dịch của $\mu$ ở `L09-27`, lý do bỏ $\gamma^t$ sai, khẳng định hội tụ và tác dụng thiếu giả thiết trong ghi chú bài giảng.

Quyết định của điều phối viên: kế hoạch D1–D7 (bảy mạch $8/15/30/15/22/20/10$ phút; thuật ngữ và ký hiệu theo Bài 08; ví dụ xuyên suốt A "trạng thái kế hai hành động" và B "bài toán một bước hai hành động"; hình nhắc lại tại chỗ; sửa nội dung bắt buộc D4; thứ tự bước C0, mạch 1, mạch 2…). Khi báo cáo và kế hoạch khác nhau, theo kế hoạch.

### Bảng phát hiện gộp

Nguồn phát hiện: CT, SV, TH như trên; mã CT (G, P) giữ để truy nguyên. Mức độ lấy mức cao nhất trong các báo cáo. Trạng thái "đã sửa ở …" còn chờ điều phối viên duyệt.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|---|
| chặn bàn giao | `L09-16` | Tràn khung 16:9: hai thẻ dưới bị cắt, đè chân trang (SV) | Đáy 860 px; sau C0 846 px | Tách hai trang; câu mở sang ghi chú | mở (bước `L09-16`) | chấp nhận (D1 mạch 4) |
| nghiêm trọng | `L09-16`, `aliased-grid-policy.svg`, ghi chú bài giảng topic-06, `note-for-author.md` | Đảo kết luận của nguồn tr. 23–25: khi đặc trưng gộp hai ô xám, chính sách ngẫu nhiên $0{,}5/0{,}5$ tốt hơn mọi chính sách tất định; deck và SVG nói ngược lại; "có thể tồn tại" quá yếu cho MDP hữu hạn có chiết khấu (CT P17, TH) | Nguồn tr. 24–25; mặt trang "Một chính sách tối ưu tất định có thể tồn tại; không cần ngẫu nhiên hóa"; TH tính lại hành lang gộp: tất định $-5{,}5$, ngẫu nhiên $-1{,}818$ | Hai mệnh đề, mỗi mệnh đề kèm điều kiện; vẽ lại lưới nguồn; sửa ghi chú và `note-for-author.md` | mở (bước `L09-16`) | chấp nhận (D1, D4) |
| nghiêm trọng | mạch 2–7 | Không mạch nào có trang tiêu đề mạch (CT G01, SV) | `grep strand-title` = 0 | Thêm `L09-M2T`…`L09-M7T` | mở (bước của từng mạch) | chấp nhận |
| nghiêm trọng | mạch 1 | Thiếu Tiên quyết và quy ước, Nội dung, Vấn đề trung tâm; bìa không có câu luận đề, đơn vị (CT G02, P01; SV) | `L09-01`–`L09-03` | Thêm `L09-01b`, `L09-02b`, `L09-02c`; sửa `L09-01`, `L09-02` | đã sửa ở S1–S6 (`L09-01`, `L09-01b`, `L09-01c`, `L09-01d`, `L09-02`, `L09-02b`, `L09-02c`) | chấp nhận |
| nghiêm trọng | mạch kết | Không có mạch tổng kết; `L09-33` là bốn thẻ "hợp đồng", 91 âm tiết > 80 (CT G03, P38; SV) | `L09-33` | Mạch 7 `L09-M7T`, `L09-K1`…`L09-K7`; bỏ `L09-33` | `L09-33` đã sang section 7 ở C0; nội dung mở | chấp nhận |
| nghiêm trọng | toàn bài | Không có khung lý thuyết chung; hai nửa nối bằng "rồi" (CT G04) | Phụ đề `L09-01` cũ | Khung "ước lượng từ mẫu và độ chệch" trong `outline.md`, `storyboard.md` | đã sửa ở C0 (planning) và S1, S6 (bìa, Vấn đề trung tâm) | chấp nhận |
| nghiêm trọng | toàn deck, SVG, ghi chú bài giảng | Thuật ngữ lệch Bài 06–08: "đích", "sai lệch cực đại", "online", "target", "replay", "return", "episodic", "tỷ số", "gần như chắc chắn", "véc-tơ" (CT G05; TH) | `grep -c đích`: deck 9, ghi chú 16 | Bảng thuật ngữ trong `outline.md`; sửa ở từng trang | bảng thuật ngữ đã có ở C0; mạch 1 đã dùng đúng; các trang khác mở | chấp nhận (D2) |
| nghiêm trọng | toàn deck | Khối `<style>` cục bộ thu nhỏ chữ và ghi đè hệ chung (CT G06; SV nhẹ) | `section[data-slide-id]{font-size:.82em}` | Bỏ; dùng lớp của `lecture-slide.css` | đã sửa ở C0 | chấp nhận (D5) |
| nghiêm trọng | `L09-07` | Double DQN mở bằng tên và công thức; thiếu dòng giới hạn của DQN và bước trực giác–ví dụ cho việc tách (CT P07) | Mặt trang bắt đầu bằng $a_i^*=\arg\max\ldots$ | Thêm `L09-06b`; `L09-07` "Mục tiêu Double DQN" mở bằng "Nhu cầu:" | mở | chấp nhận (D1 mạch 3) |
| nghiêm trọng | `L09-23` | Hàm điểm mở bằng định nghĩa; bước vấn đề của nguồn tr. 33 bị dời ra cuối bài (CT P24) | Thứ tự cũ `L09-23` … `L09-30A` | `L09-30A` làm trang vấn đề trước `L09-23`; dòng "Trực quan." | vị trí `L09-30A` đã sửa ở C0; nội dung mở | chấp nhận (D1 mạch 5) |
| nghiêm trọng | `X02` | Hỏi hàm điểm Gaussian trước khi công thức (`L09-26`) và dữ kiện (`L09-27`) xuất hiện (CT P27, SV, TH) | Thứ tự cũ `L09-25` → `X02` → `L09-26` | Chuyển sau `L09-27`; nêu lại dữ kiện | vị trí đã sửa ở C0; dữ kiện, nhãn mở | chấp nhận |
| nghiêm trọng | `L09-30` | Định lý gradient chính sách (nguồn tr. 39) bị gắn "Mở rộng… có thể lược", đặt sau REINFORCE; nhãn "Trực giác:" không có trong danh sách (CT P36; TH trung bình; SV) | Ghi chú "Trang này là phần mở rộng, có thể lược" | Trang "Định lý." cốt lõi trước REINFORCE; dạng chiếm dụng là "Dạng khác:" | vị trí đã sửa ở C0; nội dung mở | chấp nhận (D1 mạch 6, D4) |
| nghiêm trọng | `L09-19` | Tràn khung; dòng lời giải đè chân trang (SV) | Đáy 729 px; sau C0 792 px | Rút còn ≤ 6 dòng | mở | chấp nhận |
| nghiêm trọng | `L09-03`, `L09-04`, `L09-07` | Mục tiêu DQN không được nhắc lại trên mặt trang nào (SV) | Không trang nào có $R+\gamma\max_aQ_{\theta^-}(S',a)$ | "Nhắc lại:" mục tiêu DQN | đã sửa ở S3 (`L09-01c`); `L09-03` sẽ nhắc lại tại chỗ ở bước của trang | chấp nhận |
| nghiêm trọng | `L09-20`, `L09-22`, `L09-28` | $\tau$, $p_\theta(\tau)$ dùng trước khi định nghĩa ở `L09-28A` (SV; TH trung bình; CT G09) | `L09-20` "$\mathbb E_{\tau\sim p_\theta}[G_0]$" | Định nghĩa ở `L09-20` | mở | chấp nhận |
| trung bình | ghi chú diễn giả nhiều trang | Dòng "Nguồn:" mang quyết định biên tập; lời phân tuyến, thời lượng, nhãn quy trình; chỉ dẫn giảng viên (CT G07; SV) | `L09-13` "chu trình rút gọn"; `L09-30` "có thể lược"; `L09-06` "Không phát biểu…" | Ghi chú chỉ giải thích học thuật; quyết định sang `storyboard.md` | mạch 1 đã sửa; các trang khác mở | chấp nhận |
| trung bình | `X01`, `X02`, `X03`, `L09-15`, `L09-19`, `L09-25`, `L09-27` | Lời giải trên mặt trang không nhãn; ghi chú dùng "Đáp án" (CT G08; SV; TH nhẹ) | Lớp `fragment answer` | Nhãn "Lời giải:"; "Lời giải" thay "Đáp án" | nhãn "Lời giải:" đã thêm ở C0 (sáu đoạn `.fragment`); "Đáp án" trong ghi chú `L09-15`, `L09-19` mở | chấp nhận |
| trung bình | nhiều trang | Ký hiệu dùng trước khi định nghĩa: $P$, $\psi_t$, $\operatorname{Cat}$, MDP, Jensen, $q_\pi$ (CT G09; TH) | `L09-16`, `L09-19`, `L09-22`, `L09-29`, `L09-06`, `L09-30` | Gom vào "Ký hiệu:" hoặc định nghĩa tại chỗ | MDP, $\rho_0$, $P$, Jensen, $q_\pi$ đã có ở `L09-01b`–`L09-01d` (S2, S3); $\psi_t$, $\operatorname{Cat}$ mở | chấp nhận |
| trung bình | `L09-22`, `L09-30`, `L09-30A` | Ba trang đứng sai chỗ so với nguồn và chỗ dùng (CT G10) | Nguồn tr. 33 → 34 → 39 → 40 | Chuyển theo D1 | đã sửa ở C0 | chấp nhận |
| trung bình | học liệu | Ghi chú bài giảng chia "Mạch k — … (phút)" khác deck; X01–X03 dùng mã nội bộ; chưa có `exercises.md`; `index.html` chưa có thẻ Bài 09 (CT G11; TH nhẹ) | `lecture-note.md`; `grep lecture-09 index.html` = 0 | Mục `## N.` theo bảy phần; Bài tập 09.k; thẻ index | mục đánh số theo bảy phần, bỏ thời lượng, thẻ index đã sửa ở C0/mạch 1; X01–X03 mở (mạch 7) | chấp nhận (D6, D7) |
| trung bình | nửa học giá trị | Ba bộ số rời cho cùng câu hỏi; không so hai thuật toán trên cùng số liệu (CT G12) | `L09-08` $(5,4)/(3,6)$; `L09-13` $(2,1)/(1,4)$ | Ví dụ A | mở | chấp nhận (D3) |
| trung bình | `L09-02` | Tiêu đề "Kết quả học tập"; bốn thẻ không khớp mạch, không kiểm được (CT P02) | Mặt trang cũ | "Mục tiêu học tập", năm mục ứng mạch 2–6 | đã sửa ở S4 | chấp nhận |
| trung bình | `L09-03` | Hai luận điểm khác loại; "Bài này giả sử…"; không "Muốn…", không ví dụ số; câu khẩu hiệu trong SVG; nhãn SVG tràn (CT P03; SV) | Tiêu đề "DQN ổn định hơn nhưng vẫn có sai lệch" | Quy ước $O=S$ sang `L09-01b`; trang vấn đề với ví dụ CartPole | quy ước $O=S$ đã sang `L09-01b` (S2); phần còn lại mở | chấp nhận |
| trung bình | `L09-04` | Hình hai hành động nhiễu đứng trước khi ví dụ được đặt; tiêu đề câu kèm tiếng Anh; $Q_a$, $\widehat Q_a$ chưa đọc thành lời (CT P04; SV; TH nhẹ) | `maximization-bias.svg` ở `L09-04` | Chuyển hình xuống `L09-05`; dùng $q_a$ cho giá trị đúng | mở | chấp nhận |
| trung bình | `L09-06` | Không nhãn "Mệnh đề.", không giả thiết khả tích; "Đây là Jensen vì…"; "có thể bằng nhau" (CT P06; SV; TH nhẹ) | Mặt trang | "Mệnh đề." có giả thiết; "Chứng minh." một dòng; "thì hai vế bằng nhau" | mở | chấp nhận |
| trung bình | `L09-07`, ghi chú topic-03 | Coi việc không tính argmax tại trạng thái kết thúc là bắt buộc; mâu thuẫn cách cài theo lô của Bài 08 (TH) | Ghi chú Bài 08 dòng 358, 426 | Dạng mặt nạ; nói một lần dạng từng trường hợp cho cùng giá trị | mở | chấp nhận (D2) |
| trung bình | `X01`, `L09-09` | `X01` đứng trước trang hình thức; câu (a) lặp `L09-05` dựa vào trí nhớ; `L09-09` chỉ nhắc lại Bài 08, không phải thuật toán Double DQN (CT P09, P10; SV) | Thứ tự cũ `X01` → `L09-09` | `L09-09` "Thuật toán." trước `X01`; câu (a) kiểm việc tách | thứ tự đã sửa ở C0; nội dung mở | chấp nhận |
| trung bình | `L09-10` | 58–62 âm tiết; câu chung "nhiều lần chạy" không số (CT P11; SV) | Mặt trang | Giữ hai luận điểm có điều kiện | mở | chấp nhận |
| trung bình | `L09-11`, `L09-12`, `L09-13` | Mở thuật toán bằng tên; công thức trước ví dụ; thiếu khởi tạo, hành vi, dừng; "$Z=0$" như phép gán; nhãn SVG tràn (CT P12–P14; SV; TH nhẹ) | Mặt trang | Dòng giới hạn; `L09-13` trước `L09-12`; thuật toán đủ | thứ tự `L09-13`/`L09-12` đã sửa ở C0; nội dung mở | chấp nhận |
| trung bình | `L09-15` | Tiêu đề điều hướng; "Đáp án"; cầu nối sang mạch 4 chỉ trong ghi chú (CT P16; SV) | Mặt trang, ghi chú | "Bài tập: …"; cầu nối vào ghi chú trang tiêu đề mạch 4 | mở | chấp nhận |
| trung bình | `L09-18` | Ví dụ không có số; số liệu nguồn tr. 27–29 bị bỏ (CT P19; SV) | `policy-distributions.svg` | Ví dụ $(0{,}1;0{,}2;0{,}2;0{,}5)$ | mở | chấp nhận |
| trung bình | `L09-20`, `L09-21` | Hàm mục tiêu mở bằng định nghĩa; "episodic"; câu chỉ đường; thẻ "Ước lượng" nêu lời giải trước vấn đề (CT P21, P22) | Mặt trang | Vấn đề và ví dụ B trước định nghĩa | mở | chấp nhận |
| trung bình | `L09-22` | Giả thiết cách chỗ dùng sáu trang; "hợp đồng"; điều kiện mơ hồ, chưa đủ cho $T$ ngẫu nhiên (CT P23; TH) | Mặt trang | "Giả thiết:" cạnh `L09-28`; điều kiện đủ $R$, $\psi$, $T$ bị chặn | vị trí đã sửa ở C0; nội dung mở | chấp nhận (D4) |
| trung bình | `L09-28`, `L09-29` | Mặt trang `L09-28` không có câu chữ; tiêu đề câu; $\psi_t$ chưa định nghĩa; kết luận trước phép tách (CT P30, P32; SV; TH nhẹ) | Mặt trang | Dòng "Muốn…"; ví dụ B; `L09-29b` | mở | chấp nhận |
| trung bình | `L09-31`, `L09-32`, `X03` | Thuật toán mở bằng tên, thiếu đầu vào, khởi tạo, dừng; ví dụ sau thuật toán; `X03` "giữ dữ kiện của ví dụ trước"; ba câu gộp; không phân biệt theo chính sách và khác chính sách; lý do bỏ $\gamma^t$ sai (CT P33–P35; SV; TH) | Mặt trang, ghi chú | Thuật toán đủ; `L09-32` trước; thẻ dữ kiện; "Lưu ý:" theo chính sách; Nota và Thomas (2020) | thứ tự `L09-32`/`L09-31` đã sửa ở C0; nội dung mở | chấp nhận (D4) |
| trung bình | `L09-30A` | Lệch thứ tự nguồn; tiền tố "Đọc thêm:"; ghi chú phân tuyến; $u_k$ chưa định nghĩa (CT P37; SV) | Tiêu đề cũ | Trang vấn đề của hàm điểm, ví dụ B | vị trí đã sửa ở C0; nội dung mở | chấp nhận |
| trung bình | `L09-27`, `L09-32`, `X03` | Dấu phẩy thập phân lẫn dấu phẩy phân cách tọa độ (SV) | "$(1{,}5,3)$" | Dấu chấm phẩy | mở; mạch 1 và ghi chú phần mở đầu đã dùng dấu chấm phẩy | chấp nhận (D4) |
| trung bình | `L09-27` | Lời giải mơ hồ về hướng dịch của $\mu$ (TH; CT nhẹ; SV nhẹ) | $\Delta\mu=\alpha G\cdot1{,}5\lVert\phi\rVert^2/\sigma^2$ | "hệ số âm đẩy $\mu$ ra xa $a$" | mở | chấp nhận (D4) |
| trung bình | ghi chú bài giảng topic-11 | Hệ số chuẩn hóa sai: phải là $(1-\gamma)$, không phải $1/(1-\gamma)$ (TH) | Dòng "với hệ số $1/(1-\gamma)$ bảo đảm $\sum_sd^\pi(s)=1$" | Sửa hệ số; nói tổng tính cả trạng thái hấp thụ | mở (bước `L09-30`) | chấp nhận (D4) |
| trung bình | ghi chú bài giảng topic-01, topic-03 | Khẳng định hội tụ và tác dụng của Double DQN thiếu giả thiết; bộ ước lượng kép có thể chệch âm (TH) | "Q-learning hội tụ dưới các giả thiết tiêu chuẩn"; "giảm sai lệch…, ổn định hơn" | Nêu giả thiết; hạ mức khẳng định | mở (bước `L09-03`, `L09-10`) | chấp nhận (D4) |
| trung bình | SVG `dqn-stability`, `dqn-vs-ddqn`, `double-q-cross-update` | Nhãn chữ tràn khung; câu khẩu hiệu trong hình; không khai báo phông không chân (SV; CT) | Ảnh | Sửa SVG ở bước của trang | mở | chấp nhận (D5) |
| nhẹ | nhiều trang | Tiêu đề ví dụ không theo dạng "Ví dụ: <đối tượng>"; tiêu đề dạng câu (CT P05, P08, P14, P26, P29, P34; SV) | "Ví dụ Rademacher", "Áp dụng cập nhật chéo" | Đổi ở bước của trang | mở | chấp nhận |
| nhẹ | 18 trang | Ghi chú diễn giả dưới 40 âm tiết (SV) | `L09-25` 14, `X02` 24… | Bổ sung giả thiết, nhầm lẫn thường gặp | mở | chấp nhận |
| nhẹ | `L09-24`, `softmax-score.svg` | "Tổng kỳ vọng của hàm điểm" sai từ; thiếu một dòng "Chứng minh." (CT P25; SV) | Hình | "Kỳ vọng theo $\pi_\theta$"; dòng chứng minh | mở | chấp nhận |
| nhẹ | `L09-08` | Thiếu kết luận $y^{\mathrm{DDQN}}\le y^{\mathrm{DQN}}$ trên mọi mẫu (TH) | Ba bộ số đều thỏa | Thêm dòng hoặc ghi chú | mở | chấp nhận |
| nhẹ | toàn bài | Ẩn dụ "hợp đồng"; "Thu hồi bất đẳng thức Jensen" (CT G13; TH; SV) | `L09-22`, `L09-33` | "Giả thiết:", "Nhắc lại:" | mở | chấp nhận |
| nhẹ | ghi chú bài giảng | Mã nội bộ hiện ra cho người đọc ("topic-02", "X01"); `\text{if }` (TH) | Các dòng của mục 2–7 | Thay bằng số hiệu mục, Bài tập 09.k | phần mở đầu và Mục 1 đã sạch; mục 2–7 mở | chấp nhận |
| nhẹ | outline | Nội dung nguồn tr. 11, 28–29, 31 bị bỏ không ghi lý do (TH) | Bảng ánh xạ nguồn cũ | Ghi quyết định cho từng trang | tr. 11 ghi ở C0 (`storyboard.md`, Lệch khỏi trật tự nguồn); tr. 28–29, 31 mở | chấp nhận |
| trung bình | `L09-07`, `L09-19`, `L09-24`, `L09-30`, `L09-31` | Phát hiện ở C0: sau khi bỏ CSS cục bộ (`font-size:.82em`, `.smallmath`, `.figure` `max-height:325px`), đáy nội dung ở 750, 792, 787, 630, 748 px; tràn phải `L09-24` 1 310 px, `L09-30` 1 282 px; `L09-16` 846 px | `check.py --all`, 1600×900 | Sửa ở bước của từng trang; không thu nhỏ chữ | mở | chờ điều phối viên |

### Bước C0 — sắp lại bảy mạch, bỏ CSS cục bộ (biên tập viên)

- Deck: bảy section ngoài theo kế hoạch D1, chỉ bằng di chuyển trang: mạch 1 `L09-01`, `L09-02`; mạch 2 `L09-03`–`L09-06`; mạch 3 `L09-07`, `L09-08`, `L09-09`, `X01`, `L09-10`, `L09-11`, `L09-13`, `L09-12`, `L09-14`, `L09-15`; mạch 4 `L09-16`–`L09-19`; mạch 5 `L09-20`, `L09-21`, `L09-30A`, `L09-23`–`L09-27`, `X02`; mạch 6 `L09-28`, `L09-22`, `L09-28A`, `L09-29`, `L09-30`, `L09-32`, `L09-31`, `X03`; mạch 7 `L09-33` (sẽ bỏ). Trang tiêu đề mạch 2–7 và các trang mới của mạch 2–7 chưa tạo.
- CSS: bỏ khối `<style>`; `div.reveal` thêm lớp `lecture-deck`; `.math-large smallmath` thành `.math-large`; sáu khối `div.fragment.answer` thành `p.fragment` mở bằng "**Lời giải:**" như deck 08. Các lớp `.box`, `.grid2`, `.card`, `.check`, `.figure`, `.math-large`, `.note-source` có trong `lecture-slide.css` dưới `.reveal.lecture-deck`. Kiểu nội dòng `max-height:230px` của hình ở `L09-07` giữ nguyên tới bước của trang. `lecture-slide.css` không đổi.
- Khai báo Reveal theo deck 08: bỏ `plugin/markdown/markdown.js` và `RevealMarkdown`; thêm `scrollActivationWidth:null`; plugin cục bộ `RevealHighlight`, `RevealNotes`, `RevealMath.KaTeX`; `controlsLayout:"edges"`, `slideNumber`, `hash`, `hashOneBasedIndex`, khung $1280\times720$.
- Nội dung từng trang giữ nguyên, trừ nhãn "Lời giải:".
- `outline.md`: phạm vi, khung lý thuyết chung, năm mục tiêu ứng mạch 2–6, bảy mạch với dòng dẫn dự kiến, bảng thuật ngữ Việt–Anh, quyết định ký hiệu, danh sách kiểm Concept cho mạch 1, bảng `note-topic-id`, thời lượng; phần cũ chuyển xuống "Bản trước đợt sửa 2026-10-28".
- `storyboard.md`: bản đồ bảy mạch (chức năng, đầu vào, đầu ra, đóng góp, mã trang tiêu đề mạch, thời lượng), danh sách trang theo mạch (quyết định, lý do, vị trí sau C0 và sau bước mạch 1), lệch khỏi trật tự nguồn, ngoại lệ mật độ; phần cũ chuyển xuống "Bản trước đợt sửa 2026-10-28".
- `index.html`: thẻ Bài 9 theo khuôn thẻ Bài 8 (Bài giảng; Ghi chú bài giảng qua viewer; Bài tập và Thực hành "Chưa có"); không liên kết tệp kế hoạch.
- Kiểm C0 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900): 38 `data-slide-id` duy nhất, 7 section ngoài, mọi trang có `aside.notes`, không URL mạng trong deck, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ra ngoài, không cuộn ngang. Tràn: xem dòng cuối bảng phát hiện.

### Bước mạch 1 (S1–S6, biên tập viên)

| bước | trang | thay đổi | âm tiết mặt trang trước → sau | dòng sau | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|---|
| S1 | `L09-01` | Tiêu đề giữ "Double DQN và gradient chính sách"; phụ đề "Tách chọn–đánh giá, rồi tối ưu trực tiếp phân phối hành động" thay bằng "Bài 09 · Học tăng cường", câu luận đề một câu trong hộp, đơn vị, năm học; ghi chú diễn giả viết lại (khoảng 130 âm tiết), mã chủ đề `lec-09-topic-16` | 20 → 58 (hộp 39) | 4 | Câu luận đề, ghi chú; bỏ "Bài học bắt đầu từ…" (tài liệu làm chủ ngữ); đạt | chờ điều phối viên duyệt |
| S2 | `L09-01b` (mới) | "Tiên quyết và quy ước", phần Ký hiệu: dòng "Ký hiệu:" và bảng năm hàng; mã chủ đề `lec-09-topic-15` | — → 59 | 6 | Dòng ký hiệu, bảng, ghi chú; "phần 6 dùng lại điều này" đổi thành câu bị động có đối tượng làm chủ ngữ; đạt | chờ điều phối viên duyệt |
| S3 | `L09-01c`, `L09-01d` (mới) | "Tiên quyết và quy ước", phần Nhắc lại: mục tiêu DQN, $L_B$, $\operatorname{sg}$, đồng bộ, cắt ngắn (Bài 08); chính sách, $\mathbb E_\pi$, $G_t$, $q_\pi$ (Bài 03), Jensen. Bản một trang có đáy 808 px, tràn phải 1 395 px, nên tách hai trang | — → 31 và 31 | 5 và 4 | Ghi chú: "và cho dấu $\ge$, không cho dấu lớn hơn nghiêm ngặt" (đối lập nhị phân) đổi thành "chỉ cho dấu $\ge$; dấu lớn hơn nghiêm ngặt cần thêm điều kiện"; đạt | chờ điều phối viên duyệt |
| S4 | `L09-02` | "Kết quả học tập" (bốn thẻ) → "Mục tiêu học tập" (năm mục ứng mạch 2–6); ghi chú nêu sản phẩm từng mục | 52 → 69 | 5 | Năm mục mở bằng động từ học tập; bỏ câu siêu văn bản "hai nửa có cầu nối rõ"; đạt | chờ điều phối viên duyệt |
| S5 | `L09-02b` (mới) | "Nội dung": bảy mục liên kết `#/1`…`#/7`, "Đọc trước: Sutton và Barto (2018), §6.7, §13.1–13.3, §13.7." | — → 39 | 8 (ngoại lệ) | Ghi chú liệt kê việc của từng phần và mục sách; đạt | chờ điều phối viên duyệt |
| S6 | `L09-02c` (mới) | "Vấn đề trung tâm": hộp bài toán và năm câu trả lời có điều kiện | — → 71 (ngoại lệ) | 6 | Dòng 3 rút gọn để một dòng; không câu hỏi tu từ, không khẩu hiệu; đạt | chờ điều phối viên duyệt |

Ghi chú bài giảng ở bước mạch 1:

- Phần đầu viết lại theo `AGENTS.md` mục "Cấu trúc bắt buộc của một chương" và khuôn ghi chú Bài 08: đoạn mở đầu một đoạn (thay các dòng giảng viên, học kỳ, thời lượng, nguồn); "Mục tiêu học tập" năm mục có sản phẩm; "Kiến thức tiên quyết" tám nhóm in đậm có số hiệu (08.3, 08.4, 08.6, 08.10, 08.12, 08.16, 08.19, 08.21, 03.8, 03.9, 03.13, 03.16) và phát biểu lại; "Bảng ký hiệu" 27 hàng ba cột, quy ước đọc, hai vai của $\theta$, tương ứng với giáo trình *Học máy thống kê* và Bài 03; "Bản đồ chủ đề" bốn nhóm có cột Mục; "Bảy phần của chương" và dòng "Đọc trước:" thay bảng "Bảy mạch — 120 phút".
- `## 1. Mở đầu`, "Bài toán trung tâm của chương" (`lec-09-topic-16`): kết quả kế thừa (Thuật toán 08.13, Nhận xét 08.19), bài toán có số liệu (CartPole, cận $100$ và $99{,}3$, $\max_aQ_\theta(O_0,a)=108{,}5$ ở lần chạy khi soạn bài thực hành Bài 08, mục 7, ô in kết quả), giới hạn dẫn tới nửa sau (hành động liên tục; lưới gộp trạng thái của nguồn tr. 23–25), hình mới `central-problem.svg` có đoạn đọc hình, năm câu trả lời có điều kiện khớp `L09-02c`, đoạn kết nối sang Mục 2.
- Các mục cũ "Mạch 1"…"Mạch 7 — … (phút)" đổi tiêu đề thành `## 2.`…`## 7.` theo bảy phần, chỉ đổi và dời tiêu đề: mục Double Q-learning nằm trong Mục 3; mục phân bố chiếm dụng nằm cuối Mục 6; sai phân hữu hạn và cầu nối Bài 10 tạm nằm trong Mục 7 tới bước của trang `L09-30A`; "Bốn hợp đồng cần giữ" thành mục con của Mục 7; "Bài tập (30 phút)" thành "Bài tập củng cố". Nội dung các mục 2–7 chưa sửa; các lỗi đã biết (hệ số $1/(1-\gamma)$, "đích", "topic-02", "Phần bổ sung; có thể lược…") sửa ở bước của trang tương ứng.
- Mã chủ đề mới: `lec-09-topic-15` (Kiến thức tiên quyết, ghi trước `## Kiến thức tiên quyết`; ứng `L09-01b`–`L09-01d`) và `lec-09-topic-16` (Mở đầu; ứng `L09-01`, `L09-02`, `L09-02b`, `L09-02c`), theo cách deck 08 dùng `lec-08-topic-13`, `lec-08-topic-17`. `lec-09-topic-01` giữ cho `L09-03`.
- Giáo trình đã tham khảo cho phần đầu: Sutton và Barto (2018), §6.7 (cách mở độ chệch của phép cực đại bằng nhiều hành động có giá trị đúng bằng $0$ và ước lượng phân tán quanh $0$; Ví dụ 6.7), §13.1 (lý do chính sách tham số hóa: chính sách gần đúng tốt nhất có thể ngẫu nhiên khi các trạng thái giống nhau dưới xấp xỉ hàm, Ví dụ 13.1), bản trích văn bản tại `/data/tqlong/qa/sources/sutton-barto-rl2020/extracted.md`. Không dịch hay chép đoạn văn.
- Độ dài: 7 635 từ theo `wc -w` (gồm công thức và bảng), 5 895 từ thân văn khi bỏ công thức và bảng; trước bước mạch 1: 4 271 từ. Đích ≥ 8 000 từ đạt khi các mục 2–7 được viết lại.
- `no-ai-slop` (Edit) trên phần ghi chú mới viết: sửa câu lấy tài liệu làm chủ ngữ ("Mục 2 áp dụng…", "Mục 5 dùng…", "Mục 6 dùng…", "Mục 7 đặt…", "Chương không xét…", "Nửa sau của chương xuất phát…", "chương có một khung chung") thành câu có chủ ngữ là đối tượng hoặc "chúng ta"; không câu hỏi tu từ, không từ trong danh sách cấm, không gạch ngang dài. Đạt.

Kiểm sau bước mạch 1 (Playwright Chromium, `http://127.0.0.1:8799`):

- Deck: 43 `data-slide-id` duy nhất, 7 section ngoài, mọi trang có `aside.notes`, không URL mạng. `#/1`…`#/7` và bảy liên kết của `L09-02b` mở `L09-01`, `L09-03`, `L09-07`, `L09-16`, `L09-20`, `L09-28`, `L09-33`. Mạch 1 ở 1600×900 và 390×844: 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang; đáy nội dung `L09-01` 455, `L09-01b` 583, `L09-01c` 557, `L09-01d` 467, `L09-02` 384, `L09-02b` 560, `L09-02c` 579 px (khung 720). Đã xem ảnh 1600×900 của bảy trang và ảnh 390×844 của `L09-02c`.
- Ghi chú bài giảng trong viewer (1400×900 và 390×844): hiển thị, 17/17 khối `:::` được nhận diện, 528 biểu thức KaTeX, 0 `.katex-error`, 0 lỗi console, 0 yêu cầu ngoài, mã chủ đề không trùng (viewer không báo lỗi), hình `central-problem.svg` tải được.
- `index.html`: thẻ Bài 9 hiển thị ở 1400×900 và 390×844, hai liên kết trả HTTP 200, không cuộn ngang.
- `git diff --check`: không lỗi.

Điểm chờ điều phối viên quyết:

1. Ba trang Tiên quyết (`L09-01b` Ký hiệu, `L09-01c` Nhắc lại Bài 08, `L09-01d` Nhắc lại Bài 03 và Jensen) thay cho một hoặc hai trang của kế hoạch; trang Ký hiệu đặt trước trang Nhắc lại.
2. Ký hiệu $q_\pi$ (Bài 03–08) thay $Q^\pi$ của brief và bản trước.
3. Tên mạch 5 "Hàm mục tiêu và hàm điểm" thay "Mục tiêu và hàm điểm".
4. Dòng "Đọc trước:" thêm §13.7.
5. Ký hiệu phân bố chiếm dụng ($d^\pi$ trùng chữ $d$ số chiều): quyết định ở bước mạch 6.
6. Ngoại lệ mật độ `L09-02c` (71 âm tiết) và `L09-02b` (8 dòng).

### Quyết định của điều phối viên về C0 và mạch 1 (2026-10-28)

- C0 và mạch 1: chấp nhận có điều kiện (sửa theo bước R1).
- Sáu điểm lệch kế hoạch do biên tập viên nêu: chấp nhận 1 (ba trang Tiên quyết, Ký hiệu trước Nhắc lại), 2 ($q_\pi$), 3 (tên mạch 5 "Hàm mục tiêu và hàm điểm"), 4 (§13.7 trong dòng Đọc trước), 6 (tràn có từ trước sửa ở bước của từng trang). Điểm 5: phân bố chiếm dụng viết $\nu^\pi_\gamma$, gọn $\nu^\pi$; không dùng $d$ hay $\mu$; ghi vào bảng ký hiệu ngay, áp dụng ở mạch 6.
- Thẻ Bài 9 trên `index.html`: **giữ**, theo yêu cầu rõ của người dùng ("gắn chúng lên 2627-1/index.html"), như quyết định đã ghi cho Bài 08; ghi chú bài giảng được sửa song song từng trang trong đợt này.

### Rà lại mạch 1 (bước R1)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 1 (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R1 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R1-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 1 nghiêm trọng, 7 trung bình, 9 nhẹ; điều phối viên chấp nhận toàn bộ, kèm các chốt ghi ở cột "quyết định".

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|---|
| nghiêm trọng | `L09-02c` dòng 3; ghi chú bài giảng Mục 1 câu trả lời 3; `outline.md` | "Không chệch lên" thiếu giả thiết bản đánh giá không chệch; "Double DQN chỉ giảm" khẳng định không điều kiện; Double Q-learning bị coi là độc lập | "Khi chọn và đánh giá độc lập: không chệch lên; Double DQN chỉ giảm độ chệch." | Câu có giả thiết; Double Q-learning độc lập chỉ ở dạng lý tưởng | đã sửa ở R1: mặt trang "Khi bản đánh giá không chệch, độc lập với bản chọn: không chệch lên; Double DQN chỉ gần thỏa."; ghi chú bài giảng câu trả lời 3 viết lại (mỗi bảng bootstrap từ bảng kia; mức giảm đo bằng thực nghiệm); đoạn sau danh sách và "Giả thiết chung" của `outline.md` sửa theo | chấp nhận (câu đề xuất, áp dụng nhất quán) |
| trung bình | `L09-02c` dòng 6; ghi chú bài giảng câu trả lời 6 | "$\psi_\theta$ bị chặn" loại chính sách Gaussian | Hàm điểm Gaussian không bị chặn theo $a$ | Điều kiện phủ cả softmax và Gaussian | đã sửa ở R1: "Khi $\rho_0$, $P$ không phụ thuộc $\theta$; $R$, $T$ bị chặn; đổi được $\nabla_\theta$ và $\int$"; ghi chú bài giảng thêm điều kiện đủ (đặc trưng bị chặn; softmax có hàm điểm chuẩn $\le2\Phi$; Gaussian $\sigma^2$ cố định có đạo hàm mật độ bị trội bởi đa thức nhân mật độ Gaussian); ghi chú diễn giả nêu lý do | chấp nhận (không dùng "ψ bị chặn") |
| trung bình | `L09-02c` dòng 2 | $\widehat Q_a$ không nói ước lượng của gì; vế phải không so với giá trị đúng | Mặt trang cũ | Dùng $q_a$ | đã sửa ở R1: "Khi mỗi $\widehat Q_a$ không chệch cho $q_a$, có nhiễu: $\mathbb E[\max_a\widehat Q_a]\ge\max_aq_a$"; ghi chú bài giảng câu trả lời 2 và `outline.md` theo; `L09-03`, `L09-04` ở bước mạch 2 | chấp nhận |
| trung bình | `L09-01` luận đề; ghi chú bài giảng đoạn mở đầu | Khẳng định không điều kiện | "cho giá trị chệch lên"; "cho ước lượng không chệch" | Thêm điều kiện, vẫn một câu | đã sửa ở R1: "Trên ước lượng không chệch có nhiễu, độ chệch của phép cực đại không âm; …, còn dưới giả thiết của định lý gradient chính sách, hàm điểm (score function) cho ước lượng không chệch của gradient."; đoạn mở đầu ghi chú thêm hai điều kiện | chấp nhận |
| trung bình | `L09-01c`; `L09-02c` | Mặt trang không gọi tên mạng trực tuyến, mạng mục tiêu; $\theta$ đổi vai không được nói trong deck | Mặt trang cũ | Dòng gọi tên; ghi chú diễn giả về vai của $\theta$ | đã sửa ở R1: dòng "$Q_\theta$: mạng trực tuyến (online network); $Q_{\theta^-}$: mạng mục tiêu (target network), $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu"; cắt ngắn chuyển vào dòng $\operatorname{sg}$; ghi chú diễn giả `L09-02c` nói $\theta$ là tham số chính sách từ phần 4 | chấp nhận |
| trung bình | `L09-01d`, `L09-01b`; ghi chú bài giảng | Bài 03 viết $\mu$, $p$; deck gán $\rho_0$, $P$ cho Bài 03 không nói tương ứng | Ghi chú Bài 03, dòng 611 | Nêu tương ứng một lần | đã sửa ở R1: ghi chú diễn giả `L09-01b` và đoạn sau bảng ký hiệu của ghi chú bài giảng nêu $\mu\to\rho_0$, $p\to P$ và lý do | chấp nhận (giữ $\rho_0$, $P$) |
| trung bình | `index.html` | Thẻ Bài 9 công bố trước khi bài hoàn tất | CLAUDE.md, mục Index | Hoãn hoặc ghi lý do | giữ thẻ; quyết định ghi ở mục trên | chấp nhận (giữ theo yêu cầu người dùng) |
| trung bình | `L09-03`, `L09-04` | Lặp quy ước $O=S$, "Bài này", "Replay", "đích", $Q_a$ cho giá trị đúng, "sai lệch" | Mặt trang | Sửa ở bước mạch 2 | mở (bước mạch 2) | chấp nhận (chuyển bước mạch 2) |
| nhẹ | `L09-02c` dòng 6 | Ký hiệu rút gọn; điều kiện dòng 5 không nói là cộng dồn | "$\nabla J=\mathbb E[\sum_t\ldots]$" | $\nabla_\theta J=\mathbb E_{\pi_\theta}[\sum_{t=0}^{T-1}\ldots]$ | đã sửa ở R1 (công thức đầy đủ; ghi chú bài giảng viết "Nếu thêm…"; mặt trang bỏ chữ "thêm" để giữ mật độ, quan hệ cộng dồn nêu trong ghi chú diễn giả qua "Dòng số $N$…") | chấp nhận |
| nhẹ | `L09-02c` dòng 4 | Thiếu "cần hành động khác nhau" | Mặt trang | Thêm điều kiện | đã sửa ở R1 ("đặc trưng gộp trạng thái cần hành động khác") | chấp nhận |
| nhẹ | `L09-02c` hộp | Hộp là cụm danh từ, không phát biểu nhiệm vụ | Mặt trang | "Xác định khi nào…" | đã sửa ở R1 | chấp nhận |
| nhẹ | `L09-01b` | "$S_t$ là quan sát $O_t$" đảo nghĩa | Mặt trang | "quan sát $O_t$ của Bài 08 trùng trạng thái $S_t$" | đã sửa ở R1 (bỏ "nhận" ở hàng $R_{t+1}$ để giữ 60 âm tiết) | chấp nhận |
| nhẹ | `L09-01d` | $q_\pi$ theo $G_t\mid S_t$ nhưng trích 03.16; Jensen không nói vector | Mặt trang | $G_0\mid S_0$; $f:\mathbb R^m\to\mathbb R$; Bổ đề 03.20(d) | đã sửa ở R1 (mặt trang, nguồn ghi chú diễn giả, nhóm tiên quyết của ghi chú bài giảng) | chấp nhận |
| nhẹ | `L09-01c` nguồn | Thiếu Định nghĩa 08.10 | Dòng Nguồn | Thêm | đã sửa ở R1 | chấp nhận |
| nhẹ | `L09-01c`, `L09-01d`, `L09-02` | Thiếu tên tiếng Anh ở lần dùng đầu | Mặt trang | Thêm ngoặc | đã sửa ở R1: mục tiêu (target), hàm mất mát (loss), dừng gradient (stop-gradient), mạng trực tuyến (online network), mạng mục tiêu (target network), lợi tức (return), độ chệch của phép cực đại (maximization bias, ở mục tiêu 1 của `L09-02`, lần dùng đầu). "Chính sách tham số hóa (parameterized policy)": lần đầu trên mặt trang là tên mục trong `L09-02b`, phải trùng tên trang tiêu đề mạch 4; tên tiếng Anh đặt trong ghi chú diễn giả `L09-02b` và trên trang nội dung đầu của mạch 4 ở bước đó | chấp nhận |
| nhẹ | `L09-02` ghi chú diễn giả | 153 âm tiết > 150 | Đếm token | Bỏ câu cuối | đã sửa ở R1; mọi ghi chú diễn giả mạch 1 ≤ 135 âm tiết theo `dens.py` (`L09-01` 133, `L09-01b` 131, `L09-01c` 95, `L09-01d` 96, `L09-02` 135, `L09-02b` 118, `L09-02c` 133) | chấp nhận |
| nhẹ | ghi chú bài giảng, đoạn đọc hình | Đọc $\mathbb E[\hat g]=\nabla J$ không điều kiện; "Hình dưới đặt…" | Đoạn đọc hình | "dưới các giả thiết của Mục 6"; "Hình dưới gồm…" | đã sửa ở R1 | chấp nhận |
| nhẹ | ghi chú bài giảng, bảng ký hiệu | $\alpha$ "bước học" không nói quan hệ với $\eta$ của Bài 08 | Định nghĩa 08.16 | Ghi vai trò | đã sửa ở R1; thêm hàng $\nu^\pi_\gamma$ | chấp nhận |
| nhẹ | ghi chú diễn giả `L09-02c`, `L09-02b` | Câu số trang nguồn lặp dòng Nguồn; "chệch lên" không điều kiện | Ghi chú diễn giả | Thay câu | đã sửa ở R1 | chấp nhận |

Kiểm sau R1 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mạch 1 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang; đáy `L09-01` 455, `L09-01b` 583, `L09-01c` 651, `L09-01d` 519, `L09-02` 384, `L09-02b` 560, `L09-02c` 630 px; đã xem ảnh 1600×900 của `L09-01`, `L09-01c`, `L09-02c`. Mặt trang (`dens.py`): `L09-01` 65 (bìa, ngoại lệ), `L09-01b` 60, `L09-01c` 40, `L09-01d` 35, `L09-02` 71, `L09-02b` 39, `L09-02c` 83 (ngoại lệ 1,38 lần trần; `dens.py` đếm 79 vì bốn từ nối bằng dấu cách không ngắt). 43 `data-slide-id` duy nhất, 7 section ngoài, `#/1`…`#/7` đúng. Viewer ghi chú bài giảng: 17/17 khối `:::`, 554 biểu thức KaTeX, 0 `.katex-error`, 0 lỗi console, mã chủ đề không trùng. Ghi chú bài giảng 7 952 từ theo `wc -w`. `git diff --check` sạch. `no-ai-slop` (Edit) trên mọi câu mới của R1: không đối lập nhị phân, không chủ ngữ là tài liệu, không câu hỏi tu từ; đạt. Trạng thái: chờ điều phối viên duyệt.

### Bước mạch 2 (S7–S11, biên tập viên)

Căn cứ: kế hoạch D1 mạch 2, các phát hiện CT P03–P06, SV (mục 2, bảng phát hiện), TH (bảng phát hiện, Kiểm tra số mục 1–2), R1 (các mục hoãn về `L09-03`, `L09-04`). Mạch 1 đã commit (`4b58f48`, `7bc43f1`).

| bước | trang | thay đổi | âm tiết mặt trang trước → sau | dòng sau | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|---|
| S7 | `L09-M2T` (mới) | Trang tiêu đề mạch 2, `id="mach-2"`, khuôn `L08-M2T`: "2. Độ chệch của phép cực đại"; dòng dẫn "Muốn dùng phép cực đại trong mục tiêu bootstrap, phải biết nó lệch bao nhiêu khi ước lượng có nhiễu."; bốn từ khóa; ghi chú khoảng 91 âm tiết | — → dòng dẫn 20, từ khóa 17 | 2 | Câu dẫn trần thuật, không câu hỏi; ghi chú không lấy tài liệu làm chủ ngữ ("Nhiệm vụ ở đây là…"); đạt | chờ điều phối viên duyệt |
| S8 | `L09-03` | "DQN ổn định hơn nhưng vẫn có sai lệch" → "Phép cực đại trong mục tiêu DQN"; "Nhu cầu:" kèm công thức $y_i$ tại chỗ; "Ví dụ." CartPole, cận $100$; hình mới `cartpole-overestimate.svg` thay `dqn-stability.svg` (bỏ câu khẩu hiệu, "Replay", "đích"); "Lưu ý:" con số gộp nhiều nguồn sai số; bỏ quy ước $O=S$ lặp | 45 → 43 | 4 + hình | Bỏ tiêu đề đối lập "…nhưng…", "Bài này giả sử…"; đạt | chờ điều phối viên duyệt |
| S9 | `L09-04` | "Phép cực đại chọn cả giá trị lẫn nhiễu (maximization bias)" → "Độ chệch của phép cực đại"; $q_a$ cho giá trị đúng; "Trực quan."; đại lượng cần đo; hình chuyển xuống `L09-05` | 13 → 43 | 5 | Bỏ "sai lệch"; câu trực quan có cơ chế, không khẩu hiệu; đạt | chờ điều phối viên duyệt |
| S10 | `L09-05` | "Ví dụ Rademacher" → "Ví dụ: hai hành động có nhiễu ±1"; dữ kiện, "Tính", hình bốn cặp vẽ lại, dòng tính, "Diễn giải:" | 24 → 28 | 4 + hình | Bỏ câu kết "Ví dụ này chứng minh…" trong ghi chú; đạt | chờ điều phối viên duyệt |
| S11 | `L09-06` | "Bất đẳng thức kỳ vọng" → "Độ chệch của phép cực đại không âm"; "Mệnh đề." có giả thiết ($\mathcal A$ hữu hạn, khả tích); "Chứng minh." một dòng, Jensen phát biểu lại tại chỗ; "Ý nghĩa:" dấu bằng khi và chỉ khi; "Câu hỏi:" và "Lời giải:" | 35 → 57 | 6 hiển thị | Bỏ "Đây là Jensen vì…", chỉ dẫn giảng viên "Không phát biểu…"; đạt | chờ điều phối viên duyệt |

SVG: `cartpole-overestimate.svg` (mới; trục số, hình tròn và hình thoi phân biệt bằng hình dạng và nhãn, không chỉ màu; phông không chân; `role="img"`, `title`, `desc`). `maximization-bias.svg` vẽ lại (dấu trừ chuẩn, tọa độ ngăn bằng dấu chấm phẩy, bỏ chấm màu không chú giải và câu khẩu hiệu, ba khung có cực đại dương viền đậm). `dqn-stability.svg` không còn dùng trong deck và ghi chú; giữ tệp, chờ điều phối viên quyết xóa hay giữ.

Ghi chú bài giảng, `## 2. Độ chệch của phép cực đại` viết lại: đoạn mở (kết quả kế thừa Định nghĩa 08.4, bài toán CartPole); "Phép cực đại trong mục tiêu DQN" (hai vai của phép cực đại; Q-learning bảng với giả thiết Định lý 06.21; Sutton và Barto §6.7, Ví dụ 6.7; Ví dụ 09.1 CartPole có kiểm tra $0{,}99^{500}$; hình trục số có đoạn đọc hình; nhầm lẫn gán toàn bộ độ vượt cho phép cực đại); "Độ chệch của phép cực đại và bất đẳng thức kỳ vọng" (trực quan; Ví dụ 09.2 có bảng bốn cặp; hình có đoạn đọc; Định nghĩa 09.1 $\beta$; Mệnh đề 09.2 bốn phần, chứng minh ba bước có $\square$, cách khác không dùng Jensen; vai trò hai giả thiết với phản ví dụ Cauchy và ước lượng lệch $-1$; Ví dụ 09.3 khoảng cách $0{,}5$ cho $0{,}375$, khoảng cách $3$ cho $0$; Nhận xét 09.3 bốn nhầm lẫn; "Trong thực hành."; Bài tập 09.1 có gợi ý và lời giải: $q=(1;\,0)$ cho $\beta=0{,}25$; đoạn kết nối sang Mục 3). Bảng ký hiệu thêm hàng $q_a$, $\beta$. Giáo trình tham khảo: Sutton và Barto (2018), §6.7 (mở bằng nhiều hành động giá trị đúng $0$, Ví dụ 6.7). Số liệu đã tính lại: $\tfrac14(-1+1+1+1)=\tfrac12$; $\tfrac14(-0{,}5+1+1{,}5+1{,}5)=0{,}875$; $\tfrac14(0+1+2+2)=1{,}25$; $(1-0{,}99^{500})/0{,}01\approx99{,}34$. Độ dài ghi chú 10 022 từ theo `wc -w`. `no-ai-slop` trên mục mới: sửa "Mục này xây dựng…", "Mục 1 đã chỉ ra…" (tài liệu làm chủ ngữ); bỏ một câu không có căn cứ về trạng thái đầu của CartPole; không câu hỏi tu từ, không gạch ngang dài; đạt.

Kiểm sau bước mạch 2 (Playwright Chromium, `http://127.0.0.1:8799`): `L09-02c`, `L09-M2T`, `L09-03`–`L09-06`, `L09-07` ở 1600×900 và 390×844: 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang; đáy `L09-M2T` 364, `L09-03` 649, `L09-04` 457, `L09-05` 647, `L09-06` 576 px; `L09-07` 750 px (tràn có từ C0, sửa ở mạch 3). Đã xem ảnh 1600×900 của năm trang mạch 2. 44 `data-slide-id` duy nhất; `#/2` và mục 2 của `L09-02b` mở `L09-M2T`. Viewer: 26/26 khối `:::`, 719 biểu thức KaTeX, 0 `.katex-error`, mã chủ đề không trùng. `git diff --check` sạch. Trạng thái: chờ điều phối viên duyệt.

### Rà lại mạch 2 (bước R2)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 2 (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R2 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R2-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 5 trung bình, 7 nhẹ; điều phối viên duyệt mạch 2 (diff, `check.py` hai cỡ, ảnh năm trang) và chấp nhận toàn bộ, kèm các chốt ghi ở cột "quyết định".

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|---|
| trung bình | `L09-06` "Ý nghĩa:", ghi chú diễn giả; ghi chú bài giảng (đoạn sau phản ví dụ, Nhận xét 09.3 mục 3, đoạn kết mục) | Điều kiện dấu bằng không chính xác khi hòa hoặc nhiều hành động cùng kỳ vọng lớn nhất; $b^*$ chưa định nghĩa trong ghi chú diễn giả | "khi và chỉ khi hành động có kỳ vọng lớn nhất luôn thắng" | Điều kiện theo $b^*$ | đã sửa ở R2: mặt trang "bằng nhau khi và chỉ khi có $b^*\in\arg\max_aq_a$ với $\widehat Q_{b^*}=\max_a\widehat Q_a$ hầu chắc chắn"; ghi chú diễn giả định nghĩa $b^*$, nói hòa vẫn tính là đạt cực đại; ghi chú bài giảng: Mệnh đề 09.2(c) thêm câu về hòa và $b^*\in\arg\max_aq_a$ khi không chệch, ba chỗ (đoạn sau phản ví dụ, Nhận xét 09.3 mục 3, đoạn kết mục) và đoạn giải thích Ví dụ 09.2, Ví dụ 09.3(ii) viết theo cùng điều kiện | chấp nhận (điều kiện $b^*\in\arg\max_aq_a$) |
| trung bình | `L09-03`, `cartpole-overestimate.svg` | Chỉ nêu cận của lợi tức; kết luận cần cận của giá trị đúng của bài toán không giới hạn bước | "nên mọi lợi tức nhỏ hơn 100"; nhãn "cận trên của mọi lợi tức" | Cận cho cả lợi tức và giá trị đúng | đã sửa ở R2: "mọi lợi tức và mọi giá trị đúng không vượt $\sum_{k\ge0}\gamma^k=100$"; nhãn hình "cận 1/(1 − γ) = 100", "lợi tức $G_0$ = 99,3 (cắt ở bước 500)"; `desc`, `alt`, chú thích ảnh trong ghi chú bài giảng sửa theo; ghi chú diễn giả thêm câu bootstrap qua bước cắt ngắn; 48 âm tiết | chấp nhận |
| trung bình | mạch 2, bước ứng dụng | Bước ứng dụng không có trên mặt trang | Bảng hành trình | Thêm lên `L09-05` | đã sửa ở R2: dòng "Với $q=(0{,}5;\,0)$, độ chệch $0{,}375$; với $q=(3;\,0)$, độ chệch $0$." trên `L09-05` (đáy 691 px, 34 âm tiết); ghi chú diễn giả `L09-06` thêm ứng dụng vào $Q_{\theta^-}(S'_i,a)$; bảng hành trình sửa | chấp nhận (đặt ở `L09-05` vì `L09-06` đã đủ dòng) |
| trung bình | ghi chú bài giảng | $q_*$ dùng mà không nhắc lại | "$Q_t\to q_*$"; "$q_*(S'_i,a)$" | Nhắc lại Định nghĩa 04.19; thêm hàng bảng ký hiệu | đã sửa ở R2 (nhóm "Chính sách, lợi tức và giá trị hành động" của Kiến thức tiên quyết; hàng $q_*(s,a)$) | chấp nhận |
| trung bình | `L09-07`, `L09-08` | Tràn, tiêu đề câu, "đích", "online", "target" trần; đầu vào của mạch 2 chưa được nhận | Ảnh `w-L09-07` đáy 750 | Sửa ở bước mạch 3 | mở (bước mạch 3) | chấp nhận (chuyển bước mạch 3) |
| nhẹ | `L09-04` | Tiêu đề trùng tên mạch; định nghĩa không nhãn | `L09-M2T` h2 = `L09-04` h2 | "Nhiễu của hành động được chọn"; "Định nghĩa." | đã sửa ở R2 | chấp nhận |
| nhẹ | `L09-05`, `maximization-bias.svg` | Hình không ghi cặp là $(\widehat Q_1;\widehat Q_2)$ | SVG | Thêm nhãn | đã sửa ở R2: dòng "cặp (Q̂₁; Q̂₂), mỗi cặp xác suất 1/4" phía trên bốn khung, bỏ dòng xác suất lặp trong từng khung, `desc` sửa theo | chấp nhận |
| nhẹ | `L09-05` ghi chú diễn giả | "cách xa" không có ngưỡng; câu chỉ dẫn tài liệu | Ghi chú diễn giả | Nêu ngưỡng $2$ và số $0{,}375$ | đã sửa ở R2 | chấp nhận |
| nhẹ | `L09-M2T`, `L09-03` | "lệch" lẫn với "chệch" | Dòng dẫn, "Nhu cầu:" | "chệch" | đã sửa ở R2 | chấp nhận |
| nhẹ | ghi chú bài giảng, phản ví dụ Cauchy | Vế trái vẫn có nghĩa mở rộng | "cả hai vế của (a) không có nghĩa" | "vế phải của (a) không xác định" | đã sửa ở R2 | chấp nhận |
| nhẹ | ghi chú bài giảng, đoạn kết mục 2 | Dấu hai chấm tiết lộ; câu khái quát | "Chứng minh chỉ dùng một điều: …" | Câu có điều kiện | đã sửa ở R2 | chấp nhận |
| nhẹ | ghi chú bài giảng, đoạn trực quan | Siêu văn bản | "Đây chưa phải một phát biểu chính xác; ví dụ sau cho một con số." | Xóa | đã sửa ở R2 | chấp nhận |

Hình: `img/lec-09/dqn-stability.svg` **xóa vì không còn dùng** (quyết định của điều phối viên; xóa bằng `rm`, không dùng git; `grep` trên deck và ghi chú bài giảng không còn tham chiếu); `outline.md` mục Tài sản SVG và `storyboard.md` mục `L09-03` ghi theo.

Kiểm sau R2 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mạch 2 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang; đáy `L09-M2T` 364, `L09-03` 650, `L09-04` 457, `L09-05` 691, `L09-06` 585 px; đã xem ảnh 1600×900 của `L09-03`, `L09-05`, `L09-06`. Âm tiết mặt trang: 37 (dẫn và khóa), 48, 46, 34, 50; ghi chú diễn giả 91, 142, 83, 102, 131. `#/2` mở `L09-M2T`. Viewer: 26/26 khối, 742 biểu thức KaTeX, 0 `.katex-error`. Ghi chú bài giảng 10 143 từ. `git diff --check` sạch. `no-ai-slop` (Edit) trên câu mới của R2: đạt. Trạng thái: chờ điều phối viên duyệt.

### Bước mạch 3 (S12–S23, biên tập viên)

Căn cứ: kế hoạch D1 mạch 3, D2, D3; phát hiện CT P07–P16, G12; SV (mục 2 và bảng phát hiện về `L09-07`–`L09-15`); TH (đích, argmax tại trạng thái kết thúc, $y^{\mathrm{DDQN}}\le y^{\mathrm{DQN}}$, "bảng thứ nhất", "$Z=0$" ở `L09-12`, chệch âm); R2 (mục hoãn về `L09-07`, `L09-08`). Mạch 2 đã commit (`2cc2fbf`, `f77212f`).

| bước | trang | thay đổi | âm tiết trước → sau | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|
| S12 | `L09-M3T` (mới) | Trang tiêu đề mạch 3, `id="mach-3"`, dòng dẫn theo CT §2.2, bốn từ khóa | — → dẫn 23, khóa 18 | ghi chú không lấy tài liệu làm chủ ngữ; đạt | chờ điều phối viên duyệt |
| S13 | `L09-06b` (mới) | "Ví dụ: hai bản ước lượng độc lập": "Nhu cầu:", dữ kiện, phép chọn và báo, hình `double-estimator.svg`, "Diễn giải:" | — → 37 | đạt | chờ điều phối viên duyệt |
| S14 | `L09-07` | "Double DQN tách chọn và đánh giá" → "Mục tiêu Double DQN"; mở bằng giới hạn của DQN; dạng mặt nạ với $\operatorname{sg}$; "Lưu ý:" dạng từng trường hợp; hình vẽ lại; hết tràn (750 → 608 px) | 16 → 27 | bỏ "online" trần, "vô nghĩa"; đạt | chờ điều phối viên duyệt |
| S15 | `L09-08` | "Hai đích có thể khác nhau" → "Ví dụ: một mẫu chuyển, hai mục tiêu"; hình có số; "Diễn giải:" | 12 + bảng → 24 | bỏ "đích", "target:", "online:"; đạt | chờ điều phối viên duyệt |
| S16 | `L09-09` | "Miền, kích thước và đường gradient" → "Thuật toán Double DQN"; năm bước; kích thước mảng | 16 → 44 | bỏ backtick `sg` trong ghi chú; đạt | chờ điều phối viên duyệt |
| S17 | `X01` | "Bài tập: sai lệch và hai đích" → "Bài tập: mục tiêu DQN và Double DQN"; "Câu hỏi:" tự đủ, (a) $Z=0$, (b) $Z=1$; "Lời giải:" từng bước | 23 → 29 | bỏ câu phân tuyến trong ghi chú; đạt | chờ điều phối viên duyệt |
| S18 | `L09-10` | "Hai mạng vẫn có tương quan" → "Phạm vi của Double DQN"; bỏ hộp lời khuyên chung; ví dụ chệch âm | 58 → 60 | bỏ "Replay" trần, câu chỉ dẫn "Dùng lại bài tập…"; đạt | chờ điều phối viên duyệt |
| S19 | `L09-11` | "Double Q-learning dùng hai bảng riêng" → "Double Q-learning dạng bảng"; "Nhu cầu:"; hình vẽ lại; "bảng kia đánh giá" thay "bảng thứ nhất" | 27 → 36 | đạt | chờ điều phối viên duyệt |
| S20 | `L09-13` | "Áp dụng cập nhật chéo" → "Ví dụ: một cập nhật Double Q-learning"; số ví dụ A; hình `double-q-example.svg`; chuyển trước `L09-12` | 3 → 25 | bỏ nhãn quy trình "chu trình rút gọn"; đạt | chờ điều phối viên duyệt |
| S21 | `L09-12` | "Cập nhật chéo theo trạng thái kết thúc" → "Thuật toán Double Q-learning"; thuật toán đầy đủ; bỏ "$Z=0$" như phép gán | 16 → 34 | đạt | chờ điều phối viên duyệt |
| S22 | `L09-14` | "Hai cách tách không đồng nhất" → "So sánh DQN, Double DQN và Double Q-learning"; ba cột, năm tiêu chí | 26 → 55 | dùng "mạng trực tuyến", "bộ nhớ phát lại"; đạt | chờ điều phối viên duyệt |
| S23 | `L09-15` | "Kiểm tra phần học giá trị" → "Bài tập: Double DQN và Double Q-learning"; "Lời giải:" fragment; dòng "Giới hạn chung:" | 38 → 57 | bỏ "Đáp án", câu "Sau đó chuyển sang…"; đạt | chờ điều phối viên duyệt |

Số liệu đã tính lại: $1+0{,}9\cdot5=5{,}5$; $1+0{,}9\cdot4=4{,}6$; $1+0{,}8\cdot7=6{,}6$; $1+0{,}8\cdot2=2{,}6$; $4+0{,}1\cdot0{,}6=4{,}06$; nhánh kia $1+0{,}9\cdot3=3{,}7$, $3+0{,}1\cdot0{,}7=3{,}07$; ước lượng kép với $q=(0;0)$ cho $0$; với $q=(0{,}5;0)$, $\Pr(a^*=1)=\tfrac34$, $\tfrac34\cdot0{,}5=0{,}375$, độ chệch $-0{,}125$.

SVG: mới `double-estimator.svg`, `ddqn-example.svg`, `double-q-example.svg`; vẽ lại `dqn-vs-ddqn.svg` (hai hàng, phông không chân, nhãn tiếng Việt, không tràn), `double-q-cross-update.svg` (nhãn chọn ngẫu nhiên $1/2$, mũi tên đủ đầu, nhánh dưới viền nét đứt). Tín hiệu không chỉ dựa vào màu: khung vuông, viền ellip nét đứt, hình thoi, viền liền và viền đứt.

Ghi chú bài giảng, `## 3. Tách chọn và đánh giá` viết lại, thay ba mục cũ "Đích Double DQN", "Phạm vi tác dụng của Double DQN", "Double Q-learning dạng bảng": đoạn mở (kế thừa Mệnh đề 09.2, nhu cầu tách); "Ước lượng kép" (`lec-09-topic-17`, mới; trực quan, Ví dụ 09.4 có hình, Mệnh đề 09.4 bốn phần với chứng minh ba bước, ba phản ví dụ khi bỏ giả thiết, Ví dụ 09.5 chệch âm $-0{,}125$, câu hỏi thảo luận nguồn tr. 21 về 4-DQN/8-DQN); "Mục tiêu và thuật toán Double DQN" (Ví dụ 09.6 có hình, $y^{\mathrm{DDQN}}\le y^{\mathrm{DQN}}$, Thuật toán 09.5 đủ đầu vào, đầu ra, khởi tạo, năm bước, kích thước, chi phí; dạng từng trường hợp cho cùng giá trị; "Trong thực hành." nối bài thực hành Bài 08 mục 14–15); "Phạm vi của Double DQN" (Nhận xét 09.6; "Trong thực hành." với số Lunar Lander mục 15.4); "Double Q-learning dạng bảng" (Ví dụ 09.7 có hình, Thuật toán 09.7, bảng so sánh, Nhận xét 09.8 bốn nhầm lẫn, Bài tập 09.2 có gợi ý và lời giải, đoạn kết nối sang Mục 4). Bảng ký hiệu thêm $\widehat Q^A_a$, $\widehat Q^B_a$, $\epsilon_{\mathrm{exp}}$; bản đồ chủ đề và "Bảy phần" thêm `lec-09-topic-17`. Giáo trình tham khảo: Sutton và Barto (2018), §6.7 (học kép, Double Q-learning); van Hasselt (2010); van Hasselt, Guez và Silver (2016). Độ dài 12 748 từ theo `wc -w`. `no-ai-slop`: sửa một câu không có căn cứ về chi phí của mạng thứ hai và một dòng kiểm tra lời giải mơ hồ; không câu hỏi tu từ, không chủ ngữ là tài liệu; đạt.

Phát hiện ngoài phạm vi ghi tệp: notebook Bài 08 (mục 15.2) dẫn tên mục cũ của ghi chú Bài 09 ("Sai lệch cực đại và ví dụ Rademacher", "Đích Double DQN"); các mục này nay là "Độ chệch của phép cực đại và bất đẳng thức kỳ vọng" và "Mục tiêu và thuật toán Double DQN". Chờ điều phối viên quyết sửa notebook (thuộc `materials/lec-08`).

Kiểm sau bước mạch 3 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mười hai trang mạch 3 và hai trang kề, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn; đáy `L09-M3T` 364, `L09-06b` 685, `L09-07` 608, `L09-08` 640, `L09-09` 606, `X01` 412, `L09-10` 344, `L09-11` 560, `L09-13` 694, `L09-12` 613, `L09-14` 559, `L09-15` 440 px. Đã xem ảnh 1600×900 của mười hai trang. 46 `data-slide-id` duy nhất; `#/3` và mục 3 của `L09-02b` mở `L09-M3T`. Viewer: 37/37 khối, 949 biểu thức KaTeX, 0 `.katex-error`, mã chủ đề không trùng. `git diff --check` sạch. Trạng thái: chờ điều phối viên duyệt.

### Rà lại mạch 3 (bước R3)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 3 (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R3 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R3-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 8 trung bình, 8 nhẹ; điều phối viên duyệt mạch 3 (`check.py`, ảnh `L09-06b`, `L09-09`, `L09-13`, `L09-14`; đối chiếu notebook ô 80) và chấp nhận toàn bộ, kèm các chốt ở cột "quyết định".

| mức độ | trang chiếu | vấn đề | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|
| trung bình | `L09-09`; Thuật toán 09.5 | $T$ dùng cho ngân sách bước, trùng $T$ bước kết thúc lượt; $\mathcal D$, $N_{\mathrm{start}}$, $F$, $\epsilon_{\mathrm{exp}}$ không được gọi tên | $t_{\mathrm{end}}$; gọi tên tại chỗ | đã sửa ở R3 (mặt trang, ghi chú diễn giả, Thuật toán 09.5 và câu giải thích $t_{\mathrm{end}}$ trong ghi chú bài giảng); 58 âm tiết, không cần tách trang | chấp nhận ($t_{\mathrm{end}}$) |
| trung bình | `L09-14`; bảng trong ghi chú bài giảng | Hàng "chệch lên" mạnh hơn kết quả, thiếu giả thiết | Hàng "độ chệch của mục tiêu" theo đề xuất | đã sửa ở R3 ở cả hai nơi | chấp nhận |
| trung bình | `L09-06b`, `double-estimator.svg` | Nhãn là kỳ vọng có điều kiện; "Diễn giải:" thiếu hai giả thiết, không tự đủ; thiếu xác suất $1/2$; đáy 685 px | Nhãn "𝔼[Q̂ᴮ_a* \| cặp A] = 0"; dữ kiện; "Diễn giải:" mới | đã sửa ở R3 (SVG, `desc`, `alt`, chú thích ảnh và câu đọc hình ghi chú bài giảng); hình thấp hơn; đáy 654 px | chấp nhận |
| trung bình | mạch 3, bước hình thức | Mệnh đề ước lượng kép không có trang kết quả | Thêm `L09-06c` | đã sửa ở R3: `L09-06c` "Ước lượng kép không chệch lên" sau `L09-06b`; dòng chệch âm chuyển từ `L09-10` sang "Ý nghĩa:" của `L09-06c`; tên tiếng Anh "double estimator" đặt ở đây; storyboard, outline, bảng hành trình cập nhật | chấp nhận (thêm `L09-06c`, tránh lặp với `L09-10`) |
| trung bình | `L09-15`, ghi chú diễn giả, đoạn kết Mục 3, ghi chú `L09-M3T` | "Tất định / không biểu diễn được chính sách ngẫu nhiên" không đúng nguyên văn khi có $\epsilon$-tham lam | Phân biệt xác suất được học với ngẫu nhiên cố định | đã sửa ở R3 (mặt trang "chọn bằng $\arg\max_aQ$ thì không học xác suất hành động; mỗi bước cần $\max$ trên $\mathcal A$"; ghi chú diễn giả, ghi chú `L09-M3T`, đoạn kết Mục 3 nêu $\epsilon_{\mathrm{exp}}$-tham lam chỉ thêm ngẫu nhiên cố định) | chấp nhận |
| trung bình | ghi chú bài giảng | "Mục này xét…", "Mục con sau…" | Chủ ngữ "chúng ta" | đã sửa ở R3; `grep` toàn ghi chú không còn "Mục này", "Mục con", "Phần này", "Chương này" | chấp nhận |
| trung bình | notebook Bài 08, mục 15.2 (ô 71, 73) | Dẫn tên mục cũ của ghi chú Bài 09, dùng "đích" | Commit `fix(materials-08)` riêng | mở; không sửa ở R3 | chấp nhận (điều phối viên giao riêng sau mạch 3) |
| trung bình | `L09-16`, `L09-17` | Tràn, thông điệp gộp trạng thái sai, "return", "kernel" | Sửa ở bước mạch 4 | mở (bước mạch 4) | chấp nhận (chuyển bước mạch 4) |
| nhẹ | ghi chú diễn giả `L09-M3T` | 107 âm tiết > 100 | Rút | đã sửa ở R3 (khoảng 91) | chấp nhận |
| nhẹ | `L09-10` dòng 4 | "hội tụ vẫn như DQN" mơ hồ | "việc thiếu bảo đảm hội tụ" | đã sửa ở R3 | chấp nhận |
| nhẹ | `L09-10` | "Bộ ước lượng kép" thiếu tên tiếng Anh | Thêm ở lần dùng đầu | đã sửa ở R3 (ở `L09-06c`) | chấp nhận |
| nhẹ | `double-q-example.svg` | "(cập nhật)" gợi ý ô tại $S'$ bị cập nhật | "bảng chọn" | đã sửa ở R3 | chấp nhận |
| nhẹ | `L09-15` Lời giải | (3) thiếu nối với giả thiết; (4) thiếu "một ô" | Sửa | đã sửa ở R3 ((4) "một ô của một bảng"; nối giả thiết của (3) đặt trong ghi chú diễn giả để giữ 58 âm tiết) | chấp nhận |
| nhẹ | ghi chú bài giảng Ví dụ 09.4 | $\mathbb E[\varepsilon^B_{a^*}]$ dễ lẫn | $\mathbb E[\varepsilon^B_b]\big|_{b=a^*}$ | đã sửa ở R3 | chấp nhận |
| nhẹ | ghi chú bài giảng sau phản ví dụ của Mệnh đề 09.4 | Bước 1 cũng dùng khả tích | Sửa câu | đã sửa ở R3 | chấp nhận |
| nhẹ | ghi chú bài giảng sau Ví dụ 09.5; đầu "Ước lượng kép" | Bước nhảy lập luận; câu siêu văn bản | Viết lại; xóa | đã sửa ở R3 | chấp nhận |

Kiểm sau R3 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mười ba trang mạch 3, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn; đáy `L09-06b` 654, `L09-06c` 447, `L09-09` 614, `L09-10` 316, `L09-14` 654, `L09-15` 446 px; đã xem ảnh 1600×900 của `L09-06b`, `L09-06c`, `L09-09`, `L09-14`, `L09-15`. 47 `data-slide-id` duy nhất; `#/3` mở `L09-M3T`. Viewer: 37/37 khối, 954 biểu thức KaTeX, 0 `.katex-error`. Ghi chú bài giảng 12 803 từ. `git diff --check` sạch. `no-ai-slop` (Edit) trên câu mới của R3: đạt. Trạng thái: chờ điều phối viên duyệt.

### Sửa tham chiếu trong bài thực hành Bài 08 (mục 7 của R3)

`materials/lec-08/thuc-hanh-dqn-cartpole-lunarlander-flappybird.ipynb`: ba dòng `source` của ba ô Markdown (mục 15.2, ô 71 và 73; mục tài liệu tham khảo, ô 96) đổi tên mục cũ của ghi chú Bài 09 ("Sai lệch cực đại và ví dụ Rademacher", "Đích Double DQN", ví dụ "Đối chiếu hai đích") sang tên và số hiện hành (Mục 2, Định nghĩa 09.1, Mệnh đề 09.2; Mục 3, Thuật toán 09.5; Ví dụ 09.6 "Một mẫu chuyển, hai mục tiêu"), bỏ "đích". Ghi bằng `json` (`indent=1`, `ensure_ascii=False`, kết thúc bằng xuống dòng; ghi lại không đổi gì cho đúng từng byte tệp gốc trước khi sửa); `git diff --stat` cho 3 dòng thêm, 3 dòng bớt, không ô mã hay output nào đổi. Trạng thái: chờ điều phối viên duyệt; commit riêng `fix(materials-08)`.

### Bước mạch 4 (S24–S29, biên tập viên)

Căn cứ: kế hoạch D1 mạch 4, D4 (sửa `L09-16`, `aliased-grid-policy.svg`, ghi chú bài giảng, `note-for-author.md`); CT P17–P20; SV (`L09-16` chặn bàn giao, `L09-19` tràn, nhãn SVG); TH (nghiêm trọng về gộp trạng thái); R3 mục 8. Nguồn tr. 22–29 đã xem bằng `pdftoppm` (ảnh trong scratchpad, không nhúng). Mạch 3 đã commit (`b30cc10`, `39fd5c1`).

| bước | trang | thay đổi | âm tiết trước → sau | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|
| S24 | `L09-M4T` (mới) | Trang tiêu đề mạch 4 | — → dẫn 18, khóa 13 | đạt | chờ điều phối viên duyệt |
| S25 | `L09-16` | Tách; trang vấn đề với lưới nguồn, chính sách tất định kẹt; hết tràn (846 → 634 px) | 75 → 47 | bỏ câu khẩu hiệu SVG "Trộn hành động không khôi phục…", câu phủ định "không phải hệ quả của Double DQN"; đạt | chờ điều phối viên duyệt |
| S26 | `L09-16b` (mới) | Ví dụ chính sách ngẫu nhiên $\tfrac12$, $h_2=4$; "Lưu ý:" Định lý 04.25 có điều kiện | — → 56 | đạt | chờ điều phối viên duyệt |
| S27 | `L09-17` | "Chính sách tham số hóa": Nhu cầu hai lý do, Định nghĩa | 40 → 51 | bỏ "kernel", "Không cần đưa sigma-đại số lên mặt trang" (chỉ dẫn), "return"; đạt | chờ điều phối viên duyệt |
| S28 | `L09-18` | "Ví dụ: phân phối hành động" với số liệu nguồn; hình vẽ lại | 25 → 27 | đạt | chờ điều phối viên duyệt |
| S29 | `L09-19` | Bảng softmax/Gaussian; "Câu hỏi:", "Lời giải:"; dòng đầu ra cho mạch 5; hết tràn (792 → 596 px) | 30 → 49 | bỏ "giao diện", "Đáp án"; đạt | chờ điều phối viên duyệt |

Số liệu đã tính lại: lưới năm ô, chính sách tất định Đông ở hai ô xám: $h_3=1$, $h_2=2$, $h_1=3$, $h_4=h_5=\infty$; Tây: đối xứng. Chính sách ngẫu nhiên với xác suất Đông $p$: $h_2=p\cdot2+(1-p)(2+h_2)\Rightarrow h_2=2/p$, $h_4=2/(1-p)$; trung bình $1/(p(1-p))$ nhỏ nhất tại $p=\tfrac12$: $h_2=h_4=4$, $h_1=h_5=5$; theo ô $h_2=h_4=2$. Bài tập 09.3: $p=0{,}8$ cho $2{,}5$, $10$, trung bình $6{,}25$. Softmax hai hành động $\theta=(\ln2;0)$: $(\tfrac23;\tfrac13)$; phân loại $(0{,}1;0{,}2;0{,}2;0{,}5)$ với $\theta=\ln$ các xác suất. Bộ số chọn theo nguồn: số bước kỳ vọng (phần thưởng không được nguồn cho); bộ số của TH (hành lang ba ô, $\gamma=0{,}9$) là một môi trường khác nguồn nên không dùng.

SVG: `aliased-grid-policy.svg` vẽ lại theo nguồn tr. 23 (lưới hai hàng năm cột, hai ô xám ghi $x=1$, X dưới ô 1 và ô 5, \$ dưới ô 3; chính sách tất định Đông ở hai ô xám, vòng kẹt nét đứt); `aliased-grid-stochastic.svg` mới (Đông/Tây $\tfrac12$ ở ô xám, $h_2=h_4=4$); `policy-distributions.svg` vẽ lại (cột $0{,}1;0{,}2;0{,}2;0{,}5$ có số; Gaussian với $\mu$, $a_{\min}$, $a_{\max}$, đuôi ngoài miền tô màu và ghi chữ). Phông không chân; tín hiệu không chỉ dựa vào màu (nét đứt, chữ ghi).

Ghi chú bài giảng, `## 4. Chính sách tham số hóa` viết lại: đoạn mở (giới hạn của Mục 3, câu hỏi nghiên cứu trả lời ngay trong mục); "Giới hạn của chính sách tham lam theo $Q$" (mô tả lưới nguồn đầy đủ, hình, Ví dụ 09.8 tất định với cả hai hướng, trực quan, hình, Ví dụ 09.9 với $p$ tổng quát và $p=\tfrac12$ tối ưu, Nhận xét 09.9 đối chiếu Định lý 04.25 có điều kiện, hành động liên tục); "Chính sách tham số hóa" (Định nghĩa 09.10, hai vai điều khiển và học, $\theta$ đổi vai, mật độ; Ví dụ 09.10 bốn hành động với $\theta$ cho phân phối phân loại; hình; Định nghĩa 09.11 softmax kèm ví dụ $\theta=(\ln2;0)$; Định nghĩa 09.12 Gaussian, miền bị chặn; bảng so sánh; Nhận xét 09.13 bốn nhầm lẫn, gồm "chính sách ngẫu nhiên không khôi phục thông tin trạng thái"; "Trong thực hành."; Bài tập 09.3 có gợi ý và lời giải; đoạn kết nối sang Mục 5). Kiến thức tiên quyết thêm nhóm "Chính sách tối ưu tất định (Định lý 04.25)". Giáo trình tham khảo: Sutton và Barto (2018), §13.1 (Ví dụ 13.1 hành lang có hành động đảo, cùng kết luận: chính sách gần đúng tốt nhất có thể ngẫu nhiên), §13.7. Độ dài 15 210 từ. `no-ai-slop`: đạt (một câu hỏi mở mục được trả lời ngay trong đoạn, theo quy định cho ghi chú bài giảng).

`note-for-author.md`: dòng ghi ngược kết luận nguồn ("Không dùng ví dụ gộp trạng thái để tuyên bố ngẫu nhiên hóa tăng return…") thay bằng kết luận đúng nguồn kèm đối chiếu có điều kiện với Định lý 04.25; bỏ "kernel".

Kiểm sau bước mạch 4 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): `L09-15`, sáu trang mạch 4, `L09-20`: 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn; đáy `L09-M4T` 328, `L09-16` 634, `L09-16b` 680, `L09-17` 410, `L09-18` 546, `L09-19` 596 px; đã xem ảnh 1600×900 của sáu trang và ba SVG. 49 `data-slide-id` duy nhất; `#/4` và mục 4 của `L09-02b` mở `L09-M4T`. Viewer: 48/48 khối, 1 093 biểu thức KaTeX, 0 `.katex-error`. `git diff --check` sạch. Tràn còn lại (mạch 5–6, có từ C0): `L09-24` 787 px và tràn phải 1 310 px, `L09-30` tràn phải 1 282 px, `L09-31` 748 px. Trạng thái: chờ điều phối viên duyệt.

### Rà lại mạch 4 (bước R4)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 4 (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R4 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R4-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 1 nghiêm trọng, 3 trung bình, 8 nhẹ; điều phối viên duyệt mạch 4 (`check.py` hai cỡ, ảnh `L09-16`, `L09-16b`, đối chiếu nguồn tr. 23, tự tính $h_2=4$, $h_2=2$) và chấp nhận toàn bộ, kèm các chốt ở cột "quyết định".

| mức độ | trang chiếu | vấn đề | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | `L09-16`, ghi chú diễn giả; ghi chú bài giảng Ví dụ 09.8 | Lớp chính sách "theo $x$" không xác định đúng: với $x\in\{0,1\}$, ba ô trắng cũng bị gộp, nên chính sách ô trắng của Ví dụ 09.9 không thuộc lớp | Đặc trưng phân biệt ô 1, 3, 5, chỉ gộp ô 2 và ô 4 | đã sửa ở R4: mặt trang "$x(s)$ phân biệt ô 1, 3, 5, gộp ô 2 và ô 4 ($x=\mathrm g$)"; hai SVG ghi "x = g", chú thích hình `L09-16` ghi ba ô trắng có đặc trưng riêng; ghi chú bài giảng định nghĩa đặc trưng bốn giá trị và đoạn "sai khác có chủ ý" | chấp nhận (cùng một định nghĩa ở mặt trang, hình, ghi chú bài giảng) |
| trung bình | `L09-16b`; ghi chú bài giảng Ví dụ 09.9, Nhận xét 09.9, đoạn kết mục; `note-for-author.md` | (a) Tiêu chí "tốt hơn" không nêu; (b) mô hình phần thưởng của Nhận xét 09.9 không nhất quán với X kết thúc lượt | Trung bình trên ô xuất phát; X là ô kẹt; công thức giá trị | đã sửa ở R4: "Diễn giải:" xuất phát đều trên năm ô, $3{,}8$ bước; ghi chú bài giảng nói rõ từ riêng ô 2 chính sách tất định Đông chỉ cần 2 bước; đoạn "Theo lợi tức chiết khấu" với $V_2=-(1+\gamma)/(1-(1-p)\gamma^2)$, $V_4=-(1+\gamma)/(1-p\gamma^2)$, cực đại tổng tại $p=\tfrac12$, $\gamma=0{,}9$: $-3{,}19$ so với $-10$; Nhận xét 09.9 dùng X là ô kẹt, chính sách theo ô cho $V_2=V_4=-(1+\gamma)$ | chấp nhận |
| trung bình | `L09-16`, `L09-16b` | Mô hình chuyển không có trên mặt trang | Nêu ngắn gọn | đã sửa ở R4: chú thích hình `L09-16` (đi một ô, gặp tường đứng yên, X là ô kẹt, hàng dưới chỉ vào được từ ô 1, 3, 5); dữ kiện `L09-16b` nêu ô 1 Đông, ô 3 Nam, ô 5 Tây; ghi chú diễn giả `L09-16` nêu tập hành động; `alt` sửa theo | chấp nhận (mô hình chuyển ở chú thích hình để giữ trần) |
| trung bình | `L09-20`, `L09-21` | Chưa có `L09-M5T`; "episodic", "gần như chắc chắn", $\tau$ trước định nghĩa, "return", ghi chú trái D1 | Sửa ở bước mạch 5 | mở (bước mạch 5) | chấp nhận (chuyển bước mạch 5) |
| nhẹ | `L09-16b` "Lưu ý:" | Thiếu điều kiện; "xác định" (Bài 04) và "tất định" chưa nối | "chính sách theo ô"; ghi tương ứng | đã sửa ở R4: "MDP hữu hạn, $\gamma<1$, chính sách theo ô: có tối ưu tất định (Định lý 04.25)"; chọn "tất định", ghi "Bài 04 gọi là chính sách xác định" ở nhóm tiên quyết của ghi chú bài giảng (lần dùng đầu) và ghi chú diễn giả `L09-16b` | chấp nhận ("tất định") |
| nhẹ | `L09-16` ghi chú diễn giả | "một nửa số ô" sai; bỏ qua Bắc/Nam | "hai trong năm ô" | đã sửa ở R4 | chấp nhận |
| nhẹ | ghi chú bài giảng sau Định nghĩa 09.12 | Câu về phép cắt quá chặt | Cắt: coi là một phần môi trường; $\tanh$: thừa số $1/(1-a^2)$ | đã sửa ở R4 | chấp nhận |
| nhẹ | `L09-19` | Nhãn "Còn thiếu:" không được phép | "Lưu ý:" | đã sửa ở R4 | chấp nhận |
| nhẹ | `L09-17` | Tiêu đề trùng tên mạch | "Phân phối hành động có tham số" | đã sửa ở R4 | chấp nhận |
| nhẹ | nguồn ghi chú diễn giả `L09-16b`; Ví dụ 09.9 | Phép tính số bước là bổ sung | Ghi rõ | đã sửa ở R4 (dòng "Nguồn:" và đoạn sai khác có chủ ý trong ghi chú bài giảng) | chấp nhận |
| nhẹ | `storyboard.md` hàng `L09-16b` | Hàng còn ghi kế hoạch cũ | Sửa hàng | đã sửa ở R4 | chấp nhận |
| nhẹ | `note-for-author.md` | Mục cũ trái quyết định hiện hành ("online", "target", "đích", argmax tại trạng thái kết thúc, $Q^\pi$) | Dọn | đã sửa ở R4 (dòng Double DQN, $\operatorname{sg}$ và mặt nạ, Double Q-learning, mạng trực tuyến/mục tiêu, gộp trạng thái, $q_\pi$); dòng "cập nhật online" của REINFORCE sửa ở bước mạch 6 | chấp nhận |

Sai khác có chủ ý so với nguồn: nguồn tr. 23 viết đặc trưng $x(s,a)=1$ nếu $s$ là ô xám, $0$ nơi khác; đặc trưng đó gộp cả ba ô trắng nên lớp chính sách tất định theo đặc trưng còn hẹp hơn. Bài dùng đặc trưng chỉ gộp hai ô xám để giữ đúng kết luận tr. 24–25; mô hình chuyển, ô kẹt X, số bước và giá trị chiết khấu là phần bổ sung (nguồn chỉ cho xác suất $0{,}5$).

Kiểm sau R4 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): sáu trang mạch 4, 0 lỗi console hoặc trang, 0 `.katex-error`, không cuộn ngang, không trang nào tràn; đáy `L09-M4T` 328, `L09-16` 678, `L09-16b` 637, `L09-17` 410, `L09-18` 546, `L09-19` 598 px; `L09-16b` 51 âm tiết; đã xem ảnh 1600×900 của `L09-16`, `L09-16b`. Viewer: 1 114 biểu thức KaTeX, 0 `.katex-error`. Ghi chú bài giảng 15 608 từ. `git diff --check` sạch. `no-ai-slop` (Edit) trên câu mới của R4: đạt. Trạng thái: chờ điều phối viên duyệt.

### Bước mạch 5 (S30–S40, biên tập viên)

Căn cứ: kế hoạch D1 mạch 5, D3 (bài toán một bước hai hành động, hình thẻ dữ kiện), D4 (`L09-27` hệ số âm đẩy $\mu$ ra xa $a$; dấu chấm phẩy trong vector); CT P21, P22, P24–P29, P37, G07, G09, G10; SV (`L09-20` $\tau$ dùng trước định nghĩa, `X02` hỏi Gaussian trước khi dạy, `L09-24` tràn, nhãn hình sai từ, ghi chú dưới 40 âm tiết); TH (`X02` nghiêm trọng, `L09-27` hướng dời, `L09-25`/`X02` trùng câu hỏi, $\tau$/$p_\theta$ trước định nghĩa); mục chuyển từ R4 (`L09-M5T`, "episodic", "gần như chắc chắn", "return", ghi chú `L09-21` trái D1). Nguồn tr. 30–38 đọc lại từ bản trích văn bản của PDF. Mạch 4 đã commit (`67db202`, `0f40934`).

| bước | trang | thay đổi | âm tiết trước → sau | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|
| S30 | `L09-M5T` (mới) | Trang tiêu đề mạch 5, `id="mach-5"`; dòng dẫn theo outline | — → dẫn 19, khóa 16 | đạt | chờ điều phối viên duyệt |
| S31 | `L09-20` | "Hàm mục tiêu của chính sách": Nhu cầu, thẻ dữ kiện, Ví dụ $J=2$, Định nghĩa với $\mathbb E_{\pi_\theta}$ (bỏ $\tau$, $p_\theta$), Giả thiết hầu chắc chắn và trạng thái hấp thụ | 31 → 42 | bỏ câu chỉ đường "Trọng số $\gamma^t$ sẽ trở lại…"; đạt | chờ điều phối viên duyệt |
| S32 | `L09-21` | "Bước tăng gradient": Nhắc lại hạ gradient DQN, dấu cộng, ví dụ $\nabla_\theta J=(\tfrac23;\,-\tfrac23)$, Lưu ý $J$ chỉ đo qua lượt; bỏ hai thẻ | 24 → 40 | bỏ câu quy trình "Sai phân hữu hạn không còn trong tuyến bài", "return", "loss"; đạt | chờ điều phối viên duyệt |
| S33 | `L09-30A` | "Ước lượng gradient bằng sai phân hữu hạn": trang vấn đề của hàm điểm, $u_k$ định nghĩa, thẻ dữ kiện, $0{,}655$ so với $\tfrac23$, $d+1$ giá trị $J$ | 19 → 42 | bỏ tiền tố "Đọc thêm:", câu "có thể lược", câu nối rối sang Bài 10; đạt | chờ điều phối viên duyệt |
| S34 | `L09-23` | "Hàm điểm": Trực quan → Ví dụ $(\tfrac13;\,-\tfrac13)$ → Định nghĩa → Lưu ý miền hỗ trợ | 26 → 50 | đạt | chờ điều phối viên duyệt |
| S35 | `L09-24` | Mệnh đề và Chứng minh softmax; `softmax-score.svg` vẽ lại; hết tràn (787 → 655 px, phải 1310 → 1256) | 12 → 24 | bỏ câu hình "Tổng kỳ vọng của hàm điểm bằng 0" (sai từ); đạt | chờ điều phối viên duyệt |
| S36 | `L09-25` | "Ví dụ: hàm điểm softmax hai hành động": thẻ dữ kiện, hai hàm điểm, trung bình $(0;\,0)$, Diễn giải | 20 → 21 | đạt | chờ điều phối viên duyệt |
| S37 | `L09-25b` (mới) | "Kỳ vọng của hàm điểm": Mệnh đề ba giả thiết, Chứng minh, Ý nghĩa | — → 34 | đạt | chờ điều phối viên duyệt |
| S38 | `L09-26` | "Hàm điểm của chính sách Gaussian": Nhắc lại, Mệnh đề, Chứng minh, Ý nghĩa | 24 → 25 | đạt | chờ điều phối viên duyệt |
| S39 | `L09-27` | "Ví dụ: hàm điểm Gaussian tại $a=1{,}5$": $(1{,}5;\,3)$; Câu hỏi với hệ số $c$; Lời giải $\Delta\mu=-0{,}75$, ra xa $a$ | 33 → 18 | bỏ "hệ số return"; đạt | chờ điều phối viên duyệt |
| S40 | `X02` | "Bài tập: hàm điểm softmax và Gaussian": hình dữ kiện mới, bộ số softmax mới, Lời giải ba dòng, Lưu ý đầu ra cho mạch 6 | 20 → 45 | bỏ "Với ví dụ softmax", "giữ $\phi=(1,2)$"; đạt | chờ điều phối viên duyệt |

Số liệu đã tính lại (Python): $J(\log2;\,0)=2$, $J(0;\,0)=1{,}5$; $\nabla_\theta J=3\pi_1\pi_2(1;\,-1)=(\tfrac23;\,-\tfrac23)$; một bước $\alpha=0{,}1$: $\pi(1\mid s)=0{,}6956$, $J=2{,}0868$. Sai phân $\epsilon=0{,}1$: $J(\theta+\epsilon u_1)=2{,}06552$, thương $0{,}65520$; $J(\theta+\epsilon u_2)=1{,}93226$, thương $-0{,}67739$; trung tâm $0{,}66630$; $\epsilon=0{,}01$: $0{,}66555$. Phương sai lợi tức $9\pi_1\pi_2=2$ tại $\theta$, $1{,}930$ tại $\theta+\epsilon u_1$; độ lệch chuẩn của thương với $n=100$: $1{,}98$; $n$ cho độ lệch chuẩn $0{,}1$: $39\,302$. Softmax: $\psi(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi(s,2)=(-\tfrac23;\,\tfrac23)$, trung bình $(0;\,0)$; `X02`: $\pi=(\tfrac14;\,\tfrac34)$, $\psi(s,1)=(\tfrac34;\,-\tfrac34)$, $\psi(s,2)=(-\tfrac14;\,\tfrac14)$, trung bình $(0;\,0)$; Gaussian $(1{,}5;\,3)$, $(-1;\,-2)$; $\Delta\mu=\alpha c(a-\mu)\lVert\phi\rVert^2/\sigma^2=0{,}1\cdot(-1)\cdot1{,}5\cdot5=-0{,}75$. Hình `softmax-score.svg`: trọng tâm $(214;\,95)$ của ba điểm với trọng số $0{,}5$; $0{,}3$; $0{,}2$, tổng có trọng số của ba mũi tên bằng $(0;\,0)$ theo tọa độ hình.

SVG: `one-step-card.svg` mới (thẻ dữ kiện bài toán một bước: bảng $\phi$, $\pi_\theta$, $r$; $\theta=(\log2;\,0)$; dùng ở `L09-20`, `L09-30A`, `L09-25`, mạch 6 dùng lại); `score-exercise-card.svg` mới (hai thẻ dữ kiện của `X02`); `softmax-score.svg` vẽ lại. Cả ba có `width`/`height` nội tại, `role="img"`, `title`, `desc`.

Ghi chú bài giảng, `## 5. Hàm mục tiêu và hàm điểm` viết lại (khoảng 4 700 từ), thay các mục cũ "Mục tiêu episodic và giả thiết", "Hàm điểm softmax", "Hàm điểm Gaussian phương sai cố định" và mục "Đọc thêm: sai phân hữu hạn" ở Mục 7 (mã `lec-09-topic-14` chuyển về Mục 5): đoạn mở và hình thẻ dữ kiện; Ví dụ 09.11 trước Định nghĩa 09.14 (Hàm mục tiêu) với vai trò từng giả thiết và phản ví dụ; Ví dụ 09.12 (lượt hai bước); bước tăng gradient có lý do bậc một và số; câu hỏi nguồn tr. 30, cách không dùng gradient tr. 31; "Trong thực hành." (cực tiểu hóa $-J$); sai phân hữu hạn với Ví dụ 09.13, phân tích phương sai $2\sigma_G^2/(n\epsilon^2)$ có số, chi phí $d+1$; hàm điểm: trực quan, Ví dụ 09.14, Định nghĩa 09.15, điều kiện $\pi>0$; Mệnh đề 09.16 (softmax) chứng minh bốn bước; hình đọc trong văn bản; Ví dụ 09.15; Mệnh đề 09.17 (kỳ vọng bằng $0$) ba giả thiết, chứng minh bốn bước, phản ví dụ phân phối đều trên $[0,\theta]$; Mệnh đề 09.18 (Gaussian) chứng minh; Ví dụ 09.16; câu hỏi nguồn tr. 38 và hàm điểm theo $\log\sigma$; Nhận xét 09.19 (năm nhầm lẫn); "Trong thực hành." (log-softmax, vi phân tự động, che hành động không hợp lệ, dữ liệu khác chính sách); Bài tập 09.4–09.6 có gợi ý, lời giải, "Kiểm tra lại"; đoạn kết nối sang Mục 6. Ký hiệu: thêm "$\log$ là logarit tự nhiên" vào quy ước đọc; đổi bốn chỗ $\ln$ cũ (Mục 2, Mục 4) thành $\log$. Bản đồ chủ đề: hàng topic-07, topic-08 cập nhật.

Sửa ngoài phạm vi mạch 5, phát hiện khi kiểm trình xem: Mục 4 (commit `0f40934`) viết "ô đích \$ dưới ô 3"; trình xem coi dấu đô-la thoát là mở công thức, tạo một khối KaTeX dài 2 500 px gây cuộn ngang trang (không báo `.katex-error`). Đã bỏ ký hiệu đô-la khỏi câu. Kiểm cuộn ngang được thêm vào bộ kiểm trình xem.

`outline.md`: bảng note-topic-id → data-slide-id (topic-07, 14, 08, 09; `X02` sang topic-09), số mã sau bước mạch 5 (51), ký hiệu $\log$ và bài toán một bước. `note-for-author.md`: thêm dòng mạch 5 ($J$ không dùng $\tau$; sai phân hữu hạn là trang vấn đề; thẻ dữ kiện; $\log$).

Kiểm sau bước mạch 5 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): `L09-19`, mười một trang mạch 5, `L09-28`: 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn; đáy `L09-M5T` 371, `L09-20` 649, `L09-21` 597, `L09-30A` 608, `L09-23` 622, `L09-24` 655, `L09-25` 666, `L09-25b` 617, `L09-26` 573, `L09-27` 449 (đủ phân đoạn), `X02` 655 px; đã xem ảnh 1600×900 của mười một trang và ảnh 390×844 của `L09-24`. Mật độ: lớn nhất `L09-23` 50 âm tiết; ghi chú diễn giả 74–121, `L09-M5T` 95. `#/5` mở `L09-M5T`; liên kết "Nội dung" bấm được cả bảy; 51 `data-slide-id` duy nhất, 7 section ngoài, mọi trang có ghi chú. Trình xem: 0 `.katex-error`, mọi khối `:::` nhận diện, 0 yêu cầu ngoài, không cuộn ngang ở 1400 và 390 px; đã xem ảnh Mệnh đề 09.17, Ví dụ 09.13, Bài tập 09.4–09.6. `git diff --check` sạch. `quill` (Concept, Threads): $J$, $\psi_\theta$, miền hỗ trợ, $u_k$ định nghĩa trước khi dùng; $\tau$, $p_\theta$ không xuất hiện ở mạch 5; thẻ dữ kiện là sợi chỉ nối `L09-20` → `L09-30A` → `L09-25` → mạch 6.

Còn mở, chuyển bước sau: (1) Mục 6 của ghi chú bài giảng còn tham chiếu "các giả thiết ở topic-07", nay đã chuyển sang mạch 6; sửa ở bước mạch 6. (2) Mục "Bài tập củng cố" còn mục X02 cũ (cùng cách xử lý với X01); thay ở bước mạch 7. (3) Ghi chú bài giảng 19 728 từ, sát trần 20 000 của `AGENTS.md`; bước mạch 6–7 cần thay chứ không cộng thêm (Mục 6 cũ, Mục 7 cũ, "Bài tập củng cố" cũ khoảng 1 800 từ).

### Rà lại mạch 5 (bước R5)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 5 (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R5 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R5-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 4 trung bình (1 chuyển bước mạch 6), 6 nhẹ. Điều phối viên duyệt mạch 5 (`check.py`, ảnh `L09-20`, `L09-30A`, `X02`; tự tính $0{,}655$, $\Delta\mu=-0{,}75$, độ lệch chuẩn sai phân $\approx2$) và chấp nhận toàn bộ, kèm các chốt ở cột "quyết định".

| mức độ | vị trí | vấn đề | đề xuất | trạng thái | quyết định |
|---|---|---|---|---|---|
| trung bình | `L09-21` | Gradient $3\pi_1\pi_2(1;\,-1)$ xuất hiện không bước, không nói softmax và $r$ đã biết | Câu thay thế; thẻ nếu vừa trang | đã sửa ở R5: "Softmax hai hành động, $\phi$ đơn vị, $r=(3;\,0)$ đã biết: $J=3\pi_\theta(1\mid s)$, và $\nabla_\theta\pi_\theta(1\mid s)=\pi_1\pi_2(1;\,-1)$" / "Tính trực tiếp…"; ghi chú diễn giả có đạo hàm softmax; thẻ không vừa trang (597 + 220 px) | chấp nhận |
| trung bình | `one-step-card.svg` | Thẻ không ghi họ chính sách | Ghi "chính sách softmax" | đã sửa ở R5: tiêu đề thẻ "Bài toán một bước, chính sách softmax"; `desc`, ba `alt` của deck và `alt` ở ghi chú bài giảng theo | chấp nhận |
| trung bình | ghi chú bài giảng, độ dài | Sát trần 20 000 từ (`wc -w`) | Cắt đoạn lặp; dành chỗ cho Mục 6–7 | đã sửa ở R5: bỏ đoạn "Thẻ ghi một trạng thái…" (lặp dữ kiện Ví dụ 09.11); đoạn câu hỏi nguồn tr. 38 không nêu sẵn công thức của Bài tập 09.6; bỏ mục 4 của Nhận xét 09.19 (lặp Ví dụ 09.16); "Kiểm tra lại" của Ví dụ 09.7 không còn lộ lời giải Bài tập 09.2; rút cột "Vai trò" của sáu hàng bản đồ chủ đề. Không chuyển bài tập sang `exercises.md` (người dùng chưa yêu cầu giai đoạn bài tập) | chấp nhận (quy ước đo dưới đây) |
| trung bình (chuyển bước mạch 6) | `L09-28`, `L09-22` | Chưa có `L09-M6T`; $\tau$, $p_\theta$ chưa định nghĩa; "Tỷ", "return", "Hợp đồng"; ghi chú `L09-22` về sai phân hữu hạn đã sai | Sửa ở bước mạch 6 | mở (bước mạch 6) | chấp nhận (chuyển bước mạch 6) |
| nhẹ | ghi chú diễn giả `L09-30A`; Bài tập 09.5 | Sai lệch một phía là $0{,}011$, không $0{,}012$ | Sửa số | đã sửa ở R5 | chấp nhận |
| nhẹ | `X02` (b); Bài tập 09.4 (b) | $\psi_\theta(s,-1)$ dễ đọc thành hành động số $-1$; "về phía $a$" chỉ đúng với bước nhỏ | "Với $a=-1$: $\psi_\theta(s,a)$"; "bước nhỏ" | đã sửa ở R5 (ghi chú bài giảng nêu $\alpha<0{,}2$ thì không vượt $a$) | chấp nhận |
| nhẹ | ghi chú diễn giả `L09-26`; ghi chú bài giảng Mục 5 | Câu Gaussian bị chặn trái Mục 4 | Khớp Mục 4 | đã sửa ở R5 | chấp nhận |
| nhẹ | ghi chú bài giảng Mục 5 | "tỉ số khả năng xảy ra" lệch bảng thuật ngữ | "tỉ số xác suất (likelihood ratio)" | đã sửa ở R5 | chấp nhận |
| nhẹ | ghi chú diễn giả `L09-25b` | Điều kiện đổi đạo hàm–tích phân lỏng | Chặn $\lVert\nabla_\theta\pi_{\theta'}(a\mid s)\rVert$ bởi hàm khả tích của $a$, đều trong lân cận | đã sửa ở R5 | chấp nhận |
| nhẹ | ghi chú bài giảng Ví dụ 09.7 | "Kiểm tra lại" lộ lời giải Bài tập 09.2 | Thay bằng kiểm $4<4{,}06<4{,}6$ | đã sửa ở R5 | chấp nhận |

Quy ước đo độ dài ghi chú bài giảng (chốt của điều phối viên ở R5, như đã dùng cho Bài 08): trần 8 000–20 000 từ của `AGENTS.md` tính theo số từ thân văn, bỏ công thức (`$…$`, `$$…$$`), bảng (dòng bắt đầu bằng `|`), khối mã, dòng ảnh, dòng `:::` và chú thích HTML; chỉ đếm token có chữ cái. Công cụ: `c09/bodywords.py` trong scratchpad. Đích: ≤ 20 000 từ thân văn khi xong mạch 7; Mục 6–7 viết lại thay văn bản cũ, không cộng thêm. Số đo sau R5: `wc -w` 19 587 (trước R5 19 727); thân văn 14 012 (trước R5 14 085).

Kiểm sau R5 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mười một trang mạch 5, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn (`X02` lần đầu 707 px, rút dòng (b) còn 655 px); đáy `L09-20` 649, `L09-21` 597, `L09-30A` 608, `L09-25` 666, `L09-25b` 617, `L09-26` 573 px; `L09-21` 49 âm tiết, `X02` 49. Đã xem ảnh 1600×900 của `L09-20`, `L09-21`, `X02`. Trình xem: 0 `.katex-error`, mọi khối `:::` nhận diện, 0 yêu cầu ngoài, không cuộn ngang ở 1400 và 390 px; đã xem ảnh đoạn Gaussian và Nhận xét 09.19. `git diff --check` sạch. `no-ai-slop` (Edit) trên câu mới của R5: đạt. Trạng thái: chờ điều phối viên duyệt.

### Bước mạch 6 (S41–S51, biên tập viên)

Căn cứ: kế hoạch D1 mạch 6; D4 (định lý có nhãn và giả thiết trên mặt trang, điều kiện đủ đơn giản $|R|\le R_{\max}$, hàm điểm hoặc đặc trưng bị chặn, $T\le T_{\max}$; giữ $\gamma^t$, Nota và Thomas 2020; phân biệt theo chính sách và khác chính sách; $\mathbb E[\widehat g]=\nabla J(\theta_{\mathrm{old}})$); CT P30–P36, G07, G09, G10, G13; SV (`L09-28` không có chữ, `L09-29` $\psi_t$ chưa định nghĩa và thứ tự lập luận, `L09-30` đoạn đặc và "Trực giác:", `X03` dựa vào trí nhớ, dấu chấm phẩy trong vector, "Đáp án"); TH (định lý không nhãn, điều kiện đổi đạo hàm mơ hồ, $\tau$ trước định nghĩa, on-policy, cắt ngắn, lý do bỏ $\gamma^t$ sai, $G_0(\tau)$ không phụ thuộc $\theta$, biến thể cập nhật theo từng $t$); mục chuyển từ R5 (`L09-M6T`, "Tỷ", "return", "Hợp đồng", câu sai về sai phân hữu hạn); dòng "online" của `note-for-author.md`. Nguồn tr. 39–40 đọc lại từ bản trích văn bản (nguồn: định lý dạng $\mathbb E[\nabla\log\pi\,Q^\pi]$; REINFORCE không có $\gamma^t$, cập nhật theo từng $t$). Mạch 5 đã commit (`348cd43`, `2da4088`).

| bước | trang | thay đổi | âm tiết trước → sau | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|
| S41 | `L09-M6T` (mới) | Trang tiêu đề mạch 6, `id="mach-6"` | — → dẫn 19, khóa 18 | đạt | chờ điều phối viên duyệt |
| S42 | `L09-28` | Nhu cầu; ví dụ một bước với thẻ dữ kiện; Ký hiệu $\tau$, $p_\theta$; tỉ số xác suất | 0 → 27 | bỏ "return", "Tỷ", tiếng Anh trong tiêu đề; đạt | chờ điều phối viên duyệt |
| S43 | `L09-28A` | Xác suất của quỹ đạo; $\psi_t$; Ý nghĩa không cần $P$ | 8 → 29 | bỏ "luận điểm trung tâm" (phóng đại), "Trang sau dùng…" (chỉ đường); đạt | chờ điều phối viên duyệt |
| S44 | `L09-29` | Tách $G_0$ trước, rồi $\mathbb E[G_{<t}\psi_t]=0$, rồi kết luận | 20 → 16 | đạt | chờ điều phối viên duyệt |
| S45 | `L09-29b` (mới) | Ví dụ: lượt hai bước; $5{,}6\psi$, $4{,}6\psi$, $4{,}8\psi$ | — → 31 | đạt | chờ điều phối viên duyệt |
| S46 | `L09-22` | Giả thiết (G1)–(G4), chuyển xuống trước định lý | 47 → 51 | bỏ "hợp đồng", "chi phối toàn bộ suy diễn", câu sai về sai phân hữu hạn; đạt | chờ điều phối viên duyệt |
| S47 | `L09-30` | Định lý. dạng quỹ đạo; Chứng minh một dòng; Dạng khác với $\nu^\pi_\gamma$; hết tràn phải | 32 → 26 | bỏ "Mở rộng", "Trực giác:", gạch ngang dài, "có thể lược"; đạt | chờ điều phối viên duyệt |
| S48 | `L09-32` | Ví dụ: một cập nhật REINFORCE, thẻ dữ kiện, kiểm kỳ vọng | 13 → 5 | bỏ "Dùng lại…", "episode", "return"; đạt | chờ điều phối viên duyệt |
| S49 | `L09-31` | Thuật toán. REINFORCE đầy đủ; không chệch; Lưu ý theo chính sách; hết tràn (748 → 565 px) | 11 → 37 | sửa câu "bỏ $\gamma^t$ vì dùng mục tiêu khác", "sửa có chủ ý" (nhãn quy trình); đạt | chờ điều phối viên duyệt |
| S50 | `X03` | Câu hỏi tự đủ với thẻ; (a) phần thưởng $-3$; (b) lượt hai bước mới | 36 → 28 | bỏ "Giữ dữ kiện của ví dụ softmax trước đó", "hợp đồng lấy mẫu"; đạt | chờ điều phối viên duyệt |
| S51 | `X03b` (mới) | Lời giải từng bước; Lưu ý phương sai, đầu ra cho mạch 7 | — → 31 | đạt | chờ điều phối viên duyệt |

Số liệu đã tính lại (Python): $\sum_ar(a)\pi\psi=\tfrac23\cdot3(\tfrac13;\,-\tfrac13)=(\tfrac23;\,-\tfrac23)$. Lượt hai bước: $G_1=2$, $G_0=2{,}8$; $5{,}6\psi=(1{,}867;\,-1{,}867)$, $4{,}6\psi=(1{,}533;\,-1{,}533)$, $4{,}8\psi=(1{,}6;\,-1{,}6)$. Cập nhật: $\pi=2/(2+e^{-0{,}2})=0{,}70954$; phần thưởng $-3$: $2/(2+e^{0{,}2})=0{,}62085$. `X03` (b): $2{,}8(\tfrac13;\,-\tfrac13)+1{,}8(-\tfrac23;\,\tfrac23)=(-0{,}2667;\,0{,}2667)$. Phương sai $\widehat g$ một bước: $r=(3;\,0)$ tổng $0{,}4444=\tfrac49$; $r=(4;\,1)$ kỳ vọng vẫn $(\tfrac23;\,-\tfrac23)$, tổng $1{,}7778=\tfrac{16}9$. Hai trạng thái tham số riêng (ghi chú bài giảng Ví dụ 09.21): $\nabla J=(g;\,0{,}9g)$, bỏ $\gamma^t$ cho $(g;\,g)$, $\cos=0{,}99862$, góc $3{,}01^\circ$. Ghi chú: TH đề xuất "$r(2)=1$" làm ví dụ cộng hằng; thực ra đổi $r(2)$ làm đổi gradient thành $(\tfrac49;\,-\tfrac49)$, nên bài dùng $r=(4;\,1)$ (cộng $1$ vào mọi phần thưởng), gradient giữ nguyên.

SVG: `reinforce-trajectory.svg` vẽ lại (phông theo deck, "lượt", "lợi tức" thay "episode", "return"; $G_t=R_{t+1}+\gamma G_{t+1}$ tính lùi; $\widehat g=\sum_t\gamma^tG_t\psi_t$; $\pi_{\theta_{\mathrm{old}}}$ giữ cố định), chuyển từ `L09-31` sang ghi chú bài giảng vì trang thuật toán đủ bảy dòng. Ba trang mới dùng lại `one-step-card.svg` (`L09-28`, `L09-32`, `X03`).

Ghi chú bài giảng, `## 6. Gradient chính sách và REINFORCE` viết lại thay văn bản cũ (bỏ ba mục cũ "Tỷ số xác suất và nhân quả", "REINFORCE episodic", "Phân bố chiếm dụng chiết khấu" cùng các trỏ "giả thiết ở topic-07"): đoạn mở nối Mục 5; Ví dụ 09.17 (gradient một bước bằng hàm điểm); Định nghĩa 09.20 (quỹ đạo, xác suất quỹ đạo); tỉ số xác suất; Bổ đề 09.21 với chứng minh; bỏ phần thưởng quá khứ; Ví dụ 09.18 (lượt hai bước); giả thiết (G1)–(G4); Định lý 09.22 bốn phần (Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi), chứng minh năm bước có nhãn, `aligned`, $\square$; vai trò từng giả thiết và điều kiện tổng quát hơn $\mathbb E[T]<\infty$; Hệ quả 09.23 (dạng phân bố chiếm dụng, $(1-\gamma)$ chuẩn hóa, chứng minh ba bước, cắt ngắn); Ví dụ 09.19 (một cập nhật, kiểm kỳ vọng); Thuật toán 09.24; hình vẽ lại; Hệ quả 09.25 (không chệch, theo chính sách, bộ nhớ phát lại); Ví dụ 09.20 (phương sai $\tfrac49$); Nhận xét 09.26 (bỏ $\gamma^t$, Nota và Thomas 2020); Ví dụ 09.21 (hai trạng thái, góc $3^\circ$); Nhận xét 09.27 (năm nhầm lẫn); "Trong thực hành." (hàm mất mát thay thế $-\sum_t\gamma^tG_t\log\pi_\theta$, trung bình nhiều lượt, quan sát không Markov, cắt ngắn CartPole, mỗi lượt dùng một lần); Bài tập 09.7, 09.8 có gợi ý, lời giải, "Kiểm tra lại"; kết mục nối Bài 10 và Mục 7. Tài liệu tham khảo thêm Sutton và cộng sự (2000), Nota và Thomas (2020).

Độ dài ghi chú bài giảng sau bước mạch 6: `wc -w` 22 364 (trước 19 587); thân văn theo quy ước của R5 16 018 (trước 14 012). Mục 7 và "Bài tập củng cố" cũ (khoảng 560 từ `wc -w`) sẽ được thay ở bước mạch 7; còn khoảng 4 000 từ thân văn trước trần 20 000.

`note-for-author.md`: dòng "online" sửa thành "cập nhật trong khi đang thu lượt"; thêm theo chính sách và bộ nhớ phát lại; dòng phân bố chiếm dụng ($\nu^\pi_\gamma$, $q_\pi$, (G1)–(G4), không nói về hội tụ); lý do giữ $\gamma^t$; dòng ví dụ cập nhật dùng thẻ dữ kiện. `outline.md`: bảng note-topic-id → data-slide-id (topic-10, 11, 12; `L09-22` sang topic-11), số mã sau bước mạch 6 (54), giả thiết (G1)–(G4).

Kiểm sau bước mạch 6 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mười một trang mạch 6 và `L09-33`: 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn; đáy `L09-M6T` 450, `L09-28` 670, `L09-28A` 681, `L09-29` 606, `L09-29b` 557, `L09-22` 507, `L09-30` 607, `L09-32` 557, `L09-31` 565, `X03` 626, `X03b` 545 px; đã xem ảnh 1600×900 của mười một trang. `#/6` mở `L09-M6T`; liên kết "Nội dung" bấm được cả bảy; 54 `data-slide-id` duy nhất, 7 section ngoài, mọi trang có ghi chú. Trình xem: 0 `.katex-error`, mọi khối `:::` nhận diện (gồm `lemma`, `theorem`, `corollary`), 0 yêu cầu ngoài, không cuộn ngang trang ở 1400 và 390 px (hình rộng cuộn trong khung của chính nó theo CSS của trình xem); đã xem ảnh Định lý 09.22 và Thuật toán 09.24 cùng hình. `git diff --check` sạch. `quill` (Concept, Threads): $\tau$, $p_\theta$, $\psi_t$, $H_t$, $G_{<t}$, (G1)–(G4), $\nu^\pi_\gamma$, $q_\pi$ định nghĩa hoặc nhắc lại trước khi dùng; thẻ dữ kiện nối mạch 5 → `L09-28` → `L09-32` → `X03`.

Còn mở, chuyển bước mạch 7: `L09-33` ("Bốn hợp đồng", "Thu hồi Jensen", "Online chọn; target đánh giá") và Mục 7 của ghi chú bài giảng ("Cầu nối: baseline…", "Bốn hợp đồng cần giữ", "Bài tập củng cố" X01–X03 cũ).

### Rà lại mạch 6 (bước R6)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 6 (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R6 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R6-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 4 trung bình (1 chuyển bước mạch 7), 7 nhẹ (1 không cần sửa). Điều phối viên duyệt mạch 6 (`check.py`, ảnh `L09-29`, `L09-30`, `L09-31`; tự tính $5{,}6/4{,}6/4{,}8$, phương sai $\tfrac49$, $\tfrac{16}9$) và chấp nhận toàn bộ, kèm các chốt ở cột "quyết định".

| mức độ | vị trí | vấn đề | đề xuất | trạng thái | quyết định |
|---|---|---|---|---|---|
| trung bình | `L09-30`, `L09-28` | Giả thiết của định lý không có trên mặt trang; "Dạng khác" thiếu điều kiện; `L09-28` đổi $\nabla$ với $\int$ chưa nói cần giả thiết | Tóm tắt bốn giả thiết tại chỗ; điều kiện kết thúc do MDP | đã sửa ở R6: "Định lý. Nếu … (G1); … (G2); … (G3); … (G4):" (44 âm tiết, đáy 639 px); "Dạng khác (lượt kết thúc do MDP, không cắt ngắn)", $q_{\pi_\theta}$; `L09-28` "đổi $\nabla$ với $\int$ cần giả thiết (G1)–(G4)"; dòng "Chứng minh." của `L09-30` chuyển vào ghi chú diễn giả để giữ đáy | chấp nhận |
| trung bình | ghi chú bài giảng sau Định lý 09.22; ghi chú diễn giả `L09-22` | Câu "điều kiện tổng quát hơn với $\mathbb E[T]<\infty$" sai lý lẽ (chặn trội cần đều trong lân cận; $p_{\theta'}/p_\theta$ tăng theo hàm mũ của $T$) | Thay bằng lập luận chuỗi $\sum_t\gamma^t$ hội tụ đều | đã sửa ở R6: ghi chú bài giảng viết $J=\sum_t\gamma^t\mathbb E[R_{t+1}\mathbf 1\{t<T\}]$, gradient số hạng thứ $t$ chặn bởi $(t+1)CR_{\max}$, chuỗi chặn bởi $\sum_t\gamma^t(t+1)CR_{\max}<\infty$ (Sutton và cộng sự, 2000), kèm câu vì sao chặn trực tiếp trên cả lượt không đủ; ghi chú diễn giả `L09-22`: "Ghi chú bài giảng nêu cách bỏ giới hạn độ dài lượt khi $\gamma<1$ và hàm điểm bị chặn." | chấp nhận |
| trung bình | ghi chú bài giảng Mục 6, độ dài | Bốn chủ đề lặp; đoạn kết kể lại mọi số | Giữ mỗi ý một chỗ | đã sửa ở R6: (a) bỏ đoạn "Bỏ $\gamma^t$" của Ví dụ 09.18 và mục 5 của nhận xét nhầm lẫn; Nhận xét 09.26 cũ thành đoạn dẫn của Ví dụ 09.21 (nhận xét nhầm lẫn đổi số thành Nhận xét 09.26); (b) bỏ mục 3 của nhận xét nhầm lẫn và câu cuối "Trong thực hành." về bộ nhớ phát lại (giữ đoạn sau Hệ quả 09.25); (c) bỏ câu cắt ngắn sau Hệ quả 09.23 (giữ trong "Trong thực hành."; giả thiết của hệ quả đã nêu kết thúc do MDP); (d) đoạn kết còn ba câu | chấp nhận |
| trung bình (chuyển bước mạch 7) | `L09-33` | Chưa có `L09-M7T`; `L09-33` bản cũ; dòng "Lưu ý:" của `X03b` chưa có nơi nhận | Sửa ở bước mạch 7 | mở (bước mạch 7) | chấp nhận (chuyển bước mạch 7) |
| nhẹ | `L09-29` | Số hiệu ghi chú làm chủ ngữ; thiếu $A_t\sim\pi_\theta(\cdot\mid S_t)$ khi biết $H_t$ | Câu thay thế | đã sửa ở R6 | chấp nhận |
| nhẹ | `L09-22` (G4); ghi chú bài giảng (G4) | Câu ghép đọc như "softmax là một đặc trưng bị chặn" | "$\pi_\theta$ là softmax, hoặc Gaussian với $\sigma$ cố định; đặc trưng bị chặn" | đã sửa ở R6 | chấp nhận |
| nhẹ | `L09-29b` | "không có kỳ vọng $0$" quá mạnh | "nói chung có kỳ vọng khác $0$" | đã sửa ở R6 | chấp nhận |
| nhẹ | `X03` (b); Bài tập 09.7 (b) | Mâu thuẫn với thẻ "lượt dừng sau $A_0$" | "Bỏ điều kiện dừng sau $A_0$: lượt hai bước…" | đã sửa ở R6 (phát biểu dữ kiện mới tại chỗ) | chấp nhận |
| nhẹ | ghi chú diễn giả `X03b`; Bài tập 09.7 "Kiểm tra lại" | Lý do "nghiêng về hành động 2" so sai đại lượng | So đóng góp $1{,}2$ với $0{,}933$, hàm điểm hành động 2 dài gấp đôi | đã sửa ở R6 | chấp nhận |
| nhẹ | ghi chú bài giảng "Trong thực hành." | "đầu ra bị chặn" chưa đủ | Gradient của logit hoặc trung bình theo $\theta$ bị chặn | đã sửa ở R6 | chấp nhận |
| nhẹ | `L09-31` "Lưu ý:" | "phải hiệu chỉnh" chưa nói bằng gì | Trọng số $p_{\theta_{\mathrm{old}}}(\tau)/p_{\theta'}(\tau)$ | đã sửa ở R6 | chấp nhận |
| nhẹ | `L09-28A` | Đáy 681 px | Giảm nếu được | đã sửa ở R6: bỏ dòng mở, đáy 596 px | chấp nhận |
| nhẹ | `note-for-author.md` | Đã khớp | Không cần sửa | không sửa | chấp nhận |

Độ dài ghi chú bài giảng sau R6 (thước đo theo quy ước ở R5: số từ thân văn, bỏ công thức, bảng, khối mã, dòng ảnh, dòng `:::`, chú thích HTML; vì công thức và bảng không phải văn bản người đọc phải đọc như câu chữ, và `wc -w` đếm mỗi mảnh LaTeX tách bởi khoảng trắng là một từ): thân văn 15 981 (trước R6 16 018); `wc -w` 22 290 (trước R6 22 364).

Kiểm sau R6 (Playwright Chromium, `http://127.0.0.1:8799`, 1600×900 và 390×844): mười một trang mạch 6, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn (`L09-28` lần đầu 713–767 px khi thêm câu giả thiết, sửa còn 670; `L09-30` lần đầu 711 px, sửa còn 639); đáy `L09-28` 670, `L09-28A` 596, `L09-29` 649, `L09-29b` 557, `L09-22` 507, `L09-30` 639, `L09-31` 626, `X03` 626, `X03b` 545 px; đã xem ảnh 1600×900 của `L09-28`, `L09-30`, `L09-31`, `X03`. Trình xem: 0 `.katex-error`, mọi khối `:::` nhận diện, 0 yêu cầu ngoài, không cuộn ngang trang; đã xem ảnh Ví dụ 09.21 và Nhận xét 09.26. `git diff --check` sạch. `no-ai-slop` (Edit) trên câu mới của R6: đạt. Trạng thái: chờ điều phối viên duyệt.

### Bước mạch 7 (S52–S61, biên tập viên)

Căn cứ: kế hoạch D1 mạch 7, D6 (tình huống áp dụng, tóm tắt chương, Bài tập 09.k ba mức thay X01–X03, tài liệu tham khảo), D7; CT §3.2 (mạch tổng kết) và P38, G11, G13; SV (`L09-33` vượt trần, "Thu hồi Jensen", "hợp đồng"); mục chuyển từ R6 (`L09-M7T`, `L09-33` bản cũ, nơi nhận dòng "Lưu ý:" của `X03b`). Khuôn: mạch 7 của deck 08 và `## 7.`, các mục cấp chương của ghi chú bài giảng Bài 08. Mạch 6 đã commit (`fcfcf5a`, `88646cd`).

| bước | trang | thay đổi | âm tiết | `no-ai-slop` (Edit, tự kiểm theo `eval.md`) | trạng thái |
|---|---|---|---|---|---|
| S52 | `L09-M7T` (mới) | Trang tiêu đề mạch 7, `id="mach-7"` | dẫn 17, khóa 14 | đạt | chờ điều phối viên duyệt |
| S53–S54 | `L09-K1`, `L09-K1b` (mới) | Bảng kết quả–giả thiết–công thức, bảy hàng tách 3 + 4 | 48; 46 | đạt | chờ điều phối viên duyệt |
| S55–S56 | `L09-K2`, `L09-K2b` (mới) | Hai bảng so sánh bốn phương pháp; kết luận về độ chệch, không viết "hội tụ" | 63; 70 | đạt | chờ điều phối viên duyệt |
| S57–S58 | `L09-K3`, `L09-K4` (mới) | Bài tập tổng hợp trên thẻ dữ kiện, lời giải trên mặt trang | 31; 31 | đạt | chờ điều phối viên duyệt |
| S59 | `L09-K5` (mới) | Trả lời vấn đề trung tâm, năm dòng có điều kiện, "Nguồn:" | 72 | đạt | chờ điều phối viên duyệt |
| S60 | `L09-K6` (mới) | Câu hỏi tự kiểm tra, bốn câu | 52 | đạt | chờ điều phối viên duyệt |
| S61 | `L09-K7` (mới) | Bài tập về nhà (bảng trỏ Bài tập 09.1–09.9 trong ghi chú; không liên kết giả), tài liệu đọc, liên kết ghi chú, dòng nối Bài 10 | 52 | đạt | chờ điều phối viên duyệt |
| — | `L09-33` | Bỏ; nội dung vào `L09-K1`, `L09-K1b`, `L09-K2b` | 91 → — | bỏ "hợp đồng", "Thu hồi", "Online chọn; target đánh giá" | chờ điều phối viên duyệt |

Số liệu đã tính lại: bài tổng hợp (c): $r=(3;\,0)$, nhiễu $\pm1$: $\widehat r_1\in\{2;4\}>\widehat r_2\in\{-1;1\}$, $\mathbb E\max=3$, không chệch (trường hợp dấu bằng của Mệnh đề 09.2); $r(2)=2{,}5$: cực đại $2$; $3{,}5$; $4$; $4$, $\mathbb E\max=3{,}375$, chệch $+0{,}375$. Ghi chú: kế hoạch (CT §3.2) ghi "ước lượng tham lam chệch lên" cho bộ số của thẻ dữ kiện; tính lại cho thấy với khoảng cách $3$ và nhiễu $\pm1$ độ chệch bằng $0$, nên bài thêm biến thể $r(2)=2{,}5$ để có chệch lên. Tình huống 09.2: trung bình $\widehat g$ trên lượt của $\theta'=(0;0)$ là $(\tfrac12;-\tfrac12)$; với trọng số $\tfrac43$ khi $A=1$ thành $(\tfrac23;-\tfrac23)$. Số của notebook Bài 08 (ô 78, 81, 88): Lunar Lander, Double DQN $200{,}0$ trên năm hạt giống (từ $201{,}17$; $162{,}46$; $225{,}76$; $218{,}27$; $192{,}3$), cấu hình gốc $205{,}4$ trên cùng hạt giống, hiệu $-5{,}4$, $t=-0{,}38$; Flappy Bird, Double DQN $39{,}8$ trên ba hạt giống, cấu hình gốc $31{,}5$ trên cùng hạt giống, $t=0{,}76$.

Ghi chú bài giảng: `## 7. Tổng kết và chuyển tiếp` viết lại theo khuôn Bài 08 (Kết quả và giả thiết của bài, So sánh bốn phương pháp, Trả lời vấn đề trung tâm, Câu hỏi tự kiểm tra có lời giải, Bài tập về nhà và tài liệu đọc với chuyển tiếp Bài 10); thêm "## Tình huống áp dụng và ứng dụng" (Tình huống 09.1 Double DQN trên Lunar Lander và Flappy Bird với số đã kiểm và giới hạn; Tình huống 09.2 REINFORCE trên dữ liệu bộ nhớ phát lại, giả thiết không thỏa, có số và cách hiệu chỉnh; mục Ứng dụng: Bài 10, Rainbow), "## Tóm tắt chương" (đoạn bảy câu có số, kết quả theo mục, công thức cần nhớ, giả thiết hay bị quên), "## Bài tập củng cố" ba mức (nhận biết: bốn câu hỏi tự kiểm tra; tính toán hoặc chứng minh: Bài tập 09.1–09.6; vận dụng: 09.7, 09.8 và Bài tập 09.9 mới = bài tổng hợp của `L09-K3`/`L09-K4`), "## Hướng dẫn đọc thêm và tài liệu tham khảo" (chín tài liệu, mỗi tài liệu nói rõ phần dùng). Các khối Bài tập 09.1–09.8 chuyển từ cuối Mục 2–6 về mục bài tập củng cố, giữ số; 09.3, 09.5, 09.6, 09.8 bổ sung dữ kiện để tự đủ. Bỏ "Cầu nối: baseline và actor–critic", "Bốn hợp đồng cần giữ", "Bài tập củng cố" X01–X03 cũ.

Độ dài ghi chú bài giảng (quy ước của R5): thân văn 18 494 từ (≤ 20 000); `wc -w` 25 629.

Rà toàn deck của biên tập viên: `L09-02b` bảy tên khớp tên trang tiêu đề mạch và liên kết `#/1`…`#/7` mở `L09-01`, `L09-M2T`…`L09-M7T` (`hashcheck.py`: bấm cả bảy, phím mũi tên tới `L09-M7T`); năm mục tiêu `L09-02` ứng mạch 2–6; năm dòng `L09-K5` ứng năm dòng `L09-02c`; 17 `data-note-topic-id` của deck đều có trong ghi chú bài giảng và ngược lại; 63 `data-slide-id` duy nhất, 7 section ngoài, mọi trang có ghi chú. Mật độ: trang nội dung ≤ 60 âm tiết trừ `L09-01` (65, ngoại lệ đã ghi), `L09-02` (71), `L09-02c` (79), `L09-14` (73), `L09-K2` (63), `L09-K2b` (70), `L09-K5` (72), đều thuộc loại có trần 80. Ghi chú diễn giả 40–150 âm tiết trừ `L09-16` (161, đo với mỗi công thức là một token; mức `nhẹ`, để lại). `outline.md`: bảng note-topic-id (topic-13), số mã sau bước mạch 7 (63), bảng thời lượng bảy mạch, kiểm kê mười lăm SVG. `storyboard.md`: mục mạch 7 (S52–S61), danh sách trang theo mạch, rà toàn deck.

Kiểm sau bước mạch 7 (Playwright Chromium, `http://127.0.0.1:8799`, `check.py --all --narrow`, 1600×900 và 390×844): 63 trang, 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, không trang nào tràn; đáy mạch 7: `L09-M7T` 321, `L09-K1` 501, `L09-K1b` 584, `L09-K2` 666, `L09-K2b` 540, `L09-K3` 500, `L09-K4` 475, `L09-K5` 647, `L09-K6` 462, `L09-K7` 586 px (lần đầu `L09-K1` 894 px, `L09-K2` 712 px: tách bảng, rút chữ, nhóm công thức); đã xem ảnh 1600×900 của `L09-K1`, `L09-K1b`, `L09-K2`, `L09-K3`, `L09-K4`, `L09-K5`, `L09-K7`. Trình xem toàn ghi chú: 0 `.katex-error`, mọi khối `:::` nhận diện (gồm `application`), 0 yêu cầu ngoài, không cuộn ngang trang ở 1400 và 390 px; đã xem ảnh Tình huống 09.1 và Bài tập 09.9. `git diff --check` sạch.

### Rà lại mạch 7 (bước R7)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 7 và phần cuối ghi chú bài giảng (toán–RL, mạch, sinh viên–mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R7 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/R7-recheck.md` trong scratchpad phiên. Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 5 trung bình, 8 nhẹ. Điều phối viên duyệt mạch 7 (`check.py --all --narrow`, ảnh `L09-K1b`, `L09-K7`; tự tính $3{,}375$, $(\tfrac12;-\tfrac12)$, trọng số $\tfrac43$; xác nhận Bài 10 mở bằng đường cơ sở và actor–critic) và chấp nhận toàn bộ, kèm các chốt ở cột "quyết định".

| mức độ | vị trí | vấn đề | đề xuất | trạng thái | quyết định |
|---|---|---|---|---|---|
| trung bình | `L09-K5` | Lệch `L09-02c`: "chệch lên" thay "≥"; thiếu điều kiện của $\tfrac12$; dòng 3 thiếu "không chệch", dùng $5{,}5\to4{,}6$ làm bằng chứng; dòng 4 thiếu hành động liên tục và tiêu chí của $3{,}8$ | Khớp từng dòng | đã sửa ở R7: "chệch lên hoặc bằng ($\tfrac12$: hai $q_a$ bằng nhau, nhiễu $\pm1$)"; "Bản đánh giá không chệch, độc lập: không chệch lên; Double DQN chỉ gần thỏa"; "$\mathcal A$ liên tục hoặc đặc trưng gộp: học $\pi_\theta$ ($3{,}8$ bước, ô đầu đều)"; 76 âm tiết, đáy 644 px; bỏ câu siêu dữ liệu nguồn trong ghi chú diễn giả | chấp nhận |
| trung bình | `L09-K2b`; ghi chú diễn giả `L09-K6`; ghi chú bài giảng (bảng thứ hai Mục 7, Trả lời vấn đề trung tâm, Câu hỏi tự kiểm tra 2, Tình huống 09.1) | "Double DQN chỉ giảm độ chệch" không điều kiện | Câu có điều kiện | đã sửa ở R7: "gần thỏa điều kiện tách; không bảo đảm hết chệch lên, mức giảm phải đo bằng thí nghiệm" ở mọi chỗ | chấp nhận |
| trung bình | `L09-K1`, `L09-K1b` | Thiếu kết quả của mục tiêu 3, 4 | Thêm hàng; `L09-K1c` nếu vượt trần | đã sửa ở R7: hàng "Chính sách ngẫu nhiên khi gộp trạng thái" ở `L09-K1` (75 âm tiết, 635 px), hàng "Hàm điểm" thay hàng kỳ vọng ở `L09-K1b` (50 âm tiết, 633 px); không cần `L09-K1c` | chấp nhận |
| trung bình | ghi chú bài giảng, tài liệu tham khảo 1 | Sai học kỳ của nguồn | "học kỳ 2, 2025–2026" | đã sửa ở R7; đã tìm "Học kỳ 1, 2026–2027" trong ghi chú bài giảng và planning: không còn chỗ nào gắn với nguồn (dòng chân trang deck và tiêu đề ghi chú là học kỳ của học phần, đúng) | chấp nhận |
| trung bình | ghi chú bài giảng, độ dài; Mục 7 lặp số | Ba chỗ kể lại cùng bộ số | Giữ một chỗ | đã sửa ở R7: "Trả lời vấn đề trung tâm" còn năm câu điều kiện không kèm số và đoạn kết (số ở Tóm tắt chương); "Bài tập về nhà" bỏ câu phương sai; hai đoạn diễn bảng còn mỗi đoạn một câu | chấp nhận (thước đo: từ thân văn, quy ước R5) |
| nhẹ | `L09-K2` | Dấu chấm phẩy đứng riêng; "Double Q-" ngắt | Bỏ `<br>`; gạch nối không ngắt | đã sửa ở R7 (cả `L09-K1b`, `L09-K2b`) | chấp nhận |
| nhẹ | `L09-K1b` hàng định lý | Thiếu (G2) | Nêu đủ | đã sửa ở R7 | chấp nhận |
| nhẹ | `L09-K7` | Dòng Bài 10 thiếu TRPO, PPO | Câu thay thế | đã sửa ở R7 | chấp nhận |
| nhẹ | Tình huống 09.1 | Cấu hình tốt nhất gộp năm yếu tố | Kể đủ | đã sửa ở R7 | chấp nhận |
| nhẹ | Trả lời vấn đề trung tâm, đoạn kết | Câu kết không điều kiện | "chệch lên hoặc bằng" | đã sửa ở R7 | chấp nhận |
| nhẹ | ghi chú diễn giả `L09-K5` | Câu siêu dữ liệu nguồn | Xóa | đã sửa ở R7 | chấp nhận |
| nhẹ | Bài tập củng cố, mức nhận biết | Không có bài đánh số | Thêm bài | đã sửa ở R7: Bài tập 09.1 mới (phép cực đại trên ước lượng không chệch) có gợi ý, lời giải; các bài cũ dời số thành 09.2–09.10, mọi tham chiếu trong ghi chú cập nhật; bảng `Mạch \| Bài tập` của `L09-K7` và ghi chú diễn giả theo số mới | chấp nhận |
| nhẹ | ghi chú diễn giả `L09-16` | 166 âm tiết | Bỏ câu về $\epsilon$-tham lam | đã sửa ở R7: 143 | chấp nhận |

Độ dài ghi chú bài giảng sau R7: thân văn 18 373 (trước 18 494); `wc -w` 25 536.

Kiểm sau R7 (Playwright Chromium, `http://127.0.0.1:8799`, `check.py --all --narrow`, 1600×900 và 390×844): 63 trang, 0 trang tràn, 0 `.katex-error`, 0 lỗi console hoặc trang, 0 yêu cầu ngoài, không cuộn ngang; đáy mạch 7: `L09-K1` 635, `L09-K1b` 633, `L09-K2` 625, `L09-K2b` 502, `L09-K5` 644 (lần đầu 741 px, 88 âm tiết: rút ba dòng và dòng nguồn), `L09-K7` 630 px; đã xem ảnh 1600×900 của `L09-K1`, `L09-K1b`, `L09-K2`, `L09-K5`. Trình xem toàn ghi chú: 0 `.katex-error`, mọi khối `:::` nhận diện, 0 yêu cầu ngoài, không cuộn ngang trang ở 1400 và 390 px; đã xem ảnh mức nhận biết với Bài tập 09.1. `git diff --check` sạch. Trạng thái: chờ điều phối viên duyệt.

### Rà cuối từ góc nhìn sinh viên (bước F)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà cuối toàn deck từ góc nhìn sinh viên (63 trang, ảnh 1600×900, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập F | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/F-student.md` trong scratchpad phiên (văn bản trích kèm số âm tiết: `shots-F/dump.txt`). Kết quả: 0 chặn bàn giao, 2 nghiêm trọng, 7 trung bình, 16 nhẹ. Điều phối viên kiểm hai phát hiện nghiêm trọng trên deck và chấp nhận toàn bộ, kèm các chốt ở cột "quyết định". Mạch 7 đã commit (`9417fc3`, `d373d27`).

| mức độ | trang | vấn đề | trạng thái | quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L09-28` | (G1)–(G4) dùng trước khi phát biểu | đã sửa ở F: "Giả sử đổi được $\nabla_\theta$ với tích phân; điều kiện đủ nêu cùng định lý."; không đảo `L09-22` | chấp nhận (giữ trang vấn đề trước) |
| nghiêm trọng | `L09-16b` | $h_i$ không định nghĩa; $3{,}8$ không kiểm được | đã sửa ở F: "tính $h_i$, số bước kỳ vọng tới đích từ ô $i$"; hình thêm hàng $h_i$: $5,4,1,4,5$; "Diễn giải:" $(5+4+1+4+5)/5=3{,}8$; 48 âm tiết, đáy 638 px | chấp nhận |
| trung bình | `L09-13` | nhắc ví dụ trước bằng lời; thứ tự hàng bảng ngược `L09-08` | đã sửa ở F: `double-q-example.svg` hàng trên $Q_2$ (đánh giá), hàng dưới $Q_1$ (chọn), mũi tên đi lên như `ddqn-example.svg`; "Diễn giải:" nêu vai tại chỗ; ghi chú bài giảng sửa `alt` và câu đọc hình | chấp nhận |
| trung bình | `L09-06b` | cụm "một bản cho cả hai việc" | đã sửa ở F | chấp nhận |
| trung bình | `L09-K1`, `L09-K5` | cụm rút gọn khó giải mã | đã sửa ở F | chấp nhận |
| trung bình | `L09-02c` | dòng 3, 4, 6 dùng khái niệm chưa học | đã sửa ở F (viết bằng lời; công thức ở `L09-K5`); ngoại lệ mật độ 94 âm tiết ghi trong storyboard | chấp nhận |
| trung bình | `L09-23` | trực quan không nói tổng nào cần thành kỳ vọng | đã sửa ở F | chấp nhận |
| trung bình | `L09-30` | $\nu^\pi_\gamma$ xuất hiện đột ngột | đã sửa ở F: "Dạng khác" giữ trên mặt trang với cụm định nghĩa ngắn "phân bố chiếm dụng chiết khấu … tần suất thăm $s$, lượt muộn tính nhẹ hơn"; ghi chú bài giảng thêm câu đọc $\nu^\pi_\gamma$ bằng lời | chấp nhận (theo chốt: cụm định nghĩa ngắn) |
| trung bình | `L09-17`, `L09-19` | $\theta$ đổi vai; $\phi$ chưa nhắc | đã sửa ở F; `L09-16` ghi "đặc trưng $x(s)$" | chấp nhận |
| trung bình | `L09-29b` | ba ước lượng không có nhãn | đã sửa ở F: (i), (ii), (iii) và hai hiệu; ghi chú bài giảng Ví dụ 09.18 cùng nhãn | chấp nhận |
| nhẹ | `L09-07` | "dạng từng trường hợp" | đã sửa ở F | chấp nhận |
| nhẹ | `L09-06c` | $-0{,}125$ không có phép tính | đã sửa ở F | chấp nhận |
| nhẹ | `L09-03` | nguồn của $108{,}5$; γ trong SVG giống "y" | đã sửa ở F: dòng "Ví dụ." nêu thực hành Bài 08; γ trong `cartpole-overestimate.svg`, `reinforce-trajectory.svg` dùng phông có chân, nghiêng | chấp nhận |
| nhẹ | `L09-27` | nghĩa của $c$ | đã sửa ở F | chấp nhận |
| nhẹ | `L09-15` | nhãn "Giới hạn chung:" | đã sửa ở F ("Lưu ý:") | chấp nhận |
| nhẹ | `L09-02`, `L09-20` | "mục tiêu" ba nghĩa | đã sửa ở F: `L09-20` nêu hàm mục tiêu khác mục tiêu $y_i$; kiểm deck: mọi chỗ nói $J$ viết "hàm mục tiêu" | chấp nhận |
| nhẹ | `L09-16`, `L09-16b` | "tất định" và "xác định" của Bài 04 | đã sửa ở F: "tất định (Bài 04: xác định)" ở lần dùng đầu trên mặt trang `L09-16` | chấp nhận |
| nhẹ | `L09-21` | "$\phi$ đơn vị" | đã sửa ở F: nêu $\phi(s,1)$, $\phi(s,2)$; đạo hàm softmax đã có trong ghi chú diễn giả; không thêm thẻ (không đủ chỗ) | chấp nhận |
| nhẹ | `L09-30A` | "thương" | đã sửa ở F | chấp nhận |
| nhẹ | `L09-26` | `\text{hằng số}` lệch dấu thanh | đã sửa ở F; ghi chú bài giảng: bỏ mọi `\text{}` chữ Việt (năm chỗ: hai khối `aligned` có chú thích, hai chỗ "nên"), chú thích chuyển ra văn xuôi | chấp nhận |
| nhẹ | `L09-14`, `L09-29` | số hiệu ghi chú không đối chiếu được | đã sửa ở F: thay bằng điều kiện hoặc bỏ | chấp nhận |
| nhẹ | `L09-22` | đánh số kép | đã sửa ở F | chấp nhận |
| nhẹ | `L09-K2`, `L09-K2b` | thứ tự, tên hàng khác nhau | đã sửa ở F | chấp nhận |
| nhẹ | `L09-K1b` | giả thiết Double Q-learning là cơ chế | đã sửa ở F | chấp nhận |
| nhẹ | `L09-K7` | dòng trạng thái; "actor–critic" | đã sửa ở F: "Bài tập: mục Bài tập củng cố của ghi chú bài giảng."; "actor–critic" giữ nguyên là tên phương pháp theo bảng thuật ngữ của `outline.md` | chấp nhận một phần (tên phương pháp giữ) |
| nhẹ | `L09-01` | "tách chọn khỏi đánh giá" chưa rõ | đã sửa ở F | chấp nhận |
| nhẹ | ghi chú diễn giả `L09-16`, `L09-21`, `L09-26`, `L09-25`, `L09-06b`, `L09-02c`, `L09-K5`, `L09-03`, `L09-16b` | thông tin quy trình, "Nguồn hỏi…", nhắc trang khác bằng lời, câu mở siêu văn bản; bốn ghi chú dài | đã sửa ở F: bỏ "sai khác có chủ ý so với nguồn" (giữ trong review-log, storyboard), viết lại "Nguồn hỏi" thành câu khẳng định, thay "ở trang định nghĩa" bằng số liệu, bỏ "Dòng số N…"; mọi ghi chú ≤ 150 âm tiết theo cách đếm của `dens.py` (`L09-16b` 108, `L09-K5` 114, `L09-03` 111, `L09-16` 117) | chấp nhận |

Ghi chú bài giảng đổi theo trang: `alt` của `aliased-grid-stochastic.svg` (hàng $h_i$), `alt` và câu đọc hình của `double-q-example.svg`, Ví dụ 09.18 nhãn (i), (ii), (iii), câu đọc $\nu^\pi_\gamma$ bằng lời sau Hệ quả 09.23, bỏ `\text{}` chữ Việt. Độ dài: thân văn 18 460 từ; `wc -w` 25 646.

Kiểm sau F (Playwright Chromium, `http://127.0.0.1:8799`, `check.py --all --narrow`, 1600×900 và 390×844): 63 trang, 0 trang tràn, 0 `.katex-error`, 0 lỗi console hoặc trang, 0 yêu cầu ngoài, không cuộn ngang (lần đầu `L09-13` 736, `L09-16b` 736, `L09-K1` 725 px, `L09-03` 702 px: rút chữ, rút cột bảng); đã xem ảnh 1600×900 của `L09-02c`, `L09-03`, `L09-06b`, `L09-13`, `L09-16b`, `L09-19`, `L09-20`, `L09-22`, `L09-23`, `L09-26`, `L09-27`, `L09-28`, `L09-29b`, `L09-30`, `L09-K1`, `L09-K1b`, `L09-K2b`, `L09-K5`, `L09-K7`. Trình xem toàn ghi chú: 0 `.katex-error`, mọi khối `:::` nhận diện, 0 yêu cầu ngoài, không cuộn ngang trang. `git diff --check` sạch. Trạng thái: chờ điều phối viên duyệt.

### Bước F2 (sửa theo rà lại bước F)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại bước F (chỉ đọc, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập F2 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Báo cáo: `review/RF-recheck.md` trong scratchpad phiên. Kết quả: 0 chặn bàn giao, 0 nghiêm trọng, 2 trung bình, 7 nhẹ. Điều phối viên duyệt bước F (`check.py --all --narrow`, ảnh `L09-02c`, `L09-16b`) và chấp nhận toàn bộ.

| mức độ | vị trí | vấn đề | trạng thái | quyết định |
|---|---|---|---|---|
| trung bình | `L09-02c`, `L09-K5` | dòng 3 lặp từ, 22 âm tiết; dòng 6 thiếu đặc trưng bị chặn; tổng 94 | đã sửa ở F2: bộ câu thay của báo cáo; 78 âm tiết, mỗi dòng ≤ 19; `L09-K5` cùng câu dòng 3 và hộp; gỡ ngoại lệ 94 trong storyboard | chấp nhận |
| trung bình | `L09-30` | $\nu^\pi_\gamma$ "lượt muộn" sai nghĩa | đã sửa ở F2: "lần thăm ở bước muộn tính nhẹ hơn"; ghi chú bài giảng cùng chữ | chấp nhận |
| nhẹ | `L09-01` | luận đề "tách … làm giảm" không điều kiện | đã sửa ở F2: "đánh giá bằng một ước lượng không chệch, độc lập với ước lượng chọn bỏ được phần chệch lên này" (một câu; 75 âm tiết, ngoại lệ bìa ghi trong storyboard) | chấp nhận |
| nhẹ | `L09-16b` | `alt` cũ; chính sách ở ô xám chỉ có trong hình | đã sửa ở F2 (55 âm tiết, 690 px) | chấp nhận |
| nhẹ | `L09-23` | công thức một bước đọc như công thức chung | đã sửa ở F2 ("Bài toán một bước:") | chấp nhận |
| nhẹ | `L09-28` | câu giả thiết dưới nhãn "Ký hiệu:" | đã sửa ở F2 (dòng "Giả thiết:" riêng; 696 px) | chấp nhận |
| nhẹ | `L09-14`, `L09-K5` | vượt trần 80 | đã sửa ở F2: 72 và 78 | chấp nhận |
| nhẹ | ghi chú bài giảng, sau Hệ quả 09.23 | $\mu$ dùng cho phân bố trạng thái | đã sửa ở F2: $\eta(s)=\sum_t\gamma^t\Pr(S_t=s)$ không chuẩn hóa | chấp nhận |
| nhẹ | ghi chú bài giảng, đầu mục Hàm điểm | dấu phẩy thừa trước $\Longrightarrow$ | đã sửa ở F2 | chấp nhận |

Kiểm sau F2 (Playwright Chromium, `http://127.0.0.1:8799`, `check.py --all --narrow`, 1600×900 và 390×844): 63 trang, 0 trang tràn, 0 `.katex-error`, 0 lỗi console hoặc trang, 0 yêu cầu ngoài, không cuộn ngang; đã xem ảnh 1600×900 của `L09-01`, `L09-02c`, `L09-16b`, `L09-28`. Trình xem toàn ghi chú: 0 `.katex-error`, mọi khối `:::` nhận diện, không cuộn ngang trang. Ghi chú bài giảng: thân văn 18 466 từ, `wc -w` 25 653. `git diff --check` sạch.

**Trạng thái bàn giao:** đợt sửa 2026-10-28 của Bài 09 (C0, mạch 1–7, R1–R7, F, F2) đã xong phần biên tập; chờ điều phối viên ký duyệt.

### Ký duyệt của điều phối viên (2026-10-28)

- Bước F (rà cuối từ góc nhìn sinh viên, tác tử độc lập Agent `general-purpose`, `claude-opus-5-5`, high, chỉ đọc), rà lại bước F (tác tử rà lại của đợt, cùng mô hình) và bước F2 (biên tập viên): **chấp nhận**.
- Căn cứ: điều phối viên tự chạy Playwright (`check.py --all --narrow`, 63 trang, 1600×900 và 390×844): 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ra ngoài máy chủ cục bộ, không tràn khung, không cuộn ngang; xem ảnh `L09-01`, `L09-02c`, `L09-16b`, `L09-28`; tự tính lại $h_i=5,4,1,4,5$ và trung bình $3{,}8$.
- Mọi phát hiện chặn bàn giao và nghiêm trọng của ba rà soát đầu, bảy lượt rà lại theo mạch và lượt rà cuối đã xử lý và ghi ở các mục trên.
- Giới hạn còn lại: chưa có `exercises.md` và notebook thực hành cho Bài 09 (thẻ index ghi "Chưa có"); ghi chú bài giảng dài 18 466 từ thân văn (25 646 theo `wc -w`); bìa `L09-01` giữ ngoại lệ mật độ (luận đề một câu có điều kiện).

### Sửa theo phản hồi người dùng (2026-10-28): L09-23

Phản hồi của người dùng: "slide HÀM ĐIỂM không rõ đang từ J=E[G_0] sao có thể có ∇J = … được". Chẩn đoán của điều phối viên: thiếu hai bước, $J=\sum_a\pi_\theta(a\mid s)r(a)$ (vì $G_0=r(A_0)$) và $\nabla_\theta r=0$, trước bước nhân, chia cho $\pi_\theta$. Biên tập: Agent `general-purpose` (biên tập viên của đợt sửa), `claude-opus-5-5`, high; `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt.

| vị trí | thay đổi | trạng thái | quyết định |
|---|---|---|---|
| `L09-23` | tách thành hai trang. `L09-23` "Gradient của $J$ trên bài toán một bước": khối `aligned` bốn dòng $J=\sum_a\pi_\theta r$ → $\sum_ar\nabla\pi_\theta$ ($\nabla_\theta r=0$) → $\sum_a\pi_\theta r\nabla\log\pi_\theta$ (nhân, chia $\pi_\theta>0$) → $\mathbb E_{A\sim\pi_\theta}[r(A)\nabla\log\pi_\theta(A\mid s)]$; "Ý nghĩa:" một hành động cho một mẫu, không cần $r$ của mọi hành động, không cần sai phân; bỏ dòng ví dụ trùng `L09-25`; ghi chú diễn giả giải thích bước nhân, chia (107 âm tiết) | đã sửa | chờ điều phối viên duyệt |
| `L09-23b` (mới) | "Hàm điểm": Định nghĩa, $\nabla\pi=\pi\psi$, $\nabla J=\mathbb E[r(A)\psi_\theta(s,A)]$ trên bài toán một bước, Lưu ý miền hỗ trợ cố định | đã sửa | chờ điều phối viên duyệt |
| `L09-25`, `L09-25b` | kiểm nối: `L09-25` tính $\psi_\theta(s,1)$, $\psi_\theta(s,2)$ bằng công thức softmax của `L09-24` (không lặp dẫn xuất); `L09-25b` dùng $\nabla\pi=\pi\psi$ của `L09-23b`; không đổi | đã kiểm | chờ điều phối viên duyệt |
| ghi chú bài giảng, Mục 5 "Hàm điểm" | đoạn mở viết cùng chuỗi suy ra với lý do từng bước (khối `aligned` bốn dòng, câu chú thích từng dòng) và nêu vì sao dạng kỳ vọng có ích | đã sửa | chờ điều phối viên duyệt |
| `outline.md`, `storyboard.md` | topic-08 thêm `L09-23b`; 64 mã; bảng thời lượng mạch 5; mục sửa với hành trình sáu bước của cụm hàm điểm | đã sửa | chờ điều phối viên duyệt |

Kiểm: `check.py` `L09-30A`, `L09-23`, `L09-23b`, `L09-24`, `L09-25`, `L09-25b` (1600×900, 390×844): không tràn (lần đầu `L09-23` tràn phải 1338 px, rút chú thích dòng ba còn $(\times\tfrac{\pi_\theta}{\pi_\theta},\ \pi_\theta>0)$; đáy 609 và 455 px), 0 lỗi, 0 `.katex-error`; đã xem ảnh 1600×900 của `L09-23`, `L09-23b`. `hashcheck.py`: 64 `data-slide-id` duy nhất, 7 section ngoài, mọi trang có ghi chú. Trình xem: 0 `.katex-error`, không cuộn ngang trang. Ghi chú bài giảng: thân văn 18 556 từ. `git diff --check` sạch.

Rà lại sửa `L09-23` (Agent `general-purpose`, `claude-opus-5-5`, high, chỉ đọc; báo cáo `review/R-L0923.md`): 0 chặn bàn giao, 0 nghiêm trọng, 1 trung bình, 3 nhẹ. Điều phối viên chấp nhận toàn bộ.

| mức độ | vị trí | vấn đề | trạng thái | quyết định |
|---|---|---|---|---|
| trung bình | `L09-23` → `L09-23b`; `L09-25` ghi chú; `L09-28` | mất bước ví dụ có số trước định nghĩa; ghi chú `L09-25` dẫn tới phép tính không còn; `L09-28` lặp phép tính | đã sửa: `L09-23` thêm "Ví dụ." $\theta=(\log2;0)$, $r=(3;0)$: $\nabla_\theta\log\pi_\theta(1\mid s)=(\tfrac13;-\tfrac13)$, vế phải $\tfrac23\cdot3(\tfrac13;-\tfrac13)=(\tfrac23;-\tfrac23)$, khớp tính trực tiếp; `L09-28` thay ví dụ bằng "Nhắc lại:" $\nabla_\theta J=\mathbb E[r(A)\psi_\theta(s,A)]=(\tfrac23;-\tfrac23)$; ghi chú `L09-25` trỏ tới giá trị trong dẫn xuất gradient một bước; ghi chú bài giảng Ví dụ 09.14 thêm vế phải của dẫn xuất, Ví dụ 09.17 kiểm lại theo Ví dụ 09.14 | chấp nhận |
| nhẹ | `L09-23` "Trực quan." | $s$ cố định; $A_0$ và $A$ | đã sửa: "$s$ cố định, $A=A_0\sim\pi_\theta(\cdot\mid s)$, $G_0=r(A)$" | chấp nhận |
| nhẹ | `L09-23` nhãn lý do | "$\times\tfrac{\pi_\theta}{\pi_\theta}$" khó đọc | đã sửa: bỏ nhãn trong khối công thức (tránh chữ Việt trong KaTeX), thêm dòng chữ "Dòng một: $\nabla_\theta r=0$; dòng hai: nhân và chia cho $\pi_\theta>0$." | chấp nhận |
| nhẹ | `L09-23b` | thiếu "Ý nghĩa:" | đã sửa: "$\psi_\theta(s,a)$ là thay đổi tương đối của $\pi_\theta(a\mid s)$ theo $\theta$; bước nhỏ theo nó tăng $\pi_\theta(a\mid s)$." | chấp nhận |

Kiểm sau rà lại: `check.py` `L09-21`, `L09-30A`, `L09-23`, `L09-23b`, `L09-24`, `L09-25`, `L09-25b`, `L09-28` (1600×900, 390×844): không tràn (lần đầu `L09-23` 851 px, rồi 753 px: rút khối công thức còn ba dòng, đưa $J=\sum_a\pi_\theta r$ lên dòng "Trực quan.", rút "Ý nghĩa:"; sau sửa 659 px), 0 lỗi, 0 `.katex-error`; đáy `L09-23b` 578, `L09-28` 688 px; âm tiết `L09-23` 35, `L09-23b` 37, `L09-28` 37; đã xem ảnh 1600×900 của `L09-23`, `L09-23b`, `L09-28`. Trình xem: 0 `.katex-error`, không cuộn ngang trang. `git diff --check` sạch. Trạng thái: chờ điều phối viên duyệt.

Sửa thêm (yêu cầu điều phối viên, 2026-10-28): dòng "Ví dụ." của `L09-23` nêu đủ dữ kiện để kiểm $(\tfrac13;-\tfrac13)$ tại chỗ — softmax, $\phi(s,1)=(1;0)$, $\phi(s,2)=(0;1)$, $\theta=(\log2;0)$, $r=(3;0)$, $\pi_\theta=(\tfrac23;\tfrac13)$, vế phải $(\tfrac23;-\tfrac23)$. Phát hiện và hoàn tác một thay thế nhầm vào dòng "Ví dụ." của `L09-21` (trả về bản HEAD). `check.py` `L09-21`, `L09-23` (1600×900, 390×844): đáy 597 px và 660 px, 0 lỗi KaTeX/console; `L09-23` 32 âm tiết, ghi chú 111; ảnh đã xem; `git diff --check` sạch. Chấp nhận.

### Sửa theo phản hồi người dùng (2026-10-28): L09-29

Phản hồi: "chứng minh quá tắt". Người sửa: tác tử biên tập (general-purpose, Opus 5.5, effort high), theo yêu cầu của điều phối viên.

| mức độ | vị trí | vấn đề | trạng thái | quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L09-29` | lập luận dồn vào hai dòng: không nêu vì sao $\mathbb E[\psi_t\mid H_t]=0$, vì sao $G_{<t}$ ra khỏi kỳ vọng có điều kiện, cách cộng theo $t$; thiếu bước trực quan | đã sửa: `L09-29` ("Nhu cầu:", "Trực quan.", hình `past-reward-timeline.svg`, dòng tách lợi tức); `L09-29a` mới ("Nhắc lại:", "Bổ đề." với giả thiết nêu bằng lời, "Ý nghĩa:"); `L09-29b` giữ nguyên số, đứng sau phát biểu; `L09-29c`, `L09-29d` mới ("Chứng minh:", Bước 1–4, `aligned` một quan hệ mỗi dòng, lý do từng dòng, $\square$) | chấp nhận |
| trung bình | ghi chú bài giảng Mục 6 | bước bỏ phần thưởng quá khứ không có khối kết quả và chứng minh riêng; Bổ đề 09.21 là gradient của log xác suất quỹ đạo, không phải kết quả này | đã sửa: thêm Bổ đề 09.22 (Phần thưởng quá khứ và hàm điểm), chứng minh bốn bước cùng lý do, đoạn đọc hình dòng thời gian, đoạn vai trò giả thiết; Bước 5 của Định lý dẫn Bổ đề 09.22; các kết quả sau đánh số lại 09.23–09.27 (ghi chú diễn giả `L09-K6` đổi "Định lý 09.22" thành "Định lý 09.23"; `outline.md` đổi "Thuật toán 09.24" thành "Thuật toán 09.25"); Ví dụ 09.18 dẫn Bổ đề 09.22 | chấp nhận |

Kiểm: `check.py` `L09-28A`, `L09-29`, `L09-29a`, `L09-29b`, `L09-29c`, `L09-29d`, `L09-22` (1600×900, 390×844): đáy 596, 570, 610, 609, 629, 691, 507 px, 0 lỗi KaTeX, console, yêu cầu ngoài; âm tiết 32, 50, 38, 36, 28; ghi chú diễn giả 83, 93, 94, 103, 91; ảnh đã xem. 67 `data-slide-id` duy nhất, 7 section ngoài. So section với HEAD: chỉ `L09-29`, `L09-K6` (số hiệu trong ghi chú) đổi; thêm `L09-29a`, `L09-29c`, `L09-29d`. Trình xem ghi chú: 0 lỗi KaTeX, không khối `:::` thô, hình mới tải được, không yêu cầu ngoài, không tràn ngang ở 1400 và 390 px; thân bài 19 058 từ. `git diff --check` sạch. no-ai-slop Edit trên văn bản mới của bốn trang, ghi chú diễn giả và ghi chú bài giảng Mục 6; tự kiểm `eval.md`: đạt (không câu dẫn, không câu hỏi tu từ, không tổng kết lặp). Thời lượng mạch 6 giữ 20 phút (phân lại trong `storyboard.md`).

Rà lại R-L0929 (tác tử rà lại chỉ đọc; điều phối viên chấp nhận toàn bộ):

| mức độ | vị trí | vấn đề | trạng thái | quyết định |
|---|---|---|---|---|
| trung bình | `L09-29a`; Bổ đề 09.22 | "$G_0$ bị chặn" không kéo theo $G_{<t}$ bị chặn; Bước 4 cần $T$ bị chặn; $\psi_t$ chỉ xác định khi $t<T$ | đã sửa: giả thiết $|R_{t+1}|\le R_{\max}$, $T\le T_{\max}$ ở cả deck và ghi chú; quy ước $\psi_t=0$ khi $t\ge T$ (tức $\mathbf 1\{t<T\}\psi_t$) ở `L09-29a`, ghi chú diễn giả `L09-29d` và kết luận bổ đề; Bước 2 nêu sự kiện $\{t<T\}$ xác định bởi $H_t$; Bước 4 viết tổng tới $T_{\max}$ với lý do từng dòng; đoạn vai trò giả thiết nêu vì sao chỉ chặn $G_0$ không đủ; Bước 5 của Định lý 09.23 dẫn chặn theo (G3) | chấp nhận |
| nhẹ | `L09-29a`; Bổ đề 09.22 | điều kiện cho hành động liên tục không có trong giả thiết | đã sửa: mặt trang "(tích phân nếu hành động liên tục)", ghi chú diễn giả thêm một câu; ghi chú bài giảng thêm giả thiết mật độ và đổi $\nabla_\theta$ với tích phân như Mệnh đề 09.17 | chấp nhận |
| nhẹ | thứ tự `L09-29a` → `L09-29b` → `L09-29c` | ví dụ sau phát biểu chưa được ghi là lệch quy tắc hành trình | đã sửa: `storyboard.md` ghi lệch có chủ ý với lý do (phép kiểm dùng kết luận bổ đề với $t=1$; ví dụ dẫn nhập là `L09-28`; ghi chú đặt Ví dụ 09.18 sau chứng minh) | chấp nhận |
| nhẹ | `L09-29d` | đáy 691 px; thiếu lý do dòng hai của Bước 3 và Bước 4 | đã sửa: lý do Bước 3 chuyển lên câu mở (gồm "$G_{<t}$ là hàm của $H_t$, nên là hằng khi biết $H_t$"); Bước 4 "dòng một: Bước 1; dòng hai: hạng đầu bằng $0$ theo Bước 3"; đáy 655 px | chấp nhận |

Kiểm sau rà lại: `check.py` `L09-29`, `L09-29a`, `L09-29b`, `L09-29c`, `L09-29d` (1600×900, 390×844): đáy 570, 653, 609, 629, 655 px, 0 lỗi; âm tiết 32, 57, 38, 36, 32; ghi chú diễn giả 83, 122, 94, 103, 92; ảnh đã xem. Trình xem: 0 lỗi KaTeX, không khối thô, không yêu cầu ngoài, không tràn ngang. 67 `data-slide-id`, 7 section ngoài. `git diff --check` sạch. no-ai-slop Edit trên câu mới, tự kiểm `eval.md`: đạt.

### Giai đoạn III: bài tập `exercises.md` (2026-10-28)

Yêu cầu người dùng: "bổ sung bài tập … ý là bài tập từ Barto Sutton". Người soạn: tác tử biên tập (general-purpose, Opus 5.5, effort high), theo yêu cầu của điều phối viên; chưa qua ba vai rà soát của giai đoạn III.

Nguồn: Sutton và Barto (2018), PDF tác giả `/data/tqlong/qa/sources/sutton-barto-rl2020/original.pdf` và văn bản trích; dấu trừ bị mất khi trích đã đối chiếu bằng ảnh trang (PDF tr. 156: phần thưởng $\mathcal N(-0{,}1;\,1)$ ở Ví dụ 6.7; tr. 345: phần thưởng $-1$, giá trị $-44$, $-82$, $-11{,}6$ ở Ví dụ 13.1). Đề bài phát biểu lại bằng ký hiệu ghi chú Bài 09, không dịch nguyên văn; lời giải tự viết.

| bài | tên | nguồn Sutton và Barto (2018) | mức | mạch |
|---|---|---|---|---|
| 09.11 | MDP độ chệch cực đại | Ví dụ 6.7 | nhận biết | 2, 3 |
| 09.12 | Hành lang ngắn và chính sách tất định | Ví dụ 13.1 | nhận biết | 4 |
| 09.13 | Double Expected Sarsa | Bài tập 6.13 | tính toán | 3 |
| 09.14 | Xác suất tối ưu trên hành lang ngắn | Bài tập 13.1 | tính toán | 4 |
| 09.15 | Hàm điểm softmax với mức ưu tiên tổng quát | Bài tập 13.3, mở rộng (mức ưu tiên phi tuyến, ba hành động có số) | chứng minh, tính toán | 5 |
| 09.16 | Đơn vị Bernoulli–logistic | Bài tập 13.5 | tính toán | 4, 5, 6 |
| 09.17 | Định lý gradient chính sách có chiết khấu theo phương trình Bellman | Bài tập 13.2 | chứng minh | 6 |
| 09.18 | Q-learning và Double Q-learning trên MDP độ chệch cực đại | Ví dụ 6.7, Hình 6.5 | vận dụng (lập trình) | 2, 3 |
| 09.19 | REINFORCE trên hành lang ngắn | Ví dụ 13.1, Hình 13.1 | vận dụng (lập trình) | 6 |
| 09.20 | Gradient đúng và một mẫu REINFORCE trên hành lang ngắn | Ví dụ 13.1 | vận dụng | 5, 6 |

Bỏ: Bài tập 13.4 (hàm điểm Gaussian hai phần) vì trùng góc hỏi với Bài tập củng cố 09.5(b) (hàm điểm theo trung bình) và 09.7 (học $\sigma=e^\omega$); chỉ khác ở vector đặc trưng của $\sigma$, không đổi được góc hỏi rõ rệt. Bài tập 13.3 chỉ giữ ở dạng mở rộng (09.15), vì dạng tuyến tính là Mệnh đề 09.16 của ghi chú. Bài tập 13.2 giữ vì đường chứng minh (phương trình Bellman của $\nabla v_\pi$) khác chứng minh của Định lý 09.23 (xác suất quỹ đạo).

Tính lại bằng chương trình (thư viện chuẩn Python, scratchpad `ex09/`): $J(p)=-2(2-p)/\bigl(p(1-p)\bigr)$ khớp lặp giá trị tại $p=\tfrac12$ ($v=(-12;\,-10;\,-6)$); $p^*=2-\sqrt2$, $J(p^*)=-(6+4\sqrt2)\approx-11{,}657$, $J(0{,}95)\approx-44{,}21$, $J(0{,}05)\approx-82{,}11$; $\nabla_\theta J(0;\,0)=(2;\,-2)$; lượt $1,1,1,2,1$ cho $\widehat g=(-5{,}5;\,5{,}5)$, $p$ mới $\approx0{,}2497$, $J\approx-18{,}68$; mô phỏng $400\,000$ lượt (hạt giống 1): trung bình $1{,}964$, độ lệch chuẩn $26{,}98$, sai số chuẩn $0{,}043$. Bernoulli–logistic: $P=0{,}3775$, $\theta$ mới $(0{,}6245;\,0{,}2510)$, $P$ mới $0{,}5306$. Softmax ba hành động: $\pi$ sau bước $\approx(0{,}319;\,0{,}291;\,0{,}390)$. Mô phỏng MDP độ chệch cực đại ($1000$ lần chạy, hạt giống 2026, 2027) và REINFORCE trên hành lang ($100$ lần chạy, hạt giống $100+k$, $212$) ghi trong lời giải 09.18, 09.19, nêu rõ là một lần chạy của người soạn.

Cập nhật kèm: `L09-K7` (bảng `Mạch | Bài tập`, dòng nguồn, liên kết "Ghi chú bài giảng · Bài tập", ghi chú diễn giả); ghi chú bài giảng mục "Bài tập về nhà và tài liệu đọc" trỏ tới tệp bài tập; `index.html` thẻ Bài 9, nhóm Bài tập là liên kết viewer (Thực hành vẫn "Chưa có"); `storyboard.md` mục `L09-K7`.

Kiểm: trình xem `exercises.md` ở 1400 và 390 px: 30 khối `:::` nhận diện (10 `exercise`, 10 `hint`, 10 `solution`), 0 lỗi KaTeX, 0 khối thô, không yêu cầu ngoài, không tràn ngang; bảy liên kết `#/N/1` mở đúng `L09-01`, `L09-M2T`…`L09-M7T` (Playwright). `check.py` `L09-K7` (1600×900, 390×844): đáy 674 px, 0 lỗi; 61 âm tiết (trần 80), ghi chú diễn giả 124; ảnh đã xem. Tệp mới không bị `.gitignore` chặn (quy tắc `!2627-1/materials/**`). `git diff --check` sạch. no-ai-slop Edit trên toàn tệp, tự kiểm `eval.md`: đạt. Chưa có: ba vai rà soát chỉ đọc của giai đoạn III.

Rà soát giai đoạn III (hai vai chỉ đọc: EX-math toán–RL, 1 trung bình, 5 nhẹ; EX-student sinh viên–sư phạm và no-ai-slop Detect, 5 trung bình, các mục nhẹ). Điều phối viên tự tính lại hành lang ngắn và chấp nhận toàn bộ, trừ hai mục ghi dưới. Người sửa: tác tử biên tập (general-purpose, Opus 5.5, effort high).

| mức độ | nguồn | vị trí | vấn đề | trạng thái | quyết định |
|---|---|---|---|---|---|
| trung bình | EX-math, EX-student | "Hướng dẫn và ký hiệu" | $\gamma=1$ và độ dài lượt không bị chặn, trong khi ghi chú phát biểu Định lý 09.23, Hệ quả 09.26 với $\gamma<1$, $T\le T_{\max}$ | đã sửa: đoạn "Quy ước chiết khấu" nêu $T\le2$ ở MDP độ chệch cực đại; trên hành lang ngắn, $0<p<1$ cho $\Pr(T>3n)\le(1-p^2(1-p))^n$, mọi mô men của $T$ hữu hạn; kết luận chứng minh theo đường Bài tập 09.17 với chuỗi, $\mathbb E[\sum_t\lvert G_t\rvert\lVert\psi_t\rVert]\le\sqrt2\,\mathbb E[T^2]$; Định lý 09.23 ở đoạn đầu kèm "dưới (G1)–(G4)" | chấp nhận |
| trung bình | EX-student; nhẹ EX-math | 09.17 | $p(s',r\mid s,a)$ khác ký hiệu $P$ của ghi chú; dẫn số công thức của sách | đã sửa: $P(s',r\mid s,a)$, ghi một lần "Sutton và Barto viết $p$"; dạng không chiết khấu viết ra tại chỗ; bỏ "(13.9) của nguồn" ở 09.15 | chấp nhận |
| trung bình | EX-student | 09.18, 09.19 | `assert` không có hàm để gọi | đã sửa: khung có `update_left` (hai `assert` cho bước Q-learning $0{,}035$ và Double Q-learning $-0{,}030$), `grad_estimate` và `assert` cho `step`, `grad_estimate([1,1,1,2,1], 0.5) == (-5.5, 5.5)`; cài đặt tham chiếu chạy qua cả bốn `assert` | chấp nhận |
| trung bình | EX-student; nhẹ EX-math | 09.18 "Kiểm tra lại." | ngưỡng cứng $5\%$ sai với dao động lấy mẫu | đã sửa: sai số chuẩn $\approx0{,}7$ điểm phần trăm trên $1000$ lần chạy; dấu hiệu lỗi khi dưới khoảng $3{,}6\%$ qua nhiều lượt | chấp nhận |
| trung bình | EX-student | gợi ý 09.14 | lộ $v_1=v_2-1/p$ và $f(p)$ | đã sửa: chỉ hướng bước đầu (biểu diễn theo $v_2$, viết $J=-cf$ rồi lấy đạo hàm của $\log f$) | chấp nhận |
| nhẹ | EX-student | gợi ý 09.20 | đưa sẵn $J'(p)$ | đã sửa: gợi ý quy tắc thương và $\mathrm dp/\mathrm d(\theta_1-\theta_2)=p(1-p)$; lời giải (a) dẫn $J'(p)$ từng bước | chấp nhận |
| nhẹ | EX-math, EX-student | 09.19 (b) | thiếu sai số chuẩn; câu "lên gần $-12$" mâu thuẫn với $-15{,}1$ | đã sửa: $-11{,}87$ ($0{,}11$), $-12{,}50$ ($0{,}11$), $-15{,}10$ ($0{,}14$); $p$ cuối $0{,}550$ ($0{,}004$), $0{,}470$ ($0{,}003$), $0{,}343$ ($0{,}002$), chạy lại `reinforce_se.py`; câu định tính "về phía $-12$, $\alpha=2^{-14}$ mới tới khoảng $-15$" | chấp nhận |
| nhẹ | EX-math | 09.19 (c) | "bước nhỏ" chưa nói so với gì | đã sửa: độ trôi trong lượt cỡ $\alpha T^2$; nhỏ so với $1$; với $T=1000$, $\alpha=2^{-12}$ cỡ $240$ | chấp nhận |
| nhẹ | EX-math | 09.20 (d) | số mô phỏng thiếu hạt giống | đã sửa: "một lần chạy của người soạn, hạt giống `random.Random(1)`" | chấp nhận |
| nhẹ | EX-student | hành lang ngắn | chỉ có mô tả bằng lời | đã sửa: `img/lec-09/short-corridor.svg` mới (`role="img"`, `title`, `desc`; ô đảo phân biệt bằng viền nét đứt và nhãn chữ), chèn ở "Hướng dẫn và ký hiệu" kèm đoạn đọc hình và trong đề 09.12, 09.14, 09.19, 09.20 | chấp nhận |
| nhẹ | EX-student | khối mã 09.18, 09.19 | chú thích tiếng Việt trong phông đơn cách hiển thị lỗi dấu; dòng dài | đã sửa: bỏ chú thích trong mã, giải thích biến bằng đoạn văn trước khối mã; tách dòng `assert` dài; ở 1400 px không còn khối nào cuộn ngang | chấp nhận |
| nhẹ | EX-student | công thức dài | cuộn ngang trong khung | đã sửa: tách `aligned` ở 09.13 (a), 09.14 (b), (c), 09.15 (a), (c), 09.16 (a), 09.17 (a)–(c), 09.20 (b); ở 1400 px 0 khối tràn; ở 390 px (khung nội dung 271 px) còn 11 công thức rộng 274–355 px cuộn trong khung, không cuộn trang | chấp nhận |
| nhẹ | EX-student | 09.16 | $\sigma$ trùng độ lệch chuẩn | đã sửa: $\operatorname{sig}$, ghi lý do một lần | chấp nhận |
| nhẹ | EX-student | 09.12 (b) | $J=-\infty$ bỏ qua giả thiết lượt kết thúc | đã sửa: nêu giả thiết của Định nghĩa 09.14 không thỏa, $J=-\infty$ theo nghĩa giới hạn | chấp nhận |
| nhẹ | EX-student | 09.11 (a), 09.14, 09.18 (b) | dẫn hình của sách | đã sửa: nêu số tại chỗ ($5\%$; $0{,}59$, $-11{,}6$, $-44$, $-82$); 09.18 (b) mô tả dạng đường cong của Hình 6.5 (đối chiếu ảnh trang PDF 157) | chấp nhận |
| nhẹ | EX-student | 09.11 (c) | câu đề khó hiểu | đã sửa theo đề xuất | chấp nhận |
| nhẹ | EX-student | 09.16 (a) | "như" thay cho "vì" | đã sửa | chấp nhận |
| nhẹ | EX-student | bảng `Mạch \| Mở phần \| Bài tập` | thiếu liên kết trang bài tập trên trang chiếu | đã sửa: `X01` `#/3/7`, `X02` `#/5/12`, `X03` `#/6/13` và `#/6/14`, `L09-K3` `#/7/6` và `#/7/7` (kiểm bằng Playwright) | chấp nhận |
| nhẹ | EX-student | đoạn mở đầu | đoạn dài; câu về người soạn | đã sửa: tách hai đoạn; "mọi số trong lời giải đã được tính lại" | chấp nhận |
| nhẹ | EX-student | `L09-K7` | "actor–critic" | đã sửa: "phương pháp actor–critic" (tên thuật toán, giữ tiếng Anh); 63 âm tiết, đáy 674 px | chấp nhận |
| nhẹ | EX-student | ghi chú `L09-K6` | "Định lý 09.22" | không sửa: deck đã ghi "Định lý 09.23" (điều phối viên kiểm bằng grep) | bác bỏ |
| nhẹ | EX-student | `index.html` | liên kết "Mở bài tập" bật khi tệp còn đang duyệt | giữ liên kết: tệp qua duyệt của điều phối viên trước khi commit | giữ (quyết định của điều phối viên) |

Kiểm sau sửa: trình xem `exercises.md` ở 1400 và 390 px: 30 khối nhận diện, 0 lỗi KaTeX, không khối thô, không yêu cầu ngoài, không cuộn trang ngang, hình `short-corridor.svg` tải ở năm chỗ; ảnh đã xem. Liên kết `#/1/1`…`#/7/1` và sáu liên kết trang bài tập mở đúng trang. `check.py` `L09-K7` (hai cỡ): 0 lỗi. Chạy lại `reinforce_se.py` (sai số chuẩn 09.19) và kiểm `update_left`. `git diff --check` sạch.

Rà lại EX-recheck (3 nhẹ, điều phối viên chấp nhận): 09.16(a) sửa "độ lệch chuẩn $\operatorname{sig}$" (thay hàng loạt nhầm) thành $\sigma$, quét toàn tệp không còn chỗ nhầm khác; `assert` của `grad_estimate` ở 09.19 so từng phần tử bằng `math.isclose`, không phụ thuộc kiểu trả về; 09.19(c) nêu cận trên $\sqrt2\,\alpha T^2$ (khoảng $345$ với $T=1000$, $\alpha=2^{-12}$). Trình xem 0 lỗi KaTeX; `git diff --check` sạch. Chấp nhận.

## Thực hành: notebook A (2026-10-28 → 2026-10-29)

Tệp: `materials/lec-09/thuc-hanh-double-dqn-reinforce-cartpole-lunarlander-flappybird.ipynb`. Yêu cầu người dùng: notebook thực hành tiếp nối Bài 09 cho DQN, Double DQN và REINFORCE trên CartPole, Lunar Lander, Flappy Bird; Breakout tách thành notebook riêng (notebook B, chưa có). Người dùng yêu cầu dùng siêu tham số đã công bố để tránh quét nhiều cấu hình; yêu cầu thường trực về notebook (standalone, `%pip` ở ô đầu, Markdown có ký hiệu trước mỗi ô chính, trình phát `<canvas>`, dải ảnh, bước tính tay có `assert`, công bố mọi thử nghiệm sơ bộ) áp dụng. Nguồn dựng và dữ liệu ngoài repo: `/data/tqlong/rl-plan-work/lec-09/` (`PLAN.md`, `RESEARCH-hparams.md`, `code/`, `runs/`, `logs/`).

| vai trò | loại tác tử | mô hình | effort | ghi tệp? | kết quả | quyết định của điều phối viên |
|---|---|---|---|---|---|---|
| thử nghiệm và soạn notebook | `general-purpose` | opus (claude-opus-5-5) | high | thử nghiệm: chỉ `rl-plan-work/lec-09/`; soạn: tệp notebook | `PLAN.md`: `train_dqn` (bản sao Bài 08 + cờ `double`) tái tạo đúng từng chữ số kết quả Bài 08; DQN và Double DQN tám hạt giống mỗi môi trường; REINFORCE trên ba môi trường; notebook 70 ô | chấp nhận sau các vòng sửa dưới |
| nghiên cứu siêu tham số (chỉ đọc nguồn, ghi scratchpad) | `general-purpose` | opus | high | chỉ `RESEARCH-hparams.md` | nguồn ở commit cố định: van Hasselt, Guez, Silver (2016) dùng đúng siêu tham số của DQN cho Double DQN; RL Baselines3 Zoo, SB3, CleanRL không có Double DQN hay REINFORCE riêng; pytorch/examples và Hugging Face Unit 4 chuẩn hóa lợi tức và bỏ $\gamma^t$; Dopamine cho Breakout | chấp nhận |
| rà soát RL–toán (chỉ đọc) | `general-purpose` | opus | high | không | NB-A-math: 0 chặn, 0 nghiêm trọng, 3 trung bình (số lần chạy một luồng sai so với dữ liệu nhúng; kết luận về độ chệch mạnh hơn dữ liệu; phép đo phương sai ở chính sách đã học không đỡ con số "$\approx2000$"), 3 nhẹ | chấp nhận |
| rà soát sư phạm + `no-ai-slop` Detect (chỉ đọc) | `general-purpose` | opus | high | không | NB-A-pedagogy: 3 nghiêm trọng (so sai tập hạt giống ở mục 9; khái quát hóa sai bảng cấu hình REINFORCE, bỏ qua dòng ReLU; thiếu trình phát cho REINFORCE trên CartPole), 10 trung bình, 16 nhẹ | chấp nhận |
| rà soát sinh viên + kiểm thử standalone (chỉ đọc) | `general-purpose` | opus | high | không | NB-A-student: venv rỗng mới, 0 lỗi, 640 s; 3 trung bình (thiếu trình phát chính sách học được; số "khi soạn" phụ thuộc phiên bản; hình ô 58 phân biệt chỉ bằng màu), 7 nhẹ | chấp nhận |
| sửa (gộp ba rà soát) | tác tử soạn | opus | high | tệp notebook | 7 trình phát; bảng REINFORCE đọc cả dòng ReLU; câu chữ về độ chệch hạ theo mức thống kê (2/6 hiệu vượt $2{,}365$, 0 vượt Bonferroni $3{,}64$); nối Bài 08 mục 15.4 và Tình huống 09.1 | chuyển rà lại |
| rà lại phần đã sửa (chỉ đọc) | `general-purpose` | opus | high | không | NB-A-recheck: các phát hiện đã chấp nhận đều xử lý; còn 1 trung bình (bất đẳng thức $y^{\mathrm{DDQN}}_i\le y^{\mathrm{DQN}}_i$ dùng cho hai lần huấn luyện khác nhau, ô 39), 6 nhẹ (điều kiện bất đẳng thức ô 22; phép kiểm ô 68; nhãn $\gamma^t$ ô 58; câu ô 51; hai tỉ số ô 63 không có trong dữ liệu nhúng; hai tài liệu chưa dẫn) | chấp nhận; tác tử soạn sửa cả 7 mục |
| tích hợp `index.html`, ghi chú Tình huống 09.1, nhật ký | `general-purpose` (tác tử biên tập) | opus | high | `index.html`, `lecture-note.md`, `review-log.md` | xem dưới | chờ duyệt |

**Quyết định cấu hình.**

- DQN và Double DQN giữ nguyên cấu hình DQN của notebook Bài 08 cho cả ba môi trường; Double DQN chỉ đổi mục tiêu (Thuật toán 09.5), theo van Hasselt, Guez và Silver (2016), vốn dùng đúng siêu tham số của DQN. Tám hạt giống mỗi ô, cùng quy ước hạt giống `TEST_SEED`, `SEL_SEED`, `VALID_SEED` với Bài 08.
- REINFORCE theo Thuật toán 09.25 (giữ $\gamma^t$, không chuẩn hóa lợi tức): mạng hai tầng ẩn $64$ nút tanh, Adam với $\alpha=10^{-3}$, gộp $K=4$ lượt mỗi cập nhật, $2000$ lượt, $\gamma=0{,}99$. Không nguồn nào được kiểm có REINFORCE đúng dạng Thuật toán 09.25; cấu hình được chốt trên các lần chạy công bố trong bảng của notebook, với ràng buộc thời gian khoảng $2$–$3$ phút. Notebook đối chiếu cài đặt REINFORCE của `pytorch/examples` (chuẩn hóa lợi tức, bỏ $\gamma^t$) trên CartPole.
- Breakout cần CNN và hàng giờ CPU mỗi hạt giống (`PLAN.md` mục 2), nên tách thành notebook B; thẻ Bài 9 ghi "Breakout: Chưa có".

**Kiểm cuối của điều phối viên (theo báo cáo giao việc):** JSON hợp lệ, 70 ô, 31/31 ô mã đã chạy trong venv sạch `venv_nbA5`, 0 lỗi, 591 s; notebook không đọc tệp nào trong repo; chỉ tải PyTorch bản CPU.

**Tích hợp (tác tử biên tập, 2026-10-29).**

- `index.html`, thẻ Bài 9, nhóm Thực hành: nút "CartPole, Lunar Lander, Flappy Bird: Mở trên Colab" tới `https://colab.research.google.com/github/uet-iai-course/reinforcement-learning-planning/blob/main/2627-1/materials/lec-09/thuc-hanh-double-dqn-reinforce-cartpole-lunarlander-flappybird.ipynb`, liên kết tải `.ipynb`, trạng thái "Breakout: Chưa có" (không liên kết). Dùng lớp sẵn có `resource-links`, `resource-alt`, `resource-status`; không sửa CSS.
- Ghi chú bài giảng, Tình huống 09.1: thêm đoạn "Đo độ chệch" lấy số từ ô 32–39 của notebook (kiểm lại với đầu ra): $Q_0-G_0$ và đỉnh của trung bình $q_i$ của Double DQN thấp hơn ở cả ba môi trường; 2/6 hiệu vượt $2{,}365$, 0 hiệu vượt $3{,}64$; độ lệch theo bước trên Lunar Lander ngược chiều ($+5{,}5$, $t\approx0{,}7$); $Q_0$ của Double DQN trên CartPole $109{,}5>100$; điểm không phân biệt được; Lunar Lander năm hạt giống $200{,}0$ → tám hạt giống $124{,}6$ (DQN $184{,}3$, $t\approx-1{,}7$). Bỏ câu "chưa được thực hiện" ở đoạn "Giới hạn".
- Deck: không có chỗ ghi "Thực hành: chưa có"; không sửa.
- Kiểm: `index.html` mở ở 1400 và 390 px, 0 lỗi trang, không cuộn ngang, ảnh thẻ đã xem; liên kết tải trả 200 (2 293 000 byte) trên `http://127.0.0.1:8799`; trình xem ghi chú 0 lỗi KaTeX; `git diff --check` sạch.

## Thực hành: notebook B — Breakout (2026-10-28 → 2026-10-29)

Tệp: `materials/lec-09/thuc-hanh-double-dqn-reinforce-breakout.ipynb`. Notebook thứ hai của Bài 09, tách khỏi notebook A vì Breakout cần mạng tích chập và hàng giờ CPU mỗi lần huấn luyện một triệu bước (`PLAN.md` mục 2). Notebook chạy trực tiếp các bước dựng, kiểm và một lần huấn luyện ngắn ($40\,000$ bước); kết quả một triệu bước được nhúng dưới dạng bảng và nhật ký. Người dùng yêu cầu dùng siêu tham số đã công bố để tránh quét nhiều cấu hình. Nguồn dựng và dữ liệu ngoài repo: `/data/tqlong/rl-plan-work/lec-09/`.

| vai trò | loại tác tử | mô hình | effort | ghi tệp? | kết quả | quyết định của điều phối viên |
|---|---|---|---|---|---|---|
| thử nghiệm và soạn notebook | `general-purpose` | opus (claude-opus-5-5) | high | thử nghiệm: chỉ `rl-plan-work/lec-09/`; soạn: tệp notebook | tiền xử lý Atari, bộ nhớ phát lại lưu mỗi khung một lần (dựng lại chồng bốn khung khớp $996/996$ vị trí), Nature CNN $1\,686\,180$ tham số; sáu lần chạy DQN và Double DQN $10^6$ bước; ba lần chạy REINFORCE | chấp nhận sau các vòng sửa dưới |
| nghiên cứu siêu tham số (chỉ đọc nguồn) | `general-purpose` | opus | high | chỉ `RESEARCH-hparams.md` | mục 4 Breakout: CleanRL `dqn_atari.py`, RL Baselines3 Zoo `dqn.yml` (atari), Dopamine JAX `dqn.gin` và `breakout.json`, phụ lục Mnih 2015 / van Hasselt 2016, ở commit cố định | chấp nhận |
| rà soát RL–toán (chỉ đọc) | `general-purpose` | opus | high | không | NB-B-math: 0 chặn, 0 nghiêm trọng, 5 trung bình (giao thức Dopamine trung bình cả vòng; $Q_0-G_0$ đo với $\epsilon_{\mathrm{ev}}=0{,}05$ thay vì chính sách tham lam; câu tái lập không khớp nhật ký ba lần chạy; câu tổng kết trái đầu ra $1{,}60$; hàm mục tiêu của REINFORCE theo từng mạng không chính xác vì trạng thái đầu của mạng sau phụ thuộc $\theta$), 7 nhẹ | chấp nhận |
| rà soát sư phạm + `no-ai-slop` Detect (chỉ đọc) | `general-purpose` | opus | high | không | NB-B-pedagogy: 2 nghiêm trọng (câu tổng kết trái đầu ra; hai chính sách REINFORCE tham lam cho cùng chuỗi điểm trên 30 ván, nghi suy biến, chưa so với chính sách hằng), 7 trung bình (gồm "hai bước học" sai, thiếu trình phát REINFORCE, đơn vị ngân sách của Mnih 2015, thuật ngữ Atari, nối Bài 10 vượt ghi chú), 11 nhẹ | chấp nhận |
| rà soát sinh viên + kiểm thử standalone (chỉ đọc) | `general-purpose` | opus | high | không | NB-B-student: venv rỗng mới, 0 lỗi, 11 phút 15 giây; 4 trung bình (thiếu trình phát và dải ảnh REINFORCE; văn bản và mã ô 32–33 không khớp; câu tổng kết; mã không chọn GPU), 7 nhẹ | chấp nhận |
| sửa (gộp ba rà soát) | tác tử soạn | opus | high | tệp notebook | $Q_0-G_0$ đo cả với chính sách tham lam ($\epsilon=0$, đánh giá lại trọng số đã lưu, không huấn luyện thêm); so REINFORCE với bốn chính sách hằng, phát hiện suy biến luôn `RIGHT`; trình phát REINFORCE; biến `DEVICE`; ngân sách Mnih 2015 viết theo khung và bước tác tử | chuyển rà lại |
| rà lại phần đã sửa (chỉ đọc) | `general-purpose` | opus | high | không | NB-B-recheck: 0 chặn, 0 nghiêm trọng, 0 trung bình, 4 nhẹ (ván đầu của `TEST_SEED` không phân biệt các chính sách yếu; thiếu dải ảnh REINFORCE 1M; điểm Dopamine vẽ ở cuối vòng; câu cơ chế `lr1e-4` với Adam) | chấp nhận; tác tử soạn sửa cả 4 mục |
| tích hợp `index.html`, ghi chú bài giảng, nhật ký | `general-purpose` (tác tử biên tập) | opus | high | `index.html`, `lecture-note.md`, `review-log.md` | xem dưới | chờ duyệt |

**Quyết định cấu hình và dữ liệu.**

- DQN và Double DQN, cấu hình `CFG_1M` ghép từ các nguồn đã công bố (CleanRL `dqn_atari.py`, RL Baselines3 Zoo, Dopamine; tiền xử lý theo Mnih và cộng sự 2015): $T=10^6$ bước tác tử, $N=10^5$, $N_{\mathrm{start}}=2\cdot10^4$, $b=32$, $F=4$, $C=250$, Adam $\eta=10^{-4}$, $\epsilon_{\mathrm{exp}}$ giảm tuyến tính tới $0{,}01$ trong $25\%$ đầu; Double DQN chỉ đổi mục tiêu. Ba hạt giống mỗi thuật toán; mỗi lần chạy khoảng $7$–$9$ giờ CPU.
- Notebook không nạp trọng số mạng; dữ liệu nhúng gồm bảng, nhật ký và các ván ghi sẵn cho trình phát. Phép đo với chính sách tham lam dùng trọng số đã lưu khi soạn, ngoài notebook.
- Double DQN hạt giống $2$ không học được (điểm $1{,}73\pm0{,}57$, ngang chọn đều); lần chạy được giữ nguyên trong bảng, không chạy lại, và notebook ghi rằng hiệu ở hạt giống đó không đo cùng một tình huống.
- REINFORCE (Thuật toán 09.25, $K=1$, $\gamma^t$, Nature CNN): ba lần chạy với hạt giống $1$: `lr1e-4` sụp về chính sách gần tất định, điểm $0$, dừng thủ công ở khoảng $2\cdot10^5$ bước và công bố như kết quả bị loại; `lr1e-5` một triệu bước; `lr1e-5_norm` thêm chuẩn hóa lợi tức trong từng lượt, theo câu hỏi của người dùng. Cả hai lần một triệu bước suy biến: chính sách tham lam luôn chọn `RIGHT`, $2{,}43\pm0{,}49$ điểm, trùng chính sách hằng luôn `RIGHT` ở cả 30 ván.

**Kiểm cuối của điều phối viên (theo báo cáo giao việc):** JSON hợp lệ, 46 ô, 20/20 ô mã đã chạy trong venv sạch `venv_nbB5`, 0 lỗi, 11 phút 50 giây; notebook không đọc tệp nào trong repo; chỉ tải PyTorch bản CPU.

**Tích hợp (tác tử biên tập, 2026-10-29).**

- `index.html`, thẻ Bài 9, nhóm Thực hành: thay "Breakout: Chưa có" bằng nút "Breakout: Mở trên Colab" tới `https://colab.research.google.com/github/uet-iai-course/reinforcement-learning-planning/blob/main/2627-1/materials/lec-09/thuc-hanh-double-dqn-reinforce-breakout.ipynb` và liên kết "Tải notebook Breakout (.ipynb)"; nút notebook A giữ tên "CartPole, Lunar Lander, Flappy Bird: Mở trên Colab"; lớp CSS sẵn có.
- Ghi chú bài giảng, Tình huống 09.1: đoạn "Breakout" với số từ ô 31–32 của notebook (kiểm lại với đầu ra): $Q_0-G_0$ tham lam DQN $0{,}91$; $1{,}76$; $1{,}42$, Double DQN $0{,}47$; $0{,}10$; $0{,}30$; $t=-3{,}04$, $\mathrm{df}=2$, dưới ngưỡng $4{,}30$; Double DQN hạt giống $2$ không học được. Mục 7, đoạn nối Bài 10: một câu về REINFORCE trên Breakout (ô 37–39: suy biến luôn sang phải, $2{,}43$ điểm, bằng chính sách hằng; DQN và Double DQN $42$–$66$ điểm ở bốn trong sáu lần chạy). Tình huống 09.2 nói về dữ liệu của bộ nhớ phát lại, không hợp với kết quả này; không sửa.
- Kiểm: xem dòng kiểm ngay dưới.
- Kiểm tích hợp: `index.html` mở ở 1400 và 390 px, 0 lỗi trang, không cuộn ngang, ảnh thẻ đã xem; hai liên kết tải trả 200 (862 025 và 2 293 000 byte) trên `http://127.0.0.1:8799`; trình xem ghi chú 0 lỗi KaTeX, không khối thô; `git diff --check` sạch.
