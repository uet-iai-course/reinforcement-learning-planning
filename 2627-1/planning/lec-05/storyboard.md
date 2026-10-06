# Storyboard mới Bài 05: Dự đoán phi mô hình

Ngày 28-09-2026. Bản đồ này được lập từ dàn bài mới đã được duyệt, không kế thừa dàn hoặc HTML cũ. HTML, SVG và học liệu đã triển khai; bản đồ đang được đồng bộ sau năm báo cáo độc lập, trước rà lại và kiểm định cuối. [outline.md](outline.md) là đặc tả nội dung, câu hỏi và đáp án từng trang; [analysis.md](analysis.md) lưu phân tích tám bước, nguồn, ký hiệu và đặc tả SVG. Chỉ các mã dưới đây được dùng làm `data-slide-id` trong HTML mới. Mã, thời gian, vai trò và quyết định là dữ liệu quy trình, không hiện trên mặt trang hoặc trong ghi chú diễn giả.

## Hành trình khái niệm

Vấn đề xuyên suốt là ước lượng giá trị của một chính sách cố định khi có tương tác nhưng không biết mô hình. Mạch A xác định đối tượng và dữ liệu; mạch B dùng lợi tức hoàn chỉnh; mạch C xây mục tiêu có thể tính sau một chuyển; mạch D xác định điều kiện và tiêu chuẩn so sánh; mạch E trả lại quyết định lựa chọn phương pháp cho vấn đề mở đầu. Mỗi mạch nhận một thiếu hụt cụ thể từ mạch trước và tạo sản phẩm để mạch sau sử dụng.

| Mạch | Loại phần | Chức năng và đóng góp cho vấn đề trung tâm | Đầu vào | Đầu ra | Trang | Phút | Kiểm tra |
|---|---|---|---|---|---|---:|---|
| A. Mở đầu: đánh giá chính sách từ dữ liệu | Mở đầu | Xác định cùng đối tượng giá trị khi đầu vào chuyển từ mô hình sang mẫu. | Chính sách, giá trị và Bellman kỳ vọng từ bài trước. | Nhu cầu dùng lượt hoàn chỉnh để lấy mẫu lợi tức. | L05-A01–L05-A05 | 12 | L05-A05 |
| B. Dự đoán Monte Carlo | Phát triển kiến thức và ứng dụng | Xây dựng ước lượng từ lợi tức, lựa chọn lần ghé và bước học. | Bài toán dự đoán và mẫu tương tác của mạch A. | Thuật toán MC hoàn chỉnh và giới hạn phải chờ kết thúc lượt. | L05-B01–L05-B13 | 35 | L05-B13 |
| C. Dự đoán sai phân thời gian TD(0) | Phát triển kiến thức và ứng dụng | Thay phần lợi tức chưa quan sát bằng giá trị trạng thái sau để cập nhật mỗi bước. | Lợi tức, bảng V và bước học của mạch B. | Bảng sau từng chuyển và cách phân biệt mục tiêu, sai số, giá trị. | L05-C01–L05-C10 | 27 | L05-C10 |
| D. So sánh theo dữ liệu và giả thiết | Phát triển kiến thức và ứng dụng tổng hợp | So sánh đúng đại lượng, điều kiện và tiêu chuẩn trên cùng dữ liệu. | MC và TD(0) đã được thực hiện trên cùng hai lượt. | Căn cứ chọn phương pháp; phân biệt mẫu mới với dữ liệu cố định. | L05-D01–L05-D12 | 34 | L05-D12 |
| E. Kết luận và tự kiểm tra | Kết luận | Giải quyết lại bài toán mở đầu bằng lựa chọn phương pháp có điều kiện. | Cơ chế, kết quả số và giới hạn ở mạch B–D. | Năng lực tính, giải thích, lựa chọn và các bài tập củng cố có nguồn. | L05-E01–L05-E05 | 12 | L05-E04 |

Tổng **45 trang, 120 phút**. Mỗi mạch là một `<section>` ngoài; từng trang là `<section>` con. Năm mạch đáp ứng khoảng 5–7, không cần ngoại lệ. 30 phút chữa bảy bài HW05 theo bảng trong outline nằm ngoài tổng này. Không thêm phần mã vì nguồn không có nội dung mã.

## Chu trình của các cụm khái niệm

### Cụm A: xác định bài toán và tiên quyết, 12 phút

- Dạng: nhắc khái niệm đã học, không phải một thuật toán mới. Kiến thức đầu vào là chính sách, giá trị và Bellman kỳ vọng.
- Mở đúng thứ tự: L05-A01 tên bài; L05-A02 nội dung, mục tiêu và tiên quyết; L05-A03 động lực; L05-A04 dữ liệu; L05-A05 kiểm tra riêng.
- Vấn đề: L05-A03 thiếu mô hình để tính kỳ vọng. Trực giác và đối tượng: L05-A04 nối một chuyển quan sát với giá trị dài hạn. Ví dụ và ứng dụng nhận diện: L05-A05 dùng chuyển S→X thưởng 0. Hình thức mới không áp dụng; định nghĩa giá trị chỉ nhắc lại và lợi tức được hình thức đầy đủ sau ví dụ ở L05-B03.
- Sản phẩm: người học phân biệt mẫu với mô hình, giá trị chính sách cố định với mục tiêu tối ưu; trả lời đủ câu L05-A05 mà chưa cần công thức MC/TD.
- Câu nối ra: “Các lượt kết thúc cung cấp những kết quả quan sát để ước lượng cùng giá trị kỳ vọng đó.”
- Lý do gộp: tiên quyết đã học không cần chu trình sáu trang; MC mới được xây theo chu trình đầy đủ tiếp theo. Toàn mạch 12 phút, gồm kiểm tra 3 phút.

### Cụm B: Monte Carlo và cách cập nhật, 35 phút

- Dạng kết hợp: khái niệm lợi tức và ước lượng MC; thuật toán MC với hai trục lựa chọn. Năng lực nhận diện là chọn đúng mẫu và phân biệt trọng số; năng lực sử dụng là tính bảng sau từng lượt.
- Vấn đề + ví dụ dẫn nhập: L05-B01 đặt nhiệm vụ dự đoán S/X; L05-B02 cho hai lượt cụ thể. Ví dụ làm rõ thiếu hụt kỳ vọng chưa biết bằng hai kết quả quan sát +1/−1; chuỗi L,S,X,G, cùng chính sách và $\gamma=1$ được dùng tiếp.
- Trực giác: L05-B02 định nghĩa lần ghé và ghi lợi tức dưới từng nút. Hình thức lợi tức: L05-B03 sau phép cộng số, kèm bảng tính ngược. Ví dụ lựa chọn: L05-B04 phát biểu hai quy tắc, lập bảng thời điểm ghé, giải thích trọng số $2/3$ và nêu kỳ vọng $v_\pi(s)$ của từng mẫu theo tính Markov, trước định nghĩa ước lượng L05-B05 (bảng theo dõi $n$, tổng, $V_n$ tại $X$).
- Chu trình phụ bước học: vấn đề tính trung bình mới chỉ từ trung bình cũ, số mẫu và mẫu mới + trực giác (trục số) + tính tay hai cách L05-B06; hình thức và chứng minh L05-B07; ví dụ bước hằng trước quy tắc L05-B08; ứng dụng phân loại L05-B09. Bốn trang này nằm trong 35 phút, không là một mạch riêng.
- Quy trình đầy đủ: L05-B10 có đầu vào, khởi tạo, tính lùi lợi tức, chọn xuôi lần ghé, bước học, trạng thái kết thúc và dừng. Dữ kiện truyền sang ký hiệu: các giá trị +1/−1 thành $g_i(s)$; số lần được chọn thành $N(s)$; phép sửa 0→0.5 thành cập nhật với $\alpha$.
- Ứng dụng: L05-B11 chạy $e_2$ sau $e_1$ cho cả hai quy tắc lần ghé. Điều kiện thống kê: L05-B12. Kiểm tra riêng: L05-B13; đáp án trung bình của X lần ghé đầu 0, mọi lần ghé $1/3$, bước hằng lần ghé đầu −0.25.
- Câu nối giữa các bước: kết quả sau một lần ghé → cần quy tắc chọn mẫu → cần cách kết hợp mẫu → cần quy trình giữ đúng cả hai lựa chọn → cần phân biệt kết quả tính được với bảo đảm thống kê.
- Câu nối ra: “Lợi tức đầy đủ chỉ có khi lượt kết thúc; dữ liệu của một chuyển chưa xác định phần còn lại.”
- Phân bổ nội bộ: L05-B01–L05-B05 12 phút, L05-B06–L05-B09 10 phút, L05-B10–L05-B13 13 phút. Không bỏ bước của chu trình chính; nhiều bước được gộp trong cùng ví dụ và được ghi rõ ở trên.

### Cụm C: TD(0), 27 phút

- Dạng thuật toán dự đoán theo chính sách, phi mô hình, dạng bảng. Tiên quyết là lợi tức, bảng V, bước học và mẫu chuyển của mạch B.
- Vấn đề: L05-C01 tiền tố chưa kết thúc nên MC chưa có $G_t$. Trực giác: L05-C02 thưởng đã biết cộng ước lượng còn lại. Ví dụ tính tay: L05-C03 với V(S)=0, V(X)=0.5, thưởng 0, gamma 1, alpha 0.5 cho mục tiêu 0.5 và giá trị mới 0.25.
- Hình thức: L05-C04 gắn các số với $Y_t,\delta_t,V_t$. Quy trình đầy đủ: L05-C05 xác định đầu vào, khởi tạo, hành vi theo $\pi$, thứ tự đọc/ghi và hai loại dừng. Trường hợp biên: L05-C06 trạng thái kết thúc và tự chuyển.
- Ứng dụng: L05-C07 chạy cả $e_1$ từ 0; L05-C08 tiếp tục $e_2$. Bảng cho trước ở L05-C03 được kiểm lại từ kết quả L05-C07, nên không có tiên quyết vòng. L05-C09 xác định chi phí của đúng quy trình này.
- Kiểm tra riêng: L05-C10 tách hai chuyển xuất phát độc lập từ cùng bảng. Đáp án V(S)=0.375 với chuyển S→X và −0.375 với chuyển S→L, các phần tử khác giữ nguyên.
- Câu nối: thiếu phần đuôi → dùng V của trạng thái sau → tính một mục tiêu → viết quy tắc tổng quát → thực hiện toàn lượt → đánh giá bảng kết quả. Đầu ra cho D là các bảng MC/TD trên cùng dữ liệu, không chỉ tên hai thuật toán.
- Mọi bước có trang rõ; không áp dụng yêu cầu chứng minh hội tụ tại đây vì điều kiện so sánh được đặt ở L05-D07 sau khi cơ chế đã hoàn chỉnh. 27 phút gồm kiểm tra 3 phút.

### Cụm D1: so sánh mục tiêu, dữ liệu và bảo đảm, 19 phút trước kiểm tra chung

