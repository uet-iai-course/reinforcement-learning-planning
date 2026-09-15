# Storyboard Bài 02

## Hành trình khái niệm và thời lượng

Tuyến chính có 48 trang (kể cả bìa và các trang mở phần), tổng 120 phút. X01, X02, X05, X06 và X10 là nhánh dọc, dùng trong 30 phút chữa bài và không tính vào 120 phút trình chiếu.

| Cụm / vi chu trình | Vấn đề | Trực giác | Ví dụ | Hình thức/thuật toán | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Thời lượng |
|---|---|---|---|---|---|---|---|---:|
| Định hướng | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | Bài 01 → mục tiêu và bản đồ Bài 02 | 6 phút |
| Giao diện tương tác | A00 | A02 | A02 | A03 | A03 | A04 | ranh giới → lịch sử đúng chỉ số | 14 phút |
| Tín hiệu học | B00 | B02 | B03 | B04 | B05 | B05 | ba dạng học → nhận dạng phản hồi trễ | 16 phút |
| Markov | C00 | C02 | C02 | C03F | C03F–C04 | C03F | $S,O,X$ → ví dụ vị trí–vận tốc → phát biểu Markov đầy đủ | 12 phút |
| Quan sát một phần | C04 | C05 | C05 | C05; C06 hình thức hóa biểu diễn | C06 | C07 | trạng thái Markov → phân loại giao diện quan sát | 12 phút |
| Chính sách | D00 | D02V | D02V | D02–D03 | E04P | X06; D03 kiểm tra cục bộ | $X_t$ → phân phối trên $\mathcal A(x)$ | 8 phút |
| Giá trị | D00 | D04 | D04, D06 | D04F, D05S, D05 | E04V | E04V, X05 | $X_t=S_t$, $\pi(a\mid s)$ → quỹ đạo thưởng → $G_t$ → $v_\pi$ | 14 phút |
| Mô hình | D00 | D07 | D07 | D07B | E04P | X02 | quy ước tối thiểu → ví dụ $1/0$ → phân phối chuẩn hóa → tách $p$ và $\hat p$ | 6 phút |
| Giới hạn mô hình | D10 | D10 | D10 | D10 | D10 | D10 | mô hình một bước → hiểu phạm vi, sai số và lập kế hoạch | 2 phút |
| Dự đoán và điều khiển | D08 | D08 | D09 | D08 | D08 | D09 | chính sách + giá trị + mô hình → phân biệt vai trò | 6 phút |
| Mê cung | E00 | E02 | E02–E03 | E00–E02 | E03–E05, E04P–E04V | E04, E04V | toàn bộ ký hiệu → mô hình hóa nhất quán | 20 phút |
| Kết nối | Z00 | không áp dụng | không áp dụng | không áp dụng | không áp dụng | Z00 | Bài 02 → Bài 03 | 4 phút |
| Bài tập | X01, X02, X05, X06, X10 | X01, X02, X05, X06, X10 | X01, X02, X05, X06, X10 | không áp dụng: luyện tập | X01, X02, X05, X06, X10 | X01, X02, X05, X06, X10 | nội dung vừa học → lời giải có giả thiết | ngoài tuyến chính |

Tổng: $6+14+16+12+12+8+14+6+2+6+20+4=120$ phút. So với bản trước, cụm dự đoán và điều khiển giảm từ 8 xuống 6 phút để cấp 2 phút cho trang giới hạn mô hình D10; bài vẫn có 7 mạch, gồm mạch mở bài và mạch kết luận.

## Dữ kiện truyền giữa các cụm

