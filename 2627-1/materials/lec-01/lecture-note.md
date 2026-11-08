# Bài 01 — Giới thiệu Học tăng cường

Học tăng cường (reinforcement learning) nghiên cứu cách một tác tử (agent) chọn hành động khi đánh giá chỉ đến sau cả chuỗi hành động và dữ liệu do chính các hành động đó sinh ra. Trên hai ví dụ nhỏ tính được bằng tay, một robot dọn dãy bốn ô và một thế cờ Tic-tac-toe, chúng ta dựng bộ khái niệm dùng cho cả học phần. Chúng ta chỉ xét lượt (episode) hữu hạn, không dùng hệ số chiết khấu (discount factor), và không giả thiết thông tin tác tử nhận ở một bước đủ để dự báo tương lai, tức không giả thiết tính Markov (Markov property).

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Mô tả một bài toán ra quyết định bằng tác tử, môi trường (environment), trạng thái (state), quan sát (observation), hành động (action) và phần thưởng (reward); chỉ ra một trường hợp trạng thái khác quan sát (Bài tập 01.1, 01.11, 01.13, 01.15, 01.16).
2. Phân biệt phần thưởng với nhãn của học có giám sát (supervised learning) và nhận diện các dấu hiệu của một bài toán Học tăng cường (Bài tập 01.2, 01.15).
3. Tính lợi tức (return) $G_t$ của một lượt hữu hạn và dùng hệ thức $G_t=R_{t+1}+G_{t+1}$ để tính ngược (Bài tập 01.3, 01.4, 01.10, 01.13, 01.14).
4. Phân biệt chính sách (policy), hàm giá trị (value function) và mô hình (model); tính giá trị $v_\pi(h)$ của một lịch sử trong bài toán có lượt ngắn trực tiếp từ định nghĩa (Bài tập 01.5, 01.9, 01.11, 01.12, 01.13, 01.15, 01.16).
5. Nhận diện thăm dò (exploration) và khai thác (exploitation) khi ước lượng còn dựa trên ít mẫu (Bài tập 01.6, 01.15).
6. Mô hình hóa Tic-tac-toe thành bài toán Học tăng cường, xác định tập hành động hợp lệ và tính nước khai thác một bước (Bài tập 01.7, 01.8).

Bài tập 01.1–01.11 nằm trong ghi chú; Bài tập 01.1–01.8 có lại trong [tệp bài tập](material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html), cùng với Bài tập 01.12–01.16.

## Kiến thức tiên quyết

Số hiệu `01.k` chỉ Bài 01 (ghi chú này và tệp bài tập); Định nghĩa, Mệnh đề và Nhận xét dùng chung một bộ đếm, Ví dụ, Bài tập và Tình huống mỗi loại một bộ đếm riêng.

- **Biến ngẫu nhiên rời rạc và kỳ vọng.** Một biến ngẫu nhiên $X$ nhận hữu hạn giá trị có kỳ vọng $\mathbb E[X]=\sum_x x\,\Pr(X=x)$. Kỳ vọng tuyến tính: $\mathbb E[X+Y]=\mathbb E[X]+\mathbb E[Y]$ và $\mathbb E[cX]=c\,\mathbb E[X]$ với mọi hằng số $c$.
- **Kỳ vọng có điều kiện** (conditional expectation). Với sự kiện $\{Y=y\}$ có xác suất dương, $\mathbb E[X\mid Y=y]=\sum_x x\,\Pr(X=x\mid Y=y)$. Công thức kỳ vọng toàn phần (law of total expectation), dạng rời rạc của tính chất tháp (tower property), là

  $$
  \mathbb E[X\mid Y=y]=\sum_{z}\Pr(Z=z\mid Y=y)\,\mathbb E[X\mid Y=y,Z=z],
  $$

  trong đó tổng lấy trên các $z$ có $\Pr(Z=z,Y=y)>0$.
- **Học có giám sát.** Dữ liệu là $n$ cặp $(x_i,y_i)$, trong đó nhãn $y_i$ là đầu ra đúng cho đầu vào $x_i$. Hàm dự đoán (predictor) $f$ được chọn để làm nhỏ mất mát trung bình $\frac1n\sum_{i=1}^n\ell(f(x_i),y_i)$, trong đó $\ell$ là hàm mất mát (loss function). Ta giả thiết các cặp độc lập và cùng phân phối (independent and identically distributed, i.i.d.); giả thiết này cho phép coi mất mát trung bình trên dữ liệu là ước lượng của mất mát trên phân phối dữ liệu.

## Bảng ký hiệu

Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$ | bước quyết định | $\{0,1,2,\dots\}$ |
| $T$ | thời điểm kết thúc lượt | biến ngẫu nhiên nguyên dương, $T\le L$ |
| $L$ | số hành động tối đa của một lượt | số nguyên dương cho trước |
| $\mathcal S$, $S_t$, $s$ | tập trạng thái; trạng thái tại bước $t$; một giá trị cụ thể | tập hữu hạn; biến ngẫu nhiên; phần tử của $\mathcal S$ |
| $\mathcal O$, $O_t$, $o$ | tập quan sát; quan sát tại bước $t$; một giá trị cụ thể | tập hữu hạn; biến ngẫu nhiên; phần tử của $\mathcal O$ |
| $\mathcal A(s)$, $A_t$, $a$ | tập hành động hợp lệ tại $s$; hành động tại bước $t$; một hành động | tập hữu hạn khác rỗng; $A_t\in\mathcal A(S_t)$ |
| $R_{t+1}$ | phần thưởng của chuyển (transition) từ bước $t$ sang bước $t+1$ | số thực, bị chặn |
| $H_t$, $h$ | lịch sử (history) đến bước $t$; một giá trị cụ thể | dãy gồm $3t+1$ phần tử (Định nghĩa 01.2) |
| $G_t$ | lợi tức từ bước $t$ | biến ngẫu nhiên thực; $G_T=0$ |
| $\pi(a\mid h)$ | chính sách của tác tử | phân phối trên tập hành động hợp lệ, với mỗi $h$ |
| $\pi_1$, $\pi_u$, $\pi_w$ | ba chính sách cụ thể: $\pi_1$ cho robot sang phải khi thấy sạch và hút khi thấy bẩn (Mục 4.1); $\pi_u$ chọn đều; $\pi_w$ thắng ngay nếu có, nhiều nước thắng thì chọn đều trong số đó, nếu không thì chọn đều ($\pi_u$, $\pi_w$: Ví dụ 01.6) | chính sách |
| $\sigma(\cdot\mid\tilde s)$ | chính sách của đối thủ O tại thế cờ $\tilde s$ | phân phối trên các ô trống (Định nghĩa 01.18) |
| $\mathbb E_\pi$, $\mathbb E$ | kỳ vọng khi tác tử theo $\pi$; kỳ vọng chỉ theo luật của môi trường, khi hành động đã cố định | số thực |
| $v_\pi(h)$, $v_\pi(s)$ | giá trị của lịch sử $h$; giá trị của thế cờ $s$ (Mục 5) | $\mathbb R$ |
| $N(a)$ | số lần hành động $a$ đã được chọn trong bài toán chọn lặp lại một bước (Mục 4.4) | số nguyên dương |
| $\bar r(a)$ | trung bình mẫu của các phần thưởng nhận được khi chọn $a$ (Định nghĩa 01.16) | số thực |
| $a^*$ | nước khai thác một bước | phần tử của $\mathcal A(s)$ |
| $\gamma$ | hệ số chiết khấu, không dùng trong chương | tương ứng $\gamma=1$ |

Chỉ số thời gian của phần thưởng đi theo chuyển: tác tử chọn $A_t$ ở bước $t$, rồi môi trường trả $R_{t+1}$ cùng quan sát $O_{t+1}$, nên $R_{t+1}$ là hậu quả của bước $t$, theo quy ước của Sutton và Barto (2018, §3.1). Lượt kết thúc tại $T$; lợi tức tại thời điểm kết thúc bằng $0$, nên giá trị của một lịch sử đã kết thúc cũng bằng $0$. Tên hành động và tên quan sát viết chữ đứng ($\text{phải}$, $\text{sạch}$); chữ nghiêng dành cho biến. Trong Tic-tac-toe, chữ O đứng chỉ quân cờ của đối thủ, còn $O_t$ nghiêng chỉ quan sát.

Ký hiệu của học phần theo Sutton và Barto (2018). Giáo trình *Học máy thống kê* viết giá trị là $V^\pi$ và mô tả quá trình quyết định Markov (Markov decision process, MDP) bằng bộ $\langle S,A,T,R,\gamma\rangle$; trong học phần này, $v_\pi$ ứng với $V^\pi$, và chữ $T$ chỉ thời điểm kết thúc lượt, không chỉ hàm chuyển. Mọi bộ số của robot dọn dãy bốn ô và của các thế cờ là số liệu sư phạm tự xây dựng.

<!-- note-topic-id: lec-01-topic-01 -->
## 1. Tác tử học từ tương tác

Học có giám sát dựa trên bốn điều kiện:

- các cặp có nhãn có sẵn trước khi học, và mỗi nhãn cho biết đầu ra đúng;
- sai lệch được đo ngay trên từng mẫu;
- thứ tự các mẫu không ảnh hưởng tới kết quả;
- hàm dự đoán đang học không làm thay đổi dữ liệu nó sẽ nhận.

Bài toán sau không thỏa các điều kiện đó. Một robot hút bụi đứng ở ô 1 của một dãy bốn ô sàn đánh số từ 1 đến 4, và chỉ ô 4 có rác. Ở mỗi bước, robot chọn một trong ba hành động: sang trái, sang phải, hoặc hút tại ô đang đứng. Cảm biến của robot chỉ báo ô đang đứng sạch hay bẩn, không báo robot đang ở ô nào. Robot nhận $+1$ khi hút được rác ở ô 4, và lượt dừng ngay khi đó; mọi bước khác cho $0$; nếu sau năm hành động robot vẫn chưa hút được rác thì lượt bị cắt.

Không ai cho robot biết hành động đúng ở từng bước. Ba lần sang phải đầu tiên đều nhận $0$, và tín hiệu duy nhất cho thấy chúng có ích là phần thưởng $+1$ nhận sau hành động thứ tư; nếu robot sang trái hai lần ở đầu lượt, ba hành động còn lại không đủ để tới ô 4 và hút, và phần thưởng đó không đến. Để xử lý bài toán này, chúng ta cần một ngôn ngữ nói rõ:

- ai chọn hành động;
- ai sinh dữ liệu;
- dữ liệu gồm những gì;
- hậu quả dài hạn được đo bằng đại lượng nào.

Qua năm mục, chúng ta dựng ngôn ngữ đó, rồi dùng nó để chọn một nước đi (move) trong Tic-tac-toe bằng phép tính tay.

![Sơ đồ năm khối nối bằng mũi tên từ trái sang phải. Mục 1, tương tác, với các đại lượng S t, O t, A t, H t. Mục 2, tín hiệu học, ghi phần thưởng R t+1 không là nhãn. Mục 3, lợi tức, ghi G t bằng R t+1 cộng G t+1. Mục 4 ghi chính sách pi, giá trị v pi, mô hình, thăm dò và khai thác. Mục 5, Tic-tac-toe, ghi nước khai thác một bước a sao. Dòng trên cùng ghi bài toán trung tâm: chọn hành động khi đánh giá chỉ đến sau cả chuỗi hành động. Dòng dưới cùng ghi Bài 02 thêm tính Markov và hệ số chiết khấu gamma.](img/lec-01/chapter-map.svg)

Sơ đồ trên đọc từ trái sang phải; mỗi khối ghi các đại lượng mới của khối đó, và các khối sau dùng lại chúng. Lịch sử $H_t$ là đầu vào của chính sách $\pi$, phần thưởng $R_{t+1}$ được cộng thành lợi tức $G_t$, và khối cuối là phép chọn nước $a^*$, nơi các đại lượng trước được dùng cùng lúc.

### 1.1 Một lượt của robot dọn dãy bốn ô

![Bốn ô sàn xếp thành một hàng, đánh số 1 đến 4 từ trái sang phải. Robot đứng ở ô 1, chỉ ô 4 có rác. Phía trên ghi luật hành động: phải là sang ô bên phải, ở ô 4 thì đứng yên; trái là sang ô bên trái, ở ô 1 thì đứng yên; hút là hút tại ô đang đứng. Phía dưới ghi: hút ở ô 4 khi còn rác cho phần thưởng cộng 1 và kết thúc lượt, các bước khác cho 0, cảm biến báo sạch hoặc bẩn.](img/lec-01/robot-four-cells.svg)

Trên hình, robot cần đi qua hai ô ở giữa rồi mới hút được rác; dòng chữ phía dưới ghi luật phần thưởng và cảm biến, hai thứ robot không điều khiển được.

::: example Ví dụ 01.1 (Một lượt của robot dọn dãy bốn ô)
**Dữ kiện.**

- Dãy bốn ô đánh số 1 đến 4; robot bắt đầu ở ô 1; chỉ ô 4 có rác.
- Hành động $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ giữ nguyên vị trí và làm sạch ô đang đứng.
- Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$.
- Cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$ cho ô đang đứng.
- Lượt bị cắt sau $L=5$ hành động.
- Robot lần lượt chọn $\text{phải}$, $\text{phải}$, $\text{phải}$, $\text{hút}$.

**Ghi từng bước.** Ở mỗi bước $t$, robot nhận quan sát $O_t$, chọn hành động $A_t$, rồi môi trường trả phần thưởng $R_{t+1}$ và đưa robot tới vị trí mới.

| $t$ | Vị trí | $O_t$ | $A_t$ | $R_{t+1}$ | Vị trí sau hành động |
|---:|---|---|---|---:|---|
| $0$ | ô 1 | $\text{sạch}$ | $\text{phải}$ | $0$ | ô 2 |
| $1$ | ô 2 | $\text{sạch}$ | $\text{phải}$ | $0$ | ô 3 |
| $2$ | ô 3 | $\text{sạch}$ | $\text{phải}$ | $0$ | ô 4 |
| $3$ | ô 4 | $\text{bẩn}$ | $\text{hút}$ | $+1$ | ô 4, lượt kết thúc |

**Kết quả.** Lượt kết thúc sau bốn hành động, nên thời điểm kết thúc là $T=4$, nhỏ hơn giới hạn $L=5$. Dãy phần thưởng là $(R_1,R_2,R_3,R_4)=(0,0,0,1)$.

**Đổi một hành động.** Nếu ở bước $0$ robot chọn $\text{trái}$, nó đứng yên ở ô 1 và nhận $O_1=\text{sạch}$, $R_1=0$. Khi đó robot cần thêm ba lần $\text{phải}$ và một lần $\text{hút}$, tổng cộng năm hành động, nên lượt kết thúc đúng ở giới hạn với $T=5$. Nếu robot chọn $\text{trái}$ hai lần liên tiếp ở đầu lượt, ba hành động còn lại không đủ để tới ô 4 và hút, nên lượt bị cắt ở $T=5$ với mọi phần thưởng bằng $0$.

**Kiểm tra lại.** Dòng cuối của bảng là bước duy nhất robot đứng ở ô 4 khi ô 4 còn rác và chọn $\text{hút}$, đúng điều kiện cho phần thưởng $+1$. Ba vị trí trước đó đều là ô sạch, khớp với ba quan sát $\text{sạch}$.
:::

Hành động của robot quyết định vị trí và các quan sát về sau: với $A_0=\text{trái}$, $O_3$ là $\text{sạch}$ (ô 3) thay vì $\text{bẩn}$ (ô 4).

Bảng còn ghi hai loại thông tin khác nhau: cột "Vị trí" là điều xảy ra trong môi trường, cột $O_t$ là điều robot biết.

### 1.2 Tác tử, môi trường và vòng tương tác

Một cách trực quan, bài toán của Ví dụ 01.1 có hai bên. Một bên ra quyết định và chỉ điều khiển được lựa chọn của chính nó. Bên kia nhận lựa chọn đó rồi quyết định điều gì xảy ra tiếp theo, gồm phần thưởng và dữ liệu mà bên ra quyết định sẽ thấy.

![Hai khối chữ nhật. Khối trái ghi tác tử, khối phải ghi môi trường. Mũi tên trên đi từ tác tử sang môi trường, ghi hành động. Mũi tên dưới đi từ môi trường về tác tử, ghi quan sát, phần thưởng.](img/lec-01/agent-environment.svg)

Hình trên vẽ hai chiều trao đổi. Mũi tên trên mang hành động $A_t$; mũi tên dưới mang phần thưởng $R_{t+1}$ và quan sát $O_{t+1}$ của bước kế tiếp, có chỉ số lớn hơn một đơn vị vì chúng đến sau hành động.

::: definition Định nghĩa 01.1 (Tác tử, môi trường, vòng tương tác)
Thời gian được chia thành các bước rời rạc $t=0,1,2,\dots$.

**Tác tử** là bộ phận ra quyết định. Ở mỗi bước $t$, tác tử nhận quan sát $O_t$, thuộc một tập hữu hạn $\mathcal O$, rồi chọn một hành động $A_t$ trong tập hành động hợp lệ ở bước đó.

**Môi trường** gồm mọi thứ nằm ngoài tác tử. Sau khi nhận $A_t$, môi trường trả về một số thực $R_{t+1}$, gọi là phần thưởng, và quan sát kế tiếp $O_{t+1}$.

**Vòng tương tác** là dãy luân phiên

$$
O_0,\ A_0,\ R_1,\ O_1,\ A_1,\ R_2,\ O_2,\ \dots
$$

sinh ra khi hai thao tác trên được lặp lại. Dãy dừng khi lượt kết thúc, tại thời điểm ký hiệu là $T$.
:::

Tác tử chỉ quyết định $A_t$; môi trường quyết định $R_{t+1}$ và $O_{t+1}$, có thể một cách ngẫu nhiên. Ranh giới giữa hai bên đặt ở giới hạn điều khiển của tác tử: trong Ví dụ 01.1, tác tử là bộ chọn hành động của robot, còn dãy ô, rác, cảm biến và luật phần thưởng thuộc môi trường. Nhầm lẫn thường gặp là coi cả robot, kể cả cảm biến, là tác tử; cảm biến thuộc môi trường vì tác tử không điều khiển được điều cảm biến báo.

So với học có giám sát, đầu ra $A_t$ làm thay đổi đầu vào $O_{t+1}$ của bước sau.

