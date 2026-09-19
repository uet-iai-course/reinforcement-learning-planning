# Bài 03 — Storyboard triển khai

Đã triển khai phần 1–3/7. Bảy phần và 120 phút theo [kế hoạch chi tiết](detailed-slide-plan.md); bản này ghi quyết định thể hiện thực tế. Các phần chưa triển khai dùng bản HTML cũ, không được tính là hoàn tất.

## Phần 1. Từ tương tác đến mô hình xác suất — 8 phút

Đầu vào: giao diện tác tử–môi trường ở Bài 02. Đầu ra: nhu cầu mô tả quy luật sinh các quỹ đạo và tính giá trị bằng mô hình. Đây là phần mở đầu, chỉ ôn và đặt vấn đề; định nghĩa mới nằm ở các phần sau.


### L03-01-01 — Quá trình quyết định Markov

Thời lượng: 1 phút. Vai trò: tiêu đề bài giảng.

**Đầu vào:** Bài 02 đã giới thiệu giao diện tác tử–môi trường và các thành phần của bài toán.

**Nội dung trên slide:** “Quá trình quyết định Markov”; “Bài 03 · Học tăng cường”; học kỳ 1, năm học 2026–2027; Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội.

**Cách thể hiện:** Trang tiêu đề theo mẫu và CSS chung; tên bài là nội dung lớn nhất. Không dùng tiêu đề phần 1 thay cho tên bài.

**Giải thích và hình thức hóa:** Giới thiệu mục tiêu bằng lời: từ mô hình đã biết và chính sách cố định, tính giá trị dài hạn. Chưa có công thức mới.

**Kết nối:** Sang bản đồ nội dung toàn bài.

**Kiểm tra/ghi chú đáp án:** Không đặt câu hỏi tại trang tiêu đề.

**Nguồn:** PPTX28; thông tin học phần.

**Quyết định thể hiện khi triển khai:** Trang tiêu đề chỉ đặt tên bài và thông tin học phần, không có công thức mới vì đây là điểm vào của toàn bài; mục tiêu nằm trong notes. Không dùng hình trực giác để tránh lặp với slide mở phần ngay sau đó. Tiên quyết: Bài 02 (giao diện tác tử–môi trường, tổng thưởng). Cầu nối: slide nội dung bài học.

### L03-01-02 — Nội dung bài học

Thời lượng: 1 phút. Vai trò: định hướng toàn bài.

**Đầu vào:** Tên và mục tiêu Bài 03.

**Nội dung trên slide:** Bảy phần theo thứ tự: 1. Từ tương tác đến mô hình xác suất; 2. Chuỗi Markov; 3. Quá trình phần thưởng Markov; 4. Phương trình Bellman; 5. MDP và chính sách cố định; 6. Giá trị trạng thái và giá trị hành động; 7. Tổng hợp và vận dụng.

**Cách thể hiện:** Danh sách hai cột hoặc sơ đồ bảy mục, đánh dấu phần 1. Không hiện thời lượng, ID hoặc chỉ dẫn tác giả.

**Giải thích và hình thức hóa:** Các tên gọi mới chỉ xuất hiện như tên nội dung, chưa yêu cầu sinh viên hiểu định nghĩa. Khi nói, diễn đạt mạch bằng lời: mô tả chuyển tiếp, thêm thưởng, đánh giá tương lai, rồi xét lựa chọn hành động. “Quá trình quyết định Markov (MDP)” được viết đầy đủ trong mục 5 khi dựng slide.

**Kết nối:** Sang slide mở phần 1, rồi ví dụ một mô hình sinh nhiều quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Không thêm kiểm tra tại trang nội dung; phần 1 kết thúc bằng câu hỏi riêng.

**Nguồn:** Dàn ý bảy phần đã được thống nhất; PPTX28–58.

