# Nhật ký rà soát Bài 01: Giới thiệu Học tăng cường

## Trạng thái bài giảng

- Tệp nguồn: `RL-hk2-2025-2026/lecture1-introduction-to-RL.pptx`, 45 trang.
- Bản RevealJS: 42 trang, từ `P00` đến `Z00` theo storyboard.
- Dự án Codex Slides: `20260824091941-b-i-01-gi-i-thi-u-h-c-t-ng-c-ng-83wl`.
- Bản hiện tại đã qua kiểm định storyboard, năm rà soát độc lập, vòng chỉnh sửa hợp nhất và hai tái kiểm định sau sửa.
- Dàn ý do Codex Slides đề xuất có thêm nội dung ngoài nguồn. Các phần về quy trình quyết định Markov, phương trình Bellman, học sai phân thời gian, epsilon-greedy và thuật toán chuyên sâu đã bị loại để giữ đúng phạm vi.
- **Trạng thái hiện hành:** kiểm định RevealJS cục bộ hoàn tất; giới hạn `reloadserver` và in-editor Browser của Codex Slides được ghi ở mục kiểm định cuối.

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

### Phân tích nguồn 45 → 42

- Bốn trang hình tiến bộ gần đây (nguồn 10–13) gộp thành hai trang trường hợp B01–B02: nguồn chỉ có ảnh minh họa, không có luận điểm riêng.
- Các trang thông tin học phần (nguồn 31–35) chuyển thành phụ lục H00–H03 dưới Z00, không tính vào tuyến 150 phút.
- Trang cảm ơn (nguồn 45) thay bằng Z00 tài liệu đọc và tự kiểm tra.
- Các trang trắc nghiệm nguồn gộp vào ôn tập H04–H05; AGI (nguồn 14–15) chuyển thành thảo luận H06–H07.
- Kết quả: 42 trang, thứ tự ý chính của nguồn được giữ; không có khái niệm nguồn nào bị mất mà không có quyết định ghi trong outline.

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

## Báo cáo rà soát — vòng trước

Các báo cáo dưới đây được tác tử chỉ đọc bổ sung sau bản nháp đầu. Mỗi mục dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

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
| chặn bàn giao | G03 | Ba số giá trị là tùy ý và trạng thái không được vẽ. | Không thể kiểm chứng $-0,4$, $0,1$, $0,7$. | Dùng một thế cờ gốc, ba nước hợp lệ và phần tiếp diễn dưới cùng $\pi$. | Áp dụng; bỏ số tùy ý, tách thưởng $+1$ của nước thắng khỏi giá trị tương lai 0 ở trạng thái kết thúc. |
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

## Kiểm định chạy trước của điều phối viên (đã ghi lịch sử, không phải kiểm định cuối)

- `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`; thử cài vào `/tmp` cũng thất bại vì kho gói không truy cập được. Dùng `python3 -m http.server 8765` làm phương án cục bộ tương đương để kiểm tra đường dẫn.
- Các URL của bộ trang chiếu, chỉ mục và SVG mẫu đều trả HTTP 200 tại cổng 8765.
- Chromium headless đã chụp đủ 42 trang tại `1280 × 720` và `720 × 720`. Hai contact sheet được duyệt trực quan; không thấy tràn, chồng lấn, công thức lỗi, ảnh vỡ hoặc tương phản gây mất nội dung.
- Nhật ký máy chủ xác nhận RevealJS, CSS, plugin Notes/Highlight/Math, KaTeX, phông chữ và cả 12 SVG đều trả HTTP 200. Yêu cầu `favicon.ico` trả 404 nhưng không ảnh hưởng bộ trang chiếu.
- Kiểm tra tĩnh cuối: 42 mã duy nhất, 42 ghi chú, 49 section cân bằng (7 vỏ ngoài + 42 trang), 42 hàng storyboard khớp mã, 12 SVG hợp lệ và không có nhãn SVG dưới 30 px.
- `2627-1/index.html` liên kết duy nhất tới bộ trang chiếu của Bài 01; không liên kết ba tài liệu quy trình.
- Dự án Codex Slides `20260824091941-b-i-01-gi-i-thi-u-h-c-t-ng-c-ng-83wl` đã được mở và dùng ở bước tiếp nhận, dàn ý và hệ thiết kế. Bốn Design Files cuối đã được ghi bền vững và đọc lại thành công. Công cụ tải Design File mới trả HTTP 500, nên dùng các tệp có sẵn trong dự án để đồng bộ nội dung.
- Giới hạn Codex Slides: dự án chỉ cho tối đa 30 trang và môi trường hiện tại không có bề mặt Browser để kiểm tra trực quan 42 trang trong dự án. Vì vậy không tuyên bố phiên bản 30 trang của Codex Slides đồng nhất với RevealJS; kiểm định trực quan được thực hiện trên chính RevealJS bằng Chromium.

---

# Đợt rà 2026-08-30

## Metadata runtime