### 1.3 Trạng thái, quan sát và lịch sử

Trong bảng của Ví dụ 01.1, robot ở ô 1, ô 2 và ô 3 đều nhận cùng quan sát $\text{sạch}$. Một cách trực quan, môi trường ở ba tình huống khác nhau, nhưng tác tử thấy cùng một dữ liệu; điều tác tử có để phân biệt chúng là những gì nó đã làm và đã thấy từ đầu lượt.

::: definition Định nghĩa 01.2 (Trạng thái, quan sát, lịch sử)
**Luật của môi trường** (environment dynamics) là quy tắc, có thể ngẫu nhiên, cho biết phần thưởng và cấu hình kế tiếp của môi trường khi biết cấu hình hiện tại và hành động.

**Trạng thái** của môi trường tại bước $t$ là biến ngẫu nhiên $S_t$ nhận giá trị trong một tập hữu hạn $\mathcal S$. Giá trị của $S_t$ mô tả cấu hình của môi trường mà luật của môi trường dùng tới: biết $S_t$ và $A_t$ thì xác định được phân phối của phần thưởng $R_{t+1}$ và trạng thái $S_{t+1}$.

**Quan sát** $O_t\in\mathcal O$ là phần thông tin về môi trường mà tác tử nhận ở bước $t$; $O_t$ là một hàm, có thể ngẫu nhiên, của $S_t$. Khi $O_t=S_t$ ở mọi bước, ta nói tác tử quan sát đầy đủ (full observability).

**Lịch sử** đến bước $t$ là dãy

$$
\begin{aligned}
H_t&=(O_0,A_0,R_1,O_1,\dots,A_{t-1},R_t,O_t),\\
H_0&=(O_0),
\end{aligned}
$$

gồm mọi quan sát, hành động và phần thưởng từ đầu lượt tới bước $t$. Một giá trị cụ thể của $H_t$ được ký hiệu là $h$.

**Tập hành động hợp lệ** $\mathcal A(s)$ là tập hữu hạn khác rỗng các hành động được phép khi môi trường ở trạng thái $s$, và $A_t\in\mathcal A(S_t)$. Trong chương này, hoặc $\mathcal A(s)$ không phụ thuộc $s$, hoặc tác tử quan sát đầy đủ, nên tác tử luôn biết tập hành động hợp lệ từ lịch sử của nó.
:::

Áp vào robot của Ví dụ 01.1, trạng thái là cặp (vị trí, tình trạng ô 4), nên $\mathcal S=\{1,2,3,4\}\times\{\text{còn rác},\text{hết rác}\}$ có tám phần tử và $S_0=(1,\text{còn rác})$. Tập quan sát là $\mathcal O=\{\text{sạch},\text{bẩn}\}$, với $O_t=\text{bẩn}\iff S_t=(4,\text{còn rác})$. Tập hành động $\{\text{trái},\text{phải},\text{hút}\}$ giống nhau ở mọi trạng thái. Sau ba bước của Ví dụ 01.1, lịch sử là

$$
H_3=(\text{sạch},\text{phải},0,\text{sạch},\text{phải},0,\text{sạch},\text{phải},0,\text{bẩn}).
$$

Tác tử có thể không bao giờ thấy trạng thái; lịch sử là toàn bộ dữ liệu nó có trước khi chọn $A_t$. Độ dài của lịch sử cho biết $t$, tức số hành động đã dùng, và với $L=5$ thông tin này quyết định robot còn đủ bước để tới ô 4 hay không.

::: remark Nhận xét 01.3 (Trạng thái khác quan sát)
Hai trạng thái khác nhau có thể cho cùng một quan sát: $(1,\text{còn rác})$, $(2,\text{còn rác})$ và $(3,\text{còn rác})$ đều cho $O_t=\text{sạch}$. Quy tắc "ở ô 3 thì sang phải" vì thế không thực hiện được, còn quy tắc "thấy $\text{sạch}$ thì sang phải, thấy $\text{bẩn}$ thì hút" thì thực hiện được.

Nhầm lẫn thường gặp là đồng nhất quan sát với trạng thái: robot ở ô 3 và robot ở ô 1 cùng thấy $\text{sạch}$, nhưng cần một và ba lần $\text{phải}$ để tới rác. Lịch sử phân biệt được hai tình huống này: sau hai lần $\text{phải}$ từ ô 1, lịch sử chứa hai hành động $\text{phải}$. Khi tác tử quan sát đầy đủ, như người chơi Tic-tac-toe nhìn thấy toàn bộ bàn cờ, nhầm lẫn này không xảy ra.
:::

<!-- note-topic-id: lec-01-topic-08 -->
### 1.4 Nhu cầu học và giới hạn của mô hình cố định

Nếu người thiết kế biết trước rác ở ô 4, chương trình "sang phải ba lần rồi hút" giải xong bài toán của Ví dụ 01.1 mà không cần học. Khi điều người thiết kế biết trước không còn đúng, tác tử phải học để làm được ba việc (bài giảng gốc 2025–2026, trang 6):

- ghi nhớ kết quả các tương tác đã có;
- thích nghi khi môi trường đổi;
- khái quát sang tình huống chưa gặp đúng dạng.

::: remark Nhận xét 01.4 (Giới hạn của điều khiển với mô hình cố định)
Cách thiết kế điều khiển truyền thống mô hình hóa môi trường trước, chẳng hạn vẽ bản đồ ngôi nhà, rồi chọn hành động tối ưu theo mô hình đó qua một hàm mục tiêu. Cách này gặp ba vấn đề (bài giảng gốc 2025–2026, trang 7–8).

- **Môi trường đổi.** Đồ đạc di chuyển hoặc có vật thể chuyển động làm mô hình viết sẵn sai. Chương trình "sang phải ba lần rồi hút" cho phần thưởng $0$ ở mọi lượt nếu rác chuyển sang ô 2, và không tự sửa vì không dùng phản hồi.
- **Không gian tìm kiếm quá lớn.** Với ba hành động và lượt dài $L$ bước có $3^L$ chuỗi hành động: $3^5=243$ chuỗi khi $L=5$, nhưng $3^{50}\approx7{,}2\cdot10^{23}$ chuỗi khi $L=50$.
- **Lập kế hoạch dưới bất định.** Khi kết quả của hành động là ngẫu nhiên, như với xe tự hành hoặc khi đăng ký môn học, một kế hoạch vòng hở (open-loop plan), tức dãy hành động định sẵn, không phản ứng được với kết quả thực. Nếu luật ngẫu nhiên đã biết, một quy tắc chọn hành động theo kết quả thực, tính bằng quy hoạch động (dynamic programming), xử lý được mà không cần học; việc học cần khi luật chưa biết hoặc thay đổi.

Học tăng cường dùng phản hồi của môi trường để cập nhật quyết định, và có thể học hoặc cập nhật mô hình từ tương tác.
:::

![Hai khối. Khối trái ghi mô hình cố định, mũi tên ghi suy ra hành động. Khối phải ghi học từ tương tác, mũi tên ghi dữ liệu cập nhật quyết định.](img/lec-01/control-learning.svg)

Hình trên đặt hai cách làm cạnh nhau. Ở khối trái, người thiết kế suy ra hành động một lần từ mô hình, và phản hồi của môi trường không quay lại làm đổi quyết định. Ở khối phải, tác tử dùng dữ liệu tương tác để cập nhật quyết định, đúng vòng phản hồi của Định nghĩa 01.1.

::: exercise Bài tập 01.1 (Trạng thái và quan sát của robot dọn dãy bốn ô)
Dãy bốn ô đánh số 1 đến 4; chỉ ô 4 có rác. Hành động $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy; $\text{hút}$ làm sạch ô đang đứng. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Cảm biến báo $\text{sạch}$ hoặc $\text{bẩn}$ cho ô đang đứng. Lượt bị cắt sau $L=5$ hành động. Lần này robot bắt đầu ở ô 3.

- (a) Viết $S_0$, $O_0$ và tập hành động hợp lệ.
- (b) Robot chọn $A_0=\text{phải}$. Viết $R_1$, $S_1$, $O_1$ và lịch sử $H_1$.
- (c) Liệt kê mọi trạng thái chưa kết thúc lượt cho cùng quan sát với $S_0$, và nêu số lần $\text{phải}$ mỗi trạng thái cần để tới rác.
:::

::: hint
Trạng thái là cặp (vị trí, tình trạng ô 4). Quan sát chỉ phụ thuộc ô robot đang đứng.
:::

::: solution
**Câu (a).** $S_0=(3,\text{còn rác})$, $O_0=\text{sạch}$ vì ô 3 sạch, và tập hành động hợp lệ là $\{\text{trái},\text{phải},\text{hút}\}$.

**Câu (b).** Sang phải từ ô 3 đưa robot tới ô 4, chưa hút nên $R_1=0$ và lượt chưa kết thúc. Do đó $S_1=(4,\text{còn rác})$, $O_1=\text{bẩn}$, và $H_1=(\text{sạch},\text{phải},0,\text{bẩn})$.

**Câu (c).** Quan sát $\text{sạch}$ xuất hiện khi robot đứng ở ô 1, 2 hoặc 3 lúc ô 4 còn rác: các trạng thái $(1,\text{còn rác})$, $(2,\text{còn rác})$, $(3,\text{còn rác})$, cần lần lượt ba, hai và một lần $\text{phải}$. Vì cả ba cho cùng $O_0=\text{sạch}$ và lịch sử ở bước $0$ chỉ gồm $O_0$, robot không biết mình cần bao nhiêu lần $\text{phải}$.

**Kiểm tra lại.** Câu (b) phù hợp luật: phần thưởng $+1$ chỉ đến khi robot chọn $\text{hút}$ ở ô 4, chưa xảy ra ở bước $0$.
:::

Vòng tương tác (Định nghĩa 01.1) cùng trạng thái, quan sát và lịch sử (Định nghĩa 01.2) đủ để ghi lại một lượt của robot, trong đó phần thưởng $R_{t+1}$ chỉ được cho là một số thực do môi trường trả về.

<!-- note-topic-id: lec-01-topic-02 -->
## 2. Tín hiệu học và dữ liệu tương tác

Trong Ví dụ 01.1, ở bước $0$ robot nhận $R_1=0$ sau khi sang phải; nếu sang trái, nó cũng nhận $R_1=0$. Một nhãn sẽ nói "hành động đúng ở ô 1 là sang phải", còn phần thưởng $0$ không phân biệt hai lựa chọn. Để nhận dạng một bài toán Học tăng cường, chúng ta cần so sánh tín hiệu này với tín hiệu của học có giám sát và học không giám sát (unsupervised learning), và chỉ ra vì sao dữ liệu tương tác không đổi thứ tự được.

### 2.1 Thứ tự của dữ liệu tương tác

Một cách trực quan, dữ liệu có nhãn là một tập: các cặp $(x_i,y_i)$ có thể xếp theo thứ tự bất kỳ mà nội dung không đổi. Dữ liệu tương tác là một dãy: mỗi mẫu là hậu quả của hành động trong mẫu trước. Để kiểm tra điều này trên robot, xem ví dụ sau.

::: example Ví dụ 01.2 (Đổi thứ tự các mẫu tương tác)
**Dữ kiện.** Lượt của Ví dụ 01.1 cho bốn mẫu dạng (quan sát, hành động, phần thưởng):

$$
(\text{sạch},\text{phải},0),\quad(\text{sạch},\text{phải},0),\quad(\text{sạch},\text{phải},0),\quad(\text{bẩn},\text{hút},1).
$$

Robot bắt đầu ở ô 1; chỉ ô 4 có rác; cảm biến báo tình trạng ô đang đứng.

**Đổi thứ tự.** Đưa mẫu cuối lên đầu cho dãy $(\text{bẩn},\text{hút},1)$, $(\text{sạch},\text{phải},0)$, $(\text{sạch},\text{phải},0)$, $(\text{sạch},\text{phải},0)$. Mẫu đầu đòi hỏi robot thấy $\text{bẩn}$ ở bước $0$, nhưng ở bước $0$ robot đứng ở ô 1 sạch. Dãy mới không thể xảy ra trong môi trường này. Hơn nữa, sau khi hút được rác lượt đã kết thúc, nên không có mẫu nào đứng sau mẫu $(\text{bẩn},\text{hút},1)$.

**So với dữ liệu có nhãn.** Với ba cặp $(x_1,y_1)$, $(x_2,y_2)$, $(x_3,y_3)$, mất mát trung bình $\frac13\big[\ell(f(x_1),y_1)+\ell(f(x_2),y_2)+\ell(f(x_3),y_3)\big]$ không đổi khi đổi thứ tự ba số hạng, vì phép cộng giao hoán.

**Đổi chính sách.** Nếu robot luôn chọn $\text{trái}$, nó ở mãi ô 1 và mọi quan sát đều là $\text{sạch}$. Trong dữ liệu đó không có mẫu nào chứa quan sát $\text{bẩn}$, nên robot không có thông tin gì về hậu quả của việc hút ở ô bẩn.

**Kiểm tra lại.** Trong dãy gốc, quan sát $\text{bẩn}$ xuất hiện đúng một lần, ở bước $3$, ngay sau ba lần $\text{phải}$ đưa robot từ ô 1 tới ô 4.
:::

Dữ liệu tương tác vì vậy có thứ tự cố định, và phân phối của nó phụ thuộc cách tác tử chọn hành động, điều không có trong học có giám sát.

### 2.2 Ba dạng tín hiệu học

Theo bài giảng gốc (2025–2026, trang 19), ba dạng học máy phân biệt nhau ở tín hiệu hướng dẫn.

![Ba khối. Khối có giám sát ghi nhãn trực tiếp. Khối không giám sát ghi cấu trúc dữ liệu. Khối tăng cường ghi tương tác, thưởng trễ.](img/lec-01/learning-signals.svg)

Trên hình, ba khối khác nhau ở nguồn và thời điểm của tín hiệu:

- ở khối có giám sát, mỗi mẫu đi kèm đầu ra đúng ngay từ đầu;
- ở khối không giám sát, không có đầu ra đúng nào;
- ở khối tăng cường, tín hiệu là phần thưởng đến sau hành động, có khi sau nhiều hành động.

::: definition Định nghĩa 01.5 (Ba dạng tín hiệu học)
**Học có giám sát** là bài toán học từ tập dữ liệu $\{(x_i,y_i)\}_{i=1}^n$ cho trước, trong đó nhãn $y_i$ là đầu ra đúng cho đầu vào $x_i$; hàm dự đoán được chọn để làm nhỏ mất mát giữa đầu ra của hàm dự đoán và nhãn.

**Học không giám sát** là bài toán học từ tập dữ liệu $\{x_i\}_{i=1}^n$ cho trước, không có nhãn. Mục tiêu là tìm cấu trúc trong dữ liệu, chẳng hạn chia các $x_i$ thành cụm theo độ tương tự.

**Học tăng cường** là bài toán học từ dãy tương tác $O_0,A_0,R_1,O_1,A_1,R_2,\dots$ (Định nghĩa 01.1), trong đó các hành động do chính tác tử chọn và tín hiệu là phần thưởng $R_{t+1}\in\mathbb R$. Phần thưởng là một số đánh giá chuyển vừa xảy ra, không cho biết hành động đúng. Mục tiêu là chọn hành động để làm lớn kỳ vọng của tổng phần thưởng từ thời điểm chọn trở đi.
:::

Trong Học tăng cường, phần thưởng đánh giá hành động đã chọn và có thể đến trễ; tác tử không biết hành động khác có tốt hơn không nếu chưa thử.

Theo bài giảng gốc (2025–2026, trang 17) và Sutton và Barto (2018, §1.1), hai đặc trưng phân biệt Học tăng cường là thử và sai (trial-and-error) và phản hồi trễ (delayed reward).

::: remark Nhận xét 01.6 (Bốn khác biệt của Học tăng cường)
Theo bài giảng gốc (2025–2026, trang 21), Học tăng cường khác hai dạng học còn lại ở bốn điểm, minh họa trên robot dọn dãy bốn ô:

- **Không có người giám sát, chỉ có phần thưởng.** Robot không nhận "hành động đúng là sang phải" mà nhận các số $0,0,0,1$.
- **Phản hồi bị trễ.** Phần thưởng $+1$ đến ở bước thứ tư, sau ba hành động có phần thưởng $0$.
- **Dữ liệu không độc lập, không cùng phân phối, thứ tự thời gian có vai trò.** $O_{t+1}$ phụ thuộc $S_t$ và $A_t$: robot ở ô 3 chọn $\text{phải}$ thì chắc chắn thấy $\text{bẩn}$ ở bước sau, nên hai mẫu liên tiếp không độc lập. Phân phối của quan sát đổi theo $t$: ở bước $0$ robot luôn thấy $\text{sạch}$.
- **Hành động có hậu quả lên dữ liệu về sau.** Robot luôn sang trái không bao giờ quan sát được ô bẩn.

Nhầm lẫn thường gặp là coi một lượt dài như một tập mẫu lớn rồi áp dụng nguyên các kết luận dựa trên giả thiết i.i.d. của học có giám sát.
:::

::: exercise Bài tập 01.2 (Nhận dạng tín hiệu học)
Xếp mỗi tình huống sau vào một trong ba dạng của Định nghĩa 01.5, và nêu tín hiệu học trong tình huống đó.

- (a) $1\,000$ ảnh ô sàn, mỗi ảnh được người gán nhãn $\text{sạch}$ hoặc $\text{bẩn}$; cần dự đoán nhãn của ảnh mới.
- (b) $1\,000$ ảnh ô sàn không có nhãn; cần chia ảnh thành các nhóm giống nhau.
- (c) Một robot hút bụi trên dãy bốn ô, bắt đầu ở ô 1, chỉ ô 4 có rác, lượt bị cắt sau $L=5$ hành động, ghi được dãy mẫu (quan sát, hành động, phần thưởng): $(\text{sạch},\text{phải},0)$, $(\text{sạch},\text{hút},0)$, $(\text{sạch},\text{phải},0)$, $(\text{sạch},\text{phải},0)$, $(\text{bẩn},\text{hút},1)$.
- (d) Một sinh viên chỉ biết điểm tổng kết ở cuối học kỳ, sau khi đã chọn cách học trong suốt học kỳ.
:::

