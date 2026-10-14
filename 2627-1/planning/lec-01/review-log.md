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

## Giai đoạn I — Lecture note (02/09/2026)

### Phạm vi và sai khác so với quy trình deck cũ

- Đầu ra mới: `2627-1/materials/lec-01/lecture-note.md` và liên kết tĩnh qua
  `material-viewer.html`.
- Bản đồ chủ đề có 6 mục `cốt lõi`, 1 mục `cầu nối`, 3 mục `bổ sung` và nhóm
  `đọc thêm`. Tuyến cốt lõi giữ thứ tự nguồn: tác tử học → tín hiệu → phần
  thưởng → chính sách/giá trị/mô hình → thăm dò–khai thác → Tic-tac-toe.
- Nhóm tài nguyên hai liên kết trong `index.html` thay quy tắc một liên kết duy
  nhất của `AGENTS.md` theo yêu cầu cụ thể trong `prompt_lecture_note_deck.md`.
- Không dùng thông tin học phần trang 31–37 vì chưa xác nhận cho học kỳ đích.
  Không có code demo trong nguồn nên không tạo code hoặc notebook.
- Sửa lỗi nguồn ở trang 29–30: bỏ giá trị thưởng `9`, dùng miền thắng/hòa/thua
  $\{+1,0,-1\}$; tập hành động chỉ gồm ô trống hợp lệ. Sai khác được giải thích
  ngay trong note và ánh xạ sang `G02`–`G04`.

### Reader, hợp nhất và writer

| Vai trò | Profile | requested_model | observed_model | provider | Kết quả |
|---|---|---|---|---|---|
| Lập kế hoạch | `plan` | `deepseek/deepseek-v3.2` | `deepseek/deepseek-v3.2` | OpenRouter | Hoàn tất vòng 11 với trần 12; một phản hồi HTTP 200 rỗng được thử lại. |
| Phân tích nguồn | `source` | `deepseek/deepseek-v3.2` | `deepseek/deepseek-v3.2` | OpenRouter | Hoàn tất vòng 9 với trần 20; ánh xạ đủ 45 trang. |
| Hợp nhất phạm vi lần 1 | `recheck` | `deepseek/deepseek-v3.2` | `deepseek/deepseek-v3.2` | OpenRouter | Hoàn tất vòng 7; thiếu trường đầu vào/đầu ra cho từng mục nên chưa duyệt. |
| Hợp nhất phạm vi lần 2 | `recheck` | `deepseek/deepseek-v3.2` | `deepseek/deepseek-v3.2` | OpenRouter | Hoàn tất vòng 5; đủ trường và kết luận PASS. |
| Soạn note | `write` | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter | Hoàn tất vòng 9; một `finish_reason=error` được thử lại trước khi ghi. |
| Sửa sau review | `write` | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter | Sửa tuần tự note; lượt sửa sót riêng hoàn tất vòng 4. |

Các lượt trong sandbox trước đó trả `api_transport_error`; các lượt hợp lệ
đều chạy lại với quyền mạng nâng cao và cùng model đã chỉ định. Writer dùng
repo-root hẹp; cầu nối nạp khóa qua liên kết `.env` tạm, MCP chặn worker đọc
`.env`, và liên kết được gỡ ngay sau mỗi lượt.

### Năm báo cáo độc lập

#### Góc nhìn sinh viên

| mức độ | vị trí | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | `lec-01-topic-06` | Ô 9 vừa được gọi là đã có quân vừa được gọi là ô trống tạo thắng. | Đoạn ví dụ dùng cùng một thế cờ nhưng hai dữ kiện trái nhau. | Dùng thế cờ trống `3,7,9`; chọn ô 5 đã có quân làm hành động không hợp lệ. | Áp dụng. |
| trung bình | G03/G04 | Hai trang deck dùng hai thế cờ khác nhau mà chưa báo chuyển ví dụ. | G03 dùng `3,7,9`; G04 dùng `2,6,8`. | Đồng bộ hoặc nêu rõ hai thế cờ. | Chuyển sang Giai đoạn II; note đã ghi “bàn cờ khác ví dụ trên”. |
| nhẹ | các mục Kiểm tra | Đáp án hiển thị ngay sau câu hỏi. | Sáu chủ đề đều có “Trả lời” trong prose. | Đưa đáp án vào `::: solution`. | Áp dụng cho cả sáu chủ đề. |
| nhẹ | cầu nối và bổ sung | Chưa có `note-topic-id` riêng. | Bản đầu chỉ có sáu mã cốt lõi. | Thêm mã duy nhất cho mọi chủ đề nội dung. | Áp dụng; hiện có 10 mã. |

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider
OpenRouter, profile `review`, hoàn tất vòng 5.

#### Chuyên gia Học tăng cường

| mức độ | vị trí | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | `lec-01-topic-06` | Cách sửa lỗi thưởng nguồn cần truy nguyên rõ. | Nguồn có `9`; note dùng $\{+1,0,-1\}$. | Nêu lỗi và quy ước thay thế. | Đã có trong “Ứng dụng và giới hạn”; không lặp ở “Hình thức”. |
| nhẹ | `lec-01-topic-05` | Ví dụ số thăm dò không có trong nguồn. | Bảng A/B là dữ kiện do note đặt để tính tay. | Gắn nhãn giả định hoặc bỏ số. | Giữ và ghi rõ “không phải số liệu từ nguồn”. |
| nhẹ | thảo luận AGI | Cần phân biệt quan điểm nguồn với kết luận của bài. | Trang 14–15, 43–44 thiếu bằng chứng. | Ghi là quan điểm chưa được kiểm chứng. | Áp dụng. |

Lượt đầu lỗi `model exceeded the tool-call limit (10)` và không được tính.
Lượt chạy lại độc lập có
`requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter,
profile `review`, hoàn tất vòng 6.

#### Độ chính xác toán học và thuật toán

Reviewer ban đầu không báo lỗi bắt buộc và bỏ sót mâu thuẫn ô 9; điều phối
viên không dùng kết luận này để bác bằng chứng trực tiếp từ hai vai khác.
Reviewer xác nhận $G_0=G_1=G_3=1$, ví dụ giá trị bằng 0 và bảng A/B được tính
đúng. Runtime:
`requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter,
profile `review`, hoàn tất vòng 9.

#### Phản biện học thuật và giảng dạy

| mức độ | vị trí | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | `lec-01-topic-06` | Công thức chọn một bước xuất hiện thiếu cầu nối từ định nghĩa giá trị. | $V^\pi$ được định nghĩa ở topic-04; biểu thức $R_{t+1}+V^\pi(S_{t+1})$ xuất hiện ở topic-06. | Nối bằng $G_t=R_{t+1}+G_{t+1}$ và nêu giả thiết riêng của Tic-tac-toe. | Áp dụng; không gọi đây là Bellman tổng quát cho phần trước. |
| trung bình | `lec-01-topic-03` | Ví dụ $T=4$ chưa nối sang ký hiệu $T$ tổng quát. | Công thức tổng xuất hiện ngay sau ví dụ. | Thêm một câu khái quát hóa. | Áp dụng ở cuối ví dụ. |
| nhẹ | `lec-01-topic-04` | Ví dụ chính sách đều có thể bị hiểu là mặc định. | Dữ kiện ba kết quả bằng nhau là giả định. | Gắn nhãn ví dụ giả định. | Áp dụng. |

Runtime: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider
OpenRouter, profile `review`, hoàn tất vòng 11.

#### Kết nối và mạch viết

| mức độ | vị trí | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | `lec-01-topic-06` | Chuỗi ví dụ đứt vì hai thế cờ bị trộn. | Vai trò trong mạch: ví dụ tổng hợp; kết nối vào từ cầu nối trạng thái; kết nối ra công thức và kiểm tra. | Dùng một thế cờ hoặc tách rõ hai tình huống. | Áp dụng. |
| trung bình | G03/G04 | Deck đổi thế cờ không có câu nối. | Vai trò G03 là tổng hợp; vào từ G02, ra G04. | Đồng bộ hoặc báo chuyển. | Ghi cho Giai đoạn II. |
| nhẹ | các bổ sung/cầu nối | Thứ bậc nhấn cần rõ sau khi tách heading. | Các phần phụ phải phục vụ tuyến cốt lõi. | Rà toàn bộ sau sửa. | Recheck toàn bộ note đã PASS. |

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider
OpenRouter, profile `review`, hoàn tất vòng 7.

### Sửa và tái kiểm

- Sửa ví dụ Tic-tac-toe thành thế cờ trống `3,7,9`; ô 5 đã có quân là hành
  động không hợp lệ; bài kiểm tra dùng một thế cờ khác trống `2,6,8`.
- Thêm quy ước $V^\pi(S_T)=0$; thêm cầu nối
  $G_t=R_{t+1}+G_{t+1}$ trước công thức chọn một bước; nêu trạng thái gồm bàn
  cờ và lượt chơi là đủ thông tin trong miền này.
- Gắn nhãn hai ví dụ số là giả định; gập sáu đáp án; bỏ câu hỏi tu từ; thêm
  bốn mã cho cầu nối và bổ sung.
- Recheck toán học: `requested_model=observed_model=deepseek/deepseek-v3.2`,
  provider OpenRouter, profile `recheck`, hoàn tất vòng 6, kết luận PASS và
  tính lại các ví dụ.