- Dạng khái niệm và ứng dụng phân tích, nhận đầu vào là hai thuật toán đã chạy. Năng lực cần kiểm là xác định đúng đối tượng của kết luận: mục tiêu, ước lượng, mẫu hay nghiệm trên dữ liệu.
- Vấn đề + ví dụ dẫn nhập: L05-D01 hai bảng khác nhau trên cùng hai lượt; L05-D02 cung cấp giá trị chuẩn để phân biệt ước lượng với giá trị thật. L05-D03 chuỗi dài làm cụ thể tác động của độ dài và chiết khấu.
- Trực giác và ví dụ tính: L05-D04 hai lợi tức 0.970299 và −0.99; cả hai khác giá trị chuẩn tại $S$ của chuỗi dài, làm rõ nhu cầu tách kỳ vọng khỏi biến thiên; không tính phương sai tổng thể. Dữ kiện bốn/hai chuyển và phần thưởng cuối nối trực tiếp về chỉ số của $G_t$ ở L05-B03.
- Ví dụ nối trước hình thức: L05-D05 quay về chuỗi ngắn đã biết, giữ $\gamma=1,V(X)=0.5,V(L)=0$; hai mục tiêu $-1,0.5$ với xác suất $0.2,0.8$ cho kỳ vọng $0.2$, khác $v_\pi(S)=11/21$. Mục tiêu học tập là phân biệt giữ bảng cố định với lấy trung bình qua chuyển kế tiếp. Dữ kiện của B01/C03/D02 truyền sang $R,S_{t+1},V$ trong đẳng thức HT5. Hình thức: L05-D05 gọi tên độ chệch sau ví dụ số rồi nêu công thức độ chệch tổng quát; L05-D06 nêu bất đẳng thức phương sai cho mục tiêu lý tưởng và giới hạn của nó với bảng $V$ đang học. Ghi chú giải thích V cố định nhưng $V(S_{t+1})$ vẫn ngẫu nhiên. L05-D07 nêu điều kiện hội tụ, không suy từ một ví dụ hữu hạn.
- Ứng dụng tiếp: các phân biệt mẫu mới/dữ liệu cố định và tiêu chuẩn đánh giá được dùng ở L05-D08–L05-D11. Kiểm tra L05-D12 đo cả hai cụm D1/D2, thời gian chỉ tính một lần trong 15 phút D2.
- Câu nối ra: “Khi không có thêm mẫu, việc dùng lại cùng dữ liệu tạo bài toán so sánh theo tiêu chuẩn trên tập dữ liệu đó.”
- Không áp dụng giả mã độc lập cho D1 vì đây là phân tích hai quy tắc đã có. Không đưa điều khiển hoặc xấp xỉ hàm làm phản ví dụ mới. Các bước khái niệm được gộp theo đại lượng cần phân biệt; không coi hai quỹ đạo là chứng minh.

### Cụm D2: dự đoán trên tám lượt cố định, 15 phút gồm kiểm tra chung

- Dạng kết hợp: quy trình theo lô phục vụ khái niệm hai tiêu chuẩn hữu hạn mẫu. Đầu vào là MC, TD, lợi tức, bảng V và phân biệt với mẫu mới ở L05-D07.
- Vấn đề + ví dụ: L05-D08 A chỉ có lợi tức trực tiếp 0 nhưng luôn chuyển tới B; dữ liệu B gồm sáu kết quả 1 và hai kết quả 0. Trực giác là hai nguồn thông tin khác nhau cùng xuất phát từ một tập dữ liệu.
- Bước tính tay: L05-D09 từ V=0, alpha 1/8 cho cả hai phương pháp bảng sau quét đầu (0,0.75). Hình thức và quy trình đầy đủ cùng trang: giữ $V_k$, cộng gia số, ghi đồng thời, dừng theo epsilon hoặc ngân sách K. Trên mặt trang có một lượt tính mẫu cạnh quy trình năm bước; phép cộng từng gia số và phép ghi đồng thời đều hiển thị, có khai báo ký hiệu. Điều kiện ổn định riêng của alpha và chi phí vẫn nằm trong ghi chú.
- Ứng dụng và nghiệm: L05-D10 tìm trung bình lợi tức (0,0.75); L05-D11 tìm nghiệm quan hệ thực nghiệm (0.75,0.75). Bước TD tiếp ở L05-D11 cho (0.09375,0.75), giúp kiểm rằng hai lượt quét chưa đồng nghĩa hội tụ. Dùng nguyên gamma 1, alpha 1/8 của L05-D09.
- Dữ kiện sang hình thức: sáu lần thưởng 1 và tám lần ghé B tạo $6-8V(B)$; một chuyển A→B thưởng 0 tạo $V(B)-V(A)$. Mô hình thực nghiệm chỉ diễn giải nghiệm, không được đưa vào đầu vào học.
- Kiểm tra riêng mạch D: L05-D12, 4 phút, yêu cầu nêu hai tiêu chuẩn và bác bỏ các mệnh đề tuyệt đối bằng điều kiện đã học. Câu hỏi không yêu cầu nhớ tên kết quả tối ưu của mô hình thực nghiệm.
- Câu nối ra: “Phương pháp dự đoán phải được chọn theo dữ liệu có sẵn và tiêu chuẩn đánh giá.” Không bỏ bước chu trình. 2+3+3+3+4=15 phút; tổng D1+D2=34 phút.

### Cụm E: lựa chọn, tự kiểm và bài tập, 12 phút

- Loại kết luận: không mở khái niệm trọng tâm mới. Đầu vào là các cơ chế, phép tính, điều kiện và hai tiêu chuẩn đã có.
- Thu hồi bài toán ở L05-E01: cùng mục tiêu giá trị chính sách cố định, lựa chọn dựa trên dữ liệu hoàn chỉnh, tiền tố hay dữ liệu cố định. L05-E02 tổng kết hai phương pháp theo sáu tiêu chí có điều kiện và nối sang Bài 06.
- Ứng dụng tự luyện: L05-E03 dẫn đủ bảy bài HW05 theo nhóm sản phẩm, với hiệu chỉnh tiền đề được ghi rõ. Kiểm tra riêng L05-E04 phối hợp chọn mẫu, chọn mục tiêu và tiêu chuẩn so sánh. L05-E05 gắn tài liệu đọc với năng lực cần củng cố.
- Chu trình mới không áp dụng: các bước vấn đề, trực giác và hình thức đã được xây dựng ở A–D; kết luận chỉ thu hồi và đánh giá. Câu hỏi L05-E04 không sử dụng công thức hoặc giả thiết chưa dạy.
- Đầu ra: người học có thể nêu cách dự đoán từ dữ liệu, thực hiện một cập nhật và giới hạn kết luận. 12 phút gồm kiểm tra 4 phút; 30 phút chữa HW05 được tính riêng, không giấu trong kết luận.

## Ràng buộc bố cục và ghi chú

Một luận điểm trên mỗi trang; công thức và bảng dài được chia theo các bước đã định, không thu chữ để giữ cả báo cáo. SVG theo đặc tả ở analysis.md, công thức/giả mã/bảng dùng KaTeX/HTML. Giữ 1280×720, `lang="vi"`, CSS chung và thư viện cục bộ theo mẫu. Mỗi SVG có mô tả cụ thể, nhãn và hình dạng phân biệt trạng thái kết thúc; thưởng trên cạnh không đồng nhất với giá trị trạng thái kết thúc. Các SVG đã được tạo và dùng trong HTML/học liệu; các thay đổi trực quan sau rà cần kiểm lại trên cả hai bề mặt.

Các trang L05-B10, L05-C05 và L05-D09 có nguy cơ quá tải cao nhất. L05-B10 dùng hai khối tính lợi tức rồi chọn/cập nhật với khoảng 10–12 dòng; L05-C05 một giả mã khoảng 10 dòng; L05-D09 một ví dụ quét đầu cạnh sơ đồ quy trình. Khai triển trọng số L05-B08, chứng minh phương sai L05-D06, điều kiện alpha riêng A–B L05-D09 và hệ năm trạng thái L05-D03 thuộc ghi chú. Kiểm hiển thị thực tế sau triển khai quyết định việc giảm nội dung mặt trang, không được làm mất giả thiết trong ghi chú.

Ghi chú diễn giả chỉ chứa giải thích học thuật, giả thiết, lỗi dễ nhầm, đáp án và nguồn. Không chép các trường “quyết định”, thời lượng, mã trang, chỉ dẫn đọc, thao tác hoặc yêu cầu người soạn vào ghi chú. Mọi lời mời người học thực hiện nhiệm vụ dùng nhãn “Câu hỏi:”.

## Từng trang: lý do tồn tại và kết nối

### Mạch A: Mở đầu: đánh giá chính sách từ dữ liệu

#### L05-A01: Dự đoán phi mô hình

- **Lý do tồn tại và nhu cầu:** Cập nhật học kỳ và chuẩn hóa tên tiếng Việt, giữ đúng chủ đề nguồn.
- **Vai trò, mục tiêu và sản phẩm:** Mở đầu; MT1. Đầu ra là xác định bài toán đánh giá một chính sách cố định bằng Monte Carlo và sai phân thời gian.
- **Đầu vào → đầu ra:** Nhận kiến thức đánh giá chính sách từ bài trước → xác định tuyến bài ở L05-A02.
- **Dữ kiện/hình thức được truyền:** Không áp dụng; ký hiệu được chuẩn bị ở L05-A04.
- **Nguồn và quyết định:** L05 tr.1; thông tin học phần theo AGENTS.md và index.html. Quyết định `sửa`.
- **Bố cục và đối tượng:** Không cần hình; trang tên xác định đúng bài và đối tượng học.
- **Thời lượng:** 1 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-A02: Nội dung và mục tiêu

- **Lý do tồn tại và nhu cầu:** Thay mục lục ôn điều khiển và phép co bằng sườn Sutton–Barto đã được yêu cầu.
- **Vai trò, mục tiêu và sản phẩm:** Bản đồ và tiên quyết; MT1–MT6. Đầu ra là ba nhiệm vụ được kiểm trong bài: tính/chọn mẫu, thực hiện cập nhật và so sánh theo giả thiết.
- **Đầu vào → đầu ra:** Tên bài L05-A01 → giới hạn thiếu mô hình ở L05-A03; MC và TD cùng giải một đối tượng dự đoán.
- **Dữ kiện/hình thức được truyền:** Không đưa công thức mới; nhắc tên $v_\pi$ nhưng giải nghĩa bằng lời.
- **Nguồn và quyết định:** L05 tr.2, 15; SB Ch.5 tr.91, Ch.6 tr.119. Quyết định `sửa`.
- **Bố cục và đối tượng:** Sơ đồ mũi tên bằng HTML hoặc SVG nội dòng; mỗi nút là một đầu ra học tập, không chỉ tên phần.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Ba thẻ mục tiêu được viết lại theo ba mạch nội dung: Monte Carlo; sai phân thời gian TD(0); so sánh hai phương pháp (độ chệch, phương sai, điều kiện hội tụ, dữ liệu cố định). Lý do: thẻ cũ không khớp mạch B–D và thẻ "So sánh có điều kiện" mơ hồ.

#### L05-A03: Đánh giá chính sách khi chưa biết mô hình

- **Lý do tồn tại và nhu cầu:** Thu gọn phần ôn thành đúng thiếu hụt tạo nhu cầu MC; không dạy lại điều khiển.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề; MT1. Người học cần giải thích hoặc thực hiện được kết luận: Các mẫu tương tác có thể thay dữ liệu mô hình trong việc ước lượng giá trị của cùng chính sách.
- **Đầu vào → đầu ra:** Năng lực dự đoán L05-A02 → cần mô tả chính xác mẫu và đại lượng ở L05-A04.
- **Dữ kiện/hình thức được truyền:** Không cần khai triển Bellman; khác biệt ở đầu vào được thiết lập trước công thức.
- **Nguồn và quyết định:** L05 tr.6, 15–16; SB Ch.5 tr.91; UCL tr.3; ST tr.2–5. Quyết định `gộp`.
- **Bố cục và đối tượng:** Hai cột dữ liệu mô hình và dữ liệu mẫu cùng hướng tới nhãn giá trị của chính sách; chưa có cây xác suất chi tiết.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở nêu bài toán dự đoán: cho $\pi$ cố định, ước lượng $v_\pi(s)$ tại mọi trạng thái. Lý do: câu cũ là cụm danh từ cụt, chưa nêu bài toán.

#### L05-A04: Mẫu chuyển và giá trị cần ước lượng

