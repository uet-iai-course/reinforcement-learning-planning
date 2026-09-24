# Đề xuất sửa mạch, nội dung và bố cục Bài 04 — Giải MDP bằng quy hoạch động

**Trạng thái: Đề xuất chờ duyệt** — ngày 25-09-2026.
**Phạm vi rà soát:** bản bài giảng hiện hành gồm 45 slide, chia 7 phần (ID slide cũ `L04-S01` … `L04-S45`; trong tài liệu này gọi tắt S01…S45; các mã P01…P45 dưới đây chỉ là số thứ tự phương án đề xuất, chưa thay ID HTML).

Đề xuất giữ **45 slide chính, 120 phút**, dành cho sinh viên năm 3. Mạch mới dùng lại Bellman kỳ vọng và hệ tuyến tính của Bài 03, xây dựng bài toán quy hoạch tuyến tính (LP) và điều kiện Karush–Kuhn–Tucker (KKT), rồi suy ra hai cách tính: lặp chính sách (PI) chọn các ràng buộc đạt dấu bằng và đánh giá lại; lặp giá trị (VI) cập nhật bảng bằng toán tử Bellman tối ưu. Phần cuối giải thích hội tụ và cách kiểm tra kết quả. Ngoài phần trình chiếu, 30 phút dành cho chữa bài tập có sẵn; không bổ sung chương trình minh họa.

---

## 1. Tiên quyết KKT và phạm vi của phương án

Trong [Bài 03 hiện có](../../lecture-03-qua-trinh-quyet-dinh-markov.html), gồm 50 slide, và [PPTX nguồn](../../../RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx), chưa tìm thấy KKT, nhân tử Lagrange hoặc LP. Các kết quả có thể dùng trực tiếp là hàm giá trị, phương trình Bellman kỳ vọng và hệ tuyến tính đánh giá chính sách của quá trình quyết định Markov (MDP). Cần xác nhận tệp hoặc học phần chứa KKT mà thầy muốn nối vào; tài liệu này chưa coi KKT là kiến thức đã dạy trong bản Bài 03 đang có.

Phương án chính dưới đây đáp ứng yêu cầu đưa KKT vào tuyến chính, nhưng được trình bày như **cầu nối mới**: giả định sinh viên đã biết nhân tử Lagrange và KKT ở một học phần khác (ví dụ tối ưu hóa). Phân bổ 26 phút / 9 slide (Phần III, P11–P19) chỉ đủ để vận dụng KKT và giải thích ý nghĩa của nó trong ngữ cảnh MDP; thời lượng này **không đủ** để dạy từ đầu toàn bộ lý thuyết đối ngẫu lồi.

Nếu sinh viên chưa học KKT, cần duyệt thêm tài liệu đọc trước và phần hỗ trợ phù hợp; việc dùng 30 phút chữa bài cho mục này cũng cần được quyết định vì làm giảm thời gian chữa bài tập nguồn. Khi đó phải đánh giá lại tải học tập của phương án 120 phút. Bản đề xuất vẫn giữ KKT trong tuyến chính theo yêu cầu của thầy và giữ nguyên nội dung Bài 03 trong thời gian chờ duyệt.

---

## 2. Các điểm cần sửa trong bản hiện hành

Gọi slide cũ là S01…S45 với ID `L04-SNN`. Bảng dưới đây liệt kê 12 phát hiện, mỗi dòng gồm: mức độ | slide | bằng chứng | ảnh hưởng | sửa đề xuất.

| # | Mức độ | Slide | Bằng chứng | Ảnh hưởng | Sửa |
|---|--------|-------|-----------|-----------|-----|
| 1 | Cao | S03–S05 | Không chỉ rõ dùng kết quả nào của Bài 03; đổi mô hình robot H/L sang s0/s1 mà không có câu nối. Lưu ý: S03 **có** SVG đủ 4 cạnh với thưởng. | Sinh viên mất mốc liên kết với bài trước. | Thêm cầu nối tường minh tới L03R-05-03/06/07; S05 cho $v=(4,7)$ chưa tính đến S14, phải ghi rõ "bảng cho trước" hoặc dời sau phần đánh giá. |
| 2 | Cao | S06–S11 | Đi từ $Q_v$ đến định nghĩa bằng $\sup$ trên cả chính sách phụ thuộc lịch sử, $q_*$ đệ quy, hai toán tử trước khi xây dựng cách đánh giá chính sách (S13–S18): tạo vòng quay lại khái niệm, tải ký hiệu quá sớm. | Quá tải ký hiệu trước khi có nền. | $q_*$, $q_\pi$, $Q_v$ có ý nghĩa khác nhau ; ghi rõ quan hệ $Q_{v_\pi}=q_\pi$. Dời đệ quy $q_*$ sang phụ lục. |
| 3 | Trung bình | S07 | Bảng $Q_{v_{\pi_0}}$ lặp lại ở S12/S19/S20 với vai trò khác nhau nhưng không nêu "đầu ra mới". | Tính lặp, dễ nhầm là bảng mới. | Tính một lần, dùng lại cho cả hành động và ràng buộc. |
| 4 | Cao | S14, S24 | Thiếu câu nối trực tiếp tới hệ $(I-\gamma P_\pi)v=r_\pi$ từ L03R-06-07; S24 đặt công thức ma trận trong quy trình nhưng các slide trước chưa nhắc lại kết quả này trên mặt trang. | Đứt gãy suy diễn. | Thêm câu nối và nhắc lại hệ tuyến tính Bài 03 trước khi dùng ma trận. |
| 5 | Cao | S21 | Gộp ba bước $\pi_0=(a,a), v=(4,7)\to\pi_1=(a,b), v=(4,20)\to\pi_2=(b,b), v=(9,20)$; phép tính 20/9 nằm ẩn trong ghi chú diễn giả. | Sinh viên không thấy cơ chế PI. | Tách thành hai lượt riêng, mỗi lượt: đánh giá → $Q$ → đổi chính sách. |
| 6 | Trung bình | S23 | Chuỗi bất đẳng thức đúng nhưng bước dùng tính đơn điệu/giới hạn nằm trong ghi chú diễn giả; chưa thể hiện hai bước then chốt trên mặt slide. | Chứng minh không tự hoàn chỉnh trên mặt trang. | Đưa 2 bước then chốt lên mặt trang. S22 **đã có** quy tắc giữ hòa trên mặt trang — giữ lại. |
| 7 | Cao | S27 | Đổi mô hình 5 ô đồng thời với thuật toán mới; SVG mô tả lưới đã có; giải thích PI đắt ở bước đánh giá nằm trong ghi chú diễn giả. | Hai thay đổi cùng lúc. | Dẫn VI trên 2 trạng thái trước, sau đó dùng lưới để minh họa sự lan truyền giá trị. |
| 8 | Trung bình | S16, S31 | S16 trả bảng mới $w$, S31 trả bảng cũ $v$ đã kiểm: phân biệt hợp lệ nhưng gây rối và hệ số trong chặn sai số khác nhau. | Nhầm lẫn vai trò giá trị trả về. | Thống nhất trả "bảng đã đo bằng phần dư Bellman", ghi cụ thể trong giả mã. |
| 9 | Cao | S31, S39 | S31 dùng ngưỡng $\theta$ trước khi S39 giải thích quan hệ giữa ngưỡng phần dư và sai số giá trị. | Người học chưa biết ngưỡng dừng bảo đảm điều gì. | Đưa quy trình dừng đầy đủ sau chặn sai số; phần đầu VI chỉ ngân sách K lượt. |
| 10 | Cao | S35–S39 | Dồn chuẩn vô cùng, co, Banach, tối ưu cho mọi chính sách, chặn sai số vào một cụm; S37 hai cột chứa cả tồn tại duy nhất, chặn giá trị mọi chính sách, chính sách tham lam đạt chặn. | Quá tải chứng minh. | Đưa tối ưu và KKT về trước; co chỉ phải giải quyết hội tụ. |
| 11 | Trung bình | S38, S40 | S38 thêm số 64 độc lập; S40 CartPole 324 ngắt mạch chứng minh và điều kiện dừng: đúng nội dung nhưng nên dời phụ lục để có thời gian KKT. Số 64 không phải "dữ liệu sai" vì minh họa đã giải thích rõ. | Chưa tạo bước tiến cho lập luận đang theo dõi. | Chuyển 64 và CartPole sang phụ lục. |
| 12 | Trung bình | S33 | $O(n^3)$ chỉ là giải hệ; một vòng PI tổng phải $O(n^3+n^2m)$ với mô hình đặc; VI một quét $O(n^2m)$; một lượt đánh giá chính sách cố định với ma trận dựng sẵn $O(n^2)$; bộ nhớ mô hình $O(n^2m)$, $v$ là $O(n)$, $Q$ tùy chọn $O(nm)$. | Nguy cơ kết luận sai "PI luôn nhanh hơn VI". | Trình bày đầy đủ các thành phần chi phí; **không** kết luận PI luôn nhanh hơn VI. |

