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

## Lượt soạn note tự học

- Đã tạo `materials/lec-05/lecture-note.md` với 15 topic `lec-05-topic-01..15`, bản đồ chủ đề bốn nhóm, bảng ký hiệu và tài liệu tham khảo; mỗi topic có exercise + hint + solution.
- Note giữ nguyên mọi quyết định số của storyboard và review-log: $(1,1)\to(0,0)$ trung bình mẫu; $(0{,}5,0{,}5)\to(-0{,}25,-0{,}25)$ với $\alpha=0{,}5$; mọi lần ghé $(0,1/3)$; TD $(-0{,}375,0{,}375)$; $\gamma^3=0{,}970299$; $-\gamma=-0{,}99$; oracle $11/21$, $19/21$.
- Sai khác có chủ ý so với nguồn được giữ nguyên trong note: không dùng $0{,}829$ và $0{,}992$; không tuyên bố MC không chệch hay TD phương sai thấp hơn vô điều kiện; tách trung bình mẫu khỏi $\alpha$ hằng; $\alpha$ hằng không hội tụ điểm nói chung; giả thiết hội tụ nêu đầy đủ (cập nhật vô hạn lần, Robbins–Monro, đúng đắn, khởi động lại, hấp thụ).
- Không thêm code demo; không sửa deck, index, CSS hoặc SVG; không tạo `quill.json` — rà mạch theo Quill chỉ biên tập thứ tự vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra.
- Chỉ dùng `$...$` và `$$...$$` cho toán; không dùng các cú pháp toán khác.

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

## Pha ghi chú bài giảng 2026-09-03

### Worker và bằng chứng runtime

