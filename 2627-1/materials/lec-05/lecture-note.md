# Bài 05 — Dự đoán phi mô hình: Monte Carlo và Sai phân thời gian (TD)

## Mục tiêu và kiến thức tiên quyết

- Phân biệt giá trị thật $v_\pi$, ước lượng $V_t$, phần thưởng tích lũy $G_t$, đích TD $Y_t^{\mathrm{TD}}$ và sai số TD $\delta_t$.
- Thực hiện được Monte Carlo (MC) lần ghé đầu và TD(0) dạng bảng, tính tay trên ví dụ đi bộ ngắn hai lượt.
- Nêu điều kiện hội tụ của MC và TD(0) đi cùng giả thiết; giải thích cơ chế chệch–phương sai có điều kiện, không xếp hạng phổ quát.
- Kiến thức tiên quyết: MDP, phương trình Bellman, đánh giá chính sách bằng quy hoạch động (Bài 04); luật số lớn ở mức đại học năm nhất.

## Bản đồ chủ đề

Mười lăm topic với bốn nhãn bắt buộc: **cốt lõi** = 01, 02, 03, 04, 06, 07, 08, 09, 12, 13, 15; **cầu nối** = 05, 10, 11; **bổ sung** = 14; **đọc thêm** = ôn MDP và quy hoạch động từ nguồn tr. 1–14 cùng các mục tài liệu tham khảo cuối note, không có note ID. Bốn nhóm mạch: **Đặt bài** (topic 01), **Monte Carlo** (02–06), **TD(0)** (07–11), **So sánh và tổng hợp** (12–15).

### lec-05-topic-01 — Bài toán dự đoán phi mô hình và giả thiết

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: đặt phạm vi toàn bài — chính sách cố định, mô hình chưa biết, học từ quỹ đạo lấy mẫu.
- Kết nối vào: MDP, phương trình Bellman và đánh giá chính sách của Bài 04.
- Kết nối ra: mọi chủ đề sau đều học cùng đích $v_\pi$ dưới cùng giả thiết.
- Nguồn: tr. 15–16; slide P00–P02.

### lec-05-topic-02 — Lượt, trạng thái kết thúc, phần thưởng tích lũy $G_t$

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: định nghĩa đại lượng học của MC trước mọi thuật toán.
- Kết nối vào: giả thiết theo lượt và $V(\text{kết thúc})=0$ của topic 01.
- Kết nối ra: thuật toán MC lần ghé đầu (topic 03) dùng $G_t$ làm đích.
- Nguồn: tr. 17, 20; slide A00–A01.

### lec-05-topic-03 — MC lần ghé đầu và thuật toán

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: biến đích $G_t$ thành thuật toán tái tạo được với giao diện đầy đủ.
- Kết nối vào: $G_t$ của topic 02.
- Kết nối ra: tính tay hai lượt (topic 04) và hai trục thiết kế (topic 06).
- Nguồn: tr. 18, 21; slide A02.

### lec-05-topic-04 — Ví dụ đi bộ ngắn hai lượt, tính tay

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: kiểm tra thuật toán bằng số cụ thể trước khi nói hội tụ.
- Kết nối vào: thuật toán topic 03 với $V_0(S)=V_0(x)=0$, $\gamma=1$.
- Kết nối ra: đối chiếu giá trị chuẩn đối chiếu (topic 05) và so với TD (topic 09).
- Nguồn: tr. 20–22; slide A03.

### lec-05-topic-05 — Giá trị chuẩn $11/21$, $19/21$ và điều kiện kỳ vọng

- Nhóm: `cầu nối`.
- Vai trò trong mạch: giá trị chuẩn đối chiếu đo sai số sau ước lượng, không phải đầu vào của thuật toán.
- Kết nối vào: kết quả $(0,0)$ của topic 04.
- Kết nối ra: đặt nền cho câu hỏi "khi nào trung bình hội tụ" (topic 06, 11).
- Nguồn: tr. 19; slide A04.

### lec-05-topic-06 — Hai trục MC: lần ghé đầu/mọi lần ghé và trung bình mẫu/$\alpha$ hằng

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: tách quy tắc lấy mẫu khỏi quy tắc bước học — hai lựa chọn độc lập.
- Kết nối vào: thuật toán topic 03 và ví dụ topic 04.
- Kết nối ra: điều kiện hội tụ của trung bình mẫu (topic 11) và bài tập hw05 Bài 5.
- Nguồn: tr. 18, 20–23; slide A05–A08.

### lec-05-topic-07 — Chuyển mẫu, đích TD, delta

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: mở sang TD — một chuyển tiếp đủ để tạo đích học.
- Kết nối vào: chuyển mẫu $(S_t,R_{t+1},S_{t+1})$ của topic 01; $G_t$ của topic 02 làm đối chiếu.
- Kết nối ra: thuật toán TD(0) (topic 08).
- Nguồn: tr. 16, 24–25; slide B00–B01.

### lec-05-topic-08 — Thuật toán TD(0)

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: giao diện đầy đủ của TD(0) dạng bảng với lịch bước học $\alpha_n(s)$.
- Kết nối vào: đích và sai số của topic 07.
- Kết nối ra: tính tay cùng ví dụ (topic 09) và kỳ vọng cập nhật (topic 10).
- Nguồn: tr. 24–25; slide B02.

### lec-05-topic-09 — Cập nhật TD tính tay cùng ví dụ

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: cùng hai lượt, cùng $\alpha=0{,}5$, cùng khởi tạo — khác biệt chỉ còn cơ chế cập nhật.
- Kết nối vào: thuật toán topic 08; ví dụ topic 04.
- Kết nối ra: so thời điểm và phạm vi tác động (topic 12, 13).
- Nguồn: tr. 29; hw05 Bài 7; slide B03–B04, B08.

### lec-05-topic-10 — $T^\pi$ và kỳ vọng cập nhật

- Nhóm: `cầu nối`.
- Vai trò trong mạch: nối một mẫu nhiễu $\delta_t$ với sai số Bellman kỳ vọng.
- Kết nối vào: $\delta_t$ của topic 07–09.
- Kết nối ra: giả thiết hội tụ (topic 11).
- Nguồn: tr. 25–28; slide B06.

