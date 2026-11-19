# Bài tập Bài 11 — Lập kế hoạch dựa trên mô hình

Tệp gồm tám bài, Bài tập 11.12–11.19, đánh số tiếp theo mười một bài tập củng cố của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html) (Bài tập 11.1–11.11) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập của Sutton và Barto (2018), ấn bản 2, ghi số bài, mục và trang. Các bài chia theo ba mức: nhận biết (11.12, 11.13); tính toán hoặc chứng minh (11.14, 11.15); vận dụng vào bài toán Học tăng cường (11.16–11.19). Tệp này không có bài cho mục tiêu học tập 5 (tối ưu kế hoạch bằng đạo hàm) và 7 (chọn cách dùng mô hình). Mục tiêu 5 được luyện ở Bài tập 11.6, 11.11 của ghi chú, mục tiêu 7 ở Bài tập 11.9, 11.10, 11.11 của ghi chú. Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu, với bài của ghi chú đứng sau chữ "ghi chú".

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Bài toán lập kế hoạch với mô hình học được | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/1/1) | — |
| 2. Tính bất định của môi trường và lập kế hoạch nền | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2/1) | 11.12, 11.13, 11.14, 11.16, 11.17, 11.19; ghi chú: 11.2, 11.4 |
| 3. Tìm kiếm theo cây Monte Carlo | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/3/1) | 11.18; ghi chú: 11.5, 11.8 |
| 4. Tối ưu kế hoạch dựa trên đạo hàm | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/4/1) | ghi chú: 11.1, 11.6, 11.11 |
| 5. Học tăng cường phân cấp | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/5/1) | 11.15; ghi chú: 11.3, 11.7, 11.9, 11.10 |
| 6. Tổng kết | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/6/1) | — |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 11; công thức của sách được ghi rõ "của sách". Thời gian rời rạc $t=0,1,\dots$; tại bước $t$, trạng thái $S_t$, hành động $A_t$, phần thưởng $R_{t+1}$ của chuyển từ $t$ sang $t+1$; $\gamma$ là hệ số chiết khấu. $Q$ là bảng giá trị hành động đang học hoặc đang lập kế hoạch, $\alpha$ là bước học, $\varepsilon$ là tham số của chính sách $\varepsilon$-tham lam, $n$ là số cập nhật lập kế hoạch sau mỗi bước thật. Dyna-Q là Thuật toán 11.10. Dyna-Q+ là Định nghĩa 11.12, với hệ số thưởng thăm dò (exploration bonus) $\kappa>0$ và $\ell(s,a)$ là số bước thật kể từ lần thử thật gần nhất của $(s,a)$.

Ký hiệu của sách khác ghi chú ở các điểm sau:

- sách viết $\tau$ cho số bước kể từ lần thử gần nhất; ở đây viết $\ell(s,a)$, vì $\tau$ dành cho thời điểm kết thúc của tùy chọn (option);
- $c$ của (2.10) của sách viết $c_{\mathrm{ucb}}$, và ước lượng $Q_t(a)$ của bài toán chọn lặp lại một bước (multi-armed bandit) viết $\bar r(a)$, như (3.2) của ghi chú;
- chính sách phân cấp (hierarchical policy) viết $\mu$ thay cho $\pi$; tốc độ phần thưởng, sách viết $r(\pi)$, ở đây viết $g(\mu)$, vì $r(s,\omega)$ đã là phần thưởng của mô hình tùy chọn.

**Mê cung lưới.** Bài tập 11.12, 11.13, 11.16, 11.17, 11.19 dùng các mê cung lưới $6\times9$ của Sutton và Barto (2018, Chương 8). Ô $(i,j)$ nằm ở hàng $i$, đếm từ trên ($1\le i\le6$), và cột $j$, đếm từ trái ($1\le j\le9$). Mỗi ô không phải tường là một trạng thái. Bốn hành động $\uparrow$, $\downarrow$, $\leftarrow$, $\rightarrow$ đưa tác tử sang ô kề theo hướng đó một cách tất định; nếu ô kề là tường hoặc nằm ngoài lưới, tác tử ở yên. Phần thưởng bằng $+1$ cho chuyển vào ô đích $\mathrm G$ và $0$ cho mọi chuyển khác. Sau khi vào $\mathrm G$, tác tử trở về ô xuất phát $\mathrm S$ và lượt mới bắt đầu; bước thật được đếm liên tục qua các lượt. Ba mê cung gồm:

- **mê cung Dyna** (Dyna maze; Ví dụ 8.1 của sách, trang 164): $\mathrm S=(3,1)$, $\mathrm G=(1,9)$; tường ở $(2,3)$, $(3,3)$, $(4,3)$, $(5,6)$, $(1,8)$, $(2,8)$, $(3,8)$; còn $47$ trạng thái; đường ngắn nhất từ $\mathrm S$ tới $\mathrm G$ dài $14$ bước;
- **mê cung bị chặn** (blocking maze; Ví dụ 8.2, trang 166): $\mathrm S=(6,4)$, $\mathrm G=(1,9)$; trong $1\,000$ bước thật đầu, tường gồm $(4,1),\dots,(4,8)$, lối qua ở $(4,9)$ và đường ngắn nhất dài $10$ bước; từ bước $1\,001$, tường gồm $(4,2),\dots,(4,9)$, lối qua ở $(4,1)$ và đường ngắn nhất dài $16$ bước;
- **mê cung lối tắt** (shortcut maze; Ví dụ 8.3, trang 167): $\mathrm S=(6,4)$, $\mathrm G=(1,9)$; trong $3\,000$ bước thật đầu, tường gồm $(4,2),\dots,(4,9)$, lối qua ở $(4,1)$ và đường ngắn nhất dài $16$ bước; từ bước $3\,001$, ô $(4,9)$ mở thêm, tường còn $(4,2),\dots,(4,8)$, đường ngắn nhất qua $(4,9)$ dài $10$ bước và đường cũ vẫn mở.

**Phần thưởng tích lũy.** Phần thưởng tích lũy (cumulative reward) tới bước $t$ là tổng phần thưởng nhận trong $t$ bước thật đầu, tức số lần tới $\mathrm G$; độ dốc của đường phần thưởng tích lũy là số lần tới đích trên một bước thật. Hình 8.4 và 8.5 của sách (trang 167) vẽ phần thưởng tích lũy, lấy trung bình qua nhiều lần chạy, của Dyna-Q và Dyna-Q+:

- Hình 8.4, mê cung bị chặn, trục hoành từ $0$ tới $3\,000$ bước: đường Dyna-Q+ nằm trên đường Dyna-Q suốt thí nghiệm; ngay sau bước $1\,000$ cả hai đường nằm ngang một đoạn, rồi tăng trở lại khi tác tử tìm ra lối mới, và sau đó đường Dyna-Q+ dốc hơn;
- Hình 8.5, mê cung lối tắt, trục hoành từ $0$ tới $6\,000$ bước: trước bước $3\,000$ hai đường gần nhau, Dyna-Q+ cao hơn một chút, và khoảng cách giữa hai đường hẹp lại một chút; sau bước $3\,000$ đường Dyna-Q+ dốc hơn rõ rệt, còn Dyna-Q giữ độ dốc cũ vì không chuyển sang lối tắt.

Số thập phân viết bằng dấu phẩy, chẳng hạn $0{,}95$; số trong mã giữ dấu chấm.

## Mức nhận biết

### Bài tập 11.12. Dyna-Q+ ở hai pha của thí nghiệm

**Mức độ:** nhận biết; mục tiêu học tập 2; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 8.2, §8.3, trang 168; Ví dụ 8.2, 8.3 và Hình 8.4, 8.5, trang 166–167; chú thích 1, trang 168.

::: exercise Bài tập 11.12 (Dyna-Q+ ở hai pha của thí nghiệm)
Hai thí nghiệm so Dyna-Q (Thuật toán 11.10) với Dyna-Q+ (Định nghĩa 11.12) trên lưới $6\times9$ với bốn hành động tất định, $\mathrm S=(6,4)$, $\mathrm G=(1,9)$, phần thưởng $+1$ khi vào $\mathrm G$ rồi trở về $\mathrm S$, tường nằm trên hàng $4$:

- mê cung bị chặn: trong $1\,000$ bước đầu, lối qua tường ở cột $9$ (đường ngắn nhất $10$ bước); từ bước $1\,001$, lối đó bị chặn và lối mới mở ở cột $1$ (đường ngắn nhất $16$ bước);
- mê cung lối tắt: trong $3\,000$ bước đầu, lối qua duy nhất ở cột $1$ (đường ngắn nhất $16$ bước); từ bước $3\,001$, cột $9$ mở thêm (đường ngắn nhất $10$ bước), lối cũ vẫn mở.

Dyna-Q+ khác Dyna-Q ở bốn điểm: sau mỗi bước thật $(S,A)$, $\ell(S,A)$ về $0$ và $\ell$ của mọi cặp khác tăng $1$; bước lập kế hoạch (f) thay phần thưởng mô phỏng $\tilde R$ bằng $\tilde R+\kappa\sqrt{\ell(\tilde S,\tilde A)}$; bước (f) chọn cả hành động chưa từng thử tại trạng thái đã gặp; mô hình khởi tạo của hành động chưa thử cho tác tử ở yên với phần thưởng $0$. Trên đồ thị phần thưởng tích lũy trung bình, đường Dyna-Q+ nằm trên đường Dyna-Q cả ở pha thứ nhất (trước khi mê cung đổi) lẫn ở pha thứ hai (sau khi mê cung đổi) của hai thí nghiệm.

- (a) Giải thích vì sao Dyna-Q+ làm tốt hơn Dyna-Q ở pha thứ nhất, khi môi trường chưa đổi.
- (b) Giải thích vì sao Dyna-Q+ làm tốt hơn Dyna-Q ở pha thứ hai của từng thí nghiệm.
:::

::: hint Gợi ý Bài tập 11.12
Ở câu (a), xét lượt đầu tiên, khi $Q\equiv0$: Dyna-Q chọn hành động thế nào, và bước (f) của Dyna-Q+ làm gì với cặp chưa thử. Ở câu (b), xác định trong mỗi thí nghiệm mô hình cũ sai theo hướng lạc quan hay bi quan (Ví dụ 11.8).
:::

::: solution Lời giải Bài tập 11.12
**Câu (a).** Ban đầu $Q\equiv0$ và mọi phần thưởng trước khi tới $\mathrm G$ bằng $0$. Với Dyna-Q, mọi hành động hòa nhau, phá hòa (tie-breaking) ngẫu nhiên, nên lượt đầu là một quá trình đi ngẫu nhiên (random walk). Bước (f) chỉ cập nhật cặp đã thử, với mục tiêu $0+\gamma\cdot0=0$, nên không đổi gì cho tới lần đầu tới $\mathrm G$.

Với Dyna-Q+, bước (f) cập nhật cả hành động chưa thử với mô hình "ở yên, thưởng $0$" và thưởng $\kappa\sqrt{\ell}$. Cặp chưa thử có $\ell$ bằng số bước thật đã trôi qua, lớn nhất trong bảng, còn cặp vừa thử có $\ell=0$. Mục tiêu lập kế hoạch của cặp chưa thử là $\kappa\sqrt{\ell}+\gamma\max_{a'}Q(s,a')>0$, nên các hành động chưa thử được ưu tiên, vì $\ell$ của chúng lớn nhất. Các cập nhật lập kế hoạch còn lan giá trị này qua mô hình về các trạng thái dẫn tới vùng có nhiều cặp chưa thử. Chính sách tham lam theo $Q$ vì vậy đưa tác tử tới các cặp chưa thử một cách có hệ thống, thay cho việc đi ngẫu nhiên. Khi tác tử thăm dò như vậy, mô hình phủ mê cung sau ít bước thật hơn, và các cập nhật lập kế hoạch tìm ra đường ngắn nhất ($10$ bước ở mê cung bị chặn, $16$ bước ở mê cung lối tắt) sớm hơn. Cơ chế này giải thích kết quả trong thí nghiệm của Sutton và Barto: đường phần thưởng tích lũy của Dyna-Q+ nằm trên đường Dyna-Q ngay từ pha thứ nhất, như mô tả Hình 8.4.

