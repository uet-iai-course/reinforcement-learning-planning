# Bài 05 — Dự đoán phi mô hình

Trong chương này, chúng ta ước lượng giá trị $v_\pi$ của một chính sách cố định khi chưa biết mô hình môi trường, một bài toán dự đoán (prediction). Dữ liệu duy nhất là các lượt (episode) tương tác sinh theo chính sách đó. Monte Carlo lấy trung bình các lợi tức (return) quan sát được sau khi lượt kết thúc. Sai phân thời gian (temporal difference, TD) một bước, ký hiệu TD(0), cập nhật ngay sau mỗi chuyển. Hai phương pháp khác nhau ở mục tiêu cập nhật (update target), tức con số dùng để sửa bảng giá trị. Chúng được so sánh theo độ chệch (bias) của mục tiêu. Chúng cũng được so sánh theo phương sai (variance) và điều kiện hội tụ. Phần cuối xét nghiệm của chúng khi cập nhật theo lô (batch updating) trên một tập dữ liệu cố định.

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Tính lợi tức chiết khấu của mọi thời điểm trong một lượt bằng truy hồi ngược từ thời điểm kết thúc. Phân biệt lượt kết thúc với lượt bị cắt ngắn (truncated episode), theo Mục 2.1.
2. Liệt kê các lần ghé (visit) một trạng thái trong một lượt. Lập tập mẫu lợi tức theo quy tắc lần ghé đầu tiên (first-visit). Lập tập mẫu theo quy tắc mọi lần ghé (every-visit) và giải thích vì sao mỗi mẫu có kỳ vọng $v_\pi(s)$ (Mục 2.2–2.3).
3. Thực hiện một lượt dự đoán Monte Carlo với bước học (step size) $1/N(s)$ và với bước học hằng, nêu hai trục lựa chọn và điều kiện hội tụ của từng cấu hình (Mục 2.3–2.6).
4. Thực hiện TD(0) trên một lượt có chuyển vào trạng thái kết thúc (terminal state), với thứ tự đọc bảng rồi ghi bảng đúng. Xử lý được tự chuyển (self-transition), tức chuyển từ một trạng thái về chính nó (Mục 3).
5. Tính độ chệch và phương sai của mục tiêu cập nhật trên một mô hình nhỏ, và phát biểu đủ giả thiết của định lý hội tụ TD(0) dạng bảng (Mục 4).
6. Tính nghiệm Monte Carlo theo lô và nghiệm TD theo lô trên một tập dữ liệu cố định, rồi chọn phương pháp dự đoán kèm tiêu chuẩn và giả thiết (Mục 5, Tình huống 05.1–05.2).

<!-- note-topic-id: lec-05-topic-20 -->
## Kiến thức tiên quyết

Cụm "ghi chú Bài 0N, Mục k" chỉ mục $k$ của ghi chú Bài 0N; mỗi kết quả được dẫn như vậy được phát biểu lại dưới đây.

- **Quá trình quyết định Markov và chính sách Markov dừng** (ghi chú Bài 03, Mục 1 và Mục 3). Môi trường là một quá trình quyết định Markov (Markov decision process, MDP), mô tả bởi phân phối $p(s',r\mid s,a)$ của trạng thái sau và phần thưởng, không đổi theo thời gian. Chính sách Markov dừng $\pi(a\mid s)$ chọn hành động chỉ theo trạng thái hiện tại; kỳ vọng $\mathbb E_\pi$ lấy theo cả chính sách và môi trường.
- **Lợi tức chiết khấu** (ghi chú Bài 03, Mục 2). Lợi tức từ thời điểm $t$ là tổng các phần thưởng về sau, phần thưởng ở chuyển thứ $m$ sau $t$ nhân với $\gamma^{m-1}$. Mục 2.1 của chương này phát biểu lại định nghĩa cho lượt có thời điểm kết thúc.
- **Hàm giá trị và tính Markov của lợi tức** (ghi chú Bài 03, Mục 3). Giá trị trạng thái là $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$. Khi biết toàn bộ lịch sử $H_t=(S_0,A_0,R_1,\ldots,S_t)$, kỳ vọng của lợi tức chỉ phụ thuộc trạng thái cuối của lịch sử: $\mathbb E_\pi[G_t\mid H_t]=v_\pi(S_t)$.
- **Phương trình Bellman kỳ vọng** (ghi chú Bài 03, Mục 4). Với mọi trạng thái không kết thúc $s$, ta có $v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s]$, và giá trị của trạng thái kết thúc bằng $0$.
- **Đánh giá chính sách bằng quy hoạch động** (ghi chú Bài 04, Mục 1). Toán tử Bellman kỳ vọng là $(T_\pi V)(s)=\mathbb E_\pi[R_{t+1}+\gamma V(S_{t+1})\mid S_t=s]$. Với ma trận chuyển $P_\pi$ và vectơ phần thưởng kỳ vọng $r_\pi$, phương trình Bellman có dạng $(I-\gamma P_\pi)v_\pi=r_\pi$. Khi $\gamma<1$, $T_\pi$ là ánh xạ co hệ số $\gamma$ theo chuẩn cực đại; một ánh xạ co trên $\mathbb R^n$ có đúng một điểm bất động, và phép lặp từ mọi điểm đầu hội tụ về điểm đó. Hiệu $(T_\pi V)(s)-V(s)$ là phần dư Bellman (Bellman residual) tại $s$; chuẩn cực đại $\lVert T_\pi V-V\rVert_\infty$ của nó là phần dư Bellman của bảng $V$.
- **Công cụ xác suất** (học phần Xác suất thống kê). Luật kỳ vọng lặp: $\mathbb E[\mathbb E[X\mid Z]]=\mathbb E[X]$. Luật phương sai toàn phần: $\operatorname{Var}(X)=\operatorname{Var}(\mathbb E[X\mid Z])+\mathbb E[\operatorname{Var}(X\mid Z)]$ khi $X$ có mômen bậc hai hữu hạn. Luật mạnh số lớn: trung bình của $n$ biến độc lập cùng phân phối có kỳ vọng hữu hạn hội tụ hầu chắc chắn (almost surely) về kỳ vọng đó khi $n\to\infty$.

## Bảng ký hiệu

