# Nhật ký rà soát Bài 04

## Trạng thái sau chỉnh sửa

- 38 trang tuyến chính, 4 trang bài tập dọc; 5 SVG cục bộ; không dùng raster hoặc tài nguyên mạng cốt lõi.
- Bản trước đã hợp nhất bốn báo cáo độc lập; lượt bổ sung dưới đây có kiểm định storyboard và đủ năm báo cáo độc lập. Mọi mục `chặn bàn giao` và `nghiêm trọng` đều có quyết định xử lý.
- Không sửa `index.html`, CSS dùng chung, không commit hoặc push.

## Bốn báo cáo độc lập — đầu vào chỉnh sửa

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | A00–A03 cũ | Hình thức hóa $v_*,T^\pi,T_*$ đến trước khi người học thấy một quyết định cụ thể. | A02 nằm sau hai trang định nghĩa/tính chất. | Chuyển micro-example lên trước mọi hình thức tối ưu. | A02 đứng trước A08,A00,A01,A03. |
| nghiêm trọng | B06,C04,D03 cũ | Giả mã và chứng minh quá dày cho màn chiếu. | Codebox dưới 0,75 em; nhiều kết luận trên một trang. | Tăng chữ, tách thuật toán và chứng minh. | Codebox và bảng 0,92 em theo cỡ chữ trang; tách C04/C09, D03/D06, D04/D07. |
| trung bình | A07,D05 cũ | Hai kiểm tra thiếu mô hình cách nhau xa và lặp vai trò. | Cùng hỏi trạng thái hữu hạn/hạt nhân. | Gộp kiểm tra vào CartPole gần cuối bài. | Bỏ A07; D05 có câu hỏi và đáp án fragment. |
| trung bình | các câu hỏi chính | Thiếu kết luận thấy được sau tương tác. | Đáp án chỉ có trong notes. | Thêm fragment ngắn khi thực tế. | P02, B06, C05, D05 có đáp án fragment. |

### Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | phần Bellman tối ưu | Thiếu $q_*$, Bellman $q_*$ và cách trích chính sách. | Bài đi thẳng từ $v_*$ sang $T_*$, không nối giá trị hành động. | Thêm định nghĩa, phương trình và greedy extraction từ A02. | Thêm A08,A09; A00 nối $v_*=\max_aq_*$. |
| nghiêm trọng | B02–B03 | Bước đổi hành động ở $s_0$ thiếu giá trị hành động giải thích. | Chỉ ghi $\pi_2=(b,b)$. | Tính $q_{\pi_1}(s_0,b)$. | B03 hiển thị $27$. |
| nghiêm trọng | X09 | Bài tập không tự chứa MDP. | Notes trỏ người học sang PDF. | Chép dữ kiện gọn và lời giải truy nguyên. | X09 có đủ sáu cặp trạng thái–hành động; notes cho $V_1$ và greedy. |
| trung bình | D08 mới | Thiếu cầu nối tới điều khiển phi mô hình. | CartPole kết bài nhưng không nêu vai trò $q_*$. | Thêm trang quyết định cuối. | D08 nối $q_*$ với các bài điều khiển sau. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | A01,A03,D01–D02 cũ | Miền toán tử và chuẩn xuất hiện ngầm. | Dùng “co” trước khi định nghĩa không gian và chuẩn. | Định nghĩa $\mathcal V$, chuẩn vô cùng, kiểu $T^\pi,T_*$. | P02, A01, A03 đã sửa. |
| nghiêm trọng | A01 cũ | Miền chính sách của $T^\pi$ không rõ. | Có thể bị hiểu áp dụng trực tiếp cho chính sách phụ thuộc lịch sử. | Ghi chính sách Markov dừng. | A01 và D03/D06 phân biệt hai miền. |
| nghiêm trọng | B04 cũ | Ngưỡng dừng chưa cho biết sai số của giá trị nào. | Dừng theo chênh lệch nhưng không gắn với bảng trả về. | Dùng $\varepsilon_{\mathrm{step}}$ và chặn contraction đúng. | B04 trả $v_{j+1}$, chặn $\gamma\varepsilon_{\mathrm{step}}/(1-\gamma)$. |
| nghiêm trọng | C04 cũ | Phần dư tại bảng mới cần thêm một lượt $T_*$. | Giả mã vừa cập nhật vừa dùng residual không tách chi phí. | Tách lượt cập nhật và lượt residual. | C04/C09; C06 tính lượt kiểm đầu và nêu cách tái sử dụng $w=T_*v$ ở các vòng sau. |
| chặn bàn giao | D04 cũ | Hai chặn được nêu mà không suy diễn. | Không có bước $\rho+\gamma e$ hay greedy identity. | Tách residual→value và value→policy. | D04, D07 mở đầy đủ bước chính. |
| chặn bàn giao | D03 cũ | Chứng minh tối ưu toàn cục quá dày và dễ dùng sai $T^\pi$. | Cận trên và đạt cận nằm chung một trang. | Tách upper bound và greedy attainment. | D03 và D06. |
| trung bình | C06 cũ | Nhãn chi phí “thường cao/thấp” không kiểm chứng được. | Không ghi phép tính chính. | Ghi chi phí theo $|\mathcal S|$ và lượt mô hình. | C06 dùng ba hàng định lượng. |

### Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | A00–A04 cũ | Công thức đúng riêng lẻ nhưng trình tự chưa hỗ trợ suy luận $q_*\to v_*\to T_*$. | Micro-example đến muộn; thiếu cầu nối giá trị hành động. | Dùng A02 trước, truyền cùng số qua các hình thức. | A02→A08→A00→A01→A03→A09. |
| nghiêm trọng | B07 cũ | Lặp chính sách sửa đổi không đủ dữ kiện để tái lập hoặc gắn bảo đảm. | Không rõ mang $v_0$, dừng ngoài, phá hòa, chi phí. | Hoàn thiện hoặc bỏ khỏi tuyến chính. | Bỏ B07; log sai khác; giữ PI chính xác B06–B08. |
| nghiêm trọng | C04–C08 cũ | Tiêu chuẩn dừng xuất hiện trước cơ chế tính residual và chứng minh. | Chưa thấy lượt $T_*$ bổ sung. | Tách cơ chế, xem trước, rồi chứng minh cuối bài. | C04,C09,C08→D04,D07. |
| trung bình | D05 cũ | CartPole trong nửa lưới khó đọc. | Hình chỉ có max-width, không có width cục bộ. | Đặt width rõ và giữ max-height. | CSS `.figure` và `.grid2 .figure` đã sửa. |
| trung bình | kết bài cũ | Không có trang tổng hợp quyết định trước bài tập. | D05 chuyển thẳng sang nhánh dọc. | Thêm trang quyết định. | D08 được thêm trước X09. |

## Sai khác có chủ ý so với nguồn

- Gộp các trang mục lục/tính chất lặp; bỏ trang định lý xem trước để dành không gian cho $q_*$ và các bước chứng minh.
- Bổ sung A08/A09 về $q_*$, Bellman $q_*$ và greedy extraction. Đây là sai khác nội dung lớn nhất nhưng dùng trực tiếp micro-example A02 và ký hiệu chuẩn của chính bài.
- Bỏ lặp chính sách sửa đổi khỏi tuyến chính vì nguồn không đủ đặc tả tái lập. Không bỏ PI chính xác hoặc bảo đảm tối ưu hữu hạn.
- Tách C04/C09 để tính residual bằng một lượt $T_*$ thêm; bổ sung chi phí lượt này.
- Tách D03/D06 và D04/D07 để mỗi trang chỉ giữ một bước chứng minh.
- Gộp kiểm tra mô hình đầu bài vào CartPole; thêm D08 làm trang quyết định cuối.
- Không thêm code demo hoặc thuật toán phi mô hình.

## Quyết định không áp dụng

- Không hoàn thiện lặp chính sách sửa đổi bằng các giả thiết hoặc định lý ngoài nguồn. Việc này sẽ mở rộng phạm vi và cần một phân tích hội tụ riêng.
- Không đưa Q-learning vào A09/D08. Chỉ nêu $q_*$ là cầu nối; thuật toán học từ trải nghiệm thuộc bài sau.
- Không chuyển X09 thành ví dụ chính vì 120 phút đã phân bổ đủ; dữ kiện đầy đủ được giữ ở nhánh dọc.

