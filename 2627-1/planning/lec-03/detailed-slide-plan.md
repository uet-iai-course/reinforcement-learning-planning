# Bài 03 — Kế hoạch chi tiết từng slide

Ngày lập: 2026-09-19. Trạng thái: đang triển khai, đã tích hợp phần 1–5/7; các phần sau chưa hoàn tất. Các ID `L03-…` dùng cho bản viết lại; outline và storyboard ghi phạm vi đã tích hợp thực tế.

## Mục tiêu và phạm vi

Sinh viên năm 3 đã học học máy, học sâu, xác suất và thuật toán; đã học Bài 02 về trạng thái, quan sát, chính sách, tổng thưởng và mô hình chuyển. Sau Bài 03, sinh viên có thể đọc một mô hình hữu hạn, suy ra phương trình giá trị và đánh giá một chính sách cố định.

- 47 slide, gồm 1 slide tiêu đề bài, 1 slide nội dung bài học, 7 slide mở phần và 7 slide câu hỏi kiểm tra; 120 phút trình bày và hoạt động ngắn trong lớp.
- 30 phút chữa bài tập nguồn, tách khỏi 120 phút. Không tạo code demo mới.
- Toàn bài mở bằng slide tiêu đề “Quá trình quyết định Markov”, tiếp theo là slide “Nội dung bài học”; cả hai nằm trong phần 1. Sau đó mới đến slide mở phần “Từ tương tác đến mô hình xác suất” và các slide còn lại của phần 1. Các phần 2–7 bắt đầu ngay bằng slide tiêu đề phần. Slide mở phần có một hình gợi tình huống và tối đa một câu dẫn, không có danh sách công thức.
- Mỗi khái niệm mới đi từ vấn đề, ví dụ trực quan và phép tính cụ thể tới định nghĩa/công thức; sau đó vận dụng và kiểm tra. Các trường hợp rút gọn được ghi ở từng phần.
- Giữ giả thiết mô hình đã biết, hữu hạn và không đổi theo thời gian. Tính Markov và tính không đổi theo thời gian là hai giả thiết riêng. Quan sát đầy đủ không đồng nghĩa biết mô hình.
- Tập trung Bellman kỳ vọng; Bellman tối ưu, lặp giá trị và lặp chính sách thuộc Bài 04.
- Khi triển khai: dùng `lecture-slide.css`, RevealJS cục bộ, SVG có nhãn và mô tả thay thế, KaTeX cho công thức. Chỉ đưa nội dung học thuật và mạch nói vào HTML/notes; các hướng dẫn dựng hình, thời lượng và ID trong tài liệu này là thông tin nội bộ.

## Nguồn và cách sử dụng

