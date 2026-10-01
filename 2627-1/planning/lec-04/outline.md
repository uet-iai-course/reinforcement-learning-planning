# Dàn bài mới Bài 04

Bài 04 — Giải MDP bằng quy hoạch động. Học phần Học tăng cường, học kỳ 1 năm học 2026–2027. Người học: sinh viên đại học đã học học máy, học sâu và thuật toán; tiên quyết dùng trực tiếp là MDP, xác suất có điều kiện, tổng chiết khấu, vector, chuẩn vô cùng được định nghĩa lại và hệ tuyến tính.

Vấn đề trung tâm: từ mô hình chuyển–thưởng đã biết, tính giá trị của một chính sách, cải thiện lựa chọn và tìm chính sách tối ưu có điều kiện kiểm chứng. Phần trình chiếu gồm **45 trang, 7 mạch, 120 phút**; thời gian đã gồm các câu kiểm tra riêng và chữa ngắn. **30 phút còn lại của buổi 150 phút dành cho chữa bài tập** theo nguồn; không tự tạo code demo vì PDF và tài liệu tuần 4 không có chương trình.

Đây là bản dàn bài mới, không dùng dàn bài cũ làm khung. Chỉ dẫn cụ thể của người dùng cho phép thay thứ tự nguồn để theo Sutton–Barto chương 4: đánh giá → cải thiện → lặp chính sách → lặp giá trị → bất đồng bộ/GPI/hiệu quả. Chủ đề và dữ kiện của PDF nguồn được bảo toàn qua ánh xạ đủ 38 trang. Kế hoạch đã được chấp nhận và triển khai ngày 2026-09-28. Năm vai đã rà độc lập cùng bản cố định; các sửa cục bộ sau rà được cập nhật trong hồ sơ này. Bằng chứng kiểm định và trạng thái rà lại nằm trong review-log.md.

Phân tích và nguồn chi tiết: [analysis.md](analysis.md). Cấu trúc học tập và quyết định theo trang: [storyboard.md](storyboard.md).

## Mục tiêu

| Mã | Năng lực quan sát được | Kiểm tra chính |
|---|---|---|
| MT1 | Xác định mô hình, chính sách, phần thưởng và tổng chiết khấu trong bài toán lập kế hoạch. | Kiểm tra mở đầu |
| MT2 | Tính một lượt đánh giá đồng bộ, phân biệt $V_k$ với $v_\pi$, dùng phần dư đánh giá. | Kiểm tra đánh giá chính sách |
| MT3 | Tính $q_\pi$, chọn hành động cải thiện và giải thích vì sao giá trị không giảm dưới giả thiết. | Kiểm tra cải thiện |
| MT4 | Thực hiện một lần lặp chính sách và phân biệt bảo đảm đánh giá chính xác với dừng gần đúng. | Kiểm tra lặp chính sách |
| MT5 | Thực hiện lặp giá trị, trích chính sách và kiểm tra phần dư trên đúng bảng trả về. | Kiểm tra lặp giá trị; kiểm tra tổng hợp |
| MT6 | So sánh đồng bộ, tại chỗ, bất đồng bộ; nêu điều kiện lịch, chi phí và giới hạn mô hình. | Kiểm tra thực hành; kiểm tra tổng hợp |

## Bản đồ bảy mạch

| Mạch | Vai trò | Đầu vào | Đầu ra và đóng góp | Trang | Phút | Kiểm tra riêng |
|---|---|---|---|---|---:|---|
| A. Mở đầu | Thiết lập bài toán | MDP, xác suất có điều kiện và tổng chiết khấu | Mô hình hai trạng thái và nhu cầu đánh giá một chính sách cố định | L04-A01–L04-A05 | 10 | L04-A05 |
| B. Đánh giá chính sách | Phát triển kiến thức và luyện tập | Mô hình đã biết và chính sách cố định | Giá trị chính xác hoặc bảng có phần dư; làm đầu vào so sánh hành động | L04-B01–L04-B08 | 22 | L04-B08 |
| C. Cải thiện chính sách | Phát triển kiến thức và luyện tập | Giá trị của chính sách đã đánh giá | Chính sách mới không kém; nhu cầu đánh giá lại chính sách mới | L04-C01–L04-C07 | 20 | L04-C07 |
| D. Lặp chính sách | Phát triển thuật toán và luyện tập | Đánh giá, cải thiện, tính co theo chính sách | Chính sách ổn định và điều kiện tối ưu; giới hạn chi phí đánh giá đầy đủ | L04-D01–L04-D06 | 18 | L04-D06 |
| E. Lặp giá trị | Phát triển thuật toán và luyện tập | Lặp chính sách và nhu cầu cắt ngắn đánh giá | Cập nhật tối ưu, phần dư và chính sách trích; nhu cầu phân bổ công việc | L04-E01–L04-E08 | 22 | L04-E08 |
| F. Quy hoạch động trong thực hành | Tổ chức tính toán và giới hạn | Cập nhật kỳ vọng, lặp chính sách, lặp giá trị | Lịch cập nhật, điều kiện bao phủ, GPI và giới hạn mô hình | L04-F01–L04-F06 | 16 | L04-F06 |
| G. Tổng hợp và bài tập | Kết luận và vận dụng tổng hợp | Kết quả của sáu mạch trước | Kiểm tra nghiệm, so sánh phương pháp theo giả thiết; bài tập và tài liệu đọc | L04-G01–L04-G05 | 12 | L04-G04 |

Tổng: **45 trang; 120 phút**. Kiểm tra riêng của từng mạch: A05, B08, C07, D06, E08, F06, G04. G03 là bài tập bổ sung, không thay kiểm tra riêng G04. Mã nội bộ chỉ xuất hiện trong tệp kế hoạch và thuộc tính HTML; không hiển thị trên mặt trang hay ghi chú diễn giả.

## Bảng thuật ngữ và ký hiệu

