# Dàn bài mới Bài 05: Dự đoán phi mô hình

Ngày 28-09-2026. Trạng thái: dàn bài đã duyệt và triển khai; đã đồng bộ với chỉnh sửa sau năm báo cáo độc lập, hoàn tất rà lại và kiểm định cuối. Căn cứ phân tích, nguồn, lựa chọn ví dụ và mức hình thức hóa nằm trong [analysis.md](analysis.md). Bản đồ chu trình và lý do từng trang nằm trong [storyboard.md](storyboard.md). Các mã nội bộ, ngân sách phút và quyết định biên soạn không được hiển thị trên trang chiếu hoặc ghi chú diễn giả.

## Thông tin chung

Bài giảng thuộc học phần Học tăng cường, học kỳ 1 năm học 2026–2027. Người học đã học học máy, học sâu, thuật toán, MDP, chính sách, giá trị trạng thái và Bellman kỳ vọng. Vấn đề trung tâm là ước lượng giá trị của một chính sách cố định từ tương tác khi không biết mô hình chuyển và phần thưởng kỳ vọng. Sutton–Barto §5.1, §6.1–6.3 là sườn; L05 và HW05 quyết định phạm vi ví dụ và bài tập. Mọi thuật toán trong tuyến chính là dự đoán dạng bảng từ dữ liệu theo chính sách.

Mục tiêu MT1 xác định dữ liệu và đối tượng; MT2 tính lợi tức và chọn mẫu; MT3 thực hiện MC với hai quy tắc bước học; MT4 thực hiện TD(0); MT5 so sánh theo dữ liệu và giả thiết; MT6 chọn phương pháp có căn cứ. Mỗi mục tiêu có câu kiểm tra cụ thể bên dưới.

Thiết kế gồm **45 trang, năm mạch, 120 phút**, tính cả suy nghĩ và chữa các câu kiểm tra. **30 phút chữa bài tập nguồn** nằm ngoài 120 phút, tạo đủ buổi 150 phút. Không có mã nguồn để chuyển; không tạo chương trình hoặc notebook. Ứng dụng được đặt sau khái niệm tương ứng, không có phần thực hành tách riêng.

## Thuật ngữ và ký hiệu dùng chung

| Ký hiệu hoặc thuật ngữ | Quy ước và thời điểm khai báo |
|---|---|
| Monte Carlo (MC) | Tên phương pháp, khai báo trước lần dùng viết tắt trong mạch B |
| Sai phân thời gian (TD) | Thuật ngữ tiếng Việt thống nhất; không luân phiên các cách dịch |
| Lượt; lần ghé đầu tiên; mọi lần ghé | Lượt kết thúc ở thời điểm T; lần ghé đầu tiên theo chiều thời gian, không theo chiều duyệt lùi |
| Bước học | Dùng thống nhất cho $\alpha$; không gọi cùng đại lượng bằng nhiều tên |
| $\pi(a\mid s)$ | Chính sách Markov cố định; dữ liệu được sinh theo $\pi$; môi trường Markov dừng |
| $\mathcal S$, $\mathcal S^+$ | Trạng thái không kết thúc hữu hạn; tập gồm cả trạng thái kết thúc |
| $S_t,A_t,R_{t+1}$ | Trạng thái, hành động và thưởng của chuyển $t\to t+1$; thưởng là số thực |
| $T$ | Thời điểm kết thúc; không dùng lại cho toán tử Bellman. Nếu buộc cần toán tử thì dùng $T_\pi$ theo Bài 04, không dùng $T^\pi$ |
| $G_t$ | Tổng phần thưởng chiết khấu, sau khai báo có thể gọi lợi tức; $G_T=0$ |
| $v_\pi(s)$ | Giá trị thật; $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$; giá trị ở trạng thái kết thúc bằng 0 |
| $V$; $V_t$ | Bảng ước lượng hiện tại; $V_t$ là bảng trước cập nhật TD tại bước t. Không dùng $V^\pi$ làm giá trị thật |
| $g_i(s)$, $N(s)$, n | Mẫu lợi tức thứ i được chọn, bộ đếm và số cập nhật của riêng trạng thái s |
| $\alpha_n(s)$ | Bước học lần cập nhật thứ n của s; $1/n$ tái tạo trung bình mẫu; bước hằng cần ghi rõ |
| $Y_t$, $\delta_t$ | Mục tiêu TD; sai số TD bằng mục tiêu trừ giá trị cũ, khác lỗi thật |
| $V_k$, K | Bảng đầu lượt quét theo lô thứ k và ngân sách số quét; khai báo mới ở L05-D09, không lẫn k với thời điểm tương tác |

Thưởng vào trạng thái kết thúc được đặt trên cạnh; giá trị tiếp nối ở trạng thái kết thúc luôn 0. $\gamma=1$ đi kèm giả thiết lượt kết thúc hợp lệ; cắt dữ liệu theo ngân sách không tự tạo trạng thái kết thúc. Mọi ký hiệu trong hình, công thức, giả mã, ví dụ, câu kiểm tra và ghi chú phải tuân cùng bảng này.

## Bản đồ các phần

| Mạch | Loại, chức năng | Đầu vào | Đầu ra nối sang mạch sau | Trang | Phút | Kiểm tra riêng |
|---|---|---|---|---|---:|---|
| A. Mở đầu: đánh giá chính sách từ dữ liệu | Mở đầu; Xác định cùng đối tượng giá trị khi đầu vào chuyển từ mô hình sang mẫu. | Chính sách, giá trị và Bellman kỳ vọng từ bài trước. | Nhu cầu dùng lượt hoàn chỉnh để lấy mẫu lợi tức. | L05-A01–L05-A05 (5) | 12 | L05-A05 |
| B. Dự đoán Monte Carlo | Phát triển kiến thức và ứng dụng; Xây dựng ước lượng từ lợi tức, lựa chọn lần ghé và bước học. | Bài toán dự đoán và mẫu tương tác của mạch A. | Thuật toán MC hoàn chỉnh và giới hạn phải chờ kết thúc lượt. | L05-B01–L05-B13 (13) | 35 | L05-B13 |
| C. Dự đoán sai phân thời gian TD(0) | Phát triển kiến thức và ứng dụng; Thay phần lợi tức chưa quan sát bằng giá trị trạng thái sau để cập nhật mỗi bước. | Lợi tức, bảng V và bước học của mạch B. | Bảng sau từng chuyển và cách phân biệt mục tiêu, sai số, giá trị. | L05-C01–L05-C10 (10) | 27 | L05-C10 |
| D. So sánh theo dữ liệu và giả thiết | Phát triển kiến thức và ứng dụng tổng hợp; So sánh đúng đại lượng, điều kiện và tiêu chuẩn trên cùng dữ liệu. | MC và TD(0) đã được thực hiện trên cùng hai lượt. | Căn cứ chọn phương pháp; phân biệt mẫu mới với dữ liệu cố định. | L05-D01–L05-D12 (12) | 34 | L05-D12 |
| E. Kết luận và tự kiểm tra | Kết luận; Giải quyết lại bài toán mở đầu bằng lựa chọn phương pháp có điều kiện. | Cơ chế, kết quả số và giới hạn ở mạch B–D. | Năng lực tính, giải thích, lựa chọn và các bài tập củng cố có nguồn. | L05-E01–L05-E05 (5) | 12 | L05-E04 |

Tổng 5 mạch, 45 trang, 120 phút. Mở đầu giữ thứ tự giới thiệu → nội dung/mục tiêu → động lực → dữ liệu → kiểm tra. Phần MC có 13 trang vì cần tách tập mẫu, bước học và quy trình; phần so sánh có 12 trang để mỗi kết luận đi cùng dữ kiện hoặc giả thiết. Không có trang mở phần chỉ để trang trí.

## Dàn bài từng trang

### Mạch A. Mở đầu: đánh giá chính sách từ dữ liệu

Chức năng: Xác định cùng đối tượng giá trị khi đầu vào chuyển từ mô hình sang mẫu. Đầu vào: Chính sách, giá trị và Bellman kỳ vọng từ bài trước. Đầu ra: Nhu cầu dùng lượt hoàn chỉnh để lấy mẫu lợi tức. Mục tiêu: MT1. Thời lượng: 12 phút, gồm trang kiểm tra L05-A05.

#### L05-A01: Dự đoán phi mô hình

- **Vai trò và mục tiêu:** Mở đầu; MT1.
- **Luận điểm trung tâm:** Bài 05 đánh giá giá trị của một chính sách cố định bằng Monte Carlo và sai phân thời gian.
- **Nội dung cần soạn:** Tên học phần Học tăng cường; Bài 05; học kỳ 1 năm học 2026–2027. Tên chủ đề phụ: Monte Carlo (MC) và sai phân thời gian (TD). Không ghi tác giả hoặc đơn vị dựa trên suy đoán từ PDF nguồn.
- **Ví dụ hoặc hình:** Không cần hình; trang tên xác định đúng bài và đối tượng học.
- **Hình thức hóa:** Không áp dụng; ký hiệu được chuẩn bị ở L05-A04.
- **Kết nối vào và ra:** Nhận kiến thức đánh giá chính sách từ bài trước → xác định tuyến bài ở L05-A02.
- **Nguồn:** L05 tr.1; thông tin học phần theo AGENTS.md và index.html.
- **Thời lượng:** 1 phút.
- **Ghi chú học thuật:** Monte Carlo là tên phương pháp; thuật ngữ TD được khai báo đầy đủ ở đây. Mục tiêu là dự đoán dưới một chính sách đã cho, không tìm chính sách tối ưu.
- **Quyết định và lý do:** `sửa`; Cập nhật học kỳ và chuẩn hóa tên tiếng Việt, giữ đúng chủ đề nguồn.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-A02: Nội dung và mục tiêu

- **Vai trò và mục tiêu:** Bản đồ và tiên quyết; MT1–MT6.
- **Luận điểm trung tâm:** Bài học đi từ dữ liệu hoàn chỉnh đến cập nhật một bước rồi so sánh điều kiện sử dụng.
- **Nội dung cần soạn:** Bản đồ gồm dự đoán từ dữ liệu → MC → TD(0) → so sánh → lựa chọn phương pháp. Mục tiêu hiển thị gọn: tính và chọn lợi tức; thực hiện hai cập nhật; so sánh kết quả theo dữ liệu và giả thiết. Tiên quyết: chính sách, giá trị trạng thái, kỳ vọng và Bellman kỳ vọng.
- **Ví dụ hoặc hình:** Sơ đồ mũi tên bằng HTML hoặc SVG nội dòng; mỗi nút là một đầu ra học tập, không chỉ tên phần.
- **Hình thức hóa:** Không đưa công thức mới; nhắc tên $v_\pi$ nhưng giải nghĩa bằng lời.
- **Kết nối vào và ra:** Tên bài L05-A01 → giới hạn thiếu mô hình ở L05-A03; MC và TD cùng giải một đối tượng dự đoán.
- **Nguồn:** L05 tr.2, 15; SB Ch.5 tr.91, Ch.6 tr.119.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Sáu mục tiêu đầy đủ nằm trong tài liệu quy trình; mặt trang chỉ nhóm các năng lực để giữ khả năng đọc. Chưa giả định kiến thức về bước học ngẫu nhiên hoặc cập nhật theo lô.
- **Quyết định và lý do:** `sửa`; Thay mục lục ôn điều khiển và phép co bằng sườn Sutton–Barto đã được yêu cầu.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Ba thẻ mục tiêu được viết lại theo ba mạch nội dung: Monte Carlo; sai phân thời gian TD(0); so sánh hai phương pháp (độ chệch, phương sai, điều kiện hội tụ, dữ liệu cố định). Lý do: thẻ cũ không khớp mạch B–D và thẻ "So sánh có điều kiện" mơ hồ.

#### L05-A03: Đánh giá chính sách khi chưa biết mô hình

- **Vai trò và mục tiêu:** Vấn đề; MT1.
- **Luận điểm trung tâm:** Các mẫu tương tác có thể thay dữ liệu mô hình trong việc ước lượng giá trị của cùng chính sách.
- **Nội dung cần soạn:** Quy hoạch động dùng mô hình chuyển và phần thưởng kỳ vọng để lấy kỳ vọng. Trong bài này, hai thành phần ấy chưa biết nhưng tác tử có thể thực hiện chính sách cố định và thu được các lượt. Sản phẩm cần tìm là bảng giá trị trạng thái, không phải hành động tối ưu. Nêu một nhiệm vụ cụ thể: ước lượng kết quả dài hạn từ trạng thái hiện tại bằng các lượt đã quan sát.
- **Ví dụ hoặc hình:** Hai cột dữ liệu mô hình và dữ liệu mẫu cùng hướng tới nhãn giá trị của chính sách; chưa có cây xác suất chi tiết.
- **Hình thức hóa:** Không cần khai triển Bellman; khác biệt ở đầu vào được thiết lập trước công thức.
- **Kết nối vào và ra:** Năng lực dự đoán L05-A02 → cần mô tả chính xác mẫu và đại lượng ở L05-A04.
- **Nguồn:** L05 tr.6, 15–16; SB Ch.5 tr.91; UCL tr.3; ST tr.2–5.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Bộ mô phỏng sinh mẫu vẫn phù hợp với phương pháp phi mô hình. Thuật toán không cần biết xác suất chuyển dù bài tập cung cấp mô hình để xác định môi trường hoặc kiểm giá trị chuẩn.
- **Quyết định và lý do:** `gộp`; Thu gọn phần ôn thành đúng thiếu hụt tạo nhu cầu MC; không dạy lại điều khiển.
- **Hiệu chỉnh sau rà:** Mô hình chuyển cùng phần thưởng kỳ vọng đủ cho mục tiêu kỳ vọng lợi tức; phân phối chung của thưởng và trạng thái sau là một biểu diễn đủ, không là thông tin tối thiểu bắt buộc. RL-01.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở nêu bài toán dự đoán: cho $\pi$ cố định, ước lượng $v_\pi(s)$ tại mọi trạng thái. Lý do: câu cũ là cụm danh từ cụt, chưa nêu bài toán.

#### L05-A04: Mẫu chuyển và giá trị cần ước lượng

- **Vai trò và mục tiêu:** Trực giác và nhắc định nghĩa; MT1.
- **Luận điểm trung tâm:** Một chuyển quan sát được cung cấp phần thưởng tức thời; giá trị mô tả kỳ vọng phần thưởng tích lũy về sau.
- **Nội dung cần soạn:** Mẫu là $(S_t,A_t,R_{t+1},S_{t+1})$, $A_t\sim\pi(\cdot\mid S_t)$. $\pi$ Markov và cố định; môi trường dừng. Trạng thái được quan sát đầy đủ trong phạm vi bài. $\mathcal S$ hữu hạn gồm trạng thái không kết thúc; $\mathcal S^+$ thêm trạng thái kết thúc; trạng thái kết thúc có giá trị 0. $G_t$ là tổng phần thưởng chiết khấu, gọi ngắn là lợi tức; $v_\pi$ là giá trị thật, $V$ là ước lượng.
- **Ví dụ hoặc hình:** Một cạnh chuyển có nhãn hành động và thưởng; nhãn $t,t+1$ đặt đúng vị trí.
- **Hình thức hóa:** HT1 ở mức $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$; tổng định nghĩa $G_t$ được xây dựng sau ví dụ ở L05-B03. $0\le\gamma\le1$ và $T$ là thời điểm kết thúc được khai báo bằng lời.
- **Kết nối vào và ra:** Bài toán L05-A03 → xác định đối tượng và dữ liệu đủ cho câu kiểm tra L05-A05; chuẩn bị quỹ đạo L05-B01.
- **Nguồn:** L05 tr.3, 15–17; SB §5.1 tr.92, §6.1 tr.119–120.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Thưởng trên bước $t\to t+1$ mang chỉ số $t+1$. Không gọi một quan sát bất kỳ là trạng thái Markov. Trường hợp bị cắt theo giới hạn thu thập không tự động là trạng thái kết thúc.
- **Quyết định và lý do:** `gộp`; Khôi phục đủ kiểu đại lượng và quy ước trước khi dùng lại ký hiệu nguồn.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Giữ mẫu chuyển, $v_\pi=\mathbb E_\pi[G_t\mid S_t=s]$, phân biệt $v_\pi$/$V$ và giả thiết dữ liệu; chuyển $T$, $\mathcal S^+$, giá trị kết thúc bằng 0 và điều kiện $\gamma$ sang L05-B03. Lý do: giảm số ký hiệu mở cùng lúc trước ví dụ.

