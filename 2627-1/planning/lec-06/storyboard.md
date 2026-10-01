# Storyboard mới Bài 06: Điều khiển phi mô hình

Ngày lập: 29-09-2026. Bản cập nhật theo HTML và học liệu sau biên tập; 45 trang, bảy mạch, 120 phút kể cả kiểm tra. Năm báo cáo độc lập trên bản nháp đã được điều phối viên chấp nhận; đã hoàn tất tái kiểm các vùng thay đổi và kiểm định cuối; bằng chứng và giới hạn nằm trong review-log. Nguồn và các phát biểu hình thức tham chiếu [analysis.md](analysis.md); thuật ngữ và ánh xạ đủ 30 trang tại [outline.md](outline.md). Không dùng nội dung sản phẩm Bài 06 cũ.

Trong mỗi phiếu, “mặt trang” ghi đặc tả nội dung học thuật đã triển khai; “ghi chú” là diễn giải học thuật/đáp án. Các nhãn vai trò, thời lượng, nguồn quyết định, quan hệ trước–sau và mã trang chỉ phục vụ soạn bài. Không chép chúng thành lời điều phối hoặc mã hiển thị trong deck/notes. Mọi lời mời làm bài dùng **Câu hỏi:**. Nguồn L06 dùng số PDF; SB dùng trang in, PDF=trang in+22.

## Bản đồ các mạch và ngân sách

| Mạch, loại | Chức năng, đầu vào | Kết quả đầu ra; đóng góp cho vấn đề trung tâm | Trang và phút | Kiểm tra; chủ đề học liệu |
|---|---|---|---|---|
| A, mở đầu | Nhận tiên quyết dự đoán; đặt quyết định tại D | Phân biệt thông tin quan sát với giá trị hành động cần học | A01, A02, A04, A03, A05: 1+2+2+3+2=10 | A05; lec-06-topic-01 |
| B, phát triển khái niệm | Nhận thiếu hụt so sánh hành động | q/Q, chọn hành động có thăm dò; tạo đầu vào cho MC | B01–B07: 2+3+2+3+2+3+3=18 | B07; lec-06-topic-02 |
| C, thuật toán và luyện tập | Nhận cặp, lợi tức, chính sách mềm | Quy trình MC đầy đủ, giới hạn chờ kết thúc | C01–C04, C07, C05, C06, C08: 2+2+3+3+3+3+3+3=22 | C08; lec-06-topic-03 |
| D, thuật toán và luyện tập | Nhận giới hạn MC, tiên quyết TD | Sarsa dùng hành động kế tiếp đã lấy mẫu; bảng từ năm chuyển | D01–D08: 2+2+3+3+3+3+3+3=22 | D08; lec-06-topic-04 |
| E, khái niệm/thuật toán và luyện tập | Nhận mục tiêu Sarsa phụ thuộc hành vi | Q-learning với mục tiêu cực đại; so sánh trên dữ liệu chung | E01–E08: 2+3+3+3+2+3+3+3=22 | E08; lec-06-topic-05 |
| F, khái niệm và áp dụng | Nhận kết quả hữu hạn mẫu của ba phương pháp | Phân biệt điều kiện dài hạn, định lý và dừng thực hành | F01–F05: 3+3+3+4+3=16 | F05; lec-06-topic-06 |
| G, kết luận và vận dụng tổng hợp | Nhận dữ liệu/mục tiêu/điều kiện | Trở lại D, chọn phương pháp có lý do; bài tập/đọc thêm đúng phạm vi | G01–G04: 3+2+3+2=10 | G03; lec-06-topic-07 |

Tổng: 45 trang, 120 phút. Bảy section ngoài tương ứng A–G; ứng dụng đặt trong từng mạch, không tạo phần thứ tám. 30 phút chữa bài riêng đã đặc tả tại analysis §7; không tính lại vào bảng này, không tạo code demo.

Thứ tự trình chiếu sau rà soát từng trang 01-10-2026: A04 trước A03 (bài toán điều khiển trước ví dụ, theo nguồn tr. 6 rồi tr. 15); C07 ngay sau C04 (ví dụ lấy mẫu và cập nhật một lượt liền mạch, rồi mới tới thuật toán C05–C06). Hai lần đổi chỗ không đổi phút, số trang hay chức năng mạch. Mỗi phiếu trang có dòng "Rà soát từng trang 01-10-2026" ghi quyết định và thay đổi.

## Bản đồ chu trình học tập

| Cụm; dạng; tiên quyết; sản phẩm | Vấn đề, trực giác, ví dụ | Hình thức/quy trình | Ứng dụng và kiểm tra | Kế thừa dữ kiện, bước gộp, câu nối, phút |
|---|---|---|---|---|
| Mở đầu; định vị; MDP/MC/TD đã học; xác định thông tin thiếu | A03 quyết định tại D bằng ví dụ môi trường; A04 so sánh dự đoán/điều khiển | Không áp dụng định lý mới; A04 chỉ nhắc tiên quyết | A05 nhận diện mẫu và giới hạn suy luận | A01→A02→A03 đúng thứ tự giới thiệu/nội dung/động lực. A05 tạo nhu cầu tách hai hành động. 10 phút. |
| KN1; khái niệm; mẫu và chính sách; diễn giải q/Q | A05→B01 thiếu ô trái ở D; B01 bảng I làm ví dụ dẫn nhập cùng nhu cầu so sánh | B02 định nghĩa hành động đầu cố định và chính sách tiếp nối | B03 vòng cập nhật từ dữ liệu; B07 giải thích q/Q | B01 đưa ví dụ trước định nghĩa, trực giác nằm trong phép so sánh hai ô. B02 truyền đúng cặp D0 sang $q_\pi$ (D,0). B03 tạo nhu cầu thăm dò. B01–B03:7 phút, kiểm tra chung 3 phút ở B07. |
| KN2; khái niệm; KN1 và phân phối; tính xác suất | B03 hành động chưa thử→B04 dành xác suất để lấy dữ liệu; B04 tính 1/8,7/8 | B05 công thức, đồng hạng, lớp mềm | B06 cải thiện với q chính xác; B07 tính và phân biệt | Ví dụ số B04 trước HT2. B06 là kết quả hỗ trợ KN7, mức phác thảo; proof dài ở ghi chú. B04–B06:8 phút; B07 dùng chung với KN1, không cộng hai lần. |
| KN3; thuật toán; lợi tức+cặp+thăm dò; làm một lượt MC | C01 thiếu giá trị hai ô→gắn lợi tức với cặp; C02 tính mẫu đầu D→E | C03 trung bình/lần ghé đầu; C05–C06 quy trình đầy đủ | C04 cung cấp lượt số cho C07; C08 kiểm cặp lặp | C02 số 10,N0=0 chuẩn bị tử/mẫu C03. C04 không là ví dụ đầu tiên; là dữ liệu ứng dụng quy trình. G tính lùi nhưng chỉ số ghé đầu lưu theo chiều thuận. Đầu ra MC còn chờ trạng thái kết thúc tạo nhu cầu D01. 22 phút. |
| KN4; thuật toán; MC,TD,Q; thực hiện Sarsa | D01 tiền tố thiếu lợi tức→giá trị tiếp nối; D02 dữ liệu, D03 hai bước số | D04 mục tiêu/sai lệch; D05–D06 quy trình đầy đủ | D07 trạng thái kết thúc; D08 tiền tố cuối ngân sách | D03 dùng mẫu 2 C0→B,A'=0, Q(B,0)=0; D04 giữ cùng ký hiệu. D05/D06 là hai nửa liên tục, không bỏ khởi tạo/dừng. D08 nêu phụ thuộc hành động thăm dò để vào E01. 22 phút. |
| KN5; kết hợp; KN4; phân biệt hành vi/đích và thực hiện Q-learning | E01 tách đích khỏi A' hành vi→E02 cùng mẫu 2 nhưng dùng max | E03 công thức; E04–E05 quy trình đầy đủ | E06 đủ năm mẫu; E07 áp vào điều kiện dữ liệu; E08 tính mục tiêu | Đặt lại bảng I riêng, không dùng kết quả Sarsa. Ví dụ dùng cùng phần thưởng−1 và bảng B=(0,1) để chỉ đổi giá trị tiếp nối. Sau E08 cần phân biệt kết quả vài mẫu với bảo đảm F01. 22 phút. |
| KN6; khái niệm; chính sách/bước học/cập nhật; kiểm giả thiết | F01 thiếu căn cứ từ năm mẫu→độ phủ và sai lệch mẫu; F02 lịch ε cố định/giảm, F03 bước 0.8/1/n | F02 GLIE; F03 Robbins–Monro; F04 định lý trong miền F01 | F04 đối chiếu hai thuật toán và giới hạn MC; F05 phân loại trường hợp | Ví dụ và trực giác gộp ngay trước công thức F02/F03; không dùng chúng làm chứng minh. KN6 không là thuật toán mới nên giả mã không áp dụng. Đầu ra là điều kiện chọn phương pháp cho G. 16 phút. |
| Tổng hợp; kết hợp; KN1–KN6; chọn phương pháp | G01 tổ chức lại dữ liệu/mục tiêu đã học; G02 trở lại D | Không áp dụng hình thức trọng tâm mới | G03 lựa chọn có điều kiện; G04 bài tập/đọc thêm | G02 dùng đúng các bảng hữu hạn mẫu, không nâng thành q*. G04 chỉ trỏ nội dung đọc thêm 19/29, không giảng định lý mới trong kết luận. 10 phút. |

## A. Bài toán điều khiển

#### L06-A01: Điều khiển phi mô hình

- **Vai trò, mục tiêu, thời lượng:** giới thiệu chủ đề; MT1/MT7; 1 phút. Luận điểm: bài học tìm hành động từ kinh nghiệm lấy mẫu.
- **Mặt trang:** “Bài 06 · Học tăng cường”, “Điều khiển phi mô hình”, “Monte Carlo (MC), Sarsa và Q-learning”, “Học kỳ 1 · 2026–2027”. Tạ Việt Cường là tác giả nguồn.
- **Ghi chú:** Bài tập trung vào bảng giá trị hành động hữu hạn. Ba phương pháp được phân biệt qua dữ liệu cần có và cách tạo mục tiêu cập nhật. Bảng sau hữu hạn mẫu chưa tự bảo đảm chính sách tối ưu.
- **Bố cục/hình thức:** một khối tiêu đề, không hình trang trí; chưa cần công thức.
- **Quan hệ và lý do:** đầu vào là tên học phần; đầu ra là phạm vi để A02 đặt lộ trình. `Giữ, sửa` L06 tr. 1: chuẩn hóa tên/học kỳ, giữ chủ đề và tác giả. Không sao chép metadata bài mẫu.
- **Rà soát từng trang 01-10-2026:** `giữ`. Không đổi.

#### L06-A02: Nội dung và mục tiêu

- **Vai trò, mục tiêu, thời lượng:** bản đồ bài; MT1–MT7; 2 phút. Luận điểm: lựa chọn phương pháp phụ thuộc dữ liệu, mục tiêu và điều kiện bảo đảm.
- **Mặt trang:** bảy mục ngắn: bài toán điều khiển; giá trị hành động và thăm dò; Monte Carlo; Sarsa; Q-learning; điều kiện bảo đảm; tổng hợp. Ba mục tiêu hiển thị: thực hiện cập nhật; giải thích khác biệt mục tiêu; kiểm tra điều kiện sử dụng.
- **Ghi chú:** năng lực tính bao gồm lợi tức và một bước của ba thuật toán; năng lực giải thích gồm vai hành vi/đích và xử lý kết thúc; năng lực kiểm giả thiết gồm bao phủ và bước học. Các bài tính giữ một môi trường chung.
- **Bố cục/hình thức:** mục lục chữ có quan hệ theo chiều đọc, không sơ đồ trang trí; không liệt kê toàn bộ ký hiệu tại đây.
- **Quan hệ và lý do:** A01 xác định chủ đề; A02 cho vị trí các phương pháp; A03 cung cấp bài toán mà chúng giải quyết. `Sửa` L06 tr. 2: ví dụ phân bố tại chỗ dùng, không tạo khối ví dụ tách khỏi cơ chế.
- **Rà soát từng trang 01-10-2026:** `sửa`. Ba mục tiêu cụ thể: tính cập nhật MC/Sarsa/Q-learning trên bảng giá trị hành động; phân biệt chính sách sinh dữ liệu với chính sách được học; nêu điều kiện thăm dò và bước học để hội tụ tới giá trị tối ưu. Mục 6 đổi thành "Điều kiện hội tụ".

#### L06-A04: Từ dự đoán đến điều khiển

