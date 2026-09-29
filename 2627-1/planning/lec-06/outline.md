# Dàn bài mới Bài 06: Điều khiển phi mô hình

Ngày lập: 29-09-2026. Trạng thái: đã triển khai, được năm vai độc lập rà và được điều phối viên chấp nhận làm đầu vào biên tập; bản dàn bài đã cập nhật sau biên tập, hoàn tất tái kiểm toán học và mạch viết, kiểm định kỹ thuật và trực quan cuối. [Phân tích và nguồn](analysis.md), [đặc tả từng trang](storyboard.md), [nhật ký](review-log.md). Dàn cũ không được dùng làm đầu vào. Các mã chỉ dùng nội bộ, không xuất hiện trên mặt trang hoặc trong ghi chú diễn giả.

## Thông tin chung và mục tiêu

Học phần Học tăng cường, học kỳ 1 năm học 2026–2027; sinh viên đại học đã học học máy, học sâu và thuật toán. Tiên quyết được nhắc: quá trình quyết định Markov (MDP), chính sách, kỳ vọng có điều kiện, giá trị trạng thái, đánh giá–cải thiện chính sách, Monte Carlo (MC), sai phân thời gian (TD). Nguồn bắt buộc: Tạ Việt Cường, `RL-hk2-2025-2026/lecture-06-model-free-control.pdf`, 30 trang. Không gán tên đơn vị chưa xác minh. Sườn học thuật: Sutton–Barto §§5.2–5.4, §§6.4–6.5; dùng đúng quan hệ tiên quyết và đặc tả thuật toán của sách.

Vấn đề trung tâm là học giá trị hành động từ lượt hoặc chuyển tiếp để chọn hành động tại D trong chuỗi A–E, đồng thời xác định giới hạn của bảng học được. Toàn bài dùng 45 trang trong bảy section ngoài, 120 phút gồm kiểm tra; 30 phút chữa bài riêng. Nguồn không có code demo, nên không tạo notebook/chương trình. Các dạng xấp xỉ hàm, thuật toán sâu, nhiều bước và chứng minh hội tụ đầy đủ nằm ngoài phạm vi.

| Mục tiêu | Năng lực | Nội dung chuẩn bị | Kiểm tra |
|---|---|---|---|
| MT1 | Phân biệt dự đoán/điều khiển, $q_\pi$/Q và thông tin có trong mẫu | A03–B03 | A05, B07 |
| MT2 | Tính $\varepsilon$-tham lam và xác định vai hành vi/đích | B04–B06, E01/E07 | B07, E08 |
| MT3 | Tính lợi tức, MC lần ghé đầu theo cặp, dùng đúng N | C01–C07 | C08 |
| MT4 | Tính Sarsa, giữ thứ tự chọn $A'$ và xử lý trạng thái kết thúc | D01–D07 | D08 |
| MT5 | Tính Q-learning, so sánh mục tiêu trên cùng bảng/dữ liệu | E01–E07 | E08 |
| MT6 | Kiểm giả thiết hội tụ và phân biệt với dừng theo ngân sách | F01–F04 | F05, G03 |
| MT7 | Chọn phương pháp và giải thích quyết định từ dữ liệu hữu hạn | G01–G02 | G03 |

## Thuật ngữ và ký hiệu