| Đối tượng | requested_model | observed_model | provider | Ghi chú phiên |
|---|---|---|---|---|
| Plan (điều phối) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Phiên hợp lệ. |
| Source (trích nguồn) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Phiên hợp lệ. |
| Storyboard (kiểm định) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Phiên hợp lệ. |
| Reviewer flow | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Lần 1 trả về phiên rỗng/không hợp lệ; chạy lại lần 2 hợp lệ, báo cáo `reviews/flow.md` dùng kết quả lần chạy lại. |
| Reviewer math | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Lần 1 trả về phiên rỗng/không hợp lệ; chạy lại lần 2 hợp lệ, báo cáo `reviews/math.md` dùng kết quả lần chạy lại. |
| Reviewer pedagogy | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Lần 1 trả về phiên rỗng/không hợp lệ; chạy lại lần 2 hợp lệ, báo cáo `reviews/pedagogy.md` dùng kết quả lần chạy lại. |
| Reviewer rl-expert | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Lần 1 trả về phiên rỗng/không hợp lệ; chạy lại lần 2 hợp lệ, báo cáo `reviews/rl-expert.md` dùng kết quả lần chạy lại. |
| Reviewer student | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Phiên đầu hợp lệ; báo cáo `reviews/student.md` dùng trực tiếp kết quả này. |

Phân biệt: reviewer student trả báo cáo hợp lệ ngay lần đầu. Bốn vai flow, math, pedagogy và rl-expert có lần gọi đầu không tạo báo cáo dùng được, rồi trả báo cáo đầy đủ ở lần chạy lại. Không có báo cáo nào được ghép từ hai phiên.

## Báo cáo kiểm định storyboard (đợt 2026-08-30)

Phạm vi: `planning/lec-01/outline.md`, `storyboard.md`, HTML hiện hành, nguồn 45 trang.

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| chặn bàn giao | Toàn bộ (cấu trúc `<section>` ngoài) | HTML có 10 section ngoài, vượt giới hạn 5–7 mà không có ngoại lệ ghi lý do. | 52 cặp section cân bằng = 42 trang + 10 vỏ ngoài; storyboard chỉ khai "sáu cụm P–G". | Gộp về 7 mạch: P+A+B, C, D, E, F, G, H+Z; ghi lý do vào storyboard và review-log. | Áp dụng. HTML hiện hành có đúng 7 section ngoài; outline và storyboard đã cập nhật bảng 7 mạch. |
| nghiêm trọng | B00–B02 | Mạch B lặp chức năng ví dụ của cụm 1, không tạo bước tiến lập luận riêng. | Storyboard cũ xếp B01–B02 vào cột Ví dụ/Kiểm tra của cụm 1; B00 chỉ mô tả hai miền. | Gộp B vào mạch mở đầu, định vị lại là "trường hợp ứng dụng dẫn nhập" với câu nối A04→B00→C00. | Áp dụng. Storyboard có cụm 1b riêng với vai trò dẫn nhập có chủ ý. |
| nghiêm trọng | E01, G03 | Ký hiệu $V^\pi$ định nghĩa trên lịch sử nhưng dùng trên trạng thái mà không có cầu nối. | E01: $V^\pi(h_t)=\mathbb E_\pi[G_t\mid H_t=h_t]$; G03 dùng $V^\pi(S_{t+1}^{(a)})$. | Thêm cầu nối $h_t\leftrightarrow(S_t,\text{lượt})$ vào bảng thuật ngữ, ghi chú E01 và điểm dùng G03. | Áp dụng. Outline dòng cầu nối và storyboard E01/G03 đã ghi cầu nối. |
| nghiêm trọng | G03 | Công thức chọn nước thiếu kỳ vọng trên đại lượng ngẫu nhiên. | $\arg\max$ trên $R_{t+1}^{(a)}+V^\pi(S_{t+1}^{(a)})$ hiện thực ngẫu nhiên. | Đưa kỳ vọng lên mặt chiếu: $\arg\max_a\mathbb E_\pi[R_{t+1}+V^\pi(S_{t+1})\mid S_t,A_t=a]$. | Áp dụng. G03 hiện dùng kỳ vọng có điều kiện; ký hiệu $R_{t+1}^{(a)}$ đã bỏ khỏi bản hiện hành. |
| nghiêm trọng | G02 | Quy ước thưởng $0$ gộp hai vai trò (bước thường và hòa). | G02 ghi "$0$ nếu hòa hoặc chưa kết thúc" không tách ý. | Tách hai ý: thưởng 0 ở mọi bước chưa kết thúc và thưởng kết thúc 0 khi hòa. | Áp dụng trong G02 và ghi chú. |
| trung bình | G04, H05 | G04 bước 3 trùng chức năng với H05 câu 1. | Cùng hỏi phân biệt chính sách với hàm giá trị. | G04 tập trung mô hình hóa trạng thái–hành động–thưởng; H05 giữ câu hỏi vai trò thành phần. | Áp dụng. Storyboard ghi rõ hai trang không trùng chức năng. |
| trung bình | G03–G04 | Hai trang bị ghi đồng thời vào cụm 4 và cụm 6, nguy cơ đếm trùng thời lượng. | Storyboard cũ: cụm 4 "Ứng dụng: E02, G03; Kiểm tra: E02, G04" và cụm 6 cũng chứa G03–G04. | Quy G03–G04 thuộc cụm 6; cụm 4 ghi "không áp dụng — dùng lại kết quả". | Áp dụng. |