- **Lý do tồn tại và nhu cầu:** Khôi phục đủ kiểu đại lượng và quy ước trước khi dùng lại ký hiệu nguồn.
- **Vai trò, mục tiêu và sản phẩm:** Trực giác và nhắc định nghĩa; MT1. Người học cần giải thích hoặc thực hiện được kết luận: Một chuyển quan sát được cung cấp phần thưởng tức thời; giá trị mô tả kỳ vọng phần thưởng tích lũy về sau.
- **Đầu vào → đầu ra:** Bài toán L05-A03 → xác định đối tượng và dữ liệu đủ cho câu kiểm tra L05-A05; chuẩn bị quỹ đạo L05-B01.
- **Dữ kiện/hình thức được truyền:** HT1 ở mức $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$; tổng định nghĩa $G_t$ được xây dựng sau ví dụ ở L05-B03. $0\le\gamma\le1$ và $T$ là thời điểm kết thúc được khai báo bằng lời.
- **Nguồn và quyết định:** L05 tr.3, 15–17; SB §5.1 tr.92, §6.1 tr.119–120. Quyết định `gộp`.
- **Bố cục và đối tượng:** Một cạnh chuyển có nhãn hành động và thưởng; nhãn $t,t+1$ đặt đúng vị trí.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Giữ mẫu chuyển, $v_\pi=\mathbb E_\pi[G_t\mid S_t=s]$, phân biệt $v_\pi$/$V$ và giả thiết dữ liệu; chuyển $T$, $\mathcal S^+$, giá trị kết thúc bằng 0 và điều kiện $\gamma$ sang L05-B03. Lý do: giảm số ký hiệu mở cùng lúc trước ví dụ.

#### L05-A05: Kiểm tra mẫu chuyển và mô hình

- **Lý do tồn tại và nhu cầu:** Kiểm tra tiên quyết và nhu cầu trước khi mở khái niệm MC, theo yêu cầu mỗi mạch có trang kiểm tra riêng.
- **Vai trò, mục tiêu và sản phẩm:** Kiểm tra riêng của mạch A; MT1. Người học cần giải thích hoặc thực hiện được kết luận: Dữ liệu mẫu và đối tượng dự đoán phải được xác định trước khi chọn thuật toán.
- **Đầu vào → đầu ra:** Quy ước L05-A04 → nhận diện đúng bài toán → L05-B01 dùng các lượt hoàn chỉnh để ước lượng đại lượng đó.
- **Dữ kiện/hình thức được truyền:** HT1; chỉ dùng tiên quyết đã nhắc, chưa yêu cầu công thức MC hoặc TD.
- **Nguồn và quyết định:** L05 tr.15–16; HW05 bài 2; câu hỏi biên tập từ dữ kiện chuỗi nguồn. Quyết định `thêm`.
- **Bố cục và đối tượng:** Một cạnh $S\to X$ có nhãn thưởng 0; không hiển thị xác suất chuyển chưa được cung cấp trong câu hỏi.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Kiểm tra và sản phẩm cần nộp:** Xác định (a) bốn thành phần của mẫu quan sát; (b) đại lượng cần ước lượng khi chính sách giữ cố định; (c) thông tin còn thiếu để đánh giá bằng quy hoạch động.
- **Đáp án đối chiếu:** $(s,a,0,s')$ với $a$ là hành động sang phải; cần $v_\pi$ tại các trạng thái quan tâm; thiếu phân phối chuyển và phần thưởng cho các khả năng, một mẫu không thay thế toàn bộ mô hình.
- **Tiêu chí:** Đúng chỉ số phần thưởng, không chuyển mục tiêu sang tìm chính sách tối ưu, không suy xác suất từ một mẫu.
- **Phân bổ hoạt động:** 1 phút tự xác định, 1 phút trả lời, 1 phút đối chiếu; đã nằm trong 3 phút.
- **Rà soát 01-10-2026:** `sửa`; Câu hỏi dùng ký hiệu chung $s\to s'$ với hành động $a$ và thưởng 0, không dùng $S,X$ trước khi chuỗi ngắn được giới thiệu. Đáp án: $(s,a,0,s')$.
- **Sửa sau rà 01-10-2026:** `sửa`; Ngữ cảnh "tác tử" thay "robot"; hành động sang phải ký hiệu $a$.

### Mạch B: Dự đoán Monte Carlo

#### L05-B01: Chuỗi ngắn và ý tưởng Monte Carlo

- **Lý do tồn tại và nhu cầu:** Giữ môi trường nguồn làm ví dụ xuyên suốt, đặt trước định nghĩa MC.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề và ví dụ dẫn nhập MC; MT2. Người học cần giải thích hoặc thực hiện được kết luận: Một lượt kết thúc cho biết kết quả thực tế sau khi ghé trạng thái.
- **Đầu vào → đầu ra:** Nhu cầu mẫu ở L05-A05 → kết quả của hai lượt cụ thể L05-B02.
- **Dữ kiện/hình thức được truyền:** HT1 được gắn với $\mathcal S=\{S,X\}$; chưa giải hệ Bellman.
- **Nguồn và quyết định:** L05 tr.19–20; HW05 bài 7. Quyết định `giữ`.
- **Bố cục và đối tượng:** `short-walk.svg`; xác suất trên cạnh và thưởng nhận khi vào trạng thái kết thúc tách khỏi nhãn giá trị trạng thái kết thúc.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Thêm định nghĩa lượt và hộp ý tưởng Monte Carlo (giá trị là kỳ vọng lợi tức, nên ước lượng bằng trung bình lợi tức quan sát trong các lượt hoàn chỉnh) theo nguồn tr.17. Lý do: ý tưởng cốt lõi trước đây chưa xuất hiện trên mặt trang.

#### L05-B02: Lợi tức sau mỗi lần ghé

- **Lý do tồn tại và nhu cầu:** Tách phép tính trên dữ liệu khỏi công thức nguồn tr.17 để tạo trực giác trước ký hiệu.
- **Vai trò, mục tiêu và sản phẩm:** Trực giác và ví dụ; MT2. Người học cần giải thích hoặc thực hiện được kết luận: Mỗi lần ghé trạng thái gắn với phần thưởng còn lại của lượt đó.
- **Đầu vào → đầu ra:** Môi trường L05-B01 → đại lượng còn lại sau từng thời điểm → tổng quát hóa ở L05-B03.
- **Dữ kiện/hình thức được truyền:** Chưa viết tổng ký hiệu; tính trực tiếp $0+0+0+1=1$ và $0+0-1=-1$.
- **Nguồn và quyết định:** L05 tr.20, 22, 29; HW05 bài 7. Quyết định `tách`.
- **Bố cục và đối tượng:** Câu định nghĩa "lần ghé"; `episode-one.svg` và `episode-two.svg`, mỗi lần ghé là một nút riêng, hàng $G_t$ dưới từng nút, ngoặc nét đứt đánh dấu phần đuôi sau $t=1$ trong $e_1$; hộp tính hai phần đuôi.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.
- **Rà soát 06-10-2026:** `sửa`; Định nghĩa "lần ghé" lên mặt trang; SVG thêm hàng $G_t$ và ngoặc phần đuôi. Lý do: bố cục cũ hứa đánh dấu phần đuôi nhưng hình không có; phép cộng chỉ nằm trong ghi chú.

#### L05-B03: Lợi tức chiết khấu

- **Lý do tồn tại và nhu cầu:** Sửa dòng công thức bị cắt trong nguồn và thiết lập chỉ số dùng lại ở chuỗi dài.
- **Vai trò, mục tiêu và sản phẩm:** Hình thức khái niệm lợi tức; MT2. Người học cần giải thích hoặc thực hiện được kết luận: Phần thưởng nhận ngay có số mũ 0; mỗi bước xa hơn thêm một hệ số chiết khấu.
- **Đầu vào → đầu ra:** Phép cộng L05-B02 → lợi tức có chỉ số chính xác → lựa chọn những lợi tức đưa vào trung bình ở L05-B04; thứ tự tính ngược dùng lại ở L05-B10.
- **Dữ kiện/hình thức được truyền:** HT1: $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}=R_{t+1}+\gamma G_{t+1}$.
- **Nguồn và quyết định:** L05 tr.17; SB §5.1 tr.92 và §6.1 tr.119–120. Quyết định `sửa`.
- **Bố cục và đối tượng:** Câu mở khai báo $T$, $G_T=0$, $\gamma$; một dòng công thức tổng và truy hồi; bảng tính ngược trên $e_1$ (hàng $R_{t+1}$, $G_t$); chú thích nối về L05-B02.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề gọi tên khái niệm. Câu mở khai báo $T$ và $0\le\gamma\le1$; $\mathcal S^+$ và quy ước trạng thái kết thúc chuyển từ L05-A04 vào ghi chú diễn giả.
- **Sửa sau rà 01-10-2026:** `sửa`; Câu mở thêm "giá trị ở trạng thái kết thúc bằng $0$".
- **Rà soát 06-10-2026:** `sửa`; Bảng tính ngược trên $e_1$ thay thẻ $G_0,G_3$; gộp hai công thức; bỏ CSS cục bộ. Lý do: công thức truy hồi chưa được dùng trên mặt trang, thiếu nối về L05-B02.

#### L05-B04: Lần ghé đầu tiên và mọi lần ghé

- **Lý do tồn tại và nhu cầu:** Bổ sung quy tắc mọi lần ghé từ SB và tạo số khác nhau để đo đúng sự phân biệt.
- **Vai trò, mục tiêu và sản phẩm:** Ví dụ lựa chọn mẫu; MT2. Người học cần giải thích hoặc thực hiện được kết luận: Hai quy tắc MC khác nhau ở những lần ghé được đưa vào tập mẫu; theo tính Markov, mỗi mẫu của cả hai quy tắc có kỳ vọng $v_\pi(s)$.
- **Đầu vào → đầu ra:** Lợi tức L05-B03 → chọn dữ liệu thống kê → định nghĩa ước lượng MC L05-B05.
- **Dữ kiện/hình thức được truyền:** HT2 được chuẩn bị bằng tập mẫu; chưa đồng nhất quy tắc chọn mẫu với bước học.
- **Nguồn và quyết định:** L05 tr.18, 20, 22; SB §5.1 tr.92–93; phép tính từ hai lượt nguồn. Quyết định `sửa`.
- **Bố cục và đối tượng:** Hai dòng quy tắc có nhãn đậm (lần ghé đầu tiên lấy $G_t$ tại thời điểm sớm nhất có $S_t=s$; mọi lần ghé lấy $G_t$ tại mọi thời điểm có $S_t=s$); ký hiệu $t_1<t_2<\cdots$ ở ghi chú; bảng hai hàng S/X với cột thời điểm ghé ghi rõ từng lượt và hai cột quy tắc; câu giải thích tại $X$ mọi lần ghé lấy hai mẫu từ $e_1$ và một mẫu từ $e_2$, nên $e_1$ chiếm trọng số $2/3$; hộp kỳ vọng theo tính Markov. Các tập mẫu và số đếm là HTML. Lập luận thời điểm dừng ở ghi chú.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở nêu lý do cần quy tắc: một trạng thái có thể xuất hiện nhiều lần trong một lượt.
- **Rà soát 06-10-2026:** `sửa`; Phát biểu hai quy tắc (hai dòng nhãn đậm); cột thời điểm ghé ghi rõ từng lượt; câu giải thích trọng số $2/3$ để bảng ($0$ và $1/3$ tại $X$) không mâu thuẫn với hộp; hộp nêu theo tính Markov mỗi mẫu của cả hai quy tắc có kỳ vọng $v_\pi(s)$ (yêu cầu của người dùng). Lý do: trang cũ không phát biểu quy tắc, hộp cuối không mang thông tin.

#### L05-B05: Ước lượng Monte Carlo

