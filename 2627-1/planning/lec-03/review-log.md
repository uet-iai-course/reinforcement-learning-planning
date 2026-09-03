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

- Đổi `\text{với mọi }i` thành `\forall i` tại `A01`. Hai biểu thức tương đương; ký hiệu chuẩn loại cảnh báo thiếu metric ký tự tiếng Việt bên trong `\text{...}` của KaTeX và không đổi nội dung toán học.

## Vòng chỉnh sửa 2026-08-30

### Bằng chứng runtime của các lượt hoàn tất

Mọi lượt hoàn tất dưới đây có `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`:

| Vai | Task profile | Ghi chú lượt lỗi |
|---|---|---|
| planner | plan | — |
| source reader | source | — |
| storyboard reviewer | storyboard | Lượt đầu chạm giới hạn tool-call; lượt hoàn tất dùng `max_rounds=14`. |
| reviewer 1 | góc nhìn sinh viên | — |
| reviewer 2 | chuyên gia Học tăng cường | — |
| reviewer 3 | toán học và thuật toán | — |
| reviewer 4 | phản biện học thuật và giảng dạy | Hai lượt chưa hoàn tất vì giới hạn đầu ra; lượt hoàn tất dùng `max_tokens=16000`. |
| reviewer 5 | kết nối và mạch viết | — |

Các lượt lỗi do giới hạn không được tính là báo cáo độc lập.

### Sáu báo cáo rà soát — vòng 2026-08-30

#### Kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| trung bình | toàn bài | Storyboard mô tả 7 mạch nhưng HTML chỉ có 5 `<section>` ngoài. | Đếm section ngoài trong HTML là 5; storyboard liệt kê 7 mạch. | Tách thành 7 section ngoài. | Đã tách: P; A; B; C; D01–D08; D09–D10; D11–D13 cùng nhánh X. Không đổi mã hay thứ tự trang. |
| nhẹ | B02 | Lý do bỏ hình trang nguồn 37 chưa được ghi. | Outline và storyboard không nêu hình suy giảm mũ. | Ghi lý do bỏ hình. | Đã ghi ở outline, storyboard và notes B02: công thức và ba trường hợp gamma phủ đủ nội dung. |
| nhẹ | A02 | Caption nhắc sớm thưởng và giá trị. | Caption cũ: “Đồ thị, ma trận, thưởng và giá trị dùng cùng thứ tự trạng thái.” | Sửa caption chỉ nói đồ thị và ma trận. | Đã sửa caption A02. |
| nhẹ | D06 | Dữ kiện chưa có cách truy nguyên. | Hai giá trị $-30/13$, $35/13$ xuất hiện không rõ nguồn. | Sửa notes/storyboard chỉ nguồn và cách kiểm. | Đã sửa: notes D06 dẫn trang 54–55, véc-tơ nghiệm đầy đủ và một phương trình Bellman kiểm tại C1. |

#### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| trung bình | C05 | Cỡ hiệu dụng khoảng 0,67em do style lồng `.82em`; số quá dài. | `font-size:.82em` nhân với `.82em` toàn bài. | Bỏ style lồng, rút số trên mặt trang. | Đã bỏ hai `style="font-size:.82em"`; rút nghiệm gamma 0,9 còn 3 chữ số thập phân, số đầy đủ chuyển vào notes. |
| trung bình | D06 | Dữ kiện chưa có cách tái lập. | Người học không sinh được $-30/13$, $35/13$. | Nêu nguồn, nghiệm đầy đủ trong notes và một phép kiểm. | Đã sửa D06 như trên. |
| trung bình | C04 | `$Q$`, `$\rho(Q)$` chưa được định nghĩa. | Ký hiệu xuất hiện lần đầu không có giải thích. | Bổ sung định nghĩa. | Đã bổ sung trong notes C04: $Q$ là ma trận chuyển giới hạn, $\rho$ là bán kính phổ. |
| trung bình | B03, D06, D10 | Đổi $\gamma$ giữa các ví dụ dễ nhầm. | B03 dùng $\gamma=1/2$; D06, D10 dùng $\gamma=1$. | Thêm tín hiệu trong notes nếu không làm mặt trang nặng. | Đã áp dụng: mỗi trang đã nêu giá trị $\gamma$ trên mặt trang; notes B03 nhắc đây là phần thưởng tích lũy từng quỹ đạo, notes D06 và D10 nêu rõ $\gamma=1$. |
| nhẹ | D11 | Bảng nhỏ trên màn hình hẹp. | Bảng ba cột với công thức. | Chờ kiểm render, sửa cục bộ nếu cần. | Chưa sửa; chờ điều phối viên kiểm render hẹp theo quyết định 13 của brief. |
| nhẹ | toàn bài | Viewport và lưới theo template. | Không đổi viewport hay CSS dùng chung. | Kiểm bằng trình duyệt trước khi quyết định. | Không áp dụng ở lượt writer; điều phối viên kiểm tra render hẹp thực tế. |
| nhẹ | D09 | Nhãn Racing Car sát mép. | Nhãn “Slow: p=1; r=+1” và “Fast: p=1; r=−10” gần mép viewBox. | Sửa SVG. | Đã dịch hai nhãn vào trong (`x` 130→185 và 780→770), không đổi sáu kết quả. |

#### Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | A00 | Thiếu phát biểu giả thiết Markov từ nguồn trang 29. | Trang chỉ định nghĩa bộ $\langle\mathcal S,P\rangle$. | Bổ sung phát biểu trên mặt trang. | Đã bổ sung box tính Markov tại A00, dẫn trang 29. |
| trung bình | D06 | Dữ kiện xuất hiện đột ngột. | Không có cầu nối trước hai giá trị. | Xử lý như báo cáo sinh viên. | Đã xử lý: nêu nguồn, chính sách đều ở mọi trạng thái hai hành động, $\gamma=1$, và phép kiểm. |
| trung bình | C04 | Thiếu định nghĩa ký hiệu. | Như báo cáo sinh viên. | Bổ sung. | Đã bổ sung. |
| nhẹ | B02 | Thiếu ý chiết khấu ưu tiên thưởng sớm. | Chỉ nói trọng số giảm. | Bổ sung. | Đã bổ sung trên mặt trang B02 cùng điều kiện hữu hạn khi $\gamma<1$ dưới thưởng bị chặn. |
| nhẹ | student-mdp.svg | `desc` thiếu hành động Quit và tự lặp Facebook. | `desc` cũ không nêu hai hành động từ C1. | Bổ sung. | Đã bổ sung `desc`: Facebook tự lặp thưởng âm một, Quit trở về C1 thưởng không. |

#### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| trung bình | D06 | Cách gọi dữ kiện chưa truy nguyên được. | “Dữ kiện đã giải” mơ hồ. | Sửa cách gọi thành dữ kiện nguồn và chỉ cách kiểm; không đổi số. | Đã sửa; nghiệm nguồn trang 54 exact $(-30,-17,35,96,0)/13$ theo thứ tự Facebook, C1, C2, C3, Sleep được giữ nguyên. |
| nhẹ | D09 | Quy ước Warm–Fast quyết định nghiệm nhưng nằm trong notes. | Nghiệm D10 phụ thuộc việc chọn $-10$. | Đưa quy ước lên mặt trang. | Đã đưa box quy ước lên D09 và nhắc lại trong notes D10. |
| nhẹ | C04 | Lý do khả nghịch chưa chặt. | “Nghịch đảo tồn tại với $P$ hữu hạn” không đủ. | Sửa bằng bán kính phổ. | Đã sửa: $\rho(\gamma P)\le\gamma<1$ trên mặt trang; giữ điều kiện đủ thực hành trong notes. |
| nhẹ | student-mdp.svg | `desc` thiếu. | Như báo cáo chuyên gia RL. | Bổ sung. | Đã bổ sung. |

#### Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | D06 | Thiếu cầu nối dữ kiện. | Hai giá trị tiếp tục xuất hiện không có nguồn và cách kiểm. | Xử lý bằng nguồn + nghiệm đầy đủ + một phương trình kiểm, không thêm trang. | Đã xử lý đúng phương án; không thêm trang. |
| trung bình | D09, D10 | Quy ước thưởng nằm sai chỗ. | Quy ước quyết định nghiệm chỉ có trong notes D09. | Đưa lên slide D09 và notes D10. | Đã thực hiện. |
| trung bình | C04 | Ký hiệu chưa định nghĩa. | Như hai báo cáo trước. | Bổ sung. | Đã bổ sung. |
| trung bình | C05 | Chưa nêu biên trên mặt trang. | Nghiệm gamma 1 cần biên $v(\text{Sleep})=0$. | Bổ sung. | Đã nêu “$v(\text{Sleep})=0$ ở cả hai trường hợp” trên mặt trang C05. |
| trung bình | A05 | Dùng $\mu_t$ trước định nghĩa. | Câu hỏi dùng $\mu_t$ chưa giải thích. | Bổ sung định nghĩa trước câu hỏi. | Đã bổ sung: $\mu_t$ là phân phối trạng thái dạng véc-tơ cột, phần tử thứ $i$ là $\Pr(S_t=s_i)$. |
| trung bình | C06→D01 | Thiếu vấn đề cần hành động. | C06 kết thúc MRP; D01 vào MDP không nêu giới hạn của MRP. | Bổ sung D01. | Đã bổ sung câu mở D01: MRP không biểu diễn lựa chọn hành động. |

#### Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| trung bình | toàn bài | 7 mạch storyboard không khớp 5 section HTML. | Đếm section ngoài. | Tách 7 section. | Đã tách; vai trò này cần tái rà các trang bị ảnh hưởng, hai trang lân cận mỗi phía và mọi ranh giới phần. |
| trung bình | D06 | Bước nhảy dữ kiện. | Như các báo cáo trước. | Xử lý. | Đã xử lý. |
| nhẹ | D09–D10 | Thiếu tín hiệu đây là mạch ứng dụng mới. | Không có câu nối từ D08 sang D09. | Thêm câu nối notes/storyboard. | Đã thêm câu nối trong notes D09 và storyboard. |
| nhẹ | D12 | Chưa thu hồi đủ mục tiêu. | Tự kiểm thiếu kiểm ma trận và MRP cảm sinh. | Bổ sung. | Đã bổ sung hai mục 5–6 vào D12 bằng lưới hai cột, giữ trang đọc được. |

### Quyết định của điều phối viên — áp dụng

1. Tách 7 section ngoài: đã thực hiện, giữ 39 mã trang và thứ tự.
2. Phát biểu Markov ở A00: đã bổ sung; giữ A02 trước A00.
3. Caption A02: đã sửa.
4. Định nghĩa $\mu_t$ ở A05: đã bổ sung trước câu hỏi.
5. B02: đã bổ sung ý ưu tiên thưởng sớm và điều kiện hữu hạn; lý do bỏ hình trang 37 đã ghi ở outline, storyboard, notes.
6. C04: đã định nghĩa $Q$, $\rho$; sửa lý do khả nghịch thành $\rho(\gamma P)\le\gamma<1$; điều kiện đủ thực hành giữ trong notes.
7. C05: đã bỏ cỡ chữ lồng, rút 3 chữ số thập phân, nêu $v(\text{Sleep})=0$ và giải hệ con khi $\gamma=1$.
8. D01: đã bổ sung vấn đề lựa chọn hành động; `desc` student-mdp.svg đã bổ sung tự lặp Facebook và Quit.
9. D06: không thêm trang; đã sửa thành dữ kiện nguồn trang 54, chính sách đều mọi trạng thái hai hành động, $\gamma=1$; véc-tơ nghiệm đầy đủ và phép kiểm Bellman trong notes. Storyboard ghi bước giải hệ đầy đủ được lược nhưng dữ kiện truy nguyên và kiểm được.
10. D09: quy ước thưởng đã lên mặt trang; notes D10 nhắc lại; nhãn SVG đã dịch khỏi mép, không đổi sáu kết quả.
11. D12: đã bổ sung kiểm ma trận/hấp thụ và MRP cảm sinh bằng lưới hai cột.
12. Không thêm nhãn “Tự luyện” lên X07; phân bổ chỉ giữ trong planning. Notes X07 chỉ chứa gợi ý lời giải và nguồn.
13. Không đổi viewport hay CSS dùng chung ở lượt writer.
14. Đã bỏ script `plugin/markdown/markdown.js` và `RevealMarkdown` khỏi danh sách tiện ích.
15. Giữ toàn bộ phép tính hiện có, gồm nghiệm nguồn trang 54 exact $(-30,-17,35,96,0)/13$.

### Đề xuất không áp dụng

- Không thêm nhãn “Tự luyện” hiển thị trên X07: AGENTS cấm hiển thị nhãn phân tuyến trên slide hoặc notes.
- Không đổi viewport, `lecture-style.css` hay template: theo quyết định 13 của brief; điều phối viên kiểm render hẹp rồi quyết định.
- Không sửa bảng D11 cho màn hình hẹp ở lượt này: chờ kết quả kiểm render thực tế.

### Nhu cầu tái rà sau sửa

- Vai kết nối và mạch viết cần rà lại các trang bị ảnh hưởng, hai trang lân cận mỗi phía và mọi ranh giới phần sau khi tách 7 section ngoài: ranh giới C→D01, D08→D09, D10→D11.
- Vai toán học–thuật toán cần tái rà C04, C05, D06 vì nội dung toán học hiển thị đã đổi đáng kể (bán kính phổ, rút số, phép kiểm mới).
- Điều phối viên cần kiểm render hẹp cho D11 và toàn trang ở khung 1280 × 720 trước khi quyết định sửa cục bộ tiếp theo.