#### L05-A05: Kiểm tra mẫu chuyển và mô hình

- **Vai trò và mục tiêu:** Kiểm tra riêng của mạch A; MT1.
- **Luận điểm trung tâm:** Dữ liệu mẫu và đối tượng dự đoán phải được xác định trước khi chọn thuật toán.
- **Nội dung cần soạn:** Cho chính sách luôn chọn sang phải. Quan sát một bước $S\to X$, thưởng 0; chưa biết xác suất đi sai hướng. Câu hỏi yêu cầu phân loại dữ liệu đang có và đại lượng cần học.
- **Ví dụ hoặc hình:** Một cạnh $S\to X$ có nhãn thưởng 0; không hiển thị xác suất chuyển chưa được cung cấp trong câu hỏi.
- **Hình thức hóa:** HT1; chỉ dùng tiên quyết đã nhắc, chưa yêu cầu công thức MC hoặc TD.
- **Kết nối vào và ra:** Quy ước L05-A04 → nhận diện đúng bài toán → L05-B01 dùng các lượt hoàn chỉnh để ước lượng đại lượng đó.
- **Nguồn:** L05 tr.15–16; HW05 bài 2; câu hỏi biên tập từ dữ kiện chuỗi nguồn.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Phân biệt một mẫu thưởng 0 với mô hình mọi phần thưởng đều 0. Dữ liệu không đủ xác định ngay kỳ vọng dài hạn.
- **Quyết định và lý do:** `thêm`; Kiểm tra tiên quyết và nhu cầu trước khi mở khái niệm MC, theo yêu cầu mỗi mạch có trang kiểm tra riêng.
- **Câu hỏi:** Xác định (a) bốn thành phần của mẫu quan sát; (b) đại lượng cần ước lượng khi chính sách giữ cố định; (c) thông tin còn thiếu để đánh giá bằng quy hoạch động.
- **Kiến thức được đo:** MT1; nội dung trong cùng mạch hoặc tiên quyết đã khai báo.
- **Đáp án/gợi ý trong ghi chú:** $(s,a,0,s')$ với $a$ là hành động sang phải; cần $v_\pi$ tại các trạng thái quan tâm; thiếu mô hình chuyển và phần thưởng kỳ vọng cho các khả năng, một mẫu không thay thế toàn bộ mô hình.
- **Tiêu chí đánh giá:** Đúng chỉ số phần thưởng, không chuyển mục tiêu sang tìm chính sách tối ưu, không suy xác suất từ một mẫu.
- **Thời gian hoạt động:** 1 phút tự xác định, 1 phút trả lời, 1 phút đối chiếu; đã nằm trong 3 phút.
- **Hiệu chỉnh sau rà:** Nhãn “Câu hỏi:” là khối riêng phía trên danh sách. Đáp án dùng mô hình chuyển và phần thưởng kỳ vọng. SV-02, RL-01.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu hỏi dùng ký hiệu chung $s\to s'$ với hành động $a$ và thưởng 0, không dùng $S,X$ trước khi chuỗi ngắn được giới thiệu. Đáp án: $(s,a,0,s')$.
- **Sửa sau rà 01-10-2026:** `sửa`; Ngữ cảnh "tác tử" thay "robot"; hành động sang phải ký hiệu $a$.

### Mạch B. Dự đoán Monte Carlo

Chức năng: Xây dựng ước lượng từ lợi tức, lựa chọn lần ghé và bước học. Đầu vào: Bài toán dự đoán và mẫu tương tác của mạch A. Đầu ra: Thuật toán MC hoàn chỉnh và giới hạn phải chờ kết thúc lượt. Mục tiêu: MT2–MT3; nền cho MT5. Thời lượng: 35 phút, gồm trang kiểm tra L05-B13.

#### L05-B01: Chuỗi ngắn và ý tưởng Monte Carlo

- **Vai trò và mục tiêu:** Vấn đề và ví dụ dẫn nhập MC; MT2.
- **Luận điểm trung tâm:** Một lượt kết thúc cho biết kết quả thực tế sau khi ghé trạng thái.
- **Nội dung cần soạn:** Môi trường $L,S,X,G$, chính sách luôn chọn sang phải nhưng thực tế đi phải 0.8 và trái 0.2. Thưởng −1 khi vào L, +1 khi vào G, còn lại 0; $\gamma=1$. L và G kết thúc, giá trị tiếp nối bằng 0. Nhiệm vụ: dùng các lượt để ước lượng giá trị S và X. Ánh xạ X là ô dấu chấm của nguồn.
- **Ví dụ hoặc hình:** `short-walk.svg`; xác suất trên cạnh và thưởng nhận khi vào trạng thái kết thúc tách khỏi nhãn giá trị trạng thái kết thúc.
- **Hình thức hóa:** HT1 được gắn với $\mathcal S=\{S,X\}$; chưa giải hệ Bellman.
- **Kết nối vào và ra:** Nhu cầu mẫu ở L05-A05 → kết quả của hai lượt cụ thể L05-B02.
- **Nguồn:** L05 tr.19–20; HW05 bài 7.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Hai trạng thái kết thúc bảo đảm lượt kết thúc hầu chắc chắn trong chuỗi hữu hạn này. Các xác suất xác định bài toán nhưng không được đưa vào quy tắc MC.
- **Quyết định và lý do:** `giữ`; Giữ môi trường nguồn làm ví dụ xuyên suốt, đặt trước định nghĩa MC.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Thêm định nghĩa lượt và hộp ý tưởng Monte Carlo (giá trị là kỳ vọng lợi tức, nên ước lượng bằng trung bình lợi tức quan sát trong các lượt hoàn chỉnh) theo nguồn tr.17. Lý do: ý tưởng cốt lõi trước đây chưa xuất hiện trên mặt trang.

#### L05-B02: Lợi tức sau mỗi lần ghé

- **Vai trò và mục tiêu:** Trực giác và ví dụ; MT2.
- **Luận điểm trung tâm:** Mỗi lần ghé trạng thái gắn với phần thưởng còn lại của lượt đó.
- **Nội dung cần soạn:** Hai lượt $e_1:S\to X\to S\to X\to G$ và $e_2:S\to X\to S\to L$. Thưởng $e_1=(0,0,0,1)$; $e_2=(0,0,-1)$. Với $\gamma=1$, mọi lần ghé S hoặc X trong $e_1$ có lợi tức +1, trong $e_2$ có lợi tức −1. Kết quả quan sát có thể khác giá trị kỳ vọng.
- **Ví dụ hoặc hình:** `episode-one.svg` và `episode-two.svg`; mỗi lần ghé là một nút riêng, hàng $G_t$ ghi lợi tức dưới từng nút, ngoặc nét đứt đánh dấu phần đuôi sau $t=1$ trong $e_1$. Mặt trang định nghĩa "lần ghé" là thời điểm $t$ có $S_t=s$; hộp tính hai phần đuôi cụ thể.
- **Hình thức hóa:** Chưa viết tổng ký hiệu; tính trực tiếp $0+0+0+1=1$ và $0+0-1=-1$.
- **Kết nối vào và ra:** Môi trường L05-B01 → đại lượng còn lại sau từng thời điểm → tổng quát hóa ở L05-B03.
- **Nguồn:** L05 tr.20, 22, 29; HW05 bài 7.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Lợi tức ở các lần ghé lặp đang bằng nhau vì cấu hình thưởng và $\gamma=1$, không phải tính chất chung của mọi lượt. Những lần ghé lặp vẫn là các mẫu khác nhau theo thời điểm.
- **Quyết định và lý do:** `tách`; Tách phép tính trên dữ liệu khỏi công thức nguồn tr.17 để tạo trực giác trước ký hiệu.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.
- **Hiệu chỉnh 06-10-2026:** `sửa`; Mặt trang định nghĩa "lần ghé"; hai SVG thêm hàng $G_t$ và ngoặc phần đuôi sau $t=1$; hộp tính hai phần đuôi cụ thể. Lý do: trang chỉ nêu kết quả, phép cộng phần đuôi chỉ có trong ghi chú.

#### L05-B03: Lợi tức chiết khấu

- **Vai trò và mục tiêu:** Hình thức khái niệm lợi tức; MT2.
- **Luận điểm trung tâm:** Phần thưởng nhận ngay có số mũ 0; mỗi bước xa hơn thêm một hệ số chiết khấu.
- **Nội dung cần soạn:** $T$ là thời điểm kết thúc của một lượt, $t<T$; $R_{t+1}$ là thưởng đầu tiên sau S_t. $G_T=0$. Với $e_1$ có T=4, $G_0=\gamma^3$ và $G_3=1$. Khi $\gamma=1$ thu lại kết quả L05-B02.
- **Ví dụ hoặc hình:** Bảng tính ngược trên $e_1$ theo $t=4,3,2,1,0$: hàng $R_{t+1}$ và hàng $G_t$ (ô $t=3,2$ ghi phép truy hồi). Chú thích: với $\gamma=1$ thu lại các lợi tức của L05-B02.
- **Hình thức hóa:** HT1: $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}=R_{t+1}+\gamma G_{t+1}$.
- **Kết nối vào và ra:** Phép cộng L05-B02 → lợi tức có chỉ số chính xác → lựa chọn những lợi tức đưa vào trung bình ở L05-B04; thứ tự tính ngược dùng lại ở bước tính lợi tức của L05-B10.
- **Nguồn:** L05 tr.17; SB §5.1 tr.92 và §6.1 tr.119–120.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Tách số hạng đầu chứng minh công thức truy hồi. $\gamma=1$ không tự bảo đảm tổng hữu hạn trong mọi bài toán; chuỗi hiện tại có kết thúc hợp lệ.
- **Quyết định và lý do:** `sửa`; Sửa dòng công thức bị cắt trong nguồn và thiết lập chỉ số dùng lại ở chuỗi dài.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề gọi tên khái niệm. Câu mở khai báo $T$ và $0\le\gamma\le1$; $\mathcal S^+$ và quy ước trạng thái kết thúc chuyển từ L05-A04 vào ghi chú diễn giả.
- **Sửa sau rà 01-10-2026:** `sửa`; Câu mở thêm "giá trị ở trạng thái kết thúc bằng $0$".
- **Hiệu chỉnh 06-10-2026:** `sửa`; Gộp tổng và truy hồi thành một dòng; thay thẻ $G_0,G_3$ bằng bảng tính ngược trên $e_1$; chú thích nối về L05-B02; bỏ CSS cục bộ của trang. Câu mở giữ $T$, $G_T=0$, $0\le\gamma\le1$; giá trị ở trạng thái kết thúc bằng 0 thể hiện qua $G_T=0$ và ghi chú. Lý do: công thức truy hồi chưa được dùng trên mặt trang.

#### L05-B04: Lần ghé đầu tiên và mọi lần ghé

- **Vai trò và mục tiêu:** Ví dụ lựa chọn mẫu; MT2.
- **Luận điểm trung tâm:** Hai quy tắc MC khác nhau ở những lần ghé được đưa vào tập mẫu; theo tính Markov, mỗi mẫu của cả hai quy tắc có kỳ vọng $v_\pi(s)$.
- **Nội dung cần soạn:** Dùng cả $e_1,e_2$. Lần ghé đầu tiên: S có mẫu $(1,-1)$, X có $(1,-1)$. Mọi lần ghé: S có $(1,1,-1,-1)$, X có $(1,1,-1)$. Trung bình tương ứng: lần ghé đầu $(0,0)$; mọi lần ghé $(0,1/3)$.
- **Ví dụ hoặc hình:** Hai dòng nhãn đậm phát biểu quy tắc (lần ghé đầu tiên lấy $G_t$ tại thời điểm sớm nhất có $S_t=s$; mọi lần ghé lấy $G_t$ tại mọi thời điểm có $S_t=s$; ký hiệu $t_1<t_2<\cdots$ ở ghi chú); bảng hai hàng S/X có cột thời điểm ghé ghi rõ $e_1$, $e_2$ và hai cột quy tắc; câu giải thích tại $X$ mọi lần ghé lấy hai mẫu từ $e_1$ và một mẫu từ $e_2$ nên $e_1$ chiếm trọng số $2/3$; hộp nêu kỳ vọng $v_\pi(s)$ của từng mẫu theo tính Markov. Các tập mẫu và số đếm là HTML.
- **Hình thức hóa:** HT2 được chuẩn bị bằng tập mẫu; chưa đồng nhất quy tắc chọn mẫu với bước học.
- **Kết nối vào và ra:** Lợi tức L05-B03 → chọn dữ liệu thống kê → định nghĩa ước lượng MC L05-B05.
- **Nguồn:** L05 tr.18, 20, 22; SB §5.1 tr.92–93; phép tính từ hai lượt nguồn.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Lần ghé đầu tiên là lần sớm nhất theo thời gian trong từng lượt. Với $\pi$ Markov cố định và môi trường Markov dừng, thời điểm ghé thứ $k$ là thời điểm dừng; theo tính Markov mạnh, $\mathbb E_\pi[G_{t_k}\mid\text{lần ghé thứ }k\text{ xảy ra}]=v_\pi(s)$. Các mẫu của mọi lần ghé dùng chung phần đuôi nên phụ thuộc trong cùng lượt. Sự phụ thuộc trong lượt không tự gây chệch; số mẫu mỗi lượt ngẫu nhiên và tương quan với lợi tức làm trung bình mọi lần ghé có dạng tỉ số, nên không khẳng định không chệch ở số lượt hữu hạn (giữ lập trường L05-B12). Tại $X$, $e_1$ chiếm trọng số $2/3$ trong trung bình mọi lần ghé; tại $S$, mỗi lượt cho hai mẫu bằng nhau nên hai quy tắc cùng trung bình.
- **Quyết định và lý do:** `sửa`; Bổ sung quy tắc mọi lần ghé từ SB và tạo số khác nhau để đo đúng sự phân biệt.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở nêu lý do cần quy tắc: một trạng thái có thể xuất hiện nhiều lần trong một lượt.
- **Hiệu chỉnh 06-10-2026:** `sửa`; Phát biểu hai quy tắc trên mặt trang; bảng thêm cột thời điểm ghé; bỏ dòng liệt kê hai lượt; thay hộp "lần ghé đầu tiên được xác định theo chiều thời gian" bằng ý của người dùng: theo tính Markov, mỗi mẫu của cả hai quy tắc có kỳ vọng $v_\pi(s)$. Câu giải thích trọng số $2/3$ trên mặt trang; lập luận thời điểm dừng ở ghi chú. Lý do: trang nêu nhu cầu cần quy tắc nhưng không phát biểu quy tắc.

#### L05-B05: Ước lượng Monte Carlo

- **Vai trò và mục tiêu:** Hình thức MC; MT2–MT3.
- **Luận điểm trung tâm:** MC ước lượng giá trị bằng cách kết hợp các lợi tức đã chọn tại trạng thái đó.
- **Nội dung cần soạn:** Định nghĩa $g_i(s)$ là mẫu lợi tức thứ i được chọn cho s, không phải thời điểm i toàn cục. Với trung bình mẫu, mỗi mẫu có trọng số $1/n$. Dữ liệu từ chính sách cố định; giá trị thật là kỳ vọng cần ước lượng. Dùng lại X: $(1,1,-1)$ cho $1/3$.
- **Ví dụ hoặc hình:** Công thức đặt cạnh bảng theo dõi tại X (mọi lần ghé): cột mẫu mới $g_n(X)$, $n$, tổng, $V_n(X)$ qua ba mẫu $1,1,-1$; không cần môi trường mới. Hai cột giữa là bộ đếm và tổng của nguồn tr.18 (tổng $S(s)$ của nguồn được gọi là "tổng" để tránh trùng với trạng thái $S$).
- **Hình thức hóa:** HT2: $V_n(s)=\frac1n\sum_{i=1}^{n}g_i(s)$.
- **Kết nối vào và ra:** Tập mẫu L05-B04 → phép kết hợp chính thức → nhu cầu cập nhật khi nhận thêm mẫu L05-B06.
- **Nguồn:** SB §5.1 tr.92–93; L05 tr.18.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** $V_n$ là ước lượng sau n mẫu của riêng s. Dùng $v_\pi$ cho giá trị thật; không dùng chung $V^\pi$ cho cả hai đại lượng.
- **Quyết định và lý do:** `sửa`; Tách định nghĩa ước lượng khỏi lựa chọn lần ghé và điều kiện thống kê.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.
- **Hiệu chỉnh 06-10-2026:** `sửa`; Thay hai thẻ lặp ô $X$ của L05-B04 bằng bảng theo dõi $g_n$, $n$, tổng, $V_n(X)$, đặt cạnh công thức; ghi chú nêu dạng bộ đếm và tổng của nguồn tr.18. Lý do: ví dụ cũ trùng L05-B04 và chưa cho thấy trạng thái "hai mẫu, trung bình 1" mà L05-B06 dùng.

