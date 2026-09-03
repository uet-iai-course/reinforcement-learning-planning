# Storyboard Bài 02

## Hành trình khái niệm và thời lượng

Tuyến chính có 36 trang, tổng 120 phút. X01, X02, X05, X06 và X10 là nhánh dọc, dùng trong 30 phút chữa bài và không tính vào 120 phút trình chiếu.

| Cụm / vi chu trình | Vấn đề | Trực giác | Ví dụ | Hình thức/thuật toán | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Thời lượng |
|---|---|---|---|---|---|---|---|---:|
| Định hướng | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | không áp dụng: cụm chỉ nêu phạm vi | Bài 01 → mục tiêu và bản đồ Bài 02 | 6 phút |
| Giao diện tương tác | A00 | A02 | A02 | A03 | A03 | A04 | ranh giới → lịch sử đúng chỉ số | 14 phút |
| Tín hiệu học | B00 | B02 | B03 | B04 | B05 | B05 | ba dạng học → nhận dạng phản hồi trễ | 16 phút |
| Markov | C00 | C02 | C02 | C03 | C03–C04 | C03 | $S,O,X$ → ví dụ vị trí–vận tốc → phát biểu Markov đầy đủ | 12 phút |
| Quan sát một phần | C04 | C05 | C05 | C05–C06 | C06 | C07 | trạng thái Markov → phân loại giao diện quan sát | 12 phút |
| Chính sách | D00 | D02 | D03 | D02–D03 | D03 | D03 | $X_t$ → phân phối trên $\mathcal A(x)$ | 8 phút |
| Giá trị | D00 | D04 | D04, D06 | D04–D05 | D06 | D06 | $X_t=S_t$, $\pi(a\mid s)$ → quỹ đạo thưởng → $G_t$ → $v_\pi$ | 14 phút |
| Mô hình | D00 | D07 | D07 | D07B | D07–D07B | D07B | quy ước tối thiểu → ví dụ $1/0$ → phân phối chuẩn hóa → tách $p$ và $\hat p$ | 6 phút |
| Giới hạn mô hình | D10 | D10 | D10 | D10 | D10 | D10 | mô hình dự báo cục bộ → phân biệt với mô hình hoàn thiện, không suy diễn AGI | 2 phút |
| Dự đoán và điều khiển | D08 | D08 | D09 | D08 | D08 | D09 | chính sách + giá trị + mô hình → phân biệt vai trò | 6 phút |
| Mê cung | E00 | E02 | E02–E03 | E00–E02 | E03–E05 | E04 | toàn bộ ký hiệu → mô hình hóa nhất quán | 20 phút |
| Kết nối | Z00 | không áp dụng | không áp dụng | không áp dụng | không áp dụng | Z00 | Bài 02 → Bài 03 | 4 phút |
| Bài tập | X01, X02, X05, X06, X10 | X01, X02, X05, X06, X10 | X01, X02, X05, X06, X10 | không áp dụng: luyện tập | X01, X02, X05, X06, X10 | X01, X02, X05, X06, X10 | nội dung vừa học → lời giải có giả thiết | ngoài tuyến chính |

Tổng: $6+14+16+12+12+8+14+6+2+6+20+4=120$ phút. So với bản trước, cụm dự đoán và điều khiển giảm từ 8 xuống 6 phút để cấp 2 phút cho trang giới hạn mô hình D10; bài vẫn có 7 mạch, gồm mạch mở bài và mạch kết luận.

## Dữ kiện truyền giữa các cụm

