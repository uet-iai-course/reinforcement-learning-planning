# Nhật ký rà soát Bài 06

## Kiểm kê nguồn

- Tệp chính: `RL-hk2-2025-2026/lecture-06-model-free-control.pdf`, 30 trang.
- Không có bài tập hoặc code demo riêng cho Bài 06 trong `RL-hk2-2025-2026/resources/`.
- Hình kỹ thuật được vẽ lại thành năm SVG; không dùng ảnh raster hoặc tài nguyên mạng.

## Lỗi nguồn đã xử lý trong bản nháp

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | A03 | Định nghĩa on/off-policy bằng mức độ “gần trùng nhau” không xác định đối tượng học. | Nguồn tr. 8 không tách $\mu$ và $\pi$. | Định nghĩa theo chính sách hành vi và chính sách đích. | đã xử lý |
| nghiêm trọng | A02 | Mệnh đề cải thiện $\varepsilon$-greedy thiếu giả thiết chặt. | Nguồn tr. 24 bắt đầu từ một chính sách $\varepsilon$-greedy nhưng phép chứng minh dùng cấu trúc $\varepsilon$-mềm. | Phát biểu $\pi$ là $\varepsilon$-mềm, $\pi'$ là $\varepsilon$-tham lam theo $q_\pi$. | đã xử lý |
| nghiêm trọng | A04 | Quy tắc số không cho kết quả duy nhất nếu thiếu cách tiêu thụ số. | Nguồn tr. 17 không nói có dùng thêm số khi thăm dò hoặc cách phá hòa. | Công bố cổng, số chọn hành động và phá hòa; chốt lượt $D\to C\to B\to A$. | đã xử lý |
| nghiêm trọng | B01–B02,C01–C02,D01–D02 | Thuật toán thiếu giao diện, trạng thái kết thúc, dừng hoặc chi phí. | Các trang nguồn chủ yếu nêu cập nhật cục bộ. | Nêu đủ đầu vào, đầu ra, khởi tạo, vòng lặp, nhánh kết thúc, dừng và chi phí. | đã xử lý |
| chặn bàn giao | C03,D03 | Ví dụ SARSA và Q-learning không có các mẫu cụ thể nên không tái tạo được. | Nguồn tr. 18 và 21 chỉ yêu cầu “5 mẫu”. | Dùng cùng lượt từ tr. 17; tính từng đích và cập nhật tại chỗ. | đã xử lý |
| chặn bàn giao | D06–D07 | Trang 19 gọi công thức giá trị trạng thái là off-policy SARSA và thiếu điều kiện hỗ trợ. | Công thức cập nhật $V$, không phải $Q$; thiếu $\pi>0\Rightarrow\mu>0$. | Đổi thành TD(0) khác chính sách cho giá trị trạng thái với tỉ số từng bước thông thường. | đã xử lý |
| nghiêm trọng | B06 | Nguồn suy GLIE từ $\varepsilon_k=1/k$. | $\varepsilon_k\to0$ không tự bảo đảm mọi cặp được ghé vô hạn. | Tách hai điều kiện GLIE và nêu vai trò của động lực, khởi động lượt. | đã xử lý |
| nghiêm trọng | C05,D07 | Robbins–Monro dùng chỉ số toàn cục và thiếu giả thiết. | Điều kiện cần áp dụng cho số lần cập nhật riêng của mỗi cặp. | Viết $\alpha_n(s,a)$ và tách phạm vi chiết khấu/theo lượt. | đã xử lý |
| nghiêm trọng | E02 | Chặn độ phức tạp mẫu thiếu điều kiện và bị diễn giải quá rộng. | Nguồn tr. 29 không nêu rõ i.i.d., khoảng của return và tính điểm. | Viết chặn Hoeffding cho một trung bình vô hướng i.i.d. bị chặn; không suy sang điều khiển thích nghi. | đã xử lý |
| trung bình | E00,E03 | Danh mục thuật toán vượt phạm vi bài. | Nguồn tr. 22–23, 30 nhắc DQN, actor-critic và nhiều thuật toán không được định nghĩa. | Lược danh mục; khóa phạm vi bảng hữu hạn. | đã xử lý |

## Kết quả số đã tự tính

- LCG cho $u_1,u_2,u_3,u_4=(0{,}8,0{,}6,0{,}2,0{,}4)$ và lượt $(D,0)\to(C,0)\to(B,0)\to A$.
- Return MC là $998,999,1000$ tại $(D,0),(C,0),(B,0)$.
- MC trung bình mẫu với $N$ mới bằng một cho $998,999,1000$.
- MC với $\alpha=0{,}8$ cho $798{,}6;799{,}4;800$.
- SARSA tại chỗ cho $Q(D,0)=0{,}2$, $Q(C,0)=-0{,}6$, $Q(B,0)=800$.
- Q-learning tại chỗ cho $Q(D,0)=0{,}2$, $Q(C,0)=0{,}2$, $Q(B,0)=800$.
- Khác biệt tại C đến từ $Q(B,0)=0$ so với $\max_aQ(B,a)=1$.

