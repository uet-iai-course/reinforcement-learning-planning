# Bài 09 — Double DQN và gradient chính sách

**Giảng viên:** Tạ Việt Cường, Ph.D. — Phòng thí nghiệm HMI, Trường Đại học Công nghệ
**Học kỳ:** Học kỳ 1, 2026–2027 · **Môn:** Học tăng cường (AIT3007)
**Thời lượng:** 120 phút chính + 30 phút ba bài tập (X01–X03)
**Nguồn chính:** `lecture09-ddqn-and-policy-gradient-part1.pdf`, 40 trang; ghi trang nguồn ở từng chủ đề.

## Mục tiêu quan sát được

Sau bài học, sinh viên làm được bốn việc:

1. Tính sai lệch cực đại trên ước lượng nhiễu bằng ví dụ Rademacher và phát biểu bất đẳng thức Jensen đúng phạm vi.
2. Viết đích Double DQN có cờ kết thúc và stop-gradient, phân biệt với Double Q-learning dạng bảng, và tính tay cả hai đích.
3. Tham số hóa chính sách bằng softmax hoặc Gaussian phương sai cố định và tính hàm điểm $\psi_\theta$.
4. Suy ra gradient chính sách theo tỷ số xác suất, loại phần thưởng quá khứ bằng lập luận nhân quả, và thực hiện một bước REINFORCE episodic với quy ước chiết khấu nhất quán.

## Bản đồ chủ đề — bốn nhóm

| Nhóm | Chủ đề | Vai trò |
|---|---|---|
| **Cầu nối** | topic-01, topic-13 | Nối Bài 08 vào vấn đề sai lệch cực đại; nối phương sai REINFORCE sang Bài 10 |
| **Cốt lõi** | topic-02, 03, 05, 06, 07, 08, 09, 10, 12 | Sai lệch cực đại, Double DQN, Double Q-learning, chính sách là phân phối, mục tiêu và hàm điểm, tỷ số xác suất, REINFORCE |
| **Bổ sung** | topic-04, topic-11 | Phạm vi tác dụng của Double DQN; phân bố chiếm dụng chiết khấu |
| **Đọc thêm** | topic-14 | Sai phân hữu hạn, đối chiếu ngoài tuyến chính |

## Bảy mạch — 120 phút

| # | Mạch | Thời lượng | Chủ đề |
|---|---|---|---|
| 1 | Ôn DQN và đặt sai lệch cực đại | 12 phút | topic-01, 02 |
| 2 | Double DQN và phạm vi | 20 phút | topic-03, 04 |
| 3 | Double Q-learning dạng bảng | 13 phút | topic-05 |
| 4 | Chính sách là phân phối | 15 phút | topic-06 |
| 5 | Mục tiêu, giả thiết và hàm điểm | 25 phút | topic-07, 08, 09 |
| 6 | Tỷ số xác suất, nhân quả và REINFORCE | 27 phút | topic-10, 12 |
| 7 | Hai cách viết định lý, đọc thêm và kết nối | 8 phút | topic-11, 14, 13 |

Tổng: 120 phút. Ba bài tập X01–X03 dùng 30 phút sau phần chính.

## Ký hiệu và quy ước

- $Q_\theta$: mạng **online**, nhận gradient. $Q_{\theta^-}$: mạng **mục tiêu**, bản sao trễ, không nhận gradient.
- $Z_i\in\{0,1\}$: cờ kết thúc của chuyển tiếp $i$; $Z_i=1$ nghĩa là $S'_i$ là trạng thái kết thúc.
- $\operatorname{sg}(u)=u$ ở lượt thuận, đạo hàm bằng $0$ (dừng gradient, stop-gradient).
- $T<\infty$ hầu chắc chắn; $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$ với $0\le\gamma<1$; $J(\theta)=\mathbb E_{\tau\sim p_\theta}[G_0]$.
- $\pi_\theta(a\mid s)$: **xác suất** ở hành động rời rạc, **mật độ** ở hành động liên tục.
- $\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$: hàm điểm (score function).
- $\rho_0$: phân phối trạng thái khởi đầu; $P$: động lực chuyển tiếp; cả hai không phụ thuộc $\theta$.
- Sau thời điểm kết thúc $T$, nối một trạng thái hấp thụ với phần thưởng và giá trị bằng $0$.
- Bài giả sử quan sát đầy đủ $O=S$. Nếu $O=h(S)$ làm mất thông tin, cần biểu diễn hoặc bộ nhớ đủ thông tin; thay $S$ bằng $O$ trong mạng không làm quan sát tự có tính Markov.

---

## Mạch 1 — Ôn DQN và đặt sai lệch cực đại (12 phút)

<!-- note-topic-id: lec-09-topic-01 -->
### DQN còn ghép chọn với đánh giá

**Vấn đề.** Với dạng bảng chính xác, Q-learning hội tụ dưới các giả thiết tiêu chuẩn. Với mạng neural, huấn luyện có thể phân kỳ vì hai nguyên nhân: tương quan giữa các mẫu và mục tiêu không dừng (tr. 3–4).

