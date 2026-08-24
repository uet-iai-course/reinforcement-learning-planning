# Nhật ký rà soát Bài 05

## Lỗi nguồn và bản nháp đã xử lý trước phản biện độc lập

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| chặn bàn giao | A04–A06 | Nguồn trộn quy tắc lần ghé với quy tắc bước học. | “Lần ghé đầu tiên”, “trung bình mẫu” và “alpha hằng” không cùng một trục. | Dùng ma trận $2\times2$ và ghi đủ hai lựa chọn. | đã xử lý ở A05–A06 |
| nghiêm trọng | A03–A06 | Ví dụ thiếu quy tắc lần ghé và thứ tự cập nhật. | Các trang nguồn không mở từng phép tính. | Tính lại hai lượt và nêu quy ước tại chỗ. | đã xử lý |
| nghiêm trọng | B06–B07 | Thiếu cầu nối từ cập nhật mẫu sang hội tụ; bản sửa đầu dùng tính co cả khi $\gamma=1$. | $T^\pi$ chưa được định nghĩa; $\gamma=1$ không co nghiêm trong chuẩn vô cùng. | Định nghĩa $T^\pi$; tách nhánh chiết khấu và nhánh kết thúc hấp thụ. | đã xử lý |
| chặn bàn giao | C01 | Số mũ của quỹ đạo dài sai. | Nguồn ghi $0{,}99^4$ và $-0{,}99^2$. | Dùng $\gamma^3=0{,}970299$ và $-\gamma=-0{,}99$. | đã xử lý |
| nghiêm trọng | B06,C03 | Nguồn xếp hạng phương sai và tốc độ quá mạnh. | Thiếu giả thiết để kết luận phổ quát. | Nêu cơ chế có điều kiện, không xếp hạng tuyệt đối. | đã xử lý |

## Bốn báo cáo độc lập sau bản nháp

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | A03,B02 | Thuật toán chưa đủ để sinh viên tự chạy. | Chỉ có quy tắc cập nhật cục bộ. | Thêm đầu vào, khởi tạo, vòng lặp, dừng và đầu ra. | đã xử lý ở A02,B02 |
| nghiêm trọng | B07 | Điều kiện hội tụ vượt tiên quyết. | Chưa giải thích Robbins–Monro, đúng đắn và quá độ. | Dùng câu “học mãi nhưng bước nhỏ dần”; định nghĩa thuật ngữ bằng tiếng Việt. | đã xử lý |
| trung bình | A02–A07 | Oracle đặt sớm; mọi lần ghé làm quá tải tuyến chính. | Người học chưa tạo ước lượng đầu tiên. | Đặt oracle sau A03; dành A06 cho vùng đệm. | đã xử lý |
| trung bình | B01,C02,C03 | Tiêu đề sai vai trò; đổi bối cảnh thiếu báo hiệu; mô tả chệch chưa rõ. | $G_t$ không mới với TD; C02 quay lại lượt ngắn. | Đổi tiêu đề; chốt dữ kiện C02; nêu nguồn ngẫu nhiên và phần đuôi xấp xỉ. | đã xử lý |
| trung bình | P02,C07,D01 | Câu hỏi không có đáp án trên mặt trang. | Đáp án chỉ ở ghi chú. | Thêm đáp án hiện dần. | đã xử lý |
| trung bình | A06,B03,B04 | Bảng năm cột sát ngưỡng máy chiếu. | Cỡ hiệu dụng ban đầu xấp xỉ $0{,}75$ em. | Giữ cỡ $0{,}754$ em, rút chữ; chuyển A06 khỏi tuyến lõi. | đã xử lý; cần rà trực quan cuối |
| trung bình | X07 | Lặp lại bài đã giải. | Hai lượt và kết quả đã xuất hiện trong tuyến chính. | Chuyển sang giải thích vì sao ba kết quả khác nhau. | đã xử lý |

### Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | A03,B02 | MC và TD chưa có luồng thuật toán tái tạo được. | Thiếu giao diện, vòng lượt/chuyển và chi phí. | Bổ sung giả mã tối thiểu và quy ước terminal. | đã xử lý ở A02,B02 |
| trung bình | C03–C04 | Cơ chế chệch–phương sai quá dè dặt. | Chưa nói $G_t$ tích lũy nhiều nguồn ngẫu nhiên. | So phần đuôi quỹ đạo với phần đuôi $V_t$. | đã xử lý |
| trung bình | A04,A07 | Oracle và điều kiện độc lập cần rõ hơn. | Oracle đứng trước ước lượng; “độc lập” chưa gắn với lượt khởi động lại. | Đổi thứ tự; ghi các lượt độc lập dưới cùng $\pi$. | đã xử lý |
| trung bình | B05,C02 | Hai trang gần trùng. | Cùng nói thời điểm cập nhật. | Biến C02 thành phép áp dụng có đủ $\gamma,\alpha,V_0$. | đã xử lý |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | A03,B02 | Thiếu $\pi,\gamma$, bộ sinh dữ liệu, lịch bước học, khởi tạo, terminal, dừng, đầu ra và chi phí. | Quy tắc cục bộ không xác định thuật toán. | Nêu đủ giao diện và độ phức tạp; không trộn $\alpha$ hằng với Robbins–Monro. | đã xử lý ở A02,B02 |
| trung bình | B07 | Tổng bước học dùng chỉ số thời gian mơ hồ. | Điều kiện phải theo lần cập nhật riêng của $s$. | Dùng $\alpha_n(s)$, $0<\alpha_n\le1$, ví dụ $1/n$; khởi động lại lượt khi $\gamma=1$. | đã xử lý |
| trung bình | B06 | $T^\pi$ chưa được định nghĩa. | Chỉ có ký hiệu trong kỳ vọng. | Viết tổng theo $a,s',r$ và giữ $V_t$ cố định. | đã xử lý |
| nhẹ | C02 | Thiếu dữ kiện để kết quả là duy nhất. | Chưa chốt $\gamma,\alpha,V_0$. | Ghi $\gamma=1$, $\alpha=0{,}5$, bảng 0. | đã xử lý |

Reviewer toán xác nhận các kết quả số MC, TD và quỹ đạo dài hiện có là đúng.

### Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | A03–A06 | Chưa áp dụng trọn MC lần ghé đầu với trung bình mẫu. | Thiếu $(1,1)$ sau $e_1$ và $(0,0)$ sau $e_2$. | Hoàn tất trung bình mẫu trước khi so $\alpha$ hằng và mọi lần ghé. | đã xử lý ở A03–A06 |
| nghiêm trọng | A03,B02 | Thuật toán thiếu đầu–cuối. | Công thức đúng riêng lẻ nhưng chưa nằm trong vòng học. | Đặt công thức vào giao diện và vòng lặp đầy đủ. | đã xử lý |
| nghiêm trọng | B06–B07 | Công thức Bellman và hội tụ thiếu cầu nối sư phạm. | Nhảy từ mẫu sang định lý và dùng thuật ngữ chưa giải thích. | Định nghĩa $T^\pi$; giải thích Robbins–Monro, đúng đắn và quá độ. | đã xử lý |
| trung bình | A02,C00–C04 | Oracle sai trình tự; đổi bối cảnh và cơ chế chệch–phương sai chưa liền mạch. | Hình thức hóa đúng nhưng đặt trước thao tác học; C02 đổi ví dụ ngầm. | Đặt oracle sau A03; đổi tiêu đề C02; nối phần đuôi ngẫu nhiên với $V_t$. | đã xử lý |
| trung bình | toàn bài | Tuyến 120 phút không có dự phòng. | Mọi nội dung đều được tính bắt buộc. | Chốt tuyến lõi 108 phút và vùng đệm 12 phút. | đã xử lý trong storyboard và ghi chú tác giả |

## Quyết định chỉnh sửa

- Nhận toàn bộ đề xuất nghiêm trọng của bốn báo cáo.
- Nhận đề xuất chuyển A06 và chi tiết $\gamma=1$ thành vùng đệm; không xóa vì chúng sửa hai chỗ dễ gây hiểu sai trong nguồn.
- Không tách B03–B04 thành nhiều trang: bảng đã rút chữ, cỡ hiệu dụng theo CSS là khoảng $0{,}754$ em và mỗi bảng chỉ có ba đến bốn hàng. Việc chấp nhận cuối cùng phụ thuộc rà trực quan.
- Giữ C04 sau C03: C03 giải thích cơ chế chệch–phương sai, C04 chuyển cơ chế đó thành tiêu chí chọn phương pháp; hai trang không còn cùng luận điểm.
- Không thêm code demo vì nguồn không có nội dung tương ứng.