- Recheck mạch viết: `requested_model=observed_model=z-ai/glm-5.3-flash`,
  provider OpenRouter, profile `recheck`, hoàn tất vòng 2, kết luận PASS cho
  toàn bộ tuyến và 10 `note-topic-id`.

Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng` của Giai đoạn I. Các góp ý
chỉ liên quan deck được giữ cho Giai đoạn II; chưa sửa deck trước commit note.

### Kiểm định cổng Giai đoạn I

- `python3 -m reloadserver 8765` đã chạy và thất bại với
  `/usr/bin/python3: No module named reloadserver`. Dùng
  `python3 -m http.server 8765` trên đúng cổng làm máy chủ kiểm định thay thế;
  không ghi nhận `reloadserver` là thành công.
- URL viewer, Markdown và deck đều trả HTTP 200. Viewer render đúng Bài 01 ở
  1280×720 và 800×600; ảnh chụp đầu trang không có tràn ngang, chồng lấn hoặc
  tài nguyên hỏng. Bản in Chromium có 16 trang và chứa đủ các mục Lời giải,
  Mô hình hóa Tic-tac-toe và Tài liệu tham khảo.
- Viewer từ chối đúng hai ca âm: `doc` Bài 01 ghép với `deck` Bài 02; đường
  dẫn `doc=../AGENTS.md`. Cả hai hiển thị thông báo lỗi cụ thể và không mở nội
  dung ngoài `materials/lec-NN/`.
- Một heading cấp một; 10 `note-topic-id` duy nhất, đúng mẫu và đứng ngay trước
  heading; 7 khối `solution` cân bằng, không lồng; không có `\(...\)` hoặc
  `\[...\]`; không có `quill.json`.
- `node --check 2627-1/material-viewer.js` đạt. SRI SHA-256 trong HTML khớp
  chính xác KaTeX CSS/JS, auto-render, Marked và DOMPurify cục bộ. Thành phần
  cốt lõi không dùng CDN.
- `index.html` có đúng một liên kết ghi chú Bài 01 theo dạng quy định, còn 11
  bài chưa đạt kiểm định vẫn hiển thị `Chưa có`; không liên kết tệp planning.
- Tự kiểm trực tiếp theo `no-ai-slop/eval.md`: không thêm thuật toán, code hoặc
  mệnh đề không có căn cứ; ví dụ tự đặt được gắn nhãn giả định; không có lời
  dẫn rỗng, giọng quảng bá, câu hỏi tu từ hoặc kết luận AGI thiếu bằng chứng.
  Câu “Vì sao” còn lại là bài kiểm tra có đáp án, không phải câu hỏi tu từ.
- Codex Slides không được dùng cho cổng note; Giai đoạn II vẫn phải rà deck
  bằng Codex Slides. Phiên hiện tại không có in-editor Browser để tuyên bố đã
  xác minh bằng bề mặt Codex Slides.

Trạng thái Giai đoạn I: đủ điều kiện commit; giới hạn còn lại là thiếu mô-đun
`reloadserver`. Giai đoạn II phải xử lý các điểm đồng bộ deck đã hoãn và chạy
lại kiểm định RevealJS/Codex Slides trước commit deck.

---

# Đợt rà Giai đoạn II — Writer

## Số trang và cấu trúc

- Báo cáo reader ghi **64 trang là sai**. Kiểm đếm trực tiếp trên
  `lecture-01-gioi-thieu-hoc-tang-cuong.html`: deck có **42 `data-slide-id`
  duy nhất** (`P00–P02`, `A00–A04`, `B00–B02`, `C00–C05`, `D00–D03`,
  `E00–E02`, `F00–F03`, `G00–G04`, `H04–H07`, `Z00`, phụ lục `H00–H03`) trong
  **7 section ngoài**. Outline và storyboard đã ghi rõ căn cứ 42.
- Mạch nguồn giữ nguyên: 120 phút trình chiếu chính (mạch 1–6) và 30 phút bài
  tập (mạch 7). Không thêm code demo.

## Đồng bộ note ↔ deck

- Bảng ánh xạ hai chiều 10 `note-topic-id` ↔ `data-slide-id` đã thêm vào
  `outline.md` và `storyboard.md`; cả hai chiều đều truy được.
- Rà ký hiệu trên deck: $S_t$, $A_t$, $R_{t+1}$, $G_t$, $\pi(a\mid h_t)$,
  $V^\pi(h_t)$, $\mathcal A(S_t)$ khớp bảng thuật ngữ outline; cầu nối
  $h_t\leftrightarrow(S_t,\text{lượt})$ có trên mặt G03 và ghi chú E01, G02.
- Rà khái niệm: trạng thái/quan sát tách biệt (A01); có mô hình/phi mô hình
  (E02, nối lại A03–A04); thăm dò/khai thác (F00–F03); Tic-tac-toe (G00–G04).
  Chu trình vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra có
  trong từng cụm của storyboard; mỗi trang một luận điểm; ghi chú diễn giả
  tiếng Việt không lặp mặt trang; mọi trang có dòng `Nguồn` truy nguyên.

## Sửa SVG

- `img/lec-01/delayed-reward.svg`: mô tả (`desc`) cũ đọc số kiểu "S không",
  "A t tại S t" dễ hiểu thành phủ định/đơn vị sai. Đã viết lại thành "S0 đến
  S4" theo góp ý reviewer sinh viên. File vẫn hợp lệ XML, giữ
  `role="img"`, `title`, `desc`. Các SVG khác không phát hiện lỗi truy cập
  hoặc nội dung.

## Metadata runtime

| Vai trò | requested_model | observed_model | provider | Ghi chú |
|---|---|---|---|---|
| Plan reader (Giai đoạn II) | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter | Phiên hợp lệ. |

- Một lượt plan trước đó bị loại vì agent gọi sai công cụ `list_files` thay vì
  trả kế hoạch; lượt hợp lệ chạy lại độc lập như bảng trên.
- Codex Slides không khả dụng trong môi trường này: Node là v18.19.1 trong khi
  plugin cần Node 20+, và khởi động báo
  `ReferenceError: File is not defined`. Vì vậy **chưa được phép tuyên bố đã
  rà deck bằng Codex Slides**; đây là giới hạn công cụ còn lại.

## Tự kiểm cuối đợt này

- Đếm lại 42 `data-slide-id` duy nhất; 49 cặp `<section>` cân bằng
  (7 vỏ ngoài + 42 trang); 42 ghi chú diễn giả.
- Đường dẫn trong deck: 11 tham chiếu SVG ngoài + 2 SVG nội dòng (B02),
  CSS `lecture-style.css`, `revealjs/*`, `plugin/*`, `vendor/katex` đều tồn
  tại theo kiểm kê trước; không có ảnh raster.
- `index.html` liên kết đúng một bài giảng Bài 01 và một ghi chú Bài 01 qua
  `material-viewer.html`; không cần sửa.
- `no-ai-slop`: không thêm câu dẫn rỗng, số liệu ngoài nguồn hoặc thuật ngữ
  xuất hiện sớm. Quill dùng ở chế độ rà mạch; không tạo `quill.json`.
- Không commit.

## Tiếp nối lượt writer Giai đoạn II sau lỗi tool_call_limit

- Lượt writer Giai đoạn II trước đó dừng giữa chừng vì agent vượt giới hạn
  gọi công cụ (`tool_call_limit`); không hoàn tác các thay đổi hợp lệ của lượt
  đó. Lượt tiếp nối này dùng cùng model và chỉ đọc các tệp được giao:
  `materials/lec-01/lecture-note.md`,
  `lecture-01-gioi-thieu-hoc-tang-cuong.html`, `planning/lec-01/outline.md`,
  `planning/lec-01/storyboard.md`, `planning/lec-01/review-log.md`.
- Kết quả đối chiếu trên lượt này:
  - Đếm lại 42 `data-slide-id` duy nhất trong HTML (P 3, A 5, B 3, C 6, D 4,
    E 3, F 4, G 5, H04–H07+Z00 5, phụ lục H00–H03 4), đúng 7 section ngoài;
    tổng thời lượng 120 phút (mạch 1–6: 30+22+18+18+14+18) và 30 phút bài tập
    (6+7+7+7+3) khớp outline và storyboard; không sửa số trang hay thời lượng.
  - Bảng ánh xạ hai chiều 10 `note-topic-id` ↔ `data-slide-id` khớp nội dung
    note và HTML; ký hiệu và quy ước trên deck ($R_{t+1}$, $G_t$, $\pi(a\mid h_t)$,
    $V^\pi(h_t)$, $\mathcal A(S_t)$, cầu nối $h_t\leftrightarrow(S_t,\text{lượt})$,
    thưởng $+1/0/-1$, kiểm tra ô 5) khớp note; HTML không cần sửa.
  - Sửa một sai khác trong `outline.md`: dòng cầu nối trong bảng thuật ngữ ghi
    "dùng ở E01, G00, G03" trong khi G00 không nhắc cầu nối trên deck; đã sửa
    thành "E01, G02, G03 (ghi chú E01, G02; mặt trang G03)" khớp HTML hiện hành.
- Giới hạn: lượt này không chạy lệnh shell (không dựng server, không chụp
  Chromium, không kiểm tra đường dẫn hệ thống tệp); các kiểm định đó phải do
  điều phối viên chạy. Không sửa lecture note, SVG, index, template, CSS,
  vendor hoặc bài khác. Không tạo `quill.json`; không commit.

---

# Đợt rà Giai đoạn II — Writer hợp nhất năm báo cáo (lượt hiện hành)

## Năm báo cáo độc lập (đợt hợp nhất)

### 1. Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | P01 | Tiên quyết nêu sai: chỉ "xác suất cơ bản" trong khi note yêu cầu kỳ vọng có điều kiện và đại số tuyến tính cơ bản. | P01 dòng "Kiến thức cần dùng" so với note §Mục tiêu và kiến thức tiên quyết. | Nêu đầy đủ tiên quyết trên P01. | Áp dụng: P01 ghi "xác suất cơ bản (biến ngẫu nhiên, kỳ vọng có điều kiện, phân phối đều) và đại số tuyến tính cơ bản". |
| trung bình | B00/B02 | Hai trang dẫn nhập chưa nói rõ đây là ví dụ sẽ được phân tích sau. | B00 chỉ "chuẩn bị cho phần hình thức"; B02 ghi chú "dẫn nhập cho phần hình thức sau". | Ghi tường minh "ví dụ dẫn nhập sẽ được phân tích sau" ở box B00 và ghi chú B02. | Áp dụng. |
| nhẹ | Z00 | Chỉ dẫn "nhấn ↓" nằm trên mặt trang, không phù hợp mặt chiếu. | Z00: "Phụ lục thông tin nguồn: nhấn ↓". | Bỏ khỏi mặt trang, giữ hướng dẫn trong ghi chú. | Áp dụng. |

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.

### 2. Kết nối và mạch viết

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | D03→E00 | Chưa có câu nối từ mục tiêu kỳ vọng $G_t$ sang chính sách/hàm giá trị. | Ghi chú D03 kết thúc ở phần thưởng; E00 mở bằng thế cờ. | Thêm câu nối ở ghi chú D03 hoặc box E00. | Áp dụng ở ghi chú D03. |
| trung bình | F00–F03 | Thăm dò–khai thác chưa nối với chính sách vừa định nghĩa. | F01–F03 không nhắc $\pi$. | Nối bằng diễn đạt trong nguồn; không nêu UCB hay epsilon-greedy vì ngoài nguồn. | Áp dụng ở ghi chú F03: khai thác ↔ chọn theo giá trị ước lượng, thăm dò ↔ $\pi$ đặt xác suất khác không. |
| trung bình | F03→G00 | Chưa có câu nối từ F03 sang phần G. | F03 kết bằng câu hỏi; G00 mở bằng bài toán. | Thêm câu nối. | Áp dụng: G00 mở bằng "gắn khái niệm đã định nghĩa vào một bài toán cụ thể". |
| nhẹ | G04→H04 | Thiếu tín hiệu chuyển sang phần ôn tập. | H04 mở trực tiếp bằng câu hỏi. | Thêm câu dẫn đánh dấu chuyển khối. | Áp dụng. |

Runtime: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter.

### 3. Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | A04 | Dùng cặp thuật ngữ "có mô hình/phi mô hình" trước khi E02 định nghĩa. | Box A04: "học cả mô hình hoặc học không cần mô hình tường minh". | Giữ ý, diễn đạt trung tính và dẫn tới phần E. | Áp dụng: "cách tác tử sử dụng hoặc không sử dụng mô hình được định nghĩa ở phần sau"; ghi chú A04 sửa kèm theo. |
| trung bình | C05 | Chưa nhắc hành động $t$ làm đổi quan sát sau. | Box C05 chỉ nêu đổi vị trí/quan sát tiếp theo mà không gắn với hành động. | Nhắc $A_t$ làm đổi quan sát sau. | Áp dụng. |
| nhẹ | G03 | Thiếu ghi chú $G_t=R_{t+1}+G_{t+1}$ làm nền của công thức chọn nước. | Công thức G03 dùng $R_{t+1}+V^\pi(S_{t+1})$ mà không nêu đồng nhất thức. | Thêm ghi chú nêu $G_t=R_{t+1}+G_{t+1}$. | Áp dụng trong ghi chú G03. |

Runtime: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter.

### 4. Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | D02 | $T$ chưa được định nghĩa khi xuất hiện; chuỗi $R_1,\ldots,R_4$ chưa nêu giá trị từng phần. | D02: "Với $T=4$ trên hình trước…". | Định nghĩa $T$ là chỉ số trạng thái kết thúc; nêu $R_1=R_2=R_3=0$, $R_4=1$. | Áp dụng. |
| trung bình | E01 | Việc viết $V^\pi(S_t)$ ở phần sau thiếu ghi chú điều kiện cho phép rút gọn lịch sử. | E01 định nghĩa trên $h_t$; G03 dùng $V^\pi(S_{t+1})$. | Thêm ghi chú nêu điều kiện Markov/quan sát đầy đủ cho phép viết $V^\pi(S_t)$. | Áp dụng trong ghi chú E01. |

Báo cáo toán này có ba dòng kết luận ghi $G_0=G_1=G_3=-1$: **loại vì tự mâu thuẫn** với chính phép tính trong báo cáo và với deck ($G_0=R_1+R_2+R_3+R_4=0+0+0+1=1$; quỹ đạo thưởng 0, 0, 0, 1 cho $G_0=G_1=G_2=G_3=1$). Không dùng các dòng này làm căn cứ sửa.

Runtime: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter.

### 5. Phản biện học thuật và giảng dạy

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|
| trung bình | D03→E00 | Mục tiêu kỳ vọng $G_t$ chưa được nối sang đại lượng điều khiển và đánh giá. | Giống mục Kết nối và mạch viết. | Thêm câu nối ghi chú D03. | Áp dụng (trùng với mục 2; sửa một lần). |

Runtime: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter.

## Quyết định tổng hợp

- Xử lý toàn bộ lỗi nghiêm trọng của năm báo cáo; sửa các điểm trung bình có căn cứ trong hàng đợi đã duyệt.
- Loại đề xuất thêm hệ số chiết khấu $\gamma$: nguồn và note dùng tổng hữu hạn, không có $\gamma$.
- Loại đề xuất thêm UCB hoặc epsilon-greedy: thuật toán ngoài nguồn.
- Giữ question-box H06–H07: `lecture-style.css` (dòng 130) đã định nghĩa `.reveal .question-box` dùng chung, không cần thêm CSS.
- Loại ba dòng báo cáo toán nói $G_0$, $G_1$, $G_3=-1$ vì tự mâu thuẫn; phép tính đúng là $G_0=G_1=G_2=G_3=1$ với quỹ đạo $R_1=R_2=R_3=0$, $R_4=1$.
- Codex Slides vẫn không khả dụng: Node là v18.19.1 (cần Node 20+) và khởi động báo `ReferenceError: File is not defined`; không tuyên bố đã rà deck bằng Codex Slides.
- Cấu trúc giữ nguyên: 7 section, 42 trang, thứ tự và ID không đổi; không thêm gamma, không thêm thuật toán ngoài nguồn, không tạo trang mới, không sửa SVG, note, CSS, index, template, vendor.
- `no-ai-slop` áp dụng khi viết lại các câu nối: không câu dẫn rỗng, không thuật ngữ sớm. Quill dùng ở chế độ rà mạch, không tạo `quill.json`.

## Danh sách tệp sửa (không commit)

- `lecture-01-gioi-thieu-hoc-tang-cuong.html`
- `planning/lec-01/outline.md`
- `planning/lec-01/storyboard.md`
- `planning/lec-01/review-log.md`

## Giai đoạn II — Recheck deck sau sửa (writer, đợt kế tiếp)

### Metadata runtime

| Vai | requested_model | observed_model | provider |
|---|---|---|---|
| Reviewer flow (recheck) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| Reviewer math (recheck) | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter |

### Kết luận

- Recheck flow: không còn lỗi nghiêm trọng về kết nối; lỗi nghiêm trọng đã đóng. Hai gợi ý câu nối còn sót được áp dụng cục bộ.
- Recheck math: xác nhận phép tính $G_0=G_1=G_3=1$ và các công thức D02, E01, G03 đúng; không còn lỗi nghiêm trọng. Mục "lời nói có lỗi argmax" của vòng trước bị loại vì không có bằng chứng trong checkpoint.

### Phát hiện escape LaTeX và sửa

| Vị trí | Phát hiện | Sửa |
|---|---|---|
| E01 (ghi chú) | `V^\\pi(S_t)` dùng hai backslash trong chuỗi | Đổi thành một backslash `$V^\pi(S_t)$`; không đụng công thức đúng khác |
| F03 (ghi chú) | `$\\pi$` dùng hai backslash | Đổi thành `$\pi$` |
| G03 (ghi chú) | `$t+1 \\le T$` và `$\\pi$`, `V^\\pi` dùng hai backslash | Đổi thành `\le` và `\pi`, `V^\pi` một backslash |
| Z00 (ghi chú) | Thiếu câu nối H07→Z00 | Thêm câu đầu ghi chú: "Hai thảo luận vừa rồi khép phần mở rộng."; không thêm dòng trên mặt trang |

### Sửa câu nối

- E00 box đổi thành câu nối trực tiếp từ D03: "Để cực đại hóa kỳ vọng của $G_t$, tác tử phải tách hai việc: chọn nước đi và đánh giá thế cờ."
- H04 dòng muted đổi thành: "Ví dụ Tic-tac-toe khép phần lý thuyết; trang sau chữa câu hỏi ôn tập, rồi chuyển sang hai thảo luận."
- Storyboard đã đồng bộ đúng các câu này tại các hàng mạch 4, E00, H04 và Z00.

### Quy tắc

- Áp dụng `no-ai-slop`: không câu dẫn rỗng, không khẳng định tuyệt đối. Quill dùng ở chế độ rà mạch, không tạo `quill.json`. Không commit.

### Danh sách tệp sửa (không commit)

- `lecture-01-gioi-thieu-hoc-tang-cuong.html`
- `planning/lec-01/storyboard.md`
- `planning/lec-01/review-log.md`

## Giai đoạn II — Recheck cuối sau sửa escape và câu nối

| Vai | requested_model | observed_model | provider | Kết quả |
|---|---|---|---|---|
| Toán học (recheck cuối) | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter | Không còn lỗi bắt buộc; công thức và các escape ở E00, E01, F03, G03 đúng. |
| Mạch viết (recheck cuối) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | Không còn lỗi bắt buộc; các ranh giới D–E, F–G, G–H và H–Z đã nối được. |

Quyết định của điều phối viên:

- Bác nhận định H00–H03 là các trang ngang. Trong RevealJS, các `<section>`
  con cùng nằm trong một `<section>` ngoài tạo stack dọc; H00–H03 nằm dưới
  Z00 đúng như HTML và storyboard.
- Giữ cụm “chữa câu hỏi ôn tập” ở H04–H05. Mặt trang nêu câu hỏi và ghi chú
  diễn giả chứa đáp án, nên người dạy có đủ nội dung để chữa; không cần thêm
  trang đáp án.
- Không đổi `\mathbb E` thành `\mathbb{E}`: cả hai cách đều hợp lệ, và ký hiệu
  hiện tại đã thống nhất với lecture note cùng các trang khác.
- Không dùng tuyên bố “đã từng có lỗi ngoặc trong `argmax`” của recheck toán,
  vì không có bằng chứng trong checkpoint hoặc diff. Công thức G03 hiện tại đã
  được điều phối viên đối chiếu trực tiếp và đúng.
- Tìm chuỗi hai backslash trong HTML sau sửa trả về rỗng; `git diff --check`
  đạt trước khi chuyển sang kiểm định cục bộ.

## Giai đoạn II — Kiểm định cục bộ cuối

### Kiểm tra cấu trúc và tài nguyên

- 42 `data-slide-id`, 42 giá trị duy nhất; 42 khối ghi chú diễn giả.
- 7 `<section>` ngoài, gồm mạch mở đầu và mạch kết luận; cấu trúc đóng thẻ hợp lệ.
- 10 `note-topic-id` được ánh xạ hai chiều giữa lecture note và deck.
- 12 SVG trong `img/lec-01/`; tất cả phân tích được bằng trình phân tích XML và có `role="img"` cùng mô tả thay thế.
- Không có tham chiếu ảnh raster, tài nguyên cốt lõi từ xa, đường dẫn cục bộ bị thiếu hoặc chuỗi LaTeX hai backslash.
- Cấu hình bắt buộc hiện diện: khung 1280 × 720, điều khiển ở cạnh, số trang, băm một-based, băm URL, Math/Notes/Highlight.
- `git diff --check` đạt.

### Kiểm tra chạy và hiển thị

- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`: `/usr/bin/python3: No module named reloadserver`.
- Dùng phương án dự phòng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm chỉ chứa tài sản công khai; không sao chép `.env`.
- Chromium qua Playwright 1.55.0 duyệt đủ 42 trang ở 1280 × 720 và 800 × 600. Cả hai lượt trả HTTP 200, không lỗi console, lỗi trang hoặc yêu cầu mạng thất bại; không trang nào có `scrollWidth`/`scrollHeight` vượt khung.
- Kiểm tra bàn phím đạt: từ P00, `ArrowDown` tới P01 và `ArrowRight` tới C00 theo cấu trúc stack dọc/ngang.
- Đã dựng và xem bảng ảnh thu nhỏ của toàn bộ 42 trang ở cả hai kích thước; không phát hiện chữ bị cắt, chồng lấn, công thức vỡ, hình mất hoặc tương phản gây chặn bàn giao.
- Trình đọc lecture note trả HTTP 200, dựng 30 tiêu đề và nội dung Markdown; liên kết về deck hiện diện. `index.html` trả HTTP 200, có liên kết deck và lecture note, không có liên kết tới planning/outline/storyboard/review-log.

### Giới hạn công cụ

- Không thể rà bằng Codex Slides: runtime cục bộ dùng Node v18.19.1 trong khi plugin cần Node 20+, và máy chủ dừng với `ReferenceError: File is not defined`. Đã tiếp tục đầy đủ kiểm tra RevealJS cục bộ; không tuyên bố đã xác minh bằng Codex Slides.

## Đợt sửa 2026-10-12 — Giai đoạn I: ghi chú bài giảng

### Tác tử và phạm vi

- Vai: tác tử soạn ghi chú bài giảng Bài 01 (viết tệp). Loại `general-purpose` theo brief của điều phối viên; mô hình Opus 5.5 (`claude-opus-5-5`), mức `high` theo brief. Không commit, không push.
- Tệp ghi: `2627-1/materials/lec-01/lecture-note.md` (viết lại toàn bộ); thêm ba SVG mới cho ghi chú: `img/lec-01/chapter-map.svg` (cấu trúc chương), `img/lec-01/robot-four-cells.svg` (môi trường robot dọn dãy bốn ô), `img/lec-01/tictactoe-four-moves.svg` (bốn nước 3, 6, 7, 9 cùng kỳ vọng một bước). Không sửa SVG cũ, deck, outline, storyboard, index.
- Đầu vào đã đọc: `quyet-dinh-chuan-2026-10-12.md` (mục 1–4, 6, 8), `revision-plan-2026-10-12.md` (A, B, C, D), `AGENTS.md` (các mục brief yêu cầu), mẫu `materials/_templates/lecture-note.md`, mẫu math-4-AI Bài 07 (chỉ cách trình bày), ghi chú và deck cũ, `no-ai-slop` (`SKILL.md`, `eval.md`), `quill/references/workflows.md` (Outline, Threads, Concept, Revise), Sutton và Barto (2018) bản PDF, văn bản và hình trang 28–30 của PPTX nguồn (chỉ đọc).

### Kiểm thế cờ gốc (quyết định chung mục 8)

- Hình trang 28–29 của PPTX nguồn là thế cờ X O O / O X X / _ _ X (X ở ô 1, 5, 6, 9; O ở ô 2, 3, 4): bốn X, ba O, X đã thắng theo đường chéo 1–5–9. Đây là thế cờ đã kết thúc của Sutton và Barto (2018, §1.5, tr. 8), không phải thế cờ chờ X chọn nước. Trang 30 là Hình 1.1 của Sutton và Barto (dãy nước đi), không có thế cờ riêng.
- Vì vậy nguồn không có thế cờ "2 X, 3 O". Ghi chú dùng thế cờ của `tictactoe-board.svg` (X ở 1, 5; O ở 2, 4, 8; trống 3, 6, 7, 9) như số liệu sư phạm tự xây dựng, nêu rõ O đi trước (đếm quân) và đến lượt X ở bước $t=2$, và tính đủ bốn nhánh, gồm $a=6$. Hai SVG cũ `tictactoe-search.svg` và `tictactoe-value.svg` chỉ vẽ ba nhánh nên ghi chú không dùng; việc sửa hai SVG này (thêm nhánh $a=6$, gọi đúng thế cờ sau nước của X) thuộc giai đoạn deck.

### Số liệu đã tính lại (bằng tay và bằng mã phân số trong scratchpad)

- Tic-tac-toe, thế cờ $s$, X và O chọn đều: kỳ vọng một bước $a=3$: $\frac13$; $a=6$: $0$ (giá trị ba thế cờ kế tiếp $\frac12$, $0$, $-\frac12$); $a=7$: $\frac23$; $a=9$: $1$. $v_{\pi_u}(s)=\frac12$; xác suất X thắng $\frac23$, O thắng $\frac16$, hòa $\frac16$. $a^*=9$.
- Ví dụ 01.9: thế cờ hai ô trống (X 1, 3, 5; O 2, 4, 7, 8): $v_{\pi_u}=0$, $v_{\pi_w}=1$.
- Bài tập 01.8 ($\pi_w$: thắng ngay nếu có, nếu không chọn đều): $a=3,7,9$ cho $1$, $a=6$ cho $\frac12$; $\arg\max=\{3,7,9\}$.
- Bài tập 01.7 (X 3, 4, 9; O 1, 5, 7; trống 2, 6, 8; X đi trước): nước 6 thắng qua cột 3–6–9.
- Robot dọn dãy bốn ô: Ví dụ 01.5 $G_0=\dots=G_3=1$; Ví dụ 01.6 (chi phí di chuyển $c=0{,}1$) $G=(0{,}7;0{,}8;0{,}9;1;0)$; Ví dụ 01.7 lượt B sau sửa phần thưởng $G_0=0$; Bài tập 01.3 $(0,-1,0,1)$: $G_0=0$, $G_1=0$, $G_3=1$; Bài tập 01.5 ($L=4$, phải/hút mỗi $\frac12$) $v=\frac1{16}$; Tình huống 01.1 ($L=5$, chọn đều ba hành động) bảng $w(k,m)$ và $v_{\pi_u}(h_0)=\frac8{243}$, kiểm bằng đếm $1+5$ dãy thành công; nước khai thác một bước tại $h_0$ là $\text{phải}$ ($\frac6{81}$ so với $\frac1{81}$); Tình huống 01.2 $v_{\pi_1}(h_a)=1$, $v_{\pi_1}(h_b)=0$.
- Ví dụ 01.10: một lần thử thêm dịch $\bar r(\mathrm A)$ trong $[\frac{12}{21},\frac{13}{21}]$, $\bar r(\mathrm B)$ trong $[\frac{1{,}1}3,\frac{2{,}1}3]$; Bài tập 01.6: $\frac{2{,}00}3\approx0{,}667$ và $0{,}50$.

### Lỗi của bản cũ đã sửa

- $V^\pi$ đổi thành $v_\pi$; "phần thưởng tích lũy" đổi thành "lợi tức (return)".
- Giá trị sau nước thắng: bản cũ (dòng 202) ghi $+1$; nay giá trị của lịch sử đã kết thúc bằng $0$, phần thưởng $+1$ nằm ở $R_{t+1}$ (Nhận xét 01.15, Bài tập 01.7, 01.10).
- Tập hành động hợp lệ $\{3,7,9\}$ sửa thành $\{3,6,7,9\}$; chỉ số bước Tic-tac-toe đếm theo lượt của X, nước của O thuộc môi trường; trạng thái không cần "lượt chơi".
- Rút gọn lịch sử thành thế cờ có đủ ba điều kiện (Nhận xét 01.21); phép chọn nước có Mệnh đề 01.22 và chứng minh theo bước.
- Bỏ mọi lời quy trình ("bước thuật toán không áp dụng", "cần ghi vào nhật ký", "note"), bỏ liên kết URL và tên tệp nguồn; trích dẫn "Bài giảng gốc (2025–2026), trang N".

### Giáo trình đã tham khảo theo mục (tham khảo cách dẫn dắt, không dịch, không chép)

| Mục của ghi chú | Giáo trình và mục |
|---|---|
| Mở chương, Mục 1 | Sutton và Barto (2018) §1.1 (tr. 1–4), §3.1 (tr. 47–53, ranh giới tác tử–môi trường, chỉ số $R_{t+1}$), §1.4 (tr. 7–8, cách hiểu trạng thái); *Học máy thống kê* `sec_mdp_introduction.tex` (dẫn từ học có giám sát sang tương tác; giáo trình dùng "tác nhân"/"tác tử", học phần dùng "tác tử") |
| Mục 2 | Sutton và Barto (2018) §1.1; Goodfellow, Bengio và Courville (2016) §5.1.3 (chỉ dẫn mục, không ghi trang) |
| Mục 3 | Sutton và Barto (2018) §3.2 (tr. 53–54, giả thuyết phần thưởng), §3.3 (tr. 54–57, lượt và lợi tức), §3.4 (tr. 57, quy ước trạng thái kết thúc) |
| Mục 4 | Sutton và Barto (2018) §1.3 (tr. 6–7, bốn thành phần, phần thưởng khác giá trị), §3.5 (tr. 58), §2.1–2.2 (tr. 25–28, hành động tham lam, khai thác, thăm dò), §8.1 (tr. 159–161, lập kế hoạch) |
| Mục 5 | Sutton và Barto (2018) §1.5 (tr. 8–13, đối thủ không hoàn hảo, bảng giá trị, nước thăm dò), §6.8 (tr. 136–137, trạng thái sau nước đi) |
| Tình huống | Sutton và Barto (2018) §17.3 (tr. 464, quan sát và trạng thái) cho Tình huống 01.2 |

Ví dụ xuyên suốt robot dọn dãy bốn ô là phiên bản thu nhỏ tự xây dựng (theo plan A5 và quyết định chung mục 8), ghi là số liệu sư phạm trong đoạn quy ước sau bảng ký hiệu.

### Số hiệu cuối cùng

- Bộ đếm chung (24): Định nghĩa 01.1, 01.2; Nhận xét 01.3, 01.4, 01.5; Định nghĩa 01.6; Nhận xét 01.7, 01.8; Định nghĩa 01.9, 01.10; Mệnh đề 01.11; Nhận xét 01.12; Định nghĩa 01.13, 01.14; Nhận xét 01.15; Định nghĩa 01.16; Nhận xét 01.17; Định nghĩa 01.18; Nhận xét 01.19; Định nghĩa 01.20; Nhận xét 01.21; Mệnh đề 01.22; Định nghĩa 01.23; Nhận xét 01.24.
- Ví dụ 01.1–01.12; Bài tập 01.1–01.8 trong mục, 01.9–01.12 củng cố; Tình huống 01.1, 01.2. Công thức đánh số (3.1), (3.2), (4.1), (5.1), (5.2), (5.3). Không có khối `algorithm` (nguồn không có thuật toán).
- `note-topic-id`: giữ `lec-01-topic-01`…`10` (topic-07 đổi tên "Lịch sử và thế cờ trong Tic-tac-toe", Mục 5.2); thêm `lec-01-topic-11` (đọc thêm: tác tử nhiều nhiệm vụ và mô hình thế giới).

### Sai khác so với kế hoạch B và lý do

- Độ dài: 25 696 từ theo `wc -w` (khoảng 24 800 khi tính mỗi công thức một từ), vượt đích 12 000–14 000 của B4 và mức thường gặp 8 000–20 000. Lý do: mọi ví dụ, bài tập, tình huống tự chứa dữ kiện; Ví dụ 01.12 và Bài tập 01.8 liệt kê đủ mười nhánh của cây hai lượt; Tình huống 01.1 có bảng tính ngược đầy đủ. Điều phối viên quyết định có cần rút gọn hay không.
- Mệnh đề 01.22 phát biểu ba phần: (a), (b) trên lịch sử, không cần Markov; (c) trên thế cờ dưới Nhận xét 01.21. Kế hoạch đặt mệnh đề chỉ cho Tic-tac-toe; dạng trên lịch sử cần cho Tình huống 01.1.
- Tình huống 01.1 dùng $L=5$ và chính sách chọn đều ba hành động ($v=\frac8{243}$) thay cho "cắt sau 6 bước" của B4, để thống nhất $L=5$ với Ví dụ 01.1 và Bài tập 01.13 của kế hoạch C; thêm bước chọn hành động đầu bằng Định nghĩa 01.23. Bài tập 01.5 giữ $L=4$ (ghi rõ trong khối) để giữ kết quả $\frac1{16}$ của kế hoạch.
- Mục 1 thêm mục con 1.4 (Nhận xét 01.4, 01.5) và 1.5 (Ví dụ 01.2, 01.3) theo thứ tự B2; Bài tập 01.1 dùng robot bắt đầu ở ô 3 để khác Ví dụ 01.1.
- Bài tập 01.2 dùng năm tình huống (a)–(e), gồm câu hỏi "học một môn học" của nguồn trang 20, thay cho "4 mẫu".
- Ví dụ 01.6 thêm cách đặt phần thưởng có chi phí di chuyển $c=0{,}1$ để các $G_t$ khác nhau và minh họa ý "hy sinh phần thưởng tức thời" của nguồn trang 25.
- Không dùng `tictactoe-search.svg`, `tictactoe-value.svg`, `uncertainty.svg`, `course-map.svg` (hai hình đầu thiếu nhánh $a=6$; hai hình sau không có chỗ trong chương).

### Giới hạn còn lại

- Kết quả của bài khác được dẫn bằng "Bài 0N" kèm phát biểu lại một câu, chưa có số hiệu `0N.k`; đợt đồng bộ sau thay bằng số hiệu.
- Bài tập 01.16 được nhắc trong "Hướng dẫn đọc thêm" trước khi `exercises.md` tồn tại.
- Deck hiện tại còn lệch ghi chú ($V^\pi$, $\{3,7,9\}$, giá trị sau nước thắng, thiếu Mệnh đề 01.22); giai đoạn II sửa theo ghi chú.
- Các chỗ nhờ tác tử rà toán soi kỹ: chứng minh Mệnh đề 01.22 Bước 2 (điều kiện hóa theo $H_{t+1}$, quy ước kỳ vọng khi chọn $a$ mà $\pi(a\mid h)=0$); lập luận Nhận xét 01.21; bảng $w(k,m)$ của Tình huống 01.1.

### Tự kiểm `no-ai-slop` (chế độ Edit) và `quill`

- Phạm vi: toàn bộ văn bản của ghi chú. Đối chiếu `eval.md`: không câu hỏi tu từ, không mệnh lệnh "hãy", không lời quy trình hay lời giảng viên, tài liệu không làm chủ ngữ; đã bỏ "nhấn mạnh", "rất"; một dấu gạch dài duy nhất ở tiêu đề `#` theo mẫu; danh sách chỉ dùng cho mục song song; đoạn kết mục là văn xuôi ba ý. Mẫu lặp có chủ đích được giữ vì có chức năng học tập: câu "Nhầm lẫn thường gặp là…" (6 lần) và nhãn giai đoạn trong ví dụ (Dữ kiện, Tính, Diễn giải, Kiểm tra lại). Kết quả: đạt, không còn mục `fail`.
- `quill` (Outline, Concept, Threads làm bảng kiểm, không tạo `quill.json`): mỗi khái niệm được định nghĩa trước lần dùng; các tham chiếu tiến (Định nghĩa 01.9 trong Định nghĩa 01.1; Định nghĩa 01.16 trong Nhận xét 01.5; Bài tập 01.8 trong Nhận xét 01.24) đều nêu điều đang tạm chấp nhận; luồng "lịch sử → thế cờ" mở ở Mục 1.3, đóng ở Nhận xét 01.21 và Tình huống 01.2; luồng "ước lượng $\bar r$ → nước khai thác" mở ở Định nghĩa 01.18, đóng ở Định nghĩa 01.23.

### Kết quả hai script

- `note_check.py`: 24 môi trường bộ đếm chung, 12 ví dụ, 12 bài tập, không khoảng trống, không trùng, không khối lạ hay lồng, không khối chưa đánh số, không mẫu câu cấm, không `\(`/`\[`.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html` (cổng 8766): 1600×900 và 390×844 đều 0 lỗi KaTeX, 0 lỗi console, 0 yêu cầu ngoài hoặc thất bại, không tràn ngang (đã sửa bảng ký hiệu từng làm tràn ở 390 px). Đã xem ảnh chụp khối chứng minh Mệnh đề 01.22 (1600 px) và Ví dụ 01.12 (390 px), cùng ảnh ba SVG mới.

## Đợt sửa 2026-10-12 — Giai đoạn I: sửa ghi chú theo hai báo cáo rà soát (vai A toán, vai B mạch viết)

Tác tử soạn ghi chú Bài 01 (cùng phiên trên; Opus 5.5, `high`), sửa theo quyết định của điều phối viên. Tệp sửa: `materials/lec-01/lecture-note.md`. Không thêm hay sửa SVG trong đợt này. Không commit.

### Số từ

- Trước: 25 696 (`wc -w`). Sau: 21 037.
- Đã làm toàn bộ C1–C46 và O2, O3, O5, O6, O7, O8, O9, O10, O11; không làm O1, O4, O12.
- Vẫn vượt đích 18 000–19 000 khoảng 2 000 từ. Phần thêm theo yêu cầu rà soát chiếm khoảng 700 từ: quy ước kỳ vọng xác suất 0 (A1), phản ví dụ điều kiện 2 (A2), ba lý do ở Tình huống 01.1 (A3), chia bước Nhận xét 01.19 (B9), ví dụ mô hình (B12), chép lại dữ kiện vào khối (B7). Bảng 9 dòng của Ví dụ 01.10 (O5) tốn thêm ký tự `|` khi đếm bằng `wc`.
- Ứng viên cắt tiếp, cần điều phối viên quyết định: Bài tập 01.11 (khoảng 400 từ); hai tình huống (d), (e) của Bài tập 01.2; rút bản đồ chủ đề còn ba trường.

### Đánh số lại

| Cũ | Mới |
|---|---|
| Định nghĩa/Nhận xét/Mệnh đề 01.1–01.3 | giữ |
| Nhận xét 01.4 (ghi nhớ, thích nghi, khái quát) | bỏ (O3); còn một câu ở Mục 1.4 |
| Nhận xét 01.5 | Nhận xét 01.4 |
| Định nghĩa 01.6 | Định nghĩa 01.5 |
| Nhận xét 01.7 + 01.8 | gộp thành Nhận xét 01.6 (C12) |
| 01.9, 01.10, 01.11, 01.12 | 01.7, 01.8, Mệnh đề 01.9, Nhận xét 01.10 |
| 01.13–01.19 | 01.11–01.17 |
| 01.20–01.24 | 01.18–01.22 |
| Ví dụ 01.2, 01.3 (AlphaGo, thao tác robot) | bỏ (O2); dữ kiện nằm ở Bài tập 01.9, 01.12 |
| Ví dụ 01.4–01.10 | Ví dụ 01.2–01.7, 01.9 |
| (mới) | Ví dụ 01.8 (Mô hình đúng và mô hình sai của robot), B12 |
| Ví dụ 01.11 (thế cờ bốn ô trống) | bỏ khối; nội dung ở đoạn đọc hình Mục 5.1 (C31) |
| Ví dụ 01.12 | Ví dụ 01.10 |
| Bài tập 01.1–01.12, Tình huống 01.1–01.2 | giữ số |

Danh sách cuối:
- Bộ đếm chung (22): Định nghĩa 01.1, 01.2; Nhận xét 01.3, 01.4; Định nghĩa 01.5; Nhận xét 01.6; Định nghĩa 01.7, 01.8; Mệnh đề 01.9; Nhận xét 01.10; Định nghĩa 01.11, 01.12; Nhận xét 01.13; Định nghĩa 01.14; Nhận xét 01.15; Định nghĩa 01.16; Nhận xét 01.17; Định nghĩa 01.18; Nhận xét 01.19; Mệnh đề 01.20; Định nghĩa 01.21; Nhận xét 01.22.
- Ví dụ 01.1–01.10.

`note-topic-id`:
- `lec-01-topic-09` (AlphaGo và thao tác robot) được rút khỏi bản đồ vì chủ đề không còn là một mục. Deck không tham chiếu mã này (đã kiểm `grep`).
- Các mã còn lại giữ nguyên.

Giai đoạn II cần đồng bộ deck với số hiệu mới.

### Phát hiện và xử lý

| Mã | Trạng thái | Xử lý (vị trí mới) |
|---|---|---|
| A1 | đã sửa | Kiến thức tiên quyết thêm "tổng lấy trên các $z$ có $\Pr(Z=z,Y=y)>0$". Định nghĩa 01.12 thêm quy ước kỳ vọng trên phân phối diễn biến bắt đầu từ $h$, trùng kỳ vọng có điều kiện khi xác suất dương; hiểu tương tự cho $\mathbb E_\pi[\cdot\mid H_t=h,A_t=a]$. Bước 3 Mệnh đề 01.20 thêm câu về số hạng $\pi(a\mid h)=0$. Ví dụ sau Định nghĩa 01.12 đổi sang $h=(\text{sạch},\text{trái},0,\text{sạch})$, $v_{\pi_1}(h)=1$ |
| A2 | đã sửa | "Bỏ điều kiện 2" sau Nhận xét 01.19 dùng luật O mới (chọn đều, trừ khi nước trước là ô 4 thì đánh ô nhỏ nhất) và hai lịch sử O4, X1, O2, X5, O8 / O2, X1, O8, X5, O4 |
| A3 | đã sửa | Tình huống 01.1 mục 3: ba lý do riêng (k là hàm của lịch sử; $\pi_u$ không dùng lịch sử nên không cần quan sát đầy đủ; luật chỉ phụ thuộc $(k,m)$) |
| A4 | đã sửa | Tình huống 01.2: biểu diễn "vị trí $k$ suy ra bằng cách áp luật dịch chuyển từ ô 1, cùng số hành động còn lại" |
| A5 | đã sửa | Bài tập 01.3(b) giới hạn $t=0..3$ và nêu $G_4=0$ |
| A6 | đã sửa | Bài tập 01.4(b): tính ngược cần $T-1$ phép cộng ($T=4$: 3); "Trong thực hành" sau Mệnh đề 01.9 bỏ con số $T$ |
| A7 | đã sửa | Sau Định nghĩa 01.12: "phần thưởng trong một lượt thuộc một tập hữu hạn và $T\le L$" |
| A8 | đã sửa | $\pi_w$ ở Ví dụ 01.6, Ví dụ 01.7, Bài tập 01.8: "nhiều nước thắng ngay thì chọn đều trong số đó" |
| A9 | đã sửa | Dòng $\sigma$ bỏ khỏi bảng ký hiệu (O6); Định nghĩa 01.18 và Nhận xét 01.19 dùng $\tilde s$ |
| A10 | đã sửa | Nhận xét 01.22: "với $\gamma<1$ hoặc khi mọi lượt kết thúc" |
| A11 | đã sửa | Một đoạn sau Định nghĩa 01.12: trạng thái ẩn tương thích với luật cố định theo $(h,a)$ |
| B1 | đã sửa | Rút phần trùng Bài 02 theo bảng 3.3. Dẫn "Bài 02, Mục 1.1" (ranh giới), "Mục 2.5" (Markov), "Mục 3" (chính sách), "Mục 4.2" (chiết khấu), "Mục 4.5" (mô hình), "Mục 5" (thiết kế phần thưởng), "Mục 2.4–2.5" (Tình huống 01.2) |
| B2 | đã sửa | Viết lại đoạn mở Mục 2, 3, 4, 5, không lặp kết mục trước |
| B3 | đã sửa | Định nghĩa 01.7: phần thưởng bị chặn; trong các lượt nhiều bước của chương thuộc tập hữu hạn |
| B4 | đã sửa | Như A3 |
| B5 | đã sửa | Sau Định nghĩa 01.16: "một ước lượng của kỳ vọng lợi tức sau hành động; dạng chính xác có ở Mục 5" |
| B6 | đã sửa | Bỏ Ví dụ 01.2, 01.3 cũ (O2) và gạch AlphaGo ở nhận xét mô hình; Nhận xét 01.22 gạch 1 bỏ số liệu của Bài tập 01.8 |
| B7 | đã sửa | Chép dữ kiện vào Bài tập 01.11(b) (đổi lịch sử thành $(\text{sạch},\text{phải},0,\text{sạch},\text{hút},0,\text{sạch})$, $v=1$), Tình huống 01.2, Ví dụ 01.6 (luật Tic-tac-toe), Ví dụ 01.7, Bài tập 01.2(c) |
| B8 | đã sửa | Bỏ `rl-fields.svg` và đoạn đọc hình |
| B9 | đã sửa | Nhận xét 01.19 chia ba bước có nhãn: một bước, quy nạp theo bước, kỳ vọng |
| B10 | đã sửa | Tình huống 01.1 và Ví dụ 01.10 dùng `aligned` và bảng; Bài tập 01.8 dùng `aligned` |
| B11 | đã sửa | Tách hoặc rút các đoạn nhiều ý (kết mục 3, 4, 5; "Trong thực hành" Mục 5; diễn giải chính sách, mô hình, thăm dò) |
| B12 | đã sửa | Câu trực giác trước Định nghĩa 01.18 (Mục 5.1); Ví dụ 01.8 trước Định nghĩa 01.14; lý do "không áp dụng" ghi dưới đây |
| B13 | không đổi | Theo quyết định 2 của điều phối viên (quyết định chung mục 2): Bài 01 giữ $H_t$ trên quan sát |
| B14 | sửa một phần ở vòng này (câu L509 thực tế chưa đổi; ghi "đã sửa" là sai); hoàn tất ở vòng rà lại 2, mã R6 | Định nghĩa 01.2 thêm "luật của môi trường"; L509 (hai cụm chêm) chưa sửa ở vòng này; Định nghĩa 01.12 nêu rõ "dưới một cách chọn hành động nào đó" cùng quy ước xác suất 0; sau Mệnh đề 01.20 thêm đoạn giải thích $\mathbb E_\pi$ và $\mathbb E$; Tình huống 01.2 sửa biểu diễn; L414 bỏ cùng hình |
| N1 | đã sửa | Đổi các câu "Chương này…", "Mục N làm…" của chính ghi chú sang "chúng ta" hoặc bị động |
| N2 | đã sửa | Nhận xét 01.10 dùng "tổng các phần thưởng nhận được" |
| N3 | đã sửa | Còn một lần nêu "giả thuyết mô hình hóa" |
| N4 | đã sửa | Bỏ khuôn "Ví dụ 01.k cho thấy ba điều" |
| N5 | đã sửa | Bỏ hai tương phản nhị phân (Mục 1.3, Tình huống 01.2) |
| N6 | đã sửa | Bỏ câu kết châm ngôn ở phần đọc thêm |
| N7 | đã sửa | Bỏ "nước 6 dễ bị bỏ sót", "gồm cả ô 6" |
| N8 | đã sửa | Bỏ bình luận "lỗi đánh máy" khỏi ghi chú; lý do vẫn ghi ở review-log |
| N9 | đã sửa | Bảng ký hiệu thêm $\pi_1,\pi_u,\pi_w$ và $\mathbb E_\pi$, $\mathbb E$ |
| N10 | đã sửa | Đổi thành "Mô tả này chưa phải định nghĩa" |
| N11 | đã sửa | "Mục 5.2"; vai trò giả thiết của Mệnh đề 01.20 thành danh sách "Bỏ…" |
| N12 | đã sửa | Từ 21 còn 5 câu lấy bài giảng gốc làm chủ ngữ, giữ ở chỗ cần quy nhận định cho nguồn; còn lại trích trong ngoặc |
| N13 | đã sửa | Công thức mất mát chỉ còn ở Kiến thức tiên quyết |
| N14 | đã sửa | Bài tập 01.10 đổi sang lợi tức theo hai góc nhìn X và O |
| N15 | đã sửa | Trỏ Bài 02 về Markov còn ba chỗ: mở chương, Mục 1.3, Tình huống 01.2 |
| N16 | đã sửa | Câu trực giác trước Định nghĩa 01.2 |
| N17 | đã sửa | Như B14 về (5.1) |

### Bước 4–5 "không áp dụng" của mẫu tám bước

Các khái niệm tác tử, môi trường, trạng thái, quan sát (Mục 1), ba dạng tín hiệu học (Mục 2), chính sách, hàm giá trị, mô hình (Mục 4.1–4.3) và thăm dò, khai thác (Mục 4.4) là khái niệm định nghĩa. Nguồn (trang 4–27) không nêu kết quả hay thuật toán nào cho chúng. Vì vậy bước 4 (kết quả hoặc thuật toán) và bước 5 (chứng minh) không áp dụng. Kết quả của chương chỉ có Mệnh đề 01.9 (Mục 3) và Mệnh đề 01.20 (Mục 5), cả hai có chứng minh.

Bước "kiểm tra" của khái niệm mô hình nằm ở Bài tập 01.9(b) và 01.12(b) trong phần củng cố, không có bài tập ngay trong Mục 4.3.

### Tình huống 01.1 mới (tự tính lại)

- Thiết lập: $L=4$, ba hành động chọn đều.
- $w(4,1)=\frac13$, $w(3,2)=\frac19$, $w(2,3)=\frac1{27}$, $w(1,4)=\frac1{81}$; mọi $w(k,m)$ với $m<5-k$ bằng $0$.
- $v_{\pi_u}(h_0)=\frac1{81}$; kỳ vọng một bước (trái, phải, hút) $=(0,\frac1{27},0)$; $a^*=\text{phải}$.
- Kiểm tra: $\frac13\cdot\frac1{27}=\frac1{81}=(\frac13)^4$.
- Bài tập 01.5 giữ $L=4$, hai hành động: $\frac1{16}$.

### Hai đề nghị chuyển cho tác tử Bài 02

1. Nhận xét 02.3 (Ba dạng tín hiệu học) đổi thành dòng "Nhắc lại:", dẫn Định nghĩa 01.5 và Nhận xét 01.6 của ghi chú Bài 01, kèm phát biểu lại một câu.
2. Câu tiên quyết "Chính sách, hàm giá trị và mô hình ở mức trực quan (ghi chú Bài 01, Mục 4)" sửa thành dẫn Định nghĩa 01.11, 01.12 (chính sách và giá trị trên lịch sử) và Định nghĩa 01.14 (mô hình).

### Kiểm tra sau sửa

- `note_check.py`: 22 môi trường bộ đếm chung, 10 ví dụ, 12 bài tập. Không khoảng trống, không trùng, không khối lồng hay khối lạ, không mẫu câu cấm.
- Tham chiếu chéo: kiểm bằng script, mọi "Định nghĩa/Mệnh đề/Nhận xét/Ví dụ/Bài tập 01.k" trỏ đúng loại và số. Ngoại lệ có chủ đích là Bài tập 01.16, thuộc tệp bài tập sau này.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html`: 1600×900 và 390×844 đều 0 lỗi KaTeX, 0 lỗi console, 0 yêu cầu ngoài, không tràn ngang. Đã xem ảnh chụp Ví dụ 01.10 (1600 px) và Tình huống 01.1 (390 px; khối `aligned` cuộn ngang trong `.katex-display`).
- `no-ai-slop` (Edit) tự kiểm lại trên phần đã sửa: đạt.

## Đợt sửa 2026-10-12 — Giai đoạn I: rà lại vòng 2 và sửa (vòng cuối trước commit)

Hai tác tử rà lại chỉ đọc (Opus 5.5, `high`), theo phân công của điều phối viên:
- Vai A (toán): `scratchpad/recheck-01-A.md`, 2 trung bình, 4 nhẹ.
- Vai B (mạch viết): `scratchpad/recheck-01-B.md`, 5 trung bình R1–R5, 11 nhẹ R6–R16.

Không còn phát hiện chặn bàn giao hay nghiêm trọng. Tác tử soạn ghi chú sửa theo quyết định của điều phối viên. Tệp sửa: `materials/lec-01/lecture-note.md` và tệp này. Không sửa SVG. Không commit.

### Rà lại vòng 2: phát hiện và xử lý

| Mã | Mức | Trạng thái | Xử lý |
|---|---|---|---|
| A-1 | trung bình | đã sửa | Bước 2 của Nhận xét 01.19 viết lại đúng câu đề xuất: giả thiết quy nạp trên phân phối đồng thời của $(A_t,R_{t+1},S_{t+1},\dots,A_j,R_{j+1},S_{j+1})$ |
| A-2 | trung bình | đã sửa | Như R1 |
| A-3 | nhẹ | đã sửa | Bài tập 01.5(c) dẫn Định nghĩa 01.12 thay cho Nhận xét 01.13 |
| A-4 | nhẹ | đã sửa | Ví dụ 01.10, "Ba nước còn lại": đường duy nhất O còn có thể hoàn thành là 7–8–9, cần cả ô 7 và ô 9; với $a=7$ đường này đã bị chặn |
| A-5 | nhẹ | đã sửa | Tình huống 01.1, dẫn ngược: "dùng giả thiết 1–3" |
| A-6 | nhẹ | đã sửa | Bảng ký hiệu và Ví dụ 01.7 thêm vế "nhiều nước thắng thì chọn đều" cho $\pi_w$ |
| A (tùy chọn) | — | đã sửa | Gộp vào R2: "với phân phối trạng thái đầu cố định". Phản ví dụ bỏ điều kiện 2 ghi thêm hai giá trị $\frac12$ và $\frac34$ dưới $\pi_u$; đã tính lại tay: $\frac14(1+\frac12+\frac12+1)=\frac34$ |
| R1 | trung bình | đã sửa | Xóa hai tiêu đề lặp "### Mức tính toán hoặc chứng minh" và "### Mức vận dụng" |
| R2 | trung bình | đã sửa | Đoạn trạng thái ẩn sau Định nghĩa 01.12 thay bằng một công thức Bayes $\Pr(S_t=s\mid H_t=h)$; tích $\prod_k\pi(a_k\mid h_k)$ triệt tiêu giữa tử và mẫu, kèm "với phân phối trạng thái đầu cố định" |
| R3 | trung bình | đã sửa | Đoạn đọc hình Mục 5.1 tách thành danh sách bốn ý: ai đi trước, chưa ai thắng, tập hành động hợp lệ, chỉ số bước |
| R4 | trung bình | đã sửa | Câu cuối Nhận xét 01.4: "Trong cách thiết kế truyền thống, mô hình được cho trước và giữ cố định; Học tăng cường có thể học hoặc cập nhật mô hình từ tương tác (Định nghĩa 01.14)." |
| R5 | trung bình | sửa một phần, có lý do | Xem mục "Số từ" bên dưới |
| R6 | nhẹ | đã sửa | Sau Định nghĩa 01.8: "(3.1) cộng các phần thưởng từ $R_{t+1}$ đến $R_T$. $R_{t+1}$ là phần thưởng đầu tiên chịu ảnh hưởng của $A_t$." Dòng B14 của vòng trước đã được sửa lại cho đúng |
| R7 | nhẹ | đã sửa | Bỏ câu "Nếu rác chuyển sang ô 2…" ở đoạn mở Mục 1.4 |
| R8 | nhẹ | đã sửa | Đọc hình ba dạng tín hiệu: thêm "ở khối có giám sát / không giám sát / tăng cường" |
| R9 | nhẹ | đã sửa | Bài tập 01.2(c) thêm "lượt bị cắt sau $L=5$ hành động" |
| R10 | nhẹ | đã sửa | Nhận xét 01.10: "Đây là một giả thuyết mô hình hóa: chưa có chứng minh rằng…" |
| R11 | nhẹ | đã sửa | Thêm câu giải thích ký hiệu: "Viết O4 cho "O đánh ô 4"" |
| R12 | nhẹ | đã sửa | Mở chương: "Bài 02 bổ sung hệ số chiết khấu và giả thiết đó, gọi là tính Markov" |
| R13 | nhẹ | đã sửa | Gạch Nhận xét 01.6 đổi thành "Dữ liệu không độc lập, không cùng phân phối"; chú "(independent and identically distributed, i.i.d.)" chuyển lên phần tiên quyết |
| R14 | nhẹ | đã sửa | Mở Mục 3 bỏ vế lặp kết Mục 2 |
| R15 | nhẹ | đã sửa | Câu so sánh với học có giám sát sau Định nghĩa 01.1 tách thành đoạn riêng |
| R16 | nhẹ | đã sửa | Đổi tiêu đề thành "Nhận xét 01.6 (Bốn khác biệt của Học tăng cường)", cập nhật tóm tắt |

### Cắt độ dài theo quyết định

- Chuyển Bài tập 01.11 cũ (Giá trị khi mọi thứ tất định) sang `exercises.md`. Nguyên văn đề, gợi ý và lời giải chép ở cuối mục này.
- Bỏ Bài tập 01.2(d) (sinh viên so với lời giải mẫu); (e) cũ thành (d).
- E2: rút đoạn i.i.d. trong Nhận xét 01.6 còn một câu; định nghĩa i.i.d. chuyển lên phần tiên quyết.
- E3: rút "Điều kiện áp dụng" của Mệnh đề 01.20 còn một câu.
- E4: bỏ câu (d) của Bài tập 01.12 cũ (thăm dò).
- E5: bỏ câu (c) của Bài tập 01.9 (phần thưởng 0 và giá trị).
- Không làm E6 (giữ ba hình) và E7 (giữ Bài tập 01.8); không gọt bản đồ chủ đề.

### Đánh số lại bài tập

| Cũ | Mới |
|---|---|
| Bài tập 01.1–01.10 | giữ |
| Bài tập 01.11 (Giá trị khi mọi thứ tất định) | chuyển sang `exercises.md`, đề nghị số 01.12 |
| Bài tập 01.12 (Bàn tay robot xoay khối) | Bài tập 01.11 |
| Bài tập 01.13–01.16 (kế hoạch C, `exercises.md`) | giữ |

Bộ đếm Bài tập trong ghi chú liên tục từ 01.1 đến 01.11. Bộ đếm chung (22) và Ví dụ 01.1–01.10 không đổi.

### Số từ

- Trước vòng này: 21 037 (`wc -w`). Sau: 20 474.
- Vẫn vượt đích ≤ 20 000 khoảng 470 từ. Theo quyết định, không cắt thêm. Lý do vượt:
  - Vòng này thêm khoảng 300 từ theo yêu cầu: công thức Bayes và câu dẫn (R2), danh sách bốn ý (R3), câu giải thích ký hiệu nước đi cùng hai giá trị $\frac12$, $\frac34$ (R11, A-2), giả thiết quy nạp đầy đủ (A-1).
  - Phần còn lại là các mục được giữ theo danh sách "Không cắt" và quyết định không làm E6, E7.

### `no-ai-slop` (Edit) và kiểm tra

- Tự kiểm theo `eval.md` trên mọi đoạn đã đổi: không câu hỏi tu từ, không "hãy", không tài liệu làm chủ ngữ, không tương phản nhị phân mới, không câu kết châm ngôn; danh sách mới (R3) là các ý song song. Đạt.
- `note_check.py`: 22 môi trường bộ đếm chung, 10 ví dụ, 11 bài tập; không khoảng trống, không trùng, không lồng khối, không mẫu câu cấm.
- Tham chiếu chéo kiểm bằng script: chỉ "Bài tập 01.16" không khớp, đúng như ngoại lệ có chủ đích.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html`: 1600×900 và 390×844 đều 0 lỗi KaTeX, 69 khối, 0 lỗi console, 0 yêu cầu ngoài, không tràn ngang.
- `git diff --check` sạch.

### Nguyên văn Bài tập 01.11 cũ (chuyển sang `exercises.md`, đề nghị số 01.12)

::: exercise Bài tập 01.11 (Giá trị khi mọi thứ tất định)
Giả sử môi trường tất định, tức là với mỗi lịch sử và hành động, phần thưởng kế tiếp, quan sát kế tiếp và việc lượt có kết thúc hay không được xác định duy nhất, và chính sách $\pi$ tất định. Cho một lịch sử $h$ đến bước $t$.

- (a) Chứng minh rằng từ $h$, lượt có đúng một diễn biến tiếp theo, và $v_\pi(h)$ bằng lợi tức $G_t$ của diễn biến đó.
- (b) Áp dụng cho robot dọn dãy bốn ô: robot bắt đầu ở ô 1, chỉ ô 4 có rác; $\text{trái}$, $\text{phải}$ dịch một ô, đứng yên nếu đi ra ngoài dãy; hút ở ô 4 khi còn rác cho $+1$ và kết thúc lượt, mọi bước khác cho $0$; cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$; $L=5$. Chính sách $\pi_1$: thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$. Lịch sử $h=(\text{sạch},\text{phải},0,\text{sạch},\text{hút},0,\text{sạch})$.
:::

::: hint
Chứng minh câu (a) theo từng bước: nếu diễn biến đến bước $j$ là duy nhất, thì hành động và phản hồi ở bước $j$ cũng duy nhất.
:::

::: solution
**Câu (a).** Lập luận theo bước $j=t,t+1,\dots$.

**Bước 1 (một bước duy nhất).** Giả sử lịch sử đến bước $j$ được xác định duy nhất, là $h_j$; với $j=t$ thì $h_t=h$. Vì $\pi$ tất định, $A_j$ là hành động duy nhất mà $\pi(\cdot\mid h_j)$ gán xác suất $1$. Vì môi trường tất định, $R_{j+1}$, $O_{j+1}$ và việc kết thúc được xác định duy nhất từ $h_j$ và $A_j$. Do đó lịch sử đến bước $j+1$ cũng duy nhất.

**Bước 2 (cả diễn biến duy nhất).** Lượt kết thúc sau nhiều nhất $L$ bước, nên sau hữu hạn lần áp dụng Bước 1, cả diễn biến từ $h$ đến khi kết thúc là duy nhất, với một lợi tức $g$ xác định.

**Bước 3 (kỳ vọng của một hằng số).** Dưới điều kiện $H_t=h$, $G_t$ nhận giá trị $g$ với xác suất $1$, nên $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]=g$. $\square$

**Câu (b).** Theo $h$, robot sang ô 2 ở bước $0$ rồi hút tại ô 2 sạch, nên ở bước $2$ robot đứng ở ô 2 và còn ba hành động. Theo $\pi_1$, robot sang phải tới ô 3, sang phải tới ô 4, rồi thấy $\text{bẩn}$ và hút ở hành động thứ năm: $R_3=R_4=0$, $R_5=+1$, $T=5\le L$. Vậy $G_2=1$ và $v_{\pi_1}(h)=1$.

**Kiểm tra lại.** Tổng số hành động của lượt là $2+3=5$, đúng bằng $L$, nên lần hút cuối vẫn kịp trước khi lượt bị cắt.
:::

## Đợt sửa 2026-10-12 — Giai đoạn II: bộ trang chiếu

### Tác tử và phạm vi

- Vai: tác tử soạn deck Bài 01 (viết tệp), theo brief `brief_deck_writer.md` của điều phối viên; loại `general-purpose`, mô hình Opus 5.5 (`claude-opus-5-5`), mức `high` theo brief (điều phối viên ghi bằng chứng từ lệnh gọi công cụ). Không commit, không push.
- Tệp ghi: `lecture-01-gioi-thieu-hoc-tang-cuong.html` (viết lại toàn bộ), `planning/lec-01/outline.md`, `storyboard.md` (viết lại), mục này của `review-log.md`; SVG trong `img/lec-01/` (bảng dưới). Không sửa ghi chú bài giảng, `lecture-slide.css`, `index.html`, viewer, tệp bài khác.
- Đã đọc: `quyet-dinh-chuan-2026-10-12.md`, `revision-plan-2026-10-12.md` (A, D), `AGENTS.md` (các mục brief nêu), `CLAUDE.md`, ghi chú `e860f53`, các mục giai đoạn I của nhật ký này, deck cũ, `lecture-slide.css`, deck mẫu math-4-AI Bài 07 (mở đầu, trang tiêu đề mạch, mạch kết luận), `no-ai-slop` (`SKILL.md`, `eval.md`).

### Cấu trúc mới

- 7 mạch, 69 trang (cũ: 42 trang, 7 `<section>` ngoài kèm phụ lục). Trang tiêu đề mạch AT, CT, DT, ET, GT, ZT (`id` `mach-2` … `mach-7`); mạch E và F cũ gộp thành mạch 5.
- Mạch mở đầu: P00 (câu luận đề), P01a "Tiên quyết và quy ước", P01 (6 mục tiêu theo ghi chú), P02 "Nội dung" (7 dòng), P03 "Vấn đề trung tâm".
- Mạch kết luận: ZT, Z01–Z01b (bảng tổng kết tách hai trang), Z02–Z02b (bài tổng hợp có lời giải), Z03 (kết luận có điều kiện, "Nguồn:"), H04 "Câu hỏi tự kiểm tra", Z00 (bảng `Mạch | Bài tập`, tài liệu đọc, liên kết viewer ghi chú, dòng nối Bài 02).
- Bỏ khối `<style>` cục bộ (`font-size:.84em`, `.reveal table{font-size:.82em}`, hệ lớp `.box/.card/.grid2/.check` riêng); dùng `class="reveal lecture-deck"` của `lecture-slide.css` như deck 02–07. Thêm `scrollActivationWidth:null` vào `Reveal.initialize` (như deck 02) để khung 390 px vẫn là chế độ trình chiếu, không chuyển sang chế độ cuộn; các thiết lập bắt buộc khác giữ nguyên.
- Số hiệu kết quả theo ghi chú `e860f53` (bộ đếm chung 01.1–01.22, Ví dụ 01.1–01.10, Bài tập 01.1–01.11), chỉ ghi trong ghi chú diễn giả, tối đa một lần mỗi trang; danh sách trong `outline.md`.

### Bảng mã trang cũ → mới

| Cũ | Mới |
|---|---|
| P00, P01, P02 | giữ mã, sửa nội dung |
| — | thêm P01a, P03 |
| A00 | giữ mã, đổi thành "Robot dọn dãy bốn ô" |
| A01 | giữ mã; phần trạng thái, quan sát tách sang A01c |
| A02 | bỏ, gộp vào A03 |
| A03, A04 | giữ mã, sửa |
| B00 | bỏ |
| B01, B02 | gộp thành B01 "Ví dụ: AlphaGo và thao tác robot" |
| C00 | giữ mã, đổi thành "Phần thưởng và nhãn", mang hình của C02 |
| C01 | giữ mã, đổi thành ví dụ đổi thứ tự; định nghĩa sang C04b |
| C02 | bỏ (hình lên C00) |
| C03, C04 | gộp thành C03 |
| C05 | giữ mã, thành "Bài tập: nhận dạng tín hiệu học" |
| D00–D03 | giữ mã, sửa |
| E00, E01, E02 | giữ mã; E01 tách thành E01 và E01b |
| F00, F01 | giữ mã; F01 gộp F01 và F02 cũ |
| F02 | mã dùng lại cho trang Nhận xét 01.17 (nội dung khác trang "Khai thác" cũ) |
| F03 | giữ mã, thành "Bài tập: chọn chế độ hút" |
| G00–G04 | giữ mã, sửa; công thức chọn nước của G03 cũ sang G03d |
| H04 | giữ mã, thành "Câu hỏi tự kiểm tra"; gộp H05 |
| H05, H06, H07 | bỏ (H06–H07 thành Bài tập 01.16 [Tìm hiểu]) |
| Z00 | giữ mã, thành "Bài tập về nhà và tài liệu đọc" |
| H00–H03 | bỏ: phụ lục thông tin tổ chức của bản nguồn tháng 02/2026 chưa được xác nhận cho học kỳ này, nhãn "Phụ lục:" ngoài danh sách cho phép, H03 có chỉ dẫn giảng viên (quyết định chung §8) |
| — | thêm AT, A00b, A01c, A01d, A05, A06, CT, C04b, C04c, C06, DT, D02b, D02c, D03b, D04, D05, ET, E00b, E01b, E03, E04, E02a, F00b, F04, GT, G02b, G02c, G03b, G03c, G03d, G05, ZT, Z01, Z01b, Z02, Z02b, Z03 |

### Mật độ (`density.py`)

| | Trước | Sau |
|---|---:|---:|
| Số trang | 42 | 69 |
| Âm tiết trung bình | 40,5 | 49,7 |
| Trang > 40 âm tiết | 20 | 55 |
| Trang > 60 âm tiết | 7 | 1 (P01, 77, trần 80 của trang mục tiêu) |
| Dòng `<-- VƯỢT` | 23 | 2 (P01; P02 7 dòng), cả hai có ngoại lệ trong `storyboard.md` |

Deck cũ đạt trung bình thấp hơn nhờ CSS thu chữ và ít nội dung hơn; deck mới không thu chữ, nhưng 55 trang vẫn trên đích 40 (dấu câu sau công thức bị đếm là token). Đây là chỗ cần rà soát sinh viên đo lại.

### SVG

| Tệp | Thao tác |
|---|---|
| `tictactoe-search.svg` | vẽ lại: gốc là thế cờ $s$, đủ bốn nhánh $a=3,6,7,9$, ô vừa đánh đóng khung đứt nét, nước 9 thắng, ba nước trả lời của O dưới mỗi nhánh còn lại; chữ ≥ 25 đơn vị |
| `robot-manipulation.svg` | mới: gộp hai hình nội dòng của B02 cũ (gắp và sắp xếp; đổi tư thế vật), giữ nguyên hình học |
| `agent-environment.svg` | sửa bố cục: nhãn "quan sát, phần thưởng" đè lên khối, chuyển xuống dưới; thêm phông Arial; nội dung không đổi |
| `control-learning.svg` | sửa: nhãn "dữ liệu cập nhật quyết định" tràn khung, tách hai dòng |
| `explore-exploit.svg` | sửa: chữ tràn ra ngoài hai vòng tròn, phóng to vòng tròn |
| `uncertainty.svg` | sửa: chỉ một trong ba mũi tên có đầu mũi tên (marker trên đường gộp), tách ba đường; chữ "trạng thái" tràn khỏi vòng tròn |

Không còn dùng trong deck: `tictactoe-value.svg` (chỉ ba nhánh, nhãn $V^\pi$; thay bằng bảng G03), `rl-fields.svg` (ghi chú đã bỏ ở giai đoạn I), `chapter-map.svg` và `tictactoe-four-moves.svg` (ghi chú dùng; chữ quá nhỏ ở khung trang chiếu nên deck dùng bảng). Không xóa tệp nào. Đề nghị điều phối viên xóa `tictactoe-value.svg` và `rl-fields.svg`; `course-map.svg` vẫn được `index.html` dùng.

### Sai lệch so với kế hoạch A và lý do

- 69 trang thay vì khoảng 58: mỗi cụm có trang lời giải riêng trên mặt trang (A06, C06, D05, E04, F04, G05, Z02b) và các định nghĩa dài được tách để không thu chữ. Vẫn trong khoảng 60–70 của quyết định chung §5.
- P01 có 6 mục tiêu theo ghi chú `e860f53`, không 5 như A2. P03 không đặt `agent-environment.svg`: sáu dòng đã kín khung.
- A02 gộp vào A03 thay vì sửa riêng; B01 và B02 gộp một trang; C02 bỏ, hình lên C00; C03 gộp C04; C00 dùng một ví dụ dẫn nhập (nhãn và phần thưởng ở ô 1) thay vì ba, vì ba tình huống ảnh và học tập trùng Bài tập 01.2.
- Lượt "phải, phải, phải, hút" đặt ở A00b (mạch 2, theo Ví dụ 01.1 của ghi chú) thay vì D00; D00 gộp vấn đề, trực giác, ví dụ tổng còn lại (Ví dụ 01.3).
- Thêm E02a (Ví dụ 01.8 mô hình đúng và sai) theo ghi chú; A3 chỉ có một dòng ví dụ ở E02.
- G03b là Mệnh đề 01.20 (phân tích một bước), G03d là nước khai thác một bước (A3 đặt nước khai thác ở G03b và chưa có trang mệnh đề); G03c mới cho $v_{\pi_u}(s)=\frac12$.
- Bảng tổng kết tách Z01 và Z01b; bỏ hàng giả thuyết phần thưởng (là giả thuyết, không phải kết quả; ghi trong ghi chú diễn giả Z01).
- Bài tổng hợp Z02 đổi dữ kiện so với A2 và kế hoạch C (robot từ ô 2, $L=3$, $\pi_u$; (a) $S_0$, $O_0$; (b) $G_t$ ngược; (c) $v_{\pi_u}(h_0)=\frac1{27}$; (d) nước khai thác một bước tại $h_0$ là phải). Lý do: dữ kiện A2 (ô 1, $L=5$, $\pi_1$) trùng Ví dụ 01.1 và Bài tập 01.5(c), câu (c) có giá trị hiển nhiên $1$. Đã tính tay: chỉ dãy phải, phải, hút thành công, $(\frac13)^3=\frac1{27}$; sau trái (ô 1, còn 2 hành động) và sau hút (ô 2, còn 2) giá trị $0$, sau phải (ô 3, còn 2) giá trị $(\frac13)^2=\frac19$; kiểm $\frac13(0+\frac19+0)=\frac1{27}$. `exercises.md` (giai đoạn III) cần dùng cùng dữ kiện cho Bài tập 01.13 và dẫn tới Z02, Z02b.
- Z00 dùng bảng `Mạch | Bài tập` xoay ngang (hai dòng) để giữ ≤ 6 dòng. Bài tập 01.12–01.16 là số hiệu dự kiến của `exercises.md` (01.12 giá trị khi tất định, theo nhật ký giai đoạn I; 01.13 tổng hợp; 01.14, 01.15, 01.16 theo kế hoạch C). Liên kết "Bài tập" trên Z00 chưa đặt vì tệp chưa có; giai đoạn III thêm "· Bài tập" vào dòng liên kết.
- Tên hành động và quan sát viết ngoài KaTeX trên deck (ghi chú dùng `\text{…}`): `\text{sạch}`, `\text{bẩn}` làm KaTeX cảnh báo "No character metrics" với ký tự ạ, ẩ.

### Đề nghị sửa ghi chú

Không có mâu thuẫn số liệu giữa deck và ghi chú. Mọi số trên deck đã tính lại: Ví dụ 01.4 ($0{,}7$; $0{,}8$; $0{,}9$; $1$; $0$), Ví dụ 01.7 ($0$ và $1$), Ví dụ 01.9 ($[0{,}367;\,0{,}700]$, $[\frac{12}{21},\frac{13}{21}]$), Ví dụ 01.10 (bảng 9 dòng, kỳ vọng $\frac13,0,\frac23,1$; X thắng $\frac23$, O thắng $\frac16$, hòa $\frac16$, $v_{\pi_u}(s)=\frac12$), Bài tập 01.3, 01.5, 01.6, 01.7.

### Đề nghị cho `lecture-slide.css`

- `.reveal.lecture-deck table{font-size:.9em}` trong khi section đã `.8em`: chữ trong bảng là $0{,}72$em của cỡ gốc (30,24 px trên khung 1280), dưới mức $0{,}75$em của `AGENTS.md`. Đề nghị đặt bảng `1em` (tương đối section) hoặc ghi ngoại lệ chung. Không sửa trong đợt này.

### Tự kiểm `no-ai-slop` (Edit) và `eval.md`

- Phạm vi: mọi tiêu đề, mặt trang và ghi chú diễn giả của deck.
- Đã bỏ: lời chỉ đường và lời quy trình ("phần E", "Tiếp theo:", "Trang này", "Đáp án", "bản chuyển đổi"), câu hỏi không nhãn, nhãn ngoài danh sách ("Ghi nhớ:", "Chi phí:", "Rủi ro:", "Bài toán:", "Ví dụ giả định:", "Ba dấu hiệu:", "Phụ lục:"), URL trong ghi chú, câu điều hướng "Hai trang sau…", câu "dự kiến mang số" trong ghi chú Z02, tương phản nhị phân "không là nhãn" trên P03.
- Đối chiếu `eval.md`: không từ cấm, không câu hỏi tu từ, không mở ghi chú bằng "Trang này" hay tài liệu làm chủ ngữ, không câu kết châm ngôn, không "chúng ta", "ta thấy", "rõ ràng", "hãy" trên deck. Giữ có chủ đích: câu "Nhầm lẫn thường gặp là…" trong nhiều ghi chú (chức năng học tập), các dòng "X: kết luận" dạng mệnh đề có điều kiện ở P03, Z03. Kết quả: đạt.
- Ghi chú diễn giả: 40–150 âm tiết ở 63/69 trang; sáu trang 151–163 âm tiết (P03, E02, G03, G03b, G03d, Z00), mức `nhẹ`; G03b là trang mệnh đề.
- `quill` (Outline, Concept, Threads làm bảng kiểm): mỗi ký hiệu xuất hiện trên mặt trang sau trang định nghĩa hoặc dòng "Ký hiệu:" của P01a ($\pi_1$ được nêu lại ở E03; $\sigma$ ở G02 trước G02c); luồng robot mở ở A00, đóng ở Z02b; luồng thế cờ $s$ mở ở E00, đóng ở G03d và Z03.

### Kiểm trình duyệt

- Script Playwright Chromium trong scratchpad (`d01/check_deck.py`), cổng 8766, chặn yêu cầu `api-reloadserver` để trang không tự tải lại khi tác tử khác ghi tệp, tắt hiệu ứng chuyển trang khi đo.
- 1600×900 và 390×844, đủ 69 trang (`Reveal.slide(h,v,99)`): 0 lỗi và 0 cảnh báo console, 0 lỗi trang, 0 `.katex-error`, 0 yêu cầu ra ngoài localhost, 0 yêu cầu hỏng, không tràn ngang; mọi phần tử nằm trong khung 1280×720 (so `getBoundingClientRect` với `.reveal .slides`). Số trên sáu trang tiêu đề mạch khớp "Nội dung" và chỉ số ngang (`mach-N` ở `#/N`). Phím mũi tên phải chuyển trang. Mọi `src`, `href` cục bộ tồn tại.
- Đã xem ảnh chụp mọi trang ở 1600 px (bảng ghép `d01/all0.png` … `all6.png`) và các trang tiêu đề mạch, Z01, Z01b, G01 ở 390 px; ảnh lưu tại scratchpad `d01/shots/`.
- `git diff --check`: sạch.

## Rà soát năm vai và biên tập (giai đoạn II)

### Tác tử

- Năm tác tử rà soát chỉ đọc (Opus 5.5, `high`, theo phân công của điều phối viên): SV (góc nhìn sinh viên, đo mật độ), RL (chuyên gia), TOAN (toán và thuật toán), PB (phản biện sư phạm, `no-ai-slop` Detect), MACH (kết nối và mạch). Báo cáo: `scratchpad/deckrev-01-{SV,RL,TOAN,PB,MACH}.md`.
- Biên tập viên: chính tác tử soạn deck (Opus 5.5, `high`, `general-purpose`), theo brief `brief_deck_editor.md` và quyết định của điều phối viên. Không commit.
- Kết quả rà: 0 chặn; 1 nghiêm trọng (RL-1); trung bình: RL 5, TOAN 3, SV 6, PB 13, MACH 7 (nhiều mục trùng nhau giữa các vai).
- Thư mục scratchpad của phiên không còn dùng được giữa vòng này; script kiểm và ảnh chụp của vòng biên tập nằm ở `~/.cache/rl01edit/` (ngoài kho).

### Bảng phát hiện và xử lý

| Mã | Trang | Mức | Trạng thái |
|---|---|---|---|
| RL-1 | G03d, mạch 6 | nghiêm trọng | đã sửa: thêm G03e "Học giá trị thế cờ từ các ván đã chơi", vẽ lại Hình 1.1 (nguồn tr. 30) thành `tictactoe-learning.svg`; F02 đổi thành ứng dụng trên Tic-tac-toe nối sang G03e; Z03 ghi chú thêm giới hạn thứ tư; GT dòng dẫn mới |
| RL-2 | C04b | trung bình | đã sửa: dòng "Hai đặc trưng: thử và sai (trial-and-error) và phản hồi trễ" |
| RL-3 | G00, G02, E00, G04, G05 | trung bình | đã sửa: "phiên X", "số nước X đã đi"; "lượt" chỉ cho episode, cả trong ghi chú diễn giả và SVG cây trò chơi |
| RL-4 | D02c | trung bình | đã sửa: $L=4$ trên mặt trang, diễn giải so với hút trước (lợi tức lớn nhất $0$) |
| RL-5 | A04 | trung bình | đã sửa: dãy hành động cố định, luật ngẫu nhiên chưa biết; ghi chú nêu quy hoạch động Bài 04 |
| RL-6 | storyboard | trung bình | đã sửa: phút theo cụm; C05–C06, D04–D05, G04–G05 vào khối 30 phút; mạch 6 lên 26 phút |
| RL-7 | P01a | nhẹ | đã sửa: bỏ "không giả thiết Markov" khỏi mặt trang; ghi chú nêu tính Markov của quan sát |
| RL-8 | P03 | nhẹ | đã sửa: "kỳ vọng" ở dòng 6 |
| RL-9 | E02 | nhẹ | đã sửa |
| RL-10 | B01 | nhẹ | đã sửa: ghi chú "lập kế hoạch bằng tìm kiếm cây trên luật cờ"; mặt trang "Khi phần thưởng chỉ đặt ở bước cuối" |
| RL-11 | G03d | nhẹ | đã sửa: "$\gamma\lt1$ hoặc khi mọi lượt kết thúc" |
| RL-12 | Z01 | nhẹ | đã sửa: "lượt hữu hạn; $G_T=0$"; ghi chú nêu dạng có chiết khấu |
| RL-13 | thuật ngữ | nhẹ | đã sửa: episode, reward, policy, return ở P01a; greedy ở F01; TD ở ghi chú D02b |
| RL-14 | E01b, G03d | nhẹ | đã sửa: câu dự đoán (prediction) ở ghi chú E01b, điều khiển (control) ở ghi chú G03d |
| RL-15 | E01 | nhẹ | đã sửa theo brief mục 5: "chính sách xác định (deterministic policy)" |
| RL-16 | Z00 | nhẹ | đã sửa theo brief mục 4 |
| RL-17 | số hiệu trong ghi chú | nhẹ | đã sửa: mỗi trang một số hiệu kết quả; danh sách trong outline cập nhật |
| TOAN-1 | D02c | trung bình | đã sửa (như RL-4) |
| TOAN-2 | G03d, Z02 | trung bình | đã sửa: "Giả thiết: ba điều kiện rút gọn", "Dạng khác:" trên lịch sử; Z02(d) "dạng trên lịch sử" |
| TOAN-3 | P03, Z01b, Z03 | trung bình | đã sửa: "quan sát đầy đủ, O và $\pi$ theo thế cờ" |
| TOAN-4 | G03b | nhẹ | đã sửa: ghi chú nêu trường hợp $\pi(a\mid h)=0$ |
| TOAN-5 | F00b, F02 | nhẹ | đã sửa: "không đổi được quyết định, vì $\frac{12}{21}\approx0{,}571>0{,}55$" |
| TOAN-6 | F00b, F04 | nhẹ | đã sửa: $\big[\frac{11}{30},\frac7{10}\big]\approx[0{,}367;\,0{,}700]$ |
| TOAN-7 | Z01 hàng 1 | nhẹ | đã sửa: "không giả thiết quan sát đầy đủ" |
| TOAN-8 | G03d | nhẹ | đã sửa (như RL-11) |
| TOAN-9 | E02a | nhẹ | đã sửa: M2 dự báo $\widehat R_3=1$ trên mặt trang |
| TOAN-10 | Z01, Z01b | nhẹ | đã sửa: tên cột thống nhất; số hiệu bỏ khỏi ghi chú Z01 |
| SV-1 | B01 | trung bình | đã sửa: bỏ `.card` |
| SV-2 | "lượt" | trung bình | đã sửa (như RL-3) |
| SV-3 | G03d, Z02, Z01b | trung bình | đã sửa (như TOAN-2, TOAN-3) |
| SV-4 | A05, A06 | trung bình | đã sửa theo Bài tập 01.1 |
| SV-5 | G02 | trung bình | đã sửa: định nghĩa $\tilde s$ |
| SV-6 | A04, B01 (SVG) | trung bình | đã sửa: `uncertainty.svg` chữ 36–44, `robot-manipulation.svg` chữ 50; A04 đưa hình ra hàng riêng |
| SV-7 | A03, F02, A01, C00 (SVG) | nhẹ | đã sửa A03, F02 (chữ 32–38, hình ra hàng riêng); A01, C00 giữ (0,53–0,58em; hình dùng chung với ghi chú, ghi chú bài giảng hiển thị lớn) |
| SV-8 | P01a | nhẹ | đã sửa |
| SV-9 | P03 | nhẹ | đã sửa: "Chính sách chọn, giá trị đánh giá" thay ký hiệu |
| SV-10 | A00 | nhẹ | đã sửa: bỏ dòng mặt trang lặp hình (không sửa SVG vì ghi chú dùng chung) |
| SV-11 | E00b | nhẹ | đã sửa |
| SV-12 | F00 | nhẹ | đã sửa |
| SV-13 | E02a | nhẹ | đã sửa |
| SV-14 | Z01, Z01b | nhẹ | đã sửa: cột thống nhất, công thức nhóm trong `{…}` để không ngắt, dòng viết tắt $h,a$ |
| SV-15 | G03 | nhẹ | đã sửa: `\dfrac` ở cột kỳ vọng |
| SV-16 | H04 câu 1 | nhẹ | đã sửa |
| SV-17 | "bước thứ tư" | nhẹ | đã sửa: $R_4$ |
| SV-18 | ghi chú dài | nhẹ | đã sửa: mọi ghi chú 40–150 âm tiết sau rút gọn |
| SV-19 | storyboard | nhẹ | đã sửa (như RL-6) |
| PB-1 | G03 | trung bình | đã sửa: "Nhu cầu:" |
| PB-2 | G04–G05 | trung bình | đã sửa: H04 câu 3 kiểm nước khai thác với $\pi_w$ |
| PB-3 | "lượt" | trung bình | đã sửa (như RL-3) |
| PB-4 | D02c | trung bình | đã sửa (như RL-4) |
| PB-5 | C00 | trung bình | đã sửa theo quyết định điều phối viên; trường hợp hai lần trái vào ghi chú |
| PB-6 | E00b, E01b | trung bình | đã sửa: cầu nối trong ghi chú E01b |
| PB-7 | F00 | trung bình | đã sửa |
| PB-8 | D00 | trung bình | đã sửa: dòng $1=0+1$, $1=1+0$ |
| PB-9 | Z02, G03d | trung bình | đã sửa (như TOAN-2) |
| PB-10 | G02, G02c | trung bình | đã sửa (như SV-5) |
| PB-11 | G01 | trung bình | đã sửa: hai dòng mới |
| PB-12 | P01a | trung bình | đã sửa |
| PB-13 | ghi chú trang tiêu đề mạch | trung bình | đã sửa: sáu ghi chú viết lại, mở bằng đối tượng kế thừa, đổi khuôn câu |
| PB-14 | A04 | nhẹ | đã sửa |
| PB-15 | AT | nhẹ | đã sửa (MACH 3.1a) |
| PB-16 | GT | nhẹ | đã sửa (MACH 3.4) |
| PB-17 | P03 | nhẹ | đã sửa |
| PB-18 | E00 | nhẹ | đã sửa: quy tắc viết bằng lời, tên đặt ở E01 |
| PB-19 | E02 | nhẹ | đã sửa |
| PB-20 | D02b | nhẹ | đã sửa |
| PB-21 | D01, C04b | nhẹ | từ chối một phần: tiếng Anh đã gom ở P01a; D01 là định nghĩa chính thức nên không đổi thành "Nhắc lại:" |
| PB-22 | A00b | nhẹ | đã sửa |
| PB-23 | C05(d) | nhẹ | đã sửa |
| PB-24 | A03 | nhẹ | đã sửa |
| PB-25 | G02b | nhẹ | đã sửa |
| PB-26 | Z01, Z01b | nhẹ | đã sửa |
| PB-27 | H04 | nhẹ | đã sửa: câu 3 về $\pi_w$ (theo MACH 3.5 thay cho đề xuất "O đổi cách chơi"; chọn vì kiểm kết quả chính của mạch 6) |
| PB-28 | Z03 | nhẹ | đã sửa (Z03 viết lại song song P03) |
| PB-29 | D03 | nhẹ | đã sửa |
| PB-30 | E04 | nhẹ | đã sửa |
| PB-31 | ghi chú P01, P03, A00, G03, Z01, F02, C03 | nhẹ | đã sửa; lý do thiết kế chuyển sang storyboard |
| PB-32 | A05, A06 | nhẹ | đã sửa (như SV-4) |
| MACH-3.1 | AT, A00, A03 | trung bình | đã sửa (a)–(d) |
| MACH-3.2 | ET, F00 | trung bình | đã sửa |
| MACH-3.3 | F02 | trung bình | đã sửa: ứng dụng trên Tic-tac-toe |
| MACH-3.4 | GT | trung bình | đã sửa (rút còn 20 âm tiết) |
| MACH-3.5 | G04–G05, H04 | trung bình | đã sửa: dời G04–G05 lên sau G02c; H04 câu 3 |
| MACH-3.6 | Z03, G03d | trung bình | đã sửa: G03e và giới hạn thứ tư trong ghi chú Z03 |
| MACH-3.7 | Z01b, Z02 | trung bình | đã sửa |
| MACH-3.8 | P03, Z03, Z01 | trung bình | đã sửa: Z03 năm dòng 2–6 song song P03; Z01 thêm hàng ba dạng tín hiệu học |
| MACH-3.9 | D04–D05 | nhẹ | đã sửa |
| MACH-3.10 | C00 | nhẹ | đã sửa |
| MACH-3.11 | E02a | nhẹ | đã sửa |
| MACH-3.12 | G00 | nhẹ | đã sửa |
| MACH-3.13 | G01 | nhẹ | đã sửa |
| MACH-3.14 | H04 câu 2, 3 | nhẹ | đã sửa: câu 2 nối mạch 2 và 4 (trái ở bước 0: $T=5$, $G_0=1$) |
| MACH-3.15 | P03 | nhẹ | đã sửa dòng 3; vế "dữ liệu do chính hành động sinh ra" không thêm vào khung vì trần 60 |
| MACH-3.16 | Z01 | nhẹ | đã sửa |
| MACH-3.17 | Z00 | nhẹ | không còn áp dụng: bảng chỉ ghi bài tập đã có (brief mục 4) |

### Trang đổi, thêm, dời

- Thêm: G03e. Sửa mặt trang: P01a, P03, AT, A00, A00b, A03, A04, A05, A06, B01, C00, C04b, C04c, C05, D00, D02b, D02c, D03, ET, E00, E01, E00b, E03, E04, E02a, E02, F00, F00b, F01, F02, F04, GT, G00, G01, G02, G02b, G03, G03d, Z01, Z01b, Z02, Z03, H04, Z00, G04, G05. Chỉ sửa ghi chú: P01, CT, DT, ZT, C03, E01b, G03b.
- Dời: A05–A06 lên sau A01d; D04–D05 lên sau D02c; G04–G05 lên sau G02c.
- SVG: mới `tictactoe-learning.svg`; sửa `uncertainty.svg`, `robot-manipulation.svg`, `control-learning.svg`, `explore-exploit.svg` (chữ lớn hơn), `tictactoe-search.svg` ("đến phiên X").

### Đề nghị sửa ghi chú (sau giai đoạn II)

| Vị trí trong ghi chú | Nội dung sửa | Nguồn |
|---|---|---|
| Ví dụ 01.4 | Đặt $L=4$ (deck D02c đã đổi); "Diễn giải" so với hút trước, lợi tức lớn nhất $0$. Với $L=5$, hút trước rồi đi đúng đường cũng cho $0{,}7$ | RL, TOAN, PB 4 |
| §5.1, Định nghĩa 01.18, Ví dụ 01.6, 01.7, 01.10, Bài tập 01.7 | "lượt của X / đến lượt X" thành "nước đi / phiên của X"; "lượt" chỉ cho episode | RL, SV, PB 3 |
| Định nghĩa 01.5 hoặc Nhận xét 01.6 | Thêm "thử và sai (trial-and-error)" cùng phản hồi trễ | RL |
| Nhận xét 01.4, ý 3 | Tách kế hoạch vòng hở khỏi chính sách phản hồi khi đã biết luật ngẫu nhiên (Bài 04) | RL |
| §4.2 sau Ví dụ 01.7 | Câu giải thích vì sao giá trị chỉ phụ thuộc thế cờ trong ví dụ ($\pi_u,\pi_w$ không nhớ nước trước, nước cuối của O bị buộc), dẫn tới Nhận xét 01.19 | PB 6 |
| Đầu §4.4 | Cầu nối sang bài toán chọn lặp lại một bước, giá trị của $a$ là kỳ vọng phần thưởng một bước | PB 7 |
| Nhận xét 01.17 | "gần như không đổi được quyết định" thành "không đổi được quyết định ($\frac{12}{21}>0{,}55$)" | TOAN |
| Bài tập 01.6, "Kiểm tra lại" | Khoảng viết $\approx[0{,}367;\,0{,}700]$ hoặc $\big[\frac{11}{30},\frac7{10}\big]$ | TOAN |
| Đoạn sau Ví dụ 01.1, đoạn mở §1 (dòng 143) | "chỉ phần thưởng $+1$ ở cuối lượt phân biệt được" mâu thuẫn trường hợp một lần trái; nêu trường hợp hai lần trái hoặc nói rõ $R_4$ | PB 5 |
| Chính sách tất định | "chính sách tất định" thành "chính sách xác định (deterministic policy)" theo brief mục 5 | biên tập viên |

### Số hiệu dự kiến cho `exercises.md` (giai đoạn III)

01.12 giá trị khi môi trường và chính sách tất định (nguyên văn trong mục giai đoạn I); 01.13 bài tổng hợp robot từ ô 2, $L=3$, $\pi_u$, đúng dữ kiện và lời giải Z02–Z02b; 01.14 hai thiết kế phần thưởng robot dọn nhà; 01.15 đăng ký môn học hoặc xe tự hành (mạch 3 và 5); 01.16 [Tìm hiểu] tác tử nhiều nhiệm vụ và mô hình thế giới. Z00 chỉ ghi "Tệp bài tập: chưa có".

### Mật độ sau biên tập

70 trang; trung bình 51,0 âm tiết; 57 trang trên 40; 1 trang trên 60 (P01, 77, trần 80); dòng `<-- VƯỢT`: P01 và P02, đều có ngoại lệ.

### `no-ai-slop` (Edit) và kiểm tra

- Tự kiểm theo `eval.md` trên mọi mặt trang và ghi chú đã đổi: không "Trang này", không tài liệu làm chủ ngữ (sáu ghi chú trang tiêu đề mạch mở bằng đối tượng kế thừa, khuôn câu khác nhau), không lời điều hướng ("hai trang sau" đã bỏ), không câu kết châm ngôn (E04 kết bằng số), không tương phản nhị phân mới. Đạt.
- `density.py`: 0 dòng vượt không có ngoại lệ. Playwright 1600×900 và 390×844, 70 trang: 0 lỗi và 0 cảnh báo console (kể cả KaTeX), 0 `.katex-error`, 0 yêu cầu ra ngoài, 0 tài nguyên hỏng, không tràn ngang; chỉ báo vượt khung ở E02 là các `span` khung đỡ (`pstrut`, `svg-align`) của `\widehat`, không hiển thị (đã kiểm từng lớp, ảnh chụp sạch). Số trên trang tiêu đề mạch khớp `#/N`. Đã xem ảnh chụp mọi trang đổi ở 1600 px và G03e, A04 ở 390 px (`~/.cache/rl01edit/shots/`, bảng ghép `c0.png`–`c6.png`).
- `git diff --check`: sạch.

## Rà lại vòng 2 và sửa (giai đoạn II, trước commit)

Hai tác tử rà lại chỉ đọc (Opus 5.5, `high`): TOAN (`scratchpad/deckrecheck-01-TOAN.md`: 1 trung bình, 5 nhẹ) và MACH (`scratchpad/deckrecheck-01-MACH.md`: 2 trung bình R1–R2, 8 nhẹ R3–R10). Không còn chặn hay nghiêm trọng. Biên tập viên (cùng tác tử, Opus 5.5 `high`) sửa theo quyết định của điều phối viên. Không commit.

| Mã | Trang | Mức | Trạng thái |
|---|---|---|---|
| TOAN-H04 | H04 câu 2 | trung bình | đã sửa: "Từ ô 1, $L=5$, phần thưởng gốc: …; tính $T,\ G_0$" |
| TOAN-G03d | G03d | nhẹ | đã sửa: "Dạng khác: trên lịch sử, không cần ba điều kiện: thay $s,S_{t+1},\mathcal A(s)$ bằng $h,H_{t+1},\mathcal A(h)$" |
| TOAN-G03e | G03e ghi chú | nhẹ | đã sửa: a, c, e, g là thế cờ dạng $\tilde s$, trạng thái sau nước đi (afterstate) |
| TOAN-F02 | F02 | nhẹ | đã sửa: tiêu chí thăm dò là nước không dẫn tới giá trị ước lượng cao nhất; gộp với R9: "thế cờ chưa thử có thể không bao giờ được thử" |
| TOAN-F04 | F04 ghi chú | nhẹ | đã sửa: $\big[\tfrac{11}{30},\tfrac7{10}\big]$ |
| TOAN-D02c | D02c ghi chú | nhẹ | đã sửa: "mọi $G_t$ với $t\lt T$" |
| R1 | G02b–G03, G00 | trung bình | đã sửa: thứ tự G02b → G04 → G05 → G02c → G03; G03 nêu lại thế cờ $s$ ngay trong dòng "Nhu cầu:" (gộp với "Nhắc lại:" để giữ 6 dòng cùng bảng 5 hàng); G00 đổi tiêu đề "Ví dụ: thế cờ bốn ô trống"; storyboard ghi G02c là cầu nối vào cụm phân tích một bước |
| R2 | storyboard | trung bình | đã sửa: G03c bỏ khỏi danh sách có thể bỏ; F02 giữ trong danh sách; ghi chú G03e có "(phần 5)" |
| R3 | Z03 dòng 2–3 | nhẹ | đã sửa theo đề xuất; dòng Nguồn rút; Z03 còn 60 âm tiết |
| R4 | ghi chú P02, P03 | nhẹ | đã sửa: thêm câu về học giá trị thế cờ từ các ván đã chơi |
| R5 | D03 ghi chú | nhẹ | đã sửa: "Ví dụ chi phí di chuyển và bài tập va ghế cho thấy…" |
| R6 | C06 ghi chú | nhẹ | đã sửa: "ba trong bốn khác biệt của Học tăng cường" |
| R7 | G03e ghi chú | nhẹ | đã sửa theo câu đề xuất |
| R8 | GT | nhẹ | đã sửa: từ khóa "Mô hình hóa · Cây trò chơi · Phân tích một bước · Khai thác · Học từ ván chơi" (rút "Nước khai thác một bước" thành "Khai thác" để dòng ≤ 20 âm tiết) |
| R9 | F02 | nhẹ | đã sửa (gộp với TOAN-F02) |
| R10 | G04 ghi chú, `tictactoe-search.svg` | nhẹ | đã sửa: "phiên đi", "đến phiên X" trong `<desc>` |

Đề nghị sửa ghi chú bổ sung (thêm vào bảng "Đề nghị sửa ghi chú (sau giai đoạn II)"):

| Vị trí trong ghi chú | Nội dung sửa | Nguồn |
|---|---|---|
| `img/lec-01/tictactoe-four-moves.svg` (chỉ ghi chú dùng) | "thế cờ s, đến lượt X" và "X chọn đều ở các lượt sau" thành "phiên"; sửa cả `<desc>` và alt trong ghi chú | MACH rà lại |
| Ví dụ 01.9 | Tùy chọn: "dịch trung bình của A tối đa $\frac1{21}$" viết thành "trung bình mới của A thuộc $[\frac{12}{21},\frac{13}{21}]$, rộng $\frac1{21}$", như F00b | TOAN rà lại |

Kiểm tra sau sửa:
- `density.py`: chỉ P01 và P02 vượt, đều có ngoại lệ trong storyboard; Z03, H04 ở 60 âm tiết.
- `scratchpad/deck_check.py` (cổng 8799), 70 trang ở 1600×900 và 390×844: 0 lỗi, 0 cảnh báo console, 0 `.katex-error`, 0 yêu cầu ngoài, 0 yêu cầu hỏng, không cuộn ngang, đủ 6 trang tiêu đề mạch. Cờ `overflow` (P01a, D02, G03b, G03d) và `small_font` là báo động giả của các `span` KaTeX ẩn, như vai SV đã kiểm ở vòng trước; ảnh chụp các trang này sạch.
- Ghi chú diễn giả: mọi trang 40–150 âm tiết.
- Đã xem ảnh 1600 px của G00, G04, G02c, G03, G03d, G03e, F02, Z03, H04, GT (`scratchpad/ed01r2/shots/`, bảng ghép `scratchpad/ed01r2/s1.png`).
- `git diff --check`: sạch.

### Quyết định của điều phối viên (2026-10-12, giai đoạn II, deck)

- Tác tử: tác tử soạn kiêm biên tập (general-purpose, claude-opus-5-5, high) hai vòng; rà lại toán và rà lại mạch (general-purpose, claude-opus-5-5, high, chỉ đọc); điều phối viên Claude Fable 5.1 (medium).
- Kiểm độc lập của điều phối viên sau vòng 2: `density.py` chỉ gắn cờ các trang có lý do trong `storyboard.md`; Playwright 1600×900 và 390×844: 0 lỗi console, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, đủ 6 trang tiêu đề mạch; ảnh các trang đổi ở vòng 2 đã xem; `git diff --check` sạch.
- Quyết định: **chấp nhận**; commit `fix(lecture-01)`.

## Đợt sửa 2026-10-14 — Sửa ghi chú sau giai đoạn II

### Tác tử và phạm vi

- Vai: tác tử biên tập ghi chú bài giảng Bài 01 (viết tệp), theo `brief_note_revision.md` của điều phối viên. Loại `general-purpose`; mô hình Opus 5.5 (`claude-opus-5-5`), mức `high` theo brief. Không commit, không push.
- Danh sách việc: mười dòng của bảng "Đề nghị sửa ghi chú (sau giai đoạn II)" và hai dòng "Đề nghị sửa ghi chú bổ sung" của mục "Rà lại vòng 2 và sửa (giai đoạn II, trước commit)". Bản đối chiếu: deck đã commit (D02c, C04b, A04, E00b, E01b, F00, F00b, F04, E01, G00, G02, G04).
- Tệp sửa: `materials/lec-01/lecture-note.md`; `img/lec-01/tictactoe-four-moves.svg` (chỉ ghi chú dùng; deck không tham chiếu tệp này); mục này của nhật ký. Không sửa deck, outline, storyboard, `exercises.md`, `index.html`.
- Số hiệu không đổi: bộ đếm chung 01.1–01.22, Ví dụ 01.1–01.10, Bài tập 01.1–01.11, Tình huống 01.1–01.2; mọi `note-topic-id` giữ nguyên.

### Từng đề nghị và xử lý

Số dòng là số dòng trong ghi chú sau đợt sửa.

| Đề nghị | Trạng thái | Vị trí mới và nội dung |
|---|---|---|
| Ví dụ 01.4: $L=4$, so với hút trước | đã sửa | Dòng 466: "$L=4$". Dòng 478 (Diễn giải): hút ở ô 1 cho $0>-0{,}1$, nhưng ba hành động còn lại không đủ để tới ô 4 rồi hút và mỗi lần di chuyển chỉ thêm $-0{,}1$, nên lợi tức lớn nhất khi hút trước là $0<0{,}7$; câu cuối nêu với $L=5$ thì hút rồi đi đúng đường cũng cho $0+3\cdot(-0{,}1)+1=0{,}7$, nên so sánh cần $L=4$; thêm vế "với cách đặt của Ví dụ 01.3, mọi $G_t$ với $t<T$ bằng $1$" như ghi chú diễn giả D02c. |
| "lượt" của X thành "nước đi"/"phiên" | đã sửa | Dòng 570 (Ví dụ 01.6): "luân phiên đặt"; định nghĩa "nước đi (move)", "đến phiên (turn)" ở lần dùng đầu. Dòng 607 (Ví dụ 01.7), 813 (tiêu đề Mục 5.1 "Thế cờ, phiên đi và tập hành động hợp lệ"), 815 ("Mỗi nước đi của X vì vậy là một bước, còn cả ván cờ là một lượt"), 821, 824 và 829 ("đếm số nước X đã đi", như G00, G02), 831, 840, 845 (Định nghĩa 01.18 và đoạn sau), 883 (Ví dụ 01.10), 921 (alt hình), 1017 và 1027 (Bài tập 01.7), 1037 và 1072 (Bài tập 01.8, "ở nước sau"). Sau sửa, "lượt" trong ghi chú chỉ dùng cho episode; "lần lượt" chỉ còn ở hai câu về robot, nghĩa trạng từ. |
| Thử và sai (trial-and-error) cùng phản hồi trễ | đã sửa | Dòng 332, đoạn sau Định nghĩa 01.5: "Bài giảng gốc (2025–2026, trang 17) và Sutton và Barto (2018, §1.1) nêu hai đặc trưng phân biệt Học tăng cường: thử và sai (trial-and-error) … và phản hồi trễ …". Đặt ở đoạn đọc định nghĩa, không trong khối định nghĩa, vì đây là đặc trưng, không phải điều kiện của định nghĩa. Đã kiểm văn bản trang 17 của PPTX nguồn ("Two characteristics: Trial-and-errors and Delay-outcome"). |
| Nhận xét 01.4, ý 3: tách kế hoạch vòng hở khỏi chính sách phản hồi | đã sửa | Dòng 254: kế hoạch vòng hở (open-loop plan), tức dãy hành động định sẵn, không phản ứng được với kết quả thực; nếu luật ngẫu nhiên đã biết, một chính sách phản hồi (Định nghĩa 01.11), tính bằng quy hoạch động ở Bài 04, xử lý được mà không cần học; việc học cần khi luật chưa biết hoặc thay đổi. Khớp ghi chú diễn giả A04. |
| §4.2 sau Ví dụ 01.7: vì sao giá trị chỉ phụ thuộc thế cờ | đã sửa | Dòng 645, sau đoạn đọc Định nghĩa 01.12 (đặt sau định nghĩa để đối số "lịch sử" đã có tên): $\pi_u$, $\pi_w$ chỉ dùng thế cờ hiện tại, không nhớ các nước trước, và nước cuối của O bị buộc; dẫn Nhận xét 01.19 ở Mục 5.2. Khớp ghi chú diễn giả E01b. |
| Đầu §4.4: cầu nối sang bài toán chọn lặp lại một bước | đã sửa | Dòng 731: giá trị ở Mục 4.2 và lập kế hoạch ở Mục 4.3 dùng luật đã biết; tác tử phi mô hình chỉ có mẫu; bài toán chọn lặp lại một bước có mỗi lượt một hành động, nên lợi tức bằng phần thưởng một bước và giá trị của $a$ là kỳ vọng phần thưởng khi chọn $a$. Khớp F00. |
| Nhận xét 01.17: "không đổi được quyết định" | đã sửa | Dòng 773: "không đổi được quyết định, vì trung bình mới của A ít nhất $\frac{12}{21}\approx0{,}571>0{,}55$". |
| Bài tập 01.6, "Kiểm tra lại": viết khoảng chính xác | đã sửa | Dòng 803: $\big[\frac{11}{30},\frac7{10}\big]\approx[0{,}367;\,0{,}700]$. |
| Mâu thuẫn "chỉ phần thưởng $+1$ ở cuối lượt phân biệt được" | đã sửa | Dòng 143: "phần thưởng $+1$ nhận sau hành động thứ tư; nếu robot sang trái hai lần ở đầu lượt, ba hành động còn lại không đủ để tới ô 4 và hút, và phần thưởng đó không đến". Dòng 176: với một lần $\text{trái}$, $+1$ đến muộn một bước ($R_5$ thay cho $R_4$), tổng phần thưởng vẫn bằng $1$; chỉ với hai lần $\text{trái}$, tổng bằng $0$. Bỏ vế mâu thuẫn. |
| "Chính sách tất định" thành "chính sách xác định (deterministic policy)" | đã sửa | Dòng 597 (Định nghĩa 01.11) và 600 (hai chỗ). Kéo theo: hai chỗ "tất định" nói về môi trường ở Tình huống 01.1 (dòng 1090, 1092) đổi thành "không ngẫu nhiên", để một thuật ngữ tiếng Anh không ứng với hai từ tiếng Việt trong cùng chương; deck không dùng "tất định". |
| `tictactoe-four-moves.svg`: "lượt" thành "phiên" | đã sửa | Nhãn "thế cờ s, đến phiên X", dòng chân "X chọn đều ở các phiên sau", `<desc>` sửa cùng; alt trong ghi chú (dòng 921) sửa cùng. SVG còn là XML hợp lệ (ElementTree). Chiều dài dòng chân không đổi số ký tự đáng kể ("lượt" → "phiên"). |
| Ví dụ 01.9: khoảng của A thay cho "dịch tối đa $\frac1{21}$" | đã sửa | Dòng 747: thêm một lần thử A với $r\in[0,1]$ cho $\frac{12+r}{21}\in\big[\frac{12}{21},\frac{13}{21}\big]\approx[0{,}571;\,0{,}619]$, rộng $\frac1{21}<0{,}05$, nằm hoàn toàn trên $0{,}55$ của B, như F00b. Kéo theo trong cùng câu: khoảng của B viết $\big[\frac{11}{30},\frac7{10}\big]$ như F00b và Bài tập 01.6; "vượt quá $0{,}60$ của A" đổi thành "chứa $0{,}60$ của A" (khoảng chứa $0{,}60$, không nằm trên nó). |

Không từ chối đề nghị nào.

### Số liệu đã tính lại

- Ví dụ 01.4 ($L=4$): $(R_1,\dots,R_4)=(-0{,}1;-0{,}1;-0{,}1;1)$, $G_4=0$, $G_3=1$, $G_2=0{,}9$, $G_1=0{,}8$, $G_0=0{,}7$; $T=4\le L$. Hút ở bước $0$ rồi ba hành động: tới ô 4 cần ba lần $\text{phải}$, không còn hành động để hút, mọi phần thưởng còn lại thuộc $\{0,-0{,}1\}$, nên lợi tức lớn nhất $0$ (ba lần hút). Với $L=5$: $0-0{,}3+1=0{,}7$.
- Ví dụ 01.1 với một lần $\text{trái}$: $(R_1,\dots,R_5)=(0,0,0,0,1)$, $T=5$, tổng $1$; hai lần $\text{trái}$: còn ba hành động, cần bốn, tổng $0$.
- Ví dụ 01.9: $\frac{1{,}1}{3}=\frac{11}{30}\approx0{,}3667$, $\frac{2{,}1}{3}=\frac7{10}$, độ rộng $\frac13>0{,}33$; $\frac{12}{21}\approx0{,}5714$, $\frac{13}{21}\approx0{,}6190$, độ rộng $\frac1{21}\approx0{,}0476<0{,}05$; $0{,}5714>0{,}55$, nên A vẫn tham lam sau một lần thử A bất kỳ.
- Bài tập 01.6: $\frac23\approx0{,}667$ và $0{,}50$ đều thuộc $\big[\frac{11}{30},\frac7{10}\big]$.

### Số từ

- `wc -w`: trước 20 474 (HEAD), sau 20 886 (+412). Phần thêm đều do danh sách đề nghị: Nhận xét 01.4 ý 3, đoạn thử và sai, câu cầu nối sau Định nghĩa 01.12, câu mở Mục 4.4, Diễn giải Ví dụ 01.4, hai trường hợp sang trái ở dòng 143 và 176, khoảng của A ở Ví dụ 01.9. Đã rút gọn các đoạn thêm một lượt sau bản nháp đầu (bản nháp đầu 21 017). Vẫn vượt mức thường gặp 20 000 khoảng 890 từ; theo quyết định ở đợt trước, không cắt thêm nội dung khác.

### `no-ai-slop` (Edit) và kiểm tra

- Phạm vi: mọi câu đã thêm hoặc sửa trong ghi chú, nhãn và `<desc>` của `tictactoe-four-moves.svg`. Đối chiếu `eval.md`: không câu hỏi tu từ, không "hãy", không tài liệu làm chủ ngữ, không lời quy trình; không tương phản nhị phân mới; đã bỏ một dấu hai chấm kiểu "tiết lộ" ở Diễn giải Ví dụ 01.4 ("so sánh này mất tác dụng: …") thành câu thường có "nên"; dấu hai chấm còn lại dẫn danh sách hoặc phép tính. Không thêm nhận định không có nguồn: hai đặc trưng dẫn trang 17 nguồn và Sutton và Barto §1.1; quy hoạch động dẫn Bài 04 như ghi chú diễn giả A04. Kết quả: đạt.
- `note_check.py`: 22 môi trường bộ đếm chung, 10 ví dụ, 11 bài tập, không khoảng trống, không trùng; 0 dấu `\(`/`\[`.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html` (viewer cổng 8766, server có cwd `/data/tqlong/rl-plan`): 1600×900 và 390×844 đều 0 `.katex-error`, 69 khối, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, không tràn ngang.
- `git diff --check`: sạch. Tệp của đợt này trong `git diff --stat`: `materials/lec-01/lecture-note.md`, `img/lec-01/tictactoe-four-moves.svg`, `planning/lec-01/review-log.md`. Cây làm việc còn thay đổi chưa commit ở tệp của các bài khác (ghi chú, nhật ký, SVG của Bài 02–06) không do đợt này tạo; không đụng tới.
- Sau đợt này, hai "lệch tạm thời" ghi ở `outline.md` (dòng 152: $L=4$ ở D02c; "phiên"/"nước đi") đã hết lệch về phía ghi chú; dòng đó trong `outline.md` nằm ngoài phạm vi ghi của đợt này, đề nghị điều phối viên cập nhật.

### Rà lại sau đợt sửa và sửa bổ sung

- Tác tử rà lại: vai rà lại toán và nhất quán, chỉ đọc; `general-purpose`, `claude-opus-5-5`, `high` (báo cáo `scratchpad/noterecheck-01.md`). Kết quả: 0 chặn, 0 nghiêm trọng, 2 trung bình, 7 nhẹ. Mọi số liệu của đợt sửa đã được tính lại và khớp deck.
- Biên tập viên (cùng tác tử của đợt sửa, Opus 5.5, `high`) sửa theo quyết định của điều phối viên; điều phối viên cho phép sửa riêng một dòng ngoài phạm vi là `outline.md` dòng 152.

| Phát hiện | Mức | Trạng thái |
|---|---|---|
| Dòng 176, câu đầu: "quyết định quan sát kế tiếp" sai, vì cả hai trường hợp đều cho $O_1=\text{sạch}$ | trung bình | đã sửa: "… quyết định vị trí và các quan sát về sau: sau ba hành động, $O_3$ là $\text{sạch}$ (ô 3) thay vì $\text{bẩn}$ (ô 4)" (kiểm: trái, phải, phải đưa robot tới ô 3) |
| `outline.md` dòng 152, dòng "Lệch tạm thời" đã cũ | trung bình | đã sửa: "Đã khớp với ghi chú (2026-10-14) …" |
| Dòng 176, câu mới: chữ "chỉ" nói quá (phải, trái, … cũng cho tổng $0$) | nhẹ | đã sửa: "với hai lần $\text{trái}$ ở đầu lượt, tổng phần thưởng của lượt bằng $0$" |
| Dòng 645: khối của tài liệu làm chủ ngữ | nhẹ | đã sửa: "Trong Ví dụ 01.7, giá trị được ghi theo thế cờ $s'$ …; điều kiện tổng quát có ở Nhận xét 01.19 (Mục 5.2)." |
| Dòng 1090: "không ngẫu nhiên" như thể là điều kiện của Mệnh đề 01.20 | nhẹ | đã sửa: "Luật của môi trường cố định (ở đây còn không ngẫu nhiên), nên …" |
| Dòng 332: vế giải thích thử và sai lặp câu trước; trích dẫn bài giảng gốc lặp hai lần liền nhau | nhẹ | đã sửa: "Theo bài giảng gốc (2025–2026, trang 17) và Sutton và Barto (2018, §1.1), hai đặc trưng … là thử và sai (trial-and-error), như vừa mô tả, và phản hồi trễ …"; câu sau mở bằng "Trang 9 của bài giảng gốc mô tả …" |
| Dòng 143: "nước đi" lần đầu chưa có "(move)" | nhẹ | đã sửa: thêm "(move)" ở dòng 143, bỏ "(move)" lặp ở dòng 570 ("(turn)" vẫn ở dòng 570) |
| Dòng 600: "xác định" hai nghĩa trong hai câu liền nhau | nhẹ | không sửa (tùy chọn theo điều phối viên): câu khớp ghi chú diễn giả E01 |
| Số từ 20 886 vượt mức thường gặp | nhẹ | giữ quyết định cũ, không cắt |

Kiểm tra sau sửa bổ sung: `wc -w` 20 900; `note_check.py` bộ đếm 22/10/11, không khoảng trống, không trùng, 0 `\(`/`\[`; `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html` (cổng 8766) ở 1600×900 và 390×844: 0 lỗi KaTeX, 69 khối, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, không tràn ngang; `git diff --check` sạch. `no-ai-slop` (Edit) trên các câu đổi: không tài liệu làm chủ ngữ, không câu lặp ý, dấu hai chấm ở dòng 176 dẫn một ví dụ cụ thể có số liệu. Đạt.

### Quyết định của điều phối viên (2026-10-14, sửa ghi chú sau giai đoạn II)

- Kiểm độc lập: `note_check.py` sạch; viewer cổng 8766 ở 1600×900 và 390×844: 0 lỗi KaTeX, 69 khối, 0 lỗi console, không tải ngoài; SVG `tictactoe-four-moves.svg` là XML hợp lệ; `git diff --check` sạch. Rà lại toán (Opus 5.5 high, chỉ đọc): 2 trung bình, 7 nhẹ, đã sửa (dòng 600 giữ theo deck).
- Quyết định: **chấp nhận**; commit `fix(materials-01)`.

## Đợt sửa 2026-10-12 — Giai đoạn III: bài tập

### Tác tử và phạm vi

- Vai: tác tử soạn `exercises.md` Bài 01 (viết tệp), theo `brief_exercises_writer.md` của điều phối viên, kể cả mục "Bổ sung 2026-10-14". Loại `general-purpose`; mô hình Opus 5.5 (`claude-opus-5-5`), mức `high` theo brief. Không commit, không push.
- Tệp tạo: `materials/lec-01/exercises.md` (538 dòng, khoảng 9 700 từ). Tệp sửa: mục này của nhật ký. Không tạo SVG mới. Không sửa ghi chú, deck, outline, storyboard, `index.html`.
- Bản đối chiếu: ghi chú và deck ở HEAD (`b8ee716`, `d9a6283`); kế hoạch C trong `revision-plan-2026-10-12.md`; nguyên văn Bài tập 01.11 cũ trong mục "Giai đoạn I: rà lại vòng 2"; số hiệu dự kiến trong mục "Số hiệu dự kiến cho `exercises.md` (giai đoạn III)".
- Không có phiếu hw01 trong `RL-hk2-2025-2026/resources/`; mọi bài dựa trên ghi chú, bài giảng gốc (PPTX bài 1, chỉ đọc văn bản trang 8, 14–15, 20, 24–25, 43–44) và Sutton và Barto (2018) §3.2, §3.3, §8.1, §17.1 (trang in kiểm trên `extracted.md`: PDF − 22).

### Danh sách bài

| Số hiệu | Mức | Mạch | Nguồn | Mục tiêu (ghi chú) | Trùng deck |
|---|---|---|---|---|---|
| 01.1 | nhận biết | 2 | ghi chú §1.3 | 1 | A05 `#/2/7`, A06 `#/2/8` |
| 01.2 | nhận biết | 3 | ghi chú §2.2; nguồn tr. 20 | 2 | C05 `#/3/7`, C06 `#/3/8` |
| 01.6 | nhận biết, tính toán | 5 | ghi chú §4.4 | 5 | F03 `#/5/14`, F04 `#/5/15` |
| 01.7 | nhận biết | 6 | ghi chú §5.1; nguồn tr. 28–30 | 6 | G04 `#/6/6`, G05 `#/6/7` |
| 01.3 | tính toán | 4 | ghi chú §3.2–3.3 | 3 | D04 `#/4/7`, D05 `#/4/8` |
| 01.4 | chứng minh, tính toán | 4 | ghi chú §3.3 | 3 | không |
| 01.5 | tính toán | 5 | ghi chú §4.2 | 4 | E03 `#/5/6`, E04 `#/5/7` |
| 01.8 | tính toán | 6 | ghi chú §5.4 | 6 | không |
| 01.12 | chứng minh, tính toán | 5 | Bài tập 01.11 cũ của ghi chú (nhật ký giai đoạn I) | 4 | không |
| 01.13 | vận dụng | 7 | ghi chú Mệnh đề 01.20, Tình huống 01.1 | 1, 3, 4 | Z02 `#/7/4`, Z02b `#/7/5` |
| 01.14 | vận dụng | 4 | nguồn tr. 24–25; Sutton và Barto §3.2 tr. 53–54; Ví dụ 01.5 | 3 | không |
| 01.15 | vận dụng | 3, 5 | nguồn tr. 8, 25; Nhận xét 01.4, 01.6; Mệnh đề 01.20 | 1, 2, 4, 5 | không |
| 01.16 | vận dụng, [Tìm hiểu] | 7 | nguồn tr. 14–15, 43–44; Sutton và Barto §8.1 tr. 159–160, §17.1 tr. 459–460 | 1, 4 | không |

Mỗi mức có ít nhất bốn bài; mọi mục tiêu 1–6 có ít nhất hai bài trong tệp. Bài tập 01.9–01.11 (mục "Bài tập củng cố" của ghi chú) không chép lại; `note_check.py` vì vậy báo khoảng trống 9, 10, 11, đúng chủ đích.

Liên kết: bảy liên kết `#/N/1` tới trang tiêu đề mạch và mười bốn liên kết trùng trang chiếu đã mở bằng Playwright (cổng 8799) và đọc `data-slide-id` của trang hiện hành; tất cả đúng (P00, AT, CT, DT, ET, GT, ZT; A05/A06, C05/C06, D04/D05, E03/E04, F03/F04, G04/G05, Z02/Z02b).

### Thay đổi so với bản trong ghi chú (01.1–01.8) và so với nguyên văn 01.12

- Đề bài 01.1–01.8, gợi ý và các câu (a)–(c) của lời giải giữ nguyên chữ; kết quả không đổi. Thêm để đề tự chứa: tên ba dạng học ở 01.2; bảng số liệu ở 01.6 (đúng bảng F03); luật luân phiên và thắng ở 01.7; công thức (3.1), (3.2) ở 01.3, 01.4; biểu thức (5.3) ở 01.8; "(Định nghĩa 01.16)" ở lời giải 01.6(a). Gợi ý 01.7 thêm "Đếm quân của mỗi bên để biết phiên đi" (như ghi chú diễn giả G04).
- Mọi "Kiểm tra lại" thêm lỗi thường gặp kèm kết quả sai mà lỗi dẫn tới, lấy từ ghi chú diễn giả của deck khi có (A06, C06, D05, E04, F04, G05, Z02b).
- 01.12: đổi "môi trường tất định" thành "môi trường không ngẫu nhiên" và "chính sách tất định" thành "chính sách xác định (deterministic policy)" theo đợt sửa ghi chú 2026-10-14; tiêu đề đổi thành "Giá trị khi môi trường không ngẫu nhiên và chính sách xác định"; câu (b) thêm yêu cầu "Tính $v_{\pi_1}(h)$" và "hút làm sạch ô đang đứng"; lời giải (b) nêu rõ "theo câu (a)", "ở bước 1". Kết quả $v_{\pi_1}(h)=1$ không đổi.

### Sai lệch so với kế hoạch C và lý do

- 01.12 không có trong bảng kế hoạch C; được thêm theo quyết định ở giai đoạn I (chuyển từ ghi chú) và số hiệu dự kiến của giai đoạn II.
- 01.13 dùng dữ kiện Z02 (robot từ ô 2, $L=3$, $\pi_u$), không phải "robot dãy bốn ô (a)–(d)" của A2, theo quyết định giai đoạn II.
- 01.14: kế hoạch ghi "phạt đổ đồ"; Ví dụ 01.5 của ghi chú đã có thiết kế phạt bình hoa, nên bài dùng thiết kế đó làm D1 và thêm thiết kế D2 thưởng $b=0{,}2$ cho mỗi lần hút (mục tiêu con), có cơ sở ở Sutton và Barto §3.2 (thưởng cho mục tiêu con có thể làm tác tử đạt mục tiêu con mà bỏ mục tiêu thật). Ba lượt thay cho hai để có một lượt không hút rác.
- 01.15 chọn đăng ký môn học (không chọn xe tự hành), có phần tính: hai lớp, hai đợt, xác suất $0{,}4$ và $0{,}8$, phần thưởng $1$ và $0{,}6$; nối với "hy sinh phần thưởng tức thời" (nguồn tr. 25, ví dụ "Take a course").
- 01.16: thêm phần tính (a)–(c) trên hai nhiệm vụ N1, N2 của robot để bài tìm hiểu có ví dụ kiểm được; lời giải (d) là dàn ý tham khảo, mỗi ý kèm căn cứ; câu hỏi trí tuệ nhân tạo tổng quát được nêu là câu hỏi mở, không kết luận thay người học.
- Tệp xếp theo ba mức (theo brief), không theo mạch như sản phẩm mẫu math-4-AI 07; bảng `Mạch | Mở phần | Bài tập` cho ánh xạ theo mạch.

### Số liệu đã tính lại

Tính bằng script trong `/tmp/claude-1000/ex01/calc.py` (phân số chính xác, duyệt mọi dãy hành động).

- 01.13: dãy thành công duy nhất $\text{phải},\text{phải},\text{hút}$; $v_{\pi_u}(h_0)=\frac1{27}$; giá trị sau $\text{trái}$, $\text{phải}$, $\text{hút}$: $0$, $\frac19$, $0$; $\frac13(0+\frac19+0)=\frac1{27}$. Khớp Z02b.
- 01.14 ($L=5$): D1: $\tau_1$ $G_0=1$, $\tau_2$ $0$, $\tau_3$ $0$; D2: $1{,}2$; $0{,}4$; $1{,}0$; $\tau_2$ dưới D2 ngược: $0;1{,}2;1{,}2;1{,}2;0{,}4;0{,}4$. Cực đại D1 $=1$; cực đại D2 $=1{,}4$, đạt đúng bởi $\text{hút},\text{phải},\text{phải},\text{phải},\text{hút}$ và $\text{phải},\text{phải},\text{hút},\text{phải},\text{hút}$; không hút rác tối đa $1{,}0$. $L=10$ (duyệt $3^{10}$ dãy): cực đại $2{,}4$, không hút rác tối đa $2{,}0$.
- 01.15: $\mathbb E[R_1\mid\mathrm M]=0{,}4$, $\mathbb E[R_1\mid\mathrm C]=0{,}48$; $\mathbb E[G_0]$: $(\mathrm M,\mathrm M)=0{,}64$, $(\mathrm M,\mathrm C)=0{,}688$, $(\mathrm C,\mathrm M)=0{,}56$, $(\mathrm C,\mathrm C)=0{,}576$.
- 01.16: P trên N1 $G_0=1$ ($T=4$), trên N2 $0$ ($T=5$); $\pi_1$ trên N1 $1$ ($T=4$), trên N2 $1$ ($T=2$).
- 01.12(b): $G_2=1$, $T=5$; với $L=4$ (lỗi thường gặp) $v=0$.
- Các số của 01.1–01.8 giữ nguyên ghi chú; đã đối chiếu lại với trang lời giải của deck (A06, C06, D05, E04, F04, G05).

### `no-ai-slop` (Edit) và kiểm tra

- Phạm vi: toàn bộ chữ mới (đoạn mở, hướng dẫn, 01.12–01.16, các câu "lỗi thường gặp" thêm vào 01.1–01.8). Đối chiếu `eval.md`: không câu hỏi tu từ, không "hãy", không tài liệu làm chủ ngữ, không lời quy trình, không tương phản nhị phân kiểu "không phải X mà là Y", không câu kết châm ngôn; dấu hai chấm chỉ dẫn danh sách, phép tính hoặc định nghĩa; nhận định về mô hình thế giới dẫn nguồn cụ thể (Sutton và Barto §8.1, §17.1) hoặc nêu là quan điểm có điều kiện. Câu "Hai lỗi thường gặp." lặp ở nhiều bài là nhãn có chức năng theo mẫu, giữ. Kết quả: đạt.
- `note_check.py`: 13 khối `exercise`, 13 `hint`, 13 `solution`; không khối lạ, không lồng; bộ đếm 01.1–01.8, 01.12–01.16, không trùng; khoảng trống 9–11 có chủ đích; mẫu "trang chiếu" chỉ ở các dòng "Trùng trang chiếu" và đoạn mở; 0 dấu `\(`/`\[`.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html exercises` (viewer cổng 8766, server cwd `/data/tqlong/rl-plan`): 1600×900 và 390×844 đều 0 `.katex-error`, 39 khối, 26 khối gập, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, không tràn ngang. Đã xem ảnh chụp đầu tệp (1600) và lời giải 01.14 (390): bảng năm cột của 01.14 cuộn ngang trong khung bảng ở 390 px.
- `git diff --check` (và `git diff --no-index --check` cho tệp mới): sạch. Tệp mới nằm trong danh sách cho phép của `.gitignore` (`!2627-1/materials/**`).

### Đề nghị sửa deck

| Mức | Trang | Vấn đề | Đề xuất |
|---|---|---|---|
| trung bình | Z00 | Bảng mạch–bài tập chỉ có 01.1–01.11, không có cột mạch 7; dòng "Tệp bài tập: chưa có"; ghi chú diễn giả nói 01.1–01.11 | Thêm 01.12, 01.15 vào cột mạch 5 (01.15 cả mạch 3), 01.14 vào mạch 4, thêm cột 7 với 01.13, 01.16; thay "Tệp bài tập: chưa có" bằng liên kết "Ghi chú bài giảng · Bài tập" tới `material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html`; nếu bảng xoay ngang quá rộng, gộp theo dạng "01.12–01.16 (tệp bài tập)" |

### Đề nghị sửa ghi chú

| Mức | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|
| nhẹ | Mục tiêu học tập | Chỉ dẫn Bài tập 01.1–01.11 | Có thể thêm "và tệp bài tập: 01.12–01.16" ở các mục tiêu 1, 3, 4, 5 |
| nhẹ | Bài tập 01.6 (ghi chú) | Đề không có bảng số liệu như F03 | Không bắt buộc; tệp bài tập đã thêm bảng |

### Chỗ cần rà toán soi

- 01.14(b), (c): lập luận chặn trên ($1{,}2+b\cdot$ số hành động thừa) và khẳng định "đạt bởi đúng hai lượt" ($L=5$).
- 01.15(b): công thức $\mathbb E[G_0]=\mathbb E[R_1]+\Pr(\text{thất bại})\,\mathbb E[R_2]$ dựa trên độc lập giữa hai đợt; (c) nối với Mệnh đề 01.20(a).
- 01.16(b): khẳng định P là chính sách xác định chỉ dùng $t$ và $v_{\mathrm P}(h_0)$ bằng lợi tức của lượt duy nhất (môi trường không ngẫu nhiên, theo 01.12).

### Rà soát bài tập (ba vai chỉ đọc) và sửa theo quyết định của điều phối viên

- Tác tử rà soát: TOAN (độ chính xác toán học), SV (góc nhìn sinh viên), PB (sư phạm, `no-ai-slop` Detect); cả ba `general-purpose`, `claude-opus-5-5`, mức `high`, chỉ đọc. Báo cáo: `scratchpad/exrev-01-TOAN.md`, `exrev-01-SV.md`, `exrev-01-PB.md`. Tổng: 0 chặn bàn giao, 0 nghiêm trọng; trung bình: TOAN 3, SV 3 (một thuộc deck), PB 3 (một thuộc deck).
- Biên tập: cùng tác tử soạn (Opus 5.5, `high`), `no-ai-slop` Edit. Tệp sửa: `materials/lec-01/exercises.md` (579 dòng) và mục này. Không commit.

| Mã | Mức | Trạng thái | Xử lý |
|---|---|---|---|
| TOAN-1 | trung bình | đã sửa | 01.15 "Kiểm tra lại": nêu hai giả thiết của đề (xác suất như nhau ở hai đợt, hai đợt độc lập) và ghi Định nghĩa 01.12 không đòi chúng |
| TOAN-2 | trung bình | đã sửa | 01.16(b): N1, N2 không ngẫu nhiên, P xác định (chọn theo $t$ đọc từ độ dài lịch sử), dẫn Bài tập 01.12(a) |
| TOAN-3 = PB | trung bình | đã sửa | 01.16(b): "Nhận xét 01.4, ý thứ nhất: môi trường đổi" |
| SV-1 | trung bình | đã sửa | 01.13: hai đẳng thức thành hai khối display, gọi tên (1), (2); câu (d), (e) dẫn theo tên. Ở 1600 px không còn khối nào cuộn ngang |
| SV-2 | trung bình | đã sửa | 01.16(c): đề ghi rõ rác thật ở ô 2, mô hình ghi nhầm ở ô 3 |
| PB-1 | trung bình | đã sửa | 01.13: giữ dữ kiện, mức và (a)–(d) khớp Z02/Z02b; dòng Nguồn ghi (c), (d) là $w(2,3)$, $w(3,2)$ của Tình huống 01.1; thêm câu (e): ô xuất phát ẩn đồng khả năng 1, 2, 3; kỳ vọng sau trái, phải, hút $0$, $\frac5{27}$, $\frac1{27}$ (cần $w(4,2)=\frac49$); nước khai thác vẫn là phải; kiểm $v_{\pi_u}(h_0)=\frac2{27}$ bằng (2) và bằng trung bình $w(1,3)=0$, $w(2,3)=\frac1{27}$, $w(3,3)=\frac5{27}$ (tính lại bằng script phân số) |
| PB-2 | trung bình | đã sửa | Thêm tên tiếng Anh ở lần đầu: hàm giá trị (value function), hành động tham lam (greedy action), có mô hình (model-based), phi mô hình (model-free) ở mục Hướng dẫn; giả thuyết phần thưởng (reward hypothesis), mục tiêu con (subgoal, thay "việc con") ở 01.14; robot đa năng (general-purpose robot), trí tuệ nhân tạo tổng quát (artificial general intelligence), kế hoạch vòng hở (open-loop plan) ở 01.16. Tên mạch trong bảng giữ đúng deck |
| SV/PB Z00 | trung bình | chuyển | Deck Z00 sửa trong đợt sửa deck riêng (theo quyết định của điều phối viên); đề nghị giữ nguyên như mục "Đề nghị sửa deck" ở trên |
| TOAN 01.4 | nhẹ | đã sửa | Kiểm tra lại: lỗi đếm $m$ phép cộng cho $10$; lỗi riêng của tính ngược (coi $G_{T-1}=R_T+G_T$ là một phép cộng) cho $4$ |
| TOAN 01.12(a) | nhẹ | đã sửa | Bước 3 dẫn cách đọc "phân phối của diễn biến bắt đầu từ $h$", đúng cả khi $\Pr_\pi(H_t=h)=0$ |
| TOAN 01.14(b) | nhẹ | đã sửa | Thêm lý do "đúng hai dãy" (ô 1 trước lần phải đầu; ô 3 giữa lần phải thứ hai và thứ ba) |
| TOAN 01.14(c), SV 01.14(c) | nhẹ | đã sửa | Nêu cận $G_0\le2{,}4$ và cận $2{,}0$ của lượt không hút rác; câu cuối giới hạn cho "lượt chỉ hút ở ô 1" |
| TOAN 01.15(b) | nhẹ | đã sửa | Viết $\mathbb E[R_2\mid A_1=a_1,\ \text{đợt 1 thất bại}]$ và nêu tính độc lập |
| TOAN 01.16(c) | nhẹ | đã sửa | "dãy ngắn nhất có tổng dự báo $1$" |
| TOAN/SV/PB 01.2(d) | nhẹ | đã sửa | Lời giải (d) mở bằng dạng học và tín hiệu, "ba trong bốn khác biệt" (khớp C06) |
| TOAN/SV 01.15 nguồn | nhẹ | đã sửa | Thêm Nhận xét 01.3 vào dòng Nguồn và Tài liệu tham khảo |
| SV 01.8 `\tag` | nhẹ | đã sửa | Bỏ `\tag{5.3}`, câu dẫn ghi "Theo công thức (5.3) của ghi chú" |
| SV 01.14 bảng | nhẹ | đã sửa | Tách hai bảng ba cột (D1, D2), cùng bố cục ba cột Lượt, Phần thưởng, $G_0$ |
| SV 01.1, 01.13 trạng thái | nhẹ | đã sửa | Đề nêu "Trạng thái là cặp (vị trí, tình trạng ô 4)" |
| SV/PB 01.15 $O_0$, "ở mỗi đợt" | nhẹ | đã sửa | Đề nêu $O_0$ là thông báo mở đăng ký và "ở mỗi đợt"; lời giải (a) thêm câu về nghĩa của giả thiết độc lập |
| SV 01.3 va ghế | nhẹ | không sửa | Giữ như ghi chú và D04; đề nghị đồng bộ sau (xem dưới) |
| SV đoạn mở, bảng mạch | nhẹ | đã sửa | Bảng ghi 01.9–01.11 "(chỉ trong ghi chú)" ở mạch 4, 5; đoạn mở nói 01.9–01.11 chỉ trong ghi chú nhưng thuộc bộ bài giao, và thứ tự số hiệu không liên tục vì xếp theo mức |
| SV gợi ý 01.5 | nhẹ | đã sửa | Gợi ý không nêu kết luận câu (a) |
| SV mục lục viewer | nhẹ | ngoài phạm vi | Hạ tầng viewer, ghi cho điều phối viên |
| PB nhịp "Hai lỗi thường gặp." | nhẹ | đã sửa | Bỏ khuôn ở 01.1, 01.3, 01.4, 01.5, 01.6, 01.8, 01.12, 01.13, 01.14, 01.15, 01.16; mỗi lỗi viết thành câu có chủ ngữ và kết quả sai |
| PB nhấn mạnh thiếu căn cứ | nhẹ | đã sửa | 01.5(c) "(Định nghĩa 01.12)"; 01.15(c) "đó là phản hồi trễ (Nhận xét 01.6)"; 01.13 "dù $v_{\pi_u}(h_0)$ chỉ bằng $\frac1{27}$", hai câu diễn giải chuyển từ "Kiểm tra lại" về cuối câu (d) |
| PB 01.16(c) câu khái quát | nhẹ | đã sửa | Vế sai số tích lũy chuyển sang ý 5 của dàn ý (d), dẫn ghi chú Mục 4.3, đoạn "Trong thực hành" |
| PB 01.16(d) ý 6 | nhẹ | đã sửa | "Các định nghĩa và kết quả của Bài 01 không đủ để trả lời…"; không lấy tài liệu làm chủ ngữ |
| PB Nguồn ↔ Tài liệu tham khảo | nhẹ | đã sửa | 01.3, 01.4 thêm Sutton và Barto §3.3 tr. 54–57; 01.8 thêm bài giảng gốc tr. 28–30; §8.1 tr. 159–161 (theo ghi chú); thêm Nhận xét 01.3, Tình huống 01.2, Bài tập 01.9 |
| PB 01.16 trang 14–15, robot hình người | nhẹ | đã sửa | Đề nối N1/N2 với ý trang 15 (khó chuyển từ cờ vua sang cờ vây) và thêm "như robot hình người" (trang 43) |
| PB 01.14(a), 01.16(a) phần đã giải | nhẹ | đã sửa | Dòng Nguồn ghi phần lấy lại Ví dụ 01.5 và Nhận xét 01.4 |
| PB 01.15 trạng thái ẩn | nhẹ | đã sửa | Như dòng SV/PB 01.15 |
| PB 01.6 vị trí | nhẹ | đã sửa | Chuyển 01.6 sang mục "Mức tính toán hoặc chứng minh", sau 01.5; lý do: hai trong ba câu là phép tính; dòng Mức độ ghi lý do. Mức nhận biết còn 01.1, 01.2, 01.7 |
| PB 01.16(d) ý 4 | nhẹ | đã sửa | Bỏ tương phản "không phải một dãy hành động định sẵn", dẫn Nhận xét 01.4, ý thứ ba |

Cảnh báo KaTeX "Unrecognized Unicode character" cho chữ Việt trong `\text{…}` (SV đo 268 cảnh báo, strict mode): chấp nhận như ghi chú bài giảng, chữ hiển thị đúng; không sửa.

Đề nghị sửa ghi chú (bổ sung, nhẹ): (1) Bài tập 01.2(d) của ghi chú mở bằng dạng học và tín hiệu như tệp bài tập; (2) Bài tập 01.5: gợi ý không nêu kết luận, câu (c) bỏ "như Định nghĩa 01.12 ghi rõ"; (3) Bài tập 01.3 (cùng D04): nêu va ghế không cản robot sang ô kế tiếp. Các đổi khác của 01.1–01.8 chỉ ở phần "Kiểm tra lại" và câu dẫn, kết quả không đổi.

Kiểm tra sau sửa: `note_check.py` 13 `exercise`/13 `hint`/13 `solution`, bộ đếm 01.1–01.8, 01.12–01.16, khoảng trống 9–11 có chủ đích, không trùng, 0 `\(`/`\[`; `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html exercises` (cổng 8766) ở 1600×900 và 390×844: 0 `.katex-error`, 39 khối, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, không tràn ngang; ở 1600 px không khối công thức hay bảng nào cuộn ngang, ở 390 px các công thức dài cuộn trong khung như ghi chú. Liên kết: 21 liên kết tới deck mở đúng trang (P00, AT, CT, DT, ET, GT, ZT, A05/A06, C05/C06, D04/D05, E03/E04, F03/F04, G04/G05, Z02/Z02b). `git diff --check` sạch. `no-ai-slop` (Edit) trên mọi câu đổi: không còn khuôn câu lặp, không nhấn mạnh thiếu căn cứ, không tài liệu làm chủ ngữ, không tương phản nhị phân; đạt.

### Quyết định của điều phối viên (2026-10-14, giai đoạn III, bài tập)

- Kiểm độc lập: `note_check.py` sạch (13 bài, mỗi bài có gợi ý và lời giải); viewer cổng 8766 ở 1600×900 và 390×844: 0 lỗi KaTeX, 39 khối, 0 lỗi console, không tải ngoài; `git diff --check` sạch. Ba vai rà soát chỉ đọc (Opus 5.5 high): 0 chặn, 0 nghiêm trọng; mọi mục trung bình đã sửa. Cảnh báo KaTeX chữ Việt trong `\text{}` chấp nhận như ghi chú.
- Quyết định: **chấp nhận**; commit `feat(materials-01)`. Trang Z00 của deck và nhóm "Bài tập" trên `index.html` cập nhật ở đợt sau.

## Đợt sửa 2026-10-14 — Đồng bộ trang bài tập về nhà

### Tác tử và phạm vi

- Vai: biên tập deck Bài 01 (sửa nhỏ, có kiểm), theo `brief_deck_homework_sync.md` của điều phối viên; loại `general-purpose`, mô hình Opus 5.5 (`claude-opus-5-5`), mức `high` theo brief. `no-ai-slop` Edit. Không commit.
- Tệp sửa: `lecture-01-gioi-thieu-hoc-tang-cuong.html` (chỉ trang Z00), `storyboard.md` (dòng Z00, bảng ngoại lệ mật độ, câu trung bình mật độ), `outline.md` (sáu dòng mục tiêu học tập và một dòng ánh xạ Z00), mục này. Không sửa ghi chú, `exercises.md`, `lecture-slide.css`, `index.html`, SVG.
- Đối chiếu: bảng `Mạch | Mở phần | Bài tập` của `materials/lec-01/exercises.md` (commit `e338bea`) và mục "Đề nghị sửa deck" của giai đoạn III.

### Trang Z00

| Thành phần | Trước | Sau |
|---|---|---|
| Bảng `Mạch \| Bài tập` | Cột mạch 2–6, chỉ 01.1–01.11 | Cột mạch 2–7. Hàng "Bài tập": 2: 01.1; 3: 01.2, 01.15; 4: 01.3, 01.4, 01.14; 5: 01.5, 01.6, 01.12, 01.15; 6: 01.7, 01.8; 7: 01.13, 01.16. Hàng "Chỉ trong ghi chú": 4: 01.10; 5: 01.9, 01.11; các mạch khác "—" |
| Dòng tệp bài tập | "Tệp bài tập: chưa có." | Bỏ; dòng liên kết thành "Ghi chú bài giảng · Bài tập", "Bài tập" dẫn tới `material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html` |
| Dòng Bài 02 | "Bài 02: …" không có liên kết | "Bài 02" là liên kết tới `lecture-02-giao-dien-tac-tu-moi-truong.html` (CLAUDE.md, mạch kết luận: liên kết một dòng tới bài sau) |
| Ghi chú diễn giả | Nói 01.1–01.8 trong các mục, 01.9–01.11 trong bài tập củng cố | Nêu 01.1–01.8 có ở cả ghi chú và tệp bài tập, 01.12–01.16 chỉ trong tệp, 01.9–01.11 chỉ trong ghi chú; 01.15 dùng mạch 3 và mạch 5; 01.13 là bài tổng hợp của mạch 7, 01.16 là bài tìm hiểu; giữ tài liệu đọc và câu nối Bài 02. 134 âm tiết |

- Mật độ (`density.py`): 57 → 71 âm tiết, 6 dòng, tối đa 16 âm tiết mỗi dòng, 0 công thức hiển thị. Trên đích 60 nhưng trong trần 80 của nhóm trang tổng kết; ngoại lệ ghi ở bảng "Ngoại lệ mật độ" của `storyboard.md`. Giữ số dòng 6 bằng cách gộp hai liên kết vào một dòng.
- Đề nghị trung bình "Z00" của giai đoạn III (bảng mục "Đề nghị sửa deck" và dòng "SV/PB Z00" của bảng rà soát bài tập): đã sửa đúng như đề xuất; không cần dạng gộp "01.12–01.16 (tệp bài tập)" vì bảng hai hàng vừa khung.
- Đề nghị nhẹ còn lại liên quan deck: "SV 01.3 va ghế" (thêm "va ghế không cản robot sang ô kế tiếp" vào đề, sửa đồng bộ ghi chú, `exercises.md` và D04). Không sửa trong đợt này: đề nghị đòi sửa đồng thời ghi chú và `exercises.md`, nằm ngoài phạm vi ghi; sửa riêng D04 sẽ làm đề trên trang khác đề trong hai tệp học liệu. Chuyển cho đợt đồng bộ học liệu sau.
- Ghi chú diễn giả P01 vẫn ánh xạ mục tiêu sang bài tập "trong ghi chú bài giảng", đúng với ghi chú; không sửa. `outline.md` ghi thêm các bài của tệp bài tập theo dòng "Mục tiêu học tập" của từng bài trong `exercises.md`.

### `no-ai-slop` (Edit) và kiểm tra

- Phạm vi: chữ mới trên mặt trang Z00 (nhãn hàng bảng, dòng liên kết) và ghi chú diễn giả Z00. Đối chiếu `eval.md`: không câu hỏi tu từ, không lời quy trình hay chỉ dẫn người dạy, không tài liệu làm chủ ngữ, không câu kết khẩu hiệu, không tương phản nhị phân; mỗi câu ghi chú nêu vị trí hoặc phạm vi của bài tập cụ thể. Đạt.
- `deck_check.py lecture-01-gioi-thieu-hoc-tang-cuong.html` (server tĩnh cổng 8799, cwd gốc kho), 70 trang ở 1600×900 và 390×844: 0 lỗi console hay trang, 0 `.katex-error`, 0 yêu cầu ngoài, 0 yêu cầu hỏng, không cuộn ngang, đủ 6 trang tiêu đề mạch. Cờ `overflow` (P01a, D02, G03b, G03d) giống hệt lần kiểm trước đợt sửa (báo động giả của `span` KaTeX ẩn). Cờ `small_font` ở Z00 (1600) là ngưỡng làm tròn: đo trực tiếp, ô bảng 0,752 em, đoạn văn 0,800 em, không ô nào dưới 0,75 em.
- Ảnh đã xem: `scratchpad/hw01/Z00-1600.png`, `scratchpad/hw01/Z00-390.png`: bảng bảy cột vừa khung, không chồng lấn; nhãn "Chỉ trong ghi chú" xuống hai dòng trong ô.
- Liên kết của Z00 mở bằng Playwright từ deck (cổng 8766): ghi chú bài giảng (HTTP 200, 0 `.katex-error`), tệp bài tập (HTTP 200, tiêu đề "Bài tập Bài 01 — Giới thiệu Học tăng cường", 13 khối bài tập, 0 `.katex-error`; ảnh `scratchpad/hw01/viewer-exercises.png`), Bài 02 (HTTP 200); 0 lỗi trang, 0 tải ngoài, 0 yêu cầu hỏng.
- `git diff --check`: sạch.

### Quyết định của điều phối viên (2026-10-14, đồng bộ trang bài tập về nhà)

- Tác tử biên tập deck (general-purpose, claude-opus-5-5, high). Kiểm độc lập: trang Z00 71 âm tiết (trần 80 của trang tổng kết, ngoại lệ ghi storyboard); Playwright 1600×900 và 390×844 toàn deck: 0 lỗi console, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang; liên kết viewer bài tập mở được; `git diff --check` sạch.
- Quyết định: **chấp nhận**; commit `fix(lecture-01)`.

## Đợt sửa 2026-10-14 — Đồng bộ chéo ghi chú

### Tác tử và phạm vi

- Vai: biên tập ghi chú bài giảng Bài 01 (sửa nhỏ), theo `brief_note_crosssync.md` của điều phối viên; loại `general-purpose`, mô hình Opus 5.5 (`claude-opus-5-5`), mức `high` theo brief. `no-ai-slop` Edit. Không commit.
- Tệp sửa: `materials/lec-01/lecture-note.md` và mục này. Không sửa deck, `exercises.md`, outline, storyboard, notebook, CSS.
- Đối chiếu: `planning/quyet-dinh-chuan-2026-10-12.md` (mục 1–2), `materials/lec-01/exercises.md` đã commit, deck đã commit (C06, D04, E04).
- Số hiệu không đổi (bộ đếm chung 01.1–01.22, Ví dụ 01.1–01.10, Bài tập 01.1–01.11, Tình huống 01.1–01.2); mọi `note-topic-id` giữ nguyên.

### Đề nghị còn mở và xử lý

Số dòng là số dòng trong ghi chú sau đợt sửa.

| Đề nghị (nguồn) | Trạng thái | Vị trí và nội dung |
|---|---|---|
| Bài tập 01.2(d) mở bằng dạng học và tín hiệu (giai đoạn III, đề nghị bổ sung (1)) | đã sửa | Dòng 367: "Học tăng cường. Tín hiệu là điểm tổng kết, một số đánh giá đến sau cả học kỳ. Tình huống này có ba trong bốn khác biệt … theo Nhận xét 01.6"; khớp `exercises.md` và ghi chú diễn giả C06 |
| Bài tập 01.5: gợi ý không nêu kết luận (giai đoạn III, (2)) | đã sửa | Dòng 675: "Phần thưởng khác $0$ chỉ có thể đến ở một bước. Đếm các dãy bốn hành động đưa robot tới ô 4 rồi hút."; đúng chữ của `exercises.md` |
| Bài tập 01.5(c): bỏ "như Định nghĩa 01.12 ghi rõ" (giai đoạn III, (2)) | đã sửa | Dòng 687: "giá trị là một hàm của chính sách (Định nghĩa 01.12)" |
| Bài tập 01.3: va ghế không cản robot sang ô kế tiếp (giai đoạn III, (3); đồng bộ trang bài tập về nhà) | đã sửa ở ghi chú | Dòng 513: thêm vế "va ghế không cản robot sang ô kế tiếp". Kiểm: với $T=4$ và $R_4=1$, bốn hành động phải là $\text{phải},\text{phải},\text{phải},\text{hút}$, nên bước va ghế ($R_2$) là lần sang phải thứ hai và robot vẫn tới ô 3; nếu va ghế giữ robot đứng yên thì cần năm hành động. Kết quả $G_t$ không đổi. Deck D04 và `exercises.md` chưa có vế này (xem đề nghị dưới) |
| Mục tiêu học tập dẫn 01.12–01.16 của `exercises.md` (giai đoạn III, "Đề nghị sửa ghi chú", nhẹ) | đã sửa | Dòng 9–13: thêm "trong tệp bài tập còn …" theo dòng "Mục tiêu học tập" của từng bài trong `exercises.md`: mục tiêu 1: 01.13, 01.15, 01.16; 2: 01.15; 3: 01.13, 01.14; 4: 01.12, 01.13, 01.15, 01.16; 5: 01.15; 6: không thêm. Dòng 16 (mới): bộ bài giao gồm tệp bài tập (liên kết viewer) và 01.9–01.11; 01.1–01.8 có ở cả hai nơi, 01.12–01.16 chỉ trong tệp |
| Bài tập 01.6: thêm bảng số liệu như F03 (giai đoạn III, nhẹ, "không bắt buộc") | không sửa | Đề trong ghi chú nằm ngay sau Ví dụ 01.9 có cùng số liệu; `exercises.md` đã có bảng để tự chứa. Giữ ghi chú gọn |

Brief mục (3): dòng mở "Bài tập củng cố" (dòng 1194) thêm một câu có liên kết `material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html`, nêu 01.1–01.8 có cả trong tệp bài tập (phần "Kiểm tra lại" nêu thêm lỗi thường gặp), 01.12 (tính toán hoặc chứng minh) và 01.13–01.16 (vận dụng) chỉ có trong tệp, 01.9–01.11 chỉ có ở mục này. Đoạn "Đọc thêm: tác tử nhiều nhiệm vụ và mô hình thế giới" (dòng 1277): "Bài tập 01.16 của [tệp bài tập](…)". Ba liên kết đã mở bằng Playwright từ viewer (cổng 8766): HTTP 200, trang "Bài tập Bài 01 — Giới thiệu Học tăng cường", 0 `.katex-error`.

### Đồng bộ ký hiệu theo `quyet-dinh-chuan-2026-10-12.md`

Không cần sửa. Đã quét toàn ghi chú: giá trị viết $v_\pi$; $V^\pi$ chỉ còn ở hai câu nêu tương ứng với giáo trình *Học máy thống kê* (dòng 50, 1272), đúng mục 2 của tệp quyết định; không có $P^\pi$, $r^\pi$, $T^\pi$ (bài không dùng ma trận hay toán tử Bellman); tên hành động và quan sát viết chữ đứng bằng `\text{}`; quy ước chữ đứng cho quân O và chữ nghiêng cho $O_t$ đã nêu ở dòng 48; mọi số thập phân trong KaTeX dùng `{,}` (quét các khoảng `$…$` tìm `chữ số.chữ số`: chỉ còn số hiệu `\tag`); không có "gần chắc chắn", "quy trình quyết định Markov", "tác nhân", "điểm thưởng", "Đáp án".

### Đề nghị sửa deck và `exercises.md`

| Mức | Vị trí | Vấn đề | Đề xuất |
|---|---|---|---|
| nhẹ | Deck D04 | Đề không nói va ghế có cản robot hay không; với $T=4$, robot phải sang được ô kế tiếp ở bước va ghế. Ghi chú nay đã nêu | Thêm vào dòng "Câu hỏi:" vế "va ghế không cản robot sang ô kế tiếp" (kiểm mật độ D04), hoặc nêu trong ghi chú diễn giả nếu dòng vượt 20 âm tiết |
| nhẹ | `exercises.md`, Bài tập 01.3 | Đề trong tệp còn theo chữ cũ của ghi chú; tệp ghi "giữ đề bài 01.1–01.8 của ghi chú" | Thêm cùng vế sau "va vào một chiếc ghế" ở đợt sửa `exercises.md` sau |
| nhẹ | `outline.md`, dòng mục tiêu 6 | Outline ghi Bài tập 01.13 dưới mục tiêu 6; dòng "Mục tiêu học tập" của 01.13 trong `exercises.md` ghi mục tiêu 1, 3, 4 (cùng phân tích một bước của Mục 5.4). Ghi chú theo `exercises.md`, không thêm 01.13 vào mục tiêu 6 | Điều phối viên chọn một cách ghi và đồng bộ outline hoặc dòng mức độ của 01.13 |

### Số từ

- `wc -w`: trước 20 900, sau 21 059 (+159), do câu liên kết ở mục tiêu, ở "Bài tập củng cố", các số bài thêm vào mục tiêu và câu (d) của 01.2. Vẫn theo quyết định cũ, không cắt nội dung khác.

### `no-ai-slop` (Edit) và kiểm tra

- Phạm vi: mọi câu đã thêm hoặc sửa (dòng 9–13, 16, 367, 513, 675, 687, 1194, 1277). Đối chiếu `eval.md`: không câu hỏi tu từ, không "hãy", không lời quy trình; bản nháp đầu của dòng 1194 lấy tệp bài tập làm chủ ngữ ("Tệp bài tập … giữ … và thêm …"), đã viết lại với các bài tập làm chủ ngữ; không tương phản nhị phân, không câu kết khẩu hiệu; dấu hai chấm ở dòng 367 dẫn danh sách ba khác biệt. Đạt.
- `note_check.py`: bộ đếm chung 22, ví dụ 10, bài tập 11, không khoảng trống, không trùng; 0 dấu `\(`/`\[`.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html` (viewer cổng 8766, server cwd `/data/tqlong/rl-plan`): 1600×900 và 390×844 đều 0 `.katex-error`, 69 khối, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, không tràn ngang.
- `git diff --check`: sạch.

### Quyết định của điều phối viên (2026-10-14, đồng bộ chéo ghi chú)

- Kiểm độc lập: `note_check.py` sạch; viewer 1600×900 và 390×844: 0 lỗi KaTeX, 0 lỗi console; `git diff --check` sạch. Quyết định: **chấp nhận**; commit `fix(materials-01)`. Ba đề nghị nhẹ còn lại (deck D04, `exercises.md` 01.3, outline mục tiêu 6: theo cách ghi của `exercises.md`) gom vào lượt khép đợt.

## Đợt sửa 2026-10-14 — Khép đợt: đồng bộ D04 và Bài tập 01.3

Biên tập viên: `general-purpose`, Claude Opus 5.5, effort `high`, `no-ai-slop` Edit; không commit. Đóng ba đề nghị nhẹ của đợt "Đồng bộ chéo ghi chú" (bảng "Đề nghị sửa deck và `exercises.md`").

| Mức | Vị trí | Thay đổi | Trạng thái |
|---|---|---|---|
| nhẹ | Deck D04, dòng "Câu hỏi:" | "robot từ ô 1; va vào ghế cho phần thưởng $-1$ và không cản robot sang ô kế tiếp." Dòng 20 âm tiết (đúng trần), trang 46 → 53 âm tiết (≤ 60), 4 dòng, 0 công thức hiển thị; đưa được lên mặt trang nên không cần lý do ngoại lệ | đã sửa |
| nhẹ | Deck D04, ghi chú diễn giả | Thêm: "Với $T=4$ và $R_4=1$, bốn hành động là phải, phải, phải, hút, nên bước va ghế là lần sang phải thứ hai; nếu va ghế giữ robot đứng yên thì lượt cần năm hành động." Khớp phần kiểm ở dòng 513 của ghi chú | đã sửa |
| nhẹ | `exercises.md`, đề Bài tập 01.3 | Thêm "; va ghế không cản robot sang ô kế tiếp" sau "va vào một chiếc ghế", đúng chữ dòng 513 của ghi chú. Gợi ý, lời giải và kết quả $G_t$ không đổi | đã sửa |
| nhẹ | `outline.md`, mục tiêu 6 | Bỏ 01.13 khỏi danh sách bài của mục tiêu 6; thêm câu: Z02–Z02b (Bài tập 01.13) xếp dưới mục tiêu 1, 3 và 4 theo dòng "Mức độ" của `exercises.md`. Mục tiêu 1, 3, 4 đã có "trong tệp bài tập còn 01.13" | đã sửa |
| nhẹ | `storyboard.md`, dòng D04 | Cột "Vòng biên tập" ghi thay đổi; cột âm tiết "— → 46 → 53" | đã sửa |
| nhẹ | `storyboard.md`, dòng Z02, Z02b | Cột "Mục tiêu" còn ghi "1, 3, 4, 6", lệch outline mới. Ngoài phạm vi ghi của lượt này | còn mở, chuyển điều phối viên |

Kiểm tra:

- `density.py`: D04 53 âm tiết, 4 dòng, tối đa 20 âm tiết mỗi dòng, 0 công thức hiển thị.
- `deck_check.py lecture-01-gioi-thieu-hoc-tang-cuong.html <outdir> D04` (cổng 8799, server cwd gốc kho), 70 trang ở 1600×900 và 390×844: 0 lỗi console hay trang, 0 `.katex-error`, 0 yêu cầu ngoài, 0 yêu cầu hỏng, không cuộn ngang, đủ 6 trang tiêu đề mạch. Cờ `overflow` (P01a, D02, G03b, G03d) giống hệt các lần kiểm trước (báo động giả của `span` KaTeX ẩn). Đã xem ảnh D04 ở hai cỡ: dòng "Câu hỏi:" xuống hai dòng ở 1600×900, nội dung nằm gọn trong khung, không chồng lấn.
- `note_check.py materials/lec-01/exercises.md`: 13 bài tập, 13 gợi ý, 13 lời giải; khoảng trống 9, 10, 11 là ba bài chỉ trong ghi chú; không trùng; 0 dấu `\(`/`\[`.
- `check_note.py 01 lecture-01-gioi-thieu-hoc-tang-cuong.html exercises`: 1600×900 và 390×844 đều 0 `.katex-error`, 39 khối, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, không tràn ngang.
- `git diff --check`: sạch.
- `no-ai-slop` (Edit), phạm vi: ba câu thêm (D04 mặt trang, D04 ghi chú, đề 01.3) và câu mới ở mục tiêu 6. Đối chiếu `eval.md`: không thêm khẳng định ngoài ghi chú, không câu hỏi tu từ, không lời quy trình, không câu kết khẩu hiệu. Đạt.

### Quyết định của điều phối viên (2026-10-14, khép đợt Bài 01)

- Kiểm độc lập: D04 53 âm tiết, dòng dài nhất 20; Playwright hai cỡ 0 lỗi; viewer bài tập 0 lỗi KaTeX; `git diff --check` sạch. Điều phối viên sửa cột "Mục tiêu" của Z02, Z02b trong storyboard thành "1, 3, 4" cho khớp outline. Quyết định: **chấp nhận**; commit `fix(lecture-01)`.