- $A_t\to(R_{t+1},O_{t+1})$ từ A02 được dùng ở A03, A04, D04 và E02.
- $H_t=(O_0,A_0,R_1,\ldots,O_t)$ ở A03 chỉ là lịch sử quan sát. C03 dùng $\mathcal H_t^S=h_t^S$ kết thúc ở $S_t=s$ và biến cố điều kiện có xác suất dương.
- Ví dụ C02 truyền hai biến $x_t,v_t$ sang tiêu chuẩn C03: bỏ $v_t$ làm hai lịch sử cùng giá trị hiện tại nhưng có chuyển tiếp khác nhau.
- $X_t$ từ C00 và C06 đi vào $\pi(a\mid x)$ và $\mathcal A(x)$ ở D02–D03. Trường hợp $X_t=S_t$ được nêu riêng.
- D04 chốt phạm vi D04–D09 là quan sát đầy đủ $X_t=S_t$ với chính sách Markov $\pi(a\mid s)$. Quỹ đạo $(-1,-1)$ tạo $G_t=-1-\gamma$ trước khi tổng quát hóa; D05–D06 dùng đúng giả thiết này.
- E00 cố định bản đồ, tọa độ, $\mathcal A$, thưởng và điều kiện dừng. E02–E04 không thay các quy ước đó khi đổi giao diện quan sát.
- D07 không phụ thuộc E00 tương lai: trang tự nêu quy ước tối thiểu (mê cung lưới, chuyển tất định, mỗi chuyển tiếp $-1$). Ví dụ $1/0$ truyền sang D07B để định nghĩa phân phối chuẩn hóa và phân biệt động lực $p$ với mô hình ước lượng $\hat p$.

## Bản đồ từng trang