## Sai khác có chủ ý so với nguồn

- Gộp phần ôn dự đoán vào hai trang mở đầu.
- Dùng một bảng $Q_0$ và một lượt chung thay vì các câu hỏi rời không đủ mẫu.
- Đưa trực giác về đích trước giao diện thuật toán, rồi mới chạy số.
- Sửa định nghĩa chính sách, mệnh đề cải thiện, GLIE, Robbins–Monro, nhánh kết thúc và TD(0) khác chính sách.
- Thu hẹp chặn Hoeffding và không mở sang xấp xỉ hàm, DQN hoặc actor-critic.
- Giữ D06–D07 và E02 như nội dung linh hoạt vì chúng sửa lỗi nguồn nhưng không cần cho mạch thuật toán chính.

## Trạng thái bản nháp

- Đã tạo 34 trang chính và 3 trang bài tập dọc.
- Tuyến cốt lõi 110 phút không gồm D06, D07 hoặc E02; ba trang linh hoạt dùng đúng 10 phút; bài tập dùng 30 phút.
- Đã tạo năm SVG có `role="img"`, `title`, `desc`; nhãn nhỏ nhất 30 px.
- Bốn báo cáo phản biện độc lập đã được hợp nhất ở phần cuối; mọi lỗi chặn bàn giao và nghiêm trọng đã được xử lý.

## Kiểm tra tĩnh của tác tử soạn

- HTML có 37 `data-slide-id` duy nhất, 37 ghi chú diễn giả và 44 cặp thẻ `section` cân bằng. Mọi mã trang đều có trong storyboard.
- Mười bốn đường dẫn CSS, JavaScript và SVG đều trỏ đến tệp cục bộ hiện có. Không có ảnh raster hoặc URL mạng trong HTML.
- Năm SVG đọc được bằng bộ phân tích XML, có `role="img"`, `title`, `desc`; không có nhãn dưới 30 px.
- 210 biểu thức qua KaTeX ở chế độ nghiêm ngặt, không có lỗi phân tích.
- Cỡ chữ nội dung chính là $0{,}84$ em; bảng và khối giả mã có cỡ hiệu dụng xấp xỉ $0{,}756$ em. Không dùng ngoại lệ dưới $0{,}65$ em.
- Không có nhãn tuyến, thời lượng hoặc mã nội bộ trên mặt trang chiếu và trong ghi chú diễn giả.
- Đã tự kiểm theo `no-ai-slop/eval.md`: giữ số liệu và mệnh đề của nguồn sau hiệu chỉnh; cắt lời dẫn, nhận định quảng bá, câu tổng kết lặp và nhịp câu máy móc. Không phát hiện từ cấm hoặc khuôn diễn đạt bị cấm trong nội dung hiển thị.
- Đã rà mạch theo nguyên tắc Quill: thuật ngữ, ký hiệu, bảng $Q_0$ và lượt mẫu được truyền liên tục; không tạo `quill.json`.

## Chỉnh sửa sau kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | E00–X03 | Nhóm E03/X01–X03 bị lồng trong nhóm E00–E02, tạo cấp RevealJS thứ ba. | Bộ phân tích cấu trúc ghi nhận độ sâu ba. | Đóng nhóm E00–E02; tạo nhóm ngang mới có E03 làm neo và X01–X03 là các trang dọc. | đã xử lý; độ sâu tối đa bằng hai |
| nghiêm trọng | C00–C04 | Công thức và giao diện SARSA xuất hiện trước ví dụ cụ thể. | Người học chưa biết vì sao $A_{t+1}$ phải đi vào đích. | Đặt chuyển $C0\to B$, $A'=0$ trước công thức; sau đó mới nêu thuật toán, toàn lượt và kiểm tra đổi hành động. | đã xử lý |
| nghiêm trọng | D00–D04 | Q-learning cũng mở bằng công thức trước khi có đối chiếu hành động lấy mẫu và hành động tham lam. | Hai giá trị tại B chưa được đặt cạnh nhau. | Đặt ví dụ $Q(B,0)=0$ và $\max_aQ(B,a)=1$ trước công thức; sau đó mới chạy toàn lượt. | đã xử lý |
| nghiêm trọng | P02,A03–B06 | Bản nháp có thể khiến người học suy mọi lượt dài ba bước và MC luôn có return. | Chính sách tham lam ban đầu tạo vòng B–C. | Chỉ nói lượt cố định dài ba bước; nêu MC cần kết thúc gần chắc chắn và return hữu hạn hoặc bị chặn ở P02, B01, B02 và B06. | đã xử lý |
| nghiêm trọng | A04 | Chuỗi số bị trình bày như bộ mô phỏng $\varepsilon$-tham lam. | Dãy là tuần hoàn tất định; số sau cổng thăm dò luôn là $0{,}4$. | Gọi là quy tắc tất định để tái tạo lượt; không dùng để kiểm chứng phân phối. | đã xử lý |
| trung bình | A02,B05–B06 | Định lý cải thiện đứng trước mọi ứng dụng MC. | Hình thức hóa chưa giải thích một bước cải thiện đã quan sát. | Chuyển thành B05, sau hai bảng cập nhật và trước GLIE ở B06. | đã xử lý |
| trung bình | D05–D07 | TD(0) giá trị trạng thái chen trước kết luận hội tụ Q-learning. | Mạch thuật toán chính bị ngắt. | Đặt hội tụ Q-learning ở D05; chuyển D06–D07 thành phần mở rộng và nối trở lại E00. | đã xử lý |
| trung bình | X01–X03 | Bài tập chủ yếu lặp phép tính đã giải. | Chưa đủ yêu cầu giải thích cho 30 phút. | Thêm phản biện bộ lấy mẫu, đối chiếu ba bảng, sửa lập luận hội tụ và tình huống thay đổi hành động. | đã xử lý |