::: hint
Hỏi hai câu cho mỗi tình huống: dữ liệu có sẵn trước hay do người học sinh ra, và tín hiệu có cho biết đầu ra đúng hay không.
:::

::: solution
**Câu (a).** Học có giám sát. Tín hiệu là nhãn $\text{sạch}$ hoặc $\text{bẩn}$ của từng ảnh, cho biết đầu ra đúng.

**Câu (b).** Học không giám sát. Không có nhãn; tiêu chí là độ giống nhau giữa các ảnh trong cùng nhóm.

**Câu (c).** Học tăng cường. Tín hiệu là dãy phần thưởng $0,0,0,0,1$, đến trễ, và dữ liệu do chính robot sinh ra.

**Câu (d).** Học tăng cường. Tín hiệu là điểm tổng kết, một số đánh giá đến sau cả học kỳ. Tình huống này có ba trong bốn khác biệt của Học tăng cường theo Nhận xét 01.6:

- chỉ có một số đánh giá thay cho đầu ra đúng;
- đánh giá đến sau cả chuỗi lựa chọn;
- cách học đã chọn ảnh hưởng tới những gì sinh viên trải qua về sau.

**Kiểm tra lại.** Lượt (c) dùng năm hành động, đúng bằng giới hạn $L=5$, và kết thúc bằng phần thưởng $1$ ở bước cuối.
:::

Ba dạng tín hiệu học (Định nghĩa 01.5) và bốn khác biệt của Học tăng cường (Nhận xét 01.6) cho tiêu chí nhận dạng một bài toán Học tăng cường. Tuy nhiên, khi phản hồi trễ, phần thưởng của một bước không cho biết hành động ở bước đó tốt đến đâu.

<!-- note-topic-id: lec-01-topic-03 -->
## 3. Phần thưởng và lợi tức

Trong Ví dụ 01.1, hậu quả của hành động ở bước $0$ chỉ lộ ra ở phần thưởng $+1$ của bước thứ tư. Chúng ta cần một đại lượng gom mọi phần thưởng từ sau hành động đến hết lượt, và cách tính đại lượng ấy trên mọi bước của lượt.

### 3.1 Phần thưởng trễ trên một lượt

Một cách trực quan, hậu quả của hành động $A_t$ gồm phần thưởng ngay sau nó và mọi phần thưởng về sau mà nó góp phần tạo ra, vì $A_t$ quyết định tình huống mà các hành động sau bắt đầu từ đó. Cộng các phần thưởng ấy lại cho một con số đo hậu quả dài hạn. Trước hết, ta tính con số đó trên lượt của Ví dụ 01.1.

![Năm vòng tròn S0, S1, S2, S3, S4 nối bằng bốn mũi tên từ trái sang phải. Trên mũi tên ghi hành động A0, A1, A2, A3; dưới mũi tên ghi phần thưởng R1 bằng 0, R2 bằng 0, R3 bằng 0, R4 bằng cộng 1.](img/lec-01/delayed-reward.svg)

Hình trên vẽ lượt của Ví dụ 01.1 dưới dạng một quỹ đạo. Mỗi mũi tên là một chuyển: hành động $A_t$ ghi phía trên đưa trạng thái $S_t$ sang $S_{t+1}$, và phần thưởng $R_{t+1}$ ghi phía dưới thuộc về chuyển đó. Chỉ phần thưởng của chuyển cuối khác $0$.

::: example Ví dụ 01.3 (Tổng phần thưởng còn lại trên lượt của robot)
**Dữ kiện.** Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác, chọn $\text{phải},\text{phải},\text{phải},\text{hút}$. Theo Ví dụ 01.1, lượt kết thúc ở $T=4$ với $(R_1,R_2,R_3,R_4)=(0,0,0,1)$.

**Tính.** Với mỗi bước $t$, cộng các phần thưởng đến sau hành động $A_t$:

- từ bước $0$: $R_1+R_2+R_3+R_4=0+0+0+1=1$;
- từ bước $1$: $R_2+R_3+R_4=0+0+1=1$;
- từ bước $2$: $R_3+R_4=0+1=1$;
- từ bước $3$: $R_4=1$;
- từ bước $4$: không còn phần thưởng nào, tổng rỗng bằng $0$.

**Diễn giải.** Ba hành động $\text{phải}$ có phần thưởng một bước bằng $0$ nhưng tổng phần thưởng còn lại bằng $1$.

**Kiểm tra lại.** Mỗi tổng bằng phần thưởng của bước kế tiếp cộng tổng của bước sau đó: $1=0+1$, $1=0+1$, $1=0+1$, $1=1+0$.
:::

### 3.2 Lượt, phần thưởng một bước và lợi tức

Phép tính của Ví dụ 01.3 cần ba quy ước:

- lượt dừng lúc nào;
- phần thưởng nào thuộc bước nào;
- tổng lấy tới đâu.

::: definition Định nghĩa 01.7 (Phần thưởng một bước, lượt, thời điểm kết thúc)
**Phần thưởng** $R_{t+1}\in\mathbb R$ là số thực môi trường trả sau hành động $A_t$; nó đánh giá chuyển từ bước $t$ sang bước $t+1$. Phần thưởng bị chặn; trong các lượt nhiều bước của chương, phần thưởng thuộc một tập hữu hạn số thực.

**Lượt** là một dãy tương tác từ bước $0$ tới một bước kết thúc. Lượt kết thúc khi xảy ra một sự kiện kết thúc do luật của môi trường quy định, như hút được rác hay ván cờ có kết quả, hoặc khi đã thực hiện $L$ hành động, gọi là cắt lượt (truncation).

**Thời điểm kết thúc** (termination time) $T$ là số hành động đã thực hiện khi lượt dừng. $T$ là biến ngẫu nhiên nhận giá trị nguyên dương với $T\le L$; sau bước $T$ không còn hành động hay phần thưởng nào.

**Quỹ đạo** (trajectory) của một lượt là dãy $S_0,A_0,R_1,S_1,\dots,A_{T-1},R_T,S_T$.
:::

$T$ ngẫu nhiên vì lượt có thể dừng sớm hay muộn tùy các hành động và phản hồi của môi trường: trong Ví dụ 01.1, $T=4$ với dãy $\text{phải},\text{phải},\text{phải},\text{hút}$ và $T=5$ khi robot sang trái ở bước đầu. Cận $T\le L$ bảo đảm mọi tổng dưới đây chỉ có hữu hạn số hạng.

::: definition Định nghĩa 01.8 (Lợi tức)
Với một lượt kết thúc tại $T$, lợi tức từ bước $t$, với $t=0,1,\dots,T$, là tổng các phần thưởng đến sau bước $t$:

$$
\begin{aligned}
G_t&=\sum_{k=t+1}^{T}R_k\\
&=R_{t+1}+R_{t+2}+\dots+R_T .
\end{aligned}\tag{3.1}
$$

Tại $t=T$, tổng không có số hạng nào, nên $G_T=0$.
:::

Công thức (3.1) cộng các phần thưởng từ $R_{t+1}$, phần thưởng đầu tiên chịu ảnh hưởng của $A_t$, đến $R_T$. $G_t$ là biến ngẫu nhiên vì cả các phần thưởng lẫn $T$ phụ thuộc diễn biến của lượt. Trên lượt của Ví dụ 01.3, $G_0=G_1=G_2=G_3=1$ và $G_4=0$, đúng năm tổng đã tính. Mọi phần thưởng có trọng số $1$, dù đến sớm hay muộn.

**Câu hỏi.** Tại sao không so sánh các hành động bằng phần thưởng một bước $R_{t+1}$? Trong Ví dụ 01.3, $R_1=0$ trong khi $G_0=1$, nên đại lượng dùng để so sánh hành động là $G_t$. Nhầm lẫn thường gặp là gọi $R_{t+1}$ là "phần thưởng của trạng thái $S_{t+1}$" rồi coi đó là đánh giá dài hạn của $S_{t+1}$.

### 3.3 Hệ thức đệ quy của lợi tức

Các phép kiểm tra lại trong Ví dụ 01.3 đều có cùng dạng: lợi tức ở một bước bằng phần thưởng kế tiếp cộng lợi tức ở bước sau. Hệ thức này đúng cho mọi lượt hữu hạn.

::: proposition Mệnh đề 01.9 (Hệ thức đệ quy của lợi tức)
**Giả thiết.** Một lượt kết thúc tại $T$ hữu hạn, với các phần thưởng $R_1,\dots,R_T$ và lợi tức $G_t$ cho bởi (3.1).

**Kết luận.** Với mọi $t=0,1,\dots,T-1$,

$$
G_t=R_{t+1}+G_{t+1},\qquad G_T=0 .\tag{3.2}
$$

**Điều kiện áp dụng.** Hệ thức đúng cho từng lượt cụ thể, với mọi giá trị của các phần thưởng, mọi cách chọn hành động và mọi luật của môi trường; không cần kỳ vọng hay giả thiết xác suất.

**Phạm vi.** Hệ thức dùng tổng không chiết khấu của (3.1), xác định được vì lượt hữu hạn. Khi lượt có thể kéo dài vô hạn, tổng (3.1) có thể không hội tụ; lợi tức có chiết khấu thêm hệ số $\gamma$ trước $G_{t+1}$.
:::

::: proof Chứng minh Mệnh đề 01.9
Với $t\le T-1$, tổng (3.1) có ít nhất số hạng $R_{t+1}$; tách số hạng này ra khỏi tổng:

$$
\begin{aligned}
G_t&=\sum_{k=t+1}^{T}R_k\\
&=R_{t+1}+\sum_{k=t+2}^{T}R_k\\
&=R_{t+1}+G_{t+1}.
\end{aligned}
$$

Đẳng thức thứ nhất là định nghĩa (3.1), đẳng thức thứ hai tách số hạng $k=t+1$, đẳng thức thứ ba là định nghĩa (3.1) tại bước $t+1$. Khi $t=T-1$, tổng ở dòng thứ hai là tổng rỗng, bằng $0=G_T$, nên đẳng thức vẫn đúng. $\square$
:::

Giả thiết $T$ hữu hạn và đẳng thức $G_T=0$ có vai trò riêng:

- **Bỏ $T$ hữu hạn.** $G_{t+1}$ có thể không còn là một số; với phần thưởng $1$ ở mọi bước của một lượt không bao giờ dừng, hai vế của (3.2) không xác định.
- **Bỏ $G_T=0$.** Đẳng thức này được dùng ở dòng cuối chứng minh; gán cho $G_T$ giá trị khác thì hệ thức sai ở $t=T-1$.

::: example Ví dụ 01.4 (Tính lợi tức ngược khi di chuyển có chi phí)
**Dữ kiện.** Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác, lượt bị cắt sau $L=4$ hành động. Với chi phí di chuyển $c=0{,}1$, phần thưởng được đặt lại là

$$
R_{t+1}=\begin{cases}
-c, & \text{trái hoặc phải},\\
0, & \text{hút ở ô sạch},\\
+1, & \text{hút rác ở ô 4},
\end{cases}
$$

và hút được rác thì lượt kết thúc. Robot chọn $\text{phải},\text{phải},\text{phải},\text{hút}$.

**Dãy phần thưởng.** Ba lần di chuyển rồi một lần hút được rác, nên $T=4$ và $(R_1,R_2,R_3,R_4)=(-0{,}1;\,-0{,}1;\,-0{,}1;\,1)$.

**Tính ngược theo (3.2).**

- $G_4=0$;
- $G_3=R_4+G_4=1+0=1$;
- $G_2=R_3+G_3=-0{,}1+1=0{,}9$;
- $G_1=R_2+G_2=-0{,}1+0{,}9=0{,}8$;
- $G_0=R_1+G_1=-0{,}1+0{,}8=0{,}7$.

**Diễn giải.** Với cách đặt này, $G_t$ giảm $0{,}1$ cho mỗi lần di chuyển còn phải làm, nên $G_t$ phân biệt các bước ở gần và xa rác; với cách đặt của Ví dụ 01.3, mọi $G_t$ với $t<T$ bằng $1$. Ở bước đầu, $\text{hút}$ tại ô 1 sạch cho phần thưởng $0$, cao hơn $-0{,}1$ của $\text{phải}$, nhưng ba hành động còn lại không đủ để tới ô 4 rồi hút và mỗi lần di chuyển chỉ thêm $-0{,}1$, nên lợi tức lớn nhất khi hút trước là $0<0{,}7$. Chịu phần thưởng tức thời thấp hơn để được lợi tức cao hơn là hiện tượng bài giảng gốc (2025–2026, trang 25) gọi là hy sinh phần thưởng tức thời. Với $L=5$, hút ở ô 1 rồi đi $\text{phải},\text{phải},\text{phải},\text{hút}$ cũng cho $0+3\cdot(-0{,}1)+1=0{,}7$, nên so sánh trên cần $L=4$.

**Kiểm tra lại.** Cộng trực tiếp theo (3.1): $G_0=3\cdot(-0{,}1)+1=0{,}7$.
:::

**Trong thực hành.** Mệnh đề 01.9 là cách tính mọi $G_t$ của một lượt đã ghi lại: đi ngược từ $G_T=0$, mỗi bước một phép cộng, thay vì cộng lại từ đầu cho từng $t$ (Bài tập 01.4 đếm số phép cộng). Phép tính ngược cần lượt đã kết thúc để có $G_T=0$.

<!-- note-topic-id: lec-01-topic-10 -->
### 3.4 Giả thuyết phần thưởng

Lợi tức chỉ đo được những gì phần thưởng ghi nhận: Ví dụ 01.4 đổi cách đặt phần thưởng và các $G_t$ đổi theo. Điều người thiết kế mong muốn ở robot phải được viết thành các con số $R_{t+1}$, và chúng ta cần biết mọi mục tiêu có viết được như vậy hay không.

::: remark Nhận xét 01.10 (Giả thuyết phần thưởng)
Giả thuyết phần thưởng (reward hypothesis) phát biểu rằng mọi mục tiêu đều mô tả được bằng việc làm lớn nhất kỳ vọng của tổng các phần thưởng nhận được (bài giảng gốc 2025–2026, trang 24; Sutton và Barto 2018, §3.2). Với lượt hữu hạn, mục tiêu là chọn cách hành động sao cho $\mathbb E[G_0]$ lớn nhất. Trong cờ, chẳng hạn, kết quả thắng, hòa hoặc thua mã hóa được thành phần thưởng $+1$, $0$ hoặc $-1$ ở cuối ván.

Giả thuyết phần thưởng là một giả thiết mô hình hóa: không có chứng minh rằng mọi mục tiêu thực tế đều mã hóa đầy đủ được bằng một tín hiệu số cộng dồn. Khi phần thưởng ghi thiếu một phần mục tiêu, tác tử có thể có hành vi ngoài ý muốn, như trong ví dụ sau.
:::

::: example Ví dụ 01.5 (Phần thưởng bỏ sót mục tiêu)
**Dữ kiện.** Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác, lượt bị cắt sau $L=5$ hành động; phần thưởng $+1$ khi hút được rác ở ô 4, $0$ ở mọi bước khác. Ô 2 có một bình hoa; nếu robot chọn $\text{hút}$ khi đứng ở ô 2, bình hoa bị đổ. Lượt A là $\text{phải},\text{phải},\text{phải},\text{hút}$; lượt B là $\text{phải},\text{hút},\text{phải},\text{phải},\text{hút}$, trong đó lần hút thứ nhất ở ô 2 làm đổ bình hoa.

**Tính.** Lượt A có $T=4$, $(R_1,\dots,R_4)=(0,0,0,1)$ và $G_0=1$. Lượt B có $T=5$, $(R_1,\dots,R_5)=(0,0,0,0,1)$ và $G_0=1$.

**Diễn giải.** Hai lượt có cùng lợi tức dù lượt B làm đổ bình hoa, nên một tác tử làm lớn kỳ vọng của $G_0$ không có lý do nào để tránh lượt B. Mục tiêu "không làm đổ đồ" bị bỏ sót vì nó không có mặt trong phần thưởng.

**Sửa phần thưởng.** Thêm phần thưởng $-1$ cho bước làm đổ bình hoa. Lượt B khi đó có $(R_1,\dots,R_5)=(0,-1,0,0,1)$ và $G_0=0$, còn lượt A vẫn có $G_0=1$.

**Kiểm tra lại.** Tính ngược theo (3.2) trên lượt B đã sửa: $G_5=0$, $G_4=1$, $G_3=1$, $G_2=1$, $G_1=-1+1=0$, $G_0=0+0=0$.
:::

::: exercise Bài tập 01.3 (Lợi tức trên dãy bốn ô có ghế)
Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác. Cách đặt phần thưởng có thêm $-1$ cho bước robot va vào một chiếc ghế; va ghế không cản robot sang ô kế tiếp. Trong một lượt, robot nhận dãy phần thưởng $(R_1,R_2,R_3,R_4)=(0,-1,0,1)$ và lượt kết thúc ở $T=4$.

- (a) Tính $G_4,G_3,G_2,G_1,G_0$ theo chiều ngược bằng (3.2), rồi kiểm tra $G_0$ bằng (3.1).
- (b) Trong các bước $t=0,1,2,3$, bước nào có lợi tức nhỏ hơn phần thưởng cuối $R_4$, và vì sao.
:::

::: hint
$G_t$ cộng các phần thưởng có chỉ số từ $t+1$ đến $T$; $G_T=0$.
:::

::: solution
**Câu (a).** $G_4=0$; $G_3=R_4+G_4=1$; $G_2=R_3+G_3=0+1=1$; $G_1=R_2+G_2=-1+1=0$; $G_0=R_1+G_1=0+0=0$. Theo (3.1), $G_0=0+(-1)+0+1=0$.

**Câu (b).** $G_0=G_1=0<1=R_4$. Hai lợi tức này còn chứa phần thưởng $R_2=-1$ của bước va ghế, xảy ra sau bước $0$ và bước $1$. Từ bước $2$ trở đi, phần thưởng $-1$ đã ở quá khứ nên $G_2=G_3=1$. Ngoài khoảng được hỏi, $G_4=0<1$ vì sau thời điểm kết thúc không còn phần thưởng nào.

**Kiểm tra lại.** Tổng mọi phần thưởng của lượt là $0$, bằng $G_0$.
:::

::: exercise Bài tập 01.4 (Lợi tức tích lũy và chi phí tính toán)
Một lượt kết thúc tại $T$ hữu hạn với các phần thưởng $R_1,\dots,R_T$; lợi tức $G_t$ cho bởi (3.1).