- **Vai trò, mục tiêu, thời lượng:** nhắc tiên quyết và xác định nhu cầu; MT1; 2 phút. Luận điểm: điều khiển bổ sung quyết định thay đổi chính sách vào bài toán dự đoán từ mẫu.
- **Mặt trang:** hai cột “Dự đoán: chính sách đã cho → ước lượng giá trị” và “Điều khiển: kinh nghiệm → giá trị hành động → cải thiện chính sách”. Tiên quyết: quá trình quyết định Markov (MDP), kỳ vọng, giá trị; MC và sai phân thời gian (TD), với biến thể TD(0).
- **Ghi chú:** Quá trình quyết định Markov (MDP) dùng trạng thái Markov, hành động hợp lệ và động lực không đổi theo thời gian; trạng thái hiện tại chứa thông tin cần để dự đoán bước kế theo hành động. Monte Carlo (MC) dự đoán dùng lợi tức sau lượt; sai phân thời gian (TD), với biến thể TD(0), dùng thưởng và giá trị trạng thái tiếp. Điều khiển cần phân biệt các hành động ở cùng trạng thái; ký hiệu giá trị của Bài 05 được giữ.
- **Bố cục/hình thức:** hai thẻ chữ; công thức dự đoán dài chỉ trong notes khi cần ôn. Không mở thêm thuật toán.
- **Quan hệ và lý do:** A03 có hành động cần chọn; A04 đặt thiếu hụt; A05 kiểm người học nhận diện thông tin trước khi đưa q/Q. `Gộp, sửa` L06 tr. 3–6/22; SB §5.2, §6.2 tr. 124. Không giữ ưu thế tốc độ mẫu không có điều kiện.
- **Rà soát từng trang 01-10-2026:** `sửa, đổi chỗ`. Đặt trước A03 để bài toán điều khiển đứng trước ví dụ (nguồn tr. 6 trước tr. 15). Thêm hộp mục tiêu điều khiển theo nguồn tr. 6; gộp hai dòng tiên quyết thành một.

#### L06-A03: Chuỗi năm trạng thái

- **Vai trò, mục tiêu, thời lượng:** động lực với ví dụ dẫn nhập; MT1/MT7; 3 phút. Luận điểm: tác tử cần dữ liệu về hệ quả của từng hành động để chọn tại D.
- **Mặt trang:** SVG chuỗi A–B–C–D–E; D bắt đầu, A/E kết thúc; 0 trái,1 phải; thưởng vào A=1000, vào E=10, còn lại−1; $\gamma=1$. Dòng nhiệm vụ: “Học giá trị của hai hành động tại D từ các lượt hoặc chuyển tiếp đã quan sát.”
- **Ghi chú:** $\mathcal S=\{B,C,D\}$ và $\mathcal S^+=\{A,B,C,D,E\}$. Chuyển tất định, thưởng gắn với cạnh; sau trạng thái kết thúc không có hành động. Mô hình được công bố để kiểm phép tính, thuật toán chỉ dùng mẫu. Lượt kết thúc thật tại A/E; độ dài ba bước chỉ thuộc lượt minh họa, không làm C thành trạng thái kết thúc.
- **Bố cục/hình thức:** `chain-five-states.svg` lớn ở giữa; một chú thích phân biệt thưởng trên cạnh với giá trị tiếp nối 0 của trạng thái kết thúc.
- **Quan hệ và lý do:** A02 nêu phương pháp; A03 làm cụ thể quyết định; A04 xác định phần kiến thức dự đoán chưa giải quyết. `Tách, sửa, chuyển cục bộ` L06 tr. 15 lên trước khái niệm; sửa mơ hồ thời hạn theo analysis§5.
- **Rà soát từng trang 01-10-2026:** `sửa, đổi chỗ`. Tiêu đề gọi tên ví dụ; trang đứng sau A04.

#### L06-A05: Kiểm tra thông tin trong một mẫu

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch A; MT1; 2 phút, gồm 45 giây suy nghĩ,30 giây trả lời,45 giây đối chiếu. Luận điểm: một chuyển chỉ cung cấp kết quả của hành động đã thực hiện.
- **Mặt trang — Câu hỏi:** cho mẫu $(D,1,10,E)$ trong môi trường vừa nêu. Xác định trạng thái đầu, hành động, phần thưởng, trạng thái kế tiếp. Xác định thông tin mẫu này cung cấp cho hành động trái ở D và số hành động còn thực hiện trong lượt.
- **Ghi chú/đáp án:** D là trạng thái đầu,1 đi phải,10 là thưởng,E là trạng thái kết thúc. Không còn hành động trong lượt. Mẫu không chứa một lần thử trái ở D hoặc lợi tức sau trái. Dữ kiện mô hình của bài tập cho phép suy luận riêng, nhưng không biến mẫu này thành dữ liệu của hành động trái.
- **Tiêu chí:** đúng cả bốn thành phần; nêu không có mẫu hành động trái; không gán thưởng 10 cho mọi hành động ở D. Không đòi công thức điều khiển chưa học.
- **Quan hệ, nguồn, quyết định:** A04→A05 kiểm thiếu hụt→B01 tách giá trị theo hành động. `Thêm` câu kiểm tra suy từ L06 tr. 3/15/16; không SVG mới, dùng bộ bốn lớn. Sau rà SV-02, nhãn “Câu hỏi:” đặt thành dòng khối trước danh sách, giữ nguyên dữ kiện và yêu cầu.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề theo quy ước "Kiểm tra …".

## B. Giá trị hành động và thăm dò

#### L06-B01: Giá trị hành động