- **Lý do tồn tại và nhu cầu:** Tách định nghĩa ước lượng khỏi lựa chọn lần ghé và điều kiện thống kê.
- **Vai trò, mục tiêu và sản phẩm:** Hình thức MC; MT2–MT3. Người học cần giải thích hoặc thực hiện được kết luận: MC ước lượng giá trị bằng cách kết hợp các lợi tức đã chọn tại trạng thái đó.
- **Đầu vào → đầu ra:** Tập mẫu L05-B04 → phép kết hợp chính thức → nhu cầu cập nhật khi nhận thêm mẫu L05-B06.
- **Dữ kiện/hình thức được truyền:** HT2: $V_n(s)=\frac1n\sum_{i=1}^{n}g_i(s)$.
- **Nguồn và quyết định:** SB §5.1 tr.92–93; L05 tr.18. Quyết định `sửa`.
- **Bố cục và đối tượng:** Dòng ký hiệu $g_i(s)$, $n=N(s)$; công thức đặt cạnh bảng theo dõi tại X (mọi lần ghé) với cột $g_n(X)$, $n$, tổng, $V_n(X)$; không cần môi trường mới.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.
- **Rà soát 06-10-2026:** `sửa`; Bảng theo dõi $n$, tổng, $V_n(X)$ thay hai thẻ lặp L05-B04; ghi chú nêu dạng bộ đếm và tổng của nguồn tr.18. Lý do: tránh trùng và chuẩn bị trạng thái đầu của L05-B06.

#### L05-B06: Cập nhật trung bình khi có mẫu mới

- **Lý do tồn tại và nhu cầu:** Khôi phục ví dụ số trước công thức gia tăng thay cho việc trình bày công thức ngay ở nguồn tr.21.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề, trực giác và tính tay gia tăng; MT3. Người học cần giải thích hoặc thực hiện được kết luận: Trung bình mới bằng trung bình cũ dịch về phía mẫu mới một phần $1/n$ sai lệch; chỉ cần số mẫu, trung bình cũ và mẫu mới.
- **Đầu vào → đầu ra:** Tổng L05-B05 → phép điều chỉnh dùng đủ thông tin → chứng minh đẳng thức tổng quát L05-B07.
- **Dữ kiện/hình thức được truyền:** Ví dụ $1+\frac13(-1-1)=\frac13$ chuẩn bị HT3.
- **Nguồn và quyết định:** SB §2.4 tr.30–31; L05 tr.18; dữ liệu X từ L05-B04. Quyết định `thêm`.
- **Bố cục và đối tượng:** Câu yêu cầu (tính trung bình mới chỉ từ trung bình cũ, số mẫu và mẫu mới) và dòng dữ kiện (2 mẫu, trung bình 1, mẫu mới −1); hai thẻ "Tính lại từ tổng" và "Sửa trung bình cũ"; trục số SVG nội tuyến; hộp "một phần ba của sai lệch".
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở nêu yêu cầu chỉ lưu trung bình và số mẫu. Lý do: vấn đề của trang trước chỉ có trong ghi chú.
- **Rà soát 06-10-2026:** `sửa`; Hai cách tính cạnh nhau, trục số, lý do bộ nhớ sửa theo SB §2.4. Lý do: phân biệt hai cách tính và nêu cấu trúc dịch về mục tiêu dùng lại ở L05-B08 và mạch C.

#### L05-B07: Trung bình gia tăng

- **Lý do tồn tại và nhu cầu:** Giữ công thức nguồn và thêm suy diễn ngắn đủ để hiểu vai trò bộ đếm.
- **Vai trò, mục tiêu và sản phẩm:** Hình thức và chứng minh ngắn; MT3. Người học cần giải thích hoặc thực hiện được kết luận: Bước học nghịch đảo số mẫu tái tạo chính xác trung bình số học.
- **Đầu vào → đầu ra:** Phép tính L05-B06 → quy tắc trung bình đúng với mọi n → xét thay đổi trọng số bằng bước hằng ở L05-B08.
- **Dữ kiện/hình thức được truyền:** HT3: $V_n(s)=V_{n-1}(s)+\frac1n[g_n(s)-V_{n-1}(s)]$.
- **Nguồn và quyết định:** SB §2.4 tr.30–31; L05 tr.21. Quyết định `giữ`.
- **Bố cục và đối tượng:** Hai dòng biến đổi lớn; không thêm hình cạnh công thức.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Gọi tên mục tiêu cập nhật: $g_n(s)$ là mục tiêu trong $V\leftarrow V+\alpha[\text{mục tiêu}-V]$.

#### L05-B08: Bước học hằng

- **Lý do tồn tại và nhu cầu:** Bổ sung giả thiết bước học thiếu trong nguồn và phân biệt trung bình với trọng số mũ.
- **Vai trò, mục tiêu và sản phẩm:** Ví dụ rồi quy tắc biến thể; MT3. Người học cần giải thích hoặc thực hiện được kết luận: Với $0<\alpha<1$, khởi tạo còn ảnh hưởng và mẫu gần đây có trọng số lớn hơn; với $\alpha=1$, ước lượng bằng mẫu mới nhất.
- **Đầu vào → đầu ra:** Trung bình chính xác L05-B07 → quy tắc trọng số khác → tách hai trục phương pháp ở L05-B09.
- **Dữ kiện/hình thức được truyền:** HT3: $V_n=V_{n-1}+\alpha(g_n-V_{n-1})$; nêu dạng hai trọng số $(1-\alpha)V_{n-1}+\alpha g_n$.
- **Nguồn và quyết định:** SB §2.5 tr.32–33; L05 tr.20–23. Quyết định `sửa`.
- **Bố cục và đối tượng:** Hai cột tính trên cùng hai mẫu $(1,-1)$, đồng nhất khởi tạo và thứ tự.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở nêu lý do dùng bước hằng khi môi trường thay đổi theo thời gian (nguồn tr.21). Lý do: bước hằng trước đây xuất hiện không có động cơ.
- **Sửa sau rà 01-10-2026:** `sửa`; Câu mở nêu môi trường không dừng nằm ngoài giả thiết của bài; $\alpha=0.5$ cho thấy cách đặt trọng số theo thời gian; dẫn bài giảng gốc tr.21 trong ghi chú diễn giả.

#### L05-B09: Hai lựa chọn của Monte Carlo

- **Lý do tồn tại và nhu cầu:** Loại nhầm lẫn quyết định mẫu với quyết định trọng số trước quy trình đầy đủ.
- **Vai trò, mục tiêu và sản phẩm:** Ứng dụng phân loại; MT2–MT3. Người học cần giải thích hoặc thực hiện được kết luận: Quy tắc chọn lần ghé và quy tắc bước học là hai quyết định độc lập.
- **Đầu vào → đầu ra:** L05-B04 và L05-B08 → đặc tả đầu vào của giả mã L05-B10.
- **Dữ kiện/hình thức được truyền:** HT2–HT3; các số từ hai cập nhật $0\to0.5\to0.75$.
- **Nguồn và quyết định:** SB §5.1 tr.92–93, §6.1 tr.119; HW05 bài 5 được sửa. Quyết định `thêm`.
- **Bố cục và đối tượng:** Bảng HTML có chú thích dữ liệu và bước học; không tô màu làm tín hiệu duy nhất.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Viết đầy đủ tên phương pháp trong tiêu đề.

#### L05-B10: Thuật toán dự đoán Monte Carlo

- **Lý do tồn tại và nhu cầu:** Nguồn chưa có giả mã đủ đầu vào, quy tắc chọn mẫu, thứ tự và dừng; bổ sung từ SB để người học thực hiện được thuật toán.
- **Vai trò, mục tiêu và sản phẩm:** Thuật toán đầy đủ; MT2–MT3. Người học cần giải thích hoặc thực hiện được kết luận: Tính lợi tức trước rồi chọn lần ghé theo thời gian giúp triển khai MC đúng quy tắc.
- **Đầu vào → đầu ra:** Hai đầu vào L05-B09 → quy trình có thể lần theo → áp dụng lượt thứ hai L05-B11.
- **Dữ kiện/hình thức được truyền:** HT1–HT3; $V(S_t)\leftarrow V(S_t)+\alpha_{N(S_t)}(S_t)[G_t-V(S_t)]$.
- **Nguồn và quyết định:** SB §5.1 tr.92; §2.4 tr.30–31; bản diễn đạt hai lượt quét tương đương về tập mẫu với MC lần ghé đầu. Quyết định `thêm`.
- **Bố cục và đối tượng:** Giả mã khoảng 10–12 dòng ở cỡ chữ chuẩn; tách phần tính lợi tức và phần cập nhật bằng khoảng trắng.
- **Thời lượng:** 4 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Đổi "quy trình" thành "thuật toán" cho thống nhất với L05-C05.
- **Sửa sau rà 01-10-2026:** `sửa`; Chữ giả mã nâng từ 0.82em lên 0.92em (CSS cục bộ), trang vẫn vừa khung.

#### L05-B11: Monte Carlo trên lượt thứ hai

- **Lý do tồn tại và nhu cầu:** Bài nguồn chưa chỉ rõ lần ghé; nêu hai phiên bản và đáp án nhất quán.
- **Vai trò, mục tiêu và sản phẩm:** Ứng dụng thuật toán; MT3. Người học cần giải thích hoặc thực hiện được kết luận: Số lần cập nhật quyết định kết quả MC khi bước học giữ hằng.
- **Đầu vào → đầu ra:** Giả mã L05-B10 → kết quả kiểm chứng từng quy tắc → phân biệt tính toán đúng với bảo đảm thống kê L05-B12.
- **Dữ kiện/hình thức được truyền:** HT3 dùng cùng $\alpha$ và các $G_t=-1$ đã tính.
- **Nguồn và quyết định:** L05 tr.22, 29; HW05 bài 7; kiểm toán số độc lập. Quyết định `sửa`.
- **Bố cục và đối tượng:** Quỹ đạo $e_2$ và bảng các giá trị trung gian; mỗi cột ghi rõ cách chọn lần ghé.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Viết đầy đủ tên phương pháp.

#### L05-B12: Tính không chệch và hội tụ của Monte Carlo

- **Lý do tồn tại và nhu cầu:** Giữ tính chất có căn cứ và loại phát biểu không chệch bao trùm mọi biến thể MC.
- **Vai trò, mục tiêu và sản phẩm:** Điều kiện và giới hạn; MT3–MT5. Người học cần giải thích hoặc thực hiện được kết luận: Tính chất của lợi tức không tự động là tính chất của mọi cách kết hợp lợi tức.
- **Đầu vào → đầu ra:** L05-B11 chỉ là kết quả hữu hạn mẫu → điều kiện kết luận đúng → câu kiểm tra L05-B13 và nhu cầu cập nhật sớm L05-C01.
- **Dữ kiện/hình thức được truyền:** HT2–HT3; không đưa chứng minh hội tụ MC mọi lần ghé vào tuyến chính.
- **Nguồn và quyết định:** SB §5.1 tr.92–93; §2.5 tr.32–33; L05 tr.23 được giới hạn lại. Quyết định `sửa`.
- **Bố cục và đối tượng:** Ba nhãn đối tượng: lợi tức, trung bình mẫu, bảng dùng bước hằng; mỗi nhãn kèm điều kiện tương ứng.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Điều kiện bổ sung sau rà:** Với quá trình phần thưởng Markov hữu hạn do chính sách Markov dừng, cố định tạo ra, phần thưởng bị chặn, kết thúc hầu chắc chắn từ mọi trạng thái không kết thúc đang xét, các lượt khởi động độc lập theo cùng phân phối và xác suất ghé $s$ dương, trung bình mọi lần ghé với $0\le\gamma\le1$ và bước học $1/N(s)$ hội tụ hầu chắc chắn về $v_\pi(s)$ khi số lượt hoàn chỉnh tăng vô hạn. Kết luận ở ghi chú/học liệu; mặt trang phân biệt phụ thuộc trong lượt, nhất quán và ảnh hưởng khởi tạo có điều kiện. M01/RL-02 và M02/RL-03/ACA-01.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề nêu kết quả thay vì "giả thiết". Ba thẻ: lần ghé đầu tiên; mọi lần ghé; bước học hằng. Chú thích nêu giả thiết của hai kết quả hội tụ.
- **Sửa sau rà 01-10-2026:** `sửa`; Định nghĩa ngắn "ước lượng không chệch: kỳ vọng bằng $v_\pi(s)$"; chú thích giả thiết viết liền: lượt độc lập, cùng phân phối, kết thúc hầu chắc chắn, thưởng bị chặn, $s$ được ghé với xác suất dương; ghi chú diễn giả nêu tính Markov cho thời điểm ghé ngẫu nhiên; thẻ bước hằng viết dạng khẳng định có điều kiện.
- **Rà soát 06-10-2026:** `sửa`; Câu mở thêm "Theo tính Markov", nối với L05-B04. Phần còn lại giữ.