Sau đổi thứ tự, đã rà lại hai trang lân cận mỗi phía tại A03–B01, B03–C02, C03–D02 và D03–E01. Outline, storyboard và ghi chú giảng viên đã được đồng bộ.

## Kiểm tra tĩnh sau chỉnh sửa storyboard

- HTML vẫn có 34 trang chính và 3 trang bài tập dọc; 37 mã duy nhất và 37 ghi chú diễn giả.
- Có 44 cặp thẻ `section` cân bằng; độ sâu lồng tối đa bằng hai. E00–E02 và E03/X01–X03 là hai nhóm ngang riêng.
- Mọi mã trang có trong storyboard; toàn bộ tài sản cục bộ tồn tại; trang trả HTTP 200 tại cổng 8765.
- 210 biểu thức qua KaTeX nghiêm ngặt. `git diff --check` không báo lỗi khoảng trắng.

## Hợp nhất bốn báo cáo độc lập

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | A04 | Ký hiệu số giả ngẫu nhiên, cổng thăm dò và cách tiêu thụ số chưa đủ để tái tạo hành động. | Chưa nêu $\varepsilon$, bất đẳng thức cổng và quy tắc dùng số kế. | Đổi thành $u_t$, nêu $\varepsilon=0{,}25$, cổng $u_t\le\varepsilon$ và cách chọn 0/1; dùng `shared-trace.svg`. | đã xử lý |
| nghiêm trọng | C02,D02 | Giả mã mới mô tả một chuyển, thiếu vòng lượt và nhánh dừng hoàn chỉnh. | Không thấy reset $S_0$, chọn $A_0$ của SARSA hoặc `break` ở trạng thái kết thúc. | Viết lại thành thuật toán đầu-cuối; chỉ gán $A'$ ở nhánh chưa kết thúc. | đã xử lý |
| nghiêm trọng | B06,C05,D05 | Phạm vi hội tụ và miền độ phủ chưa chặt; ví dụ $\gamma=1$, $\alpha$ hằng dễ bị hiểu là bằng chứng. | Mệnh đề dùng cụm mơ hồ và chưa gắn MC với quy tắc bước học hội tụ. | Phát biểu chính cho MDP hữu hạn chiết khấu, thưởng bị chặn, cặp khả đạt, GLIE và Robbins–Monro; tách ví dụ số khỏi định lý. | đã xử lý |
| nghiêm trọng | D06,D07 | Nhánh đánh giá khác chính sách chưa báo rõ quay lại dự đoán và điều kiện hỗ trợ chưa lượng hóa. | Người học có thể nhầm đây là thuật toán điều khiển thứ tư. | Gắn nhãn dự đoán $V$, lượng hóa trên cặp khả đạt, thêm ví dụ $\rho=4$ và điều kiện chi phí $O(1)$. | đã xử lý |
| trung bình | B03,B05 | B03 mô tả sai thay đổi hành động tham lam; định lý B05 chưa tách $q_\pi$ chính xác khỏi một mẫu $Q$. | Hành động 0 đã tham lam tại C,D; một mẫu không cho cải thiện đơn điệu. | Sửa mô tả B03 và thêm cầu nối, giới hạn vào B05. | đã xử lý |
| trung bình | B02,E01,E02 | Chi phí cập nhật chính sách, chi phí chọn hành động và giả thiết Hoeffding còn thiếu. | Đọc đích khác với quét để chọn hành động; chặn cần i.i.d., chính sách và phân phối khởi đầu cố định, $0<\delta<1$. | Bổ sung trực tiếp trên trang. | đã xử lý |
| trung bình | X01–X03 | Khối lượng chưa khớp 30 phút và đáp án chỉ nằm trong ghi chú. | Mỗi bài có bốn yêu cầu, không có nội dung chữa hiện trên mặt trang. | Rút gọn, thêm đáp án dạng fragment; phân bổ 5–10–15 phút và tùy chọn chia nhóm trong `note-for-author.md`. | đã xử lý |