- (a) Chứng minh $G_0=\sum_{k=1}^{t}R_k+G_t$ với mọi $t=0,1,\dots,T$, trong đó tổng rỗng bằng $0$.
- (b) Đếm số phép cộng cần để tính $G_0,\dots,G_{T-1}$ nếu tính mỗi $G_t$ trực tiếp bằng (3.1), và nếu tính ngược bằng (3.2); áp dụng với $T=4$.
:::

::: hint
Câu (a): tách tổng $\sum_{k=1}^{T}$ tại chỉ số $t$. Câu (b): một tổng $m$ số hạng cần $m-1$ phép cộng.
:::

::: solution
**Câu (a).** Theo (3.1), $G_0=\sum_{k=1}^{T}R_k$. Với $0\le t\le T$, tách tổng tại $t$:

$$
\begin{aligned}
G_0&=\sum_{k=1}^{T}R_k\\
&=\sum_{k=1}^{t}R_k+\sum_{k=t+1}^{T}R_k\\
&=\sum_{k=1}^{t}R_k+G_t.
\end{aligned}
$$

Đẳng thức thứ nhất là định nghĩa (3.1) tại $t=0$, đẳng thức thứ hai tách tổng tại chỉ số $t$, đẳng thức thứ ba là định nghĩa (3.1) tại bước $t$. Khi $t=0$, tổng thứ nhất rỗng; khi $t=T$, tổng thứ hai rỗng và $G_T=0$. $\square$

**Câu (b).** Tính trực tiếp, $G_t$ là tổng của $T-t$ số hạng nên cần $T-t-1$ phép cộng; tổng số là $\sum_{t=0}^{T-1}(T-t-1)=0+1+\dots+(T-1)=\frac{T(T-1)}{2}$. Tính ngược, $G_{T-1}=R_T$ không cần phép cộng nào, và mỗi $G_t=R_{t+1}+G_{t+1}$ với $t=T-2,\dots,0$ cần một phép cộng, tổng cộng $T-1$ phép cộng. Với $T=4$: tính trực tiếp cần $\frac{4\cdot3}{2}=6$ phép cộng, tính ngược cần $3$.

**Kiểm tra lại.** Với $T=4$, tính trực tiếp: $G_0$ cần $3$ phép cộng, $G_1$ cần $2$, $G_2$ cần $1$, $G_3$ cần $0$, tổng $6$; tính ngược: $G_2$, $G_1$, $G_0$, mỗi số một phép cộng.
:::

Lợi tức (Định nghĩa 01.8) đo hậu quả dài hạn trên một lượt và tính được ngược nhờ hệ thức $G_t=R_{t+1}+G_{t+1}$ (Mệnh đề 01.9). Tuy nhiên, lợi tức là con số của một lượt cụ thể, còn tác tử phải chọn hành động trước khi biết lượt sẽ diễn ra thế nào.

<!-- note-topic-id: lec-01-topic-04 -->
## 4. Chính sách, hàm giá trị, mô hình và thăm dò

Cả robot dọn dãy bốn ô lẫn người chơi X trong một ván Tic-tac-toe đều cần một quy tắc chọn hành động và một cách đánh giá tình huống không gắn với một lượt cụ thể. Đứng trước một thế cờ, X phải làm hai việc khác nhau: chọn một nước trong các ô trống, và đánh giá thế cờ hiện tại tốt đến đâu khi các nước về sau còn chưa biết. Chúng ta cần tên và ký hiệu cho:

- quy tắc chọn hành động;
- phép đánh giá tình huống;
- phần dự báo môi trường mà tác tử có thể dùng;
- cách chọn giữa dùng ước lượng hiện có của giá trị và thu thêm dữ liệu, khi giá trị chỉ ước lượng được từ ít mẫu.

### 4.1 Chọn nước và chính sách

Một cách trực quan, việc chọn nước là một quy tắc: nhận những gì đã biết về ván cờ và trả về một nước, có thể kèm yếu tố ngẫu nhiên. Việc đánh giá là một con số tóm tắt kết quả tương lai khi quy tắc chọn nước đã được cố định. Để tách hai việc này, xem ví dụ sau trên cùng một thế cờ.

::: example Ví dụ 01.6 (Hai việc trên một thế cờ)
**Dữ kiện.**

- Tic-tac-toe chơi trên bàn $3\times3$, các ô đánh số 1 đến 9 theo hàng, từ trái sang phải và từ trên xuống dưới.
- Hai người luân phiên đặt quân X và quân O vào ô trống; mỗi lần đặt một quân là một nước đi, và người sắp đặt quân là người đến phiên (turn).
- Ai có ba quân thẳng hàng theo hàng, cột hoặc đường chéo trước thì thắng; bàn đầy mà không ai có ba quân thẳng hàng thì hòa.
- Thế cờ $s$: X ở ô 1 và 5; O ở ô 2, 4 và 8; các ô 3, 6, 7, 9 trống; đến phiên X.

**Việc thứ nhất: chọn nước.** Hai quy tắc chọn nước khác nhau:

- quy tắc $\pi_w$: nếu có nước làm X thắng ngay thì đánh nước đó, nếu có nhiều nước như vậy thì chọn đều trong số đó, nếu không có thì chọn đều trên các ô trống;
- quy tắc $\pi_u$: luôn chọn đều trên các ô trống.

Ở thế cờ $s$, nước 9 tạo đường chéo 1–5–9 cho X. Không ô trống nào khác cho X ba quân thẳng hàng: mỗi đường đi qua ô 3, 6 hoặc 7 hoặc chứa một quân O, hoặc còn một ô trống khác. Quy tắc $\pi_w$ chọn ô 9 với xác suất $1$; quy tắc $\pi_u$ chọn ô 9 với xác suất $\frac14$.

**Việc thứ hai: đánh giá thế cờ.** Dưới $\pi_w$, X thắng ngay, nên mọi diễn biến từ $s$ cho lợi tức $+1$. Dưới $\pi_u$, với xác suất $\frac14$ X thắng ngay; với xác suất $\frac34$ ván tiếp tục và kết quả phụ thuộc nước trả lời của O cùng các nước sau của X.

**Diễn giải.** Việc chọn nước cho một phân phối trên bốn ô, việc đánh giá cho một số, và số đó phụ thuộc quy tắc chọn nước.

**Kiểm tra lại.** Bốn xác suất của $\pi_u$ có tổng $4\cdot\frac14=1$.
:::

Phép đánh giá dùng đến quy tắc chọn nước, nên chúng ta định nghĩa quy tắc đó trước. Quy tắc đó nhận toàn bộ lịch sử $H_t$, tức mọi dữ liệu tác tử có theo Định nghĩa 01.2.

::: definition Định nghĩa 01.11 (Chính sách)
**Chính sách** của tác tử là một quy tắc $\pi$ gán cho mỗi lịch sử $h$ một phân phối xác suất $\pi(\cdot\mid h)$ trên tập hành động hợp lệ ở bước đó:

$$
\begin{aligned}
&\pi(a\mid h)\ge0,\\
&\sum_{a}\pi(a\mid h)=1 .
\end{aligned}
$$

Tác tử theo chính sách $\pi$ nếu ở mỗi bước $t$, khi $H_t=h$, nó chọn $A_t=a$ với xác suất $\pi(a\mid h)$.

**Chính sách xác định** (deterministic policy) là trường hợp mỗi $\pi(\cdot\mid h)$ dồn toàn bộ xác suất vào một hành động.
:::

Khi chính sách và luật của môi trường đã cố định, xác suất của mọi diễn biến trong lượt được xác định.

Với robot, ba quy tắc sau đều là chính sách:

- chính sách $\pi_1$ chọn $\text{phải}$ khi thấy $\text{sạch}$ và $\text{hút}$ khi thấy $\text{bẩn}$; đây là chính sách xác định chỉ dùng $O_t$;
- chính sách chọn đều (uniform random policy) $\pi_u$ chọn đều trên ba hành động và không dùng lịch sử;
- chương trình "phải ba lần rồi hút" là một chính sách xác định chỉ dùng số bước $t$.

Nhầm lẫn thường gặp là coi chính sách như hàm dự đoán $f$ của học có giám sát, được chọn để khớp nhãn; chính sách không có nhãn để khớp và được đánh giá qua lợi tức mà nó tạo ra.

### 4.2 Hàm giá trị

Đánh giá thế cờ ở Ví dụ 01.6 là kỳ vọng của lợi tức khi chính sách đã cố định. Ta tính đánh giá đó trên một thế cờ chỉ còn hai ô trống, nhỏ đến mức liệt kê được mọi diễn biến.

::: example Ví dụ 01.7 (Giá trị của một thế cờ hai ô trống)
**Dữ kiện.** Thế cờ $s'$: X ở ô 1, 3 và 5; O ở ô 2, 4, 7 và 8; các ô 6 và 9 trống; đến phiên X. Thế cờ này xuất hiện từ thế cờ $s$ của Ví dụ 01.6 khi X đánh ô 3 rồi O đánh ô 7. Phần thưởng từ góc nhìn của X: $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở mọi bước chưa kết thúc. Hai người đánh luân phiên vào ô trống; ai có ba quân thẳng hàng theo hàng, cột hoặc đường chéo trước thì thắng. Khi chỉ còn một ô trống, O buộc phải đánh ô đó. Chính sách $\pi_u$ chọn đều trên các ô trống; $\pi_w$ đánh nước thắng ngay nếu có, chọn đều trong số đó nếu có nhiều nước như vậy, nếu không có thì chọn đều.

**Liệt kê diễn biến.**

- X đánh ô 9: X có đường chéo 1–5–9 và thắng. Lợi tức là $+1$.
- X đánh ô 6: X không có ba quân thẳng hàng, vì hàng 4–5–6 có O ở ô 4 và cột 3–6–9 còn trống ô 9. O đánh ô trống còn lại là ô 9 và có hàng 7–8–9, nên O thắng. Lợi tức là $-1$.

**Tính dưới $\pi_u$.** Mỗi nước có xác suất $\frac12$:

$$
\frac12\cdot(+1)+\frac12\cdot(-1)=0 .
$$

**Tính dưới $\pi_w$.** Ô 9 là nước thắng ngay, nên $\pi_w$ chọn ô 9 với xác suất $1$ và kỳ vọng của lợi tức là $1$.

**Kiểm tra lại.** Không ai đã thắng trước nước này: đường 1–5–9 của X còn thiếu ô 9, cột 3–6–9 còn thiếu ô 6 và ô 9; hàng 7–8–9 của O còn thiếu ô 9. Thế cờ có ba quân X và bốn quân O, phù hợp với việc O đi trước.
:::

Cùng thế cờ có hai đánh giá khác nhau, $0$ và $1$, theo hai chính sách. Đánh giá vì vậy là một hàm của cả tình huống lẫn chính sách, nên ký hiệu của giá trị ghi cả hai đối số.

::: definition Định nghĩa 01.12 (Hàm giá trị)
Giả sử luật của môi trường cố định: với mỗi lịch sử và hành động, phân phối của phần thưởng kế tiếp, quan sát kế tiếp và việc lượt có kết thúc hay không là cố định, không phụ thuộc chính sách. Cho chính sách $\pi$ và một lịch sử $h$ đến bước $t$ mà môi trường có thể sinh ra dưới một cách chọn hành động nào đó.

**Giá trị** của $h$ dưới $\pi$ là

$$
v_\pi(h)=\mathbb E_\pi\big[G_t\mid H_t=h\big],\tag{4.1}
$$

kỳ vọng của lợi tức từ bước $t$ dưới phân phối của diễn biến bắt đầu từ $h$, trong đó các hành động từ bước $t$ trở đi theo $\pi$ và các phản hồi theo luật của môi trường. Khi xác suất $\Pr_\pi(H_t=h)$ để lịch sử $h$ xảy ra dưới $\pi$ là dương, đại lượng này trùng kỳ vọng có điều kiện thông thường; khi xác suất đó bằng $0$, (4.1) được hiểu theo nghĩa vừa nêu. Ký hiệu $\mathbb E_\pi[\,\cdot\mid H_t=h,A_t=a]$ được hiểu tương tự, với hành động ở bước $t$ cố định là $a$ và các hành động sau đó theo $\pi$.

Nếu $h$ là lịch sử của một lượt đã kết thúc, tức $t=T$, thì $G_T=0$ và $v_\pi(h)=0$.

**Hàm giá trị** của $\pi$ là ánh xạ $h\mapsto v_\pi(h)$.
:::

Công thức (4.1) có ba thành phần:

- lợi tức $G_t$ là đại lượng được đánh giá (Định nghĩa 01.8);
- điều kiện $H_t=h$ cố định những gì đã xảy ra;
- chỉ số $\pi$ cố định cách chọn hành động về sau.

Vì phần thưởng bị chặn, tức $\lvert R_{t+1}\rvert\le R_{\max}$ với một hằng số $R_{\max}$, và $T\le L$, nên $\lvert G_t\rvert\le LR_{\max}$ và kỳ vọng (4.1) luôn tồn tại. Theo giả thuyết phần thưởng (Nhận xét 01.10), mục tiêu của Học tăng cường là tìm chính sách đạt $\max_\pi\mathbb E_\pi[G_0]$.

Trong Ví dụ 01.7, giá trị được ghi theo thế cờ $s'$, không theo lịch sử dẫn tới $s'$. Cách ghi đó đúng ở đây vì $\pi_u$ và $\pi_w$ chỉ dùng thế cờ hiện tại, không nhớ các nước trước, và nước cuối của O bị buộc.

Giả thiết luật cố định vẫn thỏa khi môi trường có trạng thái ẩn (hidden state) như Định nghĩa 01.2, với phân phối trạng thái đầu cố định. Theo công thức Bayes, với $h$ chứa các hành động $a_0,\dots,a_{t-1}$,

$$
\begin{aligned}
&\Pr(S_t=s\mid H_t=h)\\
&\quad=\frac{\Pr(S_t=s,\,h)}{\sum_{z}\Pr(S_t=z,\,h)},\\
&\Pr(S_t=s,\,h)\\
&\quad=\Big[\prod_{k<t}\pi(a_k\mid h_k)\Big]\cdot q(s,h),
\end{aligned}
$$

trong đó $h_k$ là phần đầu của $h$ đến bước $k$ và $q(s,h)$ chỉ gồm phân phối trạng thái đầu và các xác suất của luật môi trường. Khi tích các xác suất chọn hành động dương, tích đó có mặt ở cả tử lẫn mẫu nên triệt tiêu; khi tích bằng $0$, phân phối được định nghĩa trực tiếp bằng $q(s,h)/\sum_z q(z,h)$. Do đó phân phối của trạng thái ẩn khi biết $h$ không phụ thuộc chính sách.

Theo cách hiểu trên, $h$ có thể chứa những hành động mà $\pi$ không bao giờ chọn. Với robot dọn dãy bốn ô và $L=5$, xét $h=(\text{sạch},\text{trái},0,\text{sạch})$: robot sang trái ở bước $0$, điều $\pi_1$ không làm, và vẫn ở ô 1 tại bước $1$. Từ $h$, $\pi_1$ chọn $\text{phải}$ ba lần rồi $\text{hút}$ ở hành động thứ năm, nhận $R_2=R_3=R_4=0$ và $R_5=1$, nên $v_{\pi_1}(h)=1$.

::: remark Nhận xét 01.13 (Hai nhầm lẫn về giá trị)
- **Giá trị khác phần thưởng.** Phần thưởng đánh giá một chuyển; giá trị đánh giá mọi phần thưởng về sau theo kỳ vọng. Ở lịch sử $h$ vừa xét, $R_2=0$ nhưng $v_{\pi_1}(h)=1$; dưới $\pi_u$, từ thế cờ của Ví dụ 01.7 mỗi lượt cho $+1$ hoặc $-1$, còn giá trị $0$ là trung bình của hai khả năng đó.
- **Giá trị sau khi lượt kết thúc bằng $0$.** Khi X đánh ô 9 ở thế cờ của Ví dụ 01.7, phần thưởng $+1$ là $R_{t+1}$ của chuyển cuối; giá trị của lịch sử đã kết thúc sau nước thắng bằng $0$, không bằng $+1$.
:::

**Trong thực hành.** Khi số trạng thái nhỏ, chúng ta lưu hàm giá trị thành bảng theo trạng thái; khi số trạng thái lớn, chúng ta xấp xỉ nó bằng hàm có tham số (parameterized function) hay mạng nơ-ron (neural network). Chúng ta không lưu giá trị trên lịch sử, vì với ba hành động, robot có tới $3^t$ dãy hành động khác nhau sau $t$ bước. Khi không biết luật của môi trường, chúng ta ước lượng $v_\pi(h)$ bằng trung bình lợi tức của nhiều lượt chạy theo $\pi$.

::: exercise Bài tập 01.5 (Giá trị của robot dưới một chính sách ngẫu nhiên)
Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác. Hành động $\text{phải}$ dịch robot sang phải một ô, robot đứng yên nếu đang ở ô 4; $\text{hút}$ làm sạch ô đang đứng. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Trong bài này, lượt bị cắt sau $L=4$ hành động. Chính sách $\pi$ chọn $\text{phải}$ hoặc $\text{hút}$, mỗi hành động với xác suất $\frac12$, không phụ thuộc lịch sử. Gọi $h_0$ là lịch sử ban đầu.

- (a) Lợi tức $G_0$ nhận những giá trị nào.
- (b) Tính $v_\pi(h_0)$.
- (c) Tính $v_{\pi_1}(h_0)$ với $\pi_1$: thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$. Giải thích vì sao hai giá trị khác nhau.
:::

::: hint
Phần thưởng khác $0$ chỉ có thể đến ở một bước. Đếm các dãy bốn hành động đưa robot tới ô 4 rồi hút.
:::

::: solution
**Câu (a).** Phần thưởng khác $0$ duy nhất là $+1$ ở bước hút được rác, và sau bước đó lượt kết thúc. Do đó $G_0=1$ nếu robot hút được rác trong bốn hành động và $G_0=0$ nếu không.