### Sửa từ kiểm định hiển thị của điều phối viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Sửa đã áp dụng |
|---|---|---|---|---|
| nghiêm trọng | C05 | Véc-tơ phân số của nghiệm $\gamma=1$ bị cắt trong thẻ bên phải. | Ảnh chụp Chromium ở cả 1280 × 720 và 800 × 600 cho thấy phần cuối véc-tơ nằm ngoài vùng nhìn thấy của thẻ; phép kiểm overflow theo phần tử con không bắt được tràn nội bộ này. | Mặt trang hiển thị cả hai nghiệm với ba chữ số thập phân; véc-tơ $\gamma=1$ ngắt thành hai dòng, còn nghiệm phân số chính xác chuyển vào notes. Không đổi giá trị toán học. Yêu cầu render và tái rà toán lại C05. |

Nguyên nhân CSS là cột `1fr` nhận chiều rộng tối thiểu từ công thức dài và đẩy cột kế tiếp ra khỏi khung. Sửa cục bộ `.grid2` của riêng bài thành `repeat(2,minmax(0,1fr))`; không sửa `lecture-style.css` dùng chung.

### Tái rà toán học và mạch viết sau sửa

Các lượt hoàn tất dưới đây đều có `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.

- Lượt toán đầu nêu lỗi nghiêm trọng D06 vì bỏ sót nhánh Study $+10$ tại C3. Điều phối viên bác bỏ bằng phép thế đầy đủ; lượt xác nhận độc lập thứ hai kiểm cả bốn phương trình Bellman và kết luận véc-tơ $(-30,-17,35,96,0)/13$ đúng. Cụ thể tại C3: $96/13=\tfrac12(10)+\tfrac12(1+49/13)$.
- Lượt mạch viết xác nhận đúng 7 section ngoài; các ranh giới C06→D01, D08→D09, D10→D11 và việc D12–D13 thu hồi mục tiêu đều đạt.
- Báo cáo mạch nêu D10 sai do giả định Warm–Fast còn một nhánh tiếp diễn xác suất 0,5. Đối chiếu nguồn trang 51 và `racing-car.svg` cho thấy Warm–Fast có đúng một kết quả xác suất 1 đi Overheated; Warm–Slow mới có hai kết quả xác suất 0,5. Vì vậy giữ $v(W)=-4{,}5+0{,}25v(C)+0{,}25v(W)$ và nghiệm $(0,-6)$.
- Báo cáo mạch phát hiện đúng notes D01 gán Facebook/Quit cho C1. Đã sửa: C1 có Facebook/Study; trạng thái Facebook có Facebook/Quit. Đồng bộ `student-mdp.svg` và làm rõ D06 là chính sách đều trên các hành động khả dụng tại mỗi trạng thái.

Các lượt không hoàn tất không được tính: ba lượt sandbox lỗi vận chuyển API; một lượt nạp nhật ký quá dài bị hủy; một lượt phạm vi hẹp bị cắt ở 7.000 token. Tiến độ JSONL cho phép điều phối viên phát hiện và điều chỉnh phạm vi, `max_tokens` và quyền mạng trước khi chạy lại.

### Kiểm định cuối 2026-08-30

- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Phương án thay thế dùng `python3 -m http.server 8765` trên webroot tạm chỉ chứa HTML Bài 03, CSS, 4 SVG và thư viện RevealJS/KaTeX cục bộ; `.env` không được sao chép hoặc phục vụ.
- Chromium headless duyệt đủ 39 trang ở 1280 × 720 và 800 × 600. Cả hai khung: 0 lỗi console, 0 request hỏng, 0 trang bị bộ đo tràn đánh dấu. Điều hướng bàn phím kiểm được P00 ↓ P01, ↑ P00, → A02.
- Kiểm ảnh trực tiếp phát hiện C05 bị cắt dù bộ đo tràn không báo. Sau khi làm tròn mặt trang, ngắt hai véc-tơ thành hai dòng và đổi lưới cục bộ thành `repeat(2,minmax(0,1fr))`, ảnh cuối ở cả hai khung không còn cắt hoặc chồng lấn. Nghiệm đầy đủ và phân số chính xác giữ trong notes.
- Kiểm tĩnh cuối: 7 section ngoài; 39 `data-slide-id` duy nhất; 39 notes; mọi ID có trong storyboard; 4 SVG hợp lệ XML, có `role="img"`, `title`, `desc`; không ảnh raster, URL cốt lõi ngoài, tài nguyên hỏng hoặc `RevealMarkdown`; `git diff --check` sạch. `index.html` có đúng liên kết tới bài giảng.
- Tự kiểm theo `no-ai-slop/eval.md`: nội dung hiển thị và notes không có câu hỏi tu từ, lời ca tụng/quảng bá, lời dẫn rỗng, kết luận lặp hoặc nhãn phân tuyến. Rà theo Quill xác nhận 7 mạch có điểm vào–ra, thứ tự ví dụ → hình thức và kết luận thu hồi mục tiêu; không tạo `quill.json`.
- Codex Slides: `get_project` xác nhận dự án `20260824143212-chuy-n-lecture-3-quy-tr-nh-quy-t-nh-mark-w2vu` vẫn ở trạng thái `draft`, checkpoint `clarify`, 0 slide. Bốn Design Files HTML/outline/storyboard/review-log đã được ghi lại và đọc lại khớp chính xác với tệp trong kho tại thời điểm đồng bộ. Codex in-editor Browser không khả dụng trong phiên, nên không tuyên bố đã kiểm trực quan bằng Codex Slides; kiểm trực quan RevealJS cục bộ bằng Chromium là bằng chứng hiển thị cuối.

## Giai đoạn I — lecture note, 2026-09-03

### Phạm vi và bằng chứng runtime

- Tệp nguồn chính: `lecture2-3-MDPswithKeyConcepts.pptx`, trang 28–58; bài tập: `hw02.pdf`, Bài 3, 4, 7, 8. Bài 9 chuyển sang Bài 04.
- Writer bản đầu: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, profile `write`, `max_rounds=12`, timeout 600 giây, 28.000 token; hoàn tất ở vòng 3.
- Hai reviewer sinh viên và mạch viết: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Ba reviewer chuyên gia Học tăng cường, toán học–thuật toán và học thuật–giảng dạy: `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Reviewer toán hợp lệ đọc toàn bộ note trong một tool call, profile `review`, `max_rounds=4`, timeout 600 giây, 12.000 token; hoàn tất ở vòng 2. Các lượt nhiều tệp chạm giới hạn 5, 8, 12 vòng hoặc timeout 300 giây không được tính là báo cáo.
- Writer vá cục bộ và bổ sung bản đồ chủ đề đều dùng đúng `z-ai/glm-5.3-flash`/OpenRouter; các lượt hoàn tất dùng 4–5 vòng. Liên kết `.env` chỉ tồn tại trong lúc cầu nối nạp khóa, bị MCP chặn đọc và được gỡ ngay sau mỗi đợt.

