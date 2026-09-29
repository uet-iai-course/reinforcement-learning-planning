# Phân tích xây dựng lại Bài 05: Dự đoán phi mô hình

Ngày 28-09-2026. Bản phân tích được lập mới từ kế hoạch, báo cáo phân tích nguồn, đối chiếu đại học và kiểm toán số đã được điều phối viên chấp nhận. Không sử dụng dàn bài, storyboard, HTML hoặc ghi chú biên soạn của lần dựng trước. Nội dung dưới đây là cơ sở cho [outline.md](outline.md) và [storyboard.md](storyboard.md). HTML, SVG và học liệu đã được triển khai; đủ năm báo cáo độc lập của bản cố định đã được điều phối chấp nhận. Hồ sơ đã đồng bộ sau chỉnh sửa; các lượt rà lại toán học, khả năng đọc và toàn tuyến nội dung cùng kiểm định kỹ thuật cuối đều đạt.

## 1. Bài toán giảng dạy

Chủ đề thuộc học phần Học tăng cường, học kỳ 1 năm học 2026–2027. Người học là sinh viên đại học đã học học máy, học sâu, thuật toán và các bài trước về quá trình quyết định Markov, chính sách, hàm giá trị và đánh giá chính sách bằng quy hoạch động. Kiến thức xác suất cần dùng gồm kỳ vọng có điều kiện, trung bình mẫu và phương sai. Luật phương sai toàn phần chỉ dùng trong ghi chú chứng minh ngắn, không là điều kiện để hoàn thành các bài tính tay.

**Vấn đề trung tâm:** ước lượng giá trị trạng thái của một chính sách cố định từ các lượt tương tác khi không biết mô hình chuyển trạng thái và phần thưởng kỳ vọng. Đầu vào chuyển từ mô hình sang mẫu; đối tượng cần dự đoán vẫn là $v_\pi$.

| Mục tiêu | Năng lực quan sát được | Bằng chứng đánh giá |
|---|---|---|
| MT1 | Xác định chính sách được đánh giá, đại lượng cần ước lượng và dữ liệu quan sát ở mỗi bước | Phân biệt dự đoán với điều khiển và mẫu với mô hình |
| MT2 | Tính tổng phần thưởng chiết khấu; chọn đúng lần ghé đầu tiên hoặc mọi lần ghé | Lập tập mẫu cho cùng hai lượt có trạng thái lặp |
| MT3 | Thực hiện Monte Carlo với trung bình mẫu hoặc bước học hằng; giải thích sự khác biệt | Tính bảng giá trị sau hai lượt và kiểm tra thứ tự giả mã |
| MT4 | Tính mục tiêu, sai số và một lượt cập nhật sai phân thời gian TD(0) | Lần theo các bước, xử lý trạng thái kết thúc và tự chuyển |
| MT5 | So sánh MC và TD(0) theo dữ liệu, thời điểm cập nhật, sai lệch, phương sai và điều kiện hội tụ | Nêu kết luận có điều kiện; giải thích hai nghiệm trên tám lượt A–B |
| MT6 | Chọn phương pháp và cách đánh giá phù hợp với thông tin sẵn có | Chọn từ dữ liệu hoàn chỉnh, dữ liệu chưa kết thúc và dữ liệu cố định |

Phạm vi chính gồm Monte Carlo (MC) dự đoán, hai quy tắc chọn lần ghé, trung bình gia tăng, bước học, TD(0) dạng bảng và so sánh trên cùng dữ liệu. Không đưa điều khiển, khác chính sách, xấp xỉ hàm, TD nhiều bước hoặc TD($\lambda$) vào bài. Dự toán 45 trang, năm mạch, 120 phút gồm kiểm tra; 30 phút còn lại chữa bài tập nguồn. Nguồn không có mã, vì vậy không tạo chương trình hoặc notebook.

Chính sách $\pi$ là Markov, cố định theo thời gian; môi trường Markov dừng. Dữ liệu học được sinh theo $\pi$. Không yêu cầu người học biết mô hình để chạy MC/TD; các xác suất trong ví dụ chỉ xác định môi trường và cho phép người soạn kiểm chứng giá trị thật.

## 2. Học liệu và kiểm kê