### Phát hiện sai bị bác: "thiếu tài sản"

- Một reviewer trong đợt này báo phát hiện "thiếu tài sản" (thiếu SVG/tệp tài sản trong workspace).
- **Quyết định: bác.** Lý do: snapshot tạm thời mà reviewer đọc không chứa toàn workspace — chỉ gồm ba tệp `planning/lec-01/` và một phần kho, nên không thấy thư mục SVG và tài sản khác. Kiểm kê trực tiếp trên workspace đầy đủ xác nhận cả 12 tệp SVG tồn tại và mọi đường dẫn trong HTML đều trả HTTP 200 (xem kiểm định tĩnh và kiểm định chạy trước). Phát hiện là artefact của phạm vi đọc, không phải lỗi của bộ tài liệu.

## Năm báo cáo rà soát độc lập (đợt 2026-08-30)

Năm báo cáo đầy đủ nằm tại `reviews/flow.md`, `reviews/math.md`, `reviews/pedagogy.md`, `reviews/rl-expert.md`, `reviews/student.md`. Dưới đây là các mục chính trích từng báo cáo, giữ đủ bằng chứng.

### 1. Vai Kết nối và mạch viết (`reviews/flow.md`)

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| chặn bàn giao | Toàn bộ (section ngoài) | 10 section ngoài vượt khoảng 5–7, không có ngoại lệ ghi lý do. | 52 cặp section = 42 trang + 10 vỏ ngoài; AGENTS.md yêu cầu 5–7; storyboard chỉ khai sáu cụm. | Gộp về 5–7 mạch, ghi lý do vào storyboard và review-log, rà lại ranh giới các phần gộp. |
| nghiêm trọng | B00–B02 | Mạch B lặp chức năng ví dụ của cụm 1, không có luận điểm mới. | Storyboard xếp B01–B02 vào cột Ví dụ/Kiểm tra cụm 1; B00 chỉ mô tả hai miền; hai đầu nối A04→B00 và B00→C00 không dùng nội dung B. | Gộp B vào mạch A với câu nối tường minh, cập nhật storyboard và hai trang lân cận mỗi phía. |
| trung bình | A04 → B00 | Câu chuyển ý ở A04 hứa "Phần E sẽ phân biệt…" nhưng trang liền sau là B00. | Ghi chú A04 so với nội dung B00 mở đầu bằng AlphaGo/robot. | Thêm câu nối A04→B00 "hai miền dưới đây cho thấy quyết định phải học từ tương tác"; giữ lời hứa phần E ở dạng "về sau". |
| trung bình | F00 | F00 dùng Tic-tac-toe làm bối cảnh trước khi miền này được giới thiệu ở G00. | Ghi chú F00 nhắc Tic-tac-toe; G00 mới giới thiệu miền. | Thay bối cảnh trung lập hoặc thêm câu giới thiệu rằng Tic-tac-toe được dùng xuyên suốt từ E00. |
| trung bình | E01 → G03 | Ký hiệu $V^\pi(h_t)$ đổi thành $V^\pi(S_{t+1}^{(a)})$ không có câu nối. | Định nghĩa E01 trên lịch sử so với công thức G03 trên trạng thái. | Thêm câu nối "lịch sử $h_t$ rút gọn thành thế cờ và lượt" hoặc thống nhất ký hiệu theo $h_t$. |
| trung bình | Z00 | Kết luận không thu hồi tường minh trọng tâm P02. | P02 nêu trọng tâm; Z00 chỉ có tài liệu đọc và tự kiểm tra. | Thêm khối tóm lược ba–bốn dòng thu hồi trọng tâm và ba dấu hiệu nhận dạng. |
| trung bình | H04–H07 | Một mạch đảm nhiệm hai chức năng (ôn tập và thảo luận) không có tín hiệu chuyển khối. | H04–H05 là ôn tập, H06–H07 là thảo luận; H05→H06 không có câu nối. | Thêm câu chuyển ở H05/H06 hoặc tách ôn tập về sau G khi gộp mạch. |
| nhẹ | C00 | Tiêu đề mạch trùng chủ đề toàn bài, không báo hiệu chức năng. | "C. Học tăng cường" so với P00 cùng tên. | Đổi thành "Khung học và tín hiệu", đồng bộ outline và storyboard. |
| nhẹ | Z00, H00–H03 | Mạch kết dùng chung vỏ ngoài với phụ lục, ranh giới chỉ báo bằng chữ nhỏ. | Một section ngoài chứa Z00 và bốn trang phụ lục. | Tách mạch kết và mạch phụ lục hoặc tăng cường tín hiệu chuyển và ghi rõ trong storyboard. |
| nhẹ | P01 | Ghi chú hứa "thảo luận hai tình huống chuyển giao" nhưng từ khóa không thu hồi ở H06–H07. | Ghi chú P01 so với nội dung H06–H07. | Thống nhất từ khóa ở H06–H07 hoặc sửa ghi chú P01 thành "hai thảo luận mở rộng". |

