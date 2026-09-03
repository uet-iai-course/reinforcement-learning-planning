# Bài 06 — Điều khiển phi mô hình

## Mục tiêu và kiến thức tiên quyết

- Phân biệt dự đoán (prediction) với điều khiển (control) và theo chính sách (on-policy) với khác chính sách (off-policy).
- Tạo chính sách $\varepsilon$-tham lam từ bảng $Q$ với quy tắc phá hòa tất định.
- Thực hiện điều khiển Monte Carlo (MC) lần ghé đầu, SARSA và Q-learning dạng bảng trên một lượt dùng chung.
- Phát biểu đúng điều kiện hội tụ: GLIE, độ phủ vô hạn, bước học Robbins–Monro, trên miền cặp khả đạt $\mathcal X_{\mathrm{reach}}$.

Kiến thức tiên quyết: MDP hữu hạn, hàm giá trị $v_\pi$ và $q_\pi$, dự đoán MC và TD(0) từ Bài 05.

## Bản đồ chủ đề

Bản đồ gồm bốn nhóm: `cốt lõi` (12 chủ đề), `cầu nối` (1 chủ đề), `bổ sung` (2 chủ đề) và `đọc thêm`. Ba nhóm đầu có topic ID. Hai chủ đề bổ sung là chủ đề 12, nhánh mở rộng 5 phút quay lại bài toán dự đoán, và chủ đề 14, nhánh linh hoạt 5 phút về chi phí bảng cùng chặn Hoeffding. Chủ đề 15 là kết luận cốt lõi: thu hồi mục tiêu, neo ba bài tập dọc và nối sang Bài 07. Nhóm đọc thêm là phần mở rộng của bảng phân loại ở PDF tr. 23 (DQN, policy gradient, actor–critic); tuyến này không có topic ID, chỉ để định vị và không được dạy trong bài.

Thời lượng: tuyến cốt lõi 110 phút; chủ đề 12 và chủ đề 14 là hai nhánh bổ sung, mỗi nhánh 5 phút, nâng tổng trình chiếu lên 120 phút; ba bài tập X01–X03 nặng 5–10–15 phút, tổng 30 phút.

### 01. Dự đoán sang điều khiển phi mô hình

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: chuyển từ Bài 05 (chính sách cố định) sang mục tiêu học chính sách và $Q$.
- Kết nối vào: dự đoán MC và TD(0).
- Kết nối ra: công cụ chọn hành động ở chủ đề 02.
- Nguồn: PDF tr. 1–3, 6; slide P00–P02.

### 02. Giá trị hành động và chính sách epsilon-tham lam

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: $Q$ và phá hòa tất định là nền cho cả ba thuật toán.
- Kết nối vào: miền $\mathcal X$ và vòng điều khiển.
- Kết nối ra: ba thuật toán MC, SARSA, Q-learning.
- Nguồn: PDF tr. 7, 10–11; slide A00–A01.

### 03. Theo chính sách và khác chính sách

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: phân loại chính sách hành vi $\mu$ và chính sách đích $\pi$.
- Kết nối vào: chính sách $\varepsilon$-tham lam.
- Kết nối ra: SARSA (theo chính sách) và Q-learning (khác chính sách).
- Nguồn: PDF tr. 8; slide A02.

### 04. Chuỗi năm trạng thái và quy tắc số tất định

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: một bảng $Q_0$ và một lượt dùng chung cho ba phép cập nhật.
- Kết nối vào: chính sách $\varepsilon$-tham lam.
- Kết nối ra: ba phép cập nhật số ở các chủ đề 05, 08, 10.
- Nguồn: PDF tr. 15–17; slide A03–A04.

### 05. Điều khiển MC lần ghé đầu

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: phần thưởng tích lũy → thuật toán đầy đủ → bảng trung bình mẫu và $\alpha$ hằng.
- Kết nối vào: lượt dùng chung ở chủ đề 04.
- Kết nối ra: câu hỏi cải thiện ở chủ đề 06.
- Nguồn: PDF tr. 10–11, 15–17; slide B00–B04.

### 06. Cải thiện cần $q_\pi$ chính xác

- Nhóm: `cầu nối`.
- Vai trò trong mạch: một mẫu $Q$ còn nhiễu không cho cải thiện đơn điệu; định lý cải thiện dùng $q_\pi$ chính xác.
- Kết nối vào: hai bảng cập nhật MC.
- Kết nối ra: điều kiện dài hạn GLIE ở chủ đề 07.
- Nguồn: PDF tr. 24; slide B05.

### 07. GLIE và hội tụ điều khiển MC

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: thăm dò vô hạn và tham lam ở giới hạn.
- Kết nối vào: định lý cải thiện $\varepsilon$-mềm.
- Kết nối ra: cùng hai điều kiện xuất hiện lại ở hội tụ SARSA.
- Nguồn: PDF tr. 25–26; slide B06.

### 08. SARSA dạng bảng và ví dụ

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: đích dùng hành động kế tiếp thật sự; cập nhật tại chỗ trên lượt dùng chung.
- Kết nối vào: bảng $Q_0$ và lượt ở chủ đề 04.
- Kết nối ra: điều kiện hội tụ ở chủ đề 09.
- Nguồn: PDF tr. 12–14, 17–18; slide C00–C04.

### 09. Hội tụ SARSA

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: GLIE cộng Robbins–Monro theo từng cặp, kết luận trên miền khả đạt.
- Kết nối vào: thuật toán SARSA.
- Kết nối ra: đối chiếu với điều kiện hội tụ Q-learning.
- Nguồn: PDF tr. 27; slide C05.

### 10. Q-learning dạng bảng và ví dụ

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: đích cực đại; đối chiếu trực tiếp với SARSA trên cùng lượt.
- Kết nối vào: chuyển $(C,0)\to B$ và hai giá trị tại B.
- Kết nối ra: điều kiện hội tụ ở chủ đề 11.
- Nguồn: PDF tr. 20–21; slide D00–D04.

### 11. Hội tụ Q-learning

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: độ phủ vô hạn cộng Robbins–Monro; không bắt buộc GLIE.
- Kết nối vào: thuật toán Q-learning.
- Kết nối ra: nhánh dự đoán khác chính sách ở chủ đề 12.
- Nguồn: PDF tr. 28; slide D05.

### 12. Dự đoán khác chính sách cho $V$

- Nhóm: `bổ sung`.
- Vai trò trong mạch: lấy mẫu quan trọng (importance sampling) một bước; không phải thuật toán điều khiển thứ tư.
- Kết nối vào: phân biệt $\mu$ và $\pi$ ở chủ đề 03.
- Kết nối ra: quay lại ba thuật toán điều khiển chính.
- Nguồn: PDF tr. 18–19; slide D06–D07.

### 13. Ba thuật toán, ba cơ chế

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: so đích, thời điểm cập nhật, quan hệ chính sách và điều kiện hành vi.
- Kết nối vào: cả ba thuật toán.
- Kết nối ra: chi phí ở chủ đề 14.
- Nguồn: PDF tr. 22–23, 30; slide E00.

### 14. Chi phí bảng và chặn Hoeffding

- Nhóm: `bổ sung`.
- Vai trò trong mạch: chi phí bộ nhớ và chọn hành động; chặn xác suất chỉ cho trung bình vô hướng i.i.d. cố định.
- Kết nối vào: bảng tổng hợp.
- Kết nối ra: giới hạn kết luận ở chủ đề 15.
- Nguồn: PDF tr. 29; slide E01–E02.

### 15. Phạm vi kết luận và cầu nối sang xấp xỉ hàm

- Nhóm: `cốt lõi`.
- Vai trò trong mạch: thu hồi mục tiêu, ba bài tập tổng hợp, mở Bài 07.
- Kết nối vào: toàn bài.
- Kết nối ra: Bài 07 thay bảng bằng hàm xấp xỉ.
- Nguồn: PDF tr. 23, 25–30; slide E03, X01–X03.