| Mã | Tài liệu, loại, tác giả/đơn vị đã xác minh | Đường dẫn hoặc URL | Vị trí đã đọc trong các báo cáo được duyệt | Vai trò và trạng thái |
|---|---|---|---|---|
| L05 | *Dự đoán phi mô hình: Monte Carlo và Temporal Difference*, PDF bài giảng; chưa xác minh tác giả từ bản nguồn | `RL-hk2-2025-2026/lecture-05-du-doan-phi-mo-hinh.pdf` | Toàn bộ 33 trang; trang PDF trùng số in | Nguồn phạm vi, ví dụ và ánh xạ; đã phân tích đủ |
| HW05 | *Bài tập tuần 5 – Dự đoán phi mô hình*, PDF | `RL-hk2-2025-2026/resources/hw05-model-free-prediction.pdf` | Hai trang, đủ bảy bài | Nguồn bài tập; đã đọc, cần sửa giả thiết bài 4, 5, 7 |
| SB | Richard S. Sutton và Andrew G. Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, 2018; PDF bản quyền 2018, 2020 | [Trang sách MIT Press](https://mitpress.mit.edu/9780262039246/reinforcement-learning/); bản đã đọc `/tmp/rl04-rebuild/RLbook2020.pdf` và `book.txt` cùng thư mục | Mở đầu Ch.5 tr.91; §5.1 tr.92–96; §6.1–6.3 tr.119–128; §2.4–2.5 tr.30–33. Trang PDF bằng trang in cộng 22 | Sườn học thuật theo yêu cầu hiện tại; nội dung theo PDF 2020 đã kiểm, thông tin ấn bản đối chiếu trang nhà xuất bản |
| UCL | David Silver, *Lecture 4: Model-Free Prediction*, Advanced Topics 2015, COMPM050/COMPGI13 | [Trang môn](https://davidstarsilver.wordpress.com/teaching/), [PDF](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-4-model-free-prediction-.pdf) | PDF 51 trang; đọc tr.1–30; xem hình tr.9, 15, 19, 20, 30; nhận diện phần mở rộng tr.31–51 | Đối chiếu sư phạm; đã đọc. Năm trong URL tải lại không là năm bài giảng |
| ST | Emma Brunskill, Stanford CS234 Winter 2026, *Lecture 3: Model-Free Policy Evaluation* | [Trang môn](https://web.stanford.edu/class/cs234/modules.html), [PDF](https://web.stanford.edu/class/cs234/slides/lecture3pre.pdf) | PDF 53 trang; đọc tr.1–49; xem hình tr.14, 17–20, 26, 36, 38 | Đối chiếu sư phạm; đã đọc. Dẫn trang theo PDF, không theo mẫu số 67 ở chân trang |
| STYLE | Hướng dẫn trình bày của kho Học máy UET | [SLIDE_STYLE_GUIDE.md](https://raw.githubusercontent.com/uet-iai-course/machine-learning/main/SLIDE_STYLE_GUIDE.md) | Mục tiêu, cấu trúc, cấp phần/trang, hình, công thức, ví dụ, câu chữ và tiêu chí rà | Tham khảo bố cục; không sao chép CSS hoặc tài sản |
| TECH | Mẫu, CSS chung và danh mục học phần trong kho | `2627-1/lecture-template.html`, `lecture-slide.css`, `index.html` | Cấu trúc, cấu hình, lớp giao diện và thẻ Bài 05 | Nền kỹ thuật đã đọc; không kế thừa nội dung hoặc metadata của bài mẫu |

Nguồn L05 chứa nội dung hiển thị, công thức, các chuỗi trạng thái, quỹ đạo ký hiệu và bảng so sánh; không có mã, raster hay dữ liệu đường học thực nghiệm. Không có ghi chú diễn giả riêng để chuyển. Những câu hỏi trên trang nguồn là học liệu; mục lục lặp và phần ôn điều khiển không phải khái niệm mới của bài này. Các mục nguồn tr.1–14 chiếm nhiều trang ôn quy hoạch động, cần thu gọn theo sườn SB được người dùng chỉ định. Ánh xạ đủ 33 trang và bảy bài tập đặt trong outline để phục vụ triển khai.

Các báo cáo nguồn đã mở trực tiếp các tài liệu nêu trên. Công cụ chụp PDF trên web gặp lỗi; tác tử nghiên cứu tải PDF công khai và dựng ảnh tạm để đọc, không đưa ảnh đó vào bài. Hai bộ slide UCL và Stanford không là hai bằng chứng lý thuyết độc lập: Stanford ghi cấu trúc dựa trên Silver. Kết luận toán học được đối chiếu SB và tính lại; không dùng uy tín của trường thay cho kiểm chứng.

## 3. Đối chiếu hai bộ slide đại học

| Bộ slide và bằng chứng | Quan sát trực tiếp | Quyết định cho bài mới và lý do sư phạm |
|---|---|---|
| UCL tr.3–11 | Đặt đánh giá chính sách giữa quy hoạch động và điều khiển; MC đi từ lợi tức qua hai cách chọn lần ghé, Blackjack rồi cập nhật gia tăng | Giữ điểm vào từ đánh giá chính sách. Dùng chuỗi ngắn của L05 thay Blackjack để dùng lại trạng thái lặp và tránh học luật chơi mới |
| UCL tr.12–25 | TD được chuẩn bị bằng thời điểm cập nhật và hành trình về nhà; tiếp theo là sai lệch–phương sai, bước ngẫu nhiên và dữ liệu hữu hạn | Giữ thứ tự cơ chế TD trước so sánh. Tái dùng quỹ đạo L05 làm ví dụ cập nhật sớm; thêm A–B theo SB để phân biệt tiêu chuẩn trên dữ liệu hữu hạn |
| UCL tr.17–18, 22–23 | Phát biểu độ chệch/phương sai khá khái quát; có bài tính A–B nhưng không có kiểm tra riêng mọi phần | Ghi điều kiện kỳ vọng và giữ bảng $V$ cố định khi phân tích mục tiêu. Bố trí một trang kiểm tra riêng ở mỗi mạch |
| ST tr.2–5, 10–26 | Kiểm tra kiến thức cũ trước nhu cầu học từ trải nghiệm; hình dựng dần cây cập nhật; phân biệt tính chất thống kê của các ước lượng MC | Mở theo thứ tự giới thiệu → bản đồ → động lực → dữ liệu → kiểm tra. Tách lựa chọn mẫu khỏi quy tắc bước học trước giả mã MC |
| ST tr.35–38 | Dùng lại quỹ đạo xe tự hành cho TD và kiểm tra bước học | Dùng lại $e_1,e_2$ của L05 cho cả MC/TD. Mỗi thay đổi mục tiêu giữ nguyên dữ liệu, khởi tạo và $\alpha$ để so sánh |
| ST tr.36, 48 | Trang 36 có chỉ số lợi tức và điều kiện $\gamma$ không nhất quán; trang 48 dùng A–B | Không sao chép đáp án hoặc ví dụ trang 36. A–B dùng đúng tám lượt của SB và tính lại nghiệm |

Các quyết định trên là nhận định sư phạm của bản phân tích. Mỗi trang sẽ có một đối tượng chính, hình hoặc công thức đủ lớn, chú thích nêu quan hệ cần đọc. Mẫu và CSS chung trong kho quyết định giao diện; không mang CSS, phông hay tài sản từ kho đối chiếu vào bài.

## 4. Khái niệm và quan hệ phụ thuộc

| Mã | Khái niệm và vai trò | Đầu vào | Năng lực, mục tiêu | Phân biệt cần giữ | Đầu ra dùng tiếp |
|---|---|---|---|---|---|
| KN0 | Dự đoán giá trị, tiên quyết được nhắc | Chính sách, MDP, Bellman kỳ vọng | Nhận diện $v_\pi$ và mẫu; MT1 | Dự đoán/điều khiển; mô hình/mẫu; trạng thái/quan sát | KN1 và KN3 |
| KN1 | Lợi tức và MC, trọng tâm | Lượt kết thúc, kỳ vọng, trạng thái lặp | Tính $G_t$, chọn mẫu và trung bình; MT2–3 | Lợi tức/phần thưởng; lần ghé đầu tiên/mọi lần ghé | KN2; đối chiếu KN3 |
| KN2 | Cập nhật gia tăng và bước học, hỗ trợ thuật toán MC | Dãy mẫu hợp lệ của KN1 | Dùng $1/n$ hoặc $\alpha$ đúng mục đích; MT3 | Quy tắc chọn mẫu/quy tắc trọng số; $n$ của từng trạng thái/thời gian toàn cục | Giả mã MC; KN3 và điều kiện KN4 |
| KN3 | Mục tiêu một bước, sai số và TD(0), trọng tâm | $V$, bước học, mẫu chuyển, giá trị trạng thái kết thúc | Tính một bước và cả lượt; MT4 | Mục tiêu/giá trị thật; sai số TD/lỗi ước lượng; bảng trước/sau cập nhật | KN4 và KN5 |
| KN4 | So sánh thống kê và điều kiện áp dụng, trọng tâm | Cơ chế MC và TD | Giải thích kết luận có điều kiện; MT5–6 | Đích không chệch/ước lượng không chệch; mẫu mới/dữ liệu dùng lại | KN5; lựa chọn cuối bài |
| KN5 | Hai nghiệm trên dữ liệu cố định, trọng tâm giới hạn | Hai quy tắc cập nhật; tập tám lượt | Tính nghiệm MC/TD theo lô và tiêu chuẩn tương ứng; MT5–6 | Mô hình thực nghiệm/môi trường thật; quét đồng bộ/cập nhật tại chỗ | Quyết định dự đoán có căn cứ |

Quan hệ phụ thuộc: KN0 → KN1 → KN2 → KN3 → KN4 → KN5. KN0 nhận kết quả Bài 04 nhưng không cần nhắc lại phép co. KN2 nằm trong mạch MC vì giải quyết trực tiếp cách tính ước lượng đó; không tách thành phần chỉ để tăng số mạch. So sánh trên cùng dữ liệu được đặt sau khi người học đã thực hiện cả hai thuật toán. Dữ liệu A–B xuất hiện sau phân biệt mẫu mới với dữ liệu cố định, nên không đưa ngầm quy trình theo lô vào phần TD trực tuyến.

## 5. Mạch giảng từng khái niệm

### KN1 và KN2: từ một lượt kết thúc đến Monte Carlo

Vấn đề là chưa biết kỳ vọng lợi tức nhưng đã có các lượt tương tác. Chuỗi ngắn và $e_1,e_2$ cho phép nhìn thấy hai kết quả cuối khác nhau trước công thức. Trực giác là dùng kết quả quan sát sau trạng thái làm một mẫu của giá trị; cùng trạng thái có thể tạo nhiều mẫu trong một lượt. Dẫn nhập dùng B01–B02; B03 xác định $G_t$; B04 tính tập mẫu; B05 phát biểu MC; B06 tính trung bình gia tăng rồi B07 chứng minh đẳng thức; B08 tính bước học hằng rồi B09 tách hai trục lựa chọn; B10 cho quy trình đầy đủ; B11 vận dụng; B12 nêu điều kiện; B13 kiểm tra.

Đầu vào là cùng trạng thái $S,X$, hai lượt $e_1,e_2$, thưởng cuối $+1,-1$ và $\gamma=1$. Ký hiệu $G_t,N(s),\alpha_n(s)$ được ánh xạ trực tiếp vào các lợi tức và số mẫu đã đếm. Năng lực nhận diện: phân biệt mẫu hợp lệ và trọng số của mẫu. Năng lực sử dụng: tính bảng giá trị và giải thích vì sao $0.5$ sau lượt đầu đòi $\alpha=0.5$. Phương án mở bằng giả mã bị loại vì che khuất quyết định chọn lần ghé. Blackjack và Soap Bubble không được chọn vì thêm luật chơi hoặc vật lý mà không làm rõ hơn hai trục cần phân biệt.

MC gia tăng là dạng thuật toán của cùng ước lượng, không có chu trình trọng tâm riêng sáu trang. Chu trình hỗ trợ được gộp: vấn đề bộ nhớ và ví dụ ở B06, trực giác cân bằng tổng cũ/mẫu mới ở B06, hình thức ở B07–B09, quy trình và ứng dụng B10–B11, kiểm tra B13. Ví dụ số xuất hiện trước công thức tổng quát của từng quy tắc.

### KN3: từ chờ kết thúc đến TD(0)

C01 đặt giới hạn chờ kết thúc trên chính tiền tố của $e_1$. C02 giải thích dùng thưởng vừa nhận cộng dự đoán còn lại; bảng $V$ minh họa được ghi là ước lượng cho trước. C03 tính $0+1\times0.5=0.5$ rồi điều chỉnh $0$ thành $0.25$ với $\alpha=0.5$. C04 gắn ký hiệu mục tiêu, sai số và quy tắc; C05 trình bày đầu vào, khởi tạo, vòng lặp và dừng. C06 giải quyết trạng thái kết thúc và tự chuyển. C07–C08 chạy toàn bộ $e_1,e_2$; C09 đối chiếu chi phí; C10 kiểm tra. Driving Home không thêm vì chuỗi ngắn đã tạo đủ nhu cầu cập nhật trước kết thúc và giữ đối tượng giá trị nhất quán.

Đầu ra là bảng sau từng chuyển, trong đó các giá trị bên phải thuộc cùng $V_t$. $Y_t$ và $\delta_t$ là kết quả của phép tính C03, không là ký hiệu xuất hiện trước đối tượng. Người học phải phân biệt cập nhật sau một bước với truyền thưởng đến mọi trạng thái trước đó trong một lượt. Toàn bộ số của C07–C08 được tái dùng ở D01; không dùng hai lượt để suy ra tốc độ hội tụ tổng thể.

### KN4: so sánh có điều kiện

D01 nêu khác biệt thực tế trên cùng dữ liệu; D02 đối chiếu giá trị chuẩn của chuỗi ngắn. D03–D04 giữ chuỗi dài nguồn làm ví dụ dẫn nhập về độ dài và số mũ chiết khấu. Hai lợi tức khác nhau tạo trực giác về biến thiên, chưa đo phương sai. D04 đối chiếu hai lợi tức từ $S$ với giá trị chuẩn tại chính $S$, tạo nhu cầu tách kỳ vọng và biến thiên. D05 dùng lại chuỗi ngắn cùng bảng $V(X)=0.5,V(L)=0$, tính kỳ vọng mục tiêu $0.2$ trước khi hình thức hóa sai lệch; D06 giải thích nguồn ngẫu nhiên, với kết quả phương sai lý tưởng chỉ ở ghi chú; D07 nêu điều kiện hội tụ và giới hạn bước học hằng. Việc áp dụng các phân biệt này tiếp tục trên dữ liệu A–B, rồi D12 kiểm tra khả năng kết luận.

Phương án dùng đồ thị học MC/TD của SB bị loại: báo cáo không có bảng số gốc để vẽ lại trung thực, và bài đã đủ hai chuỗi nguồn. Không thêm bước ngẫu nhiên năm trạng thái của SB vì trùng vai trò chuẩn so sánh với chuỗi ngắn/dài. Không chuyển kết quả của một thí nghiệm thành định lý tốc độ học.

### KN5: hai tiêu chuẩn trên cùng dữ liệu hữu hạn

D08 đặt bài toán tái dùng tám lượt A–B và phân biệt kinh nghiệm trực tiếp của A với thông tin chuyển đến B. D09 tính lượt quét đầu từ bảng 0, sau đó nêu quy trình giữ bảng cố định trong lượt quét. Mặt trang khai báo $k,\Delta_k(s),y$ và hiển thị phép cộng từng gia số cùng phép ghi đồng thời. D10 tính nghiệm MC từ các lợi tức; D11 tính nghiệm TD từ quan hệ Markov thực nghiệm; D12 kiểm tra và yêu cầu nêu tiêu chuẩn. Ví dụ có ít trạng thái nhưng tạo hai nghiệm khác nhau, điều mà hai lượt chuỗi ngắn chưa giải thích.

Đầu vào gồm đúng một lượt $A,0,B,0$, sáu lượt $B,1$ và một lượt $B,0$, với $\gamma=1$. Đầu ra MC $(0,0.75)$ và TD $(0.75,0.75)$. Thứ tự được chọn đi từ dữ liệu → một lượt quét → quy trình → nghiệm → kiểm tra; không bắt đầu bằng mô hình thực nghiệm, vì người học cần thấy dữ liệu đầu vào vẫn là các mẫu. Quy trình theo lô là biến thể phục vụ so sánh, không mở tuyến ước lượng mô hình như thuật toán thứ ba.

## 6. Ví dụ và đặc tả trực quan

| Tài sản dự kiến | Dữ kiện, đối tượng và nhãn | Quan hệ cần nhìn thấy; vị trí |
|---|---|---|
| `short-walk.svg` | Bốn nút $L,S,X,G$; $L,G$ có hình dạng trạng thái kết thúc; nhãn $V(L)=V(G)=0$; từ nút trong đi phải 0.8, trái 0.2; thưởng −1/+1 trên cạnh đi vào trạng thái kết thúc, các cạnh còn lại 0 | Nhãn $X$ thay ô `.` của nguồn; xác suất môi trường tách khỏi mẫu thuật toán. B01, D02 |
| `episode-one.svg`, `episode-two.svg` | Mỗi lần ghé thành một nút riêng theo thời gian; $e_1:S,X,S,X,G$ có thưởng $(0,0,0,1)$; $e_2:S,X,S,L$ có thưởng $(0,0,-1)$ | Đánh dấu lần ghé đầu bằng khung và nhãn, mọi lần ghé bằng chỉ số; không gộp hai nút S. B02–B04, B11, C01, C07–C08 |
| `mc-td-targets.svg` | Hai hàng dùng cùng đoạn $S_t\to S_{t+1}\to\cdots\to S_T$; MC nối đến phần thưởng cuối; TD dừng phần quan sát ở $t+1$ rồi gắn nhãn $V_t(S_{t+1})$ | MC cần lợi tức hoàn chỉnh, TD dùng ước lượng còn lại. C02, D01 hoặc E01; không có trục số giả |
| `long-walk.svg` | Bảy nút $L,x_1,S,x_3,x_4,x_5,G$; bắt đầu tại S; đi phải 0.8, trái 0.2; $\gamma=0.99$; thưởng ở cạnh vào trạng thái kết thúc | Hai chuyển đến L và bốn chuyển đến G; giá trị ở trạng thái kết thúc bằng 0. D03 |
| `long-returns.svg` | Hai đường riêng $S,x_3,x_4,x_5,G$ và $S,x_1,L$; thưởng từng cạnh; chỉ số thưởng cuối là 4 và 2 | Công thức bên ngoài SVG: $0.99^3$ và $-0.99$. D04; SVG chỉ biểu diễn quỹ đạo, công thức dựng KaTeX |
| `ab-empirical.svg` | Ghi rõ “ước lượng từ tám lượt”; A→B có thưởng 0 và xác suất 1; B→trạng thái kết thúc có thưởng 1 sáu lần và 0 hai lần; giá trị ở trạng thái kết thúc bằng 0 | Quan hệ dữ liệu tạo nghiệm $V(A)=V(B)$ của TD; không là mô hình thật đã biết. D11 |
| `hw05-chain.svg` nếu cần trong chữa bài | $c_1,\ldots,c_5$, trạng thái kết thúc $c_5$; xác suất phải/đứng/trái 0.8/0.1/0.1; ở biên trái đứng tổng 0.2; $c_4\to c_5$ thưởng 10, còn lại −1 | Chuẩn có mô hình để đối chiếu dự đoán; không là đầu vào bắt buộc của MC/TD. Ngoài 120 phút |

Không cần hình minh họa trang trí, logo hoặc ảnh chụp. Bảng giá trị, dữ liệu A–B, thuật toán và công thức là HTML/KaTeX, không là SVG. SVG có `role="img"`, mô tả thay thế cụ thể, nhãn/hình dạng phụ trợ màu. Không tạo tài sản ở giai đoạn dàn bài.

Kết quả số đã kiểm: chuỗi ngắn $v_\pi(S)=11/21$, $v_\pi(X)=19/21$; chuỗi dài tại S là $0.829218798$, tại $x_5$ là $0.992155697$. Những số nguồn tr.19 và 30 đúng. Các giá trị còn lại của chuỗi dài lần lượt $0.456741288,0.932808109,0.970483318$ tại $x_1,x_3,x_4$. Chỉ đưa các số phục vụ luận điểm vào mặt trang; hệ giải và đối chiếu thuộc ghi chú.

## 7. Danh mục hình thức hóa

### HT1. Lợi tức và giá trị trạng thái: định nghĩa được nhắc lại

Với tập hữu hạn $\mathcal S$ của trạng thái không kết thúc, $\mathcal S^+$ bổ sung trạng thái kết thúc, $S_t\in\mathcal S^+$, $R_{t+1}\in\mathbb R$, $T$ là thời điểm kết thúc và $0\le\gamma\le1$:

$$G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},\quad G_T=0,\quad v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s].$$

Giả thiết khả tích được nêu khi dùng kỳ vọng; $\gamma=1$ trong chuỗi ngắn đi kèm kết thúc hầu chắc chắn và mômen hữu hạn. $v_\pi$ là giá trị thật, $V$ là bảng ước lượng; trạng thái kết thúc có giá trị 0. Từ định nghĩa suy ra $G_t=R_{t+1}+\gamma G_{t+1}$. Chứng minh một dòng bằng tách phần thưởng đầu, dùng để tính lùi trong MC. Nguồn SB §5.1 tr.92 và §6.1 tr.119–120; L05 tr.15–17. Vị trí A04, B03; không dạy lại MDP hay Bellman tối ưu.

### HT2. Ước lượng MC: định nghĩa và tính chất có điều kiện

Với $g_1(s),\ldots,g_n(s)$ là các lợi tức được chọn cho trạng thái $s$ theo quy tắc đã nêu:

$$V_n(s)=\frac1n\sum_{i=1}^n g_i(s).$$

Lần ghé đầu tiên chọn thời điểm nhỏ nhất trong từng lượt; mọi lần ghé chọn tất cả thời điểm có trạng thái đó. Với các lượt độc lập, lợi tức lần ghé đầu cùng phân phối, phương sai hữu hạn và số lượt ghé $s$ tăng vô hạn, trung bình này nhất quán; ở số mẫu cố định, nó không chệch. Các mẫu trong cùng lượt của mọi lần ghé có thể phụ thuộc; không chuyển nguyên lập luận độc lập sang ước lượng đó. Với quá trình phần thưởng Markov hữu hạn do chính sách Markov dừng, cố định tạo ra, phần thưởng bị chặn, kết thúc hầu chắc chắn từ mọi trạng thái không kết thúc đang xét, các lượt khởi động độc lập theo cùng phân phối và xác suất ghé $s$ dương, trung bình mọi lần ghé với $0\le\gamma\le1$ và bước học $1/N(s)$ hội tụ hầu chắc chắn về $v_\pi(s)$ khi số lượt hoàn chỉnh tăng vô hạn. Lập luận theo tổng lợi tức và số lần ghé ở cấp lượt, không coi lợi tức trong lượt độc lập. Kết luận không suy tính không chệch hữu hạn mẫu và không áp dụng nguyên văn cho bước hằng; không đưa chứng minh dài vào tuyến chính. Nguồn SB §5.1 tr.92–93; vị trí B04–B05, B12–B13.

### HT3. Trung bình gia tăng và bước học: đẳng thức và quy tắc cập nhật

$$V_n(s)=V_{n-1}(s)+\frac1n[g_n(s)-V_{n-1}(s)].$$

Chứng minh đầy đủ bằng tách tổng thành $n-1$ mẫu cũ và mẫu mới; $n$ đếm mẫu được chọn của chính $s$. Thay $1/n$ bằng $0<\alpha\le1$ tạo trọng số:

$$V_n(s)=(1-\alpha)^nV_0(s)+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}g_i(s).$$

Với $0<\alpha<1$, ảnh hưởng khởi tạo giảm dần và mẫu gần đây có trọng số lớn hơn; với $\alpha=1$, $V_n=g_n$ từ mẫu đầu tiên. Công thức trọng số chỉ cần giải thích sau ví dụ $+1,-1$; đặt khai triển tổng trong ghi chú nếu mặt trang quá tải. Đây không còn trung bình số học nói chung. Nguồn SB §2.4–2.5 tr.30–33, §6.1 tr.119; L05 tr.21–23. Vị trí B06–B09; dùng trong cả MC/TD và điều kiện hội tụ D07.

### HT4. TD(0): định nghĩa mục tiêu, sai số và quy tắc

$$Y_t=R_{t+1}+\gamma V_t(S_{t+1}),\quad\delta_t=Y_t-V_t(S_t),$$
$$V_{t+1}(s)=\begin{cases}V_t(s)+\alpha_n(s)\delta_t,&s=S_t,\\V_t(s),&s\ne S_t.\end{cases}$$

$V_t$ là bảng trước bước cập nhật; $n$ đếm cập nhật của $S_t$. Trạng thái kết thúc giữ 0. Dữ liệu sinh theo $\pi$; chỉ cập nhật sau quan sát một chuyển. Phát biểu và áp dụng sau ví dụ C03; không gọi sai số TD là lỗi thật. Nguồn SB §6.1 tr.119–121, L05 tr.24–25; vị trí C04–C10.

### HT5. Sai lệch kỳ vọng của mục tiêu TD: hệ quả Bellman

Ví dụ trước công thức dùng lại chuỗi ngắn: $\gamma=1$, $V(X)=0.5,V(L)=0$; từ $S$, $Y=-1$ với xác suất $0.2$ và $Y=0.5$ với xác suất $0.8$. Kỳ vọng là $1/5$, sai lệch so với $11/21$ là $-34/105$. Dữ kiện từ B01/C03/D02 ánh xạ trực tiếp vào $R_{t+1},S_{t+1},V$ trong công thức. Giữ bảng $V$ cố định, với cùng quy luật Markov của $\pi$ và các kỳ vọng hữu hạn:

$$\mathbb E_\pi[R_{t+1}+\gamma V(S_{t+1})\mid S_t=s]-v_\pi(s)=\gamma\mathbb E_\pi[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s].$$

Phác thảo bằng trừ phương trình Bellman kỳ vọng của $v_\pi$; không cần toán tử mới. Mục tiêu MC có kỳ vọng $v_\pi(s)$ theo HT1. TD có thể có sai lệch, nhưng không bắt buộc khác 0. Kết quả nói về mục tiêu với bảng cố định, không tự động nói về độ chệch của toàn bộ thuật toán. Nguồn SB §6.1–6.2 tr.120–124, suy ra trực tiếp từ Bellman; vị trí D05.

### HT6. Phương sai: cơ chế và trường hợp lý tưởng

Với trạng thái Markov và mômen bậc hai hữu hạn, mục tiêu dùng giá trị thật $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$ là kỳ vọng của $G_t$ khi biết chuyển đầu. Luật phương sai toàn phần cho $\operatorname{Var}(Y^*\mid S_t=s)\le\operatorname{Var}(G_t\mid S_t=s)$. Phần 3 phút của D06 chỉ dành cho nguồn ngẫu nhiên, cơ chế kỳ vọng phần đuôi và giới hạn của bảng $V$ bất kỳ. Khai triển bằng trường thông tin $\mathcal F_1$ và luật phương sai toàn phần là phần đọc phụ trợ trong ghi chú/học liệu, không tính như một chứng minh trình bày trọn vẹn trong 3 phút. Chưa có diễn tập thời lượng. Không thay $v_\pi$ bằng $V$ học được rồi giữ nguyên bất đẳng thức. Nguồn SB §6.2 tr.124 về cơ chế so sánh, kết quả điều kiện suy ra từ luật phương sai toàn phần; vị trí D06. Hai đường ở D04 chỉ minh họa, không là bằng chứng của bất đẳng thức.

### HT7. Điều kiện hội tụ: phát biểu giới hạn, không chứng minh

Đối với TD(0) dạng bảng theo chính sách trong môi trường hữu hạn Markov dừng, phần thưởng bị chặn, $0\le\gamma<1$, mọi trạng thái cần ước lượng được cập nhật vô hạn, và bước học từng trạng thái thỏa:

$$\sum_n\alpha_n(s)=\infty,\qquad\sum_n\alpha_n(s)^2<\infty,$$

có bảo đảm hội tụ đến $v_\pi$ với xác suất 1 dưới các điều kiện chuẩn này. Trường hợp $\gamma=1$ cần bài toán có lượt kết thúc hợp lệ, như chuỗi hấp thụ đang xét; không suy từ riêng $\gamma=1$ ra hội tụ. Bước học hằng trên mẫu mới không bảo đảm từng đường ước lượng hội tụ đúng. Phát biểu phạm vi và áp dụng, không chứng minh xấp xỉ ngẫu nhiên. Nguồn SB §2.5 tr.33, §6.2 tr.124–125; vị trí D07. Bảo đảm theo lô trên dữ liệu cố định ở HT8 là phát biểu khác.

### HT8. Quy trình theo lô và hai nghiệm: thuật toán so sánh, kết quả ví dụ

Đầu vào là tập lượt cố định $\mathcal D$, $\gamma$, bước học đủ nhỏ, ngưỡng $\varepsilon$ và ngân sách quét $K$. Khởi tạo $V_0$ tùy ý, giá trị ở trạng thái kết thúc bằng 0. Ở lượt quét $k$, giữ nguyên $V_k$ khi tính tất cả mục tiêu; cộng sai số theo trạng thái rồi ghi bảng mới một lần. MC dùng các lợi tức đã tính; TD dùng từng chuyển với $V_k$ ở trạng thái kế tiếp. Dừng thực hành khi thay đổi lớn nhất nhỏ hơn $\varepsilon$ hoặc hết $K$; cả hai không chứng minh đã biết giá trị của môi trường thật.

Tám lượt A–B cho $V_{\rm MC}(A)=0,V_{\rm MC}(B)=3/4$ và $V_{\rm TD}(A)=V_{\rm TD}(B)=3/4$. MC khớp lợi tức quan sát theo bình phương sai số; TD khớp Bellman của mô hình Markov thực nghiệm. Phép tính nghiệm trình bày đầy đủ trên hai trang, không chứng minh tối ưu tổng quát. Với phép cộng gia số ở D09, $\alpha=1/8$ ổn định cho chính ví dụ này; không biến nó thành lựa chọn chung. Nguồn SB §6.3 tr.126–128, Ví dụ 6.4; vị trí D08–D12.

MC có đầu vào $\pi,\gamma$, số lượt, quy tắc lần ghé và bước học; tính lùi mọi $G_t$ trước, rồi chọn mẫu theo chiều thời gian. Bộ đếm tăng trước khi dùng $1/N(s)$. TD có đầu vào tương tự nhưng ngân sách có thể tính bằng số chuyển; các giá trị bên phải được đọc trước khi ghi. MC cần $O(|\mathcal S|+T)$ bộ nhớ và $O(T)$ xử lý một lượt theo quy trình đã chọn; TD cần bảng $O(|\mathcal S|)$ và $O(1)$ tính mỗi chuyển. Những chi phí này tính cả bảng, không gọi MC hay TD là bộ nhớ hằng theo số trạng thái.

## 8. Quyết định tổng hợp và giới hạn bàn giao

Chọn năm mạch: mở đầu 5 trang/12 phút; MC 13 trang/35 phút; TD(0) 10 trang/27 phút; so sánh 12 trang/34 phút; kết luận 5 trang/12 phút. Tổng 45 trang/120 phút. Ứng dụng nằm cạnh khái niệm; không cần phần thực hành riêng trong 120 phút. Phần 30 phút chữa HW05 được dự toán riêng trong outline, không cộng vào thời gian trình chiếu.

Thay thứ tự dài của phần ôn quy hoạch động bằng sườn SB theo yêu cầu người dùng. Giữ chuỗi ngắn và dài của L05; thêm A–B có chức năng phân biệt hai tiêu chuẩn trên dữ liệu hữu hạn. Không thêm Blackjack, Driving Home, bước ngẫu nhiên năm trạng thái, bề mặt giá trị hoặc đường học thực nghiệm; các nội dung ấy trùng chức năng hoặc cần tài sản/dữ kiện ngoài nhu cầu hiện tại. Không có ngoại lệ raster.

Sửa nguồn tr.20 bằng cách nêu MC lần ghé đầu tiên và $\alpha=0.5$; tr.31 dùng số mũ 3 và 1; tr.26–28, 31 và HW05 bài 4 bỏ các kết luận ưu thế vô điều kiện. HW05 bài 5 tách lựa chọn lần ghé khỏi bước học, bỏ tiền đề cả ba cách luôn cùng hội tụ khi có bước hằng; bài 7 chỉ định rõ quy tắc lần ghé. Không gán tác giả cho L05 khi chưa xác minh. Không có số học trọng tâm còn bỏ ngỏ sau báo cáo kiểm toán.

Đã tự rà thứ tự và thuật ngữ theo Quill ở phạm vi dàn ý; không tạo `quill.json`. Đã biên tập no-ai-slop chế độ Edit và tự đối chiếu `eval.md`; kết quả từng nhóm kiểm tra được ghi trong review-log. Dàn bài đã qua kiểm định storyboard và được điều phối chấp nhận trước triển khai. Năm vai rà độc lập đã hoàn tất trên cùng bản cố định; các đề xuất được chấp nhận đã được sửa cục bộ. Điều phối viên đã chấp nhận các lượt rà lại toán học, góc nhìn sinh viên và toàn tuyến mạch viết; bản HTML sau sửa đã qua đủ 90 lượt kiểm hiển thị rộng/hẹp. Phạm vi, bằng chứng và giới hạn công cụ được ghi trong review-log.