**Quyết định thể hiện khi triển khai:** Danh sách hai cột giúp bảy mục vừa khung 1280x720 mà không cần hình; mục 1 được nhấn mạnh để sinh viên biết vị trí hiện tại. Thứ tự mục chính là bản đồ khái niệm: mỗi lớp mô hình là mở rộng của lớp trước, nên thứ tự đọc cũng là thứ tự xây dựng. Không hiện thời lượng hay ID vì đó là thông tin điều hành, không phải nội dung học.

### L03-01-03 — Từ tương tác đến mô hình xác suất

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** Bản đồ bài học ở 01-02 và giao diện tác tử–môi trường từ Bài02.

**Nội dung trên slide:** Tiêu đề phần và câu: “Cùng trạng thái và hành động có thể cho kết quả khác nhau.”

**Cách thể hiện:** Một nút hiện tại, một hành động và hai kết quả; chưa đặt bộ ký hiệu MDP.

**Giải thích và hình thức hóa:** Nhắc lại vòng tương tác bằng lời; bài này giả sử đã biết xác suất chuyển.

**Kết nối:** Từ một bước tương tác sang nhiều khả năng diễn tiến.

**Kiểm tra/ghi chú đáp án:** Không đặt câu hỏi riêng trên trang mở.

**Nguồn:** PPTX 28–29; nối Bài 02.

**Quyết định thể hiện khi triển khai:** Hình trực giác gồm một nút trạng thái, một nút hành động và hai nút trạng thái kế tiếp với hai mũi tên, thể hiện đúng luận điểm duy nhất của slide: một bước tương tác có nhiều khả năng diễn tiến. Hai nhãn trạng thái 1 và trạng thái 2 phân biệt hai kết quả khác nhau. Chưa dùng bộ ký hiệu MDP để không vượt trước định nghĩa ở phần 5. Tiên quyết: giao diện tác tử–môi trường Bài 02. Cầu nối: slide sau cho thấy nhiều quỹ đạo sinh ra từ chính tính ngẫu nhiên này.

### L03-01-04 — Một mô hình, nhiều quỹ đạo

Thời lượng: 2 phút. Vai trò: vấn đề và trực giác.

**Đầu vào:** Một bước có thể có nhiều kết quả; trạng thái quan sát được.

**Nội dung trên slide:** Hai đường đi từ cùng điểm xuất phát trên đồ thị sinh viên.

**Cách thể hiện:** Chỉ hiện các nút liên quan đến hai đường; cùng điểm xuất phát và cùng kết thúc Sleep, hai diễn tiến khác nhau.

**Giải thích và hình thức hóa:** Quỹ đạo là một kết quả lấy mẫu. Mô hình là quy luật sinh ra cả các quỹ đạo chưa quan sát; chưa đồng nhất hai tổng cụ thể với kỳ vọng.

**Kết nối:** Từ sự khác nhau của đường đi đến việc phải dùng phân phối.

**Kiểm tra/ghi chú đáp án:** Một đường quan sát được có xác định hết xác suất chuyển không? Không.

**Nguồn:** PPTX 31–32.

**Quyết định thể hiện khi triển khai:** Hình vẽ hai hàng quỹ đạo riêng biệt, cùng xuất phát từ C1 và cùng kết thúc ở Sleep, mỗi hàng có nhãn Đường 1/Đường 2 để sinh viên đọc được ngay luận điểm: cùng điểm đầu, nhiều diễn tiến. Hai quỹ đạo là các đường hợp lệ suy ra từ đồ thị, không phải hai kết thúc khác nhau. Chỉ hiện các nút liên quan, đúng yêu cầu của kế hoạch. Đây là bước vấn đề–trực giác trước khi đưa vào phân phối ở phần 2; chưa tính tổng thưởng để không trộn với phần 3. Tiên quyết: khái niệm trạng thái và quỹ đạo từ Bài 02. Cầu nối: cần một cách mô tả gọn quy luật sinh mọi quỹ đạo — đó là ba lớp mô hình ở slide sau.

### L03-01-05 — Ba lớp mô hình

Thời lượng: 1 phút. Vai trò: bản đồ khái niệm.

**Đầu vào:** Hai quỹ đạo từ cùng điểm đầu; nhu cầu mô tả quy luật sinh chúng.

