# Phân tích học liệu và thiết kế Bài 04

Phân tích ban đầu ngày 23-09-2026; cập nhật để triển khai ngày 24-09-2026. Tiến độ HTML/SVG và kiểm định được ghi trong review-log. Dàn bài đích có 45 slide, 120 phút, bảy phần và bảy slide kiểm tra riêng. Các mục tiêu MT1–MT6 được phát biểu trong [outline.md](outline.md).

## 1. Bài toán giảng dạy

Bài 03 đã thiết lập MDP, phần thưởng tích lũy, chính sách và Bellman kỳ vọng. Bài 04 cần biến mô hình đã biết thành một phương pháp tính chính sách, đồng thời phân biệt ba sản phẩm: giá trị của chính sách cố định, bảng giá trị đang được lặp và giá trị tối ưu. Sinh viên phải tự tính được một lượt, giải thích một lần đổi hành động và kiểm tra điều kiện dừng.

Người học là sinh viên năm 3 có nền xác suất, đại số tuyến tính, thuật toán, học máy và học sâu. Phát biểu và áp dụng định lý điểm bất động trong không gian hữu hạn; không yêu cầu học trước giải tích hàm. Chứng minh tính co, cải thiện và chặn phần dư được trình bày bằng bất đẳng thức, kỳ vọng và tổng chiết khấu.

Giới hạn: MDP hữu hạn, các tập hành động hữu hạn khác rỗng, phần thưởng bị chặn, mô hình đã biết, $0\le\gamma<1$. Không giảng thuật toán phi mô hình, xấp xỉ hàm, trường hợp không chiết khấu tổng quát hay chứng minh hội tụ của phương pháp trong không gian liên tục. CartPole chỉ là trường hợp kiểm tra giới hạn biểu diễn.

Tuyến 120 phút gồm hoạt động tính tay và hỏi–chữa. Theo cấu trúc học phần, còn 30 phút chữa bài ngoài tuyến này; chưa xây thêm học liệu mã vì nguồn không có mã tương ứng.

## 2. Kiểm kê học liệu

