# Bài 03 — Quá trình quyết định Markov

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Kiểm tra một biểu diễn trạng thái có tính Markov hay không, lập bộ quá trình quyết định Markov (Markov decision process, MDP) hữu hạn và bảng hàm động lực $p(s',r\mid s,a)$ từ một mô tả bằng lời, kiểm tra điều kiện chuẩn hóa và suy ra $p(s'\mid s,a)$, $r(s,a)$ (Định nghĩa 03.2, 03.4, 03.7, Mệnh đề 03.6; Bài tập 03.1, 03.2).
2. Phân loại nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn, tính lợi tức (return) chiết khấu của một dãy phần thưởng và dùng cận $\lvert G_t\rvert\le M/(1-\gamma)$, tính lùi lợi tức theo $G_t=R_{t+1}+\gamma G_{t+1}$ (Định nghĩa 03.8, 03.9, Mệnh đề 03.11, Bổ đề 03.18; Bài tập 03.3, 03.10, 03.12).
3. Phân biệt mô hình, chính sách, giá trị trạng thái và giá trị hành động; tính kỳ vọng của lợi tức cắt sau hai bước trên cây quỹ đạo (Định nghĩa 03.13, 03.15, 03.16; Bài tập 03.4, 03.5).
4. Chứng minh phương trình Bellman kỳ vọng cho $v_\pi$ và $q_\pi$, chỉ ra bước dùng tính Markov và bước dùng tính dừng (Định lý 03.21, Hệ quả 03.24; Bài tập 03.6, 03.7, 03.11).
5. Lập, giải và kiểm tra hệ $(I-\gamma P^\pi)v=r^\pi$ của một chính sách cho trước, nêu điều kiện để hệ có nghiệm duy nhất và đọc các giá trị $q_\pi$ thu được (Định lý 03.28, Thuật toán 03.29; Bài tập 03.8, 03.9, 03.13, 03.14).

<!-- note-topic-id: lec-03-part-09 -->
## Kiến thức tiên quyết

Số hiệu `03.k` chỉ ghi chú Bài 03, số hiệu `02.k` chỉ ghi chú Bài 02. Kết quả của Bài 02 được dẫn theo mục, kèm số hiệu ở những chỗ chương này dùng lại trực tiếp, và được phát biểu lại tại chỗ.

- **Vòng tương tác** (ghi chú Bài 02, Mục 1). Ở mỗi thời điểm rời rạc, tác tử (agent) nhận trạng thái và chọn hành động; một bước sau, môi trường trả về một phần thưởng (reward) là số thực và một trạng thái mới.
- **Trạng thái và tính Markov** (ghi chú Bài 02, Mục 2, Định nghĩa 02.5). Khi biết trạng thái hiện tại và hành động, lịch sử trước đó không cải thiện dự báo bước tới; Định nghĩa 03.2 phát biểu lại định nghĩa này với các tập hữu hạn của chương.
- **Chính sách** (ghi chú Bài 02, Mục 3). Chính sách xác định gán mỗi trạng thái một hành động; chính sách ngẫu nhiên gán một phân phối trên các hành động.
- **Lợi tức, giá trị, mô hình** (ghi chú Bài 02, Mục 4). Hệ số chiết khấu $\gamma\in[0,1]$ giảm trọng số của phần thưởng ở xa; giá trị là kỳ vọng của lợi tức; mô hình dự báo đồng thời trạng thái kế tiếp và phần thưởng. Bài 03 định nghĩa lại cả ba (Định nghĩa 03.4, 03.9, 03.15).
- **Xác suất có điều kiện và quy tắc nhân.** Với các biến ngẫu nhiên rời rạc và sự kiện $B$ có xác suất dương, $\Pr(X=x,Y=y\mid B)=\Pr(X=x\mid B)\Pr(Y=y\mid X=x,B)$ khi $\Pr(X=x,B)>0$. Áp dụng lặp lại, xác suất của một dãy biến bằng tích các xác suất có điều kiện của từng biến khi biết các biến trước nó.
- **Kỳ vọng toàn phần.** Nếu $Y$ nhận hữu hạn giá trị và $X$ khả tích, thì $\mathbb E[X\mid B]=\sum_y \Pr(Y=y\mid B)\,\mathbb E[X\mid Y=y,B]$, tổng lấy trên các $y$ có $\Pr(Y=y,B)>0$. Kỳ vọng có điều kiện tuyến tính, và hằng số đi ra ngoài kỳ vọng.
- **Hệ phương trình tuyến tính.** Ma trận vuông $A$ khả nghịch khi và chỉ khi $Ax=0$ chỉ có nghiệm $x=0$; khi đó $Ax=b$ có nghiệm duy nhất $x=A^{-1}b$. Phép khử Gauss giải hệ $n$ ẩn với số phép tính cỡ $n^3$.

## Bảng ký hiệu

