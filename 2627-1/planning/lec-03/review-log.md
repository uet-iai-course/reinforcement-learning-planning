# Nhật ký rà soát — Bài 03

## Trạng thái sau chỉnh sửa

- 35 trang tuyến chính, 4 trang bài tập dọc; 4 SVG cục bộ; không dùng tài sản raster.
- Tác tử chỉnh sửa đã hợp nhất kiểm định storyboard và bốn báo cáo độc lập. Mọi mục `chặn bàn giao` và `nghiêm trọng` trong các báo cáo đã có sửa tương ứng; cần tác tử độc lập tái rà phần toán học và trình tự đã đổi.
- Không sửa `index.html`, CSS dùng chung, không commit hoặc push.

## Bốn báo cáo độc lập — đầu vào cho vòng chỉnh sửa

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | B06–B07, C01–C05 cũ | Nghiệm xuất hiện trước khi người học có phương trình và ví dụ sao lưu. | Người học phải chấp nhận véc-tơ nghiệm chưa có cách sinh. | Đưa một backup Student trước Bellman; chuyển cả hai nghiệm sau công thức. | Đã sửa tại C00–C05. |
| nghiêm trọng | D03–D06 cũ | Cụm $P^\pi,r^\pi,v_\pi,q_\pi$ dồn công thức, thiếu phép tính trung gian. | Không có hàng $P^\pi,r^\pi$ hoặc giá trị $q_\pi$ cụ thể. | Thêm ví dụ trước hình thức và cầu nối giữa các giá trị. | Đã sửa tại D03–D08. |
| trung bình | toàn bài | 38 trang chính làm giảm thời gian suy luận Bellman và MDP. | Các trang B05–B08, C05 lặp đồ thị hoặc nghiệm. | Gộp trang lặp, giữ khoảng 34–35 trang. | Còn 35 trang; tăng thời lượng Bellman và MDP. |

### Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | A02, D01 cũ | Hai SVG Student không khớp động lực nguồn. | MRP thiếu hoặc gán sai cạnh; MDP bỏ nút ngẫu nhiên Pub và một số cạnh Sleep. | Vẽ lại đúng topology và xác suất nguồn. | Đã vẽ lại `student-mrp.svg`, `student-mdp.svg`. |
| chặn bàn giao | D08–D09 cũ | Racing Car không biểu diễn đủ sáu kết quả theo $(s,a)$. | Nhãn đồ thị không cho truy ra đầy đủ hạt nhân và thưởng. | Ghi rõ từng kết quả, xác suất, thưởng. | Đã vẽ lại `racing-car.svg`; D09 chỉ đọc mô hình. |
| nghiêm trọng | D01 cũ | Student MRP và Student MDP bị trình bày như cùng một đặc tả. | MRP có Pass, Pub; MDP dùng Pub làm hành động và không có Pass. | Nêu rõ đây là hai đặc tả khác nhau. | Đã sửa D01 và ghi trong note-for-author. |
| trung bình | P02, D11–D13 cũ | Thiếu định vị bài biết mô hình và quan hệ với các bài sau. | Nối sang Bài 04 còn chung chung. | Nêu quy hoạch động khi biết mô hình; phi mô hình về sau. | Đã sửa P02, D11, D13. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | C04 cũ | Điều kiện $\gamma=1$ chỉ nói đặt biên, chưa đủ để bảo đảm nghiệm hữu hạn. | Trạng thái kết thúc không tự bảo đảm thời gian kết thúc kỳ vọng hữu hạn. | Nêu $Q$ quá độ, $\rho(Q)<1$ và điều kiện đủ về thời gian kết thúc, thưởng bị chặn. | Đã sửa C04, C06 và notes. |
| nghiêm trọng | D00–D04 cũ | Miền thưởng, quy tắc tổng/tích phân và tính dừng của chính sách chưa rõ. | Công thức dùng tổng nhưng không nêu miền rời rạc; $\pi$ có thể bị hiểu phụ thuộc $t$. | Nêu miền hữu hạn/rời rạc, thay tổng bằng tích phân khi liên tục, chính sách Markov dừng. | Đã sửa D00, D02, D04. |
| nghiêm trọng | D04–D06 cũ | Thiếu quan hệ $v_\pi=\sum_a\pi q_\pi$ và ví dụ số cho $q_\pi$. | Tự kiểm yêu cầu phân biệt nhưng không có bước tính. | Thêm quan hệ trước kiểm tra và tính một cặp $q_\pi$. | Đã sửa D05–D06. |
| trung bình | A05 cũ | Quy ước véc-tơ phân phối không nhất quán giữa mặt slide và notes. | Dùng véc-tơ hàng rồi nói thêm véc-tơ cột. | Chọn một quy ước duy nhất. | Dùng véc-tơ cột tại A05 và outline. |

### Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | B06–C05 cũ | Công thức và nghiệm đúng riêng lẻ nhưng đặt sai trình tự sư phạm. | Nghiệm Bellman có trước định nghĩa Bellman; C05 lặp lại hai nghiệm. | Ví dụ sao lưu → phân rã → Bellman → dạng ma trận → điều kiện → nghiệm. | Đã sắp lại C00–C05; bỏ trang lặp. |
| nghiêm trọng | D03–D06 cũ | MRP cảm sinh chưa làm cầu nối từ Bellman MRP sang đánh giá chính sách. | Hai công thức $P^\pi,r^\pi$ đứng riêng, không dẫn tới $v_\pi$. | Tạo một hàng cụ thể rồi thêm $v_\pi=r^\pi+\gamma P^\pi v_\pi$. | Đã sửa D03–D04. |
| trung bình | D09–D10 cũ | Trang Racing Car quá tải, trang kế tiếp chủ yếu cảnh báo thay vì cho người học áp dụng. | Hệ phương trình, nghiệm và điều kiện hữu hạn dồn một trang. | D09 chỉ đọc mô hình; D10 thành câu hỏi lập hệ và kiểm hữu hạn. | Đã sửa D09–D10. |
| trung bình | D12 cũ | Tự kiểm chưa phủ đủ $v_\pi$, $q_\pi$ và Bellman kỳ vọng. | Chỉ yêu cầu biến MDP thành MRP. | Thêm quan hệ, điều kiện hóa và công thức Bellman. | Đã sửa D12. |

## Sai khác và sửa nguồn