| Mã | Tài liệu và thông tin xác minh | Phạm vi đã đọc | Vai trò |
|---|---|---|---|
| NG1 | [lecture04-solving-MDP.pdf](../../../RL-hk2-2025-2026/lecture04-solving-MDP.pdf), Tạ Việt Cường, 19-03-2026; 38 trang, số PDF trùng số in | Toàn bộ 1–38; xem hình trực tiếp tr.17,25,36 | Nguồn nội dung chính |
| NG2 | [hw3.pdf](../../../RL-hk2-2025-2026/resources/hw3.pdf), “Bài tập tuần 3 – Giải bài toán MDP”, Tạ Việt Cường, 08-05-2026 | Toàn bộ văn bản; chọn B1–B7, B9 ở tr.1–2 | Bài tập phù hợp; B8 mở rộng, phần lớn B10 vượt phạm vi |
| NG3 | [hw04.pdf](../../../RL-hk2-2025-2026/resources/hw04.pdf), “Bài tập tuần 4 – Đánh giá chính sách”, 26-03-2026 | Toàn bộ một trang | Đối chiếu ví dụ; có nội dung MC/TD và lưới có nhiễu, không đồng nhất với NG1 |
| NG4 | [Bài giảng hiện có](../../lecture-04-giai-mdp-bang-quy-hoach-dong.html) và [ghi chú học liệu](../../materials/lec-04/lecture-note.md) | Đọc cấu trúc, ký hiệu và các cụm ví dụ/bảo đảm; kiểm kế hoạch cũ | Đối chiếu triển khai, không thay quyền ưu tiên của NG1 |
| ĐC1 | David Silver, *Lecture 3: Planning by Dynamic Programming*, khóa UCL trên [trang giảng dạy](https://davidstarsilver.wordpress.com/teaching/); mục khóa học ghi 2015 | [PDF 42 trang](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-3-planning-by-dynamic-programming-.pdf): tr.2–12,16–18,20–29,34–42; xem trực tiếp tr.10,22 | Đối chiếu trình tự, hình lặp, mức chứng minh; năm trong URL là năm tải lên, không suy thành niên khóa |
| ĐC2 | Emma Brunskill, Stanford CS234, Winter 2022, *Lecture 2: Making Sequences of Good Decisions Given a Model of the World* | [PDF 66 trang](https://web.stanford.edu/class/archive/cs/cs234/cs234.1224/slides/lecture2_ns.pdf): tr.22–24,30–40,43,47–56,65–66; xem trực tiếp tr.39 | Đối chiếu cầu nối đánh giá–cải thiện, câu hỏi kiểm tra và hình thức hóa |

Đã đọc mẫu kỹ thuật, CSS dùng chung và chỉ mục để kế hoạch có thể triển khai trong RevealJS hiện có. Chưa có công việc dựng hình hoặc kiểm tra giao diện trong yêu cầu này.

URL cũ của ĐC1 tại `davidsilver.uk/wp-content/uploads/2020/03/DP.pdf` trả 404. Đã theo liên kết trên trang giảng viên tới PDF hiện dùng. Ảnh chụp PDF của công cụ web có lỗi ở một trang Stanford; đã tải đúng PDF công khai và xem trang được kết xuất cục bộ. Đây là tài liệu đối chiếu thực sự đã đọc, không chỉ kết quả tìm kiếm. Không dùng bản ghi bài học không chính thức thay cho slide của trường.

## 3. Đối chiếu hai bộ slide đại học

### UCL / David Silver

**Quan sát:** tr.2 chia đánh giá, lặp chính sách, lặp giá trị, mở rộng và ánh xạ co; tr.9–11 đặt bảng giá trị cạnh mũi tên chính sách; tr.22 cho thấy thông tin lan qua lưới; phần co đứng cuối. **Quyết định thiết kế:** giữ ví dụ số của NG1, dùng cách hiện bảng theo từng lượt và đặt chứng minh sau cơ chế. Không nhập nguyên lưới không chiết khấu của ĐC1 vào giả thiết $\gamma<1$ của bài. [PDF, tr.2,9–11,22,34–42](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-3-planning-by-dynamic-programming-.pdf).

### Stanford / Emma Brunskill

**Quan sát:** tr.36–39 tách tính giá trị hành động, tham lam một bước và giá trị của chính sách mới; tr.43 có kiểm tra lặp chính sách. Tr.53 viết điều kiện với hệ số 1, chưa đủ cho tính co nghiêm ngặt. **Quyết định thiết kế:** tách hai lần đánh giá trong ví dụ nguồn; đặt câu hỏi sau mỗi phần; dùng hệ số $\gamma<1$ và chặn rõ ràng. Không nhập phần chân trời hữu hạn thành một tuyến mới. [PDF, tr.36–43,53–56](https://web.stanford.edu/class/archive/cs/cs234/cs234.1224/slides/lecture2_ns.pdf).

Các quyết định trên là nhận định sư phạm cho bài hiện tại. Chỉ dùng hai bộ đối chiếu vì đã bao phủ đúng các cơ chế và mức chứng minh cần thiết; không thêm nguồn chỉ để đủ số.

## 4. Bản đồ khái niệm và tiên quyết

| Nhóm | Khái niệm | Kiến thức đầu vào | Năng lực và lỗi cần phân biệt | Đầu ra dùng tiếp |
|---|---|---|---|---|
| Tiên quyết | MDP, kỳ vọng, $G_t,v^\pi,q^\pi$ | Bài 03 | Nhận đúng trạng thái kế tiếp và chiết khấu; không đồng nhất thưởng với tổng thưởng | Phép nhìn trước |
| Trọng tâm 1 | Bellman tối ưu | Một bước kỳ vọng | Phân biệt $Q_v,q^\pi,q_*$; thứ tự tổng theo môi trường rồi max theo hành động | Hai toán tử và chính sách tham lam |
| Trọng tâm 2 | Đánh giá chính sách | Bellman kỳ vọng, giải hệ | Tính $v^\pi$ chính xác hoặc xấp xỉ khi giữ $\pi$ cố định | Bảng cho cải thiện |
| Trọng tâm 3 | Cải thiện và lặp chính sách | Giá trị chính sách, argmax | Tính bước đổi, đánh giá lại, giữ hòa; phân biệt đánh giá chính xác và bị cắt | Chính sách ổn định, nhu cầu giảm chi phí |
| Trọng tâm 4 | Lặp giá trị | $T_*$, cập nhật đồng bộ | Tính một lượt, trích chính sách theo cùng bảng; không gọi mọi bảng trung gian là $v^\pi$ | Dãy bảng và phần dư |
| Trọng tâm 5 | Hội tụ và kiểm soát sai số | Không gian bảng hữu hạn, kỳ vọng, bất đẳng thức | Giải thích co, điểm bất động, tồn tại tối ưu và chặn sai số từ phần dư | Căn cứ dừng và giới hạn |
| Hỗ trợ | Đồng bộ/tại chỗ, chi phí, rời rạc hóa | Các thuật toán đã có | Không suy tại chỗ luôn nhanh; không suy chia ô là đã có MDP chính xác | Chọn cách sử dụng |
| Đọc thêm | Chặn mất mát chính sách, chứng minh chi tiết Banach, MDP liên tục | Các kết quả chính | Giữ mức năm 3 của tuyến chính | Tự học, không kiểm tra bắt buộc |

Mạch phụ thuộc: MDP/Bellman kỳ vọng → nhìn trước → Bellman tối ưu và toán tử → đánh giá → cải thiện/lặp chính sách → lặp giá trị → tính co/điểm bất động/sai số → quyết định phương pháp. Chứng minh tính co được hoãn, nhưng điều kiện và kết luận cần dùng đã phát biểu rõ. Định lý cải thiện trước đó dùng khai triển và đuôi chiết khấu, không viện dẫn một chứng minh chưa có.

## 5. Lựa chọn mạch trình bày và ví dụ

### Bellman tối ưu

Nhu cầu là chọn hành động dựa trên cả phần tiếp diễn. Cây một bước tạo trực giác; bảng $v=(4,7)$ cho phép tính cụ thể; sau đó mới định nghĩa $v_*,q_*$ và viết Bellman. Ứng dụng là tính điểm hành động và lấy cực đại; câu kiểm tra yêu cầu phân biệt một cập nhật với nghiệm bất động. Giữ thứ tự chủ đề NG1 nhưng đưa mô hình tr.17 lên mở đầu để mọi ký hiệu có đối tượng.

Phương án khác là bắt đầu ngay bằng $v_*=\max_\pi v^\pi$ như nguồn. Không chọn vì sinh viên chưa có một quyết định cụ thể và dễ nhầm tối ưu phần tiếp diễn với tham lam theo bảng bất kỳ. Phương án học đánh giá trước toàn bộ Bellman tối ưu như ĐC1 hợp lý cho bài khác, nhưng đổi nhiều hơn mạch NG1; ở đây chỉ nhắc Bellman kỳ vọng và giới thiệu nhu cầu tối ưu trước.

### Đánh giá chính sách

Hai phương trình của $\pi_0=(a,a)$ cho chuẩn chính xác; các bảng từ 0 cho trực giác xấp xỉ; rồi trình bày quy trình đánh giá và lịch cập nhật. Mỗi ví dụ vẫn dùng bốn cạnh đã thấy từ mở đầu. Câu kiểm tra tính lượt thứ ba và giải thích vì sao không có max. Không dùng một MDP mới cho phần này.

### Cải thiện và lặp chính sách

Bắt đầu tại $s_1$: chọn $b$ một lần rồi theo $\pi_0$ có giá trị $13{,}5$, lớn hơn 7. Tính toàn bảng, thu $\pi_1$, đánh giá lại rồi mới thu $\pi_2$. Quy tắc, định lý và thuật toán đứng sau hai vòng tính tay. Câu kiểm tra dùng cùng dữ kiện và hỏi thêm vai trò giữ hòa. Việc tách bước đánh giá lại sửa khoảng nhảy trên NG1 tr.19.

### Lặp giá trị

Nhu cầu là tránh đánh giá đầy đủ một chính sách ở mỗi vòng. Lưới năm ô trực quan hơn hai trạng thái cho cơ chế lan truyền; hiện một lượt và bảng bốn lượt trước công thức. Quy trình trả cùng bảng đã đo phần dư, rồi thực hành trích chính sách. Câu kiểm tra tính ô xa đích và bác bỏ kết luận hội tụ chỉ từ một ô.

### Hội tụ và sai số

Hai bảng trong chính MDP hai trạng thái tạo ví dụ về khoảng cách co; tiếp theo là chuẩn, định lý co, điểm bất động và chính sách đạt cận. Chặn hình học làm lộ thiếu hụt thực hành: chưa biết $v_*$. Phần dư giải quyết thiếu hụt đó. CartPole kiểm tra lại miền áp dụng; câu hỏi tính chặn và xét giới hạn $\gamma=1$. Không mở phần bằng thuật ngữ Banach.

### So sánh ví dụ trực quan

| Phương án | Giá trị sư phạm | Quyết định |
|---|---|---|
| MDP hai trạng thái NG1 tr.17 | Chỉ bốn cạnh; giải hệ, tính bảng hành động và hai vòng cải thiện bằng tay | Ví dụ xuyên suốt phần 1–4 và kiểm chứng cuối |
| Lưới năm ô NG1 tr.25 | Nhìn thấy phần thưởng lan từ đích; giữ nguyên dữ kiện nguồn và kiểm từng ô | Ví dụ chính phần 5 |
| MDP ba trạng thái NG2 B9 | Có chuyển ngẫu nhiên, kiểm tổng kỳ vọng và max | Bài tập sau tuyến chính; đủ dữ kiện trong tài liệu nguồn |
| Lưới nhiễu NG3 B10 | Làm rõ kỳ vọng khi hành động không tất định | Đọc thêm có chỉ dẫn; không trộn bảng số với lưới NG1 |
| Lưới lớn/cho thuê xe từ nguồn đối chiếu | Minh họa phong phú nhưng tăng dữ kiện và tiên quyết | Không đưa vào tuyến 120 phút |
| CartPole NG1 tr.35–37 | Phân biệt biểu diễn hữu hạn, mô hình và tính Markov | Giữ ở cuối phần 6; không dùng như bằng chứng thực nghiệm |

## 6. Bộ số sư phạm và kết quả đã kiểm — cập nhật 24-09-2026

Người dùng yêu cầu lựa chọn số để tránh lẫn các đại lượng khi giảng. Giữ cấu trúc hai ví dụ của NG1 nhưng thay tham số; số dưới đây là ví dụ thích nghi, không phải số trích nguyên văn từ PDF.

Mô hình hai trạng thái dùng $\gamma=0{,}5$: tại $s_0$, $a$ cho thưởng 2 và về $s_0$, $b$ cho thưởng −1 và tới $s_1$; tại $s_1$, $a$ cho thưởng 5 và về $s_0$, $b$ cho thưởng 10 và ở $s_1$. Bốn phần thưởng khác nhau, cũng khác các giá trị chính sách ban đầu 4,7 và giá trị tối ưu 9,20. Phép tính mẫu $-1+0{,}5\cdot7=2{,}5$ có bốn số khác nhau ứng với thưởng, chiết khấu, phần tiếp diễn và kết quả.

| Chính sách | Giá trị | $q^\pi(s_0,a),q^\pi(s_0,b)$ | $q^\pi(s_1,a),q^\pi(s_1,b)$ | Cải thiện |
|---|---|---|---|---|
| $(a,a)$ | $(4,7)$ | $(4,2{,}5)$ | $(7,13{,}5)$ | $(a,b)$ |
| $(a,b)$ | $(4,20)$ | $(4,9)$ | $(7,20)$ | $(b,b)$ |
| $(b,b)$ | $(9,20)$ | $(6{,}5,9)$ | $(9{,}5,20)$ | Không đổi |

Bảng giá trị hành động phải dùng phần tiếp diễn của đúng chính sách: $q_*(s_0,a)=2+0{,}5\cdot9=6{,}5$, còn $q^{\pi_0}(s_0,a)=2+0{,}5\cdot4=4$. Chọn $a$ một lần rồi theo chính sách tối ưu khác với luôn chọn $a$.

Đánh giá đồng bộ $\pi_0$ từ 0: $(0,0)\to(2,5)\to(3,6)\to(3{,}5,6{,}5)$. Cập nhật tại chỗ theo thứ tự $s_0,s_1$ cho lượt đầu $(2,6)$. Ví dụ co dùng $u=(4,7),v=(8,9)$: khoảng cách 4, sau toán tử thành $T_*u=(4,13{,}5),T_*v=(6,14{,}5)$, khoảng cách 2.

Lưới giữ bước thường thưởng −1, thay thưởng vào đích bằng 24 và dùng $\gamma=0{,}5$. Ra trái tại $c_1$ thì đứng yên và nhận −1; $c_5$ kết thúc, giá trị0 và không nhận thưởng sau kết thúc.

| Lượt | $c_1$ | $c_2$ | $c_3$ | $c_4$ | $c_5$ |
|---|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | -1 | -1 | -1 | 24 | 0 |
| 2 | -1,5 | -1,5 | 11 | 24 | 0 |
| 3 | -1,75 | 4,5 | 11 | 24 | 0 |
| 4 | 1,25 | 4,5 | 11 | 24 | 0 |
| 5 (kiểm) | 1,25 | 4,5 | 11 | 24 | 0 |

Chặn hội tụ minh họa dùng sai số đầu64: $64(0{,}5)^6=1$, $64(0{,}5)^7=0{,}5$. Phần dư0,15 cho chặn sai số0,3; muốn sai số không quá0,2 thì dùng ngưỡng phần dư0,1. Mỗi số luôn gắn với tên đại lượng, không chỉ hiện số rời.

Không ép mọi ô số phải khác nhau: các ô giống nhau do cùng khoảng cách, cùng bước thưởng, điểm bất động hoặc đẳng thức $q^\pi(s,\pi(s))=v^\pi(s)$ có ý nghĩa toán học. Chỉ các trùng hợp không phục vụ cơ chế mới cần tránh. Nguồn gốc vẫn được đối chiếu: NG1 dùng thưởng1/0/2/3, hệ số 0,9 và lưới thưởng đích 10; bộ số mới là thay đổi được người dùng yêu cầu. Các bài tập chỉ dẫn trong hw3.pdf giữ nguyên tham số riêng của tài liệu đó.

## 7. Danh mục hình thức hóa ở mức năm 3

### Định nghĩa và ký hiệu

- **HT1:** $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$, $v^\pi$ và $q^\pi$ là giá trị thật dưới chính sách. Bước đầu trong $q^\pi(s,a)$ được ấn định; $v_*,q_*$ lấy supremum trước khi có định lý tồn tại. Phát biểu và áp dụng, không lặp lại toàn bộ định nghĩa MDP. NG1 tr.4–8.
- **HT2:** $Q_v(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$, $(T^\pi v)(s)=\sum_a\pi(a\mid s)Q_v(s,a)$, $(T_*v)(s)=\max_aQ_v(s,a)$; miền $\mathcal V=\mathbb R^{|\mathcal S|}$. Chính sách trong $T^\pi$ là Markov dừng. Dùng để tính, không gọi toán tử là một giá trị vô hướng. NG1 tr.10.
- **HT3:** chuẩn vô cùng $\|v\|_\infty=\max_s|v(s)|$ và phần dư $\rho(v)=\|T_*v-v\|_\infty$. Ví dụ hai bảng đứng trước tính chất tổng quát. NG1 tr.24,31,34; phần dư được đặt tên để làm rõ đại lượng nguồn đang tính.

### Các kết quả và mức chứng minh

| Mục | Phát biểu, giả thiết | Mức trình bày và nơi dùng |
|---|---|---|
| HT4: Bellman | $v^\pi=T^\pi v^\pi$; $v_*=T_*v_*$; $q_*(s,a)=\mathbb E[R_1+\gamma\max_{a'}q_*(S_1,a')]$ với hành động đầu cố định | Giải thích phân rã một bước; tính tồn tại/tính duy nhất chứng minh phần 6. NG1 tr.6,8–10 |
| HT5: đánh giá | $(I-\gamma P^\pi)v^\pi=r^\pi$; $I-\gamma P^\pi$ khả nghịch vì $\rho(\gamma P^\pi)\le\gamma<1$ | Giải hệ 2 ẩn; phần chứng minh nghịch đảo bằng chuỗi hình học ma trận giao NG2 B6. Không dùng nghịch đảo tường minh làm thuật toán số. NG1 tr.6,18 |
| HT6: cải thiện | Với $\pi'$ tham lam theo $v^\pi$, $v^{\pi'}\ge v^\pi$; nếu $\pi$ chưa tối ưu thì nghiêm ngặt ở ít nhất một trạng thái | Phác thảo bằng $v^\pi\le T^{\pi'}v^\pi$, tính đơn điệu và hạng đuôi chiết khấu tiến về 0. Không nói nghiêm ngặt ở mọi trạng thái. NG1 tr.21 |
| HT7: lặp chính sách | Đánh giá chính xác, giữ hành động cũ khi hòa, tập chính sách xác định hữu hạn → dừng hữu hạn tại chính sách tối ưu | Lập luận không lặp lại và ổn định thỏa Bellman tối ưu. Số chính sách là $\prod_s|\mathcal A(s)|$; nếu cùng tập hành động là $|\mathcal A|^{|\mathcal S|}$. NG1 tr.20,33 |
| HT8: tính co | $\|T_*u-T_*v\|_\infty\le\gamma\|u-v\|_\infty$; tương tự $T^\pi$ với $\pi$ cố định | Chứng minh bước cực đại và kỳ vọng đủ trên lớp; điều kiện quyết định là $\gamma<1$. NG1 tr.31 |
| HT9: tồn tại tối ưu | Co trên $\mathbb R^n$ cho điểm bất động duy nhất $\bar v$; mọi chính sách bị chặn trên bởi $\bar v$; một chính sách dừng xác định tham lam đạt nó | Phát biểu Banach, trình bày sơ đồ chặn trên/đạt cận; nhánh đạt cận dùng $T^{\bar\pi}\bar v=\bar v$. Quy nạp theo toàn lịch sử để chứng minh nhánh chặn trên nằm trong ghi chú đọc thêm, không trình bày trọn trong 4 phút. Kết luận $\bar v=v_*$. NG1 tr.9,31–32 |
| HT10: hội tụ | $\|v_k-v_*\|_\infty\le\gamma^k\|v_0-v_*\|_\infty$ | Suy từ co bằng lặp bất đẳng thức; ví dụ 7 lượt là phép tính theo chặn. NG1 tr.32 |
| HT11: sai số thực hành | $\|v-v_*\|_\infty\le\rho(v)/(1-\gamma)$ | Chứng minh $e\le\rho+\gamma e$; áp dụng chọn ngưỡng. Nếu trả $Tv$ sau khi đo $\delta=\|Tv-v\|$, chặn là $\gamma\delta/(1-\gamma)$ cho bảng mới. Suy ra từ NG1 tr.31–34 |

Với đánh giá chính sách, thay $T_*,v_*$ bằng $T^\pi,v^\pi$ trong chặn phần dư. Cả hai trường hợp cần tính phần dư trên toàn bảng, không thay bằng chênh lệch cục bộ tùy ý của một lượt tại chỗ.

**Đọc thêm, không thuộc kiểm tra tuyến chính:** nếu $\pi_v$ tham lam theo $v$, tính chính xác trên cùng mô hình, thì

$$\|v_*-v^{\pi_v}\|_\infty\le\frac{2\gamma}{1-\gamma}\|v-v_*\|_\infty\le\frac{2\gamma}{(1-\gamma)^2}\rho(v).$$

Gợi ý suy diễn: dùng $T^{\pi_v}v=T_*v$, thêm và bớt hai hạng tại $v$, rồi áp dụng tính co để có $d\le2\gamma e+\gamma d$. Chặn này có trong kế hoạch cũ; chuyển ra khỏi tuyến chính để dành thời gian cho bảy câu kiểm tra và hai thuật toán. Phần dư dương không chứng nhận tối ưu tuyệt đối của chính sách; trường hợp $\gamma=0$ được xử lý trực tiếp, không chia cho $\gamma$.

## 8. Đặc tả hình, bảng và nội dung phải chuyển khi triển khai

| Tài sản nguồn | Điều phải giữ | Đặc tả đích |
|---|---|---|
| NG1 tr.13, chu trình đánh giá–cải thiện | Chiều hai mũi tên, giá trị/chính sách ở mỗi bước | Sơ đồ SVG hai khối; thêm nhánh dừng ổn định ở thuật toán |
| NG1 tr.17, MDP hai trạng thái | Hai vòng tự khép, hai cạnh chéo, nhãn $a/1,b/0,a/2,b/3$, $\gamma=0{,}9$ | Một SVG dùng lại, cấu trúc nguồn giữ nguyên; thay thưởng thành 2/−1/5/10 và hệ số 0,5 theo yêu cầu người dùng; dùng nhãn cùng độ dày cạnh |
| NG1 tr.17–19, bảng và phép tính | Đúng bốn chuyển và ba chính sách | Bảng HTML/công thức, không chuyển thành ảnh; tách rõ đánh giá lại $\pi_1$ |
| NG1 tr.25–28, lưới và bảng lặp | Năm ô, đích $c_5$, thưởng, dữ kiện từng lượt | SVG lưới và bảng HTML riêng; hiện từng lượt, không chụp raster nguồn |
| NG1 tr.29, so sánh | Khác nhau giữa đánh giá đầy đủ và một phép Bellman tối ưu | Bảng ba tiêu chí có thao tác/chi phí cụ thể |
| NG1 tr.36, sơ đồ rời rạc hóa | Bốn biến, số khoảng và tổng 324 | SVG thêm bước xác định mô hình; không hàm ý chia ô tự bảo đảm Markov |
| Chặn hình học, tính lại từ NG1 tr.32 | Thay minh họa thành $64\cdot(0{,}5)^k$, ngưỡng1, mốc6 và7 | Đồ thị SVG có tên trục; ghi “chặn lý thuyết” |
| NG1 tr.6–10,14,20–24,31–34 | Công thức, giả mã, giả thiết | KaTeX/HTML và khối giả mã; mỗi trang một bước, không dùng ảnh công thức |

Trong lần lập dàn bài này chỉ tạo đặc tả. Mẫu slide/CSS vẫn là nền giao diện cho lần triển khai sau; không sao chép CSS hoặc tài sản của hai trường.

## 9. Ánh xạ đủ 38 trang nguồn

| Trang NG1 | Nội dung | Slide đề xuất | Quyết định và lý do |
|---:|---|---|---|
| 1 | Tiêu đề | 01 | Giữ chủ đề, sửa học kỳ theo dự án |
| 2 | Mục tiêu | 02 và phần đầu outline | Sửa thành năng lực kiểm tra được; không chen trước slide nội dung |
| 3 | Nội dung | 02 | Sửa thành bảy phần theo nhu cầu học tập |
| 4 | MDP | 03, quy ước | Gộp ôn tập vào mô hình dùng xuyên suốt |
| 5 | Tổng thưởng và giá trị | 04–08 | Sửa “hàm phần thưởng” thành phần thưởng tích lũy; nhắc theo nhu cầu |
| 6 | Bellman kỳ vọng | 05–07,11,13–16 | Tách tính tay, quan hệ và hệ tuyến tính |
| 7 | Tối ưu | 08,10 | Giữ; dùng supremum và làm rõ hành động đầu |
| 8 | Bellman tối ưu | 09–10 | Tách giá trị trạng thái và hành động |
| 9 | Tồn tại tối ưu | 10,37 | Nêu điều kiện sớm, chuyển chứng minh sau tính co |
| 10 | Toán tử | 11,30,35–39 | Giữ, bổ sung miền và chuẩn tại nơi cần |
| 11 | Mục lục lặp | 02 | Gộp để tránh phần trang trí |
| 12 | Quy hoạch động, giả thiết | 03,27,40,42 | Giữ đầu vào mô hình; giới hạn tuyến chính ở chiết khấu |
| 13 | Đánh giá–cải thiện | 19–25 | Dùng sau khi đã có bảng giá trị, thay sơ đồ đứng riêng |
| 14 | Đánh giá lặp | 13,15–16,18 | Ví dụ trước quy trình; thêm dừng rõ bảng trả |
| 15 | Đồng bộ/bất đồng bộ | 17 | Sửa: tại chỗ là một lịch bất đồng bộ; thêm điều kiện cập nhật công bằng |
| 16 | Mục lục lặp | 02 | Gộp |
| 17 | Mô hình hai trạng thái | 03–07,13–26,35,43 | Giữ dữ kiện; đưa lên sớm, tái sử dụng |
| 18 | Đánh giá $\pi_0$ | 14–15 | Giữ, tính lại |
| 19 | Cải thiện và nghiệm | 19–21,26,43 | Tách bước đánh giá $\pi_1$ và chứng nhận cuối |
| 20 | Lặp chính sách | 22,24–26 | Giữ; đặc tả đánh giá chính xác, giữ hòa, ngân sách |
| 21 | Cải thiện chính sách | 23 | Giữ, mở bước đơn điệu/đuôi chiết khấu |
| 22 | Mục lục lặp | 02 | Gộp |
| 23 | Ý tưởng lặp giá trị | 27–30 | Chuyển lưới lên trước công thức |
| 24 | Thuật toán và dừng | 30–32,39,45 | Tách; phần dư, chính sách và bảng trả phải nhất quán |
| 25 | Mô hình lưới | 27 | Giữ; bổ sung biên và hấp thụ |
| 26 | Lượt đầu | 28 | Giữ, tính lại |
| 27 | Các lượt tiếp | 29,34 | Giữ, tính lại; dùng làm câu kiểm tra |
| 28 | Chính sách lưới | 29,32 | Giữ; không nhầm bảng trung gian và giá trị chính sách |
| 29 | So sánh PI/VI | 33,42 | Thay nhận xét định tính bằng thao tác và chi phí |
| 30 | Nhu cầu hội tụ | 35 | Gắn nhu cầu với khoảng cách giữa hai bảng |
| 31 | Tính co | 35–37 | Trực giác và ví dụ trước định lý; mở chứng minh |
| 32 | Hội tụ | 37–38 | Tách tồn tại/đạt cận và tốc độ hội tụ |
| 33 | Dừng PI | 25 | Chuyển về ngay sau quy trình PI; thêm giữ hòa |
| 34 | Sai số và dừng | 31,38–39,41,45 | Sửa chặn theo đúng bảng, thêm ứng dụng ngưỡng |
| 35 | CartPole liên tục | 40 | Gộp với 36–37 để kiểm tra giả thiết |
| 36 | Rời rạc hóa | 40 | Giữ 324 ô; sửa hàm ý tự tạo MDP chính xác |
| 37 | Hạn chế | 40,42 | Giữ; phân biệt sai số mô hình và sai số tính toán |
| 38 | Tổng kết | 42–45 | Trở lại vấn đề mở đầu, chỉ dẫn bài tập và kiểm tra tổng hợp |

## 10. Các sửa đổi quan trọng so với kế hoạch cũ

- Kế hoạch cũ có chỗ gán $(10,11)$ cho giá trị tiếp diễn tối ưu; theo mô hình đầy đủ tr.17–19 đây là $v^{\pi_0}$, còn $v_*=(27,30)$. Đây là lỗi của bản cũ theo tham số gốc. Bản triển khai mới dùng bộ số thích nghi ở mục6 và giữ phân biệt giữa giá trị chính sách với giá trị tối ưu; ghi chú học liệu cũ chưa được đồng bộ trong yêu cầu này.
- Tách đánh giá chính sách thành phần riêng, thay 38 slide chính bằng 45 slide với đủ bảy kiểm tra; không thêm một ví dụ lớn ngoài nguồn.
- Đưa chuẩn vô cùng tới nơi cần dùng thay vì mở bài bằng không gian hàm; tại thuật toán dừng giải thích ngắn nó là chênh lệch lớn nhất.
- Khôi phục $q_*$ và Bellman cho $q_*$ từ NG1 tr.7–8. Đây đã là nội dung nguồn, không ghi nhầm là nội dung mới do bản chuyển đổi bổ sung.
- Chứng minh tồn tại ở sau co để tránh lập luận vòng; bảo đảm PI nằm ngay sau thuật toán, với lời dẫn rõ tới nền tảng chung ở phần 6.
- Chặn mất mát chính sách là đọc thêm; phần chính vẫn chứng minh chặn sai số giá trị để ngưỡng dừng có ý nghĩa. Lược phần này có lý do về tải học và phạm vi NG1.
- NG3 có hai mục cùng nhãn “Bài 1” và ví dụ lưới nhiễu; tham chiếu theo nội dung, không tự sửa số bài rồi coi đó là bản gốc.
