# Nhật ký rà soát Bài 01: Giới thiệu Học tăng cường

## Trạng thái bản nháp

- Tệp nguồn: `RL-hk2-2025-2026/lecture1-introduction-to-RL.pptx`, 45 trang.
- Bản RevealJS: 42 trang, từ `P00` đến `Z00` theo storyboard.
- Dự án Codex Slides: `20260824091941-b-i-01-gi-i-thi-u-h-c-t-ng-c-ng-83wl`.
- Bản hiện tại đã qua kiểm định storyboard, ba rà soát độc lập và vòng chỉnh sửa hợp nhất.
- Dàn ý do Codex Slides đề xuất có thêm nội dung ngoài nguồn. Các phần về quy trình quyết định Markov, phương trình Bellman, học sai phân thời gian, epsilon-greedy và thuật toán chuyên sâu đã bị loại để giữ đúng phạm vi.

## Quyết định có chủ ý so với nguồn

| Thay đổi | Lý do | Tác động |
|---|---|---|
| 45 trang nguồn thành 42 trang đích | Gộp bốn trang hình tiến bộ gần đây, các trang thông tin học phần và câu hỏi trắc nghiệm; tách các khái niệm quá tải. | Giữ thứ tự ý chính, giảm lặp và tăng khả năng đọc. |
| Thay toàn bộ hình kỹ thuật bằng 12 SVG | Không dùng ảnh raster; bảo đảm nhãn và mô tả thay thế. | Quan hệ khái niệm được giữ, ảnh trang trí bị bỏ. |
| AlphaGo và thao tác robot thay các trang ảnh không có luận điểm | Giữ đúng hai miền xuất hiện ở trang nguồn 11–13. | Vẽ robot bằng SVG nội dòng; không thêm thuật toán hoặc số liệu ngoài nguồn. |
| AGI chuyển thành thảo luận | Nguồn đưa các phát biểu khái quát chưa có bằng chứng đủ. | Không kết luận về con đường hoặc điều kiện cần của AGI. |
| Mô hình môi trường ghi là tùy chọn | Không phải mọi tác tử Học tăng cường đều dùng mô hình tường minh. | Thêm phân biệt có mô hình và phi mô hình ở mức nhập môn. |
| Trang cảm ơn đổi thành tài liệu đọc và tự kiểm tra | Kết thúc bằng sản phẩm học tập. | Không thay đổi nội dung kiến thức trước đó. |
| Thông tin học phần và đánh giá đặt trong phụ lục | Dữ liệu lấy từ bản nguồn tháng 02/2026. | Giữ truy nguyên mà không ngắt tuyến bài chính. |
| Chuyển H00–H03 thành phụ lục dọc dưới Z00 | Chuẩn đầu ra, lịch và đánh giá thuộc học phần khác trong nguồn, chưa được xác nhận cho 2026–2027. | Tuyến ngang 150 phút dừng tại Z00; nhấn ↓ mới mở phụ lục; không gán mã CLO nguồn cho bài hiện tại. |
| Đưa H04–H05 liền sau G04 | Ôn tập cần diễn ra ngay sau khi hoàn tất ví dụ tổng hợp. | Mạch kiến thức khép trước hai thảo luận cuối buổi. |

## Lỗi nguồn đã sửa

| Vị trí nguồn | Lỗi hoặc điểm thiếu | Cách sửa |
|---|---|---|
| Trang 29–30 | Hành động ghi chung là số 1–9, chưa phụ thuộc thế cờ. | Dùng $A_t\in\mathcal A(S_t)$, trong đó $\mathcal A(S_t)$ là tập ô trống. |
| Trang 29–30 | Tập thưởng ghi `{1, 0, -1, 9}`. | Theo góc nhìn tác tử: $+1$ thắng, $-1$ thua, $0$ hòa hoặc chưa kết thúc. |
| Trang 26 | Gọi chính sách, giá trị và mô hình là ba thành phần chính theo cách dễ hiểu là bắt buộc. | Ghi mô hình là thành phần tùy chọn. |
| Trang 14–15 | Phát biểu AGI và foundation agent theo dạng kết luận. | Chuyển thành câu hỏi thảo luận có giới hạn bằng chứng. |
| Trang 35 | Tỷ lệ đánh giá có ghi chú có thể thay đổi. | Giữ tỷ lệ trong phụ lục; bỏ câu hướng dẫn trên mặt chiếu theo yêu cầu người dùng. |