**Trực giác.** Mục tiêu DQN chứa $\max_{a'}Q_{\theta^-}(s',a')$: khi mạng thay đổi, mục tiêu thay đổi theo — mô hình đuổi theo một mục tiêu đang di chuyển (tr. 4).

**Hai công cụ đã học ở Bài 08** (tr. 5–10):

- **Bộ nhớ phát lại (experience replay):** lưu $(s,a,r,s')$ vào bộ đệm, lấy mini-batch ngẫu nhiên — phá tương quan theo thời gian, tái sử dụng dữ liệu.
- **Target network:** duy trì $Q_{\theta^-}$ để tính đích, sao chép $\theta^-\leftarrow\theta$ theo chu kỳ $C$ bước — làm đích thay đổi chậm.

Hàm mất mát trên lô $b$ mẫu:

$$L_B(\theta)=\frac1b\sum_{i=1}^{b}\big[\operatorname{sg}(y_i)-Q_\theta(S_i,A_i)\big]^2,$$

với đích DQN từng trường hợp:

$$y_i=\begin{cases}R_i,&Z_i=1,\\ R_i+\gamma\max_{a'}Q_{\theta^-}(S'_i,a'),&Z_i=0.\end{cases}$$

Gradient chỉ đi qua $Q_\theta(S_i,A_i)$; đích và mạng mục tiêu không nhận gradient.

**Giới hạn còn lại.** Replay và mạng mục tiêu xử lý hai cơ chế khác nhau, nhưng **không tách việc chọn hành động khỏi việc đánh giá hành động**: trong $\max_{a'}Q_{\theta^-}(s',a')$, cùng một bộ ước lượng vừa chọn vừa đánh giá. Đây là chủ đề của topic-02.

**Kiểm tra.** Trong đích DQN, biến nào chọn hành động ở $s'$? — Chính $Q_{\theta^-}$, qua phép max.

*Nguồn: tr. 3–10.*

<!-- note-topic-id: lec-09-topic-02 -->
### Sai lệch cực đại và ví dụ Rademacher

**Vấn đề.** Viết $\widehat Q_a=Q^*_a+\varepsilon_a$ với $\mathbb E[\varepsilon_a]=0$. Từng ước lượng không chệch, nhưng

$$\max_a\widehat Q_a=\max_a\big(Q^*_a+\varepsilon_a\big)$$

nhiều khả năng lớn hơn $\max_a Q^*_a$, vì phép max có xu hướng chọn hành động có hiện thực nhiễu thuận lợi (tr. 12–13). Cùng một mẫu nhiễu quyết định cả hành động thắng lẫn giá trị được báo cáo.

::: example
**Ví dụ Rademacher.** Hai hành động có giá trị thật bằng $0$. Nhiễu $\varepsilon_1,\varepsilon_2$ độc lập, nhận $-1$ hoặc $1$ với xác suất $1/2$. Từng ước lượng: $\mathbb E[\widehat Q_1]=\mathbb E[\widehat Q_2]=0$. Bốn cặp $(\varepsilon_1,\varepsilon_2)$ đồng xác suất: $(-1,-1)$ cho $\max=-1$; ba cặp còn lại cho $\max=1$. Do đó

$$\mathbb E\big[\max_a\widehat Q_a\big]=\tfrac14(-1)+\tfrac34(1)=\tfrac12\neq 0=\max_a\mathbb E[\widehat Q_a].$$

Sai lệch dương xuất hiện dù từng ước lượng không chệch.
:::

**Hình thức.** Hàm cực đại theo véc-tơ là hàm lồi, nên Jensen cho

$$\mathbb E\Big[\max_a\widehat Q_a\Big]\ \ge\ \max_a\mathbb E[\widehat Q_a].$$

Phạm vi phát biểu: đây là **bất đẳng thức không nghiêm** nói chung. Dấu bằng có thể xảy ra (ví dụ một hành động luôn thắng); dấu nghiêm cần điều kiện bổ sung về phân phối nhiễu và quan hệ giữa các ước lượng. Không phát biểu "mọi lần lấy max đều đánh giá quá cao" — kết luận là về kỳ vọng.

**Nhu cầu.** Vì sai lệch này lặp lại qua bootstrap và có thể dẫn đến mất ổn định hoặc phân kỳ, cần tách **chọn** và **đánh giá** hành động bằng hai bộ ước lượng khác nhau.

**Kiểm tra.** Trong ví dụ Rademacher, vì sao $\max_a\mathbb E[\widehat Q_a]=0$? — Vì $\mathbb E[\widehat Q_a]=0$ với cả hai hành động.

*Nguồn: tr. 11–13.*

---

## Mạch 2 — Double DQN và phạm vi (20 phút)

<!-- note-topic-id: lec-09-topic-03 -->
### Đích Double DQN

**Trực giác.** Tách hai vai trò của phép max: mạng online **chọn** hành động kế tiếp tốt nhất theo thứ hạng hiện tại, mạng mục tiêu **đánh giá** hành động đã chọn (tr. 14–16).

**Hình thức.** Với tập hành động hữu hạn $\mathcal A$, đặt

$$a_i^*=\arg\max_{a\in\mathcal A}Q_\theta(S'_i,a)\quad\text{if }Z_i=0,$$

và đích từng trường hợp:

$$y_i=\begin{cases}R_i,&Z_i=1,\\ R_i+\gamma\,\operatorname{sg}\!\big(Q_{\theta^-}(S'_i,a_i^*)\big),&Z_i=0.\end{cases}$$

Ba điểm bắt buộc:

- **Không gọi argmax ở nhánh terminal:** khi $Z_i=1$, đích là $R_i$; tính $a_i^*$ tại trạng thái kết thúc là vô nghĩa.
- **$\operatorname{sg}$ chặn gradient:** đích và mạng mục tiêu không nhận gradient; chỉ $Q_\theta(S_i,A_i)$ đi qua loss.
- **Hòa argmax:** cài đặt phải ghi quy tắc phá hòa.

::: example
**Đối chiếu hai đích.** Cho $r=1$, $\gamma=0{,}9$, $Z=0$, $Q_{\theta^-}(s',\cdot)=(5,4)$, $Q_\theta(s',\cdot)=(3,6)$.

- **DQN:** mạng mục tiêu vừa chọn vừa đánh giá — chọn hành động 1 (giá trị $5$), đích $y^{\mathrm{DQN}}=1+0{,}9\cdot 5=5{,}5$.
- **Double DQN:** mạng online chọn hành động 2 (giá trị $6$), mạng mục tiêu đánh giá $4$, đích $y^{\mathrm{DDQN}}=1+0{,}9\cdot 4=4{,}6$.

Chênh lệch không chứng minh Double DQN luôn gần giá trị thật hơn trong từng mẫu; cơ chế nhằm giảm liên hệ giữa nhiễu tạo thứ hạng và nhiễu tạo giá trị đánh giá.
:::

**Ứng dụng và giới hạn.** Double DQN chỉ thay công thức bootstrap, không thay hướng gradient của loss. Nó giảm sai lệch đánh giá quá cao, làm giá trị Q ổn định hơn và thứ hạng hành động đáng tin cậy hơn (tr. 17).

**Kiểm tra.** Trong ví dụ trên, nếu hoán đổi hai bộ giá trị thì hai đích đổi thành bao nhiêu? — Khi hoán đổi, mạng mục tiêu mới là $(3,6)$ và mạng online mới là $(5,4)$. DQN có mạng mục tiêu vừa chọn vừa đánh giá: max của $(3,6)$ là $6$, nên đích $1+0{,}9\cdot 6=6{,}4$. Double DQN dùng mạng online $(5,4)$ chọn hành động 1, rồi mạng mục tiêu $(3,6)$ đánh giá hành động 1 bằng $3$, nên đích $1+0{,}9\cdot 3=3{,}7$.

*Nguồn: tr. 14–16.*

<!-- note-topic-id: lec-09-topic-04 -->
### Phạm vi tác dụng của Double DQN

**Phát biểu giới hạn đúng** (tr. 17–19):

- Double DQN **không** tự loại bỏ tương quan mẫu — đó là việc của replay.
- Double DQN **không** tự loại bỏ tính không dừng của mục tiêu — đó là việc của target network.
- Double DQN **không** bảo đảm hội tụ với mọi kiến trúc mạng neural tùy ý.
- Có thể gây học chậm trong một số hoàn cảnh.

**Vì sao hai mạng không độc lập.** $\theta^-$ là bản sao trễ của $\theta$, nên hai sai số đánh giá có quan hệ; không được dùng lập luận độc lập như trong Double Q-learning lý tưởng để mô tả hai mạng sâu. Tách chọn–đánh giá **thường giảm** sai lệch cực đại, không buộc sai lệch bằng $0$.

**Vị trí của bộ tối ưu.** RMSprop/Adam/SGD ảnh hưởng đến cách tham số được tối ưu; Double DQN ảnh hưởng đến mục tiêu mà bộ tối ưu phải khớp. Hai cải tiến xử lý hai vấn đề khác nhau.

**Kiểm tra.** Kết luận về chất lượng cần dựa trên gì? — Nhiều lần chạy và thước đo đánh giá, không chỉ loss huấn luyện.

*Nguồn: tr. 17–19.*

---

## Mạch 3 — Double Q-learning dạng bảng (13 phút)

<!-- note-topic-id: lec-09-topic-05 -->
### Double Q-learning dạng bảng

**Nguyên tắc double.** Duy trì hai bảng $Q_1,Q_2$; mỗi bước cập nhật **một** bảng, bảng còn lại đánh giá hành động do bảng đang cập nhật chọn (tr. 20–21).

**Hình thức.** Khởi tạo $Q_1,Q_2$ tùy ý, $Q_1(\text{terminal},\cdot)=Q_2(\text{terminal},\cdot)=0$. Chính sách hành vi (ví dụ $\varepsilon$-greedy trên $Q_1+Q_2$) chọn $A$; sau khi quan sát $(R,S',Z)$, với xác suất $1/2$ cập nhật bảng thứ nhất:

$$a^*=\arg\max_{a\in\mathcal A}Q_1(S',a),\qquad Z=0,$$

$$y_1=\begin{cases}R,&Z=1,\\ R+\gamma Q_2(S',a^*),&Z=0,\end{cases}$$

$$Q_1(S,A)\leftarrow Q_1(S,A)+\alpha\,[y_1-Q_1(S,A)].$$

Nhánh còn lại hoán đổi $Q_1\leftrightarrow Q_2$. Hai điểm bắt buộc:

- **Che bootstrap khi terminal:** khi $Z=1$, đích là $R$, không tính argmax trên trạng thái kết thúc.
- **Chọn bằng bảng đang cập nhật, đánh giá bằng bảng kia:** $Q_1$ chọn, $Q_2$ đánh giá. Lấy $\max$ của $Q_2$ sẽ phá cơ chế tách.

::: example
**Tính tay.** Cho $Q_1(S,A)=4$, $\alpha=0{,}1$, $R=1$, $\gamma=0{,}9$, $Z=0$. Tại $S'$: $Q_1=(2,1)$, $Q_2=(1,4)$.

- $Q_1$ chọn $a^*=1$ (giá trị $2$); $Q_2$ đánh giá hành động 1 bằng $1$.
- $y_1=1+0{,}9\cdot 1=1{,}9$.
- $Q_1^{\mathrm{new}}(S,A)=4+0{,}1\,(1{,}9-4)=3{,}79$.
:::

**So sánh hai cách tách** (tr. 14–21):

| | Double Q-learning | Double DQN |
|---|---|---|
| biểu diễn | hai bảng $Q_1,Q_2$ | online $Q_\theta$, target $Q_{\theta^-}$ |
| cập nhật | chọn ngẫu nhiên một bảng | luôn cập nhật online |
| đánh giá | bảng còn lại | bản sao trễ |
| dữ liệu | thường trực tuyến | thường từ replay |

Cùng nguyên tắc tách chọn–đánh giá, nhưng **không phải cùng thuật toán**. Tên "Double" không cho phép suy ra tùy ý rằng bốn hay tám bộ ước lượng sẽ tốt hơn: thêm bộ ước lượng làm đổi thuật toán, chi phí và quan hệ tương quan.

**Kiểm tra.** Double Q-learning cập nhật mấy bảng trong một bước? — Một bảng; bảng kia chỉ đánh giá.

*Nguồn: tr. 20–21.*

---

## Mạch 4 — Chính sách là phân phối (15 phút)

<!-- note-topic-id: lec-09-topic-06 -->
### Chính sách trực tiếp là phân phối hành động

**Vấn đề của học giá trị.** $Q_\theta$ kết hợp với argmax quá tất định: argmax chỉ trả một hành động, khó dùng trực tiếp cho hành động liên tục, và trong biểu diễn đặc trưng kém (ví dụ ô xám che hai hướng E và W đều tối ưu), hàm Q buộc chọn một trong hai và đều lệch với phương án tối ưu (tr. 22–25).

**Trực giác.** Thay vì học giá trị rồi trích chính sách bằng argmax, tham số hóa **trực tiếp** một phân phối hành động $\pi_\theta:s\mapsto\mathcal P(\cdot\mid s)$ để lấy mẫu (tr. 25–29).

**Hai giới hạn cần nói đúng:**

- Trong MDP quan sát đầy đủ, một chính sách **tất định** tối ưu có thể tồn tại; không cần ngẫu nhiên hóa để đạt tối ưu. Lợi ích của tham số hóa trực tiếp là giao diện lấy mẫu khả vi và miền hành động liên tục, không phải "ngẫu nhiên tốt hơn".
- **Không nói chính sách ngẫu nhiên tự khôi phục thông tin trạng thái đã mất:** nếu hai trạng thái cho cùng biểu diễn, cùng tham số chính sách tạo cùng phân phối hành động. Muốn quyết định khác nhau, cần biểu diễn hoặc bộ nhớ đủ thông tin.

**Điều khiển và học.** Tại $s$: lấy $A\sim\pi_\theta(\cdot\mid s)$ rồi gửi cho môi trường; học bằng cách điều chỉnh $\theta$ để tăng xác suất của hành động gắn với return cao.

**Kiểm tra.** Chính sách trực tiếp có phải hệ quả của Double DQN không? — Không; nó là một lựa chọn biểu diễn độc lập.

*Nguồn: tr. 22–29.*

---

## Mạch 5 — Mục tiêu, giả thiết và hàm điểm (25 phút)

<!-- note-topic-id: lec-09-topic-07 -->
### Mục tiêu episodic và giả thiết

**Quy ước.** $S_0\sim\rho_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$, $R_{t+1}$ nhận sau $A_t$, $0\le\gamma<1$, $T<\infty$ hầu chắc chắn:

$$G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},\qquad J(\theta)=\mathbb E_{\tau\sim p_\theta}[G_0].$$

Sau $T$, nối một trạng thái hấp thụ có phần thưởng và giá trị bằng $0$ — quy ước này cho phép dùng tổng vô hạn mà không đổi mục tiêu episodic (tr. 30–32, 39–40).

**Bài toán tối ưu.** Cực đại hóa $J(\theta)$; cập nhật $\theta\leftarrow\theta+\alpha\,\widehat g$ với $\widehat g\approx\nabla_\theta J(\theta)$, $\alpha>0$. Dấu cộng vì mục tiêu được cực đại hóa (tr. 30–33).

**Giả thiết** (tr. 33–40) — chi phối toàn bộ suy diễn sau này:

1. $\rho_0$ và động lực $P$ **không phụ thuộc** $\theta$.
2. $\pi_\theta$ khả vi, có **miền hỗ trợ cố định** và dương tại hành động được lấy mẫu.
3. $G_0\nabla_\theta\log p_\theta(\tau)$ khả tích; có điều kiện (ví dụ một chặn trội phù hợp) cho phép đổi đạo hàm với tích phân.
4. $S_t$ là trạng thái Markov; sau kết thúc dùng tiếp diễn hấp thụ.

Miền hỗ trợ thay đổi theo $\theta$ có thể sinh thêm hạng biên.

**Kiểm tra.** Vì sao dấu cập nhật là cộng? — Vì ta cực đại hóa $J$, không cực tiểu hóa loss.

*Nguồn: mục tiêu ở tr. 30–34; các điều kiện support và khả tích được làm rõ để dùng cho suy diễn ở tr. 39.*

<!-- note-topic-id: lec-09-topic-08 -->
### Hàm điểm softmax

**Hàm điểm.** Với hành động đã lấy mẫu và $\pi_\theta(a\mid s)>0$:

$$\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s),\qquad \nabla_\theta\pi_\theta(a\mid s)=\pi_\theta(a\mid s)\,\psi_\theta(s,a).$$

Đồng nhất thức đạo hàm log chỉ hợp lệ tại nơi xác suất hoặc mật độ dương (tr. 34).

**Softmax cho hành động rời rạc.** Cho đặc trưng $\phi(s,a)\in\mathbb R^d$ cố định khi lấy đạo hàm theo $\theta$, logit $z_a(s)=\phi(s,a)^\top\theta$:

$$\pi_\theta(a\mid s)=\frac{e^{\phi(s,a)^\top\theta}}{\sum_b e^{\phi(s,b)^\top\theta}},\qquad \psi_\theta(s,a)=\phi(s,a)-\sum_b\pi_\theta(b\mid s)\,\phi(s,b).$$

Hàm điểm là đặc trưng của hành động chọn trừ trung bình đặc trưng theo chính sách; do đó $\mathbb E_{A\sim\pi_\theta}[\psi_\theta(s,A)]=0\in\mathbb R^d$. Nếu $\phi$ cũng có tham số học, công thức phải dùng quy tắc dây chuyền đầy đủ (tr. 35–36).

::: example
**Ví dụ hai hành động.** $\pi_\theta(1\mid s)=2/3$, $\pi_\theta(2\mid s)=1/3$, $\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$:

$$\psi_\theta(s,1)=(1,0)-\big(\tfrac23,\tfrac13\big)=\big(\tfrac13,-\tfrac13\big),\qquad \psi_\theta(s,2)=\big(-\tfrac23,\tfrac23\big).$$

Tổng có trọng số: $\tfrac23(\tfrac13,-\tfrac13)+\tfrac13(-\tfrac23,\tfrac23)=(0,0)$.
:::

**Kiểm tra.** Kỳ vọng có điều kiện của hàm điểm dưới chính sách bằng gì? — $0\in\mathbb R^d$.

*Nguồn: tr. 35–36.*

<!-- note-topic-id: lec-09-topic-09 -->
### Hàm điểm Gaussian phương sai cố định

**Hành động liên tục.** Lấy mẫu $A\mid S=s\sim\mathcal N(\mu_\theta(s),\sigma^2)$ với $\mu_\theta(s)=\phi(s)^\top\theta$; giữ $\phi(s)\in\mathbb R^d$ và $\sigma^2>0$ cố định (tr. 37–38):

$$\psi_\theta(s,a)=\frac{a-\mu_\theta(s)}{\sigma^2}\,\phi(s)\in\mathbb R^d.$$

- Hành động lớn hơn trung bình cho phần dư dương → tăng log mật độ của hành động đó.
- Phương sai nhỏ khuếch đại độ lớn hàm điểm.
- Công thức chỉ là gradient theo tham số trung bình; nếu $\phi$ hoặc $\sigma$ phụ thuộc $\theta$, cần đạo hàm thêm theo quy tắc dây chuyền.
- Với hành động bị chặn, Gaussian không biến đổi có thể sinh hành động ngoài miền; có thể cần biến đổi.

::: example
**Tính tay.** $\phi(s)=(1,2)$, $\theta=(0,0)$ nên $\mu=0$, $\sigma^2=1$, $a=1{,}5$:

$$\psi_\theta(s,a)=\frac{1{,}5-0}{1}\,(1,2)=(1{,}5,\,3).$$

Nếu hệ số return âm, hướng hàm điểm bị đảo và bước cập nhật làm giảm log mật độ của hành động vừa lấy mẫu; một mẫu đơn lẻ không bảo đảm cải thiện chính sách.
:::

**Kiểm tra.** Góc lái liên tục phù hợp với họ phân phối nào? — Gaussian.

*Nguồn: tr. 37–38.*

---

## Mạch 6 — Tỷ số xác suất, nhân quả và REINFORCE (27 phút)

<!-- note-topic-id: lec-09-topic-10 -->
### Tỷ số xác suất và nhân quả

**Tỷ số xác suất (likelihood ratio).** Với $J(\theta)=\int G_0(\tau)\,p_\theta(\tau)\,\mathrm d\tau$ và các giả thiết ở topic-07:

::: derivation
$$\nabla_\theta J(\theta)=\int G_0(\tau)\,\nabla_\theta p_\theta(\tau)\,\mathrm d\tau=\mathbb E_{\tau\sim p_\theta}\!\big[G_0\,\nabla_\theta\log p_\theta(\tau)\big].$$

Dòng đầu dùng điều kiện đổi đạo hàm–tích phân; dòng sau dùng $\nabla_\theta p_\theta=p_\theta\nabla_\theta\log p_\theta$.
:::

**Phân tích xác suất quỹ đạo.** Vì $\rho_0$ và $P$ không phụ thuộc $\theta$:

$$p_\theta(\tau)=\rho_0(s_0)\prod_{t=0}^{T-1}\pi_\theta(a_t\mid s_t)\,P(s_{t+1},r_{t+1}\mid s_t,a_t),\qquad \nabla_\theta\log p_\theta(\tau)=\sum_{t=0}^{T-1}\psi_\theta(s_t,a_t).$$

Gradient của xác suất quỹ đạo gom thành tổng hàm điểm từng bước (tr. 39–40).

**Lập luận nhân quả loại phần thưởng quá khứ.** Đặt $H_t=(S_0,A_0,R_1,\ldots,A_{t-1},R_t,S_t)$. Không cần giả sử các phần thưởng độc lập với hành động:

::: derivation
Với $A_t\sim\pi_\theta(\cdot\mid S_t)$ (rời rạc: thay tích phân bằng tổng theo $a$):

$$\mathbb E_{A_t\sim\pi_\theta}\!\big[\psi_t\mid H_t\big]=\nabla_\theta\!\int_{\mathcal A}\pi_\theta(a\mid S_t)\,\mathrm da=0,$$

trong đó $\psi_t=\psi_\theta(S_t,A_t)$ là hàm điểm tại bước $t$.

Với $G_{<t}=\sum_{k=0}^{t-1}\gamma^kR_{k+1}$ đo được theo $H_t$, ta có $G_0=G_{<t}+\gamma^tG_t$, và vì $G_{<t}$ đo được trước khi lấy mẫu $A_t$:

$$\mathbb E\big[G_{<t}\,\psi_t\big]=0\quad\Longrightarrow\quad \mathbb E\Big[G_0\sum_t\psi_t\Big]=\mathbb E\Big[\sum_t\gamma^tG_t\,\psi_t\Big].$$
:::

Đây là lập luận nhân quả (điều kiện theo lịch sử), **không phải** giả thiết độc lập. Hệ số $\gamma^t$ không được bỏ: nó đi kèm quy ước $J(\theta)=\mathbb E[G_0]$.

**Kiểm tra.** Vì sao $\mathbb E[G_{<t}\psi_t]=0$? — $G_{<t}$ đo được theo $H_t$, còn kỳ vọng có điều kiện của $\psi_t$ theo $H_t$ bằng $0$.

*Nguồn: tr. 39–40.*

<!-- note-topic-id: lec-09-topic-12 -->
### REINFORCE episodic

**Thuật toán Monte Carlo** (tr. 40; sửa thứ tự thu thập và hệ số chiết khấu so với nguồn — sửa có chủ ý để nhất quán với $J(\theta)=\mathbb E[G_0]$):

1. Khởi tạo $\theta$ tùy ý, chọn $\alpha>0$, $0\le\gamma<1$.
2. Với mỗi episode: chép $\theta_{\mathrm{old}}\leftarrow\theta$; thu **trọn episode** dưới $\pi_{\theta_{\mathrm{old}}}$; giữ $\theta_{\mathrm{old}}$ cố định đến khi cộng xong.
3. Tính mọi $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$ lùi từ $T-1$ về $0$.
4. Cộng $\widehat g=\sum_{t=0}^{T-1}\gamma^tG_t\,\psi_{\theta_{\mathrm{old}}}(S_t,A_t)$.
5. Cập nhật **một lần**: $\theta\leftarrow\theta_{\mathrm{old}}+\alpha\,\widehat g$.

Không tuyên bố không chệch/hội tụ nếu thiếu các giả thiết ở topic-07. Đây là ước lượng một mẫu; từng episode không bảo đảm cải thiện $J$.

::: example
**Áp dụng cho softmax.** Dùng lại $\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$, $\theta=(\log 2,0)$ nên $\pi_\theta(1\mid s)=2/3$, $\psi_\theta(s,1)=(\tfrac13,-\tfrac13)$. Một episode một bước chọn hành động 1, nhận $G_0=3$; $\alpha=0{,}1$:

$$\widehat g=3\big(\tfrac13,-\tfrac13\big)=(1,-1),\qquad \theta_{\mathrm{new}}=(\log 2+0{,}1,\,-0{,}1),$$

$$\pi_{\theta_{\mathrm{new}}}(1\mid s)=\frac{2e^{0{,}1}}{2e^{0{,}1}+e^{-0{,}1}}\approx0{,}710>\tfrac23.$$

Return dương tăng chênh lệch logit giữa hai hành động thêm $0{,}2$, nên xác suất của hành động đã nhận return dương tăng.
:::

**Kiểm tra.** Vì sao cập nhật một lần sau episode thay vì từng bước? — Vì $G_t$ cần toàn bộ phần thưởng tương lai của episode và $\theta_{\mathrm{old}}$ phải cố định trong khi thu.

*Nguồn: tr. 40.*

---

## Mạch 7 — Hai cách viết định lý, đọc thêm và kết nối (8 phút)

<!-- note-topic-id: lec-09-topic-11 -->
### Phân bố chiếm dụng chiết khấu

Phần bổ sung; có thể lược khi thiếu thời gian.

Đặt $Q^\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$. Nếu chân trời cưỡng bức phụ thuộc $t$, ghép $t$ vào trạng thái; trạng thái hấp thụ có $Q^\pi=0$. Phân bố chiếm dụng chuẩn hóa:

$$d_{\rho_0,\gamma}^{\pi}(s)=(1-\gamma)\sum_{t\ge0}\gamma^t\Pr_\pi(S_t=s),$$

với hệ số $1/(1-\gamma)$ bảo đảm $\sum_s d^\pi(s)=1$. Trọng số $\gamma^t$ trong ước lượng quỹ đạo chính là trọng số tạo phân bố lượt thăm — lượt thăm muộn được tính ít hơn. Khi đó:

$$\mathbb E\Big[\sum_{t\ge0}\gamma^tG_t\psi_t\Big]=\frac1{1-\gamma}\,\mathbb E_{S\sim d^\pi,\,A\sim\pi}\!\big[Q^\pi(S,A)\,\psi_\theta(S,A)\big]=\nabla_\theta J(\theta),$$

vì kỳ vọng có điều kiện thay $G_t$ bằng $Q^\pi$. Đây là **cách viết thứ hai** của cùng một định lý: dạng quỹ đạo (topic-10) và dạng phân bố chiếm dụng. Các giả thiết khả vi, miền hỗ trợ và khả tích đã nêu ở topic-07 vẫn áp dụng.

*Nguồn: tr. 39 và suy diễn.*

<!-- note-topic-id: lec-09-topic-14 -->
### Đọc thêm: sai phân hữu hạn

Đọc thêm, ngoài tuyến chính. Từ định nghĩa đạo hàm, xấp xỉ từng thành phần:

$$\frac{\partial J(\theta)}{\partial\theta_k}\approx\frac{J(\theta+\epsilon u_k)-J(\theta)}{\epsilon},$$

với $u_k$ là véc-tơ đơn vị hướng $k$ (tr. 33). Đơn giản, áp dụng được cho chính sách bất kỳ kể cả không khả vi, nhưng nhiễu lớn, kém hiệu quả khi số tham số lớn — vì vậy tuyến chính của bài dùng hàm điểm thay vì sai phân.

*Nguồn: tr. 33.*

<!-- note-topic-id: lec-09-topic-13 -->
### Cầu nối: baseline và actor–critic

Baseline và actor–critic được triển khai ở Bài 10.

Ước lượng $\widehat g=\sum_t\gamma^tG_t\psi_t$ dùng return Monte Carlo nên có phương sai lớn. Bài kế tiếp dùng **baseline** để giảm phương sai mà không gây chệch, và **actor–critic** để bootstrap giá trị thay vì chờ hết episode. Hai trong bốn hợp đồng của bài này — hàm điểm chỉ dùng nơi mật độ dương, chỉ số return nhất quán — vẫn giữ nguyên khi thêm baseline.

*Nguồn: tr. 40, chỉ báo trước.*

---

## Bốn hợp đồng cần giữ

1. **Double DQN:** online chọn; target đánh giá; kết thúc che bootstrap; đích dừng gradient.
2. **Chính sách:** phân phối đúng miền hành động (xác suất ở rời rạc, mật độ ở liên tục); hàm điểm chỉ dùng nơi mật độ dương.
3. **REINFORCE:** chỉ số return nhất quán ($\gamma^tG_t$); thu dưới tham số cũ; cộng rồi cập nhật một lần.
4. **Sai lệch cực đại:** thu hồi bất đẳng thức Jensen $\mathbb E\big[\max_a\widehat Q_a\big]\ge\max_a\mathbb E[\widehat Q_a]$; kết luận là về kỳ vọng, không về từng lần lấy max.

---

## Bài tập (30 phút)

### X01 — Sai lệch Rademacher và hai đích

::: exercise
1. Liệt kê bốn cặp giá trị $(\varepsilon_1,\varepsilon_2)$ Rademacher độc lập và kiểm lại $\mathbb E[\max_a\widehat Q_a]=1/2$ khi giá trị thật bằng $0$.
2. Với $r=1$, $\gamma=0{,}8$, $Z=0$, $Q_{\theta^-}(s',\cdot)=(2,7)$ và $Q_\theta(s',\cdot)=(4,1)$, tính đích DQN và đích Double DQN.
:::

::: hint
Phần 1: đếm trong bốn cặp đồng xác suất có bao nhiêu cặp cho cực đại bằng $-1$. Phần 2: DQN để $Q_{\theta^-}$ vừa chọn vừa đánh giá; Double DQN lấy argmax theo $Q_\theta$ rồi đánh giá bằng $Q_{\theta^-}$.
:::

::: solution
1. Bốn cặp: $(-1,-1)\to\max=-1$; $(-1,1),(1,-1),(1,1)\to\max=1$. Kỳ vọng $\tfrac14(-1)+\tfrac34(1)=\tfrac12$, trong khi $\max_a\mathbb E[\widehat Q_a]=0$.
2. DQN: mạng mục tiêu chọn hành động 2 (giá trị $7$), $y^{\mathrm{DQN}}=1+0{,}8\cdot 7=6{,}6$. Double DQN: mạng online chọn hành động 1 (giá trị $4$), mạng mục tiêu đánh giá $2$, $y^{\mathrm{DDQN}}=1+0{,}8\cdot 2=2{,}6$.
:::

### X02 — Hai hàm điểm

::: exercise
1. Với ví dụ softmax $\pi_\theta(1\mid s)=2/3$, $\pi_\theta(2\mid s)=1/3$, $\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$: tính $\psi_\theta(s,2)$ và kiểm $\mathbb E_{A\sim\pi}[\psi_\theta(s,A)]=0$.
2. Với Gaussian: đổi thành $a=-1$, giữ $\phi(s)=(1,2)$, $\mu=0$, $\sigma^2=1$. Tính $\psi_\theta(s,a)$.
:::

::: hint
Phần 1: hàm điểm là đặc trưng hành động trừ trung bình đặc trưng theo chính sách; kỳ vọng có trọng số bằng xác suất $\pi_\theta(b\mid s)$. Phần 2: dùng $\psi=(a-\mu)/\sigma^2\cdot\phi(s)$.
:::

::: solution
1. $\psi_\theta(s,2)=(0,1)-(\tfrac23,\tfrac13)=(-\tfrac23,\tfrac23)$. Kỳ vọng: $\tfrac23(\tfrac13,-\tfrac13)+\tfrac13(-\tfrac23,\tfrac23)=(0,0)$.
2. $\psi_\theta(s,-1)=\dfrac{-1-0}{1}(1,2)=(-1,-2)$.
:::

### X03 — Kiểm cập nhật REINFORCE

::: exercise
1. Giữ dữ kiện ví dụ softmax ($\phi(s,1)=(1,0)$, $\phi(s,2)=(0,1)$, $\theta=(\log 2,0)$, $\pi_\theta(1\mid s)=2/3$, episode một bước chọn hành động 1, $\alpha=0{,}1$) nhưng đặt $G_0=-3$. Tính $\theta_{\mathrm{new}}$ và $\pi_{\theta_{\mathrm{new}}}(1\mid s)$.
2. Episode hai bước với $R_1=1$, $R_2=2$, $\gamma=0{,}9$: tính $G_0$ và $G_1$.
3. Nêu tham số phải giữ cố định trong khi thu một episode nhiều bước.
:::

::: hint
Phần 1: $\widehat g=G_0\,\psi_\theta(s,1)$; return âm đảo hướng cập nhật. Phần 2: $G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}$ với $T=2$. Phần 3: hợp đồng lấy mẫu của REINFORCE episodic.
:::

::: solution
1. $\widehat g=-3(\tfrac13,-\tfrac13)=(-1,1)$, nên $\theta_{\mathrm{new}}=(\log 2-0{,}1,\;0{,}1)$ và
$$\pi_{\theta_{\mathrm{new}}}(1\mid s)=\frac{2e^{-0{,}1}}{2e^{-0{,}1}+e^{0{,}1}}\approx0{,}621<\tfrac23.$$
Xác suất hành động 1 giảm vì return âm.
2. $G_1=R_2=2$; $G_0=R_1+\gamma R_2=1+0{,}9\cdot 2=2{,}8$.
3. $\theta_{\mathrm{old}}$ phải giữ cố định trong khi thu trọn episode; chỉ cập nhật một lần sau khi cộng xong $\widehat g$.
:::

---

## Tài liệu tham khảo

1. Tạ Việt Cường. *Bài giảng 10: Policy Gradient* (bản trích dùng cho Bài 09: lecture09-ddqn-and-policy-gradient-part1.pdf, tr. 1–40). Phòng thí nghiệm HMI, Trường Đại học Công nghệ, Học kỳ 1, 2026–2027.
2. Mnih, V. và cộng sự. "Human-level control through deep reinforcement learning." *Nature* 518 (2015): 529–533. (Experience replay, target network, thuật toán DQN — tr. 5–10.)
3. van Hasselt, H. "Double Q-learning." *NeurIPS* 2010. (Double Q-learning dạng bảng — tr. 20–21.)
4. van Hasselt, H., Guez, A., Silver, D. "Deep Reinforcement Learning with Double Q-learning." *AAAI* 2016. (Double DQN — tr. 14–19.)
5. Williams, R. J. "Simple statistical gradient-following algorithms for connectionist reinforcement learning." *Machine Learning* 8 (1992): 229–256. (REINFORCE — tr. 40.)
6. Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, 2nd ed., MIT Press, 2018. (Định lý gradient chính sách, phân bố chiếm dụng — tr. 39.)
