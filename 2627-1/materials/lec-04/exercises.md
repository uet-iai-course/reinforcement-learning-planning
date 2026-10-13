# Bài tập Bài 04 — Giải MDP bằng quy hoạch động

Bộ bài tập gồm mười bốn bài, phủ bảy mạch của bộ trang chiếu Bài 04, ở ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào bài toán Học tăng cường. Bài tập 04.1–04.6 giữ số hiệu, đề bài và kết quả lời giải của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-04/lecture-note.md&deck=lecture-04-giai-mdp-bang-quy-hoach-dong.html), và cả sáu bài trùng bài tập có lời giải trên trang chiếu. Bài tập 04.7–04.9 nằm ở mục "Bài tập củng cố" của ghi chú và không chép lại ở đây; bảng dưới ghi chúng sau chữ "ghi chú" ở mạch mà bộ trang chiếu xếp chúng vào. Bài tập 04.10–04.17 chỉ có trong tệp này; riêng Bài tập 04.16 trùng bài tập lợi tức ở mạch mở đầu của bộ trang chiếu. Khi một bài trùng trang chiếu, dòng "Trùng trang chiếu" dẫn tới trang đề bài và trang lời giải, và lời giải trong tệp cho cùng kết quả với lời giải trên trang. Trong mỗi mức, bài xếp theo thứ tự mạch, không theo độ khó; các bài 04.10, 04.11 và 04.12 dài hơn các bài cùng mức.

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/1/1) | 04.16 |
| 2. Đánh giá chính sách | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/2/1) | 04.1, 04.10 |
| 3. Cải thiện chính sách | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/3/1) | 04.2, 04.17 |
| 4. Lặp chính sách | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/4/1) | 04.3, 04.12 |
| 5. Lặp giá trị | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/5/1) | 04.4, 04.11, 04.13; ghi chú: 04.7, 04.8 |
| 6. Lịch cập nhật và giới hạn của mô hình bảng | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/6/1) | 04.5, 04.14, 04.15; ghi chú: 04.9 |
| 7. Tổng kết và chuyển tiếp | [Mở phần](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/7/1) | 04.6 |

## Hướng dẫn và ký hiệu

Ký hiệu, giả thiết và số hiệu theo ghi chú bài giảng Bài 04. Một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn có tập trạng thái chưa kết thúc $\mathcal S$ với $n=\lvert\mathcal S\rvert$, có thể thêm một trạng thái kết thúc $s_{\mathrm{term}}$, tập hành động hữu hạn $\mathcal A(s)$ tại mỗi $s$, và mô hình $p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$. Phần thưởng $R_{t+1}$ thuộc về chuyển từ thời điểm $t$ sang $t+1$; lợi tức (return) là $G_t=\sum_{j\ge0}\gamma^jR_{t+j+1}$ với hệ số chiết khấu $0\le\gamma<1$, trừ khi đề bài nói khác. Mọi bảng giá trị bằng $0$ tại $s_{\mathrm{term}}$; phần thưởng của chính chuyển đi vào $s_{\mathrm{term}}$ vẫn được tính. Kỳ vọng $\mathbb E_\pi$ lấy theo cả chính sách $\pi$ lẫn mô hình $p$. Bất đẳng thức giữa hai bảng hiểu theo từng trạng thái.

Các đại lượng dùng lại: giá trị nhìn trước một bước $Q_V(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr]$ (Định nghĩa 04.11); toán tử Bellman đánh giá $(T_\pi V)(s)=\sum_a\pi(a\mid s)Q_V(s,a)$ (Định nghĩa 04.1); toán tử Bellman tối ưu $(T_*V)(s)=\max_aQ_V(s,a)$ (Định nghĩa 04.22); phần dư Bellman $\Delta_\pi(V)=\lVert T_\pi V-V\rVert_\infty$ và $\Delta_*(V)=\lVert T_*V-V\rVert_\infty$, với chuẩn vô cùng $\lVert U\rVert_\infty=\max_s\lvert U(s)\rvert$; ngưỡng dừng $\theta=(1-\gamma)\kappa$ cho sai số cho phép $\kappa$. Quy tắc phá hòa (tie-breaking) của Định nghĩa 04.12 giữ hành động cũ khi nó thuộc tập cực đại, nếu không thì chọn hành động đứng đầu theo thứ tự cố định ($\mathrm a$ trước $\mathrm b$, $\mathrm{trai}$ trước $\mathrm{phai}$).

**Các kết quả dùng lại.** Đề bài dẫn các kết quả sau của ghi chú bằng tên; phát biểu được nhắc lại ở đây.