## Ký hiệu và quy ước

- $\mathcal S$: tập trạng thái hữu hạn; $\mathcal A(s)$: tập hành động hợp lệ tại $s$; $m_s=|\mathcal A(s)|$; $A_{\max}=\max_{s\in\mathcal S}|\mathcal A(s)|$.
- $\mathcal X=\{(s,a):s\in\mathcal S,\ a\in\mathcal A(s)\}$: tập cặp trạng thái–hành động hợp lệ.
- $\mathcal X_{\mathrm{reach}}\subseteq\mathcal X$: các cặp có thể được ghé từ phân phối khởi đầu dưới cơ chế thăm dò đang xét. Mọi kết luận hội tụ của bài chỉ phát biểu trên miền này.
- $Q_t(s,a)$: bảng ước lượng trên $\mathcal X$ trước cập nhật thứ $t$; $q_\pi(s,a)$ và $q_*(s,a)$: giá trị hành động thật của $\pi$ và giá trị tối ưu.
- $g_Q(s)\in\arg\max_{a\in\mathcal A(s)}Q(s,a)$: một hành động tham lam theo quy tắc phá hòa cố định.
- $\mu_t$: chính sách hành vi tại chuyển $t$; $\mu$: chính sách hành vi sinh dữ liệu; $\pi$: chính sách đích.
- $\rho_t=\pi(A_t\mid S_t)/\mu_t(A_t\mid S_t)$: tỉ số lấy mẫu độ quan trọng từng bước.
- $N(s,a)$, $N_k(s,a)$: bộ đếm cập nhật của cặp; $N_k(s,a)$ là giá trị đến hết lượt $k$.
- $\alpha_n(s,a)$: bước học ở lần cập nhật thứ $n$ của cặp $(s,a)$.
- $Y_t^{\mathrm{SARSA}}=R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$; $Y_t^Q=R_{t+1}+\gamma\max_aQ_t(S_{t+1},a)$.
- Chỉ số $k$ đánh lượt, $t$ đánh chuyển, $n$ đánh lần cập nhật riêng của từng cặp. Trạng thái kết thúc có giá trị 0. Toàn bài dùng $0\le\gamma\le1$; các định lý hội tụ dùng $0\le\gamma<1$ với MDP hữu hạn và phần thưởng bị chặn.

<!-- note-topic-id: lec-06-topic-01 -->
## Dự đoán sang điều khiển phi mô hình

Bài 05 giữ chính sách cố định và chỉ ước lượng giá trị. Khi mô hình chuyển và hàm thưởng không được cung cấp, tác tử chỉ quan sát các chuyển $(S_t,A_t,R_{t+1},S_{t+1})$. Câu hỏi của bài này: làm sao học trực tiếp một chính sách tốt, hoặc học $Q$ để suy ra chính sách tối ưu, chỉ từ dữ liệu tương tác.

Trực giác: điều khiển là vòng lặp hai việc. Chính sách hiện tại sinh trải nghiệm; trải nghiệm cập nhật bảng $Q$; bảng $Q$ mới lại suy ra chính sách tốt hơn. Thành phần làm phân phối dữ liệu thay đổi trong lúc học là chính sách hành vi, vì nó được suy ra lại từ $Q$ sau mỗi lần cập nhật.

Thiết lập của bài là MDP bảng hữu hạn với phần thưởng bị chặn. MC chỉ áp dụng khi lượt kết thúc gần chắc chắn và phần thưởng tích lũy hữu hạn. Bài toán theo lượt đặt giá trị trạng thái kết thúc bằng không. Nguồn tr. 15 ghi môi trường "tối đa 3 bước" nhưng không nêu quy ước phần thưởng tích lũy nếu cắt trước trạng thái kết thúc, nên bài không dùng mệnh đề này; giả thiết kết thúc gần chắc chắn của MC vẫn phải nêu riêng.

::: example Vòng học trên một lượt
Chính sách $\varepsilon$-tham lam theo $Q$ chọn hành động tại mỗi trạng thái; môi trường trả về phần thưởng và trạng thái kế tiếp; sau lượt (hoặc sau mỗi chuyển, tùy thuật toán), bảng $Q$ được cập nhật; chính sách được suy ra lại. Không bước nào dùng xác suất chuyển $P$ hay kỳ vọng thưởng $R$ của MDP.
:::

::: exercise Câu hỏi kiểm tra
Phân biệt dự đoán và điều khiển bằng một câu mỗi loại, và chỉ ra thành phần nào trong vòng học làm phân phối dữ liệu thay đổi.
:::

::: hint
So sánh đối tượng được học: giá trị của một chính sách cố định hay chính sách đang thay đổi.
:::

::: solution
Dự đoán: giữ $\pi$ cố định, ước lượng $v_\pi$ hoặc $q_\pi$. Điều khiển: vừa ước lượng $Q$, vừa cải thiện chính sách sinh dữ liệu. Thành phần làm phân phối dữ liệu thay đổi là chính sách hành vi, vì nó được suy ra lại từ bảng $Q$ sau mỗi lần cập nhật. (Nguồn: PDF tr. 3, 6; slide P01.)
:::

<!-- note-topic-id: lec-06-topic-02 -->
## Giá trị hành động và chính sách epsilon-tham lam

Vấn đề: để cải thiện chính sách cần so sánh các hành động tại cùng một trạng thái; $v_\pi(s)$ không cho phép so sánh đó, $q_\pi(s,a)$ cho phép. Vì mô hình không có, ta học bảng $Q$ trên miền $\mathcal X=\{(s,a):s\in\mathcal S,\ a\in\mathcal A(s)\}$, tức tập các cặp trạng thái–hành động hợp lệ đã nêu ở mục Ký hiệu; bảng là một hàm $Q:\mathcal X\to\mathbb R$ ước lượng từ mẫu.

Trực giác: từ bảng $Q$ suy ra hành động tham lam $g_Q(s)$ bằng quy tắc phá hòa tất định, ví dụ chọn hành động có chỉ số nhỏ nhất trong các hành động đạt cực đại. Lý do cần phá hòa tất định: nếu có nhiều hành động cùng đạt cực đại, quy tắc cố định giúp $g_Q(s)$ là một hàm xác định của bảng $Q$, để chính sách suy ra và các phát biểu sau này không phụ thuộc lựa chọn tùy ý. Quy tắc này chỉ làm $g_Q$ xác định; nó không tự là điều kiện đủ cho hội tụ. Chính sách tham lam một mình không thăm dò, nên điều khiển dùng chính sách $\varepsilon$-tham lam.

Định nghĩa. Với $m_s=|\mathcal A(s)|$ và $g_Q(s)$ đã cố định:

$$\pi_\varepsilon(a\mid s)=\begin{cases}1-\varepsilon+\varepsilon/m_s,&a=g_Q(s),\\ \varepsilon/m_s,&a\ne g_Q(s).\end{cases}$$

Cơ chế: với xác suất $1-\varepsilon$ chọn $g_Q(s)$; với xác suất $\varepsilon$ chọn đều trong $\mathcal A(s)$. Vì nhánh thăm dò cũng có thể chọn $g_Q(s)$, xác suất tổng của hành động này là $1-\varepsilon+\varepsilon/m_s$, mỗi hành động khác nhận $\varepsilon/m_s$.

::: example Tính xác suất $\varepsilon$-tham lam
Tại một trạng thái có $m_s=2$ hành động, $\varepsilon=0{,}25$, hành động tham lam là 1. Khi đó $\pi_\varepsilon(1\mid s)=1-0{,}25+0{,}25/2=0{,}875$ và $\pi_\varepsilon(0\mid s)=0{,}25/2=0{,}125$. Tổng hai xác suất bằng 1.
:::

