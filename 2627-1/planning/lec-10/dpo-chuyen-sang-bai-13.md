# Phần DPO cắt khỏi Bài 10, chuyển sang Bài 13

Tác giả 2026-11-21 (`tong-hop-gop-y-2026-11-21.md` mục 3a; `gop-y-tac-gia-deck-2026-11-20.md` mục #27): "Bỏ luôn khỏi ghi chú"; học tăng cường từ phản hồi con người và DPO sẽ trình bày ở Bài 13. Tệp này lưu nguyên văn mọi đoạn đã cắt khỏi `2627-1/materials/lec-10/lecture-note.md` và `exercises.md` (bản ở commit `67bcbd6`, trước lượt sửa 2026-11-21), kèm tiêu đề nguồn và số dòng cũ, để dùng lại khi dựng Bài 13.

Lưu ý khi dùng lại:

- Số hiệu khối 10.52–10.70, Ví dụ 10.23–10.28, Tình huống 10.4–10.5, Bài tập 10.18–10.21 là số của Bài 10 cũ; Bài 13 đánh lại theo bộ đếm của bài đó.
- Mục 7 dùng các kết quả của Bài 10 (Định nghĩa 10.21, 10.23, Mệnh đề 10.24, Định nghĩa 10.39, 10.43, Thuật toán 10.49, Ví dụ 10.17) và giả thiết người đọc đã có kiến thức tiên quyết về hồi quy logistic và mô hình ngôn ngữ tự hồi quy (đoạn dòng 43 dưới đây).
- Hình `img/lec-10/central-problem.svg` còn hàng thứ ba (RLHF với PPO, DPO, phạt KL theo $\pi_{\mathrm{ref}}$); ghi chú Bài 10 sau lượt sửa chỉ đọc hai hàng đầu.
- Bài tập 10.22 của `exercises.md` (Sutton và Barto, Bài tập 2.9) được giữ trong Bài 10 với số hiệu mới 10.18; chỉ đoạn "Liên hệ với mô hình Bradley–Terry" và câu kiểm tra nhắc Ví dụ 10.23 bị thay. Bản cũ lưu đầy đủ dưới đây.

## `lecture-note.md`, dòng 1: Tiêu đề chương

````markdown
# Bài 10 — TRPO, PPO và DPO
````

## `lecture-note.md`, dòng 14–15: Mục tiêu học tập, mục tiêu 8 và 9

````markdown
8. **Phần thưởng từ dữ liệu ưu tiên và mục tiêu có phạt KL.** Ước lượng *mô hình phần thưởng* (reward model) từ *dữ liệu ưu tiên* (preference data) theo mô hình Bradley–Terry bằng hợp lý cực đại; chứng minh nghiệm dạng đóng của *mục tiêu có phạt KL* (KL-regularized objective) theo một *chính sách tham chiếu* (reference policy, reference model) cố định; mô tả ba giai đoạn của *học tăng cường từ phản hồi con người* (reinforcement learning from human feedback, RLHF) với PPO; phân biệt chính sách cũ của PPO với chính sách tham chiếu.
9. **Tối ưu ưu tiên trực tiếp.** Suy ra hàm mất mát của *tối ưu ưu tiên trực tiếp* (Direct Preference Optimization, DPO) bằng phép đổi biến giữa phần thưởng và chính sách; tính bằng tay một bước DPO; phát biểu các giả thiết để DPO và RLHF cho cùng chính sách tối ưu, và nêu hậu quả khi một giả thiết không thỏa.
````

## `lecture-note.md`, dòng 20: Kiến thức tiên quyết, câu mở (nhắc Bài tập 10.22)

````markdown
Số hiệu `03.k`, …, `09.k` chỉ khối trong ghi chú Bài 03–09. Bài tập 10.13–10.17 và 10.22 thuộc tệp bài tập `exercises.md` của Bài 10.
````

## `lecture-note.md`, dòng 43: Kiến thức tiên quyết, mục "Hồi quy logistic và mô hình ngôn ngữ tự hồi quy"

````markdown
- **Hồi quy logistic và mô hình ngôn ngữ tự hồi quy** (kiến thức học máy và học sâu). Với $\sigma(z)=1/(1+e^{-z})$, hồi quy logistic cực tiểu hóa trung bình của $-\log\sigma(z_i)$ trên các mẫu nhãn dương, với $\sigma'(z)=\sigma(z)\sigma(-z)$ và $1-\sigma(z)=\sigma(-z)$. Mô hình ngôn ngữ tự hồi quy gán cho chuỗi token $y=(A_0,\dots,A_{T-1})$ sau lời nhắc $x$ xác suất $\prod_t\pi(A_t\mid x,A_0,\dots,A_{t-1})$.
````

## `lecture-note.md`, dòng 74: Bảng ký hiệu, dòng $\epsilon$, $\beta$, $c_1$, $c_2$ (nhắc $\pi_{\mathrm{ref}}$ ở Mục 7)

````markdown
| $\epsilon$, $\beta$, $c_1$, $c_2$ | bán kính cắt; hệ số phạt KL (theo $\pi_{\mathrm{old}}$ ở Mục 6.2, theo $\pi_{\mathrm{ref}}$ ở Mục 7); hai trọng số mất mát | $(0,1)$; $(0,\infty)$; $[0,\infty)$ |
````

## `lecture-note.md`, dòng 77–84: Bảng ký hiệu, các dòng của Mục 7

````markdown
| $x$, $\mathcal X$; $y$, $\mathcal Y(x)$; $\mathcal V$ | lời nhắc, tập lời nhắc; câu trả lời, tập câu trả lời cho $x$; tập token (Mục 7) | $\mathcal Y(x)$, $\mathcal V$ hữu hạn |
| $\pi_{\mathrm{ref}}$, $\theta_{\mathrm{ref}}$ | chính sách tham chiếu, cố định trong cả Mục 7; tham số của nó | phân phối trên $\mathcal Y(x)$ với mỗi $x$ |
| $y_w$, $y_l$; $\mathcal D_{\mathrm{pref}}$, $\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}$ | câu trả lời được chọn, bị loại trong một phép so sánh; tập dữ liệu ưu tiên, trung bình đều trên nó | bộ ba $(x,y_w,y_l)$ |
| $\sigma$ | hàm logistic $\sigma(z)=1/(1+e^{-z})$ | $\mathbb R\to(0,1)$ |
| $r(x,y)$, $\hat r(x,y)$ | phần thưởng chưa biết sinh ra các phép so sánh, tức $r(s,a)$ với $s=x$, $a=y$; mô hình phần thưởng học được | $\mathbb R$ |
| $J_\beta$, $\pi^*_r$, $\mathcal Z_r(x)$ | mục tiêu có phạt KL; nghiệm của nó với phần thưởng $r$; hàm phân hoạch | $\mathbb R$; phân phối; $(0,\infty)$ |
| $r_\theta$, $\Delta r_\theta$; $\tilde r_\theta$ | phần thưởng ngầm định $\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$ và hiệu của nó giữa $y_w$ và $y_l$; phần thưởng đã trừ KL $r-r_\theta$ | $\mathbb R$ |
| $L^{\mathrm{BT}}$, $L^{\mathrm{DPO}}$ | mất mát Bradley–Terry của mô hình phần thưởng; mất mát DPO (đều được cực tiểu hóa) | $[0,\infty)$ |
````

## `lecture-note.md`, dòng 94–95: Quy ước đọc bảng, hai gạch đầu dòng về $n$, $k$, $x$, $y$ ở Mục 7

````markdown
  - $n$ là số trạng thái, số bước của lợi tức $n$ bước, và là hình chiếu trong chứng minh Mệnh đề 10.34; ở Mục 7, Tình huống 10.5 và Bài tập 10.19, $n$ là số phép so sánh và $k$ là số phép chọn $y_1$;
  - $x_k$, $y_k$ là bước lặp và tích $Fp_k$ của Thuật toán 10.36, $x$ trong $\langle x,f\rangle$ là vector của chứng minh Định lý 10.26, $\sigma(x)$ ở Ví dụ 10.2 có biến $x$ thực, và $y_t$ là mục tiêu $V^{\mathrm{targ}}_t$ ở Định nghĩa 10.47; ngoài các chỗ đó, $x$ và $y$ là lời nhắc và câu trả lời của Mục 7;
````

## `lecture-note.md`, dòng 101: Quy ước đọc bảng, ký hiệu của các bài báo ở Mục 7

````markdown
- Ký hiệu của các bài báo ở Mục 7: $r^*$, $r_\phi$, $\hat r_\theta$, $Z(x)$, $\mathcal D$, $\mathcal L_R$, $\mathcal L_{\mathrm{DPO}}$, $\pi_r$ của Rafailov và cộng sự (2023) là $r$, $\hat r$, $r_\theta$, $\mathcal Z_r(x)$, $\mathcal D_{\mathrm{pref}}$, $L^{\mathrm{BT}}$, $L^{\mathrm{DPO}}$, $\pi^*_r$; ở đây dấu mũ chỉ mô hình phần thưởng, không chỉ phần thưởng ngầm định. Ouyang và cộng sự (2022) viết mô hình phần thưởng là $r_\theta$ và chính sách là $\pi^{\mathrm{RL}}_\phi$; Ziegler và cộng sự (2019) viết mô hình ban đầu là $\rho$; Gheshlaghi Azar và cộng sự (2024) viết hệ số KL là $\tau$.
````

## `lecture-note.md`, dòng 178–182: §1.1, bài toán trung tâm, hình cấu trúc chương và đoạn đọc hình (hàng thứ ba của hình là Mục 7)

````markdown
Hai giới hạn này dẫn tới **bài toán trung tâm của chương**: giảm phương sai của ước lượng gradient mà vẫn giữ kỳ vọng của nó, và dùng lại dữ liệu của $\pi_{\mathrm{old}}$ để chọn một bước cập nhật lớn mà chính sách mới không kém chính sách cũ. Khi phần thưởng chỉ được biết qua các phép so sánh ưu tiên, bài toán có thêm phần thứ ba: tìm chính sách cực đại hóa phần thưởng mà vẫn ở gần một chính sách tham chiếu cố định.

![Ba hàng khung nối bằng mũi tên. Hàng trên, viền liền, nhãn phương sai của ước lượng gradient: khung đường cơ sở và critic, với G t trừ v mũ của S t và sai số TD delta t (Mục 2), dẫn tới khung GAE, A mũ t bằng tổng theo k của (gamma lambda) mũ k nhân delta t cộng k (Mục 3). Hàng dưới, viền nét đứt, nhãn độ lớn bước cập nhật: khung hàm thay thế và chặn cải thiện (Mục 4), dẫn tới khung TRPO, KL trung bình không vượt kappa (Mục 5), rồi khung PPO, cắt tỉ số rho t vào đoạn từ 1 trừ epsilon đến 1 cộng epsilon (Mục 6). Hai hàng gặp nhau ở khung cuối, viền đậm: Thuật toán 10.49, PPO kiểu actor–critic, GAE cho lợi thế và mục tiêu cắt cho chính sách. Hàng thứ ba, viền chấm, nhãn phần thưởng từ so sánh ưu tiên: một mũi tên đi xuống từ khung PPO tới khung RLHF với PPO, DPO, phạt KL theo pi ref cố định (Mục 7).](img/lec-10/central-problem.svg)

Trên hình, các mục xếp thành ba hàng, mỗi hàng trả lời một phần của bài toán trung tâm. Hàng trên giảm phương sai: ở Mục 2, chúng ta trừ đường cơ sở và bootstrap từ một hàm giá trị học được; ở Mục 3, chúng ta trộn các ước lượng nhiều bước thành GAE. Hàng dưới giới hạn bước cập nhật: ở Mục 4, chúng ta chặn mức thay đổi của $J$ theo khoảng cách giữa hai chính sách; ở Mục 5, chúng ta giải bài toán có ràng buộc KL; ở Mục 6, chúng ta thay ràng buộc bằng phép cắt tỉ số. Hai hàng đầu gặp nhau ở thuật toán PPO, nơi lợi thế ước lượng bằng GAE đi vào mục tiêu cắt. Hàng thứ ba nhận PPO làm công cụ: ở Mục 7, chúng ta học phần thưởng từ các phép so sánh, phạt KL theo một chính sách tham chiếu cố định, rồi giải bài toán đó bằng PPO hoặc bằng DPO.
````

## `lecture-note.md`, dòng 2096: §6.6, đoạn cuối dẫn sang Mục 7

````markdown
Thuật toán 10.49 cần phần thưởng $R_{t+1}$ do môi trường trả về sau mỗi hành động, và phạt KL của PPO-Penalty (Định nghĩa 10.43) chỉ giữ mỗi bước gần chính sách $\pi_{\mathrm{old}}$ vừa sinh dữ liệu. Khi môi trường không trả phần thưởng mà chỉ có người so sánh hai kết quả, các công cụ của Mục 2–6 không dùng trực tiếp được, và chưa có gì giữ chính sách cuối gần một chính sách cho trước.
````

## `lecture-note.md`, dòng 2100–2553: §7 "Tối ưu chính sách từ phản hồi ưu tiên" (7.1–7.6), nguyên văn

````markdown
## 7. Tối ưu chính sách từ phản hồi ưu tiên

<!-- note-topic-id: lec-10-topic-25 -->
### 7.1 Dữ liệu ưu tiên và mô hình Bradley–Terry

Giả sử một mô hình ngôn ngữ nhận một *lời nhắc* (prompt) $x$ và đáp bằng một trong hai *câu trả lời* (response, completion) $y_1$, $y_2$, với xác suất $(\tfrac23;\,\tfrac13)$; gọi mô hình hiện có này là *chính sách tham chiếu* $\pi_{\mathrm{ref}}$. Không có hàm phần thưởng, chỉ có sáu lần người gán nhãn đọc hai câu trả lời và chọn câu tốt hơn, bốn lần chọn $y_1$, hai lần chọn $y_2$.

**Câu hỏi.** Từ sáu phép so sánh này, chính sách mới nên chọn mỗi câu trả lời với xác suất nào nếu vẫn phải gần chính sách tham chiếu, và có cần một vòng học tăng cường để tìm chính sách đó không?

::: definition Định nghĩa 10.52 (Bài toán sinh câu trả lời)
Cho tập lời nhắc hữu hạn $\mathcal X$ với phân phối $\mu_0$, và với mỗi $x$ một tập câu trả lời hữu hạn $\mathcal Y(x)$.

- (a) *Dạng một bước.* Trạng thái đầu $x\sim\mu_0$; hành động là câu trả lời $y\in\mathcal Y(x)$, chọn theo $\pi(y\mid x)$; lượt kết thúc sau hành động đó với phần thưởng $r(x,y)$. Đây là bài toán một bước của Ví dụ 10.1 với $s=x$, $a=y$.
- (b) *Dạng mức token* (token-level MDP). Với tập token hữu hạn $\mathcal V$ có một ký hiệu kết thúc: $S_0=x$; hành động $A_t\in\mathcal V$; chuyển tất định $S_{t+1}=(S_t,A_t)$, chuỗi đã có ghép thêm token mới; lượt kết thúc, $Z_{t+1}=1$, khi $A_t$ là ký hiệu kết thúc hoặc $t+1=T_{\max}$; vì $T_{\max}$ thuộc bài toán và $S_t$ chứa độ dài chuỗi, đây là kết thúc, không phải cắt ngắn. Câu trả lời $y=(A_0,\dots,A_{T-1})$ có xác suất $\pi(y\mid x)=\prod_{t=0}^{T-1}\pi(A_t\mid S_t)$; phần thưởng chỉ ở bước cuối, $R_T=r(x,y)$, các $R_{t+1}$ khác bằng $0$; $\gamma=1$.
:::

Với $\gamma=1$, lợi tức $G_0$ của dạng (b) bằng $r(x,y)$, nên hai dạng có cùng hàm mục tiêu và chỉ khác cách đếm bước. Tập $\mathcal Y(x)$ của dạng (b) có tới $\lvert\mathcal V\rvert^{T_{\max}}$ phần tử.

::: example Ví dụ 10.23 (Dữ liệu ưu tiên trên bài toán một bước)
**Dữ kiện.** Lời nhắc $x$, hai câu trả lời; $\pi_{\mathrm{ref}}$ là chính sách softmax của Ví dụ 10.1 với $\theta_{\mathrm{ref}}=(\log2;\,0)$, tức $(\tfrac23;\,\tfrac13)$. Mỗi phép so sánh là một bộ ba (lời nhắc, câu được chọn, câu bị loại):