Không áp dụng đề xuất đưa thời lượng hoặc phân tuyến lên mặt trang chiếu; thông tin này chỉ nằm trong `note-for-author.md`. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng` chưa xử lý trong bốn báo cáo.

Đã tự kiểm lại theo `no-ai-slop/eval.md`: giữ nguyên số liệu và phạm vi học thuật, cắt cụm mơ hồ, không thêm nhận định quảng bá hoặc câu hỏi tu từ. Đã rà tính liên tục theo Quill: $(D,0)$ được định nghĩa trước khi dùng; $Q_0$, lượt chung, đích MC–SARSA–Q-learning và điều kiện hội tụ được truyền nhất quán; không tạo `quill.json`.

## Chỉnh sửa cục bộ hậu rà soát

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| nghiêm trọng | B06,C05,D05 | “Cặp khả đạt” chưa có định nghĩa chung và kết luận hội tụ chưa giới hạn miền. | D06 dùng $\mathcal X_{\mathrm{reach}}$ nhưng P02 chưa định nghĩa. | Định nghĩa $\mathcal X_{\mathrm{reach}}$ tại P02; viết mọi điều kiện và kết luận hội tụ trên miền này. | đã xử lý |
| nghiêm trọng | C02,D02 | Lịch bước học theo từng cặp chưa được thực thi trong giả mã. | Giao diện có $\alpha_n$ nhưng vòng lặp chỉ dùng $\alpha$. | Khởi tạo $N(s,a)=0$; tăng bộ đếm trước cập nhật và đặt $\alpha=\alpha_{N(s,a)}(s,a)$. Tách $k$ cho lượt, $t$ cho chuyển. | đã xử lý |
| trung bình | P02,B02,C02,D02 | $A_{\max}$ được dùng ở B02 nhưng chưa có định nghĩa dùng chung; ký hiệu chi phí chưa nhất quán. | B02 dùng $A_{\max}$, D02 dùng $|\mathcal A|$. | Định nghĩa $A_{\max}=\max_s|\mathcal A(s)|$ tại P02 và dùng lại trong các thuật toán. | đã xử lý |
| trung bình | E03 | Cầu nối sang Bài 07 nêu sai nội dung. | Bản trước nói về dấu vết đủ điều kiện và phương pháp nhiều bước. | Đổi thành thay bảng giá trị bằng hàm xấp xỉ và xét lại bảo đảm hội tụ. | đã xử lý theo chỉ dẫn chương trình |
| trung bình | X02,X03 | Đáp án hiển thị chưa xử lý hai nhánh phản biện. | X02 thiếu trường hợp B chọn phải; X03 chưa tách điều kiện của Q-learning. | Bổ sung kết quả SARSA tại C và điều kiện độ phủ, Robbins–Monro của Q-learning. | đã xử lý |
| trung bình | storyboard | Bảng thời lượng chưa hiển thị trực tiếp ranh giới cốt lõi và linh hoạt. | D06–D07, E02 chỉ được mô tả dưới bảng. | Thêm hai hàng linh hoạt 5 phút; giữ sáu hàng cốt lõi tổng 110 phút và tổng linh hoạt 10 phút. | đã xử lý |

Outline và storyboard đã được đồng bộ với miền $\mathcal X_{\mathrm{reach}}$, bộ đếm cập nhật theo cặp, $A_{\max}$ và cầu nối đúng sang Bài 07.

## Dọn bản trình chiếu trước kiểm định cuối

- Loại mọi mã trang khỏi nội dung hiển thị và ghi chú diễn giả; các mã chỉ còn trong HTML và tài liệu quy trình.
- Chuyển hướng dẫn thời lượng bài tập sang `note-for-author.md`; ghi chú diễn giả chỉ giữ mạch nói và cách tổ chức hoạt động.
- Đổi nhãn “Mở rộng” thành tiêu đề nội dung về dự đoán khác chính sách để không hiển thị phân tuyến nội bộ.

## Sửa ba lỗi trung bình cuối

- P02 và outline viết đủ miền $\mathcal X=\{(s,a):s\in\mathcal S,\ a\in\mathcal A(s)\}$ và $A_{\max}=\max_{s\in\mathcal S}|\mathcal A(s)|$.
- X02 chỉ thay $A_{t+1}$ tại B và yêu cầu tính lại đích, cập nhật tại C; không suy rằng toàn bộ lượt giữ nguyên.
- X03 hiển thị đủ MDP hữu hạn, thưởng bị chặn và $\gamma<1$ trước khi tách GLIE, độ phủ và Robbins–Monro.

Storyboard đã đồng bộ luận điểm và phạm vi đáp án của X02–X03.

## Kiểm định cuối

- Rà chốt toán học và học thuật xác nhận không còn lỗi từ mức `trung bình` trở lên trong các phần đã sửa; 263 biểu thức qua KaTeX ở chế độ nghiêm ngặt.
- HTML có 37 `data-slide-id` duy nhất, 37 ghi chú diễn giả, 44 cặp thẻ `section` cân bằng và độ sâu lồng tối đa bằng hai; mọi mã trang có trong storyboard.
- Mười lăm đường dẫn CSS, JavaScript và SVG đều tồn tại. Trang HTML và năm SVG trả HTTP 200 tại cổng 8765.
- Năm SVG đều đọc được dưới dạng XML, có `role="img"`, `title`, `desc` và cỡ nhãn nhỏ nhất 30 px. Mọi SVG đều được dùng; không có ảnh raster hoặc tài nguyên mạng trong trang chiếu.
- Cỡ chữ bảng và khối thuật toán hiệu dụng nhỏ nhất là khoảng $0{,}756$ em. Môi trường không có Chromium, Firefox hoặc Playwright, nên chưa thể xác nhận tràn chữ và chồng lấn bằng trình duyệt thật.
- Đã đồng bộ HTML, outline, storyboard, review-log và note-for-author vào Design Files của dự án Codex Slides `20260824175305-chuy-n-lecture-6-i-u-khi-n-phi-m-h-nh-mo-c905`; các bản sao khớp từng byte. Codex in-editor Browser không khả dụng trong phiên này, nên chưa tuyên bố đã rà trực quan bằng Codex Slides.

## Chỉnh sửa theo REVIEW_BRIEF.md

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Kết quả |
|---|---|---|---|---|---|
| trung bình | P02 | Gạch đầu dòng cảnh báo "tối đa 3 bước" nằm trên mặt trang gây quá tải. | REVIEW_BRIEF.md mục 1. | Bỏ khỏi mặt trang; giữ mạch trong notes P02 và các mục A03/C00. | đã xử lý |
| trung bình | A01 | $m_s$ chưa được định nghĩa ngay; nhánh khai thác dễ đọc nhầm là $1-\varepsilon$. | REVIEW_BRIEF.md mục 2. | Định nghĩa $m_s=|\mathcal A(s)|$ ngay đầu trang; sửa gạch đầu dòng nhánh khai thác thành $1-\varepsilon+\varepsilon/m_s$; thêm $m_s$ vào bảng ký hiệu outline. | đã xử lý |
| trung bình | A03,C00,greedy-induced-mrp.svg | Diễn đạt chưa chính xác về quan hệ chuyển và giới hạn thời gian của nguồn. | REVIEW_BRIEF.md mục 1. | Nêu rõ: sơ đồ B–C là quan hệ chuyển tham lam theo bảng thống nhất khi bỏ bộ đếm giới hạn; lượt dùng trong deck kết thúc ở A sau đúng ba chuyển; nguồn ghi tối đa 3 bước nhưng không nêu quy ước return khi cắt. Sửa title/desc SVG, không đổi hình học. | đã xử lý |
| trung bình | C00,D00 | Câu đặt lại $Q_0$ còn dài. | REVIEW_BRIEF.md mục 4. | Rút thành một câu ngắn ở mỗi trang, đồng bộ storyboard. | đã xử lý |
| trung bình | C04,X02 | Phản thực cục bộ chưa có caveat. | REVIEW_BRIEF.md mục 6. | Thêm caveat vào notes: chỉ thay $A_{t+1}$ trong đích tại C; không khẳng định phần còn lại của lượt vật lý giữ nguyên. | đã xử lý |
| trung bình | D02,D05 | $\mu_t$ chưa được định nghĩa và nối với độ phủ. | REVIEW_BRIEF.md mục 7. | Định nghĩa $\mu_t$ là chính sách hành vi tại chuyển $t$; yêu cầu cơ chế hành vi bảo đảm mọi cặp khả đạt được cập nhật vô hạn; không ép Q-learning GLIE; thêm $\mu_t$ vào outline. | đã xử lý |
| trung bình | E00 | Hàng "Khám phá" không phản ánh đúng điều kiện từng thuật toán. | REVIEW_BRIEF.md mục 8. | Đổi nhãn thành "Điều kiện hành vi": MC cần GLIE và lượt kết thúc; SARSA cần GLIE; Q-learning cần cập nhật vô hạn từng cặp; thêm câu GLIE gồm độ phủ vô hạn và tham lam ở giới hạn. | đã xử lý |
| trung bình | outline,storyboard | Cấu trúc và E03 chưa phản ánh 7 section ngoài. | REVIEW_BRIEF.md mục 10–11. | E03 là kiểm tra/kết luận và neo X01–X03; hàng 6 là E00–E02, hàng 7 là E03/X01–X03; không tách section thứ tám. | đã xử lý |

## Nhật ký runtime

- planner: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- source reader: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- storyboard reviewer: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- reviewer 1 (sinh viên): `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- reviewer 2 (chuyên gia Học tăng cường): `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- reviewer 3 (toán học và thuật toán): `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- reviewer 4 (phản biện học thuật–giảng dạy): `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- reviewer 5 (kết nối và mạch viết): `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.
- writer: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` — thành công.

Báo cáo reviewer ghi nhận: sinh viên — gạch đầu dòng P02 quá tải, đã xử lý; chuyên gia Học tăng cường — E00 cần tách điều kiện hành vi, đã xử lý; toán học và thuật toán — $m_s$ và $\mu_t$ thiếu định nghĩa, đã xử lý; phản biện học thuật–giảng dạy — caveat C04/X02 cần thêm, đã xử lý; kết nối và mạch viết — câu đặt lại $Q_0$ ở C00/D00 cần rút, đã xử lý. Dương tính giả: báo cáo `target-comparison.svg` thiếu `role="img"`/`aria-labelledby`/title/desc — điều phối viên xác nhận tệp đã có đủ, đề xuất bị bác. Chưa tuyên bố đã render hoặc rà Codex Slides.

## Tái kiểm sau chỉnh sửa

- Tái kiểm toán học, thuật toán và đối chiếu nguồn: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`; các phép tính MC, SARSA, Q-learning, xác suất $\varepsilon$-tham lam, bảng $Q_0$, giới hạn ba bước và điều kiện độ phủ đều nhất quán.
- Tái kiểm kết nối và mạch viết: cùng metadata runtime. Xác nhận 7 `<section>` ngoài, 37 `data-slide-id`, độ sâu tối đa 2 và E03 là neo của nhóm dọc X01–X03. Ba sai lệch nhẹ giữa outline và storyboard đã được sửa.
- Điều phối viên đổi tiêu đề C00 thành “Hành động kế tiếp trong đích SARSA”, liệt kê đủ 37 mã trang trong outline và tách công thức B05 thành ba dòng sau khi render phát hiện tràn ngang.