| Mã | Luận điểm trung tâm | Kiến thức đầu vào | Sản phẩm học tập | Câu nối |
|---|---|---|---|---|
| P00 | Bài 02 xây giao diện trước MDP. | Bài 01 | Biết phạm vi. | “Các mục tiêu đều kiểm tra được.” |
| P01 | Mục tiêu giới hạn ở giao diện, thông tin và vai trò. | P00 | Biết chuẩn đầu ra. | “Ba tuyến dùng lại cùng ký hiệu.” |
| P02 | Bốn trục Tương tác, Tín hiệu học, Thông tin và Quyết định tạo một chuỗi. | P01 | Có bản đồ bài. | “Bắt đầu bằng ranh giới hai phía.” |
| A00 | Ranh giới xác định phần nào chọn và phần nào sinh phản hồi. | P02 | Phân biệt tác tử với môi trường. | “Đặt chỉ số cho một bước.” |
| A02 | $A_t$ sinh $R_{t+1},O_{t+1}$. | A00 | Viết một chuyển tiếp. | “Lặp chuyển tiếp thành lịch sử.” |
| A03 | Lịch sử quan sát có thứ tự. | A02 | Viết $H_t$. | “Kiểm tra một chỉ số cụ thể.” |
| A04 | Phản hồi sau $A_3$ mang chỉ số 4. | A03 | Tự sửa lỗi chỉ số trước khi hiện đáp án. | “Thứ tự này làm tín hiệu RL khác nhãn.” |
| B00 | Ba dạng học khác nhau ở nguồn tín hiệu. | A04 | Phân biệt nhãn, cấu trúc và thưởng. | “Dữ liệu RL còn phụ thuộc hành động.” |
| B02 | Mẫu liên tiếp thường phụ thuộc; phân phối đổi khi chính sách đổi. | B00 | Diễn giải đúng ý không i.i.d. | “Phản hồi có thể đến muộn.” |
| B03 | Thưởng cuối chưa chỉ ra công của từng hành động. | B02 | Nhận ra phản hồi trễ. | “Mục tiêu được mã hóa qua thưởng.” |
| B04 | Giả thuyết phần thưởng chưa cần $\pi$ hay $G_t$; sản phẩm nối tới hình thức hóa tổng phần thưởng ở phần giá trị. | B03 | Phát biểu không vượt tiên quyết. | “Giả thuyết này dẫn tới tổng phần thưởng ở phần giá trị.” |
| B05 | Dữ liệu tuần tự chưa đủ để là RL. | B00–B04 | Kiểm tra cục bộ tình huống. | “Dự báo phản hồi đòi hỏi trạng thái đủ.” |
| C00 | $S_t,O_t,X_t$ có miền và vai trò khác nhau. | B05 | Phân biệt ba tầng thông tin. | “Xét ví dụ khi biểu diễn thiếu biến.” |
| C02 | Cùng vị trí nhưng khác vận tốc cho bước kế tiếp khác. | C00 | Thấy một biến trạng thái bị bỏ. | “Viết tiêu chuẩn bằng lịch sử trạng thái.” |
| C03 | Lịch sử trạng thái không thêm thông tin khi biết $S_t=s,A_t=a$. | C02 | Phát biểu đầy đủ với $h_t^S$ kết thúc ở $s$; kiểm tra vị trí với vị trí–vận tốc. | “Từ đây xét tác tử quan sát được gì.” |
| C04 | Quan sát đầy đủ xác định được trạng thái Markov. | C03 | Không đồng nhất quan sát đầy đủ với MDP. | “Quan sát thiếu dẫn tới POMDP.” |
| C05 | POMDP có trạng thái Markov nhưng tác tử chỉ nhận quan sát. | C04 | Biết tên đầy đủ và cơ chế nhập nhằng. | “Ghép thông tin qua thời gian.” |
| C06 | $X_t=f(H_t)$ có thể giữ thông tin cần cho quyết định. | C05 | Nêu vai trò bộ nhớ và niềm tin. | “Phân loại phải bắt đầu từ giao diện.” |
| C07 | Tên miền không đủ để kết luận khả năng quan sát. | C04–C06 | Lập luận có điều kiện. | “Biểu diễn quyết định là đầu vào của chính sách.” |
| D00 | Trang mở phần dùng chung; bốn vi chu trình bắt đầu lần lượt ở D02, D04, D07 và D08. | C07 | Có bản đồ vai trò; biết mô hình là tùy chọn. | “Định nghĩa chính sách trên $X_t$.” |
| D02 | Chính sách ánh xạ $X_t$ tới hành động hoặc phân phối. | C00, C06 | Định nghĩa $\mathcal A(x)$ và hai loại chính sách. | “Phân phối phải chuẩn hóa.” |
| D03 | Chính sách ngẫu nhiên chuẩn hóa trên $\mathcal A(x)$. | D02 | Kiểm tra miền và tổng xác suất. | “Đánh giá chính sách cần gộp thưởng tương lai.” |
| D04 | Trong trường hợp $X_t=S_t$, quỹ đạo $(-1,-1)$ cho $G_t=-1-\gamma$ rồi dẫn tới công thức tổng. | A02, B04, D02 | Chốt chính sách Markov và định nghĩa phần thưởng tích lũy theo thứ tự ví dụ → hình thức. | “Giá trị là kỳ vọng của đại lượng này.” |
| D05 | $v_\pi$ đánh giá tương lai dưới chính sách cố định. | D04 | Định nghĩa hàm giá trị trạng thái. | “Kỳ vọng gộp nhiều quỹ đạo.” |
| D06 | Kỳ vọng không bảo đảm từng quỹ đạo. | D05 | Tính $2{,}5$. | “Mô hình trả lời câu hỏi khác.” |
| D07 | Chuyển tiếp mê cung tất định có xác suất $1$ cho kết quả đúng, $0$ cho kết quả khác. | Quy ước tối thiểu tự nêu trên chính trang: mê cung lưới, chuyển tất định, mỗi chuyển tiếp $-1$ | Có ví dụ tính được trước khi định nghĩa tổng quát. | “Khái quát ví dụ thành phân phối có điều kiện.” |
| D07B | Mô hình chung là phân phối chuẩn hóa của trạng thái và phần thưởng kế tiếp. | D07 | Định nghĩa $p(s',r\mid s,a)$, điều kiện chuẩn hóa và phân biệt $p$ với $\hat p$. | “Mô hình một bước này có phạm vi và sai số nào?” |
| D10 | Mô hình dự báo cục bộ có điều kiện: câu mở là cầu nối vấn đề — mô hình một bước ở phần trước hữu ích nhưng có phạm vi và sai số, nên cần phân biệt với mô hình hoàn thiện; một luận điểm trung tâm, không quá tải. | D07B | Phân biệt mô hình cục bộ với "mô hình hoàn thiện về thế giới" bằng phạm vi và độ tin cậy; không suy diễn hệ thống AI bắt buộc cần mô hình tường minh; kết nối ra: dẫn sang phân biệt dự đoán và điều khiển. | “Dự đoán và điều khiển dùng các vai trò khác nhau.” |
| D08 | Dự đoán giữ $\pi$; điều khiển cải thiện $\pi$. | D10, D02, D05 | Nhận câu nối từ D10 và phân biệt hai bài toán dựa trên vai trò đã tách. | “Kiểm tra bằng ba phát biểu.” |
| D09 | Mỗi vai trò có đầu ra riêng. | D00–D08 | Ghép đúng phát biểu. | “Áp toàn bộ vào mê cung.” |
| E00 | Mê cung cố định có đặc tả $S,A,R$ và kết thúc rõ. | D09 | Có tọa độ, hành động, thưởng đích và va tường. | “Viết một chuyển tiếp.” |
| E02 | Chuyển tiếp mê cung giữ đúng chỉ số và tọa độ. | E00, A02 | Áp dụng ký hiệu. | “Đổi quan sát nhưng giữ môi trường.” |
| E03 | Tính Markov không phụ thuộc tác tử biết mô hình. | C03, E00 | Tách trạng thái khỏi kiến thức tác tử. | “Ảnh cục bộ tạo nhập nhằng.” |
| E04 | Ảnh cục bộ có thể là quan sát một phần. | E03, C05 | Nêu bằng chứng và vai trò lịch sử. | “Nối các kết quả thành toàn bộ vòng tương tác.” |
| E05 | Lịch sử → biểu diễn → chính sách → phản hồi là trục bài; mê cung thu hồi bốn trục mở đầu. | Toàn bài | Tái dựng $X_t=f(H_t)$ trong vòng giao diện và vai trò của giá trị, mô hình. | “Tự kiểm tra trước khi sang bài tiếp.” |
| Z00 | Nơi duy nhất nêu tuyến chi tiết Bài 03 và phân tuyến bài tập. | E05 | Tự kiểm bốn đầu ra, biết tuyến bài kế tiếp và phân tuyến bài tập (1, 2, 5, 6 chính; 10 mở rộng; 3, 4, 7, 8, 9 sau Bài 03); ghi chú đọc thêm Sutton & Barto Chương 3 và Silver Lecture 2. | “Nhấn xuống để chữa bài tập tuần 2.” |
| X01 | Đối chiếu ba dạng học và giải thích phản hồi trễ. | B00–B03 | Trả lời đúng Bài 1 nguồn. | “Áp vào mê cung.” |
| X02 | Mô hình hóa mê cung trong hai thiết lập quan sát. | C04–C06, E00–E04 | Trả lời đúng Bài 2 nguồn. | “Tính tổng phần thưởng chiết khấu.” |
| X05 | Tính $G_0$ và $G_1$ cho dãy thưởng cho trước với $\gamma=0{,}5$. | D04–D05 | Trả lời đúng Bài 5 nguồn ($G_0=3$, $G_1=4$). | “Kiểm tra chuẩn hóa chính sách.” |
| X06 | Kiểm tra chuẩn hóa và phân loại chính sách ngẫu nhiên. | D02–D03 | Trả lời đúng Bài 6 nguồn ($\pi(\text{Nam}\mid s)=0{,}3$, ngẫu nhiên). | “Mở rộng sang bài toán thực tế.” |
| X10 | Mô hình hóa một bài toán thực tế bằng trạng thái, hành động, chuyển tiếp, phần thưởng và điều kiện kết thúc/tiếp diễn. | E00–E04 | Trả lời đúng Bài 10 nguồn (mở rộng); không cần $q_\pi$ hay Bellman. | Kết thúc phần chữa bài. |

## Quyết định bố cục và rà lân cận

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