#### L05-B13: Kiểm tra chọn mẫu Monte Carlo

- **Lý do tồn tại và nhu cầu:** Kiểm tra riêng hai trục vừa học bằng số cho đáp án khác nhau.
- **Vai trò, mục tiêu và sản phẩm:** Kiểm tra riêng của mạch B; MT2–MT3. Người học cần giải thích hoặc thực hiện được kết luận: Một kết quả MC chỉ xác định khi cả tập mẫu và bước học đã được chỉ rõ.
- **Đầu vào → đầu ra:** Quy trình và giả thiết L05-B10–L05-B12 → xác nhận đủ năng lực MC → giới hạn chờ kết thúc L05-C01.
- **Dữ kiện/hình thức được truyền:** HT1–HT3.
- **Nguồn và quyết định:** HW05 bài 5, 7; L05 tr.20, 22. Quyết định `thêm`.
- **Bố cục và đối tượng:** Hai dòng quỹ đạo và ô trống cho tập mẫu, số mẫu, kết quả; không hiện đáp án ban đầu.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Kiểm tra và sản phẩm cần nộp:** Với X, lập dãy lợi tức theo lần ghé đầu tiên và mọi lần ghé; tính hai trung bình sau $e_1,e_2$. Nếu dùng lần ghé đầu tiên với $\alpha=0.5$, tính V(X) sau mỗi lượt và giải thích sự khác biệt.
- **Đáp án đối chiếu:** Lần ghé đầu tiên $(1,-1)$ cho 0; mọi lần ghé $(1,1,-1)$ cho $1/3$. Bước hằng cho $0.5$ rồi $-0.25$ vì mẫu cũ và khởi tạo có trọng số khác trung bình số học.
- **Tiêu chí:** Chọn đúng ba mẫu của X theo mọi lần ghé, đếm n riêng cho X, phân biệt trọng số với chọn mẫu.
- **Phân bổ hoạt động:** 1 phút tính, 1 phút đối chiếu cặp kết quả, 1 phút giải thích; nằm trong 3 phút.
- **Rà soát 01-10-2026:** `sửa`; Viết đầy đủ tên phương pháp.

### Mạch C: Dự đoán sai phân thời gian TD(0)

#### L05-C01: Cập nhật khi lượt chưa kết thúc

- **Lý do tồn tại và nhu cầu:** Giữ động lực cập nhật một bước của nguồn bằng chính ví dụ đã học.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề TD; MT4. Người học cần giải thích hoặc thực hiện được kết luận: MC đầy đủ chưa có mục tiêu khi phần đuôi của lượt chưa được quan sát.
- **Đầu vào → đầu ra:** MC cần kết thúc ở L05-B13 → nhu cầu dùng dự đoán còn lại L05-C02.
- **Dữ kiện/hình thức được truyền:** Không đưa quy tắc TD trước trực giác; dùng ý nghĩa lợi tức từ L05-B03.
- **Nguồn và quyết định:** L05 tr.24; SB §6.1 tr.119–120. Quyết định `giữ`.
- **Bố cục và đối tượng:** Quỹ đạo $e_1$ chỉ hiện cạnh đầu, phần tương lai nét đứt có nhãn chưa quan sát.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Chỉnh câu chữ tiêu đề.

#### L05-C02: Mục tiêu một bước

- **Lý do tồn tại và nhu cầu:** Diễn giải đối tượng trước công thức; giữ thuật ngữ khi cần nhưng không dùng từ phỏng đoán thay ước lượng.
- **Vai trò, mục tiêu và sản phẩm:** Trực giác; MT4. Người học cần giải thích hoặc thực hiện được kết luận: Thưởng vừa nhận cộng ước lượng ở trạng thái sau tạo một mục tiêu có sẵn sau một bước.
- **Đầu vào → đầu ra:** Phần đuôi chưa biết L05-C01 → thay bằng ước lượng có sẵn → tính tay L05-C03.
- **Dữ kiện/hình thức được truyền:** Trực giác từ $G_t=R_{t+1}+\gamma G_{t+1}$; chưa gắn sai số tổng quát.
- **Nguồn và quyết định:** SB §6.1 tr.120–121; L05 tr.24–25. Quyết định `sửa`.
- **Bố cục và đối tượng:** `mc-td-targets.svg`; một nhánh quan sát tới $t+1$ rồi hộp V, đối chiếu quỹ đạo đầy đủ MC.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Hiển thị $G_t=R_{t+1}+\gamma G_{t+1}\approx R_{t+1}+\gamma V(S_{t+1})$ và gọi tên bootstrap trên mặt trang (nguồn tr.24). Lý do: phép thay thế cốt lõi trước đây chỉ có trong ghi chú.
- **Sửa sau rà 01-10-2026:** `sửa`; Bỏ dấu ≈; hiển thị $G_t=R_{t+1}+\gamma G_{t+1}$ và $v_\pi(S_{t+1})=\mathbb E_\pi[G_{t+1}\mid S_{t+1}]$; hộp nêu mục tiêu một bước thay mục tiêu $G_t$ của Monte Carlo; hình dùng cỡ ngắn.

#### L05-C03: Một bước cập nhật TD

- **Lý do tồn tại và nhu cầu:** Bổ sung bước tính tay trước ký hiệu TD, không thêm môi trường.
- **Vai trò, mục tiêu và sản phẩm:** Ví dụ tính tay; MT4. Người học cần giải thích hoặc thực hiện được kết luận: TD điều chỉnh ước lượng hiện tại theo khoảng cách đến mục tiêu một bước.
- **Đầu vào → đầu ra:** Cơ chế L05-C02 → một cập nhật kiểm được → công thức tổng quát L05-C04.
- **Dữ kiện/hình thức được truyền:** Bước số chuẩn bị HT4; từng số ánh xạ sang $R_{t+1},\gamma,V_t(S_{t+1}),V_t(S_t),\alpha$.
- **Nguồn và quyết định:** Quy tắc SB §6.1 tr.119–120; phép tính từ trạng thái sau $e_1$ của ví dụ nguồn, chưa yêu cầu người học biết cách tạo bảng ấy. Quyết định `thêm`.
- **Bố cục và đối tượng:** Một cạnh chuyển và ba ô tính mục tiêu, sai số, giá trị mới; số 0.5 ở X ghi rõ là bảng cho trước.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích nêu bảng $V(S)=0$, $V(X)=0.5$ là kết quả TD(0) sau $e_1$, được tính lại khi chạy TD(0) trên lượt thứ nhất.

#### L05-C04: Mục tiêu và sai số TD(0)

- **Lý do tồn tại và nhu cầu:** Tách công thức và giả mã khỏi trang nguồn để mỗi trang có một chức năng.
- **Vai trò, mục tiêu và sản phẩm:** Hình thức; MT4. Người học cần giải thích hoặc thực hiện được kết luận: Sai số TD là mục tiêu một bước trừ giá trị trước cập nhật.
- **Đầu vào → đầu ra:** Ba ô tính L05-C03 → ký hiệu tổng quát → quy trình qua nhiều chuyển L05-C05.
- **Dữ kiện/hình thức được truyền:** HT4: $Y_t=R_{t+1}+\gamma V_t(S_{t+1})$, $\delta_t=Y_t-V_t(S_t)$, $V_{t+1}(S_t)=V_t(S_t)+\alpha_n(S_t)\delta_t$.
- **Nguồn và quyết định:** SB §6.1 tr.119–121; L05 tr.25. Quyết định `tách`.
- **Bố cục và đối tượng:** Công thức lớn và chú thích ngắn dưới từng thành phần; không dùng bảng mô hình chuyển.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Chú thích giải thích tên gọi: $\delta_t$ là hiệu giữa hai dự đoán ở hai thời điểm liên tiếp.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích: $\delta_t$ là hiệu giữa mục tiêu dựa trên dự đoán tại $t+1$ và dự đoán tại $t$.

#### L05-C05: Thuật toán TD(0)

- **Lý do tồn tại và nhu cầu:** Hoàn thiện đầu vào, nguồn dữ liệu, thứ tự và dừng mà nguồn chưa diễn đạt đủ.
- **Vai trò, mục tiêu và sản phẩm:** Thuật toán đầy đủ; MT4. Người học cần giải thích hoặc thực hiện được kết luận: TD(0) cập nhật sau mỗi chuyển do chính sách cố định sinh ra.
- **Đầu vào → đầu ra:** Công thức L05-C04 → trình tự thực thi → trường hợp biên L05-C06 và chạy toàn lượt L05-C07.
- **Dữ kiện/hình thức được truyền:** HT4; đầu ra là bảng V sau ngân sách. Trạng thái kết thúc không có hành động tiếp theo trong lượt.
- **Nguồn và quyết định:** SB §6.1 tr.120, hộp TD(0); L05 tr.25. Quyết định `thêm`.
- **Bố cục và đối tượng:** Giả mã khoảng 10 dòng; nhãn đầu vào và đầu ra đặt ngoài vòng lặp.
- **Thời lượng:** 4 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Chữ giả mã nâng từ 0.82em lên 0.92em (CSS cục bộ), trang vẫn vừa khung.

#### L05-C06: Trạng thái kết thúc và tự chuyển

- **Lý do tồn tại và nhu cầu:** Khôi phục trường hợp trạng thái kết thúc và kiểm việc đọc bảng cũ; ví dụ tự xây dựng được ghi rõ nguồn gốc.
- **Vai trò, mục tiêu và sản phẩm:** Ứng dụng trường hợp biên; MT4. Người học cần giải thích hoặc thực hiện được kết luận: Cùng bảng trước cập nhật và giá trị trạng thái kết thúc bằng 0 xác định mục tiêu ở các trường hợp biên.
- **Đầu vào → đầu ra:** Quy trình L05-C05 → hai lỗi triển khai cần tránh → chạy $e_1$ L05-C07.
- **Dữ kiện/hình thức được truyền:** HT4; ở trạng thái kết thúc $Y_t=R_{t+1}$. Cả hai lần đọc trong tự chuyển dùng $V_t(s)=2$.
- **Nguồn và quyết định:** SB §6.1 tr.120; trạng thái kết thúc từ L05 tr.19; tự chuyển là ví dụ kiểm toán quy tắc do bài soạn tạo, phù hợp tự chuyển HW05 bài 6. Quyết định `thêm`.
- **Bố cục và đối tượng:** Hai cạnh nhỏ: một đến trạng thái kết thúc, một vòng tự chuyển có đầy đủ nhãn.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở nêu hai trường hợp biên và gắn tự chuyển với việc đứng yên trong chuỗi năm ô của HW05 bài 6. Lý do: tự chuyển trước đây xuất hiện khiên cưỡng.
- **Sửa sau rà 01-10-2026:** `sửa`; Mặt trang chỉ nêu tự chuyển xảy ra khi tác tử đứng yên; dẫn chiếu HW05 bài 6 và "số liệu minh họa" chuyển vào ghi chú diễn giả.

#### L05-C07: TD(0) trên lượt thứ nhất