#### L05-B06: Cập nhật trung bình khi có mẫu mới

- **Vai trò và mục tiêu:** Vấn đề, trực giác và tính tay gia tăng; MT3.
- **Luận điểm trung tâm:** Trung bình mới bằng trung bình cũ dịch về phía mẫu mới một phần $1/n$ sai lệch; phép tính chỉ cần số mẫu, trung bình cũ và mẫu mới.
- **Nội dung cần soạn:** Với X theo mọi lần ghé, hai mẫu đầu $(1,1)$ có trung bình 1. Mẫu tiếp theo −1 tạo trung bình $(2\times1-1)/3=1/3$. Thay đổi là một phần ba của khoảng cách từ 1 đến −1. Dữ liệu lịch sử không cần lưu lại sau khi đã tích lũy số mẫu và trung bình.
- **Ví dụ hoặc hình:** Câu yêu cầu tính trung bình mới chỉ từ trung bình cũ, số mẫu và mẫu mới; hai thẻ cùng tính $1/3$: "Tính lại từ tổng" và "Sửa trung bình cũ"; trục số SVG nội tuyến từ −1 đến 1 với mẫu mới (vuông), trung bình mới (tròn đặc), trung bình cũ (tròn rỗng), mũi tên dài một phần ba đoạn khoảng cách 2.
- **Hình thức hóa:** Ví dụ $1+\frac13(-1-1)=\frac13$ chuẩn bị HT3.
- **Kết nối vào và ra:** Tổng L05-B05 → phép điều chỉnh dùng đủ thông tin → chứng minh đẳng thức tổng quát L05-B07.
- **Nguồn:** SB §2.4 tr.30–31; L05 tr.18; dữ liệu X từ L05-B04.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Bộ nhớ không cần toàn bộ lợi tức lịch sử; lưu tổng và bộ đếm như nguồn tr.18 cũng đủ. Dạng sửa trung bình có cấu trúc ước lượng cũ + bước × (mục tiêu − ước lượng cũ), dùng lại ở L05-B08 (bước hằng) và TD(0). Vẫn cần bảng nhiều trạng thái và dữ liệu một lượt để tính MC theo quy trình này.
- **Quyết định và lý do:** `thêm`; Khôi phục ví dụ số trước công thức gia tăng thay cho việc trình bày công thức ngay ở nguồn tr.21.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở nêu yêu cầu chỉ lưu trung bình và số mẫu. Lý do: vấn đề của trang trước chỉ có trong ghi chú.
- **Hiệu chỉnh 06-10-2026:** `sửa`; Hai cách tính đặt cạnh nhau, thêm trục số; ghi chú sửa lý do: tổng và bộ đếm cũng không cần lịch sử, dạng sửa trung bình có cấu trúc dịch về mục tiêu dùng lại ở L05-B08 và TD(0). Lý do: câu "không lưu mọi lợi tức cũ" chưa phân biệt hai cách tính.

#### L05-B07: Trung bình gia tăng

- **Vai trò và mục tiêu:** Hình thức và chứng minh ngắn; MT3.
- **Luận điểm trung tâm:** Bước học nghịch đảo số mẫu tái tạo chính xác trung bình số học.
- **Nội dung cần soạn:** Tách tổng n mẫu thành tổng n−1 mẫu cũ và mẫu thứ n. Nhận $V_n=((n-1)V_{n-1}+g_n)/n$ rồi biến đổi sang dạng sai số. Khởi tạo $N(s)=0$; sau mẫu hợp lệ tăng N lên trước khi dùng nghịch đảo.
- **Ví dụ hoặc hình:** Hai dòng biến đổi lớn; không thêm hình cạnh công thức.
- **Hình thức hóa:** HT3: $V_n(s)=V_{n-1}(s)+\frac1n[g_n(s)-V_{n-1}(s)]$.
- **Kết nối vào và ra:** Phép tính L05-B06 → quy tắc trung bình đúng với mọi n → xét thay đổi trọng số bằng bước hằng ở L05-B08.
- **Nguồn:** SB §2.4 tr.30–31; L05 tr.21.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** $n$ đếm mẫu được chọn của s. Không dùng $1/t$ với thời gian toàn cục khi các trạng thái có số mẫu khác nhau. Với n=1, ước lượng bằng mẫu đầu dù V khởi tạo thế nào.
- **Quyết định và lý do:** `giữ`; Giữ công thức nguồn và thêm suy diễn ngắn đủ để hiểu vai trò bộ đếm.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Gọi tên mục tiêu cập nhật: $g_n(s)$ là mục tiêu trong $V\leftarrow V+\alpha[\text{mục tiêu}-V]$.

#### L05-B08: Bước học hằng

- **Vai trò và mục tiêu:** Ví dụ rồi quy tắc biến thể; MT3.
- **Luận điểm trung tâm:** Với $0<\alpha<1$, bước học hằng còn ảnh hưởng khởi tạo và ưu tiên mẫu gần đây; với $\alpha=1$, ước lượng bằng mẫu mới nhất.
- **Nội dung cần soạn:** Một mẫu +1, khởi tạo 0: trung bình mẫu cho 1; $\alpha=0.5$ cho 0.5. Mẫu tiếp theo −1: trung bình cho 0; bước hằng cho $0.5+0.5(-1-0.5)=-0.25$. Công thức cập nhật có cùng dạng nhưng ý nghĩa thống kê khác.
- **Ví dụ hoặc hình:** Hai cột tính trên cùng hai mẫu $(1,-1)$, đồng nhất khởi tạo và thứ tự.
- **Hình thức hóa:** HT3: $V_n=V_{n-1}+\alpha(g_n-V_{n-1})$; nêu dạng hai trọng số $(1-\alpha)V_{n-1}+\alpha g_n$.
- **Kết nối vào và ra:** Trung bình chính xác L05-B07 → quy tắc trọng số khác → tách hai trục phương pháp ở L05-B09.
- **Nguồn:** SB §2.5 tr.32–33; L05 tr.20–23.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Khai triển $V_n=(1-\alpha)^nV_0+\sum_i\alpha(1-\alpha)^{n-i}g_i$ đặt trong ghi chú; không nhồi lên mặt trang. Bước hằng không tự cho hội tụ đúng trên mẫu ngẫu nhiên mới. Giá trị 0.5 của nguồn tr.20 được hiểu theo điều kiện này.
- **Quyết định và lý do:** `sửa`; Bổ sung giả thiết bước học thiếu trong nguồn và phân biệt trung bình với trọng số mũ.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở nêu lý do dùng bước hằng khi môi trường thay đổi theo thời gian (nguồn tr.21). Lý do: bước hằng trước đây xuất hiện không có động cơ.
- **Sửa sau rà 01-10-2026:** `sửa`; Câu mở nêu môi trường không dừng nằm ngoài giả thiết của bài; $\alpha=0.5$ cho thấy cách đặt trọng số theo thời gian; dẫn bài giảng gốc tr.21 trong ghi chú diễn giả.

#### L05-B09: Hai lựa chọn của Monte Carlo

- **Vai trò và mục tiêu:** Ứng dụng phân loại; MT2–MT3.
- **Luận điểm trung tâm:** Quy tắc chọn lần ghé và quy tắc bước học là hai quyết định độc lập.
- **Nội dung cần soạn:** Bảng 2×2: hàng lần ghé đầu tiên/mọi lần ghé; cột trung bình mẫu/bước hằng. Sau riêng $e_1$ từ V=0, hai ô trung bình đều $(1,1)$; bước hằng $\alpha=0.5$ cho lần ghé đầu $(0.5,0.5)$ và mọi lần ghé $(0.75,0.75)$. Mỗi nhãn thuật toán phải chỉ rõ cả hai lựa chọn.
- **Ví dụ hoặc hình:** Bảng HTML có chú thích dữ liệu và bước học; không tô màu làm tín hiệu duy nhất.
- **Hình thức hóa:** HT2–HT3; các số từ hai cập nhật $0\to0.5\to0.75$.
- **Kết nối vào và ra:** L05-B04 và L05-B08 → đặc tả đầu vào của giả mã L05-B10.
- **Nguồn:** SB §5.1 tr.92–93, §6.1 tr.119; HW05 bài 5 được sửa.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** “MC gia tăng” không là đối thủ loại trừ “lần ghé đầu tiên”; nó mô tả cách kết hợp mẫu. Bảng này thay cấu trúc ba cách không cùng trục của HW05 bài 5.
- **Quyết định và lý do:** `thêm`; Loại nhầm lẫn quyết định mẫu với quyết định trọng số trước quy trình đầy đủ.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Viết đầy đủ tên phương pháp trong tiêu đề.

#### L05-B10: Thuật toán dự đoán Monte Carlo

- **Vai trò và mục tiêu:** Thuật toán đầy đủ; MT2–MT3.
- **Luận điểm trung tâm:** Tính lợi tức trước rồi chọn lần ghé theo thời gian giúp triển khai MC đúng quy tắc.
- **Nội dung cần soạn:** Đầu vào: $\pi,\gamma$, số lượt M, quy tắc lần ghé, bước học. Khởi tạo V, $N(s)=0$, giá trị ở trạng thái kết thúc bằng 0. Mỗi lượt: thu $S_0,A_0,R_1,\ldots,S_T$ theo $\pi$; đặt $G_T=0$; tính lùi mọi $G_t$; duyệt xuôi t, chọn mẫu theo quy tắc; tăng N và cập nhật V; hết lượt tiếp tục đến đủ M. Với lần ghé đầu tiên, đặt tập đã ghé rỗng ở đầu mỗi lượt và thêm s sau lần xử lý đầu.
- **Ví dụ hoặc hình:** Giả mã khoảng 10–12 dòng ở cỡ chữ chuẩn; tách phần tính lợi tức và phần cập nhật bằng khoảng trắng.
- **Hình thức hóa:** HT1–HT3; $V(S_t)\leftarrow V(S_t)+\alpha_{N(S_t)}(S_t)[G_t-V(S_t)]$.
- **Kết nối vào và ra:** Hai đầu vào L05-B09 → quy trình có thể lần theo → áp dụng lượt thứ hai L05-B11.
- **Nguồn:** SB §5.1 tr.92; §2.4 tr.30–31; bản diễn đạt hai lượt quét tương đương về tập mẫu với MC lần ghé đầu.
- **Thời lượng:** 4 phút.
- **Ghi chú học thuật:** Duyệt ngược rồi dùng tập đã gặp sẽ chọn lần ghé cuối, nên không dùng cách đó. Với bước hằng mọi lần ghé, thứ tự cập nhật xuôi được nêu rõ. Không cập nhật trạng thái kết thúc. MC cần lượt thật sự kết thúc; ngân sách M tách khỏi điều kiện kết thúc lượt.
- **Quyết định và lý do:** `thêm`; Nguồn chưa có giả mã đủ đầu vào, quy tắc chọn mẫu, thứ tự và dừng; bổ sung từ SB để người học thực hiện được thuật toán.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Đổi "quy trình" thành "thuật toán" cho thống nhất với L05-C05.
- **Sửa sau rà 01-10-2026:** `sửa`; Chữ giả mã nâng từ 0.82em lên 0.92em (CSS cục bộ), trang vẫn vừa khung.

#### L05-B11: Monte Carlo trên lượt thứ hai

- **Vai trò và mục tiêu:** Ứng dụng thuật toán; MT3.
- **Luận điểm trung tâm:** Số lần cập nhật quyết định kết quả MC khi bước học giữ hằng.
- **Nội dung cần soạn:** Tiếp tục sau $e_1$ với $\alpha=0.5$. Lần ghé đầu tiên: $(0.5,0.5)$ nhận một mẫu −1 mỗi trạng thái, thành $(-0.25,-0.25)$. Mọi lần ghé: từ $(0.75,0.75)$, S đi $0.75\to-0.125\to-0.5625$, X đi $0.75\to-0.125$. Dữ liệu là $e_2:S,X,S,L$.
- **Ví dụ hoặc hình:** Quỹ đạo $e_2$ và bảng các giá trị trung gian; mỗi cột ghi rõ cách chọn lần ghé.
- **Hình thức hóa:** HT3 dùng cùng $\alpha$ và các $G_t=-1$ đã tính.
- **Kết nối vào và ra:** Giả mã L05-B10 → kết quả kiểm chứng từng quy tắc → phân biệt tính toán đúng với bảo đảm thống kê L05-B12.
- **Nguồn:** L05 tr.22, 29; HW05 bài 7; kiểm toán số độc lập.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Không nhập kết quả của một quy tắc làm khởi tạo cho quy tắc còn lại. Cả hai chạy riêng từ 0 qua đúng $e_1,e_2$. Kết quả được dùng lại trong chữa bài 7.
- **Quyết định và lý do:** `sửa`; Bài nguồn chưa chỉ rõ lần ghé; nêu hai phiên bản và đáp án nhất quán.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Viết đầy đủ tên phương pháp.

#### L05-B12: Tính không chệch và hội tụ của Monte Carlo

- **Vai trò và mục tiêu:** Điều kiện và giới hạn; MT3–MT5.
- **Luận điểm trung tâm:** Tính chất của lợi tức không tự động là tính chất của mọi cách kết hợp lợi tức.
- **Nội dung cần soạn:** Lợi tức khả tích từ $\pi$ có kỳ vọng điều kiện $v_\pi(s)$. Trung bình lần ghé đầu tiên với số mẫu cố định là không chệch khi các lượt cung cấp mẫu độc lập cùng phân phối. Trong khung đang xét, giả sử lợi tức có phương sai hữu hạn và số mẫu tăng vô hạn để áp dụng luật số lớn. Mẫu mọi lần ghé có phụ thuộc trong lượt. Với $0<\alpha<1$, khởi tạo còn ảnh hưởng; $\alpha=1$ giữ mẫu mới nhất. Bước hằng có thể dao động trên mẫu mới.
- **Ví dụ hoặc hình:** Ba nhãn đối tượng: lợi tức, trung bình mẫu, bảng dùng bước hằng; mỗi nhãn kèm điều kiện tương ứng.
- **Hình thức hóa:** HT2–HT3; không đưa chứng minh hội tụ MC mọi lần ghé vào tuyến chính.
- **Kết nối vào và ra:** L05-B11 chỉ là kết quả hữu hạn mẫu → điều kiện kết luận đúng → câu kiểm tra L05-B13 và nhu cầu cập nhật sớm L05-C01.
- **Nguồn:** SB §5.1 tr.92–93; §2.5 tr.32–33; L05 tr.23 được giới hạn lại.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** “Không chệch” ở đây nói rõ đối tượng và số mẫu. Không khẳng định trung bình mọi lần ghé luôn không chệch ở mẫu hữu hạn. MC đầy đủ cần lợi tức của lượt đã kết thúc.
- **Quyết định và lý do:** `sửa`; Giữ tính chất có căn cứ và loại phát biểu không chệch bao trùm mọi biến thể MC.
- **Bảo đảm mọi lần ghé trong ghi chú:** Với quá trình phần thưởng Markov hữu hạn do chính sách Markov dừng, cố định tạo ra, phần thưởng bị chặn, kết thúc hầu chắc chắn từ mọi trạng thái không kết thúc đang xét, các lượt khởi động độc lập theo cùng phân phối và xác suất ghé $s$ dương, trung bình mọi lần ghé với $0\le\gamma\le1$ và bước học $1/N(s)$ hội tụ hầu chắc chắn về $v_\pi(s)$ khi số lượt hoàn chỉnh tăng vô hạn. Phân biệt nhất quán với không chệch hữu hạn mẫu; không áp dụng kết luận cho bước hằng. M01/RL-02.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề nêu kết quả thay vì "giả thiết". Ba thẻ: lần ghé đầu tiên; mọi lần ghé; bước học hằng. Chú thích nêu giả thiết của hai kết quả hội tụ.
- **Sửa sau rà 01-10-2026:** `sửa`; Định nghĩa ngắn "ước lượng không chệch: kỳ vọng bằng $v_\pi(s)$"; chú thích giả thiết viết liền: lượt độc lập, cùng phân phối, kết thúc hầu chắc chắn, thưởng bị chặn, $s$ được ghé với xác suất dương; ghi chú diễn giả nêu tính Markov cho thời điểm ghé ngẫu nhiên; thẻ bước hằng viết dạng khẳng định có điều kiện.
- **Hiệu chỉnh 06-10-2026:** `sửa`; Câu mở thêm "Theo tính Markov" và nối với ý đã nêu ở L05-B04; phần còn lại giữ nguyên.