Bảng gồm các ký hiệu dùng xuyên suốt chương; ký hiệu cục bộ được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$; $\mathcal S^+$ | tập trạng thái không kết thúc; $\mathcal S$ cùng các trạng thái kết thúc | tập hữu hạn |
| $\mathcal A(s)$ | tập hành động hợp lệ tại $s$ | tập hữu hạn |
| $\pi(a\mid s)$ | chính sách cần đánh giá | phân phối trên $\mathcal A(s)$ với mỗi $s$; Markov, cố định |
| $p(s',r\mid s,a)$ | động lực môi trường, chưa biết | phân phối trên $\mathcal S^+\times\mathbb R$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động tại $t$; phần thưởng của chuyển từ $t$ sang $t+1$ | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathbb R$ |
| $H_t$ | lịch sử $(S_0,A_0,R_1,\ldots,S_t)$ | dãy hữu hạn |
| $t$; $T$ | thời điểm; thời điểm kết thúc của lượt | số nguyên không âm; hữu hạn hầu chắc chắn |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $\gamma=1$ chỉ dùng khi lượt kết thúc hầu chắc chắn |
| $G_t$ | lợi tức từ thời điểm $t$ | biến ngẫu nhiên thực; $G_T=0$ |
| $v_\pi(s)$ | giá trị thật của $s$ dưới $\pi$ | $\mathbb R$; bằng $0$ tại trạng thái kết thúc |
| $V$; $V_t$ | bảng ước lượng; toàn bộ bảng ngay trước cập nhật ở chuyển $t\to t+1$ | $\mathbb R^{\mathcal S^+}$, bằng $0$ tại trạng thái kết thúc |
| $N(s)$; $n$ | số mẫu hoặc số lần cập nhật của riêng trạng thái $s$; giá trị hiện tại của bộ đếm đó | số nguyên không âm |
| $g_i(s)$; $V_n(s)$ | mẫu lợi tức thứ $i$ được chọn tại $s$; ước lượng sau $n$ mẫu | $\mathbb R$ |
| $\alpha$; $\alpha_n(s)$ | bước học hằng; bước học ở lần cập nhật thứ $n$ của $s$ | $(0,1]$ |
| $Y_t$; $\delta_t$ | mục tiêu TD; sai số TD (TD error) | $\mathbb R$ |
| $Y^*$ | mục tiêu lý tưởng $R_{t+1}+\gamma v_\pi(S_{t+1})$ | $\mathbb R$ |
| $T_\pi$; $P_\pi$, $r_\pi$ | toán tử Bellman kỳ vọng; ma trận chuyển và vectơ phần thưởng kỳ vọng của $\pi$ | $\mathbb R^{\mathcal S}\to\mathbb R^{\mathcal S}$; ma trận, vectơ cỡ $\lvert\mathcal S\rvert$ |
| $R_{\max}$ | chặn trên của $\lvert R_{t+1}\rvert$ | số thực dương |
| $M$; $B$ | ngân sách lượt của Monte Carlo; ngân sách chuyển của TD(0) | số nguyên dương |
| $\mathcal D$ | tập dữ liệu cố định gồm các lượt đã quan sát | tập hữu hạn |
| $k$; $K$; $V_k$ | chỉ số lượt quét (sweep) dữ liệu; ngân sách lượt quét; bảng ở đầu lượt quét $k$ | số nguyên không âm; $\mathbb R^{\mathcal S^+}$ |
| $\Delta_k(s)$ | tổng gia số của lượt quét $k$ tại $s$ | $\mathbb R$ |
| $\theta$ | ngưỡng dừng của phép quét lặp | số thực dương |
| $\hat r(s)$, $\hat P(s'\mid s)$ | phần thưởng trung bình và tần suất chuyển tính từ $\mathcal D$ | $\mathbb R$; $[0,1]$ |
| $\mathrm L,\mathrm S,\mathrm X,\mathrm G$; $\mathrm A,\mathrm B$; $\mathrm x_1,\mathrm x_3,\mathrm x_4,\mathrm x_5$ | tên các ô và trạng thái trong ví dụ | nhãn, không phải biến |

Các quy ước đọc sau dùng trong cả chương.

- $R_{t+1}$ là phần thưởng nhận trên chuyển từ thời điểm $t$ sang $t+1$, nên phần thưởng đầu tiên sau $S_t$ mang chỉ số $t+1$.
- $\mathbb E_\pi[\cdot\mid S_t=s]$ lấy kỳ vọng theo chính sách $\pi$ và động lực môi trường, với điều kiện trạng thái tại thời điểm $t$ bằng $s$.
- Tên ô và trạng thái viết chữ đứng: $\mathrm S$ là một ô, $S_t$ là trạng thái tại thời điểm $t$; $\mathrm G$ là một ô, $G_t$ là lợi tức; $\mathrm B$ là một trạng thái, $B$ là ngân sách chuyển.
- Chữ $T$ không chỉ số là thời điểm kết thúc; $T_\pi$ là toán tử.
- Số liệu của "tàu đổ bộ thu nhỏ" và "dãy bảy ô" là số liệu sư phạm lấy từ bài giảng gốc (2025–2026). Số liệu Lunar Lander lấy từ một lần chạy đã nhúng trong notebook thực hành của bài, với gymnasium 1.3.0.

Giáo trình *Học máy thống kê* dùng bộ $\langle S,A,T,R,\gamma\rangle$ với hàm chuyển $T(s,a,s')$, phần thưởng $R(s,a,s')$ và giá trị $V^\pi$. Trong chương này, $p(s',r\mid s,a)$ thay cho cặp $T$, $R$, còn $v_\pi$ thay cho $V^\pi$; chữ $V$ dành cho bảng ước lượng.

## Bản đồ chủ đề

Nhóm **cốt lõi** tạo mạch chính; **cầu nối** phát biểu lại tiên quyết; **bổ sung** lấp hai khoảng trống cụ thể; **đọc thêm** nối hai mục tiêu cập nhật.

| Chủ đề (`note-topic-id`) | Nhóm | Mục | Vai trò → sản phẩm dùng tiếp |
|---|---|---|---|
| Tiên quyết (`lec-05-topic-20`) | cầu nối | Tiên quyết | Bellman kỳ vọng, $T_\pi$, công cụ xác suất → các chứng minh của Mục 2–5 |
| Bài toán dự đoán, mẫu chuyển (transition sample) (`-01`) | cốt lõi | 1.1 | Bài toán trung tâm, ví dụ xuyên suốt → dữ liệu của mọi phương pháp |
| Khung cập nhật chung (`-17`) | cốt lõi | 1.2 | Ước lượng cũ cộng bước nhân sai lệch → Định nghĩa 05.10 |
| Lượt và lợi tức (`-02`) | cốt lõi | 2.1 | Đại lượng được lấy mẫu → mẫu theo lần ghé |
| Lần ghé (`-06`) | cốt lõi | 2.2 | Kỳ vọng $v_\pi(s)$ của mỗi mẫu → ước lượng, hội tụ |
| Ước lượng Monte Carlo (`-04`) | cốt lõi | 2.3 | Trung bình mẫu → trung bình gia tăng |
| Trung bình gia tăng, bước hằng (`-18`) | cốt lõi | 2.3–2.4 | Mục tiêu cập nhật, hai trục lựa chọn → Thuật toán 05.13 |
| Thuật toán Monte Carlo (`-03`) | cốt lõi | 2.5 | Quy trình đầy đủ → Tình huống 05.1 |
| Không chệch (unbiased) và hội tụ Monte Carlo (`-19`) | cốt lõi | 2.6 | Điều kiện hội tụ → so sánh với TD(0) |
| Chệch của mọi lần ghé (`-21`) | bổ sung | 2.6 | Phạm vi của Định lý 05.17 |
| Mục tiêu một bước, sai số TD (`-07`) | cốt lõi | 3.1 | Mục tiêu khi lượt chưa kết thúc → TD(0) |
| Thuật toán TD(0) (`-08`) | cốt lõi | 3.2 | Quy trình, trường hợp biên, chi phí → Mục 4 |
| Ô tự chuyển (`-22`) | bổ sung | 3.2 | Tốc độ lan truyền trên số liệu thật → Tình huống 05.1 |
| Hai bảng trên cùng dữ liệu (`-09`) | cốt lõi | 4.1 | Hai cơ chế lan truyền → nhu cầu giá trị chuẩn |
| Giá trị chuẩn, độ lệch (`-05`) | cốt lõi | 4.1 | Đo sai số → tách nguồn sai số |
| Độ chệch của mục tiêu TD (`-10`) | cốt lõi | 4.2 | Kỳ vọng mục tiêu → phần dư Bellman |
| Dãy bảy ô (`-12`) | cốt lõi | 4.3 | Lượt dài → bảng phương sai |
| Phương sai của mục tiêu (`-13`) | cốt lõi | 4.3 | Định lý 05.28 → lựa chọn phương pháp |
| Hội tụ của TD(0) (`-11`) | cốt lõi | 4.4 | Robbins–Monro theo trạng thái → Mục 5 |
| Dữ liệu cố định, cập nhật theo lô (`-16`) | cốt lõi | 5 | Hai nghiệm theo lô → Tình huống 05.1, Bài 07 |
| Lựa chọn phương pháp (`-14`) | cốt lõi | Tình huống | Ba kết luận có điều kiện → Bài 06 |
| Tóm tắt chương (`-15`) | cốt lõi | Tóm tắt | Chuỗi kết quả → Bài 06, 07 |
| Sai số Monte Carlo là tổng sai số TD (`-23`) | đọc thêm | Đọc thêm | Nối hai mục tiêu → TD $n$ bước |

## 1. Bài toán dự đoán khi chưa biết mô hình

Trong Bài 04, chúng ta đánh giá một chính sách cố định bằng quy hoạch động: lặp $V\leftarrow T_\pi V$ hoặc giải $(I-\gamma P_\pi)V=r_\pi$ (ghi chú Bài 04, Mục 1). Cả hai cách đều đọc mô hình $P_\pi$, $r_\pi$.

Xét một tàu đổ bộ thu nhỏ trên dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$, xuất phát ở $\mathrm S$; chính sách luôn tiến về phía $\mathrm G$. Do nhiễu của động cơ, tàu tiến một ô với xác suất $0{,}8$ và bị đẩy lùi một ô với xác suất $0{,}2$. Vào $\mathrm L$ ("rơi") nhận $-1$, vào $\mathrm G$ ("nằm yên") nhận $+1$, mọi chuyển khác nhận $0$. Biết hai xác suất đó, phương trình Bellman kỳ vọng cho $v_\pi(\mathrm S)=11/21$ và $v_\pi(\mathrm X)=19/21$ (Ví dụ 05.14, Mục 4.1).

Tác tử không biết hai xác suất này; nó chỉ có hai lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$. Để ước lượng $v_\pi$ từ các lượt như vậy, chúng ta cần biết lấy mục tiêu cập nhật nào từ dữ liệu, cập nhật lúc nào, ước lượng có tiến tới $v_\pi$ không và dưới giả thiết nào, và khi dữ liệu không tăng thêm thì khớp dữ liệu theo tiêu chuẩn nào.

Chúng ta xây dựng Monte Carlo, lấy trung bình lợi tức sau khi lượt kết thúc, và TD(0), cập nhật sau mỗi chuyển bằng phần thưởng vừa nhận cộng giá trị ước lượng tại trạng thái kế tiếp. Chúng ta chứng minh mục tiêu Monte Carlo không chệch, mục tiêu TD chệch theo độ lệch của bảng, mục tiêu một bước lý tưởng có phương sai không lớn hơn, và cả hai phương pháp hội tụ về $v_\pi$ dưới những điều kiện bước học khác nhau.

![Sơ đồ sáu khối nối từ trái sang phải, dưới mỗi khối ghi phần tương ứng của chương: "Dữ liệu" (Mục 1, các lượt sinh theo chính sách cố định), "Lợi tức Monte Carlo" (Mục 2, mục tiêu là lợi tức đầy đủ sau khi lượt kết thúc), "Một bước TD" (Mục 3, mục tiêu là phần thưởng một bước cộng giá trị ước lượng tại trạng thái sau), "Giả thiết" (Mục 4, độ chệch, phương sai, điều kiện hội tụ), "Dữ liệu cố định" (Mục 5, quét lại một tập lượt không tăng thêm) và "Lựa chọn" (tình huống áp dụng, chọn phương pháp theo dữ liệu và giả thiết).](img/lec-05/learning-route.svg)

Hình trên là lộ trình của chương, đọc từ trái sang phải; dòng chữ dưới mỗi khối ghi phần tương ứng. Khối "Dữ liệu" là bài toán của Mục 1, còn hai khối kế tiếp là hai cách tạo mục tiêu cập nhật ở Mục 2 và Mục 3. Khối "Giả thiết" là phép so sánh hai mục tiêu qua độ chệch, phương sai và điều kiện hội tụ ở Mục 4. Khối "Dữ liệu cố định" là việc quét lại một tập lượt không tăng thêm ở Mục 5, và khối "Lựa chọn" là các tình huống áp dụng.

<!-- note-topic-id: lec-05-topic-01 -->
### 1.1 Mẫu chuyển và bài toán dự đoán

Một cách trực quan, mỗi bước tương tác cho biết một kết quả đã xảy ra, còn mô hình cho biết mọi kết quả có thể xảy ra cùng xác suất của chúng; giá trị $v_\pi(s)$ là một kỳ vọng theo mô hình, nên từ dữ liệu ta chỉ ước lượng được nó. Mô tả này chưa phải định nghĩa.

![Dãy bốn ô L, S, X, G. Từ S: sang X với xác suất 0,8 và thưởng 0, sang L với xác suất 0,2 và thưởng âm 1. Từ X: sang G với xác suất 0,8 và thưởng +1, sang S với xác suất 0,2 và thưởng 0. Hai ô L và G là trạng thái kết thúc với giá trị 0.](img/lec-05/short-walk.svg)

Trên hình, mỗi mũi tên ghi xác suất và phần thưởng của một chuyển. Hai ô biên là trạng thái kết thúc, có giá trị $0$; phần thưởng $\pm1$ nằm trên chuyển đi vào chúng. Các xác suất là mô hình mà tác tử không được biết.

::: example Ví dụ 05.1 (Tàu đổ bộ thu nhỏ: mô hình và hai lượt quan sát)
**Môi trường.** Tập trạng thái không kết thúc $\mathcal S=\{\mathrm S,\mathrm X\}$; tập đầy đủ $\mathcal S^+=\{\mathrm L,\mathrm S,\mathrm X,\mathrm G\}$, trong đó $\mathrm L$ là kết cục "rơi" và $\mathrm G$ là kết cục "nằm yên", cả hai là trạng thái kết thúc. Mỗi lượt bắt đầu ở $\mathrm S$.

**Chính sách.** Tại mọi trạng thái không kết thúc, chính sách chọn hành động duy nhất "tiến", ký hiệu $\mathrm{tien}$, với xác suất $1$.

**Động lực.** Sau hành động $\mathrm{tien}$, tàu sang ô bên phải với xác suất $0{,}8$ và sang ô bên trái với xác suất $0{,}2$. Phần thưởng là $-1$ khi đi vào $\mathrm L$, $+1$ khi đi vào $\mathrm G$, và $0$ cho mọi chuyển khác. Hệ số chiết khấu $\gamma=1$.

**Hai lượt quan sát.** Viết mỗi lượt thành dãy trạng thái và dãy phần thưởng:

| Lượt | Trạng thái $S_0,S_1,\ldots,S_T$ | Phần thưởng $R_1,\ldots,R_T$ | $T$ |
|---|---|---|---|
| $e_1$ | $\mathrm S,\mathrm X,\mathrm S,\mathrm X,\mathrm G$ | $0,0,0,1$ | $4$ |
| $e_2$ | $\mathrm S,\mathrm X,\mathrm S,\mathrm L$ | $0,0,-1$ | $3$ |

**Các mẫu chuyển của $e_1$.** Bốn chuyển cho bốn mẫu $(S_t,A_t,R_{t+1},S_{t+1})$:

$$
(\mathrm S,\mathrm{tien},0,\mathrm X),\quad(\mathrm X,\mathrm{tien},0,\mathrm S),\quad(\mathrm S,\mathrm{tien},0,\mathrm X),\quad(\mathrm X,\mathrm{tien},1,\mathrm G).
$$

**Kiểm tra lại.** Tổng phần thưởng của $e_1$ là $1$, của $e_2$ là $-1$.
:::

Từ bốn mẫu của $e_1$, tác tử biết chuyển $\mathrm X\to\mathrm S$ có thể xảy ra, nhưng không biết tần suất $0{,}2$ của nó. Định nghĩa sau phát biểu bài toán tổng quát.

::: definition Định nghĩa 05.1 (Bài toán dự đoán phi mô hình)
Cho tập trạng thái hữu hạn $\mathcal S^+$, trong đó $\mathcal S\subseteq\mathcal S^+$ là tập trạng thái không kết thúc, và một chính sách Markov dừng $\pi(a\mid s)$ được giữ cố định. Môi trường là Markov và dừng, với động lực $p(s',r\mid s,a)$ không đổi theo thời gian, và trạng thái $S_t$ được quan sát đầy đủ.

Một **mẫu chuyển** là bộ $(S_t,A_t,R_{t+1},S_{t+1})$ với $A_t\sim\pi(\cdot\mid S_t)$ và $(S_{t+1},R_{t+1})\sim p(\cdot,\cdot\mid S_t,A_t)$; thành phần $R_{t+1}$ là phần thưởng của chuyển từ thời điểm $t$ sang $t+1$.

**Dữ liệu theo chính sách** (on-policy) là một dãy lượt, mỗi lượt là một dãy mẫu chuyển nối tiếp nhau sinh theo $\pi$.

**Bài toán dự đoán phi mô hình** là: chỉ từ dữ liệu theo chính sách, không nhận $p$ làm đầu vào, tính một bảng $V:\mathcal S^+\to\mathbb R$ với $V(s)=0$ tại trạng thái kết thúc, sao cho $V(s)$ xấp xỉ $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ với mọi $s\in\mathcal S$.
:::

Định nghĩa có ba thành phần: đối tượng cần tìm là $v_\pi$ trên các trạng thái không kết thúc; đầu vào là các kết quả đã xảy ra, sinh theo chính sách đang đánh giá; giả thiết gồm chính sách cố định, môi trường Markov dừng, trạng thái quan sát đầy đủ.

Mẫu $(\mathrm S,\mathrm{tien},0,\mathrm X)$ của Ví dụ 05.1 thỏa định nghĩa. Một trường hợp không thỏa là bài thực hành Lunar Lander: quan sát liên tục được gộp thành ô, hai quan sát trong cùng một ô có thể có lợi tức kỳ vọng khác nhau, nên ô không chứa đủ thông tin Markov (Mục 2.2, Tình huống 05.1).

Bài toán dự đoán khác bài toán điều khiển ở chỗ chính sách không đổi trong quá trình học; cải thiện chính sách là nội dung Bài 06. Dữ liệu ở đây theo chính sách: chính sách sinh dữ liệu trùng chính sách cần đánh giá. So với Bài 04, đầu vào đổi từ $(P_\pi,r_\pi)$ sang các mẫu chuyển.

::: remark Nhận xét 05.2 (Mẫu, mô hình và giá trị chuẩn)
Ba nhầm lẫn thường gặp đều đến từ việc đồng nhất một mẫu với một kỳ vọng.

- Một mẫu có phần thưởng $0$ không cho biết phần thưởng kỳ vọng hay lợi tức kỳ vọng: mẫu $(\mathrm S,\mathrm{tien},0,\mathrm X)$ có phần thưởng $0$, nhưng $v_\pi(\mathrm S)=11/21$.
- Mô hình của tàu đổ bộ thu nhỏ chỉ dùng để tính giá trị chuẩn; không thuật toán nào của chương đọc các xác suất $0{,}8$, $0{,}2$.
- Dừng thu thập vì hết ngân sách không biến trạng thái cuối thành trạng thái kết thúc (Nhận xét 05.22).
:::

::: exercise Bài tập 05.1
Tàu đổ bộ thu nhỏ của Ví dụ 05.1 có $\mathcal S=\{\mathrm S,\mathrm X\}$, hành động duy nhất $\mathrm{tien}$, phần thưởng $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho chuyển khác, $\gamma=1$; tác tử không biết xác suất tiến và lùi. Tác tử quan sát một chuyển từ $\mathrm X$ về $\mathrm S$ với phần thưởng $0$.

(a) Viết mẫu chuyển tương ứng.
(b) Nêu đại lượng cần ước lượng.
(c) Nêu thông tin còn thiếu để đánh giá chính sách bằng quy hoạch động như ở Bài 04.
:::

::: hint
Phân biệt một kết quả đã xảy ra với phân phối của mọi kết quả có thể xảy ra từ cùng trạng thái và hành động.
:::

::: solution
(a) Mẫu là $(\mathrm X,\mathrm{tien},0,\mathrm S)$.

(b) Đại lượng cần ước lượng là $v_\pi(\mathrm S)$ và $v_\pi(\mathrm X)$, tức kỳ vọng lợi tức từ hai trạng thái không kết thúc dưới chính sách luôn tiến.

(c) Quy hoạch động cần $P_\pi$ và $r_\pi$: xác suất đi từ $\mathrm S$, $\mathrm X$ sang từng ô và phần thưởng kỳ vọng của mỗi trạng thái. Mẫu chỉ cho biết chuyển $\mathrm X\to\mathrm S$ có thể xảy ra, không cho biết xác suất $0{,}2$ của nó.

**Kiểm tra lại.** Với $r_\pi(\mathrm X)=0{,}8\cdot1+0{,}2\cdot0=0{,}8$, mẫu đang xét có phần thưởng $0$ khác $r_\pi(\mathrm X)$, nên một mẫu không thay được phần thưởng kỳ vọng.
:::

<!-- note-topic-id: lec-05-topic-17 -->
### 1.2 Khung chung của các quy tắc cập nhật

Để so sánh các phương pháp, chúng ta cần một ngôn ngữ chung. Về mặt ý tưởng, mọi phương pháp của chương sửa từng phần tử của bảng $V$ theo cùng một cách: ước lượng mới bằng ước lượng cũ cộng một phần, gọi là bước học, của khoảng cách tới một con số lấy từ dữ liệu, gọi là mục tiêu cập nhật. Mô tả này chưa phải định nghĩa; Định nghĩa 05.10 ở Mục 2.3 phát biểu nó sau ví dụ về trung bình mẫu.

Các phương pháp của chương khác nhau ở mục tiêu cập nhật và ở dữ liệu dùng để tạo mục tiêu:

- Monte Carlo dùng lợi tức đầy đủ của lượt, chỉ có sau khi lượt kết thúc (Mục 2).
- TD(0) dùng phần thưởng một bước cộng giá trị ước lượng tại trạng thái kế tiếp, có ngay sau mỗi chuyển (Mục 3).
- Cập nhật theo lô dùng một trong hai mục tiêu trên, nhưng quét lại một tập dữ liệu cố định nhiều lần (Mục 5).

Như vậy, chúng ta đã đặt bài toán dự đoán phi mô hình (Định nghĩa 05.1) trên tàu đổ bộ thu nhỏ và nêu khung cập nhật chung. Khung này chưa cho biết mục tiêu cụ thể; Mục 2 dùng lợi tức của lượt làm mục tiêu đầu tiên.

## 2. Lợi tức và ước lượng Monte Carlo

Sau Mục 1, chúng ta chưa có con số nào để đặt vào $V(\mathrm S)$ và $V(\mathrm X)$. Định nghĩa $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ gợi ý lấy trung bình các lợi tức quan sát được sau những lần tàu ở $s$. Muốn vậy, chúng ta cần định nghĩa lợi tức của một lượt có thời điểm kết thúc, quyết định lấy lợi tức nào khi $\mathrm S$ xuất hiện hai lần trong $e_1$, tính trung bình mà không lưu mọi mẫu, và chứng minh trung bình tiến tới $v_\pi(s)$; Mục 2.1–2.6 làm lần lượt các việc này.

<!-- note-topic-id: lec-05-topic-02 -->
### 2.1 Lượt và lợi tức

Trong $e_1$, phần thưởng $+1$ chỉ đến ở chuyển cuối. Một cách trực quan, lợi tức tại thời điểm $t$ là tổng các phần thưởng còn nhận từ sau $t$ đến khi lượt kết thúc, mỗi phần thưởng giảm theo số bước phải chờ; mô tả này chưa phải định nghĩa.

::: example Ví dụ 05.2 (Lợi tức của lượt $e_1$ tính ngược)
**Dữ kiện.** Lượt $e_1$ của Ví dụ 05.1: trạng thái $\mathrm S,\mathrm X,\mathrm S,\mathrm X,\mathrm G$ tại $t=0,\ldots,4$; phần thưởng $(R_1,R_2,R_3,R_4)=(0,0,0,1)$; lượt kết thúc tại $T=4$; hệ số chiết khấu $\gamma\in[0,1]$.

**Tính từ cuối lượt.** Sau thời điểm kết thúc không còn phần thưởng, nên $G_4=0$. Mỗi bước lùi lấy phần thưởng của chuyển kế tiếp cộng $\gamma$ nhân lợi tức vừa tính:

| $t$ | $4$ | $3$ | $2$ | $1$ | $0$ |
|---|---|---|---|---|---|
| $S_t$ | $\mathrm G$ | $\mathrm X$ | $\mathrm S$ | $\mathrm X$ | $\mathrm S$ |
| $R_{t+1}$ | không có | $1$ | $0$ | $0$ | $0$ |
| $G_t$ | $0$ | $1+\gamma\cdot0=1$ | $0+\gamma\cdot1=\gamma$ | $0+\gamma\cdot\gamma=\gamma^2$ | $\gamma^3$ |

**Hai giá trị của $\gamma$.** Với $\gamma=1$, ta được $G_0=G_1=G_2=G_3=1$. Với $\gamma=0{,}9$, ta được $(G_0,G_1,G_2,G_3)=(0{,}729;\ 0{,}81;\ 0{,}9;\ 1)$.

**Kiểm tra lại.** Cộng trực tiếp: phần thưởng $R_4=1$ nhận ở chuyển thứ tư tính từ $S_0$, nên mang hệ số $\gamma^{4-1}=\gamma^3$ trong $G_0$, khớp cột $t=0$.
:::

![Lượt e1: trạng thái S, X, S, X, G tại t bằng 0 đến 4; phần thưởng trên bốn chuyển là 0, 0, 0, 1; hàng G_t ghi 1, 1, 1, 1 và 0 tại G, ứng với gamma bằng 1; một ngoặc nét đứt đánh dấu phần đuôi sau t bằng 1 gồm ba chuyển cuối.](img/lec-05/episode-one.svg)

![Lượt e2: trạng thái S, X, S, L tại t bằng 0 đến 3; phần thưởng 0, 0, âm 1; hàng G_t ghi âm 1, âm 1, âm 1 và 0 tại L, ứng với gamma bằng 1.](img/lec-05/episode-two.svg)

Hai hình đặt mỗi lượt trên trục thời gian, phần thưởng ghi trên mũi tên, $G_t$ ghi dưới mỗi trạng thái khi $\gamma=1$. Ngoặc nét đứt của $e_1$ đánh dấu phần đuôi sau $t=1$, có tổng phần thưởng $0+0+1=1=G_1$. Các lợi tức bằng nhau trong mỗi lượt là hệ quả của $\gamma=1$ và việc chỉ có phần thưởng cuối, không phải tính chất chung.

::: definition Định nghĩa 05.3 (Lượt, thời điểm kết thúc, lợi tức)
Một **lượt** là một dãy $S_0,A_0,R_1,S_1,A_1,R_2,\ldots$ sinh theo $\pi$ và $p$, dừng tại **thời điểm kết thúc**

$$
T=\min\{t\ge0: S_t\notin\mathcal S\},
$$

tức thời điểm đầu tiên tàu vào một trạng thái kết thúc. Lượt **kết thúc hầu chắc chắn** khi $\Pr(T<\infty)=1$.

Với hệ số chiết khấu $\gamma\in[0,1]$ và $t<T$, **lợi tức** từ thời điểm $t$ là

$$
G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},
$$

và quy ước $G_T=0$. Trường hợp $\gamma=1$ chỉ dùng khi lượt kết thúc hầu chắc chắn.
:::

Lợi tức $G_t$ là biến ngẫu nhiên, phụ thuộc mọi hành động, phần thưởng và chuyển trạng thái từ $t$ đến $T$; phần thưởng đầu tiên $R_{t+1}$ không bị chiết khấu. Định nghĩa trùng với lợi tức của Bài 03 khi coi mọi phần thưởng sau $T$ bằng $0$.

Hai trường hợp giới hạn cho thấy vai trò của thời điểm kết thúc. Lượt bị cắt ngắn, như bị dừng ở bước $1000$ trong Lunar Lander khi tàu chưa rơi cũng chưa nằm yên, không có thời điểm kết thúc; tổng phần thưởng đã quan sát thiếu phần đuôi và không phải $G_0$. Với $\gamma=1$, một trạng thái tự chuyển mãi với phần thưởng $1$ cho tổng phân kỳ, nên định nghĩa chỉ cho $\gamma=1$ khi lượt kết thúc hầu chắc chắn.

Tách số hạng đầu khỏi tổng cho một đẳng thức giữa hai lợi tức liên tiếp, cơ sở của phép tính ngược ở Ví dụ 05.2 và của mục tiêu TD ở Mục 3.

::: proposition Mệnh đề 05.4 (Truy hồi của lợi tức)
**Giả thiết.** Lượt kết thúc tại $T$; $\gamma\in[0,1]$.

**Kết luận.** Với mọi $t<T$,

$$
G_t=R_{t+1}+\gamma G_{t+1}.
$$

**Điều kiện áp dụng.** Đẳng thức đúng cho từng lượt cụ thể, không cần lấy kỳ vọng.

**Phạm vi.** Với lượt bị cắt ngắn, vế phải tại thời điểm cuối cần $G$ của phần đuôi chưa quan sát, nên đẳng thức không cho phép tính ngược từ điểm cắt.
:::

::: proof Chứng minh Mệnh đề 05.4
Với $t<T$, tách số hạng $k=t$ rồi đổi chỉ số trong phần còn lại:

$$
\begin{aligned}
G_t&=R_{t+1}+\sum_{k=t+1}^{T-1}\gamma^{k-t}R_{k+1} &&\text{(tách } k=t\text{, hệ số } \gamma^0=1)\\
&=R_{t+1}+\gamma\sum_{k=t+1}^{T-1}\gamma^{k-(t+1)}R_{k+1} &&\text{(đặt } \gamma \text{ ra ngoài)}\\
&=R_{t+1}+\gamma G_{t+1} &&\text{(Định nghĩa 05.3).}
\end{aligned}
$$

Khi $t=T-1$, tổng ở dòng thứ hai rỗng và bằng $0=G_T$, nên đẳng thức vẫn đúng. $\square$
:::

Mệnh đề 05.4 tính mọi lợi tức của lượt bằng $T$ phép nhân và cộng, bắt đầu từ $G_T=0$.

Để lấy kỳ vọng và phương sai của $G_t$, chúng ta cần $G_t$ khả tích. Khi $\gamma<1$ và phần thưởng bị chặn, $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$; khi $\gamma=1$, bổ đề sau thay chặn này bằng một chặn cho độ dài lượt.

::: lemma Bổ đề 05.5 (Thời điểm kết thúc có đuôi hình học)
**Giả thiết.** $\mathcal S$ hữu hạn; $\pi$ cố định; môi trường Markov dừng; từ mọi trạng thái không kết thúc, lượt kết thúc hầu chắc chắn.

**Kết luận.** Tồn tại $\rho\in(0,1]$ sao cho với mọi trạng thái xuất phát và mọi số nguyên $j\ge0$,

$$
\Pr\bigl(T>j\lvert\mathcal S\rvert\bigr)\le(1-\rho)^j .
$$

Do đó $\mathbb E[T^m]<\infty$ với mọi $m\ge1$. Nếu thêm $\lvert R_{t+1}\rvert\le R_{\max}$ và $\gamma\le1$ thì $\lvert G_t\rvert\le R_{\max}(T-t)$ và $\mathbb E[G_t^2]\le R_{\max}^2\,\mathbb E[T^2]<\infty$.

**Điều kiện áp dụng.** Cần cả tính hữu hạn của $\mathcal S$ lẫn kết thúc hầu chắc chắn từ mọi trạng thái.

**Phạm vi.** Bổ đề không cho giá trị cụ thể của $\rho$.
:::

Chứng minh nằm ngoài phạm vi học phần; Bertsekas và Tsitsiklis (1996, chương 2) trình bày lập luận cho chính sách kết thúc hầu chắc chắn trong bài toán đường đi ngắn nhất ngẫu nhiên. Ý tưởng như sau. Từ mỗi trạng thái có một đường tới trạng thái kết thúc với xác suất dương, và bỏ các vòng lặp khỏi đường đó cho một đường dài không quá $\lvert\mathcal S\rvert$ bước, nên $\rho=\min_s\Pr_s(T\le\lvert\mathcal S\rvert)>0$. Theo tính Markov, mỗi khối $\lvert\mathcal S\rvert$ bước tiếp theo lại kết thúc với xác suất ít nhất $\rho$, nên xác suất chưa kết thúc giảm theo cấp số nhân, và mọi mômen của $T$ hữu hạn.

Trên tàu đổ bộ thu nhỏ, $\lvert\mathcal S\rvert=2$; từ $\mathrm S$, lượt kết thúc trong hai bước với xác suất $0{,}2+0{,}8^2=0{,}84$, và từ $\mathrm X$ với xác suất $0{,}8+0{,}2\cdot0{,}2=0{,}84$. Vậy $\rho=0{,}84$ và $\Pr(T>2j)\le0{,}16^j$. Nếu một trạng thái tự chuyển với xác suất $1$ thì $\rho=0$, nên bổ đề cần giả thiết kết thúc.

**Trong thực hành.** Notebook Lunar Lander tính $G_t$ theo Mệnh đề 05.4, duyệt lùi từ $G_T=0$ với $\gamma=0{,}99$. Các lượt bị cắt ngắn ở bước $1000$ không có $T$, nên phép tính ngược không bắt đầu được và Monte Carlo bỏ chúng; giới hạn $1000$ bước thay cho Bổ đề 05.5.

::: exercise Bài tập 05.2
(a) Trong một lượt, phần thưởng $+1$ là $R_{t+4}$ và mọi phần thưởng khác sau $t$ bằng $0$; hệ số chiết khấu $\gamma=0{,}99$. Tính $G_t$.

(b) Lượt $e_2$ của Ví dụ 05.1 có trạng thái $\mathrm S,\mathrm X,\mathrm S,\mathrm L$ và phần thưởng $(0,0,-1)$. Với $\gamma=0{,}9$, tính $G_2$, $G_1$, $G_0$ bằng Mệnh đề 05.4.
:::

::: hint
Phần thưởng ở chuyển thứ $m$ sau thời điểm $t$ mang hệ số $\gamma^{m-1}$. Với câu (b), bắt đầu từ $G_3=0$.
:::

::: solution
(a) Phần thưởng $R_{t+4}$ nhận ở chuyển thứ tư sau $t$, nên mang hệ số $\gamma^3$: $G_t=0{,}99^3=0{,}970299$.

(b) Lượt kết thúc tại $T=3$, nên $G_3=0$. Theo Mệnh đề 05.4:

$$
\begin{aligned}
G_2&=R_3+\gamma G_3=-1+0{,}9\cdot0=-1,\\
G_1&=R_2+\gamma G_2=0+0{,}9\cdot(-1)=-0{,}9,\\
G_0&=R_1+\gamma G_1=0+0{,}9\cdot(-0{,}9)=-0{,}81.
\end{aligned}
$$

**Kiểm tra lại.** Theo Định nghĩa 05.3, $G_0=\gamma^2R_3=0{,}81\cdot(-1)=-0{,}81$.
:::

<!-- note-topic-id: lec-05-topic-06 -->
### 2.2 Lần ghé và kỳ vọng của lợi tức sau lần ghé

Trong $e_1$, ô $\mathrm S$ xuất hiện tại $t=0$ và $t=2$, ô $\mathrm X$ tại $t=1$ và $t=3$. Chúng ta cần quyết định lợi tức nào được đưa vào trung bình và biết mỗi lợi tức được chọn có kỳ vọng $v_\pi(s)$ hay không. Một cách trực quan, khi tàu quay lại $\mathrm S$ ở $t=2$, phần lượt từ đó giống một lượt mới bắt đầu tại $\mathrm S$, vì tương lai chỉ phụ thuộc vị trí hiện tại; nhận xét này chưa phải chứng minh.

::: example Ví dụ 05.3 (Hai quy tắc lần ghé trên hai lượt)
**Dữ kiện.** Hai lượt của Ví dụ 05.1 với $\gamma=1$: $e_1$ có trạng thái $\mathrm S,\mathrm X,\mathrm S,\mathrm X,\mathrm G$ và mọi lợi tức bằng $1$; $e_2$ có trạng thái $\mathrm S,\mathrm X,\mathrm S,\mathrm L$ và mọi lợi tức bằng $-1$ (Ví dụ 05.2).

**Thời điểm ghé.** Trong $e_1$, $\mathrm S$ ở $t=0,2$ và $\mathrm X$ ở $t=1,3$. Trong $e_2$, $\mathrm S$ ở $t=0,2$ và $\mathrm X$ ở $t=1$.

**Lập tập mẫu.** Lấy lợi tức tại thời điểm sớm nhất của mỗi lượt, hoặc lấy lợi tức tại mọi thời điểm:

| Trạng thái | Chỉ thời điểm sớm nhất trong mỗi lượt | Mọi thời điểm |
|---|---|---|
| $\mathrm S$ | $(1,-1)$, trung bình $0$ | $(1,1,-1,-1)$, trung bình $0$ |
| $\mathrm X$ | $(1,-1)$, trung bình $0$ | $(1,1,-1)$, trung bình $1/3$ |

**Kiểm tra lại.** Tại $\mathrm X$, cột thứ ba có hai mẫu từ $e_1$ và một mẫu từ $e_2$, nên trung bình là $(1+1-1)/3=1/3$; kết cục của $e_1$ nhận trọng số $2/3$.
:::

::: definition Định nghĩa 05.6 (Lần ghé, lần ghé đầu tiên, mọi lần ghé)
Cho một lượt và một trạng thái $s\in\mathcal S$. Một **lần ghé** $s$ là một thời điểm $t<T$ với $S_t=s$. Gọi $t_1<t_2<\cdots<t_{N_e(s)}$ là các thời điểm ghé $s$ trong lượt, với $N_e(s)$ là số lần ghé.

Quy tắc **lần ghé đầu tiên** lấy một mẫu $G_{t_1}$ từ mỗi lượt có $N_e(s)\ge1$.

Quy tắc **mọi lần ghé** lấy $N_e(s)$ mẫu $G_{t_1},\ldots,G_{t_{N_e(s)}}$ từ mỗi lượt.
:::

Lần ghé là một thời điểm: hai lần ghé $\mathrm S$ trong $e_1$ là $t=0$ và $t=2$, mỗi lần có lợi tức riêng. Trong Ví dụ 05.3, cột thứ hai là quy tắc lần ghé đầu tiên, cột thứ ba là quy tắc mọi lần ghé. Khi $N_e(s)=0$, cả hai quy tắc không lấy mẫu nào từ lượt.

Hai quy tắc khác nhau ở số mẫu và quan hệ giữa các mẫu, không ở đối tượng ước lượng. Mẫu lần ghé đầu tiên từ các lượt độc lập thì độc lập; mẫu mọi lần ghé trong cùng một lượt dùng chung phần đuôi nên phụ thuộc nhau. Mệnh đề sau cho thấy cả hai loại mẫu có kỳ vọng $v_\pi(s)$.

::: proposition Mệnh đề 05.7 (Kỳ vọng của lợi tức sau lần ghé thứ $k$)
**Giả thiết.** Các giả thiết của Định nghĩa 05.1 và Bổ đề 05.5; phần thưởng bị chặn bởi $R_{\max}$; $s\in\mathcal S$ và $k\ge1$ với $\Pr(N_e(s)\ge k)>0$.

**Kết luận.**

$$
\mathbb E_\pi\bigl[G_{t_k}\mid N_e(s)\ge k\bigr]=v_\pi(s).
$$

**Điều kiện áp dụng.** Đúng cho mọi $k$, không riêng $k=1$, và cho mọi phân phối trạng thái đầu của lượt.

**Phạm vi.** Mệnh đề nói về từng mẫu. Nó không nói về trung bình của các mẫu mọi lần ghé trong một số hữu hạn lượt; Mục 2.6 xét trung bình đó.
:::

::: proof Chứng minh Mệnh đề 05.7
**Bước 1 (biến cố ghé lần thứ $k$ tại thời điểm $t$).** Biến cố $\{t_k=t\}$ nghĩa là trong $S_0,\ldots,S_t$ có đúng $k$ phần tử bằng $s$ và $S_t=s$. Biến cố này được xác định bởi lịch sử $H_t$, và trên biến cố đó $S_t=s$, $t<T$.

**Bước 2 (dùng tính Markov của lợi tức).** Theo tiên quyết của Bài 03, $\mathbb E_\pi[G_t\mid H_t]=v_\pi(S_t)$. Vì $\mathbf 1\{t_k=t\}$ là hàm của $H_t$, luật kỳ vọng lặp cho

$$
\begin{aligned}
\mathbb E_\pi\bigl[G_t\,\mathbf 1\{t_k=t\}\bigr]
&=\mathbb E_\pi\bigl[\mathbb E_\pi[G_t\mid H_t]\,\mathbf 1\{t_k=t\}\bigr] &&\text{(luật kỳ vọng lặp)}\\
&=\mathbb E_\pi\bigl[v_\pi(S_t)\,\mathbf 1\{t_k=t\}\bigr] &&\text{(tính Markov của lợi tức)}\\
&=v_\pi(s)\Pr(t_k=t) &&\text{(trên biến cố, } S_t=s).
\end{aligned}
$$

**Bước 3 (cộng theo $t$).** Các biến cố $\{t_k=t\}$, $t=0,1,\ldots$, rời nhau và hợp của chúng là $\{N_e(s)\ge k\}$. Cộng đẳng thức của Bước 2 theo $t$:

$$
\mathbb E_\pi\bigl[G_{t_k}\mathbf 1\{N_e(s)\ge k\}\bigr]=\sum_{t\ge0}\mathbb E_\pi\bigl[G_t\mathbf 1\{t_k=t\}\bigr]=v_\pi(s)\Pr\bigl(N_e(s)\ge k\bigr).
$$

Đổi thứ tự tổng và kỳ vọng hợp lệ vì $\sum_t\lvert G_t\rvert\mathbf 1\{t_k=t\}\le\max_{t<T}\lvert G_t\rvert\le R_{\max}T$, và $\mathbb E[T]<\infty$ theo Bổ đề 05.5. Chia hai vế cho $\Pr(N_e(s)\ge k)>0$ được kết luận. $\square$
:::

Mệnh đề 05.7 nói thời điểm ghé ngẫu nhiên không làm lệch kỳ vọng, miễn việc "đã ghé lần thứ $k$" chỉ được quyết định từ quá khứ. Giả thiết Markov dùng ở Bước 2; Bổ đề 05.5 chỉ dùng để đổi thứ tự tổng và kỳ vọng.

Hai giả thiết của mệnh đề có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ tính Markov của trạng thái: trong notebook Lunar Lander, ô gộp nhiều vị trí của tàu; trong một lượt, ô 3426 xuất hiện $48$ lần, với lợi tức $55{,}22$ ở lần ghé đầu tiên và trung bình $67{,}09$ trên cả $48$ lần. Một lượt không chứng minh hai kỳ vọng khác nhau, nhưng trên ô gộp không có lý do để chúng bằng nhau.
- Bỏ chính sách cố định: nếu chính sách đổi giữa lần ghé thứ nhất và lần ghé thứ hai, lợi tức sau lần ghé thứ hai đo giá trị của chính sách mới, nên không còn kỳ vọng $v_\pi(s)$ của chính sách cũ.

**Trong thực hành.** Trong notebook Lunar Lander, quy tắc mọi lần ghé cho khoảng sáu lần số mẫu của quy tắc lần ghé đầu tiên, vì một ô thường xuất hiện ở nhiều thời điểm liên tiếp. Ô gộp không bảo đảm giả thiết Markov, nên hai quy tắc có thể ước lượng hai đại lượng khác nhau (Tình huống 05.1).

::: exercise Bài tập 05.3
Một lượt mới của tàu đổ bộ thu nhỏ đi $\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,0,0,1)$; $\gamma=1$.

(a) Liệt kê các thời điểm ghé $\mathrm S$ và $\mathrm X$.
(b) Lập tập mẫu tại $\mathrm S$ theo hai quy tắc của Định nghĩa 05.6 và tính trung bình mẫu của mỗi tập.
(c) Giải thích vì sao mẫu tại lần ghé thứ ba của $\mathrm S$ vẫn có kỳ vọng $v_\pi(\mathrm S)$, dù thời điểm ghé thứ ba là ngẫu nhiên.
:::

::: hint
Lượt kết thúc tại $T=6$. Với câu (c), xác định biến cố "ghé $\mathrm S$ lần thứ ba tại thời điểm $t$" phụ thuộc vào những biến nào.
:::

::: solution
(a) Ô $\mathrm S$ ở $t=0,2,4$; ô $\mathrm X$ ở $t=1,3,5$.

(b) Với $\gamma=1$ và phần thưởng duy nhất khác $0$ là $R_6=1$, mọi lợi tức $G_0,\ldots,G_5$ bằng $1$. Lần ghé đầu tiên cho một mẫu $(1)$; mọi lần ghé cho ba mẫu $(1,1,1)$. Cả hai trung bình bằng $1$.

(c) Biến cố "lần ghé thứ ba của $\mathrm S$ xảy ra tại $t$" chỉ phụ thuộc $S_0,\ldots,S_t$, tức lịch sử $H_t$. Theo Mệnh đề 05.7 (Bước 2), khi biết $H_t$ và $S_t=\mathrm S$, kỳ vọng của $G_t$ là $v_\pi(\mathrm S)$, bất kể lịch sử dẫn tới $\mathrm S$ bằng đường nào.

**Kiểm tra lại.** Ba mẫu ở (b) bằng nhau vì $\gamma=1$; câu (c) nói về kỳ vọng trên mọi lượt có thể xảy ra.
:::

<!-- note-topic-id: lec-05-topic-04 -->
### 2.3 Ước lượng Monte Carlo và trung bình gia tăng

Khi đã có tập mẫu tại mỗi trạng thái, ta lấy trung bình của chúng làm ước lượng, như hai cột của Ví dụ 05.3. Định nghĩa sau cố định thứ tự các mẫu, để chuẩn bị cho cách tính trung bình gia tăng.

::: definition Định nghĩa 05.8 (Ước lượng Monte Carlo)
Cố định một quy tắc lần ghé (Định nghĩa 05.6). Với $s\in\mathcal S$, gọi $g_1(s),g_2(s),\ldots$ là các mẫu lợi tức được quy tắc đó chọn tại $s$, theo thứ tự lượt và trong mỗi lượt theo thứ tự thời gian. Sau $n\ge1$ mẫu, **ước lượng Monte Carlo** của $v_\pi(s)$ là

$$
V_n(s)=\frac1n\sum_{i=1}^{n}g_i(s).
$$

Khi $n=0$, bảng giữ giá trị khởi tạo $V_0(s)$.
:::

Chỉ số $n$ đếm mẫu của riêng trạng thái $s$, không phải thời điểm tương tác $t$ hay số lượt: sau hai lượt, $\mathrm X$ có $n=3$ mẫu theo mọi lần ghé và $n=2$ mẫu theo lần ghé đầu tiên. Hai cột của Ví dụ 05.3 là định nghĩa áp dụng với hai quy tắc. Bài giảng gốc (2025–2026, trang 18) lưu bộ đếm $N(s)$ và tổng các mẫu của từng trạng thái rồi lấy thương; cách lưu đó cho cùng $V_n(s)$.

So với Bài 04, ước lượng Monte Carlo thay kỳ vọng $\mathbb E_\pi[G_t\mid S_t=s]$ bằng trung bình mẫu, và mỗi trạng thái được ước lượng độc lập với các trạng thái khác: $V_n(\mathrm S)$ không dùng $V_n(\mathrm X)$. Đây là điểm khác với TD(0) ở Mục 3, nơi mục tiêu tại $\mathrm S$ đọc giá trị tại $\mathrm X$.

Nhầm lẫn thường gặp là coi $V_n(s)$ là giá trị của chính sách. Hai lượt trong Ví dụ 05.3 cho $V_2(\mathrm S)=0$ theo lần ghé đầu tiên, trong khi $v_\pi(\mathrm S)=11/21$; con số $0$ chỉ phản ánh rằng một lượt nằm yên và một lượt rơi có cùng trọng số.

<!-- note-topic-id: lec-05-topic-18 -->
Định nghĩa 05.8 cần tổng của mọi mẫu đã chọn, nên lưu danh sách mẫu tốn bộ nhớ tăng theo số mẫu. Chúng ta cần cập nhật trung bình chỉ từ trung bình hiện tại, số mẫu và mẫu mới. Một cách trực quan, mẫu mới lớn hơn trung bình cũ thì trung bình tăng, và mức tăng nhỏ dần khi đã có nhiều mẫu; mô tả này chưa phải công thức.

::: example Ví dụ 05.4 (Hai cách tính trung bình khi thêm mẫu $-1$)
**Dữ kiện.** Tại $\mathrm X$, theo mọi lần ghé, hai mẫu đầu là $(1,1)$ với trung bình $V_2(\mathrm X)=1$; mẫu thứ ba là $g_3(\mathrm X)=-1$ (Ví dụ 05.3).

**Cách thứ nhất, tính lại từ tổng.** Tổng của hai mẫu cũ bằng số mẫu nhân trung bình, tức $2\cdot1$. Thêm mẫu mới:

$$
V_3(\mathrm X)=\frac{2\cdot1+(-1)}{3}=\frac13 .
$$

**Cách thứ hai, sửa trung bình cũ.** Dịch trung bình cũ về phía mẫu mới một phần ba khoảng cách:

$$
V_3(\mathrm X)=1+\frac13\bigl(-1-1\bigr)=\frac13 .
$$

**Diễn giải.** Khoảng cách từ trung bình cũ $1$ tới mẫu mới $-1$ là $2$; trung bình mới dịch $2/3$, tức một phần ba khoảng cách, đúng bằng $1/n$ với $n=3$.

**Kiểm tra lại.** Hai cách cho cùng $1/3$, khớp cột mọi lần ghé tại $\mathrm X$ trong Ví dụ 05.3.
:::

Cách thứ hai chỉ cần ba số: trung bình cũ, số mẫu và mẫu mới. Mệnh đề sau chứng minh nó đúng với mọi $n$.

::: proposition Mệnh đề 05.9 (Trung bình gia tăng)
**Giả thiết.** $V_n(s)$ là ước lượng Monte Carlo của Định nghĩa 05.8, $n\ge1$; $V_0(s)$ là giá trị khởi tạo tùy ý.

**Kết luận.**

$$
V_n(s)=V_{n-1}(s)+\frac1n\bigl[g_n(s)-V_{n-1}(s)\bigr].
$$

**Điều kiện áp dụng.** Bộ đếm $n$ thuộc riêng trạng thái $s$ và được tăng trước khi dùng bước $1/n$.

**Phạm vi.** Đẳng thức tái tạo đúng trung bình số học; với bước khác $1/n$, kết quả không còn là trung bình số học (Mệnh đề 05.11).
:::

::: proof Chứng minh Mệnh đề 05.9
**Bước 1 ($n=1$).** Vế phải bằng $V_0(s)+g_1(s)-V_0(s)=g_1(s)=V_1(s)$, bất kể $V_0(s)$.

**Bước 2 ($n\ge2$).** Tổng của $n-1$ mẫu đầu bằng $(n-1)V_{n-1}(s)$ theo Định nghĩa 05.8, nên

$$
\begin{aligned}
V_n(s)&=\frac1n\Bigl[(n-1)V_{n-1}(s)+g_n(s)\Bigr] &&\text{(tách mẫu thứ } n\text{)}\\
&=\Bigl(1-\frac1n\Bigr)V_{n-1}(s)+\frac1n g_n(s) &&\text{(chia từng số hạng)}\\
&=V_{n-1}(s)+\frac1n\bigl[g_n(s)-V_{n-1}(s)\bigr] &&\text{(nhóm theo } \tfrac1n\text{).}
\end{aligned}
$$

$\square$
:::

Đẳng thức có dạng "ước lượng cũ cộng bước nhân sai lệch". Đại lượng $g_n(s)-V_{n-1}(s)$ là sai lệch giữa mẫu mới và ước lượng cũ; bước $1/n$ giảm dần, nên mỗi mẫu mới thay đổi trung bình ít hơn mẫu trước. Bước 1 của chứng minh cho thấy mẫu đầu tiên xóa hoàn toàn giá trị khởi tạo. Ta đặt tên cho cấu trúc này vì TD(0) ở Mục 3 dùng lại nó với một mục tiêu khác.

::: definition Định nghĩa 05.10 (Mục tiêu cập nhật, bước học, quy tắc cập nhật)
Một **quy tắc cập nhật** cho phần tử $V(s)$ của bảng có dạng

$$
V(s)\leftarrow V(s)+\alpha\bigl[Y-V(s)\bigr],
$$

trong đó $Y\in\mathbb R$ là **mục tiêu cập nhật**, một số tạo ra từ dữ liệu; $\alpha\in(0,1]$ là **bước học**; và $Y-V(s)$ là **sai lệch** giữa mục tiêu và ước lượng cũ. Mọi phần tử khác của bảng giữ nguyên.
:::

Mệnh đề 05.9 là trường hợp $Y=g_n(s)$, $\alpha=1/n$. Định nghĩa không nói mục tiêu phải bằng giá trị thật: lợi tức $g_n(s)$ là một mẫu ngẫu nhiên có kỳ vọng $v_\pi(s)$ theo Mệnh đề 05.7, không phải $v_\pi(s)$. Đây là khung đã nêu bằng lời ở Mục 1.2; Monte Carlo và TD(0) là hai lựa chọn của $Y$ trong cùng khung, và Mục 4 so sánh hai lựa chọn này qua kỳ vọng và phương sai của $Y$.

Với một mục tiêu $Y$ cho trước, quy tắc của Định nghĩa 05.10 là một bước giảm gradient của hàm $\tfrac12\bigl(Y-V(s)\bigr)^2$ theo biến $V(s)$. Đạo hàm của hàm này là $-\bigl(Y-V(s)\bigr)$, nên trừ $\alpha$ nhân đạo hàm khỏi $V(s)$ cho đúng quy tắc trên. Với mục tiêu Monte Carlo $Y=G_t$, mục tiêu không phụ thuộc bảng và có kỳ vọng $v_\pi(s)$ theo Mệnh đề 05.7, nên đạo hàm có kỳ vọng $-\bigl(v_\pi(s)-V(s)\bigr)$, tức đạo hàm của $\tfrac12\bigl(v_\pi(s)-V(s)\bigr)^2$. Cập nhật Monte Carlo vì vậy là một bước gradient ngẫu nhiên (stochastic gradient) thật trên bình phương khoảng cách tới $v_\pi(s)$.

Mục tiêu TD của Mục 3 là $Y_t=R_{t+1}+\gamma V(S_{t+1})$, chứa giá trị của chính bảng. Quy tắc vẫn giữ $Y_t$ cố định khi lấy đạo hàm, tức bỏ số hạng $\gamma\bigl(Y_t-V(S_t)\bigr)$, là đạo hàm của $\tfrac12\bigl(Y_t-V(S_t)\bigr)^2$ theo biến $V(S_{t+1})$ khi $S_{t+1}\ne S_t$; cập nhật khi đó được gọi là bán gradient (semi-gradient). Sutton và Barto (2018, §9.3, trang 201–202) gọi hai cách cập nhật này là Monte Carlo gradient và TD(0) bán gradient. Bài 07 dùng cách đọc này khi thay bảng bằng hàm có tham số.

### 2.4 Bước học hằng và bốn cấu hình Monte Carlo

Với bước $1/n$, mẫu thứ $1000$ chỉ dịch ước lượng một phần nghìn khoảng cách. Bài giảng gốc (2025–2026, trang 21) thay $1/n$ bằng hằng số $\alpha$ để theo kịp môi trường thay đổi theo thời gian, trường hợp nằm ngoài giả thiết môi trường dừng của chương; bài giảng gốc và Bài tập tuần 5 (bài 7) dùng $\alpha=0{,}5$. Chúng ta cần biết bước hằng đặt trọng số cho các mẫu như thế nào. Một cách trực quan, mỗi mẫu mới luôn nhận cùng một phần $\alpha$, nên các mẫu cũ mờ dần theo cấp số nhân; mô tả này chưa phải mệnh đề.

::: example Ví dụ 05.5 (Bốn cấu hình Monte Carlo trên hai lượt)
**Dữ kiện.** Hai lượt $e_1$, $e_2$ của Ví dụ 05.1, $\gamma=1$; mọi lợi tức của $e_1$ bằng $1$, của $e_2$ bằng $-1$ (Ví dụ 05.2). Mỗi cấu hình khởi tạo riêng $V(\mathrm S)=V(\mathrm X)=0$; bước hằng dùng $\alpha=0{,}5$. Mỗi ô ghi $(V(\mathrm S),V(\mathrm X))$.

| Cấu hình | Sau $e_1$ | Sau $e_2$ |
|---|---|---|
| Lần ghé đầu tiên, trung bình mẫu | $(1,1)$ | $(0,0)$ |
| Mọi lần ghé, trung bình mẫu | $(1,1)$ | $(0,1/3)$ |
| Lần ghé đầu tiên, $\alpha=0{,}5$ | $(0{,}5;\ 0{,}5)$ | $(-0{,}25;\ -0{,}25)$ |
| Mọi lần ghé, $\alpha=0{,}5$ | $(0{,}75;\ 0{,}75)$ | $(-0{,}5625;\ -0{,}125)$ |

**Hàng thứ ba, từng bước.** Tại $\mathrm X$, hai mẫu $(1,-1)$ cho $0+0{,}5\cdot(1-0)=0{,}5$ rồi $0{,}5+0{,}5\cdot(-1-0{,}5)=-0{,}25$; viết lại, $-0{,}25=0{,}25\cdot0+0{,}25\cdot1+0{,}5\cdot(-1)$: giá trị khởi tạo còn ảnh hưởng và mẫu mới hơn có trọng số lớn hơn.

**Hàng cuối, từng bước.** Trong $e_1$, mỗi trạng thái nhận hai mẫu $1$: $0\to0{,}5\to0{,}75$. Trong $e_2$, $\mathrm S$ nhận hai mẫu $-1$:

$$
\begin{aligned}
0{,}75+0{,}5\cdot(-1-0{,}75)&=-0{,}125,\\
-0{,}125+0{,}5\cdot(-1+0{,}125)&=-0{,}5625,
\end{aligned}
$$

còn $\mathrm X$ nhận một mẫu $-1$: $0{,}75+0{,}5\cdot(-1-0{,}75)=-0{,}125$.

**Kiểm tra lại.** Hàng thứ hai: tại $\mathrm S$, bốn mẫu $(1,1,-1,-1)$ có trung bình $0$; tại $\mathrm X$, ba mẫu $(1,1,-1)$ có trung bình $1/3$, khớp Ví dụ 05.3.
:::

Hàng thứ ba của Ví dụ 05.5 gợi ý rằng sau $n$ mẫu, giá trị khởi tạo có trọng số $(1-\alpha)^n$ và mẫu thứ $i$ có trọng số $\alpha(1-\alpha)^{n-i}$. Mệnh đề sau chứng minh điều đó.

::: proposition Mệnh đề 05.11 (Trọng số của bước học hằng)
**Giả thiết.** $V_n=V_{n-1}+\alpha[g_n-V_{n-1}]$ với $n\ge1$, hằng số $\alpha\in(0,1]$, giá trị khởi tạo $V_0$.

**Kết luận.** Với mọi $n\ge1$,

$$
V_n=(1-\alpha)^nV_0+\sum_{i=1}^{n}\alpha(1-\alpha)^{n-i}g_i ,
$$

và tổng các trọng số $(1-\alpha)^n+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}$ bằng $1$.

**Điều kiện áp dụng.** Mọi dãy mẫu, không cần giả thiết xác suất.

**Phạm vi.** Với $0<\alpha<1$, trọng số giảm theo tuổi của mẫu; với $\alpha=1$, $V_n=g_n$ với mọi $n\ge1$.
:::

::: proof Chứng minh Mệnh đề 05.11
**Bước 1 (cơ sở quy nạp).** Với $n=1$: $V_1=V_0+\alpha(g_1-V_0)=(1-\alpha)V_0+\alpha g_1$, đúng dạng cần chứng minh.

**Bước 2 (bước quy nạp).** Giả sử công thức đúng với $n-1$. Viết lại quy tắc thành $V_n=(1-\alpha)V_{n-1}+\alpha g_n$ rồi thế giả thiết quy nạp:

$$
\begin{aligned}
V_n&=(1-\alpha)\Bigl[(1-\alpha)^{n-1}V_0+\sum_{i=1}^{n-1}\alpha(1-\alpha)^{n-1-i}g_i\Bigr]+\alpha g_n &&\text{(giả thiết quy nạp)}\\
&=(1-\alpha)^nV_0+\sum_{i=1}^{n-1}\alpha(1-\alpha)^{n-i}g_i+\alpha(1-\alpha)^{0}g_n &&\text{(nhân vào)}\\
&=(1-\alpha)^nV_0+\sum_{i=1}^{n}\alpha(1-\alpha)^{n-i}g_i &&\text{(gộp số hạng } i=n\text{).}
\end{aligned}
$$

**Bước 3 (tổng trọng số).** Áp dụng công thức vừa chứng minh cho dãy $V_0=1$, $g_i=1$ với mọi $i$: quy tắc giữ $V_n=1$ với mọi $n$, nên tổng các trọng số bằng $1$. $\square$
:::

Theo Mệnh đề 05.11, mẫu cách lần cập nhật hiện tại $j$ lần có trọng số $\alpha(1-\alpha)^j$; với $\alpha=0{,}5$ là $0{,}5$, $0{,}25$, $0{,}125$. So với Mệnh đề 05.9, bước hằng mất tính chất "mỗi mẫu cùng trọng số $1/n$" và giữ lại một phần giá trị khởi tạo, đổi lại phản ứng nhanh với mẫu mới; Nhận xét 05.19 chỉ ra cái giá khi môi trường dừng.

Hai lựa chọn của Mục 2.2 và Mục 2.3–2.4 độc lập với nhau, và nhận xét sau tách chúng.

::: remark Nhận xét 05.12 (Hai trục lựa chọn của Monte Carlo)
Một cấu hình Monte Carlo được xác định bởi hai lựa chọn độc lập:

- quy tắc lần ghé quyết định **mẫu nào được dùng** (Định nghĩa 05.6);
- quy tắc bước học quyết định **cách kết hợp các mẫu** (Mệnh đề 05.9 hoặc 05.11).

Hai trục tạo bốn cấu hình. Báo cáo một kết quả Monte Carlo cần nêu cả hai lựa chọn, cùng giá trị khởi tạo khi bước học hằng.
:::

![Lưới hai nhân hai: trục ngang "Quy tắc bước học" gồm trung bình mẫu và alpha hằng số; trục dọc "Quy tắc lần ghé" gồm lần ghé đầu tiên và mọi lần ghé; bốn ô là bốn cấu hình; dòng chú thích "Hai lựa chọn độc lập, không phải ba thuật toán rời nhau".](img/lec-05/design-grid.svg)

Trên hình, mỗi ô của lưới là một cấu hình, và đi theo một hàng chỉ đổi quy tắc bước học, đi theo một cột chỉ đổi quy tắc lần ghé. Bài tập tuần 5 (2025–2026, bài 5) liệt kê "lần ghé đầu tiên", "trung bình mẫu" và "bước hằng" như ba phương pháp ngang hàng; lưới cho thấy chúng thuộc hai trục khác nhau. Ví dụ 05.5 đã chạy cả bốn ô trên hai lượt với $\gamma=1$. Bài tập 05.18 của [tệp bài tập](material-viewer.html?doc=materials/lec-05/exercises.md&deck=lecture-05-du-doan-phi-mo-hinh.html) chạy lại bốn ô tại $\mathrm S$ với $\gamma=0{,}9$, khi các lợi tức của cùng một lượt không còn bằng nhau.

<!-- note-topic-id: lec-05-topic-03 -->
### 2.5 Thuật toán dự đoán Monte Carlo

Các Mục 2.1–2.4 cho từng thành phần: tính lợi tức ngược (Mệnh đề 05.4), chọn mẫu theo lần ghé (Định nghĩa 05.6), cập nhật gia tăng (Mệnh đề 05.9, 05.11). Chúng ta cần ghép chúng thành một quy trình chạy trên một luồng lượt, với thứ tự thao tác đúng. Ví dụ sau thực hiện bằng tay một lượt của quy trình, từ bảng đã có sau $e_1$.

::: example Ví dụ 05.6 (Một lượt của Monte Carlo lần ghé đầu tiên)
**Dữ kiện.** Cấu hình lần ghé đầu tiên với bước $1/N(s)$; $\gamma=1$. Sau khi xử lý $e_1$ (Ví dụ 05.5): $V(\mathrm S)=V(\mathrm X)=1$, $N(\mathrm S)=N(\mathrm X)=1$. Lượt mới là $e_2$: $S_0=\mathrm S$, $S_1=\mathrm X$, $S_2=\mathrm S$, $S_3=\mathrm L$, phần thưởng $(R_1,R_2,R_3)=(0,0,-1)$, $T=3$.

**Pha 1, tính lợi tức ngược.** $G_3=0$; $G_2=-1+1\cdot0=-1$; $G_1=0+1\cdot(-1)=-1$; $G_0=0+1\cdot(-1)=-1$.

**Pha 2, duyệt xuôi và cập nhật.** Tập đã ghé $\mathcal H$ bắt đầu rỗng.

| $t$ | $S_t$ | $S_t\in\mathcal H$ | Thao tác | $N(S_t)$ | Mục tiêu $G_t$ | Giá trị mới |
|---|---|---|---|---|---|---|
| $0$ | $\mathrm S$ | không | cập nhật, thêm $\mathrm S$ vào $\mathcal H$ | $2$ | $-1$ | $1+\tfrac12(-1-1)=0$ |
| $1$ | $\mathrm X$ | không | cập nhật, thêm $\mathrm X$ vào $\mathcal H$ | $2$ | $-1$ | $1+\tfrac12(-1-1)=0$ |
| $2$ | $\mathrm S$ | có | bỏ qua | $2$ | không dùng | $0$ |

**Kết quả.** $(V(\mathrm S),V(\mathrm X))=(0,0)$, $N(\mathrm S)=N(\mathrm X)=2$.

**Kiểm tra lại.** Hàng đầu của Ví dụ 05.5 ghi $(0,0)$ sau $e_2$ cho cùng cấu hình.
:::

Ví dụ 05.6 tách hai pha. Pha 1 duyệt lùi để tính mọi $G_t$ trong $T$ phép tính. Pha 2 duyệt xuôi để nhận ra lần ghé đầu tiên theo thời gian. Nếu ta vừa duyệt lùi vừa loại trạng thái đã gặp, mẫu được giữ tại $\mathrm S$ sẽ là $G_2$, lần ghé cuối cùng theo thời gian; trong $e_2$ hai giá trị trùng nhau, nhưng trong một lượt có chiết khấu thì không.

::: algorithm Thuật toán 05.13 (Dự đoán Monte Carlo)
**Đầu vào.** Chính sách $\pi$ cần đánh giá; hệ số chiết khấu $\gamma\in[0,1]$; ngân sách $M$ lượt; quy tắc lần ghé (đầu tiên hoặc mọi lần); lịch bước học $\alpha_n(s)$, bằng $1/n$ cho trung bình mẫu hoặc một hằng số $\alpha$.

**Đầu ra.** Bảng $V$ ước lượng $v_\pi$ trên $\mathcal S$.

**Giả thiết.** Các giả thiết của Định nghĩa 05.1; mỗi lượt sinh theo $\pi$ kết thúc tại một trạng thái kết thúc thật.

**Khởi tạo.** $V(s)$ tùy ý và $N(s)=0$ với mọi $s\in\mathcal S$; $V(s)=0$ tại mọi trạng thái kết thúc.

**Tham số.** $\gamma$, $M$, quy tắc lần ghé, lịch bước học.

1. Lặp với $m=1,\ldots,M$:
2. Sinh một lượt $S_0,A_0,R_1,S_1,\ldots,S_T$ theo $\pi$ cho tới khi $S_T$ là trạng thái kết thúc.
3. Đặt $G_T=0$; với $t=T-1,T-2,\ldots,0$, tính $G_t=R_{t+1}+\gamma G_{t+1}$.
4. Đặt tập đã ghé $\mathcal H=\varnothing$. Với $t=0,1,\ldots,T-1$, đặt $s=S_t$:
5. Nếu quy tắc là mọi lần ghé, hoặc quy tắc là lần ghé đầu tiên và $s\notin\mathcal H$: tăng $N(s)\leftarrow N(s)+1$, đặt $n=N(s)$, cập nhật $V(s)\leftarrow V(s)+\alpha_n(s)\bigl[G_t-V(s)\bigr]$, rồi đặt $\mathcal H\leftarrow\mathcal H\cup\{s\}$.
6. Kết thúc vòng lặp của bước 1 và trả về $V$.

**Điều kiện dừng.** Dừng sau đúng $M$ lượt. Kết thúc một lượt ở bước 2 chỉ chuyển sang lượt kế tiếp; nó không dừng thuật toán.

**Chi phí mỗi bước.** Một lượt dài $T$ cần $O(T)$ phép tính cho hai pha và $O(T)$ bộ nhớ tạm để giữ lượt, với truy cập bảng và tập $\mathcal H$ trong thời gian hằng; bảng $V$ và bộ đếm $N$ cần $O(\lvert\mathcal S\rvert)$ bộ nhớ.
:::

Thuật toán 05.13 chạy trên $e_1$ rồi $e_2$ với bước $1/N(s)$ cho đúng hàng đầu của Ví dụ 05.5: sau $e_1$ là $(1,1)$, và lượt $e_2$ là Ví dụ 05.6. Bước 5 dùng bộ đếm của riêng trạng thái, phù hợp điều kiện áp dụng của Mệnh đề 05.9.

::: remark Nhận xét 05.14 (Trạng thái kết thúc và lượt bị dừng giữa chừng)
Trạng thái kết thúc không bao giờ được cập nhật; giá trị của nó luôn bằng $0$. Một lượt bị dừng vì giới hạn thời gian chưa tới trạng thái kết thúc, nên bước 3 không áp dụng được cho nó và thuật toán không dùng lượt đó.
:::

**Trong thực hành.** Hàm `mc_prediction` của notebook Lunar Lander cài Thuật toán 05.13 trên bảng $9216$ ô và bỏ $42$ lượt bị cắt ngắn của tập huấn luyện. Với mọi lần ghé và bước $1/N(s)$, bảng thu được trùng trung bình cộng các lợi tức theo ô tới sai số làm tròn, đúng như Mệnh đề 05.9 dự đoán. Tình huống 05.2 xét điều gì xảy ra nếu ta coi bước $1000$ là trạng thái kết thúc thay vì bỏ các lượt này.

::: exercise Bài tập 05.4
Dữ kiện: lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ của tàu đổ bộ thu nhỏ.

(a) Mỗi trạng thái $\mathrm S$, $\mathrm X$ cung cấp bao nhiêu mẫu theo lần ghé đầu tiên và theo mọi lần ghé.
(b) Giải thích vì sao bước 4 của Thuật toán 05.13 duyệt xuôi chứ không duyệt lùi.
:::

::: hint
Lần ghé đầu tiên được xác định riêng trong từng lượt. Ở câu (b), xét thứ tự các thời điểm ghé $\mathrm S$ trong $e_1$.
:::

::: solution
(a) Mỗi trạng thái cho một mẫu theo lần ghé đầu tiên và hai mẫu theo mọi lần ghé.

(b) Lần ghé đầu tiên của $\mathrm S$ là $t=0$. Duyệt lùi gặp $t=2$ trước; nếu đánh dấu $\mathrm S$ ở đó và bỏ qua $t=0$, mẫu được giữ là $G_2$, tức lần ghé cuối cùng. Với $\gamma<1$, $G_2=\gamma$ khác $G_0=\gamma^3$ (Ví dụ 05.2).

**Kiểm tra lại.** Với $\gamma=0{,}9$: $G_0=0{,}729$, $G_2=0{,}9$; hai quy tắc cho hai mẫu khác nhau.
:::

<!-- note-topic-id: lec-05-topic-19 -->
### 2.6 Tính không chệch và hội tụ của Monte Carlo

Sau hai lượt, lần ghé đầu tiên với trung bình mẫu cho $V(\mathrm S)=0$, trong khi $v_\pi(\mathrm S)=11/21$. Chúng ta cần biết sai số này giảm thế nào khi số lượt tăng và dưới giả thiết nào. Một cách trực quan, mỗi lượt cho một mẫu độc lập của cùng một biến ngẫu nhiên, nên trung bình tiến tới kỳ vọng theo luật số lớn; nhận xét này chưa phải định lý.

::: example Ví dụ 05.7 (Sai số của trung bình lần ghé đầu tiên tại $\mathrm S$)
**Dữ kiện.** Tàu đổ bộ thu nhỏ của Ví dụ 05.1, $\gamma=1$, mỗi lượt bắt đầu ở $\mathrm S$. Giá trị chuẩn $v_\pi(\mathrm S)=11/21$ được giải từ mô hình bằng phương trình Bellman kỳ vọng (Ví dụ 05.14, Mục 4.1). Mô hình chỉ dùng để đo sai số (Mục 2.6, Bài tập 05.6 và Mục 4); Monte Carlo không đọc nó.

**Phân phối của mẫu.** Lần ghé đầu tiên của $\mathrm S$ là $t=0$. Với $\gamma=1$ và chỉ có phần thưởng cuối, $G_0=1$ khi tàu nằm yên và $G_0=-1$ khi tàu rơi. Gọi $h$ là xác suất nằm yên; khi đó $\mathbb E[G_0]=h-(1-h)=2h-1$. Đặt bằng $11/21$ cho $h=16/21$.

**Phương sai của một mẫu.** Vì $G_0^2=1$,

$$
\operatorname{Var}(G_0)=\mathbb E[G_0^2]-\bigl(\mathbb E[G_0]\bigr)^2=1-\Bigl(\frac{11}{21}\Bigr)^2=\frac{320}{441}\approx0{,}726 .
$$

**Sai số của trung bình.** Trung bình $V_n(\mathrm S)$ của $n$ mẫu độc lập có kỳ vọng $11/21$ và độ lệch chuẩn $\sqrt{320/441}/\sqrt n\approx0{,}852/\sqrt n$. Với $n=2$, độ lệch chuẩn khoảng $0{,}602$; với $n=100$, khoảng $0{,}085$.

**Kiểm tra lại.** Sau hai lượt, $V_2(\mathrm S)-v_\pi(\mathrm S)=0-11/21\approx-0{,}524$; trị tuyệt đối $0{,}524$ nhỏ hơn một độ lệch chuẩn $0{,}602$.
:::

Ví dụ 05.7 dùng hai tính chất mà định nghĩa sau đặt tên.

::: definition Định nghĩa 05.15 (Ước lượng không chệch, ước lượng hội tụ hầu chắc chắn)
Cho $\hat v$ là một ước lượng ngẫu nhiên của số thực $v$, tính từ dữ liệu.

$\hat v$ là **không chệch** khi $\mathbb E[\hat v]=v$.

Một dãy ước lượng $\hat v_1,\hat v_2,\ldots$ **hội tụ hầu chắc chắn** về $v$ khi $\Pr\bigl(\lim_{m\to\infty}\hat v_m=v\bigr)=1$.
:::

Không chệch là tính chất ở một cỡ mẫu cố định: trung bình của ước lượng qua mọi tập dữ liệu có thể bằng $v$. Hội tụ hầu chắc chắn là tính chất khi lượng dữ liệu tăng mãi: trên gần như mọi luồng dữ liệu, ước lượng tiến tới $v$. Hai tính chất độc lập nhau. Ước lượng bằng mẫu đầu tiên $\hat v_m=g_1$ không chệch nhưng không hội tụ, còn Nhận xét 05.18 sau Định lý 05.17 cho một ước lượng hội tụ mà chệch ở cỡ mẫu hữu hạn.

Định lý đầu tiên cần Mệnh đề 05.7 với $k=1$ và luật mạnh số lớn.

::: theorem Định lý 05.16 (Hội tụ của Monte Carlo lần ghé đầu tiên)
**Giả thiết.**

- Các giả thiết của Định nghĩa 05.1 và Bổ đề 05.5: $\mathcal S$ hữu hạn, $\pi$ cố định, môi trường Markov dừng, lượt kết thúc hầu chắc chắn từ mọi trạng thái.
- Phần thưởng bị chặn: $\lvert R_{t+1}\rvert\le R_{\max}$; $\gamma\in[0,1]$.
- Các lượt độc lập, cùng phân phối trạng thái đầu; $p_s=\Pr(N_e(s)\ge1)>0$.
- Quy tắc lần ghé đầu tiên với bước $1/N(s)$ (Thuật toán 05.13).

**Kết luận.**

- (a) Với mọi $n\ge1$, khi đã có $n$ mẫu tại $s$, $V_n(s)$ không chệch và có phương sai $\sigma^2(s)/n$, với $\sigma^2(s)=\operatorname{Var}(G_{t_1}\mid N_e(s)\ge1)<\infty$.
- (b) Khi số lượt $M\to\infty$, ước lượng tại $s$ hội tụ hầu chắc chắn về $v_\pi(s)$.

**Điều kiện áp dụng.** Mọi trạng thái được ghé với xác suất dương trong một lượt; dữ liệu theo chính sách.

**Phạm vi.** Định lý không áp dụng cho bước học hằng (Nhận xét 05.19) và không cho tốc độ ngoài phương sai $\sigma^2(s)/n$ ở (a).
:::

::: proof Chứng minh Định lý 05.16
**Bước 1 (mẫu độc lập cùng phân phối).** Mẫu lần ghé đầu tiên của một lượt là một hàm của riêng lượt đó. Vì các lượt độc lập cùng phân phối, các mẫu lấy từ những lượt có ghé $s$ là độc lập, cùng phân phối với $G_{t_1}$ khi biết $N_e(s)\ge1$.

**Bước 2 (kỳ vọng và phương sai).** Theo Mệnh đề 05.7 với $k=1$, mỗi mẫu có kỳ vọng $v_\pi(s)$. Theo Bổ đề 05.5, $\mathbb E[G_{t_1}^2]\le R_{\max}^2\mathbb E[T^2]<\infty$, nên $\sigma^2(s)<\infty$. Trung bình của $n$ mẫu độc lập có kỳ vọng $v_\pi(s)$ và phương sai $\sigma^2(s)/n$, cho kết luận (a).

**Bước 3 (số mẫu tăng vô hạn).** Gọi $n_M$ là số lượt có ghé $s$ trong $M$ lượt đầu. Các chỉ báo $\mathbf 1\{N_e(s)\ge1\}$ độc lập cùng phân phối với kỳ vọng $p_s$, nên theo luật mạnh số lớn $n_M/M\to p_s>0$ hầu chắc chắn; do đó $n_M\to\infty$ hầu chắc chắn.

**Bước 4 (hội tụ).** Theo luật mạnh số lớn áp dụng cho dãy mẫu của Bước 1, $\frac1n\sum_{i=1}^n g_i(s)\to v_\pi(s)$ hầu chắc chắn khi $n\to\infty$. Thay $n=n_M\to\infty$ của Bước 3 cho kết luận (b). $\square$
:::

Định lý 05.16 trả lời câu hỏi đầu mục cho quy tắc lần ghé đầu tiên: sai số giảm như $1/\sqrt n$ về độ lệch chuẩn, và tiến tới $0$ hầu chắc chắn. Trên tàu đổ bộ thu nhỏ, Ví dụ 05.7 cho hằng số cụ thể $0{,}852$.

Ba giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "kết thúc hầu chắc chắn": nếu một trạng thái có thể tự chuyển mãi, lợi tức của lượt chứa nó không xác định, và Bước 2 mất chặn mômen.
- Bỏ "$p_s>0$": một trạng thái không bao giờ được ghé giữ giá trị khởi tạo, và Bước 3 không có mẫu nào.
- Bỏ "bước $1/N(s)$": với bước hằng, trung bình có trọng số không hội tụ (Nhận xét 05.19).

Bước 1 dùng tính độc lập giữa các lượt, Bước 2 dùng giả thiết Markov qua Mệnh đề 05.7 và giả thiết kết thúc qua Bổ đề 05.5, còn Bước 3 dùng $p_s>0$.

Với quy tắc mọi lần ghé, Bước 1 không còn đúng: các mẫu trong cùng lượt phụ thuộc nhau, và số mẫu của mỗi lượt là ngẫu nhiên. Định lý sau giữ kết luận hội tụ bằng cách áp dụng luật số lớn theo lượt thay vì theo mẫu.

::: theorem Định lý 05.17 (Hội tụ của Monte Carlo mọi lần ghé)
**Giả thiết.** Như Định lý 05.16, trong đó điều kiện $p_s>0$ được viết thành $\mathbb E[N_e(s)]>0$; quy tắc mọi lần ghé với bước $1/N(s)$.

**Kết luận.** Gọi $V^{(M)}(s)$ là ước lượng tại $s$ sau $M$ lượt. Khi $M\to\infty$, $V^{(M)}(s)\to v_\pi(s)$ hầu chắc chắn.

**Điều kiện áp dụng.** Không cần các mẫu trong cùng lượt độc lập.

**Phạm vi.** Định lý không khẳng định $V^{(M)}(s)$ không chệch ở $M$ hữu hạn; Nhận xét 05.18 cho một trường hợp chệch.
:::

::: proof Chứng minh Định lý 05.17
**Bước 1 (ước lượng là một tỉ số).** Theo Mệnh đề 05.9, bước $1/N(s)$ cho đúng trung bình số học của mọi mẫu. Với lượt thứ $e$, đặt $Z_e=\sum_{k=1}^{N_e(s)}G^{(e)}_{t_k}$ là tổng các mẫu của lượt đó. Khi đó

$$
V^{(M)}(s)=\frac{\sum_{e=1}^MZ_e}{\sum_{e=1}^MN_e(s)}=\frac{\frac1M\sum_{e=1}^MZ_e}{\frac1M\sum_{e=1}^MN_e(s)} .
$$

**Bước 2 (khả tích).** Ta có $N_e(s)\le T_e$ và $\sum_{k\ge1}\lvert G_{t_k}\rvert\mathbf 1\{N_e(s)\ge k\}\le N_e(s)\max_t\lvert G_t\rvert\le R_{\max}T_e^2$; vế trái chặn cả $\lvert Z_e\rvert$. Theo Bổ đề 05.5, $\mathbb E[T_e^2]<\infty$, nên $\mathbb E[N_e(s)]$, $\mathbb E\lvert Z_e\rvert$ và kỳ vọng của vế trái hữu hạn.

**Bước 3 (kỳ vọng của tổng trong một lượt).** Với một lượt,

$$
\begin{aligned}
\mathbb E[Z_e]&=\sum_{k\ge1}\mathbb E\bigl[G_{t_k}\mathbf 1\{N_e(s)\ge k\}\bigr] &&\text{(đổi thứ tự, hợp lệ nhờ Bước 2)}\\
&=\sum_{k\ge1}v_\pi(s)\Pr\bigl(N_e(s)\ge k\bigr) &&\text{(Mệnh đề 05.7, Bước 3 của chứng minh)}\\
&=v_\pi(s)\,\mathbb E[N_e(s)] &&\text{(}\textstyle\sum_{k\ge1}\Pr(N\ge k)=\mathbb E[N]\text{).}
\end{aligned}
$$

Số hạng ứng với $k$ có $\Pr(N_e(s)\ge k)=0$ bằng $0$ ở cả hai vế, nên Mệnh đề 05.7 chỉ cần áp dụng cho các $k$ còn lại.

**Bước 4 (luật số lớn theo lượt).** Các cặp $(Z_e,N_e(s))$ độc lập cùng phân phối theo $e$. Theo luật mạnh số lớn, tử số ở Bước 1 hội tụ hầu chắc chắn về $v_\pi(s)\mathbb E[N_e(s)]$ và mẫu số hội tụ hầu chắc chắn về $\mathbb E[N_e(s)]>0$. Thương của hai giới hạn là $v_\pi(s)$. $\square$
:::

So với Định lý 05.16, Định lý 05.17 bỏ được tính độc lập giữa các mẫu nhưng trả giá ở hai điểm: chứng minh phải đi qua tổng của cả lượt, và tính không chệch ở cỡ mẫu hữu hạn không còn. Hai định lý có cùng kết luận giới hạn và cùng cần bước $1/N(s)$; Sutton và Barto (2018, §5.1, trang 93) nêu hai kết luận này và dẫn Singh và Sutton (1996) cho quy tắc mọi lần ghé.

<!-- note-topic-id: lec-05-topic-21 -->
::: remark Nhận xét 05.18 (Mọi lần ghé chệch ở số lượt hữu hạn)
Một trạng thái $\mathrm C$, số liệu sư phạm tự xây dựng, cho thấy độ chệch này.

- Mô hình: với xác suất $1/2$ tàu ở lại $\mathrm C$ và nhận phần thưởng $1$, với xác suất $1/2$ lượt kết thúc với phần thưởng $0$; $\gamma=1$, nên $v_\pi(\mathrm C)=1$. Số lần ghé $N$ có $\Pr(N=m)=2^{-m}$, $\mathbb E[N]=2$, $\mathbb E[N^2]=6$, và lợi tức tại lần ghé thứ $k$ là $N-k$.
- Một lượt: mẫu lần ghé đầu tiên $N-1$ có kỳ vọng $1$; trung bình mọi lần ghé $\frac1N\sum_{k=1}^N(N-k)=(N-1)/2$ có kỳ vọng $1/2$.
- Giới hạn: tỉ số của Định lý 05.17 tiến tới $\dfrac{(\mathbb E[N^2]-\mathbb E[N])/2}{\mathbb E[N]}=\dfrac{(6-2)/2}{2}=1$. Độ chệch ở một lượt đến từ việc chia cho số mẫu ngẫu nhiên của lượt đó.
:::

::: remark Nhận xét 05.19 (Bước học hằng không hội tụ trên mẫu mới)
Giả sử các mẫu $g_1,g_2,\ldots$ tại $s$ độc lập cùng phân phối, với kỳ vọng $v=v_\pi(s)$ và phương sai $\sigma^2>0$, và dùng bước hằng $\alpha\in(0,1)$. Theo Mệnh đề 05.11:

- kỳ vọng $\mathbb E[V_n]=(1-\alpha)^nV_0+\bigl(1-(1-\alpha)^n\bigr)v$ tiến tới $v$, nên độ chệch do khởi tạo giảm theo cấp số nhân;
- phương sai $\operatorname{Var}(V_n)=\alpha^2\sigma^2\sum_{j=0}^{n-1}(1-\alpha)^{2j}$ tiến tới $\dfrac{\alpha^2\sigma^2}{1-(1-\alpha)^2}=\dfrac{\alpha\sigma^2}{2-\alpha}>0$.

Phương sai không tiến về $0$, nên $V_n$ dao động mãi quanh $v$, và không hội tụ hầu chắc chắn: nếu $V_n$ hội tụ thì $V_n-V_{n-1}=\alpha(g_n-V_{n-1})\to0$, kéo theo $g_n$ hội tụ, điều không thể với mẫu độc lập cùng phân phối có $\sigma^2>0$. Tại $\mathrm S$ của tàu đổ bộ thu nhỏ, $\sigma^2=320/441$ (Ví dụ 05.7); phương sai giới hạn là $\approx0{,}242$ với $\alpha=0{,}5$ và $\approx0{,}038$ với $\alpha=0{,}1$.
:::

**Trong thực hành.** Notebook Lunar Lander đo $J(V)$, trung bình của $(G_t-V(S_t))^2$ trên các mẫu của lượt kiểm tra kết thúc thật (Tình huống 05.1). Sau $2000$ lượt, trung bình qua năm thứ tự lượt, Monte Carlo mọi lần ghé cho $J=1627$ với bước $1/N(s)$ và $1802$ với bước hằng $\alpha=0{,}02$, phù hợp Nhận xét 05.19. Các lượt độc lập cùng phân phối, nhưng ô gộp không Markov.

::: exercise Bài tập 05.5
(a) Với tàu đổ bộ thu nhỏ của Ví dụ 05.7 ($v_\pi(\mathrm S)=11/21$, $\operatorname{Var}(G_0)=320/441$), tìm số lượt nhỏ nhất để độ lệch chuẩn của trung bình lần ghé đầu tiên tại $\mathrm S$ không vượt $0{,}05$.

(b) Với cùng phương sai mẫu, tính độ lệch chuẩn giới hạn của Monte Carlo lần ghé đầu tiên với bước hằng $\alpha=0{,}1$, và so với kết quả (a).
:::

::: hint
(a) Giải $\sqrt{(320/441)/n}\le0{,}05$. (b) Dùng Nhận xét 05.19.
:::

::: solution
(a) Điều kiện là $n\ge(320/441)/0{,}0025\approx290{,}2$, nên cần $n=291$ lượt.

(b) Phương sai giới hạn là $\alpha\sigma^2/(2-\alpha)=0{,}1\cdot0{,}7256/1{,}9\approx0{,}0382$, độ lệch chuẩn khoảng $0{,}195$. Trung bình mẫu đạt độ lệch chuẩn $0{,}05$ sau $291$ lượt và tiếp tục giảm; bước hằng $0{,}1$ dừng ở khoảng $0{,}195$ dù chạy bao lâu.

**Kiểm tra lại.** Ở (a), $\sqrt{0{,}7256/291}\approx0{,}0499\le0{,}05$, còn $\sqrt{0{,}7256/290}\approx0{,}05002>0{,}05$.
:::

Như vậy, từ lợi tức của một lượt (Định nghĩa 05.3, Mệnh đề 05.4) và hai quy tắc lần ghé có mẫu kỳ vọng $v_\pi(s)$ (Định nghĩa 05.6, Mệnh đề 05.7), chúng ta có ước lượng Monte Carlo dạng gia tăng (Định nghĩa 05.8, Mệnh đề 05.9), khung cập nhật chung (Định nghĩa 05.10), Thuật toán 05.13, và hai Định lý 05.16, 05.17 bảo đảm hội tụ khi bước học là $1/N(s)$.

Tuy nhiên, mọi kết quả trên cần lượt kết thúc trước khi cập nhật; Mục 3 bỏ yêu cầu đó bằng cách thay phần lợi tức chưa quan sát bằng giá trị ước lượng.

## 3. Sai phân thời gian TD(0)

Sau chuyển đầu $\mathrm S\to\mathrm X$ của $e_1$, chưa biết tàu sẽ nằm yên hay rơi, nên $G_0$ chưa có và Monte Carlo chưa cập nhật được; bảng $V$ thì đã chứa một dự đoán cho phần còn lại từ $\mathrm X$. Để cập nhật $V(\mathrm S)$ ngay, chúng ta cần một mục tiêu chỉ dùng phần thưởng vừa nhận và thông tin đã có, một thứ tự đọc và ghi bảng, và cách xử lý chuyển vào trạng thái kết thúc, tự chuyển, lượt bị cắt ngắn.

<!-- note-topic-id: lec-05-topic-07 -->
### 3.1 Mục tiêu một bước và sai số TD

![Chuyển S sang X với phần thưởng 0 được tô là đã quan sát; từ X, hai nhánh nét đứt dẫn tới G hoặc L được ghi là phần đuôi chưa quan sát.](img/lec-05/unfinished-episode.svg)

Trên hình, phần đã quan sát chỉ gồm một chuyển $\mathrm S\to\mathrm X$ và phần thưởng $0$ của nó; hai nhánh nét đứt là hai kết cục còn có thể xảy ra. Lợi tức $G_0$ phụ thuộc nhánh nào xảy ra, nên chưa tính được. Truy hồi của Mệnh đề 05.4 tách $G_0$ thành phần đã biết và phần chưa biết:

$$
G_t=\underbrace{R_{t+1}}_{\text{đã quan sát}}+\gamma\underbrace{G_{t+1}}_{\text{chưa quan sát}} .
$$

Về mặt ý tưởng, phần chưa quan sát $G_{t+1}$ có kỳ vọng $v_\pi(S_{t+1})$, và $V(S_{t+1})$ là ước lượng của kỳ vọng đó; thay $G_{t+1}$ bằng $V(S_{t+1})$ cho một mục tiêu có ngay sau một chuyển, dùng một ước lượng để cập nhật một ước lượng khác. Đây là trực giác, chưa phải định nghĩa.

![Hai hàng. Hàng Monte Carlo: từ S_t qua chuyển có phần thưởng R_{t+1} tới S_{t+1}, rồi phần đuôi được quan sát đầy đủ tới trạng thái kết thúc. Hàng TD(0): từ S_t qua chuyển có R_{t+1} tới S_{t+1}, dừng sau một chuyển và dùng giá trị ước lượng ở trạng thái sau.](img/lec-05/mc-td-targets.svg)

Hình so sánh hai mục tiêu theo lượng dữ liệu chúng cần. Hàng trên là mục tiêu Monte Carlo: chuỗi mũi tên kéo dài tới trạng thái kết thúc, ứng với $G_t$. Hàng dưới là mục tiêu một bước: chỉ một mũi tên, rồi giá trị ước lượng tại $S_{t+1}$, ứng với $R_{t+1}+\gamma V(S_{t+1})$.

::: example Ví dụ 05.8 (Một bước TD(0) sau chuyển $\mathrm S\to\mathrm X$)
**Dữ kiện.** Tàu đổ bộ thu nhỏ, $\gamma=1$, bước học $\alpha=0{,}5$. Bảng hiện tại $V(\mathrm S)=0$, $V(\mathrm X)=0{,}5$, $V(\mathrm L)=V(\mathrm G)=0$. Chuyển quan sát: $\mathrm S\to\mathrm X$ với phần thưởng $0$.

**Tính.**

$$
\begin{aligned}
\text{mục tiêu: }&0+1\cdot V(\mathrm X)=0+0{,}5=0{,}5,\\
\text{sai lệch: }&0{,}5-V(\mathrm S)=0{,}5-0=0{,}5,\\
\text{giá trị mới: }&V(\mathrm S)=0+0{,}5\cdot0{,}5=0{,}25 .
\end{aligned}
$$

**Diễn giải.** Mục tiêu gồm phần thưởng $0$ đã quan sát và dự đoán $0{,}5$ cho phần còn lại từ $\mathrm X$; bước học $0{,}5$ dịch $V(\mathrm S)$ một nửa khoảng cách tới mục tiêu. Chỉ phần tử $V(\mathrm S)$ thay đổi; $V(\mathrm X)=0{,}5$ giữ nguyên.

**Kiểm tra lại.** Bảng $(0;\ 0{,}5)$ là kết quả TD(0) sau lượt $e_1$ từ bảng $0$ (Ví dụ 05.9), và bước này là chuyển đầu tiên của $e_2$ trong Ví dụ 05.10.
:::

::: definition Định nghĩa 05.20 (Mục tiêu TD, sai số TD, cập nhật TD(0))
Cho bảng $V_t$ ngay trước chuyển $t\to t+1$, với $V_t(s)=0$ tại mọi trạng thái kết thúc, và mẫu chuyển $(S_t,A_t,R_{t+1},S_{t+1})$ với $S_t\in\mathcal S$.

**Mục tiêu TD** là

$$
Y_t=R_{t+1}+\gamma V_t(S_{t+1}).
$$

Một mục tiêu cập nhật chứa giá trị ước lượng của chính bảng đang học được gọi là **mục tiêu bootstrap** (bootstrap target); $Y_t$ là một mục tiêu bootstrap.

**Sai số TD** là

$$
\delta_t=Y_t-V_t(S_t).
$$

**Cập nhật TD(0)** là quy tắc của Định nghĩa 05.10 với mục tiêu $Y_t$: $V_{t+1}(S_t)=V_t(S_t)+\alpha_n(S_t)\,\delta_t$, với $n$ là số thứ tự cập nhật của riêng $S_t$; mọi phần tử khác giữ nguyên, $V_{t+1}(s)=V_t(s)$ với $s\ne S_t$.
:::

Hai phép đọc ở vế phải đều lấy từ cùng bảng $V_t$ trước khi ghi. Sai số $\delta_t$ là hiệu giữa dự đoán dựa trên thông tin ở thời điểm $t+1$ và dự đoán ở thời điểm $t$; tên gọi sai phân thời gian đến từ hiệu này. Ví dụ 05.8 là định nghĩa với $Y_t=0{,}5$, $\delta_t=0{,}5$.

So với mục tiêu Monte Carlo, mục tiêu TD thay phần đuôi ngẫu nhiên bằng một ước lượng; so với $T_\pi$ của Bài 04, nó thay kỳ vọng theo mọi trạng thái kế tiếp bằng một mẫu của biểu thức bên trong $(T_\pi V)(s)$. Sutton và Barto (2018, §6.1, trang 120) gọi đây là kết hợp lấy mẫu của Monte Carlo với bootstrap của quy hoạch động.

Nhầm lẫn thường gặp là coi $\delta_t$ là sai số thật $v_\pi(S_t)-V_t(S_t)$, đại lượng dương khi bảng đánh giá thấp trạng thái $S_t$. Một sai số TD là một mẫu; quan hệ của nó với sai số thật chỉ phát biểu được qua kỳ vọng (Mệnh đề 05.25, 05.27), và Bài tập 05.6 cho một mẫu trái dấu với sai số thật.

::: exercise Bài tập 05.6
Dữ kiện: tàu đổ bộ thu nhỏ, $\gamma=1$, bảng $V(\mathrm S)=0$, $V(\mathrm X)=0{,}5$, $V(\mathrm L)=V(\mathrm G)=0$; giá trị chuẩn $v_\pi(\mathrm S)=11/21$. Từ $\mathrm S$, chuyển sang $\mathrm X$ có xác suất $0{,}8$ với phần thưởng $0$, chuyển sang $\mathrm L$ có xác suất $0{,}2$ với phần thưởng $-1$.

(a) Tính sai số TD $\delta_t$ cho mỗi chuyển có thể từ $\mathrm S$.
(b) Giải thích vì sao dấu của một sai số TD không xác định dấu của sai số thật.
:::

::: hint
Tính $Y_t$ cho từng trạng thái kế tiếp. Sai số thật tại $\mathrm S$ là $v_\pi(\mathrm S)-V(\mathrm S)$.
:::

::: solution
(a) Sang $\mathrm X$: $Y_t=0+0{,}5=0{,}5$, $\delta_t=0{,}5$. Sang $\mathrm L$: $Y_t=-1+0=-1$, $\delta_t=-1$.

(b) Sai số thật là $11/21\approx0{,}524>0$. Một mẫu cho $\delta_t=0{,}5$ hoặc $\delta_t=-1$; với xác suất $0{,}2$, sai số TD âm dù sai số thật dương.

**Kiểm tra lại.** Ở chuyển sang $\mathrm L$, giá trị tiếp nối là $V(\mathrm L)=0$, nên $Y_t=-1$ và $\delta_t=-1-0$.
:::

<!-- note-topic-id: lec-05-topic-08 -->
### 3.2 Thuật toán TD(0) và các trường hợp biên

Định nghĩa 05.20 cho một bước. Chúng ta cần một quy trình chạy trên luồng chuyển: thứ tự đọc và ghi bảng khi nhiều bước nối tiếp, cách bắt đầu lượt mới, và điều kiện dừng. Ví dụ sau chạy bằng tay một lượt đầy đủ từ bảng $0$.

::: example Ví dụ 05.9 (TD(0) trên lượt thứ nhất)
**Dữ kiện.** Lượt $e_1$: $\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,1)$; $\gamma=1$; bước hằng $\alpha=0{,}5$; bảng ban đầu $V(\mathrm S)=V(\mathrm X)=0$; giá trị trạng thái kết thúc bằng $0$.

