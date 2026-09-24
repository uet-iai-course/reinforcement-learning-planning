# Dàn bài Bài 04: Giải MDP bằng quy hoạch động

**Trạng thái:** đã triển khai đủ 45 slide trong HTML và ghi chú diễn giả, với bộ số điều chỉnh theo yêu cầu người dùng. Thời lượng 120 phút là kế hoạch giảng; chưa có số đo từ buổi chạy thử với sinh viên. Kết quả rà và giới hạn công cụ ghi trong review-log.

**Quy mô:** 45 slide, 120 phút, trung bình 2 phút 40 giây/slide. Thời gian đã gồm giải thích, tính tay và bảy lượt hỏi–chữa. Theo quy ước học phần, 30 phút chữa bài còn lại nằm ngoài tuyến này; không chuẩn bị chương trình hoặc notebook.

**Người học:** sinh viên năm 3 đã học xác suất, đại số tuyến tính, thuật toán, học máy và học sâu; đã học Bài 03 về quy trình quyết định Markov (MDP), phần thưởng tích lũy, $v^\pi,q^\pi$ và Bellman kỳ vọng. Chỉ nhắc kiến thức cần dùng, không giảng lại Bài 03.

**Vấn đề trung tâm:** từ mô hình chuyển và phần thưởng đã biết, tính một chính sách tốt từ mọi trạng thái và xác định điều kiện cho phép dừng tính toán.

Nguồn, kiểm kê 38 trang, lựa chọn ví dụ và hình thức hóa: [analysis.md](analysis.md). Bản đồ chu trình và quyết định từng slide: [storyboard.md](storyboard.md). Lịch sử và kết quả rà: [review-log.md](review-log.md).

## Mục tiêu học tập

- **MT1:** Phân biệt Bellman kỳ vọng, Bellman tối ưu, giá trị của chính sách và giá trị tối ưu; tính một bước nhìn trước từ mô hình.
- **MT2:** Giải hệ Bellman nhỏ và thực hiện một lượt đánh giá chính sách đồng bộ; phân biệt với cập nhật tại chỗ.
- **MT3:** Thực hiện đánh giá–cải thiện và mô tả lặp chính sách chính xác, xử lý hòa, điều kiện dừng hữu hạn.
- **MT4:** Thực hiện lặp giá trị và trích chính sách từ cùng bảng giá trị; so sánh chi phí với lặp chính sách.
- **MT5:** Giải thích tính co, sự tồn tại của chính sách tối ưu và hội tụ; chuyển phần dư Bellman thành chặn sai số giá trị.
- **MT6:** Nhận diện giới hạn của quy hoạch động dạng bảng và của rời rạc hóa; chọn quy trình theo đầu vào và đầu ra cần đạt.

## Bản đồ các phần

| Phần | Slide | Phút | Đầu vào → đầu ra | Slide kiểm tra |
|---|---|---:|---|---|
| 1. Mở đầu và động lực | 01–05 | 10 | MDP đã học → nhu cầu tối ưu phần thưởng dài hạn | L04-S05 |
| 2. Bellman tối ưu | 06–12 | 18 | Một bước nhìn trước → $Q_v,T^\pi,T_*,v_*,q_*$ | L04-S12 |
| 3. Đánh giá chính sách | 13–18 | 17 | $T^\pi$, chính sách cố định → tính $v^\pi$ | L04-S18 |
| 4. Lặp chính sách | 19–26 | 23 | $v^\pi$ → cải thiện, lặp và kiểm tra ổn định | L04-S26 |
| 5. Lặp giá trị | 27–34 | 23 | Chi phí đánh giá đầy đủ → cập nhật trực tiếp $T_*v$ | L04-S34 |
| 6. Hội tụ và sai số | 35–41 | 20 | Các dãy cập nhật → bảo đảm, ngưỡng dừng và giới hạn | L04-S41 |
| 7. Tổng hợp và kết luận | 42–45 | 9 | Toàn bộ kết quả → quyết định phương pháp và kiểm tra kết quả | L04-S45 |
| **Tổng** | **45** | **120** | | **7 slide kiểm tra** |

Ứng dụng tính tay đặt ngay trong phần 3–5; không tách thêm phần thực hành vì sẽ chia nhỏ ba chu trình đang dùng chung ví dụ. Bài tập dài có căn cứ từ `hw3.pdf` được chỉ dẫn ở slide 44.

## Quy ước khi soạn