1. **Nguồn chính:** `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 28–58. Giữ tuyến chuỗi Markov → quá trình phần thưởng Markov → Bellman → MDP → Bellman kỳ vọng. Bài tập: `RL-hk2-2025-2026/resources/hw02.pdf`, bài 3, 4, 7, 8.
2. [David Silver, Lecture 2: Markov Decision Processes](https://web.stanford.edu/class/cme241/lecture_slides/david_silver_slides/MDP.pdf): ví dụ sinh viên và sơ đồ nhìn trước một bước; trang PDF 7–9, 10–23, 24–34. Không lấy phần tối ưu và các mở rộng ngoài phạm vi.
3. [Berkeley CS188, Fall 2025, Lecture 8](https://inst.eecs.berkeley.edu/~cs188/fa25/assets/lectures/cs188-fa25-lec08.pdf): cách phân biệt nút hành động/nút ngẫu nhiên, ví dụ xe đua; trang PDF 20–22. Không sao chép CSS hoặc tài sản.
4. [Stanford CS234, ghi chú Lecture 2 của Rahul Sarkar và Emma Brunskill](https://web.stanford.edu/~rsarkar/materials/lecture2-CS234.pdf): kiểm tra giả thiết, chuyển từ đồ thị sang ma trận và đánh giá khi biết mô hình. Đây là ghi chú bài giảng, không phải bộ slide để sao chép bố cục.

Ví dụ sinh viên là mạch chính. Bài tập ba trạng thái là ví dụ tính toán nhỏ để giải hệ; xe đua là bài vận dụng chuyển sang tình huống khác. Không thêm một ví dụ lớn thứ ba. Mọi xác suất và thưởng giữ theo nguồn; quy ước xe quá nhiệt nhận -10, không cộng thêm +2, được nêu rõ trước khi tính.

## Phân bổ

| Phần | Tiêu đề mở phần | Slide | Phút |
|---|---|---:|---:|
| 1 | Từ tương tác đến mô hình xác suất | 6 | 8 |
| 2 | Chuỗi Markov | 6 | 18 |
| 3 | Quá trình phần thưởng Markov | 6 | 18 |
| 4 | Phương trình Bellman | 9 | 24 |
| 5 | MDP và chính sách cố định | 7 | 20 |
| 6 | Giá trị trạng thái và giá trị hành động | 9 | 24 |
| 7 | Tổng hợp và vận dụng | 4 | 8 |
| **Tổng** | | **47** | **120** |

47 slide nhiều hơn ước lượng ban đầu 36–40 vì có slide tiêu đề bài, slide nội dung bài học, 7 trang mở phần và các bước suy diễn được tách riêng. Không tăng số khái niệm hoặc thời lượng. Phần 4 và 6 dành tổng 48 phút cho Bellman; các slide mở phần chỉ 1 phút. Phần 1 có sáu slide trong 8 phút: 1 + 1 + 1 + 2 + 1 + 2.

## Ký hiệu và thứ tự xuất hiện

| Ký hiệu/khái niệm | Nơi xuất hiện chính thức | Chuẩn bị bằng ví dụ |
|---|---|---|
| Trạng thái, Markov, tổng thưởng, chính sách | Đã có ở Bài 02; chỉ nhắc ngắn | 01-04 |
| $P_{ij}$, ma trận chuyển | 02-03 | Các cạnh ra ở 02-02 |
| Phân phối trạng thái $\mu_t$ | 02-05 | Dồn xác suất theo các cạnh bằng số trước |
| Thưởng trung bình $r(s)$, quá trình phần thưởng Markov (MRP) | 03-03 | Gắn thưởng vào bước chuyển ở 03-02 |
| $G_t$ và $v(s)$ của MRP | 03-04/05 | Hai quỹ đạo với tổng khác nhau |
| Bellman, dạng hệ tuyến tính | 04-03…07 | Nhánh một bước ở 04-02 |
| Quá trình quyết định Markov (MDP), $P(s',r\mid s,a)$ | 05-03 | Lựa chọn học/nghỉ ở 05-02 |
| $P^\pi,r^\pi$ | 05-06 | Gộp nút hành động trên hình ở 05-05 |
| $q_\pi(s,a)$ | 06-03 | So sánh hai hành động đầu tiên ở 06-02 |
| Bellman kỳ vọng theo $v_\pi,q_\pi$ | 06-04…07 | Cùng sơ đồ trạng thái → hành động → phản hồi |

$P$ trong chuỗi Markov là ma trận; $P(s',r\mid s,a)$ trong MDP là xác suất chung, tiếp nối ký hiệu Bài 02. $r(s)$ và $r^\pi(s)$ là kỳ vọng của phần thưởng, khác biến ngẫu nhiên $R_{t+1}$. Dùng véc-tơ cột cho $v,r,\mu$; do P chuẩn hóa theo hàng, $\mu_{t+1}=P^{\mathsf T}\mu_t$. Xét chính sách Markov dừng khi viết giá trị không có chỉ số thời gian; không khẳng định mọi chính sách đều thuộc lớp này.

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

### L03-01-02 — Nội dung bài học

Thời lượng: 1 phút. Vai trò: định hướng toàn bài.

**Đầu vào:** Tên và mục tiêu Bài 03.

**Nội dung trên slide:** Bảy phần theo thứ tự: 1. Từ tương tác đến mô hình xác suất; 2. Chuỗi Markov; 3. Quá trình phần thưởng Markov; 4. Phương trình Bellman; 5. MDP và chính sách cố định; 6. Giá trị trạng thái và giá trị hành động; 7. Tổng hợp và vận dụng.

**Cách thể hiện:** Danh sách hai cột hoặc sơ đồ bảy mục, đánh dấu phần 1. Không hiện thời lượng, ID hoặc chỉ dẫn tác giả.

**Giải thích và hình thức hóa:** Các tên gọi mới chỉ xuất hiện như tên nội dung, chưa yêu cầu sinh viên hiểu định nghĩa. Khi nói, diễn đạt mạch bằng lời: mô tả chuyển tiếp, thêm thưởng, đánh giá tương lai, rồi xét lựa chọn hành động. “Quá trình quyết định Markov (MDP)” được viết đầy đủ trong mục 5 khi dựng slide.

**Kết nối:** Sang slide mở phần 1, rồi ví dụ một mô hình sinh nhiều quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Không thêm kiểm tra tại trang nội dung; phần 1 kết thúc bằng câu hỏi riêng.

**Nguồn:** Dàn ý bảy phần đã được thống nhất; PPTX28–58.

### L03-01-03 — Từ tương tác đến mô hình xác suất

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** Bản đồ bài học ở 01-02 và giao diện tác tử–môi trường từ Bài02.

**Nội dung trên slide:** Tiêu đề phần và câu: “Cùng trạng thái và hành động có thể cho kết quả khác nhau.”

**Cách thể hiện:** Một nút hiện tại, một hành động và hai kết quả; chưa đặt bộ ký hiệu MDP.

**Giải thích và hình thức hóa:** Nhắc lại vòng tương tác bằng lời; bài này giả sử đã biết xác suất chuyển.

**Kết nối:** Từ một bước tương tác sang nhiều khả năng diễn tiến.

**Kiểm tra/ghi chú đáp án:** Không đặt câu hỏi riêng trên trang mở.

**Nguồn:** PPTX 28–29; nối Bài 02.

### L03-01-04 — Một mô hình, nhiều quỹ đạo

Thời lượng: 2 phút. Vai trò: vấn đề và trực giác.

**Đầu vào:** Một bước có thể có nhiều kết quả; trạng thái quan sát được.

**Nội dung trên slide:** Hai đường đi từ cùng điểm xuất phát trên đồ thị sinh viên.

**Cách thể hiện:** Chỉ hiện các nút liên quan đến hai đường; cùng điểm xuất phát và cùng kết thúc Sleep, hai diễn tiến khác nhau.

**Giải thích và hình thức hóa:** Quỹ đạo là một kết quả lấy mẫu. Mô hình là quy luật sinh ra cả các quỹ đạo chưa quan sát; chưa đồng nhất hai tổng cụ thể với kỳ vọng.

**Kết nối:** Từ sự khác nhau của đường đi đến việc phải dùng phân phối.

**Kiểm tra/ghi chú đáp án:** Một đường quan sát được có xác định hết xác suất chuyển không? Không.

**Nguồn:** PPTX 31–32.

### L03-01-05 — Ba lớp mô hình

Thời lượng: 1 phút. Vai trò: bản đồ khái niệm.

**Đầu vào:** Hai quỹ đạo từ cùng điểm đầu; nhu cầu mô tả quy luật sinh chúng.

**Nội dung trên slide:** Chuỗi trạng thái → thêm thưởng → thêm lựa chọn hành động.

**Cách thể hiện:** Ba hình dùng cùng các nút; lần lượt thêm nhãn thưởng và nút lựa chọn.

**Giải thích và hình thức hóa:** Gọi đầy đủ ba tên bằng tiếng Việt; chưa yêu cầu ghi nhớ các bộ thành phần hoặc viết tắt.

**Kết nối:** Phần 2 bắt đầu bằng lớp đơn giản nhất.

**Kiểm tra/ghi chú đáp án:** Đầu ra cần đạt cuối bài: từ mô hình và chính sách viết được phương trình giá trị.

**Nguồn:** PPTX 30,34,49.

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

### L03-02-02 — Một ngày của sinh viên

Thời lượng: 3 phút. Vai trò: ví dụ trực quan.

**Đầu vào:** Các nút biểu diễn trạng thái; mũi tên biểu diễn chuyển tiếp.

**Nội dung trên slide:** Các trạng thái học, mạng xã hội, giải trí, thi đạt, ngủ; nhãn ngắn đi kèm C1,C2,C3,Pass,Pub,FB,Sleep.

**Cách thể hiện:** Giữ nguyên đồ thị và xác suất nguồn; làm nổi hai cạnh C1→C2 và C1→FB, mỗi cạnh 0,5.

**Giải thích và hình thức hóa:** Đi lần lượt một quỹ đạo nguồn. Nhãn dịch không đổi ý trạng thái; Sleep là điểm dừng của lượt minh họa.

**Kết nối:** Các cạnh ra từ C1 chuẩn bị một hàng ma trận.

**Kiểm tra/ghi chú đáp án:** Tổng xác suất các cạnh ra bằng 1. Một cạnh không vẽ có xác suất 0.

**Nguồn:** PPTX 31–32; Silver PDF7–8.

### L03-02-03 — Xác suất chuyển và tính Markov

Thời lượng: 3 phút. Vai trò: hình thức hóa.

**Đầu vào:** Đồ thị C1 có hai cạnh ra xác suất0,5.

**Nội dung trên slide:** Định nghĩa chuỗi hữu hạn đồng nhất theo thời gian bằng $(\mathcal S,P)$ và $P_{ij}=\Pr(S_{t+1}=s_j\mid S_t=s_i)$.

**Cách thể hiện:** Bên trái C1 và các cạnh; bên phải công thức vừa đủ mô tả những cạnh đó.

**Giải thích và hình thức hóa:** Nêu n trạng thái, P có kích thước n×n. Nhắc ngắn tính Markov; không đổi theo thời gian là giả thiết bổ sung, không suy ra từ Markov.

**Kết nối:** Từ một cặp trạng thái đến tất cả cặp trong ma trận.

**Kiểm tra/ghi chú đáp án:** Không diễn giải Markov là “trạng thái tương lai độc lập hoàn toàn với quá khứ”.

**Nguồn:** PPTX 29–30.

### L03-02-04 — Từ đồ thị đến ma trận chuyển

Thời lượng: 4 phút. Vai trò: cơ chế và vận dụng.

**Đầu vào:** Định nghĩa P_ij và thứ tự các trạng thái.

**Nội dung trên slide:** Hàng C1 có 0,5 ở C2, 0,5 ở FB và 0 ở các cột khác; $P_{ij}\ge0$, $\sum_jP_{ij}=1$.

**Cách thể hiện:** Đồ thị và hàng ma trận dùng cùng thứ tự; hiện toàn ma trận ở bước sau, không thu nhỏ cả hai hình.

**Giải thích và hình thức hóa:** Giới thiệu trạng thái hấp thụ qua hàng Sleep có phần tử chéo bằng 1. Phân biệt hấp thụ của chuỗi với kết thúc lượt; sau kết thúc có thể quy ước tự lặp với thưởng 0.

**Kết nối:** P biểu diễn mọi phân phối bước tới có điều kiện theo trạng thái hiện tại.

**Kiểm tra/ghi chú đáp án:** Xác định hàng nào sai nếu tổng xác suất khác 1.

**Nguồn:** PPTX 33.

### L03-02-05 — Phân phối sau một bước

Thời lượng: 4 phút. Vai trò: ứng dụng.

**Đầu vào:** Ma trận P chuẩn hóa theo hàng; định luật xác suất toàn phần đã học.

**Nội dung trên slide:** Dồn xác suất từ nhiều trạng thái xuất phát tới các trạng thái đích.

**Cách thể hiện:** Ban đầu, toàn bộ xác suất tập trung ở C1. Sau một bước, C2 và FB mỗi trạng thái có xác suất 0,5. Sau đó minh họa hai mũi tên cùng đi vào một nút.

**Giải thích và hình thức hóa:** Sau phép cộng bằng số, đặt $\mu_t(i)=\Pr(S_t=s_i)$; suy ra $\mu_{t+1}(j)=\sum_i\mu_t(i)P_{ij}$ và $\mu_{t+1}=P^{\mathsf T}\mu_t$. Không dạy phân phối dừng.

**Kết nối:** Phân biệt phân phối tại một thời điểm với một quỹ đạo cụ thể.

**Kiểm tra/ghi chú đáp án:** Nếu bắt đầu ở Sleep thì phân phối sau một bước vẫn tập trung ở Sleep.

**Nguồn:** Vận dụng ma trận PPTX33; bổ sung định luật xác suất toàn phần.

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

### L03-03-02 — Phần thưởng trên từng bước

Thời lượng: 3 phút. Vai trò: ví dụ.

**Đầu vào:** Các quỹ đạo Student đã đọc ở phần2.

**Nội dung trên slide:** Quỹ đạo C1→C2→C3→Pass→Sleep với thưởng -2,-2,-2,+10.

**Cách thể hiện:** Dải thời gian: trạng thái phía trên, thưởng phía dưới mũi tên.

**Giải thích và hình thức hóa:** Trong ví dụ này $R_{t+1}=r(S_t)$: thưởng gắn với trạng thái xuất phát của bước. +10 nhận khi rời Pass sang Sleep. Nêu rõ để tránh cộng lệch một bước hoặc coi mọi thưởng là thưởng vào trạng thái.

**Kết nối:** Từ bốn giá trị cụ thể đến hàm thưởng r(s).

**Kiểm tra/ghi chú đáp án:** Sau Sleep không có thưởng; quy ước tự lặp với thưởng 0 nếu viết chuỗi vô hạn.

**Nguồn:** PPTX35,40; Silver PDF11,15.

### L03-03-03 — Định nghĩa quá trình phần thưởng Markov

Thời lượng: 3 phút. Vai trò: hình thức hóa.

**Đầu vào:** Các thưởng -2,-2,-2,+10 trên từng bước.

**Nội dung trên slide:** Quá trình phần thưởng Markov (MRP): $(\mathcal S,P,r,\gamma)$; $r(s)=\mathbb E[R_{t+1}\mid S_t=s]$.

**Cách thể hiện:** Liên kết từng thành phần với nút, cạnh, nhãn thưởng và trọng số thời gian trên hình trước.

**Giải thích và hình thức hóa:** r là véc-tơ n thành phần khi liệt kê trạng thái; có thể là kỳ vọng của thưởng ngẫu nhiên. Phân phối phản hồi bước tới, có điều kiện theo lịch sử, chỉ phụ thuộc trạng thái hiện tại; quy luật không đổi theo thời gian. Miền mặc định: n hữu hạn, thưởng bị chặn, $0\le\gamma<1$; ví dụ kết thúc có thể dùng gamma=1 với điều kiện nêu sau.

**Kết nối:** Từ mô hình thưởng tới tính tổng của một quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Phân biệt số r(s) với quan sát thưởng R ở một lần chuyển.

**Nguồn:** PPTX34–35.

### L03-03-04 — Hai quỹ đạo, hai tổng thưởng

Thời lượng: 4 phút. Vai trò: ví dụ tính toán.

**Đầu vào:** P, r(s), gamma; quy ước thưởng ở trạng thái rời đi.

**Nội dung trên slide:** Với $\gamma=1/2$: C1→C2→C3→Pass→Sleep cho -2,25; C1→FB→FB→C1→C2→Sleep cho -3,125.

**Cách thể hiện:** Hai dải thời gian, mỗi dòng chỉ một phép cộng có chiết khấu.

**Giải thích và hình thức hóa:** Tính $-2-1-0{,}5+1{,}25=-2{,}25$ và $-2-0{,}5-0{,}25-0{,}25-0{,}125=-3{,}125$. Nhắc $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$ với thưởng 0 sau kết thúc.

**Kết nối:** Hai tổng khác nhau dẫn tới nhu cầu một giá trị đại diện theo phân phối.

**Kiểm tra/ghi chú đáp án:** Đây là hai mẫu, không lấy trung bình đơn giản của chúng để tuyên bố giá trị chính xác.

**Nguồn:** PPTX36–40.

### L03-03-05 — Giá trị của một trạng thái

Thời lượng: 4 phút. Vai trò: trực giác → định nghĩa.

**Đầu vào:** Hai tổng mẫu -2,25 và -3,125 từ cùng C1; khái niệm kỳ vọng.

**Nội dung trên slide:** Từ cùng C1 có nhiều quỹ đạo và tổng khác nhau; $v(s)=\mathbb E[G_t\mid S_t=s]$.

**Cách thể hiện:** Một nút tỏa ra nhiều quỹ đạo; đặt từng tổng ở cuối; bao nhóm bằng ký hiệu kỳ vọng.

**Giải thích và hình thức hóa:** Kỳ vọng dùng xác suất do mô hình sinh, không phải trung bình không trọng số của vài đường tùy chọn. v(s) là một số, G là biến ngẫu nhiên. Giá trị lớn có thể đến từ thưởng muộn.

**Kết nối:** Phần 4 sẽ tính v mà không liệt kê vô hạn quỹ đạo.

**Kiểm tra/ghi chú đáp án:** Tại Sleep, v=0 dưới quy ước kết thúc; chưa đưa bảng v đầy đủ khi chưa có cách tính.

**Nguồn:** PPTX39–43.

### L03-03-06 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra.

**Đầu vào:** Phân biệt thưởng một bước, tổng mẫu, kỳ vọng tổng.

**Nội dung trên slide:** 1. r(s), G và v(s) khác nhau thế nào? 2. Tính tổng đường C1→C2→Sleep với gamma=1/2. 3. Một mẫu G có bằng v(s) không?

**Cách thể hiện:** Ba câu đánh số; một dải thời gian nhỏ cho câu 2.

**Giải thích và hình thức hóa:** Chỉ dùng thưởng và ký hiệu đã giới thiệu.

**Kết nối:** Khép phân biệt mẫu/kỳ vọng, mở bài toán tính v từ một bước.

**Kiểm tra/ghi chú đáp án:** 1. Kỳ vọng thưởng một bước/tổng một mẫu/kỳ vọng tổng. 2. -3. 3. Không nhất thiết.

**Nguồn:** PPTX34–40.

## Phần 4. Phương trình Bellman — 24 phút

Đầu vào: P, r, G và v. Đầu ra: lập hệ Bellman và kiểm tra nghiệm. Suy diễn được tách thành ba trang 04-03…05; sau đó áp dụng, viết ma trận và nêu điều kiện. Không dùng các thuật ngữ ánh xạ co, bán kính phổ hoặc chuỗi Neumann trước khi định nghĩa; chúng không thuộc tuyến chính.

### L03-04-01 — Phương trình Bellman

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** G và v(s) cùng việc không thể liệt kê hết các quỹ đạo.

**Nội dung trên slide:** Tiêu đề phần và câu: “Tính giá trị từ một bước chuyển và phần đường còn lại.”

**Cách thể hiện:** Một nút hiện tại, hai nhánh kế tiếp và các phần đuôi được đóng thành hộp.

**Giải thích và hình thức hóa:** Không đặt công thức kết quả ngay trên trang mở.

**Kết nối:** Từ nhiều quỹ đạo ở phần 3 đến cách gộp phần tương lai.

**Kiểm tra/ghi chú đáp án:** Chưa yêu cầu tính giá trị chưa biết.

**Nguồn:** PPTX44.

### L03-04-02 — Một bước và phần còn lại

Thời lượng: 3 phút. Vai trò: trực giác trên ví dụ.

**Đầu vào:** C3 tới Pass/Pub; thưởng -2 và xác suất0,6/0,4.

**Nội dung trên slide:** Từ C3: nhận -2, rồi tới Pass với xác suất 0,6 hoặc Pub với xác suất 0,4; dùng $\gamma=0{,}9$.

**Cách thể hiện:** Tách hình thành nhãn thưởng ngay và hai hộp “giá trị từ Pass”, “giá trị từ Pub”; không cho giá trị số chưa tính.

**Giải thích và hình thức hóa:** Mỗi hộp đại diện kỳ vọng của toàn bộ phần còn lại. Bằng lời: giá trị tại C3 bằng -2 cộng 0,9 lần trung bình có trọng số của hai giá trị kế tiếp. Giữ các giá trị này là ẩn.

**Kết nối:** Từ cách nhìn trên hình sang tách chính xác tổng G.

**Kiểm tra/ghi chú đáp án:** Không gán 10 và 1 là nghiệm v của hai nút nếu chưa kiểm mô hình.

**Nguồn:** PPTX35,44–46.

### L03-04-03 — Tách phần thưởng tích lũy

Thời lượng: 3 phút. Vai trò: suy diễn 1: đồng nhất thức.

**Đầu vào:** Định nghĩa tổng thưởng và giá trị phần đuôi.

**Nội dung trên slide:** Hiện lần lượt ba dòng:

$$
\begin{aligned}
G_t&=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots\\
&=R_{t+1}+\gamma\big(R_{t+2}+\gamma R_{t+3}+\cdots\big)\\
&=R_{t+1}+\gamma G_{t+1}.
\end{aligned}
$$

**Cách thể hiện:** Dải thời gian; khoanh phần đuôi cùng màu với G ở dòng cuối.

**Giải thích và hình thức hóa:** Dòng 1 là định nghĩa; dòng 2 đặt gamma ra ngoài; dòng 3 nhận diện tổng bắt đầu ở t+1. Với lượt hữu hạn, dừng tại T và đặt G_T=0. Đây là đẳng thức trên mỗi quỹ đạo, không cần Markov, tính dừng hoặc phép lấy kỳ vọng.

**Kết nối:** Sang bước lấy kỳ vọng theo trạng thái hiện tại.

**Kiểm tra/ghi chú đáp án:** Số hạng đầu của $G_{t+1}$ là $R_{t+2}$, không phải $R_{t+1}$.

**Nguồn:** PPTX44; Silver PDF19.

### L03-04-04 — Từ tổng thưởng đến giá trị

Thời lượng: 3 phút. Vai trò: suy diễn 2: tuyến tính và kỳ vọng lặp.

**Đầu vào:** Đẳng thức tách G từ04-03; định nghĩa v và r.

**Nội dung trên slide:** Hai dòng chính:

$$
\begin{aligned}
v(s)&=\mathbb E[R_{t+1}+\gamma G_{t+1}\mid S_t=s]\\
&=r(s)+\gamma\mathbb E[G_{t+1}\mid S_t=s].
\end{aligned}
$$

Sau đó khai triển phần tương lai:

$$
\mathbb E[G_{t+1}\mid S_t=s]
=\mathbb E\!\left[\mathbb E[G_{t+1}\mid S_t,S_{t+1}]\mid S_t=s\right].
$$

**Cách thể hiện:** Dòng suy diễn xuất hiện lần lượt. Bên phải là nút s phân nhánh theo S_(t+1), khớp với kỳ vọng trong/ngoài. Không dồn cả chứng minh lên một lần hiện.

**Giải thích và hình thức hóa:** Dòng đầu thế kết quả trước vào định nghĩa v. Dòng sau dùng tính tuyến tính và định nghĩa r(s). Dòng cuối dùng kỳ vọng lặp: trung bình trong từng nhóm có cùng trạng thái kế tiếp, rồi trung bình giữa các nhóm. Không giả định thưởng độc lập với trạng thái kế tiếp.

**Kết nối:** Kỳ vọng bên trong sẽ được nhận diện là giá trị của trạng thái kế tiếp.

**Kiểm tra/ghi chú đáp án:** Notes giải thích điều kiện tính được kỳ vọng đã nêu ở phần 3; chỉ xét các biến cố có xác suất dương khi viết theo từng giá trị.

**Nguồn:** PPTX44–45; bổ sung bước kỳ vọng lặp.

### L03-04-05 — Bellman cho quá trình phần thưởng Markov

Thời lượng: 3 phút. Vai trò: suy diễn 3: Markov và tổng theo trạng thái.

**Đầu vào:** Biểu thức kỳ vọng lặp từ04-04; Markov và quy luật không đổi theo thời gian.

**Nội dung trên slide:** Với chuyển tiếp có thể xảy ra:

$$
\mathbb E[G_{t+1}\mid S_t=s,S_{t+1}=s']=v(s').
$$

Suy ra lần lượt:

$$
\begin{aligned}
v(s)&=r(s)+\gamma\mathbb E[v(S_{t+1})\mid S_t=s]\\
&=r(s)+\gamma\sum_{s'}P_{ss'}v(s').
\end{aligned}
$$

**Cách thể hiện:** Thay hai hộp tương lai ở 04-02 bằng v(Pass), v(Pub); ghi nhãn “Markov” cạnh phép thay và “lấy trung bình” cạnh dấu tổng.

**Giải thích và hình thức hóa:** Tính Markov của quá trình có thưởng cho phép bỏ thông tin trạng thái trước; quy luật không đổi theo thời gian cho phép dùng cùng hàm v tại t và t+1. Trở lại ví dụ: v(C3)=-2+0,9[0,6v(Pass)+0,4v(Pub)]. Đây là quan hệ giữa các giá trị chưa biết, không phải phép gán đáp số tùy ý.

**Kết nối:** Mỗi trạng thái cho một phương trình; tập các phương trình tạo thành hệ.

**Kiểm tra/ghi chú đáp án:** Sinh viên chỉ được giả thiết dùng tại từng dấu bằng; không nói “do Markov” cho bước đặt gamma ra ngoài tổng.

**Nguồn:** PPTX45–46.

### L03-04-06 — Hệ Bellman ba trạng thái

Thời lượng: 3 phút. Vai trò: ứng dụng vào dữ liệu đã biết.

**Đầu vào:** Bellman MRP và ma trận ba trạng thái đã đọc ở02-06.

**Nội dung trên slide:** Dùng lại ma trận ở 02-06; thêm $r=(1,-1,0)^{\mathsf T}$, $\gamma=0{,}9$:

$$
\begin{aligned}
v_1&=1+0{,}9(0{,}5v_1+0{,}5v_2),\\
v_2&=-1+0{,}9(0{,}2v_1+0{,}3v_2+0{,}5v_3),\\
v_3&=0+0{,}9v_3=0.
\end{aligned}
$$

**Cách thể hiện:** Hiện một hàng P rồi phương trình tương ứng; nhãn v_i=v(s_i) trước khi rút gọn chỉ số.

**Giải thích và hình thức hóa:** Quy ước s3 kết thúc với thưởng 0 sau đó. Việc biểu diễn tự lặp làm hàng cuối hợp lệ. Hàng 1 chứa v1 ở hai vế vì có cạnh tự lặp, không phải lỗi.

**Kết nối:** Gom hệ thành dạng ma trận rồi giải.

**Kiểm tra/ghi chú đáp án:** Thử để trống hệ số trước v3 ở hàng 2; đáp án 0,45.

**Nguồn:** hw02 bài3; PPTX47.

### L03-04-07 — Dạng ma trận và nghiệm

Thời lượng: 3 phút. Vai trò: hình thức hóa và giải hệ.

**Đầu vào:** Ba phương trình từ04-06; đại số ma trận và giải hệ tuyến tính.

**Nội dung trên slide:** Với $v,r\in\mathbb R^n$, $I$ là ma trận đơn vị:

$$v=r+\gamma Pv\quad\Longrightarrow\quad(I-\gamma P)v=r.$$

Ví dụ ba trạng thái rút còn:

$$0{,}55v_1-0{,}45v_2=1,\qquad -0{,}18v_1+0{,}73v_2=-1.$$

$$v_1=\frac{560}{641}\approx0{,}874,\quad v_2=-\frac{740}{641}\approx-1{,}154,\quad v_3=0.$$

**Cách thể hiện:** Nối từng dòng ma trận với phương trình ở trang trước; giữ kích thước chữ. Các bước khử ẩn chi tiết ở notes và buổi chữa bài, không đặt thêm ma trận 7×7.

**Giải thích và hình thức hóa:** Chuyển gamma Pv sang trái, đặt v làm nhân tử. Với gamma<1, có thể viết nghiệm lý thuyết (I-gamma P)^(-1)r; khi tính toán giải hệ, không cần tạo ma trận nghịch đảo. Trong ghi chú hoặc buổi chữa bài, kiểm nghiệm bằng thay lại cả hai phương trình. Chi phí giải hệ đặc O(n^3), nên dành mô hình lớn cho phương pháp lặp ở Bài 04.

**Kết nối:** Nghiệm hữu hạn phụ thuộc giả thiết, không chỉ thao tác biến đổi.

**Kiểm tra/ghi chú đáp án:** Notes: định thức hệ hai ẩn 0,3205; các tử số 0,28 và -0,37.

**Nguồn:** PPTX47–48; hw02 bài3, nghiệm tính lại.

### L03-04-08 — Điều kiện để giá trị hữu hạn

Thời lượng: 2 phút. Vai trò: giới hạn và kiểm tra giả thiết.

**Đầu vào:** Hệ Bellman và nghiệm ví dụ; tổng hình học.

**Nội dung trên slide:** Nếu $|R_{t+1}|\le M$ và $0\le\gamma<1$:

$$|G_t|\le\frac{M}{1-\gamma}.$$

Với $\gamma=1$: ví dụ kết thúc có kỳ vọng thời gian kết thúc hữu hạn và thưởng bị chặn vẫn cho giá trị hữu hạn.

**Cách thể hiện:** Hai khung riêng: gamma<1 có cận tổng hình học; gamma=1 cần điều kiện khác. Ví dụ vòng lặp nhận +1 cho thấy tổng không chiết khấu phân kỳ.

**Giải thích và hình thức hóa:** Với gamma<1, P chuẩn hóa theo hàng làm I-gamma P khả nghịch. Ghi chú chứng minh ngắn: nếu d=gamma Pd thì max|d|≤gamma max|d| nên d=0; ma trận vuông có hạt nhân chỉ gồm 0 thì khả nghịch. Với gamma=1, không nghịch đảo toàn bộ I-P của chuỗi có trạng thái hấp thụ; áp v(terminal)=0 và giải trên các trạng thái chưa kết thúc có tính quá độ. Điều kiện kết thúc hữu hạn kỳ vọng là điều kiện đủ, không phải điều kiện cần cho mọi hàm thưởng.

**Kết nối:** Phần 5 sẽ thêm hành động nhưng giữ cách đánh giá bằng Bellman.

**Kiểm tra/ghi chú đáp án:** Vòng lặp +1, gamma=1 phân kỳ; trạng thái hấp thụ không mặc nhiên là kết thúc nếu vẫn sinh thưởng.

**Nguồn:** PPTX36–38,48; bổ sung điều kiện giải hệ.

### L03-04-09 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra suy luận.

**Đầu vào:** Suy diễn Bellman, hệ ba trạng thái và điều kiện hữu hạn.

**Nội dung trên slide:** 1. Bước nào cần Markov trong suy diễn Bellman?
2. Viết phương trình cho s2 của bài ba trạng thái.
3. Vòng lặp thưởng +1, gamma=1 có giá trị hữu hạn không?

**Cách thể hiện:** Ba câu đánh số; câu 2 kèm hàng P và r(s2) để không cần quay slide.

**Giải thích và hình thức hóa:** Kiểm tra lý do của công thức và điều kiện áp dụng, không chỉ chép lại định nghĩa.

**Kết nối:** Từ đánh giá một quá trình sang tác động của việc chọn hành động.

**Kiểm tra/ghi chú đáp án:** 1. Thay kỳ vọng tương lai có điều kiện bằng v(s′). 2. Như 04-06. 3. Không.

**Nguồn:** PPTX44–48; hw02 bài3.

## Phần 5. MDP và chính sách cố định — 20 phút

Đầu vào: MRP và Bellman. Đầu ra: hiểu MDP có lựa chọn hành động; cố định một chính sách Markov dừng tạo mô hình P^pi,r^pi để đánh giá như MRP. Không mặc định MRP cảm sinh bằng đúng MRP sinh viên đầu bài: phải tính theo chính sách cụ thể.

### L03-05-01 — MDP và chính sách cố định

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** MRP có quy luật chuyển đã cố định và phương trình đánh giá.

**Nội dung trên slide:** Tiêu đề phần và hai lựa chọn học/nghỉ từ cùng một trạng thái.

**Cách thể hiện:** Dùng cùng bối cảnh sinh viên, chuyển sang đồ thị MDP của nguồn trang 50; làm nổi lựa chọn tại C2.

**Giải thích và hình thức hóa:** Ở phần trước quá trình chuyển đã cho sẵn; giờ hành động ảnh hưởng phản hồi.

**Kết nối:** Nhìn hai hành động cụ thể trước định nghĩa MDP.

**Kiểm tra/ghi chú đáp án:** Chưa hiện bộ thành phần ở trang mở.

**Nguồn:** PPTX49–50.

### L03-05-02 — Lựa chọn làm thay đổi phản hồi

Thời lượng: 3 phút. Vai trò: ví dụ trực quan.

**Đầu vào:** Bối cảnh sinh viên; tác tử có thể chọn học hoặc ngủ.

**Nội dung trên slide:** Tại C2, chọn Study chuyển tới C3 và nhận -2; chọn Sleep chuyển tới Sleep và nhận 0.

**Cách thể hiện:** Một nút C2 nối hai nút hành động có hình dạng riêng, rồi tới trạng thái kế tiếp.

**Giải thích và hình thức hóa:** Phân biệt lựa chọn hành động với kết quả môi trường. Bản MDP nguồn có năm trạng thái: C1, C2, C3, Facebook, Sleep. So với MRP trước, thưởng thi đạt được gộp vào hành động Study từ C3 tới Sleep; Pub trở thành hành động dẫn qua một nút ngẫu nhiên. Nút này không phải trạng thái mới. Giải thích thay đổi biểu diễn trước khi hiện toàn hình, không nói đây chỉ là cùng ma trận P thêm nhãn hành động.

**Kết nối:** Cần một mô hình có điều kiện theo cả s và a.

**Kiểm tra/ghi chú đáp án:** Hai cạnh hành động không phải hai xác suất chuyển chưa điều kiện hóa.

**Nguồn:** PPTX50; đồ thị Student MDP.

### L03-05-03 — Quá trình quyết định Markov

Thời lượng: 3 phút. Vai trò: hình thức hóa.

**Đầu vào:** Hai lựa chọn có phản hồi khác nhau; xác suất chung từ Bài02.

**Nội dung trên slide:** Quá trình quyết định Markov (MDP), với trạng thái và hành động hữu hạn:

$$\big(\mathcal S,\mathcal A,P,\gamma\big),\qquad
P(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a).
$$

$P(s',r\mid s,a)\ge0$, $\sum_{s',r}P(s',r\mid s,a)=1$.

**Cách thể hiện:** Đặt (s,a) ở đầu một nhánh, cặp (s′,r) ở cuối; cùng ký hiệu xác suất chung của Bài 02.

**Giải thích và hình thức hóa:** Ở đây P đã chứa cả quy luật thưởng nên không thêm một hàm thưởng độc lập vào bộ. Tập hành động hợp lệ A(s), miền thưởng rời rạc trong các công thức tổng; quy luật Markov và không đổi theo thời gian. Quan sát đầy đủ và biết mô hình là hai khái niệm khác nhau.

**Kết nối:** Mô hình chưa quy định tác tử chọn hành động nào: cần chính sách.

**Kiểm tra/ghi chú đáp án:** Nêu vai trò của từng thành phần trên chính ví dụ học/nghỉ.

**Nguồn:** PPTX49; tiếp nối Bài02.

### L03-05-04 — Cố định một chính sách

Thời lượng: 4 phút. Vai trò: ví dụ → định nghĩa.

**Đầu vào:** MDP chưa quy định tần suất tác tử chọn các hành động.

**Nội dung trên slide:** Tại C2, chọn Study với 0,75 và Sleep với 0,25; sau đó nhắc $\pi(a\mid s)$ và $\sum_a\pi(a\mid s)=1$.

**Cách thể hiện:** Tô nhãn xác suất tại tầng hành động, khác nhãn ở tầng môi trường bằng vị trí và hình dạng, không chỉ màu.

**Giải thích và hình thức hóa:** Đây là chính sách minh họa được chọn để tính, không gán là chính sách gốc hoặc tối ưu. Chốt chính sách đầy đủ: tại C1 chọn Study/Facebook mỗi hành động 0,5; tại Facebook chọn Facebook/Quit mỗi hành động 0,5; tại C3 chọn Study/Pub mỗi hành động 0,5; Sleep kết thúc, không chọn hành động. Xét chính sách Markov dừng; không khẳng định mọi chính sách đều dừng.

**Kết nối:** Gộp hai tầng ngẫu nhiên thành phản hồi theo trạng thái.

**Kiểm tra/ghi chú đáp án:** Từ C2 theo chính sách này, xác suất đến C3 là 0,75; đến Sleep là 0,25.

**Nguồn:** PPTX52; xác suất 0,75/0,25 là bài luyện bổ sung.

### L03-05-05 — Từ MDP đến quá trình phần thưởng Markov

Thời lượng: 3 phút. Vai trò: trực giác và phép tính trước công thức.

**Đầu vào:** Chính sách đầy đủ đã chốt ở05-04; mô hình C2 theo từng hành động.

**Nội dung trên slide:** Tại C2: $P^\pi(C2,C3)=0{,}75$, $P^\pi(C2,Sleep)=0{,}25$; $r^\pi(C2)=0{,}75(-2)+0{,}25(0)=-1{,}5$.

**Cách thể hiện:** Bên trái hai tầng (chính sách/môi trường); bên phải nút C2 với các cạnh đã gộp.

**Giải thích và hình thức hóa:** Giới thiệu ký hiệu mũ pi bằng lời “quy luật khi tác tử theo chính sách này”. Tính từng xác suất và thưởng bằng số trước, không đưa hai dấu tổng ngay từ đầu.

**Kết nối:** Khái quát phép gộp ở tất cả trạng thái.

**Kiểm tra/ghi chú đáp án:** Đổi pi làm P^pi hoặc r^pi thay đổi, dù mô hình môi trường giữ nguyên.

**Nguồn:** PPTX52–55; hw02 bài4.

### L03-05-06 — Mô hình dưới chính sách

Thời lượng: 3 phút. Vai trò: suy diễn ngắn.

**Đầu vào:** Phép tính P^pi và r^pi tại C2 ở05-05.

**Nội dung trên slide:** Từ xác suất chung theo chính sách:

$$P^\pi(s',r\mid s)=\sum_a\pi(a\mid s)P(s',r\mid s,a).$$

Lấy biên và kỳ vọng:

$$P^\pi_{ss'}=\sum_a\pi(a\mid s)\sum_rP(s',r\mid s,a),$$
$$r^\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}rP(s',r\mid s,a).$$

**Cách thể hiện:** Ba dòng xuất hiện theo thứ tự: trộn theo hành động → cộng bỏ thưởng → lấy trung bình thưởng. Công thức cuối có thể hiện thay thế dòng đầu để không quá tải.

**Giải thích và hình thức hóa:** Dùng xác suất toàn phần và định nghĩa kỳ vọng rời rạc. Cố định pi thì v_pi là giá trị MRP cảm sinh và thỏa v_pi=r^pi+gamma P^pi v_pi. Không giả định thưởng độc lập với trạng thái kế tiếp.

**Kết nối:** Phần 6 mở lại tầng hành động để so sánh giá trị của từng lựa chọn.

**Kiểm tra/ghi chú đáp án:** Tổng mỗi hàng P^pi bằng 1; chính sách thay đổi theo thời gian thì không có một ma trận P^pi cố định như trên.

**Nguồn:** PPTX52–57; hw02 bài4.

### L03-05-07 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra.

**Đầu vào:** Cách lấy trung bình theo chính sách và giới hạn bài toán đánh giá.

**Nội dung trên slide:** 1. Cố định pi, ngẫu nhiên nào còn trong quá trình?
2. Nếu tại C2 luôn chọn Study, hàng chuyển và thưởng trung bình là gì?
3. Biết mô hình có đồng nghĩa đã biết chính sách tốt nhất không?

**Cách thể hiện:** Ba câu đánh số, giữ hình C2 nhỏ nếu cần.

**Giải thích và hình thức hóa:** Không yêu cầu tối ưu chính sách ở bài này.

**Kết nối:** Từ giá trị khi theo pi đến giá trị của một hành động đầu tiên.

**Kiểm tra/ghi chú đáp án:** 1. Hành động nếu pi ngẫu nhiên và phản hồi môi trường. 2. Đến C3 xác suất 1, thưởng -2. 3. Không.

**Nguồn:** PPTX50–52; hw02 bài4.

## Phần 6. Giá trị trạng thái và giá trị hành động — 24 phút

Đầu vào: mô hình chung P, chính sách cố định, MRP cảm sinh và Bellman cho v. Đầu ra: giải thích và suy ra ba quan hệ v theo q, q theo v, q theo q; dùng một MDP khác để kiểm tra. Duy trì cùng cây một bước qua các trang, chỉ mở thêm tầng cần thiết.

### L03-06-01 — Giá trị trạng thái và giá trị hành động

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** v_pi của MRP cảm sinh và mô hình có điều kiện theo hành động.

**Nội dung trên slide:** Tiêu đề phần và hai nhánh Study/Sleep xuất phát từ cùng C2.

**Cách thể hiện:** Hai hình: chưa chọn hành động và đã chọn Study.

**Giải thích và hình thức hóa:** Cùng chính sách tiếp tục, khác việc có ấn định hành động đầu tiên hay không.

**Kết nối:** Từ v_pi của cả trạng thái sang giá trị từng lựa chọn.

**Kiểm tra/ghi chú đáp án:** Không đưa bốn công thức Bellman trên trang mở.

**Nguồn:** PPTX53.

### L03-06-02 — Ấn định hành động đầu tiên

Thời lượng: 3 phút. Vai trò: ví dụ trực quan.

**Đầu vào:** C2 có Study/Sleep và một chính sách tiếp tục cố định.

**Nội dung trên slide:** Từ C2: một lượt chọn Study trước, lượt khác chọn Sleep trước; sau đó đều theo cùng pi.

**Cách thể hiện:** Khoanh hành động đầu tiên; các bước sau ghi “theo pi”.

**Giải thích và hình thức hóa:** Giá trị hành động không phải phần thưởng tức thời và không phải giá trị của một chính sách mới dùng hành động đó mãi. Tác tử chỉ ấn định bước đầu.

**Kết nối:** Đặt tên q cho kỳ vọng của thí nghiệm vừa mô tả.

**Kiểm tra/ghi chú đáp án:** Ở nhánh Sleep, không còn hành động nào sau khi kết thúc.

**Nguồn:** PPTX50,53–54.

### L03-06-03 — Định nghĩa giá trị hành động

Thời lượng: 2 phút. Vai trò: hình thức hóa.

**Đầu vào:** Thí nghiệm ấn định hành động đầu rồi theo pi ở06-02.

**Nội dung trên slide:** Với các kỳ vọng hữu hạn:

$$v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],$$
$$q_\pi(s,a)=\mathbb E[G_t\mid S_t=s,\ A_t\text{ được ấn định là }a;\ \pi\text{ từ }t+1].$$

Ký hiệu thông dụng: $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$.

**Cách thể hiện:** Hai cột chung phần “từ bước sau theo pi”; chỉ khác điều kiện về hành động đầu. Ký hiệu thông dụng trên mặt slide; cách định nghĩa đầy đủ ở ghi chú nếu dòng quá dài.

**Giải thích và hình thức hóa:** q được định nghĩa cho mọi hành động hợp lệ, kể cả pi(a|s)=0: thực hiện a một lần rồi theo pi. Công thức điều kiện thông dụng được hiểu theo quy ước này, không coi điều kiện trên biến cố xác suất 0 là phép chia xác suất hợp lệ. Cũng hiểu giá trị từ trạng thái s bằng khởi tạo tại s.

**Kết nối:** Từ q của từng hành động sang trung bình khi để pi chọn.

**Kiểm tra/ghi chú đáp án:** Phân biệt hai chỉ số s,a với chỉ số pi: pi quy định hành vi tiếp tục.

**Nguồn:** PPTX53; làm rõ quy ước hành động có xác suất 0.

### L03-06-04 — Từ giá trị hành động đến giá trị trạng thái

Thời lượng: 3 phút. Vai trò: suy diễn bằng xác suất toàn phần.

**Đầu vào:** Định nghĩa v_pi,q_pi; chính sách chọn hành động với xác suất pi.

**Nội dung trên slide:** Trước tiên minh họa C2 chọn Study/Sleep với trọng số 0,75/0,25. Sau đó:

$$
\begin{aligned}
v_\pi(s)&=\mathbb E_\pi[G_t\mid S_t=s]\\
&=\sum_a\Pr_\pi(A_t=a\mid S_t=s)\,
\mathbb E_\pi[G_t\mid S_t=s,A_t=a]\\
&=\sum_a\pi(a\mid s)q_\pi(s,a).
\end{aligned}
$$

**Cách thể hiện:** Cây s→a; mỗi nhánh mang một giá trị q và trọng số pi. Hai mức hiện: phép tính hai nhánh trước, dấu tổng sau.

**Giải thích và hình thức hóa:** Dòng giữa là kỳ vọng toàn phần theo A_t. Các hành động có pi=0 đóng góp 0; không cần đánh giá một kỳ vọng điều kiện xác suất 0 trong phép chứng minh.

**Kết nối:** Đã biết cách gộp q thành v; tiếp theo tính q từ phản hồi một bước.

**Kiểm tra/ghi chú đáp án:** Không dùng max: chính sách đã cố định.

**Nguồn:** PPTX53,56–57; hw02 bài7.

### L03-06-05 — Giá trị hành động từ phản hồi một bước

Thời lượng: 3 phút. Vai trò: suy diễn Bellman: q theo v.

**Đầu vào:** Đẳng thức tách G; mô hình phản hồi chung; định nghĩa q_pi.

**Nội dung trên slide:** Ấn định (s,a), dùng đồng nhất thức đã có:

$$
q_\pi(s,a)=\mathbb E[R_{t+1}+\gamma G_{t+1}\mid s,a;\pi\text{ sau đó}].
$$

Chia theo cặp phản hồi $(s',r)$:

$$
q_\pi(s,a)=\sum_{s',r}P(s',r\mid s,a)
\left[r+\gamma\mathbb E[G_{t+1}\mid s,a,s',r;\pi\text{ sau đó}]\right].
$$

Nhận diện kỳ vọng tương lai:

$$q_\pi(s,a)=\sum_{s',r}P(s',r\mid s,a)\big[r+\gamma v_\pi(s')\big].$$

**Cách thể hiện:** Một cây từ cặp (s,a) tới các cặp (s′,r); phần tương lai tại mỗi s′ là hộp v_pi(s′). Hai dòng dài là các bước xuất hiện nối tiếp, không ép lên cùng mặt một lúc.

**Giải thích và hình thức hóa:** Bước 1 dùng tách G; bước 2 dùng kỳ vọng toàn phần theo phản hồi chung; bước 3 dùng Markov của môi trường, chính sách Markov dừng và quy luật không đổi theo thời gian. Chỉ các cặp có xác suất dương cần kỳ vọng điều kiện trung gian. Không tách P(s′,r|s,a) thành tích hai phân phối độc lập.

**Kết nối:** Thay v ở vế phải bằng trung bình các q ở thời điểm kế tiếp.

**Kiểm tra/ghi chú đáp án:** Nếu s′ kết thúc thì v_pi(s′)=0, nhưng r ở bước vào đó vẫn được cộng.

**Nguồn:** PPTX56–57; nối mô hình chung Bài02.

### L03-06-06 — Bellman kỳ vọng cho giá trị hành động

Thời lượng: 2 phút. Vai trò: suy diễn: q theo q.

**Đầu vào:** q theo v ở06-05 và v theo q ở06-04.

**Nội dung trên slide:** Tại trạng thái kế tiếp:

$$v_\pi(s')=\sum_{a'}\pi(a'\mid s')q_\pi(s',a').$$

Thế vào kết quả trước:

$$
q_\pi(s,a)=\sum_{s',r}P(s',r\mid s,a)
\left[r+\gamma\sum_{a'}\pi(a'\mid s')q_\pi(s',a')\right].
$$

**Cách thể hiện:** Mở hộp v_pi(s′) thành tầng hành động a′. Dùng nhãn t và t+1 để phân biệt a và a′.

**Giải thích và hình thức hóa:** Không có suy luận mới ngoài phép thế; tránh trình bày như một công thức độc lập phải học thuộc. Tổng trong là trung bình theo hành động tiếp theo, tổng ngoài là trung bình phản hồi của hành động hiện tại. Với s′ kết thúc, quy ước tổng tiếp tục bằng 0.

**Kết nối:** Quay lại giá trị trạng thái bằng cách lấy trung bình hành động đầu tiên.

**Kiểm tra/ghi chú đáp án:** Câu kiểm tra miệng: pi bên trong được điều kiện theo s hay s′? Đáp án s′.

**Nguồn:** PPTX56–57.

### L03-06-07 — Bellman kỳ vọng cho giá trị trạng thái

Thời lượng: 2 phút. Vai trò: suy diễn: thế và đối chiếu MRP.

**Đầu vào:** Hai quan hệ v theo q và q theo v; P^pi,r^pi từ05-06.

**Nội dung trên slide:** Bắt đầu từ kết quả 06-04, thế công thức 06-05:

$$
\begin{aligned}
v_\pi(s)&=\sum_a\pi(a\mid s)q_\pi(s,a)\\
&=\sum_a\pi(a\mid s)\sum_{s',r}P(s',r\mid s,a)
\big[r+\gamma v_\pi(s')\big]\\
&=r^\pi(s)+\gamma\sum_{s'}P^\pi_{ss'}v_\pi(s').
\end{aligned}
$$

**Cách thể hiện:** Cây s→a→(s′,r) rồi gộp lại như phần 5; đánh dấu bằng nhãn hai nhóm số hạng tạo r^pi và P^pi.

**Giải thích và hình thức hóa:** Dòng cuối phân phối phép cộng và dùng đúng định nghĩa P^pi,r^pi. Không lấy trung bình thêm lần nữa theo pi sau khi đã tạo P^pi. Hai cách viết là cùng Bellman kỳ vọng, không phải hai giả thuyết.

**Kết nối:** Áp dụng ba quan hệ vừa suy ra vào xe đua.

**Kiểm tra/ghi chú đáp án:** Đối chiếu với 05-06 để khép mạch MDP→MRP.

**Nguồn:** PPTX56–57; hw02 bài4,8.

### L03-06-08 — Vận dụng với xe đua

Thời lượng: 5 phút. Vai trò: chuyển sang tình huống mới.

**Đầu vào:** Ba quan hệ Bellman đã suy ra và điều kiện gamma=1 ở04-08.

**Nội dung trên slide:** Ba trạng thái Cool, Warm, Overheated; hai hành động Slow/Fast. Chính sách chọn mỗi hành động với 0,5 ở hai trạng thái chưa kết thúc; $\gamma=1$.

Cho $v_\pi(Cool)=0$, $v_\pi(Warm)=-6$, $v_\pi(Overheated)=0$:

$$q_\pi(Cool,Slow)=1+v_\pi(Cool)=1,\quad q_\pi(Cool,Fast)=2+0{,}5(0)+0{,}5(-6)=-1.$$

$$v_\pi(Cool)=0{,}5(1)+0{,}5(-1)=0.$$

**Cách thể hiện:** Đồ thị xe đua; trước phép tính chỉ làm nổi hai hành động từ Cool. Các kết quả còn lại giải thích trong notes và phần chữa bài, tránh sáu nhánh cộng bốn công thức trên một trang.

**Giải thích và hình thức hóa:** Các giá trị là dữ kiện đã giải dưới chính sách trên, không yêu cầu sinh viên tự tìm cả hệ trong 5 phút. Notes: Cool–Slow tới Cool thưởng1; Cool–Fast tới Cool/Warm mỗi xác suất0,5 thưởng2; Warm–Slow tới Cool/Warm mỗi0,5 thưởng1; Warm–Fast tới Overheated thưởng-10, không thêm2. Kiểm các giá trị đã cho bằng cách thay ngược vào hệ: vC=1,5+0,75vC+0,25vW; vW=-4,5+0,25vC+0,25vW. Từ Cool, đường Fast→Warm→Fast→Overheated có xác suất (1/2)(1/2)(1/2)=1/8. Từ Warm, xác suất kết thúc ngay là 1/2. Vì thế chính sách này có xác suất kết thúc ít nhất 1/8 trong mỗi hai bước từ mọi trạng thái chưa kết thúc, nên kỳ vọng thời gian hữu hạn; gamma=1 hợp lệ.

**Kết nối:** Từ phép tính Cool sang câu hỏi tự làm tại Warm.

**Kiểm tra/ghi chú đáp án:** Đọc mô hình trước khi tính; lựa chọn đầu tiên Fast có thể có q thấp dù thưởng tức thời cao hơn.

**Nguồn:** PPTX51,55; Berkeley CS188; quy ước thưởng quá nhiệt đã nêu.

### L03-06-09 — Câu hỏi kiểm tra

Thời lượng: 3 phút. Vai trò: kiểm tra.

**Đầu vào:** Mô hình xe đua, chính sách đều và các giá trị ở06-08.

**Nội dung trên slide:** 1. Với xe đua và các giá trị đã cho, tính q_pi(Warm,Slow), q_pi(Warm,Fast).
2. Từ hai q đó, tính v_pi(Warm).
3. Trong Bellman kỳ vọng, vì sao lấy trung bình theo pi thay vì chọn giá trị lớn nhất?

**Cách thể hiện:** Giữ mô hình Warm và ba giá trị cần thiết trên mặt slide, không buộc nhớ số từ trang trước.

**Giải thích và hình thức hóa:** Câu 1 vận dụng mô hình, câu 2 vận dụng xác suất toàn phần, câu 3 phân biệt đánh giá và tối ưu.

**Kết nối:** Khép phần giá trị, sang tổng hợp quy trình đọc và giải một mô hình.

**Kiểm tra/ghi chú đáp án:** 1. -2 và -10. 2. -6. 3. Đang đánh giá chính sách cố định.

**Nguồn:** PPTX51,55–57; hw02 bài7,8.

## Phần 7. Tổng hợp và vận dụng — 8 phút

Đầu vào: toàn tuyến lập luận. Đầu ra: sinh viên tự nối mô tả môi trường với một phương trình giá trị, biết nội dung chữa bài và đích đến của Bài 04. Phần kết dùng chu trình rút gọn, không giới thiệu khái niệm mới.

### L03-07-01 — Tổng hợp và vận dụng

Thời lượng: 1 phút. Vai trò: mở phần.

**Đầu vào:** Toàn bộ tuyến chuỗi Markov, MRP, MDP, chính sách và Bellman.

**Nội dung trên slide:** Tiêu đề phần và sơ đồ nhỏ từ mô hình tới giá trị.

**Cách thể hiện:** Tái dùng các biểu tượng trạng thái, thưởng, hành động và giá trị đã có.

**Giải thích và hình thức hóa:** Không thêm thuật ngữ hoặc công thức tối ưu.

**Kết nối:** Thu hồi câu hỏi mở bài về tính giá trị khi biết mô hình.

**Kiểm tra/ghi chú đáp án:** Không có phép tính mới ở trang mở.

**Nguồn:** Tổng hợp PPTX30–57.

### L03-07-02 — Từ mô hình đến phương trình giá trị

Thời lượng: 2 phút. Vai trò: tổng hợp trực quan.

**Đầu vào:** Các khái niệm đã học và sơ đồ mở phần.

**Nội dung trên slide:** Chuỗi Markov → thêm thưởng thành MRP; thêm lựa chọn thành MDP; cố định pi thu được MRP để đánh giá.

**Cách thể hiện:** Sơ đồ hai chiều ở bước MRP/MDP, gắn P,r và P^pi,r^pi đúng chỗ.

**Giải thích và hình thức hóa:** Tại một nút, nối hai đường giải thích: gộp theo pi trước rồi viết Bellman; hoặc mở cây s→a→s′ rồi lấy kỳ vọng. Hai đường cho cùng v_pi.

**Kết nối:** Từ khái niệm sang nhiệm vụ tự viết phương trình.

**Kiểm tra/ghi chú đáp án:** Bài 04 sẽ thay câu hỏi “chính sách này có giá trị bao nhiêu” bằng “chọn chính sách nào”.

**Nguồn:** PPTX30,34,49,56–58.

### L03-07-03 — Bài tập và bước tiếp theo

Thời lượng: 3 phút. Vai trò: ứng dụng và chuẩn bị chữa bài.

**Đầu vào:** Quy trình từ mô hình đến phương trình giá trị.

**Nội dung trên slide:** Bài 3: kiểm ma trận, lập hệ. Bài 4: MDP dưới pi. Bài 7: v từ q. Bài 8: Bellman kỳ vọng. Bài 04: Bellman tối ưu và quy hoạch động.

**Cách thể hiện:** Bảng bốn nhiệm vụ với sản phẩm cần nộp; không đưa toàn bộ đề dài vào một trang.

**Giải thích và hình thức hóa:** 30 phút chữa bài nguồn: 10 phút bài3, 8 phút bài4, 5 phút bài7, 7 phút bài8. Bài9 về tối ưu để Bài04. Không thêm chương trình minh họa ngoài nguồn.

**Kết nối:** Câu hỏi cuối xác nhận sinh viên đã phân biệt đánh giá với tối ưu.

**Kiểm tra/ghi chú đáp án:** Các bài tập dùng đúng ký hiệu đã xây dựng; bản HTML không hiển thị phân bổ phút hoặc chỉ dẫn soạn.

**Nguồn:** PPTX58; hw02 bài3,4,7,8.

### L03-07-04 — Câu hỏi kiểm tra

Thời lượng: 2 phút. Vai trò: kiểm tra cuối bài.

**Đầu vào:** Phân biệt mô hình, phần thưởng, chính sách, giá trị và tối ưu.

**Nội dung trên slide:** 1. Biết P và pi, cần thêm gì để tính v_pi?
2. G, v và q khác nhau thế nào?
3. Tăng xác suất chọn một hành động có chắc làm giá trị tăng không?

**Cách thể hiện:** Ba câu ngắn; kết thúc bằng câu trả lời cụ thể, không khẩu hiệu.

**Giải thích và hình thức hóa:** Câu 1 chỉ rõ P trong câu hỏi là xác suất chuyển trạng thái, chưa bao gồm thưởng; tránh đánh đố do P chung.

**Kết nối:** Kết thúc Bài03; Bài04 giải bài toán lựa chọn chính sách.

**Kiểm tra/ghi chú đáp án:** 1. Quy luật/kỳ vọng thưởng, gamma, quy ước kết thúc và điều kiện giá trị hữu hạn. 2. Tổng một lượt/kỳ vọng theo trạng thái/kỳ vọng khi ấn định hành động đầu. 3. Không, phụ thuộc giá trị và hậu quả của hành động.

**Nguồn:** Tổng hợp bài học.

## Các phép kiểm bắt buộc trước khi triển khai

- **Nối ví dụ với công thức:** giữ đúng thứ tự trạng thái, nhãn thưởng và chỉ số thời gian từ hình sang công thức. Student MRP nhận thưởng theo trạng thái rời đi; không chuyển ngầm sang thưởng vào trạng thái.
- **Mỗi dấu bằng trong Bellman:** 04-03 là tách tổng; 04-04 là tuyến tính và kỳ vọng lặp; 04-05 là Markov, không đổi theo thời gian và kỳ vọng rời rạc. 06-04 lấy trung bình hành động đầu; 06-05 lấy trung bình phản hồi chung; 06-06/07 là phép thế và gom nhóm.
- **Không trình bày nghiệm sai:** bài ba trạng thái có nghiệm $(560/641,-740/641,0)^{\mathsf T}$ khi gamma=0,9. Giá trị xe đua (0,-6,0) dùng gamma=1 và chính sách đều; không tái sử dụng cho gamma=0,9.
- **Trạng thái kết thúc:** đặt giá trị tiếp tục bằng 0, vẫn tính thưởng ở bước vào trạng thái. Nếu thêm tự lặp để chuẩn hóa ma trận, thưởng sau khi kết thúc phải bằng 0.
- **Không lẫn ba phép tính:** kỳ vọng theo hành động pi, kỳ vọng theo môi trường P, và phép tối ưu. Bài này chưa dùng phép max của Bellman tối ưu.
- **Khả năng đọc:** mỗi trang suy diễn hiện tối đa khoảng ba dòng trọng tâm cùng lúc; công thức dài mở dần. Chú thích lý do đặt sát bước biến đổi; phần chứng minh điều kiện phụ nằm trong notes. Không thu nhỏ chữ để giữ cả chứng minh trên một mặt.
- **Kiểm tra cuối mỗi phần:** bảy trang 01-06, 02-06, 03-06, 04-09, 05-07, 06-09, 07-04, mỗi trang 2–3 câu đánh số. Chỉ có đáp án trong ghi chú, không tự lộ trước khi sinh viên làm.
- **Không đưa chỉ dẫn tác giả lên slide:** nhãn vai trò, thời lượng, nguồn quyết định biên tập, mã ID và các câu “vẽ/nhấn mạnh/đặt…” trong bản kế hoạch chỉ dùng để triển khai. Ghi chú diễn giả là lời giải thích toán học, giả thiết và đáp án.

## Tài sản dự kiến

| Tài sản | Sử dụng | Cách xử lý |
|---|---|---|
| Đồ thị Student không thưởng | Phần 1–2 | Từ `student-mrp.svg`, tách nhãn thưởng; không đổi xác suất |
| Đồ thị Student có thưởng và dải quỹ đạo | Phần 3–4 | Giữ dữ kiện nguồn; dựng dải bước đi riêng để không lẫn thời điểm thưởng |
| Sơ đồ Bellman một bước | Phần 4 | Tái cấu trúc `bellman-backup.svg`, thêm phiên bản khoanh phần đuôi |
| Student MDP và MRP cảm sinh | Phần 5–6 | Từ `student-mdp.svg`; làm nổi xác suất chính sách khác xác suất môi trường |
| Xe đua | 06-08/09 | Tái dùng `racing-car.svg`, giữ sáu kết quả và quy ước -10 khi quá nhiệt |
| Ma trận, phương trình, bảng số | Các phần | HTML/KaTeX, không biến công thức thành SVG |

## Ánh xạ và sai khác so với bản hiện hành

| Nguồn chính | Phần kế hoạch mới | Quyết định |
|---|---|---|
| PPTX28–30 | 1–2 | Rút phần ôn Markov đã học ở Bài02; thêm slide mở phần |
| PPTX31–33 | 2 | Giữ đồ thị, quỹ đạo và ma trận; giới thiệu một hàng trước toàn ma trận |
| PPTX34–43 | 3 | Ví dụ thưởng và tổng đi trước định nghĩa giá trị; không đưa bảng nghiệm trước cách tính |
| PPTX44–48 | 4 | Tách suy diễn thành ba trang và áp dụng hệ nhỏ từ bài tập; nêu rõ điều kiện gamma |
| PPTX49–52 | 5 | Dùng xác suất chung của Bài02; thêm phép gộp MDP dưới pi bằng số trước công thức |
| PPTX53–57 | 6 | Giới thiệu q qua hành động đầu tiên; suy ra từng Bellman; xe đua dùng để kiểm chứng |
| PPTX58 và hw02 | 7 | Giao bài3,4,7,8; tối ưu chuyển Bài04 |

Không sửa bản HTML đang dùng trong lượt lập kế hoạch này. Khi triển khai sẽ chuyển nội dung đã duyệt sang storyboard chính, cập nhật outline, ID, hình và ánh xạ lecture-note liên quan; không coi bản kế hoạch là bằng chứng deck đã thay đổi.