- Reader lập kế hoạch: `deepseek/deepseek-v3.2`, profile `plan`, 12 vòng, timeout 600 giây, 14.000 token; runtime `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Reader phân tích nguồn: cùng model, profile `source`, 20 vòng, timeout 600 giây, 18.000 token; hoàn tất sau một lần cầu nối tự thử lại phản hồi rỗng; runtime model khớp, provider OpenRouter.
- Lượt hợp nhất đầu bằng DeepSeek, 8 vòng, dừng đúng lỗi `model exceeded the tool-call limit (8)`. Lượt chạy lại chỉ đọc hai JSON, profile `recheck`, 6 vòng, timeout 600 giây, 10.000 token, hoàn tất với model quan sát đúng yêu cầu và provider OpenRouter.
- Writer bản đầu: `z-ai/glm-5.3-flash`, profile `write`, 20 vòng, timeout 600 giây, 32.000 token; cầu nối phục hồi một phản hồi chưa hoàn chỉnh; runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Hai lượt writer sửa rộng tiếp theo cùng GLM, 12 vòng, lần lượt dừng đúng lỗi `model exceeded the tool-call limit (12)` sau khi đã ghi một phần. Điều phối viên kiểm diff và dùng bản vá cục bộ cho phần còn lại; không đổi model, không chuyển sang worker mặc định.
- Mọi gói worker chỉ chứa tệp được phép đọc. Liên kết `.env` tạm được gỡ sau từng lượt; kiểm tra cuối không còn liên kết `.env` trong `/tmp`.

### Năm rà soát độc lập

| Vai | Model runtime | Mức độ cao nhất | Bằng chứng và quyết định |
|---|---|---|---|
| Góc nhìn sinh viên | `z-ai/glm-5.3-flash` / OpenRouter | trung bình | Báo nhầm kết quả mọi lần ghé $(0,1/3)$ và hai kết quả $\alpha$ hằng; điều phối viên tính lại, giữ các kết quả và sửa mô tả tổng số mẫu thành bốn mẫu cho $S$, ba mẫu cho $x$. Chấp nhận đề nghị chuẩn hóa thuật ngữ. |
| Chuyên gia Học tăng cường | `deepseek/deepseek-v3.2` / OpenRouter | trung bình | Lượt đầu chạm `model exceeded the tool-call limit (8)`; chạy lại trên đúng một note hoàn tất. Bổ sung miền trạng thái có thể đạt được trong nhánh $\gamma=1$, tách hội tụ của thuật toán khỏi tính không chệch của mẫu đích. |
| Toán học và thuật toán | `deepseek/deepseek-v3.2` / OpenRouter | nghiêm trọng trước sửa | Lượt đầu chạm `model exceeded the tool-call limit (8)`; chạy lại trên đúng một note hoàn tất. Tính lại MC mọi lần ghé, MC $\alpha$ hằng, TD tại chỗ, $11/21$, $19/21$, $\gamma^3$ và $-\gamma$; không phát hiện sai số số học. Sửa phát biểu kỳ vọng TD chỉ dịch $V_t(s)$ về $(T^\pi V_t)(s)$; hội tụ cần giả thiết riêng. |
| Phản biện học thuật–giảng dạy | `deepseek/deepseek-v3.2` / OpenRouter | trung bình | Lượt đầu chạm `model exceeded the tool-call limit (8)`; chạy lại trên đúng một note hoàn tất. Chấp nhận cầu nối topic 10→11→12 và giải thích riêng hai tổng Robbins–Monro; bác đề nghị thêm định lý hoặc xếp hạng phương sai ngoài nguồn. |
| Kết nối và mạch viết | `z-ai/glm-5.3-flash` / OpenRouter | trung bình | Xác nhận cần bốn nhãn học tập thay vì gọi bốn mạch là bốn nhóm; chấp nhận phân tuyến cốt lõi/cầu nối/bổ sung/đọc thêm và thêm đầu ra topic 11 sang quỹ đạo dài topic 12. |

### Chỉnh sửa sau rà soát

- Chuẩn hóa tên tiếng Việt “sai phân thời gian (TD)”, “tự mồi (bootstrap)”, “chuẩn vô cùng”, “giá trị chuẩn đối chiếu”; bỏ các nhãn nội bộ “đúng chỉ số”, `return`, `oracle` khỏi note.
- Topic 03 nêu rõ các lượt khởi động lại độc lập, còn mẫu trong cùng lượt phụ thuộc nhau. Topic 06 giữ đúng mọi lần ghé $(0,1/3)$ và $\alpha=0{,}5$ tại chỗ $(-0{,}5625,-0{,}125)$.
- Topic 10 chỉ phát biểu cập nhật kỳ vọng dịch về $T^\pi V_t$; topic 11 nêu miền trạng thái đạt được, tính quá độ và ý nghĩa riêng của hai tổng Robbins–Monro.
- Topic 12 dùng bản đồ $L\;\cdot\;S\;\cdot\;\cdot\;\cdot\;G$, tách bài kiểm tra khỏi phép tính lặp ở topic 02. Topic 13 gắn tính không chệch với mẫu đích $G_t$, không với MC $\alpha$ hằng, và không xếp hạng phương sai phổ quát.
- Topic 14 bỏ khuyến nghị cho môi trường không dừng ngoài phạm vi nguồn. Topic 15 tổng hợp năm ý và dùng $\alpha_{n(s)}(s)$ nhất quán.
- Tự kiểm `no-ai-slop/eval.md`: giữ ý nguồn, không thêm số liệu hay định lý, bỏ lời dẫn rỗng và thuật ngữ Anh không cần thiết. Rà theo Quill xác nhận thứ tự khái niệm, kết nối 10→15 và bảng thuật ngữ nhất quán; không tạo `quill.json`.

### Tái kiểm sau chỉnh sửa note

- DeepSeek: profile `recheck`, 4 vòng, timeout 600 giây, 10.000 token; runtime `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`. Worker đọc note thành hai đoạn do giới hạn 400 dòng, gọi thừa một `search_text` sai kiểu đường dẫn nhưng vẫn hoàn tất ở vòng 4. Báo cáo tính lại topic 03, 06, 10, 11, 12, 13, 15 và xác nhận không còn lỗi mức trung bình trở lên.
- GLM: profile `recheck`, 4 vòng, timeout 600 giây, 8.000 token; runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Báo cáo xác nhận mạch 10→15 và bốn nhãn thống nhất; hai gợi ý nhẹ đã xử lý: viết $\gamma(-1)=-0{,}99$ thay cho $-\gamma$ ở bản đồ topic và dùng thống nhất “lần ghé đầu”.
- Kiểm tra cấu trúc sau sửa: 15 `note-topic-id` duy nhất, 15 khối `exercise`, 15 `hint`, 15 `solution`; không có `\\(...\\)` hoặc `\\[...\\]`; không có `quill.json`.

### Kiểm định cuối pha ghi chú

- `python3 -m reloadserver 8765` dừng với `/usr/bin/python3: No module named reloadserver`. Dùng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm chỉ chứa tài sản cần thiết và không có `.env`.
- Trình duyệt tải thành công liên kết ghi chú duy nhất từ thẻ Bài 05 trong `index.html`. Chromium headless kiểm ở 1280×720 và 800×600: 489 phần tử KaTeX, 15 bài tập, 30 khối `details`, 15 lời giải; không có lỗi console, request hỏng, tràn ngang hoặc phần tử nội dung tràn khung. Phím Enter mở được khối gợi ý đầu tiên.
- `git diff --check` đạt; cấu trúc 15 topic và 15 bộ exercise–hint–solution cân bằng; các đường dẫn note và deck trong thẻ Bài 05 hợp lệ.
- Codex Slides không khả dụng trong môi trường hiện tại do Node.js 18 thấp hơn yêu cầu Node.js 20 của plugin. Pha ghi chú đã được kiểm đầy đủ bằng trình xem Markdown cục bộ, nhưng không tuyên bố đã rà trực quan bằng Codex Slides.

## Hoàn thiện ánh xạ ghi chú–trang chiếu — 04-09-2026

### Phát hiện của reader DeepSeek

- Reader DeepSeek V4 Flash phát hiện bảng ánh xạ cũ trong outline bỏ sót C07 và còn 33 thay vì 34 trang.
- Runtime `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, `provider=OpenRouter`, `reasoning=none`.