### lec-05-topic-11 — Giả thiết hội tụ MC/TD, $\gamma<1$ và $\gamma=1$ theo lượt

- Nhóm: `cầu nối`.
- Vai trò trong mạch: phát biểu hội tụ đầy đủ, tách hai nhánh chiết khấu và kết thúc hấp thụ.
- Kết nối vào: $T^\pi$ (topic 10), trung bình mẫu (topic 06).
- Kết nối ra: quỹ đạo dài ở topic 12 kiểm tra vai trò của $\gamma$ và điều kiện kết thúc trước khi chuyển sang tiêu chí chọn phương pháp.
- Nguồn: tr. 18, 21–23, 28; slide A07, B07.

### lec-05-topic-12 — Quỹ đạo dài và hệ số chiết khấu $\gamma^3=0{,}970299$, $\gamma(-1)=-0{,}99$

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: cho thấy $G_t$ nhạy với đường đi khi lượt dài và thưởng thưa.
- Kết nối vào: định nghĩa $G_t$ (topic 02).
- Kết nối ra: cơ chế chệch–phương sai (topic 13).
- Nguồn: tr. 30–31; slide C00–C01, C05.

### lec-05-topic-13 — Cơ chế chệch–phương sai có điều kiện

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: giải thích vì sao đích khác nhau tạo đánh đổi khác nhau, không xếp hạng phổ quát.
- Kết nối vào: hai đích $G_t$ và $Y_t^{\mathrm{TD}}$ (topic 02, 07).
- Kết nối ra: tiêu chí chọn (topic 14) và bài tập hw05 Bài 4.
- Nguồn: tr. 26–28, 31; slide C02–C04.

### lec-05-topic-14 — Tiêu chí chọn, giới hạn và phạm vi

- Nhóm: `bổ sung`.
- Vai trò trong mạch: chuyển cơ chế thành tiêu chí lựa chọn và chặn suy diễn quá phạm vi.
- Kết nối vào: topic 06, 11, 13.
- Kết nối ra: tổng hợp (topic 15).
- Nguồn: tr. 15, 28, 31–33; slide C04, C06.

### lec-05-topic-15 — Tổng hợp, cầu nối Bài 06 và bài tập hw05 B7/B3/B4

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: khép năm ý chính, mở cầu nối điều khiển, gắn nhánh bài tập dọc.
- Kết nối vào: toàn bài.
- Kết nối ra: Bài 06 — điều khiển phi mô hình.
- Nguồn: tr. 32–33; hw05 Bài 7, Bài 3, Bài 4; slide D00–D01, X07, X03, X04.

## Ký hiệu và quy ước

- $\mathcal S$ hữu hạn, $\mathcal A$ hữu hạn; chính sách Markov dừng $\pi(a\mid s)$ cố định trong toàn bài; dữ liệu sinh theo chính sách $\pi$ (theo chính sách).
- Phần thưởng bị chặn; $0\le\gamma\le1$; lượt kết thúc tại thời điểm $T$; trạng thái kết thúc hấp thụ với $V(\text{kết thúc})=0$.
- $S_t$ — trạng thái tại thời điểm $t$; $R_{t+1}$ — phần thưởng của chuyển $S_t\to S_{t+1}$; $R_{t+k+1}$ mang hệ số $\gamma^k$.
- $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ là giá trị thật, cố định; $V_t(s)$ là ước lượng bảng trước cập nhật ở bước $t$.
- $N(s)$ — số mẫu MC đã nhận cho $s$; $n(s)$ — số lần TD đã cập nhật $s$; $\alpha_n(s)$ — bước học ở lần cập nhật thứ $n$ của $s$.
- Kỳ vọng $\mathbb E_\pi[\cdot\mid S_t=s]$ lấy có điều kiện theo chuyển tiếp dưới $\pi$, giữ $V_t$ cố định khi cần.

<!-- note-topic-id: lec-05-topic-01 -->
## Bài toán dự đoán phi mô hình và giả thiết

**Vấn đề.** Bài 04 đánh giá chính sách bằng quy hoạch động, đòi hỏi biết đủ $P$ và $R$. Trong nhiều bài toán, mô hình không được cho trước; ta chỉ có trải nghiệm.

**Trực giác.** Ở mỗi bước, tác nhân chỉ quan sát được trạng thái hiện tại, hành động được chọn, phần thưởng nhận được và trạng thái kế tiếp. Học phải diễn ra trực tiếp từ các quỹ đạo lấy mẫu, không đi qua mô hình.

**Thiết lập.** Cho MDP bảng hữu hạn chưa biết mô hình, chính sách Markov dừng $\pi$ cố định, dữ liệu theo chính sách $\pi$. Cần ước lượng

$$v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s].$$

**Giả thiết dùng suốt bài.** $\mathcal S$ hữu hạn; phần thưởng bị chặn; $0\le\gamma\le1$; MC dùng bài toán theo lượt, lượt kết thúc gần như chắc chắn dưới $\pi$; $V(\text{kết thúc})=0$. Không dạy điều khiển, học khác chính sách, Q-learning hay xấp xỉ hàm.

**Ứng dụng và giới hạn.** Hai cách tiếp cận cốt lõi là Monte Carlo và sai phân thời gian; cả hai đều chỉ hợp lệ cho chính sách đang sinh dữ liệu. Thay đổi chính sách làm thay đổi phân phối dữ liệu và đích cần ước lượng.

::: exercise Câu hỏi kiểm tra
Trong bối cảnh phi mô hình, tác nhân quan sát được những gì ở mỗi bước? Vì sao vẫn có thể học $v_\pi$ dù không biết $P$ và $R$?
:::

::: hint
Liệt kê bốn đại lượng quan sát được; nhớ rằng kỳ vọng trong định nghĩa $v_\pi$ có thể xấp xỉ bằng trung bình mẫu.
:::

::: solution
Quan sát được $(S_t, A_t, R_{t+1}, S_{t+1})$. Vì $v_\pi$ là kỳ vọng của tổng phần thưởng chiết khấu dưới $\pi$, ta có thể xấp xỉ kỳ vọng đó bằng trung bình các phần thưởng tích lũy quan sát được trên các quỹ đạo sinh theo $\pi$, mà không cần biết $P$ và $R$. Hạn chế so với quy hoạch động: cần nhiều mẫu, chỉ học được giá trị của chính sách sinh dữ liệu, và không có bảo đảm nếu thiếu giả thiết (lượt kết thúc, bước học phù hợp).
:::