::: exercise Câu hỏi kiểm tra
Với $m_s=4$, $\varepsilon=0{,}2$ và hành động tham lam là 2, tính $\pi_\varepsilon(a\mid s)$ cho từng $a\in\{0,1,2,3\}$ và kiểm tra tổng bằng 1.
:::

::: hint
Nhớ rằng nhánh thăm dò chọn đều trên cả $m_s$ hành động, gồm cả hành động tham lam.
:::

::: solution
Hành động 2: $1-0{,}2+0{,}2/4=0{,}85$. Ba hành động còn lại mỗi cái $0{,}2/4=0{,}05$. Tổng $0{,}85+3\cdot0{,}05=1$. (Nguồn: PDF tr. 10–11; slide A01.)
:::

<!-- note-topic-id: lec-06-topic-03 -->
## Theo chính sách và khác chính sách

Vấn đề: nguồn tr. 8 mô tả on/off-policy bằng mức độ "gần trùng nhau" giữa các chính sách, cách nói không xác định đối tượng học. Cách phát biểu đúng tách hai vai trò: chính sách hành vi $\mu$ sinh dữ liệu và chính sách đích $\pi$ là đối tượng được học hoặc tối ưu.

Trực giác: cùng một dữ liệu từ $\mu$ có thể dùng để học chính $\mu$ đang hành động, hoặc để học một $\pi$ khác. Cách hiệu chỉnh phụ thuộc thuật toán; khác chính sách không mặc nhiên cần lấy mẫu độ quan trọng.

| | Theo chính sách | Khác chính sách |
|---|---|---|
| Dữ liệu | $\mu$ | $\mu$ |
| Đối tượng học | cùng chính sách đang hành động | một chính sách đích $\pi$ khác |
| Ví dụ trong bài | Điều khiển MC đang xét; SARSA | Q-learning; đánh giá có hiệu chỉnh |

::: exercise Câu hỏi kiểm tra
Xác định $\mu$ và $\pi$ cho SARSA và cho Q-learning, và giải thích vì sao Q-learning là khác chính sách dù không nhân tỉ số lấy mẫu độ quan trọng.
:::

::: hint
Xem đích cập nhật của mỗi thuật toán: đích chứa hành động của chính sách nào?
:::

::: solution
SARSA: $\mu$ là chính sách $\varepsilon$-tham lam đang học và $\pi$ cũng chính là $\mu$, vì đích dùng $A_{t+1}$ do $\mu$ chọn. Q-learning: $\mu$ là chính sách hành vi $\varepsilon$-tham lam, còn $\pi$ là chính sách tham lam ngầm thể hiện qua cực đại $\max_aQ(S_{t+1},a)$ trong đích; vì đích không dùng hành động của $\mu$ nên thuật toán khác chính sách, và dạng bảng cập nhật chuẩn không cần nhân $\rho_t$. (Nguồn: PDF tr. 8; slide A02; xem áp dụng ở chủ đề 08, 10, 12.)
:::

<!-- note-topic-id: lec-06-topic-04 -->
## Chuỗi năm trạng thái và quy tắc số tất định

Vấn đề: ba thuật toán cần một ví dụ số chung để so sánh. Bài dùng một môi trường, một bảng khởi tạo $Q_0$ và một lượt cố định.

Môi trường: năm trạng thái theo hàng $A\ B\ C\ D\ E$; $A$ và $E$ kết thúc; $D$ là trạng thái bắt đầu; hành động 0 đi trái, 1 đi phải; môi trường tất định; $\gamma=1$ trong ví dụ; thưởng vào $A$ là $+1000$, vào $E$ là $+10$, các chuyển khác là $-1$. Bảng thống nhất:

| Trạng thái | $Q_0(s,0)$ | $Q_0(s,1)$ |
|---|---|---|
| B | 0 | 1 |
| C | 1 | 0 |
| D | 1 | 0 |

$Q$ ở trạng thái kết thúc bằng 0. Với bảng này, quan hệ chuyển tham lam là $D\to C$, $C\to B$, $B\to C$: nếu bỏ bộ đếm giới hạn thời gian, quan hệ đó có thể lặp giữa B và C. Sơ đồ B–C chỉ là quan hệ chuyển tham lam theo bảng $Q_0$ thống nhất, không phải MRP đầy đủ của môi trường có giới hạn thời gian. Lượt dùng để tính kết thúc ở $A$ sau đúng ba chuyển.

Giới hạn: quy tắc số chỉ để tái tạo lượt minh họa, không phải bộ lấy mẫu đúng của chính sách $\varepsilon$-tham lam và không dùng để kiểm chứng phân phối.

Quy tắc số tất định để cố định lượt:

- Sinh dãy: $u_t=(x_t+1)/5$ với $x_t=(2x_{t-1}+1)\bmod 5$, $x_0=1$, cho $u_1,u_2,u_3,u_4=0{,}8;\,0{,}6;\,0{,}2;\,0{,}4$.
- Mở cổng: đặt $\varepsilon=0{,}25$; thăm dò khi $u_t\le\varepsilon$.
- Chọn hành động khi cổng mở: dùng số kế, chọn hành động 0 nếu $u_{t+1}\le0{,}5$, ngược lại chọn 1.
- Áp dụng: tại D, $u_1=0{,}8>0{,}25$ nên khai thác, chọn hành động tham lam 0; tại C, $u_2=0{,}6>0{,}25$ nên khai thác, chọn 0; tại B, $u_3=0{,}2\le0{,}25$ mở cổng thăm dò, số kế $u_4=0{,}4\le0{,}5$ chọn hành động 0. Lượt là $(D,0)\to(C,0)\to(B,0)\to A$.

::: example Tái tạo lượt từ quy tắc số
Kiểm tra từng bước như trên: hai lần khai thác tại D và C theo hành động tham lam, một lần thăm dò tại B với số kế chọn 0, rồi chuyển sang $A$ và kết thúc. Ba cặp được ghé là $(D,0)$, $(C,0)$, $(B,0)$.
:::

::: exercise Câu hỏi kiểm tra
Dùng cùng quy tắc số nhưng đổi cổng thành $\varepsilon=0{,}5$: lượt mới đi qua những cặp nào, và kết thúc ở đâu?
:::

::: hint
Xét lần lượt $u_1,u_2,u_3$ với cổng mới; chỉ dùng số kế khi cổng thăm dò mở, và sau một lần dùng $u_{t+1}$ để chọn hành động, số tiếp theo là $u_{t+2}$.
:::

::: solution
Tại D, $u_1=0{,}8>0{,}5$: khai thác, chọn 0, đến C. Tại C, $u_2=0{,}6>0{,}5$: khai thác, chọn 0, đến B. Tại B, $u_3=0{,}2\le0{,}5$: thăm dò; số kế $u_4=0{,}4\le0{,}5$ chọn hành động 0, về C. Tại C, $u_5=0{,}8>0{,}5$: khai thác, chọn 0, đến B. Lượt tiếp tục luân chuyển B–C và không kết thúc sau ba chuyển; điều này cho thấy quan hệ chuyển tham lam có thể lặp khi bỏ giới hạn thời gian, đúng như cảnh báo ở đầu mục. Lưu ý: ví dụ này cố ý bỏ giới hạn thời gian mà nguồn không định nghĩa đầy đủ, nên chỉ dùng để minh họa quan hệ chuyển, không phải mô tả môi trường gốc. (Nguồn: PDF tr. 15–17; slide A03–A04.)
:::

<!-- note-topic-id: lec-06-topic-05 -->
## Điều khiển MC lần ghé đầu

Vấn đề: điều khiển MC đánh giá trực tiếp $Q(s,a)$ từ phần thưởng tích lũy đầy đủ của mỗi lần ghé đầu tiên đến một cặp trong lượt, rồi cải thiện chính sách theo $Q$ mới.