**Nội dung trên slide:** Chuỗi trạng thái → thêm thưởng → thêm lựa chọn hành động.

**Cách thể hiện:** Ba hình dùng cùng các nút; lần lượt thêm nhãn thưởng và nút lựa chọn.

**Giải thích và hình thức hóa:** Gọi đầy đủ ba tên bằng tiếng Việt; chưa yêu cầu ghi nhớ các bộ thành phần hoặc viết tắt.

**Kết nối:** Phần 2 bắt đầu bằng lớp đơn giản nhất.

**Kiểm tra/ghi chú đáp án:** Đầu ra cần đạt cuối bài: từ mô hình và chính sách viết được phương trình giá trị.

**Nguồn:** PPTX 30,34,49.

**Quyết định thể hiện khi triển khai:** Ba hàng của hình dùng cùng hai trạng thái A và B: hàng một chỉ có chuyển tiếp, hàng hai thêm nhãn thưởng trên phản hồi, hàng ba thêm hai lựa chọn hành động a và b trước khi về B, vẫn giữ nhãn thưởng — trực quan thể hiện quan hệ bao chứa giữa ba lớp mà không mất phần thưởng khi thêm hành động. Nhãn tiếng Việt đủ ba lớp, không công thức, vì slide chỉ làm bản đồ khái niệm. Tiên quyết: hai quỹ đạo từ cùng điểm đầu ở slide trước cho thấy cần mô hình hóa quy luật. Cầu nối: phần 2 bắt đầu bằng lớp đơn giản nhất, chuỗi Markov.

### L03-01-06 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: kiểm tra tiên quyết.

**Đầu vào:** Phân biệt trạng thái, mô hình và một mẫu quỹ đạo.

**Nội dung trên slide:** 1. Quan sát đúng trạng thái có đồng nghĩa biết xác suất chuyển không?
2. Cùng trạng thái có thể dẫn tới các trạng thái kế tiếp khác nhau không?

**Cách thể hiện:** Hai câu đánh số, đáp án trong notes.

**Giải thích và hình thức hóa:** Chỉ kiểm tra những khái niệm đã có, chưa hỏi ma trận hay Bellman.

**Kết nối:** Từ phân biệt trạng thái và mô hình sang đọc đồ thị chuyển.

**Kiểm tra/ghi chú đáp án:** 1. Không. 2. Có, nếu chuyển ngẫu nhiên.

**Nguồn:** Bài 02; PPTX 29–30.

**Quyết định thể hiện khi triển khai:** Hai câu trong danh sách đánh số dưới một nhãn Câu hỏi chung; đáp án nằm trọn trong notes để slide chỉ giữ câu hỏi. Câu 1 tách quan sát khỏi mô hình, câu 2 khẳng định tính ngẫu nhiên — đúng hai phân biệt mà phần 1 đặt ra. Không dùng hình vì hai câu đủ tự đứng và slide kiểm tra cần gọn. Tiên quyết: slide 01-03 và 01-04. Cầu nối: sang phần 2, đọc đồ thị chuyển.

## Phần 2. Chuỗi Markov — 18 phút

Vấn đề → ví dụ đồ thị → xác suất chuyển → ma trận → phân phối sau một bước → kiểm tra. Đầu ra là cách đọc P và xác định các bước chuyển hợp lệ, dùng ngay ở phần 3.


### L03-02-01 — Chuỗi Markov

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** Câu hỏi về quy luật sinh nhiều quỹ đạo ở phần1.

**Nội dung trên slide:** Tiêu đề phần, hình các trạng thái nối bằng mũi tên xác suất.

**Cách thể hiện:** Đồ thị sinh viên chưa có thưởng hoặc hành động.

**Giải thích và hình thức hóa:** Chỉ quan sát quá trình di chuyển giữa trạng thái.

**Kết nối:** Từ nhiều quỹ đạo sang quy luật chung sinh chúng.

**Kiểm tra/ghi chú đáp án:** Không thêm ký hiệu mới.

