# Bài 05: Dự đoán phi mô hình

Monte Carlo (MC) và sai phân thời gian (TD) ước lượng giá trị của một chính sách cố định từ dữ liệu tương tác. Bài học xây dựng hai cách cập nhật, thực hiện chúng trên cùng các lượt quan sát và xác định điều kiện để so sánh kết quả.

Kiến thức tiên quyết gồm quá trình quyết định Markov (MDP), chính sách, giá trị trạng thái, kỳ vọng có điều kiện và phương trình Bellman kỳ vọng. Sau bài học, người học có thể tính lợi tức, chọn mẫu MC, thực hiện TD(0) dạng bảng và giải thích kết luận theo dữ liệu, bước học cùng tiêu chuẩn đánh giá.

## Bài toán dự đoán từ dữ liệu

<!-- note-topic-id: lec-05-topic-01 -->
### Dữ liệu tương tác và giá trị cần dự đoán

Đánh giá chính sách bằng quy hoạch động cần mô hình chuyển trạng thái và phần thưởng kỳ vọng. Khi mô hình chưa biết, tác tử vẫn có thể thực hiện chính sách và ghi lại các kết quả đã xảy ra. Một mẫu chuyển có dạng

$$(S_t,A_t,R_{t+1},S_{t+1}),\qquad A_t\sim\pi(\cdot\mid S_t).$$

Ở đây, $S_t$ là trạng thái hiện tại, $A_t$ là hành động, $R_{t+1}$ là phần thưởng trên chuyển từ thời điểm $t$ đến $t+1$, còn $S_{t+1}$ là trạng thái sau chuyển. Mẫu có đầy đủ sau khi chuyển đã xảy ra. Trong phạm vi bài, trạng thái được quan sát đầy đủ và chứa đủ thông tin Markov; một quan sát bất kỳ chưa chắc có tính chất này.

Chính sách Markov $\pi$ được giữ cố định trong môi trường Markov dừng. Dữ liệu được sinh theo chính sách đang đánh giá. Tập $\mathcal S$ gồm hữu hạn trạng thái không kết thúc; $\mathcal S^+$ bổ sung các trạng thái kết thúc. Đối tượng cần ước lượng là

$$v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s],$$

trong đó $G_t$ là tổng phần thưởng chiết khấu sau thời điểm $t$, gọi ngắn là **lợi tức**. $v_\pi$ là giá trị thật; $V$ là bảng ước lượng. Kỳ vọng lấy theo chính sách $\pi$ và động lực môi trường, với điều kiện trạng thái hiện tại bằng $s$.

Giá trị tiếp nối ở trạng thái kết thúc bằng $0$. Phần thưởng nhận trên chuyển vào trạng thái ấy vẫn được tính. Dừng thu thập do hết ngân sách không tự biến một trạng thái thành trạng thái kết thúc. Các quy trình dự đoán trong bài nhận dữ liệu tương tác, không đòi hỏi mô hình chuyển và phần thưởng kỳ vọng làm đầu vào.

::: exercise Câu hỏi:
Chính sách luôn chọn sang phải. Quan sát một chuyển từ $S$ sang $X$ có thưởng $0$, nhưng chưa biết xác suất thực sự đi theo từng hướng. Xác định bốn thành phần của mẫu, đại lượng cần ước lượng và thông tin còn thiếu để đánh giá bằng quy hoạch động.
:::

::: hint
Phân biệt một kết quả đã xảy ra với phân phối của mọi kết quả có thể xảy ra. Chính sách được giữ cố định.
:::