**Câu (b).** Muốn hút ở ô 4, robot cần ba lần $\text{phải}$ để đi từ ô 1 tới ô 4, rồi một lần $\text{hút}$, tổng cộng bốn hành động. Với $L=4$, không còn chỗ cho hành động thừa, nên dãy duy nhất cho $G_0=1$ là $\text{phải},\text{phải},\text{phải},\text{hút}$. Mỗi hành động được chọn độc lập với xác suất $\frac12$, nên

$$
\begin{aligned}
\Pr(G_0=1)&=\Big(\frac12\Big)^4=\frac1{16},\\
v_\pi(h_0)&=1\cdot\frac1{16}+0\cdot\frac{15}{16}\\
&=\frac1{16}.
\end{aligned}
$$

**Câu (c).** Dưới $\pi_1$, robot thấy $\text{sạch}$ ở ô 1, 2, 3 nên sang phải ba lần, thấy $\text{bẩn}$ ở ô 4 nên hút. Lượt luôn là $\text{phải},\text{phải},\text{phải},\text{hút}$ với $G_0=1$, nên $v_{\pi_1}(h_0)=1$. Hai giá trị khác nhau vì cùng lịch sử ban đầu nhưng chính sách khác nhau; giá trị là một hàm của chính sách (Định nghĩa 01.12).

**Kiểm tra lại.** $16$ dãy bốn hành động trên $\{\text{phải},\text{hút}\}$ có cùng xác suất $\frac1{16}$, và chỉ một dãy cho $G_0=1$.
:::

### 4.3 Mô hình của môi trường

Để tính giá trị trong Ví dụ 01.7, chúng ta đã dùng luật Tic-tac-toe để biết điều gì xảy ra sau mỗi nước. Một cách trực quan, tác tử cũng có thể mang theo một bản mô phỏng như vậy để thử trước các hành động trong đầu, thay vì thử trong môi trường thật; bản mô phỏng đó có thể đúng hoặc sai.

::: example Ví dụ 01.8 (Mô hình đúng và mô hình sai của robot)
**Dữ kiện.** Robot dọn dãy bốn ô bắt đầu ở ô 1, chỉ ô 4 có rác; $\text{trái}$, $\text{phải}$ dịch một ô, đứng yên nếu đi ra ngoài dãy; hút ở ô 4 khi còn rác cho $+1$ và kết thúc lượt, mọi bước khác cho $0$; $L=5$. Robot mang theo một bản mô phỏng, ghi dự báo phần thưởng là $\widehat R_{t+1}$.

- Bản M1 ghi đúng luật trên.
- Bản M2 ghi nhầm rằng rác ở ô 3.

**Thử trong đầu với M1.** Trong $3^4=81$ dãy bốn hành động, chỉ dãy $\text{phải},\text{phải},\text{phải},\text{hút}$ cho tổng dự báo bằng $1$. Thực hiện dãy đó trong môi trường thật cho $G_0=1$, đúng dự báo.

**Thử trong đầu với M2.** Dãy ngắn nhất có tổng dự báo $1$ là $\text{phải},\text{phải},\text{hút}$. Trong môi trường thật, lần hút ở ô 3 sạch cho $R_3=0$ và lượt chưa kết thúc.

**Kiểm tra lại.** Sau ba hành động, tổng dự báo của M2 là $1$, còn tổng phần thưởng thật là $0+0+0=0$.
:::

::: definition Định nghĩa 01.14 (Mô hình, lập kế hoạch, có mô hình và phi mô hình)
**Mô hình** của môi trường là một mô tả, do người thiết kế cung cấp hoặc do tác tử học từ dữ liệu, cho phép dự báo phản hồi của môi trường: với một trạng thái hoặc một lịch sử và một hành động, mô hình cho dự báo $(\widehat S_{t+1},\widehat R_{t+1})$, hoặc $(\widehat O_{t+1},\widehat R_{t+1})$ khi làm việc với quan sát, hoặc một phân phối xác suất trên các khả năng đó. Dấu mũ chỉ dự báo của mô hình, phân biệt với đại lượng do môi trường thật sinh ra.

**Lập kế hoạch** (planning) là việc dùng mô hình để chọn hành động bằng cách xét các diễn biến tương lai trước khi chúng thật sự xảy ra.

**Phương pháp có mô hình** (model-based) dùng một mô hình để lập kế hoạch. **Phương pháp phi mô hình** (model-free) học chính sách hoặc hàm giá trị trực tiếp từ dữ liệu tương tác, không dùng mô hình.
:::

Trong Ví dụ 01.8, M1 và M2 là hai mô hình, và việc thử $81$ dãy trong đầu là lập kế hoạch. Mô hình là thành phần thứ ba của tác tử, sau chính sách và hàm giá trị; theo bài giảng gốc (2025–2026, trang 26), nó mô tả thế giới thay đổi thế nào từ góc nhìn của tác tử.

![Ba khối xếp cạnh nhau. Khối chính sách ghi chọn hành động. Khối hàm giá trị ghi đánh giá tương lai. Khối mô hình ghi tùy chọn.](img/lec-01/rl-components.svg)

Hình trên đặt ba thành phần cạnh nhau; nhãn "tùy chọn" dưới khối mô hình có nghĩa là một tác tử Học tăng cường có thể không có mô hình.

::: remark Nhận xét 01.15 (Mô hình khác môi trường)
- **Dự báo có thể sai.** Môi trường sinh dữ liệu thật; mô hình chỉ dự báo, và dự báo có thể sai như M2 của Ví dụ 01.8. Nhầm lẫn thường gặp là coi kết quả lập kế hoạch trên mô hình là kết quả trên môi trường.
- **Tính giá trị trong Tic-tac-toe là lập kế hoạch.** Khi tính giá trị trong Tic-tac-toe, chúng ta cần biết đối thủ O chọn nước thế nào (ở Ví dụ 01.7, O buộc đánh ô trống cuối cùng); quy tắc đó là một mô hình của đối thủ. Trong thực tế, cách chơi của đối thủ không được biết trước và phải được ước lượng từ kinh nghiệm (Sutton và Barto 2018, §1.5).
:::

**Trong thực hành.** Mô hình thường là một bộ mô phỏng, như luật trò chơi hay bộ mô phỏng vật lý, hoặc một mô hình học được từ các bộ $(S_t,A_t,R_{t+1},S_{t+1})$ đã ghi; khi lập kế hoạch qua nhiều bước, sai số dự báo của bước trước làm đầu vào của bước sau sai theo, nên sai số tích lũy.

<!-- note-topic-id: lec-01-topic-05 -->
### 4.4 Thăm dò và khai thác

Các giá trị và phép lập kế hoạch ở trên dùng luật đã biết của môi trường. Tác tử phi mô hình chỉ có các mẫu đã thu, và khi mẫu còn ít, việc ước lượng giá trị từ mẫu tạo ra một xung đột mới. Để tách riêng khó khăn này, chúng ta xét bài toán chọn lặp lại một bước (multi-armed bandit): mỗi lượt chỉ gồm một hành động, nên lợi tức bằng phần thưởng một bước, và giá trị của hành động $a$ là kỳ vọng phần thưởng khi chọn $a$. Ví dụ: robot dọn dãy bốn ô có hai chế độ hút, một chế độ đã dùng nhiều lần, chế độ kia mới dùng hai lần, và robot phải chọn chế độ cho lần hút tới.

Một cách trực quan, hành động có ước lượng cao nhất là lựa chọn tốt nhất theo dữ liệu đã có, nhưng ước lượng từ ít mẫu có thể sai nhiều. Thử thêm hành động ít dữ liệu có thể làm mất phần thưởng ở lần thử đó, nhưng làm ước lượng chính xác hơn cho các lần sau. Ta đo độ bất định đó bằng số trên hai chế độ hút.

::: example Ví dụ 01.9 (Hai chế độ hút)
**Dữ kiện.** Hai chế độ hút A và B. Phần thưởng của mỗi lần hút là tỉ lệ bụi được hút sạch, trong $[0,1]$. Số liệu đã có:

| Chế độ $a$ | Số lần thử $N(a)$ | Tổng phần thưởng | Trung bình mẫu (sample mean) $\bar r(a)$ |
|---|---:|---:|---:|
| A | $20$ | $12{,}00$ | $0{,}60$ |
| B | $2$ | $1{,}10$ | $0{,}55$ |

Hai lần dùng chế độ B cho phần thưởng $0{,}50$ và $0{,}60$.

**Lựa chọn theo ước lượng.** $\bar r(\mathrm A)=0{,}60>0{,}55=\bar r(\mathrm B)$, nên chọn theo ước lượng hiện có là chọn A.

**Độ bất định.**

- Thêm một lần thử B với phần thưởng $r\in[0,1]$ cho trung bình mới $\frac{1{,}1+r}{3}$, nằm trong $\big[\frac{11}{30},\frac7{10}\big]\approx[0{,}367;\,0{,}700]$, một khoảng rộng hơn $0{,}33$ và chứa $0{,}60$ của A.
- Thêm một lần thử A với phần thưởng $r\in[0,1]$ cho trung bình mới $\frac{12+r}{21}$, nằm trong $\big[\frac{12}{21},\frac{13}{21}\big]\approx[0{,}571;\,0{,}619]$, một khoảng rộng $\frac1{21}<0{,}05$ và nằm hoàn toàn trên $0{,}55$ của B.

**Diễn giải.** Chọn A dùng hiểu biết hiện có; chọn B thu thêm thông tin về chế độ còn ít dữ liệu. Lựa chọn tốt hơn phụ thuộc số lần hút còn lại và độ biến động của phần thưởng mỗi chế độ.

**Kiểm tra lại.** $\frac{12}{20}=0{,}60$ và $\frac{0{,}50+0{,}60}{2}=0{,}55$, khớp bảng.
:::

::: definition Định nghĩa 01.16 (Hành động tham lam, khai thác, thăm dò)
Tác tử chọn lặp lại trong một tập hữu hạn hành động. Sau một số lần chọn, với mỗi hành động $a$ đã được thử, $N(a)\ge1$ là số lần $a$ đã được chọn và

$$
\bar r(a)=\frac1{N(a)}\sum_{i=1}^{N(a)}r_i(a)
$$

là trung bình mẫu của các phần thưởng $r_1(a),\dots,r_{N(a)}(a)$ nhận được khi chọn $a$.

**Hành động tham lam theo ước lượng** (greedy action) là hành động thuộc $\arg\max_a\bar r(a)$.

**Khai thác** là chọn một hành động tham lam theo ước lượng hiện có. **Thăm dò** là chọn một hành động không tham lam. Một chính sách có thăm dò nếu nó gán xác suất dương cho ít nhất một hành động không tham lam.
:::

Trung bình mẫu $\bar r(a)$ là ước lượng giá trị hành động (action value) của $a$ trong bài toán chọn lặp lại một bước. Hành động chưa thử lần nào không có trung bình mẫu, nên muốn so sánh nó với các hành động khác, tác tử phải thăm dò ít nhất một lần.

::: remark Nhận xét 01.17 (Về thăm dò và khai thác)
- **Thăm dò thu thông tin cho các quyết định sau.** Trong Ví dụ 01.9, thử B có ích vì ước lượng của B còn bất định nhiều, còn thử A thêm một lần không đổi được quyết định, vì trung bình mới của A ít nhất $\frac{12}{21}\approx0{,}571>0{,}55$.
- **Khai thác quá sớm có thể giữ tác tử ở lựa chọn kém.** Nếu robot luôn chọn A từ nay, ước lượng của B mãi dựa trên hai mẫu, và nếu B thật sự tốt hơn, robot không bao giờ biết.
- **Xung đột chỉ có khi ước lượng còn bất định.** Nếu biết chính xác kỳ vọng phần thưởng của mỗi chế độ, chọn chế độ có kỳ vọng lớn nhất là đủ.
:::

![Hai khối nối với nhau. Khối thăm dò ghi thu dữ liệu. Khối khai thác ghi dùng ước lượng.](img/lec-01/explore-exploit.svg)

Hình trên nối hai việc: thăm dò sinh dữ liệu, dữ liệu làm ước lượng chính xác hơn, và khai thác dùng ước lượng đó (bài giảng gốc 2025–2026, trang 27).

**Trong thực hành.** Tác tử thường dùng chính sách $\varepsilon$-tham lam ($\varepsilon$-greedy): với xác suất $1-\varepsilon$ chọn hành động tham lam theo ước lượng, với xác suất $\varepsilon$ chọn đều trên mọi hành động, nên mọi hành động luôn có xác suất được thử dương.

::: exercise Bài tập 01.6 (Chọn chế độ hút)
Robot có hai chế độ hút A và B; phần thưởng của mỗi lần hút là tỉ lệ bụi được hút sạch, trong $[0,1]$. Chế độ A đã dùng $N(\mathrm A)=20$ lần với trung bình $\bar r(\mathrm A)=0{,}60$. Chế độ B đã dùng $N(\mathrm B)=2$ lần với các phần thưởng $0{,}50$ và $0{,}60$.

- (a) Nêu hành động tham lam theo ước lượng hiện có, và cho biết chọn B ở lần tới là khai thác hay thăm dò.
- (b) Robot thử B thêm một lần và nhận $0{,}90$. Tính $N(\mathrm B)$, $\bar r(\mathrm B)$ mới và hành động tham lam mới.
- (c) Làm lại câu (b) nếu phần thưởng của lần thử thêm là $0{,}40$.
:::

::: hint
Trung bình mới bằng tổng phần thưởng mới chia cho số lần thử mới.
:::

::: solution
**Câu (a).** $\bar r(\mathrm A)=0{,}60>\bar r(\mathrm B)=\frac{0{,}50+0{,}60}{2}=0{,}55$, nên A là hành động tham lam. Chọn B là chọn hành động không tham lam, tức là thăm dò.

**Câu (b).** $N(\mathrm B)=3$ và $\bar r(\mathrm B)=\frac{0{,}50+0{,}60+0{,}90}{3}=\frac{2{,}00}{3}\approx0{,}667$. Vì $0{,}667>0{,}60$, hành động tham lam mới là B.

**Câu (c).** $N(\mathrm B)=3$ và $\bar r(\mathrm B)=\frac{0{,}50+0{,}60+0{,}40}{3}=\frac{1{,}50}{3}=0{,}50$. Hành động tham lam vẫn là A, với khoảng cách lớn hơn trước.

**Kiểm tra lại.** Hai giá trị $\frac{2{,}00}{3}$ và $0{,}50$ nằm trong khoảng $\big[\frac{11}{30},\frac7{10}\big]\approx[0{,}367;\,0{,}700]$ của Ví dụ 01.9, đúng với một lần thử thêm có phần thưởng trong $[0,1]$.
:::

Chính sách, hàm giá trị và mô hình (Định nghĩa 01.11, 01.12, 01.14) tách việc chọn hành động, đánh giá và dự báo; khai thác và thăm dò (Định nghĩa 01.16) được phát biểu bằng ngôn ngữ của chính sách. Tuy nhiên, giá trị $v_\pi(h)$ xác định trên lịch sử, còn khai thác dựa trên ước lượng $\bar r(a)$ của bài toán một bước; để chọn nước trong một ván cờ nhiều bước, chúng ta cần nối giá trị với lựa chọn hành động.

<!-- note-topic-id: lec-01-topic-06 -->
## 5. Tic-tac-toe như một bài toán Học tăng cường

Thế cờ $s$ của Ví dụ 01.6 có bốn nước hợp lệ cho X, và giá trị của nó dưới $\pi_u$ phụ thuộc mọi diễn biến sau nước của X; người chơi lại chỉ nhìn bàn cờ hiện tại. Chúng ta mô hình hóa Tic-tac-toe thành một bài toán Học tăng cường, nêu các điều kiện để viết giá trị trên thế cờ, rồi chọn nước cho X ở $s$ bằng cách so bốn nước theo phần thưởng một bước cộng giá trị của thế cờ kế tiếp.

### 5.1 Thế cờ, phiên đi và tập hành động hợp lệ

Một cách trực quan, ván cờ là một vòng tương tác trong đó X là tác tử, còn bàn cờ, luật chơi và người chơi O là môi trường: X đặt một quân, rồi môi trường trả lời bằng nước của O và báo kết quả nếu ván đã ngã ngũ. Mỗi nước đi của X vì vậy là một bước, còn cả ván cờ là một lượt. Trước hết, ta đọc thế cờ $s$ theo cách nhìn đó.

![Bàn cờ Tic-tac-toe 3 nhân 3. Hàng trên: X ở ô 1, O ở ô 2, ô 3 trống. Hàng giữa: O ở ô 4, X ở ô 5, ô 6 trống. Hàng dưới: ô 7 trống, O ở ô 8, ô 9 trống. Các ô trống 3, 6, 7, 9 mang số hiệu, là bốn hành động hợp lệ.](img/lec-01/tictactoe-board.svg)

Hình trên là thế cờ $s$: các ô đã có quân không mang số, bốn ô trống mang số 3, 6, 7, 9. Từ hình, ta xác định bốn điều.

- **Ai đi trước.** Hai người đánh luân phiên, nên người đi trước có số quân bằng hoặc hơn người kia một quân; O có ba quân, X có hai, nên O đi trước và bây giờ đến phiên X.
- **Chưa ai thắng.** Hai quân X chưa đủ ba; ba quân O ở ô 2, 4, 8 không nằm trên cùng một hàng, cột hay đường chéo.
- **Tập hành động hợp lệ.** X chỉ được đánh vào ô trống, nên $\mathcal A(s)=\{3,6,7,9\}$; ô 5 không hợp lệ vì đã có quân.
- **Chỉ số bước.** Nếu bước $t$ đếm số nước X đã đi, thì $s$ là trạng thái tại $t=2$; bốn ô trống được lấp theo thứ tự X, O, X, O, nên lượt kết thúc chậm nhất ở $T=4$.

::: definition Định nghĩa 01.18 (Tic-tac-toe như một bài toán Học tăng cường)
**Tác tử** là người chơi X. **Môi trường** gồm bàn cờ, luật chơi và đối thủ O. Đối thủ chọn nước theo một chính sách cố định $\sigma(\cdot\mid\tilde s)$, là một phân phối trên các ô trống của thế cờ $\tilde s$ mà O phải đi; trong chương, $\sigma$ chọn đều trên các ô trống.

**Bước** $t=0,1,2,\dots$ đếm số nước X đã đi. Nước của O nằm giữa bước $t$ và bước $t+1$.