## Kiểm kê SVG

| Tệp | Nội dung | Trang dùng |
|---|---|---|
| `agent-environment.svg` | Vòng tương tác tác tử–môi trường | A00 |
| `control-learning.svg` | Điều khiển cố định và học từ tương tác | A03 |
| `uncertainty.svg` | Một hành động, nhiều kết quả | A04 |
| `rl-fields.svg` | Các lĩnh vực liên quan | C00 |
| `learning-signals.svg` | Ba dạng tín hiệu học | C02 |
| `delayed-reward.svg` | Phần thưởng trễ trên quỹ đạo | D00 |
| `rl-components.svg` | Chính sách, hàm giá trị, mô hình tùy chọn | E00 |
| `explore-exploit.svg` | Đánh đổi thăm dò–khai thác | F00 |
| `tictactoe-board.svg` | Bàn cờ và số hiệu hành động | G00 |
| `tictactoe-search.svg` | Cây tìm kiếm | G01 |
| `tictactoe-value.svg` | Đánh giá thế cờ | G03 |
| `course-map.svg` | Bản đồ học phần | H00 |

Tất cả SVG dùng bảng màu `#2F3E7A`, `#B15A2B`, `#2E7D32`, `#F7EFE6`; có `role="img"`, `title` và `desc`. Không có ngoại lệ raster.

## Báo cáo rà soát

Các báo cáo dưới đây sẽ được tác tử chỉ đọc bổ sung sau bản nháp đầu. Mỗi mục phải dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

### Kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | Bản đồ hành trình | Hai cụm lớn gộp nhiều khái niệm, không chỉ ra đúng sáu hành trình. | Tác tử, tín hiệu học, phần thưởng, thành phần, đánh đổi và Tic-tac-toe dùng chung các cột. | Tách thành sáu cụm và phân bổ đủ 120 phút. | Áp dụng. Storyboard hiện có sáu cụm, tổng 120 phút. |
| nghiêm trọng | A00–G04 | Một số cụm bắt đầu bằng trực giác hoặc tên khái niệm, chưa nêu vấn đề cần giải quyết. | A00, C00, E00 và F00 chưa chỉ ra quyết định hoặc giới hạn trước phần giải thích. | Đặt vấn đề trên mặt chiếu và giữ thứ tự vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra. | Áp dụng tại A00, C00, E00 và F00; cập nhật câu nối trong storyboard. |
| nghiêm trọng | D00–D03 | Cụm phần thưởng chưa có ví dụ số và tự kiểm tra. | D02 chỉ nêu công thức; người học chưa tính $G_t$. | Dùng chuỗi thưởng trên D00 để tính tổng và thêm câu hỏi sau phần ứng dụng. | Áp dụng tại D01–D03. |
| nghiêm trọng | E00–G03 | Chính sách và hàm giá trị chưa được nối bằng cùng một ví dụ. | E01 nêu hai định nghĩa rời; G03 chỉ nói về giá trị. | Dùng Tic-tac-toe từ E00 và chỉ ra chính sách dùng giá trị để chọn nước ở G03. | Áp dụng. |
| chặn bàn giao | G00 | Giả thiết về đối thủ chỉ nằm trong ghi chú. | Giá trị thế cờ phụ thuộc hành vi tiếp tục chơi. | Hiển thị giả thiết đối thủ chọn ngẫu nhiên một nước hợp lệ. | Áp dụng trên mặt G00. |
| nghiêm trọng | G04–H05 | Ôn tập bị ngăn cách bởi bốn trang thông tin học phần. | H00–H03 đứng giữa ví dụ tổng hợp và H04–H05. | Đưa ôn tập liền sau G04. | Áp dụng; thứ tự trình chiếu là G04, H04, H05. |
| chặn bàn giao | H00–H03 | Thông tin chưa xác nhận bị trình bày như nội dung hiện hành và dùng mã CLO của học phần khác. | Nguồn tháng 02/2026 ghi *Intelligent Agents and Robotics*. | Chuyển thành phụ lục, ghi chưa áp dụng và bỏ gán CLO. | Áp dụng; H00–H03 nằm sau Z00, dùng nhãn phụ lục và `Không gán` trong storyboard. |
| nghiêm trọng | Kế hoạch thời lượng | 30 phút cuối gộp thông tin học phần, ôn tập và thảo luận nên không khả thi. | Outline không phân bổ thời gian theo hoạt động. | Chia 30 phút cho H04–H07 và Z00; loại code demo vì nguồn không có mã. | Áp dụng: 6 + 7 + 7 + 7 + 3 phút. |