## Sai khác có chủ ý so với nguồn

- Lược 14 trang ôn MDP và quy hoạch động đã học ở Bài 04.
- Đưa lượt/chuyển mẫu trước công thức; thêm giao diện, vòng lặp, dừng, đầu ra và chi phí cho MC và TD(0).
- Sửa thứ tự MC thành return → thuật toán → trung bình mẫu hai lượt → oracle → $\alpha$ hằng → mọi lần ghé.
- Tách quy tắc lần ghé khỏi quy tắc bước học; tính lại mọi kết quả số.
- Định nghĩa $T^\pi$, dùng Robbins–Monro theo số lần cập nhật trạng thái và tách $\gamma<1$ khỏi $\gamma=1$ theo lượt.
- Sửa số mũ của quỹ đạo dài; thay tuyên bố xếp hạng bằng cơ chế chệch–phương sai có điều kiện.
- Chuyển X07 từ lặp phép tính sang giải thích ba kết quả đã có.
- Không có ảnh điểm, tài nguyên mạng, mã nguồn, điều khiển, khác chính sách hoặc Q-learning.

## Trạng thái trước kiểm định cuối

Bản chỉnh sửa đã xử lý mọi lỗi `chặn bàn giao` và `nghiêm trọng` được báo cáo. Bốn hình giữ nguyên vì không có lỗi mới. Các kiểm tra cuối và giới hạn rà trực quan được ghi ở cuối nhật ký.

## Quyết định hậu rà soát toán học

- Sửa A06: trung bình mọi lần ghé cho $(V(S),V(x))=(1,1)$ sau $e_1$ và $(0,1/3)$ sau $e_2$.
- Đổi định nghĩa $T^\pi$ ở B06 sang kỳ vọng có điều kiện, nên không ngầm giả định phần thưởng rời rạc; giữ nguyên hai cầu nối $\mathbb E[Y_t^{\mathrm{TD}}]$ và $\mathbb E[\delta_t]$.
- Bổ sung kết luận TD(0) hội tụ gần chắc chắn về $v_\pi$ cho nhánh $\gamma<1$ và nhánh theo lượt $\gamma=1$ với chính sách đúng đắn, dưới các giả thiết đã nêu.
- Tách $N(s)$ là số mẫu MC khỏi $n(s)$ là số lần cập nhật TD trong bảng ký hiệu.

## Kiểm định cuối

- Rà chốt toán học xác nhận A06, B06, B07 và bảng ký hiệu không còn lỗi mức `trung bình` trở lên; 238 biểu thức qua KaTeX ở chế độ nghiêm ngặt.
- HTML có 34 `data-slide-id` duy nhất, 34 ghi chú diễn giả và 40 cặp thẻ `section` cân bằng; mọi mã trang có trong storyboard.
- Mười bốn đường dẫn CSS, JavaScript và SVG đều tồn tại; trang HTML và bốn SVG trả HTTP 200 tại cổng 8765.
- Bốn SVG đều đọc được dưới dạng XML, có `role="img"`, `title` và `desc`. Không có ảnh raster hoặc tài nguyên mạng trong trang chiếu.
- Cỡ chữ bảng hiệu dụng nhỏ nhất là khoảng $0{,}754$ em. Môi trường không có Chromium, Firefox hoặc Playwright, nên chưa thể xác nhận tràn chữ và chồng lấn bằng trình duyệt thật.
- Đã đồng bộ HTML, outline, storyboard, review-log và note-for-author vào Design Files của dự án Codex Slides `20260824165326-chuy-n-lecture-5-d-o-n-phi-m-h-nh-monte--cp0p`. Codex in-editor Browser không khả dụng trong phiên này; chưa tuyên bố đã rà trực quan bằng Codex Slides.