**Tính.** Mỗi dòng đọc bảng sau dòng trước, tính mục tiêu và sai số, rồi ghi một phần tử:

| Chuyển | Thưởng | Mục tiêu $Y_t$ | Sai số TD $\delta_t$ | $V(\mathrm S)$ sau bước | $V(\mathrm X)$ sau bước |
|---|---|---|---|---|---|
| $\mathrm S\to\mathrm X$ | $0$ | $0+0=0$ | $0-0=0$ | $0$ | $0$ |
| $\mathrm X\to\mathrm S$ | $0$ | $0+0=0$ | $0-0=0$ | $0$ | $0$ |
| $\mathrm S\to\mathrm X$ | $0$ | $0+0=0$ | $0-0=0$ | $0$ | $0$ |
| $\mathrm X\to\mathrm G$ | $1$ | $1+0=1$ | $1-0=1$ | $0$ | $0+0{,}5\cdot1=0{,}5$ |

**Diễn giải.** Ba chuyển đầu có phần thưởng $0$ và giá trị tiếp nối $0$, nên không thay đổi gì. Phần thưởng $+1$ chỉ chạm tới $\mathrm X$, trạng thái ngay trước $\mathrm G$; TD(0) không quay lại sửa $\mathrm S$ trong lượt này.

**Kiểm tra lại.** Ở chuyển cuối, giá trị tiếp nối của $\mathrm G$ là $0$, nên mục tiêu là phần thưởng $1$, tính đúng một lần.
:::