Trên lượt $(D,0)\to(C,0)\to(B,0)\to A$ với phần thưởng $(-1,-1,+1000)$ và $\gamma=1$:

$$G(D,0)=998,\qquad G(C,0)=999,\qquad G(B,0)=1000.$$

Tại D cộng đủ ba phần thưởng; tại C cộng hai phần thưởng cuối; tại B chỉ có phần thưởng vào A. Các cặp chỉ xuất hiện một lần nên lần ghé đầu và mọi lần ghé trùng nhau trên lượt này.

**Thuật toán điều khiển MC lần ghé đầu (dạng bảng).**

- Đầu vào: bộ sinh lượt kết thúc gần chắc chắn, tức $\Pr(T<\infty)=1$; phần thưởng tích lũy hữu hạn hoặc bị chặn; $\gamma$; lịch $\varepsilon_k$; ngân sách $K$; quy tắc lần ghé và bước học.
- Khởi tạo: $Q(s,a)$ tùy ý với $Q(\text{kết thúc},\cdot)=0$; $N(s,a)=0$ nếu dùng trung bình mẫu; $\pi_1$ là $\varepsilon_1$-tham lam theo $Q$.
- Vòng lặp, với $k=1,\dots,K$:
  1. Sinh một lượt đến trạng thái kết thúc; giả thiết việc này xảy ra gần chắc chắn.
  2. Tính phần thưởng tích lũy hữu hạn $G_t$ ngược từ cuối lượt.
  3. Với lần xuất hiện đầu của mỗi $(S_t,A_t)$: tăng $N(S_t,A_t)$; đặt $Q(S_t,A_t)\leftarrow Q(S_t,A_t)+(G_t-Q(S_t,A_t))/N(S_t,A_t)$.
  4. Với mỗi trạng thái đã ghé, cập nhật $\pi_{k+1}$ thành $\varepsilon_{k+1}$-tham lam theo $Q$.
- Dừng: hết $K$ lượt hoặc tiêu chuẩn đã định trước.
- Đầu ra: bảng $Q$ và chính sách $g_Q$.
- Chi phí: lượt dài $T_k$ tốn $O(T_kA_{\max})$ nếu cập nhật chính sách tại các trạng thái đã ghé; quét toàn bảng tốn thêm $O(\sum_s|\mathcal A(s)|)$; bộ nhớ $O(\sum_s|\mathcal A(s)|+T_k)$.
- Điều kiện áp dụng: lượt kết thúc gần chắc chắn ($\Pr(T<\infty)=1$) và phần thưởng tích lũy hữu hạn hoặc bị chặn. Nếu với xác suất dương, lượt không bao giờ kết thúc và $\gamma=1$, phần thưởng tích lũy có thể không xác định hoặc không hữu hạn.

::: example Hai bảng cập nhật trên cùng lượt
Trung bình mẫu (bước $1/N$, với $N$ mới bằng 1 cho cả ba cặp):

| Cặp | $Q_0$ | $G$ | $N$ mới | $Q_1$ |
|---|---|---|---|---|
| $(D,0)$ | 1 | 998 | 1 | 998 |
| $(C,0)$ | 1 | 999 | 1 | 999 |
| $(B,0)$ | 0 | 1000 | 1 | 1000 |

Các ô còn lại giữ nguyên; hành động 0 mới trở thành tham lam ở B, còn hành động 0 vẫn tham lam tại C và D. Cùng lượt với $\alpha=0{,}8$, tức $Q\leftarrow Q+0{,}8(G-Q)$:

| Cặp | $Q_0$ | $G$ | $Q_1$ |
|---|---|---|---|
| $(D,0)$ | 1 | 998 | 798,6 |
| $(C,0)$ | 1 | 999 | 799,4 |
| $(B,0)$ | 0 | 1000 | 800 |

Hai bảng khác nhau vì trung bình mẫu dùng bước $1/N=1$ cho mẫu đầu, còn $\alpha=0{,}8$ chỉ đi 80% quãng đường tới phần thưởng tích lũy. Ví dụ $\gamma=1$, $\alpha=0{,}8$ chỉ minh họa phép cập nhật, không phải bằng chứng hội tụ.
:::

::: exercise Câu hỏi kiểm tra
Trên cùng lượt, dùng $\alpha=0{,}5$: tính $Q_1$ của ba cặp $(D,0)$, $(C,0)$, $(B,0)$ và giải thích vì sao kết quả khác trung bình mẫu.
:::

::: hint
Áp dụng $Q_1=Q_0+\alpha(G-Q_0)$ cho từng cặp với $G$ đã cho.
:::

::: solution
$(D,0)$: $1+0{,}5(998-1)=499{,}5$. $(C,0)$: $1+0{,}5(999-1)=500$. $(B,0)$: $0+0{,}5(1000-0)=500$. Khác trung bình mẫu vì bước $0{,}5$ giữ 50% giá trị khởi tạo, trong khi trung bình mẫu với mẫu đầu dùng bước 1 và thay hoàn toàn giá trị khởi tạo bằng phần thưởng tích lũy. (Nguồn: PDF tr. 10, 17; slide B00–B04.)
:::

<!-- note-topic-id: lec-06-topic-06 -->
## Cải thiện cần $q_\pi$ chính xác

Vấn đề: hai bảng ở chủ đề 05 đều từ một lượt, nên chỉ từ một phần thưởng tích lũy, còn nhiễu. Khi nào việc cải thiện chính sách theo giá trị hành động bảo đảm giá trị trạng thái không giảm?

Trực giác: định lý cải thiện chính sách cần kỳ vọng đúng theo chính sách, tức $q_\pi$ chính xác, chứ không phải một mẫu. Một phần thưởng tích lũy và một bảng $Q$ còn nhiễu không bảo đảm giá trị tăng đơn điệu sau mỗi lượt.

**Mệnh đề cải thiện cho lớp $\varepsilon$-mềm.** Chính sách $\varepsilon$-tham lam là một trường hợp đặc biệt của lớp $\varepsilon$-mềm; mệnh đề sau áp dụng cho cả lớp này và là bước dẫn tới điều kiện GLIE ở chủ đề 07. Giả sử $\pi$ là chính sách $\varepsilon$-mềm, tức $\pi(a\mid s)\ge\varepsilon/m_s$ với mọi $a$, và đã biết đúng $q_\pi$. Lấy $\pi'$ là $\varepsilon$-tham lam theo $q_\pi$. Khi đó với mọi $s$:

$$\sum_a\pi'(a\mid s)\,q_\pi(s,a)=\frac{\varepsilon}{m_s}\sum_aq_\pi(s,a)+(1-\varepsilon)\max_aq_\pi(s,a)\ge v_\pi(s),$$

suy ra từ định lý cải thiện chính sách: $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s\in\mathcal S$.

Giới hạn: thuật toán MC chỉ có $Q$ ước lượng thay cho $q_\pi$ chính xác, nên không có bảo đảm tăng đơn điệu từng lượt; mệnh đề trên là cầu nối lý thuyết, ứng dụng của nó nằm ở điều kiện dài hạn GLIE ở chủ đề 07.

::: exercise Câu hỏi kiểm tra
Phát biểu đúng giả thiết của mệnh đề cải thiện: $\pi$ thuộc lớp nào và $\pi'$ được xây từ đại lượng nào? Vì sao một mẫu phần thưởng tích lũy không đủ để áp dụng mệnh đề?
:::

::: hint
So sánh hai đại lượng: $q_\pi$ chính xác và một giá trị $Q$ vừa cập nhật từ một phần thưởng tích lũy.
:::