| Thuật ngữ/ký hiệu | Quy ước thống nhất |
|---|---|
| Động lực không đổi theo thời gian | Phân phối chuyển và phần thưởng theo cặp không thay đổi theo thời gian; phân biệt với kết thúc lượt và dừng ngân sách. |
| Tác tử, môi trường, trạng thái | Bài xét trạng thái Markov quan sát được; không thay “trạng thái” bằng “quan sát” tùy câu. Mô hình p không là đầu vào của thuật toán. |
| $\mathcal S,\mathcal S^+,\mathcal A(s)$ | Tập trạng thái không kết thúc; tập có bổ sung trạng thái kết thúc; tập hành động hợp lệ tại s. Bảng gồm $M=\sum_{s\in\mathcal S}|\mathcal A(s)|$ ô. |
| $S_t,A_t,R_{t+1}$ | Trạng thái và hành động ở thời điểm t; thưởng nhận sau hành động ấy. t là chỉ số tương tác; có thể đặt lại mốc trong một lượt khi ghi rõ. |
| $G_t,T,\gamma$ | Lợi tức: tổng phần thưởng chiết khấu từ t; T thời điểm kết thúc thật của lượt; $G_T=0$. $\gamma=1$ cần lợi tức tồn tại/khả tích khi dùng kỳ vọng. T không là ngân sách chạy. |
| $v_\pi,q_\pi,q_*$ | Giá trị đúng; $q_\pi(s,a)$ cố định hành động đầu a, các hành động sau theo $\pi$; $q_*$ giá trị hành động tối ưu. |
| $V,Q,Q_t,Q^{[k]}$ | Bảng ước lượng; $Q_t$ ngay trước cập nhật bước t; $Q^{[k]}$ trước lượt MC k. Dữ liệu và giả mã phải chỉ rõ đang dùng bảng nào. |
| $\pi,b$ | Chính sách đích và chính sách hành vi. Theo chính sách dùng cùng quy tắc chọn hành động và quy tắc trong mục tiêu. Q-learning: b sinh hành động, đích tham lam rút từ Q. |
| $m(s),\mathcal G_Q(s)$ | Số hành động và tập hành động đạt cực đại; chia đều phần khai thác khi đồng hạng. |
| $N(s,a),n,\alpha_n(s,a)$ | N đếm các lợi tức MC được chọn; n đếm cập nhật riêng của một cặp khi xét bước học. $N_0=0$; giá trị khởi tạo không là giả quan sát. |
| $C_t(s,a),\pi_t,\mathcal G_t(s)$ | Số lần thăm đến bước t; quy tắc chọn hành động theo $Q_t$; tập cực đại của chính bảng ấy. Dùng cho GLIE theo tương tác, không thay C bằng N của MC. |
| k | Chỉ số lượt MC hoặc lịch $\varepsilon_k$ giữ cố định trong lượt; không thay n hoặc t bằng k. |
| $Y_t,\delta_t$ | Mục tiêu cập nhật và $\delta_t=Y_t-Q_t(S_t,A_t)$; không phải sai số thật so với $q_\pi$ hoặc $q_*$. |
| $x_j,u_j$ | Trạng thái bộ sinh và số thao tác của bài nguồn 17; j đếm số tiêu thụ, không là t của môi trường. Không dùng $r_t$ vì dễ lẫn thưởng R. |
| Lượt; lần ghé đầu; mọi lần ghé | Lượt kết thúc tại A/E. Lần ghé đầu xác định theo chiều thời gian và theo cặp $(s,a)$, dù G được tính lùi. |
| MC; TD; Sarsa; Q-learning | Viết đầy đủ Monte Carlo (MC), sai phân thời gian (TD) ở lần xuất hiện đầu. Dùng nhất quán “Sarsa”, “thăm dò”, “tham lam”, “bước học”, “mục tiêu cập nhật”, “theo chính sách”, “khác chính sách”. |
| GLIE | Lần đầu: “tham lam trong giới hạn với thăm dò vô hạn (GLIE)”; gồm bao phủ và khối xác suất trên tập cực đại tiến tới 1. |

### Đối chiếu trực tiếp với Bài 05

| Bài 05 đã xác nhận | Bài 06 giữ hoặc mở rộng |
|---|---|
| $\mathcal S$ không kết thúc, $\mathcal S^+$ có kết thúc | Giữ; A/E thuộc $\mathcal S^+\setminus\mathcal S$; không tạo hàng Q trạng thái kết thúc có hành động giả. |
| $R_{t+1}$ và “lợi tức” $G_t$ | Giữ chỉ số và thuật ngữ; không luân phiên gọi G là thưởng tức thời. |
| $v_\pi$ khác V, $q_\pi$ khác Q | Giữ; tập trung vào giá trị hành động để cải thiện chính sách. |
| b hành vi, $\pi$ đích | Giữ; nguồn 19 dùng $\mu$, ánh xạ sang b một lần trong đọc thêm. |
| Kết thúc thật khác cắt dữ liệu | Giữ; mẫu 5 dừng ngân sách ở C vẫn dùng giá trị tiếp nối. |

