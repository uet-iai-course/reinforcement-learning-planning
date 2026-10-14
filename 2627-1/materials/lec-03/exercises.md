# Bài tập Bài 03 — Quá trình quyết định Markov

Bộ bài tập chính thức của Bài 03 gồm mười chín bài, dùng chung bộ đếm với [ghi chú bài giảng](material-viewer.html?doc=materials/lec-03/lecture-note.md&deck=lecture-03-qua-trinh-quyet-dinh-markov.html), ở ba mức: nhận biết (03.1, 03.15, 03.5, 03.16, 03.17), tính toán hoặc chứng minh (03.2, 03.3, 03.18, 03.4, 03.6, 03.7, 03.19, 03.20, 03.21), vận dụng vào bài toán Học tăng cường (03.22, 03.8, 03.23, 03.24, 03.25); trong mỗi mức, các bài xếp theo mạch. Bài tập 03.1–03.8 giữ số hiệu, đề và lời giải của ghi chú và trùng các trang "Bài tập: …" của bộ trang chiếu; dòng "Trùng trang chiếu" dẫn tới trang câu hỏi và trang lời giải, và lời giải trong tệp cho cùng kết quả với trang. Bài tập 03.9 (Mục 5 của ghi chú) và các bài củng cố 03.10–03.14 chỉ có trong ghi chú; bài củng cố 03.13 là bài tổng hợp trên bộ trang chiếu, có lời giải trên trang và trong ghi chú. Bài tập 03.15–03.25 chỉ có trong tệp này; dòng "Nguồn" của các bài này ghi trang chiếu chứa dữ kiện hoặc kết quả được dùng. Bảng sau xếp các bài theo mạch của bộ trang chiếu.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/1/1) | — |
| 2. Trạng thái Markov và mô hình môi trường | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/1) | 03.1, 03.2, 03.15, 03.22 |
| 3. Lợi tức chiết khấu | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/3/1) | 03.3, 03.18; chỉ trong ghi chú: 03.10 |
| 4. Chính sách và hàm giá trị | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/1) | 03.4, 03.5, 03.16 |
| 5. Phương trình Bellman kỳ vọng | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/5/1) | 03.6, 03.7, 03.17, 03.19; chỉ trong ghi chú: 03.11, 03.12 |
| 6. Đánh giá chính sách bằng hệ tuyến tính | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/1) | 03.8, 03.20, 03.21, 03.23; chỉ trong ghi chú: 03.9, 03.14 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-03-qua-trinh-quyet-dinh-markov.html#/7/1) | 03.24 (câu (a), (b) làm được sau mạch 2), 03.25; chỉ trong ghi chú: 03.13 (bài tổng hợp trên trang [Bài tập: robot với rủi ro cứu hộ thấp hơn](lecture-03-qua-trinh-quyet-dinh-markov.html#/7/4); đề và lời giải trong [ghi chú bài giảng](material-viewer.html?doc=materials/lec-03/lecture-note.md&deck=lecture-03-qua-trinh-quyet-dinh-markov.html)) |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 03. Môi trường được mô tả bằng một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn. Thời điểm quyết định là $t=0,1,2,\dots$; trạng thái, hành động và phần thưởng là các biến ngẫu nhiên $S_t$, $A_t$, $R_{t+1}$, trong đó phần thưởng (reward) $R_{t+1}$ và trạng thái $S_{t+1}$ đến cùng lúc, sau hành động $A_t$. Lịch sử tới thời điểm $t$ là $H_t=(S_0,A_0,R_1,S_1,\dots,R_t,S_t)$, viết nghiêng, khác tên trạng thái $\mathrm H$ viết đứng. Trạng thái có tính Markov (Markov property) khi phân phối của $(S_{t+1},R_{t+1})$ biết $H_t$ và $A_t$ chỉ phụ thuộc $S_t$ và $A_t$. Hàm động lực (dynamics function) là $p(s',r\mid s,a)$; xác suất chuyển $p(s'\mid s,a)$ và thưởng kỳ vọng một bước $r(s,a)$ suy ra từ $p$ theo (1.5), (1.6). Với hệ số chiết khấu (discount factor) $\gamma\in[0,1)$, trừ khi bài nêu khác, lợi tức (return) là $G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots$, với $G_T=0$ khi lượt (episode) kết thúc tại $T$; nhiệm vụ không chia thành lượt là nhiệm vụ tiếp diễn (continuing task). Chính sách (policy) $\pi(a\mid s)$ là chính sách Markov dừng; $\mathbb E_\pi$ là kỳ vọng khi hành động theo $\pi$ và phản hồi theo $p$. Hàm giá trị (value function) gồm giá trị trạng thái $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$, lấy trên quá trình xuất phát tại $s$, và giá trị hành động $q_\pi(s,a)$, lấy trên quá trình ấn định $S_0=s$, $A_0=a$ rồi theo $\pi$ từ thời điểm $1$. Giá trị tại trạng thái kết thúc bằng $0$. Ma trận chuyển và véc-tơ thưởng kỳ vọng dưới $\pi$ viết $P_\pi$, $r_\pi$ như ghi chú (5.2), với trạng thái xếp theo thứ tự nêu trong từng bài.

Tên trạng thái và tên hành động viết chữ đứng: $\mathrm H$ (pin cao), $\mathrm L$ (pin thấp), $\mathrm{tim}$ (Tìm), $\mathrm{cho}$ (Chờ), $\mathrm{sac}$ (Sạc). Số thập phân viết với dấu phẩy, như $0{,}9$; khi một véc-tơ có thành phần thập phân, các thành phần cách nhau bằng dấu chấm phẩy, như $(0{,}874;\,-1{,}154;\,0)$.

**Robot thu gom lon hai mức pin** (ghi chú Ví dụ 03.1, 03.5) là môi trường dùng chung của nhiều bài và được nêu lại trong từng bài dùng nó. Tập trạng thái $\mathcal S=\{\mathrm H,\mathrm L\}$, không có trạng thái kết thúc; nhiệm vụ tiếp diễn. Tập hành động $\mathcal A(\mathrm H)=\{\mathrm{tim},\mathrm{cho}\}$, $\mathcal A(\mathrm L)=\{\mathrm{tim},\mathrm{cho},\mathrm{sac}\}$; tập phần thưởng $\mathcal R=\{-3,0,1,2\}$. Bảng phản hồi có bảy hàng:

| $s$ | $a$ | $s'$ | $r$ | $p(s',r\mid s,a)$ |
|---|---|---|---:|---:|
| $\mathrm H$ | $\mathrm{tim}$ | $\mathrm H$ | $2$ | $1/2$ |
| $\mathrm H$ | $\mathrm{tim}$ | $\mathrm L$ | $2$ | $1/2$ |
| $\mathrm H$ | $\mathrm{cho}$ | $\mathrm H$ | $1$ | $1$ |
| $\mathrm L$ | $\mathrm{tim}$ | $\mathrm L$ | $2$ | $1/2$ |
| $\mathrm L$ | $\mathrm{tim}$ | $\mathrm H$ | $-3$ | $1/2$ |
| $\mathrm L$ | $\mathrm{cho}$ | $\mathrm L$ | $1$ | $1$ |
| $\mathrm L$ | $\mathrm{sac}$ | $\mathrm H$ | $0$ | $1$ |

**Chính sách chia đều tại pin thấp** (ghi chú Ví dụ 03.9): ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động xác suất $1/2$, không bao giờ Tìm. Với $\gamma=1/2$, giá trị của chính sách này là $v_\pi(\mathrm H)=13/4$, $v_\pi(\mathrm L)=7/4$ (ghi chú, Ví dụ 03.14). Khi giải hệ, viết $v_{\mathrm H}=v_\pi(\mathrm H)$, $v_{\mathrm L}=v_\pi(\mathrm L)$.

Mọi xác suất, mức thưởng và môi trường nhỏ trong tệp là số liệu sư phạm tự xây dựng, trừ khi dòng "Nguồn" ghi khác. Lời giải nêu kết quả của ghi chú được dùng ở từng bước.

## Mức nhận biết

### Bài tập 03.1. Trạng thái của robot

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** ghi chú bài giảng, Bài tập 03.1 (tiểu mục 1.2), giữ số hiệu, đề và lời giải; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: trạng thái của robot](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/7) và [trang lời giải](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/8): câu (b); câu (a) chỉ có trong ghi chú và tệp này.

::: exercise Bài tập 03.1 (Trạng thái của robot)
**Dữ kiện.** (a) Robot thu gom lon hai mức pin (Chờ từ $\mathrm L$ cho phần thưởng $1$ và giữ pin ở $\mathrm L$) ghi được bản ghi $(\mathrm L,\mathrm{cho},1,\mathrm L)$ ở bước bắt đầu tại thời điểm $t=4$. (b) Số liệu sư phạm tự xây dựng: một robot chỉ hoạt động ở pin cao, pin luôn giữ ở $\mathrm H$, và ở mọi bước tác tử chọn Tìm hoặc Chờ, mỗi hành động xác suất $1/2$. Robot được đặt cố định suốt đời ở một trong hai vị trí, mỗi vị trí xác suất $1/2$, và trạng thái không ghi vị trí. Ở vị trí gần cửa, Tìm luôn cho phần thưởng $2$. Ở vị trí xa cửa, Tìm cho $2$ hoặc $0$, mỗi kết quả xác suất $1/2$. Chờ ở cả hai vị trí cho $1$.

**Yêu cầu.** (a) Viết bản ghi bằng các biến ngẫu nhiên có chỉ số thời gian. (b) Xét hai lịch sử $h=(\mathrm H,\mathrm{tim},0,\mathrm H)$ và $h'=(\mathrm H,\mathrm{cho},1,\mathrm H)$ tại $t=1$. Tính $\Pr(R_2=0\mid H_1=h,A_1=\mathrm{tim})$ và $\Pr(R_2=0\mid H_1=h',A_1=\mathrm{tim})$, rồi kết luận trạng thái "mức pin" có tính Markov hay không.
:::

::: hint Gợi ý Bài tập 03.1
Ở câu (b), phần thưởng $0$ chỉ xảy ra ở vị trí xa cửa. Tính xác suất robot ở vị trí xa cửa khi biết từng lịch sử, rồi nhân với xác suất Tìm cho $0$ ở vị trí đó.
:::

::: solution Lời giải Bài tập 03.1
**Câu (a).** Bước bắt đầu tại $t=4$ nên $S_4=\mathrm L$, $A_4=\mathrm{cho}$, $R_5=1$, $S_5=\mathrm L$. Phần thưởng mang chỉ số $5$ vì nó đến sau hành động $A_4$.

**Câu (b).** Với $h$, phần thưởng $R_1=0$ sau Tìm chỉ có thể xảy ra ở vị trí xa cửa, nên robot chắc chắn ở vị trí xa cửa và

$$
\begin{aligned}
&\Pr(R_2=0\mid H_1=h,A_1=\mathrm{tim})\\
&\qquad=\tfrac12 .
\end{aligned}
$$

Với $h'$, Chờ cho $1$ ở cả hai vị trí, nên lịch sử không cho thông tin về vị trí; xác suất ở vị trí xa cửa vẫn là $1/2$. Theo công thức xác suất toàn phần theo vị trí,

