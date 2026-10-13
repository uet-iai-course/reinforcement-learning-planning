# Bài tập Bài 05 — Dự đoán phi mô hình

Bộ bài tập gồm mười sáu bài ở ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Ba bài 05.8, 05.11 và 05.12 là bài tập trong thân chương của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html) có trang "Bài tập: …" tương ứng trên trang chiếu. Chúng giữ số hiệu, đề, gợi ý và lời giải của ghi chú, được nêu lại cho tự chứa dữ kiện, bổ sung phần "Kiểm tra lại", và được xếp vào mức tương ứng. Mười ba bài 05.16–05.28 chỉ có ở tệp này và tiếp nối bộ đếm Bài tập của ghi chú. Trong mỗi mức, các bài xếp theo thứ tự mạch của bài học, nên số hiệu không tăng liên tục: 05.11 (mạch 4) đứng cuối mức nhận biết; 05.12 (mạch 5) đứng trước 05.25 cùng mạch; bài tổng hợp 05.8 của mạch kết luận đứng cuối mức tính toán. Các bài tập thân chương khác của ghi chú (05.1–05.7, 05.9, 05.10) và mục "Bài tập củng cố" (05.13–05.15) không có trang tương ứng trên trang chiếu, nên chỉ được ghi trong bảng dưới và không chép lại. Năm bài trùng bài tập trên trang chiếu: 05.8, 05.11 (câu (e)), 05.12, 05.18 và 05.20. Với các bài này, dòng "Trùng trang chiếu" dẫn tới trang đề và trang lời giải, lời giải trong tệp cho cùng kết quả với lời giải trên trang, và các câu thêm của tệp được ghi rõ. Ba bài vận dụng 05.26–05.28 dùng số liệu của notebook thực hành Lunar Lander của bài; hai bài có nhãn [Lập trình].

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/1/1) | [chỉ trong ghi chú](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html): 05.1 |
| 2. Lợi tức và ước lượng Monte Carlo | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/2/1) | 05.16, 05.18, 05.19; [chỉ trong ghi chú](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html): 05.2–05.5 |
| 3. Sai phân thời gian TD(0) | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/3/1) | 05.17, 05.20, 05.21, 05.26; [chỉ trong ghi chú](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html): 05.6, 05.7 |
| 4. Độ chệch, phương sai và hội tụ | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/4/1) | 05.11, 05.22, 05.23, 05.24, 05.27; [chỉ trong ghi chú](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html): 05.9, 05.10, 05.14 |
| 5. Dữ liệu cố định và cập nhật theo lô | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/5/1) | 05.12, 05.25, 05.28 |
| 6. Tổng kết và chuyển tiếp | [Mở phần](lecture-05-du-doan-phi-mo-hinh.html#/6/1) | 05.8; [chỉ trong ghi chú](material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html): 05.13, 05.15 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 05. Một chính sách Markov dừng $\pi$ được giữ cố định; môi trường là quá trình quyết định Markov (Markov decision process, MDP) dừng với động lực $p(s',r\mid s,a)$ mà tác tử (agent) không biết. $\mathcal S$ là tập trạng thái không kết thúc; giá trị của mọi trạng thái kết thúc bằng $0$, cả với giá trị thật $v_\pi$ lẫn với bảng ước lượng $V$. $R_{t+1}$ là phần thưởng (reward) của chuyển từ thời điểm $t$ sang $t+1$; $T$ là thời điểm kết thúc của lượt (episode), $G_T=0$, và lợi tức (return) là $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}=R_{t+1}+\gamma G_{t+1}$. Kỳ vọng $\mathbb E_\pi[\cdot\mid S_t=s]$ lấy theo chính sách và động lực môi trường. Monte Carlo và sai phân thời gian (temporal difference, TD) một bước, ký hiệu TD(0), là hai cách tạo mục tiêu cập nhật (update target) $Y$ trong quy tắc $V(s)\leftarrow V(s)+\alpha[Y-V(s)]$ với bước học (step size) $\alpha$; cập nhật theo lô (batch updating) quét lại nhiều lần một tập dữ liệu cố định. Mục tiêu TD, một mục tiêu bootstrap (bootstrap target), là $Y_t=R_{t+1}+\gamma V_t(S_{t+1})$, sai số TD là $\delta_t=Y_t-V_t(S_t)$, cập nhật là $V(S_t)\leftarrow V(S_t)+\alpha\,\delta_t$; mục tiêu một bước lý tưởng là $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$. Độ lệch của bảng là $V-v_\pi$; độ chệch (bias) của một mục tiêu $Y$ tại $s$ là $\operatorname{bias}(Y;s)=\mathbb E_\pi[Y\mid S_t=s]-v_\pi(s)$, tính với bảng giữ cố định (Định nghĩa 05.24).

**Tàu đổ bộ thu nhỏ.** Dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$ (số liệu sư phạm của bài giảng gốc 2025–2026); $\mathcal S=\{\mathrm S,\mathrm X\}$, hai ô biên $\mathrm L$ ("rơi") và $\mathrm G$ ("nằm yên") là trạng thái kết thúc; mỗi lượt bắt đầu ở $\mathrm S$. Chính sách luôn chọn hành động $\mathrm{tien}$; tàu sang ô bên phải với xác suất $0{,}8$ và sang ô bên trái với xác suất $0{,}2$. Phần thưởng là $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho mọi chuyển khác. Hai lượt dùng chung:

| Lượt | Trạng thái $S_0,S_1,\ldots,S_T$ | Phần thưởng $R_1,\ldots,R_T$ | $T$ |
| --- | --- | --- | --- |
| $e_1$ | $\mathrm S,\mathrm X,\mathrm S,\mathrm X,\mathrm G$ | $0,0,0,1$ | $4$ |
| $e_2$ | $\mathrm S,\mathrm X,\mathrm S,\mathrm L$ | $0,0,-1$ | $3$ |

Với $\gamma=1$, giá trị chuẩn giải từ mô hình là $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$ (Ví dụ 05.14). Mô hình chỉ dùng để đo sai số; không thuật toán nào của bài đọc các xác suất $0{,}8$, $0{,}2$. Dữ kiện được nêu lại trong từng bài dùng nó.

**Quy ước trình bày.** Số thập phân viết với dấu phẩy; một cặp giá trị ghi $(V(\mathrm S);\ V(\mathrm X))$, các thành phần cách nhau bằng dấu chấm phẩy. Số liệu Lunar Lander lấy từ một lần chạy đã nhúng trong notebook thực hành Bài 05 (gymnasium 1.3.0) và có thể đổi khi chạy lại với phiên bản gói khác. Lời giải nêu kết quả của ghi chú được dùng ở từng bước. Số liệu của Bài tập 05.19, 05.24, 05.25 là số liệu sư phạm tự xây dựng.

## Mức nhận biết

### Bài tập 05.16. Hai trục lựa chọn và giả thiết của Monte Carlo

**Mức độ:** nhận biết. Mục tiêu học tập 2 và 3 của ghi chú bài giảng; mạch 2.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 5, đã hiệu chỉnh tiền đề "cả ba cách cùng hội tụ"; ghi chú bài giảng, Nhận xét 05.12, 05.19, Định lý 05.16, 05.17.

::: exercise Bài tập 05.16 (Hai trục lựa chọn và giả thiết của Monte Carlo)
Bài tập tuần 5 của học kỳ 2 năm học 2025–2026 liệt kê ba cách cập nhật trong đánh giá chính sách: Monte Carlo lần ghé đầu tiên (first-visit); Monte Carlo gia tăng với trung bình mẫu, tức bước học $1/N(s)$; Monte Carlo gia tăng với bước học hằng $\alpha\in(0,1)$. Môi trường là MDP dừng, hữu hạn, chính sách $\pi$ cố định, mọi lượt kết thúc hầu chắc chắn (almost surely) và phần thưởng bị chặn.

- (a) Xếp ba cách vào hai trục lựa chọn của Monte Carlo và liệt kê bốn cấu hình mà hai trục tạo ra.
- (b) Nêu các giả thiết về cách sinh lượt để những mẫu lợi tức lần ghé đầu tiên tại một trạng thái $s$, lấy từ các lượt khác nhau, độc lập cùng phân phối. Nêu lý do các mẫu mọi lần ghé (every-visit) trong cùng một lượt không độc lập.
- (c) Trong bốn cấu hình, chỉ ra các cấu hình hội tụ hầu chắc chắn về $v_\pi(s)$ theo các định lý của Mục 2.6, kèm điều kiện. Nêu các cấu hình không hội tụ và hoàn cảnh mà chúng phù hợp hơn.
:::

::: hint Gợi ý Bài tập 05.16
Một trục quyết định mẫu nào được dùng, trục kia quyết định cách kết hợp các mẫu (Nhận xét 05.12). Ở (c), so phạm vi của Định lý 05.16, 05.17 với Nhận xét 05.19.
:::

::: solution Lời giải Bài tập 05.16
**Câu (a).** Trục thứ nhất là quy tắc lần ghé: lần ghé đầu tiên hoặc mọi lần ghé. Trục thứ hai là quy tắc bước học: $1/N(s)$ hoặc hằng số $\alpha$. "Lần ghé đầu tiên" thuộc trục thứ nhất; "trung bình mẫu" và "bước học hằng" thuộc trục thứ hai. Hai trục tạo bốn cấu hình: lần ghé đầu tiên với $1/N(s)$; mọi lần ghé với $1/N(s)$; lần ghé đầu tiên với $\alpha$ hằng; mọi lần ghé với $\alpha$ hằng. Ba cách của Bài tập tuần 5 vì vậy nằm trên hai trục khác nhau, và mỗi cấu hình chạy được ghép một lựa chọn của mỗi trục; với bước hằng còn cần giá trị khởi tạo $V_0(s)$, vì theo Mệnh đề 05.11 nó giữ trọng số $(1-\alpha)^n$ sau $n$ mẫu.

**Câu (b).** Các lượt được sinh độc lập với nhau, cùng phân phối trạng thái đầu, dưới cùng chính sách cố định $\pi$ và cùng động lực dừng $p$. Khi đó mẫu lần ghé đầu tiên của mỗi lượt là một hàm của riêng lượt đó, nên các mẫu từ những lượt khác nhau độc lập cùng phân phối (Bước 1 của chứng minh Định lý 05.16). Trong cùng một lượt, các mẫu mọi lần ghé dùng chung phần đuôi của lượt: trong $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$, hai lợi tức tại $\mathrm S$ là $G_0=\gamma^3$ và $G_2=\gamma$, cùng được quyết định bởi phần thưởng $+1$ ở chuyển cuối.

**Câu (c).** Hai cấu hình dùng bước $1/N(s)$ hội tụ hầu chắc chắn về $v_\pi(s)$: lần ghé đầu tiên theo Định lý 05.16 và mọi lần ghé theo Định lý 05.17. Điều kiện gồm $\mathcal S$ hữu hạn, chính sách cố định, môi trường Markov dừng, lượt kết thúc hầu chắc chắn, phần thưởng bị chặn, các lượt độc lập cùng phân phối, và $s$ được ghé với xác suất dương trong một lượt. Hai cấu hình dùng bước hằng $\alpha\in(0,1)$ không hội tụ. Với lần ghé đầu tiên, các mẫu độc lập cùng phân phối và phương sai của ước lượng tiến tới $\alpha\sigma^2/(2-\alpha)>0$ (Nhận xét 05.19). Với mọi lần ghé, các mẫu không độc lập nên công thức phương sai không áp dụng, nhưng lập luận cuối Nhận xét 05.19 vẫn dùng được: nếu $V_n$ hội tụ thì $g_n=V_{n-1}+(V_n-V_{n-1})/\alpha$ hội tụ, điều không xảy ra khi các mẫu còn dao động. Bước hằng phù hợp hơn khi môi trường thay đổi theo thời gian, vì mẫu mới nhận trọng số lớn hơn mẫu cũ (bài giảng gốc, trang 21); trường hợp này nằm ngoài giả thiết môi trường dừng của chương.

**Kiểm tra lại.** Tiền đề "cả ba cách cùng hội tụ" của Bài tập tuần 5 sai ở bước học hằng. Hai lỗi thường gặp. Thứ nhất, coi "lần ghé đầu tiên" và "trung bình mẫu" là hai phương pháp loại trừ nhau; cấu hình ghép hai lựa chọn này là hàng đầu của Ví dụ 05.5. Thứ hai, lấy việc ước lượng bước hằng tiến tới đích khi mục tiêu không có nhiễu (Ví dụ 05.19) làm bằng chứng hội tụ trên mẫu ngẫu nhiên.
:::

### Bài tập 05.17. Monte Carlo và TD(0) trên một lượt bị cắt ngắn

**Mức độ:** nhận biết. Mục tiêu học tập 1 và 4 của ghi chú bài giảng; mạch 3.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 1 và bài 3; ghi chú bài giảng, Định nghĩa 05.3, 05.10, 05.20, Thuật toán 05.13, 05.21, Nhận xét 05.22, Tình huống 05.2.

::: exercise Bài tập 05.17 (Monte Carlo và TD(0) trên một lượt bị cắt ngắn)
Xét tàu đổ bộ thu nhỏ: dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$, hai ô biên là trạng thái kết thúc, phần thưởng $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho chuyển khác; $\gamma=1$. Bảng hiện tại $V(\mathrm S)=0{,}4$, $V(\mathrm X)=0{,}6$, $V(\mathrm L)=V(\mathrm G)=0$; bước học $\alpha=0{,}5$. Một lượt bị cắt ngắn (truncated episode) vì giới hạn hai bước: tác tử quan sát $\mathrm S\to\mathrm X\to\mathrm S$ với phần thưởng $(0,0)$, và trạng thái $S_2=\mathrm S$ tại điểm cắt không phải trạng thái kết thúc.

- (a) So sánh Monte Carlo và TD(0) theo ba khía cạnh: mục tiêu cập nhật, thời điểm cập nhật, khả năng học từ lượt chưa kết thúc hoặc bị cắt ngắn.
- (b) Viết mục tiêu TD, sai số TD và giá trị mới cho hai chuyển của lượt, theo thứ tự. Nêu ý nghĩa của từng đại lượng và các phần tử của bảng giữ nguyên ở mỗi chuyển.
- (c) Tính lại chuyển thứ hai khi coi điểm cắt là trạng thái kết thúc, tức đặt giá trị tiếp nối bằng $0$, và giải thích vì sao cách này sai. Nêu điều Monte Carlo làm được với lượt này.
:::

::: hint Gợi ý Bài tập 05.17
Viết hai mục tiêu theo cùng khung của Định nghĩa 05.10. Mục tiêu TD thay $G_{t+1}$ trong $G_t=R_{t+1}+\gamma G_{t+1}$ bằng $V(S_{t+1})$. Chuyển thứ hai đọc bảng sau chuyển thứ nhất.
:::

::: solution Lời giải Bài tập 05.17
**Câu (a).** Cả hai phương pháp dùng quy tắc $V(s)\leftarrow V(s)+\alpha[Y-V(s)]$ của Định nghĩa 05.10 và khác nhau ở mục tiêu $Y$.

| Khía cạnh | Monte Carlo | TD(0) |
| --- | --- | --- |
| Mục tiêu cập nhật | lợi tức đầy đủ $G_t$ | $R_{t+1}+\gamma V(S_{t+1})$, mục tiêu bootstrap |
| Thời điểm cập nhật | sau khi lượt kết thúc (Thuật toán 05.13) | ngay sau mỗi chuyển (Thuật toán 05.21) |
| Lượt chưa kết thúc hoặc bị cắt ngắn | không dùng được: không có $T$ để tính ngược từ $G_T=0$ | dùng được mọi chuyển đã quan sát (Nhận xét 05.22) |

**Câu (b).** Chuyển $\mathrm S\to\mathrm X$:

$$
\begin{aligned}
Y_0&=0+1\cdot V(\mathrm X)=0{,}6,\\
\delta_0&=0{,}6-0{,}4=0{,}2,\\
V(\mathrm S)&=0{,}4+0{,}5\cdot0{,}2=0{,}5 .
\end{aligned}
$$

Chuyển $\mathrm X\to\mathrm S$, chuyển cuối trước điểm cắt, đọc $V(\mathrm S)=0{,}5$ vừa ghi:

$$
\begin{aligned}
Y_1&=0+1\cdot V(\mathrm S)=0{,}5,\\
\delta_1&=0{,}5-0{,}6=-0{,}1,\\
V(\mathrm X)&=0{,}6+0{,}5\cdot(-0{,}1)=0{,}55 .
\end{aligned}
$$

$Y_t$ gồm phần thưởng đã quan sát và dự đoán của bảng cho phần còn lại của lượt từ $S_{t+1}$. $\delta_t$ là hiệu giữa dự đoán dựa trên thông tin ở thời điểm $t+1$ và dự đoán $V(S_t)$ ở thời điểm $t$. Bước học $\alpha$ quyết định phần của hiệu đó được cộng vào $V(S_t)$. Ở chuyển thứ nhất chỉ $V(\mathrm S)$ đổi; ở chuyển thứ hai chỉ $V(\mathrm X)$ đổi; $V(\mathrm L)=V(\mathrm G)=0$ giữ nguyên.

**Câu (c).** Coi điểm cắt là trạng thái kết thúc cho $Y_1=0+0=0$, $\delta_1=-0{,}6$, $V(\mathrm X)=0{,}3$. Cách này sai vì $S_2=\mathrm S$ không phải trạng thái kết thúc: lượt chỉ dừng do giới hạn thời gian, và phần đuôi chưa quan sát từ $\mathrm S$ có kỳ vọng $v_\pi(\mathrm S)=11/21\ne0$ (Nhận xét 05.22, Tình huống 05.2). Monte Carlo không có $G_0$ hay $G_1$ của lượt này, vì không có thời điểm kết thúc để tính ngược từ $G_T=0$; Thuật toán 05.13 bỏ cả lượt.

**Kiểm tra lại.** Ở chuyển thứ hai, giá trị tiếp nối là $V(\mathrm S)$ của chính bảng đang học, không phải $0$. Ba lỗi thường gặp: đọc $V(\mathrm S)=0{,}4$ cũ ở chuyển thứ hai, cho $V(\mathrm X)=0{,}5$; đặt giá trị tiếp nối bằng $0$ tại điểm cắt, cho $V(\mathrm X)=0{,}3$; và đọc $\delta_1<0$ thành bằng chứng bảng đánh giá cao $\mathrm X$, dù $\delta_1$ chỉ là một mẫu (Bài tập 05.6 của ghi chú).
:::

### Bài tập 05.11. Lịch bước học và điều kiện Robbins–Monro

**Mức độ:** nhận biết. Mục tiêu học tập 5 của ghi chú bài giảng; mạch 4. Bài giữ số hiệu, đề, gợi ý và lời giải của ghi chú bài giảng (Mục 4.4).

**Nguồn:** ghi chú bài giảng, Bài tập 05.11, Định lý 05.30, Ví dụ 05.19; Sutton và Barto (2018), §2.5, trang 33.

**Trùng trang chiếu:** câu (e) trùng câu (c) của [Bài tập: nhận định về độ chệch, phương sai và bước học](lecture-05-du-doan-phi-mo-hinh.html#/4/13) và [trang lời giải](lecture-05-du-doan-phi-mo-hinh.html#/4/14). Câu (a) của trang đó là trường hợp $x=10$ của Bài tập 05.24; câu (b) dùng Nhận xét 05.19 của ghi chú, và Bài tập 05.22(c) làm cùng phép tính với $\alpha=0{,}2$.

::: exercise Bài tập 05.11 (Lịch bước học và điều kiện Robbins–Monro)
Định lý 05.30 bảo đảm TD(0) dạng bảng hội tụ về $v_\pi$ khi, với mọi trạng thái $s$, bước học ở lần cập nhật thứ $n$ của $s$ thỏa $\alpha_n(s)\in[0,1]$ và hai điều kiện Robbins–Monro

$$
\sum_{n=1}^{\infty}\alpha_n(s)=\infty,\qquad\sum_{n=1}^{\infty}\alpha_n(s)^2<\infty .
$$

Với mỗi lịch bước học sau, xác định nó có thỏa hai điều kiện này không: (a) $\alpha_n=1/n$; (b) $\alpha_n=1/\sqrt n$; (c) $\alpha_n=0{,}1$; (d) $\alpha_n=1/n^2$; (e) $\alpha_n=n^{-0{,}6}$.
:::

::: hint Gợi ý Bài tập 05.11
Chuỗi $\sum_nn^{-p}$ hội tụ khi và chỉ khi $p>1$.
:::

::: solution Lời giải Bài tập 05.11
**Câu (a).** $\sum1/n=\infty$, $\sum1/n^2<\infty$: thỏa cả hai.

**Câu (b).** $\sum n^{-1/2}=\infty$, nhưng $\sum1/n=\infty$: vi phạm điều kiện thứ hai.

**Câu (c).** $\sum0{,}1=\infty$, $\sum0{,}01=\infty$: vi phạm điều kiện thứ hai.

**Câu (d).** $\sum1/n^2<\infty$: vi phạm điều kiện thứ nhất.

**Câu (e).** $p=0{,}6\le1$ nên $\sum n^{-0{,}6}=\infty$; $2p=1{,}2>1$ nên $\sum n^{-1{,}2}<\infty$: thỏa cả hai.

**Kiểm tra lại.** Lịch $n^{-p}$ thỏa cả hai điều kiện khi và chỉ khi $1/2<p\le1$. Câu (e) cho cùng kết luận "đúng" như câu (c) của trang lời giải. Hai lỗi thường gặp: kiểm điều kiện thứ hai trên $\sum_n\alpha_n$ thay vì $\sum_n\alpha_n^2$, nên kết luận sai ở (b); và lấy việc bước hằng $0{,}1$ tới được đích khi mục tiêu không có nhiễu (Ví dụ 05.19) làm bằng chứng nó thỏa giả thiết của định lý.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 05.18. Chọn mẫu Monte Carlo tại $\mathrm S$ với $\gamma=0{,}9$

**Mức độ:** tính toán. Mục tiêu học tập 1, 2 và 3 của ghi chú bài giảng; mạch 2.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 5 và bài 7, đổi hệ số chiết khấu; bài giảng gốc (2025–2026), trang 20, 22; ghi chú bài giảng, Định nghĩa 05.3, 05.6, Mệnh đề 05.4, 05.11.

**Trùng trang chiếu:** [Bài tập: chọn mẫu Monte Carlo tại $\mathrm S$](lecture-05-du-doan-phi-mo-hinh.html#/2/18) và [trang lời giải](lecture-05-du-doan-phi-mo-hinh.html#/2/19), câu (a) và (b). Câu (c) chỉ có trong tệp này.

::: exercise Bài tập 05.18 (Chọn mẫu Monte Carlo tại $\mathrm S$ với $\gamma=0{,}9$)
Tàu đổ bộ thu nhỏ có hai lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,1)$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$ với phần thưởng $(0,0,-1)$, xử lý theo thứ tự $e_1$ rồi $e_2$. Hệ số chiết khấu $\gamma=0{,}9$; bảng ban đầu $V(\mathrm S)=V(\mathrm X)=0$.

- (a) Tại $\mathrm S$, lập dãy lợi tức theo quy tắc lần ghé đầu tiên và theo quy tắc mọi lần ghé; tính hai trung bình.
- (b) Dùng lần ghé đầu tiên với bước học hằng $\alpha=0{,}5$: tính $V(\mathrm S)$ sau mỗi lượt. Giải thích vì sao kết quả khác trung bình lần ghé đầu tiên ở (a), dù hai cách dùng cùng tập mẫu.
- (c) Dùng mọi lần ghé với $\alpha=0{,}5$, cập nhật các mẫu của một lượt theo thứ tự thời gian (bước 4 của Thuật toán 05.13): tính $V(\mathrm S)$ sau mỗi lượt, khai triển kết quả sau $e_2$ thành tổng có trọng số, và lập bảng giá trị $V(\mathrm S)$ sau $e_2$ của bốn cấu hình Monte Carlo.
:::

::: hint Gợi ý Bài tập 05.18
Tính lợi tức ngược từ cuối mỗi lượt bằng $G_t=R_{t+1}+\gamma G_{t+1}$, bắt đầu từ $G_T=0$. Ở (b) và (c), viết kết quả thành tổng có trọng số theo Mệnh đề 05.11: sau $n$ mẫu, giá trị khởi tạo có trọng số $(1-\alpha)^n$ và mẫu thứ $i$ có trọng số $\alpha(1-\alpha)^{n-i}$.
:::

::: solution Lời giải Bài tập 05.18
**Câu (a).** Tính ngược trong $e_1$: $G_4=0$, $G_3=1$, $G_2=0{,}9$, $G_1=0{,}81$, $G_0=0{,}729$. Trong $e_2$: $G_3=0$, $G_2=-1$, $G_1=-0{,}9$, $G_0=-0{,}81$. Ô $\mathrm S$ được ghé tại $t=0$ và $t=2$ trong cả hai lượt.

- Lần ghé đầu tiên: dãy $(0{,}729;\ -0{,}81)$, trung bình $(0{,}729-0{,}81)/2=-0{,}0405$.
- Mọi lần ghé: dãy $(0{,}729;\ 0{,}9;\ -0{,}81;\ -1)$, tức thêm $0{,}9$ và $-1$; trung bình $(0{,}729+0{,}9-0{,}81-1)/4=-0{,}181/4=-0{,}04525$.

**Câu (b).** Hai mẫu theo thứ tự $0{,}729$ rồi $-0{,}81$:

$$
\begin{aligned}
\text{sau } e_1:\ V(\mathrm S)&=0+0{,}5\cdot(0{,}729-0)=0{,}3645,\\
\text{sau } e_2:\ V(\mathrm S)&=0{,}3645+0{,}5\cdot(-0{,}81-0{,}3645)=-0{,}22275 .
\end{aligned}
$$

Theo Mệnh đề 05.11 với $n=2$, $-0{,}22275=0{,}25\cdot0+0{,}25\cdot0{,}729+0{,}5\cdot(-0{,}81)$. Trung bình mẫu đặt trọng số $0{,}5$ cho mỗi mẫu và $0$ cho giá trị khởi tạo. Bước hằng $0{,}5$ giữ trọng số $0{,}25$ cho giá trị khởi tạo và ưu tiên mẫu mới hơn, nên cùng tập mẫu cho hai kết quả khác nhau.

**Câu (c).** Bốn mẫu theo thứ tự $0{,}729$; $0{,}9$; $-0{,}81$; $-1$:

$$
\begin{aligned}
0+0{,}5\cdot(0{,}729-0)&=0{,}3645,\\
0{,}3645+0{,}5\cdot(0{,}9-0{,}3645)&=0{,}63225,\\
0{,}63225+0{,}5\cdot(-0{,}81-0{,}63225)&=-0{,}088875,\\
-0{,}088875+0{,}5\cdot(-1+0{,}088875)&=-0{,}5444375 .
\end{aligned}
$$

Vậy $V(\mathrm S)=0{,}63225$ sau $e_1$ và $-0{,}5444375$ sau $e_2$. Theo Mệnh đề 05.11 với $n=4$:

$$
-0{,}5444375=0{,}0625\cdot0+0{,}0625\cdot0{,}729+0{,}125\cdot0{,}9+0{,}25\cdot(-0{,}81)+0{,}5\cdot(-1).
$$

Bảng giá trị $V(\mathrm S)$ sau $e_2$:

| Quy tắc lần ghé | Trung bình mẫu | Bước hằng $\alpha=0{,}5$ |
| --- | --- | --- |
| Lần ghé đầu tiên | $-0{,}0405$ | $-0{,}22275$ |
| Mọi lần ghé | $-0{,}04525$ | $-0{,}5444375$ |

Đi theo một hàng chỉ đổi cách kết hợp mẫu; đi theo một cột chỉ đổi tập mẫu (Nhận xét 05.12). Với $\gamma=1$, hai ô của cột trung bình mẫu cùng bằng $0$ (Ví dụ 05.5); với $\gamma=0{,}9$, hai lần ghé $\mathrm S$ trong một lượt có lợi tức khác nhau, nên hai quy tắc lần ghé cho hai tập mẫu khác nhau.

**Kiểm tra lại.** Tổng trọng số của bốn mẫu ở (c) là $0{,}0625+0{,}125+0{,}25+0{,}5=0{,}9375=1-0{,}5^4$, phần còn lại $0{,}0625$ là trọng số của giá trị khởi tạo. Ba lỗi thường gặp: tính lợi tức xuôi từ đầu lượt, cho $G_0=0$ trong $e_1$ vì $R_1=0$; nhân $\gamma^4$ thay cho $\gamma^3$ cho phần thưởng $R_4$ trong $G_0$; và dùng mọi lần ghé ở câu (b), cho $-0{,}5444375$ thay cho $-0{,}22275$.
:::

### Bài tập 05.19. Ô chờ: mọi lần ghé chệch ở một lượt

**Mức độ:** chứng minh. Mục tiêu học tập 2 và 3 của ghi chú bài giảng; mạch 2.

**Nguồn:** ghi chú bài giảng, Nhận xét 05.18 (trường hợp $q=1/2$), Mệnh đề 05.7, Định lý 05.17; Sutton và Barto (2018), §5.1, trang 92–93. Số liệu sư phạm tự xây dựng.

::: exercise Bài tập 05.19 (Ô chờ: mọi lần ghé chệch ở một lượt)
Một môi trường có một trạng thái không kết thúc $\mathrm C$ và một trạng thái kết thúc; mọi lượt bắt đầu ở $\mathrm C$. Từ $\mathrm C$, với xác suất $q\in(0,1)$ tác tử ở lại $\mathrm C$ và nhận phần thưởng $1$; với xác suất $1-q$ lượt kết thúc với phần thưởng $0$. Hệ số chiết khấu $\gamma=1$. Gọi $N$ là số lần ghé $\mathrm C$ trong một lượt.

- (a) Tính $v_\pi(\mathrm C)$ bằng phương trình Bellman kỳ vọng.
- (b) Chứng minh $\Pr(N=m)=q^{m-1}(1-q)$ với $m\ge1$, $\mathbb E[N]=1/(1-q)$, $\mathbb E[N(N-1)]=2q/(1-q)^2$, và lợi tức tại lần ghé thứ $k$ bằng $N-k$.
- (c) Chứng minh mẫu lần ghé đầu tiên của một lượt có kỳ vọng $v_\pi(\mathrm C)$, còn trung bình các mẫu mọi lần ghé của một lượt có kỳ vọng $v_\pi(\mathrm C)/2$.
- (d) Chứng minh ước lượng mọi lần ghé với bước $1/N(s)$ sau $M$ lượt hội tụ hầu chắc chắn về $v_\pi(\mathrm C)$ khi $M\to\infty$. Nêu nguyên nhân của độ chệch ở (c).
- (e) Một lượt cụ thể có $N=4$. Tính ước lượng lần ghé đầu tiên và ước lượng mọi lần ghé từ riêng lượt này.
:::

::: hint Gợi ý Bài tập 05.19
Ở (b), đạo hàm hai lần chuỗi hình học $\sum_{m\ge0}q^m=1/(1-q)$ theo $q$. Tại lần ghé thứ $k$, còn $N-k$ lần ở lại, mỗi lần nhận phần thưởng $1$. Ở (d), dùng tỉ số của Bước 1 trong chứng minh Định lý 05.17, với $Z=\sum_{k=1}^{N}(N-k)$.
:::

::: solution Lời giải Bài tập 05.19
**Câu (a).** Phương trình Bellman kỳ vọng tại $\mathrm C$, với giá trị trạng thái kết thúc bằng $0$:

$$
v=q\,(1+v)+(1-q)\cdot(0+0),
$$

nên $(1-q)v=q$ và $v_\pi(\mathrm C)=q/(1-q)$.

**Câu (b).** Lượt có đúng $m$ lần ghé khi tác tử ở lại $m-1$ lần rồi kết thúc; các lựa chọn ở mỗi bước độc lập theo tính Markov, nên $\Pr(N=m)=q^{m-1}(1-q)$. Với $\lvert q\rvert<1$, chuỗi lũy thừa $\sum_{m\ge0}q^m=1/(1-q)$ được đạo hàm từng số hạng:

$$
\sum_{m\ge1}mq^{m-1}=\frac1{(1-q)^2},\qquad\sum_{m\ge2}m(m-1)q^{m-2}=\frac2{(1-q)^3}.
$$

Nhân với $1-q$, và với $q(1-q)$ ở đẳng thức thứ hai:

$$
\mathbb E[N]=\frac{1-q}{(1-q)^2}=\frac1{1-q},\qquad\mathbb E[N(N-1)]=\frac{2q(1-q)}{(1-q)^3}=\frac{2q}{(1-q)^2}.
$$

Lần ghé thứ $k$ xảy ra tại $t=k-1$. Sau đó tác tử còn ở lại $N-k$ lần, mỗi lần phần thưởng $1$, rồi kết thúc với phần thưởng $0$; với $\gamma=1$, lợi tức là $N-k$.

**Câu (c).** Mẫu lần ghé đầu tiên là $N-1$, có kỳ vọng $1/(1-q)-1=q/(1-q)=v_\pi(\mathrm C)$, nên không chệch, đúng như Mệnh đề 05.7 với $k=1$. Trung bình mọi lần ghé của một lượt là

$$
\hat v=\frac1N\sum_{k=1}^{N}(N-k)=\frac1N\cdot\frac{N(N-1)}2=\frac{N-1}2,
$$

có kỳ vọng $(\mathbb E[N]-1)/2=v_\pi(\mathrm C)/2$. Độ chệch của nó là $-v_\pi(\mathrm C)/2$, khác $0$ với mọi $q\in(0,1)$.

**Câu (d).** Theo Bước 1 của chứng minh Định lý 05.17, sau $M$ lượt ước lượng là $\sum_eZ_e/\sum_eN_e$, với $Z_e=N_e(N_e-1)/2$ là tổng các mẫu của lượt $e$. Các cặp $(Z_e,N_e)$ độc lập cùng phân phối theo $e$, có kỳ vọng hữu hạn theo (b). Chia tử và mẫu cho $M$ rồi áp dụng luật mạnh số lớn cho từng dãy; mẫu số hội tụ hầu chắc chắn về $\mathbb E[N]=1/(1-q)>0$, nên thương hội tụ về thương hai giới hạn:

$$
\frac{\frac1M\sum_eZ_e}{\frac1M\sum_eN_e}\to\frac{\mathbb E[N(N-1)]/2}{\mathbb E[N]}=\frac{q/(1-q)^2}{1/(1-q)}=\frac q{1-q}=v_\pi(\mathrm C)
$$

hầu chắc chắn. Độ chệch ở (c) đến từ phép chia cho số mẫu ngẫu nhiên $N$ của chính lượt đó. Trung bình trong một lượt cho mỗi lượt cùng trọng số, nên một lượt dài, có nhiều mẫu lớn, bị gộp thành một số $(N-1)/2$. Tỉ số theo nhiều lượt cho mỗi lượt trọng số tỉ lệ với $N_e$, nên lượt dài góp đúng phần của nó.

**Câu (e).** Các lợi tức tại bốn lần ghé là $3,2,1,0$. Ước lượng lần ghé đầu tiên là $3$; ước lượng mọi lần ghé là $(3+2+1+0)/4=1{,}5=(N-1)/2$.

**Kiểm tra lại.** Với $q=1/2$: $v_\pi(\mathrm C)=1$, $\mathbb E[N]=2$, $\mathbb E[N^2]=\mathbb E[N(N-1)]+\mathbb E[N]=4+2=6$, trung bình mọi lần ghé của một lượt có kỳ vọng $1/2$, đúng Nhận xét 05.18. Hai lỗi thường gặp: kết luận từ một lượt $N=3$ (mẫu $2,1,0$, trung bình $1=v_\pi(\mathrm C)$) rằng mọi lần ghé không chệch, dù không chệch là tính chất của kỳ vọng qua mọi lượt; và coi độ chệch ở (c) là trái với Định lý 05.17. Định lý chỉ khẳng định giới hạn khi $M\to\infty$.
:::

### Bài tập 05.20. Một bước TD(0) từ cùng bảng

**Mức độ:** tính toán. Mục tiêu học tập 4 và 5 của ghi chú bài giảng; mạch 3.

**Nguồn:** Sutton và Barto (2018), §6.1, trang 119–121; Bài tập tuần 5 (2025–2026), bài 3 và bài 7; ghi chú bài giảng, Định nghĩa 05.20, Mệnh đề 05.25, 05.27.

**Trùng trang chiếu:** [Bài tập: một bước TD(0) từ cùng bảng](lecture-05-du-doan-phi-mo-hinh.html#/3/11) và [trang lời giải](lecture-05-du-doan-phi-mo-hinh.html#/3/12), câu (a) và (b). Câu (c) chỉ có trong tệp này.

::: exercise Bài tập 05.20 (Một bước TD(0) từ cùng bảng)
Tàu đổ bộ thu nhỏ: dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$, hai ô biên là trạng thái kết thúc, phần thưởng $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho chuyển khác. Bảng hiện tại $V(\mathrm S)=0{,}25$, $V(\mathrm X)=0{,}5$, $V(\mathrm L)=V(\mathrm G)=0$; bước học $\alpha=0{,}5$; $\gamma=1$. Xét riêng hai trường hợp, mỗi trường hợp bắt đầu từ cùng bảng đã cho:

| Chuyển | Thưởng | Mục tiêu $Y_t$ | Sai số TD $\delta_t$ | $V(\mathrm S)$ sau bước |
| --- | --- | --- | --- | --- |
| $\mathrm S\to\mathrm X$ | $0$ | | | |
| $\mathrm S\to\mathrm L$ | $-1$ | | | |

- (a) Điền ba cột trống của dòng thứ nhất và nêu các phần tử của bảng giữ nguyên.
- (b) Điền ba cột trống của dòng thứ hai và nêu các phần tử của bảng giữ nguyên.
- (c) Mô hình của tàu, chỉ dùng để kiểm, cho chuyển $\mathrm S\to\mathrm X$ với xác suất $0{,}8$ và $\mathrm S\to\mathrm L$ với xác suất $0{,}2$; giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Với bảng đã cho giữ cố định, tính kỳ vọng của $\delta_t$ khi $S_t=\mathrm S$, so với phần dư Bellman $(T_\pi V)(\mathrm S)-V(\mathrm S)$, trong đó $(T_\pi V)(s)=\mathbb E_\pi[R_{t+1}+\gamma V(S_{t+1})\mid S_t=s]$ là toán tử Bellman kỳ vọng, và với sai số thật $v_\pi(\mathrm S)-V(\mathrm S)$, rồi giải thích dấu của kỳ vọng bằng độ chệch của mục tiêu.
:::

::: hint Gợi ý Bài tập 05.20
Tính mục tiêu trước, với giá trị tiếp nối $V(\mathrm X)$ ở dòng đầu và $V(\mathrm L)=0$ ở dòng sau; dòng thứ hai không đọc kết quả của dòng thứ nhất. Ở (c), dùng Mệnh đề 05.27 và công thức độ chệch của Mệnh đề 05.25.
:::

::: solution Lời giải Bài tập 05.20
**Câu (a).** Chuyển $\mathrm S\to\mathrm X$, phần thưởng $0$:

$$
\begin{aligned}
Y_t&=0+1\cdot0{,}5=0{,}5,\\
\delta_t&=0{,}5-0{,}25=0{,}25,\\
V(\mathrm S)&=0{,}25+0{,}5\cdot0{,}25=0{,}375 .
\end{aligned}
$$

$V(\mathrm X)=0{,}5$ và $V(\mathrm L)=V(\mathrm G)=0$ giữ nguyên.

**Câu (b).** Chuyển $\mathrm S\to\mathrm L$, phần thưởng $-1$; $\mathrm L$ là trạng thái kết thúc nên giá trị tiếp nối bằng $0$:

$$
\begin{aligned}
Y_t&=-1+1\cdot0=-1,\\
\delta_t&=-1-0{,}25=-1{,}25,\\
V(\mathrm S)&=0{,}25+0{,}5\cdot(-1{,}25)=-0{,}375 .
\end{aligned}
$$

$V(\mathrm X)=0{,}5$ và $V(\mathrm L)=V(\mathrm G)=0$ giữ nguyên. Phần thưởng $-1$ được tính một lần trong mục tiêu, vì $V(\mathrm L)=0$.

**Câu (c).** Lấy kỳ vọng theo hai chuyển của (a) và (b):

$$
\mathbb E_\pi[\delta_t\mid S_t=\mathrm S]=0{,}8\cdot0{,}25+0{,}2\cdot(-1{,}25)=0{,}2-0{,}25=-0{,}05 .
$$

Phần dư Bellman: $(T_\pi V)(\mathrm S)=0{,}8\cdot(0+0{,}5)+0{,}2\cdot(-1+0)=0{,}2$, nên $(T_\pi V)(\mathrm S)-V(\mathrm S)=0{,}2-0{,}25=-0{,}05$, khớp Mệnh đề 05.27. Sai số thật là $11/21-1/4=23/84\approx0{,}274>0$: bảng đánh giá thấp $\mathrm S$, nhưng kỳ vọng của sai số TD âm. Theo Mệnh đề 05.25, mục tiêu TD tại $\mathrm S$ có độ chệch

$$
\operatorname{bias}(Y;\mathrm S)=1\cdot\Bigl[0{,}8\cdot\Bigl(0{,}5-\frac{19}{21}\Bigr)+0{,}2\cdot0\Bigr]=-\frac{34}{105}\approx-0{,}324,
$$

vì bảng đánh giá thấp trạng thái kế tiếp $\mathrm X$. Do đó $\mathbb E_\pi[\delta_t\mid S_t=\mathrm S]=23/84-34/105=(115-136)/420=-0{,}05$: trị tuyệt đối $0{,}324$ của độ chệch lớn hơn sai số thật $0{,}274$ tại $\mathrm S$, nên kỳ vọng của một bước cập nhật kéo $V(\mathrm S)$ ra xa $v_\pi(\mathrm S)$. Kỳ vọng của giá trị mới là $0{,}25+0{,}5\cdot(-0{,}05)=0{,}225$.

**Kiểm tra lại.** Kỳ vọng của hai giá trị mới ở (a), (b) cũng là $0{,}8\cdot0{,}375+0{,}2\cdot(-0{,}375)=0{,}225$. Ba lỗi thường gặp: cộng $-1$ hai lần bằng cách lấy $V(\mathrm L)=-1$, cho mục tiêu $-2$; tính dòng thứ hai từ $V(\mathrm S)=0{,}375$ của dòng thứ nhất, cho $-0{,}3125$; và suy từ $\delta_t>0$ ở (a), hoặc từ kỳ vọng âm ở (c), dấu của sai số thật.
:::

### Bài tập 05.21. Monte Carlo và TD(0) trên hai lượt với $\gamma=0{,}9$

**Mức độ:** tính toán. Mục tiêu học tập 1, 3 và 4 của ghi chú bài giảng; mạch 3.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 7, đổi hệ số chiết khấu từ $1$ sang $0{,}9$; ghi chú bài giảng, Thuật toán 05.13, 05.21, Ví dụ 05.13.

::: exercise Bài tập 05.21 (Monte Carlo và TD(0) trên hai lượt với $\gamma=0{,}9$)
Tàu đổ bộ thu nhỏ: dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$, chính sách luôn tiến, tàu sang ô bên phải với xác suất $0{,}8$ và sang ô bên trái với xác suất $0{,}2$; phần thưởng $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho chuyển khác. Hai lượt liên tiếp $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,1)$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$ với phần thưởng $(0,0,-1)$. Hệ số chiết khấu $\gamma=0{,}9$; bước học hằng $\alpha=0{,}5$; mỗi phương pháp khởi tạo riêng $V(\mathrm S)=V(\mathrm X)=0$.

- (a) Dùng Monte Carlo lần ghé đầu tiên với bước hằng: tính $(V(\mathrm S);\ V(\mathrm X))$ sau $e_1$ và sau $e_2$.
- (b) Dùng TD(0): tính mục tiêu, sai số TD và bảng sau từng chuyển của $e_1$ và $e_2$.
- (c) So sánh hai bảng sau $e_1$ và sau $e_2$; giải thích phương pháp nào đưa phần thưởng cuối lượt tới $\mathrm S$ sớm hơn trong ví dụ này.
- (d) Với $\gamma=0{,}9$, giá trị chuẩn giải từ mô hình là $v_\pi(\mathrm S)=235/544\approx0{,}4320$ và $v_\pi(\mathrm X)=955/1088\approx0{,}8778$. Kiểm tra hai giá trị này bằng phương trình Bellman kỳ vọng, rồi tính độ lệch của hai bảng sau $e_2$.
:::

::: hint Gợi ý Bài tập 05.21
Lợi tức tại lần ghé đầu tiên của $\mathrm S$ và $\mathrm X$ là $G_0$ và $G_1$. Ở TD(0), mỗi chuyển đọc bảng sau chuyển trước; ba chuyển đầu của $e_1$ có phần thưởng $0$ và giá trị tiếp nối $0$.
:::

::: solution Lời giải Bài tập 05.21
**Câu (a).** Lợi tức tính ngược: $e_1$ cho $G_0=0{,}729$, $G_1=0{,}81$; $e_2$ cho $G_0=-0{,}81$, $G_1=-0{,}9$. Tại $\mathrm S$: $0+0{,}5\cdot0{,}729=0{,}3645$, rồi $0{,}3645+0{,}5\cdot(-0{,}81-0{,}3645)=-0{,}22275$. Tại $\mathrm X$: $0+0{,}5\cdot0{,}81=0{,}405$, rồi $0{,}405+0{,}5\cdot(-0{,}9-0{,}405)=-0{,}2475$. Bảng là $(0{,}3645;\ 0{,}405)$ sau $e_1$ và $(-0{,}22275;\ -0{,}2475)$ sau $e_2$.

**Câu (b).** Mỗi dòng đọc bảng sau dòng trước:

| Lượt | Chuyển | Thưởng | Mục tiêu $Y_t$ | Sai số TD $\delta_t$ | $V(\mathrm S)$ sau bước | $V(\mathrm X)$ sau bước |
| --- | --- | --- | --- | --- | --- | --- |
| $e_1$ | $\mathrm S\to\mathrm X$ | $0$ | $0+0{,}9\cdot0=0$ | $0$ | $0$ | $0$ |
| $e_1$ | $\mathrm X\to\mathrm S$ | $0$ | $0+0{,}9\cdot0=0$ | $0$ | $0$ | $0$ |
| $e_1$ | $\mathrm S\to\mathrm X$ | $0$ | $0+0{,}9\cdot0=0$ | $0$ | $0$ | $0$ |
| $e_1$ | $\mathrm X\to\mathrm G$ | $1$ | $1+0{,}9\cdot0=1$ | $1$ | $0$ | $0{,}5$ |
| $e_2$ | $\mathrm S\to\mathrm X$ | $0$ | $0+0{,}9\cdot0{,}5=0{,}45$ | $0{,}45$ | $0{,}225$ | $0{,}5$ |
| $e_2$ | $\mathrm X\to\mathrm S$ | $0$ | $0+0{,}9\cdot0{,}225=0{,}2025$ | $-0{,}2975$ | $0{,}225$ | $0{,}35125$ |
| $e_2$ | $\mathrm S\to\mathrm L$ | $-1$ | $-1+0{,}9\cdot0=-1$ | $-1{,}225$ | $-0{,}3875$ | $0{,}35125$ |

Bảng TD(0) là $(0;\ 0{,}5)$ sau $e_1$ và $(-0{,}3875;\ 0{,}35125)$ sau $e_2$.

**Câu (c).** Sau $e_1$, Monte Carlo đã cập nhật cả $\mathrm S$ và $\mathrm X$ bằng lợi tức chiết khấu của phần thưởng $+1$; TD(0) chỉ đổi $V(\mathrm X)$, ở chuyển $\mathrm X\to\mathrm G$, và $V(\mathrm S)$ vẫn bằng $0$. Thông tin về $+1$ chỉ tới $\mathrm S$ ở chuyển đầu của $e_2$, qua $V(\mathrm X)=0{,}5$. Phần thưởng $-1$ của $e_2$ thì TD(0) đưa thẳng vào $\mathrm S$ ở chuyển cuối, còn $V(\mathrm X)$ chỉ nhận một phần qua $V(\mathrm S)=0{,}225$ ở chuyển giữa. Vậy Monte Carlo đưa phần thưởng $+1$ của $e_1$ tới $\mathrm S$ sớm hơn: sau $e_1$, $V(\mathrm S)=0{,}3645$ với Monte Carlo và $0$ với TD(0), tức TD(0) chậm một lượt. Với phần thưởng $-1$ của $e_2$, cả hai phương pháp đổi $V(\mathrm S)$ ở cuối $e_2$. Monte Carlo đưa kết quả cuối lượt tới mọi lần ghé được chọn khi lượt kết thúc, còn TD(0) truyền kết quả ngược lại từng chuyển một.

**Câu (d).** Phương trình Bellman kỳ vọng với $\gamma=0{,}9$:

$$
\begin{aligned}
v_\pi(\mathrm S)&=0{,}2\cdot(-1)+0{,}8\cdot0{,}9\,v_\pi(\mathrm X)=-0{,}2+0{,}72\,v_\pi(\mathrm X),\\
v_\pi(\mathrm X)&=0{,}8\cdot1+0{,}2\cdot0{,}9\,v_\pi(\mathrm S)=0{,}8+0{,}18\,v_\pi(\mathrm S).
\end{aligned}
$$

Thế phương trình thứ hai vào phương trình thứ nhất: $v_\pi(\mathrm S)=-0{,}2+0{,}576+0{,}1296\,v_\pi(\mathrm S)$, tức $0{,}8704\,v_\pi(\mathrm S)=0{,}376$, nên $v_\pi(\mathrm S)=0{,}376/0{,}8704=235/544\approx0{,}4320$ và $v_\pi(\mathrm X)=0{,}8+0{,}18\cdot235/544=955/1088\approx0{,}8778$. Độ lệch sau $e_2$:

| Bảng | $V(\mathrm S)-v_\pi(\mathrm S)$ | $V(\mathrm X)-v_\pi(\mathrm X)$ |
| --- | --- | --- |
| Monte Carlo lần ghé đầu tiên | $-0{,}22275-0{,}4320\approx-0{,}655$ | $-0{,}2475-0{,}8778\approx-1{,}125$ |
| TD(0) | $-0{,}3875-0{,}4320\approx-0{,}819$ | $0{,}35125-0{,}8778\approx-0{,}527$ |

Monte Carlo gần giá trị chuẩn hơn tại $\mathrm S$, TD(0) gần hơn tại $\mathrm X$, cùng thứ tự như với $\gamma=1$ (Ví dụ 05.15). Hai lượt không đủ xếp hạng hai phương pháp.

**Kiểm tra lại.** Tại $\mathrm S$, Monte Carlo cho đúng $-0{,}22275$ như câu (b) của Bài tập 05.18. Ba lỗi thường gặp: dùng $\gamma=1$ trong mục tiêu TD, cho $Y=0{,}5$ ở chuyển đầu của $e_2$; dùng $V(\mathrm S)=0$ cũ thay cho $0{,}225$ ở chuyển $\mathrm X\to\mathrm S$, cho $V(\mathrm X)=0{,}25$; và cập nhật Monte Carlo trước khi lượt kết thúc.
:::

### Bài tập 05.22. Độ lệch của bốn cấu hình Monte Carlo sau hai lượt

**Mức độ:** tính toán. Mục tiêu học tập 3 và 5 của ghi chú bài giảng; mạch 4.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 5 và bài 7; ghi chú bài giảng, Ví dụ 05.5, 05.14, 05.15, Mệnh đề 05.11, Định lý 05.16, 05.17, Nhận xét 05.19.

::: exercise Bài tập 05.22 (Độ lệch của bốn cấu hình Monte Carlo sau hai lượt)
Tàu đổ bộ thu nhỏ với hai lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$, phần thưởng $(0,0,0,1)$, và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$, phần thưởng $(0,0,-1)$; $\gamma=1$, nên mọi lợi tức của $e_1$ bằng $1$ và mọi lợi tức của $e_2$ bằng $-1$. Giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Mỗi cấu hình khởi tạo riêng từ bảng $0$; bước hằng dùng $\alpha=0{,}5$. Sau $e_2$, bốn cấu hình cho $(V(\mathrm S);\ V(\mathrm X))$ như sau:

| Cấu hình | Sau $e_2$ |
| --- | --- |
| Lần ghé đầu tiên, trung bình mẫu | $(0;\ 0)$ |
| Mọi lần ghé, trung bình mẫu | $(0;\ 1/3)$ |
| Lần ghé đầu tiên, $\alpha=0{,}5$ | $(-0{,}25;\ -0{,}25)$ |
| Mọi lần ghé, $\alpha=0{,}5$ | $(-0{,}5625;\ -0{,}125)$ |

- (a) Tính độ lệch $V-v_\pi$ của bốn cấu hình tại hai trạng thái, dạng phân số và dạng thập phân ba chữ số.
- (b) Dùng Mệnh đề 05.11 giải thích vì sao tại $\mathrm S$ cấu hình mọi lần ghé với bước hằng lệch xa nhất, còn tại $\mathrm X$ nó gần giá trị chuẩn hơn cấu hình lần ghé đầu tiên cùng bước học.
- (c) Nêu cấu hình nào có độ lệch tiến về $0$ hầu chắc chắn khi số lượt tăng mãi, kèm kết quả và giả thiết, và mức dao động giới hạn tại $\mathrm S$ của cấu hình lần ghé đầu tiên với bước hằng $\alpha=0{,}2$, biết phương sai của một mẫu lần ghé đầu tiên tại $\mathrm S$ là $320/441$.
:::

::: hint Gợi ý Bài tập 05.22
Viết các mẫu theo thứ tự: tại $\mathrm S$, lần ghé đầu tiên chọn $(1,-1)$ và mọi lần ghé chọn $(1,1,-1,-1)$; tại $\mathrm X$, hai dãy là $(1,-1)$ và $(1,1,-1)$. Với $\alpha=0{,}5$, mẫu cách lần cập nhật hiện tại $j$ lần có trọng số $0{,}5^{j+1}$.
:::

::: solution Lời giải Bài tập 05.22
**Câu (a).** Lấy $V$ trừ $v_\pi$:

| Cấu hình | Độ lệch tại $\mathrm S$ | Độ lệch tại $\mathrm X$ |
| --- | --- | --- |
| Lần ghé đầu tiên, trung bình mẫu | $-11/21\approx-0{,}524$ | $-19/21\approx-0{,}905$ |
| Mọi lần ghé, trung bình mẫu | $-11/21\approx-0{,}524$ | $1/3-19/21=-4/7\approx-0{,}571$ |
| Lần ghé đầu tiên, $\alpha=0{,}5$ | $-65/84\approx-0{,}774$ | $-97/84\approx-1{,}155$ |
| Mọi lần ghé, $\alpha=0{,}5$ | $-365/336\approx-1{,}086$ | $-173/168\approx-1{,}030$ |

Chẳng hạn $-0{,}5625-11/21=(-11{,}8125-11)/21=-22{,}8125/21=-365/336$.

**Câu (b).** Tại $\mathrm S$, mọi lần ghé với bước hằng nhận bốn mẫu $(1,1,-1,-1)$. Theo Mệnh đề 05.11 với $n=4$:

$$
V_4=0{,}0625\cdot0+0{,}0625\cdot1+0{,}125\cdot1+0{,}25\cdot(-1)+0{,}5\cdot(-1)=-0{,}5625 .
$$

Hai mẫu $-1$ cuối cùng nhận tổng trọng số $0{,}75$, nên kết cục rơi của $e_2$ chi phối bảng. Lần ghé đầu tiên cùng bước học chỉ nhận một mẫu $-1$, trọng số $0{,}5$: $V_2=0{,}25\cdot0+0{,}25\cdot1+0{,}5\cdot(-1)=-0{,}25$. Tại $\mathrm X$, mọi lần ghé nhận $(1,1,-1)$: $V_3=0{,}125\cdot0+0{,}125\cdot1+0{,}25\cdot1+0{,}5\cdot(-1)=-0{,}125$. Hai mẫu $1$ của $e_1$ kéo giá trị lên $0{,}75$ trước khi gặp mẫu $-1$, nên bảng gần $v_\pi(\mathrm X)\approx0{,}905$ hơn so với $-0{,}25$ của lần ghé đầu tiên.

**Câu (c).** Hai cấu hình dùng bước $1/N(s)$ có độ lệch tiến về $0$ hầu chắc chắn: lần ghé đầu tiên theo Định lý 05.16, mọi lần ghé theo Định lý 05.17, dưới các giả thiết $\mathcal S$ hữu hạn, chính sách cố định, môi trường Markov dừng, lượt kết thúc hầu chắc chắn, phần thưởng bị chặn, lượt độc lập cùng phân phối và mỗi trạng thái được ghé với xác suất dương. Trên tàu đổ bộ thu nhỏ các giả thiết này thỏa. Hai cấu hình dùng bước hằng không hội tụ. Theo Nhận xét 05.19, với lần ghé đầu tiên và $\alpha=0{,}2$, phương sai giới hạn tại $\mathrm S$ là

$$
\frac{\alpha\sigma^2}{2-\alpha}=\frac{0{,}2\cdot320/441}{1{,}8}=\frac{320}{3969}\approx0{,}081,
$$

tức độ lệch chuẩn khoảng $0{,}28$, dù số lượt tăng bao nhiêu. Với $\alpha=0{,}5$ của bảng trong đề, cùng công thức cho $\approx0{,}242$ (Nhận xét 05.19).

**Kiểm tra lại.** Tổng trọng số trong ba khai triển ở (b) đều bằng $1$: $0{,}0625+0{,}0625+0{,}125+0{,}25+0{,}5=1$, $0{,}25+0{,}25+0{,}5=1$, $0{,}125+0{,}125+0{,}25+0{,}5=1$. Hai lỗi thường gặp: dùng độ lệch sau hai lượt để xếp hạng các cấu hình, dù độ lệch ở số lượt hữu hạn còn phụ thuộc thứ tự lượt và khởi tạo; và nhầm độ lệch $V-v_\pi$ với sai số thật $v_\pi-V$, đổi dấu cả bảng.
:::

### Bài tập 05.23. Giá trị chuẩn của dãy năm ô và độ chệch của mục tiêu TD

**Mức độ:** tính toán. Mục tiêu học tập 5 của ghi chú bài giảng; mạch 4.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 6; ghi chú bài giảng, Ví dụ 05.14, 05.17, Định nghĩa 05.24, Mệnh đề 05.25.

::: exercise Bài tập 05.23 (Giá trị chuẩn của dãy năm ô và độ chệch của mục tiêu TD)
Một robot đi trên dãy năm ô $\mathrm c_1,\mathrm c_2,\mathrm c_3,\mathrm c_4,\mathrm c_5$, trong đó $\mathrm c_5$ là trạng thái kết thúc. Chính sách luôn chọn đi sang phải, nhưng hành động có nhiễu: với xác suất $0{,}8$ robot sang ô bên phải, với xác suất $0{,}1$ đứng yên, với xác suất $0{,}1$ sang ô bên trái; nếu hành động đưa robot ra ngoài biên trái thì robot đứng nguyên tại chỗ. Mỗi bước nhận phần thưởng $-1$, riêng chuyển từ $\mathrm c_4$ sang $\mathrm c_5$ nhận $+10$. Hệ số chiết khấu $\gamma=0{,}9$; viết $v_i=v_\pi(\mathrm c_i)$, với $v_5=0$.

- (a) Viết các phương trình Bellman kỳ vọng cho $v_1,\ldots,v_4$.
- (b) Giải hệ để được $v_1,\ldots,v_4$ với ba chữ số thập phân.
- (c) Giải thích vì sao giá trị tăng dần khi robot ở gần $\mathrm c_5$ hơn.
- (d) Một bảng TD được giữ cố định với $V(\mathrm c_1),\ldots,V(\mathrm c_4)=2,4,6,8$ và $V(\mathrm c_5)=0$. Tính kỳ vọng của mục tiêu TD $Y=R_{t+1}+\gamma V(S_{t+1})$ khi $S_t=\mathrm c_3$ và độ chệch $\operatorname{bias}(Y;\mathrm c_3)$; kiểm tra bằng công thức của Mệnh đề 05.25. Làm lại với bảng bằng $0$ ở mọi ô.
:::

::: hint Gợi ý Bài tập 05.23
Tại $\mathrm c_1$, bước sang trái giữ robot ở $\mathrm c_1$, nên robot ở lại với xác suất $0{,}2$. Ở (b), rút $v_1$ theo $v_2$ từ phương trình đầu, rồi thế dần xuống tới phương trình của $v_4$.
:::

::: solution Lời giải Bài tập 05.23
**Câu (a).** Mỗi chuyển có phần thưởng $-1$ trừ chuyển $\mathrm c_4\to\mathrm c_5$, và $v_5=0$:

$$
\begin{aligned}
v_1&=0{,}8\,(-1+0{,}9\,v_2)+0{,}2\,(-1+0{,}9\,v_1),\\
v_2&=0{,}8\,(-1+0{,}9\,v_3)+0{,}1\,(-1+0{,}9\,v_2)+0{,}1\,(-1+0{,}9\,v_1),\\
v_3&=0{,}8\,(-1+0{,}9\,v_4)+0{,}1\,(-1+0{,}9\,v_3)+0{,}1\,(-1+0{,}9\,v_2),\\
v_4&=0{,}8\,(10+0{,}9\cdot0)+0{,}1\,(-1+0{,}9\,v_4)+0{,}1\,(-1+0{,}9\,v_3).
\end{aligned}
$$

Gom các số hạng: $0{,}82\,v_1=-1+0{,}72\,v_2$; $0{,}91\,v_2=-1+0{,}72\,v_3+0{,}09\,v_1$; $0{,}91\,v_3=-1+0{,}72\,v_4+0{,}09\,v_2$; $0{,}91\,v_4=7{,}8+0{,}09\,v_3$.

**Câu (b).** Thế dần, làm tròn năm chữ số ở các hệ số trung gian:

$$
\begin{aligned}
v_1&=-1{,}21951+0{,}87805\,v_2,\\
0{,}83098\,v_2&=-1{,}10976+0{,}72\,v_3,\ \text{tức } v_2=-1{,}33549+0{,}86645\,v_3,\\
0{,}83202\,v_3&=-1{,}12019+0{,}72\,v_4,\ \text{tức } v_3=-1{,}34636+0{,}86536\,v_4,\\
0{,}83212\,v_4&=7{,}67883 .
\end{aligned}
$$

Do đó $v_4\approx9{,}228$, rồi thế ngược: $v_3\approx6{,}639$, $v_2\approx4{,}417$, $v_1\approx2{,}659$.

**Câu (c).** Từ $\mathrm c_i$, robot chỉ tới $\mathrm c_5$ sau khi đi qua các ô ở giữa, nên càng xa $\mathrm c_5$ thì số bước kỳ vọng mang phần thưởng $-1$ càng lớn và phần thưởng $+10$ càng bị chiết khấu nhiều. Các hiệu $v_2-v_1\approx1{,}758$, $v_3-v_2\approx2{,}222$, $v_4-v_3\approx2{,}589$ đều dương. Từ $\mathrm c_4$, với xác suất $0{,}8$ robot nhận ngay $+10$, nên $v_4=8+0{,}1\,(-1+0{,}9\,v_4)+0{,}1\,(-1+0{,}9\,v_3)\approx8+1{,}228$; hai nhánh đứng yên và lùi vẫn có giá trị dương vì robot còn tới $\mathrm c_5$ sau đó.

**Câu (d).** Với bảng $(2,4,6,8)$, khi $S_t=\mathrm c_3$:

$$
\begin{aligned}
\mathbb E_\pi[Y\mid S_t=\mathrm c_3]&=0{,}8\,(-1+0{,}9\cdot8)+0{,}1\,(-1+0{,}9\cdot6)+0{,}1\,(-1+0{,}9\cdot4)\\
&=0{,}8\cdot6{,}2+0{,}1\cdot4{,}4+0{,}1\cdot2{,}6=5{,}66,
\end{aligned}
$$

nên $\operatorname{bias}(Y;\mathrm c_3)=5{,}66-6{,}639\approx-0{,}979$. Theo Mệnh đề 05.25:

$$
\operatorname{bias}(Y;\mathrm c_3)=0{,}9\,\bigl[0{,}8\,(8-9{,}228)+0{,}1\,(6-6{,}639)+0{,}1\,(4-4{,}417)\bigr]\approx0{,}9\cdot(-1{,}088)\approx-0{,}979 .
$$

Số hạng của $\mathrm c_4$ chiếm phần lớn, vì $\mathrm c_4$ là trạng thái kế tiếp có xác suất $0{,}8$. Với bảng bằng $0$, mọi chuyển từ $\mathrm c_3$ có phần thưởng $-1$ và giá trị tiếp nối $0$, nên $\mathbb E_\pi[Y\mid S_t=\mathrm c_3]=-1$ và độ chệch là $-1-6{,}639\approx-7{,}639$; công thức của Mệnh đề 05.25 cho $0{,}9\cdot(-0{,}8\cdot9{,}228-0{,}1\cdot6{,}639-0{,}1\cdot4{,}417)\approx-7{,}639$.

**Kiểm tra lại.** Thế các giá trị làm tròn vào bốn phương trình đã gom: $0{,}82\cdot2{,}659\approx2{,}180$ và $-1+0{,}72\cdot4{,}417\approx2{,}180$; $0{,}91\cdot9{,}228\approx8{,}3975$ và $7{,}8+0{,}09\cdot6{,}639\approx8{,}3975$. Ba lỗi thường gặp: quên rằng ở biên trái robot đứng yên với xác suất $0{,}2$, không phải $0{,}1$; cộng thêm $\gamma v_5$ khác $0$ cho chuyển vào $\mathrm c_5$; và dùng phần thưởng $-1$ thay cho $+10$ trên chuyển $\mathrm c_4\to\mathrm c_5$.
:::

### Bài tập 05.24. Sai số bình phương trung bình của mục tiêu TD

**Mức độ:** chứng minh và tính toán. Mục tiêu học tập 5 của ghi chú bài giảng; mạch 4.

**Nguồn:** ghi chú bài giảng, Định lý 05.28, Nhận xét 05.29 (trường hợp $V(\mathrm X)=0{,}5$ và $V(\mathrm X)=10$), Mệnh đề 05.25; Bài tập tuần 5 (2025–2026), bài 4, được hiệu chỉnh. Phép khảo sát theo $x$ là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 05.24 (Sai số bình phương trung bình của mục tiêu TD)
Tàu đổ bộ thu nhỏ: từ $\mathrm S$, tàu sang $\mathrm X$ với xác suất $0{,}8$ và phần thưởng $0$, sang $\mathrm L$ với xác suất $0{,}2$ và phần thưởng $-1$; $\mathrm L$ là trạng thái kết thúc; $\gamma=1$; $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Lợi tức Monte Carlo tại $\mathrm S$ có $\operatorname{Var}(G_t\mid S_t=\mathrm S)=320/441\approx0{,}726$. Một bảng được giữ cố định với $V(\mathrm X)=x\in\mathbb R$ và $V(\mathrm L)=0$; mục tiêu TD tại $\mathrm S$ là $Y=R_{t+1}+V(S_{t+1})$. Đặt $\operatorname{MSE}(x)=\mathbb E_\pi\bigl[(Y-v_\pi(\mathrm S))^2\mid S_t=\mathrm S\bigr]$, sai số bình phương trung bình của mục tiêu quanh giá trị chuẩn.

- (a) Chứng minh rằng với mọi biến ngẫu nhiên $Y$ có mômen bậc hai hữu hạn và mọi số thực $v$, $\mathbb E[(Y-v)^2]=\operatorname{Var}(Y)+(\mathbb E[Y]-v)^2$.
- (b) Tính $\operatorname{Var}(Y\mid S_t=\mathrm S)$, $\operatorname{bias}(Y;\mathrm S)$ và $\operatorname{MSE}(x)$ theo $x$. Chứng minh $\operatorname{MSE}(x)=0{,}8\,(x-11/21)^2+1024/2205$.
- (c) Tìm tập các $x$ để $\operatorname{Var}(Y\mid S_t=\mathrm S)>320/441$, tập các $x$ để $\operatorname{MSE}(x)<320/441$, và giá trị $x$ làm $\operatorname{MSE}$ nhỏ nhất. So sánh với trường hợp $x=v_\pi(\mathrm X)$, ứng với mục tiêu lý tưởng $Y^*$.
- (d) Rút ra kết luận về nhận định "mục tiêu TD có phương sai thấp hơn mục tiêu Monte Carlo nên tốt hơn".
:::

::: hint Gợi ý Bài tập 05.24
Ở (a), viết $Y-v=(Y-\mathbb E[Y])+(\mathbb E[Y]-v)$ rồi khai triển bình phương. Ở (b), $Y$ chỉ nhận hai giá trị $-1$ và $x$; một biến hai giá trị $a$, $b$ với xác suất $p$, $1-p$ có phương sai $p(1-p)(a-b)^2$.
:::

::: solution Lời giải Bài tập 05.24
**Câu (a).** Đặt $\mu=\mathbb E[Y]$. Khai triển và dùng tính tuyến tính của kỳ vọng:

$$
\begin{aligned}
\mathbb E[(Y-v)^2]&=\mathbb E\bigl[(Y-\mu)^2\bigr]+2(\mu-v)\,\mathbb E[Y-\mu]+(\mu-v)^2\\
&=\operatorname{Var}(Y)+(\mu-v)^2,
\end{aligned}
$$

vì $\mathbb E[Y-\mu]=0$. Mômen bậc hai hữu hạn bảo đảm mọi kỳ vọng ở trên tồn tại. $\square$

**Câu (b).** Với xác suất $0{,}2$, $Y=-1+0=-1$; với xác suất $0{,}8$, $Y=0+x=x$. Do đó

$$
\begin{aligned}
\operatorname{Var}(Y\mid S_t=\mathrm S)&=0{,}2\cdot0{,}8\,(x+1)^2=0{,}16\,(x+1)^2,\\
\operatorname{bias}(Y;\mathrm S)&=(-0{,}2+0{,}8\,x)-\frac{11}{21}=0{,}8\Bigl(x-\frac{19}{21}\Bigr),
\end{aligned}
$$

trong đó đẳng thức thứ hai dùng $0{,}2+11/21=15{,}2/21=0{,}8\cdot19/21$; đây cũng là công thức của Mệnh đề 05.25 với một trạng thái kế tiếp không kết thúc. Theo (a) với $v=v_\pi(\mathrm S)$:

$$
\begin{aligned}
\operatorname{MSE}(x)&=0{,}16\,(x+1)^2+0{,}64\Bigl(x-\frac{19}{21}\Bigr)^2\\
&=0{,}8\,x^2-\frac{88}{105}\,x+\frac{1508}{2205}\\
&=0{,}8\Bigl(x-\frac{11}{21}\Bigr)^2+\frac{1024}{2205}.
\end{aligned}
$$

Dòng thứ hai khai triển hai bình phương: hệ số của $x$ là $0{,}32-1{,}28\cdot19/21=-17{,}6/21=-88/105$, hằng số là $0{,}16+0{,}64\cdot361/441=301{,}6/441=1508/2205$. Dòng thứ ba bù bình phương: $0{,}8\cdot(11/21)^2=96{,}8/441$ và $1508/2205-96{,}8/441=(1508-484)/2205=1024/2205$.

**Câu (c).** Phương sai: $0{,}16\,(x+1)^2>320/441$ khi và chỉ khi $(x+1)^2>2000/441$, tức $\lvert x+1\rvert>\sqrt{2000}/21\approx2{,}130$, nên $x>1{,}130$ hoặc $x<-3{,}130$.

Sai số bình phương trung bình: $\operatorname{MSE}(x)<320/441=1600/2205$ khi và chỉ khi $0{,}8\,(x-11/21)^2<576/2205$, tức $(x-11/21)^2<16/49$, hay $\lvert x-11/21\rvert<12/21$. Tập cần tìm là $-1/21<x<23/21$, tức khoảng $(-0{,}048;\ 1{,}095)$.

Giá trị nhỏ nhất của $\operatorname{MSE}$ đạt tại $x=11/21\approx0{,}524$, với $\operatorname{MSE}=1024/2205\approx0{,}464$; khi đó độ chệch là $0{,}8\,(11/21-19/21)\approx-0{,}305$. Tại $x=19/21$, mục tiêu là $Y^*$: độ chệch $0$ và $\operatorname{MSE}=\operatorname{Var}(Y^*)=0{,}16\,(40/21)^2=256/441\approx0{,}580$, nhỏ hơn $320/441$ đúng như Định lý 05.28, nhưng lớn hơn giá trị nhỏ nhất $0{,}464$.

**Câu (d).** Nhận định sai ở hai chỗ. Thứ nhất, phương sai của mục tiêu TD phụ thuộc bảng: với $x>1{,}130$ hoặc $x<-3{,}130$ nó lớn hơn $\operatorname{Var}(G_t)$; Định lý 05.28 chỉ áp dụng cho $Y^*$, dùng $v_\pi$. Thứ hai, phương sai thấp không đủ: với $1{,}095<x<1{,}130$ hoặc $-3{,}130<x<-0{,}048$, mục tiêu TD có phương sai nhỏ hơn $G_t$ nhưng sai số bình phương trung bình lớn hơn, vì bình phương độ chệch bù phần phương sai giảm được. Kết luận nói về một mục tiêu với bảng cố định và không so sánh sai số của hai thuật toán, vốn còn phụ thuộc bước học, khởi tạo và dữ liệu (phạm vi của Định lý 05.28).

**Kiểm tra lại.** Với $x=0{,}5$: $\operatorname{MSE}=0{,}36+0{,}64\cdot(0{,}5-19/21)^2\approx0{,}36+0{,}105=0{,}465$; với $x=10$: $\operatorname{MSE}=19{,}36+\bigl[0{,}8\,(10-19/21)\bigr]^2\approx19{,}36+52{,}94\approx72{,}3$; hai số khớp Nhận xét 05.29. Hai lỗi thường gặp: tính $\operatorname{Var}(Y)$ bằng $0{,}16\,(x-1)^2$, quên rằng giá trị của nhánh rơi là $-1$; và đồng nhất giá trị $x$ làm $m$ nhỏ nhất với giá trị chuẩn $19/21$.
:::

### Bài tập 05.12. Hai nghiệm trên tám lượt $\mathrm A$, $\mathrm B$

**Mức độ:** tính toán. Mục tiêu học tập 6 của ghi chú bài giảng; mạch 5. Câu (a) giữ số hiệu, đề, gợi ý và lời giải của ghi chú bài giảng (Mục 5.3); câu (b) theo trang chiếu.

**Nguồn:** ghi chú bài giảng, Bài tập 05.12, Ví dụ 05.20–05.22, Mệnh đề 05.33, 05.34, Nhận xét 05.35; Sutton và Barto (2018), §6.3, Ví dụ 6.4, trang 127–128.

**Trùng trang chiếu:** [Bài tập: hai nghiệm trên tám lượt $\mathrm A$, $\mathrm B$](lecture-05-du-doan-phi-mo-hinh.html#/5/8) và [trang lời giải](lecture-05-du-doan-phi-mo-hinh.html#/5/9).

::: exercise Bài tập 05.12 (Hai nghiệm trên tám lượt $\mathrm A$, $\mathrm B$)
Dữ kiện: tập dữ liệu cố định gồm tám lượt, một lượt $\mathrm A\xrightarrow{0}\mathrm B\xrightarrow{0}$ kết thúc, sáu lượt $\mathrm B\xrightarrow{1}$ kết thúc, một lượt $\mathrm B\xrightarrow{0}$ kết thúc (Ví dụ 05.20); $\gamma=1$, $\alpha=1/8$. Cập nhật theo lô giữ bảng cố định trong mỗi lượt quét và ghi tổng gia số ở cuối lượt quét. Bảng sau lượt quét đầu là $V_1=(0;\ 3/4)$ cho cả hai phương pháp; nghiệm Monte Carlo theo lô là $(0;\ 3/4)$ và nghiệm TD theo lô là $(3/4;\ 3/4)$.

- (a) Tính $V_3(\mathrm A)$ của TD theo lô.
- (b) Giải thích hai nghiệm khác nhau tại $\mathrm A$ bằng tiêu chuẩn mà mỗi phương pháp khớp.
:::

::: hint Gợi ý Bài tập 05.12
Ở (a), $V_k(\mathrm B)=3/4$ với mọi $k\ge1$, nên mỗi lượt quét dịch $V(\mathrm A)$ về phía $3/4$ một phần $\alpha=1/8$ khoảng cách; tính $V_2(\mathrm A)$ rồi $V_3(\mathrm A)$. Ở (b), xét dữ liệu mà mỗi mục tiêu dùng cho $\mathrm A$.
:::

::: solution Lời giải Bài tập 05.12
**Câu (a).** $V_2(\mathrm A)=0+\tfrac18\bigl(\tfrac34-0\bigr)=\tfrac3{32}$, rồi $V_3(\mathrm A)=\tfrac3{32}+\tfrac18\bigl(\tfrac34-\tfrac3{32}\bigr)=\tfrac3{32}+\tfrac{21}{256}=\tfrac{45}{256}\approx0{,}176$. Cách khác: theo công thức đóng của Ví dụ 05.22, $V_3(\mathrm A)=\tfrac34\bigl[1-(7/8)^2\bigr]=\tfrac34\cdot\tfrac{15}{64}=\tfrac{45}{256}$.

**Câu (b).** Monte Carlo theo lô khớp lợi tức duy nhất $0$ của lượt qua $\mathrm A$ (Mệnh đề 05.33). TD theo lô khớp quá trình phần thưởng Markov thực nghiệm: chuyển $\mathrm A\to\mathrm B$ với phần thưởng $0$ và $V(\mathrm B)=3/4$ ước lượng từ tám lần ghé $\mathrm B$ (Mệnh đề 05.34). Hai nghiệm theo hai tiêu chuẩn; tám lượt không đủ để chọn nghiệm đúng hơn với mọi môi trường (Nhận xét 05.35).

**Kiểm tra lại.** Hai cách cho cùng $45/256$, khớp trang lời giải. Ba lỗi thường gặp: dùng mục tiêu Monte Carlo $0$ tại $\mathrm A$ cho phép quét TD, cho $V_3(\mathrm A)=0$; ghi bảng ngay sau mỗi mẫu trong một lượt quét; và gọi một nghiệm là đúng mà không nêu tiêu chuẩn.
:::

### Bài tập 05.25. Hai nghiệm theo lô trên ba lượt

**Mức độ:** tính toán. Mục tiêu học tập 6 của ghi chú bài giảng; mạch 5.

**Nguồn:** ghi chú bài giảng, Thuật toán 05.32, Mệnh đề 05.33, 05.34, Nhận xét 05.35; Sutton và Barto (2018), §6.3, trang 126–128. Bộ ba lượt là số liệu sư phạm tự xây dựng theo cấu trúc của Ví dụ 6.4 trong sách.

::: exercise Bài tập 05.25 (Hai nghiệm theo lô trên ba lượt)
Tập dữ liệu cố định $\mathcal D$ gồm ba lượt đã kết thúc, với $\mathcal S=\{\mathrm A,\mathrm B\}$ và $\gamma=1$:

| Lượt | Trạng thái và phần thưởng |
| --- | --- |
| thứ nhất | $\mathrm A\xrightarrow{1}\mathrm B\xrightarrow{0}$ kết thúc |
| thứ hai | $\mathrm B\xrightarrow{1}$ kết thúc |
| thứ ba | $\mathrm B\xrightarrow{1}$ kết thúc |

Cập nhật theo lô (Thuật toán 05.32) dùng bước học $\alpha=1/3$ và bảng đầu $V_0(\mathrm A)=V_0(\mathrm B)=0$; Monte Carlo theo lô dùng mọi lần ghé.

- (a) Tính nghiệm Monte Carlo theo lô và nghiệm TD theo lô. Mô tả quá trình phần thưởng Markov (Markov reward process, MRP) thực nghiệm $(\hat P,\hat r)$ dùng cho nghiệm TD, và kiểm tra điều kiện bước học của hai mệnh đề.
- (b) Tính $V_1$, $V_2$, $V_3$ của hai phương pháp; tìm công thức đóng của $V_k(\mathrm A)$.
- (c) Tính tổng sai số TD tại $\mathrm A$ của nghiệm Monte Carlo, và tổng bình phương $\sum_i(G_i-V(S_i))^2$ trên $\mathcal D$ của nghiệm TD. Giải thích hai nghiệm bằng hai tiêu chuẩn.
- (d) TD theo lô dừng khi thay đổi lớn nhất giữa hai bảng liên tiếp nhỏ hơn $\theta=0{,}01$. Xác định lượt quét dừng, bảng trả về tại $\mathrm A$ và khoảng cách của nó tới nghiệm.
:::

::: hint Gợi ý Bài tập 05.25
$\mathrm A$ có $N(\mathrm A)=1$ lần ghé, $\mathrm B$ có $N(\mathrm B)=3$ lần ghé với lợi tức $0,1,1$. Với $\alpha N(\mathrm B)=1$, $V_1(\mathrm B)$ đã bằng nghiệm. Từ lượt quét thứ hai, truy hồi tại $\mathrm A$ có dạng $V_{k+1}(\mathrm A)=V_k(\mathrm A)+\tfrac13\bigl(y-V_k(\mathrm A)\bigr)$ với $y$ không đổi.
:::

::: solution Lời giải Bài tập 05.25
**Câu (a).** Monte Carlo theo lô: theo Mệnh đề 05.33, nghiệm tại mỗi trạng thái là trung bình các lợi tức tại đó. Lợi tức duy nhất tại $\mathrm A$ là $1+0=1$; ba lợi tức tại $\mathrm B$ là $0,1,1$. Nghiệm là $(V(\mathrm A);\ V(\mathrm B))=(1;\ 2/3)$.

TD theo lô: MRP thực nghiệm có $\hat P(\mathrm B\mid\mathrm A)=1$, $\hat r(\mathrm A)=1$; từ $\mathrm B$ mọi chuyển vào trạng thái kết thúc, $\hat r(\mathrm B)=(0+1+1)/3=2/3$. Phương trình $V=\hat TV$ cho $V(\mathrm B)=2/3$ và $V(\mathrm A)=1+V(\mathrm B)=5/3$. Nghiệm là $(5/3;\ 2/3)$ theo Mệnh đề 05.34.

Điều kiện bước học: $\alpha N(\mathrm A)=1/3$ và $\alpha N(\mathrm B)=1$ thỏa $0<\alpha N(s)<2$ của Mệnh đề 05.33 và $0<\alpha N(s)\le1$ của Mệnh đề 05.34.

**Câu (b).** Lượt quét đầu, từ $V_0=0$:

$$
\begin{aligned}
\text{Monte Carlo: }\Delta_0(\mathrm A)&=\tfrac13(1-0)=\tfrac13,\quad\Delta_0(\mathrm B)=\tfrac13\bigl[(0-0)+(1-0)+(1-0)\bigr]=\tfrac23,\\
\text{TD: }\Delta_0(\mathrm A)&=\tfrac13\bigl(1+V_0(\mathrm B)-V_0(\mathrm A)\bigr)=\tfrac13,\quad\Delta_0(\mathrm B)=\tfrac23 .
\end{aligned}
$$

Cả hai cho $V_1=(1/3;\ 2/3)$. Từ đó tổng sai lệch tại $\mathrm B$ bằng $(0-\tfrac23)+2(1-\tfrac23)=0$, nên $V_k(\mathrm B)=2/3$ với mọi $k\ge1$. Tại $\mathrm A$, Monte Carlo dùng mục tiêu $1$ và TD dùng mục tiêu $1+\tfrac23=\tfrac53$:

| Bảng | Monte Carlo $V_k(\mathrm A)$ | TD $V_k(\mathrm A)$ |
| --- | --- | --- |
| $V_1$ | $1/3$ | $1/3$ |
| $V_2$ | $\tfrac13+\tfrac13\bigl(1-\tfrac13\bigr)=5/9$ | $\tfrac13+\tfrac13\bigl(\tfrac53-\tfrac13\bigr)=7/9$ |
| $V_3$ | $\tfrac59+\tfrac13\bigl(1-\tfrac59\bigr)=19/27$ | $\tfrac79+\tfrac13\bigl(\tfrac53-\tfrac79\bigr)=29/27$ |

Mỗi lượt quét nhân khoảng cách tới mục tiêu với $1-\tfrac13=\tfrac23$. Monte Carlo: $V_k(\mathrm A)=1-(2/3)^k$ với $k\ge0$. TD: $\tfrac53-V_k(\mathrm A)=(2/3)^{k-1}\bigl(\tfrac53-\tfrac13\bigr)$, tức $V_k(\mathrm A)=\tfrac53-\tfrac43(2/3)^{k-1}$ với $k\ge1$.

**Câu (c).** Tại nghiệm Monte Carlo $(1;\ 2/3)$, sai số TD của chuyển duy nhất rời $\mathrm A$ là $1+\tfrac23-1=\tfrac23\ne0$, nên nghiệm này không phải điểm bất động của phép quét TD. Tại nghiệm TD $(5/3;\ 2/3)$, tổng bình phương trên $\mathcal D$ là $(1-\tfrac53)^2$ tại $\mathrm A$ cộng $(0-\tfrac23)^2+2(1-\tfrac23)^2=\tfrac23$ tại $\mathrm B$, tức $\tfrac49+\tfrac23=\tfrac{10}9$, lớn hơn $\tfrac23$ của nghiệm Monte Carlo. Monte Carlo theo lô khớp lợi tức đã quan sát, cực tiểu tổng bình phương (Mệnh đề 05.33); TD theo lô khớp MRP thực nghiệm, dùng cả ba lần ghé $\mathrm B$ cho phần lượt sau $\mathrm A$ (Mệnh đề 05.34, Nhận xét 05.35). Ba lượt không đủ để gọi một nghiệm là đúng hơn với môi trường thật.

**Câu (d).** Theo Thuật toán 05.32, lượt quét $k$ ($k=0,1,\ldots$; $k=0$ là lượt quét đầu) biến $V_k$ thành $V_{k+1}$. Với $k\ge1$, thay đổi ở lượt quét $k$ chỉ còn tại $\mathrm A$: $V_{k+1}(\mathrm A)-V_k(\mathrm A)=\tfrac13\cdot\tfrac43(2/3)^{k-1}=\tfrac49(2/3)^{k-1}$. Thay đổi này bằng khoảng $0{,}0116$ khi $k=10$ và khoảng $0{,}0077<\theta$ khi $k=11$, nên thuật toán dừng ở lượt quét $k=11$, tức lượt quét thứ $12$, và trả về $V_{12}(\mathrm A)=\tfrac53-\tfrac43(2/3)^{11}\approx1{,}6513$. Khoảng cách tới nghiệm là $\tfrac43(2/3)^{11}\approx0{,}0154$, gấp đôi thay đổi cuối cùng và lớn hơn $\theta$, vì mỗi lượt quét chỉ thu hẹp khoảng cách theo hệ số $2/3$.

**Kiểm tra lại.** Công thức đóng của TD cho $V_2(\mathrm A)=\tfrac53-\tfrac43\cdot\tfrac23=\tfrac79$ và $V_3(\mathrm A)=\tfrac53-\tfrac43\cdot\tfrac49=\tfrac{29}{27}$, khớp bảng. Ba lỗi thường gặp: lấy lợi tức tại $\mathrm A$ bằng $0$ vì chuyển cuối có phần thưởng $0$, quên phần thưởng $1$ của chuyển $\mathrm A\to\mathrm B$; cập nhật bảng ngay sau mỗi mẫu trong một lượt quét thay vì giữ $V_k$ cố định; và coi $\theta$ là chặn của khoảng cách tới nghiệm.
:::

### Bài tập 05.8. Tàu đổ bộ thu nhỏ, lượt thứ ba

**Mức độ:** tính toán, bài tổng hợp. Mục tiêu học tập 3 và 4 của ghi chú bài giảng; mạch 4 trong ghi chú (Mục 4.1), mạch 6 trên trang chiếu. Bài giữ số hiệu, đề, gợi ý và lời giải của ghi chú bài giảng; dữ kiện của hai lượt đầu được nêu lại trong đề.

**Nguồn:** ghi chú bài giảng, Bài tập 05.8, Ví dụ 05.5, 05.9, 05.10, 05.14, 05.15.

**Trùng trang chiếu:** [Bài tập: tàu đổ bộ thu nhỏ, lượt thứ ba](lecture-05-du-doan-phi-mo-hinh.html#/6/6) và [trang lời giải](lecture-05-du-doan-phi-mo-hinh.html#/6/7).

::: exercise Bài tập 05.8 (Tàu đổ bộ thu nhỏ, lượt thứ ba)
Dữ kiện: tàu đổ bộ thu nhỏ, dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$, phần thưởng $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho chuyển khác; $\gamma=1$, $\alpha=0{,}5$, giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Hai lượt đầu là $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,1)$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$ với phần thưởng $(0,0,-1)$. Mỗi phương pháp khởi tạo riêng từ bảng $0$. Sau $e_1$, $e_2$, Monte Carlo lần ghé đầu tiên với bước hằng cho $(V(\mathrm S);\ V(\mathrm X))=(-0{,}25;\ -0{,}25)$, còn TD(0) cho $(-0{,}375;\ 0{,}375)$. Lượt thứ ba là $e_3:\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,1)$.

- (a) Tiếp tục mỗi phương pháp trên $e_3$.
- (b) Tính độ lệch $V-v_\pi$ của hai bảng và so với độ lệch sau $e_2$, là $(-0{,}774;\ -1{,}155)$ cho Monte Carlo và $(-0{,}899;\ -0{,}530)$ cho TD(0) (Ví dụ 05.15).
:::

::: hint Gợi ý Bài tập 05.8
Hai lợi tức của $e_3$ đều bằng $1$; ở TD(0), chuyển thứ hai đọc bảng sau chuyển thứ nhất.
:::

::: solution Lời giải Bài tập 05.8
**Câu (a).** Monte Carlo: $V(\mathrm S)=-0{,}25+0{,}5\cdot(1+0{,}25)=0{,}375$ và $V(\mathrm X)=0{,}375$ theo cùng phép tính.

TD(0), chuyển $\mathrm S\to\mathrm X$:

$$
\begin{aligned}
Y&=0+0{,}375=0{,}375,\\
\delta&=0{,}375-(-0{,}375)=0{,}75,\\
V(\mathrm S)&=-0{,}375+0{,}5\cdot0{,}75=0 .
\end{aligned}
$$

Chuyển $\mathrm X\to\mathrm G$:

$$
\begin{aligned}
Y&=1+0=1,\\
\delta&=1-0{,}375=0{,}625,\\
V(\mathrm X)&=0{,}375+0{,}5\cdot0{,}625=0{,}6875 .
\end{aligned}
$$

**Câu (b).** Monte Carlo lệch $-25/168\approx-0{,}149$ tại $\mathrm S$ và $-89/168\approx-0{,}530$ tại $\mathrm X$; TD(0) lệch $-11/21\approx-0{,}524$ và $-73/336\approx-0{,}217$. So với sau $e_2$ (Ví dụ 05.15), cả hai bảng gần giá trị chuẩn hơn ở cả hai trạng thái; Monte Carlo vẫn gần hơn tại $\mathrm S$, TD(0) gần hơn tại $\mathrm X$.

**Kiểm tra lại.** $0{,}5\cdot0{,}75$ bù đúng $-0{,}375$, nên $V(\mathrm S)=0$. Kết quả khớp trang lời giải: Monte Carlo $(0{,}375;\ 0{,}375)$, TD(0) $(0;\ 0{,}6875)$, độ lệch $(-0{,}149;\ -0{,}530)$ và $(-0{,}524;\ -0{,}217)$. Ba lỗi thường gặp: ở chuyển $\mathrm S\to\mathrm X$ của TD(0), đọc $V(\mathrm X)=0{,}5$ của bảng sau $e_1$ thay cho $0{,}375$ sau $e_2$, cho $V(\mathrm S)=0{,}0625$; cập nhật Monte Carlo trước khi $e_3$ kết thúc; và kết luận từ ba lượt rằng một phương pháp tốt hơn. Kết quả còn phụ thuộc bước hằng $0{,}5$, khởi tạo $0$ và thứ tự các lượt.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 05.26. [Lập trình] Tự chuyển trên Lunar Lander và lịch bước học của TD(0)

**Mức độ:** vận dụng. Mục tiêu học tập 4 và 5 của ghi chú bài giảng; mạch 3.

**Nguồn:** notebook thực hành Bài 05, phần 5, mục 7.1, mục 8.1 và nhiệm vụ 4 của phần 12 (một lần chạy đã nhúng, gymnasium 1.3.0); ghi chú bài giảng, Ví dụ 05.12, Nhận xét 05.22, Định lý 05.30, Mục 4.4.

::: exercise Bài tập 05.26 ([Lập trình] Tự chuyển trên Lunar Lander và lịch bước học của TD(0))
Notebook thực hành đánh giá một chính sách cố định trên `LunarLander-v3` (rời rạc, không gió) với $\gamma=0{,}99$. Quan sát tám chiều được gộp thành $9216$ ô; mỗi bước mô phỏng dài $0{,}02$ giây, và trong tập huấn luyện $2000$ lượt, $70\%$ số chuyển không đi vào trạng thái kết thúc là tự chuyển (self-transition) $S_{t+1}=S_t$. Ở một tự chuyển với phần thưởng $r$, cập nhật TD(0) đọc $V(s)$ ở cả hai vế trước khi ghi, nên $V(s)\leftarrow V(s)+\alpha_n\bigl[r-(1-\gamma)V(s)\bigr]$, và khoảng cách tới điểm cố định $r/(1-\gamma)$ được nhân với $1-\alpha_n(1-\gamma)$; $n$ là số thứ tự cập nhật của riêng ô $s$. Notebook in $J$, trung bình của $(G_t-V(S_t))^2$ trên $131\,278$ mẫu của $493$ lượt kiểm tra kết thúc thật, sau $2000$ lượt huấn luyện, trung bình qua năm thứ tự lượt:

| Bảng | $J$ |
| --- | --- |
| Monte Carlo mọi lần ghé, bước $1/N(s)$ | $1627$ |
| TD(0), $\alpha=0{,}5$ | $2085$ |
| TD(0), $\alpha_n=n^{-0{,}6}$ | $2962$ |
| TD(0), $\alpha_n=1/n$ | $5086$ |
| bảng $\mathbf 0$ (để đối chiếu) | $5797$ |

- (a) Xét một ô chỉ có tự chuyển với cùng phần thưởng $r$. Với $\alpha_n=1/n$, viết hệ số thu hẹp khoảng cách sau $n$ cập nhật thành một tích; dùng xấp xỉ tích bằng $n^{-(1-\gamma)}$ để ước lượng số cập nhật cần cho khoảng cách còn không quá $10\%$ khoảng cách ban đầu. So sánh với bước hằng $\alpha=0{,}5$, cần $460$ cập nhật, và với $\alpha_n=n^{-0{,}6}$.
- (b) Lịch $\alpha_n=1/n$ thỏa điều kiện Robbins–Monro. Giải thích vì sao $J=5086$ không mâu thuẫn với Định lý 05.30.
- (c) Giải thích vì sao Monte Carlo không bị chuỗi tự chuyển làm chậm.
- (d) Cài đặt nhiệm vụ 4 của notebook: thay mỗi chuỗi $m$ bước liên tiếp trong cùng một ô bằng một chuyển với phần thưởng $\sum_{i=0}^{m-1}\gamma^iR_{t+i+1}$ và hệ số $\gamma^m$ cho giá trị tiếp nối. Viết quy tắc cập nhật; chứng minh rằng khi trạng thái là Markov và bảng bằng $v_\pi$, mục tiêu mới có kỳ vọng $v_\pi(s)$; nêu các đại lượng cần đo và cách đọc kết quả.
:::

::: hint Gợi ý Bài tập 05.26
Ở (a), $\ln\prod_{k=1}^{n}(1-c/k)\approx-c\sum_{k=1}^{n}1/k\approx-c(\ln n+0{,}577)$ với $c=1-\gamma=0{,}01$, nên tích xấp xỉ $0{,}994\,n^{-c}$; bỏ hằng số được $n^{-c}$. Với $\alpha_n=n^{-0{,}6}$, dùng $\ln\prod_k(1-0{,}01\,k^{-0{,}6})\approx-0{,}01\sum_{k\le n}k^{-0{,}6}$ với $\sum_{k\le n}k^{-0{,}6}\approx n^{0{,}4}/0{,}4$, hoặc tính tích bằng một vòng lặp. Ở (d), gọi $\tau$ là số bước tới lần đầu rời ô $s$ hoặc tới thời điểm kết thúc; biến cố $\{\tau=j\}$ được xác định bởi lịch sử tới thời điểm $t+j$, như biến cố "lần ghé thứ $k$" trong chứng minh Mệnh đề 05.7.
:::

::: solution Lời giải Bài tập 05.26
**Câu (a).** Ở cập nhật thứ $k$ của ô, hệ số là $1-(1-\gamma)/k=1-0{,}01/k$, nên sau $n$ cập nhật khoảng cách còn $\prod_{k=1}^{n}(1-0{,}01/k)\approx n^{-0{,}01}$ lần khoảng cách ban đầu. Điều kiện $n^{-0{,}01}\le0{,}1$ tương đương $n\ge10^{100}$; hằng số $0{,}994$ bị bỏ không đổi bậc độ lớn này. Lịch $1/n$ vì vậy không thu hẹp đáng kể khoảng cách trong số cập nhật thực tế: sau $10^4$ cập nhật, khoảng cách mới giảm khoảng $9\%$. Notebook in hệ số $n^{-0{,}01}\approx0{,}912$ với $n=10^4$; các ô chứa trạng thái đầu của lượt kiểm tra có trung bình $580$ cập nhật, và nếu mọi cập nhật đều là tự chuyển thì khoảng cách còn khoảng $580^{-0{,}01}\approx0{,}94$ lần ban đầu.

| Lịch bước học | Số cập nhật để còn $10\%$ |
| --- | --- |
| $\alpha=0{,}5$ hằng, hệ số $0{,}995$ | $460$ (Bài tập 05.7 của ghi chú) |
| $\alpha_n=n^{-0{,}6}$, tích $\prod_k(1-0{,}01\,k^{-0{,}6})$ tính bằng vòng lặp | khoảng $8{,}3\cdot10^4$ |
| $\alpha_n=1/n$, xấp xỉ $n^{-0{,}01}$ | khoảng $10^{100}$ (bậc độ lớn) |

Thứ tự này trùng thứ tự $J$ của ba cấu hình TD(0) trong bảng của đề.

**Câu (b).** $\sum_n1/n=\infty$ và $\sum_n1/n^2<\infty$, nên lịch $1/n$ thỏa giả thiết bước học. Định lý 05.30 là bảo đảm tiệm cận: nó khẳng định giới hạn khi số chuyển tiến tới vô hạn và không cho tốc độ. Hơn nữa, ô gộp không Markov, nên định lý không áp dụng nguyên văn (Nhận xét 05.31). Notebook in tỉ số có trọng số

$$
\frac{\sum_sN(s)V_{1/n}(s)}{\sum_sN(s)V_{\mathrm{MC}}(s)}\approx0{,}084 .
$$

Sau $2000$ lượt, bảng TD(0) với $1/n$ mới rời giá trị khởi tạo $0$ một phần nhỏ, nên $J=5086$ gần $5797$ của bảng $\mathbf 0$.

**Câu (c).** Mục tiêu Monte Carlo là $G_t$, đã chứa mọi phần thưởng về sau, kể cả phần thưởng $\pm100$ ở cuối lượt; nó không đọc giá trị của ô kế tiếp, nên số bước tàu ở lại một ô không làm chậm việc đưa thông tin cuối lượt vào bảng. Với bước $1/N(s)$, mẫu đầu tiên xóa hẳn giá trị khởi tạo (Mệnh đề 05.9).

**Câu (d).** *Quy tắc cập nhật.* Với một chuỗi bắt đầu tại $S_t=s$ và kéo dài $m$ bước trong ô $s$, mục tiêu là

$$
Y=\sum_{i=0}^{m-1}\gamma^iR_{t+i+1}+\gamma^mV(S_{t+m}),
$$

với $V(S_{t+m})=0$ khi $S_{t+m}$ là trạng thái kết thúc, rồi $V(s)\leftarrow V(s)+\alpha_n(s)\,[Y-V(s)]$, một cập nhật cho cả chuỗi. Nếu lượt bị cắt ngắn khi tàu còn ở ô $s$, giá trị tiếp nối vẫn là $V(s)$, không phải $0$ (Nhận xét 05.22).

*Kỳ vọng của mục tiêu.* Giả sử trạng thái là Markov, phần thưởng bị chặn và lượt kết thúc hầu chắc chắn (Bổ đề 05.5). Gọi $\tau=\min\{j\ge1: S_{t+j}\ne s\}\wedge(T-t)$.

- *Bước 1.* Lặp Mệnh đề 05.4 $\tau$ lần: $G_t=\sum_{i=0}^{\tau-1}\gamma^iR_{t+i+1}+\gamma^\tau G_{t+\tau}$.
- *Bước 2.* Biến cố $\{\tau=j\}$ chỉ phụ thuộc $S_t,\ldots,S_{t+j}$, tức được xác định bởi lịch sử $H_{t+j}$. Như Bước 2 của chứng minh Mệnh đề 05.7, luật kỳ vọng lặp và $\mathbb E_\pi[G_{t+j}\mid H_{t+j}]=v_\pi(S_{t+j})$ cho $\mathbb E_\pi\bigl[G_{t+j}\mathbf 1\{\tau=j\}\mid S_t=s\bigr]=\mathbb E_\pi\bigl[v_\pi(S_{t+j})\mathbf 1\{\tau=j\}\mid S_t=s\bigr]$.
- *Bước 3.* Nhân đẳng thức của Bước 2 với $\gamma^j$, cộng thêm phần thưởng của $j$ bước đầu, rồi cộng theo $j\ge1$. Các biến cố $\{\tau=j\}$, $j\ge1$, rời nhau và phủ toàn bộ không gian vì $\tau\le T-t<\infty$ hầu chắc chắn; đổi thứ tự tổng và kỳ vọng hợp lệ vì $\lvert G\rvert\le R_{\max}T$ và $\mathbb E[T]<\infty$. Theo Bước 1:

$$
\mathbb E_\pi\Bigl[\sum_{i=0}^{\tau-1}\gamma^iR_{t+i+1}+\gamma^\tau v_\pi(S_{t+\tau})\Bigm| S_t=s\Bigr]=\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s). \qquad\square
$$

Vậy khi $V=v_\pi$, mục tiêu gộp không chệch tại $s$; với bảng khác $v_\pi$, độ chệch của nó là $\mathbb E_\pi[\gamma^\tau(V-v_\pi)(S_{t+\tau})\mid S_t=s]$, cùng dạng Mệnh đề 05.25 với $\gamma$ thay bằng $\gamma^\tau$. Trên ô gộp, giả thiết Markov không thỏa, nên kết luận này là căn cứ để thử nghiệm và không bảo đảm kết quả trên Lunar Lander.

*Đo và đọc kết quả.* Dùng cùng dữ liệu huấn luyện, cùng năm thứ tự lượt và các điểm đo của mục 8.1; vẽ đường $J$ của TD gộp và TD(0) thường với $\alpha=0{,}5$ và với $\alpha_n=1/n$; in số cập nhật của mỗi cách. Nếu cơ chế ở (a) là nguyên nhân chính làm TD(0) chậm, đường của TD gộp với $1/n$ phải giảm rõ so với $5086$; nếu đường không đổi, nguyên nhân nằm ở chỗ khác, chẳng hạn ô không Markov hoặc khởi tạo $\mathbf 0$. Kết luận chỉ áp dụng cho cách chia ô, dữ liệu và phiên bản gói đã dùng.

**Kiểm tra lại.** Với $n=10^4$, $10^{4\cdot(-0{,}01)}=10^{-0{,}04}\approx0{,}912$, khớp số notebook in; tích chính xác $\prod_{k=1}^{10^4}(1-0{,}01/k)\approx0{,}907$. Ba lỗi thường gặp: đọc một chuỗi tự chuyển dài thành bằng chứng ô có giá trị $r/(1-\gamma)$; dùng $\gamma$ thay cho $\gamma^m$ cho giá trị tiếp nối của chuyển gộp; và đặt giá trị tiếp nối bằng $0$ khi lượt bị cắt ngắn trong lúc tàu còn ở ô.
:::

### Bài tập 05.27. Lượt dài, phần thưởng cuối và nhiễu hành động trên Lunar Lander

**Mức độ:** vận dụng. Mục tiêu học tập 1, 5 và 6 của ghi chú bài giảng; mạch 4.

**Nguồn:** Bài tập tuần 5 (2025–2026), bài 4, tiền đề tuyệt đối được thay bằng phát biểu có điều kiện; notebook thực hành Bài 05, phần 2, 3, 5, mục 8.1 và 9.2 (một lần chạy đã nhúng, gymnasium 1.3.0); ghi chú bài giảng, Mệnh đề 05.25, Định lý 05.28, Nhận xét 05.29, Ví dụ 05.11, 05.12, Tình huống 05.1; Sutton và Barto (2018), §6.2, trang 124–125.

::: exercise Bài tập 05.27 (Lượt dài, phần thưởng cuối và nhiễu hành động trên Lunar Lander)
Bài tập tuần 5 (2025–2026), bài 4, phát biểu: trong các môi trường có quỹ đạo (trajectory) dài, phần thưởng thưa và nhiễu hành động, TD thường học nhanh hơn Monte Carlo dù mục tiêu TD chệch. Cần kiểm tra nhận định trên dữ liệu của bài thực hành Lunar Lander. Dữ kiện của notebook:

- `LunarLander-v3`, bốn hành động rời rạc, không gió; chính sách cần đánh giá là bộ điều khiển heuristic của Gymnasium, thay bằng một hành động ngẫu nhiên đều với xác suất $\varepsilon=0{,}1$; $\gamma=0{,}99$; mỗi bước dài $0{,}02$ giây.
- Ở mỗi bước không kết thúc, phần thưởng là số hạng định hình, bằng độ tăng của một hàm thế theo vị trí, vận tốc, góc và số chân chạm đất, trừ chi phí nhiên liệu; chuyển cuối có phần thưởng $-100$ khi tàu rơi hoặc ra khỏi khung và $+100$ khi tàu nằm yên. Lượt bị cắt ngắn ở bước $1000$.
- Tập huấn luyện: $2000$ lượt, $546\,869$ chuyển, $42$ lượt bị cắt ngắn. Quan sát được gộp thành $9216$ ô; $70\%$ số chuyển không vào trạng thái kết thúc là tự chuyển. Monte Carlo mọi lần ghé thực hiện $504\,869$ cập nhật, TD(0) thực hiện $546\,869$.
- Một lượt có chuyển vào trạng thái kết thúc tại $t=254$, tàu nằm yên, nên $T=255$.
- $J$ trên $493$ lượt kiểm tra kết thúc thật, trung bình qua năm thứ tự lượt, theo số lượt huấn luyện đã xử lý. Trong năm lịch bước học TD(0) đã chạy ($\alpha=0{,}05$; $0{,}2$; $0{,}5$; $1/n$; $n^{-0{,}6}$), $\alpha=0{,}5$ cho $J$ nhỏ nhất ở mọi điểm đo.

| Bảng | $10$ | $33$ | $115$ | $391$ | $1330$ | $2000$ |
| --- | --- | --- | --- | --- | --- | --- |
| Monte Carlo mọi lần ghé, $1/N(s)$ | $3661$ | $2625$ | $2083$ | $1760$ | $1646$ | $1627$ |
| Monte Carlo mọi lần ghé, $\alpha=0{,}02$ | $4253$ | $3316$ | $2510$ | $2011$ | $1829$ | $1802$ |
| TD(0), $\alpha=0{,}5$ | $5208$ | $4635$ | $3784$ | $2912$ | $2175$ | $2085$ |

Bảng hằng bằng trung bình lợi tức cho $J\approx3021$; bảng $\mathbf 0$ cho $J\approx5797$. Trên toàn tập huấn luyện (nghiệm theo lô không phụ thuộc thứ tự lượt), TD theo lô cho $J\approx1803{,}4$ khi chỉ dùng các lượt kết thúc thật và $J\approx1835{,}8$ khi thêm các chuyển của lượt bị cắt ngắn.

- (a) Tính hệ số của phần thưởng $+100$ trong $G_0$ của lượt có $T=255$ và đóng góp của nó vào $G_0$. Nêu thành phần nào của phần thưởng Lunar Lander là thưa.
- (b) Nêu các kết quả của ghi chú ủng hộ nhận định và các kết quả chống lại nó, mỗi kết quả kèm giả thiết.
- (c) Dựa vào bảng $J$, xác định nhận định có đúng trên dữ liệu này không, và nêu các nguyên nhân có căn cứ.
- (d) Tính số chuyển TD(0) dùng thêm so với Monte Carlo. Xác định việc dùng thêm các chuyển này có bảo đảm $J$ nhỏ hơn hay không.
- (e) Phát biểu lại nhận định thành một khuyến nghị có điều kiện.
:::

::: hint Gợi ý Bài tập 05.27
Phần thưởng $R_T$ mang hệ số $\gamma^{T-1}$ trong $G_0$. Ở (b), phân biệt mục tiêu lý tưởng $Y^*$ với mục tiêu TD dùng bảng đang học, và nhớ giả thiết Markov của Định lý 05.28. Ở (c), so các hàng ở mọi điểm đo, không chỉ ở điểm cuối.
:::

::: solution Lời giải Bài tập 05.27
**Câu (a).** Phần thưởng $+100$ là $R_{255}$, nhận ở chuyển thứ $255$ tính từ $S_0$, nên mang hệ số $\gamma^{254}=0{,}99^{254}\approx0{,}0779$ và đóng góp khoảng $7{,}79$ vào $G_0$. Hệ số $\gamma^k$ còn khoảng $0{,}37$ sau $1/(1-\gamma)=100$ bước. Chỉ thành phần $\pm100$ là thưa: nó xuất hiện một lần ở chuyển cuối. Phần thưởng định hình trừ chi phí nhiên liệu khác $0$ ở hầu hết các bước không kết thúc, nên tiền đề "phần thưởng thưa" chỉ đúng một phần cho Lunar Lander.

**Câu (b).** Ủng hộ nhận định:

- Định lý 05.28: mục tiêu một bước lý tưởng $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$ có phương sai không lớn hơn $G_t$, và phần chênh là phương sai của phần đuôi sau chuyển đầu. Lượt dài và hành động ngẫu nhiên với xác suất $0{,}1$ làm phần đuôi dài và nhiễu hơn; ở dãy bảy ô, phần đuôi chiếm $84\%$ phương sai của $G_t$ (Ví dụ 05.18). Giả thiết: mục tiêu dùng $v_\pi$, trạng thái Markov.
- Sutton và Barto (2018, §6.2, trang 124–125) ghi rằng trên các bài toán ngẫu nhiên, thực nghiệm thường cho TD(0) hội tụ nhanh hơn Monte Carlo bước hằng, và chưa có chứng minh toán học cho điều này.

Chống lại nhận định:

- Mệnh đề 05.25: mục tiêu TD dùng bảng đang học có độ chệch $\gamma\,\mathbb E_\pi[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s]$. Với bảng $\mathbf 0$, độ chệch tại $s$ là $-\gamma\,\mathbb E_\pi[v_\pi(S_{t+1})\mid S_t=s]$, âm khi các trạng thái kế tiếp có giá trị dương. Nhận xét 05.29: với bảng khác $v_\pi$, phương sai của mục tiêu TD không có thứ tự chung với $G_t$.
- Với phần thưởng $\pm100$ chỉ ở chuyển cuối, TD(0) đưa nó về các trạng thái trước từng chuyển một (Ví dụ 05.9); trên chuỗi tự chuyển, mỗi cập nhật chỉ dịch giá trị một phần nhỏ khi $\gamma$ gần $1$ (Ví dụ 05.12).
- Ô gộp không Markov, nên Định lý 05.28 không áp dụng nguyên văn (Tình huống 05.1).

**Câu (c).** Ở cả sáu điểm đo, $J$ của Monte Carlo nhỏ hơn của TD(0) với $\alpha=0{,}5$, cấu hình TD(0) tốt nhất đã chạy: $3661$ so với $5208$ sau $10$ lượt, $1627$ so với $2085$ sau $2000$ lượt. Monte Carlo bước hằng $\alpha=0{,}02$, loại so sánh trong quan sát của Sutton và Barto, cũng nhỏ hơn ở mọi điểm đo: $4253$ so với $5208$, $1802$ so với $2085$. Với các cấu hình đã chạy, nhận định không đúng trên dữ liệu này; kết luận không mở rộng sang bước học hay cách chia ô khác. Các nguyên nhân có căn cứ trong notebook và ghi chú: $70\%$ chuyển là tự chuyển, nên thông tin cuối lượt lan chậm; bảng TD khởi tạo bằng $\mathbf 0$, nên mục tiêu chệch xuống ở các lượt đầu, và $J=5208$ sau $10$ lượt còn gần $5797$ của bảng $\mathbf 0$; ô gộp không Markov; thước đo $J$ nhỏ nhất tại lợi tức kỳ vọng theo ô, đích của Monte Carlo mọi lần ghé, nên nghiêng về Monte Carlo (Tình huống 05.1).

**Câu (d).** TD(0) dùng $546\,869-504\,869=42\,000$ chuyển mà Monte Carlo bỏ, đúng $42$ lượt bị cắt ngắn nhân $1000$ bước. Việc dùng thêm không bảo đảm $J$ nhỏ hơn: trên cùng dữ liệu, TD theo lô cho $1835{,}8$ khi thêm các chuyển này, so với $1803{,}4$ khi chỉ dùng lượt kết thúc thật. Một lần chạy không đủ để kết luận chiều ngược lại; nó chỉ cho thấy thêm dữ liệu không tự động giảm $J$.

**Câu (e).** Một khuyến nghị có điều kiện: khi trạng thái là Markov, lượt dài và nhiễu làm phương sai của $G_t$ lớn, và cần cập nhật sau mỗi chuyển hoặc có nhiều lượt bị cắt ngắn, TD(0) là lựa chọn có căn cứ. Nó dùng được mọi chuyển, cập nhật sau mỗi chuyển, và hội tụ về $v_\pi$ với lịch Robbins–Monro (Định lý 05.30); định lý không cho tốc độ. Về tốc độ, Sutton và Barto (2018, §6.2) ghi rằng trên các bài toán ngẫu nhiên, TD(0) bước hằng thường hội tụ nhanh hơn Monte Carlo bước hằng; quan sát này chưa có chứng minh. Khi trạng thái là ô gộp không Markov, tự chuyển chiếm phần lớn dữ liệu và phần lớn lượt kết thúc trong giới hạn ($1958$ trong $2000$ lượt), như ở notebook, Monte Carlo mọi lần ghé với bước $1/N(s)$ là lựa chọn có căn cứ hơn: nó hội tụ về lợi tức kỳ vọng theo ô (Tình huống 05.1) và cho $J$ nhỏ hơn ở mọi điểm đo của lần chạy này. Kết luận thứ hai dựa trên $J$ trung bình qua năm thứ tự lượt của một lần chạy.

**Kiểm tra lại.** $0{,}99^{254}=e^{254\ln0{,}99}\approx e^{-2{,}553}\approx0{,}0779$. Ba lỗi thường gặp: dùng hệ số $\gamma^{255}$ cho $R_{255}$; đọc "mục tiêu TD có phương sai thấp hơn" thành định lý cho mọi bảng; và so hai phương pháp chỉ ở một điểm đo hoặc một thứ tự lượt.
:::

### Bài tập 05.28. [Lập trình] Cách chia ô và hai nghiệm theo lô trên Lunar Lander

**Mức độ:** vận dụng, có một câu chứng minh. Mục tiêu học tập 6 của ghi chú bài giảng; mạch 5.

**Nguồn:** notebook thực hành Bài 05, phần 4, mục 9.2 và nhiệm vụ 1, 10 của phần 12 (một lần chạy đã nhúng, gymnasium 1.3.0); ghi chú bài giảng, Mệnh đề 05.33, 05.34, Nhận xét 05.35, Tình huống 05.1.

::: exercise Bài tập 05.28 ([Lập trình] Cách chia ô và hai nghiệm theo lô trên Lunar Lander)
Notebook thực hành gộp quan sát tám chiều của `LunarLander-v3` thành ô bằng các điểm cắt `CUTS` trên từng biến, được $9216$ ô. Hàm `prediction_pipeline(cuts, ...)` rời rạc hóa lại dữ liệu đã thu theo một cách chia mới và trả số ô được ghé, tỉ lệ tự chuyển, $J$ của Monte Carlo theo lô, của TD theo lô và của TD(0) với $\alpha=0{,}5$. Với cách chia gốc, notebook in: $1935$ trong $9216$ ô được ghé, tỉ lệ tự chuyển $0{,}70$, $J\approx1627$ cho Monte Carlo theo lô, $J\approx1836$ cho TD theo lô trên toàn bộ tập huấn luyện, $J\approx2101$ cho TD(0) với $\alpha=0{,}5$ theo thứ tự lượt gốc (trung bình qua năm thứ tự lượt là $2085$, Bài tập 05.26; Monte Carlo theo lô cho $1627$ với mọi thứ tự). Với cách chia thô hơn `CUTS_COARSE`, bỏ điểm cắt $0$ của vận tốc ngang $v_x$, góc nghiêng $\varphi$ và vận tốc góc $\omega$, notebook in: $3888$ ô, $991$ ô được ghé, tỉ lệ tự chuyển $0{,}83$, $J\approx1645$, $1859$ và $2125$ cho ba phương pháp theo cùng thứ tự. $J$ là trung bình của $(G_t-V(S_t))^2$ trên các mẫu của tập kiểm tra; $J_{\mathrm{hl}}$ là cùng đại lượng tính trên các lượt kết thúc thật của tập huấn luyện. Một cách chia $\mathcal B$ gọi là thô hơn cách chia $\mathcal A$ khi mỗi ô của $\mathcal B$ là hợp của một số ô của $\mathcal A$; bỏ một điểm cắt cho một cách chia thô hơn.

- (a) Chứng minh: nếu $\mathcal B$ thô hơn $\mathcal A$ thì $J_{\mathrm{hl}}$ của nghiệm Monte Carlo theo lô với $\mathcal B$ không nhỏ hơn với $\mathcal A$. Giải thích vì sao kết luận không chuyển sang $J$ trên tập kiểm tra.
- (b) Chạy `prediction_pipeline` với một cách chia mịn hơn cách chia gốc (thêm điểm cắt cho $x$, $y$). Lập bảng số ô được ghé, tỉ lệ tự chuyển, $J$ của ba phương pháp và hiệu $J_{\mathrm{TD\,lô}}-J_{\mathrm{MC\,lô}}$ cho ba cách chia; kiểm tra mã bằng kết luận của (a).
- (c) Giải thích kết quả bằng Mệnh đề 05.33, 05.34 và phân rã của $J$; nêu số đo bổ sung cần có trước khi quy hiệu giữa hai nghiệm theo lô cho việc ô không Markov.
:::

::: hint Gợi ý Bài tập 05.28
Ở (a), $J_{\mathrm{hl}}$ chia cho cùng một số mẫu với mọi cách chia, nên chỉ cần so tổng bình phương. Theo Mệnh đề 05.33, nghiệm Monte Carlo theo lô cực tiểu tổng bình phương trên dữ liệu huấn luyện trong lớp các bảng hằng trên từng ô. Xét xem một bảng hằng trên từng ô của $\mathcal B$ có hằng trên từng ô của $\mathcal A$ hay không.
:::

::: solution Lời giải Bài tập 05.28
**Câu (a).** Gọi $\mathcal F_{\mathcal A}$ là tập các hàm trên không gian quan sát, hằng trên từng ô của $\mathcal A$, và $L(f)=\sum_i(G_i-f(o_i))^2$ là tổng bình phương trên các mẫu huấn luyện, với $o_i$ là quan sát của mẫu thứ $i$.

- *Bước 1.* $L$ tách thành tổng theo ô, và theo Mệnh đề 05.33 mỗi số hạng cực tiểu tại trung bình các lợi tức của ô đó; do đó nghiệm Monte Carlo theo lô $f_{\mathcal A}$ cực tiểu $L$ trên $\mathcal F_{\mathcal A}$.
- *Bước 2.* Mỗi ô của $\mathcal B$ là hợp của các ô của $\mathcal A$, nên một hàm hằng trên từng ô của $\mathcal B$ cũng hằng trên từng ô của $\mathcal A$: $\mathcal F_{\mathcal B}\subseteq\mathcal F_{\mathcal A}$.
- *Bước 3.* Do đó $L(f_{\mathcal A})=\min_{\mathcal F_{\mathcal A}}L\le\min_{\mathcal F_{\mathcal B}}L=L(f_{\mathcal B})$. Chia hai vế cho cùng số mẫu được $J_{\mathrm{hl}}(f_{\mathcal A})\le J_{\mathrm{hl}}(f_{\mathcal B})$. $\square$

Trên tập kiểm tra, lập luận không còn đúng vì $f_{\mathcal A}$ được chọn theo dữ liệu huấn luyện. Ô mịn hơn có ít mẫu hơn, nên trung bình theo ô dao động nhiều hơn quanh lợi tức kỳ vọng của ô, và có thêm ô của tập kiểm tra chưa từng được ghé (với cách chia gốc, notebook in tỉ lệ $0{,}0007$ mẫu kiểm tra rơi vào ô chưa có). Ô thô hơn thì gộp các quan sát có lợi tức kỳ vọng khác nhau. $J$ trên tập kiểm tra có thể tăng hoặc giảm theo cả hai hướng.

**Câu (b).** Bảng kết quả có dạng sau. Hai hàng đầu là số in trong notebook và phải được tái tạo trước khi chạy cách chia mới; hàng cuối điền số của lần chạy của người học:

| Cách chia | Số ô được ghé | Tỉ lệ tự chuyển | $J$ MC theo lô | $J$ TD theo lô | $J$ TD(0), $\alpha=0{,}5$ | Hiệu TD lô − MC lô |
| --- | --- | --- | --- | --- | --- | --- |
| Gốc, $9216$ ô | $1935$ | $0{,}70$ | $1627$ | $1836$ | $2101$ | $209$ |
| Thô hơn, $3888$ ô | $991$ | $0{,}83$ | $1645$ | $1859$ | $2125$ | $214$ |
| Mịn hơn | | | | | | |

Kiểm tra mã: tính thêm $J_{\mathrm{hl}}$ của Monte Carlo theo lô cho ba cách chia. Vì cách chia thô và cách chia gốc lồng nhau, cũng như cách chia gốc và cách chia mịn, (a) đòi hỏi $J_{\mathrm{hl}}$ không giảm khi đi từ cách chia mịn tới cách chia thô; một vi phạm cho thấy lỗi trong phép rời rạc hóa hoặc trong việc chỉ dùng các lượt kết thúc thật. Cách chia theo phân vị của nhiệm vụ 1 không lồng với cách chia gốc, nên (a) không áp dụng cho nó.

**Câu (c).** Theo Mệnh đề 05.33, Monte Carlo theo lô cho trung bình lợi tức theo ô, nên $J$ của nó chỉ chịu sai số ước lượng trung bình theo ô và phần dao động của lợi tức quanh lợi tức kỳ vọng theo ô. Theo Mệnh đề 05.34, TD theo lô là giá trị đúng của quá trình phần thưởng Markov thực nghiệm trên ô. Nếu dữ liệu trên ô là Markov, hai nghiệm cùng ước lượng một đại lượng và hiệu giữa chúng chỉ do số mẫu hữu hạn; nếu không, quá trình thực nghiệm trộn các lượt đi vào ô theo những hướng khác nhau, như hai cách đọc tám lượt $\mathrm A$, $\mathrm B$ (Nhận xét 05.35). Hiệu $209$ của cách chia gốc và $214$ của cách chia thô vì vậy phù hợp với ô không Markov nhưng không chứng minh điều đó. Với cách chia thô, tỉ lệ tự chuyển tăng từ $0{,}70$ lên $0{,}83$ vì ô lớn hơn, và $J$ của TD(0) trực tuyến tăng từ $2101$ lên $2125$, phù hợp cơ chế lan chậm qua tự chuyển của Bài tập 05.26; $J$ của Monte Carlo theo lô cũng tăng, từ $1627$ lên $1645$, phù hợp với việc mỗi ô thô gộp nhiều quan sát hơn, với lợi tức kỳ vọng có thể khác nhau. Một lần chạy với hai cách chia không đủ để tách hai cơ chế. Trước khi quy hiệu cho việc ô không Markov, cần đo trực tiếp như nhiệm vụ 10 của notebook: khoảng cách biến phân toàn phần giữa $\hat P(S_{t+1}\mid S_t)$ và $\hat P(S_{t+1}\mid S_t,S_{t-1})$ trên các ô có đủ mẫu, rồi đối chiếu các ô có khoảng cách lớn với các ô có $\lvert V_{\mathrm{MC}}-V_{\mathrm{TD}}\rvert$ lớn. Mọi kết luận chỉ áp dụng cho dữ liệu, cách chia và phiên bản gói đã dùng.

**Kiểm tra lại.** Hai hàng đầu của bảng: $1836-1627=209$ và $1859-1645=214$. Ba lỗi thường gặp: dùng (a) để kết luận cách chia mịn luôn cho $J$ kiểm tra nhỏ hơn; so $J$ của các cách chia đo trên những tập mẫu kiểm tra khác nhau; và coi hiệu giữa hai nghiệm theo lô là sai số của TD theo lô. Hai nghiệm khớp hai tiêu chuẩn khác nhau.
:::

## Tài liệu tham khảo

- Bài tập tuần 5 (2025–2026), *Dự đoán phi mô hình*: bài 1 và bài 3 cho Bài tập 05.17; bài 3 cho Bài tập 05.20; bài 4 cho Bài tập 05.24, 05.27; bài 5 cho Bài tập 05.16, 05.18, 05.22; bài 6 cho Bài tập 05.23; bài 7 cho Bài tập 05.18, 05.20, 05.21, 05.22. Tiền đề tuyệt đối của bài 4 và bài 5 được thay bằng phát biểu có điều kiện; bài 7 được đổi hệ số chiết khấu ở Bài tập 05.18, 05.21.
- Bài giảng gốc (2025–2026), *Dự đoán phi mô hình*, trang 20–22 (lần ghé, trung bình gia tăng, bước học hằng): Bài tập 05.16, 05.18.
- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §2.5, trang 33 (Bài tập 05.11); §5.1, trang 92–93 (Bài tập 05.19); §6.1, trang 119–121 (Bài tập 05.20); §6.2, trang 124–125 (Bài tập 05.27); §6.3, trang 126–128 và Ví dụ 6.4 (Bài tập 05.12, 05.25).
- Notebook thực hành Bài 05, *Dự đoán Monte Carlo và TD(0) trên Lunar Lander*, gymnasium 1.3.0, một lần chạy đã nhúng: Bài tập 05.26, 05.27, 05.28.
- Ghi chú bài giảng Bài 05: Bài tập 05.8, 05.11, 05.12 (đề, gợi ý, lời giải); phát biểu và chứng minh của các kết quả được dùng; Bài tập 05.19, 05.24, 05.25 dùng số liệu sư phạm tự xây dựng.