## Bản đồ bảy mạch

| Mạch | Vai trò, chức năng | Đầu vào | Đầu ra và kết nối tiếp | Trang | Phút | Kiểm tra |
|---|---|---|---|---|---:|---|
| A. Bài toán điều khiển | Mở đầu; thiết lập quyết định tại D và loại dữ liệu | MDP, dự đoán MC/TD | Mẫu của một hành động chưa đủ so sánh mọi hành động; cần bảng Q | A01–A05 | 10 | A05 |
| B. Giá trị hành động và thăm dò | Khái niệm; xác định đối tượng học và quy tắc lấy hành động | Vấn đề thiếu dữ liệu của A | $q_\pi$/Q, phân phối mềm, vòng đánh giá–cải thiện; cần ước lượng từ lượt | B01–B07 | 18 | B07 |
| C. Điều khiển Monte Carlo | Thuật toán; học từ lượt hoàn chỉnh | Lợi tức, cặp, thăm dò | Quy trình lần ghé đầu MC và giới hạn chờ hết lượt | C01–C08 | 22 | C08 |
| D. Sarsa | Thuật toán; dùng mục tiêu một bước theo hành vi | MC, TD(0), Q, hành vi mềm | Quy trình và bảng cập nhật; mục tiêu còn phụ thuộc hành động thăm dò | D01–D08 | 22 | D08 |
| E. Q-learning | Khái niệm và thuật toán; tách hành vi/đích | Sarsa và năm mẫu đã công bố | Mục tiêu cực đại, so sánh hai bảng; cần xét điều kiện dài hạn | E01–E08 | 22 | E08 |
| F. Điều kiện bảo đảm | Khái niệm và áp dụng; giới hạn suy luận từ mẫu | Cơ chế ba thuật toán | Bao phủ, GLIE, bước học theo cặp, định lý có giả thiết | F01–F05 | 16 | F05 |
| G. Tổng hợp và kết luận | Thu hồi quyết định tại D; chọn phương pháp | Dữ liệu, mục tiêu, điều kiện | Chọn phương pháp có lý do; bài tập và đọc thêm có phạm vi rõ | G01–G04 | 10 | G03 |
| **Tổng** | **7 mạch, gồm mở đầu và kết luận** | | | **45 trang** | **120** | **7 trang riêng** |

## Dàn từng trang

Mỗi hàng là một luận điểm, không phải toàn bộ chữ trên mặt slide. Storyboard là phần đặc tả chi tiết của dàn bài này: đủ công thức, ví dụ, nguồn/trang, ghi chú, lý do thay đổi, quan hệ trước–sau và đáp án. Mã đầy đủ thêm tiền tố `L06-`.