<!-- note-topic-id: lec-05-topic-02 -->
## Lượt, trạng thái kết thúc, phần thưởng tích lũy $G_t$

**Vấn đề.** Muốn học từ một lượt, cần một con số duy nhất tóm tắt "kết quả" từ thời điểm $t$ trở đi.

**Trực giác.** Đi hết lượt, cộng dồn phần thưởng với chiết khấu: phần thưởng càng xa càng bị nhân bởi nhiều lần $\gamma$.

**Hình thức.** Với lượt kết thúc tại thời điểm $T$:

$$G_t=\sum_{k=0}^{T-t-1}\gamma^kR_{t+k+1}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{T-t-1}R_T.$$

Chỉ số $R_{t+k+1}$ mang hệ số $\gamma^k$: phần thưởng ở chuyển thứ tư kể từ $t$ mang $\gamma^3$. Trạng thái kết thúc hấp thụ nên $V(\text{kết thúc})=0$; phần thưởng nằm trên chuyển tiếp vào trạng thái kết thúc.

**Ứng dụng và giới hạn.** $G_t$ là đích của MC, chỉ biết được sau khi lượt kết thúc. Nếu $\pi$ không đảm bảo đi tới kết thúc, $G_t$ có thể không xác định hữu hạn.

::: example Lượt mẫu $e_1$
Môi trường $L\;S\;x\;G$; chính sách dự định Right, mỗi chuyển bị đảo chiều sang trái với xác suất $0{,}2$; thưởng $-1$ vào $L$, $+1$ vào $G$, $0$ ở các ô còn lại; $\gamma=1$. Lấy được $e_1:S\to x\to S\to x\to G$ với thưởng chuyển $(0,0,0,+1)$. Với mọi lần ghé $S$ và $x$ trong $e_1$, $G_t=+1$.
:::

::: exercise Câu hỏi kiểm tra
Nếu phần thưởng $+1$ là $R_{t+4}$ và $\gamma=0{,}99$, đóng góp của nó vào $G_t$ là bao nhiêu?
:::

::: hint
Viết $R_{t+k+1}=R_{t+4}$ để tìm $k$.
:::

::: solution
$k=3$, nên đóng góp là $\gamma^3\cdot(+1)=0{,}99^3=0{,}970299$. Sai thường gặp là lấy $\gamma^4$ vì chỉ số thời gian là $t+4$; quy tắc đúng là $R_{t+k+1}$ mang $\gamma^k$.
:::

<!-- note-topic-id: lec-05-topic-03 -->
## MC lần ghé đầu và thuật toán

**Vấn đề.** Từ các lượt mẫu, làm sao biến $G_t$ thành ước lượng $V(s)$ một cách tái tạo được?

**Trực giác.** Mỗi lần ghé đầu của $s$ trong một lượt cho một mẫu của $v_\pi(s)$; trung bình các mẫu là ước lượng, theo luật số lớn.

**Thuật toán — MC lần ghé đầu.**

- *Đầu vào:* $\pi,\gamma$; bộ sinh lượt theo $\pi$; ngân sách $M$ lượt hoặc tiêu chuẩn dừng.
- *Khởi tạo:* $V(s)=0$, $N(s)=0$ cho mọi $s$; $V(\text{kết thúc})=0$.
- *Mỗi lượt:* sinh quỹ đạo tới kết thúc; tính $G_t$ ngược từ cuối lượt; với lần ghé đầu của mỗi $s$: tăng $N(s)$ và cập nhật trung bình mẫu.
- *Quy tắc cập nhật:* $N(s)\leftarrow N(s)+1$, $\;V(s)\leftarrow V(s)+\dfrac{G_t-V(s)}{N(s)}$.
- *Quy tắc mẫu:* mỗi trạng thái tối đa một mẫu trong mỗi lượt (lần ghé đầu).
- *Đầu ra:* $V$. Chi phí: mỗi lượt dài $T_e$ mất $O(T_e)$ thời gian; bảng $O(|\mathcal S|)$, quỹ đạo tạm $O(T_e)$.

**Ứng dụng và giới hạn.** Chỉ cập nhật sau khi lượt kết thúc; cần lượt được khởi động lại độc lập dưới cùng $\pi$ để trung bình có ý nghĩa.

::: exercise Câu hỏi kiểm tra
Vì sao quy tắc "mỗi trạng thái tối đa một mẫu trong mỗi lượt" quan trọng cho lần ghé đầu?
:::

::: hint
Hãy đếm số mẫu mà $S$ đóng góp trong $e_1$ nếu đếm mọi lần ghé.
:::

::: solution
Trong $e_1$, $S$ xuất hiện hai lần và $x$ hai lần. Nếu đếm mọi lần ghé, một lượt cho hai mẫu cho mỗi trạng thái và các mẫu đó phụ thuộc nhau (chung phần đuôi lượt). Lần ghé đầu cho mỗi lượt đúng một mẫu cho mỗi trạng thái: với các lượt khởi động lại độc lập, các mẫu từ khác lượt là độc lập, còn hai mẫu trong cùng lượt luôn phụ thuộc nhau. Nhờ đó luật số lớn áp dụng trực tiếp trên các lượt khởi động lại độc lập.
:::

<!-- note-topic-id: lec-05-topic-04 -->
## Ví dụ đi bộ ngắn hai lượt, tính tay

**Vấn đề.** Chạy trọn thuật toán trên dữ liệu nhỏ để thấy từng bước.

**Ví dụ.** $V_0(S)=V_0(x)=0$, $\gamma=1$, lần ghé đầu, trung bình mẫu. Hai lượt:

- $e_1:S\to x\to S\to x\to G$ với thưởng $(0,0,0,+1)$: mọi lần ghé đầu có $G=+1$.
- $e_2:S\to x\to S\to L$ với thưởng $(0,0,-1)$: mọi lần ghé đầu có $G=-1$.

