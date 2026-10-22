# Nhật ký rà soát Bài 08

## Kiểm kê

Nguồn có 36 trang, không có tài liệu bài tập hoặc code demo đi kèm. Bản đích có 34 trang chính, ba trang bài tập dọc và tám SVG vẽ lại. Tuyến cốt lõi dài 110 phút; phần optimizer chi tiết là 10 phút linh hoạt. Không dùng ảnh raster hay tài nguyên mạng.

## Phản biện nguồn và quyết định ban đầu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa / quyết định |
|---|---|---|---|---|
| chặn bàn giao | `L08-06` | Cận mẫu dạng bảng được gắn với GLIE chung nhưng thiếu mô hình lấy mẫu, chuẩn sai số và xác suất thành công. | Nguồn tr. 8–9. | Bỏ công thức khỏi phần chính; chỉ giữ nhận xét quy mô. |
| chặn bàn giao | `L08-06` | Cận theo $d$ không suy ra từ giả thiết riêng $Q^*$ biểu diễn tuyến tính. | Nguồn tr. 10–11. | Bỏ công thức; ghi cần cấu trúc MDP tuyến tính, bao phủ và thuật toán cụ thể. |
| nghiêm trọng | `L08-04`, `L08-12`, `L08-17` | Chỉ số chuyển tiếp và phần thưởng không nhất quán. | Nguồn tr. 4–5, 19–21. | Dùng duy nhất $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$. |
| nghiêm trọng | `L08-10`, `L08-17`, `L08-19` | Nguồn không nói rõ dừng gradient qua đích bootstrap. | Nguồn tr. 16, 20–22, 34. | Dùng $\operatorname{sg}(y)$ và detach/no-grad trong giả mã. |
| nghiêm trọng | `L08-09`, `L08-12`, `L08-17` | Nguồn không phân biệt kết thúc MDP với cắt ngắn. | Nguồn tr. 21, 34. | Dùng hai cờ; chỉ $Z$ che bootstrap theo quy ước nhiệm vụ tiếp diễn. |
| nghiêm trọng | `L08-07`, `L08-20` | Giao diện mạng lúc nhận $(s,a)$, lúc xuất vector hành động. | Nguồn tr. 14–17, 35. | Chốt đầu vào quan sát, đầu ra $\mathbb R^{|\mathcal A|}$ và phép gather. |
| nghiêm trọng | `L08-27`–`L08-30` | Replay và target network dễ bị hiểu là giải quyết hội tụ. | Nguồn tr. 12–13, 29–34. | Nói rõ hai kỹ thuật giảm bất ổn thực nghiệm, không loại bỏ deadly triad. |
| trung bình | `L08-13`–`L08-14`, `L08-28` | “Phá vỡ tương quan” và ngụ ý i.i.d. quá mạnh. | Nguồn tr. 19, 30, 32. | Đổi thành giảm tương quan ngắn hạn; nêu phân phối buffer vẫn thay đổi. |
| trung bình | `L08-16` | “Cập nhật thường xuyên” mâu thuẫn với mục tiêu giữ mạng cố định. | Nguồn tr. 19, 33. | Giữ $\theta^-$ cố định trong $C$ bước rồi sao chép. |
| trung bình | `L08-22`–`L08-26` | Phần optimizer quá dài và có khẳng định thắng chung. | Nguồn tr. 23–28. | Gộp còn năm trang ngắn; so sánh có điều kiện. |
| trung bình | `L08-24`–`L08-25` | RMSprop/Adam thiếu quy ước tọa độ; mẫu số Adam sai chuẩn đã chọn. | Nguồn tr. 25–26. | Nêu khởi tạo, phép toán tọa độ và dùng $\sqrt{\hat v}+\epsilon_{\mathrm{opt}}$. |
| trung bình | `L08-31`–`L08-32` | Bốn khung được gọi là trạng thái như thể chắc chắn Markov. | Nguồn tr. 35. | Gọi là lịch sử quan sát ngắn; không bảo đảm Markov. |

## Sai khác có chủ ý so với nguồn

1. Bỏ hai công thức độ phức tạp mẫu ở tr. 9 và 11 khỏi phần chính vì thiếu thiết lập định lý và có nguy cơ bị hiểu như kết quả chung.
2. Chuẩn hóa giao diện DQN thành mạng nhận quan sát và xuất vector cho hành động rời rạc hữu hạn.
3. Bổ sung mặt nạ kết thúc, cờ cắt ngắn và dừng gradient.
4. Tách replay khỏi mạng mục tiêu; dùng “giảm tương quan” và “làm chậm đích”, không dùng “loại bỏ” hay “bảo đảm”.
5. Gộp phần optimizer, sửa công thức và hạ mức các nhận xét thực nghiệm.
6. Gọi bốn khung Atari là lịch sử quan sát ngắn, không phải trạng thái Markov được bảo đảm.
7. Thêm ba bài tập dọc từ chính công thức và giả mã nguồn; không tạo code demo.

## Kiểm tra số

Với $|B|=2$, $\gamma=0{,}9$:

$$
y=(4{,}6,-2),\qquad \delta=(1{,}5,-0{,}5).
$$

$$
L=\frac{1{,}5^2+(-0{,}5)^2}{2}=1{,}25,
\qquad \frac{\partial L}{\partial(q_1,q_2)}=(-1{,}5,0{,}5).
$$

Mẫu kết thúc có giá trị bootstrap 100 nhưng giá trị này bị mặt nạ loại bỏ.

## Trạng thái

Bản nháp đã qua kiểm định storyboard, bốn vòng rà soát độc lập và vòng chỉnh sửa hợp nhất. Bản này còn cần rà lại toán học phần đã đổi và kiểm định cuối trước khi bàn giao.