### Năm báo cáo độc lập

| Vai | Mức độ | Vị trí | Vấn đề và bằng chứng | Đề xuất / quyết định |
|---|---|---|---|---|
| Góc nhìn sinh viên | nghiêm trọng | `lec-03-topic-01`, `lec-03-topic-03` | Hàng C3 và quỹ đạo không khớp đồ thị; quỹ đạo Facebook tính $G_0=-3{,}875$ trái véc-tơ thưởng. | Thêm toàn bộ $P$, sửa C3 sang Pass/Pub, sửa $G_0=-3{,}125$. Đã áp dụng. |
| Chuyên gia Học tăng cường | trung bình | `lec-03-topic-07`, `lec-03-topic-09`, deck D01–D10 | Báo cáo chủ yếu xác nhận note đã bổ sung các công thức bị ẩn trong ảnh nguồn: hạt nhân chung, MRP cảm sinh và Bellman kỳ vọng. | Giữ note; chuyển các đề xuất chỉ dành cho deck sang Giai đoạn II. Không tính là lỗi note. |
| Toán học–thuật toán | nghiêm trọng | `lec-03-topic-03`, `lec-03-topic-05` | Tính lại xác nhận $G_0=-3{,}125$; recheck phát hiện phép nhìn trước dùng hàng C2 nhưng ghi C3. | Sửa số và nhãn thành C2; recheck cuối xác nhận phép tính $0{,}88$ đúng và hết lỗi nghiêm trọng. |
| Học thuật–giảng dạy | trung bình | `lec-03-topic-07`, `lec-03-topic-11` | Ví dụ số $q_\pi$ thiếu cách truy nguyên; hạt nhân chung cần trực giác trước công thức. | Dùng dữ kiện phân số từ nguồn/deck và đặt Student MDP trước định nghĩa hạt nhân. Đã áp dụng. |
| Kết nối và mạch viết | chặn bàn giao | `lec-03-topic-03`, `lec-03-topic-05` | Số $G_0$ sai lan sang topic 04; ví dụ nhìn trước đặt sau công thức; bản đồ nguồn thiếu tín hiệu bốn nhóm. | Sửa số, đưa ví dụ trước Bellman, thêm bản đồ đủ `cốt lõi`, `cầu nối`, `bổ sung`, `đọc thêm`. Recheck toàn note xác nhận 13 mã khớp 13 marker và không còn lỗi bắt buộc. |

### Quyết định chỉnh sửa và sai khác có chủ ý