Không có đề xuất nào của vòng kiểm định storyboard bị từ chối. Bản sửa giữ 42 trang; chỉ đổi thứ tự H00–H05 và sửa vai trò của các trang liên quan.

### Tái kiểm định storyboard

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | A00–B02 | Hàng hành trình gán trực giác và ví dụ cho các trang không khớp nội dung hiện tại. | A00 đã chứa vòng tương tác và ví dụ robot; A01 tách thành phần; A02–A04 đối chiếu khả năng học với mô hình cố định. | Ghi A00 là vấn đề, trực giác và ví dụ; A01 là hình thức; A02–A04 là ứng dụng hoặc đối chiếu; B01–B02 là trường hợp và kiểm tra. | Áp dụng; A00 được làm rõ bằng ví dụ robot, không đổi thứ tự. |
| nghiêm trọng | C05 | Trang liệt kê lại bốn khác biệt, chưa tạo nhiệm vụ áp dụng. | C05 lặp nội dung đã nêu và câu hỏi chỉ yêu cầu chọn hai mục. | Dùng tình huống có tương tác và phản hồi trễ; yêu cầu xác định dạng học bằng hai dấu hiệu. | Áp dụng; C05 còn một luận điểm trung tâm. |
| nghiêm trọng | Z00, H00–H03 | Phụ lục nằm trên tuyến ngang sau trang kết thúc. | Phím → vẫn đi vào bốn trang thông tin chưa xác nhận. | Đặt Z00 và H00–H03 trong một stack dọc; thêm chỉ dẫn nhấn ↓. | Áp dụng; tuyến ngang kết thúc tại Z00. |
| trung bình | B00 | Tiêu đề “Tiến bộ gần đây” mô tả thời điểm, chưa nêu chức năng học tập. | Hai trang sau là hai trường hợp để đối chiếu khái niệm. | Đổi thành “Hai trường hợp tiêu biểu” và nêu hai dấu hiệu cần kiểm tra. | Áp dụng. |
| trung bình | D00–F03 | Vai trò trong bản đồ không khớp nội dung sau vòng sửa đầu. | D00 đặt vấn đề; E02 và G04 cùng kiểm tra thành phần; F00 đã có tình huống chọn nước. | Cập nhật từng cột theo nội dung hiện hành. | Áp dụng; không đổi thứ tự trang. |
| nhẹ | H06 | “Chính sách tổng quát” có thể gợi một loại chính sách đã được định nghĩa. | Bài chỉ nói robot đa nhiệm, chưa định nghĩa chính sách tổng quát. | Dùng “tác tử học trên nhiều nhiệm vụ”. | Áp dụng. |