## Kiểm định storyboard và quyết định chỉnh sửa

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa / quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L08-07`–`L08-08` | $\theta^-$ xuất hiện trong đích trước khi hai mạng và phép khởi tạo được thiết lập. | Bản nháp chỉ gọi $Q_{\theta^-}$ là mạng mục tiêu tại `L08-08`; vai trò đầy đủ đến `L08-15` mới xuất hiện. | Đã đưa giao diện hai mạng và $\theta^-\leftarrow\theta$ vào `L08-07`; `L08-08` chỉ dùng ký hiệu sau bước này. `L08-15` trở thành cầu nối hai đường tính trước loss hoàn chỉnh. |
| nghiêm trọng | `L08-10`, `L08-17`, `L08-19`, `L08-20`, `L08-29` | Chỉ số thời gian và chỉ số batch bị trộn, nên $R_{i+1}$ và $O_{i+1}$ có thể bị hiểu là mẫu kế tiếp trong batch. | Schema thời gian dùng $t+1$, nhưng batch không có thứ tự thời gian theo chỉ số $i$. | Đã chốt batch $\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$ và cập nhật loss, giả mã, tensor, ví dụ mục tiêu di động, outline và ghi chú tác giả. |
| nghiêm trọng | `L08-27`–`L08-29` | Mạch cũ có thể khiến người học hiểu đồng bộ mạng mục tiêu tạo ra mục tiêu di động. | Nguyên nhân là bootstrap từ hàm giá trị đang được học; mạng mục tiêu chỉ giữ tham số tạo đích cố định theo đoạn. | Đã sửa quan hệ nhân quả ở tiêu đề, nội dung và notes; công thức `L08-29` chỉ minh họa độ nhảy tại mốc đồng bộ. |
| trung bình | `storyboard.md` | Chu trình trọng tâm chưa nêu đủ sáu bước, dữ kiện truyền, sản phẩm học tập và lý do gộp/không áp dụng. | Bảng cũ chỉ gắn một vài nhãn chu trình cho cả cụm. | Đã thêm năm bảng chu trình sáu bước; mỗi hàng có mã, đầu vào, sản phẩm và quyết định gộp. Optimizer có chu trình rút gọn với lý do rõ. |
| trung bình | `L08-20`–`L08-21` | Hợp đồng tensor còn chung chung và chưa áp dụng vào Atari trước bước kiểm tra. | Bản nháp dùng $[b,c,h,w]$, trong khi ứng dụng nguồn dùng lịch sử bốn khung. | Đã đổi `L08-20` thành batch Atari $[b,4,h,w]$, sửa SVG và giữ `L08-21` làm kiểm tra dấu gradient ngay sau đó. |
| trung bình | `L08-22`–`L08-26` | Phần optimizer chiếm 17 phút dù chỉ là công cụ phụ. | Mục tiêu bài là DQN, replay, mạng mục tiêu và bất ổn. | Đã phân tuyến 7 phút cốt lõi cộng 10 phút linh hoạt; `L08-23`–`L08-25` là phần có thể rút. Tổng phần cốt lõi còn 110 phút. |
| trung bình | `L08-25` | Công thức Adam chứa chuỗi `,quad` thay vì lệnh khoảng trắng KaTeX. | Biểu thức đầu của Adam trong bản nháp. | Đã sửa thành `,\quad`. |
| trung bình | `X03` | Câu hỏi yêu cầu “số seed” cụ thể dù nguồn và ngân sách thí nghiệm không xác định. | Bài chỉ yêu cầu thiết kế ablation, không chạy code. | Đã đổi thành cách tổng hợp qua các lần chạy độc lập và báo độ phân tán; không ép một con số. |

Sau các thay đổi, đã rà lại từng trang bị sửa và hai trang lân cận theo mạch: `L08-03`–`L08-10`, `L08-13`–`L08-21`, `L08-22`–`L08-31`, `X01`–`X03`. Số trang và thứ tự vật lý không đổi: 34 trang chính và ba trang dọc.

## Kiểm tra kỹ thuật của bản nháp đầu

- 34 mã trang chính và ba mã bài tập duy nhất; 37 khối ghi chú và 37 mục storyboard; độ sâu `<section>` lớn nhất là 2.
- KaTeX chế độ nghiêm ngặt đọc 132 biểu thức, không có lỗi phân tích.
- Tám SVG hợp lệ khi đọc bằng trình phân tích XML, có `role="img"`, `title`, `desc`; nhãn nhỏ nhất là 30 px.
- HTML và tám SVG trả HTTP 200 tại cổng 8765; mọi tài nguyên cốt lõi là cục bộ.
- Không có ảnh raster, URL mạng trong HTML, mã trang, nhãn phân tuyến hoặc thời lượng lộ trên mặt trang và ghi chú.
- Cỡ chữ hiệu dụng của bảng, giả mã và khối code ít nhất khoảng 0,76 em theo CSS; cần xác nhận tràn trang bằng vòng rà trực quan sau chỉnh sửa.
- `xmllint` không có trong môi trường; kiểm tra cú pháp SVG dùng `xml.etree.ElementTree` thay thế.

## Kiểm tra kỹ thuật sau chỉnh sửa storyboard

- Giữ nguyên 34 mã trang chính và ba mã bài tập; cả 37 mã đều duy nhất, có 37 khối ghi chú, độ sâu `<section>` lớn nhất là 2.
- KaTeX chế độ nghiêm ngặt đọc 136 biểu thức sau chỉnh sửa, không có lỗi phân tích; công thức Adam dùng `\quad` hợp lệ.
- Tám SVG đọc được bằng `xml.etree.ElementTree`, có `role="img"`, `title`, `desc`; `tensor-contract.svg` đã đổi sang batch Atari $[b,4,h,w]$.
- HTML và tám SVG trả HTTP 200 tại cổng 8765; không có tài sản raster hoặc URL mạng trong HTML.
- Quét phần hiển thị và notes sau khi bỏ thuộc tính `data-slide-id`: không có mã trang, thời lượng hay nhãn phân tuyến bị lộ.
- Các tệp Markdown chỉ dùng dấu đô-la cho công thức nội dòng và công thức khối.

## Hợp nhất bốn báo cáo độc lập

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa / quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L08-12`, `L08-18`, `X02` | Môi trường tự reset có thể làm replay lưu quan sát đầu của episode mới thay cho quan sát cuối của chuyển tiếp. | Schema cũ chỉ nói reset, không xử lý `final_observation`. | Đã yêu cầu lấy final observation trước reset; `X02` nêu rõ giả thiết và kiểm riêng lỗi này. |
| nghiêm trọng | `L08-12`, `L08-17`, `X02` | Mặt nạ không thể suy ra máy móc từ tên cờ API; nó phải theo kết thúc của MDP đang mô hình hóa. | `terminated` và `truncated` phụ thuộc semantics của wrapper và nhiệm vụ. | Đã định nghĩa $Z$ là kết thúc của MDP mô hình hóa, $U$ là cắt ngắn ngoài mô hình; chỉ $Z$ che bootstrap trong quy ước đã chọn. |
| nghiêm trọng | `L08-18`–`L08-19` | Giả mã thiếu warmup replay, tần suất tối ưu và hai đồng hồ môi trường/tối ưu. | Điều kiện cũ chỉ là $|\mathcal D|\ge b$. | Đã thêm $N_{\mathrm{start}}$, $F$, $t$, $k_{\mathrm{opt}}$; bản đơn giản có thể chọn $F=1$ nhưng vẫn phải warmup. |
| nghiêm trọng | `L08-16`, `L08-19` | Thời điểm đồng bộ cứng chưa xác định rõ trước hay sau bước cập nhật. | Câu “sau mỗi $C$ bước” còn mơ hồ. | Đã chốt thứ tự: cập nhật $\theta$, tăng $k_{\mathrm{opt}}$, rồi kiểm tra $k_{\mathrm{opt}}\bmod C=0$. |
| nghiêm trọng | `L08-10`, `dqn-computation-graph.svg` | Đồ thị cũ ghi mạng online “chọn a”, dễ lẫn với hành động lưu trong batch. | Loss phải dùng $A_i$ của chuyển tiếp replay. | Đã vẽ batch $A_i$ đi vào nút gather; gradient chỉ qua $q_i=Q_\theta(O_i,A_i)$. |
| nghiêm trọng | `L08-20`, `tensor-contract.svg` | Hợp đồng tensor thiếu $O'$, mạng mục tiêu, max, $U$, kiểu dữ liệu và thiết bị. | Bản cũ chỉ có nhánh online và gather. | Đã vẽ hai nhánh online/target, gather/max, $R,Z,U$; mặt trang ghi shape, dtype, device và quy tắc một hành động mỗi hàng. |
| nghiêm trọng | `L08-07`, `L08-27`–`L08-30` | Nguyên nhân mục tiêu di động xuất hiện sau giải pháp, còn cầu nối tới deadly triad chưa rõ. | Mạch cũ giải thích target network trước phản ví dụ một mạng. | Đã đưa phản ví dụ vào `L08-07`; `L08-27` ánh xạ hai biểu hiện bất ổn sang xấp xỉ hàm, bootstrap và dữ liệu khác chính sách. |
| trung bình | `L08-04`–`L08-05`, `L08-13` | Giải thích khác chính sách chưa nêu vì sao Q-learning không cần importance sampling và chưa tách hai nguồn lệch hành vi. | Có cả khám phá hiện tại và dữ liệu từ hành vi cũ trong replay. | Đã gọi đúng phép tối ưu Bellman; giải thích phép cực đại không phải kỳ vọng hành động, và nêu hai nguồn mismatch. |
| trung bình | `L08-04`, `L08-13`, `L08-16`, `L08-18`, `L08-22`–`L08-25` | Miền, kiểu và ý nghĩa của nhiều siêu tham số chưa được khai báo trước khi dùng. | Thiếu miền của $\gamma,\eta,\rho,\beta$, epsilon và kiểu của $b,N,C,F,t,k_{\mathrm{opt}}$. | Đã khai báo tại lần dùng đầu và bổ sung bảng ký hiệu trong outline; tách $t$, $k_{\mathrm{opt}}$, $j$. |
| trung bình | `L08-10`, `L08-14`, `L08-20`, `X03` | MSE, i.i.d., detach, gather và ablation xuất hiện bằng tiếng Anh trước khi giải nghĩa. | Các thuật ngữ hiện trên mặt trang hoặc notes. | Đã viết đầy đủ tiếng Việt ở lần đầu, giữ dạng tiếng Anh trong ngoặc khi cần nối với code. |
| trung bình | `L08-10`, `L08-17` | MSE bị diễn đạt như yêu cầu của nguồn hoặc DQN. | DQN có thể dùng Huber trong thực hành. | Đã ghi MSE là lựa chọn của bài để thống nhất phép tính; Huber chỉ nằm trong notes như lựa chọn khác. |
| trung bình | `L08-22`–`L08-26` | Điều hướng optimizer chưa thể hiện nhánh ngang cốt lõi và nhánh dọc tùy chọn. | Cả năm trang nằm trong cùng một cột dọc. | Đã tách `L08-26` sang section ngang mới; `L08-23`–`L08-25` vẫn là nhánh dọc dưới `L08-22`. Số mã không đổi. |
| trung bình | `L08-31` | Pipeline Atari thiếu hành động/phần thưởng và dễ bị hiểu là đặc tả tái lập. | Nguồn chỉ cho mô tả kiến trúc mức cao. | Đã thêm $A_t$, $R_{t+1}$ và tuyên bố rõ đây chỉ là giao diện tối thiểu. |
| trung bình | `X02`, `X03` | Bài sửa code mới có hai lỗi; bài ablation chưa nói cách giữ số lần chạy công bằng. | Hai bài chưa đủ kiểm semantics và nhiễu thực nghiệm. | `X02` nay có bốn lỗi; `X03` yêu cầu định trước cùng số lần chạy hoặc kế hoạch seed cho mọi nhánh nhưng không ép một con số khi thiếu ngân sách. |
| trung bình | tám SVG | Nhãn 30 px còn nhỏ và một số sơ đồ dùng nhiều khoảng trống. | Kiểm kê SVG sau bản nháp. | Đã tăng nhãn lên tối thiểu 34 px, tiêu đề nhóm lên 36 px; hai đồ thị tính toán được bố trí lại gọn hơn. |
| nhẹ | `note-for-author.md` | Overestimation liên quan DQN nhưng không đủ thời lượng và nguồn để mở thành cụm mới. | Phạm vi hiện tại dừng ở DQN cơ bản và bất ổn. | Chỉ ghi lưu ý cho tác giả; không thêm lên slide. |

Sau thay đổi cấu trúc optimizer, đã rà `L08-20`–`L08-28` và các trang lân cận. Sau thay đổi mục tiêu di động, đã rà `L08-04`–`L08-10` và `L08-27`–`L08-31`. Số mã vẫn là 34 trang chính và ba bài tập.

