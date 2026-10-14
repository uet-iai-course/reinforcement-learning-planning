# Bài 04 — Giải MDP bằng quy hoạch động

## Mục tiêu học tập

Sau chương này, người học có thể:

1. Thực hiện một lượt quét đánh giá chính sách, giải giá trị chính xác trên mô hình nhỏ và chặn sai số bằng phần dư Bellman (Bài tập 04.1, 04.7; tệp bài tập: 04.10, 04.16).
2. Tính giá trị nhìn trước, lập chính sách tham lam với quy tắc phá hòa và giải thích bằng định lý cải thiện vì sao giá trị không giảm (Bài tập 04.2; tệp bài tập: 04.17).
3. Chạy lặp chính sách tới chính sách ổn định; phân biệt chứng nhận tối ưu với việc chính sách không đổi theo một bảng gần đúng (Bài tập 04.3; tệp bài tập: 04.12, 04.15).
4. Chạy lặp giá trị, trích chính sách tham lam, chọn ngưỡng dừng theo sai số cho phép và đọc chặn hội tụ hình học (Bài tập 04.4; tệp bài tập: 04.11–04.14).
5. So sánh cập nhật đồng bộ, cập nhật tại chỗ và quy hoạch động bất đồng bộ; nêu điều kiện bao phủ của lịch cập nhật và các điều kiện về mô hình khi áp dụng cho CartPole rời rạc hóa (Bài tập 04.5, 04.6, 04.9; tệp bài tập: 04.14, 04.15; Tình huống 04.1–04.2).

Bài tập 04.1–04.9 nằm trong chương; [tệp bài tập của Bài 04](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-giai-mdp-bang-quy-hoach-dong.html) chép lại Bài tập 04.1–04.6 và thêm Bài tập 04.10–04.17, cùng bộ đếm.

## Kiến thức tiên quyết

Cách dẫn "ghi chú Bài 03, Mục k" chỉ Mục k của ghi chú Bài 03, và số hiệu dạng 03.k là số hiệu kết quả trong ghi chú đó; mỗi kết quả được phát biểu lại dưới đây ở dạng dùng được.

- **Quá trình quyết định Markov hữu hạn** (ghi chú Bài 03, Mục 1; Định nghĩa 03.7). Một quá trình quyết định Markov (Markov decision process, MDP) hữu hạn gồm tập trạng thái, tập hành động, tập phần thưởng hữu hạn và mô hình $p(s',r\mid s,a)=\Pr(S_{t+1}=s',R_{t+1}=r\mid S_t=s,A_t=a)$. Tính Markov: phân phối của $(S_{t+1},R_{t+1})$ chỉ phụ thuộc $(S_t,A_t)$, không phụ thuộc phần lịch sử trước đó.
- **Lợi tức chiết khấu** (ghi chú Bài 03, Mục 2 và 4; Định nghĩa 03.9, Mệnh đề 03.11, Bổ đề 03.18). Lợi tức (return) từ thời điểm $t$ là $G_t=\sum_{j\ge0}\gamma^jR_{t+j+1}$ và thỏa $G_t=R_{t+1}+\gamma G_{t+1}$. Khi $\lvert R_{t+1}\rvert\le R_{\max}$ với mọi $t$ và $0\le\gamma<1$, chuỗi hội tụ và $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$.
- **Chính sách và hàm giá trị** (ghi chú Bài 03, Mục 3; Định nghĩa 03.13, 03.15, 03.16). Chính sách Markov dừng (stationary policy) $\pi(a\mid s)$ là một phân phối trên các hành động hợp lệ tại $s$, chỉ phụ thuộc trạng thái hiện tại và không đổi theo thời gian. Chữ "dừng" ở đây chỉ tính chất không đổi theo thời gian của chính sách, khác với việc dừng một thuật toán ở các mục sau. Giá trị trạng thái là $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$; giá trị hành động $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ ấn định hành động đầu là $a$ rồi theo $\pi$ từ bước sau.
- **Phương trình Bellman kỳ vọng** (ghi chú Bài 03, Mục 4; Định lý 03.21, Mệnh đề 03.22, 03.23). Với mọi $s$ và mọi hành động $a$ hợp lệ,
  $q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr]$ và $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$; ghép hai đẳng thức cho phương trình của $v_\pi$ theo chính $v_\pi$.
- **Đánh giá chính sách bằng hệ tuyến tính** (ghi chú Bài 03, Mục 5; Mệnh đề 03.27, Định lý 03.28). Trên $n$ trạng thái chưa kết thúc, phương trình Bellman kỳ vọng là hệ tuyến tính $(I-\gamma P_\pi)v_\pi=r_\pi$, với $P_\pi$ là ma trận chuyển giữa các trạng thái chưa kết thúc và $r_\pi$ là vectơ thưởng kỳ vọng một bước dưới $\pi$; khi $0\le\gamma<1$, $I-\gamma P_\pi$ khả nghịch.
- **Giải tích trên $\mathbb R$.** Mỗi dãy Cauchy số thực hội tụ; cực đại của một hàm trên tập hữu hạn khác rỗng luôn đạt tại một phần tử của tập; tổng hữu hạn có trọng số không âm, tổng trọng số bằng $1$, nằm giữa giá trị nhỏ nhất và lớn nhất của các số hạng.

## Bảng ký hiệu