### 2. Vai Độ chính xác toán học và thuật toán (`reviews/math.md`)

Tự kiểm đã xác nhận đúng: $G_0=R_1+R_2+R_3+R_4=0+0+0+1=1$ với $T=4$; chỉ số $S_0..S_4$, $A_0..A_3$, $R_1..R_4$ khớp hình; bàn cờ gốc khớp giữa ba SVG; nước $a=9$ tạo đường chéo 1–5–9; $p_1+p_2+p_3=1$; 42 `data-slide-id` khớp storyboard.

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| trung bình | G03 | $\arg\max$ theo $V^\pi$ là tham lam một bước, không phải hành động tối ưu vì $V^\pi\neq V^*$. | Công thức argmax kèm ghi chú không phát biểu tính không tối ưu. | Thêm câu nêu rõ: tham lam theo $V^\pi$ chỉ tối ưu khi $V^\pi=V^*$. |
| trung bình | G03 (đối chiếu E01, G00) | Nguồn ngẫu nhiên của kỳ vọng tại $S_{t+1}$ (đến lượt đối thủ) chưa nêu trên quan hệ công thức. | Định nghĩa trên $h_t$ ở E01 so với $S_{t+1}^{(a)}$ ở G03; giả thiết đối thủ nằm ở G00. | Nêu rõ kỳ vọng lấy theo cả $\pi$ và phân phối đều của đối thủ, hoặc dùng $V^\pi(h_{t+1})$. |
| nhẹ | E01 | $\mathbb E_\pi$ dễ bị đọc là kỳ vọng chỉ theo chính sách. | Công thức dùng $\mathbb E_\pi$; nguồn ngẫu nhiên môi trường chỉ nằm ở ghi chú. | Thêm chú thích dưới công thức hoặc dùng $\mathbb E_{\pi,M}$ kèm giải thích. |
| nhẹ | G04 | Câu hỏi không cho biết thế cờ đầy đủ và lượt ai, nên đáp án $\{2,6,8\}$ không kiểm chứng được. | Đề bài và đáp án không mô tả vị trí X/O và lượt chơi. | Bổ sung mô tả thế cờ cụ thể vào đề bài hoặc ghi chú. |
| nhẹ | E01, G02 | $\pi(a\mid h_t)$ và $A_t\in\mathcal A(S_t)$ gặp nhau mà không có cầu nối tại điểm dùng. | Cầu nối rút gọn lịch sử chỉ nằm trong ghi chú E01; G02 không tham chiếu. | Thêm câu nối ở G02: $h_t$ được thay bằng $(S_t,\text{lượt})$. |
| nhẹ | D02 | Công thức $G_t=\sum_{k=t+1}^{T}R_k$ tổng quát nhưng chỉ có ví dụ $G_0$. | Chỉ có $G_0=1$; hình đủ dữ kiện cho $G_3=R_4=1$. | Thêm ví dụ $G_t$ với $t>0$ vào ghi chú D02. |

### 3. Vai Phản biện học thuật và giảng dạy (`reviews/pedagogy.md`)

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | G03 | Dùng ký hiệu chưa định nghĩa ($V^\pi(S_{t+1}^{(a)})$, $R_{t+1}^{(a)}$), đứt cầu nối với E01. | E01 định nghĩa trên lịch sử; $R_{t+1}^{(a)}$ không xuất hiện ở D00–D03 hay G02. | Thêm dòng cầu nối trên mặt G03 hoặc thống nhất ký hiệu $V^\pi(h_{t+1})$. |
| nghiêm trọng | E00–E02 | Tic-tac-toe được dùng làm ví dụ trước khi luật và quy ước thưởng được hình thức hóa ở G02. | E00 nói "một thế cờ" chung chung; G02 mới chốt $\mathcal A(S_t)$ và tập thưởng. | Thêm câu giới thiệu luật tối thiểu ở E00 hoặc dẫn rõ "ví dụ đầy đủ ở phần G". |
| trung bình | G03 | Chính sách $\pi$ trong $V^\pi$ chưa được chỉ định cho Tic-tac-toe. | G00 chỉ định phân phối đối thủ, không chỉ định $\pi$ của tác tử. | Nêu $\pi$ là chính sách hiện tại của tác tử và đây là đánh giá dưới chính sách cố định. |
| trung bình | D02 | Giá trị $R_1,\ldots,R_4$ không có chỗ neo hiển thị trên hình. | Alt D00 không nêu giá trị; số liệu xuất hiện đột ngột ở D02. | Ghi giá trị thưởng trên SVG D00 hoặc lặp chuỗi thưởng ở đầu D02. |
| trung bình | E01 | Ký hiệu kỳ vọng có điều kiện là bước nhảy tiên quyết; xác suất chỉ nằm ở phụ lục H03. | Không có trang chuẩn bị nào trên tuyến chính trước E01. | Thêm dòng chuẩn bị ở E01 hoặc ghi chú nhắc định nghĩa kỳ vọng. |
| trung bình | Cụm 4 và cụm 6 | G03–G04 bị ghi vào hai cụm cùng lúc, nguy cơ đếm trùng thời lượng. | Storyboard hai hàng cụm cùng chứa G03–G04. | Quy G03–G04 thuộc một cụm, cụm còn lại ghi "không áp dụng". |
| trung bình | C01 | "Phần thưởng tích lũy kỳ vọng" dùng trước khi phần thưởng và kỳ vọng được định nghĩa. | Định nghĩa $R_{t+1}$, $G_t$ chỉ có ở D01–D02. | Dùng diễn đạt phi hình thức ở C01 hoặc thêm ghi chú "sẽ định nghĩa ở phần D". |
| nhẹ | B01 | Cầu nối dùng "đánh giá" trước khi hàm giá trị được định nghĩa; chỉ nằm trong ghi chú. | Mặt trang B01 so với định nghĩa E01. | Thêm cụm từ trên mặt trang báo đây là xem trước có chủ ý. |
| nhẹ | F03 | Ví dụ bảng hai hành động tách khỏi ví dụ Tic-tac-toe đang chạy. | Bảng A/B so với các trang dùng Tic-tac-toe. | Thêm câu nối hoặc ghi lý do chọn ví dụ ngoài miền chính trong storyboard. |
| nhẹ | G04 | Bước 3 trùng chức năng với H05 câu 1. | Cùng hỏi phân biệt chính sách với hàm giá trị. | Thay bước 3 bằng yêu cầu áp dụng, ví dụ chỉ ra $V^\pi$ đánh giá thế cờ nào sau nước 5. |

