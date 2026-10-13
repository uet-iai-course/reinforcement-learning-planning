# Bài tập Bài 06 — Điều khiển phi mô hình

Bộ bài tập gồm mười một bài theo sáu mạch nội dung của bài học, ở ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Bài tập 06.1–06.6 giữ số hiệu và kết quả của [ghi chú bài giảng Bài 06](material-viewer.html?doc=materials/lec-06/lecture-note.md&deck=lecture-06-dieu-khien-phi-mo-hinh.html); đề được phát biểu lại cho tự chứa, lời giải được bổ sung các lỗi thường gặp, và mỗi bài trùng một bài tập có lời giải trên trang chiếu. Bài tập 06.7–06.12 nằm ở mục "Bài tập củng cố" của ghi chú và không chép lại ở đây. Bài tập 06.13–06.17 chỉ có trong tệp này: 06.13 lấy từ bộ bài tập tuần 3 của học kỳ trước, 06.14 là bài chứng minh về lớp chính sách $\varepsilon$-mềm ($\varepsilon$-soft), 06.15 và 06.16 là bài lập trình trên notebook thực hành LunarLander của Bài 06, còn 06.17 trùng bài tập tổng hợp ở mạch kết luận của trang chiếu. Khi một bài trùng bài tập trên trang chiếu, dòng "Trùng trang chiếu" dẫn tới trang câu hỏi và trang lời giải, và lời giải trong tệp cho cùng kết quả với lời giải trên trang.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/1/1) | — |
| 2. Giá trị hành động và thăm dò | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/2/1) | 06.1, 06.2, 06.14 |
| 3. Điều khiển Monte Carlo | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/3/1) | 06.3, 06.13 |
| 4. Sarsa và mục tiêu một bước | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/4/1) | 06.4, 06.15 |
| 5. Q-learning và học khác chính sách | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/5/1) | 06.5, 06.13 |
| 6. Điều kiện hội tụ | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/6/1) | 06.6, 06.16 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-06-dieu-khien-phi-mo-hinh.html#/7/1) | 06.17 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 06. Tác tử (agent) tương tác với môi trường theo các lượt (episode); $S_t$, $A_t$ là trạng thái và hành động tại bước $t$, và $R_{t+1}$ là phần thưởng (reward) của chuyển từ $S_t$ sang $S_{t+1}$. Lợi tức (return) là $G_t=\sum_{j=t}^{T-1}\gamma^{j-t}R_{j+1}$ với $G_T=0$; giá trị của mọi trạng thái kết thúc bằng $0$, trong hàm thật lẫn trong bảng ước lượng. $q_\pi$ và $q_*$ là giá trị hành động thật của chính sách $\pi$ và giá trị hành động tối ưu; $Q$ là bảng ước lượng do thuật toán giữ, và $Q_t$ là bảng ngay trước cập nhật ở bước $t$. Một mẫu chuyển viết theo thứ tự $(S,A,R,S')$, và với Sarsa thêm hành động kế tiếp đã chọn $A'$. Số thập phân viết với dấu phẩy; khi một bộ số có thành phần thập phân, các thành phần cách nhau bằng dấu chấm phẩy, như $(0{,}45;\,0{,}45;\,0{,}1)$. Kết quả trung gian dạng phân số được giữ chính xác.

**Dãy năm ô** (dùng ở Bài tập 06.1–06.5; dữ kiện được nêu lại trong từng bài). Năm ô xếp thành hàng A–B–C–D–E; A và E là trạng thái kết thúc, $\mathcal S=\{\mathrm B,\mathrm C,\mathrm D\}$. Tại mỗi ô không kết thúc có hai hành động: $0$ đi sang trái, $1$ đi sang phải; chuyển tất định. Vào A nhận phần thưởng $1000$, vào E nhận $10$, vào B, C hoặc D nhận $-1$. Mỗi lượt bắt đầu tại D và $\gamma=1$. Bảng khởi tạo nghiêng phải, ghi theo thứ tự hành động $(0,1)$, là B $(0,1)$, C $(1,0)$, D $(0,1)$; tên gọi đến từ hàng D: tại ô bắt đầu, bảng xếp hành động phải trên hành động trái. Các bộ số này lấy từ bài giảng gốc (2025–2026), trang 15–21.

**Tàu đổ bộ** (dùng ở Bài tập 06.15–06.17). Môi trường `LunarLander-v3` của Gymnasium, hành động rời rạc, không gió, được rời rạc hóa thành $2187$ ô với bốn hành động $\{0,1,2,3\}$; $\gamma=0{,}99$; $Q_0=0$; lượt kết thúc khi tàu rơi hoặc ra khỏi khung (phần thưởng $-100$) hay nằm yên ($+100$), và bị cắt ngắn ở bước $1000$. Chính sách hành vi là chính sách $\varepsilon_k$-tham lam với $\varepsilon_k$ giảm tuyến tính từ $1$ về $0{,}05$ trong $1500$ lượt rồi giữ nguyên; bước học theo cặp là $\alpha_n=\max(0{,}05;\,n^{-0{,}6})$; ngân sách là $3000$ lượt huấn luyện. Số liệu của tàu đổ bộ là của một lần chạy đã nhúng trong notebook `thuc-hanh-lunarlander-dieu-khien-phi-mo-hinh.ipynb`, trừ năm lần huấn luyện sơ bộ dẫn ở Bài tập 06.15: các lần này được ghi nhận khi soạn notebook, chạy ngoài notebook, và được đánh giá trên một tập hạt giống khác `TEST_SEED` (notebook, phần 8.2).

**Nhắc lại các kết quả được dùng.**

- Chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy, Định nghĩa 06.3): với $m(s)$ hành động và tập cực đại $\mathcal G_Q(s)=\operatorname{arg\,max}_aQ(s,a)$, $\pi_\varepsilon(a\mid s)=\varepsilon/m(s)+(1-\varepsilon)\,\mathbf 1\{a\in\mathcal G_Q(s)\}/|\mathcal G_Q(s)|$. Chính sách $\pi$ là $\varepsilon$-mềm (Định nghĩa 06.4) nếu $\pi(a\mid s)\ge\varepsilon/m(s)$ với mọi $s$, $a$.
- Phương trình Bellman của một chính sách $\pi$ (ghi chú Bài 03, Mục 4): $v_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\,[r+\gamma v_\pi(s')]$, với $v_\pi=0$ tại trạng thái kết thúc.
- Mệnh đề 06.6: trong quá trình quyết định Markov (Markov decision process, MDP) hữu hạn có phần thưởng bị chặn và $0\le\gamma<1$, nếu $\pi$ là $\varepsilon$-mềm và $\pi'$ là chính sách $\varepsilon$-tham lam theo $q_\pi$ chính xác với cùng $\varepsilon$, thì $\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$ và $v_{\pi'}\ge v_\pi$.
- Monte Carlo lần ghé đầu tiên (first-visit) theo cặp (Định nghĩa 06.8, Thuật toán 06.9): chỉ lợi tức $G_{f(s,a)}$ sau lần ghé đầu $f(s,a)$ của cặp được dùng; bộ đếm $N(s,a)$ tăng trước khi cập nhật $Q(s,a)\leftarrow Q(s,a)+[G-Q(s,a)]/N(s,a)$.
- Mục tiêu Sarsa (Định nghĩa 06.11) và mục tiêu Q-learning (Định nghĩa 06.15): khi $S_{t+1}$ chưa kết thúc, $Y_t=R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$ và $Y_t=R_{t+1}+\gamma\max_aQ_t(S_{t+1},a)$; khi $S_{t+1}$ kết thúc, cả hai bằng $R_{t+1}$. Cập nhật: $Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t[Y_t-Q_t(S_t,A_t)]$, các ô khác giữ nguyên.
- Kết thúc lượt, cắt ngắn và hết ngân sách là ba sự kiện khác nhau (Nhận xét 06.13); chỉ khi kết thúc lượt mới đặt $Y_t=R_{t+1}$.
- Tham lam trong giới hạn với thăm dò vô hạn (greedy in the limit with infinite exploration, GLIE; Định nghĩa 06.18) đòi mọi cặp được thực hiện vô hạn lần và khối xác suất trên tập cực đại tiến tới $1$; Robbins–Monro theo cặp (Định nghĩa 06.19) đòi $\sum_n\alpha_n(s,a)=\infty$ và $\sum_n\alpha_n(s,a)^2<\infty$ với mọi cặp. Định lý 06.21 (Q-learning) cần các giả thiết nền của Nhận xét 06.20 (MDP hữu hạn có tính Markov, động lực dừng, phần thưởng bị chặn, $0\le\gamma<1$, $Q_0$ hữu hạn, mẫu sinh từ chính MDP), mọi cặp được cập nhật vô hạn lần và Robbins–Monro theo cặp; Định lý 06.22 (Sarsa) cần thêm GLIE.

Lời giải nêu kết quả được dùng ở từng bước. Các bộ số không ghi nguồn là số liệu sư phạm tự xây dựng.

## Mức nhận biết

### Bài tập 06.1. Thông tin trong một mẫu chuyển

- **Mức độ:** nhận biết; mục tiêu học tập 1 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Mục 1.1; bài giảng gốc (2025–2026), trang 3, 15.
- **Trùng trang chiếu:** [Thông tin trong một mẫu chuyển](lecture-06-dieu-khien-phi-mo-hinh.html#/2/2); câu hỏi (b) và lời giải của nó nằm trên cùng trang, lời giải hiện ở bước cuối của trang.

::: exercise Bài tập 06.1 (Thông tin trong một mẫu chuyển)
Trên dãy năm ô A–B–C–D–E ($\mathcal S=\{\mathrm B,\mathrm C,\mathrm D\}$, hành động $0$ trái và $1$ phải, A và E kết thúc; vào A nhận $1000$, vào E nhận $10$, vào B, C, D nhận $-1$; $\gamma=1$), tác tử ghi được mẫu $(\mathrm D,1,10,\mathrm E)$ theo thứ tự trạng thái, hành động, phần thưởng, trạng thái kế tiếp. Khi biết mô hình, lượt D→C→B→A có lợi tức $-1-1+1000=998$; tác tử không biết số này.

- (a) Xác định trạng thái, hành động, phần thưởng, trạng thái kế tiếp, và số hành động còn thực hiện trong lượt sau mẫu này.
- (b) Xác định mẫu này cung cấp dữ liệu gì về cặp $(\mathrm D,0)$.
- (c) Giải thích vì sao muốn so sánh hai hành động tại D, tác tử phải giữ hai ô riêng $Q(\mathrm D,0)$ và $Q(\mathrm D,1)$.
:::

::: hint Gợi ý Bài tập 06.1
Đọc bộ bốn theo thứ tự đã cho. Phân biệt hành động đã được thực hiện với hành động chưa xuất hiện trong dữ liệu, và dùng quy ước kết thúc tại A, E.
:::

::: solution Lời giải Bài tập 06.1
**Câu (a).** Trạng thái là D, hành động là $1$ (phải), phần thưởng là $10$, trạng thái kế tiếp là E. Vì E là trạng thái kết thúc, không còn hành động nào trong lượt.

**Câu (b).** Mẫu không chứa lần thực hiện hành động $0$ tại D, nên không cho dữ liệu nào về cặp $(\mathrm D,0)$. Con số $998$ của lượt "đi trái ba lần" tính từ mô hình của dãy năm ô, không từ mẫu.

**Câu (c).** Mẫu $(\mathrm D,1,10,\mathrm E)$ chỉ là một quan sát của cặp $(\mathrm D,1)$. Nếu chỉ giữ một ô $V(\mathrm D)$, quan sát này trộn với các quan sát sau hành động trái. Hai ô riêng cho phép so sánh $Q(\mathrm D,0)$ với $Q(\mathrm D,1)$ mà không cần mô hình.

**Kiểm tra lại.** Mẫu có đúng một hành động là $1$, nên chỉ ô $(\mathrm D,1)$ có thể được cập nhật từ nó. Hai lỗi thường gặp: dùng $998$ như một dữ liệu về $(\mathrm D,0)$, trong khi số này chỉ tính được khi biết mô hình; và coi $10$ là giá trị của trạng thái D, khi đó hai hành động bị trộn vào một ô.
:::

### Bài tập 06.6. Kiểm giả thiết hội tụ

- **Mức độ:** nhận biết; mục tiêu học tập 5 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Mục 5.4; bài giảng gốc (2025–2026), trang 25–28.
- **Trùng trang chiếu:** [Bài tập: kiểm giả thiết hội tụ](lecture-06-dieu-khien-phi-mo-hinh.html#/6/11) và [trang lời giải](lecture-06-dieu-khien-phi-mo-hinh.html#/6/12).

::: exercise Bài tập 06.6 (Kiểm giả thiết hội tụ)
Giả sử MDP hữu hạn với động lực dừng, phần thưởng bị chặn, $\gamma=0{,}9$, $Q_0$ hữu hạn, mẫu sinh từ chính MDP, mọi cặp được cập nhật vô hạn lần, và mọi trạng thái có hai hành động. Với mỗi trường hợp (a), (b), (c) dưới đây, xác định Định lý 06.21 hoặc 06.22 có áp dụng không; nếu không, nêu giả thiết còn thiếu.

| Trường hợp | Thuật toán và hành vi | Bước học theo cặp |
|---|---|---|
| (a) | Q-learning, $\varepsilon$-tham lam với $\varepsilon=0{,}25$ cố định | $\alpha_n=1/n$ |
| (b) | Sarsa, $\varepsilon$-tham lam với $\varepsilon=0{,}25$ cố định | $\alpha_n=1/n$ |
| (c) | Sarsa, dãy chính sách GLIE | $\alpha_n=0{,}8$ |

Ở trường hợp (b), có ít nhất một trạng thái mà hàng của bảng có cực đại duy nhất tại mọi bước từ một thời điểm nào đó.
:::

::: hint Gợi ý Bài tập 06.6
Kiểm riêng điều kiện bước học (Định nghĩa 06.19) và điều kiện về hành vi của từng định lý. Trong trường hợp (b), tính khối xác suất trên hành động cực đại; trong trường hợp (c), tính tổng bình phương bước học.
:::

::: solution Lời giải Bài tập 06.6
**Câu (a).** Áp dụng được Định lý 06.21. Lịch $1/n$ thỏa hai tổng (ghi chú Bài 05, Mục 4); Q-learning chỉ cần độ phủ, đã có theo giả thiết, và không cần hành vi trở nên tham lam.

**Câu (b).** Không áp dụng được Định lý 06.22: thiếu điều kiện tham lam trong giới hạn. Tại trạng thái có cực đại duy nhất, khối xác suất trên cực đại là $1-0{,}25+0{,}25/2=0{,}875=7/8$, không tiến tới $1$.

**Câu (c).** Không áp dụng được Định lý 06.22: $\sum_n0{,}8^2=\infty$ vi phạm tổng thứ hai của Định nghĩa 06.19.

**Kiểm tra lại.** Trong (b) và (c), định lý không áp dụng; điều này không chứng minh thuật toán phân kỳ, chỉ nói rằng kết luận $Q_t\to q_*$ không có căn cứ từ định lý. Hai lỗi thường gặp: coi một bước học dương bất kỳ, hoặc một $\varepsilon$ dương cố định, là đủ, trong khi bước hằng $0{,}8$ vi phạm tổng thứ hai và $\varepsilon$ cố định giữ khối cực đại ở $7/8$; và đòi GLIE cho Q-learning ở trường hợp (a), trong khi Định lý 06.21 chỉ cần độ phủ.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 06.2. Chính sách $\varepsilon$-tham lam và điều kiện của Mệnh đề 06.6

- **Mức độ:** tính toán; mục tiêu học tập 1 và 2 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Mục 1.2–1.3; bài giảng gốc (2025–2026), trang 6–8, 24.
- **Trùng trang chiếu:** [Bài tập: chính sách $\varepsilon$-tham lam trên dãy năm ô](lecture-06-dieu-khien-phi-mo-hinh.html#/2/12) và [trang lời giải](lecture-06-dieu-khien-phi-mo-hinh.html#/2/13).

::: exercise Bài tập 06.2 (Chính sách $\varepsilon$-tham lam và điều kiện của Mệnh đề 06.6)
Các câu (a), (c), (d) xét dãy năm ô ($\gamma=1$, hai hành động $0$ trái và $1$ phải tại mỗi ô không kết thúc; hành động $1$ tại D đi vào E, kết thúc lượt với phần thưởng $10$); câu (b) xét một trạng thái ngoài dãy năm ô.

- (a) Cho hàng D của bảng là $Q(\mathrm D,0)=0$, $Q(\mathrm D,1)=1$ và $\varepsilon=0{,}2$. Tính xác suất của mỗi hành động tại D theo Định nghĩa 06.3.
- (b) Tại một trạng thái có ba hành động với hàng $Q(s,\cdot)=(4;\,1;\,1)$ và $\varepsilon=0{,}6$, tính phân phối $\varepsilon$-tham lam.
- (c) Trong $q_\pi(\mathrm D,0)$, nêu hành động nào được cố định và hành động nào lấy theo $\pi$.
- (d) Bảng khởi tạo nghiêng phải là B $(0,1)$, C $(1,0)$, D $(0,1)$ theo thứ tự hành động $(0,1)$. Xác định bảng này đã đủ căn cứ để áp dụng Mệnh đề 06.6 cho dãy năm ô hay chưa.
:::

::: hint Gợi ý Bài tập 06.2
Tách nhánh thăm dò và nhánh khai thác; ở câu (b), phần khai thác chia đều cho các hành động đồng hạng. Với câu (d), đối chiếu từng giả thiết của Mệnh đề 06.6: bảng dùng để tạo $\pi'$ là gì, và hệ số chiết khấu của dãy năm ô là bao nhiêu.
:::

::: solution Lời giải Bài tập 06.2
**Câu (a).** Hành động $1$ là cực đại duy nhất. Hành động $0$ có xác suất $0{,}2/2=0{,}1$; hành động $1$ có $0{,}8+0{,}1=0{,}9$.

**Câu (b).** $\mathcal G_Q(s)=\{0\}$. Mỗi hành động nhận $0{,}6/3=0{,}2$ từ phần chọn đều; hành động cực đại nhận thêm $0{,}4$. Phân phối là $(0{,}6;\,0{,}2;\,0{,}2)$.

**Câu (c).** $q_\pi(\mathrm D,0)$ cố định hành động đầu $A_t=0$; mọi hành động từ bước $t+1$ trở đi lấy theo $\pi$.

**Câu (d).** Chưa đủ, vì hai lý do. Thứ nhất, Mệnh đề 06.6 đòi hỏi $\pi'$ được tạo từ $q_\pi$ chính xác, còn bảng khởi tạo chưa là giá trị hành động của chính sách nào: $Q_0(\mathrm D,1)=1$ trong khi $q_\pi(\mathrm D,1)=10$ với mọi $\pi$, vì hành động $1$ tại D luôn kết thúc lượt với phần thưởng $10$. Thứ hai, mệnh đề dùng $\gamma<1$, còn dãy năm ô dùng $\gamma=1$.

**Kiểm tra lại.** Ở câu (a) và câu (b), tổng xác suất đều bằng $1$: $0{,}1+0{,}9=1$ và $0{,}6+0{,}2+0{,}2=1$. Hai lỗi thường gặp: gán xác suất $\varepsilon=0{,}2$ cho hành động không cực đại, quên rằng nhánh thăm dò chọn đều trong cả hai hành động, kể cả hành động cực đại; và coi bảng khởi tạo như $q_\pi$ rồi áp dụng mệnh đề cải thiện.
:::

### Bài tập 06.3. Lần ghé đầu tiên trên lượt có cặp lặp

- **Mức độ:** tính toán; mục tiêu học tập 3 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Mục 2.1–2.3; bài giảng gốc (2025–2026), trang 9–11.
- **Trùng trang chiếu:** [Bài tập: lần ghé đầu tiên trên lượt có cặp lặp](lecture-06-dieu-khien-phi-mo-hinh.html#/3/10) và [trang lời giải](lecture-06-dieu-khien-phi-mo-hinh.html#/3/11).

::: exercise Bài tập 06.3 (Lần ghé đầu tiên trên lượt có cặp lặp)
Trên dãy năm ô ($\gamma=1$; hành động $0$ trái, $1$ phải; A và E kết thúc), cho lượt D→C→D→C→B→A với dãy hành động $0,1,0,0,0$ và dãy phần thưởng $-1,-1,-1,-1,1000$. Bộ đếm ban đầu $N(\mathrm D,0)=0$.

- (a) Tính các lợi tức $G_0,\dots,G_4$.
- (b) Tính $Q(\mathrm D,0)$ và $N(\mathrm D,0)$ sau Monte Carlo lần ghé đầu tiên theo cặp (Định nghĩa 06.8).
- (c) Tính lại nếu dùng mọi lần ghé (every-visit): nhắc lại rằng Monte Carlo mọi lần ghé (ghi chú Bài 05, Mục 2) gắn với cặp lợi tức sau mỗi lần ghé, không chỉ lần đầu.
- (d) Xác định các cặp tại ô C và số lợi tức mỗi cặp nhận.
:::

::: hint Gợi ý Bài tập 06.3
Đánh số thời điểm từ $0$ và tính lợi tức lùi. Lần ghé đầu tiên xác định theo chiều thời gian, dù lợi tức được tính theo chiều ngược.
:::

::: solution Lời giải Bài tập 06.3
**Câu (a).** Tính lùi: $G_4=1000$, $G_3=-1+1000=999$, $G_2=998$, $G_1=997$, $G_0=996$.

**Câu (b).** Cặp $(\mathrm D,0)$ xuất hiện tại $t=0$ và $t=2$. Lần ghé đầu tiên là $t=0$, nên chỉ lợi tức $G_0=996$ được dùng: $N(\mathrm D,0)=1$ và $Q(\mathrm D,0)=996$.

**Câu (c).** Mọi lần ghé dùng cả $G_0=996$ và $G_2=998$: $N(\mathrm D,0)=2$ và $Q(\mathrm D,0)=(996+998)/2=997$.

**Câu (d).** Tại C có hai lần ghé với hai hành động khác nhau: $(\mathrm C,1)$ tại $t=1$ với lợi tức $997$, và $(\mathrm C,0)$ tại $t=3$ với lợi tức $999$. Đây là hai cặp riêng, mỗi cặp nhận một lợi tức.

**Kiểm tra lại.** Giá trị khởi tạo không được tính thành mẫu ở cả hai cách, vì bộ đếm bắt đầu từ $0$. Hai cách chỉ khác nhau ở cặp lặp $(\mathrm D,0)$. Hai lỗi thường gặp: đếm theo trạng thái thay cho theo cặp, coi hai lần ghé ô C là của cùng một đơn vị; và chia cho $N+1$, như thể giá trị khởi tạo là một quan sát.
:::

### Bài tập 06.4. Cập nhật Sarsa với bước học khác

- **Mức độ:** tính toán; mục tiêu học tập 4 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Mục 3.1–3.2; bài giảng gốc (2025–2026), trang 13–14, 18.
- **Trùng trang chiếu:** [Bài tập: cập nhật Sarsa với bước học khác](lecture-06-dieu-khien-phi-mo-hinh.html#/4/10) và [trang lời giải](lecture-06-dieu-khien-phi-mo-hinh.html#/4/11).

::: exercise Bài tập 06.4 (Cập nhật Sarsa với bước học khác)
Trên dãy năm ô ($\gamma=1$; hành động $0$ trái, $1$ phải; A và E kết thúc), bảng hiện tại có $Q(\mathrm D,0)=0$ và $Q(\mathrm C,0)=-0{,}6$; bảng khởi tạo nghiêng phải có $Q_0(\mathrm C,0)=1$, và $-0{,}6$ là giá trị sau một cập nhật Sarsa. Tác tử quan sát chuyển $(\mathrm D,0,-1,\mathrm C)$ và chọn $A'=0$ tại C; bước học là $\alpha=0{,}5$.

- (a) Tính $Y$, $\delta$ và giá trị mới của $Q(\mathrm D,0)$, mỗi đại lượng trên một dòng.
- (b) Xác định thời điểm chọn $A'$ và hành động phải thực hiện nếu tiếp tục tương tác.
- (c) Tính lại câu (a) trong trường hợp giả định C là trạng thái kết thúc.
- (d) Nếu ngân sách hết ngay sau cập nhật ở câu (a), xác định mục tiêu có thay đổi không.
:::

::: hint Gợi ý Bài tập 06.4
Dùng giá trị hiện tại của ô $(\mathrm C,0)$, không dùng bảng khởi tạo. Phân biệt trạng thái kết thúc với điểm dừng thu thập dữ liệu (Nhận xét 06.13).
:::

::: solution Lời giải Bài tập 06.4
**Câu (a).**

$$
\begin{aligned}
Y&=-1+1\cdot(-0{,}6)=-1{,}6,\\
\delta&=-1{,}6-0=-1{,}6,\\
Q(\mathrm D,0)&\leftarrow0+0{,}5\cdot(-1{,}6)=-0{,}8 .
\end{aligned}
$$

**Câu (b).** $A'=0$ được chọn ở bước 2 của Thuật toán 06.12, trước khi cập nhật, từ bảng chưa cập nhật. Nếu tương tác tiếp tục, hành động thực hiện tại C phải là đúng $A'=0$.

**Câu (c).** Nếu C kết thúc thì không chọn $A'$: $Y=-1$, $\delta=-1$, $Q(\mathrm D,0)\leftarrow0+0{,}5\cdot(-1)=-0{,}5$.

**Câu (d).** Mục tiêu không đổi: C vẫn là trạng thái không kết thúc, nên $Y$ vẫn chứa $Q(\mathrm C,0)$; hết ngân sách chỉ có nghĩa $A'$ không được thực hiện.

**Kiểm tra lại.** Với $\alpha=0{,}8$ thay cho $0{,}5$, câu (a) cho $0+0{,}8\cdot(-1{,}6)=-1{,}28$, trùng cập nhật của mẫu 5 trong Ví dụ 06.10 của ghi chú. Ba lỗi thường gặp: dùng $Q(\mathrm C,0)=1$ của bảng khởi tạo thay cho giá trị hiện tại $-0{,}6$, cho $Y=0$ và $Q(\mathrm D,0)$ không đổi; đặt $Y=R$ khi hết ngân sách, coi C như trạng thái kết thúc, và nhận $-0{,}5$ ở câu (d); và chọn lại hành động tại C sau cập nhật, khi đó hành động được thực hiện có thể khác $A'$ đã dùng trong mục tiêu.
:::

### Bài tập 06.5. Mục tiêu Sarsa và Q-learning trên cùng chuyển

- **Mức độ:** tính toán; mục tiêu học tập 4 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Mục 4.2–4.3; bài giảng gốc (2025–2026), trang 19–21.
- **Trùng trang chiếu:** [Bài tập: mục tiêu Sarsa và Q-learning trên cùng chuyển](lecture-06-dieu-khien-phi-mo-hinh.html#/5/11) và [trang lời giải](lecture-06-dieu-khien-phi-mo-hinh.html#/5/12).

::: exercise Bài tập 06.5 (Mục tiêu Sarsa và Q-learning trên cùng chuyển)
Trên dãy năm ô ($\gamma=1$; hành động $0$ trái, $1$ phải; A và E kết thúc), bảng hiện tại có $Q(\mathrm B,0)=800$, $Q(\mathrm B,1)=1$. Chuyển quan sát được là $(\mathrm C,0,-1,\mathrm B)$, và Sarsa đã chọn hành động kế tiếp $A'=1$ tại B.

- (a) Tính mục tiêu Sarsa và mục tiêu Q-learning.
- (b) Nêu điều kiện cần và đủ để hai mục tiêu trùng nhau khi trạng thái kế tiếp chưa kết thúc, với cùng bảng và cùng phần thưởng.
- (c) Nêu cặp nào được cập nhật trong mỗi thuật toán.
:::

::: hint Gợi ý Bài tập 06.5
Sarsa phải dùng $A'=1$ đã cho; Q-learning dùng cực đại của hàng B. So sánh hai số hạng tiếp nối mà không đổi dữ liệu.
:::

::: solution Lời giải Bài tập 06.5
**Câu (a).** Mục tiêu Sarsa là $-1+Q(\mathrm B,1)=-1+1=0$. Mục tiêu Q-learning là $-1+\max(800,1)=799$.

**Câu (b).** Hai mục tiêu chỉ khác ở số hạng tiếp nối, nên chúng trùng nhau khi và chỉ khi $\gamma Q(S',A')=\gamma\max_aQ(S',a)$. Với $\gamma>0$, điều này tương đương $Q(S',A')=\max_aQ(S',a)$, tức $A'\in\mathcal G_Q(S')$; không cần cực đại duy nhất. Với $\gamma=0$, hai mục tiêu luôn trùng nhau và bằng $R$.

**Câu (c).** Cả hai thuật toán chỉ cập nhật ô $(\mathrm C,0)$ của cặp đã thực hiện; hành vi quyết định ô nào được cập nhật, mục tiêu quyết định cập nhật hướng về đâu.

**Kiểm tra lại.** Ở đây $A'=1\notin\mathcal G_Q(\mathrm B)=\{0\}$, nên hai mục tiêu khác nhau, khớp $0\ne799$; hai mục tiêu lệch nhau $799$. Hai lỗi thường gặp: để Sarsa tự thay $A'=1$ bằng hành động tốt hơn, khi đó thuật toán đã thành Q-learning; và cho rằng Q-learning cập nhật ô $(\mathrm B,0)$ vì ô này đạt cực đại, trong khi ô được cập nhật luôn là cặp $(S,A)$ đã thực hiện.
:::

### Bài tập 06.13. Monte Carlo và Q-learning trên dãy sáu ô có chuyển ngẫu nhiên

- **Mức độ:** tính toán; mục tiêu học tập 3 và 4 của ghi chú.
- **Nguồn:** Bài tập tuần 3 (2025–2026), bài 10, các câu 1–3 (câu 4 về xấp xỉ tuyến tính thuộc Bài 07, không dùng ở đây). Câu (a) ứng với câu 1 của bài gốc; câu (b) mở rộng câu 1 (lợi tức bị cắt, giá trị khi bỏ giới hạn số bước); câu (e) là phần bổ sung.

::: exercise Bài tập 06.13 (Monte Carlo và Q-learning trên dãy sáu ô có chuyển ngẫu nhiên)
Sáu ô xếp thành hàng A–B–C–D–E–F; A và F là trạng thái kết thúc, tập trạng thái không kết thúc là $\{\mathrm B,\mathrm C,\mathrm D,\mathrm E\}$, và mỗi lượt bắt đầu tại D. Tại mỗi ô không kết thúc có hai hành động: $0$ (trái) và $1$ (phải). Mỗi hành động đi một ô theo hướng của nó, trừ hành động $0$ tại B: với xác suất $0{,}9$ tác tử tới A, với xác suất $0{,}1$ tác tử ở lại B. Phần thưởng xác định theo ô đi tới: vào A nhận $10$, vào F nhận $-2$, vào B, C, D hoặc E (kể cả khi ở lại B) nhận $-1$. Hệ số chiết khấu là $\gamma=1/2$; mỗi lượt dài tối đa $5$ bước. Bảng khởi tạo:

| Trạng thái | $Q_0(s,0)$ | $Q_0(s,1)$ |
|---|---:|---:|
| B | $-1$ | $1$ |
| C | $0$ | $2$ |
| D | $1$ | $0$ |
| E | $1$ | $5$ |

Hai lượt quan sát được, mỗi chuyển viết theo thứ tự $(S,A,R,S')$, gồm tổng cộng sáu mẫu chuyển:

- $\tau_1$: $(\mathrm D,0,-1,\mathrm C)$, $(\mathrm C,0,-1,\mathrm B)$, $(\mathrm B,0,-1,\mathrm B)$, $(\mathrm B,0,10,\mathrm A)$;
- $\tau_2$: $(\mathrm D,1,-1,\mathrm E)$, $(\mathrm E,1,-2,\mathrm F)$.

Các câu (c) và (d) dùng hai bản sao riêng của bảng khởi tạo.

- (a) Xác định chính sách tham lam theo $Q_0$ tại B, C, D, E và các chuyển của quá trình Markov có phần thưởng (Markov reward process, MRP) mà nó sinh ra (trạng thái kế tiếp, xác suất, phần thưởng).
- (b) Xác định lượt bắt đầu tại D dưới chính sách của (a) có kết thúc không. Tính lợi tức chiết khấu của lượt khi bị cắt ở bước $5$, và giá trị của bốn trạng thái dưới chính sách này khi bỏ giới hạn số bước.
- (c) Cập nhật Monte Carlo lần ghé đầu tiên theo cặp trên $\tau_1$ rồi $\tau_2$, với mọi bộ đếm ban đầu bằng $0$. Trình bày bảng cuối, gồm giá trị và bộ đếm. Tính riêng ô $(\mathrm B,0)$ nếu thay bằng mọi lần ghé.
- (d) Đặt lại bảng khởi tạo và cập nhật Q-learning với bước học $\alpha=1$ qua sáu mẫu theo thứ tự đã cho. Trình bày mục tiêu, giá trị mới của mỗi ô được cập nhật, và bảng cuối.
- (e) So sánh hành động tham lam tại D theo hai bảng cuối của (c) và (d), và giải thích khác biệt bằng mục tiêu mà mỗi phương pháp dùng cho cặp $(\mathrm D,1)$.
:::

::: hint Gợi ý Bài tập 06.13
Ở (a), so hai số trong từng hàng của $Q_0$. Ở (b), lần theo lượt từ D để xem nó có tới A hay F không, rồi dùng phương trình Bellman của chính sách (mục Hướng dẫn và ký hiệu). Ở (c), cặp $(\mathrm B,0)$ xuất hiện hai lần trong $\tau_1$ với hai lợi tức khác nhau, và lần ghé đầu là lần có chỉ số thời gian nhỏ hơn. Ở (d), với $\alpha=1$ giá trị mới bằng mục tiêu; mục tiêu dùng bảng ngay trước từng mẫu, kể cả ở chuyển ở lại B.
:::

::: solution Lời giải Bài tập 06.13
**Câu (a).** So hai số trong từng hàng của $Q_0$: tại B chọn $1$ ($1>-1$), tại C chọn $1$ ($2>0$), tại D chọn $0$ ($1>0$), tại E chọn $1$ ($5>1$). Mọi chuyển của MRP đều tất định, vì chuyển ngẫu nhiên chỉ có ở hành động $0$ tại B mà chính sách không chọn:

- B → C với xác suất $1$, phần thưởng $-1$;
- C → D với xác suất $1$, phần thưởng $-1$;
- D → C với xác suất $1$, phần thưởng $-1$;
- E → F với xác suất $1$, phần thưởng $-2$, rồi kết thúc.

**Câu (b).** Từ D, lượt đi D→C→D→C→… và không bao giờ tới A hay F. Giới hạn $5$ bước cắt lượt tại C, một trạng thái chưa kết thúc, sau năm phần thưởng $-1$; lợi tức chiết khấu của năm bước ấy, ký hiệu $G_0^{(5)}$, là

$$
G_0^{(5)}=-\Big(1+\tfrac12+\tfrac14+\tfrac18+\tfrac1{16}\Big)=-\tfrac{31}{16}.
$$

Bỏ giới hạn số bước, phương trình Bellman của chính sách cho $v(\mathrm C)=-1+\tfrac12v(\mathrm D)$ và $v(\mathrm D)=-1+\tfrac12v(\mathrm C)$, nên $v(\mathrm C)=v(\mathrm D)=-1/(1-\tfrac12)=-2$. Tiếp theo $v(\mathrm B)=-1+\tfrac12v(\mathrm C)=-2$ và $v(\mathrm E)=-2+\tfrac12\cdot0=-2$.

**Câu (c).** Với $\tau_1$ ($T=4$), tính lùi:

$$
\begin{aligned}
G_3&=10,\\
G_2&=-1+\tfrac12\cdot10=4,\\
G_1&=-1+\tfrac12\cdot4=1,\\
G_0&=-1+\tfrac12\cdot1=-\tfrac12 .
\end{aligned}
$$

Lần ghé đầu của $(\mathrm B,0)$ là $t=2$, có lợi tức $4$; lần ghé thứ hai, tại $t=3$ với lợi tức $10$, không được dùng. Với $\tau_2$ ($T=2$): $G_1=-2$ và $G_0=-1+\tfrac12\cdot(-2)=-2$. Mỗi cặp xuất hiện nhận đúng một lợi tức, nên $N=1$ và giá trị mới bằng lợi tức đó:

| Trạng thái | $Q(s,0)$ | $Q(s,1)$ | $N(s,0)$ | $N(s,1)$ |
|---|---:|---:|---:|---:|
| B | $4$ | $1$ | $1$ | $0$ |
| C | $1$ | $2$ | $1$ | $0$ |
| D | $-1/2$ | $-2$ | $1$ | $1$ |
| E | $1$ | $-2$ | $0$ | $1$ |

Những ô chưa có lợi tức nào giữ giá trị khởi tạo và bộ đếm $0$. Nếu dùng mọi lần ghé, riêng ô $(\mathrm B,0)$ nhận hai lợi tức $4$ và $10$, nên $N(\mathrm B,0)=2$ và $Q(\mathrm B,0)=(4+10)/2=7$.

**Câu (d).** Với $\alpha=1$, giá trị mới bằng mục tiêu $Y$:

| Mẫu | Ô cập nhật | Mục tiêu và giá trị mới |
|---:|---|---|
| 1: D → C | $(\mathrm D,0)$ | $-1+\tfrac12\max(0;\,2)=0$ |
| 2: C → B | $(\mathrm C,0)$ | $-1+\tfrac12\max(-1;\,1)=-\tfrac12$ |
| 3: B → B | $(\mathrm B,0)$ | $-1+\tfrac12\max(-1;\,1)=-\tfrac12$ |
| 4: B → A | $(\mathrm B,0)$ | A kết thúc: $10$ |
| 5: D → E | $(\mathrm D,1)$ | $-1+\tfrac12\max(1;\,5)=\tfrac32$ |
| 6: E → F | $(\mathrm E,1)$ | F kết thúc: $-2$ |

Ở mẫu 3, hàng B ở vế phải là hàng ngay trước cập nhật, $(-1;\,1)$; mẫu 4 mới thay ô $(\mathrm B,0)$ bằng $10$. Bảng cuối:

| Trạng thái | $Q(s,0)$ | $Q(s,1)$ |
|---|---:|---:|
| B | $10$ | $1$ |
| C | $-1/2$ | $2$ |
| D | $0$ | $3/2$ |
| E | $1$ | $-2$ |

**Câu (e).** Theo bảng Monte Carlo, hàng D là $(-\tfrac12;\,-2)$, nên hành động tham lam tại D là $0$ (trái). Theo bảng Q-learning, hàng D là $(0;\,\tfrac32)$, nên hành động tham lam là $1$ (phải). Khác biệt nằm ở ô $(\mathrm D,1)$. Monte Carlo dùng lợi tức thật của $\tau_2$, $G_0=-2$. Q-learning dùng mục tiêu bootstrap (bootstrap target) $-1+\tfrac12\max_aQ(\mathrm E,a)$ tại mẫu 5, khi hàng E còn là giá trị khởi tạo $(1;\,5)$ chưa từng được quan sát; mẫu 6 chỉ hạ $(\mathrm E,1)$ xuống $-2$ sau đó. Nếu lặp lại mẫu 5 thêm một lần trên bảng cuối, mục tiêu là $-1+\tfrac12\max(1;\,-2)=-\tfrac12$, và hàng D trở thành $(0;\,-\tfrac12)$, xếp trái trên phải.

**Kiểm tra lại.** Hai lượt đã cho dài $4$ và $2$ bước, đều kết thúc thật tại A hoặc F trước giới hạn $5$ bước, nên các lợi tức ở (c) là lợi tức hoàn chỉnh. Ở (b), lợi tức bị cắt $-\tfrac{31}{16}$ thiếu đúng phần $\gamma^5v(\mathrm C)=\tfrac1{32}\cdot(-2)=-\tfrac1{16}$ so với $v(\mathrm D)=-2$. Ba lỗi thường gặp: quên hệ số chiết khấu, cho các lợi tức $7,8,9,10$ thay cho $-\tfrac12,1,4,10$ trong $\tau_1$; dùng lợi tức $10$ của lần ghé thứ hai cho $(\mathrm B,0)$ trong Monte Carlo lần ghé đầu; và thay mẫu $(\mathrm B,0,-1,\mathrm B)$ bằng kỳ vọng theo hai xác suất $0{,}9$ và $0{,}1$, trong khi cả hai phương pháp chỉ dùng chuyển thật sự quan sát được.
:::

### Bài tập 06.14. Chính sách $\varepsilon$-tham lam trong lớp $\varepsilon$-mềm

- **Mức độ:** chứng minh; mục tiêu học tập 2 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Định nghĩa 06.3, 06.4, Mệnh đề 06.6 và Ví dụ 06.5 (môi trường một bước); Sutton và Barto (2018), §5.4, tr. 100–101 (chính sách $\varepsilon$-mềm, chính sách $\varepsilon$-tham lam). Bộ chính sách $\pi^{(1)},\dots,\pi^{(4)}$ là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 06.14 (Chính sách $\varepsilon$-tham lam trong lớp $\varepsilon$-mềm)
Cho một trạng thái $s$ với $m(s)$ hành động, một bảng $Q$ bất kỳ và $\varepsilon\in[0,1]$. Chính sách $\varepsilon$-tham lam theo $Q$ là $\pi_\varepsilon(a\mid s)=\varepsilon/m(s)+(1-\varepsilon)\,\mathbf 1\{a\in\mathcal G_Q(s)\}/|\mathcal G_Q(s)|$, với $\mathcal G_Q(s)$ là tập hành động đạt cực đại của hàng $s$; chính sách $\pi$ là $\varepsilon$-mềm nếu $\pi(a\mid s)\ge\varepsilon/m(s)$ với mọi $a$.

- (a) Chứng minh $\pi_\varepsilon(\cdot\mid s)$ là một phân phối trên $\mathcal A(s)$ và là $\varepsilon$-mềm.
- (b) Xét ba hành động $0,1,2$ và $\varepsilon=0{,}3$. Với mỗi phân phối sau tại $s$, xác định nó có $0{,}3$-mềm không và có là chính sách $0{,}3$-tham lam theo một bảng $Q$ nào đó không: $\pi^{(1)}=(0{,}45;\,0{,}45;\,0{,}1)$, $\pi^{(2)}=(0{,}8;\,0{,}1;\,0{,}1)$, $\pi^{(3)}=(0{,}5;\,0{,}4;\,0{,}1)$, $\pi^{(4)}=(0{,}05;\,0{,}05;\,0{,}9)$.
- (c) Chứng minh rằng với $m(s)\ge2$ và $\varepsilon<1$, tại $s$ chỉ có hữu hạn phân phối $\varepsilon$-tham lam, trong khi có vô số phân phối $\varepsilon$-mềm; suy ra chiều ngược của (a) sai. Xác định điều gì xảy ra khi $\varepsilon=1$.
- (d) Trong môi trường một bước của Ví dụ 06.5 (mỗi hành động $0,1,2$ kết thúc lượt ngay với phần thưởng tất định $3$, $3$, $-1$, nên $q_\pi(s,\cdot)=(3;\,3;\,-1)$ với mọi $\pi$), gọi $\pi'$ là chính sách $0{,}3$-tham lam theo $q_\pi$ với $\pi=\pi^{(3)}$. Chứng minh $v_{\pi'}(s)=v_\pi(s)$ dù $\pi'\ne\pi$. Với $\varepsilon<1$, nêu và chứng minh điều kiện cần và đủ để bất đẳng thức một bước $\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$ của Mệnh đề 06.6 xảy ra dấu bằng.
:::

::: hint Gợi ý Bài tập 06.14
Ở (a), cộng riêng hai số hạng của công thức theo $a$. Ở (b), một phân phối $0{,}3$-tham lam nhận nhiều nhất hai mức: $0{,}1$ tại hành động không cực đại và $0{,}1+0{,}7/g$ tại $g$ hành động cực đại. Ở (c), phân phối $\varepsilon$-tham lam được xác định hoàn toàn bởi tập $\mathcal G_Q(s)$. Ở (d), viết $\pi(a\mid s)=\varepsilon/m+(1-\varepsilon)w(a\mid s)$ với $w(a\mid s)=[\pi(a\mid s)-\varepsilon/m]/(1-\varepsilon)$, rồi so trung bình theo $w$ của $q_\pi(s,\cdot)$ với $\max_aq_\pi(s,a)$.
:::

::: solution Lời giải Bài tập 06.14
**Câu (a).** Mỗi số hạng không âm: $\varepsilon/m(s)\ge0$ và $(1-\varepsilon)\mathbf 1\{\cdot\}/|\mathcal G_Q(s)|\ge0$, với $|\mathcal G_Q(s)|\ge1$ vì tập hành động hữu hạn và khác rỗng nên hàng $s$ đạt cực đại. Cộng theo $a\in\mathcal A(s)$: số hạng thứ nhất cho $m(s)\cdot\varepsilon/m(s)=\varepsilon$; số hạng thứ hai bằng $(1-\varepsilon)/|\mathcal G_Q(s)|$ tại mỗi hành động của $\mathcal G_Q(s)$ và bằng $0$ ở các hành động khác, nên cho $(1-\varepsilon)\,|\mathcal G_Q(s)|/|\mathcal G_Q(s)|=1-\varepsilon$. Tổng bằng $\varepsilon+(1-\varepsilon)=1$.

Vậy $\pi_\varepsilon(\cdot\mid s)$ là một phân phối. Vì số hạng thứ hai không âm, $\pi_\varepsilon(a\mid s)\ge\varepsilon/m(s)$ với mọi $a$, tức $\pi_\varepsilon$ là $\varepsilon$-mềm. $\square$

**Câu (b).** Với $m=3$ và $\varepsilon=0{,}3$, cận dưới của lớp mềm là $0{,}1$; một phân phối $0{,}3$-tham lam có xác suất $0{,}1$ tại hành động không cực đại và $0{,}1+0{,}7/g$ tại $g\in\{1,2,3\}$ hành động cực đại, tức $0{,}8$, $0{,}45$ hoặc $1/3$.

- $\pi^{(1)}$: mọi xác suất $\ge0{,}1$, nên $0{,}3$-mềm; có dạng $0{,}3$-tham lam với $\mathcal G_Q(s)=\{0,1\}$, chẳng hạn theo $Q(s,\cdot)=(3;\,3;\,-1)$.
- $\pi^{(2)}$: $0{,}3$-mềm; có dạng $0{,}3$-tham lam với $\mathcal G_Q(s)=\{0\}$.
- $\pi^{(3)}$: $0{,}3$-mềm, nhưng không $0{,}3$-tham lam theo bảng nào, vì $0{,}5$ và $0{,}4$ không thuộc tập mức $\{0{,}1;\,0{,}8;\,0{,}45;\,1/3\}$.
- $\pi^{(4)}$: không $0{,}3$-mềm, vì $0{,}05<0{,}1$; do đó theo (a) cũng không $0{,}3$-tham lam. Nó là chính sách $0{,}15$-tham lam với $\mathcal G_Q(s)=\{2\}$, vì $0{,}15/3=0{,}05$ và $0{,}05+0{,}85=0{,}9$; tính mềm luôn gắn với một giá trị $\varepsilon$ cụ thể.

**Câu (c).** Với $\varepsilon$ cố định, công thức của $\pi_\varepsilon(\cdot\mid s)$ chỉ phụ thuộc $Q$ qua tập $\mathcal G_Q(s)$, một tập con khác rỗng của $\mathcal A(s)$; có $2^{m(s)}-1$ tập như vậy. Hai sự kiện cho thấy số phân phối $\varepsilon$-tham lam tại $s$ đúng bằng $2^{m(s)}-1$ khi $\varepsilon<1$.

- Mọi tập con khác rỗng $\mathcal G$ đều là tập cực đại của một bảng: với $Q(s,a)=\mathbf 1\{a\in\mathcal G\}$, các hành động trong $\mathcal G$ có giá trị $1$, các hành động còn lại có giá trị $0$, nên $\mathcal G_Q(s)=\mathcal G$.
- Hai tập cực đại khác nhau cho hai phân phối khác nhau: khi $\varepsilon<1$, phần $(1-\varepsilon)/|\mathcal G|>0$ chỉ cộng vào các hành động của $\mathcal G$, nên $\mathcal G$ chính là tập các hành động có xác suất lớn hơn $\varepsilon/m(s)$ và đọc lại được từ phân phối.

Với $m=3$ và $\varepsilon=0{,}3$ có đúng $7$ phân phối: ba phân phối dạng $(0{,}8;\,0{,}1;\,0{,}1)$, ba phân phối dạng $(0{,}45;\,0{,}45;\,0{,}1)$ và phân phối đều. Ngược lại, với $m(s)\ge2$, $\varepsilon<1$ và mỗi $\lambda\in[0,1]$, phân phối gán $\varepsilon/m(s)+\lambda(1-\varepsilon)$ cho hành động thứ nhất, $\varepsilon/m(s)+(1-\lambda)(1-\varepsilon)$ cho hành động thứ hai và $\varepsilon/m(s)$ cho các hành động còn lại là $\varepsilon$-mềm. Vì $1-\varepsilon>0$, các giá trị $\lambda$ khác nhau cho các phân phối khác nhau, nên lớp $\varepsilon$-mềm vô hạn và chứa phân phối không $\varepsilon$-tham lam; $\pi^{(3)}$ ứng với $\lambda=4/7$. Khi $\varepsilon=1$, điều kiện mềm buộc mọi xác suất $\ge1/m(s)$ mà tổng bằng $1$, nên mọi xác suất bằng $1/m(s)$: lớp $1$-mềm chỉ gồm phân phối đều, và chính sách $1$-tham lam theo mọi bảng cũng là phân phối đều, nên hai lớp bằng nhau. $\square$

**Câu (d).** Với $\pi=\pi^{(3)}$, $v_\pi(s)=0{,}5\cdot3+0{,}4\cdot3+0{,}1\cdot(-1)=2{,}6$. Tập cực đại của $q_\pi(s,\cdot)$ là $\{0,1\}$, nên $\pi'=(0{,}45;\,0{,}45;\,0{,}1)\ne\pi$ và $v_{\pi'}(s)=0{,}45\cdot3+0{,}45\cdot3+0{,}1\cdot(-1)=2{,}6=v_\pi(s)$. Vì bài toán chỉ có một bước, $v_{\pi'}(s)=\sum_a\pi'(a\mid s)q_\pi(s,a)$, nên bất đẳng thức một bước xảy ra dấu bằng.

Điều kiện tổng quát, với $\varepsilon<1$: viết $\pi(a\mid s)=\varepsilon/m+(1-\varepsilon)w(a\mid s)$, trong đó $w(a\mid s)=[\pi(a\mid s)-\varepsilon/m]/(1-\varepsilon)$ không âm vì $\pi$ là $\varepsilon$-mềm và có tổng bằng $1$. Phần sàn $\varepsilon/m$ góp như nhau vào $\sum_a\pi'(a\mid s)q_\pi(s,a)$ và $v_\pi(s)$, còn $\pi'$ dồn phần $1-\varepsilon$ vào các hành động cực đại, nên

$$
\sum_a\pi'(a\mid s)q_\pi(s,a)-v_\pi(s)=(1-\varepsilon)\sum_aw(a\mid s)\Big[\max_bq_\pi(s,b)-q_\pi(s,a)\Big].
$$

Vế phải là tổng các số hạng không âm nhân với $1-\varepsilon>0$, nên bằng $0$ khi và chỉ khi $w(a\mid s)=0$ tại mọi hành động $a$ không cực đại, tức $\pi$ chỉ đặt phần vượt sàn $1-\varepsilon$ lên các hành động cực đại của $q_\pi(s,\cdot)$. Với $\pi^{(3)}$, $w=(4/7;\,3/7;\,0)$ thỏa điều kiện này. Khi $\varepsilon=1$, mọi chính sách $1$-mềm là phân phối đều và dấu bằng luôn xảy ra. $\square$

**Kiểm tra lại.** Ở (d), $0{,}1\cdot(3+3-1)+0{,}7\cdot3=0{,}5+2{,}1=2{,}6$, khớp phân tách theo phần sàn của Ví dụ 06.5. Ba lỗi thường gặp: kết luận "$\pi$ là $\varepsilon$-mềm nên là $\varepsilon$-tham lam", bị bác bởi $\pi^{(3)}$; đọc Mệnh đề 06.6 như bảo đảm cải thiện chặt, trong khi (d) cho $v_{\pi'}=v_\pi$ với $\pi'\ne\pi$; và kiểm tính mềm của $\pi^{(4)}$ với cận $0{,}15/3$ thay cho $0{,}3/3$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 06.15. Mục tiêu tại bước cắt ngắn của tàu đổ bộ

- **Mức độ:** vận dụng [Lập trình]; mục tiêu học tập 4 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Nhận xét 06.13 và Tình huống 06.1; notebook thực hành Bài 06, phần 3 (`paired_difference`) và phần 6–8 (`sarsa`, `q_learning`). Số cập nhật $h$ là của một lần chạy đã nhúng (phần 8); năm lần huấn luyện sơ bộ được ghi nhận khi soạn notebook, chạy ngoài notebook và được đánh giá trên một tập hạt giống khác `TEST_SEED` (phần 8.2). Bộ số của câu (a) là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 06.15 (Mục tiêu tại bước cắt ngắn của tàu đổ bộ)
Tàu đổ bộ của notebook: $2187$ ô, bốn hành động, $\gamma=0{,}99$; lượt kết thúc thật khi tàu rơi hoặc ra khỏi khung ($-100$) hay nằm yên ($+100$), và bị cắt ngắn ở bước $1000$ khi chưa kết thúc. Trong hàm `sarsa` và `q_learning` của notebook, cờ `terminated` báo trạng thái kết thúc thật, cờ `truncated` báo cắt ngắn; mục tiêu chỉ bằng `r` khi `terminated` đúng, nên ở bước cắt ngắn mục tiêu vẫn chứa giá trị tiếp nối. Một lần chạy đã nhúng trong notebook cho $h=1\,276\,891$ cập nhật Sarsa và $h=907\,456$ cập nhật Q-learning trong $3000$ lượt huấn luyện. Năm lần huấn luyện sơ bộ của Sarsa với các hạt giống huấn luyện khác và cùng cấu hình, chạy ngoài notebook khi soạn và cùng được đánh giá trên một tập $100$ lượt riêng (khác `TEST_SEED`), cho tổng thưởng trung bình của chính sách tham lam từ $66{,}1$ đến $136{,}1$.

- (a) Ở bước thứ $1000$ của một lượt, tác tử ở ô $S$, thực hiện $A$ với $Q(S,A)=20$, nhận $R=-0{,}8$, và ô $S'$ chưa kết thúc có hàng $Q(S',\cdot)=(25;\,30;\,18;\,22)$; Sarsa đã chọn $A'=3$; bước học là $\alpha=0{,}05$. Tính $Y$, $\delta$ và giá trị mới của $Q(S,A)$ cho Sarsa, cho Q-learning, và cho cách cài đặt sai đặt $Y=R$ khi bị cắt ngắn.
- (b) Viết thay đổi trong mã để tạo biến thể sai "đặt $Y=R$ khi cắt ngắn" cho cả hai hàm. Tính cận trên của tỉ lệ cập nhật bị ảnh hưởng trong $3000$ lượt huấn luyện của mỗi thuật toán.
- (c) Giải thích vì sao một tỉ lệ cập nhật nhỏ như ở (b) vẫn có thể làm thay đổi các ô khác của bảng.
- (d) Thiết kế phép so sánh giữa cách cài đặt đúng và biến thể sai: nêu các hạt giống được giữ cố định, chính sách được đánh giá, đại lượng báo cáo và kết luận nào được phép rút ra từ một lần huấn luyện.
- (e) Chạy phép so sánh của (d) cho cả hai thuật toán. Hai bảng đúng đã có trong notebook (phần 8), nên chỉ cần hai lần huấn luyện mới cho biến thể sai, mỗi lần khoảng $80$–$105$ giây trên máy dùng để soạn notebook (trên Colab có thể lâu hơn). Sản phẩm nộp: mã hai hàm đã sửa; một bảng bốn dòng (hai thuật toán, hai cách cài đặt) gồm tổng thưởng trung bình $\pm$ sai số chuẩn và tỉ lệ ba kiểu dừng; hai hiệu ghép cặp "đúng trừ sai" kèm nửa độ rộng khoảng $95\%$; một đoạn kết luận không quá năm câu.
:::

::: hint Gợi ý Bài tập 06.15
Ở (a), hai mục tiêu bootstrap chỉ khác ở số hạng tiếp nối; mục tiêu sai không có số hạng ấy. Ở (b), mỗi lượt bị cắt ngắn nhiều nhất một lần. Ở (c), giá trị mới của $Q(S,A)$ đi vào mục tiêu của những cặp đứng trước $S$. Ở (d), dùng hiệu ghép cặp trên cùng tập hạt giống kiểm tra và so độ lớn của hiệu với độ biến thiên giữa các lần huấn luyện.
:::

::: solution Lời giải Bài tập 06.15
**Câu (a).** Sarsa dùng $Q(S',3)=22$:

$$
\begin{aligned}
Y&=-0{,}8+0{,}99\cdot22=20{,}98,\\
\delta&=20{,}98-20=0{,}98,\\
Q(S,A)&\leftarrow20+0{,}05\cdot0{,}98=20{,}049 .
\end{aligned}
$$

Q-learning dùng cực đại $30$ của hàng $S'$:

$$
\begin{aligned}
Y&=-0{,}8+0{,}99\cdot30=28{,}9,\\
\delta&=28{,}9-20=8{,}9,\\
Q(S,A)&\leftarrow20+0{,}05\cdot8{,}9=20{,}445 .
\end{aligned}
$$

Cách cài đặt sai cho cùng kết quả ở hai thuật toán:

$$
\begin{aligned}
Y&=-0{,}8,\\
\delta&=-0{,}8-20=-20{,}8,\\
Q(S,A)&\leftarrow20+0{,}05\cdot(-20{,}8)=18{,}96 .
\end{aligned}
$$

Biến thể sai coi $S'$, một trạng thái tàu chưa kết thúc, như trạng thái kết thúc có giá trị $0$, nên kéo $Q(S,A)$ xuống thay vì đẩy lên.

**Câu (b).** Trong `sarsa`, đổi điều kiện `if terminated:` (nhánh `a2, y = None, r`) thành `if terminated or truncated:`; trong `q_learning`, đổi `y = r if terminated else r + gamma * Q[s2].max()` thành `y = r if (terminated or truncated) else r + gamma * Q[s2].max()`. Vòng lặp đã dừng khi `terminated or truncated`, nên `a2 = None` không được dùng tiếp. Nên chép mỗi hàm thành một hàm mới, chẳng hạn `sarsa_cut`, để giữ nguyên bản đúng.

Mỗi lượt có nhiều nhất một bước cắt ngắn, nên số cập nhật bị ảnh hưởng không vượt số lượt huấn luyện, $3000$. Tỉ lệ không vượt $3000/1\,276\,891\approx0{,}23\%$ với Sarsa và $3000/907\,456\approx0{,}33\%$ với Q-learning. Cận này dùng số cập nhật của lần chạy đã nhúng; biến thể sai cho đường học khác, nên $h$ của nó có thể khác.

**Câu (c).** Giá trị sai của $Q(S,A)$ không dừng ở ô đó. Ở những lượt sau, mỗi khi một cặp $(S_-,A_-)$ dẫn tới $S$ và hành động tiếp theo tại $S$ là $A$ (Sarsa) hay $A$ là cực đại của hàng $S$ (Q-learning), mục tiêu của $(S_-,A_-)$ chứa $\gamma Q(S,A)$. Sai lệch vì thế lan lùi qua các cập nhật bootstrap, giống cách phần thưởng $1000$ lan lùi từng ô trên dãy năm ô. Sai lệch cũng có thể đổi hành động tham lam tại $S$, nên đổi chính sách.

**Câu (d).** Phép so sánh gồm các bước sau.

- Giữ cố định `TRAIN_SEED` (địa hình và lực đẩy của từng lượt huấn luyện), `AGENT_SEED` (nguồn ngẫu nhiên của tác tử), lịch $\varepsilon_k$, lịch $\alpha_n$, số lượt $3000$ và cách chia ô; chỉ đổi cách xử lý bước cắt ngắn.
- Đánh giá chính sách tham lam theo mỗi bảng cuối trên cùng $100$ lượt kiểm tra với hạt giống `TEST_SEED`, không thăm dò và không cập nhật.
- Báo tổng thưởng trung bình kèm sai số chuẩn, tỉ lệ ba kiểu dừng (nằm yên, rơi, cắt ngắn), và hiệu ghép cặp `paired_difference` kèm nửa độ rộng khoảng $95\%$; đọc khoảng như ở Bài tập 06.17(d).
- Kết luận được phép chỉ áp dụng cho hai bảng cụ thể của một lần huấn luyện, không cho hai cách cài đặt nói chung. Năm lần huấn luyện sơ bộ của Sarsa, cùng cấu hình và cùng tập đánh giá, đã lệch nhau tới $136{,}1-66{,}1=70$ điểm chỉ vì đổi hạt giống huấn luyện, nên một hiệu cỡ này có thể đến từ hạt giống. Muốn so hai cách cài đặt, cần lặp lại với nhiều cặp hạt giống huấn luyện (notebook, phần 13, nhiệm vụ 1).

**Câu (e).** Lời giải không nêu con số, vì kết quả thuộc về lần chạy của người làm. Với mỗi thuật toán, đọc hiệu "đúng trừ sai". Nếu khoảng chứa $0$, lần chạy chưa phân biệt được hai bảng. Nếu khoảng không chứa $0$, ghi chiều của hiệu và giới hạn của (d): một lần huấn luyện, một ngân sách. Cột tỉ lệ cắt ngắn đáng đối chiếu, vì biến thể sai chỉ đổi mục tiêu ở bước cắt ngắn; mọi khác biệt ở cột này cũng chỉ là quan sát của một lần chạy. Đoạn kết luận cần nêu rằng cách cài đặt đúng được chọn theo Nhận xét 06.13, không theo kết quả của thí nghiệm này.

**Kiểm tra lại.** Ở (a), hai mục tiêu bootstrap trùng nhau khi $A'\in\{1\}$, tập cực đại của hàng $S'$; với $A'=3$ chúng khác nhau $0{,}99\cdot(30-22)=7{,}92=28{,}9-20{,}98$. Ba lỗi thường gặp: gộp cờ `truncated` vào điều kiện kết thúc; so hai biến thể trên hai tập hạt giống kiểm tra khác nhau, làm mất tính ghép cặp; và báo một hiệu dương từ một lần huấn luyện như bằng chứng rằng một cách cài đặt tốt hơn.
:::

### Bài tập 06.16. Lịch thăm dò và lịch bước học của tàu đổ bộ so với GLIE và Robbins–Monro

- **Mức độ:** vận dụng [Lập trình]; mục tiêu học tập 5 của ghi chú.
- **Nguồn:** notebook thực hành Bài 06, phần 5, 6, 10 và phần 13, nhiệm vụ 2–3 (số liệu bộ đếm là của một lần chạy đã nhúng); ghi chú bài giảng Bài 06, Mục 5.2–5.3 và Ví dụ 06.14–06.15; Singh và cộng sự (2000) cho lịch thăm dò theo trạng thái. Giá trị $c=100$ và quy ước đếm lượt từ $1$ là lựa chọn của bài tập.

::: exercise Bài tập 06.16 (Lịch thăm dò và lịch bước học của tàu đổ bộ so với GLIE và Robbins–Monro)
Trong notebook tàu đổ bộ (bốn hành động mỗi ô), lịch thăm dò `linear_epsilon(k)` nhận chỉ số lượt huấn luyện $k=0,1,2,\dots$ (lượt đầu có $k=0$) và giảm $\varepsilon$ tuyến tính từ $1$ về $0{,}05$ trong $1500$ lượt rồi giữ nguyên; lịch bước học `step_size(n)` trả $\max(0{,}05;\,n^{-0{,}6})$, với $n\ge1$ là số thứ tự của lần cập nhật sắp thực hiện của cặp. Hàm `train_and_test(algo, eps_fn=..., alpha_fn=...)` huấn luyện $3000$ lượt rồi đánh giá chính sách tham lam trên $100$ lượt kiểm tra với hạt giống `TEST_SEED`. Trong một lần chạy đã nhúng, sau $3000$ lượt Sarsa, các cặp đã được cập nhật có số cập nhật trung vị $n=17$ và lớn nhất $n=80\,743$; $1334$ trong $2187$ ô được ghé. Phần 13 của notebook (nhiệm vụ 2–3) đề nghị thử $\varepsilon_k=\min(1,c/k)$ và $\alpha_n=1/n$; trong bài này $k=1,2,\dots$ đếm lượt từ $1$ và $c=100$.

- (a) Viết hai hàm `eps_fn`, `alpha_fn` cho hai lịch trên theo quy ước chỉ số của notebook. Xác định lỗi xảy ra nếu viết `min(1, c / k)` với `k` của notebook.
- (b) Với một hàng có cực đại duy nhất, tính $\varepsilon_k$ và khối xác suất trên hành động cực đại tại các lượt $k=1000$, $2000$, $3000$ dưới lịch mới và dưới lịch tuyến tính. Xác định lịch nào thỏa điều kiện tham lam trong giới hạn khi $k\to\infty$.
- (c) Giả sử một ô chỉ được ghé đúng một lần trong mỗi lượt $k=2^n$, $n=1,2,\dots$, không được ghé ở lượt khác, và hàng của nó giữ một cực đại duy nhất cố định. Tính tổng các xác suất chọn một hành động không cực đại cố định tại các lần ghé ấy dưới lịch $\min(1,100/k)$, và kết luận về điều kiện thăm dò vô hạn. So với một ô được ghé ít nhất một lần trong mọi lượt.
- (d) Nhắc lại kết quả trung bình gia tăng của Bài 05 cho mục tiêu thay đổi: chứng minh rằng với $\alpha_n=1/n$, sau $n$ cập nhật, $Q(s,a)$ bằng trung bình cộng của $n$ mục tiêu $Y_1,\dots,Y_n$ mà cặp đã nhận, không phụ thuộc $Q_0(s,a)$. Tính bước học tại $n=17$ và $n=80\,743$ dưới $1/n$ và dưới `step_size`, và giải thích lý do notebook giữ sàn $0{,}05$.
- (e) Dùng thiết kế của Bài tập 06.15(d) để so cấu hình gốc với ba cấu hình đổi một hoặc cả hai lịch. Nêu giả thiết của Định lý 06.21–06.22 mà mỗi thay đổi nhắm tới. Nêu kết luận được phép rút ra nếu cấu hình dùng `eps_glie` và `alpha_rm` cho tổng thưởng cao hơn; cấu hình này gần GLIE theo nghĩa của (c) (tham lam trong giới hạn, nhưng thăm dò vô hạn theo từng cặp không được bảo đảm) và thỏa hai tổng Robbins–Monro theo số lần cập nhật của mỗi cặp.
- (f) Chạy phép so sánh của (e) cho Sarsa: cấu hình gốc đã có trong notebook, nên cần ba lần huấn luyện mới, mỗi lần khoảng $80$–$105$ giây trên máy dùng để soạn notebook (tổng khoảng $4$–$5{,}5$ phút; trên Colab có thể lâu hơn). Phần cho Q-learning không bắt buộc. Sản phẩm nộp: mã `eps_fn`, `alpha_fn`; bảng bốn cấu hình với tổng thưởng trung bình $\pm$ sai số chuẩn và tỉ lệ ba kiểu dừng; ba hiệu ghép cặp so với cấu hình gốc kèm nửa độ rộng khoảng $95\%$; một đoạn kết luận không quá năm câu nêu giả thiết nào đã đổi và giả thiết nào vẫn bị vi phạm.
:::

::: hint Gợi ý Bài tập 06.16
Ở (a), lượt đầu của notebook có `k = 0`. Ở (b), khối xác suất trên cực đại duy nhất là $1-\varepsilon_k+\varepsilon_k/4$. Ở (c), tách các lượt có $2^n\le100$ khỏi các lượt còn lại; dùng vế thứ nhất của bổ đề Borel–Cantelli (Ví dụ 06.14). Ở (d), quy nạp theo $n$ với $\alpha_1=1$.
:::

::: solution Lời giải Bài tập 06.16
**Câu (a).** Lượt thứ $k$ (đếm từ $1$) ứng với chỉ số `k + 1` của notebook:

```python
C_EPS = 100

def eps_glie(k, c=C_EPS):
    # notebook đếm lượt từ k = 0: lượt thứ k + 1
    return min(1.0, c / (k + 1))

def alpha_rm(n):
    # n >= 1: thứ tự của cập nhật sắp làm của cặp
    return 1.0 / n
```

Nếu viết `min(1, c / k)` với `k` của notebook, lượt đầu có `k = 0` và Python dừng với lỗi chia cho $0$ (`ZeroDivisionError`). Lời gọi so sánh là `train_and_test(sarsa, eps_fn=eps_glie)` hay `train_and_test(sarsa, alpha_fn=alpha_rm)`.

**Câu (b).** Với $c=100$ thì $\varepsilon_k=1$ khi $k\le100$ và $\varepsilon_k=100/k$ khi $k>100$. Khối trên cực đại duy nhất là $1-\varepsilon_k+\varepsilon_k/4=1-\tfrac34\varepsilon_k$. Lịch tuyến tính ở lượt $k$ là `linear_epsilon(k - 1)`.

| Lượt $k$ | $\varepsilon_k$ mới | Khối, lịch mới | $\varepsilon$ tuyến tính | Khối, lịch tuyến tính |
|---:|---:|---:|---:|---:|
| $1000$ | $0{,}1$ | $0{,}925$ | $\approx0{,}367$ | $\approx0{,}725$ |
| $2000$ | $0{,}05$ | $0{,}9625$ | $0{,}05$ | $0{,}9625$ |
| $3000$ | $\approx0{,}0333$ | $0{,}975$ | $0{,}05$ | $0{,}9625$ |

Lịch $\min(1,100/k)$ có $\varepsilon_k\to0$, nên khối tiến tới $1$ và điều kiện tham lam trong giới hạn thỏa. Lịch tuyến tính giữ $\varepsilon=0{,}05$ từ lượt $1500$ trở đi, nên khối dừng ở $0{,}9625$ và điều kiện này không thỏa. Ở lượt $1000$, lịch tuyến tính còn thăm dò nhiều hơn lịch mới; sau lượt $2000$, lịch mới thăm dò ít hơn.

**Câu (c).** Tại lần ghé ở lượt $2^n$, xác suất chọn một hành động không cực đại cố định là $\varepsilon_{2^n}/4$. Với $n=1,\dots,6$ ($2^n\le64\le100$), $\varepsilon=1$; với $n\ge7$, $\varepsilon_{2^n}=100/2^n$. Tổng là

$$
\begin{aligned}
\sum_{n\ge1}\frac{\varepsilon_{2^n}}4
&=6\cdot\frac14+\sum_{n\ge7}\frac{25}{2^n}\\
&=\frac32+\frac{25}{64}\\
&=\frac{121}{64}\approx1{,}89<\infty .
\end{aligned}
$$

Theo vế thứ nhất của bổ đề Borel–Cantelli, vốn không cần tính độc lập, hành động ấy chỉ được thử hữu hạn lần, hầu chắc chắn. Điều kiện thăm dò vô hạn của Định nghĩa 06.18 vì thế không thỏa cho cặp này, dù $\varepsilon_k\to0$. Với một ô được ghé ít nhất một lần trong mọi lượt, tổng ít nhất là $\sum_{k>100}25/k=\infty$, và khi hàng giữ cực đại cố định như Ví dụ 06.14, vế thứ hai của bổ đề cho vô hạn lần thử.

Liên hệ với tàu đổ bộ: tần suất ghé từng ô không do lịch thăm dò quyết định, và lần chạy đã nhúng chỉ ghé $1334$ trong $2187$ ô sau $3000$ lượt. Singh và cộng sự (2000) dùng lịch theo trạng thái $\varepsilon_t(s)=c/C_t(s)$ với $0<c<1$, trong đó $C_t(s)$ là số lần ghé $s$ trong các bước $0,\dots,t$. Lịch này thỏa định nghĩa GLIE gốc của các tác giả, vốn chỉ đặt điều kiện tại các trạng thái được ghé vô hạn lần và đi kèm giả thiết MDP liên thông (ghi chú, Mục 5.2); Định nghĩa 06.18 đòi mọi cặp được thực hiện vô hạn lần, nên mạnh hơn.

**Câu (d).** Gọi $Q_n$ là giá trị của cặp sau $n$ cập nhật và $Y_n$ là mục tiêu của cập nhật thứ $n$. Ta chứng minh $Q_n=\tfrac1n\sum_{j=1}^nY_j$ bằng quy nạp. Với $n=1$, $\alpha_1=1$ nên $Q_1=Q_0+(Y_1-Q_0)=Y_1$, không phụ thuộc $Q_0$. Giả sử đúng tới $n-1$; khi đó

$$
\begin{aligned}
Q_n&=Q_{n-1}+\tfrac1n\big(Y_n-Q_{n-1}\big)\\
&=\tfrac{n-1}{n}\,Q_{n-1}+\tfrac1n\,Y_n\\
&=\tfrac{n-1}{n}\cdot\tfrac1{n-1}\sum_{j=1}^{n-1}Y_j+\tfrac1n\,Y_n\\
&=\tfrac1n\sum_{j=1}^{n}Y_j . \qquad\square
\end{aligned}
$$

Bước học tại hai mốc của lần chạy đã nhúng:

| $n$ | $1/n$ | `step_size(n)` |
|---:|---:|---:|
| $17$ | $\approx0{,}0588$ | $17^{-0{,}6}\approx0{,}183$ |
| $80\,743$ | $\approx1{,}24\cdot10^{-5}$ | $0{,}05$ (sàn) |

Dưới $1/n$, cặp được cập nhật nhiều nhất giữ trung bình của $80\,743$ mục tiêu, phần lớn được tính khi bảng và chính sách còn khác, và mỗi mục tiêu mới chỉ dịch giá trị khoảng $1/80\,743$ của sai lệch. Trong điều khiển, mục tiêu của một cặp đổi theo chính sách, nên notebook giữ sàn $0{,}05$ để các cặp được ghé nhiều còn phản ứng với mục tiêu mới (phần 6), chấp nhận vi phạm tổng thứ hai của Robbins–Monro. Điều kiện Robbins–Monro là thành phần của một chứng minh hội tụ khi số cập nhật tiến tới vô hạn; nó không nói gì về chất lượng bảng sau $3000$ lượt.

**Câu (e).** Bốn cấu hình cho mỗi thuật toán là gốc (`linear_epsilon`, `step_size`), đổi thăm dò (`eps_glie`, `step_size`), đổi bước học (`linear_epsilon`, `alpha_rm`) và đổi cả hai (`eps_glie`, `alpha_rm`), với hạt giống, cách đánh giá và đại lượng báo cáo như Bài tập 06.15(d).

- `eps_glie` nhắm tới điều kiện tham lam trong giới hạn của GLIE, chỉ có trong Định lý 06.22 (Sarsa). Với Q-learning, Định lý 06.21 không cần GLIE; đổi lịch thăm dò chỉ đổi dữ liệu thu được, nên đổi độ phủ của các cặp.
- `alpha_rm` nhắm tới Robbins–Monro theo cặp (Định nghĩa 06.19), có trong cả hai định lý.

Nếu cấu hình đổi cả hai cho tổng thưởng cao hơn với khoảng không chứa $0$, kết luận được phép chỉ là: với hạt giống huấn luyện này và ngân sách $3000$ lượt, bảng thu được cho chính sách tham lam tốt hơn trên tập kiểm tra. Kết quả ấy không xác nhận bảng đã hội tụ tới $q_*$: ngân sách hữu hạn, thăm dò vô hạn theo từng cặp không được bảo đảm (câu (c)), và giả thiết Markov của các ô gộp vẫn không thỏa (Bài tập 06.12 của ghi chú xét giả thiết này).

**Câu (f).** Lời giải không nêu con số, vì kết quả thuộc về lần chạy của người làm. Đọc mỗi hiệu ghép cặp như Bài tập 06.17(d). Theo câu (d), dưới `alpha_rm` các cặp được cập nhật nhiều có bước học rất nhỏ (từ /bin/bash{,}001$ trở xuống sau 000$ cập nhật), còn các cặp ít được cập nhật vẫn nhận bước lớn; vì vậy hiệu của cấu hình đổi bước học có thể mang dấu bất kỳ, và một lần chạy không cho biết dấu nào là điển hình. Đoạn kết luận cần nêu: cấu hình đổi thăm dò sửa điều kiện tham lam trong giới hạn, cấu hình đổi bước học sửa hai tổng Robbins–Monro, còn thăm dò vô hạn theo từng cặp và tính Markov vẫn không được bảo đảm trong mọi cấu hình.

**Kiểm tra lại.** Ở (b), $1-\tfrac34\cdot\tfrac1{30}=1-0{,}025=0{,}975$ và lịch tuyến tính ở lượt $1000$ cho $1-0{,}95\cdot\tfrac{999}{1500}=0{,}3673$. Ở (d), với $Y_1=Y_2=\cdots=y$ thì $Q_n=y$ với mọi $n\ge1$, khớp công thức trung bình. Ba lỗi thường gặp: đọc "$\varepsilon_k\to0$" như đủ cho GLIE, bị bác bởi câu (c); kết luận từ $\sum_n1/n=\infty$ rằng mọi cặp được cập nhật vô hạn lần, trong khi Robbins–Monro tính theo các lần cập nhật đã xảy ra của từng cặp; và coi tổng thưởng cao hơn sau khi đổi lịch là bằng chứng hội tụ.
:::

### Bài tập 06.17. Chọn phương pháp cho tàu đổ bộ

- **Mức độ:** vận dụng; mục tiêu học tập 4 và 5 của ghi chú.
- **Nguồn:** ghi chú bài giảng Bài 06, Nhận xét 06.10, 06.13 và Tình huống 06.1; notebook thực hành Bài 06, phần 4–8 và 10 (số liệu huấn luyện ở phần 8.1, số liệu đánh giá ở phần 8.2; một lần chạy đã nhúng).
- **Trùng trang chiếu:** [Bài tập: chọn phương pháp cho tàu đổ bộ](lecture-06-dieu-khien-phi-mo-hinh.html#/7/6) và [trang lời giải](lecture-06-dieu-khien-phi-mo-hinh.html#/7/7); câu (d) đọc hai dòng cuối của trang lời giải.

::: exercise Bài tập 06.17 (Chọn phương pháp cho tàu đổ bộ)
Tàu đổ bộ của notebook: mỗi biến liên tục của quan sát được chia thành ba khoảng và số chân chạm đất nhận ba giá trị, nên có $3^6\cdot3=2187$ ô; bốn hành động; $\gamma=0{,}99$; lượt kết thúc khi tàu rơi hoặc ra khỏi khung ($-100$) hay nằm yên ($+100$), và bị cắt ngắn ở bước $1000$. Hành vi là chính sách $\varepsilon_k$-tham lam với $\varepsilon_k$ giảm tuyến tính từ $1$ về $\varepsilon_{\min}=0{,}05$ trong $1500$ lượt đầu rồi giữ nguyên; bước học theo cặp là $\alpha_n=\max(0{,}05;\,n^{-0{,}6})$. Trong một lần chạy đã nhúng, $500$ lượt huấn luyện cuối của Sarsa (hành vi với $\varepsilon=0{,}05$) dài trung bình $655$ bước và $7\%$ số lượt bị cắt ngắn. Sau $3000$ lượt huấn luyện, chính sách tham lam theo mỗi bảng được đánh giá trên cùng $100$ lượt kiểm tra; tổng phần thưởng không chiết khấu của lượt, trung bình $\pm$ sai số chuẩn, là $26{,}2\pm14{,}0$ với Sarsa và $-6{,}6\pm17{,}2$ với Q-learning; hiệu ghép cặp Sarsa trừ Q-learning là $32{,}8\pm46{,}2$, trong đó $46{,}2$ là nửa độ rộng khoảng tin cậy $95\%$.

- (a) Chọn Monte Carlo hay phương pháp một bước, kèm lý do.
- (b) Viết mục tiêu Sarsa và mục tiêu Q-learning tại bước cắt ngắn.
- (c) Chỉ ra các giả thiết của Định lý 06.21–06.22 bị vi phạm, và các giả thiết được thỏa.
- (d) Từ kết quả đánh giá, xác định đã xếp hạng được hai thuật toán chưa.
:::

::: hint Gợi ý Bài tập 06.17
Phân biệt trạng thái kết thúc với lượt bị cắt ngắn (Nhận xét 06.10, 06.13). Với câu (c), kiểm lần lượt tính Markov, bước học và điều kiện tham lam trong giới hạn. Với câu (d), xét khoảng của hiệu ghép cặp có chứa $0$ không.
:::

::: solution Lời giải Bài tập 06.17
**Câu (a).** Chọn Sarsa hoặc Q-learning. Lượt bị cắt ngắn dừng tại một trạng thái chưa kết thúc nên thiếu lợi tức hoàn chỉnh, và Monte Carlo không dùng được dữ liệu của nó (Nhận xét 06.10). Trong $500$ lượt huấn luyện cuối của Sarsa, $7\%$ số lượt bị cắt, nên Monte Carlo bỏ toàn bộ dữ liệu của các lượt ấy; lượt dài trung bình $655$ bước, nên mỗi cập nhật Monte Carlo phải chờ hàng trăm bước. Phương pháp một bước cập nhật sau mỗi chuyển, kể cả trong lượt bị cắt.

**Câu (b).** Ở bước $1000$, $S'$ chưa kết thúc, nên mục tiêu vẫn chứa giá trị tiếp nối:

$$
Y^{\text{Sarsa}}=R+\gamma Q(S',A'),\qquad Y^{\text{Q}}=R+\gamma\max_aQ(S',a).
$$

Đặt $Y=R$ là coi một trạng thái giữa chừng như trạng thái kết thúc có giá trị $0$ (Nhận xét 06.13).

**Câu (c).** Các giả thiết bị vi phạm:

- Tính Markov: mỗi ô gộp vô số quan sát; hai quan sát trong cùng ô có thể dẫn tới phân phối ô kế tiếp khác nhau, nên không có $p(\cdot\mid s,a)$ chung cho ô.
- Robbins–Monro theo cặp: $n^{-0{,}6}\le0{,}05$ khi và chỉ khi $n\ge20^{5/3}\approx147{,}4$, nên $\alpha_n=0{,}05$ khi $n\ge148$ và $\sum_n\alpha_n^2=\infty$.
- GLIE, chỉ cần cho Sarsa: với một cực đại duy nhất, khối xác suất trên cực đại dừng ở $1-0{,}05+0{,}05/4=0{,}9625$, không tiến tới $1$.

Tập ô hữu hạn và $\gamma=0{,}99<1$ thì thỏa. Thiếu giả thiết nên định lý không bảo đảm hội tụ; điều đó cũng không chứng minh hai bảng phân kỳ.

**Câu (d).** Chưa xếp hạng được. Hai chính sách được chạy trên cùng $100$ hạt giống kiểm tra, nên phép so sánh dùng hiệu ghép cặp: hiệu của hai tổng thưởng trên từng hạt giống, lấy trung bình, kèm nửa độ rộng $1{,}96$ sai số chuẩn của các hiệu. Khoảng ở đây là $32{,}8\pm46{,}2=[-13{,}4;\,79{,}0]$, chứa $0$, nên $100$ lượt kiểm tra chưa đủ để kết luận Sarsa tốt hơn Q-learning trên tàu đổ bộ. Nếu khoảng không chứa $0$, kết luận chỉ áp dụng cho hai bảng cụ thể đã học, vì mỗi bảng phụ thuộc hạt giống huấn luyện; muốn so hai thuật toán cần lặp lại huấn luyện với nhiều hạt giống (notebook, phần 13, nhiệm vụ 1). Hai con số $26{,}2\pm14{,}0$ và $-6{,}6\pm17{,}2$ thuộc về một lần huấn luyện.

**Kiểm tra lại.** $3^6\cdot3=729\cdot3=2187$; $148^{-0{,}6}\approx0{,}0499<0{,}05<147^{-0{,}6}\approx0{,}0501$. Ba lỗi thường gặp: đặt $Y=R$ ở bước cắt ngắn; nêu GLIE như giả thiết của Định lý 06.21, trong khi Q-learning chỉ cần độ phủ; và so hai trung bình $26{,}2$ và $-6{,}6$ với hai sai số chuẩn riêng, bỏ mất tương quan giữa hai chính sách trên cùng hạt giống.
:::

## Tài liệu tham khảo

- Bài giảng gốc (2025–2026). Tạ Việt Cường, *Lecture 06: Điều khiển phi mô hình — Monte Carlo Control, SARSA, Q-Learning và tính chất hội tụ*, học phần Học tăng cường, năm học 2025–2026, trang 3–30; nguồn của dãy năm ô (trang 15–21) và của Bài tập 06.1–06.6.
- Bài tập tuần 3 (2025–2026), bài 10, các câu 1–3: nguồn của Bài tập 06.13.
- [Ghi chú bài giảng Bài 06](material-viewer.html?doc=materials/lec-06/lecture-note.md&deck=lecture-06-dieu-khien-phi-mo-hinh.html): ký hiệu, số hiệu kết quả, và đề cùng lời giải của Bài tập 06.1–06.6.
- Notebook `thuc-hanh-lunarlander-dieu-khien-phi-mo-hinh.ipynb` của Bài 06, phần 4–8, 10, 13: dữ kiện và số liệu của Bài tập 06.15–06.17 (một lần chạy đã nhúng).
- R. S. Sutton, A. G. Barto (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §5.4, tr. 100–101 (chính sách $\varepsilon$-mềm và $\varepsilon$-tham lam) cho Bài tập 06.14; §6.4–6.5, tr. 129–132 (Sarsa, Q-learning) cho Bài tập 06.4, 06.5, 06.13.
- S. Singh, T. Jaakkola, M. L. Littman, C. Szepesvári (2000), "Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms", *Machine Learning* 38, 287–308: định nghĩa GLIE và lịch thăm dò theo trạng thái, dùng ở Bài tập 06.16.