| Ký hiệu/thuật ngữ | Miền và nghĩa | Quy ước sử dụng |
|---|---|---|
| $\mathcal S$, $\mathcal A(s)$, $\mathcal R$ | Tập hữu hạn các trạng thái chưa kết thúc, hành động hợp lệ khác rỗng và phần thưởng thực | Nếu có kết thúc, $\mathcal S^+=\mathcal S\cup\{s_\mathrm{term}\}$; mô hình hai trạng thái là tiếp diễn. |
| $S_t,A_t,R_{t+1}$ | Trạng thái, hành động tại $t$, phần thưởng nhận sau hành động | $t$ chỉ thời gian tương tác; viết $R_{t+1}$, không đổi thành $R_t$ trong cùng quy ước. |
| $p(s',r\mid s,a)$ | Phân phối chung trạng thái kế tiếp và thưởng, tổng bằng 1 | Markov và bất biến theo thời gian trong bài; dữ kiện đã biết. Tổng theo $s'\in\mathcal S^+$ và $r\in\mathcal R$. |
| $P(s'\mid s,a)$, $\bar r(s,a)$ | Các đại lượng suy ra từ phân phối chung | $P=\sum_rp$; $\bar r=\sum_{s',r}rp$. Chỉ dùng khi giải thích chi phí hoặc ma trận; không coi là phần thưởng độc lập khác. |
| $\pi(a\mid s)$; $\pi(s)$ | Chính sách dừng ngẫu nhiên; cách viết cho chính sách xác định | $\pi(s)=a$ tương đương phân phối tập trung tại $a$. Chính sách xác định dùng trong lặp chính sách chính xác. |
| $G_t$ | Tổng thưởng chiết khấu, bắt đầu từ $R_{t+1}$ | $\gamma\in[0,1)$ và thưởng bị chặn trong bảo đảm chính; khi kết thúc $G_T=0$. |
| $v_\pi$, $q_\pi$ | Giá trị trạng thái và giá trị hành động chính xác của chính sách | Chỉ số dưới; $q_\pi$ cố định hành động đầu rồi theo $\pi$, kể cả hành động đầu không được $\pi$ chọn. |
| $v_*,q_*$ | Giá trị tối ưu | Không đổi qua lại với $v^*$ hoặc $v^\pi$ trong bài mới. |
| $V$, $V_k$, $W$ | Bảng ước lượng hiện có, sau $k$ lượt, và bảng mới tạm | Chữ hoa; $k$ chỉ lượt tính toán, $i$ chỉ lần cải thiện chính sách. Cặp trả từ PI phải thuộc cùng một chính sách. |
| $T_\pi,T_*$ | Toán tử Bellman đánh giá và tối ưu trên bảng giá trị | Định nghĩa sau bước tính tương ứng; $V_{k+1}=TV_k$ dùng cho đồng bộ. |
| $Q_V(s,a)$ | Giá trị nhìn trước từ bảng tùy ý $V$ | Chỉ giới thiệu khi cần ở lặp giá trị; $Q_{v_\pi}=q_\pi$, không đồng nhất $Q_V$ với $q_\pi$ nói chung. |
| $\Delta_\pi(V),\Delta_*(V)$ | Phần dư của bảng $V$: $\|T_\pi V-V\|_\infty$, $\|T_*V-V\|_\infty$ | Tính khi giữ nguyên bảng trả; mức đổi lớn nhất của lượt tại chỗ không tự bằng phần dư. |
| $\eta,\varepsilon,K,I_{\max}$ | Ngưỡng phần dư, sai số giá trị yêu cầu, ngân sách cập nhật, ngân sách PI | $K\ge0$ đếm số lần nhận bảng mới; $I_{\max}\ge1$ đếm vòng lặp chính sách. Dùng $\eta$ để tránh trùng $\theta$ là góc CartPole. Hết ngân sách không là bằng chứng hội tụ. |
| $P_\pi,r_\pi$ | Ma trận chuyển $n\times n$, vector thưởng kỳ vọng $n$ dưới chính sách | $P_\pi(s,s')=\sum_a\pi(a\mid s)\sum_rp(s',r\mid s,a)$, $r_\pi(s)=\sum_a\pi(a\mid s)\bar r(s,a)$. |

Thuật ngữ cố định: **đánh giá chính sách**, **cải thiện chính sách**, **lặp chính sách**, **lặp giá trị**, **cập nhật đồng bộ**, **cập nhật tại chỗ**, **quy hoạch động bất đồng bộ**, **cập nhật kỳ vọng**, **phần dư Bellman**, **chính sách tham lam**. Lần đầu viết đầy đủ “quá trình quyết định Markov (MDP)”, “quy hoạch động (DP)” nếu dùng DP, “lặp chính sách tổng quát (GPI)” nếu dùng GPI. Ưu tiên tên tiếng Việt; không thêm viết tắt PI/VI trên mặt trang khi không cần.

## Dàn bài từng trang

### Mạch A. Mở đầu

Chức năng: Thiết lập bài toán. Đầu vào: MDP, xác suất có điều kiện và tổng chiết khấu. Đầu ra: Mô hình hai trạng thái và nhu cầu đánh giá một chính sách cố định. Mục tiêu: MT1. Thời lượng: 10 phút; kiểm tra riêng L04-A05.

#### L04-A01 — Giải MDP bằng quy hoạch động

- **Vai trò và mục tiêu:** Mở đầu; MT1–MT6
- **Luận điểm trung tâm:** Quy hoạch động tính giá trị và chính sách từ mô hình môi trường đã biết.
- **Ý chính:** Bài 04; học phần Học tăng cường; học kỳ 1 năm học 2026–2027. Tên đầy đủ của quá trình quyết định Markov (MDP) xuất hiện khi giới thiệu chủ đề.
- **Ví dụ/hình dự kiến:** Trang tiêu đề dùng kiểu chữ và chân trang của mẫu; không cần hình trang trí.
- **Hình thức hóa:** Chưa dùng công thức.
- **Kết nối vào:** Chủ đề học phần và tiên quyết của Bài 03.
- **Kết nối ra:** Chủ đề lập kế hoạch được cụ thể hóa bằng chuỗi năng lực cần thực hiện.
- **Nguồn:** NG1, tr. 1; NG2, Ch. 4, tr. in 73 (PDF 95).
- **Thời lượng:** 1 phút
- **Ghi chú học thuật dự kiến:** Phạm vi là lập kế hoạch trong MDP hữu hạn với mô hình chuyển và phần thưởng đã biết. Quy hoạch động dùng mô hình này để tính giá trị của chính sách và xác định lựa chọn tối ưu.

#### L04-A02 — Nội dung và mục tiêu

- **Vai trò và mục tiêu:** Bản đồ nội dung; MT1–MT6
- **Luận điểm trung tâm:** Đánh giá chính sách cung cấp căn cứ cho cải thiện và các thuật toán điều khiển.
- **Ý chính:** Mạch nội dung: đánh giá chính sách → cải thiện chính sách → lặp chính sách → lặp giá trị → quy hoạch động bất đồng bộ. Mục tiêu trên mặt trang (sửa 2026-10-01): đánh giá và cải thiện chính sách; thực hiện lặp chính sách, lặp giá trị; chặn sai số bằng phần dư; so sánh cập nhật đồng bộ và bất đồng bộ. Tiên quyết: kỳ vọng có điều kiện, tổng chiết khấu, MDP và hệ tuyến tính.
- **Ví dụ/hình dự kiến:** Sơ đồ năm nút có nhãn sản phẩm: giá trị của chính sách, chính sách mới, chính sách ổn định, giá trị tối ưu, lịch cập nhật.
- **Hình thức hóa:** Không thêm định nghĩa; mục tiêu chi tiết ở hồ sơ kế hoạch.
- **Kết nối vào:** Chủ đề lập kế hoạch được cụ thể hóa bằng chuỗi năng lực cần thực hiện.
- **Kết nối ra:** Chuỗi đánh giá và cải thiện cần bắt đầu từ dữ kiện mô hình và mục tiêu điều khiển.
- **Nguồn:** NG1, tr. 2–3; NG2, §4.1–4.7, tr. in 74–88 (PDF 96–110).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Mọi thuật toán trong bài dùng cùng mô hình chuyển–thưởng và quy ước chiết khấu. Đánh giá giữ chính sách cố định; điều khiển cho phép thay chính sách. Ánh xạ bốn mục tiêu sang các mạch.

#### L04-A03 — Lập kế hoạch với mô hình đã biết

- **Vai trò và mục tiêu:** Vấn đề trung tâm; MT1
- **Luận điểm trung tâm:** Mô hình cho phép tính kỳ vọng của quyết định trước khi thực hiện tương tác.
- **Ý chính:** Cho tập trạng thái và hành động hữu hạn, phân phối chuyển–thưởng đã biết và hệ số chiết khấu nhỏ hơn 1. Cần tìm chính sách có tổng phần thưởng chiết khấu kỳ vọng lớn nhất tại mọi trạng thái. Mặt trang định nghĩa quy hoạch động là nhóm thuật toán tính chính sách tối ưu từ mô hình MDP đầy đủ (NG2, chương 4, tr. 73). Giá trị của chính sách hiện tại là đại lượng cần tính trước; ý này nằm trong notes.
- **Ví dụ/hình dự kiến:** Hai khối mô hình và chính sách dẫn tới bảng giá trị; phân biệt dữ kiện với đầu ra cần tìm.
- **Hình thức hóa:** Nhắc giả thiết Markov: $p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$; mọi tổng xác suất bằng 1. $0\le\gamma<1$; phần thưởng bị chặn. Miền: $S_t\in\mathcal S$, $A_t\in\mathcal A(S_t)$, $R_{t+1}\in\mathcal R\subset\mathbb R$; $\pi(a\mid s)$ là phân phối hành động.
- **Kết nối vào:** Chuỗi đánh giá và cải thiện cần bắt đầu từ dữ kiện mô hình và mục tiêu điều khiển.
- **Kết nối ra:** Mô hình hữu hạn đã biết được biểu diễn bằng bốn chuyển tiếp của một ví dụ cụ thể.
- **Nguồn:** NG1, tr. 4, 12; NG2, §3.1, §4 mở đầu, tr. in 73 (PDF 95).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Trạng thái chứa thông tin cần thiết để mô tả phân phối bước kế tiếp. Bài này xét trạng thái quan sát đầy đủ; quan sát cảm biến nói chung không tự đồng nhất với trạng thái Markov. Mô hình là dữ kiện, không được suy ra chỉ từ một bảng phần thưởng. $\mathcal S$ gồm trạng thái chưa kết thúc; $\mathcal A(s)$ hữu hạn khác rỗng. Tổng theo $s'$ lấy trên $\mathcal S^+$, gồm cả đích nếu có. Mọi bảng mở rộng bằng $0$ tại đích.

#### L04-A04 — MDP hai trạng thái

- **Vai trò và mục tiêu:** Ví dụ dẫn nhập; MT1
- **Luận điểm trung tâm:** Bốn chuyển tiếp xác định đủ để so sánh lựa chọn hiện tại và phần thưởng tiếp nối.
- **Ý chính:** $s_0,a\to s_0,1$; $s_0,b\to s_1,0$; $s_1,a\to s_0,2$; $s_1,b\to s_1,3$. $\gamma=0.9$. Bài toán tiếp diễn, không có trạng thái kết thúc. Chính sách ban đầu chọn $a$ tại cả hai trạng thái.
- **Ví dụ/hình dự kiến:** SVG dp04-two-state.svg: hai đỉnh, hai vòng tự khép và hai cạnh ngược chiều; mỗi cạnh ghi hành động/phần thưởng. Bảng HTML bốn dòng cung cấp dữ kiện tương đương.
- **Hình thức hóa:** $\pi_0=(a,a)$ viết tắt cho hai hành động theo thứ tự $(s_0,s_1)$; chưa định nghĩa hàm giá trị.
- **Kết nối vào:** Mô hình hữu hạn đã biết được biểu diễn bằng bốn chuyển tiếp của một ví dụ cụ thể.
- **Kết nối ra:** Dữ kiện bốn chuyển tiếp đủ để kiểm tra một quỹ đạo theo chính sách cố định.
- **Nguồn:** NG1, tr. 17–18; số được kiểm chứng trong báo cáo số độc lập.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Hành động có phần thưởng trước mắt cao nhất chưa đủ để kết luận chính sách tối ưu. Mỗi chuyển tiếp ở đây có xác suất 1; không có bước lấy mẫu trong phép tính quy hoạch động.

#### L04-A05 — Kiểm tra tổng thưởng chiết khấu

- **Vai trò và mục tiêu:** Kiểm tra mở đầu; MT1
- **Luận điểm trung tâm:** Chính sách cố định và mô hình xác định hoàn toàn quỹ đạo trong ví dụ này.
- **Ý chính:** Xuất phát ở $s_1$, theo $\pi_0=(a,a)$ và $\gamma=0.9$. Chỉ xét ba phần thưởng đầu.
- **Ví dụ/hình dự kiến:** Giữ sơ đồ hai trạng thái nhỏ bên cạnh yêu cầu; lời giải chỉ trong ghi chú.
- **Hình thức hóa:** Nhắc $G_t=\sum_{j=0}^{\infty}\gamma^jR_{t+1+j}$; câu hỏi dùng tổng ba hạng đầu.
- **Kết nối vào:** Dữ kiện bốn chuyển tiếp đủ để kiểm tra một quỹ đạo theo chính sách cố định.
- **Kết nối ra:** Tổng ba bước chưa bao gồm phần thưởng về sau; đánh giá cần một biểu diễn cho phần tiếp nối.
- **Nguồn:** NG1, tr. 5, 17–18; câu kiểm tra được biên soạn từ dữ kiện nguồn.
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Phần thưởng đầu có chỉ số $t+1$ vì nó được nhận sau hành động tại thời điểm $t$. Tổng ba bước là một tổng cắt ngắn, chưa phải giá trị vô hạn.
- **Yêu cầu trên mặt trang:** Câu hỏi: Xác định ba phần thưởng đầu và tổng chiết khấu của chúng. Xác định dữ kiện nào còn phải biết nếu chỉ được cung cấp phần thưởng của từng hành động.
- **Kiến thức được đo:** MT1; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** Từ $s_1$: các phần thưởng là $2,1,1$; tổng $2+0.9+0.9^2=3.71$. Cần mô hình chuyển để xác định trạng thái tiếp theo; bảng thưởng riêng không đủ.
- **Tiêu chí đánh giá:** Đúng thứ tự thưởng, hệ số chiết khấu và phân biệt thưởng với mô hình chuyển.
- **Thời gian hoạt động:** 0.5 phút đọc dữ kiện, 0.75 phút tính, 0.75 phút đối chiếu; đã tính trong thời lượng của trang.

### Mạch B. Đánh giá chính sách

Chức năng: Phát triển kiến thức và luyện tập. Đầu vào: Mô hình đã biết và chính sách cố định. Đầu ra: Giá trị chính xác hoặc bảng có phần dư; làm đầu vào so sánh hành động. Mục tiêu: MT2. Thời lượng: 22 phút; kiểm tra riêng L04-B08.

#### L04-B01 — Bài toán đánh giá chính sách

- **Vai trò và mục tiêu:** Vấn đề và trực giác; MT2
- **Luận điểm trung tâm:** Đánh giá chính sách cộng thưởng hiện tại với giá trị tiếp nối theo chính sách đó.
- **Ý chính:** Giữ $\pi_0=(a,a)$. Tổng thưởng có vô hạn hạng, nhưng sau một chuyển tiếp bài toán trở lại một trạng thái trong cùng mô hình. Một bảng giá trị gần đúng cung cấp ước lượng cho phần tiếp nối.
- **Ví dụ/hình dự kiến:** SVG dp04-expectation-backup.svg: trạng thái gốc, hành động do chính sách chọn, các kết quả chuyển–thưởng; nhãn trung bình theo mô hình.
- **Hình thức hóa:** Gọi tên đánh giá chính sách (bài toán dự đoán); nêu hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ suy từ định nghĩa tổng chiết khấu và định nghĩa giá trị tiếp nối $V(s')$. Chưa đưa quy tắc cập nhật tổng quát.
- **Kết nối vào:** Tổng ba bước chưa bao gồm phần thưởng về sau; đánh giá cần một biểu diễn cho phần tiếp nối.
- **Kết nối ra:** Giá trị tiếp nối được thay bằng bảng hiện có để thực hiện lượt tính đầu tiên.
- **Nguồn:** NG1, tr. 6, 12–14; NG2, §4.1, tr. in 74–75 (PDF 96–97).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Đây là bài toán dự đoán. Chính sách không thay đổi trong suốt đánh giá. Cập nhật kỳ vọng sử dụng mọi kết quả có thể theo mô hình, khác với một chuyển tiếp lấy mẫu.

#### L04-B02 — Hai lượt đánh giá đồng bộ

- **Vai trò và mục tiêu:** Ví dụ tính tay; MT2
- **Luận điểm trung tâm:** Một lượt đồng bộ dùng cùng bảng cũ cho mọi trạng thái.
- **Ý chính:** $V_0=(0,0)$. Lượt đầu: $1+0.9\cdot0=1$, $2+0.9\cdot0=2$. Lượt sau: $1+0.9\cdot1=1.9$, $2+0.9\cdot1=2.9$. Do đó $V_1=(1,2)$ và $V_2=(1.9,2.9)$.
- **Ví dụ/hình dự kiến:** Hai cột bảng cũ và bảng mới; mũi tên từ ô $s_0$ cũ đến cả hai phép tính.
- **Hình thức hóa:** $V_k$ là bảng ước lượng sau $k$ lượt, không phải giá trị chính xác của một chính sách mới.
- **Kết nối vào:** Giá trị tiếp nối được thay bằng bảng hiện có để thực hiện lượt tính đầu tiên.
- **Kết nối ra:** Các phép tính một bước được khái quát thành giá trị chính xác và phương trình kỳ vọng.
- **Nguồn:** NG1, tr. 14, 17–18; suy tính được kiểm chứng từ dữ kiện nguồn.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Giá trị 2.9 của $s_1$ ở lượt hai dùng $V_1(s_0)=1$. Nếu dùng ngay giá trị mới 1.9 sẽ đổi thuật toán và cho 3.71 ở ô đó.

#### L04-B03 — Phương trình Bellman kỳ vọng

- **Vai trò và mục tiêu:** Định nghĩa; MT2
- **Luận điểm trung tâm:** Giá trị chính xác là kỳ vọng của tổng thưởng và thỏa quan hệ đệ quy một bước.
- **Ý chính:** $v_\pi(s)$ là tổng thưởng chiết khấu kỳ vọng khi bắt đầu ở $s$ và theo $\pi$. Kỳ vọng gồm ngẫu nhiên của chính sách và môi trường. Trong ví dụ, $v_{\pi_0}(s_0)=1+0.9v_{\pi_0}(s_0)$, $v_{\pi_0}(s_1)=2+0.9v_{\pi_0}(s_0)$.
- **Ví dụ/hình dự kiến:** Một công thức trung tâm, hai phương trình ví dụ ngắn phía dưới; không chèn đồng thời phương trình $q_\pi$.
- **Hình thức hóa:** HT1: $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_\pi(s')]$.
- **Kết nối vào:** Các phép tính một bước được khái quát thành giá trị chính xác và phương trình kỳ vọng.
- **Kết nối ra:** Nghiệm ở cả hai vế được thay bằng bảng hiện có để tạo toán tử cập nhật.
- **Nguồn:** NG1, tr. 5–6; NG2, §4.1, (4.3)–(4.4), tr. in 74 (PDF 96).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Vế phải sử dụng chính $v_\pi$ nên đây là phương trình xác định điểm bất động. Công thức cập nhật sẽ thay giá trị chưa biết ở vế phải bằng bảng hiện có. Nếu có trạng thái kết thúc, giá trị tiếp nối của nó bằng 0. Ví dụ chính sách ngẫu nhiên được tính ngay sau định nghĩa toán tử ở B04 để không lẫn bảng một lượt với giá trị chính xác.

#### L04-B04 — Toán tử đánh giá chính sách

- **Vai trò và mục tiêu:** Hình thức và quy tắc cập nhật; MT2
- **Luận điểm trung tâm:** Lặp đánh giá thay nghiệm chưa biết trong phương trình Bellman bằng bảng của lượt trước.
- **Ý chính:** $T_\pi$ biến một bảng hữu hạn thành một bảng mới; chính sách và mô hình được giữ cố định. $V_{k+1}=T_\pi V_k$. Chỉ số $k$ đếm lượt tính toán, không đếm thời gian tương tác.
- **Ví dụ/hình dự kiến:** Sơ đồ $V_k\to T_\pi\to V_{k+1}$ với nhãn $\pi,p$ cố định.
- **Hình thức hóa:** HT2: $(T_\pi V)(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]$; $v_\pi=T_\pi v_\pi$.
- **Kết nối vào:** Nghiệm ở cả hai vế được thay bằng bảng hiện có để tạo toán tử cập nhật.
- **Kết nối ra:** Quy tắc cập nhật cần quy định bảng đọc, bảng ghi và thời điểm dừng.
- **Nguồn:** NG1, tr. 10, 14; NG2, §4.1, (4.5), tr. in 74–75 (PDF 96–97).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Với $V_0=0$, $V_k$ bằng kỳ vọng của tổng thưởng cắt ngắn sau $k$ bước trong bài toán tiếp diễn này. Diễn giải đó phụ thuộc khởi tạo bằng không; với khởi tạo khác có thêm giá trị cuối ước lượng. Bảng có $|\mathcal S|$ thành phần và mở rộng bằng $0$ tại đích. Bootstrapping dùng ước lượng tiếp nối để xây mục tiêu. Với chính sách ngẫu nhiên đều và cùng mô hình, từ bảng không nhận $(0.5,2.5)$ do trung bình hai hành động. Cuối notes, trở lại $\pi_0=(a,a)$: giữa $V_1=(1,2)$ và $V_2=(1.9,2.9)$, độ lệch lớn nhất là $0.9$. Ví dụ định lượng này đứng trước định nghĩa phần dư ở B05 và đặt nhu cầu chặn sai số so với nghiệm chưa biết ở B06.

#### L04-B05 — Thuật toán đánh giá chính sách đồng bộ

- **Vai trò và mục tiêu:** Quy trình đầy đủ; MT2
- **Luận điểm trung tâm:** Hai bảng tách giá trị cũ và mới, còn phần dư kiểm tra độ chính xác của bảng được trả về.
- **Ý chính:** Đầu vào $p,\pi,\gamma$, ngưỡng phần dư $\eta>0$, ngân sách $K$; khởi tạo $V=0$, giá trị kết thúc bằng 0. Tính $W=T_\pi V$ từ bản chụp cố định. Nếu $\|W-V\|_\infty\le\eta$, trả $V$ cùng phần dư. Nếu chưa đạt và còn ngân sách, đặt $V\leftarrow W$. Khi hết ngân sách, tính lại phần dư trên bảng cuối và trả trạng thái chưa chứng nhận nếu còn vượt ngưỡng.
- **Ví dụ/hình dự kiến:** Mở bằng nhu cầu đại lượng dừng tính được và ví dụ $\Delta_{\pi_0}(V_1)=0{,}9$; giả mã ba bước (sửa 2026-10-01: gộp kiểm ngưỡng và hết ngân sách vào một bước, cùng ngữ nghĩa).
- **Hình thức hóa:** HT3: $\Delta_\pi(V)=\|T_\pi V-V\|_\infty$; thao tác kiểm tra không ghi đè $V$. Chuẩn vô cùng là $\|U-V\|_\infty=\max_{s\in\mathcal S}|U(s)-V(s)|$.
- **Kết nối vào:** Quy tắc cập nhật cần quy định bảng đọc, bảng ghi và thời điểm dừng.
- **Kết nối ra:** Phần dư đo được cần được liên hệ với sai số so với nghiệm chính xác.
- **Nguồn:** NG1, tr. 14–15; NG2, §4.1, tr. in 74–75 (PDF 96–97); tiêu chuẩn phần dư là bổ sung sư phạm.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Cập nhật đồng bộ cố định bảng đọc trong cả lượt, nên kết quả không phụ thuộc thứ tự ghi các ô của bảng mới. Cập nhật tại chỗ sử dụng cả giá trị vừa ghi và có kết quả trung gian phụ thuộc thứ tự. Ngân sách là giới hạn tài nguyên, không chứng minh hội tụ. Dữ liệu dùng để cập nhật là mô hình đầy đủ. $K$ là số nguyên không âm, đếm số lần nhận $V\leftarrow W$; tính thêm phần dư trên bảng cuối, kể cả khi $K=0$. Ví dụ độ lệch $0.9$ đã nằm cuối notes B04 nên không lặp trên mặt B05.

#### L04-B06 — Hội tụ của đánh giá lặp

- **Vai trò và mục tiêu:** Bảo đảm có điều kiện; MT2
- **Luận điểm trung tâm:** Chiết khấu nhỏ hơn 1 làm sai số đánh giá co lại và biến phần dư thành chặn sai số.
- **Ý chính:** Với MDP hữu hạn và thưởng bị chặn, $T_\pi$ co theo chuẩn vô cùng. Vì vậy lặp đồng bộ từ bảng hữu hạn bất kỳ hội tụ đến $v_\pi$. Nếu $\Delta_\pi(V)\le\eta$, sai số không quá $\eta/(1-\gamma)$.
- **Ví dụ/hình dự kiến:** Công thức co và chặn phần dư; không dùng đồ thị dữ liệu thực nghiệm.
- **Hình thức hóa:** HT4: $\|T_\pi U-T_\pi V\|_\infty\le\gamma\|U-V\|_\infty$; $\|V-v_\pi\|_\infty\le \Delta_\pi(V)/(1-\gamma)$.
- **Kết nối vào:** Phần dư đo được cần được liên hệ với sai số so với nghiệm chính xác.
- **Kết nối ra:** Bảo đảm hội tụ được đối chiếu với nghiệm giải trực tiếp của ví dụ nhỏ.
- **Nguồn:** NG1, tr. 14, 31–32 (mở rộng lập luận sang $T_\pi$); NG2, §4.1, tr. in 74–75 (PDF 96–97).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Tổng có trọng số xác suất không tăng độ lệch lớn nhất; hệ số $\gamma$ tạo tính co. Chặn phần dư suy ra từ bất đẳng thức tam giác và tính co. Với $\gamma=1$, lập luận này không áp dụng; có trạng thái kết thúc riêng lẻ chưa đủ bảo đảm mọi chính sách kết thúc.

#### L04-B07 — Giá trị chính xác của chính sách ban đầu

- **Vai trò và mục tiêu:** Ứng dụng và đối chiếu; MT2
- **Luận điểm trung tâm:** Giải hệ Bellman cho nghiệm chính xác để đối chiếu bảng lặp.
- **Ý chính:** Từ $x=1+0.9x$ suy ra $x=10$; từ $y=2+0.9x$ suy ra $y=11$. Vậy $v_{\pi_0}=(10,11)$. Các bảng $V_1,V_2$ còn thấp vì mới chứa các phần thưởng đầu.
- **Ví dụ/hình dự kiến:** Hai phương trình và nghiệm; bảng nhỏ $V_0,V_1,V_2,v_{\pi_0}$.
- **Hình thức hóa:** HT5: $(I-\gamma P_\pi)v_\pi=r_\pi$; công thức ma trận đặt trong ghi chú với $P_\pi\in\mathbb R^{n\times n}$, $r_\pi,v_\pi\in\mathbb R^n$.
- **Kết nối vào:** Bảo đảm hội tụ được đối chiếu với nghiệm giải trực tiếp của ví dụ nhỏ.
- **Kết nối ra:** Nghiệm và bảng ước lượng cho phép kiểm tra riêng thao tác cập nhật và chặn sai số.
- **Nguồn:** NG1, tr. 6, 18; NG2, §4.1, tr. in 74 (PDF 96).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Với chính sách cố định, các phương trình tuyến tính ghép tất cả trạng thái. Giải trực tiếp và đánh giá lặp cùng nhằm tìm một nghiệm, nhưng có chi phí khác nhau. Nghiệm này sẽ làm giá trị tiếp nối khi so sánh hành động. $P_\pi$ chỉ chuyển giữa trạng thái chưa kết thúc, tổng hàng không vượt $1$; $r_\pi$ tính cả thưởng khi chuyển vào đích qua tổng trên $\mathcal S^+$.

#### L04-B08 — Kiểm tra đánh giá chính sách

- **Vai trò và mục tiêu:** Kiểm tra đánh giá chính sách; MT2
- **Luận điểm trung tâm:** Kết quả đánh giá phụ thuộc việc giữ nguyên bảng ở vế phải.
- **Ý chính:** Với $\pi_0=(a,a)$, $\gamma=0.9$ và $V_2=(1.9,2.9)$, xét lượt đồng bộ tiếp theo.
- **Ví dụ/hình dự kiến:** Bảng cũ hai ô và hai ô kết quả trống; lời giải trong ghi chú.
- **Hình thức hóa:** Dùng HT2 và HT4 đã học.
- **Kết nối vào:** Nghiệm và bảng ước lượng cho phép kiểm tra riêng thao tác cập nhật và chặn sai số.
- **Kết nối ra:** Giá trị của chính sách cố định đã có; phần điều khiển cần so sánh các hành động khác.
- **Nguồn:** NG1, tr. 14, 17–18; câu kiểm tra suy từ dữ kiện nguồn.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Chuẩn vô cùng lấy độ lệch lớn nhất giữa các trạng thái. Mức thay đổi của lượt hiện tại không bằng sai số thật so với nghiệm chưa biết.
- **Yêu cầu trên mặt trang:** Câu hỏi: Tính $V_3$. Tính $\Delta_{\pi_0}(V_2)$ và chặn sai số của $V_2$. Giải thích vì sao chưa được gọi $V_3$ là $v_{\pi_0}$.
- **Kiến thức được đo:** MT2; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** $V_3=(2.71,3.71)$; $\Delta_{\pi_0}(V_2)=0.81$; chặn sai số $0.81/0.1=8.1$. $V_3$ chưa thỏa điểm bất động và khác $(10,11)$.
- **Tiêu chí đánh giá:** Tính đúng hai ô từ cùng $V_2$, lấy chuẩn đúng và gắn chặn với đúng bảng $V_2$.
- **Thời gian hoạt động:** 1 phút lập phép tính, 1 phút trả lời, 1 phút đối chiếu; đã tính trong thời lượng của trang.

### Mạch C. Cải thiện chính sách

Chức năng: Phát triển kiến thức và luyện tập. Đầu vào: Giá trị của chính sách đã đánh giá. Đầu ra: Chính sách mới không kém; nhu cầu đánh giá lại chính sách mới. Mục tiêu: MT3. Thời lượng: 20 phút; kiểm tra riêng L04-C07.

#### L04-C01 — Đổi hành động ở bước đầu

- **Vai trò và mục tiêu:** Vấn đề và trực giác; MT3
- **Luận điểm trung tâm:** Giá trị của chính sách hiện tại cho phép đánh giá một thay đổi hành động ở bước đầu.
- **Ý chính:** Đã biết $v_{\pi_0}=(10,11)$. Bài toán điều khiển: xác định có nên đổi hành động của $\pi_0$ tại một trạng thái. Xét chọn một hành động khác tại bước đầu, rồi theo $\pi_0$ ở mọi bước sau. Giá trị nhìn trước $r+\gamma\,v_{\pi_0}(s')$ là đại lượng so sánh.
- **Ví dụ/hình dự kiến:** Hai nhánh hành động từ một trạng thái, mỗi nhánh nối với hộp tiếp tục theo $\pi_0$.
- **Hình thức hóa:** Chưa viết định nghĩa $q_\pi$; thiết lập nghĩa của phần tiếp nối.
- **Kết nối vào:** Giá trị của chính sách cố định đã có; phần điều khiển cần so sánh các hành động khác.
- **Kết nối ra:** So sánh một thay đổi tại bước đầu được tính trên hai nhánh của trạng thái thứ hai.
- **Nguồn:** NG1, tr. 19; NG2, §4.2, tr. in 76, 78 (PDF 98, 100).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Thử một hành động rồi tiếp tục theo chính sách cũ khác với thay chính sách vĩnh viễn. Định lý cải thiện sẽ nối hai phát biểu đó.

#### L04-C02 — So sánh hai nhánh hành động

- **Vai trò và mục tiêu:** Ví dụ tính tay; MT3
- **Luận điểm trung tâm:** Tại $s_1$, hành động $b$ có giá trị nhìn trước lớn hơn khi dùng cùng giá trị tiếp nối.
- **Ý chính:** Chọn $a$: $2+0.9\cdot10=11$. Chọn $b$: $3+0.9\cdot11=12.9$. Cả hai phép tính đều tiếp tục theo $\pi_0$ sau bước đầu.
- **Ví dụ/hình dự kiến:** SVG dp04-one-step-choice.svg: hai nhánh từ $s_1$, nhãn thưởng 2/3 và giá trị tiếp nối 10/11; hai kết quả lớn.
- **Hình thức hóa:** Phép tính cụ thể chuẩn bị HT6.
- **Kết nối vào:** So sánh một thay đổi tại bước đầu được tính trên hai nhánh của trạng thái thứ hai.
- **Kết nối ra:** Hai giá trị nhìn trước xác định đối tượng được gọi là giá trị hành động theo chính sách.
- **Nguồn:** NG1, tr. 17–19; NG2, (4.6), tr. in 78 (PDF 100).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Số 12.9 chưa phải $v_{\pi_1}(s_1)$, vì chính sách tiếp nối trong phép tính vẫn là $\pi_0$. Giá trị sau khi đổi vĩnh viễn sang $b$ sẽ phải được đánh giá lại.

#### L04-C03 — Hàm giá trị hành động

- **Vai trò và mục tiêu:** Định nghĩa và ánh xạ; MT3
- **Luận điểm trung tâm:** Giá trị hành động cố định hành động đầu và cố định chính sách từ bước kế tiếp.
- **Ý chính:** $q_\pi(s,a)$ được định nghĩa cho $s\in\mathcal S$, $a\in\mathcal A(s)$. $v_\pi(s)$ là trung bình của $q_\pi(s,a)$ theo chính sách. Trong ví dụ, $q_{\pi_0}(s_1,a)=11$, $q_{\pi_0}(s_1,b)=12.9$.
- **Ví dụ/hình dự kiến:** Công thức một bước trên cùng; phép tính từ ví dụ nối bằng nhãn từng thành phần.
- **Hình thức hóa:** HT6: $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_\pi(s')]$; $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$.
- **Kết nối vào:** Hai giá trị nhìn trước xác định đối tượng được gọi là giá trị hành động theo chính sách.
- **Kết nối ra:** Giá trị hành động cung cấp tiêu chí lựa chọn chính sách mới tại mọi trạng thái.
- **Nguồn:** NG1, tr. 5–6, 19; NG2, §4.2, (4.6), tr. in 78 (PDF 100).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Thay $v_\pi(s')$ bằng trung bình theo chính sách cho phương trình $q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma\sum_{a'}\pi(a'\mid s')q_\pi(s',a')]$. Hành động đầu được ấn định, còn hành động kế tiếp được lấy trung bình theo $\pi$.

#### L04-C04 — Cải thiện chính sách tham lam

- **Vai trò và mục tiêu:** Quy tắc và định lý; MT3
- **Luận điểm trung tâm:** Chọn hành động cực đại theo giá trị của chính sách cũ tạo chính sách không kém tại mọi trạng thái.
- **Ý chính:** Đầu vào là giá trị chính xác $v_\pi$. Với mọi trạng thái, tính các $q_\pi$ rồi chọn $\pi'(s)\in\arg\max_a q_\pi(s,a)$. Giá trị $v_\pi$ được giữ nguyên trong toàn bộ bước chọn. Nếu hành động cũ cùng đạt cực đại thì giữ nó.
- **Ví dụ/hình dự kiến:** Hai cột đầu vào cố định $v_\pi$ và đầu ra $\pi'$; không cập nhật giá trị xen giữa các trạng thái.
- **Hình thức hóa:** HT7: Nếu $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$, thì $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s$. Giả thiết: MDP hữu hạn chiết khấu, chính sách dừng xác định, giá trị chính xác.
- **Kết nối vào:** Giá trị hành động cung cấp tiêu chí lựa chọn chính sách mới tại mọi trạng thái.
- **Kết nối ra:** Bảo đảm không giảm giá trị cần lập luận vượt ra ngoài một phép thử số.
- **Nguồn:** NG1, tr. 19–21; NG2, §4.2, (4.7)–(4.9), tr. in 78–79 (PDF 100–101); Ex. 4.4, tr. in 82 (PDF 104).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Bất đẳng thức là so sánh theo từng trạng thái. Nếu điều kiện cải thiện nghiêm tại một trạng thái, giá trị mới cũng tăng nghiêm tại trạng thái đó. Quy tắc giữ hành động cũ khi hòa loại bỏ việc đổi chính sách chỉ do hòa và là một cách bảo đảm dừng hữu hạn; đây không phải cách xử lý hòa duy nhất.

#### L04-C05 — Chứng minh định lý cải thiện

- **Vai trò và mục tiêu:** Phác thảo chứng minh; MT3
- **Luận điểm trung tâm:** Tính đơn điệu truyền lợi ích của lựa chọn một bước đến toàn bộ giá trị chính sách mới.
- **Ý chính:** Từ $v_\pi\le T_{\pi'}v_\pi$, áp dụng $T_{\pi'}$ nhiều lần. Mỗi lần giữ chiều bất đẳng thức. Dãy lặp hội tụ đến $v_{\pi'}$ nhờ tính co đã học.
- **Ví dụ/hình dự kiến:** Chuỗi ba bất đẳng thức lớn; mũi tên giới hạn với nhãn $0\le\gamma<1$.
- **Hình thức hóa:** HT7, chứng minh: $v_\pi\le T_{\pi'}v_\pi\le(T_{\pi'})^2v_\pi\le\cdots\to v_{\pi'}$. Đơn điệu: $U\le V\Rightarrow T_{\pi'}U\le T_{\pi'}V$.
- **Kết nối vào:** Bảo đảm không giảm giá trị cần lập luận vượt ra ngoài một phép thử số.
- **Kết nối ra:** Tính đơn điệu cho phép áp dụng quy tắc trên toàn bộ mô hình hai trạng thái.
- **Nguồn:** NG1, tr. 21; NG2, §4.2, tr. in 78–79 (PDF 100–101).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Hệ số xác suất và $\gamma$ không âm bảo toàn thứ tự. Giá trị bị chặn cùng $\gamma<1$ bảo đảm phần tiếp nối xa mất ảnh hưởng. Một ví dụ số chỉ minh họa điều kiện; chuỗi bất đẳng thức mới cung cấp lập luận tổng quát.

#### L04-C06 — Lần cải thiện thứ nhất

- **Vai trò và mục tiêu:** Ứng dụng; MT3
- **Luận điểm trung tâm:** Cải thiện đồng thời tại hai trạng thái tạo $(a,b)$ và cần đánh giá lại giá trị.
- **Ý chính:** Tại $s_0$: $q_{\pi_0}(s_0,a)=10$, $q_{\pi_0}(s_0,b)=9.9$, nên giữ $a$. Tại $s_1$: chọn $b$. Do đó $\pi_1=(a,b)$. Giải hệ $x=1+0.9x$, $y=3+0.9y$ được $v_{\pi_1}=(10,30)$.
- **Ví dụ/hình dự kiến:** Bảng HTML hai trạng thái × hai hành động; bên dưới ghi chính sách mới và giá trị mới.
- **Hình thức hóa:** Áp dụng HT6–HT7 và hệ Bellman HT1; không thêm định nghĩa.
- **Kết nối vào:** Tính đơn điệu cho phép áp dụng quy tắc trên toàn bộ mô hình hai trạng thái.
- **Kết nối ra:** Giá trị sau lần đổi chính sách cung cấp dữ kiện cho một lần lựa chọn mới.
- **Nguồn:** NG1, tr. 18–19; NG2, §4.2–4.3, tr. in 79–80 (PDF 101–102); bước đánh giá giữa hai chính sách được khôi phục.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Giá trị 30 khác với giá trị nhìn trước 12.9 vì từ $s_1$ chính sách mới chọn $b$ ở mọi lần quay lại. Kết quả $(10,30)$ vẫn có thể tạo lựa chọn tốt hơn tại $s_0$.

#### L04-C07 — Kiểm tra cải thiện chính sách

- **Vai trò và mục tiêu:** Kiểm tra cải thiện; MT3
- **Luận điểm trung tâm:** Tham lam phải được tính theo giá trị của chính sách đang được cải thiện.
- **Ý chính:** Cho $\pi_1=(a,b)$ và $v_{\pi_1}=(10,30)$ trong cùng mô hình hai trạng thái.
- **Ví dụ/hình dự kiến:** Bảng mô hình và giá trị mới; không hiển thị đáp án ban đầu.
- **Hình thức hóa:** Dùng HT6 và HT7.
- **Kết nối vào:** Giá trị sau lần đổi chính sách cung cấp dữ kiện cho một lần lựa chọn mới.
- **Kết nối ra:** Lần cải thiện kế tiếp cho thấy nhu cầu lặp lại hai thao tác trên chính sách mới.
- **Nguồn:** NG1, tr. 17–19; câu kiểm tra từ bước trung gian được khôi phục.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Hành động tối đa hóa phần thưởng tức thời ở $s_0$ là $a$, nhưng phần giá trị tiếp nối thay đổi lựa chọn.
- **Yêu cầu trên mặt trang:** Câu hỏi: Tính giá trị hai hành động tại $s_0$ theo $\pi_1$, rồi xác định hành động mới. Giải thích sự khác biệt so với cải thiện từ $\pi_0$.
- **Kiến thức được đo:** MT3; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** $q_{\pi_1}(s_0,a)=10$; $q_{\pi_1}(s_0,b)=27$; chọn $b$. Giá trị tiếp nối tại $s_1$ tăng từ 11 lên 30, nên chính sách mới chuyển từ $s_0$ sang $s_1$.
- **Tiêu chí đánh giá:** Giữ cùng $v_{\pi_1}$ trong cả hai nhánh, tính đúng và giải thích bằng phần tiếp nối.
- **Thời gian hoạt động:** 1 phút lập phép tính, 1 phút trả lời, 1 phút đối chiếu; đã tính trong thời lượng của trang.

### Mạch D. Lặp chính sách

Chức năng: Phát triển thuật toán và luyện tập. Đầu vào: Đánh giá, cải thiện, tính co theo chính sách. Đầu ra: Chính sách ổn định và điều kiện tối ưu; giới hạn chi phí đánh giá đầy đủ. Mục tiêu: MT4. Thời lượng: 18 phút; kiểm tra riêng L04-D06.

#### L04-D01 — Chu trình lặp chính sách

- **Vai trò và mục tiêu:** Vấn đề và trực giác; MT4
- **Luận điểm trung tâm:** Một lần cải thiện thay đổi giá trị, vì vậy quá trình phải lặp lại trên chính sách mới.
- **Ý chính:** Đánh giá $\pi_i$ cho $v_{\pi_i}$; cải thiện theo giá trị đó cho $\pi_{i+1}$. Khi chính sách thay đổi, bảng của chính sách cũ không còn là nghiệm đánh giá của chính sách mới.
- **Ví dụ/hình dự kiến:** SVG dp04-policy-iteration.svg: chu trình chính sách → đánh giá → giá trị → cải thiện → chính sách; mũi tên có sản phẩm.
- **Hình thức hóa:** $i$ đếm lần cải thiện chính sách; phân biệt với $k$ đếm lượt đánh giá và $t$ đếm bước tương tác.
- **Kết nối vào:** Lần cải thiện kế tiếp cho thấy nhu cầu lặp lại hai thao tác trên chính sách mới.
- **Kết nối ra:** Chu trình tổng quát được lần theo bằng toàn bộ chuỗi chính sách và giá trị của ví dụ.
- **Nguồn:** NG1, tr. 13, 19–20; NG2, §4.3, tr. in 80 (PDF 102).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Lặp chính sách giải bài toán điều khiển với mô hình đã biết. Hai phép toán thay đổi hai đối tượng khác nhau; giá trị hoặc chính sách phải được giữ cố định đúng lúc.

#### L04-D02 — Lặp chính sách trên MDP hai trạng thái

- **Vai trò và mục tiêu:** Ví dụ một lần lặp đầy đủ; MT4
- **Luận điểm trung tâm:** Hai lần đổi chính sách đưa ví dụ từ $(a,a)$ đến $(b,b)$.
- **Ý chính:** Chuỗi đầy đủ: $(a,a)\to(10,11)\to(a,b)\to(10,30)\to(b,b)\to(27,30)$. Với $(b,b)$, so sánh tại $s_0$: $25.3<27$; tại $s_1$: $26.3<30$; chính sách không đổi.
- **Ví dụ/hình dự kiến:** Bảng ba hàng: chính sách, giá trị được đánh giá, hành động sau cải thiện; bốn giá trị nhìn trước của hàng cuối ở ghi chú.
- **Hình thức hóa:** Áp dụng HT1, HT6–HT7; chưa dùng Bellman tối ưu làm điểm xuất phát.
- **Kết nối vào:** Chu trình tổng quát được lần theo bằng toàn bộ chuỗi chính sách và giá trị của ví dụ.
- **Kết nối ra:** Chuỗi số được chuyển thành quy trình có đầu vào, đầu ra và điều kiện dừng rõ ràng.
- **Nguồn:** NG1, tr. 17–20; số kiểm chứng độc lập.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Dòng giữa $(10,30)$ giải thích việc $s_0$ đổi hành động. Mọi đánh giá trong bảng này là chính xác, nên có thể áp dụng định lý cải thiện và tiêu chuẩn ổn định.

#### L04-D03 — Thuật toán lặp chính sách

- **Vai trò và mục tiêu:** Quy trình đầy đủ; MT4
- **Luận điểm trung tâm:** Lặp chính sách chính xác xen kẽ giải hệ Bellman và cải thiện với quy tắc phá hòa ổn định.
- **Ý chính:** Đầu vào $p,\gamma$ và chính sách xác định $\pi_0$; tùy chọn ngân sách số lần cải thiện $I_{\max}$. Mỗi lần: giải chính xác hệ đánh giá; giữ nguyên $v_{\pi_i}$; chọn hành động cực đại cho từng trạng thái, ưu tiên hành động cũ khi hòa. Nếu toàn bộ chính sách không đổi, trả $(\pi_i,v_{\pi_i})$ cùng trạng thái ổn định. Nếu hết ngân sách, trả cặp vừa đánh giá và trạng thái chưa chứng nhận; không trả chính sách mới với giá trị của chính sách cũ.
- **Ví dụ/hình dự kiến:** Giả mã HTML, tách đánh giá và cải thiện thành hai khối nối nhau; khoảng 9 dòng chính.
- **Hình thức hóa:** HT8: thuật toán lặp chính sách chính xác. Bản đánh giá gần đúng gọi thủ tục HT3 nhưng có bảo đảm dừng khác.
- **Kết nối vào:** Chuỗi số được chuyển thành quy trình có đầu vào, đầu ra và điều kiện dừng rõ ràng.
- **Kết nối ra:** Kết quả không đổi chính sách được kiểm tra bằng điều kiện Bellman tối ưu.
- **Nguồn:** NG1, tr. 20, 33–34; NG2, §4.3, tr. in 80, Ex. 4.4 tr. in 82 (PDF 102, 104).
- **Thời lượng:** 4 phút
- **Ghi chú học thuật dự kiến:** Giải hệ tuyến tính là cách xác định đánh giá chính xác trên bài hữu hạn. Với số thực máy tính hoặc đánh giá lặp theo ngưỡng, kết quả là gần đúng; phần dư của bảng cuối cần được báo. Một lần lặp ngoài có thể gồm nhiều lượt đánh giá.

#### L04-D04 — Chính sách ổn định là tối ưu

- **Vai trò và mục tiêu:** Định lý và điều kiện điểm bất động; MT4
- **Luận điểm trung tâm:** Chính sách tham lam theo chính giá trị của nó thỏa phương trình Bellman tối ưu.
- **Ý chính:** Định nghĩa $v_*(s)=\max_\pi v_\pi(s)$, $q_*(s,a)=\max_\pi q_\pi(s,a)$. Nếu đánh giá chính xác và bước cải thiện không đổi chính sách, thì $v_\pi(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_\pi(s')]$. Trong MDP hữu hạn chiết khấu, nghiệm là $v_*$ và có chính sách tối ưu dừng, xác định. Áp dụng: với $(b,b)$ và giá trị $(27,30)$, các cực đại lần lượt bằng 27 và 30 nên chính sách này đạt điều kiện.
- **Ví dụ/hình dự kiến:** Một đẳng thức nối đánh giá với cực đại; định nghĩa $q_*$ và lập luận phụ trong ghi chú để mặt trang có một kết quả chính.
- **Hình thức hóa:** HT9: điều kiện tối ưu Bellman và tồn tại chính sách tối ưu dừng xác định; nêu giả thiết hữu hạn, thưởng bị chặn, $\gamma<1$.
- **Kết nối vào:** Kết quả không đổi chính sách được kiểm tra bằng điều kiện Bellman tối ưu.
- **Kết nối ra:** Điều kiện ổn định cần đi cùng lập luận dừng hữu hạn và độ chính xác đánh giá.
- **Nguồn:** NG1, tr. 7–9, 33; NG2, §4.2–4.3, tr. in 79–80 (PDF 101–102); §3.6.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Tập hành động hữu hạn bảo đảm đạt cực đại. Chính sách lấy hành động cực đại theo nghiệm Bellman có giá trị bằng nghiệm đó nhờ tính duy nhất của phương trình đánh giá. Tính duy nhất của nghiệm tối ưu sẽ được giải thích bằng toán tử co trong lặp giá trị.

#### L04-D05 — Dừng hữu hạn và đánh giá gần đúng

- **Vai trò và mục tiêu:** Bảo đảm và giới hạn; MT4
- **Luận điểm trung tâm:** Dừng hữu hạn của lặp chính sách cần đánh giá chính xác và tránh đổi hành động chỉ vì hòa.
- **Ý chính:** Số chính sách xác định là $\prod_s|\mathcal A(s)|$. Nếu chính sách đổi dưới quy tắc phá hòa ổn định, ít nhất một trạng thái có cải thiện nghiêm; không thể có chuỗi như vậy vô hạn. Đánh giá theo ngưỡng chỉ cho bảng gần đúng, nên chính sách không đổi chưa chứng nhận tối ưu chính xác.
- **Ví dụ/hình dự kiến:** Hai cột: giả thiết của kết quả lý thuyết và đầu ra thực hành cần kiểm tra; không dùng nhãn quảng bá.
- **Hình thức hóa:** HT10: dừng hữu hạn của HT8; phân biệt với dừng do ngân sách hoặc ngưỡng của HT3.
- **Kết nối vào:** Điều kiện ổn định cần đi cùng lập luận dừng hữu hạn và độ chính xác đánh giá.
- **Kết nối ra:** Một bảng gần đúng cung cấp trường hợp kiểm tra giới hạn của tiêu chuẩn ổn định.
- **Nguồn:** NG1, tr. 33–34; NG2, §4.3, tr. in 80, Ex. 4.4 tr. in 82 (PDF 102, 104).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Với cùng số hành động $m$ tại $n$ trạng thái, số chính sách bằng $m^n$. Tính hữu hạn riêng nó không loại dao động giữa các chính sách cùng giá trị. Nếu bảng ước lượng bằng không, chính sách $(a,b)$ đã tham lam theo bảng đó nhưng chưa tối ưu.

#### L04-D06 — Kiểm tra điều kiện dừng

- **Vai trò và mục tiêu:** Kiểm tra lặp chính sách; MT4
- **Luận điểm trung tâm:** Ổn định của chính sách chỉ có ý nghĩa cùng độ chính xác của bảng dùng để cải thiện.
- **Ý chính:** Trong mô hình hai trạng thái, một chương trình đang giữ $\pi=(a,b)$ và bảng gần đúng $V=(0,0)$. Bước tham lam vẫn cho $(a,b)$.
- **Ví dụ/hình dự kiến:** Hai đầu vào hiện rõ; gợi ý tính bốn tổng thưởng một bước trong ghi chú.
- **Hình thức hóa:** Dùng HT6, HT8–HT10; chưa yêu cầu toán tử tối ưu có tên.
- **Kết nối vào:** Một bảng gần đúng cung cấp trường hợp kiểm tra giới hạn của tiêu chuẩn ổn định.
- **Kết nối ra:** Chi phí đánh giá đầy đủ và giới hạn dừng gần đúng dẫn tới cập nhật điều khiển cắt ngắn.
- **Nguồn:** NG1, tr. 17–20, 34; phản ví dụ tính trực tiếp từ dữ kiện nguồn.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Phép chọn hành động có thể đúng đối với bảng sai. Để áp dụng định lý dừng chính xác, bảng phải là giá trị của chính sách đang giữ.
- **Yêu cầu trên mặt trang:** Câu hỏi: Xác định bốn giá trị nhìn trước theo $V$. Kết luận chương trình đã tìm được chính sách tối ưu có hợp lệ hay không; nêu căn cứ.
- **Kiến thức được đo:** MT4; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** Các điểm là $1,0,2,3$, nên $(a,b)$ tham lam theo $V$. Nhưng $v_{(a,b)}=(10,30)$ và chính sách $(b,b)$ có giá trị $(27,30)$; kết luận tối ưu không hợp lệ. Thiếu đánh giá chính xác hoặc chứng nhận sai số thích hợp.
- **Tiêu chí đánh giá:** Phân biệt đúng bảng $V$ với $v_\pi$ và dùng một so sánh giá trị đã biết để bác kết luận.
- **Thời gian hoạt động:** 1 phút lập phép tính, 1 phút trả lời, 1 phút đối chiếu; đã tính trong thời lượng của trang.

### Mạch E. Lặp giá trị

Chức năng: Phát triển thuật toán và luyện tập. Đầu vào: Lặp chính sách và nhu cầu cắt ngắn đánh giá. Đầu ra: Cập nhật tối ưu, phần dư và chính sách trích; nhu cầu phân bổ công việc. Mục tiêu: MT5. Thời lượng: 22 phút; kiểm tra riêng L04-E08.

#### L04-E01 — Cắt ngắn bước đánh giá

- **Vai trò và mục tiêu:** Vấn đề và trực giác; MT5
- **Luận điểm trung tâm:** Lặp giá trị chọn hành động tốt nhất trong mỗi cập nhật mà không hoàn tất đánh giá một chính sách.
- **Ý chính:** Lặp chính sách phải giải hoặc lặp nhiều lượt đánh giá trước mỗi lần cải thiện. Có thể dùng bảng hiện tại để tính các nhánh hành động, lấy nhánh lớn nhất rồi cập nhật giá trị. Bảng mới tiếp tục làm giá trị tiếp nối cho lượt sau.
- **Ví dụ/hình dự kiến:** Sơ đồ hai nhánh hành động hội tụ vào phép cực đại và bảng mới; đối chiếu sơ đồ đánh giá trung bình.
- **Hình thức hóa:** Chưa đưa $T_*$; trực giác nối từ quy trình HT8.
- **Kết nối vào:** Chi phí đánh giá đầy đủ và giới hạn dừng gần đúng dẫn tới cập nhật điều khiển cắt ngắn.
- **Kết nối ra:** Phép chọn nhánh lớn nhất được thử trên cùng bốn chuyển tiếp trước khi viết toán tử.
- **Nguồn:** NG1, tr. 23; NG2, §4.4, tr. in 82–83 (PDF 104–105).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Cập nhật tối ưu gộp lựa chọn tham lam với một bước dùng giá trị tiếp nối. Nó không đòi bảng hiện tại phải bằng giá trị chính xác của một chính sách.

#### L04-E02 — Hai lượt lặp giá trị đồng bộ

- **Vai trò và mục tiêu:** Ví dụ tính tay; MT5
- **Luận điểm trung tâm:** Phép cực đại thay việc giữ hành động của chính sách trong mỗi lượt đồng bộ.
- **Ý chính:** $V_0=(0,0)$ cho $V_1=(\max(1,0),\max(2,3))=(1,3)$. Dùng $V_1$: tại $s_0$ các điểm là $1.9,2.7$; tại $s_1$ là $2.9,5.7$; do đó $V_2=(2.7,5.7)$.
- **Ví dụ/hình dự kiến:** Bảng hai trạng thái, hai nhánh và cực đại; phân biệt rõ bảng dùng để tính và bảng kết quả.
- **Hình thức hóa:** Dữ kiện chuẩn bị HT11; không gọi các điểm theo bảng tùy ý là $q_\pi$.
- **Kết nối vào:** Phép chọn nhánh lớn nhất được thử trên cùng bốn chuyển tiếp trước khi viết toán tử.
- **Kết nối ra:** Phép cực đại từ bảng tùy ý cần ký hiệu riêng để phân biệt với giá trị hành động chính xác.
- **Nguồn:** NG1, tr. 17, 23–24; số suy tính từ mô hình nguồn đã kiểm chứng.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Lượt đầu đánh giá chính sách $(a,a)$ cho $(1,2)$, còn lặp giá trị cho $(1,3)$. Sự khác biệt tại $s_1$ đến từ phép cực đại trên các hành động.

#### L04-E03 — Toán tử Bellman tối ưu

- **Vai trò và mục tiêu:** Hình thức hóa; MT5
- **Luận điểm trung tâm:** Toán tử tối ưu trả giá trị lớn nhất của các nhánh nhìn trước từ cùng một bảng.
- **Ý chính:** Định nghĩa $Q_V(s,a)$ là giá trị nhìn trước một bước từ bảng $V$. $(T_*V)(s)=\max_a Q_V(s,a)$ và $V_{k+1}=T_*V_k$. Khi $V=v_\pi$, có $Q_V=q_\pi$; với $V=v_*$ có $Q_V=q_*$.
- **Ví dụ/hình dự kiến:** Một định nghĩa phụ $Q_V$ và công thức toán tử; sơ đồ max khác nhãn với sơ đồ kỳ vọng.
- **Hình thức hóa:** HT11: $Q_V(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]$; $v_*=T_*v_*$.
- **Kết nối vào:** Phép cực đại từ bảng tùy ý cần ký hiệu riêng để phân biệt với giá trị hành động chính xác.
- **Kết nối ra:** Toán tử tối ưu được đặt trong vòng lặp và ghép với chính sách trích từ bảng trả về.
- **Nguồn:** NG1, tr. 8, 10, 23; NG2, §4.4, (4.10), tr. in 83 (PDF 105); ký hiệu $Q_V$ do bài giảng định nghĩa.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Phương trình cho giá trị hành động tối ưu là $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma\max_{a'}q_*(s',a')]$. Với trạng thái kết thúc, giá trị tiếp nối bằng 0 và không lấy cực đại trên tập hành động rỗng.

#### L04-E04 — Thuật toán lặp giá trị đồng bộ

- **Vai trò và mục tiêu:** Quy trình đầy đủ; MT5
- **Luận điểm trung tâm:** Thuật toán trả bảng giá trị, chính sách tham lam theo chính bảng đó và phần dư kiểm chứng.
- **Ý chính:** Đặt $\Delta_*(V)=\|T_*V-V\|_\infty$ trước khi xét điều kiện dừng. Đầu vào $p,\gamma$, ngưỡng $\eta>0$, ngân sách $K$. Khởi tạo $V=0$, giữ giá trị kết thúc bằng 0. Tính $W=T_*V$ từ bản chụp cố định. Bước 3 gộp hai điều kiện dừng như thuật toán đánh giá: nếu $\|W-V\|_\infty\le\eta$ hoặc đã nhận $K$ bảng mới, trả $V$, phần dư và kết quả so ngưỡng; ngược lại nhận $W$ làm bảng hiện tại. Chính sách tham lam trích từ chính bảng trả về.
- **Ví dụ/hình dự kiến:** Giả mã 8–10 dòng; phép trích chính sách bên ngoài vòng cập nhật; không dùng khối mã chương trình.
- **Hình thức hóa:** HT12: $\Delta_*(V)=\|T_*V-V\|_\infty$; $\pi_V(s)\in\arg\max_aQ_V(s,a)$.
- **Kết nối vào:** Toán tử tối ưu được đặt trong vòng lặp và ghép với chính sách trích từ bảng trả về.
- **Kết nối ra:** Vòng lặp có tiêu chuẩn dừng cần bảo đảm rằng toán tử tiến tới đúng điểm bất động.
- **Nguồn:** NG1, tr. 24, 34; NG2, §4.4, tr. in 83 (PDF 105); điều chỉnh phần dư để đúng bảng trả về.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Nếu tính $W=T_*V$ rồi trả $W$, mức thay đổi vừa đo là phần dư của $V$ cũ. Bản giả mã này trả đúng bảng đã kiểm hoặc tính lại phần dư khi bảng cuối đã đổi. Mọi phép cập nhật dùng mô hình, không dùng dữ liệu lấy mẫu.

#### L04-E05 — Tính co và hội tụ của lặp giá trị

- **Vai trò và mục tiêu:** Định lý và phác thảo chứng minh; MT5
- **Luận điểm trung tâm:** Cực đại theo hành động vẫn bảo toàn tính co khi hệ số chiết khấu nhỏ hơn 1.
- **Ý chính:** Dùng $|\max_a x_a-\max_a y_a|\le\max_a|x_a-y_a|$. Kết hợp tổng xác suất bằng 1 cho hệ số co $\gamma$. Từ điểm bất động $v_*$, sai số sau $k$ lượt bị chặn bởi $\gamma^k\|V_0-v_*\|_\infty$.
- **Ví dụ/hình dự kiến:** Hai công thức lớn; bất đẳng thức cực đại ở ghi chú hoặc dòng phụ ngắn.
- **Hình thức hóa:** HT13: $\|T_*U-T_*V\|_\infty\le\gamma\|U-V\|_\infty$; $\|V_k-v_*\|_\infty\le\gamma^k\|V_0-v_*\|_\infty$.
- **Kết nối vào:** Vòng lặp có tiêu chuẩn dừng cần bảo đảm rằng toán tử tiến tới đúng điểm bất động.
- **Kết nối ra:** Bảo đảm của cập nhật tối ưu được áp dụng để đọc sự lan truyền giá trị trên lưới.
- **Nguồn:** NG1, tr. 31–32; NG2, §4.4, tr. in 83 (PDF 105) cho kết quả hội tụ, chứng minh co theo nguồn bài giảng.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** MDP hữu hạn, thưởng bị chặn và $0\le\gamma<1$ được giữ suốt lập luận. Dãy hội tụ từ mọi bảng hữu hạn; số lượt hữu hạn thường chỉ cho xấp xỉ. Chặn theo $v_*$ giải thích lý thuyết nhưng chưa là phép kiểm thực hành vì chưa biết $v_*$.

#### L04-E06 — Lan truyền giá trị trên lưới năm ô

- **Vai trò và mục tiêu:** Ứng dụng trực quan; MT5
- **Luận điểm trung tâm:** Cập nhật đồng bộ lan truyền phần thưởng kết thúc lùi từng bước qua lưới.
- **Ý chính:** Lưới $c_1,\ldots,c_5$; $c_5$ kết thúc, $V(c_5)=0$. Trái/phải; thưởng thường $-1$, riêng chuyển $c_4\to c_5$ nhận $10$; $\gamma=0.9$. Đi trái ở $c_1$ giữ nguyên trạng thái và nhận $-1$. Từ $V_0=0$, các bảng lần lượt: $(-1,-1,-1,10,0)$; $(-1.9,-1.9,8,10,0)$; $(-2.71,6.2,8,10,0)$; $(4.58,6.2,8,10,0)$. Tập hành động trái/phải được ghi tường minh trên mặt trang; mũi tên chỉ biểu diễn chính sách tối ưu.
- **Ví dụ/hình dự kiến:** SVG dp04-five-cell.svg có biên trái và đích; bảng HTML bốn lượt; nhãn từng ô, mũi tên hướng phải không chỉ dùng màu.
- **Hình thức hóa:** Áp dụng HT11–HT12; phép tính mẫu $V_2(c_3)=\max(-1.9,8)=8$.
- **Kết nối vào:** Bảo đảm của cập nhật tối ưu được áp dụng để đọc sự lan truyền giá trị trên lưới.
- **Kết nối ra:** Lưới đã đạt điểm bất động ở $V_4$; mô hình hai trạng thái có bảng $V_1=(1,3)$ còn sai số dù chính sách trích đã tối ưu. Phần dư phân biệt hai tình huống.
- **Nguồn:** NG1, tr. 25–28; bổ sung quy ước biên được ghi công khai; số kiểm chứng độc lập.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Phần thưởng 10 xuất hiện một lần khi đi vào $c_5$, không gán giá trị 10 cho trạng thái kết thúc. Nghiệm cuối là điểm bất động; chọn phải ở bốn ô chưa kết thúc. Tính số dùng bảng cũ của cùng lượt. Kiểm lại toàn bảng cho $V_5=V_4$, không chỉ một ô. Điểm chọn trái ở bốn ô là $3.122,3.122,4.58,6.2$, đều nhỏ hơn điểm chọn phải.

#### L04-E07 — Phần dư Bellman và ngưỡng sai số

- **Vai trò và mục tiêu:** Ứng dụng bảo đảm; MT5
- **Luận điểm trung tâm:** Ngưỡng phần dư xác định chặn sai số của chính bảng đang được trả về.
- **Ý chính:** $\|V-v_*\|_\infty\le \Delta_*(V)/(1-\gamma)$. Với $\gamma=0.9$ và sai số mục tiêu $\varepsilon=0.1$, một điều kiện đủ theo chặn phần dư là $\Delta_*(V)\le0.01$. Ở ví dụ hai trạng thái, $V_1=(1,3)$ có chính sách tham lam $(b,b)$ nhưng phần dư 2.7 và sai số giá trị 27.
- **Ví dụ/hình dự kiến:** Thang ba đại lượng: bảng, phần dư, chặn sai số; ví dụ số ngắn. Thẻ ví dụ ghi rõ “Mô hình hai trạng thái”, còn $V_1=(1,3)$ nằm trong thân thẻ.
- **Hình thức hóa:** HT14: bất đẳng thức tam giác cho $\|V-v_*\|_\infty\le \Delta_*(V)+\gamma\|V-v_*\|_\infty$; điều kiện $\Delta_*(V)\le(1-\gamma)\varepsilon$.
- **Kết nối vào:** Lưới đã đạt điểm bất động ở $V_4$; mô hình hai trạng thái có bảng $V_1=(1,3)$ còn sai số dù chính sách trích đã tối ưu. Phần dư phân biệt hai tình huống.
- **Kết nối ra:** Quy tắc đồng bộ và quy ước kết thúc được kiểm tra bằng hai phép tính trên bảng đã cho.
- **Nguồn:** NG1, tr. 31–34; hệ quả được suy và kiểm chứng từ tính co, không gán nguyên công thức cho sách.
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Chính sách có thể đạt tối ưu trước khi bảng giá trị hội tụ. Ngưỡng sai số giá trị không được gọi là ngưỡng tổn thất chính sách. Với mô hình hai trạng thái, lượt 55 đạt phần dư khoảng 0.00913. Chặn sai số tương ứng xấp xỉ 0.0913.

#### L04-E08 — Kiểm tra cập nhật và trạng thái kết thúc

- **Vai trò và mục tiêu:** Kiểm tra lặp giá trị; MT5
- **Luận điểm trung tâm:** Mỗi lượt phải giữ giá trị kết thúc bằng không và dùng đúng bảng tiếp nối.
- **Ý chính:** Trong lưới đã học, cho $V_2=(-1.9,-1.9,8,10,0)$, $\gamma=0.9$ và cùng quy ước thưởng. Dòng dữ kiện ghi rõ “Lưới năm ô” để xác định miền của bảng.
- **Ví dụ/hình dự kiến:** Hiển thị bảng $V_2$ và sơ đồ biên; yêu cầu tính hai ô.
- **Hình thức hóa:** Dùng HT11–HT12.
- **Kết nối vào:** Quy tắc đồng bộ và quy ước kết thúc được kiểm tra bằng hai phép tính trên bảng đã cho.
- **Kết nối ra:** Một lượt tính đúng vẫn có thể tốn kém; chi phí phụ thuộc số trạng thái và nhánh chuyển.
- **Nguồn:** NG1, tr. 25–28; câu kiểm tra từ dữ kiện nguồn.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Phép tính có hai nhánh ở mỗi ô. Đi trái ở biên trái và đi phải từ $c_1$ đều tới giá trị -1.9 của bảng cũ.
- **Yêu cầu trên mặt trang:** Câu hỏi: Tính $V_3(c_1)$ và $V_3(c_2)$. Giải thích vì sao giữ $V_3(c_5)=0$ dù chuyển $c_4\to c_5$ nhận thưởng 10.
- **Kiến thức được đo:** MT5; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** $V_3(c_1)=-2.71$; $V_3(c_2)=\max(-2.71,6.2)=6.2$. Thưởng 10 được nhận trên chuyển tiếp đi vào đích; sau kết thúc không còn phần thưởng tiếp nối.
- **Tiêu chí đánh giá:** Tính đúng từ $V_2$, không dùng giá trị vừa cập nhật và đặt thưởng đúng trên chuyển tiếp.
- **Thời gian hoạt động:** 1 phút lập phép tính, 1 phút trả lời, 1 phút đối chiếu; đã tính trong thời lượng của trang.

### Mạch F. Quy hoạch động trong thực hành

Chức năng: Tổ chức tính toán và giới hạn. Đầu vào: Cập nhật kỳ vọng, lặp chính sách, lặp giá trị. Đầu ra: Lịch cập nhật, điều kiện bao phủ, GPI và giới hạn mô hình. Mục tiêu: MT6. Thời lượng: 16 phút; kiểm tra riêng L04-F06.

#### L04-F01 — Chi phí của một lượt cập nhật

- **Vai trò và mục tiêu:** Giới hạn và trực giác; MT6
- **Luận điểm trung tâm:** Quét toàn bộ mô hình có thể chiếm phần lớn chi phí, nên cách phân bổ cập nhật cần được lựa chọn.
- **Ý chính:** Đặt $n=|\mathcal S|$, tối đa $m$ hành động. Với mô hình đặc đã gộp thưởng kỳ vọng: một lượt lặp giá trị hoặc cải thiện tốn $O(n^2m)$; bảng giá trị cần $O(n)$ bộ nhớ. Mô hình thưa với tối đa $d$ trạng thái kế tiếp giảm lượt lặp giá trị xuống $O(nmd)$.
- **Ví dụ/hình dự kiến:** Bảng so sánh một lượt tính, dữ kiện mô hình và bộ nhớ; chỉ giữ hai chi phí trung tâm trên mặt trang.
- **Hình thức hóa:** HT15: đếm số cặp trạng thái–hành động và số trạng thái tiếp nối; không nêu định lý độ phức tạp đa thức toàn thuật toán.
- **Kết nối vào:** Một lượt tính đúng vẫn có thể tốn kém; chi phí phụ thuộc số trạng thái và nhánh chuyển.
- **Kết nối ra:** Chi phí quét gợi nhu cầu dùng ngay giá trị mới và lựa chọn thứ tự cập nhật.
- **Nguồn:** NG1, tr. 29, 37; NG2, §4.5, §4.7, tr. in 85, 87–88 (PDF 107, 109–110); đếm phép tính từ công thức.
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Đánh giá chính sách xác định tốn $O(n^2)$ mỗi lượt; giải hệ đặc bằng khử Gauss tốn $O(n^3)$. Chính sách ngẫu nhiên có thể gộp $P_\pi,r_\pi$ trước, nhưng phải tính cả chi phí lập chúng. Bộ nhớ mô hình đặc là $O(n^2m)$; chi phí hai bảng vẫn $O(n)$.

#### L04-F02 — Cập nhật tại chỗ và thứ tự trạng thái

- **Vai trò và mục tiêu:** Ví dụ dẫn nhập và trực giác; MT6
- **Luận điểm trung tâm:** Giá trị vừa tính có thể được dùng ngay, làm kết quả một lượt phụ thuộc thứ tự cập nhật.
- **Ý chính:** Đánh giá $\pi_0=(a,a)$ từ $V=(0,0)$. Thứ tự $s_0,s_1$: nhận $V(s_0)=1$, rồi $V(s_1)=2+0.9\cdot1=2.9$. Kết quả là $(1,2.9)$; đồng bộ cho $(1,2)$. Trên lưới, thứ tự $c_4,c_3,c_2,c_1$ đưa phần thưởng 10 về $c_1$ trong một lượt.
- **Ví dụ/hình dự kiến:** SVG dp04-update-order.svg: bảng mới ghi đè một ô, mũi tên từ giá trị mới sang phép tính kế; ghi rõ thứ tự bằng số.
- **Hình thức hóa:** Cùng cập nhật kỳ vọng nhưng dùng bảng hiện có; chưa đồng nhất tại chỗ với mọi thuật toán bất đồng bộ.
- **Kết nối vào:** Chi phí quét gợi nhu cầu dùng ngay giá trị mới và lựa chọn thứ tự cập nhật.
- **Kết nối ra:** Cơ chế dùng giá trị mới nhất được giữ; ví dụ lưới dùng $T_*$ dẫn tới lặp giá trị bất đồng bộ, khác ví dụ đánh giá hai trạng thái dùng $T_{\pi_0}$.
- **Nguồn:** NG1, tr. 15, 25–28; NG2, §4.1, §4.5, tr. in 75, 85 (PDF 97, 107).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Lưới ngược thứ tự cho $(4.58,6.2,8,10,0)$ từ bảng không; đây là tính chất ví dụ này, không phải bảo đảm một lượt cho mọi MDP. Thay đổi lớn nhất trong lượt tại chỗ không trực tiếp bằng phần dư của bảng cuối. Gọi rõ lặp giá trị tại chỗ trên lưới: từ bảng không, $c_4$ nhận $\max\{-1,10\}=10$, rồi $c_3$ nhận $\max\{-1,-1+0.9\cdot10\}=8$. Giữ ví dụ đánh giá theo $\pi_0$ để đối chiếu đồng bộ/tại chỗ; không đồng nhất hai toán tử.

#### L04-F03 — Lặp giá trị bất đồng bộ

- **Vai trò và mục tiêu:** Quy trình và điều kiện sử dụng; MT6
- **Luận điểm trung tâm:** Bất đồng bộ cho phép chọn trạng thái cập nhật linh hoạt nhưng phải tiếp tục cập nhật mọi trạng thái.
- **Ý chính:** Đầu vào mô hình, $\gamma$, bảng $V$, lịch trạng thái và ngân sách cập nhật. Mỗi bước chọn một trạng thái, thay riêng giá trị của nó bằng $(T_*V)(s)$ dùng bảng hiện có, giữ các ô khác. Theo định kỳ hoặc khi hết ngân sách, cố định bảng để tính phần dư toàn cục. Trả $V$, chính sách tham lam và phần dư.
- **Ví dụ/hình dự kiến:** Giả mã ngắn và sơ đồ một ô được chọn trong bảng; số thứ tự làm tín hiệu ngoài màu.
- **Hình thức hóa:** HT16: Với MDP hữu hạn chiết khấu và giá trị mới nhất, nếu mỗi trạng thái được cập nhật vô hạn lần thì lặp giá trị bất đồng bộ hội tụ đến $v_*$.
- **Kết nối vào:** Cơ chế dùng giá trị mới nhất được giữ; ví dụ lưới dùng $T_*$ dẫn tới lặp giá trị bất đồng bộ, khác ví dụ đánh giá hai trạng thái dùng $T_{\pi_0}$.
- **Kết nối ra:** Các lịch khác nhau được đặt trong quan hệ chung giữa đánh giá và cải thiện.
- **Nguồn:** NG1, tr. 15; NG2, §4.5, tr. in 85–86 (PDF 107–108).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Một lượt quét tại chỗ là trường hợp có lịch hệ thống; bất đồng bộ tổng quát không cần lượt quét. Lịch chỉ cập nhật $s_0$ trong ví dụ hai trạng thái bỏ mất giá trị 30 ở $s_1$; không thỏa điều kiện hội tụ. Bản trình bày không bao gồm giá trị truyền trễ. Áp dụng quy trình vào lưới sau lịch $c_4,c_3,c_2,c_1$: bảng cuối $(4.58,6.2,8,10,0)$ có phần dư toàn cục bằng 0 và chính sách trích chọn phải ở mọi ô chưa kết thúc. Phần dư được tính sau khi cố định toàn bảng. Từ bảng $(1,0)$ trong mô hình hai trạng thái, $T_*$ cập nhật tại $s_1$ thành $\max\{2.9,3\}=3$, còn $T_{\pi_0}$ cho $2.9$. Thành phần truyền từ F02 là cơ chế đọc bảng mới và ví dụ lưới tối ưu, không phải đầu ra đánh giá $(1,2.9)$.

#### L04-F04 — Lặp chính sách tổng quát

- **Vai trò và mục tiêu:** Khái niệm hỗ trợ và ứng dụng phân loại; MT6
- **Luận điểm trung tâm:** Các phương pháp quy hoạch động phối hợp đánh giá và cải thiện với mức hoàn tất khác nhau.
- **Ý chính:** Đánh giá đưa $V$ về $v_\pi$; cải thiện đưa $\pi$ về chính sách tham lam theo $V$. Lặp chính sách hoàn tất đánh giá trước cải thiện; lặp giá trị dùng một lượt; phương pháp bất đồng bộ có thể xen kẽ ở từng trạng thái. Hai quá trình ổn định chính xác tại cùng cặp thì cặp đó tối ưu.
- **Ví dụ/hình dự kiến:** SVG dp04-gpi.svg: hai quá trình, hai đối tượng $V,\pi$, điểm chung được gắn hai điều kiện. Bảng ba phương pháp nối với các ví dụ đã học.
- **Hình thức hóa:** HT17: lặp chính sách tổng quát (GPI); điểm chung thỏa $V=v_\pi$ và $\pi(s)\in\arg\max_aQ_V(s,a)$, suy ra $V=T_*V$.
- **Kết nối vào:** Các lịch khác nhau được đặt trong quan hệ chung giữa đánh giá và cải thiện.
- **Kết nối ra:** Các cách tổ chức cập nhật vẫn cần biểu diễn trạng thái hữu hạn và mô hình đã biết. CartPole có trạng thái liên tục, nên việc tạo biểu diễn hữu hạn còn phải xét ảnh hưởng của gộp trạng thái.
- **Nguồn:** NG1, tr. 13, 23, 29; NG2, §4.6, tr. in 86–87 (PDF 108–109).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** GPI là khuôn mô tả tương tác giữa hai quá trình, không là bảo đảm hội tụ cho mọi cách xen kẽ hay mọi xấp xỉ. Ứng dụng là nhận diện thành phần cố định và thành phần thay đổi của ba thuật toán đã có. Các cách tổ chức cập nhật vẫn cần biểu diễn trạng thái hữu hạn và mô hình đã biết. CartPole có trạng thái liên tục, nên việc tạo biểu diễn hữu hạn còn phải xét ảnh hưởng của gộp trạng thái.

#### L04-F05 — Rời rạc hóa và mô hình CartPole

- **Vai trò và mục tiêu:** Ứng dụng giới hạn; MT6
- **Luận điểm trung tâm:** Rời rạc hóa giảm biểu diễn liên tục về bảng hữu hạn nhưng chưa cung cấp mô hình Markov phù hợp.
- **Ý chính:** Trạng thái gồm vị trí, vận tốc xe, góc cột và vận tốc góc. Chia lần lượt thành $3,3,6,6$ khoảng cho $3\cdot3\cdot6\cdot6=324$ tổ hợp; hành động trái/phải. Cần xác định mô hình chuyển–thưởng và kiểm tra ảnh hưởng của gộp trạng thái.
- **Ví dụ/hình dự kiến:** SVG dp04-cartpole-bins.svg: xe–cột với bốn đại lượng; bốn dãy khoảng dẫn tới 324 tổ hợp, rồi khối yêu cầu mô hình.
- **Hình thức hóa:** $(x,\dot x,\theta,\dot\theta)\mapsto(b_x,b_{\dot x},b_\theta,b_{\dot\theta})$; đây là biểu diễn xấp xỉ.
- **Kết nối vào:** Các cách tổ chức cập nhật vẫn cần biểu diễn trạng thái hữu hạn và mô hình đã biết. CartPole có trạng thái liên tục, nên việc tạo biểu diễn hữu hạn còn phải xét ảnh hưởng của gộp trạng thái.
- **Kết nối ra:** Các điều kiện về lịch và mô hình được kiểm tra bằng hai trường hợp thiếu dữ kiện.
- **Nguồn:** NG1, tr. 35–37; NG2, Ch. 4 mở đầu, tr. in 73 (PDF 95).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Hai trạng thái liên tục trong cùng ô có thể có phân phối chuyển khác nhau. Việc gộp không tự bảo đảm Markov; cần mô hình xấp xỉ và đánh giá sai số. Tối ưu trong mô hình gộp không tự chứng nhận tối ưu của hệ liên tục.

#### L04-F06 — Kiểm tra lịch cập nhật và dữ kiện mô hình

- **Vai trò và mục tiêu:** Kiểm tra quy hoạch động thực hành; MT6
- **Luận điểm trung tâm:** Lịch cập nhật và mô hình hợp lệ là hai điều kiện độc lập của phép giải.
- **Ý chính:** Trong mô hình hai trạng thái, xét lịch chỉ cập nhật $s_0$ từ bảng không. Trong CartPole, xét bảng 324 tổ hợp nhưng chưa có phân phối chuyển–thưởng.
- **Ví dụ/hình dự kiến:** Hai tình huống ngắn, không cần hình mới.
- **Hình thức hóa:** Dùng HT16 và dữ kiện CartPole đã học.
- **Kết nối vào:** Các điều kiện về lịch và mô hình được kiểm tra bằng hai trường hợp thiếu dữ kiện.
- **Kết nối ra:** Những điều kiện sử dụng được thu hồi cùng nghiệm của bài toán hai trạng thái.
- **Nguồn:** NG1, tr. 15, 35–37; NG2, §4.5, tr. in 85 (PDF 107).
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Tăng số lần tính không khắc phục việc bỏ một trạng thái hoặc thiếu mô hình. Phải kiểm tra điều kiện của thuật toán trước khi diễn giải đầu ra.
- **Yêu cầu trên mặt trang:** Câu hỏi: Với lịch chỉ cập nhật $s_0$, điều kiện hội tụ nào bị vi phạm và giá trị nào không thể được khôi phục? Bảng 324 tổ hợp đã đủ để chạy quy hoạch động hay chưa; nêu dữ kiện còn thiếu.
- **Kiến thức được đo:** MT6; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** $s_1$ không được cập nhật, nên giữ 0 thay vì 30; điều kiện mọi trạng thái xuất hiện vô hạn lần bị vi phạm. CartPole còn thiếu mô hình $p(s',r\mid s,a)$ và đánh giá tính phù hợp Markov của biểu diễn gộp.
- **Tiêu chí đánh giá:** Nêu đúng điều kiện lịch, hậu quả số ở $s_1$ và phân biệt biểu diễn trạng thái với mô hình.
- **Thời gian hoạt động:** 1 phút lập phép tính, 1 phút trả lời, 1 phút đối chiếu; đã tính trong thời lượng của trang.

### Mạch G. Tổng hợp và bài tập

Chức năng: Kết luận và vận dụng tổng hợp. Đầu vào: Kết quả của sáu mạch trước. Đầu ra: Kiểm tra nghiệm, so sánh phương pháp theo giả thiết; bài tập và tài liệu đọc. Mục tiêu: MT1–MT6. Thời lượng: 12 phút; kiểm tra riêng L04-G04.

#### L04-G01 — Kết quả của bài toán lập kế hoạch

- **Vai trò và mục tiêu:** Tổng hợp theo vấn đề mở đầu; MT1–MT5
- **Luận điểm trung tâm:** Mô hình hai trạng thái có chính sách tối ưu $(b,b)$ với giá trị $(27,30)$.
- **Ý chính:** Đánh giá tạo giá trị của chính sách đang xét; cải thiện dùng giá trị đó để thay hành động; lặp chính sách hoặc lặp giá trị tìm nghiệm tối ưu. Trong ví dụ, cả hai phương pháp quy về $v_*=(27,30)$ và cùng lựa chọn $b$ tại hai trạng thái.
- **Ví dụ/hình dự kiến:** Sơ đồ dữ kiện nguồn → hai nhánh thuật toán → cùng cặp đầu ra; không lặp toàn bộ bảng số.
- **Hình thức hóa:** Thu hồi HT8 và HT12; không thêm khái niệm.
- **Kết nối vào:** Những điều kiện sử dụng được thu hồi cùng nghiệm của bài toán hai trạng thái.
- **Kết nối ra:** Hai thuật toán cho cùng nghiệm nhưng yêu cầu so sánh cấu trúc công việc và độ chính xác.
- **Nguồn:** NG1, tr. 18–24, 38; NG2, §4.8, tr. in 88–89 (PDF 110–111).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Điểm chung của hai thuật toán là sử dụng kỳ vọng theo mô hình và giá trị tiếp nối. Số lượt hữu hạn cần đi kèm phần dư hoặc điều kiện dừng chính xác để đánh giá độ tin cậy. Bootstrapping là dùng ước lượng tiếp nối để xây mục tiêu; yêu cầu mô hình đầy đủ để tính kỳ vọng là một đặc điểm riêng.

#### L04-G02 — Lựa chọn phương pháp và điều kiện áp dụng

- **Vai trò và mục tiêu:** Tổng hợp so sánh; MT4–MT6
- **Luận điểm trung tâm:** So sánh phương pháp phải dùng cùng đơn vị công việc và cùng yêu cầu độ chính xác.
- **Ý chính:** Lặp chính sách có bước đánh giá và bước cải thiện tách biệt; lặp giá trị dùng cập nhật tối ưu lặp; bất đồng bộ cho phép phân bổ cập nhật theo trạng thái. Cả ba trong bài đều cần mô hình hữu hạn chiết khấu đã biết. Tốc độ phụ thuộc mô hình, khởi tạo, lịch và ngưỡng.
- **Ví dụ/hình dự kiến:** Bảng ba hàng: đại lượng giữ cố định, thao tác, kiểm tra đầu ra; không khẳng định phương pháp nào luôn nhanh nhất.
- **Hình thức hóa:** Tóm tắt HT10, HT13–HT16 với giả thiết; chi phí chi tiết tham chiếu trong ghi chú.
- **Kết nối vào:** Hai thuật toán cho cùng nghiệm nhưng yêu cầu so sánh cấu trúc công việc và độ chính xác.
- **Kết nối ra:** So sánh kỳ vọng và mô hình được vận dụng khi chuyển tiếp của lưới trở thành ngẫu nhiên.
- **Nguồn:** NG1, tr. 29–34; NG2, §4.7–4.8, tr. in 87–89 (PDF 109–111).
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Một lần lặp chính sách ngoài không tương đương một lượt lặp giá trị. Khi $\gamma$ gần 1, chặn co yếu hơn; đây không phải dự đoán tuyệt đối về thời gian chạy trên mọi bài toán.

#### L04-G03 — Bài tập lưới có chuyển tiếp ngẫu nhiên

- **Vai trò và mục tiêu:** Bài tập tổng hợp được chuẩn bị; MT2, MT5
- **Luận điểm trung tâm:** Kỳ vọng trong cập nhật phải ghép xác suất với phần thưởng của chuyển thực tế.
- **Ý chính:** Giữ lưới năm ô và $\gamma=0.9$. Hành động thực hiện đúng hướng với xác suất 0.8, đứng yên 0.1, đi ngược 0.1. Chuyển ra ngoài ở $c_1$ ở lại; thưởng 10 chỉ khi chuyển thực tế $c_4\to c_5$, các chuyển chưa kết thúc khác thưởng -1; $V(c_5)=0$. Mỗi ô chưa kết thúc có hai hành động trái/phải; yêu cầu là lặp giá trị đồng bộ từ bảng không.
- **Ví dụ/hình dự kiến:** SVG dp04-stochastic-grid.svg: ba kết quả từ $c_4$, nhãn xác suất và thưởng; nhiệm vụ đầy đủ ở ghi chú hoặc học liệu.
- **Hình thức hóa:** $Q_V(c_4,\text{phải})=0.8\cdot10+0.1[-1+0.9V(c_4)]+0.1[-1+0.9V(c_3)]$.
- **Kết nối vào:** So sánh kỳ vọng và mô hình được vận dụng khi chuyển tiếp của lưới trở thành ngẫu nhiên.
- **Kết nối ra:** Bài tập dùng kỳ vọng dẫn tới kiểm tra tổng hợp cách chứng nhận nghiệm từ mô hình.
- **Nguồn:** NG3, hw04.pdf tr. 1; giả thiết biên và nhiệm vụ do bài giảng bổ sung, ghi rõ.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Với $V_0=0$, $V_1=(-1,-1,-1,7.8,0)$; từ đó $V_2(c_3)=4.436$. Tại $c_4$, chọn trái vẫn có xác suất 0.1 thực hiện chuyển thực tế sang phải và nhận thưởng 10. Vì vậy phần thưởng phụ thuộc kết quả chuyển, không chỉ tên hành động.
- **Yêu cầu trên mặt trang:** Câu hỏi: Lặp giá trị đồng bộ từ $V_0=0$, tính $V_1$ và $V_2(c_3)$. Ghi đủ các kết quả chuyển, xác suất và phần thưởng.
- **Kiến thức được đo:** MT2, MT5; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** $V_1=(-1,-1,-1,7.8,0)$; chọn phải tại $c_3$ cho $-1+0.9[0.8\cdot7.8+0.1(-1)+0.1(-1)]=4.436$, lớn hơn điểm chọn trái.
- **Tiêu chí đánh giá:** Mỗi tổng đủ ba kết quả, thưởng gắn với chuyển thực tế và giữ đích bằng 0.
- **Thời gian hoạt động:** 1 phút đọc quy ước, 1 phút lập kỳ vọng tại ô sát đích, 1 phút đối chiếu; lời giải toàn bài được chữa trong 30 phút riêng; đã tính trong thời lượng của trang.

#### L04-G04 — Kiểm tra nghiệm và chứng nhận tối ưu

- **Vai trò và mục tiêu:** Kiểm tra tổng hợp; MT3–MT6
- **Luận điểm trung tâm:** Một nghiệm điều khiển được kiểm tra bằng hành động tham lam và phần dư Bellman cùng giả thiết.
- **Ý chính:** Cho mô hình hai trạng thái của bài và bảng $V=(27,30)$. Cần kiểm tra đầu ra và xác định giới hạn khi chuyển sang môi trường chỉ có bộ mô phỏng.
- **Ví dụ/hình dự kiến:** Bảng hai giá trị và mô hình bốn chuyển tiếp; đáp án không lộ trên mặt trang.
- **Hình thức hóa:** Dùng HT11–HT14 và điều kiện đầu vào của HT12.
- **Kết nối vào:** Bài tập dùng kỳ vọng dẫn tới kiểm tra tổng hợp cách chứng nhận nghiệm từ mô hình.
- **Kết nối ra:** Năng lực kiểm chứng được củng cố bằng các mục đọc và bài tập gắn với chương 4.
- **Nguồn:** NG1, tr. 17–19, 31–38; câu kiểm tra tổng hợp từ nguồn.
- **Thời lượng:** 3 phút
- **Ghi chú học thuật dự kiến:** Phần dư bằng 0 chứng nhận điểm bất động trong mô hình đã cho. Chứng nhận đó phụ thuộc độ đúng của mô hình; không tự chuyển thành bảo đảm cho một mô hình xấp xỉ khác.
- **Yêu cầu trên mặt trang:** Câu hỏi: Tính bốn $Q_V$, suy ra chính sách tham lam và phần dư $\Delta_*(V)$. Nêu căn cứ kết luận tối ưu. Nếu chỉ có bộ mô phỏng sinh một chuyển tiếp mỗi lần gọi, bước nào của thuật toán chưa được cung cấp trực tiếp?
- **Kiến thức được đo:** MT3–MT6; các công thức và dữ kiện đã trình bày trước trang này.
- **Đáp án/gợi ý trong ghi chú:** $Q_V=(25.3,27;26.3,30)$; chính sách $(b,b)$; $T_*V=V$ nên $\Delta_*(V)=0$ và $V=v_*$. Căn cứ là MDP hữu hạn, thưởng bị chặn, $\gamma=0.9<1$ và tính duy nhất điểm bất động. Bộ mô phỏng chưa cung cấp trực tiếp kỳ vọng đầy đủ theo $p$; cần xây mô hình hoặc phương pháp lấy mẫu ngoài phạm vi.
- **Tiêu chí đánh giá:** Đúng bốn điểm, đúng phần dư của bảng đã cho, nêu giả thiết và phân biệt mẫu với mô hình đầy đủ.
- **Thời gian hoạt động:** 1 phút lập phép tính, 1 phút trả lời, 1 phút đối chiếu; đã tính trong thời lượng của trang.

#### L04-G05 — Tài liệu đọc và bài tập tiếp nối

- **Vai trò và mục tiêu:** Kết luận và đọc thêm; MT1–MT6
- **Luận điểm trung tâm:** Chương 4 củng cố quan hệ giữa đánh giá, cải thiện và các cách tổ chức cập nhật.
- **Ý chính:** Đọc Sutton–Barto §4.1–4.4 cho cơ chế thuật toán; §4.5–4.8 cho bất đồng bộ, GPI và giới hạn. Bài tập 4.3 về giá trị hành động và 4.4 về phá hòa; lưới 4×4 của Ví dụ 4.1 chỉ đọc thêm với điều kiện kết thúc riêng. Hoàn thiện bài lưới ngẫu nhiên đã giao.
- **Ví dụ/hình dự kiến:** Danh sách tài liệu ngắn có tác giả, năm, mục và trang; không hình trang trí.
- **Hình thức hóa:** Không thêm kiến thức trọng tâm; ký hiệu giữ nguyên như toàn bài.
- **Kết nối vào:** Năng lực kiểm chứng được củng cố bằng các mục đọc và bài tập gắn với chương 4.
- **Kết nối ra:** Bài học kết thúc bằng nhiệm vụ tính và đọc đã có tiên quyết; không mở thuật toán mới.
- **Nguồn:** NG2, §4.1–4.8, tr. in 74–89 (PDF 96–111), Ex. 4.3 tr. in 76, Ex. 4.4 tr. in 82; NG3 tr. 1.
- **Thời lượng:** 2 phút
- **Ghi chú học thuật dự kiến:** Bài tập 4.3 yêu cầu viết các phương trình đánh giá cho giá trị hành động từ các phương trình theo trạng thái. Bài tập 4.4 xét lỗi không dừng do lựa chọn tùy ý giữa các hành động hòa. Ví dụ lưới không chiết khấu cần bảo đảm kết thúc dưới chính sách đang xét; chặn chia cho $1-\gamma$ không áp dụng khi $\gamma=1$.

## Ánh xạ đủ 38 trang nguồn

Số trang in và số trang PDF của NG1 trùng nhau. “Bỏ” dưới đây chỉ áp dụng cho trang mục lục lặp; nội dung học thuật vẫn có đích hoặc ghi chú.

| Trang nguồn | Nội dung | Trang đích | Quyết định | Lý do |
|---:|---|---|---|---|
| 1 | Tên bài và siêu dữ liệu | L04-A01 | sửa | Đổi học kỳ theo yêu cầu, không dùng ngày nguồn làm ngày mới. |
| 2 | Mục tiêu | L04-A02; L04-G01–G04 | sửa | Chuyển thành năng lực tính, giải thích, kiểm chứng; không hứa mã nguồn không có. |
| 3 | Mục lục | L04-A02 | sửa | Theo thứ tự chương 4 được người dùng yêu cầu. |
| 4 | Mô hình MDP | L04-A03 | gộp | Gắn điều kiện mô hình với bài toán lập kế hoạch; thưởng kỳ vọng suy từ p chung. |
| 5 | Tổng thưởng, v, q | L04-A05; L04-B03; L04-C03 | tách | Sửa nhãn G; phân biệt các giá trị theo vai trò. |
| 6 | Bellman kỳ vọng và ma trận | L04-B03; L04-B07; L04-C03 | tách | Giữ v trước q; ma trận và Bellman q ở ghi chú để giảm tải. |
| 7 | Giá trị tối ưu và chính sách tham lam | L04-D04; L04-E03 | sửa | Đặt sau ví dụ cải thiện và ổn định; chuẩn hóa v*,q*. |
| 8 | Bellman tối ưu cho v và q | L04-D04; L04-E03 | tách | v trên mặt trang, q trong ghi chú có định nghĩa; không mở mạch bằng hệ công thức. |
| 9 | Tồn tại chính sách tối ưu | L04-D04 | gộp | Nêu hữu hạn/chiết khấu, chứng minh qua điểm bất động; không chỉ viện hữu hạn hành động. |
| 10 | Hai toán tử Bellman | L04-B04; L04-E03 | tách | Mỗi toán tử xuất hiện sau phép tính cụ thể của nó. |
| 11 | Mục lục lặp | Không có trang riêng | bỏ | Quan hệ giữa mô hình và đánh giá được ghi bằng câu nối. |
| 12 | Điều kiện DP, backup, bootstrap | L04-A03; L04-B01,B04; L04-F05; L04-G01 | tách | Giữ mô hình và giá trị tiếp nối; gọi tên bootstrapping ở B04, phân biệt với yêu cầu mô hình ở G01; giới hạn gamma=1 nêu riêng. |
| 13 | Chu trình đánh giá và cải thiện | L04-D01; L04-F04 | giữ | Vẽ lại sơ đồ, dùng chu trình sau khi hai thao tác đã được xây dựng. |
| 14 | Đánh giá lặp đồng bộ | L04-B02–B08 | tách | Bổ sung tính tay, quy trình và câu kiểm tra có đáp án. |
| 15 | Đồng bộ và tại chỗ dưới tên bất đồng bộ | L04-F02–F03 | sửa | Phân biệt quét tại chỗ với lịch không theo lượt quét, bổ sung điều kiện bao phủ. |
| 16 | Mục lục lặp | Không có trang riêng | bỏ | Trang tiếp trong nguồn thuộc ví dụ PI; mạch mới không dùng mục lục lặp. |
| 17 | MDP hai trạng thái | L04-A04; dùng lại ở B–E,G | giữ | Giữ bốn cạnh và gamma0.9; đưa lên để thống nhất ví dụ. |
| 18 | Đánh giá chính sách (a,a) | L04-B07; L04-D02 | giữ | Giữ nghiệm (10,11), nối với bảng ước lượng đã học. |
| 19 | Cải thiện, pi1 và pi2 | L04-C02–C07; L04-D02 | tách | Khôi phục giá trị (10,30) ở giữa, không gộp hai lần cải thiện. |
| 20 | Thuật toán lặp chính sách | L04-D03 | sửa | Đủ đầu vào/ra, đánh giá chính xác, phá hòa ổn định và ngân sách. |
| 21 | Định lý cải thiện | L04-C04–C05 | giữ | Giữ bất đẳng thức và phác thảo, bổ sung điểm dùng giả thiết. |
| 22 | Mục lục lặp | Không có trang riêng | bỏ | Nhu cầu cắt ngắn đánh giá dẫn trực tiếp tới lặp giá trị. |
| 23 | Ý tưởng lặp giá trị | L04-E01–E03 | tách | Trực giác và tính tay trước cập nhật tổng quát. |
| 24 | Thuật toán lặp giá trị | L04-E04; L04-E07 | sửa | Dùng đúng bảng cũ/mới, terminal, phần dư của bảng trả và chính sách theo bảng đó. |
| 25 | Thiết lập lưới năm ô | L04-E06 | gộp | Giữ mô hình, bổ sung minh bạch quy ước biên trái. |
| 26 | Lượt đầu trên lưới | L04-E06 | gộp | Giữ số; ví dụ tính tay trung tâm trước công thức dùng hai trạng thái thay vì lưới. |
| 27 | Bảng các lượt 0–4 | L04-E06; L04-E08 | giữ | Bảng HTML, kiểm thêm V5=V4 trong ghi chú. |
| 28 | Chính sách tối ưu lưới | L04-E06; L04-F02–F03 | giữ | Bốn mũi tên phải và giá trị; đối chiếu điểm trái trong ghi chú. |
| 29 | So sánh PI/VI | L04-F01; L04-G02 | sửa | Chi phí trên cùng đơn vị, không tuyên bố luôn nhanh hơn. |
| 30 | Nhu cầu hội tụ | L04-B06; L04-D05; L04-E05; L04-G02 | gộp | Đặt bảo đảm cạnh thuật toán, bỏ tiêu đề tu từ và lời ca ngợi. |
| 31 | Tính co tối ưu | L04-E05 | giữ | Nêu đủ giả thiết; bất đẳng thức của phép cực đại được dùng trước bước chặn tổng theo xác suất. |
| 32 | Sai số hình học | L04-E05; L04-E07 | gộp | Phân biệt chặn lý thuyết với phần dư quan sát được. |
| 33 | Hội tụ PI | L04-D05 | sửa | Đánh giá chính xác, giữ hành động hòa; số chính sách là tích cỡ tập hành động. |
| 34 | Sai số và dừng | L04-B05–B06; L04-D05–D06; L04-E04,E07 | tách | Phần dư, sai số và ổn định chính sách có điều kiện khác nhau. |
| 35 | CartPole liên tục | L04-F05 | gộp | Giữ bốn đại lượng và hai hành động. |
| 36 | Rời rạc hóa 324 ô | L04-F05 | sửa | 324 tổ hợp biểu diễn chưa bảo đảm Markov và chưa gồm terminal nếu cần riêng. |
| 37 | Giới hạn CartPole | L04-F05–F06; L04-G02 | gộp | Giữ chi phí, sai số gộp và mô hình; không tạo code. |
| 38 | Tổng kết và ôn tập | L04-G01–G05 | tách | Quay lại đầu ra, kiểm tra tổng hợp có lời giải và đọc thêm có nguồn. |


## Tự kiểm và giới hạn

- Các mạch lần lượt có 5, 8, 7, 6, 8, 6, 5 trang; thời lượng 10, 22, 20, 18, 22, 16, 12 phút, cộng đúng 120. Bảy trang kiểm tra riêng có dữ kiện, đáp án và tiêu chí; bài tập G03 có nhiệm vụ và giả thiết bổ sung.
- Định nghĩa phần dư/chuẩn ở đánh giá xuất hiện trước điều kiện dừng sử dụng chúng. Lặp giá trị định nghĩa $\Delta_*$ ở trang giả mã; chặn sai số có sau tính co. Thuật toán dùng ngưỡng phần dư $\eta$, chưa gọi nó là ngưỡng sai số khi chưa có HT14.
- Mỗi khái niệm trọng tâm có phép tính trước quy tắc tổng quát và ứng dụng sau quy trình. Ma trận/Bellman $q$/GPI là phần hỗ trợ được ghi rõ mức rút gọn; không dùng chúng để đưa tiên quyết chưa chuẩn bị.
- Biên tập theo no-ai-slop/Edit và tự đối chiếu eval.md: giữ thuật ngữ, giả thiết, điều kiện và chức năng kiểm tra; loại lời dẫn, lời điều phối, tiêu đề tu từ và nhận định thiếu căn cứ. Kết quả chi tiết trong review-log.md.
- Các ghi chú ở đây là nội dung học thuật dự kiến. Nhãn trường, mã, nguồn kỹ thuật và thời lượng của kế hoạch không đưa nguyên vào mặt trang hoặc ghi chú diễn giả. Bản kế hoạch đang chờ kiểm định độc lập và chấp nhận của điều phối viên trước khi viết HTML.