::: algorithm Thuật toán 05.21 (TD(0) dạng bảng)
**Đầu vào.** Chính sách $\pi$ cần đánh giá; hệ số chiết khấu $\gamma\in[0,1]$; lịch bước học $\alpha_n(s)$; ngân sách $B$ chuyển.

**Đầu ra.** Bảng $V$ ước lượng $v_\pi$ trên $\mathcal S$.

**Giả thiết.** Các giả thiết của Định nghĩa 05.1; lượt mới bắt đầu theo cơ chế khởi tạo của môi trường.

**Khởi tạo.** $V(s)$ tùy ý và $N(s)=0$ với mọi $s\in\mathcal S$; $V(s)=0$ tại mọi trạng thái kết thúc. Bắt đầu một lượt tại trạng thái $S\in\mathcal S$.

**Tham số.** $\gamma$, $B$, lịch bước học.

1. Lặp khi ngân sách $B>0$:
2. Chọn $A\sim\pi(\cdot\mid S)$, thực hiện, quan sát $R$ và $S'$.
3. Tăng $N(S)\leftarrow N(S)+1$ và đặt $n=N(S)$.
4. Đọc bảng hiện tại: $Y=R+\gamma V(S')$, $\delta=Y-V(S)$, với $V(S')=0$ nếu $S'$ là trạng thái kết thúc.
5. Ghi $V(S)\leftarrow V(S)+\alpha_n(S)\,\delta$; giảm $B\leftarrow B-1$.
6. Nếu $S'$ là trạng thái kết thúc, bắt đầu một lượt mới và gán $S$ bằng trạng thái đầu của lượt đó; ngược lại gán $S\leftarrow S'$.
7. Khi $B=0$, trả về $V$.

**Điều kiện dừng.** Dừng khi hết $B$ chuyển. Kết thúc một lượt ở bước 6 chỉ mở lượt mới. Nếu ngân sách hết giữa lượt, trạng thái hiện tại không được coi là trạng thái kết thúc.

**Chi phí mỗi bước.** $O(1)$ phép tính cho mỗi chuyển, với truy cập bảng trong thời gian hằng; $O(\lvert\mathcal S\rvert)$ bộ nhớ cho $V$ và $N$; không cần giữ lượt.
:::

Ví dụ 05.9 là bốn vòng lặp của Thuật toán 05.21 với $\alpha_n=0{,}5$. Bước 4 đọc xong cả hai giá trị trước khi bước 5 ghi, nên khi $S'=S$ cả hai phép đọc dùng giá trị cũ; bảng và bộ đếm được giữ qua các lượt.

::: example Ví dụ 05.10 (TD(0) trên lượt thứ hai)
**Dữ kiện.** Lượt $e_2$: $\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$ với phần thưởng $(0,0,-1)$; $\gamma=1$; $\alpha=0{,}5$; bảng đầu lượt $(V(\mathrm S),V(\mathrm X))=(0;\ 0{,}5)$ từ Ví dụ 05.9.

**Tính.**

| Chuyển | Thưởng | Mục tiêu $Y_t$ | Sai số TD $\delta_t$ | $V(\mathrm S)$ sau bước | $V(\mathrm X)$ sau bước |
|---|---|---|---|---|---|
| $\mathrm S\to\mathrm X$ | $0$ | $0+0{,}5=0{,}5$ | $0{,}5-0=0{,}5$ | $0{,}25$ | $0{,}5$ |
| $\mathrm X\to\mathrm S$ | $0$ | $0+0{,}25=0{,}25$ | $0{,}25-0{,}5=-0{,}25$ | $0{,}25$ | $0{,}375$ |
| $\mathrm S\to\mathrm L$ | $-1$ | $-1+0=-1$ | $-1-0{,}25=-1{,}25$ | $-0{,}375$ | $0{,}375$ |

**Diễn giải.** Chuyển thứ hai đọc $V(\mathrm S)=0{,}25$ vừa được ghi ở chuyển thứ nhất: bảng được sửa tại chỗ giữa các chuyển. Phần thưởng $-1$ ở chuyển cuối sửa trực tiếp $\mathrm S$, còn $\mathrm X$ giữ $0{,}375$.

**Kiểm tra lại.** Chuyển cuối: $V(\mathrm S)=0{,}25+0{,}5\cdot(-1{,}25)=0{,}25-0{,}625=-0{,}375$.
:::

Hai trường hợp biên của bước 4 cần được tách riêng: chuyển vào trạng thái kết thúc, nơi giá trị tiếp nối bằng $0$, và tự chuyển $S'=S$, nơi hai phép đọc cùng một phần tử. Tàu đổ bộ thu nhỏ không có tự chuyển, nên ví dụ sau dùng hai chuyển thật của bài thực hành Lunar Lander.

::: example Ví dụ 05.11 (Tự chuyển và chuyển vào trạng thái kết thúc trên Lunar Lander)
**Dữ kiện.** Notebook thực hành Bài 05, mục 7.1, một lần chạy đã nhúng: bảng hiện tại là bảng Monte Carlo của mục 6 trên $9216$ ô; $\gamma=0{,}99$; bước hằng $\alpha=0{,}1$. Notebook in $R$ với ba chữ số thập phân, còn $V$, $Y$, $\delta$ với hai; các phép tính dưới đây dùng giá trị đã làm tròn đó.

**Tự chuyển** ($t=0$, $S_{t+1}=S_t$). $R=0{,}960$, $V_t(S_t)=V_t(S_{t+1})=43{,}85$:

$$
\begin{aligned}
Y&=0{,}960+0{,}99\cdot43{,}85=44{,}3715,\\
\delta&=44{,}3715-43{,}85=0{,}5215,\\
V_{t+1}(S_t)&=43{,}85+0{,}1\cdot0{,}5215\approx43{,}90 .
\end{aligned}
$$

**Vào trạng thái kết thúc** ($t=254$, tàu nằm yên). $R=100$, $V_t(S_t)=63{,}52$, giá trị tiếp nối bằng $0$:

$$
\begin{aligned}
Y&=100+0{,}99\cdot0=100,\\
\delta&=100-63{,}52=36{,}48,\\
V_{t+1}(S_t)&=63{,}52+0{,}1\cdot36{,}48=67{,}168\approx67{,}17 .
\end{aligned}
$$

**Kiểm tra lại.** Notebook in $Y=44{,}37$, $\delta=0{,}52$, giá trị mới $43{,}90$ cho tự chuyển và $Y=100$, $\delta=36{,}48$, giá trị mới $67{,}17$ cho chuyển cuối, khớp phép tính trên. Ở tự chuyển, cả hai phép đọc dùng giá trị cũ $43{,}85$.
:::

::: remark Nhận xét 05.22 (Trạng thái kết thúc, tự chuyển và lượt bị cắt ngắn)
- Phần thưởng của chuyển vào trạng thái kết thúc được tính một lần trong $R$; giá trị tiếp nối của trạng thái kết thúc bằng $0$, không bằng phần thưởng đó.
- Ở tự chuyển, quy tắc rút gọn thành $V(s)\leftarrow V(s)+\alpha\bigl[R-(1-\gamma)V(s)\bigr]$, vì $V(S')=V(s)$ được đọc trước khi ghi.
- Một lượt bị cắt ngắn vì giới hạn thời gian không kết thúc tại trạng thái kết thúc. Ở chuyển cuối trước điểm cắt, $S'$ là trạng thái không kết thúc, nên mục tiêu vẫn là $R+\gamma V(S')$; đặt $V(S')=0$ là coi điểm cắt như trạng thái kết thúc và làm lệch mục tiêu (Tình huống 05.2).
- Vì mỗi mục tiêu chỉ cần một chuyển, TD(0) dùng được mọi chuyển của lượt bị cắt ngắn, còn Thuật toán 05.13 phải bỏ cả lượt.
:::

<!-- note-topic-id: lec-05-topic-22 -->
Trong notebook Lunar Lander, mỗi bước mô phỏng dài $0{,}02$ giây; trong một bước, tàu dịch chuyển ít so với kích thước một ô gộp, nên $70\%$ số chuyển là tự chuyển. Chúng ta cần biết một chuỗi tự chuyển dài làm gì với $V(s)$, khi mỗi tự chuyển kéo $V(s)$ về phía $R+\gamma V(s)$ (Nhận xét 05.22).

::: example Ví dụ 05.12 (Ô chỉ có tự chuyển)
**Dữ kiện.** Một ô $s$ chỉ có tự chuyển, mỗi lần với cùng phần thưởng $r$; TD(0) với bước hằng $\alpha$; $\gamma<1$; giá trị đầu $V_0$.

**Điểm cố định.** Theo Nhận xét 05.22, $V_{k+1}=V_k+\alpha\bigl[r-(1-\gamma)V_k\bigr]$. Điểm cố định thỏa $r-(1-\gamma)V^*=0$, tức $V^*=r/(1-\gamma)$: giá trị của việc ở lại ô mãi mãi với phần thưởng $r$ mỗi bước.

**Khoảng cách tới điểm cố định.** Trừ hai vế cho $V^*$:

$$
V_{k+1}-V^*=\bigl(1-\alpha(1-\gamma)\bigr)(V_k-V^*),\qquad V_k-V^*=\bigl(1-\alpha(1-\gamma)\bigr)^k(V_0-V^*).
$$

**Số liệu của notebook.** Với $\alpha=0{,}5$, $\gamma=0{,}99$, hệ số là $1-0{,}005=0{,}995$, và $0{,}995^{100}\approx e^{-0{,}5}\approx0{,}61$: sau $100$ tự chuyển, khoảng cách còn khoảng $61\%$.

**Kiểm tra lại.** $100\ln0{,}995\approx-0{,}501$, và $e^{-0{,}501}\approx0{,}606$.
:::

Trong một chuỗi tự chuyển, mục tiêu không chứa thông tin của ô kế tiếp, và khi $\gamma$ gần $1$, mỗi tự chuyển chỉ dịch $V$ rất ít. Mục tiêu Monte Carlo $G_t$ thì đã chứa phần thưởng $\pm100$ ở cuối lượt, bất kể tàu ở lại một ô bao lâu.

::: remark Nhận xét 05.23 (Chi phí của hai quy trình)
Với truy cập bảng trong thời gian hằng, Monte Carlo có mục tiêu sau khi lượt kết thúc, giữ cả lượt, tốn $O(\lvert\mathcal S\rvert+T)$ bộ nhớ và $O(T)$ phép tính cho một lượt. TD(0) có mục tiêu sau mỗi chuyển, tốn $O(\lvert\mathcal S\rvert)$ bộ nhớ và $O(1)$ phép tính cho một chuyển. Chi phí một cập nhật khác số mẫu cần để đạt một sai số cho trước, nên các con số này không so sánh hiệu quả dùng dữ liệu.
:::

**Trong thực hành.** Notebook Lunar Lander cài Thuật toán 05.21 trên bảng $9216$ ô và dùng thêm $42\,000$ chuyển của các lượt bị cắt ngắn mà Monte Carlo bỏ; ở chuyển cuối của các lượt đó, mục tiêu vẫn giữ $V_t(S_{t+1})$, đúng Nhận xét 05.22.


::: exercise Bài tập 05.7
Dữ kiện: một ô $s$ của Lunar Lander chỉ có tự chuyển với cùng phần thưởng $r$; TD(0) với $\alpha=0{,}5$, $\gamma=0{,}99$; mỗi tự chuyển nhân khoảng cách tới $r/(1-\gamma)$ với $1-\alpha(1-\gamma)$ (Ví dụ 05.12). Tìm số tự chuyển nhỏ nhất để khoảng cách còn không quá $10\%$ khoảng cách ban đầu.
:::

::: hint
Hệ số là $1-0{,}5\cdot0{,}01=0{,}995$; giải $0{,}995^k\le0{,}1$.
:::

::: solution
Điều kiện là $k\ge\ln0{,}1/\ln0{,}995\approx(-2{,}3026)/(-0{,}0050125)\approx459{,}4$, nên cần $460$ tự chuyển.

**Kiểm tra lại.** $0{,}995^{460}=e^{460\ln0{,}995}\approx e^{-2{,}306}\approx0{,}0997\le0{,}1$, còn $0{,}995^{459}\approx0{,}1002$.
:::

Như vậy, chúng ta đã có mục tiêu và sai số TD (Định nghĩa 05.20), Thuật toán 05.21 với các trường hợp biên (Nhận xét 05.22) và chi phí $O(1)$ mỗi chuyển (Nhận xét 05.23).

Tuy nhiên, mục tiêu TD đọc một bảng đang sai; Mục 4 xét hệ quả của điều đó đối với kỳ vọng, phương sai và sự hội tụ.

## 4. Độ chệch, phương sai và hội tụ

Với $\alpha=0{,}5$, Monte Carlo lần ghé đầu tiên và TD(0) cho hai bảng khác nhau từ cùng hai lượt. Để biết bảng nào gần $v_\pi$ hơn và vì sao, chúng ta cần giá trị chuẩn và cần tách độ lệch $V-v_\pi$ của mỗi bảng thành các nguồn: kỳ vọng của mục tiêu lệch khỏi $v_\pi$ bao nhiêu, mục tiêu dao động quanh kỳ vọng bao nhiêu, và bước học có làm dao động tắt dần không. Mục 4.1 đặt hai bảng cạnh giá trị chuẩn, Mục 4.2–4.3 xét kỳ vọng và phương sai của mục tiêu, Mục 4.4 phát biểu điều kiện hội tụ.

<!-- note-topic-id: lec-05-topic-09 -->
### 4.1 Hai bảng trên cùng dữ liệu và giá trị chuẩn

Hai bảng của hai phương pháp được tính ở hai mục khác nhau; đặt chúng cạnh nhau cho thấy hai cơ chế lan truyền phần thưởng cuối lượt.

::: example Ví dụ 05.13 (Monte Carlo và TD(0) trên cùng dữ liệu)
**Dữ kiện.** Hai lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,1)$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$ với phần thưởng $(0,0,-1)$; $\gamma=1$; bước hằng $\alpha=0{,}5$; mỗi phương pháp khởi tạo riêng từ bảng $0$. Mỗi ô ghi $(V(\mathrm S),V(\mathrm X))$.

| Phương pháp | Sau $e_1$ | Sau $e_2$ |
|---|---|---|
| Monte Carlo lần ghé đầu tiên (Ví dụ 05.5) | $(0{,}5;\ 0{,}5)$ | $(-0{,}25;\ -0{,}25)$ |
| TD(0) (Ví dụ 05.9, 05.10) | $(0;\ 0{,}5)$ | $(-0{,}375;\ 0{,}375)$ |

**Sau $e_1$.** Monte Carlo cập nhật cả $\mathrm S$ và $\mathrm X$ bằng lợi tức $1$ khi lượt kết thúc. TD(0) chỉ đổi $V(\mathrm X)$, ở chuyển $\mathrm X\to\mathrm G$, vì ba mục tiêu trước đó bằng $0$.

**Kiểm tra lại.** Sau $e_2$, Monte Carlo cho $V(\mathrm S)=V(\mathrm X)$, vì hai trạng thái có cùng dãy mẫu $(1,-1)$; TD(0) cho hai giá trị khác nhau, vì mục tiêu tại mỗi trạng thái đọc giá trị của trạng thái kia.
:::

Monte Carlo đưa kết quả cuối lượt tới mọi lần ghé được chọn khi lượt kết thúc; TD(0) truyền kết quả ngược lại từng chuyển một (bài giảng gốc, trang 29). Hai cơ chế nói về đường đi của thông tin, không xếp hạng độ chính xác.

<!-- note-topic-id: lec-05-topic-05 -->
Trong ví dụ, mô hình của tàu đổ bộ thu nhỏ được biết riêng, nên ta tính được $v_\pi$ bằng phương trình Bellman kỳ vọng. Các giá trị này không phải đầu vào của Monte Carlo hay TD(0); chúng chỉ dùng để đo sai số.

::: example Ví dụ 05.14 (Giá trị chuẩn của tàu đổ bộ thu nhỏ)
**Dữ kiện.** Mô hình của Ví dụ 05.1: từ $\mathrm S$, sang $\mathrm X$ với xác suất $0{,}8$ và phần thưởng $0$, sang $\mathrm L$ với xác suất $0{,}2$ và phần thưởng $-1$; từ $\mathrm X$, sang $\mathrm G$ với xác suất $0{,}8$ và phần thưởng $+1$, sang $\mathrm S$ với xác suất $0{,}2$ và phần thưởng $0$; $\gamma=1$; $v_\pi(\mathrm L)=v_\pi(\mathrm G)=0$.

**Hệ Bellman kỳ vọng.**

$$
\begin{aligned}
v_\pi(\mathrm S)&=0{,}2\cdot(-1+0)+0{,}8\cdot\bigl(0+v_\pi(\mathrm X)\bigr)=-0{,}2+0{,}8\,v_\pi(\mathrm X),\\
v_\pi(\mathrm X)&=0{,}8\cdot(1+0)+0{,}2\cdot\bigl(0+v_\pi(\mathrm S)\bigr)=0{,}8+0{,}2\,v_\pi(\mathrm S).
\end{aligned}
$$

**Giải.** Thế phương trình thứ hai vào phương trình thứ nhất: $v_\pi(\mathrm S)=-0{,}2+0{,}64+0{,}16\,v_\pi(\mathrm S)$, tức $0{,}84\,v_\pi(\mathrm S)=0{,}44$. Do đó

$$
v_\pi(\mathrm S)=\frac{0{,}44}{0{,}84}=\frac{11}{21}\approx0{,}524,\qquad v_\pi(\mathrm X)=0{,}8+0{,}2\cdot\frac{11}{21}=\frac{19}{21}\approx0{,}905 .
$$

**Kiểm tra lại.** Phương trình thứ nhất: $-0{,}2+0{,}8\cdot19/21=(-4{,}2+15{,}2)/21=11/21$.
:::

Giá trị chuẩn lấy kỳ vọng theo mọi khả năng của môi trường, còn hai bảng chỉ phản ánh hai lượt đã quan sát. Ví dụ sau đo khoảng cách giữa chúng.

::: example Ví dụ 05.15 (Độ lệch của hai bảng so với giá trị chuẩn)
**Dữ kiện.** Hai bảng của Ví dụ 05.13 và giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$ của Ví dụ 05.14. Độ lệch là $V-v_\pi$, tức sai số thật $v_\pi-V$ của Mục 3.1 đổi dấu; độ lệch âm nghĩa là bảng đánh giá thấp giá trị chuẩn.

| Bảng | $V(\mathrm S)$, độ lệch | $V(\mathrm X)$, độ lệch |
|---|---|---|
| Monte Carlo sau $e_1$ | $0{,}5$; $-1/42\approx-0{,}024$ | $0{,}5$; $-17/42\approx-0{,}405$ |
| TD(0) sau $e_1$ | $0$; $-11/21\approx-0{,}524$ | $0{,}5$; $-17/42\approx-0{,}405$ |
| Monte Carlo sau $e_2$ | $-0{,}25$; $-65/84\approx-0{,}774$ | $-0{,}25$; $-97/84\approx-1{,}155$ |
| TD(0) sau $e_2$ | $-0{,}375$; $-151/168\approx-0{,}899$ | $0{,}375$; $-89/168\approx-0{,}530$ |

**Đọc bảng.** Sau $e_2$, Monte Carlo gần giá trị chuẩn hơn tại $\mathrm S$, còn TD(0) gần hơn tại $\mathrm X$.

**Kiểm tra lại.** $-0{,}375-11/21=(-7{,}875-11)/21=-18{,}875/21=-151/168$.
:::

Hai lượt không xếp hạng được hai phương pháp. Độ lệch của một bảng gộp nhiều nguồn: kỳ vọng của mục tiêu, dao động của mục tiêu, bước học, giá trị khởi tạo và hai lượt cụ thể. Mục 4.2 và 4.3 tách hai nguồn đầu, với bảng giữ cố định.

::: exercise Bài tập 05.8
Dữ kiện: tàu đổ bộ thu nhỏ, $\gamma=1$, $\alpha=0{,}5$, giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Sau hai lượt $e_1$, $e_2$, Monte Carlo lần ghé đầu tiên với bước hằng cho $(V(\mathrm S),V(\mathrm X))=(-0{,}25;\ -0{,}25)$, còn TD(0) cho $(-0{,}375;\ 0{,}375)$. Lượt thứ ba là $e_3:\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,1)$.

(a) Tiếp tục mỗi phương pháp trên $e_3$.
(b) Tính độ lệch của hai bảng so với giá trị chuẩn và so với Ví dụ 05.15.
:::

::: hint
Hai lợi tức của $e_3$ đều bằng $1$; ở TD(0), chuyển thứ hai đọc bảng sau chuyển thứ nhất.
:::

::: solution
(a) Monte Carlo: $V(\mathrm S)=-0{,}25+0{,}5\cdot(1+0{,}25)=0{,}375$ và $V(\mathrm X)=0{,}375$ theo cùng phép tính.

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

(b) Monte Carlo lệch $-25/168\approx-0{,}149$ tại $\mathrm S$ và $-89/168\approx-0{,}530$ tại $\mathrm X$; TD(0) lệch $-11/21\approx-0{,}524$ và $-73/336\approx-0{,}217$. So với sau $e_2$ (Ví dụ 05.15), cả hai bảng gần giá trị chuẩn hơn ở cả hai trạng thái; Monte Carlo vẫn gần hơn tại $\mathrm S$, TD(0) gần hơn tại $\mathrm X$.

**Kiểm tra lại.** $0{,}5\cdot0{,}75$ bù đúng $-0{,}375$, nên $V(\mathrm S)=0$.
:::


<!-- note-topic-id: lec-05-topic-10 -->
### 4.2 Độ chệch của mục tiêu TD

Mục tiêu Monte Carlo có kỳ vọng $v_\pi(s)$ (Mệnh đề 05.7); mục tiêu TD đọc bảng, nên kỳ vọng của nó phụ thuộc bảng, và chúng ta cần đo khoảng cách từ kỳ vọng đó tới $v_\pi(s)$. Một cách trực quan, nếu bảng đánh giá thấp trạng thái kế tiếp, mục tiêu TD đánh giá thấp trạng thái hiện tại theo, nhân với $\gamma$; mô tả này chưa phải định nghĩa.

::: example Ví dụ 05.16 (Kỳ vọng của mục tiêu TD tại $\mathrm S$)
**Dữ kiện.** Tàu đổ bộ thu nhỏ, $\gamma=1$. Bảng TD(0) sau $e_1$ (Ví dụ 05.9) được giữ cố định: $V(\mathrm X)=0{,}5$, $V(\mathrm L)=0$. Giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$ (Ví dụ 05.14).

**Phân phối của mục tiêu tại $\mathrm S$.** Với xác suất $0{,}2$, tàu vào $\mathrm L$ và $Y=-1+0=-1$; với xác suất $0{,}8$, tàu sang $\mathrm X$ và $Y=0+0{,}5=0{,}5$.

**Kỳ vọng.**

$$
\mathbb E_\pi[Y\mid S_t=\mathrm S]=0{,}2\cdot(-1)+0{,}8\cdot0{,}5=0{,}2 .
$$

**So với giá trị chuẩn.**

$$
0{,}2-\frac{11}{21}=\frac{4{,}2-11}{21}=-\frac{6{,}8}{21}=-\frac{34}{105}\approx-0{,}324 .
$$

**Kiểm tra lại.** Mục tiêu Monte Carlo tại $\mathrm S$ có kỳ vọng $11/21$ (Ví dụ 05.7), nên hiệu tương ứng bằng $0$.
:::

::: definition Định nghĩa 05.24 (Độ chệch của mục tiêu)
Cho $s\in\mathcal S$ và một mục tiêu cập nhật $Y$ được tạo từ một mẫu mới sinh theo $\pi$ khi $S_t=s$, với mọi bảng mà $Y$ đọc được giữ cố định. **Độ chệch** của mục tiêu tại $s$ là

$$
\operatorname{bias}(Y;s)=\mathbb E_\pi[Y\mid S_t=s]-v_\pi(s).
$$

Mục tiêu **không chệch** tại $s$ khi độ chệch bằng $0$.
:::

Định nghĩa nói về một mục tiêu với bảng cố định, kỳ vọng chỉ lấy theo phần thưởng và trạng thái kế tiếp của một mẫu mới; trong Ví dụ 05.16, $\operatorname{bias}(Y;\mathrm S)=-34/105$. Định nghĩa 05.15 thì nói về một ước lượng tính từ dữ liệu, nên một bảng không chệch vẫn có thể cho một mục tiêu TD chệch.

Nhầm lẫn thường gặp là trộn năm đại lượng có tên gần nhau của chương:

- sai lệch $Y-V(s)$ giữa mục tiêu và ước lượng cũ, theo Định nghĩa 05.10;
- sai số thật $v_\pi(s)-V(s)$, theo Mục 3.1, dương khi bảng đánh giá thấp;
- độ lệch $V(s)-v_\pi(s)$ của bảng, theo Ví dụ 05.15, là sai số thật đổi dấu;
- độ chệch $\operatorname{bias}(Y;s)=\mathbb E_\pi[Y\mid S_t=s]-v_\pi(s)$ của một mục tiêu, theo Định nghĩa 05.24;
- độ lệch chuẩn, căn bậc hai của phương sai, như $0{,}852/\sqrt n$ của Ví dụ 05.7.

Mệnh đề sau cho công thức độ chệch của mục tiêu TD với mọi bảng. Nó chỉ cần phương trình Bellman kỳ vọng của Bài 03.

::: proposition Mệnh đề 05.25 (Độ chệch của mục tiêu TD)
**Giả thiết.** Các giả thiết của Định nghĩa 05.1; bảng $V$ cố định với $V=0$ tại trạng thái kết thúc; $Y=R_{t+1}+\gamma V(S_{t+1})$ được tạo từ một mẫu mới theo $\pi$ với $S_t=s$.

**Kết luận.**

$$
\operatorname{bias}(Y;s)=\gamma\,\mathbb E_\pi\bigl[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s\bigr].
$$

**Điều kiện áp dụng.** Mọi bảng $V$ cố định trong lúc lấy kỳ vọng; dữ liệu theo chính sách.

**Phạm vi.** Mệnh đề không nói gì về độ chệch của bảng ước lượng sau nhiều cập nhật, vì khi đó bảng là ngẫu nhiên và thay đổi.
:::

::: proof Chứng minh Mệnh đề 05.25
Viết gọn $\mathbb E_s[\cdot]=\mathbb E_\pi[\cdot\mid S_t=s]$. Theo phương trình Bellman kỳ vọng, $v_\pi(s)=\mathbb E_s[R_{t+1}+\gamma v_\pi(S_{t+1})]$. Trừ đẳng thức này khỏi kỳ vọng của $Y$:

$$
\begin{aligned}
\mathbb E_s[Y]-v_\pi(s)&=\mathbb E_s\bigl[R_{t+1}+\gamma V(S_{t+1})\bigr]-\mathbb E_s\bigl[R_{t+1}+\gamma v_\pi(S_{t+1})\bigr]\\
&=\gamma\,\mathbb E_s\bigl[V(S_{t+1})-v_\pi(S_{t+1})\bigr].
\end{aligned}
$$

Dòng thứ nhất dùng phương trình Bellman kỳ vọng; dòng thứ hai dùng tính tuyến tính của kỳ vọng, vì hai số hạng $R_{t+1}$ triệt tiêu. Tại trạng thái kết thúc, cả $V$ và $v_\pi$ bằng $0$, nên số hạng tương ứng bằng $0$. $\square$
:::

Kiểm lại trên Ví dụ 05.16: $1\cdot\bigl[0{,}8\cdot(0{,}5-19/21)+0{,}2\cdot0\bigr]=-34/105$. Phần thưởng $R_{t+1}$ là mẫu thật nên không góp độ chệch.

::: corollary Hệ quả 05.26 (Khi nào mục tiêu không chệch)
**Giả thiết.** Như Mệnh đề 05.25.

**Kết luận.**

- (a) Mục tiêu Monte Carlo $G_t$ không chệch tại mọi $s$.
- (b) Nếu $V(s')=v_\pi(s')$ tại mọi trạng thái $s'$ có thể theo sau $s$, thì mục tiêu TD không chệch tại $s$.
- (c) Mục tiêu TD không chệch tại $s$ khi và chỉ khi $\mathbb E_\pi[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s]=0$ hoặc $\gamma=0$.

**Điều kiện áp dụng.** Bảng cố định; dữ liệu theo chính sách.

**Phạm vi.** Phần (c) cho phép độ lệch của bảng bù trừ nhau trong kỳ vọng; không chệch không có nghĩa bảng đúng.
:::

::: proof Chứng minh Hệ quả 05.26
Phần (a) là định nghĩa của $v_\pi$; phần (b) và (c) đọc trực tiếp từ công thức của Mệnh đề 05.25, vì độ chệch là tích của $\gamma$ với kỳ vọng của độ lệch $V-v_\pi$ tại trạng thái kế tiếp. $\square$
:::

Trường hợp (c) có thể xảy ra với bảng sai khi độ lệch tại các trạng thái kế tiếp bù trừ nhau trong kỳ vọng; trên tàu đổ bộ thu nhỏ, mỗi trạng thái chỉ có một trạng thái kế tiếp không kết thúc, nên mục tiêu tại $\mathrm S$ không chệch khi và chỉ khi $V(\mathrm X)=19/21$.

Mệnh đề 05.25 nối mục tiêu TD với toán tử $T_\pi$ của Bài 04. Vì $\mathbb E_\pi[Y\mid S_t=s]=(T_\pi V)(s)$, sai số TD có kỳ vọng là phần dư Bellman tại $s$.

::: proposition Mệnh đề 05.27 (Kỳ vọng của sai số TD)
**Giả thiết.** Như Mệnh đề 05.25, với $V=V_t$ là bảng trước cập nhật tại bước $t$.

**Kết luận.**

$$
\mathbb E_\pi[\delta_t\mid S_t=s,\ V_t]=(T_\pi V_t)(s)-V_t(s).
$$

**Điều kiện áp dụng.** Dữ liệu theo chính sách, trạng thái Markov; kỳ vọng lấy theo chuyển của bước $t$ khi $V_t$ đã biết.

**Phạm vi.** Mệnh đề nói về kỳ vọng của một bước; nó chưa đủ để kết luận hội tụ, vì còn dao động của $\delta_t$ quanh kỳ vọng (Mục 4.4).
:::

::: proof Chứng minh Mệnh đề 05.27
Khi $V_t$ đã biết và $S_t=s$, số hạng $V_t(S_t)=V_t(s)$ là hằng số, nên

$$
\begin{aligned}
\mathbb E_\pi[\delta_t\mid S_t=s,V_t]
&=\mathbb E_\pi[R_{t+1}+\gamma V_t(S_{t+1})\mid S_t=s,V_t]-V_t(s) &&\text{(Định nghĩa 05.20)}\\
&=(T_\pi V_t)(s)-V_t(s) &&\text{(định nghĩa } T_\pi\text{, Bài 04).}
\end{aligned}
$$

Đẳng thức thứ hai dùng tính Markov: phân phối của $(R_{t+1},S_{t+1})$ khi biết $S_t=s$ không phụ thuộc lịch sử, kể cả lịch sử đã tạo ra $V_t$. $\square$
:::

Như vậy, tính trung bình, TD(0) đi theo hướng của phép lặp $V\leftarrow T_\pi V$ của Bài 04, mỗi bước dùng một mẫu thay cho kỳ vọng; kỳ vọng của sai số TD bằng $0$ ở mọi trạng thái đúng khi $V=v_\pi$, đích của định lý hội tụ ở Mục 4.4.

Kết hợp với Mệnh đề 05.25, ta viết được kỳ vọng này theo sai số thật $v_\pi-V$ của Mục 3.1. Với bảng $V=V_t$ cố định, $\mathbb E_\pi[\delta_t\mid S_t=s]=\mathbb E_\pi[Y_t\mid S_t=s]-V(s)$ bằng $v_\pi(s)+\operatorname{bias}(Y_t;s)-V(s)$, nên

$$
\mathbb E_\pi[\delta_t\mid S_t=s]=\bigl(v_\pi-V\bigr)(s)-\gamma\,\mathbb E_\pi\bigl[(v_\pi-V)(S_{t+1})\mid S_t=s\bigr].
$$

Kỳ vọng của sai số TD bằng sai số thật tại $s$ trừ $\gamma$ nhân sai số thật trung bình tại trạng thái kế tiếp, nên kỳ vọng này khác sai số thật tại $s$ về độ lớn, và có thể cả về dấu. Trên dữ kiện của Bài tập 05.6, vế trái là $0{,}2\cdot(-1)+0{,}8\cdot0{,}5=0{,}2$ và vế phải là $11/21-0{,}8\cdot(19/21-0{,}5)=4{,}2/21=0{,}2$, trong khi sai số thật tại $\mathrm S$ là $11/21\approx0{,}524$.

**Trong thực hành.** Trong notebook Lunar Lander, bảng TD(0) bắt đầu bằng $\mathbf 0$. Ô gộp không Markov nên $v_\pi$ của ô không được định nghĩa; theo nghĩa gần đúng của Mệnh đề 05.25, với lợi tức kỳ vọng theo ô thay cho $v_\pi$, mục tiêu bị kéo xuống cho tới khi các ô kế tiếp nhận được thông tin. Sau $10$ lượt, trung bình qua năm thứ tự lượt, $J$ của TD(0) với $\alpha=0{,}5$ còn $5208$, gần giá trị $5797$ của bảng $\mathbf 0$.

::: exercise Bài tập 05.9
Dữ kiện: tàu đổ bộ thu nhỏ, $\gamma=1$; bảng cố định $V$ với $V(\mathrm L)=V(\mathrm G)=0$.

(a) Phân biệt $\delta_t$ của một chuyển với $(T_\pi V)(s)-V(s)$, và nêu quan hệ giữa chúng.
(b) Với $V(\mathrm S)=V(\mathrm X)=1$, tính độ chệch của mục tiêu TD tại $\mathrm S$ và tại $\mathrm X$ bằng Mệnh đề 05.25.
:::

::: hint
(a) Một đại lượng là ngẫu nhiên, đại lượng kia là kỳ vọng có điều kiện của nó. (b) Từ $\mathrm X$, trạng thái kế tiếp là $\mathrm G$ hoặc $\mathrm S$.
:::