## Kiểm tra kỹ thuật sau vòng hợp nhất

- 37 mã duy nhất, 37 khối notes và 37 hàng storyboard theo cùng thứ tự; độ sâu section lớn nhất là 2.
- Điều hướng optimizer tạo một cột dọc `L08-22`–`L08-25`, sau đó `L08-26` ở vị trí ngang kế tiếp. Tổng số trang không đổi.
- KaTeX nghiêm ngặt đọc 166 biểu thức sau rà toán học, không có lỗi phân tích.
- Tám SVG hợp lệ, có `role="img"`, `title`, `desc`; cỡ nhãn khai báo nhỏ nhất là 34 px.
- Pseudocode dùng cỡ hiệu dụng khoảng $0{,}82\times0{,}94=0{,}7708$ em; bảng khoảng $0{,}82\times0{,}93=0{,}7626$ em.
- HTML và tám SVG trả HTTP 200 tại cổng 8765; không có raster hoặc URL mạng trong HTML.
- Quét phần hiển thị và notes không thấy mã trang, thời lượng, nhãn tuyến hoặc chỉ dẫn điều phối. Markdown chỉ dùng dấu đô-la cho công thức.
- Chưa xác nhận tràn trang bằng trình duyệt đồ họa trong vòng sửa này; kiểm định trực quan cuối vẫn bắt buộc.

## Rà lại toán học sau chỉnh sửa

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa / quyết định |
|---|---|---|---|---|
| trung bình | `L08-04` | Quy tắc cập nhật dùng $\alpha_t$ nhưng chưa khai báo miền; ghi chú hội tụ chưa gắn Robbins–Monro theo từng cặp. | Công thức cập nhật Q-learning dạng bảng. | Đã thêm $\alpha_t>0$ trên mặt trang; notes giới hạn phát biểu hội tụ bằng điều kiện Robbins–Monro theo từng cặp trạng thái–hành động và giả thiết thăm. |
| trung bình | `L08-04`, `L08-18` | Miền $\gamma\in[0,1]$ thiếu điều kiện cho trường hợp $\gamma=1$. | Với nhiệm vụ tiếp diễn, return có thể không hữu hạn khi không chiết khấu. | Giữ $\gamma\in[0,1]$ nhưng nêu rõ $\gamma=1$ chỉ dùng khi episode kết thúc thích hợp và return hữu hạn; nhiệm vụ tiếp diễn dùng $\gamma<1$. |

Tác tử rà toán xác nhận PASS sau hai sửa cuối; không còn lỗi từ mức trung bình trở lên.

## Vòng rà soát độc lập hiện tại và lượt writer

- Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.
- Phạm vi thực thi: chỉ sửa ba tệp planning (`outline.md`, `storyboard.md`, `review-log.md`); không sửa HTML hay tệp khác.
- Năm báo cáo độc lập đều chạy bằng `openrouter-mcp-reviewer`, không có worker ghi tệp:
  1. Góc nhìn sinh viên: yêu cầu khởi tạo $O_0$, tách bước dừng khỏi điều kiện tối ưu, làm rõ final observation và hai đồng hồ.
  2. Chuyên gia Học tăng cường: xác nhận phạm vi DQN; yêu cầu nối giả mã với vòng huấn luyện, làm rõ autoreset và ký hiệu $j/k_{\mathrm{opt}}$.
  3. Độ chính xác toán học và thuật toán: kiểm lại đích $y$, MSE, gradient, mặt nạ, giả mã và optimizer; không phát hiện lỗi từ mức trung bình trở lên.
  4. Phản biện học thuật và giảng dạy: yêu cầu báo trước nguồn batch tại `L08-10`, thêm đáp án ví dụ `L08-09`, và nói rõ thời điểm kiểm $t\bmod F$.
  5. Kết nối và mạch viết: xác nhận bảy mạch sau khi gộp hai section đầu; yêu cầu bổ sung câu nối tại các ranh giới và ghi đúng vai trò vào–ra trong storyboard.
- Writer HTML và writer planning chạy tuần tự, có phạm vi tệp không trùng nhau. Cả hai dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.
- Quyết định chấp nhận/từ chối:
  - Chấp nhận: gộp hai section đầu thành M1; ghi X01–X03 là 30 phút chữa bài ngoài 120 phút chính.
  - Chấp nhận: thêm truy nguyên bốn trang bổ sung và lý do bỏ câu hỏi tr.36 vào outline.
  - Chấp nhận: bản đồ bảy mạch và ghi chú trang dùng chung trong storyboard.
  - Từ chối: tách `L08-18`/`L08-19`/`L08-20` (chưa có bằng chứng tràn từ render); đổi vị trí `X03`; thêm câu hỏi mới lên mặt trang.
- Hai dương tính giả cần ghi nhận:
  1. "120 phút chính + 30 phút chữa bài" là đúng yêu cầu, không phải vượt giờ; 30 phút chữa bài nằm ngoài 120 phút chính.
  2. `L08-20`/`L08-21` và `X01`/`X03` không phải trang mồ côi; chúng là bổ sung truy nguyên từ công thức/tensor/kiểm tra, nhưng outline cần ghi rõ truy nguyên này (đã ghi).
- Chưa tuyên bố render, HTTP hoặc Codex Slides ở lượt writer này; các kiểm tra đó thuộc vòng sau.

## Kiểm định cuối của điều phối viên

- 37 mã trang duy nhất, 37 khối ghi chú và 37 mục storyboard; đúng bảy `<section>` ngoài, độ sâu lớn nhất là 2. Các range vật lý khớp outline và storyboard.
- RevealMath/KaTeX dựng toàn bộ công thức ở cả hai lượt render, không có lỗi console hoặc lỗi trang.
- Tám SVG hợp lệ về XML, có `role="img"`, `title`, `desc`; nhãn nhỏ nhất là 34 px.
- Máy chủ tối thiểu chỉ chứa Bài 08 và thư viện cục bộ trả HTTP 200 cho HTML, CSS, RevealJS, KaTeX, phông cục bộ và tám SVG tại `127.0.0.1:8765`. Lệnh `python3 -m reloadserver 8765` không chạy được vì mô-đun `reloadserver` không có trong môi trường; dùng `python3 -m http.server 8765 --bind 127.0.0.1` thay thế.
- Chromium headless duyệt đủ 37 trang ở $1280\times720$ và $800\times600$, tạo 74 ảnh chụp; không có lỗi tài nguyên. Điều hướng bàn phím xuống, lên và sang phải đi đúng `L08-02`, `L08-01`, `L08-07`.
- Bộ dò hình học báo mười dương tính giả ở H1 và hộp KaTeX; đối chiếu montage và ảnh gốc xác nhận không có chữ, công thức hoặc hình bị cắt. Đã kiểm riêng `L08-18`–`L08-20`, `X02`, `L08-33`, `X03`.
- Không có ảnh raster, tài nguyên mạng cốt lõi, mã trang, nhãn phân tuyến hoặc thời lượng lộ trên mặt trang và ghi chú.
- Cỡ chữ hiệu dụng của giả mã là khoảng 0,77 em và của bảng là khoảng 0,76 em.
- Nhánh optimizer có độ sâu dọc một cấp và có thể bỏ qua bằng điều hướng ngang sau trang tổng quan.
- Tự kiểm theo `no-ai-slop/eval.md`: giữ nội dung nguồn, không thêm số liệu hoặc mệnh đề mới; không còn từ cấm, lời dẫn rỗng, câu hỏi tu từ, phô trương, kết giả hoặc nhịp câu máy móc trong nội dung hiển thị và notes.
- Rà mạch theo Quill khi không có `quill.json`: bảy mạch tiến từ bảng Q đến hợp đồng DQN; thuật ngữ, ký hiệu $O,A,R,Z,U,\theta,\theta^-$ và hai đồng hồ được truyền liên tục; không tạo `quill.json`.
- Ba lần yêu cầu tái kiểm định OpenRouter sau chỉnh sửa giả mã/mạch đều dừng ở `api_transport_error` trước khi model nhận prompt. Không ghi các lượt này là PASS; điều phối viên đã tự kiểm lại thứ tự bước 1–10, mặt nạ, autoreset, fallback `final_observation=None`, $t\bmod F$ và phạm vi bước dừng.

Codex Slides không thể đồng bộ bản hiện tại. Runtime đi kèm đang chạy Node.js 18.19.1 trong khi skill yêu cầu Node.js 20 trở lên; API Design Files lỗi `ReferenceError: File is not defined`. Vì vậy không tuyên bố năm Design Files khớp bản hiện tại và không tuyên bố đã duyệt bằng Codex Browser. Kiểm định trực quan RevealJS cục bộ ở hai khung đã hoàn tất như trên.

## Giai đoạn I — lecture note độc lập

- Writer bản đầu dùng `requested_model=observed_model=z-ai/glm-5.3-flash`,
  provider OpenRouter, profile `write/20/900/32000`. Worker ghi 43.217 byte ở
  vòng 3 và hoàn tất vòng 4 sau 303,643 giây. Lượt trước đó với sáu tệp đầu vào
  và timeout 600 giây đã dừng đúng ngưỡng; bản chạy lại chỉ nhận ba tệp đã cô lập.