### Chuẩn hóa của writer GLM

- Writer GLM chuẩn hóa bảng ánh xạ ở outline và thêm bảng ánh xạ vào storyboard; không đổi nội dung, thứ tự, công thức hoặc SVG.
- Runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, `reasoning=minimal`.

### Kết quả ánh xạ

- HTML được gắn đúng 34 `data-note-topic-id`; C07 thuộc topic-14; mỗi trang đúng một topic và đủ 15 topic.

### Tái kiểm độc lập

- GLM (mạch) PASS; DeepSeek (chuyên môn) PASS. DeepSeek nêu hai lỗi nhẹ ở tham chiếu note topic-13/14, đã sửa thành C02–C03 và C04,C06–C07.
- Không còn lỗi chặn, nghiêm trọng hoặc trung bình.

## Pha đồng bộ bộ trang chiếu 2026-09-03

### Worker và bản nháp

- Reader lập kế hoạch dùng `deepseek/deepseek-v3.2`, profile `plan`, 10 vòng, timeout 600 giây, 16.000 token; runtime `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`. Reader xác nhận 34 trang, 5 mạch ngoài, 34 ghi chú, 4 SVG và tuyến lõi 108 phút cộng vùng đệm 12 phút.
- Writer đồng bộ dùng `z-ai/glm-5.3-flash`, profile `write`, 20 vòng, timeout 600 giây, 18.000 token; runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Điều phối viên bác đề nghị đặt bước học hằng $0{,}1$ vào phát biểu hội tụ B07 vì trái điều kiện Robbins–Monro; giữ $\alpha_n=1/n$.
- Lượt writer chỉnh sửa sau rà dùng cùng GLM, profile `write`, 16 vòng, dừng đúng lỗi `model exceeded the tool-call limit (16)` khi lặp một phép thay thế B07. Điều phối viên kiểm diff, áp dụng các sửa đã chấp nhận bằng bản vá cục bộ, không đổi model và không chuyển worker mặc định.

### Năm rà soát độc lập

| Vai | Model runtime | Kết quả và quyết định |
|---|---|---|
| Góc nhìn sinh viên | `z-ai/glm-5.3-flash` / OpenRouter | Chấp nhận làm rõ bản đồ C00 và giảm tải B07. Bác nhận định sai về thời lượng vì quy định là 120 phút trình chiếu và 30 phút bài tập. |
| Chuyên gia Học tăng cường | `deepseek/deepseek-v3.2` / OpenRouter | Chấp nhận bổ sung điều kiện chính sách đúng đắn tại B07. Bác nhận định $11/21$ và $19/21$ sai sau khi tính lại hệ phương trình. |
| Toán học và thuật toán | `deepseek/deepseek-v3.2` / OpenRouter | Lượt đầu dừng `model exceeded the tool-call limit (6)`; lượt chạy lại cô lập đúng một deck hoàn tất và không phát hiện lỗi toán hoặc thuật toán. |
| Phản biện học thuật–giảng dạy | `deepseek/deepseek-v3.2` / OpenRouter | Lượt đầu dừng `model exceeded the tool-call limit (7)`; lượt chạy lại hoàn tất. Bác các đề nghị thêm đồ thị, số liệu chệch–phương sai, ví dụ mới, code và đổi thứ tự ngoài phạm vi nguồn. |
| Kết nối và mạch viết | `z-ai/glm-5.3-flash` / OpenRouter | Chấp nhận bổ sung B05 vào topic 09, tách A07 khỏi ánh xạ topic 06 và làm rõ năm ý ở D00. |

### Chỉnh sửa và tái kiểm