**Nguồn:** PPTX 30–31.

**Quyết định thể hiện khi triển khai:** Slide mở phần dùng lại chính đồ thị sinh viên nhưng lược bỏ mọi thành phần ngoài trạng thái, để hình trực tiếp thể hiện luận điểm: chuỗi Markov chỉ nói về di chuyển giữa trạng thái. Sinh viên năm 3 đã quen đồ thị từ phần 1 nên hình hoạt như cầu nối, không cần câu dẫn dài; một câu duy nhất đặt vấn đề quy luật sinh quỹ đạo là đủ.

### L03-02-02 — Một ngày của sinh viên

Thời lượng: 3 phút. Vai trò: ví dụ trực quan.

**Đầu vào:** Các nút biểu diễn trạng thái; mũi tên biểu diễn chuyển tiếp.

**Nội dung trên slide:** Các trạng thái học, mạng xã hội, giải trí, thi đạt, ngủ; nhãn ngắn đi kèm C1,C2,C3,Pass,Pub,FB,Sleep.

**Cách thể hiện:** Giữ nguyên đồ thị và xác suất nguồn; làm nổi hai cạnh C1→C2 và C1→FB, mỗi cạnh 0,5.

**Giải thích và hình thức hóa:** Đi lần lượt một quỹ đạo nguồn. Nhãn dịch không đổi ý trạng thái; Sleep là điểm dừng của lượt minh họa.

**Kết nối:** Các cạnh ra từ C1 chuẩn bị một hàng ma trận.

**Kiểm tra/ghi chú đáp án:** Tổng xác suất các cạnh ra bằng 1. Một cạnh không vẽ có xác suất 0.

**Nguồn:** PPTX 31–32; Silver PDF7–8.

**Quyết định thể hiện khi triển khai:** Đồ thị lớn chiếm phần trung tâm; quỹ đạo nguồn nằm ở chú thích. Hai cạnh ra từ C1 có nét dày để nối sang định nghĩa xác suất chuyển. Ghi chú diễn giả giải nghĩa C1–C3, FB, Pub, Pass, Sleep. Đầu vào: nút và cạnh; đầu ra: đọc được một quỹ đạo và các khả năng từ C1.

### L03-02-03 — Xác suất chuyển và tính Markov

Thời lượng: 3 phút. Vai trò: hình thức hóa.

**Đầu vào:** Đồ thị C1 có hai cạnh ra xác suất0,5.

**Nội dung trên slide:** Định nghĩa chuỗi hữu hạn đồng nhất theo thời gian bằng $(\mathcal S,P)$ và $P_{ij}=\Pr(S_{t+1}=s_j\mid S_t=s_i)$.

**Cách thể hiện:** Bên trái C1 và các cạnh; bên phải công thức vừa đủ mô tả những cạnh đó.

**Giải thích và hình thức hóa:** Nêu n trạng thái, P có kích thước n×n. Nhắc ngắn tính Markov; không đổi theo thời gian là giả thiết bổ sung, không suy ra từ Markov.

**Kết nối:** Từ một cặp trạng thái đến tất cả cặp trong ma trận.

**Kiểm tra/ghi chú đáp án:** Không diễn giải Markov là “trạng thái tương lai độc lập hoàn toàn với quá khứ”.

**Nguồn:** PPTX 29–30.

**Quyết định thể hiện khi triển khai:** Bố cục hai cột đặt cạnh nhau cặp trạng thái cụ thể và công thức tổng quát, để phép hình thức hóa đi từ ví dụ đến định nghĩa chứ không rơi từ trên xuống. Công thức chỉ gồm hai dòng lớn, đúng giới hạn; tính Markov viết dưới dạng phương trình xác suất thay vì câu chữ mơ hồ, kèm câu tách hai giả thiết — điểm sinh viên năm 3 hay gộp chung.

### L03-02-04 — Từ đồ thị đến ma trận chuyển

Thời lượng: 4 phút. Vai trò: cơ chế và vận dụng.