## Kiểm định cuối ngày 30-08-2026

- `git diff --check` không báo lỗi. HTML có 37 mã trang duy nhất, 37 ghi chú diễn giả, 44 cặp thẻ `section` cân bằng, 7 section ngoài và độ sâu tối đa 2. Mọi mã trang xuất hiện trong outline và storyboard.
- Năm SVG đọc được dưới dạng XML, có `role="img"`, `title`, `desc`; không có ảnh raster hoặc tài nguyên mạng cốt lõi. Mọi đường dẫn CSS, JavaScript và SVG đều tồn tại.
- Lệnh `reloadserver` không có trong môi trường. Đã dùng bản sao webroot tạm chỉ chứa HTML, CSS, RevealJS, plugin, KaTeX và năm SVG; bản sao không chứa `.env`; phục vụ bằng `python3 -m http.server 8765`.
- Chromium duyệt đủ 37 trang ở 1280 × 720 và 800 × 600, tạo 74 ảnh kiểm tra. Không có lỗi console, lỗi trang hoặc request thất bại; điều hướng bàn phím ngang và dọc hoạt động. Công thức B05 bị tràn ở lượt đầu, đã tách dòng và render lại. Các cảnh báo hình học còn lại ở P00, C01, D01 và E02 là dương tính giả do biên glyph KaTeX/tiêu đề; ảnh chụp xác nhận không bị cắt hoặc chồng lấn.
- Đã tự kiểm theo `no-ai-slop/eval.md`: không thêm lời dẫn rỗng, khẩu hiệu, nhận định quảng bá hoặc kết luận lặp; nội dung hiển thị giữ câu ngắn và thuật ngữ nhất quán. Đã rà theo Quill: tuyến dự đoán → chính sách → MC → SARSA → Q-learning → tổng hợp → kết luận truyền liên tục bảng $Q_0$, lượt chung và ký hiệu; không tạo `quill.json`.
- Đã đồng bộ chính xác HTML, outline, storyboard và hai bản review-log vào Design Files của dự án Codex Slides `20260824175305-chuy-n-lecture-6-i-u-khi-n-phi-m-h-nh-mo-c905`; kiểm tra đọc lại khớp từng ký tự. Dự án Codex Slides vẫn ở trạng thái draft với 0 slide, và phiên này không có công cụ Browser trong trình soạn thảo để mở resource link; vì vậy không tuyên bố đã rà trực quan bằng Codex Slides.

