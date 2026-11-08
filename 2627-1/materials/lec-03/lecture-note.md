# Bài 03 — Quá trình quyết định Markov

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Kiểm tra một biểu diễn trạng thái có tính Markov hay không, lập bộ quá trình quyết định Markov (Markov decision process, MDP) hữu hạn và bảng hàm động lực $p(s',r\mid s,a)$ từ một mô tả bằng lời, kiểm tra điều kiện chuẩn hóa và suy ra $p(s'\mid s,a)$, $r(s,a)$ (Bài tập 03.1, 03.2, 03.15, 03.22, 03.24).
2. Phân loại nhiệm vụ có kết thúc (episodic task) và nhiệm vụ tiếp diễn (continuing task), tính lợi tức (return) chiết khấu của một dãy phần thưởng và dùng cận $\lvert G_t\rvert\le M/(1-\gamma)$, tính lùi lợi tức theo $G_t=R_{t+1}+\gamma G_{t+1}$ (Bài tập 03.3, 03.10, 03.12, 03.18, 03.20, 03.23).
3. Phân biệt mô hình (model), chính sách (policy), giá trị trạng thái (state value) và giá trị hành động (action value); tính kỳ vọng của lợi tức cắt sau hai bước trên cây quỹ đạo (Bài tập 03.4, 03.5, 03.16, 03.17).
4. Chứng minh phương trình Bellman kỳ vọng (Bellman expectation equation) cho $v_\pi$ và $q_\pi$, chỉ ra bước dùng tính Markov và bước dùng tính dừng (Bài tập 03.6, 03.7, 03.11, 03.17, 03.19, 03.24, 03.25).
5. Lập, giải và kiểm tra hệ $(I-\gamma P_\pi)v=r_\pi$ của một chính sách cho trước (đánh giá chính sách, policy evaluation), nêu điều kiện để hệ có nghiệm duy nhất và đọc các giá trị $q_\pi$ thu được (Bài tập 03.8, 03.9, 03.13, 03.14, 03.20, 03.21, 03.23–03.25).

Bài tập 03.1–03.14 nằm trong ghi chú; [tệp bài tập](material-viewer.html?doc=materials/lec-03/exercises.md&deck=lecture-03-qua-trinh-quyet-dinh-markov.html) chứa lại Bài tập 03.1–03.8 và thêm Bài tập 03.15–03.25.

<!-- note-topic-id: lec-03-part-09 -->
## Kiến thức tiên quyết

Số hiệu `02.k` chỉ ghi chú Bài 02, `03.k` chỉ ghi chú này.