- Năm reviewer chỉ đọc chạy song song bằng `review/8/600/12000`. Hai vai sinh
  viên và mạch viết dùng GLM; ba vai chuyên gia Học tăng cường, toán–thuật toán
  và phản biện sư phạm dùng DeepSeek. Tất cả trả đúng model yêu cầu, model quan
  sát và provider OpenRouter; không có lỗi chặn bàn giao hoặc nghiêm trọng.
- Đã xử lý các góp ý có căn cứ: sửa câu về phép sao lưu lệch chính sách; thống
  nhất bộ sáu thành phần và ký hiệu quan sát; đưa hợp đồng tensor về đúng mạch;
  tách thời lượng để bảy mạch cộng đúng 120 phút mà không tính đôi; nối đích hồi
  quy với mặt nạ kết thúc; làm rõ đạo hàm theo đầu ra và gradient theo tham số;
  mô tả điều kiện dùng `final_observation`; sửa mở–kết thành sáu điểm kiểm tra.
- Không áp dụng gợi ý thêm kết quả CartPole, giả thiết hội tụ mới hoặc khẳng định
  thực nghiệm ngoài nguồn. Công thức cận mẫu thiếu thiết lập đã được bỏ hoàn
  toàn; chỉ giữ cảnh báo về phạm vi giả thiết.
- Tự kiểm theo `no-ai-slop/eval.md`: bỏ lời dẫn quy trình, tiêu đề thừa, nhịp câu
  quảng bá và các công thức không đủ căn cứ. Rà mạch theo Quill mà không tạo
  `quill.json`: 15 chủ đề thuộc đủ bốn nhóm, bảy mạch tiến từ Q-learning dạng
  bảng đến giao diện DQN, vòng huấn luyện, bất ổn và Atari.
- Material viewer được kiểm trên bản sao tối thiểu không chứa `.env`: 15 mã chủ
  đề duy nhất và không hiển thị, 278 biểu thức KaTeX, ba bài tập, ba gợi ý, ba
  lời giải, không lỗi console và không tràn ngang ở 1280×720 hay 390×844.
- Cổng 8765 đang bị tiến trình khác chiếm; lượt viewer riêng dùng cổng 18765.
  Kiểm định deck Bài 08 tại cổng 8765 đã được ghi ở mục trên. Codex Slides vẫn
  không khả dụng do giới hạn Node.js đã nêu.
- Tái kiểm toán–thuật toán bằng DeepSeek trả PASS. Tái kiểm mạch bằng GLM phát
  hiện topic-05 ở mạch 3 phụ thuộc topic-04 từng bị xếp ở mạch 4; đã chuyển
  topic-04 về mạch 3 và cân lại mạch 3/4 thành 29/24 phút, tổng vẫn là 120 phút.
- Tái kiểm hẹp lần cuối bằng GLM xác nhận PASS: 15 chủ đề xuất hiện đúng một mạch,
  quan hệ topic-04 → topic-05 → topic-06 đúng thứ tự và tổng thời lượng là 120 phút.

## Đồng bộ lecture note → deck

- Reader kế hoạch dùng `requested_model=observed_model=deepseek/deepseek-v3.2`,
  provider OpenRouter, profile `plan/12/600/16000`; hoàn tất vòng 8 sau 264,68 giây.
- Writer HTML dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, provider
  OpenRouter, profile `write/20/900/32000`; ghi 42.620 byte ở vòng 3 và hoàn tất
  vòng 4 sau 329,885 giây. Worker chỉ sửa tệp HTML đã giao.
- Đã gắn đúng một `data-note-topic-id` cho cả 37 trang có `data-slide-id`; đủ 15
  chủ đề của note. Bổ sung notes về giới hạn replay, giới hạn bộ tối ưu, đối chiếu
  giả mã nguồn và ba hướng thảo luận; không đổi mặt trang, thứ tự, SVG hoặc CSS.
- Outline và storyboard ghi bảng ánh xạ hai chiều. Bài tập được gắn với chủ đề
  chi phối trực tiếp: `X01` → topic-09, `X02` → topic-05, `X03` → topic-15.
- Reviewer mạch phát hiện hai lỗi trung bình: cầu nối topic-13 đứng sau vấn đề
  topic-01 và `L08-02` bị gắn nhầm topic-15. Đã chuyển `L08-04`–`L08-05` lên
  trước `L08-03`, gắn `L08-02` vào topic-01 và sửa câu nối ở notes.
- Lượt writer sắp xếp cấu trúc nhận một phản hồi `finish_reason=error`, sau đó
  kết thúc mà không gọi công cụ ghi và tuyên bố sai rằng thứ tự đã đạt. Điều phối
  viên không chấp nhận kết quả này; kiểm tra chuỗi ID cho thấy M2/M3 vẫn sai.
- Điều phối viên sắp lại M2/M3 theo đặc tả đã duyệt. Phép di chuyển theo dòng làm
  lộ `X02` là khối nhiều dòng; kiểm định tĩnh phát hiện thiếu một notes và số
  section ngoài giảm. `X02` được khôi phục nguyên vẹn từ `HEAD`, giữ thêm thuộc
  tính ánh xạ. Sau sửa: 37 ID duy nhất, 37 notes, 7 section ngoài.
- Lượt rà mạch tiếp theo yêu cầu đưa toàn bộ bất ổn trước bộ tối ưu vì giả định
  mã topic phải tăng tuần tự. Không áp dụng: note và deck đều chủ ý dùng mạch
  “bộ tối ưu phụ trợ → quay lại bất ổn cấu trúc”, đã có câu nối ở `L08-26`.
  Đề xuất cục bộ hợp lệ được áp dụng: chuyển `L08-28` (tương quan/replay,
  topic-07) lên trước `L08-27`–`L08-30` (tổng hợp topic-12).
- Tái rà toàn mạch phát hiện `L08-15` quay lại topic-08 sau `X01` và `L08-21`
  quay lại topic-09 sau topic-11. Đã nhóm lại M3 thành hai đường tính → loss →
  bài tính/kiểm tra → vòng DQN → tensor → đồng bộ → bài sửa lỗi. Không đổi nội
  dung hay mã trang.
- Tái kiểm mạch cuối bằng GLM trả PASS sau khi nhóm lại M3. Kiểm định tĩnh xác
  nhận 37 ID duy nhất, 37 ánh xạ, đủ 15 topic, 37 notes, 7 section ngoài, không
  thiếu tài sản, không raster và không URL tài sản ngoài.
- `python3 -m reloadserver 8765` tiếp tục không khả dụng vì thiếu mô-đun. Fallback
  `python3 -m http.server 8765 --bind 127.0.0.1` chạy trên bản sao tối thiểu không
  chứa `.env`; mọi tài sản trả HTTP 200. Chromium duyệt đủ 37 trang ở 1280×720
  và 800×600: không lỗi console, lỗi tài nguyên hoặc tràn hình học.

## Đợt sửa 2026-10-22 — rà từng trang, trang tiêu đề mạch, giảm chữ

Phạm vi: deck `lecture-08-deep-q-learning.html`, tám SVG trong `img/lec-08/`, ghi chú bài giảng `materials/lec-08/lecture-note.md`, `outline.md`, `storyboard.md`, thẻ Bài 8 trong `index.html`. Quy trình: ba rà soát chỉ đọc trên bản đóng băng (37 trang, 7 section ngoài, không trang tiêu đề mạch) → kế hoạch sửa của điều phối viên → biên tập theo bước C0, C1…Cn (mỗi trang một bước) → rà lại sau mỗi mạch → rà toàn deck và kiểm định cuối.

### Vai và mô hình

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà cấu trúc–mạch (kèm `no-ai-slop` Detect, `quill` làm danh sách kiểm) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Rà sinh viên–mật độ (kèm kiểm trực quan Playwright) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Rà RL–toán (kèm đối chiếu ghi chú bài giảng) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập (tác tử duy nhất ghi tệp; `no-ai-slop` Edit) | Agent `general-purpose` | `claude-opus-5-5` | high | có |
| Điều phối viên (lập kế hoạch, duyệt, commit) | phiên chính | `claude-opus-5-5` | — | commit |

Điều phối viên chạy `claude-opus-5-5` theo quy định mới ngày 2026-10-22 (`AGENTS.md`, mục "Điều phối mô hình trong dự án"; commit `c3c98f8`). Mô hình và mức suy luận của các tác tử con ghi theo lời gọi công cụ của điều phối viên.

### Kết luận của ba rà soát

- Cấu trúc–mạch: thiếu toàn bộ trang tiêu đề mạch, trang Tiên quyết, Nội dung, Vấn đề trung tâm và mạch tổng kết chuẩn; mạch 5 cũ chỉ có một trang; trang vấn đề của bộ nhớ phát lại (`L08-28`) đứng sau cơ chế bốn mạch; Q-learning bảng và bộ ba bất ổn được dạy lại như nội dung mới; thuật ngữ lệch Bài 06–07. Đề xuất bảy mạch mới với nội dung trang tiêu đề mạch, trang mở bài và kết bài.
- Sinh viên–mật độ: `L08-10` tràn khung (chặn bàn giao); sáu trang vượt trần 60 âm tiết, `X03` vượt 1,5 lần trần; nhiều ký hiệu (sg, phép chọn theo hành động, $\mathcal D$, $\odot$, $\oslash$, CNN) chỉ được định nghĩa trong ghi chú diễn giả; SVG có nhãn chồng nét; ghi chú diễn giả chứa chỉ dẫn giảng viên, mã trang và "Đáp án".
- RL–toán: mọi ví dụ số đúng; bốn lỗi nghiêm trọng về lập luận: lý do không cần tỉ số lấy mẫu quan trọng, dấu cập nhật khi $\theta$ dùng chung, tương quan bị xếp vào bộ ba bất ổn, giả thiết hội tụ của Q-learning bảng; các lỗi trung bình về $Z$ trước định nghĩa, bán gradient, cài đặt `X02`, quan sát cuối khi tự đặt lại, vòng lặp ngoài của giả mã.