| Mức độ | Trang nguồn | Vấn đề / quyết định | Lý do |
|---|---:|---|---|
| chặn bàn giao | 31,33 | Vẽ lại toàn bộ Student MRP theo đúng $P$. | Bản nháp có cạnh sai; SVG mới biểu diễn đầy đủ 13 cạnh kể cả Sleep tự lặp. |
| chặn bàn giao | 50 | Khôi phục topology Student MDP và nút ngẫu nhiên Pub. | Bản nháp bỏ nút ngẫu nhiên và làm sai quan hệ C2/C3 với Sleep. |
| chặn bàn giao | 51 | Warm–Fast nhận $-10$, tới Overheated rồi kết thúc. | Nguồn đồng thời gắn Fast với $+2$ và Overheated với $-10$; chọn một thưởng chuyển tiếp nhất quán để giải ví dụ. |
| nghiêm trọng | 36 | Không gọi $\gamma$ nhỏ là hành động tham lam. | $G_t$ không tự chọn hành động. |
| nghiêm trọng | 39 | Giá trị MRP do $P,r,\gamma$ quyết định. | MRP không có hành động. |
| nghiêm trọng | 47–48 | Bỏ phát biểu ánh xạ co chưa được định nghĩa; bổ sung điều kiện $\gamma=1$. | Tránh dùng định lý như khẩu quyết và tránh suy ra nghịch đảo toàn cục. |
| nghiêm trọng | 49,56–57 | Dùng hạt nhân chung $p(s',r\mid s,a)$. | Giữ điều kiện hóa và phần thưởng nhất quán. |
| trung bình | 58 | Chuyển nguồn đọc thiếu thư mục sang `note-for-author.md`. | Không đưa chỉ dẫn chưa kiểm chứng lên slide. |

## Quyết định không áp dụng

- Không thêm Bellman tối ưu, lặp giá trị, lặp chính sách hoặc thuật toán phi mô hình. Các nội dung này vượt phạm vi trang 28–58 và được nối sang Bài 04 hoặc các bài sau.
- Không thêm chứng minh phổ bán kính hoặc định lý nghịch đảo. Bản trình chiếu chỉ nêu điều kiện cần dùng; phần chứng minh không có trong nguồn và không phù hợp thời lượng.
- Không tạo code demo vì nguồn không có nội dung mã tương ứng.

## Kiểm tra toán học sau chỉnh sửa

- Student MRP dùng thứ tự C1, C2, C3, Pass, Pub, Facebook, Sleep; mọi hàng $P$ tổng bằng 1.
- Hai phần thưởng tích lũy với $\gamma=1/2$ là $-9/4$ và $-25/8$.
- $\gamma=0{,}9$: $(-5{,}012729,0{,}942655,4{,}087021,10,1{,}908392,-7{,}637608,0)$.
- $\gamma=1$, $v(\text{Sleep})=0$: $(-1016/81,118/81,350/81,10,65/81,-1826/81,0)$.
- Student MDP, chính sách đều, thứ tự Facebook, C1, C2, C3, Sleep: $(-30/13,-17/13,35/13,96/13,0)$.
- Tại C1: $q_\pi(\text{C1,Facebook})=-43/13$, $q_\pi(\text{C1,Study})=9/13$; trung bình là $v_\pi(\text{C1})=-17/13$.
- Racing Car dưới chính sách đều: thế $v(C)=0$, $v(W)=-6$ thỏa hai phương trình ở D10.

## Tự kiểm `no-ai-slop/eval.md`

- Câu trực tiếp; không dùng câu hỏi tu từ, khẩu hiệu, lời quảng bá hoặc kết luận lặp.
- Thuật ngữ trạng thái, chuyển tiếp, phần thưởng, phần thưởng tích lũy, giá trị, chính sách và hạt nhân nhất quán.
- Tiêu đề gọi đúng khái niệm; mã trang, phân tuyến và thời lượng không xuất hiện trên mặt trang chiếu hoặc notes.
- Mọi câu mời tương tác trên mặt trang chiếu dùng nhãn “Câu hỏi:”.

## Rà mạch theo Quill

- Chuỗi Markov → MRP → $G_t$ → $v$ → sao lưu số → Bellman → điều kiện giải → MDP → $P^\pi,r^\pi$ → $v_\pi,q_\pi$ → Bellman kỳ vọng.
- Mỗi hình thức hóa mới có ví dụ, trực giác hoặc tiên quyết ngay trước; không còn nghiệm trước định nghĩa.
- Đã rà hai trang lân cận mỗi phía sau khi gộp B06/B07/C05 cũ và sắp lại D03–D10.
- Không tạo `quill.json`; đây không phải dự án sách.

## Giới hạn và bước tiếp theo

- Cần tác tử độc lập tái rà chính xác toán học và trình tự sau các thay đổi đáng kể.
- Cần điều phối viên rà trực quan bằng Codex Slides và RevealJS ở khung 16:9 và màn hình hẹp.

## Kiểm tĩnh của tác tử chỉnh sửa

- HTML có 39 `data-slide-id` duy nhất: 35 trang chính và 4 trang dọc; cả 39 trang có ghi chú diễn giả và nằm ở độ sâu section đúng mẫu.
- Mọi ID có mục tương ứng trong storyboard; không có mã nội bộ xuất hiện trong nội dung hoặc ghi chú diễn giả.
- 14 đường dẫn CSS, script và hình đều là đường dẫn cục bộ tồn tại; không có tham chiếu raster hoặc URL cốt lõi bên ngoài.
- Bốn SVG phân tích XML được, có `role="img"`, `title`, `desc`; cỡ chữ nhỏ nhất trong SVG là 30 px. Đã kết xuất thử ba đồ thị chính sang PNG tạm để kiểm nhãn và topology; PNG không được đưa vào kho.
- KaTeX phân tích 136 công thức mà không có lỗi; có cảnh báo phông cho chữ tiếng Việt bên trong `\text{...}`, không làm hỏng công thức.
- `git diff --check` không phát hiện lỗi khoảng trắng.

## Sửa sau tái rà độc lập

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Sửa đã áp dụng |
|---|---|---|---|---|
| chặn bàn giao | D09–D10 | Hai cạnh có nhãn Fast→Cool và Slow→Warm không phải self-loop đúng nút. | SVG cũ vẽ hai đường cong sang nút khác dù nhãn mô tả tự lặp. | Vẽ lại hai self-loop; giữ Cool–Fast→Warm, Warm–Slow→Cool và Warm–Fast→Overheated. Sáu kết quả hiện khớp topology, xác suất, thưởng và hai phương trình D10. |
| nghiêm trọng | A00–A02, B00–B01, D00–D01 | Ba cụm trọng tâm đặt hình thức trước ví dụ. | Định nghĩa chuỗi Markov, MRP và MDP xuất hiện trước hình Student tương ứng. | Sắp lại A02→A00→A01, B01→B00 và D01→D00; rà hai trang lân cận và cập nhật storyboard. |
| trung bình | D13, X03, X04, X07, X08 | Notes chứa chỉ dẫn phân bổ hoặc phân tuyến cho người soạn. | Có các cụm “ưu tiên chữa”, “tự luyện” và mô tả nơi lưu phân bổ. | Xóa khỏi notes; giữ talk track và đáp án. Phân bổ chỉ còn trong `note-for-author.md` và planning. |
| trung bình | D06 | Nguồn của hai giá trị tiếp tục được gọi mơ hồ là “đã kiểm”. | Người học không biết $-30/13$ và $35/13$ đến từ đâu. | Nêu trực tiếp $v_\pi(\text{Facebook})$, $v_\pi(\text{C2})$ là dữ kiện đã giải từ Student MDP; notes dẫn trang nguồn 54–55. |
| nhẹ | P02 | Quan hệ ba lớp chưa diễn đạt rõ tính kế thừa thông tin. | Cụm “giữ cấu phần trước” có thể bị hiểu là giữ nguyên tham số hóa. | Đổi thành “kế thừa thông tin của lớp trước và bổ sung phần thưởng hoặc hành động”. |

Sau các sửa trên, số trang và phân bổ tuyến chính giữ nguyên: 35 trang, 120 phút. Không đổi nghiệm số hoặc phạm vi thuật toán.

## Tái rà cuối

- Tác tử toán học–thuật toán xác nhận `racing-car.svg` có đúng hai vòng tự lặp và đủ sáu kết quả; các phương trình D03–D10 vẫn đúng sau khi sắp lại. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Tác tử học thuật–giảng dạy xác nhận ba cụm đã theo thứ tự ví dụ → hình thức, storyboard và hai trang lân cận đã đồng bộ, ghi chú diễn giả không còn chỉ dẫn nội bộ, và tổng tuyến chính vẫn là 120 phút. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.

## Kiểm định cuối của điều phối viên

- `python3 -m reloadserver 8765` đang phục vụ kho tại cổng 8765; trang bài giảng và trang chỉ mục trả HTTP 200.
- HTML có 39 mã trang duy nhất, 39 ghi chú diễn giả và đúng cấu trúc section lồng; mọi mã đều có mục trong storyboard.
- KaTeX dựng được 29 công thức khối và 107 công thức nội dòng, không có lỗi phân tích.
- Bốn SVG hợp lệ về XML, có `role="img"`, `title`, `desc`; cỡ chữ nhỏ nhất là 30 px. Không có tham chiếu ảnh raster hoặc tài nguyên cốt lõi qua mạng.
- Năm tệp HTML/planning đã được tải vào Design Files của dự án Codex Slides `20260824143212-chuy-n-lecture-3-quy-tr-nh-quy-t-nh-mark-w2vu` và đối chiếu trùng từng byte với tệp trong kho.
- Codex Browser không khả dụng trong phiên này. Vì vậy chưa thể xác nhận trực quan từng trang ở khung 1280 × 720, màn hình hẹp, chồng lấn, tràn chữ hoặc thao tác bàn phím trong Codex Slides. Các kiểm tra RevealJS cục bộ và kiểm tra tĩnh vẫn được thực hiện đầy đủ; không tuyên bố đã rà trực quan bằng Codex Slides.

## Hậu kiểm toàn học phần

- Đổi `\text{với mọi }i` thành `\forall i` tại `A01`. Hai biểu thức tương đương; ký hiệu chuẩn loại cảnh báo thiếu metric ký tự tiếng Việt của KaTeX và không đổi nội dung toán học.