::: solution
$\pi$ phải là chính sách $\varepsilon$-mềm với $\pi(a\mid s)\ge\varepsilon/m_s$; $\pi'$ là $\varepsilon$-tham lam theo $q_\pi$ chính xác. Một phần thưởng tích lũy chỉ cho một mẫu nhiễu của $q_\pi$, không cho kỳ vọng đúng, nên bất đẳng thức $\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$ chưa được bảo đảm với bảng ước lượng; do đó không suy ra tăng đơn điệu sau mỗi lượt. (Nguồn: PDF tr. 24; slide B05.)
:::

<!-- note-topic-id: lec-06-topic-07 -->
## GLIE và hội tụ điều khiển MC

Vấn đề: mệnh đề cải thiện cần $q_\pi$ chính xác về lâu dài; cần điều kiện nào để thăm dò không tắt sớm và ước lượng hội tụ?

Trực giác: hai việc phải xảy ra đồng thời — mọi cặp tiếp tục được ghé để trung bình mẫu hội tụ, và chính sách dần tham lam để tiến về tối ưu.

**Định nghĩa GLIE** (Greedy in the Limit with Infinite Exploration). Với quy tắc phá hòa tất định, dãy chính sách $\{\pi_k\}$ là GLIE khi đồng thời thỏa hai điều kiện: (1) thăm dò vô hạn, tức $N_k(s,a)\to\infty$ với mọi $(s,a)\in\mathcal X_{\mathrm{reach}}$; và (2) tham lam ở giới hạn, tức khối xác suất ngoài hành động tham lam tiến về 0:

$$N_k(s,a)\to\infty,\qquad \sum_{b\ne g_{Q_k}(s)}\pi_k(b\mid s)\to0.$$

Điều thứ nhất bảo đảm tiếp tục học mọi cặp khả đạt; điều thứ hai làm khối xác suất ngoài hành động tham lam tiến về 0. Ví dụ kinh điển là $\varepsilon_k$-tham lam với $\varepsilon_k=1/k$; tuy vậy, một lịch $\varepsilon$ cụ thể không tự chứng minh số lần ghé vô hạn, vì điều đó còn phụ thuộc phân phối khởi đầu và động lực MDP. Ví dụ về bước học thỏa điều kiện Robbins–Monro theo từng cặp: $\alpha_n(s,a)=1/n$ có $\sum_n1/n=\infty$ và $\sum_n1/n^2<\infty$.

**Định lý hội tụ điều khiển MC.** Nếu điều khiển Monte Carlo dùng một dãy chính sách GLIE, lượt kết thúc gần chắc chắn và phần thưởng tích lũy bị chặn, thì với trung bình mẫu $1/N$, hoặc bước Robbins–Monro theo từng cặp, $Q(s,a)\to q_*(s,a)$ trên $\mathcal X_{\mathrm{reach}}$ trong trường hợp bảng hữu hạn. Bước học $\alpha=0{,}8$ hằng không thuộc bảo đảm này.

::: exercise Câu hỏi kiểm tra
Liệt kê hai điều kiện của GLIE và giải thích vì sao $\varepsilon_k=1/k$ chưa tự bảo đảm điều kiện thứ nhất.
:::

::: hint
Điều kiện thứ nhất nói về bộ đếm $N_k(s,a)$; hãy hỏi điều gì quyết định cặp nào được ghé.
:::

::: solution
GLIE gồm: (1) mọi cặp khả đạt được ghé vô hạn lần, $N_k(s,a)\to\infty$; (2) chính sách hội tụ về tham lam, tổng xác suất ngoài hành động tham lam tiến về 0. Lịch $\varepsilon_k=1/k$ chỉ làm $\varepsilon_k\to0$, tức điều kiện (2); số lần ghé còn phụ thuộc phân phối khởi đầu và động lực MDP, nên điều kiện (1) phải được kiểm tra riêng trên cơ chế hành vi. (Nguồn: PDF tr. 25–26; slide B06.)
:::

<!-- note-topic-id: lec-06-topic-08 -->
## SARSA dạng bảng và ví dụ

Vấn đề: MC phải chờ hết lượt. Điều khiển TD cập nhật ngay sau mỗi chuyển bằng đích bootstrap một bước; câu hỏi cốt lõi là chọn đích nào. SARSA trả lời: dùng hành động kế tiếp mà chính sách đang học sẽ thực hiện.

Trực giác qua một chuyển: SARSA và Q-learning đều khởi động lại từ $Q_0$ ở chủ đề 04. Trên lượt cố định, sau chuyển $(C,0)\to B$ thì hành động kế tiếp thật sự là $A'=0$ (do thăm dò), dù hành động tham lam tại B là 1. Nếu đánh giá đúng hành vi, cập nhật ở C phải đọc $Q(B,0)$, vì đó là hành động hành vi sẽ thực hiện.

**Đích SARSA.** Với $A_{t+1}\sim\mu_t(\cdot\mid S_{t+1})$ là hành động chính sách đang học sẽ thực hiện:

$$Y_t^{\mathrm{SARSA}}=R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1}),$$
$$Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t(S_t,A_t)\bigl[Y_t^{\mathrm{SARSA}}-Q_t(S_t,A_t)\bigr].$$

Trong công thức theo thời gian, $\alpha_t(S_t,A_t)$ là bước học được dùng tại chuyển $t$; nếu lịch được đánh chỉ số theo số lần ghé thì đại lượng này bằng $\alpha_{N_t(S_t,A_t)}(S_t,A_t)$.

Tên SARSA đến từ chuỗi năm biến $(S_t,A_t,R_{t+1},S_{t+1},A_{t+1})$. Thuật toán theo chính sách vì $A_{t+1}$ đi vào đích được lấy theo chính sách đang học.

**Thuật toán SARSA dạng bảng.**

- Đầu vào: môi trường; $\gamma$; lịch theo lượt $\varepsilon_k$; lịch theo lần ghé $\alpha_n(s,a)$; ngân sách $K$.
- Khởi tạo: $Q(s,a)$ tùy ý với $Q(\text{kết thúc},\cdot)=0$; $N(s,a)=0$.
- Vòng lặp, với lượt $k=1,\dots,K$:
  1. Đặt lại $S\leftarrow S_0$; chọn $A$ theo $\varepsilon_k$-tham lam.
  2. Lặp: thực hiện $A$, quan sát $R,S'$; tăng $N(S,A)$; đặt $\alpha\leftarrow\alpha_{N(S,A)}(S,A)$.
     - Nếu $S'$ kết thúc: cập nhật với đích $R$; dừng vòng lượt.
     - Nếu chưa: chọn $A'$ theo $\varepsilon_k$-tham lam; cập nhật với đích $R+\gamma Q(S',A')$; gán $S\leftarrow S'$, $A\leftarrow A'$.
- Dừng: sau $K$ lượt hoặc tiêu chuẩn đặt trước.
- Đầu ra: bảng $Q$ và chính sách $g_Q$.
- Chi phí: chọn hành động tốn $O(A_{\max})$; bảng tốn $O(|\mathcal X|)$.

::: example SARSA trên lượt dùng chung, $\alpha=0{,}8$, cập nhật tại chỗ

| Chuyển | Đích SARSA | Ô trước | Ô sau |
|---|---|---|---|
| $(D,0)\to C$, $A'=0$ | $-1+Q(C,0)=0$ | $Q(D,0)=1$ | $0{,}2$ |
| $(C,0)\to B$, $A'=0$ | $-1+Q(B,0)=-1$ | $Q(C,0)=1$ | $-0{,}6$ |
| $(B,0)\to A$ | $1000$ | $Q(B,0)=0$ | $800$ |

Ở hàng hai, hành động kế tiếp thật sự tại B là trái do thăm dò. Hàng cuối dùng nhánh trạng thái kết thúc. Kết quả: $Q(D,0)=0{,}2$, $Q(C,0)=-0{,}6$, $Q(B,0)=800$.
:::

