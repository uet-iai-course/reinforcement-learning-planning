# Bài tập Bài 01 — Giới thiệu Học tăng cường

Bộ bài tập gồm mười ba bài cho năm mạch nội dung và mạch tổng kết của bài học, xếp theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường (reinforcement learning). Bài tập 01.1–01.8 giữ số hiệu, đề bài và lời giải của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-01/lecture-note.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html) Bài 01; phần "Kiểm tra lại" của các bài này nêu thêm lỗi thường gặp. Bài tập 01.9–01.11 chỉ có trong mục "Bài tập củng cố" của ghi chú, không chép lại ở đây, nhưng vẫn thuộc bộ bài giao của buổi học. Bài tập 01.12–01.16 chỉ có trong tệp này. Các bài được xếp theo mức và giữ số hiệu của ghi chú, nên thứ tự số hiệu trong tệp không liên tục. Bảy bài trùng bài tập trên trang chiếu: 01.1, 01.2, 01.3, 01.5, 01.6, 01.7 và 01.13; với mỗi bài, dòng "Trùng trang chiếu" dẫn tới trang câu hỏi và trang lời giải, và lời giải trong tệp cho cùng kết quả với lời giải trên trang.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/1/1) | — |
| 2. Tác tử học từ tương tác | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/2/1) | 01.1 |
| 3. Tín hiệu học và dữ liệu tương tác | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/3/1) | 01.2, 01.15 |
| 4. Phần thưởng và lợi tức | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/4/1) | 01.3, 01.4, 01.14; 01.10 (chỉ trong ghi chú) |
| 5. Chính sách, hàm giá trị, mô hình và thăm dò | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/5/1) | 01.5, 01.6, 01.12, 01.15; 01.9, 01.11 (chỉ trong ghi chú) |
| 6. Tic-tac-toe như một bài toán Học tăng cường | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/6/1) | 01.7, 01.8 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-01-gioi-thieu-hoc-tang-cuong.html#/7/1) | 01.13, 01.16 |

Bài tập 01.15 dùng cả mạch 3 (phản hồi trễ) và mạch 5 (mô hình, thăm dò).

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 01. Bước quyết định là $t=0,1,2,\dots$; ở bước $t$, tác tử (agent) nhận quan sát (observation) $O_t$, chọn hành động (action) $A_t$, rồi môi trường (environment) trả phần thưởng (reward) $R_{t+1}$ và quan sát $O_{t+1}$. Lịch sử là $H_t=(O_0,A_0,R_1,O_1,\dots,A_{t-1},R_t,O_t)$, với $H_0=(O_0)$. Lượt (episode) kết thúc tại $T\le L$, trong đó $L$ là số hành động tối đa. Lợi tức (return) là $G_t=R_{t+1}+\dots+R_T$, không chiết khấu, với $G_T=0$; giá trị của một lịch sử đã kết thúc bằng $0$. Giá trị của lịch sử $h$ dưới chính sách (policy) $\pi$ là $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$ (Định nghĩa 01.12): kỳ vọng lấy theo các hành động từ bước $t$ trở đi chọn theo $\pi$ và các phản hồi theo luật cố định của môi trường; ánh xạ $h\mapsto v_\pi(h)$ là hàm giá trị (value function) của $\pi$. Mô hình (model) của môi trường là một mô tả cho phép dự báo phản hồi của môi trường, và lập kế hoạch (planning) là dùng mô hình để chọn hành động bằng cách xét trước các diễn biến; phương pháp có mô hình (model-based) dùng mô hình để lập kế hoạch, phương pháp phi mô hình (model-free) học chính sách hoặc hàm giá trị trực tiếp từ dữ liệu tương tác (Định nghĩa 01.14). Trong bài toán chọn lặp lại, hành động tham lam (greedy action) là hành động có trung bình mẫu $\bar r(a)$ của các phần thưởng đã nhận lớn nhất; khai thác (exploitation) là chọn một hành động tham lam, thăm dò (exploration) là chọn một hành động không tham lam (Định nghĩa 01.16).

**Robot dọn dãy bốn ô.** Dãy bốn ô sàn đánh số 1 đến 4; trừ khi đề bài nói khác, chỉ ô 4 có rác. Ba hành động $\text{trái}$, $\text{phải}$, $\text{hút}$: $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ giữ nguyên vị trí và làm sạch ô đang đứng. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$ cho ô đang đứng, không báo vị trí. Trạng thái (state) là cặp (vị trí, tình trạng ô 4). Ba chính sách dùng nhiều lần: $\pi_1$ thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$; $\pi_u$ chọn đều trên các hành động; ở Tic-tac-toe, $\pi_w$ đánh nước thắng ngay nếu có, chọn đều trong số đó nếu có nhiều nước như vậy, nếu không có thì chọn đều trên các ô trống. Giới hạn $L$, ô xuất phát và cách đặt phần thưởng thay đổi theo từng bài và được nêu lại trong đề.

**Tic-tac-toe.** Bàn $3\times3$, ô đánh số 1 đến 9 theo hàng, từ trái sang phải và từ trên xuống dưới. Tác tử là người chơi X; bàn cờ, luật chơi và đối thủ O là môi trường; O chọn đều trên các ô trống. Bước $t$ đếm số nước X đã đi. Phần thưởng của X là $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc. Chữ O đứng chỉ quân cờ của đối thủ, $O_t$ nghiêng chỉ quan sát.

Tên hành động và quan sát viết chữ đứng ($\text{phải}$, $\text{sạch}$). Số thập phân viết với dấu phẩy, như $0{,}55$; khi một bộ số có thành phần thập phân, các thành phần cách nhau bằng dấu chấm phẩy. Mọi bộ số là số liệu sư phạm tự xây dựng. Lời giải cần nêu kết quả của ghi chú được dùng ở từng bước.

## Mức nhận biết

### Bài tập 01.1. Trạng thái và quan sát của robot dọn dãy bốn ô