## Giai đoạn I — ghi chú bài giảng, ngày 03-09-2026

- Nguồn: `RL-hk2-2025-2026/lecture-06-model-free-control.pdf`, 30 trang. Ghi chú mới nằm tại `2627-1/materials/lec-06/lecture-note.md`, gồm 15 `note-topic-id` duy nhất và bốn nhóm chủ đề: 12 cốt lõi, 1 cầu nối, 2 bổ sung, cùng một tuyến đọc thêm không có topic ID.
- Lộ trình trình chiếu là 110 phút cốt lõi cộng hai nhánh 5 phút; X01–X03 dành 5–10–15 phút cho phần chữa bài. Mỗi chủ đề có bài kiểm tra, gợi ý và đáp án.
- Hai reader lập kế hoạch độc lập. Reader `plan/12/600/16000` dùng `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`, thành công. Reader nguồn ban đầu dừng với lỗi `model exceeded the tool-call limit (20)`; lượt chạy lại trên hai phần nguồn bằng `source/6/600/20000` giữ nguyên model và thành công.
- Lượt hợp nhất đầu dừng với lỗi `model exceeded the tool-call limit (10)`; lượt chạy lại trên gói tối thiểu bằng `recheck/6/600/16000` giữ nguyên DeepSeek và thành công. Bản đồ cuối loại Expected SARSA, Double Q-learning, n-step TD và các mục mở rộng không có trong nguồn.
- Writer bản đầu dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, cấu hình `write/20/600/32000`, thành công. Writer sửa sau phản biện đã ghi 59 dòng mới và sửa 51 dòng trước khi dừng với lỗi `model exceeded the tool-call limit (20)`; điều phối viên kiểm diff, áp dụng phần hợp lệ và hoàn tất các vá còn thiếu.

