# Bài tập Bài 08 — Deep Q-Learning

Bộ bài tập gồm mười bốn bài, phủ năm mạch nội dung 2–6 của bài học, ở ba mức: nhận biết (08.6, 08.7, 08.8); tính toán hoặc chứng minh (08.9–08.14); vận dụng vào bài toán Học tăng cường (08.15–08.19). Năm bài 08.1–08.5 của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-deep-q-learning.html) Bài 08 thuộc mục "Bài tập củng cố" của ghi chú, có gợi ý và lời giải tại đó, nên không chép lại; bảng dưới ghi chúng ở dạng "ghi chú: 08.k". Bốn bài 08.1–08.4 còn có trang đề bài và trang lời giải trên trang chiếu, và bảng dẫn tới hai trang đó. Mười bốn bài 08.6–08.19 chỉ có trong tệp này, tiếp nối bộ đếm Bài tập của ghi chú và đánh số theo thứ tự xuất hiện; không bài nào trùng một trang bài tập của trang chiếu. Học phần 2025–2026 không có phiếu bài tập tuần 8, nên dòng "Nguồn" của mỗi bài dẫn tới mục của ghi chú, trang của bài giảng gốc và giáo trình đã dùng.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-08-deep-q-learning.html#/1/1) | — |
| 2. Mạng giá trị hành động và mục tiêu hồi quy | [Mở phần](lecture-08-deep-q-learning.html#/2/1) | 08.6, 08.7, 08.9 |
| 3. Bộ nhớ phát lại | [Mở phần](lecture-08-deep-q-learning.html#/3/1) | 08.8, 08.10, 08.16 |
| 4. Hàm mất mát và thuật toán DQN | [Mở phần](lecture-08-deep-q-learning.html#/4/1) | 08.9, 08.11, 08.12, 08.15, 08.16, 08.17; [ghi chú: 08.1, 08.2 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-deep-q-learning.html); trang [Bài tập: một mini-batch](lecture-08-deep-q-learning.html#/4/5) và [trang lời giải](lecture-08-deep-q-learning.html#/4/6); trang [Bài tập: lỗi cài đặt mục tiêu DQN](lecture-08-deep-q-learning.html#/4/13) và [trang lời giải](lecture-08-deep-q-learning.html#/4/14) |
| 5. Bộ tối ưu theo gradient | [Mở phần](lecture-08-deep-q-learning.html#/5/1) | 08.8, 08.13, 08.19; [ghi chú: 08.5 (a) (Bài tập củng cố)](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-deep-q-learning.html) |
| 6. Bất ổn và phạm vi bảo đảm của DQN | [Mở phần](lecture-08-deep-q-learning.html#/6/1) | 08.8, 08.14, 08.17, 08.18, 08.19; [ghi chú: 08.3, 08.5 (b) (Bài tập củng cố)](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-deep-q-learning.html); trang [Bài tập: thí nghiệm loại bỏ](lecture-08-deep-q-learning.html#/6/6) và [trang lời giải](lecture-08-deep-q-learning.html#/6/7) |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-08-deep-q-learning.html#/7/1) | [ghi chú: 08.4 (Bài tập củng cố)](material-viewer.html?doc=materials/lec-08/lecture-note.md&deck=lecture-08-deep-q-learning.html); trang [Bài tập: một bước DQN trên CartPole](lecture-08-deep-q-learning.html#/7/6) và [trang lời giải](lecture-08-deep-q-learning.html#/7/7) |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 08. Tập hành động $\mathcal A$ hữu hạn, có $\lvert\mathcal A\rvert$ phần tử. Mạng giá trị hành động (action-value network) nhận quan sát $o\in\mathcal O$ và trả vector $\mathbf q_\theta(o)\in\mathbb R^{\lvert\mathcal A\rvert}$; giá trị của hành động $a$ là thành phần $Q_\theta(o,a)=[\mathbf q_\theta(o)]_a$. Tham số $\theta\in\mathbb R^d$ thuộc mạng trực tuyến (online network), được cập nhật bằng gradient; $\theta^-$ thuộc mạng mục tiêu (target network), cùng kiến trúc, khởi tạo $\theta^-\leftarrow\theta$ và chỉ đổi tại các mốc đồng bộ $\theta^-\leftarrow\theta$ (Định nghĩa 08.3). Hệ số chiết khấu $\gamma\in[0,1)$.

Trên dòng thời gian, mẫu chuyển (transition) là bộ sáu $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$: phần thưởng $R_{t+1}$ nhận sau $A_t$; cờ kết thúc $Z_{t+1}=1$ khi và chỉ khi MDP đang mô hình hóa kết thúc tại bước $t+1$; cờ cắt ngắn (truncation) $U_{t+1}=1$ khi việc thu thập dừng vì một giới hạn không thuộc động lực của MDP (Định nghĩa 08.4, 08.6). Môi trường được đặt lại khi $Z_{t+1}\lor U_{t+1}=1$. Sau khi rút một mini-batch $b$ mẫu từ bộ nhớ phát lại (experience replay) $\mathcal D$ dung lượng $N$, mẫu thứ $i$ viết $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\dots,b$; chỉ số $i$ không mang thứ tự thời gian. Mục tiêu hồi quy (regression target), dự đoán và sai số TD của mẫu $i$ là

$$
\begin{aligned}
y_i&=R_i+\gamma(1-Z_i)\max_{a'\in\mathcal A}Q_{\theta^-}(O'_i,a'),\\
q_i&=Q_\theta(O_i,A_i),\\
\delta_i&=y_i-q_i .
\end{aligned}
$$

Thừa số $1-Z_i$ là mặt nạ kết thúc; cờ $U_i$ không vào mục tiêu. Hàm mất mát (loss) sai số bình phương trung bình (mean squared error, MSE) là $L_B(\theta)=\tfrac1b\sum_{i=1}^b(\operatorname{sg}(y_i)-q_i)^2$, với $\operatorname{sg}$ là phép dừng gradient (stop-gradient) và $q_i$ lấy bằng phép chọn theo hành động (gather) (Định nghĩa 08.10, 08.12); khi đó $\partial L_B/\partial q_i=\tfrac2b(q_i-y_i)$.

Ba chỉ số đếm ba thứ khác nhau: $t$ đếm bước môi trường, $k_{\mathrm{opt}}$ đếm bước tối ưu, $j$ là chỉ số bước trong công thức của bộ tối ưu, $j=k_{\mathrm{opt}}$ sau khi tăng. Thuật toán 08.13 dùng năm số nguyên dương $N$, $b$, $N_{\mathrm{start}}$ (số mẫu tối thiểu trong $\mathcal D$ trước bước tối ưu đầu), $F$ (số bước môi trường giữa hai bước tối ưu), $C$ (số bước tối ưu giữa hai lần đồng bộ), với $b\le N_{\mathrm{start}}\le N$; bước tối ưu chạy khi $\lvert\mathcal D\rvert\ge N_{\mathrm{start}}$ và $t\bmod F=0$, sau khi $t$ đã tăng; sau mỗi cập nhật, $k_{\mathrm{opt}}$ tăng rồi mới kiểm $k_{\mathrm{opt}}\bmod C=0$. Xác suất thăm dò (exploration) của hành vi $\epsilon_{\mathrm{exp}}$-tham lam viết $\epsilon_{\mathrm{exp}}$; hằng ổn định trong mẫu số của RMSprop và Adam viết $\epsilon_{\mathrm{opt}}$; tốc độ học của bộ tối ưu (optimizer) viết $\eta$. Mọi phép bình phương, căn và chia của RMSprop, Adam lấy theo từng tọa độ, ký hiệu $\odot$, $\oslash$ (Định nghĩa 08.16–08.18).

Thuật ngữ và chữ viết tắt dùng trong tệp: mạng Q sâu (Deep Q-Network, DQN); sai phân thời gian (temporal difference, TD); lượt (episode); lợi tức (return); hạ gradient ngẫu nhiên (stochastic gradient descent, SGD); hiệu chỉnh lệch (bias correction); bộ đệm vòng (ring buffer); tự đặt lại (autoreset); học khác chính sách (off-policy); tỉ số lấy mẫu quan trọng (importance sampling ratio); bộ ba bất ổn (deadly triad); thí nghiệm loại bỏ (ablation); lan truyền kích thước (broadcasting); cỡ mẫu hiệu dụng (effective sample size); hạt giống ngẫu nhiên (seed); sai số chuẩn (standard error, SE); quá trình quyết định Markov (Markov decision process, MDP).

Ba môi trường xuất hiện ở các bài vận dụng; bài nào dùng chúng đều nêu lại dữ kiện trong khối đề bài.

- **CartPole-v1** (ghi chú Bài 08, Tình huống 08.1 và Bài tập 08.4). Quan sát gồm $4$ biến: vị trí, vận tốc của xe, góc và vận tốc góc của cột; $2$ hành động; phần thưởng $+1$ ở mỗi bước. $Z=1$ khi góc của cột vượt $12^\circ$ hoặc vị trí của xe vượt $2{,}4$ về một phía; $U=1$ khi lượt đạt $500$ bước.
- **Lunar Lander** (ghi chú Bài 07, Ví dụ 07.1 và Bài tập 07.20; ghi chú Bài 08, Ví dụ 08.1). Quan sát gồm $8$ thành phần: sáu biến liên tục và hai cờ chân chạm đất; $4$ hành động.
- **Flappy Bird** (ghi chú Bài 07, Mục 1; Bài tập 07.20). Quan sát gồm $12$ biến liên tục; $2$ hành động.

Mọi bộ số không ghi nguồn là số liệu sư phạm tự xây dựng; các "nhật ký huấn luyện" trong bài vận dụng là số liệu tự xây dựng, không phải kết quả của một lần chạy. Số thập phân viết với dấu phẩy. Lời giải nêu kết quả được dùng ở từng bước; số hiệu "Định nghĩa 08.k", "Nhận xét 08.k", "Mệnh đề 08.k", "Thuật toán 08.k", "Ví dụ 08.k" chỉ khối của ghi chú bài giảng Bài 08.

## Mức nhận biết

### Bài tập 08.6. Đọc vector giá trị hành động

**Mức độ:** nhận biết. Mục tiêu học tập 1 của ghi chú: đọc $\mathbf q_\theta(o)$, chọn giá trị của hành động đã thực hiện và tính mục tiêu của một mẫu chuyển.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 2 (Định nghĩa 08.1, Ví dụ 08.3, Định nghĩa 08.4); bài giảng gốc (2025–2026), trang 14–17; Mnih và cộng sự (2015), mục Methods (chi phí khi mạng nhận cặp quan sát–hành động); số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.6 (Đọc vector giá trị hành động)
Tập hành động $\mathcal A=\{a_1,a_2,a_3\}$. Tại ba quan sát, mạng trực tuyến trả về

$$
\begin{aligned}
\mathbf q_\theta(o_1)&=(1{,}2;\,-0{,}4;\,0{,}7),\\
\mathbf q_\theta(o_2)&=(2{,}0;\,2{,}0;\,-1{,}0),\\
\mathbf q_\theta(o_3)&=(-0{,}6;\,-0{,}2;\,-1{,}1).
\end{aligned}
$$

Hành vi là $\epsilon_{\mathrm{exp}}$-tham lam với $\epsilon_{\mathrm{exp}}=0{,}3$: với xác suất $\epsilon_{\mathrm{exp}}$ chọn đều một hành động trong $\mathcal A$, ngược lại chọn một hành động trong $\mathcal G_\theta(o)=\arg\max_aQ_\theta(o,a)$, phá hòa chia đều.

- (a) Với mỗi quan sát, xác định $\max_aQ_\theta(o,a)$, $\mathcal G_\theta(o)$ và xác suất hành vi chọn từng hành động.
- (b) Một mẫu chuyển có $O_t=o_1$, $A_t=a_3$, $R_{t+1}=1$, $O_{t+1}=o_3$, $Z_{t+1}=0$; $\gamma=0{,}9$; mẫu được dùng ngay sau một mốc đồng bộ, nên $\theta^-=\theta$. Tính $q_t=Q_\theta(O_t,A_t)$, mục tiêu $y_t$ và sai số $\delta_t=y_t-q_t$. Tính lại $\delta_t$ khi một bản cài đặt dùng $\max_aQ_\theta(O_t,a)$ thay cho giá trị của $A_t$.
- (c) Xét một môi trường khác, có $\lvert\mathcal A\rvert=18$ (như Atari). Một bước tối ưu dùng mini-batch $b=32$ mẫu. Đếm số lần đánh giá mạng trên một đầu vào cần để có mọi $q_i$ và mọi $\max_{a'}Q_{\theta^-}(O'_i,a')$, trong hai trường hợp: mạng theo Định nghĩa 08.1; mạng nhận cặp $(o,a)$ làm đầu vào và trả một số. Đếm tương tự cho một lần chọn hành động tham lam.
:::

::: hint Gợi ý Bài tập 08.6
$Q_\theta(o,a)$ là thành phần thứ $a$ của vector đầu ra (Định nghĩa 08.1). Khi $\mathcal G_\theta(o)$ có $\lvert\mathcal G\rvert$ phần tử, mỗi hành động tham lam có xác suất $\epsilon_{\mathrm{exp}}/\lvert\mathcal A\rvert+(1-\epsilon_{\mathrm{exp}})/\lvert\mathcal G\rvert$. Dự đoán dùng hành động đã lưu tại $O_t$; phép cực đại chỉ dùng tại $O_{t+1}$.
:::

::: solution Lời giải Bài tập 08.6
**Câu (a).** Mỗi hành động nhận phần thăm dò $0{,}3/3=0{,}1$; phần $0{,}7$ còn lại chia đều trên $\mathcal G_\theta(o)$.

| quan sát | $\max_aQ_\theta(o,a)$ | $\mathcal G_\theta(o)$ | xác suất $(a_1,a_2,a_3)$ |
| --- | --- | --- | --- |
| $o_1$ | $1{,}2$ | $\{a_1\}$ | $(0{,}8;\,0{,}1;\,0{,}1)$ |
| $o_2$ | $2{,}0$ | $\{a_1,a_2\}$ | $(0{,}45;\,0{,}45;\,0{,}1)$ |
| $o_3$ | $-0{,}2$ | $\{a_2\}$ | $(0{,}1;\,0{,}8;\,0{,}1)$ |

Tại $o_2$, hai hành động hòa nên mỗi hành động nhận $0{,}1+0{,}7/2=0{,}45$. Tại $o_3$, mọi giá trị âm và giá trị lớn nhất là $-0{,}2$ của $a_2$. Mỗi hàng có tổng bằng $1$.

**Câu (b).** Theo phép chọn theo hành động, $q_t=[\mathbf q_\theta(o_1)]_{a_3}=0{,}7$. Vì $\theta^-=\theta$, $\max_{a'}Q_{\theta^-}(o_3,a')=-0{,}2$. Theo Định nghĩa 08.4,

$$
\begin{aligned}
y_t&=1+0{,}9\cdot(1-0)\cdot(-0{,}2)\\
&=0{,}82,\\
\delta_t&=0{,}82-0{,}7=0{,}12 .
\end{aligned}
$$

Dùng $\max_aQ_\theta(o_1,a)=1{,}2$ thay cho $q_t$ cho $\delta_t=0{,}82-1{,}2=-0{,}38$: sai số đổi dấu, và bước cập nhật kéo giá trị của $a_1$ xuống về một mục tiêu sinh từ hành động $a_3$.

**Câu (c).** Với mạng theo Định nghĩa 08.1, một lần đánh giá trên $O_i$ cho cả $18$ giá trị, nên cần $32$ lần cho các $q_i$ (mạng trực tuyến trên $O_i$) và $32$ lần cho các giá trị cực đại (mạng mục tiêu trên $O'_i$), tổng $64$. Với mạng nhận cặp $(o,a)$, mỗi $q_i$ cần một lần, còn mỗi giá trị cực đại cần $18$ lần, nên tổng là $32+32\cdot18=608$, khoảng $9{,}5$ lần nhiều hơn. Chọn hành động tham lam cần $1$ lần với mạng theo Định nghĩa 08.1 và $18$ lần với mạng nhận cặp. Chi phí của kiến trúc thứ hai tăng tuyến tính theo $\lvert\mathcal A\rvert$, lý do Mnih và cộng sự (2015) dùng kiến trúc trả vector.

**Kiểm tra lại.** Tổng xác suất ở mỗi quan sát bằng $1$. Ba lỗi thường gặp: cho mỗi hành động hòa xác suất $1-\epsilon_{\mathrm{exp}}+\epsilon_{\mathrm{exp}}/3=0{,}8$, làm tổng tại $o_2$ bằng $1{,}7$; chọn hành động tham lam tại $o_3$ theo trị tuyệt đối, được $a_3$; dùng giá trị lớn nhất tại $O_t$ làm dự đoán, cho $\delta_t=-0{,}38$ thay cho $0{,}12$.
:::

### Bài tập 08.7. Cờ kết thúc và cờ cắt ngắn trong sáu tình huống

**Mức độ:** nhận biết. Mục tiêu học tập 1 của ghi chú: phân biệt mẫu kết thúc với mẫu bị cắt ngắn.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 2 (Định nghĩa 08.4, 08.6, Ví dụ 08.7, 08.8, đoạn về giới hạn số bước thuộc nhiệm vụ, Nhận xét 08.2); Pardo và cộng sự (2018); bài giảng gốc (2025–2026), trang 21; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.7 (Cờ kết thúc và cờ cắt ngắn trong sáu tình huống)
Mỗi tình huống dưới đây mô tả bước cuối của một lượt, với mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$.

1. Lunar Lander: tàu va chạm với mặt đất và lượt kết thúc theo luật của môi trường.
2. Lunar Lander: cấu hình thu thập dừng lượt sau $1\,000$ bước khi tàu vẫn đang bay; giới hạn này không thuộc động lực của MDP.
3. Flappy Bird: chim chạm ống và lượt kết thúc theo luật của trò chơi.
4. Flappy Bird: người thu thập dừng mọi lượt đạt $10\,000$ bước để giới hạn thời gian huấn luyện.
5. CartPole: ở bước thứ $500$ của lượt, góc của cột cũng vượt $12^\circ$.
6. Nhiệm vụ "hạ cánh trong $200$ bước": hết $200$ bước mà chưa hạ cánh là thất bại theo định nghĩa của nhiệm vụ, và số bước còn lại là một thành phần của quan sát.

- (a) Với mỗi tình huống, xác định $Z_{t+1}$, $U_{t+1}$, môi trường có được đặt lại không, giá trị mặt nạ $1-Z_{t+1}$ và dạng của mục tiêu $y_t$.
- (b) Trong tình huống 2, $R_{t+1}=-0{,}3$, $\gamma=0{,}99$ và $\max_{a'}Q_{\theta^-}(O_{t+1},a')=42$. Tính $y_t$, và tính lại khi một bản cài đặt dùng mặt nạ $1-(Z_{t+1}\lor U_{t+1})$.
- (c) Trong tình huống 6, giả sử số bước còn lại không có trong quan sát. Xác định giả thiết nào của ghi chú không còn thỏa.
:::

::: hint Gợi ý Bài tập 08.7
$Z_{t+1}$ chỉ ghi kết thúc của chính MDP; $U_{t+1}$ ghi việc dừng vì một giới hạn bên ngoài. Đặt lại khi $Z_{t+1}\lor U_{t+1}=1$, còn mục tiêu chỉ dùng $1-Z_{t+1}$ (Định nghĩa 08.6). Một giới hạn thuộc nhiệm vụ, với thời gian còn lại quan sát được, là kết thúc của MDP.
:::

::: solution Lời giải Bài tập 08.7
**Câu (a).**

| tình huống | $Z_{t+1}$ | $U_{t+1}$ | đặt lại | $1-Z_{t+1}$ | $y_t$ |
| --- | --- | --- | --- | --- | --- |
| 1 | $1$ | $0$ | có | $0$ | $R_{t+1}$ |
| 2 | $0$ | $1$ | có | $1$ | $R_{t+1}+\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$ |
| 3 | $1$ | $0$ | có | $0$ | $R_{t+1}$ |
| 4 | $0$ | $1$ | có | $1$ | $R_{t+1}+\gamma\max_{a'}Q_{\theta^-}(O_{t+1},a')$ |
| 5 | $1$ | $1$ | có | $0$ | $R_{t+1}$ |
| 6 | $1$ | $0$ | có | $0$ | $R_{t+1}$ |

Tình huống 1 và 3 là kết thúc theo luật của MDP. Tình huống 2 và 4 dừng vì giới hạn của việc thu thập; nếu đi tiếp từ $O_{t+1}$ thì tác tử vẫn nhận phần thưởng, nên mục tiêu giữ phần bootstrap (Định nghĩa 08.6). Ở tình huống 5, hai cờ cùng bằng $1$; mặt nạ chỉ đọc $Z_{t+1}=1$, nên phần bootstrap bị xóa, đúng vì MDP đã kết thúc. Ở tình huống 6, giới hạn là một phần của nhiệm vụ và thời gian còn lại nằm trong quan sát, nên hết giờ là kết thúc thật của MDP (ghi chú, Mục 2, đoạn sau Ví dụ 08.8).

**Câu (b).** Với $1-Z_{t+1}=1$: $y_t=-0{,}3+0{,}99\cdot42=41{,}28$. Với mặt nạ gộp, $1-(0\lor1)=0$ và $y_t=-0{,}3$: mục tiêu bị hạ $41{,}58$, như thể tàu dừng hẳn ở bước $1\,000$ (Ví dụ 08.8 cho cùng hiện tượng với độ hạ $3{,}6$).

**Câu (c).** Giả thiết Markov của Nhận xét 08.2 không thỏa. Hai quan sát giống nhau có thể ứng với hai số bước còn lại khác nhau, nên có tương lai khác nhau; phân phối của $(R_{t+1},O_{t+1},Z_{t+1})$ khi biết $(O_t,A_t)$ còn phụ thuộc phần lịch sử đã đếm số bước (Pardo và cộng sự, 2018).

**Kiểm tra lại.** Ở mỗi hàng, cột "đặt lại" ứng với $Z\lor U=1$, còn mặt nạ chỉ phụ thuộc $Z$. Ba lỗi thường gặp: đặt $Z_{t+1}=1$ ở tình huống 2 và 4 vì "lượt đã dừng"; ở tình huống 5, giữ phần bootstrap vì có $U_{t+1}=1$; ở tình huống 6, coi hết giờ là cắt ngắn và bootstrap qua mốc $200$ bước.
:::

### Bài tập 08.8. Phát biểu đúng và sai về bộ nhớ phát lại, mạng mục tiêu và bộ tối ưu

**Mức độ:** nhận biết. Mục tiêu học tập 2, 4 và 5 của ghi chú: phát biểu đúng phạm vi của từng cơ chế.

**Nguồn:** bài giảng gốc (2025–2026), trang 28, 32, 33 và câu hỏi thảo luận 1, 2 ở trang 36; ghi chú bài giảng Bài 08, Mục 3 (Mệnh đề 08.8, Nhận xét 08.9), Mục 5 (Định nghĩa 08.15), Mục 6 (Nhận xét 08.19, 08.20, 08.21); ghi chú bài giảng Bài 07, Nhận xét 07.39.

::: exercise Bài tập 08.8 (Phát biểu đúng và sai về bộ nhớ phát lại, mạng mục tiêu và bộ tối ưu)
Xét DQN theo Thuật toán 08.13: mạng trực tuyến $Q_\theta$, mạng mục tiêu $Q_{\theta^-}$ đồng bộ sau mỗi $C$ bước tối ưu, bộ nhớ phát lại $\mathcal D$ dung lượng $N$ do hành vi $\epsilon_{\mathrm{exp}}$-tham lam ghi, mini-batch $b$ mẫu rút đều, mục tiêu một bước $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$. Với mỗi phát biểu, xác định đúng hay sai và nêu kết quả của ghi chú làm căn cứ; viết lại mỗi phát biểu sai thành một phát biểu đúng.

1. Bộ nhớ phát lại phá vỡ hoàn toàn tương quan theo thời gian giữa các mẫu của một mini-batch.
2. Khi đã biết nội dung của $\mathcal D$, các lần rút đều có hoàn lại độc lập và cùng phân phối theo phân phối thực nghiệm của $\mathcal D$.
3. Một mẫu do hành vi theo một phiên bản $\theta$ cũ sinh ra phải được nhân với tỉ số lấy mẫu quan trọng trong mục tiêu một bước.
4. Mạng mục tiêu giảm tương quan giữa các mẫu trong một mini-batch.
5. Giữa hai mốc đồng bộ, mục tiêu của mỗi mẫu đã lưu trong $\mathcal D$ là một hằng số.
6. Tại một mốc đồng bộ, mục tiêu của một mẫu bị cắt ngắn ($U_i=1$, $Z_i=0$) không đổi.
7. Thay RMSprop bằng Adam loại yếu tố bootstrap khỏi DQN, nên DQN dùng Adam có bảo đảm hội tụ.
8. Vì DQN không có bảo đảm hội tụ tổng quát, mọi lần chạy DQN có lợi tức đánh giá thấp là một lần chạy phân kỳ.
:::

::: hint Gợi ý Bài tập 08.8
Với mỗi phát biểu, xác định cơ chế đổi thành phần nào của bước cập nhật: cách chọn mẫu (bộ nhớ phát lại), tham số dùng trong mục tiêu (mạng mục tiêu) hay cách đổi gradient thành bước tham số (bộ tối ưu). Nhận xét 08.19 ghép mỗi nguồn bất ổn với một cơ chế; Nhận xét 08.21 nói về ba yếu tố của bộ ba bất ổn.
:::

::: solution Lời giải Bài tập 08.8
1. **Sai.** Bộ nhớ phát lại giảm tương quan ngắn hạn: hai lần rút độc lập trúng hai mẫu liền nhau với xác suất $2(N-1)/N^2\approx2/N>0$, hai mẫu liên tiếp của một lượt dùng chung một quan sát, và nội dung của $\mathcal D$ là các đoạn quỹ đạo của chính tác tử (Nhận xét 08.9, điều 1). Phát biểu đúng: bộ nhớ phát lại làm hiếm các cặp liền nhau trong mini-batch, nhưng không loại hết tương quan. Bài giảng gốc (trang 32) viết "phá vỡ tương quan"; ghi chú thay bằng "giảm".
2. **Đúng.** Đây là phần đầu của Nhận xét 08.9, điều 1. Khi $\mathcal D$ thay đổi theo hành vi (điều 2), phân phối thực nghiệm đó không cố định qua các bước tối ưu.
3. **Sai.** Theo Mệnh đề 08.8, khi quan sát đủ Markov, động lực không đổi theo thời gian và $\theta^-$ cố định, $\mathbb E[y_i\mid O_i,A_i]=(\mathcal TQ_{\theta^-})(O_i,A_i)$ bất kể phiên bản hành vi đã sinh mẫu, vì $A_i$ là đối số điều kiện và phép cực đại tại $O'_i$ được tính trọn. Phát biểu đúng: mục tiêu một bước không cần tỉ số lấy mẫu quan trọng dưới ba giả thiết đó; mục tiêu nhiều bước thì cần.
4. **Sai.** Mini-batch do cách rút từ $\mathcal D$ quyết định; mạng mục tiêu chỉ đổi tham số dùng trong mục tiêu (Nhận xét 08.19). Phát biểu đúng: mạng mục tiêu làm mục tiêu đứng yên giữa hai mốc đồng bộ; tương quan do bộ nhớ phát lại giảm.
5. **Đúng.** Giữa hai mốc, $\theta^-$ là hằng và $R_i$, $Z_i$, $O'_i$ đã lưu, nên $y_i$ cố định (Định nghĩa 08.3, Nhận xét 08.20).
6. **Sai.** Theo Nhận xét 08.20, $\Delta y_i=\gamma(1-Z_i)\bigl[\max_{a'}Q_\theta(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\bigr]$ không chứa $U_i$; với $Z_i=0$, mẫu bị cắt ngắn vẫn bootstrap và đổi mục tiêu tại mốc. Phát biểu đúng: chỉ mẫu kết thúc, $Z_i=1$, giữ mục tiêu tại mốc đồng bộ.
7. **Sai.** Theo Định nghĩa 08.15, bộ tối ưu chỉ nhận gradient và trạng thái phụ; công thức mục tiêu, cách thu thập và lớp hàm không đổi, nên ba yếu tố của bộ ba bất ổn còn nguyên và không có bảo đảm hội tụ tổng quát (Nhận xét 08.21). Phát biểu đúng: Adam đổi quỹ đạo của $\theta$, không đổi mục tiêu bootstrap. Bài giảng gốc (trang 28) nêu cùng giới hạn.
8. **Sai.** Nhận xét 08.21 nói về bảo đảm cho mọi bài toán, kiến trúc và siêu tham số, không dự báo một lần chạy (Điều kiện áp dụng; Nhận xét 07.39 của Bài 07). Lợi tức thấp với giá trị và tham số bị chặn là một chính sách kém, khác dấu hiệu phân kỳ, tức $Q_\theta$ hoặc $\lVert\theta\rVert$ tăng không chặn qua các lần đánh giá. Phát biểu đúng: DQN có thể phân kỳ trên một số bài toán; một lần chạy cụ thể cần được chẩn đoán bằng độ lớn của giá trị và tham số.

**Kiểm tra lại.** Mỗi phát biểu sai ở trên gán cho một cơ chế tác dụng của cơ chế khác hoặc một bảo đảm không có. Ba lỗi thường gặp: coi xác suất $2/N$ rất nhỏ là bằng $0$; nhớ "mặt nạ" thành $1-(Z\lor U)$ khi xét $\Delta y_i$; đọc "không có bảo đảm hội tụ" thành "phân kỳ".
:::

## Mức tính toán hoặc chứng minh

### Bài tập 08.9. Mục tiêu có mặt nạ trên một mini-batch bốn mẫu

**Mức độ:** tính toán. Mục tiêu học tập 1, 3 và 6 của ghi chú: tính mục tiêu, hàm mất mát và đạo hàm theo dự đoán trên một mini-batch có cả mẫu kết thúc lẫn mẫu bị cắt ngắn.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 2 (Định nghĩa 08.4, 08.6, Ví dụ 08.7, 08.8) và Mục 4 (Định nghĩa 08.10); mở rộng Bài tập 08.1 của ghi chú sang $b=4$ và một mẫu có cả hai cờ; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.9 (Mục tiêu có mặt nạ trên một mini-batch bốn mẫu)
Cho $b=4$, $\gamma=0{,}99$ và mini-batch bốn mẫu chuyển, với $q_i=Q_\theta(O_i,A_i)$:

| $i$ | $R_i$ | $Z_i$ | $U_i$ | $\max_{a'}Q_{\theta^-}(O'_i,a')$ | $q_i$ |
| --- | --- | --- | --- | --- | --- |
| 1 | $0{,}5$ | $0$ | $0$ | $20$ | $19$ |
| 2 | $-1$ | $0$ | $1$ | $30$ | $28$ |
| 3 | $10$ | $1$ | $0$ | $50$ | $12$ |
| 4 | $2$ | $1$ | $1$ | $40$ | $3$ |

- (a) Tính $y_i$, $\delta_i=y_i-q_i$, hàm mất mát $L_B=\tfrac1b\sum_i\delta_i^2$ và $\partial L_B/\partial q_i$ với $i=1,\dots,4$.
- (b) Tính lại $y_i$, $L_B$ và $\partial L_B/\partial q_i$ cho hai bản cài đặt sai: bản bỏ mặt nạ (coi mọi $Z_i=0$) và bản dùng mặt nạ $1-(Z_i\lor U_i)$. Với mỗi bản, chỉ ra mẫu nào đổi mục tiêu.
- (c) Một bản cài đặt dùng tổng $\sum_i\delta_i^2$ thay cho trung bình. Tính giá trị hàm mất mát và đạo hàm theo $q_i$, nêu hệ số chênh so với (a), và nêu hệ quả cho bước tham số khi bộ tối ưu là SGD và khi là RMSprop hoặc Adam.
- (d) Xác định các mẫu có mục tiêu không phụ thuộc $\theta^-$, và suy ra độ thay đổi mục tiêu của chúng tại một mốc đồng bộ.
:::

::: hint Gợi ý Bài tập 08.9
Áp mặt nạ $1-Z_i$ trước khi tính sai số; cờ $U_i$ không vào mục tiêu (Định nghĩa 08.6). Với $b=4$, $\partial L_B/\partial q_i=\tfrac24(q_i-y_i)=\tfrac12(q_i-y_i)$, nên hệ số $\tfrac2b$ không còn bằng $1$ như ở Bài tập 08.1.
:::

::: solution Lời giải Bài tập 08.9
**Câu (a).** Mẫu 1 và mẫu 2 có $Z_i=0$ nên giữ phần bootstrap; mẫu 2 bị cắt ngắn nhưng $U_2$ không vào mục tiêu. Mẫu 3 và mẫu 4 có $Z_i=1$ nên $y_i=R_i$; ở mẫu 4, cờ $U_4=1$ không đổi kết luận vì mặt nạ chỉ đọc $Z_4$.

$$
\begin{aligned}
y_1&=0{,}5+0{,}99\cdot20=20{,}3,\\
y_2&=-1+0{,}99\cdot30=28{,}7,\\
y_3&=10,\\
y_4&=2.
\end{aligned}
$$

Sai số là $\delta=(1{,}3;\,0{,}7;\,-2;\,-1)$, nên

$$
\begin{aligned}
L_B&=\tfrac14\bigl(1{,}69+0{,}49+4+1\bigr)\\
&=\tfrac{7{,}18}4=1{,}795 .
\end{aligned}
$$

Theo Định nghĩa 08.10, $\partial L_B/\partial q_i=\tfrac12(q_i-y_i)=-\tfrac12\delta_i$, tức $(-0{,}65;\,-0{,}35;\,1;\,0{,}5)$. Xét các $q_i$ như bốn biến riêng, một bước hạ gradient nhỏ tăng $q_1$, $q_2$ và giảm $q_3$, $q_4$.

**Câu (b).** Bỏ mặt nạ chỉ đổi hai mẫu kết thúc: $y_3=10+0{,}99\cdot50=59{,}5$, $y_4=2+0{,}99\cdot40=41{,}6$, nên $\delta=(1{,}3;\,0{,}7;\,47{,}5;\,38{,}6)$, $L_B=3\,748{,}39/4=937{,}0975$ và đạo hàm $(-0{,}65;\,-0{,}35;\,-23{,}75;\,-19{,}3)$. Hai mẫu 3, 4 đổi dấu đạo hàm và bị kéo lên về các giá trị không ứng với phần thưởng nào (Ví dụ 08.7).

Mặt nạ gộp chỉ đổi mẫu bị cắt ngắn còn chưa kết thúc: $y_2=-1$, $\delta_2=-29$, nên $L_B=(1{,}69+841+4+1)/4=211{,}9225$ và $\partial L_B/\partial q_2=14{,}5$. Mẫu 4 không đổi, vì với $Z_4=1$ hai mặt nạ cùng bằng $0$.

**Câu (c).** Tổng cho $\sum_i\delta_i^2=7{,}18$ và đạo hàm $2(q_i-y_i)$, tức $(-2{,}6;\,-1{,}4;\,4;\,2)$: cả hai lớn gấp $b=4$ lần so với (a), nên gradient theo $\theta$ cũng lớn gấp bốn lần. Với SGD, bước $-\eta g_j$ lớn gấp bốn lần, nên tốc độ học phải nhỏ đi bốn lần để giữ cùng bước tham số. Với RMSprop và Adam, khi mọi $g_\ell$, $\ell\le j$, đều nhân $4$ (cài đặt dùng tổng ngay từ đầu), $m_j$ nhân $4$ và $v_j$ nhân $16$, tức $\sqrt{v_j}$ nhân $4$; vì vậy tỉ số theo từng tọa độ $g_j\oslash(\sqrt{v_j}+\epsilon_{\mathrm{opt}})$ hoặc $\hat m_j\oslash(\sqrt{\hat v_j}+\epsilon_{\mathrm{opt}})$ chỉ đổi qua hằng $\epsilon_{\mathrm{opt}}$ nhỏ (Định nghĩa 08.17, 08.18), và bước tham số gần như giữ nguyên với cùng $\eta$.

**Câu (d).** Mẫu 3 và mẫu 4 có $Z_i=1$, nên $y_i=R_i$ không chứa $\theta^-$. Theo Nhận xét 08.20, $\Delta y_i=\gamma(1-Z_i)[\cdots]=0$: hai mẫu này giữ mục tiêu qua mọi mốc đồng bộ. Mẫu 2 bị cắt ngắn vẫn đổi mục tiêu tại mốc, như mẫu 1.

**Kiểm tra lại.** Với hai mẫu kết thúc, $y_i=R_i$ đọc thẳng từ bảng; với hai mẫu còn lại, $y_i-R_i=0{,}99\max_{a'}Q_{\theta^-}(O'_i,a')$. Ba lỗi thường gặp: coi mẫu 4 là mẫu bị cắt ngắn vì $U_4=1$ và giữ phần bootstrap, cho $y_4=41{,}6$; giữ hệ số $\tfrac2b=1$ của Bài tập 08.1, cho đạo hàm $(-1{,}3;\,-0{,}7;\,2;\,1)$; dùng mặt nạ gộp và coi mẫu 2 là mẫu kết thúc.
:::

### Bài tập 08.10. Bộ đệm vòng, cặp mẫu liền nhau và cỡ mẫu hiệu dụng

**Mức độ:** tính toán ở câu (a)–(c); chứng minh ở câu (d). Mục tiêu học tập 2 của ghi chú: tính xác suất hai mẫu liền nhau cùng vào một mini-batch và đo tác dụng của tương quan lên phương sai.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 3 (Định nghĩa 08.7, Ví dụ 08.9, 08.10, 08.12, Nhận xét 08.9); bài giảng gốc (2025–2026), trang 19, 30, 32; Mnih và cộng sự (2015), Extended Data Table 1 ($N=10^6$, $b=32$); số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.10 (Bộ đệm vòng, cặp mẫu liền nhau và cỡ mẫu hiệu dụng)
Bộ nhớ phát lại là một bộ đệm vòng (Định nghĩa 08.7) gồm $N=5$ vị trí đánh số $1,\dots,5$. Các mẫu chuyển được đánh số $1,2,\dots$ theo thứ tự thu thập, và mẫu thứ $k$ được ghi vào vị trí $((k-1)\bmod N)+1$. Hai mẫu gọi là liền nhau khi số thứ tự thu thập của chúng hơn kém nhau $1$.

- (a) Sau $12$ lần ghi, xác định mẫu nằm ở mỗi vị trí, vị trí của con trỏ ghi và mẫu sẽ bị mẫu $13$ ghi đè.
- (b) Với $b=2$, tính xác suất hai mẫu của mini-batch liền nhau khi rút không hoàn lại và khi rút có hoàn lại (hai lần rút đều, độc lập); với rút có hoàn lại, tính thêm xác suất hai lần rút trúng cùng một mẫu. So kết quả với $2/N$ và $2(N-1)/N^2$.
- (c) Với $b=3$ và rút không hoàn lại, tính xác suất mini-batch chứa ít nhất một cặp liền nhau. Cho biết số tập con $b$ phần tử của $\{1,\dots,N\}$ không chứa hai số liền nhau là $\binom{N-b+1}{b}$; tính xác suất tương ứng khi $N=10^6$, $b=32$, làm tròn tới ba chữ số có nghĩa, và so với $b(b-1)/N$.
- (d) Gọi $g_1,\dots,g_b$ là một tọa độ của gradient mẫu trên $b$ mẫu chuyển liền nhau, mỗi $g_k$ có phương sai $\sigma^2>0$ và hệ số tương quan giữa $g_k$, $g_l$ bằng $c^{\lvert k-l\rvert}$ với $0\le c<1$. Với $\bar g=\tfrac1b\sum_kg_k$, chứng minh
$$
\operatorname{Var}\bar g=\frac{\sigma^2}{b^2}\Bigl(b+2\sum_{m=1}^{b-1}(b-m)c^m\Bigr),
$$
và suy ra cỡ mẫu hiệu dụng $n_{\mathrm{eff}}=\sigma^2/\operatorname{Var}\bar g$ bằng $2/(1+c)$ khi $b=2$. Tính $n_{\mathrm{eff}}$ cho $(b,c)=(4;\,0{,}9)$, $(4;\,0{,}5)$ và $(32;\,0{,}9)$.
:::

::: hint Gợi ý Bài tập 08.10
Với (a), ghi lần lượt các mẫu $1,\dots,12$ vào vị trí theo công thức; con trỏ ghi chỉ vị trí của mẫu kế tiếp. Với (b), liệt kê $\binom52=10$ cặp không thứ tự hoặc $25$ cặp có thứ tự. Với (d), khai triển $\operatorname{Var}\sum_kg_k=\sum_k\sum_l\operatorname{Cov}(g_k,g_l)$ và đếm số cặp $(k,l)$ có $\lvert k-l\rvert=m$.
:::

::: solution Lời giải Bài tập 08.10
**Câu (a).** Mẫu $8$, $9$, $10$ vào vị trí $3$, $4$, $5$; mẫu $11$ vào vị trí $((11-1)\bmod5)+1=1$ và mẫu $12$ vào vị trí $2$. Sau $12$ lần ghi, các vị trí $1,\dots,5$ chứa mẫu $11,12,8,9,10$, tức $5$ mẫu gần nhất. Mẫu $13$ vào vị trí $((13-1)\bmod5)+1=3$, nên con trỏ ghi ở vị trí $3$ và mẫu $13$ ghi đè mẫu $8$, mẫu cũ nhất (Định nghĩa 08.7, quy tắc ghi).

**Câu (b).** Năm mẫu $8,\dots,12$ có bốn cặp liền nhau $(8,9)$, $(9,10)$, $(10,11)$, $(11,12)$; cặp $(10,11)$ nằm ở vị trí $5$ và $1$ nhưng vẫn liền nhau theo thời gian. Rút không hoàn lại cho $10$ cặp đồng khả năng, nên xác suất là $4/10=0{,}4=2/N$ (Ví dụ 08.12). Rút có hoàn lại cho $25$ cặp có thứ tự đồng khả năng, trong đó $2\cdot4=8$ cặp liền nhau, nên xác suất là $8/25=0{,}32=2(N-1)/N^2$; xác suất trúng cùng một mẫu là $5/25=0{,}2=1/N$ (Nhận xét 08.9).

**Câu (c).** Trong $\binom53=10$ bộ ba, chỉ bộ $\{8,10,12\}$ không có cặp liền nhau, khớp với $\binom{5-3+1}{3}=1$. Xác suất có ít nhất một cặp liền nhau là $9/10$: với $N=5$, gần như mọi mini-batch ba mẫu chứa hai mẫu liền nhau, nên $N$ phải lớn hơn nhiều so với $b$. Với $N=10^6$, $b=32$,

$$
\begin{aligned}
1-\frac{\binom{N-31}{32}}{\binom{N}{32}}&\approx9{,}92\cdot10^{-4},\\
\frac{b(b-1)}N&=\frac{992}{10^6}=9{,}92\cdot10^{-4}.
\end{aligned}
$$

Hai số trùng nhau tới ba chữ số có nghĩa: trong khoảng một nghìn mini-batch, khoảng một mini-batch chứa một cặp liền nhau.

**Câu (d).** Theo tính song tuyến của hiệp phương sai,

$$
\begin{aligned}
\operatorname{Var}\sum_{k=1}^bg_k&=\sum_{k=1}^b\sum_{l=1}^b\operatorname{Cov}(g_k,g_l)\\
&=\sigma^2\sum_{k=1}^b\sum_{l=1}^bc^{\lvert k-l\rvert}\\
&=\sigma^2\Bigl(b+2\sum_{m=1}^{b-1}(b-m)c^m\Bigr).
\end{aligned}
$$

Dòng thứ hai đếm cặp: $b$ cặp có $k=l$; với $1\le m\le b-1$, có $b-m$ cặp $(k,l)$ với $l-k=m$ và cũng $b-m$ cặp với $k-l=m$. Chia cho $b^2$ được công thức cần chứng minh. Với $b=2$: $\operatorname{Var}\bar g=\tfrac{\sigma^2}4(2+2c)$, nên $n_{\mathrm{eff}}=\tfrac{4}{2+2c}=\tfrac2{1+c}$. Với ba cặp tham số:

| $(b,c)$ | $b+2\sum_m(b-m)c^m$ | $\operatorname{Var}\bar g/\sigma^2$ | $n_{\mathrm{eff}}$ |
| --- | --- | --- | --- |
| $(4;\,0{,}9)$ | $14{,}098$ | $0{,}881$ | $1{,}135$ |
| $(4;\,0{,}5)$ | $8{,}25$ | $0{,}516$ | $1{,}939$ |
| $(32;\,0{,}9)$ | $434{,}18$ | $0{,}424$ | $2{,}358$ |

Hàng đầu là Ví dụ 08.9. Với $c=0{,}9$, tăng $b$ từ $4$ lên $32$ chỉ đưa $n_{\mathrm{eff}}$ từ $1{,}1$ lên $2{,}4$; với $c=0$, $n_{\mathrm{eff}}=b$.

**Kiểm tra lại.** Với $c=0$, công thức (d) cho $\operatorname{Var}\bar g=\sigma^2/b$; với $c\to1$, nó cho $\sigma^2$, đúng phương sai của một mẫu. Ba lỗi thường gặp: xét "liền nhau" theo vị trí trong bộ đệm, bỏ cặp $(10,11)$ ở vị trí $5$ và $1$ và được $3/10$; quên hệ số $2$ của các cặp $(k,l)$ và $(l,k)$; coi $n_{\mathrm{eff}}$ tăng tuyến tính theo $b$ khi các mẫu liền nhau.
:::

### Bài tập 08.11. Phép chọn theo hành động, dừng gradient và gradient của tầng ra

**Mức độ:** tính toán. Mục tiêu học tập 3 của ghi chú: chỉ ra phần nào của mạng nhận gradient và phần nào không.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 4 (Định nghĩa 08.10, 08.12, Ví dụ 08.13, đoạn về gradient dư); Sutton và Barto (2018), §9.3, §11.5; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.11 (Phép chọn theo hành động, dừng gradient và gradient của tầng ra)
Chỉ tham số của tầng ra được cập nhật; các tầng trước giữ cố định. Tầng ẩn cuối cho vector $\phi(o)\in\mathbb R^2$, và tham số được cập nhật là $\theta=W\in\mathbb R^{3\times2}$, nên trong bài này mạng trực tuyến viết $\mathbf q_W(o)=W\phi(o)$ và $Q_W(o,a_k)=[\mathbf q_W(o)]_{a_k}$, với hàng $k$ của $W$ ứng với hành động $a_k$:

$$
W=\begin{pmatrix}1&0\\0&1\\0{,}5&0{,}5\end{pmatrix}.
$$

Mạng mục tiêu $\mathbf q_{W^-}(o)=W^-\phi(o)$ vừa được đồng bộ, nên $W^-=W$; $\gamma=0{,}9$; mini-batch $b=2$:

| $i$ | $\phi(O_i)$ | $A_i$ | $R_i$ | $Z_i$ | $\phi(O'_i)$ |
| --- | --- | --- | --- | --- | --- |
| 1 | $(2;\,1)$ | $a_3$ | $1$ | $0$ | $(1;\,2)$ |
| 2 | $(0;\,3)$ | $a_1$ | $-1$ | $1$ | $(2;\,2)$ |

- (a) Tính mảng $M$ kích thước $[2,3]$ có hàng $i$ là $\mathbf q_W(O_i)$, các $q_i$ bằng phép chọn theo hành động, các $y_i$, $\delta_i$ và $L_B$.
- (b) Tính $\partial L_B/\partial M$ và $\nabla_WL_B$. Chỉ ra hàng nào của $W$ có gradient bằng $0$ và giải thích.
- (c) Đi một bước SGD với $\eta=0{,}1$. Tính $W$ mới, $q_1$, $q_2$ mới, giá trị $Q_W(O_1,a_1)$ trước và sau bước, và vector $\mathbf q_W(o^\star)$ trước và sau bước tại quan sát $o^\star$ có $\phi(o^\star)=(1;\,1)$, không có trong mini-batch.
- (d) Một bản cài đặt tính mục tiêu bằng chính đối tượng mạng trực tuyến và không dừng gradient. Tính số hạng mà mục tiêu $y_1$ thêm vào $\nabla_WL_B$, gradient đầy đủ, và giá trị $Q_W(O'_1,a_2)$ sau một bước SGD với $\eta=0{,}1$ trong hai trường hợp: có và không có dừng gradient.
:::

::: hint Gợi ý Bài tập 08.11
Theo Định nghĩa 08.12, $\partial q_i/\partial M_{i,a}$ bằng $1$ khi $a=A_i$ và $0$ khi $a\ne A_i$. Vì $M_{i,k}=W_{k,\cdot}\,\phi(O_i)$, gradient theo hàng $k$ của $W$ là $\sum_i(\partial L_B/\partial M_{i,k})\,\phi(O_i)^\top$. Với (d), khi giá trị cực đại đạt duy nhất tại $a_2$, $\nabla_Wy_1$ chỉ khác $0$ ở hàng $a_2$ và bằng $\gamma\,\phi(O'_1)^\top$ tại đó.
:::

::: solution Lời giải Bài tập 08.11
**Câu (a).** $\mathbf q_W(O_1)=W(2;1)=(2;\,1;\,1{,}5)$ và $\mathbf q_W(O_2)=W(0;3)=(0;\,3;\,1{,}5)$, nên

$$
M=\begin{pmatrix}2&1&1{,}5\\0&3&1{,}5\end{pmatrix},
$$

và phép chọn theo hành động cho $q_1=M_{1,3}=1{,}5$, $q_2=M_{2,1}=0$.

Với $W^-=W$, $\mathbf q_{W^-}(O'_1)=(1;\,2;\,1{,}5)$ có cực đại $2$ tại $a_2$, nên $y_1=1+0{,}9\cdot2=2{,}8$. Mẫu 2 có $Z_2=1$, nên $y_2=R_2=-1$, dù $\mathbf q_{W^-}(O'_2)=(2;\,2;\,2)$. Vậy $\delta=(1{,}3;\,-1)$ và $L_B=\tfrac12(1{,}69+1)=1{,}345$.

**Câu (b).** Với $b=2$, $\tfrac2b(q_i-y_i)$ bằng $-1{,}3$ và $1$; lan truyền ngược đặt hai số này vào ô $(1,3)$ và $(2,1)$:

$$
\frac{\partial L_B}{\partial M}=\begin{pmatrix}0&0&-1{,}3\\1&0&0\end{pmatrix},
$$

$$
\nabla_WL_B=\begin{pmatrix}0&3\\0&0\\-2{,}6&-1{,}3\end{pmatrix}.
$$

Hàng $a_1$ nhận $1\cdot\phi(O_2)^\top=(0;\,3)$, hàng $a_3$ nhận $-1{,}3\cdot\phi(O_1)^\top=(-2{,}6;\,-1{,}3)$. Hàng $a_2$ có gradient $0$ vì không mẫu nào có $A_i=a_2$. Hành động $a_2$ đạt cực đại tại $O'_1$, nhưng giá trị đó nằm trên đường tạo mục tiêu, trong $\operatorname{sg}$ (Định nghĩa 08.12).

**Câu (c).** $W\leftarrow W-0{,}1\,\nabla_WL_B$ cho hàng $a_1$ bằng $(1;\,-0{,}3)$, hàng $a_2$ giữ $(0;\,1)$, hàng $a_3$ bằng $(0{,}76;\,0{,}63)$. Khi đó $q_1=0{,}76\cdot2+0{,}63\cdot1=2{,}15$, tăng từ $1{,}5$ về phía $2{,}8$, và $q_2=-0{,}3\cdot3=-0{,}9$, giảm từ $0$ về phía $-1$. Giá trị $Q_W(O_1,a_1)$ đổi từ $2$ thành $1{,}7$ dù mẫu 1 đã thực hiện $a_3$: hàng $a_1$ bị mẫu 2 kéo xuống, và $O_1$ dùng chung hàng đó. Tại $o^\star$, $\mathbf q_W(o^\star)$ đổi từ $(1;\,1;\,1)$ thành $(0{,}7;\,1;\,1{,}39)$. Một bước trên hai mẫu đổi giá trị ở các cặp quan sát–hành động không có trong mini-batch, vì các cặp dùng chung tham số.

**Câu (d).** Khi mục tiêu tính bằng chính $W$, $y_1(W)=1+0{,}9\max_{a'}[W\phi(O'_1)]_{a'}$ và cực đại đạt duy nhất tại $a_2$, nên $\nabla_Wy_1$ chỉ khác $0$ ở hàng $a_2$ và bằng $0{,}9\cdot(1;\,2)=(0{,}9;\,1{,}8)$. Gradient đầy đủ của $\tfrac1b\sum_i(y_i-q_i)^2$ là $\tfrac2b\sum_i(y_i-q_i)(\nabla_Wy_i-\nabla_Wq_i)$; so với (b), nó thêm số hạng $\tfrac22\,\delta_1\nabla_Wy_1=1{,}3\cdot(0{,}9;\,1{,}8)=(1{,}17;\,2{,}34)$ ở hàng $a_2$. Mẫu 2 không thêm gì vì $y_2=R_2$. Sau một bước, hàng $a_2$ thành $(-0{,}117;\,0{,}766)$, và $Q_W(O'_1,a_2)=-0{,}117+0{,}766\cdot2=1{,}415$; có dừng gradient, hàng $a_2$ không đổi và $Q_W(O'_1,a_2)=2$. Gradient qua mục tiêu kéo giá trị bootstrap xuống về phía dự đoán; đó là phương pháp gradient dư (Sutton và Barto, 2018, §11.5), không phải DQN. Khi mạng mục tiêu có tham số riêng $W^-$, $\nabla_Wy_1=0$ đúng về mặt toán học, và $\operatorname{sg}$ chỉ giúp thư viện không lưu đồ thị của đường tạo mục tiêu.

**Kiểm tra lại.** Với tầng ra tuyến tính, độ đổi của $q_i$ sau bước là $-\eta\,\tfrac2b(q_i-y_i)\lVert\phi(O_i)\rVert^2$ cộng ảnh hưởng của mẫu kia trên cùng hàng; ở đây hai mẫu dùng hai hàng khác nhau, nên $\Delta q_1=0{,}1\cdot1{,}3\cdot5=0{,}65$ và $\Delta q_2=-0{,}1\cdot1\cdot9=-0{,}9$, khớp (c). Ba lỗi thường gặp: chọn theo chỉ số hàng thay cho cột $A_i$; đặt gradient vào ô lớn nhất của mỗi hàng, như ô $(2,2)$ có giá trị $3$; đưa giá trị $2$ tại $O'_2$ vào mục tiêu của mẫu kết thúc, cho $y_2=0{,}8$.
:::

### Bài tập 08.12. Truy dấu hai bộ đếm với $F=3$

**Mức độ:** tính toán ở câu (a)–(c); chứng minh ở câu (d). Mục tiêu học tập 3 của ghi chú: truy dấu vòng lặp của DQN với hai bộ đếm $t$ và $k_{\mathrm{opt}}$.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 4 (Thuật toán 08.13, Ví dụ 08.14, 08.15); Mnih và cộng sự (2015), Extended Data Table 1 ($N_{\mathrm{start}}=5\cdot10^4$, $F=4$, $C=10^4$); số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.12 (Truy dấu hai bộ đếm với $F=3$)
Chạy Thuật toán 08.13 với $N=8$, $b=2$, $N_{\mathrm{start}}=4$, $F=3$, $C=2$, $T=20$; khởi tạo $t=0$, $k_{\mathrm{opt}}=0$, $\mathcal D=\varnothing$; các mẫu chuyển được đánh số $1,2,\dots$ theo thứ tự thu thập. Nhắc lại thứ tự của thuật toán: bước 4 tăng $t$; bước 5–9 chạy khi $\lvert\mathcal D\rvert\ge N_{\mathrm{start}}$ và $t\bmod F=0$; bước 8 cập nhật $\theta$ rồi tăng $k_{\mathrm{opt}}$; bước 9 gán $\theta^-\leftarrow\theta$ khi $k_{\mathrm{opt}}\bmod C=0$.

- (a) Lập bảng các giá trị $t$ tại đó bước 5–9 chạy, kèm $\lvert\mathcal D\rvert$, các mẫu đang có trong $\mathcal D$, $k_{\mathrm{opt}}$ sau cập nhật và việc có đồng bộ hay không.
- (b) Bản cài đặt thứ nhất kiểm $k_{\mathrm{opt}}\bmod C=0$ trước khi tăng $k_{\mathrm{opt}}$. Xác định các bước tối ưu được theo sau bởi một lần đồng bộ, và số bước tối ưu dùng tham số $\theta^-$ ban đầu.
- (c) Bản cài đặt thứ hai bỏ bước 9 và gán $\theta^-\leftarrow\theta$ ở cuối mỗi vòng lặp có $t\bmod C=0$, tức sau bước 4 khi không tối ưu và sau bước 8 khi có tối ưu. Xác định các thời điểm $\theta^-$ nhận giá trị mới, và chứng tỏ mỗi bước tối ưu dùng $\theta^-$ bằng $\theta$ ngay trước bước đó, như khi $C=1$.
- (d) Chứng minh rằng khi $N_{\mathrm{start}}\le N$ và $N_{\mathrm{start}}\le T$, số bước tối ưu sau $T$ bước môi trường là $K=\lfloor T/F\rfloor-\lfloor(N_{\mathrm{start}}-1)/F\rfloor$. Tính $K$ và số lần đồng bộ cho $T=5\cdot10^6$, $N_{\mathrm{start}}=5\cdot10^4$, $F=4$, $C=10^4$.
:::

::: hint Gợi ý Bài tập 08.12
Sau bước 4, $t$ là số bước môi trường đã hoàn tất và $\lvert\mathcal D\rvert=\min(t,N)$; sau $t\ge N$ lần ghi, $\mathcal D$ chứa các mẫu $t-N+1,\dots,t$ (Định nghĩa 08.7). Với (d), vì $N_{\mathrm{start}}\le N$, điều kiện $\min(t,N)\ge N_{\mathrm{start}}$ tương đương $t\ge N_{\mathrm{start}}$; còn lại là đếm bội của $F$ trong một đoạn số nguyên.
:::

::: solution Lời giải Bài tập 08.12
**Câu (a).** Điều kiện tối ưu là $\min(t,8)\ge4$ và $t$ chia hết cho $3$, tức $t\in\{6,9,12,15,18\}$; tại $t=3$, $\lvert\mathcal D\rvert=3<N_{\mathrm{start}}$.

| $t$ | $\lvert\mathcal D\rvert$ | mẫu trong $\mathcal D$ | $k_{\mathrm{opt}}$ sau cập nhật | đồng bộ |
| --- | --- | --- | --- | --- |
| $6$ | $6$ | $1$–$6$ | $1$ | không |
| $9$ | $8$ | $2$–$9$ | $2$ | có |
| $12$ | $8$ | $5$–$12$ | $3$ | không |
| $15$ | $8$ | $8$–$15$ | $4$ | có |
| $18$ | $8$ | $11$–$18$ | $5$ | không |

Tại $t=19$ và $t=20$ không có bước tối ưu; khi $t=20=T$ thuật toán dừng. Từ $t=6$ tới $t=18$ có năm bước tối ưu và hai lần đồng bộ; $\theta^-$ ban đầu phục vụ bước tối ưu $1$ và $2$, đúng $C=2$ bước, và bước $5$ dùng $\theta^-$ của lần đồng bộ sau bước $4$.

**Câu (b).** Phép kiểm đọc $k_{\mathrm{opt}}=0,1,2,3,4$ trước khi tăng, nên đồng bộ xảy ra sau bước tối ưu $1$ ($t=6$), $3$ ($t=12$) và $5$ ($t=18$). Tham số $\theta^-$ ban đầu chỉ phục vụ bước tối ưu $1$; mọi lần đồng bộ sớm hơn một bước tối ưu so với (a), như Ví dụ 08.15 với $F=2$.

**Câu (c).** $\theta$ chỉ đổi tại $t=6,9,12,15,18$, sau các bước tối ưu $1,\dots,5$. Phép gán ở các thời điểm chẵn cho $\theta^-$ giá trị mới tại $t=6$ ($\theta$ sau bước $1$), $t=10$ (sau bước $2$), $t=12$ (sau bước $3$), $t=16$ (sau bước $4$) và $t=18$ (sau bước $5$); ở các thời điểm chẵn khác, phép gán chép lại cùng giá trị. Vì vậy bước $2$ tại $t=9$ dùng $\theta$ sau bước $1$, bước $3$ tại $t=12$ dùng $\theta$ sau bước $2$ (gán tại $t=10$), bước $4$ tại $t=15$ dùng $\theta$ sau bước $3$, bước $5$ tại $t=18$ dùng $\theta$ sau bước $4$: mỗi bước tối ưu hồi quy về mục tiêu tính bằng $\theta$ ngay trước nó, đúng như $C=1$. Khi $C\le F$, đếm $C$ theo $t$ ở mỗi bước môi trường xóa tác dụng của mạng mục tiêu, vì từ thời điểm của một bước tối ưu tới trước bước tối ưu kế tiếp có $F\ge C$ giá trị $t$ liên tiếp, trong đó luôn có một bội của $C$; trong Ví dụ 08.14, cùng số $10\,000$ đếm theo $t$ chỉ giữ $\theta^-$ đứng yên $2\,500$ bước tối ưu.

**Câu (d).** Vì $N_{\mathrm{start}}\le N$: nếu $t\ge N_{\mathrm{start}}$ thì $\min(t,N)\ge N_{\mathrm{start}}$; nếu $t<N_{\mathrm{start}}$ thì $\min(t,N)\le t<N_{\mathrm{start}}$. Vậy bước tối ưu chạy đúng tại các $t\in\{N_{\mathrm{start}},\dots,T\}$ chia hết cho $F$. Số bội của $F$ trong $\{1,\dots,T\}$ là $\lfloor T/F\rfloor$, trong $\{1,\dots,N_{\mathrm{start}}-1\}$ là $\lfloor(N_{\mathrm{start}}-1)/F\rfloor$; hiệu hai số là $K$. Với dữ kiện của (a): $K=\lfloor20/3\rfloor-\lfloor3/3\rfloor=6-1=5$, khớp bảng. Với $T=5\cdot10^6$, $N_{\mathrm{start}}=5\cdot10^4$, $F=4$:

$$
\begin{aligned}
K&=1\,250\,000-\lfloor49\,999/4\rfloor\\
&=1\,250\,000-12\,499\\
&=1\,237\,501 .
\end{aligned}
$$

Lần đồng bộ thứ $m$ xảy ra ngay sau bước tối ưu thứ $mC$, nên số lần đồng bộ là $\lfloor K/C\rfloor=123$; $7\,501$ bước tối ưu cuối dùng $\theta^-$ của lần đồng bộ thứ $123$.

**Kiểm tra lại.** Ở (a), $K=5$ và $\lfloor5/2\rfloor=2$ lần đồng bộ khớp công thức của (d). Ba lỗi thường gặp: tính một bước tối ưu tại $t=3$ khi $\lvert\mathcal D\rvert=3<N_{\mathrm{start}}$; ghi $\mathcal D$ chứa mẫu $1$–$9$ tại $t=9$, quên mẫu $1$ đã bị ghi đè; coi bản cài đặt ở (c) tương đương $C=2$ vì "cứ hai bước môi trường lại đồng bộ".
:::

### Bài tập 08.13. Ba bộ tối ưu trên ba tọa độ

**Mức độ:** tính toán ở câu (a)–(c); chứng minh ở câu (d). Mục tiêu học tập 4 của ghi chú: viết SGD, RMSprop và Adam theo từng tọa độ.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 5 (Định nghĩa 08.15–08.18, Ví dụ 08.20–08.22, bảng so sánh ba bộ tối ưu); bài giảng gốc (2025–2026), trang 23–26; Kingma và Ba (2015); Goodfellow, Bengio và Courville (2016), §8.5.2, §8.5.3; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.13 (Ba bộ tối ưu trên ba tọa độ)
Tham số $\theta\in\mathbb R^3$. Hai bước tối ưu liên tiếp $j=1,2$ có gradient mini-batch

$$
\begin{aligned}
g_1&=(0{,}4;\,-0{,}01;\,0),\\
g_2&=(-0{,}2;\,-0{,}01;\,0);
\end{aligned}
$$

tọa độ thứ ba là một tham số mà không mẫu nào trong hai mini-batch tác động tới. Tốc độ học $\eta=0{,}01$. RMSprop dùng $\rho=0{,}9$, $v_0=0$; Adam dùng $\beta_1=0{,}9$, $\beta_2=0{,}999$, $m_0=v_0=0$; cả hai dùng $\epsilon_{\mathrm{opt}}=10^{-8}$, đặt ngoài căn.

- (a) Tính lượng thay đổi $\theta_j-\theta_{j-1}$ theo từng tọa độ, với $j=1,2$, của SGD.
- (b) Tính các đại lượng tương tự cho RMSprop và Adam, làm tròn tới bốn chữ số có nghĩa. Với tọa độ thứ ba, nêu điều xảy ra khi $\epsilon_{\mathrm{opt}}=0$. Tính bước đầu của Adam khi bỏ hiệu chỉnh lệch.
- (c) So sánh hướng và độ lớn của bước ở tọa độ thứ nhất (gradient đổi dấu) và tọa độ thứ hai (gradient không đổi) giữa ba bộ tối ưu.
- (d) Chứng minh: nếu một tọa độ có gradient không đổi $g\ne0$ ở mọi bước, bước Adam theo tọa độ đó là $-\eta g/(\lvert g\rvert+\epsilon_{\mathrm{opt}})$ với mọi $j$, còn bước RMSprop là $-\eta g/\bigl(\lvert g\rvert\sqrt{1-\rho^{\,j}}+\epsilon_{\mathrm{opt}}\bigr)$. Kiểm hai công thức trên tọa độ thứ hai.
:::

::: hint Gợi ý Bài tập 08.13
Mọi phép toán lấy theo từng tọa độ. Ở bước đầu với $v_0=0$, RMSprop có $v_1=(1-\rho)g_1\odot g_1$, còn Adam có $\hat m_1=g_1$ và $\hat v_1=g_1\odot g_1$. Với (d), khai triển $m_j=(1-\beta_1)\sum_{\ell=1}^j\beta_1^{\,j-\ell}g_\ell$ và tổng cấp số nhân $\sum_{\ell=1}^j\beta^{\,j-\ell}=(1-\beta^{\,j})/(1-\beta)$.
:::

::: solution Lời giải Bài tập 08.13
**Câu (a).** SGD trừ $\eta g_j$ (Định nghĩa 08.16): bước $1$ là $(-0{,}004;\,0{,}0001;\,0)$, bước $2$ là $(0{,}002;\,0{,}0001;\,0)$. Mỗi bước tỉ lệ với độ lớn của gradient tại tọa độ đó, nên tọa độ thứ hai đi nhỏ hơn tọa độ thứ nhất $40$ lần ở bước $1$.

**Câu (b).** RMSprop (Định nghĩa 08.17):

$$
\begin{aligned}
v_1&=0{,}1\,g_1\odot g_1\\
&=(0{,}016;\,10^{-5};\,0),\\
\sqrt{v_1}&\approx(0{,}1265;\,0{,}003162;\,0),\\
v_2&=0{,}9\,v_1+0{,}1\,g_2\odot g_2\\
&=(0{,}0184;\,1{,}9\cdot10^{-5};\,0),\\
\sqrt{v_2}&\approx(0{,}1356;\,0{,}004359;\,0).
\end{aligned}
$$

Bước $1$ là $-\eta\,g_1\oslash(\sqrt{v_1}+\epsilon_{\mathrm{opt}})\approx(-0{,}03162;\,0{,}03162;\,0)$; bước $2$ là $\approx(0{,}01474;\,0{,}02294;\,0)$.

Adam (Định nghĩa 08.18): $m_1=(0{,}04;\,-0{,}001;\,0)$, $v_1=(1{,}6\cdot10^{-4};\,10^{-7};\,0)$, $\hat m_1=g_1$, $\hat v_1=g_1\odot g_1$, nên bước $1$ là $\approx(-0{,}01000;\,0{,}01000;\,0)$, tức bằng $\eta$ theo dấu gradient tới bốn chữ số có nghĩa. Tiếp theo,

$$
\begin{aligned}
m_2&=0{,}9\,m_1+0{,}1\,g_2\\
&=(0{,}016;\,-0{,}0019;\,0),\\
\hat m_2&=m_2/0{,}19\\
&\approx(0{,}08421;\,-0{,}01000;\,0),\\
v_2&=0{,}999\,v_1+0{,}001\,g_2\odot g_2\\
&=(1{,}998\cdot10^{-4};\,1{,}999\cdot10^{-7};\,0),\\
\hat v_2&=v_2/0{,}001999\\
&\approx(0{,}09997;\,1{,}000\cdot10^{-4};\,0),
\end{aligned}
$$

nên $\sqrt{\hat v_2}\approx(0{,}3162;\,0{,}01000;\,0)$ và bước $2$ là $\approx(-0{,}002663;\,0{,}01000;\,0)$.

Ở tọa độ thứ ba, $g_{j,3}=0$ và $v_{j,3}=0$; với $\epsilon_{\mathrm{opt}}=10^{-8}$, bước là $0/10^{-8}=0$. Với $\epsilon_{\mathrm{opt}}=0$, bước là $0/0$, không xác định; trong số học dấu phẩy động, kết quả là giá trị không xác định (NaN) và lan sang $\theta$. Bỏ hiệu chỉnh lệch, bước đầu của Adam là $-\eta\,m_1\oslash\sqrt{v_1}\approx(-0{,}03162;\,0{,}03162;\,0)$, lớn gấp $(1-\beta_1)/\sqrt{1-\beta_2}\approx3{,}162$ lần (Ví dụ 08.22).

**Câu (c).**

| tọa độ | SGD, bước 1; 2 | RMSprop, bước 1; 2 | Adam, bước 1; 2 |
| --- | --- | --- | --- |
| thứ nhất | $-0{,}004$; $+0{,}002$ | $-0{,}03162$; $+0{,}01474$ | $-0{,}01000$; $-0{,}002663$ |
| thứ hai | $+0{,}0001$; $+0{,}0001$ | $+0{,}03162$; $+0{,}02294$ | $+0{,}01000$; $+0{,}01000$ |

Ở tọa độ thứ nhất, SGD và RMSprop đổi chiều theo dấu của gradient tức thời; Adam đi tiếp cùng chiều với bước nhỏ hơn, vì $\hat m_2>0$ còn giữ phần lớn gradient đầu (Ví dụ 08.21). Ở tọa độ thứ hai, gradient nhỏ $0{,}01$ cho SGD bước $10^{-4}$, còn hai phương pháp thích nghi đi bước cỡ $\eta$: Adam đúng $\eta$, RMSprop lớn hơn $\eta$ và giảm dần.

**Câu (d).** Với $g_\ell=g$ ở mọi bước,

$$
\begin{aligned}
m_j&=(1-\beta_1)\,g\sum_{\ell=1}^j\beta_1^{\,j-\ell}\\
&=(1-\beta_1^{\,j})\,g,\\
\hat m_j&=g,\\
v_j&=(1-\beta_2^{\,j})\,g^2,\\
\hat v_j&=g^2,
\end{aligned}
$$

nên bước Adam là $-\eta g/(\sqrt{g^2}+\epsilon_{\mathrm{opt}})=-\eta g/(\lvert g\rvert+\epsilon_{\mathrm{opt}})$, không phụ thuộc $j$. Với RMSprop, cùng phép tính cho $v_j=(1-\rho^{\,j})g^2$ và bước $-\eta g/\bigl(\lvert g\rvert\sqrt{1-\rho^{\,j}}+\epsilon_{\mathrm{opt}}\bigr)$. Bỏ qua $\epsilon_{\mathrm{opt}}$, độ lớn bước RMSprop là $\eta/\sqrt{1-\rho^{\,j}}$, giảm từ $\eta/\sqrt{1-\rho}$ về $\eta$ khi $j\to\infty$. Trên tọa độ thứ hai, $g=-0{,}01$: Adam cho $+0{,}01$ ở cả hai bước; RMSprop cho $0{,}01/\sqrt{0{,}1}\approx0{,}03162$ và $0{,}01/\sqrt{0{,}19}\approx0{,}02294$, khớp (b).

**Kiểm tra lại.** Ở mọi bộ tối ưu, tọa độ thứ ba đứng yên khi $\epsilon_{\mathrm{opt}}>0$. Ba lỗi thường gặp: đặt $\epsilon_{\mathrm{opt}}$ trong căn rồi so với số của lời giải, sai khác lớn khi $v_j$ nhỏ; dùng $\beta_1^{\,j}$ với $j=k_{\mathrm{opt}}$ trước khi tăng, tức $j=0$ ở bước đầu, cho mẫu số $1-\beta_1^0=0$; kết luận Adam "tốt hơn" từ bảng (c), trong khi bảng chỉ so hướng và độ lớn bước, không so chất lượng của chính sách.
:::

### Bài tập 08.14. Mốc đồng bộ và ví dụ hai trạng thái với mạng mục tiêu

**Mức độ:** tính toán ở câu (a), (d); chứng minh ở câu (b), (c). Mục tiêu học tập 5 của ghi chú: tính độ thay đổi của mục tiêu tại mốc đồng bộ và nêu vì sao mạng mục tiêu không tạo bảo đảm hội tụ.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 6 (Nhận xét 08.20, 08.21, Ví dụ 08.23, 08.24); ghi chú bài giảng Bài 07, Mệnh đề 07.37; Sutton và Barto (2018), §11.2, §11.3; bài giảng gốc (2025–2026), trang 29, 31, 33; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.14 (Mốc đồng bộ và ví dụ hai trạng thái với mạng mục tiêu)
(a) Ba mẫu chuyển trong $\mathcal D$, $\gamma=0{,}99$. Ngay trước một mốc đồng bộ, mạng mục tiêu cho $\max_{a'}Q_{\theta^-}(O'_i,a')$; tại mốc, mạng trực tuyến cho $\max_{a'}Q_\theta(O'_i,a')$:

| $i$ | $R_i$ | $Z_i$ | $U_i$ | $\max_{a'}Q_{\theta^-}(O'_i,a')$ | $\max_{a'}Q_\theta(O'_i,a')$ |
| --- | --- | --- | --- | --- | --- |
| 1 | $1$ | $0$ | $0$ | $50$ | $52$ |
| 2 | $1$ | $0$ | $1$ | $60$ | $57$ |
| 3 | $1$ | $1$ | $0$ | $40$ | $45$ |

Tính mục tiêu của từng mẫu trước và ngay sau phép gán $\theta^-\leftarrow\theta$, và độ thay đổi $\Delta y_i$.

(b) Hai trạng thái $s_1$, $s_2$ có đặc trưng $x(s_1)=1$, $x(s_2)=2$ và hàm giá trị $\hat v(s,w)=x(s)\,w$ với $w\in\mathbb R$. Chỉ chuyển $s_1\to s_2$ với phần thưởng $0$ được cập nhật, bằng TD(0) bán gradient với bước học $\alpha\in(0,1)$ và $\gamma\in[0,1)$; mục tiêu dùng tham số $w^-$ giữ cố định trong $C$ bước, mỗi chu kỳ bắt đầu với $w_0=w^-$, rồi đồng bộ $w^-\leftarrow w_C$:

$$
\begin{aligned}
w_{k+1}&=w_k+\alpha\,\delta_k\,x(s_1),\\
\delta_k&=\gamma\,x(s_2)\,w^--x(s_1)\,w_k .
\end{aligned}
$$

Chứng minh $w_C=c(C)\,w^-$ với $c(C)=2\gamma-(2\gamma-1)(1-\alpha)^C$, và kiểm rằng $\gamma=0{,}9$, $\alpha=0{,}1$ cho $c(C)=1{,}8-0{,}8\cdot0{,}9^C$ của Ví dụ 08.24.

(c) Với $\gamma\in(\tfrac12,1)$, chứng minh $1<c(C)\le\bigl(1+\alpha(2\gamma-1)\bigr)^C$ với mọi $C\ge1$, dấu bằng chỉ khi $C=1$. Suy ra $\lvert w\rvert\to\infty$ với mọi $C$ khi $w_0\ne0$, và hệ số tương đương mỗi bước $c(C)^{1/C}$ không vượt hệ số $1+\alpha(2\gamma-1)$ của trường hợp không có mạng mục tiêu.

(d) Với $\gamma=0{,}9$, $\alpha=0{,}1$, tính $c(20)$, $c(20)^{1/20}$ và $1{,}08^{20}$. Với $\gamma=0{,}4$ và cùng $\alpha$, tính $c(1)$, $c(10)$ và $\lim_{C\to\infty}c(C)$, rồi xác định giả thiết quyết định việc tham số tăng không chặn.
:::

::: hint Gợi ý Bài tập 08.14
Với (a), dùng Nhận xét 08.20; mặt nạ chỉ chứa $Z_i$. Với (b), trong một chu kỳ, $w_{k+1}=(1-\alpha)w_k+2\alpha\gamma w^-$ là một phép co về điểm cố định $2\gamma w^-$. Với (c), viết $c(C)=1+(2\gamma-1)\bigl[1-(1-\alpha)^C\bigr]$ và dùng bất đẳng thức Bernoulli $(1+x)^C\ge1+Cx$ với $x\ge-1$, dấu bằng chỉ khi $C=1$ hoặc $x=0$.
:::

::: solution Lời giải Bài tập 08.14
**Câu (a).** Theo Định nghĩa 08.4 và Nhận xét 08.20:

| $i$ | $y_i$ trước | $y_i$ sau | $\Delta y_i$ |
| --- | --- | --- | --- |
| 1 | $1+0{,}99\cdot50=50{,}5$ | $1+0{,}99\cdot52=52{,}48$ | $0{,}99\cdot2=1{,}98$ |
| 2 | $1+0{,}99\cdot60=60{,}4$ | $1+0{,}99\cdot57=57{,}43$ | $0{,}99\cdot(-3)=-2{,}97$ |
| 3 | $1$ | $1$ | $0$ |

Mẫu 2 bị cắt ngắn nhưng $Z_2=0$, nên vẫn đổi mục tiêu, và lần này mục tiêu giảm. Mẫu 3 kết thúc nên giữ $y_3=R_3$ dù hai giá trị cực đại khác nhau. Sáu thành phần đã lưu của cả ba mẫu không đổi; chỉ tham số trong phép cực đại đổi.

**Câu (b).** Thay $x(s_1)=1$, $x(s_2)=2$: $w_{k+1}=w_k+\alpha(2\gamma w^--w_k)=(1-\alpha)w_k+2\alpha\gamma w^-$. Trừ $2\gamma w^-$ ở hai vế,

$$
w_{k+1}-2\gamma w^-=(1-\alpha)\,(w_k-2\gamma w^-).
$$

Lặp đẳng thức này $C$ lần từ $w_0=w^-$:

$$
\begin{aligned}
w_C&=2\gamma w^-+(1-\alpha)^C\,(w^--2\gamma w^-)\\
&=\bigl[2\gamma-(2\gamma-1)(1-\alpha)^C\bigr]\,w^-.
\end{aligned}
$$

Phép tính đúng với mọi $\gamma\in[0,1)$; điều kiện $\gamma>\tfrac12$ chỉ được dùng ở (c). Với $\gamma=0{,}9$, $\alpha=0{,}1$: $2\gamma=1{,}8$, $2\gamma-1=0{,}8$, $1-\alpha=0{,}9$, nên $c(C)=1{,}8-0{,}8\cdot0{,}9^C$.

**Câu (c).** Đặt $\kappa=2\gamma-1\in(0,1)$, khi đó $c(C)=1+\kappa\bigl[1-(1-\alpha)^C\bigr]$.

1. **Cận dưới.** Vì $0<1-\alpha<1$, $0<(1-\alpha)^C<1$, nên $c(C)>1$.
2. **Cận trên.** Bất đẳng thức Bernoulli với $x=-\alpha$ cho $(1-\alpha)^C\ge1-C\alpha$, nên $1-(1-\alpha)^C\le C\alpha$ và $c(C)\le1+\kappa C\alpha$. Bất đẳng thức Bernoulli với $x=\alpha\kappa$ cho $1+C\alpha\kappa\le(1+\alpha\kappa)^C$. Ghép hai bước, $c(C)\le(1+\alpha\kappa)^C$.
3. **Dấu bằng.** Với $C=1$, cả hai vế bằng $1+\alpha\kappa$. Với $C\ge2$, bất đẳng thức Bernoulli ở bước 2 chặt vì $\alpha\ne0$, nên $c(C)<(1+\alpha\kappa)^C$.

Sau $n$ chu kỳ, $w^-=c(C)^n\,w_0$; vì $c(C)>1$, $\lvert w^-\rvert\to\infty$ khi $w_0\ne0$, với mọi $C\ge1$. Lấy căn bậc $C$ của cận trên, $c(C)^{1/C}\le1+\alpha(2\gamma-1)$, hệ số mỗi bước của Mệnh đề 07.37. $\square$

**Câu (d).** Với $\gamma=0{,}9$, $\alpha=0{,}1$: $c(20)=1{,}8-0{,}8\cdot0{,}9^{20}\approx1{,}8-0{,}8\cdot0{,}1216\approx1{,}703$, $c(20)^{1/20}\approx1{,}027$, còn $1{,}08^{20}\approx4{,}661$. Với $\gamma=0{,}4$: $c(C)=0{,}8+0{,}2\cdot0{,}9^C$, nên $c(1)=0{,}98$, $c(10)\approx0{,}870$ và $c(C)\to0{,}8$; mọi $c(C)<1$ nên $w\to0$, và không có mạng mục tiêu, hệ số mỗi bước $1+0{,}1\cdot(0{,}8-1)=0{,}98<1$ cũng cho $w\to0$. Giả thiết quyết định là $2\gamma>1$, tức mục tiêu $2\gamma w^-$ gấp $2\gamma>1$ lần giá trị đang cập nhật (như Ví dụ 08.24); chu kỳ $C$ chỉ đổi tốc độ, không đổi việc tham số tăng hay giảm. Kết quả này minh họa Nhận xét 08.21: mạng mục tiêu không bỏ yếu tố nào của bộ ba bất ổn. Với $\gamma=0{,}4$, cả ba yếu tố vẫn có mặt mà $w\to0$: bộ ba bất ổn làm mất bảo đảm hội tụ, không buộc thuật toán phân kỳ.

**Kiểm tra lại.** $C=1$ cho $c(1)=1+\alpha(2\gamma-1)=1{,}08$, đúng hệ số của Mệnh đề 07.37; $C=2$ cho $1{,}152<1{,}08^2=1{,}1664$, như câu kiểm tra nhanh của ghi chú. Ba lỗi thường gặp: đặt hệ số mỗi chu kỳ $1{,}703$ cạnh hệ số mỗi bước $1{,}08$ rồi kết luận mạng mục tiêu làm bất ổn nặng hơn; đưa $U_i$ vào mặt nạ ở (a), cho $\Delta y_2=0$; tính $\Delta y_i$ bằng hiệu giá trị cực đại tại $O_i$ thay cho $O'_i$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 08.15. Kích thước tensor và bộ nhớ của DQN trên ba môi trường

**Mức độ:** vận dụng. Mục tiêu học tập 3 và 6 của ghi chú: đọc giao diện tensor của một bước tối ưu và ước lượng bộ nhớ trước khi cài đặt.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 4 (Nhận xét 08.14, Ví dụ 08.16, 08.17, đoạn "Trong thực hành" sau Ví dụ 08.17), Mục 5 (bảng so sánh ba bộ tối ưu), Tình huống 08.1; ghi chú bài giảng Bài 07, Ví dụ 07.1 và Bài tập 07.20 (quan sát của Lunar Lander và Flappy Bird); kiến trúc mạng là lựa chọn sư phạm tự xây dựng.

::: exercise Bài tập 08.15 (Kích thước tensor và bộ nhớ của DQN trên ba môi trường)
Ba môi trường có quan sát là vector $n$ số thực và $\lvert\mathcal A\rvert$ hành động: CartPole-v1 với $n=4$, $\lvert\mathcal A\rvert=2$; Lunar Lander với $n=8$ (sáu biến liên tục và hai cờ chân chạm đất, lưu dạng số thực), $\lvert\mathcal A\rvert=4$; Flappy Bird với $n=12$, $\lvert\mathcal A\rvert=2$. Với mỗi môi trường, mạng trực tuyến là mạng nhiều tầng $n\to128\to128\to\lvert\mathcal A\rvert$, ba tầng kết nối đầy đủ có hệ số tự do, hàm kích hoạt ReLU; mạng mục tiêu có cùng kiến trúc; bộ tối ưu là Adam. Mọi tham số và trạng thái phụ ở dạng `float32` ($4$ byte). Bộ nhớ phát lại có $N=10^5$ vị trí, mỗi vị trí lưu riêng $O$ và $O'$ dạng `float32`, $A$ dạng `int64` ($8$ byte), $R$ dạng `float32`, $Z$ và $U$ dạng `bool` ($1$ byte mỗi cờ). Mini-batch có $b=64$ mẫu.

- (a) Tính số tham số $d$ của mạng trực tuyến cho mỗi môi trường, và số byte cho $\theta$, $\theta^-$ cùng hai vector trạng thái phụ $m_j$, $v_j$ của Adam.
- (b) Tính số byte của một mẫu chuyển và của toàn bộ nhớ phát lại cho mỗi môi trường; so với con số khoảng $56$ GB của bộ nhớ Atari $N=10^6$ lưu riêng $O$, $O'$ dạng `uint8` (ghi chú, Mục 4).

Chương trình viết bằng PyTorch, theo cùng quy ước với Bài tập 08.2 của ghi chú. `D.sample(b)` trả sáu mảng `ob, ab, rb, ob2, zb, ub` của một mini-batch, chiều đầu $b$, lần lượt chứa $O_i$, $A_i$, $R_i$, $O'_i$, $Z_i$, $U_i$. Hai mạng `q_online`, `q_target` nhận mảng quan sát kích thước $[b,n]$ và trả mảng $[b,\lvert\mathcal A\rvert]$. Một bước tối ưu tính

```python
with torch.no_grad():
    v = q_target(ob2).max(1).values
    y = rb + gamma * (1 - zb.float()) * v
q = q_online(ob).gather(1, ab.unsqueeze(1))
q = q.squeeze(1)
loss = ((y - q) ** 2).mean()
```

Trong đoạn mã: `max(1).values` lấy giá trị cực đại theo chiều thứ hai, chiều hành động; `ab.unsqueeze(1)` thêm một chiều kích thước $1$ ở vị trí thứ hai; `gather(1, ·)` là phép chọn theo hành động, lấy ở mỗi hàng phần tử của cột ghi trong chỉ số; `squeeze(1)` bỏ chiều thừa (squeeze) kích thước $1$ đó; khối `torch.no_grad()` là dạng cài đặt của phép dừng gradient $\operatorname{sg}$, tương đương gọi `.detach()` trên kết quả; thuộc tính `requires_grad` của một mảng bằng `True` khi mảng đó còn nhận gradient; `zb.float()` đổi cờ kiểu `bool` sang kiểu số.

- (c) Với Lunar Lander, ghi kích thước và kiểu của `ob`, `ob2`, `ab`, `rb`, `zb`, `ub`, của `q_online(ob)` và `q_target(ob2)`, của kết quả `gather` trước và sau `squeeze(1)`, của `v`, `y` và `loss`.
- (d) Viết bốn câu lệnh `assert` để phát hiện bốn lỗi: `ab` không có kiểu `int64`, kiểm trước dòng `gather`; và ba lỗi kiểm sau đoạn mã: lỗi lan truyền kích thước của Ví dụ 08.17 khi thiếu `squeeze(1)`, phép cực đại viết `.max()` không chỉ chiều, mục tiêu tính ngoài khối `torch.no_grad()`. Giải thích vì sao kiểm `y.shape == (b,)` không phát hiện được lỗi `.max()` không chỉ chiều.
:::

::: hint Gợi ý Bài tập 08.15
Một tầng kết nối đầy đủ từ $p$ sang $r$ đơn vị có $pr$ trọng số và $r$ hệ số tự do. Theo Nhận xét 08.14, chiều đầu của mọi mảng đánh số mẫu. Với (d), một số vô hướng cộng với vector `rb` kích thước $[b]$ lan truyền thành kích thước $[b]$.
:::

::: solution Lời giải Bài tập 08.15
**Câu (a).** Ba tầng có $128n+128$, $128\cdot128+128=16\,512$ và $128\lvert\mathcal A\rvert+\lvert\mathcal A\rvert$ tham số. Hai mạng và hai vector của Adam là bốn vector $d$ số, tức $16d$ byte.

| môi trường | $d$ | $\theta$, $\theta^-$, $m_j$, $v_j$ |
| --- | --- | --- |
| CartPole | $640+16\,512+258=17\,410$ | $278\,560$ byte |
| Lunar Lander | $1\,152+16\,512+516=18\,180$ | $290\,880$ byte |
| Flappy Bird | $1\,664+16\,512+258=18\,434$ | $294\,944$ byte |

Phần bộ nhớ của mạng và bộ tối ưu dưới $0{,}3$ MB ở cả ba môi trường; tầng giữa chiếm phần lớn số tham số.

**Câu (b).** Một mẫu chuyển chiếm $2\cdot4n+8+4+1+1=8n+14$ byte: $46$ byte với CartPole, $78$ byte với Lunar Lander, $110$ byte với Flappy Bird. Với $N=10^5$, bộ nhớ phát lại chiếm $4{,}6$ MB, $7{,}8$ MB và $11$ MB, gấp khoảng $17$ đến $37$ lần phần của mạng và bộ tối ưu, nhưng nhỏ hơn bộ nhớ Atari khoảng $56$ GB từ khoảng $5\,000$ đến $12\,000$ lần. Với quan sát vector số chiều thấp, lưu riêng $O$ và $O'$ không gây vấn đề bộ nhớ; kỹ thuật lưu mỗi khung một lần của ghi chú chỉ cần với ảnh.

**Câu (c).**

| mảng | kích thước | kiểu |
| --- | --- | --- |
| `ob`, `ob2` | $[64,8]$ | `float32` |
| `ab` | $[64]$ | `int64` |
| `rb` | $[64]$ | `float32` |
| `zb`, `ub` | $[64]$ | `bool` |
| `q_online(ob)`, `q_target(ob2)` | $[64,4]$ | `float32` |
| kết quả `gather`, trước `squeeze(1)` | $[64,1]$ | `float32` |
| `q` | $[64]$ | `float32` |
| `v` | $[64]$ | `float32` |
| `y` | $[64]$ | `float32` |
| `loss` | $[\,]$ | `float32` |

`ub` có trong mini-batch nhưng không vào hàm mất mát; `zb` được đổi sang kiểu số trước khi tính `1 - zb.float()`.

**Câu (d).**

Đặt trước dòng `gather`:

```python
assert ab.dtype == torch.int64
```

Đặt sau đoạn mã:

```python
assert q.shape == (b,)
assert v.shape == (b,)
assert not y.requires_grad
```

Câu lệnh đặt trước dòng `gather` bắt chỉ số hành động sai kiểu, vì `gather` của PyTorch nhận chỉ số kiểu `int64`; đặt sau đoạn mã thì chính dòng `gather` báo lỗi trước khi tới câu kiểm. Trong ba câu đặt sau, câu thứ nhất bắt lỗi thiếu `squeeze(1)`: khi `q` có kích thước $[b,1]$, phép trừ `y - q` lan truyền thành $[b,b]$ (Ví dụ 08.17). Câu thứ hai bắt lỗi `.max()` không chỉ chiều, vì khi đó `v` là một số vô hướng. Câu thứ ba bắt mục tiêu tính ngoài khối `torch.no_grad()`.

Với lỗi `.max()` không chỉ chiều, `y = rb + gamma * (1 - zb.float()) * v` vẫn có kích thước $[b]$, vì số vô hướng `v` lan truyền theo `rb`. Vì vậy chỉ kiểm `y` không đủ; phải kiểm `v` trước khi ghép vào mục tiêu. Mỗi câu lệnh kiểm một điều kiện của Nhận xét 08.14 hoặc Định nghĩa 08.12, không kiểm giá trị số, nên kết quả kiểm không phụ thuộc các con số mà phiên bản thư viện hay hạt giống ngẫu nhiên sinh ra.

**Kiểm tra lại.** Với CartPole, $17\,410=4\cdot128+128+128\cdot128+128+128\cdot2+2$. Ba lỗi thường gặp: quên hệ số tự do, cho $d=512+16\,384+256=17\,152$ với CartPole; tính bộ nhớ Adam bằng một bản $\theta$ thay cho hai; đặt `assert y.shape == (b,)` và tin rằng phép cực đại đã đúng chiều.
:::

### Bài tập 08.16. Quan sát cuối khi môi trường tự đặt lại

**Mức độ:** vận dụng. Mục tiêu học tập 1 và 2 của ghi chú: lưu đúng mẫu chuyển ở ranh giới lượt và đo sai lệch của mục tiêu khi lưu sai.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 3 (đoạn "Môi trường tự đặt lại" sau Ví dụ 08.10) và Mục 4 (Thuật toán 08.13, bước 3–4, đoạn sau thuật toán); Bài tập 08.2 (a) của ghi chú xét cùng lỗi trên đoạn mã; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.16 (Quan sát cuối khi môi trường tự đặt lại)
Một môi trường tự đặt lại (autoreset): lời gọi `step(a)` trả `obs, r, terminated, truncated, final_obs`. Khi lượt dừng ($Z\lor U=1$), môi trường tự đặt lại, `obs` là quan sát đầu của lượt mới và `final_obs` là quan sát cuối của lượt cũ; ngược lại `final_obs` là `None`. `final_obs` là một tên giả định; tên thật của trường này phụ thuộc thư viện và phiên bản. Cấu hình thu thập cắt ngắn mọi lượt sau $3$ bước. Nhật ký của năm lời gọi đầu, bắt đầu từ quan sát $o_0$; quan sát của lượt thứ hai ký hiệu $p_k$, của lượt thứ ba ký hiệu $c_k$:

| lời gọi | quan sát hiện hành | `obs` | `r` | `terminated` | `truncated` | `final_obs` |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | $o_0$ | $o_1$ | $1$ | sai | sai | `None` |
| 2 | $o_1$ | $o_2$ | $1$ | sai | sai | `None` |
| 3 | $o_2$ | $p_0$ | $1$ | sai | đúng | $o_3$ |
| 4 | $p_0$ | $p_1$ | $1$ | sai | sai | `None` |
| 5 | $p_1$ | $c_0$ | $1$ | đúng | sai | $p_2$ |

Hệ số chiết khấu $\gamma=0{,}99$; mạng mục tiêu cho $\max_{a'}Q_{\theta^-}(o_3,a')=60$, $\max_{a'}Q_{\theta^-}(p_0,a')=95$, $\max_{a'}Q_{\theta^-}(p_2,a')=5$, $\max_{a'}Q_{\theta^-}(c_0,a')=95$.

- (a) Viết năm mẫu chuyển $(O_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ mà Thuật toán 08.13 lưu vào $\mathcal D$ (bỏ qua $A_t$).
- (b) Một bản cài đặt lưu `obs` làm $O_{t+1}$ ở mọi lời gọi. Chỉ ra các mẫu bị lưu sai, và tính mục tiêu của chúng theo bản đúng và bản sai.
- (c) Một thư viện khác dùng quy ước tự đặt lại ở lời gọi kế tiếp: sau lời gọi làm lượt dừng, lời gọi `step` tiếp theo bỏ qua hành động, chỉ đặt lại môi trường và trả quan sát đầu của lượt mới với `r` bằng $0$ và hai cờ sai. Một chương trình lưu mọi lời gọi thành một mẫu chuyển thì lưu thêm một mẫu sau lời gọi 3. Viết mẫu đó, tính mục tiêu của nó, và giải thích vì sao không được lưu.
- (d) Đề xuất một phép kiểm tự động trên dữ liệu đã lưu, chỉ dùng các thành phần của mẫu chuyển, phát hiện được cả lỗi ở (b) lẫn lỗi ở (c) khi quan sát là vector số thực liên tục. Đề xuất thêm một phép kiểm bổ sung cho các mẫu nằm giữa một lượt, và cho biết nó có phát hiện hai lỗi đó không.
:::

::: hint Gợi ý Bài tập 08.16
Theo bước 3 của Thuật toán 08.13, $O_{t+1}$ là quan sát cuối của chính mẫu chuyển, lấy trước mọi lần đặt lại; theo bước 4, quan sát hiện hành của bước kế sau một lần đặt lại là quan sát đầu của lượt mới. Mặt nạ $1-Z$ chỉ xóa phần bootstrap của mẫu kết thúc. Với (d), so $O'$ của một mẫu với $O$ của mẫu lưu ngay sau nó.
:::

::: solution Lời giải Bài tập 08.16
**Câu (a).**

| mẫu | $O_t$ | $R_{t+1}$ | $O_{t+1}$ | $Z_{t+1}$ | $U_{t+1}$ |
| --- | --- | --- | --- | --- | --- |
| 1 | $o_0$ | $1$ | $o_1$ | $0$ | $0$ |
| 2 | $o_1$ | $1$ | $o_2$ | $0$ | $0$ |
| 3 | $o_2$ | $1$ | $o_3$ | $0$ | $1$ |
| 4 | $p_0$ | $1$ | $p_1$ | $0$ | $0$ |
| 5 | $p_1$ | $1$ | $p_2$ | $1$ | $0$ |

Mẫu 3 và mẫu 5 lấy $O_{t+1}$ từ `final_obs`; quan sát hiện hành sau lời gọi 3 là $p_0$, quan sát xuất phát của mẫu 4.

**Câu (b).** Bản sai lưu $O_{t+1}=p_0$ cho mẫu 3 và $O_{t+1}=c_0$ cho mẫu 5. Mẫu 3 bị cắt ngắn, $Z=0$, nên phần bootstrap còn trong mục tiêu: bản đúng cho $y=1+0{,}99\cdot60=60{,}4$, bản sai cho $y=1+0{,}99\cdot95=95{,}05$, lệch $0{,}99\cdot(95-60)=34{,}65$, vì mục tiêu lấy giá trị của quan sát đầu lượt mới, không nối với $o_2$. Mẫu 5 kết thúc, $Z=1$, nên cả hai bản cho $y=1$: mặt nạ xóa phần bootstrap và lỗi không lộ ra. Lỗi chỉ tác động lên mẫu bị cắt ngắn, như ghi chú nêu ở đoạn "Môi trường tự đặt lại".

**Câu (c).** Lời gọi kế tiếp sau lời gọi 3 xuất phát từ $o_3$ và trả $p_0$ với phần thưởng $0$, nên chương trình lưu thêm $(o_3,0,p_0,0,0)$. Mục tiêu của nó là $0+0{,}99\cdot95=94{,}05$ với mọi hành động được ghi, dù hành động không có tác dụng. Mẫu này không thuộc MDP, vì không có hành động nào đưa tác tử từ quan sát cuối của lượt cũ sang quan sát đầu của lượt mới (ghi chú, Mục 3). Mẫu đó kéo $Q_\theta(o_3,\cdot)$ về $94{,}05$, trong khi theo quy ước này mẫu 3 đã được lưu đúng là $(o_2,1,o_3,0,1)$. Chương trình phải bỏ qua lời gọi chỉ đặt lại.

**Câu (d).** Gọi mẫu $k$ và mẫu $k+1$ là hai mẫu lưu liên tiếp.

1. **Gián đoạn ở ranh giới lượt.** Nếu $Z_k\lor U_k=1$ thì $O'_k\ne O_{k+1}$. Ở (b), $O'_3=p_0=O_4$, nên phép kiểm báo lỗi tại mẫu 3 và cả tại mẫu 5 khi mẫu 6 bắt đầu từ $c_0$. Ở (c), mẫu thêm bắt đầu từ $o_3=O'_3$, nên phép kiểm báo lỗi tại mẫu 3.

2. **Liên tục trong lượt (bổ sung).** Nếu $Z_k\lor U_k=0$ thì $O'_k=O_{k+1}$. Phép kiểm này bắt lỗi ghi sai thứ tự hoặc mất mẫu, nhưng không phát hiện lỗi ở (b) hay (c): ở (b), các mẫu sai đều có $Z\lor U=1$; ở (c), mẫu thêm có $O'=p_0$ trùng $O$ của mẫu 4, nên điều kiện liên tục vẫn thỏa.

Với quan sát liên tục, quan sát đầu của lượt mới trùng quan sát cuối của lượt cũ với xác suất bằng $0$, nên phép kiểm thứ nhất không báo nhầm. Với quan sát rời rạc, phép kiểm cần thêm thông tin, chẳng hạn chỉ số lượt lưu kèm mẫu.

**Kiểm tra lại.** Số mẫu lưu bằng số lời gọi có hành động thật: năm mẫu cho năm lời gọi ở (a), không có mẫu nào cho lời gọi chỉ đặt lại ở (c). Ba lỗi thường gặp: kiểm lỗi trên mẫu kết thúc, thấy mục tiêu đúng và kết luận cài đặt đúng; gán `o = obs` trước khi lưu, làm mất `final_obs`; dùng $p_0$ làm quan sát hiện hành của mẫu 4 nhưng vẫn ghi $O_{t+1}=p_0$ cho mẫu 3.
:::

### Bài tập 08.17. Kiểm bốn cấu hình $N$, $N_{\mathrm{start}}$, $F$, $C$

**Mức độ:** vận dụng. Mục tiêu học tập 3 và 5 của ghi chú: đọc một cấu hình DQN qua hai bộ đếm và phát hiện cấu hình làm mất tác dụng của bộ nhớ phát lại hoặc mạng mục tiêu.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 2 (đoạn sau Định nghĩa 08.3 về $C$ lớn), Mục 3 (Định nghĩa 08.7, đoạn "Trong thực hành" sau Ví dụ 08.12), Mục 4 (Thuật toán 08.13 và các điều kiện trên đầu vào, Ví dụ 08.14), Mục 6 (đoạn về chu kỳ $C$ sau Ví dụ 08.23); cấu hình là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.17 (Kiểm bốn cấu hình $N$, $N_{\mathrm{start}}$, $F$, $C$)
Bốn cấu hình của Thuật toán 08.13, với $T$ là ngân sách bước môi trường:

| cấu hình | môi trường | $T$ | $N$ | $b$ |
| --- | --- | --- | --- | --- |
| A | CartPole | $10^5$ | $5\cdot10^4$ | $64$ |
| B | CartPole | $10^5$ | $10^3$ | $64$ |
| C | Lunar Lander | $5\cdot10^5$ | $10^5$ | $64$ |
| D | Flappy Bird | $10^6$ | $10^6$ | $32$ |

| cấu hình | $N_{\mathrm{start}}$ | $F$ | $C$ |
| --- | --- | --- | --- |
| A | $10^3$ | $1$ | $500$ |
| B | $2\cdot10^3$ | $1$ | $500$ |
| C | $10^4$ | $4$ | $10^5$ |
| D | $5\cdot10^4$ | $4$ | $10^3$ |

Chương trình của cấu hình D không có bước 9: nó gán $\theta^-\leftarrow\theta$ ở cuối mỗi vòng lặp có $t\bmod C=0$, kiểm ở mọi bước môi trường. Ba cấu hình còn lại theo đúng Thuật toán 08.13.

- (a) Với mỗi cấu hình, tính số bước tối ưu $K$ (công thức của Bài tập 08.12 (d)), số lần đồng bộ, số bước môi trường $\theta^-$ đứng yên giữa hai lần đồng bộ, và cho biết bộ nhớ có ghi đè không. Khi có ghi đè, tính tuổi của mẫu cũ nhất tính bằng bước tối ưu, $N/F$, và kỳ vọng số lần một mẫu được rút, $b/F$.
- (b) Chỉ ra cấu hình vi phạm một điều kiện trên đầu vào của Thuật toán 08.13 và hệ quả; cấu hình có mạng mục tiêu gần như không được làm mới và hệ quả theo ghi chú; cấu hình có chu kỳ đồng bộ thật khác chu kỳ khai báo, cùng giá trị thật tính bằng bước tối ưu.
- (c) Với cấu hình D, bộ nhớ không bao giờ ghi đè và $\lvert\mathcal D\rvert=t$. Giải thích vì sao kỳ vọng số lần rút một mẫu không còn là $b/F$. Dùng xấp xỉ $\sum_{t}b/t\approx(b/F)\ln(T/t_0)$ trên các bước tối ưu $t$ từ $t_0$ tới $T$, tính kỳ vọng số lần rút của mẫu ghi tại $t=1$ và của mẫu ghi tại $t=9\cdot10^5$.
- (d) Đề xuất một sửa đổi cho mỗi cấu hình B, C, D, mỗi sửa đổi chỉ đổi tham số gây vấn đề, và nêu các đại lượng phải đo để đánh giá sửa đổi.
:::

::: hint Gợi ý Bài tập 08.17
Điều kiện trên đầu vào là $b\le N_{\mathrm{start}}\le N$, và $\lvert\mathcal D\rvert$ không bao giờ vượt $N$. Với cấu hình D, mọi bước tối ưu xảy ra tại $t$ chia hết cho $F=4$, và $1\,000$ chia hết cho $4$. Với (c), một bước tối ưu tại $t$ rút $b$ lần đều từ $t$ mẫu, nên mỗi mẫu đang lưu được rút trung bình $b/t$ lần ở bước đó.
:::

::: solution Lời giải Bài tập 08.17
**Câu (a).**

| cấu hình | $K$ | số lần đồng bộ | $F\cdot C$ |
| --- | --- | --- | --- |
| A | $10^5-999=99\,001$ | $198$ | $500$ |
| B | $0$ | $0$ | — |
| C | $125\,000-2\,499=122\,501$ | $1$ | $4\cdot10^5$ |
| D (khai báo) | $250\,000-12\,499=237\,501$ | $237$ | $4\,000$ |

| cấu hình | ghi đè | $N/F$ | $b/F$ |
| --- | --- | --- | --- |
| A | có | $5\cdot10^4$ | $64$ |
| B | có | — | — |
| C | có | $2{,}5\cdot10^4$ | $16$ |
| D | không | — | — |

Cột $F\cdot C$ đếm bằng bước môi trường, cột $N/F$ bằng bước tối ưu.

Ở cấu hình A, $F=1$ nên bước tối ưu đầu tiên chạy tại $t=N_{\mathrm{start}}=1\,000$. Ở cấu hình B, $\lvert\mathcal D\rvert\le10^3<N_{\mathrm{start}}$ nên điều kiện tối ưu không bao giờ đúng.

**Câu (b).** Cấu hình B vi phạm $N_{\mathrm{start}}\le N$: không bước tối ưu nào chạy, và $\theta$ giữ giá trị khởi tạo suốt $10^5$ bước (ghi chú, đoạn sau Thuật toán 08.13). Cấu hình C chỉ đồng bộ một lần, sau bước tối ưu thứ $10^5$; trong $10^5$ bước tối ưu đầu, mục tiêu tính bằng mạng khởi tạo, nên $Q_\theta$ chỉ học giá trị một bước tính từ mạng ban đầu (ghi chú, đoạn sau Định nghĩa 08.3). Cấu hình D khai báo $C=10^3$ bước tối ưu, nhưng chương trình đồng bộ sau mỗi $1\,000$ bước môi trường, tức sau mỗi $1\,000/4=250$ bước tối ưu: chu kỳ thật là $250$, ngắn hơn bốn lần, với khoảng $950$ lần đồng bộ thay cho $237$.

**Câu (c).** Khi bộ nhớ không ghi đè, mẫu ghi sớm có mặt trong mọi bước tối ưu về sau, còn mẫu ghi muộn chỉ có mặt trong ít bước, và ở mỗi bước, xác suất trúng một mẫu là $1/t$, giảm theo $t$. Lập luận $b/F$ của Ví dụ 08.14 cần mỗi mẫu ở lại đúng $N$ bước môi trường với $\lvert\mathcal D\rvert=N$, điều không xảy ra ở đây. Mẫu ghi tại $t=1$ có mặt từ bước tối ưu đầu tiên $t_0=5\cdot10^4$:

$$
\begin{aligned}
\frac bF\ln\frac{T}{t_0}&=8\ln\frac{10^6}{5\cdot10^4}\\
&=8\ln20\approx23{,}97 .
\end{aligned}
$$

Mẫu ghi tại $t=9\cdot10^5$ cho $8\ln(10/9)\approx0{,}84$. Cộng trực tiếp $\sum b/t$ trên các bội của $4$ cho cùng hai số tới hai chữ số thập phân. Mẫu sinh bởi hành vi gần khởi tạo được rút nhiều hơn mẫu gần cuối khoảng $28$ lần, nên quy tắc ghi đè mẫu cũ nhất, vốn giữ $\mathcal D$ gần hành vi hiện tại (Định nghĩa 08.7), không có tác dụng.

**Câu (d).** Cấu hình B: đặt $N_{\mathrm{start}}=10^3$ hoặc tăng $N$ lên ít nhất $2\cdot10^3$, giữ $b\le N_{\mathrm{start}}\le N$. Cấu hình C: giảm $C$ để có nhiều lần đồng bộ, chẳng hạn $C=10^4$ cho $\lfloor122\,501/10^4\rfloor=12$ lần và $F\cdot C=4\cdot10^4$ bước môi trường. Cấu hình D: đếm $C$ theo $k_{\mathrm{opt}}$ như bước 9; nếu muốn bộ nhớ ghi đè, chọn $N<T$, với đánh đổi giữa dữ liệu gần hành vi hiện tại và tương quan trong mini-batch đã nêu ở ghi chú (Mục 3). Không sửa đổi nào có bảo đảm cải thiện. Mỗi sửa đổi được đánh giá như Bài tập 08.3 và 08.19: cùng tập hạt giống, lợi tức đánh giá của chính sách tham lam trên các lượt riêng, độ lớn của giá trị dự đoán trên một tập quan sát cố định, và độ phân tán giữa các lần chạy.

**Kiểm tra lại.** Với cấu hình C, $\lfloor(N_{\mathrm{start}}-1)/F\rfloor=\lfloor9\,999/4\rfloor=2\,499$, nên bước tối ưu đầu tiên chạy tại $t=10\,000$. Ba lỗi thường gặp: tính số lần đồng bộ bằng $T/C$ thay cho $K/C$, cho $5$ lần ở cấu hình C; bỏ giai đoạn chờ đủ $N_{\mathrm{start}}$ mẫu, cho $K=T/F$; coi $N=T$ là lựa chọn an toàn vì "không mất dữ liệu".
:::

### Bài tập 08.18. Đọc nhật ký huấn luyện DQN trên CartPole

**Mức độ:** vận dụng. Mục tiêu học tập 5 và 6 của ghi chú: phân biệt dấu hiệu phân kỳ với chính sách kém và với lỗi cài đặt, và nêu đúng phạm vi kết luận từ một số lần chạy.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 2 (Ví dụ 08.7), Mục 4 (Thuật toán 08.13), Mục 5 (đoạn "Trong thực hành" sau Định nghĩa 08.15), Mục 6 (Nhận xét 08.20, 08.21 và đoạn "Trong thực hành"), Tình huống 08.1; ghi chú bài giảng Bài 07, Nhận xét 07.39; nhật ký là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.18 (Đọc nhật ký huấn luyện DQN trên CartPole)
CartPole-v1: phần thưởng $+1$ ở mỗi bước, kể cả bước dẫn tới kết thúc; $Z=1$ khi góc của cột vượt $12^\circ$ hoặc vị trí của xe vượt $2{,}4$ về một phía; $U=1$ khi lượt đạt $500$ bước; $\gamma=0{,}99$. Lần chạy 1 và 2 dùng cùng một chương trình DQN với hai hạt giống; lần chạy 3 dùng một chương trình khác của cùng cấu hình. Sau mỗi $2\cdot10^4$ bước môi trường, nhật ký ghi ba đại lượng: $\bar G$, lợi tức không chiết khấu trung bình của $10$ lượt đánh giá bằng chính sách tham lam theo $Q_\theta$; $Q_{\max}$, giá trị lớn nhất của $\max_aQ_\theta(o,a)$ trên một tập cố định $200$ quan sát tham chiếu; $\bar L$, trung bình của $L_B$ trên $1\,000$ bước tối ưu gần nhất.

| $t$ | $2\cdot10^4$ | $4\cdot10^4$ | $6\cdot10^4$ | $8\cdot10^4$ | $10^5$ |
| --- | --- | --- | --- | --- | --- |
| lần 1: $\bar G$ | $25$ | $140$ | $320$ | $500$ | $500$ |
| lần 1: $Q_{\max}$ | $12$ | $45$ | $78$ | $92$ | $96$ |
| lần 1: $\bar L$ | $0{,}05$ | $0{,}4$ | $1{,}1$ | $0{,}9$ | $0{,}7$ |
| lần 2: $\bar G$ | $30$ | $180$ | $260$ | $120$ | $15$ |
| lần 2: $Q_{\max}$ | $15$ | $60$ | $140$ | $610$ | $4\,800$ |
| lần 2: $\bar L$ | $0{,}1$ | $0{,}8$ | $9$ | $150$ | $3\,000$ |
| lần 3: $\bar G$ | $20$ | $22$ | $25$ | $21$ | $23$ |
| lần 3: $Q_{\max}$ | $1{,}00$ | $1{,}00$ | $1{,}01$ | $1{,}00$ | $1{,}00$ |
| lần 3: $\bar L$ | $10^{-4}$ | $10^{-4}$ | $10^{-4}$ | $10^{-4}$ | $10^{-4}$ |

- (a) Coi cắt ngắn là giới hạn ngoài MDP, chứng minh $1\le q_\pi(s,a)\le100$ với mọi chính sách $\pi$ và mọi cặp $(s,a)$. Tính lợi tức chiết khấu của một lượt giữ cột đủ $500$ bước tính từ bước đầu, không kể phần sau giới hạn.
- (b) Xếp mỗi lần chạy vào một trong ba nhóm: có dấu hiệu phân kỳ; giá trị bị chặn và chính sách tốt; giá trị bị chặn nhưng chính sách kém. Nêu căn cứ.
- (c) Ở lần chạy 1, $\bar L$ tăng từ $0{,}05$ lên $1{,}1$ trong khi $\bar G$ tăng. Giải thích vì sao hai số này không mâu thuẫn.
- (d) Ở lần chạy 3, $Q_{\max}\approx1$ ở mọi mốc. Nêu một giả thuyết về lỗi cài đặt giải thích con số này, và một phép kiểm trên mini-batch xác nhận hoặc bác bỏ giả thuyết.
- (e) Nêu kết luận được phép rút ra từ lần chạy 1 và 2 về chương trình thứ nhất, và những gì cần thêm để kết luận về cấu hình.
:::

::: hint Gợi ý Bài tập 08.18
Với (a), $q_\pi(s,a)$ là kỳ vọng của $\sum_{k=0}^{\tau}\gamma^kR_{t+k+1}$ với $\tau\in\{0,1,2,\dots\}\cup\{\infty\}$ là số bước sau bước $t$ cho tới khi MDP kết thúc, $\tau=\infty$ khi MDP không bao giờ kết thúc, và mỗi phần thưởng bằng $1$. Với (b), dùng đoạn "Trong thực hành" sau Nhận xét 08.21. Với (d), so $Q_{\max}\approx1$ với phần thưởng một bước, xác định phần nào của mục tiêu trong Định nghĩa 08.4 có thể đã bị xóa, rồi dùng Nhận xét 08.5.
:::

::: solution Lời giải Bài tập 08.18
**Câu (a).** Lượt chỉ kết thúc khi MDP kết thúc, và mỗi bước, kể cả bước cuối, cho phần thưởng $1$. Với $\tau\in\{0,1,2,\dots\}\cup\{\infty\}$ là số bước sau bước $t$ cho tới khi MDP kết thúc, lợi tức là $\sum_{k=0}^{\tau}\gamma^k$. Khi $\tau$ hữu hạn, tổng này thuộc $[1,100)$; khi $\tau=\infty$, tổng bằng $\sum_{k\ge0}0{,}99^k=100$. Vậy lợi tức thuộc $[1,100]$, và lấy kỳ vọng theo $\pi$ được $1\le q_\pi(s,a)\le100$. Một lượt giữ cột đủ $500$ bước có lợi tức chiết khấu tính từ bước đầu $\sum_{k=0}^{499}0{,}99^k=(1-0{,}99^{500})/0{,}01\approx99{,}34$, gần cận $100$. Cận này cũng là cận của mọi mục tiêu đúng; một dự đoán ngoài $[1,100]$ chắc chắn sai (Tình huống 08.1).

**Câu (b).** Lần chạy 2 có dấu hiệu phân kỳ: tại $t=6\cdot10^4$, $Q_{\max}=140>100$, một giá trị không chính sách nào đạt được; sau đó $Q_{\max}$ tăng lên $610$ và $4\,800$ qua các lần đánh giá, cùng lúc $\bar G$ giảm còn $15$. Lần chạy 1 có giá trị bị chặn trong $[1,100]$ và chính sách tốt: $\bar G=500$, mức tối đa do giới hạn bước, ở hai mốc cuối. Lần chạy 3 có giá trị bị chặn nhưng chính sách kém: $\bar G$ quanh $22$ suốt quá trình. Theo Nhận xét 07.39 và đoạn "Trong thực hành" sau Nhận xét 08.21, chỉ lần chạy 2 có dấu hiệu phân kỳ; lần chạy 3 là hiện tượng khác.

**Câu (c).** $L_B$ đo độ khớp của dự đoán với mục tiêu hiện hành, không đo chất lượng của chính sách (đoạn "Trong thực hành" sau Định nghĩa 08.15). $Q_{\max}$ là dự đoán của mạng, không phải giá trị đúng. Giá trị đúng của chính sách tăng khi chính sách giữ cột lâu hơn: một lượt $25$ bước, ứng với $\bar G=25$ ở mốc đầu, có lợi tức chiết khấu tính từ bước đầu $(1-0{,}99^{25})/0{,}01\approx22{,}2$, còn một lượt $500$ bước có khoảng $99{,}3$. Dự đoán $Q_{\max}$ tăng theo, từ $12$ lên $96$. Tại mỗi mốc đồng bộ, mục tiêu của mọi mẫu chưa kết thúc đổi một lượng $\Delta y_i=\gamma\bigl[\max_{a'}Q_\theta(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\bigr]$ (Nhận xét 08.20), lớn khi giá trị đang tăng nhanh; dữ liệu mới trong $\mathcal D$ cũng đến từ các vùng quan sát chưa gặp. Hai cơ chế này làm sai số TD lớn hơn trong giai đoạn chính sách tốt lên; mức giảm của $\bar L$ ở hai mốc cuối phù hợp với việc $Q_{\max}$ gần ổn định ở mức $92$–$96$.

**Câu (d).** Giả thuyết: chương trình thứ hai cho mặt nạ $1-Z_i=0$ ở gần như mọi mẫu, chẳng hạn vì lưu cờ $Z$ là phủ định của cờ kết thúc, hoặc lưu một cờ luôn đúng. Khi đó $y_i=R_i=1$ với gần như mọi $i$; theo Nhận xét 08.5, hàm hồi quy tốt nhất cho mục tiêu cố định là $\mathbb E[y_i\mid O_i,A_i]\approx1$, nên $Q_\theta\approx1$ ở mọi cặp và $\bar L\approx0$. Giá trị đúng của chính sách hiện thời lớn hơn nhiều: một lượt $22$ bước có lợi tức chiết khấu tính từ bước đầu $(1-0{,}99^{22})/0{,}01\approx19{,}8$. Với mọi hành động có giá trị gần $1$, phép chọn tham lam chỉ dựa trên các chênh lệch nhỏ của mạng, nên chính sách không học được cách giữ cột. Phép kiểm: in tỉ lệ mẫu có $Z_i=1$ trong một mini-batch. Mỗi lượt có nhiều nhất một mẫu kết thúc, nên với lượt dài khoảng $22$ bước, tỉ lệ đúng xấp xỉ $1/22\approx0{,}045$; tỉ lệ gần $1$ xác nhận giả thuyết. Bổ sung một phép tính tay mục tiêu của một mẫu chưa kết thúc như Ví dụ 08.7 và so với giá trị chương trình trả về.

**Câu (e).** Với chương trình thứ nhất, hai hạt giống cho hai kết cục khác nhau: một lần giá trị bị chặn và chính sách tốt, một lần có dấu hiệu phân kỳ. Kết luận được phép: với cấu hình và chương trình này, kết quả phụ thuộc hạt giống, và cấu hình có thể cho dấu hiệu phân kỳ. Hai lần chạy không đủ để ước lượng tỉ lệ lần chạy phân kỳ hay lợi tức trung bình; cần nhiều hạt giống với cùng giao thức đánh giá, báo trung bình, độ phân tán và số lần chạy có dấu hiệu phân kỳ (Bài tập 08.3 (d)). Lần chạy 1 không chứng minh hội tụ, vì cửa sổ quan sát hữu hạn và Nhận xét 08.21 không cho bảo đảm. Lần chạy 3 nói về lỗi của chương trình thứ hai, không về thuật toán; chương trình đó phải được sửa và chạy lại trước khi đưa vào so sánh.

**Kiểm tra lại.** $Q_{\max}$ của lần chạy 1 nằm trong $[1,100]$ ở mọi mốc. Ba lỗi thường gặp: kết luận lần chạy 3 phân kỳ vì chính sách kém; kết luận lần chạy 1 kém dần vì $\bar L$ tăng; dùng lợi tức của các lượt huấn luyện có thăm dò thay cho $\bar G$.
:::

### Bài tập 08.19. So sánh ghép cặp hai bộ tối ưu trên Lunar Lander

**Mức độ:** vận dụng. Mục tiêu học tập 4 và 5 của ghi chú: đánh giá một lựa chọn bộ tối ưu bằng thí nghiệm có kiểm soát và nêu đúng phạm vi kết luận.

**Nguồn:** ghi chú bài giảng Bài 08, Mục 5 (đoạn sau bảng so sánh ba bộ tối ưu về thí nghiệm có kiểm soát, đoạn "Giới hạn"), Mục 4 (đoạn "Trong thực hành" sau Ví dụ 08.15 về đánh giá), Mục 6 (Nhận xét 08.21); Bài tập 08.3 của ghi chú (thiết kế thí nghiệm loại bỏ); bài giảng gốc (2025–2026), trang 28 và câu hỏi thảo luận 2 ở trang 36; lợi tức là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 08.19 (So sánh ghép cặp hai bộ tối ưu trên Lunar Lander)
Một thí nghiệm so DQN dùng RMSprop với DQN dùng Adam trên Lunar Lander. Hai nhánh giữ cùng kiến trúc mạng, ngân sách bước môi trường, lịch $\epsilon_{\mathrm{exp}}$, $N$, $b$, $N_{\mathrm{start}}$, $F$, $C$ và tập hạt giống đánh số $k=0,\dots,5$; tốc độ học $\eta$ của mỗi nhánh được chỉnh với cùng số lần thử ($8$ lần) trên các hạt giống riêng $100,\dots,107$. Sau huấn luyện, mỗi lần chạy được đánh giá bằng lợi tức trung bình của $20$ lượt theo chính sách tham lam, trên cùng tập lượt đánh giá:

| hạt giống $k$ | RMSprop | Adam |
| --- | --- | --- |
| $0$ | $182$ | $205$ |
| $1$ | $95$ | $120$ |
| $2$ | $210$ | $198$ |
| $3$ | $160$ | $190$ |
| $4$ | $230$ | $245$ |
| $5$ | $140$ | $150$ |

- (a) Tính trung bình và độ lệch chuẩn mẫu của mỗi nhánh; các hiệu ghép cặp $d_k=G_{\mathrm{Adam},k}-G_{\mathrm{RMSprop},k}$, trung bình $\bar d$, độ lệch chuẩn mẫu $s_d$, sai số chuẩn $\mathrm{SE}=s_d/\sqrt6$ và khoảng $\bar d\pm2{,}571\,\mathrm{SE}$, với $2{,}571$ là phân vị $0{,}975$ của phân phối Student năm bậc tự do.
- (b) Tính sai số chuẩn của hiệu hai trung bình khi bỏ ghép cặp, $\sqrt{s_{\mathrm{RMSprop}}^2/6+s_{\mathrm{Adam}}^2/6}$, so với $\mathrm{SE}$ ở (a), và giải thích chênh lệch.
- (c) Viết kết luận được phép rút ra, và nêu ba kết luận không được phép rút ra từ thí nghiệm này.
- (d) Một giao thức khác chỉnh $\eta$ của Adam với $20$ lần thử và của RMSprop với $3$ lần thử, đo lợi tức trên các lượt huấn luyện có thăm dò, và chỉ báo hạt giống tốt nhất của mỗi nhánh. Nêu ba lỗi của giao thức này.
:::

::: hint Gợi ý Bài tập 08.19
Độ lệch chuẩn mẫu chia cho $n-1=5$. Với (b), $\operatorname{Var}(d_k)=\operatorname{Var}(G_{\mathrm{Adam},k})+\operatorname{Var}(G_{\mathrm{RMSprop},k})-2\operatorname{Cov}(G_{\mathrm{Adam},k},G_{\mathrm{RMSprop},k})$; tính hệ số tương quan của hai cột theo hạt giống. Khoảng ở (a) dựa trên giả thiết các hiệu $d_k$ độc lập và xấp xỉ phân phối chuẩn.
:::

::: solution Lời giải Bài tập 08.19
**Câu (a).** RMSprop có trung bình $169{,}5$ và độ lệch chuẩn $48{,}9$; Adam có trung bình $184{,}7$ và độ lệch chuẩn $43{,}9$. Các hiệu ghép cặp là $d=(23;\,25;\,-12;\,30;\,15;\,10)$, nên

$$
\begin{aligned}
\bar d&=\frac{91}6\approx15{,}17,\\
s_d&\approx15{,}12,\\
\mathrm{SE}&=\frac{s_d}{\sqrt6}\approx6{,}17,
\end{aligned}
$$

và khoảng $15{,}17\pm2{,}571\cdot6{,}17$ là $[-0{,}70;\,31{,}04]$. Năm trong sáu hạt giống cho Adam cao hơn, nhưng khoảng chứa $0$.

**Câu (b).** Bỏ ghép cặp, sai số chuẩn là $\sqrt{48{,}92^2/6+43{,}92^2/6}\approx26{,}84$, lớn gấp khoảng $4{,}35$ lần $\mathrm{SE}$ ở (a). Hai cột có hệ số tương quan khoảng $0{,}95$ theo hạt giống: hạt giống $1$ thấp ở cả hai nhánh, hạt giống $4$ cao ở cả hai. Phần biến thiên do hạt giống, chung cho hai nhánh, triệt tiêu trong hiệu $d_k$ qua số hạng $-2\operatorname{Cov}$, nên so ghép cặp cho ước lượng chính xác hơn với cùng sáu lần chạy mỗi nhánh. Điều này cần hai nhánh dùng chung tập hạt giống và chung tập lượt đánh giá, như thiết kế của đề.

**Câu (c).** Kết luận được phép: trên Lunar Lander, với cấu hình, ngân sách và cách chỉnh $\eta$ này, Adam cho lợi tức đánh giá trung bình cao hơn RMSprop $15{,}2$ trên sáu hạt giống, nhưng khoảng $[-0{,}7;\,31{,}0]$ chứa $0$, nên dữ liệu chưa loại được khả năng hai nhánh có cùng lợi tức trung bình; cần thêm hạt giống để thu hẹp khoảng. Ba kết luận không được phép:

1. Adam tốt hơn RMSprop cho DQN nói chung, trên môi trường hoặc cấu hình khác.
2. Adam làm DQN ổn định hay hội tụ: bộ tối ưu không đổi công thức mục tiêu, cách thu thập dữ liệu hay lớp hàm, nên ba yếu tố của bộ ba bất ổn còn nguyên (Định nghĩa 08.15, Nhận xét 08.21).
3. Khác biệt đến từ "hội tụ nhanh hơn" của Adam: thí nghiệm chỉ đo lợi tức sau ngân sách cố định, không đo tốc độ hội tụ của $\theta$.

**Câu (d).** Thứ nhất, ngân sách chỉnh $\eta$ không bằng nhau, nên nhánh được chỉnh $20$ lần có lợi thế không đến từ bộ tối ưu. Thứ hai, lợi tức của lượt huấn luyện sinh bởi hành vi $\epsilon_{\mathrm{exp}}$-tham lam và trộn nhiều phiên bản $\theta$, nên không đo chất lượng của chính sách đầu ra (ghi chú, đoạn "Trong thực hành" sau Ví dụ 08.15). Thứ ba, chỉ báo hạt giống tốt nhất che độ phân tán giữa các lần chạy, và với các số của bảng, cho hiệu $245-230=15$ dù các hạt giống khác cho hiệu từ $-12$ đến $30$.

**Kiểm tra lại.** Tổng các hiệu là $23+25-12+30+15+10=91$, khớp $\bar d=91/6$. Ba lỗi thường gặp: chia độ lệch chuẩn cho $n=6$ thay cho $n-1=5$, cho $s_d\approx13{,}80$; dùng $1{,}96$ thay cho $2{,}571$ với sáu cặp; kết luận "Adam tốt hơn" từ $\bar d>0$ mà không báo khoảng.
:::

## Tài liệu tham khảo

- Tạ Việt Cường (2026). *Bài giảng 8: Deep Q-Learning* (`lecture8-dqn.pdf`), bài giảng gốc của học phần (2025–2026), 36 trang: trang 14–17 cho Bài tập 08.6; trang 19, 30, 32 cho 08.10; trang 21 cho 08.7; trang 23–26 cho 08.13; trang 28, 32, 33 và câu hỏi thảo luận ở trang 36 cho 08.8 và 08.19; trang 29, 31, 33 cho 08.14. Học phần 2025–2026 không có phiếu bài tập tuần 8.
- Ghi chú bài giảng Bài 08: các định nghĩa, nhận xét, mệnh đề, thuật toán và ví dụ dẫn trong từng bài; Bài tập 08.1–08.5 thuộc mục "Bài tập củng cố" của ghi chú và không chép lại ở đây.
- Ghi chú bài giảng Bài 07: Ví dụ 07.1, Bài tập 07.20 (quan sát của Lunar Lander và Flappy Bird) cho Bài tập 08.15; Mệnh đề 07.37 cho 08.14; Nhận xét 07.39 cho 08.8, 08.18.
- Mnih, V. và cộng sự (2015). Human-level control through deep reinforcement learning. *Nature* 518, 529–533: mục Methods (kiến trúc trả vector giá trị) cho Bài tập 08.6; Extended Data Table 1 ($N$, $b$, $N_{\mathrm{start}}$, $F$, $C$) cho 08.10, 08.12.
- Sutton, R. S. và Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §9.3 (bán gradient) và §11.5 (gradient dư) cho Bài tập 08.11; §11.2, §11.3 (phản ví dụ phân kỳ, bộ ba bất ổn) cho 08.14.
- Kingma, D. P. và Ba, J. (2015). Adam: A Method for Stochastic Optimization. *ICLR*: Bài tập 08.13.
- Goodfellow, I., Bengio, Y. và Courville, A. (2016). *Deep Learning*, MIT Press: §8.5.2, §8.5.3 (RMSprop, Adam) cho Bài tập 08.13.
- Pardo, F., Tavakoli, A., Levdik, V. và Kormushev, P. (2018). Time Limits in Reinforcement Learning. *ICML*: cờ cắt ngắn và giới hạn thời gian thuộc nhiệm vụ, Bài tập 08.7.
- Farama Foundation. Tài liệu môi trường `CartPole-v1` của thư viện Gymnasium: phần thưởng, điều kiện kết thúc và giới hạn $500$ bước, dùng ở Bài tập 08.15, 08.17, 08.18 qua Tình huống 08.1 của ghi chú.