**Trạng thái** $S_t$ là thế cờ khi đến phiên X, một phần tử của $\{\mathrm X,\mathrm O,\text{trống}\}^9$. Tác tử quan sát đầy đủ: $O_t=S_t$. Trạng thái đầu $S_0$ là bàn trống nếu X đi trước, là bàn sau nước đầu của O nếu O đi trước.

**Hành động.** $\mathcal A(s)$ là tập các ô trống của $s$, và $A_t\in\mathcal A(S_t)$.

**Luật một bước.** Từ $S_t$ và $A_t$:

1. đặt quân X vào ô $A_t$;
2. nếu X có ba quân thẳng hàng: $R_{t+1}=+1$ và lượt kết thúc;
3. nếu không và bàn đầy: $R_{t+1}=0$ và lượt kết thúc với kết quả hòa;
4. nếu không, O chọn một ô trống theo $\sigma$; nếu O có ba quân thẳng hàng: $R_{t+1}=-1$ và lượt kết thúc; nếu bàn đầy: $R_{t+1}=0$ và lượt kết thúc với kết quả hòa; còn lại: $R_{t+1}=0$ và $S_{t+1}$ là thế cờ mới, đến phiên X.

Mỗi lượt kết thúc sau nhiều nhất $5$ bước, nên $L=5$.
:::

Định nghĩa 01.18 là trường hợp riêng của Định nghĩa 01.1, 01.2 và 01.7, với đối thủ nằm trong môi trường và quan sát đầy đủ. Vì $S_t$ luôn là thế cờ khi đến phiên X, trạng thái không cần ghi phiên của ai.

Nhầm lẫn thường gặp là coi nước của O là một bước riêng của tác tử. Tác tử không chọn nước của O, nên nước đó thuộc môi trường; nếu O thắng ngay sau nước của X, phần thưởng $-1$ thuộc chuyển từ $S_t$, tức là $R_{t+1}$.

<!-- note-topic-id: lec-01-topic-07 -->
### 5.2 Rút gọn lịch sử thành thế cờ

Hai lịch sử khác nhau có thể dẫn tới cùng thế cờ, chẳng hạn khi các quân O ở ô 2, 4, 8 được đặt theo hai thứ tự khác nhau. Để viết $v_\pi(s)$ như người chơi vẫn làm, chúng ta cần biết khi nào giá trị chỉ phụ thuộc thế cờ cuối của lịch sử. Về mặt ý tưởng, giá trị chỉ phụ thuộc thế cờ khi mọi thứ quyết định diễn biến về sau, gồm luật chơi, nước của đối thủ và nước của chính X, chỉ dựa vào thế cờ hiện tại, không dựa vào cách đi tới thế cờ đó.

::: remark Nhận xét 01.19 (Rút gọn lịch sử thành thế cờ)
Giả sử ba điều kiện sau thỏa:

1. tác tử quan sát đầy đủ, $O_t=S_t$;
2. chính sách của đối thủ $\sigma(\cdot\mid\tilde s)$ chỉ phụ thuộc thế cờ $\tilde s$ mà O phải đi;
3. chính sách của tác tử chỉ phụ thuộc thế cờ cuối của lịch sử: $\pi(a\mid h)=\pi(a\mid s)$ khi $h$ kết thúc bằng thế cờ $s$.

Khi đó, với hai lịch sử $h$ và $h'$ đến bước $t$ cùng kết thúc bằng thế cờ $s$, ta có $v_\pi(h)=v_\pi(h')$, và ta viết giá trị chung là $v_\pi(s)$.

Cả $\pi_u$ và $\pi_w$ đều thỏa điều kiện 3. Thời điểm $t$ không cần ghi riêng, vì số quân trên bàn cờ cho biết $t$.
:::

::: proof Chứng minh Nhận xét 01.19
**Bước 1 (một bước).** Với $H_t=h$, theo điều kiện 3, $A_t$ có phân phối $\pi(\cdot\mid s)$. Biết $s$ và $A_t$, luật một bước của Định nghĩa 01.18 cùng điều kiện 2 xác định phân phối của $(R_{t+1},S_{t+1})$ mà không cần phần còn lại của $h$; theo điều kiện 1, thế cờ đó cũng là quan sát kế tiếp.

**Bước 2 (quy nạp theo bước).** Bước 1 là trường hợp $j=t$. Giả sử phân phối đồng thời của $(A_t,R_{t+1},S_{t+1},\dots,A_j,R_{j+1},S_{j+1})$ khi $H_t=h$ chỉ phụ thuộc $s$. Áp Bước 1 cho lịch sử đến bước $j+1$, vốn kết thúc bằng $S_{j+1}$: phân phối có điều kiện của $(A_{j+1},R_{j+2},S_{j+2})$ chỉ phụ thuộc $S_{j+1}$, nên phân phối đồng thời đến bước $j+2$ cũng chỉ phụ thuộc $s$. Vì lượt kết thúc sau nhiều nhất $L$ bước, quy nạp dừng sau hữu hạn bước.

**Bước 3 (kỳ vọng).** $G_t$ là tổng các phần thưởng từ bước $t+1$ đến $T$, nên phân phối của $G_t$, và kỳ vọng của nó, giống nhau dưới $H_t=h$ và $H_t=h'$. $\square$
:::

Mỗi điều kiện có một trường hợp vi phạm cụ thể.

- **Bỏ điều kiện 1.** Nếu X chỉ thấy một phần bàn cờ, cùng một quan sát ứng với nhiều thế cờ, như robot thấy $\text{sạch}$ ở ba ô khác nhau; giá trị theo quan sát không xác định duy nhất.
- **Bỏ điều kiện 2.** Giả sử O chọn đều trên các ô trống, trừ khi nước trước của O là ô 4 thì O đánh ô trống có số nhỏ nhất. Khi đó luật một bước của Định nghĩa 01.18 không còn chỉ phụ thuộc thế cờ: nước của O còn phụ thuộc nước trước của O, một thông tin không có trên bàn cờ dù X thấy toàn bộ bàn cờ. Viết O4 cho "O đánh ô 4" và tương tự. Hai lịch sử O4, X1, O2, X5, O8 và O2, X1, O8, X5, O4 cùng dẫn tới thế cờ $s$ với xác suất dương khi X chọn đều. Sau nước tiếp theo của X, ở lịch sử thứ nhất O chọn đều, ở lịch sử thứ hai O đánh ô nhỏ nhất. Dưới $\pi_u$, ở lịch sử thứ nhất giá trị là $\frac12$; Ví dụ 01.10 ở Mục 5.3 tính con số này. Ở lịch sử thứ hai, O đánh ô trống nhỏ nhất: sau nước 3 của X, O đánh 6 và giá trị của thế cờ còn lại là $1$; sau nước 6 hoặc 7, O đánh 3 và giá trị là $\frac12$; nước 9 thắng ngay. Do đó giá trị là $\frac14\big(1+\frac12+\frac12+1\big)=\frac34\ne\frac12$, nên giá trị phụ thuộc lịch sử.
- **Bỏ điều kiện 3.** Nếu X chọn nước theo một quy tắc nhớ nước trước của chính mình, hai lịch sử cùng thế cờ có thể dẫn tới hai nước khác nhau của X.

### 5.3 Chọn nước bằng giá trị: một ví dụ tính tay

Với thế cờ $s$, chúng ta tính cho từng nước $a$ của X kỳ vọng của lợi tức khi X đánh $a$ rồi tiếp tục theo $\pi_u$. Mỗi nước $a\ne9$ dẫn tới một nước trả lời ngẫu nhiên của O, rồi tới một thế cờ chỉ còn hai ô trống, nơi giá trị tính được như Ví dụ 01.7.

::: example Ví dụ 01.10 (Chọn nước trên thế cờ bốn ô trống)
**Dữ kiện.** Thế cờ $s$: X ở ô 1 và 5; O ở ô 2, 4 và 8; ô 3, 6, 7, 9 trống; đến phiên X, tại bước $t=2$. Luật một bước theo Định nghĩa 01.18; O chọn đều trên các ô trống. Sau nước $A_t=a$, X tiếp tục theo $\pi_u$, chọn đều trên các ô trống. Phần thưởng: $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc; giá trị sau khi lượt kết thúc bằng $0$.

**Nước $a=9$.** X có đường chéo 1–5–9 và thắng: $R_{t+1}=+1$, giá trị phần sau bằng $0$, kỳ vọng của lợi tức là $1$.

**Ba nước còn lại.** Sau $a=3$, $6$ hoặc $7$, X chưa thắng và O không thắng được bằng một nước, vì đường duy nhất O còn có thể hoàn thành là 7–8–9, cần cả ô 7 và ô 9 (với $a=7$, đường này đã bị chặn); phần thưởng của bước là $0$. O trả lời mỗi ô trống với xác suất $\frac13$, để lại hai ô trống; X chọn đều một trong hai ô, và nếu ván chưa kết thúc, O đánh ô cuối. Bảng ghi kết quả của hai lựa chọn của X và giá trị của thế cờ hai ô trống:

| $a$ | O đánh | Hai ô còn trống | X đánh ô thứ nhất | X đánh ô thứ hai | Giá trị |
|---|---|---|---|---|---:|
| $3$ | $6$ | $7,9$ | 7: thắng (3–5–7) | 9: thắng (1–5–9) | $1$ |
| $3$ | $7$ | $6,9$ | 6: O thắng (7–8–9) | 9: thắng | $0$ |
| $3$ | $9$ | $6,7$ | 6: O thắng (7–8–9) | 7: thắng (3–5–7) | $0$ |
| $6$ | $3$ | $7,9$ | 7: hòa | 9: thắng | $\frac12$ |
| $6$ | $7$ | $3,9$ | 3: O thắng (7–8–9) | 9: thắng | $0$ |
| $6$ | $9$ | $3,7$ | 3: O thắng (7–8–9) | 7: hòa | $-\frac12$ |
| $7$ | $3$ | $6,9$ | 6: hòa | 9: thắng | $\frac12$ |
| $7$ | $6$ | $3,9$ | 3: thắng (3–5–7) | 9: thắng | $1$ |
| $7$ | $9$ | $3,6$ | 3: thắng | 6: hòa | $\frac12$ |

Dòng thứ hai là thế cờ của Ví dụ 01.7.

**Tổng hợp.** Lấy trung bình ba dòng của mỗi nước:

$$
\begin{aligned}
a=3:&\quad 0+\tfrac13(1+0+0)=\tfrac13,\\
a=6:&\quad 0+\tfrac13\big(\tfrac12+0-\tfrac12\big)=0,\\
a=7:&\quad 0+\tfrac13\big(\tfrac12+1+\tfrac12\big)=\tfrac23,\\
a=9:&\quad 1+0=1 .
\end{aligned}
$$

Nước có kỳ vọng lớn nhất là $a=9$, nước $6$ có kỳ vọng thấp nhất.

**Giá trị của $s$.** Dưới $\pi_u$, X chọn mỗi nước với xác suất $\frac14$, nên $v_{\pi_u}(s)=\frac14\big(\frac13+0+\frac23+1\big)=\frac12$, tức giá trị của thế cờ $s$ ở Ví dụ 01.6 dưới $\pi_u$.

**Kiểm tra lại.** Theo kết quả cuối dưới $\pi_u$: X thắng với xác suất $\frac14\big(\frac23+\frac13+\frac23+1\big)=\frac23$, O thắng với xác suất $\frac14\big(\frac13+\frac13+0+0\big)=\frac16$, hòa với xác suất $\frac16$; $\frac23-\frac16=\frac12$.
:::

![Bên trái là thế cờ s: X ở ô 1 và 5, O ở ô 2, 4 và 8, các ô 3, 6, 7, 9 trống, đến phiên X. Bốn mũi tên dẫn tới bốn thế cờ sau nước của X, trước nước trả lời của O, mỗi thế cờ đánh dấu ô vừa đánh. Nước a bằng 3: kỳ vọng của R cộng v pi bằng 1/3. Nước a bằng 6: bằng 0. Nước a bằng 7: bằng 2/3. Nước a bằng 9: X thắng ngay, tổng bằng 1. Dòng dưới ghi: O chọn đều trên ô trống, X chọn đều ở các phiên sau, giá trị sau khi kết thúc bằng 0.](img/lec-01/tictactoe-four-moves.svg)

Hình trên tóm tắt Ví dụ 01.10: mỗi nhánh vẽ thế cờ ngay sau nước của X, với ô vừa đánh được đóng khung đứt nét, và ghi kỳ vọng của phần thưởng cộng giá trị phần sau.

### 5.4 Phân tích một bước và nước khai thác một bước

Trong Ví dụ 01.10, với mỗi nước $a$, chúng ta tách kỳ vọng của lợi tức thành hai phần thay vì cộng lợi tức trên toàn bộ cây trò chơi: phần thưởng của bước hiện tại và giá trị của thế cờ kế tiếp theo $\pi_u$. Khi luật của môi trường cố định và lượt hữu hạn, cách tách này đúng cho mọi chính sách trên lịch sử của một lượt chưa kết thúc; viết theo thế cờ, nó cần thêm ba điều kiện của Nhận xét 01.19.

::: proposition Mệnh đề 01.20 (Phân tích một bước)
**Giả thiết.** Môi trường có luật cố định như trong Định nghĩa 01.12 và mọi lượt kết thúc sau nhiều nhất $L$ bước. Cho chính sách $\pi$, một lịch sử $h$ đến bước $t$ của một lượt chưa kết thúc, và một hành động hợp lệ $a$. Ký hiệu $\mathbb E_\pi[\,\cdot\mid H_t=h,A_t=a]$ là kỳ vọng khi tác tử chọn $a$ ở bước $t$ rồi theo $\pi$ từ bước $t+1$. Quy ước $v_\pi(H_{t+1})=0$ nếu lượt kết thúc ở bước $t+1$.

**Kết luận.**

(a) Kỳ vọng của lợi tức sau khi chọn $a$ bằng kỳ vọng của phần thưởng kế tiếp cộng giá trị kế tiếp:

$$
\begin{aligned}
&\mathbb E_\pi\big[G_t\mid H_t=h,A_t=a\big]\\
&\quad=\mathbb E\big[R_{t+1}+v_\pi(H_{t+1})\mid H_t=h,A_t=a\big].
\end{aligned}\tag{5.1}
$$

(b) Giá trị của $h$ là trung bình của các đại lượng ở (5.1) theo $\pi$:

$$
v_\pi(h)=\sum_{a}\pi(a\mid h)\,\mathbb E_\pi\big[G_t\mid H_t=h,A_t=a\big].\tag{5.2}
$$

(c) Trong Tic-tac-toe theo Định nghĩa 01.18, dưới ba điều kiện của Nhận xét 01.19, nếu $h$ kết thúc bằng thế cờ $s$ thì vế phải của (5.1) bằng $\mathbb E\big[R_{t+1}+v_\pi(S_{t+1})\mid S_t=s,A_t=a\big]$, với $v_\pi(S_{t+1})=0$ khi lượt đã kết thúc.

**Điều kiện áp dụng.** Phần (a), (b) không cần quan sát đầy đủ hay tính Markov; phần (c) cần thêm ba điều kiện của Nhận xét 01.19.

**Phạm vi.** Mệnh đề là một hệ thức giữa các giá trị của cùng một chính sách $\pi$, không chiết khấu. Nó không nói nước nào là tốt nhất trong mọi chính sách.
:::

::: proof Chứng minh Mệnh đề 01.20
**Bước 1 (tách lợi tức).** Lượt chưa kết thúc ở bước $t$, nên $t\le T-1$ và theo Mệnh đề 01.9, $G_t=R_{t+1}+G_{t+1}$ trên mọi diễn biến. Lấy kỳ vọng có điều kiện hai vế và dùng tính tuyến tính của kỳ vọng:

$$
\begin{aligned}
&\mathbb E_\pi\big[G_t\mid H_t=h,A_t=a\big]\\
&\quad=\mathbb E\big[R_{t+1}\mid H_t=h,A_t=a\big]\\
&\qquad+\mathbb E_\pi\big[G_{t+1}\mid H_t=h,A_t=a\big].
\end{aligned}
$$

**Bước 2 (điều kiện hóa theo lịch sử kế tiếp).** Lịch sử kế tiếp $H_{t+1}=(h,a,R_{t+1},O_{t+1})$ chứa cả $h$ lẫn $a$. Với mỗi giá trị $h^+$ của $H_{t+1}$, từ bước $t+1$ trở đi tác tử theo $\pi$ và môi trường theo luật cố định, nên kỳ vọng của $G_{t+1}$ dưới điều kiện $H_{t+1}=h^+$ chính là $v_\pi(h^+)$ theo (4.1); nếu lượt đã kết thúc ở bước $t+1$ thì $G_{t+1}=0=v_\pi(h^+)$. Ta có

$$
\begin{aligned}
\mathbb E_\pi\big[G_{t+1}\mid H_t=h,A_t=a\big]
&=\sum_{h^+}\Pr\big(H_{t+1}=h^+\mid H_t=h,A_t=a\big)\,\mathbb E_\pi\big[G_{t+1}\mid H_{t+1}=h^+\big]\\
&=\sum_{h^+}\Pr\big(H_{t+1}=h^+\mid H_t=h,A_t=a\big)\,v_\pi(h^+)\\
&=\mathbb E\big[v_\pi(H_{t+1})\mid H_t=h,A_t=a\big].
\end{aligned}
$$

Đẳng thức thứ nhất là công thức kỳ vọng toàn phần, đẳng thức thứ hai dùng định nghĩa (4.1), đẳng thức thứ ba là định nghĩa của kỳ vọng. Thay vào Bước 1 và gộp hai kỳ vọng theo tính tuyến tính, ta được (5.1).

**Bước 3 (lấy trung bình theo hành động).** Khi $H_t=h$, tác tử theo $\pi$ chọn $A_t=a$ với xác suất $\pi(a\mid h)$. Theo công thức kỳ vọng toàn phần,

$$
\begin{aligned}
v_\pi(h)&=\mathbb E_\pi\big[G_t\mid H_t=h\big]\\
&=\sum_a\pi(a\mid h)\,\mathbb E_\pi\big[G_t\mid H_t=h,A_t=a\big],
\end{aligned}
$$

tức là (5.2). Dưới phân phối của diễn biến bắt đầu từ $h$ (Định nghĩa 01.12), $A_t$ có phân phối $\pi(\cdot\mid h)$, nên công thức kỳ vọng toàn phần áp dụng được; số hạng có $\pi(a\mid h)=0$ đóng góp $0$.