::: solution
Mẫu là $(S,a,0,X)$, với $a$ là hành động sang phải. Cần ước lượng $v_\pi(s)$ tại các trạng thái quan tâm. Quy hoạch động cần mô hình chuyển và phần thưởng kỳ vọng; mẫu này chỉ cung cấp một kết quả. Phân phối chung $p(s',r\mid s,a)$ cũng đủ để tính kỳ vọng, nhưng toàn bộ phân phối phần thưởng không phải đầu vào tối thiểu. Thưởng $0$ trong một chuyển không xác định kỳ vọng lợi tức dài hạn. Dự đoán từ mẫu còn phụ thuộc độ phủ dữ liệu và các điều kiện của phương pháp ước lượng.
:::

Nguồn: bài giảng gốc, tr.15–16; Bài tập tuần 5, bài 2; Sutton–Barto, §5.1, tr.92.

## Dự đoán Monte Carlo

<!-- note-topic-id: lec-05-topic-02 -->
### Lượt kết thúc và lợi tức

Xét chuỗi $L,S,X,G$. Chính sách luôn chọn sang phải; môi trường đưa tác tử sang phải với xác suất $0.8$ và sang trái với xác suất $0.2$. Chuyển vào $L$ nhận thưởng $-1$, chuyển vào $G$ nhận thưởng $+1$, các chuyển còn lại nhận $0$. Hai trạng thái $L,G$ kết thúc; giá trị tiếp nối của chúng bằng $0$. Ký hiệu $X$ thay cho ô dấu chấm trong nguồn.

![Chuỗi L, S, X, G với xác suất đi phải 0.8, đi trái 0.2 và phần thưởng trên chuyển vào hai trạng thái kết thúc.](img/lec-05/short-walk.svg)

Với $\gamma=1$, hai lượt quan sát là

$$e_1:S\to X\to S\to X\to G,\qquad (R_1,R_2,R_3,R_4)=(0,0,0,1),$$
$$e_2:S\to X\to S\to L,\qquad (R_1,R_2,R_3)=(0,0,-1).$$

Mỗi lần ghé $S$ hoặc $X$ trong $e_1$ có tổng thưởng còn lại bằng $1$; trong $e_2$ tổng ấy bằng $-1$. Các giá trị bằng nhau trong từng lượt do $\gamma=1$ và chỉ có thưởng cuối lượt, không phải tính chất chung của mọi quỹ đạo.

![Lượt e1 có bốn chuyển, đi qua S và X hai lần trước khi nhận thưởng 1 tại chuyển vào G.](img/lec-05/episode-one.svg)

![Lượt e2 đi qua S, X, S rồi nhận thưởng âm 1 trên chuyển vào L.](img/lec-05/episode-two.svg)

Với lượt kết thúc tại thời điểm $T$, lợi tức được định nghĩa bởi

$$G_t=\sum_{k=t}^{T-1}\gamma^{k-t}R_{k+1},\qquad G_T=0,\qquad 0\le\gamma\le1.$$

Tách phần thưởng đầu tiên khỏi tổng cho

$$G_t=R_{t+1}+\gamma G_{t+1}.$$

Thưởng nhận ngay $R_{t+1}$ có hệ số $1$. Trong $e_1$, $T=4$, nên $G_0=\gamma^3$ và $G_3=1$. Đẳng thức truy hồi cho phép tính các lợi tức theo chiều ngược từ cuối lượt.

MC dùng lợi tức đầy đủ nên cần lượt kết thúc. Trong chuỗi hữu hạn này, hai trạng thái biên hấp thụ và thời gian kết thúc có kỳ vọng hữu hạn. Riêng điều kiện $\gamma=1$ không bảo đảm một tổng thưởng hữu hạn trong bài toán bất kỳ; khi dùng kỳ vọng hoặc phương sai cần các điều kiện khả tích tương ứng.

::: exercise Câu hỏi:
Phần thưởng $+1$ là $R_{t+4}$ và $\gamma=0.99$. Tính đóng góp của phần thưởng này vào $G_t$.
:::

::: hint
Phần thưởng ở chuyển thứ $m$ sau trạng thái hiện tại mang hệ số $\gamma^{m-1}$.
:::

::: solution
Đóng góp là $\gamma^3\cdot1=0.99^3=0.970299$. Phần thưởng đầu tiên sau thời điểm $t$ mang chỉ số $t+1$ nhưng chưa bị chiết khấu, nên số mũ nhỏ hơn số thứ tự chuyển một đơn vị.
:::

Nguồn: bài giảng gốc, tr.17, 19–22; Bài tập tuần 5, bài 7; Sutton–Barto, §5.1.

<!-- note-topic-id: lec-05-topic-04 -->
### Ước lượng từ hai lượt hoàn chỉnh

Quy tắc **lần ghé đầu tiên** chọn thời điểm sớm nhất mà một trạng thái xuất hiện trong từng lượt. Với hai lượt $e_1,e_2$, mỗi trạng thái $S,X$ nhận một mẫu $+1$ từ $e_1$ và một mẫu $-1$ từ $e_2$. Trung bình các mẫu cho ước lượng MC:

| Lượt đã xử lý | Mẫu mới tại S và X | Số mẫu mỗi trạng thái | $(V(S),V(X))$ |
|---|---|---|---|
| $e_1$ | $(1,1)$ | 1 | $(1,1)$ |
| $e_1,e_2$ | $(-1,-1)$ | 2 | $(0,0)$ |

Tổng quát, gọi $g_i(s)$ là mẫu lợi tức thứ $i$ được chọn tại trạng thái $s$. Sau $n$ mẫu của chính trạng thái đó,

$$V_n(s)=\frac1n\sum_{i=1}^n g_i(s).$$

Chỉ số $n$ đếm mẫu tại $s$, không phải thời điểm tương tác toàn cục. Khi chưa có mẫu, bảng vẫn chứa giá trị khởi tạo. Hai lượt cho trung bình bằng $0$ không xác định giá trị thật của chính sách; đây là một ước lượng hữu hạn mẫu.

Nếu chọn quy tắc **mọi lần ghé**, mỗi thời điểm có trạng thái $s$ đều cung cấp một mẫu. Khi đó, $X$ có dãy $(1,1,-1)$ và trung bình $1/3$. Quy tắc lựa chọn mẫu phải được xác định trước khi tính trung bình.

::: exercise Câu hỏi:
Dùng lần ghé đầu tiên và trung bình mẫu trên $e_1,e_2$. Tính $V(S),V(X)$ sau riêng $e_1$, rồi sau cả hai lượt. Giải thích nguyên nhân hai giá trị cuối bằng $0$.
:::

::: hint
Mỗi trạng thái đóng góp một mẫu mỗi lượt. Hai mẫu được chọn có trọng số bằng nhau.
:::

::: solution
Sau $e_1$, $V(S)=V(X)=1$. Sau $e_2$, mỗi giá trị bằng $(1-1)/2=0$. Kết quả do trung bình hai lợi tức đối dấu với cùng trọng số; nó không phải kết luận rằng kỳ vọng lợi tức của môi trường bằng $0$.
:::

Nguồn: bài giảng gốc, tr.18, 20–22; Sutton–Barto, §5.1, tr.92–93.

<!-- note-topic-id: lec-05-topic-06 -->
### Quy tắc lần ghé và bước học

Trong $e_1$, $S$ xuất hiện ở thời điểm $0,2$, còn $X$ ở thời điểm $1,3$. Trong $e_2$, $S$ xuất hiện hai lần, $X$ một lần. Hai cách chọn mẫu cho

| Trạng thái | Lần ghé đầu tiên | Mọi lần ghé |
|---|---|---|
| $S$ | $(1,-1)$, trung bình $0$ | $(1,1,-1,-1)$, trung bình $0$ |
| $X$ | $(1,-1)$, trung bình $0$ | $(1,1,-1)$, trung bình $1/3$ |

Các lợi tức trong cùng lượt có thể phụ thuộc nhau vì dùng chung phần đuôi. Số mẫu được chọn không đồng nhất với số quan sát độc lập.

Đối với $X$ theo mọi lần ghé, hai mẫu đầu $(1,1)$ có trung bình $1$. Khi thêm mẫu $-1$, trung bình mới là

$$\frac{2\cdot1-1}{3}=1+\frac13(-1-1)=\frac13.$$

Tổng của $n-1$ mẫu cũ bằng $(n-1)V_{n-1}(s)$. Vì thế,

$$V_n(s)=\frac{(n-1)V_{n-1}(s)+g_n(s)}n
=V_{n-1}(s)+\frac1n[g_n(s)-V_{n-1}(s)].$$

Chỉ cần giữ trung bình và bộ đếm $N(s)$ của từng trạng thái để tổng hợp các mẫu đã chọn. Bộ đếm được tăng trước khi dùng bước học $1/N(s)$. Mẫu đầu tiên có bước học $1$, nên loại hoàn toàn ảnh hưởng khởi tạo trong trung bình mẫu.

Thay $1/n$ bằng hằng số $\alpha$ tạo quy tắc khác. Với mẫu $(1,-1)$, khởi tạo $0$ và $\alpha=0.5$, hai cập nhật là

$$0+0.5(1-0)=0.5,\qquad 0.5+0.5(-1-0.5)=-0.25.$$

Quy tắc tổng quát và các trọng số tương ứng là

$$V_n(s)=(1-\alpha)V_{n-1}(s)+\alpha g_n(s),\qquad 0<\alpha\le1,$$
$$V_n(s)=(1-\alpha)^nV_0(s)+\sum_{i=1}^n\alpha(1-\alpha)^{n-i}g_i(s).$$

Với $0<\alpha<1$, mẫu gần đây có trọng số lớn hơn và ảnh hưởng khởi tạo giảm dần. Với $\alpha=1$, $V_n(s)=g_n(s)$ từ mẫu đầu tiên: ước lượng chỉ giữ mẫu mới nhất và không còn ảnh hưởng khởi tạo. Đây không còn là trung bình số học nói chung. Khi các lợi tức khác nhau, thứ tự xử lý có thể đổi kết quả do các trọng số không bằng nhau. Trong từng lượt cụ thể đang xét, lợi tức của cùng trạng thái đều bằng nhau, nên đảo thứ tự các mẫu trong lượt ấy không đổi kết quả.

Quy tắc lần ghé xác định **mẫu nào được dùng**; bước học xác định **cách kết hợp mẫu**. Hai lựa chọn độc lập tạo bốn cấu hình. Khởi tạo riêng mỗi cấu hình từ $V=0$:

| Cấu hình | Sau $e_1$: $(V(S),V(X))$ | Sau $e_2$ |
|---|---|---|
| Lần ghé đầu tiên, trung bình mẫu | $(1,1)$ | $(0,0)$ |
| Mọi lần ghé, trung bình mẫu | $(1,1)$ | $(0,1/3)$ |
| Lần ghé đầu tiên, $\alpha=0.5$ | $(0.5,0.5)$ | $(-0.25,-0.25)$ |
| Mọi lần ghé, $\alpha=0.5$ | $(0.75,0.75)$ | $(-0.5625,-0.125)$ |

Ở cấu hình cuối, $e_2$ cập nhật $S$ hai lần: $0.75\to-0.125\to-0.5625$; $X$ được cập nhật một lần: $0.75\to-0.125$.

::: exercise Câu hỏi:
Tại $X$, lập dãy lợi tức theo lần ghé đầu tiên và mọi lần ghé từ $e_1,e_2$, rồi tính hai trung bình. Với lần ghé đầu tiên, khởi tạo $0$ và $\alpha=0.5$, tính $V(X)$ sau mỗi lượt.
:::

::: hint
Đếm hai lần xuất hiện của $X$ trong $e_1$ và một lần trong $e_2$. Giữ nguyên dãy mẫu khi chỉ thay bước học.
:::

::: solution
Lần ghé đầu tiên chọn $(1,-1)$, cho trung bình $0$. Mọi lần ghé chọn $(1,1,-1)$, cho trung bình $1/3$. Với lần ghé đầu tiên và bước học $0.5$, kết quả lần lượt là $0.5$ và $-0.25$. Khác biệt giữa $0$ và $-0.25$ do trọng số mẫu và khởi tạo, dù dãy lợi tức được chọn vẫn là $(1,-1)$.
:::

Nguồn: Sutton–Barto, §2.4–2.5, tr.30–33; §5.1, tr.92–93; bài giảng gốc, tr.18, 20–23; Bài tập tuần 5, bài 5 và 7.

<!-- note-topic-id: lec-05-topic-03 -->
### Quy trình dự đoán Monte Carlo

Đầu vào gồm chính sách $\pi$, hệ số $\gamma$, ngân sách $M$ lượt, quy tắc lần ghé và lịch bước học $\alpha_n(s)$. Đầu ra là bảng $V$ ước lượng $v_\pi$.

1. Khởi tạo $V(s)$ tùy ý, $N(s)=0$ với $s\in\mathcal S$; giữ giá trị trạng thái kết thúc bằng $0$.
2. Sinh một lượt $S_0,A_0,R_1,\ldots,S_T$ theo $\pi$ đến khi kết thúc thật.
3. Đặt $G_T=0$; tính $G_t=R_{t+1}+\gamma G_{t+1}$ với $t=T-1,\ldots,0$.
4. Đặt tập đã ghé $H=\varnothing$; duyệt xuôi $t=0,\ldots,T-1$, đặt $s=S_t$.
5. Nếu dùng mọi lần ghé, hoặc nếu dùng lần ghé đầu tiên và $s\notin H$, thực hiện

$$N(s)\leftarrow N(s)+1,$$
$$V(s)\leftarrow V(s)+\alpha_{N(s)}(s)[G_t-V(s)],\qquad H\leftarrow H\cup\{s\}.$$

6. Lặp lại từ bước 2 đến đủ $M$ lượt, rồi trả về $V$.

Với trung bình mẫu, chọn $\alpha_{N(s)}(s)=1/N(s)$; với bước học hằng, chọn cùng một $\alpha$ ở mọi lần cập nhật. Tập $H$ được đặt lại ở đầu mỗi lượt. Trạng thái kết thúc không được cập nhật.

Duyệt lùi ở bước 3 chỉ để tính lợi tức. Chọn lần ghé diễn ra theo chiều thời gian ở bước 4–5. Nếu vừa duyệt lùi vừa loại trạng thái đã gặp, quy tắc sẽ chọn lần ghé cuối cùng theo thời gian.

Quy trình giữ một lượt để tính lợi tức, dùng $O(|\mathcal S|+T)$ bộ nhớ và $O(T)$ công việc cho lượt dài $T$, với truy cập bảng và tập đánh dấu trong thời gian hằng. Không cần lưu mọi lợi tức của các lượt trước. Kết thúc một lượt khác với kết thúc toàn bộ ngân sách học.

::: exercise Câu hỏi:
Trong $e_1:S\to X\to S\to X\to G$, mỗi trạng thái $S,X$ cung cấp bao nhiêu mẫu theo lần ghé đầu tiên và mọi lần ghé? Nêu giả thiết cho phép dùng lập luận các mẫu độc lập giữa những lượt khác nhau.
:::

::: hint
Lần ghé đầu tiên được xác định riêng trong từng lượt. Phân biệt khởi động lại lượt với nhiều lần xuất hiện trong cùng lượt.
:::

::: solution
Mỗi trạng thái cung cấp một mẫu theo lần ghé đầu tiên và hai mẫu theo mọi lần ghé. Nếu các lượt được khởi động độc lập dưới cùng chính sách và môi trường dừng, các lợi tức lần ghé đầu tiên của trạng thái đang xét tạo khung mẫu độc lập cùng phân phối. Các lợi tức thuộc cùng lượt có thể phụ thuộc nhau. Lập luận độc lập này là một cách đủ để áp dụng luật số lớn; nó không phải điều kiện để mọi trung bình có ý nghĩa.
:::

Nguồn: Sutton–Barto, §5.1, tr.92–93; quy trình tách tính lợi tức và chọn mẫu theo thời gian.

## Dự đoán sai phân thời gian TD(0)

<!-- note-topic-id: lec-05-topic-07 -->
### Mục tiêu một bước và sai số TD

Sau tiền tố $S\to X$ có thưởng $0$, chưa biết lượt sẽ kết thúc tại $L$ hay $G$. MC chưa có lợi tức đầy đủ. Bảng hiện tại chứa một dự đoán cho phần còn lại bắt đầu ở $X$.

![MC dùng quỹ đạo đến kết thúc; TD dùng một chuyển đã quan sát và ước lượng tại trạng thái kế tiếp.](img/lec-05/mc-td-targets.svg)

Cho $V(S)=0$, $V(X)=0.5$, $\gamma=1$, $\alpha=0.5$ và chuyển $S\to X$ nhận thưởng $0$. Mục tiêu dự đoán là $0+1\cdot0.5=0.5$. Sai lệch so với giá trị cũ tại $S$ là $0.5$, nên giá trị mới tại $S$ bằng $0+0.5\cdot0.5=0.25$; $V(X)$ giữ nguyên.

Sai phân thời gian thay phần lợi tức chưa quan sát bằng một ước lượng hiện có. Cơ chế này được gọi là bootstrap trong tài liệu. Gọi $V_t$ là toàn bộ bảng trước cập nhật của chuyển $t\to t+1$. Khi đã quan sát $R_{t+1},S_{t+1}$,

$$Y_t=R_{t+1}+\gamma V_t(S_{t+1}),\qquad \delta_t=Y_t-V_t(S_t),$$
$$V_{t+1}(S_t)=V_t(S_t)+\alpha_n(S_t)\delta_t.$$

$Y_t$ là mục tiêu TD, $\delta_t$ là sai số TD, còn $n$ là số thứ tự cập nhật của riêng $S_t$. Mọi phần tử khác giữ nguyên. Cả hai phép đọc ở vế phải dùng cùng $V_t$. Sai số TD nói chung khác lỗi thật $v_\pi(S_t)-V_t(S_t)$ vì mục tiêu dùng một chuyển ngẫu nhiên và một bảng ước lượng.

::: exercise Câu hỏi:
Cho $V(S)=0,V(X)=0.5$, $\gamma=1$, $\alpha=0.5$. Với chuyển $S\to X$ nhận thưởng $0$, tính mục tiêu, sai số TD, giá trị mới tại $S$ và giá trị tại $X$ sau cập nhật.
:::

::: hint
Tính mục tiêu từ thưởng và giá trị trạng thái sau, sau đó lấy mục tiêu trừ giá trị cũ. Chỉ sửa phần tử của trạng thái hiện tại.
:::

::: solution
$Y=0.5$, $\delta=0.5-0=0.5$, $V(S)=0+0.5(0.5)=0.25$. Giá trị $V(X)=0.5$ giữ nguyên. Bảng ban đầu là dữ kiện của phép tính; không cần biết mô hình để thực hiện bước này.
:::

Nguồn: bài giảng gốc, tr.24–25; Sutton–Barto, §6.1, tr.119–121.

<!-- note-topic-id: lec-05-topic-08 -->
### Quy trình TD(0), kết thúc và tự chuyển

Đầu vào gồm $\pi,\gamma$, lịch bước học $\alpha_n(s)$ và ngân sách $B$ chuyển. Khởi tạo $V$, $N(s)=0$ tại các trạng thái không kết thúc; giá trị trạng thái kết thúc luôn bằng $0$.

1. Bắt đầu lượt ở trạng thái không kết thúc theo cơ chế khởi tạo của bài toán.
2. Khi còn ngân sách, chọn hành động theo $\pi$, quan sát $R_{t+1},S_{t+1}$.
3. Tăng $N(S_t)$ rồi đặt $n=N(S_t)$.
4. Đọc bảng trước cập nhật để tính $Y_t=R_{t+1}+\gamma V_t(S_{t+1})$ và $\delta_t=Y_t-V_t(S_t)$.
5. Ghi $V(S_t)\leftarrow V_t(S_t)+\alpha_n(S_t)\delta_t$; giảm ngân sách một chuyển.
6. Nhận $S_{t+1}$ làm trạng thái hiện tại. Nếu đã kết thúc và còn ngân sách, bắt đầu lượt mới. Hết ngân sách thì trả về $V$.

Bảng và bộ đếm được giữ giữa các lượt. Nếu đặt lại chỉ số thời gian tương tác ở đầu lượt, $V_t$ vẫn chỉ bảng trước bước đang xét, không phải khởi tạo lại bảng. Dừng do ngân sách không cho phép tự đặt giá trị tiếp nối bằng $0$.

Ở chuyển $X\to G$ nhận thưởng $1$, mục tiêu bằng $1+\gamma V_t(G)=1$. Thưởng nhận khi đi vào $G$ được tính một lần; giá trị tương lai ở $G$ bằng $0$.

Một phép kiểm riêng cho trường hợp tự chuyển dùng $s\to s$, thưởng $0$, $\gamma=0.9$, $V_t(s)=2$ và $\alpha=0.5$. Khi đó $Y_t=1.8$, $\delta_t=-0.2$, $V_{t+1}(s)=1.9$. Hai phép đọc đều dùng giá trị cũ $2$. Trường hợp này kiểm quy tắc cập nhật, không phải một chuyển của chuỗi ngắn.

TD(0) cần $O(|\mathcal S|)$ bộ nhớ cho bảng và bộ đếm, cùng $O(1)$ phép tính cho một chuyển. Chi phí một bước không xác định số mẫu cần để đạt sai số cho trước.

::: exercise Câu hỏi:
Cho bảng ban đầu $V(S)=0.25,V(X)=0.5,V(L)=0$, $\alpha=0.5$, $\gamma=1$. Xét riêng hai trường hợp từ cùng bảng ban đầu: (a) $S\to X$ nhận thưởng $0$; (b) $S\to L$ nhận thưởng $-1$. Tính mục tiêu, sai số và giá trị mới tại $S$; xác định phần tử giữ nguyên.
:::

::: hint
Trong trường hợp (b), trạng thái sau đã kết thúc. Mỗi trường hợp bắt đầu từ $V(S)=0.25$, không dùng kết quả của trường hợp trước.
:::

::: solution
(a) $Y=0.5$, $\delta=0.25$, $V(S)=0.25+0.5(0.25)=0.375$. (b) $Y=-1$, $\delta=-1.25$, $V(S)=0.25+0.5(-1.25)=-0.375$. Trong cả hai trường hợp, $V(X)=0.5$ và $V(L)=0$ giữ nguyên.
:::

Nguồn: Sutton–Barto, §6.1, tr.120; bài giảng gốc, tr.25; Bài tập tuần 5, bài 3 và 7. Phép tự chuyển là trường hợp kiểm quy tắc đã dùng trong bài giảng.

<!-- note-topic-id: lec-05-topic-09 -->
### TD(0) trên hai lượt của chuỗi ngắn

Khởi tạo $V(S)=V(X)=0$, dùng $\alpha=0.5,\gamma=1$. Trong mỗi chuyển, mục tiêu được tính trước khi sửa bảng; chuyển tiếp theo đọc bảng vừa được sửa.

| Chuyển trong $e_1$ | Thưởng | Mục tiêu | Sai số TD | $(V(S),V(X))$ sau bước |
|---|---|---|---|---|
| $S\to X$ | 0 | 0 | 0 | $(0,0)$ |
| $X\to S$ | 0 | 0 | 0 | $(0,0)$ |
| $S\to X$ | 0 | 0 | 0 | $(0,0)$ |
| $X\to G$ | 1 | 1 | 1 | $(0,0.5)$ |

Tiếp tục lượt $e_2:S\to X\to S\to L$ từ bảng $(0,0.5)$:

| Chuyển trong $e_2$ | Thưởng | Mục tiêu | Sai số TD | $(V(S),V(X))$ sau bước |
|---|---|---|---|---|
| $S\to X$ | 0 | 0.5 | 0.5 | $(0.25,0.5)$ |
| $X\to S$ | 0 | 0.25 | −0.25 | $(0.25,0.375)$ |
| $S\to L$ | −1 | −1 | −1.25 | $(-0.375,0.375)$ |

Bước $X\to S$ dùng $V(S)=0.25$ từ bước trước. Bước cuối cho $V(S)=0.25+0.5(-1-0.25)=-0.375$.

Trên lượt đầu từ bảng $0$, TD chỉ đổi $X$ ở chuyển vào $G$; nó không quay lại sửa các trạng thái trước đó sau khi thưởng cuối được quan sát. MC cập nhật các mẫu đã chọn sau kết thúc, nên thưởng cuối có thể tác động tới cả $S$ và $X$ trong lần xử lý lượt ấy. Cập nhật sớm hơn và tác động tới nhiều trạng thái trước đó là hai đặc điểm khác nhau.

::: exercise Câu hỏi:
Giải thích ba kết quả sau $e_2$: MC lần ghé đầu tiên với trung bình mẫu cho $(0,0)$; cùng quy tắc lần ghé với $\alpha=0.5$ cho $(-0.25,-0.25)$; TD(0) với $\alpha=0.5$ cho $(-0.375,0.375)$. Mỗi phương pháp được khởi tạo riêng từ bảng $0$.
:::

::: hint
Đối chiếu mẫu được chọn, trọng số mẫu, mục tiêu cập nhật và thời điểm sửa bảng.
:::

::: solution
MC trung bình lấy hai mẫu $1,-1$ với trọng số bằng nhau. MC bước hằng dùng cùng hai mẫu nhưng còn ảnh hưởng khởi tạo và đặt trọng số khác nhau theo thời điểm. TD dùng mục tiêu một bước và sửa bảng giữa các chuyển; mục tiêu ở $X\to S$ đọc giá trị $S$ đã thay đổi. Thưởng $-1$ ở chuyển cuối trực tiếp sửa $S$, còn $X$ giữ $0.375$. Hai lượt này giải thích cơ chế, không xác định phương pháp có hiệu quả mẫu cao hơn trong mọi bài toán.
:::

Nguồn: bài giảng gốc, tr.29; Bài tập tuần 5, bài 7.

## So sánh theo dữ liệu và giả thiết

<!-- note-topic-id: lec-05-topic-05 -->
### Giá trị chuẩn của chuỗi ngắn

Các bảng đã tính là ước lượng từ hai lượt. Trong ví dụ này, mô hình được biết riêng để tính giá trị chuẩn đối chiếu:

$$v_\pi(S)=-0.2+0.8v_\pi(X),\qquad v_\pi(X)=0.8+0.2v_\pi(S).$$

Thưởng $-1$ xuất hiện khi đi từ $S$ vào $L$; thưởng $1$ xuất hiện khi đi từ $X$ vào $G$. Thay phương trình thứ hai vào phương trình đầu cho $0.84v_\pi(S)=0.44$, do đó

$$v_\pi(S)=\frac{11}{21}\approx0.524,\qquad v_\pi(X)=\frac{19}{21}\approx0.905.$$

Các giá trị này không là đầu vào của MC hoặc TD. Chúng chỉ cho phép đo sai số ước lượng trong môi trường minh họa. Dữ liệu hữu hạn có thể cho kết quả xa giá trị thật dù phép cập nhật được thực hiện đúng.

::: exercise Câu hỏi:
MC lần ghé đầu tiên với trung bình mẫu cho $V(S)=0$ sau hai lượt. Tính sai số có dấu $V(S)-v_\pi(S)$. Nêu kết luận về sai số khi số lượt độc lập tăng dưới các giả thiết của luật số lớn.
:::

::: hint
Phân biệt hội tụ khi số mẫu tiến vô hạn với giảm sai số sau từng mẫu mới.
:::

::: solution
Sai số bằng $-11/21\approx-0.524$. Khi các mẫu lần ghé đầu tiên độc lập cùng phân phối, có kỳ vọng hữu hạn và số mẫu của trạng thái tăng vô hạn, trung bình hội tụ về giá trị kỳ vọng. Điều đó không bảo đảm sai số giảm sau mọi lượt mới. Trong khung có phương sai hữu hạn, luật số lớn áp dụng trực tiếp.
:::

Nguồn: bài giảng gốc, tr.19; hệ Bellman tính lại từ dữ kiện môi trường.

<!-- note-topic-id: lec-05-topic-12 -->
### Chuỗi dài và số mũ chiết khấu

Xét chuỗi $L,x_1,S,x_3,x_4,x_5,G$ với cùng chính sách và xác suất đi phải/trái $0.8/0.2$. Chỉ chuyển vào $L$ hoặc $G$ nhận thưởng $-1$ hoặc $1$; $\gamma=0.99$ và giá trị tiếp nối ở hai trạng thái kết thúc bằng $0$.

![Chuỗi bảy vị trí bắt đầu ở S, cách L hai chuyển và cách G bốn chuyển ngắn nhất.](img/lec-05/long-walk.svg)

Từ $S$, đường $S,x_3,x_4,x_5,G$ có thưởng $(0,0,0,1)$, nên $G_0=0.99^3=0.970299$. Đường $S,x_1,L$ có thưởng $(0,-1)$, nên $G_0=-0.99$.

![Hai đường từ S: bốn chuyển đến G với thưởng cuối 1 và hai chuyển đến L với thưởng cuối âm 1.](img/lec-05/long-returns.svg)

Giá trị chuẩn từ hệ Bellman là $v_\pi(S)\approx0.829218798$ và $v_\pi(x_5)\approx0.992155697$. Hai lợi tức từ $S$ vừa tính khác kỳ vọng $v_\pi(S)$. So sánh mục tiêu cần phân tích riêng kỳ vọng và biến thiên quanh kỳ vọng. Hai đường minh họa biến thiên của lợi tức; chúng chưa xác định phương sai tổng thể hoặc tốc độ học của một thuật toán.

::: exercise Câu hỏi:
Tính lợi tức từ $S$ trên hai đường ngắn nhất đến $G$ và $L$, với $\gamma=0.99$. Giải thích số mũ đi kèm mỗi phần thưởng cuối.
:::

::: hint
Phần thưởng cuối ở đường đến $G$ là $R_4$; ở đường đến $L$ là $R_2$.
:::

::: solution
Đường đến $G$ cho $G_0=\gamma^3=0.970299$; đường đến $L$ cho $G_0=-\gamma=-0.99$. Thưởng ở chuyển thứ $m$ có hệ số $\gamma^{m-1}$. Hai số mũ $4$ và $2$ trong trang nguồn được hiệu chỉnh thành $3$ và $1$ theo định nghĩa lợi tức.
:::

Nguồn: bài giảng gốc, tr.30–31.

<!-- note-topic-id: lec-05-topic-10 -->
### Kỳ vọng của mục tiêu cập nhật

Một mục tiêu quan sát và kỳ vọng của mục tiêu là các đại lượng khác nhau. Trong chuỗi ngắn, giữ $\gamma=1$, $V(X)=0.5$ và $V(L)=0$. Từ $S$, mục tiêu $Y=R_{t+1}+\gamma V(S_{t+1})$ nhận giá trị $-1$ với xác suất $0.2$ khi chuyển vào $L$, hoặc $0.5$ với xác suất $0.8$ khi chuyển đến $X$. Vì thế,

$$\mathbb E_\pi[Y\mid S_t=S]=0.2(-1)+0.8(0.5)=\frac15.$$

Giá trị chuẩn của chuỗi ngắn là $v_\pi(S)=11/21$, nên sai lệch kỳ vọng bằng

$$\frac15-\frac{11}{21}=-\frac{34}{105}.$$

Bảng $V$ cố định vẫn tạo các mục tiêu khác nhau qua trạng thái kế tiếp ngẫu nhiên. Dữ kiện ở đây là mô hình chuỗi ngắn và bảng đã dùng trong phép cập nhật một bước; không dùng hai đường của chuỗi dài để ước lượng phân phối.

Tổng quát, giữ bảng $V$ cố định và lấy một mẫu mới theo chính sách $\pi$. Theo định nghĩa giá trị và Bellman kỳ vọng,

$$\mathbb E_\pi[G_t\mid S_t=s]=v_\pi(s),$$
$$v_\pi(s)=\mathbb E_\pi[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t=s].$$

Với $Y=R_{t+1}+\gamma V(S_{t+1})$, trừ đẳng thức thứ hai khỏi kỳ vọng của $Y$ cho

$$\mathbb E_\pi[Y\mid S_t=s]-v_\pi(s)
=\gamma\mathbb E_\pi[V(S_{t+1})-v_\pi(S_{t+1})\mid S_t=s].$$

Sai lệch kỳ vọng của mục tiêu TD phụ thuộc sai số giá trị tại các trạng thái kế tiếp. Nó bằng $0$ nếu các giá trị tiếp nối đều đúng; sai số cũng có thể bù trừ trong kỳ vọng. Vì vậy, mục tiêu TD **có thể** chệch, không bắt buộc luôn chệch. Phát biểu về mục tiêu này không tự động xác định độ chệch của bảng ước lượng sau nhiều cập nhật.

Để viết gọn, toán tử Bellman kỳ vọng theo quy ước Bài 04 là

$$(T_\pi V)(s)=\mathbb E_\pi[R_{t+1}+\gamma V(S_{t+1})\mid S_t=s].$$

$T_\pi$ là toán tử; $T$ không có chỉ số vẫn chỉ thời điểm kết thúc một lượt. Với bảng $V_t$ trước bước cập nhật,

$$\mathbb E_\pi[\delta_t\mid S_t=s,V_t]=(T_\pi V_t)(s)-V_t(s).$$

Vế phải là sai số Bellman kỳ vọng. Tính chất này dựa trên dữ liệu theo chính sách và giả thiết Markov; nó không thay thế các điều kiện hội tụ của cập nhật ngẫu nhiên.

::: exercise Câu hỏi:
Phân biệt $\delta_t$ của một chuyển với $(T_\pi V_t)(s)-V_t(s)$. Xác định quan hệ kỳ vọng giữa chúng và giải thích vì sao dấu của một mẫu chưa quyết định dấu sai số kỳ vọng.
:::

::: hint
Giữ bảng $V_t$ cố định, lấy kỳ vọng theo phần thưởng và trạng thái kế tiếp khi $S_t=s$.
:::

::: solution
$\delta_t=R_{t+1}+\gamma V_t(S_{t+1})-V_t(S_t)$ phụ thuộc chuyển được lấy mẫu. Kỳ vọng có điều kiện của nó bằng $(T_\pi V_t)(s)-V_t(s)$. Một mẫu có thể nằm ở hai phía của kỳ vọng; dấu của một sai số TD đơn lẻ không xác định dấu của sai số Bellman kỳ vọng hoặc dấu lỗi thật $v_\pi(s)-V_t(s)$.
:::

Nguồn: Sutton–Barto, §6.1, tr.120–121; hệ quả trực tiếp của Bellman kỳ vọng; bài giảng gốc, tr.25–27 được giới hạn theo điều kiện.

<!-- note-topic-id: lec-05-topic-13 -->
### Phương sai của mục tiêu quan sát và mục tiêu lý tưởng

MC dùng phần thưởng và chuyển trạng thái đến cuối lượt. TD dùng phần thưởng đầu và giá trị ở trạng thái kế tiếp. Dù bảng $V$ được giữ cố định, $V(S_{t+1})$ vẫn ngẫu nhiên vì trạng thái kế tiếp chưa xác định trước khi lấy mẫu.

![MC phụ thuộc phần còn lại của quỹ đạo; TD vẫn ngẫu nhiên qua phần thưởng đầu và trạng thái kế tiếp dù bảng giá trị được giữ cố định.](img/lec-05/target-randomness.svg)

Một kết quả phương sai xác định được cho mục tiêu lý tưởng

$$Y^*=R_{t+1}+\gamma v_\pi(S_{t+1}).$$

Giả sử môi trường Markov dừng, chính sách Markov cố định và $G_t$ có mômen bậc hai hữu hạn. Đặt $\mathcal F_1=\sigma(R_{t+1},S_{t+1})$, tức thông tin về thưởng và trạng thái của chuyển đầu. Khi xét có điều kiện $S_t=s$, tính Markov cho

$$Y^*=\mathbb E_\pi[G_t\mid S_t=s,\mathcal F_1].$$

Luật phương sai toàn phần suy ra

$$\operatorname{Var}_\pi(G_t\mid S_t=s)
=\operatorname{Var}_\pi(Y^*\mid S_t=s)
+\mathbb E_\pi[\operatorname{Var}_\pi(G_t\mid S_t=s,\mathcal F_1)\mid S_t=s].$$

Hạng cuối không âm, nên

$$\operatorname{Var}_\pi(Y^*\mid S_t=s)\le\operatorname{Var}_\pi(G_t\mid S_t=s).$$

Thay $v_\pi$ bằng một bảng học được $V$ làm mất đẳng thức kỳ vọng có điều kiện ở trên. Không có thứ tự phương sai phổ quát cho mọi mục tiêu TD thực tế. Phương sai mục tiêu cũng không tự xác định sai số của cả thuật toán, vốn còn phụ thuộc bước học, khởi tạo và dữ liệu.

::: exercise Câu hỏi:
Xác định các nguồn ngẫu nhiên trong $G_t$ và trong $R_{t+1}+\gamma V(S_{t+1})$ khi bảng $V$ cố định. Nêu điều kiện và đối tượng của bất đẳng thức phương sai đã chứng minh; giải thích vì sao không áp dụng trực tiếp cho mọi bảng $V$.
:::

::: hint
Phân biệt một hàm được giữ cố định với đầu vào ngẫu nhiên của hàm. Kiểm tra vị trí dùng $v_\pi$ trong đẳng thức kỳ vọng có điều kiện.
:::

::: solution
$G_t$ phụ thuộc các phần thưởng, hành động theo chính sách và chuyển trạng thái còn lại trong lượt. Mục tiêu TD vẫn phụ thuộc phần thưởng đầu và trạng thái kế tiếp ngẫu nhiên. Với giả thiết Markov và mômen bậc hai hữu hạn, mục tiêu lý tưởng dùng $v_\pi$ là kỳ vọng có điều kiện của lợi tức, nên có phương sai không lớn hơn. Mục tiêu dùng $V$ bất kỳ không nhất thiết là kỳ vọng có điều kiện đó; sai số tại các trạng thái kế tiếp có thể thay đổi cả kỳ vọng và phương sai. Do đó không kết luận TD luôn có phương sai thấp hơn MC.
:::

Nguồn: Sutton–Barto, §6.2, tr.124; cơ chế so sánh ở bài giảng gốc, tr.26–28 được diễn giải có điều kiện. Bất đẳng thức suy ra từ luật phương sai toàn phần.

<!-- note-topic-id: lec-05-topic-11 -->
### Điều kiện hội tụ khi tiếp tục nhận mẫu

Với MC lần ghé đầu tiên, các lượt khởi động độc lập dưới cùng chính sách tạo mẫu lợi tức độc lập cùng phân phối cho trạng thái đang xét. Trung bình của một số mẫu cố định là không chệch khi các mẫu có cùng kỳ vọng $v_\pi(s)$. Trong khung có phương sai hữu hạn, khi số mẫu của $s$ tăng vô hạn, trung bình hội tụ về $v_\pi(s)$ theo luật số lớn. Phương sai hữu hạn là điều kiện đủ đang dùng, không phải điều kiện cần của mọi dạng luật số lớn.

Mẫu mọi lần ghé có thể phụ thuộc trong cùng lượt. Trong quá trình phần thưởng Markov hữu hạn do chính sách Markov dừng, cố định tạo ra, giả sử phần thưởng bị chặn, quá trình kết thúc hầu chắc chắn từ mọi trạng thái không kết thúc đang xét, các lượt được khởi động độc lập theo cùng phân phối và trạng thái $s$ được ghé với xác suất dương. Với $0\le\gamma\le1$ và bước học $1/N(s)$, trung bình mọi lần ghé hội tụ hầu chắc chắn về $v_\pi(s)$ khi số lượt hoàn chỉnh tiến vô hạn.

Luật số lớn áp dụng theo lượt cho tổng lợi tức và số lần ghé tại $s$, rồi lấy tỷ số; không cần coi mọi lợi tức trong lượt là độc lập. Kết quả nhất quán này không bảo đảm trung bình ở số lượt hữu hạn luôn không chệch và không áp dụng nguyên văn cho bước học hằng.

Đối với TD(0) dạng bảng, xét môi trường hữu hạn Markov dừng, chính sách cố định, dữ liệu theo chính sách và phần thưởng bị chặn. Mỗi trạng thái cần ước lượng phải được cập nhật vô hạn lần. Bước học ở lần cập nhật thứ $n$ của trạng thái $s$ thỏa

$$0<\alpha_n(s)\le1,\qquad\sum_{n=1}^{\infty}\alpha_n(s)=\infty,\qquad\sum_{n=1}^{\infty}\alpha_n(s)^2<\infty.$$

Ví dụ $\alpha_n(s)=1/n$ thỏa hai điều kiện tổng. Tổng bước học phân kỳ duy trì khả năng điều chỉnh; tổng bình phương hữu hạn kiểm soát tích lũy nhiễu. Dưới các giả thiết chuẩn này, TD(0) hội tụ về $v_\pi$ với xác suất $1$ khi $0\le\gamma<1$.

Với $\gamma=1$, cần thêm cấu trúc kết thúc hợp lệ: chính sách đưa quá trình tới trạng thái kết thúc với xác suất $1$ từ mọi trạng thái đang xét; các trạng thái không kết thúc là quá độ và các lượt được khởi động lại. Trong chuỗi hữu hạn hấp thụ đang dùng, phần thưởng bị chặn cùng điều kiện này bảo đảm các mômen cần thiết. Không thể chỉ thay $\gamma$ trong lập luận của trường hợp chiết khấu.

Bộ đếm $n$ thuộc riêng từng trạng thái. Bảng theo thời gian tương tác vẫn là $V_t$; điều kiện vô hạn lần cập nhật liên hệ số đếm riêng với thời gian học. Với bước học hằng $\alpha>0$, tổng bình phương phân kỳ: bảo đảm trên không áp dụng và ước lượng có thể tiếp tục dao động trên mẫu mới. Hội tụ khi dùng lại một tập dữ liệu cố định là bài toán khác. Hết ngân sách hoặc có một vài lượt dự đoán đúng không chứng minh hội tụ.

::: exercise Câu hỏi:
So sánh vai trò của điều kiện kết thúc trong trường hợp $\gamma<1$ và $\gamma=1$. Giải thích vì sao bước học hằng không thỏa điều kiện tổng bình phương hữu hạn khi tiếp tục nhận mẫu mới.
:::

::: hint
Xét tổng của các hệ số $\gamma^k$ khi phần thưởng bị chặn, và xét $\sum_n\alpha^2$ với một hằng số dương.
:::

::: solution
Với $\gamma<1$ và thưởng bị chặn, tổng chiết khấu hữu hạn ngay cả khi quá trình tiếp tục. Với $\gamma=1$, bảo đảm theo lượt đang dùng dựa trên kết thúc hấp thụ hợp lệ; riêng hệ số không bảo đảm lợi tức hữu hạn. MC đầy đủ vẫn cần kết thúc để quan sát trọn lợi tức dù $\gamma<1$. Khi $\alpha>0$ hằng, mỗi số hạng $\alpha^2$ dương như nhau nên tổng vô hạn; không có bảo đảm hội tụ điểm nói chung trên mẫu mới từ điều kiện bước học giảm.
:::

Nguồn: Sutton–Barto, §5.1, tr.92–93; §2.5, tr.33; §6.2, tr.124–125.

<!-- note-topic-id: lec-05-topic-16 -->
### Dự đoán từ tám lượt dữ liệu cố định

Xét hai trạng thái không kết thúc $A,B$, $\gamma=1$ và tập dữ liệu $\mathcal D$ gồm đúng tám lượt đã kết thúc:

| Số lượt | Trạng thái và phần thưởng |
|---|---|
| 1 | $A\xrightarrow{0}B\xrightarrow{0}\text{kết thúc}$ |
| 6 | $B\xrightarrow{1}\text{kết thúc}$ |
| 1 | $B\xrightarrow{0}\text{kết thúc}$ |

$A$ chỉ có một lợi tức quan sát bằng $0$. $B$ được ghé tám lần, nhận sáu lợi tức $1$ và hai lợi tức $0$. Bài toán là dự đoán khi dùng lại dữ liệu này mà không thu thêm lượt.

Khởi tạo $V_0(A)=V_0(B)=0$, chọn $\alpha=1/8$. Giữ nguyên bảng trong một lượt quét, tổng sai số tại $A$ bằng $0$ và tại $B$ bằng $6$ cho cả MC và TD. Sau khi cộng và ghi các gia số, bảng mới là $(0,3/4)$.

Trong quy trình **cập nhật theo lô**, $k$ đếm lượt quét tập dữ liệu, khác thời điểm tương tác $t$. Đầu vào gồm $\mathcal D,\gamma,V_0$, bước học đủ nhỏ $\alpha$, ngưỡng $\varepsilon>0$ và số quét tối đa $K$:

1. Giữ $V_k$ cố định; đặt tổng gia số $\Delta_k(s)=0$ tại mọi trạng thái.
2. Quét tất cả mẫu trong $\mathcal D$. MC dùng lợi tức đã tính; TD dùng thưởng và giá trị trạng thái sau trong cùng $V_k$.
3. Với mỗi mẫu tại $s$ có mục tiêu $y$ vừa tính, cộng gia số: $\Delta_k(s)\leftarrow\Delta_k(s)+\alpha[y-V_k(s)]$.
4. Ghi đồng thời $V_{k+1}(s)=V_k(s)+\Delta_k(s)$; trạng thái kết thúc giữ $0$.
5. Lặp tới khi $\max_s|V_{k+1}(s)-V_k(s)|<\varepsilon$ hoặc đủ $K$ lượt quét.

Mỗi lượt quét cần công việc tỷ lệ số chuyển trong dữ liệu và bộ nhớ cho dữ liệu cùng bảng. Ngưỡng dừng đo thay đổi giữa hai bảng, không tự xác nhận đã biết giá trị của môi trường thật.

MC theo lô khớp lợi tức quan sát. Tại $A$, tổng bình phương sai số là $v^2$; tại $B$ là $6(1-v)^2+2v^2$. Hai cực tiểu cho

$$V_{\mathrm{MC}}(A)=0,\qquad V_{\mathrm{MC}}(B)=\frac68=\frac34.$$

Quét MC tiếp từ $(0,3/4)$ không làm thay đổi bảng vì tổng sai số tại mỗi trạng thái bằng $0$.

Với TD theo lô, tổng sai số tại $A$ bằng $V_k(B)-V_k(A)$; tại $B$ bằng $6-8V_k(B)$. Hai truy hồi là

$$V_{k+1}(A)=V_k(A)+\alpha[V_k(B)-V_k(A)],$$
$$V_{k+1}(B)=V_k(B)+\alpha[6-8V_k(B)].$$

Riêng ví dụ này, $0<\alpha<1/4$ đủ để hai truy hồi ổn định, nên $\alpha=1/8$ là lựa chọn hợp lệ. Điều kiện tổng sai số bằng $0$ cho

$$V_{\mathrm{TD}}(A)=V_{\mathrm{TD}}(B)=\frac34.$$

![Mô hình Markov ước lượng từ tám lượt: A luôn chuyển đến B với thưởng 0; B kết thúc với thưởng 1 sáu lần và thưởng 0 hai lần.](img/lec-05/ab-empirical.svg)

Sơ đồ diễn giải quan hệ thực nghiệm tạo nghiệm TD; thuật toán có thể đạt nghiệm đó mà không cần dựng mô hình tường minh. MC tối thiểu hóa sai số với các lợi tức đã quan sát; TD khớp quan hệ Markov ước lượng từ dữ liệu. Hai tiêu chuẩn khác nhau giải thích hai giá trị tại $A$. Không có cơ sở gọi một nghiệm đúng hơn với mọi môi trường thật chỉ từ tám lượt này.

::: exercise Câu hỏi:
Từ bảng sau quét đầu $(V_1(A),V_1(B))=(0,3/4)$, tính quét thứ hai của MC và TD với $\alpha=1/8$. Giải thích hai nghiệm giới hạn và đánh giá hai nhận định: “TD luôn chính xác hơn vì phương sai luôn thấp hơn”; “bước học hằng luôn hội tụ đúng khi tiếp tục nhận mẫu mới”.
:::

::: hint
MC dùng lợi tức cố định; TD giữ $V_1$ khi tính mọi mục tiêu trong lượt quét. Phân biệt bảng sau hai lượt quét với nghiệm khi lặp đến giới hạn.
:::

::: solution
MC vẫn cho $(0,3/4)$ vì tổng sai số bằng $0$. TD cho $V_2(A)=0+\frac18\cdot\frac34=\frac3{32}=0.09375$ và $V_2(B)=3/4$. Hai lượt quét chưa đạt nghiệm TD $(3/4,3/4)$.

MC khớp lợi tức duy nhất $0$ của $A$; TD khớp chuyển $A\to B$ và giá trị $B=3/4$ từ tám lượt. Hai nhận định tuyệt đối đều không được bảo đảm: mục tiêu TD dùng bảng học được không có thứ tự phương sai phổ quát; bước hằng trên mẫu mới có thể duy trì dao động. Việc lặp trên tập dữ liệu cố định với bước học đủ nhỏ có điều kiện và đích hội tụ khác.
:::

Nguồn: Sutton–Barto, §6.3, tr.126–128, Ví dụ 6.4.

## Lựa chọn phương pháp và tự kiểm tra

<!-- note-topic-id: lec-05-topic-14 -->
### Lựa chọn theo thông tin sẵn có

| Thông tin và yêu cầu | Lựa chọn có căn cứ |
|---|---|
| Có lượt hoàn chỉnh, cần khớp lợi tức quan sát | MC với mục tiêu $G_t$; chỉ rõ quy tắc lần ghé và bước học. |
| Cần cập nhật sau một chuyển, chưa có kết quả cuối | TD(0) với $R_{t+1}+\gamma V_t(S_{t+1})$; trạng thái có đủ thông tin Markov. |
| Dữ liệu được giữ cố định và dùng lại | Xác định tiêu chuẩn khớp lợi tức hoặc quan hệ Markov thực nghiệm trước khi so sánh. |

MC đầy đủ cần chờ kết thúc. TD dùng giá trị tiếp nối đang ước lượng nên có thể cập nhật giữa lượt. Khi mục tiêu là hội tụ từ mẫu mới, lịch bước học phải đi cùng giả thiết về môi trường, chính sách và độ phủ dữ liệu. Không có lựa chọn nào trong bảng tạo bảo đảm hiệu quả mẫu tốt hơn trên mọi môi trường.

::: exercise Câu hỏi:
Một môi trường có lượt rất dài, thưởng chỉ ở cuối; yêu cầu là cập nhật ước lượng sau mỗi chuyển. Chọn phương pháp trong bài và nêu thông tin nó dùng cùng giới hạn của mục tiêu cập nhật.
:::

::: hint
Phân biệt thời điểm có lợi tức đầy đủ với thời điểm có thưởng đầu và trạng thái kế tiếp.
:::

::: solution
TD(0) đáp ứng cập nhật sau mỗi chuyển. Nó dùng phần thưởng, trạng thái sau, bảng hiện tại, hệ số chiết khấu và bước học. Giá trị tiếp nối là một ước lượng, nên mục tiêu có thể có sai lệch kỳ vọng và không có bảo đảm phương sai nhỏ hơn cho mọi bảng. Thưởng thưa không tự bảo đảm TD lan truyền kết quả cuối nhanh hơn MC; điều đó còn phụ thuộc dữ liệu và cách dùng lại dữ liệu.
:::

Nguồn: bài giảng gốc, tr.28, 33; Sutton–Barto, §5.1 và §6.1–6.3.

<!-- note-topic-id: lec-05-topic-15 -->
### Năng lực, bài tập và tài liệu đọc

Ba năng lực của bài là lập tập mẫu lợi tức đúng quy tắc, thực hiện các cập nhật MC/TD(0), và giải thích kết quả theo dữ liệu cùng giả thiết. Hai lượt chuỗi ngắn kiểm khả năng chọn mẫu và đọc bảng; hai đường chuỗi dài kiểm chỉ số chiết khấu; tám lượt A–B phân biệt tiêu chuẩn đánh giá trên dữ liệu cố định. Chính sách được giữ cố định trong các phép tính này.

::: exercise Câu hỏi:
(a) Sau lượt hoàn chỉnh $e_1$, nêu hai lựa chọn cần xác định trước khi báo cáo kết quả MC. (b) Sau tiền tố chưa kết thúc $S\to X$, nêu một cách cập nhật đã học và thông tin cần có. (c) Trên tám lượt A–B, xác định điều kiện để gọi một nghiệm tốt hơn nghiệm kia.
:::

::: hint
Lần lượt xét tập mẫu và trọng số, mục tiêu một bước, rồi tiêu chuẩn đánh giá trên dữ liệu hữu hạn.
:::

::: solution
(a) Cần chọn lần ghé đầu tiên hoặc mọi lần ghé, cùng quy tắc bước học; giá trị khởi tạo phải được nêu khi còn ảnh hưởng. (b) TD(0) dùng thưởng, trạng thái sau, bảng hiện tại, $\gamma$ và bước học để tạo mục tiêu $R_{t+1}+\gamma V_t(S_{t+1})$. (c) Cần xác định tiêu chuẩn khớp lợi tức quan sát hoặc khớp quan hệ Markov thực nghiệm. Để so sánh sai số với môi trường thật cần giá trị chuẩn hoặc dữ liệu đánh giá phù hợp; tám lượt chưa chứng minh ưu thế phổ quát.
:::

#### Tự luyện với Bài tập tuần 5

[Bài tập tuần 5: Dự đoán phi mô hình](../RL-hk2-2025-2026/resources/hw05-model-free-prediction.pdf) gồm bảy bài. Các yêu cầu dưới đây làm rõ những giả thiết cần dùng khi giải.

- **Bài 1–3:** so sánh mục tiêu và thời điểm cập nhật, xác định mẫu tương tác, viết mục tiêu/sai số/quy tắc TD(0). Mọi giá trị ở vế phải phải lấy từ bảng trước cập nhật; giá trị tiếp nối của trạng thái kết thúc bằng $0$.
- **Bài 4:** phân tích nguồn sai lệch và phương sai trong lượt dài, thưởng thưa, hành động nhiễu. Yêu cầu không giả định TD luôn học nhanh hơn. Lời giải cần phân biệt mục tiêu lý tưởng dùng $v_\pi$ với mục tiêu dùng $V$ đang học và nêu giới hạn của kết luận về hiệu quả mẫu.
- **Bài 5:** tách lựa chọn lần ghé khỏi lựa chọn bước học. Cả lần ghé đầu tiên và mọi lần ghé đều có thể kết hợp với trung bình mẫu hoặc bước học hằng. Không dùng tiền đề rằng mọi cấu hình, kể cả bước hằng trên mẫu mới, đều hội tụ đúng. Nêu giả thiết dữ liệu và điều kiện bước học phù hợp với kết luận.
- **Bài 6:** giải giá trị chuẩn từ mô hình chuỗi năm ô; dùng chuẩn đó để đối chiếu dự đoán, không coi mô hình là đầu vào bắt buộc của MC/TD.
- **Bài 7:** chỉ định quy tắc lần ghé trước khi tính MC; chạy riêng từng phương pháp từ cùng bảng khởi tạo. So sánh tác động của thưởng cuối trên đúng hai lượt, không suy ra thứ tự tốc độ học phổ quát.

#### Bài 5: điều kiện của các cấu hình Monte Carlo

Với lần ghé đầu tiên và trung bình mẫu, các lượt độc lập dưới cùng chính sách cho các lợi tức độc lập cùng phân phối tại trạng thái đang xét. Khi phương sai hữu hạn và số mẫu tăng vô hạn, trung bình hội tụ về $v_\pi(s)$; ở số mẫu cố định, nó không chệch.

Với mọi lần ghé và trung bình mẫu, dùng bộ điều kiện của phần hội tụ: quá trình phần thưởng Markov hữu hạn do chính sách Markov dừng, cố định; phần thưởng bị chặn; kết thúc hầu chắc chắn từ mọi trạng thái không kết thúc đang xét; các lượt khởi động độc lập cùng phân phối; xác suất ghé $s$ dương; $0\le\gamma\le1$ và bước học $1/N(s)$. Khi số lượt hoàn chỉnh tăng vô hạn, ước lượng hội tụ hầu chắc chắn về $v_\pi(s)$, dù lợi tức trong cùng lượt có thể phụ thuộc. Không suy ra tính không chệch ở số lượt hữu hạn.

Với bước học hằng, cả hai quy tắc lần ghé tạo trung bình có trọng số theo thời gian. Khi $0<\alpha<1$, ảnh hưởng khởi tạo giảm dần; khi $\alpha=1$, ước lượng bằng mẫu mới nhất. Trên mẫu ngẫu nhiên mới, bước hằng không thỏa điều kiện tổng bình phương hữu hạn và có thể duy trì dao động; không có bảo đảm hội tụ đúng chung cho cả bốn cấu hình.

#### Bài 6: giá trị chuẩn của chuỗi năm ô

Chuỗi gồm $c_1,c_2,c_3,c_4,c_5$, trong đó $c_5$ kết thúc. Chính sách luôn dự định đi phải; xác suất đi phải, đứng yên, đi trái lần lượt là $0.8,0.1,0.1$. Nếu vượt biên thì đứng tại chỗ. Mọi chuyển có thưởng $-1$, riêng $c_4\to c_5$ có thưởng $10$. Hệ số chiết khấu $\gamma=0.9$.

Câu hỏi: Viết hệ Bellman kỳ vọng, giải giá trị của bốn trạng thái không kết thúc và giải thích thứ tự các giá trị trong đúng mô hình này.

Gợi ý: Tại $c_1$, đi trái vượt biên làm xác suất đứng tổng cộng bằng $0.2$. Tại $c_4$, cần tách chuyển vào đích khỏi hai khả năng nhận thưởng $-1$.

Đặt $v_i=v_\pi(c_i)$ và $v_5=0$. Hệ phương trình và lời giải là

$$v_1=-1+0.9(0.2v_1+0.8v_2),$$
$$v_2=-1+0.9(0.1v_1+0.1v_2+0.8v_3),$$
$$v_3=-1+0.9(0.1v_2+0.1v_3+0.8v_4),$$
$$v_4=0.8(10)+0.2(-1)+0.9(0.1v_3+0.1v_4).$$

Thưởng kỳ vọng tại $c_4$ bằng $7.8$. Viết lại hệ tuyến tính:

$$\begin{aligned}
0.82v_1-0.72v_2&=-1,\\
-0.09v_1+0.91v_2-0.72v_3&=-1,\\
-0.09v_2+0.91v_3-0.72v_4&=-1,\\
-0.09v_3+0.91v_4&=7.8.
\end{aligned}$$

Khử các ẩn cho

$$(v_1,v_2,v_3,v_4)\approx(2.658941901,4.417128276,6.639280500,9.228060709).$$

Các hiệu lần lượt xấp xỉ $1.758186375$, $2.222152224$, $2.588780209$, đều dương. Trong chuỗi này, các trạng thái gần đích hơn có phần thưởng dương đến sớm hơn và ít chi phí bước kỳ vọng hơn. Kết luận tăng dần dựa trên mô hình và nghiệm cụ thể, không phải quy luật chung của mọi bài toán có đích.

#### Bài 7: đối chiếu các cập nhật

Dùng $e_1:S\to X\to S\to X\to G$, $e_2:S\to X\to S\to L$, $\gamma=1$, $\alpha=0.5$. Mỗi phương pháp khởi tạo riêng $V(S)=V(X)=0$. Thưởng khi vào $L/G$ là $-1/+1$, còn lại $0$; giá trị ở trạng thái kết thúc bằng $0$.

| Cấu hình | Sau $e_1$ | Sau $e_2$ |
|---|---|---|
| MC lần ghé đầu tiên | $(0.5,0.5)$ | $(-0.25,-0.25)$ |
| MC mọi lần ghé | $(0.75,0.75)$ | $(-0.5625,-0.125)$ |
| TD(0) | $(0,0.5)$ | $(-0.375,0.375)$ |

Các bước trung gian nằm trong phần quy tắc MC và bảng TD trên hai lượt. Với MC, lần ghé đầu tiên và mọi lần ghé dùng cùng quy tắc bước học hằng nhưng khác số mẫu. Với TD, mỗi chuyển đọc bảng đã được cập nhật ở chuyển trước. Nếu đổi MC sang trung bình mẫu, kết quả sau hai lượt lần lượt là $(0,0)$ và $(0,1/3)$; đó là thay đổi quy tắc trọng số, không phải thay dữ liệu.

#### Tài liệu đọc

- [Bài giảng gốc: Dự đoán phi mô hình](../RL-hk2-2025-2026/lecture-05-du-doan-phi-mo-hinh.pdf), tr.15–33: chuỗi ngắn, chuỗi dài, MC và TD(0).
- [Bài tập tuần 5](../RL-hk2-2025-2026/resources/hw05-model-free-prediction.pdf), bài 1–7; áp dụng các hiệu chỉnh giả thiết đã nêu.
- Richard S. Sutton và Andrew G. Barto, [Reinforcement Learning: An Introduction](https://mitpress.mit.edu/9780262039246/reinforcement-learning/), ấn bản 2. §5.1, tr.92–96: lựa chọn mẫu và MC; §6.1–6.3, tr.119–128: TD và dữ liệu hữu hạn; §2.4–2.5, tr.30–33: trung bình gia tăng và bước học. Số trang theo trang in, nội dung đối chiếu bản PDF 2020.