**Câu (b).** *Mê cung bị chặn.* Sau bước $1\,000$, mô hình cũ ghi $(5,9)$ với $\uparrow$ dẫn tới $(4,9)$: mô hình lạc quan. Chính sách tham lam đi tới $(5,9)$, chọn $\uparrow$ và ở yên. Bước (e) sửa mô hình, các cập nhật lập kế hoạch hạ giá trị của đường cũ. Cả hai tác tử tự sửa loại sai này (Ví dụ 11.8, "mô hình quá lạc quan"). Đoạn nằm ngang trên Hình 8.4 là lúc chúng đi quanh sau tường.

Với lối mới ở cột $1$, mô hình cũ sai theo hướng bi quan: cặp $(5,1)$ với $\uparrow$ hoặc chưa có trong mô hình, hoặc được ghi là ở yên, vì $(4,1)$ là tường trong pha thứ nhất. Dyna-Q chỉ sửa ô này của mô hình khi thăm dò $\varepsilon$-tham lam tình cờ đưa nó tới $(5,1)$ và chọn $\uparrow$. Với Dyna-Q+, cặp này lâu không được thử nên $\ell$ lớn, và thưởng $\kappa\sqrt{\ell}$ nâng giá trị lập kế hoạch của các đường dẫn tới nó; tác tử chủ động tới thử, phát hiện lối mới và lập kế hoạch đường $16$ bước sớm hơn.

*Mê cung lối tắt.* Sau bước $3\,000$, đường cũ vẫn đi được, nên chính sách tham lam không gặp thất bại nào để sửa mô hình. Các cặp dẫn vào $(4,9)$, như $(5,9)$ với $\uparrow$ và $(3,9)$ với $\downarrow$, được mô hình ghi là ở yên: mô hình bi quan. Theo Ví dụ 11.9, các cập nhật lập kế hoạch của Dyna-Q không đổi giá trị của cặp bi quan, và muốn tới thử nó, $\varepsilon$-tham lam phải chọn nhiều hành động thăm dò liên tiếp; Dyna-Q không chuyển sang lối tắt. Với Dyna-Q+, $\ell$ của các cặp đó tăng theo thời gian, nên $\kappa\sqrt{\ell}$ tăng tới khi giá trị lập kế hoạch của chuyến đi thử vượt giá trị của đường cũ; tác tử đi thử, bước (e) ghi lối mở, và bước (f) lập kế hoạch đường $10$ bước (Nhận xét 11.13).

**Kiểm tra lại.** Ba lỗi thường gặp:

- Chỉ giải thích pha thứ hai bằng việc thưởng giúp phát hiện thay đổi. Theo lời giải thích đó, hai tác tử như nhau trước khi mê cung đổi, trái với việc đường Dyna-Q+ nằm trên ở pha thứ nhất.
- Cho rằng thưởng làm bảng $Q$ của Dyna-Q+ chính xác hơn. Theo Nhận xét 11.13, bảng đó lệch khỏi $\hat q_*$ của mô hình, và lợi thế đến từ hành vi thăm dò.
- Coi lợi thế ở pha thứ nhất là tính chất chung của Dyna-Q+. Lợi thế đó phụ thuộc tham số, gồm $\kappa$ và bước học $\alpha$. Với $\kappa$ quá lớn, hoặc khi giá trị từ $\mathrm G$ lan chậm vì $\alpha$ nhỏ, thưởng của các cặp lâu chưa thử lấn át giá trị của đường tới đích, và Dyna-Q+ có thể tới đích ít hơn Dyna-Q trước khi môi trường đổi.
:::

### Bài tập 11.13. Khoảng cách giữa Dyna-Q+ và Dyna-Q trước khi có lối tắt

**Mức độ:** nhận biết; mục tiêu học tập 2; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 8.3, §8.3, trang 168; Ví dụ 8.3 và Hình 8.5, trang 167.

::: exercise Bài tập 11.13 (Khoảng cách giữa Dyna-Q+ và Dyna-Q trước khi có lối tắt)
Trên mê cung lối tắt (lưới $6\times9$, $\mathrm S=(6,4)$, $\mathrm G=(1,9)$, phần thưởng $+1$ khi vào $\mathrm G$ rồi trở về $\mathrm S$; trong $3\,000$ bước đầu lối qua tường duy nhất ở $(4,1)$, đường ngắn nhất $16$ bước; từ bước $3\,001$, ô $(4,9)$ mở thêm), Dyna-Q (Thuật toán 11.10) và Dyna-Q+ (Định nghĩa 11.12) được chạy $6\,000$ bước thật. Trên đồ thị phần thưởng tích lũy trung bình, trong $3\,000$ bước đầu đường Dyna-Q+ nằm trên đường Dyna-Q, nhưng khoảng cách giữa hai đường hẹp lại một chút.

Giải thích vì sao khoảng cách đó hẹp lại trong pha thứ nhất, khi môi trường chưa đổi.
:::

::: hint Gợi ý Bài tập 11.13
Khoảng cách giữa hai đường phần thưởng tích lũy hẹp lại khi độ dốc của đường dưới lớn hơn độ dốc của đường trên. Xét thưởng $\kappa\sqrt{\ell}$ của một cặp nằm ngoài đường ngắn nhất sau vài nghìn bước.
:::

::: solution Lời giải Bài tập 11.13
**Khoảng cách và độ dốc.** Khoảng cách giữa hai đường tại bước $t$ là hiệu số lần tới đích của hai tác tử trong $t$ bước đầu. Nó hẹp lại đúng khi, trên đoạn đó, Dyna-Q tới đích với tốc độ lớn hơn Dyna-Q+.

**Nguồn gốc của khoảng cách.** Theo Bài tập 11.12(a), Dyna-Q+ thăm dò có hệ thống nên, trong thí nghiệm của sách, tìm ra đường $16$ bước sớm hơn. Khoảng cách mở ra ở đầu thí nghiệm.

**Chi phí thăm dò khi môi trường không đổi.** Khi cả hai tác tử đã có mô hình đúng của mê cung và đã học đường ngắn nhất, môi trường không đổi cho tới bước $3\,000$, nên không còn gì mới để phát hiện. Dyna-Q đi theo đường ngắn nhất với chính sách $\varepsilon$-tham lam. Dyna-Q+ vẫn trả chi phí thăm dò: mỗi cặp nằm ngoài đường đi có $\ell$ tăng theo thời gian, nên $\kappa\sqrt{\ell}$ tăng không bị chặn; chẳng hạn khi $\ell$ tăng từ $100$ lên $2\,500$, thưởng tăng từ $10\kappa$ lên $50\kappa$. Đến lúc giá trị lập kế hoạch của một chuyến đi thử vượt giá trị của đường ngắn nhất, tác tử rời đường để thử lại cặp đó, rồi $\ell$ của cặp về $0$ trong khi $\ell$ của các cặp khác tiếp tục tăng. Các chuyến đi thử lặp lại làm lượt của Dyna-Q+ dài hơn trung bình, nên số lần tới đích trên một bước của Dyna-Q+ nhỏ hơn của Dyna-Q, và khoảng cách hẹp lại. Lợi thế ban đầu vẫn còn ở bước $3\,000$ nhưng bị bào mòn. Sau bước $3\,000$, chính các chuyến đi thử này giúp Dyna-Q+ tìm ra lối tắt (Bài tập 11.12(b)).

**Kiểm tra lại.** Ba lỗi thường gặp:

- Cho rằng Dyna-Q có mô hình tốt hơn ở cuối pha thứ nhất. Trong môi trường tất định không đổi, mô hình của cả hai tác tử đều đúng ở mọi cặp đã thử, nên khác biệt nằm ở hành vi.
- Coi thưởng thăm dò là hằng số. Khi đó chi phí thăm dò sẽ tắt dần khi mọi cặp đã được thử, và lập luận không giải thích được độ dốc thấp hơn kéo dài.
- Đọc khoảng cách hẹp lại thành việc phần thưởng tích lũy của Dyna-Q+ giảm. Phần thưởng tích lũy không bao giờ giảm, chỉ độ dốc của nó nhỏ hơn.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 11.14. Phân phối trạng thái kế lệch và cập nhật mẫu

**Mức độ:** chứng minh và tính toán; mục tiêu học tập 3; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 8.6, §8.5, trang 174; phân tích của Hình 8.7, trang 173–174. Câu (a), (b) dựng trên cùng thiết lập và dẫn tới câu hỏi của sách ở câu (c).