- phép 1: $(x,y_1,y_2)$;
- phép 2: $(x,y_1,y_2)$;
- phép 3: $(x,y_1,y_2)$;
- phép 4: $(x,y_1,y_2)$;
- phép 5: $(x,y_2,y_1)$;
- phép 6: $(x,y_2,y_1)$.

**Tần suất.** $y_1$ được chọn $4$ trên $6$ lần, tức $\tfrac23$.
:::

Một cách trực quan, người gán nhãn chọn câu có phần thưởng cao hơn thường xuyên hơn, và chọn gần như ngẫu nhiên khi hai phần thưởng gần nhau; xác suất chọn chỉ phụ thuộc hiệu hai phần thưởng.

::: definition Định nghĩa 10.53 (Dữ liệu ưu tiên, mô hình Bradley–Terry)
Một *phép so sánh ưu tiên* (pairwise comparison) là bộ ba $(x,y_w,y_l)$, $y_w\ne y_l$ trong $\mathcal Y(x)$, với *câu trả lời được chọn* $y_w$ và *câu trả lời bị loại* $y_l$ (chosen, rejected). *Tập dữ liệu ưu tiên* $\mathcal D_{\mathrm{pref}}$ là một tập hữu hạn các bộ ba. Với hàm phần thưởng $r$ trên các cặp $(x,y)$, *mô hình Bradley–Terry* giả thiết các phép so sánh độc lập và
$$\begin{aligned}&\Pr(y\succ y'\mid x)\\&\quad=\frac{e^{r(x,y)}}{e^{r(x,y)}+e^{r(x,y')}}\\&\quad=\sigma\bigl(r(x,y)-r(x,y')\bigr).\end{aligned}$$
Hai hàm phần thưởng *tương đương* nếu chúng hơn kém nhau một hàm $f(x)$ chỉ phụ thuộc lời nhắc; *lớp tương đương* của $r$ là $[r]=\{r+f:\ f\text{ chỉ phụ thuộc }x\}$.
:::

Chỉ hiệu $r(x,y)-r(x,y')$ xuất hiện, nên mọi phần thưởng trong $[r]$ cho cùng xác suất ưu tiên (Rafailov và cộng sự, 2023, Bổ đề 1).

::: proposition Mệnh đề 10.54 (Hợp lý cực đại của mô hình phần thưởng)
**Giả thiết.** $\mathcal D_{\mathrm{pref}}$ hữu hạn, các bộ ba độc lập và sinh theo Định nghĩa 10.53; *mô hình phần thưởng* $\hat r$ là một hàm thực tùy ý trên các cặp $(x,y)$.

**Kết luận.**

- (a) Đối log-hợp lý trung bình của $\mathcal D_{\mathrm{pref}}$ dưới $\hat r$ là
  $$\begin{aligned}&L^{\mathrm{BT}}(\hat r)\\&\quad=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\bigl[\log\sigma\bigl(\\&\qquad\hat r(x,y_w)-\hat r(x,y_l)\bigr)\bigr],\end{aligned}$$
  mất mát của hồi quy logistic với biến $\hat r(x,y_w)-\hat r(x,y_l)$ và mọi nhãn dương.
- (b) $L^{\mathrm{BT}}(\hat r+f)=L^{\mathrm{BT}}(\hat r)$ với mọi $f$ chỉ phụ thuộc $x$.
- (c) Với một lời nhắc, hai câu trả lời và $n$ phép so sánh, $k$ phép chọn $y_1$, đặt $\Delta\hat r=\hat r(x,y_1)-\hat r(x,y_2)$. Nếu $0<k<n$, $L^{\mathrm{BT}}$ đạt cực tiểu khi và chỉ khi $\Delta\hat r=\log\frac k{n-k}$, tức $\sigma(\Delta\hat r)=\frac kn$. Nếu $k=n$ (tương tự $k=0$), $L^{\mathrm{BT}}>0$ với mọi $\hat r$ và giảm về $0$ khi $\Delta\hat r\to+\infty$, nên không có cực tiểu.

**Điều kiện áp dụng.** Cực tiểu lấy trên mọi hàm $\hat r$, không trong một lớp tham số.

**Phạm vi.** Mệnh đề chỉ ràng buộc hiệu phần thưởng trong từng phép so sánh, không nói gì về câu trả lời vắng mặt trong $\mathcal D_{\mathrm{pref}}$.
:::

::: proof
**Bước 1 (kết luận a, b).** Bộ ba $(x,y_w,y_l)$ có xác suất $\sigma\bigl(\hat r(x,y_w)-\hat r(x,y_l)\bigr)$; các bộ ba độc lập, nên log-hợp lý là tổng các logarit đó; chia cho số bộ ba và đổi dấu được (a). Mỗi số hạng chỉ chứa một hiệu, trong đó $f(x)$ triệt tiêu: đó là (b).

**Bước 2 (kết luận c).** $L^{\mathrm{BT}}=-\frac1n\bigl[k\log\sigma(\Delta\hat r)+(n-k)\log\sigma(-\Delta\hat r)\bigr]$. Từ $\sigma'(z)=\sigma(z)\sigma(-z)$ và $\sigma(-z)=1-\sigma(z)$,
$$\begin{aligned}&\frac{dL^{\mathrm{BT}}}{d\Delta\hat r}\\&\quad=-\frac1n\bigl[k\,\sigma(-\Delta\hat r)\\&\qquad-(n-k)\,\sigma(\Delta\hat r)\bigr]\\&\quad=\sigma(\Delta\hat r)-\frac kn ,\end{aligned}$$
tăng ngặt, nên $L^{\mathrm{BT}}$ lồi ngặt theo $\Delta\hat r$. Với $0<k<n$, đạo hàm bằng $0$ tại đúng $\sigma(\Delta\hat r)=\frac kn$. Với $k=n$, $L^{\mathrm{BT}}=-\log\sigma(\Delta\hat r)>0$, đạo hàm âm ở mọi điểm, và $L^{\mathrm{BT}}\to0$ khi $\Delta\hat r\to+\infty$. $\square$
:::

Trường hợp $k=n$ là *ưu tiên tất định* (deterministic preference): hợp lý cực đại đòi hiệu phần thưởng vô hạn (Gheshlaghi Azar và cộng sự, 2024, §4.2). Với một lớp tham số dùng chung tham số cho nhiều cặp, $\log\frac k{n-k}$ có thể không đạt được ở mọi cặp cùng lúc.

::: example Ví dụ 10.24 (Khớp mô hình phần thưởng)
**Dữ kiện.** Sáu phép so sánh của Ví dụ 10.23: $n=6$, $k=4$.

**Tính.** $L^{\mathrm{BT}}=-\tfrac16\bigl[4\log\sigma(\Delta\hat r)+2\log\sigma(-\Delta\hat r)\bigr]$. Khi hai câu trả lời có cùng phần thưởng, $L^{\mathrm{BT}}=\log2=0{,}6931$. Theo Mệnh đề 10.54(c), cực tiểu đạt tại $\Delta\hat r=\log\frac42=\log2$, với giá trị $-\tfrac23\log\tfrac23-\tfrac13\log\tfrac13=0{,}6365$. Mệnh đề 10.54(b) cho phép chọn $\hat r(x,y_2)=0$, nên $\hat r=(\log2;\,0)$.

**Kiểm tra lại.** $\sigma(\log2)=1/(1+\tfrac12)=\tfrac23$, đúng tần suất chọn $y_1$.
:::

::: remark Nhận xét 10.55 (Thu thập và chuẩn hóa dữ liệu ưu tiên)
1. Ouyang và cộng sự (2022, §3.5) cho người gán nhãn xếp hạng từ 4 đến 9 câu trả lời của một lời nhắc, và mọi cặp trong đó thành một phép so sánh.
2. Vì dữ liệu chỉ xác định $\hat r$ tới một hàm của $x$, các bài báo chuẩn hóa $\hat r$ về trung bình $0$ trên một tập câu trả lời chọn trước (Ouyang và cộng sự, 2022, §3.5; Stiennon và cộng sự, 2020, §3.4; Ziegler và cộng sự, 2019, §2).
3. Nhầm lẫn thường gặp: coi $\hat r(x,y)$ là điểm tuyệt đối, trong khi dữ liệu chỉ xác định hiệu $\hat r(x,y)-\hat r(x,y')$ trong cùng một lời nhắc.
:::

Mệnh đề 10.54 cho phần thưởng $\hat r=(\log2;\,0)$, khớp trên các câu trả lời có trong dữ liệu, nhưng chưa cho chính sách.

<!-- note-topic-id: lec-10-topic-26 -->
### 7.2 Mục tiêu có phạt KL theo chính sách tham chiếu

Với $\hat r=(\log2;\,0)$, chính sách cực đại hóa $\mathbb E_{y\sim\pi}\hat r(x,y)$ là $(1;\,0)$: nó bỏ hẳn $y_2$, và với mô hình ngôn ngữ nó có thể sinh câu trả lời khác xa các câu mà $\hat r$ đã được khớp (Stiennon và cộng sự, 2020, §3.4). Một cách trực quan, chính sách mới trả một chi phí $\beta$ cho mỗi đơn vị KL rời khỏi chính sách tham chiếu và chỉ đi xa khi phần thưởng bù được chi phí.

::: example Ví dụ 10.25 (Ba chính sách trên bài toán một bước)
**Dữ kiện.** $\pi_{\mathrm{ref}}(\cdot\mid x)=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$, $\beta=1$. Với $p=\pi(y_1\mid x)$, phần thưởng kỳ vọng trừ $\beta$ lần KL là
$$\begin{aligned}&J_1(p)=p\log2-p\log\frac{p}{2/3}\\&\quad-(1-p)\log\frac{1-p}{1/3}.\end{aligned}$$

**Tính.**

| Chính sách | $\mathbb E_\pi\hat r$ | $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ | $J_1$ |
|---|---|---|---|
| $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ | $0{,}4621$ | $0$ | $0{,}4621$ |
| tham lam $(1;\,0)$ | $0{,}6931$ | $\log\tfrac32=0{,}4055$ | $0{,}2877$ |
| $(0{,}8;\,0{,}2)$ | $0{,}5545$ | $0{,}0437$ | $0{,}5108$ |

**Diễn giải.** Chính sách tham lam có phần thưởng kỳ vọng và chi phí KL lớn nhất; $(0{,}8;\,0{,}2)$ có $J_1$ lớn nhất.

**Kiểm tra lại.** $0{,}8\log1{,}2+0{,}2\log0{,}6=0{,}1459-0{,}1022=0{,}0437$, bằng $D_{\mathrm{KL}}(\pi'\Vert\pi)$ tại $s_B$ của Ví dụ 10.11 ở Mục 4.3.
:::

::: definition Định nghĩa 10.56 (Mục tiêu có phạt KL, chính sách tham chiếu)
Cho bài toán ở dạng (a) của Định nghĩa 10.52 với phần thưởng $r$, một *chính sách tham chiếu* $\pi_{\mathrm{ref}}(\cdot\mid x)$ cố định và $\beta>0$. *Mục tiêu có phạt KL theo chính sách tham chiếu* của chính sách $\pi$ là
$$\begin{aligned}&J_\beta(\pi)=\mathbb E_{x\sim\mu_0}\Bigl[\mathbb E_{y\sim\pi(\cdot\mid x)}r(x,y)\\&\quad-\beta D_{\mathrm{KL}}\bigl(\pi(\cdot\mid x)\\&\qquad\Vert\pi_{\mathrm{ref}}(\cdot\mid x)\bigr)\Bigr],\end{aligned}$$
với KL của Định nghĩa 10.23 trên $\mathcal Y(x)$.
:::

KL ở đây là $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$, kỳ vọng lấy theo chính sách đang tối ưu. Đây là (3) của Rafailov và cộng sự (2023), kỳ vọng theo $\pi$ của phần thưởng (2) của Ziegler và cộng sự (2019), và (2) của Ouyang và cộng sự (2022) khi hệ số của số hạng tiền huấn luyện bằng $0$.

::: theorem Định lý 10.57 (Nghiệm của mục tiêu có phạt KL)
**Giả thiết.** Với mỗi $x$, $\mathcal Y(x)$ hữu hạn và $\pi_{\mathrm{ref}}(\cdot\mid x)$ là phân phối trên $\mathcal Y(x)$; $r$ nhận giá trị thực; $\beta>0$; chính sách được chọn tự do cho mỗi $x$.

**Kết luận.** Đặt *hàm phân hoạch* (partition function) và chính sách
$$\begin{aligned}&\mathcal Z_r(x)=\sum_{y}\pi_{\mathrm{ref}}(y\mid x)\,e^{r(x,y)/\beta},\\&\pi^*_r(y\mid x)=\frac{\pi_{\mathrm{ref}}(y\mid x)\,e^{r(x,y)/\beta}}{\mathcal Z_r(x)}.\end{aligned}$$

- (a) Với mọi $x$ và mọi $\pi(\cdot\mid x)$ có $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})<\infty$,
  $$\begin{aligned}&\mathbb E_{y\sim\pi}r(x,y)\\&\quad-\beta D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})\\&\quad=\beta\log\mathcal Z_r(x)\\&\quad-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r).\end{aligned}$$
- (b) $\pi^*_r$ cực đại $J_\beta$, là nghiệm duy nhất tại mọi $x$ có $\mu_0(x)>0$, và $\max J_\beta=\mathbb E_{x\sim\mu_0}\beta\log\mathcal Z_r(x)$.
- (c) $r(x,y)-\beta\log\frac{\pi^*_r(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}=\beta\log\mathcal Z_r(x)$ với mọi $y$ có $\pi_{\mathrm{ref}}(y\mid x)>0$.
- (d) Miền hỗ trợ của $\pi^*_r(\cdot\mid x)$ là miền hỗ trợ của $\pi_{\mathrm{ref}}(\cdot\mid x)$.
- (e) $\pi^*_{r+f}=\pi^*_r$ với mọi $f$ chỉ phụ thuộc $x$.

**Điều kiện áp dụng.** Cực đại hóa riêng cho từng $x$; với lớp chính sách tham số, kết luận chỉ cho nghiệm khi $\pi^*_r$ thuộc lớp.

**Phạm vi.** Định lý cho dạng của nghiệm, không cho thuật toán tìm nghiệm khi không tính được $\mathcal Z_r(x)$.
:::

::: proof
Cố định $x$, viết $\pi=\pi(\cdot\mid x)$, $\mathcal Z=\mathcal Z_r(x)$.

**Bước 1 (viết lại log-tỉ số).** Vì KL hữu hạn, mọi $y$ có $\pi(y)>0$ cũng có $\pi_{\mathrm{ref}}(y)>0$ và $\pi^*_r(y)>0$. Từ $\pi^*_r/\pi_{\mathrm{ref}}=e^{r/\beta}/\mathcal Z$, với các $y$ đó $\log\frac{\pi(y)}{\pi_{\mathrm{ref}}(y)}-\frac{r(x,y)}\beta=\log\frac{\pi(y)}{\pi^*_r(y)}-\log\mathcal Z$.

**Bước 2 (kết luận a).** Nhân với $-\beta$ và lấy kỳ vọng theo $y\sim\pi$, một tổng hữu hạn.

**Bước 3 (kết luận b).** Theo (a) và Mệnh đề 10.24(a), biểu thức trong ngoặc của $J_\beta$ tại $x$ không vượt $\beta\log\mathcal Z_r(x)$, dấu bằng chỉ tại $\pi^*_r(\cdot\mid x)$; chính sách có KL vô hạn cho $-\infty$. Chính sách chọn tự do theo $x$, nên cực đại từng $x$ cho cực đại của $J_\beta$.

**Bước 4 (kết luận c, d, e).** Lấy logarit định nghĩa của $\pi^*_r$ được (c). Vì $e^{r/\beta}>0$, $\pi^*_r(y)>0$ khi và chỉ khi $\pi_{\mathrm{ref}}(y)>0$: đó là (d). Với $r+f$, $\mathcal Z_{r+f}(x)=e^{f(x)/\beta}\mathcal Z_r(x)$, nên thừa số $e^{f(x)/\beta}$ triệt tiêu giữa tử và mẫu: đó là (e). $\square$
:::

Định lý là (4) và Phụ lục A.1 của Rafailov và cộng sự (2023); (e) là Bổ đề 2 của bài báo. Theo (a), cực đại hóa $J_\beta$ là kéo $\pi$ về $\pi^*_r$ theo KL; theo (c), tại nghiệm, *phần thưởng đã trừ KL* (KL-penalized reward) $r-\beta\log(\pi^*_r/\pi_{\mathrm{ref}})$ bằng nhau trên miền hỗ trợ. Hai giả thiết có vai trò riêng.

- Bỏ $\beta>0$: với $\beta=0$, $J_0=\mathbb E\,r$ có nghiệm tất định như $(1;\,0)$ của Ví dụ 10.25, nên kết luận (d) sai và $e^{r/\beta}$ không xác định.
- Bỏ "chọn tự do theo $x$": một lớp tham số dùng chung cho mọi lời nhắc có thể không chứa $\pi^*_r$.

**Trong thực hành.** Ở dạng (b) của Định nghĩa 10.52, $\mathcal Z_r(x)$ là tổng trên tới $\lvert\mathcal V\rvert^{T_{\max}}$ chuỗi token; Rafailov và cộng sự (2023, §4) ghi rằng ngay cả ước lượng $\mathcal Z_r(x)$ cũng tốn kém.

::: example Ví dụ 10.26 (Nghiệm dạng đóng và vai trò của $\beta$)
**Dữ kiện.** $\pi_{\mathrm{ref}}(\cdot\mid x)=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$.

**Nghiệm với $\beta=1$.** $\pi_{\mathrm{ref}}e^{\hat r}=(\tfrac43;\,\tfrac13)$, $\mathcal Z=\tfrac53$, $\pi^*=(\tfrac45;\,\tfrac15)$, giá trị tối ưu $\log\tfrac53=0{,}5108$, đúng $J_1$ của $(0{,}8;\,0{,}2)$ trong Ví dụ 10.25.

**Kiểm kết luận (a) và (c).** $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi^*)=0{,}0487$, $0{,}5108-0{,}0487=0{,}4621=J_1(\pi_{\mathrm{ref}})$; với chính sách tham lam, $0{,}5108-\log\tfrac1{0{,}8}=0{,}2877$. Phần thưởng đã trừ KL tại $\pi^*$: $\log2-\log1{,}2=-\log0{,}6=0{,}5108$.