| Mã | Tiêu đề | Nội dung trung tâm và sản phẩm | Phút |
|---|---|---|---:|
| A01 | Điều khiển phi mô hình | Bài 06, học phần, học kỳ; MC, Sarsa, Q-learning; tác giả nguồn đúng | 1 |
| A02 | Nội dung và mục tiêu | Bản đồ bảy mạch; năng lực tính, so sánh và kiểm giả thiết | 2 |
| A03 | Quyết định từ kinh nghiệm lấy mẫu | Chuỗi A–E, thưởng trên cạnh, bắt đầu D; cần chọn trái/phải từ dữ liệu | 3 |
| A04 | Từ dự đoán đến điều khiển | Ôn MDP/MC/TD; chính sách cho trước khác chính sách cần cải thiện | 2 |
| A05 | Thông tin có trong một mẫu | Câu hỏi xác định dữ kiện và phần còn thiếu từ $(D,1,10,E)$ | 2 |
| B01 | Giá trị của từng hành động | Bảng I tách hai ô ở D, quy tắc tham lam ban đầu và nhu cầu đánh giá; notes nêu giới hạn chia sẻ thông tin trực tiếp giữa các ô | 2 |
| B02 | Giá trị đúng và bảng ước lượng | Chính sách tiếp nối $\pi_L$; định nghĩa $q_\pi$, $G_t$, chỉ số/giả thiết; phân biệt Q và $q_*$ | 3 |
| B03 | Đánh giá và cải thiện từ dữ liệu | Vòng dữ liệu–Q–chính sách; hạn chế của hành động ít được thử | 2 |
| B04 | Phân bổ xác suất thăm dò | Ví dụ hai hành động, $\varepsilon=1/4$, xác suất 7/8 và 1/8 | 3 |
| B05 | Chính sách $\varepsilon$-tham lam | Công thức với tập cực đại, đồng hạng và lớp $\varepsilon$-mềm | 2 |
| B06 | Cải thiện với giá trị chính xác | Cùng $\varepsilon$, $q_\pi$ chính xác, kết luận không giảm; phác thảo ở notes | 3 |
| B07 | Xác suất và đối tượng được ước lượng | Câu hỏi tính phân phối, đồng hạng, diễn giải $q_\pi(D,0)$ và giới hạn của Q khởi tạo | 3 |
| C01 | Giá trị hành động từ lượt hoàn chỉnh | Gắn lợi tức của lượt với cặp; chính sách sinh lượt giữ cố định | 2 |
| C02 | Một cập nhật Monte Carlo | Bảng I, D→E, N0=0; mẫu đầu thay Q(D,1) bằng 10 | 2 |
| C03 | Trung bình mẫu theo lần ghé đầu | G tính lùi; N tăng trước phép chia; lần đầu theo cặp | 3 |
| C04 | Lấy mẫu một lượt từ dãy số đã cho | Bảng II, quy tắc tiêu thụ hai số khi thăm dò; xác định quỹ đạo | 3 |
| C05 | MC: thu thập và tính lợi tức | Đầu vào/khởi tạo; sinh lượt trọn vẹn, ghi chỉ số ghé đầu trước khi tăng thời gian rồi tính G | 3 |
| C06 | MC: cập nhật và cải thiện chính sách | Chọn lần ghé đầu, cập nhật N/Q, chính sách lượt sau, dừng và chi phí | 3 |
| C07 | Cập nhật từ lượt D–C–B–A | 998,999,1000; bảng cuối MC và hành động từ bảng | 3 |
| C08 | Lần ghé đầu của cặp | Câu hỏi quỹ đạo lặp D0; phân biệt lần ghé đầu, mọi lần ghé và bộ đếm | 3 |
| D01 | Cập nhật khi lượt chưa kết thúc | Giá trị tiếp nối ước lượng thay phần lợi tức chưa quan sát | 2 |
| D02 | Dữ liệu chung cho cập nhật một bước | Bảng I, năm mẫu, α=0.8, ranh giới ba lượt; hành động cho trước | 2 |
| D03 | Hai bước tính Sarsa | Mẫu 1 cho 0; mẫu 2 mục tiêu−1, sai lệch−2, Q mới−0.6 | 3 |
| D04 | Mục tiêu Sarsa | Công thức từ năm biến, bảng trước cập nhật, nhánh trạng thái kết thúc | 3 |
| D05 | Sarsa: khởi tạo và bước không kết thúc | Đầu vào/đầu ra, chọn A đầu, chọn A' trước cập nhật và giữ để thực hiện | 3 |
| D06 | Sarsa: kết thúc và ngân sách chạy | Chỉ tái khởi đầu khi kết thúc và còn ngân sách; dừng toàn bộ, bộ nhớ và chi phí | 3 |
| D07 | Cập nhật khi chuyển vào trạng thái kết thúc | Mẫu 3/4 cho 800 và 8.2; bảng trước mẫu 5 | 3 |
| D08 | Cập nhật Sarsa từ tiền tố | Câu hỏi mẫu 5 cho −1.28, thứ tự chọn A' và giới hạn ngân sách | 3 |
| E01 | Chính sách hành vi và chính sách đích | Tách hành động sinh dữ liệu với hành động trong mục tiêu | 2 |
| E02 | Một mục tiêu cực đại | Đặt lại bảng I; mẫu 2 cho mục tiêu 0 và Q mới 0.2 | 3 |
| E03 | Quy tắc Q-learning | Cực đại từ cùng bảng trước cập nhật; trạng thái kết thúc có mục tiêu R | 3 |
| E04 | Q-learning: lấy mẫu và cập nhật | Đầu vào/đầu ra; b chọn A; bốn biến đủ để tạo mục tiêu | 3 |
| E05 | Q-learning: kết thúc và chi phí | Chỉ tái khởi đầu khi kết thúc và còn ngân sách; dừng toàn bộ, chi phí cực đại/bộ nhớ | 2 |
| E06 | Hai bảng từ cùng năm mẫu | Kết quả đủ 5 mẫu, khác biệt bắt đầu tại C và truyền về D | 3 |
| E07 | Điều kiện sử dụng dữ liệu hành vi | Đúng MDP, độ phủ, dữ liệu cũ; khác chính sách không tự bảo đảm hiệu quả mẫu | 3 |
| E08 | So sánh hai mục tiêu một bước | Câu hỏi cùng bảng B=(800,1), A'=1; tính 0 và 799, điều kiện trùng | 3 |
| F01 | Phạm vi của bảo đảm hội tụ | Phép tính hữu hạn khác định lý; miền MDP hữu hạn, động lực không đổi theo thời gian, thưởng chặn, γ<1 | 3 |
| F02 | Hai yêu cầu của GLIE | Thăm vô hạn và tham lam trong giới hạn; lịch giảm chưa suy độ phủ | 3 |
| F03 | Bước học theo từng cặp | 1/n, hằng 0.8 và đếm theo t khác n; Robbins–Monro | 3 |
| F04 | Hội tụ của Sarsa và Q-learning | Điều kiện chung; Sarsa thêm giới hạn tham lam, Q-learning không cần; giới hạn MC | 4 |
| F05 | Kiểm tra giả thiết bảo đảm | Câu hỏi phân loại lịch và hành vi dưới miền chiết khấu đã cho | 3 |
| G01 | Dữ liệu và mục tiêu của ba phương pháp | Bảng so sánh thời điểm cập nhật, đích, hành vi, bộ nhớ | 3 |
| G02 | Quyết định tại D sau các mẫu đã cho | Thu hồi mở bài: bảng hữu hạn dẫn lựa chọn nhưng chưa chứng minh tối ưu | 2 |
| G03 | Lựa chọn phương pháp có điều kiện | Câu hỏi ba trường hợp dữ liệu/mục tiêu; nêu thiếu giả thiết | 3 |
| G04 | Bài tập và tài liệu đọc | Nhiệm vụ chữa nguồn 16–18/21, H03; SB; đọc thêm sửa nguồn 19/29 | 2 |