- **Vòng tương tác, mẫu chuyển, lịch sử** (Định nghĩa 02.1, 02.3). Ở mỗi thời điểm rời rạc $t$, tác tử (agent) ở trạng thái (state) $S_t$ chọn hành động (action) $A_t$; một bước sau, môi trường (environment) trả phần thưởng (reward) $R_{t+1}$ là số thực và trạng thái mới $S_{t+1}$. Lịch sử $H_t=(S_0,A_0,R_1,\dots,S_t)$ ghi quá khứ tới $t$.
- **Tính Markov** (Định nghĩa 02.5). Trạng thái có tính Markov khi, với mọi chính sách, phân phối của $(S_{t+1},R_{t+1})$ khi biết $(H_t,A_t)$ chỉ phụ thuộc $(S_t,A_t)$.
- **Chính sách** (Định nghĩa 02.8, với biểu diễn là trạng thái). Chính sách ngẫu nhiên (stochastic policy) gán cho mỗi trạng thái $s$ một phân phối $\pi(\cdot\mid s)$ trên các hành động hợp lệ; chính sách xác định (deterministic policy) dồn xác suất $1$ vào một hành động.
- **Lợi tức** (Định nghĩa 02.12, Mệnh đề 02.13). Với hệ số chiết khấu (discount factor) $\gamma\in[0,1]$, lợi tức $G_t=\sum_{k\ge0}\gamma^kR_{t+k+1}$ thỏa $G_t=R_{t+1}+\gamma G_{t+1}$; khi $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$ với mọi $t$, $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$.
- **Giá trị, hàm động lực, dự đoán và điều khiển** (Định nghĩa 02.14, 02.16, Nhận xét 02.17). Giá trị trạng thái là $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$; hàm động lực $p(s',r\mid s,a)$ là xác suất môi trường trả $(s',r)$ sau khi tác tử chọn $a$ tại $s$; dự đoán (prediction) đánh giá một chính sách cố định, điều khiển (control) tìm chính sách tốt hơn.
- **Xác suất có điều kiện và quy tắc nhân** (chain rule). Với các biến ngẫu nhiên rời rạc và sự kiện $B$ có xác suất dương, $\Pr(X=x,Y=y\mid B)=\Pr(X=x\mid B)\Pr(Y=y\mid X=x,B)$ khi $\Pr(X=x,B)>0$. Áp dụng lặp lại, xác suất của một dãy biến bằng tích các xác suất có điều kiện của từng biến khi biết các biến trước nó.
- **Kỳ vọng toàn phần** (law of total expectation). Nếu $Y$ nhận hữu hạn giá trị và $X$ khả tích, thì $\mathbb E[X\mid B]=\sum_y \Pr(Y=y\mid B)\,\mathbb E[X\mid Y=y,B]$, tổng lấy trên các $y$ có $\Pr(Y=y,B)>0$. Kỳ vọng có điều kiện tuyến tính, và hằng số đi ra ngoài kỳ vọng.
- **Hệ phương trình tuyến tính.** Ma trận vuông $A$ khả nghịch khi và chỉ khi $Ax=0$ chỉ có nghiệm $x=0$; khi đó $Ax=b$ có nghiệm duy nhất $x=A^{-1}b$. Phép khử Gauss (Gaussian elimination) giải hệ $n$ ẩn với số phép tính cỡ $n^3$.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$, $k$ | thời điểm quyết định; chỉ số thời gian chạy trong các tổng | $\{0,1,2,\dots\}$ |
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái chưa kết thúc; tập đó thêm trạng thái kết thúc | hữu hạn, $\lvert\mathcal S\rvert=n$ |
| $\mathcal A(s)$ | tập hành động hợp lệ tại $s$ | hữu hạn, khác rỗng |
| $\mathcal R$ | tập các giá trị phần thưởng | tập con hữu hạn của $\mathbb R$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động, phần thưởng (biến ngẫu nhiên) | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathcal R$ |
| $s$, $a$, $s'$, $r$ | giá trị cụ thể của $S_t$, $A_t$, $S_{t+1}$, $R_{t+1}$ | như trên |
| $H_t$, $h_t$ | lịch sử tới thời điểm $t$ (biến ngẫu nhiên; giá trị cụ thể) | dãy hữu hạn $(S_0,A_0,R_1,\dots,S_t)$ |
| $p(s',r\mid s,a)$ | hàm động lực | $[0,1]$ |
| $p(s'\mid s,a)$, $r(s,a)$ | xác suất chuyển trạng thái; thưởng kỳ vọng một bước | $[0,1]$; $\mathbb R$ |
| $\mathcal M$ | quá trình quyết định Markov hữu hạn $(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p)$ | bộ bốn |
| $T$ | thời điểm kết thúc lượt | $\{1,2,\dots\}\cup\{\infty\}$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $[0,1)$ với nhiệm vụ tiếp diễn |
| $G_t$ | lợi tức từ thời điểm $t$ | biến ngẫu nhiên thực |
| $G_t^{[K]}$ | lợi tức cắt sau $K$ bước, $\sum_{j=0}^{K-1}\gamma^jR_{t+j+1}$ | biến ngẫu nhiên thực |
| $M$ | cận của trị tuyệt đối phần thưởng | $M\ge0$ |
| $\pi(a\mid s)$ | chính sách Markov dừng | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $\mu$ | phân phối đầu, tức phân phối của $S_0$ | phân phối trên $\mathcal S$ |
| $\Pr_\pi$, $\mathbb E_\pi$ | xác suất, kỳ vọng khi hành động theo $\pi$ và phản hồi theo $p$ | — |
| $v_\pi(s)$ | giá trị trạng thái của $\pi$ | $\mathbb R$; bằng $0$ tại trạng thái kết thúc |
| $q_\pi(s,a)$ | giá trị hành động của $\pi$ | $\mathbb R$ |
| $P_\pi$, $r_\pi$ | ma trận chuyển và véc-tơ thưởng kỳ vọng dưới $\pi$ | $\mathbb R^{n\times n}$; $\mathbb R^n$ |
| $v$ | véc-tơ giá trị xếp theo thứ tự trạng thái | $\mathbb R^n$ |
| $I$, $\lVert x\rVert_\infty$ | ma trận đơn vị; chuẩn cực đại $\max_i\lvert x_i\rvert$ | $\mathbb R^{n\times n}$; $\ge0$ |
| $\mathrm H$, $\mathrm L$ | trạng thái pin cao, pin thấp của robot | nhãn, không phải biến |
| $\mathrm{tim}$, $\mathrm{cho}$, $\mathrm{sac}$ | hành động Tìm, Chờ, Sạc của robot | nhãn, không phải biến |

Chữ hoa ($S_t$, $A_t$, $R_{t+1}$, $G_t$) là biến ngẫu nhiên; chữ thường là giá trị cụ thể. Lịch sử $H_t$ viết nghiêng, khác nhãn trạng thái $\mathrm H$ viết đứng. Phần thưởng mang chỉ số $t+1$ vì nó đến sau hành động $A_t$, cùng với trạng thái $S_{t+1}$; quy ước này theo Sutton và Barto (2018, tr. 48).

Giáo trình *Học máy thống kê* viết quá trình quyết định Markov thành bộ $\langle S,A,T,R,\gamma\rangle$, với các tương ứng sau:

- $T(s,a,s')$ ứng với $p(s'\mid s,a)$; chữ $T$ của chương chỉ thời điểm kết thúc.
- $R(s,a,s')$ là thưởng kỳ vọng khi biết cả $s'$, nên $r(s,a)=\sum_{s'}p(s'\mid s,a)R(s,a,s')$.
- $V^\pi$, $Q^\pi$ ứng với $v_\pi$, $q_\pi$.
- Giá trị quỹ đạo $U(\tau)$ ứng với $G_0$.

Ghi chú Bài 02 và Bài 04 viết $R_{\max}$ cho cận $M$ của chương này. Dấu thập phân là dấu phẩy. Các xác suất và mức thưởng của robot và của các biến thể của nó là số liệu sư phạm tự xây dựng.

## 1. Trạng thái Markov và mô hình môi trường

Trong Bài 02, chúng ta đã định nghĩa giá trị của trạng thái $s$ dưới một chính sách cố định $\pi$ là kỳ vọng của lợi tức khi xuất phát tại $s$, $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$ (Định nghĩa 02.14). Định nghĩa này nói giá trị là gì nhưng chưa cho cách tính. Tính theo định nghĩa nghĩa là liệt kê mọi quỹ đạo (trajectory), nhân lợi tức của mỗi quỹ đạo với xác suất của nó rồi cộng lại; với nhiệm vụ không bao giờ kết thúc, số quỹ đạo là vô hạn và mỗi quỹ đạo dài vô hạn.

Bài toán cụ thể của chương là robot thu gom lon hai mức pin. Ở pin thấp, Chờ cho ngay $1$, còn Sạc cho $0$ nhưng đưa robot về pin cao, nơi Tìm luôn cho $2$. Muốn so sánh hai lựa chọn, chúng ta cần một con số tổng hợp toàn bộ tương lai của mỗi cách hành động.

Chúng ta dùng hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ (Mệnh đề 02.13(a)) và tính Markov để viết giá trị thành nghiệm của một hệ phương trình tuyến tính, rồi giải hệ cho robot dưới một chính sách cụ thể, được $v_\pi(\mathrm H)=13/4$ ở pin cao và $v_\pi(\mathrm L)=7/4$ ở pin thấp. Hình dưới cho chuỗi bước dẫn tới hai giá trị này.

![Sáu khối nối bằng mũi tên. Hàng trên: Mục 1, mô hình với trạng thái Markov và hàm động lực p(s', r | s, a); mũi tên "chuỗi thưởng" sang Mục 2, lợi tức G_t = R_{t+1} + γR_{t+2} + … với cận |G_t| ≤ M/(1 − γ); mũi tên "lấy kỳ vọng" sang Mục 3, chính sách π(a | s), giá trị v_π(s) và q_π(s, a). Mũi tên "tách bước đầu, dùng tính Markov" xuống hàng dưới: Mục 4, phương trình Bellman v_π(s) = Σ π Σ p [r + γ v_π(s')], mỗi trạng thái một phương trình; mũi tên "S hữu hạn, γ < 1" sang Mục 5, hệ (I − γP_π) v = r_π có nghiệm duy nhất khi γ < 1; mũi tên "giải hệ hai ẩn" sang khối viền đứt "Robot hai mức pin" với v_π(H) = 13/4, v_π(L) = 7/4.](img/lec-03/chapter-structure.svg)

Hàm động lực $p(s',r\mid s,a)$, cùng cách chọn hành động, sinh chuỗi phần thưởng; chuỗi đó gộp thành lợi tức $G_t$, và kỳ vọng của $G_t$ dưới chính sách $\pi$ cho $v_\pi$, $q_\pi$. Nhãn trên mỗi mũi tên ghi thao tác hoặc giả thiết cho phép đi sang khối sau. Hai giả thiết quyết định nằm ở hàng dưới: sau khi tách bước đầu, tính Markov cho phép thay kỳ vọng của phần còn lại bằng giá trị của trạng thái kế tiếp, nên mỗi trạng thái cho một phương trình (Định lý 03.21); tập trạng thái hữu hạn cùng $\gamma<1$ làm hệ có nghiệm duy nhất (Định lý 03.28).

<!-- note-topic-id: lec-03-part-01 -->
### 1.1 Robot thu gom lon và một bước tương tác

Để có thể tính, mô tả bằng lời của robot phải trở thành dữ liệu: ở mỗi bước, robot đang ở mức pin nào, chọn gì, nhận bao nhiêu và chuyển sang đâu.

::: example Ví dụ 03.1 (Robot thu gom lon hai mức pin)
**Môi trường.** Một robot thu gom lon rỗng trong văn phòng. Tác tử điều khiển robot chỉ phân biệt hai mức pin: pin cao $\mathrm H$ và pin thấp $\mathrm L$.

**Hành động.** Ở pin cao, robot chọn Tìm ($\mathrm{tim}$) hoặc Chờ ($\mathrm{cho}$). Ở pin thấp, robot chọn Tìm, Chờ hoặc Sạc ($\mathrm{sac}$).

**Phản hồi.**

- Tìm từ $\mathrm H$: phần thưởng $2$; pin giữ ở $\mathrm H$ với xác suất $1/2$, xuống $\mathrm L$ với xác suất $1/2$.
- Chờ từ $\mathrm H$: phần thưởng $1$; pin giữ ở $\mathrm H$.
- Tìm từ $\mathrm L$: với xác suất $1/2$ pin còn đủ, robot nhận $2$ và vẫn ở $\mathrm L$; với xác suất $1/2$ pin cạn, robot được cứu hộ, nhận $-3$ và được sạc lại về $\mathrm H$ ngay trong bước đó.
- Chờ từ $\mathrm L$: phần thưởng $1$; pin giữ ở $\mathrm L$.
- Sạc từ $\mathrm L$: phần thưởng $0$; pin về $\mathrm H$.

**Nhiệm vụ.** Robot hoạt động liên tục; cứu hộ và sạc đều không dừng công việc.

**Nguồn.** Khung ví dụ là ví dụ 3.3 của Sutton và Barto (2018, tr. 52–53), với hai tham số xác suất của ví dụ gốc đều bằng $1/2$; ví dụ gốc chỉ cho thưởng kỳ vọng trên mỗi nhánh, nên ở đây phần thưởng cố định trên mỗi nhánh để xác định được $p$.
:::

![Robot thu gom lon ở mức pin thấp với ba lựa chọn: Tìm, Chờ, Sạc.](img/lec-03/robot-p01-recycling-robot-low.svg)

Ở pin thấp, ba lựa chọn khác nhau ở phần thưởng nhận ngay ($2$ hoặc $-3$ với Tìm, $1$ với Chờ, $0$ với Sạc) và ở mức pin của bước sau.

Mỗi bước của robot cho một mẫu chuyển (transition) gồm bốn thành phần: trạng thái, hành động, phần thưởng và trạng thái mới. Đó là mẫu chuyển của Định nghĩa 02.1 với quan sát là trạng thái.

::: example Ví dụ 03.2 (Một bước của robot)
**Dữ kiện.** Tại thời điểm $t$, robot ở pin cao, chọn Tìm, nhận phần thưởng $2$ và pin xuống thấp (Ví dụ 03.1 cho phép phản hồi này với xác suất $1/2$).

**Mẫu chuyển.**

$$
(S_t,\,A_t,\,R_{t+1},\,S_{t+1})=(\mathrm H,\ \mathrm{tim},\ 2,\ \mathrm L).
$$

**Đọc chỉ số.** Trạng thái và hành động mang chỉ số $t$ vì chúng có trước khi robot hành động. Phần thưởng và trạng thái mới mang chỉ số $t+1$ vì môi trường trả về chúng cùng lúc, sau hành động.

**Kiểm tra lại.** Nếu bước kế tiếp robot ở $\mathrm L$ chọn Chờ, mẫu chuyển tiếp theo là $(S_{t+1},A_{t+1},R_{t+2},S_{t+2})=(\mathrm L,\mathrm{cho},1,\mathrm L)$; hai mẫu chuyển nối nhau ở $S_{t+1}=\mathrm L$.
:::

Nối các mẫu chuyển lại, ta được khái niệm sau.

::: definition Định nghĩa 03.1 (Quỹ đạo và lịch sử)
Xét tác tử và môi trường tương tác tại các thời điểm rời rạc $t=0,1,2,\dots$. Tập trạng thái $\mathcal S^+$ gồm tập $\mathcal S$ các trạng thái chưa kết thúc và, với nhiệm vụ có kết thúc, các trạng thái kết thúc, nơi tương tác của một lượt dừng lại (Định nghĩa 03.8). Tại thời điểm $t$, trạng thái là biến ngẫu nhiên $S_t$ nhận giá trị trong $\mathcal S^+$, hành động là biến ngẫu nhiên $A_t$ nhận giá trị trong tập hành động hợp lệ $\mathcal A(S_t)$, và phần thưởng của chuyển từ $t$ sang $t+1$ là biến ngẫu nhiên $R_{t+1}$ nhận giá trị trong tập hữu hạn $\mathcal R\subset\mathbb R$.

Quỹ đạo (trajectory) là dãy

$$
S_0,\ A_0,\ R_1,\ S_1,\ A_1,\ R_2,\ S_2,\ A_2,\ R_3,\ \dots
\tag{1.1}
$$

Lịch sử (history) tới thời điểm $t$ là đoạn đầu của quỹ đạo kết thúc ở trạng thái hiện tại:

$$
H_t=(S_0,A_0,R_1,S_1,\dots,A_{t-1},R_t,S_t).
$$
:::

Lịch sử $H_t$ dừng ở $S_t$ và chưa chứa $A_t$, vì đó là thông tin có trước khi tác tử chọn hành động tại $t$. Trong Ví dụ 03.2, nếu robot bắt đầu ở $t=0$ thì $H_1=(\mathrm H,\mathrm{tim},2,\mathrm L)$.

Định nghĩa 03.1 dùng lại lịch sử trạng thái của Định nghĩa 02.3 và thêm hai điều: tập hành động có thể phụ thuộc trạng thái, và tập phần thưởng hữu hạn. Định nghĩa 02.3 chỉ gọi dãy của một lượt kết thúc tại $T<\infty$ là quỹ đạo; dãy (1.1) cho phép cả quỹ đạo vô hạn của nhiệm vụ tiếp diễn như robot.

### 1.2 Tính Markov

Tại pin thấp, robot chuẩn bị Tìm. Để dự báo phản hồi, chúng ta muốn chỉ dùng mức pin hiện tại, không cần biết robot đã đến pin thấp bằng cách nào. Nếu cách đến pin thấp có ảnh hưởng, mọi bảng xác suất phải đánh chỉ số theo cả lịch sử, và số lịch sử tăng theo cấp số nhân với $t$.

Một cách trực quan, trạng thái là bản tóm tắt của quá khứ. Bản tóm tắt tốt giữ lại mọi chi tiết của quá khứ có ảnh hưởng tới phản hồi sắp tới và bỏ đi phần còn lại (Sutton và Barto, 2018, tr. 49). Để làm rõ ý này, xem ví dụ sau về hai lịch sử có cùng trạng thái hiện tại.

::: example Ví dụ 03.3 (Hai lịch sử, cùng trạng thái hiện tại)
**Dữ kiện.** Robot của Ví dụ 03.1. Robot thứ nhất có lịch sử $(\mathrm H,\mathrm{tim},2,\mathrm L)$: vừa Tìm từ pin cao và xuống pin thấp. Robot thứ hai có lịch sử $(\mathrm L,\mathrm{cho},1,\mathrm L)$: vừa Chờ ở pin thấp. Cả hai đang ở $\mathrm L$ và chọn Tìm.

**Phản hồi.** Theo Ví dụ 03.1, phản hồi của Tìm từ $\mathrm L$ chỉ phụ thuộc mức pin: với cả hai robot, $(S_{t+1},R_{t+1})=(\mathrm L,2)$ với xác suất $1/2$ và $(\mathrm H,-3)$ với xác suất $1/2$.

**Kết luận.** Hai lịch sử khác nhau cho cùng một phân phối phản hồi; mức pin là trạng thái đủ thông tin trong mô hình này.

**Kiểm tra lại.** Ở cả hai lịch sử, hai xác suất cộng lại bằng $1$.
:::

::: definition Định nghĩa 03.2 (Tính Markov)
Trạng thái $S_t$ có tính Markov (Markov property) nếu với mọi cách chọn hành động của tác tử chỉ dựa trên lịch sử (có thể ngẫu nhiên), với các xác suất tính theo cách chọn đó, mọi $t\ge0$, mọi lịch sử $h_t$ kết thúc ở trạng thái $s$, mọi hành động $a\in\mathcal A(s)$ sao cho $\Pr(H_t=h_t,A_t=a)>0$, và mọi $s'\in\mathcal S^+$, $r\in\mathcal R$,

$$
\begin{aligned}
&\Pr(S_{t+1}=s',R_{t+1}=r\mid H_t=h_t,A_t=a)\\
&\quad=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a).
\end{aligned}
\tag{1.2}
$$
:::

Vế trái của (1.2) dùng toàn bộ lịch sử, vế phải chỉ dùng trạng thái cuối và hành động hiện tại; đẳng thức phải đúng với mọi lịch sử có xác suất dương. Ví dụ 03.3 là một trường hợp của (1.2): hai lịch sử kết thúc ở $\mathrm L$ với hành động Tìm cho cùng một phân phối phản hồi. Định nghĩa 03.2 là Định nghĩa 02.5 của ghi chú Bài 02 viết cho các tập hữu hạn.

Phản ví dụ sau cho thấy một robot có thể mất tính Markov khi trạng thái bỏ sót thông tin.

::: example Ví dụ 03.4 (Trạng thái thiếu phòng làm việc)
**Dữ kiện.** Robot luôn ở pin thấp và chỉ Chờ. Robot làm việc luân phiên ở hai phòng: nếu bước này ở phòng 1 thì bước sau ở phòng 2, và ngược lại. Chờ ở phòng 1 cho phần thưởng $1$, Chờ ở phòng 2 cho $0$. Phòng lúc $t=0$ được chọn ngẫu nhiên, mỗi phòng xác suất $1/2$. Trạng thái chỉ ghi mức pin, nên luôn bằng $\mathrm L$.

**Hai lịch sử.** Xét $t=1$ và hai lịch sử $h=(\mathrm L,\mathrm{cho},1,\mathrm L)$, $h'=(\mathrm L,\mathrm{cho},0,\mathrm L)$.

- Với $h$, phần thưởng $R_1=1$ cho biết lúc $t=0$ robot ở phòng 1, nên lúc $t=1$ robot ở phòng 2 và $\Pr(R_2=1\mid H_1=h,A_1=\mathrm{cho})=0$.
- Với $h'$, phần thưởng $R_1=0$ cho biết lúc $t=0$ robot ở phòng 2, nên $\Pr(R_2=1\mid H_1=h',A_1=\mathrm{cho})=1$.

**Kết luận.** Hai lịch sử kết thúc ở cùng trạng thái $\mathrm L$ nhưng cho hai xác suất $0$ và $1$. Vế phải của (1.2) là một số duy nhất $\Pr(R_2=1\mid S_1=\mathrm L,A_1=\mathrm{cho})$, nên không thể bằng cả hai; trạng thái "mức pin" không có tính Markov.

**Sửa.** Lấy trạng thái là cặp (mức pin, phòng). Phòng hiện tại quyết định phần thưởng và phòng kế tiếp, nên lịch sử không cho thêm thông tin và (1.2) thỏa.

**Kiểm tra lại.** Mỗi lịch sử có xác suất $1/2$, nên cả hai thuộc phạm vi của Định nghĩa 03.2.
:::

::: remark Nhận xét 03.3 (Trạng thái đủ thông tin và các cách hiểu sai)
- Tính Markov thuộc về biểu diễn trạng thái (state representation). Cùng một hệ vật lý có thể có biểu diễn Markov và biểu diễn không Markov, như mức pin so với cặp (mức pin, phòng) ở Ví dụ 03.4.
- Khi một biểu diễn không Markov, có hai cách sửa: thêm vào trạng thái phần thông tin bị thiếu, như phòng ở Ví dụ 03.4; hoặc dùng làm trạng thái một tóm tắt của lịch sử đủ để dự báo bước tới; ở Ví dụ 03.4, phần thưởng gần nhất đã cho biết phòng hiện tại khi $t\ge1$. Cách thứ hai làm số trạng thái tăng theo số tổ hợp lịch sử phải phân biệt.
- Tính Markov chỉ nói phân phối phản hồi phụ thuộc $(s,a)$; các con số của phân phối đó phải cho riêng cho từng cặp $(s,a)$, như các xác suất $1/2$ và $1$ của Ví dụ 03.1.
- Tính Markov không nói phản hồi là tất định: Tìm từ $\mathrm L$ vẫn có hai kết quả ngẫu nhiên.
:::

::: exercise Bài tập 03.1
**Dữ kiện.** (a) Robot của Ví dụ 03.1 ghi được mẫu chuyển $(\mathrm L,\mathrm{cho},1,\mathrm L)$ ở bước bắt đầu tại thời điểm $t=4$. (b) Một robot chỉ hoạt động ở pin cao, pin luôn giữ ở $\mathrm H$, và ở mọi bước tác tử chọn Tìm hoặc Chờ, mỗi hành động xác suất $1/2$. Robot được đặt cố định suốt đời ở một trong hai vị trí, mỗi vị trí xác suất $1/2$, và trạng thái không ghi vị trí. Ở vị trí gần cửa, Tìm luôn cho phần thưởng $2$. Ở vị trí xa cửa, Tìm cho $2$ hoặc $0$, mỗi kết quả xác suất $1/2$. Chờ ở cả hai vị trí cho $1$.

**Yêu cầu.** (a) Viết mẫu chuyển bằng các biến ngẫu nhiên có chỉ số thời gian. (b) Xét hai lịch sử $h=(\mathrm H,\mathrm{tim},0,\mathrm H)$ và $h'=(\mathrm H,\mathrm{cho},1,\mathrm H)$ tại $t=1$. Tính $\Pr(R_2=0\mid H_1=h,A_1=\mathrm{tim})$ và $\Pr(R_2=0\mid H_1=h',A_1=\mathrm{tim})$, rồi kết luận trạng thái "mức pin" có tính Markov hay không.
:::

::: hint
Ở câu (b), phần thưởng $0$ chỉ xảy ra ở vị trí xa cửa. Tính xác suất robot ở vị trí xa cửa khi biết từng lịch sử, rồi nhân với xác suất Tìm cho $0$ ở vị trí đó.
:::

::: solution
**(a)** Bước bắt đầu tại $t=4$ nên $S_4=\mathrm L$, $A_4=\mathrm{cho}$, $R_5=1$, $S_5=\mathrm L$. Phần thưởng mang chỉ số $5$ vì nó đến sau hành động $A_4$.

**(b)** Với $h$, phần thưởng $R_1=0$ sau Tìm chỉ có thể xảy ra ở vị trí xa cửa, nên robot chắc chắn ở vị trí xa cửa và

$$
\Pr(R_2=0\mid H_1=h,A_1=\mathrm{tim})=\tfrac12 .
$$

Với $h'$, Chờ cho $1$ ở cả hai vị trí, nên lịch sử không cho thông tin về vị trí; xác suất ở vị trí xa cửa vẫn là $1/2$. Theo công thức xác suất toàn phần theo vị trí,

$$
\begin{aligned}
\Pr(R_2=0\mid H_1=h',A_1=\mathrm{tim})&=\tfrac12\cdot\tfrac12+\tfrac12\cdot0\\
&=\tfrac14 .
\end{aligned}
$$

Hai lịch sử kết thúc ở cùng trạng thái $\mathrm H$ với cùng hành động Tìm nhưng cho hai xác suất $1/2$ và $1/4$, nên (1.2) không thể thỏa với cả hai; trạng thái "mức pin" không có tính Markov. Thêm vị trí vào trạng thái khôi phục tính Markov.

**Kiểm tra lại.** Theo chính sách trong Dữ kiện, $h$ có xác suất $\tfrac12\cdot\tfrac12\cdot\tfrac12=\tfrac18$ (chọn Tìm, ở vị trí xa cửa, nhận $0$) và $h'$ có xác suất $\tfrac12$ (chọn Chờ); cả hai dương.
:::

<!-- note-topic-id: lec-03-part-02 -->
### 1.3 Hàm động lực

Một mẫu chuyển như Ví dụ 03.2 không cho biết phản hồi đó xảy ra thường xuyên đến mức nào, cũng không cho biết những phản hồi nào khác có thể xảy ra. Để dự báo, chúng ta cần liệt kê mọi phản hồi của mỗi cặp trạng thái–hành động cùng xác suất của chúng. Nhờ tính Markov, bảng liệt kê chỉ cần đánh chỉ số theo cặp $(s,a)$.

::: example Ví dụ 03.5 (Bảng phản hồi của robot)
**Dữ kiện.** Robot của Ví dụ 03.1.

**Lập bảng.** Mỗi hàng là một phản hồi có xác suất dương của một cặp trạng thái–hành động hợp lệ. Phần thưởng cố định trên mỗi nhánh.

| Hiện tại $s$ | Hành động $a$ | Kế tiếp $s'$ | Phần thưởng $r$ | Xác suất |
|---|---|---|---:|---:|
| $\mathrm H$ | $\mathrm{tim}$ | $\mathrm H$ | $2$ | $1/2$ |
| $\mathrm H$ | $\mathrm{tim}$ | $\mathrm L$ | $2$ | $1/2$ |
| $\mathrm H$ | $\mathrm{cho}$ | $\mathrm H$ | $1$ | $1$ |
| $\mathrm L$ | $\mathrm{tim}$ | $\mathrm L$ | $2$ | $1/2$ |
| $\mathrm L$ | $\mathrm{tim}$ | $\mathrm H$ | $-3$ | $1/2$ |
| $\mathrm L$ | $\mathrm{cho}$ | $\mathrm L$ | $1$ | $1$ |
| $\mathrm L$ | $\mathrm{sac}$ | $\mathrm H$ | $0$ | $1$ |

**Kiểm tra chuẩn hóa.** Năm cặp hợp lệ tạo năm nhóm hàng. Nhóm $(\mathrm H,\mathrm{tim})$ và nhóm $(\mathrm L,\mathrm{tim})$ có hai hàng, mỗi hàng $1/2$, tổng $1$; ba nhóm còn lại có một hàng xác suất $1$.

**Kiểm tra lại.** Không có hàng nào cho cặp $(\mathrm H,\mathrm{sac})$, vì Sạc không thuộc $\mathcal A(\mathrm H)$. Mỗi hàng ghi một cặp (trạng thái kế tiếp, phần thưởng): ở nhóm $(\mathrm L,\mathrm{tim})$, biết phần thưởng là $-3$ thì biết trạng thái kế tiếp là $\mathrm H$.
:::

Một cách trực quan, bảng phản hồi là một họ phân phối xác suất, mỗi cặp $(s,a)$ một phân phối trên các cặp $(s',r)$.

::: definition Định nghĩa 03.4 (Hàm động lực)
Giả sử $\mathcal S^+$, mọi $\mathcal A(s)$ và $\mathcal R$ là tập hữu hạn, trạng thái có tính Markov (Định nghĩa 03.2), và xác suất ở vế phải của (1.2) không phụ thuộc thời điểm $t$ và không phụ thuộc cách chọn hành động (lập luận sau Định nghĩa 02.16). Hàm động lực (dynamics function) của môi trường là hàm $p$ xác định với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$, $s'\in\mathcal S^+$, $r\in\mathcal R$, thỏa

$$
\begin{gathered}
p(s',r\mid s,a)\ge0,\\
\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1\\
\text{với mọi } s\in\mathcal S,\ a\in\mathcal A(s),
\end{gathered}
\tag{1.3}
$$

và mỗi khi sự kiện $\{S_t=s,A_t=a\}$ có xác suất dương,

$$
p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a).
\tag{1.4}
$$
:::

Hàm $p$ là đối tượng gốc của mô hình: nó được cho với mọi cặp hợp lệ, kể cả cặp mà một tác tử cụ thể không bao giờ chọn, còn (1.4) nói $p$ trùng với xác suất có điều kiện của quá trình mỗi khi xác suất đó xác định. Hai đối số sau vạch điều kiện, $s$ và $a$, được cố định; hai đối số trước vạch, $s'$ và $r$, chạy trong tổng chuẩn hóa (1.3). Mỗi hàng của bảng Ví dụ 03.5 là một giá trị của $p$; chẳng hạn hàng thứ năm cho

$$
p(\mathrm H,-3\mid\mathrm L,\mathrm{tim})=\tfrac12 ,
$$

nghĩa là từ pin thấp, khi chọn Tìm, robot về pin cao kèm phần thưởng $-3$ với xác suất $1/2$. Các bộ $(s',r)$ không có trong bảng có $p=0$, chẳng hạn $p(\mathrm H,2\mid\mathrm L,\mathrm{tim})=0$.

Hàm $p$ không mang chỉ số $t$ vì Định nghĩa 03.4 giả thiết thêm tính dừng (stationarity).

::: remark Nhận xét 03.5 (Tính dừng khác tính Markov)
- Tính Markov nói phản hồi chỉ phụ thuộc $(S_t,A_t)$, không phụ thuộc phần còn lại của lịch sử; tính dừng nói quy luật đó giống nhau ở mọi thời điểm. Một robot có pin lão hóa theo năm tháng có thể có trạng thái Markov nhưng hàm động lực thay đổi theo $t$.
- Trạng thái kế tiếp và phần thưởng được rút cùng nhau từ $p(\cdot,\cdot\mid s,a)$, không có giả thiết hai đại lượng độc lập.
:::

Hàm động lực là mô hình (model) của môi trường. Định nghĩa 03.4 là hàm động lực của Định nghĩa 02.16 khi các tập hữu hạn.

**Trong thực hành.** Môi trường mô phỏng như Gymnasium chỉ cho mẫu chuyển: gọi hàm bước với một hành động, chúng ta nhận một trạng thái mới và một phần thưởng, không nhận bảng $p$. Muốn có bảng $p$, chúng ta phải ước lượng nó từ các mẫu chuyển.

Notebook CartPole của Bài 04 chia trạng thái liên tục $(x,\dot x,\theta,\dot\theta)$, gồm vị trí và vận tốc của xe, góc và vận tốc góc của cột, thành $324$ ô, rồi với mỗi ô và mỗi hành động lấy $N_{\text{mẫu}}=200$ trạng thái đều trong ô, chạy một bước và đếm ô kế tiếp. Kết quả là mảng $\hat p(s'\mid s,a)$ cỡ $(2,324,325)$: hai hành động, $324$ ô hiện tại, và $325$ cột gồm $324$ ô cùng một trạng thái kết thúc. Mảng thưởng kỳ vọng ước lượng bằng $1$ ở mọi ô vì Gymnasium trả phần thưởng $+1$ ở mọi bước.

### 1.4 Xác suất chuyển và thưởng kỳ vọng

Bảng $p$ trả lời mọi câu hỏi về một bước, nhưng nhiều câu hỏi chỉ cần một phần của nó: robot sẽ về mức pin nào, hoặc trung bình nhận được bao nhiêu.

::: example Ví dụ 03.6 (Xác suất chuyển và thưởng kỳ vọng sau L–Tìm)
**Dữ kiện.** Cặp $(\mathrm L,\mathrm{tim})$ của Ví dụ 03.5 có hai phản hồi: $(\mathrm L,2)$ và $(\mathrm H,-3)$, mỗi phản hồi xác suất $1/2$.

**Xác suất về pin cao.** Chỉ hàng $(\mathrm H,-3)$ dẫn tới $\mathrm H$, nên xác suất về pin cao là $1/2$. Tương tự, xác suất ở lại pin thấp là $1/2$.

**Thưởng kỳ vọng.** Trung bình có trọng số của hai mức thưởng:

$$
\tfrac12\cdot2+\tfrac12\cdot(-3)=-\tfrac12 .
$$

**Kiểm tra lại.** Hai xác suất chuyển cộng lại bằng $1$. Mỗi lần thực hiện, robot nhận $2$ hoặc $-3$, không lần nào nhận đúng $-1/2$.
:::

Mệnh đề sau viết hai phép tính của Ví dụ 03.6 cho mọi cặp $(s,a)$.

::: proposition Mệnh đề 03.6 (Xác suất chuyển và thưởng kỳ vọng từ hàm động lực)
**Giả thiết.** Hàm động lực $p$ thỏa Định nghĩa 03.4; $s\in\mathcal S$, $a\in\mathcal A(s)$.

**Kết luận.** Xác suất chuyển trạng thái (state-transition probability) và thưởng kỳ vọng một bước (expected reward) tính được từ $p$:

$$
p(s'\mid s,a)=\sum_{r\in\mathcal R}p(s',r\mid s,a),
\tag{1.5}
$$

$$
r(s,a)=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}r\,p(s',r\mid s,a).
\tag{1.6}
$$

Khi $\{S_t=s,A_t=a\}$ có xác suất dương, $p(s'\mid s,a)=\Pr(S_{t+1}=s'\mid S_t=s,A_t=a)$ và $r(s,a)=\mathbb E[R_{t+1}\mid S_t=s,A_t=a]$. Ngoài ra $\sum_{s'}p(s'\mid s,a)=1$.

**Điều kiện áp dụng.** Các tập hữu hạn, nên mọi tổng là tổng hữu hạn.

**Phạm vi.** Chiều ngược lại không đúng: biết $p(s'\mid s,a)$ và $r(s,a)$ chưa đủ để dựng lại $p(s',r\mid s,a)$, vì $r(s,a)$ chỉ giữ trung bình của phần thưởng.
:::

::: proof Chứng minh Mệnh đề 03.6
**Bước 1 (xác suất biên).** Các sự kiện $\{S_{t+1}=s',R_{t+1}=r\}$ với $r\in\mathcal R$ rời nhau và hợp của chúng là $\{S_{t+1}=s'\}$. Cộng xác suất có điều kiện của chúng và dùng (1.4), ta được (1.5).

**Bước 2 (kỳ vọng và chuẩn hóa).** Kỳ vọng của biến rời rạc $R_{t+1}$ là $\sum_r r\Pr(R_{t+1}=r\mid S_t=s,A_t=a)$; thay xác suất biên bằng tổng theo $s'$ như ở Bước 1, ta được (1.6). Cộng (1.5) theo $s'$ và dùng (1.3) cho $\sum_{s'}p(s'\mid s,a)=1$. $\square$
:::

Công thức (1.5) gom các hàng có cùng trạng thái kế tiếp; (1.6) lấy trung bình phần thưởng với trọng số là xác suất của hàng. Với cặp $(\mathrm L,\mathrm{tim})$, ta được lại hai con số của Ví dụ 03.6. Ký hiệu ba đối số $p(s'\mid s,a)$ là một lạm dụng ký hiệu có chủ ý của Sutton và Barto (2018, (3.4)). Ghi chú Bài 02 đã nêu hai công thức này sau Định nghĩa 02.16; Mệnh đề 03.6 chứng minh chúng.

Nhầm lẫn thường gặp là coi $r(s,a)$ là phần thưởng robot nhận được; đó là kỳ vọng của biến ngẫu nhiên $R_{t+1}$. Hai rút gọn (1.5), (1.6) không đủ để mô phỏng phần thưởng. Ví dụ: nếu Tìm từ $\mathrm L$ cho phần thưởng $-\tfrac12$ trên cả hai nhánh, $p(\cdot\mid\mathrm L,\mathrm{tim})$ và $r(\mathrm L,\mathrm{tim})=-\tfrac12$ giữ nguyên, nhưng $p(\mathrm H,-3\mid\mathrm L,\mathrm{tim})$ đổi từ $\tfrac12$ thành $0$.

### 1.5 Quá trình quyết định Markov hữu hạn

Các thành phần mô tả môi trường đã đủ: tập trạng thái, tập hành động theo trạng thái, tập phần thưởng và hàm động lực. Các kết quả về giá trị ở các mục sau cần cùng lúc bốn thành phần này và giả thiết mọi quỹ đạo sinh ra theo $p$, nên chúng ta gom chúng thành một đối tượng.

::: definition Định nghĩa 03.7 (Quá trình quyết định Markov hữu hạn)
Quá trình quyết định Markov (Markov decision process, MDP) hữu hạn là bộ

$$
\mathcal M=\bigl(\mathcal S^+,\ \{\mathcal A(s)\}_{s\in\mathcal S},\ \mathcal R,\ p\bigr),
$$

trong đó $\mathcal S^+$ là tập trạng thái hữu hạn, gồm tập $\mathcal S$ các trạng thái chưa kết thúc và các trạng thái kết thúc nếu có; $\mathcal A(s)$ là tập hành động hữu hạn, khác rỗng tại mỗi $s\in\mathcal S$; $\mathcal R\subset\mathbb R$ là tập phần thưởng hữu hạn; $p$ là hàm động lực thỏa (1.3). Quỹ đạo của $\mathcal M$ sinh theo quy tắc: với mọi lịch sử $h_t$ kết thúc ở $s\in\mathcal S$ và mọi $a\in\mathcal A(s)$ có $\Pr(H_t=h_t,A_t=a)>0$,

$$
\Pr(S_{t+1}=s',R_{t+1}=r\mid H_t=h_t,A_t=a)=p(s',r\mid s,a).
$$
:::

Định nghĩa đặt tính Markov và tính dừng vào ngay quy tắc sinh quỹ đạo: phản hồi chỉ phụ thuộc trạng thái cuối và hành động, và cùng một hàm $p$ dùng cho mọi $t$. Bộ $\mathcal M$ chỉ mô tả môi trường; nó không chứa quy tắc chọn hành động.

Với robot:

- $\mathcal S^+=\mathcal S=\{\mathrm H,\mathrm L\}$, không có trạng thái kết thúc;
- $\mathcal A(\mathrm H)=\{\mathrm{tim},\mathrm{cho}\}$;
- $\mathcal A(\mathrm L)=\{\mathrm{tim},\mathrm{cho},\mathrm{sac}\}$;
- $\mathcal R=\{-3,0,1,2\}$;
- $p$ là bảy hàng của Ví dụ 03.5.

Robot của Ví dụ 03.4, với trạng thái chỉ ghi mức pin, không là MDP hữu hạn: hai lịch sử kết thúc ở $\mathrm L$ cho hai phân phối phản hồi khác nhau, nên không có hàm $p$ nào thỏa quy tắc sinh quỹ đạo.

Hệ số chiết khấu $\gamma$ cố ý đứng ngoài bộ $\mathcal M$, theo Sutton và Barto (2018, §3.1), vì nó thuộc về tiêu chuẩn đánh giá chứ không thuộc về môi trường: cùng một robot, đổi $\gamma$ là đổi bài toán nhưng không đổi bảng $p$.

::: exercise Bài tập 03.2
**Dữ kiện.** Robot của Ví dụ 03.1 với bảng phản hồi của Ví dụ 03.5: $(\mathrm H,\mathrm{tim})\to(\mathrm H,2)$ hoặc $(\mathrm L,2)$, mỗi nhánh $1/2$; $(\mathrm H,\mathrm{cho})\to(\mathrm H,1)$; $(\mathrm L,\mathrm{tim})\to(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi nhánh $1/2$; $(\mathrm L,\mathrm{cho})\to(\mathrm L,1)$; $(\mathrm L,\mathrm{sac})\to(\mathrm H,0)$.

**Yêu cầu.** Lập bảng $p(\mathrm H\mid s,a)$, $p(\mathrm L\mid s,a)$ và $r(s,a)$ cho cả năm cặp hợp lệ, rồi kiểm tra điều kiện chuẩn hóa của mỗi cặp.
:::

::: hint
Dùng (1.5) cho xác suất chuyển và (1.6) cho thưởng kỳ vọng; mỗi cặp chỉ có một hoặc hai hàng.
:::

::: solution
Theo (1.5) và (1.6):

| $(s,a)$ | $p(\mathrm H\mid s,a)$ | $p(\mathrm L\mid s,a)$ | $r(s,a)$ |
|---|---:|---:|---:|
| $(\mathrm H,\mathrm{tim})$ | $1/2$ | $1/2$ | $\tfrac12\cdot2+\tfrac12\cdot2=2$ |
| $(\mathrm H,\mathrm{cho})$ | $1$ | $0$ | $1$ |
| $(\mathrm L,\mathrm{tim})$ | $1/2$ | $1/2$ | $\tfrac12\cdot2+\tfrac12\cdot(-3)=-1/2$ |
| $(\mathrm L,\mathrm{cho})$ | $0$ | $1$ | $1$ |
| $(\mathrm L,\mathrm{sac})$ | $1$ | $0$ | $0$ |

**Kiểm tra lại.** Mỗi dòng có $p(\mathrm H\mid s,a)+p(\mathrm L\mid s,a)=1$, đúng phần cuối của Mệnh đề 03.6.
:::

Trạng thái có tính Markov (Định nghĩa 03.2), cùng giả thiết tính dừng, cho phép mô tả môi trường bằng một hàm động lực $p$ không phụ thuộc lịch sử và thời điểm (Định nghĩa 03.4); từ $p$ suy ra $p(s'\mid s,a)$ và $r(s,a)$ (Mệnh đề 03.6), và bốn thành phần $(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p)$ tạo thành MDP hữu hạn (Định nghĩa 03.7). Tuy nhiên, $p$ chỉ nói về một bước, nên chưa so sánh được hậu quả lâu dài của các lựa chọn.

<!-- note-topic-id: lec-03-part-03 -->
## 2. Lợi tức chiết khấu

Xếp hạng theo phần thưởng một bước đặt Chờ lên đầu ở pin thấp, nhưng sau Sạc robot ở pin cao, nơi mỗi lần Tìm cho $2$. Để tính đến các bước sau, chúng ta cần gộp cả chuỗi phần thưởng thành một số. Cộng thẳng không dùng được cho robot: nếu robot Chờ mãi ở pin thấp, tổng $1+1+1+\cdots$ tăng vô hạn, và mọi cách hành động có phần thưởng dương đều cho tổng vô hạn như nhau.

### 2.1 Chuỗi phần thưởng và trọng số theo thời gian

Một cách trực quan, phần thưởng nhận sớm đáng giá hơn phần thưởng nhận muộn, và một phần thưởng ở rất xa trong tương lai gần như không ảnh hưởng tới quyết định hiện tại. Một cách thể hiện điều này là nhân phần thưởng của bước thứ $k$ sau hiện tại với một trọng số giảm theo cấp số nhân. Ví dụ sau dùng trọng số giảm một nửa sau mỗi bước.

::: example Ví dụ 03.7 (Hai dãy phần thưởng ba bước từ pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1 bắt đầu ở $\mathrm L$. Trọng số của ba bước đầu là $1$, $1/2$, $1/4$.

- Dãy thứ nhất: robot Sạc (phần thưởng $0$, về $\mathrm H$), rồi Tìm từ $\mathrm H$ và pin giữ ở $\mathrm H$ (phần thưởng $2$), rồi Tìm từ $\mathrm H$ lần nữa (phần thưởng $2$). Dãy phần thưởng là $(0,2,2)$. Đường này có xác suất dương: lần Tìm đầu giữ pin ở $\mathrm H$ với xác suất $1/2$.
- Dãy thứ hai: robot Chờ ba lần ở $\mathrm L$; dãy phần thưởng là $(1,1,1)$.

**Tính.**

$$
\begin{aligned}
0+\tfrac12\cdot2+\tfrac14\cdot2&=\tfrac32,\\
1+\tfrac12\cdot1+\tfrac14\cdot1&=\tfrac74.
\end{aligned}
$$

**Diễn giải.** Tổng không trọng số của dãy thứ nhất lớn hơn ($4$ so với $3$), nhưng tổng có trọng số của dãy thứ hai lớn hơn. Phần thưởng $0$ của dãy thứ nhất rơi vào bước có trọng số lớn nhất, còn hai phần thưởng $2$ rơi vào hai bước có trọng số nhỏ hơn.

**Kiểm tra lại.** $\tfrac74-\tfrac32=\tfrac14=(1-0)\cdot1+(1-2)\cdot\tfrac12+(1-2)\cdot\tfrac14$.
:::

### 2.2 Lượt, nhiệm vụ và lợi tức

Trước khi viết công thức tổng quát, chúng ta cần biết chuỗi phần thưởng dài bao nhiêu. Mê cung của Bài 02 kết thúc khi tác tử tới đích; robot thu gom lon không có điểm dừng tự nhiên.

::: definition Định nghĩa 03.8 (Lượt, nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn)
Một nhiệm vụ là nhiệm vụ có kết thúc (episodic task) nếu tương tác chia thành các lượt (episode): mỗi lượt bắt đầu từ một trạng thái đầu và dừng khi tới một trạng thái kết thúc (terminal state) tại thời điểm $T<\infty$; $T$ là biến ngẫu nhiên và có thể khác nhau giữa các lượt. Khi đó $\mathcal S$ ký hiệu tập trạng thái chưa kết thúc và $\mathcal S^+$ ký hiệu $\mathcal S$ cùng các trạng thái kết thúc.

Một nhiệm vụ là nhiệm vụ tiếp diễn (continuing task) nếu tương tác không chia thành lượt; khi đó quy ước $T=\infty$ và $\mathcal S^+=\mathcal S$.
:::

Robot của Ví dụ 03.1 là nhiệm vụ tiếp diễn: cứu hộ và sạc chỉ đổi mức pin, không đóng lượt. Một lần đi mê cung hay một lần giữ cột trong CartPole là nhiệm vụ có kết thúc. Kết thúc một lượt là sự kiện của môi trường, khác việc dừng một thuật toán học chạy qua nhiều lượt.

Với hai loại nhiệm vụ đã phân biệt, chúng ta viết lại phép tính của Ví dụ 03.7 cho mọi dãy phần thưởng, với trọng số $\gamma^k$ thay cho $(1/2)^k$.

::: definition Định nghĩa 03.9 (Lợi tức chiết khấu)
Cho hệ số chiết khấu (discount factor) $\gamma\in[0,1]$ và thời điểm $t<T$. Lợi tức (return) từ thời điểm $t$ là

$$
\begin{aligned}
G_t&=\sum_{k=t+1}^{T}\gamma^{\,k-t-1}R_k\\
&=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots,
\end{aligned}
\tag{2.1}
$$

trong đó tổng có hữu hạn số hạng khi $T<\infty$, và là tổng của một chuỗi khi $T=\infty$; trường hợp $T=\infty$ chỉ dùng với $\gamma<1$. Quy ước $G_T=0$ khi $T<\infty$.
:::

Công thức (2.1) cộng mọi phần thưởng đến sau thời điểm $t$, bắt đầu từ $R_{t+1}$ với trọng số $\gamma^0=1$; phần thưởng đến sau $k$ bước nữa, $R_{t+k+1}$, mang trọng số $\gamma^k$. Lợi tức là biến ngẫu nhiên, vì mỗi quỹ đạo cho một dãy phần thưởng khác.

Quy ước $G_T=0$ nói rằng sau khi kết thúc không còn phần thưởng nào; $R_T$ vẫn nằm trong $G_{T-1}$. Với $\gamma=1/2$, ba số hạng đầu của (2.1) là đúng phép tính của Ví dụ 03.7, nên $3/2$ và $7/4$ là lợi tức cắt (truncated return) sau ba bước. Định nghĩa 03.9 trùng lợi tức của Định nghĩa 02.12, viết theo chỉ số thời gian $k$ của phần thưởng.

Sutton và Barto (2018, §3.4) gộp hai loại nhiệm vụ bằng một quy ước: coi trạng thái kết thúc là trạng thái hấp thụ (absorbing state), chỉ chuyển về chính nó với phần thưởng $0$.

::: remark Nhận xét 03.10 (Quy ước trạng thái hấp thụ)
Với nhiệm vụ có kết thúc tại $T<\infty$, đặt $R_k=0$ với mọi $k>T$. Khi đó, đổi chỉ số $j=k-t-1$ trong (2.1) và dùng $R_{t+j+1}=0$ với $j\ge T-t$, ta có

$$
\sum_{k=t+1}^{T}\gamma^{\,k-t-1}R_k=\sum_{j=0}^{\infty}\gamma^{\,j}R_{t+j+1}
$$

với mọi $\gamma\in[0,1]$, vì vế phải chỉ có hữu hạn số hạng khác $0$. Tương đương, sau thời điểm $T$ quá trình ở lại trạng thái kết thúc, mọi bước có phần thưởng $0$, và tại trạng thái kết thúc chỉ có một hành động giả. Từ đây, mọi phát biểu về đoạn quỹ đạo dài tùy ý dùng quy ước này cho nhiệm vụ có kết thúc. Phép đệm chỉ là quy ước tính toán trong một lượt; phần thưởng của lượt sau được tính trong lợi tức của lượt sau.
:::

### 2.3 Lợi tức hữu hạn

Với nhiệm vụ tiếp diễn, (2.1) là một chuỗi vô hạn, và chuỗi đó có thể phân kỳ. Nếu robot luôn Chờ ở pin thấp, mỗi bước nhận $1$. Với $\gamma=1$, lợi tức $1+1+1+\cdots$ phân kỳ. Với $\gamma=1/2$, lợi tức là tổng cấp số nhân $1+\tfrac12+\tfrac14+\cdots=2$: mỗi số hạng bằng một nửa số hạng trước, nên tổng tiến tới $2$ và không vượt $2$.

Mệnh đề sau là dạng tổng quát của lập luận này; Mệnh đề 02.13(b) của ghi chú Bài 02 đã nêu cùng cận.

::: proposition Mệnh đề 03.11 (Cận của lợi tức)
**Giả thiết.** Có hằng số $M\ge0$ sao cho $\lvert R_k\rvert\le M$ với mọi $k$; $0\le\gamma<1$.

**Kết luận.** Chuỗi (2.1) hội tụ tuyệt đối trên mọi quỹ đạo và

$$
\lvert G_t\rvert\le\frac{M}{1-\gamma}.
\tag{2.2}
$$

**Điều kiện áp dụng.** Mọi nhiệm vụ, có kết thúc hay tiếp diễn, với phần thưởng bị chặn và $\gamma<1$; với MDP hữu hạn, lấy $M=\max_{r\in\mathcal R}\lvert r\rvert$.

**Phạm vi.** Cận (2.2) đúng trên từng quỹ đạo, không chỉ cho kỳ vọng; nó không nói lợi tức đạt tới cận.
:::

::: proof Chứng minh Mệnh đề 03.11
**Bước 1 (chuỗi trội).** Với mọi $j\ge0$, giả thiết cho $\lvert\gamma^jR_{t+j+1}\rvert\le M\gamma^j$. Chuỗi $\sum_{j\ge0}M\gamma^j$ là cấp số nhân với công bội $\gamma\in[0,1)$, hội tụ và có tổng $M/(1-\gamma)$.

**Bước 2 (hội tụ tuyệt đối và cận).** Theo tiêu chuẩn so sánh, chuỗi $\sum_j\gamma^jR_{t+j+1}$ hội tụ tuyệt đối. Áp dụng bất đẳng thức tam giác cho các tổng riêng rồi chuyển qua giới hạn:

$$
\begin{aligned}
\lvert G_t\rvert&=\Bigl\lvert\sum_{j=0}^{\infty}\gamma^jR_{t+j+1}\Bigr\rvert\\
&\le\sum_{j=0}^{\infty}\gamma^j\lvert R_{t+j+1}\rvert\\
&\le\sum_{j=0}^{\infty}\gamma^jM\\
&=\frac{M}{1-\gamma}.
\end{aligned}
$$

Dòng thứ hai dùng bất đẳng thức tam giác, dòng thứ ba dùng giả thiết $\lvert R_k\rvert\le M$, dòng cuối là tổng cấp số nhân với $\gamma<1$.

Với nhiệm vụ có kết thúc, Nhận xét 03.10 cho phép viết $G_t$ thành cùng chuỗi với các số hạng đệm bằng $0$, nên cận vẫn đúng. $\square$
:::

Nghĩa là, khi phần thưởng bị chặn và $\gamma<1$, mọi lợi tức là số hữu hạn nằm trong cùng một khoảng không phụ thuộc quỹ đạo, nên kỳ vọng của lợi tức luôn tồn tại, với mọi cách chọn hành động.

Mỗi giả thiết của Mệnh đề 03.11 bị bỏ đều có phản ví dụ.

- Bỏ $\gamma<1$: robot luôn Chờ có $R_k=1$ với mọi $k$, nên với $\gamma=1$ lợi tức phân kỳ dù phần thưởng bị chặn bởi $M=1$.
- Bỏ phần thưởng bị chặn: dãy $R_{t+j+1}=2^j$ với $\gamma=1/2$ cho mọi số hạng $\gamma^jR_{t+j+1}=1$, và lợi tức phân kỳ dù $\gamma<1$.

Bước 1 của chứng minh dùng cả hai: phần thưởng bị chặn cho chuỗi trội, $\gamma<1$ làm chuỗi trội hội tụ.

::: example Ví dụ 03.8 (Cận lợi tức của robot)
**Dữ kiện.** Robot của Ví dụ 03.1 có $\mathcal R=\{-3,0,1,2\}$; chọn $\gamma=1/2$.

**Tính.** $M=\max\{3,0,1,2\}=3$, nên theo (2.2)

$$
\begin{gathered}
\lvert G_t\rvert\le\frac{3}{1-1/2}=6,\\
\text{tức }-6\le G_t\le6\ \text{trên mọi quỹ đạo}.
\end{gathered}
$$

**Diễn giải.** Các lợi tức $3/2$, $7/4$ của Ví dụ 03.7 và lợi tức $2$ của robot luôn Chờ đều nằm trong $[-6,6]$.

**Kiểm tra lại.** Cận không đạt được ở robot: để $G_t=6$ cần $R_k=3$ ở mọi bước, nhưng $3\notin\mathcal R$; để $G_t=-6$ cần $R_k=-3$ ở mọi bước, nhưng sau mỗi lần cứu hộ robot ở pin cao, nơi mọi hành động cho phần thưởng dương.
:::

::: remark Nhận xét 03.12 (Chọn hệ số chiết khấu)
- **Trường hợp $\gamma=1$.** Với nhiệm vụ có kết thúc, kỳ vọng của lợi tức hữu hạn khi, chẳng hạn, phần thưởng bị chặn và $\mathbb E[T]<\infty$; gắn nhãn "kết thúc" cho một trạng thái chưa bảo đảm tác tử sẽ tới đó.
- **Trường hợp $\gamma=0$.** Lợi tức chỉ còn $G_t=R_{t+1}$, và mục tiêu là cận thị (myopic): chỉ phần thưởng ngay sau hành động được tính. Ở robot, mục tiêu này xếp Chờ trên Sạc tại pin thấp, bỏ qua việc Sạc mở ra các bước Tìm ở pin cao (Sutton và Barto, 2018, tr. 55). Hành vi ứng với $\gamma$ gần $0$ còn được gọi là tham lam (greedy) theo phần thưởng trước mắt (Bài giảng gốc 2025–2026, trang 36).
- **$\gamma$ thuộc về bài toán.** Giá trị và chính sách tốt nhất có thể đổi theo $\gamma$.
:::

**Trong thực hành.** CartPole cho phần thưởng $+1$ ở mỗi bước, nên với $\gamma=0{,}99$ cận (2.2) là $100$; phần thưởng sau $100$ bước còn trọng số $0{,}99^{100}\approx0{,}37$. Trong notebook CartPole của Bài 04, một lượt của chính sách luôn đẩy phải kéo dài $9$ bước; theo (2.1), lợi tức chiết khấu của lượt đó là $(1-0{,}99^9)/0{,}01\approx8{,}65$.

::: exercise Bài tập 03.3
**Dữ kiện.** Robot của Ví dụ 03.1 bắt đầu ở $\mathrm L$, Tìm và nhận $2$ (vẫn ở $\mathrm L$), Tìm lần nữa và được cứu hộ ($-3$, về $\mathrm H$), rồi Chờ ở $\mathrm H$ (phần thưởng $1$). Ba phần thưởng đầu là $(R_1,R_2,R_3)=(2,-3,1)$; tập phần thưởng $\mathcal R=\{-3,0,1,2\}$.

**Yêu cầu.** (a) Robot về pin cao sau cứu hộ; xác định nhiệm vụ có kết thúc tại thời điểm đó không. (b) Tính lợi tức cắt sau ba bước $R_1+\gamma R_2+\gamma^2R_3$ với $\gamma=1/2$ và với $\gamma=0$. (c) Với $\gamma=1/2$, xác định khoảng chứa $G_0$ của mọi quỹ đạo có ba phần thưởng đầu như trên.
:::

::: hint
Câu (a) dùng Định nghĩa 03.8. Câu (c): phần đuôi $\sum_{j\ge3}\gamma^jR_{j+1}$ bị chặn theo cùng lập luận của Mệnh đề 03.11, với thừa số $\gamma^3$.
:::

::: solution
**(a)** Không. Robot là nhiệm vụ tiếp diễn (Định nghĩa 03.8): cứu hộ chỉ đổi trạng thái, tương tác vẫn tiếp tục và không có trạng thái kết thúc.

**(b)** Với $\gamma=1/2$: $2+\tfrac12\cdot(-3)+\tfrac14\cdot1=2-\tfrac32+\tfrac14=\tfrac34$. Với $\gamma=0$: chỉ số hạng đầu còn lại, bằng $2$.

**(c)** Phần đuôi có trị tuyệt đối không quá $\gamma^3M/(1-\gamma)=\tfrac18\cdot6=\tfrac34$, nên $G_0\in\bigl[\tfrac34-\tfrac34,\ \tfrac34+\tfrac34\bigr]=\bigl[0,\tfrac32\bigr]$.

**Kiểm tra lại.** Khoảng $[0,\tfrac32]$ nằm trong $[-6,6]$ của Ví dụ 03.8, như phải có.
:::

Lợi tức $G_t$ (Định nghĩa 03.9) hữu hạn trên mọi quỹ đạo khi phần thưởng bị chặn và $\gamma<1$ (Mệnh đề 03.11), với cùng một công thức cho hai loại nhiệm vụ nhờ quy ước trạng thái hấp thụ (Nhận xét 03.10). Tuy nhiên, $G_t$ là biến ngẫu nhiên: từ cùng một trạng thái, các quỹ đạo khác nhau cho các lợi tức khác nhau, nên chưa có một con số cho mỗi trạng thái.

<!-- note-topic-id: lec-03-part-04 -->
## 3. Chính sách và hàm giá trị

Lợi tức $G_t$ của robot có hai nguồn ngẫu nhiên: phản hồi của môi trường và lựa chọn của robot. Bảng $p$ mô tả nguồn thứ nhất sau khi hành động đã được chọn; nó không nói hành động được chọn theo quy tắc nào. Muốn nói đến trung bình của lợi tức, chúng ta phải cố định quy tắc chọn hành động ở mọi trạng thái; quy tắc đó là chính sách.

### 3.1 Chính sách

Xét một quy tắc chọn hành động cụ thể của robot, gọi là chính sách chia đều tại pin thấp; từ đây, các ví dụ về robot dùng quy tắc này cùng $\gamma=1/2$.

::: example Ví dụ 03.9 (Chính sách chia đều tại pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1. Ở pin cao, robot luôn Tìm. Ở pin thấp, robot chọn Chờ hoặc Sạc, mỗi hành động xác suất $1/2$, và không bao giờ Tìm.

**Bảng xác suất chọn hành động.**

| Trạng thái | Tìm | Chờ | Sạc |
|---|---:|---:|---:|
| $\mathrm H$ | $1$ | $0$ | không hợp lệ |
| $\mathrm L$ | $0$ | $1/2$ | $1/2$ |

**Đọc bảng.** Mỗi hàng là một phân phối trên các hành động hợp lệ của trạng thái đó. Ô "không hợp lệ" khác ô $0$: số $0$ là xác suất của một hành động hợp lệ nhưng không được chọn, còn ô không hợp lệ ứng với cặp nằm ngoài mô hình.

**Kiểm tra lại.** Hàng $\mathrm H$: $1+0=1$; hàng $\mathrm L$: $0+\tfrac12+\tfrac12=1$. Ở pin cao, quy tắc là tất định; ở pin thấp, quy tắc là ngẫu nhiên.
:::

![Từ nút L, hai mũi tên mang xác suất 1/2 tới hai khối hành động dưới nhãn "Chính sách": Chờ và Sạc; từ Chờ một mũi tên xác suất 1 tới khối "L; thưởng 1", từ Sạc một mũi tên xác suất 1 tới khối "H; thưởng 0" dưới nhãn "Môi trường".](img/lec-03/robot-p04-two-layers.svg)

Hình trên tách một bước của robot ở pin thấp thành hai tầng. Tầng "Chính sách" rút hành động với các xác suất $1/2$ của Ví dụ 03.9; tầng "Môi trường" rút phản hồi theo bảng $p$ của Ví dụ 03.5, ở đây là chắc chắn. Xác suất của mỗi đường từ trái sang phải là tích các số trên đường, $\tfrac12\cdot1=\tfrac12$.

Một cách trực quan, chính sách là tầng thứ nhất của hình, viết cho mọi trạng thái.

::: definition Định nghĩa 03.13 (Chính sách Markov dừng)
Một chính sách Markov dừng (stationary Markov policy) là một hàm $\pi$ gán cho mỗi trạng thái $s\in\mathcal S$ một phân phối xác suất $\pi(\cdot\mid s)$ trên $\mathcal A(s)$:

$$
\begin{gathered}
\pi(a\mid s)\ge0,\\
\sum_{a\in\mathcal A(s)}\pi(a\mid s)=1 .
\end{gathered}
$$

Tác tử theo chính sách $\pi$ tại thời điểm $t$ nếu với mọi lịch sử $h_t$ kết thúc ở $s\in\mathcal S$ có $\Pr(H_t=h_t)>0$,

$$
\Pr(A_t=a\mid H_t=h_t)=\pi(a\mid s).
\tag{3.1}
$$

Cho một phân phối đầu $\mu$ của $S_0$, ký hiệu $\Pr_\pi$, $\mathbb E_\pi$ là xác suất và kỳ vọng trên các quỹ đạo sinh ra khi $S_0$ rút theo $\mu$, hành động theo (3.1) ở mọi thời điểm và phản hồi theo hàm động lực $p$. Ký hiệu này cũng dùng cho quá trình chỉ theo $\pi$ từ một thời điểm trở đi.
:::

"Markov" nghĩa là xác suất chọn hành động chỉ phụ thuộc trạng thái hiện tại; "dừng" nghĩa là cùng hàm $\pi$ được dùng ở mọi thời điểm. Chính sách xác định là trường hợp riêng khi mỗi $\pi(\cdot\mid s)$ dồn xác suất $1$ vào một hành động. Ở Ví dụ 03.9, $\pi(\mathrm{tim}\mid\mathrm H)=1$ (xác định tại $\mathrm H$) và $\pi(\mathrm{cho}\mid\mathrm L)=\pi(\mathrm{sac}\mid\mathrm L)=1/2$.

Chính sách bổ sung cho hàm động lực: $p$ là quy luật của môi trường, $\pi$ là quy luật của tác tử. Nhầm lẫn thường gặp là nghĩ đổi chính sách thì đổi mô hình; đổi chính sách không đổi bảng $p$, nhưng đổi xác suất của mọi quỹ đạo. Định nghĩa 03.13 là chính sách ngẫu nhiên của Định nghĩa 02.8 khi biểu diễn là trạng thái, $X_t=S_t$.

Mệnh đề sau cho xác suất của một đoạn quỹ đạo dưới cặp $(\pi,p)$. Với nhiệm vụ có kết thúc, đoạn quỹ đạo có thể vượt quá thời điểm kết thúc; khi đó ta dùng quy ước trạng thái hấp thụ của Nhận xét 03.10, với hành động giả được chọn với xác suất $1$.

::: proposition Mệnh đề 03.14 (Xác suất của một đoạn quỹ đạo)
**Giả thiết.** MDP hữu hạn (Định nghĩa 03.7) với quy ước của Nhận xét 03.10; tác tử theo chính sách Markov dừng $\pi$ tại mọi thời điểm từ $t$ trở đi; lịch sử $h_t$ kết thúc ở $s_t$ có $\Pr_\pi(H_t=h_t)>0$.

**Kết luận.** Với mọi $K\ge1$ và mọi dãy giá trị $a_{t+i}$, $r_{t+i+1}$, $s_{t+i+1}$, $0\le i<K$, đặt $E_i$ là sự kiện $\{A_{t+i}=a_{t+i},\,R_{t+i+1}=r_{t+i+1},\,S_{t+i+1}=s_{t+i+1}\}$. Khi đó

$$
\Pr_\pi\bigl(E_0\cap E_1\cap\dots\cap E_{K-1}\mid H_t=h_t\bigr)=\prod_{i=0}^{K-1}\pi(a_{t+i}\mid s_{t+i})\,p(s_{t+i+1},r_{t+i+1}\mid s_{t+i},a_{t+i}).
\tag{3.2}
$$

**Điều kiện áp dụng.** Mọi đoạn hữu hạn; vế phải không phụ thuộc phần lịch sử trước $s_t$, không phụ thuộc $t$ và không phụ thuộc phân phối đầu.

**Phạm vi.** Mệnh đề nói về đoạn dài hữu hạn $K$; phát biểu cho toàn bộ tương lai vô hạn được suy ra qua các đoạn hữu hạn ở Bổ đề 03.20.
:::

::: proof Chứng minh Mệnh đề 03.14
Ta quy nạp theo $K$. Gọi $h_{t+i}$ là lịch sử $h_t$ nối thêm $i$ bộ đã cho; sự kiện $\{H_t=h_t\}\cap E_0\cap\dots\cap E_{i-1}$ chính là $\{H_{t+i}=h_{t+i}\}$.

**Bước 1 (một bước).** Với $K=1$, quy tắc nhân cho

$$
\begin{aligned}
\Pr_\pi(E_0\mid H_t=h_t)&=\Pr_\pi(A_t=a_t\mid H_t=h_t)\\
&\quad\times\Pr_\pi(S_{t+1}=s_{t+1},R_{t+1}=r_{t+1}\mid H_t=h_t,A_t=a_t).
\end{aligned}
$$

Thừa số thứ nhất bằng $\pi(a_t\mid s_t)$ theo (3.1); thừa số thứ hai bằng $p(s_{t+1},r_{t+1}\mid s_t,a_t)$ theo quy tắc sinh quỹ đạo của Định nghĩa 03.7. Nếu thừa số thứ nhất bằng $0$, cả hai vế bằng $0$.

**Bước 2 (từ $K$ sang $K+1$).** Giả sử (3.2) đúng với $K$. Nếu vế phải với $K$ bằng $0$ thì cả hai vế với $K+1$ bằng $0$. Nếu dương, lịch sử $h_{t+K}$ có xác suất dương và kết thúc ở $s_{t+K}$. Theo quy tắc nhân, xác suất của $K+1$ bước bằng xác suất của $K$ bước nhân với $\Pr_\pi(E_K\mid H_{t+K}=h_{t+K})$, và theo Bước 1 áp dụng tại thời điểm $t+K$, thừa số này bằng $\pi(a_{t+K}\mid s_{t+K})\,p(s_{t+K+1},r_{t+K+1}\mid s_{t+K},a_{t+K})$. Vậy (3.2) đúng với $K+1$. $\square$
:::

Công thức (3.2) nói xác suất của một đoạn quỹ đạo là tích, qua từng bước, của xác suất chọn hành động và xác suất phản hồi. Mệnh đề 03.14 tổng quát hóa phép tính của Ví dụ 02.8 cho đoạn dài $K$ bước. Từ $\mathrm H$ dưới chính sách chia đều tại pin thấp, đoạn "Tìm, về $\mathrm L$ với phần thưởng $2$, Sạc, về $\mathrm H$ với phần thưởng $0$" có xác suất $1\cdot\tfrac12\cdot\tfrac12\cdot1=\tfrac14$.

Tích này không giả thiết hành động độc lập với phản hồi; mỗi thừa số là xác suất có điều kiện, rút gọn được nhờ (3.1) và quy tắc sinh quỹ đạo của Định nghĩa 03.7.

### 3.2 Kỳ vọng của lợi tức và giá trị trạng thái

Với chính sách đã cố định, Mệnh đề 03.14 cho xác suất của mọi đoạn quỹ đạo, nên kỳ vọng của mọi đại lượng tính từ một đoạn hữu hạn là một tổng hữu hạn. Ví dụ sau tính kỳ vọng của hai số hạng đầu của lợi tức từ pin cao bằng cách liệt kê các nhánh.

::: example Ví dụ 03.10 (Kỳ vọng hai bước từ pin cao)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$), $\gamma=1/2$, $S_0=\mathrm H$. Đại lượng cần tính là lợi tức cắt sau hai bước

$$
G_0^{[2]}=R_1+\gamma R_2 .
$$

**Liệt kê nhánh.** Ở $\mathrm H$, chính sách chọn Tìm với xác suất $1$, nên $R_1=2$ và $S_1$ là $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $1/2$.

- $S_1=\mathrm H$: chính sách lại chọn Tìm, $R_2=2$. Nhóm này có xác suất $\tfrac12$ và $G_0^{[2]}=2+\tfrac12\cdot2=3$.
- $S_1=\mathrm L$, chọn Chờ: xác suất $\tfrac12\cdot\tfrac12=\tfrac14$, $R_2=1$, $G_0^{[2]}=2+\tfrac12\cdot1=\tfrac52$.
- $S_1=\mathrm L$, chọn Sạc: xác suất $\tfrac14$, $R_2=0$, $G_0^{[2]}=2$.

**Tính kỳ vọng.**

$$
\begin{aligned}
\mathbb E_\pi\bigl[G_0^{[2]}\mid S_0=\mathrm H\bigr]&=\tfrac12\cdot3+\tfrac14\cdot\tfrac52+\tfrac14\cdot2\\
&=\tfrac{12}{8}+\tfrac58+\tfrac48\\
&=\tfrac{21}{8}.
\end{aligned}
$$

**Kiểm tra lại.** Theo tuyến tính, $\mathbb E_\pi[R_1]+\gamma\,\mathbb E_\pi[R_2]=2+\tfrac12\cdot\tfrac54=\tfrac{21}{8}$.
:::

![Cây hai bước từ H. Bước 1: Tìm, phần thưởng +2, tới H hoặc L, mỗi nhánh 1/2. Từ H, hành động 2 là Tìm với xác suất 1, phần thưởng +2, ô cuối ghi "3; gộp 1/2". Từ L, hành động 2 là Chờ (1/2, phần thưởng +1) với ô cuối "5/2; 1/4", hoặc Sạc (1/2, phần thưởng 0) với ô cuối "2; 1/4".](img/lec-03/robot-p04-two-step-tree.svg)

Trên cây, mỗi đường từ gốc tới một ô cuối là một nhóm quỹ đạo, ô cuối ghi $G_0^{[2]}$ và xác suất của nhóm theo (3.2). Số $1$ trên cạnh tới "Tìm: +2" là xác suất chính sách chọn Tìm; nhãn "gộp 1/2" gộp hai trạng thái kế tiếp cho cùng $R_2=2$.

Một cách trực quan, giá trị của pin cao là con số thu được nếu kéo dài cây trên xuống mọi tầng: mỗi đường vô hạn từ gốc mang một lợi tức đầy đủ $G_0$, và ta lấy trung bình các lợi tức đó với trọng số là xác suất của đường. Cây vô hạn không liệt kê được, nên định nghĩa sau gọi tên đại lượng đó bằng kỳ vọng.

::: definition Định nghĩa 03.15 (Hàm giá trị trạng thái)
Cho MDP hữu hạn, chính sách Markov dừng $\pi$, phần thưởng bị chặn và $0\le\gamma<1$. Với $s\in\mathcal S$, gọi quá trình xuất phát tại $s$ là quá trình có $S_0=s$ với xác suất $1$, hành động theo (3.1) và phản hồi theo $p$. Hàm giá trị trạng thái (state-value function) của $\pi$ là hàm $v_\pi:\mathcal S^+\to\mathbb R$,

$$
v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s],
\tag{3.3}
$$

trong đó kỳ vọng lấy trên quá trình xuất phát tại $s$. Với trạng thái kết thúc $s$, quy ước $v_\pi(s)=0$.
:::

Định nghĩa (3.3) đọc như sau: xuất phát ở $s$, hành động rút theo $\pi$, phản hồi rút theo $p$, và $v_\pi(s)$ là trung bình của lợi tức trên mọi quỹ đạo đó; kỳ vọng tồn tại vì $\lvert G_0\rvert\le M/(1-\gamma)$. Ký hiệu điều kiện $S_0=s$ cho cùng một số với mọi phân phối đầu $\mu$ có $\mu(s)>0$, theo (3.2) và Bổ đề 03.20(b) với $t=0$, $h_0=(s)$.

Định nghĩa 03.15 là Định nghĩa 02.14 với các tập hữu hạn; phần thưởng bị chặn và $\gamma<1$ bảo đảm giả thiết kỳ vọng hữu hạn của định nghĩa đó. Sutton và Barto (2018, (3.12)) viết $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ với $t$ bất kỳ; hai cách viết cho cùng một số (Bổ đề 03.20(c)).

Ví dụ 03.10 là một xấp xỉ của $v_\pi(\mathrm H)$ chỉ dùng hai số hạng đầu. Phần bị bỏ có trị tuyệt đối không quá $\gamma^2M/(1-\gamma)=\tfrac14\cdot6=\tfrac32$, nên

$$
v_\pi(\mathrm H)\in\Bigl[\tfrac{21}{8}-\tfrac32,\ \tfrac{21}{8}+\tfrac32\Bigr]=\Bigl[\tfrac98,\ \tfrac{33}{8}\Bigr].
$$

### 3.3 Giá trị hành động

Giá trị trạng thái để chính sách chọn cả hành động đầu tiên. Ở pin thấp, chính sách chia đều không bao giờ Tìm, nên $v_\pi(\mathrm L)$ không cho biết điều gì xảy ra nếu robot Tìm một lần. Để so sánh từng lựa chọn, chúng ta cần một đại lượng ấn định hành động đầu tiên.

Một cách trực quan, chúng ta làm một thí nghiệm: đặt robot ở $s$, ấn định hành động $a$ ở bước đầu, rồi từ bước sau để nó theo $\pi$. Lợi tức kỳ vọng của thí nghiệm này là giá trị của hành động $a$ tại $s$. Ví dụ sau thực hiện ba thí nghiệm như vậy, mỗi thí nghiệm chỉ tính hai bước.

::: example Ví dụ 03.11 (Ba thí nghiệm từ pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$, $S_0=\mathrm L$. Hành động $A_0$ bị ấn định; từ $t=1$ robot theo $\pi$. Đại lượng tính là kỳ vọng của $G_0^{[2]}=R_1+\gamma R_2$.

**Ấn định Tìm.** Hai phản hồi, mỗi phản hồi xác suất $1/2$.

- $(\mathrm L,2)$: ở $\mathrm L$ chính sách chọn Chờ hoặc Sạc, $\mathbb E[R_2]=\tfrac12\cdot1+\tfrac12\cdot0=\tfrac12$, nên kỳ vọng của nhánh là $2+\tfrac12\cdot\tfrac12=\tfrac94$.
- $(\mathrm H,-3)$: ở $\mathrm H$ chính sách chọn Tìm, $R_2=2$, nên nhánh cho $-3+\tfrac12\cdot2=-2$.

Kỳ vọng: $\tfrac12\cdot\tfrac94+\tfrac12\cdot(-2)=\tfrac18$.

**Ấn định Chờ.** $R_1=1$, $S_1=\mathrm L$, $\mathbb E[R_2]=\tfrac12$; kỳ vọng $1+\tfrac12\cdot\tfrac12=\tfrac54$.

**Ấn định Sạc.** $R_1=0$, $S_1=\mathrm H$, $R_2=2$; kỳ vọng $0+\tfrac12\cdot2=1$.

**Kiểm tra lại.** Với Tìm, phần $R_1$ góp $r(\mathrm L,\mathrm{tim})=-\tfrac12$ (Ví dụ 03.6) và phần $\gamma R_2$ góp $\tfrac12\bigl(\tfrac12\cdot\tfrac12+\tfrac12\cdot2\bigr)=\tfrac58$; tổng là $\tfrac18$.
:::

::: definition Định nghĩa 03.16 (Hàm giá trị hành động)
Với cùng giả thiết của Định nghĩa 03.15, $s\in\mathcal S$ và $a\in\mathcal A(s)$, gọi quá trình ấn định $(s,a)$ là quá trình có $S_0=s$, $A_0=a$ với xác suất $1$, phản hồi theo $p$, và hành động theo (3.1) từ thời điểm $1$ trở đi. Hàm giá trị hành động (action-value function) của $\pi$ là

$$
q_\pi(s,a)=\mathbb E_\pi[G_0\mid S_0=s,A_0=a],
\tag{3.4}
$$

trong đó kỳ vọng lấy trên quá trình ấn định $(s,a)$.
:::

Khác biệt duy nhất giữa $q_\pi(s,a)$ và $v_\pi(s)$ là hành động đầu: $v_\pi$ để chính sách rút nó, $q_\pi$ ấn định nó. Ba con số $\tfrac18$, $\tfrac54$, $1$ của Ví dụ 03.11 là kỳ vọng của hai số hạng đầu của lợi tức trong ba thí nghiệm định nghĩa $q_\pi(\mathrm L,\mathrm{tim})$, $q_\pi(\mathrm L,\mathrm{cho})$, $q_\pi(\mathrm L,\mathrm{sac})$. Khi $\Pr_\pi(S_t=s,A_t=a)>0$, kỳ vọng có điều kiện $\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ của Sutton và Barto (2018, (3.13)) bằng $q_\pi(s,a)$ (Bổ đề 03.20(d)).

::: remark Nhận xét 03.17 (Ba cách hiểu sai về giá trị)
- **$q_\pi(s,a)$ có nghĩa khi $\pi(a\mid s)=0$.** Định nghĩa dùng quá trình ấn định hành động, không chia cho $\Pr_\pi(A_t=a\mid S_t=s)$. Vì vậy $q_\pi(\mathrm L,\mathrm{tim})$ xác định dù $\pi(\mathrm{tim}\mid\mathrm L)=0$.
- **$q_\pi(s,a)$ khác $r(s,a)$.** Thưởng kỳ vọng $r(s,a)$ chỉ tính bước đầu; $q_\pi(s,a)$ tính toàn bộ tương lai. Ở pin thấp, $r(\mathrm L,\mathrm{cho})=1$ còn kỳ vọng hai bước của thí nghiệm Chờ đã là $5/4$.
- **$v_\pi(s)$ khác lợi tức $G_t$.** $G_t$ thay đổi theo quỹ đạo; $v_\pi(s)$ là trung bình của nó.
:::

::: exercise Bài tập 03.4
**Dữ kiện.** Robot của Ví dụ 03.1 ($\mathrm L$–Chờ: $(\mathrm L,1)$ chắc chắn; $\mathrm L$–Sạc: $(\mathrm H,0)$ chắc chắn; $\mathrm H$–Tìm: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$). Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$. $\gamma=1/2$, $S_0=\mathrm L$.

**Yêu cầu.** (a) Liệt kê các nhánh hai bước từ $\mathrm L$, ghi xác suất và giá trị $G_0^{[2]}=R_1+\gamma R_2$ của mỗi nhánh, rồi tính $\mathbb E_\pi[G_0^{[2]}\mid S_0=\mathrm L]$. (b) Kiểm tra kết quả bằng cách lấy trung bình hai kết quả thí nghiệm Chờ ($5/4$) và Sạc ($1$) của Ví dụ 03.11 theo trọng số chính sách. (c) Giải thích vì sao kết quả câu (a) chưa phải $v_\pi(\mathrm L)$.
:::

::: hint
Sau Chờ, robot ở $\mathrm L$ và lại chọn Chờ hoặc Sạc; sau Sạc, robot ở $\mathrm H$ và chọn Tìm.
:::

::: solution
**(a)** Có ba nhánh.

- Chờ rồi Chờ: xác suất $\tfrac12\cdot\tfrac12=\tfrac14$, $G_0^{[2]}=1+\tfrac12\cdot1=\tfrac32$.
- Chờ rồi Sạc: xác suất $\tfrac14$, $G_0^{[2]}=1+\tfrac12\cdot0=1$.
- Sạc rồi Tìm: xác suất $\tfrac12\cdot1=\tfrac12$, $G_0^{[2]}=0+\tfrac12\cdot2=1$.

Kỳ vọng:

$$
\begin{aligned}
\mathbb E_\pi\bigl[G_0^{[2]}\mid S_0=\mathrm L\bigr]&=\tfrac14\cdot\tfrac32+\tfrac14\cdot1+\tfrac12\cdot1\\
&=\tfrac38+\tfrac28+\tfrac48\\
&=\tfrac98 .
\end{aligned}
$$

**(b)** $\tfrac12\cdot\tfrac54+\tfrac12\cdot1=\tfrac58+\tfrac48=\tfrac98$, trùng câu (a). Thí nghiệm Tìm không đóng góp vì $\pi(\mathrm{tim}\mid\mathrm L)=0$.

**(c)** $\tfrac98$ chỉ là kỳ vọng của hai số hạng đầu; $v_\pi(\mathrm L)$ còn chứa phần $\gamma^2R_3+\gamma^3R_4+\cdots$.

**Kiểm tra lại.** Ba xác suất cộng lại bằng $\tfrac14+\tfrac14+\tfrac12=1$.
:::

::: exercise Bài tập 03.5
**Dữ kiện.** Robot của Ví dụ 03.1 với chính sách chia đều tại pin thấp, $\gamma=1/2$.

**Yêu cầu.** Đổi chính sách ở pin thấp thành "Chờ với xác suất $3/4$, Sạc với xác suất $1/4$". Trong ba đối tượng hàm động lực $p$, chính sách $\pi$ và hàm giá trị $v_\pi$, xác định đối tượng nào chắc chắn đổi, đối tượng nào chắc chắn giữ nguyên, đối tượng nào có thể đổi, và giải thích.
:::

::: hint
Hàm động lực thuộc về môi trường; chính sách thuộc về tác tử; hàm giá trị phụ thuộc cả hai.
:::

::: solution
Chính sách $\pi$ đổi theo giả thiết. Hàm động lực $p$ giữ nguyên, vì phản hồi của môi trường sau mỗi cặp $(s,a)$ không phụ thuộc cách chọn hành động. Hàm giá trị $v_\pi$ có thể đổi, vì xác suất của các quỹ đạo, tính theo (3.2), thay đổi khi $\pi$ đổi.

**Kiểm tra lại.** Theo (3.2), xác suất của mỗi đoạn quỹ đạo là tích các thừa số $\pi$ và $p$; đổi chính sách chỉ đổi các thừa số $\pi$.
:::

Chính sách Markov dừng (Định nghĩa 03.13) cho xác suất của mọi đoạn quỹ đạo dưới dạng tích các thừa số $\pi$ và $p$ (Mệnh đề 03.14), nên $v_\pi$ và $q_\pi$ (Định nghĩa 03.15, 03.16) là các kỳ vọng tồn tại và hữu hạn. Tuy nhiên, đó vẫn là kỳ vọng trên vô hạn quỹ đạo dài vô hạn, và việc liệt kê nhánh chỉ cho vài số hạng đầu.

<!-- note-topic-id: lec-03-part-05 -->
## 4. Phương trình Bellman kỳ vọng

Để tránh liệt kê vô hạn quỹ đạo, chúng ta nhóm các quỹ đạo theo bước đầu tiên: mỗi nhóm có một phần thưởng ngay và một phần còn lại bắt đầu ở trạng thái kế tiếp. Nếu kỳ vọng của phần còn lại bằng giá trị của trạng thái kế tiếp, mỗi trạng thái cho một phương trình với hữu hạn ẩn.

### 4.1 Phương trình một bước tại pin thấp

Ví dụ sau viết phương trình cho $v_\pi(\mathrm L)$, tạm chấp nhận rằng kỳ vọng của phần còn lại bằng giá trị của trạng thái kế tiếp; Bổ đề 03.20 chứng minh điều này.

::: example Ví dụ 03.12 (Phương trình một bước tại pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$. Ở $\mathrm L$, chính sách chọn Chờ hoặc Sạc, mỗi hành động $1/2$; Chờ cho $(\mathrm L,1)$ chắc chắn, Sạc cho $(\mathrm H,0)$ chắc chắn.

**Nhóm theo bước đầu.**

- Nhóm Chờ (xác suất $1/2$): phần thưởng ngay $1$; phần còn lại bắt đầu ở $\mathrm L$, được chiết khấu một lần, đóng góp $\gamma\,v_\pi(\mathrm L)$ nếu kỳ vọng của nó bằng $v_\pi(\mathrm L)$.
- Nhóm Sạc (xác suất $1/2$): phần thưởng ngay $0$; phần còn lại bắt đầu ở $\mathrm H$, đóng góp $\gamma\,v_\pi(\mathrm H)$.

**Phương trình.**

$$
\begin{aligned}
v_\pi(\mathrm L)&=\tfrac12\bigl[1+\tfrac12\,v_\pi(\mathrm L)\bigr]\\
&\quad+\tfrac12\bigl[0+\tfrac12\,v_\pi(\mathrm H)\bigr].
\end{aligned}
\tag{4.1}
$$

**Đọc phương trình.** Hai hệ số $\tfrac12$ ngoài ngoặc là $\pi(\mathrm{cho}\mid\mathrm L)$ và $\pi(\mathrm{sac}\mid\mathrm L)$; hệ số $\tfrac12$ trước $v_\pi$ trong ngoặc là $\gamma$. Ẩn $v_\pi(\mathrm L)$ có ở cả hai vế vì Chờ giữ nguyên mức pin.

**Kiểm tra lại.** Thay $v_\pi$ trong ngoặc bằng thưởng kỳ vọng một bước dưới chính sách tại trạng thái kế tiếp ($\tfrac12$ ở $\mathrm L$, $2$ ở $\mathrm H$) cho $\tfrac12(1+\tfrac14)+\tfrac12(0+1)=\tfrac98$, trùng kỳ vọng hai bước của Bài tập 03.4.
:::

Để (4.1) thành một kết quả, cần ba bước:

- tách lợi tức thành phần thưởng ngay và phần còn lại;
- lấy kỳ vọng theo hành động đầu, rồi theo phản hồi đầu;
- chứng minh kỳ vọng của phần còn lại bằng giá trị của trạng thái kế tiếp.

### 4.2 Hệ thức đệ quy của lợi tức

Bước thứ nhất là một hệ thức trên từng quỹ đạo, không dùng xác suất. Mệnh đề 02.13(a) của ghi chú Bài 02 đã nêu hệ thức này; bổ đề sau ghi rõ giả thiết để các chuỗi $G_t$, $G_{t+1}$ hội tụ.

::: lemma Bổ đề 03.18 (Hệ thức đệ quy của lợi tức)
**Giả thiết.** Phần thưởng bị chặn, $\lvert R_k\rvert\le M$, và $0\le\gamma<1$; hoặc nhiệm vụ có kết thúc với $T<\infty$, $\gamma\in[0,1]$ và quy ước $G_T=0$.

**Kết luận.** Với mọi $t<T$, trên mọi quỹ đạo,

$$
G_t=R_{t+1}+\gamma\,G_{t+1}.
\tag{4.2}
$$

**Điều kiện áp dụng.** Mọi dãy phần thưởng mà các chuỗi $G_t$, $G_{t+1}$ hội tụ.

**Phạm vi.** Đây là đẳng thức đại số; nó không dùng chính sách, hàm động lực hay tính Markov.
:::

::: proof Chứng minh Bổ đề 03.18
**Bước 1 (trường hợp vô hạn).** Theo Mệnh đề 03.11, chuỗi (2.1) của $G_t$ và của $G_{t+1}$ hội tụ tuyệt đối. Tách số hạng đầu, đặt $\gamma$ ra ngoài phần còn lại, rồi đổi chỉ số $j=i+1$:

$$
\begin{aligned}
G_t&=\sum_{j=0}^{\infty}\gamma^jR_{t+j+1}\\
&=R_{t+1}+\sum_{j=1}^{\infty}\gamma^jR_{t+j+1}\\
&=R_{t+1}+\gamma\sum_{i=0}^{\infty}\gamma^iR_{(t+1)+i+1}\\
&=R_{t+1}+\gamma\,G_{t+1}.
\end{aligned}
$$

Dòng đầu là Định nghĩa 03.9; dòng thứ hai tách số hạng $j=0$; dòng thứ ba đặt $j=i+1$; dòng cuối là Định nghĩa 03.9 tại $t+1$.

**Bước 2 (trường hợp có kết thúc).** Khi $T<\infty$, các tổng là hữu hạn và cùng phép tách cho $G_t=R_{t+1}+\gamma\sum_{k=t+2}^{T}\gamma^{k-t-2}R_k$. Với $t<T-1$, tổng cuối là $G_{t+1}$. Với $t=T-1$, tổng cuối rỗng và bằng $0=G_T$ theo quy ước. $\square$
:::

Đẳng thức (4.2) nói rằng lợi tức từ $t$ bằng phần thưởng của bước kế tiếp cộng lợi tức từ $t+1$ đã chiết khấu một lần. Số hạng đầu của $G_{t+1}$ là $R_{t+2}$, không phải $R_{t+1}$; viết lệch chỉ số ở đây là lỗi thường gặp.

### 4.3 Hai tầng kỳ vọng

Bước thứ hai lấy kỳ vọng của (4.2) bằng cách nhóm quỹ đạo theo hành động đầu, rồi theo phản hồi đầu, như hai tầng Chính sách và Môi trường của hình một bước ở pin thấp. Công cụ là kỳ vọng toàn phần $\mathbb E[X\mid B]=\sum_y\Pr(Y=y\mid B)\,\mathbb E[X\mid Y=y,B]$.

::: lemma Bổ đề 03.19 (Hai tầng kỳ vọng)
**Giả thiết.** MDP hữu hạn, tác tử theo chính sách Markov dừng $\pi$ tại thời điểm $t$; $X$ là biến ngẫu nhiên bị chặn xác định trên quỹ đạo; $h_t$ là lịch sử kết thúc ở $s\in\mathcal S$ với $\Pr_\pi(H_t=h_t)>0$.

**Kết luận.**

(a) Tầng hành động: tổng lấy trên các $a$ có $\pi(a\mid s)>0$,

$$
\mathbb E_\pi[X\mid H_t=h_t]=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,\mathbb E_\pi[X\mid H_t=h_t,A_t=a].
\tag{4.3}
$$

(b) Tầng phản hồi: với $a$ có $\Pr_\pi(H_t=h_t,A_t=a)>0$, tổng lấy trên các $(s',r)$ có $p(s',r\mid s,a)>0$,

$$
\begin{aligned}
\mathbb E_\pi[X\mid H_t=h_t,A_t=a]&=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\\
&\qquad\times\mathbb E_\pi[X\mid H_t=h_t,A_t=a,S_{t+1}=s',R_{t+1}=r].
\end{aligned}
\tag{4.4}
$$

**Điều kiện áp dụng.** Các tập hữu hạn và $X$ bị chặn, nên mọi kỳ vọng tồn tại và mọi tổng hữu hạn.

**Phạm vi.** Bổ đề chưa bỏ được lịch sử $h_t$ khỏi các kỳ vọng ở vế phải; việc đó cần Bổ đề 03.20.
:::

::: proof Chứng minh Bổ đề 03.19
**Bước 1 (tầng hành động).** $A_t$ nhận hữu hạn giá trị trong $\mathcal A(s)$. Theo kỳ vọng toàn phần với điều kiện nền $\{H_t=h_t\}$, vế trái của (4.3) bằng tổng có trọng số $\Pr_\pi(A_t=a\mid H_t=h_t)$, và theo (3.1) trọng số này bằng $\pi(a\mid s)$.

**Bước 2 (tầng phản hồi).** Cặp $(S_{t+1},R_{t+1})$ nhận hữu hạn giá trị. Theo kỳ vọng toàn phần với điều kiện nền $\{H_t=h_t,A_t=a\}$, vế trái của (4.4) bằng tổng có trọng số $\Pr_\pi(S_{t+1}=s',R_{t+1}=r\mid H_t=h_t,A_t=a)$, và theo quy tắc sinh quỹ đạo của Định nghĩa 03.7 trọng số này bằng $p(s',r\mid s,a)$. $\square$
:::

Ghép hai tầng, mỗi bộ $(a,s',r)$ mang trọng số

$$
\pi(a\mid s)\,p(s',r\mid s,a),
$$

đúng thừa số của (3.2) với $K=1$.

### 4.4 Tính Markov của phần tương lai và phương trình Bellman

Bước thứ ba là bỏ lịch sử khỏi kỳ vọng của phần còn lại. Ở robot, câu hỏi là kỳ vọng của $G_1$ khi biết $H_1=(\mathrm L,\mathrm{cho},1,\mathrm L)$ có bằng $v_\pi(\mathrm L)$ hay không. Một cách trực quan, câu trả lời là có: từ thời điểm $1$, robot ở pin thấp và theo cùng chính sách, nên tương lai bắt đầu lại từ $\mathrm L$.

::: lemma Bổ đề 03.20 (Tính Markov của phần tương lai)
**Giả thiết.** MDP hữu hạn (Định nghĩa 03.7) với quy ước của Nhận xét 03.10; chính sách Markov dừng $\pi$; phân phối đầu bất kỳ; $\lvert R_k\rvert\le M$ và $0\le\gamma<1$. Lịch sử $h_t$ kết thúc ở $s\in\mathcal S$ có xác suất dương.

**Kết luận.**

(a) Nếu tác tử theo $\pi$ tại mọi thời điểm từ $t$ trở đi, thì với mọi $K\ge1$, phân phối có điều kiện của $K$ bộ $(A_{t+i},R_{t+i+1},S_{t+i+1})$, $0\le i<K$, khi biết $H_t=h_t$ trùng với phân phối của $K$ bộ $(A_i,R_{i+1},S_{i+1})$ đầu tiên của quá trình xuất phát tại $s$.

(b) Với cùng giả thiết như (a),

$$
\mathbb E_\pi[G_t\mid H_t=h_t]=v_\pi(s).
$$

(c) Nếu tác tử theo $\pi$ ở mọi thời điểm, thì với mọi $t$ có $\Pr_\pi(S_t=s)>0$,

$$
\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s).
$$

(d) Nếu tác tử theo $\pi$ từ thời điểm $t+1$ trở đi và $a\in\mathcal A(s)$ thỏa $\Pr(H_t=h_t,A_t=a)>0$, thì

$$
\mathbb E_\pi[G_t\mid H_t=h_t,A_t=a]=q_\pi(s,a);
$$

nếu tác tử theo $\pi$ ở mọi thời điểm và $\Pr_\pi(S_t=s,A_t=a)>0$, thì $\mathbb E_\pi[G_t\mid S_t=s,A_t=a]=q_\pi(s,a)$.

**Điều kiện áp dụng.** Cần tính Markov của trạng thái, tính dừng của $p$ và của $\pi$; chính sách chỉ cần được tuân theo từ thời điểm đang xét trở đi. Phần thưởng bị chặn và $\gamma<1$ dùng ở bước qua giới hạn.

**Phạm vi.** Với nhiệm vụ có kết thúc và $\gamma=1$, kết luận vẫn đúng khi lợi tức khả tích, nhưng bước qua giới hạn cần một lập luận khác.
:::

::: proof Chứng minh Bổ đề 03.20
**Bước 1 (đoạn hữu hạn, phần a).** Theo Mệnh đề 03.14, xác suất có điều kiện của $K$ bộ đã cho khi biết $H_t=h_t$ bằng tích (3.2), với các thừa số bắt đầu từ $s$ và bằng $0$ ngay khi một thừa số bằng $0$. Áp dụng Mệnh đề 03.14 cho quá trình xuất phát tại $s$, với $t=0$ và $h_0=(s)$, ta được cùng tích. Bước này dùng tính Markov (qua Định nghĩa 03.7 và (3.1) trong Mệnh đề 03.14) và tính dừng: cùng hàm $\pi$ và cùng hàm $p$ ở thời điểm $t+i$ và ở thời điểm $i$.

**Bước 2 (lợi tức cắt, phần b).** Đặt

$$
G_t^{[K]}=\sum_{j=0}^{K-1}\gamma^jR_{t+j+1}.
$$

Đây là một hàm của $K$ bộ tiếp theo, nên theo phần (a),

$$
\mathbb E_\pi\bigl[G_t^{[K]}\mid H_t=h_t\bigr]=\mathbb E_\pi\bigl[G_0^{[K]}\mid S_0=s\bigr].
$$

**Bước 3 (qua giới hạn).** Trên mọi quỹ đạo, phần bị cắt thỏa

$$
\begin{aligned}
\bigl\lvert G_t-G_t^{[K]}\bigr\rvert&=\Bigl\lvert\sum_{j\ge K}\gamma^jR_{t+j+1}\Bigr\rvert\\
&\le\frac{\gamma^KM}{1-\gamma}
\end{aligned}
$$

theo cùng lập luận của Mệnh đề 03.11; điều tương tự đúng cho $G_0$. Vì vậy

$$
\begin{aligned}
\bigl\lvert\mathbb E_\pi[G_t\mid H_t=h_t]-v_\pi(s)\bigr\rvert
&\le\bigl\lvert\mathbb E_\pi[G_t-G_t^{[K]}\mid H_t=h_t]\bigr\rvert\\
&\quad+\bigl\lvert\mathbb E_\pi[G_0^{[K]}-G_0\mid S_0=s]\bigr\rvert\\
&\le\frac{2\gamma^KM}{1-\gamma}.
\end{aligned}
$$

Dòng đầu cộng và trừ hai kỳ vọng bằng nhau của Bước 2 rồi dùng bất đẳng thức tam giác; dòng cuối dùng cận của phần bị cắt. Vế phải tiến tới $0$ khi $K\to\infty$ vì $\gamma<1$, còn vế trái không phụ thuộc $K$; vậy vế trái bằng $0$.

**Bước 4 (phần c).** Theo kỳ vọng toàn phần theo các lịch sử $h_t$ kết thúc ở $s$, $\mathbb E_\pi[G_t\mid S_t=s]$ là trung bình có trọng số của các $\mathbb E_\pi[G_t\mid H_t=h_t]$; mỗi số hạng bằng $v_\pi(s)$ theo phần (b), và các trọng số cộng lại bằng $1$.

**Bước 5 (phần d).** Khi biết $H_t=h_t$ và $A_t=a$, phản hồi $(R_{t+1},S_{t+1})$ có phân phối $p(\cdot,\cdot\mid s,a)$ (Định nghĩa 03.7), và từ thời điểm $t+1$ tác tử theo $\pi$. Lập luận của Bước 1, với thừa số đầu $\pi(a_t\mid s_t)$ thay bằng $1$, cho thấy phân phối có điều kiện của phần quỹ đạo sau đó trùng với phân phối trong quá trình ấn định $(s,a)$. Bước 2–3 khi đó cho $\mathbb E_\pi[G_t\mid H_t=h_t,A_t=a]=q_\pi(s,a)$, và lấy trung bình theo các lịch sử như ở Bước 4 cho phát biểu thứ hai. $\square$
:::

Bổ đề 03.20 nói rằng khi biết lịch sử kết thúc ở $s$, tương lai phân phối giống tương lai của một quá trình mới bắt đầu ở $s$. Bổ đề này chứng minh chặt lập luận quy tắc nhân đã phác sau Định nghĩa 02.14, với bước qua giới hạn của Bước 3. Với robot, kỳ vọng của $G_1$ khi biết $H_1=(\mathrm L,\mathrm{cho},1,\mathrm L)$ bằng $v_\pi(\mathrm L)$, đúng điều Ví dụ 03.12 đã giả định.

Định lý sau ghép Bổ đề 03.18, 03.19 và 03.20.

::: theorem Định lý 03.21 (Phương trình Bellman kỳ vọng cho $v_\pi$)
**Giả thiết.** MDP hữu hạn (Định nghĩa 03.7), tức trạng thái có tính Markov và hàm động lực không đổi theo thời gian; chính sách Markov dừng $\pi$ (Định nghĩa 03.13); phần thưởng bị chặn và $0\le\gamma<1$.

**Kết luận.** Với mọi $s\in\mathcal S$,

$$
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\bigl[r+\gamma\,v_\pi(s')\bigr],
\tag{4.5}
$$

với quy ước $v_\pi(s')=0$ khi $s'$ là trạng thái kết thúc.

**Điều kiện áp dụng.** Mọi trạng thái chưa kết thúc; tổng lấy trên hành động hợp lệ của $s$ và trên các phản hồi của hàm động lực.

**Phạm vi.** Định lý nói $v_\pi$ thỏa hệ (4.5). Sutton và Barto (2018, (3.14)) phát biểu cùng phương trình và cho phép cả nhiệm vụ có kết thúc với $\gamma=1$ khi lợi tức khả tích.
:::

::: proof Chứng minh Định lý 03.21
Cố định $s\in\mathcal S$ và xét quá trình xuất phát tại $s$, nên $H_0=(s)$ và $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$. Các lợi tức bị chặn bởi $M/(1-\gamma)$ (Mệnh đề 03.11), nên mọi kỳ vọng dưới đây tồn tại.

**Bước 1 (tách lợi tức).** Theo Bổ đề 03.18, $v_\pi(s)=\mathbb E_\pi[R_1+\gamma G_1\mid S_0=s]$.

**Bước 2 (tầng hành động).** Áp dụng (4.3) với $X=R_1+\gamma G_1$ và $h_0=(s)$.

**Bước 3 (tầng phản hồi).** Với mỗi $a$ có $\pi(a\mid s)>0$, áp dụng (4.4); trong nhóm $\{S_1=s',R_1=r\}$, $R_1=r$ đi ra ngoài kỳ vọng.

**Bước 4 (phần tương lai).** Lịch sử $H_1=(s,a,r,s')$ kết thúc ở $s'$, nên theo Bổ đề 03.20(b) tại thời điểm $1$, $\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]=v_\pi(s')$. Khi $s'$ là trạng thái kết thúc, $G_1=0$ và vế phải bằng $0$ theo quy ước.

**Bước 5 (ghép).** Bốn bước cho chuỗi đẳng thức

$$
\begin{aligned}
v_\pi(s)&=\mathbb E_\pi[R_1+\gamma G_1\mid S_0=s]\\
&=\sum_a\pi(a\mid s)\,\mathbb E_\pi[R_1+\gamma G_1\mid S_0=s,A_0=a]\\
&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma\,\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]\bigr]\\
&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma\,v_\pi(s')\bigr].
\end{aligned}
$$

Bốn đẳng thức lần lượt dùng Bước 1, Bước 2, Bước 3 và Bước 4.

Các số hạng với $\pi(a\mid s)=0$ hoặc $p(s',r\mid s,a)=0$ bằng $0$, nên tổng có thể lấy trên toàn bộ $\mathcal A(s)$, $\mathcal S^+$, $\mathcal R$ như trong (4.5). $\square$
:::

Phương trình (4.5), phương trình Bellman kỳ vọng (Bellman expectation equation), đọc bằng lời: giá trị của một trạng thái bằng trung bình, theo xác suất chọn hành động và xác suất phản hồi, của phần thưởng một bước cộng giá trị đã chiết khấu của trạng thái kế tiếp. Vế phải chỉ chứa các giá trị $v_\pi(s')$, nên với $n$ trạng thái, (4.5) là $n$ phương trình cho $n$ ẩn.

Áp dụng (4.5) tại $s=\mathrm L$ cho robot, các số hạng của Tìm biến mất vì $\pi(\mathrm{tim}\mid\mathrm L)=0$; Chờ chỉ có phản hồi $(\mathrm L,1)$ và Sạc chỉ có $(\mathrm H,0)$, nên (4.5) trở thành phương trình (4.1) của Ví dụ 03.12.

![Hai sơ đồ cập nhật. Vòng tròn rỗng là trạng thái, chấm tròn đặc là cặp trạng thái–hành động. Bên trái, sơ đồ của v_π: gốc s, ba cạnh có nhãn π(a | s) xuống ba chấm đặc a, từ mỗi chấm đặc hai cạnh có nhãn p, r xuống hai vòng tròn s'. Bên phải, sơ đồ của q_π: gốc là chấm đặc (s, a), hai cạnh có nhãn p(s', r | s, a), r xuống hai vòng tròn s', từ mỗi s' hai cạnh có nhãn π(a' | s') xuống hai chấm đặc a'. Chú thích: giá trị ở gốc bằng trung bình có trọng số của r + γ nhân giá trị ở tầng dưới.](img/lec-03/backup-diagrams.svg)

Hình trên là sơ đồ cập nhật (backup diagram) theo cách vẽ của Sutton và Barto (2018, tr. 59, 61). Ở sơ đồ bên trái, tầng cạnh trên mang trọng số $\pi(a\mid s)$ của Bước 2, tầng cạnh dưới mang $p(s',r\mid s,a)$ của Bước 3, mỗi lá góp $r+\gamma v_\pi(s')$ theo Bước 4. Sơ đồ bên phải đảo thứ tự hai tầng: tầng trên mang $p(s',r\mid s,a)$, tầng dưới mang $\pi(a'\mid s')$.

Các giả thiết của Định lý 03.21 có vai trò riêng, và mỗi giả thiết bị bỏ đều làm hỏng một bước của chứng minh.

- Bỏ tính Markov: ở Ví dụ 03.4, phần thưởng của bước sau phụ thuộc phòng, và lịch sử tiết lộ phòng. Kỳ vọng của phần tương lai sau lịch sử $h$ khác sau lịch sử $h'$, dù cả hai kết thúc ở $\mathrm L$, nên không thể cùng bằng một số $v_\pi(\mathrm L)$; Bổ đề 03.20(b) sai.
- Bỏ tính dừng của chính sách: nếu robot Chờ ở bước chẵn và Sạc ở bước lẻ khi ở pin thấp, lợi tức kỳ vọng từ $\mathrm L$ phụ thuộc thời điểm; Bước 1 của Bổ đề 03.20 sai.
- Bỏ tính dừng của hàm động lực: với robot có pin lão hóa của Nhận xét 03.5, xác suất phản hồi đổi theo $t$, nên tương lai từ $\mathrm L$ ở thời điểm $t$ khác tương lai của quá trình xuất phát tại $\mathrm L$; Bước 1 của Bổ đề 03.20 sai.
- Bỏ $\gamma<1$ ở nhiệm vụ tiếp diễn: với $\gamma=1$, robot luôn Chờ có lợi tức vô hạn, nên $v_\pi(\mathrm L)$ không phải số thực và (4.5) không có nghĩa.

Ở Ví dụ 03.4 với $\gamma=1/2$, hai kỳ vọng của phần tương lai sau $h$ và sau $h'$ lần lượt là $\tfrac23$ và $\tfrac43$, còn $v_\pi(\mathrm L)=1$ (kỳ vọng của $G_0$ khi $S_0=\mathrm L$ trên quá trình thật, phòng đầu chọn đều). Ví dụ này làm hỏng lập luận nhưng không bác bỏ kết luận. Vì chỉ có một trạng thái và phân phối phòng như nhau ở mọi bước, phương trình lập từ bảng trung bình $p(\mathrm L,1\mid\mathrm L,\mathrm{cho})=p(\mathrm L,0\mid\mathrm L,\mathrm{cho})=\tfrac12$ vẫn đúng: $v=\tfrac1{2(1-\gamma)}$ thỏa $v=\tfrac12+\gamma v$.

**Trong thực hành.** Vế phải của (4.5) là kỳ vọng của $R_{t+1}+\gamma\,v_\pi(S_{t+1})$ khi biết $S_t=s$, và một bước tương tác thật cho một mẫu của đại lượng này. Phương pháp sai phân thời gian (temporal difference, TD) một bước, ký hiệu TD(0), của Bài 05 cập nhật bảng ước lượng $V$ với bước học $\alpha\in(0,1]$ theo

$$
V(S_t)\leftarrow V(S_t)+\alpha\bigl[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\bigr],
$$

trong đó $R_{t+1}+\gamma V(S_{t+1})$ là mục tiêu bootstrap (bootstrap target). Với $V$ giữ cố định và tác tử theo $\pi$, kỳ vọng của mục tiêu này khi biết $S_t=s$ là vế phải của (4.5) với $V$ ở vị trí của $v_\pi$; khi $V=v_\pi$, kỳ vọng đó bằng $v_\pi(s)$. Khi trạng thái là một ô rời rạc hóa (discretization) như ở CartPole, giả thiết Markov của Định lý 03.21 có thể sai.

### 4.5 Quan hệ giữa giá trị trạng thái và giá trị hành động

Với giá trị hành động, bước đầu đã bị ấn định, nên chỉ còn tầng phản hồi. Ví dụ sau viết $q_\pi(\mathrm L,\mathrm{tim})$ theo lập luận của Ví dụ 03.12.

::: example Ví dụ 03.13 (Hai nhánh của L–Tìm)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$. Tìm từ $\mathrm L$ cho $(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi phản hồi xác suất $1/2$.

**Nhóm theo phản hồi.** Hành động đầu đã là Tìm, nên không có trọng số chính sách ở bước đầu. Mỗi phản hồi đóng góp phần thưởng của nó cộng giá trị chiết khấu của trạng thái kế tiếp:

$$
\begin{aligned}
q_\pi(\mathrm L,\mathrm{tim})&=\tfrac12\bigl[2+\tfrac12\,v_\pi(\mathrm L)\bigr]\\
&\quad+\tfrac12\bigl[-3+\tfrac12\,v_\pi(\mathrm H)\bigr].
\end{aligned}
$$

**Dạng rút gọn.** Gom phần thưởng và gom giá trị:

$$
\begin{aligned}
q_\pi(\mathrm L,\mathrm{tim})&=\underbrace{\bigl(\tfrac12\cdot2+\tfrac12\cdot(-3)\bigr)}_{r(\mathrm L,\mathrm{tim})=-1/2}\\
&\quad+\tfrac12\bigl(\tfrac12\,v_\pi(\mathrm L)+\tfrac12\,v_\pi(\mathrm H)\bigr).
\end{aligned}
$$

**Đọc phương trình.** Hệ số $\tfrac12$ ngoài các ngoặc là xác suất phản hồi, không phải xác suất chính sách. Chính sách có mặt qua $v_\pi(\mathrm L)$ và $v_\pi(\mathrm H)$, vì từ bước sau robot theo $\pi$.

**Kiểm tra lại.** Khai triển hai dạng đều cho $q_\pi(\mathrm L,\mathrm{tim})=-\tfrac12+\tfrac14v_\pi(\mathrm L)+\tfrac14v_\pi(\mathrm H)$.
:::

Mệnh đề sau là dạng tổng quát của Ví dụ 03.13.

::: proposition Mệnh đề 03.22 (Giá trị hành động theo giá trị trạng thái)
**Giả thiết.** Như Định lý 03.21; $s\in\mathcal S$, $a\in\mathcal A(s)$, kể cả khi $\pi(a\mid s)=0$.

**Kết luận.**

$$
\begin{aligned}
q_\pi(s,a)&=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\bigl[r+\gamma\,v_\pi(s')\bigr]\\
&=r(s,a)+\gamma\sum_{s'\in\mathcal S^+}p(s'\mid s,a)\,v_\pi(s').
\end{aligned}
\tag{4.6}
$$

**Điều kiện áp dụng.** Mọi cặp hợp lệ $(s,a)$.

**Phạm vi.** Dạng thứ hai chỉ cần $p(s'\mid s,a)$ và $r(s,a)$, không cần phân phối đầy đủ của phần thưởng.
:::

::: proof Chứng minh Mệnh đề 03.22
**Bước 1 (đẳng thức thứ nhất).** Trong quá trình ấn định $(s,a)$ của Định nghĩa 03.16, Bổ đề 03.18 cho $G_0=R_1+\gamma G_1$, và kỳ vọng toàn phần theo $(S_1,R_1)$ cho trọng số $p(s',r\mid s,a)$. Quá trình này theo $\pi$ từ thời điểm $1$, nên Bổ đề 03.20(b) áp dụng tại thời điểm $1$ và cho $\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]=v_\pi(s')$ khi $s'\in\mathcal S$. Khi $s'$ là trạng thái kết thúc, $G_1=0=v_\pi(s')$ (Nhận xét 03.10).

**Bước 2 (dạng rút gọn).** Tách tổng thành hai phần:

$$
\begin{aligned}
&\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr]\\
&\quad=\sum_{s',r}r\,p(s',r\mid s,a)+\gamma\sum_{s'}v_\pi(s')\sum_rp(s',r\mid s,a)\\
&\quad=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s').
\end{aligned}
$$

Dòng thứ hai dùng (1.6) và (1.5). $\square$
:::

Công thức (4.6) đọc như sau: giá trị của hành động $a$ tại $s$ bằng thưởng kỳ vọng một bước của $a$ cộng giá trị kỳ vọng đã chiết khấu của trạng thái kế tiếp. So với (4.5), (4.6) thiếu tầng tổng theo $\pi(a\mid s)$, vì hành động đầu đã cố định. Chiều ngược lại gom các giá trị hành động thành giá trị trạng thái.

::: proposition Mệnh đề 03.23 (Giá trị trạng thái theo giá trị hành động)
**Giả thiết.** Như Định lý 03.21; $s\in\mathcal S$.

**Kết luận.**

$$
v_\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,q_\pi(s,a).
\tag{4.7}
$$

**Điều kiện áp dụng.** Mọi trạng thái chưa kết thúc.

**Phạm vi.** Các hành động có $\pi(a\mid s)=0$ không đóng góp vào $v_\pi(s)$, dù $q_\pi(s,a)$ của chúng vẫn xác định.
:::

::: proof Chứng minh Mệnh đề 03.23
**Bước 1 (tầng hành động).** Áp dụng (4.3) với $X=G_0$ cho quá trình xuất phát tại $s$: $v_\pi(s)=\sum_a\pi(a\mid s)\,\mathbb E_\pi[G_0\mid S_0=s,A_0=a]$, tổng trên các $a$ có $\pi(a\mid s)>0$.

**Bước 2 (giá trị hành động).** Với các $a$ đó, Bổ đề 03.20(d) tại $t=0$ cho kỳ vọng có điều kiện bằng $q_\pi(s,a)$.

**Bước 3 (hành động không được chọn).** Các $a$ có $\pi(a\mid s)=0$ góp số hạng $0\cdot q_\pi(s,a)=0$, vì $q_\pi(s,a)$ hữu hạn, nên tổng có thể lấy trên toàn bộ $\mathcal A(s)$. $\square$
:::

Công thức (4.7) nói giá trị của trạng thái là trung bình các giá trị hành động, với trọng số là xác suất chính sách chọn từng hành động. Thế (4.6) vào (4.7) ta lại được (4.5). Thế theo chiều ngược lại, (4.7) tại trạng thái kế tiếp vào (4.6), ta được một phương trình chỉ chứa $q_\pi$.

::: corollary Hệ quả 03.24 (Phương trình Bellman kỳ vọng cho $q_\pi$)
**Giả thiết.** Như Định lý 03.21.

**Kết luận.** Với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$,

$$
q_\pi(s,a)=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\Bigl[r+\gamma\sum_{a'\in\mathcal A(s')}\pi(a'\mid s')\,q_\pi(s',a')\Bigr],
\tag{4.8}
$$

với quy ước tổng trong ngoặc bằng $0$ khi $s'$ là trạng thái kết thúc.

**Điều kiện áp dụng.** Mọi cặp hợp lệ, kể cả cặp có $\pi(a\mid s)=0$.

**Phạm vi.** Như (4.5), phương trình là trung bình theo $\pi$.
:::

::: proof Chứng minh Hệ quả 03.24
Với $s'$ chưa kết thúc, Mệnh đề 03.23 tại $s'$ cho $v_\pi(s')=\sum_{a'}\pi(a'\mid s')\,q_\pi(s',a')$. Với $s'$ kết thúc, $v_\pi(s')=0$, bằng tổng rỗng theo quy ước. Thay vào đẳng thức thứ nhất của (4.6) ta được (4.8). $\square$
:::

Trong (4.8), $a$ là hành động tại thời điểm $t$, còn $a'$ là hành động chính sách chọn tại $t+1$ ở $s'$, nên trọng số là $\pi(a'\mid s')$. Tổng ngoài mang xác suất của môi trường, tổng trong mang xác suất của chính sách, theo thứ tự ngược với (4.5), như sơ đồ bên phải của hình sơ đồ cập nhật. Ở robot, (4.8) có năm phương trình, (4.5) chỉ có hai. Phương trình (4.8) là bài tập 3.17 của Sutton và Barto (2018, tr. 61).

**Trong thực hành.** Thuật toán Sarsa của Bài 06 học bảng $Q$ cho chính sách đang dùng, với mục tiêu bootstrap $R_{t+1}+\gamma\,Q(S_{t+1},A_{t+1})$, trong đó $A_{t+1}$ là hành động thật sự được chọn ở bước sau. Đây là một mẫu của ngoặc vuông trong (4.8). Khi không biết mô hình, $q_\pi$ có lợi thế theo (4.6): so sánh hành động bằng $v_\pi$ cần $p$, còn $q_\pi$ cho trực tiếp con số của từng hành động.

::: remark Nhận xét 03.25 (Chỗ dùng tính Markov; trung bình khác cực đại)
- Bổ đề 03.18 không dùng tính Markov hay tính dừng; đó là đẳng thức trên từng quỹ đạo.
- Bổ đề 03.19 dùng tính Markov một bước qua quy tắc sinh của Định nghĩa 03.7 tại một thời điểm $t$, không dùng tính dừng; (4.4) vẫn đúng nếu $p$ là hàm động lực riêng của thời điểm $t$.
- Bổ đề 03.20 dùng tính Markov cho toàn bộ phần tương lai và tính dừng của $\pi$ và $p$ để bỏ lịch sử khỏi kỳ vọng của $G_t$; mọi kết quả sau nó thừa hưởng hai giả thiết này.
- Mọi phương trình của mục là trung bình theo $\pi$. Nhầm (4.5) với phương trình có $\max_a$ là nhầm bài toán dự đoán, tức đánh giá một chính sách cho trước, với bài toán điều khiển, tức tìm chính sách tốt nhất.
:::

::: exercise Bài tập 03.6
**Dữ kiện.** Robot của Ví dụ 03.1: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $1/2$. Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm. $\gamma=1/2$. Viết $v_{\mathrm H}=v_\pi(\mathrm H)$, $v_{\mathrm L}=v_\pi(\mathrm L)$.

**Yêu cầu.** Từ Định lý 03.21, chứng minh $v_{\mathrm H}=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$, chỉ rõ mỗi hệ số đến từ $\pi$, từ $p$ hay từ $\gamma$.
:::

::: hint
Ở $\mathrm H$, tổng theo hành động chỉ còn một số hạng; tổng theo phản hồi có hai số hạng.
:::

::: solution
Áp dụng (4.5) tại $s=\mathrm H$. Tổng theo $a$ chỉ còn $a=\mathrm{tim}$ với $\pi(\mathrm{tim}\mid\mathrm H)=1$, vì $\pi(\mathrm{cho}\mid\mathrm H)=0$. Cặp $(\mathrm H,\mathrm{tim})$ có hai phản hồi $(\mathrm H,2)$ và $(\mathrm L,2)$, mỗi phản hồi $p=1/2$. Vậy

$$
\begin{aligned}
v_{\mathrm H}&=1\cdot\Bigl(\tfrac12\bigl[2+\tfrac12v_{\mathrm H}\bigr]+\tfrac12\bigl[2+\tfrac12v_{\mathrm L}\bigr]\Bigr)\\
&=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}.
\end{aligned}
$$

Dòng đầu là (4.5) tại $\mathrm H$; dòng thứ hai khai triển các ngoặc.

Hệ số $1$ ngoài cùng là $\pi(\mathrm{tim}\mid\mathrm H)$; hai hệ số $\tfrac12$ ngoài ngoặc vuông là $p(\mathrm H,2\mid\mathrm H,\mathrm{tim})$ và $p(\mathrm L,2\mid\mathrm H,\mathrm{tim})$; hệ số $\tfrac12$ trước $v_{\mathrm H}$, $v_{\mathrm L}$ trong ngoặc là $\gamma$. Mỗi hệ số $\tfrac14$ là tích $p\cdot\gamma$.

**Kiểm tra lại.** Số hạng tự do $2$ là $r(\mathrm H,\mathrm{tim})$ theo Bài tập 03.2, đúng dạng thứ hai của (4.6) nhân với $\pi(\mathrm{tim}\mid\mathrm H)=1$.
:::

::: exercise Bài tập 03.7
**Dữ kiện.** MDP hữu hạn, chính sách Markov dừng $\pi$, phần thưởng bị chặn, $0\le\gamma<1$. Ở Ví dụ 03.4, trạng thái chỉ ghi mức pin, và hai lịch sử $(\mathrm L,\mathrm{cho},1,\mathrm L)$, $(\mathrm L,\mathrm{cho},0,\mathrm L)$ cho phần thưởng bước sau chắc chắn bằng $0$ và $1$.

**Yêu cầu.** Trong chuỗi lập luận dẫn tới Hệ quả 03.24 (Bổ đề 03.20, Mệnh đề 03.22, 03.23), chỉ ra (a) bước dùng tính Markov của trạng thái, và điều gì sai ở bước đó nếu trạng thái thiếu thông tin như ở Ví dụ 03.4; (b) bước dùng tính dừng của chính sách, và điều gì sai ở bước đó nếu robot đổi quy tắc chọn theo thời điểm chẵn, lẻ.
:::

::: hint
Hệ quả 03.24 thế Mệnh đề 03.23 vào Mệnh đề 03.22; Mệnh đề 03.22 dựa trên Bổ đề 03.20(b), và chứng minh của bổ đề này gọi Mệnh đề 03.14 cho hai quá trình khác nhau.
:::

::: solution
**(a)** Tính Markov của trạng thái được dùng ở Bước 1 của chứng minh Bổ đề 03.20 (qua Mệnh đề 03.14), rồi đi vào Bước 1 của Mệnh đề 03.22, nơi $\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]$ được thay bằng $v_\pi(s')$. Ở Ví dụ 03.4, hai lịch sử kết thúc ở $\mathrm L$ cho hai phân phối phần thưởng khác nhau ở bước sau, nên hai kỳ vọng của phần tương lai không thể cùng bằng $v_\pi(\mathrm L)$.

Tính Markov một bước nằm trong trọng số $p(s',r\mid s,a)$ của tầng phản hồi (Bước 1 của Mệnh đề 03.22, như Bổ đề 03.19(b)); trọng số này do quy tắc sinh của Định nghĩa 03.7 cho, và quy tắc đó cũng là nguồn của các thừa số $p$ trong (3.2). Ở Ví dụ 03.4 quy tắc này hỏng, nên không có hàm $p$ chung không phụ thuộc lịch sử.

**(b)** Tính dừng của chính sách cũng được dùng ở Bước 1 của Bổ đề 03.20: tích (3.2) tại thời điểm $t$ trùng tích của quá trình xuất phát tại $s$ vì cùng hàm $\pi$ dùng ở thời điểm $t+i$ và $i$. Nếu robot Chờ ở bước chẵn và Sạc ở bước lẻ, tương lai từ $\mathrm L$ ở thời điểm lẻ khác tương lai từ $\mathrm L$ ở thời điểm $0$, nên đẳng thức này sai.

**Kiểm tra lại.** Mệnh đề 03.23 chỉ dùng (4.3) tại $t=0$ với $h_0=(s)$, nơi không có lịch sử để bỏ, và Bổ đề 03.20(d); cả hai giả thiết đi vào Mệnh đề 03.23 qua Bổ đề 03.20.
:::

Từ hệ thức đệ quy, hai tầng kỳ vọng và tính Markov của phần tương lai (Bổ đề 03.18–03.20), giá trị của một chính sách thỏa phương trình Bellman kỳ vọng (4.5) của Định lý 03.21, và $q_\pi$, $v_\pi$ biểu diễn được qua nhau theo (4.6), (4.7) của Mệnh đề 03.22, 03.23. Tuy nhiên, Định lý 03.21 chỉ nói $v_\pi$ là một nghiệm của hệ; chưa biết hệ có nghiệm khác hay không.

<!-- note-topic-id: lec-03-part-06 -->
## 5. Đánh giá chính sách bằng hệ tuyến tính

Robot có hai phương trình Bellman với hai ẩn $v_\pi(\mathrm H)$, $v_\pi(\mathrm L)$ ở cả hai vế. Bài toán tính $v_\pi$ khi biết $p$, $\pi$ và $\gamma$ gọi là đánh giá chính sách (policy evaluation); đó là bài toán dự đoán của Nhận xét 02.17, và là bài toán có mô hình (model-based) vì $p$ được dùng trực tiếp. Với robot, hệ hai ẩn giải được bằng phép thế; với $n$ trạng thái, chúng ta viết hệ thành một phương trình ma trận để chứng minh hệ có đúng một nghiệm và lập thuật toán giải.

### 5.1 Hệ Bellman của robot

::: example Ví dụ 03.14 (Hệ Bellman của robot và nghiệm)
**Dữ kiện.** Robot của Ví dụ 03.1; chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$); $\gamma=1/2$. Tìm từ $\mathrm H$: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$. Chờ từ $\mathrm L$: $(\mathrm L,1)$. Sạc từ $\mathrm L$: $(\mathrm H,0)$. Viết $v_{\mathrm H}=v_\pi(\mathrm H)$, $v_{\mathrm L}=v_\pi(\mathrm L)$.

**Kiểm tra giả thiết.** Mức pin là trạng thái Markov và hàm động lực không đổi theo thời gian; chính sách Markov dừng; $\lvert R\rvert\le3$ và $\gamma<1$. Định lý 03.21 áp dụng được.

**Lập hệ.** Phương trình của Bài tập 03.6 tại $\mathrm H$ và phương trình (4.1) tại $\mathrm L$, sau khi khai triển, là

$$
\begin{aligned}
v_{\mathrm H}&=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L},\\
v_{\mathrm L}&=\tfrac12+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}.
\end{aligned}
\tag{5.1}
$$

**Giải.** Hai phương trình có cùng phần $\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$; trừ vế theo vế được $v_{\mathrm H}-v_{\mathrm L}=2-\tfrac12=\tfrac32$. Thế $v_{\mathrm H}=v_{\mathrm L}+\tfrac32$ vào phương trình thứ hai:

$$
\begin{aligned}
v_{\mathrm L}&=\tfrac12+\tfrac14\bigl(v_{\mathrm L}+\tfrac32\bigr)+\tfrac14v_{\mathrm L}\\
&=\tfrac78+\tfrac12v_{\mathrm L}.
\end{aligned}
$$

Dòng thứ hai gom các số hạng, nên $v_{\mathrm L}=\tfrac74$ và $v_{\mathrm H}=\tfrac74+\tfrac32=\tfrac{13}{4}$.

**Kiểm tra lại.** Thay vào (5.1): $2+\tfrac14\bigl(\tfrac{13}4+\tfrac74\bigr)=2+\tfrac54=\tfrac{13}4$ và $\tfrac12+\tfrac54=\tfrac74$.

**Diễn giải.** Dưới chính sách chia đều tại pin thấp, robot ở pin cao có lợi tức kỳ vọng $13/4$, ở pin thấp $7/4$. Hiệu $v_{\mathrm H}-v_{\mathrm L}=3/2$ bằng hiệu của thưởng kỳ vọng một bước dưới chính sách ở hai trạng thái, $2-\tfrac12$, vì từ cả hai trạng thái robot chuyển tới $\mathrm H$ và $\mathrm L$ với cùng xác suất.
:::

Kỳ vọng hai bước của Ví dụ 03.10 và Bài tập 03.4, $21/8$ từ pin cao và $9/8$ từ pin thấp, nhỏ hơn giá trị thật $26/8$ và $14/8$ vì ở robot, phần đuôi bị cắt có kỳ vọng dương.

Giá trị hành động cho một phép kiểm tra độc lập: theo Mệnh đề 03.23, trung bình của các $q_\pi$ theo chính sách phải bằng $v_\pi$.

::: example Ví dụ 03.15 (Kiểm tra bằng giá trị hành động)
**Dữ kiện.** Robot của Ví dụ 03.1 với chính sách chia đều tại pin thấp, $\gamma=1/2$, $v_\pi(\mathrm H)=\tfrac{13}4$, $v_\pi(\mathrm L)=\tfrac74$ (Ví dụ 03.14). Tìm từ $\mathrm L$: $(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi phản hồi $1/2$, nên $r(\mathrm L,\mathrm{tim})=-\tfrac12$; Chờ từ $\mathrm L$: $(\mathrm L,1)$; Sạc từ $\mathrm L$: $(\mathrm H,0)$.

**Tính.** Theo dạng thứ hai của (4.6):

$$
\begin{aligned}
q_\pi(\mathrm L,\mathrm{tim})&=-\tfrac12+\tfrac12\bigl(\tfrac12\cdot\tfrac74+\tfrac12\cdot\tfrac{13}4\bigr)\\
&=-\tfrac12+\tfrac54=\tfrac34,\\
q_\pi(\mathrm L,\mathrm{cho})&=1+\tfrac12\cdot\tfrac74=\tfrac{15}8,\\
q_\pi(\mathrm L,\mathrm{sac})&=0+\tfrac12\cdot\tfrac{13}4=\tfrac{13}8.
\end{aligned}
$$

**Kiểm tra lại.** Theo (4.7) tại $\mathrm L$: $0\cdot\tfrac34+\tfrac12\cdot\tfrac{15}8+\tfrac12\cdot\tfrac{13}8=\tfrac{28}{16}=\tfrac74=v_\pi(\mathrm L)$. Dạng thứ nhất của (4.6) cho $q_\pi(\mathrm L,\mathrm{tim})=\tfrac12\cdot\tfrac{23}8+\tfrac12\cdot\bigl(-\tfrac{11}8\bigr)=\tfrac34$, trùng kết quả.

**Diễn giải.** Tìm có giá trị thấp nhất vì rủi ro cứu hộ. Sạc kém Chờ $\tfrac14$, không phải $1$ như phần thưởng một bước, vì Sạc đưa robot về trạng thái có giá trị cao hơn.
:::

### 5.2 Chuỗi Markov và quá trình phần thưởng Markov cảm sinh

Trong (5.1), chính sách đã biến mất khỏi hình thức của hệ: mỗi phương trình chỉ còn một số hạng tự do và hai hệ số trước $v_{\mathrm H}$, $v_{\mathrm L}$. Khi chính sách cố định, ta có thể gộp trước tầng hành động và tầng phản hồi thành xác suất chuyển giữa các trạng thái cùng thưởng kỳ vọng của mỗi trạng thái.

::: example Ví dụ 03.16 (Gộp các nhánh của robot dưới chính sách)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$. Tìm từ $\mathrm H$: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$. Chờ từ $\mathrm L$: $(\mathrm L,1)$. Sạc từ $\mathrm L$: $(\mathrm H,0)$.

**Gộp.** Tại $\mathrm H$, chính sách chọn Tìm với xác suất $1$: xác suất chuyển $\mathrm H\to\mathrm H$ và $\mathrm H\to\mathrm L$ đều là $1/2$, thưởng kỳ vọng $2$. Tại $\mathrm L$, Chờ (xác suất $1/2$) về $\mathrm L$ với phần thưởng $1$ và Sạc (xác suất $1/2$) về $\mathrm H$ với phần thưởng $0$: xác suất chuyển $\mathrm L\to\mathrm L$ và $\mathrm L\to\mathrm H$ đều là $1/2$, thưởng kỳ vọng $\tfrac12\cdot1+\tfrac12\cdot0=\tfrac12$.

**Dạng ma trận.** Xếp trạng thái theo thứ tự $\mathrm H$, $\mathrm L$; ma trận chuyển $P_\pi$ có hàng $s$ là các xác suất chuyển từ $s$, véc-tơ $r_\pi$ ghi thưởng kỳ vọng của từng trạng thái:

$$
\begin{aligned}
P_\pi&=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\\
r_\pi&=\begin{pmatrix}2\\1/2\end{pmatrix}.
\end{aligned}
$$

**Kiểm tra lại.** Hàng thứ nhất của $v=r_\pi+\gamma P_\pi v$ là $v_{\mathrm H}=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$, hàng thứ hai là $v_{\mathrm L}=\tfrac12+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$, đúng (5.1). Mỗi hàng của $P_\pi$ có tổng $1$.
:::

Thưởng kỳ vọng $1/2$ ở hàng $\mathrm L$ là trung bình theo chính sách; mỗi lần ở pin thấp, robot nhận $1$ hoặc $0$. Khi đổi chính sách, chúng ta phải tính lại $P_\pi$ và $r_\pi$.

::: definition Định nghĩa 03.26 (Chuỗi Markov và quá trình phần thưởng Markov cảm sinh bởi chính sách)
Cho MDP hữu hạn với tập trạng thái chưa kết thúc $\mathcal S=\{s_1,\dots,s_n\}$ và chính sách Markov dừng $\pi$. Ma trận chuyển $P_\pi\in\mathbb R^{n\times n}$ và véc-tơ thưởng kỳ vọng $r_\pi\in\mathbb R^n$ dưới $\pi$ là, với $s,s'\in\mathcal S$,

$$
\begin{aligned}
(P_\pi)_{ss'}&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,p(s'\mid s,a),\\
r_\pi(s)&=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,r(s,a).
\end{aligned}
\tag{5.2}
$$

Chuỗi Markov (Markov chain) cảm sinh (induced) bởi $\pi$ là dãy trạng thái $S_0,S_1,\dots$ trên $\mathcal S^+$ khi tác tử theo $\pi$, với trạng thái kết thúc hấp thụ; $P_\pi$ là khối của ma trận chuyển ứng với $\mathcal S$, nên phần xác suất còn thiếu ở mỗi hàng của $P_\pi$ là xác suất đi tới trạng thái kết thúc. Quá trình phần thưởng Markov (Markov reward process, MRP) cảm sinh bởi $\pi$ là bộ $(\mathcal S,P_\pi,r_\pi,\gamma)$.
:::

Phần tử $(P_\pi)_{ss'}$ là xác suất chuyển sau khi đã gộp hành động, $r_\pi(s)$ là thưởng kỳ vọng một bước tại $s$. Mỗi hàng của $P_\pi$ có tổng không quá $1$, bằng $1$ khi không có trạng thái kết thúc như ở robot; theo Mệnh đề 03.14, dãy trạng thái dưới $\pi$ vẫn có tính Markov.

Khác bộ $\mathcal M$ của Định nghĩa 03.7, bộ MRP ghi kèm $\gamma$, vì nó được lập ra để tính giá trị của một chính sách đã cố định và $\gamma$ có mặt trong mọi hệ số của hệ, như $\tfrac14=\gamma\cdot\tfrac12$ trong (5.1).

### 5.3 Dạng ma trận và nghiệm duy nhất

Với $P_\pi$ và $r_\pi$, phương trình Bellman của mọi trạng thái gom được thành một phương trình véc-tơ.

::: proposition Mệnh đề 03.27 (Phương trình Bellman dạng ma trận)
**Giả thiết.** Như Định lý 03.21; $\mathcal S=\{s_1,\dots,s_n\}$; $v\in\mathbb R^n$ là véc-tơ cột với $v_i=v_\pi(s_i)$; $P_\pi$, $r_\pi$ theo (5.2).

**Kết luận.**

$$
\begin{aligned}
&v=r_\pi+\gamma P_\pi v\\
\Longleftrightarrow\quad&(I-\gamma P_\pi)\,v=r_\pi .
\end{aligned}
\tag{5.3}
$$

**Điều kiện áp dụng.** Tập trạng thái hữu hạn, để $P_\pi$ là ma trận hữu hạn.

**Phạm vi.** Mệnh đề nói $v_\pi$ là một nghiệm của (5.3).
:::

::: proof Chứng minh Mệnh đề 03.27
**Bước 1 (khai triển vế phải của (4.5)).** Theo Mệnh đề 03.22 và 03.23,

$$
\begin{aligned}
v_\pi(s)&=\sum_a\pi(a\mid s)\Bigl[r(s,a)+\gamma\sum_{s'\in\mathcal S^+}p(s'\mid s,a)\,v_\pi(s')\Bigr]\\
&=\sum_a\pi(a\mid s)\,r(s,a)\\
&\quad+\gamma\sum_{s'\in\mathcal S}\Bigl(\sum_a\pi(a\mid s)\,p(s'\mid s,a)\Bigr)v_\pi(s')\\
&=r_\pi(s)+\gamma\sum_{s'\in\mathcal S}(P_\pi)_{ss'}\,v_\pi(s').
\end{aligned}
$$

Đẳng thức thứ hai đổi thứ tự hai tổng hữu hạn và bỏ các trạng thái kết thúc, nơi $v_\pi=0$; đẳng thức thứ ba là định nghĩa (5.2).

**Bước 2 (viết thành véc-tơ).** Tổng $\sum_{s'}(P_\pi)_{ss'}v_\pi(s')$ là thành phần thứ $s$ của tích $P_\pi v$, nên $n$ đẳng thức của Bước 1 là $v=r_\pi+\gamma P_\pi v$, tức $(I-\gamma P_\pi)v=r_\pi$. $\square$
:::

Phương trình (5.3) gom $n$ phương trình (4.5) thành một hệ tuyến tính $n$ ẩn với ma trận hệ số $I-\gamma P_\pi$ và vế phải $r_\pi$; với robot, đó là hệ (5.1).

Nếu hệ (5.3) có nghiệm khác $v_\pi$, giải hệ chưa chắc cho ra giá trị của chính sách. Định lý sau loại trừ khả năng đó khi $\gamma<1$, bằng chuẩn cực đại (max norm) $\lVert x\rVert_\infty=\max_i\lvert x_i\rvert$.

::: theorem Định lý 03.28 (Nghiệm duy nhất của hệ đánh giá chính sách)
**Giả thiết.** MDP hữu hạn với $n$ trạng thái chưa kết thúc; chính sách Markov dừng $\pi$; phần thưởng bị chặn; $0\le\gamma<1$; $P_\pi$, $r_\pi$ theo (5.2).

**Kết luận.**

(a) Ma trận $I-\gamma P_\pi$ khả nghịch.

(b) Hệ (5.3) có nghiệm duy nhất, và nghiệm đó là giá trị của chính sách:

$$
v_\pi=(I-\gamma P_\pi)^{-1}r_\pi .
\tag{5.4}
$$

(c) Giá trị có khai triển chuỗi Neumann (Neumann series)

$$
v_\pi=\sum_{k=0}^{\infty}\gamma^k(P_\pi)^kr_\pi,
\tag{5.5}
$$

và tổng riêng $K$ số hạng đầu sai khác $v_\pi$ không quá $\gamma^K\lVert v_\pi\rVert_\infty$ theo chuẩn cực đại.

**Điều kiện áp dụng.** Tập trạng thái hữu hạn và $\gamma<1$.

**Phạm vi.** Định lý không áp dụng cho $\gamma=1$ mà không có thêm điều kiện; Sutton và Barto (2018, §4.1, tr. 74) nêu rằng nghiệm tồn tại và duy nhất khi $\gamma<1$ hoặc khi dưới $\pi$ mọi trạng thái bảo đảm đi tới kết thúc. Định lý nói về một chính sách cho trước, không về chính sách tối ưu.
:::

::: proof Chứng minh Định lý 03.28
**Bước 1 (phép nhân $P_\pi$ không tăng chuẩn cực đại).** Các phần tử của $P_\pi$ không âm và mỗi hàng có tổng không quá $1$ (Định nghĩa 03.26). Với mọi $x\in\mathbb R^n$ và mọi hàng $i$,

$$
\begin{aligned}
\bigl\lvert(P_\pi x)_i\bigr\rvert&=\Bigl\lvert\sum_j(P_\pi)_{ij}x_j\Bigr\rvert\\
&\le\sum_j(P_\pi)_{ij}\lvert x_j\rvert\\
&\le\Bigl(\sum_j(P_\pi)_{ij}\Bigr)\lVert x\rVert_\infty\\
&\le\lVert x\rVert_\infty.
\end{aligned}
$$

Dòng thứ hai dùng bất đẳng thức tam giác và $(P_\pi)_{ij}\ge0$; dòng thứ ba dùng $\lvert x_j\rvert\le\lVert x\rVert_\infty$; dòng cuối dùng tổng hàng không quá $1$. Lấy cực đại theo $i$: $\lVert P_\pi x\rVert_\infty\le\lVert x\rVert_\infty$.

**Bước 2 (phần a).** Giả sử $(I-\gamma P_\pi)x=0$, tức $x=\gamma P_\pi x$. Theo Bước 1, $\lVert x\rVert_\infty=\gamma\lVert P_\pi x\rVert_\infty\le\gamma\lVert x\rVert_\infty$, nên $(1-\gamma)\lVert x\rVert_\infty\le0$. Vì $\gamma<1$, ta có $x=0$. Ma trận vuông chỉ có nghiệm tầm thường cho hệ thuần nhất thì khả nghịch.

**Bước 3 (phần b).** Theo Mệnh đề 03.27, véc-tơ $v_\pi$ thỏa (5.3); mỗi thành phần của nó là số thực nhờ Mệnh đề 03.11. Theo phần (a), hệ (5.3) có đúng một nghiệm, $(I-\gamma P_\pi)^{-1}r_\pi$, nên nghiệm đó là $v_\pi$.

**Bước 4 (khai triển lặp, phần c).** Ta chứng minh bằng quy nạp theo $K\ge0$ rằng

$$
v_\pi=\sum_{k=0}^{K-1}\gamma^k(P_\pi)^kr_\pi+\gamma^K(P_\pi)^Kv_\pi .
$$

Với $K=0$, tổng rỗng và đẳng thức là $v_\pi=v_\pi$. Nếu đẳng thức đúng với $K$, thay $v_\pi=r_\pi+\gamma P_\pi v_\pi$ (Mệnh đề 03.27) vào số hạng cuối:

$$
\gamma^K(P_\pi)^Kv_\pi=\gamma^K(P_\pi)^Kr_\pi+\gamma^{K+1}(P_\pi)^{K+1}v_\pi ,
$$

đó là đẳng thức với $K+1$.

**Bước 5 (qua giới hạn).** Áp dụng Bước 1 $K$ lần: $\lVert\gamma^K(P_\pi)^Kv_\pi\rVert_\infty\le\gamma^K\lVert v_\pi\rVert_\infty$. Theo Bước 4, đây là sai khác giữa $v_\pi$ và tổng riêng $K$ số hạng. Vì $\gamma<1$, sai khác tiến tới $0$, nên chuỗi (5.5) hội tụ về $v_\pi$. $\square$
:::

Định lý 03.28 đọc như sau: khi $\gamma<1$ và số trạng thái hữu hạn, hệ phương trình Bellman của một chính sách có đúng một nghiệm, và nghiệm đó là giá trị của chính sách. Giải hệ bằng bất kỳ phương pháp đúng nào cũng cho $v_\pi$. So với Định lý 03.21, Định lý 03.28 không thêm giả thiết nào mà cho thêm công thức (5.4), (5.5).

Khai triển (5.5) cũng có nghĩa trực tiếp. Cộng (3.2) theo mọi hành động, phần thưởng và trạng thái trung gian, phần tử $(s,s'')$ của $(P_\pi)^k$ là xác suất đi từ $s$ tới trạng thái chưa kết thúc $s''$ sau đúng $k$ bước; vì vậy thành phần thứ $s$ của $(P_\pi)^kr_\pi$ là $\mathbb E_\pi[R_{k+1}\mid S_0=s]$, với quy ước $R_{k+1}=0$ sau thời điểm kết thúc (Nhận xét 03.10). Đổi thứ tự kỳ vọng và tổng chuỗi trong (3.3) là hợp lệ vì phần đuôi sau $K$ số hạng bị chặn bởi $\gamma^KM/(1-\gamma)$ trên mọi quỹ đạo; do đó (5.5) là (3.3) viết theo từng bước thời gian.

Hai giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ $\gamma<1$: với robot và $\gamma=1$, mỗi hàng của $P_\pi$ có tổng $1$, nên véc-tơ toàn số $1$ thỏa $(I-P_\pi)\mathbf 1=0$ và $I-P_\pi$ không khả nghịch. Hệ (5.3) của robot khi đó là $\tfrac12v_{\mathrm H}-\tfrac12v_{\mathrm L}=2$ và $-\tfrac12v_{\mathrm H}+\tfrac12v_{\mathrm L}=\tfrac12$; cộng hai phương trình được $0=\tfrac52$, nên hệ vô nghiệm.
- Bỏ tập trạng thái hữu hạn: với $\mathcal S=\{0,1,2,\dots\}$, chuyển tất định $s\to s+1$, phần thưởng $0$ và $\gamma=\tfrac12$, hệ $v(s)=\tfrac12v(s+1)$ có mọi nghiệm $v(s)=c\,2^s$, $c\in\mathbb R$, trong khi $v_\pi=0$. Lập luận "ma trận vuông có hạt nhân tầm thường thì khả nghịch" ở Bước 2 không còn áp dụng, và tính duy nhất chỉ còn đúng trong lớp hàm bị chặn.

Bước 2, Bước 3 và Bước 5 của chứng minh dùng $\gamma<1$; Bước 2 và Bước 3 dùng tính hữu hạn.

::: example Ví dụ 03.17 (Nghịch đảo cho robot)
**Dữ kiện.** Ma trận chuyển và véc-tơ thưởng kỳ vọng của robot dưới chính sách chia đều tại pin thấp (Ví dụ 03.16), theo thứ tự $\mathrm H$, $\mathrm L$:

$$
\begin{aligned}
P_\pi&=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\\
r_\pi&=\begin{pmatrix}2\\1/2\end{pmatrix},\qquad\gamma=\tfrac12 .
\end{aligned}
$$

**Nghịch đảo.**

$$
\begin{aligned}
I-\gamma P_\pi&=\begin{pmatrix}3/4&-1/4\\-1/4&3/4\end{pmatrix},\\
\det(I-\gamma P_\pi)&=\tfrac9{16}-\tfrac1{16}=\tfrac12,\\
(I-\gamma P_\pi)^{-1}&=\begin{pmatrix}3/2&1/2\\1/2&3/2\end{pmatrix}.
\end{aligned}
$$

**Tính.** Theo (5.4): $v_{\mathrm H}=\tfrac32\cdot2+\tfrac12\cdot\tfrac12=\tfrac{13}4$ và $v_{\mathrm L}=\tfrac12\cdot2+\tfrac32\cdot\tfrac12=\tfrac74$.

**Kiểm tra lại.** Kết quả trùng phép khử thế của Ví dụ 03.14; tích $(I-\gamma P_\pi)(I-\gamma P_\pi)^{-1}$ có hàng thứ nhất $\bigl(\tfrac98-\tfrac18,\ \tfrac38-\tfrac38\bigr)=(1,0)$.
:::

### 5.4 Thuật toán đánh giá chính sách bằng giải hệ

Ví dụ 03.14, 03.16 và 03.17 đã thực hiện bằng tay mọi bước: lập $P_\pi$ và $r_\pi$ từ $p$ và $\pi$, lập ma trận $I-\gamma P_\pi$, giải hệ, kiểm tra lại. Thuật toán sau viết các bước đó cho MDP hữu hạn bất kỳ.

::: algorithm Thuật toán 03.29 (Đánh giá chính sách bằng giải hệ tuyến tính)
**Đầu vào.** MDP hữu hạn với các trạng thái chưa kết thúc $s_1,\dots,s_n$ theo một thứ tự cố định; hàm động lực $p$ hoặc hai mảng $p(s'\mid s,a)$, $r(s,a)$; chính sách Markov dừng $\pi$; hệ số chiết khấu $\gamma$.

**Đầu ra.** Véc-tơ $v\in\mathbb R^n$ với $v_i=v_\pi(s_i)$; giá trị tại trạng thái kết thúc bằng $0$.

**Giả thiết.** Trạng thái có tính Markov, hàm động lực không đổi theo thời gian, phần thưởng bị chặn, $0\le\gamma<1$ (Định lý 03.28). Đây là bài toán dự đoán có mô hình.

**Khởi tạo.** $P_\pi\leftarrow0\in\mathbb R^{n\times n}$, $r_\pi\leftarrow0\in\mathbb R^n$.

**Tham số.** $\gamma$; dung sai (tolerance) làm tròn $\eta>0$ cho bước kiểm tra, chẳng hạn $\eta=10^{-9}$.

1. Kiểm tra đầu vào, trong dung sai $\eta$: $0\le\gamma<1$; mọi $\pi(\cdot\mid s)$ không âm và có tổng $1$; nếu đầu vào là hàm động lực, mọi $p(\cdot,\cdot\mid s,a)$ không âm và có tổng $1$ trên $\mathcal S^+\times\mathcal R$ theo (1.3); nếu đầu vào là hai mảng, mọi $p(\cdot\mid s,a)$ không âm và có tổng $1$ trên $\mathcal S^+$. Nếu không, dừng và báo lỗi dữ liệu.
2. Nếu chỉ có $p(s',r\mid s,a)$, tính $p(s'\mid s,a)$ theo (1.5) và $r(s,a)$ theo (1.6) cho mọi cặp hợp lệ.
3. Với mỗi $s$: $r_\pi(s)\leftarrow\sum_a\pi(a\mid s)\,r(s,a)$; với mỗi $s'\in\mathcal S$: $(P_\pi)_{ss'}\leftarrow\sum_a\pi(a\mid s)\,p(s'\mid s,a)$. Cột của trạng thái kết thúc không được đưa vào $P_\pi$. Kiểm tra mọi hàng của $P_\pi$ có tổng không quá $1+\eta$.
4. Lập $A\leftarrow I-\gamma P_\pi$.
5. Giải hệ $Av=r_\pi$ bằng phép khử Gauss, không tính nghịch đảo tường minh.
6. Tính phần dư (residual) $\rho\leftarrow\lVert v-r_\pi-\gamma P_\pi v\rVert_\infty$. Nếu $\rho>\eta\max(1,\lVert r_\pi\rVert_\infty)$, báo sai số làm tròn lớn.
7. Trả $v$.

**Điều kiện dừng.** Thuật toán trực tiếp, không có vòng lặp: dừng sau bước 7 với số phép tính hữu hạn. Bước 6 là phép kiểm tra số học, không phải tiêu chuẩn hội tụ.

**Chi phí.** Bước 1–2: tỉ lệ với số bộ $(s,a,s',r)$ có $p>0$. Bước 3: $O(n^2\max_s\lvert\mathcal A(s)\rvert)$. Bước 5: cỡ $n^3$ phép tính và $O(n^2)$ bộ nhớ. Bước 6: $O(n^2)$.
:::

Áp dụng Thuật toán 03.29 cho robot, bước 3 cho đúng $P_\pi$, $r_\pi$ của Ví dụ 03.16, bước 4 cho ma trận $I-\gamma P_\pi$ của Ví dụ 03.17, bước 5 cho $(13/4,\,7/4)$ như Ví dụ 03.14, và bước 6 cho phần dư $0$ khi tính bằng phân số (cỡ $10^{-16}$ khi tính bằng số dấu phẩy động).

::: remark Nhận xét 03.30 (Giới hạn của giải hệ trực tiếp)
- **Quy mô.** Chi phí cỡ $n^3$ chấp nhận được khi $n$ vài trăm hay vài nghìn; với $n=10^6$ trạng thái, ma trận $P_\pi$ có $10^{12}$ phần tử và phép khử cần cỡ $10^{18}$ phép tính.
- **Cần mô hình.** Bước 2–3 dùng $p$. Khi chỉ có mẫu chuyển, chúng ta phải ước lượng $v_\pi$ từ dữ liệu.
:::

**Trong thực hành.** Notebook CartPole của Bài 04 giải hệ (5.3) bằng `np.linalg.solve` cho một chính sách trên $324$ ô, cỡ $324^3\approx3{,}4\cdot10^7$ phép tính; chia mỗi biến thành $10$ khoảng thì $n=10^4$ và chi phí cỡ $10^{12}$.

::: remark Nhận xét 03.31 (So sánh giá trị hành động chưa chứng minh tối ưu)
Ví dụ 03.15 cho $q_\pi(\mathrm L,\mathrm{cho})=15/8>q_\pi(\mathrm L,\mathrm{sac})=13/8$. Bất đẳng thức này so sánh hai thí nghiệm chỉ khác nhau ở hành động đầu, với phần tiếp diễn theo cùng chính sách $\pi$; nó chưa cho biết chính sách nào tốt nhất, vì không chính sách nào khác được đánh giá. Muốn kết luận về một chính sách mới, chúng ta phải đánh giá chính sách đó, chẳng hạn bằng Thuật toán 03.29 như ở Bài tập 03.8.
:::

::: exercise Bài tập 03.8
**Dữ kiện.** Robot của Ví dụ 03.1 với chính sách luôn Chờ tại pin thấp: ở $\mathrm H$ luôn Tìm (phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$); ở $\mathrm L$ luôn Chờ (phần thưởng $1$, ở lại $\mathrm L$). $\gamma=1/2$.

**Yêu cầu.** (a) Lập $P_\pi$ và $r_\pi$ theo thứ tự $\mathrm H$, $\mathrm L$. (b) Giải $(I-\gamma P_\pi)v=r_\pi$. (c) So sánh với giá trị $(13/4,\,7/4)$ của chính sách chia đều tại pin thấp.
:::

::: hint
Phương trình của $\mathrm L$ chỉ chứa $v_{\mathrm L}$; giải nó trước.
:::

::: solution
**(a)** Hàng $\mathrm H$ giữ nguyên như Ví dụ 03.16: $(1/2,\,1/2)$, thưởng kỳ vọng $2$. Hàng $\mathrm L$: luôn Chờ nên luôn về $\mathrm L$ với phần thưởng $1$.

$$
\begin{aligned}
P_\pi&=\begin{pmatrix}1/2&1/2\\0&1\end{pmatrix},\\
r_\pi&=\begin{pmatrix}2\\1\end{pmatrix}.
\end{aligned}
$$

**(b)** Hệ (5.3) là $v_{\mathrm H}=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$ và $v_{\mathrm L}=1+\tfrac12v_{\mathrm L}$. Phương trình thứ hai cho $v_{\mathrm L}=2$. Thế vào phương trình thứ nhất: $\tfrac34v_{\mathrm H}=2+\tfrac12=\tfrac52$, nên $v_{\mathrm H}=\tfrac{10}3$.

**(c)** $(10/3,\,2)$ lớn hơn $(13/4,\,7/4)$ ở cả hai trạng thái: $\tfrac{10}3=\tfrac{40}{12}>\tfrac{39}{12}$ và $2>\tfrac74$.

**Kiểm tra lại.** $2+\tfrac14\bigl(\tfrac{10}3+2\bigr)=2+\tfrac43=\tfrac{10}3$ và $1+\tfrac12\cdot2=2$.
:::

::: exercise Bài tập 03.9
**Dữ kiện.** Robot của Ví dụ 03.1 với chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$), $\gamma=1/2$. Ba giá trị hành động tại pin thấp là $q_\pi(\mathrm L,\mathrm{tim})=\tfrac34$, $q_\pi(\mathrm L,\mathrm{cho})=\tfrac{15}8$, $q_\pi(\mathrm L,\mathrm{sac})=\tfrac{13}8$ (Ví dụ 03.15). Chính sách luôn Chờ tại pin thấp có giá trị $(10/3,\,2)$ (Bài tập 03.8).

**Yêu cầu.** Chỉ ra lỗi trong lập luận "vì $q_\pi(\mathrm L,\mathrm{cho})$ lớn nhất trong ba giá trị nên chính sách chia đều tại pin thấp là tối ưu", và nói điều cần làm để kết luận về chính sách luôn Chờ.
:::

::: hint
Ba giá trị đều giả định phần tiếp diễn theo chính sách chia đều. Chính sách chia đều chọn những hành động nào ở pin thấp.
:::

::: solution
Ba giá trị chỉ so sánh các lệch một bước khỏi chính sách chia đều, với phần tiếp diễn theo chính sách đó. Chính sách chia đều còn chọn Sạc với xác suất $1/2$ dù $q_\pi(\mathrm L,\mathrm{sac})<q_\pi(\mathrm L,\mathrm{cho})$, và Bài tập 03.8 cho thấy chính sách luôn Chờ tại pin thấp có giá trị lớn hơn ở cả hai trạng thái; vậy kết luận "tối ưu" sai. Bài tập 03.8 chỉ chứng minh chính sách luôn Chờ tốt hơn chính sách chia đều; kết luận tối ưu cần các công cụ của Bài 04.

**Kiểm tra lại.** $v_\pi(\mathrm L)=\tfrac12\cdot\tfrac{15}8+\tfrac12\cdot\tfrac{13}8=\tfrac74<2$, phù hợp với việc chính sách luôn Chờ dồn toàn bộ xác suất vào hành động có giá trị hành động lớn hơn.
:::

Dưới chính sách chia đều tại pin thấp, robot có $v_\pi(\mathrm H)=13/4$ và $v_\pi(\mathrm L)=7/4$; với mọi MDP hữu hạn và $\gamma<1$, hệ $(I-\gamma P_\pi)v=r_\pi$ có nghiệm duy nhất $v_\pi$ (Mệnh đề 03.27, Định lý 03.28) và Thuật toán 03.29 tính nghiệm đó. Tuy nhiên, phép giải hệ trực tiếp cần biết $p$, có chi phí cỡ $n^3$ nên không dùng được cho tập trạng thái lớn, và chỉ đánh giá một chính sách chứ chưa cho biết chính sách nào tốt hơn.

<!-- note-topic-id: lec-03-part-07 -->
## Tình huống áp dụng và ứng dụng

Hai tình huống dưới đây áp dụng Thuật toán 03.29: một lưới $25$ trạng thái thỏa mọi giả thiết của Định lý 03.28, và CartPole rời rạc hóa, nơi giả thiết Markov không được bảo đảm.

::: application Tình huống 03.1 (Đánh giá chính sách chọn đều trên lưới 5×5)
**Bài toán và môi trường.** Lưới $5\times5$ của Sutton và Barto (2018, ví dụ 3.5, tr. 60). Mỗi ô là một trạng thái. Ở mỗi ô có bốn hành động bắc, nam, đông, tây, đưa tác tử sang ô kề theo hướng đó một cách tất định. Phần thưởng và các bước nhảy:

- hành động đi ra ngoài lưới giữ nguyên ô và cho phần thưởng $-1$;
- ở ô $\mathrm A$ (hàng 1, cột 2), mọi hành động đưa tới ô $\mathrm A'$ (hàng 5, cột 2) với phần thưởng $+10$;
- ở ô $\mathrm B$ (hàng 1, cột 4), mọi hành động đưa tới ô $\mathrm B'$ (hàng 3, cột 4) với phần thưởng $+5$;
- mọi bước khác cho phần thưởng $0$.

Nhiệm vụ tiếp diễn. Chính sách chọn mỗi hành động với xác suất $1/4$ ở mọi ô; $\gamma=0{,}9$. Cần tính giá trị của chính sách tại mọi ô.

**Mô hình hóa.** MDP hữu hạn (Định nghĩa 03.7): $\mathcal S$ gồm $25$ ô, không có trạng thái kết thúc; $\mathcal A(s)$ gồm bốn hành động; $\mathcal R=\{-1,0,5,10\}$; với mỗi $(s,a)$, $p(s',r\mid s,a)=1$ cho đúng một cặp $(s',r)$. Chính sách $\pi(a\mid s)=1/4$ là chính sách Markov dừng (Định nghĩa 03.13).

**Xác minh giả thiết.**

- Tính Markov (Định nghĩa 03.2): ô hiện tại và hành động xác định duy nhất ô kế tiếp và phần thưởng, nên lịch sử không cho thêm thông tin.
- Tính dừng: quy luật không đổi theo thời gian.
- Phần thưởng bị chặn với $M=10$ và $\gamma=0{,}9<1$, nên $\lvert G_t\rvert\le100$ (Mệnh đề 03.11).
- Tập trạng thái hữu hạn, $n=25$: Định lý 03.28 áp dụng, hệ có nghiệm duy nhất.

**Áp dụng Thuật toán 03.29.** Bước 3 cho $r_\pi$ như sau:

- $0$ ở ô bên trong;
- $-\tfrac14$ ở ô cạnh không phải góc;
- $-\tfrac12$ ở ô góc;
- $10$ ở $\mathrm A$;
- $5$ ở $\mathrm B$.

Hàng của $P_\pi$ có phần tử $\tfrac14$ ở mỗi ô tới được; tại ô cạnh, chính ô đó nhận $\tfrac14$ cho mỗi hướng đi ra ngoài; $(P_\pi)_{\mathrm A\mathrm A'}=(P_\pi)_{\mathrm B\mathrm B'}=1$. Bước 5 giải hệ $25$ ẩn; phần (b) của hình dưới ghi nghiệm làm tròn một chữ số, các giá trị thập phân dưới đây được tính lại bằng phép khử Gauss trên số hữu tỉ.

**Kiểm tra lại bằng phương trình Bellman.** Theo (4.5), tại $\mathrm A$ chỉ có một phản hồi, nên

$$
\begin{aligned}
v_\pi(\mathrm A)&=10+0{,}9\,v_\pi(\mathrm A')\\
&=10+0{,}9\cdot(-1{,}3452)\approx8{,}789 ,
\end{aligned}
$$

trùng nghiệm $8{,}789$. Tại $\mathrm B$: $5+0{,}9\cdot0{,}358\approx5{,}322$, trùng nghiệm $5{,}322$.

**Diễn giải.** $v_\pi(\mathrm A)\approx8{,}8<10$ vì bước nhảy đưa tác tử tới $\mathrm A'$ ở cạnh dưới, nơi chính sách chọn đều thường đi ra ngoài lưới, nên $v_\pi(\mathrm A')<0$. Ngược lại $v_\pi(\mathrm B)\approx5{,}3>5$ vì $\mathrm B'$ có giá trị dương.

**Giới hạn.** Nghiệm chỉ đánh giá chính sách chọn đều; nó không cho biết chính sách nào tốt hơn (Nhận xét 03.31).

**Dẫn ngược.** Định nghĩa 03.2, 03.7, 03.13 (mô hình hóa); Mệnh đề 03.11 và Định lý 03.28 (kiểm giả thiết); Mệnh đề 03.27 và Thuật toán 03.29 (giải); Định lý 03.21 (kiểm tra lại và diễn giải).
:::

![Hai lưới 5 hàng 5 cột. Lưới trái, (a) động lực đặc biệt: ô A ở hàng 1 cột 2, ô A' ở hàng 5 cột 2, ô B ở hàng 1 cột 4, ô B' ở hàng 3 cột 4; mũi tên từ A xuống A' ghi +10, mũi tên từ B xuống B' ghi +5. Lưới phải, (b) giá trị v_π của chính sách chọn đều, γ = 0,9, theo hàng từ trên xuống: 3,3 8,8 4,4 5,3 1,5; 1,5 3,0 2,3 1,9 0,5; 0,1 0,7 0,7 0,4 −0,4; −1,0 −0,4 −0,4 −0,6 −1,2; −1,9 −1,3 −1,2 −1,4 −2,0. Chú thích: bốn hành động bắc, nam, đông, tây, mỗi hành động xác suất 1/4; tại A mọi hành động tới A' với thưởng +10, tại B tới B' với thưởng +5; bước ra ngoài lưới giữ nguyên ô với thưởng −1; các bước khác thưởng 0.](img/lec-03/gridworld-5x5.svg)

Phần (a) của hình vẽ hai bước nhảy có phần thưởng dương; phần (b) xếp nghiệm theo vị trí ô. Theo cột 2, giá trị giảm từ $8{,}8$ ở $\mathrm A$ xuống $-1{,}3$ ở $\mathrm A'$, đúng phương trình $v_\pi(\mathrm A)=10+0{,}9\,v_\pi(\mathrm A')$; các số trùng hình 3.2 của Sutton và Barto (2018) sau khi làm tròn.

::: application Tình huống 03.2 (CartPole rời rạc hóa: khi trạng thái không còn bảo đảm tính Markov)
**Bài toán và môi trường.** Môi trường `CartPole-v1` của Gymnasium trong notebook thực hành của Bài 04. Trạng thái vật lý $(x,\dot x,\theta,\dot\theta)$ gồm vị trí, vận tốc xe, góc của cột và vận tốc góc, với động lực tất định. Hành động $0$ đẩy trái, $1$ đẩy phải; phần thưởng $+1$ ở mọi bước. Lượt kết thúc khi $\lvert\theta\rvert>12^\circ$ hoặc $\lvert x\rvert>2{,}4$; giới hạn $500$ bước là cắt ngắn do cấu hình, không đưa vào mô hình.

**Mô hình hóa.** Mọi số liệu dưới đây lấy từ một lần chạy đã nhúng trong notebook. Notebook chia $x$, $\dot x$ thành $3$ khoảng và $\theta$, $\dot\theta$ thành $6$ khoảng, được $3\cdot3\cdot6\cdot6=324$ ô cộng một trạng thái kết thúc. Với mỗi ô và mỗi hành động, notebook lấy $N_{\text{mẫu}}=200$ trạng thái vật lý đều trong ô, chạy một bước và đếm ô kế tiếp, được $\hat p(s'\mid s,a)$; thưởng kỳ vọng ước lượng bằng $1$. Chính sách $\pi_0$, gọi là luật theo dấu góc, đẩy phải khi $\theta\ge0$ và đẩy trái khi $\theta<0$. Chọn $\gamma=0{,}99$.

**Xác minh giả thiết.**

- Tập hữu hạn ($n=324$), phần thưởng bị chặn ($M=1$), $\gamma<1$, và $\pi_0$ là chính sách Markov dừng trên ô: các giả thiết này thỏa.
- Tính Markov của ô (Định nghĩa 03.2) không được bảo đảm, vì một ô chứa vô số trạng thái vật lý có thể sang các ô khác nhau. Trong notebook, phân phối $\hat p(\cdot\mid s,a)$ của cặp (ô $66$, hành động $0$) có $11$ trạng thái kế tiếp với xác suất dương và entropy $1{,}815$ nat; entropy trung bình của các phân phối $\hat p(\cdot\mid s,a)$ trên mọi cặp là $1{,}052$ nat. Ô kế tiếp phụ thuộc vị trí bên trong ô hiện tại; nếu dãy ô đã đi qua mang thông tin về vị trí đó, (1.2) sai. Entropy dương không đủ để kết luận ô mất tính Markov; muốn kết luận, chúng ta phải kiểm tra (1.2) trực tiếp trên quỹ đạo.
- Bảng $\hat p$ là hàm động lực của một MDP thay thế $(\hat p,\hat r)$, xây dựng với giả thiết trạng thái phân bố đều trong mỗi ô; MDP thay thế thỏa Định nghĩa 03.7 theo cách xây dựng.

**Áp dụng.** Giải hệ (5.3) cho $\pi_0$ trên MDP thay thế cho phần dư cỡ $2{,}1\cdot10^{-14}$ và các giá trị trong khoảng $6{,}335$ tới $31{,}080$, dưới cận $1/(1-\gamma)=100$ của Mệnh đề 03.11. Theo Định lý 03.28, đây là giá trị chính xác của $\pi_0$ trong MDP thay thế.

**Hậu quả quan sát được.** Notebook so giá trị dự đoán với lợi tức thật cho một chính sách khác, chính sách Markov dừng trên ô mà phương pháp của Bài 04 tìm được trên cùng MDP thay thế. Trên $100$ lượt trong môi trường liên tục, giá trị dự đoán trung bình tại các ô xuất phát là $84{,}473$, lợi tức chiết khấu thực tế trung bình là $95{,}377$, sai số chuẩn (standard error, SE) $0{,}370$. Chênh lệch $10{,}904$ lớn hơn nhiều so với sai số chuẩn $0{,}370$ và mức giảm tối đa $0{,}657$ do cắt ngắn ở $500$ bước, và phép giải hệ cho nghiệm đúng của MDP thay thế; do đó chênh lệch đến từ khoảng cách giữa MDP thay thế và quá trình thật nhìn qua các ô.

**Diễn giải.** Bước có thể hỏng khi áp dụng cho CartPole là Bổ đề 03.20: kỳ vọng của phần tương lai sau một lịch sử kết thúc ở ô $s$ chỉ bằng một số chung khi ô có tính Markov. Định lý 03.28 kiểm soát sai số giải hệ, không kiểm soát khoảng cách giữa mô hình và môi trường.

**Giới hạn và dẫn ngược.** Con số $10{,}904$ phụ thuộc cách chia ô và hạt giống ngẫu nhiên (random seed). Tình huống dùng Định nghĩa 03.2 (giả thiết bị vi phạm), Định nghĩa 03.4, 03.7 (MDP thay thế), Mệnh đề 03.11 (cận $100$), Bổ đề 03.20 và Định lý 03.21 (bước dùng tính Markov), Định lý 03.28 và Mệnh đề 03.27 (giải hệ $324$ ẩn).
:::

**Liên hệ với các bài sau.**

- **Bài 04.** Quy hoạch động (dynamic programming) dùng $p$; đánh giá chính sách lặp (iterative policy evaluation) thay phép khử cỡ $n^3$ bằng phép lặp $v\leftarrow r_\pi+\gamma P_\pi v$, mà từ $v=0$, lần lặp thứ $K$ cho đúng tổng riêng $K$ số hạng của chuỗi Neumann (5.5). Định lý cải thiện chính sách (policy improvement theorem) nối phép so sánh các $q_\pi(s,a)$ tính bằng (4.6) với việc đổi chính sách; lặp chính sách (policy iteration) dựa trên định lý này giải bài toán điều khiển khi biết mô hình.
- **Bài 05.** Trong dự đoán phi mô hình (model-free), Monte Carlo ước lượng $v_\pi(s)$ bằng trung bình các lợi tức quan sát được từ $s$; Monte Carlo và TD(0) chỉ cần mẫu chuyển, không cần $p$.
- **Bài 06.** Trong điều khiển phi mô hình, Q-learning dùng dạng có cực đại của cấu trúc "phần thưởng một bước cộng giá trị chiết khấu của trạng thái kế tiếp" trong (4.8).
- **Bài 07.** Trong xấp xỉ hàm (function approximation), khi $n$ quá lớn cho Thuật toán 03.29, giá trị được biểu diễn bằng hàm có tham số trên trạng thái liên tục; đặc trưng có thể mất tính Markov như ô CartPole.
- **Bài 08.** Trong Deep Q-learning, bộ nhớ phát lại (replay buffer) lưu các mẫu chuyển $(S_t,A_t,R_{t+1},S_{t+1})$ như Ví dụ 03.2; mục tiêu học của mạng dùng phần thưởng một bước cộng giá trị chiết khấu do mạng mục tiêu (target network) tính tại trạng thái kế tiếp.

<!-- note-topic-id: lec-03-part-08 -->
## Tóm tắt chương

Câu hỏi xuất phát là so sánh giá trị dài hạn của các cách hành động của robot thu gom lon khi phản hồi là ngẫu nhiên. Chúng ta mô tả môi trường bằng hàm động lực $p(s',r\mid s,a)$, với giả thiết trạng thái có tính Markov (Định nghĩa 03.2, 03.4), rồi gom thành MDP hữu hạn (Định nghĩa 03.7). Chúng ta gộp chuỗi phần thưởng thành lợi tức chiết khấu, hữu hạn khi phần thưởng bị chặn và $\gamma<1$ (Định nghĩa 03.9, Mệnh đề 03.11). Cố định chính sách Markov dừng, chúng ta định nghĩa giá trị trạng thái và giá trị hành động (Định nghĩa 03.13, 03.15, 03.16), rồi tách bước đầu của lợi tức và dùng tính Markov của phần tương lai (Bổ đề 03.18–03.20) để chứng minh phương trình Bellman kỳ vọng cho $v_\pi$ và $q_\pi$ (Định lý 03.21, Hệ quả 03.24). Hai giả thiết MDP hữu hạn và $\gamma<1$ của Định lý 03.21 cũng làm $I-\gamma P_\pi$ khả nghịch, nên hệ Bellman có nghiệm duy nhất $v_\pi=(I-\gamma P_\pi)^{-1}r_\pi$ (Định lý 03.28), tính được bằng giải hệ trực tiếp (Thuật toán 03.29). Với robot, $v_\pi=(13/4,\,7/4)$ và $q_\pi(\mathrm L,\cdot)=(3/4,\,15/8,\,13/8)$; Chờ hơn Sạc $1/4$, không phải $1$ như phần thưởng một bước. Còn lại bốn giới hạn: ba giới hạn của phép giải hệ là cần biết $p$, chi phí cỡ $n^3$ và việc chỉ đánh giá chứ chưa chọn được chính sách; giới hạn thứ tư thuộc mô hình, là điều kiện trạng thái phải có tính Markov (Tình huống 03.2). Bài 04 xử lý chi phí giải hệ và việc chọn chính sách khi vẫn biết mô hình; Bài 05–06 bỏ giả thiết biết $p$.

**Định nghĩa và kết quả theo mục.**

**Mục 1.**

- Định nghĩa 03.1: quỹ đạo xen kẽ $S_t$, $A_t$, $R_{t+1}$, và lịch sử $H_t$ dừng ở $S_t$.
- Định nghĩa 03.2: trạng thái có tính Markov khi phân phối của $(S_{t+1},R_{t+1})$ khi biết $(H_t,A_t)$ chỉ phụ thuộc $(S_t,A_t)$.
- Nhận xét 03.3: tính Markov thuộc về biểu diễn trạng thái.
- Định nghĩa 03.4: hàm động lực $p(s',r\mid s,a)$ là phân phối một bước, giống nhau ở mọi lịch sử và mọi thời điểm.
- Nhận xét 03.5: tính dừng là giả thiết riêng bên cạnh tính Markov.
- Mệnh đề 03.6: $p(s'\mid s,a)$, $r(s,a)$ suy ra từ $p$ theo (1.5), (1.6) nhưng không dựng lại được $p$.
- Định nghĩa 03.7: MDP hữu hạn là bộ $(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p)$ sinh quỹ đạo theo $p$, còn $\gamma$ đứng ngoài bộ.

**Mục 2.**

- Định nghĩa 03.8: nhiệm vụ có kết thúc dừng tại $T<\infty$, nhiệm vụ tiếp diễn có $T=\infty$.
- Định nghĩa 03.9: $G_t=\sum_{k=t+1}^{T}\gamma^{k-t-1}R_k$, với $T=\infty$ chỉ khi $\gamma<1$.
- Nhận xét 03.10: đệm phần thưởng $0$ sau $T$ gộp hai loại nhiệm vụ.
- Mệnh đề 03.11: $\lvert G_t\rvert\le M/(1-\gamma)$ trên mọi quỹ đạo khi $\lvert R_k\rvert\le M$ và $\gamma<1$.
- Nhận xét 03.12: $\gamma=0$ cho mục tiêu cận thị, và đổi $\gamma$ là đổi bài toán.

**Mục 3.**

- Định nghĩa 03.13: chính sách Markov dừng $\pi(a\mid s)$ là một phân phối trên $\mathcal A(s)$ dùng ở mọi thời điểm.
- Mệnh đề 03.14: xác suất của một đoạn quỹ đạo là tích các thừa số $\pi(a\mid s)\,p(s',r\mid s,a)$.
- Định nghĩa 03.15: $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$.
- Định nghĩa 03.16: $q_\pi(s,a)$ ấn định $A_0=a$ rồi theo $\pi$, và xác định cả khi $\pi(a\mid s)=0$.
- Nhận xét 03.17: $q_\pi$ khác $r(s,a)$, và $v_\pi$ khác $G_t$.

**Mục 4.**

- Bổ đề 03.18: $G_t=R_{t+1}+\gamma G_{t+1}$ trên từng quỹ đạo.
- Bổ đề 03.19: kỳ vọng tách theo hành động với trọng số $\pi(a\mid s)$ rồi theo phản hồi với trọng số $p(s',r\mid s,a)$.
- Bổ đề 03.20: khi biết lịch sử kết thúc ở $s$ và tác tử theo $\pi$ từ đó, kỳ vọng của $G_t$ bằng $v_\pi(s)$.
- Định lý 03.21: $v_\pi$ thỏa (4.5).
- Mệnh đề 03.22: $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s')$.
- Mệnh đề 03.23: $v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a)$.
- Hệ quả 03.24: $q_\pi$ thỏa (4.8).
- Nhận xét 03.25: Bổ đề 03.19 dùng tính Markov một bước, Bổ đề 03.20 dùng tính Markov cho toàn bộ tương lai và tính dừng.

**Mục 5.**

- Định nghĩa 03.26: dưới $\pi$, MDP thu về quá trình phần thưởng Markov $(\mathcal S,P_\pi,r_\pi,\gamma)$ theo (5.2).
- Mệnh đề 03.27: hệ Bellman là $(I-\gamma P_\pi)v=r_\pi$.
- Định lý 03.28: khi tập trạng thái hữu hạn và $\gamma<1$, $I-\gamma P_\pi$ khả nghịch và $v_\pi=(I-\gamma P_\pi)^{-1}r_\pi=\sum_{k\ge0}\gamma^k(P_\pi)^kr_\pi$.
- Thuật toán 03.29: lập $P_\pi$, $r_\pi$ rồi giải hệ bằng phép khử Gauss với chi phí cỡ $n^3$.
- Nhận xét 03.30: giải trực tiếp cần $p$ và không dùng được khi $n$ cỡ $10^6$.
- Nhận xét 03.31: $q_\pi(\mathrm L,\mathrm{cho})>q_\pi(\mathrm L,\mathrm{sac})$ chỉ so sánh lệch một bước khỏi $\pi$, không chứng minh tối ưu.

**Công thức cần nhớ.** Hàm động lực xác định xác suất chuyển và thưởng kỳ vọng:

$$
\begin{aligned}
p(s'\mid s,a)&=\sum_rp(s',r\mid s,a),\\
r(s,a)&=\sum_{s',r}r\,p(s',r\mid s,a).
\end{aligned}
$$

Lợi tức thỏa hệ thức đệ quy và bị chặn khi $\gamma<1$:

$$
G_t=R_{t+1}+\gamma G_{t+1},\qquad\lvert G_t\rvert\le\frac{M}{1-\gamma}.
$$

Tách bước đầu cho phương trình Bellman kỳ vọng:

$$
v_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr].
$$

Hai hàm giá trị biểu diễn được qua nhau:

$$
\begin{aligned}
q_\pi(s,a)&=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s'),\\
v_\pi(s)&=\sum_a\pi(a\mid s)\,q_\pi(s,a).
\end{aligned}
$$

Gộp chính sách vào mô hình cho dạng ma trận và nghiệm:

$$
v_\pi=(I-\gamma P_\pi)^{-1}r_\pi=\sum_{k\ge0}\gamma^k(P_\pi)^kr_\pi .
$$

**Giả thiết hay bị bỏ quên.**

- Tính Markov thuộc về cách chọn trạng thái; trạng thái thiếu thông tin (Ví dụ 03.4, Tình huống 03.2) làm Bổ đề 03.20 và mọi kết quả sau nó mất căn cứ.
- Tính dừng của hàm động lực và của chính sách là giả thiết riêng, đứng cạnh tính Markov.
- $\gamma<1$ là điều kiện của Mệnh đề 03.11 và Định lý 03.28 cho nhiệm vụ tiếp diễn; với $\gamma=1$, robot luôn Chờ có lợi tức vô hạn và hệ của robot vô nghiệm.
- Phần thưởng cố định trên mỗi nhánh là giả thiết thêm của ví dụ robot; $r(s,a)$ và $p(s'\mid s,a)$ không đủ để dựng lại $p$.
- Phương trình Bellman kỳ vọng là trung bình theo $\pi$; so sánh các $q_\pi(s,a)$ không chứng minh chính sách nào tối ưu.

## Bài tập củng cố

Năm bài 03.10–03.14 dưới đây xếp theo ba mức.

### Mức nhận biết

::: exercise Bài tập 03.10
**Dữ kiện.** Ba nhiệm vụ: (a) chơi một ván cờ ca-rô trên bàn $3\times3$, tối đa $9$ nước; (b) điều khiển nhiệt độ một tòa nhà suốt cả năm, mỗi phút một quyết định; (c) đi một lần trong mê cung tới ô đích, mỗi bước phần thưởng $-1$.

**Yêu cầu.** Xếp mỗi nhiệm vụ vào loại có kết thúc hoặc tiếp diễn (Định nghĩa 03.8), và nói $\gamma=1$ có dùng được không.
:::

::: hint
Xét tương tác có điểm dừng tự nhiên hay không; với $\gamma=1$, xét lợi tức có thể vô hạn hay không.
:::

::: solution
- **(a)** Có kết thúc; mỗi ván có không quá $9$ nước, nên với $\gamma=1$ lợi tức là tổng hữu hạn bị chặn; dùng được.
- **(b)** Tiếp diễn; với $\gamma=1$, tổng phần thưởng trên vô hạn bước có thể vô hạn, nên chọn $\gamma<1$, và khi đó lợi tức hữu hạn (Mệnh đề 03.11).
- **(c)** Có kết thúc. Với $\gamma=1$, lợi tức bằng trừ số bước tới đích; để kỳ vọng hữu hạn cần kỳ vọng số bước tới đích hữu hạn dưới chính sách đang xét (Nhận xét 03.12).

**Kiểm tra lại.** Phân loại phụ thuộc cấu trúc tương tác, không phụ thuộc giá trị của $\gamma$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 03.11
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$, $v_\pi(\mathrm H)=\tfrac{13}4$, $v_\pi(\mathrm L)=\tfrac74$. Tìm từ $\mathrm H$: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$. Chờ từ $\mathrm H$: phần thưởng $1$, ở lại $\mathrm H$. Chính sách ở $\mathrm H$ luôn Tìm.

**Yêu cầu.** Tính $q_\pi(\mathrm H,\mathrm{tim})$ và $q_\pi(\mathrm H,\mathrm{cho})$, rồi kiểm tra $v_\pi(\mathrm H)$ bằng (4.7).
:::

::: hint
Dùng dạng thứ hai của (4.6).
:::

::: solution
Theo (4.6):

$$
\begin{aligned}
q_\pi(\mathrm H,\mathrm{tim})&=2+\tfrac12\bigl(\tfrac12\cdot\tfrac{13}4+\tfrac12\cdot\tfrac74\bigr)\\
&=2+\tfrac12\cdot\tfrac52=\tfrac{13}4,\\
q_\pi(\mathrm H,\mathrm{cho})&=1+\tfrac12\cdot\tfrac{13}4=\tfrac{21}8 .
\end{aligned}
$$

Vì $\pi(\mathrm{tim}\mid\mathrm H)=1$, $\pi(\mathrm{cho}\mid\mathrm H)=0$, (4.7) cho $v_\pi(\mathrm H)=1\cdot\tfrac{13}4+0\cdot\tfrac{21}8=\tfrac{13}4$, đúng.

**Kiểm tra lại.** $q_\pi(\mathrm H,\mathrm{tim})=v_\pi(\mathrm H)$ vì chính sách chọn Tìm ở $\mathrm H$ với xác suất $1$.
:::

::: exercise Bài tập 03.12
**Dữ kiện.** Một lượt kết thúc tại $T=3$ với phần thưởng $R_1=1$, $R_2=-1$, $R_3=2$; $\gamma=0{,}9$.

**Yêu cầu.** Tính $G_3$, $G_2$, $G_1$, $G_0$ bằng cách tính lùi theo Bổ đề 03.18, rồi kiểm tra $G_0$ trực tiếp theo Định nghĩa 03.9.
:::

::: hint
Bắt đầu từ quy ước $G_T=0$.
:::

::: solution
Theo quy ước $G_3=0$. Theo (4.2):

$$
\begin{aligned}
G_2&=R_3+\gamma G_3=2+0{,}9\cdot0\\
&=2,\\
G_1&=R_2+\gamma G_2=-1+0{,}9\cdot2\\
&=0{,}8,\\
G_0&=R_1+\gamma G_1=1+0{,}9\cdot0{,}8\\
&=1{,}72 .
\end{aligned}
$$

**Kiểm tra lại.** Theo (2.1), $G_0=R_1+\gamma R_2+\gamma^2R_3=1-0{,}9+0{,}81\cdot2=1{,}72$.
:::

### Mức vận dụng

::: exercise Bài tập 03.13
**Dữ kiện.** Robot của Ví dụ 03.1 với một thay đổi: Tìm từ $\mathrm L$ giữ pin thấp (phần thưởng $2$) với xác suất $3/4$ và dẫn tới cứu hộ (về $\mathrm H$, phần thưởng $-3$) với xác suất $1/4$; Chờ từ $\mathrm L$ cho $(\mathrm L,1)$, Sạc cho $(\mathrm H,0)$, Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$. Chính sách chia đều tại pin thấp, $\gamma=1/2$. Trước thay đổi, giá trị của chính sách là $(13/4,\,7/4)$.

**Yêu cầu.** (a) Không giải lại hệ, xác định $v_\pi(\mathrm H)$, $v_\pi(\mathrm L)$ và giải thích. (b) Tính $r(\mathrm L,\mathrm{tim})$ và $q_\pi(\mathrm L,\mathrm{tim})$. (c) So sánh $q_\pi(\mathrm L,\mathrm{tim})$ với $q_\pi(\mathrm L,\mathrm{cho})$.
:::

::: hint
Thay đổi chỉ chạm vào cặp $(\mathrm L,\mathrm{tim})$. Xem cặp này có xuất hiện trong $P_\pi$, $r_\pi$ của chính sách chia đều không.
:::

::: solution
**(a)** Chính sách chia đều có $\pi(\mathrm{tim}\mid\mathrm L)=0$, nên theo (5.2) cặp $(\mathrm L,\mathrm{tim})$ không góp vào $P_\pi$ và $r_\pi$. Hai đối tượng này giữ nguyên, và theo Định lý 03.28, $v_\pi=(13/4,\,7/4)$ không đổi.

**(b)** Theo (1.6), $r(\mathrm L,\mathrm{tim})=\tfrac34\cdot2+\tfrac14\cdot(-3)=\tfrac34$. Theo (4.6),

$$
\begin{aligned}
q_\pi(\mathrm L,\mathrm{tim})&=\tfrac34+\tfrac12\bigl(\tfrac34\cdot\tfrac74+\tfrac14\cdot\tfrac{13}4\bigr)\\
&=\tfrac34+\tfrac12\cdot\tfrac{34}{16}=\tfrac{29}{16}.
\end{aligned}
$$

**(c)** $q_\pi(\mathrm L,\mathrm{cho})=1+\tfrac12\cdot\tfrac74=\tfrac{30}{16}$ không đổi, vì nó chỉ dùng $v_\pi(\mathrm L)$. Vậy Tìm vẫn kém Chờ $\tfrac1{16}$. Thay đổi của môi trường chỉ làm đổi giá trị của hành động mà chính sách không dùng.

**Kiểm tra lại.** Dạng thứ nhất của (4.6): $\tfrac34\cdot\tfrac{23}8-\tfrac14\cdot\tfrac{11}8=\tfrac{69}{32}-\tfrac{11}{32}=\tfrac{29}{16}$.
:::

::: exercise Bài tập 03.14
**Dữ kiện.** Lưới $5\times5$ của Tình huống 03.1: chính sách chọn đều bốn hướng, $\gamma=0{,}9$; bước đi ra ngoài lưới giữ nguyên ô với phần thưởng $-1$; bước khác ngoài các ô $\mathrm A$, $\mathrm B$ cho phần thưởng $0$. Giá trị (ba chữ số thập phân) tại ô giữa lưới (hàng 3, cột 3) là $0{,}673$; tại bốn ô kề: trên $2{,}250$, dưới $-0{,}355$, trái $0{,}738$, phải $0{,}358$. Giá trị tại ô hàng 3, cột 1 (cạnh trái) là $0{,}051$; tại ba ô kề trong lưới: trên $1{,}522$, dưới $-0{,}974$, phải $0{,}738$.

**Yêu cầu.** (a) Kiểm tra phương trình Bellman (4.5) tại ô giữa. (b) Kiểm tra (4.5) tại ô cạnh trái. (c) Giải thích vì sao ở câu (a) không có số hạng phần thưởng còn ở câu (b) có.
:::

::: hint
Mỗi hành động có xác suất $1/4$ và phản hồi tất định, nên (4.5) là trung bình của bốn số $r+0{,}9\,v_\pi(s')$.
:::

::: solution
**(a)** Ô giữa không chạm cạnh, mọi bước cho phần thưởng $0$:

$$
\begin{aligned}
&\tfrac14\cdot0{,}9\cdot\bigl(2{,}250-0{,}355+0{,}738+0{,}358\bigr)\\
&\qquad=0{,}225\cdot2{,}991\approx0{,}673 .
\end{aligned}
$$

**(b)** Ở ô cạnh trái, hướng tây đi ra ngoài lưới: phần thưởng $-1$ và ở lại ô đó.

$$
\begin{aligned}
&\tfrac14\bigl[(-1+0{,}9\cdot0{,}051)+0{,}9\cdot1{,}522+0{,}9\cdot(-0{,}974)+0{,}9\cdot0{,}738\bigr]\\
&\qquad\approx\tfrac14\bigl[-0{,}954+1{,}370-0{,}877+0{,}664\bigr]\approx0{,}051 .
\end{aligned}
$$

**(c)** Phần thưởng $-1$ chỉ phát sinh khi đi ra ngoài lưới. Ô giữa không có hướng nào đi ra ngoài, nên $r_\pi=0$; ô cạnh trái có một hướng, nên $r_\pi=-\tfrac14$ và chính ô đó xuất hiện ở vế phải với trọng số $\tfrac14\cdot0{,}9$.

**Kiểm tra lại.** Với các giá trị làm tròn một chữ số của Sutton và Barto (2018, bài tập 3.14), câu (a) cho $0{,}225\cdot(2{,}3-0{,}4+0{,}7+0{,}4)=0{,}675\approx0{,}7$.
:::

<!-- note-topic-id: lec-03-part-10 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

- **Bài giảng gốc (2025–2026)**, *Markov Decision Processes with Key Concepts*, trang 28–58: phạm vi của chương; trang 29 và 49 cho Mục 1, 36–38 cho Mục 2, 39 và 52–53 cho Mục 3, 44–46 và 56–57 cho Mục 4, 30, 34 và 47–48 cho Mục 5, trang 58 cho phần tổng kết. Bản gốc trình bày chuỗi Markov, quá trình phần thưởng Markov rồi MDP; ở ghi chú này, MDP được trình bày trước theo Sutton và Barto (2018, §3.1), và hai đối tượng kia được dựng lại ở Mục 5.
- **D. P. Bertsekas và J. N. Tsitsiklis**, *Introduction to Probability*, chương 7, và ghi chú xác suất của CS229 (Stanford): tài liệu đọc về xác suất có điều kiện và kỳ vọng toàn phần mà Bài giảng gốc (trang 58) dẫn, dùng cho mục Kiến thức tiên quyết.
- **Bài tập tuần 2 (2025–2026)**, Tạ Việt Cường, ngày 12/3/2026, bài 3, 4, 7, 8, 10: bài 4 ứng với Định nghĩa 03.26 và là nguồn của Bài tập 03.21; bài 7, 8 ứng với Mệnh đề 03.23 và Định lý 03.21, là nguồn của Bài tập 03.7, 03.19; bài 3 là một hệ Bellman ba trạng thái có trạng thái hấp thụ, nguồn của Bài tập 03.20; bài 10 mô hình hóa một bài toán thực tế thành MDP theo Định nghĩa 03.7, nguồn của Bài tập 03.24.
- **Bài tập tuần 3 (2025–2026)**, Tạ Việt Cường, ngày 8/5/2026, bài 1: nguồn của Bài tập 03.16.
- **R. S. Sutton và A. G. Barto (2018)**, *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Chương 3 (§3.1, tr. 48–53 cho Mục 1; §3.3–3.4, tr. 54–57 cho Mục 2; §3.5, tr. 58–62 cho Mục 3–4; ví dụ 3.5, tr. 60 cho Tình huống 03.1) và §4.1, tr. 74 (Mục 5). Đọc tiếp §3.6 về giá trị tối ưu trước Bài 04, và chương 17 về dựng trạng thái Markov từ quan sát không Markov.
- **M. L. Puterman (1994)**, *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley, §6.1: đánh giá chính sách trong MDP chiết khấu, nghiệm dạng nghịch đảo và chuỗi Neumann, ở mức tổng quát hơn Định lý 03.28.
- **D. P. Bertsekas (2019)**, *Reinforcement Learning and Optimal Control*, Athena Scientific, chương về bài toán vô hạn chiết khấu: phương trình Bellman viết bằng toán tử, dẫn sang tính co dùng ở Bài 04.
- **Trần Quốc Long (chủ biên), Tạ Việt Cường**, *Học máy thống kê*, chương Học tăng cường, mục giới thiệu quá trình quyết định Markov và mục quy hoạch động: bộ $\langle S,A,T,R,\gamma\rangle$, giá trị của quỹ đạo $U(\tau)$ (ứng với $G_0$) và phương trình Bellman cho $V^\pi$ (ứng với Định lý 03.21).
- **Notebook thực hành Bài 04**, `thuc-hanh-cartpole-quy-hoach-dong.ipynb`, phần 5, mục 6.2 và 8.1: nguồn số liệu của Tình huống 03.2.