Tái kiểm định không yêu cầu thêm, bỏ hoặc đổi thứ tự trang. Thay đổi cấu trúc duy nhất là gộp Z00 và H00–H03 thành một stack dọc RevealJS.

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | G00 | Số ô chồng lên quân cờ. | Các ô 1, 5, 9 cùng hiển thị số và quân. | Chỉ đánh số ô trống. | Áp dụng; hình hiện chỉ đánh số 3, 6, 7, 9. |
| nghiêm trọng | A00, A03, C02, E00, F00 | Nhãn SVG nhỏ khi chiếu. | Nhiều nhãn chỉ 19–25 px trong viewBox rộng. | Tăng nhãn cốt lõi lên khoảng 30–32 px và rút câu. | Áp dụng cho cả 12 SVG; nhãn dài được rút và dùng thêm chiều rộng. |
| nghiêm trọng | H00–H07 | CSS thu nhỏ toàn bộ phần H. | Quy tắc riêng đặt cỡ `.78em`, thấp hơn tuyến chính. | Bỏ quy tắc thu nhỏ riêng. | Áp dụng; mọi trang dùng cỡ cơ sở `.84em`. |
| trung bình | F03 | Bảng khó đọc hơn phần thân bài. | Bảng dùng cỡ `.78em`. | Tăng cỡ bảng. | Áp dụng bằng lớp `large-table` ở `.94em`. |
| trung bình | G01 | Cây chỉ có các hộp trống nên khó nối với luật chơi. | Nút không chứa thế cờ hoặc nước đi. | Vẽ thế cờ gốc và các nước 3, 7, 9. | Áp dụng. |
| trung bình | H04 | Ôn tập chưa kiểm tra dữ liệu phụ thuộc thời gian. | Câu hỏi chỉ nhắc thử–sai và thưởng trễ. | Hỏi vì sao không thể tráo thứ tự chuỗi. | Áp dụng và bổ sung đáp án trong ghi chú. |
| nhẹ | Câu hỏi | Đáp án có thể hiện dần bằng `fragment`. | Đáp án hiện chỉ ở ghi chú diễn giả. | Thêm fragment khi chữa bài. | Không áp dụng. Bản nguồn không dùng hiệu ứng; đáp án trong ghi chú giữ mặt chiếu ổn định và tránh làm thay đổi nhịp bàn phím. |

### Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | B02 | Ca trò chơi nhiều tác tử không khớp trang nguồn 12–13. | Hai trang nguồn là thao tác robot. | Trả B02 về gắp, sắp xếp và đổi tư thế vật. | Áp dụng; bỏ ca và nguồn ngoài bản gốc. |
| nghiêm trọng | A01 | Chưa phân biệt trạng thái với quan sát. | Hai thuật ngữ xuất hiện như một loại dữ liệu. | Nêu trạng thái là tình huống thực, quan sát là dữ liệu tác tử nhận. | Áp dụng ở nội dung và ghi chú. |
| nghiêm trọng | B01 | Dùng “mạng chính sách” và “mạng giá trị” trước khi định nghĩa. | Hai thuật ngữ chỉ được giải thích ở phần E. | Diễn đạt bằng học đánh giá nước đi và tìm kiếm cây. | Áp dụng. |
| nghiêm trọng | C01, C05 | Chưa dạy và đánh giá sự phụ thuộc thời gian. | Bài chỉ nói thu thập kinh nghiệm. | Nêu hành động đổi dữ liệu sau và thêm câu hỏi không tráo thứ tự. | Áp dụng; H04 cũng kiểm tra lại. |
| nghiêm trọng | D03 | Giả thuyết phần thưởng còn dễ đọc như mệnh đề phổ quát; ví dụ token ngoài mạch nguồn. | Câu đầu khẳng định mọi mục tiêu được biểu diễn. | Viết điều kiện mô hình hóa, nêu giới hạn và dùng robot. | Áp dụng. |
| nghiêm trọng | E01 | Chính sách bị mô tả như ánh xạ tất định; giá trị không gắn với chính sách. | Không có phân phối hay nguồn ngẫu nhiên của kỳ vọng. | Dùng $\pi(a\mid h_t)$ và $V^\pi(h_t)$. | Áp dụng; ghi rõ kỳ vọng theo chính sách và môi trường. |
| nghiêm trọng | E02 | Mô hình chỉ mô tả thay đổi chung. | Thiếu dự báo phần thưởng và phân biệt quan sát/trạng thái. | Nêu dự báo đại lượng kế tiếp và thưởng. | Áp dụng. |
| trung bình | A03–A04 | Đối chiếu mô hình cố định có thể bị hiểu thành Học tăng cường luôn phi mô hình. | Chưa có câu nối tới mô hình học được. | Nêu Học tăng cường có mô hình hoặc phi mô hình. | Áp dụng; E02 khép lại câu nối. |
| trung bình | C00 | Sơ đồ lĩnh vực thiếu Thần kinh học so với nguồn. | Trang nguồn 18 có nhánh NeuroScience. | Thêm nhánh. | Áp dụng trong `rl-fields.svg`. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | D00–D02 | Chỉ số phần thưởng và số trạng thái không khớp. | Hình có bốn trạng thái nhưng công thức dùng bốn phần thưởng; D01 gọi $R_t$ là thưởng tại bước $t$. | Dùng $S_0,\ldots,S_4$, $A_0,\ldots,A_3$, $R_1,\ldots,R_4$; xác lập $t,T$. | Áp dụng trong hình, công thức và ghi chú. |
| chặn bàn giao | G03 | Ba số giá trị là tùy ý và trạng thái không được vẽ. | Không thể kiểm chứng $-0,4$, $0,1$, $0,7$. | Dùng một thế cờ gốc, ba nước hợp lệ và phần tiếp diễn dưới cùng $\pi$. | Áp dụng; bỏ số tùy ý, tách thưởng +1 của nước thắng khỏi giá trị tương lai 0 ở trạng thái kết thúc. |
| nghiêm trọng | G00 | “Ngẫu nhiên” chưa xác định phân phối. | Giá trị phụ thuộc cách đối thủ chọn. | Quy định đối thủ chọn đều trên nước hợp lệ. | Áp dụng. |
| nghiêm trọng | G02 | Thưởng chưa ghi góc nhìn và thời điểm; tập hành động chưa phụ thuộc trạng thái. | Có thể hiểu $0$ chỉ dành cho hòa. | Nêu $0$ cho hòa hoặc chưa kết thúc và $A_t\in\mathcal A(S_t)$. | Áp dụng. |
| nghiêm trọng | E01 | Kỳ vọng của hàm giá trị thiếu đại lượng cố định và nguồn ngẫu nhiên. | Viết “kết quả tích lũy kỳ vọng” không đủ xác định. | Điều kiện hóa trên lịch sử và gắn với $\pi$. | Áp dụng. |
| trung bình | F03 | Bảng số dễ bị hiểu là đủ để ra quyết định. | Thiếu phân phối, phương sai, số lượt còn lại và mục tiêu rủi ro. | Ghi ví dụ giả định; liệt kê dữ kiện thiếu trong ghi chú. | Áp dụng. |
| trung bình | A04 | Ba xác suất 0,2; 0,5; 0,3 không có nguồn. | Hình có thể bị đọc như dữ liệu. | Dùng ký hiệu $p_1,p_2,p_3$ hoặc ghi minh họa. | Áp dụng bằng ký hiệu và điều kiện tổng bằng 1. |