## Ánh xạ đủ 30 trang nguồn

| Trang L06 | Nội dung | Quyết định | Đích, lý do |
|---:|---|---|---|
| 1 | Giới thiệu và tác giả | Giữ, sửa | A01; tên Sarsa và metadata đúng học phần/học kỳ, không gán đơn vị. |
| 2 | Mục lục | Sửa | A02; bảy mạch theo phụ thuộc, ví dụ đặt tại khái niệm. |
| 3 | Dự đoán phi mô hình | Gộp, sửa | A04–A05; đủ tiên quyết và phân biệt mô hình với mẫu. |
| 4 | MC dự đoán, lợi tức, cập nhật | Gộp, sửa | A04, C01–C03; chuyển từ trạng thái sang cặp, không giữ “không chệch” thiếu giả thiết hoặc “không khả thi với cờ vua”. |
| 5 | TD(0) và mục tiêu một bước | Gộp, sửa | A04, D01/D04; không suy cập nhật sớm luôn hiệu quả mẫu hơn. |
| 6 | Vòng tương tác, điều khiển | Tách, sửa | A03–A04, B03; quy trình chạy theo ngân sách, không “đến hội tụ” mơ hồ. |
| 7 | Q và chính sách tham lam | Tách, sửa | B01–B05, G01; tách q thật/Q, miền hành động và đồng hạng, bộ nhớ bảng; notes B01 và học liệu §2.1 giữ giới hạn không chia sẻ trực tiếp giữa các ô, dù trạng thái tương tự. |
| 8 | Theo/khác chính sách | Sửa, tách | C01, D04, E01/E07; xác định bằng hai vai, không bằng “gần như” hoặc ưu thế mẫu chung. |
| 9 | Một bước, tiền tố, lượt | Gộp, sửa | C01, D01–D02, E03, G01; phân biệt MC cần lượt, Sarsa cần A', Q-learning chỉ cần bộ bốn. |
| 10 | Cập nhật MC | Tách, sửa | C02–C03, C05–C08; chọn lần ghé đầu theo cặp, N0=0 và quy trình đủ. |
| 11 | Cải thiện MC, lịch 1/k | Tách, sửa | C05–C06, F02; π cố định trong lượt, giảm epsilon chưa tự GLIE. |
| 12 | Từ MC sang TD control | Giữ, tách | D01/D03/D04; bước số trước quy tắc chung. |
| 13 | Sarsa | Tách, sửa | D03–D04; mục tiêu đúng bảng, hành động kế tiếp và nhánh trạng thái kết thúc. |
| 14 | Giả mã Sarsa | Tách, sửa | D05–D06; không chọn A' tại trạng thái kết thúc, ngân sách toàn bộ và chi phí. |
| 15 | Chuỗi năm trạng thái, bảng I | Tách, sửa | A03, B01/B04, C02, D02; đưa dữ kiện sớm; sửa ba bước thành độ dài mẫu, thưởng trên cạnh. |
| 16 | MC tham lam và quá trình cảm sinh | Giữ, sửa | B04/C02; giữ vòng B↔C, chỉ lượt từ D hoàn tất; chữa riêng 30 phút. |
| 17 | MC thăm dò, bảng II, bộ sinh số | Tách, sửa | C04/C07; u_j, thứ tự tiêu thụ số, đầu mút, N0=0; dãy tất định chỉ cho thao tác. |
| 18 | Sarsa năm mẫu, α 0.8 | Tách, sửa | D02–D08; bổ sung mẫu và biên lượt đã công bố, không suy quỹ đạo từ epsilon. |
| 19 | Công thức V mang nhãn Sarsa | Sửa, chuyển đọc thêm | E01/E07 giữ vai hành vi/đích; học liệu §7.4 triển khai đặc tả analysis §7 DT1: V và tỉ số nhân mục tiêu, đẳng thức kỳ vọng của gia số chưa nhân bước học; G04 dẫn đọc. Không có slide công thức IS trong tuyến chính. |
| 20 | Q-learning | Tách, sửa, thêm | E02–E05; ví dụ trước công thức; quy trình đủ từ SB tr. 131; mục tiêu cực đại là ước lượng. |
| 21 | Q-learning năm mẫu, bảng II | Sửa, tách | E02/E06/E08; đổi sang bảng I và cùng 5 mẫu với Sarsa để chỉ thay mục tiêu, hai bảng chạy riêng. |
| 22 | Dự đoán/điều khiển, so sánh | Gộp, sửa | A04, G01–G03; giữ ba phương pháp đã học, không mở actor–critic. |
| 23 | Ma trận họ thuật toán | Gộp, bỏ một phần | G01 chỉ đối chiếu MC/Sarsa/Q-learning. Lược Expected Sarsa, TD(λ), REINFORCE, REINFORCE with Advantage, A2C, A3C, TRPO, PPO, DQN, Double DQN, Dueling DQN, DDPG, TD3, SAC, IMPALA: chưa có tiên quyết/thuật toán và nguồn trộn các tiêu chí phân loại. TD(0) giữ ở tiên quyết, không gọi là thuật toán điều khiển. |
| 24 | Cải thiện epsilon-tham lam | Sửa, chuyển cục bộ | B06; gần cơ chế thăm dò, cùng epsilon, q chính xác, giả thiết γ<1; proof dài trong notes. |
| 25 | GLIE | Sửa | F02/F05; chỉ số t nhất quán, tập cực đại xử lý đồng hạng, gần chắc chắn, lịch 1/k không tự độ phủ. |
| 26 | Hội tụ MC từ GLIE | Sửa | F04 và notes; bỏ định lý thiếu giả thiết, tách trung bình cố định với chính sách đổi. Không tuyên bố tình trạng nghiên cứu hiện nay. |
| 27 | Hội tụ Sarsa | Sửa | F01/F03/F04; đủ miền định lý, bước học theo cặp, chính sách giới hạn tham lam. |
| 28 | Hội tụ Q-learning | Sửa | E07, F01/F03/F04; hành vi cần phủ, không cần tham lam; không tuyên bố ưu thế mẫu chung. |
| 29 | Chặn MC hữu hạn mẫu | Sửa, chuyển đọc thêm | Học liệu §7.5 theo analysis §7 DT2, G04 dẫn đọc; định nghĩa J, lợi tức độc lập, độ rộng B, n cố định; không gọi độ phức tạp điều khiển, không áp γ 1. |
| 30 | Tổng kết | Sửa | G01–G04; thu hồi quyết định ở D, đối chiếu mục tiêu và kiểm tra tổng hợp; lược câu quảng bá học sâu. |