- Chuẩn hóa “lần ghé đầu”, “phần thưởng tích lũy”, “giá trị chuẩn đối chiếu”; B06 nêu TD(0) là xấp xỉ ngẫu nhiên của sai số Bellman kỳ vọng.
- B07 tách điều kiện $\gamma<1$, trường hợp theo lượt $\gamma=1$, định nghĩa chính sách đúng đắn và hai tổng Robbins–Monro thành các ý ngắn; C00 nêu rõ số chuyển tới hai đầu mút; X03 dùng $\alpha_{n(s)}(s)=0{,}1$.
- Sửa ánh xạ nguồn tr. 32–33 thành C06–C07,D01; ánh xạ topic 09 gồm B03–B05,B08; topic 06 chỉ gồm A05,A06,A08 và ghi A07 thuộc topic 11.
- Lượt tái kiểm toán cuối dùng DeepSeek, profile `recheck`, 6 vòng, timeout 600 giây, 10.000 token; runtime `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`. Worker hoàn tất ở vòng 4 và xác nhận B06, B07, C00, D00, X03 cùng các phép tính liên quan không còn lỗi mức trung bình trở lên.
- Lượt tái kiểm mạch GLM đầu tiên, profile `recheck`, 6 vòng, dừng đúng lỗi `model exceeded the tool-call limit (6)` sau khi tự ghép sai đường dẫn. Lượt chạy lại đặt gốc tại `2627-1`, profile `recheck`, 8 vòng, timeout 600 giây, 9.000 token; runtime `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, hoàn tất ở vòng 3. Không còn lỗi mức trung bình trở lên; đề nghị nhẹ loại B06 khỏi cột ứng dụng TD(0) đã áp dụng.
- Tất cả worker chỉ nhận bản chụp tệp trong phạm vi nhiệm vụ. Các liên kết `.env` tạm đã được gỡ ngay sau lượt chạy; không gửi nội dung `.env` cho worker.
- Kiểm thử trình duyệt phát hiện hai đẳng thức kỳ vọng ở B06 nằm cùng một dòng và bị cắt bên phải. Đã tách thành hai công thức khối tương đương; không đổi biểu thức toán học.

### Kiểm định cuối pha bộ trang chiếu

- `git diff --check` đạt. Parser xác nhận 5 `<section>` ngoài, 34 trang có `data-slide-id` duy nhất, 34 ghi chú diễn giả và thẻ `section` cân bằng; mọi đường dẫn cục bộ đều tồn tại.
- Bốn SVG trong `img/lec-05/` đọc được dưới dạng XML, có `role="img"`, `title` và `desc`. Deck không tham chiếu ảnh raster hoặc tài nguyên mạng cốt lõi.
- Note giữ 15 topic duy nhất, 15 khối bài tập, 15 gợi ý và 15 lời giải. Thẻ Bài 05 trong `index.html` có đúng một liên kết note, một liên kết deck và không liên kết vào `planning/`.
- `python3 -m reloadserver 8765` không khả dụng: `/usr/bin/python3: No module named reloadserver`. Đã dùng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm không có `.env`.
- Chromium headless duyệt đủ 34 trang ở 1280×720 và 800×600 sau khi sửa B06: không tràn, không lỗi KaTeX, console, JavaScript hoặc request. Phím mũi tên dọc đi P00→P01 và phím ngang đi P00→A00 ở cả hai kích thước.
- Trình xem note đạt ở cả hai kích thước: 489 phần tử KaTeX, 15 bài tập, 30 khối `details`, 15 lời giải; không tràn ngang hay request lỗi, phím Enter mở được gợi ý đầu tiên.
- Tự kiểm cuối theo `no-ai-slop/eval.md` giữ câu ngắn, không thêm lời dẫn rỗng, khẩu hiệu hay kết luận lặp. Rà theo Quill xác nhận mạch P→A→B→C→D, thuật ngữ và ký hiệu nhất quán; không tạo `quill.json`.
- Codex Slides không khả dụng vì Node.js hiện tại là 18.19.1, thấp hơn yêu cầu Node.js 20 của plugin. Đã hoàn tất kiểm tra RevealJS cục bộ nhưng không tuyên bố đã rà trực quan bằng Codex Slides.

## Tái kiểm cuối ánh xạ — 04-09-2026

- Chromium duyệt lại đủ 34 trang ở 1280×720 và 800×600: 34 mã trang duy nhất, 34 `data-note-topic-id`, không lỗi KaTeX, console, tài nguyên, bàn phím hoặc phần tử vượt khung trang hiện tại.
- Trình xem ghi chú đạt ở 1280×720 và 390×844: 489 phần tử KaTeX, 34 mục lục hợp lệ, không lỗi tải; phím Enter mở được khối `details`. Bảng và công thức rộng cuộn trong vùng riêng, còn thân tài liệu không cuộn ngang.
- Ba Design Files hiện hữu `lecture-05-du-doan-phi-mo-hinh-2.html`, `outline-2.md`, `storyboard-2.md` đã được ghi lại trong dự án Codex Slides `20260824165326-chuy-n-lecture-5-d-o-n-phi-m-h-nh-monte--cp0p` và đọc lại khớp từng byte với kho.
- Lệnh thêm `lecture-note.md` vào Design Files trả HTTP 500 trên runtime Node.js 18.19.1. Ghi chú vẫn được kiểm trực quan bằng trình xem cục bộ; không tuyên bố đã xem ghi chú hoặc deck bằng Codex in-editor Browser.