::: solution
(a) $\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t)$ phụ thuộc chuyển được lấy mẫu, nên là biến ngẫu nhiên. $(T_\pi V)(s)-V(s)$ là một số, bằng kỳ vọng có điều kiện của $\delta_t$ khi $S_t=s$ (Mệnh đề 05.27). Một mẫu có thể nằm ở hai phía của kỳ vọng.

(b) Tại $\mathrm S$: $1\cdot\bigl[0{,}8\cdot(1-19/21)+0{,}2\cdot0\bigr]=0{,}8\cdot2/21=8/105\approx0{,}076$. Tại $\mathrm X$: $1\cdot\bigl[0{,}8\cdot0+0{,}2\cdot(1-11/21)\bigr]=0{,}2\cdot10/21=2/21\approx0{,}095$.

**Kiểm tra lại.** Tại $\mathrm S$, kỳ vọng trực tiếp của mục tiêu là $0{,}2\cdot(-1)+0{,}8\cdot1=0{,}6$, và $0{,}6-11/21=(12{,}6-11)/21=1{,}6/21=8/105$.
:::

<!-- note-topic-id: lec-05-topic-12 -->
### 4.3 Biến thiên của lợi tức và phương sai của mục tiêu

Sau kỳ vọng (Mục 4.2), chúng ta xét dao động của mục tiêu quanh kỳ vọng. Mục tiêu Monte Carlo phụ thuộc mọi chuyển ngẫu nhiên tới cuối lượt; bài giảng gốc (2025–2026, trang 30–31) cho thấy điều đó trên một dãy bảy ô, nơi đường tới bãi đáp dài hơn.

![Dãy bảy ô L, x1, S, x3, x4, x5, G; tàu bắt đầu tại S; từ mỗi ô không kết thúc, sang phải với xác suất 0,8 và sang trái với xác suất 0,2; vào L nhận âm 1, vào G nhận +1, chuyển khác nhận 0; L và G có giá trị 0.](img/lec-05/long-walk.svg)

Trên hình, $\mathrm S$ cách $\mathrm L$ hai ô về bên trái và cách $\mathrm G$ bốn ô về bên phải; các mũi tên mang cùng xác suất $0{,}8$ và $0{,}2$ như dãy bốn ô.

::: example Ví dụ 05.17 (Dãy bảy ô: giá trị chuẩn và hai lợi tức từ $\mathrm S$)
**Dữ kiện.** Trạng thái $\mathrm L,\mathrm x_1,\mathrm S,\mathrm x_3,\mathrm x_4,\mathrm x_5,\mathrm G$ theo thứ tự từ trái sang phải; $\mathrm L$, $\mathrm G$ kết thúc với giá trị $0$; chính sách luôn tiến; sang phải với xác suất $0{,}8$, sang trái với xác suất $0{,}2$; phần thưởng $-1$ khi vào $\mathrm L$, $+1$ khi vào $\mathrm G$, $0$ cho chuyển khác; $\gamma=0{,}99$.

**Giá trị chuẩn.** Đặt $u_1,u_2,u_3,u_4,u_5$ là giá trị của $\mathrm x_1,\mathrm S,\mathrm x_3,\mathrm x_4,\mathrm x_5$. Hệ Bellman kỳ vọng là

$$
\begin{aligned}
u_1&=0{,}2\cdot(-1)+0{,}99\cdot0{,}8\,u_2,\\
u_i&=0{,}99\,(0{,}2\,u_{i-1}+0{,}8\,u_{i+1}),\qquad i=2,3,4,\\
u_5&=0{,}8\cdot1+0{,}99\cdot0{,}2\,u_4 .
\end{aligned}
$$

Giải hệ tuyến tính năm ẩn cho $(u_1,\ldots,u_5)\approx(0{,}457;\ 0{,}829;\ 0{,}933;\ 0{,}970;\ 0{,}992)$, trong đó $v_\pi(\mathrm S)=u_2\approx0{,}829219$.

**Hai lợi tức từ $\mathrm S$.** Đường ngắn nhất tới $\mathrm G$ là $\mathrm S\to\mathrm x_3\to\mathrm x_4\to\mathrm x_5\to\mathrm G$ với phần thưởng $(0,0,0,1)$, nên $G_0=\gamma^3=0{,}970299$. Đường ngắn nhất tới $\mathrm L$ là $\mathrm S\to\mathrm x_1\to\mathrm L$ với phần thưởng $(0,-1)$, nên $G_0=-\gamma=-0{,}99$.

**Kiểm tra lại.** Phương trình của $u_5$: $0{,}8+0{,}198\cdot0{,}970\approx0{,}992$. Hiệu của hai lợi tức là $0{,}970299+0{,}99=1{,}960299$.
:::

![Hai đường từ S. Đường trên: S, x3, x4, x5, G tại t bằng 0 đến 4, phần thưởng 0, 0, 0, 1. Đường dưới: S, x1, L tại t bằng 0 đến 2, phần thưởng 0, âm 1.](img/lec-05/long-returns.svg)

Hình đặt hai đường trên cùng trục thời gian. Phần thưởng cuối của đường trên là $R_4$, nên mang hệ số $\gamma^3$; phần thưởng cuối của đường dưới là $R_2$, nên mang hệ số $\gamma$. Bài giảng gốc ghi hai số mũ $4$ và $2$; theo Định nghĩa 05.3, hai số mũ đúng là $3$ và $1$.

Hai lợi tức từ $\mathrm S$ cách nhau gần $2$, trong khi kỳ vọng là $0{,}829$; mục tiêu Monte Carlo không chệch (Hệ quả 05.26), nên khoảng cách này là dao động quanh kỳ vọng.

<!-- note-topic-id: lec-05-topic-13 -->
Chúng ta cần so sánh mức dao động của hai mục tiêu. Mục tiêu TD đọc một bảng đang sai, nên phương sai của nó không có thứ tự chung với $G_t$; vì vậy ta xét mục tiêu một bước lý tưởng $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$. Một cách trực quan, $Y^*$ thay phần đuôi $G_{t+1}$ bằng kỳ vọng của nó, giữ dao động của chuyển đầu và bỏ dao động của phần đuôi; mô tả này chưa phải định lý.

![Một cây: từ S_t, chuyển đầu với phần thưởng R_{t+1} tới S_{t+1}; từ S_{t+1} tỏa ra phần đuôi thứ nhất, phần đuôi thứ hai và các phần đuôi khác. Chú thích: chuyển đầu vẫn ngẫu nhiên; Monte Carlo dùng phần đuôi đã xảy ra.](img/lec-05/target-randomness.svg)

Hình tách hai nguồn ngẫu nhiên của $G_t$. Mũi tên đầu, từ $S_t$ tới $S_{t+1}$, là nguồn mà cả $G_t$ và $Y^*$ đều chịu. Các nhánh sau $S_{t+1}$ là nguồn mà chỉ $G_t$ chịu, vì $Y^*$ thay chúng bằng $v_\pi(S_{t+1})$.

::: example Ví dụ 05.18 (Phương sai của $G_t$ và $Y^*$ trên hai dãy)
**Dữ kiện.** Dãy bốn ô (Ví dụ 05.1, $\gamma=1$, $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$) và dãy bảy ô (Ví dụ 05.17, $\gamma=0{,}99$); điều kiện $S_t=\mathrm S$ trong cả hai dãy.

**Dãy bốn ô, $G_t$.** Theo Ví dụ 05.7, $G_t\in\{1,-1\}$ với $\Pr(G_t=1)=16/21$, nên $\operatorname{Var}(G_t)=1-(11/21)^2=320/441\approx0{,}726$.

**Dãy bốn ô, $Y^*$.** Với xác suất $0{,}2$, $Y^*=-1+0=-1$; với xác suất $0{,}8$, $Y^*=0+19/21$. Một biến hai giá trị $a$, $b$ với xác suất $p$, $1-p$ có phương sai $p(1-p)(a-b)^2$, nên

$$
\operatorname{Var}(Y^*)=0{,}2\cdot0{,}8\cdot\Bigl(\frac{19}{21}+1\Bigr)^2=0{,}16\cdot\frac{1600}{441}=\frac{256}{441}\approx0{,}580 .
$$

**Dãy bảy ô, $Y^*$.** Với xác suất $0{,}8$, $Y^*=0{,}99\,u_3\approx0{,}923$; với xác suất $0{,}2$, $Y^*=0{,}99\,u_1\approx0{,}452$. Do đó $\operatorname{Var}(Y^*)\approx0{,}16\cdot(0{,}471)^2\approx0{,}036$.

**Dãy bảy ô, $G_t$.** Đặt $m(s)=\mathbb E_\pi[G_t^2\mid S_t=s]$. Vì phần thưởng khác $0$ chỉ xuất hiện ở chuyển vào trạng thái kết thúc, nơi $G_{t+1}=0$, ta có $G_t^2=R_{t+1}^2+\gamma^2G_{t+1}^2$, nên $m$ thỏa hệ tuyến tính $m(s)=\mathbb E_\pi[R_{t+1}^2+\gamma^2m(S_{t+1})\mid S_t=s]$ với $m=0$ tại trạng thái kết thúc. Giải hệ năm ẩn cho $m(\mathrm S)\approx0{,}9051$, nên $\operatorname{Var}(G_t)=m(\mathrm S)-v_\pi(\mathrm S)^2\approx0{,}9051-0{,}6876\approx0{,}217$.

**Tổng hợp.**

| Tại $S_t=\mathrm S$ | Dãy bốn ô, $\gamma=1$ | Dãy bảy ô, $\gamma=0{,}99$ |
|---|---|---|
| $\operatorname{Var}(G_t)$ | $320/441\approx0{,}726$ | $\approx0{,}217$ |
| $\operatorname{Var}(Y^*)$ | $256/441\approx0{,}580$ | $\approx0{,}036$ |
| Hiệu, phần do đuôi sau chuyển đầu | $64/441\approx0{,}145$ ($20\%$) | $\approx0{,}182$ ($84\%$) |

**Kiểm tra lại.** Kỳ vọng của $Y^*$ ở dãy bốn ô là $0{,}2\cdot(-1)+0{,}8\cdot19/21=11/21=v_\pi(\mathrm S)$, và ở dãy bảy ô là $0{,}8\cdot0{,}923+0{,}2\cdot0{,}452\approx0{,}829=u_2$.
:::

![Hai thanh ngang trên cùng thang từ 0 đến 0,8. Dãy bốn ô với gamma bằng 1: phương sai của lợi tức 0,726 gồm 0,580 là phương sai của mục tiêu lý tưởng Y sao (tô đặc) và 0,145 là phần do đuôi (gạch chéo), 20 phần trăm. Dãy bảy ô với gamma bằng 0,99: phương sai của lợi tức 0,217 gồm 0,036 của Y sao và 0,182 do đuôi, 84 phần trăm.](img/lec-05/variance-decomposition.svg)

Hình vẽ lại bảng tổng hợp trên cùng một thang: phần tô đặc là $\operatorname{Var}(Y^*)$, cả thanh là $\operatorname{Var}(G_t)$, phần gạch chéo là hiệu. Thanh của dãy bảy ô ngắn hơn vì từ $\mathrm S$ tàu ít khi rơi, nhưng phần gạch chéo chiếm $84\%$; ở cặp ví dụ này, lượt dài hơn làm tăng tỉ lệ phương sai đến từ phần đuôi, còn $\operatorname{Var}(G_t)$ thì nhỏ hơn.

Định lý sau chứng minh bất đẳng thức của bảng cho mọi trạng thái. Nó cần tính Markov của lợi tức (Bài 03) và luật phương sai toàn phần.

::: theorem Định lý 05.28 (Phương sai của mục tiêu một bước lý tưởng)
**Giả thiết.** Các giả thiết của Định nghĩa 05.1; $G_t$ có mômen bậc hai hữu hạn khi $S_t=s$, chẳng hạn khi phần thưởng bị chặn và Bổ đề 05.5 áp dụng; $Y^*=R_{t+1}+\gamma v_\pi(S_{t+1})$.

**Kết luận.**

$$
\mathbb E_\pi[Y^*\mid S_t=s]=v_\pi(s),\qquad\operatorname{Var}_\pi(Y^*\mid S_t=s)\le\operatorname{Var}_\pi(G_t\mid S_t=s),
$$

và hiệu của hai phương sai bằng $\mathbb E_\pi\bigl[\operatorname{Var}_\pi(G_t\mid S_t=s,R_{t+1},S_{t+1})\mid S_t=s\bigr]$.

**Điều kiện áp dụng.** Mục tiêu dùng giá trị thật $v_\pi$ tại trạng thái kế tiếp; trạng thái Markov.

**Phạm vi.** Định lý không áp dụng cho mục tiêu TD với một bảng $V\ne v_\pi$ (Nhận xét 05.29), và không so sánh sai số của hai thuật toán, vốn còn phụ thuộc bước học, khởi tạo và dữ liệu.
:::

::: proof Chứng minh Định lý 05.28
**Bước 1 ($Y^*$ là kỳ vọng có điều kiện của $G_t$).** Khi $S_t=s$, đặt $I_1=(R_{t+1},S_{t+1})$ là thông tin của chuyển đầu. Theo Mệnh đề 05.4, $G_t=R_{t+1}+\gamma G_{t+1}$. Theo tính Markov của lợi tức, khi biết $S_{t+1}$ thì kỳ vọng của $G_{t+1}$ là $v_\pi(S_{t+1})$, không phụ thuộc $S_t$ và $R_{t+1}$. Do đó

$$
\begin{aligned}
\mathbb E_\pi[G_t\mid S_t=s,I_1]&=R_{t+1}+\gamma\,\mathbb E_\pi[G_{t+1}\mid S_t=s,I_1] &&\text{(Mệnh đề 05.4, } R_{t+1}\text{ đã biết)}\\
&=R_{t+1}+\gamma\,v_\pi(S_{t+1}) &&\text{(tính Markov của lợi tức)}\\
&=Y^* .
\end{aligned}
$$

**Bước 2 (kỳ vọng).** Theo luật kỳ vọng lặp, $\mathbb E_\pi[Y^*\mid S_t=s]=\mathbb E_\pi\bigl[\mathbb E_\pi[G_t\mid S_t=s,I_1]\mid S_t=s\bigr]=\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s)$.

**Bước 3 (luật phương sai toàn phần).** Viết gọn $\mathbb E_s[\cdot]=\mathbb E_\pi[\cdot\mid S_t=s]$ và $\operatorname{Var}_s$ tương tự. Áp dụng luật phương sai toàn phần cho $G_t$ với thông tin $I_1$, dưới điều kiện $S_t=s$:

$$
\begin{aligned}
\operatorname{Var}_s(G_t)&=\operatorname{Var}_s\bigl(\mathbb E_s[G_t\mid I_1]\bigr)+\mathbb E_s\bigl[\operatorname{Var}_s(G_t\mid I_1)\bigr]\\
&=\operatorname{Var}_s(Y^*)+\mathbb E_s\bigl[\operatorname{Var}_s(G_t\mid I_1)\bigr].
\end{aligned}
$$

Dòng thứ nhất là luật phương sai toàn phần; dòng thứ hai thay $\mathbb E_s[G_t\mid I_1]=Y^*$ từ Bước 1.

**Bước 4 (bất đẳng thức).** Số hạng cuối là kỳ vọng của một phương sai nên không âm, cho bất đẳng thức cần chứng minh. $\square$
:::

Định lý 05.28 nói thay phần đuôi bằng kỳ vọng của nó không đổi kỳ vọng của mục tiêu và không làm tăng phương sai; hiệu hai phương sai là dao động của phần đuôi, cột cuối của bảng trong Ví dụ 05.18. Dấu bằng xảy ra khi $G_t$ được xác định bởi chuyển đầu.

Hai giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ "dùng $v_\pi$": mục tiêu TD với một bảng khác $v_\pi$ có thể có phương sai lớn hơn $G_t$; Nhận xét 05.29 cho một bảng như vậy trên dãy bốn ô.
- Bỏ tính Markov: Bước 1 cần kỳ vọng của phần đuôi chỉ phụ thuộc $S_{t+1}$; trên ô gộp của Lunar Lander, nó còn phụ thuộc vị trí bên trong ô, nên Bước 3 không cho bất đẳng thức cho mục tiêu dùng lợi tức kỳ vọng theo ô.

Bước 1 dùng tính Markov; Bước 3 dùng giả thiết mômen bậc hai hữu hạn để luật phương sai toàn phần có nghĩa.

::: remark Nhận xét 05.29 (Không có thứ tự phương sai chung với bảng đang học)
Mục tiêu TD với một bảng $V$ khác $v_\pi$ không có thứ tự phương sai chung với $G_t$. Trên dãy bốn ô tại $\mathrm S$, với $\operatorname{Var}(G_t)=0{,}726$:

- với $V(\mathrm X)=0{,}5$ (bảng TD sau $e_1$), mục tiêu có phương sai $0{,}16\cdot1{,}5^2=0{,}36$, nhỏ hơn, nhưng chệch $-34/105$ (Ví dụ 05.16);
- với $V(\mathrm X)=10$, phương sai là $19{,}36$, lớn hơn, và độ chệch là $0{,}8\cdot(10-19/21)\approx7{,}28$.

Sai số bình phương trung bình quanh $v_\pi(\mathrm S)$, bằng phương sai cộng bình phương độ chệch, là $\approx0{,}465$ và $\approx72{,}3$ ở hai trường hợp, so với $0{,}726$ của $G_t$. Nhận định "TD luôn có phương sai thấp hơn Monte Carlo" vì thế không có căn cứ.
:::

**Trong thực hành.** Trong notebook Lunar Lander, kỳ vọng của $J$ gồm dao động của lợi tức quanh lợi tức kỳ vọng theo ô, không phụ thuộc bảng, cộng khoảng cách bình phương từ bảng tới lợi tức kỳ vọng đó; phần thứ nhất không vượt $J$ nhỏ nhất đã đạt, khoảng $1627$, còn $3021$ là $J$ của bảng hằng bằng trung bình lợi tức. TD(0) dùng bảng bắt đầu từ $\mathbf 0$ trên ô không Markov, và trong cả $2000$ lượt, TD(0) với $\alpha=0{,}5$ vẫn có $J$ lớn hơn Monte Carlo (Tình huống 05.1).

::: exercise Bài tập 05.10
Dữ kiện: dãy bốn ô, $\gamma=1$, $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Từ $\mathrm X$: sang $\mathrm G$ với xác suất $0{,}8$ và phần thưởng $+1$, sang $\mathrm S$ với xác suất $0{,}2$ và phần thưởng $0$.

(a) Tính $\operatorname{Var}(G_t\mid S_t=\mathrm X)$.
(b) Tính $\operatorname{Var}(Y^*\mid S_t=\mathrm X)$ và kiểm Định lý 05.28.
(c) Tỉ lệ phương sai do phần đuôi tại $\mathrm X$ là bao nhiêu.
:::

::: hint
$G_t\in\{1,-1\}$ nên $\operatorname{Var}(G_t)=1-v_\pi(\mathrm X)^2$. $Y^*$ nhận hai giá trị $1$ và $0+11/21$.
:::

::: solution
(a) $\operatorname{Var}(G_t\mid\mathrm X)=1-(19/21)^2=80/441\approx0{,}181$.

(b) $\operatorname{Var}(Y^*\mid\mathrm X)=0{,}8\cdot0{,}2\cdot(1-11/21)^2=0{,}16\cdot100/441=16/441\approx0{,}036$. Ta có $16/441\le80/441$, khớp Định lý 05.28.

(c) Hiệu là $64/441$, chiếm $64/80=80\%$ phương sai của $G_t$.

**Kiểm tra lại.** $\mathbb E[Y^*\mid\mathrm X]=0{,}8\cdot1+0{,}2\cdot11/21=(16{,}8+2{,}2)/21=19/21=v_\pi(\mathrm X)$.
:::

<!-- note-topic-id: lec-05-topic-11 -->
### 4.4 Điều kiện hội tụ của TD(0)

Mục 4.2–4.3 xét mục tiêu với bảng cố định; Thuật toán 05.21 thì sửa bảng sau mỗi chuyển, và theo Nhận xét 05.19, bước hằng giữ dao động mãi. Chúng ta cần biết lịch bước học nào bảo đảm bảng TD(0) tiến tới $v_\pi$, dưới giả thiết nào về môi trường và dữ liệu.

Một cách trực quan, bước học phải đủ lớn về tổng để ước lượng đi được tới đích từ bất kỳ khởi tạo nào, và đủ nhỏ về tổng bình phương để dao động của các mục tiêu không tích lũy. Mô tả này chưa phải định lý; ví dụ sau tách hai yêu cầu đó trên một mục tiêu đơn giản.

::: example Ví dụ 05.19 (Ba lịch bước học)
**Dữ kiện.** Một trạng thái, giá trị khởi tạo $V_0=0$, quy tắc $V_n=V_{n-1}+\alpha_n(Y_n-V_{n-1})$.

**Mục tiêu không đổi $Y_n=1$.** Khi đó $1-V_n=(1-\alpha_n)(1-V_{n-1})$, nên $1-V_n=\prod_{k=1}^{n}(1-\alpha_k)$.

- Với $\alpha_n=1/(n+1)$: $\prod_{k=1}^n\frac{k}{k+1}=\frac1{n+1}\to0$, nên $V_n\to1$.
- Với $\alpha_n=1/(n+1)^2$: tích lồng nhau $\prod_{m=2}^{n+1}\frac{(m-1)(m+1)}{m^2}=\frac{n+2}{2(n+1)}\to\frac12$, nên $V_n\to\frac12$ và không bao giờ tới $1$.
- Với $\alpha_n=\alpha$ hằng: $1-V_n=(1-\alpha)^n\to0$, nên $V_n\to1$.

**Kiểm tra lại.** $\sum_n1/(n+1)=\infty$ và $\sum_n1/(n+1)^2=\pi^2/6-1\approx0{,}645$: lịch thứ nhất thỏa cả hai tổng của Định lý 05.30 dưới đây, lịch thứ hai có tổng hữu hạn, còn bước hằng có $\sum_n\alpha^2=\infty$.
:::

Lịch $1/(n+1)^2$ có tổng hữu hạn nên dừng giữa đường dù mục tiêu không có nhiễu; bước hằng tới được đích khi không có nhiễu nhưng dao động mãi khi có nhiễu (Nhận xét 05.19); lịch $1/(n+1)$ thỏa cả hai điều kiện. Định lý sau phát biểu điều kiện đó cho TD(0).

::: theorem Định lý 05.30 (Hội tụ của TD(0) dạng bảng)
**Giả thiết.**

- $\mathcal S$ hữu hạn; $\pi$ Markov dừng, cố định; môi trường Markov dừng; trạng thái quan sát đầy đủ.
- Dữ liệu theo chính sách: mỗi mẫu chuyển có $A_t\sim\pi(\cdot\mid S_t)$ và $(S_{t+1},R_{t+1})\sim p(\cdot,\cdot\mid S_t,A_t)$.
- Phần thưởng bị chặn: $\lvert R_{t+1}\rvert\le R_{\max}$.
- $\gamma<1$; hoặc $\gamma=1$ và từ mọi trạng thái không kết thúc, lượt dưới $\pi$ kết thúc với xác suất $1$.
- Mỗi trạng thái $s\in\mathcal S$ được cập nhật vô hạn lần với xác suất $1$.
- Với mọi $s$, bước học ở lần cập nhật thứ $n$ của $s$ thỏa $\alpha_n(s)\in[0,1]$ và điều kiện Robbins–Monro theo trạng thái

$$
\sum_{n=1}^{\infty}\alpha_n(s)=\infty,\qquad\sum_{n=1}^{\infty}\alpha_n(s)^2<\infty .
$$

**Kết luận.** Bảng $V_t$ của Thuật toán 05.21 hội tụ về $v_\pi$ với xác suất $1$ khi số chuyển tiến tới vô hạn.

**Điều kiện áp dụng.** Dự đoán theo chính sách, dạng bảng, tiếp tục nhận mẫu mới.

**Phạm vi.** Định lý không cho tốc độ hội tụ, không áp dụng cho bước hằng, cho trạng thái không Markov, hay cho bảng được thay bằng hàm xấp xỉ (Bài 07). Chứng minh nằm ngoài phạm vi học phần.
:::

Chứng minh dùng lý thuyết xấp xỉ ngẫu nhiên (stochastic approximation) và nằm ngoài phạm vi học phần. Sutton và Barto (2018, §6.2, trang 124) phát biểu kết quả với điều kiện (2.7) của §2.5, trang 33; chú dẫn chương 6 (trang 139) dẫn Dayan (1992), Jaakkola, Jordan và Singh (1994), Tsitsiklis (1994). Ý tưởng: viết cập nhật thành $V(s)\leftarrow V(s)+\alpha_n(s)\bigl[(T_\pi V)(s)-V(s)+w\bigr]$, với nhiễu $w=\delta_t-\mathbb E[\delta_t\mid S_t=s,V_t]$ có kỳ vọng $0$ (Mệnh đề 05.27) và phương sai có điều kiện không vượt $A+B\lVert V_t\rVert_\infty^2$ với hai hằng số $A$, $B$. Phần tất định kéo bảng về điểm bất động của $T_\pi$, ánh xạ co khi $\gamma<1$; điều kiện Robbins–Monro làm nhiễu tắt dần. Khi $\gamma=1$ và lượt kết thúc từ mọi trạng thái, $T_\pi$ co theo một chuẩn cực đại có trọng số (Bertsekas và Tsitsiklis, 1996, chương 2), và Dayan (1992) xét đúng trường hợp chuỗi hấp thụ không chiết khấu.

::: remark Nhận xét 05.31 (Vai trò của từng giả thiết)
Mỗi giả thiết của Định lý 05.30 bị bỏ đều có phản ví dụ.

- Bỏ $\sum_n\alpha_n(s)=\infty$: lịch $1/(n+1)^2$ dừng ở $1/2$ (Ví dụ 05.19).
- Bỏ $\sum_n\alpha_n(s)^2<\infty$: bước hằng dao động mãi (Nhận xét 05.19).
- Bỏ "cập nhật vô hạn lần": một trạng thái không bao giờ được ghé giữ giá trị khởi tạo.
- Bỏ "dữ liệu theo chính sách": nếu dữ liệu sinh theo một chính sách khác $\pi$, Mệnh đề 05.27 cho kỳ vọng theo chính sách sinh dữ liệu, và đích là giá trị của chính sách đó.
- Bỏ tính Markov: trên ô gộp của Lunar Lander, TD(0) dạng bảng là một trường hợp của xấp xỉ hàm tuyến tính với đặc trưng là chỉ báo của ô; giới hạn của nó, nếu có, nói chung khác trung bình lợi tức theo ô, và phân tích của trường hợp này thuộc Bài 07 (Tsitsiklis và Van Roy, 1997).

So với Monte Carlo, kết luận giống nhau nhưng giả thiết bước học khác: Định lý 05.16, 05.17 được chứng minh cho $1/N(s)$, lịch tái tạo đúng trung bình mẫu; Định lý 05.30 cho TD(0) chấp nhận mọi lịch Robbins–Monro. Monte Carlo cần lượt kết thúc với mọi $\gamma$; TD(0) với $\gamma<1$ thì không.
:::

Định lý 05.16, 05.17 và 05.30 đều không nói phương pháp nào tới $v_\pi$ nhanh hơn, và Sutton và Barto (2018, §6.2, trang 124) ghi rằng chưa có chứng minh toán học cho câu hỏi này. Cũng theo Sutton và Barto, trên các bài toán ngẫu nhiên, thực nghiệm thường cho TD(0) hội tụ nhanh hơn Monte Carlo bước hằng, như ở dãy năm ô của Ví dụ 6.2 trong sách, trang 125; bài giảng gốc (trang 28) cũng ghi TD thường hiệu quả mẫu hơn Monte Carlo. Trên ô gộp không Markov của Tình huống 05.1, thứ tự ngược lại: TD(0) với $\alpha=0{,}5$ cho $J\approx2101$, còn Monte Carlo mọi lần ghé cho $J\approx1627$, với thước đo $J$ vốn nghiêng về Monte Carlo.

Cùng trang 28, bài giảng gốc ghi TD nhạy với giá trị khởi tạo hơn Monte Carlo. Mục tiêu $G_t$ không đọc bảng, nên khởi tạo $V_0(s)$ chỉ ảnh hưởng tới chính $V(s)$ và mất dần theo số mẫu tại $s$: mẫu đầu tiên xóa hẳn nó khi bước là $1/N(s)$, còn với bước hằng nó giữ trọng số $(1-\alpha)^n$ sau $n$ mẫu (Mệnh đề 05.9, 05.11). Mục tiêu TD đọc $V(S_{t+1})$, nên khởi tạo của các trạng thái kế tiếp đi vào mục tiêu tại $s$; phần đã đi vào chỉ giảm theo lịch bước học tại $s$ và còn lan sang các trạng thái đứng trước $s$. Ở tự chuyển, mục tiêu đọc chính $V_0(s)$, và với $\alpha=0{,}5$, $\gamma=0{,}99$, Ví dụ 05.12 cho khoảng cách tới điểm cố định còn khoảng $61\%$ sau $100$ tự chuyển.