Quyết định của điều phối viên: kế hoạch sửa ngày 2026-10-22 (bảy mạch 10/25/15/30/10/15/15 phút; thuật ngữ theo Bài 06–07; ví dụ xuyên suốt "mini-batch hai mẫu chuyển"; thứ tự commit C0, C1…Cn). Khi báo cáo và kế hoạch khác nhau, theo kế hoạch.

### Bảng phát hiện gộp

Nguồn phát hiện: CT = rà cấu trúc–mạch, SV = rà sinh viên–mật độ, TH = rà RL–toán. Mức độ lấy mức cao nhất trong các báo cáo. Trạng thái "đã sửa ở C0" còn chờ điều phối viên duyệt.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|---|
| chặn bàn giao | `L08-10` | Tràn khung 16:9: công thức gradient ra ngoài khung, $L_B$ đè chân trang (SV). Sau C0 đáy nội dung ở 972 px trong khung 720 vì hình theo `max-height` 390 px của hệ chung. | Ảnh `shots-before/13-L08-10-wide.png`; kiểm C0 ở 1280×720 | `L08-17` định nghĩa $q_i,y_i,L_B$ trước; `L08-10` giữ hình, định nghĩa $\operatorname{sg}$ và gradient; gộp `L08-15`; vẽ lại SVG | mở | chấp nhận (kế hoạch, mạch 4) |
| nghiêm trọng | mạch 2–7 | Không mạch nào có trang tiêu đề mạch (CT, SV) | `grep strand-title` = 0 | Thêm `L08-M2T`…`L08-M7T`, `id="mach-N"` | mở | chấp nhận |
| nghiêm trọng | mở bài | Thiếu Tiên quyết và quy ước, Nội dung, Vấn đề trung tâm; bìa không có câu luận đề, phụ đề "Từ…đến…" (CT, SV) | `L08-01`, `L08-02` | Thêm `L08-01b`, `L08-01c`, `L08-02b`, `L08-02c`; sửa `L08-01` | bìa `L08-01` đã sửa ở S1; phần còn lại mở | chấp nhận |
| nghiêm trọng | kết bài | Thiếu bảng tổng kết chuẩn, trả lời vấn đề trung tâm, bài tổng hợp có lời giải, bài tập về nhà và tài liệu đọc, dòng nối Bài 09 (CT, SV) | `L08-33`, `L08-34` | `L08-34` thành bảng; thêm `L08-K1`–`L08-K5` | mở | chấp nhận |
| nghiêm trọng | `L08-26` (mạch 5 cũ) | Mạch chỉ có một trang, dựng để điều hướng (CT; SV nhẹ) | Bản đồ mạch cũ | Gộp mạch 4 và 5 cũ thành mạch 5 "Bộ tối ưu theo gradient" | đã sửa ở C0 | chấp nhận |
| nghiêm trọng | `L08-28`, `L08-13` | Vấn đề tương quan đứng sau cơ chế bộ nhớ phát lại bốn mạch (CT) | Thứ tự cũ: `L08-13` ở mạch 2, `L08-28` ở mạch 6 | Chuyển `L08-28` lên đầu mạch 3 | vị trí đã sửa ở C0; nội dung trang mở | chấp nhận |
| nghiêm trọng | `L08-03`–`L08-06`, `L08-30` | Dạy lại Q-learning bảng và bộ ba bất ổn như mới, không có "Nhắc lại:"; thiếu cầu nối từ Q-learning bán gradient tuyến tính của Bài 07 (CT, SV) | Bài 07 `L07-32`, `L07-36f` | Gộp `L08-04`, `L08-05` vào `L08-01b`; `L08-30` mở bằng "Nhắc lại:" | `L08-04`, `L08-05` gộp vào `L08-01b`, `L08-01b2` ở S2; phần còn lại mở | chấp nhận |
| nghiêm trọng | toàn deck | Thuật ngữ lệch Bài 06–07: "bộ ba nguy hiểm", khám phá, greedy, chuyển tiếp, episode, return, TD error; tiếng Anh trần optimizer, loss, replay, gather (CT, SV, TH) | Deck 06, deck 07, ghi chú Bài 07 | Bảng thuật ngữ trong `outline.md`; sửa khi sửa từng trang, cả SVG và ghi chú bài giảng | bảng thuật ngữ có ở C0; câu chữ mở | chấp nhận |
| nghiêm trọng | (thiếu) | Không nhắc lại mạng nơ-ron, lan truyền ngược, mạng tích chập (SV) | `L08-07`, `L08-31` | Thêm trang "Nhắc lại: mạng nơ-ron" | dòng Nhắc lại có ở `L08-01b2` (S2); `L08-31` mở | chấp nhận một phần: một dòng "Nhắc lại:" trong `L08-01b` và tên đầy đủ "mạng tích chập (CNN)" ở `L08-31`; không thêm trang riêng vì mạch 1 có 10 phút và nguồn (tr. 17) chỉ dùng mạng như công cụ |
| nghiêm trọng | `X03` | 91 âm tiết, vượt 1,5 lần trần 60 (CT, SV) | Đo mặt trang | Tách `X03` (câu hỏi) và `X03b` (lời giải) | mở | chấp nhận |
| nghiêm trọng | `L08-34` (ghi chú) | Mã trang "L08-02" trong ghi chú diễn giả (CT, SV) | Ghi chú `L08-34` | Xóa mã trang | mở | chấp nhận |
| nghiêm trọng | `L08-33` | Lời chỉ đường trên mặt trang "Bài tập kế là một ablation…" (CT; SV trung bình) | Mặt trang | Xóa hộp | mở | chấp nhận |
| nghiêm trọng | `L08-05`; ghi chú `L08-13`; ghi chú bài giảng dòng 106–112, 297–305 | Lý do không cần tỉ số lấy mẫu quan trọng nêu sai: với chính sách đích tham lam, $\max_{a'}Q$ chính là kỳ vọng theo chính sách đích (TH) | Sutton và Barto (2018), §6.6, §7.3 | Lý do đúng: $A_t$ là đối số điều kiện của $Q(S_t,A_t)$; hành động kế tiếp được tính trọn bằng phép cực đại, không lấy mẫu từ hành vi | `L08-01b` và ghi chú bài giảng (tiên quyết, mục bộ nhớ phát lại) đã sửa ở S2; ghi chú diễn giả `L08-13` và trang `L08-05r` mở | chấp nhận (sửa mọi chỗ) |
| nghiêm trọng | `L08-21`; ghi chú bài giảng dòng 389–391, 655–656 | "Gradient theo $q_1$ âm nên $q_1$ tăng" chỉ đúng khi bỏ qua giao thoa qua $\theta$ dùng chung (TH) | $\Delta q_1\approx\eta(1{,}5\lVert\nabla q_1\rVert^2-0{,}5\nabla q_1^\top\nabla q_2)$ | Thêm giả thiết "xét $q_1,q_2$ như hai biến riêng" vào câu hỏi; ghi chú nêu công thức | mở | chấp nhận |
| nghiêm trọng | `L08-27`; ghi chú bài giảng dòng 502–504 | Tương quan giữa các mẫu liền nhau bị xếp vào bộ ba bất ổn (TH) | Nguồn tr. 29; Sutton và Barto (2018), §11.3; Bài 07 | Bảng `Nguồn bất ổn \| Cơ chế giảm \| Điều còn lại`; tương quan nằm ngoài bộ ba | mở | chấp nhận |
| nghiêm trọng | ghi chú `L08-04`; ghi chú bài giảng dòng 114–117 | Hội tụ của Q-learning bảng thiếu giả thiết: MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$ (TH) | Ghi chú Bài 07 dòng 30 | Dòng "Nhắc lại:" đủ giả thiết ở `L08-01b` và ghi chú bài giảng; $Q^*$ thành $q_*$ | đã sửa ở S2 (`L08-01b2`, mục Kiến thức tiên quyết) | chấp nhận |
| trung bình | `L08-07` | Ba luận điểm trên một trang; phản ví dụ không có số; tiêu đề ẩn dụ; $o$, $\mathcal O$ chưa định nghĩa; giả thiết Markov chỉ ở ghi chú (CT, SV, TH) | Mặt trang và ghi chú | Tách `L08-07`, `L08-07b`, `L08-07c`; dòng "Giả thiết:" về Markov | $\mathcal O$, $O_t$ và điều kiện viết $S_t$ đã có ở `L08-01c` (S3); phần còn lại mở | chấp nhận; ví dụ số theo kế hoạch ($\theta_0=0\to0{,}5$, đích $1\to1{,}45$), không dùng ví dụ "đích tăng 0,72" của SV |
| trung bình | `L08-05` | "replay" dùng trước khi giới thiệu; 82 âm tiết; "sao lưu" là thuật ngữ mới (CT, SV) | Mặt trang | Phần khác chính sách sang `L08-05r` ở mạch 3; bỏ trang | trang đã bỏ ở S2; `L08-05r` mở | chấp nhận |
| trung bình | `L08-20`, `L08-31` | $[b,4,h,w]$ dùng trước khi có bốn khung; $h,w$ chưa định nghĩa (CT, SV, TH) | Thứ tự cũ | `L08-31` lên mạch 2; dòng "Nhắc lại:" bốn khung và định nghĩa $h,w$ ở `L08-20` | vị trí đã sửa ở C0; dòng Nhắc lại mở | chấp nhận |
| trung bình | `L08-10`, `L08-15`, `L08-17` | Ba trang lặp hàm mất mát và hai đường tính; $L_B$ ở `L08-10` dùng $q_i,y_i$ trước định nghĩa (CT, SV, TH) | Mặt trang | `L08-17` lên đầu mạch 4; gộp `L08-15` vào `L08-10` | vị trí đã sửa ở C0; gộp mở | chấp nhận |
| trung bình | `L08-10` | $\operatorname{sg}$ và phép chọn theo hành động chưa định nghĩa trên mặt trang; chưa nối bán gradient Bài 07; ghi chú dẫn chiếu "đã giải thích ở phần trước" (CT, SV, TH) | Mặt trang và ghi chú | Dòng định nghĩa $\operatorname{sg}$; "Nhắc lại:" bán gradient | mở | chấp nhận |
| trung bình | `L08-16` | Trùng bước 9 của giả mã; trục SVG không nhãn; $\theta^-$ không vẽ dạng bậc thang (CT, SV, TH) | Mặt trang, ảnh SVG | Bỏ trang; hình vẽ lại sang `L08-07c`; thứ tự đồng bộ vào ghi chú `L08-19` | mở | chấp nhận |
| trung bình | `L08-12` | Tự đặt lại và quan sát cuối chỉ có trong ghi chú; "thường vẫn bootstrap" mơ hồ; không có ví dụ (CT, SV, TH) | Mặt trang | $U=1,Z=0$ vẫn bootstrap; đặt lại khi $Z\lor U$, mặt nạ chỉ $1-Z$; hình dòng thời gian; dòng tự đặt lại sang `L08-13` | mở | chấp nhận |
| trung bình | `L08-18` | 87 âm tiết; dòng Đầu vào > 20 âm tiết; $N_{\mathrm{start}}$, $F$ chưa có nghĩa; "optimizer" trước mạch 5; $O_{t+1}$ hai nghĩa ở ranh giới lượt; văn xuôi trong phông Courier (CT, SV, TH) | Đo mặt trang; ảnh | Tách `L08-18a`; mỗi siêu tham số một dòng nghĩa; dòng "Lưu ý:" về quan sát cuối | phông Courier bỏ ở C0 (giả mã thành `ol`); phần còn lại mở | chấp nhận |
| trung bình | `L08-19` | Thiếu vòng lặp ngoài và ngân sách dừng; bước 10 ngoài khối; "Gather", "no-grad", "MSE" dạng mã (CT, SV, TH) | Mặt trang | "quay lại bước 1"; $T_{\max}$; viết bằng lời | mở | chấp nhận |
| trung bình | `L08-18`, `X02` | Quy tắc dự phòng `final_observation` sai với Gymnasium 1.x (trường `final_obs`); lưu nhầm quan sát sau đặt lại (TH) | TH ghi cần kiểm lại tên trường | Không gắn tên trường cố định trên mặt trang; ghi chú nói tên trường phụ thuộc phiên bản API; không lưu mẫu chuyển nối hai lượt | mở | chấp nhận |
| trung bình | `X02` | Trộn mã thu thập với mã batch; lỗi thứ năm `.max()` không chiều; `terminated.float()` với bool Python; không ngữ cảnh API; dấu tiếng Việt lệch trong khối mã; thiếu nhãn Lời giải (CT, SV, TH) | Mã; ảnh `shots-before/23-X02-wide.png` | Mã nhất quán theo batch; bỏ chú thích tiếng Việt khỏi mã; tách `X02b` nếu cần | nhãn "Lời giải:" thêm ở C0; phần còn lại mở | chấp nhận |
| trung bình | `L08-22` | Dẫn chiếu "bước 8 giả mã"; khai báo $\rho,\beta$ trước khi dùng; tiêu đề tiếng Anh; $L_{B_j}$ còn phụ thuộc $\theta^-$ (CT, SV, TH) | Mặt trang | Hình chuỗi $B_j\to L_{B_j}\to g_j\to\theta_j$; dời miền tham số sang `L08-24`, `L08-25` | mở | chấp nhận |
| trung bình | `L08-29` | Không có số; ghi chú dẫn chiếu trang trước; $\theta$ và $\theta^-$ tại mốc đồng bộ dễ nhầm (CT, SV, TH) | Mặt trang | Mẫu 1: $4{,}6\to5{,}5$, $\Delta y=0{,}9$; ký hiệu $\theta^-$ cũ và mới; hình bậc thang | mở | chấp nhận |
| trung bình | mật độ | Vượt trần 60 không có ngoại lệ: `L08-05` 82, `L08-18` 87, `L08-27` 70, `L08-28` 64, `L08-32` 68; `L08-33` 73 (CT, SV) | `measure.json` của SV | Tách hoặc chuyển sang ghi chú; ghi số trước và sau vào storyboard | mở | chấp nhận |
| trung bình | toàn deck | Khối `<style>` cục bộ thu nhỏ mọi trang `.82em`, định nghĩa lại `.box`, `.card`, `.grid2`, …; `div.reveal` thiếu `lecture-deck` (CT, SV) | Dòng 12–22 bản cũ | Bỏ khối style; thêm `lecture-deck`; thay lớp riêng bằng cấu trúc chung | đã sửa ở C0 | chấp nhận |
| trung bình | `L08-09`, `X01`, `L08-21`, `X02`, `L08-32`, `X03` | Lời giải không có nhãn "Lời giải:", không theo từng bước; ghi chú thiếu "Gợi ý:" (CT, SV) | Mặt trang | Nhãn "Lời giải:", mỗi bước một dòng; "Gợi ý:" trong ghi chú | nhãn thêm ở C0; từng bước và Gợi ý mở | chấp nhận |
| trung bình | ghi chú diễn giả nhiều trang | Mở bằng "Trang này", lời chuyển "Trang kế…", chỉ dẫn giảng viên ("Nhấn mạnh:", "Mời người học", "Yêu cầu người học", "khi giảng"), siêu dữ liệu biên soạn, "Đáp án" (CT, SV) | `L08-03`, `L08-06`, `L08-11`, `L08-14`, `L08-15`, `L08-18`, `L08-26`, `L08-27`, `L08-30`, `L08-33`, `X01` | Viết lại thành giải thích học thuật; "Lời giải" | mở | chấp nhận |
| trung bình | `L08-02` | Bốn thẻ lệch sáu mục tiêu; tên "Kết quả học tập"; thẻ "Mục tiêu" mơ hồ; ghi chú có siêu dữ liệu (CT, SV, TH) | Mặt trang; `outline.md` | "Mục tiêu học tập", sáu mục ứng mạch 2–7 | đã sửa ở S4 (trang và ghi chú bài giảng) | chấp nhận |
| trung bình | `L08-06` | Cảnh báo phủ định một cận mẫu chưa từng nêu (CT, SV) | Mặt trang | Bỏ trang; ý quy mô vào `L08-02c` và `L08-03` | mở | chấp nhận |
| trung bình | ví dụ | Không có ví dụ xuyên suốt; số của `L08-09` lặp ngầm ở `X01` (CT) | Mặt trang | "Mini-batch hai mẫu chuyển" với bảng cùng khuôn ở mỗi lần dùng | mở | chấp nhận |
| trung bình | `L08-04`, `L08-08`, `L08-09` | $Z_{t+1}$ dùng trên mặt trang trước khi định nghĩa (TH, SV) | Mặt trang | Định nghĩa $Z$ ở `L08-08`; dòng Nhắc lại ở `L08-01b` không dùng $Z$ | `L08-04` đã bỏ ở S2, `L08-01b` không dùng $Z$; `L08-08`, `L08-09` mở | chấp nhận |
| trung bình | `L08-08` | "Đồng bộ" dùng trước định nghĩa; câu mở kể tiến trình; ghi chú "đích không đổi ở mọi bước tối ưu" mâu thuẫn câu sau (CT, SV, TH) | Mặt trang và ghi chú | `L08-07c` định nghĩa đồng bộ trước `L08-08` | mở | chấp nhận |
| trung bình | `L08-11` | Thiếu dòng Nhu cầu; SVG ghi $s'$, thiếu $\epsilon_{\mathrm{exp}}$-tham lam, cạnh không nhãn, chữ tràn hộp; ghi chú chỉ dẫn giảng viên (CT, SV, TH) | Ảnh SVG | "Nhu cầu:"; vẽ lại SVG | mở | chấp nhận |
| trung bình | `L08-11` | Đề xuất đưa vòng huấn luyện lên đầu mạch 2 làm bản đồ (SV) | Thứ tự cũ | — | đóng | bác bỏ: hình dùng bộ nhớ phát lại, mini-batch và mạng mục tiêu, các khái niệm chỉ có sau mạch 2–3; kế hoạch giữ `L08-11` mở cụm thuật toán ở mạch 4 với dòng "Nhu cầu:" |
| trung bình | `L08-14`, `L08-28` | Lặp nội dung tương quan; đề xuất gộp `L08-28` vào `L08-14` (SV) | Mặt trang | — | đóng | bác bỏ phần gộp: `L08-28` là trang vấn đề mở mạch 3, `L08-14` là trang giới hạn có Câu hỏi; phần lặp được cắt khi sửa từng trang |
| trung bình | `L08-23`, `L08-24`, `L08-25` | SGD chưa viết đầy đủ; $\odot,\oslash$ chưa định nghĩa; Adam không có câu giải thích (CT, SV, TH) | Mặt trang | "Ký hiệu:", "Ý nghĩa:" | mở | chấp nhận |
| trung bình | `L08-26` | Thiếu Ký hiệu $m_j,v_j$; câu giới hạn bộ tối ưu chỉ ở ghi chú; ghi chú có "Trang kế…", "Nhấn mạnh:" (CT, TH) | Mặt trang và ghi chú | Dòng Ký hiệu; câu kết bộ tối ưu không sửa đích, dữ liệu, xấp xỉ hàm | mở | chấp nhận |
| trung bình | ký hiệu | $m_j,v_j,\rho$ trùng $v_\pi$, $m=\lvert\mathcal A\rvert$, $\rho_t$ của Bài 07; $q_t,q_i$ trùng $q_\pi,q_*$; đề xuất đổi tên hoặc thêm Ký hiệu (TH) | Ghi chú Bài 07 | — | mở | chấp nhận dòng "Ký hiệu:" ($q_i$ ở mở bài và `L08-17`; $m_j,v_j,\rho$ ở mạch 5); bác bỏ đổi tên: $m_j,v_j,\rho$ là tên chuẩn của RMSprop và Adam (nguồn tr. 25–26), $q_i$ giữ theo `note-for-author.md` |
| trung bình | ghi chú bài giảng dòng 300 | "phá vỡ tương quan theo thời gian" mâu thuẫn dòng 324, 329 và `note-for-author.md` (TH, CT) | Ghi chú bài giảng | "giảm tương quan ngắn hạn" | mở | chấp nhận |
| trung bình | ghi chú bài giảng dòng 586 | "Đầu vào trạng thái: chồng bốn khung" (TH) | Ghi chú bài giảng | "quan sát; xấp xỉ trạng thái" | mở | chấp nhận |
| trung bình | ghi chú bài giảng, mục bảy mạch | Thứ tự chủ đề và thời lượng của bảy mạch trong ghi chú lệch deck (TH) | Ghi chú dòng 52–60 | Đồng bộ khi tới trang tiêu đề mạch tương ứng | mở | chấp nhận |
| trung bình | SVG | Nhãn chồng nét, mũi tên che chữ, chữ tràn hộp; phông serif; cỡ nhãn khoảng 0,71 em ở bốn hình (SV, CT, TH) | Ảnh, `svgsize.py` | Vẽ lại theo mục A.8 của kế hoạch | mở | chấp nhận |
| trung bình | `L08-32` | 68 âm tiết; thẻ chung chung (SV, CT) | Đo mặt trang | Rút mỗi thẻ ≤ 15 âm tiết; Lời giải | nhãn "Lời giải:" thêm ở C0; phần còn lại mở | chấp nhận |
| trung bình | `L08-28` | 64 âm tiết; "cỡ mẫu hiệu dụng" chưa định nghĩa; không có ví dụ; "mini-batch liên tiếp" mơ hồ (SV, CT, TH) | Đo mặt trang | Dòng "Muốn…"; ví dụ bốn mẫu liền nhau; hình dải quỹ đạo | mở | chấp nhận |
| trung bình | `L08-13` | Mở bằng ký hiệu; $\mathcal D$ chưa định nghĩa; $\tau_k$ chưa giải thích; không nêu ghi đè; không có ví dụ (CT, SV, TH) | Mặt trang, SVG | "Nhu cầu:"; ví dụ $N=6$ | mở | chấp nhận |
| trung bình | `L08-03` | Không có Nhu cầu và ví dụ số; SVG ghi "o hoặc s", $Q(s,a)$; ghi chú "trang này chốt…" (CT, SV, TH) | Mặt trang, SVG | Lunar Lander $9\,216$/$1\,896$ ô; sửa nhãn SVG | mở | chấp nhận |
| trung bình | `L08-17` | Hộp $Z/U$ lặp lần thứ ba; "$U_i$ điều khiển reset" sai trong batch (SV, CT, TH) | Mặt trang | Bỏ hộp; "Ký hiệu:" $q_i$ | mở | chấp nhận |
| nhẹ | tiêu đề | Tiêu đề ẩn dụ hoặc dạng câu (CT) | Mục 3 báo cáo CT | Tiêu đề mới theo `storyboard.md` | mở | chấp nhận |
| nhẹ | `no-ai-slop` | Tương phản nhị phân, colon reveal, siêu văn bản diễn giải, lời dẫn tiến trình, kết lặp lại (CT, SV) | `L08-05`, `L08-14`, `L08-31`, ghi chú `L08-07`, `L08-26`, `L08-27` | Viết thành mệnh đề khẳng định có điều kiện | mở | chấp nhận |
| nhẹ | nhiều trang | Dòng > 20 âm tiết; trang > 6 dòng (SV) | Bảng mật độ SV | Tách câu, gộp mục | mở | chấp nhận |
| nhẹ | 12 trang | Ghi chú diễn giả dưới 40 âm tiết (SV) | `notes.json` | Bổ sung giả thiết hoặc chỗ dễ nhầm | mở | chấp nhận |
| nhẹ | `L08-14` | Mẫu lấy đều có hoàn lại là i.i.d. theo phân phối của bộ đệm hiện tại; cái thiếu là một phân phối cố định (TH) | — | Dòng "Lưu ý:" | mở | chấp nhận |
| nhẹ | `L08-31` | SVG vẽ tiền xử lý sau bốn khung; đầu ra thiếu $\theta$, $o$; hai dòng chú thích đè nhau; CNN chưa viết đầy đủ; tương phản nhị phân (TH, SV, CT) | Ảnh SVG | Khung thô → tiền xử lý → xếp chồng bốn khung → mạng tích chập → $Q_\theta(O_t,a_k)$ | mở | chấp nhận |
| nhẹ | `X03` | Nhánh loại bỏ chưa định nghĩa đủ để so sánh công bằng (TH) | — | Bỏ mạng mục tiêu: $C=1$, vẫn dừng gradient; bỏ bộ nhớ: $N=b$; giữ số bước | mở | chấp nhận |
| nhẹ | `L08-30` | $\epsilon$ thiếu chỉ số exp; "lệch chính sách" và "khác chính sách" (TH, SV) | Mặt trang, SVG | Thống nhất $\epsilon_{\mathrm{exp}}$ và "khác chính sách" | mở | chấp nhận |
| nhẹ | ghi chú bài giảng dòng 75–83, 376–379, 467–468, 554–555, 571 | Trực giác $q_*$ viết sai; $Q_k$ lệch $Q_t$; $L_B$ thiếu $\operatorname{sg}$; câu broadcast của phép chọn sai chỗ; khẳng định về Adam và hai cơ chế chưa ghi nguồn (TH) | Ghi chú bài giảng | Sửa khi tới mục tương ứng | mở | chấp nhận |
| nhẹ | ghi chú `L08-10`, `L08-18`, `L08-19` | Có thể dẫn Mnih và cộng sự (2015), Extended Data Table 1 cho $N_{\mathrm{start}}$, $F$, $C$ đếm theo bước cập nhật (TH) | — | Ghi vào dòng "Nguồn:" của ghi chú diễn giả | mở | chấp nhận |
| nhẹ (gợi ý) | `L08-08` hoặc `L08-17` | "Ý nghĩa:" của đích theo lặp Q có khớp (fitted Q-iteration), Riedmiller (2005) (TH) | — | Dòng "Ý nghĩa:" với giả thiết $O$ Markov và $\theta^-$ cố định | mở | chờ điều phối viên: kế hoạch không nêu; cần nguồn ngoài và giả thiết Markov |
| nhẹ | ghi chú bài giảng | Khoảng 6 400 từ, dưới 8 000 từ của chuẩn giáo trình; chưa có bảng ký hiệu (CT, ngoài phạm vi) | Đếm từ | — | mở | chờ điều phối viên: ngoài phạm vi kế hoạch (mục A.7 chỉ đồng bộ ghi chú với trang) |
| trung bình | `L08-20` | Phát hiện ở C0: sau khi bỏ CSS cục bộ, đáy nội dung ở 729 px trong khung 720 vì hình theo `max-height` 390 px của hệ chung (bản cũ 330 px) | Kiểm C0 ở 1280×720; ảnh `c0/shots/25-L08-20-1600.png` | Sửa ở bước `L08-20`; không thu nhỏ chữ | mở | chờ điều phối viên |
| trung bình | `X02` | Phát hiện ở C0: đáy nội dung ở 755 px sau khi thêm dòng "Lời giải:"; khối `pre` mang `style` nội dòng `font-size:.94em;width:100%` vì `lecture-slide.css` không có quy tắc cho `pre` (theme đặt `.55em`) | Kiểm C0; ảnh `c0/shots/26-X02-1600.png` | Tách `X02b` ở bước `X02`; quyết định thêm quy tắc `pre` vào CSS chung hoặc giữ kiểu nội dòng | mở | chờ điều phối viên |
| nhẹ | `L08-25` | Phát hiện ở C0: sau khi bỏ `.smallmath` (`.94em`), dòng công thức thứ hai rộng tới 1 285 px, vượt mép phải vùng nội dung (1 256 px) và chạm vùng nút điều hướng | Kiểm C0 ở 1280×720; ảnh `c0/shots/30-L08-25-1280.png` | Tách $\theta_j$ thành dòng riêng ở bước `L08-25` | mở | chờ điều phối viên |

### Bước C0 — sắp lại bảy mạch, bỏ CSS cục bộ (biên tập viên)

- Deck: bảy section ngoài theo `storyboard.md`, mục "Danh sách trang theo mạch", chỉ bằng di chuyển trang. Các trang sẽ gộp hoặc bỏ (`L08-04`, `L08-05`, `L08-06` ở mạch 1; `L08-15`, `L08-16` ở mạch 4) nằm tạm sát vị trí đích. Mạch 5 cũ (`L08-26`) gộp vào mạch bộ tối ưu; `L08-28` lên đầu mạch 3; `L08-31`, `L08-32` lên mạch 2; `X03` sang mạch 6; `L08-33` sang mạch 7.
- CSS: bỏ khối `<style>`; `div.reveal` thêm lớp `lecture-deck`. Thay lớp riêng: `.codebox` thành `p` + `ol` (bước 1–4) và `ol.substeps` (bước 5–9) như deck 05; `.answer` thành đoạn `.fragment` mở bằng "**Lời giải:**"; `.warn` thành đoạn mở bằng "**Lưu ý:**"; bỏ `.smallmath`, `.compact`. Hai khối `pre` của `X02` mang `style` nội dòng (xem phát hiện cuối bảng).
- Khai báo Reveal theo deck 06: bỏ `plugin/markdown/markdown.js` và `RevealMarkdown` (deck không dùng Markdown); thêm `scrollActivationWidth:null`; plugin `RevealHighlight`, `RevealNotes`, `RevealMath.KaTeX` cục bộ.
- Nội dung từng trang giữ nguyên, trừ nhãn "Lời giải:" và "Lưu ý:" thay cho lớp `.answer` và `.warn`.
- `outline.md`: phạm vi, sáu mục tiêu ứng mạch 2–7, danh sách bảy mạch, bảng thuật ngữ Việt–Anh, bảng ký hiệu và thời lượng mới; mục cũ đánh dấu "bản cũ".
- `storyboard.md`: bản đồ bảy mạch, danh sách trang theo mạch (quyết định, lý do, vị trí sau C0), lệch khỏi trật tự nguồn, số âm tiết trước sửa; phần cũ chuyển xuống mục "Bản trước đợt sửa 2026-10-22".
- `index.html`: thẻ Bài 8 (Bài giảng, Ghi chú bài giảng có liên kết viewer; Bài tập và Thực hành ở trạng thái "Chưa có").
- `no-ai-slop` (Edit, tự kiểm theo `eval.md`): phạm vi là câu mới trong `outline.md`, `storyboard.md`, mục này của nhật ký và mô tả thẻ Bài 8; hai nhãn "Lời giải:", "Lưu ý:" trên mặt trang. Câu chữ cũ của từng trang chưa sửa ở C0.

- Kiểm C0 (Playwright Chromium, `http://localhost:8799`): 37 `data-slide-id` duy nhất, 7 section ngoài, độ sâu `<section>` tối đa 2, mỗi trang có `aside.notes`, không còn `<style>` và không có URL mạng trong deck. Ở 1280×720, 1600×900 và 390×844: không lỗi console hoặc trang, không `.katex-error`, không yêu cầu ra ngoài máy chủ cục bộ, không cuộn ngang. `#/1`…`#/7` mở đúng trang đầu mỗi mạch; phím mũi tên đổi đúng chỉ số. Tràn đáy (> 702 px trong khung 720): `L08-10` 972 px (chặn bàn giao có từ trước), `L08-20` 729 px, `X02` 755 px; tràn phải: `L08-25` 1 285 px. Cỡ chữ thân nhỏ nhất 0,752 em (ô bảng, mã). Thẻ Bài 8 trong `index.html` và hai liên kết trả HTTP 200; viewer ghi chú Bài 08 hiển thị, 278 biểu thức KaTeX, không `.katex-error`, không khối `:::` sót. Ảnh trong thư mục `c0/` của scratchpad phiên.

### Quyết định của điều phối viên về C0 (2026-10-22)

- C0: **chấp nhận**. Đã đọc diff deck, `index.html`, planning; tự chạy Playwright (1600×900, 390×844, tắt hiệu ứng chuyển trang): 0 lỗi console, 0 `.katex-error`, 0 yêu cầu ngoài; tràn đáy `L08-10` (972 px, có từ trước), `L08-20` (729), `X02` (755); tràn phải `L08-25` (1 285). Bốn trang này sửa ở bước của chính trang đó.
- Kiểu nội tuyến `pre` ở `X02`: **giữ** (nhu cầu một trang; `lecture-slide.css` không đổi), xét lại ở bước `X02`.
- Liên kết ghi chú trên thẻ Bài 8 của `index.html`: **giữ** theo yêu cầu rõ của người dùng ("gắn chúng lên 2627-1/index.html"); ghi chú được sửa song song từng trang trong đợt này.
- Dòng "Ý nghĩa:" lặp Q có khớp (Riedmiller 2005): **bác bỏ** — ngoài nguồn và ngoài phạm vi đợt; không thêm nguồn ngoài khi không cần sửa sai.
- Độ dài ghi chú (~6 400 từ, dưới 8 000): **ngoài phạm vi đợt này**; ghi là giới hạn còn lại khi bàn giao.
- Bước S1 (`L08-01`, biên tập viên): bìa theo khuôn deck 06 (tên bài, "Bài 08 · Học tăng cường", câu luận đề một câu trong hộp, đơn vị, năm học); bỏ phụ đề "Từ … đến …"; ghi chú diễn giả viết lại (Bài 07 → các thành phần của DQN → phạm vi kết luận), 141 âm tiết; đoạn mở đầu của ghi chú bài giảng khớp câu luận đề, bỏ dòng giảng viên–thời lượng và đoạn mô tả tài liệu nguồn. Mặt trang 58 âm tiết. Điều phối viên yêu cầu luận đề một câu; đã sửa. Chờ điều phối viên duyệt.

### Quyết định của điều phối viên theo từng bước

| bước | trang | quyết định | căn cứ kiểm |
|---|---|---|---|
| S1 | `L08-01` | yêu cầu sửa (luận đề hai câu → một câu), rồi chấp nhận | diff; `check.py` 1600×900, 390×844; xem ảnh |
- Bước S2 (`L08-01b`, `L08-01b2`, biên tập viên): hai trang "Tiên quyết và quy ước" thay `L08-04`, `L08-05` (đã xóa); mỗi nhóm mở bằng "Nhắc lại:"; lý do không cần tỉ số lấy mẫu quan trọng và giả thiết hội tụ sửa theo Bài 06; mặt trang 55 và 59 âm tiết. Ghi chú bài giảng: mục "Kiến thức tiên quyết" thay Phần 1; câu lý do sai trong mục bộ nhớ phát lại đã sửa. Chờ điều phối viên duyệt.
| S2 | `L08-01b`, `L08-01b2` (thay `L08-04`, `L08-05`) | chấp nhận; "đích hồi quy (còn gọi là mục tiêu cập nhật)" ở `L08-08`; ghi chú `L08-13` sửa ở bước của trang | diff; tính lại lý do không cần tỉ số lấy mẫu quan trọng; `check.py`; xem ảnh 1600 |
- Bước S3 (`L08-01c`, biên tập viên): trang "Tiên quyết và quy ước", phần Ký hiệu, đặt sau `L08-01b2`: dòng "Ký hiệu:" và bảng bốn hàng; 58 âm tiết. Ghi chú bài giảng thêm mục "Bảng ký hiệu" 22 hàng với quy ước đọc; `outline.md` bổ sung bảng ký hiệu, $\gamma\in[0,1)$. Đề xuất: khai báo $q_i$ ở `L08-17` thay vì ở mở bài (lệch dòng quyết định "$q_i$ ở mở bài và `L08-17`"), chờ điều phối viên. Chờ điều phối viên duyệt.
| S3 | `L08-01c` | chấp nhận; $q_i$ khai báo ở `L08-17`; $\gamma\in[0,1)$ đồng bộ ở `L08-18`; kích thước ảnh dùng $H\times W$ ở `L08-20` | diff; `check.py`; xem ảnh 1600 |
- Bước S4 (`L08-02`, biên tập viên): tiêu đề "Mục tiêu học tập"; sáu mục đánh số ứng mạch 2–7, mặt trang 79 âm tiết (trần 80), ghi chú diễn giả 150 âm tiết, bỏ siêu dữ liệu biên soạn. `L08-01c` thêm "(optimizer)" ở lần dùng đầu "bộ tối ưu". Ghi chú bài giảng: mục "Mục tiêu học tập" thay đoạn "Sau bài này…". Chờ điều phối viên duyệt.
| S4 | `L08-02` | chấp nhận | diff; xem ảnh 1600 |