**Bước 4 (rút gọn về thế cờ).** Trong Tic-tac-toe, dưới ba điều kiện của Nhận xét 01.19, lịch sử $H_{t+1}$ của một lượt chưa kết thúc kết thúc bằng thế cờ $S_{t+1}$, và $v_\pi(H_{t+1})=v_\pi(S_{t+1})$. Theo luật một bước của Định nghĩa 01.18 và điều kiện 2, phân phối của $(R_{t+1},S_{t+1})$ khi biết $H_t=h$ và $A_t=a$ chỉ phụ thuộc thế cờ $s$ và $a$. Do đó vế phải của (5.1) bằng $\mathbb E\big[R_{t+1}+v_\pi(S_{t+1})\mid S_t=s,A_t=a\big]$. $\square$
:::

Trong (5.1), vế trái mang chỉ số $\pi$ vì $G_t$ phụ thuộc mọi hành động sau bước $t$. Vế phải chỉ có $\mathbb E$, vì khi biết $h$ và $a$, phân phối của $R_{t+1}$ và $H_{t+1}$ chỉ do luật của môi trường quyết định; chính sách $\pi$ đã nằm trong hàm $v_\pi$.

Mệnh đề 01.20 nói rằng để đánh giá một hành động, ta không cần nhìn tới cuối lượt: chỉ cần phần thưởng của bước kế tiếp và giá trị của tình huống kế tiếp, cả hai lấy kỳ vọng. Ví dụ 01.10 là phần (c) với $\pi=\pi_u$, và phép tính $v_{\pi_u}(s)=\frac12$ là phần (b). Mỗi giả thiết có vai trò riêng.

- **Bỏ lượt hữu hạn.** Bước 1 dựa vào Mệnh đề 01.9, mà hệ thức của nó không xác định khi lượt không dừng.
- **Bỏ luật cố định.** Nếu cách O chọn nước thay đổi theo số ván đã chơi, kỳ vọng của $G_{t+1}$ dưới cùng lịch sử $h^+$ không còn là một số cố định $v_\pi(h^+)$, và Bước 2 không còn đúng.
- **Bỏ một điều kiện của Nhận xét 01.19.** Phần (a) vẫn đúng trên lịch sử, nhưng Bước 4 không dùng được và phần (c) không xác định, như ở trường hợp bỏ điều kiện 2 của Nhận xét 01.19, khi đối thủ nhớ nước trước của mình.

::: definition Định nghĩa 01.21 (Nước khai thác một bước)
Trong Tic-tac-toe theo Định nghĩa 01.18, cho chính sách $\pi$ thỏa các điều kiện của Nhận xét 01.19 và hàm giá trị $v_\pi$ của nó. Tại thế cờ $s$ chưa kết thúc, một **nước khai thác một bước** theo $v_\pi$ là một nước

$$
a^*\in\arg\max_{a\in\mathcal A(s)}\mathbb E\big[R_{t+1}+v_\pi(S_{t+1})\mid S_t=s,A_t=a\big],\tag{5.3}
$$

với $v_\pi(S_{t+1})=0$ khi lượt đã kết thúc. Khi tập $\arg\max$ có nhiều phần tử, một **quy tắc phá hòa** (tie-breaking) cố định, chẳng hạn chọn ô có số nhỏ nhất, xác định nước được chọn. Trên lịch sử, định nghĩa tương tự dùng vế phải của (5.1).
:::

Định nghĩa 01.21 đưa khai thác của Định nghĩa 01.16 vào bài toán nhiều bước: ước lượng $\bar r(a)$ được thay bằng đại lượng ở (5.3), theo Mệnh đề 01.20 bằng kỳ vọng của lợi tức khi chọn $a$ rồi tiếp tục theo $\pi$. Trên thế cờ $s$ với $\pi=\pi_u$, (5.3) cho $a^*=9$.

::: remark Nhận xét 01.22 (Giới hạn của nước khai thác một bước)
- **Nước khai thác một bước phụ thuộc $\pi$.** Đại lượng trong (5.3) đánh giá việc tiếp tục theo $\pi$, không đánh giá việc tiếp tục chơi tốt nhất; đổi chính sách tiếp tục thì tập $\arg\max$ có thể đổi (Bài tập 01.8).
- **Không bảo đảm tối ưu.** Chọn $a^*$ ở mỗi bước theo $v_\pi$ của một chính sách $\pi$ kém không bảo đảm cho chính sách tốt nhất. Bài 04 chứng minh, cho quá trình quyết định Markov hữu hạn với $0\le\gamma<1$, rằng chính sách chọn $a^*$ ở mọi trạng thái không kém $\pi$, và lặp lại xen kẽ đánh giá và khai thác dẫn tới chính sách tối ưu.
- **Cần mô hình.** Tính (5.3) cần biết phân phối của $(R_{t+1},S_{t+1})$, tức là cần luật cờ và chính sách $\sigma$ của đối thủ: đó là lập kế hoạch với một mô hình đã biết (Định nghĩa 01.14). Khi không biết $\sigma$, các đại lượng trong (5.3) phải được ước lượng từ các ván đã chơi, và luôn chọn $a^*$ khi đó là khai thác thuần túy, không thăm dò.
:::

**Trong thực hành.** Sutton và Barto (2018, §1.5) giải Tic-tac-toe bằng một bảng ước lượng giá trị cho từng thế cờ: phần lớn thời gian người chơi khai thác theo bảng, thỉnh thoảng thăm dò, và sau mỗi nước khai thác dịch ước lượng của thế cờ trước về phía ước lượng của thế cờ sau, tức một cập nhật sai phân thời gian (temporal-difference learning, TD). Đại lượng trong (5.3) chỉ phụ thuộc thế cờ ngay sau nước của X, gọi là trạng thái sau nước đi (afterstate; Sutton và Barto 2018, §6.8), nên chỉ cần lưu giá trị cho các trạng thái này, như hình của Ví dụ 01.10.

::: exercise Bài tập 01.7 (Biểu diễn một thế cờ có ô 2, 6, 8 trống)
Thế cờ $u$: X ở ô 3, 4 và 9; O ở ô 1, 5 và 7; các ô 2, 6, 8 trống. Ô đánh số 1 đến 9 theo hàng, từ trái sang phải, từ trên xuống dưới. Phần thưởng của X theo Định nghĩa 01.18: $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc.

- (a) Xác định ai đi trước, đến phiên ai, và tập hành động hợp lệ $\mathcal A(u)$.
- (b) Một biểu diễn cho X chọn ô 5. Biểu diễn đó sai ở đâu.
- (c) X đánh ô 6. Xác định $R_{t+1}$, lượt có kết thúc không, và giá trị của lịch sử ngay sau nước đó.
:::

::: hint
Kiểm tra cột 3–6–9 sau khi X đánh ô 6.
:::

::: solution
**Câu (a).** X và O cùng có ba quân, nên người đi trước là X, và bây giờ lại đến phiên X. Kiểm tra chưa ai thắng: các đường đầy đủ trên bàn cờ là 1–5–9, 3–5–7 và 1–4–7, và mỗi đường có cả X lẫn O. Tập hành động hợp lệ là $\mathcal A(u)=\{2,6,8\}$.

**Câu (b).** Ô 5 đã có quân O, nên $5\notin\mathcal A(u)$; nước này không hợp lệ.

**Câu (c).** Sau khi X đánh ô 6, X có ô 3, 6, 9 trên cùng cột 3–6–9, nên X thắng: $R_{t+1}=+1$ và lượt kết thúc. Theo Định nghĩa 01.12, giá trị của lịch sử đã kết thúc bằng $0$.

**Kiểm tra lại.** Các đường qua ô 2 (1–2–3, 2–5–8) và qua ô 8 (7–8–9, 2–5–8) đều có quân O, nên chỉ nước 6 cho X thắng ngay.
:::

::: exercise Bài tập 01.8 (Nước khai thác một bước theo một chính sách khác)
Thế cờ $s$: X ở ô 1 và 5; O ở ô 2, 4 và 8; các ô 3, 6, 7, 9 trống; đến phiên X. Luật một bước theo Định nghĩa 01.18, đối thủ O chọn đều trên các ô trống. Sau nước đầu, X tiếp tục theo chính sách $\pi_w$: nếu có nước làm X thắng ngay thì đánh nước đó, nếu có nhiều nước như vậy thì chọn đều trong số đó, nếu không có thì chọn đều trên các ô trống. Phần thưởng: $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc.

Bảng sau cho giá trị $v_{\pi_w}$ của thế cờ sau nước trả lời của O, trừ một ô cần tính:

| Nước $a$ | O đánh ô | Giá trị $v_{\pi_w}$ của thế cờ kế tiếp |
|---|---|---:|
| $3$ | $6$; $7$; $9$ | $1$; $1$; $1$ |
| $6$ | $3$; $7$; $9$ | $1$; $1$; chưa biết |
| $7$ | $3$; $6$; $9$ | $1$; $1$; $1$ |

- (a) Tính giá trị $v_{\pi_w}$ của thế cờ sau nước 6 của X và nước 9 của O.
- (b) Tính $\mathbb E[R_{t+1}+v_{\pi_w}(S_{t+1})\mid S_t=s,A_t=a]$ cho bốn nước, và tập $\arg\max$ trong (5.3).
- (c) Dùng quy tắc phá hòa "chọn ô có số nhỏ nhất" để xác định nước khai thác một bước, rồi so với Ví dụ 01.10.
:::

::: hint
Với hai ô trống, trước hết kiểm tra X có nước thắng ngay không; nếu có, $\pi_w$ đánh nước đó.
:::

::: solution
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

**Kiểm tra lại.** Ở câu (a), X không có nước thắng ngay, nên $\pi_w$ và $\pi_u$ cùng chọn đều, và giá trị $-\frac12$ trùng dòng $a=6$, O đánh 9 trong bảng của Ví dụ 01.10.
:::

Trên Tic-tac-toe, Mệnh đề 01.20 cho phép chọn nước bằng phần thưởng kỳ vọng cộng giá trị của thế cờ kế tiếp. Tuy nhiên, nước khai thác một bước chỉ tốt theo chính sách đang được đánh giá (Nhận xét 01.22), và phép tính cần biết mô hình của đối thủ.

## Tình huống áp dụng và ứng dụng

Hai tình huống sau quay lại robot dọn dãy bốn ô.

::: application Tình huống 01.1 (Đánh giá chính sách chọn đều của robot và chọn hành động đầu tiên)
**Bài toán và môi trường.** Robot dọn dãy bốn ô bắt đầu ở ô 1; chỉ ô 4 có rác. Ba hành động $\text{trái}$, $\text{phải}$, $\text{hút}$; $\text{trái}$ và $\text{phải}$ dịch robot một ô, robot đứng yên nếu đi ra ngoài dãy. Hút ở ô 4 khi còn rác cho phần thưởng $+1$ và kết thúc lượt; mọi bước khác cho $0$. Lượt bị cắt sau $L=4$ hành động. Cần so sánh chính sách $\pi_1$ (thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$) với chính sách chọn đều $\pi_u$, chọn mỗi hành động với xác suất $\frac13$; sau đó chọn hành động đầu tiên bằng nước khai thác một bước theo $v_{\pi_u}$.

**Mô hình hóa.** Tác tử là bộ chọn hành động của robot; trạng thái là cặp $(\text{vị trí},\text{tình trạng ô 4})$ và quan sát là $\text{sạch}$ hoặc $\text{bẩn}$ (Định nghĩa 01.1, 01.2); lượt, lợi tức và giá trị theo Định nghĩa 01.7, 01.8 và 01.12.

**Kiểm tra giả thiết.**

1. Luật của môi trường cố định (ở đây là tất định), nên Mệnh đề 01.20(a), (b) áp dụng được.
2. Lượt hữu hạn: $T\le4$.
3. Giá trị chỉ phụ thuộc vị trí $k$ và số hành động còn lại $m=4-t$, vì ba lý do:
   - vị trí ban đầu đã biết và luật dịch chuyển tất định, nên $k$ là một hàm của lịch sử;
   - chính sách $\pi_u$ không dùng lịch sử, nên không cần điều kiện quan sát đầy đủ của Nhận xét 01.19;
   - luật của môi trường chỉ phụ thuộc vị trí, tình trạng ô 4, vốn luôn là "còn rác" khi lượt chưa kết thúc, và số hành động còn lại.

   Ta viết giá trị đó là $w(k,m)$, với $w(k,0)=0$ vì lượt bị cắt.

**Giá trị của $\pi_1$.** Với lịch sử ban đầu $h_0=(\text{sạch})$, lượt dưới $\pi_1$ luôn là $\text{phải},\text{phải},\text{phải},\text{hút}$ với $T=4\le L$, nên $v_{\pi_1}(h_0)=1$.

**Áp dụng Mệnh đề 01.20(a) và (b) cho $\pi_u$.** Từ ô $k$, robot cần $4-k$ lần $\text{phải}$ và một lần $\text{hút}$, nên $w(k,m)=0$ khi $m<5-k$, tức $k+m<5$. Từ $(1,4)$, mọi cặp $(k,m)$ đạt được thỏa $k+m\le5$, nên chỉ còn bốn giá trị cần tính: $w(4,1)$, $w(3,2)$, $w(2,3)$ và $w(1,4)$. Mỗi giá trị là trung bình với trọng số $\frac13$ của "phần thưởng cộng giá trị kế tiếp" cho $\text{trái}$, $\text{phải}$, $\text{hút}$; từ ô 1, $\text{trái}$ và $\text{hút}$ đều giữ robot ở ô 1:

$$
\begin{aligned}
w(4,1)&=\tfrac13\big(w(3,0)+w(4,0)+1\big)\\
&=\tfrac13,\\
w(3,2)&=\tfrac13\big(w(2,1)+w(4,1)+w(3,1)\big)\\
&=\tfrac13\cdot\tfrac13=\tfrac19,\\
w(2,3)&=\tfrac13\big(w(1,2)+w(3,2)+w(2,2)\big)\\
&=\tfrac13\cdot\tfrac19=\tfrac1{27},\\
w(1,4)&=\tfrac13\big(w(1,3)+w(2,3)+w(1,3)\big)\\
&=\tfrac13\cdot\tfrac1{27}=\tfrac1{81}.
\end{aligned}
$$

Vậy $v_{\pi_u}(h_0)=w(1,4)=\frac1{81}\approx0{,}012$.

**Chọn hành động đầu tiên theo Định nghĩa 01.21.** Theo (5.1), tại $h_0$, kỳ vọng của lợi tức khi chọn $a$ rồi theo $\pi_u$ là

$$
\begin{aligned}
a=\text{trái}:&\quad 0+w(1,3)=0,\\
a=\text{phải}:&\quad 0+w(2,3)=\tfrac1{27},\\
a=\text{hút}:&\quad 0+w(1,3)=0.
\end{aligned}
$$

Nước khai thác một bước là $\text{phải}$, trùng hành động đầu của $\pi_1$.

**Diễn giải.** Chính sách chọn đều chỉ hút được rác khi gặp đúng dãy $\text{phải},\text{phải},\text{phải},\text{hút}$, xác suất khoảng $1{,}2\%$. Phép so sánh một bước theo $v_{\pi_u}$ vẫn chỉ ra hành động đầu đúng, dù $\pi_u$ là một chính sách kém.

**Giới hạn.** Phép tính dùng luật đã biết của môi trường, nên đây là lập kế hoạch với mô hình (Định nghĩa 01.14). Bảng $w(k,m)$ cần vị trí $k$, mà robot chỉ biết khi tự suy ra từ lịch sử; cảm biến không báo vị trí.

**Dẫn ngược lý thuyết.** Định nghĩa 01.7, 01.8, 01.12; Mệnh đề 01.20(a), (b) ở bước tính $w$, dùng giả thiết 1–3; Định nghĩa 01.21 và (5.1) ở bước chọn hành động.

**Kiểm tra lại.** Với $L=4$, dãy duy nhất thành công là $\text{phải},\text{phải},\text{phải},\text{hút}$, xác suất $\big(\frac13\big)^4=\frac1{81}$; theo (5.2), $\frac13\big(0+\frac1{27}+0\big)=\frac1{81}$.
:::

::: application Tình huống 01.2 (Ghi giá trị theo quan sát khi quan sát không đủ thông tin)
**Bài toán và môi trường.** Robot dọn dãy bốn ô bắt đầu ở ô 1; chỉ ô 4 có rác; $\text{trái}$, $\text{phải}$ dịch một ô, đứng yên nếu đi ra ngoài dãy; hút ở ô 4 khi còn rác cho $+1$ và kết thúc lượt, mọi bước khác cho $0$; $L=5$. Cảm biến chỉ báo ô đang đứng $\text{sạch}$ hay $\text{bẩn}$. Robot dùng $\pi_1$: thấy $\text{sạch}$ thì $\text{phải}$, thấy $\text{bẩn}$ thì $\text{hút}$. Để tiết kiệm bộ nhớ, người thiết kế muốn lưu hai số $V(\text{sạch})$ và $V(\text{bẩn})$ thay cho giá trị trên lịch sử.

**Mô hình hóa.** Tác tử là bộ chọn hành động của robot; trạng thái là cặp $(\text{vị trí},\text{tình trạng ô 4})$, quan sát là $\text{sạch}$ hoặc $\text{bẩn}$; hàm $V$ của quan sát cuối $O_t$ thay cho $v_{\pi_1}(h)$.

**Giả thiết bị vi phạm.** Quan sát $\text{sạch}$ ứng với ba vị trí 1, 2, 3, nên điều kiện quan sát đầy đủ (điều kiện 1 của Nhận xét 01.19) không thỏa.

**Hai lịch sử cùng quan sát.** Xét hai lịch sử đến bước $t=2$, cùng có $O_2=\text{sạch}$ và còn ba hành động:

- $h_a=(\text{sạch},\text{phải},0,\text{sạch},\text{phải},0,\text{sạch})$: robot đi từ ô 1 tới ô 3;
- $h_b=(\text{sạch},\text{trái},0,\text{sạch},\text{hút},0,\text{sạch})$: robot vẫn ở ô 1.