### 4. Vai Chuyên gia Học tăng cường (`reviews/rl-expert.md`)

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | G03 | $\arg\max$ trên đại lượng ngẫu nhiên, thiếu kỳ vọng. | Với đối thủ "chọn đều", $R_{t+1}^{(a)}$ và $S_{t+1}^{(a)}$ là ngẫu nhiên. | Viết $\arg\max_a\mathbb E[R_{t+1}+V^\pi(S_{t+1})\mid S_t,A_t=a]$ hoặc đưa kỳ vọng lên mặt chiếu. |
| trung bình | E01 so với G03 | Ký hiệu hàm giá trị không nhất quán: định nghĩa trên lịch sử, áp dụng trên trạng thái. | $V^\pi(h_t)$ ở E01 so với $V^\pi(S_{t+1}^{(a)})$ ở G03. | Viết $V^\pi(h_{t+1}^{(a)})$ hoặc thêm câu nối rút gọn lịch sử. |
| trung bình | Cụm 1 và cụm 4 | 34 phút cho định hướng, chỉ 14 phút cho ba khái niệm trung tâm. | Outline: cụm 1 = 34 phút, cụm 4 = 14 phút. | Rút cụm 1 xuống 28–30 phút, tăng cụm 4 lên 18–20 phút. |
| trung bình | B00–B02 | Ví dụ nguồn trang 22 (lái xe, trợ lý mã) bị bỏ không có quyết định ghi. | Nguồn trang 22 liệt kê bốn ví dụ; HTML chỉ còn AlphaGo, robot, robot đa nhiệm. | Bổ sung dòng liệt kê miền ứng dụng vào B00 hoặc ghi quyết định bỏ kèm lý do. |
| trung bình | F00–F02 | Thăm dò–khai thác chưa nối với chính sách $\pi$ vừa định nghĩa. | F01–F02 chỉ mô tả bằng lời, không liên hệ $\pi(a\mid h_t)$ hay $\arg\max$. | Thêm câu nối: khai thác tương ứng $\arg\max$ giá trị ước lượng, thăm dò tương ứng $\pi$ đặt xác suất khác không. |
| nhẹ | C01, C05 | Thuật ngữ "i.i.d." của nguồn không được đưa vào. | Nguồn trang 21 ghi "Non i.i.d data"; C01 chỉ diễn đạt bằng lời. | Thêm một lần "dữ liệu không i.i.d. (độc lập cùng phân phối)". |
| nhẹ | C01 | Trật tự từ "phần thưởng tích lũy kỳ vọng" dễ đọc sai. | C01 so với định nghĩa đúng $\mathbb E_\pi[G_t\mid H_t=h_t]$. | Đổi thành "kỳ vọng của tổng phần thưởng tích lũy" hoặc $\mathbb E[G_t]$. |
| nhẹ | C00 | Mốc lịch sử Bellman thập niên 1950 bị lược không có quyết định ghi. | Nguồn trang 17; HTML không còn mốc. | Thêm một câu ngắn hoặc ghi quyết định bỏ vào review-log. |
| nhẹ | F03 | Ví dụ hai hành động thực chất là bandit nhưng không gọi tên. | Bảng A/B kèm ghi chú chỉ nói "ví dụ giả định". | Thêm câu ghi chú về bài toán bandit. |
| nhẹ | G02 | Giá trị 0 gộp hai vai trò: thưởng bước thường và thưởng kết thúc hòa. | G02: "$0$ nếu hòa hoặc chưa kết thúc". | Tách hai ý trong G02 hoặc ghi chú. |