## Sửa cục bộ sau tái rà

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | A08 | Định nghĩa $q_*$ bằng điều kiện $A_0=a$ có thể không xác định khi biến cố này có xác suất bằng không dưới chính sách. | Chính sách tiếp tục và hành động đầu chưa được tách. | Dùng can thiệp ép hành động đầu, rồi tối ưu chính sách từ $t=1$. | Định nghĩa $a\triangleright\pi$ và giải thích rõ trong notes. |
| nghiêm trọng | A09,D06 | Trích tham lam được gọi là chính sách tối ưu trước khi chứng minh đạt cận. | Kết luận xuất hiện trước bước $T^{\pi_v}v_*=v_*$. | Chỉ gọi là ứng viên tại A09. | Dùng $\bar\pi$ tại A09; chỉ kết luận tối ưu ở D06. |
| nghiêm trọng | X09 | Lời giải tham lam chưa cho các giá trị hành động tạo từ $V_1$. | Kết quả $(b,a,a)$ thiếu phép tính trung gian. | Ghi đủ hai giá trị tại mỗi trạng thái. | Notes có $Q_{V_1}(s_0)=(1{,}35;2{,}8)$, $Q_{V_1}(s_1)=(2{,}9;0{,}8)$ và $Q_{V_1}(s_2)=(3{,}8;0{,}9)$. |
| nghiêm trọng | C09 | Lượt kiểm phần dư có thể bị tính lại khi VI chưa dừng. | $w=T_*v$ đã là bảng lặp kế tiếp. | Gán $v\leftarrow w$ và lặp. | Giả mã và notes nêu rõ tái sử dụng; ngưỡng được giới hạn cho $\gamma>0$. |
| trung bình | A02 | Hai nhánh số chưa nói rõ là kết quả tất định và giá trị tiếp tục tối ưu. | Người học có thể hiểu $v_*(s')$ là giá trị tức thời. | Nêu trạng thái kế chắc chắn và chính sách tiếp tục. | Hai nhánh ghi rõ kết quả tất định; notes nêu tiếp tục tối ưu từ $t=1$. |
| trung bình | A09 | Cầu nối từ Bellman $q_*$ tới phép cực đại chưa có tương tác thực. | Chỉ có công thức và kết luận. | Hỏi vị trí của phép cực đại và cho đáp án ngắn. | Thêm “Câu hỏi:” và fragment giải thích cực đại tại trạng thái kế. |
| trung bình | B08 | Notes còn câu biên tập về phân tuyến nội dung. | Câu này không thuộc mạch nói. | Chuyển quyết định biên tập sang planning. | Notes chỉ giữ bảo đảm và giả thiết phá hòa. |
| trung bình | CSS,D08 | Bảng/codebox nhỏ và bảng kết bài dài. | Cỡ cục bộ dưới ngưỡng; câu trong ô dài. | Tăng cỡ chữ, rút gọn hàng. | Bảng và codebox 0,92 em; D08 dùng bốn lựa chọn ngắn. |

Rà lân cận sau sửa: A02–A09–A00–A01 giữ mạch ví dụ → định nghĩa → hình thức; B06–B08 giữ bảo đảm PI; C04–C09–C05–C06 nối cập nhật → kiểm phần dư → chi phí; D06–D08–X09 nối chứng minh → quyết định → bài tập. Số trang và tổng thời lượng không đổi.

## Tự kiểm toán học của tác tử chỉnh sửa

- A02: $2+0{,}9\cdot5=6{,}5$; $0+0{,}9\cdot8=7{,}2$.
- B03: $q_{\pi_1}(s_0,b)=0+0{,}9\cdot30=27$.
- B04: nếu $\Delta_j\le\varepsilon_{\mathrm{step}}$, sai số của $v_{j+1}$ không quá $\gamma\varepsilon_{\mathrm{step}}/(1-\gamma)$.
- C02 dùng đúng $\gamma=0{,}9$ và cập nhật đồng bộ.
- D04: $e\le\rho+\gamma e$ cho $e\le\rho/(1-\gamma)$.
- D07: từ $T^{\pi_v}v=T_*v$, $L\le\gamma e+\gamma(e+L)$, nên $L\le2\gamma e/(1-\gamma)$.
- X09: $V_1=(1,2,2)$; chính sách tham lam $(b,a,a)$.

## Tự kiểm biên tập và mạch

- `no-ai-slop`: câu trực tiếp, không khẩu hiệu, không nhận định quảng bá, không lặp kết luận; thuật ngữ và ký hiệu nhất quán.
- Quill: ví dụ → định nghĩa → toán tử → thuật toán → bảo đảm → giới hạn; không có công thức trọng tâm trước tiên quyết.
- Không tạo `quill.json`; đây không phải dự án sách.

## Giới hạn

- Cần tác tử độc lập tái rà phần $q_*$, B04, C09 và D03–D07 vì đây là các thay đổi toán học đáng kể.
- Cần điều phối viên rà trực quan toàn bộ trang bằng RevealJS/Codex Slides ở khung 16:9 và màn hình hẹp.

## Kiểm tĩnh của tác tử chỉnh sửa

- HTML có 42 `data-slide-id` duy nhất: 38 trang chính và 4 trang dọc; cả 42 trang có notes và nằm ở độ sâu section đúng mẫu.
- Mọi ID có mục tương ứng trong storyboard; không có ID, phân bổ hoặc chỉ dẫn phân tuyến xuất hiện trên mặt trang hay trong notes.
- 15 đường dẫn CSS, script và hình đều là tài sản cục bộ tồn tại; không có raster hoặc URL cốt lõi bên ngoài.
- Năm SVG phân tích XML được, có `role="img"`, `title`, `desc`; cỡ chữ nhỏ nhất là 30 px.
- KaTeX nghiêm ngặt phân tích 232 công thức không có lỗi; `git diff --check` sạch.

## Tái rà cuối

- Tác tử toán học–thuật toán xác nhận định nghĩa $q_*$ bằng hành động đầu bị ép, ứng viên tham lam, chứng minh tối ưu, phép tính X09 và luồng lặp giá trị đều đúng. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Tác tử học thuật–giảng dạy xác nhận cỡ chữ hiệu dụng của bảng/giả mã là $0{,}7544\,\mathrm{em}$, câu hỏi A09 và storyboard khớp, ghi chú diễn giả sạch chỉ dẫn nội bộ, 38 trang chính đủ 120 phút và ranh giới Bài 03/Bài 05 được giữ. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.

## Kiểm định cuối của điều phối viên

- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Điều phối viên dùng cây web tạm không có `.env` và `python3 -m http.server 8765 --bind 127.0.0.1` để kiểm thử tại đúng cổng 8765.
- HTML có 42 mã trang duy nhất, 42 ghi chú diễn giả và đúng cấu trúc section lồng; mọi mã đều có mục trong storyboard.
- Chromium headless dựng đủ 42 trang ở 1280 × 720 và 800 × 600, không có lỗi console hoặc request. Điều hướng `↓`, `↑`, `→` cho kết quả P01, P00, A02. Điều phối viên duyệt ảnh mọi trang và mở riêng các trang công thức bị bộ dò hình học gắn dương tính giả do cấu trúc nội bộ KaTeX; không thấy cắt, chồng hoặc tràn.

## Pha II — đồng bộ với lecture note và rà lại độc lập

### Runtime OpenRouter

- Tác tử lập kế hoạch: `requested_model=deepseek/deepseek-v3.2`, `observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`; hồ sơ `plan`, 10 lượt. Lần đầu dừng với `model exceeded the tool-call limit (8)`; lần chạy lại thành công.
- Hai lượt writer đầu dùng `requested_model=z-ai/glm-5.3-flash` lần lượt dừng với `model exceeded the tool-call limit (10)` và `model exceeded the tool-call limit (8)`. Lượt sửa tiếp theo bị mất JSON ở lớp điều phối nên không dùng lời tự khai của worker làm bằng chứng runtime; điều phối viên kiểm tra diff và hoàn tất các sửa còn thiếu.
- Năm báo cáo độc lập ban đầu dùng đúng mô hình quy định. Bốn lượt thành công ngay; vai phản biện học thuật–giảng dạy lần đầu dừng với `model exceeded the tool-call limit (8)` rồi chạy lại thành công. Các JSON thành công đều ghi `provider=OpenRouter` và `requested_model=observed_model`.
- Tái rà toán–thuật toán: lần đầu dừng với `model exceeded the tool-call limit (6)`; lần chạy lại thành công với hồ sơ `recheck`, 8 lượt, `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Tái rà phản biện học thuật–giảng dạy: hồ sơ `recheck`, 6 lượt, `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Tái rà kết nối và mạch viết: hồ sơ `recheck`, 5 lượt, `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Mọi liên kết `.env` tạm trong gói worker đã được gỡ sau khi các tiến trình kết thúc. Không đưa `.env` vào gói nội dung, prompt hoặc nhật ký.

### Năm báo cáo độc lập và quyết định

| Vai | Mức cao nhất | Vấn đề chính | Quyết định |
|---|---|---|---|
| Góc nhìn sinh viên | trung bình | A02 thiếu nguồn của giá trị tiếp tục 10/11; A08 cần giải thích can thiệp trên mặt trang; cầu nối miền chính sách ở A01 còn mờ. | Nêu 10/11 ở A02; định nghĩa rõ can thiệp ở A08; A01 hẹn chặn chân trời ở phần bảo đảm. Sửa câu phân bổ Bài 9 thành 12 phút. |
| Chuyên gia Học tăng cường | trung bình | A08 cần tách can thiệp khỏi điều kiện hóa; D01 cần nêu cơ sở đơn điệu. | Sửa A08; tách hai cơ sở đơn điệu thành hai gạch đầu dòng ở D01. Không đổi thứ tự A02→A08→A00 vì đây là mạch ví dụ→định nghĩa→giá trị. |
| Toán học và thuật toán | trung bình | C09 cần ký hiệu phép nhân rõ; lecture note cần chặn dừng B04 và ngưỡng mất mát chính sách. | Dùng `\cdot` ở C09; bổ sung hai chặn vào topic 06 và 13; tự tính lại micro-example và $k=44$. |
| Phản biện học thuật–giảng dạy | nghiêm trọng | A08 chưa nói rõ $a\triangleright\pi$ buộc $A_0=a$, không phải điều kiện hóa theo hành động do $\pi$ sinh. | Đã sửa trực tiếp trên mặt trang và trong ghi chú; tái rà xác nhận lỗi nghiêm trọng được xử lý triệt để. |
| Kết nối và mạch viết | trung bình | C08 cần báo rõ ba bước sẽ được xử lý theo thứ tự; topic 06 trong note cần neo B04. | Thêm câu chuyển ở C08 và chặn đánh giá vào topic 06. Báo cáo ban đầu đếm nhầm nhánh dọc thành section ngoài; kiểm tĩnh xác nhận đúng 5 section ngoài. |

Các đề xuất không áp dụng:

- Giữ dấu phẩy thập phân theo quy ước tiếng Việt; không đổi sang dấu chấm.
- Giữ định nghĩa ngắn của $\Pi$ ở A00 dù đã có ở P02 để trang định nghĩa $v_*$ tự chứa.
- Giữ công thức đếm chính sách ở B08 vì sửa trực tiếp lỗi của nguồn trang 33.
- Không đổi thứ tự cụm tối ưu và không chuyển Bài 9 vào tuyến chính; hai thay đổi này không cần thiết để sửa lỗi cục bộ.

### Tái rà sau chỉnh sửa

- Toán–thuật toán xác nhận các số $10$, $11$, $9{,}9$, nghiệm biến thể $20$, định nghĩa $a\triangleright\pi$, chặn đánh giá, ngưỡng phần dư, số chính sách, tính đơn điệu và $k=44$ đều đúng; không còn lỗi chặn hoặc nghiêm trọng.
- Phản biện học thuật–giảng dạy xác nhận A08 đã phân biệt can thiệp với điều kiện hóa; các cầu nối từ ví dụ tới hình thức và từ tiêu chuẩn dừng tới chứng minh nhất quán; không còn lỗi chặn hoặc nghiêm trọng.
- Kết nối và mạch viết rà A02±2, A08–A03, B06–C00 và C08–D03; xác nhận 5 section ngoài, 42 mã trang và bốn bài tập dọc nằm trong section kết luận; không còn lỗi chặn hoặc nghiêm trọng.
- `no-ai-slop`: loại từ tiếng Anh không cần thiết trong topic 06, cắt diễn giải trùng và giữ câu trực tiếp. Quill: dàn ý vẫn theo ví dụ→định nghĩa→toán tử→thuật toán→bảo đảm→giới hạn; không tạo `quill.json`.

### Kiểm định cuối sau Pha II

- Kiểm tĩnh: 42 `data-slide-id` duy nhất, 42 ghi chú, 5 section ngoài; mọi tài nguyên tương đối tồn tại; `git diff --check` sạch.
- `python3 -m reloadserver 8765` không chạy vì thiếu mô-đun `reloadserver`. Dùng cây web cô lập trong `/tmp`, không chứa `.env`, và `python3 -m http.server 8765 --bind 127.0.0.1 --directory <cây-tạm>`.
- Chromium headless kiểm đủ 42 trang ở 1280×720 và 800×600. Lần đầu phát hiện A01 bị cắt công thức ở mép phải; đã tách kiểu toán tử và định nghĩa thành hai dòng rồi chạy lại toàn bộ. Kết quả cuối: không tràn, không lỗi KaTeX, console, request hoặc tài nguyên; không có request ngoài máy chủ cục bộ. Phím `↓`, `↑`, `→` lần lượt tới P01, P00, A02.
- Trình đọc lecture note ở 390×844 trả HTTP 200, dựng 589 công thức KaTeX, 30 khối `details`, 15 lời giải; không tràn ngang, không lộ `note-topic-id`, phím Enter mở được khối đầu tiên.
- Codex Slides không khả dụng trong môi trường này do runtime Node.js 18 thấp hơn yêu cầu Node.js 20 của gói. Vì vậy chỉ xác nhận kiểm định RevealJS cục bộ, không tuyên bố đã rà bằng Codex Slides.
- Năm SVG tải được trong Chromium; mỗi tệp có `role="img"`, `title`, `desc`. Không có ảnh raster hoặc tài nguyên cốt lõi qua mạng. Môi trường thiếu `xmllint`, nên tính hợp lệ được xác nhận qua tải ảnh thực tế và không có request lỗi.
- Bốn tệp văn bản HTML/outline/storyboard/review-log đã được ghi vào Design Files của dự án Codex Slides `20260824154346-chuy-n-lecture-4-gi-i-mdp-b-ng-quy-ho-ch-z4es` và đọc lại trùng chính xác nội dung trong kho. Tải riêng `gridworld.svg` lên Design Files trả HTTP 500; SVG vẫn được kiểm trực tiếp trong RevealJS.
- Dự án Codex Slides vẫn ở trạng thái `draft`, bước `clarify`, 0 trang; Codex Browser không khả dụng trong phiên này. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; kiểm tra trực quan được thực hiện trên RevealJS cục bộ.

## Lượt rà storyboard và năm báo cáo độc lập — lượt bổ sung B04

Runtime: các lượt thành công dùng `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` (storyboard, sinh viên, chuyên gia Học tăng cường, toán lượt hẹp, học thuật–giảng dạy và mạch viết). Lượt toán đầu vượt giới hạn tool-call nên không được tính; lượt toán hẹp sau đó thành công.

### Rà storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | A02,A09 | Cột Kiểm tra ghi cả A02. | A02 là ví dụ; chỉ A09 đặt câu hỏi kiểm tra Bellman tối ưu. | Chỉ ghi A09 ở cột Kiểm tra. | Chấp nhận. |
| nhẹ | C09 | Dùng $\varepsilon_{\mathrm{pol}}$ trước khi định nghĩa trên mặt trang. | Ký hiệu chỉ được giải thích trong mạch chứng minh sau đó. | Nêu đây là mức mất mát chính sách cho phép. | Chấp nhận. |

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | A02,A09 | Storyboard gán sai vai trò kiểm tra cho A02. | A02 không có nhãn “Câu hỏi:”. | Chỉ giữ A09 ở bước kiểm tra. | Chấp nhận. |
| nhẹ | B06 | Cụm “giá trị có thể không tăng nghiêm” chưa nói rõ hệ quả. | Người học chưa thấy vì sao phá hòa tùy ý nguy hiểm. | Nêu khả năng tạo chu trình chính sách. | Chấp nhận. |
| nhẹ | X07 | Có thể thêm nhãn tự luyện trên mặt trang. | Nhãn giúp phân tuyến bài tập. | Thêm nhãn. | Không áp dụng: quy ước cấm hiển thị nhãn phân tuyến nội bộ. |
| chặn bàn giao | toàn bài | Báo thiếu thư viện RevealJS trong cây worker. | Cây tạm chỉ chứa tệp được phép gửi, không phải kho đầy đủ. | Bổ sung thư viện. | Bác bỏ là dương tính giả; kho thật có đủ tài sản cục bộ và sẽ được kiểm khi render. |

### Chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | X09 | Chỉ bao phủ phần 1 của Bài 9. | Phần 2 không xuất hiện trong nhánh bài tập. | Thêm phần 2. | Không thêm trang: nội dung trùng chu trình B01–B03 và vượt 12 phút; ghi rõ sai khác trong outline, notes và nhật ký. |
| nhẹ | A08–A00 | Có thể nhắc lại quan hệ $q_\pi$–$v_\pi$. | Bài đi thẳng vào $q_*$ và $v_*$. | Thêm trang/công thức nhắc lại. | Không áp dụng: đây là tiên quyết đã hoàn thành ở Bài 03. |
| nhẹ | C06 | Ánh xạ trang nguồn 29 chưa rõ. | Nguồn dùng so sánh định tính, đích dùng chi phí định lượng. | Ghi sai khác. | Chấp nhận trong outline và nhật ký. |
| nhẹ | P01 | Từ “hạt nhân” có thể mơ hồ. | Notes chưa ghi ký hiệu cụ thể. | Gọi rõ mô hình chuyển–thưởng $p(s',r\mid s,a)$. | Chấp nhận. |
| nhẹ | D08 | Cầu nối sang Bài 05 chưa thu hồi phân ranh mô hình. | Kết bài chỉ nhắc $q_*$. | Nêu rõ biết mô hình và không biết mô hình. | Chấp nhận. |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | B06 | Giải thích phá hòa chưa nêu điều kiện gây chu trình. | Đổi tùy ý giữa các hành động đồng hạng có thể làm chính sách đổi qua lại dù giá trị không đổi. | Nêu phá hòa tùy ý có thể tạo chu trình; dùng quy tắc cố định. | Chấp nhận. |
| nhẹ | A02,B04,C09,D04,D07,X09 | Không phát hiện lỗi số hay công thức. | Tính lại cho kết quả lần lượt $6{,}5$, $7{,}2$, các chặn phần dư và chính sách $(b,a,a)$. | Giữ các phép tính. | Chấp nhận; X09 được rà lại sau khi tách bốn hàng chuyển. |

### Phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | X09 | Hai hàng gộp làm mỗi hành động có hai kết quả xác suất 1. | Mỗi hàng `(s_1,a),(s_1,b)` và `(s_2,a),(s_2,b)` chứa hai chuyển tất định. | Tách thành bốn hàng, mỗi cặp $(s,a)$ có đúng một kết quả. | Chấp nhận. |
| trung bình | B05 | Điều kiện công bằng được viết như mô tả, chưa phải giả thiết chủ động. | Câu cũ không chỉ rõ lịch cập nhật phải thỏa điều kiện. | Viết “lịch cập nhật phải…”. | Chấp nhận. |
| trung bình | C03 | “Bảng đã kiểm tra” không chỉ ra quan hệ với phần dư. | Chặn ở C09 yêu cầu cùng một $v$. | Nói chính bảng $v$ dùng để kiểm phần dư. | Chấp nhận. |
| nhẹ | B06 | Tổng chuyển bị viết tắt. | Thiếu chỉ số $s',r$ và đối số của $p$. | Viết đầy đủ phép tổng Bellman. | Chấp nhận. |

### Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | A02→A00 | $v_*$ xuất hiện trước trang định nghĩa. | A02 ghi trực tiếp $v_*(s_1),v_*(s_2)$. | Dùng cụm “giá trị tiếp tục tối ưu”, đặt ký hiệu ở A00. | Chấp nhận. |
| nhẹ | B08→C00 | Chuyển từ PI sang VI chưa hiện trên mặt trang. | Vai trò trong mạch: kết PI; kết nối ra Gridworld còn nằm ở suy luận của người học. | Thêm câu báo bỏ bước giải hệ và chuyển sang VI. | Chấp nhận. |
| nhẹ | D08 | Kết bài chưa thu hồi rõ P01 và nối Bài 05. | Vai trò trong mạch: chọn công cụ; kết nối vào từ bảo đảm, kết nối ra bài tập/Bài 05 còn mờ. | Thu hồi đầu vào–đầu ra và phân ranh mô hình. | Chấp nhận. |
| trung bình | số section | Báo cáo đếm sáu section ngoài. | Bộ phân tích HTML và storyboard đều cho năm section ngoài; nhánh X nằm dọc trong section D. | Giảm số section. | Bác bỏ là lỗi đếm; giữ năm mạch hợp lệ. |

## Sửa sau các báo cáo

- HTML: sửa P01, A02, B05, B06, B08, C00, C03, C09, D08 và X09; bỏ `RevealMarkdown` không dùng khỏi riêng tệp B04.
- SVG: `gridworld.svg` bỏ vòng tự lặp “0” ở trạng thái kết thúc và ghi rõ không sao lưu.
- X09 có bốn hàng chuyển tất định riêng; $V_1=(1,2,2)$ và chính sách tham lam $(b,a,a)$ vẫn đúng.
- Outline ghi sai khác trang nguồn 29, lỗi gõ trang 33 và việc lược Bài 9 phần 2.
- Worker từng sửa nhầm bản sao `lecture-template.html`; điều phối viên loại thay đổi này, không đưa vào kho.
- Chưa tính lượt này là đã render hoặc kiểm định cuối; các bước đó do điều phối viên thực hiện sau tái rà.

## Tái rà sau chỉnh sửa

- Runtime của hai lượt thành công: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Rà toán học–thuật toán: tính lại độc lập X09 cho $V_1=(1,2,2)$, sáu giá trị hành động $(1{,}35;2{,}8)$, $(2{,}9;0{,}8)$, $(3{,}8;0{,}9)$ và chính sách $(b,a,a)$; tổng xác suất của mỗi cặp $(s,a)$ bằng 1. B05, B06, C03, C09 và `gridworld.svg` nhất quán; không còn lỗi chặn bàn giao hoặc nghiêm trọng.
- Rà mạch viết: xác nhận đúng 5 section ngoài và các ranh giới A02±2, B05–C00, C03–C09, D05–X09. Không còn lỗi chặn bàn giao hoặc nghiêm trọng. Đề xuất nhẹ ở A02 được áp dụng bằng cách hiển thị trực tiếp hai phép tính thay cho ký hiệu suy ra; thứ tự ID C09 trước C05 là chủ ý và không đổi thứ tự trình bày.

## Giai đoạn I — ghi chú bài giảng

### Đầu ra và runtime

- Tạo `materials/lec-04/lecture-note.md` gồm 15 chủ đề duy nhất, đủ bốn nhóm cốt lõi, cầu nối, bổ sung và đọc thêm; mỗi chủ đề có câu hỏi, gợi ý và lời giải.
- Ba reader lập kế hoạch, phân tích nguồn và hợp nhất đều trả
  `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Writer bản đầu và các lượt sửa thành công đều trả
  `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Năm vai rà độc lập dùng đúng model được phân công: sinh viên và mạch viết dùng
  `z-ai/glm-5.3-flash`; chuyên gia Học tăng cường, toán–thuật toán và phản biện
  giảng dạy dùng `deepseek/deepseek-v3.2`; mọi kết quả hợp lệ có provider
  `OpenRouter`.

### Vấn đề bắt buộc và quyết định

| mức độ | chủ đề | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| nghiêm trọng | `lec-04-topic-11` | Bài tập yêu cầu sai số nhỏ hơn 1 nhưng lời giải dùng ngưỡng 0,1. | Bất đẳng thức đúng là $0{,}9^k100<1$. | Sửa thành $k>43{,}7$, cần 44 lượt. |
| nghiêm trọng | `lec-04-topic-06` | Tuyên bố đánh giá dừng sớm vẫn bảo đảm PI dừng hữu hạn thiếu giả thiết và ngoài phạm vi nguồn. | Bảo đảm trong bài dùng đánh giá chính xác. | Ghi rõ đánh giá dừng sớm là biến thể chưa phân tích. |
| nghiêm trọng | `lec-04-topic-12` | Chứng minh dùng tính đơn điệu trước khi phát biểu. | $T^\pi$ và $T_*$ phải bảo toàn thứ tự. | Thêm bổ đề đơn điệu ở topic 04, truy nguyên hw3 Bài 7. |
| nghiêm trọng | `lec-04-topic-02` | Lời giải ban đầu giữ $v_*(s_1)=11$ sau khi đổi phần thưởng của nhánh $b$, nên không tự nhất quán. | Hệ mới cho $v_*(s_0)=v_*(s_1)=20$. | Viết lại hệ, phép thế và kiểm tra nhánh $a$. |
| nghiêm trọng | `lec-04-topic-13` | Chặn mất mát chính sách được nêu nhưng suy diễn quá tắt. | Cần đưa $L$ sang hai vế trong $L\le\gamma e+\gamma(e+L)$. | Mở đầy đủ chuỗi bất đẳng thức và chặn theo phần dư. |

### Các sửa và sai khác có chủ ý

- Sửa lỗi gõ nguồn trang 33: số chính sách xác định tổng quát là
  $\prod_s|\mathcal A(s)|$; khi mọi trạng thái có cùng tập hành động thì bằng
  $|\mathcal A|^{|\mathcal S|}$.
- Dùng $C_{\text{model}}=O(\sum_s\sum_a|\operatorname{supp}p_{s,a}|)$ thay cho
  nhãn định tính “đắt/rẻ”; không tuyên bố PI hoặc VI nhanh hơn tuyệt đối.
- Giữ phần 1 Bài 9 trong khối 30 phút; phần 2 là tự học bằng PI ở topic 05–07.
  Không thêm Monte Carlo, Q-learning hoặc code demo.
- Giữ cả bản đồ bốn nhóm và danh sách 15 chủ đề: bản đồ phục vụ phân loại theo
  yêu cầu, danh sách cố định thứ tự ánh xạ. Đề xuất bỏ một khối được bác vì làm
  mất một trong hai chức năng này.
- Báo động `(27,30)` phải thành `(29,30)` được bác sau khi đối chiếu: MDP
  topic 05 dùng $s_0\xrightarrow{b}(0,s_1)$, còn biến thể topic 02–03 mới dùng
  phần thưởng 2. Hai reviewer tái rà đã xác nhận các nghiệm 10/11, 20/20 và
  27/30 đúng trong từng MDP.

### Lỗi worker và phục hồi

- Một lượt reviewer toán trên gói lớn dừng đúng lỗi
  `model exceeded the tool-call limit (4)`; chạy lại cùng DeepSeek trên một tệp
  cô lập và hoàn tất.
- Các writer vá rộng lần lượt dừng `model exceeded the tool-call limit (8)`,
  `model exceeded the tool-call limit (12)`, và
  `model returned an empty or incomplete answer after all retries`. Lượt vá ba
  điểm tiếp theo dừng `model exceeded the tool-call limit (4)` sau khi ghi một
  phần. Không đổi model; điều phối viên kiểm diff, khôi phục đoạn bị thay nhầm,
  áp dụng các vá cơ học còn lại và yêu cầu tái rà độc lập.
- Một recheck DeepSeek phạm vi hẹp dừng `model exceeded the tool-call limit (3)`;
  chạy lại cùng model với phạm vi dòng rõ hơn và hoàn tất.
- Liên kết `.env` chỉ tồn tại tạm để cầu nối nạp khóa, bị MCP chặn đọc và được
  gỡ ngay sau mỗi nhóm tiến trình. Không nội dung `.env` nào được đưa vào prompt,
  log hoặc sản phẩm.

### Tái rà sau sửa

- DeepSeek xác nhận Bellman, tính đơn điệu, tính co, số chính sách, điều kiện PI,
  phép tính 44 lượt, chi phí, chặn mất mát và Bài 9 đều đúng; không còn lỗi
  `chặn bàn giao` hoặc `nghiêm trọng`.
- GLM xác nhận đủ 15 marker, các kết nối vào–ra, thuật ngữ và văn phong; không
  còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Hai lượt cuối cùng đọc riêng topic 02 xác nhận ví dụ gốc thêm $b$ với phần
  thưởng 0 cho 10/11, còn bài kiểm tra đổi phần thưởng thành 2 cho 20/20; không
  còn bước nhảy logic. Phép thế được viết thêm một bước theo đề xuất mức trung bình.
- Tự kiểm `no-ai-slop`: không có khẩu hiệu, câu hỏi tu từ, kết luận lặp hoặc lời
  dẫn rỗng. Tự kiểm Quill: tuyến Bellman kỳ vọng → tối ưu → toán tử → PI/VI →
  hội tụ → phần dư → giới hạn liên tục giữ thứ tự tiên quyết. Không tạo
  `quill.json`.

### Kiểm định cuối ghi chú

- `python3 -m reloadserver 8765` thất bại vì môi trường thiếu mô-đun
  `reloadserver`. Điều phối viên dùng cây web tạm không chứa `.env` và
  `python3 -m http.server 8765 --bind 127.0.0.1` tại đúng cổng 8765.
- Chromium headless tải `material-viewer.html` ở 1440 × 900 và 390 × 844:
  HTTP 200, không lỗi console, page hoặc request; không tràn ngang toàn trang.
- Trình xem dựng 584 biểu thức KaTeX, không có `.katex-error`; nhận đủ 30 khối
  thu gọn gồm 15 lời giải; không hiển thị `note-topic-id`.
- Liên kết “Mở ghi chú” trên thẻ Bài 04 trỏ đúng tài liệu và deck. Dùng bàn
  phím đặt tiêu điểm vào `summary` rồi nhấn Enter mở được khối “Gợi ý”. Một
  bảng rộng dùng cuộn ngang cục bộ trong khung, không làm tràn trang.
- Kiểm tĩnh xác nhận 15 marker duy nhất, đủ 15 bộ exercise/hint/solution, chỉ
  dùng cú pháp `$...$` và `$$...$$` cho toán Markdown, không có `quill.json`
  hoặc liên kết `.env` ngoài tệp bí mật gốc đã được git bỏ qua.
- Codex Slides không khả dụng trong phiên này do runtime Node.js 18 thấp hơn
  yêu cầu của gói (Node.js 20 trở lên). Vì vậy không tuyên bố đã rà bằng Codex
  Slides; toàn bộ kiểm tra hiển thị giai đoạn này được thực hiện bằng trình xem
  tài liệu cục bộ và Chromium.

## Giai đoạn II — đồng bộ deck với lecture note

### Kế hoạch và bản nháp

- Reader lập kế hoạch thành công với
  `requested_model=observed_model=deepseek/deepseek-v3.2`,
  `provider=OpenRouter`. Lượt trước đó đọc gói bảy tệp rồi dừng đúng lỗi
  `model exceeded the tool-call limit (8)`; lượt thành công dùng gói bốn tệp
  đã đóng băng và không đổi model.
- Writer dùng `requested_model=observed_model=z-ai/glm-5.3-flash`,
  `provider=OpenRouter`. Lượt đầu dừng `model exceeded the tool-call limit (10)`
  sau khi sửa HTML và một phần outline. Lượt phục hồi cùng model dừng
  `model exceeded the tool-call limit (8)` sau khi hoàn thiện D01 và bảng ánh
  xạ outline. Điều phối viên kiểm diff và hoàn tất phần metadata planning còn
  lại trước khi mở đợt review.
- A02, A08, A00 và ghi chú A03 dùng lại micro-example của note: hành động $a$
  cho giá trị 10, hành động $b$ với phần thưởng 0 cho $9{,}9$; câu hỏi đổi phần
  thưởng $b$ thành 2 cho nghiệm tự nhất quán 20/20.
- B08 thêm số chính sách xác định $\prod_s|\mathcal A(s)|$ và trường hợp chung
  $|\mathcal A|^{|\mathcal S|}$; vẫn giả sử đánh giá chính xác và phá hòa cố định.
- D01 phát biểu tính đơn điệu của $T^\pi,T_*$ với đúng lý do; D02 thêm phép tính
  $0{,}9^k100<1$, cho số lượt tối thiểu 44.
- Giữ nguyên 42 trang, 5 mạch, 120 phút và năm SVG. `bellman-choice.svg` chỉ mô
  tả quan hệ tổng quát, không chứa phần thưởng hoặc giá trị số nên không cần sửa.
- Outline và storyboard ánh xạ đủ 15 `note-topic-id` tới mọi `data-slide-id`.
  Các mã chỉ nằm trong HTML và planning, không hiển thị trên mặt trang hoặc
  trong ghi chú diễn giả.

Checkpoint này chưa được tính là đã qua năm báo cáo độc lập hoặc kiểm định
RevealJS. Các bước đó được thực hiện sau khi đóng băng bản nháp.
