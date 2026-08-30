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