**Tính giá trị theo Định nghĩa 01.12.** Từ $h_a$, $\pi_1$ chọn $\text{phải}$ tới ô 4, thấy $\text{bẩn}$ rồi hút: $R_3=0$, $R_4=1$, $T=4$, nên $v_{\pi_1}(h_a)=1$. Từ $h_b$, $\pi_1$ chọn $\text{phải}$ ba lần, robot tới ô 4 đúng lúc lượt bị cắt ở $T=5$, nên $v_{\pi_1}(h_b)=0$.

**Diễn giải và giới hạn.** Một số $V(\text{sạch})$ duy nhất không thể bằng cả $1$ lẫn $0$, nên mọi lựa chọn của nó đánh giá sai ít nhất một trong hai lịch sử. Mệnh đề 01.20(a) vẫn đúng trên lịch sử, nhưng phần (c) không dùng được với quan sát thay cho trạng thái. Một biểu diễn đủ thông tin phải tính được từ lịch sử, chẳng hạn vị trí $k$ suy ra bằng cách áp luật dịch chuyển từ ô 1 cùng số hành động còn lại.

**Dẫn ngược lý thuyết.** Định nghĩa 01.2, Nhận xét 01.3; Định nghĩa 01.12; Nhận xét 01.19, điều kiện 1 là giả thiết bị vi phạm; Mệnh đề 01.20(a) và (c).

**Kiểm tra lại.** Ở $h_b$, ba lần $\text{phải}$ đưa robot tới ô 2, 3, 4 ở các bước $3$, $4$, $5$; lượt bị cắt sau hành động thứ năm, trước khi robot kịp hút.
:::

**Liên hệ với các bài sau.**

- **Bài 02.** Trạng thái có tính Markov thay cho lịch sử của Định nghĩa 01.2, và hệ số chiết khấu được thêm vào lợi tức (3.1).
- **Bài 03.** Hệ thức (5.2) của Mệnh đề 01.20, viết cho quá trình quyết định Markov, là phương trình Bellman kỳ vọng (Bellman expectation equation) của $v_\pi$.
- **Bài 04.** Phép tính $w(k,m)$ ở Tình huống 01.1 là đánh giá chính sách (policy evaluation) khi biết mô hình; lặp lại xen kẽ phép tính đó với nước khai thác một bước của Định nghĩa 01.21 cho thuật toán lặp chính sách (policy iteration).
- **Bài 05.** Monte Carlo lấy trung bình các lợi tức tính ngược theo Mệnh đề 01.9; sai phân thời gian dùng (3.2) với $G_{t+1}$ thay bằng một ước lượng để cập nhật ngay sau mỗi bước, không chờ hết lượt.
- **Bài 06.** Thăm dò và khai thác của Định nghĩa 01.16 trở thành chính sách $\varepsilon$-tham lam trong Sarsa và Q-learning.
- **Bài 07–08.** Hàm giá trị của Định nghĩa 01.12 được biểu diễn bằng hàm có tham số và mạng nơ-ron khi bảng quá lớn.
- **Bài 09–11.** Chính sách của Định nghĩa 01.11 được tham số hóa và tối ưu trực tiếp theo kỳ vọng của lợi tức.

## Tóm tắt chương

Xuất phát từ một robot phải chọn hành động khi đánh giá chỉ đến sau cả chuỗi hành động, chúng ta đặt tên cho vòng tương tác (Định nghĩa 01.1), trạng thái, quan sát và lịch sử (Định nghĩa 01.2), rồi phân biệt phần thưởng với nhãn (Định nghĩa 01.5). Hậu quả dài hạn được đo bằng lợi tức (Định nghĩa 01.8) với hệ thức $G_t=R_{t+1}+G_{t+1}$ (Mệnh đề 01.9). Chính sách, hàm giá trị và mô hình (Định nghĩa 01.11, 01.12, 01.14) tách việc chọn, đánh giá và dự báo; khi ước lượng còn bất định, khai thác xung đột với thăm dò (Định nghĩa 01.16). Kết quả chính của chương là Mệnh đề 01.20: kỳ vọng của lợi tức sau một hành động bằng phần thưởng kỳ vọng cộng giá trị kỳ vọng của tình huống kế tiếp, viết được trên thế cờ dưới ba điều kiện của Nhận xét 01.19. Nước khai thác một bước (Định nghĩa 01.21) chọn $a^*=9$ ở thế cờ bốn ô trống, với $v_{\pi_u}(s)=\frac12$. Giá trị trên lịch sử khó lưu trữ, giá trị theo quan sát có thể sai (Tình huống 01.2), và nước khai thác một bước chưa chắc tối ưu; Bài 02 đến Bài 04 xử lý các giới hạn này.

**Định nghĩa và kết quả theo mục.**

- Mục 1: tác tử chọn $A_t$, môi trường trả $R_{t+1}$ và $O_{t+1}$ (Định nghĩa 01.1); lịch sử $H_t$ là toàn bộ dữ liệu của tác tử, còn trạng thái $S_t$ nằm trong môi trường (Định nghĩa 01.2); hai trạng thái khác nhau có thể cho cùng một quan sát (Nhận xét 01.3); một mô hình viết sẵn không tự sửa khi môi trường đổi (Nhận xét 01.4).
- Mục 2: phần thưởng là một số đánh giá, không cho biết hành động đúng như nhãn (Định nghĩa 01.5); dữ liệu tương tác không độc lập, không cùng phân phối và phụ thuộc các hành động đã chọn (Nhận xét 01.6).
- Mục 3: lượt kết thúc tại $T\le L$ (Định nghĩa 01.7); lợi tức $G_t$ là tổng các phần thưởng từ bước $t+1$ đến $T$ (Định nghĩa 01.8); $G_t=R_{t+1}+G_{t+1}$, $G_T=0$ (Mệnh đề 01.9); giả thuyết phần thưởng: mọi mục tiêu đều mô tả được bằng việc làm lớn nhất kỳ vọng của tổng phần thưởng (Nhận xét 01.10).
- Mục 4: chính sách gán cho mỗi lịch sử một phân phối trên tập hành động hợp lệ (Định nghĩa 01.11); $v_\pi(h)$ là kỳ vọng của lợi tức từ $h$ khi tác tử theo $\pi$ (Định nghĩa 01.12); giá trị khác phần thưởng và bằng $0$ sau khi lượt kết thúc (Nhận xét 01.13); mô hình dự báo phản hồi của môi trường và được dùng để lập kế hoạch (Định nghĩa 01.14); dự báo của mô hình có thể sai (Nhận xét 01.15); khai thác chọn hành động tham lam theo ước lượng, thăm dò chọn hành động khác (Định nghĩa 01.16); xung đột giữa hai việc chỉ có khi ước lượng còn bất định (Nhận xét 01.17).
- Mục 5: Tic-tac-toe là bài toán quan sát đầy đủ, với đối thủ thuộc môi trường (Định nghĩa 01.18); giá trị viết được trên thế cờ dưới ba điều kiện (Nhận xét 01.19); kỳ vọng của lợi tức sau hành động $a$ bằng phần thưởng kỳ vọng cộng giá trị kỳ vọng của tình huống kế tiếp (Mệnh đề 01.20); nước khai thác một bước làm lớn nhất đại lượng đó (Định nghĩa 01.21); nước này phụ thuộc $\pi$, không bảo đảm tối ưu và cần mô hình (Nhận xét 01.22).

**Công thức cần nhớ.** Lợi tức của lượt hữu hạn và hệ thức đệ quy:

$$
\begin{aligned}
G_t&=\sum_{k=t+1}^{T}R_k,\\
G_t&=R_{t+1}+G_{t+1},\qquad G_T=0 .
\end{aligned}
$$

Hàm giá trị trên lịch sử:

$$
v_\pi(h)=\mathbb E_\pi\big[G_t\mid H_t=h\big].
$$

Phân tích một bước và nước khai thác một bước trong Tic-tac-toe:

$$
\begin{aligned}
v_\pi(s)&=\sum_{a}\pi(a\mid s)\,\mathbb E\big[R_{t+1}+v_\pi(S_{t+1})\mid S_t=s,A_t=a\big],\\
a^*&\in\arg\max_{a\in\mathcal A(s)}\mathbb E\big[R_{t+1}+v_\pi(S_{t+1})\mid S_t=s,A_t=a\big].
\end{aligned}
$$

**Giả thiết hay bị bỏ quên.**

- Giá trị sau khi lượt kết thúc bằng $0$; phần thưởng của nước thắng nằm ở $R_{t+1}$, không nằm ở giá trị của thế cờ sau đó.
- Giá trị luôn gắn với một chính sách cố định; đổi chính sách thì đổi giá trị.
- Viết giá trị trên thế cờ hay trạng thái cần quan sát đầy đủ, và cần các luật, kể cả đối thủ, cùng chính sách của tác tử chỉ phụ thuộc thế cờ hiện tại; nếu không, giá trị phải viết trên lịch sử.
- Lợi tức không chiết khấu chỉ xác định khi lượt hữu hạn.
- Tập hành động hợp lệ phụ thuộc trạng thái.
- Nước khai thác một bước dùng mô hình đã biết của đối thủ và chỉ tốt theo chính sách đang được đánh giá.

## Bài tập củng cố

### Mức nhận biết

::: exercise Bài tập 01.9 (Ba thành phần trong AlphaGo)
Chương trình AlphaGo (Silver và cộng sự, 2016; bài giảng gốc 2025–2026, trang 11) chơi cờ vây, trò chơi hai người trên bàn $19\times19$, bằng ba bộ phận:

- một mạng nơ-ron cho phân phối xác suất trên các nước đi hợp lệ từ một thế cờ;
- một mạng nơ-ron cho một số ước lượng kết quả ván cờ từ một thế cờ khi các nước sau được chọn theo một cách chơi cố định;
- một phép tìm kiếm cây (tree search) mô phỏng các nước đi tương lai bằng luật cờ vây.

Phần thưởng là $+1$ khi thắng, $-1$ khi thua ở cuối ván, $0$ ở các nước khác.

- (a) Mỗi bộ phận ứng với thành phần nào trong ba thành phần chính sách, hàm giá trị, mô hình.
- (b) AlphaGo có lập kế hoạch theo Định nghĩa 01.14 không.
:::

::: hint
Chính sách cho phân phối trên hành động; hàm giá trị cho một số; mô hình cho dự báo về điều xảy ra sau một hành động.
:::

::: solution
**Câu (a).** Mạng cho phân phối trên các nước đi là một chính sách (Định nghĩa 01.11). Mạng cho một số ước lượng kết quả ván cờ khi các nước sau theo một cách chơi cố định là một ước lượng của hàm giá trị (Định nghĩa 01.12). Luật cờ vây dùng trong tìm kiếm là một mô hình (Định nghĩa 01.14).

**Câu (b).** Có. Phép tìm kiếm cây dùng luật cờ để xét các nước đi tương lai trước khi đánh, đúng định nghĩa lập kế hoạch; AlphaGo là phương pháp có mô hình.

**Kiểm tra lại.** Câu (a) gán đủ ba bộ phận cho ba thành phần, không trùng thành phần nào.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 01.10 (Lợi tức theo hai góc nhìn trong Tic-tac-toe)
Trong Tic-tac-toe theo Định nghĩa 01.18, phần thưởng của X là $+1$ khi X thắng, $-1$ khi O thắng, $0$ khi hòa và ở bước chưa kết thúc.

- (a) Một ván kết thúc ở $T=4$ với $(R_1,R_2,R_3,R_4)=(0,0,0,-1)$. Tính $G_0,G_1,G_2,G_3,G_4$ và cho biết ai thắng.
- (b) Nếu mô hình hóa cùng ván từ góc nhìn của O, với phần thưởng của O bằng đối của phần thưởng của X ở mỗi bước, lợi tức $G_0$ của O bằng bao nhiêu.
:::

::: hint
Dùng $G_T=0$ và $G_t=R_{t+1}+G_{t+1}$, tính từ cuối về đầu; đổi dấu mọi phần thưởng thì đổi dấu mọi tổng.
:::

::: solution
**Câu (a).** $G_4=0$; $G_3=R_4+G_4=-1$; $G_2=R_3+G_3=-1$; $G_1=R_2+G_2=-1$; $G_0=R_1+G_1=-1$. Phần thưởng cuối $-1$ cho biết O thắng. $G_4=0$ không mâu thuẫn với $R_4=-1$: $R_4$ thuộc chuyển cuối, đã được tính trong $G_3,\dots,G_0$.

**Câu (b).** Phần thưởng của O là $(0,0,0,+1)$, nên $G_0=0+0+0+1=1$, đối của $G_0$ của X.

**Kiểm tra lại.** Cộng trực tiếp: $G_0$ của X là $0+0+0+(-1)=-1$, và tổng lợi tức của hai người bằng $0$.
:::

### Mức vận dụng

::: exercise Bài tập 01.11 (Bàn tay robot xoay khối: có mô hình hay phi mô hình)
Một bàn tay robot ba ngón, như trong bài giảng gốc (2025–2026, trang 13), phải xoay một khối lập phương để mặt có đánh dấu hướng lên trên. Mỗi bước, bộ điều khiển gửi một lệnh cho các khớp; camera và cảm biến khớp cho ảnh của khối và góc các khớp. Phần thưởng là $+1$ ở bước cuối nếu mặt đánh dấu hướng lên, $0$ ở mọi bước khác; lượt bị cắt sau $50$ bước. Ở bài này, trạng thái và quan sát nhận giá trị liên tục, khác với giả thiết tập hữu hạn của Định nghĩa 01.2; bài chỉ yêu cầu nhận diện các thành phần. Có hai phương án.

**P1.** Dùng một bộ mô phỏng vật lý của bàn tay và khối để thử trước các chuỗi lệnh, rồi thực hiện chuỗi tốt nhất trên robot thật.

**P2.** Học trực tiếp trên robot thật từ các lượt thử.

- (a) Xác định tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng; nêu một lý do khiến quan sát khác trạng thái.
- (b) P1 và P2 là phương pháp có mô hình hay phi mô hình.
- (c) Nêu một tình huống làm kế hoạch của P1 thất bại trên robot thật, và một chi phí của P2.
:::

::: hint
So bộ mô phỏng với môi trường thật theo Nhận xét 01.15.
:::

::: solution
**Câu (a).** Tác tử là bộ điều khiển; môi trường gồm bàn tay, khối và các định luật vật lý. Trạng thái gồm tư thế thật của khối, góc và vận tốc các khớp, lực tiếp xúc; quan sát là ảnh camera và góc khớp; hành động là lệnh cho các khớp; phần thưởng như đề bài. Quan sát khác trạng thái vì camera không đo lực tiếp xúc và ngón tay có thể che một phần khối.

**Câu (b).** P1 có mô hình: bộ mô phỏng là mô hình, và việc thử trước các chuỗi lệnh là lập kế hoạch (Định nghĩa 01.14). P2 phi mô hình nếu tác tử học chính sách hoặc giá trị trực tiếp từ các lượt thử mà không xây bộ dự báo nào.

**Câu (c).** Nếu hệ số ma sát trong bộ mô phỏng khác ma sát thật, khối trượt khác dự báo, và một chuỗi lệnh thành công trong mô phỏng có thể làm rơi khối trên robot thật; đó là mô hình khác môi trường (Nhận xét 01.15). P2 cần nhiều lượt thử trên robot thật, tốn thời gian và làm mòn thiết bị.

**Kiểm tra lại.** Câu (b) dùng đúng tiêu chí của Định nghĩa 01.14: có hay không dùng mô hình để lập kế hoạch.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Bài giảng gốc (2025–2026), *Reinforcement Learning and Planning*, bài 1, Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội: trang 4–9 cho Mục 1; trang 11–13 cho Bài tập 01.9 và 01.11; trang 17–21 cho Mục 2; trang 23–25 cho Mục 3; trang 26–27 cho Mục 4; trang 28–30 cho Mục 5; trang 14–15 và 43–44 cho phần đọc thêm dưới đây.
- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press: §1.1 (tr. 1–4) cho Mục 1–2; §1.3–1.4 (tr. 6–8) cho Mục 1.3 và 4.1–4.3; §1.5 (tr. 8–13) cho Mục 5; §2.1–2.2 (tr. 25–28) cho Mục 4.4; §3.1–3.3 (tr. 47–57) cho Định nghĩa 01.1, 01.7, 01.8, Mệnh đề 01.9 và Nhận xét 01.10; §3.5 (tr. 58) cho Định nghĩa 01.12; §6.8 (tr. 136–137) cho trạng thái sau nước đi; §8.1 (tr. 159–161) cho Định nghĩa 01.14; §17.3 (tr. 464) cho Tình huống 01.2.
- Silver, D. (2015), *Lectures on Reinforcement Learning*, University College London, bài 1: cùng bộ khái niệm tác tử, môi trường, lịch sử, trạng thái, chính sách, giá trị, mô hình với các ví dụ khác, cho Mục 1 và 4.
- Silver, D. và cộng sự (2016), "Mastering the game of Go with deep neural networks and tree search", *Nature* 529, tr. 484–489: Bài tập 01.9.
- Goodfellow, I., Bengio, Y. và Courville, A. (2016), *Deep Learning*, MIT Press, §5.1.3: học có giám sát và học không giám sát ở Mục 2.
- Giáo trình *Học máy thống kê*, chương Học tăng cường, mục giới thiệu quá trình quyết định Markov: cách dẫn dắt từ học có giám sát sang tương tác và thuật ngữ tiếng Việt của Mục 1–4.

<!-- note-topic-id: lec-01-topic-11 -->
### Đọc thêm: tác tử nhiều nhiệm vụ và mô hình thế giới

Bài giảng gốc (2025–2026, trang 14–15 và 43–44) nêu một quan điểm gắn Học tăng cường với trí tuệ nhân tạo tổng quát (artificial general intelligence) và với tác tử dùng chung cho nhiều nhiệm vụ, cùng câu hỏi trí tuệ nhân tạo tổng quát có cần một mô hình thế giới (world model) hay không. Hai điểm vào là chính sách (Định nghĩa 01.11), khi một chính sách phải dùng cho nhiều nhiệm vụ, và mô hình (Định nghĩa 01.14), khi một mô hình thế giới học được dùng để lập kế hoạch. Chủ đề này được giao dưới dạng bài tìm hiểu, Bài tập 01.16 của [tệp bài tập](material-viewer.html?doc=materials/lec-01/exercises.md&deck=lecture-01-gioi-thieu-hoc-tang-cuong.html).