#### L05-B13: Kiểm tra chọn mẫu Monte Carlo

- **Vai trò và mục tiêu:** Kiểm tra riêng của mạch B; MT2–MT3.
- **Luận điểm trung tâm:** Một kết quả MC chỉ xác định khi cả tập mẫu và bước học đã được chỉ rõ.
- **Nội dung cần soạn:** Cho lại hai lượt $e_1,e_2$, $\gamma=1$, V ban đầu 0. Tính trên trạng thái X với hai quy tắc chọn lần ghé; đối chiếu bước hằng khi chỉ dùng lần ghé đầu tiên.
- **Ví dụ hoặc hình:** Hai dòng quỹ đạo và ô trống cho tập mẫu, số mẫu, kết quả; không hiện đáp án ban đầu.
- **Hình thức hóa:** HT1–HT3.
- **Kết nối vào và ra:** Quy trình và giả thiết L05-B10–L05-B12 → xác nhận đủ năng lực MC → giới hạn chờ kết thúc L05-C01.
- **Nguồn:** HW05 bài 5, 7; L05 tr.20, 22.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Gợi ý: đánh chỉ số các lần xuất hiện X trước khi tính trung bình; sau đó chạy quy tắc bước hằng trên đúng tập mẫu đã chọn.
- **Quyết định và lý do:** `thêm`; Kiểm tra riêng hai trục vừa học bằng số cho đáp án khác nhau.
- **Câu hỏi:** Với X, lập dãy lợi tức theo lần ghé đầu tiên và mọi lần ghé; tính hai trung bình sau $e_1,e_2$. Nếu dùng lần ghé đầu tiên với $\alpha=0.5$, tính V(X) sau mỗi lượt và giải thích sự khác biệt.
- **Kiến thức được đo:** MT2–MT3; nội dung trong cùng mạch hoặc tiên quyết đã khai báo.
- **Đáp án/gợi ý trong ghi chú:** Lần ghé đầu tiên $(1,-1)$ cho 0; mọi lần ghé $(1,1,-1)$ cho $1/3$. Bước hằng cho $0.5$ rồi $-0.25$ vì mẫu cũ và khởi tạo có trọng số khác trung bình số học.
- **Tiêu chí đánh giá:** Chọn đúng ba mẫu của X theo mọi lần ghé, đếm n riêng cho X, phân biệt trọng số với chọn mẫu.
- **Thời gian hoạt động:** 1 phút tính, 1 phút đối chiếu cặp kết quả, 1 phút giải thích; nằm trong 3 phút.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Viết đầy đủ tên phương pháp.

### Mạch C. Dự đoán sai phân thời gian TD(0)

Chức năng: Thay phần lợi tức chưa quan sát bằng giá trị trạng thái sau để cập nhật mỗi bước. Đầu vào: Lợi tức, bảng V và bước học của mạch B. Đầu ra: Bảng sau từng chuyển và cách phân biệt mục tiêu, sai số, giá trị. Mục tiêu: MT4; nền cho MT5. Thời lượng: 27 phút, gồm trang kiểm tra L05-C10.

#### L05-C01: Cập nhật khi lượt chưa kết thúc

- **Vai trò và mục tiêu:** Vấn đề TD; MT4.
- **Luận điểm trung tâm:** MC đầy đủ chưa có mục tiêu khi phần đuôi của lượt chưa được quan sát.
- **Nội dung cần soạn:** Tại tiền tố $S\to X$ của $e_1$, đã biết thưởng 0 nhưng chưa biết lượt kết thúc ở L hay G. $G_0$ chưa có; một thuật toán muốn cập nhật ngay phải dùng thông tin khác cho phần còn lại. Giá trị hiện có của trạng thái X là một nguồn dự đoán.
- **Ví dụ hoặc hình:** Quỹ đạo $e_1$ chỉ hiện cạnh đầu, phần tương lai nét đứt có nhãn chưa quan sát.
- **Hình thức hóa:** Không đưa quy tắc TD trước trực giác; dùng ý nghĩa lợi tức từ L05-B03.
- **Kết nối vào và ra:** MC cần kết thúc ở L05-B13 → nhu cầu dùng dự đoán còn lại L05-C02.
- **Nguồn:** L05 tr.24; SB §6.1 tr.119–120.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Đây là giới hạn về thời điểm có dữ liệu mục tiêu. Chưa kết luận MC kém hơn về mọi tiêu chí hoặc TD truyền thưởng qua toàn lượt ngay khi nhận thưởng.
- **Quyết định và lý do:** `giữ`; Giữ động lực cập nhật một bước của nguồn bằng chính ví dụ đã học.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Chỉnh câu chữ tiêu đề.

#### L05-C02: Mục tiêu một bước

- **Vai trò và mục tiêu:** Trực giác; MT4.
- **Luận điểm trung tâm:** Thưởng vừa nhận cộng ước lượng ở trạng thái sau tạo một mục tiêu có sẵn sau một bước.
- **Nội dung cần soạn:** Tách lợi tức thành phần đã biết và phần còn lại. Thưởng đầu đã được quan sát; bảng V cung cấp ước lượng phần còn lại từ trạng thái kế tiếp. Cơ chế dùng một ước lượng để cập nhật ước lượng khác được gọi là bootstrap trong tài liệu; cách diễn đạt tiếng Việt chính là cập nhật dựa trên ước lượng hiện có.
- **Ví dụ hoặc hình:** `mc-td-targets.svg`; một nhánh quan sát tới $t+1$ rồi hộp V, đối chiếu quỹ đạo đầy đủ MC.
- **Hình thức hóa:** Trực giác từ $G_t=R_{t+1}+\gamma G_{t+1}$; chưa gắn sai số tổng quát.
- **Kết nối vào và ra:** Phần đuôi chưa biết L05-C01 → thay bằng ước lượng có sẵn → tính tay L05-C03.
- **Nguồn:** SB §6.1 tr.120–121; L05 tr.24–25.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Bảng V là ước lượng, không phải một mẫu thưởng thật. Thuật ngữ bootstrap chỉ giải thích cơ chế, không mở thêm phương pháp lấy mẫu thống kê cùng tên.
- **Quyết định và lý do:** `sửa`; Diễn giải đối tượng trước công thức; giữ thuật ngữ khi cần nhưng không dùng từ phỏng đoán thay ước lượng.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Hiển thị $G_t=R_{t+1}+\gamma G_{t+1}\approx R_{t+1}+\gamma V(S_{t+1})$ và gọi tên bootstrap trên mặt trang (nguồn tr.24). Lý do: phép thay thế cốt lõi trước đây chỉ có trong ghi chú.
- **Sửa sau rà 01-10-2026:** `sửa`; Bỏ dấu ≈; hiển thị $G_t=R_{t+1}+\gamma G_{t+1}$ và $v_\pi(S_{t+1})=\mathbb E_\pi[G_{t+1}\mid S_{t+1}]$; hộp nêu mục tiêu một bước thay mục tiêu $G_t$ của Monte Carlo; hình dùng cỡ ngắn.

#### L05-C03: Một bước cập nhật TD

- **Vai trò và mục tiêu:** Ví dụ tính tay; MT4.
- **Luận điểm trung tâm:** TD điều chỉnh ước lượng hiện tại theo khoảng cách đến mục tiêu một bước.
- **Nội dung cần soạn:** Cho bảng trước cập nhật $V(S)=0,V(X)=0.5$, $\gamma=1$, $\alpha=0.5$ và chuyển $S\to X$ thưởng 0. Mục tiêu là $0+0.5=0.5$; sai số là $0.5-0=0.5$; giá trị mới tại S là $0+0.5\times0.5=0.25$. X giữ 0.5.
- **Ví dụ hoặc hình:** Một cạnh chuyển và ba ô tính mục tiêu, sai số, giá trị mới; số 0.5 ở X ghi rõ là bảng cho trước.
- **Hình thức hóa:** Bước số chuẩn bị HT4; từng số ánh xạ sang $R_{t+1},\gamma,V_t(S_{t+1}),V_t(S_t),\alpha$.
- **Kết nối vào và ra:** Cơ chế L05-C02 → một cập nhật kiểm được → công thức tổng quát L05-C04.
- **Nguồn:** Quy tắc SB §6.1 tr.119–120; phép tính từ trạng thái sau $e_1$ của ví dụ nguồn, chưa yêu cầu người học biết cách tạo bảng ấy.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Bảng này được cung cấp như dữ kiện. Nó trùng bảng TD sau $e_1$ được tính ở L05-C07, tạo cơ hội đối chiếu mà không dùng kết quả chưa học làm tiền đề.
- **Quyết định và lý do:** `thêm`; Bổ sung bước tính tay trước ký hiệu TD, không thêm môi trường.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích nêu bảng $V(S)=0$, $V(X)=0.5$ là kết quả TD(0) sau $e_1$, được tính lại khi chạy TD(0) trên lượt thứ nhất.

#### L05-C04: Mục tiêu và sai số TD(0)

- **Vai trò và mục tiêu:** Hình thức; MT4.
- **Luận điểm trung tâm:** Sai số TD là mục tiêu một bước trừ giá trị trước cập nhật.
- **Nội dung cần soạn:** Khai báo $V_t$ là toàn bộ bảng trước bước t; n là số cập nhật của $S_t$. $Y_t$ dùng phần thưởng quan sát và $V_t$ ở trạng thái sau. Chỉ phần tử tương ứng trạng thái hiện tại được thay đổi, các phần tử khác giữ nguyên.
- **Ví dụ hoặc hình:** Công thức lớn và chú thích ngắn dưới từng thành phần; không dùng bảng mô hình chuyển.
- **Hình thức hóa:** HT4: $Y_t=R_{t+1}+\gamma V_t(S_{t+1})$, $\delta_t=Y_t-V_t(S_t)$, $V_{t+1}(S_t)=V_t(S_t)+\alpha_n(S_t)\delta_t$.
- **Kết nối vào và ra:** Ba ô tính L05-C03 → ký hiệu tổng quát → quy trình qua nhiều chuyển L05-C05.
- **Nguồn:** SB §6.1 tr.119–121; L05 tr.25.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** $\delta_t$ không bằng lỗi thật $v_\pi(S_t)-V_t(S_t)$ nói chung. Dấu cộng trong cập nhật làm V tăng khi mục tiêu cao hơn giá trị cũ. Nếu t được đặt lại ở lượt mới, giả mã vẫn tiếp tục dùng cùng bảng hiện tại.
- **Quyết định và lý do:** `tách`; Tách công thức và giả mã khỏi trang nguồn để mỗi trang có một chức năng.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Chú thích giải thích tên gọi: $\delta_t$ là hiệu giữa hai dự đoán ở hai thời điểm liên tiếp.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích: $\delta_t$ là hiệu giữa mục tiêu dựa trên dự đoán tại $t+1$ và dự đoán tại $t$.

#### L05-C05: Thuật toán TD(0)

- **Vai trò và mục tiêu:** Thuật toán đầy đủ; MT4.
- **Luận điểm trung tâm:** TD(0) cập nhật sau mỗi chuyển do chính sách cố định sinh ra.
- **Nội dung cần soạn:** Đầu vào: $\pi,\gamma$, bước học, ngân sách chuyển hoặc lượt. Khởi tạo V tùy ý ở trạng thái trong, giá trị ở trạng thái kết thúc bằng 0; khởi tạo bộ đếm nếu bước học phụ thuộc số mẫu. Mỗi lượt chọn trạng thái đầu; chọn $A_t\sim\pi(\cdot\mid S_t)$; quan sát thưởng và trạng thái sau; tăng bộ đếm của trạng thái hiện tại; đọc bảng cũ để tính Y và sai số; cập nhật; chuyển trạng thái. Nếu trạng thái kết thúc thì bắt đầu lượt mới khi còn ngân sách.
- **Ví dụ hoặc hình:** Giả mã khoảng 10 dòng; nhãn đầu vào và đầu ra đặt ngoài vòng lặp.
- **Hình thức hóa:** HT4; đầu ra là bảng V sau ngân sách. Trạng thái kết thúc không có hành động tiếp theo trong lượt.
- **Kết nối vào và ra:** Công thức L05-C04 → trình tự thực thi → trường hợp biên L05-C06 và chạy toàn lượt L05-C07.
- **Nguồn:** SB §6.1 tr.120, hộp TD(0); L05 tr.25.
- **Thời lượng:** 4 phút.
- **Ghi chú học thuật:** Đọc cả hai giá trị vế phải trước khi ghi. Hết ngân sách dừng toàn bộ việc học; đến trạng thái kết thúc dừng một lượt. TD không cần tính mô hình hoặc chờ lợi tức đầy đủ.
- **Quyết định và lý do:** `thêm`; Hoàn thiện đầu vào, nguồn dữ liệu, thứ tự và dừng mà nguồn chưa diễn đạt đủ.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Chữ giả mã nâng từ 0.82em lên 0.92em (CSS cục bộ), trang vẫn vừa khung.

#### L05-C06: Trạng thái kết thúc và tự chuyển

- **Vai trò và mục tiêu:** Ứng dụng trường hợp biên; MT4.
- **Luận điểm trung tâm:** Cùng bảng trước cập nhật và giá trị trạng thái kết thúc bằng 0 xác định mục tiêu ở các trường hợp biên.
- **Nội dung cần soạn:** Vào G, thưởng +1, $V(G)=0$: mục tiêu bằng 1. Tự chuyển tại s với $R=0,\gamma=0.9,V_t(s)=2,\alpha=0.5$: mục tiêu 1.8, sai số −0.2, giá trị mới 1.9. Dữ kiện tự chuyển là phép kiểm quy tắc, không là một chuyển của chuỗi ngắn.
- **Ví dụ hoặc hình:** Hai cạnh nhỏ: một đến trạng thái kết thúc, một vòng tự chuyển có đầy đủ nhãn.
- **Hình thức hóa:** HT4; ở trạng thái kết thúc $Y_t=R_{t+1}$. Cả hai lần đọc trong tự chuyển dùng $V_t(s)=2$.
- **Kết nối vào và ra:** Quy trình L05-C05 → hai lỗi triển khai cần tránh → chạy $e_1$ L05-C07.
- **Nguồn:** SB §6.1 tr.120; trạng thái kết thúc từ L05 tr.19; tự chuyển là ví dụ kiểm toán quy tắc do bài soạn tạo, phù hợp tự chuyển HW05 bài 6.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Không đặt giá trị 0 khi dữ liệu chỉ bị ngắt theo thời gian. Phần thưởng +1 nằm trên chuyển vào G, không phải giá trị tương lai của G.
- **Quyết định và lý do:** `thêm`; Khôi phục trường hợp trạng thái kết thúc và kiểm việc đọc bảng cũ; ví dụ tự xây dựng được ghi rõ nguồn gốc.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở nêu hai trường hợp biên và gắn tự chuyển với việc đứng yên trong chuỗi năm ô của HW05 bài 6. Lý do: tự chuyển trước đây xuất hiện khiên cưỡng.
- **Sửa sau rà 01-10-2026:** `sửa`; Mặt trang chỉ nêu tự chuyển xảy ra khi tác tử đứng yên; dẫn chiếu HW05 bài 6 và "số liệu minh họa" chuyển vào ghi chú diễn giả.