**Phát hiện về bố cục:** 17 trang khảo sát có 9 trang 2 cột, 4 trang hình; chữ thân bài khoảng 32,3 px, bảng 29,0 px, tiêu đề 48,4 px ở 1280×720. Ảnh kiểm định khớp phiên bản hiện hành không cho thấy lỗi tràn trang; vấn đề thực sự là **quan hệ suy diễn chưa hiện ra trên sơ đồ**. Cần thay các thẻ song song bằng chuỗi 3 bước hoặc thẻ cầu nối "dùng kết quả cũ", giữ chữ đủ lớn.

### Kết quả Bài 03 được tái sử dụng

Các kết quả được dùng lại: L03R-05-03 $G_t = R_{t+1} + \gamma G_{t+1}$; L03R-05-06 Bellman kỳ vọng; L03R-05-07 $q_\pi$; L03R-05-08 $v_\pi = \sum_a \pi(a|s)\, q_\pi(s,a)$; L03R-06-07 dạng ma trận. Robot với $\gamma = 0.5$: $v_H = 13/4$, $v_L = 7/4$; $q(L,\text{chờ}) = 15/8$, $q(L,\text{sạc}) = 13/8$. Dùng các số này ở P03 để nối bài; **không** nói đây là tối ưu; hành động thứ ba tại L có $q(L,\text{tìm}) = 6/8$. Mô hình hai trạng thái của Bài 04 giữ thưởng $2, -1, 5, 10$ và $\gamma = 0.5$ để các vai trò số dễ phân biệt và phép diễn LP 2D gọn. Mỗi lần chuyển mô hình phải chỉ rõ: giữ phương pháp, đổi dữ kiện.

---

## 3. Suy diễn toán học đề xuất cho tuyến chính

### 3.1 Giả thiết và ký hiệu