**Mức độ:** nhận biết. Mục tiêu học tập 1 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 1.3; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: trạng thái và quan sát của robot](lecture-01-gioi-thieu-hoc-tang-cuong.html#/2/7) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/2/8).

::: exercise Bài tập 01.1 (Trạng thái và quan sát của robot dọn dãy bốn ô)
Dãy bốn ô đánh số 1 đến 4; chỉ ô 4 có rác. Hành động $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ làm sạch ô đang đứng. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$ cho ô đang đứng. Lượt bị cắt sau $L=5$ hành động. Trạng thái là cặp (vị trí, tình trạng ô 4). Lần này robot bắt đầu ở ô 3.

- (a) Viết $S_0$, $O_0$ và tập hành động hợp lệ.
- (b) Robot chọn $A_0=\text{phải}$. Viết $R_1$, $S_1$, $O_1$ và lịch sử $H_1$.
- (c) Liệt kê mọi trạng thái chưa kết thúc lượt cho cùng quan sát với $S_0$, và nêu số lần $\text{phải}$ mỗi trạng thái cần để tới rác.
:::

::: hint Gợi ý Bài tập 01.1
Trạng thái là cặp (vị trí, tình trạng ô 4). Quan sát chỉ phụ thuộc ô robot đang đứng.
:::

::: solution Lời giải Bài tập 01.1
**Câu (a).** $S_0=(3,\text{còn rác})$, $O_0=\text{sạch}$ vì ô 3 sạch, và tập hành động hợp lệ là $\{\text{trái},\text{phải},\text{hút}\}$.

**Câu (b).** Sang phải từ ô 3 đưa robot tới ô 4, chưa hút nên $R_1=0$ và lượt chưa kết thúc. Do đó $S_1=(4,\text{còn rác})$, $O_1=\text{bẩn}$, và $H_1=(\text{sạch},\text{phải},0,\text{bẩn})$.

**Câu (c).** Quan sát $\text{sạch}$ xuất hiện khi robot đứng ở ô 1, 2 hoặc 3 lúc ô 4 còn rác: các trạng thái $(1,\text{còn rác})$, $(2,\text{còn rác})$, $(3,\text{còn rác})$, cần lần lượt ba, hai và một lần $\text{phải}$. Vì cả ba cho cùng $O_0=\text{sạch}$ và lịch sử ở bước $0$ chỉ gồm $O_0$, robot không biết mình cần bao nhiêu lần $\text{phải}$.

**Kiểm tra lại.** Câu (b) phù hợp luật: phần thưởng $+1$ chỉ đến khi robot chọn $\text{hút}$ ở ô 4, chưa xảy ra ở bước $0$. Viết $O_0=(3,\text{còn rác})$ là đồng nhất quan sát với trạng thái, trong khi cảm biến không báo vị trí. Ghi $R_1=+1$ ngay khi robot tới ô 4 cũng sai, vì luật chỉ thưởng cho hành động $\text{hút}$ ở ô đó, không thưởng cho việc đến ô bẩn.
:::

### Bài tập 01.2. Nhận dạng tín hiệu học

**Mức độ:** nhận biết. Mục tiêu học tập 2 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 2.2; câu (d) theo câu hỏi về việc học một môn học của bài giảng gốc (2025–2026), trang 20.

**Trùng trang chiếu:** [Bài tập: nhận dạng tín hiệu học](lecture-01-gioi-thieu-hoc-tang-cuong.html#/3/7) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/3/8).

::: exercise Bài tập 01.2 (Nhận dạng tín hiệu học)
Ba dạng tín hiệu học của Định nghĩa 01.5 là học có giám sát (supervised learning), học không giám sát (unsupervised learning) và Học tăng cường. Xếp mỗi tình huống sau vào một trong ba dạng đó, và nêu tín hiệu học trong tình huống đó.

- (a) $1\,000$ ảnh ô sàn, mỗi ảnh được người gán nhãn $\text{sạch}$ hoặc $\text{bẩn}$; cần dự đoán nhãn của ảnh mới.
- (b) $1\,000$ ảnh ô sàn không có nhãn; cần chia ảnh thành các nhóm giống nhau.
- (c) Một robot hút bụi trên dãy bốn ô, bắt đầu ở ô 1, chỉ ô 4 có rác, lượt bị cắt sau $L=5$ hành động, ghi được dãy mẫu (quan sát, hành động, phần thưởng): $(\text{sạch},\text{phải},0)$, $(\text{sạch},\text{hút},0)$, $(\text{sạch},\text{phải},0)$, $(\text{sạch},\text{phải},0)$, $(\text{bẩn},\text{hút},1)$.
- (d) Một sinh viên chỉ biết điểm tổng kết ở cuối học kỳ, sau khi đã chọn cách học trong suốt học kỳ.
:::

::: hint Gợi ý Bài tập 01.2
Hỏi hai câu cho mỗi tình huống: dữ liệu có sẵn trước hay do người học sinh ra, và tín hiệu có cho biết đầu ra đúng hay không.
:::

::: solution Lời giải Bài tập 01.2
**Câu (a).** Học có giám sát. Tín hiệu là nhãn $\text{sạch}$ hoặc $\text{bẩn}$ của từng ảnh, cho biết đầu ra đúng.

**Câu (b).** Học không giám sát. Không có nhãn; tiêu chí là độ giống nhau giữa các ảnh trong cùng nhóm.

**Câu (c).** Học tăng cường. Tín hiệu là dãy phần thưởng $0,0,0,0,1$, đến trễ, và dữ liệu do chính robot sinh ra.

**Câu (d).** Học tăng cường. Tín hiệu là điểm tổng kết, một số đánh giá đến sau cả học kỳ. Tình huống này có ba trong bốn khác biệt của Học tăng cường theo Nhận xét 01.6: chỉ có một số đánh giá thay cho đầu ra đúng; đánh giá đến sau cả chuỗi lựa chọn; cách học đã chọn ảnh hưởng tới những gì sinh viên trải qua về sau.

**Kiểm tra lại.** Lượt (c) dùng năm hành động, đúng bằng giới hạn $L=5$, và kết thúc bằng phần thưởng $1$ ở bước cuối; lần hút ở ô 2 sạch cho $0$ và không kết thúc lượt. Lỗi thường gặp là xếp (a) và (c) vào cùng một dạng vì cả hai đều có $\text{sạch}$ và $\text{bẩn}$: ở (a), $\text{sạch}$ hoặc $\text{bẩn}$ là nhãn do người gán; ở (c), nó là quan sát của robot, còn tín hiệu học là phần thưởng.
:::

### Bài tập 01.7. Biểu diễn một thế cờ có ô 2, 6, 8 trống

**Mức độ:** nhận biết. Mục tiêu học tập 6 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 5.1, Định nghĩa 01.18; bài giảng gốc (2025–2026), trang 28–30; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: biểu diễn một thế cờ có ô 2, 6, 8 trống](lecture-01-gioi-thieu-hoc-tang-cuong.html#/6/6) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/6/7).

::: exercise Bài tập 01.7 (Biểu diễn một thế cờ có ô 2, 6, 8 trống)
Thế cờ $u$: X ở ô 3, 4 và 9; O ở ô 1, 5 và 7; các ô 2, 6, 8 trống. Ô đánh số 1 đến 9 theo hàng, từ trái sang phải, từ trên xuống dưới. Hai người luân phiên đặt quân vào ô trống; ai có ba quân thẳng hàng theo hàng, cột hoặc đường chéo trước thì thắng. Phần thưởng của X theo Định nghĩa 01.18: $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc.

- (a) Xác định ai đi trước, đến phiên ai, và tập hành động hợp lệ $\mathcal A(u)$.
- (b) Một biểu diễn cho X chọn ô 5. Biểu diễn đó sai ở đâu.
- (c) X đánh ô 6. Xác định $R_{t+1}$, lượt có kết thúc không, và giá trị của lịch sử ngay sau nước đó.
:::

::: hint Gợi ý Bài tập 01.7
Đếm quân của mỗi bên để biết phiên đi. Ở câu (c), kiểm tra cột 3–6–9 sau khi X đánh ô 6.
:::

::: solution Lời giải Bài tập 01.7
**Câu (a).** X và O cùng có ba quân, nên người đi trước là X, và bây giờ lại đến phiên X. Kiểm tra chưa ai thắng: các đường đầy đủ trên bàn cờ là 1–5–9, 3–5–7 và 1–4–7, và mỗi đường có cả X lẫn O. Tập hành động hợp lệ là $\mathcal A(u)=\{2,6,8\}$.

**Câu (b).** Ô 5 đã có quân O, nên $5\notin\mathcal A(u)$; nước này không hợp lệ.

**Câu (c).** Sau khi X đánh ô 6, X có ô 3, 6, 9 trên cùng cột 3–6–9, nên X thắng: $R_{t+1}=+1$ và lượt kết thúc. Theo Định nghĩa 01.12, giá trị của lịch sử đã kết thúc bằng $0$.

**Kiểm tra lại.** Các đường qua ô 2 (1–2–3, 2–5–8) và qua ô 8 (7–8–9, 2–5–8) đều có quân O, nên chỉ nước 6 cho X thắng ngay. Lỗi thường gặp là ghi giá trị sau nước thắng bằng $+1$: phần thưởng của nước thắng đã nằm trong $R_{t+1}$, và theo quy ước $G_T=0$, giá trị của lịch sử đã kết thúc bằng $0$.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 01.3. Lợi tức trên dãy bốn ô có ghế

**Mức độ:** tính toán. Mục tiêu học tập 3 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 3.2–3.3; Sutton và Barto (2018), §3.3, tr. 54–57; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: lợi tức trên dãy bốn ô có ghế](lecture-01-gioi-thieu-hoc-tang-cuong.html#/4/7) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/4/8).

::: exercise Bài tập 01.3 (Lợi tức trên dãy bốn ô có ghế)
Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác. Cách đặt phần thưởng có thêm $-1$ cho bước robot va vào một chiếc ghế. Trong một lượt, robot nhận dãy phần thưởng $(R_1,R_2,R_3,R_4)=(0,-1,0,1)$ và lượt kết thúc ở $T=4$. Lợi tức là $G_t=\sum_{k=t+1}^{T}R_k$ (công thức (3.1)), và theo Mệnh đề 01.9, $G_t=R_{t+1}+G_{t+1}$ với $G_T=0$ (công thức (3.2)).

- (a) Tính $G_4,G_3,G_2,G_1,G_0$ theo chiều ngược bằng (3.2), rồi kiểm tra $G_0$ bằng (3.1).
- (b) Trong các bước $t=0,1,2,3$, bước nào có lợi tức nhỏ hơn phần thưởng cuối $R_4$, và vì sao.
:::

::: hint Gợi ý Bài tập 01.3
$G_t$ cộng các phần thưởng có chỉ số từ $t+1$ đến $T$; $G_T=0$.
:::

::: solution Lời giải Bài tập 01.3
**Câu (a).** $G_4=0$; $G_3=R_4+G_4=1$; $G_2=R_3+G_3=0+1=1$; $G_1=R_2+G_2=-1+1=0$; $G_0=R_1+G_1=0+0=0$. Theo (3.1), $G_0=0+(-1)+0+1=0$.

**Câu (b).** $G_0=G_1=0<1=R_4$. Hai lợi tức này còn chứa phần thưởng $R_2=-1$ của bước va ghế, xảy ra sau bước $0$ và bước $1$. Từ bước $2$ trở đi, phần thưởng $-1$ đã ở quá khứ nên $G_2=G_3=1$. Ngoài khoảng được hỏi, $G_4=0<1$ vì sau thời điểm kết thúc không còn phần thưởng nào.

**Kiểm tra lại.** Tổng mọi phần thưởng của lượt là $0$, bằng $G_0$. Lợi tức từ bước $1$ bắt đầu ở $R_2$, nên $G_1$ chứa phần thưởng va ghế; người bắt đầu tổng ở $R_3$ được $G_1=1$, sai. Gán $G_4=R_4=1$ thay cho $G_4=0$ làm mọi lợi tức tính ngược lớn hơn đúng $1$.
:::

### Bài tập 01.4. Lợi tức tích lũy và chi phí tính toán

**Mức độ:** chứng minh (câu a) và tính toán (câu b). Mục tiêu học tập 3 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 3.3, Mệnh đề 01.9; Sutton và Barto (2018), §3.3, tr. 54–57.

::: exercise Bài tập 01.4 (Lợi tức tích lũy và chi phí tính toán)
Một lượt kết thúc tại $T$ hữu hạn với các phần thưởng $R_1,\dots,R_T$; lợi tức là $G_t=\sum_{k=t+1}^{T}R_k$ (công thức (3.1)), với $G_T=0$, và thỏa $G_t=R_{t+1}+G_{t+1}$ (công thức (3.2)).

- (a) Chứng minh $G_0=\sum_{k=1}^{t}R_k+G_t$ với mọi $t=0,1,\dots,T$, trong đó tổng rỗng bằng $0$.
- (b) Đếm số phép cộng cần để tính $G_0,\dots,G_{T-1}$ nếu tính mỗi $G_t$ trực tiếp bằng (3.1), và nếu tính ngược bằng (3.2); áp dụng với $T=4$.
:::

::: hint Gợi ý Bài tập 01.4
Câu (a): tách tổng $\sum_{k=1}^{T}$ tại chỉ số $t$. Câu (b): một tổng $m$ số hạng cần $m-1$ phép cộng.
:::

::: solution Lời giải Bài tập 01.4
**Câu (a).** Theo (3.1), $G_0=\sum_{k=1}^{T}R_k$. Với $0\le t\le T$, tách tổng tại $t$:

$$
\begin{aligned}
G_0&=\sum_{k=1}^{T}R_k &&\text{(định nghĩa (3.1) tại } t=0\text{)}\\
&=\sum_{k=1}^{t}R_k+\sum_{k=t+1}^{T}R_k &&\text{(tách tổng tại chỉ số } t\text{)}\\
&=\sum_{k=1}^{t}R_k+G_t &&\text{(định nghĩa (3.1) tại bước } t\text{)}.
\end{aligned}
$$

Khi $t=0$, tổng thứ nhất rỗng; khi $t=T$, tổng thứ hai rỗng và $G_T=0$. $\square$

**Câu (b).** Tính trực tiếp, $G_t$ là tổng của $T-t$ số hạng nên cần $T-t-1$ phép cộng; tổng số là $\sum_{t=0}^{T-1}(T-t-1)=0+1+\dots+(T-1)=\frac{T(T-1)}{2}$. Tính ngược, $G_{T-1}=R_T$ không cần phép cộng nào, và mỗi $G_t=R_{t+1}+G_{t+1}$ với $t=T-2,\dots,0$ cần một phép cộng, tổng cộng $T-1$ phép cộng. Với $T=4$: tính trực tiếp cần $\frac{4\cdot3}{2}=6$ phép cộng, tính ngược cần $3$.

**Kiểm tra lại.** Với $T=4$, tính trực tiếp: $G_0$ cần $3$ phép cộng, $G_1$ cần $2$, $G_2$ cần $1$, $G_3$ cần $0$, tổng $6$; tính ngược: $G_2$, $G_1$, $G_0$, mỗi số một phép cộng. Đếm $m$ phép cộng cho một tổng $m$ số hạng cho $\frac{T(T+1)}{2}=10$ phép cộng khi tính trực tiếp. Khi tính ngược, coi $G_{T-1}=R_T+G_T$ là một phép cộng cho $T=4$ thay cho $3$. Ở câu (a), bỏ trường hợp $t=T$ làm chứng minh thiếu đúng chỗ cần quy ước $G_T=0$.
:::

### Bài tập 01.5. Giá trị của robot dưới một chính sách ngẫu nhiên

**Mức độ:** tính toán. Mục tiêu học tập 4 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 4.2, Định nghĩa 01.12; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: giá trị của robot dưới chính sách ngẫu nhiên](lecture-01-gioi-thieu-hoc-tang-cuong.html#/5/6) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/5/7).

::: exercise Bài tập 01.5 (Giá trị của robot dưới một chính sách ngẫu nhiên)
Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác. Hành động $\text{phải}$ dịch robot sang phải một ô, robot đứng yên nếu đang ở ô 4; $\text{hút}$ làm sạch ô đang đứng. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Trong bài này, lượt bị cắt sau $L=4$ hành động. Chính sách $\pi$ chọn $\text{phải}$ hoặc $\text{hút}$, mỗi hành động với xác suất $\frac12$, không phụ thuộc lịch sử. Gọi $h_0$ là lịch sử ban đầu; giá trị là $v_\pi(h_0)=\mathbb E_\pi[G_0\mid H_0=h_0]$.

- (a) Lợi tức $G_0$ nhận những giá trị nào.
- (b) Tính $v_\pi(h_0)$.
- (c) Tính $v_{\pi_1}(h_0)$ với $\pi_1$: thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$. Giải thích vì sao hai giá trị khác nhau.
:::

::: hint Gợi ý Bài tập 01.5
Phần thưởng khác $0$ chỉ có thể đến ở một bước. Đếm các dãy bốn hành động đưa robot tới ô 4 rồi hút.
:::

::: solution Lời giải Bài tập 01.5
**Câu (a).** Phần thưởng khác $0$ duy nhất là $+1$ ở bước hút được rác, và sau bước đó lượt kết thúc. Do đó $G_0=1$ nếu robot hút được rác trong bốn hành động và $G_0=0$ nếu không.

**Câu (b).** Muốn hút ở ô 4, robot cần ba lần $\text{phải}$ để đi từ ô 1 tới ô 4, rồi một lần $\text{hút}$, tổng cộng bốn hành động. Với $L=4$, không còn chỗ cho hành động thừa, nên dãy duy nhất cho $G_0=1$ là $\text{phải},\text{phải},\text{phải},\text{hút}$. Mỗi hành động được chọn độc lập với xác suất $\frac12$, nên

$$
\Pr(G_0=1)=\Big(\frac12\Big)^4=\frac1{16},\qquad v_\pi(h_0)=1\cdot\frac1{16}+0\cdot\frac{15}{16}=\frac1{16}.
$$

**Câu (c).** Dưới $\pi_1$, robot thấy $\text{sạch}$ ở ô 1, 2, 3 nên sang phải ba lần, thấy $\text{bẩn}$ ở ô 4 nên hút. Lượt luôn là $\text{phải},\text{phải},\text{phải},\text{hút}$ với $G_0=1$, nên $v_{\pi_1}(h_0)=1$. Hai giá trị khác nhau vì cùng lịch sử ban đầu nhưng chính sách khác nhau; giá trị là một hàm của chính sách (Định nghĩa 01.12).

**Kiểm tra lại.** $16$ dãy bốn hành động trên $\{\text{phải},\text{hút}\}$ có cùng xác suất $\frac1{16}$, và chỉ một dãy cho $G_0=1$. Lượt kết thúc ngay khi hút được rác, nên không có phần thưởng nào của các bước sau để cộng thêm. Dùng xác suất $\frac13$ cho mỗi hành động, như thể robot còn hành động $\text{trái}$, cho $\big(\frac13\big)^4=\frac1{81}$; đó là giá trị của chính sách chọn đều trên ba hành động ở Tình huống 01.1 của ghi chú, không phải của $\pi$.
:::

### Bài tập 01.6. Chọn chế độ hút

**Mức độ:** tính toán (câu b, c) và nhận biết (câu a); bài xếp ở mức tính toán vì hai trong ba câu là phép tính. Mục tiêu học tập 5 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 4.4, Ví dụ 01.9; số liệu sư phạm tự xây dựng.

**Trùng trang chiếu:** [Bài tập: chọn chế độ hút](lecture-01-gioi-thieu-hoc-tang-cuong.html#/5/14) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/5/15).

::: exercise Bài tập 01.6 (Chọn chế độ hút)
Robot có hai chế độ hút A và B; phần thưởng của mỗi lần hút là tỉ lệ bụi được hút sạch, trong $[0,1]$. Chế độ A đã dùng $N(\mathrm A)=20$ lần với trung bình $\bar r(\mathrm A)=0{,}60$. Chế độ B đã dùng $N(\mathrm B)=2$ lần với các phần thưởng $0{,}50$ và $0{,}60$.

| Chế độ $a$ | Số lần thử $N(a)$ | Tổng phần thưởng | Trung bình mẫu $\bar r(a)$ |
|---|---:|---:|---:|
| A | $20$ | $12{,}00$ | $0{,}60$ |
| B | $2$ | $1{,}10$ | $0{,}55$ |

- (a) Nêu hành động tham lam theo ước lượng hiện có, và cho biết chọn B ở lần tới là khai thác hay thăm dò.
- (b) Robot thử B thêm một lần và nhận $0{,}90$. Tính $N(\mathrm B)$, $\bar r(\mathrm B)$ mới và hành động tham lam mới.
- (c) Làm lại câu (b) nếu phần thưởng của lần thử thêm là $0{,}40$.
:::

::: hint Gợi ý Bài tập 01.6
Trung bình mới bằng tổng phần thưởng mới chia cho số lần thử mới.
:::

::: solution Lời giải Bài tập 01.6
**Câu (a).** $\bar r(\mathrm A)=0{,}60>\bar r(\mathrm B)=\frac{0{,}50+0{,}60}{2}=0{,}55$, nên A là hành động tham lam. Chọn B là chọn hành động không tham lam, tức là thăm dò (Định nghĩa 01.16).

**Câu (b).** $N(\mathrm B)=3$ và $\bar r(\mathrm B)=\frac{0{,}50+0{,}60+0{,}90}{3}=\frac{2{,}00}{3}\approx0{,}667$. Vì $0{,}667>0{,}60$, hành động tham lam mới là B.

**Câu (c).** $N(\mathrm B)=3$ và $\bar r(\mathrm B)=\frac{0{,}50+0{,}60+0{,}40}{3}=\frac{1{,}50}{3}=0{,}50$. Hành động tham lam vẫn là A, với khoảng cách lớn hơn trước.

**Kiểm tra lại.** Hai giá trị $\frac{2{,}00}{3}$ và $0{,}50$ nằm trong khoảng $\big[\frac{11}{30},\frac7{10}\big]\approx[0{,}367;\,0{,}700]$ của Ví dụ 01.9, đúng với một lần thử thêm có phần thưởng trong $[0,1]$. Lấy trung bình của hai số $0{,}55$ và $0{,}90$ cho $0{,}725$, sai vì $0{,}55$ đã gộp hai lần thử; trung bình đúng chia tổng phần thưởng $2{,}00$ cho $3$. Ở câu (a), gọi thăm dò là "chọn ngẫu nhiên" cũng sai: thăm dò là chọn một hành động không tham lam, dù chọn có chủ đích.
:::

### Bài tập 01.8. Nước khai thác một bước theo một chính sách khác

**Mức độ:** tính toán. Mục tiêu học tập 6 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 5.4, Mệnh đề 01.20, Định nghĩa 01.21, Ví dụ 01.10; bài giảng gốc (2025–2026), trang 28–30; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 01.8 (Nước khai thác một bước theo một chính sách khác)
Thế cờ $s$: X ở ô 1 và 5; O ở ô 2, 4 và 8; các ô 3, 6, 7, 9 trống; đến phiên X. Luật một bước theo Định nghĩa 01.18, đối thủ O chọn đều trên các ô trống. Sau nước đầu, X tiếp tục theo chính sách $\pi_w$: nếu có nước làm X thắng ngay thì đánh nước đó, nếu có nhiều nước như vậy thì chọn đều trong số đó, nếu không có thì chọn đều trên các ô trống. Phần thưởng: $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc; giá trị sau khi lượt kết thúc bằng $0$. Theo công thức (5.3) của ghi chú, nước khai thác một bước theo $v_{\pi_w}$ là một phần tử của tập

$$
\arg\max_{a\in\mathcal A(s)}\mathbb E\big[R_{t+1}+v_{\pi_w}(S_{t+1})\mid S_t=s,A_t=a\big] .
$$

Bảng sau cho giá trị $v_{\pi_w}$ của thế cờ sau nước trả lời của O, trừ một ô cần tính:

| Nước $a$ | O đánh ô | Giá trị $v_{\pi_w}$ của thế cờ kế tiếp |
|---|---|---:|
| $3$ | $6$; $7$; $9$ | $1$; $1$; $1$ |
| $6$ | $3$; $7$; $9$ | $1$; $1$; chưa biết |
| $7$ | $3$; $6$; $9$ | $1$; $1$; $1$ |

- (a) Tính giá trị $v_{\pi_w}$ của thế cờ sau nước 6 của X và nước 9 của O.
- (b) Tính $\mathbb E[R_{t+1}+v_{\pi_w}(S_{t+1})\mid S_t=s,A_t=a]$ cho bốn nước, và tập $\arg\max$ trong (5.3).
- (c) Dùng quy tắc phá hòa (tie-breaking) "chọn ô có số nhỏ nhất" để xác định nước khai thác một bước, rồi so với Ví dụ 01.10 của ghi chú, nơi nước khai thác một bước theo $v_{\pi_u}$ là ô 9.
:::

::: hint Gợi ý Bài tập 01.8
Với hai ô trống, trước hết kiểm tra X có nước thắng ngay không; nếu có, $\pi_w$ đánh nước đó.
:::

::: solution Lời giải Bài tập 01.8
**Câu (a).** X ở ô 1, 5, 6; O ở ô 2, 4, 8, 9; ô 3 và 7 trống. Ô 3 không cho X thắng, vì 1–2–3 có O, 3–6–9 có O, 3–5–7 còn trống ô 7; ô 7 không cho X thắng, vì 1–4–7 và 7–8–9 có O, 3–5–7 còn trống ô 3. Vậy $\pi_w$ chọn đều: X đánh ô 3 thì O đánh ô 7 và thắng bằng 7–8–9, cho $-1$; X đánh ô 7 thì O đánh ô 3, hòa, cho $0$. Giá trị là $\frac12(-1)+\frac12\cdot0=-\frac12$.

**Câu (b).** Với $a=3$, $6$, $7$, phần thưởng của bước bằng $0$, vì X chưa thắng và O không thắng được bằng một nước.

$$
\begin{aligned}
a=3:&\quad 0+\tfrac13(1+1+1)=1,\\
a=6:&\quad 0+\tfrac13\big(1+1-\tfrac12\big)=\tfrac12,\\
a=7:&\quad 0+\tfrac13(1+1+1)=1,\\
a=9:&\quad 1+0=1 .
\end{aligned}
$$

Tập $\arg\max$ là $\{3,7,9\}$.

**Câu (c).** Quy tắc phá hòa chọn ô 3. Trong Ví dụ 01.10, theo $v_{\pi_u}$, chỉ ô 9 đạt cực đại. Hai kết quả khác nhau vì giá trị được tính theo hai chính sách tiếp tục khác nhau: dưới $\pi_w$, X không bỏ lỡ nước thắng ở nước sau, nên nước 3 và nước 7 cũng chắc chắn thắng.

**Kiểm tra lại.** Ở câu (a), X không có nước thắng ngay, nên $\pi_w$ và $\pi_u$ cùng chọn đều, và giá trị $-\frac12$ trùng dòng $a=6$, O đánh 9 trong bảng của Ví dụ 01.10. Nếu cho rằng $\pi_w$ luôn thắng và ghi giá trị $1$ ở câu (a), nước 6 cũng đạt cực đại, sai. Với nước 9, giá trị sau khi lượt kết thúc bằng $0$; ghi giá trị đó bằng $1$ rồi cộng với $R_{t+1}=+1$ cho tổng $2$, sai.
:::

### Bài tập 01.12. Giá trị khi môi trường không ngẫu nhiên và chính sách xác định

**Mức độ:** chứng minh (câu a) và tính toán (câu b). Mục tiêu học tập 4 của ghi chú.

**Nguồn:** ghi chú bài giảng Bài 01, Mục 4.2, Định nghĩa 01.11 và 01.12; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 01.12 (Giá trị khi môi trường không ngẫu nhiên và chính sách xác định)
Giả sử môi trường không ngẫu nhiên, tức là với mỗi lịch sử và hành động, phần thưởng kế tiếp, quan sát kế tiếp và việc lượt có kết thúc hay không được xác định duy nhất, và $\pi$ là một chính sách xác định (deterministic policy), tức là mỗi $\pi(\cdot\mid h)$ dồn toàn bộ xác suất vào một hành động. Mọi lượt kết thúc sau nhiều nhất $L$ hành động. Cho một lịch sử $h$ đến bước $t$ của một lượt chưa kết thúc; giá trị là $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$.

- (a) Chứng minh rằng từ $h$, lượt có đúng một diễn biến tiếp theo, và $v_\pi(h)$ bằng lợi tức $G_t$ của diễn biến đó.
- (b) Áp dụng cho robot dọn dãy bốn ô: robot bắt đầu ở ô 1, chỉ ô 4 có rác; $\text{trái}$, $\text{phải}$ dịch một ô, đứng yên nếu đi ra ngoài dãy; $\text{hút}$ làm sạch ô đang đứng; hút ở ô 4 khi còn rác cho $+1$ và kết thúc lượt, mọi bước khác cho $0$; cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$; $L=5$. Chính sách $\pi_1$: thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$. Lịch sử $h=(\text{sạch},\text{phải},0,\text{sạch},\text{hút},0,\text{sạch})$. Tính $v_{\pi_1}(h)$.
:::

::: hint Gợi ý Bài tập 01.12
Chứng minh câu (a) theo từng bước: nếu diễn biến đến bước $j$ là duy nhất, thì hành động và phản hồi ở bước $j$ cũng duy nhất. Ở câu (b), trước hết xác định vị trí của robot và số hành động còn lại sau $h$.
:::

::: solution Lời giải Bài tập 01.12
**Câu (a).** Lập luận theo bước $j=t,t+1,\dots$.

**Bước 1 (một bước duy nhất).** Giả sử lịch sử đến bước $j$ được xác định duy nhất, là $h_j$; với $j=t$ thì $h_t=h$. Vì $\pi$ xác định, $A_j$ là hành động duy nhất mà $\pi(\cdot\mid h_j)$ gán xác suất $1$. Vì môi trường không ngẫu nhiên, $R_{j+1}$, $O_{j+1}$ và việc kết thúc được xác định duy nhất từ $h_j$ và $A_j$. Do đó lịch sử đến bước $j+1$ cũng duy nhất.

**Bước 2 (cả diễn biến duy nhất).** Lượt kết thúc sau nhiều nhất $L$ bước, nên sau hữu hạn lần áp dụng Bước 1, cả diễn biến từ $h$ đến khi kết thúc là duy nhất, với một lợi tức $g$ xác định.

**Bước 3 (kỳ vọng của một hằng số).** Dưới phân phối của diễn biến bắt đầu từ $h$ (Định nghĩa 01.12), $G_t$ nhận giá trị $g$ với xác suất $1$, nên $v_\pi(h)=g$. Điều này đúng cả khi $\Pr_\pi(H_t=h)=0$, vì Định nghĩa 01.12 hiểu (4.1) theo phân phối của diễn biến bắt đầu từ $h$. $\square$

**Câu (b).** Theo $h$, robot sang ô 2 ở bước $0$ rồi hút tại ô 2 sạch ở bước $1$, nên ở bước $2$ robot đứng ở ô 2 và còn ba hành động. Theo $\pi_1$, robot thấy $\text{sạch}$ nên sang phải tới ô 3, lại thấy $\text{sạch}$ nên sang phải tới ô 4, rồi thấy $\text{bẩn}$ và hút ở hành động thứ năm: $R_3=R_4=0$, $R_5=+1$, $T=5\le L$. Theo câu (a), $v_{\pi_1}(h)=G_2=0+0+1=1$.

**Kiểm tra lại.** Tổng số hành động của lượt là $2+3=5$, đúng bằng $L$, nên lần hút cuối vẫn kịp trước khi lượt bị cắt. Lịch sử $h$ chứa hành động $\text{hút}$ ở ô sạch mà $\pi_1$ không bao giờ chọn; Định nghĩa 01.12 vẫn cho $v_{\pi_1}(h)$ nghĩa, vì giá trị chỉ dùng $\pi_1$ cho các hành động từ bước $2$ trở đi. Kết luận $v_{\pi_1}(h)=0$ vì "lượt này không theo $\pi_1$" là trộn hành động đã xảy ra với hành động do chính sách chọn về sau. Giới hạn $L$ quyết định kết quả: với $L=4$, robot chỉ còn hai hành động sau $h$, tới ô 4 mà không kịp hút, và $v_{\pi_1}(h)=0$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 01.13. Robot dọn dãy bốn ô, tổng hợp

**Mức độ:** vận dụng. Mục tiêu học tập 1, 3 và 4 của ghi chú, cùng phân tích một bước của Mục 5.4.

**Nguồn:** ghi chú bài giảng Bài 01, Định nghĩa 01.2, Nhận xét 01.3, Mệnh đề 01.9, Định nghĩa 01.12, Mệnh đề 01.20, Tình huống 01.1 và 01.2; số liệu sư phạm tự xây dựng. Hai số ở câu (c), (d) là $w(2,3)=\frac1{27}$ và $w(3,2)=\frac19$ đã tính trong Tình huống 01.1 của ghi chú; câu (e) chỉ có trong tệp này.

**Trùng trang chiếu:** [Bài tập: robot dọn dãy bốn ô, tổng hợp](lecture-01-gioi-thieu-hoc-tang-cuong.html#/7/4) và [trang lời giải](lecture-01-gioi-thieu-hoc-tang-cuong.html#/7/5), các câu (a)–(d).

::: exercise Bài tập 01.13 (Robot dọn dãy bốn ô, tổng hợp)
Dãy bốn ô đánh số 1 đến 4; chỉ ô 4 có rác. Robot bắt đầu ở ô 2. Ba hành động $\text{trái}$, $\text{phải}$, $\text{hút}$: $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ làm sạch ô đang đứng. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$ cho ô đang đứng. Trạng thái là cặp (vị trí, tình trạng ô 4). Lượt bị cắt sau $L=3$ hành động. Chính sách $\pi_u$ chọn mỗi hành động với xác suất $\frac13$, không phụ thuộc lịch sử; $h_0$ là lịch sử ban đầu. Theo Mệnh đề 01.20, với một hành động $a$ ở bước $0$, có hai đẳng thức. Đẳng thức (1):

$$
\mathbb E_{\pi_u}\big[G_0\mid H_0=h_0,A_0=a\big]=\mathbb E\big[R_1+v_{\pi_u}(H_1)\mid H_0=h_0,A_0=a\big],
$$

với quy ước $v_{\pi_u}(H_1)=0$ nếu lượt kết thúc ở bước $1$. Đẳng thức (2):

$$
v_{\pi_u}(h_0)=\sum_a\tfrac13\,\mathbb E_{\pi_u}\big[G_0\mid H_0=h_0,A_0=a\big].
$$

- (a) Viết $S_0$, $O_0$ và tập hành động hợp lệ.
- (b) Lượt $\text{phải},\text{phải},\text{hút}$ xảy ra. Tính $G_3,G_2,G_1,G_0$ bằng hệ thức đệ quy $G_t=R_{t+1}+G_{t+1}$.
- (c) Tính $v_{\pi_u}(h_0)$ trực tiếp từ định nghĩa giá trị.
- (d) Tìm nước khai thác một bước theo $v_{\pi_u}$ tại $h_0$, tức hành động làm lớn nhất vế phải của (1); kiểm tra kết quả (c) bằng (2).
- (e) Giữ các luật trên và $L=3$, nhưng robot không biết mình xuất phát ở ô 1, 2 hay 3: mỗi ô có xác suất $\frac13$, và cả ba cho cùng $O_0=\text{sạch}$, nên lịch sử ban đầu vẫn là $h_0=(\text{sạch})$. Sau hành động đầu, robot theo $\pi_u$. Tính $\mathbb E_{\pi_u}[G_0\mid H_0=h_0,A_0=a]$ cho ba hành động, với kỳ vọng lấy theo cả ô xuất phát; xác định nước khai thác một bước và so với câu (d).
:::

::: hint Gợi ý Bài tập 01.13
Từ ô $k$, robot cần $4-k$ lần $\text{phải}$ rồi một lần $\text{hút}$; đếm các dãy thành công trong số hành động còn lại. Ở câu (e), tính riêng cho từng ô xuất phát rồi lấy trung bình; từ ô 4, robot có thể hút ngay.
:::

::: solution Lời giải Bài tập 01.13
**Câu (a).** $S_0=(2,\text{còn rác})$, $O_0=\text{sạch}$ vì ô 2 sạch, và tập hành động hợp lệ là $\{\text{trái},\text{phải},\text{hút}\}$.

**Câu (b).** Robot sang ô 3, sang ô 4, rồi hút được rác: $(R_1,R_2,R_3)=(0,0,1)$ và $T=3\le L$.

- $G_3=0$;
- $G_2=R_3+G_3=1+0=1$;
- $G_1=R_2+G_2=0+1=1$;
- $G_0=R_1+G_1=0+1=1$.

**Câu (c).** Từ ô 2, robot cần hai lần $\text{phải}$ rồi một lần $\text{hút}$, đúng ba hành động, nên với $L=3$ dãy duy nhất cho $G_0=1$ là $\text{phải},\text{phải},\text{hút}$; mọi diễn biến khác cho $G_0=0$. Mỗi hành động có xác suất $\frac13$, nên $v_{\pi_u}(h_0)=1\cdot\big(\frac13\big)^3=\frac1{27}$.

**Câu (d).** Không hành động nào ở bước $0$ cho phần thưởng khác $0$, vì robot đứng ở ô 2 sạch, nên $R_1=0$ và lượt chưa kết thúc. Vị trí ban đầu đã biết và luật dịch chuyển không ngẫu nhiên, nên $H_1$ xác định vị trí mới; vì $\pi_u$ không dùng lịch sử, $v_{\pi_u}(H_1)$ là xác suất hút được rác trong hai hành động còn lại từ vị trí đó.

- Sau $\text{trái}$: robot ở ô 1, cần bốn hành động, chỉ còn hai, nên $v_{\pi_u}(H_1)=0$.
- Sau $\text{phải}$: robot ở ô 3, thành công khi chọn $\text{phải}$ rồi $\text{hút}$, nên $v_{\pi_u}(H_1)=\big(\frac13\big)^2=\frac19$.
- Sau $\text{hút}$ ở ô 2 sạch: robot vẫn ở ô 2, cần ba hành động, chỉ còn hai, nên $v_{\pi_u}(H_1)=0$.

Vế phải của (1) bằng $0$, $\frac19$, $0$ lần lượt cho $\text{trái}$, $\text{phải}$, $\text{hút}$, nên nước khai thác một bước là $\text{phải}$. Kiểm tra bằng (2):

$$
v_{\pi_u}(h_0)=\tfrac13\big(0+\tfrac19+0\big)=\tfrac1{27},
$$

khớp câu (c). Nước khai thác một bước trùng hành động đầu của $\pi_1$, dù $v_{\pi_u}(h_0)$ chỉ bằng $\frac1{27}$. Phép tính dùng luật đã biết của môi trường, nên đây là lập kế hoạch với mô hình (Định nghĩa 01.14).

**Câu (e).** Ký hiệu $w(k,m)$ là xác suất hút được rác trong $m$ hành động còn lại khi robot đứng ở ô $k$ và theo $\pi_u$, như trong Tình huống 01.1 của ghi chú. Sau hành động đầu còn $m=2$ hành động. Ngoài $w(1,2)=w(2,2)=0$ và $w(3,2)=\frac19$ của câu (d), cần thêm $w(4,2)$: từ ô 4, robot hút ngay với xác suất $\frac13$; chọn $\text{phải}$ thì đứng yên ở ô 4 rồi hút với xác suất $\frac13\cdot\frac13$; chọn $\text{trái}$ thì sang ô 3 với một hành động còn lại, không kịp. Vậy $w(4,2)=\frac13+\frac19=\frac49$. Ở bước $0$ không ô xuất phát nào là ô 4, nên $R_1=0$ ở mọi trường hợp. Giá trị của phần còn lại sau mỗi hành động đầu:

| Ô xuất phát | Sau $\text{trái}$ | Sau $\text{phải}$ | Sau $\text{hút}$ |
|---|---:|---:|---:|
| 1 | $w(1,2)=0$ | $w(2,2)=0$ | $w(1,2)=0$ |
| 2 | $w(1,2)=0$ | $w(3,2)=\frac19$ | $w(2,2)=0$ |
| 3 | $w(2,2)=0$ | $w(4,2)=\frac49$ | $w(3,2)=\frac19$ |

Lấy trung bình theo ô xuất phát, mỗi ô với xác suất $\frac13$:

$$
\begin{aligned}
a=\text{trái}:&\quad \tfrac13(0+0+0)=0,\\
a=\text{phải}:&\quad \tfrac13\big(0+\tfrac19+\tfrac49\big)=\tfrac5{27},\\
a=\text{hút}:&\quad \tfrac13\big(0+0+\tfrac19\big)=\tfrac1{27}.
\end{aligned}
$$

Nước khai thác một bước vẫn là $\text{phải}$, như câu (d), nhưng $\text{hút}$ không còn có giá trị $0$: nếu robot đang ở ô 3, hút ở ô sạch giữ robot ở ô 3, nơi hai hành động còn lại vẫn đủ để tới rác. Cùng quan sát $\text{sạch}$ ứng với ba trạng thái (Nhận xét 01.3), nên giá trị trên lịch sử $h_0$ là trung bình theo phân phối của trạng thái ẩn, và đổi phân phối ô xuất phát thì đổi các số trên, như Tình huống 01.2 của ghi chú.

**Kiểm tra lại.** Ở câu (e), theo (2), $v_{\pi_u}(h_0)=\frac13\big(0+\frac5{27}+\frac1{27}\big)=\frac2{27}$; tính trực tiếp theo ô xuất phát, $w(1,3)=0$, $w(2,3)=\frac1{27}$, $w(3,3)=\frac13\big(0+\frac49+\frac19\big)=\frac5{27}$, trung bình $\frac13\cdot\frac6{27}=\frac2{27}$, khớp. Ghi giá trị sau $\text{phải}$ ở câu (d) bằng $\frac13$ là quên rằng từ ô 3 còn cần hai hành động đúng. Ghi $G_3=1$ vì phần thưởng $+1$ đến ở bước cuối cũng sai: theo quy ước $G_T=0$, phần thưởng đó nằm trong $G_2$. Ở câu (e), coi $O_0=\text{sạch}$ là trạng thái rồi dùng các số của câu (d) cho mọi ô xuất phát là bỏ qua việc cảm biến không phân biệt ô 1, 2, 3.
:::

### Bài tập 01.14. Hai thiết kế phần thưởng cho robot dọn nhà

**Mức độ:** vận dụng. Mục tiêu học tập 3 của ghi chú, cùng giả thuyết phần thưởng (reward hypothesis) của Mục 3.4.

**Nguồn:** bài giảng gốc (2025–2026), trang 24–25; Sutton và Barto (2018), §3.2, tr. 53–54; ghi chú bài giảng Bài 01, Nhận xét 01.10 và Ví dụ 01.5; số liệu sư phạm tự xây dựng. Phần D1 của câu (a) với $\tau_1$, $\tau_2$ lấy lại phép tính của Ví dụ 01.5 (lượt A, lượt B sau khi sửa phần thưởng); thiết kế D2, lượt $\tau_3$ và các câu (b)–(d) chỉ có trong tệp này.

::: exercise Bài tập 01.14 (Hai thiết kế phần thưởng cho robot dọn nhà)
Robot dọn dãy bốn ô bắt đầu ở ô 1; chỉ ô 4 có rác; ô 2 có một bình hoa. Ba hành động $\text{trái}$, $\text{phải}$, $\text{hút}$: $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ giữ nguyên vị trí. Hút ở ô 4 khi còn rác làm sạch rác và kết thúc lượt; lần đầu robot chọn $\text{hút}$ khi đứng ở ô 2, bình hoa bị đổ. Lượt bị cắt sau $L=5$ hành động, trừ câu (c). Mục tiêu của người thiết kế là robot hút rác ở ô 4 và không làm đổ đồ. Hai thiết kế phần thưởng được đề xuất:

- D1: $+1$ cho bước hút được rác, $-1$ cho bước làm đổ bình hoa, $0$ cho mọi bước khác;
- D2: như D1, cộng thêm $b=0{,}2$ cho mọi bước chọn $\text{hút}$, kể cả bước hút được rác và bước làm đổ bình hoa, với ý định khuyến khích robot hút bụi.

Ba lượt được ghi lại: $\tau_1$ là $\text{phải},\text{phải},\text{phải},\text{hút}$; $\tau_2$ là $\text{phải},\text{hút},\text{phải},\text{phải},\text{hút}$, trong đó lần hút thứ nhất ở ô 2 làm đổ bình hoa; $\tau_3$ là năm lần $\text{hút}$ liên tiếp ở ô 1.

- (a) Viết dãy phần thưởng, $T$ và lợi tức $G_0$ của ba lượt dưới mỗi thiết kế. Với $\tau_2$ dưới D2, tính $G_5,\dots,G_0$ bằng hệ thức $G_t=R_{t+1}+G_{t+1}$.
- (b) Dưới mỗi thiết kế, với $L=5$, xác định lợi tức $G_0$ lớn nhất trên mọi dãy hành động và các lượt đạt giá trị đó.
- (c) Dưới D2, đổi giới hạn thành $L=10$, các luật khác giữ nguyên. So sánh $G_0$ của $\tau_1$ với $G_0$ của lượt chỉ hút ở ô 1 suốt mười hành động; xác định lợi tức lớn nhất và hành vi đạt được nó.
- (d) Thiết kế nào phù hợp mục tiêu của người thiết kế. Nêu nguyên tắc đặt phần thưởng rút ra từ (b) và (c).
:::

::: hint Gợi ý Bài tập 01.14
Lượt kết thúc ngay khi hút được rác, nên bước hút được rác luôn là bước cuối. Muốn hút được rác, robot cần ít nhất ba lần $\text{phải}$; dưới D2, mỗi hành động thừa đem lại nhiều nhất $b$.
:::

::: solution Lời giải Bài tập 01.14
**Câu (a).** Ba lượt có $T=4$, $T=5$ và $T=5$; $\tau_3$ không hút được rác và bị cắt ở giới hạn.

Dưới D1:

| Lượt | Phần thưởng | $G_0$ |
|---|---|---:|
| $\tau_1$ | $(0,0,0,1)$ | $1$ |
| $\tau_2$ | $(0,-1,0,0,1)$ | $0$ |
| $\tau_3$ | $(0,0,0,0,0)$ | $0$ |

Dưới D2:

| Lượt | Phần thưởng | $G_0$ |
|---|---|---:|
| $\tau_1$ | $(0;\,0;\,0;\,1{,}2)$ | $1{,}2$ |
| $\tau_2$ | $(0;\,-0{,}8;\,0;\,0;\,1{,}2)$ | $0{,}4$ |
| $\tau_3$ | $(0{,}2;\,0{,}2;\,0{,}2;\,0{,}2;\,0{,}2)$ | $1{,}0$ |

Với $\tau_2$ dưới D2: $G_5=0$; $G_4=1{,}2+0=1{,}2$; $G_3=0+1{,}2=1{,}2$; $G_2=0+1{,}2=1{,}2$; $G_1=-0{,}8+1{,}2=0{,}4$; $G_0=0+0{,}4=0{,}4$.

**Câu (b).** Dưới D1, mọi phần thưởng thuộc $\{-1,0,1\}$ và chỉ bước hút được rác cho $+1$, nên $G_0\le1$. Giá trị $1$ đạt được bởi mọi lượt hút được rác mà không làm đổ bình hoa, như $\tau_1$ ($T=4$) hoặc $\text{phải},\text{phải},\text{phải},\text{phải},\text{hút}$ ($T=5$).

Dưới D2, xét hai trường hợp.

- Lượt hút được rác: bước đó là bước cuối và cho $1{,}2$; trước đó cần ít nhất ba lần $\text{phải}$, mỗi lần cho $0$. Với $L=5$ còn nhiều nhất một hành động thừa, cho nhiều nhất $b=0{,}2$ khi đó là một lần $\text{hút}$ ở ô 1 hoặc ô 3. Vậy $G_0\le1{,}2+0{,}2=1{,}4$.
- Lượt không hút được rác: mỗi bước cho nhiều nhất $0{,}2$, nên $G_0\le5\cdot0{,}2=1{,}0$.

Lợi tức lớn nhất là $1{,}4$, đạt bởi đúng hai lượt: $\text{hút},\text{phải},\text{phải},\text{phải},\text{hút}$ và $\text{phải},\text{phải},\text{hút},\text{phải},\text{hút}$. Robot chỉ ở ô 1 trước lần $\text{phải}$ đầu tiên và chỉ ở ô 3 giữa lần $\text{phải}$ thứ hai và lần thứ ba, nên lần hút thừa có đúng hai vị trí trong dãy. Cả hai lượt chèn một lần hút vô ích ở ô sạch và hút được rác muộn hơn $\tau_1$ một bước.

**Câu (c).** Với $L=10$, $\tau_1$ vẫn cho $G_0=1{,}2$, còn lượt chỉ hút ở ô 1 cho $G_0=10\cdot0{,}2=2{,}0>1{,}2$. Lập luận như câu (b): lượt hút được rác có nhiều nhất sáu hành động thừa, nên $G_0\le1{,}2+6\cdot0{,}2=2{,}4$; lượt không hút rác có $G_0\le10\cdot0{,}2=2{,}0$. Lợi tức lớn nhất là $2{,}4$, đạt khi robot hút sáu lần ở ô sạch không có bình hoa, đi ba lần $\text{phải}$, và chỉ hút rác ở hành động thứ mười. Với giới hạn $L$ bất kỳ, lượt chỉ hút ở ô 1 suốt $L$ hành động có lợi tức $0{,}2L$, lớn hơn $1{,}2$ của $\tau_1$ khi $L\ge7$.

**Câu (d).** D1 phù hợp mục tiêu: lợi tức lớn nhất đạt được khi và chỉ khi robot hút được rác mà không làm đổ bình hoa. D2 thưởng cho một mục tiêu con (subgoal), hành động $\text{hút}$, thay cho kết quả cần đạt; tác tử làm lớn lợi tức dưới D2 trì hoãn việc hút rác, và với lượt dài, xếp một lượt không hút rác trên một lượt hút rác ngay. Sutton và Barto (2018, §3.2) nêu cùng nguyên tắc: phần thưởng truyền đạt điều cần đạt, không truyền đạt cách đạt, vì thưởng cho mục tiêu con có thể khiến tác tử đạt mục tiêu con mà bỏ mục tiêu thật.

**Kiểm tra lại.** Cộng trực tiếp $\tau_2$ dưới D2: $0-0{,}8+0+0+1{,}2=0{,}4$. D1 không phân biệt hút rác ở $T=4$ hay $T=5$; nếu người thiết kế còn muốn robot hút sớm, chi phí di chuyển của Ví dụ 01.4 là một cách ghi điều đó vào phần thưởng. Quên phần cộng thêm $b$ ở bước làm đổ bình hoa cho $-1$ thay cho $-0{,}8$, và $G_0=0{,}2$ cho $\tau_2$. Sau bước hút được rác, lượt đã kết thúc, nên không có phần thưởng nào để cộng thêm.
:::

### Bài tập 01.15. Đăng ký môn học qua hai đợt

**Mức độ:** vận dụng. Mục tiêu học tập 1, 2, 4 và 5 của ghi chú.

**Nguồn:** bài giảng gốc (2025–2026), trang 8 (lập kế hoạch dưới bất định, với ví dụ đăng ký môn học) và trang 25 (hy sinh phần thưởng tức thời); ghi chú bài giảng Bài 01, Nhận xét 01.3, 01.4 và 01.6, Định nghĩa 01.14 và 01.16, Mệnh đề 01.20, Ví dụ 01.9; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 01.15 (Đăng ký môn học qua hai đợt)
Một sinh viên đăng ký một môn học có hai lớp: lớp sáng M và lớp chiều C. Việc đăng ký diễn ra trong hai đợt, ứng với bước $t=0$ và $t=1$. Ở mỗi đợt mà sinh viên chưa có lớp, sinh viên gửi một yêu cầu vào M hoặc vào C. Yêu cầu vào M thành công với xác suất $0{,}4$, yêu cầu vào C thành công với xác suất $0{,}8$; hai xác suất này như nhau ở hai đợt, và kết quả của hai đợt độc lập với nhau. Kết quả ở mỗi đợt do số chỗ còn trống và yêu cầu của các sinh viên khác ở đợt đó quyết định, những thứ sinh viên không thấy. Trước đợt 1, sinh viên chỉ nhận thông báo mở đăng ký, là quan sát $O_0$; sau mỗi đợt, hệ thống chỉ báo thành công hay thất bại. Vào được M cho phần thưởng $+1$, vào được C cho $+0{,}6$, vì sinh viên ưa lớp sáng hơn; khi vào được một lớp, lượt kết thúc. Một đợt thất bại cho phần thưởng $0$; sau hai đợt thất bại, lượt kết thúc.

- (a) Xác định tác tử, môi trường, hành động, quan sát, phần thưởng, giới hạn $L$ và các giá trị có thể của $T$. Nêu một thành phần của trạng thái mà sinh viên không quan sát được.
- (b) Một cách đăng ký là cặp $(a_0,a_1)$: yêu cầu ở đợt 1, và yêu cầu ở đợt 2 nếu đợt 1 thất bại. Tính $\mathbb E[R_1\mid A_0=a]$ với $a\in\{\mathrm M,\mathrm C\}$, rồi tính $\mathbb E[G_0]$ cho bốn cách đăng ký và xác định cách có $\mathbb E[G_0]$ lớn nhất.
- (c) Dùng kết quả (b) để giải thích vì sao so hai yêu cầu ở đợt 1 bằng phần thưởng kỳ vọng một bước cho lựa chọn sai. Nối kết quả với phản hồi trễ.
- (d) Phép tính ở (b) là lập kế hoạch có mô hình hay học phi mô hình. Nếu sinh viên không biết hai xác suất $0{,}4$ và $0{,}8$, nêu dữ liệu cần có và chỗ xuất hiện xung đột giữa thăm dò và khai thác.
:::

::: hint Gợi ý Bài tập 01.15
Lợi tức của cách $(a_0,a_1)$ bằng phần thưởng của đợt 1 cộng phần thưởng của đợt 2, và đợt 2 chỉ diễn ra khi đợt 1 thất bại. Kỳ vọng phần thưởng của một yêu cầu bằng xác suất thành công nhân phần thưởng khi thành công.
:::

::: solution Lời giải Bài tập 01.15
**Câu (a).** Tác tử là sinh viên, với quy tắc chọn yêu cầu ở mỗi đợt. Môi trường gồm hệ thống đăng ký, số chỗ của hai lớp và các sinh viên khác. Hành động $A_t\in\{\mathrm M,\mathrm C\}$. Quan sát $O_0$ là thông báo mở đăng ký; quan sát sau mỗi đợt là thông báo thành công hoặc thất bại. Phần thưởng $R_{t+1}$ bằng $1$, $0{,}6$ hoặc $0$. Có nhiều nhất hai đợt nên $L=2$, và $T\in\{1,2\}$: $T=1$ khi đợt 1 thành công. Số chỗ còn trống của mỗi lớp và các yêu cầu của sinh viên khác là thành phần của trạng thái mà sinh viên không quan sát được, nên quan sát khác trạng thái (Nhận xét 01.3). Giả thiết độc lập của đề nghĩa là các thành phần ẩn này được coi như rút lại ở mỗi đợt; nếu chúng mang sang đợt sau, kết quả của đợt 1 chứa thông tin về đợt 2.

**Câu (b).** Phần thưởng kỳ vọng của một yêu cầu, ở đợt nào cũng vậy:

$$
\mathbb E[R_1\mid A_0=\mathrm M]=0{,}4\cdot1=0{,}4,\qquad \mathbb E[R_1\mid A_0=\mathrm C]=0{,}8\cdot0{,}6=0{,}48 .
$$

Với cách $(a_0,a_1)$, đợt 2 chỉ diễn ra khi đợt 1 thất bại, nên

$$
\mathbb E[G_0]=\mathbb E[R_1\mid A_0=a_0]+\Pr(\text{đợt 1 thất bại})\cdot\mathbb E[R_2\mid A_1=a_1,\ \text{đợt 1 thất bại}] .
$$

Vì kết quả của đợt 2 độc lập với đợt 1, kỳ vọng cuối bằng phần thưởng kỳ vọng một bước của $a_1$ đã tính ở trên:

$$
\begin{aligned}
(\mathrm M,\mathrm M):&\quad 0{,}4+0{,}6\cdot0{,}4=0{,}64,\\
(\mathrm M,\mathrm C):&\quad 0{,}4+0{,}6\cdot0{,}48=0{,}688,\\
(\mathrm C,\mathrm M):&\quad 0{,}48+0{,}2\cdot0{,}4=0{,}56,\\
(\mathrm C,\mathrm C):&\quad 0{,}48+0{,}2\cdot0{,}48=0{,}576 .
\end{aligned}
$$

Cách tốt nhất là $(\mathrm M,\mathrm C)$: thử lớp sáng ở đợt 1, nếu thất bại thì đăng ký lớp chiều ở đợt 2, với $\mathbb E[G_0]=0{,}688$.

**Câu (c).** Ở đợt 1, C có phần thưởng kỳ vọng một bước lớn hơn, $0{,}48>0{,}4$, nhưng hành động đầu tốt nhất là M. Ở đợt 2, yêu cầu tốt nhất là C, vì $0{,}48>0{,}4$; khi đợt 2 dùng C, hành động đầu M cho $\mathbb E[G_0]=0{,}688$, còn C cho $0{,}576$. Đây là Mệnh đề 01.20(a) với lịch sử ban đầu: kỳ vọng của lợi tức sau $A_0$ gồm phần thưởng của đợt 1 và giá trị của phần còn lại, mà khi M thất bại, phần còn lại vẫn có đợt 2. Phần thưởng $R_1=0$ sau một yêu cầu M thất bại không cho biết M là lựa chọn kém; hậu quả của $A_0$ chỉ đo được sau đợt 2, và đó là phản hồi trễ (Nhận xét 01.6). Chọn M là chịu phần thưởng kỳ vọng tức thời thấp hơn để được kỳ vọng của lợi tức cao hơn, hiện tượng bài giảng gốc (trang 25) gọi là hy sinh phần thưởng tức thời.

**Câu (d).** Phép tính ở (b) dùng hai xác suất thành công đã biết, tức một mô hình của môi trường, để xét các diễn biến trước khi đăng ký; đó là lập kế hoạch có mô hình (Định nghĩa 01.14). Nếu không biết hai xác suất, sinh viên cần các kết quả thành công hay thất bại của những yêu cầu đã gửi vào M và vào C. Ước lượng tỉ lệ thành công của một lớp từ ít yêu cầu còn bất định, như chế độ B của Ví dụ 01.9; gửi yêu cầu vào lớp đang có ước lượng thấp hơn để thu thêm dữ liệu là thăm dò, gửi vào lớp có ước lượng cao nhất là khai thác (Định nghĩa 01.16).

**Kiểm tra lại.** Với $(\mathrm M,\mathrm C)$, ba kết cục có xác suất $0{,}4$ (vào M), $0{,}6\cdot0{,}8=0{,}48$ (vào C ở đợt 2) và $0{,}6\cdot0{,}2=0{,}12$ (không có lớp), tổng $1$; kỳ vọng $0{,}4\cdot1+0{,}48\cdot0{,}6=0{,}688$. Kết luận dựa trên hai giả thiết của đề: xác suất thành công như nhau ở hai đợt, và kết quả hai đợt độc lập. Định nghĩa 01.12 không đòi hai giả thiết này; nếu lớp C đầy dần sau đợt 1, xác suất của đợt 2 khác $0{,}8$ và phép so sánh phải tính lại với xác suất mới. Cộng $\mathbb E[R_2]$ mà không nhân xác suất đợt 2 diễn ra cho $(\mathrm M,\mathrm C)$ giá trị $0{,}88$, sai. Chọn yêu cầu ở đợt 1 theo $0{,}48>0{,}4$ là so phần thưởng một bước thay cho lợi tức.
:::

### Bài tập 01.16. Tác tử nhiều nhiệm vụ và mô hình thế giới

**Mức độ:** vận dụng, bài tìm hiểu ([Tìm hiểu] theo cách gọi của giáo trình *Học máy thống kê*). Mục tiêu học tập 1 và 4 của ghi chú, cùng phần đọc thêm cuối ghi chú.

**Nguồn:** bài giảng gốc (2025–2026), trang 14–15 và hai câu hỏi thảo luận ở trang 43–44; Sutton và Barto (2018), §8.1, tr. 159–161 và §17.1, tr. 459–460; ghi chú bài giảng Bài 01, Nhận xét 01.4 và 01.15, Định nghĩa 01.11, 01.12 và 01.14, Ví dụ 01.8, Bài tập 01.9, Bài tập 01.12, mục "Đọc thêm: tác tử nhiều nhiệm vụ và mô hình thế giới". Lợi tức $0$ của chương trình P trên N2 ở câu (a) đã có trong ý thứ nhất của Nhận xét 01.4; phần còn lại của (a) và các câu (b)–(d) chỉ có trong tệp này.

::: exercise Bài tập 01.16 [Tìm hiểu] (Tác tử nhiều nhiệm vụ và mô hình thế giới)
Bài giảng gốc (trang 43–44) nêu hai câu hỏi thảo luận. Câu thứ nhất so sánh lập kế hoạch hoặc điều khiển với một môi trường cố định và học từ tương tác, rồi so sánh nhiệm vụ của một robot chuyên dụng, như robot dọn nhà, với nhiệm vụ của một robot đa năng (general-purpose robot), như robot hình người. Câu thứ hai hỏi vì sao cách tiếp cận dùng mô hình thế giới (world model) được xem là hướng có triển vọng cho tính tổng quát và hiệu quả dùng mẫu (sample efficiency), cách tiếp cận đó liên hệ thế nào với lập kế hoạch dưới bất định, và trí tuệ nhân tạo tổng quát (artificial general intelligence) có cần một mô hình thế giới hay không. Trang 15 của bài giảng gốc nêu rằng một tác tử Học tăng cường học cho một nhiệm vụ khó chuyển sang nhiệm vụ khác, chẳng hạn từ cờ vua sang cờ vây; hai nhiệm vụ N1, N2 dưới đây là một phiên bản nhỏ của vấn đề đó.

Xét robot dọn dãy bốn ô với hai nhiệm vụ trên cùng dãy ô. Ở cả hai nhiệm vụ, robot bắt đầu ở ô 1; $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ làm sạch ô đang đứng; cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$ cho ô đang đứng; lượt bị cắt sau $L=5$ hành động. Ở nhiệm vụ N1, chỉ ô 4 có rác; ở nhiệm vụ N2, chỉ ô 2 có rác. Hút ở ô có rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$.

- (a) Chương trình P gồm ba lần $\text{phải}$, sau đó $\text{hút}$ đến hết lượt. Chính sách $\pi_1$ thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$. Tính lợi tức $G_0$ của P và của $\pi_1$ trên N1 và trên N2.
- (b) Chỉ ra phần nào của bài toán giống nhau giữa N1 và N2, phần nào khác. Giá trị $v_{\mathrm P}(h_0)$ của lịch sử ban đầu có dùng lại được từ N1 sang N2 không. Một mô hình gồm luật dịch chuyển đúng và vị trí rác được cập nhật thành ô 2 cho kế hoạch nào trên N2, và kế hoạch đó cần bao nhiêu lượt thử trên robot thật.
- (c) Trên N2, rác thật ở ô 2, nhưng mô hình ghi nhầm rác ở ô 3, như mô hình M2 của Ví dụ 01.8. Xác định kế hoạch mà mô hình này cho và điều xảy ra khi thực hiện kế hoạch đó trên robot thật.
- (d) Viết một bài ngắn, khoảng $600$ đến $900$ từ, trả lời hai câu hỏi thảo luận. Bài dùng ít nhất bốn khái niệm của chương với số hiệu (chẳng hạn Định nghĩa 01.11, 01.12, 01.14, Nhận xét 01.4), dùng kết quả của (a)–(c) làm ví dụ, dẫn ít nhất một nguồn cụ thể ngoài bài giảng gốc, và tách rõ nhận định có cơ sở với quan điểm cá nhân.
:::

::: hint Gợi ý Bài tập 01.16
Ở (b), giá trị được định nghĩa qua lợi tức, mà lợi tức phụ thuộc phần thưởng; luật dịch chuyển không phụ thuộc vị trí rác. Ở (d), đọc Sutton và Barto (2018), §17.1 về dự báo nhiều tín hiệu như một dạng mô hình môi trường, và §8.1 về mô hình và lập kế hoạch.
:::

::: solution Lời giải Bài tập 01.16
**Câu (a).** Trên N1, P đi tới ô 4 sau ba lần $\text{phải}$ rồi hút được rác ở hành động thứ tư: $G_0=1$, $T=4$. Trên N2, P đi qua ô 2 mà không hút, tới ô 4 rồi hút hai lần ở ô 4 sạch: mọi phần thưởng bằng $0$, $G_0=0$, $T=5$. Trên N1, $\pi_1$ cho lượt $\text{phải},\text{phải},\text{phải},\text{hút}$ với $G_0=1$. Trên N2, $\pi_1$ thấy $\text{sạch}$ ở ô 1 nên sang phải, thấy $\text{bẩn}$ ở ô 2 nên hút: $G_0=1$, $T=2$.

**Câu (b).** Hai nhiệm vụ có chung tập hành động, luật dịch chuyển, cảm biến và giới hạn $L$; chúng khác nhau ở vị trí rác, nên khác nhau ở luật phần thưởng và luật kết thúc lượt. Ở N1 và N2, luật dịch chuyển, phần thưởng và kết thúc lượt không ngẫu nhiên, và P là chính sách xác định: P chọn theo $t$, mà $t$ đọc được từ độ dài lịch sử (Định nghĩa 01.11). Theo Bài tập 01.12(a), từ $h_0$ có đúng một diễn biến, nên $v_{\mathrm P}(h_0)$ bằng lợi tức ở câu (a): $1$ trên N1 và $0$ trên N2. Giá trị gắn với phần thưởng của nhiệm vụ (Định nghĩa 01.12), nên không dùng lại được khi phần thưởng đổi. Mô hình có luật dịch chuyển đúng và vị trí rác mới dự báo rằng dãy ngắn nhất cho tổng phần thưởng $1$ trên N2 là $\text{phải},\text{hút}$; thử các dãy trong mô hình là lập kế hoạch (Định nghĩa 01.14) và không cần lượt thử nào trên robot thật. Phần luật dịch chuyển của mô hình học được ở N1 dùng lại nguyên vẹn ở N2. Chính sách $\pi_1$ cũng đạt $G_0=1$ trên cả hai nhiệm vụ, vì nó phản ứng với quan sát thay cho thi hành một dãy định sẵn (Nhận xét 01.4, ý thứ nhất: môi trường đổi).

**Câu (c).** Trong mô hình ghi rác ở ô 3, dãy ngắn nhất có tổng dự báo $1$ là $\text{phải},\text{phải},\text{hút}$. Trên N2, robot đi qua ô 2 có rác, hút ở ô 3 sạch và nhận phần thưởng $0$; lượt chưa kết thúc. Kế hoạch tốt trên mô hình sai không tốt trên môi trường thật (Nhận xét 01.15).

**Câu (d).** Dàn ý tham khảo, mỗi ý kèm căn cứ:

1. **Điều khiển với mô hình cố định và học từ tương tác.** Ba vấn đề của Nhận xét 01.4: môi trường đổi, như P cho $G_0=0$ khi rác chuyển sang ô 2; không gian tìm kiếm lớn, $3^L$ dãy hành động; lập kế hoạch dưới bất định, khi kế hoạch vòng hở (open-loop plan) không phản ứng được với kết quả thực.
2. **Robot chuyên dụng và robot đa năng.** Robot chuyên dụng giải một nhiệm vụ với một phần thưởng. Robot đa năng gặp nhiều nhiệm vụ trên cùng luật của môi trường, như N1 và N2: chính sách và giá trị gắn với phần thưởng của từng nhiệm vụ (câu b), còn phần luật dịch chuyển của mô hình dùng chung được.
3. **Lý do mô hình thế giới được kỳ vọng.** Sutton và Barto (2018, §8.1) định nghĩa lập kế hoạch là quá trình lấy mô hình làm đầu vào và tạo ra hoặc cải thiện chính sách, và mô hình dùng được để mô phỏng kinh nghiệm. Theo §17.1, khả năng dự báo và điều khiển nhiều tín hiệu có thể tạo thành một dạng mô hình môi trường mạnh, và một mô hình tốt giúp tác tử nhận phần thưởng hiệu quả hơn. Câu (b) cho một trường hợp nhỏ: nhiệm vụ mới được giải bằng lập kế hoạch mà không cần lượt thử thật nào.
4. **Liên hệ với lập kế hoạch dưới bất định.** Khi luật của môi trường ngẫu nhiên, mô hình phải cho một phân phối trên các phản hồi (Định nghĩa 01.14), và kết quả của lập kế hoạch là một chính sách phản hồi theo kết quả thực (Nhận xét 01.4, ý thứ ba).
5. **Giới hạn.** Mô hình có thể sai (câu c); khi lập kế hoạch qua nhiều bước, sai số dự báo của bước trước làm sai đầu vào của bước sau (ghi chú, Mục 4.3, đoạn "Trong thực hành"); và việc học một mô hình đủ đúng tự nó cần dữ liệu. Các phương pháp phi mô hình của Bài 05 và Bài 06 học chính sách hoặc giá trị mà không cần mô hình. AlphaGo (Bài tập 01.9 của ghi chú) lập kế hoạch bằng luật cờ vây đã biết, không bằng một mô hình thế giới học được.
6. **Câu hỏi về trí tuệ nhân tạo tổng quát.** Các định nghĩa và kết quả của Bài 01 không đủ để trả lời câu hỏi này; bài giảng gốc nêu đây là một quan điểm, và ghi chú không kiểm chứng nó. Một bài đạt yêu cầu trình bày lập trường như một quan điểm có điều kiện, chẳng hạn "nếu một tác tử phải giải nhiều nhiệm vụ trên cùng luật của môi trường và lượt thử thật đắt, thì một mô hình dùng chung có lợi", và nêu điều kiện làm lập trường đó sai, chẳng hạn khi mô hình học được sai ở chính các trạng thái mà kế hoạch đi qua.

**Kiểm tra lại.** Ở câu (a), $T=2$ của $\pi_1$ trên N2 thỏa $T\le L=5$; P trên N2 dùng đủ năm hành động. Mang $v_{\mathrm P}(h_0)=1$ từ N1 sang N2 như một đặc tính của robot là sai, vì giá trị phụ thuộc phần thưởng và chính sách. Ở câu (d), nhận định về một hệ thống cụ thể cần nguồn; câu hỏi thứ hai là câu hỏi mở, và bài viết tách điều suy ra từ định nghĩa của chương với quan điểm.
:::

## Tài liệu tham khảo

- Bài giảng gốc (2025–2026), *Reinforcement Learning and Planning*, bài 1, Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội: trang 8 và 25 cho Bài tập 01.15; trang 14–15 và 43–44 cho Bài tập 01.16; trang 20 cho Bài tập 01.2(d); trang 24–25 cho Bài tập 01.14; trang 28–30 cho Bài tập 01.7 và 01.8.
- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §3.2 (tr. 53–54) cho Bài tập 01.14; §3.3 (tr. 54–57) cho Bài tập 01.3, 01.4 và 01.13(b); §8.1 (tr. 159–161) và §17.1 (tr. 459–460) cho Bài tập 01.16.
- Ghi chú bài giảng Bài 01 cho phát biểu và chứng minh của mọi kết quả được dùng: Định nghĩa 01.2, 01.5, 01.8, 01.11, 01.12, 01.14, 01.16, 01.18, 01.21; Mệnh đề 01.9 và 01.20; Nhận xét 01.3, 01.4, 01.6, 01.10, 01.15; Ví dụ 01.4, 01.5, 01.8, 01.9, 01.10; Tình huống 01.1, 01.2; Bài tập 01.9 (dẫn trong lời giải Bài tập 01.16).
