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
| nghiêm trọng | mạch 2–7 | Không mạch nào có trang tiêu đề mạch (CT, SV) | `grep strand-title` = 0 | Thêm `L08-M2T`…`L08-M7T`, `id="mach-N"` | `L08-M2T` đã thêm ở S7, `L08-M3T` ở S17, `L08-M4T` ở S22; mạch 5–7 mở | chấp nhận |
| nghiêm trọng | mở bài | Thiếu Tiên quyết và quy ước, Nội dung, Vấn đề trung tâm; bìa không có câu luận đề, phụ đề "Từ…đến…" (CT, SV) | `L08-01`, `L08-02` | Thêm `L08-01b`, `L08-01c`, `L08-02b`, `L08-02c`; sửa `L08-01` | bìa `L08-01` (S1), Tiên quyết `L08-01b`, `L08-01b2`, `L08-01c` (S2–S3), Nội dung `L08-02b` (S5), Vấn đề trung tâm `L08-02c` (S6) đã có; mạch mở đầu đủ | chấp nhận |
| nghiêm trọng | kết bài | Thiếu bảng tổng kết chuẩn, trả lời vấn đề trung tâm, bài tổng hợp có lời giải, bài tập về nhà và tài liệu đọc, dòng nối Bài 09 (CT, SV) | `L08-33`, `L08-34` | `L08-34` thành bảng; thêm `L08-K1`–`L08-K5` | mở | chấp nhận |
| nghiêm trọng | `L08-26` (mạch 5 cũ) | Mạch chỉ có một trang, dựng để điều hướng (CT; SV nhẹ) | Bản đồ mạch cũ | Gộp mạch 4 và 5 cũ thành mạch 5 "Bộ tối ưu theo gradient" | đã sửa ở C0 | chấp nhận |
| nghiêm trọng | `L08-28`, `L08-13` | Vấn đề tương quan đứng sau cơ chế bộ nhớ phát lại bốn mạch (CT) | Thứ tự cũ: `L08-13` ở mạch 2, `L08-28` ở mạch 6 | Chuyển `L08-28` lên đầu mạch 3 | vị trí đã sửa ở C0; nội dung trang (vấn đề, ví dụ, hình) sửa ở S18 | chấp nhận |
| nghiêm trọng | `L08-03`–`L08-06`, `L08-30` | Dạy lại Q-learning bảng và bộ ba bất ổn như mới, không có "Nhắc lại:"; thiếu cầu nối từ Q-learning bán gradient tuyến tính của Bài 07 (CT, SV) | Bài 07 `L07-32`, `L07-36f` | Gộp `L08-04`, `L08-05` vào `L08-01b`; `L08-30` mở bằng "Nhắc lại:" | `L08-04`, `L08-05` gộp vào `L08-01b`, `L08-01b2` ở S2; phần còn lại mở | chấp nhận |
| nghiêm trọng | toàn deck | Thuật ngữ lệch Bài 06–07: "bộ ba nguy hiểm", khám phá, greedy, chuyển tiếp, episode, return, TD error; tiếng Anh trần optimizer, loss, replay, gather (CT, SV, TH) | Deck 06, deck 07, ghi chú Bài 07 | Bảng thuật ngữ trong `outline.md`; sửa khi sửa từng trang, cả SVG và ghi chú bài giảng | bảng thuật ngữ có ở C0; câu chữ mở | chấp nhận |
| nghiêm trọng | (thiếu) | Không nhắc lại mạng nơ-ron, lan truyền ngược, mạng tích chập (SV) | `L08-07`, `L08-31` | Thêm trang "Nhắc lại: mạng nơ-ron" | dòng Nhắc lại có ở `L08-01b2` (S2); `L08-31` mở | chấp nhận một phần: một dòng "Nhắc lại:" trong `L08-01b` và tên đầy đủ "mạng tích chập (CNN)" ở `L08-31`; không thêm trang riêng vì mạch 1 có 10 phút và nguồn (tr. 17) chỉ dùng mạng như công cụ |
| nghiêm trọng | `X03` | 91 âm tiết, vượt 1,5 lần trần 60 (CT, SV) | Đo mặt trang | Tách `X03` (câu hỏi) và `X03b` (lời giải) | mở | chấp nhận |
| nghiêm trọng | `L08-34` (ghi chú) | Mã trang "L08-02" trong ghi chú diễn giả (CT, SV) | Ghi chú `L08-34` | Xóa mã trang | mở | chấp nhận |
| nghiêm trọng | `L08-33` | Lời chỉ đường trên mặt trang "Bài tập kế là một ablation…" (CT; SV trung bình) | Mặt trang | Xóa hộp | mở | chấp nhận |
| nghiêm trọng | `L08-05`; ghi chú `L08-13`; ghi chú bài giảng dòng 106–112, 297–305 | Lý do không cần tỉ số lấy mẫu quan trọng nêu sai: với chính sách đích tham lam, $\max_{a'}Q$ chính là kỳ vọng theo chính sách đích (TH) | Sutton và Barto (2018), §6.6, §7.3 | Lý do đúng: $A_t$ là đối số điều kiện của $Q(S_t,A_t)$; hành động kế tiếp được tính trọn bằng phép cực đại, không lấy mẫu từ hành vi | `L08-01b` và ghi chú bài giảng (tiên quyết, mục bộ nhớ phát lại) đã sửa ở S2; ghi chú diễn giả `L08-13` đã sửa ở S19 (bỏ lý do sai; ý khác chính sách để cho `L08-05r`); trang `L08-05r` thêm ở S20 (lý do đúng trên mặt trang, ghi chú diễn giả và Mệnh đề 08.8 của ghi chú bài giảng); `note-for-author.md` dòng 15 sửa ở S20 | chấp nhận (sửa mọi chỗ) |
| nghiêm trọng | `L08-21`; ghi chú bài giảng dòng 389–391, 655–656 | "Gradient theo $q_1$ âm nên $q_1$ tăng" chỉ đúng khi bỏ qua giao thoa qua $\theta$ dùng chung (TH) | $\Delta q_1\approx\eta(1{,}5\lVert\nabla q_1\rVert^2-0{,}5\nabla q_1^\top\nabla q_2)$ | Thêm giả thiết "xét $q_1,q_2$ như hai biến riêng" vào câu hỏi; ghi chú nêu công thức | mở | chấp nhận |
| nghiêm trọng | `L08-27`; ghi chú bài giảng dòng 502–504 | Tương quan giữa các mẫu liền nhau bị xếp vào bộ ba bất ổn (TH) | Nguồn tr. 29; Sutton và Barto (2018), §11.3; Bài 07 | Bảng `Nguồn bất ổn \| Cơ chế giảm \| Điều còn lại`; tương quan nằm ngoài bộ ba | mở | chấp nhận |
| nghiêm trọng | ghi chú `L08-04`; ghi chú bài giảng dòng 114–117 | Hội tụ của Q-learning bảng thiếu giả thiết: MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$ (TH) | Ghi chú Bài 07 dòng 30 | Dòng "Nhắc lại:" đủ giả thiết ở `L08-01b` và ghi chú bài giảng; $Q^*$ thành $q_*$ | đã sửa ở S2 (`L08-01b2`, mục Kiến thức tiên quyết) | chấp nhận |
| trung bình | `L08-07` | Ba luận điểm trên một trang; phản ví dụ không có số; tiêu đề ẩn dụ; $o$, $\mathcal O$ chưa định nghĩa; giả thiết Markov chỉ ở ghi chú (CT, SV, TH) | Mặt trang và ghi chú | Tách `L08-07`, `L08-07b`, `L08-07c`; dòng "Giả thiết:" về Markov | $\mathcal O$, $O_t$ và điều kiện viết $S_t$ đã có ở `L08-01c` (S3); `L08-07` đã sửa ở S10 (chỉ giữ giao diện, tiêu đề "Mạng giá trị hành động", dòng "Nhắc lại:" $\hat q(s,a,w)$, dòng "Giả thiết:" Markov, hình vector đầu ra); phản ví dụ có số ở `L08-07b` (S12), hai bản sao ở `L08-07c` (S13) | chấp nhận; ví dụ số theo kế hoạch ($\theta_0=0\to0{,}5$, đích $1\to1{,}45$), không dùng ví dụ "đích tăng 0,72" của SV |
| trung bình | `L08-05` | "replay" dùng trước khi giới thiệu; 82 âm tiết; "sao lưu" là thuật ngữ mới (CT, SV) | Mặt trang | Phần khác chính sách sang `L08-05r` ở mạch 3; bỏ trang | trang đã bỏ ở S2; `L08-05r` thêm ở S20 (59 âm tiết, không dùng "replay", "sao lưu") | chấp nhận |
| trung bình | `L08-20`, `L08-31` | $[b,4,h,w]$ dùng trước khi có bốn khung; $h,w$ chưa định nghĩa (CT, SV, TH) | Thứ tự cũ | `L08-31` lên mạch 2; dòng "Nhắc lại:" bốn khung và định nghĩa $h,w$ ở `L08-20` | vị trí đã sửa ở C0; `L08-31` định nghĩa $4\times H\times W$ ở S9; dòng Nhắc lại ở `L08-20` mở | chấp nhận |
| trung bình | `L08-10`, `L08-15`, `L08-17` | Ba trang lặp hàm mất mát và hai đường tính; $L_B$ ở `L08-10` dùng $q_i,y_i$ trước định nghĩa (CT, SV, TH) | Mặt trang | `L08-17` lên đầu mạch 4; gộp `L08-15` vào `L08-10` | vị trí đã sửa ở C0; gộp mở | chấp nhận |
| trung bình | `L08-10` | $\operatorname{sg}$ và phép chọn theo hành động chưa định nghĩa trên mặt trang; chưa nối bán gradient Bài 07; ghi chú dẫn chiếu "đã giải thích ở phần trước" (CT, SV, TH) | Mặt trang và ghi chú | Dòng định nghĩa $\operatorname{sg}$; "Nhắc lại:" bán gradient | mở | chấp nhận |
| trung bình | `L08-16` | Trùng bước 9 của giả mã; trục SVG không nhãn; $\theta^-$ không vẽ dạng bậc thang (CT, SV, TH) | Mặt trang, ảnh SVG | Bỏ trang; hình vẽ lại sang `L08-07c`; thứ tự đồng bộ vào ghi chú `L08-19` | hình vẽ lại và dùng ở `L08-07c` (S13); bỏ trang và thứ tự đồng bộ ở ghi chú `L08-19` mở | chấp nhận |
| trung bình | `L08-12` | Tự đặt lại và quan sát cuối chỉ có trong ghi chú; "thường vẫn bootstrap" mơ hồ; không có ví dụ (CT, SV, TH) | Mặt trang | $U=1,Z=0$ vẫn bootstrap; đặt lại khi $Z\lor U$, mặt nạ chỉ $1-Z$; hình dòng thời gian; dòng tự đặt lại sang `L08-13` | đã sửa ở S16 (điều kiện $U=1,Z=0$, mặt nạ $1-Z$, đặt lại khi $Z\lor U$, hình `termination-truncation.svg`, ví dụ $4{,}6$ so với $1$); dòng tự đặt lại chuyển sang `L08-13` (đã thêm ở S19, dòng "Lưu ý:") | chấp nhận |
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
| trung bình | `L08-06` | Cảnh báo phủ định một cận mẫu chưa từng nêu (CT, SV) | Mặt trang | Bỏ trang; ý quy mô vào `L08-02c` và `L08-03` | đã sửa ở S6 (trang bỏ; ý chuyển sang `L08-03`, `L08-30`) | chấp nhận |
| trung bình | ví dụ | Không có ví dụ xuyên suốt; số của `L08-09` lặp ngầm ở `X01` (CT) | Mặt trang | "Mini-batch hai mẫu chuyển" với bảng cùng khuôn ở mỗi lần dùng | mẫu 2 dùng ở `L08-09` (S15) với chỉ số $t$, bảng một hàng cùng cột; các lần dùng ở mạch 4 và 6 mở | chấp nhận |
| trung bình | `L08-04`, `L08-08`, `L08-09` | $Z_{t+1}$ dùng trên mặt trang trước khi định nghĩa (TH, SV) | Mặt trang | Định nghĩa $Z$ ở `L08-08`; dòng Nhắc lại ở `L08-01b` không dùng $Z$ | `L08-04` đã bỏ ở S2, `L08-01b` không dùng $Z$; $Z_{t+1}$ định nghĩa bằng dòng "Ký hiệu:" ở `L08-08` (S14), `L08-09` dùng sau định nghĩa (S15) | chấp nhận |
| trung bình | `L08-08` | "Đồng bộ" dùng trước định nghĩa; câu mở kể tiến trình; ghi chú "đích không đổi ở mọi bước tối ưu" mâu thuẫn câu sau (CT, SV, TH) | Mặt trang và ghi chú | `L08-07c` định nghĩa đồng bộ trước `L08-08` | đồng bộ định nghĩa ở `L08-07c` (S13); câu mở kể tiến trình bỏ và ghi chú viết lại ở S14 | chấp nhận |
| trung bình | `L08-11` | Thiếu dòng Nhu cầu; SVG ghi $s'$, thiếu $\epsilon_{\mathrm{exp}}$-tham lam, cạnh không nhãn, chữ tràn hộp; ghi chú chỉ dẫn giảng viên (CT, SV, TH) | Ảnh SVG | "Nhu cầu:"; vẽ lại SVG | mở | chấp nhận |
| trung bình | `L08-11` | Đề xuất đưa vòng huấn luyện lên đầu mạch 2 làm bản đồ (SV) | Thứ tự cũ | — | đóng | bác bỏ: hình dùng bộ nhớ phát lại, mini-batch và mạng mục tiêu, các khái niệm chỉ có sau mạch 2–3; kế hoạch giữ `L08-11` mở cụm thuật toán ở mạch 4 với dòng "Nhu cầu:" |
| trung bình | `L08-14`, `L08-28` | Lặp nội dung tương quan; đề xuất gộp `L08-28` vào `L08-14` (SV) | Mặt trang | — | đóng | bác bỏ phần gộp: `L08-28` là trang vấn đề mở mạch 3, `L08-14` là trang giới hạn có Câu hỏi; phần lặp được cắt khi sửa từng trang |
| trung bình | `L08-23`, `L08-24`, `L08-25` | SGD chưa viết đầy đủ; $\odot,\oslash$ chưa định nghĩa; Adam không có câu giải thích (CT, SV, TH) | Mặt trang | "Ký hiệu:", "Ý nghĩa:" | mở | chấp nhận |
| trung bình | `L08-26` | Thiếu Ký hiệu $m_j,v_j$; câu giới hạn bộ tối ưu chỉ ở ghi chú; ghi chú có "Trang kế…", "Nhấn mạnh:" (CT, TH) | Mặt trang và ghi chú | Dòng Ký hiệu; câu kết bộ tối ưu không sửa đích, dữ liệu, xấp xỉ hàm | mở | chấp nhận |
| trung bình | ký hiệu | $m_j,v_j,\rho$ trùng $v_\pi$, $m=\lvert\mathcal A\rvert$, $\rho_t$ của Bài 07; $q_t,q_i$ trùng $q_\pi,q_*$; đề xuất đổi tên hoặc thêm Ký hiệu (TH) | Ghi chú Bài 07 | — | mở | chấp nhận dòng "Ký hiệu:" ($q_i$ ở mở bài và `L08-17`; $m_j,v_j,\rho$ ở mạch 5); bác bỏ đổi tên: $m_j,v_j,\rho$ là tên chuẩn của RMSprop và Adam (nguồn tr. 25–26), $q_i$ giữ theo `note-for-author.md` |
| trung bình | ghi chú bài giảng dòng 300 | "phá vỡ tương quan theo thời gian" mâu thuẫn dòng 324, 329 và `note-for-author.md` (TH, CT) | Ghi chú bài giảng | "giảm tương quan ngắn hạn" | đã sửa ở S19 (mục topic-06 viết lại, không còn câu "phá vỡ"; phát biểu phạm vi ở mục topic-07 sửa ở S21, viết "giảm" kèm xác suất $2/N>0$) | chấp nhận |
| trung bình | ghi chú bài giảng dòng 586 | "Đầu vào trạng thái: chồng bốn khung" (TH) | Ghi chú bài giảng | "quan sát; xấp xỉ trạng thái" | mở | chấp nhận |
| trung bình | ghi chú bài giảng, mục bảy mạch | Thứ tự chủ đề và thời lượng của bảy mạch trong ghi chú lệch deck (TH) | Ghi chú dòng 52–60 | Đồng bộ khi tới trang tiêu đề mạch tương ứng | `## 1.`, `## 2.` (S7), `## 3.` (S17), `## 4.` (S22) đã đồng bộ; phần 5–7 mở | chấp nhận |
| trung bình | SVG | Nhãn chồng nét, mũi tên che chữ, chữ tràn hộp; phông serif; cỡ nhãn khoảng 0,71 em ở bốn hình (SV, CT, TH) | Ảnh, `svgsize.py` | Vẽ lại theo mục A.8 của kế hoạch | mở | chấp nhận |
| trung bình | `L08-32` | 68 âm tiết; thẻ chung chung (SV, CT) | Đo mặt trang | Rút mỗi thẻ ≤ 15 âm tiết; Lời giải | nhãn "Lời giải:" thêm ở C0; đã sửa ở S11 (hai thẻ thay bằng hình `frame-stack-markov.svg`, 44 âm tiết) | chấp nhận |
| trung bình | `L08-28` | 64 âm tiết; "cỡ mẫu hiệu dụng" chưa định nghĩa; không có ví dụ; "mini-batch liên tiếp" mơ hồ (SV, CT, TH) | Đo mặt trang | Dòng "Muốn…"; ví dụ bốn mẫu liền nhau; hình dải quỹ đạo | đã sửa ở S18 (dòng "Nhu cầu:", Ví dụ cỡ mẫu hiệu dụng $\approx1{,}1$, hình `correlated-minibatch.svg`, 44 âm tiết) | chấp nhận |
| trung bình | `L08-13` | Mở bằng ký hiệu; $\mathcal D$ chưa định nghĩa; $\tau_k$ chưa giải thích; không nêu ghi đè; không có ví dụ (CT, SV, TH) | Mặt trang, SVG | "Nhu cầu:"; ví dụ $N=6$ | đã sửa ở S19 ("Nhu cầu:"; "Định nghĩa." $\mathcal D$; ghi đè mẫu cũ nhất; $b$ lần rút đều; ví dụ $N=6$ sau $8$ bước, xác suất $1/6$; hình vẽ lại không dùng $\tau_k$) | chấp nhận |
| trung bình | `L08-03` | Không có Nhu cầu và ví dụ số; SVG ghi "o hoặc s", $Q(s,a)$; ghi chú "trang này chốt…" (CT, SV, TH) | Mặt trang, SVG | Lunar Lander $9\,216$/$1\,896$ ô; sửa nhãn SVG | đã sửa ở S8 | chấp nhận |
| trung bình | `L08-17` | Hộp $Z/U$ lặp lần thứ ba; "$U_i$ điều khiển reset" sai trong batch (SV, CT, TH) | Mặt trang | Bỏ hộp; "Ký hiệu:" $q_i$ | mở | chấp nhận |
| nhẹ | tiêu đề | Tiêu đề ẩn dụ hoặc dạng câu (CT) | Mục 3 báo cáo CT | Tiêu đề mới theo `storyboard.md` | mở | chấp nhận |
| nhẹ | `no-ai-slop` | Tương phản nhị phân, colon reveal, siêu văn bản diễn giải, lời dẫn tiến trình, kết lặp lại (CT, SV) | `L08-05`, `L08-14`, `L08-31`, ghi chú `L08-07`, `L08-26`, `L08-27` | Viết thành mệnh đề khẳng định có điều kiện | `L08-05` bỏ ở S2; `L08-31` sửa ở S9; ghi chú `L08-07` sửa ở S10; còn lại mở | chấp nhận |
| nhẹ | nhiều trang | Dòng > 20 âm tiết; trang > 6 dòng (SV) | Bảng mật độ SV | Tách câu, gộp mục | mở | chấp nhận |
| nhẹ | 12 trang | Ghi chú diễn giả dưới 40 âm tiết (SV) | `notes.json` | Bổ sung giả thiết hoặc chỗ dễ nhầm | mở | chấp nhận |
| nhẹ | `L08-14` | Mẫu lấy đều có hoàn lại là i.i.d. theo phân phối của bộ đệm hiện tại; cái thiếu là một phân phối cố định (TH) | — | Dòng "Lưu ý:" | đã sửa ở S21: mục "Độc lập, cùng phân phối cố định." trên mặt trang (dòng "Lưu ý:" không còn chỗ); câu đầy đủ trong ghi chú diễn giả và Nhận xét 08.9 | chấp nhận |
| nhẹ | `L08-31` | SVG vẽ tiền xử lý sau bốn khung; đầu ra thiếu $\theta$, $o$; hai dòng chú thích đè nhau; CNN chưa viết đầy đủ; tương phản nhị phân (TH, SV, CT) | Ảnh SVG | Khung thô → tiền xử lý → xếp chồng bốn khung → mạng tích chập → $Q_\theta(O_t,a_k)$ | đã sửa ở S9 | chấp nhận |
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
- Bước S5 (`L08-02b`, biên tập viên): trang "Nội dung" sau `L08-02`: bảy mục trùng tên các mạch, mỗi mục liên kết `#/N` (đã thử bấm), dòng "Đọc trước:" Sutton và Barto (2018), §11.3, §16.5; Mnih và cộng sự (2015). 54 âm tiết, 8 dòng (ngoại lệ số dòng ghi trong storyboard). Ghi chú bài giảng: "Bảy phần của chương" thay danh sách mạch có thời lượng. Chờ điều phối viên duyệt.
| S5 | `L08-02b` | chấp nhận (ngoại lệ 8 dòng của trang Nội dung ghi trong storyboard) | diff; `check.py` |
- Bước S6 (`L08-02c`, biên tập viên): trang "Vấn đề trung tâm" sau `L08-02b`, xóa `L08-06`; hộp bài toán và năm dòng trả lời có điều kiện; 70 âm tiết (ngoại lệ ghi trong storyboard). Ghi chú diễn giả nêu bốn khó khăn của nguồn tr. 12 và lý do không trình bày hai cận độ phức tạp mẫu. Ghi chú bài giảng: mục "Bài toán trung tâm của chương" ở đầu Phần 2; đoạn độ phức tạp mẫu viết lại. Chờ điều phối viên duyệt.
| S6 | `L08-02c` (thay `L08-06`) | chấp nhận (ngoại lệ 70 âm tiết ghi trong storyboard); đã đối chiếu hai cận với nguồn tr. 9, 11 bằng `pdftotext` | diff; xem ảnh 1600 |
- Bước S7 (`L08-M2T`, biên tập viên): trang tiêu đề mạch 2 ở đầu section ngoài thứ 2, `id="mach-2"`; `#/2` và mục 2 của trang Nội dung mở đúng trang này. Ghi chú bài giảng: `## 1. Mở đầu` (bài toán trung tâm) và `## 2. Mạng giá trị hành động và đích hồi quy` với các mục con xếp theo thứ tự trang của mạch 2; hai mục Atari tách khỏi topic-15 thành `lec-08-topic-16` (trình xem từ chối mã chủ đề lặp), `L08-31`, `L08-32` đổi `data-note-topic-id` theo. Chờ điều phối viên duyệt.
| S7 | `L08-M2T` | chấp nhận; chấp nhận mã chủ đề mới `lec-08-topic-16` cho `L08-31`, `L08-32` (viewer không cho trùng mã) | diff; xem ảnh 1600; `#/2` mở đúng trang |
- Bước S8 (`L08-03`, biên tập viên): tiêu đề "Giới hạn của bảng giá trị hành động"; dòng "Muốn …", ví dụ Lunar Lander có số trên trang, $\lvert\mathcal S\rvert\lvert\mathcal A\rvert=9\,216\cdot4=36\,864$, trực giác; `table-vs-dqn.svg` vẽ lại. 51 âm tiết. Ghi chú bài giảng: mục cùng tên với Ví dụ 08.1 và hình. Chờ điều phối viên duyệt.
| S8 | `L08-03`, `table-vs-dqn.svg` | chấp nhận; chấp nhận cách tách $9\,216$ ô trạng thái và $36\,864$ ô bảng $Q$ (bốn hành động) | diff; tính lại số; xem ảnh 1600 |
- Bước S9 (`L08-31`, biên tập viên): tiêu đề "Ví dụ: đầu vào bốn khung Atari"; ba dòng theo nguồn tr. 35, $H\times W$ trên mặt trang, số của Mnih và cộng sự (2015) chỉ ở ghi chú có trích dẫn; `atari-pipeline.svg` vẽ lại đúng thứ tự tiền xử lý → xếp chồng, đầu ra $Q_\theta(O_t,a_k)$. 37 âm tiết. Ghi chú bài giảng: Ví dụ 08.2 và hình. Chờ điều phối viên duyệt.
| S9 | `L08-31`, `atari-pipeline.svg` | chấp nhận | diff; đối chiếu nguồn tr. 35; xem ảnh 1600 |

### Rà lại mạch 1 (bước R1)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 1 (toán, mạch, mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R1 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 5 trung bình, 9 nhẹ; điều phối viên chấp nhận toàn bộ và thêm mục 15 (dòng 2 của `L08-02c`), đã kiểm định nghĩa $\epsilon$-tối ưu ở nguồn tr. 8 bằng `pdftotext`. Bảng dưới ghi quyết định đã duyệt (tệp `recheck/R1-decisions.md` trong scratchpad phiên) và trạng thái sau bước R1.

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|---|
| trung bình | `L08-02c`, `L08-03`, ghi chú bài giảng §1 | "Quan sát là ảnh" quá hẹp: Lunar Lander, CartPole có quan sát là vector | Ví dụ 08.1; notebook Bài 04, 06 | "vector liên tục hoặc ảnh" ở hộp bài toán, dòng mở `L08-03` và §1 | đã sửa ở R1 | chấp nhận |
| trung bình | `L08-02c` dòng 5, ghi chú `L08-02`, ghi chú bài giảng §1 mục 5 và mục tiêu 4 | "Bộ tối ưu không sửa đích hay dữ liệu" sai: bộ tối ưu đổi quỹ đạo $\theta$, do đó đổi dữ liệu và $\theta^-$ | Vòng DQN: hành vi và đồng bộ dùng $\theta$ | "Bộ tối ưu không loại được nguồn bất ổn ở đích, dữ liệu, lớp hàm"; công thức đích, cơ chế thu thập dữ liệu và lớp hàm không phụ thuộc lựa chọn bộ tối ưu | đã sửa ở R1; áp dụng tiếp cho `L08-22`, `L08-26` | chấp nhận |
| trung bình | ghi chú `L08-02c`, ghi chú bài giảng §1, `note-for-author.md` | Lý do bác hai cận tr. 9, 11 sai một phần: nguồn có chuẩn sai số (tr. 8) và có thuật toán cho cận thứ nhất (tr. 9) | Nguồn tr. 8–11 | Lý do: thiếu mô hình lấy mẫu và xác suất thành công, chỉ nêu định tính điều kiện khám phá; cận thứ hai không gắn thuật toán cụ thể | đã sửa ở R1 (cả câu tương ứng trong `note-for-author.md`) | chấp nhận |
| trung bình | `L08-01b2` | Thiếu giả thiết "mẫu sinh từ chính MDP" của Định lý 06.21 | Ghi chú Bài 06, Nhận xét 06.20, Định lý 06.21 | Thêm vào dòng giả thiết; viết Robbins–Monro bằng hai tổng | đã sửa ở R1 | chấp nhận |
| trung bình | ghi chú `L08-02c` → `L08-17` | Ghi chú hứa phần 4–5 xử lý khó khăn không lồi nhưng chưa trang nào nói | Ghi chú `L08-02c` | Thêm dòng "Lưu ý: $L_B$ vẫn không lồi theo $\theta$…" ở `L08-17` | mở (ghi trong storyboard, làm ở bước `L08-17`) | chấp nhận |
| nhẹ | ghi chú bài giảng, ghi chú `L08-01b2`, `L08-01c` | Tài liệu làm chủ ngữ ("Chương này…", "Bài dùng…", "Bài 08 chỉ dùng…") | Các câu đã trích trong quyết định | Viết lại với "chúng ta", "ta" hoặc chủ ngữ là đối tượng | đã sửa ở R1 (thêm "chương này gọi là quan sát" ở mục Atari) | chấp nhận |
| nhẹ | `L08-01b` | Công thức dùng $\leftarrow$ trong khi mặt trang Bài 06 dùng chỉ số $Q_t$, $Q_{t+1}$ | Định nghĩa 06.15 | $Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t[\dots]$ | đã sửa ở R1 (vừa khung 16:9) | chấp nhận |
| nhẹ | `L08-01b` | Thiếu tên tiếng Anh "off-policy", "importance sampling ratio"; dòng lý do chưa nói "đối số của ô cập nhật" | Mặt trang | Câu đã duyệt | đã sửa ở R1 (bỏ "dữ liệu theo" ở dòng trên để giữ ≤ 60) | chấp nhận |
| nhẹ | `L08-01b2` | Dòng mạng chưa nói "khả vi" | Mặt trang | "mạng nhiều tầng, mạng tích chập (CNN) khả vi theo $\theta$; lan truyền ngược tính gradient" nếu trang ≤ 60 | sửa một phần: câu đề xuất làm trang vượt 60 nên giữ câu cũ (bỏ "(MLP)"), ý khả vi nằm trong ghi chú diễn giả | chấp nhận |
| nhẹ | ghi chú `L08-01b2` | Vai của $\gamma<1$ và phần thưởng bị chặn chưa tách | Ghi chú | "$\gamma<1$ làm toán tử Bellman tối ưu co theo chuẩn cực đại; phần thưởng bị chặn giữ mọi giá trị hữu hạn" | đã sửa ở R1 (thêm vai của "mẫu từ chính MDP") | chấp nhận |
| nhẹ | ghi chú `L08-01`, ghi chú bài giảng §1 mục 6 | "Mọi kết luận… dựa trên thí nghiệm" quá tuyệt đối | — | "các kết luận về hiệu quả của DQN gốc chủ yếu dựa trên thí nghiệm" | đã sửa ở R1 | chấp nhận |
| nhẹ | `L08-01c` | $b$ chưa được gọi tên | Mặt trang | "mini-batch cỡ $b$" | đã sửa ở R1 | chấp nhận |
| nhẹ | `L08-02`, ghi chú `L08-02`, ghi chú bài giảng | "Độ nhảy" là từ khẩu ngữ; ghi chú dùng "mạch" (nhãn quy trình) | Mặt trang và ghi chú | "độ thay đổi"; "các phần 2 đến 7" | đã sửa ở R1; áp dụng cho `L08-29` | chấp nhận |
| nhẹ | `L08-01`, `L08-02`, `L08-02b`, `L08-02c` | Bốn trang mở bài gắn `lec-08-topic-01` (chủ đề "Giới hạn của bảng") | `data-note-topic-id` | Chủ đề mới `lec-08-topic-17` cho phần mở đầu; topic-01 giữ cho `L08-M2T`, `L08-03` | đã sửa ở R1 (deck, ghi chú bài giảng, bản đồ chủ đề, `outline.md`) | chấp nhận |
| nhẹ | `L08-02c` | Dòng 2 "bản sao mạng cố định" bỏ qua việc đồng bộ; các dòng "X: Y" chưa là câu điều kiện | Mặt trang | "đích từ bản sao đồng bộ định kỳ"; dòng 3, 4, 6 mở bằng "Khi …" | đã sửa ở R1 (ngoại lệ mật độ 85 âm tiết ghi trong storyboard) | chấp nhận (mục do điều phối viên thêm) |

- Bước R1 (biên tập viên): áp dụng 15 mục; mục 5 chỉ ghi kế hoạch; mục 9 sửa một phần (lý do ở bảng). Số đo mật độ mới và ngoại lệ (`L08-01` hộp luận đề một câu; `L08-02b` 8 dòng; `L08-02c` 85 âm tiết) ghi trong `storyboard.md`, mục "Rà lại mạch 1 (bước R1)" và "Ngoại lệ mật độ". Chờ điều phối viên duyệt.
| R1 | mạch 1 (rà lại) | chấp nhận; `L08-02c` 84–85 âm tiết (< 1,5 × trần) giữ với ngoại lệ ghi trong storyboard vì sáu dòng đều là câu trả lời có điều kiện | diff; `check.py` mạch 1; xem ảnh |
- Bước S10 (`L08-07`, biên tập viên): tiêu đề "Mạng giá trị hành động"; chỉ giữ giao diện: dòng "Nhắc lại:" $\hat q(s,a,w)=x(s,a)^\top w$, "Định nghĩa." $\mathbf q_\theta:\mathcal O\to\mathbb R^{\lvert\mathcal A\rvert}$, $Q_\theta(o,a)=[\mathbf q_\theta(o)]_a$, hình mới `q-vector.svg` (ô lớn nhất đánh dấu bằng viền kép và tam giác), dòng "$\max_a$ cho mục tiêu; $\arg\max_a$ cho hành động tham lam", dòng "Giả thiết:" $O_t$ đủ Markov. Hai thẻ "Phản ví dụ một mạng", "Tách hai bản sao" bỏ khỏi trang, chuyển sang `L08-07b`, `L08-07c`. 51 âm tiết, 4 dòng, đáy 666 px. Theo yêu cầu sửa của điều phối viên: dòng 3 rút còn "$\max_a$ cho mục tiêu; $\arg\max_a$ cho hành động tham lam." (bỏ ý một lần tính lặp nhãn hình và chữ "lam." lẻ dòng). Ghi chú bài giảng: mục "Mạng giá trị hành động" với Định nghĩa 08.1, Nhận xét 08.2, Ví dụ 08.3 và hình; phần hai mạng chuyển thành mục tạm "Đích di động và mạng mục tiêu" sau "Bốn khung và tính Markov". `no-ai-slop` Edit trên mặt trang, ghi chú diễn giả và mục ghi chú bài giảng mới, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S10 | `L08-07`, `q-vector.svg` (mới) | yêu cầu sửa (dòng 3 lặp nhãn hình, chữ lẻ dòng), rồi chấp nhận | diff; tính lại xác suất $\epsilon$-tham lam trong note; xem ảnh 1600 |
- Bước S11 (`L08-32`, biên tập viên): tiêu đề "Bốn khung và tính Markov"; hai thẻ chữ thay bằng hình mới `frame-stack-markov.svg` (một khung: biết vị trí, hai hướng có dấu hỏi; bốn khung: bốn vị trí cách đều, ba vòng rỗng nét đứt và một chấm đặc, mũi tên hướng); một dòng tự đủ nghĩa nêu điều kiện Markov của $O_t$; "Câu hỏi:" và "Lời giải:" (`.fragment`). 44 âm tiết (trước 68), 3 dòng, đáy 647 px. Ghi chú bài giảng: mục "Bốn khung và tính Markov" viết lại với Ví dụ 08.4 (tọa độ quả bóng, vận tốc $(4,-3)$, vị trí dự đoán $(26,28)$), hình và đoạn đọc hình, ba loại thông tin bốn khung có thể thiếu, "Trong thực hành.", kiểm tra nhanh; bỏ câu về đặc tả tái lập (trùng mục Atari) và câu lấy tài liệu làm chủ ngữ. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S11 | `L08-32`, `frame-stack-markov.svg` (mới) | chấp nhận; còn mở (nhẹ): nhãn $t-3$, $t-1$ chạm vòng tròn trong hình, sửa ở lượt rà cuối | diff; xem ảnh 1600; kiểm số Ví dụ 08.4 |
- Bước S12 (`L08-07b`, biên tập viên): trang mới "Ví dụ: một tham số tạo cả dự đoán lẫn đích" sau `L08-32` (topic-02): $Q_\theta=\theta$, $R_{t+1}=1$, $\gamma=0{,}9$, $\theta_0=0$, $\alpha=0{,}5$; $q=0$, $y=1$; $\theta_1=0{,}5$; đích mới $1{,}45$; "Diễn giải:" sai số $0{,}95$ so với $0{,}5$ khi đích đứng yên. Hình mới `moving-target-step.svg`. 27 âm tiết, 6 dòng, 1 công thức hiển thị, đáy 698 px. Đóng một phần phát hiện `L08-07` (phản ví dụ có số); `L08-07c` còn mở. Ghi chú bài giảng: Ví dụ 08.5, hình, đoạn dãy lặp và Mệnh đề 07.37 trong mục tạm "Đích di động và mạng mục tiêu". `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S12 | `L08-07b` (mới), `moving-target-step.svg` (mới) | chấp nhận; đáy 698 px giữ; quy tắc chung `min-width: 900px` của `material-viewer.css` làm hình nhỏ bị phóng trong viewer — hạ tầng dùng chung, không sửa trong đợt này, báo người dùng | diff; tính lại dãy $\theta_{n+1}=0{,}95\theta_n+0{,}5$; xem ảnh 1600 |
- Bước S13 (`L08-07c`, biên tập viên): trang mới "Mạng mục tiêu" sau `L08-07b` (topic-02): "Nhu cầu:" đích tính bằng $\theta$ đổi $1\to1{,}45$; "Định nghĩa." $Q_{\theta^-}$ cùng kiến trúc với mạng trực tuyến (online network), chỉ tính đích, không nhận gradient; khởi tạo $\theta^-\leftarrow\theta$, đồng bộ khi $k_{\mathrm{opt}}\bmod C=0$ sau bước tối ưu; hình `target-network-timeline.svg` vẽ lại (trục $k_{\mathrm{opt}}$, $\theta^-$ bậc thang); "Diễn giải:" đích $1$ trong $C$ bước khi $\theta^-=0$. 51 âm tiết, 4 dòng, đáy 687 px. Ghi chú diễn giả: không bảo đảm hội tụ. Ghi chú bài giảng: mục tạm tách thành "Một tham số tạo cả dự đoán lẫn đích" và "Mạng mục tiêu" (Định nghĩa 08.3, vai của từng điều kiện, Ví dụ 08.6, so sánh tốc độ cho thấy mạng mục tiêu không làm ví dụ một tham số nhanh hơn, "Trong thực hành." với nguồn Mnih và cộng sự 2015 và Lillicrap và cộng sự 2016). `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S13 | `L08-07c` (mới), `target-network-timeline.svg` (vẽ lại) | chấp nhận; giữ đoạn so sánh tốc độ trung thực trong note (đã tính lại hệ số $0{,}9+0{,}1\cdot0{,}5^C$, $C=3$: $0{,}9125$ so với $0{,}95^3$); hình là sơ đồ hai làn, mũi tên nét đứt chỉ phép sao chép | diff; tính lại Ví dụ 08.6; xem ảnh 1600 |
- Bước S14 (`L08-08`, biên tập viên): tiêu đề "Đích hồi quy"; dòng "Ký hiệu:" định nghĩa $Z_{t+1}\in\{0,1\}$ trước khi dùng; "Định nghĩa." đích hồi quy (còn gọi là mục tiêu cập nhật) của mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1})$; công thức $y_t$ hiển thị; dự đoán $q_t$, sai số sai phân thời gian (sai số TD) $\delta_t$; dòng hồi quy $q_t$ về $y_t$ khi $\theta^-$ cố định. Bỏ câu kể tiến trình "Sau khi khởi tạo hai mạng…" và "mạng online". 53 âm tiết (trước 28), 4 dòng, đáy 619 px. Ghi chú diễn giả: đích là ước lượng, cố định trong $C$ bước; $Z$ khác cờ cắt ngắn. Ghi chú bài giảng: mục topic-03 viết lại thành "Đích hồi quy" (Định nghĩa 08.4, đoạn đọc, vai của từng điều kiện, nối với hồi quy có giám sát và bước hạ gradient của dạng bảng, Nhận xét 08.5 về kỳ vọng có điều kiện $\mathcal TQ_{\theta^-}$, "Trong thực hành."); bỏ "Kiểm tra nhanh" trùng. Nhận xét 08.5 đáp một phần gợi ý "lặp Q có khớp" (hàng nhẹ ở trên) mà không dẫn Riedmiller (2005); chờ điều phối viên quyết. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S14 | `L08-08` | chấp nhận; giữ Nhận xét 08.5 (kỳ vọng có điều kiện cực tiểu sai số bình phương, có giả thiết, không suy ra hội tụ), không cần trích Riedmiller | diff; xem ảnh 1600 |
- Bước S15 (`L08-09`, biên tập viên): tiêu đề "Ví dụ: đích tại mẫu chuyển kết thúc"; mẫu 2 của ví dụ xuyên suốt "mini-batch hai mẫu chuyển" viết theo chỉ số thời gian $t$ (chỉ số mẫu $i$ giới thiệu ở mạch 4) trong bảng một hàng `R_{t+1} | Z_{t+1} | max_{a'} Q_{θ⁻}(O_{t+1},a') | q_t` ($-2$, $1$, $100$, $-1{,}5$); tính $y_t=-2$, $\delta_t=-0{,}5$; "Câu hỏi:" bỏ mặt nạ; "Lời giải:" $y_t=88$, $\delta_t=89{,}5$; "Diễn giải:" lệch $90$, $\delta_t$ đổi dấu. 41 âm tiết (trước 8 + hộp, trang cũ không có $q_t$, $\delta_t$), 6 dòng và bảng một hàng, đáy 691 px. Ghi chú bài giảng: mục topic-04 viết lại với Ví dụ 08.7 (bảng, tính có và không có mặt nạ, diễn giải), đoạn quy ước $Q(s,\cdot)=0$, đoạn lỗi lan ngược và cờ gộp, "Trong thực hành."; bỏ khối Vấn đề/Trực giác/Hình thức/Kiểm tra nhanh cũ và chữ `done`. Sửa thêm ở mục topic-03 (bước S14): công thức của Nhận xét 08.5 tràn khung trong viewer, chuyển sang `aligned` hai dòng. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S15 | `L08-09` | chấp nhận; hàng bảng tính là dòng dữ liệu (trang 6 dòng chữ + 1 hàng bảng, 41 âm tiết, vừa khung) — ghi ngoại lệ dòng ở storyboard trong bước kế; "Diễn giải:" là fragment: chấp nhận | diff; tính lại $-2$, $-0{,}5$, $88$, $89{,}5$; xem ảnh 1600 |
- Bước S16 (`L08-12`, biên tập viên): tiêu đề "Kết thúc và cắt ngắn" (trang cuối mạch 2); "Ký hiệu:" $U_{t+1}$; bộ sáu thành phần; hình mới `termination-truncation.svg` (hai nhánh $Z=1$ và $U=1,Z=0$ với đích tương ứng, phân biệt bằng viền liền và nét đứt); dòng mặt nạ chỉ $1-Z$, đặt lại khi $Z\lor U$; "Ví dụ." mẫu 1 của ví dụ xuyên suốt bị cắt ngắn: $y_t=4{,}6$, mặt nạ gộp cho sai $y_t=1$. 36 âm tiết (trước 31), 5 dòng, đáy 693 px. Dòng tự đặt lại bỏ khỏi trang, chuyển sang `L08-13`; trong ghi chú bài giảng đoạn tự đặt lại chuyển lên đầu mục bộ nhớ phát lại (topic-06), bỏ tên trường API. Ghi chú bài giảng: mục topic-05 viết lại thành "Kết thúc và cắt ngắn" (Định nghĩa 08.6, đoạn vai hai cờ, hình, Ví dụ 08.8, giả thiết giới hạn không thuộc nhiệm vụ theo Pardo và cộng sự 2018, "Trong thực hành."), đoạn kết phần 2 bằng văn xuôi. Ngoại lệ mật độ `L08-09` ghi vào storyboard. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S16 | `L08-12`, `termination-truncation.svg` (mới) | chấp nhận; Pardo và cộng sự (2018) vào tài liệu tham khảo ở mạch 7 | diff; xem ảnh 1600 |
- Bước S17 (`L08-M3T`, biên tập viên): trang tiêu đề mạch 3 ở đầu section ngoài thứ 3, `id="mach-3"`, khuôn `L08-M2T`: "3. Bộ nhớ phát lại"; dòng dẫn "Muốn mini-batch ít tương quan, phải lưu mẫu chuyển rồi lấy mẫu đều từ bộ nhớ." (17 âm tiết); bốn cụm từ khóa; ghi chú diễn giả 83 âm tiết. `#/3` và mục 3 của `L08-02b` mở đúng trang (hash `#/mach-3`). Chủ đề mới `lec-08-topic-18` cho `L08-M3T` và `L08-28` (tương quan giữa các mẫu chuyển), vì `L08-28` và `L08-14` trước đây cùng topic-07 nên không xếp được mục ghi chú theo thứ tự trang (viewer không cho trùng mã). Ghi chú bài giảng: `## 3. Bộ nhớ phát lại` với bốn mục theo thứ tự trang (topic-18 tách từ đoạn Vấn đề/Trực giác của topic-07; topic-06; mục "Dữ liệu khác chính sách trong bộ nhớ" tách từ topic-06; topic-07 đổi tên "Giới hạn của bộ nhớ phát lại"), nội dung chưa viết lại; phần còn lại dưới tiêu đề tạm "## Hàm mất mát, vòng huấn luyện và bất ổn". `outline.md`: bảng ánh xạ thêm topic-18, sửa topic-02 (`L08-07`, `L08-07b`, `L08-07c`) và topic-07. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S17 | `L08-M3T` | chấp nhận; chấp nhận mã chủ đề `lec-08-topic-18` và bổ sung ánh xạ `L08-07b`, `L08-07c` trong outline | diff; `check.py` |
- Bước S18 (`L08-28`, biên tập viên): tiêu đề "Tương quan giữa các mẫu chuyển liên tiếp"; "Nhu cầu:" $b$ mẫu gần độc lập để gradient mini-batch giảm phương sai; hình mới `correlated-minibatch.svg` (bốn mẫu liên tiếp, hình vuông đặc, so với bốn mẫu rải, tam giác đặc); "Ví dụ." bốn gradient mẫu, phương sai $\sigma^2$, tương quan $0{,}9^k$ (giả thiết minh họa): $\operatorname{Var}\bar g\approx0{,}881\,\sigma^2$ so với $0{,}25\,\sigma^2$, cỡ mẫu hiệu dụng $\approx1{,}1$; dòng gradient dao động theo đoạn quỹ đạo gần nhất. 44 âm tiết (trước 64), 4 dòng, đáy 656 px. Ghi chú diễn giả: phép tính phương sai, giả thiết minh họa, tương quan không nhất thiết làm chệch, ý quá khớp/quên của nguồn tr. 30. Ghi chú bài giảng: mục topic-18 viết lại (nhu cầu nối SGD và giả thiết i.i.d., trực giác, Ví dụ 08.9, hình và đoạn đọc hình, không i.i.d. ngay cả khi lấy rải, "Trong thực hành.", đoạn nối sang bộ nhớ). `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S18 | `L08-28`, `correlated-minibatch.svg` (mới) | chấp nhận; mô hình tương quan $0{,}9^k$ là dữ liệu của ví dụ, ghi rõ là giả thiết minh họa trong ghi chú và note | diff; tính lại $14{,}098/16\approx0{,}881$; `check.py` |
- Bước S19 (`L08-13`, biên tập viên): tiêu đề "Bộ nhớ phát lại"; "Nhu cầu:" mẫu rải trên dòng thời gian; "Định nghĩa." $\mathcal D$ là bộ đệm vòng chứa $N$ mẫu chuyển; đầy thì ghi đè mẫu cũ nhất, mini-batch gồm $b$ lần rút đều; hình `replay-buffer.svg` vẽ lại ($N=6$ sau $8$ bước: mẫu $7,8,3,4,5,6$, con trỏ ghi ở mẫu $3$, hai vị trí được rút); "Ví dụ." mỗi lần rút chọn mỗi mẫu $3,\dots,8$ với xác suất $1/6$; "Lưu ý:" lưu quan sát cuối lượt làm $O_{t+1}$ khi môi trường tự đặt lại, không nêu tên trường API. 60 âm tiết (trước 35), 5 dòng, đáy 699 px. Ghi chú diễn giả: vị trí $((k-1)\bmod N)+1$, rút có hoặc không hoàn lại, $N=10^6$, $b=32$ (Mnih và cộng sự, 2015), tên trường phụ thuộc phiên bản API, hệ quả lưu nhầm với mẫu bị cắt ngắn; bỏ lý do sai về tỉ số lấy mẫu quan trọng. Ghi chú bài giảng: mục topic-06 viết lại (Định nghĩa 08.7, vai của ba quy tắc có phản ví dụ, Ví dụ 08.10, hình, môi trường tự đặt lại, "Trong thực hành.", kiểm tra nhanh, đoạn kết). `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.