- Student MRP dùng đúng thứ tự C1, C2, C3, Pass, Pub, Facebook, Sleep và ma trận trong `student-mrp.svg`. Nghiệm $\gamma=0{,}9$ được tính lại thành $(-5{,}013,0{,}943,4{,}087,10,1{,}908,-7{,}638,0)$.
- Student MDP là đặc tả khác Student MRP. Tại C3, hành động Study đi tới Sleep và nhận $+10$; Pub nhận $+1$ rồi qua nút ngẫu nhiên. Không áp dụng đề xuất đổi C3–Study sang Pass vì trái `student-mdp.svg` và deck đã kiểm định.
- Dữ kiện chính sách đều, $\gamma=1$: $v_\pi(\text{Facebook})=-30/13$, $v_\pi(\text{C2})=35/13$, $q_\pi(\text{C1,Facebook})=-43/13$, $q_\pi(\text{C1,Study})=9/13$, $v_\pi(\text{C1})=-17/13$.
- Racing Car giữ sáu kết quả trong `racing-car.svg`; chuyển vào Overheated nhận $-10$ thay cho $+2$ và kết thúc. Dưới chính sách đều ở Cool: $P^\pi_{C,W}=0{,}25$, $P^\pi_{C,C}=0{,}75$, $r^\pi(C)=1{,}5$.
- Không thêm Bellman tối ưu, lặp giá trị, lặp chính sách, code demo hoặc ví dụ ngoài nguồn.
- Thẻ Bài 03 trên `index.html` có hai liên kết Bài giảng/Ghi chú. Đây là ngoại lệ có chủ ý thay quy tắc một liên kết duy nhất trong `AGENTS.md`, do `prompt_lecture_note_deck.md` yêu cầu trực tiếp.

### Recheck và biên tập

- Recheck toán toàn note xác nhận ma trận, hai $G_0$, nghiệm Student, điều kiện $\gamma=1$, Racing Car, $P^\pi/r^\pi$, các phân số $q_\pi/v_\pi$ và Bellman kỳ vọng. Recheck hẹp cuối xác nhận lỗi C2/C3 đã hết.
- Recheck mạch toàn note xác nhận đủ bốn nhóm, 13 mã trong bản đồ khớp 13 marker, trình tự chuỗi Markov → MRP → $G_t$ → $v$ → Bellman → MDP → chính sách → MRP cảm sinh → $v_\pi,q_\pi$ → Bellman kỳ vọng, và mở–kết nhất quán.
- Tự kiểm theo `no-ai-slop/eval.md`: bỏ lặp ý, nhịp “là hợp lý”, từ mang phán xét và thuật ngữ mơ hồ. Rà theo Quill giữ vai trò, kết nối vào–ra và thứ tự trực giác → hình thức; không tạo `quill.json`.

### Kiểm định công bố Giai đoạn I

- Lệnh bắt buộc `python3 -m reloadserver 8765` đã được thử và thất bại với `/usr/bin/python3: No module named reloadserver`.
- Phương án thay thế dùng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm cô lập. Webroot chỉ chứa index, viewer, note/deck Bài 03, CSS, SVG và thư viện cục bộ cần thiết; không chứa `.env`, planning hoặc nguồn.
- Chromium headless chụp material-viewer ở 1280 × 720 và 800 × 600; note hiển thị đúng, bố cục hẹp chuyển thành một cột. Cảnh báo thiếu phông DejaVu của Chromium không làm mất chữ hoặc công thức.
- DOM sau render: tiêu đề đúng; layout hiển thị; trạng thái lỗi ẩn; 342 phần tử KaTeX; 0 `katex-error`; 26 khối `details`; marker `note-topic-id` không lộ; liên kết deck và Markdown đúng.
- `index.html` có đúng liên kết deck và viewer của Bài 03, không có liên kết planning. Viewer chặn cặp doc/deck lệch số bài và ẩn layout nội dung.
- Kiểm bàn phím qua Chrome DevTools Protocol: sáu lần Tab lần lượt đặt tiêu điểm vào liên kết bỏ qua điều hướng, danh mục học phần, bộ trang chiếu, Markdown gốc và hai liên kết mục lục đầu. Viewer dùng được không cần chuột.
- Playwright không chạy vì gói hiện có yêu cầu Node ≥20 còn môi trường là Node 18.19.1; kiểm Chromium trực tiếp và DevTools Protocol thay thế. Codex Slides/Browser vẫn không khả dụng, nên không tuyên bố đã rà bằng Codex Slides.

## Giai đoạn II — slide deck, 2026-09-03

### Kế hoạch, ánh xạ và runtime