**Vai trò của $\beta$.** $\pi^*(y_1)/\pi^*(y_2)=2\cdot2^{1/\beta}$:

- $\beta=\tfrac12$: $\mathcal Z=3$, $\pi^*=(\tfrac89;\,\tfrac19)$, giá trị tối ưu $\tfrac12\log3=0{,}5493$;
- $\beta=2$: $\mathcal Z=1{,}2761$, $\pi^*=(0{,}7388;\,0{,}2612)$, giá trị tối ưu $0{,}4877$;
- $\beta\to\infty$: $\pi^*\to\pi_{\mathrm{ref}}$; $\beta\to0^+$: $\pi^*\to(1;\,0)$.

**Diễn giải.** $\beta$ nhỏ cho phép đi xa $\pi_{\mathrm{ref}}$; với mọi $\beta>0$, $\pi^*(y_2)>0$, đúng (d).
:::

::: remark Nhận xét 10.58 (Hai mỏ neo, hai chiều KL)
**Câu hỏi.** Hệ số $\beta$ của Định nghĩa 10.56 và hệ số $\beta$ của phạt KL theo chính sách cũ (PPO-Penalty) có cùng vai trò không? Không, vì hai phép phạt đo KL tới hai chính sách khác nhau.

1. Phạt KL theo chính sách cũ (PPO-Penalty, Định nghĩa 10.43) đo $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$ với $\pi_{\mathrm{old}}$ đổi sau mỗi lần cập nhật, nên chỉ giới hạn từng bước. Mục tiêu có phạt KL theo chính sách tham chiếu đo $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ với $\pi_{\mathrm{ref}}$ cố định, nên quyết định nghiệm cuối. Ta gọi chính sách mà phép phạt giữ chính sách mới ở gần là *mỏ neo* của phép phạt: $\pi_{\mathrm{old}}$ là mỏ neo đổi theo vòng, $\pi_{\mathrm{ref}}$ là mỏ neo cố định.
2. Quy tắc chỉnh $\beta$ theo KL mục tiêu của Ziegler và cộng sự (2019, §2.2), tương tự Định nghĩa 10.43, đo KL tới mô hình ban đầu, không tới $\pi_{\mathrm{old}}$.
3. Chiều KL ngược nhau: phạt KL theo chính sách cũ đặt mỏ neo ở vị trí thứ nhất, $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$, còn Định nghĩa 10.56 đặt mỏ neo ở vị trí thứ hai, $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$. Với $\pi=(1;\,0)$, $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})=\log\tfrac32$, còn $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi)=+\infty$.
:::

Định lý 10.57 cho $\pi^*=(\tfrac45;\,\tfrac15)$ trên ví dụ, nhưng cần $\mathcal Z_r(x)$; với mô hình ngôn ngữ, chúng ta cần cực đại hóa $J_\beta$ bằng mẫu.

<!-- note-topic-id: lec-10-topic-27 -->
### 7.3 RLHF với PPO

*Học tăng cường từ phản hồi con người* (reinforcement learning from human feedback, RLHF) cực đại hóa $J_\beta$ bằng mẫu. Thuật toán 10.49 nhận phần thưởng sau mỗi bước, còn $J_\beta$ chứa KL của cả câu trả lời; bổ đề sau chia KL đó theo token.

::: lemma Bổ đề 10.59 (KL của câu trả lời bằng tổng KL theo token)
**Giả thiết.** Bài toán ở dạng (b) của Định nghĩa 10.52; $\pi$, $\pi_{\mathrm{ref}}$ là hai chính sách trên token, với $\pi_{\mathrm{ref}}(a\mid s)>0$ khi $\pi(a\mid s)>0$.

**Kết luận.**