| Lượt | $(G(S),G(x))$ | $(N(S),N(x))$ | $(V(S),V(x))$ |
|---|---|---|---|
| $e_1$ | $(+1,+1)$ | $(1,1)$ | $(1,1)$ |
| $e_2$ | $(-1,-1)$ | $(2,2)$ | $(0,0)$ |

**Ứng dụng và giới hạn.** Hai lượt đối nghịch cho trung bình bằng $0$ ở cả hai trạng thái — cỡ mẫu rất nhỏ, không phản ánh chất lượng dài hạn của thuật toán.

::: exercise Câu hỏi kiểm tra
Nếu chỉ có $e_1$, giá trị ước lượng là bao nhiêu? Nếu thêm $e_2$, vì sao kết quả về $0$?
:::

::: hint
Áp dụng trực tiếp công thức trung bình với $N=1$ rồi $N=2$.
:::

::: solution
Sau $e_1$: $V(S)=V(x)=1$. Sau $e_2$: $V(S)=\frac{1+(-1)}{2}=0$, $V(x)=\frac{1+(-1)}{2}=0$. Trung bình mẫu cân bằng hai mẫu đối nghịch.
:::

<!-- note-topic-id: lec-05-topic-05 -->
## Giá trị chuẩn $11/21$, $19/21$ và điều kiện kỳ vọng

**Vấn đề.** Sau hai lượt, ước lượng $(0,0)$ lệch bao nhiêu so với giá trị thật?

**Trực giác.** Giải hệ Bellman kỳ vọng của mô hình thật cho giá trị chuẩn — chỉ để đối chiếu, thuật toán không dùng chúng.

**Kết quả.** Với chính sách Right, xác suất đảo chiều $0{,}2$, $\gamma=1$:

$$v_\pi(S)=\frac{11}{21}\approx0{,}524,\qquad v_\pi(x)=\frac{19}{21}\approx0{,}905.$$

**Điều kiện kỳ vọng.** Các giá trị này là kỳ vọng $\mathbb E_\pi[G_t\mid S_t=s]$: chúng là giới hạn của trung bình mẫu khi số mẫu tiến vô hạn, không phải kết quả của một vài lượt. Sai số lớn sau hai lượt phản ánh cỡ mẫu nhỏ, không bác bỏ tính nhất quán dài hạn.

**Ứng dụng và giới hạn.** Trong bài toán phi mô hình thật, giá trị chuẩn đối chiếu không có sẵn; vai trò ở đây chỉ là dạy cách đọc sai số ước lượng.

::: exercise Câu hỏi kiểm tra
Sau hai lượt, sai số của $V(S)$ so với $v_\pi(S)$ là bao nhiêu? Điều gì giảm sai số này?
:::

::: hint
Trừ trực tiếp; nghĩ về luật số lớn.
:::

::: solution
Sai số là $0-\frac{11}{21}=-\frac{11}{21}\approx-0{,}524$. Sai số giảm khi số lượt độc lập tăng: trung bình mẫu hội tụ về $v_\pi(s)$ theo luật số lớn, với điều kiện mỗi trạng thái được ghé trong vô hạn lượt và $G_t$ có kỳ vọng hữu hạn.
:::

<!-- note-topic-id: lec-05-topic-06 -->
## Hai trục MC: lần ghé đầu/mọi lần ghé và trung bình mẫu/$\alpha$ hằng

**Vấn đề.** Cụm từ "Monte Carlo gia tăng" chưa đủ để tái tạo kết quả: còn thiếu quy tắc lấy mẫu và quy tắc bước học.

**Trực giác.** Có hai lựa chọn độc lập:

1. *Quy tắc lần ghé:* lần ghé đầu (mỗi trạng thái một mẫu mỗi lượt) hoặc mọi lần ghé (nhiều mẫu phụ thuộc nhau trong cùng lượt).
2. *Quy tắc bước học:* trung bình mẫu với bước $1/N(s)$, hoặc bước học hằng $\alpha$.

**Hình thức.** Cùng các mẫu của topic 04 nhưng đổi bước học sang $\alpha=0{,}5$ (vẫn lần ghé đầu): sau $e_1$ có $(V(S),V(x))=(0{,}5,0{,}5)$; sau $e_2$ có $(-0{,}25,-0{,}25)$ — khác $(0,0)$ của trung bình mẫu vì $\alpha$ hằng đặt trọng số lớn hơn lên lượt mới.

Với *mọi lần ghé* và trung bình mẫu, tiếp tục từ giá trị sau $e_1$: sau $e_2$ có $(V(S),V(x))=(0,1/3)$ — $S$ nhận hai mẫu $+1$ trong $e_1$ rồi thêm hai mẫu $-1$ trong $e_2$ (tổng bốn mẫu $1,1,-1,-1$, trung bình $0$), $x$ nhận hai mẫu $+1$ trong $e_1$ rồi thêm một mẫu $-1$ trong $e_2$ (tổng ba mẫu $1,1,-1$, trung bình $1/3$). Với mọi lần ghé và $\alpha=0{,}5$ xử lý theo $t$ tăng dần, kết quả khác nữa: sau $e_1$ là $(0{,}75,0{,}75)$, sau $e_2$ là $(-0{,}5625,-0{,}125)$; các mẫu trong cùng lượt phụ thuộc nhau nên thứ tự xử lý ảnh hưởng kết quả khi $\alpha$ hằng.

**Ứng dụng và giới hạn.** Trung bình mẫu (bước $1/N$) có bảo đảm hội tụ; $\alpha$ hằng không hội tụ điểm nói chung — nó tiếp tục bám dữ liệu mới, hữu ích khi môi trường thay đổi nhưng không cho giới hạn xác định.

::: exercise Câu hỏi kiểm tra
Hai cấu hình nào dưới đây cho $(0,0)$ sau hai lượt: (a) lần ghé đầu + trung bình mẫu; (b) lần ghé đầu + $\alpha=0{,}5$; (c) mọi lần ghé + trung bình mẫu?
:::

::: hint
Tính lại bảng của topic 04 và phần mọi lần ghé ở trên.
:::

::: solution
(a) cho $(0,0)$; (b) cho $(-0{,}25,-0{,}25)$; (c) cho $(0,1/3)$. Vậy chỉ (a) cho $(0,0)$. Bài học: phải nêu đủ hai trục — quy tắc lần ghé và quy tắc bước học — mới mô tả được thuật toán.
:::