### Rà lại mạch 2 (bước R2)

| vai | loại tác tử | mô hình | mức suy luận | ghi tệp |
|---|---|---|---|---|
| Rà lại mạch 2 (toán, mạch, mật độ, `no-ai-slop` Detect) | Agent `general-purpose` | `claude-opus-5-5` | high | không |
| Biên tập R2 | Agent `general-purpose` (biên tập viên của đợt sửa) | `claude-opus-5-5` | high | có |

Kết quả rà: 0 chặn bàn giao, 0 nghiêm trọng, 5 trung bình, 16 nhẹ; điều phối viên chấp nhận toàn bộ (tệp `recheck/R2-decisions.md` trong scratchpad phiên). Bảng dưới ghi trạng thái sau bước R2.

| mức độ | trang chiếu | vấn đề | đề xuất sửa | trạng thái | quyết định |
|---|---|---|---|---|---|
| trung bình (TB1) | `L08-07b`, ghi chú `L08-07c`, ghi chú bài giảng | Ví dụ một tham số ngụ ý đích đứng yên "tốt hơn"; thực tế mạng mục tiêu không đưa $\theta$ tới $10$ nhanh hơn | Nói trung thực tốc độ ($0{,}9125$ so với $0{,}95^3\approx0{,}857$); "Diễn giải:" trung tính; câu nhu cầu "tách tham số tạo đích khỏi tham số được cập nhật" | đã sửa ở R2 (cả câu "đích di động chỉ làm chậm" trong ghi chú bài giảng) | chấp nhận |
| trung bình (TB2) | `L08-07`, `L08-32` | Dòng "Giả thiết:" Markov đặt ở `L08-07` trước khi có ví dụ; `L08-32` định nghĩa lại | Bỏ khỏi `L08-07`; `L08-32` dùng câu "Giả thiết:" đầy đủ | đã sửa ở R2 | chấp nhận |
| trung bình (TB3) | `L08-07b`, `L08-07`, `L08-08` | "Đích" dùng ở `L08-07b` trước cụm "còn gọi là mục tiêu cập nhật" ở `L08-08`; dễ lẫn với "chính sách đích" | Cụm "còn gọi là" ở lần dùng đầu (`L08-07b`); bỏ ở `L08-08`; ghi chú `L08-08` phân biệt với chính sách đích | đã sửa ở R2 (bỏ "Bài 06" trong ngoặc trên mặt trang `L08-07b` để không xuống dòng) | chấp nhận |
| trung bình (TB4) | `L08-12` | Một trang chứa định nghĩa, hình và ví dụ; ví dụ cắt ngắn không có câu hỏi kiểm tra | Tách `L08-12` (Nhu cầu, Ký hiệu, hình, quy tắc mặt nạ) và trang mới `L08-12b` (ví dụ, Câu hỏi, Lời giải, Diễn giải) | đã sửa ở R2 (dòng "Nhu cầu:" rút "cho phép", "khác nhau" để ≤ 20 âm tiết; bộ sáu gộp vào dòng "Ký hiệu:") | chấp nhận |
| trung bình (TB5) | `L08-08` | Dòng "Ký hiệu:" $Z$ không nêu nhu cầu; dòng cuối dài | "Nhu cầu:" mạng không có ô $Q(s,\cdot)=0$; cờ $Z_{t+1}$; dòng cuối rút gọn | đã sửa ở R2 (tách thành hai dòng để mỗi dòng ≤ 20 âm tiết) | chấp nhận |
| nhẹ (1) | `L08-03` và các trang khác | Nhãn "Trực giác." không có trong danh sách nhãn | "Trực quan." | đã sửa ở R2 (deck và ghi chú bài giảng) | chấp nhận |
| nhẹ (2) | `L08-03` | Ví dụ thiếu nguồn bài và số hành động | "Lunar Lander rời rạc hóa (Bài 07)"; "Bảng $Q$ với $4$ hành động" | đã sửa ở R2 ("sau $2\,000$ lượt" chuyển vào ghi chú diễn giả để dòng không xuống dòng) | chấp nhận |
| nhẹ (3) | `L08-31` | Ví dụ thiếu số cụ thể | $H=W=84$, $28\,224$ số; $4$ đến $18$ hành động; nguồn trong ghi chú | đã sửa ở R2 (hình giữ $4\times H\times W$) | chấp nhận |
| nhẹ (4) | `L08-20` | Ký hiệu kích thước | Dùng $[b,4,H,W]$ | ghi nhớ trong storyboard (hàng `L08-20`); làm ở bước `L08-20` | chấp nhận |
| nhẹ (5) | `L08-32` | Định nghĩa Markov không gắn nhãn "Giả thiết:" | Gộp vào TB2 | đã sửa ở R2 | chấp nhận |
| nhẹ (6) | `frame-stack-markov.svg` | Nhãn $t-3$, $t-1$ chạm vòng tròn | Dời nhãn | đã sửa ở R2 (nhãn đặt phía trên vòng tròn) | chấp nhận |
| nhẹ (7) | `target-network-timeline.svg` | Đoạn $\theta^-$ không bằng $\theta$ tại mốc đồng bộ | Vẽ $\theta^-$ bằng giá trị $\theta$ tại $0$, $C$, $2C$ | đã sửa ở R2 (vẽ lại trên một trục giá trị; chú giải vòng tròn rỗng; alt và đoạn đọc hình trong ghi chú bài giảng cập nhật; `L08-16` dùng cùng hình, vẫn hiển thị đúng) | chấp nhận |
| nhẹ (8) | `L08-07c` | $C$ chưa có miền; thiếu câu về $C=1$ | "($C\in\mathbb N_+$)"; ghi chú thêm $C=1$ | đã sửa ở R2 | chấp nhận |
| nhẹ (9) | `L08-07b`, bảng ký hiệu ghi chú bài giảng | Hai dòng tính có thể gộp; $\alpha$ và $\eta$ | Gộp dòng; câu $\alpha$/$\eta$ | câu $\alpha$/$\eta$ đã thêm; gộp dòng thử rồi bỏ vì cột hẹp làm ngắt giữa công thức (đáy vẫn 698 px) | chấp nhận một phần |
| nhẹ (10) | `L08-12` | Ví dụ cắt ngắn | Xử lý trong TB4 | đã sửa ở R2 | chấp nhận |
| nhẹ (11) | ghi chú `L08-08` | "$y_t$ là ước lượng của $q_*$" không chính xác | Mẫu có kỳ vọng $(\mathcal TQ_{\theta^-})(O_t,A_t)$; $q_t$ khác $q_*$ | đã sửa ở R2 | chấp nhận |
| nhẹ (12) | ghi chú bài giảng, Định nghĩa 08.4 | Vai của $\gamma<1$ | "cùng phần thưởng bị chặn giữ $q_*$ hữu hạn" | đã sửa ở R2 | chấp nhận |
| nhẹ (13) | ghi chú bài giảng, đoạn hồi quy | Đạo hàm chưa nêu $y_t$ coi là hằng | "khi coi $y_t$ là hằng" | đã sửa ở R2 | chấp nhận |
| nhẹ (14) | ghi chú `L08-07` | Thiếu xác suất $\epsilon_{\mathrm{exp}}$-tham lam | $0{,}925$, $0{,}025$ | đã sửa ở R2 | chấp nhận |
| nhẹ (15) | ghi chú bài giảng, Ví dụ 08.1 | "lượt huấn luyện" sai bản chất dữ liệu | "lượt của một chính sách cố định" | đã sửa ở R2 (cả ghi chú diễn giả `L08-03`) | chấp nhận |
| nhẹ (16) | ghi chú bài giảng, ghi chú `L08-M2T`, `L08-M3T` | "Phần N" làm chủ ngữ | Viết lại với "chúng ta" hoặc bị động | đã sửa ở R2 (thêm "Mục tiếp theo …", "mục kế tiếp tính …", "Ví dụ 08.7 dưới đây tính …"); ghi chú `L08-02b` (mạch 1) còn "Phần 2 thay bảng…", ngoài phạm vi R2 | chấp nhận |