::: exercise Bài tập 11.14 (Phân phối trạng thái kế lệch và cập nhật mẫu)
Xét một cặp $(s,a)$ có $b$ trạng thái kế $s_1',\dots,s_b'$ với xác suất $\hat p_1,\dots,\hat p_b>0$ theo mô hình, phần thưởng bằng $0$. Giá trị kế $y_i=\gamma\max_{a'}Q(s_i',a')$ cố định trong lúc cập nhật, và mục tiêu kỳ vọng là $\bar y=\sum_i\hat p_iy_i$. Một cập nhật kỳ vọng (expected update), (2.3), tốn $b$ lần đánh giá và cho đúng $\bar y$. Một dãy $k$ cập nhật mẫu (sample update), (2.4), với bước học $\alpha_j=1/j$, mỗi cập nhật rút một trạng thái kế độc lập theo $\hat p$ và tốn một lần đánh giá, cho giá trị $Q_k$. Như Mệnh đề 11.15(b), coi $y_1,\dots,y_b$ là các biến ngẫu nhiên độc lập, cùng kỳ vọng, phương sai $1$, độc lập với việc rút mẫu. Khi $\hat p_i=1/b$ với mọi $i$, sai số căn bình phương trung bình là $\sqrt{(b-1)/(bk)}$, theo (2.5).

- (a) Chứng minh rằng với mọi phân phối $\hat p$,
$$\mathbb E(Q_k-\bar y)^2=\frac{1-\sum_i\hat p_i^2}{k}.$$
- (b) Với $b=100$, $\hat p_1=0{,}9$ và $99$ trạng thái còn lại chia đều xác suất $0{,}1$, tính sai số căn bình phương trung bình sau $k=1$ và $k=10$ cập nhật mẫu, và so với phân phối đều. Tìm $k$ nhỏ nhất để sai số không vượt $0{,}1$ trong mỗi trường hợp.
- (c) Giả sử phân phối của trạng thái kế rất lệch: một số trạng thái có xác suất lớn hơn hẳn đa số. Xác định điều đó làm mạnh thêm hay làm yếu đi lập luận ủng hộ cập nhật mẫu so với cập nhật kỳ vọng, và lập luận cho câu trả lời.
:::

::: hint Gợi ý Bài tập 11.14
Mệnh đề 11.15(a) cho $\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k$ với $\sigma^2=\sum_i\hat p_i(y_i-\bar y)^2$. Gọi $m$ là kỳ vọng chung của các $y_i$ và viết $y_i-\bar y$ thành tổ hợp tuyến tính của các $y_j-m$.
:::

::: solution Lời giải Bài tập 11.14
**Câu (a).** Theo Mệnh đề 11.15(a), với mọi giá trị cố định của $y_1,\dots,y_b$, sau $k$ cập nhật mẫu $Q_k$ là trung bình của $k$ giá trị $y_{S'_j}$ và $\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k$, với $\sigma^2=\sum_i\hat p_i(y_i-\bar y)^2$. Còn phải tính $\mathbb E\sigma^2$ theo $y$.

Gọi $m$ là kỳ vọng chung của các $y_j$. Vì $\sum_j\hat p_j=1$,
$$\begin{aligned}y_i-\bar y&=(1-\hat p_i)(y_i-m)\\&\quad-\sum_{j\ne i}\hat p_j(y_j-m).\end{aligned}$$
Các $y_j-m$ độc lập, kỳ vọng $0$, phương sai $1$, nên $\mathbb E(y_i-\bar y)=0$ và
$$\begin{aligned}\mathbb E(y_i-\bar y)^2&=(1-\hat p_i)^2+\sum_{j\ne i}\hat p_j^2\\&=1-2\hat p_i+\sum_j\hat p_j^2.\end{aligned}$$
Lấy tổng có trọng số $\hat p_i$:
$$\begin{aligned}\mathbb E\sigma^2&=\sum_i\hat p_i\Bigl(1-2\hat p_i+\sum_j\hat p_j^2\Bigr)\\&=1-2\sum_i\hat p_i^2+\sum_j\hat p_j^2\\&=1-\sum_i\hat p_i^2.\end{aligned}$$
Lấy kỳ vọng theo $y$ của đẳng thức có điều kiện cho $\mathbb E(Q_k-\bar y)^2=\mathbb E\sigma^2/k=(1-\sum_i\hat p_i^2)/k$.

Với phân phối đều, $\sum_i\hat p_i^2=1/b$ và kết quả là $(b-1)/(bk)$, đúng (2.5). Theo bất đẳng thức Cauchy–Schwarz, $\sum_i\hat p_i^2\ge(\sum_i\hat p_i)^2/b=1/b$, dấu bằng khi và chỉ khi $\hat p$ đều. Vậy với $b$ cho trước, phân phối đều cho sai số lớn nhất.

**Câu (b).** Mỗi trạng thái còn lại có xác suất $0{,}1/99$, nên
$$\begin{aligned}\sum_i\hat p_i^2&=0{,}81+99\cdot\Bigl(\frac{0{,}1}{99}\Bigr)^2\\&=0{,}81+\frac{0{,}01}{99}\\&=0{,}810101,\end{aligned}$$
và $1-\sum_i\hat p_i^2=0{,}189899$. Với phân phối đều, $1-1/100=0{,}99$. Sai số căn bình phương trung bình là $\sqrt{(1-\sum_i\hat p_i^2)/k}$:

| $k$ | phân phối lệch | phân phối đều |
|---:|---:|---:|
| $1$ | $0{,}4358$ | $0{,}9950$ |
| $10$ | $0{,}1378$ | $0{,}3146$ |

Sai số không vượt $0{,}1$ khi $(1-\sum_i\hat p_i^2)/k\le0{,}01$. Với phân phối lệch, $k\ge18{,}99$, nên $k=19$, cho $\sqrt{0{,}189899/19}=0{,}09997$. Với phân phối đều, $k\ge99$, nên $k=99$. Cập nhật kỳ vọng tốn $100$ lần đánh giá trong cả hai trường hợp.

**Câu (c).** Phân phối lệch làm mạnh thêm lập luận ủng hộ cập nhật mẫu. Chi phí của cập nhật kỳ vọng không phụ thuộc hình dạng phân phối: nó vẫn đánh giá đủ $b$ trạng thái kế, kể cả các trạng thái gần như không bao giờ xảy ra. Sai số của cập nhật mẫu thì giảm khi phân phối lệch, vì các mẫu rơi chủ yếu vào những trạng thái có xác suất lớn, cũng là những trạng thái quyết định phần lớn giá trị của $\bar y$. Câu (a) cho tỉ số sai số so với phân phối đều cùng $b$, cùng $k$, là
$$\sqrt{\frac{1-\sum_i\hat p_i^2}{(b-1)/b}}\le1;$$
ở câu (b) tỉ số này bằng $0{,}4380$, và $19$ cập nhật mẫu, tức $19\%$ chi phí của một cập nhật kỳ vọng, đã đưa sai số xuống dưới $0{,}1$. Ở giới hạn một trạng thái có xác suất gần $1$, một mẫu gần như cho đúng $\bar y$. Muốn giảm chi phí của cập nhật kỳ vọng, có thể bỏ các trạng thái kế xác suất nhỏ khỏi tổng (2.3), nhưng khi đó mục tiêu không còn đúng bằng $\bar y$. Kết luận dùng giả thiết các $y_i$ độc lập, cùng phương sai và độc lập với xác suất $\hat p_i$, như Mệnh đề 11.15(b).

**Kiểm tra lại.** Với $\hat p$ đều, câu (a) cho lại (2.5); với $b=1$, $\sum_i\hat p_i^2=1$ và sai số bằng $0$, vì chỉ có một trạng thái kế. Ba lỗi thường gặp:

- Dùng (2.5) cho phân phối lệch, được $0{,}9950$ sau một cập nhật thay cho $0{,}4358$, rồi kết luận độ lệch của phân phối không ảnh hưởng.
- Coi $y_i$ và $\bar y$ độc lập khi tính $\mathbb E(y_i-\bar y)^2$, được $1+\sum_j\hat p_j^2$ và $\mathbb E\sigma^2=1{,}810101$ ở câu (b), lớn hơn cả trường hợp phân phối đều.
- Tính chi phí của cập nhật kỳ vọng bằng số trạng thái có xác suất lớn, chẳng hạn $1$ ở câu (b). Cập nhật kỳ vọng (2.3) lấy tổng trên mọi trạng thái kế có $\hat p>0$, nên vẫn tốn $100$ lần đánh giá.
:::

### Bài tập 11.15. Tùy chọn trong thiết lập phần thưởng trung bình

**Mức độ:** chứng minh; mục tiêu học tập 6; mạch 5.

**Nguồn:** Sutton và Barto (2018), Bài tập 17.1, §17.2, trang 464; (17.2)–(17.4), trang 462–463; thiết lập phần thưởng trung bình, (10.6), (10.9) và phương trình Bellman vi phân, §10.3, trang 249–250.

::: exercise Bài tập 11.15 (Tùy chọn trong thiết lập phần thưởng trung bình)
Viết $\mathbb E_{s,\omega}$, $\Pr_{s,\omega}$ cho kỳ vọng và xác suất khi $S_0=s$ và tùy chọn đầu tiên là $\omega$. Trong thiết lập chiết khấu, mô hình của tùy chọn $\omega$ kết thúc với xác suất $1$ tại thời điểm $\tau$ là (5.1):
$$\begin{aligned}&r(s,\omega)\\&\ =\mathbb E_{s,\omega}\Bigl[\sum_{k=1}^{\tau}\gamma^{k-1}R_k\Bigr],\\&p(s'\mid s,\omega)\\&\ =\sum_{k\ge1}\gamma^k\Pr_{s,\omega}\{S_k=s',\tau=k\},\end{aligned}$$
và giá trị của chính sách phân cấp $\mu$ thỏa (5.2): $v_\mu(s)=\sum_{\omega}\mu(\omega\mid s)\bigl[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)v_\mu(s')\bigr]$ (Định lý 11.42).

Thiết lập phần thưởng trung bình (average-reward setting) xét nhiệm vụ liên tục (continuing task) trên một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn, không có trạng thái kết thúc, không chiết khấu. Mỗi tùy chọn có chính sách Markov dừng, hàm kết thúc chỉ phụ thuộc trạng thái, và từ mọi trạng thái của tập khởi đầu kết thúc với xác suất $1$, với $\mathbb E\tau<\infty$. Chính sách phân cấp $\mu$ chọn tùy chọn theo trạng thái tại mỗi thời điểm chọn và chạy tùy chọn tới khi kết thúc (Định nghĩa 11.39). *Tốc độ phần thưởng* (reward rate, average reward) của $\mu$ là
$$g(\mu)=\lim_{h\to\infty}\frac1h\sum_{t=1}^h\mathbb E_\mu[R_t\mid S_0];$$
giả thiết giới hạn này tồn tại và không phụ thuộc $S_0$ (sách viết $r(\pi)$, (10.6)). *Lợi tức vi phân* (differential return) là $G_t=\sum_{k\ge1}\bigl(R_{t+k}-g(\mu)\bigr)$, (10.9) của sách, và *giá trị vi phân* (differential value) là $v_\mu(s)=\mathbb E_\mu[G_0\mid S_0=s]$ khi tùy chọn đầu tiên được chọn tại $S_0=s$; giả thiết mọi kỳ vọng dưới đây xác định và hữu hạn. Khi tùy chọn chỉ gồm hành động một bước và $\mu=\pi$, giá trị vi phân thỏa phương trình Bellman vi phân của sách:
$$\begin{aligned}v_\pi(s)&=\sum_a\pi(a\mid s)\\&\quad\times\sum_{s',r}p(s',r\mid s,a)\\&\quad\times\bigl[r-g(\pi)+v_\pi(s')\bigr].\end{aligned}$$

- (a) Viết hai phần $r(s,\omega)$ và $p(s'\mid s,\omega)$ của mô hình tùy chọn trong thiết lập phần thưởng trung bình, tương tự (17.2) và (17.3) của sách, tức (5.1).
- (b) Viết phương trình Bellman cho giá trị vi phân $v_\mu$ của chính sách phân cấp, tương tự (17.4) của sách, tức (5.2), và chứng minh nó.
- (c) Kiểm rằng khi mọi tùy chọn là hành động một bước, phương trình ở câu (b) trở thành phương trình Bellman vi phân ở trên.
:::

::: hint Gợi ý Bài tập 11.15
Tách lợi tức vi phân tại thời điểm kết thúc $\tau$ của tùy chọn đầu tiên, như Bước 1 của chứng minh Định lý 11.42; tùy chọn chạy $\tau$ bước gốc, và mỗi bước gốc trừ $g(\mu)$ một lần.
:::

::: solution Lời giải Bài tập 11.15
**Câu (a).** Trong lợi tức vi phân, mỗi bước gốc đóng góp $R_k-g(\mu)$ và không có chiết khấu. Tùy chọn bắt đầu tại $s$ chạy $\tau$ bước gốc, nên hai phần của mô hình là
$$\begin{aligned}&r(s,\omega)\\&\ =\mathbb E_{s,\omega}\Bigl[\textstyle\sum_{k=1}^{\tau}\bigl(R_k-g(\mu)\bigr)\Bigr]\\&\ =\mathbb E_{s,\omega}\Bigl[\textstyle\sum_{k=1}^{\tau}R_k\Bigr]\\&\qquad-g(\mu)\,\mathbb E_{s,\omega}\tau,\\&p(s'\mid s,\omega)\\&\ =\textstyle\sum_{k\ge1}\Pr_{s,\omega}\{S_k=s',\tau=k\}\\&\ =\Pr_{s,\omega}\{S_\tau=s'\}.\end{aligned}$$
Đẳng thức thứ hai của $r$ dùng $\mathbb E\tau<\infty$. Phần $p$ là xác suất thật của trạng thái lúc kết thúc: $\sum_{s'}p(s'\mid s,\omega)=\Pr_{s,\omega}\{\tau<\infty\}=1$, khác Mệnh đề 11.41, nơi tổng bằng $\mathbb E[\gamma^\tau]\le\gamma$. Phần $r$ phụ thuộc $\mu$ qua $g(\mu)$, nên mô hình tùy chọn trong thiết lập này không chỉ phụ thuộc tùy chọn. Tương đương, có thể giữ ba đại lượng $\mathbb E[\sum_{k=1}^{\tau}R_k]$, $\mathbb E\tau$ và $p$, rồi ghép với $g(\mu)$ khi cần.

**Câu (b).** Phương trình là
$$\begin{aligned}&v_\mu(s)=\sum_{\omega\in\Omega(s)}\mu(\omega\mid s)\\&\quad\times\Bigl[r(s,\omega)\\&\qquad+\sum_{s'}p(s'\mid s,\omega)\,v_\mu(s')\Bigr],\end{aligned}$$
với $r$, $p$ của câu (a). Chứng minh theo các bước của Định lý 11.42.

*Bước 1 (tách lợi tức tại $\tau$).* Cố định tùy chọn đầu tiên $\omega$ chọn tại $S_0=s$. Vì $\tau<\infty$ hầu chắc chắn,
$$G_0=\sum_{k=1}^{\tau}\bigl(R_k-g(\mu)\bigr)+G_\tau,$$
với $G_\tau=\sum_{k\ge1}\bigl(R_{\tau+k}-g(\mu)\bigr)$.

*Bước 2 (phần đầu).* Theo câu (a), kỳ vọng của tổng đầu khi biết $S_0=s$ và $\omega$ là $r(s,\omega)$.

*Bước 3 (phần sau).* Trên biến cố $\{\tau=k,S_k=s'\}$, $\tau$ là một thời điểm chọn: tác tử rút tùy chọn mới theo $\mu(\cdot\mid s')$. Tùy chọn có chính sách Markov và hàm kết thúc chỉ phụ thuộc trạng thái, nên, như Bước 3 của chứng minh Định lý 11.42, phần tương lai từ bước $k$ cùng phân phối với quá trình theo $\mu$ xuất phát tại $s'$. Do đó $\mathbb E[G_\tau\mid\tau=k,S_k=s']=v_\mu(s')$, và
$$\begin{aligned}&\mathbb E_{s,\omega}[G_\tau]\\&\ =\sum_{k\ge1}\sum_{s'}\Pr_{s,\omega}\{\tau=k,S_k=s'\}\\&\qquad\times v_\mu(s')\\&\ =\sum_{s'}p(s'\mid s,\omega)\,v_\mu(s').\end{aligned}$$
Không có thừa số $\gamma^k$, vì lợi tức vi phân không chiết khấu.

*Bước 4 (gom theo $\mu$).* Tùy chọn đầu tiên được rút theo $\mu(\cdot\mid s)$; lấy trung bình của Bước 2 và Bước 3 theo $\mu(\omega\mid s)$ cho phương trình. $\square$

Phải trừ $g(\mu)$ ở mỗi bước gốc, tức trừ $g(\mu)\,\mathbb E\tau$, không trừ một lần cho cả tùy chọn. Chẳng hạn với $g(\mu)=0{,}5$, hai tùy chọn cùng cho tổng phần thưởng kỳ vọng $1$, một tùy chọn chạy $1$ bước, một tùy chọn chạy $10$ bước, có $r=1-0{,}5=0{,}5$ và $r=1-5=-4$: tùy chọn dài chiếm mười bước mà chỉ cho phần thưởng của một bước. Trừ một lần sẽ cho cả hai $r=0{,}5$, và tùy chọn dài được đánh giá ngang tùy chọn ngắn.

**Câu (c).** Với hành động một bước $a$, $\tau=1$ hầu chắc chắn, nên
$$\begin{aligned}r(s,a)&=\sum_{s',r}p(s',r\mid s,a)\,r\\&\quad-g(\pi),\\p(s'\mid s,a)&=\sum_rp(s',r\mid s,a).\end{aligned}$$
Thế vào câu (b) với $\mu=\pi$ và gộp hai tổng theo $p(s',r\mid s,a)$, dùng $\sum_{s',r}p(s',r\mid s,a)=1$ để đưa $-g(\pi)$ vào trong ngoặc:
$$\begin{aligned}v_\pi(s)&=\sum_a\pi(a\mid s)\\&\quad\times\sum_{s',r}p(s',r\mid s,a)\\&\quad\times\bigl[r-g(\pi)+v_\pi(s')\bigr],\end{aligned}$$
đúng phương trình Bellman vi phân của sách.

**Kiểm tra lại.** Vì $\sum_{s'}p(s'\mid s,\omega)=1$, cộng cùng một hằng $d$ vào mọi $v_\mu(s')$ làm vế phải tăng đúng $d$; nghĩa là $v_\mu+d$ cũng thỏa phương trình, như phương trình Bellman vi phân của sách. Ba lỗi thường gặp:

- Trừ $g(\mu)$ một lần cho cả tùy chọn, $r(s,\omega)=\mathbb E[\sum_{k=1}^{\tau}R_k]-g(\mu)$. Với ví dụ trên, hai tùy chọn khi đó cùng có $r=0{,}5$ thay cho $0{,}5$ và $-4$.
- Dùng (5.1) với $\gamma=1$, tức không trừ $g(\mu)$. Trong nhiệm vụ liên tục với $g(\mu)\ne0$, tổng phần thưởng của $t$ bước đầu tăng cỡ $g(\mu)\,t$, nên giá trị không xác định.
- Trừ tốc độ phần thưởng $g_\omega$ của chính sách bên trong $\pi_\omega$ thay cho $g(\mu)$. Khi đó $r(s,\omega)$ lệch $\bigl(g(\mu)-g_\omega\bigr)\mathbb E_{s,\omega}\tau$ so với câu (a), khác nhau giữa các tùy chọn, và $v_\mu$ không còn thỏa phương trình. Lợi tức vi phân được định nghĩa so với tốc độ của chính sách phân cấp, nên mọi tùy chọn trừ cùng một $g(\mu)$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 11.16. Bootstrap nhiều bước so với Dyna-Q trên mê cung Dyna

**Mức độ:** vận dụng; mục tiêu học tập 2; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 8.1, §8.2, trang 166; Ví dụ 8.1 và Hình 8.2, 8.3, trang 164–165; Sarsa $n$ bước, (7.4)–(7.5), §7.2, trang 146.

::: exercise Bài tập 11.16 (Bootstrap nhiều bước so với Dyna-Q trên mê cung Dyna)
Mê cung Dyna là lưới $6\times9$ với tường ở $(2,3)$, $(3,3)$, $(4,3)$, $(5,6)$, $(1,8)$, $(2,8)$, $(3,8)$ (hàng đếm từ trên, cột đếm từ trái), $47$ trạng thái, $\mathrm S=(3,1)$, $\mathrm G=(1,9)$. Bốn hành động tất định; đụng tường hay biên thì ở yên; phần thưởng $+1$ khi vào $\mathrm G$, $0$ ở mọi chuyển khác; sau khi vào $\mathrm G$ tác tử trở về $\mathrm S$; $\gamma=0{,}95$; đường ngắn nhất dài $14$ bước. Các tác tử Dyna-Q (Thuật toán 11.10) dùng $Q\equiv0$ ban đầu, $\alpha=0{,}1$, $\varepsilon=0{,}1$, phá hòa ngẫu nhiên. Với cùng hạt giống (random seed) cho bộ sinh số ngẫu nhiên, lượt thứ nhất giống nhau cho mọi $n$ và dài khoảng $1\,700$ bước. Tác tử không lập kế hoạch ($n=0$, tức Q-learning một bước) cần khoảng $25$ lượt để đạt hiệu năng gần tối ưu, tác tử $n=5$ khoảng $5$ lượt, tác tử $n=50$ khoảng $3$ lượt. Ở giữa lượt thứ hai, chính sách tham lam của tác tử $n=0$ chỉ có một hành động đã học, tại ô ngay dưới $\mathrm G$; chính sách của tác tử $n=50$ đã có hành động tham lam ở phần lớn các ô, trong khi tác tử vẫn còn ở gần $\mathrm S$; tới cuối lượt, các hành động tham lam đó gần dẫn được từ $\mathrm S$ tới $\mathrm G$.

Phương pháp bootstrap nhiều bước (multi-step bootstrapping) được xét là Sarsa $k$ bước (n-step Sarsa; sách viết $n$ bước). Lợi tức $k$ bước có dạng của Định nghĩa 10.11, với bảng $Q$ ở chỗ hàm giá trị:
$$\begin{aligned}G_{t:t+k}&=R_{t+1}+\gamma R_{t+2}+\dots\\&\quad+\gamma^{k-1}R_{t+k}\\&\quad+\gamma^kQ(S_{t+k},A_{t+k}),\end{aligned}$$
và $G_{t:t+k}=G_t$ khi $t+k\ge T$; cập nhật $Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha\bigl[G_{t:t+k}-Q(S_t,A_t)\bigr]$ được làm ở bước $t+k$, khi đã biết $R_{t+k}$, $S_{t+k}$, $A_{t+k}$; các cập nhật còn lại làm khi lượt kết thúc. Mọi cặp khác giữ nguyên giá trị.

- (a) Với $Q\equiv0$ ban đầu, xác định những cặp có $Q\ne0$ sau lượt thứ nhất của Sarsa $k$ bước.
- (b) Xác định một phương pháp bootstrap nhiều bước như vậy có thể làm tốt bằng Dyna-Q với $n=50$ trên mê cung này hay không, và giải thích vì sao.
:::

::: hint Gợi ý Bài tập 11.16
Ở câu (a), trong lượt thứ nhất mọi phần thưởng bằng $0$ trừ $R_T=1$; xét mục tiêu $G_{t:t+k}$ khi $t+k<T$ và khi $t+k\ge T$. Ở câu (b), so những cặp mỗi phương pháp cập nhật trong lượt thứ hai, và nêu rõ so theo số lượt thật hay theo số phép tính.
:::

::: solution Lời giải Bài tập 11.16
**Câu (a).** Các cập nhật được làm theo thứ tự $t=0,1,\dots$. Với $t+k<T$, mọi phần thưởng $R_{t+1},\dots,R_{t+k}$ bằng $0$, nên $G_{t:t+k}=\gamma^kQ(S_{t+k},A_{t+k})$. Quy nạp theo $t$: chừng nào chưa có cập nhật nào với mục tiêu khác $0$, mọi giá trị trong bảng vẫn bằng $0$, nên mục tiêu của các cập nhật với $t<T-k$ bằng $0$ và các cập nhật đó không đổi bảng. Với $T-k\le t\le T-1$, $G_{t:t+k}=G_t=\gamma^{T-t-1}$, khác $0$. Vậy sau lượt thứ nhất, chỉ các cặp $(S_t,A_t)$ với $T-k\le t\le T-1$, không quá $k$ cặp nằm ở đoạn cuối của quỹ đạo, có $Q\ne0$. Với $k=1$ chỉ còn cặp cuối, đúng như tác tử $n=0$ chỉ học được một hành động tại ô ngay dưới $\mathrm G$.

**Câu (b).** Theo số lượt thật trên mê cung tất định này: không, phương pháp $k$ bước có thể tốt hơn Q-learning một bước nhưng không bằng Dyna-Q với $n=50$. Lý do nằm ở những cặp mỗi phương pháp cập nhật:

- Sarsa $k$ bước chỉ cập nhật cặp trên quỹ đạo thật, mỗi cặp vào lúc $k$ bước sau khi nó xảy ra, theo đúng thứ tự đã đi. Trong lượt thứ hai, giá trị chỉ lan về các cặp mà tác tử đi qua trong vòng $k$ bước trước khi chạm vào một cặp đã có giá trị; mỗi lượt nối thêm khoảng $k$ bước dọc đường tác tử thực sự đi.
- Mỗi mẫu chuyển thật chỉ đi vào không quá $k$ cập nhật, làm trong vòng $k$ bước sau khi nó xảy ra, rồi bị bỏ. Một mẫu chuyển của lượt thứ nhất, như "ô $x$ với $\rightarrow$ dẫn tới ô $y$", không được dùng lại khi giá trị của $y$ thay đổi ở lượt thứ hai.
- Phương pháp $k$ bước không ghép được các đoạn của những lượt khác nhau. Dyna-Q lưu mọi mẫu chuyển đã gặp trong mô hình; ở lượt thứ hai, sau mỗi bước thật, $50$ cập nhật lập kế hoạch trên các cặp đã thử trong lượt thứ nhất dài khoảng $1\,700$ bước lan giá trị từ $\mathrm G$ ngược qua mô hình, bất kể tác tử đang ở đâu. Chính sách tham lam vì vậy phủ phần lớn mê cung khi tác tử còn gần $\mathrm S$.

Lấy $k$ rất lớn, tới Monte Carlo ($k\ge T$), thì sau lượt thứ nhất mọi cặp trên quỹ đạo đều có giá trị, nhưng các mục tiêu là $\gamma^{T-t-1}$, nên giá trị phụ thuộc thời điểm $t$ tác tử đi qua cặp trong lượt thứ nhất, một quỹ đạo gần như đi ngẫu nhiên dài khoảng $1\,700$ bước, chứ không phụ thuộc khoảng cách ngắn nhất tới $\mathrm G$. Chính sách tham lam đi theo các hướng tác tử đã đi, không theo đường $14$ bước, và cần thêm nhiều lượt để sửa. Chỉ Dyna-Q, nhờ mô hình, tính được giá trị theo đường ngắn nhất trên những chuyển đã biết mà không phải đi lại đường đó.

Kết luận phụ thuộc đơn vị so sánh. Dyna-Q với $n=50$ làm $51$ cập nhật mỗi bước thật, còn Sarsa $k$ bước làm một cập nhật. Khi bước thật rẻ và phép tính đắt, so theo số phép tính có thể cho kết quả khác. Lợi thế của Dyna-Q cũng dựa trên mô hình đúng: mê cung tất định và không đổi, nên mỗi chuyển đã thử được mô hình ghi đúng.

**Kiểm tra lại.** Với $k=1$, câu (a) cho lại Hình 8.3 của sách: chỉ cặp cuối được học sau lượt thứ nhất. Ba lỗi thường gặp:

- Cho rằng Monte Carlo ($k\ge T$) cho đường ngắn nhất sau một lượt. Giá trị khi đó phụ thuộc thời điểm tác tử đi qua cặp trên quỹ đạo $1\,700$ bước, nên chính sách tham lam lặp lại các đường vòng đã đi.
- Quên rằng phương pháp $k$ bước chỉ cập nhật cặp trên quỹ đạo thật, rồi kết luận nó lan giá trị khắp mê cung như bước (f) của Dyna-Q.
- So hai phương pháp mà không nêu đơn vị. "Dyna-Q cần ít lượt hơn" đúng theo số bước thật, nhưng mỗi bước thật của Dyna-Q tốn $51$ cập nhật.
:::

### Bài tập 11.17. Dyna-Q cho môi trường ngẫu nhiên và môi trường thay đổi

**Mức độ:** vận dụng; mục tiêu học tập 1 và 2; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 8.5, §8.3, trang 168; giả mã Dyna-Q dạng bảng, trang 164; Ví dụ 8.2, 8.3, trang 166–167.

::: exercise Bài tập 11.17 (Dyna-Q cho môi trường ngẫu nhiên và môi trường thay đổi)
Ở bước (e) của Dyna-Q dạng bảng (Thuật toán 11.10), mô hình ghi đè $\mathrm{Model}(S,A)\leftarrow(R,S')$; bước (f) lấy $(\tilde R,\tilde S')=\mathrm{Model}(\tilde S,\tilde A)$ cho một cặp đã thử chọn ngẫu nhiên. Thuật toán giả thiết môi trường tất định. Môi trường thay đổi được xét là hai mê cung $6\times9$ có $\mathrm S=(6,4)$, $\mathrm G=(1,9)$ và tường trên hàng $4$: mê cung bị chặn, lối qua ở cột $9$ bị chặn sau bước $1\,000$ và lối mới mở ở cột $1$; mê cung lối tắt, chỉ có lối ở cột $1$ tới bước $3\,000$, sau đó cột $9$ mở thêm.

- (a) Nêu cách sửa Dyna-Q để xử lý môi trường ngẫu nhiên.
- (b) Chỉ ra sửa đổi ở câu (a) có thể làm việc kém thế nào trong môi trường thay đổi như hai mê cung trên.
- (c) Nêu cách sửa Dyna-Q để xử lý cả môi trường ngẫu nhiên lẫn môi trường thay đổi.
:::

::: hint Gợi ý Bài tập 11.17
Ở câu (a), xét bước (e) giữ lại gì khi cùng một cặp cho nhiều trạng thái kế khác nhau. Ở câu (b), xét một cặp đã thử $20$ lần trong môi trường cũ, lần nào cũng tới cùng một trạng thái kế, rồi môi trường đổi: tính $\hat p$ sau $j$ lần thử mới. Ở câu (c), xét những lần thử nào còn phản ánh môi trường hiện tại, và cặp nào không bao giờ được thử lại.
:::

::: solution Lời giải Bài tập 11.17
**Câu (a).** Thay mô hình ghi đè bằng mô hình đếm (count-based model, Định nghĩa 11.4), như đoạn "Trong thực hành" sau Thuật toán 11.10. Ở bước (e), tăng $C(S,A)$ và $C(S,A,S')$ thêm $1$ và cộng $R$ vào tổng phần thưởng của cặp. Ở bước (f), rút $\tilde S'$ theo $\hat p(\cdot\mid\tilde S,\tilde A)$, dùng $\tilde R=\hat r(\tilde S,\tilde A)$, rồi làm cập nhật mẫu (2.4). Mục tiêu kỳ vọng không đổi, vì cập nhật tuyến tính theo $\tilde R$. Cách khác là làm cập nhật kỳ vọng (2.3) trên $\hat p$, tốn $b$ lần đánh giá với $b$ là số trạng thái kế đã thấy. Khi môi trường dừng và số lần thử cố định, $\hat p$ không chệch và có độ lệch chuẩn $\sqrt{p(1-p)/C(s,a)}$ (Mệnh đề 11.5).

**Câu (b).** Mô hình đếm gộp mọi lần thử từ đầu, nên giả thiết "cùng phân phối" của Mệnh đề 11.5 bị vi phạm khi môi trường đổi, và $\hat p$ trộn xác suất cũ với xác suất mới. Hai cách hỏng:

- *Thích nghi chậm với thay đổi xấu đi.* Ở mê cung bị chặn, giả sử cặp $(5,9)$ với $\uparrow$ đã được thử $20$ lần trước bước $1\,000$, lần nào cũng tới $(4,9)$. Sau khi lối bị chặn, mỗi lần thử mới cho kết quả ở yên. Sau $j$ lần thử mới, xác suất ước lượng của việc tới $(4,9)$ là
$$\hat p_j=\frac{20}{20+j},$$
còn ít nhất $0{,}5$ tới $j=20$ và chỉ xuống dưới $0{,}1$ khi $j>180$. Trong suốt thời gian đó, các cập nhật lập kế hoạch vẫn coi lối cũ là đi được với xác suất lớn, nên tác tử quay lại thử nhiều lần. Mô hình ghi đè của Dyna-Q sửa sai này chỉ sau một lần thử.
- *Không phát hiện thay đổi tốt lên.* Ở mê cung lối tắt, các cặp dẫn vào $(4,9)$ được ghi là ở yên với $\hat p=1$. Như Dyna-Q (Ví dụ 11.8), chính sách tham lam không thử lại cặp bi quan, nên mô hình đếm không bao giờ nhận dữ liệu mới về chúng.

**Câu (c).** Một cách sửa gồm hai phần.

*Bộ đếm có quên* (trung bình có trọng số giảm theo tuổi, exponential recency-weighted average). Mỗi lần thử $(s,a)$, nhân $C(s,a)$, mọi $C(s,a,\cdot)$ và tổng phần thưởng của cặp với $\phi\in(0,1)$ trước khi cộng lần thử mới. Lần thử thứ $i$ tính từ lần gần nhất ($i=0,1,\dots$) có trọng số $\phi^i$, và $\hat p$ là tỉ số của hai bộ đếm có trọng số. Ở ví dụ của câu (b), $20$ lần thử cũ thành công và $j$ lần thử mới ở yên có tổng trọng số $\sum_{i=j}^{j+19}\phi^i$ và $\sum_{i=0}^{j-1}\phi^i$, nên
$$\hat p=\frac{\phi^j(1-\phi^{20})}{1-\phi^{j+20}}.$$
Với $\phi=0{,}9$, $\hat p=0{,}5588$ khi $j=5$ và $0{,}4991$ khi $j=6$: $\hat p$ xuống dưới $0{,}5$ sau $6$ lần thử mới thay vì $21$, và dưới $0{,}1$ sau $21$ lần thay vì $181$. Cái giá là phương sai: trong môi trường dừng, với các lần thử độc lập, $\hat p$ có phương sai
$$\begin{aligned}&p(1-p)\frac{\sum_i\phi^{2i}}{\bigl(\sum_i\phi^i\bigr)^2}\\&\quad\to p(1-p)\frac{1-\phi}{1+\phi}\end{aligned}$$
khi số lần thử tăng, nên độ lệch chuẩn không giảm về $0$ như Mệnh đề 11.5. Với $\phi=0{,}9$, giới hạn này bằng phương sai của mô hình đếm không quên với $C=19$ lần thử; khi $p=0{,}8$, độ lệch chuẩn dừng ở $\sqrt{0{,}16/19}=0{,}0918$. Cửa sổ trượt (sliding window) gồm $M$ lần thử gần nhất cho cùng đánh đổi: $M$ nhỏ thích nghi nhanh nhưng phương sai lớn.

*Thưởng thăm dò.* Bộ đếm có quên chỉ sửa được cặp mà tác tử còn thử. Để phát hiện lối tắt, thêm thưởng $\kappa\sqrt{\ell(s,a)}$ vào phần thưởng mô phỏng ở bước (f) như Dyna-Q+ (Định nghĩa 11.12), để các cặp lâu chưa thử được thử lại.

Tham số $\phi$ (hoặc $M$) cân bằng hai loại sai: quên chậm thì sai vì dữ liệu cũ, quên nhanh thì sai vì ít dữ liệu. Tham số $\kappa$ cân bằng chi phí thăm dò với tốc độ phát hiện thay đổi (Bài tập 11.13).

**Kiểm tra lại.** Khi $\phi\to1$, $\phi^j(1-\phi^{20})/(1-\phi^{j+20})\to20/(20+j)$, đúng công thức của câu (b). Ba lỗi thường gặp:

- Giữ bước (e) ghi đè trong môi trường ngẫu nhiên. Mô hình khi đó coi kết cục gần nhất là chắc chắn: sau một lần trượt tại cặp có xác suất đi đúng $0{,}8$, mô hình ghi ở yên với xác suất $1$.
- Bỏ hẳn dữ liệu cũ, tức chỉ giữ lần thử gần nhất. Đó lại là mô hình ghi đè, với $\hat p\in\{0,1\}$ và độ lệch chuẩn $\sqrt{p(1-p)}=0{,}4$ khi $p=0{,}8$ (Mệnh đề 11.5 với $C=1$).
- Cho rằng bộ đếm có quên đủ cho môi trường thay đổi. Bộ đếm đó sửa nhanh hơn các sai lạc quan nhưng không sửa sai bi quan ở cặp không được thử lại, nên vẫn cần thưởng thăm dò.
:::

### Bài tập 11.18. Đỉnh ở bước thứ mười một của quy tắc cận tin cậy trên

**Mức độ:** vận dụng; mục tiêu học tập 4; mạch 3.

**Nguồn:** Sutton và Barto (2018), Bài tập 2.8, §2.7, trang 36; bộ thử mười tay, §2.3, trang 28–29; (2.10), trang 35; Hình 2.4, trang 36.

::: exercise Bài tập 11.18 (Đỉnh ở bước thứ mười một của quy tắc cận tin cậy trên)
Bộ thử mười tay (10-armed testbed) gồm $2\,000$ bài toán chọn lặp lại một bước độc lập. Mỗi bài toán có $10$ hành động; giá trị thật $q_*(a)$, $a=1,\dots,10$, được rút độc lập theo $\mathcal N(0,1)$ khi tạo bài toán; mỗi lần chọn $a$, phần thưởng được rút theo $\mathcal N\bigl(q_*(a),1\bigr)$. Mỗi phương pháp chạy $1\,000$ bước trên mỗi bài toán, và hiệu năng ở bước $t$ là phần thưởng ở bước $t$ lấy trung bình trên $2\,000$ bài toán. Quy tắc cận tin cậy trên (upper confidence bound, UCB) của Định nghĩa 11.23, công thức (3.2), chọn
$$\begin{aligned}A_t\in\arg\max_a\Bigl[&\bar r(a)\\&+c_{\mathrm{ucb}}\sqrt{\frac{\ln t}{N(a)}}\Bigr],\end{aligned}$$
với $N(a)$ là số lần đã chọn $a$ trước bước $t$, $\bar r(a)$ là trung bình mẫu, hành động có $N(a)=0$ có chỉ số $+\infty$, phá hòa ngẫu nhiên. Với $c_{\mathrm{ucb}}=2$, đường hiệu năng của quy tắc này nằm quanh $0$ ở bước $1$–$10$, có một đỉnh rõ ở bước $11$, giảm ở các bước ngay sau, rồi tăng dần và nằm trên đường của chính sách $\varepsilon$-tham lam với $\varepsilon=0{,}1$ ở phần lớn $1\,000$ bước.

- (a) Giải thích vì sao phần thưởng trung bình tăng vọt ở bước $11$.
- (b) Giải thích vì sao nó giảm ở các bước sau đó.
- (c) Với $c_{\mathrm{ucb}}=1$, đỉnh kém rõ hơn. Giải thích vì sao.
:::

::: hint Gợi ý Bài tập 11.18
Ở bước $11$, mọi hành động có $N(a)=1$. Ở bước $12$, so số hạng thăm dò của hành động vừa chọn hai lần với số hạng của hành động mới chọn một lần, dùng $\ln12$.
:::

::: solution Lời giải Bài tập 11.18
**Câu (a).** Ở bước $1$–$10$, luôn còn hành động có $N(a)=0$ với chỉ số $+\infty$, nên mỗi hành động được chọn đúng một lần, theo thứ tự ngẫu nhiên. Phần thưởng ở mỗi bước này là phần thưởng của một hành động chọn đều, có kỳ vọng $\mathbb E\,q_*(a)=0$: đường hiệu năng nằm quanh $0$.

Ở bước $11$, mọi hành động có $N(a)=1$, nên số hạng thăm dò $c_{\mathrm{ucb}}\sqrt{\ln11}$ bằng nhau và quy tắc chọn hành động có mẫu đầu $Y_a=q_*(a)+\xi_a$ lớn nhất, với $\xi_a\sim\mathcal N(0,1)$ độc lập. Mẫu đầu là thông tin về $q_*$: cặp $(q_*(a),Y_a)$ có phân phối chuẩn với $\operatorname{Cov}(q_*(a),Y_a)=1$, $\operatorname{Var}Y_a=2$, và các cặp độc lập giữa các hành động, nên $\mathbb E[q_*(a)\mid Y_1,\dots,Y_{10}]=Y_a/2$. Hành động được chọn chỉ phụ thuộc các $Y$, nên
$$\begin{aligned}\mathbb E\,q_*(A_{11})&=\tfrac12\,\mathbb E\max_aY_a\\&=\tfrac{\sqrt2}{2}\,\mathbb E\max_aZ_a,\end{aligned}$$
với $Z_1,\dots,Z_{10}$ là các biến chuẩn tắc độc lập và $\mathbb E\max_aZ_a=1{,}5388$. Phần thưởng trung bình ở bước $11$ vì vậy nhảy từ $0$ lên $1{,}0881$, so với $\mathbb E\max_aq_*(a)=1{,}5388$ của hành động tốt nhất.

**Câu (b).** Ở bước $12$, hành động $A_{11}$ có $N=2$, các hành động khác có $N=1$, và $t=12$. Hai điều làm chỉ số của $A_{11}$ tụt so với các hành động khác:

- số hạng thăm dò của nó là $c_{\mathrm{ucb}}\sqrt{\ln12/2}$, của hành động khác là $c_{\mathrm{ucb}}\sqrt{\ln12}$; với $\sqrt{\ln12}=\sqrt{2{,}4849}=1{,}5764$, chênh lệch là $c_{\mathrm{ucb}}\sqrt{\ln12}\,(1-1/\sqrt2)$, bằng $0{,}9234$ khi $c_{\mathrm{ucb}}=2$;
- $A_{11}$ được chọn vì mẫu đầu lớn nhất, nên mẫu đầu đó ước lượng quá cao: $\mathbb E\max_aY_a=\sqrt2\cdot1{,}5388=2{,}1761$, còn mẫu thứ hai có kỳ vọng $\mathbb E\,q_*(A_{11})=1{,}0881$; trung bình hai mẫu có kỳ vọng $1{,}6321$, nhỏ hơn kỳ vọng của mẫu đầu $0{,}5440$.

Vì vậy, ở bước $12$, quy tắc chọn lại $A_{11}$ chỉ với xác suất $0{,}186$, ước lượng bằng mô phỏng $2\cdot10^7$ bài toán với sai số chuẩn $0{,}0001$. Với xác suất còn lại, quy tắc chuyển sang một hành động có mẫu đầu nhỏ hơn, có $q_*$ kỳ vọng nhỏ hơn, và phần thưởng trung bình giảm. Ở các bước tiếp theo, các hành động có mẫu đầu lớn lần lượt được chọn lần thứ hai và bị cùng hai hiệu ứng, nên quy tắc tiếp tục thăm dò các hành động kém hơn trong vài bước, trước khi các ước lượng đủ mẫu để hiệu năng tăng dần.

**Câu (c).** Lựa chọn ở bước $11$ không phụ thuộc $c_{\mathrm{ucb}}$, nên chiều cao của đỉnh giữ nguyên. Với $c_{\mathrm{ucb}}=1$, chênh lệch số hạng thăm dò ở bước $12$ chỉ còn $0{,}4617$, nên hành động $A_{11}$ được chọn lại ở bước $12$ với xác suất $0{,}360$ (cùng mô phỏng), gần gấp đôi so với $c_{\mathrm{ucb}}=2$, và hiệu năng sau bước $11$ giảm ít. Đỉnh kém rõ vì phần sau nó không tụt sâu.

**Kiểm tra lại.** Một mô phỏng $200\,000$ bài toán (bộ sinh `numpy.random.default_rng(0)`; sai số chuẩn khoảng $0{,}003$ mỗi điểm) cho phần thưởng trung bình $1{,}092$ ở bước $11$, gần giá trị $1{,}0881$ ở câu (a); ở bước $12$ là $0{,}927$ khi $c_{\mathrm{ucb}}=2$ và $1{,}044$ khi $c_{\mathrm{ucb}}=1$; với $c_{\mathrm{ucb}}=2$, giá trị nhỏ nhất sau đỉnh là $0{,}801$ ở bước $16$. Xác suất chọn lại $A_{11}$ ở bước $12$ là $0{,}186$ khi $c_{\mathrm{ucb}}=2$ và $0{,}360$ khi $c_{\mathrm{ucb}}=1$ ($20$ khối $10^6$ bài toán, `default_rng(0)` tới `default_rng(19)`). Ba lỗi thường gặp:

- Dùng $\ln11$ ở bước $12$, được chênh lệch $0{,}9071$ thay cho $0{,}9234$. Theo (3.2), $t$ là chỉ số của bước đang chọn và $N(a)$ đếm các lần chọn trước bước đó.
- Cho rằng ở bước $11$ quy tắc chọn đúng hành động tốt nhất. Theo mô phỏng trên, xác suất đó chỉ khoảng $0{,}43$, và phần thưởng kỳ vọng $1{,}0881$ thấp hơn $1{,}5388$.
- Cho rằng $c_{\mathrm{ucb}}$ đổi lựa chọn ở bước $11$. Khi mọi $N(a)$ bằng nhau, số hạng thăm dò như nhau với mọi $c_{\mathrm{ucb}}$.
:::

### Bài tập 11.19. Thưởng thăm dò chỉ dùng khi chọn hành động [Lập trình]

**Mức độ:** vận dụng; mục tiêu học tập 2; mạch 2.

**Nguồn:** Sutton và Barto (2018), Bài tập 8.4, §8.3, trang 168; Ví dụ 8.2, 8.3 và Hình 8.4, 8.5, trang 166–167; chú thích 1, trang 168.

::: exercise Bài tập 11.19 (Thưởng thăm dò chỉ dùng khi chọn hành động)
Thưởng thăm dò của Dyna-Q+ (Định nghĩa 11.12) làm thay đổi giá trị ước lượng $Q$ của các cặp trạng thái–hành động (Nhận xét 11.13). Xét một cách dùng khác: thưởng $\kappa\sqrt{\ell}$ không đi vào cập nhật nào mà chỉ dùng khi chọn hành động. Tác tử luôn chọn
$$\begin{aligned}A_t\in\arg\max_a\Bigl[&Q(S_t,a)\\&+\kappa\sqrt{\ell(S_t,a)}\Bigr],\end{aligned}$$
còn các bước (c)–(f) như Dyna-Q (Thuật toán 11.10). Dùng hai mê cung $6\times9$ có $\mathrm S=(6,4)$, $\mathrm G=(1,9)$ (hàng đếm từ trên, cột đếm từ trái), bốn hành động tất định, đụng tường hay biên thì ở yên, phần thưởng $+1$ khi vào $\mathrm G$ rồi trở về $\mathrm S$, $0$ ở mọi chuyển khác:

- mê cung lối tắt: trong $3\,000$ bước thật đầu, tường gồm $(4,2),\dots,(4,9)$ (đường ngắn nhất $16$ bước); từ bước $3\,001$, tường còn $(4,2),\dots,(4,8)$ (đường ngắn nhất $10$ bước qua $(4,9)$, đường cũ vẫn mở); chạy $6\,000$ bước;
- mê cung bị chặn: trong $1\,000$ bước thật đầu, tường gồm $(4,1),\dots,(4,8)$ (đường ngắn nhất $10$ bước); từ bước $1\,001$, tường gồm $(4,2),\dots,(4,9)$ (đường ngắn nhất $16$ bước); chạy $3\,000$ bước.

- (a) Cài đặt Dyna-Q, Dyna-Q+ và tác tử chỉ dùng thưởng khi chọn hành động trên hai mê cung.
- (b) Chạy thí nghiệm với nhiều hạt giống chung cho các tác tử; báo cáo phần thưởng tích lũy (trung bình và sai số chuẩn) ở thời điểm môi trường đổi và ở cuối, và chính sách tham lam cuối cùng có đi đường ngắn nhất mới hay không.
- (c) Từ kết quả, xác định việc đưa thưởng vào cập nhật có cần thiết không, và nêu điểm mạnh, điểm yếu của cách chỉ dùng thưởng khi chọn hành động, kèm điều kiện của từng kết luận.
:::

::: hint Gợi ý Bài tập 11.19
Kiểm mã bằng một bước tính tay trước khi chạy cả thí nghiệm, chẳng hạn cập nhật Dyna-Q+ của Ví dụ 11.9. So ghép cặp theo hạt giống. Thêm một biến thể có $\varepsilon$-tham lam quanh $Q+\kappa\sqrt{\ell}$ để tách tác dụng của thưởng khỏi việc bỏ $\varepsilon$. Ngoài phần thưởng tích lũy, đo số lần tới đích trong $1\,000$ bước cuối, vì phần thưởng tích lũy còn mang lợi thế của pha thứ nhất.
:::

::: solution Lời giải Bài tập 11.19
**Câu (a).** Bốn tác tử, cùng mô hình tất định ghi đè, $Q\equiv0$ ban đầu (cả tại $\mathrm G$, coi là trạng thái kết thúc), $\gamma=0{,}95$, $n=50$:

- (A) Dyna-Q: Thuật toán 11.10, $\varepsilon$-tham lam theo $Q$ với $\varepsilon=0{,}1$; bước (f) chọn đều một trạng thái đã gặp rồi chọn đều một hành động đã thử tại đó;
- (B) Dyna-Q+: Định nghĩa 11.12, $\varepsilon$-tham lam theo $Q$ với $\varepsilon=0{,}1$; bước (f) chọn đều một trạng thái đã gặp rồi chọn đều một trong bốn hành động, cộng $\kappa\sqrt{\ell}$ vào phần thưởng mô phỏng; khi một trạng thái được gặp lần đầu, mô hình của các hành động chưa thử tại đó là "ở yên, phần thưởng $0$";
- (C) tác tử của đề: bước (d)–(f) như (A), không có thưởng trong cập nhật; chọn $A_t\in\arg\max_a[Q(S_t,a)+\kappa\sqrt{\ell(S_t,a)}]$, không có $\varepsilon$;
- (C′) như (C) nhưng $\varepsilon$-tham lam quanh $Q+\kappa\sqrt{\ell}$ với $\varepsilon=0{,}1$.

Với mọi tác tử, $\ell(s,a)$ là số bước thật kể từ lần thử thật gần nhất của $(s,a)$, đếm từ bước $0$ với cặp chưa từng thử; $\ell$ chỉ đổi theo bước thật, không theo cập nhật lập kế hoạch. Phép $\arg\max$ phá hòa ngẫu nhiên. Mỗi lần chạy dùng một bộ sinh số ngẫu nhiên `random.Random(seed)` của Python, với `seed` là hạt giống, cho bước $\varepsilon$, phá hòa và chọn cặp lập kế hoạch; cùng tập hạt giống dùng cho mọi tác tử.

Trước khi chạy, mã được kiểm bằng `assert` trên các phép tính tay:

- cập nhật Dyna-Q+ của Ví dụ 11.9 ($\kappa=0{,}01$, $\ell=400$, $Q(\mathrm B,\rightarrow)=0{,}54$, $\max_aQ(\mathrm B,a)=0{,}6$, $\alpha=0{,}5$, $\gamma=0{,}9$) cho thưởng $0{,}2$ và giá trị mới $0{,}64$;
- với $Q(S_t,\cdot)=(0{,}30;\,0{,}28;\,0{,}10;\,0{,}10)$, $\ell=(5;\,400;\,400;\,2\,500)$, $\kappa=10^{-3}$, các chỉ số của (C) là $0{,}3022$, $0{,}3$, $0{,}12$, $0{,}15$, nên (C) chọn hành động thứ nhất; đổi $\ell$ của hành động thứ hai thành $2\,500$ thì chỉ số của nó thành $0{,}33$ và (C) chọn nó;
- tìm kiếm theo chiều rộng cho đường ngắn nhất $16$ rồi $10$ bước ở mê cung lối tắt, $10$ rồi $16$ bước ở mê cung bị chặn.

Ở mê cung bị chặn, nếu lúc đổi tác tử đang đứng ở ô $(4,9)$ vừa thành tường, mã giữ tác tử ở đó và cho nó đi tiếp theo bảng chuyển như ở mọi ô; với $\kappa=10^{-3}$, điều này xảy ra ở $1$ tới $4$ trên $30$ lần chạy của (A), (B), (C), và ở $7$ lần chạy của (C′) khi $\alpha=0{,}1$, $0$ lần khi $\alpha=1$.

**Câu (b).** *Thước đo.* Phần thưởng tích lũy ở bước đổi môi trường và ở cuối; số lần tới đích trong $1\,000$ bước cuối; số lần chạy mà chính sách tham lam theo $Q$ ở bước cuối đi đường ngắn nhất mới. Chính sách tham lam được thử trên mê cung sau khi đổi, từ $\mathrm S$, tối đa $100$ bước, phá hòa theo thứ tự $\uparrow,\downarrow,\leftarrow,\rightarrow$. Mỗi ô của bảng là trung bình $\pm$ sai số chuẩn trên $30$ hạt giống $0,\dots,29$; hiệu ghép cặp tính trên cùng hạt giống.

*Các lần chạy.* Mọi lần chạy dùng để chọn và kiểm cấu hình như sau:

1. một lần chạy mỗi tác tử với hạt giống $0$ để kiểm mã và đo thời gian;
2. cấu hình ban đầu $\alpha=0{,}1$, $\varepsilon=0{,}1$, $\gamma=0{,}95$ như Ví dụ 8.1 của sách, $n=50$, $\kappa\in\{10^{-4};\,10^{-3};\,10^{-2}\}$, bốn tác tử, hai mê cung, hạt giống $0,\dots,29$;
3. lặp lại cấu hình của bước 2 với $30$ hạt giống khác, $30,\dots,59$, cho $\kappa=10^{-3}$;
4. thử nghiệm sơ bộ ở bước 2 cho Dyna-Q+ kém Dyna-Q trong pha thứ nhất, ngược với Hình 8.4 và 8.5 của sách; vì vậy, một đợt chạy bổ sung chỉ gồm (A) và (B) với $\alpha\in\{0{,}1;\,0{,}5;\,1\}$, $\kappa\in\{10^{-4};\,10^{-3}\}$; với $\alpha=1$, (B) hơn (A) ở pha thứ nhất trên cả hai mê cung, như trên hình của sách;
5. chọn thêm cấu hình $\alpha=1$ từ kết quả của bước 4 và chạy lại bước 2 và bước 3 với $\alpha=1$;
6. sau các bước trên, một lần chạy chẩn đoán của (C) trên mê cung bị chặn, hạt giống $0,\dots,9$, ghi $\max_aQ(\mathrm S,a)$ sau bước $1\,000$.

Mọi số dưới đây thuộc cấu hình nêu trên; kết quả chính dùng $\kappa=10^{-3}$.

*Mê cung lối tắt, $\kappa=10^{-3}$.* Cột "đường $10$ bước" là số lần chạy, trên $30$, có chính sách tham lam cuối đi lối tắt.

| $\alpha$ | tác tử | tới bước $3\,000$ | tới bước $6\,000$ | bước $5\,001$–$6\,000$ | đường $10$ bước |
|---|---|---:|---:|---:|---:|
| $0{,}1$ | (A) | $130{,}0\pm4{,}8$ | $295{,}0\pm5{,}4$ | $56{,}1\pm1{,}1$ | $1$ |
| $0{,}1$ | (B) | $90{,}0\pm2{,}7$ | $308{,}0\pm3{,}4$ | $80{,}1\pm0{,}5$ | $26$ |
| $0{,}1$ | (C) | $150{,}0\pm1{,}8$ | $329{,}1\pm2{,}8$ | $59{,}7\pm0{,}5$ | $0$ |
| $0{,}1$ | (C′) | $133{,}8\pm1{,}8$ | $297{,}5\pm1{,}7$ | $55{,}0\pm0{,}2$ | $0$ |
| $1$ | (A) | $129{,}1\pm4{,}8$ | $291{,}3\pm5{,}1$ | $54{,}3\pm0{,}3$ | $0$ |
| $1$ | (B) | $135{,}5\pm0{,}7$ | $365{,}7\pm1{,}6$ | $81{,}2\pm0{,}4$ | $24$ |
| $1$ | (C) | $158{,}4\pm1{,}8$ | $337{,}5\pm2{,}8$ | $59{,}6\pm0{,}5$ | $0$ |
| $1$ | (C′) | $139{,}8\pm1{,}6$ | $302{,}9\pm1{,}8$ | $54{,}7\pm0{,}3$ | $0$ |

Ở cả hai giá trị $\alpha$:

- tới bước $3\,000$, (C) hơn (A) theo hiệu ghép cặp $20{,}0\pm5{,}3$ ($\alpha=0{,}1$) và $29{,}3\pm5{,}4$ ($\alpha=1$); phần lớn mức hơn này đến từ việc bỏ $\varepsilon$, vì (C) hơn (C′) $16{,}2\pm2{,}8$ và $18{,}6\pm2{,}9$;
- (C) không chuyển sang lối tắt ở lần chạy nào; sau bước $3\,000$ nó tới ô $(4,9)$ ở $4$ trên $30$ lần chạy, Dyna-Q ở $9$ ($\alpha=0{,}1$) và $6$ ($\alpha=1$), Dyna-Q+ ở cả $30$ lần chạy;
- trong pha thứ hai, (B) hơn (C) theo hiệu ghép cặp $38{,}8\pm2{,}4$ ($\alpha=0{,}1$) và $51{,}1\pm2{,}0$ ($\alpha=1$) lần tới đích; trong $1\,000$ bước cuối, (B) tới đích khoảng $80$ lần, (C) khoảng $60$ lần, gần mức của đường $16$ bước;
- phần thưởng tích lũy tới bước $6\,000$ của (C) vẫn cao hơn (B) khi $\alpha=0{,}1$, nhờ lợi thế ở pha thứ nhất, dù (C) không dùng lối tắt.

*Độ nhạy theo $\kappa$, mê cung lối tắt.*

| $\alpha$ | $\kappa$ | tác tử | tới bước $3\,000$ | tới bước $6\,000$ | đường $10$ bước |
|---|---|---|---:|---:|---:|
| $0{,}1$ | $10^{-4}$ | (B) | $103{,}0\pm3{,}1$ | $268{,}4\pm3{,}1$ | $0$ |
| $0{,}1$ | $10^{-4}$ | (C) | $154{,}5\pm1{,}8$ | $339{,}3\pm2{,}8$ | $0$ |
| $0{,}1$ | $10^{-2}$ | (B) | $4{,}0\pm0{,}2$ | $6{,}7\pm0{,}5$ | $0$ |
| $0{,}1$ | $10^{-2}$ | (C) | $59{,}3\pm1{,}6$ | $164{,}8\pm6{,}7$ | $12$ |
| $1$ | $10^{-4}$ | (B) | $151{,}2\pm0{,}6$ | $317{,}7\pm0{,}9$ | $0$ |
| $1$ | $10^{-4}$ | (C) | $160{,}5\pm1{,}8$ | $345{,}1\pm2{,}7$ | $0$ |
| $1$ | $10^{-2}$ | (B) | $4{,}0\pm0{,}3$ | $6{,}5\pm0{,}4$ | $0$ |
| $1$ | $10^{-2}$ | (C) | $61{,}4\pm1{,}6$ | $158{,}3\pm6{,}2$ | $11$ |

Với $\kappa=10^{-4}$, cả (B) lẫn (C) đều không chuyển sang lối tắt trong $3\,000$ bước của pha thứ hai. Với $\kappa=10^{-2}$, (C) đi lối tắt ở $12$ và $11$ trên $30$ lần chạy, nhưng chỉ tới đích khoảng $60$ lần trong pha thứ nhất, so với khoảng $130$ lần của (A): thưởng lớn lấn át $Q$ ở mọi trạng thái và tác tử đi lang thang. (B) với $\kappa=10^{-2}$ gần như không tới đích: với $\ell=1\,000$, thưởng là $0{,}32$ cho mỗi chuyển mô phỏng, cộng vào mọi mục tiêu lập kế hoạch, trong khi việc tới $\mathrm G$ chỉ cho phần thưởng $1$ một lần.

*Mê cung bị chặn, $\kappa=10^{-3}$.* Cột "đường $16$ bước" là số lần chạy, trên $30$, có chính sách tham lam ở bước $3\,000$ đi đường mới.

| $\alpha$ | tác tử | tới bước $1\,000$ | tới bước $3\,000$ | bước $1\,001$–$3\,000$ | đường $16$ bước |
|---|---|---:|---:|---:|---:|
| $0{,}1$ | (A) | $53{,}1\pm4{,}6$ | $73{,}0\pm4{,}6$ | $19{,}9\pm6{,}1$ | $8$ |
| $0{,}1$ | (B) | $43{,}9\pm2{,}4$ | $91{,}3\pm3{,}5$ | $47{,}4\pm3{,}3$ | $17$ |
| $0{,}1$ | (C) | $69{,}8\pm2{,}3$ | $83{,}2\pm4{,}7$ | $13{,}4\pm5{,}0$ | $7$ |
| $0{,}1$ | (C′) | $60{,}0\pm1{,}8$ | $79{,}7\pm4{,}6$ | $19{,}7\pm5{,}6$ | $9$ |
| $1$ | (A) | $51{,}6\pm4{,}5$ | $68{,}5\pm6{,}0$ | $16{,}9\pm6{,}3$ | $6$ |
| $1$ | (B) | $73{,}5\pm1{,}1$ | $165{,}2\pm1{,}2$ | $91{,}6\pm0{,}4$ | $17$ |
| $1$ | (C) | $72{,}5\pm2{,}0$ | $149{,}3\pm2{,}4$ | $76{,}8\pm2{,}4$ | $14$ |
| $1$ | (C′) | $64{,}2\pm1{,}6$ | $137{,}2\pm2{,}7$ | $73{,}0\pm2{,}4$ | $24$ |

Ở mê cung này, mô hình cũ sai theo hướng lạc quan và tự được sửa khi tác tử đi vào lối đã bị chặn. Kết quả của (C) ở pha thứ hai phụ thuộc $\alpha$: với $\alpha=1$, (C) hơn (A) $59{,}9\pm6{,}7$ lần tới đích và kém (B) $14{,}9\pm2{,}3$ lần; với $\alpha=0{,}1$, (C) không hơn (A) (hiệu $-6{,}6\pm8{,}2$) và kém (B) $34{,}0\pm6{,}5$ lần. Lần chạy chẩn đoán giải thích sự phụ thuộc này. Khi mô hình đã ghi lối cũ bị chặn và chưa biết lối mới, các cập nhật lập kế hoạch hạ $Q$ dọc đường cũ, và khi $Q$ đã nhỏ thì thưởng $\kappa\sqrt{\ell}$ quyết định hành động. Trung bình trên hạt giống $0,\dots,9$, $\max_aQ(\mathrm S,a)$ của (C) giảm từ $0{,}60$ ở bước $1\,000$ xuống $0{,}12$ ở bước $1\,200$ khi $\alpha=1$, nhưng chỉ xuống $0{,}48$ khi $\alpha=0{,}1$.

*Lặp lại với hạt giống $30,\dots,59$, $\kappa=10^{-3}$.* Các kết luận trên giữ nguyên: ở mê cung lối tắt, (C) đi lối tắt ở $0$ trên $30$ lần chạy với cả hai $\alpha$, (B) ở $27$ ($\alpha=0{,}1$) và $28$ ($\alpha=1$); trong pha thứ hai, (B) hơn (C) $36{,}0\pm2{,}3$ và $47{,}9\pm1{,}9$ lần; tới bước $3\,000$, (C) hơn (A) $23{,}6\pm5{,}2$ và $31{,}8\pm5{,}1$ lần. Ở mê cung bị chặn, trong pha thứ hai (B) hơn (C) $41{,}2\pm5{,}2$ ($\alpha=0{,}1$) và $11{,}0\pm2{,}4$ ($\alpha=1$) lần.

**Câu (c).** *Việc đưa thưởng vào cập nhật có cần thiết không.* Với thí nghiệm này, có, nếu mục đích là phát hiện thay đổi ở một cặp cách xa đường đang đi, như lối tắt: với $\kappa=10^{-3}$, Dyna-Q+ chuyển sang lối tắt ở $24$ tới $28$ trên $30$ lần chạy, (C) ở $0$, Dyna-Q ở nhiều nhất $1$. Thưởng trong cập nhật lan qua các cập nhật lập kế hoạch, nên giá trị của một chuyến đi thử nhiều bước tới cặp lâu chưa thử được cộng vào $Q$ của các trạng thái trên đường tới đó, và tác tử lập kế hoạch đi tới cặp đó. Thưởng chỉ dùng khi chọn hành động tác động một bước, tại trạng thái hiện tại: tác tử chỉ thử những cặp lâu chưa thử ở các trạng thái nó đang đi qua. Lối tắt chỉ được ghi vào mô hình khi tác tử thử $\uparrow$ tại $(5,9)$, một ô không nằm trên đường $16$ bước nào (đường ngắn nhất qua $(5,9)$ trong pha thứ nhất dài $26$ bước). Thưởng chỉ dùng khi chọn hành động không kéo tác tử tới ô đó, nên (C) không tìm ra lối tắt.

*Điểm mạnh của (C).*

- $Q$ không bị thưởng làm lệch: bước (f) giống hệt Dyna-Q, nên bảng của (C) không chứa thưởng như bảng của Dyna-Q+ ở Nhận xét 11.13, và lập kế hoạch không trả chi phí thăm dò;
- thăm dò có hệ thống tại trạng thái hiện tại thay được $\varepsilon$; khi môi trường không đổi, với $\kappa\le10^{-3}$, (C) tới đích nhiều hơn cả (A) lẫn (B) ở pha thứ nhất của mê cung lối tắt, nhiều hơn (A) và không kém (B) quá sai số chuẩn ở pha thứ nhất của mê cung bị chặn;
- ở mê cung bị chặn với $\alpha=1$, nơi sai của mô hình là lạc quan, (C) phục hồi phần lớn: $76{,}8$ lần tới đích trong pha thứ hai, so với $91{,}6$ của Dyna-Q+ và $16{,}9$ của Dyna-Q.

*Điểm yếu của (C).*

- không phát hiện thay đổi tốt lên ở xa đường đang đi: với $\kappa=10^{-3}$, $0$ trên $60$ lần chạy (hạt giống $0,\dots,59$) chuyển sang lối tắt, ở mỗi giá trị $\alpha$;
- tăng $\kappa$ tới $10^{-2}$ thì (C) tìm ra lối tắt ở $23$ trên $60$ lần chạy (hai giá trị $\alpha$), nhưng mất hơn một nửa số lần tới đích ở pha thứ nhất;
- không có $\varepsilon$, (C) tới ô $(4,9)$ còn ít hơn Dyna-Q ($4$ so với $9$ và $6$ trên $30$ lần chạy), vì thăm dò của nó chỉ đi theo $\ell$ của các cặp quanh đường đang đi.

Các kết luận này thuộc hai mê cung $6\times9$ tất định, $n=50$, $\alpha\in\{0{,}1;\,1\}$, $\kappa\in\{10^{-4};\,10^{-3};\,10^{-2}\}$ và $6\,000$ hoặc $3\,000$ bước. Phần thưởng tích lũy cuối thí nghiệm xếp (C) trên (B) khi $\alpha=0{,}1$ vì thí nghiệm dừng ở bước $6\,000$. Tốc độ tới đích ở $1\,000$ bước cuối cho thấy (B) đã chuyển sang đường tốt hơn.

**Kiểm tra lại.** Các phép tính tay ở câu (a) là phép kiểm: mã đúng cho thưởng $0{,}2$ và giá trị mới $0{,}64$ ở Ví dụ 11.9, và chỉ số $0{,}3022$, $0{,}3$, $0{,}12$, $0{,}15$ của (C). Ba lỗi thường gặp:

- Cộng thưởng cả vào mục tiêu của bước (f). Tác tử khi đó là Dyna-Q+ chọn hành động theo $Q+\kappa\sqrt{\ell}$, và mọi khác biệt với (B) không còn đo được tác dụng của việc bỏ thưởng khỏi cập nhật.
- Tăng $\ell$ cả ở các cập nhật lập kế hoạch. Vì $\ell$ đếm bước thật, với $n=50$, $\ell$ khi đó tăng nhanh gấp $51$ lần và thưởng lớn gấp $\sqrt{51}\approx7{,}1$ lần.
- Chỉ so phần thưởng tích lũy ở bước $6\,000$. Với $\alpha=0{,}1$, (C) đứng đầu ($329{,}1$ so với $308{,}0$ của (B)) dù không lần chạy nào của nó đi lối tắt.
:::

## Tài liệu tham khảo

- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 2.8, §2.7, trang 36, cùng bộ thử mười tay, §2.3, trang 28–29, (2.10), trang 35, và Hình 2.4, trang 36 (Bài tập 11.18); (7.4)–(7.5), §7.2, trang 146 (Bài tập 11.16); Bài tập 8.1, §8.2, trang 166, cùng Ví dụ 8.1 và Hình 8.2, 8.3, trang 164–165 (Bài tập 11.16); Bài tập 8.2–8.5, §8.3, trang 168, cùng Ví dụ 8.2, 8.3, Hình 8.4, 8.5, trang 166–167, và chú thích 1, trang 168 (Bài tập 11.12, 11.13, 11.17, 11.19); giả mã Dyna-Q dạng bảng, trang 164 (Bài tập 11.17); Bài tập 8.6, §8.5, trang 174, và phân tích của Hình 8.7, trang 173–174 (Bài tập 11.14); §10.3, (10.6), (10.9) và phương trình Bellman vi phân, trang 249–250 (Bài tập 11.15); Bài tập 17.1, §17.2, trang 464, cùng (17.2)–(17.4), trang 462–463 (Bài tập 11.15).