- $A_t\to(R_{t+1},O_{t+1})$ từ A02 được dùng ở A03, A04, D04 và E02.
- $H_t=(O_0,A_0,R_1,\ldots,O_t)$ ở A03 chỉ là lịch sử quan sát. C03 dùng $\mathcal H_t^S=h_t^S$ kết thúc ở $S_t=s$ và biến cố điều kiện có xác suất dương.
- Ví dụ C02 truyền hai biến $x_t,v_t$ sang tiêu chuẩn C03: bỏ $v_t$ làm hai lịch sử cùng giá trị hiện tại nhưng có chuyển tiếp khác nhau.
- $X_t$ từ C00 và C06 đi vào $\pi(a\mid x)$ và $\mathcal A(x)$ ở D02–D03. Trường hợp $X_t=S_t$ được nêu riêng.
- D04 giải thích chiết khấu trước ví dụ $(-1,-1)$ và câu hỏi; D04F định nghĩa $G_t$. D05S mới giới hạn phần đánh giá theo trạng thái với chính sách và động lực không đổi theo thời gian. D06 tính trung bình $2{,}5$ trước định nghĩa $v_\pi$ ở D05. $T$ là thời điểm chạm đích riêng của quỹ đạo; không phải hạn chung cố định.
- E00 cố định bản đồ, tọa độ, $\mathcal A$, thưởng và điều kiện dừng. E02–E04 không thay các quy ước đó khi đổi giao diện quan sát.
- D07 không phụ thuộc E00 tương lai: trang tự nêu quy ước tối thiểu (mê cung lưới, chuyển tất định, mỗi chuyển tiếp $-1$). Ví dụ $1/0$ truyền sang D07B để định nghĩa phân phối chuẩn hóa và phân biệt động lực $p$ với mô hình ước lượng $\hat p$.

## Bản đồ từng trang