<!-- note-topic-id: lec-05-topic-07 -->
## Chuyển mẫu, đích TD, delta

**Vấn đề.** MC phải chờ lượt kết thúc. Có thể học từ một chuyển tiếp chưa kết thúc không?

**Trực giác.** Ở thời điểm $t$, quan sát mẫu $(S_t,R_{t+1},S_{t+1})=(S,0,x)$. Biết ngay $R_{t+1}$ và ước lượng hiện tại $V_t(x)$; chưa biết phần thưởng kết thúc của lượt. TD dùng cơ chế tự mồi (bootstrap): thay toàn bộ phần còn lại của lượt bằng $\gamma V_t(S_{t+1})$.

**Hình thức.**

$$Y_t^{\mathrm{TD}}=R_{t+1}+\gamma V_t(S_{t+1}),\qquad \delta_t=Y_t^{\mathrm{TD}}-V_t(S_t).$$

Đối chiếu: $G_t$ là đích MC, biết sau kết thúc; $Y_t^{\mathrm{TD}}$ là đích TD một bước, dùng $V_t$ ở trạng thái kế tiếp; $\delta_t$ là sai số TD. $v_\pi$ vẫn là đích thật; $V_t$ vẫn là bảng đang học. Hành động không xuất hiện trong công thức giá trị trạng thái vì dữ liệu sinh theo chính sách cố định.

**Ứng dụng và giới hạn.** TD cập nhật ngay sau mỗi chuyển, kể cả giữa lượt; nhưng đích dùng ước lượng kế tiếp nên có thể mang chệch (topic 13).

::: exercise Câu hỏi kiểm tra
Cho chuyển $(S_t,R_{t+1},S_{t+1})=(s,2,s')$, $\gamma=0{,}9$, $V_t(s)=4$, $V_t(s')=5$. Tính $Y_t^{\mathrm{TD}}$ và $\delta_t$.
:::

::: hint
Thay trực tiếp vào hai công thức.
:::

::: solution
$Y_t^{\mathrm{TD}}=2+0{,}9\cdot5=6{,}5$; $\delta_t=6{,}5-4=2{,}5$.
:::

<!-- note-topic-id: lec-05-topic-08 -->
## Thuật toán TD(0)

**Vấn đề.** Biến đích một bước thành thuật toán có giao diện đầy đủ.

**Thuật toán — TD(0) dạng bảng.**

- *Đầu vào:* $\pi,\gamma$; bộ sinh chuyển theo $\pi$; lịch bước học $\alpha_n(s)$; ngân sách hoặc tiêu chuẩn dừng.
- *Khởi tạo:* $V$ và $n(s)=0$; đặt $V(\text{kết thúc})=0$.
- *Mỗi chuyển:* chọn $A\sim\pi(\cdot\mid S)$; quan sát $R,S'$; tăng $n(S)$; tính $Y=R+\gamma V(S')$ và $\delta=Y-V(S)$; cập nhật $V(S)\leftarrow V(S)+\alpha_{n(S)}(S)\,\delta$; đặt $S\leftarrow S'$.
- *Vòng lặp:* lặp đến kết thúc lượt rồi khởi động lượt mới.
- *Đầu ra:* $V$. Chi phí: mỗi lượt dài $T_e$ mất $O(T_e)$ thời gian, $O(|\mathcal S|)$ bộ nhớ.

**Quy ước cập nhật tại chỗ:** chuyển sau đọc bảng vừa được cập nhật ở chuyển trước; $n$ là số lần trạng thái $S$ đã được cập nhật, không nhất thiết là chỉ số thời gian toàn cục.

**Ứng dụng và giới hạn.** TD(0) học giữa lượt và không cần mô hình; nhưng kết quả phụ thuộc lịch bước học và giá trị khởi tạo nhiều hơn MC.

::: exercise Câu hỏi kiểm tra
Trong chuyển $x\to S$ của lượt hai (topic 09), vì sao đích là $0{,}25$ chứ không phải $0$?
:::

::: hint
Kiểm tra quy ước cập nhật tại chỗ.
:::

::: solution
Vì cập nhật tại chỗ: chuyển trước đó ($S\to x$) đã đổi $V(S)$ từ $0$ lên $0{,}25$, nên chuyển $x\to S$ đọc $V(S)=0{,}25$ và đích là $0+\gamma\cdot0{,}25=0{,}25$. Nếu dùng hai bảng cố định trong cả lượt, kết quả sẽ khác và phải ghi rõ quy ước đó.
:::

<!-- note-topic-id: lec-05-topic-09 -->
## Cập nhật TD tính tay cùng ví dụ

**Vấn đề.** Cùng hai lượt, cùng $\alpha=0{,}5$, $\gamma=1$, $V_0(S)=V_0(x)=0$ — TD cho kết quả gì?

**Lượt $e_1:S\to x\to S\to x\to G$** (cập nhật tại chỗ):

| Chuyển | $(V(S),V(x))$ trước | $Y^{\mathrm{TD}}$ | $\delta$ | sau |
|---|---|---|---|---|
| $S\to x,0$ | $(0,0)$ | $0$ | $0$ | $(0,0)$ |
| $x\to S,0$ | $(0,0)$ | $0$ | $0$ | $(0,0)$ |
| $S\to x,0$ | $(0,0)$ | $0$ | $0$ | $(0,0)$ |
| $x\to G,+1$ | $(0,0)$ | $1$ | $1$ | $(0,0{,}5)$ |

**Lượt $e_2:S\to x\to S\to L$**, tiếp tục từ $(0,0{,}5)$:

| Chuyển | trước | $Y^{\mathrm{TD}}$ | $\delta$ | sau |
|---|---|---|---|---|
| $S\to x,0$ | $(0,0{,}5)$ | $0{,}5$ | $0{,}5$ | $(0{,}25,0{,}5)$ |
| $x\to S,0$ | $(0{,}25,0{,}5)$ | $0{,}25$ | $-0{,}25$ | $(0{,}25,0{,}375)$ |
| $S\to L,-1$ | $(0{,}25,0{,}375)$ | $-1$ | $-1{,}25$ | $(-0{,}375,0{,}375)$ |