- **Lý do tồn tại và nhu cầu:** Hiển thị các bước thay cho kết luận lan truyền không gắn thứ tự.
- **Vai trò, mục tiêu và sản phẩm:** Ứng dụng đầy đủ; MT4. Người học cần giải thích hoặc thực hiện được kết luận: Trong lượt đầu từ bảng 0, thưởng cuối chỉ trực tiếp cập nhật trạng thái ngay trước trạng thái kết thúc.
- **Đầu vào → đầu ra:** Trường hợp biên L05-C06 → lượt đầy đủ và bảng mới → tiếp tục lượt thứ hai L05-C08.
- **Dữ kiện/hình thức được truyền:** HT4 theo đúng giả mã L05-C05.
- **Nguồn và quyết định:** L05 tr.29; HW05 bài 7; kiểm toán số độc lập. Quyết định `sửa`.
- **Bố cục và đối tượng:** Quỹ đạo $e_1$ và bảng bốn hàng, cột t, trạng thái, thưởng, mục tiêu, V(S), V(X).
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-C08: TD(0) trên lượt thứ hai

- **Lý do tồn tại và nhu cầu:** Làm rõ số trung gian và ranh giới giữa trực tuyến với theo lô.
- **Vai trò, mục tiêu và sản phẩm:** Ứng dụng cập nhật tại chỗ; MT4. Người học cần giải thích hoặc thực hiện được kết luận: Chuyển sau dùng bảng vừa cập nhật bởi chuyển trước trong TD trực tuyến.
- **Đầu vào → đầu ra:** Bảng L05-C07 → phụ thuộc thứ tự của TD trực tuyến → chi phí và thông tin cần giữ L05-C09.
- **Dữ kiện/hình thức được truyền:** HT4; dòng cuối $0.25+0.5(-1-0.25)=-0.375$.
- **Nguồn và quyết định:** L05 tr.29; HW05 bài 7; kiểm toán số độc lập. Quyết định `sửa`.
- **Bố cục và đối tượng:** Bảng ba hàng đồng bộ vị trí với quỹ đạo; mũi tên chỉ giá trị S=0.25 được dùng ở bước thứ hai.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-C09: Chi phí bộ nhớ và tính toán

- **Lý do tồn tại và nhu cầu:** Thay bảng ưu/nhược tuyệt đối của nguồn bằng thông tin và chi phí có phạm vi.
- **Vai trò, mục tiêu và sản phẩm:** Điều kiện thực hiện; MT4–MT5. Người học cần giải thích hoặc thực hiện được kết luận: TD xử lý một chuyển bằng lượng tính toán không phụ thuộc độ dài lượt.
- **Đầu vào → đầu ra:** Lần theo thuật toán L05-C07–L05-C08 → giải thích tài nguyên và thời điểm → kiểm tra L05-C10.
- **Dữ kiện/hình thức được truyền:** Chi phí suy ra từ L05-B10 và L05-C05, không là định lý tốc độ hội tụ.
- **Nguồn và quyết định:** SB §6.1–6.2 tr.119–124; phân tích chi phí trực tiếp từ giả mã. Quyết định `sửa`.
- **Bố cục và đối tượng:** Bảng hai hàng MC/TD, ba cột thời điểm, dữ liệu tạm, chi phí; chú thích đây là quy trình dạng bảng đang học.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề nêu đúng nội dung bảng.

#### L05-C10: Kiểm tra một bước TD(0)

- **Lý do tồn tại và nhu cầu:** Kiểm tra riêng mục tiêu, dấu sai số và trạng thái kết thúc trước phân tích so sánh.
- **Vai trò, mục tiêu và sản phẩm:** Kiểm tra riêng của mạch C; MT4. Người học cần giải thích hoặc thực hiện được kết luận: Mục tiêu, sai số và bảng mới phải được tính từ cùng bảng trước cập nhật.
- **Đầu vào → đầu ra:** Quy trình và trường hợp biên L05-C05–L05-C09 → kiểm đủ thao tác → so sánh hai thuật toán L05-D01.
- **Dữ kiện/hình thức được truyền:** HT4.
- **Nguồn và quyết định:** HW05 bài 3, 7; các số được chọn để kiểm trực tiếp quy tắc SB §6.1. Quyết định `thêm`.
- **Bố cục và đối tượng:** Hai cạnh có nhãn và ô trống cho mục tiêu, sai số, giá trị mới.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Kiểm tra và sản phẩm cần nộp:** Cho $V(S)=0.25,V(X)=0.5,\alpha=0.5,\gamma=1$. (a) Với $S\to X$, thưởng 0, tính Y, sai số và V(S) mới. (b) Xét riêng bước $S\to L$, thưởng −1, từ cùng bảng ban đầu; tính ba đại lượng đó.
- **Đáp án đối chiếu:** (a) Y=0.5, sai số 0.25, V(S)=0.375; (b) Y=−1, sai số −1.25, V(S)=−0.375. Cả hai trường hợp V(X) giữ 0.5, V(L)=0.
- **Tiêu chí:** Hai trường hợp bắt đầu độc lập từ cùng bảng; không coi thưởng −1 khi vào trạng thái kết thúc là giá trị tiếp nối để cộng lần nữa; đúng dấu và chỉ sửa S.
- **Phân bổ hoạt động:** 1 phút tính, 1 phút trình bày, 1 phút đối chiếu; nằm trong 3 phút.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

### Mạch D: So sánh theo dữ liệu và giả thiết

#### L05-D01: Monte Carlo và TD(0) trên cùng dữ liệu

- **Lý do tồn tại và nhu cầu:** Giữ so sánh nguồn nhưng gắn đủ điều kiện và loại kết luận vượt dữ liệu.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề so sánh và ví dụ; MT5. Người học cần giải thích hoặc thực hiện được kết luận: MC và TD(0) tạo các bảng khác nhau vì dùng mục tiêu và thời điểm cập nhật khác nhau.
- **Đầu vào → đầu ra:** Hai thuật toán đã chạy → cần chuẩn giá trị và tiêu chí để đánh giá → L05-D02.
- **Dữ kiện/hình thức được truyền:** HT3–HT4, không thêm phép cập nhật.
- **Nguồn và quyết định:** L05 tr.29; HW05 bài 7; số đã kiểm ở L05-B11, L05-C07–L05-C08. Quyết định `sửa`.
- **Bố cục và đối tượng:** Bảng HTML hai phương pháp, hai mốc; dùng lại sơ đồ mục tiêu nếu còn khoảng trống.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Thêm hộp nêu nhu cầu giá trị chuẩn để đánh giá hai bảng.
- **Sửa sau rà 01-10-2026:** `sửa`; Hộp: "Để xác định bảng nào gần $v_\pi$ hơn, cần giá trị chuẩn của môi trường."

#### L05-D02: Giá trị chuẩn của chuỗi ngắn

- **Lý do tồn tại và nhu cầu:** Đặt giá trị chuẩn sau khi đã có ước lượng, giúp phân biệt đối tượng đánh giá với dữ liệu học.
- **Vai trò, mục tiêu và sản phẩm:** Ứng dụng đối chiếu giá trị; MT5. Người học cần giải thích hoặc thực hiện được kết luận: Giá trị thật là kỳ vọng của môi trường; hai lượt dữ liệu chưa xác định chính xác giá trị đó.
- **Đầu vào → đầu ra:** Bảng dự đoán L05-D01 → chuẩn so sánh có mô hình → chuỗi dài giữ cùng cơ chế nhưng thay khoảng cách và chiết khấu L05-D03.
- **Dữ kiện/hình thức được truyền:** Hai phương trình Bellman kỳ vọng từ tiên quyết; không đưa toán tử Bellman hoặc phép co mới.
- **Nguồn và quyết định:** L05 tr.19; kiểm toán số độc lập; Bellman kỳ vọng đã học ở Bài 04. Quyết định `giữ`.
- **Bố cục và đối tượng:** `short-walk.svg` với hàng giá trị thật tại S,X; giá trị ở trạng thái kết thúc tiếp tục ghi 0.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở: mô hình chuỗi ngắn đã biết trong ví dụ, nên $v_\pi$ được tính từ Bellman kỳ vọng.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích nối ra: độ lệch của hai bảng được phân tích qua kỳ vọng (độ chệch) và biến thiên (phương sai) của mục tiêu; hình giới hạn 150px.

#### L05-D03: Chuỗi dài với thưởng thưa

- **Lý do tồn tại và nhu cầu:** Giữ ví dụ dài riêng của nguồn và dùng nó cho vấn đề số mũ, độ dài đường đi.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề và ví dụ dẫn nhập so sánh; MT2–MT5. Người học cần giải thích hoặc thực hiện được kết luận: Khoảng cách đến phần thưởng và chiết khấu làm các lợi tức khác nhau theo đường đi.
- **Đầu vào → đầu ra:** Chuỗi ngắn L05-D02 → độ dài và chiết khấu khác → tính hai lợi tức L05-D04.
- **Dữ kiện/hình thức được truyền:** HT1 với $\gamma=0.99$; các giá trị chuẩn đã được giải độc lập, không trình bày hệ năm phương trình trên mặt trang.
- **Nguồn và quyết định:** L05 tr.30; kiểm toán số độc lập. Quyết định `giữ`.
- **Bố cục và đối tượng:** `long-walk.svg`; giữ đúng vị trí bắt đầu và nhãn thưởng cạnh, giá trị ở trạng thái kết thúc bằng 0.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Chú thích nêu lý do xét chuỗi dài: lợi tức phụ thuộc nhiều chuyển ngẫu nhiên hơn; thưởng chỉ khi vào $L$ hoặc $G$ (nguồn tr.30).
- **Sửa sau rà 01-10-2026:** `sửa`; Câu lý do chuỗi dài lên làm câu mở; hai thẻ gộp mỗi thẻ một dòng; hình dùng cỡ ngắn.

#### L05-D04: Biến thiên của lợi tức

- **Lý do tồn tại và nhu cầu:** Sửa lỗi lệch chỉ số chiết khấu và giới hạn kết luận theo đúng dữ liệu.
- **Vai trò, mục tiêu và sản phẩm:** Ví dụ tính tay và trực giác biến thiên; MT2–MT5. Người học tính được số mũ $\gamma^{m-1}$ và phân biệt hai lợi tức mẫu từ $S$ với giá trị kỳ vọng tại chính $S$.
- **Đầu vào → đầu ra:** Giá trị chuẩn L05-D03 → hai lợi tức mẫu tại cùng trạng thái khác kỳ vọng → nhu cầu lấy kỳ vọng mục tiêu tại L05-D05, rồi xét nguồn biến thiên L05-D06.
- **Dữ kiện/hình thức được truyền:** HT1; sửa số mũ 4 và 2 ở nguồn thành 3 và 1.
- **Nguồn và quyết định:** L05 tr.31; kiểm toán số độc lập. Quyết định `sửa`.
- **Bố cục và đối tượng:** `long-returns.svg`; công thức KaTeX đặt cạnh mỗi quỹ đạo với chỉ số thưởng cuối.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề nêu luận điểm thay cho chi tiết số mũ; giữ hiệu chỉnh số mũ trong ghi chú.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích nêu thứ tự xét: kỳ vọng (độ chệch) rồi phương sai.

#### L05-D05: Độ chệch của mục tiêu TD

- **Lý do tồn tại và nhu cầu:** Thay so sánh nhị phân của nguồn bằng điều kiện và đại lượng chính xác.
- **Vai trò, mục tiêu và sản phẩm:** Ví dụ rồi hình thức so sánh sai lệch; MT5. Người học tính kỳ vọng qua các chuyển kế tiếp khi bảng cố định, sau đó giải thích sai lệch qua sai số giá trị tiếp nối.
- **Đầu vào → đầu ra:** Nhu cầu tách mẫu/kỳ vọng ở L05-D04 → phép kỳ vọng số trong chuỗi ngắn từ dữ kiện đã biết → đẳng thức sai lệch, rồi phân biệt với phương sai tại L05-D06.
- **Dữ kiện/hình thức được truyền:** HT5: $\mathbb E[Y\mid S_t=s]-v_\pi(s)=\gamma\mathbb E[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s]$.
- **Nguồn và quyết định:** SB §6.1–6.2 tr.120–124; L05 tr.26–27 được sửa; hệ quả từ Bellman kỳ vọng. Quyết định `sửa`.
- **Bố cục và đối tượng:** Dữ kiện và hai mục tiêu, phép tính kỳ vọng số, rồi công thức sai lệch tổng quát; phép trừ dài ở ghi chú. Giữ cỡ chữ và ngân sách 3 phút.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Gọi tên độ chệch của mục tiêu (kỳ vọng mục tiêu trừ $v_\pi(s)$) ngay sau ví dụ số, giữ thứ tự ví dụ trước hình thức; chú thích nêu độ chệch của MC bằng 0 và điều kiện để độ chệch TD bằng 0. Số liệu giữ nguyên: $0.2(-1)+0.8(0.5)=0.2$, $1/5-11/21=-34/105$.