$$
\begin{aligned}
&\Pr(R_2=0\mid H_1=h',A_1=\mathrm{tim})\\
&\qquad=\tfrac12\cdot\tfrac12+\tfrac12\cdot0\\
&\qquad=\tfrac14 .
\end{aligned}
$$

Hai lịch sử kết thúc ở cùng trạng thái $\mathrm H$ với cùng hành động Tìm nhưng cho hai xác suất $1/2$ và $1/4$, nên (1.2) không thể thỏa với cả hai; trạng thái "mức pin" không có tính Markov. Thêm vị trí vào trạng thái khôi phục tính Markov.

**Kiểm tra lại.** Theo chính sách trong Dữ kiện, $h$ có xác suất $\tfrac12\cdot\tfrac12\cdot\tfrac12=\tfrac18$ (chọn Tìm, ở vị trí xa cửa, nhận $0$) và $h'$ có xác suất $\tfrac12$ (chọn Chờ); cả hai dương. Hai lỗi thường gặp: viết phần thưởng của bước bắt đầu tại $t=4$ là $R_4$, tức bản ghi lệch chỉ số $(S_4,A_4,R_4,S_5)$; coi vị trí được rút lại ở mỗi bước, khi đó hai xác suất cùng bằng $\tfrac14$ và dẫn tới kết luận sai rằng mức pin có tính Markov.
:::

### Bài tập 03.15. Phản hồi đồng thời trong bảng hàm động lực

**Mức độ:** nhận biết; mục tiêu học tập 1.

**Nguồn:** Sutton và Barto (2018), bài tập 3.4, tr. 53; ghi chú Mệnh đề 03.6. Dữ kiện như trang [Ví dụ: bảng phản hồi của robot](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/10).

::: exercise Bài tập 03.15 (Phản hồi đồng thời trong bảng hàm động lực)
Robot thu gom lon hai mức pin có bảng phản hồi: $(\mathrm H,\mathrm{tim})\to(\mathrm H,2)$ hoặc $(\mathrm L,2)$, mỗi nhánh xác suất $1/2$; $(\mathrm H,\mathrm{cho})\to(\mathrm H,1)$ với xác suất $1$; $(\mathrm L,\mathrm{tim})\to(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi nhánh xác suất $1/2$; $(\mathrm L,\mathrm{cho})\to(\mathrm L,1)$ với xác suất $1$; $(\mathrm L,\mathrm{sac})\to(\mathrm H,0)$ với xác suất $1$. Mỗi mũi tên ghi cặp (trạng thái kế tiếp, phần thưởng).

- (a) Đọc $p(\mathrm H,0\mid\mathrm L,\mathrm{sac})$ và $p(\mathrm H,2\mid\mathrm L,\mathrm{tim})$; kiểm tra điều kiện chuẩn hóa (1.3) của cặp $(\mathrm L,\mathrm{sac})$.
- (b) Biết phần thưởng sau cặp $(\mathrm L,\mathrm{tim})$ là $-3$, xác định trạng thái kế tiếp. Chứng tỏ rằng, khi biết $S_t=\mathrm L$, $A_t=\mathrm{tim}$, hai biến $S_{t+1}$ và $R_{t+1}$ không độc lập.
- (c) Một bảng khác cho cặp $(\mathrm L,\mathrm{tim})$ hai phản hồi $(\mathrm L,-1/2)$ và $(\mathrm H,-1/2)$, mỗi phản hồi xác suất $1/2$. Tính $p(\mathrm H\mid\mathrm L,\mathrm{tim})$ và $r(\mathrm L,\mathrm{tim})$ theo bảng này, so với bảng của robot, rồi rút ra kết luận về việc dựng lại $p(s',r\mid s,a)$ từ $p(s'\mid s,a)$ và $r(s,a)$.
:::

::: hint Gợi ý Bài tập 03.15
Mỗi hàng của bảng là một giá trị dương của $p$; bộ $(s',r)$ không có trong bảng có $p=0$. Ở câu (b), so sánh $\Pr(S_{t+1}=\mathrm H,R_{t+1}=-3\mid\cdot)$ với tích hai xác suất biên.
:::

::: solution Lời giải Bài tập 03.15
**Câu (a).** Cặp $(\mathrm L,\mathrm{sac})$ chỉ có hàng $(\mathrm H,0)$ với xác suất $1$, nên $p(\mathrm H,0\mid\mathrm L,\mathrm{sac})=1$. Tổng của $p(\cdot,\cdot\mid\mathrm L,\mathrm{sac})$ trên mọi bộ $(s',r)$ gồm một số hạng bằng $1$ và các số hạng $0$, nên (1.3) thỏa. Bộ $(\mathrm H,2)$ không có trong nhóm $(\mathrm L,\mathrm{tim})$, nên $p(\mathrm H,2\mid\mathrm L,\mathrm{tim})=0$.

**Câu (b).** Trong nhóm $(\mathrm L,\mathrm{tim})$, phần thưởng $-3$ chỉ đi cùng trạng thái kế tiếp $\mathrm H$, nên trạng thái kế tiếp là $\mathrm H$. Theo (1.5), $\Pr(S_{t+1}=\mathrm H\mid S_t=\mathrm L,A_t=\mathrm{tim})=\tfrac12$. Cộng các hàng có phần thưởng $-3$ được $\Pr(R_{t+1}=-3\mid S_t=\mathrm L,A_t=\mathrm{tim})=\tfrac12$. Nếu hai biến độc lập thì xác suất đồng thời bằng $\tfrac12\cdot\tfrac12=\tfrac14$. Bảng cho xác suất đồng thời $p(\mathrm H,-3\mid\mathrm L,\mathrm{tim})=\tfrac12\ne\tfrac14$, nên hai biến không độc lập.

**Câu (c).** Bảng mới cho $p(\mathrm H\mid\mathrm L,\mathrm{tim})=\tfrac12$ và $r(\mathrm L,\mathrm{tim})=\tfrac12\cdot(-\tfrac12)+\tfrac12\cdot(-\tfrac12)=-\tfrac12$. Bảng của robot cho cùng hai số: $p(\mathrm H\mid\mathrm L,\mathrm{tim})=\tfrac12$ và $r(\mathrm L,\mathrm{tim})=\tfrac12\cdot2+\tfrac12\cdot(-3)=-\tfrac12$. Hai hàm động lực khác nhau có cùng $p(s'\mid s,a)$ và $r(s,a)$, nên hai đại lượng này không đủ để dựng lại $p(s',r\mid s,a)$, đúng phần Phạm vi của Mệnh đề 03.6.

**Kiểm tra lại.** Ở bảng mới, $S_{t+1}$ và $R_{t+1}$ độc lập vì $R_{t+1}=-\tfrac12$ chắc chắn. Ba lỗi thường gặp: coi bộ không có trong bảng là "không xác định" thay vì $p=0$, nên không kiểm được tổng (1.3) của cặp; tính xác suất đồng thời bằng tích hai xác suất biên, tức ngầm giả thiết độc lập, được $\tfrac14$ thay vì $\tfrac12$; cho rằng biết $r(s,a)$ là biết phần thưởng của từng nhánh, tức không phân biệt được bảng của câu (c) với bảng của robot.
:::

### Bài tập 03.5. Mô hình, chính sách và giá trị

**Mức độ:** nhận biết; mục tiêu học tập 3.

**Nguồn:** ghi chú bài giảng, Bài tập 03.5 (tiểu mục 3.3), giữ số hiệu, đề và lời giải.

**Trùng trang chiếu:** [Bài tập: mô hình, chính sách và giá trị](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/9) và [trang lời giải](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/10): câu (a) của trang.

::: exercise Bài tập 03.5 (Mô hình, chính sách và giá trị)
**Dữ kiện.** Robot thu gom lon hai mức pin với chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động xác suất $1/2$), $\gamma=1/2$.

**Yêu cầu.** Đổi chính sách ở pin thấp thành "Chờ với xác suất $3/4$, Sạc với xác suất $1/4$". Trong ba đối tượng hàm động lực $p$, chính sách $\pi$ và hàm giá trị $v_\pi$, xác định đối tượng nào chắc chắn đổi, đối tượng nào chắc chắn giữ nguyên, đối tượng nào có thể đổi, và giải thích.
:::

::: hint Gợi ý Bài tập 03.5
Hàm động lực thuộc về môi trường; chính sách thuộc về tác tử; hàm giá trị phụ thuộc cả hai.
:::

::: solution Lời giải Bài tập 03.5
Chính sách $\pi$ đổi theo giả thiết. Hàm động lực $p$ giữ nguyên, vì phản hồi của môi trường sau mỗi cặp $(s,a)$ không phụ thuộc cách chọn hành động. Hàm giá trị $v_\pi$ có thể đổi, vì xác suất của các quỹ đạo, tính theo (3.2), thay đổi khi $\pi$ đổi.

**Kiểm tra lại.** Nếu tính lại $v_\pi$ cho chính sách mới, các phương trình của Mục 4 dùng cùng các hệ số từ $p$ và hệ số mới từ $\pi$. Lỗi thường gặp: cho rằng đổi chính sách thì đổi hàm động lực $p$, dẫn tới kết luận sai rằng cả ba đối tượng đều chắc chắn đổi; đổi chính sách chỉ đổi xác suất của các quỹ đạo.
:::

### Bài tập 03.16. Giá trị trạng thái và giá trị hành động tại pin thấp

**Mức độ:** nhận biết; mục tiêu học tập 3.

**Nguồn:** Bài tập tuần 3 (2025–2026), bài 1; ghi chú Định nghĩa 03.15, 03.16, Ví dụ 03.11 và 03.15. Kết quả dùng lại ở trang [Ví dụ: ba thí nghiệm từ pin thấp](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/7) và trang [Ví dụ: kiểm tra nghiệm bằng giá trị hành động](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/5).

::: exercise Bài tập 03.16 (Giá trị trạng thái và giá trị hành động tại pin thấp)
Robot thu gom lon hai mức pin: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $1/2$; Tìm từ $\mathrm L$ cho $(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi phản hồi xác suất $1/2$; Chờ từ $\mathrm L$ cho $(\mathrm L,1)$; Sạc từ $\mathrm L$ cho $(\mathrm H,0)$. Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động xác suất $1/2$, nên $\pi(\mathrm{tim}\mid\mathrm L)=0$. Hệ số chiết khấu $\gamma=1/2$. Kỳ vọng hai số hạng đầu của lợi tức khi ấn định Tìm tại $\mathrm L$ bằng $\tfrac18$ (ghi chú, Ví dụ 03.11); ba giá trị hành động tại $\mathrm L$ là $q_\pi(\mathrm L,\mathrm{tim})=\tfrac34$, $q_\pi(\mathrm L,\mathrm{cho})=\tfrac{15}8$, $q_\pi(\mathrm L,\mathrm{sac})=\tfrac{13}8$ (ghi chú, Ví dụ 03.15).

- (a) Trong định nghĩa của $v_\pi(\mathrm L)$ và của $q_\pi(\mathrm L,\mathrm{tim})$, nêu hành động đầu tiên được chọn theo quy tắc nào, và từ thời điểm nào robot theo $\pi$.
- (b) Trong thí nghiệm định nghĩa $q_\pi(\mathrm L,\mathrm{tim})$, robot bị buộc Tìm bao nhiêu lần. Xác định trong thí nghiệm đó robot còn có thể Tìm ở những trạng thái nào và vì sao.
- (c) Giải thích vì sao $q_\pi(\mathrm L,\mathrm{tim})$ xác định dù $\pi(\mathrm{tim}\mid\mathrm L)=0$, còn kỳ vọng có điều kiện $\mathbb E_\pi[G_t\mid S_t=\mathrm L,A_t=\mathrm{tim}]$ trên quá trình theo $\pi$ ở mọi thời điểm thì không xác định.
:::

::: hint Gợi ý Bài tập 03.16
Định nghĩa 03.16 dùng quá trình ấn định $(s,a)$. Ở câu (c), tính $\Pr_\pi(S_t=\mathrm L,A_t=\mathrm{tim})$ khi robot theo $\pi$ ở mọi thời điểm.
:::

::: solution Lời giải Bài tập 03.16
**Câu (a).** Với $v_\pi(\mathrm L)$, quá trình xuất phát tại $\mathrm L$ rút cả hành động đầu $A_0$ theo $\pi(\cdot\mid\mathrm L)$, tức Chờ hoặc Sạc, và theo $\pi$ ở mọi thời điểm (Định nghĩa 03.15). Với $q_\pi(\mathrm L,\mathrm{tim})$, hành động đầu bị ấn định $A_0=\mathrm{tim}$ với xác suất $1$, và robot theo $\pi$ từ thời điểm $1$ (Định nghĩa 03.16).

**Câu (b).** Robot bị buộc Tìm đúng một lần, tại thời điểm $0$. Từ thời điểm $1$, hành động do $\pi$ chọn. Nếu phản hồi đầu là $(\mathrm H,-3)$, robot ở $\mathrm H$ và chính sách chọn Tìm với xác suất $1$; lần Tìm này do $\pi$ chọn, không do thí nghiệm buộc. Ở $\mathrm L$, từ thời điểm $1$ robot không bao giờ Tìm, vì $\pi(\mathrm{tim}\mid\mathrm L)=0$.

**Câu (c).** Định nghĩa 03.16 lấy kỳ vọng trên quá trình ấn định, nơi sự kiện $\{S_0=\mathrm L,A_0=\mathrm{tim}\}$ có xác suất $1$; định nghĩa không chia cho $\pi(\mathrm{tim}\mid\mathrm L)$. Kỳ vọng tồn tại vì mọi phần thưởng có trị tuyệt đối không quá $3$, nên $\lvert G_0\rvert\le3/(1-\gamma)=6$ (Mệnh đề 03.11). Trên quá trình theo $\pi$ ở mọi thời điểm, theo (3.1),

$$
\begin{aligned}
&\Pr_\pi(S_t=\mathrm L,A_t=\mathrm{tim})\\
&\quad=\Pr_\pi(S_t=\mathrm L)\,\pi(\mathrm{tim}\mid\mathrm L)\\
&\quad=0,
\end{aligned}
$$

nên kỳ vọng có điều kiện theo sự kiện này không xác định. Bổ đề 03.20(d) chỉ đồng nhất hai cách viết khi $\Pr_\pi(S_t=s,A_t=a)>0$. Hai số của ghi chú đều tính trên quá trình ấn định: hai số hạng đầu cho $\tfrac18$, toàn bộ lợi tức cho $q_\pi(\mathrm L,\mathrm{tim})=\tfrac34$.

**Kiểm tra lại.** Theo (4.7), $v_\pi(\mathrm L)=0\cdot\tfrac34+\tfrac12\cdot\tfrac{15}8+\tfrac12\cdot\tfrac{13}8=\tfrac74$: giá trị của Tìm không góp vào $v_\pi(\mathrm L)$ dù nó xác định. Hai lỗi thường gặp: cho rằng thí nghiệm buộc robot Tìm ở mọi bước, khi đó con số thu được là giá trị của chính sách "luôn Tìm", khác $q_\pi(\mathrm L,\mathrm{tim})$; cho rằng $q_\pi(s,a)=0$ khi $\pi(a\mid s)=0$, được $q_\pi(\mathrm L,\mathrm{tim})=0$ thay vì $\tfrac34$.
:::

### Bài tập 03.17. Hai con số $21/8$ ở pin cao

**Mức độ:** nhận biết (công thức (4.6) cho sẵn trong đề); mục tiêu học tập 3 và 4.

**Nguồn:** số liệu sư phạm tự xây dựng; ghi chú Ví dụ 03.10 và Bài tập 03.11. Kỳ vọng hai bước ở trang [Ví dụ: kỳ vọng hai bước từ pin cao](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/5); quan hệ $q$ theo $v$ ở trang [Giá trị hành động theo giá trị trạng thái](lecture-03-qua-trinh-quyet-dinh-markov.html#/5/8).

::: exercise Bài tập 03.17 (Hai con số $21/8$ ở pin cao)
Robot thu gom lon hai mức pin: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $1/2$; Chờ từ $\mathrm H$ cho phần thưởng $1$ và ở lại $\mathrm H$; Chờ từ $\mathrm L$ cho $(\mathrm L,1)$; Sạc từ $\mathrm L$ cho $(\mathrm H,0)$. Chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$), $\gamma=1/2$, $v_\pi(\mathrm H)=\tfrac{13}4$, $v_\pi(\mathrm L)=\tfrac74$. Hai con số sau bằng nhau: kỳ vọng hai bước $\mathbb E_\pi[R_1+\gamma R_2\mid S_0=\mathrm H]=\tfrac{21}8$ (ghi chú, Ví dụ 03.10) và $q_\pi(\mathrm H,\mathrm{cho})=\tfrac{21}8$ (ghi chú, Bài tập 03.11). Nhắc lại (4.6): $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s')$.

- (a) Với mỗi con số, nêu hành động đầu tiên, số số hạng của lợi tức được tính, và cách robot chọn hành động từ thời điểm $1$.
- (b) Đổi phần thưởng của Chờ từ $\mathrm H$ thành $\tfrac12$, mọi phản hồi khác giữ nguyên. Xác định giá trị mới của $v_\pi$, của kỳ vọng hai bước từ $\mathrm H$ và của $q_\pi(\mathrm H,\mathrm{cho})$.
- (c) Kết luận đẳng thức giữa hai con số $\tfrac{21}8$ là một tính chất chung hay một trùng hợp số học.
:::

::: hint Gợi ý Bài tập 03.17
Ở câu (b), xét cặp $(\mathrm H,\mathrm{cho})$ có góp vào $P_\pi$, $r_\pi$ và vào cây hai bước từ $\mathrm H$ hay không; $q_\pi(\mathrm H,\mathrm{cho})$ tính theo dạng thứ hai của (4.6).
:::

::: solution Lời giải Bài tập 03.17
**Câu (a).** Kỳ vọng hai bước: hành động đầu do $\pi$ chọn, ở $\mathrm H$ là Tìm; chỉ hai số hạng $R_1+\gamma R_2$ được tính; từ thời điểm $1$ robot theo $\pi$. Giá trị $q_\pi(\mathrm H,\mathrm{cho})$: hành động đầu bị ấn định là Chờ; toàn bộ lợi tức $G_0$ được tính; từ thời điểm $1$ robot theo $\pi$. Hai con số khác nhau ở cả hành động đầu lẫn số số hạng.

**Câu (b).** Chính sách có $\pi(\mathrm{cho}\mid\mathrm H)=0$, nên theo (5.2) cặp $(\mathrm H,\mathrm{cho})$ không góp vào $P_\pi$ và $r_\pi$. Hai đối tượng này giữ nguyên, và theo Định lý 03.28, $v_\pi=(\tfrac{13}4,\tfrac74)$ không đổi. Cây hai bước từ $\mathrm H$ chỉ dùng Tìm ở $\mathrm H$ và Chờ, Sạc ở $\mathrm L$, nên kỳ vọng hai bước vẫn là $\tfrac{21}8$. Theo (4.6), robot ở lại $\mathrm H$ sau Chờ, nên

$$
q_\pi(\mathrm H,\mathrm{cho})=\tfrac12+\tfrac12\cdot\tfrac{13}4=\tfrac{17}8 .
$$

**Câu (c).** Sau thay đổi, kỳ vọng hai bước giữ $\tfrac{21}8$ còn $q_\pi(\mathrm H,\mathrm{cho})$ thành $\tfrac{17}8$. Đẳng thức ban đầu là trùng hợp số học: $\tfrac{21}8=2+\tfrac12\cdot\tfrac54$ ở kỳ vọng hai bước, với $\mathbb E_\pi[R_2\mid S_0=\mathrm H]=\tfrac54$, và $\tfrac{21}8=1+\tfrac12\cdot\tfrac{13}4$ ở giá trị hành động.

**Kiểm tra lại.** Giá trị của hành động chính sách thật sự chọn ở $\mathrm H$ là $q_\pi(\mathrm H,\mathrm{tim})=v_\pi(\mathrm H)=\tfrac{13}4$, khác $\tfrac{21}8$. Hai lỗi thường gặp: coi kỳ vọng hai bước là một giá trị hành động, dẫn tới $q_\pi(\mathrm H,\mathrm{tim})=\tfrac{21}8$ thay vì $\tfrac{13}4$; hạ cả $v_\pi(\mathrm H)$ theo phần thưởng mới của Chờ, trong khi $\pi$ không chọn Chờ ở $\mathrm H$ nên $v_\pi$ vẫn là $(\tfrac{13}4,\tfrac74)$.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 03.2. Đọc hàm động lực của robot

**Mức độ:** tính toán; mục tiêu học tập 1.

**Nguồn:** ghi chú bài giảng, Bài tập 03.2 (tiểu mục 1.5), giữ số hiệu, đề và lời giải.

**Trùng trang chiếu:** [Bài tập: đọc hàm động lực của robot](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/14) và [trang lời giải](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/15).

::: exercise Bài tập 03.2 (Đọc hàm động lực của robot)
**Dữ kiện.** Robot thu gom lon hai mức pin có bảng phản hồi: $(\mathrm H,\mathrm{tim})\to(\mathrm H,2)$ hoặc $(\mathrm L,2)$, mỗi nhánh $1/2$; $(\mathrm H,\mathrm{cho})\to(\mathrm H,1)$; $(\mathrm L,\mathrm{tim})\to(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi nhánh $1/2$; $(\mathrm L,\mathrm{cho})\to(\mathrm L,1)$; $(\mathrm L,\mathrm{sac})\to(\mathrm H,0)$.

**Yêu cầu.** Lập bảng $p(\mathrm H\mid s,a)$, $p(\mathrm L\mid s,a)$ và $r(s,a)$ cho cả năm cặp hợp lệ, rồi kiểm tra điều kiện chuẩn hóa của mỗi cặp.
:::

::: hint Gợi ý Bài tập 03.2
Dùng (1.5) cho xác suất chuyển và (1.6) cho thưởng kỳ vọng; mỗi cặp chỉ có một hoặc hai hàng.
:::

::: solution Lời giải Bài tập 03.2
Theo (1.5) và (1.6):

| $(s,a)$ | $p(\mathrm H\mid s,a)$ | $p(\mathrm L\mid s,a)$ | $r(s,a)$ |
|---|---:|---:|---:|
| $(\mathrm H,\mathrm{tim})$ | $1/2$ | $1/2$ | $\tfrac12\cdot2+\tfrac12\cdot2=2$ |
| $(\mathrm H,\mathrm{cho})$ | $1$ | $0$ | $1$ |
| $(\mathrm L,\mathrm{tim})$ | $1/2$ | $1/2$ | $\tfrac12\cdot2+\tfrac12\cdot(-3)=-1/2$ |
| $(\mathrm L,\mathrm{cho})$ | $0$ | $1$ | $1$ |
| $(\mathrm L,\mathrm{sac})$ | $1$ | $0$ | $0$ |

**Kiểm tra lại.** Mỗi dòng có $p(\mathrm H\mid s,a)+p(\mathrm L\mid s,a)=1$, đúng phần cuối của Mệnh đề 03.6. Hai lỗi thường gặp: ghi $r(\mathrm L,\mathrm{tim})$ bằng phần thưởng của một nhánh, $2$ hoặc $-3$, thay vì trung bình $-\tfrac12$; lập thêm hàng cho cặp $(\mathrm H,\mathrm{sac})$, vốn không hợp lệ, nên bảng có sáu hàng thay vì năm.
:::

### Bài tập 03.3. Lợi tức và cận của robot

**Mức độ:** tính toán; mục tiêu học tập 2.

**Nguồn:** ghi chú bài giảng, Bài tập 03.3 (tiểu mục 2.3), giữ số hiệu, đề và lời giải.

**Trùng trang chiếu:** [Bài tập: lợi tức và cận của robot](lecture-03-qua-trinh-quyet-dinh-markov.html#/3/6) và [trang lời giải](lecture-03-qua-trinh-quyet-dinh-markov.html#/3/7).

::: exercise Bài tập 03.3 (Lợi tức và cận của robot)
**Dữ kiện.** Robot thu gom lon hai mức pin bắt đầu ở $\mathrm L$, Tìm và nhận $2$ (vẫn ở $\mathrm L$), Tìm lần nữa và được cứu hộ ($-3$, về $\mathrm H$), rồi Chờ ở $\mathrm H$ (phần thưởng $1$). Ba phần thưởng đầu là $(R_1,R_2,R_3)=(2,-3,1)$; tập phần thưởng $\mathcal R=\{-3,0,1,2\}$.

**Yêu cầu.** (a) Robot về pin cao sau cứu hộ; xác định nhiệm vụ có kết thúc tại thời điểm đó không. (b) Tính lợi tức cắt sau ba bước $R_1+\gamma R_2+\gamma^2R_3$ với $\gamma=1/2$ và với $\gamma=0$. (c) Với $\gamma=1/2$, xác định khoảng chứa $G_0$ của mọi quỹ đạo có ba phần thưởng đầu như trên.
:::

::: hint Gợi ý Bài tập 03.3
Câu (a) dùng Định nghĩa 03.8. Câu (c): phần đuôi $\sum_{j\ge3}\gamma^jR_{j+1}$ bị chặn theo cùng lập luận của Mệnh đề 03.11, với thừa số $\gamma^3$.
:::

::: solution Lời giải Bài tập 03.3
**Câu (a).** Không. Robot là nhiệm vụ tiếp diễn (Định nghĩa 03.8): cứu hộ chỉ đổi trạng thái, tương tác vẫn tiếp tục và không có trạng thái kết thúc.

**Câu (b).** Với $\gamma=1/2$: $2+\tfrac12\cdot(-3)+\tfrac14\cdot1=2-\tfrac32+\tfrac14=\tfrac34$. Với $\gamma=0$: chỉ số hạng đầu còn lại, bằng $2$.

**Câu (c).** Với $M=\max_{r\in\mathcal R}\lvert r\rvert=3$, phần đuôi có trị tuyệt đối không quá $\gamma^3M/(1-\gamma)=\tfrac18\cdot6=\tfrac34$, nên $G_0\in\bigl[\tfrac34-\tfrac34,\ \tfrac34+\tfrac34\bigr]=\bigl[0,\tfrac32\bigr]$.

**Kiểm tra lại.** Khoảng $[0,\tfrac32]$ nằm trong $[-6,6]$ của Ví dụ 03.8, như phải có. Hai lỗi thường gặp: coi cận $6$ là giá trị của lợi tức, tức kết luận $G_0=6$; chặn phần đuôi bằng $M/(1-\gamma)$ mà quên thừa số $\gamma^3$, được khoảng quá rộng $[\tfrac34-6,\ \tfrac34+6]=[-\tfrac{21}4,\ \tfrac{27}4]$.
:::

### Bài tập 03.18. Lợi tức cắt và cận phần đuôi

**Mức độ:** tính toán; mục tiêu học tập 2. Câu (a), (b) luyện lại dạng của Bài tập 03.3 trên một dãy khác; câu (c), (d) mở rộng.

**Nguồn:** Sutton và Barto (2018), bài tập 3.8–3.9, tr. 56; ghi chú Mệnh đề 03.11. Dãy phần thưởng là dãy thứ nhất của trang [Lợi tức của robot](lecture-03-qua-trinh-quyet-dinh-markov.html#/3/2); cận ở trang [Cận của lợi tức](lecture-03-qua-trinh-quyet-dinh-markov.html#/3/5).

::: exercise Bài tập 03.18 (Lợi tức cắt và cận phần đuôi)
Robot thu gom lon hai mức pin bắt đầu ở $\mathrm L$. Robot Sạc (phần thưởng $0$, về $\mathrm H$), rồi Tìm từ $\mathrm H$ và pin giữ ở $\mathrm H$ (phần thưởng $2$), rồi Tìm từ $\mathrm H$ lần nữa (phần thưởng $2$). Ba phần thưởng đầu là $(R_1,R_2,R_3)=(0,2,2)$; các phần thưởng sau chưa biết. Tập phần thưởng là $\mathcal R=\{-3,0,1,2\}$; nhiệm vụ tiếp diễn.

- (a) Tính lợi tức cắt sau ba bước $G_0^{[3]}=R_1+\gamma R_2+\gamma^2R_3$ với $\gamma=\tfrac12$, $\gamma=0$ và $\gamma=0{,}9$.
- (b) Với $\gamma=\tfrac12$ và $M=\max_{r\in\mathcal R}\lvert r\rvert$, xác định một khoảng chứa $G_0$ của mọi quỹ đạo có ba phần thưởng đầu như trên.
- (c) Dùng $-3\le R_k\le2$ thay cho $\lvert R_k\rvert\le M$, thu hẹp khoảng ở câu (b).
- (d) Tìm số nguyên $K$ nhỏ nhất sao cho cận phần đuôi $\gamma^KM/(1-\gamma)$ không vượt $0{,}1$, với $\gamma=\tfrac12$ và với $\gamma=0{,}9$; với $\gamma=0{,}9$, viết khoảng của câu (b).
:::

::: hint Gợi ý Bài tập 03.18
Phần đuôi là $\sum_{j\ge3}\gamma^jR_{j+1}=\gamma^3\sum_{i\ge0}\gamma^iR_{i+4}$; chặn tổng sau bằng lập luận chuỗi trội của Mệnh đề 03.11.
:::

::: solution Lời giải Bài tập 03.18
**Câu (a).** Theo (2.1) cắt sau ba số hạng:

- $\gamma=\tfrac12$: $0+\tfrac12\cdot2+\tfrac14\cdot2=\tfrac32$;
- $\gamma=0$: $G_0^{[3]}=0$;
- $\gamma=0{,}9$: $0+0{,}9\cdot2+0{,}81\cdot2=3{,}42$.

Với $\gamma=0$, chỉ $R_1=0$ được tính, nên lợi tức bằng $0$ dù hai bước sau cho $2$.

**Câu (b).** $M=\max\{3,0,1,2\}=3$. Phần đuôi $D=\sum_{j\ge3}\gamma^jR_{j+1}$ thỏa $\lvert D\rvert\le\gamma^3\sum_{i\ge0}\gamma^iM=\gamma^3M/(1-\gamma)=\tfrac18\cdot6=\tfrac34$. Vì $G_0=\tfrac32+D$,

$$
G_0\in\bigl[\tfrac32-\tfrac34,\ \tfrac32+\tfrac34\bigr]=\bigl[\tfrac34,\ \tfrac94\bigr].
$$

**Câu (c).** Mỗi số hạng của phần đuôi nằm giữa $\gamma^j\cdot(-3)$ và $\gamma^j\cdot2$, nên

$$
\begin{aligned}
D&\ge\gamma^3\cdot\frac{-3}{1-\gamma}=-\tfrac34,\\
D&\le\gamma^3\cdot\frac{2}{1-\gamma}=\tfrac12 .
\end{aligned}
$$

Do đó $G_0\in\bigl[\tfrac34,\ 2\bigr]$, hẹp hơn câu (b) ở đầu trên vì phần thưởng lớn nhất là $2<M=3$.

**Câu (d).** Với $\gamma=\tfrac12$: $M/(1-\gamma)=6$, cần $6\cdot2^{-K}\le0{,}1$, tức $2^K\ge60$; $2^5=32$, $2^6=64$, nên $K=6$ (cận bằng $0{,}09375$). Với $\gamma=0{,}9$: $M/(1-\gamma)=30$, cần $0{,}9^K\le\tfrac1{300}$, tức $K\ge\ln300/\ln(10/9)\approx54{,}1$, nên $K=55$ (cận $\approx0{,}0913$, còn $K=54$ cho $\approx0{,}1014$). Khoảng của câu (b) với $\gamma=0{,}9$ có bán kính $0{,}9^3\cdot30=21{,}87$:

$$
\begin{aligned}
G_0&\in[3{,}42-21{,}87;\ 3{,}42+21{,}87]\\
&=[-18{,}45;\ 25{,}29].
\end{aligned}
$$

**Kiểm tra lại.** Với $\gamma=\tfrac12$, các khoảng của câu (b), (c) chứa lợi tức cắt $\tfrac32$ (ứng với phần đuôi bằng $0$) và nằm trong $[-6,6]$ của Ví dụ 03.8. Với $\gamma=0{,}9$, khoảng của câu (d) chứa lợi tức cắt $3{,}42$ và nằm trong $[-30,30]$, cận $M/(1-\gamma)$ ứng với $\gamma=0{,}9$. Số $K$ tăng từ $6$ lên $55$ khi $\gamma$ tăng từ $\tfrac12$ lên $0{,}9$: với $\gamma$ gần $1$, ba phần thưởng đã biết hầu như không thu hẹp khoảng của $G_0$. Ba lỗi thường gặp: chặn phần đuôi bằng $M/(1-\gamma)$ mà quên thừa số $\gamma^3$, được $[-\tfrac92,\tfrac{15}2]$ thay vì $[\tfrac34,\tfrac94]$; viết trọng số của $R_3$ là $\gamma^3$ thay cho $\gamma^2$, được $\tfrac54$ thay vì $\tfrac32$ khi $\gamma=\tfrac12$; coi cận $6$ là giá trị của $G_0$.
:::

### Bài tập 03.4. Kỳ vọng hai bước từ pin thấp

**Mức độ:** tính toán; mục tiêu học tập 3.

**Nguồn:** ghi chú bài giảng, Bài tập 03.4 (tiểu mục 3.3), giữ số hiệu, đề và lời giải.

**Trùng trang chiếu:** [Bài tập: mô hình, chính sách và giá trị](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/9) và [trang lời giải](lecture-03-qua-trinh-quyet-dinh-markov.html#/4/10): câu (b) của trang là câu (a), (b) của bài; câu (c) của trang là câu (c) của bài.

::: exercise Bài tập 03.4 (Kỳ vọng hai bước từ pin thấp)
**Dữ kiện.** Robot thu gom lon hai mức pin ($\mathrm L$–Chờ: $(\mathrm L,1)$ chắc chắn; $\mathrm L$–Sạc: $(\mathrm H,0)$ chắc chắn; $\mathrm H$–Tìm: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$). Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$. $\gamma=1/2$, $S_0=\mathrm L$.

**Yêu cầu.** (a) Liệt kê các nhánh hai bước từ $\mathrm L$, ghi xác suất và giá trị $G_0^{[2]}=R_1+\gamma R_2$ của mỗi nhánh, rồi tính $\mathbb E_\pi[G_0^{[2]}\mid S_0=\mathrm L]$. (b) Kiểm tra kết quả bằng cách lấy trung bình hai kết quả thí nghiệm Chờ ($5/4$) và Sạc ($1$) của Ví dụ 03.11 theo trọng số chính sách. (c) Giải thích vì sao kết quả câu (a) chưa phải $v_\pi(\mathrm L)$.
:::

::: hint Gợi ý Bài tập 03.4
Sau Chờ, robot ở $\mathrm L$ và lại chọn Chờ hoặc Sạc; sau Sạc, robot ở $\mathrm H$ và chọn Tìm.
:::

::: solution Lời giải Bài tập 03.4
**Câu (a).** Có ba nhánh.

- Chờ rồi Chờ: xác suất $\tfrac12\cdot\tfrac12=\tfrac14$, $G_0^{[2]}=1+\tfrac12\cdot1=\tfrac32$.
- Chờ rồi Sạc: xác suất $\tfrac14$, $G_0^{[2]}=1+\tfrac12\cdot0=1$.
- Sạc rồi Tìm: xác suất $\tfrac12\cdot1=\tfrac12$, $G_0^{[2]}=0+\tfrac12\cdot2=1$.

Kỳ vọng:

$$
\begin{aligned}
&\mathbb E_\pi\bigl[G_0^{[2]}\mid S_0=\mathrm L\bigr]\\
&\quad=\tfrac14\cdot\tfrac32+\tfrac14\cdot1+\tfrac12\cdot1\\
&\quad=\tfrac38+\tfrac28+\tfrac48=\tfrac98 .
\end{aligned}
$$

**Câu (b).** $\tfrac12\cdot\tfrac54+\tfrac12\cdot1=\tfrac58+\tfrac48=\tfrac98$, trùng câu (a). Thí nghiệm Tìm không đóng góp vì $\pi(\mathrm{tim}\mid\mathrm L)=0$.

**Câu (c).** $\tfrac98$ chỉ là kỳ vọng của hai số hạng đầu; $v_\pi(\mathrm L)$ còn chứa phần $\gamma^2R_3+\gamma^3R_4+\cdots$.

**Kiểm tra lại.** Ba xác suất cộng lại bằng $\tfrac14+\tfrac14+\tfrac12=1$. Hai lỗi thường gặp: lệch trọng số một bậc, dùng $\gamma R_1+\gamma^2R_2$, được $\tfrac9{16}$ thay vì $\tfrac98$; bỏ sót nhánh Chờ rồi Sạc, ba xác suất chỉ còn tổng $\tfrac34$ và kỳ vọng thành $\tfrac78$.
:::

### Bài tập 03.6. Phương trình Bellman tại pin cao

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** ghi chú bài giảng, Bài tập 03.6 (tiểu mục 4.5), giữ số hiệu, đề và lời giải.

**Trùng trang chiếu:** [Bài tập: phương trình Bellman tại pin cao](lecture-03-qua-trinh-quyet-dinh-markov.html#/5/12); đề và lời giải ở cùng trang, lời giải hiện theo bước.

::: exercise Bài tập 03.6 (Phương trình Bellman tại pin cao)
**Dữ kiện.** Robot thu gom lon hai mức pin: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $1/2$. Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm. $\gamma=1/2$. Viết $v_{\mathrm H}=v_\pi(\mathrm H)$, $v_{\mathrm L}=v_\pi(\mathrm L)$. Định lý 03.21 cho phương trình (4.5): $v_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr]$.

**Yêu cầu.** Từ Định lý 03.21, chứng minh $v_{\mathrm H}=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$, chỉ rõ mỗi hệ số đến từ $\pi$, từ $p$ hay từ $\gamma$.
:::

::: hint Gợi ý Bài tập 03.6
Ở $\mathrm H$, tổng theo hành động chỉ còn một số hạng; tổng theo phản hồi có hai số hạng.
:::

::: solution Lời giải Bài tập 03.6
Áp dụng (4.5) tại $s=\mathrm H$. Tổng theo $a$ chỉ còn $a=\mathrm{tim}$ với $\pi(\mathrm{tim}\mid\mathrm H)=1$, vì $\pi(\mathrm{cho}\mid\mathrm H)=0$. Cặp $(\mathrm H,\mathrm{tim})$ có hai phản hồi $(\mathrm H,2)$ và $(\mathrm L,2)$, mỗi phản hồi $p=1/2$. Viết (4.5) tại $\mathrm H$ rồi khai triển:

$$
\begin{aligned}
v_{\mathrm H}&=1\cdot\Bigl(\tfrac12\bigl[2+\tfrac12v_{\mathrm H}\bigr]\\
&\qquad+\tfrac12\bigl[2+\tfrac12v_{\mathrm L}\bigr]\Bigr)\\
&=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}.
\end{aligned}
$$

Hệ số $1$ ngoài cùng là $\pi(\mathrm{tim}\mid\mathrm H)$; hai hệ số $\tfrac12$ ngoài ngoặc vuông là $p(\mathrm H,2\mid\mathrm H,\mathrm{tim})$ và $p(\mathrm L,2\mid\mathrm H,\mathrm{tim})$; hệ số $\tfrac12$ trước $v_{\mathrm H}$, $v_{\mathrm L}$ trong ngoặc là $\gamma$. Mỗi hệ số $\tfrac14$ là tích $p\cdot\gamma$.

**Kiểm tra lại.** Số hạng tự do $2$ là $r(\mathrm H,\mathrm{tim})$ theo Bài tập 03.2, đúng dạng thứ hai của (4.6) nhân với $\pi(\mathrm{tim}\mid\mathrm H)=1$. Hai lỗi thường gặp: bỏ $\gamma$ trước giá trị của trạng thái kế tiếp, được $v_{\mathrm H}=2+\tfrac12v_{\mathrm H}+\tfrac12v_{\mathrm L}$, tức phương trình của $\gamma=1$ (Bài tập 03.23); giữ số hạng của Chờ ở $\mathrm H$ với trọng số $\tfrac12$, được $v_{\mathrm H}=\tfrac32+\tfrac38v_{\mathrm H}+\tfrac18v_{\mathrm L}$, phương trình của một chính sách khác.
:::

### Bài tập 03.7. Chỗ dùng tính Markov

**Mức độ:** chứng minh; mục tiêu học tập 4.

**Nguồn:** ghi chú bài giảng, Bài tập 03.7 (tiểu mục 4.5), giữ số hiệu, đề và lời giải; Bài tập tuần 2 (2025–2026), bài 7–8.

**Trùng trang chiếu:** [Bài tập: chỗ dùng tính Markov](lecture-03-qua-trinh-quyet-dinh-markov.html#/5/11); trang chỉ có đề, lời giải nằm trong ghi chú diễn giả của trang và cho cùng kết luận.

::: exercise Bài tập 03.7 (Chỗ dùng tính Markov)
**Dữ kiện.** MDP hữu hạn, chính sách Markov dừng $\pi$, phần thưởng bị chặn, $0\le\gamma<1$. Chuỗi kết quả dẫn tới Hệ quả 03.24 có ba bước:

- Bổ đề 03.20(b): nếu tác tử theo $\pi$ từ thời điểm $t$ và lịch sử $h_t$ kết thúc ở $s$, thì $\mathbb E_\pi[G_t\mid H_t=h_t]=v_\pi(s)$. Chứng minh đồng nhất xác suất của đoạn quỹ đạo sau $h_t$ với xác suất của quá trình xuất phát tại $s$ (Mệnh đề 03.14).
- Mệnh đề 03.22 và 03.23: $q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr]$ và $v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a)$. Chứng minh tách bước đầu, lấy trọng số $p(s',r\mid s,a)$ cho phản hồi đầu, rồi thay kỳ vọng của phần tương lai bằng Bổ đề 03.20.
- Hệ quả 03.24: thế Mệnh đề 03.23 tại $s'$ vào Mệnh đề 03.22.

Trạng thái thiếu phòng làm việc (ghi chú, Ví dụ 03.4; số liệu sư phạm tự xây dựng): robot luôn ở pin thấp và chỉ Chờ, làm việc luân phiên ở phòng 1 và phòng 2; Chờ ở phòng 1 cho phần thưởng $1$, ở phòng 2 cho $0$; phòng lúc $t=0$ được chọn ngẫu nhiên, mỗi phòng xác suất $\tfrac12$; trạng thái chỉ ghi mức pin, nên luôn bằng $\mathrm L$. Tại $t=1$, hai lịch sử $(\mathrm L,\mathrm{cho},1,\mathrm L)$ và $(\mathrm L,\mathrm{cho},0,\mathrm L)$ cho phần thưởng bước sau chắc chắn bằng $0$ và $1$.

**Yêu cầu.** Trong chuỗi lập luận dẫn tới Hệ quả 03.24 (Bổ đề 03.20, Mệnh đề 03.22, 03.23), chỉ ra (a) bước dùng tính Markov của trạng thái, và điều gì sai ở bước đó nếu trạng thái thiếu thông tin như ở Ví dụ 03.4; (b) bước dùng tính dừng của chính sách, và điều gì sai ở bước đó nếu robot đổi quy tắc chọn theo thời điểm chẵn, lẻ.
:::

::: hint Gợi ý Bài tập 03.7
Hệ quả 03.24 thế Mệnh đề 03.23 vào Mệnh đề 03.22; Mệnh đề 03.22 dựa trên Bổ đề 03.20(b), và chứng minh của bổ đề này gọi Mệnh đề 03.14 cho hai quá trình khác nhau.
:::

::: solution Lời giải Bài tập 03.7
**Câu (a).** Tính Markov của trạng thái được dùng ở Bước 1 của chứng minh Bổ đề 03.20 (qua Mệnh đề 03.14), rồi đi vào Bước 1 của Mệnh đề 03.22, nơi $\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]$ được thay bằng $v_\pi(s')$. Ở Ví dụ 03.4, hai lịch sử kết thúc ở $\mathrm L$ cho hai phân phối phần thưởng khác nhau ở bước sau, nên hai kỳ vọng của phần tương lai không thể cùng bằng $v_\pi(\mathrm L)$. Tính Markov một bước còn nằm trong trọng số $p(s',r\mid s,a)$ của phản hồi đầu ở Bước 1 của Mệnh đề 03.22, như ở Bổ đề 03.19(b). Trọng số này do quy tắc sinh quỹ đạo của Định nghĩa 03.7 cho; cùng quy tắc đó cho các thừa số $p$ trong (3.2). Ở Ví dụ 03.4 quy tắc này hỏng, nên không có hàm $p$ chung không phụ thuộc lịch sử.

**Câu (b).** Tính dừng của chính sách cũng được dùng ở Bước 1 của Bổ đề 03.20: tích (3.2) tại thời điểm $t$ trùng tích của quá trình xuất phát tại $s$ vì cùng hàm $\pi$ dùng ở thời điểm $t+i$ và $i$. Nếu robot Chờ ở bước chẵn và Sạc ở bước lẻ, tương lai từ $\mathrm L$ ở thời điểm lẻ khác tương lai từ $\mathrm L$ ở thời điểm $0$, nên đẳng thức này sai.

**Kiểm tra lại.** Mệnh đề 03.23 chỉ dùng (4.3) tại $t=0$ với $h_0=(s)$, nơi không có lịch sử để bỏ, và Bổ đề 03.20(d); cả hai giả thiết đi vào Mệnh đề 03.23 qua Bổ đề 03.20. Lỗi thường gặp: cho rằng hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ (Bổ đề 03.18) dùng tính Markov; đó là đẳng thức trên từng quỹ đạo (Nhận xét 03.25). Lỗi này dẫn tới kết luận sai rằng ở Ví dụ 03.4 hệ thức đệ quy của lợi tức cũng hỏng.
:::

### Bài tập 03.19. Phương trình Bellman cho giá trị hành động của robot

**Mức độ:** tính toán; mục tiêu học tập 4.

**Nguồn:** Sutton và Barto (2018), bài tập 3.17, tr. 61; Bài tập tuần 2 (2025–2026), bài 7–8; ghi chú Hệ quả 03.24. Phương trình ở trang [Phương trình Bellman kỳ vọng cho giá trị hành động](lecture-03-qua-trinh-quyet-dinh-markov.html#/5/10).

::: exercise Bài tập 03.19 (Phương trình Bellman cho giá trị hành động của robot)
Robot thu gom lon hai mức pin có bảng phản hồi: $(\mathrm H,\mathrm{tim})\to(\mathrm H,2)$ hoặc $(\mathrm L,2)$, mỗi nhánh $1/2$; $(\mathrm H,\mathrm{cho})\to(\mathrm H,1)$; $(\mathrm L,\mathrm{tim})\to(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi nhánh $1/2$; $(\mathrm L,\mathrm{cho})\to(\mathrm L,1)$; $(\mathrm L,\mathrm{sac})\to(\mathrm H,0)$. Chính sách chia đều tại pin thấp: $\pi(\mathrm{tim}\mid\mathrm H)=1$, $\pi(\mathrm{cho}\mid\mathrm H)=0$, $\pi(\mathrm{tim}\mid\mathrm L)=0$, $\pi(\mathrm{cho}\mid\mathrm L)=\pi(\mathrm{sac}\mid\mathrm L)=\tfrac12$; $\gamma=\tfrac12$. Viết $q_{s,a}=q_\pi(s,a)$.

- (a) Viết phương trình (4.8) cho cả năm cặp hợp lệ, chỉ dùng các ẩn $q_{s,a}$.
- (b) Chứng tỏ ba phương trình của các cặp $(\mathrm H,\mathrm{tim})$, $(\mathrm L,\mathrm{cho})$, $(\mathrm L,\mathrm{sac})$ chỉ chứa ba ẩn của chính các cặp đó; giải hệ ba ẩn này.
- (c) Tính hai giá trị còn lại $q_{\mathrm H,\mathrm{cho}}$, $q_{\mathrm L,\mathrm{tim}}$, rồi suy ra $v_\pi(\mathrm H)$, $v_\pi(\mathrm L)$ theo (4.7).
:::

::: hint Gợi ý Bài tập 03.19
Tổng trong ngoặc của (4.8) tại $s'=\mathrm H$ là $q_{\mathrm H,\mathrm{tim}}$, tại $s'=\mathrm L$ là $\tfrac12(q_{\mathrm L,\mathrm{cho}}+q_{\mathrm L,\mathrm{sac}})$. Ở câu (b), phương trình của Sạc cho $q_{\mathrm L,\mathrm{sac}}$ theo $q_{\mathrm H,\mathrm{tim}}$.
:::

::: solution Lời giải Bài tập 03.19
**Câu (a).** Đặt $m_{\mathrm H}=q_{\mathrm H,\mathrm{tim}}$ và $m_{\mathrm L}=\tfrac12(q_{\mathrm L,\mathrm{cho}}+q_{\mathrm L,\mathrm{sac}})$, tức tổng $\sum_{a'}\pi(a'\mid s')q_\pi(s',a')$ tại $s'=\mathrm H$ và $s'=\mathrm L$. Theo (4.8):

$$
\begin{aligned}
q_{\mathrm H,\mathrm{tim}}&=\tfrac12\bigl[2+\tfrac12m_{\mathrm H}\bigr]\\
&\qquad+\tfrac12\bigl[2+\tfrac12m_{\mathrm L}\bigr],\\
q_{\mathrm H,\mathrm{cho}}&=1+\tfrac12m_{\mathrm H},\\
q_{\mathrm L,\mathrm{tim}}&=\tfrac12\bigl[2+\tfrac12m_{\mathrm L}\bigr]\\
&\qquad+\tfrac12\bigl[-3+\tfrac12m_{\mathrm H}\bigr],\\
q_{\mathrm L,\mathrm{cho}}&=1+\tfrac12m_{\mathrm L},\\
q_{\mathrm L,\mathrm{sac}}&=0+\tfrac12m_{\mathrm H}.
\end{aligned}
$$

**Câu (b).** Vế phải chỉ chứa $m_{\mathrm H}$, $m_{\mathrm L}$, tức chỉ chứa $q_{\mathrm H,\mathrm{tim}}$, $q_{\mathrm L,\mathrm{cho}}$, $q_{\mathrm L,\mathrm{sac}}$; hai ẩn $q_{\mathrm H,\mathrm{cho}}$, $q_{\mathrm L,\mathrm{tim}}$ có trọng số chính sách bằng $0$. Đặt $x=q_{\mathrm H,\mathrm{tim}}$, $y=q_{\mathrm L,\mathrm{cho}}$, $z=q_{\mathrm L,\mathrm{sac}}$. Ba phương trình là

$$
\begin{aligned}
x&=2+\tfrac14x+\tfrac18(y+z),\\
y&=1+\tfrac14(y+z),\\
z&=\tfrac12x .
\end{aligned}
$$

Thế $z=\tfrac12x$ vào phương trình thứ hai: $\tfrac34y=1+\tfrac18x$, nên $y=\tfrac43+\tfrac16x$. Thế $y$, $z$ vào phương trình thứ nhất rồi gom số hạng:

$$
\begin{aligned}
x&=2+\tfrac14x+\tfrac18\bigl(\tfrac43+\tfrac16x+\tfrac12x\bigr)\\
&=\tfrac{13}6+\tfrac13x,
\end{aligned}
$$

nên $\tfrac23x=\tfrac{13}6$ và $x=\tfrac{13}4$. Suy ra $z=\tfrac{13}8$ và $y=\tfrac43+\tfrac{13}{24}=\tfrac{15}8$.

**Câu (c).** Với $m_{\mathrm H}=\tfrac{13}4$ và $m_{\mathrm L}=\tfrac12\bigl(\tfrac{15}8+\tfrac{13}8\bigr)=\tfrac74$:

$$
\begin{aligned}
q_{\mathrm H,\mathrm{cho}}&=1+\tfrac12\cdot\tfrac{13}4=\tfrac{21}8,\\
q_{\mathrm L,\mathrm{tim}}&=\tfrac12\bigl[2+\tfrac78\bigr]+\tfrac12\bigl[-3+\tfrac{13}8\bigr]\\
&=\tfrac{23}{16}-\tfrac{11}{16}=\tfrac34 .
\end{aligned}
$$

Theo (4.7), $v_\pi(\mathrm H)=1\cdot\tfrac{13}4+0\cdot\tfrac{21}8=\tfrac{13}4$ và $v_\pi(\mathrm L)=0\cdot\tfrac34+\tfrac12\cdot\tfrac{15}8+\tfrac12\cdot\tfrac{13}8=\tfrac74$, trùng Ví dụ 03.14.

**Kiểm tra lại.** Năm giá trị trùng Ví dụ 03.15 và Bài tập 03.11 của ghi chú. Hệ (4.8) có năm ẩn, nhiều hơn hai ẩn của (4.5), nhưng chỉ ba ẩn của các cặp được chọn với xác suất dương liên kết với nhau. Hai lỗi thường gặp: dùng trọng số $\pi(a\mid s)$ của hành động hiện tại trong ngoặc thay cho $\pi(a'\mid s')$ của trạng thái kế tiếp, khi đó phương trình của $(\mathrm H,\mathrm{cho})$ mất phần tương lai vì $\pi(\mathrm{cho}\mid\mathrm H)=0$ và cho $q_{\mathrm H,\mathrm{cho}}=1$ thay vì $\tfrac{21}8$; cộng cả $q_{\mathrm L,\mathrm{tim}}$ vào $m_{\mathrm L}$ với trọng số $\tfrac13$, tức giải hệ của chính sách chọn đều ba hành động ở $\mathrm L$ chứ không phải của $\pi$.
:::

### Bài tập 03.20. Hệ Bellman của một quá trình ba trạng thái có trạng thái hấp thụ

**Mức độ:** tính toán; mục tiêu học tập 2 và 5.

**Nguồn:** Bài tập tuần 2 (2025–2026), bài 3 (đề gốc gồm câu (a), (b)); câu (c)–(e) bổ sung. Định lý dùng ở trang [Nghiệm duy nhất của hệ đánh giá chính sách](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/9).

::: exercise Bài tập 03.20 (Hệ Bellman của một quá trình ba trạng thái có trạng thái hấp thụ)
Một quá trình phần thưởng Markov (Markov reward process, MRP) có ba trạng thái $\mathrm s_1,\mathrm s_2,\mathrm s_3$, xếp theo thứ tự đó, với ma trận chuyển và véc-tơ thưởng kỳ vọng một bước

$$
P=\begin{pmatrix}0{,}5&0{,}5&0\\0{,}2&0{,}3&0{,}5\\0&0&1\end{pmatrix},
$$

$$
R=\begin{pmatrix}1\\-1\\0\end{pmatrix},\qquad\gamma=0{,}9 .
$$

Thành phần $R_i$ là thưởng kỳ vọng của bước rời trạng thái $\mathrm s_i$, đóng vai trò của $r_\pi$ trong ghi chú (5.2); $P$ đóng vai trò của $P_\pi$.

- (a) Kiểm tra $P$ là ma trận chuyển hợp lệ và xác định trạng thái hấp thụ.
- (b) Viết hệ phương trình Bellman cho véc-tơ giá trị $v=(v_1,v_2,v_3)$.
- (c) Giải hệ, cho nghiệm dạng phân số và dạng thập phân làm tròn tới ba chữ số thập phân, và kiểm tra lại.
- (d) Với $\gamma=1$, chứng tỏ hệ ba ẩn $(I-P)v=R$ có vô số nghiệm. Coi $\mathrm s_3$ là trạng thái kết thúc với quy ước $v_3=0$ (Nhận xét 03.10), giải hệ hai ẩn còn lại.
- (e) Giả sử phần thưởng thực nhận khi rời $\mathrm s_i$ đúng bằng $R_i$. Với $\gamma=0{,}9$, một lượt mẫu đi qua $\mathrm s_1\to\mathrm s_1\to\mathrm s_2\to\mathrm s_3$ và nhận các phần thưởng $1$, $1$, $-1$; sau đó quá trình ở lại $\mathrm s_3$ với phần thưởng $0$. Tính lùi $G_2$, $G_1$, $G_0$ theo $G_t=R_{t+1}+\gamma G_{t+1}$ (ghi chú, Bổ đề 03.18), tính xác suất của lượt này, và so $G_0$ với $v_1$ của câu (c).
:::

::: hint Gợi ý Bài tập 03.20
Phương trình của $\mathrm s_3$ chỉ chứa $v_3$; giải nó trước. Nhân hai phương trình còn lại với $100$ để có hệ số nguyên. Ở câu (e), lượt tới $\mathrm s_3$ tại $T=3$, nên bắt đầu từ $G_3=0$.
:::

::: solution Lời giải Bài tập 03.20
**Câu (a).** Mọi phần tử của $P$ không âm. Tổng của ba hàng lần lượt là $0{,}5+0{,}5+0=1$; $0{,}2+0{,}3+0{,}5=1$; $0+0+1=1$. Vậy $P$ là ma trận chuyển hợp lệ. Hàng thứ ba có $P_{33}=1$: từ $\mathrm s_3$ quá trình ở lại $\mathrm s_3$ với xác suất $1$, nên $\mathrm s_3$ là trạng thái hấp thụ; thưởng kỳ vọng tại đó bằng $0$, như quy ước trạng thái hấp thụ của Nhận xét 03.10.

**Câu (b).** Phương trình $v=R+\gamma Pv$ (Mệnh đề 03.27) viết theo từng thành phần:

$$
\begin{aligned}
v_1&=1+0{,}9\,(0{,}5\,v_1+0{,}5\,v_2),\\
v_2&=-1+0{,}9\,(0{,}2\,v_1+0{,}3\,v_2\\
&\qquad+0{,}5\,v_3),\\
v_3&=0+0{,}9\,v_3 .
\end{aligned}
$$

**Câu (c).** Phương trình thứ ba cho $0{,}1\,v_3=0$, nên $v_3=0$. Khai triển hai phương trình đầu và nhân với $100$:

$$
\begin{aligned}
55\,v_1-45\,v_2&=100,\\
-18\,v_1+73\,v_2&=-100 .
\end{aligned}
$$

Phương trình thứ nhất cho $v_1=\tfrac{20+9v_2}{11}$. Thế vào phương trình thứ hai và nhân với $11$: $-360-162\,v_2+803\,v_2=-1100$, nên $641\,v_2=-740$. Suy ra

$$
\begin{aligned}
v_2&=-\tfrac{740}{641}\approx-1{,}154,\\
v_1&=\tfrac{20+9\cdot(-740/641)}{11}\\
&=\tfrac{560}{641}\approx0{,}874,\\
v_3&=0 .
\end{aligned}
$$

Kiểm tra: $1+0{,}45\cdot\tfrac{560-740}{641}=1-\tfrac{81}{641}=\tfrac{560}{641}$ và $-1+0{,}9\cdot\tfrac{0{,}2\cdot560-0{,}3\cdot740}{641}=-1-\tfrac{99}{641}=-\tfrac{740}{641}$. Theo Định lý 03.28, với $\gamma=0{,}9<1$ đây là nghiệm duy nhất: $v\approx(0{,}874;\,-1{,}154;\,0)$.

**Câu (d).** Với $\gamma=1$, hàng thứ ba của $(I-P)v=R$ là $0\cdot v_3=0$, đúng với mọi $v_3$. Hai hàng đầu là $0{,}5\,v_1-0{,}5\,v_2=1$ và $-0{,}2\,v_1+0{,}7\,v_2-0{,}5\,v_3=-1$. Với $v_3=c$ tùy ý, hàng đầu cho $v_1=2+v_2$; thế vào hàng thứ hai được $0{,}5\,v_2=-0{,}6+0{,}5\,c$. Vậy mọi véc-tơ

$$
\begin{aligned}
v&=(0{,}8;\,-1{,}2;\,0)\\
&\quad+c\,(1;\,1;\,1),
\end{aligned}
$$

với $c\in\mathbb R$, là nghiệm: hệ có vô số nghiệm và $I-P$ không khả nghịch, vì $(I-P)\mathbf 1=0$. Khi coi $\mathrm s_3$ là trạng thái kết thúc, $v_3=0$ và còn hệ hai ẩn với ma trận $\begin{pmatrix}0{,}5&-0{,}5\\-0{,}2&0{,}7\end{pmatrix}$, định thức $0{,}35-0{,}1=0{,}25\ne0$; nghiệm duy nhất là $(v_1,v_2)=(0{,}8;\,-1{,}2)$.

**Câu (e).** Lượt tới $\mathrm s_3$ sau ba bước và mọi phần thưởng sau đó bằng $0$, nên $G_3=0$. Tính lùi theo $G_t=R_{t+1}+\gamma G_{t+1}$:

$$
\begin{aligned}
G_2&=-1+0{,}9\cdot0=-1,\\
G_1&=1+0{,}9\cdot(-1)=0{,}1,\\
G_0&=1+0{,}9\cdot0{,}1=1{,}09 .
\end{aligned}
$$

Kiểm tra trực tiếp: $1+0{,}9\cdot1+0{,}81\cdot(-1)=1{,}09$. Lượt có xác suất $P_{11}P_{12}P_{23}=0{,}5\cdot0{,}5\cdot0{,}5=0{,}125$. Giá trị $G_0=1{,}09$ khác $v_1\approx0{,}874$ vì $G_0$ là lợi tức của một lượt, còn $v_1$ là kỳ vọng của $G_0$ trên mọi lượt xuất phát từ $\mathrm s_1$; phương pháp Monte Carlo của Bài 05 ước lượng $v_1$ bằng trung bình của nhiều giá trị $G_0$ như vậy.

**Kiểm tra lại.** Ở câu (d), từ $\mathrm s_1$ hoặc $\mathrm s_2$, trong hai bước quá trình tới $\mathrm s_3$ với xác suất ít nhất $0{,}5\cdot0{,}5=0{,}25$, nên xác suất chưa tới $\mathrm s_3$ sau $2k$ bước không quá $0{,}75^k\to0$. Đây là trường hợp "mọi trạng thái bảo đảm đi tới kết thúc" mà Sutton và Barto (2018, §4.1, tr. 74) nêu; Định lý 03.28 của ghi chú không chứng minh trường hợp đó. Kiểm tra bằng số lần ghé kỳ vọng: nghịch đảo của ma trận hệ hai ẩn là $\begin{pmatrix}2{,}8&2\\0{,}8&2\end{pmatrix}$, nên từ $\mathrm s_1$ tổng phần thưởng kỳ vọng là $2{,}8\cdot1+2\cdot(-1)=0{,}8$. Ba lỗi thường gặp: đặt $v=R+Pv$ mà quên $\gamma$, tức giải hệ $\gamma=1$ của câu (d) và gặp vô số nghiệm; kết luận chung rằng với $\gamma=1$ hệ vô nghiệm, trong khi hệ ba ẩn ở đây có vô số nghiệm, hệ của robot ở Bài tập 03.23 vô nghiệm, và hệ hai ẩn sau khi coi $\mathrm s_3$ là trạng thái kết thúc có nghiệm duy nhất; ở câu (e) bắt đầu tính lùi từ $G_2=0$ thay vì $G_3=0$, được $G_0=1{,}9$.
:::

### Bài tập 03.21. Quá trình phần thưởng Markov cảm sinh bởi một chính sách cố định

**Mức độ:** chứng minh; mục tiêu học tập 5.

**Nguồn:** Bài tập tuần 2 (2025–2026), bài 4; ghi chú Định nghĩa 03.26 và câu "dãy trạng thái dưới $\pi$ vẫn có tính Markov" sau định nghĩa đó. Phép gộp ở trang [Chuỗi Markov và quá trình phần thưởng Markov cảm sinh](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/7).

::: exercise Bài tập 03.21 (Quá trình phần thưởng Markov cảm sinh bởi một chính sách cố định)
Cho MDP hữu hạn $\bigl(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p\bigr)$ với tập trạng thái chưa kết thúc $\mathcal S$, và chính sách Markov dừng $\pi$ được tuân theo ở mọi thời điểm. Với $s,s'\in\mathcal S$ đặt

$$
\begin{aligned}
(P_\pi)_{ss'}&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,p(s'\mid s,a),\\
r_\pi(s)&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,r(s,a).
\end{aligned}
$$

Chứng minh các khẳng định sau.

- (a) $(P_\pi)_{ss'}\ge0$ và $\sum_{s'\in\mathcal S}(P_\pi)_{ss'}\le1$, với dấu bằng khi không có trạng thái kết thúc.
- (b) Với mọi $t$ và mọi dãy trạng thái $s_0,\dots,s_t$ có $s_t\in\mathcal S$ và $\Pr_\pi(S_0=s_0,\dots,S_t=s_t)>0$, ta có $\Pr_\pi(S_{t+1}=s'\mid S_0=s_0,\dots,S_t=s_t)=(P_\pi)_{s_ts'}$ với mọi $s'\in\mathcal S$; tức dãy trạng thái dưới $\pi$ là một chuỗi Markov thuần nhất theo thời gian, với ma trận chuyển $P_\pi$.
- (c) Với cùng điều kiện, $\mathbb E_\pi[R_{t+1}\mid S_0=s_0,\dots,S_t=s_t]=r_\pi(s_t)$.
- (d) Robot thu gom lon hai mức pin với chính sách chia đều tại pin thấp ($\pi(\mathrm{tim}\mid\mathrm H)=1$; $\pi(\mathrm{cho}\mid\mathrm L)=\pi(\mathrm{sac}\mid\mathrm L)=\tfrac12$), $\gamma=\tfrac12$, có $q_\pi(\mathrm L,\mathrm{tim})=\tfrac34$ khi Tìm từ $\mathrm L$ cho $(\mathrm L,2)$ hoặc $(\mathrm H,-3)$ mỗi phản hồi $\tfrac12$, và $q_\pi(\mathrm L,\mathrm{tim})=\tfrac{29}{16}$ khi hai phản hồi đó có xác suất $\tfrac34$ và $\tfrac14$ (ghi chú Ví dụ 03.15 và Bài tập 03.13). Trong cả hai MDP, các phản hồi khác như nhau: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $\tfrac12$; Chờ từ $\mathrm H$ cho $(\mathrm H,1)$; Chờ từ $\mathrm L$ cho $(\mathrm L,1)$; Sạc từ $\mathrm L$ cho $(\mathrm H,0)$. Giải thích vì sao hai MDP này cảm sinh cùng một MRP $(\mathcal S,P_\pi,r_\pi,\gamma)$, và rút ra thông tin nào của MDP bị mất khi chuyển sang MRP.
:::

::: hint Gợi ý Bài tập 03.21
Ở câu (b), sự kiện $\{S_0=s_0,\dots,S_t=s_t\}$ là hợp rời của các sự kiện $\{H_t=h_t\}$, với $h_t$ chạy trên các lịch sử có đúng các trạng thái đó và hành động, phần thưởng tùy ý. Với mỗi $h_t$, dùng Mệnh đề 03.14 với $K=1$, rồi lấy trung bình theo $h_t$.
:::

::: solution Lời giải Bài tập 03.21
**Câu (a).** Mỗi số hạng $\pi(a\mid s)\,p(s'\mid s,a)$ không âm, nên $(P_\pi)_{ss'}\ge0$. Ta có

$$
\begin{aligned}
&\sum_{s'\in\mathcal S}(P_\pi)_{ss'}\\
&\quad=\sum_a\pi(a\mid s)\sum_{s'\in\mathcal S}p(s'\mid s,a)\\
&\quad\le\sum_a\pi(a\mid s)\sum_{s'\in\mathcal S^+}p(s'\mid s,a)\\
&\quad=\sum_a\pi(a\mid s)=1 .
\end{aligned}
$$

Đẳng thức đầu đổi thứ tự hai tổng hữu hạn. Bất đẳng thức thêm các trạng thái kết thúc, mỗi số hạng thêm vào không âm. Hai đẳng thức cuối dùng $\sum_{s'\in\mathcal S^+}p(s'\mid s,a)=1$ (Mệnh đề 03.6) và Định nghĩa 03.13. Khi $\mathcal S^+=\mathcal S$, dòng thứ hai là đẳng thức.

**Câu (b).** Gọi $\mathcal H$ là tập các lịch sử $h_t=(s_0,a_0,r_1,s_1,\dots,r_t,s_t)$ có đúng các trạng thái đã cho và $\Pr_\pi(H_t=h_t)>0$. Các sự kiện $\{H_t=h_t\}$, $h_t\in\mathcal H$, rời nhau, và hợp của chúng bằng $\{S_0=s_0,\dots,S_t=s_t\}$ sai khác một sự kiện xác suất $0$.

Với mỗi $h_t\in\mathcal H$, Mệnh đề 03.14 với $K=1$ cho $\Pr_\pi(A_t=a,R_{t+1}=r,S_{t+1}=s'\mid H_t=h_t)=\pi(a\mid s_t)\,p(s',r\mid s_t,a)$. Cộng theo $a$ và $r$:

$$
\begin{aligned}
&\Pr_\pi(S_{t+1}=s'\mid H_t=h_t)\\
&\quad=\sum_a\pi(a\mid s_t)\\
&\qquad\times\sum_rp(s',r\mid s_t,a)\\
&\quad=\sum_a\pi(a\mid s_t)\,p(s'\mid s_t,a)\\
&\quad=(P_\pi)_{s_ts'} .
\end{aligned}
$$

Đẳng thức đầu cộng các sự kiện rời nhau, đẳng thức thứ hai dùng (1.5), đẳng thức cuối là định nghĩa của $P_\pi$. Vế phải không phụ thuộc $h_t$. Theo công thức xác suất toàn phần trên các $h_t\in\mathcal H$, với trọng số $w(h_t)=\Pr_\pi(H_t=h_t\mid S_0=s_0,\dots,S_t=s_t)$ có tổng $1$,

$$
\begin{aligned}
&\Pr_\pi(S_{t+1}=s'\mid S_0=s_0,\dots,\\
&\qquad S_t=s_t)\\
&\quad=\sum_{h_t\in\mathcal H}w(h_t)\,(P_\pi)_{s_ts'}\\
&\quad=(P_\pi)_{s_ts'} .
\end{aligned}
$$

Xác suất này chỉ phụ thuộc $s_t$ và không phụ thuộc $t$, vì $\pi$ và $p$ là cùng một hàm ở mọi thời điểm. Vậy dãy trạng thái là chuỗi Markov thuần nhất theo thời gian, với ma trận chuyển $P_\pi$.

**Câu (c).** Với mỗi $h_t\in\mathcal H$, cùng phép cộng nhưng nhân với $r$:

$$
\begin{aligned}
&\mathbb E_\pi[R_{t+1}\mid H_t=h_t]\\
&\quad=\sum_a\pi(a\mid s_t)\\
&\qquad\times\sum_{s',r}r\,p(s',r\mid s_t,a)\\
&\quad=\sum_a\pi(a\mid s_t)\,r(s_t,a)\\
&\quad=r_\pi(s_t),
\end{aligned}
$$

trong đó đẳng thức thứ hai dùng (1.6). Lấy trung bình theo $h_t$ với các trọng số $w(h_t)$ như ở câu (b) được $\mathbb E_\pi[R_{t+1}\mid S_0=s_0,\dots,S_t=s_t]=r_\pi(s_t)$.

**Câu (d).** Hai MDP chỉ khác nhau ở cặp $(\mathrm L,\mathrm{tim})$, mà $\pi(\mathrm{tim}\mid\mathrm L)=0$; theo cùng lập luận như lời giải Bài tập 03.17(b), cặp này không góp vào $P_\pi$ và $r_\pi$. Vì vậy cả hai cho $P_\pi=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix}$, $r_\pi=(2;\,\tfrac12)$ và cùng $\gamma$, tức cùng một MRP, và cùng $v_\pi=(\tfrac{13}4,\tfrac74)$ theo Định lý 03.28. Hai giá trị $q_\pi(\mathrm L,\mathrm{tim})$ khác nhau, nên từ MRP không dựng lại được $q_\pi$. Phép gộp giữ lại các đại lượng trung bình theo $\pi$ và mất phản hồi của từng hành động, nhất là của hành động chính sách không chọn.

**Kiểm tra lại.** Với robot không có trạng thái kết thúc, mỗi hàng của $P_\pi$ có tổng $1$, đúng câu (a). Ba lỗi thường gặp: bỏ qua bước lấy trung bình theo lịch sử ở câu (b), nên chỉ chứng minh được đẳng thức khi biết $H_t=h_t$, chưa được khi chỉ biết dãy trạng thái; đưa cột của trạng thái kết thúc vào $P_\pi$, được ma trận cỡ $n\times(n+1)$ không dùng được trong (5.3); nghĩ rằng MRP cảm sinh còn đủ thông tin để so sánh các hành động, dẫn tới kết luận sai rằng hai MDP của câu (d) có cùng $q_\pi(\mathrm L,\mathrm{tim})$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 03.22. Vị trí xe trong CartPole không có tính Markov

**Mức độ:** vận dụng; mục tiêu học tập 1.

**Nguồn:** notebook thực hành Bài 04, `thuc-hanh-cartpole-quy-hoach-dong.ipynb`, phần 2 và mục 3.1 (bước thời gian $\tau=0{,}02$ giây), mục 7.1 (bộ tích phân Euler mặc định của Gymnasium cập nhật vị trí bằng vận tốc trước khi lực tác động); mã nguồn `CartPoleEnv.step` của Gymnasium (công thức gia tốc $\ddot x$, tham số mặc định: khối lượng xe $1$ kg, khối lượng cột $0{,}1$ kg, nửa chiều dài cột $0{,}5$ m, lực đẩy $10$ N); Sutton và Barto (2018), ví dụ 3.4, tr. 56; ghi chú Tình huống 03.2. Định nghĩa dùng ở trang [Tính Markov](lecture-03-qua-trinh-quyet-dinh-markov.html#/2/5).

::: exercise Bài tập 03.22 (Vị trí xe trong CartPole không có tính Markov)
Môi trường `CartPole-v1` của Gymnasium có trạng thái vật lý $(x,\dot x,\theta,\dot\theta)$: vị trí và vận tốc của xe, góc và vận tốc góc của cột; động lực tất định; hành động $0$ đẩy trái, $1$ đẩy phải. Bộ mô phỏng cập nhật theo phương pháp Euler với bước thời gian $\Delta t=0{,}02$ giây (notebook ký hiệu bước này là $\tau$):

$$
\begin{aligned}
x_{t+1}&=x_t+\Delta t\,\dot x_t,\\
\dot x_{t+1}&=\dot x_t+\Delta t\,\ddot x_t,
\end{aligned}
$$

trong đó gia tốc $\ddot x_t$ phụ thuộc $(\theta_t,\dot\theta_t)$ và hành động $A_t$. Giả thiết: ở mọi bước đang xét, $\lvert\ddot x_t\rvert\le10$ m/s²; với tham số mặc định của Gymnasium, điều này đúng khi $\lvert\theta\rvert\le12^\circ$ và $\lvert\dot\theta\rvert\le6$ rad/s. Một tác tử chỉ quan sát $x$ và dùng nó làm trạng thái. Vì $x$ là biến liên tục, tính Markov ở đây hiểu theo nghĩa của (1.2) cho phân phối có điều kiện: phân phối của $x_{t+1}$ khi biết toàn bộ lịch sử chỉ được phụ thuộc $x_t$ và $A_t$.

- (a) Chứng minh $x_{t+1}=2x_t-x_{t-1}+\Delta t^2\,\ddot x_{t-1}$.
- (b) Xét hai lịch sử cùng kết thúc ở $x_t=0{,}10$ m, một lịch sử có $x_{t-1}=0{,}09$ m, lịch sử kia có $x_{t-1}=0{,}11$ m. Với mỗi lịch sử, xác định vận tốc $\dot x_{t-1}$ và một khoảng chứa $x_{t+1}$; kết luận về tính Markov của trạng thái $x$.
- (c) Nêu một biểu diễn trạng thái có tính Markov, và giải thích vì sao cặp $(x_{t-1},x_t)$ chưa đủ.
:::

::: hint Gợi ý Bài tập 03.22
Ở câu (a), viết $x_t-x_{t-1}=\Delta t\,\dot x_{t-1}$ và thay $\dot x_t=\dot x_{t-1}+\Delta t\,\ddot x_{t-1}$ vào phương trình của $x_{t+1}$. Ở câu (b), $\Delta t^2=4\cdot10^{-4}$.
:::

::: solution Lời giải Bài tập 03.22
**Câu (a).** Phương trình vị trí tại bước $t-1$ cho $\Delta t\,\dot x_{t-1}=x_t-x_{t-1}$. Thế phương trình vận tốc vào phương trình vị trí tại bước $t$:

$$
\begin{aligned}
x_{t+1}&=x_t+\Delta t\,\dot x_t\\
&=x_t+\Delta t\,\dot x_{t-1}+\Delta t^2\,\ddot x_{t-1}\\
&=2x_t-x_{t-1}+\Delta t^2\,\ddot x_{t-1}.
\end{aligned}
$$

**Câu (b).** Theo giả thiết, $\lvert\Delta t^2\,\ddot x_{t-1}\rvert\le4\cdot10^{-4}\cdot10=0{,}004$ m.

- Lịch sử thứ nhất: $2x_t-x_{t-1}=0{,}11$, nên $x_{t+1}\in[0{,}106;\,0{,}114]$; vận tốc $\dot x_{t-1}=(0{,}10-0{,}09)/0{,}02=0{,}5$ m/s.
- Lịch sử thứ hai: $2x_t-x_{t-1}=0{,}09$, nên $x_{t+1}\in[0{,}086;\,0{,}094]$; vận tốc $\dot x_{t-1}=-0{,}5$ m/s.

Hai khoảng rời nhau, nên với cùng $x_t=0{,}10$ và cùng hành động $A_t$, hai lịch sử cho hai phân phối của $x_{t+1}$ không có điểm chung. Phân phối có điều kiện phụ thuộc $x_{t-1}$, không chỉ $x_t$ và $A_t$; trạng thái $x$ không có tính Markov. Lịch sử mang thông tin về vận tốc, và trạng thái $x$ bỏ sót thông tin đó, như phòng làm việc ở Ví dụ 03.4.

**Câu (c).** Trạng thái vật lý đầy đủ $(x,\dot x,\theta,\dot\theta)$ có tính Markov: động lực tất định, nên trạng thái này cùng hành động xác định duy nhất trạng thái kế tiếp. Cặp $(x_{t-1},x_t)$ cho $\dot x_{t-1}$, nhưng $x_{t+1}$ còn phụ thuộc $\ddot x_{t-1}$, tức phụ thuộc $\theta_{t-1}$, $\dot\theta_{t-1}$; điều kiện kết thúc $\lvert\theta\rvert>12^\circ$ cũng phụ thuộc góc. Vì vậy cặp này vẫn không đủ để dự báo bước tới.

**Kiểm tra lại.** Hai lịch sử khác nhau ở $x_{t-1}$ đúng $0{,}02$ m, cho hai dự báo cách nhau $0{,}02$ m, gấp năm lần bán kính $0{,}004$ m của mỗi khoảng. Notebook CartPole của Bài 04 dùng cả bốn biến khi chia ô, và Tình huống 03.2 của ghi chú cho thấy ngay cả ô của bốn biến cũng không bảo đảm tính Markov. Hai lỗi thường gặp: nhầm $\dot x_{t-1}$ với $\dot x_t$ trong phương trình Euler, được $x_{t+1}=2x_t-x_{t-1}$ và bỏ mất số hạng $\Delta t^2\,\ddot x_{t-1}$ cỡ $0{,}004$ m; kết luận sai rằng $x$ có tính Markov vì động lực vật lý tất định, trong khi tính Markov là tính chất của biểu diễn trạng thái (Nhận xét 03.3).
:::

### Bài tập 03.8. Đánh giá chính sách luôn Chờ tại pin thấp

**Mức độ:** vận dụng (đánh giá một chính sách mới và so sánh với chính sách chia đều trên cùng robot; trong mức vận dụng, các bài xếp theo mạch nên bài này đứng sau Bài tập 03.22); mục tiêu học tập 5.

**Nguồn:** ghi chú bài giảng, Bài tập 03.8 (tiểu mục 5.4), giữ số hiệu, đề và lời giải.

**Trùng trang chiếu:** [Bài tập: đánh giá chính sách luôn Chờ tại pin thấp](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/13) và [trang lời giải](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/14).

::: exercise Bài tập 03.8 (Đánh giá chính sách luôn Chờ tại pin thấp)
**Dữ kiện.** Robot thu gom lon hai mức pin với chính sách luôn Chờ tại pin thấp: ở $\mathrm H$ luôn Tìm (phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$); ở $\mathrm L$ luôn Chờ (phần thưởng $1$, ở lại $\mathrm L$). $\gamma=1/2$.

**Yêu cầu.** (a) Lập $P_\pi$ và $r_\pi$ theo thứ tự $\mathrm H$, $\mathrm L$. (b) Giải $(I-\gamma P_\pi)v=r_\pi$. (c) So sánh với giá trị $(13/4,\,7/4)$ của chính sách chia đều tại pin thấp.
:::

::: hint Gợi ý Bài tập 03.8
Phương trình của $\mathrm L$ chỉ chứa $v_{\mathrm L}$; giải nó trước.
:::

::: solution Lời giải Bài tập 03.8
**Câu (a).** Hàng $\mathrm H$ giữ nguyên như Ví dụ 03.16: $(1/2,\,1/2)$, thưởng kỳ vọng $2$. Hàng $\mathrm L$: luôn Chờ nên luôn về $\mathrm L$ với phần thưởng $1$.

$$
\begin{aligned}
P_\pi&=\begin{pmatrix}1/2&1/2\\0&1\end{pmatrix},\\
r_\pi&=\begin{pmatrix}2\\1\end{pmatrix}.
\end{aligned}
$$

**Câu (b).** Hệ (5.3) là $v_{\mathrm H}=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$ và $v_{\mathrm L}=1+\tfrac12v_{\mathrm L}$. Phương trình thứ hai cho $v_{\mathrm L}=2$. Thế vào phương trình thứ nhất: $\tfrac34v_{\mathrm H}=2+\tfrac12=\tfrac52$, nên $v_{\mathrm H}=\tfrac{10}3$.

**Câu (c).** $(10/3,\,2)$ lớn hơn $(13/4,\,7/4)$ ở cả hai trạng thái: $\tfrac{10}3=\tfrac{40}{12}>\tfrac{39}{12}$ và $2>\tfrac74$.

**Kiểm tra lại.** $2+\tfrac14\bigl(\tfrac{10}3+2\bigr)=2+\tfrac43=\tfrac{10}3$ và $1+\tfrac12\cdot2=2$. Hai lỗi thường gặp: giữ hàng $\mathrm L$ của chính sách chia đều, tức $(\tfrac12,\tfrac12)$ và thưởng $\tfrac12$, được lại $(\tfrac{13}4,\tfrac74)$; kết luận chính sách luôn Chờ là tối ưu, trong khi bài chỉ so sánh hai chính sách cụ thể.
:::

### Bài tập 03.23. Robot với $\gamma=1$ và phần thưởng trung bình mỗi bước

**Mức độ:** vận dụng; mục tiêu học tập 2 và 5.

**Nguồn:** ghi chú, đoạn "Bỏ $\gamma<1$" sau Định lý 03.28 và đoạn đọc chuỗi Neumann (5.5); Sutton và Barto (2018), §10.3, tr. 249, (10.6)–(10.8) về phần thưởng trung bình. Hệ của robot ở trang [Ví dụ: gộp các nhánh của robot](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/6).

::: exercise Bài tập 03.23 (Robot với $\gamma=1$ và phần thưởng trung bình mỗi bước)
Robot thu gom lon hai mức pin theo chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm, nhận $2$ và về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $\tfrac12$; ở $\mathrm L$ Chờ, nhận $1$ và ở lại $\mathrm L$, hoặc Sạc, nhận $0$ và về $\mathrm H$, mỗi hành động $\tfrac12$). Nhiệm vụ tiếp diễn. Theo thứ tự $\mathrm H$, $\mathrm L$:

$$
\begin{aligned}
P_\pi&=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\\
r_\pi&=\begin{pmatrix}2\\1/2\end{pmatrix}.
\end{aligned}
$$

Theo ghi chú (đoạn đọc chuỗi Neumann (5.5)), thành phần thứ $s$ của $(P_\pi)^kr_\pi$ là $\mathbb E_\pi[R_{k+1}\mid S_0=s]$.

- (a) Chứng minh $(P_\pi)^k=P_\pi$ với mọi $k\ge1$, rồi tính $\mathbb E_\pi[R_{k+1}\mid S_0=s]$ với mọi $k\ge0$ và $s\in\{\mathrm H,\mathrm L\}$.
- (b) Với $\gamma=1$, tính kỳ vọng tổng $K$ phần thưởng đầu $\mathbb E_\pi\bigl[\sum_{k=0}^{K-1}R_{k+1}\mid S_0=s\bigr]$; kết luận về $v_\pi$ và chỉ ra giả thiết bị vi phạm của Mệnh đề 03.11 và Định lý 03.28.
- (c) Với $0\le\gamma<1$, tìm công thức của $v_\pi(\mathrm H)$, $v_\pi(\mathrm L)$ theo $\gamma$ và kiểm tra với $\gamma=\tfrac12$.
- (d) Phần thưởng trung bình mỗi bước từ $s$ là $\bar r(s)=\lim_{K\to\infty}\tfrac1K\,\mathbb E_\pi\bigl[\sum_{k=0}^{K-1}R_{k+1}\mid S_0=s\bigr]$. Tính $\bar r(s)$ và chứng tỏ $(1-\gamma)\,v_\pi(s)\to\bar r(s)$ khi $\gamma\to1$.
:::

::: hint Gợi ý Bài tập 03.23
Mọi hàng của $P_\pi$ bằng $(\tfrac12,\tfrac12)$, nên $P_\pi x$ là véc-tơ có hai thành phần bằng trung bình cộng các thành phần của $x$. Ở câu (c), đặt $m=\tfrac12\bigl(v_\pi(\mathrm H)+v_\pi(\mathrm L)\bigr)$.
:::

::: solution Lời giải Bài tập 03.23
**Câu (a).** Với $x=(x_1,x_2)$, $P_\pi x=\tfrac{x_1+x_2}2\,(1,1)$. Áp dụng công thức này cho từng cột của $P_\pi$, mỗi cột là $(\tfrac12,\tfrac12)$ với trung bình cộng $\tfrac12$, ta được $P_\pi P_\pi=P_\pi$; quy nạp cho $(P_\pi)^k=P_\pi$ với $k\ge1$. Với $k=0$: $\mathbb E_\pi[R_1\mid S_0=\mathrm H]=2$ và $\mathbb E_\pi[R_1\mid S_0=\mathrm L]=\tfrac12$. Với $k\ge1$: $(P_\pi)^kr_\pi=P_\pi r_\pi=\tfrac{2+1/2}2\,(1,1)=(\tfrac54,\tfrac54)$, nên $\mathbb E_\pi[R_{k+1}\mid S_0=s]=\tfrac54$ ở cả hai trạng thái.

**Câu (b).** Cộng các kỳ vọng của câu (a):

$$
\begin{aligned}
&\mathbb E_\pi\Bigl[\sum_{k=0}^{K-1}R_{k+1}\Bigm| S_0=\mathrm H\Bigr]\\
&\quad=2+\tfrac54(K-1)=\tfrac{5K+3}4,\\
&\mathbb E_\pi\Bigl[\sum_{k=0}^{K-1}R_{k+1}\Bigm| S_0=\mathrm L\Bigr]\\
&\quad=\tfrac12+\tfrac54(K-1)=\tfrac{5K-3}4 .
\end{aligned}
$$

Cả hai tăng không bị chặn theo $K$. Dưới $\pi$, mọi phần thưởng thuộc $\{0,1,2\}$, không âm, nên tổng $\sum_{k\ge0}R_{k+1}$ có nghĩa trong $[0,+\infty]$ và kỳ vọng của nó là giới hạn của các tổng riêng trên, bằng $+\infty$. Vậy với $\gamma=1$, $v_\pi$ không phải véc-tơ số thực. Mệnh đề 03.11 và Định lý 03.28 đều cần $\gamma<1$; nhiệm vụ tiếp diễn không có trạng thái kết thúc để thay giả thiết đó.

**Câu (c).** Đặt $m=\tfrac12\bigl(v_\pi(\mathrm H)+v_\pi(\mathrm L)\bigr)$. Theo (5.3) và câu (a), $v=r_\pi+\gamma P_\pi v=r_\pi+\gamma m\,(1,1)$. Lấy trung bình hai phương trình:

$$
\begin{aligned}
m&=\tfrac12\bigl(2+\tfrac12\bigr)+\gamma m\\
&=\tfrac54+\gamma m,
\end{aligned}
$$

nên $m=\dfrac{5}{4(1-\gamma)}$ và

$$
\begin{aligned}
v_\pi(\mathrm H)&=2+\frac{5\gamma}{4(1-\gamma)},\\
v_\pi(\mathrm L)&=\frac12+\frac{5\gamma}{4(1-\gamma)} .
\end{aligned}
$$

Với $\gamma=\tfrac12$: $\tfrac{5\gamma}{4(1-\gamma)}=\tfrac54$, nên $v_\pi=(\tfrac{13}4,\tfrac74)$, trùng Ví dụ 03.14. Hiệu $v_\pi(\mathrm H)-v_\pi(\mathrm L)=\tfrac32$ không phụ thuộc $\gamma$.

**Câu (d).** Theo câu (b), $\tfrac1K\cdot\tfrac{5K\pm3}4\to\tfrac54$, nên $\bar r(\mathrm H)=\bar r(\mathrm L)=\tfrac54$. Theo câu (c),

$$
\begin{aligned}
&(1-\gamma)\,v_\pi(\mathrm H)\\
&\quad=2(1-\gamma)+\tfrac54\gamma\to\tfrac54,\\
&(1-\gamma)\,v_\pi(\mathrm L)\\
&\quad=\tfrac12(1-\gamma)+\tfrac54\gamma\to\tfrac54 .
\end{aligned}
$$

Khi $\gamma$ gần $1$, $v_\pi(s)\approx\tfrac54\cdot\tfrac1{1-\gamma}$: giá trị lớn vì phần thưởng trung bình mỗi bước dương, và mức khởi đầu chỉ góp một hằng số.

**Kiểm tra lại.** Phân phối $d=(\tfrac12,\tfrac12)$ thỏa $dP_\pi=d$, và $d\cdot r_\pi=\tfrac54$, đúng dạng (10.7)–(10.8) của Sutton và Barto. Với $\gamma=1$, hệ (5.3) vô nghiệm vì cộng hai phương trình được $0=\tfrac52=2\bar r$. Hai lỗi thường gặp: cho rằng phần thưởng $-3$ của cứu hộ có thể làm tổng hội tụ, dẫn tới kết luận sai rằng $v_\pi$ hữu hạn với $\gamma=1$, trong khi chính sách không bao giờ Tìm ở $\mathrm L$; dùng $\mathbb E_\pi[R_{k+1}]=\tfrac54$ cho cả $k=0$, được tổng $K$ bước bằng $\tfrac54K$ ở cả hai trạng thái và mất hiệu $\tfrac32$.
:::

### Bài tập 03.24. Mô hình hóa robot ba mức pin

**Mức độ:** vận dụng (tổng hợp các mạch 2–6); mục tiêu học tập 1, 4 và 5.

**Nguồn:** Bài tập tuần 2 (2025–2026), bài 10 (mô hình hóa một bài toán robot thành MDP); khung ví dụ 3.3 và bài tập 3.4 của Sutton và Barto (2018, tr. 52–53); số liệu sư phạm tự xây dựng. Thuật toán dùng ở trang [Đánh giá chính sách bằng giải hệ tuyến tính](lecture-03-qua-trinh-quyet-dinh-markov.html#/6/10).

::: exercise Bài tập 03.24 (Mô hình hóa robot ba mức pin)
Robot thu gom lon được nâng cấp để phân biệt ba mức pin: cao $\mathrm H$, vừa $\mathrm V$, thấp $\mathrm L$. Robot hoạt động liên tục; cứu hộ và sạc không dừng công việc. Phản hồi của từng lựa chọn:

- ở $\mathrm H$: Tìm cho phần thưởng $2$, pin giữ ở $\mathrm H$ hoặc xuống $\mathrm V$, mỗi khả năng xác suất $\tfrac12$; Chờ cho $1$ và pin giữ ở $\mathrm H$;
- ở $\mathrm V$: Tìm cho $2$, pin giữ ở $\mathrm V$ hoặc xuống $\mathrm L$, mỗi khả năng $\tfrac12$; Chờ cho $1$ và pin giữ ở $\mathrm V$; Sạc cho $0$ và pin về $\mathrm H$;
- ở $\mathrm L$: Tìm có hai khả năng, mỗi khả năng xác suất $\tfrac12$. Pin còn đủ: robot nhận $2$ và ở lại $\mathrm L$. Pin cạn: robot được cứu hộ, nhận $-3$ và được sạc về $\mathrm H$ ngay trong bước đó. Chờ cho $1$ và pin giữ ở $\mathrm L$. Sạc cho $0$ và pin lên $\mathrm V$.

Chính sách $\pi$: ở $\mathrm H$ và ở $\mathrm V$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động xác suất $\tfrac12$. Hệ số chiết khấu $\gamma=\tfrac12$.

- (a) Lập bộ MDP hữu hạn: $\mathcal S^+$, $\mathcal A(s)$ cho mỗi $s$, $\mathcal R$; xác định loại nhiệm vụ và lý do cần $\gamma<1$.
- (b) Lập bảng $p(s',r\mid s,a)$ gồm mọi hàng có xác suất dương, kiểm tra điều kiện chuẩn hóa của từng cặp, và tính $r(\mathrm L,\mathrm{tim})$.
- (c) Lập $P_\pi$, $r_\pi$ theo thứ tự $\mathrm H$, $\mathrm V$, $\mathrm L$; viết hệ $(I-\gamma P_\pi)v=r_\pi$, giải và kiểm tra lại.
- (d) Giải thích vì sao $v_\pi(\mathrm V)$, $v_\pi(\mathrm L)$ trùng giá trị $(\tfrac{13}4,\tfrac74)$ của robot hai mức pin dưới chính sách chia đều tại pin thấp.
- (e) Giả sử xác suất cạn pin khi Tìm ở $\mathrm L$ tăng theo số lần Tìm liên tiếp ở $\mathrm L$ ngay trước đó, nhưng luôn nhỏ hơn $1$. Xét chính sách $\pi'$ trùng $\pi$ ở $\mathrm H$ và $\mathrm V$, còn ở $\mathrm L$ chọn Tìm, Chờ, Sạc, mỗi hành động xác suất $\tfrac13$. Với $\pi'$, xác định định nghĩa bị vi phạm khi trạng thái chỉ là mức pin, bước của chứng minh phương trình Bellman mất căn cứ, và cách sửa biểu diễn trạng thái.
:::

::: hint Gợi ý Bài tập 03.24
Ở câu (b), cặp có hai phản hồi cho hai hàng, cặp tất định cho một hàng. Ở câu (c), dưới $\pi$, từ $\mathrm V$ và $\mathrm L$ robot không bao giờ về $\mathrm H$; giải hai phương trình của $\mathrm V$, $\mathrm L$ trước.
:::

::: solution Lời giải Bài tập 03.24
**Câu (a).** $\mathcal S^+=\mathcal S=\{\mathrm H,\mathrm V,\mathrm L\}$, không có trạng thái kết thúc. $\mathcal A(\mathrm H)=\{\mathrm{tim},\mathrm{cho}\}$, $\mathcal A(\mathrm V)=\mathcal A(\mathrm L)=\{\mathrm{tim},\mathrm{cho},\mathrm{sac}\}$, tổng cộng tám cặp hợp lệ. $\mathcal R=\{-3,0,1,2\}$. Nhiệm vụ tiếp diễn (Định nghĩa 03.8), nên lợi tức là chuỗi vô hạn; Mệnh đề 03.11 cần $\gamma<1$ để chuỗi hội tụ, và khi đó $\lvert G_t\rvert\le3/(1-\gamma)=6$.

**Câu (b).** Bảng có mười một hàng:

| $s$ | $a$ | $s'$ | $r$ | $p(s',r\mid s,a)$ |
|---|---|---|---:|---:|
| $\mathrm H$ | $\mathrm{tim}$ | $\mathrm H$ | $2$ | $1/2$ |
| $\mathrm H$ | $\mathrm{tim}$ | $\mathrm V$ | $2$ | $1/2$ |
| $\mathrm H$ | $\mathrm{cho}$ | $\mathrm H$ | $1$ | $1$ |
| $\mathrm V$ | $\mathrm{tim}$ | $\mathrm V$ | $2$ | $1/2$ |
| $\mathrm V$ | $\mathrm{tim}$ | $\mathrm L$ | $2$ | $1/2$ |
| $\mathrm V$ | $\mathrm{cho}$ | $\mathrm V$ | $1$ | $1$ |
| $\mathrm V$ | $\mathrm{sac}$ | $\mathrm H$ | $0$ | $1$ |
| $\mathrm L$ | $\mathrm{tim}$ | $\mathrm L$ | $2$ | $1/2$ |
| $\mathrm L$ | $\mathrm{tim}$ | $\mathrm H$ | $-3$ | $1/2$ |
| $\mathrm L$ | $\mathrm{cho}$ | $\mathrm L$ | $1$ | $1$ |
| $\mathrm L$ | $\mathrm{sac}$ | $\mathrm V$ | $0$ | $1$ |

Ba cặp Tìm có hai hàng, mỗi hàng $\tfrac12$, tổng $1$; năm cặp còn lại có một hàng xác suất $1$. Vậy (1.3) thỏa ở cả tám cặp. Theo (1.6), $r(\mathrm L,\mathrm{tim})=\tfrac12\cdot2+\tfrac12\cdot(-3)=-\tfrac12$.

**Câu (c).** Theo (5.2), hàng $\mathrm H$ chỉ dùng Tìm, hàng $\mathrm V$ chỉ dùng Tìm, hàng $\mathrm L$ trộn Chờ và Sạc:

$$
\begin{aligned}
P_\pi&=\begin{pmatrix}1/2&1/2&0\\0&1/2&1/2\\0&1/2&1/2\end{pmatrix},\\
r_\pi&=\begin{pmatrix}2\\2\\1/2\end{pmatrix}.
\end{aligned}
$$

Với $\gamma=\tfrac12$ và $v=(v_{\mathrm H},v_{\mathrm V},v_{\mathrm L})$, trong đó $v_{\mathrm H}=v_\pi(\mathrm H)$, $v_{\mathrm V}=v_\pi(\mathrm V)$, $v_{\mathrm L}=v_\pi(\mathrm L)$, hệ (5.3) là

$$
\begin{aligned}
\tfrac34v_{\mathrm H}-\tfrac14v_{\mathrm V}&=2,\\
\tfrac34v_{\mathrm V}-\tfrac14v_{\mathrm L}&=2,\\
-\tfrac14v_{\mathrm V}+\tfrac34v_{\mathrm L}&=\tfrac12 .
\end{aligned}
$$

Trừ phương trình thứ ba khỏi phương trình thứ hai: $v_{\mathrm V}-v_{\mathrm L}=\tfrac32$. Thế $v_{\mathrm V}=v_{\mathrm L}+\tfrac32$ vào phương trình thứ ba: $\tfrac12v_{\mathrm L}-\tfrac38=\tfrac12$, nên $v_{\mathrm L}=\tfrac74$ và $v_{\mathrm V}=\tfrac{13}4$. Phương trình thứ nhất cho $\tfrac34v_{\mathrm H}=2+\tfrac{13}{16}=\tfrac{45}{16}$, nên $v_{\mathrm H}=\tfrac{15}4$. Kiểm tra theo (4.5) tại $\mathrm H$: $2+\tfrac14\bigl(\tfrac{15}4+\tfrac{13}4\bigr)=2+\tfrac74=\tfrac{15}4$. Theo Định lý 03.28, $v_\pi=(\tfrac{15}4;\,\tfrac{13}4;\,\tfrac74)$ là nghiệm duy nhất.

**Câu (d).** Dưới $\pi$, từ $\mathrm V$ robot chỉ tới $\mathrm V$ hoặc $\mathrm L$, từ $\mathrm L$ chỉ tới $\mathrm L$ hoặc $\mathrm V$; hai phương trình của $\mathrm V$, $\mathrm L$ không chứa $v_{\mathrm H}$. Đổi tên $\mathrm V$ thành $\mathrm H$, hai phương trình này trùng hệ (5.1) của robot hai mức: Tìm cho $2$ và giữ mức hoặc xuống $\mathrm L$ mỗi khả năng $\tfrac12$; ở $\mathrm L$, Chờ cho $(\mathrm L,1)$, Sạc cho $0$ và lên mức trên. Vì vậy hai giá trị trùng $(\tfrac{13}4,\tfrac74)$. Xuất phát tại $\mathrm H$, mỗi bước robot rời $\mathrm H$ với xác suất $\tfrac12$ và sau đó không quay lại, nên $\mathrm H$ chỉ xuất hiện ở đoạn đầu của quỹ đạo.

**Câu (e).** Dưới $\pi'$, xét hai lịch sử cùng kết thúc ở $\mathrm L$ rồi chọn Tìm: một lịch sử vừa từ $\mathrm V$ xuống $\mathrm L$, chưa Tìm lần nào ở $\mathrm L$; lịch sử kia vừa Tìm hai lần liên tiếp ở $\mathrm L$ và vẫn ở $\mathrm L$. Cả hai có xác suất dương, vì $\pi'$ Tìm ở $\mathrm V$ với xác suất $1$, Tìm ở $\mathrm L$ với xác suất $\tfrac13$, và mỗi lần Tìm ở $\mathrm L$ pin còn đủ với xác suất dương. Hai lịch sử cho hai xác suất cạn pin khác nhau, tức hai phân phối phản hồi khác nhau. Đẳng thức (1.2) của Định nghĩa 03.2 sai, nên không có hàm động lực $p$ chỉ phụ thuộc $(s,a)$ theo Định nghĩa 03.4. Bước mất căn cứ là Bổ đề 03.20: kỳ vọng của phần tương lai sau một lịch sử kết thúc ở $\mathrm L$ không còn là một số $v_\pi(\mathrm L)$ chung, nên Định lý 03.21 không áp dụng. Cách sửa: thêm vào trạng thái số lần Tìm liên tiếp ở $\mathrm L$, chặn trên bởi một số $N$ nếu sau $N$ lần xác suất cạn pin không tăng nữa; trạng thái $(\mathrm L,k)$ với $k=0,\dots,N$ giữ cho tập trạng thái hữu hạn.

**Kiểm tra lại.** Mỗi hàng của $P_\pi$ có tổng $1$. Hiệu $v_{\mathrm H}-v_{\mathrm V}=\tfrac12$ nhỏ hơn hiệu $v_{\mathrm V}-v_{\mathrm L}=\tfrac32$: $\mathrm H$ và $\mathrm V$ có cùng thưởng kỳ vọng $2$ dưới $\pi$, và trừ hai phương trình đầu theo (4.5) được $v_{\mathrm H}-v_{\mathrm V}=\tfrac14(v_{\mathrm H}-v_{\mathrm V})+\tfrac14(v_{\mathrm V}-v_{\mathrm L})$. Với chính sách $\pi$ của đề, robot không bao giờ Tìm ở $\mathrm L$, nên bộ đếm của câu (e) luôn bằng $0$ và các giá trị của câu (c) không đổi. Ba lỗi thường gặp: quên hàng $(\mathrm H,-3)$ của Tìm từ $\mathrm L$, khi đó nhóm $(\mathrm L,\mathrm{tim})$ có tổng $\tfrac12$ và vi phạm (1.3); dùng trọng số $\tfrac13$ cho cả ba hành động ở $\mathrm L$ khi lập $P_\pi$, tức đánh giá chính sách $\pi'$ thay vì $\pi$; cho Sạc từ $\mathrm L$ về $\mathrm H$ như ở robot hai mức, được $v=(\tfrac{49}{13};\,\tfrac{43}{13};\,\tfrac{25}{13})$ thay vì $(\tfrac{15}4;\,\tfrac{13}4;\,\tfrac74)$.
:::

### Bài tập 03.25. Xác suất cứu hộ và lựa chọn tại pin thấp

**Mức độ:** vận dụng (bài tổng hợp của mạch 7); mục tiêu học tập 4 và 5.

**Nguồn:** số liệu sư phạm tự xây dựng; mở rộng bài tổng hợp trên trang [Bài tập: robot với rủi ro cứu hộ thấp hơn](lecture-03-qua-trinh-quyet-dinh-markov.html#/7/4) (ghi chú, Bài tập 03.13, ứng với $\rho=\tfrac14$) và ghi chú Ví dụ 03.15 (ứng với $\rho=\tfrac12$); ghi chú Nhận xét 03.31.

::: exercise Bài tập 03.25 (Xác suất cứu hộ và lựa chọn tại pin thấp)
Robot thu gom lon hai mức pin có các phản hồi: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $\tfrac12$; Chờ từ $\mathrm H$ cho $(\mathrm H,1)$; Chờ từ $\mathrm L$ cho $(\mathrm L,1)$; Sạc từ $\mathrm L$ cho $(\mathrm H,0)$. Tìm từ $\mathrm L$ phụ thuộc tham số $\rho\in[0,1]$: với xác suất $1-\rho$ pin còn đủ, robot nhận $2$ và ở lại $\mathrm L$; với xác suất $\rho$ robot được cứu hộ, nhận $-3$ và về $\mathrm H$. Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động xác suất $\tfrac12$. Hệ số chiết khấu $\gamma=\tfrac12$. Khi $\rho=\tfrac12$, giá trị của chính sách là $v_\pi=(\tfrac{13}4,\tfrac74)$. Nhắc lại (4.6): $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s')$.

- (a) Chứng tỏ $v_\pi$ không phụ thuộc $\rho$.
- (b) Tính $r(\mathrm L,\mathrm{tim})$ và $q_\pi(\mathrm L,\mathrm{tim})$ theo $\rho$; kiểm tra với $\rho=\tfrac12$.
- (c) Tính $q_\pi(\mathrm L,\mathrm{cho})$, $q_\pi(\mathrm L,\mathrm{sac})$; tìm $\rho^*$ sao cho $q_\pi(\mathrm L,\mathrm{tim})=q_\pi(\mathrm L,\mathrm{cho})$ và khoảng giá trị của $\rho$ trong đó Tìm có giá trị hành động lớn nhất tại $\mathrm L$.
- (d) Với $\rho=\tfrac1{10}$, nêu kết luận được phép rút ra từ việc so sánh ba giá trị hành động tại $\mathrm L$. Đánh giá chính sách $\pi''$ "ở $\mathrm H$ luôn Tìm, ở $\mathrm L$ luôn Tìm" bằng hệ (5.3) và so sánh với $v_\pi$.
:::

::: hint Gợi ý Bài tập 03.25
Ở câu (a), $\rho$ chỉ xuất hiện ở cặp $(\mathrm L,\mathrm{tim})$. Ở câu (b), $p(\mathrm L\mid\mathrm L,\mathrm{tim})=1-\rho$ và $p(\mathrm H\mid\mathrm L,\mathrm{tim})=\rho$.
:::

::: solution Lời giải Bài tập 03.25
**Câu (a).** Tham số $\rho$ chỉ xuất hiện ở cặp $(\mathrm L,\mathrm{tim})$, mà $\pi(\mathrm{tim}\mid\mathrm L)=0$. Theo cùng lập luận như lời giải Bài tập 03.17(b), $P_\pi$ và $r_\pi$ không phụ thuộc $\rho$, nên theo Định lý 03.28, $v_\pi=(\tfrac{13}4,\tfrac74)$ với mọi $\rho\in[0,1]$.

**Câu (b).** Theo (1.6), $r(\mathrm L,\mathrm{tim})=(1-\rho)\cdot2+\rho\cdot(-3)=2-5\rho$. Theo (4.6):

$$
\begin{aligned}
&q_\pi(\mathrm L,\mathrm{tim})\\
&\quad=2-5\rho\\
&\qquad+\tfrac12\bigl[(1-\rho)\cdot\tfrac74+\rho\cdot\tfrac{13}4\bigr]\\
&\quad=2-5\rho+\tfrac78+\tfrac34\rho\\
&\quad=\tfrac{23}8-\tfrac{17}4\rho .
\end{aligned}
$$

Với $\rho=\tfrac12$: $\tfrac{23}8-\tfrac{17}8=\tfrac34$, trùng ghi chú Ví dụ 03.15.

**Câu (c).** Chờ và Sạc không phụ thuộc $\rho$: $q_\pi(\mathrm L,\mathrm{cho})=1+\tfrac12\cdot\tfrac74=\tfrac{15}8$ và $q_\pi(\mathrm L,\mathrm{sac})=0+\tfrac12\cdot\tfrac{13}4=\tfrac{13}8$. Phương trình $\tfrac{23}8-\tfrac{17}4\rho=\tfrac{15}8$ cho $\tfrac{17}4\rho=1$, nên $\rho^*=\tfrac4{17}\approx0{,}235$. Hàm $q_\pi(\mathrm L,\mathrm{tim})$ giảm theo $\rho$, nên Tìm có giá trị hành động lớn nhất tại $\mathrm L$ khi $0\le\rho<\tfrac4{17}$; khi đó $q_\pi(\mathrm L,\mathrm{tim})>\tfrac{15}8>\tfrac{13}8$.

**Câu (d).** Với $\rho=\tfrac1{10}$: $q_\pi(\mathrm L,\mathrm{tim})=\tfrac{23}8-\tfrac{17}{40}=\tfrac{49}{20}=2{,}45$, lớn hơn $\tfrac{15}8$ và $\tfrac{13}8$. Kết luận được phép: trong ba thí nghiệm ấn định hành động đầu tại $\mathrm L$ rồi theo $\pi$, thí nghiệm Tìm cho lợi tức kỳ vọng lớn nhất. Phép so sánh này chưa đánh giá chính sách nào khác $\pi$ (Nhận xét 03.31). Với $\pi''$, hàng $\mathrm L$ dùng Tìm: $r^{\pi''}=(2;\,\tfrac32)$, và hệ (5.3) là

$$
\begin{aligned}
v_{\mathrm H}&=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L},\\
v_{\mathrm L}&=\tfrac32+\tfrac1{20}v_{\mathrm H}+\tfrac9{20}v_{\mathrm L} .
\end{aligned}
$$

Phương trình thứ nhất cho $v_{\mathrm H}=\tfrac83+\tfrac13v_{\mathrm L}$. Thế vào phương trình thứ hai: $\tfrac{11}{20}v_{\mathrm L}=\tfrac32+\tfrac2{15}+\tfrac1{60}v_{\mathrm L}$, nên $\tfrac8{15}v_{\mathrm L}=\tfrac{49}{30}$ và $v_{\mathrm L}=\tfrac{49}{16}$; suy ra $v_{\mathrm H}=\tfrac{59}{16}$. Giá trị $(\tfrac{59}{16},\tfrac{49}{16})$ lớn hơn $(\tfrac{52}{16},\tfrac{28}{16})=(\tfrac{13}4,\tfrac74)$ ở cả hai trạng thái. Kết luận chỉ là $\pi''$ tốt hơn $\pi$ khi $\rho=\tfrac1{10}$; muốn kết luận $\pi''$ tối ưu cần các công cụ của Bài 04.

**Kiểm tra lại.** Với $\rho=\tfrac14$, công thức câu (b) cho $\tfrac{23}8-\tfrac{17}{16}=\tfrac{29}{16}$, trùng bài tổng hợp trên trang; với $\rho=0$, Tìm và Chờ cùng giữ robot ở $\mathrm L$ nên hiệu $q_\pi(\mathrm L,\mathrm{tim})-q_\pi(\mathrm L,\mathrm{cho})=\tfrac{23}8-\tfrac{15}8=1$ bằng hiệu phần thưởng $2-1$. Thế nghiệm câu (d): $2+\tfrac14\bigl(\tfrac{59}{16}+\tfrac{49}{16}\bigr)=2+\tfrac{27}{16}=\tfrac{59}{16}$. Hai lỗi thường gặp: dùng $v_\pi(\mathrm L)$ cho nhánh cứu hộ thay vì $v_\pi(\mathrm H)$, được $q_\pi(\mathrm L,\mathrm{tim})=\tfrac{23}8-5\rho$ và $\rho^*=\tfrac15$; kết luận từ $q_\pi(\mathrm L,\mathrm{tim})>q_\pi(\mathrm L,\mathrm{cho})$ rằng $\pi''$ tối ưu mà không đánh giá $\pi''$.
:::

## Tài liệu tham khảo

- Bài giảng gốc (2025–2026), *Markov Decision Processes with Key Concepts*, trang 28–58: phạm vi nội dung của các bài tập.
- Bài tập tuần 2 (2025–2026), Tạ Việt Cường, ngày 12/3/2026: bài 3 (Bài tập 03.20), bài 4 (Bài tập 03.21), bài 7–8 (Bài tập 03.7, 03.19), bài 10 (Bài tập 03.24).
- Bài tập tuần 3 (2025–2026), Tạ Việt Cường, ngày 8/5/2026: bài 1 (Bài tập 03.16).
- R. S. Sutton và A. G. Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: ví dụ 3.3 và bài tập 3.4, tr. 52–53 (Bài tập 03.15, 03.24); bài tập 3.8–3.9, tr. 56 (Bài tập 03.18); ví dụ 3.4, tr. 56 (Bài tập 03.22); bài tập 3.17, tr. 61 (Bài tập 03.19); §4.1, tr. 74 (Bài tập 03.20); §10.3, tr. 249 (Bài tập 03.23).
- Notebook thực hành Bài 04, `thuc-hanh-cartpole-quy-hoach-dong.ipynb`, phần 2, mục 3.1 và 7.1 (Bài tập 03.22).
- Gymnasium, môi trường `CartPole-v1`, mã nguồn `CartPoleEnv.step`: bộ tích phân Euler và công thức gia tốc với tham số mặc định (Bài tập 03.22).