**Ứng dụng và giới hạn.** Sau $e_2$: TD cho $(-0{,}375,0{,}375)$, trong khi MC lần ghé đầu với trung bình mẫu cho $(0,0)$ và với $\alpha=0{,}5$ cho $(-0{,}25,-0{,}25)$. TD cập nhật sớm hơn nhưng không thấy xa hơn: trên lượt đầu với khởi tạo bằng không, TD chỉ thay đổi $x$ ở chuyển cuối, còn MC sau kết thúc thay đổi cả $S$ và $x$. Lưu ý $\delta=-1{,}25$ chỉ là một mẫu nhiễu của sai số, chưa xác định dấu của sai số kỳ vọng.

::: exercise Câu hỏi kiểm tra
Giải thích vì sao ba phương pháp cho ba kết quả khác nhau sau $e_2$.
:::

::: hint
Đối chiếu ba yếu tố: quy tắc mẫu, quy tắc bước học, thời điểm cập nhật.
:::

::: solution
MC lần ghé đầu + trung bình mẫu: hai mẫu $\pm1$ cân bằng, cho $(0,0)$. MC lần ghé đầu + $\alpha=0{,}5$: cùng hai mẫu nhưng lượt mới được trọng số lớn, cho $(-0{,}25,-0{,}25)$. TD(0) tại chỗ: cập nhật sau từng chuyển, phần thưởng $-1$ chỉ tác động lên $S$ ở chuyển cuối và lan truyền qua bảng tại chỗ, cho $(-0{,}375,0{,}375)$. Khác biệt đến từ cơ chế, không phải từ lỗi tính toán.
:::

<!-- note-topic-id: lec-05-topic-10 -->
## $T^\pi$ và kỳ vọng cập nhật

**Vấn đề.** Một mẫu $\delta_t$ nhiễu; điều gì đúng *trung bình*?

**Trực giác.** Nếu lấy kỳ vọng của đích TD theo chuyển tiếp dưới $\pi$, giữ $V_t$ cố định, ta được toán tử kỳ vọng Bellman:

$$(T^\pi V)(s)=\mathbb E_\pi\!\left[R_{t+1}+\gamma V(S_{t+1})\mid S_t=s\right].$$

**Hình thức.**

$$\mathbb E_\pi[Y_t^{\mathrm{TD}}\mid S_t=s,V_t]=(T^\pi V_t)(s),\qquad \mathbb E_\pi[\delta_t\mid S_t=s,V_t]=(T^\pi V_t)(s)-V_t(s).$$

Mỗi $\delta_t$ là một mẫu nhiễu của sai số Bellman $(T^\pi V_t)(s)-V_t(s)$; một chuyển chưa xác định dấu của sai số kỳ vọng. Với $\gamma<1$, $T^\pi$ là ánh xạ co hệ số $\gamma$ theo chuẩn vô cùng và có điểm bất động duy nhất $v_\pi$, cùng cơ chế hội tụ của quy hoạch động ở Bài 04.

**Ứng dụng và giới hạn.** Định nghĩa bằng kỳ vọng có điều kiện dùng được cho phần thưởng rời rạc hoặc liên tục. Khi $V_t\ne v_\pi$, đích TD dùng phần đuôi xấp xỉ nên có thể chệch so với đích lý tưởng $R_{t+1}+\gamma v_\pi(S_{t+1})$. Với $\gamma=1$, không viện dẫn tính co nghiêm trong chuẩn vô cùng.

::: exercise Câu hỏi kiểm tra
Vì sao $\mathbb E_\pi[\delta_t\mid S_t=s,V_t]\ne0$ chưa đủ để kết luận $V_t$ sai hướng?
:::

::: hint
So sánh với điểm bất động của $T^\pi$.
:::

::: solution
Kỳ vọng sai số bằng $(T^\pi V_t)(s)-V_t(s)$, là sai số Bellman của $V_t$. Nó bằng $0$ tại điểm bất động $v_\pi$. Cập nhật kỳ vọng tại trạng thái $s$ dịch $V_t(s)$ về phía $(T^\pi V_t)(s)$; kết luận hội tụ về $v_\pi$ chỉ đúng dưới các giả thiết ở topic 11. Cần phân biệt kỳ vọng với một mẫu đơn lẻ.
:::

<!-- note-topic-id: lec-05-topic-11 -->
## Giả thiết hội tụ MC/TD, $\gamma<1$ và $\gamma=1$ theo lượt

**Vấn đề.** Khi nào trung bình mẫu và TD(0) thực sự hội tụ về $v_\pi$?

**MC lần ghé đầu, trung bình mẫu.** Hội tụ về $v_\pi(s)$ theo luật số lớn nếu: các lượt được khởi động lại độc lập và sinh theo cùng $\pi$; $G_t$ có kỳ vọng hữu hạn; mỗi trạng thái cần đánh giá xuất hiện trong vô hạn lượt.

**TD(0) dạng bảng.** Với mỗi trạng thái $s$, gọi $n$ là số lần đã cập nhật $s$. Lịch điển hình $\alpha_n(s)=1/n$ thỏa điều kiện Robbins–Monro:

$$0<\alpha_n(s)\le1,\qquad \sum_{n=1}^{\infty}\alpha_n(s)=\infty,\qquad \sum_{n=1}^{\infty}\alpha_n(s)^2<\infty.$$

Tổng thứ nhất phân kỳ để mỗi trạng thái tiếp tục được điều chỉnh; tổng bình phương hội tụ để nhiễu ngẫu nhiên không tích lũy vô hạn. Khi mỗi trạng thái được cập nhật vô hạn lần, $V_n(s)\to v_\pi(s)$ gần chắc chắn nếu:

- $\gamma<1$; hoặc
- $\gamma=1$ theo lượt: các lượt được khởi động lại, trạng thái kết thúc hấp thụ, và $\pi$ *đúng đắn* — đi tới kết thúc với xác suất $1$ từ mọi trạng thái có thể đạt được từ phân phối khởi tạo dưới $\pi$; các trạng thái không kết thúc này là quá độ.

Cả hai nhánh còn cần MDP hữu hạn, phần thưởng bị chặn và dữ liệu theo chính sách $\pi$.