#### L05-D06: Phương sai của mục tiêu

- **Lý do tồn tại và nhu cầu:** Gộp hai trang nguồn lặp về phương sai và bỏ mức độ không định lượng.
- **Vai trò, mục tiêu và sản phẩm:** Trực giác và giới hạn phương sai; MT5. Người học cần giải thích hoặc thực hiện được kết luận: MC dùng phần đuôi quỹ đạo ngẫu nhiên; TD thay phần đuôi bằng một giá trị ước lượng.
- **Đầu vào → đầu ra:** Sai lệch L05-D05 → phương sai là trục khác → cần điều kiện để nói về học lâu dài L05-D07.
- **Dữ kiện/hình thức được truyền:** HT6; bất đẳng thức lý tưởng đặt trong ghi chú hoặc một dòng riêng có nhãn điều kiện.
- **Nguồn và quyết định:** SB §6.2 tr.124; L05 tr.26–28; suy luận điều kiện từ luật phương sai toàn phần. Quyết định `gộp`.
- **Bố cục và đối tượng:** Cây nhỏ một bước rồi hai phần đuôi; MC giữ một đuôi quan sát, mục tiêu lý tưởng thay bằng kỳ vọng. Hình là quan hệ, không có số thực nghiệm.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Ngân sách theo SV-R2:** 3 phút cho nguồn ngẫu nhiên, cơ chế kỳ vọng phần đuôi và giới hạn của $V$ bất kỳ. Chứng minh dùng $\mathcal F_1$ và luật phương sai toàn phần thuộc phần đọc phụ trợ; chưa có dữ liệu diễn tập.
- **Rà soát 01-10-2026:** `sửa`; Mặt trang nêu bất đẳng thức $\operatorname{Var}(R_{t+1}+\gamma v_\pi(S_{t+1})\mid s)\le\operatorname{Var}(G_t\mid s)$ và giới hạn với bảng $V$ đang học; hai thẻ nguồn ngẫu nhiên gộp thành một câu; hình giảm còn 200px. Lý do: kết quả dương trước đây chỉ có trong ghi chú.
- **Sửa sau rà 01-10-2026:** `sửa`; Mặt trang thêm giả thiết Markov và mômen bậc hai hữu hạn; tách nguồn ngẫu nhiên (thưởng đầu, trạng thái sau) khỏi sai số tất định của $V$; hộp viết dạng khẳng định có điều kiện; hình giới hạn 170px.

#### L05-D07: Điều kiện hội tụ của TD(0)

- **Lý do tồn tại và nhu cầu:** Bổ sung điều kiện còn thiếu; phân biệt bảo đảm với tiêu chuẩn dừng thực hành.
- **Vai trò, mục tiêu và sản phẩm:** Điều kiện áp dụng và hội tụ; MT5–MT6. Người học cần giải thích hoặc thực hiện được kết luận: Bảo đảm hội tụ phụ thuộc dữ liệu và bước học, không chỉ tên thuật toán.
- **Đầu vào → đầu ra:** Cơ chế sai số L05-D05–L05-D06 → ranh giới bảo đảm trên mẫu mới → bài toán khác là dùng lại dữ liệu cố định L05-D08.
- **Dữ kiện/hình thức được truyền:** HT7: $\sum_n\alpha_n(s)=\infty$, $\sum_n\alpha_n(s)^2<\infty$; $1/n$ là ví dụ, $\alpha$ hằng vi phạm điều kiện tổng bình phương.
- **Nguồn và quyết định:** SB §2.5 tr.33; §6.2 tr.124–125; L05 tr.28 được giới hạn. Quyết định `sửa`.
- **Bố cục và đối tượng:** Hai nhóm điều kiện: bài toán/dữ liệu và bước học; không dựng đồ thị hội tụ minh họa giả.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề gọi tên kết quả; hộp nêu "với xác suất 1".

#### L05-D08: Dự đoán trên dữ liệu cố định

- **Lý do tồn tại và nhu cầu:** Bổ sung ví dụ tối giản tạo hai nghiệm khác nhau theo sườn SB §6.3.
- **Vai trò, mục tiêu và sản phẩm:** Vấn đề và ví dụ dẫn nhập theo lô; MT5. Người học cần giải thích hoặc thực hiện được kết luận: Kinh nghiệm trực tiếp của A và thông tin về trạng thái kế tiếp B có thể gợi hai giá trị khác nhau.
- **Đầu vào → đầu ra:** Giới hạn mẫu mới L05-D07 → câu hỏi trên dữ liệu cố định → cách dùng lại dữ liệu L05-D09.
- **Dữ kiện/hình thức được truyền:** Chưa đưa nghiệm; xác định hai trạng thái không kết thúc và tập dữ liệu $\mathcal D$.
- **Nguồn và quyết định:** SB §6.3, Ví dụ 6.4 tr.127–128; đối chiếu UCL tr.22–23, ST tr.48. Quyết định `thêm`.
- **Bố cục và đối tượng:** Bảng ba nhóm lượt có số lượng 1,6,1 và tổng số 8; trạng thái kết thúc được thể hiện rõ.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Câu mở nối từ mẫu mới sang dùng lại dữ liệu (Sutton–Barto §6.3); nhiệm vụ dự đoán $A$ chuyển lên dòng dữ kiện; hai thẻ rút gọn.

#### L05-D09: Cập nhật theo lô

- **Lý do tồn tại và nhu cầu:** Chuẩn bị thuật toán theo lô trước khi so sánh nghiệm, tránh gọi một lần chạy trực tuyến là theo lô.
- **Vai trò, mục tiêu và sản phẩm:** Tính tay rồi quy trình theo lô; MT5. Người học cần giải thích hoặc thực hiện được kết luận: Trong một lượt quét theo lô, mọi sai số được tính từ cùng bảng trước lượt quét.
- **Đầu vào → đầu ra:** Tập dữ liệu L05-D08 → quy trình tái sử dụng → nghiệm MC L05-D10 và TD L05-D11.
- **Dữ kiện/hình thức được truyền:** HT8. $k$: lượt quét; $\Delta_k(s)$: tổng gia số; $y$: mục tiêu. Hiển thị $\Delta_k(s)\leftarrow\Delta_k(s)+\alpha[y-V_k(s)]$ và $V_{k+1}(s)=V_k(s)+\Delta_k(s)$; bảng $V_k$ cố định tới hết lượt quét.
- **Nguồn và quyết định:** SB §6.3 tr.126–128; phép quét số từ dữ liệu Ví dụ 6.4. Quyết định `thêm`.
- **Bố cục và đối tượng:** Một phép tính đầu tiên cạnh quy trình năm bước; ký hiệu được khai báo trên mặt trang, gồm phép cộng và phép ghi. Không thêm một lượt quét thứ hai hoặc giảm cỡ chữ.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Khai báo $k$, $\Delta_k(s)$ đặt đầu thẻ ví dụ trước khi dùng $\Delta_0$; $\varepsilon$, $K$ khai báo ngay ở bước 1; tiêu đề thẻ "Quét đầu, MC và TD".

#### L05-D10: Nghiệm Monte Carlo theo lô

- **Lý do tồn tại và nhu cầu:** Tính đầy đủ tiêu chuẩn MC trước khi đưa nghiệm TD khác, không chỉ hiện hai con số.
- **Vai trò, mục tiêu và sản phẩm:** Hình thức và ứng dụng theo lô MC; MT5. Người học cần giải thích hoặc thực hiện được kết luận: MC khớp các lợi tức đã quan sát tại mỗi trạng thái.
- **Đầu vào → đầu ra:** Quy trình L05-D09 → nghiệm gắn lợi tức thực tế → xét quan hệ Markov thực nghiệm L05-D11.
- **Dữ kiện/hình thức được truyền:** HT2 và HT8; tại A tối thiểu hóa $v^2$, tại B tối thiểu hóa $6(1-v)^2+2v^2$.
- **Nguồn và quyết định:** SB §6.3 tr.127–128, Ví dụ 6.4. Quyết định `thêm`.
- **Bố cục và đối tượng:** Hai nhóm mẫu A và B nối tới nghiệm; mục tiêu bình phương ở một dòng riêng.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề thống nhất với L05-D09.

#### L05-D11: Nghiệm TD theo lô

- **Lý do tồn tại và nhu cầu:** Làm rõ nguồn khác biệt của hai nghiệm và phân biệt bảng sau quét với nghiệm giới hạn.
- **Vai trò, mục tiêu và sản phẩm:** Hình thức và ứng dụng theo lô TD; MT5. Người học cần giải thích hoặc thực hiện được kết luận: TD khớp quan hệ chuyển trạng thái ước lượng từ dữ liệu.
- **Đầu vào → đầu ra:** Nghiệm theo lợi tức L05-D10 → nghiệm theo quan hệ Markov → kiểm tra tiêu chuẩn và giới hạn L05-D12.
- **Dữ kiện/hình thức được truyền:** HT8: $0=V(B)-V(A)$, $0=6-8V(B)$.
- **Nguồn và quyết định:** SB §6.3 tr.127–128, Ví dụ 6.4; kiểm toán số độc lập. Quyết định `thêm`.
- **Bố cục và đối tượng:** `ab-empirical.svg` ghi rõ mô hình ước lượng từ tám lượt, cạnh thưởng và giá trị ở trạng thái kết thúc bằng 0.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Tiêu đề thống nhất với L05-D09.

#### L05-D12: Kiểm tra kết luận từ dữ liệu hữu hạn

- **Lý do tồn tại và nhu cầu:** Kiểm tra tổng hợp phần so sánh, không yêu cầu nhớ bảng ưu nhược chung chung.
- **Vai trò, mục tiêu và sản phẩm:** Kiểm tra riêng của mạch D; MT5–MT6. Người học cần giải thích hoặc thực hiện được kết luận: Một kết luận so sánh phải nêu tiêu chuẩn và phạm vi dữ liệu.
- **Đầu vào → đầu ra:** L05-D10–L05-D11 → khả năng giải thích hai nghiệm có điều kiện → lựa chọn phương pháp L05-E01.
- **Dữ kiện/hình thức được truyền:** HT5–HT8; không đưa công thức ngoài tuyến đã học.
- **Nguồn và quyết định:** SB §6.2–6.3 tr.124–128; HW05 bài 4, 5 được sửa. Quyết định `thêm`.
- **Bố cục và đối tượng:** Bảng dữ liệu rút gọn và hai ô tiêu chuẩn; đáp án chỉ trong ghi chú.
- **Thời lượng:** 4 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Kiểm tra và sản phẩm cần nộp:** Giải thích MC theo lô cho A=0 còn TD theo lô cho A=0.75. Nhận định “TD luôn chính xác hơn vì phương sai luôn thấp hơn” và “bước học hằng luôn hội tụ đúng khi lấy thêm mẫu” có được bài học bảo đảm không? Nêu căn cứ.
- **Đáp án đối chiếu:** MC khớp lợi tức duy nhất 0 của A; TD khớp A→B và trung bình B=0.75. Hai mệnh đề đều không được bảo đảm: phương sai của TD dùng V học được không có thứ tự phổ quát; bước hằng trên mẫu mới không thỏa điều kiện tổng bình phương và có thể dao động.
- **Tiêu chí:** Nêu đúng hai tiêu chuẩn, phân biệt dữ liệu cố định/mẫu mới, không dùng kết quả A–B làm chứng minh TD đúng hơn môi trường thật.
- **Phân bổ hoạt động:** 1.5 phút lập luận, 1 phút trả lời, 1.5 phút đối chiếu; nằm trong 4 phút.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