Các phần thêm có căn cứ: bảy trang kiểm tra; khung mục tiêu/tiên quyết; cơ chế chia đều đồng hạng; giả mã Q-learning; nhánh trạng thái kết thúc, chi phí và ngân sách; ví dụ C08 suy từ môi trường nguồn; ví dụ E08 suy từ bảng đã tính. Không thêm nguồn số liệu thực nghiệm. 30/30 trang đều có đích hoặc quyết định lược rõ.

## Điều kiện triển khai và tự kiểm

Học liệu đã ánh xạ bảy mạch với `lec-06-topic-01` tới `lec-06-topic-07`; các mã chỉ nằm trong thuộc tính/comment nội bộ. DT1/DT2 nằm ở mục đọc thêm của chủ đề 07, không tạo section chính thứ tám. Dùng nguồn, bảng ký hiệu và dữ kiện trong bản này làm cơ sở, không đọc lại nội dung Bài 06 cũ để tái sử dụng.

Tổng thời lượng đã cộng đúng 120 phút; bảy kiểm tra đều có dữ kiện, lời giải và tiêu chí trong storyboard. Mẫu số, trạng thái kết thúc, chỉ số thời gian và sự khác nhau Q/q được chốt trước giả mã. no-ai-slop Edit đã loại lời dẫn rỗng, diễn đạt so sánh thiếu phạm vi và thuật ngữ luân phiên; tự kiểm eval giữ định nghĩa, giả thiết và yêu cầu học tập. Quill xác nhận đầu ra mỗi mạch được dùng ở mạch kế, kết luận dùng lại quyết định D, không có khái niệm trọng tâm mới ở kết bài. Bản nháp HTML và học liệu đã được kiểm kỹ thuật và rà độc lập; phạm vi thực kiểm nằm trong review-log. Các vùng thay đổi sau biên tập đã được tái kiểm và kiểm định cuối trên đúng bản mới; bằng chứng và giới hạn nằm trong review-log.