- Reader lập kế hoạch trên gói bốn tệp cô lập: `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`, profile `plan`, `max_rounds=8`, timeout 600 giây, 12.000 token. Điều phối viên sửa hai sai số trong báo cáo: deck có 39, không phải 40 mã; X03 ánh xạ cả topic01 và topic06.
- Outline và storyboard chứa ánh xạ nhiều–nhiều đủ 13 `note-topic-id` và 39 `data-slide-id`; P00–P01 tạo khung cho cả bài, P02 nối topic01, topic02, topic07 và topic13.
- Writer đồng bộ ban đầu: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, profile `write`, `max_rounds=10`, timeout 600 giây, 16.000 token. Writer chỉnh sửa sau review chạm `model exceeded the tool-call limit (12)` sau khi ghi bán phần; điều phối viên kiểm diff và chạy writer vá hai chuỗi với cùng model, `max_rounds=6`, timeout 300 giây, 6.000 token. Không đổi model.

### Năm báo cáo độc lập

| Vai | Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa / quyết định |
|---|---|---|---|---|---|
| Góc nhìn sinh viên | trung bình | B01 | Quy ước thưởng diễn đạt là “rời” trạng thái, trái $R_{t+1}=r(S_t)$. | B01 nói “Rời C1”; B00 và lecture note gắn thưởng với trạng thái hiện tại. | Đổi thành “Ở C1/Pass/Sleep”; notes dùng đúng quy ước. Đã áp dụng. |
| Góc nhìn sinh viên | trung bình | C04–C06 | Bán kính phổ trên mặt trang tạo tải nhận thức sớm. | C04 đặt cả $\rho(\gamma P)$ và $\rho(Q)$ trên hai thẻ. | Mặt trang giữ điều kiện thực hành; chứng minh phổ và $Q$ giữ trong notes. Đã áp dụng. |
| Chuyên gia Học tăng cường | trung bình | D06 | Báo cáo cho rằng thiếu giải thích $q_\pi$. | Bản được rà đã có notes: thưởng đầu cộng giá trị kế tiếp vì $\gamma=1$ và chuyển đầu tất định. | Không áp dụng; đề xuất đã được đáp ứng trước lượt rà. |
| Chuyên gia Học tăng cường | trung bình | D10 | Cần nêu điều kiện hữu hạn khi $\gamma=1$. | Notes đã nói chính sách kết thúc gần như chắc chắn và kỳ vọng thời gian hữu hạn. | Giữ điều kiện; bổ sung cách tạo hai hệ số và phản ví dụ chính sách Slow đầy đủ. |
| Toán học–thuật toán | nghiêm trọng | A05 | Báo cáo đầu cho rằng $\mu_{t+1}=P^{\mathsf T}\mu_t$ sai. | A00 định nghĩa $P_{ij}=\Pr(S_{t+1}=s_j\mid S_t=s_i)$ theo hàng; A05 định nghĩa $\mu_t$ là véc-tơ cột. | Bác đề xuất: với hai quy ước này, $P^{\mathsf T}\mu_t$ là đúng. Recheck DeepSeek xác nhận. |
| Toán học–thuật toán | trung bình | D10 | Hệ số $1{,}5$ và $-4{,}5$ chưa được khai triển. | Mặt trang chỉ có hệ Bellman. | Notes thêm $0{,}5\times1+0{,}5\times2$ và $0{,}5\times1+0{,}5\times(-10)$; nêu số hạng Overheated có giá trị tiếp tục 0. |
| Học thuật–giảng dạy | trung bình | C05 | Cần nói rõ biên và hệ con khi $\gamma=1$. | Notes hiện có $v(\text{Sleep})=0$, giải hệ con và nói $I-P$ toàn cục suy biến. | Không áp dụng thêm; đề xuất đã được đáp ứng. |
| Học thuật–giảng dạy | nhẹ | P01 | Mục tiêu “đúng điều kiện” chưa gọi tên hai trường hợp. | P01 chưa nêu $\gamma<1$ và $\gamma=1$. | Gọi rõ hai trường hợp; notes nhắc tiên quyết. Đã áp dụng. |
| Kết nối và mạch viết | trung bình | B01 | Cùng lỗi quy ước thưởng với vai sinh viên. | B01 trái B00 và note. | Đã sửa. |
| Kết nối và mạch viết | nhẹ | outline, X07–X08 | Ánh xạ nguồn chồng dải; nhánh bài tập có thể trông lặp chức năng. | C00 ghi nguồn 44–46; X07/X08 yêu cầu lại quan hệ đã học. | Chuyển C00 sang hàng 44–48; notes nêu yêu cầu tự suy diễn trước khi đối chiếu. |