### 5. Vai Góc nhìn sinh viên (`reviews/student.md`)

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | Toàn bộ (section ngoài) | 10 section ngoài làm nhịp giảng bị ngắt trung bình mỗi 15 phút; cụm B chỉ 3 trang. | Các thẻ ngoài tại 10 vị trí HTML; review-log đếm 52 cặp section; AGENTS.md yêu cầu 5–7. | Gộp về 5–7 mạch hoặc ghi ngoại lệ kèm lý do. |
| trung bình | Cụm 1 đối trọng cụm 4 | 34 phút (~28%) cho định hướng 11 trang; cụm hình thức dày nhất chỉ 14 phút với hai công thức mới liên tiếp. | Outline phân bổ 34/22/18/14/14/18; E01 chứa hai công thức trong một trang. | Rút B00–B02 xuống 6–8 phút, chuyển 4–6 phút cho E00–E02. |
| trung bình | P00–P02 (và H03) | Tiên quyết chỉ nằm ở phụ lục H03; tuyến chính không báo nền giả định trong khi E01 dùng kỳ vọng ngay. | Nguồn trang 37 ánh xạ vào H03; P00–P02 không nêu nền. | Thêm một dòng nền giả định ở P01 hoặc P02 kèm ghi chú phụ lục. |
| trung bình | G00, G01, G03 | Bất đồng bộ số nhánh: G00 nêu 4 ô trống nhưng cây và hình đánh giá chỉ vẽ 3 nước. | G00: ô 3, 6, 7, 9; G01/G03: nước 3, 7, 9. | Thêm nhãn "ba trong bốn nước hợp lệ" hoặc vẽ đủ nhánh nước 6 kèm "…". |
| nhẹ | D00 | Alt text đọc số kiểu "S không" dễ hiểu thành phủ định. | Alt: "Quỹ đạo từ S không đến S bốn…". | Viết "S0, S1, …, S4" và "R1 đến R4". |
| nhẹ | C03 | Câu hỏi kiểm tra nén quá mức, thiếu bối cảnh ai chấm cái gì. | "chấm điểm một đáp án đúng đã biết thuộc dạng phản hồi nào?". | Viết lại có bối cảnh, giữ đáp án trong ghi chú. |
| nhẹ | G03 | Ký hiệu chỉ số $(a)$ xuất hiện lần đầu không có chú giải trên mặt chiếu. | Giải thích chỉ nằm trong `<aside class="notes">`. | Thêm chú thích ngắn dưới công thức. |
| nhẹ | Z00 | Ghi chú dẫn URL nằm trong tệp quy trình nội bộ, không phải tài liệu sinh viên. | HTML Z00 ghi "URL đầy đủ nằm trong outline và review-log". | Đưa URL đầy đủ vào ghi chú diễn giả Z00. |
| nhẹ | B02 → C00 | Câu nối từ hai trường hợp sang khung học chỉ tồn tại trong ghi chú. | B02 kết bằng câu hỏi; C00 mở bằng sơ đồ không nhắc lại hai ca. | Thêm mệnh đề nối ở box C00 hoặc ghi chú C00. |

Giới hạn chưa kiểm chứng của reviewer sinh viên (đã đóng sau bằng kiểm định tĩnh và chạy trước): `lecture-style.css`, 12 SVG, `vendor/katex`, `theme/white.css`, kiểm tra trực quan trình duyệt.

## Xử lý lỗi chặn/nghiêm trọng sau đợt 2026-08-30

| Phát hiện | Xử lý |
|---|---|
| 10 → 7 section ngoài | Đã gộp về 7 mạch ngoài: P+A+B, C, D, E, F, G, H+Z. Outline và storyboard cập nhật bảng 7 mạch; HTML hiện hành có đúng 7 section ngoài. |
| B00–B02 | Định vị lại thành "trường hợp ứng dụng dẫn nhập" (cụm 1b) trong mạch mở đầu, với câu nối A04→B00→C00 tường minh; không đổi thứ tự trang. |
| Cầu nối $h_t\to(S_t,\text{lượt})$ | Đã đưa vào bảng thuật ngữ outline và ghi chú E01/G03: trong Tic-tac-toe quan sát đầy đủ, lịch sử $h_t$ rút gọn thành cặp (thế cờ $S_t$, lượt chơi); ký hiệu $V^\pi$ ở G03 là cùng một định nghĩa E01. |
| Kỳ vọng G03 | Công thức G03 viết lại với kỳ vọng tường minh: $a^*\in\arg\max_{a\in\mathcal A(S_t)}\mathbb E_\pi[R_{t+1}+V^\pi(S_{t+1})\mid S_t,A_t=a]$; ký hiệu $R_{t+1}^{(a)}$ bỏ khỏi bản hiện hành. |
| Thưởng 0 | G02 tách hai vai trò của 0: thưởng 0 ở mọi bước chưa kết thúc (mặc định) và thưởng kết thúc 0 khi hòa; khớp cách tính $G_0=0+0+0+1$ ở D02. |
| G04/H05 | G04 tập trung mô hình hóa trạng thái–hành động–thưởng (ô 5 không hợp lệ); H05 giữ câu hỏi vai trò thành phần ở mức khái niệm; hai trang không trùng chức năng. |