- Bước R2 (biên tập viên): áp dụng TB1–TB5 và nhẹ 1–16; trang mới `L08-12b` (topic-05; `outline.md` cập nhật ánh xạ). Hai hình vẽ lại hoặc sửa: `target-network-timeline.svg` (một trục giá trị, $\theta^-$ bằng $\theta$ tại mốc đồng bộ), `frame-stack-markov.svg` (nhãn thời điểm). Nhẹ 9 chấp nhận một phần (lý do ở bảng). Số đo trước/sau trong `storyboard.md`, mục "Rà lại mạch 2 (bước R2)"; ngoại lệ `L08-12b` và dòng "Giả thiết:" của `L08-32` ghi ở mục "Ngoại lệ mật độ". `check.py` mạch 2 và `L08-M3T` ở 1600×900, 390×844: không tràn, không lỗi; viewer 826 KaTeX, 0 lỗi. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| R2 | mạch 2 (rà lại), `L08-12b` (mới) | chấp nhận; câu duyệt bị rút vài chữ để vừa dòng: chấp nhận; nút điều hướng trên đè tiêu đề dài là hành vi chung của Reveal, không sửa; ghi chú `L08-02b` ("Phần 2 …" làm chủ ngữ) sửa ở lượt rà cuối | diff; `check.py`; xem ảnh `L08-07c`, `L08-12b` |
| S19 | `L08-13`, `replay-buffer.svg` (vẽ lại) | chấp nhận cả năm đề xuất (vế "không lưu quan sát đầu lượt mới" ở ghi chú; "Nhu cầu:" ngắn; bỏ "tối đa"; `note-for-author.md` dòng 15 sửa ở bước `L08-05r`; độ rộng hình trong viewer là quy tắc CSS dùng chung, báo người dùng) | diff; tính lại $56\,448$ số/mẫu; xem ảnh 1600 |
- Bước S20 (`L08-05r`, biên tập viên): trang mới "Dữ liệu khác chính sách trong bộ nhớ" sau `L08-13`, topic mới `lec-08-topic-19`; hai nguồn khác chính sách (hành vi $\epsilon_{\mathrm{exp}}$-tham lam; $\mathcal D$ giữ mẫu của các phiên bản $\theta$ cũ); hình mới `offpolicy-replay.svg`; lý do không cần tỉ số lấy mẫu quan trọng: $A_i$ là đối số điều kiện của $Q_\theta(O_i,A_i)$, tại $O'_i$ phép cực đại được tính trọn; dòng kết: phân phối mẫu của $\mathcal D$ do các hành vi cũ và hiện tại quyết định. 59 âm tiết, đáy 686 px, ghi chú diễn giả 143 âm tiết. Ghi chú bài giảng: mục viết lại với Mệnh đề 08.8 (và chứng minh), Ví dụ 08.11, "Trong thực hành.", kiểm tra nhanh, đoạn kết. `note-for-author.md` dòng 15 sửa lý do. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S20 | `L08-05r` (mới), `offpolicy-replay.svg` (mới) | chấp nhận cả ba đề xuất (dòng dẫn thay "Nhu cầu:"; bước 2 chứng minh giữ ngắn; giữ Mệnh đề 08.8); đã đọc sửa `note-for-author.md` dòng 15 | diff; kiểm $2{,}5\cdot10^5$ bước tối ưu (Mnih 2015: $N=10^6$, cập nhật mỗi 4 bước); xem ảnh 1600 |
- Bước S21 (`L08-14`, biên tập viên): tiêu đề "Giới hạn của bộ nhớ phát lại" (trang cuối mạch 3); hai cột gọn "Làm được" (giảm tương quan ngắn hạn, tái sử dụng mẫu, trộn nhiều đoạn quỹ đạo) / "Không bảo đảm" (độc lập, cùng phân phối cố định; phân phối $\mathcal D$ đứng yên; hội tụ); "Câu hỏi:" $N=6$, $\mathcal D$ chứa mẫu $3,\dots,8$, rút không hoàn lại $b=2$; "Lời giải:" $1/15$ và cặp liền nhau $5/15=1/3$. 59 âm tiết, 7 dòng hiển thị (ngoại lệ hai cột ghi trong storyboard), đáy 653 px. Ghi chú diễn giả viết lại (bỏ "Vì vậy dùng từ…", "Kết luận chốt:"). Ghi chú bài giảng: mục topic-07 viết lại (Nhận xét 08.9, Ví dụ 08.12, "Trong thực hành.", kiểm tra nhanh) và đoạn kết phần 3. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S21 | `L08-14` | chấp nhận; ngoại lệ 7 dòng hiển thị (hai cột so sánh) ghi trong storyboard; câu hỏi hai phần ($1/15$, $1/3$) chấp nhận | diff; tính lại $\binom62$, 5 cặp liền nhau, trung bình 8 lần dùng mỗi mẫu; `check.py` |
- Bước S22 (`L08-M4T`, biên tập viên): trang tiêu đề mạch 4 ở đầu section ngoài thứ 4, `id="mach-4"`, khuôn `L08-M3T`: "4. Hàm mất mát và thuật toán DQN"; dòng dẫn "Muốn cập nhật $\theta$ từ mini-batch, phải lấy gradient chỉ qua dự đoán của mạng trực tuyến." (17 âm tiết); năm cụm từ khóa; ghi chú diễn giả 90 âm tiết; topic-09. `#/4` và mục 4 của `L08-02b` mở đúng trang (hash `#/mach-4`). Ghi chú bài giảng: `## 4. Hàm mất mát và thuật toán DQN` với topic-09, 08, 10, 11 theo thứ tự trang; topic-12 dưới tiêu đề tạm "## Mạng mục tiêu và bất ổn" (mạch 6); nội dung chưa viết lại. `no-ai-slop` Edit, tự kiểm theo `eval.md`: đạt. Chờ điều phối viên duyệt.
| S22 | `L08-M4T` | chấp nhận; bài tập trong note giữ ở mục bài tập cuối chương (đánh số 08.k ở bước `X01`/`X02`); mục topic-12 dời ở bước `L08-M6T` | diff; `#/4` mở đúng trang |