Kiểm tra cơ chế: trong kịch bản giả định thay hành động thăm dò tại B bằng hành động phải, đích tại C là $-1+Q(B,1)=0$ và giá trị mới là $1+0{,}8(0-1)=0{,}2$. Kịch bản này chỉ thay $A_{t+1}$ trong đích cập nhật $Q(C,0)$; nó không mô tả một lượt vật lý mới.

::: exercise Câu hỏi kiểm tra
Tính lại đích và giá trị mới của $Q(C,0)$ trong hai trường hợp $A_{t+1}=0$ và $A_{t+1}=1$ tại B, với $\alpha=0{,}8$, và chỉ ra trường hợp nào làm $Q(C,0)$ trùng với kết quả Q-learning.
:::

::: hint
Đích SARSA tại C là $-1+Q(B,A_{t+1})$; hai giá trị tại B là $Q(B,0)=0$ và $Q(B,1)=1$.
:::

::: solution
Trường hợp $A_{t+1}=0$: đích $-1+0=-1$, giá trị mới $1+0{,}8(-1-1)=-0{,}6$. Trường hợp $A_{t+1}=1$: đích $-1+1=0$, giá trị mới $1+0{,}8(0-1)=0{,}2$. Trường hợp thứ hai trùng với kết quả Q-learning tại ô $(C,0)$, vì Q-learning dùng cực đại $\max_aQ(B,a)=Q(B,1)=1$ thay cho hành động kế tiếp. (Nguồn: PDF tr. 12–14, 17–18; slide C00–C04.)
:::

<!-- note-topic-id: lec-06-topic-09 -->
## Hội tụ SARSA

Vấn đề: ví dụ số dùng $\gamma=1$ và $\alpha=0{,}8$ hằng; những lựa chọn đó không chứng minh hội tụ. Cần phát biểu đúng điều kiện.

**Định lý hội tụ SARSA dạng bảng.** Trong MDP hữu hạn, phần thưởng bị chặn và $0\le\gamma<1$, SARSA thỏa $Q(s,a)\to q_*(s,a)$ gần chắc chắn trên $\mathcal X_{\mathrm{reach}}$ nếu:

- chính sách hành vi là GLIE với quy tắc phá hòa tất định;
- mọi $(s,a)\in\mathcal X_{\mathrm{reach}}$ được cập nhật vô hạn lần;
- với từng cặp đó, $\sum_n\alpha_n(s,a)=\infty$ và $\sum_n\alpha_n(s,a)^2<\infty$ (điều kiện Robbins–Monro theo từng cặp).

Có thể đọc hai tổng là "tiếp tục học, nhưng nhiễu giảm dần". Bộ đếm $n$ là số lần cập nhật riêng của từng cặp, không phải chỉ số toàn cục. Kết luận chỉ phát biểu trên miền khả đạt; ví dụ $\gamma=1$ và $\alpha=0{,}8$ chỉ minh họa cập nhật.

::: exercise Câu hỏi kiểm tra
Một báo cáo dùng $\alpha=0{,}1$ hằng chung cho mọi cặp và $\varepsilon_k=1/k$, rồi kết luận SARSA hội tụ về $q_*$. Liệt kê các giả thiết của định lý mà báo cáo còn thiếu.
:::

::: hint
So từng giả thiết của định lý với những gì báo cáo cung cấp; chú ý chỉ số của bước học.
:::

::: solution
Báo cáo thiếu các giả thiết sau. (1) Bước học: $\alpha$ hằng không thỏa Robbins–Monro, vì $\sum_n\alpha_n(s,a)^2<\infty$ yêu cầu nhiễu bước học giảm dần; điều kiện phải áp dụng cho số lần cập nhật riêng của từng cặp $\alpha_n(s,a)$, không phải chỉ số toàn cục. (2) Cơ chế hành vi: $\varepsilon_k=1/k$ chỉ hướng tới tham lam ở giới hạn; GLIE còn cần mọi cặp khả đạt được ghé vô hạn lần, điều này phải do cơ chế hành vi bảo đảm. (3) Thiết lập: định lý cần MDP hữu hạn, thưởng bị chặn và $\gamma<1$. Với SARSA, mỗi lần ghé một cặp tạo đúng một cập nhật, nên điều kiện định lý là số lần cập nhật của từng cặp tiến tới vô hạn. (Nguồn: PDF tr. 27; slide C05.)
:::

<!-- note-topic-id: lec-06-topic-10 -->
## Q-learning dạng bảng và ví dụ

Vấn đề: cùng chuyển $(C,0)\to B$ với $R=-1$, hành vi đã chọn $A'=0$, nhưng bảng có hai giá trị khác nhau tại B: hành động đã lấy mẫu $Q(B,0)=0$ và hành động tham lam $\max_aQ(B,a)=Q(B,1)=1$. Nếu mục tiêu là chính sách tham lam, nên dùng đại lượng nào? Q-learning trả lời: dùng cực đại.

**Đích Q-learning.**

$$Y_t^Q=R_{t+1}+\gamma\max_{a\in\mathcal A(S_{t+1})}Q_t(S_{t+1},a),$$
$$Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t(S_t,A_t)\bigl[Y_t^Q-Q_t(S_t,A_t)\bigr].$$

Hành động $A_t$ do hành vi sinh; đích không dùng $A_{t+1}$ đã lấy mẫu. Đích tham lam biểu diễn chính sách đích, nên Q-learning là khác chính sách và có xu hướng học trực tiếp $q_*$.

**Thuật toán Q-learning dạng bảng.**