**Đầu vào:** Định nghĩa P_ij và thứ tự các trạng thái.

**Nội dung trên slide:** Hàng C1 có 0,5 ở C2, 0,5 ở FB và 0 ở các cột khác; $P_{ij}\ge0$, $\sum_jP_{ij}=1$.

**Cách thể hiện:** Đồ thị và hàng ma trận dùng cùng thứ tự; hiện toàn ma trận ở bước sau, không thu nhỏ cả hai hình.

**Giải thích và hình thức hóa:** Giới thiệu trạng thái hấp thụ qua hàng Sleep có phần tử chéo bằng 1. Phân biệt hấp thụ của chuỗi với kết thúc lượt; sau kết thúc có thể quy ước tự lặp với thưởng 0.

**Kết nối:** P biểu diễn mọi phân phối bước tới có điều kiện theo trạng thái hiện tại.

**Kiểm tra/ghi chú đáp án:** Xác định hàng nào sai nếu tổng xác suất khác 1.

**Nguồn:** PPTX 33.

**Quyết định thể hiện khi triển khai:** Bảng HTML giữ thứ tự trạng thái của đồ thị; tô nền hàng C1 để đọc hai phần tử0,5 trước khi xét toàn ma trận. Bỏ dòng véc-tơ C1 trùng với bảng để tránh tràn trang. Điều kiện không âm, tổng hàng bằng1 và Sleep hấp thụ nằm ở chú thích. Đầu vào: xác suất chuyển; đầu ra: mọi phân phối bước tới có điều kiện, dùng ở phép nhân phân phối.

### L03-02-05 — Phân phối sau một bước

Thời lượng: 4 phút. Vai trò: ứng dụng.

**Đầu vào:** Ma trận P chuẩn hóa theo hàng; định luật xác suất toàn phần đã học.

**Nội dung trên slide:** Dồn xác suất từ nhiều trạng thái xuất phát tới các trạng thái đích.

**Cách thể hiện:** Ban đầu, toàn bộ xác suất tập trung ở C1. Sau một bước, C2 và FB mỗi trạng thái có xác suất 0,5. Sau đó minh họa hai mũi tên cùng đi vào một nút.

**Giải thích và hình thức hóa:** Sau phép cộng bằng số, đặt $\mu_t(i)=\Pr(S_t=s_i)$; suy ra $\mu_{t+1}(j)=\sum_i\mu_t(i)P_{ij}$ và $\mu_{t+1}=P^{\mathsf T}\mu_t$. Không dạy phân phối dừng.

**Kết nối:** Phân biệt phân phối tại một thời điểm với một quỹ đạo cụ thể.

**Kiểm tra/ghi chú đáp án:** Nếu bắt đầu ở Sleep thì phân phối sau một bước vẫn tập trung ở Sleep.

**Nguồn:** Vận dụng ma trận PPTX33; bổ sung định luật xác suất toàn phần.

**Quyết định thể hiện khi triển khai:** Slide đi từ phép cộng bằng số cụ thể (0,5 và 0,5) đến công thức véc-tơ, đúng trình tự vấn đề trước định nghĩa. Hình nhỏ dạng short minh họa hai mũi tên cùng vào một nút — bản chất của phép cộng trong định luật toàn phần — không tranh chỗ với công thức. Hai dòng công thức tách thành fragment để bước suy diễn hiện sau khi ví dụ số đã rõ. Hình dùng một phân phối ban đầu khác với ví dụ chắc chắn C1; xác suất FB bằng0,5×0,5+0,5×0,9=0,7. Các số trên cạnh là xác suất có điều kiện, các trọng số50%đặt tại nguồn.

### L03-02-06 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra.

**Đầu vào:** Ma trận chuyển, hàng xác suất và trạng thái hấp thụ.

**Nội dung trên slide:** Bài ba trạng thái: $P=\begin{pmatrix}0{,}5&0{,}5&0\\0{,}2&0{,}3&0{,}5\\0&0&1\end{pmatrix}$.
1. P hợp lệ không? 2. Trạng thái nào hấp thụ? 3. Từ s1, phân phối bước tới là gì?