**Ứng dụng và giới hạn.** $\alpha$ hằng (ví dụ $\alpha=0{,}5$) không thỏa điều kiện tổng bình phương hữu hạn, nên không có bảo đảm hội tụ điểm nói chung. Mọi bảo đảm hội tụ luôn đi cùng giả thiết; không phát biểu hội tụ mà không nêu giả thiết.

::: exercise Câu hỏi kiểm tra
Vì sao nhánh $\gamma=1$ cần thêm giả thiết "đúng đắn" trong khi nhánh $\gamma<1$ không cần nhấn mạnh?
:::

::: hint
Nghĩ về $\gamma^k$ khi $k\to\infty$ trong hai trường hợp.
:::

::: solution
Với $\gamma<1$ và phần thưởng bị chặn, phần đuôi giảm theo cấp số nhân nên tổng phần thưởng có kỳ vọng hữu hạn ngay cả khi quỹ đạo tiếp tục. Với $\gamma=1$, không có chiết khấu: nếu chính sách có thể không bao giờ tới kết thúc, $G_t$ có thể không hữu hạn và đích học mất nghĩa. Do đó cần $\pi$ đi tới kết thúc với xác suất $1$ từ mọi trạng thái có thể đạt được từ phân phối khởi tạo, cùng lượt khởi động lại và trạng thái kết thúc hấp thụ.
:::

<!-- note-topic-id: lec-05-topic-12 -->
## Quỹ đạo dài và hệ số chiết khấu

**Vấn đề.** Khi lượt dài và phần thưởng thưa, $G_t$ nhạy với đường đi như thế nào?

**Thiết lập.** Bản đồ $L\;\cdot\;S\;\cdot\;\cdot\;\cdot\;G$; chính sách dự định Right, xác suất đảo chiều $0{,}2$, $\gamma=0{,}99$; chỉ chuyển vào $L$ hoặc $G$ có thưởng $-1$ hoặc $+1$.

**Ví dụ chỉ số.** Nếu lượt tới $G$ sau bốn chuyển, phần thưởng $+1$ là $R_{t+4}$ nên mang hệ số $\gamma^3$:

$$G_t=\gamma^3(+1)=0{,}99^3=0{,}970299.$$

Nếu lượt tới $L$ sau hai chuyển, phần thưởng $-1$ là $R_{t+2}$ nên:

$$G_t=\gamma(-1)=-0{,}99.$$

**Ứng dụng và giới hạn.** Cùng một trạng thái bắt đầu có thể cho phần thưởng tích lũy dương gần $+1$ hoặc âm gần $-1$: độ dài và nhiễu làm $G_t$ phụ thuộc mạnh vào quỹ đạo đã lấy mẫu.

::: exercise Câu hỏi kiểm tra
Vì sao hai lượt bắt đầu tại $S$ có thể cho phần thưởng tích lũy gần $+0{,}97$ và $-0{,}99$?
:::

::: hint
Đếm số chuyển từ $S$ đến mỗi trạng thái kết thúc và xác định chỉ số của phần thưởng cuối.
:::

::: solution
Đường tới $G$ dài bốn chuyển nên phần thưởng $+1$ là $R_{t+4}$ và mang $\gamma^3=0{,}970299$. Đường tới $L$ dài hai chuyển nên phần thưởng $-1$ là $R_{t+2}$ và mang $\gamma=-0{,}99$. Độ dài và hướng của quỹ đạo tạo hai kết quả khác nhau.
:::

<!-- note-topic-id: lec-05-topic-13 -->
## Cơ chế chệch–phương sai có điều kiện

**Vấn đề.** Vì sao trên quỹ đạo dài, đích TD thường biến động ít hơn $G_t$, và điều gì phải trả giá?

**Trực giác.** $G_t$ cộng dồn nhiều phần thưởng và chịu nhiều chuyển tiếp ngẫu nhiên — nhiều nguồn biến động tích lũy. Đích TD chỉ phụ thuộc một chuyển được lấy mẫu, phần đuôi được thay bằng $V_t(S_{t+1})$ — một số xác định tại thời điểm cập nhật.

**Hình thức — so sánh có điều kiện.**

| | Monte Carlo | TD(0) |
|---|---|---|
| Đích | $G_t$ sau kết thúc | $R_{t+1}+\gamma V_t(S_{t+1})$ |
| Nguồn biến động | toàn bộ thưởng và chuyển tiếp còn lại | một chuyển và giá trị kế tiếp |
| Dùng ước lượng kế tiếp | không | có |
| Chệch của đích | không, nếu lấy mẫu đúng | có thể có khi $V_t\ne v_\pi$ |

Ba mệnh đề cần đọc có điều kiện:

- Mẫu đích $G_t$ có kỳ vọng bằng $v_\pi(S_t)$ khi lấy mẫu đúng chính sách và lượt kết thúc. Tính chất này không bảo đảm MC với $\alpha$ hằng hội tụ điểm.
- Đích lý tưởng $R_{t+1}+\gamma v_\pi(S_{t+1})$ cũng không chệch; nhưng đích TD thực tế dùng $V_t$ nên *có thể* chệch khi $V_t\ne v_\pi$.
- Trên quỹ đạo dài và nhiễu, đích TD *thường* biến động ít hơn vì thay phần đuôi ngẫu nhiên bằng $V_t$; đây là cơ chế thường gặp, **không phải** xếp hạng phổ quát "TD luôn phương sai thấp hơn" hay "MC luôn không chệch tốt hơn". Mức chệch, phương sai và tốc độ còn phụ thuộc môi trường, khởi tạo và bước học.

**Ứng dụng và giới hạn.** Trong lượt dài, thưởng thưa và hành động nhiễu, TD bỏ phần đuôi ngẫu nhiên khỏi từng đích cập nhật nhưng dùng ước lượng $V_t$. Không có thứ tự phương sai hay tốc độ học đúng cho mọi môi trường.

::: exercise Câu hỏi kiểm tra
Liệt kê nguồn ngẫu nhiên đi vào $G_t$; giải thích vì sao thay phần đuôi bằng $V_t$ vừa giảm biến động vừa có thể đưa chệch vào đích.
:::

::: hint
Tách $G_t$ thành phần đầu (một chuyển) và phần đuôi (phần còn lại của lượt).
:::

