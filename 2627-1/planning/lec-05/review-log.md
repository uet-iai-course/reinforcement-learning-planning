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

## Lượt kiểm định storyboard và năm báo cáo mới

Metadata lượt này: planner, source reader, storyboard reviewer, năm reviewer và writer đều chạy thành công với `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Worker chỉ nhận cây tạm không có `.env`. Kiểm định cấu trúc xác nhận đúng 5 mạch P→A→B→C→D; tuyến lõi giữ 108 phút và vùng đệm 12 phút.

### Kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | C00 | Hai giá trị chuẩn của nguồn không tái tạo nhất quán. | Mô hình ở tr. 30 không cho các số đã in khi tính lại. | Bỏ hai số và ghi rõ lý do trong hồ sơ. | chấp nhận |
| trung bình | C00,C02 | Truy nguyên nguồn chưa đủ chính xác. | C00 dùng dữ kiện tr. 30; kết quả lượt ngắn của C02 nằm ở tr. 29. | Ghi đúng từng trang nguồn. | chấp nhận |
| trung bình | outline | Hw05 Bài 6 bị lược nhưng chưa có lý do. | Bài yêu cầu giải Bellman khi biết mô hình, trùng Bài 04 và ngoài trọng tâm phi mô hình. | Ghi quyết định lược. | chấp nhận |
| nhẹ | outline | Hw05 Bài 1 và 2 đã được hấp thụ nhưng chưa ánh xạ. | Nội dung tương ứng nằm ở B05/C07 và P01–P02/B00. | Bổ sung ánh xạ. | chấp nhận |

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | B07 | Thuật ngữ “chính sách đúng đắn” chưa được định nghĩa trên mặt trang. | Định nghĩa mới chỉ có trong ghi chú. | Nêu điều kiện đi tới kết thúc với xác suất 1. | chấp nhận |
| nhẹ | X07 | Cụm “từ bảng 0” mơ hồ. | Không chỉ rõ bảng khởi tạo. | Ghi $V_0(S)=V_0(x)=0$. | chấp nhận |
| nhẹ | A06,B03,B04 | Bảng có nguy cơ dày khi chiếu. | Nhiều cột và biểu thức trong khung 16:9. | Giữ nội dung, kiểm tra bằng trình duyệt ở hai kích thước. | chờ kiểm định hiển thị |

### Chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | B06 | Một mẫu TD âm có thể bị hiểu thành sai số Bellman kỳ vọng âm. | $\delta=-1{,}25$ ở B04 chỉ là một chuyển mẫu. | Nêu giới hạn này trong ghi chú diễn giả. | chấp nhận |
| trung bình | D01–X04 | Reviewer đề nghị chuyển bài tập trước kết luận. | Nhánh dọc được đặt sau D01. | Giữ nguyên: D01 kết thúc tuyến lõi 108 phút; nhánh dọc dành cho 30 phút bài tập theo quy ước của kho. | bác |
| nhẹ | A06 | Reviewer đề nghị bổ sung chệch của MC mọi lần ghé. | Đây là nhánh đệm ngoài tuyến chính. | Không mở rộng ngoài nguồn và mục tiêu bài. | bác |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | C00 | Hai giá trị $0{,}829$ và $0{,}992$ không tái tạo được. | Tính lại từ mô hình và quy ước phần thưởng đã nêu không cho hai số này. | Không dùng hai giá trị; ghi ngoại lệ nguồn. | chấp nhận |
| trung bình | A00,A04 | Tham số tạo oracle cần hiện trước phép tính. | Xác suất đảo chiều $0{,}2$ và $\gamma=1$ quyết định $11/21$ và $19/21$. | Đưa xác suất đảo chiều lên A00; giữ $\gamma=1$ tại A03–A04. | chấp nhận |
| nhẹ | A06 | Hàng dùng $\alpha$ hằng có thể bị đọc nhầm là TD. | Nhãn cũ chỉ nêu $\alpha=0{,}5$. | Ghi rõ MC mọi lần ghé và thứ tự xử lý. | chấp nhận |
| nhẹ | toàn bài | Không phát hiện sai số số học mới. | Các bảng A03,A05,A06,B03,B04,C01,X03,X07 đều được tính lại. | Giữ kết quả. | chấp nhận |

### Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | A00,A04 | Trực giác của oracle thiếu tham số chính sách ngay từ ví dụ. | Người học phải suy ngược xác suất đảo chiều từ ghi chú. | Hiện chính sách Right và xác suất $0{,}2$ ở A00. | chấp nhận |
| nhẹ | A02 | Quy tắc lần ghé đầu cần được thấy trước bảng ví dụ. | Ghi chú có quy tắc nhưng mặt trang chưa nhấn mạnh số mẫu mỗi lượt. | Thêm “mỗi trạng thái tối đa một mẫu trong mỗi lượt”. | chấp nhận |
| nhẹ | X07 | Đầu vào của bài giải thích chưa tự đủ. | “Bảng 0” không xác định $V_0$. | Ghi đầy đủ hai giá trị khởi tạo. | chấp nhận |

### Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | A08→B00 | Cầu nối MC sang TD còn ngầm. | Vai trò trong mạch của A08 là đóng trục thiết kế MC; đầu ra cho B00 chưa gọi rõ đích một bước. | Thêm câu nối: TD thay return bằng đích một bước và cập nhật trước khi lượt kết thúc. | chấp nhận |
| trung bình | D01→X07 | Reviewer cho rằng bài kết thúc ở nhánh bài tập. | Vai trò trong mạch của D01 là kết luận; kết nối ra là nhánh chữa bài tập dọc. | Giữ nguyên vì tuyến chính đã khép tại D01; ghi rõ nhánh X là 30 phút bài tập. | bác |
| trung bình | C02,C05 | Reviewer đề nghị chuyển kiểm tra trước phần ứng dụng. | C05 kiểm tra sau khi C02–C04 đã hoàn tất ví dụ, hình thức và ứng dụng. | Giữ thứ tự; chu trình học tập không bị đảo. | bác |

### Dương tính giả và đề xuất không áp dụng

- “Có 6 section ngoài”: parser đếm đúng 5 mạch P/A/B/C/D; bác.
- “Thiếu thư viện”: cây tạm của worker cố ý chỉ chứa tệp được phép đọc; kho thật có đủ thư viện; bác.
- “Footer sai”: footer tuân theo mẫu cục bộ; bác.
- “A07 thiếu nguồn”: dòng nguồn tồn tại nhưng bị ngắt trong bản trích văn bản; bác.
- Không đổi thứ tự X hoặc C05; không thêm nội dung ngoài nguồn về chệch của MC mọi lần ghé.
- Chưa render và chưa đồng bộ Codex Slides ở thời điểm lập bảng này.

## Trạng thái trước kiểm định cuối

Bản chỉnh sửa đã xử lý mọi lỗi `chặn bàn giao` và `nghiêm trọng` được báo cáo. Bốn hình giữ nguyên vì không có lỗi mới. Các kiểm tra cuối và giới hạn rà trực quan được ghi ở cuối nhật ký.

## Tái kiểm sau chỉnh sửa

- Hai reviewer độc lập chạy qua `openrouter-mcp-reviewer` với `task_profile=recheck`, `max_rounds=8`, `timeout=240`, `max_tokens=6000`, `temperature=0.1`. Cả hai trả `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Reviewer toán học và thuật toán tính lại A00, A03–A06, B03–B04, B06–B07, C00–C02, X03 và X07; không còn lỗi mức `trung bình` trở lên.
- Reviewer kết nối và mạch viết xác nhận đúng 5 mạch ngoài, 34 trang, nhánh X là con trực tiếp của mạch D, không còn lồng sâu quá hai cấp và không có nhãn quy trình nội bộ trên mặt trang.
- Lỗi cấu trúc do kiểm thử trình duyệt phát hiện: wrapper thứ ba quanh X07/X03/X04 làm RevealJS lặp các trang P00–P02. Đã bỏ wrapper và một thẻ đóng dư, giữ D01 là kết luận của tuyến lõi và ba trang X là nhánh bài tập dọc 30 phút.
- Hai đề xuất nhẹ đã xử lý: A06 nêu rõ các cột sau $e_2$ tiếp tục từ giá trị sau $e_1$; ánh xạ tr. 1 và tr. 15–16 trong outline được tách chính xác. Dòng thời lượng cũ trong nhật ký đổi từ 120 phút thành tuyến lõi 108 phút.
- Tự kiểm theo `no-ai-slop/eval.md` không phát hiện lời dẫn rỗng, khẩu hiệu, đối lập giả hoặc kết luận lặp. Rà bằng Quill xác nhận thứ tự vấn đề → ví dụ → hình thức → ứng dụng → kiểm tra và thuật ngữ MC/TD nhất quán; không tạo `quill.json`.