**Trong thực hành.** Trong notebook Lunar Lander, lịch $\alpha_n=1/n$ thỏa giả thiết bước học của Định lý 05.30, nhưng sau $2000$ lượt, $J$ của TD(0) với lịch này còn $5086$, trung bình qua năm thứ tự lượt; bảng của Tình huống 05.1 ghi $5157{,}9$ cho một thứ tự lượt. Trên chuỗi tự chuyển, bước thứ $n$ chỉ thu hẹp khoảng cách tới điểm cố định của Ví dụ 05.12 theo hệ số $1-(1-\gamma)/n$, gần $1$ khi $\gamma=0{,}99$. Định lý là bảo đảm tiệm cận.

::: exercise Bài tập 05.11
Với mỗi lịch bước học sau, xác định nó có thỏa hai điều kiện Robbins–Monro của Định lý 05.30 không: (a) $\alpha_n=1/n$; (b) $\alpha_n=1/\sqrt n$; (c) $\alpha_n=0{,}1$; (d) $\alpha_n=1/n^2$; (e) $\alpha_n=n^{-0{,}6}$.
:::

::: hint
Chuỗi $\sum_nn^{-p}$ hội tụ khi và chỉ khi $p>1$.
:::

::: solution
(a) $\sum1/n=\infty$, $\sum1/n^2<\infty$: thỏa cả hai.

(b) $\sum n^{-1/2}=\infty$, nhưng $\sum1/n=\infty$: vi phạm điều kiện thứ hai.

(c) $\sum0{,}1=\infty$, $\sum0{,}01=\infty$: vi phạm điều kiện thứ hai.

(d) $\sum1/n^2<\infty$: vi phạm điều kiện thứ nhất.

(e) $p=0{,}6\le1$ nên $\sum n^{-0{,}6}=\infty$; $2p=1{,}2>1$ nên $\sum n^{-1{,}2}<\infty$: thỏa cả hai.

**Kiểm tra lại.** Lịch $n^{-p}$ thỏa cả hai điều kiện khi và chỉ khi $1/2<p\le1$.
:::

Như vậy, mục tiêu Monte Carlo không chệch, còn độ chệch của mục tiêu TD bằng $\gamma$ nhân độ lệch trung bình của bảng tại trạng thái kế tiếp (Mệnh đề 05.25), và sai số TD có kỳ vọng là phần dư Bellman (Mệnh đề 05.27). Mục tiêu một bước lý tưởng có phương sai không lớn hơn $G_t$ (Định lý 05.28), nhưng với bảng đang học thì không có thứ tự chung (Nhận xét 05.29). Với lịch Robbins–Monro theo trạng thái, TD(0) hội tụ về $v_\pi$ (Định lý 05.30).

Tuy nhiên, mọi kết quả hội tụ của Mục 2 và Mục 4 giả thiết các lượt mới tiếp tục đến, điều Mục 5 bỏ đi.

## 5. Dữ liệu cố định và cập nhật theo lô

Nhiều khi ta chỉ có một tập lượt hữu hạn. Bài thực hành Lunar Lander là một trường hợp như vậy: $2000$ lượt huấn luyện được thu một lần, việc thu chiếm phần lớn thời gian chạy của notebook, và phần 9 của notebook quét lại chính tập lượt đó (Tình huống 05.1). Trong tám lượt của Ví dụ 6.4 của Sutton và Barto (2018, §6.3, trang 127), liệt kê ở Ví dụ 05.20, lượt duy nhất qua $\mathrm A$ có lợi tức $0$, nhưng $\mathrm A$ luôn dẫn tới $\mathrm B$, và $\mathrm B$ thường cho phần thưởng $1$. Để dự đoán $v_\pi(\mathrm A)$, chúng ta cần một quy trình dùng lại dữ liệu và cần biết nó tiến tới nghiệm nào, theo tiêu chuẩn nào.

<!-- note-topic-id: lec-05-topic-16 -->
### 5.1 Tám lượt hai trạng thái và lượt quét đầu

Một cách trực quan, tám lượt cho phép hai cách đọc: theo lợi tức, $\mathrm A$ đáng $0$; theo chuyển, $\mathrm A$ luôn sang $\mathrm B$, nơi phần thưởng trung bình là $6/8$, nên $\mathrm A$ đáng $6/8$. Hai cách đọc này chưa phải phương pháp.

::: example Ví dụ 05.20 (Tám lượt hai trạng thái $\mathrm A$, $\mathrm B$)
**Dữ liệu.** Tập $\mathcal D$ gồm đúng tám lượt đã kết thúc; $\mathcal S=\{\mathrm A,\mathrm B\}$; $\gamma=1$; số liệu theo Sutton và Barto (2018, Ví dụ 6.4).

| Số lượt | Trạng thái và phần thưởng |
|---|---|
| $1$ | $\mathrm A\xrightarrow{0}\mathrm B\xrightarrow{0}$ kết thúc |
| $6$ | $\mathrm B\xrightarrow{1}$ kết thúc |
| $1$ | $\mathrm B\xrightarrow{0}$ kết thúc |

**Các mẫu.** Tại $\mathrm A$ có một lần ghé, lợi tức $0$, và một chuyển sang $\mathrm B$ với phần thưởng $0$. Tại $\mathrm B$ có tám lần ghé, mỗi lần là một chuyển vào trạng thái kết thúc; sáu lợi tức bằng $1$, hai lợi tức bằng $0$.

**Kiểm tra lại.** Tổng số chuyển trong $\mathcal D$ là $2+6+1=9$: một chuyển rời $\mathrm A$ và tám chuyển rời $\mathrm B$.
:::

::: example Ví dụ 05.21 (Lượt quét đầu)
**Dữ kiện.** Tám lượt $\mathcal D$: một lượt $\mathrm A\xrightarrow{0}\mathrm B\xrightarrow{0}$ kết thúc, sáu lượt $\mathrm B\xrightarrow{1}$ kết thúc, một lượt $\mathrm B\xrightarrow{0}$ kết thúc (Ví dụ 05.20); $\gamma=1$; bảng đầu lượt quét $V_0(\mathrm A)=V_0(\mathrm B)=0$; bước học $\alpha=1/8$. Bảng $V_0$ giữ nguyên trong lượt quét; các gia số được cộng rồi ghi một lần ở cuối.

**Monte Carlo.** Mục tiêu là lợi tức đã quan sát.

$$
\begin{aligned}
\Delta_0(\mathrm A)&=\tfrac18\,(0-0)=0,\\
\Delta_0(\mathrm B)&=\tfrac18\bigl[6\cdot(1-0)+2\cdot(0-0)\bigr]=\tfrac68 .
\end{aligned}
$$

**TD.** Mục tiêu là phần thưởng cộng giá trị trạng thái sau trong $V_0$; tại $\mathrm A$, mục tiêu là $0+V_0(\mathrm B)=0$; tại $\mathrm B$, giá trị tiếp nối của trạng thái kết thúc bằng $0$.

$$
\begin{aligned}
\Delta_0(\mathrm A)&=\tfrac18\bigl(0+V_0(\mathrm B)-V_0(\mathrm A)\bigr)=0,\\
\Delta_0(\mathrm B)&=\tfrac18\bigl[6\cdot(1+0-0)+2\cdot(0+0-0)\bigr]=\tfrac68 .
\end{aligned}
$$

**Ghi bảng.** Cả hai phương pháp cho $V_1=V_0+\Delta_0=(0;\ 3/4)$.

**Kiểm tra lại.** Với $\alpha=1/8$ và tám mẫu tại $\mathrm B$, tích $\alpha N(\mathrm B)=1$, nên $V_1(\mathrm B)$ bằng ngay trung bình $6/8$ của tám mục tiêu. Đây là đặc điểm của lựa chọn $\alpha$ này, không phải tính chất chung.
:::

Ở lượt quét đầu, hai phương pháp trùng nhau, vì $V_0(\mathrm B)=0$ nên mục tiêu TD tại $\mathrm A$ trùng lợi tức quan sát. Từ lượt quét thứ hai, mục tiêu TD tại $\mathrm A$ đọc $V_1(\mathrm B)=3/4$, và hai phương pháp tách ra.

### 5.2 Thuật toán cập nhật theo lô

Thuật toán sau phát biểu quy trình của Ví dụ 05.21 cho một tập dữ liệu bất kỳ. Chỉ số $k$ đếm lượt quét, khác thời điểm tương tác $t$; $\Delta_k(s)$ là **tổng gia số** của lượt quét $k$ tại $s$.

::: algorithm Thuật toán 05.32 (Cập nhật theo lô)
**Đầu vào.** Tập dữ liệu cố định $\mathcal D$ gồm các lượt đã kết thúc, sinh theo $\pi$; hệ số chiết khấu $\gamma$; loại mục tiêu, Monte Carlo hoặc TD, trong đó Monte Carlo theo lô dùng mọi lần ghé; bước học $\alpha>0$; ngưỡng dừng $\theta>0$; ngân sách $K$ lượt quét.

**Đầu ra.** Bảng $V$ trên các trạng thái xuất hiện trong $\mathcal D$.

**Giả thiết.** $\alpha$ đủ nhỏ theo nghĩa của Mệnh đề 05.33 hoặc 05.34.

**Khởi tạo.** $V_0$ tùy ý; $V_0=0$ tại trạng thái kết thúc. Với mục tiêu Monte Carlo, tính trước lợi tức của mọi mẫu bằng Mệnh đề 05.4.

**Tham số.** $\gamma$, $\alpha$, $\theta$, $K$.

1. Với $k=0,1,\ldots,K-1$:
2. Đặt $\Delta_k(s)=0$ với mọi $s$; giữ $V_k$ cố định trong cả lượt quét.
3. Với mỗi mẫu $(S_i,R_{i+1},S_{i+1})$ của $\mathcal D$ tại trạng thái $s=S_i$: tính mục tiêu $y_i$, bằng lợi tức $G_i$ với Monte Carlo, hoặc bằng $R_{i+1}+\gamma V_k(S_{i+1})$ với TD; cộng $\Delta_k(s)\leftarrow\Delta_k(s)+\alpha\bigl[y_i-V_k(s)\bigr]$.
4. Ghi đồng thời $V_{k+1}(s)=V_k(s)+\Delta_k(s)$ với mọi $s$; trạng thái kết thúc giữ $0$.
5. Nếu $\max_s\lvert V_{k+1}(s)-V_k(s)\rvert<\theta$, dừng và trả về $V_{k+1}$.
6. Hết $K$ lượt quét thì trả về $V_K$.

**Điều kiện dừng.** Thay đổi giữa hai bảng liên tiếp nhỏ hơn $\theta$, hoặc hết $K$ lượt quét.

**Chi phí mỗi bước.** Một lượt quét cần $O(\lvert\mathcal D\rvert)$ phép tính, với $\lvert\mathcal D\rvert$ là tổng số chuyển; bộ nhớ $O(\lvert\mathcal D\rvert+\lvert\mathcal S\rvert)$ cho dữ liệu và bảng.
:::

Khác Thuật toán 05.13 và 05.21, bảng không đổi trong một lượt quét, nên thứ tự các mẫu không ảnh hưởng kết quả; Ví dụ 05.21 là lượt quét $k=0$. Ngưỡng $\theta$ đo thay đổi giữa hai bảng, không đo khoảng cách tới nghiệm.

::: example Ví dụ 05.22 (Các lượt quét tiếp theo)
**Dữ kiện.** Tám lượt $\mathcal D$: một lượt $\mathrm A\xrightarrow{0}\mathrm B\xrightarrow{0}$ kết thúc, sáu lượt $\mathrm B\xrightarrow{1}$ kết thúc, một lượt $\mathrm B\xrightarrow{0}$ kết thúc (Ví dụ 05.20); $\gamma=1$; $\alpha=1/8$; bảng sau lượt quét đầu $V_1=(0;\ 3/4)$ cho cả hai phương pháp (Ví dụ 05.21).

**Monte Carlo.** Tại $\mathrm A$, tổng sai lệch là $0-0=0$; tại $\mathrm B$, là $6\cdot(1-\tfrac34)+2\cdot(0-\tfrac34)=0$. Bảng không đổi: $V_k=(0;\ 3/4)$ với mọi $k\ge1$.

**TD, lượt quét thứ hai.** Tại $\mathrm A$: $\Delta_1(\mathrm A)=\tfrac18\bigl(0+\tfrac34-0\bigr)=\tfrac3{32}$. Tại $\mathrm B$: tổng sai lệch là $6\cdot(1-\tfrac34)+2\cdot(0-\tfrac34)=0$. Do đó $V_2=(\tfrac3{32};\ \tfrac34)=(0{,}09375;\ 0{,}75)$.

**TD, mọi lượt quét.** Vì $V_k(\mathrm B)=3/4$ với $k\ge1$, truy hồi tại $\mathrm A$ là $V_{k+1}(\mathrm A)=V_k(\mathrm A)+\tfrac18\bigl(\tfrac34-V_k(\mathrm A)\bigr)$, tức $\tfrac34-V_{k+1}(\mathrm A)=\tfrac78\bigl(\tfrac34-V_k(\mathrm A)\bigr)$. Với $V_1(\mathrm A)=0$:

$$
V_k(\mathrm A)=\frac34\Bigl[1-\Bigl(\frac78\Bigr)^{k-1}\Bigr],\qquad k\ge1 .
$$

**Ngưỡng dừng và sai số.** Thay đổi ở lượt quét $k$ là $\tfrac18\cdot\tfrac34\cdot(7/8)^{k-1}$; với $\theta=0{,}01$, nó lần đầu nhỏ hơn $\theta$ ở $k=18$, khi bằng khoảng $0{,}0097$. Thuật toán trả về $V_{19}(\mathrm A)=\tfrac34[1-(7/8)^{18}]\approx0{,}682$, còn cách nghiệm $3/4$ khoảng $0{,}068$, gần bảy lần $\theta$.

**Kiểm tra lại.** $V_2(\mathrm A)=\tfrac34(1-\tfrac78)=\tfrac3{32}$, khớp phép tính trực tiếp.
:::

Ở đây sai số tại $\mathrm A$ gấp $7$ lần thay đổi của lượt quét, vì mỗi lượt quét chỉ thu hẹp sai số theo hệ số $7/8$; chặn sai số theo phần dư Bellman ở Bài 04 cũng nhân thêm $1/(1-\gamma)$ vì cùng lý do.

### 5.3 Hai nghiệm theo lô

Ví dụ 05.22 cho hai giới hạn khác nhau, $(0;\ 3/4)$ và $(3/4;\ 3/4)$. Chúng ta cần mô tả chúng cho một tập dữ liệu bất kỳ, cùng điều kiện trên $\alpha$. Gọi $N(s)\ge1$ là số lần ghé $s$ trong $\mathcal D$, cũng là số chuyển rời $s$.

::: proposition Mệnh đề 05.33 (Nghiệm Monte Carlo theo lô)
**Giả thiết.** Thuật toán 05.32 với mục tiêu Monte Carlo; $\bar g(s)$ là trung bình của $N(s)$ lợi tức tại $s$ trong $\mathcal D$; $0<\alpha N(s)<2$ với mọi $s$.

**Kết luận.** Với mọi $s$ và mọi $V_0$,

$$
V_k(s)-\bar g(s)=\bigl(1-\alpha N(s)\bigr)^k\bigl(V_0(s)-\bar g(s)\bigr)\to0 \quad(k\to\infty),
$$

và $\bar g(s)$ là nghiệm duy nhất của bài toán cực tiểu tổng bình phương $\sum_{i:S_i=s}(G_i-v)^2$ theo $v$.

**Điều kiện áp dụng.** Dữ liệu cố định; mỗi trạng thái được tính độc lập với các trạng thái khác.

**Phạm vi.** Nghiệm khớp dữ liệu huấn luyện; mệnh đề không nói nó gần $v_\pi$.
:::

::: proof Chứng minh Mệnh đề 05.33
**Bước 1 (truy hồi một trạng thái).** Lợi tức $G_i$ không phụ thuộc bảng, nên

$$
\begin{aligned}
V_{k+1}(s)&=V_k(s)+\alpha\sum_{i:S_i=s}\bigl(G_i-V_k(s)\bigr) &&\text{(bước 3–4 của Thuật toán 05.32)}\\
&=V_k(s)+\alpha N(s)\bigl(\bar g(s)-V_k(s)\bigr) &&\text{(định nghĩa } \bar g(s)\text{)}.
\end{aligned}
$$

Trừ hai vế cho $\bar g(s)$ được $V_{k+1}(s)-\bar g(s)=(1-\alpha N(s))(V_k(s)-\bar g(s))$; quy nạp theo $k$ cho đẳng thức của kết luận. Khi $0<\alpha N(s)<2$, ta có $\lvert1-\alpha N(s)\rvert<1$, nên vế phải tiến về $0$.

**Bước 2 (bình phương tối thiểu).** Hàm $f(v)=\sum_{i:S_i=s}(G_i-v)^2$ có đạo hàm $f'(v)=-2\sum_i(G_i-v)=-2N(s)(\bar g(s)-v)$, bằng $0$ duy nhất tại $v=\bar g(s)$, và $f''(v)=2N(s)>0$. $\square$
:::

Trên Ví dụ 05.20, $\bar g(\mathrm A)=0$ và $\bar g(\mathrm B)=6/8$, đúng giới hạn của Ví dụ 05.22; tổng bình phương tại $\mathrm B$ là $6(1-v)^2+2v^2$, có đạo hàm $16v-12$ bằng $0$ tại $v=3/4$. Điều kiện $\alpha N(s)<2$ là cần: với $N(\mathrm B)=8$, nó cho $\alpha<1/4$.

Với mục tiêu TD, phép quét đọc giá trị của trạng thái sau, nên các trạng thái không còn độc lập. Để mô tả giới hạn, ta dựng từ $\mathcal D$ một quá trình phần thưởng Markov (Markov reward process, MRP) thực nghiệm; mệnh đề sau nêu nó trong phần giả thiết.

::: proposition Mệnh đề 05.34 (Nghiệm TD theo lô)
**Giả thiết.** Thuật toán 05.32 với mục tiêu TD; mọi lượt của $\mathcal D$ kết thúc; $\gamma\in[0,1]$. Với mỗi trạng thái không kết thúc $s$ xuất hiện trong $\mathcal D$:

- $\hat r(s)$ là trung bình phần thưởng của $N(s)$ chuyển rời $s$;
- $\hat P(s'\mid s)$ là tỉ lệ các chuyển rời $s$ đi tới trạng thái không kết thúc $s'$; phần còn lại $1-\sum_{s'}\hat P(s'\mid s)$ là tỉ lệ chuyển vào trạng thái kết thúc;
- toán tử Bellman thực nghiệm là $(\hat TV)(s)=\hat r(s)+\gamma\sum_{s'}\hat P(s'\mid s)V(s')$;
- bước học thỏa $0<\alpha N(s)\le1$.

**Kết luận.**

- (a) Phương trình $V=\hat TV$, tức $(I-\gamma\hat P)V=\hat r$, có nghiệm duy nhất $\hat V_{\mathrm{TD}}$.
- (b) Với mọi $V_0$, $V_k\to\hat V_{\mathrm{TD}}$ khi $k\to\infty$.
- (c) $\hat V_{\mathrm{TD}}$ là bảng duy nhất mà tổng sai số TD tại mỗi trạng thái bằng $0$.

**Điều kiện áp dụng.** Dữ liệu cố định; điều kiện $\alpha N(s)\le1$ là đủ, không cần. Khi $\gamma<1$, không cần giả thiết mọi lượt kết thúc.

**Phạm vi.** $\hat V_{\mathrm{TD}}$ là giá trị đúng của quá trình phần thưởng Markov thực nghiệm $(\hat P,\hat r)$, không phải của môi trường thật. Chứng minh dưới đây đủ cho $\gamma<1$; với $\gamma=1$ chỉ nêu ý tưởng.
:::

::: proof Chứng minh Mệnh đề 05.34
**Bước 1 (tổng gia số qua $\hat T$).** Gom các chuyển rời $s$ theo trạng thái sau; chuyển vào trạng thái kết thúc góp giá trị tiếp nối $0$:

$$
\begin{aligned}
\Delta_k(s)&=\alpha\sum_{i:S_i=s}\bigl[R_{i+1}+\gamma V_k(S_{i+1})-V_k(s)\bigr]\\
&=\alpha N(s)\bigl[(\hat TV_k)(s)-V_k(s)\bigr].
\end{aligned}
$$

Dòng thứ nhất là bước 3 của Thuật toán 05.32; dòng thứ hai dùng định nghĩa của $\hat r$, $\hat P$. Tổng sai số TD tại $s$ bằng $0$ khi và chỉ khi $V_k(s)=(\hat TV_k)(s)$, nên (c) suy từ (a).

**Bước 2 (phép quét là ánh xạ co khi $\gamma<1$).** Đặt $\beta_s=\alpha N(s)\in(0,1]$. Theo Bước 1, một lượt quét là ánh xạ $\Phi$ với $(\Phi V)(s)=(1-\beta_s)V(s)+\beta_s(\hat TV)(s)$. Với hai bảng $U$, $W$, vì $\sum_{s'}\hat P(s'\mid s)\le1$ nên $\lvert(\hat TU)(s)-(\hat TW)(s)\rvert\le\gamma\lVert U-W\rVert_\infty$, do đó

$$
\lvert(\Phi U)(s)-(\Phi W)(s)\rvert\le\bigl[1-\beta_s(1-\gamma)\bigr]\lVert U-W\rVert_\infty .
$$

Hệ số $c=\max_s[1-\beta_s(1-\gamma)]$ nhỏ hơn $1$, nên $\Phi$ là ánh xạ co theo chuẩn cực đại.

**Bước 3 (kết luận khi $\gamma<1$).** Theo định lý điểm bất động cho ánh xạ co (ghi chú Bài 04, Mục 1), $\Phi$ có đúng một điểm bất động và $V_k=\Phi^kV_0$ hội tụ về điểm đó. Vì $\beta_s>0$, điểm bất động của $\Phi$ chính là nghiệm của $V=\hat TV$; điều này cho (a) và (b). $\square$
:::

Khi $\gamma=1$, hệ số $c$ của Bước 2 bằng $1$ và lập luận co một lượt quét không dùng được. Giả thiết mọi lượt của $\mathcal D$ kết thúc thay cho $\gamma<1$: từ mỗi trạng thái của $\mathcal D$, các chuyển của một lượt chứa nó, sau khi bỏ các vòng lặp, dẫn tới trạng thái kết thúc trong không quá $\lvert\mathcal S_{\mathcal D}\rvert$ bước, với $\mathcal S_{\mathcal D}$ là tập trạng thái không kết thúc xuất hiện trong $\mathcal D$, nên $\Phi^{\lvert\mathcal S_{\mathcal D}\rvert}$ là ánh xạ co theo chuẩn cực đại. Đây là cùng ý tưởng với chính sách kết thúc hầu chắc chắn trong Bertsekas và Tsitsiklis (1996, chương 2); Ví dụ 05.22 kiểm kết luận trên tám lượt $\mathrm A$, $\mathrm B$ với $\gamma=1$.

Trên Ví dụ 05.20, $\hat P(\mathrm B\mid\mathrm A)=1$, $\hat r(\mathrm A)=0$, $\hat P(\cdot\mid\mathrm B)=0$, $\hat r(\mathrm B)=6/8$. Phương trình $V=\hat TV$ cho $V(\mathrm B)=3/4$ và $V(\mathrm A)=0+V(\mathrm B)=3/4$, đúng giới hạn của Ví dụ 05.22. Với $\alpha=1/8$, $\alpha N(\mathrm B)=1$ và $\alpha N(\mathrm A)=1/8$, nên giả thiết bước học của Mệnh đề 05.34 thỏa.

![Mô hình ước lượng từ tám lượt: A sang B với xác suất 1 và phần thưởng 0; B kết thúc với phần thưởng 1 với xác suất 6/8 và với phần thưởng 0 với xác suất 2/8; trạng thái kết thúc có giá trị 0.](img/lec-05/ab-empirical.svg)

Hình vẽ quá trình phần thưởng Markov thực nghiệm $(\hat P,\hat r)$: mũi tên từ $\mathrm A$ mang tỉ lệ $1$, hai mũi tên từ $\mathrm B$ mang tỉ lệ $6/8$, $2/8$. Nghiệm TD theo lô là giá trị đúng của mô hình này; Thuật toán 05.32 tới được nó mà không dựng mô hình.

::: remark Nhận xét 05.35 (Hai tiêu chuẩn và giới hạn của chúng)
- Monte Carlo theo lô khớp các lợi tức đã quan sát; TD theo lô khớp quá trình phần thưởng Markov thực nghiệm. Hai nghiệm khác nhau tại $\mathrm A$ vì hai tiêu chuẩn khác nhau, không vì một phương pháp tính sai.
- Nghiệm TD theo lô là ước lượng tương đương chắc chắn (certainty-equivalence estimate): giá trị đúng nếu quá trình phần thưởng Markov thực nghiệm là quá trình thật (Sutton và Barto, 2018, §6.3, trang 128). Nghiệm Monte Carlo có sai số bằng $0$ trên dữ liệu huấn luyện.
- Khi quá trình thật là Markov, nghiệm TD dùng cả tám lần ghé $\mathrm B$ cho phần sau $\mathrm A$, thay vì một lợi tức; Sutton và Barto (2018, trang 128) nêu rằng khi đó ta kỳ vọng nghiệm TD có sai số nhỏ hơn trên dữ liệu tương lai. Khi trạng thái không Markov, lập luận này mất căn cứ.
- Tám lượt không đủ để gọi một nghiệm là đúng hơn với mọi môi trường thật.
:::

Mệnh đề 05.34 nối Mục 5 với Bài 04: nghiệm TD theo lô giải cùng hệ $(I-\gamma P)V=r$ như đánh giá chính sách bằng quy hoạch động, với $(\hat P,\hat r)$ thay cho $(P_\pi,r_\pi)$. Dựng $\hat P$ cần bộ nhớ cỡ $\lvert\mathcal S_{\mathcal D}\rvert^2$, còn mỗi lượt quét chỉ cần bộ nhớ cỡ $\lvert\mathcal S_{\mathcal D}\rvert$ ngoài dữ liệu (Sutton và Barto, 2018, §6.3, trang 128).

**Trong thực hành.** Notebook Lunar Lander chạy Thuật toán 05.32 với bước $1/N(s)$ cho mỗi ô, tức $\beta_s=1$; TD theo lô dừng sau $598$ lượt quét và khớp nghiệm của $(I-\gamma\hat P)V=\hat r$ giải trực tiếp. Ô gộp không Markov, nên hai nghiệm theo lô khác nhau như trong Ví dụ 05.20 (Tình huống 05.1).

::: exercise Bài tập 05.12
Dữ kiện: tám lượt gồm một lượt $\mathrm A\xrightarrow{0}\mathrm B\xrightarrow{0}$ kết thúc, sáu lượt $\mathrm B\xrightarrow{1}$ kết thúc, một lượt $\mathrm B\xrightarrow{0}$ kết thúc (Ví dụ 05.20); $\gamma=1$, $\alpha=1/8$, bảng sau lượt quét đầu $V_1=(0;\ 3/4)$ cho cả hai phương pháp.

Tính $V_3(\mathrm A)$ của TD theo lô.
:::

::: hint
Dùng công thức đóng của Ví dụ 05.22, hoặc tính trực tiếp một lượt quét từ $V_2$.
:::

::: solution
$V_3(\mathrm A)=\tfrac34\bigl[1-(7/8)^2\bigr]=\tfrac34\cdot\tfrac{15}{64}=\tfrac{45}{256}\approx0{,}176$.

**Kiểm tra lại.** Theo truy hồi trực tiếp: $V_3(\mathrm A)=\tfrac3{32}+\tfrac18\bigl(\tfrac34-\tfrac3{32}\bigr)=\tfrac3{32}+\tfrac{21}{256}=\tfrac{45}{256}$.
:::

Như vậy, trên dữ liệu cố định, Monte Carlo theo lô cho trung bình lợi tức theo trạng thái (Mệnh đề 05.33), TD theo lô cho giá trị đúng của quá trình phần thưởng Markov thực nghiệm (Mệnh đề 05.34); hai nghiệm khác nhau vì hai tiêu chuẩn khác nhau (Nhận xét 05.35). Khi trạng thái không Markov, không nghiệm nào được bảo đảm gần $v_\pi$; phần sau dùng các kết quả của Mục 1–5 trong bài toán cụ thể.

<!-- note-topic-id: lec-05-topic-14 -->
## Tình huống áp dụng và ứng dụng

Các Mục 1–5 trả lời bài toán trung tâm bằng ba kết luận có điều kiện, tóm trong bảng sau; với Monte Carlo khi trạng thái không Markov và độ dài lượt bị chặn, xem Diễn giải của Tình huống 05.1.

| Dữ liệu và yêu cầu | Lựa chọn có căn cứ | Kết quả dùng |
|---|---|---|
| Có lượt hoàn chỉnh | Monte Carlo, nêu quy tắc lần ghé và bước học | Thuật toán 05.13, Định lý 05.16–05.17 |
| Cần cập nhật sau mỗi chuyển; có lượt bị cắt ngắn; trạng thái Markov | TD(0) với lịch Robbins–Monro | Thuật toán 05.21, Định lý 05.30 |
| Tập dữ liệu cố định, quét lại nhiều lần | Chọn tiêu chuẩn: lợi tức quan sát hoặc quá trình phần thưởng Markov thực nghiệm | Thuật toán 05.32, Mệnh đề 05.33–05.34 |

Tình huống 05.1 đối chiếu bảng trên với bài thực hành Lunar Lander; Tình huống 05.2 xét một giả thiết bị vi phạm và hậu quả của nó.

::: application Tình huống 05.1 (Dự đoán giá trị của bộ điều khiển heuristic trên Lunar Lander)
**Bài toán và môi trường.** Môi trường `LunarLander-v3` của Gymnasium, bốn hành động rời rạc, không gió. Chính sách cần đánh giá là bộ điều khiển heuristic của Gymnasium, thay bằng một hành động ngẫu nhiên đều với xác suất $\varepsilon=0{,}1$. Cần dự đoán $v_\pi$ với $\gamma=0{,}99$ từ $2000$ lượt huấn luyện, trong đó $42$ lượt bị cắt ngắn ở bước $1000$; $500$ lượt kiểm tra dùng để đo sai số.

**Mô hình hóa.** Quan sát tám chiều được gộp thành $9216$ ô; ô là "trạng thái" của bảng $V$. Lượt kết thúc thật khi tàu rơi hoặc ra khỏi khung, với phần thưởng $-100$, hoặc khi tàu nằm yên, với phần thưởng $+100$; bước $1000$ là điểm cắt, không phải trạng thái kết thúc (Định nghĩa 05.3).

**Kiểm tra giả thiết.**

- Chính sách cố định, dữ liệu theo chính sách, các lượt độc lập cùng phân phối nhờ hạt giống riêng: thỏa.
- Phần thưởng bị chặn: thỏa, vì quan sát nằm trong một hộp giới hạn.
- Lượt kết thúc: $42$ lượt không thỏa, nên Thuật toán 05.13 bỏ chúng, còn Thuật toán 05.21 dùng các chuyển của chúng (Nhận xét 05.22).
- Trạng thái Markov: không thỏa, vì một ô chứa nhiều quan sát với tương lai khác nhau. Mệnh đề 05.7, Định lý 05.28 và Định lý 05.30 không áp dụng nguyên văn.

**Thước đo.** Notebook dùng $J(V)$, trung bình của $(G_t-V(S_t))^2$ trên các mẫu của $493$ lượt kiểm tra kết thúc thật. Gọi $\mu(c)$ là lợi tức kỳ vọng tại ô $c$ theo phân bố các lần ghé. Kỳ vọng của $J$ bằng phần dao động của lợi tức quanh $\mu$, không phụ thuộc $V$, cộng trung bình của $(\mu(S_t)-V(S_t))^2$, nên $J$ nhỏ nhất tại $V=\mu$. Hai mốc để đọc: bảng hằng bằng trung bình lợi tức cho $J\approx3021$, và bảng $\mathbf 0$ cho $J\approx5797$.

**Áp dụng.** Bảng dưới tính trên một thứ tự lượt huấn luyện, nên TD(0) với $\alpha_n=1/n$ cho $5157{,}9$, khác $5086$ ở Mục 4.4, vốn là trung bình qua năm thứ tự lượt.

| Bảng | Kết quả của chương | $J$ | Trung bình $V(S_0)$ |
|---|---|---|---|
| Monte Carlo mọi lần ghé, $1/N(s)$; cũng là Monte Carlo theo lô | Thuật toán 05.13, Mệnh đề 05.33 | $1626{,}8$ | $55{,}43$ |
| Monte Carlo lần ghé đầu tiên, $1/N(s)$ | Thuật toán 05.13 | $1673{,}4$ | $54{,}36$ |
| TD theo lô, cùng các lượt kết thúc | Mệnh đề 05.34 | $1803{,}4$ | $58{,}13$ |
| TD(0), $\alpha=0{,}5$ | Thuật toán 05.21 | $2100{,}8$ | $52{,}33$ |
| TD(0), $\alpha_n=1/n$ | Thuật toán 05.21 | $5157{,}9$ | $1{,}04$ |

Trung bình $G_0$ trên $500$ lượt kiểm tra là $56{,}04\pm2{,}70$ với khoảng tin cậy xấp xỉ $95\%$.

**Diễn giải.**

- Bước 1 và Bước 4 của chứng minh Định lý 05.17 không dùng tính Markov; khả tích ở Bước 2 suy từ $T\le1000$ của các lượt được giữ, và các lượt giữ lại vẫn độc lập cùng phân phối. Vì vậy Monte Carlo mọi lần ghé hội tụ về $\mu$; chỉ Bước 3, nơi giới hạn được đồng nhất với $v_\pi$, cần trạng thái Markov. $J$ nhỏ nhất tại $V=\mu$, nên thước đo này nghiêng về Monte Carlo mọi lần ghé.
- TD theo lô là giá trị đúng của quá trình phần thưởng Markov thực nghiệm trên ô (Mệnh đề 05.34), khác $\mu$ vì ô không Markov; trung vị của $\lvert V_{\mathrm{MC}}-V_{\mathrm{TD}}\rvert$ là $15{,}2$, một phiên bản lớn của Ví dụ 05.20.
- TD(0) với $1/n$ còn gần bảng khởi tạo $\mathbf 0$. Trong một bước mô phỏng $0{,}02$ giây, tàu dịch chuyển ít so với kích thước một ô gộp, nên $70\%$ chuyển là tự chuyển, và trên chuỗi tự chuyển bước $1/n$ tiến chậm tới điểm cố định (Ví dụ 05.12, Mục 4.4).

**Giới hạn.** Các số thuộc một lần chạy với gymnasium 1.3.0, một cách chia ô và các bước học đã nêu; $J$ đo khoảng cách tới $\mu$, không tới $v_\pi$ của tàu thật.

**Dẫn ngược lý thuyết.** Định nghĩa 05.1, 05.3; Thuật toán 05.13, 05.21, 05.32; Định lý 05.17 (Bước 1 và 4 dùng cho ô gộp, Bước 2 thay bằng chặn $T\le1000$, Bước 3 cần giả thiết Markov bị vi phạm); Mệnh đề 05.33, 05.34; Nhận xét 05.22; Ví dụ 05.12.
:::

::: application Tình huống 05.2 (Coi điểm cắt là trạng thái kết thúc)
**Bài toán.** Một cách xử lý lượt bị cắt ngắn là coi trạng thái tại điểm cắt như trạng thái kết thúc, tức đặt giá trị tiếp nối bằng $0$ và tính lợi tức từ các phần thưởng đã quan sát. Cần xác định hậu quả đối với mục tiêu Monte Carlo và mục tiêu TD.

**Mô hình hóa trên tàu đổ bộ thu nhỏ.** Dữ kiện của Ví dụ 05.1, $\gamma=1$, $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$; mỗi lượt bị cắt sau tối đa hai chuyển. Từ $\mathrm S$, có ba khả năng trong hai chuyển: vào $\mathrm L$ ngay với xác suất $0{,}2$, đi $\mathrm S\to\mathrm X\to\mathrm G$ với xác suất $0{,}64$, đi $\mathrm S\to\mathrm X\to\mathrm S$ với xác suất $0{,}16$ và bị cắt.

**Giả thiết bị vi phạm.** Định nghĩa 05.3 đòi hỏi $S_T$ là trạng thái kết thúc thật. Ở khả năng thứ ba, $S_2=\mathrm S$ không kết thúc, và phần đuôi sau bước $2$ có kỳ vọng $v_\pi(\mathrm S)\ne0$.

**Hậu quả cho mục tiêu Monte Carlo.** "Lợi tức" tại $t=0$ khi coi điểm cắt là kết thúc có kỳ vọng

$$
0{,}2\cdot(-1)+0{,}64\cdot1+0{,}16\cdot0=0{,}44,
$$

thay cho $11/21\approx0{,}524$. Độ chệch là $0{,}44-11/21=-0{,}16\cdot11/21\approx-0{,}084$, đúng bằng xác suất bị cắt nhân giá trị của phần đuôi bị bỏ.

**Hậu quả cho mục tiêu TD.** Trên chuyển $\mathrm X\to\mathrm S$ tại điểm cắt, mục tiêu đúng là $0+\gamma v_\pi(\mathrm S)$; đặt giá trị tiếp nối bằng $0$ làm mục tiêu của chuyển đó lệch $-v_\pi(\mathrm S)=-11/21$ so với mục tiêu lý tưởng. Đây là sai lệch có điều kiện trên một chuyển, không cùng loại với độ chệch kỳ vọng $-0{,}084$ của Monte Carlo ở trên.

**Xử lý đúng và giới hạn.** Monte Carlo bỏ các lượt bị cắt (Thuật toán 05.13), với cái giá là chỉ học từ các lượt kết thúc trước điểm cắt, nên ước lượng có điều kiện trên sự kiện đó; TD(0) giữ giá trị tiếp nối $V(S_{t+1})$ ở chuyển cuối (Nhận xét 05.22). Notebook Lunar Lander xử lý $42$ lượt bị cắt theo cách này.

**Dẫn ngược lý thuyết.** Định nghĩa 05.3 (lượt kết thúc), Mệnh đề 05.4 (phạm vi với lượt bị cắt), Nhận xét 05.2, 05.14, 05.22.

**Kiểm tra lại.** $0{,}16\cdot11/21=1{,}76/21\approx0{,}0838$, và $11/21-0{,}0838\approx0{,}44$.
:::

**Ứng dụng.**

- Bài 06 dùng lại hai mục tiêu của chương cho giá trị hành động $q_\pi(s,a)$: Monte Carlo lấy trung bình lợi tức sau lần ghé cặp trạng thái–hành động, còn Sarsa dùng mục tiêu $R_{t+1}+\gamma Q(S_{t+1},A_{t+1})$ cùng dạng Định nghĩa 05.20, và điều kiện Robbins–Monro được áp dụng theo cặp.
- Bài 07 thay bảng bằng hàm xấp xỉ có tham số. Bảng trên ô gộp của Tình huống 05.1 là trường hợp riêng với đặc trưng là chỉ báo của ô; mục tiêu TD trở thành mục tiêu của cập nhật bán gradient (Mục 2.3), và bài thực hành Lunar Lander của Bài 07 dùng lại môi trường này.
- Bài 08 dùng mục tiêu bootstrap cho mạng Q sâu, với một mạng mục tiêu giữ cố định trong một khoảng thời gian, tương tự việc giữ bảng cố định khi lấy kỳ vọng ở Mệnh đề 05.25, và một bộ nhớ phát lại dùng lại dữ liệu cũ như Thuật toán 05.32.
- Notebook thực hành của Bài 05 cài đặt Thuật toán 05.13, 05.21, 05.32 trên Lunar Lander và đo các đại lượng của Tình huống 05.1.

<!-- note-topic-id: lec-05-topic-15 -->
## Tóm tắt chương

Chương bắt đầu từ giới hạn của Bài 04: phép lặp $V\leftarrow T_\pi V$ cần mô hình, còn tàu đổ bộ thu nhỏ chỉ cho hai lượt (Định nghĩa 05.1). Monte Carlo lấy trung bình lợi tức sau lần ghé (Định nghĩa 05.3, 05.6, 05.8); mỗi lợi tức có kỳ vọng $v_\pi(s)$ (Mệnh đề 05.7), và với bước $1/N(s)$ trung bình hội tụ về $v_\pi$ (Định lý 05.16, 05.17). TD(0) thay phần lợi tức chưa quan sát bằng giá trị ước lượng (Định nghĩa 05.20, Thuật toán 05.21), nên cập nhật sau mỗi chuyển. Mục tiêu TD chệch theo độ lệch của bảng (Mệnh đề 05.25), còn mục tiêu một bước lý tưởng có phương sai không lớn hơn lợi tức (Định lý 05.28). Với lịch Robbins–Monro theo trạng thái, TD(0) cũng hội tụ về $v_\pi$ (Định lý 05.30). Trên dữ liệu cố định, hai phương pháp cho hai nghiệm theo hai tiêu chuẩn (Mệnh đề 05.33, 05.34). Bài 06 dùng các ước lượng này để cải thiện chính sách.

**Định nghĩa và kết quả theo mục.**

- Mục 1: bài toán dự đoán phi mô hình, mẫu chuyển, dữ liệu theo chính sách (Định nghĩa 05.1); mẫu, mô hình và giá trị chuẩn (Nhận xét 05.2).
- Mục 2: lượt, lợi tức (Định nghĩa 05.3); truy hồi (Mệnh đề 05.4); đuôi hình học của $T$ (Bổ đề 05.5); lần ghé (Định nghĩa 05.6); kỳ vọng sau lần ghé thứ $k$ (Mệnh đề 05.7); ước lượng Monte Carlo (Định nghĩa 05.8); trung bình gia tăng (Mệnh đề 05.9); mục tiêu cập nhật, bước học (Định nghĩa 05.10); trọng số bước hằng (Mệnh đề 05.11); hai trục lựa chọn (Nhận xét 05.12); Thuật toán 05.13, Nhận xét 05.14; không chệch, hội tụ hầu chắc chắn (Định nghĩa 05.15); hội tụ (Định lý 05.16, 05.17); mọi lần ghé chệch ở số lượt hữu hạn (Nhận xét 05.18); bước hằng không hội tụ (Nhận xét 05.19).
- Mục 3: mục tiêu TD, sai số TD, mục tiêu bootstrap (Định nghĩa 05.20); TD(0) dạng bảng (Thuật toán 05.21); trạng thái kết thúc, tự chuyển, cắt ngắn (Nhận xét 05.22); chi phí (Nhận xét 05.23).
- Mục 4: độ chệch của mục tiêu (Định nghĩa 05.24, Mệnh đề 05.25, Hệ quả 05.26); kỳ vọng sai số TD là phần dư Bellman (Mệnh đề 05.27); phương sai mục tiêu lý tưởng (Định lý 05.28, Nhận xét 05.29); hội tụ TD(0) (Định lý 05.30, Nhận xét 05.31).
- Mục 5: cập nhật theo lô (Thuật toán 05.32); nghiệm Monte Carlo theo lô (Mệnh đề 05.33); nghiệm TD theo lô (Mệnh đề 05.34); hai tiêu chuẩn (Nhận xét 05.35).

**Công thức cần nhớ.** Lợi tức và truy hồi:

$$
G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1}=R_{t+1}+\gamma G_{t+1},\qquad G_T=0 .
$$

Trung bình gia tăng và bước học hằng:

$$
V_n=V_{n-1}+\frac1n\bigl[g_n-V_{n-1}\bigr],\qquad V_n=(1-\alpha)^nV_0+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}g_i .
$$

TD(0):

$$
\delta_t=R_{t+1}+\gamma V_t(S_{t+1})-V_t(S_t),\qquad V_{t+1}(S_t)=V_t(S_t)+\alpha_n(S_t)\,\delta_t .
$$

Độ chệch của mục tiêu TD và bất đẳng thức phương sai:

$$
\operatorname{bias}(Y;s)=\gamma\,\mathbb E_\pi\bigl[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s\bigr],\qquad\operatorname{Var}_\pi(Y^*\mid S_t=s)\le\operatorname{Var}_\pi(G_t\mid S_t=s).
$$

Điều kiện Robbins–Monro theo trạng thái và nghiệm TD theo lô:

$$
\sum_n\alpha_n(s)=\infty,\quad\sum_n\alpha_n(s)^2<\infty;\qquad(I-\gamma\hat P)\hat V_{\mathrm{TD}}=\hat r .
$$

**Giả thiết hay bị bỏ quên.**

- Lượt bị cắt ngắn không phải lượt kết thúc; không đặt giá trị tiếp nối bằng $0$ tại điểm cắt (Tình huống 05.2).
- Mệnh đề 05.7, Định lý 05.28 và Định lý 05.30 cần trạng thái Markov; ô gộp của bài thực hành không thỏa.
- Chính sách cố định và dữ liệu sinh theo chính sách đó.
- Hội tụ cần bước học giảm: $1/N(s)$ cho Monte Carlo, Robbins–Monro cho TD(0); bước hằng chỉ cho dao động quanh đích.
- Độ chệch và phương sai của mục tiêu được tính với bảng cố định; chúng không phải độ chệch và phương sai của bảng sau nhiều cập nhật.
- Trong TD(0), đọc bảng xong rồi mới ghi, kể cả khi tự chuyển.
- Ngưỡng dừng trên thay đổi giữa hai bảng không đo sai số tới nghiệm (Ví dụ 05.22).

Chương còn hai giới hạn: chính sách chưa được cải thiện, việc của Bài 06; và bảng cần một phần tử cho mỗi trạng thái, nên quan sát liên tục phải gộp thành ô và mất tính Markov, việc của Bài 07.

## Bài tập củng cố

Các bài tập trong các mục và ba bài dưới đây là bộ bài tập của chương; mỗi mục tiêu học tập có ít nhất một bài: mục tiêu 1 với Bài tập 05.2; mục tiêu 2 với Bài tập 05.3; mục tiêu 3 với Bài tập 05.4, 05.5, 05.8; mục tiêu 4 với Bài tập 05.6, 05.7, 05.8; mục tiêu 5 với Bài tập 05.9, 05.10, 05.11, 05.14; mục tiêu 6 với Bài tập 05.12, 05.13, 05.15. Bộ bài giao chính thức của buổi học là [Bài tập Bài 05](material-viewer.html?doc=materials/lec-05/exercises.md&deck=lecture-05-du-doan-phi-mo-hinh.html). Tệp này giữ số hiệu và kết quả của Bài tập 05.8, 05.11, 05.12 trong thân chương và không lặp các đề 05.13–05.15 dưới đây. Mười ba bài mới 05.16–05.28 nối tiếp bộ đếm; Bài tập 05.18 chạy bốn cấu hình Monte Carlo tại $\mathrm S$ với $\gamma=0{,}9$, còn ba bài 05.26–05.28 dùng số liệu của notebook Lunar Lander.

### Mức nhận biết

::: exercise Bài tập 05.13
Dữ kiện: tàu đổ bộ thu nhỏ với hai lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$; tám lượt cố định gồm một lượt $\mathrm A\xrightarrow{0}\mathrm B\xrightarrow{0}$ kết thúc, sáu lượt $\mathrm B\xrightarrow{1}$ kết thúc, một lượt $\mathrm B\xrightarrow{0}$ kết thúc, với nghiệm Monte Carlo theo lô $(0;\ 3/4)$ và nghiệm TD theo lô $(3/4;\ 3/4)$.

(a) Sau lượt hoàn chỉnh $e_1$, nêu hai lựa chọn cần xác định trước khi báo cáo kết quả Monte Carlo.
(b) Sau tiền tố chưa kết thúc $\mathrm S\to\mathrm X$, nêu một phương pháp cập nhật được ngay và thông tin nó cần.
(c) Trên tám lượt $\mathrm A$, $\mathrm B$, nêu điều kiện để gọi một nghiệm theo lô là tốt hơn nghiệm kia.
:::

::: hint
Lần lượt xét Nhận xét 05.12, Định nghĩa 05.20 và Nhận xét 05.35.
:::

::: solution
(a) Quy tắc lần ghé, đầu tiên hay mọi lần, và quy tắc bước học, $1/N(s)$ hay hằng số; với bước hằng, cần nêu thêm giá trị khởi tạo vì nó còn ảnh hưởng (Mệnh đề 05.11).

(b) TD(0), cần phần thưởng vừa nhận, $V(\mathrm X)$, $V(\mathrm S)$, $\gamma$ và bước học để tính $Y=0+\gamma V(\mathrm X)$.

(c) Phải nêu tiêu chuẩn trước: khớp lợi tức quan sát hay khớp quá trình phần thưởng Markov thực nghiệm. Muốn so với môi trường thật cần giá trị chuẩn hoặc dữ liệu đánh giá riêng; tám lượt không đủ.

**Kiểm tra lại.** Ba câu ứng với ba dòng của bảng lựa chọn đầu mục Tình huống.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 05.14
Cho một lượt kết thúc tại $T$ và một bảng $V$ được giữ cố định trong cả lượt, với $V=0$ tại trạng thái kết thúc. Đặt $\delta_k=R_{k+1}+\gamma V(S_{k+1})-V(S_k)$. Chứng minh rằng với mọi $t<T$,

$$
G_t-V(S_t)=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k .
$$

Kiểm tra đẳng thức trên lượt $e_1$ của tàu đổ bộ thu nhỏ với $\gamma=1$ và $V(\mathrm S)=0$, $V(\mathrm X)=0{,}5$, tại $t=0$.
:::

::: hint
Quy nạp lùi theo $t$, bắt đầu từ $t=T-1$, dùng Mệnh đề 05.4 và cộng trừ $\gamma V(S_{t+1})$.
:::

::: solution
**Bước 1 ($t=T-1$).** $G_{T-1}=R_T$ và $V(S_T)=0$, nên $G_{T-1}-V(S_{T-1})=R_T+\gamma V(S_T)-V(S_{T-1})=\delta_{T-1}$.

**Bước 2 (bước quy nạp).** Giả sử đẳng thức đúng tại $t+1$. Khi đó

$$
\begin{aligned}
G_t-V(S_t)&=R_{t+1}+\gamma G_{t+1}-V(S_t) &&\text{(Mệnh đề 05.4)}\\
&=\bigl[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\bigr]+\gamma\bigl[G_{t+1}-V(S_{t+1})\bigr] &&\text{(cộng trừ } \gamma V(S_{t+1})\text{)}\\
&=\delta_t+\gamma\sum_{k=t+1}^{T-1}\gamma^{k-t-1}\delta_k &&\text{(giả thiết quy nạp)}\\
&=\sum_{k=t}^{T-1}\gamma^{k-t}\delta_k . &&
\end{aligned}
$$

$\square$

**Kiểm tra trên $e_1$.** Bốn sai số TD với bảng cố định: $\delta_0=0+0{,}5-0=0{,}5$; $\delta_1=0+0-0{,}5=-0{,}5$; $\delta_2=0{,}5$; $\delta_3=1+0-0{,}5=0{,}5$. Tổng là $1$, và $G_0-V(\mathrm S)=1-0=1$.
:::

### Mức vận dụng

::: exercise Bài tập 05.15
Một môi trường có lượt rất dài, phần thưởng khác $0$ chỉ xuất hiện ở cuối lượt, và yêu cầu là cập nhật ước lượng sau mỗi chuyển. Chọn phương pháp của chương, nêu thông tin nó dùng, và nêu giới hạn của mục tiêu cập nhật của nó dựa trên các kết quả đã chứng minh.
:::

::: hint
Phân biệt thời điểm có lợi tức đầy đủ với thời điểm có phần thưởng một bước và trạng thái kế tiếp. Xem Mệnh đề 05.25, Định lý 05.28, Ví dụ 05.12.
:::

::: solution
TD(0) đáp ứng yêu cầu cập nhật sau mỗi chuyển; Monte Carlo phải chờ lượt kết thúc. TD(0) dùng phần thưởng vừa nhận, trạng thái sau, bảng hiện tại, $\gamma$ và bước học.

Giới hạn: mục tiêu TD chệch theo độ lệch của bảng (Mệnh đề 05.25), và với phần thưởng chỉ ở cuối, thông tin lan ngược từng chuyển một (Ví dụ 05.9, 05.13). Lợi thế phương sai của Định lý 05.28 chỉ có với mục tiêu lý tưởng (Nhận xét 05.29); tự chuyển cùng bước $1/n$ làm thông tin lan rất chậm (Ví dụ 05.12).

**Kiểm tra lại.** Trong Tình huống 05.1, nơi lượt dài hàng trăm bước và phần thưởng lớn ở cuối, TD(0) với $\alpha=0{,}5$ cho $J=2101$, lớn hơn $1627$ của Monte Carlo, cho thấy lựa chọn theo yêu cầu cập nhật không bảo đảm sai số nhỏ hơn.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Sutton, R. S. và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. §2.4–2.5, trang 30–33: Mục 1.2, 2.3–2.4, 4.4. §3.3–3.4, trang 54–57: Mục 2.1. §5.1, trang 92–93: Mục 2.2–2.6. §6.1, trang 119–121: Mục 3, Bài tập 05.14. §6.2, trang 124–125: Mục 4.4. §6.3, trang 126–128: Mục 5. Chú dẫn chương 5, trang 116, và chương 6, trang 139: nguồn của các chứng minh hội tụ.
- Chứng minh hội tụ và phân tích các quy tắc lần ghé: Singh và Sutton (1996), *Machine Learning* 22(1–3), trang 123–158, cho Mục 2.6; Dayan (1992), *Machine Learning* 8(3), trang 341–362, Jaakkola, Jordan và Singh (1994), *Neural Computation* 6, trang 1185–1201, và Tsitsiklis (1994), *Machine Learning* 16(3), trang 185–202, cho Định lý 05.30; Tsitsiklis và Van Roy (1997), *IEEE Transactions on Automatic Control* 42(5), trang 674–690, cho TD trên ô gộp (Nhận xét 05.31, Bài 07).
- Bertsekas, D. P. và Tsitsiklis, J. N. (1996), *Neuro-Dynamic Programming*, Athena Scientific, chương 2 và 4–5: chính sách kết thúc hầu chắc chắn, xấp xỉ ngẫu nhiên, Monte Carlo và TD trên bảng tra; cho Bổ đề 05.5, Mệnh đề 05.34 với $\gamma=1$ và ý tưởng chứng minh của Định lý 05.30.
- Bài giảng gốc (2025–2026), *Dự đoán phi mô hình*, trang 15–33: bài toán dự đoán (trang 15–16), Monte Carlo (trang 17–23), TD(0) (trang 24–25), độ chệch và phương sai (trang 26–28, 30–31), hai lượt trên dãy bốn ô (trang 29), chuyển tiếp (trang 32–33). Bài tập tuần 5 (2025–2026): bài 2 cho Bài tập 05.1, bài 4 cho Bài tập 05.15, bài 7 cho các Ví dụ 05.5, 05.9, 05.10; tiền đề tuyệt đối của bài 4 được thay bằng phát biểu có điều kiện.
- Notebook thực hành Bài 05, *Dự đoán Monte Carlo và TD(0) trên Lunar Lander*, gymnasium 1.3.0: các đoạn "Trong thực hành", Ví dụ 05.11, 05.12, Tình huống 05.1. Ghi chú Bài 03 (Mục 1–4) và Bài 04 (Mục 1) là tiên quyết trực tiếp.
- **Bài tập.** [Bài tập Bài 05](material-viewer.html?doc=materials/lec-05/exercises.md&deck=lecture-05-du-doan-phi-mo-hinh.html), bộ bài giao chính thức ở ba mức: Bài tập 05.8, 05.11, 05.12 trùng các bài trong thân chương, Bài tập 05.16–05.28 là bài mới; bảng đầu tệp xếp từng bài theo mạch của bài học, mạch 2–5 ứng với Mục 2–5.

<!-- note-topic-id: lec-05-topic-23 -->
Bài tập 05.14 cho thấy, khi bảng giữ cố định trong một lượt, sai số của mục tiêu Monte Carlo là tổng chiết khấu các sai số TD dọc lượt; TD(0) chỉ dùng sai số đầu tiên. Sutton và Barto (2018, §7.1, trang 142–145) xây dựng các mục tiêu trung gian dùng $n$ phần thưởng rồi bootstrap từ $V(S_{t+n})$; nhiệm vụ 5 của notebook thực hành cho một khung so sánh $n\in\{1,4,16,64\}$.