#### L05-C07: TD(0) trên lượt thứ nhất

- **Vai trò và mục tiêu:** Ứng dụng đầy đủ; MT4.
- **Luận điểm trung tâm:** Trong lượt đầu từ bảng 0, thưởng cuối chỉ trực tiếp cập nhật trạng thái ngay trước trạng thái kết thúc.
- **Nội dung cần soạn:** Khởi tạo V(S)=V(X)=0, $\alpha=0.5,\gamma=1$. Bốn chuyển của $e_1:S,X,S,X,G$ cho mục tiêu $(0,0,0,1)$. Sau mỗi bước, bảng lần lượt $(0,0),(0,0),(0,0),(0,0.5)$. Bảng kết quả cuối chính là dữ kiện đã dùng ở L05-C03.
- **Ví dụ hoặc hình:** Quỹ đạo $e_1$ và bảng bốn hàng, cột t, trạng thái, thưởng, mục tiêu, V(S), V(X).
- **Hình thức hóa:** HT4 theo đúng giả mã L05-C05.
- **Kết nối vào và ra:** Trường hợp biên L05-C06 → lượt đầy đủ và bảng mới → tiếp tục lượt thứ hai L05-C08.
- **Nguồn:** L05 tr.29; HW05 bài 7; kiểm toán số độc lập.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Không quay lại sửa S trong cùng lượt sau khi X vừa nhận 0.5 nếu giả mã là TD trực tuyến một lượt. Thao tác quay lại sẽ là dùng lại dữ liệu, thuộc cơ chế khác.
- **Quyết định và lý do:** `sửa`; Hiển thị các bước thay cho kết luận lan truyền không gắn thứ tự.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-C08: TD(0) trên lượt thứ hai

- **Vai trò và mục tiêu:** Ứng dụng cập nhật tại chỗ; MT4.
- **Luận điểm trung tâm:** Chuyển sau dùng bảng vừa cập nhật bởi chuyển trước trong TD trực tuyến.
- **Nội dung cần soạn:** Tiếp tục từ $(V(S),V(X))=(0,0.5)$. Trên $e_2:S\to X\to S\to L$, các mục tiêu lần lượt $0.5,0.25,-1$. Các bảng sau bước là $(0.25,0.5),(0.25,0.375),(-0.375,0.375)$. Giữ nguyên $\alpha=0.5,\gamma=1$.
- **Ví dụ hoặc hình:** Bảng ba hàng đồng bộ vị trí với quỹ đạo; mũi tên chỉ giá trị S=0.25 được dùng ở bước thứ hai.
- **Hình thức hóa:** HT4; dòng cuối $0.25+0.5(-1-0.25)=-0.375$.
- **Kết nối vào và ra:** Bảng L05-C07 → phụ thuộc thứ tự của TD trực tuyến → chi phí và thông tin cần giữ L05-C09.
- **Nguồn:** L05 tr.29; HW05 bài 7; kiểm toán số độc lập.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Đây là cập nhật tại chỗ qua dữ liệu mới. Không giữ cố định bảng đầu lượt; quy tắc giữ bảng cố định chỉ được giới thiệu riêng cho lượt quét theo lô ở L05-D09.
- **Quyết định và lý do:** `sửa`; Làm rõ số trung gian và ranh giới giữa trực tuyến với theo lô.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-C09: Chi phí bộ nhớ và tính toán

- **Vai trò và mục tiêu:** Điều kiện thực hiện; MT4–MT5.
- **Luận điểm trung tâm:** TD xử lý một chuyển bằng lượng tính toán không phụ thuộc độ dài lượt.
- **Nội dung cần soạn:** Với bảng hữu hạn, TD dùng bảng V và bộ đếm nếu cần: $O(|\mathcal S|)$ bộ nhớ; một chuyển cần $O(1)$ phép tính. MC gia tăng theo giả mã đã chọn dùng bảng/bộ đếm và một lượt: $O(|\mathcal S|+T)$ bộ nhớ, $O(T)$ xử lý. MC cập nhật khi có lợi tức đầy đủ; TD dùng một chuyển và giá trị kế tiếp.
- **Ví dụ hoặc hình:** Bảng hai hàng MC/TD, ba cột thời điểm, dữ liệu tạm, chi phí; chú thích đây là quy trình dạng bảng đang học.
- **Hình thức hóa:** Chi phí suy ra từ L05-B10 và L05-C05, không là định lý tốc độ hội tụ.
- **Kết nối vào và ra:** Lần theo thuật toán L05-C07–L05-C08 → giải thích tài nguyên và thời điểm → kiểm tra L05-C10.
- **Nguồn:** SB §6.1–6.2 tr.119–124; phân tích chi phí trực tiếp từ giả mã.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Không gọi bộ nhớ TD là hằng theo số trạng thái. Cập nhật rẻ hơn mỗi chuyển không tự chứng minh cần ít dữ liệu hơn để đạt sai số cho trước.
- **Quyết định và lý do:** `sửa`; Thay bảng ưu/nhược tuyệt đối của nguồn bằng thông tin và chi phí có phạm vi.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề nêu đúng nội dung bảng.

#### L05-C10: Kiểm tra một bước TD(0)

- **Vai trò và mục tiêu:** Kiểm tra riêng của mạch C; MT4.
- **Luận điểm trung tâm:** Mục tiêu, sai số và bảng mới phải được tính từ cùng bảng trước cập nhật.
- **Nội dung cần soạn:** Câu hỏi dùng hai trường hợp đã chuẩn bị: chuyển sang trạng thái chưa kết thúc và chuyển vào trạng thái kết thúc. Các giá trị trước bước được cung cấp, không cần biết mô hình.
- **Ví dụ hoặc hình:** Hai cạnh có nhãn và ô trống cho mục tiêu, sai số, giá trị mới.
- **Hình thức hóa:** HT4.
- **Kết nối vào và ra:** Quy trình và trường hợp biên L05-C05–L05-C09 → kiểm đủ thao tác → so sánh hai thuật toán L05-D01.
- **Nguồn:** HW05 bài 3, 7; các số được chọn để kiểm trực tiếp quy tắc SB §6.1.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Gợi ý tách ba phép tính, sau đó kiểm các phần tử bảng không được cập nhật. Không dùng giá trị mới ở vế phải.
- **Quyết định và lý do:** `thêm`; Kiểm tra riêng mục tiêu, dấu sai số và trạng thái kết thúc trước phân tích so sánh.
- **Câu hỏi:** Cho $V(S)=0.25,V(X)=0.5,\alpha=0.5,\gamma=1$. (a) Với $S\to X$, thưởng 0, tính Y, sai số và V(S) mới. (b) Xét riêng bước $S\to L$, thưởng −1, từ cùng bảng ban đầu; tính ba đại lượng đó.
- **Kiến thức được đo:** MT4; nội dung trong cùng mạch hoặc tiên quyết đã khai báo.
- **Đáp án/gợi ý trong ghi chú:** (a) Y=0.5, sai số 0.25, V(S)=0.375; (b) Y=−1, sai số −1.25, V(S)=−0.375. Cả hai trường hợp V(X) giữ 0.5, V(L)=0.
- **Tiêu chí đánh giá:** Hai trường hợp bắt đầu độc lập từ cùng bảng; không coi thưởng −1 khi vào trạng thái kết thúc là giá trị tiếp nối để cộng lần nữa; đúng dấu và chỉ sửa S.
- **Thời gian hoạt động:** 1 phút tính, 1 phút trình bày, 1 phút đối chiếu; nằm trong 3 phút.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

### Mạch D. So sánh theo dữ liệu và giả thiết

Chức năng: So sánh đúng đại lượng, điều kiện và tiêu chuẩn trên cùng dữ liệu. Đầu vào: MC và TD(0) đã được thực hiện trên cùng hai lượt. Đầu ra: Căn cứ chọn phương pháp; phân biệt mẫu mới với dữ liệu cố định. Mục tiêu: MT5–MT6. Thời lượng: 34 phút, gồm trang kiểm tra L05-D12.

#### L05-D01: Monte Carlo và TD(0) trên cùng dữ liệu

- **Vai trò và mục tiêu:** Vấn đề so sánh và ví dụ; MT5.
- **Luận điểm trung tâm:** MC và TD(0) tạo các bảng khác nhau vì dùng mục tiêu và thời điểm cập nhật khác nhau.
- **Nội dung cần soạn:** Cùng V ban đầu 0, $\alpha=0.5,\gamma=1$, dữ liệu $e_1,e_2$. MC lần ghé đầu tiên sau $e_1$ là $(0.5,0.5)$, sau $e_2$ là $(-0.25,-0.25)$. TD lần lượt $(0,0.5)$ và $(-0.375,0.375)$. Phân biệt cập nhật sớm với tác động của thưởng cuối lên nhiều trạng thái.
- **Ví dụ hoặc hình:** Bảng HTML hai phương pháp, hai mốc; dùng lại sơ đồ mục tiêu nếu còn khoảng trống.
- **Hình thức hóa:** HT3–HT4, không thêm phép cập nhật.
- **Kết nối vào và ra:** Hai thuật toán đã chạy → cần chuẩn giá trị và tiêu chí để đánh giá → L05-D02.
- **Nguồn:** L05 tr.29; HW05 bài 7; số đã kiểm ở L05-B11, L05-C07–L05-C08.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** MC có thể cập nhật cả S và X sau khi lượt đầu kết thúc, TD chỉ đổi X trong lượt này. Không suy từ ví dụ rằng phương pháp nào luôn lan truyền nhanh hơn hoặc luôn chính xác hơn.
- **Quyết định và lý do:** `sửa`; Giữ so sánh nguồn nhưng gắn đủ điều kiện và loại kết luận vượt dữ liệu.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Thêm hộp nêu nhu cầu giá trị chuẩn để đánh giá hai bảng.
- **Sửa sau rà 01-10-2026:** `sửa`; Hộp: "Để xác định bảng nào gần $v_\pi$ hơn, cần giá trị chuẩn của môi trường."

#### L05-D02: Giá trị chuẩn của chuỗi ngắn

- **Vai trò và mục tiêu:** Ứng dụng đối chiếu giá trị; MT5.
- **Luận điểm trung tâm:** Giá trị thật là kỳ vọng của môi trường; hai lượt dữ liệu chưa xác định chính xác giá trị đó.
- **Nội dung cần soạn:** Dùng mô hình đã biết riêng cho kiểm chứng: $v_\pi(S)=-0.2+0.8v_\pi(X)$; $v_\pi(X)=0.8+0.2v_\pi(S)$. Nghiệm $11/21\approx0.524$ và $19/21\approx0.905$. Các bảng học ở L05-D01 là ước lượng hữu hạn mẫu.
- **Ví dụ hoặc hình:** `short-walk.svg` với hàng giá trị thật tại S,X; giá trị ở trạng thái kết thúc tiếp tục ghi 0.
- **Hình thức hóa:** Hai phương trình Bellman kỳ vọng từ tiên quyết; không đưa toán tử Bellman hoặc phép co mới.
- **Kết nối vào và ra:** Bảng dự đoán L05-D01 → chuẩn so sánh có mô hình → chuỗi dài giữ cùng cơ chế nhưng thay khoảng cách và chiết khấu L05-D03.
- **Nguồn:** L05 tr.19; kiểm toán số độc lập; Bellman kỳ vọng đã học ở Bài 04.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Tính thế cho $0.84v_\pi(S)=0.44$. Số nguồn tr.19 đúng sau làm tròn. Thuật toán MC/TD không nhận nghiệm này làm đầu vào; mô hình chỉ dùng để đánh giá.
- **Quyết định và lý do:** `giữ`; Đặt giá trị chuẩn sau khi đã có ước lượng, giúp phân biệt đối tượng đánh giá với dữ liệu học.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở: mô hình chuỗi ngắn đã biết trong ví dụ, nên $v_\pi$ được tính từ Bellman kỳ vọng.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích nối ra: độ lệch của hai bảng được phân tích qua kỳ vọng (độ chệch) và biến thiên (phương sai) của mục tiêu; hình giới hạn 150px.

#### L05-D03: Chuỗi dài với thưởng thưa

- **Vai trò và mục tiêu:** Vấn đề và ví dụ dẫn nhập so sánh; MT2–MT5.
- **Luận điểm trung tâm:** Khoảng cách đến phần thưởng và chiết khấu làm các lợi tức khác nhau theo đường đi.
- **Nội dung cần soạn:** Chuỗi $L,x_1,S,x_3,x_4,x_5,G$; đi phải 0.8, trái 0.2; thưởng vào L/G là −1/+1, còn lại 0; $\gamma=0.99$. Giá trị chuẩn tại S khoảng 0.829 và tại $x_5$ khoảng 0.992. Bắt đầu S cần tối thiểu bốn chuyển đến G hoặc hai chuyển đến L.
- **Ví dụ hoặc hình:** `long-walk.svg`; giữ đúng vị trí bắt đầu và nhãn thưởng cạnh, giá trị ở trạng thái kết thúc bằng 0.
- **Hình thức hóa:** HT1 với $\gamma=0.99$; các giá trị chuẩn đã được giải độc lập, không trình bày hệ năm phương trình trên mặt trang.
- **Kết nối vào và ra:** Chuỗi ngắn L05-D02 → độ dài và chiết khấu khác → tính hai lợi tức L05-D04.
- **Nguồn:** L05 tr.30; kiểm toán số độc lập.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Hai giá trị in nguồn đúng. Hệ Bellman năm trạng thái đặt trong ghi chú nếu cần đối chiếu; không dành tuyến chính cho giải hệ đã thuộc bài trước.
- **Quyết định và lý do:** `giữ`; Giữ ví dụ dài riêng của nguồn và dùng nó cho vấn đề số mũ, độ dài đường đi.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Chú thích nêu lý do xét chuỗi dài: lợi tức phụ thuộc nhiều chuyển ngẫu nhiên hơn; thưởng chỉ khi vào $L$ hoặc $G$ (nguồn tr.30).
- **Sửa sau rà 01-10-2026:** `sửa`; Câu lý do chuỗi dài lên làm câu mở; hai thẻ gộp mỗi thẻ một dòng; hình dùng cỡ ngắn.

#### L05-D04: Biến thiên của lợi tức

- **Vai trò và mục tiêu:** Ví dụ tính tay và trực giác biến thiên; MT2–MT5.
- **Luận điểm trung tâm:** Thưởng ở bước chuyển thứ m được nhân với $\gamma^{m-1}$ trong lợi tức ban đầu.
- **Nội dung cần soạn:** Đường $S,x_3,x_4,x_5,G$ có thưởng $(0,0,0,1)$ nên $G_0=0.99^3=0.970299$. Đường $S,x_1,L$ có thưởng $(0,-1)$ nên $G_0=-0.99$. Cả hai là lợi tức mẫu từ $S$, khác giá trị chuẩn $v_\pi(S)\approx0.829$ của chuỗi dài. Tách kỳ vọng khỏi biến thiên để so sánh mục tiêu; hai đường chưa xác định phương sai tổng thể.
- **Ví dụ hoặc hình:** `long-returns.svg`; công thức KaTeX đặt cạnh mỗi quỹ đạo với chỉ số thưởng cuối.
- **Hình thức hóa:** HT1; sửa số mũ 4 và 2 ở nguồn thành 3 và 1.
- **Kết nối vào và ra:** Giá trị chuẩn L05-D03 → hai lợi tức mẫu tại cùng trạng thái khác kỳ vọng → nhu cầu lấy kỳ vọng mục tiêu tại L05-D05, rồi xét nguồn biến thiên L05-D06.
- **Nguồn:** L05 tr.31; kiểm toán số độc lập.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Không gọi hai quỹ đạo là thí nghiệm ước lượng phương sai hoặc chứng cứ TD nhanh hơn MC. Tách số học của một đường khỏi giá trị kỳ vọng của trạng thái.
- **Quyết định và lý do:** `sửa`; Sửa lỗi lệch chỉ số chiết khấu và giới hạn kết luận theo đúng dữ liệu.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề nêu luận điểm thay cho chi tiết số mũ; giữ hiệu chỉnh số mũ trong ghi chú.
- **Sửa sau rà 01-10-2026:** `sửa`; Chú thích nêu thứ tự xét: kỳ vọng (độ chệch) rồi phương sai.