**Cách thể hiện:** Ma trận lớn và ba câu ngắn, không đặt đồ thị mới phức tạp.

**Giải thích và hình thức hóa:** Ma trận này sẽ được dùng lại để giải Bellman; chưa thêm phần thưởng.

**Kết nối:** Phần 3 giữ quy luật chuyển và thêm thưởng.

**Kiểm tra/ghi chú đáp án:** Hợp lệ; s3 hấp thụ; véc-tơ cột (0,5;0,5;0).

**Nguồn:** hw02 bài3.

**Quyết định thể hiện khi triển khai:** Ma trận được viết lớn bằng KaTeX và ba câu hỏi ngắn đặt trong nhãn Câu hỏi:, không kèm đồ thị mới để trọng tâm ở việc đọc P. Ba câu bám đúng ba kỹ năng của phần: kiểm tra ràng buộc hàng, nhận diện hấp thụ qua phần tử chéo, và đọc phân phối bước tới từ một hàng. Ma trận được chọn để tái sử dụng ở phần Bellman, tạo cầu nối sang phần 3 nơi quy luật chuyển được giữ nguyên và thêm thành phần thưởng.

## Phần 3. Quá trình phần thưởng Markov — 18 phút

Đầu vào: chuỗi Markov. Đầu ra: phân biệt dữ liệu thưởng, tổng trên một mẫu và kỳ vọng giá trị. Ví dụ quỹ đạo đứng trước định nghĩa giá trị; chưa giải Bellman.


### L03-03-01 — Quá trình phần thưởng Markov

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** Chuỗi Markov gồm trạng thái và xác suất chuyển.

**Nội dung trên slide:** Tiêu đề phần và đồ thị sinh viên có thêm nhãn thưởng.

**Cách thể hiện:** Thêm nhãn lên đồ thị quen thuộc, không thay xác suất.

**Giải thích và hình thức hóa:** Đi từ “quá trình xảy ra thế nào” đến “quá trình cho tổng thưởng bao nhiêu”.

**Kết nối:** Đặt nhu cầu đánh giá quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Không thêm một đồ thị khác.

**Nguồn:** PPTX34–35.

**Quyết định thể hiện khi triển khai:** Slide mở phần dùng lại đúng đồ thị phần 2 và chỉ thêm nhãn thưởng, để sinh viên thấy MRP là mở rộng trực tiếp của chuỗi Markov chứ không phải mô hình mới. Tiên quyết: chuỗi Markov, ma trận chuyển, ký hiệu S_t. Cầu nối sang slide thưởng từng bước. Bản triển khai sau rà: công thức dựng bằng KaTeX; SVG chỉ giữ nút, mũi tên và dữ liệu thưởng. Các lỗi hình và dấu được đối chiếu lại với ma trận phần2.

### L03-03-02 — Phần thưởng trên từng bước

Thời lượng: 3 phút. Vai trò: ví dụ.

**Đầu vào:** Các quỹ đạo Student đã đọc ở phần2.

**Nội dung trên slide:** Quỹ đạo C1→C2→C3→Pass→Sleep với thưởng -2,-2,-2,+10.

**Cách thể hiện:** Dải thời gian: trạng thái phía trên, thưởng phía dưới mũi tên.

**Giải thích và hình thức hóa:** Trong ví dụ này $R_{t+1}=r(S_t)$: thưởng gắn với trạng thái xuất phát của bước. +10 nhận khi rời Pass sang Sleep. Nêu rõ để tránh cộng lệch một bước hoặc coi mọi thưởng là thưởng vào trạng thái.

**Kết nối:** Từ bốn giá trị cụ thể đến hàm thưởng r(s).

**Kiểm tra/ghi chú đáp án:** Sau Sleep không có thưởng; quy ước tự lặp với thưởng 0 nếu viết chuỗi vô hạn.

**Nguồn:** PPTX35,40; Silver PDF11,15.