- Điều kiện (2.2) và Định lý 04.13 (cải thiện chính sách): cho $\pi$ là chính sách Markov dừng, có thể ngẫu nhiên, với giá trị chính xác $v_\pi$, và $\pi'$ xác định thỏa (2.2): $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$. Khi đó (a) $v_{\pi'}\ge v_\pi$ tại mọi trạng thái, và (b) $v_{\pi'}(s)>v_\pi(s)$ tại mọi trạng thái $s$ mà (2.2) nghiêm ngặt.
- Hệ quả 04.8(a) (chặn sai số theo phần dư): $\lVert V-v_\pi\rVert_\infty\le\Delta_\pi(V)/(1-\gamma)$ với mọi bảng $V$.
- Hệ quả 04.27 (chặn sai số theo phần dư tối ưu): $\lVert V-v_*\rVert_\infty\le\Delta_*(V)/(1-\gamma)$ với mọi bảng $V$; nói riêng, $\Delta_*(V)\le\theta=(1-\gamma)\kappa$ kéo theo $\lVert V-v_*\rVert_\infty\le\kappa$.
- Định nghĩa 04.16 (chính sách ổn định): chính sách xác định $\pi$ ổn định khi $\pi(s)\in\arg\max_aq_\pi(s,a)$ với mọi $s$, trong đó $q_\pi$ tính từ giá trị chính xác $v_\pi$.
- Định lý 04.32 (hội tụ của lặp giá trị bất đồng bộ): nếu mỗi trạng thái chưa kết thúc xuất hiện vô hạn lần trong lịch cập nhật thì $\lVert V_j-v_*\rVert_\infty$ không tăng và tiến về $0$; chứng minh chia các bước thành những đoạn liên tiếp, mỗi đoạn cập nhật mọi trạng thái ít nhất một lần, và sai số giảm ít nhất $\gamma$ lần sau mỗi đoạn.

Dòng "Mục tiêu học tập" của mỗi bài dẫn số thứ tự trong danh sách năm mục tiêu ở đầu ghi chú bài giảng.

Tên trạng thái và hành động của ví dụ viết chữ đứng ($\mathrm s_0$, $\mathrm a$, $\mathrm c_1$, $\mathrm{phai}$) để phân biệt với biến viết nghiêng ($s$, $a$). Số thập phân viết với dấu phẩy; khi một bảng có thành phần thập phân, các thành phần cách nhau bằng dấu chấm phẩy, như $(1{,}9;\,2{,}9)$.

**Mô hình hai trạng thái** (Bài giảng gốc (2025–2026), trang 17–18), dùng ở nhiều bài và được nêu lại trong từng bài: $\mathcal S=\{\mathrm s_0,\mathrm s_1\}$, không có trạng thái kết thúc, mọi chuyển xác định, $\gamma=0{,}9$.

| Trạng thái $s$ | Hành động | Trạng thái kế tiếp $s'$ | Phần thưởng $r$ |
|---|---|---|---:|
| $\mathrm s_0$ | $\mathrm a$ | $\mathrm s_0$ | $1$ |
| $\mathrm s_0$ | $\mathrm b$ | $\mathrm s_1$ | $0$ |
| $\mathrm s_1$ | $\mathrm a$ | $\mathrm s_0$ | $2$ |
| $\mathrm s_1$ | $\mathrm b$ | $\mathrm s_1$ | $3$ |

Chính sách xác định được viết thành cặp theo thứ tự $(\mathrm s_0,\mathrm s_1)$: $\pi_0=(\mathrm a,\mathrm a)$, $\pi_1=(\mathrm a,\mathrm b)$. Các giá trị đã có trong ghi chú: $v_{\pi_0}=(10,11)$, $v_{\pi_1}=(10,30)$, $v_*=v_{(\mathrm b,\mathrm b)}=(27,30)$.

**Dãy năm ô** (Bài giảng gốc (2025–2026), trang 25–28): các ô $\mathrm c_1,\dots,\mathrm c_5$, trong đó $\mathrm c_5$ là trạng thái kết thúc; hành động $\mathrm{trai}$, $\mathrm{phai}$ chuyển xác định sang ô bên cạnh, $\mathrm{trai}$ tại $\mathrm c_1$ giữ nguyên $\mathrm c_1$; phần thưởng $10$ cho chuyển $\mathrm c_4\to\mathrm c_5$ và $-1$ cho mọi chuyển khác; $\gamma=0{,}9$. Bài tập 04.13 dùng phiên bản trơn trượt của dãy này, nêu trong đề bài.

**CartPole rời rạc hóa** (bài thực hành `thuc-hanh-cartpole-quy-hoach-dong.ipynb`): $324$ ô chưa kết thúc cùng một trạng thái kết thúc, hai hành động, mô hình ước lượng $\hat p(s'\mid s,a)$, phần thưởng $\hat r(s,a)=1$ với mọi cặp. Notebook viết $\eta$ cho ngưỡng dừng, $\varepsilon$ cho sai số cho phép, biến `theta` cho góc cột (ghi chú viết $\phi$) và $m$ cho số lần áp dụng $T_\pi$ ở nhiệm vụ 7; tệp này viết $\theta$, $\kappa$ và $\ell$, vì trong ghi chú $m$ là số hành động tối đa. Số liệu notebook trong tệp lấy từ một lần chạy đã nhúng trong notebook (gymnasium 1.3.0).

Bộ số của chính sách ngẫu nhiên đều $\pi_u$ trên mô hình hai trạng thái là số liệu sư phạm tự xây dựng. Bài có nhãn [Lập trình] cần chạy mã, trên notebook hoặc bằng một chương trình ngắn; các phần còn lại làm được bằng tay. Lời giải cần nêu kết quả của ghi chú được dùng ở từng bước.

## Mức nhận biết

### Bài tập 04.16. Lợi tức của chính sách ban đầu

**Mức độ:** nhận biết. Mục tiêu học tập 1 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 5, 17–18; ghi chú bài giảng, Ví dụ 04.1.

**Trùng trang chiếu:** [Bài tập: lợi tức của chính sách ban đầu](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/1/9), câu (a) và (b); lời giải hiện trên cùng trang. Câu (c) chỉ có trong tệp này.

::: exercise Bài tập 04.16 (Lợi tức của chính sách ban đầu)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Tác tử xuất phát tại $S_0=\mathrm s_1$ và theo $\pi_0=(\mathrm a,\mathrm a)$.

- (a) Tính tổng chiết khấu của ba phần thưởng đầu $R_1+\gamma R_2+\gamma^2R_3$.
- (b) Ngoài phần thưởng, nêu thông tin của mô hình (bảng mô hình hai trạng thái ở mục Hướng dẫn và ký hiệu) cần dùng để làm câu (a).
- (c) Tính lợi tức $G_0$ bằng tổng của cấp số nhân, và so với $v_{\pi_0}(\mathrm s_1)=11$.
:::

::: hint Gợi ý Bài tập 04.16
Lần theo quỹ đạo $\mathrm s_1\to\mathrm s_0\to\mathrm s_0\to\cdots$. Phần thưởng đầu mang chỉ số $1$ vì nó được nhận sau hành động $A_0$.
:::

::: solution Lời giải Bài tập 04.16
**Câu (a).** Tại $\mathrm s_1$, $\pi_0$ chọn $\mathrm a$, nên $R_1=2$ và $S_1=\mathrm s_0$. Tại $\mathrm s_0$, $\pi_0$ chọn $\mathrm a$, nên $R_2=1$, $S_2=\mathrm s_0$ và $R_3=1$. Tổng là

$$
R_1+\gamma R_2+\gamma^2R_3=2+0{,}9\cdot1+0{,}81\cdot1=3{,}71 .
$$

Số $3{,}71$ chưa phải $G_0$, vì còn các số hạng $\gamma^jR_{j+1}$ với $j\ge3$.

**Câu (b).** Cần trạng thái kế tiếp $s'$ của mỗi chuyển, tức cột $s'$ của bảng mô hình, hay mô hình $p$: chỉ biết phần thưởng của từng hành động thì không xác định được $S_1=\mathrm s_0$, do đó không xác định được $R_2=1$.

**Câu (c).** Từ thời điểm $1$, mọi phần thưởng bằng $1$, nên

$$
G_0=2+\sum_{j\ge1}0{,}9^j\cdot1=2+\frac{0{,}9}{1-0{,}9}=2+9=11 .
$$

Mô hình và chính sách đều xác định, nên $G_0$ không ngẫu nhiên và bằng $v_{\pi_0}(\mathrm s_1)=11$.

**Kiểm tra lại.** Tính từ cuối về đầu cho cùng tổng cắt ngắn: $1+0{,}9\cdot1=1{,}9$, rồi $2+0{,}9\cdot1{,}9=3{,}71$. Ba lỗi thường gặp: đánh chỉ số phần thưởng đầu là $R_0$ rồi nhân nó với $\gamma$, cho $0{,}9\cdot2+0{,}81+0{,}729=3{,}339$; cho tác tử ở lại $\mathrm s_1$ và cộng phần thưởng $3$ của hành động $\mathrm b$, hành động mà $\pi_0$ không chọn; coi $3{,}71$ là lợi tức.
:::

### Bài tập 04.3. Kết luận dừng từ một bảng gần đúng

**Mức độ:** nhận biết. Mục tiêu học tập 3 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 17–20, 34; ghi chú bài giảng, Bài tập 04.3; Sutton và Barto (2018), §4.3.

**Trùng trang chiếu:** [Bài tập: kết luận dừng từ bảng gần đúng](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/4/9) và [trang lời giải](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/4/10).

::: exercise Bài tập 04.3 (Kết luận dừng từ một bảng gần đúng)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Một chương trình giữ chính sách $\pi=(\mathrm a,\mathrm b)$ và bảng gần đúng $V=(0,0)$ thay cho giá trị của $\pi$. Giá trị chính xác của hai chính sách là $v_{(\mathrm a,\mathrm b)}=(10,30)$ và $v_{(\mathrm b,\mathrm b)}=(27,30)$.

- (a) Tính bốn giá trị nhìn trước $Q_V(s,a)$.
- (b) Xác định chính sách tham lam theo $V$ với quy tắc phá hòa.
- (c) Chương trình kết luận "chính sách không đổi nên đã tối ưu". Đánh giá kết luận này bằng Định nghĩa 04.16 và Ví dụ 04.11 của ghi chú.
:::

::: hint Gợi ý Bài tập 04.3
Với $V=(0,0)$, giá trị nhìn trước chỉ còn phần thưởng của bước đầu. Để đánh giá kết luận, tính giá trị nhìn trước từ $v_{(\mathrm a,\mathrm b)}=(10,30)$ và so $(10,30)$ với $(27,30)$.
:::

::: solution Lời giải Bài tập 04.3
**Câu (a).** Mọi giá trị tiếp nối bằng $0$, nên $Q_V(\mathrm s_0,\mathrm a)=1$, $Q_V(\mathrm s_0,\mathrm b)=0$, $Q_V(\mathrm s_1,\mathrm a)=2$, $Q_V(\mathrm s_1,\mathrm b)=3$.

**Câu (b).** Tại $\mathrm s_0$, $\arg\max=\{\mathrm a\}$ chứa hành động cũ; tại $\mathrm s_1$, $\arg\max=\{\mathrm b\}$ chứa hành động cũ. Chính sách tham lam theo $V$ là $(\mathrm a,\mathrm b)$, trùng $\pi$.

**Câu (c).** Kết luận sai. Định nghĩa 04.16 đòi kiểm tính ổn định bằng giá trị chính xác $v_\pi$. Ở đây $v_{(\mathrm a,\mathrm b)}=(10,30)$ (Ví dụ 04.10), và từ bảng này $q(\mathrm s_0,\mathrm b)=0+0{,}9\cdot30=27>10=q(\mathrm s_0,\mathrm a)$, nên $\pi$ không ổn định. Theo Ví dụ 04.11, $(\mathrm b,\mathrm b)$ có giá trị $(27,30)$, lớn hơn $(10,30)$ tại $\mathrm s_0$.

**Kiểm tra lại.** Phép chọn hành động ở câu (b) đúng đối với bảng $V$; lỗi nằm ở bảng, vì $V=(0,0)$ không phải giá trị của chính sách đang giữ. Hai lỗi thường gặp: dùng Định lý 04.13 cho một bảng gần đúng, trong khi định lý đòi giá trị chính xác; coi "chính sách không đổi sau một lần cải thiện" là chứng nhận tối ưu mà không kiểm phương trình Bellman tối ưu tại $v_\pi$.
:::

## Mức tính toán hoặc chứng minh

### Bài tập 04.1. Lượt quét thứ ba và chặn sai số

**Mức độ:** tính toán. Mục tiêu học tập 1 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 14, 17–18; ghi chú bài giảng, Bài tập 04.1.

**Trùng trang chiếu:** [Bài tập: lượt quét thứ ba và chặn sai số](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/2/12) và [trang lời giải](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/2/13).

::: exercise Bài tập 04.1 (Lượt quét thứ ba và chặn sai số)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_0=(\mathrm a,\mathrm a)$ và bảng $V_2=(1{,}9;\,2{,}9)$ thu được sau hai lượt quét đồng bộ từ $V_0=(0,0)$.

- (a) Tính bảng đồng bộ $V_3=T_{\pi_0}V_2$.
- (b) Tính $\Delta_{\pi_0}(V_2)$ và chặn sai số của $V_2$ theo Hệ quả 04.8(a).
- (c) Biết $v_{\pi_0}=(10,11)$, so chặn ở (b) với sai số thật của $V_2$, và giải thích vì sao $V_3$ chưa phải $v_{\pi_0}$.
:::

::: hint Gợi ý Bài tập 04.1
Theo $\pi_0$, cả hai trạng thái chọn $\mathrm a$ và $\mathrm a$ dẫn về $\mathrm s_0$; cả hai ô của $V_3$ đọc $V_2(\mathrm s_0)$. Phần dư của $V_2$ là $\lVert V_3-V_2\rVert_\infty$.
:::

::: solution Lời giải Bài tập 04.1
**Câu (a).** Cả hai ô đọc $V_2(\mathrm s_0)=1{,}9$ từ bảng cũ:

$$
\begin{aligned}
V_3(\mathrm s_0)&=1+0{,}9\cdot1{,}9=2{,}71,\\
V_3(\mathrm s_1)&=2+0{,}9\cdot1{,}9=3{,}71.
\end{aligned}
$$

Vậy $V_3=(2{,}71;\,3{,}71)$.

**Câu (b).** $V_3-V_2=(0{,}81;\,0{,}81)$, nên $\Delta_{\pi_0}(V_2)=0{,}81$. Chặn sai số là $0{,}81/(1-0{,}9)=8{,}1$.

**Câu (c).** Sai số thật là $\max\{10-1{,}9;\ 11-2{,}9\}=8{,}1$, đúng bằng chặn. Bảng $V_3$ còn phần dư $\Delta_{\pi_0}(V_3)=0{,}9^3=0{,}729>0$, nên $V_3$ chưa thỏa $V=T_{\pi_0}V$; theo Hệ quả 04.6(a), chỉ $v_{\pi_0}$ thỏa phương trình đó.

**Kiểm tra lại.** Theo Ví dụ 04.5 của ghi chú, $\lVert V_k-v_{\pi_0}\rVert_\infty=10\cdot0{,}9^k$ với $k\ge1$; với $k=2$ được $8{,}1$. Hai lỗi thường gặp: cho ô $\mathrm s_1$ đọc giá trị mới $V_3(\mathrm s_0)=2{,}71$, cho $2+0{,}9\cdot2{,}71=4{,}439$, tức kết quả của cập nhật tại chỗ; đọc phần dư $0{,}81$ là sai số, bỏ quên thừa số $1/(1-\gamma)=10$.
:::

### Bài tập 04.10. Dạng ma trận và chuỗi Neumann của bài toán đánh giá chính sách

**Mức độ:** tính toán và chứng minh. Mục tiêu học tập 1 của ghi chú.

**Nguồn:** Bài tập tuần 3 (2025–2026), bài 6; ghi chú bài giảng, Hệ quả 04.6(c) và đoạn sau Ví dụ 04.5; ghi chú Bài 03, Định lý 03.28. Bộ số của câu (b) là số liệu sư phạm tự xây dựng.

::: exercise Bài tập 04.10 (Dạng ma trận và chuỗi Neumann của bài toán đánh giá chính sách)
Xét MDP hữu hạn với $n$ trạng thái chưa kết thúc, phần thưởng bị chặn, chính sách Markov dừng $\pi$ và $0\le\gamma<1$. Đặt $P_\pi(s,s')=\sum_a\pi(a\mid s)\sum_rp(s',r\mid s,a)$ với $s,s'\in\mathcal S$ (chỉ gồm trạng thái chưa kết thúc) và $r_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\,r$.

**Nhắc lại:** $T_\pi V=r_\pi+\gamma P_\pi V$ với mọi $V\in\mathbb R^n$, nên $(I-\gamma P_\pi)v_\pi=r_\pi$; ma trận $I-\gamma P_\pi$ khả nghịch khi $0\le\gamma<1$ và $v_\pi=(I-\gamma P_\pi)^{-1}r_\pi$ (Hệ quả 04.6(c) của ghi chú; ghi chú Bài 03, Định lý 03.28).

Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$.

- (a) Trên mô hình hai trạng thái, viết $P_{\pi_0}$, $r_{\pi_0}$ cho $\pi_0=(\mathrm a,\mathrm a)$ và giải hệ để được $v_{\pi_0}$.
- (b) Làm như câu (a) cho chính sách ngẫu nhiên đều $\pi_u(\mathrm a\mid s)=\pi_u(\mathrm b\mid s)=\tfrac12$ tại cả hai trạng thái.
- (c) Chứng minh $(I-\gamma P_\pi)^{-1}=\sum_{k\ge0}\gamma^kP_\pi^k$ (chuỗi Neumann), mọi phần tử của ma trận này không âm và tổng mỗi hàng không vượt $1/(1-\gamma)$. Nêu ý nghĩa của thành phần $s$ của $\gamma^kP_\pi^kr_\pi$. Kiểm công thức trên $\pi_0$ và $\pi_u$ của câu (a), (b), biết $P_{\pi_0}^2=P_{\pi_0}$ và $P_{\pi_u}^2=P_{\pi_u}$.
- (d) Với $\gamma=1$ và $\pi_0$, chỉ ra $I-P_{\pi_0}$ suy biến, và nối kết quả với dãy lượt quét đồng bộ từ $V_0=(0,0)$, cho $V_k=(k,\,k+1)$ với $k\ge1$.
:::

::: hint Gợi ý Bài tập 04.10
Ở (c), nhân $(I-\gamma P_\pi)$ với tổng riêng $S_N=\sum_{k=0}^{N}\gamma^kP_\pi^k$; các tổng ở giữa triệt tiêu từng cặp. Mỗi hàng của $P_\pi^k$ gồm số không âm có tổng không vượt $1$, vì $P_\pi$ có tính chất đó.
:::

::: solution Lời giải Bài tập 04.10
**Câu (a).** Theo $\pi_0$, cả hai trạng thái chọn $\mathrm a$ và đi về $\mathrm s_0$, nên

$$
P_{\pi_0}=\begin{bmatrix}1&0\\1&0\end{bmatrix},\qquad r_{\pi_0}=\begin{bmatrix}1\\2\end{bmatrix},\qquad I-0{,}9P_{\pi_0}=\begin{bmatrix}0{,}1&0\\-0{,}9&1\end{bmatrix}.
$$

Hàng thứ nhất cho $0{,}1\,x=1$, nên $x=10$; hàng thứ hai cho $-0{,}9\cdot10+y=2$, nên $y=11$. Vậy $v_{\pi_0}=(10,11)$.

**Câu (b).** Theo $\pi_u$, mỗi trạng thái đi về $\mathrm s_0$ hoặc $\mathrm s_1$ với xác suất $\tfrac12$; thưởng kỳ vọng một bước là $\tfrac{1+0}2=0{,}5$ tại $\mathrm s_0$ và $\tfrac{2+3}2=2{,}5$ tại $\mathrm s_1$:

$$
P_{\pi_u}=\begin{bmatrix}0{,}5&0{,}5\\0{,}5&0{,}5\end{bmatrix},\qquad r_{\pi_u}=\begin{bmatrix}0{,}5\\2{,}5\end{bmatrix},\qquad I-0{,}9P_{\pi_u}=\begin{bmatrix}0{,}55&-0{,}45\\-0{,}45&0{,}55\end{bmatrix}.
$$

Định thức là $0{,}55^2-0{,}45^2=0{,}1$, nên

$$
(I-0{,}9P_{\pi_u})^{-1}=\begin{bmatrix}5{,}5&4{,}5\\4{,}5&5{,}5\end{bmatrix},\qquad v_{\pi_u}=\begin{bmatrix}5{,}5\cdot0{,}5+4{,}5\cdot2{,}5\\4{,}5\cdot0{,}5+5{,}5\cdot2{,}5\end{bmatrix}=\begin{bmatrix}14\\16\end{bmatrix}.
$$

**Câu (c).** *Bước 1 (tổng riêng).* Với $S_N=\sum_{k=0}^{N}\gamma^kP_\pi^k$, khai triển tích và triệt tiêu từng cặp:

$$
(I-\gamma P_\pi)S_N=\sum_{k=0}^{N}\gamma^kP_\pi^k-\sum_{k=1}^{N+1}\gamma^kP_\pi^k=I-\gamma^{N+1}P_\pi^{N+1}.
$$

*Bước 2 (giới hạn).* $P_\pi$ có phần tử không âm và tổng mỗi hàng không vượt $1$, vì phần xác suất đi vào $s_{\mathrm{term}}$ bị bỏ khỏi tổng. Tích của hai ma trận có tính chất này cũng có tính chất này, nên mọi phần tử của $P_\pi^{k}$ nằm trong $[0,1]$. Do đó $\gamma^{N+1}P_\pi^{N+1}\to0$ khi $N\to\infty$. Mỗi phần tử của $S_N$ là tổng các số không âm, không giảm theo $N$ và bị chặn bởi $\sum_{k\ge0}\gamma^k=1/(1-\gamma)$, nên $S_N$ hội tụ về một ma trận $S$.

*Bước 3 (kết luận).* Cho $N\to\infty$ ở Bước 1 được $(I-\gamma P_\pi)S=I$, tức $S=(I-\gamma P_\pi)^{-1}$; lập luận này cũng chứng minh lại tính khả nghịch. Mọi phần tử của $S$ không âm, và tổng hàng $s$ của $S$ là $\sum_k\gamma^k\sum_{s'}P_\pi^k(s,s')\le\sum_k\gamma^k=1/(1-\gamma)$.

*Ý nghĩa.* $P_\pi^k(s,s')$ là xác suất ở $s'$ sau $k$ bước khi xuất phát từ $s$ và theo $\pi$, nên $(P_\pi^kr_\pi)(s)=\mathbb E_\pi[R_{k+1}\mid S_0=s]$. Công thức $v_\pi=\sum_k\gamma^kP_\pi^kr_\pi$ chính là $v_\pi(s)=\sum_k\gamma^k\mathbb E_\pi[R_{k+1}\mid S_0=s]$, kỳ vọng của lợi tức viết theo từng bước.

*Kiểm số.* Vì $P^k=P$ với $k\ge1$ khi $P^2=P$, chuỗi rút về $I+\bigl(\sum_{k\ge1}0{,}9^k\bigr)P=I+9P$:

$$
I+9P_{\pi_0}=\begin{bmatrix}10&0\\9&1\end{bmatrix},\qquad I+9P_{\pi_u}=\begin{bmatrix}5{,}5&4{,}5\\4{,}5&5{,}5\end{bmatrix}.
$$

Ma trận thứ hai trùng nghịch đảo ở câu (b). Ma trận thứ nhất nhân $r_{\pi_0}=(1,2)$ cho $(10,\ 9+2)=(10,11)$, trùng câu (a). Mọi hàng có tổng $10=1/(1-0{,}9)$, vì mô hình không có trạng thái kết thúc.

**Câu (d).** Với $\gamma=1$, $I-P_{\pi_0}=\begin{bmatrix}0&0\\-1&1\end{bmatrix}$ có định thức $0$. Hàng thứ nhất của hệ thành $0\cdot x=1$, vô nghiệm, nên không có bảng hữu hạn nào thỏa phương trình Bellman kỳ vọng. Điều này khớp với dãy lượt quét $V_k=(k,\,k+1)$, $k\ge1$, tăng không giới hạn. Hệ thuần nhất có nghiệm khác $0$ là $x=(1,1)$, ứng với đẳng thức $T_{\pi_0}(V+c\mathbf 1)=T_{\pi_0}V+c\mathbf 1$: cộng cùng một hằng số vào mọi ô không làm khoảng cách giảm. Ở câu (c), chuỗi $\sum_k P_{\pi_0}^k=I+P_{\pi_0}+P_{\pi_0}+\cdots$ phân kỳ.

**Kiểm tra lại.** Thế $(14,16)$ vào phương trình Bellman của $\pi_u$: $0{,}5+0{,}45\cdot14+0{,}45\cdot16=0{,}5+6{,}3+7{,}2=14$ và $2{,}5+6{,}3+7{,}2=16$. Ba lỗi thường gặp: thêm cột $s_{\mathrm{term}}$ vào $P_\pi$, làm ma trận không vuông; quên trọng số $\pi(a\mid s)$ khi tính $r_\pi$, chẳng hạn lấy $r_{\pi_u}(\mathrm s_0)=1+0=1$; viết chuỗi Neumann bắt đầu từ $k=1$, bỏ số hạng $I$, cho $9P_{\pi_0}r_{\pi_0}=(9,9)$ thay cho $(10,11)$.
:::

### Bài tập 04.2. Cải thiện từ chính sách π₁

**Mức độ:** tính toán. Mục tiêu học tập 2 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 17–20; ghi chú bài giảng, Bài tập 04.2.

**Trùng trang chiếu:** [Bài tập: lần cải thiện thứ hai](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/3/9) và [trang lời giải](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/3/10).

::: exercise Bài tập 04.2 (Cải thiện từ chính sách π₁)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_1=(\mathrm a,\mathrm b)$ có giá trị chính xác $v_{\pi_1}=(10,30)$. Lần cải thiện từ $\pi_0=(\mathrm a,\mathrm a)$ với $v_{\pi_0}=(10,11)$ đã cho $q_{\pi_0}(\mathrm s_0,\mathrm a)=10$, $q_{\pi_0}(\mathrm s_0,\mathrm b)=9{,}9$, nên giữ $\mathrm a$ tại $\mathrm s_0$.

- (a) Tính $q_{\pi_1}(\mathrm s_0,\mathrm a)$ và $q_{\pi_1}(\mathrm s_0,\mathrm b)$.
- (b) Xác định hành động của chính sách tham lam tại $\mathrm s_0$ theo Định nghĩa 04.12.
- (c) Giải thích vì sao lựa chọn tại $\mathrm s_0$ khác lựa chọn ở lần cải thiện từ $\pi_0$.
:::

::: hint Gợi ý Bài tập 04.2
Giá trị nhìn trước của $\mathrm b$ tại $\mathrm s_0$ đọc giá trị tiếp nối của $\mathrm s_1$ trong bảng $v_{\pi_1}$, không phải trong bảng $v_{\pi_0}$.
:::

::: solution Lời giải Bài tập 04.2
**Câu (a).** $q_{\pi_1}(\mathrm s_0,\mathrm a)=1+0{,}9\cdot10=10$ và $q_{\pi_1}(\mathrm s_0,\mathrm b)=0+0{,}9\cdot30=27$.

**Câu (b).** Hành động cũ $\pi_1(\mathrm s_0)=\mathrm a$ không thuộc $\arg\max=\{\mathrm b\}$, nên chính sách tham lam chọn $\mathrm b$ tại $\mathrm s_0$.

**Câu (c).** Phần thưởng tức thời tại $\mathrm s_0$ không đổi: $\mathrm a$ vẫn cho $1$, $\mathrm b$ vẫn cho $0$. Giá trị tiếp nối của $\mathrm s_1$ tăng từ $11$ dưới $\pi_0$ lên $30$ dưới $\pi_1$, nên nhánh $\mathrm b$ tăng từ $9{,}9$ lên $27$ và vượt nhánh $\mathrm a$.

**Kiểm tra lại.** Tại $\mathrm s_1$, $q_{\pi_1}(\mathrm s_1,\mathrm a)=2+0{,}9\cdot10=11<30=q_{\pi_1}(\mathrm s_1,\mathrm b)$, nên chính sách tham lam giữ $\mathrm b$ tại $\mathrm s_1$; chính sách mới là $(\mathrm b,\mathrm b)$. Hai lỗi thường gặp: đọc giá trị tiếp nối từ bảng cũ $(10,11)$, cho $9{,}9<10$ và giữ nguyên $\mathrm a$; coi $27$ là giá trị của chính sách mới tại $\mathrm s_0$, trong khi $27$ đo việc chọn $\mathrm b$ một lần rồi theo $\pi_1$ (ở mô hình này hai số trùng nhau vì $(\mathrm b,\mathrm b)$ có $v(\mathrm s_0)=27$, nhưng cần một lần đánh giá để biết điều đó).
:::

### Bài tập 04.17. Cải thiện từ chính sách ngẫu nhiên đều

**Mức độ:** tính toán. Mục tiêu học tập 2 của ghi chú.

**Nguồn:** ghi chú bài giảng, Định lý 04.13 và Ví dụ 04.3; số liệu sư phạm tự xây dựng.

::: exercise Bài tập 04.17 (Cải thiện từ chính sách ngẫu nhiên đều)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách ngẫu nhiên đều $\pi_u(\mathrm a\mid s)=\pi_u(\mathrm b\mid s)=\tfrac12$ tại cả hai trạng thái có giá trị chính xác $v_{\pi_u}=(14,16)$ (Bài tập 04.10(d)). Một bước cải thiện từ $\pi_0=(\mathrm a,\mathrm a)$ chỉ cho $(\mathrm a,\mathrm b)$.

- (a) Tính bốn giá trị hành động $q_{\pi_u}(s,a)$ và kiểm $v_{\pi_u}(s)=\sum_a\pi_u(a\mid s)\,q_{\pi_u}(s,a)$ tại cả hai trạng thái.
- (b) Xác định chính sách tham lam $\pi'$ theo $v_{\pi_u}$ và các trạng thái mà điều kiện (2.2) của Định lý 04.13 thỏa nghiêm ngặt.
- (c) Đánh giá $\pi'$ và đối chiếu với kết luận (a), (b) của Định lý 04.13.
- (d) Giải thích vì sao một bước cải thiện từ $\pi_u$ chọn $\mathrm b$ tại $\mathrm s_0$, còn một bước từ $\pi_0$ giữ $\mathrm a$.
:::

::: hint Gợi ý Bài tập 04.17
Định lý 04.13 cho phép $\pi$ ngẫu nhiên; chỉ $\pi'$ phải xác định. Giá trị hành động $q_{\pi_u}(s,a)$ ấn định hành động đầu là $a$ rồi theo $\pi_u$, nên phần tiếp nối đọc từ $v_{\pi_u}$.
:::

::: solution Lời giải Bài tập 04.17
**Câu (a).** Với giá trị tiếp nối đọc từ $v_{\pi_u}=(14,16)$:

$$
\begin{aligned}
q_{\pi_u}(\mathrm s_0,\mathrm a)&=1+0{,}9\cdot14=13{,}6, & q_{\pi_u}(\mathrm s_0,\mathrm b)&=0+0{,}9\cdot16=14{,}4,\\
q_{\pi_u}(\mathrm s_1,\mathrm a)&=2+0{,}9\cdot14=14{,}6, & q_{\pi_u}(\mathrm s_1,\mathrm b)&=3+0{,}9\cdot16=17{,}4.
\end{aligned}
$$

Trung bình hai hành động là $\tfrac12(13{,}6+14{,}4)=14$ tại $\mathrm s_0$ và $\tfrac12(14{,}6+17{,}4)=16$ tại $\mathrm s_1$, đúng bằng $v_{\pi_u}$.

**Câu (b).** Tại $\mathrm s_0$, $14{,}4>13{,}6$; tại $\mathrm s_1$, $17{,}4>14{,}6$. Tập cực đại có một phần tử ở mỗi trạng thái, nên quy tắc phá hòa không được dùng và $\pi'=(\mathrm b,\mathrm b)$. Điều kiện (2.2) thỏa nghiêm ngặt ở cả hai trạng thái: $14{,}4>14$ và $17{,}4>16$.

**Câu (c).** Hệ $v_{\pi'}=T_{\pi'}v_{\pi'}$ là $x=0+0{,}9y$ và $y=3+0{,}9y$, nên $y=30$, $x=27$. Bảng $(27,30)$ lớn hơn $(14,16)$ nghiêm ngặt ở cả hai trạng thái, đúng như Định lý 04.13(a) và (b) với (2.2) nghiêm ngặt tại $\mathrm s_0$ và $\mathrm s_1$.

**Câu (d).** Hai lựa chọn tại $\mathrm s_0$ cùng phần thưởng tức thời ($1$ cho $\mathrm a$, $0$ cho $\mathrm b$) và khác nhau ở giá trị tiếp nối. Dưới $\pi_0$, $v_{\pi_0}=(10,11)$ chỉ hơn $1$ ở $\mathrm s_1$, nên $\mathrm b$ cho $0{,}9\cdot11=9{,}9<10$. Dưới $\pi_u$, $v_{\pi_u}=(14,16)$ hơn $2$ ở $\mathrm s_1$, vì $\pi_u$ đã chọn $\mathrm b$ tại $\mathrm s_1$ với xác suất $\tfrac12$; nhánh $\mathrm b$ cho $14{,}4>13{,}6$. Chính sách $(\mathrm b,\mathrm b)$ tối ưu (Ví dụ 04.12 của ghi chú), nhưng Định lý 04.13 chỉ bảo đảm không kém đi; muốn chứng nhận tối ưu phải kiểm $(\mathrm b,\mathrm b)$ ổn định, chẳng hạn bằng bốn giá trị nhìn trước $25{,}3$; $27$; $26{,}3$; $30$ từ $(27,30)$.

**Kiểm tra lại.** Theo Định lý 04.13(c), chính sách tham lam thỏa (2.2), vì giá trị trung bình $v_{\pi_u}(s)$ không vượt cực đại của $q_{\pi_u}(s,\cdot)$. Hai lỗi thường gặp: tính $q_{\pi_u}(s,a)$ bằng cách lấy trung bình cả hành động đầu, cho lại $v_{\pi_u}(s)$; dùng bảng $(0{,}5;\,2{,}5)$ sau một lượt quét (Ví dụ 04.3 của ghi chú) thay cho giá trị chính xác, cho $q(\mathrm s_0,\cdot)=(1{,}45;\,2{,}25)$ và vi phạm giả thiết "giá trị chính xác".
:::

### Bài tập 04.12. Lặp giá trị và lặp chính sách trên MDP ba trạng thái

**Mức độ:** tính toán. Mục tiêu học tập 3, 4 của ghi chú.

**Nguồn:** Bài tập tuần 3 (2025–2026), bài 9; câu (e) bổ sung để hoàn tất vòng lặp chính sách.

::: exercise Bài tập 04.12 (Lặp giá trị và lặp chính sách trên MDP ba trạng thái)
Xét MDP với $\mathcal S=\{\mathrm s_0,\mathrm s_1,\mathrm s_2\}$, không có trạng thái kết thúc, hai hành động $\mathrm a$, $\mathrm b$ tại mọi trạng thái và $\gamma=0{,}9$. Chỉ các hành động tại $\mathrm s_0$ có kết quả ngẫu nhiên; các hành động tại $\mathrm s_1$, $\mathrm s_2$ xác định.

| Trạng thái $s$ | Hành động | Kết quả $(s',r)$ với xác suất |
|---|---|---|
| $\mathrm s_0$ | $\mathrm a$ | $(\mathrm s_0,1)$ với $0{,}5$; $(\mathrm s_2,-1)$ với $0{,}5$ |
| $\mathrm s_0$ | $\mathrm b$ | $(\mathrm s_1,0)$ với $0{,}5$; $(\mathrm s_2,2)$ với $0{,}5$ |
| $\mathrm s_1$ | $\mathrm a$ | $(\mathrm s_0,2)$ với $1$ |
| $\mathrm s_1$ | $\mathrm b$ | $(\mathrm s_1,-1)$ với $1$ |
| $\mathrm s_2$ | $\mathrm a$ | $(\mathrm s_1,2)$ với $1$ |
| $\mathrm s_2$ | $\mathrm b$ | $(\mathrm s_0,0)$ với $1$ |

- (a) Viết quy tắc cập nhật lặp giá trị $V_{k+1}=T_*V_k$ cho từng trạng thái.
- (b) Với $V_0=(0,0,0)$, tính $V_1$ và chính sách tham lam theo $V_0$.
- (c) Với $\pi_0=(\mathrm b,\mathrm a,\mathrm b)$, theo thứ tự $(\mathrm s_0,\mathrm s_1,\mathrm s_2)$, viết hệ phương trình Bellman kỳ vọng và giải để được $v_{\pi_0}$.
- (d) Viết công thức cải thiện chính sách và tính chính sách tham lam $\pi_1$ theo $v_{\pi_0}$.
- (e) Đánh giá $\pi_1$, kiểm $\pi_1$ ổn định, và nêu kết luận về tính tối ưu cùng kết quả của ghi chú được dùng.
:::

::: hint Gợi ý Bài tập 04.12
Tại $\mathrm s_0$, giá trị nhìn trước của mỗi hành động là trung bình của hai kết quả với trọng số $0{,}5$; phép cực đại đứng ngoài trung bình đó. Ở (c) và (e), có thể dùng máy tính bỏ túi; thế phương trình của $\mathrm s_1$, $\mathrm s_2$ vào phương trình của $\mathrm s_0$.
:::

::: solution Lời giải Bài tập 04.12
**Câu (a).** Theo (4.1) của ghi chú, kỳ vọng theo kết quả chuyển nằm trong phép cực đại. Tại $\mathrm s_0$, hai giá trị nhìn trước là

$$
\begin{aligned}
Q_{V_k}(\mathrm s_0,\mathrm a)&=0{,}5\,[1+0{,}9V_k(\mathrm s_0)]+0{,}5\,[-1+0{,}9V_k(\mathrm s_2)],\\
Q_{V_k}(\mathrm s_0,\mathrm b)&=0{,}5\,[0+0{,}9V_k(\mathrm s_1)]+0{,}5\,[2+0{,}9V_k(\mathrm s_2)],
\end{aligned}
$$

và quy tắc cập nhật là

$$
\begin{aligned}
V_{k+1}(\mathrm s_0)&=\max\bigl\{Q_{V_k}(\mathrm s_0,\mathrm a);\ Q_{V_k}(\mathrm s_0,\mathrm b)\bigr\},\\
V_{k+1}(\mathrm s_1)&=\max\bigl\{2+0{,}9V_k(\mathrm s_0);\ -1+0{,}9V_k(\mathrm s_1)\bigr\},\\
V_{k+1}(\mathrm s_2)&=\max\bigl\{2+0{,}9V_k(\mathrm s_1);\ 0+0{,}9V_k(\mathrm s_0)\bigr\}.
\end{aligned}
$$

**Câu (b).** Với $V_0=0$, mỗi nhánh chỉ còn thưởng kỳ vọng một bước. Tại $\mathrm s_0$: nhánh $\mathrm a$ cho $0{,}5\cdot1+0{,}5\cdot(-1)=0$, nhánh $\mathrm b$ cho $0{,}5\cdot0+0{,}5\cdot2=1$. Tại $\mathrm s_1$: $\max\{2;\,-1\}=2$. Tại $\mathrm s_2$: $\max\{2;\,0\}=2$. Vậy $V_1=(1,2,2)$, và chính sách tham lam theo $V_0$ là $(\mathrm b,\mathrm a,\mathrm a)$.

**Câu (c).** Với $x,y,z$ là giá trị của $\pi_0$ tại $\mathrm s_0,\mathrm s_1,\mathrm s_2$:

$$
\begin{aligned}
x&=0{,}5\,(0+0{,}9y)+0{,}5\,(2+0{,}9z)=1+0{,}45y+0{,}45z,\\
y&=2+0{,}9x,\\
z&=0+0{,}9x.
\end{aligned}
$$

Thế hai phương trình sau vào phương trình đầu: $x=1+0{,}45(2+0{,}9x)+0{,}45\cdot0{,}9x=1{,}9+0{,}81x$, nên $0{,}19x=1{,}9$ và $x=10$. Suy ra $y=11$, $z=9$, tức $v_{\pi_0}=(10,11,9)$.

**Câu (d).** Công thức cải thiện là $\pi_1(s)\in\arg\max_aQ_{v_{\pi_0}}(s,a)$ với quy tắc phá hòa của Định nghĩa 04.12. Từ $v_{\pi_0}=(10,11,9)$:

| Trạng thái | $q_{\pi_0}(s,\mathrm a)$ | $q_{\pi_0}(s,\mathrm b)$ | Hành động mới |
|---|---|---|---|
| $\mathrm s_0$ | $0{,}5(1+9)+0{,}5(-1+8{,}1)=8{,}55$ | $0{,}5(0+9{,}9)+0{,}5(2+8{,}1)=10$ | $\mathrm b$ |
| $\mathrm s_1$ | $2+0{,}9\cdot10=11$ | $-1+0{,}9\cdot11=8{,}9$ | $\mathrm a$ |
| $\mathrm s_2$ | $2+0{,}9\cdot11=11{,}9$ | $0+0{,}9\cdot10=9$ | $\mathrm a$ |

Vậy $\pi_1=(\mathrm b,\mathrm a,\mathrm a)$; chính sách chỉ đổi tại $\mathrm s_2$, nơi (2.2) nghiêm ngặt: $11{,}9>9$.

**Câu (e).** Hệ của $\pi_1$ là $x=1+0{,}45y+0{,}45z$, $y=2+0{,}9x$, $z=2+0{,}9y=3{,}8+0{,}81x$. Thế vào phương trình đầu:

$$
x=1+0{,}45(2+0{,}9x)+0{,}45(3{,}8+0{,}81x)=3{,}61+0{,}7695x,
$$

nên $x=3{,}61/0{,}2305=7220/461\approx15{,}662$, $y=7420/461\approx16{,}095$, $z=7600/461\approx16{,}486$. Giá trị nhìn trước từ $v_{\pi_1}$:

- tại $\mathrm s_0$: $\mathrm a$ cho $0{,}5(1+0{,}9\cdot15{,}662)+0{,}5(-1+0{,}9\cdot16{,}486)\approx14{,}466$, $\mathrm b$ cho $\approx15{,}662=v_{\pi_1}(\mathrm s_0)$;
- tại $\mathrm s_1$: $\mathrm a$ cho $\approx16{,}095=v_{\pi_1}(\mathrm s_1)$, $\mathrm b$ cho $-1+0{,}9\cdot16{,}095\approx13{,}486$;
- tại $\mathrm s_2$: $\mathrm a$ cho $\approx16{,}486=v_{\pi_1}(\mathrm s_2)$, $\mathrm b$ cho $0{,}9\cdot15{,}662\approx14{,}095$.

Hành động của $\pi_1$ đạt cực đại tại mọi trạng thái, nên $\pi_1$ ổn định (Định nghĩa 04.16). Theo Định lý 04.20 và Định lý 04.25(d), $\pi_1$ tối ưu trên mọi chính sách và $v_*\approx(15{,}662;\,16{,}095;\,16{,}486)$. Chính sách tham lam theo $V_0$ ở câu (b), và cả chính sách tham lam theo $V_1$ (giá trị nhìn trước $1{,}35<2{,}8$ tại $\mathrm s_0$; $2{,}9>0{,}8$ tại $\mathrm s_1$; $3{,}8>0{,}9$ tại $\mathrm s_2$), đã trùng $\pi_1$ dù $V_1=(1,2,2)$ còn xa $v_*$, như Nhận xét 04.29 của ghi chú nêu.

**Kiểm tra lại.** Thế $(10,11,9)$ vào hệ ở (c): $1+0{,}45\cdot11+0{,}45\cdot9=1+4{,}95+4{,}05=10$, $2+9=11$, $0+9=9$. Bảng $v_{\pi_1}$ lớn hơn $v_{\pi_0}$ tại mọi trạng thái, đúng Định lý 04.13(a). Ba lỗi thường gặp: lấy kết quả tốt hơn của một hành động thay cho trung bình hai kết quả, chẳng hạn cho nhánh $\mathrm b$ tại $\mathrm s_0$ ở câu (b) bằng $2$ thay cho $1$, tức cho tác tử chọn kết quả của môi trường; quên trọng số $0{,}5$ ở phần thưởng của $\mathrm s_0$; kiểm tính ổn định ở câu (e) bằng bảng cũ $v_{\pi_0}$ thay cho $v_{\pi_1}$.
:::

### Bài tập 04.4. Điểm bất động trên dãy năm ô

**Mức độ:** tính toán. Mục tiêu học tập 4 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 25–28; ghi chú bài giảng, Bài tập 04.4.

**Trùng trang chiếu:** [Bài tập: điểm bất động trên dãy năm ô](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/5/15) và [trang lời giải](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/5/16).

::: exercise Bài tập 04.4 (Điểm bất động trên dãy năm ô)
Cho dãy năm ô $\mathrm c_1,\dots,\mathrm c_5$ với $\mathrm c_5$ là trạng thái kết thúc; hành động $\mathrm{trai}$, $\mathrm{phai}$ chuyển xác định sang ô bên cạnh, $\mathrm{trai}$ tại $\mathrm c_1$ giữ nguyên $\mathrm c_1$; phần thưởng $10$ cho chuyển $\mathrm c_4\to\mathrm c_5$ và $-1$ cho mọi chuyển khác; $\gamma=0{,}9$. Bảng $V_4=(4{,}58;\,6{,}2;\,8;\,10;\,0)$ thu được sau bốn lượt quét lặp giá trị đồng bộ từ $V_0=0$.

- (a) Tính hai giá trị nhìn trước tại mỗi ô chưa kết thúc và bảng $T_*V_4$.
- (b) Xác định $\Delta_*(V_4)$ và chính sách tham lam theo $V_4$.
- (c) Giải thích vì sao $V_4(\mathrm c_5)=0$ dù chuyển vào $\mathrm c_5$ nhận phần thưởng $10$.
:::

::: hint Gợi ý Bài tập 04.4
Nhánh $\mathrm{trai}$ tại $\mathrm c_1$ đọc giá trị tiếp nối của chính $\mathrm c_1$. Nhánh $\mathrm{phai}$ tại $\mathrm c_4$ đọc $V_4(\mathrm c_5)=0$.
:::

::: solution Lời giải Bài tập 04.4
**Câu (a).** Giá trị nhìn trước của hai nhánh tại từng ô:

| Ô | Nhánh $\mathrm{trai}$ | Nhánh $\mathrm{phai}$ | Cực đại |
|---|---|---|---|
| $\mathrm c_1$ | $-1+0{,}9\cdot4{,}58=3{,}122$ | $-1+0{,}9\cdot6{,}2=4{,}58$ | $4{,}58$ |
| $\mathrm c_2$ | $-1+0{,}9\cdot4{,}58=3{,}122$ | $-1+0{,}9\cdot8=6{,}2$ | $6{,}2$ |
| $\mathrm c_3$ | $-1+0{,}9\cdot6{,}2=4{,}58$ | $-1+0{,}9\cdot10=8$ | $8$ |
| $\mathrm c_4$ | $-1+0{,}9\cdot8=6{,}2$ | $10+0{,}9\cdot0=10$ | $10$ |

Vậy $T_*V_4=(4{,}58;\,6{,}2;\,8;\,10;\,0)$.

**Câu (b).** $T_*V_4=V_4$ nên $\Delta_*(V_4)=0$; chính sách tham lam đi phải tại $\mathrm c_1,\dots,\mathrm c_4$. Theo Hệ quả 04.27, $\lVert V_4-v_*\rVert_\infty\le0$, tức $V_4=v_*$, và theo Định lý 04.25(b), chính sách này tối ưu.

**Câu (c).** Phần thưởng $10$ thuộc về chuyển $\mathrm c_4\to\mathrm c_5$ và được tính trong $Q_{V_4}(\mathrm c_4,\mathrm{phai})$. Sau khi vào $\mathrm c_5$, lượt (episode) kết thúc và không còn phần thưởng nào, nên giá trị của trạng thái kết thúc bằng $0$.

**Kiểm tra lại.** Tại mỗi ô, nhánh $\mathrm{phai}$ lớn hơn nhánh $\mathrm{trai}$, và giá trị nhánh $\mathrm{phai}$ trùng $V_4$. Lặp giá trị tới đúng $v_*$ sau hữu hạn lượt quét là tính chất của ví dụ này; Hệ quả 04.26 chỉ bảo đảm hội tụ dần. Hai lỗi thường gặp: gán $V(\mathrm c_5)=10$, làm phần thưởng của đích bị đếm hai lần và cho nhánh $\mathrm{phai}$ tại $\mathrm c_4$ bằng $19$; cho nhánh $\mathrm{trai}$ tại $\mathrm c_1$ đọc $V_4(\mathrm c_2)$ thay vì $V_4(\mathrm c_1)$, cho $-1+0{,}9\cdot6{,}2=4{,}58$ và một hòa giả giữa hai nhánh.
:::

### Bài tập 04.11. Tính đơn điệu của toán tử Bellman tối ưu

**Mức độ:** chứng minh. Mục tiêu học tập 4 của ghi chú.

**Nguồn:** Bài tập tuần 3 (2025–2026), bài 7; ghi chú bài giảng, Bổ đề 04.2 (tính đơn điệu của $T_\pi$) và Hệ quả 04.26.

::: exercise Bài tập 04.11 (Tính đơn điệu của toán tử Bellman tối ưu)
Xét MDP hữu hạn với phần thưởng bị chặn, tập hành động hữu hạn và $0\le\gamma<1$; mọi bảng bằng $0$ tại $s_{\mathrm{term}}$. Bổ đề 04.2 của ghi chú đã chứng minh: nếu $U\le V$ theo từng trạng thái thì $T_\pi U\le T_\pi V$.

- (a) Chứng minh: nếu $U\le V$ theo từng trạng thái thì $T_*U\le T_*V$.
- (b) Chứng minh: nếu $V_0\le T_*V_0$ thì dãy lặp giá trị $V_{k+1}=T_*V_k$ không giảm theo từng trạng thái và $V_0\le v_*$; nếu $W_0\ge T_*W_0$ thì dãy $W_{k+1}=T_*W_k$ không tăng và $W_0\ge v_*$.
- (c) Trên mô hình hai trạng thái ($\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$), kiểm điều kiện của (b) cho $V_0=(0,0)$ và $W_0=(30,30)$, tính $W_1$, $W_2$, rồi dùng $v_{(\mathrm b,\mathrm b)}=(27,30)$ để xác định $v_*$ mà không giải phương trình Bellman tối ưu.
- (d) Chỉ ra giả thiết dùng ở (a) và giả thiết chỉ cần ở (b).
:::

::: hint Gợi ý Bài tập 04.11
Ở (a), so sánh $Q_U(s,a)$ với $Q_V(s,a)$ cho từng hành động trước, rồi mới lấy cực đại. Ở (b), quy nạp theo $k$ bằng (a), rồi chuyển qua giới hạn bằng Hệ quả 04.26.
:::

::: solution Lời giải Bài tập 04.11
**Câu (a).** Cố định $s\in\mathcal S$ và $a\in\mathcal A(s)$. Phần thưởng triệt tiêu khi lấy hiệu hai giá trị nhìn trước:

$$
\begin{aligned}
Q_V(s,a)-Q_U(s,a)
&=\gamma\sum_{s',r}p(s',r\mid s,a)\bigl[V(s')-U(s')\bigr]\\
&\ge0 .
\end{aligned}
$$

Dòng đầu là Định nghĩa 04.11. Dòng sau dùng $p\ge0$, $\gamma\ge0$ và $V(s')-U(s')\ge0$; tại $s_{\mathrm{term}}$, hiệu bằng $0$ vì cả hai bảng bằng $0$ ở đó.

Do đó $Q_U(s,a)\le Q_V(s,a)\le\max_{a'}Q_V(s,a')=(T_*V)(s)$ với mọi $a$. Lấy cực đại theo $a$ ở vế trái, ta được $(T_*U)(s)\le(T_*V)(s)$. Điều này đúng với mọi $s$, nên $T_*U\le T_*V$.

**Câu (b).** Quy nạp theo $k$. Với $k=0$, $V_0\le T_*V_0=V_1$ là giả thiết. Nếu $V_{k-1}\le V_k$ thì theo (a), $V_k=T_*V_{k-1}\le T_*V_k=V_{k+1}$. Vậy dãy không giảm và $V_0\le V_k$ với mọi $k$. Theo Hệ quả 04.26, $V_k\to v_*$; bất đẳng thức không nghiêm ngặt giữ khi lấy giới hạn, nên $V_0\le v_*$. Với $W_0\ge T_*W_0$, cùng lập luận với chiều bất đẳng thức đảo lại cho $W_0\ge W_1\ge\cdots\to v_*$, nên $W_0\ge v_*$.

**Câu (c).** $T_*V_0=(\max\{1;0\},\max\{2;3\})=(1,3)\ge(0,0)$, nên điều kiện thứ nhất thỏa. Với $W_0=(30,30)$:

$$
\begin{aligned}
W_1&=\bigl(\max\{1+27;\ 0+27\},\ \max\{2+27;\ 3+27\}\bigr)=(28,30)\le W_0,\\
W_2&=\bigl(\max\{1+25{,}2;\ 0+27\},\ \max\{2+25{,}2;\ 3+27\}\bigr)=(27,30).
\end{aligned}
$$

Theo chứng minh (b), $W_0\ge W_1\ge W_2\ge\cdots\to v_*$, nên $v_*\le W_2=(27,30)$. Theo Định nghĩa 04.19, $v_*$ là cận trên đúng của giá trị mọi chính sách, nên $v_*\ge v_{(\mathrm b,\mathrm b)}=(27,30)$. Hai chặn trùng nhau, nên $v_*=(27,30)$. Dãy từ dưới lên đi qua $(0,0)$, $(1,3)$, $(2{,}7;\,5{,}7)$, đều nằm dưới $(27,30)$.

**Câu (d).** Câu (a) chỉ dùng $p(s',r\mid s,a)\ge0$, $\gamma\ge0$ và tập hành động hữu hạn để cực đại đạt; nó không cần $\gamma<1$. Câu (b) cần thêm $\gamma<1$ ở bước chuyển qua giới hạn, vì Hệ quả 04.26 dựa trên tính co của $T_*$.

**Kiểm tra lại.** Kiểm (a) trên một cặp bảng: $(0,0)\le(10,11)$ cho $T_*(0,0)=(1,3)\le(10;\,12{,}9)=T_*(10,11)$. Ba lỗi thường gặp: lấy cực đại trước rồi so sánh, với lập luận "cực đại của $U$ nhỏ hơn cực đại của $V$" mà không qua bước so sánh từng hành động; nhầm tính đơn điệu với tính tăng, tức kết luận $T_*V\ge V$ cho mọi $V$, trong khi $T_*(30,30)=(28,30)\le(30,30)$; quên rằng hiệu tại $s_{\mathrm{term}}$ bằng $0$ vì cả hai bảng cố định bằng $0$ ở đó.
:::

### Bài tập 04.5. Lịch bỏ sót một trạng thái

**Mức độ:** tính toán. Mục tiêu học tập 5 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 15, 17–18; ghi chú bài giảng, Bài tập 04.5; Sutton và Barto (2018), §4.5.

**Trùng trang chiếu:** [Bài tập: lịch bỏ sót một trạng thái](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/6/9) và [trang lời giải](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/6/10).

::: exercise Bài tập 04.5 (Lịch bỏ sót một trạng thái)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$; $v_*=(27,30)$. Lặp giá trị bất đồng bộ (Thuật toán 04.31) bắt đầu từ $V=(0,0)$ với lịch chỉ gồm $\mathrm s_0$, lặp lại mãi mãi; mỗi bước gán $V(\mathrm s_0)\leftarrow(T_*V)(\mathrm s_0)$ và giữ nguyên $V(\mathrm s_1)$.

- (a) Viết quy tắc cập nhật tại $\mathrm s_0$ và tìm giới hạn của $V(\mathrm s_0)$.
- (b) Cho biết giá trị của $V(\mathrm s_1)$ và so bảng giới hạn với $v_*$.
- (c) Chỉ ra giả thiết của Định lý 04.32 bị vi phạm và bước của chứng minh không còn đúng.
:::

::: hint Gợi ý Bài tập 04.5
Vì $V(\mathrm s_1)$ không bao giờ được cập nhật, nhánh $\mathrm b$ tại $\mathrm s_0$ luôn đọc giá trị tiếp nối $0$.
:::

::: solution Lời giải Bài tập 04.5
**Câu (a).** Mỗi bước gán $V(\mathrm s_0)\leftarrow\max\{1+0{,}9V(\mathrm s_0);\ 0+0{,}9\cdot0\}$. Từ $V(\mathrm s_0)=0$, nhánh $\mathrm a$ luôn lớn hơn, và dãy $1;\,1{,}9;\,2{,}71;\dots$ hội tụ về nghiệm của $x=1+0{,}9x$, tức $x=10$.

**Câu (b).** $V(\mathrm s_1)=0$ mãi mãi. Bảng giới hạn $(10,0)$ khác $v_*=(27,30)$ ở cả hai trạng thái; chính sách tham lam theo bảng này tại $\mathrm s_0$ là $\mathrm a$, trong khi chính sách tối ưu chọn $\mathrm b$.

**Câu (c).** Giả thiết "mỗi trạng thái chưa kết thúc xuất hiện vô hạn lần trong lịch" bị vi phạm vì $\mathrm s_1$ không xuất hiện lần nào. Bước 2 của chứng minh cần các đoạn phủ mọi trạng thái; ở đây không có đoạn nào như vậy, nên sai số tại $\mathrm s_1$ giữ nguyên $30$.

**Kiểm tra lại.** $x=10$ thỏa $10=\max\{1+0{,}9\cdot10;\ 0\}$; tăng số lần cập nhật tại $\mathrm s_0$ không đổi giới hạn này. Điểm bất động của $T_*$ vẫn là $v_*$; lịch quyết định thuật toán có tới đó hay không. Hai lỗi thường gặp: kết luận lặp giá trị bất đồng bộ "hội tụ về $v_*$ với mọi lịch", bỏ qua giả thiết vô hạn lần; đo phần dư chỉ tại các ô được cập nhật, cho $\lvert(T_*V)(\mathrm s_0)-V(\mathrm s_0)\rvert\to0$ và một nhãn "đạt ngưỡng" sai, trong khi phần dư trên toàn bảng tại $(10,0)$ là $\max\{0;\ \lvert\max\{2+9;\,3\}-0\rvert\}=11$.
:::

## Mức vận dụng vào bài toán Học tăng cường

### Bài tập 04.13. Lặp giá trị trên dãy năm ô trơn trượt

**Mức độ:** vận dụng. Mục tiêu học tập 4 của ghi chú.

**Nguồn:** Bài tập tuần 4 (2025–2026), bài 10. Câu (b) nối tiếp trang [Ví dụ: dãy năm ô trơn trượt](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/5/14), nơi đã tính $V_1(\mathrm c_4)=7{,}8$. Phiếu bài tập chỉ cho mô hình; quy ước tại biên $\mathrm c_1$ và phần thưởng của chuyển trượt vào $\mathrm c_5$ lấy theo trang ví dụ đó, còn bốn câu hỏi do bài này đặt. Bảng $v_*$ ở câu (d) tính bằng chương trình (lặp giá trị tới phần dư dưới $10^{-12}$, đối chiếu với nghiệm hệ tuyến tính của chính sách luôn đi phải).

::: exercise Bài tập 04.13 (Lặp giá trị trên dãy năm ô trơn trượt)
Dãy năm ô $\mathrm c_1,\dots,\mathrm c_5$, $\mathrm c_5$ là trạng thái kết thúc, hai hành động $\mathrm{trai}$, $\mathrm{phai}$, $\gamma=0{,}9$. Robot trượt: khi chọn một hướng, nó đi đúng hướng với xác suất $0{,}8$, đứng yên với xác suất $0{,}1$ và đi ngược hướng với xác suất $0{,}1$. Tại $\mathrm c_1$, chuyển ra ngoài dãy được thay bằng đứng yên. Mọi chuyển vào $\mathrm c_5$ nhận phần thưởng $10$, kể cả khi do trượt; mọi chuyển khác, kể cả đứng yên, nhận $-1$.

- (a) Viết các bộ $(s',r)$ và xác suất của $p(\cdot,\cdot\mid s,a)$ tại $\mathrm c_1$ và tại $\mathrm c_4$ cho cả hai hành động.
- (b) Từ $V_0=0$, tính $V_1$, rồi tính hai giá trị nhìn trước tại $\mathrm c_3$ từ $V_1$ và $V_2(\mathrm c_3)$.
- (c) Chọn ngưỡng dừng $\theta$ để bảng trả về có sai số không quá $\kappa=0{,}1$, và nêu kết quả của ghi chú bảo đảm điều đó.
- (d) Một chương trình cho $v_*\approx(2{,}659;\,4{,}417;\,6{,}639;\,9{,}228;\,0)$. Kiểm phương trình Bellman tối ưu tại $\mathrm c_4$ tới ba chữ số thập phân, xác định hành động tối ưu tại $\mathrm c_4$, và so $v_*(\mathrm c_1)$ với giá trị $4{,}58$ của dãy năm ô không trượt.
:::

::: hint Gợi ý Bài tập 04.13
Mỗi giá trị nhìn trước là trung bình của ba kết quả chuyển với trọng số $0{,}8$; $0{,}1$; $0{,}1$; tại $\mathrm c_1$, hai kết quả trùng ô thì cộng xác suất. Ở (b), trạng thái kết thúc có giá trị $0$, và phần thưởng $10$ thuộc về chuyển vào $\mathrm c_5$.
:::

::: solution Lời giải Bài tập 04.13
**Câu (a).** Tại $\mathrm c_1$, chuyển ra ngoài dãy gộp vào đứng yên; tại $\mathrm c_4$, cả hai hành động có thể đưa robot vào $\mathrm c_5$.

| $(s,a)$ | Kết quả $(s',r)$ với xác suất |
|---|---|
| $(\mathrm c_1,\mathrm{trai})$ | $(\mathrm c_1,-1)$ với $0{,}8+0{,}1=0{,}9$; $(\mathrm c_2,-1)$ với $0{,}1$ |
| $(\mathrm c_1,\mathrm{phai})$ | $(\mathrm c_2,-1)$ với $0{,}8$; $(\mathrm c_1,-1)$ với $0{,}1+0{,}1=0{,}2$ |
| $(\mathrm c_4,\mathrm{trai})$ | $(\mathrm c_3,-1)$ với $0{,}8$; $(\mathrm c_4,-1)$ với $0{,}1$; $(\mathrm c_5,10)$ với $0{,}1$ |
| $(\mathrm c_4,\mathrm{phai})$ | $(\mathrm c_5,10)$ với $0{,}8$; $(\mathrm c_4,-1)$ với $0{,}1$; $(\mathrm c_3,-1)$ với $0{,}1$ |

Mỗi hàng có tổng xác suất bằng $1$.

**Câu (b).** Với $V_0=0$, mỗi giá trị nhìn trước là thưởng kỳ vọng một bước. Tại $\mathrm c_1,\mathrm c_2,\mathrm c_3$, mọi kết quả cho $-1$, nên $V_1=-1$ ở ba ô này. Tại $\mathrm c_4$:

$$
\begin{aligned}
Q_{V_0}(\mathrm c_4,\mathrm{phai})&=0{,}8\cdot10+0{,}1\cdot(-1)+0{,}1\cdot(-1)=7{,}8,\\
Q_{V_0}(\mathrm c_4,\mathrm{trai})&=0{,}8\cdot(-1)+0{,}1\cdot(-1)+0{,}1\cdot10=0{,}1.
\end{aligned}
$$

Vậy $V_1=(-1;\,-1;\,-1;\,7{,}8;\,0)$. Tại $\mathrm c_3$, đọc $V_1$; kết quả "sang $\mathrm c_4$" có giá trị $-1+0{,}9\cdot7{,}8=6{,}02$, các kết quả còn lại có giá trị $-1+0{,}9\cdot(-1)=-1{,}9$:

$$
\begin{aligned}
Q_{V_1}(\mathrm c_3,\mathrm{phai})&=0{,}8\cdot6{,}02+0{,}1\cdot(-1{,}9)+0{,}1\cdot(-1{,}9)=4{,}436,\\
Q_{V_1}(\mathrm c_3,\mathrm{trai})&=0{,}8\cdot(-1{,}9)+0{,}1\cdot(-1{,}9)+0{,}1\cdot6{,}02=-1{,}108.
\end{aligned}
$$

Vậy $V_2(\mathrm c_3)=4{,}436$, đạt tại $\mathrm{phai}$. Tại $\mathrm c_4$, đọc $V_1$:

$$
\begin{aligned}
Q_{V_1}(\mathrm c_4,\mathrm{phai})&=0{,}8\cdot10+0{,}1\cdot6{,}02+0{,}1\cdot(-1{,}9)=8{,}412,\\
Q_{V_1}(\mathrm c_4,\mathrm{trai})&=0{,}8\cdot(-1{,}9)+0{,}1\cdot6{,}02+0{,}1\cdot10=0{,}082,
\end{aligned}
$$

với $6{,}02$ là giá trị của kết quả "ở lại $\mathrm c_4$" và $-1{,}9$ là giá trị của kết quả "sang $\mathrm c_3$". Tại $\mathrm c_1$, $\mathrm c_2$, mọi kết quả cho $-1+0{,}9\cdot(-1)=-1{,}9$. Vậy $V_2=(-1{,}9;\,-1{,}9;\,4{,}436;\,8{,}412;\,0)$.

**Câu (c).** Theo Hệ quả 04.27, nếu $\Delta_*(V)\le\theta$ với $\theta=(1-\gamma)\kappa$ thì $\lVert V-v_*\rVert_\infty\le\kappa$. Với $\gamma=0{,}9$ và $\kappa=0{,}1$, $\theta=0{,}1\cdot0{,}1=0{,}01$. Các giả thiết của Hệ quả 04.27 thỏa: MDP hữu hạn có tính Markov, phần thưởng bị chặn bởi $10$, $\gamma<1$, mô hình $p$ cho ở câu (a). Chặn thuộc về bảng $V$ được đo phần dư; Thuật toán 04.28 trả đúng bảng đó. Một chương trình chạy Thuật toán 04.28 với $\theta=0{,}01$ dừng sau $12$ lượt quét, phần dư khoảng $0{,}0087$ và sai số thật khoảng $0{,}018$, dưới chặn $0{,}087$.

**Câu (d).** Tại $\mathrm c_4$, với $v_*(\mathrm c_3)\approx6{,}639$ và $v_*(\mathrm c_4)\approx9{,}228$:

$$
\begin{aligned}
Q_{v_*}(\mathrm c_4,\mathrm{phai})&\approx0{,}8\cdot10+0{,}1\cdot7{,}3052+0{,}1\cdot4{,}9751\approx9{,}228,\\
Q_{v_*}(\mathrm c_4,\mathrm{trai})&\approx0{,}8\cdot4{,}9751+0{,}1\cdot7{,}3052+0{,}1\cdot10\approx5{,}711,
\end{aligned}
$$

với $7{,}3052=-1+0{,}9\cdot9{,}228$ (ở lại $\mathrm c_4$) và $4{,}9751=-1+0{,}9\cdot6{,}639$ (sang $\mathrm c_3$).

Cực đại $9{,}228$ trùng $v_*(\mathrm c_4)$, nên phương trình Bellman tối ưu thỏa tại $\mathrm c_4$ tới ba chữ số thập phân, và hành động tối ưu tại $\mathrm c_4$ là $\mathrm{phai}$. Giá trị $v_*(\mathrm c_1)\approx2{,}659$ nhỏ hơn $4{,}58$ của dãy không trượt: mỗi lần đứng yên hoặc lùi lại tốn thêm phần thưởng $-1$ và làm phần thưởng $10$ đến muộn hơn, nên bị chiết khấu nhiều hơn.

**Kiểm tra lại.** Thế $v_*$ vào phương trình Bellman tối ưu tại $\mathrm c_3$: $Q_{v_*}(\mathrm c_3,\mathrm{phai})\approx0{,}8\cdot7{,}3052+0{,}1\cdot4{,}9751+0{,}1\cdot2{,}9754\approx6{,}639=v_*(\mathrm c_3)$, với $7{,}3052$; $4{,}9751$; $2{,}9754$ là giá trị $-1+0{,}9\,v_*$ của các ô $\mathrm c_4$, $\mathrm c_3$, $\mathrm c_2$. Ba lỗi thường gặp: gán phần thưởng $-1$ cho chuyển trượt vào $\mathrm c_5$ khi chọn $\mathrm{trai}$ tại $\mathrm c_4$, cho $-1$ thay cho $0{,}1$; quên gộp chuyển ra ngoài dãy vào đứng yên tại $\mathrm c_1$, làm tổng xác suất chỉ còn $0{,}9$; lấy $V_1(\mathrm c_4)=10$ như dãy không trượt, cho $V_2(\mathrm c_3)=0{,}8\cdot8-0{,}38=6{,}02$ thay cho $4{,}436$ (số $6{,}02$ này trùng giá trị của kết quả "sang $\mathrm c_4$" ở câu (b) nhưng là đại lượng khác).
:::

### Bài tập 04.14. Số lượt quét của lặp giá trị theo hệ số chiết khấu [Lập trình]

**Mức độ:** vận dụng. Mục tiêu học tập 4 (chặn hội tụ của lặp giá trị) và 5 (đọc bảo đảm trên MDP ước lượng của CartPole rời rạc hóa) của ghi chú. Bài xếp ở mạch 6 vì dùng MDP ước lượng của Mục 5.4.

**Nguồn:** bài thực hành `thuc-hanh-cartpole-quy-hoach-dong.ipynb`, mục 7.2 (hàm `value_iteration`), mục 7.3–7.4 (chặn $\gamma^k\Delta_*(V_0)$ và bảng số lượt quét theo $\gamma$) và ý "số lượt quét" của nhiệm vụ 5; ghi chú bài giảng, Mệnh đề 04.24, Hệ quả 04.27 và đoạn "Trong thực hành" của Mục 4.4.

::: exercise Bài tập 04.14 (Số lượt quét của lặp giá trị theo hệ số chiết khấu)
Bài thực hành CartPole lập MDP ước lượng gồm $324$ ô chưa kết thúc, một trạng thái kết thúc $s_{\mathrm{term}}$, hai hành động, mô hình $\hat p(s'\mid s,a)$ và phần thưởng $\hat r(s,a)=1$ với mọi cặp. Lặp giá trị đồng bộ (Thuật toán 04.28) chạy từ $V_0=0$ với sai số cho phép $\kappa=0{,}01$, ngưỡng $\theta=(1-\gamma)\kappa$ và $\gamma\in\{0{,}9;\ 0{,}95;\ 0{,}99;\ 0{,}995\}$; mỗi giá trị $\gamma$ cho một bài toán khác nhau.

- (a) Chứng minh $\Delta_*(V_0)=1$ và $\Delta_*(V_k)\le\gamma^k\Delta_*(V_0)$. Suy ra số lượt quét $k\ge\ln\theta/\ln\gamma$ là đủ, và tính số nguyên nhỏ nhất thỏa điều kiện này cho bốn giá trị $\gamma$.
- (b) Dùng xấp xỉ $\ln\gamma\approx-(1-\gamma)$ khi $\gamma$ gần $1$ để giải thích số lượt quét tăng xấp xỉ theo $1/(1-\gamma)$ nhân một thừa số logarit.
- (c) Đặt $D_k=V_k-V_{k-1}$ với $k\ge1$ và gọi $\pi_k$ là chính sách tham lam theo $V_k$. Chứng minh $0\le D_{k+1}\le\gamma P_{\pi_k}D_k$ theo từng ô, với $P_{\pi_k}$ là ma trận chuyển giữa các ô chưa kết thúc dưới $\pi_k$. Suy ra $\Delta_*(V_k)\le\gamma^k\rho_k$, trong đó $\rho_k=\max_s\bigl(P_{\pi_k}P_{\pi_{k-1}}\cdots P_{\pi_1}\mathbf 1\bigr)(s)\le1$ là xác suất lớn nhất theo ô xuất phát để lượt chưa kết thúc sau $k$ bước khi lần lượt dùng $\pi_k,\pi_{k-1},\dots,\pi_1$.
- (d) [Lập trình] Sửa hàm `value_iteration` của notebook để trong khi chạy, ở mỗi $k\ge1$, ghi $\Delta_*(V_k)$, tỉ số $\Delta_*(V_k)/\gamma^k$ và $\rho_k$, với $\rho_k$ tính đệ quy qua vectơ $u_k=P_{\pi_k}u_{k-1}$, $u_0=\mathbf 1$. Với bốn giá trị $\gamma$, ghi số lượt quét tới nhãn "đạt ngưỡng", so với chặn ở (a), và kiểm bất đẳng thức $\Delta_*(V_k)/\gamma^k\le\rho_k$ của (c) tại mọi $k$. Dùng kết quả để giải thích khoảng cách giữa số đo được và chặn.
:::

::: hint Gợi ý Bài tập 04.14
Ở (a), $\Delta_*(V_k)=\lVert T_*V_k-T_*V_{k-1}\rVert_\infty$ với lượt quét đồng bộ, rồi dùng Mệnh đề 04.24. Ở (c), tính $D_{k+1}(s)$ bằng cùng một hành động $\pi_k(s)$ cho cả hai số hạng; tính không âm của $D_k$ suy từ Bài tập 04.11(b). Ở (d), trong vòng lặp của `value_iteration`, biến `pi_V` chính là $\pi_k$ khi bảng hiện tại là $V_k$, và `P[pi_V, states, :n]` là ma trận $P_{\pi_k}$ cỡ $(n,n)$.
:::

::: solution Lời giải Bài tập 04.14
**Câu (a).** Với $V_0=0$, mỗi giá trị nhìn trước chỉ còn phần thưởng, nên $(T_*V_0)(s)=\max_a\hat r(s,a)=1$ tại mọi ô và $\Delta_*(V_0)=\lVert\mathbf 1-0\rVert_\infty=1$. Với $k\ge1$, lượt quét đồng bộ cho $V_k=T_*V_{k-1}$, nên

$$
\begin{aligned}
\Delta_*(V_k)
&=\lVert T_*V_k-T_*V_{k-1}\rVert_\infty &&\text{(}V_k=T_*V_{k-1})\\
&\le\gamma\lVert V_k-V_{k-1}\rVert_\infty &&\text{(Mệnh đề 04.24)}\\
&=\gamma\,\Delta_*(V_{k-1}) &&\text{(}V_k=T_*V_{k-1}).
\end{aligned}
$$

Quy nạp cho $\Delta_*(V_k)\le\gamma^k$. Thuật toán dừng ở lượt quét đầu tiên có $\Delta_*(V_k)\le\theta$; điều kiện $\gamma^k\le\theta$ là đủ, tức $k\ln\gamma\le\ln\theta$. Chia hai vế cho $\ln\gamma<0$ đổi chiều bất đẳng thức, cho $k\ge\ln\theta/\ln\gamma$.

| $\gamma$ | $\theta=(1-\gamma)\cdot0{,}01$ | $\ln\theta/\ln\gamma$ | Chặn số lượt quét |
|---|---:|---:|---:|
| $0{,}9$ | $10^{-3}$ | $65{,}56$ | $66$ |
| $0{,}95$ | $5\cdot10^{-4}$ | $148{,}19$ | $149$ |
| $0{,}99$ | $10^{-4}$ | $916{,}42$ | $917$ |
| $0{,}995$ | $5\cdot10^{-5}$ | $1975{,}74$ | $1976$ |

**Câu (b).** Với $\gamma$ gần $1$, $\ln\gamma\approx-(1-\gamma)$, nên

$$
\frac{\ln\theta}{\ln\gamma}\approx\frac{1}{1-\gamma}\,\ln\frac{1}{(1-\gamma)\kappa}.
$$

Thừa số thứ nhất là $10$; $20$; $100$; $200$, còn thừa số logarit chỉ tăng từ $\ln10^3\approx6{,}9$ lên $\ln(2\cdot10^4)\approx9{,}9$. Xấp xỉ cho $69$; $152$; $921$; $1981$, gần các chặn ở (a). Ngưỡng $\theta=(1-\gamma)\kappa$ nhỏ đi khi $\gamma$ tăng, nên thừa số logarit cũng tăng theo $\gamma$.

**Câu (c).** Theo Bài tập 04.11(b), $V_0=0\le\mathbf 1=T_*V_0$ kéo theo dãy $V_k$ không giảm, nên $D_k\ge0$. Cố định một ô $s$ và đặt $a=\pi_k(s)$. Vì $a$ đạt cực đại của $Q_{V_k}(s,\cdot)$, ta có $(T_*V_k)(s)=Q_{V_k}(s,a)$; vì $T_*$ lấy cực đại, $(T_*V_{k-1})(s)\ge Q_{V_{k-1}}(s,a)$. Trừ hai đẳng thức và bất đẳng thức này; phần thưởng triệt tiêu và hiệu tại $s_{\mathrm{term}}$ bằng $0$:

$$
D_{k+1}(s)=(T_*V_k)(s)-(T_*V_{k-1})(s)\le Q_{V_k}(s,a)-Q_{V_{k-1}}(s,a)=\gamma\sum_{s'\in\mathcal S}\hat p(s'\mid s,a)\,D_k(s').
$$

Vậy $D_{k+1}\le\gamma P_{\pi_k}D_k$. Ma trận $P_{\pi_j}$ không âm nên giữ chiều bất đẳng thức; lặp lại và dùng $D_1=V_1-V_0=\mathbf 1$:

$$
D_{k+1}\le\gamma^k\,P_{\pi_k}P_{\pi_{k-1}}\cdots P_{\pi_1}\mathbf 1 .
$$

Thành phần tại $s$ của $P_{\pi_k}\cdots P_{\pi_1}\mathbf 1$ là xác suất lượt chưa vào $s_{\mathrm{term}}$ sau $k$ bước khi xuất phát từ $s$ và dùng $\pi_k$ ở bước thứ nhất, $\pi_{k-1}$ ở bước thứ hai, …, $\pi_1$ ở bước thứ $k$; tổng mỗi hàng của $P_\pi$ bằng $1-\hat p(s_{\mathrm{term}}\mid s,\pi(s))$. Lấy cực đại theo $s$: $\Delta_*(V_k)=\lVert D_{k+1}\rVert_\infty\le\gamma^k\rho_k\le\gamma^k$.

**Câu (d).** Một cách sửa hàm, dùng `lookahead` của notebook:

```python
def value_iteration_rho(P, R, gamma, eta, K):
    n = P.shape[1]; states = np.arange(n)
    V, u, k, rows = np.zeros(n), np.ones(n), 0, []
    while True:
        Q = lookahead(V, P, R, gamma)           # Q_{V_k}, cỡ (n, 2)
        W, pi_V = Q.max(axis=1), Q.argmax(axis=1)
        delta = np.abs(W - V).max()             # Delta_*(V_k)
        if k >= 1:
            u = P[pi_V, states, :n] @ u         # u_k = P_{pi_k} u_{k-1}, cỡ (n,)
            rows.append((k, delta, delta / gamma**k, u.max()))  # u.max() = rho_k
        if delta <= eta or k == K:
            return k, np.array(rows)
        V, k = W, k + 1
```

Kiểm tra cần thấy: ở mọi dòng, cột $\Delta_*(V_k)/\gamma^k$ không vượt cột $\rho_k$ (sai khác cỡ làm tròn số thực được bỏ qua), và cả hai không vượt $1$. Số lượt quét đo được trong lần chạy đã nhúng ở mục 7.4 của notebook là:

| $\gamma$ | Chặn ở (a) | Đo được | Tỉ số |
|---|---:|---:|---:|
| $0{,}9$ | $66$ | $65$ | $0{,}985$ |
| $0{,}95$ | $149$ | $143$ | $0{,}960$ |
| $0{,}99$ | $917$ | $736$ | $0{,}803$ |
| $0{,}995$ | $1976$ | $1\,315$ | $0{,}665$ |

Với phiên bản gói khác, mô hình ước lượng có thể khác và số lượt quét có thể khác các số trên; chặn ở (a) không đổi vì chỉ dùng $\Delta_*(V_0)=1$. Với $\gamma=0{,}99$, output nhúng ở mục 7.2 cho $\Delta_*(V_{736})=9{,}88\cdot10^{-5}$, còn $0{,}99^{736}\approx6{,}13\cdot10^{-4}$, nên tỉ số tại điểm dừng khoảng $0{,}16$; theo (c), $\rho_{736}\ge0{,}16$.

Khi $\gamma^k\le\theta$, điều kiện dừng chắc chắn thỏa, nên số đo được không vượt chặn ở (a). Khi $\rho_k<1$, phần dư xuống dưới $\theta$ sớm hơn. Bảng $\rho_k$ của chương trình cho biết trực tiếp xác suất chưa kết thúc giảm thế nào theo $k$ trên MDP ước lượng: nếu $\rho_k$ giảm rõ khi $k$ lớn, tỉ số "đo được/chặn" giảm khi $\gamma$ tăng như bảng trên, vì $\gamma$ lớn đòi nhiều lượt quét hơn.

**Kiểm tra lại.** Với $\gamma=0{,}9$: $0{,}9^{65}\approx1{,}06\cdot10^{-3}>10^{-3}$ và $0{,}9^{66}\approx9{,}55\cdot10^{-4}\le10^{-3}$, nên chặn là $66$. Ba lỗi thường gặp: lấy $\theta=\kappa$, bỏ thừa số $1-\gamma$, cho $\ln0{,}01/\ln0{,}99\approx458{,}2$, tức $459$ lượt quét với $\gamma=0{,}99$, và bảng trả về khi đó chỉ được chặn sai số $1$ thay cho $0{,}01$; chia cho $\ln\gamma$ mà không đổi chiều bất đẳng thức; cập nhật $u$ bằng chính sách tham lam theo $V_{k+1}$ thay cho $V_k$, làm lệch thứ tự các ma trận trong tích của (c).
:::

### Bài tập 04.15. Lặp chính sách cải biên [Lập trình]

**Mức độ:** vận dụng. Mục tiêu học tập 3, 5 của ghi chú.

**Nguồn:** bài thực hành `thuc-hanh-cartpole-quy-hoach-dong.ipynb`, nhiệm vụ 7; ghi chú bài giảng, mục Đọc thêm (lặp chính sách cải biên), Thuật toán 04.17, Mệnh đề 04.18, Hệ quả 04.27 và Ví dụ 04.16 (cập nhật tại chỗ); Puterman (1994), §6.5.

::: exercise Bài tập 04.15 (Lặp chính sách cải biên)
Lặp chính sách cải biên (modified policy iteration) với tham số nguyên $\ell\ge1$ chạy như sau. Khởi tạo chính sách xác định $\pi\leftarrow\pi_0$ và bảng $V\leftarrow0$. Mỗi vòng gồm bốn bước: (1) áp dụng $T_\pi$ đúng $\ell$ lần cho $V$, xuất phát từ bảng của vòng trước; (2) tính $Q_V(s,a)$ cho mọi cặp, phần dư $\Delta_*(V)$ và chính sách tham lam $\pi_V$ theo quy tắc phá hòa; (3) nếu $\Delta_*(V)\le\theta$, trả $(V,\pi_V,\Delta_*(V))$ với nhãn "đạt ngưỡng"; (4) gán $\pi\leftarrow\pi_V$ và sang vòng sau. Mỗi vòng được đếm là $\ell+1$ phép áp dụng toán tử: $\ell$ lần $T_\pi$ và một lần tính $Q_V$ trên toàn bảng.

- (a) Trên mô hình hai trạng thái ($\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$) với $\pi_0=(\mathrm a,\mathrm a)$ và $\ell=1$, tính $V$, $\pi_V$ và $\Delta_*(V)$ ở ba vòng đầu. Chỉ ra rằng từ vòng thứ hai, bảng mới bằng $T_*$ áp dụng cho bảng của vòng trước.
- (b) Một phiên bản khác thay bước (3) bằng điều kiện dừng của Thuật toán 04.17: dừng khi $\pi_V=\pi$. Với $\ell=1$ trên cùng mô hình, xác định vòng dừng và bảng $V$ khi dừng; so $V$ với $v_*=(27,30)$ và với chặn của Hệ quả 04.27. Giải thích vì sao Mệnh đề 04.18 không áp dụng.
- (c) [Lập trình] Viết chương trình cho mô hình hai trạng thái với $\theta=0{,}01$ và $\ell\in\{1,5,20\}$; ghi số vòng và tổng số phép áp dụng toán tử tới nhãn "đạt ngưỡng".
- (d) [Lập trình] Trong notebook (nhiệm vụ 7), chạy phiên bản dừng theo phần dư trên CartPole rời rạc hóa với $\gamma=0{,}99$, $\theta=10^{-4}$, chính sách khởi tạo theo dấu góc và $\ell\in\{1,5,20\}$. Chứng minh rằng với $\ell=1$, dãy bảng trùng dãy bảng của lặp giá trị đồng bộ từ $V_0=0$, biết $\hat r(s,a)=1$ với mọi cặp, và nêu số vòng dự kiến của phiên bản $\ell=1$, biết lặp giá trị cần $736$ lượt quét trong lần chạy đã nhúng.
- (e) Một cách khác giảm chi phí là cập nhật tại chỗ. Trên mô hình hai trạng thái, chạy hai lượt quét của lặp giá trị tại chỗ (mỗi ô gán $V(s)\leftarrow(T_*V)(s)$ và ô sau đọc ngay giá trị mới) từ $V=(0,0)$, lần lượt với thứ tự $\mathrm s_0,\mathrm s_1$ và thứ tự $\mathrm s_1,\mathrm s_0$. So với hai lượt quét đồng bộ $(1,3)$, $(2{,}7;\,5{,}7)$ và giải thích vì sao thứ tự có ảnh hưởng.
:::

::: hint Gợi ý Bài tập 04.15
Với $\pi_V$ tham lam theo $V$, $T_{\pi_V}V=T_*V$ (đoạn sau Định nghĩa 04.22 của ghi chú). Ở vòng thứ nhất, $\pi=\pi_0$ chưa tham lam theo bảng nào. Ở (b), chặn của Hệ quả 04.27 là $\Delta_*(V)/(1-\gamma)$ và áp dụng cho mọi bảng $V$. Ở (d), notebook có sẵn `bellman_pi` cho bước (1), `lookahead` và `greedy_keep_ties` cho bước (2). Ở (e), nhánh $\mathrm b$ tại $\mathrm s_0$ đọc giá trị của $\mathrm s_1$.
:::

::: solution Lời giải Bài tập 04.15
**Câu (a).** Ba vòng đầu với $\ell=1$:

| Vòng | $\pi$ dùng ở bước (1) | $V$ sau bước (1) | $Q_V(\mathrm s_0,\cdot)$ | $Q_V(\mathrm s_1,\cdot)$ | $\pi_V$ | $\Delta_*(V)$ |
|---|---|---|---|---|---|---:|
| $1$ | $(\mathrm a,\mathrm a)$ | $(1,2)$ | $1{,}9$; $1{,}8$ | $2{,}9$; $4{,}8$ | $(\mathrm a,\mathrm b)$ | $2{,}8$ |
| $2$ | $(\mathrm a,\mathrm b)$ | $(1{,}9;\,4{,}8)$ | $2{,}71$; $4{,}32$ | $3{,}71$; $7{,}32$ | $(\mathrm b,\mathrm b)$ | $2{,}52$ |
| $3$ | $(\mathrm b,\mathrm b)$ | $(4{,}32;\,7{,}32)$ | $4{,}888$; $6{,}588$ | $5{,}888$; $9{,}588$ | $(\mathrm b,\mathrm b)$ | $2{,}268$ |

Chẳng hạn ở vòng 2: $V(\mathrm s_0)=1+0{,}9\cdot1=1{,}9$, $V(\mathrm s_1)=3+0{,}9\cdot2=4{,}8$; phần dư là $\max\{4{,}32-1{,}9;\ 7{,}32-4{,}8\}=2{,}52$. Từ vòng 2, chính sách dùng ở bước (1) là $\pi_V$ của bảng trước, nên bảng mới là $T_{\pi_V}V=T_*V$: $T_*(1,2)=(\max\{1{,}9;1{,}8\},\max\{2{,}9;4{,}8\})=(1{,}9;\,4{,}8)$ và $T_*(1{,}9;\,4{,}8)=(4{,}32;\,7{,}32)$. Vòng 1 khác lặp giá trị: $T_{\pi_0}(0,0)=(1,2)$, còn $T_*(0,0)=(1,3)$.

**Câu (b).** Ở vòng 3, $\pi_V=(\mathrm b,\mathrm b)=\pi$, nên phiên bản này dừng với $V=(4{,}32;\,7{,}32)$. Sai số thật là $\max\{27-4{,}32;\ 30-7{,}32\}=22{,}68$, và chặn của Hệ quả 04.27 là $2{,}268/(1-0{,}9)=22{,}68$, trùng sai số thật. Chính sách trả về là $(\mathrm b,\mathrm b)$, tối ưu theo Ví dụ 04.12 của ghi chú, nhưng nhãn dừng không chứng nhận điều đó: Định nghĩa 04.16 và Định lý 04.20 đòi kiểm tính ổn định bằng giá trị chính xác $v_\pi$, còn ở đây $V\ne v_{(\mathrm b,\mathrm b)}$. Bài tập 04.3 cho một trường hợp chính sách không đổi theo một bảng gần đúng mà không tối ưu. Mệnh đề 04.18 không áp dụng vì giả thiết "mỗi lần đánh giá trả đúng $v_\pi$" bị bỏ, nên Bước 1 của chứng minh (giá trị tăng nghiêm ngặt khi chính sách đổi) không còn căn cứ.

**Câu (c).** Một chương trình viết theo đúng bốn bước của đề cho:

| $\ell$ | Số vòng | Phép áp dụng toán tử | $V$ khi dừng |
|---:|---:|---:|---|
| $1$ | $55$ | $110$ | $\approx(26{,}905;\,29{,}905)$ |
| $5$ | $12$ | $72$ | $\approx(26{,}924;\,29{,}924)$ |
| $20$ | $4$ | $84$ | $\approx(26{,}964;\,29{,}964)$ |

Tăng $\ell$ làm giảm số vòng nhưng tăng chi phí mỗi vòng; trên mô hình này, tổng số phép nhỏ nhất ở $\ell=5$. Kết luận này thuộc về mô hình, ngưỡng và cách đếm đã cho: với $\ell=1$, bảng mà bước (1) của vòng sau tính ra chính là $T_*V$ đã có ở bước (2) của vòng trước, nên một cài đặt dùng lại kết quả đó chỉ tốn một phép mỗi vòng. Ở cả ba dòng, sai số của $V$ so với $v_*=(27,30)$ không vượt $0{,}1=\theta/(1-\gamma)$, như Hệ quả 04.27 bảo đảm.

**Câu (d).** Với $V=0$ và $\hat r=1$, $(T_{\pi_0}0)(s)=1=(T_*0)(s)$ tại mọi ô, nên bảng sau vòng 1 bằng $V_1$ của lặp giá trị. Giả sử bảng sau vòng $r$ bằng $V_r$. Bước (4) đặt $\pi=\pi_{V_r}$, nên bảng sau vòng $r+1$ là $T_{\pi_{V_r}}V_r=T_*V_r=V_{r+1}$. Quy nạp cho hai dãy trùng nhau, và phép kiểm $\Delta_*(V)\le\theta$ cũng trùng, nên phiên bản $\ell=1$ dừng sau $736$ vòng như lặp giá trị, trừ sai khác do làm tròn số thực. Một cài đặt dùng các hàm của notebook: ở mỗi vòng, gọi `V = bellman_pi(V, pi, P, R, gamma)` đúng $\ell$ lần, rồi `Q = lookahead(V, P, R, gamma)`, `delta = np.abs(Q.max(axis=1) - V).max()`; nếu `delta <= theta` thì dừng, nếu không thì `pi = greedy_keep_ties(Q, pi)`; mỗi vòng cộng $\ell+1$ vào bộ đếm phép. Với $\ell=5$ và $\ell=20$, notebook chưa nhúng kết quả; số vòng và số phép áp dụng toán tử là phần sinh viên đo và báo cáo, kèm sai số thật so với $v_*$ của lặp chính sách.

**Câu (e).** Mỗi ô lấy cực đại của nhánh $\mathrm a$ và nhánh $\mathrm b$, đọc giá trị mới nhất của bảng:

| Thứ tự | Lượt | Ô cập nhật trước | Ô cập nhật sau | Bảng $(\mathrm s_0,\mathrm s_1)$ |
|---|---|---|---|---|
| $\mathrm s_0,\mathrm s_1$ | $1$ | $\mathrm s_0$: $\max\{1+0;\ 0+0\}=1$ | $\mathrm s_1$: $\max\{2+0{,}9\cdot1;\ 3+0\}=3$ | $(1,3)$ |
| $\mathrm s_0,\mathrm s_1$ | $2$ | $\mathrm s_0$: $\max\{1+0{,}9;\ 0+0{,}9\cdot3\}=2{,}7$ | $\mathrm s_1$: $\max\{2+0{,}9\cdot2{,}7;\ 3+0{,}9\cdot3\}=5{,}7$ | $(2{,}7;\,5{,}7)$ |
| $\mathrm s_1,\mathrm s_0$ | $1$ | $\mathrm s_1$: $\max\{2+0;\ 3+0\}=3$ | $\mathrm s_0$: $\max\{1+0;\ 0+0{,}9\cdot3\}=2{,}7$ | $(2{,}7;\,3)$ |
| $\mathrm s_1,\mathrm s_0$ | $2$ | $\mathrm s_1$: $\max\{2+0{,}9\cdot2{,}7;\ 3+0{,}9\cdot3\}=5{,}7$ | $\mathrm s_0$: $\max\{1+0{,}9\cdot2{,}7;\ 0{,}9\cdot5{,}7\}=5{,}13$ | $(5{,}13;\,5{,}7)$ |

Thứ tự $\mathrm s_0,\mathrm s_1$ cho đúng hai bảng của lượt quét đồng bộ, $(1,3)$ rồi $(2{,}7;\,5{,}7)$; thứ tự $\mathrm s_1,\mathrm s_0$ cho $(2{,}7;\,3)$ rồi $(5{,}13;\,5{,}7)$. Phần thưởng $3$ nằm ở $\mathrm s_1$, và nhánh tốt tại $\mathrm s_0$ là $\mathrm b$, nhánh đọc giá trị của $\mathrm s_1$. Cập nhật $\mathrm s_1$ trước cho $\mathrm s_0$ đọc ngay giá trị mới trong cùng lượt quét; theo thứ tự ngược lại, $\mathrm s_0$ đọc giá trị cũ của $\mathrm s_1$ như lượt quét đồng bộ. Sau hai lượt, sai số so với $v_*=(27,30)$ là $(24{,}3;\,24{,}3)$ với lượt quét đồng bộ và $(21{,}87;\,24{,}3)$ với thứ tự $\mathrm s_1,\mathrm s_0$: nhỏ hơn tại $\mathrm s_0$, cùng sai số lớn nhất. Cả hai thứ tự lặp lại mãi đều cập nhật mỗi trạng thái vô hạn lần, nên đều hội tụ theo Định lý 04.32; thứ tự chỉ đổi tốc độ, như Ví dụ 04.16 của ghi chú trên dãy năm ô.

**Kiểm tra lại.** Với $\ell\to\infty$, bước (1) cho $V=v_\pi$ và thuật toán trở về lặp chính sách; với $\ell=1$, nó trùng lặp giá trị từ vòng thứ hai, như mục Đọc thêm của ghi chú nêu. Bốn lỗi thường gặp: khởi động lại $V\leftarrow0$ ở mỗi vòng thay vì dùng bảng của vòng trước, khi đó bảng sau bước (1) luôn là $T_\pi^{\ell}0$, có sai số $\gamma^\ell\lVert v_\pi\rVert_\infty$ không giảm theo vòng; trên mô hình hai trạng thái, khi chính sách đã là $(\mathrm b,\mathrm b)$, phần dư đứng yên ở $2{,}7$ với $\ell=1$ (bảng $(0,3)$), $1{,}771$ với $\ell=5$ và $0{,}365$ với $\ell=20$, nên không bao giờ xuống dưới $\theta=0{,}01$, và phải có $\ell\ge55$ thuật toán mới dừng; chỉ đếm $\ell$ lần $T_\pi$ mà bỏ lần tính $Q_V$, làm phiên bản $\ell=1$ có vẻ rẻ gấp đôi; dùng nhãn "chính sách không đổi" làm chứng nhận tối ưu như ở câu (b); ở câu (e), cho $\mathrm s_0$ đọc giá trị cũ của $\mathrm s_1$ dù $\mathrm s_1$ vừa được cập nhật, cho lại $(1,3)$ của lượt quét đồng bộ thay cho $(2{,}7;\,3)$.
:::

### Bài tập 04.6. Chứng nhận nghiệm tối ưu

**Mức độ:** vận dụng (bài tổng hợp). Mục tiêu học tập 4, 5 của ghi chú.

**Nguồn:** Bài giảng gốc (2025–2026), trang 17–19, 31–38; ghi chú bài giảng, Bài tập 04.6.

**Trùng trang chiếu:** [Bài tập: chứng nhận nghiệm tối ưu](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/7/6) và [trang lời giải](lecture-04-giai-mdp-bang-quy-hoach-dong.html#/7/7).

::: exercise Bài tập 04.6 (Chứng nhận nghiệm tối ưu)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$; và hai bảng $U=(10,30)$, giá trị chính xác của $\pi_1=(\mathrm a,\mathrm b)$, và $V=(27,30)$.

- (a) Tính $T_*U$, $T_*V$, $\Delta_*(U)$, $\Delta_*(V)$ và hai chính sách tham lam.
- (b) Xác định bảng nào là $v_*$ và nêu kết quả của ghi chú được dùng làm căn cứ.
- (c) So chặn sai số của $U$ theo Hệ quả 04.27 với sai số thật của $U$.
- (d) Giả sử chỉ có một bộ mô phỏng nhận $(s,a)$ và trả một chuyển $(s',r)$. Xác định phép tính ở (a) không thực hiện được trực tiếp.
:::

::: hint Gợi ý Bài tập 04.6
Mỗi thành phần của $T_*U$ là cực đại của hai giá trị nhìn trước; dùng bảng $U$ cho mọi giá trị tiếp nối.
:::

::: solution Lời giải Bài tập 04.6
**Câu (a).** Với $U$: tại $\mathrm s_0$, $\max\{1+0{,}9\cdot10;\ 0+0{,}9\cdot30\}=\max\{10;\,27\}=27$; tại $\mathrm s_1$, $\max\{2+0{,}9\cdot10;\ 3+0{,}9\cdot30\}=\max\{11;\,30\}=30$. Vậy $T_*U=(27,30)$, $\Delta_*(U)=\max\{17;\,0\}=17$, chính sách tham lam $(\mathrm b,\mathrm b)$. Với $V$: các giá trị nhìn trước là $25{,}3$; $27$ tại $\mathrm s_0$ và $26{,}3$; $30$ tại $\mathrm s_1$, nên $T_*V=V$, $\Delta_*(V)=0$, chính sách tham lam $(\mathrm b,\mathrm b)$.

**Câu (b).** $V=v_*$, vì $V$ là điểm bất động của $T_*$ và theo Định lý 04.25(a) điểm bất động đó duy nhất và bằng $v_*$; các giả thiết MDP hữu hạn có tính Markov, phần thưởng bị chặn và $\gamma=0{,}9<1$ đều thỏa. Bảng $U$ là giá trị chính xác của một chính sách nhưng không thỏa phương trình Bellman tối ưu.

**Câu (c).** Chặn là $17/(1-0{,}9)=170$, còn sai số thật là $\lVert U-v_*\rVert_\infty=\max\{17;\,0\}=17$. Chặn đúng nhưng lớn gấp mười lần sai số thật.

**Câu (d).** Phép tính kỳ vọng đầy đủ $\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma U(s')\bigr]$ cần biết $p$. Bộ mô phỏng chỉ cho từng mẫu; muốn dùng nó phải ước lượng mô hình như CartPole rời rạc hóa (Ví dụ 04.17 của ghi chú) hoặc dùng các phương pháp lấy mẫu của Bài 05.

**Kiểm tra lại.** Theo Định lý 04.13, chính sách tham lam theo $v_{\pi_1}=U$ không kém $\pi_1$; ở đây nó là $(\mathrm b,\mathrm b)$ với giá trị $(27,30)\ge(10,30)$. Hai lỗi thường gặp: kết luận $U$ tối ưu vì $U$ là giá trị chính xác của một chính sách, trong khi phải kiểm $U=T_*U$; đọc chặn $170$ là sai số, trong khi chặn chỉ là cận trên và ở đây gấp mười lần sai số thật.
:::

## Tài liệu tham khảo

- Tạ Việt Cường, Bài giảng gốc Bài 04: Giải MDP (2025–2026): trang 5, 17–18 cho Bài tập 04.16; trang 14, 17–18 cho Bài tập 04.1; trang 17–20 cho Bài tập 04.2, 04.3; trang 25–28 cho Bài tập 04.4; trang 15 cho Bài tập 04.5; trang 17–19, 31–38 cho Bài tập 04.6.
- Tạ Việt Cường, Bài tập tuần 3 (2025–2026), "Giải bài toán MDP": bài 6 cho Bài tập 04.10, bài 7 cho Bài tập 04.11, bài 9 cho Bài tập 04.12.
- Tạ Việt Cường, Bài tập tuần 4 (2025–2026), "Đánh giá chính sách": bài 1 cho mô hình hai trạng thái, bài 10 cho Bài tập 04.13.
- Ghi chú bài giảng Bài 04 ([mở trong viewer](material-viewer.html?doc=materials/lec-04/lecture-note.md&deck=lecture-04-giai-mdp-bang-quy-hoach-dong.html)): Bài tập 04.1–04.6 giữ nguyên đề và kết quả; số liệu của chính sách ngẫu nhiên đều trong Bài tập 04.10, 04.17 là số liệu sư phạm tự xây dựng.
- Bài thực hành CartPole của Bài 04 (`thuc-hanh-cartpole-quy-hoach-dong.ipynb`): mục 7.3–7.4 và nhiệm vụ 5, 7 cho Bài tập 04.14, 04.15; số liệu từ một lần chạy đã nhúng (gymnasium 1.3.0).
- Sutton, R. S., và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, chương 4: §4.3, tr. 80–82 cho Bài tập 04.3; §4.5, tr. 85–86 cho Bài tập 04.5.
- Puterman, M. L. (1994), *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley, §6.5 (lặp chính sách cải biên) cho Bài tập 04.15.