- **Vai trò, mục tiêu, thời lượng:** vấn đề, trực giác và ví dụ dẫn nhập KN1; MT1; 2 phút. Luận điểm: bảng Q giữ một ước lượng riêng cho mỗi hành động tại cùng trạng thái.
- **Mặt trang:** bảng I với B=(0,1), C=(1,0), D=(0,1), cột 0 trái/1 phải. Tại D, chọn cực đại của bảng hiện có dẫn tới phải; hai ô là ước lượng khởi tạo, chưa là kết quả quan sát.
- **Ghi chú:** Một giá trị trạng thái không tự chỉ ra hành động nào tạo kết quả ấy khi không có mô hình để tính kỳ vọng từng hành động. Bảng I có sáu ô; Q(D,0)=0 là khởi tạo, chưa xác định giá trị đúng. Cập nhật một cặp không trực tiếp thay đổi ước lượng của các cặp khác, dù các trạng thái có đặc điểm tương tự; giữ giới hạn bảng tra của L06 tr. 7 theo RL-02. Xét riêng chính sách tiếp nối $\pi_L$ luôn chọn trái tại B,C,D: sau hành động đầu 0 ở D, lượt đi D–C–B–A. Chính sách minh họa này khác chính sách tham lam của bảng I, vốn tạo vòng B↔C. Việc nêu $\pi_L$ không thay bảng I hoặc hành vi của các ví dụ sau.
- **Bố cục/hình thức:** bảng HTML 3×2, đánh dấu hàng D bằng viền và nhãn; chưa dùng argmax trước khi đối tượng rõ.
- **Quan hệ và lý do:** A05 chỉ ra ô thiếu dữ liệu; B01 cung cấp đối tượng để B02 định nghĩa. `Tách, sửa` L06 tr. 7/15, SB §5.2 tr. 96–97. Ví dụ trước hình thức tránh đưa Q như một ký hiệu tự đủ.
- **Rà soát từng trang 01-10-2026:** `sửa`. Câu mở nêu lý do cần $Q$ thay vì $V$ khi thiếu mô hình (nguồn tr. 7); ghi chú nêu kỳ vọng một bước cần $p(s',r\mid s,a)$.
- **Sửa sau rà soát độc lập 01-10-2026:** Câu mở nêu đủ: $v(s')$ không cho biết mỗi hành động dẫn tới những $s'$, phần thưởng nào và với xác suất bao nhiêu.

#### L06-B02: Giá trị hành động của một chính sách

- **Vai trò, mục tiêu, thời lượng:** hình thức KN1; MT1; 3 phút. Luận điểm: $q_\pi$ là kỳ vọng của lợi tức với chính sách tiếp nối xác định, còn Q là ước lượng.
- **Mặt trang:** chính sách tiếp nối minh họa $\pi_L$ luôn chọn trái tại B,C,D. Định nghĩa lợi tức $G_t=\sum_{j=t}^{T-1}\gamma^{j-t}R_{j+1}$, $G_T=0$; công thức trung tâm $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$. Hai nhãn “a: hành động đầu”, “π: các hành động sau”; $s\in\mathcal S$, $a\in\mathcal A(s)$. Q là ước lượng, $q_*$ là giá trị hành động tối ưu.
- **Ghi chú:** t là thời điểm bắt đầu tính lợi tức, $0\le t<T$; T là thời điểm kết thúc thật của lượt; $R_{j+1}$ là thưởng sau hành động tại j. Tổng rỗng tại T bằng 0; T không phải ngân sách chạy. Kỳ vọng gồm động lực môi trường và hành động sau hành động đầu. Với $\pi_L$ luôn đi trái, $q_{\pi_L}(D,0)=998$ qua D–C–B–A và $q_{\pi_L}(D,1)=10$ vì đi phải tới E rồi kết thúc; cả hai dùng cùng một chính sách tiếp nối, có lợi tức hữu hạn. Các số này không thay bảng khởi tạo I. Với chính sách tham lam của bảng I, chọn trái ở D dẫn vào vòng B↔C nhận −1 mãi; không có giá trị hữu hạn tương ứng khi γ=1. Miền γ<1 với thưởng chặn bảo đảm giá trị hữu hạn; γ=1 cần lợi tức khả tích.
- **Bố cục:** công thức q lớn; G và chú giải gọn, không ảnh hóa. Phân biệt học thuật “định nghĩa”/“ước lượng”, hai giá trị 998 và 10 thuộc $q_{\pi_L}$ với chính sách tiếp nối đã xác định; không gán chúng cho chính sách tham lam của bảng I.
- **Quan hệ, nguồn, quyết định:** B01 hai ô→B02 đối tượng kỳ vọng→B03 cách ước lượng/cải thiện. `Sửa, thêm giả thiết` L06 tr. 4/7, SB §5.2 tr. 96–97.
- **Rà soát từng trang 01-10-2026:** `sửa`. Viết $q_*(s,a)=\max_\pi q_\pi(s,a)$ trên mặt trang; ghi chú nêu cực đại đạt được trong MDP hữu hạn có chiết khấu.

#### L06-B03: Nhu cầu thăm dò

- **Vai trò, mục tiêu, thời lượng:** ứng dụng KN1, vấn đề vào KN2; MT1/MT2; 2 phút. Luận điểm: chính sách quyết định dữ liệu, còn bảng học từ dữ liệu quyết định chính sách tiếp theo.
- **Mặt trang:** `control-loop.svg`: tương tác→dữ liệu→cập nhật Q→chính sách→tương tác. Chú thích: “Hành động chưa được thử không nhận thêm dữ liệu từ vòng cập nhật.”
- **Ghi chú:** đánh giá cập nhật ước lượng; cải thiện chọn hành động theo ước lượng đó. Trong lặp chính sách lý tưởng, giá trị được tính chính xác; thực hành MC/TD chỉ cập nhật từ mẫu. Nếu luôn chọn phải ở D, các lượt D→E không sửa ô D0. Vòng này không phải chứng minh hội tụ.
- **Bố cục/hình thức:** một sơ đồ có nhãn động từ, không biểu tượng q* ở cuối đường hội tụ. Không công thức mới.
- **Quan hệ, nguồn, quyết định:** B02 phân biệt q/Q→B03 vòng phụ thuộc→B04 cần xác suất thăm dò. `Gộp, sửa` L06 tr. 6/10–11; SB §4.6 tr. 86–87, §5.3 tr. 97–99; đối chiếu UCL tr. 9.
- **Rà soát từng trang 01-10-2026:** `sửa`. Hộp nêu ví dụ cụ thể: bảng I tham lam tại D luôn đi phải, $Q(D,0)$ không nhận mẫu dù lợi tức đi trái là 998.
- **Sửa sau rà soát độc lập 01-10-2026:** Thêm dòng định nghĩa vòng đánh giá–cải thiện ($Q$ xác định chính sách, chính sách sinh dữ liệu cập nhật $Q$) trước ví dụ.

#### L06-B04: Xác suất chọn hành động tại D

- **Vai trò, mục tiêu, thời lượng:** trực giác và ví dụ KN2; MT2; 3 phút. Luận điểm: một phần xác suất chọn đều tạo cơ hội thử hành động chưa là cực đại.
- **Mặt trang:** tại D của bảng I, xác suất 3/4 chọn hành động cực đại 1; xác suất 1/4 chọn đều hai hành động. Kết quả theo nhánh: trái nhận $(1/4)(1/2)=1/8$; phải nhận $3/4+(1/4)(1/2)=7/8$.
- **Ghi chú:** nhánh thăm dò có thể chọn đúng hành động đang cực đại, nên xác suất hành động tham lam không chỉ bằng 3/4. Chính sách thuần tham lam cho B→C,C→B,D→E; vòng B↔C không kết thúc, dù lượt từ D kết thúc. Xác suất dương tại D chưa là bằng chứng mọi cặp đều được thăm vô hạn.
- **Bố cục:** hai nhánh xác suất bằng HTML; có thể dùng `greedy-chain.svg` nhỏ trong ghi chú/học liệu để minh họa vòng. Không dùng số RNG nguồn 17 ở đây vì đó là dữ kiện thao tác khác.
- **Quan hệ, nguồn, quyết định:** B03 bỏ sót D0→B04 phân bổ xác suất→B05 tổng quát hóa cho m hành động và đồng hạng. `Thêm hình thức trung gian` từ L06 tr. 11/15–17, SB tr. 100–101. Kết quả 1/8,7/8 đã kiểm chính xác.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-B05: Chính sách $\varepsilon$-tham lam

- **Vai trò, mục tiêu, thời lượng:** hình thức KN2; MT2; 2 phút. Luận điểm: phần thăm dò đều cộng với phần khai thác trên tập cực đại xác định một phân phối rõ cả khi đồng hạng.
- **Mặt trang:** $m(s)=|\mathcal A(s)|$, $\mathcal G_Q(s)=\arg\max_a Q(s,a)$ và
  $$\pi_\varepsilon(a\mid s)=\frac{\varepsilon}{m(s)}+(1-\varepsilon)\frac{\mathbf1\{a\in\mathcal G_Q(s)\}}{|\mathcal G_Q(s)|}.$$
  $0\le\varepsilon\le1$. Dòng định nghĩa mềm: $\pi(a\mid s)\ge\varepsilon/m(s)$.
- **Ghi chú:** tổng xác suất bằng ε+(1−ε)=1. $\mathcal G_Q$ là tập, không phải hành động duy nhất. Khi hai hành động đồng hạng, mỗi xác suất bằng 1/2. Chia đều cực đại là quy ước mở rộng của bài; sách dùng phá hòa tùy ý. Chính sách mềm bất kỳ không nhất thiết có dạng tham lam trên.
- **Bố cục:** một công thức trung tâm và hai chú giải; không chồng chứng minh cải thiện lên cùng trang.
- **Quan hệ, nguồn, quyết định:** B04 ví dụ hai hành động→B05 định nghĩa→B06 điều kiện cải thiện. `Sửa, bổ sung đồng hạng` L06 tr. 7/11/24; SB tr. 100–101.
- **Rà soát từng trang 01-10-2026:** `giữ`. Không đổi.

#### L06-B06: Cải thiện chính sách $\varepsilon$-tham lam

- **Vai trò, mục tiêu, thời lượng:** ứng dụng KN2, kết quả hỗ trợ KN7; MT2/MT6; 3 phút. Luận điểm: cải thiện $\varepsilon$-mềm có bảo đảm khi dùng giá trị chính xác của chính sách cũ.
- **Mặt trang:** giả thiết MDP hữu hạn, có động lực không đổi theo thời gian, thưởng chặn, $0\le\gamma<1$, cùng $\varepsilon<1$. Nếu π mềm và π' là ε-tham lam theo **$q_\pi$**, thì $v_{\pi'}(s)\ge v_\pi(s)$. Dòng suy luận: $\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$. Dòng giới hạn: “Thay $q_\pi$ bằng Q từ mẫu cần phân tích sai số riêng.”
- **Ghi chú:** Cho $q=(3,3,-1)$, $\varepsilon=0.3$, $\pi=(0.2,0.1,0.7)$ và $\pi'=(0.45,0.45,0.1)$. Kỳ vọng theo hai phân phối lần lượt bằng 0.2 và 2.6; đây là phép kiểm một bất đẳng thức tại một trạng thái, không phải kết quả của chuỗi A–E. Đặt $w_a=(\pi(a\mid s)-\varepsilon/m(s))/(1-\varepsilon)$: các trọng số không âm và có tổng bằng 1. Cực đại chặn trung bình theo w; cộng thành phần đều suy ra bất đẳng thức trên mặt trang. Toán tử Bellman của chính sách mới bảo toàn thứ tự và co khi γ<1, nên lặp toán tử cho kết luận không giảm. ε=1 cho chính sách đều duy nhất; ε>0 cố định giới hạn lớp chính sách đang xét. Thay giá trị chính xác bằng bảng nhiễu chưa bảo đảm từng cập nhật mẫu làm tăng giá trị.
- **Bố cục:** kết luận và một dòng bất đẳng thức; phép tách trọng số/chi tiết ở ghi chú, không thêm slide chứng minh.
- **Quan hệ, nguồn, quyết định:** B05 phân phối→B06 ý nghĩa cải thiện→B07 kiểm giới hạn, rồi C học Q từ mẫu. `Sửa, chuyển cục bộ` L06 tr. 24, SB tr. 101–103; phác thảo phù hợp tiên quyết cải thiện chính sách.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề gọi tên kết quả; dòng cuối nêu ý nghĩa: với $q_\pi$ chính xác, vòng đánh giá–cải thiện giữ thăm dò mà không làm giảm giá trị.

#### L06-B07: Kiểm tra chính sách $\varepsilon$-tham lam

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch B; MT1/MT2; 3 phút: 1 phút tính,45 giây trả lời,75 giây chữa. Luận điểm: quy tắc hành động và đối tượng giá trị phải cùng được xác định.
- **Mặt trang — Câu hỏi:** tại D, Q(D,0)=0, Q(D,1)=1 và ε=1/4. Tính xác suất mỗi hành động; tính lại nếu hai ô cùng bằng 1 với quy ước chia đều. Giải thích hành động và chính sách được cố định khi viết $q_\pi(D,0)$. Xác định bảng khởi tạo này đã đủ căn cứ cho kết luận cải thiện chính sách hay chưa; nêu lý do.
- **Ghi chú/đáp án:** Phân phối là $(1/8,7/8)$; khi đồng hạng là $(1/2,1/2)$. Trong $q_\pi(D,0)$, hành động đầu là 0, các hành động sau theo π. Bảng khởi tạo chưa được xác nhận bằng giá trị chính xác $q_\pi$, nên không đủ căn cứ áp dụng mệnh đề cải thiện dùng giá trị chính xác. Ngoài ra, miền bảo đảm đã phát biểu dùng γ<1, còn chuỗi minh họa dùng γ=1. Q là ước lượng; lựa chọn từ Q chưa chứng nhận cải thiện giá trị thật.
- **Tiêu chí:** tính cả xác suất nhánh thăm dò chọn hành động cực đại; tổng bằng 1; phân biệt tập cực đại với một hành động; xác định chính sách tiếp nối; nêu được Q khởi tạo chưa phải giá trị chính xác. Sai số 7/8 thành 3/4 cho thấy bỏ phần thăm dò vào cực đại.
- **Quan hệ, nguồn, quyết định:** B06 giá trị chính xác→B07 kiểm cơ chế/ý nghĩa→C01 cần ước lượng bằng lượt. `Thêm` câu hỏi dựa L06 tr. 7/15/17 và SB tr. 96–101; bảng HTML, không SVG mới.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

## C. Điều khiển Monte Carlo

#### L06-C01: Điều khiển Monte Carlo

- **Vai trò, mục tiêu, thời lượng:** vấn đề và trực giác KN3; MT3; 2 phút. Luận điểm: lợi tức quan sát sau một cặp là dữ liệu để ước lượng giá trị hành động của chính sách sinh lượt.
- **Mặt trang:** chuỗi “lượt theo π → lợi tức từ từng cặp → cập nhật Q → chính sách lượt sau”. Dòng giả thiết: lượt kết thúc thật, lợi tức khả tích, chính sách sinh lượt giữ cố định trong lượt.
- **Ghi chú:** MC dự đoán Bài 05 gắn lợi tức với trạng thái; điều khiển cần gắn với cặp để so sánh hành động. Cùng quy tắc π sinh hành động và quy định phần tiếp nối trong giá trị đang đánh giá, nên đây là theo chính sách. Giữ π trong lúc lấy lượt không cấm thay π sau khi lượt hoàn tất. Trung bình mẫu của quá trình đổi π không tự là trung bình độc lập cùng một $q_\pi$.
- **Bố cục/hình thức:** giản lược `control-loop.svg`, nhãn theo lượt; chưa viết quy tắc cập nhật tổng quát.
- **Quan hệ, nguồn, quyết định:** B07 cần dữ liệu→C01 gắn lợi tức với cặp→C02 một mẫu có số. `Gộp, sửa` L06 tr. 4/9–11, SB tr. 96–103; tách rõ đối tượng khỏi giả mã.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề; hình vòng lặp giữ vì hộp trên trang cụ thể hóa vòng ở B03 bằng lợi tức của lượt.
- **Sửa sau rà soát độc lập 01-10-2026:** Hộp nói rõ trang cụ thể hóa vòng của trang Nhu cầu thăm dò bằng lợi tức của lượt; ghi chú không dùng thuật ngữ học theo chính sách trước định nghĩa.

#### L06-C02: Monte Carlo với chính sách tham lam

- **Vai trò, mục tiêu, thời lượng:** ví dụ tính tay trước HT4; MT3; 2 phút. Luận điểm: với N0=0, mẫu đầu tiên thay giá trị khởi tạo của ô được quan sát.
- **Mặt trang:** bảng I ở D=(0,1); hành động tham lam 1 tạo D→E, thưởng 10, lợi tức 10. N(D,1):0→1; Q(D,1):1→10. Hai phép tính ngắn “trung bình một mẫu=10”, “1+(10−1)/1=10”.
- **Ghi chú:** mọi ô khác giữ nguyên; chính sách tham lam từ D vẫn đi phải. Bảng I cho B→C và C→B: đồ thị cảm sinh không phải mọi điểm đều dẫn trạng thái kết thúc. Chỉ lượt bắt đầu D đang xét kết thúc sau một bước. Giá trị khởi tạo 1 không được đếm như một lợi tức quan sát; nếu tính (1+10)/2 thì đã ngầm tạo giả quan sát.
- **Bố cục/hình:** `greedy-chain.svg` hiển thị đủ vòng B–C và chuyển D→E, cùng hai ô N/Q trước–sau. Mô tả thay thế chỉ nêu chính sách và hệ quả; bỏ câu bình luận biên soạn theo FL-01. Margin của card riêng C02 giữ ở .2em theo sửa R01 trước bản cố định.
- **Quan hệ, nguồn, quyết định:** C01 trung bình lợi tức→C02 mẫu đầu→C03 tổng quát số mẫu và lần ghé. `Giữ, sửa` L06 tr. 15–16; thêm N0=0 theo SB tr. 101 và quyết định điều phối.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-C03: Cập nhật Monte Carlo theo lần ghé đầu

- **Vai trò, mục tiêu, thời lượng:** hình thức KN3; MT3; 3 phút. Luận điểm: mỗi cặp đóng góp một lợi tức ở lần ghé đầu mỗi lượt, bộ đếm tăng theo đúng các mẫu được dùng.
- **Mặt trang:** định nghĩa lần ghé đầu của cặp: $(S_t,A_t)$ chưa xuất hiện ở thời điểm nhỏ hơn t. Công thức $G_T=0$, $G_t=R_{t+1}+\gamma G_{t+1}$; rồi $N\leftarrow N+1$, $Q\leftarrow Q+(G_t-Q)/N$ cho cặp được chọn.
- **Ghi chú:** N đếm lợi tức được dùng cho riêng cặp, không phải số lượt toàn cục. Tính lùi G không biến lần ghé đầu theo thời gian thành lần gặp đầu trong vòng lặp ngược. $\alpha=1/N$ cho trung bình số học của các lợi tức đã chọn; với $N_0=0$, mẫu đầu có trọng số bằng 1. Một trạng thái xuất hiện hai lần với hai hành động khác nhau vẫn là hai cặp khác nhau.
- **Bố cục:** một khối định nghĩa và hai dòng cập nhật; giả mã nhiều bước tách C05/C06. Có thể hiện G và cập nhật theo fragment bàn phím, không giấu dữ kiện cần đọc.
- **Quan hệ, nguồn, quyết định:** C02 ví dụ trung bình→C03 quy tắc→C04 chuẩn bị lượt ứng dụng và C05 quy trình. `Sửa` L06 tr. 10–11 vốn chưa xác định biến thể; chọn lần ghé đầu theo SB tr. 101, H03 Bài 10.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-C04: Lấy mẫu $\varepsilon$-tham lam bằng dãy số cho trước

- **Vai trò, mục tiêu, thời lượng:** chuẩn bị dữ liệu ứng dụng MC; MT2/MT3; 3 phút. Luận điểm: một quy ước tiêu thụ số rõ ràng xác định lượt tính tay của nguồn 17.
- **Mặt trang:** bảng II B=(0,1),C=(1,0),D=(1,0), ε=1/4. $x_j=(2x_{j-1}+1)\bmod5$, $x_0=1$, $u_j=(x_j+1)/5$. Bốn số đầu $4/5,3/5,1/5,2/5$. Quy tắc: đọc u kiểm thăm dò; nếu u≤1/4 thì đọc thêm số, ≤1/2 chọn 0, còn lại chọn 1; nếu không thăm dò chọn cực đại.
- **Ghi chú:** Tại D, số 4/5 chọn trái cực đại; tại C, số 3/5 chọn trái cực đại; tại B, số 1/5 mở nhánh thăm dò và số 2/5 chọn trái. Lượt là D→C→B→A. j đếm số tiêu thụ nên khác thời điểm t. Đầu mút 1 thuộc nhánh phải khi dùng số phụ để chọn giữa hai hành động. Các bảng hiện tại không đồng hạng; nếu cần chọn trong tập cực đại, số phụ chia thành các khoảng bằng nhau. Dãy tất định ngắn này chỉ tái hiện thao tác. Nó không tạo các mẫu độc lập phân phối đều như nguồn ngẫu nhiên trong định nghĩa xác suất của chính sách.
- **Bố cục:** bảng II nhỏ và chuỗi bốn số, không nhét lời giải cập nhật Q vào đây. Nhãn “Dữ kiện thao tác” không gọi dãy là bằng chứng hội tụ.
- **Quan hệ, nguồn, quyết định:** C03 có quy tắc cập nhật→C04 xác định dữ liệu→C05/C06 quy trình→C07 áp dụng. `Sửa, thêm quy ước` L06 tr. 17; đổi r thành u, đủ thứ tự đọc số để đề có đáp án.
- **Rà soát từng trang 01-10-2026:** `sửa`. Câu mở nêu lý do dùng dãy số: mọi người tái tạo cùng một lượt.

#### L06-C07: Cập nhật từ lượt D–C–B–A

- **Vai trò, mục tiêu, thời lượng:** ứng dụng đầy đủ KN3; MT3; 3 phút. Luận điểm: một lượt hoàn chỉnh cập nhật được giá trị các cặp đã ghé bằng những lợi tức khác nhau.
- **Mặt trang:** `episode-return.svg` với thưởng−1,−1,1000 và G=(998,999,1000). Bảng sau cập nhật từ bảng II: B=(1000,1),C=(999,0),D=(998,0); N của ba ô trái bằng 1, các ô còn lại N=0.
- **Ghi chú:** $G_2=1000$, $G_1=-1+1000=999$, $G_0=-1+999=998$. Mỗi cặp xuất hiện một lần nên lần ghé đầu và mọi lần ghé cho cùng kết quả trên lượt này. Lợi tức 998 của lượt đã cho không phải $q_\pi(D,0)$ của chính sách tham lam bảng I. Chính sách mềm từ bảng mới ưu tiên trái nhưng vẫn thăm dò. Mệnh đề cải thiện dùng giá trị chính xác không bảo đảm từng cập nhật mẫu đều cải thiện giá trị.
- **Bố cục:** quỹ đạo và bảng riêng hai cột, công thức lùi trong ghi chú; không có bảng trả lời hai thuật toán khác nhau ở đây.
- **Quan hệ, nguồn, quyết định:** C04 dữ liệu+C05/C06 quy trình→C07 kết quả→C08 kiểm trường hợp cặp lặp. `Giữ, sửa` L06 tr. 17, dữ kiện đường đi H07 Bài 7; lời giải tính lại, không là đáp án nguyên văn nguồn.
- **Rà soát từng trang 01-10-2026:** `giữ, đổi chỗ`. Đặt ngay sau C04 để ví dụ lấy mẫu và cập nhật liền mạch trước thuật toán tổng quát.

#### L06-C05: Thuật toán điều khiển Monte Carlo: sinh lượt

- **Vai trò, mục tiêu, thời lượng:** nửa đầu quy trình đầy đủ; MT3; 3 phút. Luận điểm: dữ liệu của một lượt phải hoàn chỉnh trước khi tạo lợi tức MC.
- **Mặt trang:** đầu vào gồm môi trường tương tác, tập hành động, phân phối đầu, γ, bảng $Q_0$ hữu hạn, lịch $0<\varepsilon_k\le1$ và số nguyên dương K lượt hoàn chỉnh. Đầu ra: Q và chính sách mềm từ Q. Bước 1: đặt $Q\leftarrow Q_0$, $N\leftarrow0$, $k\leftarrow1$. Bước 2, đầu mỗi lượt: xóa quỹ đạo và bảng chỉ số ghé đầu f, giữ Q và N; đặt t=0, lấy trạng thái đầu theo phân phối đã cho; đặt $\pi_k$ là $\varepsilon_k$-tham lam theo Q, giữ chính sách này trong lượt. Bước 3: lặp việc chọn $A_t$ theo $\pi_k$, thực hiện hành động, nhận $R_{t+1},S_{t+1}$, lưu chuyển và chỉ số lần ghé đầu nếu cặp chưa có trong $f$, rồi mới tăng $t$ cho tới kết thúc. Tính lùi $G_t$ từ $G_T=0$.
- **Ghi chú:** Mỗi chính sách sinh lượt được giả thiết dẫn tới kết thúc gần chắc chắn và có lợi tức khả tích. Biết tập hành động không có nghĩa biết mô hình chuyển p. Bảng f chỉ chứa thông tin của lượt hiện tại; Q và N tích lũy qua các lượt. Khi đi thuận, nếu $(S_t,A_t)$ chưa có trong $f$, đặt $f(S_t,A_t)=t$ trước khi tăng $t$; lần xuất hiện sau không ghi đè chỉ số này. Không đọc hành động tại trạng thái kết thúc. Tính G ngược vẫn dùng chỉ số đã lưu; sửa này hợp nhất M01/RL-01. Một tiền tố bị cắt trước kết thúc chưa là lượt hoàn chỉnh cho quy trình. Q giữ nguyên trong lúc thu thập và tính G, nên $\pi_k$ không đổi giữa lượt.
- **Bố cục/hình thức:** hộp đầu vào ngắn và giả mã ba bước; chi tiết giả thiết ở ghi chú và một dòng trên mặt. Không ảnh hóa giả mã; C06 tiếp đúng bước 4.
- **Quan hệ, nguồn, quyết định:** C04 có một lượt xác định→C05 thu thập/tạo G→C06 chọn mẫu/cập nhật/cải thiện. `Tách, hoàn thiện` L06 tr. 10–11, SB tr. 101. Tách vì đầu vào và toàn bộ vòng lặp không đọc được nếu ép một trang.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề; đầu vào nêu ví dụ lịch $\varepsilon_k=1/k$ (nguồn tr. 11), ghi chú nối sang phần hội tụ.

#### L06-C06: Thuật toán điều khiển Monte Carlo: cập nhật

- **Vai trò, mục tiêu, thời lượng:** nửa sau quy trình; MT3; 3 phút. Luận điểm: cập nhật các cặp lần ghé đầu rồi mới xây dựng chính sách cho lượt kế tiếp.
- **Mặt trang:** tiếp quy trình với bước 4: mỗi cặp xuất hiện trong lượt dùng $t=f(s,a)$; tăng $N(s,a)$ rồi cập nhật Q bằng $G_t$ với bước học $1/N(s,a)$. Bước 5: tạo chính sách $\varepsilon_k$-tham lam theo Q mới. Bước 6: nếu k<K, đặt $k\leftarrow k+1$ và trở lại đầu lượt; nếu k=K, trả Q và chính sách vừa tạo. Bộ nhớ bảng và lượt là $O(M+T)$; xử lý lợi tức/lần ghé đầu là $O(T)$.
- **Ghi chú:** M là tổng số cặp hợp lệ, T là độ dài lượt hiện tại. Chi phí chọn hoặc cải thiện chính sách còn bao gồm việc tìm cực đại trong các hành động của trạng thái liên quan. Lưu f tránh việc kiểm lại tiền tố ở mỗi bước, vốn có thể tốn $O(T^2)$. K là ngân sách lượt hoàn chỉnh, không phải tiêu chuẩn hội tụ. Q và N được giữ khi sang lượt mới; chỉ quỹ đạo và f được đặt lại. Chính sách mới không thay chính sách đã sinh lượt vừa hoàn tất. Trung bình dưới π cố định không chứng minh hội tụ cho một chuỗi chính sách đang thay đổi.
- **Bố cục:** số bước tiếp C05, công thức đã có ở C03 chỉ nhắc bằng nhãn; có thể giữ N/Q một dòng. Không thêm sơ đồ trùng chức năng.
- **Quan hệ, nguồn, quyết định:** C05 tạo G và f→C06 hoàn tất thuật toán→C07 chạy trên dữ liệu C04. `Sửa, thêm đặc tả dừng/chi phí` L06 tr. 10–11 và SB tr. 99–103; chi phí suy trực tiếp từ giả mã.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-C08: Kiểm tra lần ghé đầu của cặp

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch C; MT3; 3 phút:75 giây tính,45 giây trả lời,60 giây chữa. Luận điểm: một cặp có thể xuất hiện nhiều lần trong cùng lượt nhưng chỉ một lợi tức được dùng ở lần ghé đầu.
- **Mặt trang — Câu hỏi:** trong cùng môi trường, γ=1,N0(D,0)=0, lượt D→C→D→C→B→A có hành động 0,1,0,0,0 và thưởng−1,−1,−1,−1,1000. Tính Q(D,0) và N(D,0) sau MC lần ghé đầu. Tính Q(D,0) nếu dùng mọi lần ghé và trung bình mẫu.
- **Ghi chú/đáp án:** Cặp (D,0) ở t=0 và t=2, có lợi tức tương ứng 996 và 998. Lần ghé đầu chỉ lấy 996, N=1. Mọi lần ghé lấy trung bình (996+998)/2=997, N=2. Toàn dãy lợi tức là 996,997,998,999,1000. Hai lần C dùng hai hành động khác nhau; cặp (C,0) vẫn có lần ghé đầu dù trước đó đã ghé (C,1).
- **Tiêu chí:** chỉ số đầu theo chiều thời gian; mẫu số theo cặp/mẫu được dùng; không đếm Q0 như dữ liệu. Câu cuối của lời giải cho thấy MC phải có cả phần cuối của lượt.
- **Quan hệ, nguồn, quyết định:** C07 không có cặp lặp→C08 kiểm ranh giới→D01 cần cập nhật khi thiếu phần cuối. `Thêm` quỹ đạo sư phạm suy từ môi trường L06 tr. 15, chuẩn lần ghé đầu SB tr. 101; đã kiểm số hữu tỉ. Không thêm môi trường hoặc SVG riêng. Sau rà SV-02, nhãn “Câu hỏi:” là dòng khối đứng trước danh sách; câu hỏi và lời giải giữ nguyên.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.
- **Sửa sau rà soát độc lập 01-10-2026:** Câu 2 dẫn quy tắc mọi lần ghé của Bài 05.

## D. Sarsa

#### L06-D01: Từ Monte Carlo sang cập nhật một bước

- **Vai trò, mục tiêu, thời lượng:** vấn đề và trực giác KN4; MT4; 2 phút. Luận điểm: một giá trị tiếp nối ước lượng cho phép cập nhật trước khi quan sát toàn bộ lợi tức.
- **Mặt trang:** tiền tố D→C với thưởng−1, lượt còn tiếp. Hai thành phần bằng lời: “thưởng vừa nhận” và “giá trị của hành động sẽ thực hiện tại C”. Nhãn “Sarsa dùng hành động kế tiếp đã lấy mẫu”.
- **Ghi chú:** MC phải đợi phần thưởng cuối để có lợi tức hoàn chỉnh. TD(0) đã dùng V của trạng thái tiếp; điều khiển bằng giá trị hành động cần biết cả trạng thái và hành động tiếp. Ước lượng tiếp nối có thể sai. Khả năng cập nhật sớm không tự bảo đảm hiệu quả mẫu tốt hơn trên mọi bài toán.
- **Bố cục:** tiền tố của sơ đồ chuỗi và một hộp tiếp nối chưa quan sát; không đặt giá trị 0 vào C vì dữ liệu bị cắt.
- **Quan hệ, nguồn, quyết định:** C08 giới hạn chờ→D01 cơ chế một bước→D02 cung cấp dữ liệu tính. `Gộp, sửa` L06 tr. 5/9/12, SB §6.2 tr. 124 và §6.4 tr. 129.
- **Rà soát từng trang 01-10-2026:** `sửa`. Hộp nêu tên Sarsa lấy từ bộ năm $(S,A,R,S',A')$ (nguồn tr. 13); ghi chú nêu dạng cập nhật chung và câu hỏi chọn mục tiêu (nguồn tr. 12).
- **Sửa sau rà soát độc lập 01-10-2026:** Dạng cập nhật chung $Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[\text{mục tiêu}-Q(S_t,A_t)]$ lên mặt trang (nguồn tr. 12).

#### L06-D02: Năm mẫu chuyển dùng chung

- **Vai trò, mục tiêu, thời lượng:** dữ kiện ví dụ KN4/KN5; MT4/MT5; 2 phút. Luận điểm: so sánh mục tiêu cần cố định khởi tạo và mẫu chuyển.
- **Mặt trang:** bảng I B=(0,1),C=(1,0),D=(0,1); γ=1,α=0.8. Năm hàng: (1)D,0,−1,C,0; (2)C,0,−1,B,0; (3)B,0,1000,A,không có; (4)D,1,10,E,không có; (5)D,0,−1,C,0. Tên cột $S,A,R,S',A'$; đường phân nhóm sau 3 và 4.
- **Ghi chú:** ba lượt: D–C–B–A; D–E; tiền tố D–C. Khởi động lại D sau A/E. Hành động được cho trước, đều có xác suất dương dưới hành vi ε-tham lam với ε=1/4; không phải một đường duy nhất suy từ ε hoặc bộ số nguồn 17. $A'$ mẫu 5 đã lấy trước cập nhật dù ngân sách dừng trước khi thực hiện nó. Hai thuật toán sẽ đặt lại và chạy riêng từ bảng I.
- **Bố cục:** bảng 5 hàng, tên cột gọn; bảng I thu gọn bên trái hoặc dải trên. Không đưa kết quả lên trang dữ kiện.
- **Quan hệ, nguồn, quyết định:** D01 nêu cần một bước→D02 dữ liệu→D03 tính hai bước đầu. `Sửa, bổ sung` L06 tr. 18/21 thiếu mẫu; dùng chuỗi L06 tr. 15 và quỹ đạo H07 Bài 7, không lấy chuỗi Sarsa lỗi H07 Bài 8.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.
- **Sửa sau rà soát độc lập 01-10-2026:** Chú thích: các hành động cho trước có xác suất dương dưới $\varepsilon$-tham lam, $\varepsilon=1/4$ (nguồn tr. 17–18).

#### L06-D03: Hai cập nhật Sarsa đầu tiên

- **Vai trò, mục tiêu, thời lượng:** ví dụ tính tay trước quy tắc tổng quát; MT4; 3 phút. Luận điểm: Sarsa dùng giá trị của hành động kế tiếp đã chọn, kể cả khi hành động ấy chưa đạt cực đại.
- **Mặt trang:** mẫu 1, D0→C với A'=0: Q cũ bằng 0, mục tiêu −1+1=0, Q mới bằng 0. Mẫu 2, C0→B với A'=0: Q cũ bằng 1, giá trị tiếp nối Q(B,0)=0, mục tiêu −1, sai lệch −2; Q mới bằng 1+0.8(−2)=−0.6.
- **Ghi chú:** bảng sau mẫu 1 vẫn bằng bảng I. Tại B, hành động 1 có giá trị bằng 1 nhưng dữ liệu đã chọn hành động 0. Dùng giá trị 1 thay 0 tại mẫu 2 sẽ tạo mục tiêu của thuật toán khác. Mọi giá trị trong phép tính mẫu 2 lấy từ bảng trước cập nhật mẫu này; chỉ ô C0 đổi, các ô khác giữ nguyên.
- **Bố cục/hình:** `sarsa-target.svg` cho mẫu 2; mẫu 1 là một dòng tính ngắn. Ba đại lượng Q cũ, mục tiêu và Q mới có nhãn riêng; trạng thái của bảng phải rõ.
- **Quan hệ, nguồn, quyết định:** D02 cung cấp dữ kiện; D03 tính cơ chế; D04 khái quát bằng ký hiệu. `Tách, thêm lời giải` từ L06 tr. 13/18, SB tr. 129; kết quả −3/5 đã kiểm bằng số hữu tỉ.
- **Rà soát từng trang 01-10-2026:** `sửa`. Thay hai underbrace KaTeX (nét vượt khung) bằng một dòng văn bản có cùng số liệu.

#### L06-D04: Quy tắc cập nhật Sarsa

- **Vai trò, mục tiêu, thời lượng:** hình thức KN4; MT4; 3 phút. Luận điểm: mục tiêu Sarsa là thưởng cộng giá trị hành động tiếp nối, với nhánh riêng khi kết thúc.
- **Mặt trang:** nếu S' chưa kết thúc, chọn A' theo chính sách từ Q_t rồi đặt $Y_t=R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$; nếu kết thúc, đặt $Y_t=R_{t+1}$. Sau đó $\delta_t=Y_t-Q_t(S_t,A_t)$ và $Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t\delta_t$; các ô khác giữ nguyên.
- **Ghi chú:** $Q_t$ là bảng ngay trước cập nhật; bộ năm biến đủ cho nhánh chưa kết thúc. Chính sách chọn A' cũng là chính sách được đánh giá, nên Sarsa là phương pháp theo chính sách. Quy tắc từ $Q_t$ lấy $A_{t+1}$ trước cập nhật; $A_t$ đã được chọn ở bước trước. Với mẫu 2, $Y=-1$ và $\delta=-2$. Sai lệch δ so sánh mục tiêu với ước lượng, chưa là sai số thật so với giá trị đúng.
- **Bố cục:** hai nhánh mục tiêu rõ, công thức cập nhật đặt dưới; giải thích tên Sarsa từ bộ năm biến trong ghi chú.
- **Quan hệ, nguồn, quyết định:** D03 có số; D04 tổng quát hóa; D05 xác định thứ tự thực hiện. `Sửa` L06 tr. 12–14, SB tr. 129–130; nhánh kết thúc tránh chọn hành động không tồn tại.
- **Rà soát từng trang 01-10-2026:** `sửa`. Câu cuối gọi tên học theo chính sách (on-policy) theo nguồn tr. 13.
- **Sửa sau rà soát độc lập 01-10-2026:** Câu cuối: "Sarsa học theo chính sách: hành động kế tiếp được lấy từ chính sách đang học" (không kèm tiếng Anh; dạng đầy đủ ở E01).

#### L06-D05: Thuật toán Sarsa: bước trong lượt

- **Vai trò, mục tiêu, thời lượng:** phần đầu quy trình đầy đủ KN4; MT4; 3 phút. Luận điểm: chọn A' trước cập nhật và giữ chính hành động ấy để tiếp tục tương tác.
- **Mặt trang:** đầu vào gồm môi trường, tập hành động, phân phối đầu, γ, Q0, lịch bước học/thăm dò và ngân sách cập nhật; đầu ra là Q và chính sách ε-tham lam hiện hành. Bước 1: khởi tạo Q, bộ đếm theo cặp, bộ đếm ngân sách; lấy S0 và A0 theo chính sách mềm. Bước 2: chọn bước học cho cặp (S,A) từ thông tin hiện có, thực hiện A, nhận R,S'. Bước 3 khi S' chưa kết thúc: chọn A' từ Q hiện có, tính Y, cập nhật một ô, tăng các bộ đếm; nếu còn ngân sách, gán (S,A)←(S',A') và tiếp tục.
- **Ghi chú:** mẫu chuyển tuân theo môi trường. Bước học có thể là hằng số cho bài tính hoặc phụ thuộc số cập nhật riêng của cặp khi phân tích. A' chỉ được lấy một lần trước cập nhật. Không lấy lại A' từ bảng mới, vì hành động được thực hiện có thể khác hành động đã dùng trong mục tiêu. Vẫn phải chọn A' ở bước cuối chưa kết thúc để tính Y; nếu dừng theo ngân sách thì không thực hiện nó. Bộ đếm cặp và bộ đếm ngân sách tăng sau mỗi chuyển được dùng để cập nhật.
- **Bố cục:** đầu vào/đầu ra gọn và ba bước; D06 tiếp nhánh kết thúc và điều kiện dừng. Chi tiết chọn bước học và giữ A' nằm trong ghi chú. Không giả định biết mô hình chuyển.
- **Quan hệ, nguồn, quyết định:** D04 cho quy tắc; D05 xác định thứ tự; D06 hoàn tất nhánh còn lại. `Tách, hoàn thiện` L06 tr. 14, SB tr. 129–130; ngân sách và bộ đếm là đặc tả bổ sung.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-D06: Thuật toán Sarsa: kết thúc và dừng

- **Vai trò, mục tiêu, thời lượng:** phần cuối quy trình KN4; MT4/MT6; 3 phút. Luận điểm: kết thúc một lượt và hết ngân sách toàn bộ là hai điều kiện khác nhau.
- **Mặt trang:** nhánh kết thúc: nếu S' kết thúc, đặt Y=R, cập nhật Q và tăng bộ đếm, không chọn A'. Chỉ khi S' kết thúc và còn ngân sách mới khởi động lượt mới theo phân phối đầu và lấy A từ bảng hiện có; điều kiện được ghi trực tiếp trên mặt trang theo SV-01. Nếu hết ngân sách sau cập nhật, trả Q và chính sách ε-tham lam hiện hành. Bộ nhớ bảng là $O(M)$; mục tiêu dùng một tra cứu sau khi có A'.
- **Ghi chú:** D→E cho mục tiêu 10 vì E kết thúc. D→C ở cuối ngân sách vẫn có giá trị tiếp nối vì C chưa kết thúc. Chọn ε-tham lam có thể cần tìm cực đại trên m (s) hành động; không kết luận toàn thuật toán có chi phí O(1) chỉ từ một tra cứu. Q và bộ đếm theo cặp dùng O(M) bộ nhớ, không cần lưu cả lượt. Tham số α=.8, γ=1 của bài tính chỉ xác định cập nhật; bảo đảm hội tụ được xét riêng trong miền MDP có chiết khấu.
- **Bố cục:** nhánh bằng HTML hoặc các bước 4–6 liền D05; không tạo SVG thuật toán riêng nếu khối giả mã đọc rõ. Phân tích chi phí tách khỏi điều kiện dừng.
- **Quan hệ, nguồn, quyết định:** D05 xử lý bước chưa kết thúc; D06 xử lý kết thúc/dừng; D07 áp dụng hai mẫu kết thúc. `Sửa, thêm` L06 tr. 14/18, SB tr. 129; điều kiện dừng thực hành không được gắn nhãn hội tụ.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-D07: Sarsa tại trạng thái kết thúc

- **Vai trò, mục tiêu, thời lượng:** ứng dụng KN4; MT4; 3 phút. Luận điểm: khi trạng thái kế tiếp kết thúc, mục tiêu chỉ có thưởng; ô được cập nhật vẫn là cặp trạng thái–hành động trước chuyển.
- **Mặt trang:** mẫu 3, B0→A: $0+0.8(1000-0)=800$. Mẫu 4, D1→E: $1+0.8(10-1)=8.2$. Bảng trước mẫu 5: B=(800,1), C=(−0.6,0), D=(0,8.2).
- **Ghi chú:** không có A' ở A/E; không cộng một giá trị tiếp nối bằng 1000 hoặc 10. Phần thưởng cuối đã được nhận trên chuyển, giá trị tiếp nối bằng 0. Sau mẫu 3, khởi động lại D nhưng giữ Q. Ô C0 vẫn bằng −.6 từ mẫu 2, vì chưa có mẫu cập nhật lại ô ấy.
- **Bố cục:** hai phép tính và bảng 3×2; giải thích chỉ số trong ghi chú. Chưa đưa đáp án mẫu 5 để D08 đo khả năng dùng bảng đã thay đổi.
- **Quan hệ, nguồn, quyết định:** D06 xác định nhánh kết thúc; D07 áp dụng; D08 kiểm bước chưa kết thúc ở cuối ngân sách. `Thêm lời giải` trên dữ kiện hoàn thiện L06 tr. 18, công thức SB tr. 129; 800 và 41/5 đã kiểm.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-D08: Kiểm tra cập nhật Sarsa từ tiền tố

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch D; MT4/MT6; 3 phút: 60 giây tính, 45 giây trả lời, 75 giây chữa. Luận điểm: dừng lấy mẫu không xóa giá trị tiếp nối của trạng thái chưa kết thúc.
- **Mặt trang — Câu hỏi:** cho Q(D,0)=0 và Q(C,0)=−0.6 sau bốn cập nhật; mẫu tiếp theo $(D,0,-1,C,0)$, γ=1, α=.8. Tính Y, δ và Q mới(D,0). Giải thích A' được lấy trước hay sau cập nhật, có được lấy lại từ bảng mới hay không, và việc dừng ngân sách có làm giá trị tiếp nối bằng 0 hay không.
- **Ghi chú/đáp án:** Y=−1+(−.6)=−1.6; δ=−1.6−0=−1.6; Q mới=−1.28. C vẫn chưa kết thúc. A'=0 đã lấy trước cập nhật để xác định mục tiêu. Nếu tiếp tục tương tác, phải giữ chính hành động đó; lấy lại từ bảng mới có thể làm hành động thực hiện khác hành động đã dùng trong mục tiêu. Vì hết ngân sách, hành động ấy không cần được thực hiện. MC chưa có lợi tức hoàn chỉnh cho lượt thứ ba, còn Sarsa có đủ dữ kiện cho mục tiêu một bước.
- **Tiêu chí:** dùng C0=−.6 từ bảng đã cập nhật, không dùng Q0(C,0)=1; không lấy max (C) thay cho A' đã chọn; giải thích ngân sách khác kết thúc lượt.
- **Quan hệ, nguồn, quyết định:** D07 chuẩn bị bảng; D08 hoàn tất năm mẫu; E01 tách mục tiêu khỏi hành động hành vi. `Thêm` kiểm tra trên dữ kiện đã chốt cho L06 tr. 18; kết quả −32/25 đã kiểm, không cần SVG mới.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

## E. Q-learning

#### L06-E01: Chính sách hành vi và chính sách đích

- **Vai trò, mục tiêu, thời lượng:** vấn đề và trực giác KN5; MT2/MT5; 2 phút. Luận điểm: hành động tạo dữ liệu và hành động dùng để hình thành mục tiêu có thể do hai chính sách khác nhau xác định.
- **Mặt trang:** `behavior-target.svg` với b chọn hành động tương tác, mẫu chuyển cập nhật Q, chính sách đích tham lam rút từ Q. Hai nhãn: “hành vi b: sinh dữ liệu”, “đích π: xác định giá trị được học”.
- **Ghi chú:** mẫu 2 Sarsa đã dùng hành động trái tại B dù phải có giá trị bảng lớn hơn. Q-learning dùng cực đại trong mục tiêu nhưng vẫn cho hành vi thăm dò. Theo/khác chính sách được xác định bằng hai vai, không bằng mức độ hai phân phối gần nhau. Tính cực đại trên bảng không cần mô hình chuyển. Q-learning tính trực tiếp cực đại theo các hành động, nên không cần lấy mẫu hành động đích để ước lượng giá trị tiếp nối.
- **Bố cục:** hai đường có nhãn và kiểu nét khác nhau; nét đứt bao gồm tạo mục tiêu và cập nhật bảng theo R02. Không dùng màu làm tín hiệu duy nhất, không có tỉ số trong hình.
- **Quan hệ, nguồn, quyết định:** D08 có mục tiêu phụ thuộc A'→E01 tách hai vai→E02 một bước số thay đích. `Sửa, gộp` L06 tr. 8/19/20; SB tr. 103–105 và 131.
- **Rà soát từng trang 01-10-2026:** `sửa`. Câu mở nêu vấn đề: mục tiêu Sarsa dùng hành động thăm dò; định nghĩa học theo chính sách ($b=\pi$) và khác chính sách ($b\ne\pi$) theo nguồn tr. 8; hình cỡ ngắn.
- **Sửa sau rà soát độc lập 01-10-2026:** Nhắc Monte Carlo và Sarsa ở các phần trước là học theo chính sách.

#### L06-E02: Một cập nhật Q-learning

- **Vai trò, mục tiêu, thời lượng:** ví dụ tính tay trước HT6; MT5; 3 phút. Luận điểm: cùng chuyển tiếp và bảng trước cập nhật, thay hành động lấy mẫu bằng cực đại làm đổi mục tiêu.
- **Mặt trang:** đặt lại **bảng I** riêng cho Q-learning. Mẫu 1 vẫn cho Q(D,0)=0. Mẫu 2 $(C,0,-1,B)$, bảng B=(0,1): tiếp nối $\max(0,1)=1$, mục tiêu−1+1=0, Q mới (C,0)=1+0.8(0−1)=0.2. Bên cạnh ghi mục tiêu Sarsa của cùng bước bằng−1.
- **Ghi chú:** Q-learning không dùng bảng C0=−.6 sau Sarsa làm khởi tạo. Tại bước 2, hai bản có cùng bảng trước cập nhật; khác biệt chỉ ở cách chọn giá trị tiếp nối. Cực đại 1 là giá trị lớn nhất trong bảng ước lượng, chưa là giá trị tốt nhất thật. Hành động thực tế tiếp theo trong dữ liệu vẫn là 0; nó không bị thay bằng 1 trong quỹ đạo.
- **Bố cục/hình:** `q-learning-target.svg` cùng tỷ lệ với hình Sarsa; công thức số đủ lớn, không chèn toàn bộ năm mẫu.
- **Quan hệ, nguồn, quyết định:** E01 hai vai→E02 số→E03 công thức. `Sửa, thêm lời giải` L06 tr. 20–21; bảng II nguồn 21 đổi sang I đã ghi ánh xạ; kết quả 1/5 kiểm bằng số hữu tỉ.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-E03: Quy tắc cập nhật Q-learning

- **Vai trò, mục tiêu, thời lượng:** hình thức KN5; MT5; 3 phút. Luận điểm: mục tiêu cực đại được tính trực tiếp từ các hành động hợp lệ của trạng thái kế tiếp.
- **Mặt trang:**
  $$Y_t=\begin{cases}R_{t+1}+\gamma\max_{a\in\mathcal A(S_{t+1})}Q_t(S_{t+1},a),&S_{t+1}\in\mathcal S,\\R_{t+1},&S_{t+1}\text{ kết thúc}.\end{cases}$$
  $Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t[Y_t-Q_t(S_t,A_t)]$. Các ô khác giữ nguyên; dữ liệu cần là bộ bốn $(S_t,A_t,R_{t+1},S_{t+1})$.
- **Ghi chú:** Tất cả ô bên phải lấy từ $Q_t$ trước cập nhật. Biết tập hành động là giả thiết biểu diễn bảng; việc lấy cực đại không cần xác suất chuyển. Q-learning hướng tới $q_*$ dưới các điều kiện về độ phủ, bước học và môi trường; bảng hữu hạn mẫu chưa tự bằng $q_*$. Tại trạng thái kết thúc, tập hành động rỗng nên mục tiêu được định nghĩa riêng bằng thưởng. Với mẫu C0→B và hàng B=(0,1), phép tính cho Q mới(C,0)=0.2.
- **Bố cục:** mục tiêu hai nhánh và cập nhật ở hai khối; không thêm công thức IS. Ký hiệu tiếng Việt trong cases phải được kiểm KaTeX lúc dựng.
- **Quan hệ, nguồn, quyết định:** E02 số→E03 quy tắc→E04/E05 thứ tự thao tác. `Sửa` L06 tr. 20, SB tr. 131; xử lý trạng thái kết thúc tường minh.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-E04: Thuật toán Q-learning: lấy mẫu và cập nhật

- **Vai trò, mục tiêu, thời lượng:** phần đầu quy trình đầy đủ; MT5; 3 phút. Luận điểm: hành vi chọn hành động, còn mục tiêu được tính mà không lấy mẫu hành động kế tiếp.
- **Mặt trang:** đầu vào giống Sarsa, nhưng hành vi b được chỉ rõ; đầu ra Q và chính sách tham lam từ Q. Bước 1: khởi tạo Q, bộ đếm và ngân sách; bắt đầu lượt ở S. Bước 2: chọn A theo b, chọn bước học cho lần cập nhật tiếp của cặp từ thông tin hiện có, thực hiện A, nhận R,S'. Bước 3 khi S' chưa kết thúc: tính cực đại trên hàng S' của Q hiện tại, tạo Y, cập nhật một ô; tăng các bộ đếm; nếu tiếp tục, gán S←S' rồi chọn hành động mới theo b.
- **Ghi chú:** b có thể là ε-tham lam từ bảng hiện hành, nhưng hành động kế tiếp không là đầu vào của mục tiêu. Quy trình này chọn hành động cho lần tương tác sau sau khi đã cập nhật, khác cách Sarsa giữ A' chọn trước cập nhật. Hai thuật toán có thể tạo quỹ đạo khác khi chạy tự do; bảng dữ liệu chung chỉ là đối chiếu có điều kiện trên mẫu đã cho.
- **Bố cục:** khối đầu vào/đầu ra gọn và ba bước; E05 nối nhánh kết thúc/dừng. Không dùng ảnh cho giả mã.
- **Quan hệ, nguồn, quyết định:** E03 công thức→E04 lấy mẫu/cập nhật→E05 hoàn chỉnh. `Thêm` giả mã theo SB tr. 131 để hoàn thiện L06 tr. 20 chỉ có công thức; không tự thêm chương trình.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-E05: Thuật toán Q-learning: kết thúc và chi phí

- **Vai trò, mục tiêu, thời lượng:** phần cuối quy trình; MT5/MT6; 2 phút. Luận điểm: nhánh trạng thái kết thúc chỉ dùng thưởng, còn phép cực đại tạo chi phí tại trạng thái chưa kết thúc.
- **Mặt trang:** nếu S' kết thúc, đặt Y=R, cập nhật Q và tăng bộ đếm. Chỉ khi S' kết thúc và còn ngân sách mới khởi động lượt mới; điều kiện được ghi trực tiếp theo SV-01. Nếu hết ngân sách, trả Q cùng chính sách tham lam ở cả hai nhánh. Nếu ngừng tại trạng thái chưa kết thúc, mục tiêu của bước cuối vẫn chứa cực đại. Bộ nhớ $O(M)$; tìm cực đại trực tiếp tốn $O(m(S'))$.
- **Ghi chú:** cả chi phí chọn hành vi ε-tham lam lẫn chi phí tạo mục tiêu có thể cần duyệt hành động. Không kết luận toàn bộ Sarsa luôn O(1) và Q-learning luôn chậm hơn chỉ từ một biểu thức. Có thể duy trì cấu trúc cực đại để đổi chi phí, nhưng bài dùng triển khai bảng trực tiếp. Ngân sách hữu hạn không là tiêu chuẩn hội tụ. Trạng thái kết thúc không có hàng hành động dùng trong cực đại.
- **Bố cục:** nhánh bổ sung bước 4–6 liên tục với E04; dòng chi phí tách khỏi giả mã để không trộn điều kiện toán với tiêu chuẩn chạy.
- **Quan hệ, nguồn, quyết định:** E04 nhánh thường→E05 trạng thái kết thúc/dừng→E06 chạy đủ năm mẫu. `Thêm, sửa` từ SB tr. 131 và L06 tr. 20–21; chi phí là suy luận từ biểu diễn bảng.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-E06: Sarsa và Q-learning trên cùng năm mẫu

- **Vai trò, mục tiêu, thời lượng:** ứng dụng đầy đủ KN5; MT4/MT5; 3 phút. Luận điểm: giá trị tiếp nối tại B tạo hai mục tiêu cho cập nhật (C,0), rồi giá trị tại C được dùng khi cập nhật (D,0).
- **Mặt trang:** bảng năm hàng, mỗi hàng ghi ô cập nhật và kết quả Sarsa/Q-learning: (1)D0:0/0; (2)C0:−.6/.2; (3)B0:800/800; (4)D1:8.2/8.2; (5)D0:−1.28/−.64. Dòng tính mẫu 5 của Q-learning: mục tiêu−1+max (.2,0)=−.8, Q mới=0+.8(−.8)=−.64.
- **Ghi chú:** từng cột chạy từ bản sao riêng của bảng I và dùng kết quả cập nhật trước đó trong cột. Bảng cuối Sarsa B=(800,1),C=(−.6,0),D=(−1.28,8.2); Q-learning B=(800,1),C=(.2,0),D=(−.64,8.2). Mẫu 2 dùng khác hành động trong mục tiêu; mẫu 5 truyền khác biệt tại C về D. Hai giá trị sau hữu hạn mẫu không xếp hạng hiệu quả hai thuật toán. Lượt thứ ba chưa đủ cho MC.
- **Bố cục:** một bảng HTML có 5 hàng; bảng cuối đầy đủ ở ghi chú/học liệu để không lặp sáu ô trên mặt trang. Giữ số thập phân nhất quán, phân số chính xác trong ghi chú.
- **Quan hệ, nguồn, quyết định:** E05 quy trình→E06 kết quả→E07 điều kiện dữ liệu tạo các cập nhật. `Sửa, bổ sung lời giải` L06 tr. 18/21, cùng dữ liệu đã chốt; đối chiếu cách giữ khởi tạo chung ST26 tr. 85/87.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-E07: Dữ liệu hành vi trong Q-learning

- **Vai trò, mục tiêu, thời lượng:** ứng dụng vai hành vi/đích, giới hạn KN5; MT2/MT5/MT6; 3 phút. Luận điểm: dữ liệu từ hành vi khác dùng được khi còn phản ánh đúng môi trường và đủ phủ các cặp cần học.
- **Mặt trang:** ba yêu cầu ngắn: mẫu chuyển đúng MDP đang xét; hành vi cung cấp dữ liệu tại các cặp cần học; mục tiêu Q-learning tính cực đại từ bảng. Dòng kết luận: “Tập dữ liệu hữu hạn không tự cung cấp bảo đảm hội tụ của quá trình lấy mẫu vô hạn.”
- **Ghi chú:** để ước lượng chính sách π từ hành vi b nói chung, hành động có xác suất dương theo π phải được b hỗ trợ. Điều này tại một trạng thái khác với việc mọi trạng thái/cặp được đạt tới vô hạn. Q-learning một bước không ước lượng kỳ vọng hành động tiếp theo bằng A' lấy từ b nên không cần tỉ số. Dữ liệu cũ từ cùng MDP có thể dùng, nhưng phát lại vô hạn một tập hữu hạn không tự khôi phục động lực thật. Nhãn khác chính sách không bảo đảm ưu thế hiệu quả mẫu trên mọi bài toán.
- **Bố cục/hình:** tái dùng `behavior-target.svg` với nhãn mẫu/đích; chú giải và desc của nét đứt nêu đủ tạo mục tiêu và cập nhật bảng theo R02. Không thêm hình về replay hoặc học sâu.
- **Quan hệ, nguồn, quyết định:** E06 đối chiếu mẫu hữu hạn→E07 điều kiện dùng mẫu→E08 kiểm mục tiêu trước khi sang F kiểm bảo đảm. `Sửa` L06 tr. 8/19/28; SB tr. 103–105/131, WD92 tr. 282.
- **Rà soát từng trang 01-10-2026:** `sửa`. Mặt trang nêu lý do Q-learning một bước không cần hệ số lấy mẫu quan trọng (nguồn tr. 19); $b$ chỉ quyết định cặp được cập nhật; điều kiện MDP và độ phủ trong hộp; câu về tập dữ liệu hữu hạn chuyển vào ghi chú; hình giới hạn 200px.
- **Sửa sau rà soát độc lập 01-10-2026:** Mặt trang chỉ nêu mục tiêu cực đại không dùng hành động kế tiếp của $b$ và $b$ quyết định cặp được cập nhật cùng tần suất; trường hợp cần hệ số lấy mẫu quan trọng chuyển vào ghi chú diễn giả và ghi chú bài giảng.

#### L06-E08: Kiểm tra mục tiêu Sarsa và Q-learning

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch E; MT2/MT5; 3 phút:60 giây tính,45 giây giải thích,75 giây chữa. Luận điểm: khác biệt xuất phát từ giá trị hành động được dùng trong mục tiêu, không chỉ từ tên phương pháp.
- **Mặt trang — Câu hỏi:** cho cùng một bảng tại B với Q(B,0)=800,Q(B,1)=1; chuyển$(C,0,-1,B)$, γ=1; Sarsa đã chọn A'=1. Tính mục tiêu Sarsa và Q-learning. Nêu điều kiện để hai mục tiêu trùng nhau tại một trạng thái chưa kết thúc khi dùng cùng bảng và γ=1.
- **Ghi chú/đáp án:** YSarsa=−1+1=0; YQ=−1+800=799. Hai mục tiêu bằng nhau khi $Q(B,A')=\max_aQ(B,a)$, tức A' thuộc tập cực đại; đồng hạng vẫn có thể thỏa. Nếu trạng thái kết thúc, cả hai dùng R; đó là nhánh riêng. Bằng nhau một bước không suy toàn bộ hai quá trình có cùng quỹ đạo hay hội tụ tới cùng chính sách hành vi.
- **Tiêu chí:** đọc A'=1 thay vì tự chọn 0 cho Sarsa; tính đúng cả hai mục tiêu; phát biểu điều kiện theo giá trị/tập cực đại, không bắt buộc duy nhất một hành động.
- **Quan hệ, nguồn, quyết định:** E07 hai vai→E08 đo cơ chế→F01 giới hạn suy luận từ phép tính. `Thêm` bài kiểm tra suy từ bảng B chung đã tính ở D07/E06, quy tắc L06 tr. 13/20; không là mẫu thứ sáu đã có trong nguồn.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

## F. Điều kiện bảo đảm

#### L06-F01: Giả thiết chung của các định lý hội tụ

- **Vai trò, mục tiêu, thời lượng:** vấn đề và trực giác KN6; MT6; 3 phút. Luận điểm: các cập nhật hữu hạn xác nhận cơ chế, còn hội tụ cần giả thiết về quá trình sinh dữ liệu và tham số dài hạn.
- **Mặt trang:** miền định lý được xét: MDP hữu hạn, có động lực không đổi theo thời gian; phần thưởng bị chặn, $0\le\gamma<1$; Q0 hữu hạn, mẫu theo đúng động lực môi trường. Hai yêu cầu còn phải kiểm: mọi cặp được cập nhật đủ lâu và bước học thích hợp.
- **Ghi chú:** năm mẫu đã tính dùng γ=1,α=.8; không thuộc phát biểu chiết khấu sẽ dùng. Có A/E kết thúc chưa đủ cho mở rộng mọi chính sách vì vòng B↔C. Các mở rộng không chiết khấu cần giả thiết hấp thụ và lợi tức riêng; không áp ngầm định lý γ<1 cho bài tính. Sai lệch mẫu có thể còn lớn sau năm bước; dừng vì hết ngân sách chỉ trả một bảng hiện hành.
- **Bố cục:** ba dòng giả thiết nền, một cặp yêu cầu được phát triển ở F02/F03; không đưa chứng minh hội tụ lên trang.
- **Quan hệ, nguồn, quyết định:** E08 tính đúng mục tiêu→F01 giới hạn của phép tính→F02 độ phủ/tham lam. `Sửa, bổ sung giả thiết` L06 tr. 26–28; SB tr. 129–131, SI00 tr. 294–295, WD92 tr. 282/285–286.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-F02: Điều kiện GLIE

- **Vai trò, mục tiêu, thời lượng:** ví dụ, hình thức và phân biệt KN6; MT6; 3 phút. Luận điểm: giảm xác suất thăm dò và bảo đảm thăm vô hạn là hai yêu cầu riêng.
- **Mặt trang:** tên đầy đủ “Tham lam trong giới hạn với thăm dò vô hạn (GLIE)”. Với hai hành động và một cực đại, ε=.25 giữ khối tham lam 7/8; ε giảm về 0 làm khối đó tiến tới 1. Định nghĩa với $\mathcal G_t(s)=\arg\max_aQ_t(s,a)$:
  $$C_t(s,a)\to\infty,\qquad\sum_{a\in\mathcal G_t(s)}\pi_t(a\mid s)\to1\quad\text{gần chắc chắn}.$$
- **Ghi chú:** t là chỉ số tương tác; C_t đếm lần thăm, Q_t là bảng hiện hành trước cập nhật, π_t là quy tắc chọn từ chính bảng ấy. Trong Sarsa, quy tắc này dùng để lấy A_{t+1} trước cập nhật; A_t đã được chọn ở bước trước. Với MC, k là chỉ số lượt; $Q^{[k]}$ là bảng trước lượt k và $\pi_k$ được giữ cố định trong lượt. Với cập nhật một bước, $Q_t$ là bảng trước cập nhật tại tương tác t. Lịch $\varepsilon_k$=1/k bảo đảm vế tham lam theo lượt nhưng cần kiểm riêng đạt tới/khởi đầu để có độ phủ. Chính sách mềm tại một trạng thái chưa bảo đảm trạng thái ấy được ghé vô hạn.
- **Bố cục:** ví dụ xác suất ngắn trước hai điều kiện; phản ví dụ hai bước không lên mặt trang. Ghi chú đọc thêm nêu có lịch 1/k vẫn không phủ khi phải thăm dò liên tiếp.
- **Quan hệ, nguồn, quyết định:** F01 cần dữ liệu dài hạn→F02 hai yêu cầu→F03 lượng ảnh hưởng của từng mẫu. `Sửa` L06 tr. 11/25 theo SI00 tr. 290–292/302–304; xử lý tập cực đại và chỉ số thời gian.
- **Rà soát từng trang 01-10-2026:** `sửa`. Nối lại lịch $\varepsilon_k$ của Monte Carlo; ví dụ $\varepsilon_k=1/k\to0$ (nguồn tr. 25).
- **Sửa sau rà soát độc lập 01-10-2026:** Câu nối: lịch $\varepsilon_k=1/k$ thỏa tham lam trong giới hạn, thăm vô hạn cần kiểm riêng; định nghĩa $C_t$ gộp vào dòng đặt ký hiệu.

#### L06-F03: Điều kiện Robbins–Monro

- **Vai trò, mục tiêu, thời lượng:** ví dụ trước điều kiện KN6; MT6; 3 phút. Luận điểm: một cặp được thăm thưa vẫn cần nhận đủ tổng bước học, với tổng bình phương hữu hạn.
- **Mặt trang:** n là số cập nhật riêng của (s,a). Ví dụ 1/n so với hằng 0.8. Điều kiện Robbins–Monro:
  $$0<\alpha_n(s,a)\le1,\quad\sum_n\alpha_n(s,a)=\infty,\quad\sum_n\alpha_n(s,a)^2<\infty.$$
  Dòng cảnh báo học thuật: “$1/t$ toàn cục không tự là $1/n$ theo cặp.”
- **Ghi chú:** với 1/n, tổng điều hòa phân kỳ còn tổng 1/n² hội tụ. Với 0.8, tổng bình phương 0.64 mỗi bước phân kỳ. Ví dụ cặp chỉ cập nhật ở $t_n=2^n$: dùng $\alpha_t$=1/t khiến tổng theo cặp bằng $\sum_n 2^{-n}$ hữu hạn, dù tổng toàn cục $\sum_t 1/t$ phân kỳ. Bước học dùng thông tin có trước mẫu để phù hợp miền định lý. Đây là kiểm chuỗi số, không là chứng minh xấp xỉ ngẫu nhiên.
- **Bố cục:** hai lịch số, công thức ba điều kiện; ví dụ $t_n$ ở ghi chú để không quá tải. Không lẫn N số lợi tức lần ghé đầu với số lần thăm C_t.
- **Quan hệ, nguồn, quyết định:** F02 mẫu tới vô hạn→F03 cách cân mẫu→F04 kết luận đúng thuật toán. `Sửa` L06 tr. 27–28; SI00 Định lý 1, WD92 tr. 282. Bước 0.8 giữ cho minh họa, không dùng để chứng minh hội tụ.
- **Rà soát từng trang 01-10-2026:** `sửa`. Gọi tên Robbins–Monro tại trang nêu điều kiện; công thức đặt trước hai ví dụ; ghi chú thêm diễn giải hai tổng (Sutton–Barto §2.5).

#### L06-F04: Hội tụ của Sarsa và Q-learning

- **Vai trò, mục tiêu, thời lượng:** phát biểu và áp dụng KN6; MT6; 4 phút. Luận điểm: hai thuật toán có cùng đích q* dưới giả thiết phù hợp, nhưng đòi hỏi khác nhau đối với hành vi.
- **Mặt trang:** giả thiết chung: MDP hữu hạn, có động lực không đổi theo thời gian, thưởng chặn, γ<1, Q0 hữu hạn; mẫu đúng động lực, mỗi cặp cập nhật vô hạn, bước học thỏa hai tổng Robbins–Monro theo cặp. Bảng hai hàng: Sarsa thêm “chính sách trở nên tham lam theo bảng hiện hành”; Q-learning dùng “hành vi duy trì độ phủ”. Kết luận chung $Q_t(s,a)\to q_*(s,a)$ gần chắc chắn. MC: trung bình mẫu khi chính sách cố định chưa tự chứng minh hội tụ của điều khiển đổi chính sách.
- **Ghi chú:** Miền kết quả gồm MDP hữu hạn, có động lực không đổi theo thời gian, thưởng bị chặn, $0\le\gamma<1$, $Q_0$ hữu hạn, mẫu có điều kiện đúng động lực, mọi cặp cập nhật vô hạn và hai tổng bước học theo cặp. Bước học dựa trên thông tin có trước mẫu. Sarsa cần thêm giới hạn tham lam; Q-learning không đòi b tiến về tham lam. Đồng hạng có thể khiến phân phối hành động không hội tụ tới một chính sách duy nhất. Với MC, lợi tức do các $\pi_k$ khác nhau sinh ra không có cùng kỳ vọng $q_\pi$ cố định. Mệnh đề cải thiện dùng $q_\pi$ chính xác không chứng minh từng bước MC từ mẫu. Sutton–Barto tr. 99 và 103 tách các kết quả này; Tsitsiklis (2002) chứng minh những biến thể có giả thiết riêng, không xác nhận mọi thuật toán MC GLIE.
- **Bố cục:** giả thiết chung gọn, hai hàng so sánh, kết luận một dòng; chứng minh hội tụ đầy đủ không áp dụng trong 120 phút. Notes có nguồn và giới hạn, không dùng câu “nhấn mạnh”.
- **Quan hệ, nguồn, quyết định:** F01–F03 đủ nền→F04 đối chiếu→F05 áp dụng điều kiện. `Sửa, gộp` L06 tr. 26–28; SB tr. 99–103/129–131, SI00 tr. 294–295, WD92 tr. 282, TS02 tr. 60/66–67/72.
- **Rà soát từng trang 01-10-2026:** `giữ`. Không đổi.

#### L06-F05: Kiểm tra giả thiết hội tụ

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch F; MT6; 3 phút:75 giây xét trường hợp,45 giây trả lời,60 giây chữa. Luận điểm: một tham số quen thuộc không thay cho toàn bộ giả thiết của định lý.
- **Mặt trang — Câu hỏi:** giả sử MDP hữu hạn, có động lực không đổi theo thời gian, thưởng bị chặn, γ=.9, Q0 hữu hạn, mẫu đúng môi trường và mọi cặp được cập nhật vô hạn. Xác định đủ điều kiện cho kết luận hội tụ tới $q_*$ đã học hay còn thiếu ở ba trường hợp: (a) Q-learning, b là ε-tham lam với ε=.25, $\alpha_n$=1/n; (b) Sarsa cùng ε và α; (c) Sarsa có GLIE nhưng $\alpha_n$=.8. Các trạng thái xét có hai hành động; trong (b) có trạng thái giữ một cực đại duy nhất.
- **Ghi chú/đáp án:** (a) đủ các điều kiện đã nêu; Q-learning không yêu cầu b tham lam trong giới hạn. (b) khối xác suất trên cực đại tại trạng thái ấy là 7/8, chưa tiến 1, nên không dùng kết luận hội tụ tới $q_*$ của định lý. (c) tổng bình phương bước học phân kỳ. Với nguồn $\varepsilon_k$=1/k, vẫn cần kiểm riêng bao phủ, không chỉ nhìn lịch. Không kết luận trường hợp thiếu giả thiết chắc chắn phân kỳ; chỉ kết luận định lý đang xét chưa áp dụng.
- **Tiêu chí:** gọi đúng giả thiết và thuật toán; kiểm theo n của cặp; phân biệt “chưa được bảo đảm” với “không thể hội tụ”.
- **Quan hệ, nguồn, quyết định:** F04 định lý→F05 kiểm phạm vi→G01 dùng điều kiện khi chọn phương pháp. `Thêm` câu hỏi từ L06 tr. 25/27/28 và các định lý đã dẫn; không cần mô hình mới hoặc đồ thị.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

## G. Tổng hợp và kết luận

#### L06-G01: Tổng kết ba phương pháp

- **Vai trò, mục tiêu, thời lượng:** tổng hợp kiến thức đã có; MT3–MT7; 3 phút. Luận điểm: loại dữ liệu và mục tiêu xác định khác biệt cơ chế của ba phương pháp.
- **Mặt trang:** bảng ba hàng: MC theo chính sách dùng lượt hoàn chỉnh, mục tiêu Gt, cập nhật sau lượt; Sarsa dùng bộ năm, mục tiêu R+γ Q(S',A'), cập nhật từng chuyển; Q-learning dùng bộ bốn, mục tiêu R+γmax Q(S',a), cập nhật từng chuyển. Nhãn chung: bảng Q hữu hạn; MC giữ thêm lượt, hai phương pháp TD không cần lưu cả lượt.
- **Ghi chú:** Các công thức trong bảng dùng nhánh chưa kết thúc; tại trạng thái kết thúc, hai phương pháp TD chỉ dùng thưởng R. MC trong bài dùng lần ghé đầu và giữ chính sách trong lượt. Sarsa dùng cùng chính sách cho hành vi và mục tiêu; Q-learning tách đích tham lam khỏi b. Dự đoán cố định π khác điều khiển thay đổi π. TD(0) cho giá trị trạng thái giải bài toán dự đoán, nên không cùng chức năng với ba phương pháp điều khiển đang so sánh.
- **Bố cục:** tối đa ba hàng và bốn cột; công thức ngắn đã học, chi tiết điều kiện ở ghi chú và F. Không sao chép ma trận nguồn 23.
- **Quan hệ, nguồn, quyết định:** F05 điều kiện→G01 các lựa chọn đã học→G02 quyết định tại D. `Gộp, sửa, lược` L06 tr. 9/22–23/30; ba tiêu chí đủ để chọn phương pháp trong phạm vi bài.
- **Rà soát từng trang 01-10-2026:** `sửa`. Hộp nêu một ô cho mỗi cặp; chú thích nối Bài 07 (xấp xỉ hàm) theo nguồn tr. 7, 30.

#### L06-G02: Quyết định tại D sau các cập nhật

- **Vai trò, mục tiêu, thời lượng:** thu hồi bài toán mở đầu; MT1/MT7; 2 phút. Luận điểm: bảng hữu hạn mẫu cho một lựa chọn hiện hành, kèm giới hạn về dữ liệu và bảo đảm.
- **Mặt trang:** ba kết quả có nhãn dữ liệu: MC với lượt D–C–B–A từ bảng II cho D=(998,0), ưu tiên trái; Sarsa với năm mẫu từ bảng I cho D=(−1.28,8.2), ưu tiên phải; Q-learning với cùng năm mẫu từ bảng I cho D=(−.64,8.2), ưu tiên phải. Kết luận: “Các bảng này chưa chứng nhận chính sách tối ưu.”
- **Ghi chú:** Lần chạy MC tham lam riêng từ bảng I cho D=(0,10), cũng ưu tiên phải. Kết quả MC dùng lượt và khởi tạo khác, nên ba bảng không tạo một thử nghiệm công bằng về hiệu quả học. Sarsa/Q-learning có cùng dữ liệu nhưng khác mục tiêu. Lợi tức 998 trên một lượt đi trái tới A chỉ thành $q_{\pi_L}(D,0)$ khi đã chỉ định chính sách tiếp nối $\pi_L$ luôn đi trái; nó không xác định giá trị của mọi chính sách. Quy trình điều khiển gồm thu dữ liệu, tạo mục tiêu, cập nhật bảng, chọn hành động và kiểm điều kiện. Số mẫu hữu hạn chưa đủ để kết luận tối ưu.
- **Bố cục:** ba hàng ngắn, mỗi hàng ghi rõ dữ liệu và bảng đầu; không gọi đó là đường học thực nghiệm.
- **Quan hệ, nguồn, quyết định:** G01 tổng hợp cơ chế; G02 giải thích hành động tại D; G03 chọn phương pháp cho mục đích xác định. `Sửa` L06 tr. 16–18/21/30; dùng kết quả đã kiểm, không thêm khái niệm.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-G03: Kiểm tra lựa chọn phương pháp

- **Vai trò, mục tiêu, thời lượng:** kiểm tra riêng mạch G; MT6/MT7; 3 phút: 75 giây chọn, 45 giây giải thích, 60 giây chữa. Luận điểm: lựa chọn phải khớp mục tiêu và thời điểm cập nhật, kèm điều kiện về dữ liệu.
- **Mặt trang — Câu hỏi:** chọn MC, Sarsa hoặc Q-learning phù hợp với yêu cầu: (1) dùng lợi tức hoàn chỉnh, thay chính sách sau lượt; (2) cập nhật trong lượt bằng giá trị hành động thật sẽ thực hiện; (3) có mẫu $(S,A,R,S')$ từ hành vi còn thăm dò, mục tiêu là cực đại trên bảng. Với trường hợp 3, nêu hai điều kiện cần kiểm trước khi viện dẫn hội tụ tới q*.
- **Ghi chú/đáp án:** (1) MC theo chính sách, lần ghé đầu; cần lượt kết thúc và bộ đếm đúng. (2) Sarsa; cần A' lấy trước cập nhật và nhánh kết thúc riêng. (3) Q-learning; cần mẫu đúng MDP, độ phủ và bước học theo cặp, trong miền hữu hạn, thưởng chặn và γ<1. Dữ liệu đầy đủ có thể được dùng bởi nhiều thuật toán; yêu cầu đã chỉ định cả loại mục tiêu và thời điểm cập nhật, nên lựa chọn dựa trên hai tiêu chí ấy.
- **Tiêu chí:** ghép đúng ba yêu cầu; giải thích bằng mục tiêu và dữ liệu; nêu giả thiết xác định thay vì “đủ nhiều mẫu” hoặc “đến hội tụ”.
- **Quan hệ, nguồn, quyết định:** G02 cho lựa chọn từ bảng; G03 kiểm năng lực tổng hợp; G04 nêu nhiệm vụ luyện tiếp. `Thêm` từ L06 tr. 9/13/20/25–30 và SB §5.4/§6.4–6.5; không hỏi kỹ thuật ngoài bài.
- **Rà soát từng trang 01-10-2026:** `sửa`. Tiêu đề.

#### L06-G04: Bài tập và tài liệu đọc

- **Vai trò, mục tiêu, thời lượng:** kết luận và học tiếp có căn cứ; MT3–MT7; 2 phút. Luận điểm: luyện lại quy trình và đọc các mở rộng với đúng đối tượng được ước lượng.
- **Mặt trang:** **Câu hỏi:** hoàn thiện hai bảng Sarsa/Q-learning sau từng mẫu và giải thích mẫu 2, mẫu 5. Bài tập: nguồn tr. 16–18/21; Bài 10 trong hw3.pdf, phần bảng tra. Tài liệu: Sutton–Barto §§5.2–5.4, §§6.4–6.5. Hai mục đọc thêm: “Dự đoán TD(0) khác chính sách” và “Sai số đánh giá một chính sách cố định”.
- **Ghi chú:** Bài 10 trong hw3.pdf dùng sáu trạng thái A–F và γ=.5; dữ kiện này khác chuỗi A–E. Hai lượt đã cho đều kết thúc thật trước giới hạn năm bước; lời giải phải dùng đúng bảng khởi tạo riêng của bài ấy. Nội dung lấy mẫu quan trọng của nguồn dùng V và tỉ số nhân mục tiêu, nên thuộc dự đoán TD(0) khác chính sách, không phải cập nhật Sarsa. Chặn đánh giá chính sách cố định dùng cùng π và phân phối đầu d0, các lượt độc lập và lợi tức bị chặn. Chặn cho một giá trị như vậy không xác định số mẫu cần để tìm chính sách tối ưu.
- **Bố cục:** một nhiệm vụ và danh mục đọc ngắn; URL dài và nguồn chi tiết ở ghi chú/học liệu. Đáp án và lịch chữa 30 phút trong analysis §7 là chỉ dẫn nội bộ, không hiển thị trên trang hoặc trong ghi chú diễn giả. Hai mục đọc thêm được liên kết trong học liệu, không giảng công thức mới hoặc thêm trang trong 45 trang chính.
- **Quan hệ, nguồn, quyết định:** G03 đã kiểm năng lực; G04 chỉ rõ bài luyện và phạm vi đọc; kết thúc ở sản phẩm người học có thể tự kiểm. `Sửa, bổ sung nguồn đọc` từ L06 tr. 19/29/30, H03 Bài 10, SB, HF63. Không đưa khái niệm trọng tâm mới.
- **Rà soát từng trang 01-10-2026:** `giữ`. Không đổi.

## Ranh giới triển khai và kiểm định

Các mạch lần lượt dùng `data-note-topic-id="lec-06-topic-01"` tới `lec-06-topic-07`; học liệu tương ứng đặt comment một lần ở mục chủ đề. DT1/DT2 thuộc phần đọc thêm của chủ đề 07, dùng đặc tả tại analysis §7; không viết đoạn trống “sẽ bổ sung” trong sản phẩm cuối. Mã và thời lượng chỉ ở planning; HTML có data-slide-id theo 45 heading trên.

Bảy SVG đã triển khai theo analysis §5.2; bảng, giả mã và công thức không ảnh hóa. Bộ slide dùng mẫu và CSS chung, khung 1280×720, thư viện cục bộ. Các vùng trọng điểm để kiểm định trực quan cuối sau biên tập: B02/B05/B06 về công thức; C04/D02 về dữ kiện; C05/C06/D05/D06/E04/E05 về tính liên tục của giả mã; E06/G01 về bảng. Không giảm chữ dưới mức quy định để giữ nhiều nội dung.

Dàn này đã kiểm các kết quả số MC, Sarsa, Q-learning, xác suất, C08 và E08. Phép tính khớp không thay kiểm định giả thiết hoặc khả năng đọc. Năm lượt rà độc lập đã bao phủ bản nháp triển khai và được điều phối viên chấp nhận trước biên tập. Các sửa hiện tại giữ nguyên số trang, thứ tự, thời lượng và luận điểm mở–kết. Phạm vi tái kiểm toán/thuật toán, mạch viết và các ranh giới liên quan được ghi trong review-log; chỉ chấp nhận bàn giao sau kiểm định đúng phiên bản mới.