Bảng chỉ gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một ví dụ, một chứng minh hay một tình huống được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$, $k$ | thời điểm quyết định; độ lệch thời gian | $\{0,1,2,\dots\}$ |
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái chưa kết thúc; tập đó thêm trạng thái kết thúc | hữu hạn, $\lvert\mathcal S\rvert=n$ |
| $\mathcal A(s)$ | tập hành động hợp lệ tại $s$ | hữu hạn, khác rỗng |
| $\mathcal R$ | tập các giá trị phần thưởng | tập con hữu hạn của $\mathbb R$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động, phần thưởng (biến ngẫu nhiên) | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathcal R$ |
| $s$, $a$, $s'$, $r$ | giá trị cụ thể của $S_t$, $A_t$, $S_{t+1}$, $R_{t+1}$ | như trên |
| $H_t$ | lịch sử tới thời điểm $t$ | dãy hữu hạn $(S_0,A_0,R_1,\dots,S_t)$ |
| $p(s',r\mid s,a)$ | hàm động lực | $[0,1]$ |
| $p(s'\mid s,a)$, $r(s,a)$ | xác suất chuyển trạng thái; thưởng kỳ vọng một bước | $[0,1]$; $\mathbb R$ |
| $T$ | thời điểm kết thúc lượt | $\{1,2,\dots\}\cup\{\infty\}$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $[0,1)$ với nhiệm vụ tiếp diễn |
| $G_t$ | lợi tức từ thời điểm $t$ | biến ngẫu nhiên thực |
| $M$ | cận của trị tuyệt đối phần thưởng | $M\ge0$ |
| $\pi(a\mid s)$ | chính sách Markov dừng | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $\mu$ | phân phối đầu, tức phân phối của $S_0$ | phân phối trên $\mathcal S$ |
| $\Pr_\pi$, $\mathbb E_\pi$ | xác suất, kỳ vọng khi hành động theo $\pi$ và phản hồi theo $p$ | — |
| $v_\pi(s)$ | giá trị trạng thái của $\pi$ | $\mathbb R$; bằng $0$ tại trạng thái kết thúc |
| $q_\pi(s,a)$ | giá trị hành động của $\pi$ | $\mathbb R$ |
| $P^\pi$, $r^\pi$ | ma trận chuyển và véc-tơ thưởng kỳ vọng dưới $\pi$ | $\mathbb R^{n\times n}$; $\mathbb R^n$ |
| $v$ | véc-tơ giá trị xếp theo thứ tự trạng thái | $\mathbb R^n$ |
| $I$, $\lVert x\rVert_\infty$ | ma trận đơn vị; chuẩn cực đại $\max_i\lvert x_i\rvert$ | $\mathbb R^{n\times n}$; $\ge0$ |
| $\mathrm H$, $\mathrm L$ | trạng thái pin cao, pin thấp của robot | nhãn, không phải biến |
| $\mathrm{tim}$, $\mathrm{cho}$, $\mathrm{sac}$ | hành động Tìm, Chờ, Sạc của robot | nhãn, không phải biến |

Chữ hoa ($S_t$, $A_t$, $R_{t+1}$, $G_t$) là biến ngẫu nhiên; chữ thường là giá trị cụ thể. Phần thưởng mang chỉ số $t+1$ vì nó đến sau hành động $A_t$, cùng với trạng thái $S_{t+1}$.

Giáo trình *Học máy thống kê* viết quá trình quyết định Markov thành bộ $\langle S,A,T,R,\gamma\rangle$. Trong chương này, $T(s,a,s')$ của giáo trình đó ứng với $p(s'\mid s,a)$ (chữ $T$ của chương chỉ thời điểm kết thúc), $V^\pi$ ứng với $v_\pi$, và $\gamma$ đứng ngoài bộ mô tả môi trường (Định nghĩa 03.7). Dấu thập phân là dấu phẩy. Các xác suất và mức thưởng của robot là số liệu sư phạm tự xây dựng.

## Bản đồ chủ đề

Mỗi chủ đề có một mã `note-topic-id` để đối chiếu với mạch tương ứng của bài giảng; mục cầu nối và bổ sung ghi khoảng trống mà chúng lấp.

| Nhóm | Chủ đề và mã | Vai trò trong mạch | Kết nối vào | Kết nối ra | Mục | Nguồn |
|---|---|---|---|---|---|---|
| cốt lõi | Một bước và tính Markov, `lec-03-part-01` | mô tả robot bằng dữ liệu; giả thiết trạng thái đủ thông tin | vòng tương tác (Bài 02) | điều kiện để bảng một bước đủ mô tả môi trường | 1.1–1.2 (mạch 2) | Bài giảng gốc tr. 29; Sutton và Barto §3.1, tr. 48–50 |
| cốt lõi | Hàm động lực và MDP hữu hạn, `lec-03-part-02` | đóng gói môi trường thành $(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p)$ | Định nghĩa 03.2 | $p(s'\mid s,a)$, $r(s,a)$ | 1.3–1.5 (mạch 2) | Bài giảng gốc tr. 49; Sutton và Barto (3.2)–(3.5), ví dụ 3.3, tr. 48–53 |
| cốt lõi | Lợi tức chiết khấu, `lec-03-part-03` | gộp chuỗi phần thưởng thành một số hữu hạn | $R_{t+1}$ | $G_t$ và cận $M/(1-\gamma)$ | 2 (mạch 3) | Bài giảng gốc tr. 36–38; Sutton và Barto §3.3–3.4, tr. 54–57 |
| cốt lõi | Chính sách, $v_\pi$, $q_\pi$, `lec-03-part-04` | cố định cách chọn hành động để kỳ vọng có nghĩa | $p$, $G_t$ | ẩn số của phương trình Bellman | 3 (mạch 4) | Bài giảng gốc tr. 39, 52–53; Sutton và Barto §3.5, tr. 58 |
| cốt lõi | Phương trình Bellman kỳ vọng, `lec-03-part-05` | thay kỳ vọng trên vô hạn quỹ đạo bằng một phương trình mỗi trạng thái | $G_t=R_{t+1}+\gamma G_{t+1}$, tính Markov | hệ tuyến tính của Mục 5 | 4 (mạch 5) | Bài giảng gốc tr. 44–46, 56–57; Sutton và Barto (3.14), bài tập 3.12–3.19, tr. 58–62 |
| cốt lõi | Đánh giá chính sách bằng hệ tuyến tính, `lec-03-part-06` | tính giá trị bằng số của một chính sách cho trước | Định lý 03.21 | $v_\pi=(I-\gamma P^\pi)^{-1}r^\pi$, nền cho Bài 04 | 5 (mạch 6) | Bài giảng gốc tr. 30, 34, 47–48; Bài tập tuần 2, bài 3–4; Sutton và Barto tr. 60 |
| cốt lõi | Tổng kết chương, `lec-03-part-08` | đối chiếu với vấn đề mở đầu; giả thiết không được bỏ | Mục 1–5 | Bài 04, Bài 05–06 | Tóm tắt, Bài tập củng cố (mạch 7) | Bài giảng gốc tr. 58 |
| cầu nối | Xác suất có điều kiện và kỳ vọng toàn phần, `lec-03-part-09` | công cụ của Mệnh đề 03.14 và Bổ đề 03.19; khoảng trống: phép tách kỳ vọng cần căn cứ | xác suất ở học phần trước | phép tách hai tầng kỳ vọng | Kiến thức tiên quyết; dùng ở 3.1, 4.3 | Bài giảng gốc tr. 58 (dẫn tài liệu đọc về xác suất: D. P. Bertsekas và J. N. Tsitsiklis, *Introduction to Probability*, chương 7, và ghi chú xác suất CS229) |
| bổ sung | Tình huống lưới 5×5 và CartPole rời rạc hóa, `lec-03-part-07` | áp dụng Thuật toán 03.29; khoảng trống: robot chỉ có hai trạng thái và thỏa mọi giả thiết | Định lý 03.28, Thuật toán 03.29 | notebook CartPole của Bài 04 | Tình huống áp dụng | Sutton và Barto ví dụ 3.5, tr. 60; notebook `thuc-hanh-cartpole-quy-hoach-dong.ipynb` |
| đọc thêm | Tài liệu đọc thêm, `lec-03-part-10` | nguồn cho chứng minh và mở rộng ngoài chương | Định lý 03.21, 03.28 | giá trị tối ưu (Sutton và Barto §3.6); dựng trạng thái Markov (chương 17) | Hướng dẫn đọc thêm | Sutton và Barto (2018); Puterman (1994) §6.1; Bertsekas (2019) |

## 1. Trạng thái Markov và mô hình môi trường

Trong Bài 02, chúng ta đã định nghĩa giá trị của một trạng thái dưới một chính sách cố định là kỳ vọng của lợi tức từ trạng thái đó (ghi chú Bài 02, Mục 4). Định nghĩa này nói giá trị là gì nhưng chưa cho cách tính. Tính theo định nghĩa nghĩa là liệt kê mọi quỹ đạo (trajectory), nhân lợi tức của mỗi quỹ đạo với xác suất của nó rồi cộng lại; với nhiệm vụ không bao giờ kết thúc, số quỹ đạo là vô hạn và mỗi quỹ đạo dài vô hạn.

Bài toán cụ thể của chương là robot thu gom lon hai mức pin. Ở pin thấp, Chờ cho ngay $1$, còn Sạc cho $0$ nhưng đưa robot về pin cao, nơi Tìm luôn cho $2$. Muốn so sánh hai lựa chọn, chúng ta cần một con số tổng hợp toàn bộ tương lai của mỗi cách hành động.

Chúng ta xây dựng con số đó qua năm mục, theo hình dưới, và kết thúc bằng giá trị $v_\pi(\mathrm H)=13/4$, $v_\pi(\mathrm L)=7/4$ của robot dưới một chính sách cụ thể.

![Sáu khối nối bằng mũi tên. Hàng trên: Mục 1, mô hình với trạng thái Markov và hàm động lực p(s', r | s, a); mũi tên "chuỗi thưởng" sang Mục 2, lợi tức G_t = R_{t+1} + γR_{t+2} + … với cận |G_t| ≤ M/(1 − γ); mũi tên "lấy kỳ vọng" sang Mục 3, chính sách π(a | s), giá trị v_π(s) và q_π(s, a). Mũi tên "tách bước đầu, dùng tính Markov" xuống hàng dưới: Mục 4, phương trình Bellman v_π(s) = Σ π Σ p [r + γ v_π(s')], mỗi trạng thái một phương trình; mũi tên "S hữu hạn, γ < 1" sang Mục 5, hệ (I − γP^π) v = r^π có nghiệm duy nhất khi γ < 1; mũi tên "giải hệ hai ẩn" sang khối viền đứt "Robot hai mức pin" với v_π(H) = 13/4, v_π(L) = 7/4.](img/lec-03/chapter-structure.svg)

Mỗi khối của hình ứng với một mục, và nhãn trên mũi tên ghi thao tác hoặc giả thiết cho phép đi sang khối sau. Hai giả thiết quyết định nằm ở hàng dưới: tính Markov cho phép tách bước đầu (Định lý 03.21), còn tập trạng thái hữu hạn cùng $\gamma<1$ cho phép giải hệ (Định lý 03.28). Khối viền đứt ghi kết quả số của ví dụ xuyên suốt.

<!-- note-topic-id: lec-03-part-01 -->
### 1.1 Robot thu gom lon và một bước tương tác

Để có thể tính, mô tả bằng lời của robot phải trở thành dữ liệu: ở mỗi bước, robot đang ở mức pin nào, chọn gì, nhận bao nhiêu và chuyển sang đâu.

::: example Ví dụ 03.1 (Robot thu gom lon hai mức pin)
**Môi trường.** Một robot thu gom lon rỗng trong văn phòng. Tác tử điều khiển robot chỉ phân biệt hai mức pin: pin cao $\mathrm H$ và pin thấp $\mathrm L$. Mỗi bước là một chu kỳ quyết định, không nhất thiết dài bằng nhau theo thời gian thực.

**Hành động.** Ở pin cao, robot chọn Tìm ($\mathrm{tim}$) hoặc Chờ ($\mathrm{cho}$). Ở pin thấp, robot chọn Tìm, Chờ hoặc Sạc ($\mathrm{sac}$).

**Phản hồi.**

- Tìm từ $\mathrm H$: phần thưởng $2$; pin giữ ở $\mathrm H$ với xác suất $1/2$, xuống $\mathrm L$ với xác suất $1/2$.
- Chờ từ $\mathrm H$: phần thưởng $1$; pin giữ ở $\mathrm H$.
- Tìm từ $\mathrm L$: với xác suất $1/2$ pin còn đủ, robot nhận $2$ và vẫn ở $\mathrm L$; với xác suất $1/2$ pin cạn, robot được cứu hộ, nhận $-3$ và được sạc lại về $\mathrm H$ ngay trong bước đó.
- Chờ từ $\mathrm L$: phần thưởng $1$; pin giữ ở $\mathrm L$.
- Sạc từ $\mathrm L$: phần thưởng $0$; pin về $\mathrm H$.

**Nhiệm vụ.** Robot hoạt động liên tục; cứu hộ và sạc đều không dừng công việc.

**Nguồn.** Khung ví dụ là ví dụ 3.3 của Sutton và Barto (2018, tr. 52–53); hai tham số xác suất của ví dụ gốc đều được chọn bằng $1/2$, và các mức thưởng Tìm $2$, Chờ $1$ là số liệu sư phạm tự xây dựng.
:::

![Robot thu gom lon ở mức pin thấp với ba lựa chọn: Tìm, Chờ, Sạc.](img/lec-03/robot-p01-recycling-robot-low.svg)

Hình trên đặt robot ở pin thấp với ba lựa chọn, khác nhau ở phần thưởng nhận ngay và ở mức pin của bước sau.

Mỗi lần robot thực hiện một bước tạo ra một bản ghi bốn thành phần. Ví dụ sau ghi lại một bước và quy ước chỉ số thời gian.

::: example Ví dụ 03.2 (Một bước của robot)
**Dữ kiện.** Tại thời điểm $t$, robot ở pin cao, chọn Tìm, nhận phần thưởng $2$ và pin xuống thấp (Ví dụ 03.1 cho phép phản hồi này với xác suất $1/2$).

**Bản ghi.**

$$
(S_t,\,A_t,\,R_{t+1},\,S_{t+1})=(\mathrm H,\ \mathrm{tim},\ 2,\ \mathrm L).
$$

**Đọc chỉ số.** Trạng thái và hành động mang chỉ số $t$ vì chúng có trước khi robot hành động. Phần thưởng và trạng thái mới mang chỉ số $t+1$ vì môi trường trả về chúng cùng lúc, sau hành động.

**Kiểm tra lại.** Nếu bước kế tiếp robot ở $\mathrm L$ chọn Chờ, bản ghi tiếp theo là $(S_{t+1},A_{t+1},R_{t+2},S_{t+2})=(\mathrm L,\mathrm{cho},1,\mathrm L)$; hai bản ghi nối nhau ở $S_{t+1}=\mathrm L$.
:::

Quy ước $R_{t+1}$ là của Sutton và Barto (2018, tr. 48); một số tài liệu khác viết $R_t$. Nối các bản ghi lại, ta được khái niệm sau.

::: definition Định nghĩa 03.1 (Quỹ đạo và lịch sử)
Xét tác tử và môi trường tương tác tại các thời điểm rời rạc $t=0,1,2,\dots$. Tập trạng thái $\mathcal S^+$ gồm tập $\mathcal S$ các trạng thái chưa kết thúc và, với nhiệm vụ có kết thúc, các trạng thái kết thúc (Định nghĩa 03.8). Tại thời điểm $t$, trạng thái là biến ngẫu nhiên $S_t$ nhận giá trị trong $\mathcal S^+$, hành động là biến ngẫu nhiên $A_t$ nhận giá trị trong tập hành động hợp lệ $\mathcal A(S_t)$, và phần thưởng của chuyển từ $t$ sang $t+1$ là biến ngẫu nhiên $R_{t+1}$ nhận giá trị trong tập hữu hạn $\mathcal R\subset\mathbb R$.

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

Dãy (1.1) xen kẽ trạng thái, hành động, phần thưởng theo đúng thứ tự xảy ra. Lịch sử $H_t$ dừng ở $S_t$ và chưa chứa $A_t$, vì đó là thông tin có trước khi tác tử chọn hành động tại $t$. Trong Ví dụ 03.2, nếu robot bắt đầu ở $t=0$ thì $H_1=(\mathrm H,\mathrm{tim},2,\mathrm L)$.

Định nghĩa 03.1 hình thức hóa vòng tương tác của ghi chú Bài 02, Mục 1, và thêm hai điều: tập hành động có thể phụ thuộc trạng thái, và tập phần thưởng hữu hạn. Ở robot, $\mathcal A(\mathrm H)$ có hai phần tử còn $\mathcal A(\mathrm L)$ có ba. Giả thiết hữu hạn của $\mathcal R$ làm mọi kỳ vọng một bước là tổng hữu hạn.

### 1.2 Tính Markov

Tại pin thấp, robot chuẩn bị Tìm. Để dự báo phản hồi, chúng ta muốn chỉ dùng mức pin hiện tại, không cần biết robot đã đến pin thấp bằng cách nào. Nếu cách đến pin thấp có ảnh hưởng, mọi bảng xác suất phải đánh chỉ số theo cả lịch sử, và số lịch sử tăng theo cấp số nhân với $t$.

Một cách trực quan, trạng thái là bản tóm tắt của quá khứ. Bản tóm tắt tốt giữ lại mọi chi tiết của quá khứ có ảnh hưởng tới phản hồi sắp tới và bỏ đi phần còn lại. Đây mới là mô tả bằng lời; định nghĩa chính xác viết điều này thành đẳng thức giữa hai phân phối có điều kiện.

::: example Ví dụ 03.3 (Hai lịch sử, cùng trạng thái hiện tại)
**Dữ kiện.** Robot của Ví dụ 03.1. Robot thứ nhất có lịch sử $(\mathrm H,\mathrm{tim},2,\mathrm L)$: vừa Tìm từ pin cao và xuống pin thấp. Robot thứ hai có lịch sử $(\mathrm L,\mathrm{cho},1,\mathrm L)$: vừa Chờ ở pin thấp. Cả hai đang ở $\mathrm L$ và chọn Tìm.

**Phản hồi.** Theo Ví dụ 03.1, phản hồi của Tìm từ $\mathrm L$ chỉ phụ thuộc mức pin: với cả hai robot, $(S_{t+1},R_{t+1})=(\mathrm L,2)$ với xác suất $1/2$ và $(\mathrm H,-3)$ với xác suất $1/2$.

**Kết luận.** Hai lịch sử khác nhau cho cùng một phân phối phản hồi; mức pin là trạng thái đủ thông tin trong mô hình này.

**Kiểm tra lại.** Ở cả hai lịch sử, hai xác suất cộng lại bằng $1$.
:::

::: definition Định nghĩa 03.2 (Tính Markov)
Trạng thái $S_t$ có tính Markov (Markov property) nếu với mọi $t\ge0$, mọi lịch sử $h_t$ kết thúc ở trạng thái $s$, mọi hành động $a\in\mathcal A(s)$ sao cho $\Pr(H_t=h_t,A_t=a)>0$, và mọi $s'\in\mathcal S^+$, $r\in\mathcal R$,

$$
\Pr(S_{t+1}=s',R_{t+1}=r\mid H_t=h_t,A_t=a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a).
\tag{1.2}
$$
:::

Vế trái của (1.2) dùng toàn bộ lịch sử, vế phải chỉ dùng trạng thái cuối và hành động hiện tại; đẳng thức phải đúng với mọi lịch sử có xác suất dương. Ví dụ 03.3 là một trường hợp của (1.2): hai lịch sử kết thúc ở $\mathrm L$ với hành động Tìm cho cùng một phân phối phản hồi.

Phản ví dụ sau cho thấy một robot có thể mất tính Markov khi trạng thái bỏ sót thông tin.

::: example Ví dụ 03.4 (Trạng thái thiếu phòng làm việc)
**Dữ kiện.** Số liệu sư phạm tự xây dựng. Robot luôn ở pin thấp và chỉ Chờ. Robot làm việc luân phiên ở hai phòng: nếu bước này ở phòng 1 thì bước sau ở phòng 2, và ngược lại. Chờ ở phòng 1 cho phần thưởng $1$, Chờ ở phòng 2 cho $0$. Phòng lúc $t=0$ được chọn ngẫu nhiên, mỗi phòng xác suất $1/2$. Trạng thái chỉ ghi mức pin, nên luôn bằng $\mathrm L$.

**Hai lịch sử.** Xét $t=1$ và hai lịch sử $h=(\mathrm L,\mathrm{cho},1,\mathrm L)$, $h'=(\mathrm L,\mathrm{cho},0,\mathrm L)$.

- Với $h$, phần thưởng $R_1=1$ cho biết lúc $t=0$ robot ở phòng 1, nên lúc $t=1$ robot ở phòng 2 và $\Pr(R_2=1\mid H_1=h,A_1=\mathrm{cho})=0$.
- Với $h'$, phần thưởng $R_1=0$ cho biết lúc $t=0$ robot ở phòng 2, nên $\Pr(R_2=1\mid H_1=h',A_1=\mathrm{cho})=1$.

**Kết luận.** Hai lịch sử kết thúc ở cùng trạng thái $\mathrm L$ nhưng cho hai xác suất $0$ và $1$. Vế phải của (1.2) là một số duy nhất $\Pr(R_2=1\mid S_1=\mathrm L,A_1=\mathrm{cho})$, nên không thể bằng cả hai; trạng thái "mức pin" không có tính Markov.

**Sửa.** Lấy trạng thái là cặp (mức pin, phòng). Phòng hiện tại quyết định phần thưởng và phòng kế tiếp, nên lịch sử không cho thêm thông tin và (1.2) thỏa.

**Kiểm tra lại.** Mỗi lịch sử có xác suất $1/2$, nên cả hai thuộc phạm vi của Định nghĩa 03.2.
:::

Sutton và Barto (2018, tr. 49) coi tính Markov là một hạn chế đặt lên trạng thái: trạng thái phải chứa mọi khía cạnh của quá khứ có ảnh hưởng tới tương lai.

::: remark Nhận xét 03.3 (Trạng thái đủ thông tin và các cách hiểu sai)
- Tính Markov thuộc về biểu diễn trạng thái. Cùng một hệ vật lý có thể có biểu diễn Markov và biểu diễn không Markov, như mức pin so với cặp (mức pin, phòng) ở Ví dụ 03.4.
- Khi một biểu diễn không Markov, có hai cách sửa: thêm vào trạng thái phần thông tin bị thiếu, như phòng ở Ví dụ 03.4; hoặc dùng làm trạng thái một tóm tắt của lịch sử đủ để dự báo bước tới, chẳng hạn hai phần thưởng gần nhất. Cách thứ hai làm số trạng thái tăng theo số tổ hợp lịch sử phải phân biệt.
- Trạng thái có tính Markov chưa có nghĩa là đã biết các con số xác suất. Tính Markov nói phân phối phản hồi chỉ phụ thuộc $(s,a)$; nó không cho biết phân phối đó bằng bao nhiêu.
- Tính Markov không nói phản hồi là tất định: Tìm từ $\mathrm L$ vẫn có hai kết quả ngẫu nhiên.
:::

Định nghĩa 03.2 khớp Định nghĩa 02.5 của ghi chú Bài 02 trong trường hợp các tập hữu hạn; định nghĩa ấy còn đòi đẳng thức với mọi chính sách của tác tử. Trong chương này, định nghĩa trở thành giả thiết dùng trong chứng minh: ở tiểu mục 1.3, nó cho phép mô tả môi trường bằng một bảng không phụ thuộc lịch sử; ở Bổ đề 03.20, nó cho phép thay kỳ vọng của phần tương lai bằng giá trị của trạng thái kế tiếp.

::: exercise Bài tập 03.1
**Dữ kiện.** (a) Robot của Ví dụ 03.1 ghi được bản ghi $(\mathrm L,\mathrm{cho},1,\mathrm L)$ ở bước bắt đầu tại thời điểm $t=4$. (b) Số liệu sư phạm tự xây dựng: một robot chỉ hoạt động ở pin cao, pin luôn giữ ở $\mathrm H$, và ở mọi bước tác tử chọn Tìm hoặc Chờ, mỗi hành động xác suất $1/2$. Robot được đặt cố định suốt đời ở một trong hai vị trí, mỗi vị trí xác suất $1/2$, và trạng thái không ghi vị trí. Ở vị trí gần cửa, Tìm luôn cho phần thưởng $2$. Ở vị trí xa cửa, Tìm cho $2$ hoặc $0$, mỗi kết quả xác suất $1/2$. Chờ ở cả hai vị trí cho $1$.

**Yêu cầu.** (a) Viết bản ghi bằng các biến ngẫu nhiên có chỉ số thời gian. (b) Xét hai lịch sử $h=(\mathrm H,\mathrm{tim},0,\mathrm H)$ và $h'=(\mathrm H,\mathrm{cho},1,\mathrm H)$ tại $t=1$. Tính $\Pr(R_2=0\mid H_1=h,A_1=\mathrm{tim})$ và $\Pr(R_2=0\mid H_1=h',A_1=\mathrm{tim})$, rồi kết luận trạng thái "mức pin" có tính Markov hay không.
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

Với $h'$, Chờ cho $1$ ở cả hai vị trí, nên lịch sử không cho thông tin về vị trí; xác suất ở vị trí xa cửa vẫn là $1/2$. Theo kỳ vọng toàn phần theo vị trí,

$$
\Pr(R_2=0\mid H_1=h',A_1=\mathrm{tim})=\tfrac12\cdot\tfrac12+\tfrac12\cdot0=\tfrac14 .
$$

Hai lịch sử kết thúc ở cùng trạng thái $\mathrm H$ với cùng hành động Tìm nhưng cho hai xác suất $1/2$ và $1/4$, nên (1.2) không thể thỏa với cả hai; trạng thái "mức pin" không có tính Markov. Thêm vị trí vào trạng thái khôi phục tính Markov.

**Kiểm tra lại.** Theo chính sách trong Dữ kiện, $h$ có xác suất $\tfrac12\cdot\tfrac12\cdot\tfrac12=\tfrac18$ (chọn Tìm, ở vị trí xa cửa, nhận $0$) và $h'$ có xác suất $\tfrac12$ (chọn Chờ); cả hai dương.
:::

<!-- note-topic-id: lec-03-part-02 -->
### 1.3 Hàm động lực

Một bản ghi như Ví dụ 03.2 không cho biết phản hồi đó xảy ra thường xuyên đến mức nào, cũng không cho biết những phản hồi nào khác có thể xảy ra. Để dự báo, chúng ta cần liệt kê mọi phản hồi của mỗi cặp trạng thái–hành động cùng xác suất của chúng. Nhờ tính Markov, bảng liệt kê chỉ cần đánh chỉ số theo cặp $(s,a)$.

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

Một cách trực quan, bảng phản hồi là một họ phân phối xác suất, mỗi cặp $(s,a)$ một phân phối trên các cặp $(s',r)$. Định nghĩa sau gọi tên đối tượng này và ghi rõ các giả thiết đi kèm.

::: definition Định nghĩa 03.4 (Hàm động lực)
Giả sử $\mathcal S^+$, mọi $\mathcal A(s)$ và $\mathcal R$ là tập hữu hạn, trạng thái có tính Markov (Định nghĩa 03.2), và xác suất ở vế phải của (1.2) không phụ thuộc thời điểm $t$. Hàm động lực (dynamics function) của môi trường là hàm $p$ xác định với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$, $s'\in\mathcal S^+$, $r\in\mathcal R$, thỏa

$$
p(s',r\mid s,a)\ge0,\qquad \sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)=1\quad\text{với mọi } s\in\mathcal S,\ a\in\mathcal A(s),
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

nghĩa là từ pin thấp, khi chọn Tìm, robot về pin cao kèm phần thưởng $-3$ với xác suất $1/2$. Các bộ $(s',r)$ không có trong bảng có $p=0$, chẳng hạn $p(\mathrm H,2\mid\mathrm L,\mathrm{tim})=0$. Sutton và Barto (2018, (3.2)) viết cùng hàm với chỉ số $t-1$ và $t$; ở đây ta dịch sang $t$ và $t+1$ cho khớp quy ước $R_{t+1}$.

Hàm $p$ không mang chỉ số $t$. Đây là một giả thiết riêng, đứng bên cạnh tính Markov.

::: remark Nhận xét 03.5 (Tính dừng khác tính Markov)
- Tính Markov nói phản hồi chỉ phụ thuộc $(S_t,A_t)$, không phụ thuộc phần còn lại của lịch sử; tính dừng nói quy luật đó giống nhau ở mọi thời điểm. Một robot có pin lão hóa theo năm tháng có thể có trạng thái Markov nhưng hàm động lực thay đổi theo $t$.
- Trạng thái kế tiếp và phần thưởng được rút cùng nhau từ $p(\cdot,\cdot\mid s,a)$, không có giả thiết hai đại lượng độc lập. Vì Sutton và Barto (2018, ví dụ 3.3) chỉ cho thưởng kỳ vọng trên mỗi nhánh, Ví dụ 03.1 thêm giả thiết phần thưởng cố định trên mỗi nhánh để xác định được $p$.
:::

Một mẫu chuyển như Ví dụ 03.2 là một kết quả đã rút ra; hàm động lực là quy luật sinh ra mọi kết quả đó, tức mô hình môi trường của ghi chú Bài 02, Mục 4. Các phương pháp của Bài 04 cần $p$, còn các phương pháp của Bài 05–06 chỉ dùng mẫu chuyển.

**Trong thực hành.** Môi trường mô phỏng như Gymnasium chỉ cho mẫu chuyển: gọi hàm bước với một hành động, chúng ta nhận một trạng thái mới và một phần thưởng, không nhận bảng $p$. Muốn có bảng, phải ước lượng.

Notebook CartPole của Bài 04 chia trạng thái liên tục thành $324$ ô, rồi với mỗi ô và mỗi hành động lấy $N_{\text{mẫu}}=200$ trạng thái đều trong ô, chạy một bước và đếm ô kế tiếp. Kết quả là mảng $\hat p(s'\mid s,a)$ cỡ $(2,324,325)$: hai hành động, $324$ ô hiện tại, và $325$ cột gồm $324$ ô cùng một trạng thái kết thúc. Mảng thưởng kỳ vọng ước lượng bằng $1$ ở mọi ô vì Gymnasium trả phần thưởng $+1$ ở mọi bước (một lần chạy đã nhúng trong notebook). Tình huống 03.2 xét bảng $\hat p$ này có thỏa Định nghĩa 03.2 hay không.

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

Hai phép tính của Ví dụ 03.6 là phép cộng theo hàng của bảng với hai cách nhóm khác nhau. Mệnh đề sau viết chúng cho mọi cặp $(s,a)$.

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

Công thức (1.5) gom các hàng có cùng trạng thái kế tiếp; (1.6) lấy trung bình phần thưởng với trọng số là xác suất của hàng. Với cặp $(\mathrm L,\mathrm{tim})$, ta được lại hai con số của Ví dụ 03.6. Ký hiệu ba đối số $p(s'\mid s,a)$ là một lạm dụng ký hiệu có chủ ý của Sutton và Barto (2018, (3.4)).

Nhầm lẫn thường gặp là coi $r(s,a)$ là phần thưởng robot nhận được; đó là kỳ vọng của biến ngẫu nhiên $R_{t+1}$. Hai rút gọn (1.5), (1.6) đủ cho phương trình Bellman (Mệnh đề 03.22) nhưng không đủ để mô phỏng phần thưởng.

### 1.5 Quá trình quyết định Markov hữu hạn

Các thành phần mô tả môi trường đã đủ: tập trạng thái, tập hành động theo trạng thái, tập phần thưởng và hàm động lực. Định nghĩa sau gom chúng thành một đối tượng.

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

Định nghĩa đặt tính Markov và tính dừng vào ngay quy tắc sinh quỹ đạo: phản hồi chỉ phụ thuộc trạng thái cuối và hành động, và cùng một hàm $p$ dùng cho mọi $t$. Bộ $\mathcal M$ chỉ mô tả môi trường; nó chưa nói hành động được chọn thế nào (Mục 3) và chuỗi phần thưởng được gộp thế nào (Mục 2). Với robot, $\mathcal S^+=\mathcal S=\{\mathrm H,\mathrm L\}$ (không có trạng thái kết thúc), $\mathcal A(\mathrm H)=\{\mathrm{tim},\mathrm{cho}\}$, $\mathcal A(\mathrm L)=\{\mathrm{tim},\mathrm{cho},\mathrm{sac}\}$, $\mathcal R=\{-3,0,1,2\}$, và $p$ là bảy hàng của Ví dụ 03.5.

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

Như vậy, trạng thái có tính Markov (Định nghĩa 03.2) cho phép mô tả phản hồi bằng hàm động lực $p$ không phụ thuộc lịch sử (Định nghĩa 03.4); từ $p$ suy ra xác suất chuyển và thưởng kỳ vọng (Mệnh đề 03.6), và bốn thành phần ghép thành MDP hữu hạn (Định nghĩa 03.7). Tuy nhiên, $p$ chỉ nói về một bước, nên chưa so sánh được hậu quả lâu dài của các lựa chọn. Trong Mục 2, chúng ta gộp cả chuỗi phần thưởng thành một số.

<!-- note-topic-id: lec-03-part-03 -->
## 2. Lợi tức chiết khấu

Xếp hạng theo phần thưởng một bước đặt Chờ lên đầu ở pin thấp, nhưng sau Sạc robot ở pin cao, nơi mỗi lần Tìm cho $2$. Để tính đến các bước sau, chúng ta cần gộp cả chuỗi phần thưởng thành một số. Cộng thẳng không dùng được cho robot: nếu robot Chờ mãi ở pin thấp, tổng $1+1+1+\cdots$ tăng vô hạn, và mọi cách hành động có phần thưởng dương đều cho tổng vô hạn như nhau. Trong mục này, chúng ta xây dựng lợi tức chiết khấu, một tổng có trọng số luôn hữu hạn khi phần thưởng bị chặn.

### 2.1 Chuỗi phần thưởng và trọng số theo thời gian

Một cách trực quan, phần thưởng nhận sớm đáng giá hơn phần thưởng nhận muộn, và một phần thưởng ở rất xa trong tương lai gần như không ảnh hưởng tới quyết định hiện tại. Cách đơn giản nhất để thể hiện điều này là nhân phần thưởng của bước thứ $k$ sau hiện tại với một trọng số giảm theo cấp số nhân. Đây chưa phải định nghĩa; ví dụ sau dùng trọng số giảm một nửa sau mỗi bước.

::: example Ví dụ 03.7 (Hai dãy phần thưởng ba bước từ pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1 bắt đầu ở $\mathrm L$. Trọng số của ba bước đầu là $1$, $1/2$, $1/4$.

- Dãy thứ nhất: robot Sạc (phần thưởng $0$, về $\mathrm H$), rồi Tìm từ $\mathrm H$ và pin giữ ở $\mathrm H$ (phần thưởng $2$), rồi Tìm từ $\mathrm H$ lần nữa (phần thưởng $2$). Dãy phần thưởng là $(0,2,2)$; đây là một đường có xác suất dương, vì lần Tìm đầu cũng có thể đưa robot xuống $\mathrm L$.
- Dãy thứ hai: robot Chờ ba lần ở $\mathrm L$; dãy phần thưởng là $(1,1,1)$.

**Tính.**

$$
\begin{aligned}
0+\tfrac12\cdot2+\tfrac14\cdot2&=\tfrac32,\\
1+\tfrac12\cdot1+\tfrac14\cdot1&=\tfrac74.
\end{aligned}
$$

**Diễn giải.** Tổng không trọng số của dãy thứ nhất lớn hơn ($4$ so với $3$), nhưng tổng có trọng số của dãy thứ hai lớn hơn. Phần thưởng $0$ của dãy thứ nhất rơi vào bước có trọng số lớn nhất, còn hai phần thưởng $2$ rơi vào hai bước có trọng số nhỏ hơn.

**Kiểm tra lại.** Hai con số chỉ so sánh hai đoạn ba bước cụ thể. Chúng không cho biết cách hành động nào tốt hơn về lâu dài, vì phần sau bước thứ ba và các nhánh ngẫu nhiên khác đều bị bỏ qua.
:::

### 2.2 Lượt, nhiệm vụ và lợi tức

Trước khi viết công thức tổng quát, chúng ta cần biết chuỗi phần thưởng dài bao nhiêu. Mê cung của Bài 02 kết thúc khi tác tử tới đích; robot thu gom lon không có điểm dừng tự nhiên. Hai trường hợp dẫn tới hai cách viết tổng, và một quy ước gộp chúng làm một.

::: definition Định nghĩa 03.8 (Lượt, nhiệm vụ có kết thúc và nhiệm vụ tiếp diễn)
Một nhiệm vụ là nhiệm vụ có kết thúc (episodic task) nếu tương tác chia thành các lượt (episode): mỗi lượt bắt đầu từ một trạng thái đầu và dừng khi tới một trạng thái kết thúc (terminal state) tại thời điểm $T<\infty$; $T$ là biến ngẫu nhiên và có thể khác nhau giữa các lượt. Khi đó $\mathcal S$ ký hiệu tập trạng thái chưa kết thúc và $\mathcal S^+$ ký hiệu $\mathcal S$ cùng các trạng thái kết thúc.

Một nhiệm vụ là nhiệm vụ tiếp diễn (continuing task) nếu tương tác không chia thành lượt; khi đó quy ước $T=\infty$ và $\mathcal S^+=\mathcal S$.
:::

Robot của Ví dụ 03.1 là nhiệm vụ tiếp diễn: cứu hộ và sạc chỉ đổi mức pin, không đóng lượt. Một lần đi mê cung hay một lần giữ cột trong CartPole là nhiệm vụ có kết thúc. Kết thúc một lượt là sự kiện của môi trường, khác việc dừng một thuật toán học chạy qua nhiều lượt.

Với hai loại nhiệm vụ đã phân biệt, chúng ta viết lại phép tính của Ví dụ 03.7 cho mọi dãy phần thưởng, với trọng số $\gamma^k$ thay cho $(1/2)^k$.

::: definition Định nghĩa 03.9 (Lợi tức chiết khấu)
Cho hệ số chiết khấu (discount factor) $\gamma\in[0,1]$ và thời điểm $t<T$. Lợi tức (return) từ thời điểm $t$ là

$$
G_t=\sum_{k=t+1}^{T}\gamma^{\,k-t-1}R_k=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots,
\tag{2.1}
$$

trong đó tổng có hữu hạn số hạng khi $T<\infty$, và là tổng của một chuỗi khi $T=\infty$; trường hợp $T=\infty$ chỉ dùng với $\gamma<1$. Quy ước $G_T=0$ khi $T<\infty$.
:::

Công thức (2.1) cộng mọi phần thưởng đến sau thời điểm $t$, bắt đầu từ $R_{t+1}$ với trọng số $\gamma^0=1$; phần thưởng đến sau $k$ bước nữa, $R_{t+k+1}$, mang trọng số $\gamma^k$. Lợi tức là biến ngẫu nhiên, vì mỗi quỹ đạo cho một dãy phần thưởng khác.

Quy ước $G_T=0$ nói rằng sau khi kết thúc không còn phần thưởng nào; $R_T$ vẫn nằm trong $G_{T-1}$. Với $\gamma=1/2$, ba số hạng đầu của (2.1) là đúng phép tính của Ví dụ 03.7, nên $3/2$ và $7/4$ là lợi tức cắt sau ba bước. Định nghĩa 03.9 trùng với lợi tức của ghi chú Bài 02, Mục 4.

Sutton và Barto (2018, §3.4) gộp hai loại nhiệm vụ bằng một quy ước: coi trạng thái kết thúc là trạng thái hấp thụ, chỉ chuyển về chính nó với phần thưởng $0$. Nhận xét sau ghi lại quy ước này.

::: remark Nhận xét 03.10 (Quy ước trạng thái hấp thụ)
Với nhiệm vụ có kết thúc tại $T<\infty$, đặt $R_k=0$ với mọi $k>T$. Khi đó, đổi chỉ số $j=k-t-1$ trong (2.1) và dùng $R_{t+j+1}=0$ với $j\ge T-t$, ta có

$$
\sum_{k=t+1}^{T}\gamma^{\,k-t-1}R_k=\sum_{j=0}^{\infty}\gamma^{\,j}R_{t+j+1}
$$

với mọi $\gamma\in[0,1]$, vì vế phải chỉ có hữu hạn số hạng khác $0$. Tương đương, sau thời điểm $T$ quá trình ở lại trạng thái kết thúc, mọi bước có phần thưởng $0$, và tại trạng thái kết thúc chỉ có một hành động giả. Từ đây, mọi phát biểu về đoạn quỹ đạo dài tùy ý (Mệnh đề 03.14, Bổ đề 03.20) dùng quy ước này cho nhiệm vụ có kết thúc. Phép đệm chỉ là quy ước tính toán trong một lượt; phần thưởng của lượt sau được tính trong lợi tức của lượt sau.
:::

### 2.3 Lợi tức hữu hạn

Với nhiệm vụ tiếp diễn, (2.1) là một chuỗi vô hạn, và chuỗi đó có thể phân kỳ. Nếu robot luôn Chờ ở pin thấp, mỗi bước nhận $1$. Với $\gamma=1$, lợi tức $1+1+1+\cdots$ phân kỳ. Với $\gamma=1/2$, lợi tức là tổng cấp số nhân $1+\tfrac12+\tfrac14+\cdots=2$: mỗi số hạng bằng một nửa số hạng trước, nên tổng tiến tới $2$ và không vượt $2$.

Lập luận này dùng hai điều: phần thưởng không vượt một hằng số, và trọng số giảm theo cấp số nhân với công bội nhỏ hơn $1$. Mệnh đề sau là dạng tổng quát của nó. Cận này đã có ở Mệnh đề 02.13(b) của ghi chú Bài 02, với $R_{\max}$ ở vị trí của $M$; ở đây cận được dùng cho MDP hữu hạn, và chứng minh được viết lại vì Bổ đề 03.20 dùng lại lập luận chuỗi trội của nó.

::: proposition Mệnh đề 03.11 (Cận của lợi tức)
**Giả thiết.** Có hằng số $M\ge0$ sao cho $\lvert R_k\rvert\le M$ với mọi $k$ (luôn đúng khi $\mathcal R$ hữu hạn, với $M=\max_{r\in\mathcal R}\lvert r\rvert$); $0\le\gamma<1$.

**Kết luận.** Chuỗi (2.1) hội tụ tuyệt đối trên mọi quỹ đạo và

$$
\lvert G_t\rvert\le\frac{M}{1-\gamma}.
\tag{2.2}
$$

**Điều kiện áp dụng.** Mọi nhiệm vụ, có kết thúc hay tiếp diễn, với phần thưởng bị chặn và $\gamma<1$.

**Phạm vi.** Cận (2.2) đúng trên từng quỹ đạo, không chỉ cho kỳ vọng; nó không nói lợi tức đạt tới cận. Khi $\gamma=1$, mệnh đề không áp dụng.
:::

::: proof Chứng minh Mệnh đề 03.11
**Bước 1 (chuỗi trội).** Với mọi $j\ge0$, giả thiết cho $\lvert\gamma^jR_{t+j+1}\rvert\le M\gamma^j$. Chuỗi $\sum_{j\ge0}M\gamma^j$ là cấp số nhân với công bội $\gamma\in[0,1)$, hội tụ và có tổng $M/(1-\gamma)$.

**Bước 2 (hội tụ tuyệt đối và cận).** Theo tiêu chuẩn so sánh, chuỗi $\sum_j\gamma^jR_{t+j+1}$ hội tụ tuyệt đối. Áp dụng bất đẳng thức tam giác cho các tổng riêng rồi chuyển qua giới hạn:

$$
\begin{aligned}
\lvert G_t\rvert&=\Bigl\lvert\sum_{j=0}^{\infty}\gamma^jR_{t+j+1}\Bigr\rvert\\
&\le\sum_{j=0}^{\infty}\gamma^j\lvert R_{t+j+1}\rvert&&\text{(bất đẳng thức tam giác)}\\
&\le\sum_{j=0}^{\infty}\gamma^jM&&\text{(giả thiết }\lvert R_k\rvert\le M)\\
&=\frac{M}{1-\gamma}&&\text{(tổng cấp số nhân, }\gamma<1).
\end{aligned}
$$

Với nhiệm vụ có kết thúc, Nhận xét 03.10 cho phép viết $G_t$ thành cùng chuỗi với các số hạng đệm bằng $0$, nên cận vẫn đúng. $\square$
:::

Mỗi giả thiết của Mệnh đề 03.11 bị bỏ đều có phản ví dụ.

- Bỏ $\gamma<1$: robot luôn Chờ có $R_k=1$ với mọi $k$, nên với $\gamma=1$ lợi tức phân kỳ dù phần thưởng bị chặn bởi $M=1$.
- Bỏ phần thưởng bị chặn: dãy $R_{t+j+1}=2^j$ với $\gamma=1/2$ cho mọi số hạng $\gamma^jR_{t+j+1}=1$, và lợi tức phân kỳ dù $\gamma<1$.

Bước 1 của chứng minh dùng cả hai: phần thưởng bị chặn cho chuỗi trội, $\gamma<1$ làm chuỗi trội hội tụ.

::: example Ví dụ 03.8 (Cận lợi tức của robot)
**Dữ kiện.** Robot của Ví dụ 03.1 có $\mathcal R=\{-3,0,1,2\}$; chọn $\gamma=1/2$.

**Tính.** $M=\max\{3,0,1,2\}=3$, nên theo (2.2)

$$
\lvert G_t\rvert\le\frac{3}{1-1/2}=6,\qquad\text{tức }-6\le G_t\le6\ \text{trên mọi quỹ đạo}.
$$

**Diễn giải.** Mọi lợi tức của robot với $\gamma=1/2$ nằm trong $[-6,6]$; các con số $3/2$, $7/4$ của Ví dụ 03.7 và lợi tức $2$ của robot luôn Chờ thỏa điều này.

**Kiểm tra lại.** Cận không đạt được ở robot: để $G_t=6$ cần $R_k=3$ ở mọi bước, nhưng $3\notin\mathcal R$; để $G_t=-6$ cần $R_k=-3$ ở mọi bước, nhưng sau mỗi lần cứu hộ robot ở pin cao, nơi mọi hành động cho phần thưởng dương.
:::

::: remark Nhận xét 03.12 (Chọn hệ số chiết khấu)
- **Trường hợp $\gamma=1$.** Với nhiệm vụ có kết thúc, kỳ vọng của lợi tức hữu hạn khi, chẳng hạn, phần thưởng bị chặn và $\mathbb E[T]<\infty$; gắn nhãn "kết thúc" cho một trạng thái chưa bảo đảm tác tử sẽ tới đó.
- **Trường hợp $\gamma=0$.** Lợi tức chỉ còn $G_t=R_{t+1}$, và mục tiêu là cận thị (myopic): chỉ phần thưởng ngay sau hành động được tính. Ở robot, mục tiêu này xếp Chờ trên Sạc tại pin thấp, bỏ qua việc Sạc mở ra các bước Tìm ở pin cao (Sutton và Barto, 2018, tr. 55). Bài giảng gốc (2025–2026, trang 36) gọi hành vi ứng với $\gamma$ gần $0$ là tham lam theo phần thưởng trước mắt; cách gọi này khác chính sách tham lam theo giá trị của Bài 04.
- **$\gamma$ thuộc về bài toán.** Đổi $\gamma$ là đổi tiêu chuẩn đánh giá, nên giá trị và chính sách tốt nhất có thể đổi theo, dù môi trường $p$ giữ nguyên.
:::

**Trong thực hành.** CartPole cho phần thưởng $+1$ ở mỗi bước, nên với $\gamma=0{,}99$ cận (2.2) là $100$; phần thưởng sau $100$ bước còn trọng số $0{,}99^{100}\approx0{,}37$. Trong notebook CartPole của Bài 04, một lượt của chính sách luôn đẩy phải kéo dài $9$ bước (một lần chạy đã nhúng trong notebook); theo (2.1), lợi tức chiết khấu của lượt đó là $(1-0{,}99^9)/0{,}01\approx8{,}65$.

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

Như vậy, chúng ta đã gộp chuỗi phần thưởng của mỗi quỹ đạo thành lợi tức $G_t$ (Định nghĩa 03.9), với một quy ước chung cho hai loại nhiệm vụ (Nhận xét 03.10) và một cận hữu hạn khi phần thưởng bị chặn và $\gamma<1$ (Mệnh đề 03.11). Tuy nhiên, $G_t$ là biến ngẫu nhiên và chưa quy về một con số cho mỗi trạng thái. Trong Mục 3, chúng ta cố định cách chọn hành động bằng một chính sách, rồi lấy kỳ vọng của $G_t$.

<!-- note-topic-id: lec-03-part-04 -->
## 3. Chính sách và hàm giá trị

Lợi tức $G_t$ của robot có hai nguồn ngẫu nhiên: phản hồi của môi trường và lựa chọn của robot. Bảng $p$ mô tả nguồn thứ nhất sau khi hành động đã được chọn; nó không nói hành động được chọn theo quy tắc nào. Muốn nói đến trung bình của lợi tức, chúng ta phải cố định quy tắc chọn hành động ở mọi trạng thái; quy tắc đó là chính sách.

### 3.1 Chính sách

Chúng ta bắt đầu bằng một quy tắc cụ thể cho robot. Quy tắc này được giữ cố định trong phần còn lại của chương, và chưa có khẳng định nào rằng nó tốt.

::: example Ví dụ 03.9 (Chính sách chia đều tại pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1. Ở pin cao, robot luôn Tìm. Ở pin thấp, robot chọn Chờ hoặc Sạc, mỗi hành động xác suất $1/2$, và không bao giờ Tìm.

**Bảng xác suất chọn hành động.**

| Trạng thái | Tìm | Chờ | Sạc |
|---|---:|---:|---:|
| $\mathrm H$ | $1$ | $0$ | không hợp lệ |
| $\mathrm L$ | $0$ | $1/2$ | $1/2$ |

**Đọc bảng.** Mỗi hàng là một phân phối trên các hành động hợp lệ của trạng thái đó. Ô "không hợp lệ" khác ô $0$: số $0$ là xác suất của một hành động hợp lệ nhưng không được chọn, còn ô không hợp lệ ứng với cặp nằm ngoài mô hình.

**Kiểm tra lại.** Hàng $\mathrm H$: $1+0=1$; hàng $\mathrm L$: $0+\tfrac12+\tfrac12=1$. Ở pin cao, quy tắc là tất định; ở pin thấp, quy tắc là ngẫu nhiên.

**Nguồn.** Số liệu sư phạm tự xây dựng; các ví dụ và bài tập về sau dùng chính sách này với $\gamma=1/2$ và gọi nó là chính sách chia đều tại pin thấp.
:::

![Từ nút L, hai mũi tên mang xác suất 1/2 tới hai khối hành động dưới nhãn "Chính sách": Chờ và Sạc; từ Chờ một mũi tên xác suất 1 tới khối "L; thưởng 1", từ Sạc một mũi tên xác suất 1 tới khối "H; thưởng 0" dưới nhãn "Môi trường".](img/lec-03/robot-p04-two-layers.svg)

Hình trên tách một bước của robot ở pin thấp thành hai tầng. Tầng "Chính sách" rút hành động với các xác suất $1/2$ của Ví dụ 03.9; tầng "Môi trường" rút phản hồi theo bảng $p$ của Ví dụ 03.5, ở đây là chắc chắn. Xác suất của mỗi đường từ trái sang phải là tích các số trên đường, $\tfrac12\cdot1=\tfrac12$.

Một cách trực quan, chính sách là tầng thứ nhất của hình, viết cho mọi trạng thái. Định nghĩa sau làm chính xác điều này.

::: definition Định nghĩa 03.13 (Chính sách Markov dừng)
Một chính sách (policy) Markov dừng là một hàm $\pi$ gán cho mỗi trạng thái $s\in\mathcal S$ một phân phối xác suất $\pi(\cdot\mid s)$ trên $\mathcal A(s)$:

$$
\pi(a\mid s)\ge0,\qquad\sum_{a\in\mathcal A(s)}\pi(a\mid s)=1 .
$$

Tác tử theo chính sách $\pi$ tại thời điểm $t$ nếu với mọi lịch sử $h_t$ kết thúc ở $s\in\mathcal S$ có $\Pr(H_t=h_t)>0$,

$$
\Pr(A_t=a\mid H_t=h_t)=\pi(a\mid s).
\tag{3.1}
$$

Cho một phân phối đầu $\mu$ của $S_0$, ký hiệu $\Pr_\pi$, $\mathbb E_\pi$ là xác suất và kỳ vọng trên các quỹ đạo sinh ra khi $S_0$ rút theo $\mu$, hành động theo (3.1) ở mọi thời điểm và phản hồi theo hàm động lực $p$. Ký hiệu này cũng dùng cho quá trình chỉ theo $\pi$ từ một thời điểm trở đi, như quá trình ấn định ở Định nghĩa 03.16.
:::

"Markov" nghĩa là xác suất chọn hành động chỉ phụ thuộc trạng thái hiện tại; "dừng" nghĩa là cùng hàm $\pi$ được dùng ở mọi thời điểm. Chính sách xác định là trường hợp riêng khi mỗi $\pi(\cdot\mid s)$ dồn xác suất $1$ vào một hành động; từ Ví dụ 03.9, $\pi(\mathrm{cho}\mid\mathrm L)=1/2$.

Chính sách bổ sung cho hàm động lực: $p$ là quy luật của môi trường, $\pi$ là quy luật của tác tử. Nhầm lẫn thường gặp là nghĩ đổi chính sách thì đổi mô hình; đổi chính sách không đổi bảng $p$, nhưng đổi xác suất của mọi quỹ đạo. Định nghĩa 03.13 khớp với chính sách ngẫu nhiên của ghi chú Bài 02, Mục 3 và Bài giảng gốc (2025–2026, trang 52).

Mệnh đề sau cho xác suất của một đoạn quỹ đạo dưới cặp $(\pi,p)$. Với nhiệm vụ có kết thúc, đoạn quỹ đạo có thể vượt quá thời điểm kết thúc; khi đó ta dùng quy ước trạng thái hấp thụ của Nhận xét 03.10: tại trạng thái kết thúc chỉ có một hành động giả được chọn với xác suất $1$, và nó đưa về chính trạng thái đó với phần thưởng $0$.

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

Công thức (3.2) nói xác suất của một đoạn quỹ đạo là tích, qua từng bước, của xác suất chọn hành động và xác suất phản hồi. Từ $\mathrm H$ dưới chính sách chia đều tại pin thấp, đoạn "Tìm, về $\mathrm L$ với phần thưởng $2$, Sạc, về $\mathrm H$ với phần thưởng $0$" có xác suất $1\cdot\tfrac12\cdot\tfrac12\cdot1=\tfrac14$. Tích này không giả thiết hành động độc lập với phản hồi; mỗi thừa số là xác suất có điều kiện, được rút gọn nhờ hai giả thiết Markov.

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
\mathbb E_\pi\bigl[G_0^{[2]}\mid S_0=\mathrm H\bigr]=\tfrac12\cdot3+\tfrac14\cdot\tfrac52+\tfrac14\cdot2=\tfrac{12}{8}+\tfrac58+\tfrac48=\tfrac{21}{8}.
$$

**Kiểm tra lại.** Theo tuyến tính, $\mathbb E_\pi[R_1]+\gamma\,\mathbb E_\pi[R_2]=2+\tfrac12\cdot\tfrac54=\tfrac{21}{8}$.
:::

![Cây hai bước từ H. Bước 1: Tìm, phần thưởng +2, tới H hoặc L, mỗi nhánh 1/2. Từ H, hành động 2 là Tìm với xác suất 1, phần thưởng +2, ô cuối ghi "3; gộp 1/2". Từ L, hành động 2 là Chờ (1/2, phần thưởng +1) với ô cuối "5/2; 1/4", hoặc Sạc (1/2, phần thưởng 0) với ô cuối "2; 1/4".](img/lec-03/robot-p04-two-step-tree.svg)

Trên cây, mỗi đường từ gốc tới một ô cuối là một nhóm quỹ đạo, ô cuối ghi $G_0^{[2]}$ và xác suất của nhóm theo (3.2). Số $1$ trên cạnh tới "Tìm: +2" là xác suất chính sách chọn Tìm; nhãn "gộp 1/2" gộp hai trạng thái kế tiếp cho cùng $R_2=2$.

Con số $21/8$ chỉ tính hai bước đầu. Một cách trực quan, giá trị của pin cao là con số thu được nếu kéo dài cây trên xuống mọi tầng: mỗi đường vô hạn từ gốc mang một lợi tức đầy đủ $G_0$, và ta lấy trung bình các lợi tức đó với trọng số là xác suất của đường. Mô tả này chưa phải định nghĩa, vì cây vô hạn không liệt kê được; định nghĩa sau gọi tên đại lượng đó bằng kỳ vọng.

::: definition Định nghĩa 03.15 (Hàm giá trị trạng thái)
Cho MDP hữu hạn, chính sách Markov dừng $\pi$, phần thưởng bị chặn và $0\le\gamma<1$. Với $s\in\mathcal S$, gọi quá trình xuất phát tại $s$ là quá trình có $S_0=s$ với xác suất $1$, hành động theo (3.1) và phản hồi theo $p$. Hàm giá trị trạng thái (state-value function) của $\pi$ là hàm $v_\pi:\mathcal S^+\to\mathbb R$,

$$
v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s],
\tag{3.3}
$$

trong đó kỳ vọng lấy trên quá trình xuất phát tại $s$. Với trạng thái kết thúc $s$, quy ước $v_\pi(s)=0$.
:::

Định nghĩa (3.3) đọc như sau: xuất phát ở $s$, hành động rút theo $\pi$, phản hồi rút theo $p$, và $v_\pi(s)$ là trung bình của lợi tức trên mọi quỹ đạo đó; kỳ vọng tồn tại vì $\lvert G_0\rvert\le M/(1-\gamma)$. Ký hiệu điều kiện $S_0=s$ cho cùng một số với mọi phân phối đầu $\mu$ có $\mu(s)>0$, theo (3.2) và Bổ đề 03.20(b) với $t=0$, $h_0=(s)$.

Sutton và Barto (2018, (3.12)) và ghi chú Bài 02, Mục 4 viết $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ với $t$ bất kỳ; Bổ đề 03.20(c) chứng minh hai cách viết cho cùng một số.

Ví dụ 03.10 là một xấp xỉ của $v_\pi(\mathrm H)$ chỉ dùng hai số hạng đầu. Phần bị bỏ có trị tuyệt đối không quá $\gamma^2M/(1-\gamma)=\tfrac14\cdot6=\tfrac32$, nên

$$
v_\pi(\mathrm H)\in\Bigl[\tfrac{21}{8}-\tfrac32,\ \tfrac{21}{8}+\tfrac32\Bigr]=\Bigl[\tfrac98,\ \tfrac{33}{8}\Bigr].
$$

Ở Mục 5, chúng ta sẽ tính được $v_\pi(\mathrm H)=13/4$, nằm trong khoảng này.

### 3.3 Giá trị hành động

Giá trị trạng thái để chính sách chọn cả hành động đầu tiên. Ở pin thấp, chính sách chia đều không bao giờ Tìm, nên $v_\pi(\mathrm L)$ không cho biết điều gì xảy ra nếu robot Tìm một lần. Để so sánh từng lựa chọn, chúng ta cần một đại lượng ấn định hành động đầu tiên.

Một cách trực quan, chúng ta làm một thí nghiệm: đặt robot ở $s$, ấn định hành động $a$ ở bước đầu, rồi từ bước sau để nó theo $\pi$. Lợi tức kỳ vọng của thí nghiệm này là giá trị của hành động $a$ tại $s$. Đây chưa phải định nghĩa; ví dụ sau thực hiện ba thí nghiệm, mỗi thí nghiệm chỉ tính hai bước.

::: example Ví dụ 03.11 (Ba thí nghiệm từ pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$, $S_0=\mathrm L$. Hành động $A_0$ bị ấn định; từ $t=1$ robot theo $\pi$. Đại lượng tính là kỳ vọng của $G_0^{[2]}=R_1+\gamma R_2$.

**Ấn định Tìm.** Hai phản hồi, mỗi phản hồi xác suất $1/2$.

- $(\mathrm L,2)$: ở $\mathrm L$ chính sách chọn Chờ hoặc Sạc, $\mathbb E[R_2]=\tfrac12\cdot1+\tfrac12\cdot0=\tfrac12$, nên kỳ vọng của nhánh là $2+\tfrac12\cdot\tfrac12=\tfrac94$.
- $(\mathrm H,-3)$: ở $\mathrm H$ chính sách chọn Tìm, $R_2=2$, nên nhánh cho $-3+\tfrac12\cdot2=-2$.

Kỳ vọng: $\tfrac12\cdot\tfrac94+\tfrac12\cdot(-2)=\tfrac18$.

**Ấn định Chờ.** $R_1=1$, $S_1=\mathrm L$, $\mathbb E[R_2]=\tfrac12$; kỳ vọng $1+\tfrac12\cdot\tfrac12=\tfrac54$.

**Ấn định Sạc.** $R_1=0$, $S_1=\mathrm H$, $R_2=2$; kỳ vọng $0+\tfrac12\cdot2=1$.

**Kiểm tra lại.** Mỗi thí nghiệm dùng đúng các xác suất phản hồi của Ví dụ 03.5: ấn định một hành động không làm phản hồi của môi trường trở thành chắc chắn.
:::

::: definition Định nghĩa 03.16 (Hàm giá trị hành động)
Với cùng giả thiết của Định nghĩa 03.15, $s\in\mathcal S$ và $a\in\mathcal A(s)$, gọi quá trình ấn định $(s,a)$ là quá trình có $S_0=s$, $A_0=a$ với xác suất $1$, phản hồi theo $p$, và hành động theo (3.1) từ thời điểm $1$ trở đi. Hàm giá trị hành động (action-value function) của $\pi$ là

$$
q_\pi(s,a)=\mathbb E_\pi[G_0\mid S_0=s,A_0=a],
\tag{3.4}
$$

trong đó kỳ vọng lấy trên quá trình ấn định $(s,a)$. Định nghĩa áp dụng như nhau cho mọi $a\in\mathcal A(s)$, kể cả khi $\pi(a\mid s)=0$.
:::

Khác biệt duy nhất giữa $q_\pi(s,a)$ và $v_\pi(s)$ là hành động đầu: $v_\pi$ để chính sách rút nó, $q_\pi$ ấn định nó. Ba con số $\tfrac18$, $\tfrac54$, $1$ của Ví dụ 03.11 là kỳ vọng của hai số hạng đầu của lợi tức trong ba thí nghiệm định nghĩa $q_\pi(\mathrm L,\mathrm{tim})$, $q_\pi(\mathrm L,\mathrm{cho})$, $q_\pi(\mathrm L,\mathrm{sac})$. Bổ đề 03.20(d) chứng minh rằng khi $\Pr_\pi(S_t=s,A_t=a)>0$, kỳ vọng có điều kiện $\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ của Sutton và Barto (2018, (3.13)) bằng $q_\pi(s,a)$.

::: remark Nhận xét 03.17 (Ba cách hiểu sai về giá trị)
- **$q_\pi(s,a)$ có nghĩa khi $\pi(a\mid s)=0$.** Định nghĩa dùng quá trình ấn định hành động, không chia cho $\Pr_\pi(A_t=a\mid S_t=s)$. Vì vậy $q_\pi(\mathrm L,\mathrm{tim})$ xác định dù $\pi(\mathrm{tim}\mid\mathrm L)=0$.
- **$q_\pi(s,a)$ khác $r(s,a)$.** Thưởng kỳ vọng $r(s,a)$ chỉ tính bước đầu; $q_\pi(s,a)$ tính toàn bộ tương lai. Ở pin thấp, $r(\mathrm L,\mathrm{cho})=1$ còn kỳ vọng hai bước của thí nghiệm Chờ đã là $5/4$.
- **$v_\pi(s)$ khác lợi tức $G_t$.** $G_t$ thay đổi theo quỹ đạo; $v_\pi(s)$ là trung bình của nó.
:::

Hàm $q_\pi$ cho giá trị của mọi hành động hợp lệ, kể cả hành động chính sách không chọn; quan hệ chính xác với $v_\pi$ là Mệnh đề 03.22 và 03.23.

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
\mathbb E_\pi\bigl[G_0^{[2]}\mid S_0=\mathrm L\bigr]=\tfrac14\cdot\tfrac32+\tfrac14\cdot1+\tfrac12\cdot1=\tfrac38+\tfrac28+\tfrac48=\tfrac98 .
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

**Kiểm tra lại.** Nếu tính lại $v_\pi$ cho chính sách mới, các phương trình của Mục 4 dùng cùng các hệ số từ $p$ và hệ số mới từ $\pi$.
:::

Như vậy, chúng ta đã cố định cách chọn hành động bằng chính sách Markov dừng (Định nghĩa 03.13), có công thức xác suất cho mọi đoạn quỹ đạo (Mệnh đề 03.14), và định nghĩa giá trị trạng thái và giá trị hành động (Định nghĩa 03.15, 03.16). Tuy nhiên, các định nghĩa vẫn là kỳ vọng trên vô hạn quỹ đạo dài vô hạn. Trong Mục 4, chúng ta chứng minh rằng phần đuôi của lợi tức có kỳ vọng bằng đúng giá trị của trạng thái kế tiếp, nhờ đó mỗi trạng thái có một phương trình chứa hữu hạn ẩn.

<!-- note-topic-id: lec-03-part-05 -->
## 4. Phương trình Bellman kỳ vọng

Ví dụ 03.10 và Bài tập 03.4 mới tính được hai số hạng đầu của giá trị, với cận sai số $3/2$ (theo giá trị tính ở Mục 5, sai số thật là $\tfrac{13}4-\tfrac{21}8=\tfrac58$ ở pin cao và $\tfrac74-\tfrac98=\tfrac58$ ở pin thấp); thêm số hạng thì số nhánh tăng gấp đôi sau mỗi bước. Để tránh liệt kê vô hạn quỹ đạo, chúng ta nhóm các quỹ đạo theo bước đầu tiên: mỗi nhóm có một phần thưởng ngay và một phần còn lại bắt đầu ở trạng thái kế tiếp. Nếu kỳ vọng của phần còn lại bằng giá trị của trạng thái kế tiếp, mỗi trạng thái cho một phương trình với hữu hạn ẩn. Trong mục này, chúng ta chứng minh điều đó và chỉ ra chỗ cần đến tính Markov.

### 4.1 Phương trình một bước tại pin thấp

Ví dụ sau viết phương trình cho $v_\pi(\mathrm L)$ theo lập luận trên, khi lập luận chưa được chứng minh.

::: example Ví dụ 03.12 (Phương trình một bước tại pin thấp)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$. Ở $\mathrm L$, chính sách chọn Chờ hoặc Sạc, mỗi hành động $1/2$; Chờ cho $(\mathrm L,1)$ chắc chắn, Sạc cho $(\mathrm H,0)$ chắc chắn.

**Nhóm theo bước đầu.**

- Nhóm Chờ (xác suất $1/2$): phần thưởng ngay $1$; phần còn lại bắt đầu ở $\mathrm L$, được chiết khấu một lần, đóng góp $\gamma\,v_\pi(\mathrm L)$ nếu kỳ vọng của nó bằng $v_\pi(\mathrm L)$.
- Nhóm Sạc (xác suất $1/2$): phần thưởng ngay $0$; phần còn lại bắt đầu ở $\mathrm H$, đóng góp $\gamma\,v_\pi(\mathrm H)$.

**Phương trình.**

$$
v_\pi(\mathrm L)=\tfrac12\bigl[1+\tfrac12\,v_\pi(\mathrm L)\bigr]+\tfrac12\bigl[0+\tfrac12\,v_\pi(\mathrm H)\bigr].
\tag{4.1}
$$

**Đọc phương trình.** Hai hệ số $\tfrac12$ ngoài ngoặc là $\pi(\mathrm{cho}\mid\mathrm L)$ và $\pi(\mathrm{sac}\mid\mathrm L)$; hệ số $\tfrac12$ trước $v_\pi$ trong ngoặc là $\gamma$. Ẩn $v_\pi(\mathrm L)$ có ở cả hai vế vì Chờ giữ nguyên mức pin.

**Kiểm tra lại.** Thay $v_\pi$ trong ngoặc bằng thưởng kỳ vọng một bước dưới chính sách tại trạng thái kế tiếp ($\tfrac12$ ở $\mathrm L$, $2$ ở $\mathrm H$) cho $\tfrac12(1+\tfrac14)+\tfrac12(0+1)=\tfrac98$, trùng kỳ vọng hai bước của Bài tập 03.4.
:::

Hai bước còn thiếu để (4.1) thành một kết quả: tách lợi tức thành phần thưởng ngay và phần còn lại, và chứng minh kỳ vọng của phần còn lại bằng giá trị của trạng thái kế tiếp.

### 4.2 Hệ thức đệ quy của lợi tức

Bước thứ nhất là một hệ thức trên từng quỹ đạo, không dùng xác suất. Hệ thức này đã có ở Mệnh đề 02.13(a) của ghi chú Bài 02; ở đây nó được phát biểu với giả thiết ghi rõ để các chuỗi $G_t$, $G_{t+1}$ hội tụ.

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
G_t&=\sum_{j=0}^{\infty}\gamma^jR_{t+j+1}&&\text{(Định nghĩa 03.9)}\\
&=R_{t+1}+\sum_{j=1}^{\infty}\gamma^jR_{t+j+1}&&\text{(tách số hạng }j=0)\\
&=R_{t+1}+\gamma\sum_{i=0}^{\infty}\gamma^iR_{(t+1)+i+1}&&\text{(đặt }j=i+1)\\
&=R_{t+1}+\gamma\,G_{t+1}&&\text{(Định nghĩa 03.9 tại }t+1).
\end{aligned}
$$

**Bước 2 (trường hợp có kết thúc).** Khi $T<\infty$, các tổng là hữu hạn và cùng phép tách cho $G_t=R_{t+1}+\gamma\sum_{k=t+2}^{T}\gamma^{k-t-2}R_k$. Với $t<T-1$, tổng cuối là $G_{t+1}$. Với $t=T-1$, tổng cuối rỗng và bằng $0=G_T$ theo quy ước. $\square$
:::

Đẳng thức (4.2) nói rằng lợi tức từ $t$ bằng phần thưởng của bước kế tiếp cộng lợi tức từ $t+1$ đã chiết khấu một lần. Số hạng đầu của $G_{t+1}$ là $R_{t+2}$, không phải $R_{t+1}$; viết lệch chỉ số ở đây là lỗi thường gặp.

### 4.3 Hai tầng kỳ vọng

Bước thứ hai lấy kỳ vọng của (4.2) bằng cách nhóm quỹ đạo theo hành động đầu, rồi theo phản hồi đầu, như hai tầng của hình ở tiểu mục 3.1. Công cụ là kỳ vọng toàn phần nhắc lại ở mục Kiến thức tiên quyết.

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

Ở tầng hành động, trọng số là $\pi(a\mid s)$; ở tầng phản hồi, trọng số là $p(s',r\mid s,a)$. Ghép hai tầng, mỗi bộ $(a,s',r)$ mang trọng số

$$
\pi(a\mid s)\,p(s',r\mid s,a),
$$

đúng thừa số của (3.2) với $K=1$.

### 4.4 Tính Markov của phần tương lai và phương trình Bellman

Bước thứ ba là bỏ lịch sử khỏi kỳ vọng của phần còn lại. Ở robot, câu hỏi là kỳ vọng của $G_1$ khi biết $H_1=(\mathrm L,\mathrm{cho},1,\mathrm L)$ có bằng $v_\pi(\mathrm L)$ hay không. Trực giác cho câu trả lời có: từ thời điểm $1$, robot ở pin thấp và theo cùng chính sách, nên tương lai bắt đầu lại từ $\mathrm L$. Bổ đề sau chứng minh trực giác này; nó là chỗ duy nhất trong chương dùng tính Markov cho toàn bộ tương lai.

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

**Phạm vi.** Với nhiệm vụ có kết thúc và $\gamma=1$, kết luận vẫn đúng khi lợi tức khả tích, nhưng bước qua giới hạn cần lập luận khác; chương không chứng minh trường hợp đó.
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
\bigl\lvert G_t-G_t^{[K]}\bigr\rvert=\Bigl\lvert\sum_{j\ge K}\gamma^jR_{t+j+1}\Bigr\rvert\le\frac{\gamma^KM}{1-\gamma}
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

Bổ đề 03.20 nói rằng khi biết lịch sử kết thúc ở $s$, tương lai phân phối giống tương lai của một quá trình mới bắt đầu ở $s$. Với robot, kỳ vọng của $G_1$ khi biết $H_1=(\mathrm L,\mathrm{cho},1,\mathrm L)$ bằng $v_\pi(\mathrm L)$, đúng điều Ví dụ 03.12 đã giả định.

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

**Phạm vi.** Định lý nói $v_\pi$ thỏa hệ (4.5); nó chưa nói hệ có nghiệm duy nhất (Định lý 03.28). Sutton và Barto (2018, (3.14)) phát biểu cùng phương trình và cho phép cả nhiệm vụ có kết thúc với $\gamma=1$ khi lợi tức khả tích.
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
v_\pi(s)&=\mathbb E_\pi[R_1+\gamma G_1\mid S_0=s]&&\text{(Bước 1)}\\
&=\sum_a\pi(a\mid s)\,\mathbb E_\pi[R_1+\gamma G_1\mid S_0=s,A_0=a]&&\text{(Bước 2)}\\
&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma\,\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]\bigr]&&\text{(Bước 3)}\\
&=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma\,v_\pi(s')\bigr]&&\text{(Bước 4)}.
\end{aligned}
$$

Các số hạng với $\pi(a\mid s)=0$ hoặc $p(s',r\mid s,a)=0$ bằng $0$, nên tổng có thể lấy trên toàn bộ $\mathcal A(s)$, $\mathcal S^+$, $\mathcal R$ như trong (4.5). $\square$
:::

Phương trình (4.5) đọc bằng lời: giá trị của một trạng thái bằng trung bình, theo xác suất chọn hành động và xác suất phản hồi, của phần thưởng một bước cộng giá trị đã chiết khấu của trạng thái kế tiếp. Vế phải chỉ chứa các giá trị $v_\pi(s')$, nên với $n$ trạng thái, (4.5) là $n$ phương trình cho $n$ ẩn.

Áp dụng (4.5) tại $s=\mathrm L$ cho robot, các số hạng của Tìm biến mất vì $\pi(\mathrm{tim}\mid\mathrm L)=0$; Chờ chỉ có phản hồi $(\mathrm L,1)$ và Sạc chỉ có $(\mathrm H,0)$, nên (4.5) trở thành phương trình (4.1) của Ví dụ 03.12. Lập luận nhóm theo bước đầu của ví dụ đó giờ đã được chứng minh.

![Hai sơ đồ cập nhật. Vòng tròn rỗng là trạng thái, chấm tròn đặc là cặp trạng thái–hành động. Bên trái, sơ đồ của v_π: gốc s, ba cạnh có nhãn π(a | s) xuống ba chấm đặc a, từ mỗi chấm đặc hai cạnh có nhãn p, r xuống hai vòng tròn s'. Bên phải, sơ đồ của q_π: gốc là chấm đặc (s, a), hai cạnh có nhãn p(s', r | s, a), r xuống hai vòng tròn s', từ mỗi s' hai cạnh có nhãn π(a' | s') xuống hai chấm đặc a'. Chú thích: giá trị ở gốc bằng trung bình có trọng số của r + γ nhân giá trị ở tầng dưới.](img/lec-03/backup-diagrams.svg)

Hình trên là sơ đồ cập nhật (backup diagram) theo cách vẽ của Sutton và Barto (2018, tr. 59, 61). Ở sơ đồ bên trái, tầng cạnh trên mang trọng số $\pi(a\mid s)$ của Bước 2, tầng cạnh dưới mang $p(s',r\mid s,a)$ của Bước 3, mỗi lá góp $r+\gamma v_\pi(s')$ theo Bước 4. Sơ đồ bên phải dùng cho Hệ quả 03.24.

Ba giả thiết của Định lý 03.21 có vai trò riêng, và mỗi giả thiết bị bỏ đều làm hỏng một bước của chứng minh.

- Bỏ tính Markov: ở Ví dụ 03.4, phần thưởng của bước sau phụ thuộc phòng, và lịch sử tiết lộ phòng. Kỳ vọng của phần tương lai sau lịch sử $h$ khác sau lịch sử $h'$, dù cả hai kết thúc ở $\mathrm L$, nên không thể cùng bằng một số $v_\pi(\mathrm L)$; Bổ đề 03.20(b) sai. Với $\gamma=1/2$, hai kỳ vọng đó lần lượt là $\tfrac23$ và $\tfrac43$, còn $v_\pi(\mathrm L)=1$ (kỳ vọng của $G_0$ khi $S_0=\mathrm L$ trên quá trình thật, phòng đầu chọn đều). Ví dụ này làm hỏng lập luận nhưng không bác bỏ kết luận. Vì chỉ có một trạng thái và phân phối phòng như nhau ở mọi bước, phương trình lập từ bảng trung bình $p(\mathrm L,1\mid\mathrm L,\mathrm{cho})=p(\mathrm L,0\mid\mathrm L,\mathrm{cho})=\tfrac12$ vẫn đúng do cấu trúc này: $v=\tfrac1{2(1-\gamma)}$ thỏa $v=\tfrac12+\gamma v$. Một trường hợp quan sát được là Tình huống 03.2: giá trị giải từ bảng ước lượng trên các ô lệch lợi tức thật, và chênh lệch gộp cả khả năng ô mất tính Markov lẫn cách dựng $\hat p$.
- Bỏ tính dừng của chính sách: nếu robot Chờ ở bước chẵn và Sạc ở bước lẻ khi ở pin thấp, lợi tức kỳ vọng từ $\mathrm L$ phụ thuộc thời điểm; Bước 1 của Bổ đề 03.20 sai.
- Bỏ $\gamma<1$ ở nhiệm vụ tiếp diễn: với $\gamma=1$, robot luôn Chờ có lợi tức vô hạn, nên $v_\pi(\mathrm L)$ không phải số thực và (4.5) không có nghĩa.

**Trong thực hành.** Vế phải của (4.5) là kỳ vọng của $R_{t+1}+\gamma\,v_\pi(S_{t+1})$ khi biết $S_t=s$, và một bước tương tác thật cho một mẫu của đại lượng này. Phương pháp TD(0) của Bài 05 cập nhật bảng ước lượng $V$ với bước học $\alpha\in(0,1]$ theo

$$
V(S_t)\leftarrow V(S_t)+\alpha\bigl[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\bigr],
$$

trong đó $R_{t+1}+\gamma V(S_{t+1})$ là mục tiêu bootstrap (bootstrap target). Kỳ vọng của mục tiêu này là vế phải của (4.5) với $V$ ở vị trí của $v_\pi$, không phải $v_\pi(s)$. Khi trạng thái là một ô rời rạc hóa như ở CartPole, giả thiết Markov của Định lý 03.21 có thể sai (Tình huống 03.2).

### 4.5 Quan hệ giữa giá trị trạng thái và giá trị hành động

Với giá trị hành động, bước đầu đã bị ấn định, nên chỉ còn tầng phản hồi. Ví dụ sau viết $q_\pi(\mathrm L,\mathrm{tim})$ theo lập luận của Ví dụ 03.12.

::: example Ví dụ 03.13 (Hai nhánh của L–Tìm)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$. Tìm từ $\mathrm L$ cho $(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi phản hồi xác suất $1/2$.

**Nhóm theo phản hồi.** Hành động đầu đã là Tìm, nên không có trọng số chính sách ở bước đầu. Mỗi phản hồi đóng góp phần thưởng của nó cộng giá trị chiết khấu của trạng thái kế tiếp:

$$
q_\pi(\mathrm L,\mathrm{tim})=\tfrac12\bigl[2+\tfrac12\,v_\pi(\mathrm L)\bigr]+\tfrac12\bigl[-3+\tfrac12\,v_\pi(\mathrm H)\bigr].
$$

**Dạng rút gọn.** Gom phần thưởng và gom giá trị:

$$
q_\pi(\mathrm L,\mathrm{tim})=\underbrace{\bigl(\tfrac12\cdot2+\tfrac12\cdot(-3)\bigr)}_{r(\mathrm L,\mathrm{tim})=-1/2}+\tfrac12\bigl(\tfrac12\,v_\pi(\mathrm L)+\tfrac12\,v_\pi(\mathrm H)\bigr).
$$

**Kiểm tra lại.** Hệ số $\tfrac12$ ngoài các ngoặc là xác suất phản hồi, không phải xác suất chính sách. Chính sách có mặt qua $v_\pi(\mathrm L)$ và $v_\pi(\mathrm H)$, vì từ bước sau robot theo $\pi$.
:::

Ví dụ 03.13 chưa cho con số vì $v_\pi(\mathrm L)$ và $v_\pi(\mathrm H)$ chưa biết; Ví dụ 03.15 ở Mục 5 sẽ thay số. Mệnh đề sau là dạng tổng quát của ví dụ.

::: proposition Mệnh đề 03.22 (Giá trị hành động theo giá trị trạng thái)
**Giả thiết.** Như Định lý 03.21; $s\in\mathcal S$, $a\in\mathcal A(s)$, kể cả khi $\pi(a\mid s)=0$.

**Kết luận.**

$$
q_\pi(s,a)=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\bigl[r+\gamma\,v_\pi(s')\bigr]=r(s,a)+\gamma\sum_{s'\in\mathcal S^+}p(s'\mid s,a)\,v_\pi(s').
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
\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr]&=\sum_{s',r}r\,p(s',r\mid s,a)+\gamma\sum_{s'}v_\pi(s')\sum_rp(s',r\mid s,a)\\
&=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s').
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
Áp dụng (4.3) với $X=G_0$ cho quá trình xuất phát tại $s$: $v_\pi(s)=\sum_a\pi(a\mid s)\,\mathbb E_\pi[G_0\mid S_0=s,A_0=a]$, tổng trên các $a$ có $\pi(a\mid s)>0$. Với các $a$ đó, Bổ đề 03.20(d) tại $t=0$ cho kỳ vọng có điều kiện bằng $q_\pi(s,a)$. Các $a$ có $\pi(a\mid s)=0$ góp số hạng $0\cdot q_\pi(s,a)=0$, vì $q_\pi(s,a)$ hữu hạn, nên tổng có thể lấy trên toàn bộ $\mathcal A(s)$. $\square$
:::

Thế (4.6) vào (4.7) ta lại được (4.5). Thế theo chiều ngược lại, (4.7) tại trạng thái kế tiếp vào (4.6), ta được một phương trình chỉ chứa $q_\pi$.

::: corollary Hệ quả 03.24 (Phương trình Bellman kỳ vọng cho $q_\pi$)
**Giả thiết.** Như Định lý 03.21.

**Kết luận.** Với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$,

$$
q_\pi(s,a)=\sum_{s'\in\mathcal S^+}\sum_{r\in\mathcal R}p(s',r\mid s,a)\Bigl[r+\gamma\sum_{a'\in\mathcal A(s')}\pi(a'\mid s')\,q_\pi(s',a')\Bigr],
\tag{4.8}
$$

với quy ước tổng trong ngoặc bằng $0$ khi $s'$ là trạng thái kết thúc.

**Điều kiện áp dụng.** Mọi cặp hợp lệ, kể cả cặp có $\pi(a\mid s)=0$.

**Phạm vi.** Đây là bài tập 3.17 của Sutton và Barto (2018, tr. 61); như (4.5), phương trình là trung bình theo $\pi$.
:::

::: proof Chứng minh Hệ quả 03.24
Với $s'$ chưa kết thúc, Mệnh đề 03.23 tại $s'$ cho $v_\pi(s')=\sum_{a'}\pi(a'\mid s')\,q_\pi(s',a')$. Với $s'$ kết thúc, $v_\pi(s')=0$, bằng tổng rỗng theo quy ước. Thay vào đẳng thức thứ nhất của (4.6) ta được (4.8). $\square$
:::

Trong (4.8), $a$ là hành động tại thời điểm $t$, còn $a'$ là hành động chính sách chọn tại $t+1$ ở $s'$, nên trọng số là $\pi(a'\mid s')$. Tổng ngoài mang xác suất của môi trường, tổng trong mang xác suất của chính sách, theo thứ tự ngược với (4.5), như sơ đồ bên phải của hình sơ đồ cập nhật. Ở robot, (4.8) có năm phương trình, (4.5) chỉ có hai.

**Trong thực hành.** Thuật toán Sarsa của Bài 06 học bảng $Q$ cho chính sách đang dùng, với mục tiêu bootstrap $R_{t+1}+\gamma\,Q(S_{t+1},A_{t+1})$, trong đó $A_{t+1}$ là hành động thật sự được chọn ở bước sau. Đây là một mẫu của ngoặc vuông trong (4.8). Khi không biết mô hình, $q_\pi$ có lợi thế theo (4.6): so sánh hành động bằng $v_\pi$ cần $p$, còn $q_\pi$ cho trực tiếp con số của từng hành động.

::: remark Nhận xét 03.25 (Chỗ dùng tính Markov; trung bình khác cực đại)
- Tính Markov được dùng ở hai chỗ. Bổ đề 03.19 dùng tính Markov một bước qua quy tắc sinh: trọng số $p(s',r\mid s,a)$ của tầng phản hồi không phụ thuộc lịch sử theo Định nghĩa 03.7. Bổ đề chỉ dùng quy tắc sinh tại một thời điểm $t$, nên không dùng phần "cùng hàm $p$ cho mọi $t$" của quy tắc, tức tính dừng: (4.4) vẫn đúng nếu $p$ là hàm động lực riêng của thời điểm $t$. Bổ đề 03.20 dùng tính Markov cho toàn bộ phần tương lai và tính dừng của $\pi$ và $p$ để bỏ lịch sử khỏi kỳ vọng của $G_t$; mọi kết quả sau nó thừa hưởng hai giả thiết này. Bổ đề 03.18 là đẳng thức trên từng quỹ đạo và không dùng giả thiết nào trong hai giả thiết đó.
- Mọi phương trình của mục là trung bình theo $\pi$. Nhầm (4.5) với phương trình có $\max_a$ là nhầm bài toán dự đoán (đánh giá một chính sách cho trước) với bài toán điều khiển (tìm chính sách tốt nhất); bài toán thứ hai là nội dung của Bài 04.
:::

::: exercise Bài tập 03.6
**Dữ kiện.** Robot của Ví dụ 03.1: Tìm từ $\mathrm H$ cho phần thưởng $2$ và về $\mathrm H$ hoặc $\mathrm L$, mỗi trạng thái xác suất $1/2$. Chính sách chia đều tại pin thấp: ở $\mathrm H$ luôn Tìm. $\gamma=1/2$. Viết $v_H=v_\pi(\mathrm H)$, $v_L=v_\pi(\mathrm L)$.

**Yêu cầu.** Từ Định lý 03.21, chứng minh $v_H=2+\tfrac14v_H+\tfrac14v_L$, chỉ rõ mỗi hệ số đến từ $\pi$, từ $p$ hay từ $\gamma$.
:::

::: hint
Ở $\mathrm H$, tổng theo hành động chỉ còn một số hạng; tổng theo phản hồi có hai số hạng.
:::

::: solution
Áp dụng (4.5) tại $s=\mathrm H$. Tổng theo $a$ chỉ còn $a=\mathrm{tim}$ với $\pi(\mathrm{tim}\mid\mathrm H)=1$, vì $\pi(\mathrm{cho}\mid\mathrm H)=0$. Cặp $(\mathrm H,\mathrm{tim})$ có hai phản hồi $(\mathrm H,2)$ và $(\mathrm L,2)$, mỗi phản hồi $p=1/2$. Vậy

$$
\begin{aligned}
v_H&=1\cdot\Bigl(\tfrac12\bigl[2+\tfrac12v_H\bigr]+\tfrac12\bigl[2+\tfrac12v_L\bigr]\Bigr)&&\text{((4.5) tại }\mathrm H)\\
&=2+\tfrac14v_H+\tfrac14v_L&&\text{(khai triển)}.
\end{aligned}
$$

Hệ số $1$ ngoài cùng là $\pi(\mathrm{tim}\mid\mathrm H)$; hai hệ số $\tfrac12$ ngoài ngoặc vuông là $p(\mathrm H,2\mid\mathrm H,\mathrm{tim})$ và $p(\mathrm L,2\mid\mathrm H,\mathrm{tim})$; hệ số $\tfrac12$ trước $v_H$, $v_L$ trong ngoặc là $\gamma$. Mỗi hệ số $\tfrac14$ là tích $p\cdot\gamma$.

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
**(a)** Tính Markov của trạng thái được dùng ở Bước 1 của chứng minh Bổ đề 03.20 (qua Mệnh đề 03.14), rồi đi vào Bước 1 của Mệnh đề 03.22, nơi $\mathbb E_\pi[G_1\mid H_1=(s,a,r,s')]$ được thay bằng $v_\pi(s')$. Ở Ví dụ 03.4, hai lịch sử kết thúc ở $\mathrm L$ cho hai phân phối phần thưởng khác nhau ở bước sau, nên hai kỳ vọng của phần tương lai không thể cùng bằng $v_\pi(\mathrm L)$. Tính Markov một bước nằm trong trọng số $p(s',r\mid s,a)$ của tầng phản hồi (Bước 1 của Mệnh đề 03.22, như Bổ đề 03.19(b)); trọng số này do quy tắc sinh của Định nghĩa 03.7 cho, và quy tắc đó cũng là nguồn của các thừa số $p$ trong (3.2). Ở Ví dụ 03.4 quy tắc này hỏng, nên không có hàm $p$ chung không phụ thuộc lịch sử.

**(b)** Tính dừng của chính sách cũng được dùng ở Bước 1 của Bổ đề 03.20: tích (3.2) tại thời điểm $t$ trùng tích của quá trình xuất phát tại $s$ vì cùng hàm $\pi$ dùng ở thời điểm $t+i$ và $i$. Nếu robot Chờ ở bước chẵn và Sạc ở bước lẻ, tương lai từ $\mathrm L$ ở thời điểm lẻ khác tương lai từ $\mathrm L$ ở thời điểm $0$, nên đẳng thức này sai.

**Kiểm tra lại.** Mệnh đề 03.23 chỉ dùng (4.3) tại $t=0$ với $h_0=(s)$, nơi không có lịch sử để bỏ, và Bổ đề 03.20(d); cả hai giả thiết đi vào Mệnh đề 03.23 qua Bổ đề 03.20.
:::

Như vậy, giá trị của một chính sách thỏa phương trình Bellman kỳ vọng (Định lý 03.21), nhờ hệ thức đệ quy của lợi tức (Bổ đề 03.18), hai tầng kỳ vọng (Bổ đề 03.19) và tính Markov của phần tương lai (Bổ đề 03.20). Giá trị hành động và giá trị trạng thái biểu diễn được qua nhau (Mệnh đề 03.22, 03.23), và $q_\pi$ có phương trình riêng (Hệ quả 03.24). Tuy nhiên, Định lý 03.21 chỉ nói $v_\pi$ là một nghiệm của hệ; chưa biết hệ có nghiệm khác hay không. Trong Mục 5, chúng ta giải hệ của robot, viết hệ ở dạng ma trận và chứng minh nghiệm là duy nhất, dưới chính hai giả thiết tập trạng thái hữu hạn và $\gamma<1$ đã có trong Định lý 03.21.

<!-- note-topic-id: lec-03-part-06 -->
## 5. Đánh giá chính sách bằng hệ tuyến tính

Robot có hai phương trình Bellman với hai ẩn $v_\pi(\mathrm H)$, $v_\pi(\mathrm L)$ ở cả hai vế. Bài toán tính $v_\pi$ khi biết $p$, $\pi$ và $\gamma$ gọi là đánh giá chính sách (policy evaluation), hay bài toán dự đoán (prediction): chính sách đã cho, chỉ cần đánh giá. Đây là bài toán có mô hình, vì $p$ được dùng trực tiếp.

Trong mục này, chúng ta giải hệ của robot, đưa hệ tổng quát về dạng ma trận, chứng minh hệ có nghiệm duy nhất khi $\gamma<1$, rồi viết quy trình thành thuật toán.

### 5.1 Hệ Bellman của robot

::: example Ví dụ 03.14 (Hệ Bellman của robot và nghiệm)
**Dữ kiện.** Robot của Ví dụ 03.1; chính sách chia đều tại pin thấp (ở $\mathrm H$ luôn Tìm; ở $\mathrm L$ Chờ hoặc Sạc, mỗi hành động $1/2$); $\gamma=1/2$. Tìm từ $\mathrm H$: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$. Chờ từ $\mathrm L$: $(\mathrm L,1)$. Sạc từ $\mathrm L$: $(\mathrm H,0)$. Viết $v_H=v_\pi(\mathrm H)$, $v_L=v_\pi(\mathrm L)$.

**Kiểm tra giả thiết.** Mức pin là trạng thái Markov và hàm động lực không đổi theo thời gian; chính sách Markov dừng; $\lvert R\rvert\le3$ và $\gamma<1$. Định lý 03.21 áp dụng được.

**Lập hệ.** Phương trình của Bài tập 03.6 tại $\mathrm H$ và phương trình (4.1) tại $\mathrm L$, sau khi khai triển, là

$$
\begin{aligned}
v_H&=2+\tfrac14v_H+\tfrac14v_L,\\
v_L&=\tfrac12+\tfrac14v_H+\tfrac14v_L.
\end{aligned}
\tag{5.1}
$$

**Giải.** Hai phương trình có cùng phần $\tfrac14v_H+\tfrac14v_L$; trừ vế theo vế được $v_H-v_L=2-\tfrac12=\tfrac32$. Thế $v_H=v_L+\tfrac32$ vào phương trình thứ hai:

$$
\begin{aligned}
v_L&=\tfrac12+\tfrac14\bigl(v_L+\tfrac32\bigr)+\tfrac14v_L&&\text{(thế }v_H)\\
&=\tfrac78+\tfrac12v_L&&\text{(gom số hạng)},
\end{aligned}
$$

nên $v_L=\tfrac74$ và $v_H=\tfrac74+\tfrac32=\tfrac{13}{4}$.

**Kiểm tra lại.** Thay vào (5.1): $2+\tfrac14\bigl(\tfrac{13}4+\tfrac74\bigr)=2+\tfrac54=\tfrac{13}4$ và $\tfrac12+\tfrac54=\tfrac74$.

**Diễn giải.** Dưới chính sách chia đều tại pin thấp, robot ở pin cao có lợi tức kỳ vọng $13/4$, ở pin thấp $7/4$. Hiệu $v_H-v_L=3/2$ bằng hiệu của thưởng kỳ vọng một bước dưới chính sách ở hai trạng thái, $2-\tfrac12$, vì từ cả hai trạng thái robot chuyển tới $\mathrm H$ và $\mathrm L$ với cùng xác suất.
:::

Kỳ vọng hai bước của Mục 3, $21/8$ từ pin cao và $9/8$ từ pin thấp, nhỏ hơn giá trị thật $26/8$ và $14/8$ vì phần đuôi bị cắt ở robot có kỳ vọng dương.

Giá trị hành động cho một phép kiểm tra độc lập: theo Mệnh đề 03.23, trung bình của các $q_\pi$ theo chính sách phải bằng $v_\pi$.

::: example Ví dụ 03.15 (Kiểm tra bằng giá trị hành động)
**Dữ kiện.** Robot của Ví dụ 03.1 với chính sách chia đều tại pin thấp, $\gamma=1/2$, $v_\pi(\mathrm H)=\tfrac{13}4$, $v_\pi(\mathrm L)=\tfrac74$ (Ví dụ 03.14). Tìm từ $\mathrm L$: $(\mathrm L,2)$ hoặc $(\mathrm H,-3)$, mỗi phản hồi $1/2$, nên $r(\mathrm L,\mathrm{tim})=-\tfrac12$; Chờ từ $\mathrm L$: $(\mathrm L,1)$; Sạc từ $\mathrm L$: $(\mathrm H,0)$.

**Tính.** Theo dạng thứ hai của (4.6):

$$
\begin{aligned}
q_\pi(\mathrm L,\mathrm{tim})&=-\tfrac12+\tfrac12\bigl(\tfrac12\cdot\tfrac74+\tfrac12\cdot\tfrac{13}4\bigr)=-\tfrac12+\tfrac54=\tfrac34,\\
q_\pi(\mathrm L,\mathrm{cho})&=1+\tfrac12\cdot\tfrac74=\tfrac{15}8,\\
q_\pi(\mathrm L,\mathrm{sac})&=0+\tfrac12\cdot\tfrac{13}4=\tfrac{13}8.
\end{aligned}
$$

**Kiểm tra lại.** Theo (4.7) tại $\mathrm L$: $0\cdot\tfrac34+\tfrac12\cdot\tfrac{15}8+\tfrac12\cdot\tfrac{13}8=\tfrac{28}{16}=\tfrac74=v_\pi(\mathrm L)$. Dạng thứ nhất của (4.6) cho $q_\pi(\mathrm L,\mathrm{tim})=\tfrac12\cdot\tfrac{23}8+\tfrac12\cdot\bigl(-\tfrac{11}8\bigr)=\tfrac34$, trùng kết quả.

**Diễn giải.** Tìm có giá trị thấp nhất vì rủi ro cứu hộ. Sạc kém Chờ $\tfrac14$, không phải $1$ như phần thưởng một bước, vì Sạc đưa robot về trạng thái có giá trị cao hơn.
:::

### 5.2 Chuỗi Markov và quá trình phần thưởng Markov cảm sinh

Trong (5.1), chính sách đã biến mất khỏi hình thức của hệ: mỗi phương trình chỉ còn một số hạng tự do và hai hệ số trước $v_H$, $v_L$. Khi chính sách cố định, ta có thể gộp trước tầng hành động và tầng phản hồi thành xác suất chuyển giữa các trạng thái cùng thưởng kỳ vọng của mỗi trạng thái.

::: example Ví dụ 03.16 (Gộp các nhánh của robot dưới chính sách)
**Dữ kiện.** Robot của Ví dụ 03.1, chính sách chia đều tại pin thấp, $\gamma=1/2$. Tìm từ $\mathrm H$: phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$. Chờ từ $\mathrm L$: $(\mathrm L,1)$. Sạc từ $\mathrm L$: $(\mathrm H,0)$.

**Gộp.** Tại $\mathrm H$, chính sách chọn Tìm với xác suất $1$: xác suất chuyển $\mathrm H\to\mathrm H$ và $\mathrm H\to\mathrm L$ đều là $1/2$, thưởng kỳ vọng $2$. Tại $\mathrm L$, Chờ (xác suất $1/2$) về $\mathrm L$ với phần thưởng $1$ và Sạc (xác suất $1/2$) về $\mathrm H$ với phần thưởng $0$: xác suất chuyển $\mathrm L\to\mathrm L$ và $\mathrm L\to\mathrm H$ đều là $1/2$, thưởng kỳ vọng $\tfrac12\cdot1+\tfrac12\cdot0=\tfrac12$.

**Dạng ma trận.** Xếp trạng thái theo thứ tự $\mathrm H$, $\mathrm L$:

$$
P^\pi=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\qquad r^\pi=\begin{pmatrix}2\\1/2\end{pmatrix}.
$$

**Kiểm tra lại.** Hàng thứ nhất của $v=r^\pi+\gamma P^\pi v$ là $v_H=2+\tfrac14v_H+\tfrac14v_L$, hàng thứ hai là $v_L=\tfrac12+\tfrac14v_H+\tfrac14v_L$, đúng (5.1). Mỗi hàng của $P^\pi$ có tổng $1$.
:::

Thưởng kỳ vọng $1/2$ ở hàng $\mathrm L$ là trung bình theo chính sách; mỗi lần ở pin thấp, robot nhận $1$ hoặc $0$. Đổi chính sách thì phải gộp lại.

::: definition Định nghĩa 03.26 (Chuỗi Markov và quá trình phần thưởng Markov cảm sinh bởi chính sách)
Cho MDP hữu hạn với tập trạng thái chưa kết thúc $\mathcal S=\{s_1,\dots,s_n\}$ và chính sách Markov dừng $\pi$. Ma trận chuyển $P^\pi\in\mathbb R^{n\times n}$ và véc-tơ thưởng kỳ vọng $r^\pi\in\mathbb R^n$ dưới $\pi$ là

$$
P^\pi_{ss'}=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,p(s'\mid s,a),\qquad r^\pi(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\,r(s,a),\qquad s,s'\in\mathcal S.
\tag{5.2}
$$

Chuỗi Markov (Markov chain) cảm sinh bởi $\pi$ là cặp $(\mathcal S,P^\pi)$, mô tả dãy trạng thái chưa kết thúc khi tác tử theo $\pi$; phần xác suất còn thiếu ở mỗi hàng của $P^\pi$ là xác suất đi tới trạng thái kết thúc. Quá trình phần thưởng Markov (Markov reward process, MRP) cảm sinh bởi $\pi$ là bộ $(\mathcal S,P^\pi,r^\pi,\gamma)$.
:::

Phần tử $P^\pi_{ss'}$ là xác suất chuyển sau khi đã gộp hành động, $r^\pi(s)$ là thưởng kỳ vọng một bước tại $s$. Mỗi hàng của $P^\pi$ có tổng không quá $1$, bằng $1$ khi không có trạng thái kết thúc như ở robot; theo Mệnh đề 03.14, dãy trạng thái dưới $\pi$ vẫn có tính Markov. Bộ MRP ghi kèm $\gamma$ vì nó được lập ra để tính giá trị của một chính sách đã cố định, và hệ của nó chứa $\gamma$ trong mọi hệ số, như hệ số $\tfrac14=\gamma\cdot\tfrac12$ của (5.1); bộ $\mathcal M$ của Định nghĩa 03.7 chỉ mô tả môi trường, nên $\gamma$, thuộc tiêu chuẩn đánh giá, đứng ngoài bộ đó (tiểu mục 1.5).

Định nghĩa 03.26 nối MDP với chuỗi Markov và quá trình phần thưởng Markov của Bài giảng gốc (2025–2026, trang 30, 34). Ở đó MDP được dựng như MRP có thêm quyết định (trang 49); ở đây chúng ta đi theo chiều ngược lại, cố định quyết định để từ MDP thu về MRP, đúng nội dung bài 4 của Bài tập tuần 2 (2025–2026).

### 5.3 Dạng ma trận và nghiệm duy nhất

Với $P^\pi$ và $r^\pi$, phương trình Bellman của mọi trạng thái gom được thành một phương trình véc-tơ.

::: proposition Mệnh đề 03.27 (Phương trình Bellman dạng ma trận)
**Giả thiết.** Như Định lý 03.21; $\mathcal S=\{s_1,\dots,s_n\}$; $v\in\mathbb R^n$ là véc-tơ cột với $v_i=v_\pi(s_i)$; $P^\pi$, $r^\pi$ theo (5.2).

**Kết luận.**

$$
v=r^\pi+\gamma P^\pi v\quad\Longleftrightarrow\quad(I-\gamma P^\pi)\,v=r^\pi .
\tag{5.3}
$$

**Điều kiện áp dụng.** Tập trạng thái hữu hạn, để $P^\pi$ là ma trận hữu hạn.

**Phạm vi.** Mệnh đề nói $v_\pi$ là một nghiệm của (5.3); tính duy nhất là Định lý 03.28.
:::

::: proof Chứng minh Mệnh đề 03.27
**Bước 1 (khai triển vế phải của (4.5)).** Theo Mệnh đề 03.22 và 03.23,

$$
\begin{aligned}
v_\pi(s)&=\sum_a\pi(a\mid s)\Bigl[r(s,a)+\gamma\sum_{s'\in\mathcal S^+}p(s'\mid s,a)\,v_\pi(s')\Bigr]\\
&=\sum_a\pi(a\mid s)\,r(s,a)+\gamma\sum_{s'\in\mathcal S}\Bigl(\sum_a\pi(a\mid s)\,p(s'\mid s,a)\Bigr)v_\pi(s')\\
&=r^\pi(s)+\gamma\sum_{s'\in\mathcal S}P^\pi_{ss'}\,v_\pi(s').
\end{aligned}
$$

Dòng thứ hai đổi thứ tự hai tổng hữu hạn và bỏ các trạng thái kết thúc, nơi $v_\pi=0$; dòng thứ ba là định nghĩa (5.2).

**Bước 2 (viết thành véc-tơ).** Tổng $\sum_{s'}P^\pi_{ss'}v_\pi(s')$ là thành phần thứ $s$ của tích $P^\pi v$, nên $n$ đẳng thức của Bước 1 là $v=r^\pi+\gamma P^\pi v$, tức $(I-\gamma P^\pi)v=r^\pi$. $\square$
:::

Câu hỏi còn lại là hệ (5.3) có thể có nghiệm khác $v_\pi$ hay không; nếu có, giải hệ chưa chắc cho ra giá trị của chính sách. Định lý sau loại trừ khả năng đó khi $\gamma<1$, bằng chuẩn cực đại $\lVert x\rVert_\infty=\max_i\lvert x_i\rvert$.

::: theorem Định lý 03.28 (Nghiệm duy nhất của hệ đánh giá chính sách)
**Giả thiết.** MDP hữu hạn với $n$ trạng thái chưa kết thúc; chính sách Markov dừng $\pi$; phần thưởng bị chặn; $0\le\gamma<1$; $P^\pi$, $r^\pi$ theo (5.2).

**Kết luận.**

(a) Ma trận $I-\gamma P^\pi$ khả nghịch.

(b) Hệ (5.3) có nghiệm duy nhất, và nghiệm đó là giá trị của chính sách:

$$
v_\pi=(I-\gamma P^\pi)^{-1}r^\pi .
\tag{5.4}
$$

(c) Giá trị có khai triển chuỗi Neumann (Neumann series)

$$
v_\pi=\sum_{k=0}^{\infty}\gamma^k(P^\pi)^kr^\pi,
\tag{5.5}
$$

và tổng riêng $K$ số hạng đầu sai khác $v_\pi$ không quá $\gamma^K\lVert v_\pi\rVert_\infty$ theo chuẩn cực đại.

**Điều kiện áp dụng.** Tập trạng thái hữu hạn và $\gamma<1$.

**Phạm vi.** Định lý không áp dụng cho $\gamma=1$ mà không có thêm điều kiện; Sutton và Barto (2018, §4.1, tr. 74) nêu rằng nghiệm tồn tại và duy nhất khi $\gamma<1$ hoặc khi dưới $\pi$ mọi trạng thái bảo đảm đi tới kết thúc. Định lý nói về một chính sách cho trước, không về chính sách tối ưu.
:::

::: proof Chứng minh Định lý 03.28
**Bước 1 (phép nhân $P^\pi$ không tăng chuẩn cực đại).** Các phần tử của $P^\pi$ không âm và mỗi hàng có tổng không quá $1$ (Định nghĩa 03.26). Với mọi $x\in\mathbb R^n$ và mọi hàng $i$,

$$
\begin{aligned}
\bigl\lvert(P^\pi x)_i\bigr\rvert&=\Bigl\lvert\sum_jP^\pi_{ij}x_j\Bigr\rvert\\
&\le\sum_jP^\pi_{ij}\lvert x_j\rvert&&\text{(bất đẳng thức tam giác, }P^\pi_{ij}\ge0)\\
&\le\Bigl(\sum_jP^\pi_{ij}\Bigr)\lVert x\rVert_\infty&&\text{(}\lvert x_j\rvert\le\lVert x\rVert_\infty)\\
&\le\lVert x\rVert_\infty&&\text{(tổng hàng không quá }1).
\end{aligned}
$$

Lấy cực đại theo $i$: $\lVert P^\pi x\rVert_\infty\le\lVert x\rVert_\infty$.

**Bước 2 (phần a).** Giả sử $(I-\gamma P^\pi)x=0$, tức $x=\gamma P^\pi x$. Theo Bước 1, $\lVert x\rVert_\infty=\gamma\lVert P^\pi x\rVert_\infty\le\gamma\lVert x\rVert_\infty$, nên $(1-\gamma)\lVert x\rVert_\infty\le0$. Vì $\gamma<1$, ta có $x=0$. Ma trận vuông chỉ có nghiệm tầm thường cho hệ thuần nhất thì khả nghịch.

**Bước 3 (phần b).** Theo Mệnh đề 03.27, véc-tơ $v_\pi$ thỏa (5.3); mỗi thành phần của nó là số thực nhờ Mệnh đề 03.11. Theo phần (a), hệ (5.3) có đúng một nghiệm, $(I-\gamma P^\pi)^{-1}r^\pi$, nên nghiệm đó là $v_\pi$.

**Bước 4 (khai triển lặp, phần c).** Ta chứng minh bằng quy nạp theo $K\ge0$ rằng

$$
v_\pi=\sum_{k=0}^{K-1}\gamma^k(P^\pi)^kr^\pi+\gamma^K(P^\pi)^Kv_\pi .
$$

Với $K=0$, tổng rỗng và đẳng thức là $v_\pi=v_\pi$. Nếu đẳng thức đúng với $K$, thay $v_\pi=r^\pi+\gamma P^\pi v_\pi$ (Mệnh đề 03.27) vào số hạng cuối:

$$
\gamma^K(P^\pi)^Kv_\pi=\gamma^K(P^\pi)^Kr^\pi+\gamma^{K+1}(P^\pi)^{K+1}v_\pi ,
$$

đó là đẳng thức với $K+1$.

**Bước 5 (qua giới hạn).** Áp dụng Bước 1 $K$ lần: $\lVert\gamma^K(P^\pi)^Kv_\pi\rVert_\infty\le\gamma^K\lVert v_\pi\rVert_\infty$. Theo Bước 4, đây là sai khác giữa $v_\pi$ và tổng riêng $K$ số hạng. Vì $\gamma<1$, sai khác tiến tới $0$, nên chuỗi (5.5) hội tụ về $v_\pi$. $\square$
:::

Định lý 03.28 đọc như sau: khi $\gamma<1$ và số trạng thái hữu hạn, hệ phương trình Bellman của một chính sách có đúng một nghiệm, và nghiệm đó là giá trị của chính sách. Giải hệ bằng bất kỳ phương pháp đúng nào cũng cho $v_\pi$.

Khai triển (5.5) cũng có nghĩa trực tiếp. Cộng (3.2) theo mọi hành động, phần thưởng và trạng thái trung gian, phần tử $(s,s'')$ của $(P^\pi)^k$ là xác suất đi từ $s$ tới trạng thái chưa kết thúc $s''$ sau đúng $k$ bước; vì vậy thành phần thứ $s$ của $(P^\pi)^kr^\pi$ là $\mathbb E_\pi[R_{k+1}\mid S_0=s]$, với quy ước $R_{k+1}=0$ sau thời điểm kết thúc (Nhận xét 03.10). Đổi thứ tự kỳ vọng và tổng chuỗi trong (3.3) là hợp lệ vì phần đuôi sau $K$ số hạng bị chặn bởi $\gamma^KM/(1-\gamma)$ trên mọi quỹ đạo; do đó (5.5) là (3.3) viết theo từng bước thời gian.

Hai giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ $\gamma<1$: với robot và $\gamma=1$, mỗi hàng của $P^\pi$ có tổng $1$, nên véc-tơ toàn số $1$ thỏa $(I-P^\pi)\mathbf 1=0$ và $I-P^\pi$ không khả nghịch. Hệ (5.3) của robot khi đó là $\tfrac12v_H-\tfrac12v_L=2$ và $-\tfrac12v_H+\tfrac12v_L=\tfrac12$; cộng hai phương trình được $0=\tfrac52$, nên hệ vô nghiệm.
- Bỏ tập trạng thái hữu hạn: $P^\pi$ không còn là ma trận hữu hạn, và lập luận "ma trận vuông có hạt nhân tầm thường thì khả nghịch" ở Bước 2 không áp dụng; khi đó cần lập luận toán tử co của Bài 04.

Bước 2 và Bước 5 của chứng minh dùng $\gamma<1$; Bước 2 và Bước 3 dùng tính hữu hạn.

::: example Ví dụ 03.17 (Nghịch đảo cho robot)
**Dữ kiện.** Ma trận chuyển và véc-tơ thưởng kỳ vọng của robot dưới chính sách chia đều tại pin thấp (Ví dụ 03.16), theo thứ tự $\mathrm H$, $\mathrm L$:

$$
P^\pi=\begin{pmatrix}1/2&1/2\\1/2&1/2\end{pmatrix},\qquad r^\pi=\begin{pmatrix}2\\1/2\end{pmatrix},\qquad\gamma=\tfrac12 .
$$

**Nghịch đảo.**

$$
I-\gamma P^\pi=\begin{pmatrix}3/4&-1/4\\-1/4&3/4\end{pmatrix},\qquad\det=\tfrac9{16}-\tfrac1{16}=\tfrac12,\qquad(I-\gamma P^\pi)^{-1}=\begin{pmatrix}3/2&1/2\\1/2&3/2\end{pmatrix}.
$$

**Tính.** Theo (5.4): $v_H=\tfrac32\cdot2+\tfrac12\cdot\tfrac12=\tfrac{13}4$ và $v_L=\tfrac12\cdot2+\tfrac32\cdot\tfrac12=\tfrac74$.

**Kiểm tra lại.** Kết quả trùng phép khử thế của Ví dụ 03.14; tích $(I-\gamma P^\pi)(I-\gamma P^\pi)^{-1}$ có hàng thứ nhất $\bigl(\tfrac98-\tfrac18,\ \tfrac38-\tfrac38\bigr)=(1,0)$.
:::

Định lý 03.28 mạnh hơn Định lý 03.21: nó nói $v_\pi$ là nghiệm duy nhất và cho công thức tính, mà không thêm giả thiết mới. MDP hữu hạn và $\gamma<1$ đã có trong Định lý 03.21, nơi chúng bảo đảm lợi tức bị chặn (tập $\mathcal R$ hữu hạn cho $\lvert R_k\rvert\le M$) và có kỳ vọng hữu hạn; trong Định lý 03.28, tập trạng thái hữu hạn và $\gamma<1$ làm $I-\gamma P^\pi$ khả nghịch. Lập luận ở Bước 1–2 là dạng đầu tiên của tính co mà Bài 04 dùng để chứng minh hội tụ của các phép lặp; Puterman (1994, §6.1) trình bày cùng kết quả ở mức tổng quát hơn.

### 5.4 Thuật toán đánh giá chính sách bằng giải hệ

Ví dụ 03.14, 03.16 và 03.17 đã thực hiện bằng tay mọi bước: lập $P^\pi$ và $r^\pi$ từ $p$ và $\pi$, lập ma trận $I-\gamma P^\pi$, giải hệ, kiểm tra lại. Thuật toán sau viết các bước đó cho MDP hữu hạn bất kỳ.

::: algorithm Thuật toán 03.29 (Đánh giá chính sách bằng giải hệ tuyến tính)
**Đầu vào.** MDP hữu hạn với các trạng thái chưa kết thúc $s_1,\dots,s_n$ theo một thứ tự cố định; hàm động lực $p$ hoặc hai mảng $p(s'\mid s,a)$, $r(s,a)$; chính sách Markov dừng $\pi$; hệ số chiết khấu $\gamma$.

**Đầu ra.** Véc-tơ $v\in\mathbb R^n$ với $v_i=v_\pi(s_i)$; giá trị tại trạng thái kết thúc bằng $0$.

**Giả thiết.** Trạng thái có tính Markov, hàm động lực không đổi theo thời gian, phần thưởng bị chặn, $0\le\gamma<1$ (Định lý 03.28). Đây là bài toán dự đoán có mô hình.

**Khởi tạo.** $P^\pi\leftarrow0\in\mathbb R^{n\times n}$, $r^\pi\leftarrow0\in\mathbb R^n$.

**Tham số.** $\gamma$; dung sai làm tròn $\delta>0$ cho bước kiểm tra, chẳng hạn $\delta=10^{-9}$.

1. Kiểm tra đầu vào, trong dung sai $\delta$: mọi $\pi(\cdot\mid s)$ không âm và có tổng $1$; nếu đầu vào là hàm động lực, mọi $p(\cdot,\cdot\mid s,a)$ không âm và có tổng $1$ trên $\mathcal S^+\times\mathcal R$ theo (1.3); nếu đầu vào là hai mảng, mọi $p(\cdot\mid s,a)$ không âm và có tổng $1$ trên $\mathcal S^+$. Nếu không, dừng và báo lỗi dữ liệu.
2. Nếu chỉ có $p(s',r\mid s,a)$, tính $p(s'\mid s,a)$ theo (1.5) và $r(s,a)$ theo (1.6) cho mọi cặp hợp lệ.
3. Với mỗi $s$: $r^\pi(s)\leftarrow\sum_a\pi(a\mid s)\,r(s,a)$; với mỗi $s'\in\mathcal S$: $P^\pi_{ss'}\leftarrow\sum_a\pi(a\mid s)\,p(s'\mid s,a)$. Cột của trạng thái kết thúc không được đưa vào $P^\pi$. Kiểm tra mọi hàng của $P^\pi$ có tổng không quá $1+\delta$.
4. Lập $A\leftarrow I-\gamma P^\pi$.
5. Giải hệ $Av=r^\pi$ bằng phép khử Gauss, không tính nghịch đảo tường minh.
6. Tính phần dư $\rho\leftarrow\lVert v-r^\pi-\gamma P^\pi v\rVert_\infty$. Nếu $\rho>\delta\max(1,\lVert r^\pi\rVert_\infty)$, báo sai số làm tròn lớn.
7. Trả $v$.

**Điều kiện dừng.** Thuật toán trực tiếp, không có vòng lặp: dừng sau bước 7 với số phép tính hữu hạn. Bước 6 là phép kiểm tra số học, không phải tiêu chuẩn hội tụ.

**Chi phí.** Bước 1–2: tỉ lệ với số bộ $(s,a,s',r)$ có $p>0$. Bước 3: $O(n^2\max_s\lvert\mathcal A(s)\rvert)$. Bước 5: cỡ $n^3$ phép tính và $O(n^2)$ bộ nhớ. Bước 6: $O(n^2)$.
:::

Áp dụng Thuật toán 03.29 cho robot, bước 3 cho đúng $P^\pi$, $r^\pi$ của Ví dụ 03.16, bước 4 cho ma trận $I-\gamma P^\pi$ của Ví dụ 03.17, bước 5 cho $(13/4,\,7/4)$ như Ví dụ 03.14, và bước 6 cho phần dư $0$. Ví dụ tính tay, công thức (5.4) và thuật toán cho cùng một kết quả.

::: remark Nhận xét 03.30 (Giới hạn của giải hệ trực tiếp)
- **Quy mô.** Chi phí cỡ $n^3$ chấp nhận được khi $n$ vài trăm hay vài nghìn; với $n=10^6$ trạng thái, ma trận $P^\pi$ có $10^{12}$ phần tử và phép khử cần cỡ $10^{18}$ phép tính. Bài giảng gốc (2025–2026, trang 48) nêu hạn chế này và chuyển sang phương pháp lặp; Bài 04 xây dựng đánh giá chính sách lặp dựa trên (5.5).
- **Cần mô hình.** Bước 2–3 dùng $p$. Khi chỉ có mẫu chuyển, $v_\pi$ phải được ước lượng từ dữ liệu (Bài 05).
:::

**Trong thực hành.** Notebook CartPole của Bài 04 giải hệ (5.3) bằng `np.linalg.solve` cho một chính sách trên $324$ ô, cỡ $324^3\approx3{,}4\cdot10^7$ phép tính; chia mỗi biến thành $10$ khoảng thì $n=10^4$ và chi phí cỡ $10^{12}$. Tình huống 03.2 phân tích kết quả của phép giải này.

::: remark Nhận xét 03.31 (So sánh giá trị hành động chưa chứng minh tối ưu)
Ví dụ 03.15 cho $q_\pi(\mathrm L,\mathrm{cho})=15/8>q_\pi(\mathrm L,\mathrm{sac})=13/8$. Bất đẳng thức này so sánh hai thí nghiệm chỉ khác nhau ở hành động đầu, với phần tiếp diễn theo cùng chính sách $\pi$; nó chưa cho biết chính sách nào tốt nhất, vì không chính sách nào khác được đánh giá. Muốn kết luận về một chính sách mới, phải đánh giá chính sách mới bằng chính Thuật toán 03.29, như Bài tập 03.8; định lý nối hai việc này là định lý cải thiện chính sách của Bài 04.
:::

::: exercise Bài tập 03.8
**Dữ kiện.** Robot của Ví dụ 03.1 với chính sách luôn Chờ tại pin thấp: ở $\mathrm H$ luôn Tìm (phần thưởng $2$, về $\mathrm H$ hoặc $\mathrm L$ mỗi trạng thái $1/2$); ở $\mathrm L$ luôn Chờ (phần thưởng $1$, ở lại $\mathrm L$). $\gamma=1/2$.

**Yêu cầu.** (a) Lập $P^\pi$ và $r^\pi$ theo thứ tự $\mathrm H$, $\mathrm L$. (b) Giải $(I-\gamma P^\pi)v=r^\pi$. (c) So sánh với giá trị $(13/4,\,7/4)$ của chính sách chia đều tại pin thấp.
:::

::: hint
Phương trình của $\mathrm L$ chỉ chứa $v_L$; giải nó trước.
:::

::: solution
**(a)** Hàng $\mathrm H$ giữ nguyên như Ví dụ 03.16: $(1/2,\,1/2)$, thưởng kỳ vọng $2$. Hàng $\mathrm L$: luôn Chờ nên luôn về $\mathrm L$ với phần thưởng $1$.

$$
P^\pi=\begin{pmatrix}1/2&1/2\\0&1\end{pmatrix},\qquad r^\pi=\begin{pmatrix}2\\1\end{pmatrix}.
$$

**(b)** Hệ (5.3) là $v_H=2+\tfrac14v_H+\tfrac14v_L$ và $v_L=1+\tfrac12v_L$. Phương trình thứ hai cho $v_L=2$. Thế vào phương trình thứ nhất: $\tfrac34v_H=2+\tfrac12=\tfrac52$, nên $v_H=\tfrac{10}3$.

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

Như vậy, dưới chính sách chia đều tại pin thấp, robot có $v_\pi(\mathrm H)=13/4$ và $v_\pi(\mathrm L)=7/4$ (Ví dụ 03.14). Chuỗi kết quả của mục đi từ phép gộp chính sách vào mô hình (Định nghĩa 03.26) tới dạng ma trận (Mệnh đề 03.27), định lý nghiệm duy nhất (Định lý 03.28) và quy trình giải trực tiếp (Thuật toán 03.29).

Tuy nhiên, ba giới hạn còn lại: phép giải cần biết $p$; chi phí cỡ $n^3$ không dùng được cho tập trạng thái lớn; và đánh giá một chính sách chưa cho biết chính sách nào tốt hơn. Bài 04 giải quyết giới hạn thứ hai và thứ ba khi vẫn biết mô hình; Bài 05 và Bài 06 bỏ giả thiết biết $p$.

<!-- note-topic-id: lec-03-part-07 -->
## Tình huống áp dụng và ứng dụng

Hai tình huống dưới đây áp dụng Thuật toán 03.29: một lưới $25$ trạng thái thỏa mọi giả thiết của Định lý 03.28, và CartPole rời rạc hóa, nơi giả thiết Markov không được bảo đảm.

::: application Tình huống 03.1 (Đánh giá chính sách chọn đều trên lưới 5×5)
**Bài toán và môi trường.** Lưới $5\times5$ của Sutton và Barto (2018, ví dụ 3.5, tr. 60). Mỗi ô là một trạng thái. Ở mỗi ô có bốn hành động bắc, nam, đông, tây, đưa tác tử sang ô kề theo hướng đó một cách tất định. Hành động đi ra ngoài lưới giữ nguyên ô và cho phần thưởng $-1$. Ở ô $\mathrm A$ (hàng 1, cột 2), mọi hành động đưa tới ô $\mathrm A'$ (hàng 5, cột 2) với phần thưởng $+10$; ở ô $\mathrm B$ (hàng 1, cột 4), mọi hành động đưa tới ô $\mathrm B'$ (hàng 3, cột 4) với phần thưởng $+5$. Mọi bước khác cho phần thưởng $0$. Nhiệm vụ tiếp diễn. Chính sách chọn mỗi hành động với xác suất $1/4$ ở mọi ô; $\gamma=0{,}9$. Cần tính giá trị của chính sách tại mọi ô.

**Mô hình hóa.** MDP hữu hạn (Định nghĩa 03.7): $\mathcal S$ gồm $25$ ô, không có trạng thái kết thúc; $\mathcal A(s)$ gồm bốn hành động; $\mathcal R=\{-1,0,5,10\}$; với mỗi $(s,a)$, $p(s',r\mid s,a)=1$ cho đúng một cặp $(s',r)$. Chính sách $\pi(a\mid s)=1/4$ là chính sách Markov dừng (Định nghĩa 03.13).

**Xác minh giả thiết.**

- Tính Markov (Định nghĩa 03.2): ô hiện tại và hành động xác định duy nhất ô kế tiếp và phần thưởng, nên lịch sử không cho thêm thông tin.
- Tính dừng: quy luật không đổi theo thời gian.
- Phần thưởng bị chặn với $M=10$ và $\gamma=0{,}9<1$, nên $\lvert G_t\rvert\le100$ (Mệnh đề 03.11).
- Tập trạng thái hữu hạn, $n=25$: Định lý 03.28 áp dụng, hệ có nghiệm duy nhất.

**Áp dụng Thuật toán 03.29.** Bước 3 cho $r^\pi=0$ ở ô bên trong, $-\tfrac14$ ở ô cạnh không phải góc, $-\tfrac12$ ở ô góc, $10$ ở $\mathrm A$ và $5$ ở $\mathrm B$. Hàng của $P^\pi$ có phần tử $\tfrac14$ ở mỗi ô tới được; tại ô cạnh, chính ô đó nhận $\tfrac14$ cho mỗi hướng đi ra ngoài; $P^\pi_{\mathrm A\mathrm A'}=P^\pi_{\mathrm B\mathrm B'}=1$. Bước 5 giải hệ $25$ ẩn; phần (b) của hình dưới ghi nghiệm làm tròn một chữ số, các giá trị thập phân dưới đây được tính lại bằng phép khử Gauss trên số hữu tỉ.

**Kiểm tra lại bằng phương trình Bellman.** Theo (4.5), tại $\mathrm A$ chỉ có một phản hồi, nên

$$
v_\pi(\mathrm A)=10+0{,}9\,v_\pi(\mathrm A')=10+0{,}9\cdot(-1{,}3452)\approx8{,}789 ,
$$

trùng nghiệm $8{,}789$. Tại $\mathrm B$: $5+0{,}9\cdot0{,}358\approx5{,}322$, trùng nghiệm $5{,}322$.

**Diễn giải.** $v_\pi(\mathrm A)\approx8{,}8<10$ vì bước nhảy đưa tác tử tới $\mathrm A'$ ở cạnh dưới, nơi chính sách chọn đều thường đi ra ngoài lưới, nên $v_\pi(\mathrm A')<0$. Ngược lại $v_\pi(\mathrm B)\approx5{,}3>5$ vì $\mathrm B'$ có giá trị dương.

**Giới hạn.** Đây là bài toán dự đoán cho một chính sách cố định và kém; tìm chính sách tốt hơn là việc của Bài 04.

**Dẫn ngược.** Định nghĩa 03.2, 03.7, 03.13 (mô hình hóa); Mệnh đề 03.11 và Định lý 03.28 (kiểm giả thiết); Mệnh đề 03.27 và Thuật toán 03.29 (giải); Định lý 03.21 (kiểm tra lại và diễn giải).
:::

![Hai lưới 5 hàng 5 cột. Lưới trái, (a) động lực đặc biệt: ô A ở hàng 1 cột 2, ô A' ở hàng 5 cột 2, ô B ở hàng 1 cột 4, ô B' ở hàng 3 cột 4; mũi tên từ A xuống A' ghi +10, mũi tên từ B xuống B' ghi +5. Lưới phải, (b) giá trị v_π của chính sách chọn đều, γ = 0,9, theo hàng từ trên xuống: 3,3 8,8 4,4 5,3 1,5; 1,5 3,0 2,3 1,9 0,5; 0,1 0,7 0,7 0,4 −0,4; −1,0 −0,4 −0,4 −0,6 −1,2; −1,9 −1,3 −1,2 −1,4 −2,0. Chú thích: bốn hành động bắc, nam, đông, tây, mỗi hành động xác suất 1/4; tại A mọi hành động tới A' với thưởng +10, tại B tới B' với thưởng +5; bước ra ngoài lưới giữ nguyên ô với thưởng −1; các bước khác thưởng 0.](img/lec-03/gridworld-5x5.svg)

Phần (a) của hình vẽ hai bước nhảy có phần thưởng dương; phần (b) xếp nghiệm theo vị trí ô. Theo cột 2, giá trị giảm từ $8{,}8$ ở $\mathrm A$ xuống $-1{,}3$ ở $\mathrm A'$, đúng phương trình $v_\pi(\mathrm A)=10+0{,}9\,v_\pi(\mathrm A')$; các số trùng hình 3.2 của Sutton và Barto (2018) sau khi làm tròn.

::: application Tình huống 03.2 (CartPole rời rạc hóa: khi trạng thái không còn bảo đảm tính Markov)
**Bài toán và môi trường.** Môi trường `CartPole-v1` của Gymnasium trong notebook thực hành của Bài 04. Trạng thái vật lý $(x,\dot x,\theta,\dot\theta)$ gồm vị trí, vận tốc xe, góc của cột và vận tốc góc, với động lực tất định. Hành động $0$ đẩy trái, $1$ đẩy phải; phần thưởng $+1$ ở mọi bước. Lượt kết thúc khi $\lvert\theta\rvert>12^\circ$ hoặc $\lvert x\rvert>2{,}4$; giới hạn $500$ bước là cắt ngắn do cấu hình, không đưa vào mô hình.

**Mô hình hóa.** Notebook chia $x$, $\dot x$ thành $3$ khoảng và $\theta$, $\dot\theta$ thành $6$ khoảng, được $3\cdot3\cdot6\cdot6=324$ ô cộng một trạng thái kết thúc. Với mỗi ô và mỗi hành động, notebook lấy $N_{\text{mẫu}}=200$ trạng thái vật lý đều trong ô, chạy một bước và đếm ô kế tiếp, được $\hat p(s'\mid s,a)$; thưởng kỳ vọng ước lượng bằng $1$. Chính sách $\pi_0$, gọi là luật theo dấu góc, đẩy phải khi $\theta\ge0$ và đẩy trái khi $\theta<0$. Chọn $\gamma=0{,}99$.

**Xác minh giả thiết.**

- Tập hữu hạn ($n=324$), phần thưởng bị chặn ($M=1$), $\gamma<1$, và $\pi_0$ là chính sách Markov dừng trên ô: các giả thiết này thỏa.
- Tính Markov của ô (Định nghĩa 03.2) không được bảo đảm, vì một ô chứa vô số trạng thái vật lý có thể sang các ô khác nhau. Trong notebook, phân phối $\hat p(\cdot\mid s,a)$ của cặp (ô $66$, hành động $0$) có $11$ trạng thái kế tiếp với xác suất dương và entropy $1{,}815$ nat; entropy trung bình của các phân phối $\hat p(\cdot\mid s,a)$ trên mọi cặp là $1{,}052$ nat (một lần chạy đã nhúng trong notebook). Ô kế tiếp phụ thuộc vị trí bên trong ô hiện tại; nếu dãy ô đã đi qua mang thông tin về vị trí đó, (1.2) sai. Notebook nêu rằng entropy dương chưa đủ để kết luận và đề xuất kiểm tra trực tiếp trên quỹ đạo.
- Bảng $\hat p$ là hàm động lực của một MDP thay thế $(\hat p,\hat r)$, xây dựng với giả thiết trạng thái phân bố đều trong mỗi ô; MDP thay thế thỏa Định nghĩa 03.7 theo cách xây dựng.

**Áp dụng.** Giải hệ (5.3) cho $\pi_0$ trên MDP thay thế cho phần dư cỡ $2{,}1\cdot10^{-14}$ và các giá trị trong khoảng $6{,}335$ tới $31{,}080$, dưới cận $1/(1-\gamma)=100$ của Mệnh đề 03.11. Theo Định lý 03.28, đây là giá trị chính xác của $\pi_0$ trong MDP thay thế.

**Hậu quả quan sát được.** Notebook so giá trị dự đoán với lợi tức thật cho một chính sách khác, chính sách Markov dừng trên ô mà phương pháp của Bài 04 tìm được trên cùng MDP thay thế; ở đây chỉ cần biết nó là một chính sách cố định. Trên $100$ lượt trong môi trường liên tục, giá trị dự đoán trung bình tại các ô xuất phát là $84{,}473$, lợi tức chiết khấu thực tế trung bình là $95{,}377$, sai số chuẩn $0{,}370$ (một lần chạy đã nhúng trong notebook). Chênh lệch $10{,}904$ không đến từ sai số giải hệ, sai số thống kê hay cắt ngắn ở $500$ bước (mức giảm tối đa $0{,}657$); nó đến từ khoảng cách giữa MDP thay thế và quá trình thật nhìn qua các ô.

**Diễn giải.** Định lý 03.28 vẫn đúng, nhưng nó nói về MDP thay thế. Bước có thể hỏng khi áp dụng cho CartPole là Bổ đề 03.20: kỳ vọng của phần tương lai sau một lịch sử kết thúc ở ô $s$ chỉ bằng một số chung khi ô có tính Markov. Định lý 03.28 kiểm soát sai số giải hệ, không kiểm soát khoảng cách giữa mô hình và môi trường.

**Giới hạn và dẫn ngược.** Con số $10{,}904$ phụ thuộc cách chia ô và hạt giống. Tình huống dùng Định nghĩa 03.2 (giả thiết bị vi phạm), Định nghĩa 03.4, 03.7 (MDP thay thế), Mệnh đề 03.11 (cận $100$), Bổ đề 03.20 và Định lý 03.21 (bước dùng tính Markov), Định lý 03.28 và Mệnh đề 03.27 (giải hệ $324$ ẩn).
:::

**Ứng dụng.** Các khái niệm của chương được dùng lại trong các bài sau của học phần.

- **Bài 04, giải MDP bằng quy hoạch động.** Đánh giá chính sách lặp tính tổng riêng của chuỗi Neumann (5.5) bằng phép lặp $v\leftarrow r^\pi+\gamma P^\pi v$; cải thiện chính sách so sánh các $q_\pi(s,a)$ tính bằng (4.6).
- **Bài 05, dự đoán phi mô hình.** Phương pháp Monte Carlo ước lượng $v_\pi(s)$ bằng trung bình các lợi tức quan sát được từ $s$; TD(0) dùng mẫu của vế phải (4.5) làm mục tiêu bootstrap, theo cập nhật ở đoạn "Trong thực hành" sau Định lý 03.21.
- **Bài 06, điều khiển phi mô hình.** Sarsa dùng mẫu của vế phải (4.8); Q-learning dùng dạng có cực đại của cùng cấu trúc phần thưởng một bước cộng giá trị chiết khấu của trạng thái kế tiếp.
- **Bài 07, xấp xỉ hàm.** Khi $n$ quá lớn cho Thuật toán 03.29, giá trị được biểu diễn bằng hàm có tham số trên trạng thái liên tục; đặc trưng có thể mất tính Markov như ô CartPole.
- **Bài 08, Deep Q-learning.** Bộ nhớ phát lại lưu các bộ $(S_t,A_t,R_{t+1},S_{t+1})$ của Định nghĩa 03.1; mục tiêu học của mạng dùng phần thưởng một bước cộng giá trị chiết khấu do mạng mục tiêu tính tại trạng thái kế tiếp.

<!-- note-topic-id: lec-03-part-08 -->
## Tóm tắt chương

Câu hỏi xuất phát là so sánh giá trị dài hạn của các cách hành động của robot thu gom lon khi phản hồi là ngẫu nhiên. Chúng ta mô tả môi trường bằng hàm động lực $p(s',r\mid s,a)$, với giả thiết trạng thái có tính Markov (Định nghĩa 03.2, 03.4), rồi gom thành MDP hữu hạn (Định nghĩa 03.7). Chuỗi phần thưởng được gộp thành lợi tức chiết khấu, hữu hạn khi phần thưởng bị chặn và $\gamma<1$ (Định nghĩa 03.9, Mệnh đề 03.11). Cố định chính sách Markov dừng, chúng ta định nghĩa giá trị trạng thái và giá trị hành động (Định nghĩa 03.13, 03.15, 03.16). Tách bước đầu của lợi tức và dùng tính Markov của phần tương lai (Bổ đề 03.18–03.20), chúng ta chứng minh phương trình Bellman kỳ vọng cho $v_\pi$ và $q_\pi$ (Định lý 03.21, Hệ quả 03.24). Hai trong các giả thiết của Định lý 03.21, MDP hữu hạn và $\gamma<1$, vừa cho lợi tức có kỳ vọng hữu hạn vừa làm $I-\gamma P^\pi$ khả nghịch, nên không cần giả thiết mới để hệ Bellman có nghiệm duy nhất $v_\pi=(I-\gamma P^\pi)^{-1}r^\pi$ (Định lý 03.28), tính được bằng giải hệ trực tiếp (Thuật toán 03.29); với robot, $v_\pi=(13/4,\,7/4)$ và $q_\pi(\mathrm L,\cdot)=(3/4,\,15/8,\,13/8)$, nên Chờ hơn Sạc $1/4$ chứ không phải $1$ như phần thưởng một bước. Bốn giới hạn còn lại là cần biết $p$, chi phí cỡ $n^3$, việc chỉ đánh giá chứ chưa chọn được chính sách, và trạng thái phải có tính Markov (Tình huống 03.2). Bài 04 xử lý chi phí giải hệ và việc chọn chính sách khi vẫn biết mô hình; Bài 05–06 bỏ giả thiết biết $p$. Giới hạn Markov xuất hiện lại ở Bài 07, khi đặc trưng của trạng thái có thể mất tính Markov.

**Định nghĩa và kết quả theo mục.**

- Mục 1: quỹ đạo và lịch sử (Định nghĩa 03.1); tính Markov (Định nghĩa 03.2), là tính chất của biểu diễn trạng thái (Nhận xét 03.3); hàm động lực (Định nghĩa 03.4), tính dừng khác tính Markov (Nhận xét 03.5); xác suất chuyển và thưởng kỳ vọng suy từ $p$ (Mệnh đề 03.6); MDP hữu hạn (Định nghĩa 03.7).
- Mục 2: lượt, nhiệm vụ có kết thúc và tiếp diễn (Định nghĩa 03.8); lợi tức chiết khấu (Định nghĩa 03.9); quy ước trạng thái hấp thụ (Nhận xét 03.10); cận $\lvert G_t\rvert\le M/(1-\gamma)$ (Mệnh đề 03.11); chọn $\gamma$ (Nhận xét 03.12).
- Mục 3: chính sách Markov dừng (Định nghĩa 03.13); xác suất của một đoạn quỹ đạo là tích $\pi\cdot p$ (Mệnh đề 03.14); giá trị trạng thái (Định nghĩa 03.15); giá trị hành động (Định nghĩa 03.16); ba cách hiểu sai về giá trị (Nhận xét 03.17).
- Mục 4: hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ (Bổ đề 03.18); hai tầng kỳ vọng (Bổ đề 03.19); tính Markov của phần tương lai (Bổ đề 03.20); phương trình Bellman kỳ vọng cho $v_\pi$ (Định lý 03.21); $q_\pi$ theo $v_\pi$ (Mệnh đề 03.22); $v_\pi$ theo $q_\pi$ (Mệnh đề 03.23); phương trình Bellman kỳ vọng cho $q_\pi$ (Hệ quả 03.24); chỗ dùng tính Markov (Nhận xét 03.25).
- Mục 5: chuỗi Markov và MRP cảm sinh (Định nghĩa 03.26); dạng ma trận (Mệnh đề 03.27); nghiệm duy nhất, công thức nghịch đảo và chuỗi Neumann (Định lý 03.28); đánh giá chính sách bằng giải hệ (Thuật toán 03.29); giới hạn của giải trực tiếp (Nhận xét 03.30); so sánh giá trị hành động chưa chứng minh tối ưu (Nhận xét 03.31).

**Công thức cần nhớ.** Hàm động lực xác định xác suất chuyển và thưởng kỳ vọng:

$$
p(s'\mid s,a)=\sum_rp(s',r\mid s,a),\qquad r(s,a)=\sum_{s',r}r\,p(s',r\mid s,a).
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
q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s'),\qquad v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a).
$$

Gộp chính sách vào mô hình cho dạng ma trận và nghiệm:

$$
v_\pi=(I-\gamma P^\pi)^{-1}r^\pi=\sum_{k\ge0}\gamma^k(P^\pi)^kr^\pi .
$$

**Giả thiết hay bị bỏ quên.**

- Tính Markov thuộc về cách chọn trạng thái; trạng thái thiếu thông tin (Ví dụ 03.4, Tình huống 03.2) làm Bổ đề 03.20 và mọi kết quả sau nó mất căn cứ.
- Tính dừng của hàm động lực và của chính sách là giả thiết riêng, đứng cạnh tính Markov.
- $\gamma<1$ là điều kiện của Mệnh đề 03.11 và Định lý 03.28 cho nhiệm vụ tiếp diễn; với $\gamma=1$, robot luôn Chờ có lợi tức vô hạn và hệ của robot vô nghiệm.
- Phần thưởng cố định trên mỗi nhánh là giả thiết thêm của ví dụ robot; $r(s,a)$ và $p(s'\mid s,a)$ không đủ để dựng lại $p$.
- Phương trình Bellman kỳ vọng là trung bình theo $\pi$; so sánh các $q_\pi(s,a)$ không chứng minh chính sách nào tối ưu.

## Bài tập củng cố

Các bài tập trong các mục (Bài tập 03.1–03.9) và năm bài dưới đây là bộ bài tập của chương; mỗi mục tiêu học tập có ít nhất một bài.

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
- **(b)** Tiếp diễn; cần $\gamma<1$ để lợi tức hữu hạn (Mệnh đề 03.11).
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
q_\pi(\mathrm H,\mathrm{tim})&=2+\tfrac12\bigl(\tfrac12\cdot\tfrac{13}4+\tfrac12\cdot\tfrac74\bigr)=2+\tfrac12\cdot\tfrac52=\tfrac{13}4,\\
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
G_2&=R_3+\gamma G_3=2+0{,}9\cdot0=2,\\
G_1&=R_2+\gamma G_2=-1+0{,}9\cdot2=0{,}8,\\
G_0&=R_1+\gamma G_1=1+0{,}9\cdot0{,}8=1{,}72 .
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
Thay đổi chỉ chạm vào cặp $(\mathrm L,\mathrm{tim})$. Xem cặp này có xuất hiện trong $P^\pi$, $r^\pi$ của chính sách chia đều không.
:::

::: solution
**(a)** Chính sách chia đều có $\pi(\mathrm{tim}\mid\mathrm L)=0$, nên theo (5.2) cặp $(\mathrm L,\mathrm{tim})$ không góp vào $P^\pi$ và $r^\pi$. Hai đối tượng này giữ nguyên, và theo Định lý 03.28, $v_\pi=(13/4,\,7/4)$ không đổi.

**(b)** Theo (1.6), $r(\mathrm L,\mathrm{tim})=\tfrac34\cdot2+\tfrac14\cdot(-3)=\tfrac34$. Theo (4.6),

$$
q_\pi(\mathrm L,\mathrm{tim})=\tfrac34+\tfrac12\bigl(\tfrac34\cdot\tfrac74+\tfrac14\cdot\tfrac{13}4\bigr)=\tfrac34+\tfrac12\cdot\tfrac{34}{16}=\tfrac{29}{16}.
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
\tfrac14\cdot0{,}9\cdot\bigl(2{,}250-0{,}355+0{,}738+0{,}358\bigr)=0{,}225\cdot2{,}991\approx0{,}673 .
$$

**(b)** Ở ô cạnh trái, hướng tây đi ra ngoài lưới: phần thưởng $-1$ và ở lại ô đó.

$$
\begin{aligned}
&\tfrac14\bigl[(-1+0{,}9\cdot0{,}051)+0{,}9\cdot1{,}522+0{,}9\cdot(-0{,}974)+0{,}9\cdot0{,}738\bigr]\\
&\qquad\approx\tfrac14\bigl[-0{,}954+1{,}370-0{,}877+0{,}664\bigr]\approx0{,}051 .
\end{aligned}
$$

**(c)** Phần thưởng $-1$ chỉ phát sinh khi đi ra ngoài lưới. Ô giữa không có hướng nào đi ra ngoài, nên $r^\pi=0$; ô cạnh trái có một hướng, nên $r^\pi=-\tfrac14$ và chính ô đó xuất hiện ở vế phải với trọng số $\tfrac14\cdot0{,}9$.

**Kiểm tra lại.** Với các giá trị làm tròn một chữ số của Sutton và Barto (2018, bài tập 3.14), câu (a) cho $0{,}225\cdot(2{,}3-0{,}4+0{,}7+0{,}4)=0{,}675\approx0{,}7$.
:::

<!-- note-topic-id: lec-03-part-10 -->
## Hướng dẫn đọc thêm và tài liệu tham khảo

- **Bài giảng gốc (2025–2026)**, *Markov Decision Processes with Key Concepts*, trang 28–58: phạm vi của chương. Bản gốc trình bày chuỗi Markov, quá trình phần thưởng Markov rồi MDP; ở ghi chú này, MDP được trình bày trước theo Sutton và Barto (2018, §3.1), và hai đối tượng kia được dựng lại ở Mục 5.
- **Bài tập tuần 2 (2025–2026)**, Tạ Việt Cường, ngày 12/3/2026, bài 3, 4, 7, 8, 10: bài 4 ứng với Định nghĩa 03.26; bài 7, 8 ứng với Mệnh đề 03.23 và Định lý 03.21; bài 3 là một hệ Bellman ba trạng thái có trạng thái hấp thụ; bài 10 mô hình hóa một bài toán thực tế thành MDP theo Định nghĩa 03.7.
- **R. S. Sutton và A. G. Barto (2018)**, *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Chương 3 (§3.1 cho Mục 1, §3.3–3.4 cho Mục 2, §3.5 cho Mục 3–4 và Tình huống 03.1) và §4.1 (Mục 5). Đọc tiếp §3.6 về giá trị tối ưu trước Bài 04, và chương 17 về dựng trạng thái Markov từ quan sát không Markov.
- **M. L. Puterman (1994)**, *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley, §6.1: đánh giá chính sách trong MDP chiết khấu, nghiệm dạng nghịch đảo và chuỗi Neumann, ở mức tổng quát hơn Định lý 03.28.
- **D. P. Bertsekas (2019)**, *Reinforcement Learning and Optimal Control*, Athena Scientific, chương về bài toán vô hạn chiết khấu: phương trình Bellman viết bằng toán tử, dẫn sang tính co dùng ở Bài 04.
- **Giáo trình *Học máy thống kê***, chương Học tăng cường, mục giới thiệu quá trình quyết định Markov và mục quy hoạch động: bộ $\langle S,A,T,R,\gamma\rangle$, giá trị của quỹ đạo $U(\tau)$ (ứng với $G_0$) và phương trình Bellman cho $V^\pi$ (ứng với Định lý 03.21).
- **Notebook thực hành Bài 04**, `thuc-hanh-cartpole-quy-hoach-dong.ipynb`, phần 5, mục 6.2 và 8.1: nguồn số liệu của Tình huống 03.2.