### Năm báo cáo độc lập và quyết định

- Góc nhìn sinh viên và kết nối–mạch viết dùng GLM; chuyên gia Học tăng cường, toán học–thuật toán và phản biện học thuật–giảng dạy dùng DeepSeek. Mọi lượt thành công đều có `requested_model=observed_model` và `provider=OpenRouter`.
- Hai lượt DeepSeek đầu cho vai chuyên gia và phản biện dừng với lỗi `model exceeded the tool-call limit (8)`; cả hai chạy lại trên đúng một tệp note bằng `review/5/600/12000`, giữ nguyên model, và hoàn tất ở vòng 2.
- Đã xử lý: phân loại chủ đề 15 là cốt lõi; lộ trình thời gian; điều kiện kết thúc gần chắc chắn của MC; định nghĩa GLIE; Robbins–Monro theo từng cặp; điều kiện hỗ trợ lấy mẫu quan trọng; phân biệt yêu cầu GLIE của SARSA với độ phủ vô hạn của Q-learning; quy ước bước học; phép làm tròn Hoeffding; thuật ngữ tiếng Việt và các câu chuyển.
- Không áp dụng đề xuất thêm every-visit MC, Expected SARSA, Double Q-learning, n-step TD, ví dụ Hoeffding mới hoặc điều kiện ergodic như một giả thiết bắt buộc. Độ phủ vô hạn được phát biểu trực tiếp là giả thiết của định lý; ép tính ergodic sẽ mạnh hơn mức cần thiết và không có trong nguồn.
- Tái kiểm toán học dùng `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`, `recheck/5/600/10000`; tái kiểm mạch dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, `recheck/5/600/8000`. Không còn lỗi chặn bàn giao; các nhận xét nghiêm trọng và trung bình hợp lệ đã được sửa.
- Tái kiểm hẹp sau vá dùng DeepSeek `recheck/4/600/7000` và GLM `recheck/4/600/6000`, đều có model quan sát đúng model yêu cầu. DeepSeek xác nhận không còn lỗi từ mức trung bình trở lên ở GLIE, bước học, SARSA, Q-learning và lấy mẫu quan trọng. GLM phát hiện cách mô tả thời lượng chưa khớp nhãn chủ đề 14; bản cuối coi toàn bộ chủ đề 12 và 14 là hai nhánh bổ sung 5 phút, đồng thời sửa hai câu tiếng Việt còn gượng.
- Đã tự kiểm theo `no-ai-slop/eval.md`: cắt câu hỏi tu từ, lời dẫn rỗng, nhịp câu máy móc và thuật ngữ Anh không cần thiết. Đã rà theo Quill: tuyến dự đoán → chính sách → điều khiển MC → SARSA → Q-learning → tổng hợp truyền liên tục bảng $Q_0$, lượt chung, miền $\mathcal X_{\mathrm{reach}}$ và lịch bước học; không tạo `quill.json`.
- Liên kết material-viewer trong `index.html` thay thế trạng thái `Chưa có`. Nhóm hai tài nguyên Bài giảng/Ghi chú bài giảng là ngoại lệ có chủ ý đối với quy tắc một liên kết của `AGENTS.md`, theo yêu cầu cụ thể của `prompt_lecture_note_deck.md`.

### Cổng kiểm soát ghi chú bài giảng

- Kiểm tra tĩnh: 15 `note-topic-id` duy nhất; 15 khối bài tập, 15 gợi ý và 15 đáp án; không có dấu phân cách công thức `\(...\)` hoặc `\[...\]`; không có `quill.json`, liên kết `.env` hay tệp bí mật trong đầu ra. `index.html` có đúng một liên kết viewer cho Bài 06. `git diff --check` không báo lỗi.
- Lệnh bắt buộc `python3 -m reloadserver 8765` dừng với lỗi `/usr/bin/python3: No module named reloadserver`. Đã dùng webroot cô lập trong `/tmp`, không chứa `.env`, và `python3 -m http.server 8765` làm phương án dự phòng.
- Chromium headless mở viewer từ thẻ Bài 06 ở 1280 × 720 và 800 × 600. Cả hai lượt hiển thị 550 biểu thức KaTeX, 15 bài tập, 30 khối đóng/mở và 15 đáp án; không có lỗi console, request thất bại, tràn ngang hoặc phần tử tràn; phím Enter mở được khối chi tiết.
- Codex Slides yêu cầu Node.js 20 trở lên trong khi môi trường hiện có Node.js 18.19.1. Không tuyên bố đã rà trực quan ghi chú bằng Codex Slides; kiểm định material-viewer cục bộ ở trên là bằng chứng hiển thị của giai đoạn I.