- Đầu vào: môi trường; $\gamma$; chính sách hành vi $\mu_t$ tại chuyển $t$ với cơ chế bảo đảm mọi cặp trong $\mathcal X_{\mathrm{reach}}$ được cập nhật vô hạn lần; lịch theo lần ghé $\alpha_n(s,a)$; ngân sách $K$.
- Khởi tạo: $Q(s,a)$ tùy ý với $Q(\text{kết thúc},\cdot)=0$; $N(s,a)=0$.
- Vòng lặp, với lượt $k=1,\dots,K$:
  1. Đặt lại $S\leftarrow S_0$.
  2. Lặp: chọn $A\sim\mu_t(\cdot\mid S)$; thực hiện $A$, quan sát $R,S'$; tăng $N(S,A)$; đặt $\alpha\leftarrow\alpha_{N(S,A)}(S,A)$.
     - Nếu $S'$ kết thúc: cập nhật với đích $R$; dừng vòng lượt.
     - Nếu chưa: cập nhật với đích $R+\gamma\max_aQ(S',a)$; gán $S\leftarrow S'$.
- Dừng: sau $K$ lượt hoặc tiêu chuẩn đặt trước.
- Đầu ra: bảng $Q$ và chính sách $g_Q$.
- Chi phí: chọn hành động và đọc cực đại tốn $O(A_{\max})$; bảng tốn $O(|\mathcal X|)$. Không lấy cực đại ở trạng thái kết thúc.

::: example Q-learning trên cùng lượt, $\alpha=0{,}8$, cập nhật tại chỗ

| Chuyển | Đích Q-learning | Ô trước | Ô sau |
|---|---|---|---|
| $(D,0)\to C$ | $-1+\max_aQ(C,a)=0$ | $Q(D,0)=1$ | $0{,}2$ |
| $(C,0)\to B$ | $-1+\max_aQ(B,a)=0$ | $Q(C,0)=1$ | $0{,}2$ |
| $(B,0)\to A$ | $1000$ | $Q(B,0)=0$ | $800$ |

Tại B, cực đại bằng 1 ở hành động phải dù lượt thực tế chọn trái; do đó đích ở C bằng 0 và $Q(C,0)$ thành $0{,}2$. Kết quả: $Q(D,0)=0{,}2$, $Q(C,0)=0{,}2$, $Q(B,0)=800$. Khác biệt duy nhất với SARSA trên lượt này nằm ở ô $(C,0)$, đến từ $Q(B,0)=0$ so với $\max_aQ(B,a)=1$.
:::

So đích trên một trục: MC dùng phần thưởng tích lũy; SARSA dùng hành động kế tiếp; Q-learning dùng cực đại ở trạng thái kế tiếp. Trên lượt này, chỉ SARSA dùng quyết định thăm dò tại B trong đích cập nhật ở C; Q-learning thay quyết định đó bằng cực đại; MC dùng toàn bộ kết quả nên quyết định tại B đi vào phần thưởng tích lũy nhưng không qua một đích bootstrap ở C.

::: exercise Câu hỏi kiểm tra
Giải thích vì sao $Q(C,0)$ sau cập nhật khác nhau giữa SARSA và Q-learning trên cùng lượt, và tính đích Q-learning tại chuyển $(C,0)\to B$.
:::

::: hint
So sánh hai đại lượng đi vào đích tại B: hành động đã lấy mẫu và hành động tham lam.
:::

::: solution
SARSA dùng hành động kế tiếp thật sự $A'=0$ nên đích là $-1+Q(B,0)=-1$, cho $Q(C,0)=-0{,}6$. Q-learning dùng cực đại nên đích là $-1+\max_aQ(B,a)=-1+1=0$, cho $Q(C,0)=0{,}2$. Khác biệt duy nhất đến từ $Q(B,0)=0$ so với $\max_aQ(B,a)=1$. (Nguồn: PDF tr. 20–21; slide D00–D04.)
:::

<!-- note-topic-id: lec-06-topic-11 -->
## Hội tụ Q-learning

Vấn đề: Q-learning tách chính sách hành vi khỏi đích học; điều kiện hội tụ của nó khác SARSA ở thành phần nào?

**Định lý hội tụ Q-learning dạng bảng.** Với MDP hữu hạn, phần thưởng bị chặn và $0\le\gamma<1$, nếu:

- mọi $(s,a)\in\mathcal X_{\mathrm{reach}}$ được cập nhật vô hạn lần dưới chính sách hành vi $\mu_t$;
- với từng cặp đó, $\sum_n\alpha_n(s,a)=\infty$ và $\sum_n\alpha_n(s,a)^2<\infty$;

thì $Q(s,a)\to q_*(s,a)$ gần chắc chắn trên $\mathcal X_{\mathrm{reach}}$.

Khác SARSA, Q-learning không yêu cầu thành phần “tham lam ở giới hạn” của GLIE: chính sách hành vi không cần hội tụ về tham lam. Thuật toán vẫn cần thành phần “thăm dò vô hạn”, tức số lần cập nhật của từng cặp trong $\mathcal X_{\mathrm{reach}}$ tiến tới vô hạn. Q-learning dạng bảng không cần tỉ số lấy mẫu độ quan trọng vì đích là toán tử Bellman tối ưu, không phụ thuộc hành động kế tiếp của hành vi. Ví dụ $\gamma=1$, $\alpha=0{,}8$ và một lượt chỉ minh họa phép cập nhật; chúng không chứng minh hội tụ.

::: exercise Câu hỏi kiểm tra
Liệt kê giả thiết hội tụ của Q-learning và chỉ ra giả thiết nào của SARSA không còn bắt buộc.
:::

::: hint
So sánh hai danh sách giả thiết ở chủ đề 09 và chủ đề này.
:::

::: solution
Q-learning cần: MDP hữu hạn, thưởng bị chặn, $0\le\gamma<1$; mọi $(s,a)\in\mathcal X_{\mathrm{reach}}$ được cập nhật vô hạn lần dưới $\mu_t$; bước học Robbins–Monro theo từng cặp. Giả thiết không còn bắt buộc là GLIE, cụ thể là hành vi tham lam ở giới hạn; chỉ cần độ phủ vô hạn. Cả hai vẫn cần Robbins–Monro theo từng cặp. (Nguồn: PDF tr. 28; slide D05.)
:::

<!-- note-topic-id: lec-06-topic-12 -->
## Dự đoán khác chính sách cho $V$

Vấn đề: khi dữ liệu sinh bởi chính sách hành vi $\mu$ nhưng ta muốn ước lượng giá trị của chính sách đích $\pi$ cố định, phân phối lấy mẫu của $\mu$ khác phân phối của $\pi$ và cần hiệu chỉnh.

Trực giác: các chuyển xảy ra theo $\mu$ với tần số khác $\pi$; nhân tỉ số xác suất đưa phân phối về của $\pi$. Điều kiện hỗ trợ yêu cầu hỗ trợ của $\pi(\cdot\mid s)$ là tập con của hỗ trợ của $\mu_t(\cdot\mid s)$ tại mỗi trạng thái khả đạt:

$$\forall(s,a)\in\mathcal X_{\mathrm{reach}}:\quad \pi(a\mid s)>0\Longrightarrow\mu_t(a\mid s)>0.$$

Nếu điều kiện hỗ trợ bị vi phạm, hành động mà $\pi$ cần có thể không xuất hiện trong dữ liệu và phép hiệu chỉnh không xác định. Khi điều kiện thỏa, với hành động đã lấy mẫu, $\rho_t=\pi(A_t\mid S_t)/\mu_t(A_t\mid S_t)$ là hữu hạn.

**TD(0) khác chính sách cho giá trị trạng thái:**

$$V(S_t)\leftarrow V(S_t)+\alpha_t\rho_t\bigl[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\bigr].$$

- Đầu vào: $\pi$, $\mu$, $V_0$, $\gamma$, lịch bước học $\alpha_t$ và luồng chuyển. Đầu ra: $V$; dừng theo ngân sách.
- Nếu $S_{t+1}$ kết thúc, đặt $V(S_{t+1})=0$.
- Mỗi chuyển tốn $O(1)$ chỉ khi các xác suất của $\pi$ và $\mu$ được lưu bảng và tra trực tiếp.
- Chỉ cần một hệ số lấy mẫu độ quan trọng từng bước, thường có phương sai thấp hơn lấy mẫu độ quan trọng MC trên cả quỹ đạo.

Giới hạn: đây là bài toán dự đoán $V$, không phải thuật toán điều khiển thứ tư. Q-learning là khác chính sách nhưng cập nhật bảng chuẩn không nhân tỉ số này.

::: example Ví dụ tỉ số từng bước
Nếu $\pi(A_t\mid S_t)=1$ và $\mu_t(A_t\mid S_t)=0{,}25$ thì $\rho_t=4$. Cập nhật nhân sai số TD với hệ số $4\alpha_t$.
:::

::: exercise Câu hỏi kiểm tra
Với $\pi(A_t\mid S_t)=0{,}5$, $\mu_t(A_t\mid S_t)=0{,}25$, $R_{t+1}=-1$, $\gamma=1$, $V(S_{t+1})=2$, $V(S_t)=1$ và $\alpha_t=0{,}1$: tính $\rho_t$ và giá trị mới của $V(S_t)$.
:::

::: hint
Tính sai số TD trước, rồi nhân với $\rho_t\alpha_t$.
:::

::: solution
$\rho_t=0{,}5/0{,}25=2$. Sai số TD là $-1+1\cdot2-1=0$, nên giá trị mới $V(S_t)=1+0{,}1\cdot2\cdot0=1$, không đổi. (Nguồn: PDF tr. 18–19; slide D06–D07.)
:::

<!-- note-topic-id: lec-06-topic-13 -->
## Ba thuật toán, ba cơ chế

Vấn đề: sau ba thuật toán, cần một bảng so sánh để tránh nhầm cơ chế. Phạm vi: chỉ ba thuật toán bảng của bài; không đưa DQN, actor-critic hoặc xấp xỉ hàm vào phân loại vì chúng cần giả thiết và cơ chế khác.

| | Điều khiển MC đang xét | SARSA | Q-learning |
|---|---|---|---|
| Đích | $G_t$ | $R+\gamma Q(S',A')$ | $R+\gamma\max_aQ(S',a)$ |
| Cập nhật | sau lượt | sau chuyển | sau chuyển |
| Quan hệ chính sách | theo chính sách | theo chính sách | khác chính sách |
| Điều kiện hành vi | GLIE và lượt kết thúc | GLIE | cập nhật vô hạn từng cặp |
| Bước học trong định lý | Robbins–Monro theo từng cặp | Robbins–Monro theo từng cặp | Robbins–Monro theo từng cặp |

GLIE gồm độ phủ vô hạn và tham lam ở giới hạn; bảo đảm hội tụ còn cần bước học phù hợp. Ba thuật toán khác nhau ở ba điểm: loại mục tiêu học (phần thưởng tích lũy đầy đủ hay bootstrap), theo chính sách hay khác chính sách, và cách cải thiện chính sách.

::: exercise Câu hỏi kiểm tra
Điền vào bảng so sánh: với mỗi thuật toán, nêu đích, thời điểm cập nhật, quan hệ chính sách và điều kiện hành vi.
:::

::: hint
Dùng đúng bốn hàng của bảng; điều kiện hành vi của MC gồm hai thành phần.
:::

::: solution
Điều khiển MC: đích $G_t$, cập nhật sau lượt, theo chính sách, cần GLIE và lượt kết thúc. SARSA: đích $R+\gamma Q(S',A')$, cập nhật sau chuyển, theo chính sách, cần GLIE. Q-learning: đích $R+\gamma\max_aQ(S',a)$, cập nhật sau chuyển, khác chính sách, cần cập nhật vô hạn từng cặp. (Nguồn: PDF tr. 22–23, 30; slide E00.)
:::

<!-- note-topic-id: lec-06-topic-14 -->
## Chi phí bảng và chặn Hoeffding

Vấn đề: chi phí tính toán của biểu diễn bảng không được nhầm với độ phức tạp mẫu.

Chi phí của biểu diễn bảng:

- Bộ nhớ của cả ba phương pháp: $O(|\mathcal X|)$; MC còn giữ lượt $O(T)$.
- SARSA đọc một giá trị $Q(S',A')$ trong $O(1)$, nhưng chọn $A'$ theo $\varepsilon$-tham lam có thể cần quét $\mathcal A(S')$.
- Q-learning đọc cực đại bằng cách quét $\mathcal A(S')$ nếu không duy trì cấu trúc phụ.
- Số mẫu để đạt một sai số cho trước còn phụ thuộc độ phủ, nhiễu, bước học và động lực MDP.

**Chặn Hoeffding và phạm vi.** Với chính sách và phân phối khởi đầu cố định, nếu $G_1,\dots,G_n$ là các phần thưởng tích lũy i.i.d. với $G_i\in[L,U]$ và $0<\delta<1$, thì với xác suất ít nhất $1-\delta$:

$$\left|\frac1n\sum_{i=1}^nG_i-\mathbb E[G]\right|\le(U-L)\sqrt{\frac{\log(2/\delta)}{2n}}.$$

Sai số giảm theo tốc độ $O(n^{-1/2})$ và chặn không phụ thuộc trực tiếp vào kích thước không gian trạng thái. Giới hạn: đây là chặn điểm cho một trung bình vô hướng cố định; không phải chặn đồng thời cho mọi trạng thái, mọi chính sách hoặc quá trình điều khiển thích nghi. Nếu phần thưởng có thể âm, phải dùng đúng khoảng $[L,U]$ của phần thưởng tích lũy.

::: exercise Câu hỏi kiểm tra
Với $n=100$, phần thưởng tích lũy bị chặn trong $[0,1000]$ và $\delta=0{,}05$: tính chặn Hoeffding cho sai số của trung bình mẫu, và nêu hai giả thiết bắt buộc để chặn áp dụng.
:::

::: hint
Thay trực tiếp vào công thức; $\log(2/\delta)=\log 40$.
:::

::: solution
Chặn là $(1000-0)\sqrt{\log(40)/(2\cdot100)}=1000\sqrt{3{,}6889/200}\approx1000\cdot0{,}1358\approx135{,}8$. Hai giả thiết bắt buộc: các phần thưởng tích lũy i.i.d. dưới cùng một chính sách và phân phối khởi đầu cố định, và phần thưởng tích lũy bị chặn trong khoảng đã cho với $0<\delta<1$. Chặn này không suy sang điều khiển thích nghi. (Nguồn: PDF tr. 29; slide E01–E02.)
:::

<!-- note-topic-id: lec-06-topic-15 -->
## Phạm vi kết luận và cầu nối sang xấp xỉ hàm

Thu hồi mục tiêu trong phạm vi bảng hữu hạn:

1. Điều khiển phi mô hình bảng học $Q$ từ trải nghiệm và cải thiện chính sách.
2. MC dùng phần thưởng tích lũy; SARSA dùng hành động kế tiếp; Q-learning dùng cực đại.
3. GLIE, độ phủ và Robbins–Monro là các giả thiết phải kiểm tra, phát biểu trên $\mathcal X_{\mathrm{reach}}$ với MDP hữu hạn, thưởng bị chặn và $\gamma<1$.

Ba bài tập dọc tổng hợp: tái tạo lượt và phản biện quy tắc số như một bộ lấy mẫu; đối chiếu ba bảng cập nhật và dùng kịch bản giả định đổi riêng $A_{t+1}$ tại B để tính lại cập nhật ở C; sửa một lập luận hội tụ bằng cách khôi phục miền hữu hạn, thưởng bị chặn, $\gamma<1$, tách GLIE của SARSA khỏi độ phủ và Robbins–Monro mà Q-learning vẫn cần.

Cầu nối: Bài 07 thay bảng giá trị bằng hàm xấp xỉ và xét lại các bảo đảm hội tụ; không mang nguyên định lý dạng bảng sang thiết lập đó.

::: exercise Câu hỏi kiểm tra
Một báo cáo ghi: "$\varepsilon_k=1/k$ và $\alpha=0{,}1$, nên SARSA chắc chắn hội tụ về $q_*$." Liệt kê giả thiết còn thiếu, đề xuất một lịch $\alpha_n(s,a)$ hợp lệ, và nêu phần nào của kết luận thay đổi đối với Q-learning.
:::

::: hint
Kiểm tra ba nhóm giả thiết: thiết lập MDP, cơ chế hành vi, và bước học theo từng cặp.
:::

::: solution
Cần MDP hữu hạn, thưởng bị chặn và $\gamma<1$; $\alpha$ hằng không thỏa Robbins–Monro, có thể dùng $\alpha_n(s,a)=1/n$ theo từng cặp. SARSA còn cần GLIE, tức ngoài $\varepsilon_k\to0$ phải có độ phủ vô hạn từng cặp khả đạt. Q-learning không cần hành vi tham lam ở giới hạn, nhưng cả hai vẫn cần mọi cặp trong $\mathcal X_{\mathrm{reach}}$ được cập nhật vô hạn và Robbins–Monro theo từng cặp. (Nguồn: PDF tr. 23, 25–30; slide E03, X01–X03.)
:::

## Tài liệu tham khảo

- Tạ Việt Cường. *Lecture 06: Điều khiển phi mô hình — Monte Carlo Control, SARSA, Q-Learning và tính chất hội tụ*. Bài giảng Học tăng cường, học kỳ 2 năm học 2025–2026, tr. 1–30. Tệp nguồn: `RL-hk2-2025-2026/lecture-06-model-free-control.pdf`.
- Bản trình chiếu đã hiệu chỉnh: `2627-1/lecture-06-dieu-khien-phi-mo-hinh.html`, các mã trang P00–P03, A00–A04, B00–B06, C00–C05, D00–D07, E00–E03, X01–X03.