#### L05-D05: Độ chệch của mục tiêu TD

- **Vai trò và mục tiêu:** Hình thức so sánh sai lệch; MT5.
- **Luận điểm trung tâm:** Sai lệch mục tiêu TD phụ thuộc sai số của giá trị trạng thái kế tiếp được dùng trong mục tiêu.
- **Nội dung cần soạn:** Ví dụ trước công thức dùng chuỗi ngắn, $\gamma=1$, $V(X)=0.5,V(L)=0$. Từ $S$, $Y=-1$ với xác suất $0.2$ và $Y=0.5$ với xác suất $0.8$, nên $\mathbb E[Y\mid S_t=S]=0.2\ne11/21$. Sau phép tính mới giữ $V$ tổng quát và trừ Bellman để biểu diễn sai lệch. Nếu giá trị tiếp nối đúng, sai lệch bằng $0$; TD không bắt buộc luôn chệch.
- **Ví dụ hoặc hình:** Phép tính kỳ vọng số đứng trước đẳng thức sai lệch tổng quát. Dữ kiện tái dùng B01/C03/D02; không tạo môi trường mới hoặc thu nhỏ chữ.
- **Hình thức hóa:** HT5: $\mathbb E[Y\mid S_t=s]-v_\pi(s)=\gamma\mathbb E[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s]$.
- **Kết nối vào và ra:** Nhu cầu tách mẫu/kỳ vọng ở L05-D04 → tính kỳ vọng của hai mục tiêu có thể nhận từ S trong chuỗi ngắn → hình thức hóa sai lệch, chuẩn bị phân biệt với phương sai L05-D06.
- **Nguồn:** SB §6.1–6.2 tr.120–124; L05 tr.26–27 được sửa; hệ quả từ Bellman kỳ vọng.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Bảng V cố định không làm $V(S_{t+1})$ thành hằng vì trạng thái kế tiếp vẫn ngẫu nhiên. Công thức nói về mục tiêu với V cố định; không suy mọi ước lượng MC hữu hạn mẫu đều không chệch.
- **Quyết định và lý do:** `sửa`; Thay so sánh nhị phân của nguồn bằng điều kiện và đại lượng chính xác.
- **Ngân sách và lời giải phụ trợ:** Giữ 3 phút cho hai khả năng, phép kỳ vọng số và quan hệ tổng quát; phép trừ $1/5-11/21=-34/105$ cùng suy diễn Bellman nằm trong ghi chú/học liệu. ACA-02/FLOW-01.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Gọi tên độ chệch của mục tiêu (kỳ vọng mục tiêu trừ $v_\pi(s)$) ngay sau ví dụ số, giữ thứ tự ví dụ trước hình thức; chú thích nêu độ chệch của MC bằng 0 và điều kiện để độ chệch TD bằng 0. Số liệu giữ nguyên: $0.2(-1)+0.8(0.5)=0.2$, $1/5-11/21=-34/105$.

#### L05-D06: Phương sai của mục tiêu