## Đề xuất không áp dụng và lý do

| Đề xuất | Nguồn | Lý do không áp dụng |
|---|---|---|
| Thêm fragment đáp án từng bước | Góc nhìn sinh viên (vòng trước) | Bản nguồn không dùng hiệu ứng; đáp án trong ghi chú giữ mặt chiếu ổn định và không đổi nhịp bàn phím. |
| Rút cụm 1 xuống 28–30 phút, tăng cụm 4 lên 18–20 phút | Chuyên gia Học tăng cường | Áp dụng: mạch 1 giảm từ 34 xuống 30 phút; mạch 4 tăng từ 14 lên 18 phút. Tổng sáu mạch chính vẫn là 120 phút. |
| Bổ sung ví dụ lái xe và trợ lý mã vào B00 | Chuyên gia Học tăng cường | Quyết định ánh xạ nguồn đã ghi "phân bổ vào trò chơi, thao tác robot và thảo luận"; thêm hai miền nữa làm quá tải trang dẫn nhập, trái nguyên tắc giữ đúng hai miền ở trang nguồn 11–13. |
| Thêm mốc Bellman vào C00 | Chuyên gia Học tăng cường | Có thể áp dụng như một câu ghi chú; không đưa lên mặt chiếu để giữ C00 tập trung vào tín hiệu học. Đã ghi quyết định tại đây. |
| Đổi tiêu đề C00 thành "Khung học và tín hiệu" | Kết nối và mạch viết | Áp dụng; tiêu đề phân biệt chức năng của mạch C với tiêu đề toàn bài. |
| Đưa URL đầy đủ vào ghi chú Z00 | Góc nhìn sinh viên | Áp dụng trong ghi chú diễn giả để người dạy truy cập được tài liệu mà không mở tệp planning. |

## Phạm vi phải rà lại toàn mạch và hai trang lân cận

Việc gộp 10 → 7 section ngoài làm đổi ranh giới tại ba điểm. Sau mỗi lần chỉnh sửa ảnh hưởng cấu trúc section, phải rà lại toàn bộ mạch và hai trang lân cận tại:

- **P02/A00**: ranh giới mạch mở đầu nội bộ (P → A), câu nối bản đồ sang tác tử học.
- **A04/B00**: ranh giới từ giới hạn mô hình cố định sang trường hợp ứng dụng dẫn nhập, câu nối "hai miền đòi hỏi học từ tương tác".
- **H07/Z00**: ranh giới mạch kết, câu nối thảo luận sang tài liệu đọc và tự kiểm tra, khâu thu hồi trọng tâm P02.

## Tái kiểm định sau chỉnh sửa hợp nhất — 2026-08-30

Hai reviewer chỉ đọc chạy độc lập bằng hồ sơ `recheck`: 10 vòng tối đa, timeout tuyệt đối 120 giây mỗi request, tối đa 4.000 token đầu ra, nhiệt độ 0,1 và reasoning effort `low`. Cả hai kết quả có `requested_model = observed_model = z-ai/glm-5.3-flash`, `provider = OpenRouter`.

### Độ chính xác toán học và thuật toán