Bảng chỉ gồm các ký hiệu dùng xuyên suốt chương; ký hiệu chỉ dùng trong một ví dụ, một chứng minh hay một tình huống được giới thiệu tại chỗ. Mỗi chữ giữ một nghĩa trong cả chương.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $n$ | tập trạng thái chưa kết thúc; $n=\lvert\mathcal S\rvert$ | tập hữu hạn khác rỗng |
| $s_{\mathrm{term}}$, $\mathcal S^+$ | trạng thái kết thúc (nếu có); $\mathcal S\cup\{s_{\mathrm{term}}\}$ | phần tử; tập hữu hạn |
| $\mathcal A(s)$, $m$ | tập hành động hợp lệ tại $s$; $m=\max_s\lvert\mathcal A(s)\rvert$ | tập hữu hạn khác rỗng |
| $\mathcal R$, $R_{\max}$ | tập phần thưởng; cận $\lvert r\rvert\le R_{\max}$ | tập hữu hạn của $\mathbb R$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động, phần thưởng ở bước tương tác $t$ | $t=0,1,2,\dots$ |
| $p(s',r\mid s,a)$ | mô hình chuyển–thưởng | phân phối trên $\mathcal S^+\times\mathcal R$ với mỗi $(s,a)$ |
| $p(s'\mid s,a)$, $r(s,a)$ | xác suất chuyển biên; thưởng kỳ vọng một bước | $[0,1]$; $\mathbb R$ |
| $d$ | số trạng thái kế tiếp tối đa có xác suất dương của một cặp $(s,a)$ | số nguyên dương |
| $\gamma$ | hệ số chiết khấu | $[0,1)$; $\gamma=1$ chỉ xét như phản ví dụ |
| $G_t$ | lợi tức từ thời điểm $t$ | biến ngẫu nhiên thực |
| $\pi(a\mid s)$, $\pi(s)$ | chính sách Markov dừng; hành động của chính sách xác định | phân phối trên $\mathcal A(s)$; phần tử của $\mathcal A(s)$ |
| $\Pi$ | lớp mọi chính sách, kể cả chính sách phụ thuộc lịch sử | tập |
| $v_\pi$, $q_\pi$ | giá trị trạng thái và giá trị hành động thật của $\pi$ | $\mathbb R^n$; hàm trên các cặp $(s,a)$ |
| $v_*$, $q_*$, $\pi_*$ | giá trị tối ưu; một chính sách tối ưu | $\mathbb R^n$; hàm trên các cặp $(s,a)$; chính sách |
| $V$, $U$, $W$, $V_k$ | bảng giá trị bất kỳ; bảng tạm; bảng sau $k$ lượt quét | $\mathbb R^n$, mở rộng bằng $0$ tại $s_{\mathrm{term}}$ |
| $k$, $i$ | chỉ số lượt quét; chỉ số vòng cải thiện của lặp chính sách | $0,1,2,\dots$ |
| $Q_V(s,a)$ | giá trị nhìn trước một bước tính từ bảng $V$ | $\mathbb R$ |
| $T_\pi$, $T_*$ | toán tử Bellman đánh giá và toán tử Bellman tối ưu | ánh xạ $\mathbb R^n\to\mathbb R^n$ |
| $P_\pi$, $r_\pi$ | ma trận chuyển và vectơ thưởng kỳ vọng dưới $\pi$ | $\mathbb R^{n\times n}$; $\mathbb R^n$ |
| $\lVert\cdot\rVert_\infty$ | chuẩn vô cùng, $\lVert U\rVert_\infty=\max_s\lvert U(s)\rvert$ | $\mathbb R^n\to[0,\infty)$ |
| $\Delta_\pi(V)$, $\Delta_*(V)$ | phần dư Bellman của bảng $V$ đối với $T_\pi$, $T_*$ | $[0,\infty)$ |
| $\theta$, $\kappa$ | ngưỡng dừng trên phần dư; sai số giá trị cho phép | $\theta>0$; $\kappa>0$ |
| $K$, $I_{\max}$ | ngân sách số lượt quét (Thuật toán 04.9, 04.28) hoặc số bước cập nhật (Thuật toán 04.31); ngân sách số vòng của lặp chính sách | số nguyên không âm; số nguyên dương |
| $\pi_V$ | chính sách tham lam theo bảng $V$ | chính sách xác định |
| $\mathrm s_0,\mathrm s_1$; $\mathrm a,\mathrm b$; $\mathrm c_1,\dots,\mathrm c_5$; $\mathrm{trai},\mathrm{phai}$ | tên trạng thái và hành động trong các ví dụ | nhãn, không phải biến |

Các quy ước đọc sau dùng trong cả chương.

- Bất đẳng thức giữa hai bảng hiểu theo từng trạng thái: $U\le V$ nghĩa là $U(s)\le V(s)$ với mọi $s\in\mathcal S$.
- $R_{t+1}$ là phần thưởng của chuyển từ thời điểm $t$ sang $t+1$, nhận sau hành động $A_t$; kỳ vọng $\mathbb E_\pi$ lấy theo cả chính sách $\pi$ lẫn mô hình $p$.
- Sau khi vào $s_{\mathrm{term}}$, mọi phần thưởng về sau bằng $0$, nên mọi bảng giá trị tại $s_{\mathrm{term}}$ bằng $0$; phần thưởng của chính chuyển đi vào $s_{\mathrm{term}}$ vẫn được tính.
- Chỉ số $t$ đếm bước tương tác, còn $k$ và $i$ đếm bước tính toán; kết thúc một lượt (episode) tương tác khác với việc dừng thuật toán.

Tên trạng thái và hành động của ví dụ viết chữ đứng, chẳng hạn hành động $\mathrm a$, để phân biệt với biến hành động $a$ viết nghiêng. Chính sách xác định trên mô hình hai trạng thái được viết thành cặp theo thứ tự $(\mathrm s_0,\mathrm s_1)$: $(\mathrm a,\mathrm b)$ chọn $\mathrm a$ tại $\mathrm s_0$ và $\mathrm b$ tại $\mathrm s_1$. Chính sách ngẫu nhiên đều trên mô hình hai trạng thái và các cặp bảng minh họa tính co là số liệu sư phạm tự xây dựng.

Tương ứng ký hiệu: giáo trình *Học máy thống kê* viết $V^\pi$, $Q^\pi$, $T(s,a,s')$ và bộ $\langle S,A,T,R,\gamma\rangle$ cho $v_\pi$, $q_\pi$, $p(s'\mid s,a)$ và $(\mathcal S,\mathcal A,p)$ cùng $\gamma$ ở đây; phần thưởng $R(s,a,s')$ của một chuyển cho $r(s,a)=\sum_{s'}p(s'\mid s,a)R(s,a,s')$. Bài thực hành CartPole viết $\hat p$, $\hat r$ cho mô hình ước lượng, $\eta$ cho ngưỡng dừng, $\varepsilon$ cho sai số cho phép, chữ theta (biến `theta` trong mã, $\theta$ và $\dot\theta$ trong công thức) cho góc cột và vận tốc góc, và $m$ cho số lần áp dụng $T_\pi$ mỗi vòng của lặp chính sách cải biên ở nhiệm vụ 7; chương này dùng $\theta$, $\kappa$, $\phi$, $\dot\phi$ và $\ell$, vì $m$ đã chỉ số hành động tối đa.

## Bản đồ chủ đề

Chương có năm chủ đề cốt lõi, ba chủ đề cầu nối, bốn chủ đề bổ sung và một nhóm đọc thêm. Mã chủ đề là `note-topic-id`, dùng để nối ghi chú với bộ trang chiếu. Nguồn ghi theo trang của Bài giảng gốc (2025–2026) và mục của Sutton và Barto (2018).

### Đánh giá chính sách lặp

- Mã chủ đề: `lec-04-part-03`. Nhóm: `cốt lõi`. Mục: `## 1.` (mạch 2 của bộ trang chiếu). Nguồn: trang 5–6, 10, 14, 17–18; §4.1.
- Vai trò trong mạch: tính $v_\pi$ bằng lượt quét. Kết nối vào: Bellman kỳ vọng (Bài 03). Kết nối ra: giá trị tiếp nối cho cải thiện.

### Phần dư Bellman và điều kiện dừng

- Mã chủ đề: `lec-04-part-08`. Nhóm: `cốt lõi`. Mục: `## 1.`, `## 4.` (mạch 2, 5). Nguồn: trang 14, 31–34.
- Vai trò trong mạch: đại lượng dừng có chặn sai số. Kết nối vào: tính co. Kết nối ra: Thuật toán 04.9, 04.28.

### Cải thiện chính sách

- Mã chủ đề: `lec-04-part-04`. Nhóm: `cốt lõi`. Mục: `## 2.` (mạch 3). Nguồn: trang 19–21; §4.2.
- Vai trò trong mạch: đổi hành động mà giá trị không giảm. Kết nối vào: $v_\pi$ chính xác. Kết nối ra: chính sách mới cần đánh giá lại.

### Lặp chính sách và phương trình Bellman tối ưu

- Mã chủ đề: `lec-04-part-09`. Nhóm: `cốt lõi`. Mục: `## 3.` (mạch 4). Nguồn: trang 7–9, 13, 20, 33–34; §4.3.
- Vai trò trong mạch: tới chính sách ổn định, tối ưu. Kết nối vào: định lý cải thiện. Kết nối ra: $v_*=(27,30)$, chi phí đánh giá đầy đủ.

### Lặp giá trị

- Mã chủ đề: `lec-04-part-05`. Nhóm: `cốt lõi`. Mục: `## 4.` (mạch 5). Nguồn: trang 23–28, 31–34; §4.4.
- Vai trò trong mạch: toán tử $T_*$, hội tụ, điều kiện dừng. Kết nối vào: lặp chính sách. Kết nối ra: $T_*$ cho lịch bất đồng bộ.

### Mô hình hai trạng thái và lợi tức

- Mã chủ đề: `lec-04-part-01`. Nhóm: `cầu nối`. Mục: `### 1.1`. Nguồn: trang 4–5, 17–18; Bài tập tuần 4 (2025–2026), bài 1.
- Vai trò trong mạch: ví dụ xuyên suốt. Kết nối vào: MDP, lợi tức (Bài 03). Kết nối ra: dữ kiện cho mọi mục.

### Giá trị hành động và giá trị nhìn trước

- Mã chủ đề: `lec-04-part-02`. Nhóm: `cầu nối`. Mục: `### 2.1`. Nguồn: trang 5–6, 19; công thức (4.6) của Sutton và Barto.
- Vai trò trong mạch: mở rộng $q_\pi$ thành $Q_V$. Kết nối vào: Bellman cho $q_\pi$ (Bài 03). Kết nối ra: cải thiện và $T_*$.

### Chuẩn vô cùng, tính co và điểm bất động

- Mã chủ đề: `lec-04-part-06`. Nhóm: `cầu nối`. Mục: `### 1.3`, `### 4.2`. Nguồn: trang 31–32; Bài tập tuần 3 (2025–2026), bài 6–7.
- Vai trò trong mạch: công cụ chứng minh hội tụ. Kết nối vào: giải tích trên $\mathbb R$. Kết nối ra: Mệnh đề 04.4, 04.24, Định lý 04.5.

### Tồn tại chính sách tối ưu

- Mã chủ đề: `lec-04-part-11`. Nhóm: `bổ sung`. Mục: `### 4.3`. Nguồn: Bài tập tuần 3 (2025–2026), bài 3; Puterman (1994), §6.2.
- Vai trò trong mạch: cận trên trên mọi chính sách đạt được. Kết nối vào: tính co của $T_*$. Kết nối ra: $v_*$ là điểm bất động của $T_*$.

### Lịch cập nhật và quy hoạch động bất đồng bộ

- Mã chủ đề: `lec-04-part-10`. Nhóm: `bổ sung`. Mục: `### 5.1`, `### 5.2`. Nguồn: trang 15, 29; §4.5, §4.7.
- Vai trò trong mạch: cập nhật rẻ hơn, điều kiện bao phủ. Kết nối vào: $T_*$. Kết nối ra: Tình huống 04.1.

### Lặp chính sách tổng quát

- Mã chủ đề: `lec-04-part-07`. Nhóm: `bổ sung`. Mục: `### 5.3`. Nguồn: trang 13, 23, 29; §4.6.
- Vai trò trong mạch: khung chung của ba thuật toán. Kết nối vào: Mục 3–5. Kết nối ra: Bài 05–06.

### CartPole rời rạc hóa

- Mã chủ đề: `lec-04-part-12`. Nhóm: `bổ sung`. Mục: `### 5.4`. Nguồn: trang 35–37; bài thực hành CartPole.
- Vai trò trong mạch: mô hình bảng của môi trường liên tục. Kết nối vào: Mục 1–4. Kết nối ra: Tình huống 04.1–04.2.

### Đọc thêm

- Mã chủ đề: `lec-04-part-13`. Nhóm: `đọc thêm`. Mục: `## Hướng dẫn đọc thêm và tài liệu tham khảo`. Nguồn: Puterman (1994), §6.5; Singh và Yee (1994); Sutton và Barto (2018), Ví dụ 4.1.
- Nội dung: lặp chính sách cải biên, tổn thất của chính sách tham lam, trường hợp không chiết khấu.

## 1. Đánh giá chính sách

Trong Bài 03, chúng ta đã biết rằng khi mô hình $p(s',r\mid s,a)$ và một chính sách Markov dừng $\pi$ được cho trước, giá trị $v_\pi$ thỏa phương trình Bellman kỳ vọng, và trên $n$ trạng thái chưa kết thúc, phương trình đó là một hệ tuyến tính có nghiệm duy nhất (Định lý 03.21 và 03.28, ghi chú Bài 03, Mục 4–5). Kết quả này trả lời câu hỏi "chính sách đã cho tốt đến mức nào". Nó chưa trả lời câu hỏi mà tác tử phải trả lời khi hành động: nên chọn hành động nào tại mỗi trạng thái.

Xét một mô hình có hai trạng thái $\mathrm s_0$, $\mathrm s_1$. Tại $\mathrm s_0$, hành động $\mathrm a$ cho phần thưởng $1$ và giữ tác tử ở $\mathrm s_0$, còn $\mathrm b$ cho phần thưởng $0$ nhưng đưa tác tử sang $\mathrm s_1$, nơi hai hành động cho phần thưởng $2$ và $3$. Nhìn phần thưởng trước mắt, $\mathrm a$ thắng; nhìn xa hơn, $\mathrm b$ mở đường tới phần thưởng lớn hơn. Để quyết định, chúng ta cần so sánh giá trị dài hạn, mà với $\gamma=0{,}9$ mỗi giá trị là tổng của vô hạn số hạng.

Bài toán của chương là bài toán lập kế hoạch (planning): từ mô hình đã biết, tìm chính sách $\pi$ có $v_\pi(s)$ lớn nhất đồng thời tại mọi trạng thái $s$. Quy hoạch động (dynamic programming) là tên chung của nhóm thuật toán giải bài toán này bằng cách biến các phương trình Bellman thành quy tắc cập nhật một bảng giá trị. Chúng ta sẽ chứng minh rằng, với MDP hữu hạn, phần thưởng bị chặn và $0\le\gamma<1$, cả giá trị của một chính sách lẫn giá trị tối ưu đều là điểm bất động duy nhất của một toán tử co (Định nghĩa 04.3), nên tính được bằng phép lặp có chặn sai số.

![Sơ đồ năm khối nối nhau từ trái sang phải. Khối "Đánh giá chính sách" ghi "giá trị hiện tại"; khối "Cải thiện chính sách" ghi "lựa chọn mới"; khối "Lặp chính sách" ghi "cặp ổn định"; khối "Lặp giá trị" ghi "bảng tối ưu"; khối "Lịch cập nhật" ghi "phân bổ tính".](img/lec-04/dp04-roadmap.svg)

Hình trên là cấu trúc của chương: đánh giá chính sách (Mục 1) cho giá trị của chính sách hiện tại, cải thiện (Mục 2) dùng giá trị đó tạo lựa chọn không kém hơn, lặp chính sách xen kẽ hai bước tới một cặp ổn định (Mục 3), lặp giá trị gộp hai bước làm một (Mục 4), và khối cuối xét lịch cập nhật cùng giới hạn của mô hình bảng (Mục 5).

<!-- note-topic-id: lec-04-part-01 -->
### 1.1 Mô hình hai trạng thái và lợi tức

Ví dụ xuyên suốt của chương là mô hình hai trạng thái của Bài giảng gốc (2025–2026), trang 17–18. Mô hình có tập trạng thái $\mathcal S=\{\mathrm s_0,\mathrm s_1\}$, không có trạng thái kết thúc, mỗi trạng thái có hai hành động $\mathrm a$, $\mathrm b$, và mọi chuyển đều xác định, tức xảy ra với xác suất $1$.

| Trạng thái $s$ | Hành động | Trạng thái kế tiếp $s'$ | Phần thưởng $r$ |
|---|---|---|---:|
| $\mathrm s_0$ | $\mathrm a$ | $\mathrm s_0$ | $1$ |
| $\mathrm s_0$ | $\mathrm b$ | $\mathrm s_1$ | $0$ |
| $\mathrm s_1$ | $\mathrm a$ | $\mathrm s_0$ | $2$ |
| $\mathrm s_1$ | $\mathrm b$ | $\mathrm s_1$ | $3$ |

Hệ số chiết khấu là $\gamma=0{,}9$. Trong ngôn ngữ của mô hình, dòng thứ hai của bảng nói $p(\mathrm s_1,0\mid\mathrm s_0,\mathrm b)=1$, và mọi bộ $(s',r)$ khác có xác suất $0$ dưới cặp $(\mathrm s_0,\mathrm b)$.

![Hai nút tròn s0 và s1. Từ s0, cung "a / 1" vòng về s0 và cung "b / 0" đi sang s1. Từ s1, cung "a / 2" đi về s0 và cung "b / 3" vòng về s1. Nhãn có dạng hành động / phần thưởng; mọi chuyển có xác suất 1.](img/lec-04/dp04-two-state.svg)

Trên hình, mỗi cung mang nhãn "hành động / phần thưởng". Hai cung vòng là hai cách ở lại một trạng thái: $\mathrm a$ tại $\mathrm s_0$ với phần thưởng $1$ mỗi bước, $\mathrm b$ tại $\mathrm s_1$ với phần thưởng $3$ mỗi bước. Hai cung nối là hai cách đổi trạng thái, và cung từ $\mathrm s_0$ sang $\mathrm s_1$ có phần thưởng $0$, thấp nhất trong bốn cung.

Chính sách khởi đầu của chương là $\pi_0=(\mathrm a,\mathrm a)$, tức $\pi_0(\mathrm a\mid s)=1$ tại cả hai trạng thái. Theo $\pi_0$, tác tử đứng ở $\mathrm s_1$ chỉ ghé $\mathrm s_1$ một lần rồi ở mãi tại $\mathrm s_0$.

::: example Ví dụ 04.1 (Lợi tức cắt ngắn từ $\mathrm s_1$ theo $\pi_0$)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_0=(\mathrm a,\mathrm a)$; trạng thái đầu $S_0=\mathrm s_1$.

**Quỹ đạo.** Tại $\mathrm s_1$, $\pi_0$ chọn $\mathrm a$, nên $R_1=2$ và $S_1=\mathrm s_0$. Tại $\mathrm s_0$, $\pi_0$ chọn $\mathrm a$, nên $R_2=1$, $S_2=\mathrm s_0$, rồi $R_3=1$, và mọi phần thưởng sau đó đều bằng $1$.

**Tổng ba số hạng đầu.**

$$
R_1+\gamma R_2+\gamma^2R_3=2+0{,}9\cdot1+0{,}81\cdot1=3{,}71 .
$$

**Diễn giải.** Số $3{,}71$ là tổng cắt ngắn, chưa phải lợi tức $G_0$, vì còn các số hạng $\gamma^jR_{j+1}$ với $j\ge3$. Phần thưởng đầu mang chỉ số $1$ vì nó được nhận sau hành động $A_0$; nếu chỉ biết bảng phần thưởng của từng hành động mà không biết trạng thái kế tiếp, ta không xác định được $R_2=1$.

**Kiểm tra lại.** Tính từ cuối về đầu: $1+0{,}9\cdot1=1{,}9$, rồi $2+0{,}9\cdot1{,}9=3{,}71$.
:::

Ví dụ 04.1 cho thấy rằng tính lợi tức cần cả phần thưởng lẫn trạng thái kế tiếp, tức cần mô hình chuyển, và rằng cộng từng số hạng không cho kết quả đúng sau hữu hạn bước. Chúng ta cần một cách tính kỳ vọng của tổng vô hạn mà không cộng từng số hạng.

Bài toán tính $v_\pi$ khi $\pi$ được giữ cố định gọi là đánh giá chính sách (policy evaluation), hay bài toán dự đoán (prediction). Bài toán tìm chính sách tốt nhất gọi là bài toán điều khiển (control). Trong Mục 1, chính sách không đổi trong suốt quá trình tính; từ Mục 2 trở đi, chính sách được phép thay đổi.

<!-- note-topic-id: lec-04-part-03 -->
### 1.2 Lượt quét đồng bộ và toán tử $T_\pi$

Về mặt ý tưởng, hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ gợi ý một cách tính không cần cộng vô hạn số hạng. Nếu đã có một bảng $V$ ước lượng giá trị của mọi trạng thái, ta thay phần đuôi $G_{t+1}$ bằng $V(S_{t+1})$, lấy kỳ vọng theo hành động của chính sách và theo kết quả chuyển của mô hình, và được một ước lượng mới cho từng trạng thái. Đây mới là mô tả bằng lời, chưa phải định nghĩa: chúng ta chưa biết lặp lại phép thay này có tiến tới $v_\pi$ hay không.

![Sơ đồ cập nhật kỳ vọng theo chính sách. Từ nút "Trạng thái hiện tại", chính sách chọn hành động; từ hành động, mô hình dẫn tới "Kết quả chuyển thứ nhất" và "Kết quả chuyển khác". Mỗi kết quả ghi "Phần thưởng + giá trị tiếp nối". Nhãn dưới cùng: "Trung bình theo mô hình".](img/lec-04/dp04-expectation-backup.svg)

Hình trên đọc từ trái sang phải. Ở tầng thứ nhất, chính sách gán xác suất cho các hành động; ở tầng thứ hai, mô hình gán xác suất cho các kết quả chuyển. Mỗi lá cộng phần thưởng của chuyển với giá trị tiếp nối đã chiết khấu $\gamma V(s')$, và giá trị mới là trung bình có trọng số của các lá. Phép tính dùng mọi kết quả có thể của mô hình, nên được gọi là cập nhật kỳ vọng (expected update), để phân biệt với cập nhật dùng một chuyển lấy mẫu ở Bài 05.

::: example Ví dụ 04.2 (Hai lượt quét đồng bộ đánh giá $\pi_0$)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_0=(\mathrm a,\mathrm a)$. Bảng khởi tạo $V_0=(0,0)$.

**Quy tắc.** Theo $\pi_0$, cả hai trạng thái đều chọn $\mathrm a$, và $\mathrm a$ dẫn về $\mathrm s_0$ từ cả hai trạng thái. Giá trị mới của mỗi trạng thái bằng phần thưởng của cung $\mathrm a$ cộng $0{,}9$ nhân giá trị cũ của $\mathrm s_0$. Mọi ô của bảng mới đọc từ cùng một bảng cũ.

**Lượt quét thứ nhất, đọc $V_0$.**

$$
\begin{aligned}
V_1(\mathrm s_0)&=1+0{,}9\,V_0(\mathrm s_0)=1+0{,}9\cdot0=1,\\
V_1(\mathrm s_1)&=2+0{,}9\,V_0(\mathrm s_0)=2+0{,}9\cdot0=2.
\end{aligned}
$$

**Lượt quét thứ hai, đọc $V_1=(1,2)$.**

$$
\begin{aligned}
V_2(\mathrm s_0)&=1+0{,}9\,V_1(\mathrm s_0)=1+0{,}9\cdot1=1{,}9,\\
V_2(\mathrm s_1)&=2+0{,}9\,V_1(\mathrm s_0)=2+0{,}9\cdot1=2{,}9.
\end{aligned}
$$

| Lượt quét $k$ | $V_k(\mathrm s_0)$ | $V_k(\mathrm s_1)$ |
|---|---:|---:|
| $0$ | $0$ | $0$ |
| $1$ | $1$ | $2$ |
| $2$ | $1{,}9$ | $2{,}9$ |

**Diễn giải.** Với $V_0=0$, $V_k(s)$ là tổng chiết khấu của $k$ phần thưởng đầu khi xuất phát từ $s$ và theo $\pi_0$. Từ $\mathrm s_1$: $V_2(\mathrm s_1)=2+0{,}9\cdot1$, đúng hai số hạng đầu của tổng trong Ví dụ 04.1.

**Kiểm tra lại.** Ô $\mathrm s_1$ của lượt thứ hai dùng $V_1(\mathrm s_0)=1$ từ bảng cũ. Nếu dùng ngay giá trị mới $V_2(\mathrm s_0)=1{,}9$ thì được $2+0{,}9\cdot1{,}9=3{,}71$, kết quả của một thuật toán khác, cập nhật tại chỗ, xét ở Mục 5.
:::

Mỗi lần cập nhật mọi trạng thái một lần gọi là một lượt quét (sweep). Bảng $V_k$ là bảng sau $k$ lượt quét; chỉ số $k$ đếm phép tính, không phải bước tương tác $t$. Hai lượt quét của Ví dụ 04.2 đều thực hiện cùng một phép biến đổi trên toàn bảng: nhận bảng cũ, trả bảng mới. Định nghĩa sau đặt tên cho phép biến đổi đó.

::: definition Định nghĩa 04.1 (Toán tử Bellman đánh giá, lượt quét đồng bộ)
Cho MDP hữu hạn với mô hình $p(s',r\mid s,a)$, hệ số chiết khấu $\gamma\in[0,1]$ và chính sách Markov dừng $\pi$. Mỗi bảng $V\in\mathbb R^n$ được mở rộng lên $\mathcal S^+$ bằng $V(s_{\mathrm{term}})=0$.

**Toán tử Bellman đánh giá.** Toán tử Bellman (Bellman operator) của $\pi$ là ánh xạ $T_\pi:\mathbb R^n\to\mathbb R^n$ cho bởi

$$
(T_\pi V)(s)=\sum_{a\in\mathcal A(s)}\pi(a\mid s)\sum_{s'\in\mathcal S^+,\,r\in\mathcal R}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr],\qquad s\in\mathcal S .
\tag{1.1}
$$

**Lượt quét đồng bộ.** Từ bảng khởi tạo $V_0\in\mathbb R^n$, lượt quét đồng bộ thứ $k+1$ tạo bảng $V_{k+1}=T_\pi V_k$; mọi thành phần của $V_{k+1}$ được tính từ cùng bảng $V_k$, giữ cố định trong suốt lượt quét.
:::

Công thức (1.1) có ba tầng. Tổng ngoài cùng lấy trung bình theo hành động với trọng số $\pi(a\mid s)$; tổng bên trong lấy trung bình theo kết quả chuyển với trọng số $p(s',r\mid s,a)$; trong ngoặc vuông là phần thưởng của chuyển cộng giá trị tiếp nối chiết khấu $\gamma V(s')$, đọc từ bảng $V$.

Chỉ bảng $V$ thay đổi giữa các lượt quét; $p$, $\pi$, $\gamma$ giữ cố định. Trong Ví dụ 04.2, $\pi_0$ và mô hình đều xác định, nên mỗi tổng còn đúng một số hạng và (1.1) rút về $(T_{\pi_0}V)(\mathrm s_0)=1+0{,}9V(\mathrm s_0)$, $(T_{\pi_0}V)(\mathrm s_1)=2+0{,}9V(\mathrm s_0)$.

Toán tử $T_\pi$ gắn trực tiếp với phương trình Bellman kỳ vọng của Bài 03. Vế phải của phương trình đó chính là (1.1) với $V=v_\pi$, nên phương trình Bellman kỳ vọng viết gọn thành

$$
v_\pi=T_\pi v_\pi .
\tag{1.2}
$$

Đẳng thức (1.2) nói rằng $v_\pi$ là một điểm bất động của $T_\pi$, tức một bảng không đổi khi áp dụng toán tử. Lượt quét đồng bộ thì áp dụng $T_\pi$ cho một bảng bất kỳ, nói chung chưa phải điểm bất động: trong Ví dụ 04.2, $T_{\pi_0}V_1=(1{,}9;\,2{,}9)\ne V_1$. Mục tiêu cập nhật $r+\gamma V(s')$ được xây từ chính bảng ước lượng $V$; cách xây mục tiêu này gọi là bootstrap (bootstrapping), và đại lượng $r+\gamma V(s')$ là mục tiêu bootstrap (bootstrap target).

Khi chính sách ngẫu nhiên, tổng theo hành động trong (1.1) có nhiều số hạng, và ví dụ sau cho thấy toán tử thay đổi theo chính sách dù mô hình giữ nguyên.

::: example Ví dụ 04.3 (Một lượt quét cho chính sách ngẫu nhiên đều)
**Dữ kiện.** Mô hình hai trạng thái như Ví dụ 04.2: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; $\gamma=0{,}9$. Chính sách ngẫu nhiên đều $\pi_u(\mathrm a\mid s)=\pi_u(\mathrm b\mid s)=\tfrac12$ tại cả hai trạng thái; $V_0=(0,0)$.

**Tính.** Mỗi trạng thái lấy trung bình hai nhánh với trọng số $\tfrac12$:

$$
\begin{aligned}
(T_{\pi_u}V_0)(\mathrm s_0)&=\tfrac12\bigl(1+0{,}9\cdot0\bigr)+\tfrac12\bigl(0+0{,}9\cdot0\bigr)=0{,}5,\\
(T_{\pi_u}V_0)(\mathrm s_1)&=\tfrac12\bigl(2+0{,}9\cdot0\bigr)+\tfrac12\bigl(3+0{,}9\cdot0\bigr)=2{,}5.
\end{aligned}
$$

**Diễn giải.** Bảng khác $(1,2)$ của $\pi_0$ vì mỗi trạng thái lấy trung bình hai hành động.

**Kiểm tra lại.** Với $V_0=0$, mỗi thành phần của $T_{\pi_u}V_0$ là thưởng kỳ vọng một bước dưới $\pi_u$: $\tfrac{1+0}{2}=0{,}5$ và $\tfrac{2+3}{2}=2{,}5$.
:::

Nhầm lẫn thường gặp là đọc giá trị vừa ghi trong cùng một lượt quét đồng bộ. Lượt quét đồng bộ giữ bảng đọc cố định, nên cần hai mảng, một để đọc và một để ghi; đọc giá trị vừa ghi là một quy tắc khác, cho kết quả khác (Ví dụ 04.2, phần kiểm tra lại).

Tính chất đầu tiên của $T_\pi$ chỉ dùng dấu của các trọng số trong (1.1): khi bảng tiếp nối tăng ở mọi trạng thái, giá trị mới không thể giảm.

::: lemma Bổ đề 04.2 (Tính đơn điệu của $T_\pi$)
**Giả thiết.** MDP hữu hạn; $\gamma\ge0$; $\pi$ là chính sách Markov dừng; $U,V\in\mathbb R^n$ thỏa $U\le V$ theo từng trạng thái.

**Kết luận.** $T_\pi U\le T_\pi V$ theo từng trạng thái.

**Điều kiện áp dụng.** Chỉ cần các trọng số $\pi(a\mid s)$, $p(s',r\mid s,a)$ không âm và $\gamma\ge0$; không cần $\gamma<1$.

**Phạm vi.** Bổ đề so sánh hai bảng dưới cùng một toán tử; nó không so sánh hai chính sách khác nhau.
:::

::: proof Chứng minh Bổ đề 04.2
Cố định $s\in\mathcal S$. Lấy hiệu hai vế của (1.1) với $V$ và với $U$; các phần thưởng $r$ xuất hiện như nhau ở hai vế nên triệt tiêu:

$$
\begin{aligned}
&(T_\pi V)(s)-(T_\pi U)(s)\\
&\qquad=\gamma\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[V(s')-U(s')\bigr] &&\text{(1.1)}\\
&\qquad\ge0 &&\text{(thừa số không âm)}.
\end{aligned}
$$

Ở dòng cuối, $\pi(a\mid s)\ge0$, $p(s',r\mid s,a)\ge0$, $\gamma\ge0$, và $V(s')-U(s')\ge0$ với mọi $s'\in\mathcal S$ theo giả thiết; tại $s'=s_{\mathrm{term}}$ hiệu bằng $0$ vì cả hai bảng bằng $0$ ở đó. $\square$
:::

Tính đơn điệu được dùng lại ở Mục 2: nếu một bảng nằm dưới ảnh của nó qua $T_\pi$, áp dụng $T_\pi$ nhiều lần sẽ cho một dãy không giảm.

<!-- note-topic-id: lec-04-part-06 -->
### 1.3 Tính co và điểm bất động

Ví dụ 04.2 tạo dãy $(0,0)$, $(1,2)$, $(1{,}9;\,2{,}9)$. Để biết dãy này có tiến tới $v_{\pi_0}$ hay không và nhanh đến mức nào, chúng ta cần đo khoảng cách giữa hai bảng và xem $T_{\pi_0}$ thay đổi khoảng cách đó ra sao. Vì một bảng giá trị chỉ tốt khi nó tốt ở mọi trạng thái, ta đo khoảng cách bằng độ chênh lệch lớn nhất trên các trạng thái.

::: example Ví dụ 04.4 (Khoảng cách giữa hai bảng giảm sau một lần áp dụng $T_{\pi_0}$)
**Dữ kiện.** Mô hình hai trạng thái như Ví dụ 04.2, $\gamma=0{,}9$, chính sách $\pi_0=(\mathrm a,\mathrm a)$, nên $(T_{\pi_0}V)(\mathrm s_0)=1+0{,}9V(\mathrm s_0)$ và $(T_{\pi_0}V)(\mathrm s_1)=2+0{,}9V(\mathrm s_0)$. Hai bảng $U=(10,11)$ và $V=(0,0)$; đây là số liệu sư phạm tự xây dựng.

**Khoảng cách ban đầu.** Chênh lệch là $10$ tại $\mathrm s_0$ và $11$ tại $\mathrm s_1$; độ chênh lớn nhất là $11$.

**Sau một lần áp dụng.**

$$
T_{\pi_0}U=(1+9,\;2+9)=(10,11),\qquad T_{\pi_0}V=(1,2).
$$

Chênh lệch mới là $9$ tại cả hai trạng thái, nên độ chênh lớn nhất là $9$.

**Diễn giải.** Phần thưởng triệt tiêu khi lấy hiệu; chỉ còn $0{,}9$ nhân chênh lệch cũ tại $\mathrm s_0$: $0{,}9\cdot10=9$. Bảng $U$ không đổi dưới $T_{\pi_0}$, tức $T_{\pi_0}U=U$; Ví dụ 04.5 cho thấy $U=v_{\pi_0}$.

**Kiểm tra lại.** $9\le0{,}9\cdot11=9{,}9$; dấu bằng không xảy ra vì $\mathrm s_0$ không phải nơi chênh lệch cũ lớn nhất.
:::

::: definition Định nghĩa 04.3 (Chuẩn vô cùng, ánh xạ co)
**Chuẩn vô cùng.** Với $U\in\mathbb R^n$, chuẩn vô cùng (sup norm) là $\lVert U\rVert_\infty=\max_{s\in\mathcal S}\lvert U(s)\rvert$; khoảng cách giữa hai bảng $U,V$ là $\lVert U-V\rVert_\infty$.

**Ánh xạ co.** Ánh xạ $F:\mathbb R^n\to\mathbb R^n$ là ánh xạ co (contraction) với hệ số $\beta\in[0,1)$ theo chuẩn vô cùng nếu $\lVert FU-FV\rVert_\infty\le\beta\lVert U-V\rVert_\infty$ với mọi $U,V\in\mathbb R^n$.
:::

Chuẩn vô cùng đo sai số xấu nhất trên các trạng thái: $\lVert V-v_\pi\rVert_\infty\le0{,}1$ nghĩa là $V$ lệch giá trị thật không quá $0{,}1$ tại mọi trạng thái. Một ánh xạ co kéo mọi cặp bảng lại gần nhau theo cùng một tỉ lệ $\beta$. Ánh xạ $F(V)=2V$ trên $\mathbb R$ nhân đôi mọi khoảng cách nên không co; $F(V)=V+1$ giữ nguyên khoảng cách, không co và không có điểm bất động. Ví dụ 04.4 là một trường hợp của mệnh đề sau.

::: proposition Mệnh đề 04.4 ($T_\pi$ là ánh xạ co)
**Giả thiết.** MDP hữu hạn; $0\le\gamma<1$; $\pi$ là chính sách Markov dừng.

**Kết luận.** Với mọi $U,V\in\mathbb R^n$,

$$
\lVert T_\pi U-T_\pi V\rVert_\infty\le\gamma\,\lVert U-V\rVert_\infty .
$$

**Điều kiện áp dụng.** Các trọng số $\pi(a\mid s)$ và $p(s',r\mid s,a)$ không âm, tổng theo hành động và theo kết quả chuyển đều bằng $1$; giá trị tại $s_{\mathrm{term}}$ của mọi bảng bằng $0$.

**Phạm vi.** Hệ số co là $\gamma$ theo chuẩn vô cùng. Khi $\gamma=1$, bất đẳng thức vẫn đúng nhưng không còn là tính co.
:::

::: proof Chứng minh Mệnh đề 04.4
**Bước 1 (hiệu tại một trạng thái).** Cố định $s\in\mathcal S$. Như trong chứng minh Bổ đề 04.2, phần thưởng triệt tiêu và

$$
(T_\pi U)(s)-(T_\pi V)(s)=\gamma\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\bigl[U(s')-V(s')\bigr].
$$

**Bước 2 (chặn trị tuyệt đối).** Lấy trị tuyệt đối hai vế:

$$
\begin{aligned}
\bigl\lvert(T_\pi U)(s)-(T_\pi V)(s)\bigr\rvert
&\le\gamma\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\,\bigl\lvert U(s')-V(s')\bigr\rvert &&\text{(i)}\\
&\le\gamma\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\,\lVert U-V\rVert_\infty &&\text{(ii)}\\
&=\gamma\,\lVert U-V\rVert_\infty &&\text{(iii)}.
\end{aligned}
$$

Bước (i) là bất đẳng thức tam giác, dùng được vì mọi trọng số không âm; bước (ii) dùng định nghĩa chuẩn vô cùng, với hiệu tại $s_{\mathrm{term}}$ bằng $0$; bước (iii) dùng tổng các trọng số theo hành động và theo kết quả chuyển đều bằng $1$.

**Bước 3 (lấy cực đại).** Bất đẳng thức của Bước 2 đúng với mọi $s\in\mathcal S$, nên cực đại theo $s$ của vế trái, tức $\lVert T_\pi U-T_\pi V\rVert_\infty$, cũng không vượt $\gamma\lVert U-V\rVert_\infty$. $\square$
:::

Chứng minh dùng hai sự kiện về trọng số: chúng không âm và có tổng bằng $1$, nên trung bình của các chênh lệch không vượt chênh lệch lớn nhất. Hệ số $\gamma$ xuất hiện vì mỗi lần áp dụng toán tử, chênh lệch bị đẩy lùi một bước và chiết khấu thêm một lần.

Tính co tự nó chưa nói dãy $V_{k+1}=T_\pi V_k$ có giới hạn. Định lý sau, định lý điểm bất động Banach, cung cấp phần còn thiếu; ở đây ta chỉ cần nó trên $\mathbb R^n$ với chuẩn vô cùng.

::: theorem Định lý 04.5 (Điểm bất động của ánh xạ co trên $\mathbb R^n$)
**Giả thiết.** $F:\mathbb R^n\to\mathbb R^n$ là ánh xạ co với hệ số $\beta\in[0,1)$ theo chuẩn vô cùng.

**Kết luận.**

- (a) $F$ có đúng một điểm bất động $\bar V$, tức $F\bar V=\bar V$.
- (b) Với mọi $V_0\in\mathbb R^n$, dãy $V_{k+1}=FV_k$ hội tụ về $\bar V$ và $\lVert V_k-\bar V\rVert_\infty\le\beta^k\lVert V_0-\bar V\rVert_\infty$ với mọi $k\ge0$.

**Điều kiện áp dụng.** Hệ số $\beta$ nhỏ hơn $1$ và không phụ thuộc cặp bảng; không gian là $\mathbb R^n$ với $n$ hữu hạn.

**Phạm vi.** Định lý phát biểu cho $\mathbb R^n$; dạng tổng quát cho không gian mêtric đầy đủ nằm ngoài nhu cầu của chương. Định lý không cho biết $\bar V$ bằng bao nhiêu; nó chỉ bảo đảm tồn tại, duy nhất và tốc độ hội tụ.
:::

::: proof Chứng minh Định lý 04.5
**Bước 1 (duy nhất).** Giả sử $FX=X$ và $FY=Y$. Khi đó $\lVert X-Y\rVert_\infty=\lVert FX-FY\rVert_\infty\le\beta\lVert X-Y\rVert_\infty$, nên $(1-\beta)\lVert X-Y\rVert_\infty\le0$. Vì $1-\beta>0$, ta có $\lVert X-Y\rVert_\infty=0$, tức $X=Y$.

**Bước 2 (dãy lặp có giới hạn).** Áp dụng tính co $j$ lần cho cặp $(V_1,V_0)$ được $\lVert V_{j+1}-V_j\rVert_\infty\le\beta^j\lVert V_1-V_0\rVert_\infty$. Với $l>k$,

$$
\begin{aligned}
\lVert V_l-V_k\rVert_\infty
&\le\sum_{j=k}^{l-1}\lVert V_{j+1}-V_j\rVert_\infty &&\text{(bất đẳng thức tam giác)}\\
&\le\lVert V_1-V_0\rVert_\infty\sum_{j=k}^{l-1}\beta^j &&\text{(tính co, } j \text{ lần)}\\
&\le\frac{\beta^k}{1-\beta}\lVert V_1-V_0\rVert_\infty &&\text{(tổng cấp số nhân, } 0\le\beta<1).
\end{aligned}
$$

Vế phải tiến về $0$, nên với mỗi $s$, dãy số thực $V_k(s)$ là dãy Cauchy, do đó hội tụ; đặt $\bar V(s)=\lim_kV_k(s)$. Vì chỉ có $n$ trạng thái, $\lVert V_k-\bar V\rVert_\infty\to0$.

**Bước 3 (giới hạn là điểm bất động).** Với mọi $k$,

$$
\begin{aligned}
\lVert F\bar V-\bar V\rVert_\infty
&\le\lVert F\bar V-FV_k\rVert_\infty+\lVert V_{k+1}-\bar V\rVert_\infty &&\text{(bất đẳng thức tam giác, } FV_k=V_{k+1})\\
&\le\beta\lVert\bar V-V_k\rVert_\infty+\lVert V_{k+1}-\bar V\rVert_\infty &&\text{(tính co)}.
\end{aligned}
$$

Vế phải tiến về $0$ theo Bước 2, còn vế trái không phụ thuộc $k$, nên $F\bar V=\bar V$. Cùng với Bước 1, ta có (a).

**Bước 4 (tốc độ).** $\lVert V_k-\bar V\rVert_\infty=\lVert FV_{k-1}-F\bar V\rVert_\infty\le\beta\lVert V_{k-1}-\bar V\rVert_\infty$; lặp lại $k$ lần cho (b). $\square$
:::

Định lý 04.5 cần hai giả thiết, và mỗi giả thiết bị bỏ đều có phản ví dụ.

- Bỏ $\beta<1$: ánh xạ $F(V)=V+1$ trên $\mathbb R$ thỏa bất đẳng thức với $\beta=1$ nhưng không có điểm bất động; ánh xạ $F(V)=V$ có vô số điểm bất động.
- Bỏ một hệ số chung cho mọi cặp bảng: ánh xạ $F(V)=\sqrt{V^2+1}$ trên $\mathbb R$ thỏa $\lvert F(x)-F(y)\rvert=\lvert x-y\rvert\,\dfrac{\lvert x+y\rvert}{\sqrt{x^2+1}+\sqrt{y^2+1}}<\lvert x-y\rvert$ khi $x\ne y$, tức mọi khoảng cách giảm nghiêm ngặt, nhưng tỉ lệ giảm tiến về $1$ khi $x,y\to\infty$ nên không có $\beta<1$ chung. Ánh xạ này không có điểm bất động vì $F(V)>\lvert V\rvert\ge V$.

Bước 1 và Bước 2 của chứng minh dùng $1-\beta>0$; Bước 2 còn dùng tính chất mọi dãy Cauchy số thực hội tụ và số trạng thái hữu hạn.

Ghép Mệnh đề 04.4 với Định lý 04.5 cho câu trả lời đầy đủ về đánh giá chính sách; phần (c) dưới đây nhắc lại kết quả về hệ tuyến tính của Bài 03.

::: corollary Hệ quả 04.6 (Nghiệm của bài toán đánh giá chính sách)
**Giả thiết.** MDP hữu hạn với phần thưởng bị chặn; $0\le\gamma<1$; $\pi$ là chính sách Markov dừng.

**Kết luận.**

- (a) $v_\pi$ là nghiệm duy nhất trong $\mathbb R^n$ của phương trình $V=T_\pi V$.
- (b) Với mọi $V_0\in\mathbb R^n$, các lượt quét đồng bộ $V_{k+1}=T_\pi V_k$ hội tụ về $v_\pi$ và $\lVert V_k-v_\pi\rVert_\infty\le\gamma^k\lVert V_0-v_\pi\rVert_\infty$.
- (c) Đặt $P_\pi(s,s')=\sum_a\pi(a\mid s)\sum_rp(s',r\mid s,a)$ với $s,s'\in\mathcal S$ và $r_\pi(s)=\sum_a\pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\,r$. Ma trận $I-\gamma P_\pi$ khả nghịch và $v_\pi=(I-\gamma P_\pi)^{-1}r_\pi$.

**Điều kiện áp dụng.** Mô hình $p$ được biết đầy đủ; chính sách giữ cố định trong suốt phép tính.

**Phạm vi.** $P_\pi$ chỉ gồm trạng thái chưa kết thúc; tổng mỗi hàng có thể nhỏ hơn $1$.
:::

::: proof Chứng minh Hệ quả 04.6
**Bước 1 ($v_\pi$ là điểm bất động).** Theo Mệnh đề 03.11 (ghi chú Bài 03, Mục 2), $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$, nên $v_\pi$ là một bảng số hữu hạn trong $\mathbb R^n$. Theo phương trình Bellman kỳ vọng (Định lý 03.21, ghi chú Bài 03, Mục 4), $v_\pi=T_\pi v_\pi$.

**Bước 2 ((a) và (b)).** Theo Mệnh đề 04.4, $T_\pi$ là ánh xạ co với hệ số $\gamma<1$. Định lý 04.5(a) cho $T_\pi$ đúng một điểm bất động, và theo Bước 1 điểm đó là $v_\pi$. Định lý 04.5(b) với $F=T_\pi$, $\beta=\gamma$ cho (b).

**Bước 3 (dạng ma trận).** Tách (1.1) thành phần thưởng và phần tiếp nối; số hạng ứng với $s'=s_{\mathrm{term}}$ trong phần tiếp nối bằng $0$:

$$
(T_\pi V)(s)=r_\pi(s)+\gamma\sum_{s'\in\mathcal S}P_\pi(s,s')V(s'),\qquad\text{tức}\qquad T_\pi V=r_\pi+\gamma P_\pi V .
$$

**Bước 4 (kết luận (c)).** Theo Định lý 03.28(a) (ghi chú Bài 03, Mục 5), $I-\gamma P_\pi$ khả nghịch khi $0\le\gamma<1$. Từ $v_\pi=r_\pi+\gamma P_\pi v_\pi$ (Bước 1 và Bước 3) ta được $(I-\gamma P_\pi)v_\pi=r_\pi$; nhân hai vế với $(I-\gamma P_\pi)^{-1}$ cho (c). $\square$
:::

Hệ quả 04.6 nói rằng $v_\pi$ tính được bằng hai con đường. Con đường thứ nhất giải một hệ tuyến tính $n$ ẩn; con đường thứ hai lặp toán tử $T_\pi$ từ một bảng bất kỳ. Con đường thứ hai dùng lại được cho toán tử tối ưu ở Mục 4, nơi không còn hệ tuyến tính để giải.

::: example Ví dụ 04.5 (Giá trị chính xác của $\pi_0$ và sai số của các lượt quét)
**Dữ kiện.** Mô hình hai trạng thái, $\gamma=0{,}9$, $\pi_0=(\mathrm a,\mathrm a)$: từ cả hai trạng thái, $\mathrm a$ dẫn về $\mathrm s_0$, với phần thưởng $1$ tại $\mathrm s_0$ và $2$ tại $\mathrm s_1$. Các lượt quét từ $V_0=(0,0)$ cho $V_1=(1,2)$, $V_2=(1{,}9;\,2{,}9)$ (Ví dụ 04.2).

**Hệ tuyến tính.** Với $x=v_{\pi_0}(\mathrm s_0)$, $y=v_{\pi_0}(\mathrm s_1)$, phương trình $v_{\pi_0}=T_{\pi_0}v_{\pi_0}$ là

$$
\begin{aligned}
x&=1+0{,}9x,\\
y&=2+0{,}9x.
\end{aligned}
$$

Phương trình thứ nhất chỉ chứa $x$ vì $\mathrm a$ đưa $\mathrm s_0$ về chính nó: $0{,}1x=1$, nên $x=10$. Thế vào phương trình thứ hai, ta được $y=2+9=11$. Vậy $v_{\pi_0}=(10,11)$, chính là bảng $U$ không đổi dưới $T_{\pi_0}$ trong Ví dụ 04.4.

**Sai số của các lượt quét.** Quy nạp theo $k$ từ $V_0=(0,0)$ cho $V_k(\mathrm s_0)=10(1-0{,}9^k)$ và $V_k(\mathrm s_1)=2+0{,}9V_{k-1}(\mathrm s_0)=11-10\cdot0{,}9^k$ với $k\ge1$. Do đó

$$
\lVert V_k-v_{\pi_0}\rVert_\infty=10\cdot0{,}9^k\quad(k\ge1).
$$

**Đối chiếu với Hệ quả 04.6(b).** Chặn là $0{,}9^k\lVert V_0-v_{\pi_0}\rVert_\infty=11\cdot0{,}9^k$, lớn hơn sai số thật $10\cdot0{,}9^k$; chặn đúng nhưng không chặt trong ví dụ này.

**Kiểm tra lại.** $k=2$: $10\cdot0{,}81=8{,}1$, khớp $10-1{,}9=8{,}1$ và $11-2{,}9=8{,}1$.
:::

Sau hai lượt quét, sai số vẫn là $8{,}1$; với $\gamma$ gần $1$, hệ số co gần $1$ và dãy hội tụ chậm.

Mỗi giả thiết của Hệ quả 04.6 bị bỏ đều có phản ví dụ trên cùng mô hình.

- Bỏ $\gamma<1$: với $\gamma=1$, lượt quét cho $V_k=(k,\,k+1)$ với $k\ge1$, tăng không giới hạn vì tác tử nhận phần thưởng $1$ mãi mãi tại $\mathrm s_0$. Mọi chính sách có lợi tức vô hạn, vì mọi phần thưởng không âm và trong hai bước liên tiếp luôn có ít nhất một phần thưởng dương, nên phép so sánh giá trị mất nghĩa. Toán tử $T_{\pi_0}$ không còn co: $T_{\pi_0}(V+c\mathbf 1)=T_{\pi_0}V+c\mathbf 1$ với $\mathbf 1$ là bảng bằng $1$ ở mọi trạng thái. Bỏ chiết khấu chỉ dùng được khi có giả thiết thay thế, chẳng hạn mọi chính sách tới trạng thái kết thúc với xác suất $1$ (mục Đọc thêm).
- Bỏ chính sách cố định: nếu $\pi$ thay đổi giữa các lượt quét, mỗi lượt quét áp dụng một toán tử khác, và Định lý 04.5 không còn nói gì về dãy thu được.

**Trong thực hành.** Bảng $V$ là một mảng $n$ phần tử, cộng một phần tử bằng $0$ cho $s_{\mathrm{term}}$. Trong bài thực hành CartPole, $n=324$ ô, mô hình ước lượng là mảng cỡ $(2,324,325)$ với ba trục là hành động, ô hiện tại và ô kế tiếp kể cả $s_{\mathrm{term}}$, và Hệ quả 04.6(c) được thực hiện bằng một lời gọi giải hệ với chi phí $O(n^3)$. Một lần chạy đã nhúng trong notebook cho $\lVert T_\pi v-v\rVert_\infty=2{,}1\cdot10^{-14}$ tại nghiệm $v$ tìm được, tức nghiệm thỏa (1.2) tới sai số làm tròn. Các bảo đảm của Hệ quả 04.6 thuộc về MDP 324 ô đã ước lượng; khoảng cách tới CartPole liên tục được xét ở Mục 5.4.

<!-- note-topic-id: lec-04-part-08 -->
### 1.4 Phần dư Bellman và thuật toán đánh giá chính sách

Hệ quả 04.6(b) cho biết sai số giảm theo $\gamma^k$, nhưng chặn chứa $v_\pi$, chính đại lượng chưa biết. Trong Ví dụ 04.5, chúng ta đo được sai số thật chỉ vì mô hình đủ nhỏ để giải hệ bằng tay. Để quyết định khi nào dừng các lượt quét, chúng ta cần một đại lượng tính được từ bảng hiện có. Đại lượng tự nhiên là mức thay đổi của bảng sau một lần áp dụng toán tử: trong Ví dụ 04.2, bảng thay đổi $2$ ở lượt quét thứ nhất và $0{,}9$ ở lượt quét thứ hai.

::: definition Định nghĩa 04.7 (Phần dư Bellman đối với $T_\pi$)
Cho MDP hữu hạn, $\gamma\in[0,1)$ và chính sách Markov dừng $\pi$. Phần dư Bellman (Bellman residual) của bảng $V\in\mathbb R^n$ đối với $T_\pi$ là

$$
\Delta_\pi(V)=\lVert T_\pi V-V\rVert_\infty .
$$
:::

Phần dư đo mức bảng $V$ không thỏa phương trình $V=T_\pi V$; nó bằng $0$ khi và chỉ khi $V=v_\pi$ (Hệ quả 04.6(a)). Với lượt quét đồng bộ, $\Delta_\pi(V_k)=\lVert V_{k+1}-V_k\rVert_\infty$, tức mức thay đổi ở lượt quét kế tiếp. Phần dư khác sai số $\lVert V-v_\pi\rVert_\infty$; nhầm hai đại lượng dẫn tới dừng quá sớm khi $\gamma$ gần $1$.

::: example Ví dụ 04.6 (Phần dư và sai số thật của $V_1$)
**Dữ kiện.** Mô hình hai trạng thái, $\gamma=0{,}9$, $\pi_0=(\mathrm a,\mathrm a)$; $V_1=(1,2)$, $T_{\pi_0}V_1=V_2=(1{,}9;\,2{,}9)$ (Ví dụ 04.2); $v_{\pi_0}=(10,11)$ (Ví dụ 04.5).

**Phần dư.** $\Delta_{\pi_0}(V_1)=\max\{\lvert1{,}9-1\rvert,\ \lvert2{,}9-2\rvert\}=\max\{0{,}9;\ 0{,}9\}=0{,}9$.

**Sai số thật.** $\lVert V_1-v_{\pi_0}\rVert_\infty=\max\{\lvert1-10\rvert,\ \lvert2-11\rvert\}=9$.

**Diễn giải.** Sai số thật bằng phần dư nhân $1/(1-\gamma)=10$; hệ quả sau chỉ ra rằng sai số không bao giờ vượt tích này.

**Kiểm tra lại.** $0{,}9/(1-0{,}9)=9$, đúng bằng sai số thật.
:::

::: corollary Hệ quả 04.8 (Chặn sai số theo phần dư)
**Giả thiết.** Như Hệ quả 04.6; $V\in\mathbb R^n$ là một bảng bất kỳ.

**Kết luận.**

- (a) $\lVert V-v_\pi\rVert_\infty\le\dfrac{\Delta_\pi(V)}{1-\gamma}$.
- (b) $\lVert T_\pi V-v_\pi\rVert_\infty\le\dfrac{\gamma\,\Delta_\pi(V)}{1-\gamma}$.
- (c) Với sai số cho phép $\kappa>0$, nếu $\Delta_\pi(V)\le\theta$ với $\theta=(1-\gamma)\kappa$ thì $\lVert V-v_\pi\rVert_\infty\le\kappa$.

**Điều kiện áp dụng.** Phần dư phải được đo trên chính bảng được dùng làm kết quả; chặn (a) thuộc về $V$, chặn (b) thuộc về bảng mới $T_\pi V$.

**Phạm vi.** Chặn chỉ cho cận trên; sai số thật có thể nhỏ hơn nhiều. Với $\gamma=1$ mẫu số bằng $0$ và kết luận mất nghĩa.
:::

::: proof Chứng minh Hệ quả 04.8
**Bước 1 (tách sai số).** Vì $v_\pi=T_\pi v_\pi$ (Hệ quả 04.6(a)),

$$
\begin{aligned}
\lVert V-v_\pi\rVert_\infty
&\le\lVert V-T_\pi V\rVert_\infty+\lVert T_\pi V-T_\pi v_\pi\rVert_\infty &&\text{(bất đẳng thức tam giác)}\\
&\le\Delta_\pi(V)+\gamma\lVert V-v_\pi\rVert_\infty &&\text{(Định nghĩa 04.7, Mệnh đề 04.4)}.
\end{aligned}
$$

**Bước 2 (chuyển vế).** Chuyển $\gamma\lVert V-v_\pi\rVert_\infty$ sang vế trái được $(1-\gamma)\lVert V-v_\pi\rVert_\infty\le\Delta_\pi(V)$; chia cho $1-\gamma>0$ cho (a).

**Bước 3 (bảng mới).** $\lVert T_\pi V-v_\pi\rVert_\infty=\lVert T_\pi V-T_\pi v_\pi\rVert_\infty\le\gamma\lVert V-v_\pi\rVert_\infty$ theo Mệnh đề 04.4; thay (a) vào cho (b).

**Bước 4 (ngưỡng).** Nếu $\Delta_\pi(V)\le(1-\gamma)\kappa$ thì theo (a), $\lVert V-v_\pi\rVert_\infty\le(1-\gamma)\kappa/(1-\gamma)=\kappa$. $\square$
:::

Hệ quả 04.8 đổi câu hỏi "bảng còn cách nghiệm bao xa" thành phép đo "bảng còn thay đổi bao nhiêu", với cái giá là thừa số $1/(1-\gamma)$: bằng $10$ khi $\gamma=0{,}9$ và $100$ khi $\gamma=0{,}99$. Ví dụ 04.6 cho thấy chặn (a) có thể đạt dấu bằng, nên thừa số này không giảm được cho mọi bài toán.

Đến đây chúng ta có đủ thành phần cho một thuật toán: quy tắc cập nhật (Định nghĩa 04.1), bảo đảm hội tụ (Hệ quả 04.6) và đại lượng dừng có chặn sai số (Hệ quả 04.8). Khi chạy thuật toán dưới đây trên mô hình hai trạng thái, hai lần lặp đầu cho các bảng của Ví dụ 04.2, và phép kiểm dừng tại $k=1$ là phép tính của Ví dụ 04.6.

::: algorithm Thuật toán 04.9 (Đánh giá chính sách đồng bộ có ngưỡng)
**Đầu vào.** Mô hình $p(s',r\mid s,a)$ của MDP hữu hạn; chính sách Markov dừng $\pi$; hệ số $\gamma\in[0,1)$.

**Đầu ra.** Bảng $V$, phần dư $\Delta_\pi(V)$ đo trên chính bảng đó, và nhãn "đạt ngưỡng" hoặc "hết ngân sách".

**Giả thiết.** Mô hình được biết đầy đủ; $\pi$ giữ cố định suốt thuật toán.

**Tham số.** Ngưỡng $\theta>0$, chọn $\theta=(1-\gamma)\kappa$ cho sai số cho phép $\kappa$; ngân sách $K\ge0$ là số lần nhận bảng mới tối đa.

**Khởi tạo.** $V(s)=0$ với mọi $s\in\mathcal S$; $V(s_{\mathrm{term}})=0$; bộ đếm $k=0$.

1. Giữ $V$ cố định, tính bảng tạm $W=T_\pi V$ theo (1.1) cho mọi $s\in\mathcal S$.
2. Đặt $\Delta=\lVert W-V\rVert_\infty$; đây là $\Delta_\pi(V)$.
3. Nếu $\Delta\le\theta$, trả $(V,\Delta)$ với nhãn "đạt ngưỡng".
4. Nếu $k=K$, trả $(V,\Delta)$ với nhãn "hết ngân sách".
5. Gán $V\leftarrow W$, $k\leftarrow k+1$, quay lại bước 1.

**Điều kiện dừng.** Bước 3 hoặc bước 4; với $\gamma<1$, Hệ quả 04.6(b) bảo đảm bước 3 xảy ra sau hữu hạn lần lặp khi $K$ đủ lớn.

**Chi phí mỗi bước.** Bước 1 duyệt mọi bộ $(s,a,s')$ có xác suất dương; với mô hình đặc lưu sẵn $p(s'\mid s,a)$ và $r(s,a)$, chi phí là $O(n^2m)$ phép tính và $O(n)$ bộ nhớ cho hai bảng $V$, $W$. Bước 2 tốn $O(n)$.
:::

Thuật toán trả $V$, bảng đã được đo phần dư, chứ không trả $W$. Như vậy chặn của Hệ quả 04.8(a) áp dụng đúng cho bảng trả về; nếu muốn trả $W$, chặn tương ứng là Hệ quả 04.8(b).

::: example Ví dụ 04.7 (Chạy Thuật toán 04.9 tới ngưỡng trên mô hình hai trạng thái)
**Dữ kiện.** Mô hình hai trạng thái, $\gamma=0{,}9$, $\pi_0=(\mathrm a,\mathrm a)$; từ $V_0=(0,0)$, lượt quét đồng bộ cho $V_k=\bigl(10(1-0{,}9^k),\ 11-10\cdot0{,}9^k\bigr)$ với $k\ge1$ (Ví dụ 04.5); $v_{\pi_0}=(10,11)$. Sai số cho phép $\kappa=0{,}1$; ngân sách $K=1000$.

**Ngưỡng.** $\theta=(1-0{,}9)\cdot0{,}1=0{,}01$.

**Phần dư theo $k$.** Với $k\ge1$, cả hai thành phần của $V_{k+1}-V_k$ bằng $10\cdot0{,}9^k(1-0{,}9)=0{,}9^k$, nên $\Delta_{\pi_0}(V_k)=0{,}9^k$; riêng $\Delta_{\pi_0}(V_0)=\lVert(1,2)\rVert_\infty=2$.

**Thời điểm dừng.** $0{,}9^{43}\approx0{,}0108>0{,}01$ và $0{,}9^{44}\approx0{,}0097\le0{,}01$. Thuật toán dừng ở $k=44$ với nhãn "đạt ngưỡng" và trả $V_{44}$.

**Kiểm tra lại.** Chặn của Hệ quả 04.8(a) là $0{,}9^{44}/0{,}1\approx0{,}097$, bằng sai số thật $10\cdot0{,}9^{44}$ và không vượt $\kappa=0{,}1$.
:::

::: remark Nhận xét 04.10 (Những điều Thuật toán 04.9 không làm)
- Thuật toán dùng lượt quét đồng bộ với hai bảng; cập nhật tại chỗ được xét ở Mục 5.
- Bước 1 dùng kỳ vọng đầy đủ theo $p$; khi chỉ có bộ mô phỏng sinh từng chuyển, Bài 05 thay kỳ vọng đó bằng mẫu.
- Trạng thái kết thúc giữ giá trị $0$. Một lượt tương tác kết thúc tại $s_{\mathrm{term}}$ là sự kiện của môi trường; thuật toán dừng ở bước 3 hoặc 4 là quyết định tính toán.
- Nhãn "hết ngân sách" chỉ báo rằng phép tính đã dừng; nó không chứng nhận sai số nào nhỏ hơn $\Delta/(1-\gamma)$. Một phần dư nhỏ cũng không phải sai số nhỏ khi $\gamma$ gần $1$.
:::

**Trong thực hành.** Bảng $V$ và bảng tạm $W$ là hai mảng cỡ $(n,)$; nhãn dừng được trả cùng bảng. Trong bài thực hành CartPole với $\gamma=0{,}99$ và $\kappa=0{,}01$, ngưỡng là $\theta=10^{-4}$. Một lần chạy đã nhúng trong notebook cho kết quả: với $K=10\,000$, thuật toán dừng sau $218$ lần nhận bảng với nhãn "đạt ngưỡng", chặn $9{,}605\cdot10^{-3}$ và sai số thật $2{,}197\cdot10^{-3}$; với $K=100$, nhãn là "hết ngân sách", chặn $1{,}845$ và sai số thật $0{,}4248$, lớn hơn $\kappa$. Cả hai lần chạy đều thỏa Hệ quả 04.8(a) trên MDP ước lượng.

::: exercise Bài tập 04.1 (Lượt quét thứ ba và chặn sai số)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_0=(\mathrm a,\mathrm a)$ và bảng $V_2=(1{,}9;\,2{,}9)$.

(a) Tính bảng đồng bộ $V_3=T_{\pi_0}V_2$.

(b) Tính $\Delta_{\pi_0}(V_2)$ và chặn sai số của $V_2$ theo Hệ quả 04.8(a).

(c) Biết $v_{\pi_0}=(10,11)$, so chặn ở (b) với sai số thật của $V_2$, và giải thích vì sao $V_3$ chưa phải $v_{\pi_0}$.
:::

::: hint
Theo $\pi_0$, cả hai trạng thái chọn $\mathrm a$ và $\mathrm a$ dẫn về $\mathrm s_0$; cả hai ô của $V_3$ đọc $V_2(\mathrm s_0)$. Phần dư của $V_2$ là $\lVert V_3-V_2\rVert_\infty$.
:::

::: solution
**(a)** $V_3(\mathrm s_0)=1+0{,}9\cdot1{,}9=2{,}71$ và $V_3(\mathrm s_1)=2+0{,}9\cdot1{,}9=3{,}71$, nên $V_3=(2{,}71;\,3{,}71)$.

**(b)** $V_3-V_2=(0{,}81;\,0{,}81)$, nên $\Delta_{\pi_0}(V_2)=0{,}81$. Chặn sai số là $0{,}81/(1-0{,}9)=8{,}1$.

**(c)** Sai số thật là $\max\{10-1{,}9;\ 11-2{,}9\}=8{,}1$, đúng bằng chặn. Bảng $V_3$ còn phần dư $\Delta_{\pi_0}(V_3)=0{,}9^3=0{,}729>0$, nên $V_3$ chưa thỏa $V=T_{\pi_0}V$; theo Hệ quả 04.6(a), chỉ $v_{\pi_0}$ thỏa phương trình đó.

**Kiểm tra lại.** Theo Ví dụ 04.5, $\lVert V_2-v_{\pi_0}\rVert_\infty=10\cdot0{,}9^2=8{,}1$.
:::

Như vậy, chúng ta đã có toán tử $T_\pi$ (Định nghĩa 04.1), tính co của nó (Mệnh đề 04.4), và từ định lý điểm bất động (Định lý 04.5) suy ra $v_\pi$ là nghiệm duy nhất, đạt được bằng các lượt quét với tốc độ $\gamma^k$ (Hệ quả 04.6). Phần dư Bellman (Định nghĩa 04.7) cho điều kiện dừng có chặn sai số (Hệ quả 04.8), và Thuật toán 04.9 ghép các thành phần đó lại. Tuy nhiên, giá trị $v_\pi$ chỉ nói một chính sách tốt đến đâu, chưa nói có nên đổi hành động hay không; trong Mục 2, chúng ta dùng nó làm giá trị tiếp nối để so sánh các hành động.

## 2. Cải thiện chính sách

Ở Mục 1, ta có $v_{\pi_0}=(10,11)$ nhưng chưa biết có nên đổi $\pi_0=(\mathrm a,\mathrm a)$. Tại $\mathrm s_1$, $\pi_0$ chọn $\mathrm a$ với phần thưởng $2$ rồi rời sang $\mathrm s_0$, còn $\mathrm b$ cho phần thưởng $3$ và giữ tác tử ở $\mathrm s_1$. Chúng ta cần đo giá trị dài hạn của từng hành động, rồi cần bảo đảm rằng đổi hành động theo phép đo đó không làm chính sách tệ đi ở trạng thái nào. Đây là bài toán điều khiển: chính sách được phép thay đổi.

<!-- note-topic-id: lec-04-part-02 -->
### 2.1 Giá trị nhìn trước một bước

Về mặt ý tưởng, để so sánh hai hành động tại $\mathrm s_1$, ta cho tác tử thử từng hành động đúng một lần, rồi từ trạng thái kế tiếp trở đi vẫn theo $\pi_0$. Phần sau bước đầu đã có giá trị biết trước, là $v_{\pi_0}$ của trạng thái kế tiếp, nên mỗi lựa chọn chỉ cần một phép cộng: phần thưởng của bước đầu cộng giá trị tiếp nối đã chiết khấu. Đây chưa phải định nghĩa; nó mô tả phép so sánh mà định nghĩa dưới đây sẽ làm chính xác.

![Từ nút s1 có hai nhánh. Nhánh "a / 2" đi tới s0, ghi "Giá trị: 10". Nhánh "b / 3" đi tới s1, ghi "Giá trị: 11". Nhãn chung: "Tiếp tục theo π0".](img/lec-04/dp04-one-step-choice.svg)

Hình trên vẽ hai nhánh xuất phát từ $\mathrm s_1$. Mỗi nhánh mang hành động và phần thưởng của bước đầu; nút cuối nhánh ghi giá trị tiếp nối đọc từ $v_{\pi_0}=(10,11)$. Nhãn "Tiếp tục theo $\pi_0$" nói rằng sau bước đầu, chính sách không đổi.

::: example Ví dụ 04.8 (Hai nhánh tại $\mathrm s_1$)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$, $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$, chuyển xác định; $\gamma=0{,}9$; $v_{\pi_0}=(10,11)$ với $\pi_0=(\mathrm a,\mathrm a)$ (Ví dụ 04.5).

**Nhánh $\mathrm a$ (giữ hành động cũ).** Phần thưởng $2$, tới $\mathrm s_0$ có giá trị tiếp nối $10$: $2+0{,}9\cdot10=11$.

**Nhánh $\mathrm b$ (đổi hành động).** Phần thưởng $3$, ở lại $\mathrm s_1$ có giá trị tiếp nối $11$: $3+0{,}9\cdot11=12{,}9$.

**Diễn giải.** Thử $\mathrm b$ một lần rồi theo $\pi_0$ cho $12{,}9$, lớn hơn $v_{\pi_0}(\mathrm s_1)=11$.

**Kiểm tra lại.** Nhánh của hành động cũ cho đúng $v_{\pi_0}(\mathrm s_1)=11$, vì thử hành động mà $\pi_0$ vốn chọn rồi theo $\pi_0$ chính là theo $\pi_0$.
:::

::: definition Định nghĩa 04.11 (Giá trị nhìn trước một bước)
Cho MDP hữu hạn, $\gamma\in[0,1)$ và bảng $V\in\mathbb R^n$ mở rộng bằng $V(s_{\mathrm{term}})=0$. Giá trị nhìn trước một bước (one-step lookahead) của hành động $a\in\mathcal A(s)$ tại $s\in\mathcal S$ tính từ $V$ là

$$
Q_V(s,a)=\sum_{s'\in\mathcal S^+,\,r\in\mathcal R}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr].
\tag{2.1}
$$
:::

Định nghĩa 04.11 làm chính xác phép tính của Ví dụ 04.8: hành động đầu được ấn định là $a$, kỳ vọng lấy theo kết quả chuyển của mô hình, và phần tiếp nối được đọc từ bảng $V$. Nó khác toán tử $T_\pi$ của Định nghĩa 04.1 ở chỗ không lấy trung bình theo hành động; hai đại lượng liên hệ bằng $(T_\pi V)(s)=\sum_a\pi(a\mid s)Q_V(s,a)$.

Khi $V=v_\pi$, phương trình Bellman cho giá trị hành động (Mệnh đề 03.22, ghi chú Bài 03, Mục 4) cho $Q_{v_\pi}(s,a)=q_\pi(s,a)$, kỳ vọng lợi tức khi chọn $a$ tại $s$ rồi theo $\pi$. Khi $V$ không phải giá trị của chính sách nào, chẳng hạn $V=(0,0)$, $Q_V$ vẫn tính được nhưng không là giá trị hành động của chính sách nào. Trong Ví dụ 04.8, $q_{\pi_0}(\mathrm s_1,\mathrm a)=11$ và $q_{\pi_0}(\mathrm s_1,\mathrm b)=12{,}9$.

Nhầm lẫn thường gặp ở đây là coi $12{,}9$ là giá trị tại $\mathrm s_1$ của chính sách mới chọn $\mathrm b$ tại $\mathrm s_1$. Số $12{,}9$ đo việc chọn $\mathrm b$ một lần rồi quay về $\pi_0$. Chính sách mới chọn $\mathrm b$ ở mọi lần ghé $\mathrm s_1$, nhận $3$ mãi mãi, nên giá trị của nó tại $\mathrm s_1$ là $3/(1-0{,}9)=30$, phải được tính bằng một lần đánh giá mới.

<!-- note-topic-id: lec-04-part-04 -->
### 2.2 Chính sách tham lam và định lý cải thiện

Ví dụ 04.8 mới xét một trạng thái. Để đổi chính sách, chúng ta tính giá trị nhìn trước tại mọi trạng thái và chọn hành động tốt nhất ở từng trạng thái.

::: example Ví dụ 04.9 (Một bước cải thiện từ $\pi_0$)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; $\gamma=0{,}9$; $\pi_0=(\mathrm a,\mathrm a)$, $v_{\pi_0}=(10,11)$, giữ cố định trong cả bước.

**Bốn giá trị nhìn trước.**

| Trạng thái | $q_{\pi_0}(s,\mathrm a)$ | $q_{\pi_0}(s,\mathrm b)$ | Hành động mới |
|---|---|---|---|
| $\mathrm s_0$ | $1+0{,}9\cdot10=10$ | $0+0{,}9\cdot11=9{,}9$ | $\mathrm a$ |
| $\mathrm s_1$ | $2+0{,}9\cdot10=11$ | $3+0{,}9\cdot11=12{,}9$ | $\mathrm b$ |

**Chọn.** Tại $\mathrm s_0$, $10>9{,}9$ nên giữ $\mathrm a$; tại $\mathrm s_1$, $12{,}9>11$ nên đổi sang $\mathrm b$. Chính sách mới là $\pi_1=(\mathrm a,\mathrm b)$.

**Kiểm tra lại.** Cột của hành động cũ $\mathrm a$ cho đúng $v_{\pi_0}=(10,11)$, vì $v_{\pi_0}=T_{\pi_0}v_{\pi_0}$.
:::

::: definition Định nghĩa 04.12 (Chính sách tham lam, quy tắc phá hòa)
Cho bảng $V\in\mathbb R^n$. Chính sách xác định $\pi'$ là tham lam (greedy) theo $V$ nếu

$$
\pi'(s)\in\arg\max_{a\in\mathcal A(s)}Q_V(s,a)\qquad\text{với mọi } s\in\mathcal S,
$$

trong đó $\arg\max$ là tập các hành động đạt cực đại. Khi tập này có nhiều phần tử, quy tắc phá hòa (tie-breaking) của chương là: nếu có chính sách cũ $\pi$ xác định và $\pi(s)$ thuộc tập cực đại thì giữ $\pi(s)$; nếu không, chọn phần tử đứng đầu trong một thứ tự cố định của $\mathcal A(s)$. Ký hiệu $\pi_V$ chỉ chính sách tham lam theo $V$ chọn bằng quy tắc này.
:::

Chính sách tham lam nhìn đúng một bước theo bảng $V$ và giao phần còn lại cho $V$. Tập $\mathcal A(s)$ hữu hạn nên $\arg\max$ khác rỗng. Phép $\max$ trả một con số, còn $\arg\max$ trả một tập; viết $\pi'(s)=\arg\max$ là sai khi có hòa. Ở Mục 3, quy tắc phá hòa giữ cho lặp chính sách không đổi qua lại giữa các hành động bằng giá trị.

Định lý sau cho biết vì sao đổi sang chính sách tham lam an toàn. Nó dùng tính đơn điệu (Bổ đề 04.2) để truyền một bất đẳng thức qua nhiều lần áp dụng toán tử, và Hệ quả 04.6(b) để chuyển qua giới hạn.

::: theorem Định lý 04.13 (Cải thiện chính sách)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$. $\pi$ là chính sách Markov dừng (có thể ngẫu nhiên) với giá trị chính xác $v_\pi$. $\pi'$ là chính sách Markov dừng xác định thỏa

$$
q_\pi\bigl(s,\pi'(s)\bigr)\ge v_\pi(s)\qquad\text{với mọi } s\in\mathcal S .
\tag{2.2}
$$

**Kết luận.**

- (a) $v_{\pi'}(s)\ge v_\pi(s)$ với mọi $s\in\mathcal S$.
- (b) Nếu (2.2) nghiêm ngặt tại một trạng thái $s$ thì $v_{\pi'}(s)>v_\pi(s)$.
- (c) Chính sách tham lam theo $v_\pi$ thỏa (2.2). Nếu thêm $\pi$ xác định, $\pi'=\pi_{v_\pi}$ chọn theo quy tắc phá hòa và $\pi'\ne\pi$, thì (2.2) nghiêm ngặt tại mọi trạng thái mà $\pi'(s)\ne\pi(s)$.

**Điều kiện áp dụng.** $v_\pi$ phải là giá trị chính xác của $\pi$, không phải một bảng gần đúng; $q_\pi$ trong (2.2) được tính từ $v_\pi$ theo (2.1).

**Phạm vi.** Định lý bảo đảm không kém đi, không bảo đảm $\pi'$ tối ưu, và không khẳng định tăng nghiêm ngặt ở mọi trạng thái.
:::

::: proof Chứng minh Định lý 04.13
**Bước 1 (bất đẳng thức đầu tiên).** Vì $\pi'$ xác định, tổng theo hành động trong (1.1) chỉ còn hành động $\pi'(s)$, nên $(T_{\pi'}v_\pi)(s)=Q_{v_\pi}(s,\pi'(s))=q_\pi(s,\pi'(s))$. Giả thiết (2.2) viết lại thành $v_\pi\le T_{\pi'}v_\pi$.

**Bước 2 (lặp bằng tính đơn điệu).** Giả sử $(T_{\pi'})^{j-1}v_\pi\le(T_{\pi'})^jv_\pi$ với một $j\ge1$. Áp dụng Bổ đề 04.2 cho toán tử $T_{\pi'}$ được $(T_{\pi'})^jv_\pi\le(T_{\pi'})^{j+1}v_\pi$. Quy nạp từ Bước 1 cho dãy không giảm

$$
\begin{aligned}
v_\pi&\le T_{\pi'}v_\pi &&\text{(Bước 1)}\\
&\le(T_{\pi'})^2v_\pi &&\text{(Bổ đề 04.2 áp dụng cho Bước 1)}\\
&\le\cdots\le(T_{\pi'})^kv_\pi &&\text{(quy nạp, Bổ đề 04.2)}.
\end{aligned}
$$

**Bước 3 (chuyển qua giới hạn).** Theo Hệ quả 04.6(b) áp dụng cho chính sách $\pi'$ với bảng khởi tạo $v_\pi$, $(T_{\pi'})^kv_\pi\to v_{\pi'}$. Bất đẳng thức không nghiêm ngặt giữa các số thực được giữ khi lấy giới hạn, nên $v_\pi(s)\le v_{\pi'}(s)$ với mọi $s$. Đây là (a).

**Bước 4 (tăng nghiêm ngặt).** Theo (a) và Bổ đề 04.2, $v_{\pi'}=T_{\pi'}v_{\pi'}\ge T_{\pi'}v_\pi$. Tại trạng thái $s$ mà (2.2) nghiêm ngặt,

$$
\begin{aligned}
v_{\pi'}(s)&\ge(T_{\pi'}v_\pi)(s) &&\text{(Bổ đề 04.2)}\\
&=q_\pi\bigl(s,\pi'(s)\bigr) &&\text{(Bước 1)}\\
&>v_\pi(s) &&\text{((2.2) nghiêm ngặt tại } s).
\end{aligned}
$$

Đây là (b).

**Bước 5 (chính sách tham lam).** Theo Mệnh đề 03.23 (ghi chú Bài 03, Mục 4), $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$, một trung bình có trọng số không âm, tổng trọng số bằng $1$, nên không vượt $\max_aq_\pi(s,a)=q_\pi(s,\pi'(s))$. Vậy chính sách tham lam thỏa (2.2). Khi $\pi$ xác định và $\pi'(s)\ne\pi(s)$, quy tắc phá hòa chỉ đổi hành động khi $\pi(s)$ không thuộc tập cực đại, nên $q_\pi(s,\pi'(s))>q_\pi(s,\pi(s))=v_\pi(s)$. Đây là (c). $\square$
:::

Mỗi giả thiết của Định lý 04.13 có vai trò riêng.

- Bỏ "giá trị chính xác": lấy $\pi=(\mathrm b,\mathrm b)$, có hệ $x=0{,}9y$, $y=3+0{,}9y$ nên $v_\pi=(27,30)$, nhưng thay $v_\pi$ bằng bảng gần đúng $V=(0,0)$. Các giá trị nhìn trước là $1$ và $0$ tại $\mathrm s_0$; $2$ và $3$ tại $\mathrm s_1$, nên chính sách tham lam là $(\mathrm a,\mathrm b)$. Hệ của $(\mathrm a,\mathrm b)$ là $x=1+0{,}9x$, $y=3+0{,}9y$, cho giá trị $(10,30)$: giá trị tại $\mathrm s_0$ giảm từ $27$ xuống $10$.
- Bỏ $\gamma<1$: Bước 3 cần Hệ quả 04.6(b), không còn đúng khi $\gamma=1$ (đoạn sau Ví dụ 04.5).
- Bỏ điều kiện (2.2) tại một trạng thái: từ $\pi_0=(\mathrm a,\mathrm a)$, đổi $\mathrm s_0$ sang $\mathrm b$ dù $q_{\pi_0}(\mathrm s_0,\mathrm b)=9{,}9<10$ cho $(\mathrm b,\mathrm a)$; hệ $x=0{,}9y$, $y=2+0{,}9x$ cho $x=1{,}8/0{,}19\approx9{,}47$, $y\approx10{,}53$, thấp hơn $(10,11)$ ở cả hai trạng thái.

Bước 1 dùng $\pi'$ xác định, Bước 2 dùng tính đơn điệu, Bước 3 là nơi duy nhất cần tính co và $\gamma<1$, và Bước 5 dùng phương trình Bellman kỳ vọng của Bài 03.

::: example Ví dụ 04.10 (Đánh giá lại sau cải thiện)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Từ Ví dụ 04.9, $\pi_1=(\mathrm a,\mathrm b)$ là chính sách tham lam theo $v_{\pi_0}=(10,11)$, với (2.2) nghiêm ngặt tại $\mathrm s_1$ ($12{,}9>11$) và đẳng thức tại $\mathrm s_0$.

**Tính.** Với $x=v_{\pi_1}(\mathrm s_0)$, $y=v_{\pi_1}(\mathrm s_1)$, hệ $v_{\pi_1}=T_{\pi_1}v_{\pi_1}$ là $x=1+0{,}9x$ và $y=3+0{,}9y$, nên $v_{\pi_1}=(10,30)$. Đối chiếu với $v_{\pi_0}=(10,11)$: giá trị tăng nghiêm ngặt tại $\mathrm s_1$ và giữ nguyên tại $\mathrm s_0$, vì đường đi từ $\mathrm s_0$ theo $\mathrm a$ không tới $\mathrm s_1$.

**Kiểm tra lại.** Thế vào hệ: $1+0{,}9\cdot10=10$ và $3+0{,}9\cdot30=30$. Bảng $(10,30)\ge(10,11)$, nghiêm ngặt tại $\mathrm s_1$, như Định lý 04.13(a)–(b).
:::

Ví dụ 04.10 cho thấy định lý chỉ bảo đảm không kém đi: từ $\pi_0$, một bước cải thiện tới $(\mathrm a,\mathrm b)$, chưa tới chính sách tốt nhất tìm được ở Mục 3.

Thuật toán sau viết phép tính của Ví dụ 04.9 thành quy trình cho một mô hình bất kỳ.

::: algorithm Thuật toán 04.14 (Cải thiện chính sách tham lam)
**Đầu vào.** Mô hình $p$; hệ số $\gamma\in[0,1)$; chính sách xác định $\pi$ và giá trị chính xác $v_\pi$ của nó.

**Đầu ra.** Chính sách xác định $\pi'$ và cờ "ổn định" nếu $\pi'=\pi$.

**Giả thiết.** $v_\pi$ là giá trị chính xác của $\pi$; trong suốt thuật toán $v_\pi$ giữ cố định.

**Tham số.** Một thứ tự cố định trên mỗi $\mathcal A(s)$ cho quy tắc phá hòa.

**Khởi tạo.** Cờ "ổn định" được bật.

1. Với mỗi $s\in\mathcal S$, tính $Q_{v_\pi}(s,a)$ theo (2.1) cho mọi $a\in\mathcal A(s)$.
2. Với mỗi $s$: nếu $\pi(s)\in\arg\max_aQ_{v_\pi}(s,a)$, đặt $\pi'(s)=\pi(s)$; nếu không, đặt $\pi'(s)$ là phần tử đầu tiên của $\arg\max$ theo thứ tự cố định và tắt cờ "ổn định".
3. Trả $\pi'$ và cờ.

**Điều kiện dừng.** Thuật toán dừng sau một lượt qua mọi trạng thái.

**Chi phí mỗi bước.** Bước 1 có cùng chi phí với một lượt quét của Thuật toán 04.9 nhưng cho mọi hành động: $O(n^2m)$ với mô hình đặc; bộ nhớ $O(nm)$ nếu lưu mọi $Q_{v_\pi}(s,a)$, hoặc $O(n)$ nếu chỉ giữ cực đại hiện tại khi duyệt hành động.
:::

::: remark Nhận xét 04.15 (Bước cải thiện không kết thúc bài toán điều khiển)
Thuật toán 04.14 trả chính sách mới cùng bảng $v_\pi$ của chính sách cũ: sau Ví dụ 04.9, bảng trong tay vẫn là $(10,11)$, trong khi $v_{\pi_1}=(10,30)$. Dùng tiếp $(10,11)$ để cải thiện $\pi_1$ là áp dụng Định lý 04.13 khi giả thiết "giá trị chính xác" không thỏa; phải đánh giá lại $\pi_1$ trước.
:::

**Trong thực hành.** Hai giá trị bằng nhau về lý thuyết có thể lệch nhau cỡ $10^{-13}$ do làm tròn, nên bài thực hành CartPole coi hành động cũ thuộc tập cực đại khi $Q(s,\pi(s))\ge\max_aQ(s,a)-10^{-9}$; không có dung sai này, quy tắc phá hòa có thể đổi qua lại giữa hai hành động đồng hạng. Một lần chạy đã nhúng trong notebook cho thấy bước cải thiện đầu tiên từ chính sách theo dấu góc, tức đẩy xe về phía cột đang nghiêng, đổi hành động tại $173$ trong $324$ ô, và giá trị cuối không nhỏ hơn giá trị ban đầu tại mọi ô, đúng như Định lý 04.13(a) trên MDP ước lượng.

::: exercise Bài tập 04.2 (Cải thiện từ $\pi_1$)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_1=(\mathrm a,\mathrm b)$ có giá trị chính xác $v_{\pi_1}=(10,30)$.

(a) Tính $q_{\pi_1}(\mathrm s_0,\mathrm a)$ và $q_{\pi_1}(\mathrm s_0,\mathrm b)$.

(b) Xác định hành động của chính sách tham lam tại $\mathrm s_0$ theo Định nghĩa 04.12.

(c) Giải thích vì sao lựa chọn tại $\mathrm s_0$ khác lựa chọn ở lần cải thiện từ $\pi_0$ trong Ví dụ 04.9.
:::

::: hint
Giá trị nhìn trước của $\mathrm b$ tại $\mathrm s_0$ đọc giá trị tiếp nối của $\mathrm s_1$ trong bảng $v_{\pi_1}$, không phải trong bảng $v_{\pi_0}$.
:::

::: solution
**(a)** $q_{\pi_1}(\mathrm s_0,\mathrm a)=1+0{,}9\cdot10=10$ và $q_{\pi_1}(\mathrm s_0,\mathrm b)=0+0{,}9\cdot30=27$.

**(b)** Hành động cũ $\pi_1(\mathrm s_0)=\mathrm a$ không thuộc $\arg\max=\{\mathrm b\}$, nên chính sách tham lam chọn $\mathrm b$ tại $\mathrm s_0$.

**(c)** Phần thưởng tức thời tại $\mathrm s_0$ không đổi: $\mathrm a$ vẫn cho $1$, $\mathrm b$ vẫn cho $0$. Giá trị tiếp nối của $\mathrm s_1$ tăng từ $11$ dưới $\pi_0$ lên $30$ dưới $\pi_1$, nên nhánh $\mathrm b$ tăng từ $9{,}9$ lên $27$ và vượt nhánh $\mathrm a$.

**Kiểm tra lại.** Tại $\mathrm s_1$, $q_{\pi_1}(\mathrm s_1,\mathrm a)=2+9=11<30=q_{\pi_1}(\mathrm s_1,\mathrm b)$, nên chính sách tham lam giữ $\mathrm b$ tại $\mathrm s_1$; chính sách mới là $(\mathrm b,\mathrm b)$.
:::

Như vậy, chúng ta đã có giá trị nhìn trước (Định nghĩa 04.11), chính sách tham lam với quy tắc phá hòa (Định nghĩa 04.12), và định lý cải thiện chính sách (Định lý 04.13) bảo đảm chính sách tham lam theo $v_\pi$ không kém $\pi$ ở trạng thái nào. Thuật toán 04.14 thực hiện bước này với chi phí của một lượt quét. Tuy nhiên, một bước cải thiện chỉ cho chính sách tốt hơn, chưa chắc tốt nhất; trong Mục 3, chúng ta lặp lại bước này.

<!-- note-topic-id: lec-04-part-09 -->
## 3. Lặp chính sách

Sau một bước cải thiện, $\pi_1=(\mathrm a,\mathrm b)$ có giá trị $(10,30)$, tốt hơn $(10,11)$. Bài tập 04.2 cho thấy cải thiện từ $v_{\pi_1}$ lại đổi hành động tại $\mathrm s_0$, vì giá trị tiếp nối của $\mathrm s_1$ đã tăng lên $30$. Chúng ta cần biết quá trình xen kẽ đánh giá và cải thiện có dừng hay không, và chính sách tại điểm dừng tốt đến đâu so với mọi chính sách.

### 3.1 Ba vòng trên mô hình hai trạng thái

Về mặt ý tưởng, lặp chính sách (policy iteration) luân phiên hai việc trên hai đối tượng khác nhau. Đánh giá giữ chính sách cố định và tính giá trị của nó; cải thiện giữ giá trị cố định và chọn lại hành động. Đây là mô tả, chưa phải thuật toán: chúng ta chưa nói khi nào dừng và dừng ở đâu.

![Chu trình hai khối. Khối trái "Chính sách πᵢ" dẫn sang khối "Đánh giá, πᵢ cố định", tạo "Giá trị chính xác". Khối "Cải thiện, giá trị cố định" tạo πᵢ₊₁; mũi tên quay lại ghi "Chính sách mới được đánh giá lại".](img/lec-04/dp04-policy-iteration.svg)

Trên hình, mỗi mũi tên ghi rõ đại lượng nào được giữ cố định. Chỉ số $i$ đếm vòng đánh giá–cải thiện, khác với $k$ đếm lượt quét bên trong một lần đánh giá bằng Thuật toán 04.9. Mũi tên quay lại nhắc rằng chính sách mới chưa có giá trị và phải được đánh giá trước lần cải thiện kế tiếp.

::: example Ví dụ 04.11 (Lặp chính sách trên mô hình hai trạng thái)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách khởi tạo $\pi_0=(\mathrm a,\mathrm a)$. Đánh giá giải chính xác hệ $v=T_\pi v$; cải thiện dùng Thuật toán 04.14 với thứ tự $\mathrm a$ trước $\mathrm b$.

**Vòng $i=0$.** $v_{\pi_0}=(10,11)$ (Ví dụ 04.5); cải thiện cho $\pi_1=(\mathrm a,\mathrm b)$ (Ví dụ 04.9).

**Vòng $i=1$.** $v_{\pi_1}=(10,30)$ (Ví dụ 04.10); cải thiện cho $\pi_2=(\mathrm b,\mathrm b)$ (Bài tập 04.2).

**Vòng $i=2$.** Với $x=v_{\pi_2}(\mathrm s_0)$, $y=v_{\pi_2}(\mathrm s_1)$: $x=0+0{,}9y$ và $y=3+0{,}9y$, nên $y=30$, $x=27$. Bốn giá trị nhìn trước từ $(27,30)$:

$$
\begin{aligned}
q_{\pi_2}(\mathrm s_0,\mathrm a)&=1+0{,}9\cdot27=25{,}3, & q_{\pi_2}(\mathrm s_0,\mathrm b)&=0+0{,}9\cdot30=27,\\
q_{\pi_2}(\mathrm s_1,\mathrm a)&=2+0{,}9\cdot27=26{,}3, & q_{\pi_2}(\mathrm s_1,\mathrm b)&=3+0{,}9\cdot30=30.
\end{aligned}
$$

Tại cả hai trạng thái, hành động đang chọn $\mathrm b$ đạt cực đại, nên cải thiện trả lại $\pi_2$ và thuật toán dừng.

| Vòng $i$ | Chính sách $\pi_i$ | Giá trị $v_{\pi_i}$ | Sau cải thiện |
|---|---|---|---|
| $0$ | $(\mathrm a,\mathrm a)$ | $(10,11)$ | $(\mathrm a,\mathrm b)$ |
| $1$ | $(\mathrm a,\mathrm b)$ | $(10,30)$ | $(\mathrm b,\mathrm b)$ |
| $2$ | $(\mathrm b,\mathrm b)$ | $(27,30)$ | $(\mathrm b,\mathrm b)$ |

**Kiểm tra lại.** Cột giá trị không giảm theo từng trạng thái qua các vòng, đúng Định lý 04.13(a). Ba vòng không vượt số chính sách xác định $2\cdot2=4$.
:::

Thuật toán dừng ở vòng $i=2$ vì cải thiện không đổi hành động nào. Định nghĩa sau gọi tên tình huống đó.

::: definition Định nghĩa 04.16 (Chính sách ổn định)
Chính sách Markov dừng xác định $\pi$ là ổn định nếu Thuật toán 04.14, áp dụng cho $\pi$ và giá trị chính xác $v_\pi$, trả lại chính $\pi$; tương đương, $\pi(s)\in\arg\max_{a\in\mathcal A(s)}q_\pi(s,a)$ với mọi $s\in\mathcal S$.
:::

Hai cách phát biểu tương đương nhờ quy tắc phá hòa: Thuật toán 04.14 giữ hành động cũ khi và chỉ khi nó thuộc tập cực đại. Trong Ví dụ 04.11, $\pi_2$ ổn định, còn $\pi_1$ không ổn định vì $q_{\pi_1}(\mathrm s_0,\mathrm a)=10<27$. Tính ổn định là tính chất của cặp chính sách và giá trị chính xác của nó.

### 3.2 Thuật toán và dừng hữu hạn

Ví dụ 04.11 là ba vòng của thuật toán dưới đây, chạy bằng tay.

::: algorithm Thuật toán 04.17 (Lặp chính sách)
**Đầu vào.** Mô hình $p$ của MDP hữu hạn; $\gamma\in[0,1)$; chính sách Markov dừng xác định $\pi_0$.

**Đầu ra.** Chính sách $\pi$, giá trị $v_\pi$ của chính sách đó, và nhãn "ổn định" hoặc "chưa chứng nhận".

**Giả thiết.** Mô hình được biết đầy đủ; mỗi lần đánh giá cho giá trị chính xác.

**Tham số.** Ngân sách $I_{\max}\ge1$ vòng; thứ tự phá hòa cố định trên mỗi $\mathcal A(s)$.

**Khởi tạo.** $\pi\leftarrow\pi_0$, $i\leftarrow0$.

1. Đánh giá chính xác: giải $(I-\gamma P_\pi)v=r_\pi$ (Hệ quả 04.6(c)), được $v_\pi$.
2. Cải thiện: chạy Thuật toán 04.14 với $(\pi,v_\pi)$, được $\pi'$ và cờ.
3. Nếu cờ "ổn định" bật, trả $(\pi,v_\pi)$ với nhãn "ổn định".
4. Gán $i\leftarrow i+1$. Nếu $i=I_{\max}$, trả $(\pi,v_\pi)$ với nhãn "chưa chứng nhận".
5. Gán $\pi\leftarrow\pi'$, quay lại bước 1.

**Điều kiện dừng.** Bước 3 hoặc bước 4. Theo Mệnh đề 04.18, bước 3 xảy ra sau không quá $\prod_s\lvert\mathcal A(s)\rvert$ vòng khi $I_{\max}$ đủ lớn.

**Chi phí mỗi bước.** Bước 1 tốn $O(n^3)$ với khử Gauss trên ma trận đặc; bước 2 tốn $O(n^2m)$.
:::

Ở bước 4, thuật toán trả $\pi$ cùng giá trị của chính nó, không trả $\pi'$, vì $\pi'$ chưa được đánh giá; nhãn "chưa chứng nhận" nghĩa là chính sách trả về có thể còn cải thiện được. Mệnh đề sau giải thích vì sao bước 3 chắc chắn xảy ra.

::: proposition Mệnh đề 04.18 (Lặp chính sách dừng sau hữu hạn vòng)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; Thuật toán 04.17 với đánh giá chính xác và quy tắc phá hòa của Định nghĩa 04.12; $I_{\max}$ không giới hạn.

**Kết luận.** Thuật toán dừng ở bước 3 sau không quá $\prod_{s\in\mathcal S}\lvert\mathcal A(s)\rvert$ vòng, và chính sách trả về là ổn định.

**Điều kiện áp dụng.** Mỗi lần đánh giá trả đúng $v_\pi$; quy tắc phá hòa giữ hành động cũ khi hòa.

**Phạm vi.** Chặn trên là số chính sách xác định, thường rất lớn; mệnh đề không cho một số vòng nhỏ bảo đảm.
:::

::: proof Chứng minh Mệnh đề 04.18
**Bước 1 (dãy giá trị tăng).** Gọi $\pi_0,\pi_1,\dots$ là các chính sách được đánh giá. Nếu thuật toán chưa dừng ở vòng $i$ thì $\pi_{i+1}\ne\pi_i$, và theo Định lý 04.13(a)–(c), $v_{\pi_{i+1}}\ge v_{\pi_i}$ với dấu lớn hơn nghiêm ngặt ở ít nhất một trạng thái.

**Bước 2 (không lặp lại).** Giả sử $\pi_j=\pi_i$ với $i<j$. Theo Bước 1,

$$
v_{\pi_i}\le v_{\pi_{i+1}}\le\cdots\le v_{\pi_j}=v_{\pi_i},
$$

nên mọi bất đẳng thức trong chuỗi là đẳng thức, mâu thuẫn với việc $v_{\pi_{i+1}}$ lớn hơn $v_{\pi_i}$ nghiêm ngặt ở một trạng thái.

**Bước 3 (đếm).** Một chính sách Markov dừng xác định chọn một phần tử của $\mathcal A(s)$ cho mỗi $s$, nên có đúng $\prod_s\lvert\mathcal A(s)\rvert$ chính sách như vậy. Theo Bước 2, các chính sách trong dãy đôi một khác nhau, nên dãy dừng sau không quá chừng đó vòng; khi dừng, cờ "ổn định" bật, tức chính sách trả về ổn định theo Định nghĩa 04.16. $\square$
:::

Bước 1 dùng quy tắc phá hòa ở chỗ suy ra giá trị tăng nghiêm ngặt khi chính sách đổi. Giả sử tại một trạng thái có hai hành động cho cùng giá trị nhìn trước, và bước cải thiện được phép chọn tùy ý trong tập cực đại. Bước cải thiện có thể đổi sang hành động kia mà giá trị không tăng nghiêm ngặt ở đâu cả, rồi vòng sau đổi trở lại; dãy chính sách lặp vô hạn giữa hai chính sách cùng giá trị, và cờ "ổn định" không bao giờ bật. Sutton và Barto (2018, §4.3, Bài tập 4.4, tr. 82) nêu đúng lỗi này của giả mã lặp chính sách khi không có quy tắc phá hòa.

### 3.3 Chính sách ổn định là tối ưu

Lặp chính sách dừng ở $(\mathrm b,\mathrm b)$ với giá trị $(27,30)$. Câu hỏi còn lại là có chính sách nào khác cho giá trị lớn hơn tại một trạng thái nào đó hay không. Để trả lời, chúng ta cần nói chính xác "tốt nhất" nghĩa là gì, so với lớp chính sách nào.

Một cách trực quan, "tốt nhất" nghĩa là so tại từng trạng thái xuất phát với mọi cách chọn hành động. Trên mô hình hai trạng thái có bốn chính sách Markov dừng xác định, với giá trị $(10,11)$ cho $(\mathrm a,\mathrm a)$, $(10,30)$ cho $(\mathrm a,\mathrm b)$, khoảng $(9{,}47;\,10{,}53)$ cho $(\mathrm b,\mathrm a)$ (Mục 2.2) và $(27,30)$ cho $(\mathrm b,\mathrm b)$; chính sách $(\mathrm b,\mathrm b)$ đứng đầu tại cả hai trạng thái. Tác tử còn có thể chọn ngẫu nhiên, hoặc chọn theo lịch sử, chẳng hạn đi $\mathrm b$ ở lần đầu ghé $\mathrm s_0$ và đi $\mathrm a$ ở các lần sau, nên phép so sánh phải bao cả những cách đó. Đây mới là mô tả; định nghĩa sau làm chính xác lớp chính sách và phép so sánh.

::: definition Định nghĩa 04.19 (Giá trị tối ưu, chính sách tối ưu)
Cho MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, và $\Pi$ là lớp mọi chính sách, kể cả chính sách chọn hành động theo toàn bộ lịch sử $(S_0,A_0,R_1,\dots,S_t)$. Với $\pi\in\Pi$, đặt $v_\pi(s)=\mathbb E_\pi[G_0\mid S_0=s]$.

**Giá trị tối ưu.** $v_*(s)=\sup_{\pi\in\Pi}v_\pi(s)$ với mọi $s\in\mathcal S$; $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_*(s')\bigr]$.

**Chính sách tối ưu.** $\pi_*\in\Pi$ là tối ưu nếu $v_{\pi_*}(s)=v_*(s)$ với mọi $s\in\mathcal S$.
:::

Định nghĩa dùng $\sup$ vì trước khi chứng minh, chúng ta chưa biết cận trên có đạt được bởi một chính sách nào hay không. Một chính sách tối ưu phải không thua mọi chính sách khác đồng thời tại mọi trạng thái xuất phát, và đến đây chúng ta chưa biết một chính sách như vậy có tồn tại hay không. Giá trị $v_*(s)\le R_{\max}/(1-\gamma)$ hữu hạn vì mọi lợi tức đều bị chặn bởi số đó. Định lý sau trả lời câu hỏi trên lớp chính sách Markov dừng; Định lý 04.25 ở Mục 4 mở rộng kết quả sang toàn bộ $\Pi$.

::: theorem Định lý 04.20 (Chính sách ổn định thỏa phương trình Bellman tối ưu)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; $\pi$ là chính sách Markov dừng xác định ổn định với giá trị chính xác $v_\pi$.

**Kết luận.**

- (a) $v_\pi$ thỏa phương trình Bellman tối ưu (Bellman optimality equation)

$$
v_\pi(s)=\max_{a\in\mathcal A(s)}\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma v_\pi(s')\bigr]\qquad\text{với mọi } s\in\mathcal S .
\tag{3.1}
$$

- (b) Với mọi chính sách Markov dừng $\pi'$, kể cả ngẫu nhiên, $v_{\pi'}\le v_\pi$ theo từng trạng thái.

**Điều kiện áp dụng.** $v_\pi$ là giá trị chính xác; tính ổn định được kiểm bằng $v_\pi$, không bằng một bảng gần đúng.

**Phạm vi.** Phần (b) so sánh với các chính sách Markov dừng. So sánh với chính sách phụ thuộc lịch sử cần Định lý 04.25.
:::

::: proof Chứng minh Định lý 04.20
**Bước 1 (phương trình (3.1)).** Vì $\pi$ xác định, $v_\pi(s)=(T_\pi v_\pi)(s)=q_\pi(s,\pi(s))$. Vì $\pi$ ổn định, $\pi(s)\in\arg\max_aq_\pi(s,a)$, nên $q_\pi(s,\pi(s))=\max_aq_\pi(s,a)$. Thay $q_\pi(s,a)=Q_{v_\pi}(s,a)$ theo (2.1) cho (3.1).

**Bước 2 (một lần áp dụng $T_{\pi'}$ không vượt $v_\pi$).** Với chính sách Markov dừng $\pi'$ bất kỳ và mọi $s$,

$$
\begin{aligned}
(T_{\pi'}v_\pi)(s)
&=\sum_a\pi'(a\mid s)\,q_\pi(s,a) &&\text{(Định nghĩa 04.1, (2.1))}\\
&\le\max_aq_\pi(s,a) &&\text{(trung bình không vượt cực đại)}\\
&=v_\pi(s) &&\text{(Bước 1)}.
\end{aligned}
$$

**Bước 3 (lặp và qua giới hạn).** Từ $T_{\pi'}v_\pi\le v_\pi$, áp dụng Bổ đề 04.2 lặp lại như Bước 2 của chứng minh Định lý 04.13 nhưng theo chiều ngược, được $(T_{\pi'})^kv_\pi\le v_\pi$ với mọi $k$. Theo Hệ quả 04.6(b), vế trái hội tụ về $v_{\pi'}$, nên $v_{\pi'}\le v_\pi$. $\square$
:::

Phương trình (3.1) khác phương trình Bellman kỳ vọng (1.2) ở một chỗ: trung bình theo chính sách được thay bằng cực đại theo hành động. Phép cực đại đứng ngoài kỳ vọng theo mô hình, vì tác tử chọn hành động trước khi biết kết quả ngẫu nhiên của môi trường; lấy kỳ vọng của cực đại là cho phép tác tử chọn hành động sau khi thấy kết quả, một quyền mà nó không có.

Phương trình (3.1) đọc bằng lời: giá trị của chính sách ổn định tại mỗi trạng thái bằng giá trị của hành động tốt nhất khi từ bước sau vẫn theo chính sách đó, nên không còn cách lệch một bước nào có lợi.

::: example Ví dụ 04.12 (Chứng nhận $(\mathrm b,\mathrm b)$ trên mô hình hai trạng thái)
**Dữ kiện.** Mô hình hai trạng thái như Ví dụ 04.11, $\gamma=0{,}9$; $\pi_2=(\mathrm b,\mathrm b)$ ổn định với $v_{\pi_2}=(27,30)$ và các giá trị nhìn trước $25{,}3$; $27$ tại $\mathrm s_0$ và $26{,}3$; $30$ tại $\mathrm s_1$ (Ví dụ 04.11). Bốn chính sách Markov dừng xác định có giá trị $(10,11)$, $(10,30)$, $(9{,}47;\,10{,}53)$ và $(27,30)$.

**Phương trình (3.1).** $\max\{25{,}3;\,27\}=27=v_{\pi_2}(\mathrm s_0)$ và $\max\{26{,}3;\,30\}=30=v_{\pi_2}(\mathrm s_1)$.

**Kiểm tra lại.** Trong bốn bảng, $(27,30)$ lớn nhất tại cả hai trạng thái, khớp Định lý 04.20(b).
:::

Định lý 04.20 cần hai điều kiện ở giả thiết, và mỗi điều kiện đều có phản ví dụ khi bị bỏ.

- Bỏ "giá trị chính xác": một chính sách có thể không đổi khi cải thiện theo một bảng gần đúng mà vẫn không tối ưu (phản ví dụ sau Định lý 04.13, Bài tập 04.3).
- Bỏ $\gamma<1$: Bước 3 dùng Hệ quả 04.6(b), không còn đúng khi $\gamma=1$ (đoạn sau Ví dụ 04.5).

::: remark Nhận xét 04.21 (Hai cách đọc sai kết quả của lặp chính sách)
- Kết luận tối ưu khi chính sách không đổi theo một bảng gần đúng, chẳng hạn bảng sau vài lượt quét của Thuật toán 04.9: Định nghĩa 04.16 đòi giá trị chính xác. Muốn dùng bảng gần đúng, cần một chứng nhận khác, ví dụ chặn sai số của Mục 4.
- Đồng nhất một vòng của lặp chính sách với một lượt quét: một vòng chứa một lần đánh giá đầy đủ, tương đương vô hạn lượt quét của Thuật toán 04.9 hoặc một lần giải hệ tuyến tính.
:::

**Trong thực hành.** Một lần chạy đã nhúng trong bài thực hành CartPole cho thấy lặp chính sách dừng với nhãn "ổn định" sau $6$ vòng trên MDP 324 ô; số ô đổi hành động qua các vòng là $173$, $87$, $23$, $10$, $1$, $0$. Tại chính sách ổn định, độ lệch lớn nhất giữa hai vế của (3.1) là $4{,}26\cdot10^{-14}$. Số $6$ vòng nhỏ hơn nhiều chặn $2^{324}$ của Mệnh đề 04.18, nhưng không định lý nào trong chương bảo đảm con số nhỏ như vậy cho mọi bài toán.

::: exercise Bài tập 04.3 (Kết luận dừng từ một bảng gần đúng)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Một chương trình giữ chính sách $\pi=(\mathrm a,\mathrm b)$ và bảng gần đúng $V=(0,0)$ thay cho giá trị của $\pi$.

(a) Tính bốn giá trị nhìn trước $Q_V(s,a)$.

(b) Xác định chính sách tham lam theo $V$ với quy tắc phá hòa.

(c) Chương trình kết luận "chính sách không đổi nên đã tối ưu". Đánh giá kết luận này bằng Định nghĩa 04.16 và Ví dụ 04.11.
:::

::: hint
Với $V=(0,0)$, giá trị nhìn trước chỉ còn phần thưởng của bước đầu. Để đánh giá kết luận, so giá trị thật của $(\mathrm a,\mathrm b)$ với giá trị của $(\mathrm b,\mathrm b)$.
:::

::: solution
**(a)** $Q_V(\mathrm s_0,\mathrm a)=1$, $Q_V(\mathrm s_0,\mathrm b)=0$, $Q_V(\mathrm s_1,\mathrm a)=2$, $Q_V(\mathrm s_1,\mathrm b)=3$.

**(b)** Tại $\mathrm s_0$, $\arg\max=\{\mathrm a\}$ chứa hành động cũ; tại $\mathrm s_1$, $\arg\max=\{\mathrm b\}$ chứa hành động cũ. Chính sách tham lam theo $V$ là $(\mathrm a,\mathrm b)$, trùng $\pi$.

**(c)** Kết luận sai. Định nghĩa 04.16 đòi kiểm tính ổn định bằng $v_\pi$; ở đây $v_{(\mathrm a,\mathrm b)}=(10,30)$ (Ví dụ 04.10), và từ bảng này $q(\mathrm s_0,\mathrm b)=27>10=q(\mathrm s_0,\mathrm a)$, nên $\pi$ không ổn định. Theo Ví dụ 04.11, $(\mathrm b,\mathrm b)$ có giá trị $(27,30)$, lớn hơn $(10,30)$ tại $\mathrm s_0$.

**Kiểm tra lại.** Phép chọn hành động trong (b) đúng đối với bảng $V$; lỗi nằm ở bảng, vì $V=(0,0)$ không phải giá trị của chính sách đang giữ.
:::

Như vậy, xen kẽ đánh giá chính xác với cải thiện cho thuật toán lặp chính sách (Thuật toán 04.17). Nhờ định lý cải thiện và quy tắc phá hòa, thuật toán dừng sau hữu hạn vòng (Mệnh đề 04.18) tại một chính sách ổn định, và chính sách ổn định thỏa phương trình Bellman tối ưu, không kém mọi chính sách Markov dừng (Định lý 04.20). Trên mô hình hai trạng thái, $\pi_*=(\mathrm b,\mathrm b)$ và $v_*=(27,30)$ trong lớp chính sách Markov dừng. Tuy nhiên, mỗi vòng đòi một lần đánh giá đầy đủ, và kết quả mới so với chính sách Markov dừng; trong Mục 4, chúng ta bỏ đánh giá đầy đủ và mở rộng phép so sánh sang mọi chính sách.

<!-- note-topic-id: lec-04-part-05 -->
## 4. Lặp giá trị

Lặp chính sách đánh giá đầy đủ mỗi chính sách trước khi cải thiện: trên mô hình hai trạng thái, riêng lần đánh giá $\pi_0$ bằng lượt quét đã cần $44$ lượt (Ví dụ 04.7), còn giải hệ tốn $O(n^3)$. Trong khi đó, chính sách tham lam có thể đúng từ sớm: theo bảng $V_1=(1,2)$ của Ví dụ 04.2, nhánh $\mathrm a$ tại $\mathrm s_0$ cho $1+0{,}9\cdot1=1{,}9>1{,}8=0+0{,}9\cdot2$ và nhánh $\mathrm b$ tại $\mathrm s_1$ cho $3+0{,}9\cdot2=4{,}8>2{,}9$, nên chính sách tham lam là $(\mathrm a,\mathrm b)$, trùng kết quả của Ví dụ 04.9 từ giá trị chính xác $(10,11)$. Chúng ta cần một cách cải thiện mà không chờ đánh giá xong, kèm bảo đảm vẫn tới giá trị tối ưu.

### 4.1 Gộp cải thiện vào một lượt quét

Về mặt ý tưởng, ta cắt phần đánh giá xuống còn đúng một lượt quét. Tại mỗi trạng thái, ta tính giá trị nhìn trước của mọi hành động từ bảng hiện có, chọn hành động tốt nhất, và lấy luôn giá trị nhìn trước của hành động đó làm giá trị mới. Chọn tham lam rồi đánh giá một lượt quét đúng bằng một phép lấy cực đại, nên hai bước gộp làm một. Đây là mô tả, chưa phải định nghĩa; chúng ta chưa biết các bảng thu được có nghĩa gì.

::: example Ví dụ 04.13 (Hai lượt quét lặp giá trị trên mô hình hai trạng thái)
**Dữ kiện.** Mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$; $V_0=(0,0)$.

**Lượt quét thứ nhất, đọc $V_0$.** Giá trị nhìn trước chỉ còn phần thưởng: $V_1(\mathrm s_0)=\max\{1;\,0\}=1$ và $V_1(\mathrm s_1)=\max\{2;\,3\}=3$, nên $V_1=(1,3)$.

**Lượt quét thứ hai, đọc $V_1=(1,3)$.**

| Trạng thái | Nhánh $\mathrm a$ | Nhánh $\mathrm b$ | Cực đại |
|---|---|---|---|
| $\mathrm s_0$ | $1+0{,}9\cdot1=1{,}9$ | $0+0{,}9\cdot3=2{,}7$ | $2{,}7$ |
| $\mathrm s_1$ | $2+0{,}9\cdot1=2{,}9$ | $3+0{,}9\cdot3=5{,}7$ | $5{,}7$ |

Vậy $V_2=(2{,}7;\,5{,}7)$.

**Diễn giải.** Lượt quét đầu của đánh giá $\pi_0$ cho $(1,2)$ (Ví dụ 04.2), còn lặp giá trị cho $(1,3)$: tại $\mathrm s_1$, phép cực đại chọn $\mathrm b$ thay vì $\mathrm a$ của $\pi_0$. Hành động đạt cực đại là $(\mathrm a,\mathrm b)$ ở lượt quét đầu, $(\mathrm b,\mathrm b)$ ở lượt quét sau.

**Kiểm tra lại.** Với $V_0=0$, $V_k(s)$ là tổng chiết khấu lớn nhất của $k$ phần thưởng đầu từ $s$: từ $\mathrm s_1$, hai bước $\mathrm b,\mathrm b$ cho $3+0{,}9\cdot3=5{,}7$.
:::

### 4.2 Toán tử Bellman tối ưu và tính co

Hai cột "Nhánh" của Ví dụ 04.13 là các giá trị nhìn trước $Q_{V_1}(s,a)$ của Định nghĩa 04.11, và cột "Cực đại" là bảng mới.

::: definition Định nghĩa 04.22 (Toán tử Bellman tối ưu, phần dư tối ưu)
Cho MDP hữu hạn và $\gamma\in[0,1)$. Toán tử Bellman tối ưu (Bellman optimality operator) là ánh xạ $T_*:\mathbb R^n\to\mathbb R^n$,

$$
(T_*V)(s)=\max_{a\in\mathcal A(s)}Q_V(s,a)=\max_{a\in\mathcal A(s)}\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr],\qquad s\in\mathcal S .
\tag{4.1}
$$

Lặp giá trị (value iteration) là dãy $V_{k+1}=T_*V_k$ từ một bảng $V_0\in\mathbb R^n$. Phần dư tối ưu của bảng $V$ là $\Delta_*(V)=\lVert T_*V-V\rVert_\infty$.
:::

Toán tử $T_*$ khác $T_\pi$ đúng ở khối chọn hành động: $T_\pi$ lấy trung bình theo $\pi$, $T_*$ lấy cực đại. Với chính sách tham lam $\pi_V$ theo $V$, hai phép tính trùng nhau tại bảng $V$: $T_*V=T_{\pi_V}V$.

Phương trình Bellman tối ưu (3.1) viết gọn là $V=T_*V$, nên Định lý 04.20(a) nói rằng giá trị của chính sách ổn định là một điểm bất động của $T_*$. Các số $1{,}9$; $2{,}7$; $2{,}9$; $5{,}7$ của Ví dụ 04.13 là giá trị nhìn trước từ $V_1=(1,3)$, không là giá trị hành động $q_\pi$ của một chính sách, vì $V_1$ không là giá trị của chính sách xác định nào (Nhận xét 04.29).

Để chứng minh $T_*$ co, ta cần một bất đẳng thức về cực đại: phép lấy cực đại không làm tăng độ chênh lệch lớn nhất.

::: lemma Bổ đề 04.23 (Cực đại không làm tăng chênh lệch)
**Giả thiết.** $A$ là tập hữu hạn khác rỗng; $x_a,y_a\in\mathbb R$ với $a\in A$.

**Kết luận.** $\bigl\lvert\max_ax_a-\max_ay_a\bigr\rvert\le\max_a\lvert x_a-y_a\rvert$.

**Điều kiện áp dụng.** Cực đại được đạt, điều được bảo đảm khi $A$ hữu hạn.

**Phạm vi.** Bất đẳng thức cũng đúng cho cận trên đúng trên tập vô hạn khi các cận hữu hạn; chương chỉ dùng tập hữu hạn.
:::

::: proof Chứng minh Bổ đề 04.23
**Bước 1 (một chiều).** Gọi $a^\circ$ là phần tử đạt $\max_ax_a$. Khi đó

$$
\begin{aligned}
\max_ax_a-\max_ay_a
&=x_{a^\circ}-\max_ay_a &&\text{(cách chọn } a^\circ)\\
&\le x_{a^\circ}-y_{a^\circ} &&\text{(}\max_ay_a\ge y_{a^\circ})\\
&\le\max_a\lvert x_a-y_a\rvert &&\text{(định nghĩa cực đại)}.
\end{aligned}
$$

**Bước 2 (chiều kia).** Hoán vai trò của $x$ và $y$ cho $\max_ay_a-\max_ax_a\le\max_a\lvert x_a-y_a\rvert$. Hai chiều cùng nhau cho kết luận. $\square$
:::

::: proposition Mệnh đề 04.24 ($T_*$ là ánh xạ co)
**Giả thiết.** MDP hữu hạn; $0\le\gamma<1$.

**Kết luận.** $\lVert T_*U-T_*V\rVert_\infty\le\gamma\lVert U-V\rVert_\infty$ với mọi $U,V\in\mathbb R^n$.

**Điều kiện áp dụng.** Mỗi $\mathcal A(s)$ hữu hạn khác rỗng; trọng số của mô hình không âm với tổng bằng $1$.

**Phạm vi.** Hệ số co bằng hệ số của $T_\pi$ trong Mệnh đề 04.4.
:::

::: proof Chứng minh Mệnh đề 04.24
**Bước 1 (từng hành động).** Với $s,a$ cố định, phần thưởng triệt tiêu trong hiệu như ở Bước 1–2 của chứng minh Mệnh đề 04.4, áp dụng cho chính sách chọn $a$ với xác suất $1$:

$$
\bigl\lvert Q_U(s,a)-Q_V(s,a)\bigr\rvert=\gamma\Bigl\lvert\sum_{s',r}p(s',r\mid s,a)\bigl[U(s')-V(s')\bigr]\Bigr\rvert\le\gamma\lVert U-V\rVert_\infty .
$$

**Bước 2 (qua cực đại).** Theo Bổ đề 04.23 với $x_a=Q_U(s,a)$, $y_a=Q_V(s,a)$:

$$
\bigl\lvert(T_*U)(s)-(T_*V)(s)\bigr\rvert\le\max_a\bigl\lvert Q_U(s,a)-Q_V(s,a)\bigr\rvert\le\gamma\lVert U-V\rVert_\infty .
$$

**Bước 3 (lấy cực đại).** Bất đẳng thức của Bước 2 đúng với mọi $s$; lấy cực đại theo $s$ cho kết luận. $\square$
:::

Trên mô hình hai trạng thái với $U=(10,11)$ và $V=(0,0)$ như Ví dụ 04.4, $T_*U=(\max\{10;\,9{,}9\},\ \max\{11;\,12{,}9\})=(10;\,12{,}9)$ và $T_*V=(1,3)$, nên $\lVert T_*U-T_*V\rVert_\infty=9{,}9=0{,}9\cdot11$: chặn của Mệnh đề 04.24 đạt dấu bằng.

<!-- note-topic-id: lec-04-part-11 -->
### 4.3 Tồn tại chính sách tối ưu

Theo Định lý 04.5 và Mệnh đề 04.24, $T_*$ có đúng một điểm bất động. Định lý 04.20 mới so với các chính sách Markov dừng, còn Định nghĩa 04.19 lấy cận trên trên toàn bộ $\Pi$. Định lý sau nối hai điều: điểm bất động của $T_*$ là $v_*$, và có một chính sách Markov dừng, xác định đạt được nó.

::: theorem Định lý 04.25 (Tồn tại chính sách tối ưu Markov dừng, xác định)
**Giả thiết.** MDP hữu hạn với tính Markov, phần thưởng bị chặn, $0\le\gamma<1$.

**Kết luận.**

- (a) Điểm bất động duy nhất $\bar V$ của $T_*$ bằng $v_*$; tức $v_*$ là nghiệm duy nhất của $V=T_*V$.
- (b) Mọi chính sách Markov dừng xác định tham lam theo $v_*$ là chính sách tối ưu trên toàn bộ $\Pi$.
- (c) $v_*(s)=\max_{a\in\mathcal A(s)}q_*(s,a)$ với mọi $s$, và $q_*$ thỏa phương trình Bellman tối ưu cho giá trị hành động: $q_*(s,a)=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma\max_{a'\in\mathcal A(s')}q_*(s',a')\bigr]$ với mọi $s\in\mathcal S$, $a\in\mathcal A(s)$, quy ước $\max_{a'}q_*(s_{\mathrm{term}},a')=0$.
- (d) Chính sách ổn định trả về bởi Thuật toán 04.17 là tối ưu trên toàn bộ $\Pi$.

**Điều kiện áp dụng.** Tập hành động hữu hạn để cực đại đạt; tính Markov của môi trường dùng ở bước chặn chính sách phụ thuộc lịch sử.

**Phạm vi.** Kết quả thuộc về MDP chiết khấu với tập trạng thái và hành động hữu hạn. Với tập hành động vô hạn, cận trên có thể không đạt.
:::

::: proof Chứng minh Định lý 04.25
**Bước 1 (điểm bất động).** Theo Mệnh đề 04.24 và Định lý 04.5(a), $T_*$ có đúng một điểm bất động $\bar V$.

**Bước 2 ($\bar V$ đạt được).** Chọn tại mỗi $s$ một hành động $\bar\pi(s)\in\arg\max_aQ_{\bar V}(s,a)$; tập $\arg\max$ khác rỗng vì $\mathcal A(s)$ hữu hạn. Khi đó $T_{\bar\pi}\bar V=T_*\bar V=\bar V$, tức $\bar V$ là điểm bất động của $T_{\bar\pi}$. Theo Hệ quả 04.6(a), $\bar V=v_{\bar\pi}$.

**Bước 3 (một bước của chính sách bất kỳ).** Lấy $\pi\in\Pi$ bất kỳ, xuất phát từ $S_0=s$; từ đây đến hết chứng minh, $\mathbb E_\pi$ và $\Pr$ đều có điều kiện $S_0=s$, nên $\mathbb E_\pi[\bar V(S_0)]=\bar V(s)$. Gọi $H_t=(S_0,A_0,R_1,\dots,S_t)$ là lịch sử tới thời điểm $t$. Nếu $S_t\in\mathcal S$, chính sách chọn $A_t$ theo phân phối $\pi_t(\cdot\mid H_t)$, và theo tính Markov, cặp $(S_{t+1},R_{t+1})$ có phân phối $p(\cdot,\cdot\mid S_t,A_t)$ bất kể phần còn lại của $H_t$. Do đó

$$
\begin{aligned}
\mathbb E_\pi\bigl[R_{t+1}+\gamma\bar V(S_{t+1})\mid H_t\bigr]
&=\sum_a\pi_t(a\mid H_t)\,Q_{\bar V}(S_t,a) &&\text{(tính Markov, (2.1))}\\
&\le\max_aQ_{\bar V}(S_t,a) &&\text{(trung bình không vượt cực đại)}\\
&=\bar V(S_t) &&\text{(}\bar V=T_*\bar V).
\end{aligned}
$$

Nếu $S_t=s_{\mathrm{term}}$, cả $R_{t+1}$ lẫn $\bar V(S_{t+1})$ bằng $0$ và bất đẳng thức đúng với dấu bằng.

**Bước 4 (cộng dồn).** Nhân Bước 3 với $\gamma^t$ và lấy kỳ vọng hai vế theo luật kỳ vọng lặp:

$$
\gamma^t\,\mathbb E_\pi[R_{t+1}]\le\gamma^t\,\mathbb E_\pi[\bar V(S_t)]-\gamma^{t+1}\,\mathbb E_\pi[\bar V(S_{t+1})].
$$

Cộng từ $t=0$ tới $N-1$, các số hạng ở giữa vế phải triệt tiêu từng cặp:

$$
\mathbb E_\pi\Bigl[\sum_{t=0}^{N-1}\gamma^tR_{t+1}\Bigr]\le\bar V(s)-\gamma^N\,\mathbb E_\pi[\bar V(S_N)].
$$

**Bước 5 (qua giới hạn).** Số hạng $\gamma^N\mathbb E_\pi[\bar V(S_N)]$ có trị tuyệt đối không quá $\gamma^N\lVert\bar V\rVert_\infty\to0$. Phần đuôi bị bỏ của lợi tức thỏa $\bigl\lvert G_0-\sum_{t=0}^{N-1}\gamma^tR_{t+1}\bigr\rvert\le\sum_{t\ge N}\gamma^tR_{\max}=\gamma^NR_{\max}/(1-\gamma)$, nên $\bigl\lvert v_\pi(s)-\mathbb E_\pi\bigl[\sum_{t<N}\gamma^tR_{t+1}\bigr]\bigr\rvert\le\gamma^NR_{\max}/(1-\gamma)\to0$. Cho $N\to\infty$ ở Bước 4, ta được $v_\pi(s)\le\bar V(s)$ với mọi $\pi\in\Pi$.

**Bước 6 (kết luận).** Từ Bước 5, $v_*(s)=\sup_\pi v_\pi(s)\le\bar V(s)$; từ Bước 2, $\bar V(s)=v_{\bar\pi}(s)\le v_*(s)$. Vậy $\bar V=v_*$, đây là (a), và chính sách $\bar\pi$, một chính sách tham lam tùy ý theo $v_*$, đạt $v_*$; đây là (b). Theo Định nghĩa 04.19, $q_*(s,a)=Q_{v_*}(s,a)$, nên đẳng thức đầu của (c) là $v_*=T_*v_*$ viết lại bằng $q_*$; thế $v_*(s')=\max_{a'}q_*(s',a')$ với $s'\in\mathcal S$ và $v_*(s_{\mathrm{term}})=0$ vào định nghĩa của $q_*$, ta được đẳng thức thứ hai. Với (d), Định lý 04.20(a) cho $v_\pi=T_*v_\pi$ tại chính sách ổn định, nên $v_\pi=\bar V=v_*$ theo tính duy nhất ở Bước 1. $\square$
:::

Định lý 04.25 trả lời bài toán lập kế hoạch ở đầu chương: một chính sách tốt nhất tại mọi trạng thái đồng thời tồn tại, có thể chọn nó là chính sách Markov dừng, xác định, và chỉ cần biết $v_*$ là trích được nó bằng một phép nhìn trước. Mỗi giả thiết có vai trò riêng.

- Bỏ tập hành động hữu hạn: xét một trạng thái với các hành động $\mathrm a_1,\mathrm a_2,\dots$, hành động $\mathrm a_j$ cho phần thưởng $1-1/j$ rồi kết thúc. Khi đó $v_*=1$ nhưng không chính sách nào đạt $1$; Bước 2 hỏng vì $\arg\max$ rỗng.
- Bỏ tính Markov: nếu phân phối của $(S_{t+1},R_{t+1})$ phụ thuộc cả lịch sử, đẳng thức đầu của Bước 3 sai, và chứng minh không còn loại được khả năng một chính sách nhớ lịch sử vượt mọi chính sách Markov dừng. Tình huống 04.2 xét hệ quả của việc mất tính Markov khi gộp trạng thái của CartPole.
- Bỏ $\gamma<1$: Bước 1 và Bước 5 đều dùng $\gamma<1$ (đoạn sau Ví dụ 04.5).

Theo phần (d), trên mô hình hai trạng thái, $(\mathrm b,\mathrm b)$ tốt nhất trong toàn bộ $\Pi$, kể cả các chính sách ngẫu nhiên và các chính sách nhớ lịch sử, và $v_*=(27,30)$. Bốn giá trị hành động tối ưu $q_*(\mathrm s_0,\cdot)=(25{,}3;\,27)$ và $q_*(\mathrm s_1,\cdot)=(26{,}3;\,30)$, tức các giá trị nhìn trước tính ở Ví dụ 04.11 và nhắc lại ở Ví dụ 04.12, thỏa dạng đệ quy ở (c) (Bài giảng gốc (2025–2026), trang 8); chẳng hạn $q_*(\mathrm s_0,\mathrm b)=0+0{,}9\max\{26{,}3;\,30\}=27$ và $q_*(\mathrm s_0,\mathrm a)=1+0{,}9\max\{25{,}3;\,27\}=25{,}3$.

### 4.4 Hội tụ, điều kiện dừng và thuật toán

Định lý 04.25 cho biết lặp giá trị nhắm tới đâu; hai hệ quả sau cho biết nó tới nhanh đến đâu và khi nào được dừng.

::: corollary Hệ quả 04.26 (Hội tụ hình học của lặp giá trị)
**Giả thiết.** Như Định lý 04.25; $V_0\in\mathbb R^n$ bất kỳ và $V_{k+1}=T_*V_k$.

**Kết luận.** $\lVert V_k-v_*\rVert_\infty\le\gamma^k\lVert V_0-v_*\rVert_\infty$ với mọi $k\ge0$.

**Điều kiện áp dụng.** Lượt quét đồng bộ dùng đúng $T_*$ trên mô hình đã cho.

**Phạm vi.** Chặn chứa $v_*$ chưa biết, nên cho tốc độ nhưng không dùng trực tiếp làm điều kiện dừng.
:::

::: proof Chứng minh Hệ quả 04.26
Áp dụng Định lý 04.5(b) cho $F=T_*$ với $\beta=\gamma$ (Mệnh đề 04.24), và dùng $\bar V=v_*$ (Định lý 04.25(a)). $\square$
:::

Trên mô hình hai trạng thái từ $V_0=(0,0)$, $\lVert V_0-v_*\rVert_\infty=\max\{27;\,30\}=30$, nên chặn là $30\cdot0{,}9^k$. Từ $k\ge2$, lặp giá trị chọn $\mathrm b$ ở cả hai trạng thái và cho $V_k=(27-30\cdot0{,}9^k,\ 30-30\cdot0{,}9^k)$; tại $k=1$, $V_1=(1,3)$ có sai số $\max\{26;\,27\}=27=30\cdot0{,}9$. Sai số thật trùng chặn ở mọi $k$.

![Đồ thị trên thang logarit: trục hoành là số lượt quét k từ 0 đến 60, trục tung là sai số từ 0,01 đến 100. Đường liền là chặn 30 nhân 0,9 mũ k, đi từ 30 tại k = 0 xuống khoảng 0,054 tại k = 60. Các chấm tròn tại k = 0, 5, 10, …, 60 là sai số đo được của lặp giá trị và nằm đúng trên đường. Đường ngang nét đứt ở mức 0,1; đường đứng nét đứt tại k = 55.](img/lec-04/dp04-convergence-bound.svg)

Trên thang logarit, chặn $30\cdot0{,}9^k$ là đường thẳng giảm khoảng mười lần sau mỗi $22$ lượt quét, vì $0{,}9^{22}\approx0{,}098$. Các chấm tròn là sai số đo được và nằm trên đường: chặn của Hệ quả 04.26 chặt trong ví dụ này. Đường ngang $0{,}1$ cắt đường chặn giữa $k=54$ và $k=55$, vì $30\cdot0{,}9^{54}\approx0{,}101$ và $30\cdot0{,}9^{55}\approx0{,}091$; lượt quét đầu tiên có sai số không quá $0{,}1$ là $k=55$.

::: corollary Hệ quả 04.27 (Chặn sai số theo phần dư tối ưu)
**Giả thiết.** Như Định lý 04.25; $V\in\mathbb R^n$ bất kỳ.

**Kết luận.** $\lVert V-v_*\rVert_\infty\le\dfrac{\Delta_*(V)}{1-\gamma}$. Nói riêng, nếu $\Delta_*(V)\le\theta$ với $\theta=(1-\gamma)\kappa$ thì $\lVert V-v_*\rVert_\infty\le\kappa$.

**Điều kiện áp dụng.** Phần dư đo trên chính bảng được dùng.

**Phạm vi.** Chặn sai số của bảng, không phải chặn tổn thất của chính sách trích từ bảng.
:::

::: proof Chứng minh Hệ quả 04.27
Lặp lại Bước 1–2 và Bước 4 của chứng minh Hệ quả 04.8, thay $T_\pi$ bằng $T_*$, $v_\pi$ bằng $v_*$, Định nghĩa 04.7 bằng Định nghĩa 04.22 và Mệnh đề 04.4 bằng Mệnh đề 04.24; đẳng thức $v_*=T_*v_*$ lấy từ Định lý 04.25(a). $\square$
:::

Trên mô hình hai trạng thái, $V_1=(1,3)$ có $T_*V_1=(2{,}7;\,5{,}7)$, nên $\Delta_*(V_1)=\max\{1{,}7;\,2{,}7\}=2{,}7$ và chặn bằng $27$, đúng bằng sai số thật. Với $\kappa=0{,}1$, ngưỡng là $\theta=0{,}01$; bảng $V_{55}\approx(26{,}9087;\,29{,}9087)$ có phần dư khoảng $0{,}00913\le0{,}01$, chặn và sai số thật cùng bằng khoảng $0{,}0913$.

Thuật toán dưới đây ghép quy tắc (4.1) với điều kiện dừng của Hệ quả 04.27; trên mô hình hai trạng thái, hai lần lặp đầu của nó là Ví dụ 04.13.

::: algorithm Thuật toán 04.28 (Lặp giá trị đồng bộ có kiểm tra dừng)
**Đầu vào.** Mô hình $p$ của MDP hữu hạn; $\gamma\in[0,1)$.

**Đầu ra.** Bảng $V$, chính sách tham lam $\pi_V$, phần dư $\Delta_*(V)$, cả ba thuộc cùng bảng $V$, và nhãn "đạt ngưỡng" hoặc "hết ngân sách".

**Giả thiết.** Mô hình được biết đầy đủ.

**Tham số.** Ngưỡng $\theta=(1-\gamma)\kappa$; ngân sách $K\ge0$ lượt quét; thứ tự phá hòa cố định trên mỗi $\mathcal A(s)$.

**Khởi tạo.** $V(s)=0$ với mọi $s\in\mathcal S$; $V(s_{\mathrm{term}})=0$; $k=0$.

1. Giữ $V$ cố định, tính $Q_V(s,a)$ theo (2.1) cho mọi $s\in\mathcal S$, $a\in\mathcal A(s)$.
2. Đặt $W(s)=\max_aQ_V(s,a)$ và $\pi_V(s)\in\arg\max_aQ_V(s,a)$ theo thứ tự phá hòa.
3. Đặt $\Delta=\lVert W-V\rVert_\infty$, tức $\Delta_*(V)$.
4. Nếu $\Delta\le\theta$, trả $(V,\pi_V,\Delta)$ với nhãn "đạt ngưỡng"; nếu $k=K$, trả cùng bộ ba với nhãn "hết ngân sách".
5. Gán $V\leftarrow W$, $k\leftarrow k+1$, quay lại bước 1.

**Điều kiện dừng.** Bước 4; theo Hệ quả 04.26, nhãn "đạt ngưỡng" xuất hiện sau hữu hạn lượt quét khi $K$ đủ lớn.

**Chi phí mỗi bước.** Bước 1 tốn $O(n^2m)$ với mô hình đặc, $O(nmd)$ khi mỗi cặp $(s,a)$ có tối đa $d$ trạng thái kế tiếp; bước 2–3 tốn $O(nm)$; bộ nhớ $O(n)$ cho $V$, $W$, $\pi_V$.
:::

Trên mô hình hai trạng thái với $K=1$ và $\theta=0{,}01$, thuật toán trả $V_1=(1,3)$, $\Delta_*(V_1)=2{,}7$ với nhãn "hết ngân sách" và chính sách $(\mathrm b,\mathrm b)$. So với lặp chính sách, mỗi lượt quét rẻ hơn một vòng, nhưng cần nhiều lượt quét: $55$ lượt cho sai số $0{,}1$ trên mô hình này, so với $3$ vòng của Ví dụ 04.11.

::: remark Nhận xét 04.29 (Bảng giá trị và chính sách trích từ bảng)
- Chính sách tham lam có thể đã tối ưu khi bảng còn xa nghiệm: với $V_1=(1,3)$, sai số $27$, chính sách trích ra đã là $(\mathrm b,\mathrm b)$. Ngược lại, phần dư nhỏ không bảo đảm chính sách trích ra tối ưu khi có hai hành động gần đồng hạng.
- $V_1=(1,3)$ khác cả bốn giá trị của bốn chính sách Markov dừng xác định (Mục 3.3), nên bảng giữa chừng nói chung không là giá trị của chính sách xác định nào; tiêu chuẩn "chính sách ổn định" không áp dụng cho lặp giá trị, và điều kiện dừng dựa trên phần dư.
- Ngưỡng $\theta$ kiểm soát sai số của bảng; tổn thất của chính sách trích ra có chặn riêng, nêu ở mục Đọc thêm.
:::

**Trong thực hành.** Thuật toán 04.28 chỉ cần mảng $Q$ cỡ $(n,m)$ và hai phép rút gọn theo trục hành động, một cho cực đại và một cho vị trí cực đại. Trong bài thực hành CartPole với $\gamma=0{,}99$, $\kappa=0{,}01$, $\theta=10^{-4}$, một lần chạy đã nhúng trong notebook dừng với nhãn "đạt ngưỡng" sau $736$ lượt quét, phần dư $9{,}88\cdot10^{-5}$, chặn $9{,}88\cdot10^{-3}$; sai số thật đo bằng giá trị của lặp chính sách là $7{,}84\cdot10^{-3}$.

Số lượt quét này có thể so với một chặn trước. Với lượt quét đồng bộ, $\Delta_*(V_k)=\lVert T_*V_k-T_*V_{k-1}\rVert_\infty\le\gamma\Delta_*(V_{k-1})$ theo Mệnh đề 04.24, nên $\Delta_*(V_k)\le\gamma^k\Delta_*(V_0)$. Trong bài thực hành, $\Delta_*(V_0)=1$ vì mọi phần thưởng bằng $1$, nên số lượt quét đủ dùng là $k\ge\ln\theta/\ln\gamma$ với $\theta=(1-\gamma)\cdot0{,}01$ ứng với từng $\gamma$. Một lần chạy đã nhúng trong notebook cho $65$ lượt so với chặn $66$ khi $\gamma=0{,}9$, và $736$ so với $917$ khi $\gamma=0{,}99$. Chính sách trích ra trùng chính sách của lặp chính sách tại cả $324$ ô, dù có $3$ ô mà hai hành động gần đồng hạng tới mức phép trích có thể chọn khác.

### 4.5 Dãy năm ô

Mô hình hai trạng thái không có trạng thái kết thúc. Ví dụ sau, lấy từ Bài giảng gốc (2025–2026), trang 25–28, có một ô đích kết thúc và cho thấy giá trị lan dần từ đích qua các lượt quét.

![Năm ô vuông xếp thành hàng c1, c2, c3, c4, c5. Ô c5 có viền kép, ghi "Đích", là trạng thái kết thúc. Mũi tên cong tại c1 ghi "Trái ở c1: ở lại".](img/lec-04/dp04-five-cell-plain.svg)

Mỗi ô chưa kết thúc có hai hành động $\mathrm{trai}$ và $\mathrm{phai}$; mũi tên cong ở $\mathrm c_1$ là chuyển giữ tác tử tại chỗ, viền kép đánh dấu trạng thái kết thúc $\mathrm c_5$.

::: example Ví dụ 04.14 (Lặp giá trị trên dãy năm ô)
**Dữ kiện.** Các ô $\mathrm c_1,\dots,\mathrm c_5$; $\mathrm c_5$ là trạng thái kết thúc. Hành động $\mathrm{trai}$, $\mathrm{phai}$ chuyển xác định sang ô bên cạnh; $\mathrm{trai}$ tại $\mathrm c_1$ giữ nguyên $\mathrm c_1$. Phần thưởng $10$ cho chuyển $\mathrm c_4\to\mathrm c_5$, $-1$ cho mọi chuyển khác; $\gamma=0{,}9$; $V_0=0$.

**Bảng lượt quét.**

| $k$ | $\mathrm c_1$ | $\mathrm c_2$ | $\mathrm c_3$ | $\mathrm c_4$ | $\mathrm c_5$ |
|---|---:|---:|---:|---:|---:|
| $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| $1$ | $-1$ | $-1$ | $-1$ | $10$ | $0$ |
| $2$ | $-1{,}9$ | $-1{,}9$ | $8$ | $10$ | $0$ |
| $3$ | $-2{,}71$ | $6{,}2$ | $8$ | $10$ | $0$ |
| $4$ | $4{,}58$ | $6{,}2$ | $8$ | $10$ | $0$ |

**Một ô mẫu.** Tại lượt quét thứ hai, ô $\mathrm c_3$ đọc $V_1$: nhánh $\mathrm{trai}$ cho $-1+0{,}9\cdot V_1(\mathrm c_2)=-1+0{,}9\cdot(-1)=-1{,}9$; nhánh $\mathrm{phai}$ cho $-1+0{,}9\cdot V_1(\mathrm c_4)=-1+0{,}9\cdot10=8$; cực đại là $8$.

**Diễn giải.** Mỗi lượt quét đồng bộ đẩy ảnh hưởng của phần thưởng $10$ lùi thêm một ô. Trước đó, ô chỉ thấy chi phí $-1$ mỗi bước: $\mathrm c_1$ đi qua $-1$, $-1{,}9$, $-2{,}71$ rồi nhảy lên $4{,}58$.

**Kiểm tra lại.** Đi phải liên tục từ $\mathrm c_1$ qua bốn bước cho lợi tức $-1-0{,}9-0{,}81+0{,}729\cdot10=4{,}58=V_4(\mathrm c_1)$.
:::

![Cùng năm ô c1 tới c5 như hình trước, thêm bốn mũi tên chỉ sang phải tại c1, c2, c3, c4, ghi "Mũi tên: chính sách tối ưu".](img/lec-04/dp04-five-cell.svg)

Hình trên vẽ chính sách tham lam theo $V_4$: đi phải tại cả bốn ô chưa kết thúc; các mũi tên không loại hành động trái khỏi mô hình. Bài tập 04.4 kiểm $V_4$ có phải điểm bất động của $T_*$ hay không; nếu phải, lặp giá trị trên ví dụ này tới đúng $v_*$ sau hữu hạn lượt quét. Đó là tính chất của ví dụ; Hệ quả 04.26 chỉ bảo đảm hội tụ dần.

::: exercise Bài tập 04.4 (Điểm bất động trên dãy năm ô)
Cho dãy năm ô $\mathrm c_1,\dots,\mathrm c_5$ với $\mathrm c_5$ kết thúc; hành động $\mathrm{trai}$, $\mathrm{phai}$ chuyển xác định sang ô bên cạnh, $\mathrm{trai}$ tại $\mathrm c_1$ giữ nguyên $\mathrm c_1$; phần thưởng $10$ cho chuyển $\mathrm c_4\to\mathrm c_5$ và $-1$ cho mọi chuyển khác; $\gamma=0{,}9$. Bảng $V_4=(4{,}58;\,6{,}2;\,8;\,10;\,0)$.

(a) Tính hai giá trị nhìn trước tại mỗi ô chưa kết thúc và bảng $T_*V_4$.

(b) Xác định $\Delta_*(V_4)$ và chính sách tham lam theo $V_4$.

(c) Giải thích vì sao $V_4(\mathrm c_5)=0$ dù chuyển vào $\mathrm c_5$ nhận phần thưởng $10$.
:::

::: hint
Nhánh $\mathrm{trai}$ tại $\mathrm c_1$ đọc giá trị tiếp nối của chính $\mathrm c_1$. Nhánh $\mathrm{phai}$ tại $\mathrm c_4$ đọc $V_4(\mathrm c_5)=0$.
:::

::: solution
**(a)** Tại $\mathrm c_1$: $\mathrm{trai}$ cho $-1+0{,}9\cdot4{,}58=3{,}122$, $\mathrm{phai}$ cho $-1+0{,}9\cdot6{,}2=4{,}58$. Tại $\mathrm c_2$: $\mathrm{trai}$ cho $3{,}122$, $\mathrm{phai}$ cho $-1+0{,}9\cdot8=6{,}2$. Tại $\mathrm c_3$: $\mathrm{trai}$ cho $-1+0{,}9\cdot6{,}2=4{,}58$, $\mathrm{phai}$ cho $-1+0{,}9\cdot10=8$. Tại $\mathrm c_4$: $\mathrm{trai}$ cho $-1+0{,}9\cdot8=6{,}2$, $\mathrm{phai}$ cho $10+0{,}9\cdot0=10$. Vậy $T_*V_4=(4{,}58;\,6{,}2;\,8;\,10;\,0)$.

**(b)** $T_*V_4=V_4$ nên $\Delta_*(V_4)=0$; chính sách tham lam đi phải tại $\mathrm c_1,\dots,\mathrm c_4$. Theo Hệ quả 04.27, $V_4=v_*$, và theo Định lý 04.25(b), chính sách này tối ưu.

**(c)** Phần thưởng $10$ thuộc về chuyển $\mathrm c_4\to\mathrm c_5$ và được tính trong $Q_V(\mathrm c_4,\mathrm{phai})$. Sau khi vào $\mathrm c_5$, lượt kết thúc và không còn phần thưởng nào, nên giá trị của trạng thái kết thúc bằng $0$.

**Kiểm tra lại.** Tại mỗi ô, nhánh $\mathrm{phai}$ lớn hơn nhánh $\mathrm{trai}$, và giá trị nhánh $\mathrm{phai}$ trùng $V_4$.
:::

Như vậy, gộp cải thiện vào một lượt quét cho toán tử Bellman tối ưu $T_*$ (Định nghĩa 04.22), một ánh xạ co (Mệnh đề 04.24). Điểm bất động duy nhất của nó là $v_*$, và một chính sách Markov dừng, xác định tham lam theo $v_*$ là tối ưu trên mọi chính sách (Định lý 04.25). Lặp giá trị hội tụ với tốc độ $\gamma^k$ (Hệ quả 04.26), dừng theo phần dư với chặn sai số (Hệ quả 04.27), và Thuật toán 04.28 trả bảng, chính sách và phần dư của cùng một bảng. Tuy nhiên, mỗi lượt quét vẫn cập nhật mọi trạng thái từ một bảng cũ và cần $p$ đầy đủ trên một tập hữu hạn; trong Mục 5, chúng ta xét hai giới hạn này.

## 5. Lịch cập nhật và giới hạn của mô hình bảng

Các thuật toán của Mục 1–4 quét toàn bộ tập trạng thái ở mỗi lượt và dùng kỳ vọng đầy đủ theo $p$. Trên dãy năm ô, phần thưởng $10$ cần bốn lượt quét để ảnh hưởng tới $\mathrm c_1$ (Ví dụ 04.14), vì mỗi lượt quét đồng bộ chỉ đưa ảnh hưởng đó lùi thêm một ô. Trên CartPole, trạng thái là vectơ thực bốn chiều, nên cả tập trạng thái hữu hạn lẫn mô hình $p$ đều chưa có. Chúng ta xét hai câu hỏi: tổ chức cập nhật rẻ hơn mà vẫn hội tụ được không, và các bảo đảm còn lại gì khi mô hình bảng chỉ xấp xỉ môi trường thật.

<!-- note-topic-id: lec-04-part-10 -->
### 5.1 Chi phí một lượt quét

Chi phí của một lượt quét được tính bằng số số hạng trong các tổng của (2.1). Khi phần thưởng được gộp thành kỳ vọng $r(s,a)=\sum_{s',r}p(s',r\mid s,a)\,r$ và xác suất chuyển biên $p(s'\mid s,a)=\sum_rp(s',r\mid s,a)$ được lưu sẵn, giá trị nhìn trước là $Q_V(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)V(s')$.

::: example Ví dụ 04.15 (Đếm số hạng của một lượt quét)
**Dữ kiện.** CartPole rời rạc hóa trong bài thực hành: $n=324$ ô, $m=2$ hành động, cộng một trạng thái kết thúc; một lần chạy đã nhúng trong notebook cho số trạng thái kế tiếp có xác suất dương của mỗi cặp $(s,a)$ từ $2$ tới $12$, trung vị $6$.

**CartPole, lưu đặc.** Mỗi giá trị nhìn trước tổng trên $325$ trạng thái kế tiếp, nên một lượt quét có $324\cdot2\cdot325=210\,600$ số hạng.

**CartPole, lưu thưa.** Chỉ duyệt các chuyển có xác suất dương: không quá $324\cdot2\cdot12=7\,776$ số hạng.

**Kiểm tra lại.** $210\,600/7\,776\approx27\approx325/12$.
:::

::: remark Nhận xét 04.30 (Chi phí một lượt quét)
Với $n$ trạng thái chưa kết thúc, tối đa $m$ hành động mỗi trạng thái, $r(s,a)$ và $p(s'\mid s,a)$ lưu sẵn, và tối đa $d$ trạng thái kế tiếp có xác suất dương cho mỗi cặp $(s,a)$:

- một giá trị nhìn trước tốn $O(n)$ phép tính khi lưu $p$ dạng đặc và $O(d)$ khi lưu dạng thưa, vì tổng theo $s'$ có chừng đó số hạng;
- một lượt quét của $T_*$, hoặc của $T_\pi$ với $\pi$ ngẫu nhiên, cần tối đa $nm$ giá trị nhìn trước, nên tốn $O(n^2m)$ hoặc $O(nmd)$; với $\pi$ xác định, bỏ thừa số $m$;
- bộ nhớ cho mô hình là $O(n^2m)$ hoặc $O(nmd)$, cho bảng giá trị và chính sách là $O(n)$.

Tổng chi phí còn nhân với số lượt quét, vốn phụ thuộc $\gamma$, khởi tạo và ngưỡng (Hệ quả 04.26); giải hệ tuyến tính đặc của Hệ quả 04.6(c) bằng khử Gauss tốn $O(n^3)$.
:::

Nhận xét 04.30 chỉ ra hai hướng giảm chi phí. Hướng thứ nhất giảm số lượt quét cần thiết, bằng cách để thông tin mới lan ngay trong cùng một lượt quét. Hướng thứ hai bỏ yêu cầu quét toàn bộ, chỉ cập nhật những trạng thái được chọn.

### 5.2 Cập nhật tại chỗ và quy hoạch động bất đồng bộ

Về mặt ý tưởng, cập nhật tại chỗ (in-place) chỉ dùng một bảng: mỗi giá trị mới ghi đè ngay giá trị cũ và được dùng cho các ô tính sau trong cùng lượt quét. Thứ tự tính các ô vì vậy bắt đầu có ảnh hưởng.

![Ba khung xếp dọc. Khung đầu "Khởi tạo: (0, 0)". Khung thứ hai "① Cập nhật s0: (1, 0)". Khung thứ ba "② Cập nhật s1: (1; 2,9)", với mũi tên chỉ rằng giá trị mới 1 của s0 được dùng ngay.](img/lec-04/dp04-update-order.svg)

Hình trên đi từ trên xuống: ô $\mathrm s_0$ được cập nhật trước thành $1$, rồi ô $\mathrm s_1$ đọc ngay giá trị $1$ đó thay vì giá trị cũ $0$, nên nhận $2+0{,}9\cdot1=2{,}9$.

::: example Ví dụ 04.16 (Cập nhật tại chỗ trên hai mô hình)
**Dữ kiện.** (i) Mô hình hai trạng thái, $\gamma=0{,}9$, đánh giá $\pi_0=(\mathrm a,\mathrm a)$: $(T_{\pi_0}V)(\mathrm s_0)=1+0{,}9V(\mathrm s_0)$, $(T_{\pi_0}V)(\mathrm s_1)=2+0{,}9V(\mathrm s_0)$; bảng đầu $(0,0)$; thứ tự $\mathrm s_0$ rồi $\mathrm s_1$. (ii) Dãy năm ô $\mathrm c_1,\dots,\mathrm c_5$, $\mathrm c_5$ kết thúc, hành động $\mathrm{trai}$, $\mathrm{phai}$ chuyển xác định sang ô bên cạnh, $\mathrm{trai}$ tại $\mathrm c_1$ giữ nguyên ô; phần thưởng $10$ cho $\mathrm c_4\to\mathrm c_5$, $-1$ cho chuyển khác; toán tử $T_*$; bảng đầu $0$; thứ tự $\mathrm c_4,\mathrm c_3,\mathrm c_2,\mathrm c_1$.

**(i) Đánh giá tại chỗ.** $V(\mathrm s_0)\leftarrow1+0{,}9\cdot0=1$; rồi $V(\mathrm s_1)\leftarrow2+0{,}9\cdot1=2{,}9$. Bảng sau một lượt quét là $(1;\,2{,}9)$, so với $(1,2)$ của lượt quét đồng bộ.

**(ii) Lặp giá trị tại chỗ, thứ tự ngược.**

$$
\begin{aligned}
V(\mathrm c_4)&\leftarrow\max\{-1+0{,}9\cdot0;\ 10+0{,}9\cdot0\}=10,\\
V(\mathrm c_3)&\leftarrow\max\{-1+0{,}9\cdot0;\ -1+0{,}9\cdot10\}=8,\\
V(\mathrm c_2)&\leftarrow\max\{-1+0{,}9\cdot0;\ -1+0{,}9\cdot8\}=6{,}2,\\
V(\mathrm c_1)&\leftarrow\max\{-1+0{,}9\cdot0;\ -1+0{,}9\cdot6{,}2\}=4{,}58 .
\end{aligned}
$$

Ở mỗi dòng, nhánh đầu là $\mathrm{trai}$ và đọc ô bên trái, chưa được cập nhật nên còn $0$; tại $\mathrm c_1$ nhánh $\mathrm{trai}$ đọc chính $\mathrm c_1$, cũng còn $0$. Sau một lượt quét, bảng là $(4{,}58;\,6{,}2;\,8;\,10;\,0)=V_4$ của Ví dụ 04.14.

**Diễn giải.** Lượt quét tại chỗ theo thứ tự ngược từ đích cần một lượt thay vì bốn; theo thứ tự $\mathrm c_1,\dots,\mathrm c_4$, nó chỉ cho $(-1;\,-1;\,-1;\,10;\,0)$, như lượt quét đồng bộ.

**Kiểm tra lại.** Ở (ii), áp dụng $T_*$ tại $\mathrm c_1$ cho bảng thu được: $\max\{-1+0{,}9\cdot4{,}58;\ -1+0{,}9\cdot6{,}2\}=\max\{3{,}122;\ 4{,}58\}=4{,}58$, giá trị không đổi (ba ô còn lại: Bài tập 04.4). Lợi ích của thứ tự ngược là tính chất riêng của ví dụ này.
:::

Cập nhật tại chỗ theo một thứ tự cố định vẫn đi qua mọi trạng thái trong mỗi lượt. Quy hoạch động bất đồng bộ (asynchronous dynamic programming) bỏ luôn yêu cầu đó: ở mỗi bước chỉ cập nhật một trạng thái, chọn theo một lịch (schedule) bất kỳ, và luôn đọc các giá trị mới nhất. Với lịch $\mathrm c_4,\mathrm c_3,\mathrm c_2,\mathrm c_1$, bốn bước đầu của thuật toán dưới đây trùng phép tính ở Ví dụ 04.16(ii).

::: algorithm Thuật toán 04.31 (Lặp giá trị bất đồng bộ)
**Đầu vào.** Mô hình $p$ của MDP hữu hạn; $\gamma\in[0,1)$; một lịch $\sigma_0,\sigma_1,\sigma_2,\dots$ gồm các trạng thái chưa kết thúc.

**Đầu ra.** Bảng $V$, chính sách tham lam $\pi_V$, phần dư $\Delta_*(V)$ và nhãn "đạt ngưỡng" hoặc "hết ngân sách".

**Giả thiết.** Mô hình được biết đầy đủ; mỗi cập nhật đọc giá trị mới nhất của mọi trạng thái.

**Tham số.** Ngưỡng $\theta=(1-\gamma)\kappa$; ngân sách $K$ bước cập nhật; tập các mốc kiểm tra, luôn gồm bước $K$.

**Khởi tạo.** $V(s)=0$ với mọi $s\in\mathcal S$; $V(s_{\mathrm{term}})=0$; $j=0$.

1. Lấy trạng thái $s=\sigma_j$ theo lịch; gán $V(s)\leftarrow(T_*V)(s)=\max_aQ_V(s,a)$; giữ nguyên mọi ô khác.
2. Gán $j\leftarrow j+1$. Nếu $j$ không phải mốc kiểm tra, quay lại bước 1.
3. Tại mốc kiểm tra: giữ $V$ cố định, tính $\Delta_*(V)$ trên toàn bảng và $\pi_V$. Nếu $\Delta_*(V)\le\theta$, trả kết quả với nhãn "đạt ngưỡng"; nếu $j=K$, trả với nhãn "hết ngân sách"; nếu không, quay lại bước 1.

**Điều kiện dừng.** Bước 3. Với mọi bảng $V$, $\Delta_*(V)\le\lVert T_*V-v_*\rVert_\infty+\lVert v_*-V\rVert_\infty\le(1+\gamma)\lVert V-v_*\rVert_\infty$ (bất đẳng thức tam giác, $v_*=T_*v_*$, Mệnh đề 04.24). Gọi $V_j$ là bảng sau $j$ bước cập nhật. Khi bỏ ngân sách ($K=\infty$), tập mốc kiểm tra không bị chặn và mỗi trạng thái xuất hiện vô hạn lần trong lịch, Định lý 04.32 cho $\lVert V_j-v_*\rVert_\infty\to0$, nên nhãn "đạt ngưỡng" xuất hiện sau hữu hạn bước. Với $K$ hữu hạn, nhãn này xuất hiện nếu có mốc $j\le K$ thỏa $\Delta_*(V_j)\le\theta$; nếu không, thuật toán trả "hết ngân sách".

**Chi phí mỗi bước.** Bước 1 tốn $O(nm)$ với mô hình đặc, $O(md)$ với mô hình thưa; bước 3 tốn như một lượt quét đồng bộ.
:::

Định lý sau cho bảo đảm hội tụ của thuật toán. Chứng minh chỉ cần hai kết quả đã có: $T_*$ co từng thành phần với hệ số $\gamma$ (Mệnh đề 04.24) và $v_*$ là điểm bất động của $T_*$ (Định lý 04.25(a)).

::: theorem Định lý 04.32 (Hội tụ của lặp giá trị bất đồng bộ)
**Giả thiết.** MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$. Dãy bảng $V_0,V_1,\dots$ sinh bởi bước 1 của Thuật toán 04.31: $V_{j+1}(\sigma_j)=(T_*V_j)(\sigma_j)$ và $V_{j+1}(s)=V_j(s)$ với $s\ne\sigma_j$. Mỗi trạng thái chưa kết thúc xuất hiện vô hạn lần trong lịch.

**Kết luận.** $\lVert V_j-v_*\rVert_\infty$ không tăng theo $j$ và tiến về $0$. Cụ thể, nếu trong đoạn bước $[j_0,j_1)$ mỗi trạng thái được cập nhật ít nhất một lần thì $\lVert V_{j_1}-v_*\rVert_\infty\le\gamma\lVert V_{j_0}-v_*\rVert_\infty$.

**Điều kiện áp dụng.** Mỗi cập nhật dùng giá trị mới nhất của bảng; lịch có thể tùy ý, kể cả ngẫu nhiên, miễn mọi trạng thái được cập nhật vô hạn lần.

**Phạm vi.** Định lý không xét trường hợp cập nhật đọc giá trị trễ, như trong tính toán phân tán. Nó không cho tốc độ khi các đoạn phủ toàn bộ tập trạng thái dài ra không giới hạn.
:::

::: proof Chứng minh Định lý 04.32
Đặt $e_j=\lVert V_j-v_*\rVert_\infty$.

**Bước 1 (sai số không tăng).** Chỉ ô $\sigma_j$ thay đổi ở bước $j$. Với ô đó,

$$
\begin{aligned}
\bigl\lvert V_{j+1}(\sigma_j)-v_*(\sigma_j)\bigr\rvert
&=\bigl\lvert(T_*V_j)(\sigma_j)-(T_*v_*)(\sigma_j)\bigr\rvert &&\text{(}v_*=T_*v_*\text{, Định lý 04.25)}\\
&\le\gamma\,e_j &&\text{(Mệnh đề 04.24)}.
\end{aligned}
$$

Các ô khác giữ sai số cũ, không vượt $e_j$. Vậy $e_{j+1}\le e_j$.

**Bước 2 (một đoạn phủ).** Giả sử mỗi trạng thái được cập nhật ít nhất một lần trong $[j_0,j_1)$. Với trạng thái $s$, gọi $j$ là lần cập nhật cuối của $s$ trong đoạn. Sau bước $j$, ô $s$ không đổi tới $j_1$, nên

$$
\begin{aligned}
\lvert V_{j_1}(s)-v_*(s)\rvert
&=\lvert V_{j+1}(s)-v_*(s)\rvert &&\text{(ô } s \text{ không đổi sau bước } j)\\
&\le\gamma e_j &&\text{(Bước 1, ô được cập nhật)}\\
&\le\gamma e_{j_0} &&\text{(Bước 1, } e \text{ không tăng, } j\ge j_0).
\end{aligned}
$$

Lấy cực đại theo $s$ cho $e_{j_1}\le\gamma e_{j_0}$.

**Bước 3 (vô hạn đoạn phủ).** Vì mỗi trạng thái xuất hiện vô hạn lần, ta chia được các bước thành vô hạn đoạn liên tiếp $[j_0,j_1),[j_1,j_2),\dots$ với $j_0=0$, mỗi đoạn phủ mọi trạng thái: chọn $j_{l+1}$ là bước đầu tiên sau $j_l$ mà mọi trạng thái đã được cập nhật trong $[j_l,j_{l+1})$. Theo Bước 2, $e_{j_L}\le\gamma^Le_0\to0$ khi $L\to\infty$; theo Bước 1, cả dãy $e_j$ không tăng nên cũng tiến về $0$. $\square$
:::

::: remark Nhận xét 04.33 (Lịch cập nhật, phần dư và điều kiện "vô hạn lần")
- Lượt quét tại chỗ của lặp giá trị là trường hợp riêng của Thuật toán 04.31, với lịch lặp lại một thứ tự cố định của toàn bộ $\mathcal S$; Định lý 04.32 áp dụng cho nó.
- Lượng thay đổi lớn nhất trong một lượt quét tại chỗ không phải phần dư của bảng cuối; phần dư phải đo bằng cách giữ bảng cố định và áp dụng $T_*$ cho mọi trạng thái, như bước 3 của Thuật toán 04.31.
- Giả thiết "vô hạn lần" được dùng ở Bước 3 của chứng minh, vì cần vô hạn đoạn phủ. Nếu một trạng thái bị bỏ qua từ một thời điểm nào đó, giá trị của nó đứng yên, và các trạng thái còn lại, nếu được cập nhật vô hạn lần, hội tụ về điểm bất động của bài toán đã cố định ô đó, nói chung khác $v_*$ (Bài tập 04.5).
:::

Sutton và Barto (2018, §4.5, tr. 85) phát biểu kết quả của Định lý 04.32; phần ghi chú lịch sử của chương (tr. 90) dẫn Bertsekas và Tsitsiklis (1989) cho các thuật toán bất đồng bộ.

**Trong thực hành.** Lịch bất đồng bộ cho phép tập trung tính toán vào các trạng thái mà tác tử gặp, chẳng hạn cập nhật trạng thái hiện tại sau mỗi bước tương tác; bài thực hành CartPole có hàm lặp giá trị tại chỗ ở nhiệm vụ 6 nhưng chưa nhúng kết quả. Khi lịch do quỹ đạo quyết định, điều kiện "vô hạn lần" không tự thỏa: trong một lần chạy đã nhúng trong notebook, chính sách ngẫu nhiên chỉ đi qua $64$ trong $324$ ô.

<!-- note-topic-id: lec-04-part-07 -->
### 5.3 Lặp chính sách tổng quát

Ba thuật toán của chương khác nhau ở mức độ hoàn tất của bước đánh giá trước mỗi lần cải thiện. Lặp chính sách đánh giá tới giá trị chính xác; lặp giá trị đánh giá đúng một lượt quét; lịch bất đồng bộ đánh giá và cải thiện từng trạng thái một. Về mặt ý tưởng, cả ba là sự tương tác của hai quá trình, đánh giá và cải thiện.

![Hai khối nối bằng hai mũi tên ngược chiều. Khối "Bảng giá trị V" ghi "Điều chỉnh theo π"; khối "Chính sách π" ghi "Chọn theo V". Mũi tên "Đánh giá" đi từ chính sách sang bảng; mũi tên "Cải thiện" đi từ bảng sang chính sách.](img/lec-04/dp04-gpi.svg)

Hình trên đọc theo hai mũi tên. Mũi tên "Đánh giá" làm $V$ khớp với $\pi$, và sau bước đó $\pi$ nói chung không còn tham lam theo bảng mới; mũi tên "Cải thiện" làm $\pi$ tham lam theo $V$, và sau bước đó $V$ không còn là $v_\pi$. Cả hai đứng yên chỉ khi hai đòi hỏi cùng thỏa, và theo Định lý 04.25 điểm đó là $v_*$. Đây là mô tả, chưa phải định nghĩa.

::: definition Định nghĩa 04.34 (Lặp chính sách tổng quát)
Lặp chính sách tổng quát (generalized policy iteration, GPI) là tên chung của các quy trình duy trì đồng thời một bảng giá trị $V$ và một chính sách $\pi$, xen kẽ hai loại bước theo một thứ tự và mức độ hoàn tất tùy ý: bước đánh giá đưa $V$ lại gần $v_\pi$, và bước cải thiện thay $\pi$ bằng một chính sách tham lam hơn theo $V$.
:::

| Phương pháp | Mức hoàn tất đánh giá trước mỗi cải thiện | Điều kiện dừng | Bảo đảm trong chương |
|---|---|---|---|
| Lặp chính sách (Thuật toán 04.17) | đầy đủ, $V=v_\pi$ | $\pi'=\pi$ | dừng hữu hạn tại chính sách tối ưu (Mệnh đề 04.18, Định lý 04.25) |
| Lặp giá trị (Thuật toán 04.28) | một lượt quét | $\Delta_*(V)\le\theta$ | hội tụ $\gamma^k$, chặn sai số (Hệ quả 04.26, 04.27) |
| Bất đồng bộ (Thuật toán 04.31) | một trạng thái | $\Delta_*(V)\le\theta$ tại mốc kiểm tra | hội tụ khi mọi trạng thái được cập nhật vô hạn lần (Định lý 04.32) |

Điểm đứng yên thỏa $V=T_\pi V=T_*V$. Định nghĩa 04.34 không kèm bảo đảm rằng mọi cách xen kẽ đều tới trạng thái đứng yên đó; mỗi phương pháp trong bảng có bảo đảm riêng, với giả thiết riêng. Bài 05 và Bài 06 dùng lại khuôn này khi bước đánh giá phải ước lượng từ mẫu thay vì tính từ $p$.

<!-- note-topic-id: lec-04-part-12 -->
### 5.4 CartPole rời rạc hóa

Mọi kết quả của chương giả thiết tập trạng thái hữu hạn và mô hình $p$ đã biết. Bài giảng gốc (2025–2026), trang 35–37, dùng CartPole làm ví dụ. CartPole có trạng thái $(x,\dot x,\phi,\dot\phi)$ gồm vị trí xe, vận tốc xe, góc cột so với phương thẳng đứng và vận tốc góc, là một vectơ thực; hai hành động là đẩy xe sang trái (hành động $0$) và sang phải (hành động $1$); phần thưởng là $+1$ mỗi bước, và lượt kết thúc khi $\lvert x\rvert>2{,}4$ hoặc $\lvert\phi\rvert>12^\circ$.

![Sơ đồ xe trên ray và cột gắn trên xe. Các nhãn x, x chấm chỉ vị trí và vận tốc xe; các nhãn φ, φ chấm chỉ góc và vận tốc góc của cột. Ô bên cạnh ghi "Khoảng chia 3 · 3 · 6 · 6".](img/lec-04/dp04-cartpole-bins.svg)

Hình trên ghi bốn biến trạng thái và số khoảng chia của từng biến; mỗi tổ hợp chỉ số khoảng là một ô. Bài thực hành viết góc cột là $\theta$ (biến `theta` trong mã) và chỉ số khoảng của nó là $b_\theta$; trong chương này, góc đó là $\phi$, chỉ số khoảng là $b_\phi$, còn $\theta$ là ngưỡng dừng.

::: example Ví dụ 04.17 (Từ trạng thái liên tục tới mô hình bảng)
**Dữ kiện.** Theo bài thực hành CartPole: $x$ chia $3$ khoảng với điểm cắt $\pm0{,}8$; $\dot x$ chia $3$ khoảng với điểm cắt $\pm0{,}5$; $\phi$ chia $6$ khoảng đều $4^\circ$ trên $[-12^\circ,12^\circ]$; $\dot\phi$ chia $6$ khoảng với điểm cắt $-\tfrac23,-\tfrac13,0,\tfrac13,\tfrac23$ rad/s. Chỉ số ô $s=((b_x\cdot3+b_{\dot x})\cdot6+b_\phi)\cdot6+b_{\dot\phi}$, với $b$ là chỉ số khoảng tính từ $0$.

**Số ô và một trạng thái.** Có $3\cdot3\cdot6\cdot6=324$ ô chưa kết thúc, cộng một trạng thái kết thúc. Với $(x,\dot x,\phi,\dot\phi)=(0{,}1;\,-0{,}7;\,0{,}05;\,0{,}4)$: $b_x=1$, $b_{\dot x}=0$ vì $-0{,}7<-0{,}5$, $b_\phi=3$ vì $0{,}05$ rad $\approx2{,}9^\circ\in[0^\circ,4^\circ)$, $b_{\dot\phi}=4$ vì $0{,}4\in[\tfrac13,\tfrac23)$. Chỉ số ô là $((1\cdot3+0)\cdot6+3)\cdot6+4=130$.

**Ước lượng mô hình.** Rời rạc hóa không cho $p$. Bài thực hành lấy $M$ trạng thái đều trong ô, cho bộ mô phỏng đi một bước, và đặt $\hat p(s'\mid s,a)=N(s,a,s')/M$, với $N(s,a,s')$ là số mẫu sang ô $s'$. Một lần chạy đã nhúng trong notebook với $M=5$ tại ô $130$, hành động $1$, cho ba mẫu sang ô $129$ và hai mẫu sang ô $165$, nên $\hat p(129\mid130,1)=0{,}6$ và $\hat p(165\mid130,1)=0{,}4$.

**Diễn giải.** Động lực học CartPole tất định; xác suất trong $\hat p$ đến từ thông tin bị gộp mất trong ô.

**Kiểm tra lại.** $0{,}6+0{,}4=1$; mô hình đầy đủ của bài thực hành dùng $M=200$ và kiểm tra mỗi hàng $\hat p(\cdot\mid s,a)$ có tổng bằng $1$.
:::

Trên MDP ước lượng, mọi thuật toán của chương chạy đúng như trên một MDP hữu hạn thật, và một bước tính tay vẫn làm được.

::: example Ví dụ 04.18 (Hai lượt quét lặp giá trị tại một ô của CartPole)
**Dữ kiện.** MDP ước lượng của bài thực hành: $\hat r(s,a)=1$ với mọi cặp, $\gamma=0{,}99$, $V_0=0$. Tại ô $s_h=71$, một lần chạy đã nhúng trong notebook cho $\hat p(s_{\mathrm{term}}\mid s_h,a)=0{,}435$ với cả hai hành động.

**Lượt quét thứ nhất.** $V_1(s)=\max_a\bigl[1+0{,}99\cdot0\bigr]=1$ tại mọi ô.

**Lượt quét thứ hai tại $s_h$.** Các ô chưa kết thúc có $V_1=1$, trạng thái kết thúc có giá trị $0$, nên

$$
V_2(s_h)=1+0{,}99\bigl(1-\hat p(s_{\mathrm{term}}\mid s_h,a)\bigr)=1+0{,}99\cdot0{,}565=1{,}55935 .
$$

Hai hành động cho cùng kết quả, vì trong bộ mô phỏng, vị trí và góc ở bước kế tiếp tính từ vận tốc trước khi lực tác động, nên việc kết thúc ở bước kế tiếp không phụ thuộc hành động.

**Kiểm tra lại.** $1-0{,}435=0{,}565$ và $0{,}99\cdot0{,}565=0{,}55935$; notebook in cùng giá trị $1{,}55935$ từ hàm đánh giá của nó.
:::

::: remark Nhận xét 04.35 (Những gì một chứng nhận Bellman trên mô hình gộp không nói)
- Gộp trạng thái vào ô không bảo đảm tính Markov, giả thiết của Định lý 04.25: lịch sử các ô có thể mang thông tin về vị trí bên trong ô hiện tại.
- $\hat p$ là ước lượng từ mẫu, phụ thuộc cách lấy mẫu trong ô và hạt giống ngẫu nhiên (random seed). Một chứng nhận $\Delta_*(V)=0$ thuộc về MDP $(\hat p,\hat r)$, không thuộc về CartPole.
- Sai số trong môi trường thật gồm sai số lặp, chặn được bởi Hệ quả 04.27, và sai số do rời rạc hóa và ước lượng mô hình, không có chặn nào trong chương.
- Chia mịn hơn làm số ô tăng theo tích số khoảng. Khi mỗi biến chia cùng một số khoảng, số ô là lũy thừa bậc bốn của số đó: $10$ khoảng cho $10^4$ ô, $20$ khoảng cho $1{,}6\cdot10^5$ ô; với cùng số mẫu, mỗi ô nhận ít dữ liệu hơn. Khi số biến trạng thái tăng, số ô tăng theo hàm mũ của số biến; Sutton và Barto (2018, §4.7, tr. 87) gọi hiện tượng này là lời nguyền số chiều (curse of dimensionality) và coi đó là khó khăn của chính bài toán, không riêng của quy hoạch động. Bài 07 thay bảng bằng một hàm có tham số khi số ô quá lớn.
:::

::: exercise Bài tập 04.5 (Lịch bỏ sót một trạng thái)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$; $v_*=(27,30)$. Lặp giá trị bất đồng bộ bắt đầu từ $V=(0,0)$ với lịch chỉ gồm $\mathrm s_0$, lặp lại mãi mãi.

(a) Viết quy tắc cập nhật tại $\mathrm s_0$ và tìm giới hạn của $V(\mathrm s_0)$.

(b) Cho biết giá trị của $V(\mathrm s_1)$ và so bảng giới hạn với $v_*$.

(c) Chỉ ra giả thiết của Định lý 04.32 bị vi phạm và bước của chứng minh không còn đúng.
:::

::: hint
Vì $V(\mathrm s_1)$ không bao giờ được cập nhật, nhánh $\mathrm b$ tại $\mathrm s_0$ luôn đọc giá trị tiếp nối $0$.
:::

::: solution
**(a)** Mỗi bước gán $V(\mathrm s_0)\leftarrow\max\{1+0{,}9V(\mathrm s_0);\ 0+0{,}9\cdot0\}$. Từ $V(\mathrm s_0)=0$, nhánh $\mathrm a$ luôn lớn hơn, và dãy $1;\,1{,}9;\,2{,}71;\dots$ hội tụ về nghiệm của $x=1+0{,}9x$, tức $x=10$.

**(b)** $V(\mathrm s_1)=0$ mãi mãi. Bảng giới hạn $(10,0)$ khác $v_*=(27,30)$ ở cả hai trạng thái; chính sách tham lam theo bảng này tại $\mathrm s_0$ là $\mathrm a$, trong khi chính sách tối ưu chọn $\mathrm b$.

**(c)** Giả thiết "mỗi trạng thái chưa kết thúc xuất hiện vô hạn lần trong lịch" bị vi phạm vì $\mathrm s_1$ không xuất hiện lần nào. Bước 2 của chứng minh cần các đoạn phủ mọi trạng thái; ở đây không có đoạn nào như vậy, nên sai số tại $\mathrm s_1$ giữ nguyên $30$.

**Kiểm tra lại.** $x=10$ thỏa $10=\max\{1+0{,}9\cdot10;\ 0\}$; tăng số lần cập nhật tại $\mathrm s_0$ không đổi giới hạn này.
:::

::: exercise Bài tập 04.6 (Chứng nhận nghiệm tối ưu)
Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$; và hai bảng $U=(10,30)$, giá trị chính xác của $\pi_1=(\mathrm a,\mathrm b)$, và $V=(27,30)$.

(a) Tính $T_*U$, $T_*V$, $\Delta_*(U)$, $\Delta_*(V)$ và hai chính sách tham lam.

(b) Xác định bảng nào là $v_*$ và nêu kết quả của chương được dùng làm căn cứ.

(c) So chặn sai số của $U$ theo Hệ quả 04.27 với sai số thật của $U$.

(d) Giả sử chỉ có một bộ mô phỏng nhận $(s,a)$ và trả một chuyển $(s',r)$. Xác định phép tính ở (a) không thực hiện được trực tiếp.
:::

::: hint
Mỗi thành phần của $T_*U$ là cực đại của hai giá trị nhìn trước; dùng bảng $U$ cho mọi giá trị tiếp nối.
:::

::: solution
**(a)** Với $U$: tại $\mathrm s_0$, $\max\{1+0{,}9\cdot10;\ 0+0{,}9\cdot30\}=\max\{10;\,27\}=27$; tại $\mathrm s_1$, $\max\{2+9;\ 3+27\}=\max\{11;\,30\}=30$. Vậy $T_*U=(27,30)$, $\Delta_*(U)=17$, chính sách tham lam $(\mathrm b,\mathrm b)$. Với $V$: các giá trị nhìn trước là $25{,}3$; $27$ tại $\mathrm s_0$ và $26{,}3$; $30$ tại $\mathrm s_1$, nên $T_*V=V$, $\Delta_*(V)=0$, chính sách tham lam $(\mathrm b,\mathrm b)$.

**(b)** $V=v_*$, vì $V$ là điểm bất động của $T_*$ và theo Định lý 04.25(a) điểm bất động đó duy nhất và bằng $v_*$; các giả thiết MDP hữu hạn, phần thưởng bị chặn và $\gamma=0{,}9<1$ đều thỏa. Bảng $U$ là giá trị chính xác của một chính sách nhưng không thỏa phương trình Bellman tối ưu.

**(c)** Chặn là $17/(1-0{,}9)=170$, còn sai số thật là $\lVert U-v_*\rVert_\infty=\max\{17;\,0\}=17$. Chặn đúng nhưng lớn gấp mười lần sai số thật.

**(d)** Phép tính kỳ vọng đầy đủ $\sum_{s',r}p(s',r\mid s,a)[r+\gamma U(s')]$ cần biết $p$. Bộ mô phỏng chỉ cho từng mẫu; muốn dùng nó phải ước lượng mô hình như Ví dụ 04.17 hoặc dùng các phương pháp lấy mẫu của Bài 05.

**Kiểm tra lại.** Theo Định lý 04.13, chính sách tham lam theo $v_{\pi_1}=U$ không kém $\pi_1$; ở đây nó là $(\mathrm b,\mathrm b)$ với giá trị $(27,30)\ge(10,30)$.
:::

Như vậy, chi phí một lượt quét là $O(n^2m)$ với mô hình đặc (Nhận xét 04.30); cập nhật tại chỗ và lặp giá trị bất đồng bộ (Thuật toán 04.31) có thể giảm số phép tính mà vẫn hội tụ khi mọi trạng thái được cập nhật vô hạn lần (Định lý 04.32), và cả ba thuật toán là ba cách xen kẽ trong khuôn lặp chính sách tổng quát (Định nghĩa 04.34). Tuy nhiên, mọi bảo đảm thuộc về MDP hữu hạn với mô hình đã biết; mô hình bảng của một môi trường liên tục có thể mất tính Markov (Nhận xét 04.35), và hai tình huống ở mục sau đo khoảng cách này trên CartPole.

## Tình huống áp dụng và ứng dụng

Hai tình huống dưới đây dùng công cụ của chương trên bài thực hành CartPole. Tình huống 04.1 đi trọn chuỗi lập kế hoạch và đối chiếu với kết quả của bài thực hành; Tình huống 04.2 xét trường hợp giả thiết không thỏa. Trường hợp bỏ chiết khấu, $\gamma=1$, đã được xét ngay sau Ví dụ 04.5.

::: application Tình huống 04.1 (Lập kế hoạch trên CartPole rời rạc hóa)
**Bài toán và môi trường.** `CartPole-v1` của Gymnasium như mô tả ở Mục 5.4, cắt lượt ở $500$ bước. Cần một chính sách giữ cột lâu hơn chính sách ngẫu nhiên đều và chính sách theo dấu góc.

**Mô hình hóa.** Rời rạc hóa thành $324$ ô theo Ví dụ 04.17, ước lượng $\hat p(s'\mid s,a)$ bằng $M=200$ mẫu mỗi cặp ô–hành động, $\hat r(s,a)=1$, và chọn $\gamma=0{,}99$. Đối tượng của chương là MDP hữu hạn $(\mathcal S^+,\{0,1\},\hat p,\hat r)$ với $\lvert\mathcal S^+\rvert=325$, không chứa giới hạn $500$ bước.

**Kiểm tra giả thiết.** Trên MDP ước lượng, tập trạng thái và hành động hữu hạn, phần thưởng bị chặn bởi $1$, $\gamma<1$, mô hình được biết vì chính nó được lập ra, và tính Markov thỏa theo cách xây dựng. Các giả thiết của Hệ quả 04.6, Định lý 04.13, Mệnh đề 04.18 và Định lý 04.25 thỏa cho MDP này.

**Áp dụng.** Thuật toán 04.17 và Thuật toán 04.28 cho cùng một chính sách trên MDP ước lượng, với các số liệu nêu ở đoạn "Trong thực hành" của Mục 3 và Mục 4; theo Định lý 04.25(d), chính sách này tối ưu cho MDP ước lượng. Một lần chạy đã nhúng trong notebook đánh giá nó trong môi trường liên tục bằng số bước giữ cột của mỗi lượt; vì mỗi bước có phần thưởng $+1$, số bước này là lợi tức không chiết khấu của lượt. Trên cùng $100$ lượt với cùng tập hạt giống, số bước trung bình là $343{,}4$ (sai số chuẩn $9{,}2$), so với $22{,}5$ của chính sách ngẫu nhiên và $43{,}6$ của chính sách theo dấu góc; hiệu theo cặp so với chính sách theo dấu góc là $299{,}8\pm18{,}0$ với độ rộng $1{,}96$ sai số chuẩn.

**Diễn giải.** Chính sách này giữ cột lâu hơn khoảng tám lần chính sách theo dấu góc. Trên lát cắt $36$ ô ứng với $x$ và $\dot x$ ở khoảng giữa, chính sách này khác chính sách theo dấu góc tại $14$ ô; theo hình chính sách của notebook, hành động ở đó đổi theo vận tốc góc $\dot\phi$, biến mà chính sách theo dấu góc bỏ qua.

**Giới hạn.** Định lý 04.25 chỉ bảo đảm tối ưu cho MDP ước lượng; Tình huống 04.2 đo khoảng cách tới CartPole.

**Dẫn ngược lý thuyết.** Mô hình hóa dùng Ví dụ 04.17; bước đánh giá dùng Hệ quả 04.6(c); bước cải thiện dùng Định lý 04.13 và Thuật toán 04.14; dừng và tối ưu dùng Mệnh đề 04.18, Định lý 04.20, 04.25; lặp giá trị dùng Hệ quả 04.27 và Thuật toán 04.28. Giả thiết hữu hạn được bảo đảm ở bước rời rạc hóa, giả thiết mô hình đã biết ở bước ước lượng $\hat p$.
:::

::: application Tình huống 04.2 (Chứng nhận trên mô hình gộp không chuyển sang môi trường liên tục)
**Bài toán.** Với chính sách của Tình huống 04.1, so giá trị mô hình dự đoán với lợi tức chiết khấu đo được trong CartPole, và kiểm kết luận khi thay mẫu ước lượng mô hình.

**Giả thiết bị vi phạm.** Quá trình thật trên các ô không thỏa các giả thiết đã kiểm trên MDP ước lượng.

- Tính Markov: phân phối của ô kế tiếp phụ thuộc vị trí bên trong ô hiện tại (Ví dụ 04.17), và lịch sử các ô đã đi qua mang thông tin về vị trí đó, nên $\Pr(\text{ô kế tiếp}\mid\text{ô hiện tại},a)$ có thể khác $\Pr(\text{ô kế tiếp}\mid\text{lịch sử},a)$; Định lý 04.25 cần tính Markov ở Bước 3.
- Mô hình đã biết: $\hat p$ ước lượng từ mẫu đều trong ô, còn trạng thái thật trong ô không phân bố đều.
- Mục tiêu: môi trường cắt lượt ở $500$ bước; mô hình không có giới hạn này.

**Hậu quả quan sát được.** Một lần chạy đã nhúng trong notebook cho các số sau.

- Giá trị dự đoán $v_*$ tại ô của trạng thái đầu, trung bình trên $100$ lượt, là $84{,}47$; lợi tức chiết khấu đo được, $G_0=(1-0{,}99^T)/(1-0{,}99)$ với $T$ là độ dài lượt, trung bình là $95{,}38$ (sai số chuẩn $0{,}37$). Chênh lệch $10{,}90$ lớn hơn nhiều chặn sai số lặp $0{,}01$ và mức giảm tối đa do cắt ở $500$ bước, $0{,}99^{500}/(1-0{,}99)\approx0{,}657$.
- Lặp lại toàn bộ chuỗi với năm hạt giống khác nhau khi ước lượng mô hình cho số bước trung bình $343{,}4$; $221{,}3$; $219{,}2$; $500{,}0$; $220{,}2$, độ lệch chuẩn giữa các hạt giống là $123{,}5$, lớn hơn nhiều sai số chuẩn của từng dòng, không vượt $9{,}2$.
- Với chính sách của Tình huống 04.1, $98$ trong $100$ lượt kết thúc vì $\lvert x\rvert>2{,}4$, không vì góc cột.

**Diễn giải.** Phần dư nhỏ chỉ chứng nhận sai số lặp trên MDP ước lượng (Hệ quả 04.27); sai số do gộp trạng thái và ước lượng mô hình nằm ngoài mọi chặn của chương, và ở đây lớn hơn sai số lặp ba bậc độ lớn. Muốn cải thiện trong môi trường thật, cần đổi cách rời rạc hóa hoặc cách ước lượng mô hình; giảm $\theta$ không có tác dụng.

**Dẫn ngược lý thuyết.** Giả thiết Markov của Định lý 04.25 (Bước 3) và giả thiết mô hình đã biết của mọi thuật toán; Nhận xét 04.35.
:::

**Ứng dụng trong các bài sau.**

- Bài 05 (dự đoán phi mô hình): cập nhật kỳ vọng của $T_\pi$ (Định nghĩa 04.1) được thay bằng một chuyển lấy mẫu, nên mục tiêu bootstrap $r+\gamma V(s')$ dùng một $s'$ quan sát được.
- Bài 06 (điều khiển phi mô hình): khuôn lặp chính sách tổng quát (Định nghĩa 04.34) dùng bước đánh giá ước lượng từ mẫu và cải thiện theo giá trị hành động, vì không có $p$ để tính (2.1).
- Bài 07 (xấp xỉ hàm): bảng $V$ được thay bằng một hàm có tham số khi $n$ quá lớn (Nhận xét 04.35); tính co của Mệnh đề 04.4 và 04.24 không còn tự động đúng sau phép xấp xỉ.
- Bài 08 (Deep Q-learning): mục tiêu $r+\gamma\max_{a'}Q(s',a')$ là phiên bản lấy mẫu của (4.1) cho giá trị hành động, tính bằng mạng nơ-ron.

## Tóm tắt chương

Chúng ta xuất phát từ bài toán lập kế hoạch: với mô hình $p$ đã biết, tìm chính sách tốt nhất đồng thời tại mọi trạng thái. Toán tử $T_\pi$ là ánh xạ co (Mệnh đề 04.4), nên $v_\pi$ là điểm bất động duy nhất của nó, đạt được bằng lượt quét và dừng theo phần dư với chặn sai số (Định lý 04.5, Hệ quả 04.6, 04.8). Chính sách tham lam theo $v_\pi$ không kém $\pi$ (Định lý 04.13), và xen kẽ hai bước với quy tắc phá hòa cho lặp chính sách, dừng hữu hạn tại một chính sách thỏa phương trình Bellman tối ưu (Mệnh đề 04.18, Định lý 04.20); trên mô hình hai trạng thái đó là $(\mathrm b,\mathrm b)$ với $v_*=(27,30)$. Toán tử $T_*$ cũng co; điểm bất động của nó là $v_*$, và chính sách tham lam theo $v_*$ tối ưu trên mọi chính sách, kể cả chính sách nhớ lịch sử (Mệnh đề 04.24, Định lý 04.25). Lặp giá trị hội tụ với tốc độ $\gamma^k$, còn lịch bất đồng bộ hội tụ khi mọi trạng thái được cập nhật vô hạn lần (Hệ quả 04.26, 04.27, Định lý 04.32). Các bảo đảm này thuộc về MDP hữu hạn với $\gamma<1$ và mô hình đã biết; trên CartPole rời rạc hóa, chúng chỉ chứng nhận nghiệm của mô hình ước lượng (Tình huống 04.2), và Bài 05 thay kỳ vọng theo $p$ bằng mẫu.

**Định nghĩa và kết quả theo mục.**

- Mục 1: toán tử $T_\pi$, lượt quét đồng bộ (Định nghĩa 04.1); tính đơn điệu (Bổ đề 04.2); chuẩn vô cùng, ánh xạ co (Định nghĩa 04.3); $T_\pi$ co (Mệnh đề 04.4); điểm bất động (Định lý 04.5); nghiệm đánh giá chính sách (Hệ quả 04.6); phần dư (Định nghĩa 04.7); chặn theo phần dư (Hệ quả 04.8); đánh giá chính sách đồng bộ (Thuật toán 04.9); giới hạn của thuật toán (Nhận xét 04.10).
- Mục 2: giá trị nhìn trước (Định nghĩa 04.11); chính sách tham lam, quy tắc phá hòa (Định nghĩa 04.12); cải thiện chính sách (Định lý 04.13, Thuật toán 04.14); bảng cũ không là giá trị của chính sách mới (Nhận xét 04.15).
- Mục 3: chính sách ổn định (Định nghĩa 04.16); lặp chính sách (Thuật toán 04.17); dừng hữu hạn (Mệnh đề 04.18); giá trị và chính sách tối ưu (Định nghĩa 04.19); chính sách ổn định thỏa Bellman tối ưu (Định lý 04.20); hai cách đọc sai (Nhận xét 04.21).
- Mục 4: toán tử $T_*$, phần dư tối ưu (Định nghĩa 04.22); cực đại không tăng chênh lệch (Bổ đề 04.23); $T_*$ co (Mệnh đề 04.24); tồn tại chính sách tối ưu Markov dừng, xác định (Định lý 04.25); hội tụ hình học (Hệ quả 04.26); chặn theo phần dư tối ưu (Hệ quả 04.27); lặp giá trị (Thuật toán 04.28); chính sách trích từ bảng (Nhận xét 04.29).
- Mục 5: chi phí một lượt quét (Nhận xét 04.30); lặp giá trị bất đồng bộ (Thuật toán 04.31, Định lý 04.32); lịch cập nhật và điều kiện "vô hạn lần" (Nhận xét 04.33); lặp chính sách tổng quát (Định nghĩa 04.34); giới hạn của chứng nhận trên mô hình gộp (Nhận xét 04.35).
- Ví dụ 04.1–04.18; Bài tập 04.1–04.9 (tệp bài tập thêm 04.10–04.17); Tình huống 04.1–04.2.

**Công thức cần nhớ.** Hai toán tử Bellman và giá trị nhìn trước:

$$
\begin{aligned}
Q_V(s,a)&=\sum_{s',r}p(s',r\mid s,a)\bigl[r+\gamma V(s')\bigr],\\
(T_\pi V)(s)&=\sum_a\pi(a\mid s)\,Q_V(s,a),\\
(T_*V)(s)&=\max_aQ_V(s,a).
\end{aligned}
$$

Điểm bất động và hội tụ:

$$
v_\pi=T_\pi v_\pi,\qquad v_*=T_*v_*,\qquad\lVert V_k-v_*\rVert_\infty\le\gamma^k\lVert V_0-v_*\rVert_\infty .
$$

Chặn sai số theo phần dư và ngưỡng dừng:

$$
\lVert V-v_*\rVert_\infty\le\frac{\Delta_*(V)}{1-\gamma},\qquad\theta=(1-\gamma)\kappa .
$$

Chính sách tham lam: $\pi_V(s)\in\arg\max_aQ_V(s,a)$.

**Giả thiết hay bị bỏ quên.**

- Định lý cải thiện và tiêu chuẩn chính sách ổn định cần giá trị chính xác $v_\pi$, không phải một bảng gần đúng (Bài tập 04.3).
- Lặp chính sách cần quy tắc phá hòa để dừng; không có nó, thuật toán có thể đổi qua lại giữa các chính sách cùng giá trị.
- Lịch bất đồng bộ cần mọi trạng thái được cập nhật vô hạn lần (Bài tập 04.5).
- Mọi chặn sai số cần $\gamma<1$ (đoạn sau Ví dụ 04.5) và thuộc về mô hình đã cho; chúng không chặn sai số do mô hình sai hay do gộp trạng thái (Tình huống 04.2).
- Phần dư nhỏ chặn sai số của bảng, chưa chặn tổn thất của chính sách trích ra; hết ngân sách không chứng nhận hội tụ.

## Bài tập củng cố

Các bài tập trong các mục, Bài tập 04.1–04.6, mỗi bài kiểm một mục tiêu học tập; ba bài dưới đây dựa trên Bài tập tuần 3 (2025–2026) và bổ sung mỗi mức một bài. [Tệp bài tập của Bài 04](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-giai-mdp-bang-quy-hoach-dong.html) dùng chung bộ đếm, chép lại Bài tập 04.1–04.6, không lặp đề của ba bài dưới đây, và thêm tám bài: dạng ma trận và chuỗi Neumann (04.10), tính đơn điệu của $T_*$ (04.11), lặp giá trị và lặp chính sách trên MDP ba trạng thái (04.12), dãy năm ô trơn trượt (04.13), số lượt quét của lặp giá trị theo $\gamma$ trên CartPole rời rạc hóa (04.14) và lặp chính sách cải biên (04.15), cả hai có phần lập trình trên notebook, lợi tức của chính sách ban đầu (04.16), cải thiện từ chính sách ngẫu nhiên đều (04.17).

### Mức nhận biết

::: exercise Bài tập 04.7 (Giá trị trạng thái, giá trị hành động và hai phương trình Bellman)
Theo Bài tập tuần 3 (2025–2026), bài 1–2. Cho mô hình hai trạng thái: $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $1$; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $0$; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng $2$; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng $3$; mọi chuyển xác định; $\gamma=0{,}9$. Chính sách $\pi_1=(\mathrm a,\mathrm b)$.

(a) Viết và giải hệ phương trình Bellman kỳ vọng của $\pi_1$ để tìm $v_{\pi_1}$.

(b) Tính $q_{\pi_1}(\mathrm s_0,\mathrm b)$, và mô tả bằng lời quỹ đạo mà mỗi số $v_{\pi_1}(\mathrm s_0)$, $q_{\pi_1}(\mathrm s_0,\mathrm b)$ đo.

(c) Viết phương trình Bellman tối ưu tại $\mathrm s_0$. Chỉ ra hệ nào trong hai hệ ở (a) và (c) tuyến tính theo các ẩn, và cho nghiệm của hệ tối ưu tại $\mathrm s_0$.
:::

::: hint
Theo $\pi_1$, $\mathrm s_0$ quay về chính nó và $\mathrm s_1$ quay về chính nó, nên hai phương trình ở (a) tách rời. $q_{\pi_1}(\mathrm s_0,\mathrm b)$ ấn định hành động đầu là $\mathrm b$ dù $\pi_1$ chọn $\mathrm a$ tại $\mathrm s_0$.
:::

::: solution
**(a)** $v(\mathrm s_0)=1+0{,}9\,v(\mathrm s_0)$ và $v(\mathrm s_1)=3+0{,}9\,v(\mathrm s_1)$. Từ $0{,}1\,v(\mathrm s_0)=1$ và $0{,}1\,v(\mathrm s_1)=3$, ta được $v_{\pi_1}=(10,30)$.

**(b)** $q_{\pi_1}(\mathrm s_0,\mathrm b)=0+0{,}9\cdot30=27$. Số $v_{\pi_1}(\mathrm s_0)=10$ đo lợi tức khi xuất phát từ $\mathrm s_0$ và theo $\pi_1$: tác tử chọn $\mathrm a$ mãi mãi tại $\mathrm s_0$, nhận $1$ mỗi bước. Số $27$ đo lợi tức khi chọn $\mathrm b$ một lần tại $\mathrm s_0$, sang $\mathrm s_1$, rồi theo $\pi_1$, tức chọn $\mathrm b$ mãi tại $\mathrm s_1$.

**(c)** $v(\mathrm s_0)=\max\{1+0{,}9\,v(\mathrm s_0);\ 0+0{,}9\,v(\mathrm s_1)\}$, cùng phương trình tương tự tại $\mathrm s_1$. Hệ ở (a) tuyến tính; hệ tối ưu không tuyến tính vì có phép cực đại. Theo Định lý 04.25, nghiệm duy nhất của hệ tối ưu là $v_*=(27,30)$, nên tại $\mathrm s_0$ nghiệm là $27$.

**Kiểm tra lại.** Thế $(27,30)$ vào hệ tối ưu: $\max\{1+24{,}3;\ 27\}=27$ và $\max\{2+24{,}3;\ 3+27\}=30$.
:::

### Mức tính toán hoặc chứng minh

::: exercise Bài tập 04.8 (Giá trị trạng thái qua giá trị hành động, và đặc trưng của chính sách tối ưu)
Theo Bài tập tuần 3 (2025–2026), bài 5 và bài 3. Xét MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$.

(a) Chứng minh $v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a)$ cho mọi chính sách Markov dừng $\pi$, từ định nghĩa $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ và $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$.

(b) Dùng (a) và Định lý 04.25, chứng minh: một chính sách Markov dừng $\pi$ là tối ưu khi và chỉ khi tại mọi $s$, $\pi(a\mid s)>0$ chỉ với các $a\in\arg\max_{a'}q_*(s,a')$.
:::

::: hint
Ở (a), dùng luật kỳ vọng toàn phần theo $A_t$ với phân phối có điều kiện $\pi(\cdot\mid s)$. Ở (b), chiều "nếu" chứng minh $v_*$ là điểm bất động của $T_\pi$; chiều "chỉ nếu" dùng $q_\pi=q_*$ khi $v_\pi=v_*$.
:::

::: solution
**(a)** Với $S_t=s$, hành động $A_t$ có phân phối $\pi(\cdot\mid s)$. Theo luật kỳ vọng toàn phần,

$$
\begin{aligned}
v_\pi(s)&=\mathbb E_\pi[G_t\mid S_t=s]\\
&=\sum_a\Pr(A_t=a\mid S_t=s)\,\mathbb E_\pi[G_t\mid S_t=s,A_t=a] &&\text{(kỳ vọng toàn phần)}\\
&=\sum_a\pi(a\mid s)\,q_\pi(s,a) &&\text{(định nghĩa } \pi \text{ và } q_\pi).
\end{aligned}
$$

Số hạng có $\pi(a\mid s)=0$ đóng góp $0$, nên đẳng thức đúng cả khi $q_\pi(s,a)$ được định nghĩa bằng cách ấn định hành động đầu.

**(b), chiều "nếu".** Giả sử $\pi$ chỉ đặt xác suất dương lên tập $\arg\max_{a'}q_*(s,a')$. Khi đó

$$
\begin{aligned}
(T_\pi v_*)(s)
&=\sum_a\pi(a\mid s)\,q_*(s,a) &&\text{(Định nghĩa 04.1, Định nghĩa 04.19)}\\
&=\max_aq_*(s,a) &&\text{(trọng số dương chỉ ở cực đại)}\\
&=v_*(s) &&\text{(Định lý 04.25(c))}.
\end{aligned}
$$

Vậy $v_*$ là điểm bất động của $T_\pi$, và theo Hệ quả 04.6(a), $v_\pi=v_*$: $\pi$ tối ưu.

**(b), chiều "chỉ nếu".** Giả sử $v_\pi=v_*$. Theo phương trình Bellman cho giá trị hành động (Mệnh đề 03.22, ghi chú Bài 03, Mục 4) và Định nghĩa 04.19, $q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_*(s')]=q_*(s,a)$. Theo (a), $v_*(s)=\sum_a\pi(a\mid s)q_*(s,a)$. Nếu $\pi(a^\circ\mid s)>0$ với $q_*(s,a^\circ)<\max_aq_*(s,a)$, trung bình có trọng số này nhỏ hơn nghiêm ngặt $\max_aq_*(s,a)=v_*(s)$, mâu thuẫn.

**Kiểm tra lại.** Trên mô hình hai trạng thái, $q_*(\mathrm s_0,\cdot)=(25{,}3;\,27)$ và $q_*(\mathrm s_1,\cdot)=(26{,}3;\,30)$, nên chính sách tối ưu Markov dừng duy nhất là $(\mathrm b,\mathrm b)$; chính sách ngẫu nhiên đều đặt trọng số $\tfrac12$ lên $\mathrm a$, nên theo (b) nó không tối ưu.
:::

### Mức vận dụng

::: exercise Bài tập 04.9 (Lịch theo quỹ đạo và trạng thái liên tục)
Theo Bài tập tuần 3 (2025–2026), bài 4 và bài 8. Một nhóm giải CartPole rời rạc hóa $324$ ô (Ví dụ 04.17) bằng lặp giá trị bất đồng bộ, cập nhật ở mỗi bước ô hiện tại của tác tử khi nó chạy chính sách ngẫu nhiên đều; chính sách này chỉ đi qua $64$ trong $324$ ô.

(a) Xác định lịch này có làm thay đổi điểm bất động mà thuật toán nhắm tới hay không, và có làm mất bảo đảm hội tụ hay không.

(b) Đề xuất một thay đổi của lịch để lấy lại bảo đảm của Định lý 04.32.

(c) Nếu giữ trạng thái liên tục, chỉ ra các chỗ trong chương dùng tính hữu hạn và nêu điều phải thay đổi.
:::

::: hint
Điểm bất động do toán tử quyết định, còn hội tụ phụ thuộc lịch. Ở (c), tìm chỗ chứng minh đếm số chính sách, chỗ lấy tổng theo $s'$, và chỗ cần biểu diễn bảng giá trị bằng một vectơ hữu hạn chiều.
:::

::: solution
**(a)** Mỗi cập nhật vẫn là $V(s)\leftarrow(T_*V)(s)$ với cùng mô hình, nên điểm bất động vẫn là $v_*$ của MDP ước lượng (Định lý 04.25). Nhưng $260$ ô không bao giờ được cập nhật, nên giả thiết "vô hạn lần" của Định lý 04.32 bị vi phạm, và các ô đọc chúng có thể hội tụ về giá trị sai như Bài tập 04.5.

**(b)** Xen kẽ cập nhật theo quỹ đạo với các lượt quét toàn bộ định kỳ; mọi lịch mà mỗi ô xuất hiện vô hạn lần đều được.

**(c)** Ba chỗ dùng tính hữu hạn.

- Mệnh đề 04.18, Bước 3, đếm $\prod_s\lvert\mathcal A(s)\rvert$ chính sách; với trạng thái liên tục, số chính sách xác định là vô hạn, nên lập luận "không lặp lại thì dừng" không còn cho dừng hữu hạn và phải thay bằng một lập luận hội tụ.
- Mọi tổng theo $s'$ trong (1.1), (2.1) và (4.1) thành tích phân theo phân phối của trạng thái kế tiếp, nên các đẳng thức của chương phải viết lại với tích phân.
- Định lý 04.5 được chứng minh trên $\mathbb R^n$; với trạng thái liên tục, $V$ là một hàm trên tập vô hạn, không lưu được thành bảng, nên trong tính toán phải dùng xấp xỉ hàm như ở Bài 07, và khi đó tính co của toán tử trên lớp hàm xấp xỉ không còn tự động đúng.

Định lý 04.25, Bước 2 vẫn đúng vì tập hành động hữu hạn. Định lý điểm bất động trên không gian hàm bị chặn và yêu cầu chính sách tham lam là hàm đo được của trạng thái nằm ngoài phạm vi học phần.

**Kiểm tra lại.** $324-64=260$ ô không được thăm.
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

<!-- note-topic-id: lec-04-part-13 -->
### Đọc thêm

- **Lặp chính sách cải biên.** Thay đánh giá chính xác trong Thuật toán 04.17 bằng $\ell$ lượt quét của Thuật toán 04.9 xuất phát từ bảng của vòng trước. Với $\ell=1$, thuật toán trùng với lặp giá trị từ vòng thứ hai; khi $\ell\to\infty$, nó thành lặp chính sách. Mệnh đề 04.18 không còn áp dụng vì giả thiết đánh giá chính xác bị bỏ; Puterman (1994, §6.5) trình bày điều kiện hội tụ. Bài thực hành CartPole, nhiệm vụ 7, đề nghị thử $\ell\in\{1,5,20\}$ và viết $m$ cho $\ell$. Bài tập 04.15 của [tệp bài tập](material-viewer.html?doc=materials/lec-04/exercises.md&deck=lecture-04-giai-mdp-bang-quy-hoach-dong.html) tính tay ba vòng với $\ell=1$ trên mô hình hai trạng thái, đếm bằng chương trình số vòng và số phép áp dụng toán tử với $\ell\in\{1,5,20\}$, rồi chạy nhiệm vụ 7 trên CartPole rời rạc hóa. Sáu bài còn lại của tệp, Bài tập 04.10–04.14, 04.16 và 04.17, được liệt kê ở đầu mục Bài tập củng cố.
- **Tổn thất của chính sách tham lam.** Singh và Yee (1994) chứng minh rằng nếu $\lVert V-v_*\rVert_\infty\le\epsilon_0$ thì chính sách tham lam theo $V$ thỏa $\lVert v_{\pi_V}-v_*\rVert_\infty\le2\gamma\epsilon_0/(1-\gamma)$. Bài thực hành CartPole đặt chặn này cạnh tổn thất đo được.
- **Trường hợp không chiết khấu.** Sutton và Barto (2018, Ví dụ 4.1, tr. 76–77) xét lưới $4\times4$ với $\gamma=1$, trong đó điều kiện mọi chính sách đều tới đích thay cho $\gamma<1$; đoạn sau Ví dụ 04.5 cho thấy vì sao cần một điều kiện như vậy.

### Tài liệu tham khảo

- Tạ Việt Cường, Bài giảng gốc Bài 04: Giải MDP (2025–2026): trang 4–6, 12, 17–18 cho Mục 1.1–1.2 và mô hình hai trạng thái; trang 10, 14–15, 31–32 cho Mục 1.2–1.4; trang 19–21 cho Mục 2; trang 7–9, 13, 20, 33–34 cho Mục 3; trang 23–28, 31–34 cho Mục 4; trang 15, 29, 35–37 cho Mục 5; trang 38 cho Tóm tắt chương.
- Tạ Việt Cường, Bài tập tuần 3 (2025–2026), "Giải bài toán MDP": bài 1–5 và 8 cho Bài tập 04.7–04.9; bài 6–7 cho Hệ quả 04.6(c) và Bổ đề 04.2. Bài tập tuần 4 (2025–2026), "Đánh giá chính sách": bài 1 cho mô hình hai trạng thái.
- Sutton, R. S., và Barto, A. G. (2018), *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press, chương 4: §4.1, tr. 74–76 (Mục 1); §4.2, tr. 76–80, công thức (4.6)–(4.9) (Mục 2); §4.3, tr. 80–82, Bài tập 4.4 (Mục 3); §4.4, tr. 82–84, công thức (4.10) (Mục 4); §4.5–4.7, tr. 85–88 (Mục 5); §4.8, tr. 88–89 (Tóm tắt chương).
- Puterman, M. L. (1994), *Markov Decision Processes: Discrete Stochastic Dynamic Programming*, Wiley: §6.1 (đánh giá chính sách, dạng ma trận), §6.2 (phương trình tối ưu, tồn tại chính sách tối ưu Markov dừng, xác định; Định lý 04.25), §6.3 (lặp giá trị), §6.4 (lặp chính sách), §6.5 (lặp chính sách cải biên).
- Bertsekas, D. P., và Tsitsiklis, J. N. (1989), *Parallel and Distributed Computation: Numerical Methods*, Prentice Hall: các thuật toán bất đồng bộ, được dẫn trong phần ghi chú lịch sử chương 4 của Sutton và Barto (2018, tr. 90); dùng cho Định lý 04.32.
- Singh, S. P., và Yee, R. C. (1994), An upper bound on the loss from approximate optimal-value functions, *Machine Learning* 16, 227–233.
- Giáo trình *Học máy thống kê* của tác giả, chương Học tăng cường, mục "Thuật toán tối ưu quy hoạch động" (tiểu mục lặp giá trị, lặp chính sách): giọng kể, cách đọc $V_k$, thuật ngữ "nhìn trước một bước".
- Bài thực hành CartPole của Bài 04 (`thuc-hanh-cartpole-quy-hoach-dong.ipynb`): số liệu "Trong thực hành", Ví dụ 04.15, 04.17, 04.18 và hai tình huống, từ một lần chạy đã nhúng (gymnasium 1.3.0).