- (a) Với mọi câu trả lời $y=(A_0,\dots,A_{T-1})$ có $\pi(y\mid x)>0$,
  $$\begin{aligned}&\log\frac{\pi(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}\\&\quad=\sum_{t=0}^{T-1}\log\frac{\pi(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}.\end{aligned}$$
- (b) KL của câu trả lời bằng kỳ vọng của tổng KL theo token:
  $$\begin{aligned}&D_{\mathrm{KL}}\bigl(\pi(\cdot\mid x)\Vert\pi_{\mathrm{ref}}(\cdot\mid x)\bigr)\\&\quad=\mathbb E_\pi\Bigl[\sum_{t=0}^{T-1}D_{\mathrm{KL}}\bigl(\pi(\cdot\mid S_t)\\&\qquad\Vert\pi_{\mathrm{ref}}(\cdot\mid S_t)\bigr)\Bigr].\end{aligned}$$

**Điều kiện áp dụng.** Kỳ vọng ở (b) lấy theo câu trả lời do $\pi$ sinh từ $S_0=x$.

**Phạm vi.** (b) đúng theo kỳ vọng; trên một câu trả lời, tổng ở (a) có thể âm.
:::

::: proof
**Bước 1 (kết luận a).** Theo Định nghĩa 10.52(b), cả $\pi(y\mid x)$ và $\pi_{\mathrm{ref}}(y\mid x)$ là tích theo token trên cùng dãy trạng thái, vì chuyển tất định; lấy logarit của thương.

**Bước 2 (kết luận b).** Lấy kỳ vọng của (a) theo $y\sim\pi$ và viết vế phải là $\sum_{t<T_{\max}}\mathbb E[\mathbb 1\{t<T\}\ell_t]$, với $\ell_t$ là log-tỉ số tại bước $t$. Sự kiện $\{t<T\}$ chỉ phụ thuộc $S_t$, và khi biết $S_t$ thì $A_t\sim\pi(\cdot\mid S_t)$, nên theo tính chất tháp $\mathbb E[\mathbb 1\{t<T\}\ell_t]=\mathbb E\bigl[\mathbb 1\{t<T\}\,\mathbb E[\ell_t\mid S_t]\bigr]$, với $\mathbb E[\ell_t\mid S_t]=D_{\mathrm{KL}}(\pi(\cdot\mid S_t)\Vert\pi_{\mathrm{ref}}(\cdot\mid S_t))$. $\square$
:::

Với hai token $\mathrm a$, $\mathrm b$, câu trả lời dài $T_{\max}=2$ token, $\pi_{\mathrm{ref}}$ đều ở mỗi bước, và $\pi$ chọn $(\mathrm a;\,\mathrm b)$ ở token đầu với xác suất $(0{,}6;\,0{,}4)$, token sau với $(0{,}9;\,0{,}1)$ sau $\mathrm a$, $(0{,}5;\,0{,}5)$ sau $\mathrm b$: KL của câu trả lời là $0{,}2410=0{,}0201+0{,}6\cdot0{,}3681+0{,}4\cdot0$. Theo Bổ đề 10.59(b), *phạt KL theo từng token* (per-token KL penalty) của Ouyang và cộng sự (2022, §3.5) có tổng kỳ vọng bằng KL của câu trả lời.

::: proposition Mệnh đề 10.60 (Gradient của mục tiêu có phạt KL)
**Giả thiết.** Dạng (a) của Định nghĩa 10.52; $\pi_\theta>0$ khả vi theo $\theta$, như chính sách softmax; $\pi_{\mathrm{ref}}>0$.

**Kết luận.** Với phần thưởng đã trừ KL $\tilde r_\theta=r-\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$,

- (a) $\nabla_\theta J_\beta(\theta)=\mathbb E_{x\sim\mu_0,\,y\sim\pi_\theta}\bigl[\tilde r_\theta(x,y)\,\nabla_\theta\log\pi_\theta(y\mid x)\bigr]$;
- (b) tại $\theta_{\mathrm{old}}$, $\nabla_\theta J_\beta=\mathbb E[A_{\mathrm{old}}\nabla_\theta\log\pi_\theta]$, gradient chính sách với phần thưởng cố định $\tilde r_{\theta_{\mathrm{old}}}$ và lợi thế $A_{\mathrm{old}}(x,y)=\tilde r_{\theta_{\mathrm{old}}}(x,y)-\mathbb E_{y'\sim\pi_{\mathrm{old}}}\tilde r_{\theta_{\mathrm{old}}}(x,y')$.

**Điều kiện áp dụng.** Kỳ vọng chính xác; ở (b), $\tilde r_{\theta_{\mathrm{old}}}$ giữ cố định khi lấy đạo hàm.

**Phạm vi.** Gradient tại một điểm; không nói về bước lớn hay hội tụ.
:::

::: proof
Viết $J_\beta=\mathbb E_x\sum_y\pi_\theta\tilde r_\theta$. Đạo hàm tích, với $\nabla\pi_\theta=\pi_\theta\nabla\log\pi_\theta$ và $\nabla\tilde r_\theta=-\beta\nabla\log\pi_\theta$, cho $\mathbb E[\tilde r_\theta\nabla\log\pi_\theta]-\beta\,\mathbb E[\nabla\log\pi_\theta]$; số hạng sau bằng $0$ theo Mệnh đề 09.17: đó là (a). Với $\tilde r_{\theta_{\mathrm{old}}}$ cố định, gradient chính sách $\mathbb E_{\pi_\theta}[\tilde r_{\theta_{\mathrm{old}}}\nabla\log\pi_\theta]$ trùng (a) tại $\theta_{\mathrm{old}}$, và trừ hằng $\mathbb E_{\pi_{\mathrm{old}}}\tilde r_{\theta_{\mathrm{old}}}$ không đổi kỳ vọng (Mệnh đề 09.17): đó là (b). $\square$
:::

PPO tính $\tilde r_{\theta_{\mathrm{old}}}$ lúc sinh mẫu và giữ cố định trong vòng. Khi lợi thế đúng, theo (b) và Mệnh đề 10.41(c), gradient của hàm thay thế mẫu tại $\theta_{\mathrm{old}}$ có kỳ vọng $\nabla J_\beta(\theta_{\mathrm{old}})$. Trên dạng mức token, Bổ đề 10.59(a) chia số hạng KL theo token, cho phần thưởng của bước $t$
$$\begin{aligned}&R_{t+1}=-\beta\log\frac{\pi_{\mathrm{old}}(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}\\&\quad+\mathbb 1\{t+1=T\}\,\hat r(x,y),\end{aligned}\tag{7.1}$$
với tổng bằng $\tilde r_{\theta_{\mathrm{old}}}(x,y)$ khi $r=\hat r$.

::: example Ví dụ 10.27 (Hai vòng PPO trên phần thưởng đã trừ KL)
**Dữ kiện.** $\pi_{\mathrm{ref}}(\cdot\mid x)=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$, $\beta=1$, $\epsilon=0{,}2$; $p$ là xác suất chọn $y_1$. Mỗi vòng giữ cố định $\tilde r(y)=\hat r(y)-\log\frac{\pi_{\mathrm{old}}(y)}{\pi_{\mathrm{ref}}(y)}$ và lợi thế đúng $\tilde r(y)-\mathbb E_{\pi_{\mathrm{old}}}\tilde r$; vòng trong tăng $\mathcal L^{\mathrm{CLIP}}$ từ $\pi_{\mathrm{old}}$ tới đầu đoạn phẳng. Vòng 1 dùng bộ đệm $y_1,y_1,y_2$ của Ví dụ 10.17.

**Vòng 1, $\pi_{\mathrm{old}}=\pi_{\mathrm{ref}}$.** $\tilde r=\hat r$, $\mathbb E_{\pi_{\mathrm{old}}}\tilde r=\tfrac23\log2$, và lợi thế của ba mẫu là $\tfrac13\log2\,(1;\,1;\,-2)=(0{,}2310;\,0{,}2310;\,-0{,}4621)$, tức $\tfrac13\log2$ lần lợi thế của Ví dụ 10.17. Vì vậy $\mathcal L^{\mathrm{CLIP}}$ tăng tới $p=0{,}8=\tfrac23\cdot1{,}2$ rồi nằm ngang. Gradient tại $\theta_{\mathrm{ref}}$ là $\tfrac13\bigl[2\cdot0{,}2310\,(\tfrac13;\,-\tfrac13)-0{,}4621\,(-\tfrac23;\,\tfrac23)\bigr]=\tfrac29\log2\,(1;\,-1)=(0{,}1540;\,-0{,}1540)$, đúng $\nabla J_1$ theo Mệnh đề 10.60.

**Vòng 2, $\pi_{\mathrm{old}}=(0{,}8;\,0{,}2)$.** $\tilde r=(\log2-\log1{,}2;\,-\log0{,}6)=(0{,}5108;\,0{,}5108)$, như Ví dụ 10.26; lợi thế bằng $0$, mọi số hạng cắt bằng $0$ (Mệnh đề 10.40(c)), và chính sách đứng yên ở $\pi^*=(\tfrac45;\,\tfrac15)$.

**Diễn giải.** Phép cắt đo tỉ số tới $\pi_{\mathrm{old}}$ và giới hạn vòng 1 ở $p\le0{,}8$; điểm dừng do $\pi_{\mathrm{ref}}$ và $\hat r$ quyết định qua phần thưởng đã trừ KL. Vòng 1 dừng đúng ở $\pi^*$ chỉ vì $\tfrac23(1+\epsilon)=0{,}8$ khi $\epsilon=0{,}2$.

**Kiểm tra lại.** $J_1(0{,}8)=0{,}5545-0{,}0437=0{,}5108=\log\tfrac53$.
:::

::: algorithm Thuật toán 10.61 (RLHF với PPO)
**Đầu vào.** Mô hình ngôn ngữ đã tiền huấn luyện; câu trả lời mẫu do người gán nhãn viết; tập lời nhắc; người gán nhãn; $\beta>0$; tham số của Thuật toán 10.49, với $N$ là số lời nhắc mỗi vòng.

**Đầu ra.** Chính sách $\pi_\theta$.

**Giả thiết.** Dạng (b) của Định nghĩa 10.52; người gán nhãn so sánh theo Định nghĩa 10.53; $\pi_\theta$, $\pi_{\mathrm{ref}}$ là softmax trên token.

**Các bước.**

1. *Tinh chỉnh có giám sát* (supervised fine-tuning, SFT) trên bản mẫu bằng hợp lý cực đại, được $\pi^{\mathrm{SFT}}$; đặt $\pi_{\mathrm{ref}}\leftarrow\pi^{\mathrm{SFT}}$, cố định từ đây, và $\pi_\theta\leftarrow\pi^{\mathrm{SFT}}$.
2. Sinh câu trả lời bằng $\pi^{\mathrm{SFT}}$, thu so sánh thành $\mathcal D_{\mathrm{pref}}$, khớp $\hat r$ bằng cực tiểu hóa $L^{\mathrm{BT}}$ (Mệnh đề 10.54), chuẩn hóa (Nhận xét 10.55); khởi tạo critic từ $\hat r$.
3. Mỗi vòng, chạy một vòng của Thuật toán 10.49 trên MDP mức token với $\gamma=1$: sinh câu trả lời bằng $\pi_{\mathrm{old}}$ cho $N$ lời nhắc, gán phần thưởng (7.1) cho mỗi token, tính GAE, cập nhật $\theta$, $w$ trong $K$ epoch.

**Mô hình trong bộ nhớ.** $\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic.

**Điều kiện dừng.** Ngân sách số lượt.

**Chi phí mỗi vòng.** Sinh $N$ câu trả lời; một lần tính $\hat r$ mỗi câu trả lời; log-xác suất của $\pi_{\mathrm{ref}}$ mỗi token; các bước gradient của Thuật toán 10.49.
:::

Thuật toán 10.61 theo khung chung của Ziegler và cộng sự (2019, §2), Stiennon và cộng sự (2020, §3.4) và Ouyang và cộng sự (2022, §3.1).

**Trong thực hành.** $\pi_{\mathrm{ref}}$ là bản sao đóng băng của $\pi^{\mathrm{SFT}}$. Với $\gamma=1$ và độ dài bị chặn, (G3) thỏa, còn các kết quả của Mục 4 cần $\gamma<1$. Ouyang và cộng sự (2022, Phụ lục C.4) dùng $\beta=0{,}02$, bán kính cắt $0{,}2$, một epoch mỗi vòng. Biến thể "PPO" của bài báo cực đại hóa đúng $J_\beta$; các mô hình InstructGPT chính (PPO-ptx) cộng thêm một số hạng hợp lý trên dữ liệu tiền huấn luyện, nên Định lý 10.57 không áp dụng nguyên dạng cho chúng.

::: remark Nhận xét 10.62 (Tối ưu quá mức mô hình phần thưởng)
Stiennon và cộng sự (2020, §4.3, Hình 5) đo, với một phiên bản trước của mô hình phần thưởng và nhiều hệ số KL: khi tối ưu nhẹ, chất lượng do người gán nhãn đánh giá tăng; khi tối ưu mạnh hơn, ưu tiên thật giảm so với dự đoán của mô hình phần thưởng, và cuối cùng mô hình phần thưởng tương quan âm với ưu tiên đó. Đó là *tối ưu quá mức* (over-optimization) mô hình phần thưởng; số hạng KL giữ đầu ra gần dữ liệu mà mô hình phần thưởng đã thấy (§3.4).
:::

Thuật toán 10.61 cần bốn mô hình và việc sinh câu trả lời ở mọi vòng, trong khi $\hat r$ chỉ được dùng để xác định $\pi^*_{\hat r}$.

<!-- note-topic-id: lec-10-topic-28 -->
### 7.4 Tối ưu ưu tiên trực tiếp

Trên ví dụ, ta có thể đọc lại $\hat r$ từ nghiệm: từ $\pi^*=(\tfrac45;\,\tfrac15)$ và $\mathcal Z=\tfrac53$ của Ví dụ 10.26, với $\beta=1$,
$$\begin{aligned}&\log\tfrac{0{,}8}{2/3}+\log\tfrac53\\&\quad=0{,}1823+0{,}5108\\&\quad=0{,}6931=\hat r(x,y_1),\\&\log\tfrac{0{,}2}{1/3}+\log\tfrac53\\&\quad=-0{,}5108+0{,}5108\\&\quad=0=\hat r(x,y_2).\end{aligned}$$
Hiệu hai vế trái, $\log1{,}2-\log0{,}6=\log2$, bằng $\hat r(x,y_1)-\hat r(x,y_2)$ và không chứa $\mathcal Z$. Một cách trực quan, mỗi chính sách là nghiệm của mục tiêu có phạt KL theo chính sách tham chiếu với một phần thưởng nào đó, nên chúng ta có thể viết phần thưởng theo chính sách và học thẳng chính sách.

::: proposition Mệnh đề 10.63 (Đổi biến giữa phần thưởng và chính sách)
**Giả thiết.** Như Định lý 10.57; thêm $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $x$, $y$.

**Kết luận.**

- (a) $r(x,y)=\beta\log\dfrac{\pi^*_r(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}+\beta\log\mathcal Z_r(x)$ với mọi $x$, $y$.
- (b) Dưới mô hình Bradley–Terry với phần thưởng $r$,
  $$\begin{aligned}&\Pr(y\succ y'\mid x)\\&\quad=\sigma\Bigl(\beta\log\frac{\pi^*_r(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}\\&\qquad-\beta\log\frac{\pi^*_r(y'\mid x)}{\pi_{\mathrm{ref}}(y'\mid x)}\Bigr),\end{aligned}$$
  không còn $\mathcal Z_r$.
- (c) Với mỗi chính sách $\pi$ có $\pi(y\mid x)>0$ với mọi $x$, $y$, đặt $r_\pi=\beta\log(\pi/\pi_{\mathrm{ref}})$. Khi đó $\pi^*_{r_\pi}=\pi$; $r_{\pi^*_r}=r-\beta\log\mathcal Z_r\in[r]$; và $r_{\pi^*_r}$ là phần tử duy nhất của $[r]$ có dạng $r_\pi$.

**Điều kiện áp dụng.** $\beta>0$ và $\pi_{\mathrm{ref}}>0$, để mọi log-tỉ số hữu hạn.

**Phạm vi.** Một phép đổi biến; không nói về dữ liệu hay cực tiểu của hàm mất mát.
:::

::: proof
**Bước 1 (kết luận a).** Định lý 10.57(c) cho đẳng thức với mọi $y$ có $\pi_{\mathrm{ref}}(y\mid x)>0$, tức mọi $y$ theo giả thiết.

**Bước 2 (kết luận b).** Thế (a) vào $\sigma\bigl(r(x,y)-r(x,y')\bigr)$ của Định nghĩa 10.53; số hạng $\beta\log\mathcal Z_r(x)$ có mặt ở cả $r(x,y)$ và $r(x,y')$, nên triệt tiêu trong hiệu.

**Bước 3 (kết luận c).** Với $r_\pi$, $\mathcal Z_{r_\pi}(x)=\sum_y\pi_{\mathrm{ref}}(y\mid x)\,\frac{\pi(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}=1$, nên $\pi^*_{r_\pi}=\pi_{\mathrm{ref}}\cdot\pi/\pi_{\mathrm{ref}}=\pi$. Theo (a), $r_{\pi^*_r}=r-\beta\log\mathcal Z_r(x)$, và $-\beta\log\mathcal Z_r(x)$ chỉ phụ thuộc $x$. Nếu $r_\pi$ và $r_{\pi'}$ cùng thuộc $[r]$ thì $r_\pi-r_{\pi'}=\beta\log(\pi/\pi')=f(x)$ với một $f$ chỉ phụ thuộc $x$, nên $\pi(y\mid x)=\pi'(y\mid x)\,e^{f(x)/\beta}$; lấy tổng theo $y$ được $1=e^{f(x)/\beta}$, tức $f=0$ và $\pi=\pi'$. $\square$
:::

Mệnh đề là (5), (6), Định lý 1 và Mệnh đề 1 (Phụ lục A.6) của Rafailov và cộng sự (2023). Theo (b), hàm phân hoạch triệt tiêu vì $\mathcal Z_r(x)$ chỉ phụ thuộc lời nhắc, còn phép so sánh luôn giữa hai câu trả lời của cùng lời nhắc. Theo (c), mỗi lớp $[r]$ ứng với đúng một chính sách có miền hỗ trợ đầy đủ.

::: definition Định nghĩa 10.64 (Phần thưởng ngầm định, hàm mất mát DPO)
Cho $\pi_{\mathrm{ref}}>0$, $\beta>0$ và một chính sách $\pi_\theta>0$. *Phần thưởng ngầm định* (implicit reward) của $\pi_\theta$ là
$$r_\theta(x,y)=\beta\log\frac{\pi_\theta(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}.$$
Với bộ ba $(x,y_w,y_l)$, đặt $\Delta r_\theta=r_\theta(x,y_w)-r_\theta(x,y_l)$. *Hàm mất mát DPO* là
$$\begin{aligned}&L^{\mathrm{DPO}}(\theta)\\&\quad=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\bigl[\log\sigma(\Delta r_\theta)\bigr].\end{aligned}$$
*Tối ưu ưu tiên trực tiếp* (Direct Preference Optimization, DPO) cực tiểu hóa $L^{\mathrm{DPO}}$ theo $\theta$.
:::

Theo Mệnh đề 10.54(a), $L^{\mathrm{DPO}}(\theta)=L^{\mathrm{BT}}(r_\theta)$: DPO là hồi quy logistic với biến $\Delta r_\theta$ (Rafailov và cộng sự, 2023, (7)). Với hai câu trả lời, chính sách softmax đặc trưng đơn vị và $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\log\frac{\pi_\theta(y_1\mid x)}{\pi_\theta(y_2\mid x)}=\theta_1-\theta_2$, nên bộ ba chọn $y_1$ có $\Delta r_\theta=\beta(\theta_1-\theta_2-\log2)$ và bộ ba chọn $y_2$ có $\Delta r_\theta$ ngược dấu.

::: theorem Định lý 10.65 (Tương đương giữa RLHF và DPO)
**Giả thiết.**

- (H1) Với mọi $x$, $\mathcal Y(x)$ hữu hạn và $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $y$.
- (H2) $\beta>0$.
- (H3) Lớp chính sách gồm mọi phân phối có miền hỗ trợ đầy đủ trên $\mathcal Y(x)$, chọn tự do theo $x$.
- (H4a) $L^{\mathrm{BT}}$, xét trên mọi hàm phần thưởng $\hat r$ trên các cặp $(x,y)$, đạt cực tiểu.
- (H4b) Tập cực tiểu của $L^{\mathrm{BT}}$ là đúng một lớp $[\hat r]$.

Hai con đường dùng cùng $\mathcal D_{\mathrm{pref}}$, cùng $\beta$, cùng $\pi_{\mathrm{ref}}$. Con đường RLHF lý tưởng khớp một cực tiểu $\hat r$ của $L^{\mathrm{BT}}$ rồi lấy nghiệm $\pi^*_{\hat r}$ của Định lý 10.57. Viết $L^{\mathrm{DPO}}(\pi)$ cho giá trị của $L^{\mathrm{DPO}}$ khi $\pi_\theta=\pi$.

**Kết luận.**

- (a) Dưới (H1)–(H3) và (H4a), với mọi cực tiểu $\hat r$ của $L^{\mathrm{BT}}$, $\pi^*_{\hat r}$ cực tiểu $L^{\mathrm{DPO}}$.
- (b) Dưới (H1)–(H3) và (H4a), mọi cực tiểu $\pi$ của $L^{\mathrm{DPO}}$ có $r_\pi$ cực tiểu $L^{\mathrm{BT}}$ và $\pi=\pi^*_{r_\pi}$. Thêm (H4b), $L^{\mathrm{DPO}}$ có đúng một cực tiểu, là $\pi^*_{\hat r}$.
- (c) Dưới (H1)–(H3) và (H4a), $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$.

**Điều kiện áp dụng.** Cực tiểu hóa chính xác cả hai hàm mất mát và giải chính xác $J_\beta$.

**Phạm vi.** Định lý nói về nghiệm, không về các bước lặp của PPO hay hạ gradient. Khi (H4a) hỏng, cả hai hàm mất mát không có cực tiểu; khi chỉ (H4b) hỏng, nghiệm không duy nhất.
:::

::: proof
**Bước 1 (đẳng thức đại số).** Với mọi $\pi$ trong lớp của (H3), $r_\pi$ hữu hạn theo (H1), và $L^{\mathrm{DPO}}(\pi)=L^{\mathrm{BT}}(r_\pi)$ theo Định nghĩa 10.64.

**Bước 2 (cận dưới).** Cực tiểu của (H4a) lấy trên mọi hàm phần thưởng, kể cả $r_\pi$, nên $L^{\mathrm{DPO}}(\pi)=L^{\mathrm{BT}}(r_\pi)\ge\min L^{\mathrm{BT}}$ với mọi $\pi$.

**Bước 3 (kết luận a và c).** Cho $\hat r$ là một cực tiểu của $L^{\mathrm{BT}}$. Theo Định lý 10.57(d) và (H1), $\pi^*_{\hat r}$ có miền hỗ trợ đầy đủ, nên thuộc lớp của (H3). Theo Mệnh đề 10.63(c), $r_{\pi^*_{\hat r}}\in[\hat r]$, nên theo Mệnh đề 10.54(b),
$$\begin{aligned}&L^{\mathrm{DPO}}(\pi^*_{\hat r})=L^{\mathrm{BT}}(r_{\pi^*_{\hat r}})\\&\quad=L^{\mathrm{BT}}(\hat r)=\min L^{\mathrm{BT}}.\end{aligned}$$
Cùng Bước 2, $\pi^*_{\hat r}$ cực tiểu $L^{\mathrm{DPO}}$ và $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$.

**Bước 4 (kết luận b).** Nếu $\pi$ cực tiểu $L^{\mathrm{DPO}}$ thì $L^{\mathrm{BT}}(r_\pi)=\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$ theo (c), nên $r_\pi$ cực tiểu $L^{\mathrm{BT}}$; và $\pi=\pi^*_{r_\pi}$ theo Mệnh đề 10.63(c). Dưới (H4b), $r_\pi=\hat r+f$ với $f$ chỉ phụ thuộc $x$, nên $\pi=\pi^*_{\hat r+f}=\pi^*_{\hat r}$ theo Định lý 10.57(e). $\square$
:::

Dưới (H1)–(H3), (H4a), (H4b), cực tiểu của $L^{\mathrm{DPO}}$ là nghiệm $\pi^*_{\hat r}$ của con đường RLHF lý tưởng, nhưng DPO không cần mô hình phần thưởng riêng, critic hay lấy mẫu. Vì Bước 1 là đẳng thức đại số, mô hình Bradley–Terry chỉ cần để đọc $\hat r$ là ước lượng hợp lý cực đại. (H4a), (H4b) thỏa khi $0<k<n$ với hai câu trả lời, và khi mỗi cặp được so sánh có cả hai kết quả và các cặp nối mọi câu trả lời của mỗi lời nhắc: mỗi số hạng của $L^{\mathrm{BT}}$ khi đó lồi ngặt theo hiệu của nó và tiến tới $+\infty$ khi hiệu tiến tới $\pm\infty$. Mỗi giả thiết có vai trò riêng.

- Bỏ (H1): với $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac12;\,0)$, bốn phép so sánh chọn $y_1$ trước $y_2$ và hai phép ngược lại, mọi chính sách có $\pi(y_2)=2^{-1/\beta}\pi(y_1)>0$ đều cực tiểu $L^{\mathrm{DPO}}$, dù $\pi(y_3)$ lớn, trong khi $\pi^*_{\hat r}(y_3)=0$ theo Định lý 10.57(d). Ví dụ cũng làm (H4b) hỏng, nhưng ở đây hai tập nghiệm khác nhau.
- Bỏ (H4a): với $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ và ba phép so sánh cùng chọn $y_1$, $L^{\mathrm{BT}}$ không có cực tiểu và $L^{\mathrm{DPO}}=-\log\sigma\bigl(\beta(\theta_1-\theta_2-\log2)\bigr)$ giảm ngặt theo $\theta_1-\theta_2$; cả hai con đường đẩy chính sách về $(1;\,0)$.
- Bỏ (H4b): với $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, $\beta=1$ và sáu phép so sánh chỉ giữa $y_1$, $y_2$, bốn chọn $y_1$, mọi chính sách có $\pi(y_1)=4\pi(y_2)$ đều cực tiểu $L^{\mathrm{DPO}}$.
- Bỏ (H3): trên một lớp tham số không chứa $\pi^*_{\hat r}$, cực tiểu của $L^{\mathrm{DPO}}$ và nghiệm của $J_\beta$ không nhất thiết trùng nhau.

::: proposition Mệnh đề 10.66 (Gradient của hàm mất mát DPO)
**Giả thiết.** Như Định nghĩa 10.64; $\pi_\theta$ khả vi theo $\theta$.

**Kết luận.**
$$\begin{aligned}&\nabla_\theta L^{\mathrm{DPO}}(\theta)\\&\quad=-\beta\,\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\Bigl[\sigma(-\Delta r_\theta)\\&\qquad\times\bigl(\nabla_\theta\log\pi_\theta(y_w\mid x)\\&\qquad-\nabla_\theta\log\pi_\theta(y_l\mid x)\bigr)\Bigr].\end{aligned}$$

**Điều kiện áp dụng.** $\pi_{\mathrm{ref}}$ cố định, không lấy đạo hàm qua nó.

**Phạm vi.** Gradient của hàm mất mát mẫu trên $\mathcal D_{\mathrm{pref}}$.
:::

::: proof
Từ $\frac{d}{dz}\bigl[-\log\sigma(z)\bigr]=-\sigma(-z)$ và $\nabla_\theta\Delta r_\theta=\beta\bigl(\nabla\log\pi_\theta(y_w\mid x)-\nabla\log\pi_\theta(y_l\mid x)\bigr)$, vì $\pi_{\mathrm{ref}}$ không phụ thuộc $\theta$, quy tắc dây chuyền cho từng số hạng; lấy trung bình trên $\mathcal D_{\mathrm{pref}}$. $\square$
:::

Mỗi bộ ba đẩy $\theta$ theo hướng làm tăng hiệu $\log\pi_\theta(y_w\mid x)-\log\pi_\theta(y_l\mid x)$, với trọng số $\sigma(-\Delta r_\theta)$, lớn khi phần thưởng ngầm định xếp sai cặp ($\Delta r_\theta<0$). Rafailov và cộng sự (2023, §4) viết rằng phiên bản bỏ trọng số này có thể làm mô hình ngôn ngữ suy biến.

::: example Ví dụ 10.28 (Một bước DPO tính tay)
**Dữ kiện.** Sáu phép so sánh của Ví dụ 10.23: bốn bộ ba $(x,y_1,y_2)$, hai bộ ba $(x,y_2,y_1)$. Chính sách softmax với đặc trưng đơn vị, $\pi_{\mathrm{ref}}$ có $\theta_{\mathrm{ref}}=(\log2;\,0)$, tức $(\tfrac23;\,\tfrac13)$; $\beta=1$. Hạ gradient với bước học $1$, khởi tạo $\theta=\theta_{\mathrm{ref}}$.

**Hàm mất mát.** Với $\beta=1$, bộ ba chọn $y_1$ có $\Delta r_\theta=\theta_1-\theta_2-\log2$, bộ ba chọn $y_2$ có hiệu ngược dấu, nên
$$\begin{aligned}&L^{\mathrm{DPO}}=-\tfrac16\bigl[4\log\sigma(\Delta r_\theta)\\&\quad+2\log\sigma(-\Delta r_\theta)\bigr].\end{aligned}$$
Tại $\theta_{\mathrm{ref}}$, $\Delta r_\theta=0$ và $L^{\mathrm{DPO}}=\log2=0{,}6931$.

**Gradient.** Mọi trọng số bằng $\sigma(0)=\tfrac12$. Theo Mệnh đề 09.16, $\psi_\theta(y_1)-\psi_\theta(y_2)=(1-p)(1;\,-1)+p(1;\,-1)=(1;\,-1)$ với mọi $\theta$. Mệnh đề 10.66 cho
$$\begin{aligned}&\nabla L^{\mathrm{DPO}}\\&\quad=-\bigl[\tfrac46\cdot\tfrac12\,(1;\,-1)\\&\qquad+\tfrac26\cdot\tfrac12\,(-1;\,1)\bigr]\\&\quad=(-\tfrac16;\,\tfrac16).\end{aligned}$$

**Bước.** $\theta=(\log2+\tfrac16;\,-\tfrac16)=(0{,}8598;\,-0{,}1667)$, nên $\theta_1-\theta_2=\log2+\tfrac13=1{,}0265$, $\pi_\theta(y_1)=\sigma(1{,}0265)=0{,}7362$ và $L^{\mathrm{DPO}}=0{,}6514$. Phần thưởng ngầm định là $r_\theta(y_1)=\log\frac{0{,}7362}{2/3}=0{,}0993$, $r_\theta(y_2)=\log\frac{0{,}2638}{1/3}=-0{,}2341$, với hiệu $\tfrac13$.

**Bước tiếp theo.** Ở bước 2, trọng số là $\sigma(-\tfrac13)=0{,}4174$ cho bốn bộ ba chọn $y_1$ và $\sigma(\tfrac13)=0{,}5826$ cho hai bộ ba bị xếp sai. Bước 2 đến 5 cho $\pi_\theta(y_1)=0{,}7676$; $0{,}7829$; $0{,}7907$; $0{,}7949$ và $L^{\mathrm{DPO}}=0{,}6407$; $0{,}6377$; $0{,}6369$; $0{,}6366$.

**Cực tiểu.** Theo Mệnh đề 10.54(c) với $n=6$, $k=4$, cực tiểu đạt tại $\Delta r_\theta=\log2$, tức $\theta_1-\theta_2=2\log2$ và $\pi_\theta=(\tfrac45;\,\tfrac15)$, với $\min L^{\mathrm{DPO}}=0{,}6365$. Đó là nghiệm $\pi^*$ của Ví dụ 10.26 và giá trị $\min L^{\mathrm{BT}}$ của Ví dụ 10.24, đúng như Định lý 10.65.

**Kiểm tra lại.** Với $\beta$ tùy ý, cực tiểu đạt tại $\beta(\theta_1-\theta_2-\log2)=\log2$, cho $\pi_\theta(y_1)/\pi_\theta(y_2)=2\cdot2^{1/\beta}$, đúng tỉ số của Ví dụ 10.26.
:::

::: algorithm Thuật toán 10.67 (DPO)
**Đầu vào.** Tập dữ liệu ưu tiên $\mathcal D_{\mathrm{pref}}$ cố định; chính sách tham chiếu $\pi_{\mathrm{ref}}$ đóng băng; hệ số $\beta>0$; bộ tối ưu, bước học, cỡ mini-batch $M$, số epoch.

**Đầu ra.** Chính sách $\pi_\theta$.

**Giả thiết.** (H1), (H2) của Định lý 10.65; $\pi_\theta$ là softmax trên token, nên dương ở mọi token.

**Khởi tạo.** $\theta\leftarrow\theta_{\mathrm{ref}}$; tính trước $\log\pi_{\mathrm{ref}}(y_w\mid x)$ và $\log\pi_{\mathrm{ref}}(y_l\mid x)$ cho mọi bộ ba.

**Mỗi epoch:** xáo $\mathcal D_{\mathrm{pref}}$ và chia thành các mini-batch cỡ $M$; với mỗi mini-batch:

1. tính $\log\pi_\theta(y_w\mid x)$ và $\log\pi_\theta(y_l\mid x)$, mỗi đại lượng là tổng log-xác suất của các token (Bổ đề 10.59(a));
2. tính $\Delta r_\theta$ của Định nghĩa 10.64 từ bốn log-xác suất và $L^{\mathrm{DPO}}$ trung bình trên mini-batch;
3. thực hiện một bước của bộ tối ưu theo gradient của Mệnh đề 10.66.

**Điều kiện dừng.** Sau số epoch đã định.

**Chi phí mỗi bộ ba.** Hai lượt tính $\log\pi_\theta$ trên chuỗi có sẵn và một lượt lan truyền ngược; không sinh mẫu, không critic.

**Mô hình trong bộ nhớ.** $\pi_\theta$, $\pi_{\mathrm{ref}}$.
:::

Với sáu bộ ba của Ví dụ 10.23 trong một mini-batch, hạ gradient với bước học $1$ và $\theta\leftarrow\theta_{\mathrm{ref}}$, bước đầu của Thuật toán 10.67 cho gradient $(-\tfrac16;\,\tfrac16)$ và $\pi_\theta(y_1)=0{,}7362$, đúng bước tính tay của Ví dụ 10.28.

**Trong thực hành.** $\pi_{\mathrm{ref}}$ là mô hình SFT; khi không có, Rafailov và cộng sự (2023, §4) khớp $\pi_{\mathrm{ref}}$ bằng hợp lý cực đại trên các cặp $(x,y_w)$. Log-xác suất của câu trả lời là tổng log-xác suất token (Bổ đề 10.59(a)). Dữ liệu cố định, do $\pi^{\mathrm{SFT}}$ sinh: DPO là phương pháp *ngoại tuyến* (offline) trên dữ liệu khác chính sách, khác Thuật toán 10.61 (*trực tuyến*, online), và không cần tỉ số $\rho_t$ vì $L^{\mathrm{DPO}}$ không là kỳ vọng theo $\pi_\theta$. Bài báo (Phụ lục B) dùng $\beta=0{,}1$, cỡ mini-batch $64$, RMSprop với bước học $10^{-6}$.

::: remark Nhận xét 10.68 (Đọc kết quả của DPO)
Nhầm lẫn thường gặp: coi DPO là tăng xác suất của mọi câu trả lời được chọn. $L^{\mathrm{DPO}}$ chỉ điều khiển hiệu $\Delta r_\theta$. Với mọi $\pi_\theta>0$,
$$\begin{aligned}&\mathbb E_{y\sim\pi_{\mathrm{ref}}}r_\theta(x,y)\\&\quad=\beta\sum_y\pi_{\mathrm{ref}}(y\mid x)\\&\qquad\times\log\frac{\pi_\theta(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}\\&\quad=-\beta D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)\le0\end{aligned}$$
(Rafailov, Hejna, Park và Finn, 2024, (16)), nên khi phần thưởng ngầm định của một số câu tăng, của các câu khác phải giảm. Sau bước 1 của Ví dụ 10.28, $\tfrac23\cdot0{,}0993+\tfrac13\cdot(-0{,}2341)=-0{,}0119=-D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)$. Khi có nhiều câu trả lời, cả $y_w$ và $y_l$ có thể giảm xác suất mà $\Delta r_\theta$ vẫn tăng.
:::

<!-- note-topic-id: lec-10-topic-29 -->
### 7.5 So sánh hai con đường và giới hạn

![Hai con đường từ dữ liệu ưu tiên D pref. Nhánh trên, nét liền: mô hình phần thưởng r mũ, rồi PPO; bốn mô hình. Nhánh dưới, nét đứt: cực tiểu L DPO trên dữ liệu cố định; hai mô hình. Hai nhánh gặp ở khung đậm pi sao tỉ lệ pi ref nhân e mũ r chia beta.](img/lec-10/rlhf-dpo-hai-con-duong.svg)

Trên hình, nhánh dưới bỏ khung mô hình phần thưởng nhờ phép đổi biến của Mệnh đề 10.63; hai nhánh gặp nhau ở nghiệm của Định lý 10.57 khi các giả thiết của Định lý 10.65 thỏa.

| Tiêu chí | RLHF với PPO (Thuật toán 10.61) | DPO (Thuật toán 10.67) |
|---|---|---|
| Mục tiêu | $\max J_\beta$, $\pi_{\mathrm{ref}}$ cố định (Định nghĩa 10.56) | cùng mục tiêu |
| Đại lượng được tối ưu | $L^{\mathrm{BT}}$ cho $\hat r$, rồi $\mathcal L^{\mathrm{CLIP}}$ với phần thưởng đã trừ KL | $L^{\mathrm{DPO}}$ |
| Dữ liệu | $\mathcal D_{\mathrm{pref}}$ cộng câu trả lời sinh trực tuyến bằng $\pi_{\mathrm{old}}$ | chỉ $\mathcal D_{\mathrm{pref}}$, ngoại tuyến, khác chính sách |
| Mô hình trong bộ nhớ | $\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic | $\pi_\theta$, $\pi_{\mathrm{ref}}$ |
| Mỏ neo và chiều KL | $\pi_{\mathrm{ref}}$ trong mục tiêu, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$; thêm $\pi_{\mathrm{old}}$ của phép cắt | chỉ $\pi_{\mathrm{ref}}$; cùng $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$ của $J_\beta$, qua phép đổi biến của Mệnh đề 10.63 |
| Điều kiện dừng | ngân sách số lượt | ngân sách số epoch |
| Bảo đảm | nghiệm của $J_\beta$ là $\pi^*_{\hat r}$ (Định lý 10.57); mỗi bước: gradient đúng tại $\theta_{\mathrm{old}}$ khi lợi thế đúng (Mệnh đề 10.60); không bảo đảm hội tụ | cực tiểu toàn cục là $\pi^*_{\hat r}$ dưới (H1)–(H3), (H4a), (H4b) (Định lý 10.65); hạ gradient không bảo đảm hội tụ |

Rafailov và cộng sự (2023, §6.1) viết rằng DPO và PPO tối ưu cùng một mục tiêu.

::: remark Nhận xét 10.69 (Giới hạn của hai con đường)
1. Nghiệm $\pi^*_{\hat r}$ của con đường RLHF không gán xác suất dương cho câu trả lời mà $\pi_{\mathrm{ref}}$ không sinh (Định lý 10.57(d)); DPO thì có thể khi (H1) hỏng. Trong ví dụ của Xu và cộng sự (2024, Định lý 4.1, Bảng 1), với $\pi_{\mathrm{ref}}=(0{,}5;\,0{,}5;\,0)$ và một phép so sánh $y_1\succ y_2$, $L^{\mathrm{DPO}}$ không có cực tiểu trong lớp của (H3); cận dưới đúng $0$ đạt tại $(0{,}1;\,0;\,0{,}9)$, ngoài lớp đó, với xác suất $0{,}9$ trên $y_3$.
2. DPO không đánh giá câu trả lời ngoài dữ liệu; RLHF với PPO đánh giá chúng bằng $\hat r$, có thể sai ở đó (Nhận xét 10.62).
3. Với ưu tiên tất định, cả hai con đường lý tưởng đẩy xác suất của câu thua về $0$ với mọi $\beta$. Gheshlaghi Azar và cộng sự (2024, §4.2) lập luận, không thành định lý, rằng RLHF trong thực hành tránh được điều này nhờ mô hình phần thưởng được điều chuẩn.
:::

<!-- note-topic-id: lec-10-topic-30 -->
### 7.6 Đọc thêm: biến thể và so sánh thực nghiệm

::: remark Nhận xét 10.70 (Biến thể và so sánh thực nghiệm)
1. *Tối ưu ưu tiên đồng nhất* (Identity Preference Optimization, IPO) của Gheshlaghi Azar và cộng sự (2024, §5, (17)) hồi quy hiệu log-tỉ số $\log\frac{\pi(y_w)\pi_{\mathrm{ref}}(y_l)}{\pi(y_l)\pi_{\mathrm{ref}}(y_w)}$ về $\tfrac1{2\beta}$; trên ba phép so sánh cùng chọn $y_1$, với $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\beta=1$, IPO cho $\pi(y_1)=\sigma(\log2+0{,}5)=0{,}7673$ thay cho $1$.
2. Rafailov, Hejna, Park và Finn (2024, §3.1, Định lý 1) viết lại DPO trên MDP mức token.
3. Rafailov và cộng sự (2023, §6.1, Hình 2) báo DPO có đường biên phần thưởng–KL tốt hơn PPO trên bài toán sinh văn bản theo cảm xúc; Xu và cộng sự (2024, §5–6) báo PPO với chuẩn hóa lợi thế, mini-batch lớn và mô hình tham chiếu cập nhật bằng trung bình trượt (khi đó không còn cố định) vượt DPO trên các bài thử của họ. Hai kết quả đo trên các bài toán khác nhau.
:::

Trên Ví dụ 10.23, mô hình Bradley–Terry cho $\hat r=(\log2;\,0)$ (Mệnh đề 10.54), và mục tiêu có phạt KL theo chính sách tham chiếu với $\beta=1$ có nghiệm $(\tfrac45;\,\tfrac15)$ (Định lý 10.57). PPO nhắm tới nghiệm đó bằng mẫu sinh trực tuyến (Ví dụ 10.27), không có bảo đảm hội tụ; DPO tới cùng nghiệm bằng một hàm mất mát phân loại trên sáu phép so sánh, không cần vòng học tăng cường, khi các giả thiết của Định lý 10.65 thỏa (Ví dụ 10.28). Các kết quả nói về nghiệm, không cho biết con đường nào tốt hơn khi tối ưu không chính xác.
````

## `lecture-note.md`, dòng 2559: §8 Tổng kết, câu mở

````markdown
Mỗi kết quả của Mục 2–7 đúng dưới một bộ giả thiết riêng.
````

## `lecture-note.md`, dòng 2583–2589: §8.1, năm hàng cuối của bảng kết quả và câu đọc bảng

````markdown
| Hợp lý cực đại của mô hình phần thưởng (Mệnh đề 10.54) | mô hình Bradley–Terry; $0<k<n$ | $L^{\mathrm{BT}}=-\widehat{\mathbb E}\log\sigma(\hat r(x,y_w)-\hat r(x,y_l))$; cực tiểu $\log\frac k{n-k}$ |
| Nghiệm có phạt KL (Định lý 10.57) | $\beta>0$; chính sách chọn tự do theo $x$ | $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$; $J_\beta(\pi)=\mathbb E_x[\beta\log\mathcal Z_r-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r)]$ |
| Gradient có phạt KL (Mệnh đề 10.60) | $\pi_\theta>0$; $\pi_{\mathrm{ref}}>0$ | $\nabla J_\beta=\mathbb E[\tilde r_\theta\nabla\log\pi_\theta]$, $\tilde r_\theta=r-\beta\log\frac{\pi_\theta}{\pi_{\mathrm{ref}}}$ |
| Tương đương RLHF và DPO (Định lý 10.65) | (H1)–(H3), (H4a), (H4b); cực tiểu trên mọi hàm phần thưởng; cùng dữ liệu, $\beta$, $\pi_{\mathrm{ref}}$ | $\arg\min L^{\mathrm{DPO}}=\{\pi^*_{\hat r}\}$ |
| Gradient DPO (Mệnh đề 10.66) | $\pi_{\mathrm{ref}}$ cố định; $\beta>0$ | $-\beta\widehat{\mathbb E}[\sigma(-\Delta r_\theta)(\nabla\log\pi_\theta(y_w)-\nabla\log\pi_\theta(y_l))]$ |

Sáu hàng đầu thuộc phần giảm phương sai của bài toán trung tâm, chín hàng tiếp theo thuộc phần giới hạn bước cập nhật, năm hàng cuối thuộc phần thứ ba (Mục 7).
````

## `lecture-note.md`, dòng 2591–2609: §8.2, tiêu đề, hai hàng RLHF/DPO của bảng phương pháp, câu sau bảng và hàng DPO của bảng bảo đảm

````markdown
### 8.2 So sánh sáu phương pháp

| Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng |
|---|---|---|---|
| REINFORCE có đường cơ sở (Thuật toán 10.6) | $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_t\gamma^t(G_t-\hat v(S_t,w_{\mathrm{old}}))\psi_t$; hồi quy $\hat v$ về $G_t$ | một lượt đầy đủ của $\pi_{\mathrm{old}}$, dùng một lần | sau $E$ lượt |
| Actor–critic một bước (Thuật toán 10.9) | $\theta\leftarrow\theta+\alpha_\theta I\delta\psi$; $w\leftarrow w+\alpha_w\delta\nabla_w\hat v$ | từng bước chuyển của chính sách hiện tại, dùng một lần | sau $E$ lượt |
| TRPO (Thuật toán 10.37) | bước $\sqrt{2\kappa/(x^\top Fx)}\,x$ với $x\approx F^{-1}g$, tìm kiếm lùi | $hN$ mẫu của $\pi_{\mathrm{old}}$, một bước cập nhật | sau số vòng lặp đã định |
| PPO (Thuật toán 10.49) | bước Adam trên $L(\theta,w)$ của mỗi mini-batch | $hN$ mẫu của $\pi_{\mathrm{old}}$, $K$ epoch | sau số vòng lặp; tùy chọn dừng sớm theo approxKL |
| RLHF với PPO (Thuật toán 10.61) | khớp $\hat r$ bằng $L^{\mathrm{BT}}$; rồi Thuật toán 10.49 với phần thưởng (7.1) | $\mathcal D_{\mathrm{pref}}$; câu trả lời sinh trực tuyến bằng $\pi_{\mathrm{old}}$ | sau ngân sách số lượt |
| DPO (Thuật toán 10.67) | bước của bộ tối ưu trên $L^{\mathrm{DPO}}$ của mỗi mini-batch | $\mathcal D_{\mathrm{pref}}$ cố định, ngoại tuyến | sau số epoch đã định |

Cả sáu điều kiện dừng trong bảng là ngân sách, không phải tiêu chuẩn hội tụ. Bảng sau ghi các kết luận có bảo đảm.

| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Lặp chính sách với $\mathcal M_k$ (Hệ quả 10.29) | lợi thế, $\nu^{\pi_k}$ và phép cực đại hóa chính xác | $J$ không giảm qua các vòng |
| Bài toán miền tin cậy (Hệ quả 10.31) | nghiệm chính xác theo $\nu^{\pi_k}$ | mức giảm của $J$ không quá $\sqrt{2\kappa}\gamma\chi/(1-\gamma)^2$ |
| PPO-Clip trong mô hình của Jin, Li và Wang (Nhận xét 10.51) | MDP hữu hạn; Giả thiết 3.1, 3.2, 3.4; mô hình hai thang không Adam, không mini-batch | $\liminf_n\lVert\nabla V(\theta_{n,1})\rVert^2\le C\sqrt{\lvert\mathcal A\rvert}\limsup_n\varphi_n$ hầu chắc chắn |
| DPO (Định lý 10.65) | (H1)–(H3), (H4a), (H4b); cực tiểu trên mọi hàm phần thưởng; cùng dữ liệu, $\beta$, $\pi_{\mathrm{ref}}$ | mọi cực tiểu của $L^{\mathrm{DPO}}$ là $\pi^*_{\hat r}$, nghiệm của con đường RLHF lý tưởng |
````

## `lecture-note.md`, dòng 2613: §8.3, câu mở ("sáu phần")

````markdown
Câu trả lời cho bài toán trung tâm gồm sáu phần, mỗi phần đúng dưới một điều kiện.
````

## `lecture-note.md`, dòng 2620: §8.3, phần 6

````markdown
6. Khi phần thưởng chỉ được biết qua so sánh ưu tiên, RLHF với PPO và DPO cực đại hóa cùng mục tiêu có phạt KL theo chính sách tham chiếu cố định, có nghiệm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57). PPO nhắm tới nghiệm bằng mẫu sinh trực tuyến và bốn mô hình, không có bảo đảm hội tụ; DPO cực tiểu hóa một hàm mất mát phân loại trên dữ liệu cố định, và dưới (H1)–(H3), (H4a), (H4b) cực tiểu đó là nghiệm của con đường RLHF lý tưởng (Định lý 10.65). Với ưu tiên tất định, các hàm mất mát của cả hai con đường không có cực tiểu, và cả hai con đường lý tưởng tiến tới chính sách tất định với mọi $\beta$ (Mệnh đề 10.54(c), Nhận xét 10.69).
````

## `lecture-note.md`, dòng 2640–2651: §8.5, câu mở và bảng bài tập theo mục (có hàng Mục 7)

````markdown
Bài tập củng cố 10.1–10.12, 10.18–10.21 và 10.23 nằm ở cuối chương; bộ bài tập chính thức, Bài tập 10.13–10.17 và 10.22, nằm ở [tệp bài tập Bài 10](material-viewer.html?doc=materials/lec-10/exercises.md&deck=lecture-10-trpo-va-ppo.html). Bảng sau ghi hai loại bài tập theo mục.

| Mục | Bài tập | Tệp bài tập |
|---|---|---|
| 1. Hai giới hạn của REINFORCE | — | — |
| 2. Đường cơ sở, lợi thế, actor–critic | 10.1, 10.4, 10.5, 10.10 | 10.14 |
| 3. GAE | 10.6, 10.7 | 10.13, 10.15 |
| 4. Hàm thay thế và chặn cải thiện | 10.11 | 10.16 |
| 5. TRPO và gradient tự nhiên | 10.8, 10.9 | 10.17 |
| 6. PPO | 10.2, 10.12 | 10.14 |
| 7. Tối ưu chính sách từ phản hồi ưu tiên | 10.18, 10.19, 10.20, 10.21 | 10.22 |
| 8. Tổng kết | 10.3, 10.23 | — |
````

## `lecture-note.md`, dòng 2656: §8.6, giới hạn còn lại

````markdown
Ở Mục 2–6, giới hạn còn lại là dữ liệu theo chính sách: Mệnh đề 10.2 và 10.15 cần lượt do chính sách đang cập nhật sinh ra, và Thuật toán 10.49 bỏ mỗi đoạn thu sau $K$ epoch. Thuật toán 10.61 giữ giới hạn đó và còn phụ thuộc độ đúng của $\hat r$ trên câu trả lời mới (Nhận xét 10.62). Thuật toán 10.67 dùng dữ liệu cố định và chỉ đánh giá các câu trả lời có trong dữ liệu (Nhận xét 10.69).
````

## `lecture-note.md`, dòng 2702–2743: Tình huống 10.4 và 10.5

````markdown
::: application Tình huống 10.4 (Chọn bản tóm tắt bằng dữ liệu ưu tiên)
**Bài toán.** Một bài đăng $x$ có ba bản tóm tắt $y_1$, $y_2$, $y_3$, do $\pi_{\mathrm{ref}}=(0{,}5;\,0{,}3;\,0{,}2)$ sinh ra. Người gán nhãn thực hiện $45$ phép so sánh, $15$ cho mỗi cặp:

- cặp $(y_1,y_2)$: $10$ chọn $y_1$, $5$ chọn $y_2$;
- cặp $(y_1,y_3)$: $12$ chọn $y_1$, $3$ chọn $y_3$;
- cặp $(y_2,y_3)$: $10$ chọn $y_2$, $5$ chọn $y_3$.

Cần chính sách mới với $\beta=1$.

**Mô hình hóa.** Bài toán một bước của Định nghĩa 10.52(a) với ba hành động; dữ liệu theo Định nghĩa 10.53.

**Kiểm giả thiết.** (H1): $\pi_{\mathrm{ref}}>0$ ở cả ba bản. (H2): $\beta=1$. (H3): chính sách chọn tự do trên ba bản. (H4a), (H4b): mỗi cặp có cả hai kết quả và ba cặp nối ba bản, nên $L^{\mathrm{BT}}$ có cực tiểu, duy nhất tới một hằng.

**Tính.** Tần suất $\tfrac23$, $\tfrac45$, $\tfrac23$ bằng $\sigma(\log2)$, $\sigma(\log4)$, $\sigma(\log2)$, và $\log2+\log2=\log4$, nên $\hat r=(\log4;\,\log2;\,0)$ cực tiểu từng số hạng của $L^{\mathrm{BT}}$ (Mệnh đề 10.54(c)), do đó cực tiểu $L^{\mathrm{BT}}$, đưa nó từ $0{,}6931$ xuống $0{,}5911$. Theo Định lý 10.57, $\pi_{\mathrm{ref}}e^{\hat r}=(2;\,0{,}6;\,0{,}2)$, $\mathcal Z=2{,}8$ và $\pi^*=(\tfrac57;\,\tfrac3{14};\,\tfrac1{14})=(0{,}7143;\,0{,}2143;\,0{,}0714)$, với giá trị $\log2{,}8=1{,}0296$. Theo Định lý 10.65, DPO trên $45$ phép so sánh cho cùng chính sách.

**Diễn giải.** Bản thứ nhất được chọn với xác suất $0{,}7143$ thay cho $0{,}5$; bản thứ ba giảm còn $0{,}0714$ nhưng vẫn dương (Định lý 10.57(d)).

**Kiểm tra lại.** $\mathbb E_{\pi^*}\hat r-D_{\mathrm{KL}}(\pi^*\Vert\pi_{\mathrm{ref}})=1{,}1387-0{,}1091=1{,}0296$.

**Giới hạn.** Một lời nhắc và ba câu trả lời; với mô hình ngôn ngữ, lời giải phải đi qua Thuật toán 10.61 hoặc 10.67.
:::

::: application Tình huống 10.5 (Vi phạm giả thiết: ưu tiên tất định từ ít dữ liệu)
**Bài toán.** Lời nhắc $x$, $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\beta=1$. Phần thưởng thật là $r=(\log2;\,0)$, nên mỗi phép so sánh chọn $y_1$ với xác suất $\tfrac23$. Chỉ thu được ba phép so sánh và cả ba chọn $y_1$, một biến cố có xác suất $(\tfrac23)^3=\tfrac8{27}=0{,}2963$.

**Kiểm giả thiết.** $k=n=3$, nên (H4a) của Định lý 10.65 hỏng (Mệnh đề 10.54(c)).

**Hậu quả.** $L^{\mathrm{DPO}}=-\log\sigma\bigl(\beta(\theta_1-\theta_2-\log2)\bigr)$ giảm ngặt theo $\theta_1-\theta_2$, nên hạ gradient đẩy $\theta_1-\theta_2\to\infty$ với mọi $\beta$. Với $\beta=1$ và $J_1$ tính theo phần thưởng thật:

| $\theta_1-\theta_2$ | $\pi_\theta(y_1)$ | $L^{\mathrm{DPO}}$ | $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$ | $J_1$ |
|---|---|---|---|---|
| $2$ | $0{,}8808$ | $0{,}2395$ | $0{,}1228$ | $0{,}4878$ |
| $4$ | $0{,}9820$ | $0{,}0360$ | $0{,}3278$ | $0{,}3528$ |
| $10$ | $0{,}99995$ | $0{,}0001$ | $0{,}4050$ | $0{,}2881$ |
| $\to\infty$ | $\to1$ | $\to0$ | $\to\log\tfrac32=0{,}4055$ | $\to0{,}2877$ |

Nghiệm của bài toán thật có $J_1=0{,}5108$. KL theo chiều của mục tiêu bị chặn bởi $\log\tfrac32$; đại lượng không bị chặn là $r_\theta(y_2)=\log\frac{\pi_\theta(y_2)}{1/3}\to-\infty$. Con đường RLHF lý tưởng cũng vậy: $L^{\mathrm{BT}}$ không có cực tiểu, $\hat r(y_1)-\hat r(y_2)\to\infty$, và nghiệm có phạt KL tiến tới $(1;\,0)$ với mọi $\beta$ (Gheshlaghi Azar và cộng sự, 2024, §4.2).

**Phân tích có điều kiện.** Với mô hình phần thưởng có điều chuẩn, như điều chuẩn $\ell_2$ của Christiano và cộng sự (2017, §2.2.3), $\hat r$ hữu hạn và nghiệm có $\pi(y_2)>0$.

**Giới hạn.** Trong dữ liệu ưu tiên thật, mỗi cặp câu trả lời thường chỉ được gán nhãn một lần, nên tần suất ưu tiên thực nghiệm bằng $0$ hoặc $1$ ở hầu hết các cặp (Gheshlaghi Azar và cộng sự, 2024, §4.2, §5); khi đó (H4a), (H4b) nói chung không thỏa.
:::
````

## `lecture-note.md`, dòng 2747: Tóm tắt chương, đoạn kể lại (bản đầy đủ trước khi cắt)

````markdown
Chúng ta bắt đầu từ hai giới hạn của REINFORCE: trên bài toán một bước, tổng phương sai của ước lượng tăng từ $\tfrac49$ lên $\tfrac{16}9$ khi cộng $1$ vào mọi phần thưởng (Ví dụ 10.1); trên hành lang ngắn, ba lượt cho tọa độ thứ nhất của ước lượng bằng $-1$, $1$ và $-5{,}5$, trong khi gradient đúng có tọa độ đó bằng $2$ (Ví dụ 10.2), và một bước lớn theo đúng gradient kéo $J$ từ $-12$ xuống khoảng $-21{,}3$. Trừ một đường cơ sở giữ kỳ vọng (Mệnh đề 10.2): trên chuỗi hai trạng thái, trừ $v_\pi$ giữ trung bình $0{,}2$ của tọa độ $\theta_A$ và giảm phương sai từ $0{,}6925$ xuống $0{,}2025$ (Ví dụ 10.6); trên bài toán một bước, đường cơ sở tối ưu là $b^*=1\ne v_\pi=2$ (Mệnh đề 10.3). Critic đánh giá hành động qua mục tiêu bootstrap (Định nghĩa 10.7), với sai số TD có kỳ vọng có điều kiện bằng lợi thế khi critic đúng (Mệnh đề 10.8); critic $(1{,}4;\,1)$, đánh giá thấp $s_B$, cho $\delta_0=-0{,}5$ dù lợi thế bằng $0{,}4$ (Ví dụ 10.7). GAE trộn các ước lượng $n$ bước bằng trọng số $(\gamma\lambda)^k$; với critic đó và $\lambda=0{,}5$, độ lệch là $-0{,}45$, thay cho $-0{,}9$ của ước lượng một bước, và khoảng cách giữa hai lượt là $1{,}35$, thay cho $2{,}7$ của hệ số Monte Carlo (Ví dụ 10.8); GAE không làm chệch gradient khi $\lambda=1$ với lượt đầy đủ hoặc khi critic đúng (Mệnh đề 10.14, 10.15). Trên chuỗi hai trạng thái, bổ đề hiệu hiệu năng cho $\Delta J=0{,}296$ còn hàm thay thế cho $0{,}26$; với bước tới $(1;\,0{,}5)$, hàm thay thế báo tăng $0{,}175$ trong khi $J$ giảm $0{,}05$ (Ví dụ 10.11, Bổ đề 10.19, Mệnh đề 10.22), và Định lý 10.26 chặn sai số này theo khoảng cách TV trung bình, dẫn tới bài toán miền tin cậy (Định nghĩa 10.30, Hệ quả 10.31). TRPO giải bài toán đó xấp xỉ bằng gradient tự nhiên và gradient liên hợp (Mệnh đề 10.34, Thuật toán 10.37), còn PPO thay ràng buộc bằng mục tiêu cắt, một chặn dưới của hàm thay thế mẫu (Mệnh đề 10.41, Thuật toán 10.49); trên chuỗi hai trạng thái, với bộ đệm hai lượt có lợi thế ước lượng sai dấu, phép cắt giữ mức giảm của $J$ ở $0{,}008$ thay cho $0{,}4$ (Mục 6.1). PPO cũng có thể thay ràng buộc bằng phạt KL với hệ số thích nghi (Định nghĩa 10.43). Không phương pháp thực hành nào giữ được bảo đảm đơn điệu, và kết quả hội tụ hiện có cho PPO-Clip chỉ nói về điểm dừng của một mô hình đơn giản hóa (Nhận xét 10.51). Khi phần thưởng chỉ được biết qua so sánh ưu tiên, mô hình Bradley–Terry cho mô hình phần thưởng bằng hợp lý cực đại (Mệnh đề 10.54), và mục tiêu có phạt KL theo chính sách tham chiếu cố định có nghiệm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57). RLHF với PPO nhắm tới nghiệm đó bằng mẫu sinh trực tuyến (Thuật toán 10.61), DPO giải cùng mục tiêu bằng một hàm mất mát phân loại trên dữ liệu cố định, không qua vòng học tăng cường (Thuật toán 10.67), và dưới các giả thiết của Định lý 10.65 cực tiểu của DPO là nghiệm của con đường RLHF lý tưởng.
````

## `lecture-note.md`, dòng 2756: Tóm tắt chương, gạch đầu dòng Mục 7

````markdown
- Mục 7: Định nghĩa 10.52 (bài toán sinh câu trả lời), Định nghĩa 10.53 (mô hình Bradley–Terry), Mệnh đề 10.54 (hợp lý cực đại), Nhận xét 10.55 (chuẩn hóa), Định nghĩa 10.56 (mục tiêu có phạt KL), Định lý 10.57 (nghiệm dạng đóng), Nhận xét 10.58 (hai mỏ neo), Bổ đề 10.59 (KL theo token), Mệnh đề 10.60 (gradient có phạt KL), Thuật toán 10.61 (RLHF với PPO), Nhận xét 10.62 (tối ưu quá mức), Mệnh đề 10.63 (đổi biến), Định nghĩa 10.64 (mất mát DPO), Định lý 10.65 (tương đương), Mệnh đề 10.66 (gradient DPO), Thuật toán 10.67 (DPO), Nhận xét 10.68–10.70 (đọc kết quả, giới hạn, biến thể).
````

## `lecture-note.md`, dòng 2783–2785: Công thức cần nhớ, hai công thức của Mục 7

````markdown
&\pi^*_r(y\mid x)\propto\pi_{\mathrm{ref}}(y\mid x)\,e^{r(x,y)/\beta},\\
&L^{\mathrm{DPO}}=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\log\sigma\Bigl(\beta\log\tfrac{\pi_\theta(y_w\mid x)}{\pi_{\mathrm{ref}}(y_w\mid x)}\\
&\quad-\beta\log\tfrac{\pi_\theta(y_l\mid x)}{\pi_{\mathrm{ref}}(y_l\mid x)}\Bigr).
````

## `lecture-note.md`, dòng 2799–2800: Giả thiết hay bị bỏ quên, hai gạch đầu dòng của Mục 7

````markdown
- Định lý 10.65 cần $L^{\mathrm{BT}}$ có cực tiểu để hai con đường có nghiệm, và tập cực tiểu là một lớp để nghiệm duy nhất: với ưu tiên tất định, cả hai con đường suy biến; với dữ liệu không nối mọi câu trả lời, nghiệm không duy nhất.
- $\pi_{\mathrm{old}}$ của PPO đổi sau mỗi vòng và chỉ giới hạn từng bước; $\pi_{\mathrm{ref}}$ cố định và quyết định nghiệm cuối.
````

## `lecture-note.md`, dòng 2806: Bài tập củng cố, câu phủ mục tiêu

````markdown
Các bài phủ chín mục tiêu học tập: mục tiêu 1 (Bài tập 10.1, 10.4), 2 (10.5, 10.10), 3 (10.6, 10.7), 4 (10.11, 10.23), 5 (10.3, 10.8, 10.9, 10.11), 6 (10.2, 10.12, 10.23), 7 (10.2, 10.3, 10.12), 8 (10.18, 10.19, 10.21), 9 (10.19, 10.20).
````

## `lecture-note.md`, dòng 3112–3198: Bài tập củng cố 10.18–10.21 (Mục 7), nguyên văn

````markdown
::: exercise Bài tập 10.18 (Nghiệm có phạt KL trên ba câu trả lời)
Một lời nhắc, ba câu trả lời, $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, phần thưởng $r=(\log2;\,0;\,0)$.

- (a) Với $\beta=1$, tính $\mathcal Z$, $\pi^*$, $\max J_1$, và kiểm bằng $\mathbb E_{\pi^*}r-D_{\mathrm{KL}}(\pi^*\Vert\pi_{\mathrm{ref}})$.
- (b) Tính phần thưởng ngầm định $\beta\log(\pi^*/\pi_{\mathrm{ref}})$ và chỉ ra nó thuộc $[r]$.
- (c) Lặp lại (a) với $\beta=\tfrac12$.
:::

::: hint
Theo Định lý 10.57, $\pi^*$ tỉ lệ với $\pi_{\mathrm{ref}}e^{r/\beta}$; hằng chuẩn hóa là tổng có trọng số $\pi_{\mathrm{ref}}$.
:::

::: solution
**Câu (a).** $\pi_{\mathrm{ref}}e^{r}=(1;\,\tfrac14;\,\tfrac14)$, $\mathcal Z=\tfrac32$, $\pi^*=(\tfrac23;\,\tfrac16;\,\tfrac16)$, $\max J_1=\log\tfrac32=0{,}4055$. Kiểm: $\mathbb E_{\pi^*}r=\tfrac23\log2=0{,}4621$, $D_{\mathrm{KL}}=\tfrac23\log\tfrac43+2\cdot\tfrac16\log\tfrac23=0{,}1918-0{,}1352=0{,}0566$, và $0{,}4621-0{,}0566=0{,}4055$.

**Câu (b).** $(\log\tfrac43;\,\log\tfrac23;\,\log\tfrac23)=(0{,}2877;\,-0{,}4055;\,-0{,}4055)=r-\log\tfrac32$, hơn kém $r$ một hằng của lời nhắc (Định lý 10.57(c)).

**Câu (c).** $\pi_{\mathrm{ref}}e^{2r}=(2;\,\tfrac14;\,\tfrac14)$, $\mathcal Z=\tfrac52$, $\pi^*=(0{,}8;\,0{,}1;\,0{,}1)$, $\max J_{1/2}=\tfrac12\log\tfrac52=0{,}4581$.

**Kiểm tra lại.** Chuẩn hóa bằng $\sum_ye^{r(y)/\beta}$ thay cho $\sum_y\pi_{\mathrm{ref}}(y)e^{r(y)/\beta}$ cho $(\tfrac12;\,\tfrac14;\,\tfrac14)$ ở (a). Dùng $e^{\beta r}$ thay cho $e^{r/\beta}$ ở (c) cho $\pi^*(y_1)=0{,}5858$, sai chiều tác dụng của $\beta$.
:::

::: exercise Bài tập 10.19 (Hàm mất mát DPO với hai câu trả lời)
Chính sách softmax với đặc trưng đơn vị trên hai câu trả lời; $\pi_{\mathrm{ref}}$ có $\theta_{\mathrm{ref}}=(\log2;\,0)$, tức $(\tfrac23;\,\tfrac13)$; $n$ phép so sánh giữa $y_1$ và $y_2$, trong đó $k$ phép chọn $y_1$.

- (a) Chứng minh: nếu $0<k<n$, $L^{\mathrm{DPO}}$ đạt cực tiểu khi và chỉ khi $\beta(\theta_1-\theta_2-\log2)=\log\frac k{n-k}$, và chính sách đó là $\pi^*_{\hat r}$ của con đường RLHF.
- (b) Với $n=5$, $k=4$, $\beta=1$: tính chính sách cực tiểu, gradient tại $\theta_{\mathrm{ref}}$, và chính sách sau một bước hạ gradient với bước học $1$.
- (c) Với $k=n$: chứng minh $L^{\mathrm{DPO}}$ không có cực tiểu.
:::

::: hint
Với bộ ba chọn $y_1$, $\Delta r_\theta=\beta(\theta_1-\theta_2-\log2)$; áp dụng Mệnh đề 10.54(c) với $\Delta r_\theta$ thay cho $\Delta\hat r$.
:::

::: solution
**Câu (a).** $L^{\mathrm{DPO}}=-\tfrac1n\bigl[k\log\sigma(\Delta r_\theta)+(n-k)\log\sigma(-\Delta r_\theta)\bigr]$ có đạo hàm theo $\Delta r_\theta$ là $\sigma(\Delta r_\theta)-\tfrac kn$, và $\Delta r_\theta$ tăng ngặt theo $\theta_1-\theta_2$ vì $\beta>0$; cực tiểu duy nhất tại $\Delta r_\theta=\log\frac k{n-k}$, cho $\pi(y_1)/\pi(y_2)=e^{\theta_1-\theta_2}=2\bigl(\frac k{n-k}\bigr)^{1/\beta}$. Con đường RLHF cho $\hat r(y_1)-\hat r(y_2)=\log\frac k{n-k}$ (Mệnh đề 10.54(c)) và $\pi^*_{\hat r}(y_1)/\pi^*_{\hat r}(y_2)=2\,e^{(\hat r(y_1)-\hat r(y_2))/\beta}$, cùng tỉ số.

**Câu (b).** $\Delta r_\theta=\log4$, $\theta_1-\theta_2=\log8$, $\pi=(\tfrac89;\,\tfrac19)$. Theo Mệnh đề 10.66 với trọng số $\sigma(0)=\tfrac12$ và $\psi(y_1)-\psi(y_2)=(1;\,-1)$, gradient là $-\bigl[\tfrac45\cdot\tfrac12-\tfrac15\cdot\tfrac12\bigr](1;\,-1)=(-0{,}3;\,0{,}3)$. Sau một bước, $\theta_1-\theta_2=\log2+0{,}6=1{,}2931$, $\pi_\theta(y_1)=0{,}7847$, và $L^{\mathrm{DPO}}$ giảm từ $0{,}6931$ xuống $0{,}5575$; giá trị cực tiểu là $0{,}5004$.

**Câu (c).** Với $k=n$, $L^{\mathrm{DPO}}=-\log\sigma(\Delta r_\theta)>0$, giảm ngặt theo $\theta_1-\theta_2$ và tiến về $0$ khi $\theta_1-\theta_2\to\infty$.

**Kiểm tra lại.** Quên $\log\pi_{\mathrm{ref}}$ cho cực tiểu $\theta_1-\theta_2=\log4$, tức $\pi=(0{,}8;\,0{,}2)$ ở (b). Nhầm dấu trọng số cho gradient $(0{,}3;\,-0{,}3)$, làm giảm $\pi(y_1)$.
:::

::: exercise Bài tập 10.20 (Dữ liệu không phủ một câu trả lời)
Ba câu trả lời, $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, $\beta=1$; $\mathcal D_{\mathrm{pref}}$ gồm sáu phép so sánh chỉ giữa $y_1$ và $y_2$, bốn chọn $y_1$; lớp chính sách gồm mọi phân phối có miền hỗ trợ đầy đủ.

- (a) Chứng minh mọi chính sách có $\pi(y_1)=4\pi(y_2)$ đều cực tiểu $L^{\mathrm{DPO}}$.
- (b) Tính $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ cho ba cực tiểu $(\tfrac23;\,\tfrac16;\,\tfrac16)$, $(0{,}6;\,0{,}15;\,0{,}25)$, $(0{,}4;\,0{,}1;\,0{,}5)$.
- (c) Con đường RLHF có $\hat r(y_1)-\hat r(y_2)=\log2$, còn $c=\hat r(y_3)-\hat r(y_2)$ không được dữ liệu xác định. Viết $\pi^*_{\hat r}$ theo $c$, chỉ ra giả thiết nào của Định lý 10.65 hỏng, và chứng minh tập nghiệm của hai con đường bằng nhau.
:::

::: hint
$\Delta r_\theta$ chỉ phụ thuộc tỉ số $\pi(y_1)/\pi(y_2)$; ở (c), cho $c$ chạy trên $\mathbb R$.
:::

::: solution
**Câu (a).** Bộ ba chọn $y_1$ có $\Delta r_\theta=\log\frac{\pi(y_1)}{1/2}-\log\frac{\pi(y_2)}{1/4}=\log\frac{\pi(y_1)}{2\pi(y_2)}$. Theo Mệnh đề 10.54(c) với $n=6$, $k=4$, cực tiểu đạt khi $\Delta r_\theta=\log2$, tức $\pi(y_1)=4\pi(y_2)$; $\pi(y_3)$ không xuất hiện.

**Câu (b).** $0{,}0566$; $0{,}0328$; $0{,}1657$.

**Câu (c).** $\pi^*_{\hat r}\propto(1;\,\tfrac14;\,\tfrac14e^c)$: $c=0$ cho $(\tfrac23;\,\tfrac16;\,\tfrac16)$, $c=\log2$ cho $(\tfrac47;\,\tfrac17;\,\tfrac27)$, $c=-\log2$ cho $(\tfrac8{11};\,\tfrac2{11};\,\tfrac1{11})$. (H4a) thỏa, (H4b) hỏng: tập cực tiểu của $L^{\mathrm{BT}}$ gồm mọi $\hat r$ có $\hat r(y_1)-\hat r(y_2)=\log2$, với $c$ tùy ý, nên không là một lớp. Mọi $\pi^*_{\hat r}$ có $\pi(y_1)=4\pi(y_2)$; ngược lại, mỗi cực tiểu $\pi$ của $L^{\mathrm{DPO}}$ là $\pi^*_{\hat r}$ với $c=\log\frac{\pi(y_3)}{\pi(y_2)}$. Hai tập nghiệm bằng nhau và không có nghiệm duy nhất.

**Kiểm tra lại.** Kết luận "DPO cho $\pi(y_3)=\pi_{\mathrm{ref}}(y_3)$" sai vì $L^{\mathrm{DPO}}$ không chứa $\pi(y_3)$. Kết luận "hai con đường cho nghiệm khác nhau" sai: tập nghiệm trùng nhau, chỉ không duy nhất.
:::

::: exercise Bài tập 10.21 (Hai mỏ neo khi bán kính cắt nhỏ)
Như Ví dụ 10.27 nhưng với $\epsilon=0{,}1$: $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$, $\beta=1$. Mỗi vòng tính phần thưởng đã trừ KL tại $\pi_{\mathrm{old}}$ và lợi thế đúng, giữ cố định; bộ đệm có đúng tần suất của $\pi_{\mathrm{old}}$; vòng trong tăng $\mathcal L^{\mathrm{CLIP}}$ từ $\pi_{\mathrm{old}}$ tới đầu đoạn phẳng, nơi mọi mẫu có gradient khác $0$ đều đã bị cắt.

- (a) Tính $p=\pi(y_1)$ sau vòng 1, 2, 3 và lợi thế của mỗi vòng.
- (b) So $J_1$ tại các chính sách đó với $\max J_1=0{,}5108$.
- (c) Giải thích vì sao dãy không dừng ở $p=0{,}8$.
:::

::: hint
Với $p_{\mathrm{old}}>\tfrac12$: khi lợi thế của $y_1$ dương, vòng dừng ở $p=1{,}1\,p_{\mathrm{old}}$; khi âm, ở $p=0{,}9\,p_{\mathrm{old}}$.
:::

::: solution
**Câu (a).** Vòng 1, $p_{\mathrm{old}}=\tfrac23$: phần thưởng đã trừ KL $(\log2;\,0)$, lợi thế $(0{,}2310;\,-0{,}4621)$, $p=0{,}7333$. Vòng 2: phần thưởng $(\log2-\log1{,}1;\,-\log0{,}8)=(0{,}5978;\,0{,}2231)$, lợi thế $(0{,}0999;\,-0{,}2748)$, $p=1{,}1\cdot0{,}7333=0{,}8067$. Vòng 3: phần thưởng $(0{,}5025;\,0{,}5447)$, lợi thế $(-0{,}0082;\,0{,}0340)$, $p=0{,}9\cdot0{,}8067=0{,}7260$.

**Câu (b).** $J_1=0{,}4979$; $0{,}5107$; $0{,}4950$, đều dưới $0{,}5108$.

**Câu (c).** Phép cắt chỉ chặn độ dài bước so với $\pi_{\mathrm{old}}$. Dấu của lợi thế, do $\pi_{\mathrm{ref}}$ và $\hat r$ quyết định qua phần thưởng đã trừ KL, đổi khi $p$ vượt $0{,}8$, nhưng mỗi vòng vẫn đi hết tới biên khoảng cắt, nên dãy dao động quanh $0{,}8$; vòng 4 cho $p=0{,}7986$.

**Kiểm tra lại.** Tính phần thưởng đã trừ KL theo $\pi_{\mathrm{ref}}$ thay cho $\pi_{\mathrm{old}}$ bỏ mất phạt KL, nên lợi thế của $y_1$ luôn dương và $p$ tiếp tục tăng. Cắt theo $\pi_{\mathrm{ref}}$ thay cho $\pi_{\mathrm{old}}$ cho $p$ dừng ở $0{,}7333$.
:::
````

## `lecture-note.md`, dòng 3236: Hướng dẫn đọc thêm (các câu về Mục 7)

````markdown
**Hướng dẫn đọc thêm.** Sutton và Barto (2018), §13.4–13.5, trình bày đường cơ sở và actor–critic một bước với hộp giả mã mà Thuật toán 10.6 và 10.9 dựa vào; §7.1 và §12.1–12.3 trình bày lợi tức $n$ bước và lợi tức λ, cơ sở của Mục 3. Các phần TRPO, GAE, PPO không có trong sách; đọc Schulman và cộng sự (2015, §2–3, Phụ lục C), (2016, §2–3) và (2017, §3–5). Chặn cải thiện dạng trung bình theo Achiam và cộng sự (2017, §5, phụ lục); chi tiết cài đặt theo Huang và cộng sự (2022) và Engstrom và cộng sự (2020). Mục 7 dựa vào Rafailov và cộng sự (2023, §3–5, Phụ lục A); quy trình RLHF theo Ouyang và cộng sự (2022, §3) và Stiennon và cộng sự (2020, §3.4). Định lý 10.65 ghép Định lý 1 và Mệnh đề 1 của Rafailov và cộng sự (2023, Phụ lục A.6), nửa đầu chứng minh Định lý 4.1 của Xu và cộng sự (2024) và Mệnh đề 4 của Gheshlaghi Azar và cộng sự (2024, Phụ lục B).
````

## `lecture-note.md`, dòng 3240: Tài liệu tham khảo 1 (dòng phân trang, có Mục 8)

````markdown
1. Tạ Việt Cường. *Lecture 10: Overview on Policy Gradient Algorithms, Part 1* (lecture10_policy_gradient_part2.pdf, 43 trang), học phần AIT3007, 2025–2026. Mục 1: tr. 3–4, 9–10, 14; Mục 2: tr. 5, 8, 11–13; Mục 3: tr. 13, 24; Mục 4: tr. 4, 14–16; Mục 5: tr. 17–19; Mục 6: tr. 19–42; Mục 8: tr. 2–3, 28, 43.
````

## `lecture-note.md`, dòng 3257–3264: Tài liệu tham khảo 18–25

````markdown
18. Rafailov, R., Sharma, A., Mitchell, E., Ermon, S., Manning, C. D., Finn, C. "Direct Preference Optimization: Your Language Model is Secretly a Reward Model." *NeurIPS* 2023 (arXiv 2305.18290). §3–6, (1)–(7), Định nghĩa 1, Bổ đề 1–2, Định lý 1, Phụ lục A.1–A.6, B: Mục 7.1–7.6.
19. Ouyang, L. và cộng sự. "Training language models to follow instructions with human feedback." *NeurIPS* 2022 (arXiv 2203.02155). §3.1, §3.5, (1)–(2), Phụ lục C.4: Mục 7.1–7.3.
20. Stiennon, N., Ouyang, L., Wu, J., Ziegler, D. M., Lowe, R., Voss, C., Radford, A., Amodei, D., Christiano, P. "Learning to summarize from human feedback." *NeurIPS* 2020 (arXiv 2009.01325). §3.4, §4.3, Hình 5: Mục 7.1–7.3.
21. Ziegler, D. M., Stiennon, N., Wu, J., Brown, T. B., Radford, A., Amodei, D., Christiano, P., Irving, G. "Fine-Tuning Language Models from Human Preferences." arXiv 1909.08593, 2019. §2, (2), §2.2: Mục 7.1–7.3.
22. Christiano, P. F., Leike, J., Brown, T. B., Martic, M., Legg, S., Amodei, D. "Deep Reinforcement Learning from Human Preferences." *NIPS* 2017 (arXiv 1706.03741). §2.2.3: Tình huống 10.5.
23. Gheshlaghi Azar, M., Guo, Z. D., Piot, B., Munos, R., Rowland, M., Valko, M., Calandriello, D. "A General Theoretical Paradigm to Understand Learning from Human Preferences." *AISTATS* 2024, PMLR 238 (arXiv 2310.12036; mục và số phương trình theo bản arXiv v2). Mệnh đề 4, §4.2, §5, (17), Phụ lục B: Mục 7.1, 7.4–7.6, Tình huống 10.5.
24. Xu, S., Fu, W., Gao, J., Ye, W., Liu, W., Mei, Z., Wang, G., Yu, C., Wu, Y. "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study." *ICML* 2024, PMLR 235 (arXiv 2404.10719). Định lý 4.1, Bảng 1, §5–6: Mục 7.4–7.6.
25. Rafailov, R., Hejna, J., Park, R., Finn, C. "From $r$ to $Q^*$: Your Language Model is Secretly a Q-Function." *COLM* 2024 (arXiv 2404.12358). §3.1, Định lý 1, §5.4, (16): Mục 7.4, 7.6.
````

## `exercises.md`, dòng 1–3: Tiêu đề và đoạn mở

````markdown
# Bài tập Bài 10 — TRPO, PPO và DPO

Tệp gồm sáu bài, Bài tập 10.13–10.17 và 10.22, dùng chung bộ đếm với mười bảy bài tập của [ghi chú bài giảng](material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html) (Bài tập 10.1–10.12, 10.18–10.21 và 10.23) và không lặp đề bài nào của ghi chú. Mọi bài lấy từ bài tập của Sutton và Barto (2018), ghi số bài, mục và trang. Các bài chia theo hai mức: nhận biết (10.13, 10.22); tính toán hoặc chứng minh (10.14–10.17). Mục tiêu học tập 8 dựa vào Bài tập 10.22 cùng Bài tập 10.18, 10.19, 10.21 của ghi chú; mục tiêu học tập 9 dựa vào Bài tập 10.19, 10.20 của ghi chú. Bảng dưới xếp bài của tệp này và bài của ghi chú theo mạch của bộ trang chiếu; bài của ghi chú đứng sau chữ "ghi chú".
````

## `exercises.md`, dòng 12–13: Bảng mạch, hàng mạch 6 và 7

````markdown
| 6. Học từ so sánh của người | [Mở phần](lecture-10-trpo-va-ppo.html#/6/1) | 10.22; ghi chú: 10.18–10.21 |
| 7. Tổng kết | [Mở phần](lecture-10-trpo-va-ppo.html#/7/1) | ghi chú: 10.3, 10.23 |
````

## `exercises.md`, dòng 25: Hướng dẫn và ký hiệu, đoạn về Bài tập 10.22

````markdown
Bài tập 10.22 xét phân phối softmax trên hai hành động. *Mức ưu tiên* (action preference) của hành động $a$ tại bước $t$ viết $h_t(a)$, vì chữ $H_t$ đã dành cho lịch sử; sách viết $H_t(a)$. Hàm logistic là $\sigma(z)=1/(1+e^{-z})$, như bảng ký hiệu và Mục 7.1 của ghi chú; chữ $\sigma$ có nghĩa này trong Bài tập 10.22, còn trong Bài tập 10.17, $\sigma(s,\theta)$ là độ lệch chuẩn của chính sách Gaussian. Ở Bài tập 10.22, như Mục 7 của ghi chú, $\log$ chỉ logarit tự nhiên.
````

## `exercises.md`, dòng 62–88: Bài tập 10.22 (Sutton và Barto, Bài tập 2.9), bản trước khi bỏ đoạn liên hệ Bradley–Terry

````markdown
### Bài tập 10.22. Softmax hai hành động và hàm logistic

**Mức độ:** nhận biết; mục tiêu học tập 8; mạch 7.

**Nguồn:** Sutton và Barto (2018), Bài tập 2.9, §2.8, trang 37; phân phối softmax (2.11), cùng trang.

::: exercise Bài tập 10.22 (Softmax hai hành động và hàm logistic)
Trong bài toán chọn lặp lại một bước (multi-armed bandit) với tập hành động hữu hạn $\mathcal A$, mỗi hành động $a$ có một mức ưu tiên $h_t(a)\in\mathbb R$ tại bước $t$, và hành động $A_t$ được chọn theo phân phối softmax (2.11) của sách:
$$\begin{aligned}&\Pr(A_t=a)=\pi_t(a)\\&\quad=\frac{e^{h_t(a)}}{\sum_{a'\in\mathcal A}e^{h_t(a')}}.\end{aligned}$$
Hàm logistic là $\sigma(z)=1/(1+e^{-z})$, $z\in\mathbb R$. Chứng minh rằng khi chỉ có hai hành động, phân phối softmax trùng với phân phối cho bởi hàm logistic, còn gọi là hàm sigmoid (sigmoid function), thường dùng trong thống kê và trong mạng nơ-ron nhân tạo.
:::

::: hint Gợi ý Bài tập 10.22
Chia tử và mẫu của $\pi_t(a_1)$ cho $e^{h_t(a_1)}$.
:::

::: solution Lời giải Bài tập 10.22
**Softmax hai hành động là hàm logistic.** Viết $\mathcal A=\{a_1,a_2\}$ và đặt $z_t=h_t(a_1)-h_t(a_2)$. Chia tử và mẫu của (2.11) cho $e^{h_t(a_1)}>0$:
$$\begin{aligned}\pi_t(a_1)&=\frac{e^{h_t(a_1)}}{e^{h_t(a_1)}+e^{h_t(a_2)}}\\&=\frac1{1+e^{-(h_t(a_1)-h_t(a_2))}}\\&=\sigma(z_t).\end{aligned}$$
Chia cho $e^{h_t(a_2)}$ theo cách tương tự được $\pi_t(a_2)=\sigma(-z_t)$. Vì $\sigma(-z)=\dfrac{e^{-z}}{e^{-z}+1}=1-\sigma(z)$, ta được $\pi_t(a_2)=1-\sigma(z_t)$. Vậy với hai hành động, phân phối softmax chọn $a_1$ với xác suất $\sigma(z_t)$ và $a_2$ với xác suất $1-\sigma(z_t)$, tức phân phối cho bởi hàm logistic của hiệu hai mức ưu tiên. Chỉ hiệu $z_t$ xuất hiện, nên cộng cùng một hằng vào hai mức ưu tiên không đổi phân phối.

**Mọi phân phối trên hai hành động là softmax.** Vì $\sigma'(z)=\sigma(z)\bigl(1-\sigma(z)\bigr)>0$, $\sigma(z)\to0$ khi $z\to-\infty$ và $\sigma(z)\to1$ khi $z\to+\infty$, nên $\sigma$ là song ánh tăng ngặt từ $\mathbb R$ lên $(0,1)$, với hàm ngược $\sigma^{-1}(p)=\log\frac p{1-p}$. Mỗi phân phối trên hai hành động có $\pi_t(a_1)=p\in(0,1)$ là một phân phối softmax, với hiệu mức ưu tiên $z_t=\log\frac p{1-p}$.

**Liên hệ với mô hình Bradley–Terry.** Với chính sách softmax có đặc trưng đơn vị trên hai câu trả lời $y_1$, $y_2$, logit $\theta=(\theta_1;\,\theta_2)$ là mức ưu tiên, và kết quả trên cho $\pi_\theta(y_1)=\sigma(\theta_1-\theta_2)$, đẳng thức dùng ở bước cập nhật của Ví dụ 10.28. Thay mức ưu tiên bằng phần thưởng $r(x,\cdot)$ của hai câu trả lời được đẳng thức của mô hình Bradley–Terry, $\frac{e^{r(x,y)}}{e^{r(x,y)}+e^{r(x,y')}}=\sigma\bigl(r(x,y)-r(x,y')\bigr)$ (Định nghĩa 10.53). Cộng một hằng vào hai mức ưu tiên ứng với Mệnh đề 10.54(b): cộng vào phần thưởng một hàm $f(x)$ chỉ phụ thuộc lời nhắc thì $L^{\mathrm{BT}}$ không đổi. Hiệu phần thưởng tối ưu $\log\frac k{n-k}$ của Mệnh đề 10.54(c) là $\sigma^{-1}(\tfrac kn)$.

**Kiểm tra lại.** Với $h_t=(\log2;\,0)$, (2.11) cho $\pi_t(a_1)=\tfrac{2}{2+1}=\tfrac23$, và $\sigma(\log2)=1/(1+\tfrac12)=\tfrac23$; đây là $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ của Ví dụ 10.23. Ba lỗi thường gặp: nhầm dấu của hiệu, viết $\pi_t(a_1)=\sigma\bigl(h_t(a_2)-h_t(a_1)\bigr)$, cho $\tfrac13$ thay cho $\tfrac23$; áp $\sigma$ cho từng mức ưu tiên rồi chuẩn hóa, $\sigma\bigl(h_t(a_1)\bigr)/\bigl[\sigma\bigl(h_t(a_1)\bigr)+\sigma\bigl(h_t(a_2)\bigr)\bigr]$, cho $\tfrac{2/3}{2/3+1/2}=\tfrac47\approx0{,}5714$; và viết $\pi_t(a_1)=\sigma\bigl(h_t(a_1)\bigr)$, chỉ đúng khi $h_t(a_2)=0$: với $h_t=(\log2;\,\log2)$, cách viết này cho $\tfrac23$ thay cho $\tfrac12$.
:::
````

## `exercises.md`, dòng 318: Tài liệu tham khảo

````markdown
- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. Bài tập 2.9 và (2.11), §2.8, trang 37 (Bài tập 10.22); Bài tập 5.13 và (5.11)–(5.14), §5.9, trang 114–115 (Bài tập 10.16); (6.6), §6.1, trang 121 (Bài tập 10.15); Bài tập 7.6, (7.13) và (7.14), §7.4, trang 150–151 (Bài tập 10.14); Bài tập 12.2 và (12.3), §12.1, trang 290 (Bài tập 10.13); Bài tập 12.3, §12.2, trang 295, cùng (12.4), trang 290, và (12.6), trang 293 (Bài tập 10.15); Bài tập 13.4, (13.19) và (13.20), §13.7, trang 335–336 (Bài tập 10.17).
````