Reviewer kết luận không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng` trong D02, E01 và G02–G04.

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | G03 | Nguồn ngẫu nhiên của kỳ vọng chỉ có trong ghi chú. | Mặt trang dùng $\mathbb E_\pi$; đối thủ chọn đều được nêu ở G00. | Nêu kỳ vọng theo $\pi$ và đối thủ trên mặt trang. | Áp dụng bằng dòng chú thích dưới công thức. |
| nhẹ | G03 | Cầu nối $h_t\leftrightarrow(S_t,\text{lượt})$ chưa có trên mặt trang. | E01 định nghĩa $V^\pi(h_t)$, G03 dùng $V^\pi(S_{t+1})$. | Đưa cầu nối lên mặt G03. | Áp dụng cùng dòng chú thích. |
| nhẹ | G04 | Đề bài chưa nêu lượt chơi. | Bài chỉ cho tập ô trống, trong khi bước áp dụng hàm giá trị cần quy ước lượt. | Nêu rõ đến lượt X. | Áp dụng trên đề bài G04. |
| nhẹ | G02 | Quan hệ giữa chính sách trên lịch sử và hành động trên trạng thái chỉ khép ở G03. | G02 dùng $S_t$; E01 dùng $h_t$. | Nhắc cầu nối trong ghi chú G02. | Áp dụng. |

### Kết nối và mạch viết

Reviewer xác nhận đúng 7 mạch ngoài, đủ mạch mở đầu và kết luận; 42 mã trang khớp storyboard; tổng thời lượng là 120 + 30 phút. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nhẹ | P02→A00 | Tín hiệu chuyển từ bản đồ sang tác tử học chỉ có trong ghi chú. | Vai trò trong mạch: P02 định hướng; kết nối vào P01; kết nối ra A00. | Báo điểm bắt đầu trên mặt P02. | Áp dụng. |
| nhẹ | B02→C00 | B02 chưa báo bước chuyển sang tín hiệu học. | Vai trò trong mạch: B02 khép dẫn nhập; kết nối vào B01; kết nối ra C00. | Thêm một dòng chuyển ngắn cuối B02. | Áp dụng. |
| trung bình | H05→H06 | Mạch 7 đổi từ ôn tập sang thảo luận nhưng chưa có câu chuyển khối. | Vai trò trong mạch: H05 khép ôn tập; kết nối vào H04; kết nối ra H06 mở thảo luận. | Thêm câu chuyển ở đầu H06. | Áp dụng. |
| nhẹ | H07→Z00 | Kết luận chưa thu hồi đủ ba dấu hiệu nhận dạng. | Vai trò trong mạch: H07 khép thảo luận; kết nối vào H06; kết nối ra Z00 và phụ lục H00. | Thêm tương tác, phụ thuộc thời gian và phản hồi trễ ở Z00. | Áp dụng. |

Sau các sửa cục bộ này, thứ tự, số trang và ranh giới section không đổi. Phạm vi P01–A01, A03–B01, B01–C01, H04–H07 và H06–H00 đã được đối chiếu lại.

## Tiêu chí tự kiểm

- `no-ai-slop`: giữ ý và thứ tự nguồn; không thêm số liệu ngoài nguồn; bỏ câu dẫn rỗng, khẳng định phô trương, câu hỏi tu từ và nhịp câu máy móc. Các câu hỏi có nhãn `Câu hỏi:` là nhiệm vụ đánh giá.
- Quill: dùng ở chế độ rà mạch; mạch trạng thái/quan sát → dữ liệu thời gian → phần thưởng → chính sách/giá trị → Tic-tac-toe giữ liên tục. **Không tạo `quill.json`.**
- Mọi công thức Markdown dùng $...$.

## Kiểm định cuối của điều phối viên

- Cấu trúc tĩnh: 7 section ngoài; 42 trang và 42 `data-slide-id` duy nhất; 42 hàng storyboard theo đúng thứ tự; 42 ghi chú diễn giả; thẻ section cân bằng.
- Tài sản: mọi CSS, JavaScript và 12 SVG cục bộ đều tồn tại; không có tham chiếu raster hoặc tài nguyên lõi từ mạng; `git diff --check` không báo lỗi.
- `no-ai-slop`: không phát hiện tiêu đề tu từ, lời quảng bá, câu cảm thán, nhịp dẫn rỗng hoặc khẳng định quá mức trong nội dung hiển thị và ghi chú. Quill được dùng để rà liên tục thuật ngữ và tuyến tác tử/quan sát → tín hiệu theo thời gian → phần thưởng → chính sách/giá trị → ứng dụng; không tạo `quill.json`.
- Lệnh bắt buộc `python3 -m reloadserver 8765` đã chạy nhưng môi trường thiếu mô-đun `reloadserver`. Điều phối viên dùng `python3 -m http.server 8765` làm máy chủ thay thế tại URL cục bộ.
- Chromium headless đã duyệt đủ 42 trang ở 1280×720 và 800×600. Cả hai lượt có 0 lỗi console, 0 tài nguyên hỏng và 0 trang bị công cụ phát hiện tràn. Ảnh liên hệ và các trang trọng điểm G03, H06, Z00 được xem trực tiếp.
- Lượt ảnh đầu phát hiện dòng chú thích G03 bị chân trang che ở 1280×720 dù phép đo DOM không báo tràn. Đã giảm riêng hình G03 xuống lớp `figure small`; lượt chụp lại đủ 42 trang ở cả hai kích thước không còn lỗi này.
- Bàn phím: kiểm tra P00 → ArrowDown → P01 → ArrowUp → P00 → ArrowRight → C00 thành công.
- `2627-1/index.html` có một liên kết đến `lecture-01-gioi-thieu-hoc-tang-cuong.html` và không liên kết tệp planning của bài.
- Codex Slides CLI trả danh sách capability thành công, nhưng phiên Codex này không cung cấp in-editor Browser để điều hướng URL handoff. Vì vậy chưa có xác minh hiển thị bằng Codex Slides; đây là giới hạn công cụ còn lại, không được ghi nhận như một kiểm tra đã hoàn tất.

Trạng thái: đủ điều kiện kiểm định RevealJS cục bộ; không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`. Hai giới hạn được giữ rõ: thiếu `reloadserver` và chưa có in-editor Browser cho Codex Slides.

## Nguồn chính

- PPTX nguồn, tháng 02/2026.
- David Silver, *Introduction to Reinforcement Learning*: https://www.davidsilver.uk/wp-content/uploads/2020/03/intro_RL.pdf
- Sutton & Barto (2018): https://incompleteideas.net/book/the-book-2nd.html
- Silver et al. (2016): https://doi.org/10.1038/nature16961
