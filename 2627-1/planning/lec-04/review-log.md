# Nhật ký rà soát Bài 04

## Trạng thái sau chỉnh sửa

- 38 trang tuyến chính, 4 trang bài tập dọc; 5 SVG cục bộ; không dùng raster hoặc tài nguyên mạng cốt lõi.
- Bản sửa đã hợp nhất kiểm định storyboard và bốn báo cáo độc lập. Mọi mục `chặn bàn giao` và `nghiêm trọng` đã có sửa tương ứng.
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

- `python3 -m reloadserver 8765` đang phục vụ kho tại cổng 8765; trang bài giảng và trang chỉ mục trả HTTP 200.
- HTML có 42 mã trang duy nhất, 42 ghi chú diễn giả và đúng cấu trúc section lồng; mọi mã đều có mục trong storyboard.
- KaTeX ở chế độ nghiêm ngặt dựng được 22 công thức khối và 210 công thức nội dòng, không có lỗi.
- Năm SVG hợp lệ về XML, có `role="img"`, `title`, `desc`; cỡ chữ nhỏ nhất là 30 px. Không có ảnh raster hoặc tài nguyên cốt lõi qua mạng.
- Năm tệp HTML/planning đã được tải vào Design Files của dự án Codex Slides `20260824154346-chuy-n-lecture-4-gi-i-mdp-b-ng-quy-ho-ch-z4es` và đối chiếu trùng từng byte với tệp trong kho.
- Codex Browser không khả dụng trong phiên này. Vì vậy chưa thể xác nhận trực quan từng trang ở khung 1280 × 720, màn hình hẹp, chồng lấn, tràn chữ hoặc thao tác bàn phím trong Codex Slides. Các kiểm tra RevealJS cục bộ và kiểm tra tĩnh vẫn được thực hiện đầy đủ; không tuyên bố đã rà trực quan bằng Codex Slides.
