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

## Kiểm định cuối của điều phối viên

- 37 mã trang duy nhất, 37 khối ghi chú và 37 mục storyboard; độ sâu `<section>` lớn nhất là 2.
- KaTeX nghiêm ngặt đọc 166 biểu thức, không có lỗi phân tích.
- Tám SVG hợp lệ về XML, có `role="img"`, `title`, `desc`; nhãn nhỏ nhất là 34 px.
- HTML và tám SVG trả HTTP 200 tại cổng 8765.
- Không có ảnh raster, tài nguyên mạng cốt lõi, mã trang, nhãn phân tuyến hoặc thời lượng lộ trên mặt trang và ghi chú.
- Cỡ chữ hiệu dụng của giả mã là khoảng 0,77 em và của bảng là khoảng 0,76 em.
- Nhánh optimizer có độ sâu dọc một cấp và có thể bỏ qua bằng điều hướng ngang sau trang tổng quan.
- Năm tệp HTML/quy trình trong dự án Codex Slides khớp từng byte với bản trong kho sau khi đồng bộ.

Codex Slides đã được dùng làm dự án bền vững và kho Design Files, nhưng Codex Browser trong trình soạn thảo không khả dụng trong phiên này. Vì vậy chưa thể tuyên bố đã duyệt trực quan bằng Codex Slides hoặc kiểm tra tràn trang bằng Browser. Các kiểm tra RevealJS cục bộ, cấu trúc, công thức, đường dẫn và tài sản đã được thực hiện đầy đủ; giới hạn trực quan này được giữ rõ trong bàn giao.