**Quyết định thể hiện khi triển khai:** Dải thời gian đặt trạng thái phía trên và thưởng phía dưới mũi tên để chỉ số thời gian hiện rõ trên hình, đúng chỗ dễ nhầm của sinh viên năm 3: lệch một bước trong R_{t+1}. Câu ngắn, một luận điểm. Tiên quyết: quỹ đạo đã đọc ở phần 2; cầu nối tới hàm r(s) ở slide định nghĩa. Bản triển khai sau rà: công thức dựng bằng KaTeX; SVG chỉ giữ nút, mũi tên và dữ liệu thưởng. Các lỗi hình và dấu được đối chiếu lại với ma trận phần2.

### L03-03-03 — Định nghĩa quá trình phần thưởng Markov

Thời lượng: 3 phút. Vai trò: hình thức hóa.

**Đầu vào:** Các thưởng -2,-2,-2,+10 trên từng bước.

**Nội dung trên slide:** Quá trình phần thưởng Markov (MRP): $(\mathcal S,P,r,\gamma)$; $r(s)=\mathbb E[R_{t+1}\mid S_t=s]$.

**Cách thể hiện:** Liên kết từng thành phần với nút, cạnh, nhãn thưởng và trọng số thời gian trên hình trước.

**Giải thích và hình thức hóa:** r là véc-tơ n thành phần khi liệt kê trạng thái; có thể là kỳ vọng của thưởng ngẫu nhiên. Phân phối phản hồi bước tới, có điều kiện theo lịch sử, chỉ phụ thuộc trạng thái hiện tại; quy luật không đổi theo thời gian. Miền mặc định: n hữu hạn, thưởng bị chặn, $0\le\gamma<1$; ví dụ kết thúc có thể dùng gamma=1 với điều kiện nêu sau.

**Kết nối:** Từ mô hình thưởng tới tính tổng của một quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Phân biệt số r(s) với quan sát thưởng R ở một lần chuyển.

**Nguồn:** PPTX34–35.

**Quyết định thể hiện khi triển khai:** Định nghĩa đặt trong hộp với ba dòng, mỗi thành phần nối về nút, cạnh, nhãn thưởng và trọng số thời gian của hình trước, giúp sinh viên năm 3 gắn ký hiệu mới vào đồ thị quen. Không đưa Bellman vào đây; slide kết thúc ở cấu trúc (S, P, r, gamma) và mở sang tính tổng một quỹ đạo. Bản triển khai sau rà: công thức dựng bằng KaTeX; SVG chỉ giữ nút, mũi tên và dữ liệu thưởng. Các lỗi hình và dấu được đối chiếu lại với ma trận phần2.

### L03-03-04 — Hai quỹ đạo, hai tổng thưởng

Thời lượng: 4 phút. Vai trò: ví dụ tính toán.

**Đầu vào:** P, r(s), gamma; quy ước thưởng ở trạng thái rời đi.

**Nội dung trên slide:** Với $\gamma=1/2$: C1→C2→C3→Pass→Sleep cho -2,25; C1→FB→FB→C1→C2→Sleep cho -3,125.

**Cách thể hiện:** Hai dải thời gian, mỗi dòng chỉ một phép cộng có chiết khấu.

**Giải thích và hình thức hóa:** Tính $-2-1-0{,}5+1{,}25=-2{,}25$ và $-2-0{,}5-0{,}25-0{,}25-0{,}125=-3{,}125$. Nhắc $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$ với thưởng 0 sau kết thúc.

**Kết nối:** Hai tổng khác nhau dẫn tới nhu cầu một giá trị đại diện theo phân phối.

**Kiểm tra/ghi chú đáp án:** Đây là hai mẫu, không lấy trung bình đơn giản của chúng để tuyên bố giá trị chính xác.

**Nguồn:** PPTX36–40.

