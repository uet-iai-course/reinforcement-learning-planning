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