| Mã | Luận điểm trung tâm | Kiến thức đầu vào | Sản phẩm học tập | Câu nối |
|---|---|---|---|---|
| P00 | Bài 02 xây giao diện trước MDP. | Bài 01 | Biết phạm vi. | “Các mục tiêu đều kiểm tra được.” |
| P01 | Mục tiêu giới hạn ở giao diện, thông tin và vai trò. | P00 | Biết chuẩn đầu ra. | “Bảy phần dùng lại cùng ký hiệu.” |
| P02 | Bảy mạch đi từ định hướng đến tổng kết và bài tập. | P01 | Có bản đồ khớp bảy section ngoài. | “Bắt đầu bằng giao diện tương tác.” |
| A-TITLE | Giao diện tương tác | Mạch trước | Định vị mục tiêu của phần tiếp theo. | Phần mở đầu định nghĩa ranh giới tác tử–môi trường và cách đánh chỉ số. |
| A00 | Ranh giới xác định phần nào chọn và phần nào sinh phản hồi. | P02 | Phân biệt tác tử với môi trường. | “Đặt chỉ số cho một bước.” |
| A02 | $A_t$ sinh $R_{t+1},O_{t+1}$. | A00 | Viết một chuyển tiếp. | “Lặp chuyển tiếp thành lịch sử.” |
| A03 | Lịch sử quan sát có thứ tự. | A02 | Viết $H_t$. | “Kiểm tra một chỉ số cụ thể.” |
| A04 | Phản hồi sau $A_3$ mang chỉ số 4. | A03 | Tự sửa lỗi chỉ số trước khi hiện đáp án. | “Thứ tự này làm tín hiệu RL khác nhãn.” |
| B-TITLE | Tín hiệu học và phần thưởng | Mạch trước | Định vị mục tiêu của phần tiếp theo. | Phần trước mô tả dữ liệu tương tác được tạo ra; phần này trả lời dữ liệu đó được đánh giá bằng tín hiệu nào. |
| B00 | Ba dạng học khác nhau ở nguồn tín hiệu. | A04 | Phân biệt nhãn, cấu trúc và thưởng. | “Dữ liệu RL còn phụ thuộc hành động.” |
| B02 | Mẫu liên tiếp thường phụ thuộc; phân phối đổi khi chính sách đổi. | B00 | Diễn giải đúng ý không i.i.d. | “Phản hồi có thể đến muộn.” |
| B03 | Thưởng cuối chưa chỉ ra công của từng hành động. | B02 | Nhận ra phản hồi trễ. | “Mục tiêu được mã hóa qua thưởng.” |
| B04 | Giả thuyết phần thưởng chưa cần $\pi$ hay $G_t$; sản phẩm nối tới hình thức hóa tổng phần thưởng ở phần giá trị. | B03 | Phát biểu không vượt tiên quyết. | “Giả thuyết này dẫn tới tổng phần thưởng ở phần giá trị.” |
| B05 | Dữ liệu tuần tự chưa đủ để là RL. | B00–B04 | Kiểm tra cục bộ tình huống. | “Dự báo phản hồi đòi hỏi trạng thái đủ.” |
| C-TITLE | Trạng thái, quan sát và tính Markov | Mạch trước | Định vị mục tiêu của phần tiếp theo. | Phần tín hiệu cho biết dữ liệu được đánh giá thế nào; phần này xác định tác tử nhận thông tin gì và khi nào thông tin đủ để dự báo. |
| C00 | $S_t,O_t,X_t$ có miền và vai trò khác nhau. | B05 | Phân biệt ba tầng thông tin. | “Xét ví dụ khi biểu diễn thiếu biến.” |
| C02 | Cùng vị trí nhưng khác vận tốc cho bước kế tiếp khác. | C00 | Thấy một biến trạng thái bị bỏ. | “Viết tiêu chuẩn bằng lịch sử trạng thái.” |
| C03 | Trạng thái đủ làm quá khứ không bổ sung thông tin dự báo. | C02 | Phân biệt lịch sử quan sát và lịch sử trạng thái. | Viết điều kiện bằng xác suất rời rạc. |
| C03F | Tính Markov là đẳng thức hai phân phối có điều kiện. | C03 | Phát biểu điều kiện với lịch sử kết thúc ở s và xác suất dương. | Từ trạng thái đủ sang thông tin tác tử nhận. |
| C04 | Quan sát đầy đủ xác định trạng thái Markov. | C03F | Nhận ra trường hợp X=O=S. | Hai trạng thái có thể sinh cùng quan sát. |
| C05 | Quan sát ô trước trống có thể nhập nhằng vị trí. | C04 | Giải thích quan sát một phần bằng ví dụ. | Dùng lịch sử bổ sung thông tin. |
| C06 | Biểu diễn tóm tắt lịch sử để chọn hành động. | C05 | Nêu vai trò cửa sổ quan sát hoặc bộ nhớ. | Kiểm tra dữ liệu cảm biến thực nhận. |
| C07 | Tên miền không đủ để kết luận khả năng quan sát. | C04–C06 | Lập luận có điều kiện. | “Biểu diễn quyết định là đầu vào của chính sách.” |
| D-TITLE | Chính sách, hàm giá trị và mô hình | Mạch trước | Định vị mục tiêu của phần tiếp theo. | Trên nền thông tin đã xác định ở phần trước, phần này định nghĩa cách chọn hành động, cách đánh giá tương lai và mô hình dự báo. |
| D00 | Trang mở phần dùng chung; bốn vi chu trình bắt đầu lần lượt ở D02, D04, D07 và D08. | C07 | Có bản đồ vai trò; biết mô hình là tùy chọn. | “Định nghĩa chính sách trên $X_t$.” |
| D02V | Chính sách có thể chọn cố định hoặc ngẫu nhiên. | D00, C06 | Ví dụ hai hành động xác suất 0,5 mỗi hành động. | Ký hiệu hóa cách chọn. |
| D02 | Chính sách ánh xạ $X_t$ tới hành động hoặc phân phối. | C00, C06 | Định nghĩa $\mathcal A(x)$ và hai loại chính sách. | “Phân phối phải chuẩn hóa.” |
| D03 | Chính sách ngẫu nhiên chuẩn hóa trên $\mathcal A(x)$. | D02 | Kiểm tra miền và tổng xác suất. | “Đánh giá chính sách cần gộp thưởng tương lai.” |
| D04 | Chiết khấu giảm trọng số phần thưởng xa. | D03, B04 | Tính ba tổng trên hai thưởng âm một. | Khái quát thành tổng hữu hạn. |
| D04F | Phần thưởng tích lũy là tổng chiết khấu trên một quỹ đạo. | D04 | Hiểu T riêng mỗi quỹ đạo và tổng rỗng ở đích. | Chốt giả thiết trước đánh giá theo trạng thái. |
| D05S | Giá trị theo trạng thái cần giả thiết thời gian nhất quán. | D04F, C03F, D02 | Cố định chính sách, động lực và quy ước chạm đích. | Tính trung bình trên nhiều quỹ đạo. |
| D06 | Trung bình có trọng số gộp hai kết quả. | D05S | Tính 0,7 × 4 + 0,3 × (−1) = 2,5. | Đặt tên cho trung bình này. |
| D05 | Hàm giá trị là kỳ vọng tổng thưởng dưới chính sách cố định. | D06 | Liên kết giá trị với phép tính 2,5. | Mô hình dự báo từng bước chuyển tiếp. |
| D07 | Chuyển tiếp mê cung tất định có xác suất $1$ cho kết quả đúng, $0$ cho kết quả khác. | Quy ước tối thiểu tự nêu trên chính trang: mê cung lưới, chuyển tất định, mỗi chuyển tiếp $-1$ | Có ví dụ tính được trước khi định nghĩa tổng quát. | “Khái quát ví dụ thành phân phối có điều kiện.” |
| D07B | Mô hình chung là phân phối chuẩn hóa của trạng thái và phần thưởng kế tiếp. | D07 | Định nghĩa $p(s',r\mid s,a)$, điều kiện chuẩn hóa và phân biệt $p$ với $\hat p$. | “Mô hình một bước này có phạm vi và sai số nào?” |
| D10 | Mô hình có phạm vi và sai số. | D07B | Hiểu lập kế hoạch dùng dự báo trước khi chọn. | Phân biệt đánh giá với cải thiện chính sách. |
| D08 | Dự đoán giữ $\pi$; điều khiển cải thiện $\pi$. | D10, D02, D05 | Nhận câu nối từ D10 và phân biệt hai bài toán dựa trên vai trò đã tách. | “Kiểm tra bằng ba phát biểu.” |
| D09 | Mỗi vai trò có đầu ra riêng. | D00–D08 | Ghép đúng phát biểu. | “Áp toàn bộ vào mê cung.” |
| E-TITLE | Mô hình hóa bài toán mê cung | Mạch trước | Định vị mục tiêu của phần tiếp theo. | Phần này ghép các định nghĩa của các phần trước vào một ví dụ cụ thể. |
| E00 | Mê cung cố định có đặc tả $S,A,R$ và kết thúc rõ. | D09 | Có tọa độ, hành động, thưởng đích và va tường. | “Viết một chuyển tiếp.” |
| E02 | Chuyển tiếp mê cung giữ đúng chỉ số và tọa độ. | E00, A02 | Áp dụng ký hiệu. | “Đổi quan sát nhưng giữ môi trường.” |
| E03 | Tính Markov không phụ thuộc tác tử biết mô hình. | C03, E00 | Tách trạng thái khỏi kiến thức tác tử. | “Ảnh cục bộ tạo nhập nhằng.” |
| E04 | Hai tọa độ có thể cho cùng tín hiệu cảm biến. | E03 | Chứng minh nhập nhằng, tách khỏi biết bản đồ. | Trở lại nhận tọa độ để tính ba vai trò. |
| E04P | Chính sách chọn đường; mô hình xác định từng bước. | E00–E04, D02, D07B | Đường bốn bước Đông, ba bước Bắc từ (2,1). | Tính tổng thưởng trên đường vừa xác định. |
| E04V | Giá trị của chính sách là âm bảy tại điểm xuất phát. | E04P, D04F, D05 | Tính G và v; so sánh đường thêm hai bước. | Tổng hợp vai trò của ba khái niệm. |
| E05 | Vòng tương tác nối thông tin với lựa chọn và phản hồi. | E04V | Phân biệt chính sách, giá trị và mô hình trên cùng mê cung. | Tự kiểm tra trước Bài 03. |
| Z-TITLE | Tổng kết và bài tập | Mạch trước | Định vị mục tiêu của phần tiếp theo. | Ví dụ mê cung đã ghép trạng thái, hành động, phần thưởng và quan sát thành một bài toán. |
| Z00 | Nơi duy nhất nêu tuyến chi tiết Bài 03 và phân tuyến bài tập. | E05 | Tự kiểm bốn đầu ra, biết tuyến bài kế tiếp và phân tuyến bài tập (1, 2, 5, 6 chính; 10 mở rộng; 3, 4, 7, 8, 9 sau Bài 03); ghi chú đọc thêm Sutton & Barto Chương 3 và Silver Lecture 2. | “Nhấn xuống để chữa bài tập tuần 2.” |
| X01 | Đối chiếu ba dạng học và giải thích phản hồi trễ. | B00–B03 | Trả lời đúng Bài 1 nguồn. | “Áp vào mê cung.” |
| X02 | Mô hình hóa mê cung trong hai thiết lập quan sát. | C04–C06, E00–E04 | Trả lời đúng Bài 2 nguồn. | “Tính tổng phần thưởng chiết khấu.” |
| X05 | Tính $G_0$ và $G_1$ cho dãy thưởng cho trước với $\gamma=0{,}5$. | D04–D05 | Trả lời đúng Bài 5 nguồn ($G_0=3$, $G_1=4$). | “Kiểm tra chuẩn hóa chính sách.” |
| X06 | Kiểm tra chuẩn hóa và phân loại chính sách ngẫu nhiên. | D02–D03 | Trả lời đúng Bài 6 nguồn ($\pi(\text{Nam}\mid s)=0{,}3$, ngẫu nhiên). | “Mở rộng sang bài toán thực tế.” |
| X10 | Mô hình hóa một bài toán thực tế bằng trạng thái, hành động, chuyển tiếp, phần thưởng và điều kiện kết thúc/tiếp diễn. | E00–E04 | Trả lời đúng Bài 10 nguồn (mở rộng); không cần $q_\pi$ hay Bellman. | Kết thúc phần chữa bài. |

## Lịch sử quyết định bố cục trước đợt sửa 2026-09-16

Các số trang và mô tả trong mục lịch sử phản ánh bản trước; bảng từng trang phía trên là bản hiện hành.

- Gộp A00/A01, B00/B01, C00/C01, D00/D01 và E00/E01. Các mã A01, B01, C01, D01, E01 bị loại khỏi HTML và mọi bảng ánh xạ.
- Sau mỗi lần gộp, đã rà lại hai trang trước và hai trang sau: P01–A03, A03–B03, B04–C03, C05–D03 và D08–E03. Không còn tham chiếu tới mã đã bỏ; câu nối đã được viết lại.
- Cụm D được tách thành bốn vi chu trình: chính sách (bắt đầu D02); giá trị (bắt đầu D04); mô hình (bắt đầu D07); dự đoán và điều khiển (bắt đầu D08). D00 chỉ là trang mở phần dùng chung. Không coi chín trang là một chu trình duy nhất.
- A04 giấu đáp án bằng fragment; đáp án đầy đủ nằm trong ghi chú.
- X01, X02, X05, X06 giữ nguyên tinh thần nhiệm vụ của `hw02.pdf` Bài 1, 2, 5, 6 và X10 giữ nhiệm vụ Bài 10; cả năm trang ở nhánh dọc của Z00, ngoài 120 phút tuyến chính.
- D07B và D10 dùng HTML/KaTeX, không thêm SVG; đặt theo thứ tự D07 → D07B → D10 → D08 trong cùng cụm vai trò.
- Cụm mê cung có 20 phút để người học đặc tả, tính một chuyển tiếp, so sánh hai giao diện và giải thích quan sát một phần.
- Vòng sửa hiển thị tách D07 thành D07 và D07B, đồng thời xuống dòng công thức C03. Phạm vi rà lại gồm C02–C05 và D05–D09; câu nối và giả thiết phải giữ liên tục sau khi số trang chính tăng từ 35 lên 36.
- Vai trò và kết nối vào–ra quanh D10: D07 truyền ví dụ $1/0$ sang định nghĩa tổng quát ở D07B; D07B truyền mô hình một bước sang D10 để xét phạm vi và sai số; D10 kết nối ra D08 để phân biệt dự đoán với điều khiển. Mỗi trang có một luận điểm trung tâm.
- Thứ tự deck: cụm A (giao diện tương tác, topic-02) đứng trước cụm B (tín hiệu học, topic-01), khác thứ tự note. Lý do: dựng ranh giới tác tử–môi trường và chỉ số thời gian trước khi so sánh các tín hiệu học; khác thứ tự note nhưng không đổi logic.

## Trang mở các mạch — 2026-09-15

Giữ bảy section ngoài và thứ tự trang chuyên môn. P00 là bìa đồng thời mở phần định hướng; P02 dùng tên thống nhất với các trang mở. Mỗi trang mới là câu chuyển của cụm kế tiếp, không phải khái niệm mới nên chu trình sáu bước không áp dụng riêng. Dành khoảng 15 giây cho mỗi trang mở, lấy trong thời lượng chuyển ý đã có của cụm; tổng vẫn 120 phút, cộng 30 phút chữa bài.

| Mã | Tiêu đề / vai trò | Kết nối vào | Kết nối ra | Bước tiến / câu nối | Thời lượng cụm (gồm trang mở) |
|---|---|---|---|---|---|
| A-TITLE | Giao diện tương tác | P02 | A00 | Quy ước tương tác nối mục tiêu bài với ranh giới tác tử–môi trường. | 14 phút |
| B-TITLE | Tín hiệu học và phần thưởng | A04 | B00 | Từ thứ tự phản hồi sang nguồn tín hiệu đánh giá hành động. | 16 phút |
| C-TITLE | Trạng thái, quan sát và tính Markov | B05 | C00 | Từ tín hiệu học sang thông tin dùng để dự báo và quyết định. | 24 phút |
| D-TITLE | Chính sách, hàm giá trị và mô hình | C07 | D00 | Biểu diễn quyết định trở thành đầu vào của chính sách; giá trị và mô hình có vai trò riêng. | 36 phút |
| E-TITLE | Mô hình hóa bài toán mê cung | D09 | E00 | Dùng các vai trò vừa phân biệt để đặc tả mê cung. | 20 phút |
| Z-TITLE | Tổng kết và bài tập | E05 | Z00 | Thu hồi vòng tương tác qua tự kiểm tra, bài tập và chuẩn bị Bài 03. | 4 phút |

Sản phẩm của mỗi trang mở là nhận biết nhiệm vụ của phần và liên hệ với kết quả vừa có; tiên quyết và chu trình học tập vẫn theo bảng đầu tài liệu. Các ID mới phải đứng ngay trước trang ghi ở cột kết nối ra, trong cùng section ngoài. Bản đồ hiện hành này thay cho các mô tả tên mạch cũ trong lịch sử; không đổi các vi chu trình chuyên môn.

## Sửa theo kiểm định mạch khái niệm — 2026-09-16

- Thêm C03F, D02V, D04F, D05S, E04P và E04V; giữ 7 section ngoài. D06 đứng trước D05 để ví dụ kỳ vọng chuẩn bị cho định nghĩa. Không bỏ trang nguồn hoặc bài tập.
- A02, B02–B03 giải thích ký hiệu và tên gọi khi xuất hiện. C05 dùng nhập nhằng quan sát trước tên mô hình; C06 không dùng ký hiệu chính sách trước định nghĩa.
- D00 tách ba vai trò song song. D07 tự nêu dữ kiện lưới. D10 chỉ bàn phạm vi, sai số và nghĩa của lập kế hoạch. E04 dùng hai tọa độ cụ thể để chứng minh quan sát nhập nhằng.
- E04P–E04V bổ sung ứng dụng chung chính sách–mô hình–giá trị, không thêm thuật toán. Với đường (2,1) đến (6,4), có 7 bước, mỗi bước −1, hệ số chiết khấu bằng 1.
- Giữ tổng 120 phút: các trang tách phân bổ lại thời gian trong cụm Markov 12 phút và cụm giá trị 14 phút; ví dụ tích hợp nằm trong 20 phút mê cung. Bài tập vẫn 30 phút.
- Các bước sáu phần được gộp khi dùng chung một ví dụ: A02 vừa trực giác vừa ví dụ; B04 hình thức hóa bằng lời; C05 vừa ví dụ vừa khái niệm nhập nhằng; D07 vừa trực giác vừa ví dụ. Không có thuật toán mới nên bước giả mã không áp dụng. Ứng dụng chính sách, giá trị và mô hình được nối sang E04P–E04V sau định nghĩa, rồi kiểm tra bằng thay đổi đường đi.
- Phạm vi rà lại: toàn bộ 53 trang, gồm mọi ranh giới và ít nhất hai trang lân cận mỗi phía của các thay đổi. Kết quả rà độc lập và kiểm tra hiển thị được ghi trong review-log.

Ứng dụng chung ở E04P–E04V được tính trong 20 phút mê cung, không cộng lại vào thời lượng từng khái niệm. D03 và D09 là kiểm tra cục bộ để sửa hiểu nhầm trước ứng dụng; X06 và X02 kiểm tra lại sau ứng dụng. C06 hình thức hóa biểu diễn $X_t=f(H_t)$, không hình thức hóa chính sách. Các hàng tổng kết/giới hạn mô hình dùng chu trình rút gọn vì không giới thiệu khái niệm trọng tâm hoặc thuật toán mới.