**Quyết định thể hiện khi triển khai:** Một hình chứa hai dải thời gian, mỗi dòng trên mặt slide chỉ một phép cộng có chiết khấu, đúng giới hạn ba bốn dòng công thức lớn. Số mũ gamma đặt trên từng mũi tên để phép nhân với chiết khấu nhìn thấy được thay vì chỉ xuất hiện trong công thức. Cầu nối: hai tổng khác nhau cùng xuất phát từ C1 dẫn tới định nghĩa kỳ vọng ở slide sau. Bản triển khai sau rà: công thức dựng bằng KaTeX; SVG chỉ giữ nút, mũi tên và dữ liệu thưởng. Các lỗi hình và dấu được đối chiếu lại với ma trận phần2.

### L03-03-05 — Giá trị của một trạng thái

Thời lượng: 4 phút. Vai trò: trực giác → định nghĩa.

**Đầu vào:** Hai tổng mẫu -2,25 và -3,125 từ cùng C1; khái niệm kỳ vọng.

**Nội dung trên slide:** Từ cùng C1 có nhiều quỹ đạo và tổng khác nhau; $v(s)=\mathbb E[G_t\mid S_t=s]$.

**Cách thể hiện:** Một nút tỏa ra nhiều quỹ đạo; đặt từng tổng ở cuối; bao nhóm bằng ký hiệu kỳ vọng.

**Giải thích và hình thức hóa:** Kỳ vọng dùng xác suất do mô hình sinh, không phải trung bình không trọng số của vài đường tùy chọn. v(s) là một số, G là biến ngẫu nhiên. Giá trị lớn có thể đến từ thưởng muộn.

**Kết nối:** Phần 4 sẽ tính v mà không liệt kê vô hạn quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Tại Sleep, v=0 dưới quy ước kết thúc; chưa đưa bảng v đầy đủ khi chưa có cách tính.

**Nguồn:** PPTX39–43.

**Quyết định thể hiện khi triển khai:** Hình một nút tỏa ra nhiều quỹ đạo với tổng đặt ở cuối từng nhánh, bao nhóm bằng ký hiệu kỳ vọng trong công thức phía dưới, thể hiện đúng bước trực giác sang định nghĩa. Sinh viên năm 3 đã biết kỳ vọng nên trọng tâm là phân biệt biến ngẫu nhiên G với giá trị kỳ vọng v. Cầu nối: phần 4 tính v mà không liệt kê vô hạn quỹ đạo. Bản triển khai sau rà: công thức dựng bằng KaTeX; SVG chỉ giữ nút, mũi tên và dữ liệu thưởng. Các lỗi hình và dấu được đối chiếu lại với ma trận phần2.

### L03-03-06 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra.

**Đầu vào:** Phân biệt thưởng một bước, tổng mẫu, kỳ vọng tổng.

**Nội dung trên slide:** 1. r(s), G và v(s) khác nhau thế nào? 2. Tính tổng đường C1→C2→Sleep với gamma=1/2. 3. Một mẫu G có bằng v(s) không?

**Cách thể hiện:** Ba câu đánh số; một dải thời gian nhỏ cho câu 2.

**Giải thích và hình thức hóa:** Chỉ dùng thưởng và ký hiệu đã giới thiệu.

**Kết nối:** Khép phân biệt mẫu/kỳ vọng, mở bài toán tính v từ một bước.

**Kiểm tra/ghi chú đáp án:** 1. Kỳ vọng thưởng một bước/tổng một mẫu/kỳ vọng tổng. 2. -3. 3. Không nhất thiết.

**Nguồn:** PPTX34–40.

**Quyết định thể hiện khi triển khai:** Ba câu bám sát ba đại lượng của phần: thưởng một bước, tổng mẫu, kỳ vọng. Dải thời gian nhỏ cho câu 2 giúp làm bài trực tiếp trên mặt slide mà không cần vẽ lại. Cầu nối sang phần 4: tổng G được viết lại thành quan hệ đệ quy giữa v(s) và v(s'). Bản triển khai sau rà: công thức dựng bằng KaTeX; SVG chỉ giữ nút, mũi tên và dữ liệu thưởng. Các lỗi hình và dấu được đối chiếu lại với ma trận phần2.