MDP hữu hạn, $\mathcal A(s)$ hữu hạn và khác rỗng; biết $p(s',r\mid s,a)$; $|R_t|\le R_{\max}<\infty$; $0\le\gamma<1$. Phần thưởng $R_{t+1}$ nhận sau $A_t$, trước $S_{t+1}$. Chính sách dùng trong $T^\pi$ là Markov dừng. Giá trị ở trạng thái kết thúc bằng 0, không cộng lại phần thưởng khi đã kết thúc.

$Q_v(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$ là phép nhìn trước từ bảng bất kỳ $v$; chỉ khi $v=v^\pi$ mới có $Q_v=q^\pi$, khi $v=v_*$ mới có $Q_v=q_*$. Dùng chữ thường $q^\pi,q_*$ cho hàm giá trị thực, chữ hoa $Q_v$ cho phép tính từ bảng. Các tổng theo $r$ giả định hỗ trợ phần thưởng rời rạc; dạng kỳ vọng tương ứng dùng được khi thưởng liên tục bị chặn.

Mã nguồn: **NG1** = `RL-hk2-2025-2026/lecture04-solving-MDP.pdf`, số trang PDF trùng số in 1–38; **NG2** = `resources/hw3.pdf`; **NG3** = `resources/hw04.pdf`. Đường dẫn đầy đủ và hai bộ slide đối chiếu ở analysis. Mọi hình dưới đây mới là đặc tả để dựng; công thức và bảng phải giữ dạng văn bản. Mã, thời lượng và phân vai chỉ nằm trong kế hoạch, không đưa lên mặt slide hoặc lời nói.

## Phần 1. Mở đầu và động lực

Thiết lập bài toán trước ký hiệu mới. Nhận kiến thức từ Bài 03; đầu ra là nhu cầu tính giá trị dài hạn và chọn chính sách. **10 phút.**


**Bộ số sư phạm cập nhật ngày 24-09-2026:** theo yêu cầu người dùng, giữ cấu trúc nguồn nhưng thay tham số để phần thưởng, giá trị tiếp diễn và kết quả dễ phân biệt. Mô hình hai trạng thái dùng thưởng 2/−1/5/10 và $\gamma=0{,}5$; lưới dùng thưởng thường −1, thưởng vào đích 24 và cùng hệ số 0,5. Mọi phép tính minh họa dưới đây thuộc bộ số mới, không được trích như số gốc của PDF. Các số trùng do đồng nhất thức hoặc trạng thái không đổi vẫn được giữ và giải thích.

#### L04-S01 — Giải MDP bằng quy hoạch động

- **Vai trò và mục tiêu:** Giới thiệu bài; MT1–MT6.
- **Luận điểm và nội dung:** Học tăng cường, Bài 04, học kỳ 1 năm học 2026–2027. Đầu vào là mô hình; đầu ra là chính sách cùng căn cứ đánh giá chất lượng.
- **Hình/ví dụ:** Sơ đồ ngắn: mô hình → phép tính Bellman → chính sách; chưa đưa thuật toán.
- **Nguồn:** NG1 tr.1–2.
- **Kết nối:** Trang nội dung chỉ ra các năng lực sẽ xây dựng.
- **Ghi chú triển khai:** Nêu nối tiếp Bài 03: đã mô tả giá trị, nay cần tính và tối ưu. Tên tác giả nguồn Tạ Việt Cường chỉ ghi trong nguồn; không tự suy ra người đang giảng.
- **Thời lượng:** 1 phút.

#### L04-S02 — Nội dung bài giảng

- **Vai trò và mục tiêu:** Định hướng học tập; MT1–MT6.
- **Luận điểm và nội dung:** Lộ trình: Bellman tối ưu → đánh giá chính sách → lặp chính sách → lặp giá trị → hội tụ và sai số → tổng hợp. Sản phẩm cần đạt: tính một lượt, giải thích một lần đổi hành động và kiểm tra một ngưỡng dừng.
- **Hình/ví dụ:** Một hàng các phần, đánh dấu đầu ra mỗi phần bằng động từ: tính, đổi, lặp, kiểm tra.
- **Nguồn:** NG1 tr.2–3.
- **Kết nối:** Dùng bài toán hai trạng thái để làm rõ nhu cầu của lộ trình.
- **Ghi chú triển khai:** Nhắc tiên quyết Bellman kỳ vọng và tổng chiết khấu. Chưa giải thích các công thức mới. Slide này đứng ngay sau giới thiệu, trước động lực.
- **Thời lượng:** 2 phút.

#### L04-S03 — Lập kế hoạch từ mô hình đã biết

- **Vai trò và mục tiêu:** Động lực qua ví dụ nguồn; MT1, MT6.
- **Luận điểm và nội dung:** MDP có hai trạng thái, mọi chuyển tất định: $(s_0,a)\to(2,s_0)$; $(s_0,b)\to(-1,s_1)$; $(s_1,a)\to(5,s_0)$; $(s_1,b)\to(10,s_1)$; $\gamma=0{,}5$. Cần chọn hành động ở cả hai trạng thái.
- **Hình/ví dụ:** Vẽ lại cấu trúc sơ đồ NG1 tr.17, thay tham số theo yêu cầu ngày 24-09-2026; mỗi cạnh ghi hành động/phần thưởng, nút chỉ ghi tên trạng thái.
- **Nguồn:** NG1 tr.4,12,17; chuyển ví dụ lên để tạo động lực.
- **Kết nối:** So sánh thưởng trước mắt với chuỗi thưởng dài hạn.
- **Ghi chú triển khai:** Nêu rõ mô hình cho phép tính kỳ vọng, chưa cần lấy mẫu trải nghiệm. Bốn cạnh này sẽ được dùng lại ở các phần 2–4; không thêm bối cảnh mới.
- **Thời lượng:** 2 phút.

#### L04-S04 — Phần thưởng trước mắt và dài hạn

- **Vai trò và mục tiêu:** Động lực bằng hai quỹ đạo; MT1.
- **Luận điểm và nội dung:** Từ $s_0$, luôn chọn $a$ nhận $2,2,\ldots$, tổng chiết khấu bằng 4. Chọn $b$ rồi luôn $b$ ở $s_1$ nhận $-1,10,10,\ldots$, tổng bằng 9. Chấp nhận phần thưởng đầu thấp hơn có thể đem lại tổng dài hạn cao hơn.
- **Hình/ví dụ:** Hai hàng cùng mốc $R_1,R_2,R_3$: hàng trên $2,2,2$, hàng dưới $-1,10,10$. Công thức $2/(1-0{,}5)=4$ và $-1+0{,}5\cdot10/(1-0{,}5)=9$ đặt dưới từng hàng.
- **Nguồn:** NG1 tr.5,17–19; tính lại từ nguồn.
- **Kết nối:** Khôi phục phép nhìn trước một bước trước khi tối ưu phần tiếp diễn.
- **Ghi chú triển khai:** Ví dụ giữ cấu trúc nguồn với bộ số đã đổi; mới so hai chính sách cụ thể, chưa thay cho chứng minh tối ưu. Thưởng đầu, giá trị phần tiếp diễn và tổng phải có nhãn riêng.
- **Thời lượng:** 3 phút.

#### L04-S05 — Câu hỏi: giá trị của một bước nhìn trước

- **Vai trò và mục tiêu:** Kiểm tra tiên quyết; MT1.
- **Luận điểm và nội dung:** Cho bảng tiếp diễn $v(s_0)=4,v(s_1)=7$ và $\gamma=0{,}5$; hành động $b$ ở $s_0$ nhận thưởng $-1$ và tới $s_1$ với xác suất 1.
- **Hình/ví dụ:** Cạnh $(s_0,b)\to(-1,s_1)$; ô tiếp diễn ở $s_1$ ghi 7, riêng phép tính kết quả nằm bên dưới.
- **Nguồn:** NG1 tr.6,17–19.
- **Kết nối:** Từ phép tính này, phần 2 đặt mục tiêu tối ưu cả hành động đầu và phần tiếp diễn.
- **Ghi chú triển khai:** Dành khoảng một phút tính và một phút chữa. Phân biệt thưởng −1, giá trị tiếp diễn 7, hệ số 0,5 và kết quả 2,5.
- **Thời lượng:** 2 phút.
- **Câu hỏi:** Tính giá trị của việc chọn $b$ tại $s_0$ rồi dùng bảng tiếp diễn đã cho; chỉ ra hai dữ kiện lấy từ mô hình.
- **Đáp án/gợi ý:** $-1+0{,}5\cdot7=2{,}5$; hai dữ kiện mô hình là thưởng $-1$ và chuyển đến $s_1$ với xác suất 1.
- **Tiêu chí:** Dùng đúng trạng thái kế tiếp và chiết khấu; không coi 7 hoặc 2,5 là phần thưởng trên cạnh.

## Phần 2. Bellman tối ưu

Nhận nhu cầu lựa chọn dài hạn; phân biệt phép nhìn trước từ bảng hiện tại với giá trị tối ưu thật. Đầu ra là các phép toán dùng trong phần 3–5. **18 phút.**

#### L04-S06 — Hành động đầu và phần tiếp diễn

- **Vai trò và mục tiêu:** Trực giác cho tối ưu; MT1.
- **Luận điểm và nội dung:** Mỗi lựa chọn gồm hành động đầu, chuyển trạng thái, rồi một chính sách tiếp diễn. Đánh giá giữ chính sách tiếp diễn cố định; tối ưu cho phép chọn phần tiếp diễn tốt nhất từ trạng thái đến.
- **Hình/ví dụ:** Sơ đồ cây một bước từ $s_0$, hai nhánh $a,b$ và hai khối phần tiếp diễn; tách nút hành động với nút ngẫu nhiên.
- **Nguồn:** NG1 tr.6–8,17.
- **Kết nối:** Đặt tên phép tính cho một bảng tiếp diễn bất kỳ.
- **Ghi chú triển khai:** Ở ví dụ tất định, nút ngẫu nhiên chỉ có một nhánh. Nêu rằng với chuyển ngẫu nhiên phải lấy kỳ vọng trước khi so hành động; không cho tác tử chọn kết quả ngẫu nhiên.
- **Thời lượng:** 2 phút.

#### L04-S07 — Điểm của hành động từ bảng giá trị

- **Vai trò và mục tiêu:** Ví dụ dẫn tới ký hiệu; MT1.
- **Luận điểm và nội dung:** Với $v=(4,7)$, bảng điểm theo hàng $s_0,s_1$ và cột $a,b$ là $(4,2{,}5;7,13{,}5)$. Đặt $Q_v(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v(s')]$.
- **Hình/ví dụ:** Cạnh mô hình → thưởng + giá trị tiếp diễn đã chiết khấu → ô bảng. Tính mẫu $Q_v(s_1,b)=10+0{,}5\cdot7=13{,}5$.
- **Nguồn:** NG1 tr.6,17–19; ký hiệu $Q_v$ để tránh nhầm.
- **Kết nối:** Giá trị tối ưu yêu cầu tối ưu chính sách tiếp diễn, không chỉ lấy cực đại bảng đang có.
- **Ghi chú triển khai:** $v=(4,7)$ là giá trị của $\pi_0=(a,a)$; vì vậy $Q_v=q^{\pi_0}$, còn $q_*$ chưa được tính. Các ô 4 và 7 lặp lại $v$ vì đó là hành động của chính sách đang đánh giá.
- **Thời lượng:** 3 phút.

#### L04-S08 — Giá trị tối ưu

- **Vai trò và mục tiêu:** Định nghĩa sau trực giác; MT1.
- **Luận điểm và nội dung:** Cho $\Pi$ là lớp chính sách hợp lệ, có thể phụ thuộc lịch sử. Định nghĩa $v_*(s)=\sup_{\pi\in\Pi}v^\pi(s)$ và $q_*(s,a)=\sup_{\pi\in\Pi}q^\pi(s,a)$; $v_*(s)=\max_{a\in\mathcal A(s)}q_*(s,a)$.
- **Hình/ví dụ:** Gắn $q_*(s,a)$ lên nhánh hành động và $v_*(s)$ lên nút trạng thái của cây slide 6.
- **Nguồn:** NG1 tr.7–9; làm rõ miền chính sách.
- **Kết nối:** Tính chất Markov cho phép viết phần tiếp diễn bằng giá trị của trạng thái kế tiếp.
- **Ghi chú triển khai:** Ở đây $q^\pi(s,a)$ dùng quy ước khởi đầu tại $s$, ấn định hành động đầu $a$, rồi theo $\pi$ từ bước sau; không điều kiện hóa trên hành động có xác suất 0. Dùng supremum trước khi chứng minh có chính sách đạt được nó ở phần 6.
- **Thời lượng:** 3 phút.

#### L04-S09 — Bellman tối ưu cho giá trị trạng thái

- **Vai trò và mục tiêu:** Hình thức hóa; MT1.
- **Luận điểm và nội dung:** $v_*(s)=\max_a\sum_{s^{\prime},r}p(s^{\prime},r\mid s,a)[r+\gamma v_*(s^{\prime})]$. Hai phép toán có thứ tự: kỳ vọng theo môi trường cho từng hành động, rồi cực đại theo hành động.
- **Hình/ví dụ:** Cây kỳ vọng ở từng nhánh; khoanh riêng phép tổng và phép cực đại, không dùng màu làm dấu hiệu duy nhất.
- **Nguồn:** NG1 tr.6,8.
- **Kết nối:** Viết cùng quan hệ từ góc nhìn giá trị hành động.
- **Ghi chú triển khai:** Phát biểu đây là phương trình đặc trưng, chưa phải cách giải bằng cách thay số đã biết. So với Bellman kỳ vọng: thay trung bình theo $\pi$ bằng cực đại; chứng minh tồn tại và tính duy nhất ở phần 6.
- **Thời lượng:** 3 phút.

#### L04-S10 — Giá trị hành động và chính sách tham lam

- **Vai trò và mục tiêu:** Hình thức và ứng dụng trực tiếp; MT1.
- **Luận điểm và nội dung:** $q_*(s,a)=\sum_{s^{\prime},r}p(s^{\prime},r\mid s,a)[r+\gamma\max_{a^{\prime}}q_*(s^{\prime},a^{\prime})]$. Khi đã có $q_*$, chọn $\pi_*(s)\in\arg\max_a q_*(s,a)$.
- **Hình/ví dụ:** Đánh dấu hành động đầu đã cố định và cực đại chỉ áp dụng ở trạng thái kế tiếp; minh họa hai ô của một hàng.
- **Nguồn:** NG1 tr.7–9.
- **Kết nối:** Gom các phép tính thành hai toán tử để có thể lặp.
- **Ghi chú triển khai:** Phân biệt $\max$ trả giá trị với $\arg\max$ trả tập hành động. Chính sách tham lam theo bảng xấp xỉ chưa mặc nhiên tối ưu; phép dựng theo $q_*$ sẽ được chứng minh ở slide 37.
- **Thời lượng:** 2 phút.

#### L04-S11 — Hai toán tử Bellman

- **Vai trò và mục tiêu:** Định nghĩa công cụ tính; MT1.
- **Luận điểm và nội dung:** Với $\mathcal V=\mathbb R^{|\mathcal S|}$, $T^\pi,T_*:\mathcal V\to\mathcal V$. $(T^\pi v)(s)=\sum_a\pi(a\mid s)Q_v(s,a)$; $(T_*v)(s)=\max_aQ_v(s,a)$. $T^\pi$ giữ chính sách Markov dừng; $T_*$ chọn hành động theo bảng.
- **Hình/ví dụ:** Hai sơ đồ cùng nhận bảng $v$, khác khối chọn hành động; đầu ra đều là một bảng mới.
- **Nguồn:** NG1 tr.10,13.
- **Kết nối:** Kiểm tra việc áp dụng toán tử có cho nghiệm tối ưu ngay không.
- **Ghi chú triển khai:** Nhắc điểm bất động là bảng không đổi sau phép tính. Nêu $v^\pi=T^\pi v^\pi$ và $v_*=T_*v_*$; chưa dùng chuẩn hay tính co ở đây.
- **Thời lượng:** 2 phút.

#### L04-S12 — Câu hỏi: một cập nhật có phải nghiệm tối ưu

- **Vai trò và mục tiêu:** Kiểm tra phân biệt khái niệm; MT1.
- **Luận điểm và nội dung:** Cho $v=(4,7)$ và bảng $Q_v=(4,2{,}5;7,13{,}5)$ theo mô hình hai trạng thái. Yêu cầu tính $T_*v$ và kiểm tra bảng ban đầu có phải điểm bất động không.
- **Hình/ví dụ:** Hiện hai hàng dữ kiện $(s,a,r,s^{\prime})$ và bảng $v$, giấu bảng đáp án đến lúc chữa.
- **Nguồn:** NG1 tr.10,17–19; câu hỏi biên soạn từ nguồn.
- **Kết nối:** Phần 3 giữ chính sách cố định để tính bảng giá trị một cách có hệ thống.
- **Ghi chú triển khai:** Dành hai phút tính, một phút chữa. Cần kiểm tra toàn bảng; riêng một thành phần không đổi không đủ chứng nhận điểm bất động.
- **Thời lượng:** 3 phút.
- **Câu hỏi:** Tính $T_*v$ và kết luận bảng $v$ đã phải giá trị tối ưu hay chưa.
- **Đáp án/gợi ý:** $T_*v=(4,13{,}5)\ne(4,7)$, nên bảng $v$ đã cho chưa phải $v_*$. Cực đại được lấy theo hành động trong từng hàng.
- **Tiêu chí:** Đúng hai cực đại; phân biệt $Q_v$, $T_*v$ và $v_*$.

## Phần 3. Đánh giá chính sách

Nhận toán tử theo chính sách; giải quyết nhu cầu tính cả tương lai của một quy tắc hành động cố định. Kết quả dùng để cải thiện ở phần 4. **17 phút.**

#### L04-S13 — Giá trị của chính sách cố định

- **Vai trò và mục tiêu:** MT2; mở Phần 3; đặt vấn đề: khi chính sách $\pi_0$ cố định, giá trị một trạng thái phải tính cả tương lai, không chỉ phần thưởng tức thời.
- **Luận điểm và nội dung:** Giữ $\pi_0=(a,a)$: tại mỗi trạng thái đều chọn $a$. Nhiệm vụ là tìm $v^{\pi_0}$ từ các chuyển $s_0\to s_0$ thưởng 2 và $s_1\to s_0$ thưởng 5, với $\gamma=0{,}5$.
- **Hình/ví dụ:** Sơ đồ hai trạng thái, tô đậm hai cạnh $a$; nhấn mạnh phần thưởng tương lai được chiết khấu.
- **Nguồn:** NG1, PDF lecture04-solving-MDP.pdf, tr.14, 17.
- **Kết nối:** Chuẩn bị cho hai phương trình Bellman ở slide 14.
- **Ghi chú triển khai:** Không dùng từ "tối ưu" cho $\pi_0$; chỉ nói "giá trị của chính sách".
- **Thời lượng:** 2 phút.

#### L04-S14 — Hai phương trình Bellman

- **Vai trò và mục tiêu:** Chuyển định nghĩa kỳ vọng thành hệ phương trình tuyến tính giải được bằng tay.
- **Luận điểm và nội dung:** Đặt $x=v^{\pi_0}(s_0)$, $y=v^{\pi_0}(s_1)$. Hệ Bellman: $x=2+0{,}5x$, $y=5+0{,}5x$, suy ra $x=4,y=7$.
- **Hình/ví dụ:** Đặt mỗi phương trình cạnh cạnh chuyển tương ứng; kiểm $y=5+0{,}5\cdot4=7$.
- **Nguồn:** NG1, tr.6, 18.
- **Kết nối:** Nghiệm (4,7) là chuẩn đối chiếu cho các lượt quét từ bảng 0.
- **Ghi chú triển khai:** Nhấn cấu trúc "giá trị hiện tại = phần thưởng + chiết khấu giá trị kế".
- **Thời lượng:** 3 phút.

#### L04-S15 — Đánh giá bằng các lượt quét

- **Vai trò và mục tiêu:** Cho thấy khi không giải hệ trực tiếp, có thể xấp xỉ $v^\pi$ bằng lặp.
- **Luận điểm và nội dung:** Khởi tạo $v_0=(0,0)$ và cập nhật đồng bộ $v_{k+1}=T^{\pi_0}v_k$. Hai lượt đầu: $v_1=(2,5)$, $v_2=(3,6)$; dãy tiến về $(4,7)$.
- **Hình/ví dụ:** Bảng ba cột $v_0,v_1,v_2$ đặt cạnh nghiệm $(4,7)$. Tính mẫu $v_2(s_1)=5+0{,}5\cdot2=6$ để phân biệt thưởng, giá trị cũ và kết quả.
- **Nguồn:** NG1, tr.14; ví dụ tính lại từ tr.17.
- **Kết nối:** Dẫn tới quy trình đánh giá có ngưỡng dừng ở slide 16.
- **Ghi chú triển khai:** Nhấn "đồng bộ": mọi trạng thái dùng bảng cũ $v_k$.
- **Thời lượng:** 3 phút.

#### L04-S16 — Quy trình đánh giá chính sách

- **Vai trò và mục tiêu:** Chuẩn hóa thuật toán đánh giá; MT2.
- **Luận điểm và nội dung:** Đầu vào: mô hình, $\pi$ cố định; khởi tạo $v$, giữ giá trị kết thúc bằng 0. Lặp: $w=T^\pi v$; $\delta=\max_s|w(s)-v(s)|=\|w-v\|_\infty$; nếu $\delta\le\theta$ trả $w$, ngược lại $v=w$ và lặp. Với $\gamma<1$ hội tụ được công bố, chứng minh ở Phần 6. Ngưỡng chỉ trả ước lượng; ý nghĩa sai số sẽ được giải thích ở Phần 6. Đặt $K\ge1$, $\theta>0$; sau lượt thứ $K$, nếu chưa đạt ngưỡng thì trả bảng $w$ cuối cùng kèm nhãn hết ngân sách. Đây không phải chứng nhận đạt sai số mong muốn.
- **Hình/ví dụ:** Lưu đồ vòng lặp với nhánh $\delta\le\theta$.
- **Nguồn:** NG1, tr.6, 14, 34; hw3 B6.
- **Kết nối:** Cho một cách đánh giá xấp xỉ; slide 24 sẽ dùng giải hệ chính xác để giữ bảo đảm hữu hạn.
- **Ghi chú triển khai:** Giải thích $\delta$ bằng lời trước ký hiệu chuẩn: thay đổi lớn nhất trên toàn bảng. Nhắc phương án giải hệ ở slide 14; không trình bày lại trên mặt slide. Quy trình này trả bảng mới $w$ để giữ bước đánh giá vừa tính; lặp giá trị ở slide 31 trả bảng $v$ đã dùng trích chính sách và đo phần dư. Mỗi quy ước có chặn tương ứng, không tráo hai bảng. Dành chặn sai số $\|w-v^\pi\|_\infty\le\gamma\delta/(1-\gamma)$ cho slide 39; hệ số $\gamma$ do $w=T^\pi v$ đã tiến thêm một bước. Phân biệt dừng thực hành với bảo đảm lý thuyết.
- **Thời lượng:** 4 phút.

#### L04-S17 — Hai lịch cập nhật

- **Vai trò và mục tiêu:** So sánh đồng bộ và tại chỗ, ảnh hưởng đến tốc độ hội tụ.
- **Luận điểm và nội dung:** Từ $v_0=(0,0)$, cập nhật đồng bộ cho $(2,5)$. Cập nhật tại chỗ theo thứ tự $s_0$ rồi $s_1$ cho $(2,6)$, vì bước thứ hai dùng giá trị $s_0$ vừa tính. Với mô hình chiết khấu đã nêu, mỗi cập nhật phải dùng đúng Bellman theo bảng hiện có và mỗi trạng thái phải được cập nhật vô hạn lần để có bảo đảm hội tụ.
- **Hình/ví dụ:** Hai bảng cạnh nhau: đồng bộ $(2,5)$; tại chỗ $(2,6)$. Mũi tên chỉ đúng ô nguồn dùng trong phép tính $5+0{,}5\cdot2=6$.
- **Nguồn:** NG1, tr.15.
- **Kết nối:** Bổ sung chi tiết thực hành cho quy trình slide 16.
- **Ghi chú triển khai:** Tránh khái quát hóa "tại chỗ luôn tốt hơn".
- **Thời lượng:** 2 phút.

#### L04-S18 — Câu hỏi: đánh giá chính sách

- **Vai trò và mục tiêu:** Kiểm tra kỹ năng tính một lượt quét và hiểu vai trò của toán tử $T^\pi$.
- **Luận điểm và nội dung:** Cho $\pi_0=(a,a)$, $v_2=(3,6)$, $\gamma=0{,}5$. Tính $v_3$ đồng bộ và giải thích vì sao không lấy cực đại theo hành động.
- **Câu hỏi:** $v_3=T^{\pi_0}v_2$ bằng bao nhiêu? Vì sao không có $\max$?
- **Đáp án/gợi ý:** $v_3=(3{,}5,6{,}5)$: $v_3(s_0)=2+0{,}5\cdot3=3{,}5$; $v_3(s_1)=5+0{,}5\cdot3=6{,}5$. Không có $\max$ vì chính sách được giữ cố định.
- **Tiêu chí:** Đúng hai số; nêu đúng lý do thiếu $\max$; thời lượng đã gồm hỏi–chữa.
- **Nguồn:** NG1, tr.14, 17; tự tính từ nguồn.
- **Kết nối:** Cầu sang Phần 4: khi thêm $\max$ thì có cải thiện chính sách.
- **Ghi chú triển khai:** Yêu cầu sinh viên viết công thức trước khi thay số.
- **Thời lượng:** 3 phút.

## Phần 4. Lặp chính sách

Nhận giá trị của chính sách; dùng một bước nhìn trước để đổi hành động rồi đánh giá lại. Đầu ra là thuật toán chính xác và giới hạn chi phí, tạo nhu cầu lặp giá trị. **23 phút.**

#### L04-S19 — Nhu cầu cải thiện chính sách

- **Vai trò và mục tiêu:** Mở Phần 4 (MT3: cải thiện và PI); chỉ ra $\pi_0$ chưa tốt.
- **Luận điểm và nội dung:** Bảng $q^{\pi_0}=(4,2{,}5;7,13{,}5)$ cho $q^{\pi_0}(s_1,b)=13{,}5>7=v^{\pi_0}(s_1)$. Phép chấm điểm giả sử chỉ hành động đầu đổi sang $b$, sau đó theo $\pi_0$. Giá trị của chính sách mới phải được đánh giá riêng.
- **Hình/ví dụ:** Ô $(s_1,b)=13{,}5$ đặt cạnh giá trị hiện tại $v^{\pi_0}(s_1)=7$; ghi rõ vai trò của hai đại lượng.
- **Nguồn:** NG1, tr.19.
- **Kết nối:** Dẫn tới cơ chế "nhìn trước một bước" ở slide 20.
- **Ghi chú triển khai:** Nhấn sai lầm phổ biến: coi giá trị $Q$ tính được là giá trị của chính sách mới.
- **Thời lượng:** 2 phút.

#### L04-S20 — Cải thiện bằng một bước nhìn trước

- **Vai trò và mục tiêu:** Trình bày bước tham lam trên toàn bảng $Q$.
- **Luận điểm và nội dung:** Tham lam theo toàn bảng $q^{\pi_0}$: tại $s_0$, chọn $a$ vì $4>2{,}5$; tại $s_1$, chọn $b$ vì $13{,}5>7$. Chính sách mới là $\pi_1=(a,b)$.
- **Hình/ví dụ:** Bảng $q^{\pi_0}$ với ô được chọn mỗi hàng đánh dấu; mũi tên chỉ $\pi_0\to\pi_1$.
- **Nguồn:** NG1, tr.19.
- **Kết nối:** $\pi_1$ cần được đánh giá lại — slide 21.
- **Ghi chú triển khai:** Nhấn tham lam từng trạng thái, không phải chọn toàn cục.
- **Thời lượng:** 3 phút.

#### L04-S21 — Đánh giá lại sau cải thiện

- **Vai trò và mục tiêu:** Cho thấy chính sách mới phải được đánh giá lại theo mô hình của chính sách mới.
- **Luận điểm và nội dung:** Đánh giá $\pi_1=(a,b)$ cho $v^{\pi_1}=(4,20)$. Khi đó $q^{\pi_1}(s_0,b)=-1+0{,}5\cdot20=9>4$, nên đổi sang $\pi_2=(b,b)$. Đánh giá lại được $v^{\pi_2}=(9,20)$.
- **Hình/ví dụ:** Bảng ba hàng: $\pi_0=(a,a)$ với $(4,7)$; $\pi_1=(a,b)$ với $(4,20)$; $\pi_2=(b,b)$ với $(9,20)$. Giá trị không đổi được ghi rõ do quyết định tại trạng thái đó được giữ nguyên.
- **Nguồn:** NG1, tr.19; các bước bị lược ở nguồn được tách rõ ở đây.
- **Kết nối:** Chuẩn bị quy tắc cải thiện tổng quát ở slide 22.
- **Ghi chú triển khai:** Nhấn mỗi chính sách mới đều cần đánh giá riêng, có thể dùng bảng cũ làm khởi tạo, nhưng phải tính lại giá trị của chính sách mới.
- **Thời lượng:** 3 phút.

#### L04-S22 — Quy tắc cải thiện chính sách

- **Vai trò và mục tiêu:** Phát biểu quy tắc tham lam có xử lý hòa, bảo đảm thuật toán tái lập.
- **Luận điểm và nội dung:** $\pi'(s)\in\operatorname{argmax}_a Q_{v^\pi}(s,a)$; nếu hành động cũ của $\pi$ thuộc argmax thì giữ hành động cũ; nếu không, chọn theo thứ tự cố định của tập hành động. Mọi so sánh luôn dùng $v^\pi$ cũ, chưa cập nhật.
- **Hình/ví dụ:** Với $q^{\pi_0}$: $s_0$ giữ $a$ (thuộc argmax), $s_1$ đổi sang $b$; nếu hai hành động bằng nhau thì giữ hành động cũ.
- **Nguồn:** NG1, tr.20; bổ sung phần hòa để thuật toán tái lập.
- **Kết nối:** Quy tắc này là giả thiết của định lý ở slide 23.
- **Ghi chú triển khai:** Giữ hành động cũ khi hòa giúp tránh đổi qua lại giữa các hành động đồng hạng. Chuẩn bị chứng minh kế tiếp: nếu $u\le v$ theo từng trạng thái thì $Q_u(s,a)\le Q_v(s,a)$ vì $\gamma\ge0$ và xác suất không âm; do đó $T^{\pi'}u\le T^{\pi'}v$.
- **Thời lượng:** 3 phút.

#### L04-S23 — Định lý cải thiện chính sách

- **Vai trò và mục tiêu:** Bảo đảm mỗi bước tham lam không làm chính sách tệ hơn (MT3).
- **Luận điểm và nội dung:** Phát biểu: $v^\pi\le T^{\pi'}v^\pi$ và do đó $v^\pi\le v^{\pi'}$. Phác thảo chứng minh: $T^{\pi'}v^\pi=\max_a Q_{v^\pi}\ge T^\pi v^\pi=v^\pi$; dùng đơn điệu (trọng số không âm) lặp khai triển: $v^\pi\le T^{\pi'}v^\pi\le (T^{\pi'})^2v^\pi\le\cdots$, hạng đuôi $\gamma^n\mathbb E_{\pi'}[v^\pi(S_n)]$ tiến về 0 vì $\|v^\pi\|_\infty\le R_{\max}/(1-\gamma)$ và $0\le\gamma<1$, nên $v^\pi\le v^{\pi'}$. Nghiêm ngặt tại ít nhất một trạng thái nếu $\pi$ chưa tối ưu.
- **Hình/ví dụ:** Sơ đồ ba mũi tên $v^\pi\le T^{\pi'}v^\pi\le v^{\pi'}$.
- **Nguồn:** NG1, tr.21.
- **Kết nối:** Là nền của bảo đảm dừng ở slide 25.
- **Ghi chú triển khai:** Không viện dẫn tính co chưa chứng minh; chỉ dùng đơn điệu và hạng đuôi chiết khấu tiến về 0.
- **Thời lượng:** 3 phút.

#### L04-S24 — Quy trình lặp chính sách

- **Vai trò và mục tiêu:** Ghép đánh giá và cải thiện thành thuật toán PI đầy đủ (MT3).
- **Luận điểm và nội dung:** Đầu vào: mô hình (không cần $\pi$); khởi tạo $\pi$ xác định. Vòng lặp: đánh giá chính xác bằng hệ tuyến tính $(I-\gamma P^\pi)v=r^\pi$; cải thiện tham lam, giữ hòa theo slide 22; kiểm tra tất cả trạng thái; nếu $\pi$ không đổi, trả $\pi, v^\pi$; ngược lại lặp. Sau lượt đánh giá thứ $K\ge1$, nếu bước cải thiện còn đổi hành động, trả chính sách $\pi$ vừa được đánh giá cùng $v^\pi$ và nhãn "chưa chứng nhận tối ưu"; không ghép chính sách mới chưa đánh giá với bảng cũ. Bản đánh giá ngưỡng ở slide 16 chỉ là lựa chọn xấp xỉ, không được ghép vào bảo đảm hữu hạn của PI chính xác.
- **Hình/ví dụ:** Lưu đồ hai khối "đánh giá" – "cải thiện" với nhánh dừng.
- **Nguồn:** NG1, tr.20, 33.
- **Kết nối:** Dùng định lý slide 23 để giải thích vì sao dừng khi $\pi$ không đổi.
- **Ghi chú triển khai:** Nhấn mạnh phân biệt PI chính xác và PI xấp xỉ.
- **Thời lượng:** 4 phút.

#### L04-S25 — Chính sách ổn định và dừng hữu hạn

- **Vai trò và mục tiêu:** Chứng minh PI dừng sau số hữu hạn vòng (MT3).
- **Luận điểm và nội dung:** Số chính sách xác định là $\prod_s|A(s)|$, hữu hạn trong không gian hữu hạn với mỗi $A(s)$ khác rỗng. Cải thiện nghiêm ngặt khi đổi chính sách nên không lặp lại chính sách; hòa giữ chính sách cũ. Khi $\pi$ ổn định, thỏa $T_*v^\pi=v^\pi$, tức tối ưu Bellman. Bảo đảm dừng dựa trên định lý Bellman tối ưu đã phát biểu; chứng minh đầy đủ ở Phần 6.
- **Hình/ví dụ:** Chuỗi $\pi_0\to\pi_1\to\pi_2$ rồi dừng; hai trạng thái, mỗi trạng thái hai hành động nên có $2\times2=4$ chính sách xác định.
- **Nguồn:** NG1, tr.9, 33.
- **Kết nối:** Khép vòng Phần 4; phần 5 giảm chi phí của bước đánh giá đầy đủ, phần 6 chứng minh bảo đảm chung.
- **Ghi chú triển khai:** Gắn bảo đảm dừng hữu hạn với đánh giá chính xác và giữ hành động cũ khi hòa; không suy rộng sang bản đánh giá bị cắt.
- **Thời lượng:** 2 phút.

#### L04-S26 — Câu hỏi: kiểm tra bước cải thiện

- **Vai trò và mục tiêu:** Kiểm tra MT3: thực hành tham lam và hiểu tiêu chí dừng.
- **Luận điểm và nội dung:** Cho $v^{\pi_1}=(4,20)$; điền $q^{\pi_1}(s_0,a)$, $q^{\pi_1}(s_0,b)$ và chính sách sau cải thiện, rồi giải thích vai trò giữ hành động cũ khi hòa.
- **Câu hỏi:** Hai giá trị $Q$ tại $s_0$ là gì? $\pi_2$ là gì? Vì sao cần giữ hòa?
- **Đáp án/gợi ý:** $q^{\pi_1}(s_0,a)=2+0{,}5\cdot4=4$; $q^{\pi_1}(s_0,b)=-1+0{,}5\cdot20=9$; $\pi_2=(b,b)$. Giữ hòa tránh đổi qua lại giữa các hành động đồng hạng.
- **Tiêu chí:** Đúng hai số và $\pi_2$; không kết luận nghiêm ngặt tại mọi trạng thái; tránh lặp giữa hành động đồng hạng.
- **Nguồn:** NG1, tr.19–21, 33.
- **Kết nối:** Giá trị tốt hơn đòi hỏi đánh giá lại; phần 5 xét cách cập nhật trực tiếp để tránh giải hệ ở từng vòng.
- **Ghi chú triển khai:** Thời lượng đã gồm hỏi–chữa; yêu cầu nêu rõ so sánh dùng $v^{\pi_1}$ cũ.
- **Thời lượng:** 3 phút.

## Phần 5. Lặp giá trị

Nhận giới hạn chi phí của đánh giá chính sách đầy đủ. Dùng lưới năm ô để thấy cập nhật cục bộ truyền thông tin về phần thưởng; sau đó mới viết thuật toán tổng quát. **23 phút.**

#### L04-S27 — Cập nhật từ bảng giá trị hiện có

- **Vai trò và mục tiêu:** Vấn đề và trực giác mở phần; MT4.
- **Luận điểm và nội dung:** Lặp giá trị cập nhật tốt nhất từ bảng đang có, thay cho đánh giá đầy đủ từng chính sách. Lưới $c_1,\ldots,c_5$: đi trái/phải tất định; $c_5$ kết thúc; bước thường thưởng $-1$, riêng $c_4\to c_5$ thưởng 24; $\gamma=0{,}5$.
- **Hình/ví dụ:** Năm ô ngang; cạnh đến đích ghi $+24$, cạnh thường ghi $-1$. Ra trái ở $c_1$ thì đứng yên, thưởng $-1$. Tham số đã đổi theo yêu cầu ngày 24-09-2026.
- **Nguồn:** NG1 tr.23,25; quy ước biên được bổ sung để mô hình tự chứa.
- **Kết nối:** Từ mô hình, tính một lượt với bảng khởi tạo bằng 0.
- **Ghi chú triển khai:** Sau khi đến đích không nhận thêm thưởng; $v(c_5)=0$. Không đưa nhiễu 20% của NG3 vào ví dụ tất định này.
- **Thời lượng:** 2 phút.

#### L04-S28 — Một lượt quét trên lưới

- **Vai trò và mục tiêu:** Ví dụ tính tay trước công thức tổng quát; MT4.
- **Luận điểm và nội dung:** Từ $v_0=(0,0,0,0,0)$, một lượt đồng bộ cho $v_1=(-1,-1,-1,24,0)$. Tại $c_4$, đi phải cho $24+0{,}5\cdot0=24$; các ô xa đích chỉ thấy chi phí bước đi.
- **Hình/ví dụ:** Hai hàng lưới $v_0,v_1$; các mũi tên đều đi từ hàng cũ sang hàng mới.
- **Nguồn:** NG1 tr.25–26.
- **Kết nối:** Lặp cùng thao tác để phần thưởng ở đích ảnh hưởng tới các ô xa.
- **Ghi chú triển khai:** Giữ bảng cũ suốt lượt. Việc chưa thấy đích không đồng nghĩa đường đi không có giá trị dài hạn.
- **Thời lượng:** 3 phút.

#### L04-S29 — Giá trị lan dần từ đích

- **Vai trò và mục tiêu:** Phát hiện cơ chế từ ví dụ; MT4.
- **Luận điểm và nội dung:** $v_2=(-1{,}5,-1{,}5,11,24,0)$; $v_3=(-1{,}75,4{,}5,11,24,0)$; $v_4=(1{,}25,4{,}5,11,24,0)$. Tính mẫu $v_2(c_3)=-1+0{,}5\cdot24=11$ và $v_3(c_2)=-1+0{,}5\cdot11=4{,}5$.
- **Hình/ví dụ:** Bảng năm cột trạng thái, các hàng $k=0,\ldots,4$; đánh dấu ô thay đổi bằng viền và nhãn lượt, không chỉ tô màu.
- **Nguồn:** NG1 tr.27–28; đã tính lại toàn bảng.
- **Kết nối:** Dữ kiện và chỉ số của bảng trở thành công thức lặp giá trị.
- **Ghi chú triển khai:** Ví dụ đạt điểm bất động sau bốn cập nhật; không suy ra mọi MDP dừng chính xác sau hữu hạn lượt. Có thể kiểm thêm $T_*v_4=v_4$.
- **Thời lượng:** 3 phút.

#### L04-S30 — Quy tắc lặp giá trị

- **Vai trò và mục tiêu:** Hình thức hóa từ lưới; MT4.
- **Luận điểm và nội dung:** $v_{k+1}=T_*v_k$, tức $v_{k+1}(s)=\max_a\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_k(s')]$. $k$ đếm lượt tính trên mô hình, không phải bước thời gian tương tác.
- **Hình/ví dụ:** Đặt phép tính $v_2(c_3)$ cạnh công thức tổng quát và nối từng đại lượng.
- **Nguồn:** NG1 tr.23–24,26–27.
- **Kết nối:** Cần một quy trình dừng và trả chính sách từ bảng có thể kiểm tra.
- **Ghi chú triển khai:** Từ $v_0=0$, có thể diễn giải $v_k$ là giá trị tối ưu của $k$ quyết định còn lại với giá trị cuối bằng 0. Với khởi tạo khác, không dùng diễn giải này nếu không nói rõ thưởng cuối. $v_k$ không nhất thiết bằng giá trị dài hạn của một chính sách dừng.
- **Thời lượng:** 3 phút.

#### L04-S31 — Quy trình lặp giá trị có kiểm tra dừng

- **Vai trò và mục tiêu:** Đặc tả đầy đủ thuật toán; MT4, chuẩn bị MT5.
- **Luận điểm và nội dung:** Đầu vào mô hình, $v_0$, ngưỡng phần dư $\theta>0$, ngân sách $K\ge1$. Với bảng hiện tại $v$: trước hết tính $Q_v(s,a)$ cho từng cặp trạng thái–hành động; từ bảng đó lấy $w(s)=\max_aQ_v(s,a)$, $\pi_v(s)\in\arg\max_aQ_v(s,a)$; sau đó tính $\rho(v)=\max_s|w(s)-v(s)|$. Nếu $\rho(v)\le\theta$, trả $v,\pi_v,\rho(v)$; nếu chưa đạt và còn lượt, đặt $v\leftarrow w$; nếu đã hết $K$ lượt, trả $v,\pi_v,\rho(v)$ cùng nhãn hết ngân sách, chưa chứng nhận đạt ngưỡng.
- **Hình/ví dụ:** Lưu đồ có hai nhánh trả: đạt ngưỡng; hết ngân sách. Tách nhãn bảng đang kiểm $v$ với bảng dự kiến $w$.
- **Nguồn:** NG1 tr.24,34; sửa đặc tả để phần dư gắn đúng bảng trả.
- **Kết nối:** Chính sách và phần dư phải cùng được tính từ bảng được trả.
- **Ghi chú triển khai:** Ở lượt thứ $K$, nếu chưa đạt thì trả chính bảng $v$ đã kiểm cùng $\pi_v,\rho(v)$ và nhãn hết ngân sách, không âm thầm trả $w$ chưa kiểm. Trạng thái kết thúc giữ 0; phá hòa theo thứ tự cố định. Chưa gọi ngưỡng phần dư là sai số giá trị; phần 6 lập quan hệ này. Một lượt tính $Q_v$ phục vụ cả $w$, chính sách và phần dư; không tính lặp hai lần.
- **Thời lượng:** 4 phút.

#### L04-S32 — Trích chính sách từ cùng bảng giá trị

- **Vai trò và mục tiêu:** Ứng dụng thuật toán; MT4.
- **Luận điểm và nội dung:** $\pi_v(s)\in\arg\max_aQ_v(s,a)$ và $T^{\pi_v}v=T_*v$. Dùng $v_1=(-1,-1,-1,24,0)$: tại $c_3$, điểm trái $-1{,}5$, điểm phải 11, nên chọn phải.
- **Hình/ví dụ:** Cùng một hàng $v_1$ cấp dữ liệu cho hai nhánh; ghi rõ $v_1$ trên cả nhánh tính điểm và nhánh lấy phần dư.
- **Nguồn:** NG1 tr.24,26,28; đồng nhất chỉ số bảng.
- **Kết nối:** So lượng phép tính cần thiết trước khi xét sai số và hội tụ.
- **Ghi chú triển khai:** $11=Q_{v_1}(c_3,a_R)$, với $a_R$ là hành động đi phải; đây là phép nhìn trước từ $v_1$, chưa tự gọi là giá trị thật của chính sách vừa trích. Không dùng lẫn $v$ và $w$.
- **Thời lượng:** 3 phút.

#### L04-S33 — Chi phí của một lượt tính

- **Vai trò và mục tiêu:** Đánh giá giới hạn thuật toán; MT4, MT6.
- **Luận điểm và nội dung:** Đặt $n=|\mathcal S|$, $m=\max_s|\mathcal A(s)|$. Một lượt lặp giá trị với mô hình chuyển dày tốn $O(n^2m)$; mô hình thưa tốn theo số nhánh chuyển có xác suất khác 0. Lặp chính sách chính xác còn giải hệ tuyến tính dày, chi phí thường dùng $O(n^3)$, rồi cải thiện.
- **Hình/ví dụ:** Bảng hai phương pháp, ghi thao tác phải thực hiện thay vì nhãn “nhanh/chậm”.
- **Nguồn:** NG1 tr.29; định lượng chi phí từ phép tổng và giải hệ.
- **Kết nối:** Chi phí một lượt chưa cho biết cần bao nhiêu lượt; cần kết quả hội tụ.
- **Ghi chú triển khai:** Bảng giá trị đồng bộ dùng $O(n)$ bộ nhớ bổ sung nếu giữ cực đại theo từng trạng thái; lưu toàn mô hình dày cần $O(n^2m)$. Không coi số lượt lặp của hai thuật toán là cùng đơn vị công việc hoặc khẳng định một phương pháp luôn nhanh hơn.
- **Thời lượng:** 2 phút.

#### L04-S34 — Câu hỏi: tính lượt tiếp theo

- **Vai trò và mục tiêu:** Kiểm tra cơ chế lan truyền và đồng bộ; MT4.
- **Luận điểm và nội dung:** Cho $v_2=(-1{,}5,-1{,}5,11,24,0)$ và cùng mô hình lưới. Tính hai ô của $v_3$ rồi đánh giá kết luận hội tụ từ một ô không đổi.
- **Hình/ví dụ:** Hiển thị $v_2$ và hai ô trống của $v_3(c_1),v_3(c_2)$; các phần còn lại chưa cần tính lại.
- **Nguồn:** NG1 tr.25–27; câu hỏi từ ví dụ nguồn.
- **Kết nối:** Việc một vài ô ổn định dẫn tới nhu cầu chặn sai số trên toàn bảng.
- **Ghi chú triển khai:** Hai phút tính, một phút giải thích; phải chỉ ra bảng dùng trong mỗi phép tính.
- **Thời lượng:** 3 phút.
- **Câu hỏi:** Tính $v_3(c_1),v_3(c_2)$. Giá trị $c_4$ không đổi đã đủ kết luận toàn thuật toán hội tụ hay chưa?
- **Đáp án/gợi ý:** $v_3(c_1)=-1{,}75$, $v_3(c_2)=4{,}5$; $c_4$ không đổi chưa đủ kết luận toàn thuật toán hội tụ vì các trạng thái khác còn thay đổi.
- **Tiêu chí:** Dùng $v_2$ xuyên suốt, không dùng ngay $v_3(c_1)$; không suy từ một ô sang toàn bảng.

## Phần 6. Hội tụ và sai số

Nhận hai quy trình đã chạy được; giải quyết nhu cầu chứng nhận nghiệm và chọn ngưỡng dừng. Đi từ khoảng cách giữa hai bảng tới tính co, điểm bất động và phần dư. Giới hạn CartPole áp dụng lại đúng các giả thiết. **20 phút.**

#### L04-S35 — Khoảng cách giữa hai bảng giá trị

- **Vai trò và mục tiêu:** Vấn đề, trực giác và ví dụ trước định lý; MT5.
- **Luận điểm và nội dung:** Với MDP hai trạng thái, $u=(4,7)$ và $v=(8,9)$ cách nhau tối đa 4. Sau cập nhật, $T_*u=(4,13{,}5)$ và $T_*v=(6,14{,}5)$ cách nhau tối đa $2=0{,}5\cdot4$.
- **Hình/ví dụ:** Hai cặp bảng trước/sau, ghi hiệu tuyệt đối mỗi ô; đặt tên $\|u-v\|_\infty=\max_s|u(s)-v(s)|$.
- **Nguồn:** NG1 tr.10,17,31; ví dụ sư phạm tính lại từ mô hình nguồn.
- **Kết nối:** Chứng minh độ co này cho mọi cặp bảng, không chỉ hai bảng vừa tính.
- **Ghi chú triển khai:** Tính mẫu $T_*v(s_0)=\max\{2+0{,}5\cdot8,-1+0{,}5\cdot9\}=6$; $T_*v(s_1)=\max\{5+0{,}5\cdot8,10+0{,}5\cdot9\}=14{,}5$. Hai bảng không cần là giá trị của chính sách nào; ví dụ không thay chứng minh.
- **Thời lượng:** 2 phút.

#### L04-S36 — Tính co của toán tử Bellman

- **Vai trò và mục tiêu:** Định lý và bước chứng minh then chốt; MT5.
- **Luận điểm và nội dung:** Với mọi $u,v\in\mathcal V$, $\|T_*u-T_*v\|_\infty\le\gamma\|u-v\|_\infty$. Dùng $|\max_ax_a-\max_ay_a|\le\max_a|x_a-y_a|$, rồi trọng số xác suất không âm có tổng 1. $T^\pi$ cũng thỏa chặn này khi $\pi$ cố định.
- **Hình/ví dụ:** Ba bước ngắn: chênh hai cực đại → kỳ vọng của chênh giá trị → $\gamma\|u-v\|_\infty$; đánh dấu chỗ triệt tiêu phần thưởng.
- **Nguồn:** NG1 tr.31; bước bất đẳng thức được mở để người học theo được.
- **Kết nối:** Co với hệ số nhỏ hơn 1 cho nghiệm bất động duy nhất và dãy lặp tiến tới nó.
- **Ghi chú triển khai:** “co” cần hệ số nhỏ hơn 1; bất đẳng thức chỉ với hệ số 1 chưa đủ. Khi $\gamma=0$, toán tử không phụ thuộc bảng vào và đạt nghiệm sau một cập nhật.
- **Thời lượng:** 3 phút.

#### L04-S37 — Điểm bất động và chính sách tối ưu

- **Vai trò và mục tiêu:** Định lý tồn tại, kèm phác thảo hai bước; MT5.
- **Luận điểm và nội dung:** Định lý điểm bất động Banach: ánh xạ co trên không gian đầy đủ có đúng một điểm bất động và lặp tiến tới điểm đó. $\mathcal V=\mathbb R^n$ với chuẩn vô cùng đầy đủ, nên $T_*$ có điểm bất động $\bar v$. Chọn chính sách dừng xác định $\bar\pi$ tham lam theo $\bar v$; khi đó $T^{\bar\pi}\bar v=T_*\bar v=\bar v$, nên $v^{\bar\pi}=\bar v$.
- **Hình/ví dụ:** Sơ đồ hai nhánh: mọi chính sách có giá trị không vượt $\bar v$; chính sách tham lam đạt $\bar v$; nối thành $\bar v=v_*$.
- **Nguồn:** NG1 tr.9,10,31–32; bổ sung cầu nối điểm bất động → tối ưu.
- **Kết nối:** Đã nhận diện đích của dãy lặp; có thể chặn tốc độ tiến tới đích.
- **Ghi chú triển khai:** Trong 4 phút chỉ phát biểu Banach và giải thích sơ đồ hai nhánh: điểm bất động chặn mọi giá trị; chính sách tham lam đạt cận. Dùng tính duy nhất điểm bất động của $T^{\bar\pi}$ cho nhánh đạt cận. Không trình bày đầy đủ quy nạp theo lịch sử trên lớp. Chi tiết đọc thêm cho giảng viên: với lịch sử $H_t$, $\bar v(S_t)\ge\mathbb E_\pi[R_{t+1}+\gamma\bar v(S_{t+1})\mid H_t]$; lấy kỳ vọng và lặp bất đẳng thức, hạng đuôi bị chặn bởi $\gamma^n\|\bar v\|_\infty\to0$. Điều kiện hóa theo toàn lịch sử, không dùng $T^\pi$ cho chính sách phụ thuộc lịch sử. Phát biểu tối ưu vẫn bao phủ lớp $\Pi$ ở slide 8; phần đọc thêm hoàn thiện chứng minh, không bổ sung giả thiết ngầm.
- **Thời lượng:** 4 phút.

#### L04-S38 — Hội tụ hình học của lặp giá trị

- **Vai trò và mục tiêu:** Hệ quả và ứng dụng định lượng; MT5.
- **Luận điểm và nội dung:** $\|v_k-v_*\|_\infty\le\gamma^k\|v_0-v_*\|_\infty$. Minh họa số học: giả sử chặn sai số đầu là 64, với $\gamma=0{,}5$, sau 6 lượt chặn bằng 1 và sau 7 lượt chặn bằng $0{,}5<1$.
- **Hình/ví dụ:** Đồ thị SVG của chặn $64\cdot(0{,}5)^k$, trục hoành số lượt, trục tung chặn sai số; đường ngưỡng 1, mốc 6 và 7. Ghi rõ chặn lý thuyết, không là thực nghiệm.
- **Nguồn:** NG1 tr.32,34; thay dữ kiện minh họa theo yêu cầu ngày 24-09-2026, giữ công thức hội tụ.
- **Kết nối:** $v_*$ chưa biết nên chặn chứa sai số ban đầu khó dùng trực tiếp; chuyển sang đại lượng tính được.
- **Ghi chú triển khai:** $64\cdot(0{,}5)^k<1$ tương đương $2^{6-k}<1$, tức $k>6$. Số 64 là giả định minh họa, không lấy từ lưới. Bảy lượt là đủ theo chặn, không là số lượt tối thiểu thực của mọi MDP. Hệ số gần 1 làm chặn giảm chậm hơn.
- **Thời lượng:** 3 phút.

#### L04-S39 — Phần dư Bellman và ngưỡng dừng

- **Vai trò và mục tiêu:** Chuyển bảo đảm thành quyết định tính toán; MT5.
- **Luận điểm và nội dung:** $\rho(v)=\|T_*v-v\|_\infty$ tính được. Đặt $e=\|v-v_*\|_\infty$: $e\le\rho(v)+\gamma e$, nên $e\le\rho(v)/(1-\gamma)$. Muốn $e\le\varepsilon_v$, dùng ngưỡng $\theta=(1-\gamma)\varepsilon_v$ ở slide 31.
- **Hình/ví dụ:** Chuỗi bảng $v$ → phần dư → chặn sai số; với $\gamma=0{,}5$, muốn $\varepsilon_v=0{,}2$ thì dùng $\theta=0{,}1$. Mỗi số ghi kèm tên đại lượng.
- **Nguồn:** NG1 tr.31–34; phép suy diễn bổ sung để ngưỡng có ý nghĩa.
- **Kết nối:** Mọi bảo đảm còn phụ thuộc vào mô hình và biểu diễn đã giả định.
- **Ghi chú triển khai:** Mở bước suy diễn bằng bất đẳng thức tam giác: $\|v-v_*\|_\infty\le\|v-T_*v\|_\infty+\|T_*v-T_*v_*\|_\infty\le\rho(v)+\gamma\|v-v_*\|_\infty$. Slide 31 trả $v$ có phần dư đã đo. Nếu dùng bản trả $w=Tv$ như đánh giá chính sách ở slide 16, chặn của $w$ là $\gamma\|Tv-v\|_\infty/(1-\gamma)$. Phân biệt hai bảng, không đổi hệ số ngầm. Chặn mất mát của chính sách tham lam chỉ đặt trong mục đọc thêm của analysis, không tăng tải tuyến chính.
- **Thời lượng:** 3 phút.

#### L04-S40 — Giới hạn của mô hình dạng bảng

- **Vai trò và mục tiêu:** Áp dụng giả thiết vào trường hợp biên; MT6.
- **Luận điểm và nội dung:** CartPole có trạng thái $(x,\dot x,\theta,\dot\theta)$. Chia $x,\dot x$ mỗi biến 3 khoảng, $\theta,\dot\theta$ mỗi biến 6 khoảng: $3\times3\times6\times6=324$ ô tạo biểu diễn hữu hạn, nhưng chưa cung cấp hạt nhân chuyển/phần thưởng hay bảo đảm tính Markov của trạng thái gộp.
- **Hình/ví dụ:** Sơ đồ trạng thái liên tục → chỉ số ô → mô hình xấp xỉ; đặt ô “cần xác định chuyển và thưởng” trước khối quy hoạch động. Vẽ hai điểm liên tục cùng ô để minh họa thông tin bị gộp; sơ đồ khái niệm, không gán số liệu hay kết quả mô phỏng.
- **Nguồn:** NG1 tr.35–37; làm rõ điều kiện bị lược trong sơ đồ nguồn.
- **Kết nối:** Kiểm tra lại việc áp dụng ngưỡng và bảo đảm đúng miền.
- **Ghi chú triển khai:** Phân biệt sai số lặp trên mô hình đã cho với sai số do rời rạc hóa hoặc ước lượng mô hình. Tối ưu mô hình hữu hạn không tự chứng minh tối ưu môi trường liên tục. Chỉ đặc tả sơ đồ, không thêm mô phỏng hay mã.
- **Thời lượng:** 2 phút.

#### L04-S41 — Câu hỏi: kiểm tra sai số và giả thiết

- **Vai trò và mục tiêu:** Kiểm tra MT5–MT6.
- **Luận điểm và nội dung:** MDP hữu hạn đã biết mô hình có $\rho(v)=0{,}15$, $\gamma=0{,}5$. Cần bảo đảm sai số giá trị không quá $0{,}2$. Xét thêm trường hợp thay riêng $\gamma$ bằng 1.
- **Hình/ví dụ:** Hai thẻ dữ kiện: trường hợp chiết khấu và trường hợp $\gamma=1$.
- **Nguồn:** NG1 tr.31–34; dữ kiện câu hỏi được biên soạn từ chặn vừa suy ra.
- **Kết nối:** Phần kết dùng các điều kiện này để chọn và đánh giá thuật toán.
- **Ghi chú triển khai:** Một phút tính, một phút giải thích giả thiết, một phút chữa. Không mở thêm lý thuyết MDP không chiết khấu.
- **Thời lượng:** 3 phút.
- **Câu hỏi:** Chặn sai số giá trị bằng bao nhiêu; đã bảo đảm ngưỡng $0{,}2$ chưa; chứng minh còn dùng được khi $\gamma=1$ không?
- **Đáp án/gợi ý:** $0{,}15/(1-0{,}5)=0{,}3$, chưa bảo đảm ngưỡng $0{,}2$. Khi $\gamma=1$, mất co nghiêm ngặt và mẫu số bằng 0, cần giả thiết hoặc lập luận khác.
- **Tiêu chí:** Phân biệt “chưa bảo đảm” với “chắc chắn sai số lớn”; gọi đúng giả thiết $\gamma<1$.

## Phần 7. Tổng hợp và kết luận

Trở lại quyết định ở mở bài, đối chiếu sản phẩm với mục tiêu và dùng một tình huống tổng hợp để kiểm tra. Không giới thiệu thuật toán mới. **9 phút.**

#### L04-S42 — Chọn quy trình theo đầu ra cần tính

- **Vai trò và mục tiêu:** Tổng hợp quan hệ các phương pháp; MT2–MT6.
- **Luận điểm và nội dung:** Cho mô hình và chính sách, đánh giá để tìm $v^\pi$; cho mô hình và yêu cầu điều khiển, dùng lặp chính sách hoặc lặp giá trị. Lặp chính sách có bước đánh giá đầy đủ; lặp giá trị cập nhật trực tiếp bảng rồi trích chính sách.
- **Hình/ví dụ:** Bảng đầu vào, đầu ra, thao tác chính, điều kiện dừng và điều kiện bảo đảm; tối đa ba hàng phương pháp.
- **Nguồn:** NG1 tr.12–14,20,24,29,38.
- **Kết nối:** Dùng bảng này để giải thích lời giải của ví dụ mở đầu.
- **Ghi chú triển khai:** Thiếu mô hình thì các phép tổng theo $p$ chưa thực hiện được; chỉ nối sang nhu cầu học từ trải nghiệm ở Bài 05, không giảng Monte Carlo hay sai phân thời gian.
- **Thời lượng:** 2 phút.

#### L04-S43 — Lời giải cho bài toán mở đầu

- **Vai trò và mục tiêu:** Thu hồi vấn đề trung tâm; MT1, MT3, MT5.
- **Luận điểm và nội dung:** Với mô hình hai trạng thái, $\pi_*=(b,b)$ cho $v_*=(9,20)$. Bảng $Q_{v_*}=(6{,}5,9;9{,}5,20)$ đạt cực đại ở $b$ tại mỗi trạng thái và $T_*v_*=v_*$. Có cả chính sách đạt giá trị và chứng nhận Bellman.
- **Hình/ví dụ:** Mô hình mở đầu cạnh bảng điểm cuối; nối dãy thưởng $-1,10,10,\ldots$ với giá trị 9.
- **Nguồn:** NG1 tr.17–21,31–33; phép kiểm số tính lại.
- **Kết nối:** Chỉ ra các sản phẩm sinh viên cần tự làm ở bài tập.
- **Ghi chú triển khai:** $Q_{v_*}(s_0,b)=-1+0{,}5\cdot20=9$; $Q_{v_*}(s_1,b)=10+0{,}5\cdot20=20$; hai hành động còn lại cho $6{,}5$ và $9{,}5$. Giá trị ở $s_0$ tăng từ 4 lên 9 do đổi quyết định dài hạn, trên cùng mô hình và hệ số chiết khấu.
- **Thời lượng:** 2 phút.

#### L04-S44 — Bài tập và tài liệu đọc

- **Vai trò và mục tiêu:** Định hướng tự học bằng sản phẩm cụ thể; MT2–MT5.
- **Luận điểm và nội dung:** NG2 Bài 9: tính một lượt lặp giá trị và một bước cải thiện trên MDP ba trạng thái; Bài 6: lập hệ Bellman và giải thích tính khả nghịch; Bài 3/7: viết chứng minh tồn tại/đơn điệu bằng lời của mình, nêu từng giả thiết và bước dùng giả thiết đó. Đọc lại NG1 tr.20–24,31–34.
- **Hình/ví dụ:** Ba dòng “bài → sản phẩm cần nộp”; không đưa lời giải dài lên mặt slide.
- **Nguồn:** NG2 tr.1–2, B3/B6/B7/B9; NG1 như trên.
- **Kết nối:** Câu kiểm tra cuối đánh giá khả năng sử dụng kết quả vừa học.
- **Ghi chú triển khai:** Khối chữa bài 30 phút ngoài tuyến chính có thể dùng B9 và B6, không thêm slide chính. NG2 B10 có Monte Carlo, Q-learning và xấp xỉ hàm; NG3 có MC/TD nên không giao các phần đó như kiến thức đã dạy. Không tự tạo code demo.
- **Thời lượng:** 2 phút.

#### L04-S45 — Câu hỏi: đánh giá một kết quả lập kế hoạch

- **Vai trò và mục tiêu:** Kiểm tra tổng hợp, kết bài; MT3–MT6.
- **Luận điểm và nội dung:** Trên MDP hữu hạn có mô hình chính xác và $\gamma=0{,}5$, lặp giá trị dừng với $\rho(v)=0{,}1$; người chạy trích $\pi_v$ và kết luận chính sách chắc chắn tối ưu tuyệt đối.
- **Hình/ví dụ:** Phiếu kết quả gồm bảng $v$, phần dư và chính sách, với hai ô “đã chứng nhận” và “chưa chứng nhận”.
- **Nguồn:** NG1 tr.20,24,31–34,38; câu hỏi tổng hợp các kết quả của bài.
- **Kết nối:** Kết thúc bằng điều sinh viên phải kiểm tra khi nhận một chính sách từ thuật toán.
- **Ghi chú triển khai:** Hai phút lập luận và một phút chữa; đáp án nằm trong ghi chú, chưa hiện trên mặt slide ban đầu.
- **Thời lượng:** 3 phút.
- **Câu hỏi:** Kết luận nào về $v$ được bảo đảm; kết luận tối ưu tuyệt đối của $\pi_v$ đã có đủ căn cứ chưa; thuật toán nào cho chứng nhận chính sách ổn định khi đánh giá chính xác và giữ hòa?
- **Đáp án/gợi ý:** $\|v-v_*\|_\infty\le0{,}2$; phần dư dương chưa đủ chứng nhận chính sách tối ưu tuyệt đối, dù chính sách có thể đã tối ưu. Lặp chính sách chính xác, giữ hòa và bước cải thiện không đổi cho chứng nhận ổn định tối ưu.
- **Tiêu chí:** Nối được phần dư với sai số; không đồng nhất gần đúng giá trị với tối ưu tuyệt đối; nêu đủ điều kiện của PI.