### Tái rà soát toán học sau chỉnh sửa

- Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng` tại D00–D03, E01–E02, F03 và G00–G04.
- Bổ sung tại D03 nguồn ngẫu nhiên của kỳ vọng: chính sách và môi trường.
- G02 ghi rõ giá trị `9` trong nguồn được xem là lỗi đánh máy; ánh xạ $+1/0/-1$ là quy ước mô hình hóa từ góc nhìn tác tử.
- Sửa mô tả `tictactoe-board.svg` thành hai quân X, ba quân O; ghi rõ tác tử điều khiển X và đang đến lượt X.

## Vòng chỉnh sửa hợp nhất

- Đã đóng toàn bộ lỗi `chặn bàn giao` và `nghiêm trọng` trong ba báo cáo.
- Đã xử lý các lỗi `trung bình` về cỡ chữ, cây trò chơi, câu nối mô hình, dữ kiện còn thiếu và sơ đồ lĩnh vực.
- Giữ 42 trang và thứ tự tuyến chính. Không thêm kỹ thuật ngoài nguồn.
- Theo yêu cầu sau bàn giao, đã bỏ ba câu hướng dẫn trên mặt H00, H01 và H03; nội dung phụ lục và ghi chú nguồn được giữ nguyên.
- Dùng `no-ai-slop` để bỏ câu dẫn rỗng, khẳng định tuyệt đối và thuật ngữ xuất hiện sớm. Dùng Quill ở chế độ rà mạch, không tạo `quill.json`; mạch trạng thái/quan sát → dữ liệu thời gian → phần thưởng → chính sách/giá trị → Tic-tac-toe đã được đồng bộ trong outline và storyboard.

## Kiểm định tĩnh sau chỉnh sửa

- Cấu hình RevealJS kế thừa mẫu: `1280 × 720`, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true`, `hash: true`.
- Dùng thư viện cục bộ: RevealJS, KaTeX, Notes, Markdown và Highlight.
- Không sửa `lecture-style.css`, `lecture-template.html` hoặc `index.html`.
- Bộ phân tích HTML đọc được tệp; 42 `data-slide-id` là duy nhất, 42 trang đều có ghi chú và số thẻ `<section>` mở–đóng cân bằng.
- Storyboard có đúng một hàng cho mỗi mã trang; tập 42 mã khớp HTML.
- Cả 12 tệp SVG phân tích được dưới dạng XML, có `role="img"`, `title`, `desc`; nhãn cốt lõi dùng cỡ từ 30 px.
- Mọi đường dẫn ảnh, CSS và JavaScript cục bộ đều tồn tại. Không có ảnh raster hoặc tài nguyên cốt lõi qua mạng.
- Đã dựng bảng liên hệ 12 SVG để kiểm tra nhãn, chồng lấn và quan hệ hình; đã sửa `course-map.svg`, `tictactoe-search.svg` và `tictactoe-value.svg` sau lần xem đầu.
- Tự kiểm theo `no-ai-slop/eval.md`: giữ ý và thứ tự nguồn; không thêm số liệu; bỏ câu dẫn rỗng, khẳng định phô trương, câu hỏi tu từ và nhịp câu máy móc. Các câu hỏi có nhãn `Câu hỏi:` là nhiệm vụ đánh giá, không phải câu hỏi tu từ.

