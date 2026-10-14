# Bài 02 — Giao diện tác tử–môi trường

<!-- note-topic-id: lec-02-part-01 -->
## Mục tiêu học tập

Sau chương này, người học có thể:

1. Ghi một mẫu chuyển (transition) $(O_t,A_t,R_{t+1},O_{t+1})$ với chỉ số thời gian đúng và chỉ ra thành phần nào thuộc tác tử (agent), thành phần nào thuộc môi trường (environment) (Bài tập 02.1, 02.9).
2. Phân biệt trạng thái $S_t$, quan sát $O_t$ và biểu diễn (representation) $X_t$; kiểm tra một cách chọn trạng thái có tính Markov (Markov property) hay không và sửa bằng cách mở rộng trạng thái (Bài tập 02.2, 02.3, 02.11).
3. Viết chính sách xác định (deterministic policy) và chính sách ngẫu nhiên (stochastic policy) trên một biểu diễn, kiểm tra tính hợp lệ của một phân phối hành động, tính xác suất của một dãy hành động, và giải thích khi nào biểu diễn hiện tại không đủ cho một chính sách xác định tốt (Bài tập 02.4, 02.13).
4. Tính lợi tức (return) chiết khấu và giá trị $v_\pi(s)$ trên ví dụ nhỏ, đọc một hàm động lực (dynamics function) $p(s',r\mid s,a)$, và giải thích vì sao trọng số chiết khấu có dạng hình học (Bài tập 02.5, 02.6, 02.7, 02.10, 02.12).
5. Tìm ngưỡng chi phí mỗi bước làm tác tử tối ưu đổi hành vi trong một bài toán thiết kế phần thưởng (reward), và chỉ ra giả thiết của kết quả khi phần thưởng mỗi bước đổi dấu (Bài tập 02.8, 02.10).

Bộ bài tập chính thức của Bài 02 nằm trong [tệp bài tập](material-viewer.html?doc=materials/lec-02/exercises.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html), đánh số chung với ghi chú; chín bài 02.14–02.22 chỉ có ở đó và phân theo mục tiêu như sau: mục tiêu 1 có Bài tập 02.14, 02.22; mục tiêu 2 có 02.15, 02.19, 02.22; mục tiêu 3 có 02.16, 02.19; mục tiêu 4 có 02.16–02.18, 02.20–02.22; mục tiêu 5 có 02.18, 02.20, 02.21.

## Kiến thức tiên quyết

Số hiệu `01.k` chỉ ghi chú Bài 01, `02.k` chỉ ghi chú này.

- **Xác suất có điều kiện và kỳ vọng.** Với $\Pr(F)>0$, $\Pr(E\mid F)=\Pr(E\cap F)/\Pr(F)$. Biến ngẫu nhiên rời rạc $Y$ có kỳ vọng hữu hạn khi $\sum_y\lvert y\rvert\Pr(Y=y)<\infty$, và khi đó $\mathbb E[Y]=\sum_y y\Pr(Y=y)$.
- **Tổng hình học.** Với $\gamma\ne1$, $\sum_{k=0}^{n-1}\gamma^k=(1-\gamma^n)/(1-\gamma)$; với $0\le\gamma<1$, $\sum_{k=0}^{\infty}\gamma^k=1/(1-\gamma)$.
- **Tác tử, môi trường, vòng tương tác** (Định nghĩa 01.1). Tác tử (agent) nhận quan sát $O_t$ và chọn hành động $A_t$; môi trường (environment) gồm mọi thứ ngoài tác tử, trả phần thưởng (reward) $R_{t+1}$ và quan sát $O_{t+1}$. Ranh giới đặt ở giới hạn điều khiển của tác tử, không ở vỏ máy.
- **Trạng thái, quan sát, lịch sử** (Định nghĩa 01.2, Nhận xét 01.3). Trạng thái (state) $S_t$ là cấu hình mà luật của môi trường dùng tới; quan sát (observation) $O_t$ là phần thông tin tác tử nhận; lịch sử $H_t=(O_0,A_0,R_1,\dots,O_t)$; tập hành động hợp lệ tại $s$ là $\mathcal A(s)$; khi $O_t=S_t$ ở mọi bước, tác tử quan sát đầy đủ. Hai trạng thái có thể cho cùng quan sát. Từ Bài 02, trạng thái được hiểu là biến do người mô hình chọn để mô tả môi trường; biến đó có thể nhỏ hơn cấu hình mà luật chuyển dùng tới (Mục 2.1, 2.5).
- **Tín hiệu học** (Định nghĩa 01.5, Nhận xét 01.6). Phần thưởng là một số đánh giá chuyển vừa xảy ra, không cho biết hành động đúng; phản hồi có thể trễ nhiều bước; dữ liệu tương tác không độc lập cùng phân phối, và hành động thay đổi dữ liệu về sau.
- **Lượt, lợi tức không chiết khấu, giả thuyết phần thưởng** (Định nghĩa 01.7, 01.8, Mệnh đề 01.9, Nhận xét 01.10). Một lượt (episode) kết thúc tại $T$; $G_t=R_{t+1}+\cdots+R_T$ thỏa $G_t=R_{t+1}+G_{t+1}$, $G_T=0$. Giả thuyết phần thưởng (reward hypothesis) phát biểu rằng mọi mục tiêu mô tả được bằng việc làm lớn nhất kỳ vọng của tổng phần thưởng; đây là giả thuyết mô hình hóa, không phải định lý.
- **Chính sách và hàm giá trị trên lịch sử** (Định nghĩa 01.11, 01.12). Chính sách (policy) gán cho mỗi lịch sử $h$ một phân phối $\pi(\cdot\mid h)$ trên các hành động hợp lệ; giá trị của $h$ dưới $\pi$ là $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$.
- **Mô hình** (Định nghĩa 01.14, Nhận xét 01.15). Mô hình (model) là một mô tả do người thiết kế cung cấp hoặc tác tử học được, cho dự báo $(\widehat S_{t+1},\widehat R_{t+1})$ của phản hồi; dự báo có thể sai. Phương pháp có mô hình dùng nó để lập kế hoạch; phương pháp phi mô hình thì không.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một ví dụ hay một chứng minh được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương, trừ ngoại lệ của chữ $r$ ghi sau bảng.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$, $T$ | chỉ số bước; thời điểm kết thúc lượt | $t\in\{0,1,2,\dots\}$; $T$ nguyên dương ngẫu nhiên, hoặc $T=\infty$ |
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái chưa kết thúc; thêm các trạng thái kết thúc | tập đếm được; hữu hạn trong ví dụ |
| $S_t$, $s$, $s'$ | trạng thái tại $t$; một giá trị; trạng thái kế tiếp | phần tử của $\mathcal S^+$ |
| $\mathcal O$, $O_t$ | tập quan sát; quan sát tại $t$ | tập tùy ý |
| $\mathcal X$, $X_t$, $x$ | tập biểu diễn; biểu diễn tại $t$; một giá trị | tập tùy ý |
| $f_t$ | hàm biểu diễn | $\mathcal O^{t+1}\times\mathcal A^{t}\times\mathbb R^{t}\to\mathcal X$ |
| $\mathcal A$, $\mathcal A(s)$, $A_t$, $a$ | tập hành động; hành động hợp lệ tại $s$; hành động tại $t$; một giá trị | tập hữu hạn |
| $\mathcal R$, $R_{t+1}$ | tập giá trị phần thưởng; phần thưởng của chuyển từ $t$ sang $t+1$ | $\mathcal R\subset\mathbb R$ đếm được |
| $H_t$, $\tau$ | lịch sử (history) trạng thái tới $t$; quỹ đạo (trajectory), $\tau=H_T$ | dãy hữu hạn |
| $\pi(a\mid x)$, $\pi(x)$ | chính sách ngẫu nhiên; chính sách xác định | phân phối trên $\mathcal A$; phần tử của $\mathcal A$ |
| $\sigma$, $[r,\sigma]$ | chuỗi phần thưởng hữu hạn; chuỗi nhận $r$ rồi tiếp tục bằng $\sigma$ | $\mathbb R^n$, $n\ge1$ |
| $U$, $w_i$, $\succ$ | lợi ích (utility) của chuỗi; trọng số vị trí $i$; quan hệ ưu tiên | $\mathbb R$; $w_i>0$ |
| $\gamma$ | hệ số chiết khấu (discount factor) | $[0,1]$; $\gamma<1$ khi $T=\infty$ |
| $G_t$, $R_{\max}$ | lợi tức từ $t$; chặn của $\lvert R_{t+1}\rvert$ | biến ngẫu nhiên; $R_{\max}\ge0$ |
| $v_\pi(s)$, $\mathbb E_\pi$ | giá trị trạng thái dưới $\pi$; kỳ vọng theo $\pi$ và động lực môi trường | $\mathbb R$ |
| $p(s',r\mid s,a)$ | hàm động lực của môi trường | $[0,1]$ |
| $p(s'\mid s,a)$, $r(s,a)$ | xác suất chuyển; thưởng kỳ vọng một bước | $[0,1]$; $\mathbb R$ |
| $c$, $c_{\mathrm H}$ | chi phí mỗi bước; phạt bổ sung khi vào hố | $c\ge0$, $c_{\mathrm H}\ge0$ |
| $\mathrm S$, $\mathrm H$, $\mathrm G$ | nút xuất phát, hố, đích ($\mathrm G$ cũng là đích của mê cung $8\times8$) | nhãn, không phải biến |

Hành động trong mê cung là Bắc, Đông, Nam, Tây. $R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$, nhận sau $A_t$ (Sutton và Barto, 2018, §3.1); bài giảng gốc (2025–2026, trang 15) viết lịch sử với $R_0$, lệch một chỉ số so với quy ước này.

Kỳ vọng $\mathbb E_\pi$ lấy theo cả chính sách và động lực của môi trường. Lợi tức tại thời điểm kết thúc bằng $0$, nên giá trị của trạng thái kết thúc bằng $0$.

Chữ "dừng" có ba nghĩa phân biệt bằng danh từ đi kèm: chính sách dừng không đổi theo $t$; môi trường dừng có xác suất chuyển không đổi theo $t$; ưu tiên dừng là tính chất của cách so sánh chuỗi phần thưởng (Định nghĩa 02.10). Lượt thì "kết thúc", không "dừng".

Đứng riêng, $r$ là một giá trị phần thưởng; với hai đối số, $r(s,a)$ là thưởng kỳ vọng một bước, theo cách viết của Sutton và Barto. Tọa độ ô ghi theo thứ tự (cột, hàng) và luôn nằm trong ký hiệu toán, chẳng hạn $(4,2)$ là cột $4$, hàng $2$; chữ $x$ chỉ dùng cho giá trị của biểu diễn. Trong mê cung có chìa khóa, trạng thái là cặp (ô, $k$), chẳng hạn $((7,6),1)$. Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}5$. Mê cung $8\times8$ lấy từ bài giảng gốc (trang 25–26); các bộ số khác là số liệu sư phạm tự xây dựng.

Giáo trình *Học máy thống kê* mô tả quá trình quyết định Markov (Markov decision process, MDP) bằng bộ $\langle S,A,T,R,\gamma\rangle$: $T(s,a,s')$ ứng với $p(s'\mid s,a)$, $R(s,a,s')$ là thưởng kỳ vọng khi biết cả $s'$, giá trị quỹ đạo $U(\tau)$ là $G_0$, và $V^\pi$ là $v_\pi$. Theo Sutton và Barto, $\gamma$ đặt ngoài $p$, vì nó thuộc cách đánh giá chuỗi phần thưởng (Mục 4.1).

## Bản đồ chủ đề

### Mẫu chuyển và chỉ số thời gian

- Nhóm: `cốt lõi`. Mục: `## 1.` (mạch 2).
- Vai trò trong mạch: cố định thứ tự quan sát, hành động, phần thưởng của một bước.
- Kết nối vào: vòng tương tác (Định nghĩa 01.1). Kết nối ra: lịch sử ở Mục 2, lợi tức ở Mục 4.
- Nguồn: bài giảng gốc, trang 4, 7–11, 14–15; Sutton và Barto (2018), §3.1.

### Trạng thái, quan sát và biểu diễn

- Nhóm: `cốt lõi`. Mục: `## 2.` (mạch 3).
- Vai trò trong mạch: tách điều môi trường ở, điều tác tử nhận và điều tác tử dùng để quyết định.
- Kết nối vào: Định nghĩa 01.2. Kết nối ra: đầu vào của chính sách ở Mục 3.
- Nguồn: bài giảng gốc, trang 16, 18–19, 25–27; Bài tập tuần 2 (2025–2026), bài 2.

### Tính Markov, lịch sử trạng thái và mở rộng trạng thái

- Nhóm: `cốt lõi`. Mục: `## 2.` (mạch 3).
- Vai trò trong mạch: điều kiện để trạng thái hiện tại đủ cho dự báo một bước, và cách khôi phục điều kiện đó.
- Kết nối vào: lịch sử của Bài 01; hai ô cùng quan sát. Kết nối ra: giả thiết của hàm giá trị, hàm động lực và MDP ở Bài 03.
- Nguồn: bài giảng gốc, trang 15, 17; Sutton và Barto (2018), §3.1 (trang 49), §17.3.

### Chính sách trên biểu diễn

- Nhóm: `cốt lõi`. Mục: `## 3.` (mạch 4).
- Vai trò trong mạch: viết cách chọn hướng thành đối tượng toán học trên dữ liệu tác tử thật sự có.
- Kết nối vào: Định nghĩa 01.11; biểu diễn $X_t$. Kết nối ra: kỳ vọng $\mathbb E_\pi$ ở Mục 4.
- Nguồn: bài giảng gốc, trang 20–21, 26; Sutton và Barto (2018), §3.5; Bài tập tuần 2, bài 6.

### Ưu tiên dừng và trọng số hình học

- Nhóm: `bổ sung`. Mục: `## 4.` (mạch 5).
- Vai trò trong mạch: chứng minh dạng $\gamma^k$ của trọng số chiết khấu từ ưu tiên dừng, khi lợi ích có dạng cộng.
- Kết nối vào: lợi tức của Bài 01. Kết nối ra: Định nghĩa 02.12.
- Nguồn: Russell và Norvig (2020), §17.1.1, trang 565–566 (phát biểu không kèm chứng minh).

### Lợi tức chiết khấu

- Nhóm: `cốt lõi`. Mục: `## 4.` (mạch 5).
- Vai trò trong mạch: đo cả chuỗi phần thưởng sau một hành động bằng một số, kể cả khi tương tác không kết thúc.
- Kết nối vào: Định nghĩa 01.8, Định lý 02.11. Kết nối ra: hàm giá trị; phương trình Bellman ở Bài 03.
- Nguồn: bài giảng gốc, trang 7–9, 22; Sutton và Barto (2018), §3.3–3.4; Bài tập tuần 2, bài 5.

### Từ lợi tức của một lượt đến kỳ vọng

- Nhóm: `cầu nối`. Mục: `## 4.` (mạch 5).
- Vai trò trong mạch: khoảng trống giữa lợi tức của một lượt và một con số đại diện cho trạng thái khi có yếu tố ngẫu nhiên.
- Kết nối vào: Định nghĩa 02.12. Kết nối ra: Định nghĩa 02.14.
- Nguồn: bài giảng gốc, trang 22 (câu hỏi vì sao cần kỳ vọng).

### Hàm giá trị trạng thái

- Nhóm: `cốt lõi`. Mục: `## 4.` (mạch 5).
- Vai trò trong mạch: đánh giá mỗi trạng thái dưới một chính sách cố định.
- Kết nối vào: Định nghĩa 01.12, tính Markov. Kết nối ra: dự đoán, điều khiển; Bài 03.
- Nguồn: bài giảng gốc, trang 22, 24, 26; Sutton và Barto (2018), §3.5.

### Hàm động lực

- Nhóm: `cốt lõi`. Mục: `## 4.` (mạch 5).
- Vai trò trong mạch: dự báo một bước của môi trường, tách khỏi đánh giá dài hạn.
- Kết nối vào: Định nghĩa 01.14, tính Markov. Kết nối ra: MDP (Bài 03), quy hoạch động (dynamic programming) ở Bài 04.
- Nguồn: bài giảng gốc, trang 10, 13, 23; Sutton và Barto (2018), §3.1.

### Thiết kế phần thưởng và ngưỡng đổi hành vi

- Nhóm: `cốt lõi`. Mục: `## 5.` (mạch 6).
- Vai trò trong mạch: dự báo hành vi của tác tử tối ưu khi người thiết kế đổi phần thưởng; liên hệ với khuyến khích và chế tài.
- Kết nối vào: lợi tức với $\gamma=1$. Kết nối ra: phần thưởng của các bài thực hành Bài 04–07.
- Nguồn: ví dụ mê cung đích–hố do người dùng duyệt; Sutton và Barto (2018), §3.2, §17.4.

### Quan sát một phần và chính sách ngẫu nhiên

- Nhóm: `bổ sung`. Mục: `## Tình huống áp dụng và ứng dụng`.
- Vai trò trong mạch: hậu quả khi biểu diễn gộp hai trạng thái cần hai hành động khác nhau.
- Kết nối vào: Nhận xét 02.4, Định nghĩa 02.8. Kết nối ra: chính sách ngẫu nhiên và biểu diễn có bộ nhớ ở các bài sau.
- Nguồn: Sutton và Barto (2018), §13.1, Ví dụ 13.1; Bài tập tuần 2, bài 6.

### Trạng thái Markov từ lịch sử quan sát; thiết kế tín hiệu thưởng

- Nhóm: `đọc thêm`. Mục: `## Hướng dẫn đọc thêm và tài liệu tham khảo`.
- Vai trò trong mạch: mở rộng Mệnh đề 02.6 sang lịch sử của tác tử và Mục 5 sang thiết kế phần thưởng thực tế.
- Kết nối vào: Mệnh đề 02.6, Mệnh đề 02.18. Kết nối ra: quan sát một phần trong Học tăng cường sâu.
- Nguồn: Sutton và Barto (2018), §17.3 (trang 464–468), §17.4 (trang 469–470).

<!-- note-topic-id: lec-02-part-02 -->
## 1. Vòng tương tác và tín hiệu thưởng

Ở Bài 01, chính sách được định nghĩa trên lịch sử quan sát (Định nghĩa 01.11) và giá trị là kỳ vọng của lợi tức không chiết khấu khi biết lịch sử, $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$ (Định nghĩa 01.12). Hai định nghĩa đó đúng cho mọi môi trường, nhưng đối số của chúng dài thêm sau mỗi bước, và tổng không chiết khấu chỉ dùng được khi lượt chắc chắn kết thúc. Trong chương này, chúng ta tìm điều kiện để thay lịch sử bằng một trạng thái gọn, xác định cách cộng phần thưởng có trọng số theo thời gian, và tách dự báo một bước khỏi đánh giá dài hạn.

Bài toán xuyên suốt là một mê cung lấy từ bài giảng gốc (trang 25–26).

::: example Ví dụ 02.1 (Mê cung $8\times8$)
**Dữ kiện.** Lưới $8\times8$ có 27 ô đi được và 37 ô tường. Ô ghi bằng tọa độ (cột, hàng), cả hai đánh số từ $0$, hàng tăng xuống dưới. Tác tử xuất phát tại $(0,2)$. Đích $\mathrm G$ nằm ngoài lưới, bên phải ô $(7,6)$, ghi là $(8,6)$.

**Luật chuyển.** Mỗi bước, tác tử chọn Bắc, Đông, Nam hoặc Tây. Nếu ô theo hướng đó là tường hoặc ngoài lưới, tác tử đứng yên; ngoại lệ duy nhất là bước Đông từ $(7,6)$, đưa tác tử vào $\mathrm G$ và kết thúc lượt.

**Phần thưởng.** Mỗi bước nhận $-1$, kể cả bước vào $\mathrm G$.

**Một đường đi.** Đường do bài giảng gốc vẽ đi qua $(0,2)$, $(1,2)$, $(1,1)$, $(2,1)$, $(3,1)$, $(4,1)$, $(5,1)$, $(6,1)$, $(6,2)$, $(6,3)$, $(5,3)$, $(5,4)$, $(5,5)$, $(6,5)$, $(6,6)$, $(7,6)$ rồi vào $\mathrm G$. Danh sách có 16 ô và từ mỗi ô có đúng một bước, nên đường dài 16 bước, tổng phần thưởng $16\cdot(-1)=-16$.

**Kiểm tra lại.** Hai ô liên tiếp chỉ khác nhau ở một tọa độ, chênh một đơn vị, và không ô nào là tường theo hình dưới.
:::

![Mê cung tám hàng tám cột của bài giảng gốc. Ô tường tô đậm, ô đi được để trắng. Tọa độ ghi theo thứ tự cột, hàng, cả hai đánh số từ 0 đến 7, hàng tăng xuống dưới. Tác tử bắt đầu tại ô (0,2) ở mép trái. Đích G nằm ngoài lưới bên phải ô (7,6), ghi tọa độ (8,6).](img/lec-02/source-maze.svg)

Điểm bắt đầu ở mép trái, hàng 2, và lối ra duy nhất là cạnh phải của ô $(7,6)$. Nhiều ô trắng là ngõ cụt, chẳng hạn $(4,2)$ chỉ nối với $(4,1)$; vì vậy một bước hợp lệ có thể làm đường còn lại dài thêm, và giá trị của một bước phụ thuộc những bước sau nó.

Từ ví dụ nảy ra bốn câu hỏi. Nếu cảm biến chỉ báo bốn ô kề là tường hay trống, ô $(2,1)$ và $(3,1)$ cho cùng dữ liệu; dữ liệu đó có đủ để chọn hướng không. Hai tác tử ở cùng ô $(1,2)$ có thể chọn hai hướng khác nhau; ta cần một đối tượng ghi được cách chọn trên dữ liệu mà tác tử có. Khi có yếu tố ngẫu nhiên, lợi tức của một lượt là biến ngẫu nhiên; ta cần một con số đại diện cho từng ô. Khi người thiết kế đổi phần thưởng, chẳng hạn thêm một hố kết thúc lượt, hành vi tối ưu có thể đổi theo.

![Sơ đồ cấu trúc của chương. Khối Tác tử chứa biểu diễn X t tính từ dữ liệu đến thời điểm t (Mục 2) và chính sách pi của a cho x (Mục 3). Khối Môi trường chứa trạng thái S t và tính Markov (Mục 2), hàm động lực p của s phẩy, r cho s, a (Mục 4). Mũi tên trên từ tác tử sang môi trường ghi hành động A t (Mục 1); mũi tên dưới từ môi trường về tác tử ghi R t+1 và O t+1 (Mục 1). Một mũi tên đứt đưa chuỗi phần thưởng xuống khối dưới: lợi tức G t bằng tổng gamma mũ k nhân R t+k+1 và hàm giá trị v pi của s (Mục 4); thiết kế phần thưởng (c, c H) quyết định hành vi tối ưu (Mục 5).](img/lec-02/chapter-structure.svg)

Sơ đồ đặt mỗi mục của chương lên vòng tương tác. Hai mũi tên giữa hai khối là nội dung của Mục 1. Biểu diễn và chính sách bên trong khối tác tử, trạng thái và hàm động lực bên trong khối môi trường là nội dung của Mục 2–4. Khối dưới cùng chỉ nhận chuỗi phần thưởng: lợi tức và hàm giá trị đo chuỗi đó, còn thiết kế phần thưởng ở Mục 5 thay đổi chính các con số trong chuỗi.

### 1.1 Ranh giới tác tử–môi trường trên mê cung

Nhắc lại: theo Định nghĩa 01.1, tác tử chỉ quyết định $A_t$, còn môi trường quyết định $R_{t+1}$ và $O_{t+1}$; mọi thứ tác tử không thay đổi được tùy ý thuộc môi trường, kể cả cơ chế tính phần thưởng. Sutton và Barto (2018, §3.1, trang 50) mô tả ranh giới này là giới hạn của quyền điều khiển tuyệt đối của tác tử. Trên mê cung, tác tử là phần chọn hướng; bản đồ, luật đứng yên khi gặp tường và quy tắc trừ $1$ mỗi bước thuộc môi trường, dù tác tử có thể biết rõ các luật đó. Với một robot thật, động cơ và cảm biến cũng thuộc môi trường, vì bộ điều khiển chỉ chọn được tín hiệu điều khiển.

<!-- note-topic-id: lec-02-topic-01 -->
### 1.2 Mẫu chuyển

Mọi đại lượng về sau, từ lịch sử tới lợi tức và giá trị, được ghi bằng chỉ số thời gian của các tín hiệu đi qua ranh giới. Một cách trực quan, một bước gồm thông tin tác tử có trước khi chọn, lựa chọn của nó và hai phản hồi của môi trường; ví dụ sau cụ thể hóa mô tả này trước khi có định nghĩa.

::: example Ví dụ 02.2 (Một bước Đông từ ô $(0,2)$)
**Dữ kiện.** Mê cung $8\times8$ của Ví dụ 02.1, đứng yên khi gặp tường hoặc biên, phần thưởng $-1$ mỗi bước. Tác tử nhận tọa độ ô hiện tại. Tại $t=0$, tác tử ở $(0,2)$.

**Bước.** Tác tử nhận $(0,2)$ và chọn Đông. Ô $(1,2)$ trống, nên môi trường chuyển tác tử sang $(1,2)$, trả phần thưởng $-1$ và tọa độ mới $(1,2)$. Phản hồi thuộc về chuyển từ thời điểm $0$ sang thời điểm $1$.

**Kiểm tra lại.** Nếu chọn Tây tại $(0,2)$, ô phía tây ngoài lưới, tác tử đứng yên và vẫn nhận $-1$: phản hồi vẫn đủ hai thành phần.
:::

::: definition Định nghĩa 02.1 (Mẫu chuyển)
Cho tập quan sát $\mathcal O$ và tập hành động $\mathcal A$. Tại thời điểm $t$ trước khi lượt kết thúc, tác tử có quan sát $O_t\in\mathcal O$ và chọn hành động (action) $A_t\in\mathcal A$; môi trường trả phần thưởng $R_{t+1}\in\mathbb R$ và quan sát mới $O_{t+1}\in\mathcal O$. Bộ bốn $(O_t,A_t,R_{t+1},O_{t+1})$ là một **mẫu chuyển** (transition). Nếu sau bước này môi trường ở trạng thái kết thúc thì lượt kết thúc tại $T=t+1$ và không còn hành động nào sau $T$.
:::

Định nghĩa mở rộng vòng tương tác của Định nghĩa 01.1 bằng cách cắt dãy $O_0,A_0,R_1,O_1,\dots$ thành các bộ bốn chồng nhau, mỗi bộ là đơn vị dữ liệu mà các thuật toán của Bài 05–06 dùng. Chỉ số $t+1$ của phần thưởng nói rằng $R_{t+1}$ được sinh cùng lúc với $O_{t+1}$, sau khi $A_t$ đã được chọn, nên tác tử chưa biết $R_{t+1}$ khi chọn $A_t$. Viết $R_t$ cho phần thưởng của $A_t$ là lỗi thường gặp; nó làm lệch mọi tổng về sau một bước.

Mẫu chuyển của Ví dụ 02.2 là $(O_0,A_0,R_1,O_1)=((0,2),\text{Đông},-1,(1,2))$. Định nghĩa không đòi quan sát là tọa độ: ở Mục 2, cùng bước này được ghi với quan sát là mã bốn ô kề.

![Vòng tương tác: khối Tác tử gửi hành động A t sang khối Môi trường; khối Môi trường trả về phần thưởng R t+1 và quan sát O t+1 cho khối Tác tử.](img/lec-02/agent-environment-loop.svg)

Mũi tên trên của hình mang $A_t$ từ tác tử sang môi trường; mũi tên dưới mang $R_{t+1}$ và $O_{t+1}$ theo chiều ngược lại. Vòng khép lại khi $O_{t+1}$ trở thành thông tin của bước $t+1$.

**Trong thực hành.** Thư viện Gymnasium, dùng trong các bài thực hành từ Bài 04, cài đặt Định nghĩa 02.1 bằng `env.step(a)`: hàm nhận $A_t$, trả $O_{t+1}$, $R_{t+1}$ và hai cờ. Cờ `terminated` báo môi trường vào trạng thái kết thúc; cờ `truncated` báo lượt bị cắt vì giới hạn của chương trình, như ở bước $1\,000$ của Lunar Lander (Bài 05–06) hay khi chim qua $50$ ống trong Flappy Bird (Bài 07). Lượt bị cắt chưa tới trạng thái kết thúc, nên lợi tức của nó chưa được quan sát trọn.

### 1.3 Phần thưởng trên mê cung

Nhắc lại (Định nghĩa 01.5, Nhận xét 01.6, 01.10): phần thưởng chỉ chấm kết quả chuyển vừa xảy ra, không cho biết hành động đúng, có thể đến trễ nhiều bước, và theo giả thuyết phần thưởng, tiêu chí của tác tử là kỳ vọng của tổng phần thưởng. Trên mê cung, phần thưởng $-1$ sau bước Đông không cho biết Bắc, Nam hay Tây có tốt hơn, vì mọi bước đều nhận $-1$. Ví dụ sau cho thấy tổng của cả đường mới phân biệt được hai lựa chọn.

::: example Ví dụ 02.3 (Hai đường 16 bước và 18 bước)
**Dữ kiện.** Mê cung $8\times8$, phần thưởng $-1$ mỗi bước, kể cả bước vào $\mathrm G$. Đường thứ nhất là đường 16 bước của Ví dụ 02.1. Đường thứ hai giống đường thứ nhất, trừ một chỗ: tại $(4,1)$ tác tử đi Nam vào ngõ cụt $(4,2)$, rồi đi Bắc về $(4,1)$ trước khi tiếp tục.

**Tính.** Đường thứ hai dài $16+2=18$ bước. Tổng phần thưởng của hai đường là $-16$ và $-18$.

**Đọc kết quả.** Với $-1$ mỗi bước, tổng phần thưởng của một đường hữu hạn bằng âm số bước, nên cực đại tổng phần thưởng tương đương với tới đích bằng ít bước nhất.

**Kiểm tra lại.** Tại $(4,1)$, bước Nam và bước Đông đều nhận $-1$; chỉ tổng của cả đường phân biệt được hai lựa chọn.
:::

![Một quỹ đạo ba bước của trò chơi: các quan sát O0, O1, O2, O3 nối bằng ba mũi tên. Mũi tên thứ nhất ghi A0 và R1 bằng 0, mũi tên thứ hai ghi A1 và R2 bằng 0, mũi tên thứ ba ghi A2 và R3 bằng +1 và dẫn tới quan sát kết thúc O3. Chú thích: kết quả cuối liên quan tới cả chuỗi hành động.](img/lec-02/delayed-feedback.svg)

Hình vẽ phản hồi trễ (delayed reward) trên một ván cờ ba nước, với phần thưởng $0$ ở nước chưa kết thúc và $+1$ khi thắng, cách gán của Nhận xét 01.10. Phần thưởng khác $0$ gắn với mũi tên cuối, trong khi cả $A_0,A_1,A_2$ đều có thể góp phần vào kết quả. Trên mê cung, phần thưởng đến ngay sau mỗi bước, nhưng giá trị của bước Nam tại $(4,1)$ chỉ hiện ra khi tính hết hai bước thừa về sau.

::: exercise Bài tập 02.1 (Ghi một mẫu chuyển)
Mê cung $8\times8$ của Ví dụ 02.1 (đứng yên khi gặp tường, phần thưởng $-1$ mỗi bước); quan sát là tọa độ. Tác tử đi theo đường 16 bước, nên tại $t=7$ nó ở $(6,1)$. Ô $(6,2)$ trống, ô $(7,1)$ là tường.

- (a) Tại $t=7$ tác tử chọn Nam. Ghi mẫu chuyển $(O_7,A_7,R_8,O_8)$.
- (b) Nếu tại $t=7$ tác tử chọn Đông, ghi lại mẫu chuyển.
- (c) Phần thưởng của bước ở câu (a) mang chỉ số nào, và vì sao không phải $R_7$.
:::

::: hint
Phần thưởng của chuyển từ $t$ sang $t+1$ mang chỉ số $t+1$. Đi vào tường thì đứng yên nhưng vẫn nhận phần thưởng.
:::

::: solution
**Câu (a).** $O_7=(6,1)$, $A_7=\text{Nam}$; tác tử tới $(6,2)$, nên mẫu chuyển là $((6,1),\text{Nam},-1,(6,2))$.

**Câu (b).** Ô $(7,1)$ là tường, tác tử đứng yên: $((6,1),\text{Đông},-1,(6,1))$.

**Câu (c).** Chỉ số $8$, vì đây là chuyển từ $t=7$ sang $t=8$ (Định nghĩa 02.1); $R_7$ là phần thưởng của bước Đông từ $(5,1)$ ở $t=6$.

**Kiểm tra lại.** Hai mẫu chuyển ở (a) và (b) chỉ khác nhau ở hành động và quan sát sau; phần thưởng giống nhau.
:::

Như vậy, chúng ta đã áp ranh giới của Định nghĩa 01.1 vào mê cung và cố định thứ tự tín hiệu trong một bước bằng mẫu chuyển (Định nghĩa 02.1). Phần thưởng $-1$ mỗi bước làm tổng phần thưởng bằng âm số bước (Ví dụ 02.3). Tuy nhiên, trong mọi ví dụ của mục, quan sát là tọa độ, tức toàn bộ thông tin về vị trí; Định nghĩa 02.1 chưa nói quan sát chứa gì khi cảm biến yếu hơn. Trong Mục 2, chúng ta tách trạng thái, quan sát và biểu diễn, rồi nêu điều kiện để thông tin hiện tại đủ cho dự báo.

<!-- note-topic-id: lec-02-part-03 -->
## 2. Thông tin khả dụng và tính Markov

Giả sử tác tử của mê cung $8\times8$ chỉ có một cảm biến báo bốn ô kề là tường hay trống. Tại $(2,1)$, cảm biến báo Bắc và Nam là tường, Đông và Tây trống; tại $(3,1)$, cảm biến báo đúng như vậy. Chúng ta cần trả lời hai câu hỏi: tác tử dùng thông tin gì để quyết định, và khi nào thông tin hiện tại đủ để dự báo bước kế tiếp.

<!-- note-topic-id: lec-02-topic-03 -->
### 2.1 Trạng thái, quan sát và biểu diễn

Nhắc lại (Định nghĩa 01.2): trạng thái $S_t$ là cấu hình của môi trường mà luật chuyển dùng tới, còn quan sát $O_t$ là phần thông tin tác tử nhận. Từ chương này, trạng thái là biến do người mô hình chọn để mô tả môi trường: có thể lấy toàn bộ cấu hình, hoặc một biến nhỏ hơn như tọa độ ô, và lựa chọn đó quyết định trạng thái có tính Markov hay không (Mục 2.5). Một cách trực quan, còn một đối tượng thứ ba: dữ liệu tác tử tự tính ra từ những gì đã nhận để đưa vào quy tắc chọn hành động. Ba đối tượng trùng nhau khi quan sát là tọa độ, nhưng nói chung khác nhau; đây chưa phải định nghĩa.

::: example Ví dụ 02.4 (Ô $(2,1)$ và cảm biến bốn ô kề)
**Dữ kiện.** Mê cung $8\times8$ của Ví dụ 02.1; tác tử ở $(2,1)$. Cảm biến xét bốn hướng theo thứ tự Bắc, Đông, Nam, Tây và trả một bộ mã $O_t\in\{0,1\}^4$: chữ số của một hướng là $1$ nếu bước theo hướng đó giữ tác tử đứng yên (tường hoặc ngoài lưới), là $0$ nếu bước đó đưa tác tử sang ô khác, kể cả bước Đông từ $(7,6)$ vào $\mathrm G$.

**Từ vị trí đến quan sát.** Vị trí thật là $(2,1)$. Bốn ô kề gồm Bắc $(2,0)$ tường, Đông $(3,1)$ trống, Nam $(2,2)$ tường, Tây $(1,1)$ trống. Cảm biến trả quan sát $O_t=(1,0,1,0)$. Nếu tác tử dùng luôn mã này để chọn hướng, biểu diễn là $X_t=O_t$; một biểu diễn khác quan sát xuất hiện ở Ví dụ 02.5.

**So sánh với $(3,1)$.** Bắc $(3,0)$ tường, Đông $(4,1)$ trống, Nam $(3,2)$ tường, Tây $(2,1)$ trống: quan sát cũng là $(1,0,1,0)$. Quan sát không xác định được vị trí.

**Kiểm tra lại.** Hàng $0$ toàn tường; hàng $2$ có tường tại các cột $2$, $3$, $5$, $7$, nên ô Nam của cả hai ô là tường.
:::

![Sơ đồ ba khối. Trạng thái: mê cung cố định với vị trí tác tử (2,1). Bốn ô kề: vùng cảm biến thấy, Bắc và Nam là tường, Đông và Tây trống. Quan sát O t: bộ mã (1,0,1,0) theo thứ tự Bắc, Đông, Nam, Tây, với 1 là bước giữ tác tử đứng yên và 0 là bước sang ô khác. Mũi tên từ quan sát xuống biểu diễn X t do tác tử tính. Mã này không xác định được tọa độ thật của tác tử.](img/lec-02/state-observation-representation.svg)

Hình đọc từ trái sang phải theo dòng thông tin của Ví dụ 02.4: toàn bộ bản đồ với vị trí $(2,1)$, bốn ô kề mà cảm biến thấy, rồi quan sát $O_t=(1,0,1,0)$ mà cảm biến trả về. Thông tin mất ở mũi tên đầu: từ bốn ô kề không dựng lại được bản đồ, nên từ mã $(1,0,1,0)$ không biết tác tử ở cột $2$ hay cột $3$. Mũi tên thứ hai chỉ ghi bốn ô kề thành chữ số. Mũi tên xuống là việc của tác tử: tính biểu diễn $X_t$ từ các mã đã nhận.

### 2.2 Biểu diễn từ thông tin khả dụng

Biểu diễn chỉ được dùng những gì tác tử có trước khi chọn hành động. Định nghĩa sau viết điều đó thành một hàm.

::: definition Định nghĩa 02.2 (Biểu diễn và hàm biểu diễn)
Tại thời điểm $t$, dữ liệu khả dụng của tác tử là ba dãy $O_{0:t}=(O_0,\dots,O_t)$, $A_{0:t-1}=(A_0,\dots,A_{t-1})$ và $R_{1:t}=(R_1,\dots,R_t)$, với hai dãy sau rỗng khi $t=0$. Một **hàm biểu diễn** là ánh xạ tất định $f_t:\mathcal O^{t+1}\times\mathcal A^{t}\times\mathbb R^{t}\to\mathcal X$ do người thiết kế tác tử chọn, và **biểu diễn** (representation) tại $t$ là
$$
X_t=f_t\bigl(O_{0:t},A_{0:t-1},R_{1:t}\bigr)\in\mathcal X .
\tag{2.1}
$$
:::

Công thức (2.1) đọc là: biểu diễn tại $t$ chỉ dùng các quan sát tới $t$, các hành động tới $t-1$ và các phần thưởng tới $t$; $A_t$ và mọi tín hiệu sau nó chưa tồn tại khi tính $X_t$. Ba trường hợp thường gặp:

- **Chỉ dùng quan sát hiện tại:** $X_t=\phi(O_t)$ với $\phi$ không đổi theo $t$, chẳng hạn $X_t=O_t$ khi tác tử dùng luôn mã của Ví dụ 02.4.
- **Cửa sổ hữu hạn:** $m$ quan sát gần nhất cùng các hành động xen giữa, chẳng hạn $X_t=(O_t,A_{t-1},O_{t-1})$ khi $m=2$, với quy ước $X_0=(O_0,\varnothing,\varnothing)$.
- **Toàn bộ dữ liệu:** $X_t=(O_{0:t},A_{0:t-1},R_{1:t})$, tức lịch sử quan sát của Định nghĩa 01.2; kích thước tăng theo $t$.

Trong Ví dụ 02.4, $S_t=(2,1)$ và $O_t=(1,0,1,0)$; tác tử dùng luôn mã thì $X_t=O_t$, còn tác tử dùng cửa sổ hai quan sát thì $X_t$ khác $O_t$ (Ví dụ 02.5). Với mê cung có bản đồ cố định, ta chọn $\mathcal S$ là 27 ô đi được và $\mathcal S^+=\mathcal S\cup\{\mathrm G\}$; khi tác tử nhận tọa độ và dùng luôn tọa độ, $X_t=O_t=S_t$.

Biểu diễn thuộc tác tử, trạng thái thuộc môi trường. Biểu diễn luôn tính được, nhưng không bảo đảm khôi phục được trạng thái: không hàm nào của riêng mã hiện tại phân biệt được $(2,1)$ với $(3,1)$. Nhầm lẫn thường gặp là coi mã hiện tại là trạng thái chỉ vì đó là tất cả những gì tác tử nhận ở một bước; làm vậy là gộp $(2,1)$ và $(3,1)$, trong khi bước Đông từ hai ô này cho hai bộ mã kế tiếp khác nhau, $(1,0,1,0)$ và $(1,0,0,0)$.

<!-- note-topic-id: lec-02-topic-05 -->
### 2.3 Lịch sử trạng thái và quỹ đạo

Để nói quá khứ có giúp dự báo hay không, chúng ta cần một tên cho quá khứ của môi trường, ghi bằng trạng thái thay cho quan sát. Một cách trực quan, đó là cùng dãy luân phiên của Bài 01, chỉ đổi mỗi quan sát thành trạng thái tương ứng.

::: example Ví dụ 02.5 (Ba bước đầu trên mê cung $8\times8$)
**Dữ kiện.** Mê cung $8\times8$, phần thưởng $-1$ mỗi bước. Tác tử xuất phát tại $(0,2)$ và đi Đông, Bắc, Đông.

**Từng bước.** Tại $t=0$, từ $(0,2)$ đi Đông tới $(1,2)$, $R_1=-1$. Tại $t=1$, từ $(1,2)$ đi Bắc tới $(1,1)$, $R_2=-1$. Tại $t=2$, từ $(1,1)$ đi Đông tới $(2,1)$, $R_3=-1$.

**Lịch sử trạng thái.**
$$
H_3=\bigl((0,2),\ \text{Đông},\ -1,\ (1,2),\ \text{Bắc},\ -1,\ (1,1),\ \text{Đông},\ -1,\ (2,1)\bigr).
$$

**Khi cảm biến chỉ thấy bốn ô kề.** Tác tử nhận các quan sát $O_0=(1,0,1,1)$, $O_1=(0,1,0,0)$, $O_2=(1,0,0,1)$, $O_3=(1,0,1,0)$, không nhận các ô $(0,2)$, $(1,2)$, $(1,1)$, $(2,1)$.

**Cửa sổ hai quan sát.** Bước tiếp theo của đường 16 bước là Đông, từ $(2,1)$ tới $(3,1)$, nên $O_4=(1,0,1,0)$, trùng $O_3$. Với biểu diễn $X_t=(O_t,A_{t-1},O_{t-1})$ của Mục 2.2,
$$
X_3=\bigl((1,0,1,0),\ \text{Đông},\ (1,0,0,1)\bigr),\qquad X_4=\bigl((1,0,1,0),\ \text{Đông},\ (1,0,1,0)\bigr).
$$
Hai ô cho cùng quan sát nhưng khác biểu diễn. Dọc đường 16 bước, cửa sổ này cho mười sáu biểu diễn khác nhau; Tình huống 02.2 dùng tính chất đó để tách hai ô cùng mã $(1,1)$ và $(5,3)$.

**Kiểm tra lại.** $H_3$ có $3\cdot3+1=10$ thành phần. Tại $(0,2)$, ô phía Tây nằm ngoài lưới nên mã Tây là $1$.
:::

::: definition Định nghĩa 02.3 (Lịch sử trạng thái và quỹ đạo)
**Lịch sử** (history) trạng thái tới thời điểm $t$ là dãy
$$
H_t=(S_0,A_0,R_1,S_1,\dots,A_{t-1},R_t,S_t),\qquad H_0=(S_0).
\tag{2.2}
$$
**Quỹ đạo** (trajectory) của một lượt kết thúc tại $T<\infty$ là $\tau=H_T$.
:::

Ghi chú Bài 01 định nghĩa $H_t=(O_0,A_0,R_1,\dots,O_t)$ trên quan sát (Định nghĩa 01.2); (2.2) là trường hợp $O_t=S_t$ của định nghĩa đó. Từ đây tới hết chương, $H_t$ chỉ lịch sử trạng thái, dùng để phát biểu tính Markov của môi trường; khi quan sát một phần, tác tử không có $H_t$ mà chỉ có dữ liệu khả dụng của (2.1), như dãy mã trong Ví dụ 02.5. Quỹ đạo (2.2) với $t=T$ trùng quỹ đạo của Định nghĩa 01.7. Một tương tác không kết thúc không có quỹ đạo theo nghĩa này; khi đó ta chỉ xét các $H_t$ hữu hạn.

### 2.4 Quan sát đầy đủ và quan sát một phần

Ghi chú Bài 01 gọi tác tử là quan sát đầy đủ khi $O_t=S_t$. Về mặt ý tưởng, điều cần thiết chỉ là đọc lại được trạng thái từ quan sát, dù quan sát được viết dưới dạng khác; nhận xét sau mở rộng định nghĩa theo hướng đó.

::: remark Nhận xét 02.4 (Quan sát đầy đủ theo nghĩa tổng quát)
Môi trường được **quan sát đầy đủ** (full observability) khi có hàm $g:\mathcal O\to\mathcal S^+$ với $S_t=g(O_t)$ ở mọi $t$; trường hợp $g$ là hàm đồng nhất là định nghĩa của Bài 01. Ngược lại, môi trường được **quan sát một phần** (partial observability): có một quan sát ứng với hai trạng thái khác nhau có thể xảy ra. Với cảm biến bốn ô kề, mã $(1,0,1,0)$ ứng với đúng năm ô $(2,1)$, $(3,1)$, $(5,1)$, $(2,6)$, $(7,6)$, nên mê cung được quan sát một phần. Phân loại này tương đối với biến đã chọn làm trạng thái: cùng một cảm biến có thể cho quan sát đầy đủ với một lựa chọn và quan sát một phần với lựa chọn lớn hơn.
:::

![Hai cột so sánh. Cột trái, quan sát tọa độ: vị trí (2,1) cho quan sát (2,1), vị trí (3,1) cho quan sát (3,1); hai vị trí cho hai quan sát khác nhau. Cột phải, cảm biến bốn ô kề: cả vị trí (2,1) và vị trí (3,1) cho cùng một quan sát, Bắc và Nam là tường, Đông và Tây trống. Ô tối là tường, ô trắng đi được.](img/lec-02/full-partial-observation.svg)

Hai cột của hình dùng cùng hai vị trí; chỉ cảm biến khác nhau. Ở cột trái, hai vị trí cho hai quan sát, nên $g$ tồn tại; ở cột phải, hai mũi tên gặp nhau tại một quan sát. Theo cách phân loại này, mê cung với quan sát là tọa độ, hay là ảnh toàn bản đồ có vị trí tác tử, được quan sát đầy đủ. Bài giảng gốc (trang 27) nêu câu hỏi phân loại năm tình huống mà không kèm kết luận; Bài tập 02.15 của tệp bài tập phân loại các tình huống đó theo Nhận xét 02.4. Ở trang 18–19, bài giảng gốc gắn trường hợp quan sát đầy đủ với MDP của Bài 03, và trường hợp quan sát một phần với quá trình quyết định Markov quan sát một phần (partially observable Markov decision process, POMDP), trong đó tác tử tự xây dựng biểu diễn.

Quan sát đầy đủ chỉ nói đọc lại được biến đã chọn làm trạng thái; nó chưa bảo đảm biến đó chứa đủ thông tin để dự báo, vì người mô hình có thể chọn một biến nhỏ hơn cấu hình mà luật chuyển dùng tới.

### 2.5 Tính Markov

Trong mê cung $8\times8$, biết tác tử ở $(4,1)$ và chọn Nam thì biết chắc nó tới $(4,2)$ và nhận $-1$, bất kể nó đã đi đường nào. Về mặt ý tưởng, trạng thái hiện tại đã tóm tắt đủ quá khứ cho dự báo bước kế tiếp; đây chưa phải định nghĩa. Ví dụ sau cho thấy tính chất này phụ thuộc cách chọn trạng thái.

::: example Ví dụ 02.6 (Mê cung có chìa khóa)
**Dữ kiện.** Mê cung $8\times8$ của Ví dụ 02.1 với hai thay đổi: ngõ cụt $(4,2)$, chỉ nối với $(4,1)$, chứa chìa khóa và tác tử nhặt nó khi đi vào; lối từ $(7,6)$ vào $\mathrm G$ là cửa chỉ mở khi có chìa khóa, nếu không thì bước Đông từ $(7,6)$ giữ tác tử tại chỗ. Mọi bước nhận $-1$. Tác tử chọn hướng ngẫu nhiên, mỗi hướng với xác suất dương, nên mọi lịch sử hữu hạn hợp lệ có xác suất dương. Trạng thái được chọn là tọa độ ô.

**Hai lịch sử cùng độ dài.**

- $h$: tại $(0,2)$ đi Tây hai lần (đâm biên, đứng yên), rồi theo đường $(0,2)$, $(1,2)$, $(1,1)$, $(2,1)$, $(3,1)$, $(4,1)$, $(5,1)$, $(6,1)$, $(6,2)$, $(6,3)$, $(5,3)$, $(5,4)$, $(5,5)$, $(6,5)$, $(6,6)$, $(7,6)$; tác tử tới $(7,6)$ tại $t=2+15=17$ mà không qua $(4,2)$.
- $h'$: theo cùng đường, nhưng tại $(4,1)$ đi Nam vào $(4,2)$ rồi Bắc về $(4,1)$; tác tử tới $(7,6)$ tại $t=17$ và đã có chìa khóa.

**Dự báo bước Đông.** Sau $h$, $\Pr(S_{18}=\mathrm G\mid H_{17}=h,A_{17}=\text{Đông})=0$. Sau $h'$, xác suất đó bằng $1$. Cùng trạng thái $(7,6)$, cùng hành động, nhưng dự báo khác nhau tùy lịch sử.

**Sửa.** Chọn trạng thái là cặp (ô, $k$), với $k=1$ khi đã có chìa khóa; cặp này là toàn bộ cấu hình mà luật chuyển của mê cung dùng tới. Bước Đông từ $((7,6),1)$ vào $\mathrm G$, từ $((7,6),0)$ ở lại $((7,6),0)$, đều với xác suất $1$, bất kể lịch sử.

**Kiểm tra lại.** $h'$ dài hơn đường 16 bước đúng hai bước rẽ; $h$ bù hai bước đó bằng hai lần đứng yên ở đầu.
:::

::: definition Định nghĩa 02.5 (Tính Markov)
Giả sử $\mathcal S^+$ và tập giá trị phần thưởng $\mathcal R\subset\mathbb R$ đếm được, $H_t$ theo (2.2). Trạng thái có **tính Markov** (Markov property) nếu với mọi chính sách của tác tử, với các xác suất tính theo chính sách đó, mọi $t\ge0$, mọi lịch sử $h$ kết thúc tại $s\in\mathcal S$, mọi hành động $a$ với $\Pr(H_t=h,A_t=a)>0$, và mọi $s'\in\mathcal S^+$, $r\in\mathcal R$,
$$
\Pr\bigl(S_{t+1}=s',R_{t+1}=r\mid H_t=h,A_t=a\bigr)=\Pr\bigl(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a\bigr).
\tag{2.3}
$$
Định nghĩa áp dụng cho mọi dãy biến được chọn làm trạng thái, chẳng hạn biểu diễn $X_t$, bằng cách thay $S$ bằng dãy đó trong lịch sử và trong (2.3).
:::

Vế trái của (2.3) dự báo cặp (trạng thái kế tiếp, phần thưởng) khi biết toàn bộ quá khứ; vế phải chỉ dùng trạng thái cuối và hành động hiện tại. Điều kiện xác suất dương áp dụng cho biến cố được điều kiện hóa, không đòi mọi cặp $(s',r)$ có xác suất dương. Hai vế có thể phụ thuộc $t$; tính dừng của môi trường là giả thiết riêng, cần đến ở Mục 4. Đẳng thức được đòi với mọi chính sách, không chỉ với chính sách đang dùng; nhờ điều kiện này, với chính sách chỉ dùng trạng thái, hàm động lực ở Mục 4.5 không phụ thuộc chính sách.

Với trạng thái là tọa độ trong Ví dụ 02.6, lấy $t=17$, $s=(7,6)$, $a=\text{Đông}$, $s'=\mathrm G$, $r=-1$: vế trái bằng $0$ với $h$ và $1$ với $h'$, nên không thể cùng bằng vế phải. Với trạng thái (ô, $k$), vế trái chỉ phụ thuộc ô cuối và $k$, đúng như vế phải. Cấu hình đầy đủ của mọi môi trường có tính Markov, vì theo Định nghĩa 01.2, luật chuyển chỉ dùng cấu hình hiện tại, hành động và yếu tố ngẫu nhiên riêng của bước đó. Tính Markov mất khi biến được chọn bỏ đi phần cấu hình mà luật chuyển cần, như tọa độ thiếu bit $k$. Trong mê cung gốc không có chìa khóa, tọa độ có tính Markov vì luật chuyển và phần thưởng chỉ phụ thuộc ô hiện tại và hướng đi.

Sutton và Barto (2018, §3.1, trang 49) viết rằng tính Markov là ràng buộc lên trạng thái: trạng thái phải chứa mọi khía cạnh của quá khứ có ảnh hưởng tới tương lai. Từ đó có hai nhầm lẫn thường gặp. Thứ nhất, đọc lại được tọa độ không kéo theo tính Markov: trong Ví dụ 02.6, tác tử nhận tọa độ, nên với trạng thái là tọa độ, mê cung được quan sát đầy đủ theo Nhận xét 02.4; nhưng tọa độ thiếu bit $k$ nên không có tính Markov. Nếu chọn trạng thái là cấu hình (ô, $k$), vốn có tính Markov, thì cùng tác tử đó chỉ quan sát một phần, vì quan sát $(7,6)$ ứng với cả $((7,6),0)$ và $((7,6),1)$. Thứ hai, (2.3) chỉ nói về dự báo bước kế tiếp, không chỉ ra hành động nào tốt.

Bài giảng gốc (trang 17) phát biểu giả thuyết Markov dưới dạng "tương lai độc lập với quá khứ khi biết hiện tại". Đòi hỏi này có hạn chế những gì mô hình hóa được không? Mệnh đề sau cho thấy về nguyên tắc thì không, nếu cho phép trạng thái lớn dần.

::: proposition Mệnh đề 02.6 (Lịch sử là trạng thái Markov)
**Giả thiết.** $\mathcal S^+$ và $\mathcal R$ đếm được; $H_t$ theo (2.2). Đặt $\tilde S_t=H_t$ và gọi $\tilde H_t=(\tilde S_0,A_0,R_1,\tilde S_1,\dots,A_{t-1},R_t,\tilde S_t)$ là lịch sử của dãy mới.

**Kết luận.** Dãy $\tilde S_t$ có tính Markov: với mọi $t$, mọi $\tilde h$ kết thúc tại $h$ và mọi $a$ với $\Pr(\tilde H_t=\tilde h,A_t=a)>0$,
$$
\Pr\bigl(\tilde S_{t+1}=\tilde s',R_{t+1}=r\mid \tilde H_t=\tilde h,A_t=a\bigr)=\Pr\bigl(\tilde S_{t+1}=\tilde s',R_{t+1}=r\mid \tilde S_t=h,A_t=a\bigr).
$$

**Điều kiện áp dụng.** Không cần giả thiết nào về động lực của môi trường ngoài tính đếm được; $S_t$ có thể không có tính Markov.

**Phạm vi.** $\tilde S_t$ có $3t+1$ thành phần, nên tập giá trị của nó khác nhau ở mỗi $t$. Mệnh đề dùng trạng thái của môi trường; khi quan sát một phần, tác tử không có $H_t$.
:::

::: proof Chứng minh Mệnh đề 02.6
**Bước 1 (lịch sử của dãy mới là hàm của phần tử cuối).** Mỗi $H_k$ với $k\le t$ là đoạn đầu gồm $3k+1$ thành phần của $H_t$, và $A_k$, $R_{k+1}$ với $k<t$ là thành phần của $H_t$, vì (2.2) chỉ nối thêm mà không xóa. Do đó có hàm $\psi_t$ với $\tilde H_t=\psi_t(H_t)$.

**Bước 2 (hai biến cố điều kiện trùng nhau).** Lấy $\tilde h$ với $\Pr(\tilde H_t=\tilde h)>0$ và phần tử cuối $h$. Chọn một kết cục có $\tilde H_t=\tilde h$; tại đó $H_t=h$ và $\tilde H_t=\psi_t(H_t)$, nên $\tilde h=\psi_t(h)$. Bây giờ, nếu $\tilde H_t=\tilde h$ thì $H_t=\tilde S_t=h$; ngược lại, nếu $H_t=h$ thì $\tilde H_t=\psi_t(h)=\tilde h$. Vậy
$$
\{\tilde H_t=\tilde h,\ A_t=a\}=\{H_t=h,\ A_t=a\}=\{\tilde S_t=h,\ A_t=a\},
$$
trong đó đẳng thức thứ hai là định nghĩa $\tilde S_t=H_t$.

**Bước 3 (kết luận).** Hai vế của đẳng thức cần chứng minh là xác suất của cùng biến cố $\{\tilde S_{t+1}=\tilde s',R_{t+1}=r\}$ có điều kiện trên cùng một biến cố có xác suất dương (Bước 2), nên bằng nhau; xác suất có điều kiện là tỉ số vì các tập đếm được. $\square$
:::

Đọc bằng lời: nếu trạng thái ghi lại toàn bộ quá khứ, quá khứ không thể mang thêm thông tin, nên tính Markov luôn đạt được. Trong Ví dụ 02.6, $H_t$ cho biết lịch sử có qua $(4,2)$ hay không; cách sửa (ô, $k$) gọn hơn, vì thay cho dãy dài $3t+1$ ta chỉ thêm một bit.

Mệnh đề có hai giới hạn. Chứng minh không dùng gì về môi trường, nên kết quả không cho thông tin nào về môi trường; cái giá của tính Markov ở đây là một trạng thái dài thêm sau mỗi bước. Vì số thành phần của $\tilde S_t$ thay đổi theo $t$, các phương pháp dạng bảng của Bài 04–06, vốn cần một tập trạng thái cố định, không dùng trực tiếp được trạng thái này.

::: remark Nhận xét 02.7 (Cửa sổ hữu hạn)
Giữ $m$ quan sát gần nhất cùng các hành động xen giữa cho biểu diễn có kích thước cố định; Sutton và Barto (2018, §17.3, trang 468) gọi đây là cách tiếp cận lịch sử bậc $k$ ($k$-th order history approach), với $k$ là độ dài cửa sổ; ở đây độ dài đó ký hiệu là $m$, vì $k$ đã là bit chìa khóa của Ví dụ 02.6. Cửa sổ hữu hạn không bảo đảm tính Markov. Trong Ví dụ 02.6, sau khi vào $(4,2)$, lịch sử $h'$ đi qua mười ô $(4,1)$, $(5,1)$, $(6,1)$, $(6,2)$, $(6,3)$, $(5,3)$, $(5,4)$, $(5,5)$, $(6,5)$, $(6,6)$ rồi tới $(7,6)$, nên trong $h'$, ô $(4,2)$ đứng trước $(7,6)$ đúng mười một bước. Cửa sổ $m$ quan sát tọa độ kết thúc tại $(7,6)$ chứa $(4,2)$ khi và chỉ khi $m-1\ge11$; với $m\le11$, cửa sổ của $h$ và $h'$ trùng nhau. Với các lịch sử dài hơn, chẳng hạn đâm tường nhiều lần sau khi nhặt chìa khóa, khoảng cách lớn tùy ý, nên không có $m$ hữu hạn nào đủ cho ví dụ này.
:::

**Trong thực hành.** Quan sát của CartPole (Bài 04) là $(x,\dot x,\theta,\dot\theta)$; nếu chỉ giữ vị trí xe và góc cột, hai lần ghé cùng vị trí, cùng góc nhưng khác vận tốc sẽ chuyển khác nhau sau cùng hành động, đúng kiểu vi phạm (2.3). Trong notebook Bài 04, quan sát được chia thành $3\cdot3\cdot6\cdot6=324$ ô; một ô gộp nhiều trạng thái liên tục nên nói chung không có tính Markov, và một nhiệm vụ của notebook so $\hat p(s'\mid s,a)$ với $\hat p(s'\mid s,a,s_{\text{trước}})$ để kiểm tra trực tiếp.

Trong Lunar Lander có gió (Bài 05, phần gợi mở), lực gió phụ thuộc một chỉ số nội bộ không có trong quan sát, nên quan sát không có tính Markov ngay cả trước khi chia ô. Quan sát 12 chiều của Flappy Bird (Bài 07) chứa vận tốc dọc của chim, nên đặc trưng tính từ quan sát hiện tại vẫn mang thông tin vận tốc.

::: exercise Bài tập 02.2 (Mã bốn ô kề)
Mê cung $8\times8$ của Ví dụ 02.1; quan sát là mã bốn ô kề của Ví dụ 02.4 (Bắc, Đông, Nam, Tây; $1$ khi bước theo hướng đó giữ tác tử đứng yên, $0$ khi bước đưa tác tử sang ô khác).

- (a) Tính mã tại $(1,2)$ và tại $(6,3)$.
- (b) Phân loại hai cách quan sát, tọa độ và mã bốn ô kề, theo Nhận xét 02.4, với trạng thái là tọa độ.
:::

::: hint
Hàng $1$ trống từ cột $1$ tới cột $6$; hàng $2$ trống tại các cột $0$, $1$, $4$, $6$; hàng $3$ trống tại các cột $1$, $2$, $5$, $6$; hàng $4$ trống tại các cột $2$, $3$, $5$.
:::

::: solution
**Câu (a).** Tại $(1,2)$: Bắc $(1,1)$ trống, Đông $(2,2)$ tường, Nam $(1,3)$ trống, Tây $(0,2)$ trống; mã $(0,1,0,0)$. Tại $(6,3)$: Bắc $(6,2)$ trống, Đông $(7,3)$ tường, Nam $(6,4)$ tường, Tây $(5,3)$ trống; mã $(0,1,1,0)$.

**Câu (b).** Tọa độ cho quan sát đầy đủ, với $g$ là hàm đồng nhất. Mã bốn ô kề cho quan sát một phần: mã $(1,0,1,0)$ ứng với cả $(2,1)$ và $(3,1)$ (Ví dụ 02.4), nên không có $g$ nào.

**Kiểm tra lại.** Ô $(1,2)$ có ba hướng mã $0$, khớp việc nó nối $(0,2)$, $(1,1)$ và $(1,3)$.
:::

::: exercise Bài tập 02.3 (Trạng thái Markov cho mê cung có chìa khóa)
Mê cung có chìa khóa của Ví dụ 02.6: 27 ô đi được; chìa khóa ở ngõ cụt $(4,2)$, chỉ nối với $(4,1)$, được nhặt khi vào ô đó; bước Đông từ $(7,6)$ vào $\mathrm G$ chỉ khi đã có chìa khóa; mọi bước nhận $-1$; xuất phát tại $(0,2)$ chưa có chìa khóa. Trạng thái là cặp (ô, $k$) với $k\in\{0,1\}$.

- (a) Trạng thái nào trong $27\cdot2=54$ trạng thái chưa kết thúc không bao giờ xuất hiện khi xuất phát tại $(0,2)$.
- (b) Tính tổng phần thưởng của đường ngắn nhất từ $(0,2)$ tới $\mathrm G$, biết đường ngắn nhất không có chìa khóa dài 16 bước và không qua $(4,2)$.
:::

::: hint
Xét giá trị của $k$ ngay khi tác tử vào $(4,2)$.
:::

::: solution
**Câu (a).** Trạng thái $((4,2),0)$: tác tử chỉ ở $(4,2)$ sau khi đi vào, và lúc đó đã nhặt chìa khóa. Còn $26+27=53$ trạng thái xuất hiện được.

**Câu (b).** Mọi đường tới $\mathrm G$ phải ghé $(4,2)$; mỗi lần ghé tốn ít nhất hai bước so với đường không ghé, vì $(4,2)$ chỉ nối với $(4,1)$. Đường ngắn nhất dài $16+2=18$ bước, tổng phần thưởng $-18$.

**Kiểm tra lại.** Đường 18 bước này là đường $h'$ của Ví dụ 02.6 thêm bước Đông cuối từ $(7,6)$: $17+1=18$.
:::

Như vậy, chúng ta đã tách biểu diễn khỏi trạng thái và quan sát (Định nghĩa 02.2), ghi quá khứ của môi trường bằng lịch sử trạng thái (Định nghĩa 02.3), mở rộng khái niệm quan sát đầy đủ (Nhận xét 02.4) và phát biểu tính Markov (Định nghĩa 02.5). Mệnh đề 02.6 cho thấy lịch sử luôn là trạng thái Markov nhưng lớn dần, còn cửa sổ hữu hạn không bảo đảm tính chất này (Nhận xét 02.7). Biểu diễn đã có, nhưng chưa có cách viết việc tác tử dùng nó để chọn hướng. Trong Mục 3, chúng ta viết quy tắc đó thành một phân phối trên $X_t$.

<!-- note-topic-id: lec-02-part-04 -->
## 3. Quy tắc chọn hành động

Xét hai tác tử trên mê cung $8\times8$, cùng dùng tọa độ làm biểu diễn và cùng đang ở $(1,2)$: tác tử thứ nhất luôn đi Bắc, tác tử thứ hai tung đồng xu để chọn Bắc hoặc Đông. Muốn so sánh hai tác tử, chúng ta cần viết cách chọn hướng thành một đối tượng toán học trên biểu diễn, bao gồm cả cách chọn ngẫu nhiên.

![Mê cung tám hàng tám cột với một mũi tên trong mỗi ô đi được, chỉ hướng mà chính sách chọn tại ô đó. Từ ô bắt đầu (0,2) mũi tên chỉ Đông; tại (1,2) chỉ Bắc; dọc hàng 1 từ (1,1) tới (5,1) chỉ Đông; tại (6,1), (6,2) chỉ Nam; tại (6,3) chỉ Tây; tại (5,3), (5,4) chỉ Nam; tại (5,5) chỉ Đông; tại (6,5) chỉ Nam; tại (6,6), (7,6) chỉ Đông, ra đích G tại (8,6). Các ô ngoài đường chính cũng có mũi tên dẫn về đường chính, chẳng hạn (4,2) chỉ Bắc. Theo các mũi tên từ ô bắt đầu cần 16 bước, thưởng âm một mỗi bước.](img/lec-02/source-policy.svg)

Hình lấy từ bài giảng gốc (trang 26) gán cho mỗi ô đi được đúng một hướng. Theo mũi tên từ $(0,2)$, ta đi lại đường 16 bước của Ví dụ 02.1; các ô ngoài đường chính, như ngõ cụt $(4,2)$ hay nhánh dưới từ $(1,3)$ tới $(4,6)$, cũng có mũi tên. Một bảng gán hướng cho mọi ô như vậy là một chính sách xác định trên tọa độ.

<!-- note-topic-id: lec-02-topic-06 -->
### 3.1 Phân phối hành động trên biểu diễn

Một cách trực quan, chính sách trả lời câu hỏi "với thông tin này, chọn mỗi hành động với xác suất bao nhiêu", còn hàm động lực của môi trường trả lời "chọn hành động này thì điều gì xảy ra". Hai ví dụ sau làm cụ thể câu hỏi thứ nhất.

::: example Ví dụ 02.7 (Hai quy tắc tại ô $(1,2)$)
**Dữ kiện.** Mê cung $8\times8$; biểu diễn là tọa độ, $x=(1,2)$; ô Đông $(2,2)$ là tường. Hai quy tắc ghi bằng xác suất chọn mỗi hướng:

| Quy tắc | Bắc | Đông | Nam | Tây |
|---|---|---|---|---|
| Luôn Bắc | $1$ | $0$ | $0$ | $0$ |
| Bắc hoặc Đông | $0{,}5$ | $0{,}5$ | $0$ | $0$ |

**Đọc bảng.** Mỗi hàng là một phân phối trên bốn hướng: các số không âm, tổng bằng $1$. Với quy tắc thứ hai, khi chọn Đông, tác tử gặp tường, đứng yên tại $(1,2)$ và nhận $-1$, nên tính ngẫu nhiên tự nó không làm quy tắc tốt hơn.

**Kiểm tra lại.** Tổng hàng thứ hai là $0{,}5+0{,}5+0+0=1$.
:::

::: definition Định nghĩa 02.8 (Chính sách trên biểu diễn)
Cho tập biểu diễn $\mathcal X$; với mỗi $x\in\mathcal X$, tập hành động hợp lệ $\mathcal A(x)\subseteq\mathcal A$ xác định được từ $x$. Một **chính sách ngẫu nhiên** gán cho mỗi $x$ một phân phối $\pi(\cdot\mid x)$ trên $\mathcal A(x)$:
$$
\pi(a\mid x)\ge0,\qquad\sum_{a\in\mathcal A(x)}\pi(a\mid x)=1 .
\tag{3.1}
$$
Tác tử theo $\pi$ chọn hành động với
$$
\Pr(A_t=a\mid X_t=x)=\pi(a\mid x)\qquad\text{với mọi }t,
\tag{3.2}
$$
và lựa chọn tại $t$ không phụ thuộc dữ liệu quá khứ khi đã biết $X_t$. Một **chính sách xác định** là hàm $\pi:\mathcal X\to\mathcal A$ với $\pi(x)\in\mathcal A(x)$ và $A_t=\pi(X_t)$, tức trường hợp $\pi(a\mid x)=1$ khi $a=\pi(x)$.
:::

Định nghĩa có ba thành phần. Đầu vào là biểu diễn $X_t$, vì chính sách chỉ dùng được thông tin mà tác tử có. Quy tắc không đổi theo $t$, tức chính sách dừng; chúng ta chỉ xét trường hợp này. Điều kiện cuối của (3.2) nói rằng mọi thông tin quá khứ mà chính sách cần phải nằm trong $X_t$, nên tác tử muốn nhớ quá khứ phải đưa ký ức vào biểu diễn theo (2.1).

Định nghĩa tổng quát hóa Định nghĩa 01.11 theo một chiều và thu hẹp nó theo chiều kia. Khi $X_t$ là lịch sử quan sát của Định nghĩa 01.2, ta được lại chính sách trên lịch sử của Bài 01, và chính sách xác định ở đây là chính sách tất định của Định nghĩa 01.11. Khi $X_t$ gọn hơn lịch sử, chẳng hạn mã bốn ô kề, chính sách chỉ được dùng phần thông tin còn giữ trong $X_t$. Với $X_t=S_t$ khi quan sát đầy đủ, ta viết $\pi(a\mid s)$. Quy tắc thứ hai của Ví dụ 02.7 là $\pi(\text{Bắc}\mid(1,2))=\pi(\text{Đông}\mid(1,2))=0{,}5$; bảng của hình đầu mục là một chính sách xác định. Phản ví dụ: gán $\pi(\text{Bắc}\mid x)=0{,}6$ và $\pi(\text{Đông}\mid x)=0{,}6$ không cho chính sách, vì tổng vượt $1$.

::: remark Nhận xét 02.9 (Các nhầm lẫn về chính sách)
- Một chính sách viết trên trạng thái mà tác tử không thấy thì không cài đặt được; khi quan sát một phần, đầu vào phải là biểu diễn.
- Chính sách là quy tắc đang dùng; thuật toán học là cách tạo ra hoặc thay đổi quy tắc từ dữ liệu. Trong khi học, chính sách đổi theo thời gian; định nghĩa trên mô tả quy tắc cố định trong suốt một phép đánh giá.
:::

Puterman (1994, §2.1) phân loại chính sách theo hai trục: xác định hay ngẫu nhiên, phụ thuộc trạng thái hiện tại hay phụ thuộc lịch sử. Định nghĩa 02.8 phủ cả hai trục, vì biểu diễn có thể là trạng thái hoặc lịch sử. Giáo trình *Học máy thống kê* gọi chính sách xác định là chính sách đơn định.

### 3.2 Xác suất của một dãy hành động

Khi tác tử theo một chính sách ngẫu nhiên, mỗi lượt là một quỹ đạo ngẫu nhiên. Để chuẩn bị cho phép lấy kỳ vọng ở Mục 4, ta tính xác suất của một dãy hai hành động.

::: example Ví dụ 02.8 (Xác suất của một dãy hai hành động)
**Dữ kiện.** Mê cung $8\times8$, biểu diễn là tọa độ, luật chuyển tất định. Chính sách tại hai ô: $\pi(\text{Bắc}\mid(1,2))=\pi(\text{Đông}\mid(1,2))=0{,}5$; $\pi(\text{Đông}\mid(1,1))=0{,}9$, $\pi(\text{Nam}\mid(1,1))=0{,}1$. Tại $t=1$, tác tử ở $(1,2)$.

**Bắc rồi Đông.** Bắc đưa tác tử tới $(1,1)$ chắc chắn; tại đó Đông có xác suất $0{,}9$. Theo quy tắc nhân,
$$
\Pr(A_1=\text{Bắc},A_2=\text{Đông}\mid S_1=(1,2))=0{,}5\cdot0{,}9=0{,}45,
$$
và tác tử tới $(2,1)$.

**Đông rồi Bắc.** Đông đâm vào tường $(2,2)$, tác tử đứng yên tại $(1,2)$; tại đó Bắc có xác suất $0{,}5$, nên xác suất của dãy là $0{,}5\cdot0{,}5=0{,}25$, và tác tử tới $(1,1)$.

**Kiểm tra lại.** Bốn dãy có xác suất dương là (Bắc, Đông), (Bắc, Nam), (Đông, Bắc), (Đông, Đông), với xác suất $0{,}45$, $0{,}05$, $0{,}25$, $0{,}25$; tổng bằng $1$.
:::

Thừa số thứ hai trong mỗi tích là xác suất của chính sách tại ô mà môi trường đưa tác tử tới sau bước đầu, nên xác suất của một dãy hành động phụ thuộc cả chính sách lẫn luật chuyển. Kỳ vọng ở Mục 4 vì thế lấy theo cả hai.

**Trong thực hành.** Trong bài thực hành Bài 05, chính sách được đánh giá trên Lunar Lander làm theo hành động $\mu(o)$ của bộ điều khiển heuristic của Gymnasium với xác suất $0{,}9$, và với xác suất $\varepsilon=0{,}1$ chọn đều một trong bốn hành động. Theo Định nghĩa 02.8, $\pi(\mu(o)\mid o)=0{,}9+0{,}1\cdot\tfrac14=0{,}925$ và mỗi hành động còn lại có xác suất $0{,}025$. Chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy) của Bài 06 có cùng cấu trúc, với $\mu(o)$ thay bằng hành động có giá trị ước lượng lớn nhất.

::: exercise Bài tập 02.4 (Chính sách ngẫu nhiên tại một ô)
Mê cung $8\times8$, biểu diễn là tọa độ, $x=(1,2)$; ô Đông $(2,2)$ là tường, các ô $(1,1)$, $(1,3)$, $(0,2)$ trống. Một chính sách cho $\pi(\text{Bắc}\mid x)=0{,}2$, $\pi(\text{Đông}\mid x)=0{,}5$, $\pi(\text{Tây}\mid x)=0$; tại $(1,1)$ nó chọn Đông với xác suất $0{,}9$ và Nam với xác suất $0{,}1$; tại $(1,3)$ nó luôn chọn Bắc.

- (a) Tính $\pi(\text{Nam}\mid x)$ và cho biết chính sách tại $x$ là xác định hay ngẫu nhiên.
- (b) Tính xác suất tác tử vẫn ở $x$ sau hai bước, xuất phát từ $x$.
:::

::: hint
Ở câu (b), liệt kê các dãy hai hành động đưa tác tử trở về hoặc giữ tác tử ở $x$: đứng yên hai lần, hoặc đi rồi quay lại.
:::

::: solution
**Câu (a).** Theo (3.1), $\pi(\text{Nam}\mid x)=1-0{,}2-0{,}5-0=0{,}3$. Chính sách ngẫu nhiên, vì ba hành động có xác suất dương.

**Câu (b).** Ba cách giữ tác tử ở $x$ sau hai bước:

- Đông, Đông: đứng yên hai lần, xác suất $0{,}5\cdot0{,}5=0{,}25$;
- Bắc tới $(1,1)$ rồi Nam về $x$: $0{,}2\cdot0{,}1=0{,}02$;
- Nam tới $(1,3)$ rồi Bắc về $x$: $0{,}3\cdot1=0{,}3$.

Tổng là $0{,}25+0{,}02+0{,}3=0{,}57$.

**Kiểm tra lại.** Mọi dãy khác rời $x$: Đông rồi Bắc hoặc Nam, Bắc rồi Đông; tổng xác suất của chúng là $0{,}5\cdot0{,}5+0{,}2\cdot0{,}9=0{,}43=1-0{,}57$.
:::

Như vậy, chúng ta đã viết quy tắc chọn hành động thành một phân phối trên biểu diễn (Định nghĩa 02.8), với chính sách xác định là trường hợp riêng và chính sách trên lịch sử của Bài 01 là trường hợp $X_t$ bằng lịch sử quan sát. Xác suất của một dãy hành động phụ thuộc cả chính sách lẫn luật chuyển (Ví dụ 02.8). Tuy nhiên, chúng ta chưa có cách nói chính sách nào tốt hơn, vì phần thưởng tức thời không phân biệt được hai chính sách trên mê cung. Trong Mục 4, chúng ta đo cả chuỗi phần thưởng về sau và lấy kỳ vọng của nó dưới chính sách.

<!-- note-topic-id: lec-02-part-05 -->
## 4. Lợi tức, hàm giá trị và hàm động lực

Trên mê cung $8\times8$, tại $(4,1)$, bước Đông và bước Nam đều nhận $-1$. Nếu sau đó tác tử theo chính sách của hình ở Mục 3, bước Đông dẫn tới $\mathrm G$ sau thêm 10 bước, còn bước Nam vào ngõ cụt $(4,2)$, quay về $(4,1)$ rồi mới đi tiếp, tốn thêm hai bước. Để biến nhận xét này thành phép so sánh, chúng ta cần ba việc: quy một chuỗi phần thưởng về một số, kèm lý do chọn trọng số theo thời gian; lấy trung bình số đó khi có yếu tố ngẫu nhiên; và mô tả riêng phần dự báo một bước của môi trường.

<!-- note-topic-id: lec-02-topic-07 -->
### 4.1 Ưu tiên dừng và trọng số hình học

Tổng không chiết khấu của Bài 01 chỉ là một số khi lượt kết thúc. Với một tương tác không kết thúc và phần thưởng $-1$ mỗi bước, tổng riêng sau $n$ bước là $-n$, tiến về $-\infty$ với mọi cách đi, nên tổng đó không phân biệt được hai chính sách; với phần thưởng đổi dấu, chẳng hạn $+1,-1,+1,\dots$, tổng riêng dao động giữa $1$ và $0$ và không có giới hạn. Vì vậy chúng ta xét tổng có trọng số theo vị trí, với trọng số khác $1$; đây là cách đơn giản nhất để quy một chuỗi phần thưởng về một số. Về mặt ý tưởng, nếu tác tử thích chuỗi này hơn chuỗi kia, thì việc cả hai cùng bắt đầu bằng một phần thưởng chung không nên làm đổi ý; đây chưa phải định nghĩa. Ví dụ sau cho thấy đòi hỏi này loại bỏ phần lớn các cách chọn trọng số.

::: example Ví dụ 02.9 (Hai chuỗi $(2,0)$ và $(1,1)$)
**Dữ kiện.** Hai chuỗi phần thưởng $\sigma=(2,0)$ và $\sigma'=(1,1)$; lợi ích là tổng có trọng số, phần thưởng ở vị trí $i$ nhân với $w_i$.

**Trọng số $(1,1,1,\dots)$.** $U(\sigma)=2=U(\sigma')$: hai chuỗi ngang nhau.

**Trọng số $w_i=0{,}5^{i-1}$.** $U(\sigma)=2>1{,}5=U(\sigma')$. Thêm cùng phần thưởng $r$ vào đầu:
$$
U((r,2,0))=r+0{,}5\cdot2+0{,}25\cdot0=r+1,\qquad U((r,1,1))=r+0{,}5+0{,}25=r+0{,}75 .
$$
Chuỗi đầu vẫn được ưu tiên với mọi $r$.

**Trọng số $(1;\ 0{,}5;\ 0{,}5;\dots)$.** Vẫn có $U(\sigma)=2>1{,}5=U(\sigma')$, nhưng sau khi thêm $r$, $U((r,2,0))=r+1=U((r,1,1))$: ưu tiên chặt biến thành ngang nhau.

**Kiểm tra lại.** Với $w_i=0{,}5^{i-1}$, hiệu sau khi thêm $r$ là $0{,}25$, bằng $0{,}5$ nhân hiệu ban đầu $0{,}5$.
:::

Bộ trọng số thứ ba dương và không tăng, nhưng tỉ số giữa hai trọng số liên tiếp không cố định ($0{,}5$ rồi $1$), và điều đó làm thứ tự đổi khi chuỗi bị đẩy lùi một bước. Bộ thứ hai có tỉ số cố định $0{,}5$, và hiệu lợi ích chỉ bị nhân với $0{,}5$.

::: definition Định nghĩa 02.10 (Lợi ích cộng và ưu tiên dừng)
Cho dãy trọng số $(w_i)_{i\ge1}$ dùng chung cho mọi độ dài chuỗi. Với chuỗi phần thưởng hữu hạn $\sigma=(\sigma_1,\dots,\sigma_n)\in\mathbb R^n$, $n\ge1$, **lợi ích cộng** là
$$
U(\sigma)=\sum_{i=1}^{n}w_i\sigma_i ,
\tag{4.1}
$$
và $\sigma\succ\sigma'$ khi và chỉ khi $U(\sigma)>U(\sigma')$. Với $r\in\mathbb R$, $[r,\sigma]=(r,\sigma_1,\dots,\sigma_n)$. Quan hệ $\succ$ là **ưu tiên dừng** (stationary preference) nếu với mọi chuỗi hữu hạn $\sigma$, $\sigma'$, có thể khác độ dài, và mọi $r$,
$$
\sigma\succ\sigma'\iff[r,\sigma]\succ[r,\sigma'].
\tag{4.2}
$$
:::

Công thức (4.1) gán cho phần thưởng thứ $i$ của chuỗi trọng số $w_i$, không phụ thuộc chuỗi dài bao nhiêu. Điều kiện (4.2) đọc là: thứ tự giữa hai tương lai không đổi khi cả hai bắt đầu sau một bước chung. Russell và Norvig (2020, §17.1.1, trang 566) diễn đạt điều này cho hai lịch sử có cùng chuyển đầu, và phát biểu không kèm chứng minh rằng chỉ lợi ích cộng có chiết khấu thỏa điều kiện đó. Tính dừng ở đây nói về cách so sánh chuỗi phần thưởng; tính Markov ở Mục 2.5 nói về trạng thái của môi trường.

::: theorem Định lý 02.11 (Ưu tiên dừng buộc trọng số hình học)
**Giả thiết.** Các chuỗi phần thưởng hữu hạn được so sánh bằng lợi ích cộng (4.1) với một dãy trọng số dùng chung cho mọi độ dài, thỏa $w_1=1$, $w_i>0$ và $w_{i+1}\le w_i$ với mọi $i$.

**Kết luận.** $\succ$ là ưu tiên dừng khi và chỉ khi có $\gamma\in(0,1]$ với
$$
w_i=\gamma^{i-1}\qquad\text{với mọi }i\ge1 .
\tag{4.3}
$$
Khi đó $U([r,\sigma])=r+\gamma U(\sigma)$ với mọi chuỗi hữu hạn $\sigma$ và mọi $r$.

**Điều kiện áp dụng.** Chuỗi hữu hạn, tất định; (4.2) được đòi cho mọi cặp chuỗi, kể cả khác độ dài. Điều kiện $w_1=1$ chỉ là chuẩn hóa.

**Phạm vi.** Định lý không xác định giá trị của $\gamma$, và không nói gì về chuỗi vô hạn (Mệnh đề 02.13) hay chuỗi ngẫu nhiên, nơi phải chọn thêm cách so sánh các phân phối.
:::

::: proof Chứng minh Định lý 02.11
**Bước 1 (tính dừng bảo toàn sự ngang nhau).** Giả sử $\succ$ dừng và $U(\sigma)=U(\sigma')$. Nếu $U([r,\sigma])>U([r,\sigma'])$ thì theo chiều "$\Leftarrow$" của (4.2), $U(\sigma)>U(\sigma')$, mâu thuẫn; trường hợp ngược lại tương tự. Vậy $U([r,\sigma])=U([r,\sigma'])$. Với hai chuỗi cùng độ dài $n$ và $d_i=\sigma_i-\sigma'_i$, phần tử $\sigma_i$ đứng ở vị trí $i+1$ trong $[r,\sigma]$, nên
$$
\begin{aligned}
U([r,\sigma])-U([r,\sigma'])
&=\Bigl(w_1r+\sum_{i=1}^{n}w_{i+1}\sigma_i\Bigr)-\Bigl(w_1r+\sum_{i=1}^{n}w_{i+1}\sigma'_i\Bigr)
&&\text{((4.1) với độ dài }n+1)\\
&=\sum_{i=1}^{n}w_{i+1}d_i
&&\text{(hai số hạng }w_1r\text{ triệt tiêu)},
\end{aligned}
$$
và $U(\sigma)-U(\sigma')=\sum_{i=1}^{n}w_id_i$. Mọi $d\in\mathbb R^n$ là hiệu của hai chuỗi, chẳng hạn $\sigma=d$, $\sigma'=(0,\dots,0)$. Vậy với mọi $n$ và mọi $d\in\mathbb R^n$,
$$
\sum_{i=1}^{n}w_id_i=0\ \Longrightarrow\ \sum_{i=1}^{n}w_{i+1}d_i=0 .
\tag{4.4}
$$

**Bước 2 (truy hồi của trọng số).** Cố định $j\ge2$, lấy $n=j$, $d_1=w_j$, $d_j=-w_1$, các $d_i$ khác bằng $0$. Khi đó $\sum_iw_id_i=w_1w_j-w_jw_1=0$, nên
$$
\begin{aligned}
0&=\sum_{i=1}^{j}w_{i+1}d_i
&&\text{(4.4)}\\
&=w_2w_j-w_{j+1}w_1
&&\text{(chỉ }d_1,d_j\text{ khác }0)\\
&=w_2w_j-w_{j+1}
&&(w_1=1).
\end{aligned}
$$
Đặt $\gamma=w_2$; ta có $w_{j+1}=\gamma w_j$ với mọi $j\ge2$, và với $j=1$ vì $w_2=\gamma\cdot1$. Quy nạp từ $w_1=1$ cho $w_i=\gamma^{i-1}$. Giả thiết $w_2>0$ cho $\gamma>0$, và $w_2\le w_1=1$ cho $\gamma\le1$.

**Bước 3 (chiều ngược lại).** Giả sử $w_i=\gamma^{i-1}$, $\gamma\in(0,1]$. Với chuỗi $\sigma$ độ dài $n$,
$$
\begin{aligned}
U([r,\sigma])&=r+\sum_{i=1}^{n}\gamma^{i}\sigma_i
&&\text{((4.1) với độ dài }n+1)\\
&=r+\gamma\sum_{i=1}^{n}\gamma^{i-1}\sigma_i
&&\text{(đặt }\gamma\text{ ra ngoài)}\\
&=r+\gamma U(\sigma)
&&\text{((4.1) với độ dài }n).
\end{aligned}
$$
Do đó $U([r,\sigma])-U([r,\sigma'])=\gamma\bigl(U(\sigma)-U(\sigma')\bigr)$ với mọi $\sigma$, $\sigma'$, kể cả khác độ dài; vì $\gamma>0$, hai hiệu cùng dấu, nên (4.2) đúng. $\square$
:::

Định lý đọc bằng lời: nếu đã đo chuỗi phần thưởng bằng tổng có trọng số, đòi hỏi thứ tự không đổi khi đẩy lùi một bước buộc mỗi trọng số bằng trọng số trước nhân một hệ số cố định $\gamma$, gọi là hệ số chiết khấu (discount factor). Ví dụ 02.9 là trường hợp $\gamma=0{,}5$ của Bước 3; bộ $(1;\ 0{,}5;\ 0{,}5)$ vi phạm Bước 2 với $j=2$, vì $w_3=0{,}5\ne w_2^2=0{,}25$.

Các giả thiết của định lý có vai trò khác nhau.

- **Dạng cộng là cần.** Đặt $W(\varnothing)=0$ và $W([r,\sigma])=r+W(\sigma)^3$. Vì hàm lập phương tăng ngặt, thứ tự theo $W$ là ưu tiên dừng; nhưng $W((0,y))=W((y))^3=y^3$ không bằng $w_2y$ với một hằng số $w_2$ cho mọi $y$, nên $W$ không có dạng (4.1).
- **Dùng chung trọng số cho mọi độ dài là cần.** Với $\gamma\in(0,1]$ và $0<b<1$, đặt $w^{(1)}=(b)$ và $w^{(n)}=(1,\gamma,\dots,\gamma^{n-2},b\gamma^{n-1})$ cho chuỗi độ dài $n\ge2$. Tính trực tiếp cho $U([r,\sigma])=r+\gamma U(\sigma)$ với mọi $\sigma$, nên thứ tự là ưu tiên dừng, nhưng trọng số của vị trí cuối phụ thuộc độ dài và không có dạng (4.3); điều kiện $w_1=1$ khi đó chỉ đúng với độ dài $n\ge2$.
- **Không tăng chỉ dùng để có $\gamma\le1$.** Trọng số $w_i=2^{i-1}$ thỏa (4.2) theo đúng Bước 3; bỏ giả thiết này, kết luận còn $\gamma>0$.
- **Tính dương có thể bỏ.** Không có nó, Bước 1–2 vẫn cho $w_i=\gamma^{i-1}$ với $\gamma=w_2$; từ $w_3\le w_2$ có $\gamma^2\le\gamma$, tức $0\le\gamma\le1$. Trường hợp $\gamma=0$, trọng số $(1,0,0,\dots)$, không cho ưu tiên dừng: $(2,0)\succ(1,1)$ nhưng sau khi thêm $r$ cả hai có lợi ích $r$. Vậy vẫn có $\gamma>0$.

Bước 1 dùng dạng cộng và việc dùng chung trọng số; Bước 2 dùng $w_1=1$, tính dương (cho $\gamma>0$, thay được bằng lập luận ở gạch cuối) và tính không tăng (cho $\gamma\le1$); Bước 3 chỉ dùng $\gamma>0$. Định lý cũng giải thích vì sao Bài 01 dùng được tổng không chiết khấu: đó là trường hợp $\gamma=1$ của cùng một họ.

**Trong thực hành.** Các bài thực hành CartPole (Bài 04), Lunar Lander (Bài 05–06) và Flappy Bird (Bài 07) đều dùng một hệ số $\gamma=0{,}99$ cho mọi bước, tức trọng số hình học của (4.3). Trọng số giảm theo cấp số nhân: $0{,}99^{100}\approx0{,}37$, và với bước dài $0{,}02$ giây của Lunar Lander, phần thưởng nhận sau $2$ giây mô phỏng chỉ còn trọng số khoảng $0{,}37$. Định lý 02.11 chỉ nói về thứ tự trên chuỗi tất định; việc một chính sách không đổi theo thời gian là đủ tốt còn cần tính Markov và không có hạn chót (Nhận xét 02.15, Bài 03–04).

<!-- note-topic-id: lec-02-topic-08 -->
### 4.2 Lợi tức chiết khấu

Lợi tức sẽ là lợi ích cộng của Định lý 02.11 áp vào chuỗi phần thưởng sau một thời điểm $t$, với chỉ số thời gian của Định nghĩa 02.1; ví dụ sau tính nó trên ba bước cuối của mê cung.

::: example Ví dụ 02.10 (Ba bước cuối của đường 16 bước)
**Dữ kiện.** Trên đường 16 bước của Ví dụ 02.1, tại $t=13$ tác tử ở $(6,5)$. Ba bước còn lại là $(6,5)\to(6,6)\to(7,6)\to\mathrm G$, mỗi bước $-1$, nên $R_{14}=R_{15}=R_{16}=-1$ và $T=16$.

**Với $\gamma=0{,}5$.** $G_{13}=(-1)\cdot1+(-1)\cdot0{,}5+(-1)\cdot0{,}25=-1{,}75$.

**Với $\gamma=1$.** $G_{13}=-3$, bằng âm số bước còn lại.

**Kiểm tra lại.** Tính ngược với $\gamma=0{,}5$: $G_{16}=0$, $G_{15}=-1$, $G_{14}=-1+0{,}5\cdot(-1)=-1{,}5$, $G_{13}=-1+0{,}5\cdot(-1{,}5)=-1{,}75$.
:::

::: definition Định nghĩa 02.12 (Lợi tức)
Cho hệ số chiết khấu $\gamma\in[0,1]$. Với lượt kết thúc tại $T<\infty$ và $t<T$, **lợi tức** từ $t$ là
$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1},\qquad G_T=0 .
\tag{4.5}
$$
Với nhiệm vụ tiếp diễn ($T=\infty$), đòi hỏi thêm $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$ với mọi $t$, và
$$
G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}.
\tag{4.6}
$$
:::

Số hạng đầu của (4.5) là $R_{t+1}$, phần thưởng của $A_t$; trọng số của phần thưởng thứ $k+1$ sau $t$ là $\gamma^k$, đúng dạng (4.3). Quy ước $G_T=0$ nói rằng sau khi kết thúc không còn phần thưởng; $R_T$ đã nằm trong $G_{T-1}$. Sutton và Barto (2018, §3.4, trang 57) hợp nhất hai trường hợp bằng cách coi trạng thái kết thúc là trạng thái hấp thụ, chỉ chuyển về chính nó với phần thưởng $0$.

Với $\gamma=1$, (4.5) là lợi tức của Định nghĩa 01.8. Với $\gamma=0$, $G_t=R_{t+1}$ và tác tử được gọi là cận thị (myopic) (Sutton và Barto, 2018, §3.3, trang 55). Với $\gamma$ gần $1$, phần thưởng xa được tính gần ngang phần thưởng gần. Khi $\gamma<1$, tổng mọi trọng số là $\sum_{k\ge0}\gamma^k=1/(1-\gamma)$, bằng tổng trọng số của $1/(1-\gamma)$ bước không chiết khấu; số này đo chân trời hiệu dụng (effective horizon) của tiêu chí. Với $\gamma=0{,}99$, chân trời hiệu dụng là $100$ bước, và trọng số của phần thưởng thứ $101$ sau $t$ là $0{,}99^{100}\approx0{,}37$; phần thưởng xa hơn vẫn được tính, với trọng số nhỏ dần. Khi $\gamma=1$ và một quỹ đạo không kết thúc, ta quy ước lợi tức của nó là giới hạn của tổng riêng khi giới hạn tồn tại, có thể bằng $\pm\infty$; quy ước này dùng ở Mục 5 và ở các tình huống cuối chương.

Nhầm lẫn thường gặp là coi $G_t$ là một con số gắn với trạng thái $S_t$; $G_t$ là biến ngẫu nhiên phụ thuộc toàn bộ phần còn lại của lượt.

::: proposition Mệnh đề 02.13 (Hệ thức truy hồi và chặn của lợi tức)
**Giả thiết.** $G_t$ theo Định nghĩa 02.12.

**Kết luận.**

- (a) Với mọi $t<T$, $G_t=R_{t+1}+\gamma G_{t+1}$, với $G_T=0$ khi $T<\infty$.
- (b) Nếu $\gamma<1$ và $\lvert R_{t+1}\rvert\le R_{\max}$ với mọi $t$, chuỗi (4.6) hội tụ tuyệt đối và
$$
\lvert G_t\rvert\le\frac{R_{\max}}{1-\gamma}.
\tag{4.7}
$$
- (c) Nếu $T<\infty$ và $\lvert R_{t+1}\rvert\le R_{\max}$ thì $\lvert G_t\rvert\le R_{\max}(1-\gamma^{T-t})/(1-\gamma)$ khi $\gamma<1$ và $\lvert G_t\rvert\le R_{\max}(T-t)$ khi $\gamma=1$.

**Điều kiện áp dụng.** Phần (a) cho nhiệm vụ tiếp diễn cần chuỗi hội tụ, điều mà phần (b) bảo đảm.

**Phạm vi.** Chặn (4.7) đạt được khi phần thưởng luôn bằng $R_{\max}$. Với $\gamma=1$ và nhiệm vụ tiếp diễn không có chặn hữu hạn. Mệnh đề 03.11 của ghi chú Bài 03 phát biểu chặn này cho MDP.
:::

::: proof Chứng minh Mệnh đề 02.13
**Bước 1 (truy hồi khi lượt kết thúc).** Với $t<T<\infty$,
$$
\begin{aligned}
G_t&=R_{t+1}+\sum_{k=1}^{T-t-1}\gamma^kR_{t+k+1}
&&\text{((4.5), tách số hạng }k=0)\\
&=R_{t+1}+\gamma\sum_{j=0}^{T-(t+1)-1}\gamma^{j}R_{(t+1)+j+1}
&&(\text{đổi chỉ số }j=k-1)\\
&=R_{t+1}+\gamma G_{t+1}
&&\text{((4.5) tại }t+1).
\end{aligned}
$$
Khi $t=T-1$, tổng sau khi tách là tổng rỗng, bằng $0=\gamma G_T$.

**Bước 2 (hội tụ và chặn).** Với $\gamma<1$, mỗi số hạng thỏa $\lvert\gamma^kR_{t+k+1}\rvert\le R_{\max}\gamma^k$, và $\sum_kR_{\max}\gamma^k$ hữu hạn, nên (4.6) hội tụ tuyệt đối và
$$
\begin{aligned}
\lvert G_t\rvert&\le\sum_{k=0}^{\infty}\gamma^k\lvert R_{t+k+1}\rvert
&&\text{(bất đẳng thức tam giác)}\\
&\le R_{\max}\sum_{k=0}^{\infty}\gamma^k
&&(\lvert R_{t+k+1}\rvert\le R_{\max})\\
&=\frac{R_{\max}}{1-\gamma}
&&\text{(tổng hình học)}.
\end{aligned}
$$
Cùng lập luận trên tổng hữu hạn $T-t$ số hạng cho phần (c).

**Bước 3 (truy hồi khi tiếp diễn).** Khi (4.6) hội tụ tuyệt đối, được tách số hạng đầu và đặt $\gamma$ ra ngoài phần còn lại như ở Bước 1. $\square$
:::

Phần (a) nói lợi tức bằng phần thưởng kế tiếp cộng lợi tức từ bước sau, chiết khấu một lần; nó mở rộng Mệnh đề 01.9 và là bước đầu của phương trình Bellman ở Bài 03. Phần (b) giải thích yêu cầu $\gamma<1$ cho nhiệm vụ tiếp diễn.

**Trong thực hành.** CartPole (Bài 04) trả $+1$ mỗi bước và dùng $\gamma=0{,}99$, nên theo (4.7) mọi lợi tức không vượt $1/(1-0{,}99)=100$. Lunar Lander (Bài 05–06) cắt lượt ở bước $1\,000$; phần lợi tức bị bỏ sau điểm cắt là $\gamma^{1000-t}G_{1000}$, nhỏ khi $t$ còn xa điểm cắt. Vì vậy, trong notebook Bài 05, các lượt bị cắt bị loại khỏi ước lượng Monte Carlo thay vì coi phần thiếu bằng $0$.

<!-- note-topic-id: lec-02-topic-09 -->
### 4.3 Từ lợi tức của một lượt đến kỳ vọng

Khi chính sách ngẫu nhiên (Ví dụ 02.8) hoặc môi trường ngẫu nhiên, cùng một ô xuất phát cho nhiều quỹ đạo, và $G_t$ là biến ngẫu nhiên. Bài giảng gốc (trang 22) đặt câu hỏi vì sao định nghĩa giá trị cần kỳ vọng; ví dụ sau trả lời trên một môi trường nhỏ.

::: example Ví dụ 02.11 (Môi trường hai nhánh)
**Dữ kiện.** Từ trạng thái $s$, dưới một chính sách cố định, môi trường chọn ngẫu nhiên một trong hai nhánh, mỗi nhánh với xác suất $0{,}5$: nhánh ngắn kết thúc sau $3$ bước, nhánh dài sau $5$ bước. Mỗi bước nhận $-1$; $\gamma=1$. Đây là môi trường giả định, khác mê cung tất định.

**Tính.** Hai lợi tức là $-3$ và $-5$, nên $\mathbb E[G_t\mid S_t=s]=0{,}5\cdot(-3)+0{,}5\cdot(-5)=-4$.

**Đọc kết quả.** Không lượt nào cho đúng $-4$; con số này đại diện cho trạng thái $s$, không cho một lượt.

**Kiểm tra lại.** $-4$ nằm giữa $-5$ và $-3$, bằng trung bình cộng của chúng vì hai xác suất bằng nhau.
:::

Lợi tức của một lượt thay đổi giữa các lượt, nên không dùng làm số đo của trạng thái được. Tác tử cũng không chọn được nhánh: sự ngẫu nhiên nằm ở môi trường, nên số đo của trạng thái phải lấy trung bình trên những gì môi trường có thể làm, đúng như giả thuyết phần thưởng.

<!-- note-topic-id: lec-02-topic-10 -->
### 4.4 Hàm giá trị trạng thái

Về mặt ý tưởng, giá trị của một trạng thái là con số $-4$ của Ví dụ 02.11 được định nghĩa cho mọi trạng thái và mọi chính sách; đây chưa phải định nghĩa.

::: definition Định nghĩa 02.14 (Hàm giá trị trạng thái)
**Giả thiết.** Môi trường được quan sát đầy đủ và $X_t=S_t$; trạng thái có tính Markov (Định nghĩa 02.5) và môi trường dừng, tức xác suất ở vế phải của (2.3) không phụ thuộc $t$; $\pi(a\mid s)$ là chính sách dừng trên $\mathcal S$ (Định nghĩa 02.8); với $\gamma$ đã chọn, $\mathbb E_\pi\bigl[\lvert G_0\rvert\mid S_0=s\bigr]<\infty$ với mọi $s\in\mathcal S$.

**Định nghĩa.** Xét lượt xuất phát tại $S_0=s$. **Hàm giá trị trạng thái** (state-value function) của $\pi$ là
$$
v_\pi(s)=\mathbb E_\pi\bigl[G_0\mid S_0=s\bigr],\qquad s\in\mathcal S,
\tag{4.8}
$$
và $v_\pi(s)=0$ khi $s$ là trạng thái kết thúc. $\mathbb E_\pi$ là kỳ vọng khi các hành động được chọn theo $\pi$ và các cặp $(S_{k+1},R_{k+1})$ sinh theo động lực của môi trường.
:::

Vế phải của (4.8) có ba thành phần: $G_0$ đo cả chuỗi phần thưởng của lượt, điều kiện $S_0=s$ cố định điểm xuất phát, $\mathbb E_\pi$ lấy trung bình trên chính sách và môi trường. Quy ước xuất phát tại $s$ cho giá trị ở mọi trạng thái chưa kết thúc, kể cả trạng thái mà chính sách không bao giờ ghé khi lượt bắt đầu ở ô khác, như ngõ cụt $(4,2)$ của mê cung (Ví dụ 02.12). Ba giả thiết đầu cho thêm một tính chất: với mọi phân phối xuất phát (cùng các xác suất chuyển của môi trường) và mọi $t$ có $\Pr(S_t=s)>0$, $\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s)$. Lý do: theo quy tắc nhân, phân phối có điều kiện của $(A_t,R_{t+1},S_{t+1},A_{t+1},\dots)$ khi biết $H_t=h$ là tích các thừa số $\pi(\cdot\mid\cdot)$ và các xác suất ở vế phải của (2.3); nhờ tính Markov, tính dừng của môi trường và của chính sách, phân phối đó chỉ phụ thuộc trạng thái cuối $s$ của $h$ mà không phụ thuộc $t$, nên trùng phân phối của $(A_0,R_1,S_1,A_1,\dots)$ khi xuất phát tại $s$. Giả thiết thứ tư bảo đảm cả hai vế là số thực. Ví dụ 02.11 cho $v_\pi(s)=-4$.

Định nghĩa liên hệ với giá trị trên lịch sử $v_\pi(h)$ (Định nghĩa 01.12), với $\gamma=1$; khi $\gamma<1$, thay $G_t$ trong (4.1) của Bài 01 bằng lợi tức chiết khấu: dưới tính Markov và tính dừng, với chính sách trên trạng thái, $v_\pi(h)$ của mọi lịch sử khả hữu $h$ chỉ phụ thuộc trạng thái cuối $s$ của $h$ và bằng $v_\pi(s)$, còn $v_\pi(s)$ xác định cả ở trạng thái mà không lịch sử khả hữu nào đi tới. Lợi tức thuộc một lượt, còn giá trị thuộc một trạng thái và một chính sách; đánh giá theo (4.8) chưa phải là chọn chính sách tốt nhất.

::: remark Nhận xét 02.15 (Kỳ vọng hữu hạn và hạn chót)
- Với $\gamma<1$ và phần thưởng bị chặn, kỳ vọng hữu hạn theo (4.7).
- Với $\gamma=1$, phần thưởng bị chặn và $\mathbb E_\pi[T\mid S_0=s]<\infty$ đủ để kỳ vọng hữu hạn, theo Mệnh đề 02.13(c). Kết thúc với xác suất $1$ chưa đủ: nếu trạng thái $n$ bằng số bước đã đi cộng $1$, xuất phát tại $n=1$, và từ $n$ lượt kết thúc với xác suất $1/(n+1)$, mỗi bước nhận $-1$, thì $\Pr(T>k\mid S_0=1)=\prod_{n=1}^{k}\frac{n}{n+1}=\frac1{k+1}\to0$ nhưng $\mathbb E[T\mid S_0=1]=\sum_{k\ge0}\frac1{k+1}=\infty$. Phản ví dụ cần vô hạn trạng thái: với hữu hạn trạng thái, môi trường Markov và dừng, chính sách dừng, nếu từ mọi trạng thái đạt được lượt kết thúc với xác suất $1$, thì mỗi trạng thái $s$ có $N_s$ bước với xác suất kết thúc dương; lấy $N=\max_sN_s$ và $\varepsilon$ là nhỏ nhất của các xác suất đó, ta có $N$ và $\varepsilon>0$ để từ mọi trạng thái lượt kết thúc trong $N$ bước với xác suất ít nhất $\varepsilon$, nên $\Pr(T-t>kN)\le(1-\varepsilon)^k$.
- Nếu lượt bị cắt ở một hạn chót cố định, hành động tốt ở cùng một ô có thể phụ thuộc thời gian còn lại; Russell và Norvig (2020, §17.1.1, trang 565) gọi chính sách khi đó là không dừng. Muốn dùng (4.8), cần đưa thời gian còn lại vào trạng thái.
:::

::: example Ví dụ 02.12 (Giá trị của chính sách trên mê cung $8\times8$)
**Dữ kiện.** Mê cung $8\times8$, chính sách xác định của hình ở Mục 3, luật chuyển tất định, $-1$ mỗi bước kể cả bước vào $\mathrm G$, $\gamma=1$, $v_\pi(\mathrm G)=0$.

**Tính.** Theo Định nghĩa 02.14, $v_\pi(s)$ tính trên lượt xuất phát tại $s$. Chính sách và môi trường đều tất định, nên từ mỗi ô xuất phát có đúng một quỹ đạo và $v_\pi(s)$ bằng âm số bước tới $\mathrm G$ theo mũi tên: $v_\pi((0,2))=-16$, $v_\pi((7,6))=-1$. Từ ngõ cụt $(4,2)$, mũi tên Bắc về $(4,1)$ rồi 11 bước nữa, nên $v_\pi((4,2))=-12$. Từ $(1,5)$, mũi tên dẫn qua $(1,6)$, $(2,6)$, $(3,6)$, $(3,5)$, $(3,4)$, $(2,4)$, $(2,3)$, $(1,3)$ về $(1,2)$ rồi theo đường chính, nên $v_\pi((1,5))=-24$. Lượt xuất phát tại $(0,2)$ không ghé $(4,2)$ hay $(1,5)$; hai giá trị này có nghĩa nhờ quy ước xuất phát tại $s$.

**Kiểm tra lại.** Mỗi ô $s\ne\mathrm G$ thỏa $v_\pi(s)=-1+v_\pi(s')$ với $s'$ là ô mũi tên chỉ tới, chẳng hạn $-1+(-11)=-12$ tại $(4,2)$; đây là Mệnh đề 02.13(a) với $\gamma=1$.
:::

![Mê cung tám hàng tám cột, mỗi ô đi được ghi giá trị của chính sách ở Mục 3, với gamma bằng 1 và thưởng âm một mỗi bước. Dọc đường chính: (0,2) là −16, (1,2) là −15, (1,1) là −14, hàng 1 từ (2,1) tới (6,1) lần lượt −13, −12, −11, −10, −9; (6,2) là −8, (6,3) là −7, (5,3) là −6, (5,4) là −5, (5,5) là −4, (6,5) là −3, (6,6) là −2, (7,6) là −1. Ngoài đường chính: (4,2) là −12; (1,3) là −16, (2,3) là −17, (2,4) là −18, (3,4) là −19, (3,5) là −20, (3,6) là −21, (2,6) là −22, (4,6) là −22, (1,6) là −23, (1,5) là −24.](img/lec-02/source-values.svg)

Bảng giá trị của bài giảng gốc (trang 26) là Ví dụ 02.12 cho mọi ô: dọc đường chính, giá trị tăng $1$ sau mỗi bước, từ $-16$ tới $-1$; ở nhánh dưới, các ô từ $(2,3)$ trở đi có giá trị nhỏ hơn $-16$, vì phải vòng qua cả nhánh để về đường chính. Tại $(4,1)$, bước Đông cho $-1+v_\pi((5,1))=-11$, bước Nam cho $-1+v_\pi((4,2))=-13$; ở Bài 03, đại lượng này được gọi là giá trị hành động.

**Trong thực hành.** Ở bài thực hành Bài 05, $v_\pi$ trên Lunar Lander được ước lượng bằng một bảng $V(s)$ theo ô của quan sát đã chia, cập nhật từ các lợi tức quan sát được. Giả thiết Markov của Định nghĩa 02.14 không thỏa trên ô gộp; trong notebook, Monte Carlo và sai phân thời gian (temporal difference, TD) theo lô cho hai nghiệm khác nhau trên cùng dữ liệu, và ô gộp không Markov là một nguyên nhân có thể của khác biệt đó.

<!-- note-topic-id: lec-02-topic-11 -->
### 4.5 Hàm động lực

Hàm giá trị trả lời "từ đây, theo chính sách này, kết quả dài hạn trung bình là bao nhiêu". Một cách trực quan, câu hỏi "từ đây, chọn hành động này thì bước kế tiếp ra sao" không phụ thuộc chính sách, và trả lời nó là dự báo động lực của môi trường.

::: example Ví dụ 02.13 (Động lực một bước của mê cung)
**Dữ kiện.** Mê cung $8\times8$, luật chuyển tất định, $-1$ mỗi bước.

**Hai cặp (ô, hướng).** Bước Đông từ $(0,2)$ cho cặp (trạng thái kế tiếp, phần thưởng) $((1,2),-1)$ với xác suất $1$. Bước Đông từ $(7,6)$ cho $(\mathrm G,-1)$ với xác suất $1$; $\mathrm G$ là trạng thái kết thúc.

**Kiểm tra lại.** Với mỗi cặp (ô, hướng), đúng một cặp kết quả có xác suất $1$, nên tổng xác suất bằng $1$.
:::

::: definition Định nghĩa 02.16 (Hàm động lực)
**Giả thiết.** $\mathcal S^+$ và $\mathcal R$ đếm được; trạng thái có tính Markov và môi trường dừng.

**Định nghĩa.** **Hàm động lực** (dynamics function) của môi trường là
$$
p(s',r\mid s,a)=\Pr\bigl(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a\bigr),
\tag{4.9}
$$
xác định với $s\in\mathcal S$ chưa kết thúc, $a\in\mathcal A(s)$, $s'\in\mathcal S^+$, $r\in\mathcal R$, và thỏa $p(s',r\mid s,a)\ge0$, $\sum_{s'}\sum_{r}p(s',r\mid s,a)=1$ với mọi $s,a$.
:::

Công thức (4.9) cho xác suất đồng thời của trạng thái kế tiếp và phần thưởng khi biết trạng thái và hành động hiện tại. Vế phải không chứa $t$ và lịch sử nhờ tính dừng và tính Markov; với trạng thái là tọa độ trong Ví dụ 02.6, vế phải không xác định được từ $s$ và $a$. Tổng bằng $1$ lấy trên cặp $(s',r)$, không riêng trên $s'$. Ví dụ 02.13 là trường hợp $p((1,2),-1\mid(0,2),\text{Đông})=1$. Từ $p$ suy ra xác suất chuyển $p(s'\mid s,a)=\sum_rp(s',r\mid s,a)$ và thưởng kỳ vọng một bước $r(s,a)=\sum_{s'}\sum_rr\,p(s',r\mid s,a)$; Mệnh đề 03.6 của ghi chú Bài 03 chứng minh hai đẳng thức này.

Hàm động lực là mô hình đúng của môi trường. Mô hình theo nghĩa của Định nghĩa 01.14, thứ tác tử mang theo để lập kế hoạch, nói chung là một xấp xỉ $\hat p$ của $p$ (trùng $p$ khi người thiết kế cung cấp đúng), và có thể sai. Hàm động lực khác hàm giá trị ở chỗ nó dự báo một bước và không phụ thuộc chính sách. Kết luận này dành cho chính sách chỉ dùng trạng thái, tức $X_t=S_t$, và có hai bước. Thứ nhất, trong tỉ số $\Pr(H_t=h,A_t=a,S_{t+1}=s',R_{t+1}=r)/\Pr(H_t=h,A_t=a)$, các thừa số $\pi(a_k\mid s_k)$, $k\le t$, chỉ phụ thuộc $h$ và $a$ nên triệt tiêu, do đó vế trái của (2.3) do môi trường quyết định. Thứ hai, chính sách chọn đều các hành động hợp lệ đặt xác suất dương lên mọi lịch sử khả hữu; áp (2.3) cho chính sách này, vế trái nhận cùng một giá trị trên mọi $h$ kết thúc tại $s$, nên $p$ như nhau với mọi chính sách trên trạng thái. Nếu chính sách dùng thêm thông tin ngoài trạng thái, kết luận có thể sai: với cấu hình $(s,z)$, $z$ là một bit ngẫu nhiên tác tử quan sát được và phần thưởng $z\cdot a$ với $a\in\{0,1\}$, xác suất nhận thưởng $1$ khi chọn $a=1$ là $0{,}5$ dưới chính sách chọn đều nhưng bằng $1$ dưới chính sách chọn $1$ đúng khi $z=1$. Chữ $p$ thường theo Sutton và Barto (2018, §3.1, trang 48–49) và Bài 03; giáo trình *Học máy thống kê* viết $p(s'\mid s,a)$ là $T(s,a,s')$.

**Trong thực hành.** Quy hoạch động ở Bài 04 cần $p$. Trên CartPole, phép chia ô không cung cấp $p$, nên trong notebook Bài 04, $\hat p(s'\mid s,a)$ và $\hat r(s,a)$ được ước lượng bằng cách đặt bộ mô phỏng vào nhiều trạng thái liên tục trong mỗi ô; kết quả chịu cả sai số ước lượng lẫn sai số do gộp ô. Monte Carlo và sai phân thời gian ở Bài 05–06 là phương pháp phi mô hình: chúng chỉ dùng các mẫu chuyển mà không xây dựng $\hat p$.

::: remark Nhận xét 02.17 (Dự đoán và điều khiển)
Bài giảng gốc (trang 24) phân biệt hai bài toán. **Dự đoán** (prediction) là đánh giá một chính sách cố định, tức tính hoặc ước lượng $v_\pi$, như Ví dụ 02.12. **Điều khiển** (control) là tìm hoặc cải thiện chính sách; so sánh $-11$ với $-13$ tại $(4,1)$ rồi đổi mũi tên theo hành động tốt hơn là một bước điều khiển. Biết $p$ chưa đồng nghĩa với biết chính sách tốt nhất; vẫn phải giải bài toán chọn trên $p$, nội dung của Bài 04.
:::

::: exercise Bài tập 02.5 (Lợi tức chiết khấu và hệ thức truy hồi)
Một lượt kết thúc tại $T=4$ với $R_1=2$, $R_2=0$, $R_3=-1$, $R_4=4$.

- (a) Với $\gamma=0{,}5$, tính $G_3$, $G_2$, $G_1$, $G_0$ bằng Mệnh đề 02.13(a), rồi kiểm tra $G_0$ bằng (4.5).
- (b) Với $\gamma=0{,}5$, thêm phần thưởng $r=-3$ vào đầu chuỗi. Dùng Bước 3 của Định lý 02.11, tính lợi tức của chuỗi mới mà không cộng lại từ đầu.
- (c) Tính $G_0$ với $\gamma=0$ và $\gamma=1$.
:::

::: hint
Bắt đầu từ $G_4=0$. Ở câu (b), $U([r,\sigma])=r+\gamma U(\sigma)$.
:::

::: solution
**Câu (a).** $G_3=4$; $G_2=-1+0{,}5\cdot4=1$; $G_1=0+0{,}5\cdot1=0{,}5$; $G_0=2+0{,}5\cdot0{,}5=2{,}25$. Theo (4.5): $2+0+0{,}25\cdot(-1)+0{,}125\cdot4=2{,}25$.

**Câu (b).** $-3+0{,}5\cdot2{,}25=-1{,}875$.

**Câu (c).** $\gamma=0$: $G_0=R_1=2$. $\gamma=1$: $G_0=2+0-1+4=5$.

**Kiểm tra lại.** Câu (b) cộng trực tiếp: $-3+0{,}5\cdot2+0+0{,}125\cdot(-1)+0{,}0625\cdot4=-1{,}875$.
:::

::: exercise Bài tập 02.6 (Giá trị của môi trường hai nhánh)
Từ trạng thái $s$, dưới một chính sách cố định, môi trường chọn nhánh ngắn kết thúc sau $3$ bước với xác suất $q$ và nhánh dài kết thúc sau $5$ bước với xác suất $1-q$; mỗi bước nhận $-1$.

- (a) Với $q=0{,}5$ và $\gamma=0{,}5$, tính lợi tức của từng nhánh và $v_\pi(s)$.
- (b) Với $\gamma=1$, viết $v_\pi(s)$ theo $q$ và tìm $q$ để $v_\pi(s)=-4{,}5$.
:::

::: hint
Lợi tức của $n$ bước $-1$ là $-(1-\gamma^n)/(1-\gamma)$ khi $\gamma<1$.
:::

::: solution
**Câu (a).** Nhánh ngắn: $-(1+0{,}5+0{,}25)=-1{,}75$. Nhánh dài: $-(1+0{,}5+0{,}25+0{,}125+0{,}0625)=-1{,}9375$. Do đó $v_\pi(s)=0{,}5\cdot(-1{,}75)+0{,}5\cdot(-1{,}9375)=-1{,}84375$.

**Câu (b).** $v_\pi(s)=-3q-5(1-q)=-5+2q$; giải $-5+2q=-4{,}5$ cho $q=0{,}25$.

**Kiểm tra lại.** Công thức gợi ý cho $-(1-0{,}5^3)/0{,}5=-1{,}75$ và $-(1-0{,}5^5)/0{,}5=-1{,}9375$.
:::

::: exercise Bài tập 02.7 (Hàm động lực của bước trượt)
Biến thể trơn của mê cung $8\times8$: tại $(0,2)$, bước Đông đưa tác tử tới $(1,2)$ với xác suất $0{,}8$ và giữ tác tử tại $(0,2)$ với xác suất $0{,}2$; mọi bước nhận $-1$. Viết $p(s',r\mid(0,2),\text{Đông})$ cho mọi cặp có xác suất dương, rồi tính $p(s'\mid(0,2),\text{Đông})$ và $r((0,2),\text{Đông})$.
:::

::: hint
Dùng (4.9) và hai công thức suy ra sau Định nghĩa 02.16.
:::

::: solution
$p((1,2),-1\mid(0,2),\text{Đông})=0{,}8$ và $p((0,2),-1\mid(0,2),\text{Đông})=0{,}2$. Do đó $p((1,2)\mid\cdot)=0{,}8$, $p((0,2)\mid\cdot)=0{,}2$, và $r((0,2),\text{Đông})=-1\cdot0{,}8+(-1)\cdot0{,}2=-1$.

**Kiểm tra lại.** $0{,}8+0{,}2=1$, đúng điều kiện tổng của Định nghĩa 02.16.
:::

Như vậy, chúng ta đã chứng minh rằng ưu tiên dừng buộc trọng số hình học (Định lý 02.11), định nghĩa lợi tức (Định nghĩa 02.12) với hệ thức truy hồi và chặn (Mệnh đề 02.13), lấy kỳ vọng của lợi tức dưới một chính sách cố định để được hàm giá trị trạng thái (Định nghĩa 02.14), và tách dự báo một bước thành hàm động lực (Định nghĩa 02.16). Mọi phép tính trong mục dùng phần thưởng cho sẵn, $-1$ mỗi bước; chưa có kết quả nào cho biết tác tử tối ưu sẽ làm gì khi người thiết kế đổi phần thưởng. Trong Mục 5, chúng ta tìm mức chi phí mỗi bước làm hành vi tối ưu đổi từ đích sang hố.

<!-- note-topic-id: lec-02-part-06 -->
## 5. Thiết kế phần thưởng

Trên mê cung $8\times8$, phần thưởng $-1$ mỗi bước làm cực đại lợi tức trùng với tới đích nhanh nhất (Ví dụ 02.3); sự trùng khớp đó do người thiết kế tạo ra. Giả sử trên đường tới đích có một hố, rơi vào hố cũng kết thúc lượt, và người thiết kế thưởng thêm khi tới đích, phạt mỗi bước để tác tử không đi lòng vòng. Với mức phạt mỗi bước nào thì tác tử tối ưu vẫn tới đích? Chúng ta trả lời bằng lợi tức với $\gamma=1$, áp cho mọi đường kết thúc.

<!-- note-topic-id: lec-02-topic-12 -->
### 5.1 Mê cung đích–hố

Về mặt ý tưởng, mỗi điểm kết thúc là một "gói" gồm phần thưởng khi tới đó và tổng chi phí của đường đi tới đó; tác tử tối ưu chọn gói có lợi tức lớn nhất, nên thay đổi chi phí có thể đổi gói được chọn. Đây chưa phải phát biểu chính xác.

::: example Ví dụ 02.14 (Mê cung đích–hố)
**Dữ kiện.** Một hành lang khép kín gồm mười nút. Hàng trên có năm nút từ trái sang phải: xuất phát $\mathrm S$, một nút trống, hố $\mathrm H$, một nút trống, đích $\mathrm G$. Hàng dưới có năm nút trống; nút đầu trái nối với $\mathrm S$, nút đầu phải nối với $\mathrm G$. Mỗi đoạn nối hai nút kề nhau là một bước. Tại mỗi nút chưa kết thúc, tác tử đi sang một nút kề, có thể quay lại; chuyển là tất định. $\mathrm H$ và $\mathrm G$ là trạng thái kết thúc.

**Phần thưởng.** Mỗi bước nhận $-c$ với $c\ge0$, kể cả bước cuối; bước vào $\mathrm G$ nhận thêm $+10$; bước vào $\mathrm H$ không nhận thêm. $\gamma=1$.

**Hai đường ngắn nhất.** Từ $\mathrm S$ đi hàng trên, sau $2$ bước tác tử rơi vào $\mathrm H$. Từ $\mathrm S$ xuống hàng dưới, qua năm nút rồi lên $\mathrm G$: $1+4+1=6$ bước.

**Kiểm tra lại.** Nút trống giữa $\mathrm H$ và $\mathrm G$ chỉ nối với hai trạng thái kết thúc, nên từ $\mathrm S$ không bao giờ tới được; mọi đường tới $\mathrm G$ đều đi hàng dưới.
:::

![Hành lang khép kín hình chữ nhật. Hàng trên từ trái sang phải: S, một nút trống, hố H đánh dấu chéo, một nút trống, đích G ghi Đích +10. Hàng dưới có năm nút trống, nối với S ở đầu trái và với G ở đầu phải. Đoạn từ S tới H được tô nét đứt, ghi 2 bước tới H; vòng dưới ghi 6 bước tới G. Chú thích: mỗi đoạn nối hai nút là một bước; đến H hoặc G thì kết thúc.](img/lec-02/incentive-maze.svg)

Đường nét đứt hàng trên dài $2$ bước tới $\mathrm H$, vòng hàng dưới dài $6$ bước tới $\mathrm G$; khoảng cách vẽ trên hình không biểu thị số bước. Hố nằm trên đường ngắn tới đích, nên muốn tới đích tác tử phải đi vòng.

::: example Ví dụ 02.15 (Lợi tức của hai đường)
**Dữ kiện.** Mê cung đích–hố: đường ngắn nhất tới $\mathrm G$ dài $6$ bước, tới $\mathrm H$ dài $2$ bước; $-c$ mỗi bước, thêm $+10$ khi vào $\mathrm G$; $\gamma=1$.

**Hai lợi tức.** Đường tới đích có năm bước $-c$ và bước cuối $10-c$; đường vào hố có hai bước $-c$:
$$
G_{\text{đích}}=5\cdot(-c)+(10-c)=10-6c,\qquad G_{\text{hố}}=-2c .
$$

**Ba mức chi phí.**

| $c$ | Đích: $10-6c$ | Hố: $-2c$ | Đường có lợi tức lớn hơn |
|---|---|---|---|
| $0$ | $10$ | $0$ | đích |
| $1$ | $4$ | $-2$ | đích |
| $3$ | $-8$ | $-6$ | hố |

**Đọc kết quả.** Với $c=3$, đường tới đích vẫn nhận thêm $10$ nhưng chịu tổng chi phí $18$, còn đường vào hố chỉ chịu $6$; tác tử cực đại lợi tức chọn hố, trái với ý định của người thiết kế.

**Kiểm tra lại.** Với $c=0$, hai lợi tức là $10$ và $0$, đúng phần thưởng thêm khi kết thúc.
:::

Chỉ số dưới của $G_{\text{đích}}$ và $G_{\text{hố}}$ là tên đường, không phải thời điểm; cả hai là lợi tức $G_0$ từ $\mathrm S$.

### 5.2 Ngưỡng đổi hành vi

Ví dụ 02.15 chỉ so sánh hai đường ngắn nhất, trong khi tác tử có thể đi vòng trước khi kết thúc hoặc không bao giờ kết thúc. Mệnh đề sau xét mọi khả năng đó và thêm mức phạt riêng $c_{\mathrm H}\ge0$ khi vào hố.

::: proposition Mệnh đề 02.18 (Ngưỡng đổi hành vi)
**Giả thiết.** Mê cung đích–hố của Ví dụ 02.14, với bước vào $\mathrm H$ nhận thêm $-c_{\mathrm H}$, $c_{\mathrm H}\ge0$; chi phí mỗi bước $c\ge0$; $\gamma=1$; chuyển tất định. Tác tử tối ưu chọn chính sách cực đại lợi tức kỳ vọng từ $\mathrm S$; lợi tức của quỹ đạo không kết thúc là giới hạn của tổng riêng.

**Kết luận.** Lợi tức kỳ vọng lớn nhất từ $\mathrm S$ là $M=\max\{10-6c,\ -2c-c_{\mathrm H}\}$. Với
$$
c^*=\frac{10+c_{\mathrm H}}{4},
\tag{5.1}
$$
khi $c<c^*$ mọi chính sách tối ưu kết thúc tại $\mathrm G$ với xác suất $1$; khi $c>c^*$ mọi chính sách tối ưu kết thúc tại $\mathrm H$ với xác suất $1$; khi $c=c^*$ hai đường ngắn nhất cho cùng lợi tức.

**Điều kiện áp dụng.** Chi phí mỗi bước không âm, $\gamma=1$, chuyển tất định, tác tử tìm được chính sách tối ưu.

**Phạm vi.** Kết quả nói về điểm xuất phát $\mathrm S$ và tác tử tối ưu, không mô tả tác tử đang học. Với $c=0$ có nhiều chính sách tối ưu, kể cả chính sách đi vòng hữu hạn lần rồi tới $\mathrm G$.
:::

::: proof Chứng minh Mệnh đề 02.18
**Bước 1 (quỹ đạo kết thúc).** Quỹ đạo vào $\mathrm G$ sau $k$ bước có lợi tức $-ck+10$; theo Ví dụ 02.14, $k\ge6$, nên với $c\ge0$ lợi tức không vượt $10-6c$, dấu bằng tại đường $6$ bước. Quỹ đạo vào $\mathrm H$ sau $k\ge2$ bước có lợi tức $-ck-c_{\mathrm H}\le-2c-c_{\mathrm H}$, dấu bằng tại đường $2$ bước.

**Bước 2 (quỹ đạo không kết thúc).** Tổng riêng sau $n$ bước là $-cn$. Khi $c>0$, giới hạn là $-\infty$; khi $c=0$, giới hạn là $0<10=\max\{10,-c_{\mathrm H}\}$. Trong cả hai trường hợp, lợi tức nhỏ hơn $M$.

**Bước 3 (chính sách bất kỳ).** Theo Bước 1–2, mọi quỹ đạo có $G_0\le M$. Với một chính sách bất kỳ, kể cả ngẫu nhiên, $G_0\le M$ với xác suất $1$, nên $\mathbb E[G_0]$ tồn tại trong $[-\infty,M]$ và không vượt $M$. Chính sách đi thẳng tới $\mathrm G$ cho $10-6c$, chính sách đi thẳng tới $\mathrm H$ cho $-2c-c_{\mathrm H}$; vậy giá trị lớn nhất là $M$.

**Bước 4 (so sánh hai đường).**
$$
\begin{aligned}
10-6c>-2c-c_{\mathrm H}
&\iff10+c_{\mathrm H}>4c
&&\text{(cộng }6c+c_{\mathrm H}\text{ vào hai vế)}\\
&\iff c<\frac{10+c_{\mathrm H}}{4}
&&\text{(chia hai vế cho }4>0).
\end{aligned}
$$

**Bước 5 (chính sách tối ưu kết thúc ở đâu).** Giả sử $c<c^*$, nên $M=10-6c$. Mọi quỹ đạo vào $\mathrm H$ có $G_0\le-2c-c_{\mathrm H}<M$, và mọi quỹ đạo không kết thúc có $G_0<M$ theo Bước 2. Nếu một chính sách đặt xác suất dương vào tập các quỹ đạo không kết thúc tại $\mathrm G$, thì $G_0<M$ trên một biến cố xác suất dương và $G_0\le M$ ở mọi nơi, nên $\mathbb E[G_0]<M$. Vậy chính sách tối ưu kết thúc tại $\mathrm G$ với xác suất $1$. Trường hợp $c>c^*$ đối xứng, với $\mathrm H$ thay cho $\mathrm G$. $\square$
:::

![Đồ thị lợi tức G0 với gamma bằng 1 theo chi phí mỗi bước c từ 0 đến 4. Đường liền 10 trừ 6c ứng với đích, đi từ 10 xuống âm 14. Đường đứt âm 2c ứng với hố, đi từ 0 xuống âm 8. Hai đường cắt nhau tại c bằng 2,5, lợi tức âm 5. Bên trái giao điểm ghi c nhỏ hơn 2,5 chọn đích, bên phải ghi c lớn hơn 2,5 chọn hố.](img/lec-02/goal-hole-threshold.svg)

Đồ thị vẽ hai vế của Bước 4 khi $c_{\mathrm H}=0$. Đường liền của đích dốc $-6$ vì đường tới đích dài $6$ bước, đường đứt của hố dốc $-2$ vì đường vào hố dài $2$ bước; hai đường cắt nhau tại $c^*=2{,}5$, lợi tức $-5$. Ba dòng của Ví dụ 02.15 là ba điểm trên đồ thị: $c=0$ và $c=1$ bên trái giao điểm, $c=3$ bên phải.

Đọc bằng lời: phần thưởng thêm ở đích phải bù được chi phí của bốn bước chênh lệch giữa hai đường, tức $10+c_{\mathrm H}>4c$. Ngưỡng tăng theo phần thưởng ở đích và mức phạt hố, giảm khi chênh lệch số bước tăng. Mỗi giả thiết có vai trò riêng.

- **Bỏ $c\ge0$.** Với $c<0$, tức phần thưởng dương mỗi bước, quỹ đạo không kết thúc có lợi tức $+\infty$ khi $\gamma=1$; tiêu chí lợi tức không cho giá trị tối ưu hữu hạn, và Bước 1 sai vì đi vòng làm tăng lợi tức.
- **Bỏ $\gamma=1$.** Với $\gamma<1$, phần thưởng $+10$ ở bước thứ sáu bị nhân $\gamma^5$, còn chi phí của hai bước vào hố chỉ bị nhân $1$ và $\gamma$; hai lợi tức không còn là $10-6c$ và $-2c-c_{\mathrm H}$, nên phải lặp lại Bước 1 với lợi tức chiết khấu.
- **Bỏ chuyển tất định.** Nếu mỗi bước có xác suất trượt, số bước tới đích là biến ngẫu nhiên và phải so sánh lợi tức kỳ vọng.

Mệnh đề trả lời một câu hỏi điều khiển (Nhận xét 02.17): tìm chính sách tốt nhất trong mọi chính sách. Trên bài toán nhỏ và tất định này, việc tìm quy về so sánh các đường kết thúc; trường hợp tổng quát là nội dung của Bài 04.

::: remark Nhận xét 02.19 (Phạt mỗi bước và tác tử đang học)
- Phạt mỗi bước làm đường ngắn có lợi tức lớn hơn đường dài cùng điểm kết thúc; với $c=0$, mọi đường hữu hạn tới $\mathrm G$ đều có lợi tức $10$.
- Mức phạt hố $c_{\mathrm H}$ hữu hạn không bảo đảm tác tử chọn đích với mọi $c$: tăng $c_{\mathrm H}$ chỉ dời ngưỡng thêm $c_{\mathrm H}/4$.
- Một tác tử đang học, chẳng hạn chọn ngẫu nhiên với xác suất $\varepsilon$ như ở Bài 06, có thể rơi vào hố khi $c<c^*$, và có thể chưa phát hiện đường vào hố khi $c>c^*$.
- Sutton và Barto (2018, §17.4, trang 469–470) nêu hai rủi ro cùng loại: tác tử có thể tìm ra cách không mong muốn để nhận phần thưởng, và phần thưởng phụ cho mục tiêu trung gian có thể khiến tác tử không đạt mục tiêu chung.
:::

**Trong thực hành.** Phần thưởng mỗi bước trong các bài thực hành có dấu ngược với mê cung: CartPole (Bài 04) thưởng $+1$ mỗi bước còn giữ được cột; Flappy Bird (Bài 07) thưởng $+0{,}1$ mỗi bước chim còn sống, $+1$ khi qua một ống và $-1$ khi va chạm, lúc lượt kết thúc. Với phần thưởng dương mỗi bước, kết thúc là bất lợi và tác tử tối ưu kéo dài lượt; đây là trường hợp đã loại ở gạch đầu dòng "Bỏ $c\ge0$" sau Mệnh đề 02.18. Hai bài thực hành vẫn có lợi tức hữu hạn nhờ $\gamma=0{,}99<1$ (Mệnh đề 02.13) và nhờ lượt bị cắt. Trong Lunar Lander (Bài 05–06), phần thưởng lớn $\pm100$ chỉ đến ở bước kết thúc, nên bài toán có phản hồi trễ.

::: exercise Bài tập 02.8 (Phạt hố bổ sung)
Mê cung đích–hố của Ví dụ 02.14: đường ngắn nhất tới $\mathrm G$ dài $6$ bước, tới $\mathrm H$ dài $2$ bước; mỗi bước nhận $-c$; vào $\mathrm G$ thêm $+10$; vào $\mathrm H$ thêm $-c_{\mathrm H}$ với $c_{\mathrm H}\ge0$; $\gamma=1$; chuyển tất định.

- (a) Với $c=3$, tìm điều kiện của $c_{\mathrm H}$ để tác tử tối ưu tới đích; nếu $c_{\mathrm H}$ nguyên, $c_{\mathrm H}$ nhỏ nhất là bao nhiêu.
- (b) Với $c_{\mathrm H}=4$, tìm mọi $c\ge0$ để tác tử tối ưu tới đích.
:::

::: hint
Dùng (5.1), hoặc so sánh trực tiếp $10-6c$ với $-2c-c_{\mathrm H}$.
:::

::: solution
**Câu (a).** Cần $10-18>-6-c_{\mathrm H}$, tức $c_{\mathrm H}>2$; theo (5.1), $c^*=(10+c_{\mathrm H})/4>3$ cũng cho $c_{\mathrm H}>2$. Với $c_{\mathrm H}=2$, hai lợi tức bằng nhau ($-8$). Nếu $c_{\mathrm H}$ nguyên thì $c_{\mathrm H}\ge3$.

**Câu (b).** $c^*=(10+4)/4=3{,}5$, nên tác tử tối ưu tới đích khi $0\le c<3{,}5$.

**Kiểm tra lại.** Tại $c=3{,}5$, $c_{\mathrm H}=4$: đích $10-21=-11$, hố $-7-4=-11$, ngang nhau như (5.1) dự báo.
:::

### 5.3 Khuyến khích và chế tài

::: remark Nhận xét 02.20 (Khuyến khích, chế tài và giới hạn của phép so sánh)
Trong mê cung đích–hố, phần thưởng $+10$ ở đích đóng vai trò khuyến khích, mức phạt $c_{\mathrm H}$ khi vào hố đóng vai trò chế tài. Mệnh đề 02.18 cho thấy tác dụng của chế tài phụ thuộc tương quan với các chi phí khác: với chi phí mỗi bước đủ lớn, hành vi không mong muốn vẫn có lợi tức lớn hơn. Chính sách xã hội và pháp luật cũng dùng lợi ích để làm hành vi phù hợp hấp dẫn hơn và chế tài để làm hành vi vi phạm kém hấp dẫn hơn. Phép so sánh có giới hạn. Mô hình giả định tác tử cực đại một con số duy nhất, còn con người hành động vì cả nghĩa vụ, niềm tin và quan hệ xã hội, và pháp luật còn xét quyền, nghĩa vụ, công bằng.
:::

Như vậy, chúng ta đã tính lợi tức của hai đường kết thúc trên mê cung đích–hố (Ví dụ 02.15) và chứng minh rằng tác tử tối ưu đổi từ đích sang hố tại ngưỡng $c^*=(10+c_{\mathrm H})/4$ (Mệnh đề 02.18), dưới các giả thiết chi phí không âm, $\gamma=1$ và chuyển tất định. Kết quả dùng mọi thành phần của chương: mẫu chuyển để đặt chỉ số phần thưởng, trạng thái Markov để mô tả hành lang, chính sách để nói về tác tử tối ưu, lợi tức để so sánh. Hai tình huống dưới đây đặt các thành phần đó vào một bài toán mà giả thiết được thỏa và một bài toán mà giả thiết quan sát bị vi phạm.

## Tình huống áp dụng và ứng dụng

::: application Tình huống 02.1 (Robot giao hàng trên hành lang kho)
**Bài toán.** Theo hướng của Bài tập tuần 2 (2025–2026), bài 10, một robot giao hàng chạy trên hành lang kho gồm năm ô $0,\dots,4$; ô $4$ là điểm giao hàng. Robot xuất phát tại ô $0$ với $5$ đơn vị pin. Hành động Tiến tốn $1$ đơn vị pin; với xác suất $0{,}9$ robot sang ô kế tiếp, với xác suất $0{,}1$ bánh xe trượt và robot ở lại. Hành động Chờ không tốn pin, robot đứng yên. Mỗi bước nhận $-1$; bước tới ô $4$ nhận thêm $+10$. Lượt kết thúc khi robot tới ô $4$, gọi là đã giao, hoặc khi pin về $0$ ở ô khác ô $4$, gọi là hết pin. $\gamma=0{,}9$. Robot nhận mức pin và ô hiện tại.

**Mô hình hóa.** Tác tử là bộ điều khiển; bánh xe, sàn, pin và cơ chế tính phần thưởng thuộc môi trường. Trạng thái $s=(\ell,b)$ với $\ell\in\{0,\dots,3\}$, $b\in\{1,\dots,5\}$, cho $20$ trạng thái chưa kết thúc, cùng hai trạng thái kết thúc. Hàm động lực của Tiến (Định nghĩa 02.16): với $\ell\le2$, $p((\ell+1,b-1),-1\mid(\ell,b),\text{Tiến})=0{,}9$ và $p((\ell,b-1),-1\mid(\ell,b),\text{Tiến})=0{,}1$; với $\ell=3$, $p(\text{đã giao},9\mid(3,b),\text{Tiến})=0{,}9$ và $p((3,b-1),-1\mid(3,b),\text{Tiến})=0{,}1$. Ở mọi $\ell$, trạng thái có $b-1=0$ mà chưa giao là "hết pin". Chính sách $\pi$ luôn chọn Tiến.

**Kiểm tra giả thiết.** Nếu trạng thái chỉ là $\ell$, xác suất hết pin phụ thuộc số bước Tiến đã đi: ở ô $2$, sau hai bước thành công còn $3$ đơn vị pin, sau hai lần trượt rồi hai bước thành công chỉ còn $1$. Đưa $b$ vào trạng thái làm mọi xác suất chuyển chỉ phụ thuộc $(\ell,b)$ và hành động, nên tính Markov (Định nghĩa 02.5) thỏa; xác suất trượt được giả định không đổi, nên môi trường dừng. Robot nhận cả $\ell$ và $b$, nên $X_t=S_t$. Phần thưởng bị chặn bởi $R_{\max}=9$ và $\gamma<1$, nên theo (4.7) mọi lợi tức không vượt $90$ về trị tuyệt đối. Bốn giả thiết của Định nghĩa 02.14 thỏa.

**Áp dụng.** Cần $4$ bước thành công, pin cho tối đa $5$ bước, nên có ba kết cục:

- giao sau $4$ bước, không trượt: xác suất $0{,}9^4=0{,}6561$; phần thưởng $-1,-1,-1,+9$; lợi tức $-1-0{,}9-0{,}81+0{,}729\cdot9=3{,}851$;
- trượt đúng một lần trong $4$ bước đầu, giao ở bước $5$: xác suất $4\cdot0{,}1\cdot0{,}9^3\cdot0{,}9=0{,}26244$; lợi tức $-(1+0{,}9+0{,}81+0{,}729)+0{,}6561\cdot9=2{,}4659$;
- hết pin sau $5$ bước: xác suất $1-0{,}6561-0{,}26244=0{,}08146$; lợi tức $-(1+0{,}9+0{,}81+0{,}729+0{,}6561)=-4{,}0951$.

Theo (4.8),
$$
v_\pi((0,5))=0{,}6561\cdot3{,}851+0{,}26244\cdot2{,}4659+0{,}08146\cdot(-4{,}0951)\approx2{,}840 .
$$

**Diễn giải.** Giá trị dương nghĩa là, tính trung bình, phần thưởng giao hàng bù được chi phí thời gian dưới chính sách luôn Tiến; đơn vị pin thứ năm là dự phòng cho một lần trượt. Nếu robot chỉ nhận mức pin, quan sát thành một phần: sau một bước Tiến, pin là $4$ dù robot ở ô $1$ hay ô $0$. Chính sách luôn Tiến không cần biết ô nên không bị ảnh hưởng, còn một chính sách cần biết ô thì không cài đặt được.

**Giới hạn.** Mô hình giả định xác suất trượt không đổi và độc lập giữa các bước, mức tiêu hao pin cố định và chỉ một robot trên hành lang; nới mỗi giả định cần thêm biến vào trạng thái để giữ tính Markov.

**Dẫn ngược lý thuyết.** Định nghĩa 01.1 (ranh giới); Định nghĩa 02.5 (lý do đưa $b$ vào trạng thái); Nhận xét 02.4 (quan sát đầy đủ, và trường hợp chỉ có pin); Định nghĩa 02.8 (chính sách); Định nghĩa 02.12, Mệnh đề 02.13 (lợi tức, chặn); Định nghĩa 02.14 (giá trị); Định nghĩa 02.16 (hàm động lực).

**Kiểm tra lại.** Ba xác suất cộng lại bằng $1$. Kết cục thứ nhất theo hệ thức truy hồi: $G_3=9$, $G_2=-1+0{,}9\cdot9=7{,}1$, $G_1=-1+0{,}9\cdot7{,}1=5{,}39$, $G_0=-1+0{,}9\cdot5{,}39=3{,}851$.
:::

<!-- note-topic-id: lec-02-topic-14 -->
::: application Tình huống 02.2 (Biểu diễn bốn ô kề trên mê cung $8\times8$: giả thiết quan sát đầy đủ không thỏa)
**Bài toán.** Mê cung $8\times8$ của Ví dụ 02.1: xuất phát $(0,2)$, đích $\mathrm G$ sau bước Đông từ $(7,6)$, đứng yên khi gặp tường hoặc biên, $-1$ mỗi bước, $\gamma=1$. Tác tử chỉ có cảm biến bốn ô kề và dùng luôn quan sát làm biểu diễn, $X_t=O_t$, tức mã bốn ô kề của Ví dụ 02.4. Với tọa độ làm biểu diễn, chính sách ở Mục 3 tới $\mathrm G$ sau $16$ bước, lợi tức $-16$.

**Giả thiết bị vi phạm.** Mã bốn ô kề cho quan sát một phần (Nhận xét 02.4), nên giả thiết $X_t=S_t$ của Định nghĩa 02.14 không thỏa. Hai ô $\mathrm A=(1,1)$ và $\mathrm B=(5,3)$ có cùng mã $(1,0,0,1)$: tại $\mathrm A$, Bắc $(1,0)$ và Tây $(0,1)$ là tường, Đông $(2,1)$ và Nam $(1,2)$ trống; tại $\mathrm B$, Bắc $(5,2)$ và Tây $(4,3)$ là tường, Đông $(6,3)$ và Nam $(5,4)$ trống.

![Mê cung tám hàng tám cột. Hai ô A bằng (1,1) và B bằng (5,3) được gạch chéo; cả hai có mã bốn ô kề (1,0,0,1) theo thứ tự Bắc, Đông, Nam, Tây, với 1 là bước giữ tác tử đứng yên và 0 là bước đưa tác tử sang ô khác. Mũi tên liền tại A chỉ Đông, tại B chỉ Nam: đó là hướng cần chọn để tới đích. Mũi tên đứt hai chiều giữa A và ô (1,2), và giữa B và ô (6,3), chỉ vòng lặp nếu chọn hướng kia.](img/lec-02/aliasing-pair.svg)

Để tới $\mathrm G$, tác tử phải rời $\mathrm A$ theo hướng Đông (mũi tên liền) và rời $\mathrm B$ theo hướng Nam, trong khi biểu diễn không phân biệt được hai ô; mũi tên đứt chỉ vòng lặp khi chọn hướng kia.

**Mọi chính sách xác định trên mã đều không tới $\mathrm G$.** Mã $(0,1,0,0)$ chỉ có ở $(1,2)$, mã $(0,1,1,0)$ chỉ có ở $(6,3)$.

- Từ $(0,2)$, phần mê cung chứa hàng $1$ và mọi đường tới $\mathrm G$ chỉ nối với $(1,2)$ qua $\mathrm A$. Nếu chính sách tại $(0,1,0,0)$ khác Bắc, tác tử không bao giờ tới $\mathrm A$, nên không tới $\mathrm G$; vậy chỉ cần xét chính sách chọn Bắc tại $(1,2)$, và khi đó tác tử tới $\mathrm A$ lần đầu từ $(1,2)$.
- Tương tự, vùng $(5,4)$, $(5,5)$, $(6,5)$, $(6,6)$, $(7,6)$ chỉ nối với phần còn lại qua $\mathrm B$; nếu chính sách tại $(0,1,1,0)$ khác Tây, tác tử không tới $\mathrm B$ từ $(6,3)$, nên không tới $\mathrm G$. Chỉ cần xét chính sách chọn Tây tại $(6,3)$.
- Gọi $a^*$ là hành động tại mã $(1,0,0,1)$. Nếu $a^*$ là Bắc hoặc Tây, tác tử đứng yên mãi tại $\mathrm A$. Nếu $a^*$ là Nam, tác tử đi $\mathrm A\to(1,2)\to\mathrm A\to\cdots$ mãi. Nếu $a^*$ là Đông, tác tử qua $\mathrm A$ nhưng đi $\mathrm B\to(6,3)\to\mathrm B\to\cdots$ mãi.

Theo quy ước giới hạn tổng riêng của Mục 4.2, lợi tức khi đó là $-\infty$.

**Khắc phục bằng chính sách ngẫu nhiên.** Đặt $\pi(\text{Đông}\mid(1,0,0,1))=\pi(\text{Nam}\mid(1,0,0,1))=0{,}5$; tại các mã khác trên đường 16 bước, chọn hướng của chính sách ở Mục 3. Các mã đó không mâu thuẫn dọc đường đi: $(1,0,1,0)$ luôn Đông, $(1,1,0,0)$ luôn Nam tại $(6,1)$ và $(6,5)$, $(0,1,0,1)$ luôn Nam tại $(6,2)$ và $(5,4)$, $(0,0,1,1)$ luôn Đông tại $(5,5)$ và $(6,6)$. Tại $\mathrm A$, mỗi lần chọn Nam tốn thêm $2$ bước, và số lần chọn Nam trước lần Đông đầu tiên có kỳ vọng $1$; tại $\mathrm B$ tương tự với hai hướng đổi vai. Số bước kỳ vọng từ $(0,2)$ tới $\mathrm G$ là $16+2+2=20$, lợi tức kỳ vọng $-20$.

**Khắc phục bằng bộ nhớ.** Dùng cửa sổ hai quan sát $X_t=(O_t,A_{t-1},O_{t-1})$, với quy ước $X_0=(O_0,\varnothing,\varnothing)$. Tại $\mathrm A$, quan sát trước là mã $(0,1,0,0)$ của $(1,2)$; tại $\mathrm B$, là mã $(0,1,1,0)$ của $(6,3)$. Dọc đường 16 bước, mười sáu biểu diễn khác nhau, nên một chính sách xác định trên biểu diễn mới đi lại được đường 16 bước, lợi tức $-16$.

**Diễn giải và giới hạn.** Khi biểu diễn gộp hai trạng thái cần hai hành động khác nhau, mọi chính sách xác định trên biểu diễn đó có thể không bao giờ tới đích, còn chính sách ngẫu nhiên tới đích với xác suất $1$ nhưng chậm hơn: $-20$ so với $-16$. Bộ nhớ hai bước đủ cho bản đồ này, nhưng theo Nhận xét 02.7, không có cửa sổ hữu hạn nào đủ cho mọi bài toán. Phần chính sách ngẫu nhiên giữ nguyên các mã khác theo chính sách tối ưu khi có tọa độ; kết luận "mọi chính sách xác định thất bại" chỉ dùng cấu trúc của hai ô $\mathrm A$, $\mathrm B$.

**Dẫn ngược lý thuyết.** Định nghĩa 02.2 (mã bốn ô kề là một biểu diễn); Nhận xét 02.4 (quan sát một phần); Định nghĩa 02.8 (chính sách trên $X$); Định nghĩa 02.14 (giả thiết $X_t=S_t$ bị vi phạm, nên ta chỉ tính lợi tức kỳ vọng từ ô xuất phát); Nhận xét 02.7; Bài tập tuần 2 (2025–2026), bài 6; Sutton và Barto (2018, §13.1, Ví dụ 13.1, trang 323), nơi một hành lang mà mọi ô trông như nhau cần chính sách ngẫu nhiên.

**Kiểm tra lại.** Tại $\mathrm A$, gọi $E$ là số bước kỳ vọng từ $\mathrm A$ tới $(2,1)$: $E=0{,}5\cdot1+0{,}5\cdot(2+E)$, nên $E=3$, nhiều hơn trường hợp có tọa độ đúng $2$ bước.
:::

**Ứng dụng.**

- **Quá trình quyết định Markov (Bài 03).** Trạng thái Markov, hành động và hàm động lực (Định nghĩa 02.5, 02.16), cùng hệ số chiết khấu, là một MDP. Lấy kỳ vọng hai vế của $G_t=R_{t+1}+\gamma G_{t+1}$ (Mệnh đề 02.13) dưới $\pi$ cho phương trình Bellman của $v_\pi$.
- **Quy hoạch động trên CartPole (Bài 04).** Quy hoạch động cần $p$; trong notebook Bài 04, $\hat p$ được ước lượng trên $324$ ô rời rạc và tính Markov của ô được kiểm tra.
- **Dự đoán phi mô hình trên Lunar Lander (Bài 05).** Monte Carlo và sai phân thời gian ước lượng $v_\pi$ (Định nghĩa 02.14) chỉ từ các mẫu chuyển; lượt bị cắt ở bước $1\,000$ thiếu một phần lợi tức.
- **Điều khiển phi mô hình (Bài 06).** Chính sách $\varepsilon$-tham lam là một chính sách ngẫu nhiên theo Định nghĩa 02.8, dùng cho bài toán điều khiển của Nhận xét 02.17.
- **Xấp xỉ tuyến tính trên Flappy Bird (Bài 07).** Đặc trưng là một hàm biểu diễn của quan sát hiện tại (Định nghĩa 02.2); phần thưởng dương mỗi bước là trường hợp $c<0$ đã loại ở Mệnh đề 02.18.

<!-- note-topic-id: lec-02-part-07 -->
## Tóm tắt chương

Chúng ta bắt đầu từ một mê cung $8\times8$ với phần thưởng $-1$ mỗi bước và bốn câu hỏi mà chính sách, giá trị trên lịch sử và lợi tức không chiết khấu của Bài 01 chưa trả lời gọn. Mẫu chuyển (Định nghĩa 02.1) cố định thứ tự tín hiệu của một bước. Biểu diễn (Định nghĩa 02.2) tách dữ liệu tác tử dùng khỏi trạng thái và quan sát, và tính Markov (Định nghĩa 02.5) nêu khi nào trạng thái đủ cho dự báo; Mệnh đề 02.6 cho thấy lịch sử luôn là trạng thái Markov nhưng lớn dần. Chính sách được viết trên biểu diễn (Định nghĩa 02.8), với chính sách trên lịch sử của Bài 01 là một trường hợp riêng. Định lý 02.11 chứng minh rằng ưu tiên dừng buộc trọng số hình học, dẫn tới lợi tức chiết khấu (Định nghĩa 02.12) với hệ thức truy hồi và chặn (Mệnh đề 02.13); kỳ vọng của lợi tức dưới một chính sách cố định là hàm giá trị trạng thái (Định nghĩa 02.14), tách khỏi hàm động lực dự báo một bước (Định nghĩa 02.16). Mệnh đề 02.18 cho ngưỡng $c^*=(10+c_{\mathrm H})/4$ làm tác tử tối ưu đổi từ đích sang hố. Giới hạn còn lại là giá trị mới tính được khi liệt kê được các quỹ đạo; ở Bài 03, Mệnh đề 02.13(a) và tính Markov cho phép viết giá trị thành nghiệm của một hệ phương trình.

**Định nghĩa và kết quả theo mục.**

- Mục 1: mẫu chuyển (Định nghĩa 02.1).
- Mục 2: biểu diễn và hàm biểu diễn (Định nghĩa 02.2); lịch sử trạng thái và quỹ đạo (Định nghĩa 02.3); quan sát đầy đủ theo nghĩa tổng quát (Nhận xét 02.4); tính Markov (Định nghĩa 02.5); lịch sử là trạng thái Markov (Mệnh đề 02.6); cửa sổ hữu hạn (Nhận xét 02.7).
- Mục 3: chính sách trên biểu diễn (Định nghĩa 02.8); các nhầm lẫn về chính sách (Nhận xét 02.9).
- Mục 4: lợi ích cộng và ưu tiên dừng (Định nghĩa 02.10); ưu tiên dừng buộc $w_i=\gamma^{i-1}$, $0<\gamma\le1$ (Định lý 02.11); lợi tức (Định nghĩa 02.12); $G_t=R_{t+1}+\gamma G_{t+1}$ và $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$ (Mệnh đề 02.13); hàm giá trị trạng thái (Định nghĩa 02.14); kỳ vọng hữu hạn và hạn chót (Nhận xét 02.15); hàm động lực (Định nghĩa 02.16); dự đoán và điều khiển (Nhận xét 02.17).
- Mục 5: ngưỡng đổi hành vi (Mệnh đề 02.18); phạt mỗi bước và tác tử đang học (Nhận xét 02.19); khuyến khích và chế tài (Nhận xét 02.20).

**Công thức cần nhớ.**
$$
G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}=R_{t+1}+\gamma G_{t+1},\qquad \lvert G_t\rvert\le\frac{R_{\max}}{1-\gamma}\ (\gamma<1),
$$
$$
\pi(a\mid x)=\Pr(A_t=a\mid X_t=x),\qquad v_\pi(s)=\mathbb E_\pi\bigl[G_0\mid S_0=s\bigr],\qquad p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a).
$$

**Giả thiết hay bị bỏ quên.**

- Phần thưởng của $A_t$ là $R_{t+1}$, không phải $R_t$.
- Tính Markov là tính chất của biến được chọn làm trạng thái; đọc lại được tọa độ không kéo theo tính Markov khi tọa độ thiếu bit $k$ (Ví dụ 02.6).
- Chính sách viết trên biểu diễn mà tác tử có; viết trên trạng thái chỉ khi $X_t=S_t$.
- Định lý 02.11 cần dạng cộng và trọng số dùng chung; nhiệm vụ tiếp diễn cần $\gamma<1$ và phần thưởng bị chặn.
- $v_\pi$ cần chính sách cố định, trạng thái Markov, môi trường dừng và kỳ vọng hữu hạn; với $\gamma=1$, kết thúc với xác suất $1$ chưa đủ.
- Mệnh đề 02.18 cần $c\ge0$, $\gamma=1$, chuyển tất định, và chỉ nói về tác tử tối ưu.

## Bài tập củng cố

Các bài tập trong các mục (Bài tập 02.1–02.8) và năm bài 02.9–02.13 dưới đây là bài tập của ghi chú; mỗi mục tiêu học tập có ít nhất một bài dưới đây, như ghi ở phần Mục tiêu học tập. Bộ bài tập chính thức của Bài 02 nằm trong [tệp bài tập](material-viewer.html?doc=materials/lec-02/exercises.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html), gồm hai mươi hai bài đánh số chung với ghi chú: các bài 02.1–02.5, 02.7, 02.8 được phát biểu lại với đủ dữ kiện, chín bài 02.14–02.22 chỉ có ở tệp bài tập, còn 02.6 và 02.9–02.13 chỉ có ở ghi chú.

### Mức nhận biết

::: exercise Bài tập 02.9 (Ghép phát biểu với thành phần)
Mê cung $8\times8$ của Ví dụ 02.1 với chính sách xác định của Mục 3, tại đó $(4,1)$ chọn Đông và $(4,2)$ chọn Bắc; $-1$ mỗi bước, chuyển tất định. Mỗi phát biểu mô tả thành phần nào: ranh giới tác tử–môi trường, quan sát, chính sách, hàm giá trị, hay hàm động lực. Nêu định nghĩa tương ứng.

1. Tại $(4,1)$, tác tử chọn Đông với xác suất $1$.
2. Từ $(4,1)$, với $\gamma=1$, lợi tức kỳ vọng khi theo chính sách là $-11$.
3. Từ $(4,1)$, chọn Nam thì tới $(4,2)$ và nhận $-1$ với xác suất $1$.
4. Khi tác tử ở $(4,1)$, cảm biến bốn ô kề báo mã $(1,0,0,0)$.
5. Bản đồ và quy tắc trừ $1$ mỗi bước cố định; chỉ hướng đi do tác tử chọn.
:::

::: hint
Phát biểu nào phụ thuộc chính sách, phát biểu nào chỉ nói về một bước, phát biểu nào nói về cả chuỗi phần thưởng.
:::

::: solution
1. Chính sách: $\pi(\text{Đông}\mid(4,1))=1$ (Định nghĩa 02.8).
2. Hàm giá trị: $v_\pi((4,1))=-11$ (Định nghĩa 02.14).
3. Hàm động lực: $p((4,2),-1\mid(4,1),\text{Nam})=1$ (Định nghĩa 02.16), không phụ thuộc chính sách.
4. Quan sát, hay biểu diễn nếu tác tử dùng luôn mã này (Định nghĩa 02.2): Bắc $(4,0)$ là tường, Đông $(5,1)$, Nam $(4,2)$, Tây $(3,1)$ trống.
5. Ranh giới (Định nghĩa 01.1): bản đồ và cơ chế tính phần thưởng thuộc môi trường.

**Kiểm tra lại.** $v_\pi((4,1))=-1+v_\pi((5,1))=-1+(-10)=-11$ theo Ví dụ 02.12.
:::

::: exercise Bài tập 02.10 (Hệ số chiết khấu và dấu của phần thưởng mỗi bước)
Theo Bài tập tuần 2 (2025–2026), bài 5.

- (a) So sánh $\sigma=(0,0,10)$ và $\sigma'=(1,0,0)$ bằng lợi ích cộng với $\gamma=0$, $0{,}5$, $0{,}99$; tìm $\gamma\in(0,1)$ để hai chuỗi ngang nhau, và mô tả hành vi của tác tử khi $\gamma=0$ và khi $\gamma$ gần $1$.
- (b) Trong mê cung đích–hố của Ví dụ 02.14 (đường ngắn nhất tới $\mathrm G$ dài $6$ bước, tới $\mathrm H$ dài $2$ bước, tác tử có thể đi vòng), phần thưởng $-c$ mỗi bước được thay bằng $+0{,}1$ mỗi bước, giữ $+10$ khi vào $\mathrm G$ và không thêm gì khi vào $\mathrm H$. Giải thích vì sao với $\gamma=1$ tiêu chí lợi tức không cho giá trị tối ưu hữu hạn. Với $\gamma=0{,}9$, tính lợi tức của đường thẳng tới $\mathrm G$ và của một quỹ đạo không bao giờ kết thúc.
:::

::: hint
Ở (a), $U(\sigma)=10\gamma^2$. Ở (b), so với giả thiết $c\ge0$ của Mệnh đề 02.18 và dùng tổng hình học.
:::

::: solution
**Câu (a).** $U(\sigma)=10\gamma^2$, $U(\sigma')=1$: với $\gamma=0$ chọn $\sigma'$ ($0<1$); với $\gamma=0{,}5$ chọn $\sigma$ ($2{,}5>1$); với $\gamma=0{,}99$ chọn $\sigma$ ($9{,}801>1$). Ngang nhau khi $\gamma=1/\sqrt{10}\approx0{,}316$. Với $\gamma=0$, tác tử chỉ xét phần thưởng kế tiếp; với $\gamma$ gần $1$, tác tử chịu chờ để nhận phần thưởng lớn.

**Câu (b).** Với $\gamma=1$, quỹ đạo đi vòng mãi có tổng riêng $0{,}1n\to+\infty$; mọi quỹ đạo kết thúc bị vượt bởi một quỹ đạo đi vòng đủ lâu, nên không có giá trị tối ưu hữu hạn. Đây là trường hợp $c=-0{,}1<0$. Với $\gamma=0{,}9$: đường thẳng tới $\mathrm G$ cho $0{,}1\cdot\frac{1-0{,}9^6}{0{,}1}+10\cdot0{,}9^5=0{,}468559+5{,}9049\approx6{,}373$; quỹ đạo không kết thúc cho $0{,}1/(1-0{,}9)=1$.

**Kiểm tra lại.** $0{,}9^5=0{,}59049$, $(1-0{,}9^6)/0{,}1=4{,}68559$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 02.11 (Quan sát hiện tại không phải trạng thái Markov)
Mê cung $8\times8$; tác tử dùng luôn quan sát làm biểu diễn, $X_t=O_t$ là mã bốn ô kề, với mã tại $(1,1)$ là $(1,0,0,1)$, tại $(2,1)$ và $(3,1)$ là $(1,0,1,0)$, tại $(4,1)$ là $(1,0,0,0)$. Tác tử xuất phát tại $(1,1)$ hoặc $(2,1)$, mỗi ô với xác suất $0{,}5$, và luôn chọn Đông.

- (a) Tính $\Pr\bigl(X_2=(1,0,0,0)\mid X_0=x_0,A_0=\text{Đông},X_1=(1,0,1,0),A_1=\text{Đông}\bigr)$ với $x_0=(1,0,0,1)$ và với $x_0=(1,0,1,0)$.
- (b) Tính $\Pr\bigl(X_2=(1,0,0,0)\mid X_1=(1,0,1,0),A_1=\text{Đông}\bigr)$, kết luận về tính Markov của $X_t$ và đề xuất một biểu diễn sửa được lỗi này trên đoạn hành lang đang xét.
:::

::: hint
Viết rõ tác tử ở ô nào tại $t=0,1,2$ trong mỗi trường hợp xuất phát.
:::

::: solution
**Câu (a).** Với $x_0=(1,0,0,1)$: tác tử đi $(1,1)\to(2,1)\to(3,1)$, nên $X_2=(1,0,1,0)$ và xác suất bằng $0$. Với $x_0=(1,0,1,0)$: tác tử đi $(2,1)\to(3,1)\to(4,1)$, nên $X_2=(1,0,0,0)$ và xác suất bằng $1$.

**Câu (b).** $X_1=(1,0,1,0)$ xảy ra trong cả hai trường hợp, mỗi trường hợp xác suất $0{,}5$, nên xác suất cần tính là $0{,}5\cdot0+0{,}5\cdot1=0{,}5$. Hai lịch sử cùng kết thúc ở $X_1=(1,0,1,0)$ với cùng $A_1$ cho $0$ và $1$, khác $0{,}5$, nên (2.3) sai và $X_t$ không có tính Markov. Cửa sổ $(O_t,A_{t-1},O_{t-1})$ phân biệt $(2,1)$ (quan sát trước $(1,0,0,1)$) với $(3,1)$ (quan sát trước $(1,0,1,0)$); dùng tọa độ cũng sửa được.

**Kiểm tra lại.** Ở $t=1$, hai trường hợp ở $(2,1)$ và $(3,1)$, cùng mã $(1,0,1,0)$.
:::

::: exercise Bài tập 02.12 (Chặn của lợi tức)
- (a) Phần thưởng thỏa $\lvert R_{t+1}\rvert\le1$ và $\gamma=0{,}9$. Tính chặn (4.7) và chỉ ra một chuỗi phần thưởng đạt chặn.
- (b) Một lượt kiểu CartPole nhận $+1$ mỗi bước và kéo dài đúng $20$ bước. Tính $G_0$ với $\gamma=0{,}9$.
- (c) Với cùng cách thưởng, tìm số bước $T$ nhỏ nhất để $G_0\ge9$.
:::

::: hint
Lợi tức của $T$ bước $+1$ là $(1-\gamma^T)/(1-\gamma)$.
:::

::: solution
**Câu (a).** $1/(1-0{,}9)=10$, đạt bởi chuỗi $+1$ ở mọi bước, không kết thúc.

**Câu (b).** $G_0=(1-0{,}9^{20})/0{,}1=10(1-0{,}12158)\approx8{,}784$, đúng chặn của Mệnh đề 02.13(c).

**Câu (c).** $10(1-0{,}9^T)\ge9\iff0{,}9^T\le0{,}1\iff T\ge\ln0{,}1/\ln0{,}9\approx21{,}85$, nên $T=22$.

**Kiểm tra lại.** $0{,}9^{21}\approx0{,}1094$ cho $G_0\approx8{,}906<9$; $0{,}9^{22}\approx0{,}0985$ cho $G_0\approx9{,}015$.
:::

### Mức vận dụng

::: exercise Bài tập 02.13 (Chính sách trên tọa độ trong mê cung có chìa khóa)
Mê cung có chìa khóa của Ví dụ 02.6: chìa khóa ở ngõ cụt $(4,2)$, chỉ nối với $(4,1)$, nhặt khi vào ô đó; cửa từ $(7,6)$ vào $\mathrm G$ chỉ mở khi có chìa khóa; mọi đường từ $(0,2)$ tới $\mathrm G$ đi qua $(4,1)$.

- (a) Chứng minh rằng không chính sách xác định nào trên biểu diễn là tọa độ ô hiện tại đưa tác tử từ $(0,2)$ tới $\mathrm G$.
- (b) Nêu một biểu diễn và một chính sách xác định trên nó đưa tác tử tới $\mathrm G$, và số bước tương ứng.
:::

::: hint
Xét hành động mà chính sách chọn tại $(4,1)$, lần thứ nhất và lần thứ hai tác tử ở đó.
:::

::: solution
**Câu (a).** Gọi $a$ là hành động của chính sách tại $(4,1)$. Nếu $a$ là Nam, tác tử vào $(4,2)$; tại đó chỉ có Bắc đưa tác tử đi, mọi hướng khác giữ nó đứng yên mãi; nếu chọn Bắc, tác tử về $(4,1)$ và lại đi Nam, lặp mãi. Nếu $a$ khác Nam, tác tử không bao giờ vào $(4,2)$, vì $(4,2)$ chỉ nối với $(4,1)$; nó không có chìa khóa nên không qua được cửa. Trong mọi trường hợp tác tử không tới $\mathrm G$: tại $(4,1)$, chính sách cần Nam ở lần ghé thứ nhất và Đông ở lần ghé thứ hai, điều mà tọa độ không phân biệt được.

**Câu (b).** Biểu diễn (ô, $k$) của Ví dụ 02.6: chọn Nam tại $((4,1),0)$, Bắc tại $((4,2),1)$, Đông tại $((4,1),1)$, và theo đường 16 bước ở các ô khác. Tác tử tới $\mathrm G$ sau $18$ bước, lợi tức $-18$ với $\gamma=1$.

**Kiểm tra lại.** Hai lần ghé $(4,1)$ có cùng tọa độ nhưng khác $k$, nên biểu diễn mới tách được hai lần ghé.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

- **Bài giảng gốc.** Tạ Việt Cường (2025–2026), *Lecture 2: Markov Decision Process*, trang 1–27; mê cung $8\times8$, chính sách và bảng giá trị ở trang 25–26.
- **Bài tập tuần 2 (2025–2026).** Bài 2 (Mục 2), bài 5 (Bài tập 02.10), bài 6 (Tình huống 02.2), bài 10 (Tình huống 02.1); bài 3, 4, 7, 8, 9 cần MDP và phương trình Bellman của Bài 03.
- **Bài tập Bài 02.** [Tệp bài tập](material-viewer.html?doc=materials/lec-02/exercises.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html), hai mươi hai bài ở ba mức, đánh số chung với ghi chú. Câu đố phân loại ở trang 27 của bài giảng gốc được giải ở Bài tập 02.15; Bài tập tuần 2, bài 1, 6, 10 là nguồn của Bài tập 02.14, 02.19, 02.22.
- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2: §3.1 (trang 47–50), §3.2 (trang 53–54), §3.3–3.4 (trang 54–58), §3.5 (trang 58–59), §13.1 (trang 323), §17.3–17.4 (trang 464–470).
- **Russell, S. và Norvig, P. (2020).** *Artificial Intelligence: A Modern Approach*, ấn bản 4, §17.1.1 (trang 565–566), cho Mục 4.1 và Nhận xét 02.15.
- **Puterman, M. L. (1994).** *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, §2.1, cho Mục 3.
- **Giáo trình *Học máy thống kê*,** chương Học tăng cường, mục "Giới thiệu về quá trình quyết định Markov", cho tương ứng ký hiệu và thuật ngữ.

<!-- note-topic-id: lec-02-topic-15 -->
**Đọc thêm.** Sutton và Barto (2018, §17.3, trang 464–468) mở rộng Mệnh đề 02.6 sang lịch sử hành động và quan sát của chính tác tử: một trạng thái là hàm của lịch sử đó, và là trạng thái Markov khi nó dự báo tương lai tốt như toàn bộ lịch sử; cùng mục bàn cửa sổ hữu hạn của Nhận xét 02.7. Mục §17.4 (trang 469–470) bàn phần thưởng thưa, phần thưởng phụ và kỹ thuật định hình phần thưởng, tiếp nối Mục 5. Với chuỗi ngẫu nhiên, việc so sánh bằng kỳ vọng của lợi tức là một lựa chọn mô hình: chẳng hạn, lựa chọn cho chuỗi $(2)$ chắc chắn có kỳ vọng lợi ích $2$, lớn hơn $1{,}5$ của lựa chọn cho $(0)$ hoặc $(3)$ với xác suất bằng nhau, nhưng kỳ vọng của lập phương lợi ích cho thứ tự ngược lại, $8$ so với $13{,}5$.