Ba lượt DeepSeek đầu với `max_rounds=8` và lượt toán bốn tệp với `max_rounds=12` không được tính vì dừng ở `model exceeded the tool-call limit`. Báo cáo hợp lệ đều có `requested_model=observed_model=deepseek/deepseek-v3.2` hoặc `z-ai/glm-5.3-flash` đúng phân vai, `provider=OpenRouter`.

### Chỉnh sửa, đề xuất không áp dụng và tái rà

- B01, P01, P02, C04, D04, D10, X07–X08, bảng ánh xạ nguồn và câu điều kiện $\gamma=1$ trong lecture note đã được sửa tuần tự. Không đổi số trang, thứ tự, SVG, công thức hoặc số liệu cốt lõi.
- Giữ hai nghiệm C05 làm tròn ba chữ số trên mặt trang; notes giữ số đầy đủ và phân số chính xác. Không tăng số chữ số vì làm giảm khả năng đọc mà không tăng ý nghĩa sư phạm.
- Không thêm Bài tập 5–6 và không đánh lại số X03, X04, X07, X08: số bài truy nguyên trực tiếp `hw02.pdf`; Bài 9 đã chuyển sang Bài 04.
- Giữ B01 trước B00, A02 trước A00 và D03 trước D04: đây là chủ ý ví dụ trước định nghĩa, đã ghi trong storyboard.
- Recheck toán: `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`, profile `recheck`, `max_rounds=6`, timeout 600 giây, 9.000 token. Kết luận không còn lỗi chặn/nghiêm trọng; xác nhận A05, C04–C06, D04–D06 và D09–D10 đúng.
- Recheck mạch: `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, cùng cấu hình. Kết luận đúng 7 section ngoài; các ranh giới A05→B01, B04→C00, C06→D01, D10→D11, D13→X03 liền mạch; không còn lỗi chặn/nghiêm trọng.
- Tự kiểm theo `no-ai-slop/eval.md`: bỏ câu quy trình bị lộ trong notes X07, giữ câu ngắn và không dùng khẩu hiệu, câu hỏi tu từ hoặc nhãn phân tuyến. Rà theo Quill xác nhận tuyến chuỗi Markov → MRP → Bellman → MDP → đánh giá chính sách → ứng dụng → tổng kết; không tạo `quill.json`.

### Kiểm định cuối Giai đoạn II

- Kiểm tĩnh: 7 `<section>` ngoài; 39 `data-slide-id` duy nhất; 35 trang tuyến chính và 4 trang dọc; 39 notes; mọi ID và 13 topic có trong outline/storyboard. Bốn SVG hợp lệ XML, có `role="img"`, `title`, `desc`; không có ảnh raster, URL cốt lõi ngoài, tài nguyên thiếu, `.env` hoặc `quill.json`. `git diff --check` sạch.
- Lệnh bắt buộc `python3 -m reloadserver 8765` thất bại với `/usr/bin/python3: No module named reloadserver`. Máy chủ thay thế dùng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm cô lập, không chứa `.env`, planning hoặc nguồn.
- Chromium headless duyệt đủ 39 trang ở 1280 × 720 và 800 × 600. DOM cuối có 171 phần tử KaTeX, 0 `katex-error`, 0 request hỏng và 0 lỗi trang. Lỗi 404 duy nhất ở lượt đầu là yêu cầu tự động `/favicon.ico`, không phải tài nguyên được deck tham chiếu.
- Điều hướng bàn phím cuối: P00 ↓ P01, ↑ P00, → A02. Cả bốn nhánh dọc được duyệt trong danh sách 39 trang.
- Kiểm ảnh trực tiếp phát hiện D04 bị cắt ngang sau khi thêm ngoặc. Writer GLM ngắt $r^\pi(s)$ thành hai dòng, không giảm cỡ chữ; render lại ở hai khung cho thấy công thức nằm trọn trong thẻ. Phép đo biên ở 1280 × 720: thẻ phải từ 651,6 đến 1254,4 px, công thức từ 672,4 đến 1233,6 px; ở 800 × 600, công thức từ 420,2 đến 771,0 px trong thẻ từ 407,2 đến 784,0 px.
- Recheck D04 cuối: `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`, profile `recheck`, `max_rounds=4`, timeout 300 giây, 5.000 token. Xác nhận $r^\pi(s)=\sum_a\sum_{s'}\sum_r\pi(a\mid s)p(s',r\mid s,a)r$, $P^\pi$ và Bellman MRP cảm sinh đều đúng.
- Codex Slides/Browser không khả dụng trong phiên do môi trường Node 18 không đáp ứng gói yêu cầu Node ≥20. Không tuyên bố đã rà trực quan bằng Codex Slides; kiểm trực quan RevealJS cục bộ bằng Chromium là bằng chứng cuối.