## Kiểm định cuối của điều phối viên

- `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`; thử cài vào `/tmp` cũng thất bại vì kho gói không truy cập được. Dùng `python3 -m http.server 8765` làm phương án cục bộ tương đương để kiểm tra đường dẫn.
- Các URL của bộ trang chiếu, chỉ mục và SVG mẫu đều trả HTTP 200 tại cổng 8765.
- Chromium headless đã chụp đủ 42 trang tại `1280 × 720` và `720 × 720`. Hai contact sheet được duyệt trực quan; không thấy tràn, chồng lấn, công thức lỗi, ảnh vỡ hoặc tương phản gây mất nội dung.
- Nhật ký máy chủ xác nhận RevealJS, CSS, plugin Notes/Highlight/Math, KaTeX, phông chữ và cả 12 SVG đều trả HTTP 200. Yêu cầu `favicon.ico` trả 404 nhưng không ảnh hưởng bộ trang chiếu.
- Kiểm tra tĩnh cuối: 42 mã duy nhất, 42 ghi chú, 52 cặp section cân bằng, 42 hàng storyboard khớp mã, 12 SVG hợp lệ và không có nhãn SVG dưới 30 px.
- `2627-1/index.html` đã liên kết tới bộ trang chiếu và ba tài liệu quy trình.
- Dự án Codex Slides `20260824091941-b-i-01-gi-i-thi-u-h-c-t-ng-c-ng-83wl` đã được mở và dùng ở bước tiếp nhận, dàn ý và hệ thiết kế. Bốn Design Files cuối đã được ghi bền vững và đọc lại thành công. Công cụ tải Design File mới trả HTTP 500, nên dùng các tệp có sẵn trong dự án để đồng bộ nội dung.
- Giới hạn Codex Slides: dự án chỉ cho tối đa 30 trang và môi trường hiện tại không có bề mặt Browser để kiểm tra trực quan 42 trang trong dự án. Vì vậy không tuyên bố phiên bản 30 trang của Codex Slides đồng nhất với RevealJS; kiểm định trực quan cuối được thực hiện trên chính RevealJS bằng Chromium.

## Nguồn chính

- PPTX nguồn, tháng 02/2026.
- David Silver, *Introduction to Reinforcement Learning*: https://www.davidsilver.uk/wp-content/uploads/2020/03/intro_RL.pdf
- Sutton & Barto (2018): https://incompleteideas.net/book/the-book-2nd.html
- Silver et al. (2016): https://doi.org/10.1038/nature16961