### Mạch E: Kết luận và tự kiểm tra

#### L05-E01: Lựa chọn phương pháp dự đoán

- **Lý do tồn tại và nhu cầu:** Kết luận quay lại quyết định đã nêu thay vì chỉ lặp mục lục nguồn.
- **Vai trò, mục tiêu và sản phẩm:** Thu hồi vấn đề mở đầu; MT6. Người học cần giải thích hoặc thực hiện được kết luận: Thông tin sẵn có và yêu cầu cập nhật quyết định lựa chọn MC hoặc TD(0).
- **Đầu vào → đầu ra:** Kết luận có điều kiện L05-D12 → trả lời bài toán thiếu mô hình L05-A03 → đối chiếu năng lực L05-E02.
- **Dữ kiện/hình thức được truyền:** Thu hồi HT1–HT8, chỉ cần hai mục tiêu $G_t$ và $R_{t+1}+\gamma V_t(S_{t+1})$.
- **Nguồn và quyết định:** Tổng hợp SB §5.1, §6.1–6.3; L05 tr.28, 33. Quyết định `sửa`.
- **Bố cục và đối tượng:** Bảng ba trường hợp, thông tin, lựa chọn và điều kiện; không thêm khái niệm mới.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-E02: Tổng kết Monte Carlo và TD(0)

- **Lý do tồn tại và nhu cầu:** Gộp câu hỏi mở rộng và tổng kết thành đối chiếu mục tiêu có giới hạn, tránh thêm trọng tâm cuối bài.
- **Vai trò, mục tiêu và sản phẩm:** Đối chiếu mục tiêu; MT1–MT6. Người học cần giải thích hoặc thực hiện được kết luận: Người học có thể thực hiện dự đoán dạng bảng và kiểm tra điều kiện của kết luận.
- **Đầu vào → đầu ra:** Lựa chọn L05-E01 → sản phẩm học tập có thể kiểm chứng → bài tập củng cố L05-E03.
- **Dữ kiện/hình thức được truyền:** Không áp dụng công thức mới; liên hệ chính xác các điều kiện L05-B12, L05-D07.
- **Nguồn và quyết định:** L05 tr.32–33; SB §5.1 và §6.1–6.3. Quyết định `gộp`.
- **Bố cục và đối tượng:** Ba hàng năng lực đi cùng bằng chứng đã thực hiện; không hiện mã trang hoặc mã mục tiêu trên mặt trang.
- **Thời lượng:** 2 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Thay bảng năng lực bằng bảng tổng kết sáu tiêu chí (mục tiêu, thời điểm cập nhật, độ chệch, phương sai, hội tụ trên mẫu mới, dữ liệu cố định), mỗi ô giữ điều kiện đã học; chú thích nối Bài 06. Khôi phục bảng so sánh nguồn tr.31 và tổng kết tr.33 ở dạng có điều kiện; câu nối theo câu hỏi mở tr.32.
- **Sửa sau rà 01-10-2026:** `sửa`; Dòng hội tụ nêu kết quả "về $v_\pi$ khi …"; phương sai MC "có thể lớn khi lượt dài"; chú thích thêm giả thiết của dòng hội tụ; bỏ câu bình luận nguồn khỏi ghi chú diễn giả (lưu trong review-log).
- **Thứ tự E01→E02:** `giữ`; E01 trả lời trực tiếp bài toán mở đầu bằng lựa chọn phương pháp; E02 tổng kết tính chất hai phương pháp và nối sang Bài 06, nên khép phần kết luận trước bài tập. Đề xuất đổi thứ tự bị từ chối sau rà soát 01-10-2026; người rà mạch lập luận xác nhận lý do hợp lệ.

#### L05-E03: Bài tập tuần 5

- **Lý do tồn tại và nhu cầu:** Giữ đủ bài tập nguồn với các hiệu chỉnh học thuật; phân biệt 120 phút chính và 30 phút chữa bài trong tệp quy trình.
- **Vai trò, mục tiêu và sản phẩm:** Bài tập có nguồn; MT1–MT6. Người học cần giải thích hoặc thực hiện được kết luận: Bảy bài tập nguồn kiểm tra từ dữ liệu, cơ chế đến phép tính và giới hạn kết luận.
- **Đầu vào → đầu ra:** Năng lực L05-E02 → nhiệm vụ tự luyện và chữa bài → kiểm tra lựa chọn tổng hợp L05-E04.
- **Dữ kiện/hình thức được truyền:** Bài 6 dùng Bellman kỳ vọng đã là tiên quyết; bài 7 dùng HT3–HT4. Toàn đề và đáp án có hướng dẫn trong phần chữa bài của outline.
- **Nguồn và quyết định:** HW05 tr.1–2, bài 1–7; sửa giả thiết theo nhật ký. Quyết định `sửa`.
- **Bố cục và đối tượng:** Ba nhóm bài tập bằng HTML, mỗi nhóm một sản phẩm cụ thể; không nhồi toàn đề bảy bài lên một trang.
- **Thời lượng:** 3 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Rút gọn tiêu đề.

#### L05-E04: Kiểm tra lựa chọn và điều kiện

- **Lý do tồn tại và nhu cầu:** Kiểm tra riêng phần kết luận bằng quyết định phối hợp các khái niệm thay cho câu hỏi nhớ tên.
- **Vai trò, mục tiêu và sản phẩm:** Kiểm tra riêng của mạch E; MT1–MT6. Người học cần giải thích hoặc thực hiện được kết luận: Lựa chọn phương pháp phải đi cùng mục tiêu, dữ liệu và giới hạn kết luận.
- **Đầu vào → đầu ra:** Bài tập L05-E03 → kiểm chứng toàn tuyến từ vấn đề L05-A03 → tài liệu đọc L05-E05 phục vụ phần còn cần củng cố.
- **Dữ kiện/hình thức được truyền:** HT1–HT8 đã học; đây là tổng hợp, không giới thiệu thuật toán khác.
- **Nguồn và quyết định:** Tổng hợp L05 tr.15–33, HW05 và SB §5.1, §6.1–6.3. Quyết định `thêm`.
- **Bố cục và đối tượng:** Ba thẻ ngắn đánh số tình huống; không thêm môi trường hoặc số mới.
- **Thời lượng:** 4 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Kiểm tra và sản phẩm cần nộp:** (a) Sau lượt $e_1$ hoàn chỉnh, chỉ rõ hai lựa chọn cần xác định trước khi báo cáo một kết quả MC. (b) Sau chuyển đầu chưa kết thúc, nêu một cách cập nhật đã học và thông tin cần có. (c) Trên tám lượt A–B, nêu điều kiện để gọi một nghiệm là tốt hơn nghiệm kia.
- **Đáp án đối chiếu:** (a) Quy tắc lần ghé và quy tắc bước học/khởi tạo. (b) TD(0), cần thưởng, trạng thái sau, bảng V, gamma và bước học; mục tiêu $R+\gamma V(S')$. (c) Cần tiêu chuẩn đánh giá: khớp lợi tức quan sát hay khớp cấu trúc Markov thực nghiệm; để so sánh với môi trường thật cần dữ liệu hoặc giá trị chuẩn phù hợp, tám lượt chưa chứng minh ưu thế phổ quát.
- **Tiêu chí:** Liên kết lựa chọn với dữ kiện; nêu mục tiêu đúng; không đổi chính sách hay giả định biết mô hình ngầm; phân biệt sai số dữ liệu với sai số giá trị thật.
- **Phân bổ hoạt động:** 1.5 phút chọn và ghi điều kiện, 1 phút trả lời, 1.5 phút đối chiếu; nằm trong 4 phút.
- **Rà soát 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-E05: Tài liệu đọc

- **Lý do tồn tại và nhu cầu:** Cung cấp đường đọc có vị trí cụ thể và nhiệm vụ tiếp tục, không lặp tổng kết một lần nữa.
- **Vai trò, mục tiêu và sản phẩm:** Kết thúc bằng nhiệm vụ cụ thể; MT2–MT6. Người học cần giải thích hoặc thực hiện được kết luận: Các mục đọc tương ứng trực tiếp với ba năng lực còn cần tự kiểm.
- **Đầu vào → đầu ra:** Kết quả tự kiểm L05-E04 → chọn phần đọc và bài tập cần hoàn thiện sau bài học.
- **Dữ kiện/hình thức được truyền:** Không có khái niệm mới.
- **Nguồn và quyết định:** SB các mục đã kiểm; HW05 bài 6–7. Quyết định `thêm`.
- **Bố cục và đối tượng:** Không cần hình; danh mục ba mục sách và một tài liệu bài tập, cỡ chữ đọc được.
- **Thời lượng:** 1 phút; các nội dung giải thích và ghi chú chi tiết theo mục tương ứng trong outline.
- **Rà soát 01-10-2026:** `sửa`; Rút gọn tiêu đề.

## Quyết định cấu trúc và sai khác so với nguồn

Giảm phần ôn L05 tr.1–14 xuống tiên quyết cần dùng trong L05-A03–L05-A04; lược điều khiển, phép co và mục lục lặp. Đây là thay đổi theo yêu cầu lấy Sutton–Barto làm sườn, không là thiếu trang chưa chuyển. Giữ trật tự MC trước TD, rồi so sánh và kết luận. Mọi trang trong 33 trang nguồn có quyết định và đích ở bảng outline.

Giữ môi trường ngắn/dài của L05, đổi ô dấu chấm thành X có ánh xạ; giữ thưởng trên cạnh vào trạng thái kết thúc và giá trị ở trạng thái kết thúc bằng 0. Sửa giả thiết bước học của tr.20, số mũ tr.31 và tiền đề HW05 bài 4–5; bài 7 chỉ định hai quy tắc lần ghé. Các số ở nguồn tr.19/30 đúng, không sửa thành số khác. Thêm A–B từ SB để phân biệt hai tiêu chuẩn mà hai chuỗi nguồn chưa thể hiện rõ.

Không thêm Blackjack, Driving Home hoặc chuỗi năm trạng thái A–E của SB: chuỗi nguồn đã phục vụ dẫn nhập, tính tay và đối chiếu. Không vẽ đường học thực nghiệm hoặc bề mặt giá trị thiếu dữ liệu gốc. Không dùng raster hoặc hình sinh; không cần xin ngoại lệ tài sản.

Quill được áp dụng cho thứ tự và tính liên tục: mọi đối tượng có khai báo trước khi dùng; các số của L05-C03 được cho như dữ kiện rồi kiểm lại ở L05-C07; KN5 nhận đủ mục tiêu MC/TD và quy ước dừng trước khi xuất hiện theo lô. Bảng thuật ngữ dùng nhất quán “sai phân thời gian”, “lần ghé đầu tiên/mọi lần ghé”, “bước học”. Không tạo cấu trúc dự án sách hoặc quill.json.

Tổng phút theo từng trang được tính từ cùng dữ liệu lập outline. Mỗi mạch có đúng một trang kiểm tra riêng được chỉ định; các ví dụ tính khác không được dùng thay kiểm tra đó. Bản đã qua kiểm định storyboard trước triển khai, năm vai độc lập sau triển khai và các lượt rà lại toán học, toàn tuyến mạch viết, góc nhìn sinh viên sau sửa. Nếu đổi số lượng/thứ tự, phải cập nhật outline và rà trang thay đổi cùng hai trang lân cận mỗi phía; đổi mở/kết bài hoặc vấn đề trung tâm cần rà lại toàn tuyến.