Tập trạng thái $\mathcal S$ hữu hạn; mỗi $\mathcal A(s)$ hữu hạn, khác rỗng; mô hình đã biết, bất biến theo thời gian; thưởng kỳ vọng hữu hạn; $0\le\gamma<1$. Đặt $n=|\mathcal S|$, $m=\max_s|\mathcal A(s)|$, $v\in\mathbb R^n$ và $c\in\mathbb R^n$ với mọi $c(s)>0$. Xác suất chuyển thỏa $P(s'\mid s,a)\ge0$ và $\sum_{s'}P(s'\mid s,a)=1$.

Đổi từ ký hiệu nguồn bằng hai định nghĩa rõ ràng:

$$P(s'\mid s,a)=\sum_{\tilde r}p(s',\tilde r\mid s,a),\qquad r(s,a)=\sum_{s',\tilde r}p(s',\tilde r\mid s,a)\tilde r.$$

Dùng $v_\pi,q_\pi$ theo Bài 03, tương ứng với $v^\pi,q^\pi$ của Bài 04 hiện hành. $Q_v$ nhận một bảng tiếp diễn bất kỳ; khi $v=v_\pi$ thì $Q_{v_\pi}=q_\pi$. Viết đủ đối số trước khi rút gọn:

$$ (T_\pi v)(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)Q_v(s,a),\qquad (T_*v)(s)=\max_{a\in\mathcal A(s)}Q_v(s,a).$$

Chỉ số $i$ đếm chính sách; $k$ đếm lượt cập nhật giá trị. Với ví dụ lưới, trạng thái kết thúc được biểu diễn bằng trạng thái hấp thụ có thưởng 0; khởi tạo và giữ giá trị tại đó bằng 0. Ví dụ luồng đối ngẫu chỉ dùng mô hình hai trạng thái.

### 3.2 LP và tính chặn trên

$$Q_v(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)v(s'),\qquad \Delta_v(s,a)=v(s)-Q_v(s,a).$$

Độ dư ràng buộc là $\Delta_v(s,a)$; trong các bảng dưới đây viết gọn $\Delta$. Bài toán tối ưu có $n$ biến và $\sum_s|\mathcal A(s)|$ ràng buộc:

$$\min_{v\in\mathbb R^n}c^\top v\qquad\text{với }\Delta_v(s,a)\ge0\quad\forall s,a.$$

LP **cực tiểu hóa một chặn trên** của giá trị chính sách. Mọi bảng khả thi thỏa $v\ge T_\pi v$; khai triển bất đẳng thức theo từng bước cho:

$$v(s)\ge\mathbb E_\pi\!\left[\sum_{t=0}^{N-1}\gamma^tR_{t+1}+\gamma^Nv(S_N)\mid S_0=s\right].$$

Vì $v$ bị chặn trên tập trạng thái hữu hạn và $\gamma<1$, số hạng cuối tiến về 0. Do đó $v\ge v_\pi$. Lập luận lấy kỳ vọng có điều kiện cũng áp dụng cho chính sách phụ thuộc lịch sử; đưa ý chính lên slide, khai triển đầy đủ vào ghi chú. Như vậy việc lập LP chưa cần giả sử trước phương trình Bellman tối ưu.

Đặt $R_{\max}=\max_{s,a}|r(s,a)|$. Bảng hằng $v=M\mathbf1$ với $M>R_{\max}/(1-\gamma)$ thỏa chặt mọi ràng buộc. LP khả thi, bị chặn dưới bởi $c^\top v_\pi$ của một chính sách cố định và đạt cực tiểu. Điều kiện Slater cho phép dùng KKT như điều kiện cần; tính lồi và các ràng buộc affine cho tính đủ. Cách lập LP dùng [ghi chú Stanford MS&E235, tr. 1–3](https://web.stanford.edu/class/msande235a/files/lectures/lecture07.pdf); điều kiện áp dụng KKT theo [Boyd–Vandenberghe, §5.5.3](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).

### 3.3 KKT và dòng chảy

$$L = c^\top v + \sum_{s,a} \lambda(s,a)\,\big[\,Q_v(s,a) - v(s)\,\big], \qquad \lambda \ge 0.$$

Đạo hàm theo $v(j)$ bằng 0 cho điều kiện dừng:

$$c(j) + \gamma \sum_{s,a} \lambda(s,a)\, P(j\mid s,a) - \sum_a \lambda(j,a) = 0.$$

Bốn điều kiện KKT gồm: khả thi gốc $\Delta_v(s,a)\ge0$; nhân tử không âm $\lambda(s,a)\ge0$; đạo hàm theo mọi $v(j)$ bằng 0; bù trừ bổ sung $\lambda(s,a)\Delta_v(s,a)=0$ với **từng** cặp $(s,a)$.

Đặt $d(j)=\sum_a\lambda(j,a)$. Điều kiện dừng trở thành cân bằng luồng:

$$d(j)=c(j)+\gamma\sum_{s,a}\lambda(s,a)P(j\mid s,a)>0.$$

Mỗi trạng thái có ít nhất một hành động mang nhân tử dương, nên bù trừ bổ sung buộc ràng buộc tương ứng đạt dấu bằng. Kết hợp với mọi $\Delta_v\ge0$:

$$\exists a:\ v(j)=Q_v(j,a),\qquad\forall a:\ v(j)\ge Q_v(j,a)\quad\Longrightarrow\quad v=T_*v.$$

$\lambda$ biểu diễn luồng chiết khấu, có thể lớn hơn 1. Chuẩn hóa theo trạng thái cho $\pi(a\mid s)=\lambda(s,a)/d(s)$; cũng có thể chọn một hành động đạt dấu bằng ở mỗi trạng thái để có chính sách xác định. Khi đó $v=T_\pi v$, nên hệ Bellman của Bài 03 cho $v=v_\pi$. Đồng thời $v$ chặn giá trị mọi chính sách: $v=v_*$. Đây là bước suy ra Bellman tối ưu từ KKT, theo [Ying–Zhu, §2.2, tr. 5](https://arxiv.org/pdf/2012.09417).

Bài toán đối ngẫu cực đại hóa $\sum_{s,a}\lambda(s,a)r(s,a)$ dưới điều kiện cân bằng luồng và $\lambda\ge0$. Với $v$ khả thi gốc và $\lambda$ khả thi đối ngẫu, phép thế cân bằng luồng cho:

$$c^\top v-\sum_{s,a}\lambda(s,a)r(s,a)=\sum_{s,a}\lambda(s,a)\Delta_v(s,a)\ge0.$$

Hai giá trị mục tiêu bằng nhau cùng với tính khả thi tạo chứng nhận tối ưu. Suy diễn đối ngẫu đầy đủ nằm trong ghi chú P15; P42 dùng trực tiếp đẳng thức này để kiểm kết quả. KKT xác định điều kiện nghiệm; hội tụ của PI và VI cần lập luận riêng ở mục 3.5–3.7.

### 3.4 Ví dụ số và chứng nhận tối ưu

$c=(1,1)$ là trọng số dương, tương ứng lượng luồng được đưa vào mỗi trạng thái; tổng trọng số ở đây bằng 2. Đặt $x=v(s_0)$, $y=v(s_1)$, tránh nhầm $v_0$ với bảng khởi tạo của thuật toán. Ràng buộc:

$$x \ge 2 + 0.5x,\quad x \ge -1 + 0.5y,\quad y \ge 5 + 0.5x,\quad y \ge 10 + 0.5y.$$

Vùng khả thi là giao bốn nửa mặt phẳng, không bị chặn. Từ $y\ge20$ và $x\ge-1+0.5y$ suy ra $x\ge9$. Điểm $(9,20)$ thỏa cả bốn ràng buộc, nên cực tiểu của $x+y$ bằng 29. Theo thứ tự hàng $s_0,s_1$, cột $a,b$:

$$Q = \begin{pmatrix} 6.5 & 9 \\ 9.5 & 20 \end{pmatrix},\quad \Delta = \begin{pmatrix} 2.5 & 0 \\ 10.5 & 0 \end{pmatrix},\quad \lambda = \begin{pmatrix} 0 & 1 \\ 0 & 3 \end{pmatrix}.$$

Hai phương trình luồng là $1=1+0.5\cdot0$ tại $s_0$ và $3=1+0.5(1+3)$ tại $s_1$. Mọi độ dư đều không âm; nhân tử dương chỉ đặt ở hai độ dư bằng 0. Giá trị đối ngẫu là $1\cdot(-1)+3\cdot10=29$, bằng mục tiêu gốc $9+20=29$. Chính sách là $(b,b)$; $\lambda(s_1,b)=3$ là luồng chiết khấu. Tổng luồng $4=\sum_sc(s)/(1-\gamma)$.

### 3.5 Xây dựng lặp chính sách từ các ràng buộc đạt dấu bằng

Một chính sách xác định $\pi$ chọn một phương trình đạt dấu bằng tại mỗi trạng thái:

$$v(s)=Q_v(s,\pi(s))\quad\Longleftrightarrow\quad (I-\gamma P_\pi)v=r_\pi.$$

Đây chính là **hệ đánh giá chính sách đã học ở Bài 03**, cho nghiệm $v_\pi$. Để diễn giải bằng KKT, xây dựng thêm:

$$d_\pi=(I-\gamma P_\pi^\top)^{-1}c,\qquad\lambda_\pi(s,a)=d_\pi(s)\pi(a\mid s).$$

Các nhân tử này thỏa cân bằng luồng, không âm và bù trừ bổ sung. Tuy nhiên, ràng buộc của hành động chưa chọn có thể có độ dư âm: ứng viên chưa thỏa toàn bộ KKT. PI chọn lại hành động đạt $\max_aQ_{v_\pi}(s,a)$ rồi giải hệ đánh giá mới. Thuật toán thực thi chỉ cần $v_\pi$ và bảng $Q$; không cần tính $d_\pi,\lambda_\pi$ ở mỗi vòng. Các đại lượng đối ngẫu dùng để giải thích và chứng nhận.

Đây là cách xây dựng PI từ việc chọn các phương trình trong hệ KKT, không phải một thuật toán tổng quát luôn giữ tính khả thi gốc. Các giá trị ứng viên không giảm theo từng trạng thái và tăng nghiêm ngặt ở ít nhất một trạng thái khi chính sách đổi; LP lại cực tiểu hóa trên miền các chặn trên. Vì vậy hình minh họa phải đặt các ứng viên chưa tối ưu **ngoài miền khả thi**, rồi tiến tới $(9,20)$.

Bảng đã tính lại bằng phân số chính xác. Thứ tự các phần tử trong $\Delta$ và $\lambda$ là $(s_0,a),(s_0,b),(s_1,a),(s_1,b)$:

| Chính sách | $v$ | $\Delta$ (theo hàng) | $d$ | $\lambda$ | Mục tiêu đại số |
|---|---|---|---|---|---|
| $\pi_0 = (a,a)$ | $(4,7)$ | $(0,\ 1.5,\ 0,\ -6.5)$ | $(3,1)$ | $(3,0,\ 1,0)$ | 11 |
| $\pi_1 = (a,b)$ | $(4,20)$ | $(0,\ -5,\ 13,\ 0)$ | $(2,2)$ | $(2,0,\ 0,2)$ | 24 |
| $\pi_2 = (b,b)$ | $(9,20)$ | $(2.5,\ 0,\ 10.5,\ 0)$ | $(1,3)$ | $(0,1,\ 0,3)$ | 29 |

Tại $\pi_1$, $Q_{v_{\pi_1}}(s_1,a)=5+0.5\cdot4=7$ và $\Delta(s_1,a)=20-7=13$. Số $9.5$ ở bảng trước dùng phần tiếp diễn $v_*$, không dùng $v_{\pi_1}$. Hai biểu thức mục tiêu gốc và đối ngẫu lần lượt cùng bằng 11, 24, 29; **đẳng thức mục tiêu chưa chứng nhận tối ưu khi $v$ chưa khả thi**. P45 dùng chính điểm này để kiểm tra kết quả cuối buổi.

**Chứng minh PI:** $T_{\pi'} v_\pi \ge v_\pi$ và khai triển nhờ tính đơn điệu suy ra $v_{\pi'} \ge v_\pi$; ổn định tại mọi trạng thái $\Rightarrow$ Bellman $\Rightarrow$ KKT. Đánh giá chính xác với chính sách tất định hữu hạn; quy tắc giữ hòa bảo đảm cải thiện chặt ở **một số** trạng thái đã đổi và kết thúc hữu hạn. Chỉ cần tăng nghiêm ngặt ở ít nhất một trạng thái khi chính sách đổi; không yêu cầu tăng ở mọi trạng thái.

### 3.6 Từ điều kiện Bellman đến lặp giá trị

KKT $\Rightarrow v = T_* v$; chọn lặp điểm bất động $v_{k+1} = T_* v_k$. Lựa chọn này đến từ **thiết kế thuật toán**, không phải từ lặp điều kiện đạo hàm bằng 0 của KKT. Không duy trì $\lambda$; các $v$ trung gian không nhất thiết khả thi. VI hai trạng thái với $v_0 = 0$: $v_1 = (2,10) \to v_2 = (4,15) \to v_3 = (6.5, 17.5)$; P28 chỉ hiện 2 quét đầu, phân biệt với đánh giá chính sách $(2,5), (3,6)$.

**Chứng minh co:** phần thưởng triệt tiêu, bất đẳng thức max, trung bình với các trọng số xác suất $\Rightarrow \|T_* u - T_* v\|_\infty \le \gamma \|u - v\|_\infty$; tính đầy đủ trên $\mathbb{R}^n$ cho điểm bất động duy nhất và hội tụ. KKT đã xác định tính tối ưu rồi; **không** chứng minh lại toàn bộ phần lịch sử ở đây.

### 3.7 Phần dư và quy tắc dừng

Đặt $\rho(v)=\lVert T_*v-v\rVert_\infty$ và $e=\lVert v-v_*\rVert_\infty$. Dùng bất đẳng thức tam giác và tính co:

$$e\le\rho(v)+\gamma e\quad\Longrightarrow\quad e\le\frac{\rho(v)}{1-\gamma}.$$

Với đánh giá chính sách, thay $T_*$ bằng $T_\pi$ và $v_*$ bằng $v_\pi$ để có cùng chặn cho bảng **đã kiểm**. $\Delta_v(s,a)$ là độ dư của từng ràng buộc LP; $\rho(v)$ là một số đo phần dư Bellman của cả bảng, không phải cùng đại lượng.

Quy trình hoàn chỉnh nhận mô hình, bảng khởi tạo $v$, mức sai số $\varepsilon_v>0$ và ngân sách $K\ge1$ lần tính Bellman; đặt $\theta=(1-\gamma)\varepsilon_v$. Với $T=T_*$ hoặc $T=T_\pi$, mỗi vòng thực hiện:

1. Tính đồng bộ $w=Tv$ và $\rho=\max_s|w(s)-v(s)|$ từ cùng bảng $v$.
2. Nếu $\rho\le\theta$, trả $v,\rho$ và trạng thái “đạt ngưỡng”.
3. Nếu đây là lần tính thứ $K$, trả $v,\rho$ và trạng thái “hết ngân sách”; không khẳng định đã đạt ngưỡng.
4. Nếu còn tiếp tục, gán $v\leftarrow w$.

Với VI, trả thêm $\pi_v(s)\in\arg\max_aQ_v(s,a)$ tính từ **chính bảng $v$ trả về**; dùng quy tắc phá hòa cố định. $K$ đếm số phép tính $Tv$, gồm phép tính cuối phục vụ kiểm tra, nên có tối đa $K-1$ lần gán $v\leftarrow w$. P09 và P29 giới thiệu trước phiên bản chỉ dừng theo ngân sách, vẫn theo quy ước trả bảng đã đo; P38–P39 bổ sung nhánh chứng nhận sai số.

Bản hiện hành trả bảng mới $w$ khi đánh giá chính sách và bảng cũ đã kiểm $v$ khi lặp giá trị. Việc thống nhất trên làm chặn áp dụng trực tiếp lên bảng trả về. Phần dư dương có thể chứng nhận giá trị gần đúng nhưng tự nó chưa chứng nhận chính sách tối ưu tuyệt đối. Trường hợp $\gamma=1$ cần giả thiết hoặc lập luận khác.

Với $\varepsilon_v=0.2$, $\gamma=0.5$, ngưỡng là $\theta=0.1$. Nếu $\rho=0.15$, chặn sai số là $0.3$, chưa đủ để dừng theo ngưỡng. Nếu $\rho=0.1$, chặn bằng $0.2$ và đạt mức yêu cầu.

---

## 4. Dàn bài 45 slide, tổng thời lượng 120 phút

Mỗi phần kết thúc bằng một slide kiểm tra. Thời lượng dưới đây đã gồm suy nghĩ, trả lời và chữa ngắn trên lớp; bốn chủ đề chuyển sang phụ lục không tính vào 45 slide chính hoặc 120 phút.

| Phần và chức năng | Kiến thức đầu vào | Kết quả tạo ra và câu nối sang phần sau |
|---|---|---|
| I. Mở đầu, 10 phút | Bellman và ví dụ robot Bài 03 | Nhận ra tính được giá trị một chính sách chưa giải quyết việc chọn chính sách; cần đánh giá các ứng viên trên mô hình mới |
| II. Đánh giá chính sách, 13 phút | Mô hình và chính sách cố định | Có $v_{\pi_0}=(4,7)$ và cách giải hệ/lặp; tiếp theo kiểm tra hành động chưa được chính sách chọn |
| III. Điều kiện tối ưu, 26 phút | Bảng giá trị, nhìn trước một bước, tiên quyết KKT | Lập được LP, suy ra Bellman tối ưu và kiểm một chứng nhận; tiếp theo tìm nghiệm bằng cấu trúc của các ràng buộc |
| IV. Lặp chính sách, 20 phút | Hệ đánh giá và điều kiện KKT | Thực hiện được đánh giá–cải thiện, giải thích dừng khi ổn định; bước đánh giá đầy đủ tạo nhu cầu cách cập nhật nhẹ hơn |
| V. Lặp giá trị, 19 phút | Phương trình Bellman tối ưu | Thực hiện một lượt cập nhật và trích chính sách; còn cần biết các lượt lặp có hội tụ và khi nào dừng |
| VI. Hội tụ và sai số, 20 phút | Toán tử và các bảng trước/sau cập nhật | Dùng phần dư để bảo đảm độ chính xác của đúng bảng trả về; tiếp theo chọn phương pháp và kiểm kết quả hoàn chỉnh |
| VII. Tổng hợp, 12 phút | Hai thuật toán và hai loại chứng nhận | Giải quyết bài toán mở đầu, phân biệt tối ưu chính xác với bảo đảm sai số gần đúng, giao bài tập vận dụng |

Chu trình học tập của các cụm trọng tâm:

- **Đánh giá chính sách:** bài toán, trực giác tích lũy thưởng và ví dụ giải hệ gộp trong P06 → dạng ma trận và phép lặp P07–P09 → thực hiện lượt kế tiếp P10. Phép phân rã Bellman đã có ở Bài 03 nên chỉ nhắc bước cần dùng.
- **LP/KKT:** hành động có lợi hơn ở P11 tạo nhu cầu kiểm tối ưu → ví dụ bốn ràng buộc P12 và hình học P13 → Lagrange, cân bằng luồng, bù trừ bổ sung P14–P17 → chứng nhận trên cùng mô hình P18 → kiểm tra P19. Các đại lượng $v,Q_v$ của P11 được giữ khi chuyển sang $\Delta_v$.
- **PI:** hạn chế của việc giải LP tổng quát và ý tưởng chọn một phương trình mỗi trạng thái P20 → ví dụ P21–P23 → chứng minh và thuật toán đầy đủ P24–P25 → tính bước cải thiện và kiểm hiểu ở P26.
- **VI:** chi phí đánh giá trong PI và ý tưởng nhìn trước một bước P27 → tính tay trên cùng MDP P28 → quy trình P29 → ứng dụng lan truyền trên lưới P30–P32 → kiểm tra P33.
- **Hội tụ và dừng:** nhu cầu kiểm độ chính xác từ P33 → khoảng cách hai bảng và ví dụ co P34 → chứng minh P35–P37 → dùng chặn để hoàn thiện thuật toán P38–P39 → kiểm tra P40.

**Phần I — Mở đầu (P01–P05, 10 phút, mỗi slide 2 phút)**

| Slide | Tiêu đề | Nội dung chính / lý do / nối | Bố cục | Phút |
|---|---|---|---|---|
| 01 | Giải MDP bằng quy hoạch động | Cần chính sách tối ưu, không chỉ giá trị | Tiêu đề và mục tiêu trung tâm | 2 |
| 02 | Nội dung và mục tiêu | Tính giá trị; suy ra điều kiện tối ưu; thực hiện PI/VI; kiểm tra kết quả | danh sách | 2 |
| 03 | Cầu nối Bài 03 | Dùng lại giá trị Bellman robot và so sánh $q$ | cầu nối (1) | 2 |
| 04 | Mô hình 2 trạng thái mới | Chuyển một lần từ robot sang mô hình hai trạng thái; nhiệm vụ: chọn chính sách **và** chứng nhận | 2 cột | 2 |
| 05 | Câu hỏi: đọc mô hình và quyết định | Với mô hình P04, nêu thưởng và trạng thái đến khi chọn $b$ tại $s_0$; việc $2>-1$ đã đủ để chọn chính sách tối ưu chưa? | Mô hình P04 với hai cạnh từ $s_0$ được nhấn | 2 |

**Phần II — Đánh giá chính sách (P06–P10, 13 phút: 3,3,3,2,2)**

| Slide | Tiêu đề | Nội dung | Bố cục | Phút |
|---|---|---|---|---|
| 06 | Giá trị của chính sách cố định | $x = 2 + 0.5x$, $y = 5 + 0.5x \Rightarrow (4,7)$ | phương trình | 3 |
| 07 | Dạng ma trận | Từ Bài 03; nói ngắn về khả nghịch | ma trận | 3 |
| 08 | Đánh giá bằng các lượt quét | Các lượt quét đánh giá và $T_\pi$ | bảng | 3 |
| 09 | Đánh giá với ngân sách cố định | Ngân sách $K$ lần tính Bellman, trả bảng đã đo theo mục 3.7; quan sát thay đổi lớn nhất, chưa gọi đó là sai số | Quy trình với hai bảng cũ–mới | 2 |
| 10 | Câu hỏi: | Lượt tiếp theo từ $(3,6) \to (3.5, 6.5)$; vì sao không có max | câu hỏi kiểm tra | 2 |

**Phần III — LP và KKT (P11–P19, 26 phút: 3 phút cho P11–P18, 2 phút P19)**

| Slide | Tiêu đề | Nội dung | Bố cục | Phút |
|---|---|---|---|---|
| 11 | Điểm hành động từ bảng giá trị | So sánh một hành động với chính sách hiện tại → động lực "chứng nhận tối ưu" | bảng | 3 |
| 12 | Bất đẳng thức Bellman | Dựng từ $Q_v$ | danh sách | 3 |
| 13 | Hình học LP | min = chặn trên nhỏ nhất | miền khả thi (2) | 3 |
| 14 | Lagrangian | Tổng quan 4 điều kiện KKT + giả thiết | công thức trung tâm (4) | 3 |
| 15 | Điều kiện dừng và cân bằng luồng | Đạo hàm $L$ → dòng chảy | sơ đồ dòng (4) | 3 |
| 16 | Bù trừ bổ sung | Ví dụ ứng viên $(9,20)$ — trình bày ứng viên, **chưa** tuyên bố tối ưu | bảng | 3 |
| 17 | Từ KKT đến Bellman tối ưu | → Bellman tối ưu và chính sách tham lam | chuỗi | 3 |
| 18 | Chứng nhận KKT đầy đủ $(9,20)$ | Kiểm bốn điều kiện với hai nhân tử khác 0 là 1 và 3; tính hai mục tiêu $9+20=1(-1)+3(10)=29$ | Bảng độ dư/nhân tử và một dòng mục tiêu; phép suy diễn tổng quát trong ghi chú | 3 |
| 19 | Câu hỏi: đọc nhân tử KKT | Từ $d(s_1)=3$, $\lambda(s_1,a)=0$, $\lambda(s_1,b)=3$, tính chính sách tại $s_1$ và giải thích số 3 thuộc đại lượng nào | Câu hỏi kèm sơ đồ luồng P15 thu gọn | 2 |

**Phần IV — Lặp chính sách (P20–P26, 20 phút: 3 phút P20–P25, 2 phút P26)**

| Slide | Tiêu đề | Nội dung | Bố cục | Phút |
|---|---|---|---|---|
| 20 | Bài toán PI | Chọn các phương trình đạt dấu bằng theo $\pi$, tái dùng ma trận | 3 bước (3) | 3 |
| 21 | Cải thiện chính sách đầu | Từ bảng $Q_{v_{\pi_0}}$, chọn $\pi_1$; $\Delta(s_1,b)=-6.5$ chỉ ra ràng buộc chưa thỏa | Bảng và điểm $(4,7)$ có nhãn “chưa khả thi” | 3 |
| 22 | Giải $\pi_1$ | $y=20$, $x=4$; rồi $Q_{v_{\pi_1}}(s_0,b)=9$ chọn $\pi_2$ | Ba bước; điểm $(4,20)$ có nhãn “chưa khả thi” do độ dư $-5$ | 3 |
| 23 | Giải $\pi_2$ | $x=9$, $y=20$; kiểm mọi độ dư không âm | 3 bước | 3 |
| 24 | Chứng minh cải thiện 2 bước | + chặt ở một số trạng thái / giữ hòa | chuỗi chứng minh (6) | 3 |
| 25 | Thuật toán PI đầy đủ | Đầu vào/đầu ra; đánh giá chính xác; tham lam; giữ hòa; ổn định; trần ngân sách chưa chứng nhận | quy trình | 3 |
| 26 | Câu hỏi: | Cho $v_{\pi_1}$: tính $Q_{0a}=4$, $Q_{0b}=9$; vì sao 13.5 ≠ 20 như đã nói | câu hỏi kiểm tra | 2 |

**Phần V — Lặp giá trị (P27–P33, 19 phút: 3 phút P27–P31, 2 phút P32–P33)**

| Slide | Tiêu đề | Nội dung | Bố cục | Phút |
|---|---|---|---|---|
| 27 | Chi phí đánh giá chính sách | → KKT đã khử $\lambda$ → điểm bất động: VI | chuyển tiếp | 3 |
| 28 | VI bằng tay, 2 trạng thái | $0 \to (2,10) \to (4,15)$ | bảng cũ → bảng mới (5) | 3 |
| 29 | Cập nhật và trích chính sách | Ngân sách $K$ lần tính Bellman; trả bảng đã đo và chính sách tham lam từ cùng bảng, chưa có bảo đảm sai số | Quy trình như P09, thay trung bình theo chính sách bằng cực đại | 3 |
| 30 | Mô hình lưới 5 ô | Hành động trái/phải; kết thúc/thưởng −1/24; $\gamma=0.5$ | lưới | 3 |
| 31 | Hai quét đầu | Giá trị trạng thái, mũi tên giữa cũ/mới | lưới + mũi tên | 3 |
| 32 | Quét 3–4 | Lan truyền và kiểm tra điểm bất động; **không** phải hội tụ hữu hạn tổng quát | lưới | 2 |
| 33 | Câu hỏi: lượt cập nhật tiếp theo | Cho $v_3=(-1.75,4.5,11,24,0)$ theo thứ tự $c_1$ đến $c_5$; tính $v_4(c_1)$ và độ thay đổi lớn nhất, các ô khác đã ổn định. Nhắc độ thay đổi chưa phải sai số | Lưới cũ và một ô cần tính; chưa dùng ký hiệu phần dư mới | 2 |

**Phần VI — Hội tụ và dừng (P34–P40, 20 phút: 3 phút P34–P39, 2 phút P40)**

| Slide | Tiêu đề | Nội dung | Bố cục | Phút |
|---|---|---|---|---|
| 34 | Khoảng cách / chuẩn $\infty$ | Dùng lại $u=(4,7)$, $z=(8,9)$, ghi rõ là so sánh tùy ý; 4 trước / 2 sau; nối với "thay đổi lớn nhất" | chuỗi | 3 |
| 35 | Chứng minh co | Bước max và kỳ vọng | chuỗi chứng minh (6) | 3 |
| 36 | Hội tụ của lặp giá trị | Nêu giới hạn khi $\gamma=1$ (không dồn 3 định lý mới vào một thẻ) | chuỗi | 3 |
| 37 | Chặn sai số từ phần dư | Suy diễn và $\theta = (1-\gamma)\varepsilon$ | chuỗi | 3 |
| 38 | Thuật toán VI dừng đầy đủ | Trả về $v$ đã kiểm, $\pi_v$, phần dư của chính bảng đó và trạng thái dừng | quy trình 4 bước + hộp chứng nhận (6) | 3 |
| 39 | Chứng nhận đánh giá chính sách | So sánh 2 quy trình; giữ $v$ đã kiểm; **không** suy chính sách tối ưu từ xấp xỉ | 2 cột so sánh | 3 |
| 40 | Câu hỏi: | $\rho = 0.15$, $\gamma = 0.5 \Rightarrow$ chặn $0.3$, không chứng nhận $0.2$; $\gamma=1$ phá vỡ | câu hỏi kiểm tra | 2 |

**Phần VII — Tổng hợp (P41–P45, 12 phút: 2,3,2,3,2)**

| Slide | Tiêu đề | Nội dung | Bố cục | Phút |
|---|---|---|---|---|
| 41 | Sơ đồ khái niệm | Bellman Bài 03 → LP/KKT → PI và VI → chứng nhận | sơ đồ | 2 |
| 42 | Kiểm lại kết quả lập kế hoạch | Thu hồi chứng nhận P18: chọn đúng các kiểm tra cho $(9,20)$ và mục tiêu $29=29$; giải thích điều kiện nào thiếu nếu chỉ so hai mục tiêu | Bảng kiểm để sinh viên hoàn thiện; đáp án và vai trò $c>0$ trong ghi chú | 3 |
| 43 | So sánh thuật toán | Đầu vào/đầu ra/chi phí, với mô hình đặc; chú thích trường hợp mô hình thưa | bảng | 2 |
| 44 | Bài tập về nhà | hw3 B3/6/7/9 + nguồn; nối sang Bài 05: học từ mẫu khi chưa biết mô hình; kế hoạch 30 phút chữa bài **ngoài** 120 phút; không thêm bài tập LP bắt buộc khi chưa có nguồn được duyệt | danh sách | 3 |
| 45 | Câu hỏi: kiểm chứng nhận của một ứng viên | Cho ứng viên $\hat v=v_{\pi_0}=(4,7)$ và $\hat\lambda=\begin{pmatrix}3&0\\1&0\end{pmatrix}$, hàng $s_0,s_1$, cột $a,b$. Hai mục tiêu cùng bằng 11; xác định điều kiện tối ưu chưa thỏa | Bảng ứng viên mang nhãn $\pi_0$; đối chiếu riêng với nghiệm tối ưu P42 | 2 |

### Câu hỏi và đáp án cần chuẩn bị

Đáp án đầy đủ đặt trong ghi chú diễn giả. Mặt slide hiện đề trước, chỉ mở kết quả sau thời gian trả lời nếu dùng hiệu ứng xuất hiện.

| Slide | Năng lực kiểm tra | Đáp án và lỗi cần phân biệt |
|---|---|---|
| P05 | Phân biệt thưởng trước mắt và giá trị dài hạn | Chọn $b$ tại $s_0$ nhận thưởng $-1$, đến $s_1$. So sánh $2>-1$ chỉ xét thưởng tức thời; còn phải tính phần tiếp diễn. Câu hỏi dùng mô hình vừa giới thiệu, không quay lại robot sau khi đã đổi mô hình |
| P10 | Thực hiện đánh giá đồng bộ | $(3.5,6.5)$; cả hai phép tính đọc giá trị cũ tại $s_0$. Không lấy cực đại vì hành động do $\pi_0$ ấn định |
| P19 | Hiểu nhân tử và bước KKT → Bellman | $\pi(b\mid s_1)=3/3=1$, $\pi(a\mid s_1)=0$. Số 3 là luồng chiết khấu, không phải xác suất. Câu hỏi sâu về vai trò $c(s)>0$ để ở ghi chú P17/P42 |
| P26 | Phân biệt cải thiện và đánh giá lại | $Q_{v_{\pi_1}}(s_0,a)=4$, $Q_{v_{\pi_1}}(s_0,b)=9$ nên đổi sang $b$. $13.5=q_{\pi_0}(s_1,b)$ dùng chính sách cũ từ bước sau; $20=v_{\pi_1}(s_1)$ dùng chính sách mới về sau |
| P33 | Cập nhật từ đúng bảng cũ | Đi phải cho $-1+0.5\cdot4.5=1.25$; đi trái tự lặp cho $-1+0.5(-1.75)=-1.875$. Chọn $1.25$; độ thay đổi lớn nhất là $1.25-(-1.75)=3$ |
| P40 | Dùng chặn sai số đúng chiều | Sai số không quá $0.3$; chưa bảo đảm sai số không quá $0.2$, cũng không suy ra sai số thực lớn hơn $0.2$. Khi $\gamma=1$, chặn chia cho $1-\gamma$ và tính co nghiêm ngặt không còn dùng được |
| P45 | Kiểm đủ điều kiện chứng nhận tối ưu | $\Delta_{\hat v}(s_1,b)=7-(10+0.5\cdot7)=-6.5<0$. Ứng viên $\hat v$ không khả thi gốc; $4+7=3\cdot2+1\cdot5=11$ chưa chứng nhận tối ưu. $\hat\lambda$ gắn với $\pi_0$, khác các nhân tử của nghiệm tối ưu P18/P42 |

### Đối chiếu 45 slide hiện hành với phương án mới

| S cũ | Quyết định | Đích mới | Lý do ngắn |
|---|---|---|---|
| S01 | giữ | P01 | Mở đầu |
| S02 | giữ | P02 | Nội dung |
| S03 | sửa | P04 | Cần cầu nối Bài 03 |
| S04 | sửa | P04/P11 | Chuyển lời giải giá trị 9 sang sau quá trình xây dựng; mở bài giữ xung đột thưởng trước mắt–giá trị dài hạn |
| S05 | sửa | P05 | Thay bằng câu hỏi Bài 03 |
| S06 | gộp | P11 | Dùng sơ đồ hành động đầu–tiếp diễn để giải thích bảng $Q_v$ |
| S07 | gộp | P11 | Tính $Q_{v_{\pi_0}}$ một lần |
| S08 | sửa | P17 và ghi chú | Định nghĩa tối ưu đi cùng chứng minh đạt được; chi tiết lớp chính sách nằm trong ghi chú |
| S09 | sửa | P17 | Phương trình Bellman tối ưu được suy ra từ KKT |
| S10 | chuyển phụ lục | Phương trình $q_*$ | Tuyến chính dùng $Q_v$ và $v_*$ |
| S11 | tách | P08/P17 | Hai vai trò |
| S12 | sửa | P19 | Thay câu hỏi kiểm tra chứng nhận |
| S13 | giữ | P06 | đánh giá chính sách |
| S14 | sửa | P06/P07 | Thêm nối hệ tuyến tính |
| S15 | giữ | P08 | Quét |
| S16 | sửa | P09/P39 | Thống nhất giá trị trả về |
| S17 | chuyển phụ lục | Cập nhật đồng bộ và tại chỗ | Giữ một lịch đồng bộ trong tuyến chính |
| S18 | giữ | P10 | Câu hỏi: đánh giá chính sách |
| S19 | sửa | P11/P21 | Tách |
| S20 | giữ | P21 | Chọn $\pi_1$ |
| S21 | tách | P22/P23 | Hai lượt PI |
| S22 | giữ | P25 | Quy tắc giữ hòa đã có |
| S23 | sửa | P24 | Đưa 2 bước chứng minh lên mặt trang |
| S24 | sửa | P25 | Nối ma trận |
| S25 | sửa | P24/P25 | Gộp |
| S26 | giữ | P26 | Câu hỏi: PI |
| S27 | sửa | P30 | Tách đổi mô hình khỏi thuật toán |
| S28 | giữ | P31 | Quét lưới |
| S29 | sửa | P31/P32 | Gộp |
| S30 | sửa | P27/P29 | Dẫn VI hai trạng thái trước |
| S31 | sửa | P29/P38 | Dời quy trình dừng sau chặn sai số |
| S32 | giữ | P29 | Cập nhật VI |
| S33 | sửa | P43 | Bảng chi phí đầy đủ |
| S34 | giữ | P33 | Câu hỏi: lưới |
| S35 | giữ | P34 | Chuẩn $\infty$ |
| S36 | giữ | P35 | Chứng minh co |
| S37 | sửa | P17/P36 | Tách tối ưu khỏi co |
| S38 | chuyển phụ lục | phụ lục đồ thị 64 (chặn hình học nói ngắn ở P36) | Thời gian KKT |
| S39 | sửa | P37–P39 | Phần dư |
| S40 | chuyển phụ lục | phụ lục CartPole | Thời gian KKT |
| S41 | giữ | P40 | Câu hỏi: phần dư |
| S42 | gộp | P43 | So sánh đầu vào, đầu ra, chi phí và điều kiện áp dụng |
| S43 | tách | P18/P42 | Thêm chứng nhận KKT và kiểm mục tiêu gốc–đối ngẫu cho nghiệm hiện có |
| S44 | giữ | P44 | Bài tập |
| S45 | sửa | P45 | Thay câu hỏi kiểm tra chứng nhận KKT chính xác; hiểu lầm phần dư cũ chuyển P39 |

Nội dung bổ sung: P03 tái sử dụng trực tiếp Bài 03; P12–P16 thêm LP/KKT; P17–P20 và P42 thêm cách suy ra hoặc kiểm chứng bằng KKT dựa trên nguồn ở mục 6. P19 và P45 là câu hỏi mới trên mô hình hiện hành. Các phần bổ sung này cần được ghi là thay đổi so với PDF nguồn khi triển khai storyboard.

---

## 5. Bố cục và cách trình bày số liệu

Giữ `lecture-slide.css`, khung 1280×720, tiếng Việt và KaTeX cục bộ. Dùng bảy phần ngoài trong RevealJS. Các sơ đồ mới được vẽ thành SVG theo giao diện sẵn có. Đề xuất sáu bố cục có chức năng riêng:

1. **Cầu nối Bài 03:** trái = kết quả đã biết, phải = nhu cầu hiện tại; một chuỗi công thức chính xác duy nhất.
   ```
   [Đã biết Bài 03]        [Cần hôm nay]
   Giá trị của π         →     Chính sách tối ưu và chứng nhận
   ```
2. **LP 2D:** 2/3 trái là miền khả thi, 1/3 phải là bảng 4 ràng buộc; các đẳng thức được chọn làm nổi bằng **viền + nhãn**, không chỉ dùng màu. Cần vẽ biên $x=4$, $y=20$, $x=-1+0.5y$, $y=5+0.5x$, cả điểm tối ưu khả thi lẫn các điểm PI nằm ngoài; **không** vẽ ứng viên $\pi$ là khả thi.
3. **PI ba bước:** giải → $Q$ → chính sách, thứ tự cột trạng thái nhất quán; $v_{\text{new}}$ không cùng thẻ với $Q_{\text{old}}$; mỗi lượt lặp một slide riêng.
4. **Suy diễn KKT:** một công thức trung tâm mỗi dòng; sơ đồ dòng vào/ra với bơm $c$, $\lambda$ trên cạnh, $d$ tại trạng thái; **không** xếp 4 phương trình vào 2 thẻ không có thứ tự đọc.
5. **VI:** bảng cũ trái, mới phải, mũi tên tại ô được chọn, nhãn $k$/$k+1$; lưới ở cuối.
6. **Chứng minh:** chuỗi dọc các bất đẳng thức $\le$, ghi lý do tại mỗi bước; thuật toán dừng 4 bước + hộp kết quả và chứng nhận.

Số phải được gắn nhãn $r, v, Q, \Delta, \lambda$ — không phân biệt chỉ bằng màu. Không hiển thị mã P nội bộ hay thời lượng trên slide.

Giữ bộ số đã kiểm của Bài 04; mỗi lần dùng ghi rõ loại đại lượng, trạng thái và chính sách tiếp diễn. Trình bày phép tính theo ba thành phần: thưởng → giá trị cũ được đọc → kết quả.

| Nhóm số | Vai trò và cách ghi trên slide |
|---|---|
| $2,-1,5,10$ | Thưởng trên bốn cạnh, luôn đặt cạnh nhãn hành động và hướng chuyển |
| $(4,7)$; $(4,20)$; $(9,20)$ | Ba bảng $v_{\pi_0},v_{\pi_1},v_{\pi_2}$; luôn ghi thứ tự trạng thái $s_0,s_1$ và chính sách tương ứng |
| $4,2.5,7,13.5$ | Bảng $Q_{v_{\pi_0}}$ với hàng trạng thái và cột hành động; $13.5$ là giá trị chọn $b$ một lần rồi quay về $\pi_0$ |
| $2.5,0,10.5,0$ | Bảng độ dư $\Delta_{v_*}$; số $2.5$ tình cờ trùng một ô $Q_{v_{\pi_0}}$ nên phải ghi tên bảng và phép trừ, không chỉ tô màu |
| $\lambda(s_0,b)=1$, $\lambda(s_1,b)=3$ | Luồng chiết khấu; phân biệt với xác suất hành động $\pi(b\mid s)=1$ sau chuẩn hóa |
| $24,-1$ | Thưởng của lưới năm ô, chỉ xuất hiện sau slide giới thiệu mô hình lưới |
| $\theta=0.1$, $\varepsilon_v=0.2$ | Ngưỡng phần dư và mức sai số giá trị mong muốn, đặt trong hai ô có nhãn riêng |

Các phép bằng nhau do cấu trúc Bellman vẫn được giữ. Việc chuyển ví dụ 64 và CartPole 324 sang phụ lục giảm số bộ dữ kiện độc lập trong tuyến chính.

---

## 6. Đối chiếu học liệu đại học và nguồn bổ sung

| Học liệu đã đối chiếu | Kết quả phân tích và cách áp dụng |
|---|---|
| [UCL, David Silver — Lecture 3: Planning by Dynamic Programming](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-3-planning-by-dynamic-programming-.pdf), 42 trang | Tr. 7–11 xây dựng đánh giá chính sách qua lưới trước các thuật toán điều khiển; bảng giá trị đi cùng bảng hành động tham lam. Dùng cách gắn phép tính với hình và đặt đánh giá trước tối ưu. Phần co ở cuối bài giúp tách cơ chế thuật toán khỏi bảo đảm hội tụ |
| [Stanford CS234, Emma Brunskill — Lecture 2, Winter 2022](https://web.stanford.edu/class/archive/cs/cs234/cs234.1224/slides/lecture2_ns.pdf), 66 trang | Tr. 24–26 nối mô hình dưới chính sách với đánh giá và câu hỏi; tr. 33–43 phát triển PI. Trang 39 tách việc đổi hành động một lần khỏi việc dùng chính sách mới về sau. Dùng chính sự phân biệt này để giải thích $13.5$ và $20$ ở P21–P24 |
| [Stanford MS&E235, Benjamin Van Roy — Lecture 7](https://web.stanford.edu/class/msande235a/files/lectures/lecture07.pdf), ghi chú 6 trang | Tr. 1–3 trình bày LP giá trị và hình học hai trạng thái; tr. 6 trình bày đối ngẫu theo luồng. Đây là ghi chú bài giảng, không được tính là bộ slide thứ ba. Chỉ dùng trường hợp chiết khấu $0\le\gamma<1$ |
| [Boyd–Vandenberghe — Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), §5.5.3, tr. in 243–244 | Căn cứ cho bốn điều kiện KKT, tính đủ trong bài toán lồi và điều kiện Slater. Phần vận dụng vào MDP được viết lại với ký hiệu thống nhất của bài |
| [Ying–Zhu — A Note on Optimization Formulations of Markov Decision Processes](https://arxiv.org/pdf/2012.09417), §2, tr. 3–5 | Căn cứ cho quan hệ LP gốc–đối ngẫu, nhân tử và phương trình Bellman tối ưu. Các dấu trong suy diễn được tính lại theo quy ước $\Delta_v=v-Q_v$; ví dụ số dùng mô hình hiện hành của Bài 04 |

Bản đề xuất dựa trên [deck Bài 04 hiện hành](../../lecture-04-giai-mdp-bang-quy-hoach-dong.html), [deck Bài 03](../../lecture-03-qua-trinh-quyet-dinh-markov.html), [PDF nguồn Bài 04](../../../RL-hk2-2025-2026/lecture04-solving-MDP.pdf), [PPTX nguồn Bài 03](../../../RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx), [bài tập tuần 3](../../../RL-hk2-2025-2026/resources/hw3.pdf) và [lecture note hiện hành](../../materials/lec-04/lecture-note.md). Bố cục tham khảo chỉ dùng để chọn cách trình bày; giao diện tiếp tục theo mẫu và CSS chung của kho.

## 7. Các quyết định cần duyệt và phạm vi triển khai

Bốn quyết định cần duyệt:

1. **Luồng 7 phần mới, 45 slide / 120 phút** như mục 4.
2. **KKT trên tuyến chính**, sau khi xác nhận nguồn tiên quyết; nếu chưa học KKT, duyệt riêng phương án chuẩn bị trước buổi học và tác động tới thời lượng chữa bài.
3. **Chuyển phương trình $q_*$, cập nhật tại chỗ, đồ thị 64 và CartPole sang phụ lục** để dành thời gian KKT.
4. **Giữ bộ số hiện hành của Bài 04 và dùng các bố cục SVG đề xuất** như mục 5.

Sau khi duyệt: cập nhật outline/storyboard/HTML+SVG/ghi chú/bài tập/review-log để khớp ánh xạ P → ID thực; chỉ đụng index nếu cần đổi tên/liên kết, không thiết kế lại bố cục không cần thiết. Ghi chú và bài tập hiện tại khớp deck **hiện hành**, sẽ cần đồng bộ lại sau khi duyệt luồng mới; **không** sửa chúng bây giờ.

Sau khi triển khai cần rà năm vai độc lập, tính lại ví dụ và kiểm hiển thị đủ 45 slide ở 1280×720. Trong lượt đề xuất, đã đối chiếu ảnh của bản hiện hành và tính lại ba chính sách, bảng $Q$, độ dư, nhân tử, mục tiêu đối ngẫu cùng các lượt VI bằng phân số chính xác. Chưa triển khai hoặc kiểm hiển thị một deck mới.


## 8. Ghi nhận kiểm tra bản đề xuất

Đối chiếu thực hiện trên HTML Bài 04 có SHA-256 `e55893279e9872c2616fb3b1d287ce8956aa9f206328d9676bd39974e16c0a24`. Ảnh 45 slide khớp phiên bản này; các nhận xét bố cục dựa trên ảnh hiện hành và số đo tại 1280×720. Nguồn Bài 03 đã được kiểm riêng để xác định kết quả có thể nối sang Bài 04.

- Reader phân tích nguồn, writer soạn bản nháp và các reviewer chạy qua OpenRouter. Điều phối viên đối chiếu lại HTML/SVG, công thức, nguồn đại học, biên tập và xử lý từng góp ý trước khi lưu bản này.
- Ba vai sinh viên, chuyên môn Học tăng cường và phản biện giảng dạy đọc toàn bộ bản đề xuất. Vai toán rà cụm LP/KKT, PI/VI, quy tắc dừng và đáp án. Vai mạch viết rà toàn tuyến 45 slide, bản đồ phần, ánh xạ và bố cục trên gói thu hẹp; không coi đó là lượt rà chứng minh toán đầy đủ.
- Chấp nhận rút câu hỏi P19, thêm nhãn “chưa khả thi” tại P21/P22, phân biệt độ thay đổi với sai số, thống nhất thuật ngữ đánh giá chính sách và làm rõ ngân sách $K$. Câu hỏi P05 dùng mô hình P04 để tránh đổi lại sang robot ngay sau khi vừa chuyển mô hình.
- Bác góp ý dùng thưởng $-1$ cho cạnh $(s_1,a)$: cạnh đúng có thưởng 5, nên tại $v_{\pi_1}$ điểm hành động bằng 7 và độ dư bằng 13. Bác đề nghị thay nhân tử ứng viên P45 bằng nhân tử tối ưu: ứng viên $\pi_0$ có hai mục tiêu bằng 11, còn nghiệm tối ưu có hai mục tiêu bằng 29. Đã ghi riêng $\hat v,\hat\lambda$ và thứ tự hàng/cột để tránh lẫn hai trường hợp.
- Việc gộp vấn đề, trực giác và ví dụ trên P06 là có chủ ý; P07 chuyển sang dạng ma trận. Không đổi ví dụ giải hệ sang P07 chỉ vì mã P06 từng xuất hiện hai lần trong mô tả chu trình.
- Một lượt planner và các lượt rà toán/mạch ban đầu vượt giới hạn công cụ hoặc đầu ra; những lượt đó không được tính là hoàn tất. Đã thu hẹp đầu vào và dùng lại cùng mô hình. Lượt rà riêng quy tắc dừng sau sửa xác nhận cách đếm $K$ và chặn sai số nhất quán.

Bằng chứng runtime lấy từ các trường JSON của cầu nối: reader và reviewer toán/chuyên môn có `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`; writer và các reviewer còn lại có `requested_model=observed_model=z-ai/glm-5.3-flash`; `provider=OpenRouter`. Không dùng lời tự khai của tác tử để xác định mô hình.

Tự rà theo Quill đã kiểm đầu vào–đầu ra và thứ tự khái niệm; biên tập theo `no-ai-slop/eval.md` đã cắt lời dẫn quy trình, câu lặp và thuật ngữ tiếng Anh không cần thiết. Không tạo dự án sách. Tệp này là hồ sơ để duyệt thay đổi; HTML, hình, lecture note và bài tập hiện hành chưa được thay theo phương án mới.