## Giai đoạn II — đồng bộ trang chiếu với ghi chú, ngày 03-09-2026

- Reader lập kế hoạch dùng `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`, cấu hình `plan/10/600/16000`; hoàn tất ở vòng 9 sau khoảng 204 giây. Kế hoạch ánh xạ 15 chủ đề ghi chú vào đủ 37 trang và giữ 7 mạch ngoài.
- Writer bản đầu dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, cấu hình `write/20/600/20000`; một phản hồi vòng 4 có `finish_reason=error`, cầu nối thử lại cùng model và hoàn tất ở vòng 9 sau khoảng 638 giây.
- Writer thêm `data-note-topic-id` cho đủ 37 trang, đồng bộ outline/storyboard, chuẩn hóa thuật ngữ, thời lượng 110 phút cốt lõi cộng hai nhánh 5 phút và 30 phút chữa bài. Ba SVG `greedy-induced-mrp.svg`, `shared-trace.svg`, `target-comparison.svg` được cập nhật nhãn tiếng Việt; hai SVG còn lại giữ nguyên vì đã khớp nguồn và ghi chú.

### Năm báo cáo độc lập và chỉnh sửa

- Góc nhìn sinh viên và kết nối–mạch viết dùng GLM; chuyên gia Học tăng cường, toán học–thuật toán và phản biện học thuật–giảng dạy dùng DeepSeek. Mọi lượt thành công đều có `requested_model=observed_model` và `provider=OpenRouter`.
- Lượt toán DeepSeek đầu dừng đúng với lỗi `model exceeded the tool-call limit (7)`. Lượt chạy lại giữ nguyên model, cô lập đúng deck và dùng `review/4/600/12000`; không còn lỗi từ mức trung bình trở lên.
- Writer chỉnh sửa dùng GLM `write/12/600/12000`, hoàn tất ở vòng 9 sau khoảng 178 giây. Đã sửa điều kiện GLIE và Robbins–Monro ở B06, đích Bellman và phạm vi hội tụ ở D05, điều kiện MC trong bảng E00, các câu chuyển phần, cảnh báo về bước học hằng và thuật ngữ trong SVG.
- Tái rà toán dùng DeepSeek `recheck/3–4/600/4000–8000`; tái rà mạch dùng GLM `recheck/5/600/8000`, sau đó rà ranh giới bằng `recheck/3/600/5000`. Lượt mạch cuối xác nhận không còn lỗi từ mức trung bình trở lên.
- Không áp dụng nhận xét cho rằng A03 thiếu nhãn phần thưởng vì SVG hiện rõ nhãn và giá trị. Không thêm giả thiết ergodic vì deck đã phát biểu trực tiếp điều kiện độ phủ vô hạn cần dùng. Không áp dụng nhận xét rằng Q-learning không có cơ chế độ phủ vì D02 yêu cầu chính sách hành vi cập nhật vô hạn mọi cặp khả đạt. Không áp dụng nhận xét coi cảnh báo `$\alpha=0{,}8$` hằng là lỗi: câu trên trang nói rõ giá trị này không thuộc bảo đảm hội tụ.
- Các mã trang và nhãn phân tuyến do reviewer đề xuất trong ghi chú diễn giả đã bị loại. Ghi chú chỉ giữ câu chuyển tự nhiên; mã nội bộ, phân tuyến và thời lượng chỉ nằm trong outline, storyboard và nhật ký.

### Kiểm định sau chỉnh sửa

- Đã tự kiểm theo `no-ai-slop/eval.md`: cắt lời dẫn rỗng, nhịp câu máy móc, thuật ngữ Anh không cần thiết và câu tổng kết lặp. Đã rà theo Quill: tuyến dự đoán → chính sách → MC → SARSA → Q-learning → tổng hợp → kết luận giữ liên tục bảng $Q_0$, lượt chung, miền $\mathcal X_{\mathrm{reach}}$ và lịch bước học; không tạo `quill.json`.
- Lệnh bắt buộc `python3 -m reloadserver 8765` dừng với lỗi `/usr/bin/python3: No module named reloadserver`. Đã dùng webroot cô lập trong `/tmp`, không chứa `.env`, và `python3 -m http.server 8765` làm phương án dự phòng.
- Chromium headless duyệt đủ 37 trang ở 1280 × 720 và 800 × 600. Lượt đầu phát hiện hộp kết luận B06 chạm chân trang dù phép đo DOM không báo tràn; nội dung đã được rút gọn và render lại. Lượt cuối không có lỗi console, lỗi KaTeX, request thất bại hoặc phần tử tràn; ảnh B06 và E00 xác nhận nội dung không bị cắt. Phím mũi tên phải chuyển ngang và phím mũi tên xuống chuyển dọc đúng cấu trúc.
- Codex Slides không chạy được vì môi trường có Node.js 18.19.1, thấp hơn yêu cầu Node.js 20. Không tuyên bố đã rà trực quan bằng Codex Slides; kiểm tra RevealJS cục bộ và ảnh Chromium là bằng chứng hiển thị cuối.