::: solution
$G_t$ gồm: chuyển tiếp đầu tiên ngẫu nhiên, các hành động ngẫu nhiên theo $\pi$ ở mọi bước sau, và các phần thưởng ngẫu nhiên còn lại. Đích TD giữ đúng phần đầu $R_{t+1}$ và thay phần đuôi bằng $\gamma V_t(S_{t+1})$ — một số không ngẫu nhiên tại thời điểm cập nhật, nên biến động giảm. Nhưng nếu $V_t\ne v_\pi$, phần đuôi bị thay bằng một xấp xỉ chệch, và chệch đó đi vào đích cho tới khi $V_t$ tiến về $v_\pi$.
:::

<!-- note-topic-id: lec-05-topic-14 -->
## Tiêu chí chọn, giới hạn và phạm vi

**Vấn đề.** Khi nào chọn MC, khi nào chọn TD?

**Tiêu chí.**

- Dùng MC khi lượt kết thúc rõ, có thể chờ, và cần đích không dùng ước lượng kế tiếp.
- Dùng TD khi cần cập nhật giữa lượt, hoặc lượt dài, và chấp nhận đích dùng $V_t(S_{t+1})$.
- Chọn $1/N$ hoặc lịch bước học giảm dần nếu cần hội tụ điểm. Với $\alpha$ hằng, dữ liệu mới luôn giữ trọng số dương nên dãy ước lượng nói chung không hội tụ điểm. Không đồng nhất lựa chọn bước học với lựa chọn MC hay TD.

**Giới hạn và phạm vi kết luận.**

- Chỉ dự đoán $v_\pi$ cho một chính sách cố định; chỉ dữ liệu theo chính sách.
- Chỉ biểu diễn bảng; không xấp xỉ hàm.
- Không có điều khiển, học khác chính sách hay giá trị hành động. Thay đổi chính sách làm thay đổi phân phối dữ liệu và đích cần ước lượng.
- Không kết luận một phương pháp luôn nhanh hơn hoặc hiệu quả mẫu hơn.

::: exercise Câu hỏi kiểm tra
Một môi trường có lượt rất dài, thưởng chỉ ở cuối, và bạn cần ước lượng giữa chừng. Chọn MC hay TD? Điều gì phải chấp nhận?
:::

::: hint
Dùng hai tiêu chí đầu.
:::

::: solution
Chọn TD(0): MC phải chờ lượt kết thúc rất lâu, còn TD cập nhật sau từng chuyển. Phải chấp nhận đích dùng $V_t(S_{t+1})$, tức đích có thể chệch khi $V_t$ chưa chính xác; nên dùng lịch bước học giảm dần nếu cần hội tụ điểm.
:::

<!-- note-topic-id: lec-05-topic-15 -->
## Tổng hợp, cầu nối Bài 06 và bài tập hw05 B7/B3/B4

**Chức năng tổng hợp.** Năm ý cần giữ:

1. Phi mô hình vẫn cần dữ liệu đúng chính sách cần đánh giá.
2. Monte Carlo tách quy tắc lần ghé khỏi quy tắc bước học.
3. TD tách $v_\pi$, $V_t$, $Y_t^{\mathrm{TD}}$ và $\delta_t$.
4. Bảo đảm hội tụ luôn đi cùng giả thiết.
5. So sánh chệch–phương sai phải nêu điều kiện; không có xếp hạng phổ quát giữa MC và TD.

**Cầu nối Bài 06.** Bài này giữ $\pi$ cố định và học $v_\pi$ từ trải nghiệm. Bài sau vừa đánh giá vừa cải thiện chính sách từ trải nghiệm: chính sách không còn cố định và thường cần giá trị hành động $q(s,a)$ để so sánh các hành động.

**Bài tập dọc (30 phút).**

- *hw05 B7 (giải thích ba kết quả):* trên cùng hai lượt $e_1$ tới $G$ và $e_2$ tới $L$, với $V_0(S)=V_0(x)=0$ — MC lần ghé đầu + trung bình mẫu cho $(0,0)$; MC lần ghé đầu + $\alpha=0{,}5$ cho $(-0{,}25,-0{,}25)$; TD(0) tại chỗ + $\alpha=0{,}5$ cho $(-0{,}375,0{,}375)$. Nhiệm vụ: chỉ ra lựa chọn về mẫu, bước học và thời điểm cập nhật tạo ra từng khác biệt (xem topic 04, 06, 09).
- *hw05 B3 (ba đại lượng TD):* cho chuyển $(s,2,s')$, $\gamma=0{,}9$, $V_t(s)=4$, $V_t(s')=5$, $\alpha_{n(s)}(s)=0{,}1$: tính $Y_t^{\mathrm{TD}}=6{,}5$, $\delta_t=2{,}5$, $V_{t+1}(s)=4{,}25$ (xem topic 07–08).
- *hw05 B4 (chệch–phương sai):* liệt kê nguồn ngẫu nhiên của $G_t$, giải thích đích lý tưởng và chệch khi thay $v_\pi$ bằng $V_t$, nêu vì sao không thể kết luận TD luôn nhanh hơn (xem topic 13).

::: exercise Câu hỏi tổng hợp
Thành phần nào phải thay đổi khi chuyển từ dự đoán sang điều khiển?
:::

::: hint
Nghĩ về vai trò của chính sách và loại giá trị cần học.
:::

::: solution
Chính sách không còn cố định — nó vừa được đánh giá vừa được cải thiện; do đó thường cần giá trị hành động $q(s,a)$ thay vì chỉ $v(s)$, để so sánh các hành động tại mỗi trạng thái. Phân phối dữ liệu cũng thay đổi theo chính sách đang chạy.
:::

## Tài liệu tham khảo

- Slide bài giảng "Dự đoán phi mô hình: Monte Carlo và sai phân thời gian", tr. 15–33 (Bài 05, Học tăng cường, HK1 2026–2027).
- Bài tập tuần 5 — Dự đoán phi mô hình, Bài 1–7 (dùng B7, B3, B4 cho nhánh dọc).
- Sutton, R. S. và Barto, A. G., *Reinforcement Learning: An Introduction*, ấn bản 2, chương 5 (Monte Carlo) và chương 6 (Temporal-Difference Learning) — đọc thêm cho điều kiện hội tụ và Robbins–Monro.