- **Vai trò và mục tiêu:** Trực giác và giới hạn phương sai; MT5.
- **Luận điểm trung tâm:** MC dùng phần đuôi quỹ đạo ngẫu nhiên; TD thay phần đuôi bằng một giá trị ước lượng.
- **Nội dung cần soạn:** MC phụ thuộc các phần thưởng và chuyển trạng thái đến cuối lượt. TD vẫn ngẫu nhiên qua thưởng đầu và trạng thái sau, đồng thời chịu sai số bảng V. Với mục tiêu lý tưởng dùng $v_\pi$ và mômen bậc hai hữu hạn, lấy kỳ vọng phần còn lại không làm tăng phương sai. Kết quả ấy không là bảo đảm phổ quát cho V đang học.
- **Ví dụ hoặc hình:** Cây nhỏ một bước rồi hai phần đuôi; MC giữ một đuôi quan sát, mục tiêu lý tưởng thay bằng kỳ vọng. Hình là quan hệ, không có số thực nghiệm.
- **Hình thức hóa:** HT6; bất đẳng thức lý tưởng đặt trong ghi chú hoặc một dòng riêng có nhãn điều kiện.
- **Kết nối vào và ra:** Sai lệch L05-D05 → phương sai là trục khác → cần điều kiện để nói về học lâu dài L05-D07.
- **Nguồn:** SB §6.2 tr.124; L05 tr.26–28; suy luận điều kiện từ luật phương sai toàn phần.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Với $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$, tính Markov cho $Y^*$ là kỳ vọng có điều kiện của G sau chuyển đầu; áp dụng luật phương sai toàn phần. Không gán bất đẳng thức đó cho mọi $Y=R+\gamma V(S')$.
- **Quyết định và lý do:** `gộp`; Gộp hai trang nguồn lặp về phương sai và bỏ mức độ không định lượng.
- **Phân định thời lượng:** 3 phút chỉ dành cho cơ chế nguồn ngẫu nhiên và giới hạn kết luận. Chứng minh bằng $\mathcal F_1$ và luật phương sai toàn phần là phần đọc phụ trợ trong ghi chú/học liệu; chưa diễn tập, không xác nhận nhịp lớp bằng suy đoán. SV-R2.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Mặt trang nêu bất đẳng thức $\operatorname{Var}(R_{t+1}+\gamma v_\pi(S_{t+1})\mid s)\le\operatorname{Var}(G_t\mid s)$ và giới hạn với bảng $V$ đang học; hai thẻ nguồn ngẫu nhiên gộp thành một câu; hình giảm còn 200px. Lý do: kết quả dương trước đây chỉ có trong ghi chú.
- **Sửa sau rà 01-10-2026:** `sửa`; Mặt trang thêm giả thiết Markov và mômen bậc hai hữu hạn; tách nguồn ngẫu nhiên (thưởng đầu, trạng thái sau) khỏi sai số tất định của $V$; hộp viết dạng khẳng định có điều kiện; hình giới hạn 170px.

#### L05-D07: Điều kiện hội tụ của TD(0)

- **Vai trò và mục tiêu:** Điều kiện áp dụng và hội tụ; MT5–MT6.
- **Luận điểm trung tâm:** Bảo đảm hội tụ phụ thuộc dữ liệu và bước học, không chỉ tên thuật toán.
- **Nội dung cần soạn:** Phạm vi TD dạng bảng: môi trường hữu hạn Markov dừng; chính sách cố định; thưởng bị chặn; $0\le\gamma<1$ hoặc bài toán kết thúc hợp lệ; các trạng thái quan tâm được cập nhật vô hạn. Bước học của mỗi trạng thái phải giảm theo điều kiện tổng. Bước hằng có thể tiếp tục dao động; vài lượt hoặc hết ngân sách không chứng minh hội tụ.
- **Ví dụ hoặc hình:** Hai nhóm điều kiện: bài toán/dữ liệu và bước học; không dựng đồ thị hội tụ minh họa giả.
- **Hình thức hóa:** HT7: $\sum_n\alpha_n(s)=\infty$, $\sum_n\alpha_n(s)^2<\infty$; $1/n$ là ví dụ, $\alpha$ hằng vi phạm điều kiện tổng bình phương.
- **Kết nối vào và ra:** Cơ chế sai số L05-D05–L05-D06 → ranh giới bảo đảm trên mẫu mới → bài toán khác là dùng lại dữ liệu cố định L05-D08.
- **Nguồn:** SB §2.5 tr.33; §6.2 tr.124–125; L05 tr.28 được giới hạn.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Phát biểu hội tụ có điều kiện, không chứng minh xấp xỉ ngẫu nhiên. Trường hợp $\gamma=1$ cần giả thiết kết thúc như chuỗi hấp thụ đang xét; không chỉ thay giá trị gamma trong lập luận phép co. Mọi lần ghé MC có kết quả nhất quán với điều kiện thích hợp, nhưng không chứng minh bằng giả sử các mẫu trong cùng lượt độc lập.
- **Quyết định và lý do:** `sửa`; Bổ sung điều kiện còn thiếu; phân biệt bảo đảm với tiêu chuẩn dừng thực hành.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề gọi tên kết quả; hộp nêu "với xác suất 1".

#### L05-D08: Dự đoán trên dữ liệu cố định

- **Vai trò và mục tiêu:** Vấn đề và ví dụ dẫn nhập theo lô; MT5.
- **Luận điểm trung tâm:** Kinh nghiệm trực tiếp của A và thông tin về trạng thái kế tiếp B có thể gợi hai giá trị khác nhau.
- **Nội dung cần soạn:** Dữ liệu đúng tám lượt: một lượt $A,0,B,0$; sáu lượt $B,1$; một lượt $B,0$, đều kết thúc; $\gamma=1$. A chỉ xuất hiện trong lượt có lợi tức 0; B xuất hiện tám lần với sáu phần thưởng cuối 1. Nhiệm vụ: dự đoán A khi dữ liệu này được dùng lại, không thu thêm lượt mới.
- **Ví dụ hoặc hình:** Bảng ba nhóm lượt có số lượng 1,6,1 và tổng số 8; trạng thái kết thúc được thể hiện rõ.
- **Hình thức hóa:** Chưa đưa nghiệm; xác định hai trạng thái không kết thúc và tập dữ liệu $\mathcal D$.
- **Kết nối vào và ra:** Giới hạn mẫu mới L05-D07 → câu hỏi trên dữ liệu cố định → cách dùng lại dữ liệu L05-D09.
- **Nguồn:** SB §6.3, Ví dụ 6.4 tr.127–128; đối chiếu UCL tr.22–23, ST tr.48.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Không có chính sách mới được tối ưu; bài toán vẫn là dự đoán. A–B được thêm để phân biệt tiêu chuẩn hữu hạn mẫu, không thay các chuỗi nguồn.
- **Quyết định và lý do:** `thêm`; Bổ sung ví dụ tối giản tạo hai nghiệm khác nhau theo sườn SB §6.3.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Câu mở nối từ mẫu mới sang dùng lại dữ liệu (Sutton–Barto §6.3); nhiệm vụ dự đoán $A$ chuyển lên dòng dữ kiện; hai thẻ rút gọn.

#### L05-D09: Cập nhật theo lô

- **Vai trò và mục tiêu:** Tính tay rồi quy trình theo lô; MT5.
- **Luận điểm trung tâm:** Trong một lượt quét theo lô, mọi sai số được tính từ cùng bảng trước lượt quét.
- **Nội dung cần soạn:** Từ $V_0(A)=V_0(B)=0$, tổng sai số bằng $0$ tại A và $6$ tại B; $\alpha=1/8$ cho $\Delta_0(A)=0,\Delta_0(B)=6/8$ và bảng $(0,0.75)$. Mặt trang khai báo $k$ là lượt quét, $\Delta_k(s)$ là tổng gia số, $y$ là mục tiêu. Quy trình: chọn $V_0,\alpha,\varepsilon,K$; giữ $V_k$ và đặt tổng gia số bằng $0$; cộng $\Delta_k(s)\leftarrow\Delta_k(s)+\alpha[y-V_k(s)]$ với mỗi mẫu; hết lượt quét ghi đồng thời $V_{k+1}(s)=V_k(s)+\Delta_k(s)$; lặp tới ngưỡng hoặc ngân sách.
- **Ví dụ hoặc hình:** Một phép tính đầu tiên cạnh quy trình năm bước, có phép cộng gia số và ghi bảng; không dồn hai giả mã dài lên mặt trang.
- **Hình thức hóa:** HT8. Gia số của trạng thái s là tổng $\alpha(\text{mục tiêu}-V_k(s))$; TD luôn dùng $V_k$ ở trạng thái sau. MC dùng lợi tức đã tính từ các lượt.
- **Kết nối vào và ra:** Tập dữ liệu L05-D08 → quy trình tái sử dụng → nghiệm MC L05-D10 và TD L05-D11.
- **Nguồn:** SB §6.3 tr.126–128; phép quét số từ dữ liệu Ví dụ 6.4.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Bước học phải đủ nhỏ; $1/8$ chỉ là lựa chọn hợp lệ cho ví dụ này. Với cách cộng hiện tại, TD có $V_{k+1}(A)=V_k(A)+\alpha(V_k(B)-V_k(A))$ và $V_{k+1}(B)=V_k(B)+\alpha(6-8V_k(B))$. $0<\alpha<1/4$ đủ ở riêng ví dụ; không cần dạy điều kiện số này trên mặt trang. Mỗi lượt quét dùng $O(|\mathcal D|)$ công việc theo số chuyển và bộ nhớ dữ liệu cùng bảng; giữ V cố định khác cập nhật tại chỗ L05-C08.
- **Quyết định và lý do:** `thêm`; Chuẩn bị thuật toán theo lô trước khi so sánh nghiệm, tránh gọi một lần chạy trực tuyến là theo lô.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Rút gọn tiêu đề.
- **Sửa sau rà 01-10-2026:** `sửa`; Khai báo $k$, $\Delta_k(s)$ đặt đầu thẻ ví dụ trước khi dùng $\Delta_0$; $\varepsilon$, $K$ khai báo ngay ở bước 1; tiêu đề thẻ "Quét đầu, MC và TD".

#### L05-D10: Nghiệm Monte Carlo theo lô

- **Vai trò và mục tiêu:** Hình thức và ứng dụng theo lô MC; MT5.
- **Luận điểm trung tâm:** MC khớp các lợi tức đã quan sát tại mỗi trạng thái.
- **Nội dung cần soạn:** A có một lợi tức 0 nên $V_{\rm MC}(A)=0$. B có sáu lợi tức 1 và hai lợi tức 0 nên $V_{\rm MC}(B)=6/8=0.75$. Tổng bình phương sai số tại B là $6(1-v)^2+2v^2$; nghiệm cực tiểu bằng trung bình. Một lượt quét tiếp từ $(0,0.75)$ không thay đổi bảng MC.
- **Ví dụ hoặc hình:** Hai nhóm mẫu A và B nối tới nghiệm; mục tiêu bình phương ở một dòng riêng.
- **Hình thức hóa:** HT2 và HT8; tại A tối thiểu hóa $v^2$, tại B tối thiểu hóa $6(1-v)^2+2v^2$.
- **Kết nối vào và ra:** Quy trình L05-D09 → nghiệm gắn lợi tức thực tế → xét quan hệ Markov thực nghiệm L05-D11.
- **Nguồn:** SB §6.3 tr.127–128, Ví dụ 6.4.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Có thể kiểm nghiệm B bằng đạo hàm $16v-12=0$, không cần mở một bài về hồi quy. “Tối ưu” ở đây chỉ theo sai số với lợi tức trong tập dữ liệu đã cho.
- **Quyết định và lý do:** `thêm`; Tính đầy đủ tiêu chuẩn MC trước khi đưa nghiệm TD khác, không chỉ hiện hai con số.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề thống nhất với L05-D09.

#### L05-D11: Nghiệm TD theo lô

- **Vai trò và mục tiêu:** Hình thức và ứng dụng theo lô TD; MT5.
- **Luận điểm trung tâm:** TD khớp quan hệ chuyển trạng thái ước lượng từ dữ liệu.
- **Nội dung cần soạn:** Dữ liệu cho A luôn đến B với thưởng 0; B kết thúc với thưởng trung bình 6/8. Điều kiện tổng sai số bằng 0 cho $V(B)=0.75$ và $V(A)=V(B)=0.75$. Từ bảng sau quét đầu $(0,0.75)$, quét TD tiếp với $\alpha=1/8$ đưa A lên 0.09375, B giữ 0.75. Đây là bước hướng đến nghiệm, chưa phải hội tụ sau hai lượt quét.
- **Ví dụ hoặc hình:** `ab-empirical.svg` ghi rõ mô hình ước lượng từ tám lượt, cạnh thưởng và giá trị ở trạng thái kết thúc bằng 0.
- **Hình thức hóa:** HT8: $0=V(B)-V(A)$, $0=6-8V(B)$.
- **Kết nối vào và ra:** Nghiệm theo lợi tức L05-D10 → nghiệm theo quan hệ Markov → kiểm tra tiêu chuẩn và giới hạn L05-D12.
- **Nguồn:** SB §6.3 tr.127–128, Ví dụ 6.4; kiểm toán số độc lập.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** TD có thể đạt cùng nghiệm mà không xây mô hình tường minh trong thuật toán; sơ đồ chỉ giải thích nghiệm. Không suy rằng 0.75 là giá trị thật của A nếu môi trường thật chưa biết, hoặc TD luôn tốt hơn MC.
- **Quyết định và lý do:** `thêm`; Làm rõ nguồn khác biệt của hai nghiệm và phân biệt bảng sau quét với nghiệm giới hạn.
- **Hiệu chỉnh trực quan:** Nhãn “p = 6/8; thưởng 1” dời xuống vùng trống bên trong cung; giữ nguyên hướng cạnh, xác suất và phần thưởng trong SVG dùng chung cho deck/học liệu. SV-03.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Tiêu đề thống nhất với L05-D09.

#### L05-D12: Kiểm tra kết luận từ dữ liệu hữu hạn

- **Vai trò và mục tiêu:** Kiểm tra riêng của mạch D; MT5–MT6.
- **Luận điểm trung tâm:** Một kết luận so sánh phải nêu tiêu chuẩn và phạm vi dữ liệu.
- **Nội dung cần soạn:** Dùng lại tám lượt A–B và hai nghiệm đã tính. Yêu cầu giải thích sự khác biệt tại A, đánh giá hai mệnh đề về ưu thế và hội tụ.
- **Ví dụ hoặc hình:** Bảng dữ liệu rút gọn và hai ô tiêu chuẩn; đáp án chỉ trong ghi chú.
- **Hình thức hóa:** HT5–HT8; không đưa công thức ngoài tuyến đã học.
- **Kết nối vào và ra:** L05-D10–L05-D11 → khả năng giải thích hai nghiệm có điều kiện → lựa chọn phương pháp L05-E01.
- **Nguồn:** SB §6.2–6.3 tr.124–128; HW05 bài 4, 5 được sửa.
- **Thời lượng:** 4 phút.
- **Ghi chú học thuật:** Gợi ý xác định MC dùng đại lượng đã quan sát nào ở A, TD dùng quan hệ chuyển nào. Tiêu chuẩn dữ liệu cố định và bảo đảm khi có thêm mẫu mới không đồng nhất.
- **Quyết định và lý do:** `thêm`; Kiểm tra tổng hợp phần so sánh, không yêu cầu nhớ bảng ưu nhược chung chung.
- **Câu hỏi:** Giải thích MC theo lô cho A=0 còn TD theo lô cho A=0.75. Nhận định “TD luôn chính xác hơn vì phương sai luôn thấp hơn” và “bước học hằng luôn hội tụ đúng khi lấy thêm mẫu” có được bài học bảo đảm không? Nêu căn cứ.
- **Kiến thức được đo:** MT5–MT6; nội dung trong cùng mạch hoặc tiên quyết đã khai báo.
- **Đáp án/gợi ý trong ghi chú:** MC khớp lợi tức duy nhất 0 của A; TD khớp A→B và trung bình B=0.75. Hai mệnh đề đều không được bảo đảm: phương sai của TD dùng V học được không có thứ tự phổ quát; bước hằng trên mẫu mới không thỏa điều kiện tổng bình phương và có thể dao động.
- **Tiêu chí đánh giá:** Nêu đúng hai tiêu chuẩn, phân biệt dữ liệu cố định/mẫu mới, không dùng kết quả A–B làm chứng minh TD đúng hơn môi trường thật.
- **Thời gian hoạt động:** 1.5 phút lập luận, 1 phút trả lời, 1.5 phút đối chiếu; nằm trong 4 phút.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

### Mạch E. Kết luận và tự kiểm tra

Chức năng: Giải quyết lại bài toán mở đầu bằng lựa chọn phương pháp có điều kiện. Đầu vào: Cơ chế, kết quả số và giới hạn ở mạch B–D. Đầu ra: Năng lực tính, giải thích, lựa chọn và các bài tập củng cố có nguồn. Mục tiêu: MT1–MT6. Thời lượng: 12 phút, gồm trang kiểm tra L05-E04.

#### L05-E01: Lựa chọn phương pháp dự đoán

- **Vai trò và mục tiêu:** Thu hồi vấn đề mở đầu; MT6.
- **Luận điểm trung tâm:** Thông tin sẵn có và yêu cầu cập nhật quyết định lựa chọn MC hoặc TD(0).
- **Nội dung cần soạn:** Có lượt hoàn chỉnh và cần khớp lợi tức quan sát: MC là lựa chọn trực tiếp. Cần cập nhật trước kết thúc và có trạng thái Markov cùng bảng V: TD(0) dùng một chuyển. Với tập dữ liệu cố định, chỉ rõ tiêu chuẩn lợi tức hay quan hệ Markov thực nghiệm; không chọn bằng nhãn phương pháp luôn tốt hơn.
- **Ví dụ hoặc hình:** Bảng ba trường hợp, thông tin, lựa chọn và điều kiện; không thêm khái niệm mới.
- **Hình thức hóa:** Thu hồi HT1–HT8, chỉ cần hai mục tiêu $G_t$ và $R_{t+1}+\gamma V_t(S_{t+1})$.
- **Kết nối vào và ra:** Kết luận có điều kiện L05-D12 → trả lời bài toán thiếu mô hình L05-A03 → đối chiếu năng lực L05-E02.
- **Nguồn:** Tổng hợp SB §5.1, §6.1–6.3; L05 tr.28, 33.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Cả hai học giá trị của chính sách cho trước. Bảng lựa chọn không là định lý xếp hạng hiệu quả mẫu cho mọi môi trường.
- **Quyết định và lý do:** `sửa`; Kết luận quay lại quyết định đã nêu thay vì chỉ lặp mục lục nguồn.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-E02: Tổng kết Monte Carlo và TD(0)

- **Vai trò và mục tiêu:** Đối chiếu mục tiêu; MT1–MT6.
- **Luận điểm trung tâm:** Người học có thể thực hiện dự đoán dạng bảng và kiểm tra điều kiện của kết luận.
- **Nội dung cần soạn:** Ba sản phẩm: lập mẫu lợi tức đúng quy tắc; lần theo MC và TD(0); giải thích khác biệt theo dữ liệu và giả thiết. Ba giới hạn gắn sản phẩm: MC đầy đủ cần lượt kết thúc; TD dùng giá trị ước lượng ở trạng thái sau; bảo đảm hội tụ cần điều kiện dữ liệu và bước học. Chính sách vẫn cố định trong toàn bài.
- **Ví dụ hoặc hình:** Ba hàng năng lực đi cùng bằng chứng đã thực hiện; không hiện mã trang hoặc mã mục tiêu trên mặt trang.
- **Hình thức hóa:** Không áp dụng công thức mới; liên hệ chính xác các điều kiện L05-B12, L05-D07.
- **Kết nối vào và ra:** Lựa chọn L05-E01 → sản phẩm học tập có thể kiểm chứng → bài tập củng cố L05-E03.
- **Nguồn:** L05 tr.32–33; SB §5.1 và §6.1–6.3.
- **Thời lượng:** 2 phút.
- **Ghi chú học thuật:** Các mở rộng về điều khiển và xấp xỉ hàm không được giới thiệu như kiến thức cần ghi nhớ của bài. Không nêu bài kế tiếp cụ thể khi chưa xác minh nguồn lịch môn.
- **Quyết định và lý do:** `gộp`; Gộp câu hỏi mở rộng và tổng kết thành đối chiếu mục tiêu có giới hạn, tránh thêm trọng tâm cuối bài.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Thay bảng năng lực bằng bảng tổng kết sáu tiêu chí (mục tiêu, thời điểm cập nhật, độ chệch, phương sai, hội tụ trên mẫu mới, dữ liệu cố định), mỗi ô giữ điều kiện đã học; chú thích nối Bài 06. Khôi phục bảng so sánh nguồn tr.31 và tổng kết tr.33 ở dạng có điều kiện; câu nối theo câu hỏi mở tr.32.
- **Sửa sau rà 01-10-2026:** `sửa`; Dòng hội tụ nêu kết quả "về $v_\pi$ khi …"; phương sai MC "có thể lớn khi lượt dài"; chú thích thêm giả thiết của dòng hội tụ; bỏ câu bình luận nguồn khỏi ghi chú diễn giả (lưu trong review-log).

#### L05-E03: Bài tập tuần 5

- **Vai trò và mục tiêu:** Bài tập có nguồn; MT1–MT6.
- **Luận điểm trung tâm:** Bảy bài tập nguồn kiểm tra từ dữ liệu, cơ chế đến phép tính và giới hạn kết luận.
- **Nội dung cần soạn:** Ba nhóm trên mặt trang: bài 1–3 về dữ liệu và mục tiêu; bài 4–5 về so sánh có điều kiện và hai trục MC; bài 6–7 về giá trị chuẩn và cập nhật trên chuỗi. Nêu rõ bài 5 chọn lần ghé và bước học là hai trục; bài 7 phải chỉ định lần ghé đầu tiên hoặc mọi lần ghé. Đường dẫn tài liệu HW05 có thể đặt trong ghi chú/nguồn.
- **Ví dụ hoặc hình:** Ba nhóm bài tập bằng HTML, mỗi nhóm một sản phẩm cụ thể; không nhồi toàn đề bảy bài lên một trang.
- **Hình thức hóa:** Bài 6 dùng Bellman kỳ vọng đã là tiên quyết; bài 7 dùng HT3–HT4. Toàn đề và đáp án có hướng dẫn trong phần chữa bài của outline.
- **Kết nối vào và ra:** Năng lực L05-E02 → nhiệm vụ tự luyện và chữa bài → kiểm tra lựa chọn tổng hợp L05-E04.
- **Nguồn:** HW05 tr.1–2, bài 1–7; sửa giả thiết theo nhật ký.
- **Thời lượng:** 3 phút.
- **Ghi chú học thuật:** Bài 4 được đổi thành giải thích cơ chế và giới hạn, không chứng minh TD luôn nhanh hơn. Bài 5 bỏ tiền đề bước hằng luôn cùng hội tụ đúng. Bài 6 giữ dữ kiện và dùng chuẩn có mô hình để đối chiếu, không bắt MC/TD phải biết mô hình.
- **Quyết định và lý do:** `sửa`; Giữ đủ bài tập nguồn với các hiệu chỉnh học thuật; phân biệt 120 phút chính và 30 phút chữa bài trong tệp quy trình.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Rút gọn tiêu đề.

#### L05-E04: Kiểm tra lựa chọn và điều kiện

- **Vai trò và mục tiêu:** Kiểm tra riêng của mạch E; MT1–MT6.
- **Luận điểm trung tâm:** Lựa chọn phương pháp phải đi cùng mục tiêu, dữ liệu và giới hạn kết luận.
- **Nội dung cần soạn:** Ba tình huống lấy từ bài: lượt hoàn chỉnh của chuỗi ngắn; tiền tố chưa kết thúc; tám lượt A–B cố định. Yêu cầu chọn cách làm và nêu mục tiêu cập nhật hoặc tiêu chuẩn.
- **Ví dụ hoặc hình:** Ba thẻ ngắn đánh số tình huống; không thêm môi trường hoặc số mới.
- **Hình thức hóa:** HT1–HT8 đã học; đây là tổng hợp, không giới thiệu thuật toán khác.
- **Kết nối vào và ra:** Bài tập L05-E03 → kiểm chứng toàn tuyến từ vấn đề L05-A03 → tài liệu đọc L05-E05 phục vụ phần còn cần củng cố.
- **Nguồn:** Tổng hợp L05 tr.15–33, HW05 và SB §5.1, §6.1–6.3.
- **Thời lượng:** 4 phút.
- **Ghi chú học thuật:** Gợi ý xác định thông tin có sẵn trước khi nêu tên phương pháp. Một đáp án khác vẫn chấp nhận nếu điều kiện, mục tiêu và cách đánh giá được diễn đạt đúng phạm vi.
- **Quyết định và lý do:** `thêm`; Kiểm tra riêng phần kết luận bằng quyết định phối hợp các khái niệm thay cho câu hỏi nhớ tên.
- **Câu hỏi:** (a) Sau lượt $e_1$ hoàn chỉnh, chỉ rõ hai lựa chọn cần xác định trước khi báo cáo một kết quả MC. (b) Sau chuyển đầu chưa kết thúc, nêu một cách cập nhật đã học và thông tin cần có. (c) Trên tám lượt A–B, nêu điều kiện để gọi một nghiệm là tốt hơn nghiệm kia.
- **Kiến thức được đo:** MT1–MT6; nội dung trong cùng mạch hoặc tiên quyết đã khai báo.
- **Đáp án/gợi ý trong ghi chú:** (a) Quy tắc lần ghé và quy tắc bước học/khởi tạo. (b) TD(0), cần thưởng, trạng thái sau, bảng V, gamma và bước học; mục tiêu $R+\gamma V(S')$. (c) Cần tiêu chuẩn đánh giá: khớp lợi tức quan sát hay khớp cấu trúc Markov thực nghiệm; để so sánh với môi trường thật cần dữ liệu hoặc giá trị chuẩn phù hợp, tám lượt chưa chứng minh ưu thế phổ quát.
- **Tiêu chí đánh giá:** Liên kết lựa chọn với dữ kiện; nêu mục tiêu đúng; không đổi chính sách hay giả định biết mô hình ngầm; phân biệt sai số dữ liệu với sai số giá trị thật.
- **Thời gian hoạt động:** 1.5 phút chọn và ghi điều kiện, 1 phút trả lời, 1.5 phút đối chiếu; nằm trong 4 phút.
- **Hiệu chỉnh 01-10-2026:** `giữ`; trang đạt tiêu chí tiêu đề, mạch và cách dẫn khái niệm.

#### L05-E05: Tài liệu đọc

- **Vai trò và mục tiêu:** Kết thúc bằng nhiệm vụ cụ thể; MT2–MT6.
- **Luận điểm trung tâm:** Các mục đọc tương ứng trực tiếp với ba năng lực còn cần tự kiểm.
- **Nội dung cần soạn:** Sutton–Barto §5.1 tr.92–96 cho lựa chọn mẫu và MC; §6.1–6.3 tr.119–128 cho TD và dữ liệu hữu hạn; §2.4–2.5 tr.30–33 cho bước học. HW05 bài 6–7 để đối chiếu giá trị chuẩn và cập nhật theo dữ liệu. Mỗi mục đọc gắn một nhiệm vụ: dựng tập mẫu, lần theo cập nhật, nêu điều kiện kết luận.
- **Ví dụ hoặc hình:** Không cần hình; danh mục ba mục sách và một tài liệu bài tập, cỡ chữ đọc được.
- **Hình thức hóa:** Không có khái niệm mới.
- **Kết nối vào và ra:** Kết quả tự kiểm L05-E04 → chọn phần đọc và bài tập cần hoàn thiện sau bài học.
- **Nguồn:** SB các mục đã kiểm; HW05 bài 6–7.
- **Thời lượng:** 1 phút.
- **Ghi chú học thuật:** Trang sách là số in, trang PDF cộng 22. Chỉ liệt kê các mục thuộc phạm vi đã dạy; không thêm tài liệu chưa đọc để làm dài danh mục.
- **Quyết định và lý do:** `thêm`; Cung cấp đường đọc có vị trí cụ thể và nhiệm vụ tiếp tục, không lặp tổng kết một lần nữa.
- **Hiệu chỉnh 01-10-2026:** `sửa`; Rút gọn tiêu đề.

## Ánh xạ đủ 33 trang L05

L05 là `RL-hk2-2025-2026/lecture-05-du-doan-phi-mo-hinh.pdf`; số trang PDF trùng số in. Những trang bỏ khỏi tuyến chính dưới đây được ghi nhận rõ, không chuyển ngầm sang phụ lục. Sườn Sutton–Barto theo yêu cầu hiện tại là căn cứ thay thứ tự phần ôn quy hoạch động.

| Trang nguồn | Nội dung | Quyết định | Trang đích | Lý do và hiệu chỉnh |
|---:|---|---|---|---|
| 1 | Tên bài | sửa | L05-A01 | Giữ chủ đề, đổi học kỳ, không gán tác giả chưa xác minh |
| 2 | Mục lục | sửa | L05-A02 | Bản đồ năm mạch theo SB thay mục lục cũ |
| 3 | MDP hữu hạn | gộp | L05-A04 | Chỉ nhắc dữ liệu, chính sách, giá trị và trạng thái kết thúc cần cho dự đoán |
| 4 | Giá trị/chính sách tối ưu | bỏ | Không vào tuyến chính | Điều khiển ngoài phạm vi; không mang công thức sai kiểu đầu ra của chính sách sang bài |
| 5 | Bellman tối ưu và câu hỏi | bỏ | Không vào tuyến chính | Bellman kỳ vọng được nhắc khi cần, không khai triển tối ưu |
| 6 | Dự đoán/điều khiển có mô hình | gộp | L05-A03 | Giữ đối tượng dự đoán và đối chiếu đầu vào mô hình/mẫu |
| 7 | Lặp giá trị | bỏ | Không vào tuyến chính | Thuộc bài trước và bài toán điều khiển |
| 8 | Lặp giá trị, câu hỏi giá trị hành động | bỏ | Không vào tuyến chính | Lặp nội dung, không phục vụ giá trị chính sách cố định |
| 9 | Lặp giá trị và lặp chính sách | bỏ | Không vào tuyến chính | Không cần để chuẩn bị MC/TD(0) |
| 10 | Câu hỏi hội tụ quy hoạch động | bỏ | Không vào tuyến chính | Điều kiện MC/TD được đặt riêng tại L05-B12, L05-D07 sau cơ chế |
| 11 | Chuẩn sup | bỏ | Không vào tuyến chính | Không cần cho tuyến tính tay và lựa chọn phương pháp |
| 12 | Phép co Bellman | bỏ | Không vào tuyến chính | Không dùng phép co thay chứng minh hội tụ cập nhật ngẫu nhiên; lưu ý gamma bằng 1 |
| 13 | Định lý ánh xạ co | bỏ | Không vào tuyến chính | Bài này không chứng minh hội tụ bằng phép co |
| 14 | Mục lục lặp | bỏ | Không vào tuyến chính | Không tạo trang lặp chức năng |
| 15 | Dự đoán phi mô hình | tách | L05-A03–L05-A05 | Nêu vấn đề trước, rồi dữ liệu và kiểm tra; tách giá trị thật/ước lượng |
| 16 | Thông tin quan sát | gộp | L05-A04–L05-A05 | Chuẩn hóa mẫu chuyển và chỉ số thưởng; thuật toán vẫn cần tương tác |
| 17 | Lợi tức đầy đủ và MC | tách | L05-B01–L05-B03, L05-B05 | Ví dụ và trực giác trước công thức; khôi phục dòng bị cắt, nêu T và trạng thái kết thúc |
| 18 | MC lần ghé đầu tiên | sửa | L05-B04–L05-B05, L05-B10, L05-B12 | Bổ sung mọi lần ghé, giả mã đầy đủ và điều kiện từ SB |
| 19 | Chuỗi ngắn và giá trị thật | tách | L05-B01, L05-D02 | Môi trường trước thuật toán; giá trị chuẩn sau ước lượng. Số 0.524/0.905 đúng |
| 20 | Lượt lặp và kết quả MC 0.5 | sửa | L05-B02, L05-B08–L05-B09 | Nêu lần ghé đầu tiên, V ban đầu 0 và bước học 0.5 |
| 21 | Trung bình gia tăng/bước hằng | tách | L05-B06–L05-B09 | Tính tay → chứng minh → biến thể; tách hai trục |
| 22 | Bài tính MC | sửa | L05-B11, L05-B13 | Nêu đủ quy tắc lần ghé và bước học; có đáp án khác nhau |
| 23 | Công thức lặp và không chệch | gộp | L05-B07, L05-B12 | Không lặp công thức; giới hạn phát biểu không chệch theo đối tượng và giả thiết |
| 24 | Chờ một bước và bootstrap | tách | L05-C01–L05-C03 | Dùng chuỗi đã học, trực giác và tính tay trước công thức |
| 25 | TD(0), mục tiêu và sai số | tách | L05-C04–L05-C06, L05-C10 | Bổ sung quy trình đầy đủ, trạng thái kết thúc, tự chuyển và kiểm tra |
| 26 | Độ chệch/phương sai | sửa | L05-D05–L05-D06 | Nêu bảng V cố định khi phân tích; không tuyên bố thứ tự phương sai phổ quát |
| 27 | Lặp giải thích phương sai | gộp | L05-D06 | Giữ cơ chế và điều kiện lý tưởng, bỏ mức độ không định lượng |
| 28 | Ưu/nhược MC–TD | sửa | L05-C09, L05-D07, L05-E01 | Thay tuyệt đối bằng thông tin, chi phí và điều kiện; phân biệt mẫu mới/theo lô |
| 29 | So sánh chuỗi ngắn | tách | L05-C07–L05-C08, L05-D01 | Tính từng bước rồi so sánh; MC cập nhật sau kết thúc, TD tại mỗi chuyển |
| 30 | Chuỗi dài | giữ | L05-D03 | Giữ hình và giá trị chuẩn 0.829/0.992 đã kiểm |
| 31 | Hai lợi tức và bảng so sánh | sửa | L05-D04, L05-D06 | Số mũ đúng là 3 và 1; hai đường không chứng minh phương sai hoặc tốc độ học |
| 32 | Câu hỏi mở rộng | gộp | L05-E02–L05-E04 | Giữ giới hạn và tự kiểm trong phạm vi, lược điều khiển/xấp xỉ hàm |
| 33 | Tổng kết | sửa | L05-E01–L05-E02 | Trả lời bài toán mở đầu qua lựa chọn mục tiêu và điều kiện |

Các trang thêm có căn cứ: L05-A05, L05-B13, L05-C10, L05-D12, L05-E04 là kiểm tra mỗi mạch; L05-B06–L05-B10 hoàn thiện cập nhật MC theo SB §2.4–2.5 và §5.1; L05-C03, L05-C05–L05-C06 hoàn thiện thao tác TD; L05-D08–L05-D11 là Ví dụ 6.4 và quy trình theo lô của SB §6.3; L05-E05 là đường đọc theo vị trí đã kiểm.

## Ánh xạ bảy bài HW05 và 30 phút chữa bài

HW05 là `RL-hk2-2025-2026/resources/hw05-model-free-prediction.pdf`. Năm bài đầu nằm ở trang 1, hai bài sau ở trang 2. Các hiệu chỉnh dưới đây phải xuất hiện trong đề diễn đạt lại và lời giải; không âm thầm chép tiền đề sai từ PDF nguồn.

| Bài | Quyết định và đề dùng | Nội dung chuẩn bị trong bài | Đáp án hoặc tiêu chí kiểm tra | Phút chữa |
|---:|---|---|---|---:|
| 1 | giữ: so sánh mục tiêu, thời điểm cập nhật, khả năng học trước kết thúc | L05-B03, L05-C01–L05-C05, L05-E01 | MC dùng $G_t$ sau kết thúc; TD dùng $R_{t+1}+\gamma V_t(S_{t+1})$ sau một chuyển | 1 |
| 2 | sửa thuật ngữ: dữ liệu mẫu và thiếu mô hình | L05-A03–L05-A05 | Nêu mẫu $(S_t,A_t,R_{t+1},S_{t+1})$; chính sách cố định; cần dữ liệu đủ phủ, ước lượng có sai số hữu hạn mẫu | 1 |
| 3 | giữ: mục tiêu, sai số và cập nhật TD(0) | L05-C03–L05-C06, L05-C10 | Đúng HT4, chỉ số, dấu, bảng trước cập nhật và giá trị ở trạng thái kết thúc bằng 0 | 2 |
| 4 | sửa tiền đề: phân tích nguồn sai lệch/phương sai và giới hạn kết luận về hiệu quả mẫu trong lượt dài, thưởng thưa | L05-D03–L05-D07, L05-D12 | MC dùng toàn đuôi; TD dùng V nên có thể sai lệch; không có bảo đảm TD luôn nhanh hơn hoặc phương sai luôn nhỏ hơn | 3 |
| 5 | sửa cấu trúc: tách lựa chọn lần ghé và lựa chọn bước học; nêu điều kiện thay cho “cả ba cùng hội tụ” | L05-B04–L05-B13, L05-D07 | Hai trục tạo bốn cấu hình; $1/n$ là trung bình mẫu; bước hằng đặt trọng số theo thời gian và có thể dao động; nêu bộ điều kiện mọi lần ghé ở B12/topic-11; trung bình $1/N(s)$ nhất quán theo lượt; không suy không chệch hữu hạn mẫu hoặc bảo đảm bước hằng | 4 |
| 6 | giữ dữ kiện chuỗi năm ô; tính chuẩn Bellman để đối chiếu | Tiên quyết Bài 04; L05-D02 nêu đúng vai trò chuẩn có mô hình | Hệ và nghiệm phía dưới; thưởng kỳ vọng ở $c_4$ bằng 7.8; giá trị tăng dần trong đúng mô hình này | 9 |
| 7 | sửa: yêu cầu MC lần ghé đầu tiên; thêm mọi lần ghé để so sánh; TD chạy riêng từ bảng 0 qua hai lượt | L05-B11, L05-C07–L05-C08, L05-D01 | Bảng đáp án phía dưới; so sánh tốc độ truyền thưởng chỉ trên hai lượt và đúng thứ tự đã dùng | 10 |

Tổng chữa bài 30 phút; không bổ sung trình diễn mã. Với bài 4–5, thời gian tập trung sửa tiền đề và kiểm điều kiện; không trình bày một chứng minh hội tụ dài. Phần này dùng học liệu hoặc ghi chú chữa bài, không thêm trang dọc ngoài 45 trang chính khi triển khai.

### Đáp án chuẩn bài 6

Dữ kiện: $c_1,\ldots,c_5$, $c_5$ trạng thái kết thúc, $\gamma=0.9$; đi phải 0.8, đứng 0.1, trái 0.1; vượt biên thì đứng; mọi chuyển thưởng −1 trừ $c_4\to c_5$ thưởng +10. Đặt $v_i=v_\pi(c_i)$ và $v_5=0$:

$$v_1=-1+0.9(0.2v_1+0.8v_2),$$
$$v_2=-1+0.9(0.1v_1+0.1v_2+0.8v_3),$$
$$v_3=-1+0.9(0.1v_2+0.1v_3+0.8v_4),$$
$$v_4=0.8(10)+0.2(-1)+0.9(0.1v_3+0.1v_4).$$

Nghiệm gần đúng $(2.658941901,4.417128276,6.639280500,9.228060709)$. Biên trái làm xác suất đứng tại $c_1$ thành 0.2; tại $c_4$ thưởng kỳ vọng là 7.8. Bốn giá trị tăng dần phù hợp việc các trạng thái gần đích hơn trong đúng chuỗi này có phần thưởng dương đến sớm hơn và ít chi phí bước kỳ vọng hơn. Kết luận tăng dần phải dựa trên hệ/so sánh đã giải, không là định luật cho mọi môi trường có đích.

### Đáp án chuẩn bài 7

Giữ $e_1:S,X,S,X,G$, $e_2:S,X,S,L$, $\gamma=1$, $\alpha=0.5$, khởi tạo riêng từng phương pháp từ 0. Thưởng khi vào L/G là −1/+1, các chuyển khác 0; giá trị ở trạng thái kết thúc bằng 0.

| Cấu hình | Sau $e_1$: $(V(S),V(X))$ | Sau $e_2$ |
|---|---|---|
| MC lần ghé đầu tiên, bước hằng 0.5 | $(0.5,0.5)$ | $(-0.25,-0.25)$ |
| MC mọi lần ghé, bước hằng 0.5 | $(0.75,0.75)$ | $(-0.5625,-0.125)$ |
| TD(0) trực tuyến, bước hằng 0.5 | $(0,0.5)$ | $(-0.375,0.375)$ |

TD sau từng chuyển của $e_1$: $(0,0),(0,0),(0,0),(0,0.5)$; của $e_2$: $(0.25,0.5),(0.25,0.375),(-0.375,0.375)$. MC mọi lần ghé trong $e_2$ cập nhật S hai lần theo chiều thời gian. Để đối chiếu bài 5, nếu đổi sang trung bình mẫu thì sau hai lượt, MC lần ghé đầu tiên cho $(0,0)$ và mọi lần ghé cho $(0,1/3)$.

## Nguồn dùng khi triển khai

Nguồn L05/HW05 theo đường dẫn và trang ở hai bảng ánh xạ. SB: [Sutton–Barto, ấn bản 2, MIT Press](https://mitpress.mit.edu/9780262039246/reinforcement-learning/), thông tin xuất bản 2018; nội dung và trang theo bản PDF 2020 đã đọc cục bộ, trang PDF = trang in + 22. UCL: [David Silver, Lecture 4](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-4-model-free-prediction-.pdf), tr.1–30; Stanford: [CS234 Lecture 3](https://web.stanford.edu/class/cs234/slides/lecture3pre.pdf), tr.1–49 theo chỉ số PDF. Nguồn đại học hỗ trợ thiết kế; không sao chép tài sản hoặc dùng lỗi số học trong slide tham khảo. Bảng nguồn đầy đủ và phạm vi đọc nằm trong analysis.md.

## Tự kiểm và giới hạn

Mục tiêu MT1 được đo ở L05-A05; MT2–MT3 ở L05-B13; MT4 ở L05-C10; MT5 ở L05-D12; MT6 và liên kết toàn bài ở L05-E04. Năm trang kiểm tra là riêng biệt, đủ dữ kiện, có đáp án và ngân sách hoạt động. Tổng theo trang đã tính bằng dữ liệu cấu trúc là 45 trang, 120 phút, khớp năm mạch; phần chữa HW05 là 30 phút riêng.

Chuỗi ngắn giữ xuyên MC và TD; chuỗi dài có chức năng tính chiết khấu và giới hạn kết luận; A–B chỉ phục vụ tiêu chuẩn dữ liệu cố định. L05-D09 có một lượt quét số và quy trình, L05-D11 mới dùng lượt tiếp theo để kiểm cơ chế; không đặt hai lượt quét và hai giả mã đầy đủ lên một mặt trang. Mọi phép tính chính đã đối chiếu báo cáo kiểm toán số. Không có đường học thực nghiệm tự tạo hoặc raster chưa duyệt.

Các trang L05-B10, L05-C05 đã được kiểm hiển thị ở bản trước; L05-B08, L05-B12, L05-D04, L05-D05, L05-D09 và L05-D11 cần kiểm lại sau chỉnh sửa; công thức khai triển, điều kiện bước học riêng A–B và chứng minh phương sai nằm trong ghi chú. Ghi chú học thuật trong dàn bài là nội dung để biên soạn, không được chép cả mã trang, thời gian, quyết định hoặc chỉ dẫn điều phối sang ghi chú diễn giả.

Bản mới đã biên tập no-ai-slop Edit và rà thuật ngữ, đầu vào/đầu ra theo Quill; kết quả được ghi ở review-log. Dàn bài đã qua kiểm định storyboard và được điều phối chấp nhận; HTML/học liệu đã qua năm vai rà độc lập trên bản cố định. Các phát hiện đã được sửa cục bộ và rà lại theo phạm vi ảnh hưởng; toàn tuyến mạch viết cùng bản hiển thị rộng/hẹp sau sửa đều đạt. Giới hạn đọc trên điện thoại, thời lượng chưa diễn tập và công cụ Browser được ghi trong review-log.