## Quyết định hậu rà soát toán học

- Sửa A06: trung bình mọi lần ghé cho $(V(S),V(x))=(1,1)$ sau $e_1$ và $(0,1/3)$ sau $e_2$.
- Đổi định nghĩa $T^\pi$ ở B06 sang kỳ vọng có điều kiện, nên không ngầm giả định phần thưởng rời rạc; giữ nguyên hai cầu nối $\mathbb E[Y_t^{\mathrm{TD}}]$ và $\mathbb E[\delta_t]$.
- Bổ sung kết luận TD(0) hội tụ gần chắc chắn về $v_\pi$ cho nhánh $\gamma<1$ và nhánh theo lượt $\gamma=1$ với chính sách đúng đắn, dưới các giả thiết đã nêu.
- Tách $N(s)$ là số mẫu MC khỏi $n(s)$ là số lần cập nhật TD trong bảng ký hiệu.

## Kiểm định cuối

- Rà chốt toán học xác nhận A06, B06, B07 và bảng ký hiệu không còn lỗi mức `trung bình` trở lên. Chromium không báo lỗi KaTeX hoặc JavaScript.
- HTML có 34 `data-slide-id` duy nhất, 34 ghi chú diễn giả, 5 `<section>` ngoài và 39 cặp thẻ `section` cân bằng; mọi mã trang có trong storyboard.
- `python3 -m reloadserver 8765` không khả dụng trong môi trường. Đã dùng `python3 -m http.server 8765` trên webroot tạm chỉ chứa tài sản cần thiết và không có `.env`; trang HTML, CSS, JavaScript và bốn SVG đều tải thành công.
- Bốn SVG đều đọc được dưới dạng XML, có `role="img"`, `title` và `desc`. Không có ảnh raster hoặc tài nguyên mạng trong trang chiếu.
- Chromium headless duyệt đủ 34 trang ở 1280×720 và 800×600, chụp 68 ảnh, không có lỗi console hoặc request. Kiểm tra bàn phím cho P00→P01 và P00→A00 đạt. Các cảnh báo hình học ở P00 và công thức KaTeX A01/A02/A04/B06/B07 là dương tính giả; ảnh chụp xác nhận không cắt, chồng hoặc tràn. A06, B03, B04, B06, B07 và ba trang X đều đọc rõ.
- Đã đồng bộ HTML, outline, storyboard và review-log vào Design Files `*-2` của dự án Codex Slides `20260824165326-chuy-n-lecture-5-d-o-n-phi-m-h-nh-monte--cp0p` và đọc lại để đối chiếu byte. Dự án vẫn ở trạng thái `draft/clarify` với 0 slide; Codex in-editor Browser không có trong phiên này, nên không tuyên bố đã rà trực quan trong Codex Slides.
