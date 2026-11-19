# Bài 11 — Lập kế hoạch dựa trên mô hình: kế hoạch bài tập

> **Mục đích.** Kế hoạch cho mục "Bài tập củng cố" của ghi chú mới (Bài tập 11.1–11.11) và tệp `materials/lec-11/exercises.md` (Bài tập 11.12–11.19), cùng các trang bài tập của deck. Tệp planning nội bộ.
>
> **Ngày:** 2026-11-19. **Trạng thái:** kế hoạch, chưa duyệt (chờ quyết các điểm QB ở mục 9).
>
> **Đầu vào.** `NGUYEN-TAC-HOC-PHAN.md` (BT-RL-1…9, GC-RL-11), `NGUYEN-TAC-BAI-TAP.md` (BT1–BT13), `NGUYEN-TAC-TRANG-CHIEU.md` (NT15, NT24, NT-RL-9, NT-RL-10), `NGUYEN-TAC-VAN-PHONG.md`; mẫu `materials/_templates/exercises.md`; mẫu thực tế `materials/lec-10/exercises.md`, `materials/lec-04/exercises.md` (Bài tập 04.21 [Lập trình]); Sutton và Barto (2018), bản trích `/data/tqlong/qa/sources/sutton-barto-rl2020/extracted.md`, đã đối chiếu đề Bài tập 2.8, 8.1–8.8, 17.1 và số trang (trang in = trang PDF − 22); `ke-hoach-ghi-chu.md` (số hiệu khối, ví dụ, số liệu ở mục 7).
>
> **Quy định chính.** `exercises.md` chỉ lấy bài của giáo trình chuẩn (BT-RL-1); bài của ghi chú do học phần soạn, nằm trong "Bài tập củng cố" (BT-RL-5); hai tệp không lặp đề (BT1); một bộ đếm `Bài tập 11.k` chung, `exercises.md` tiếp số sau bài cuối của ghi chú (BT4); mỗi mục tiêu học tập có ít nhất một bài (BT9).

## 0. Tóm tắt quyết định

- **Ghi chú:** mười một bài 11.1–11.11, ba mức (BT-RL-5): nhận biết 11.1–11.3; tính toán hoặc chứng minh 11.4–11.8; vận dụng 11.9–11.11. Không bài tập cuối mục (đề xuất QG4 của `ke-hoach-ghi-chu.md`).
- **`exercises.md`:** tám bài của Sutton và Barto (2018), 11.12–11.19, ba mức (BT-RL-2): nhận biết 11.12–11.13 (SB Bài tập 8.2, 8.3); tính toán hoặc chứng minh 11.14–11.15 (SB 8.6, 17.1); vận dụng 11.16–11.19 (SB 8.1, 8.5, 2.8, 8.4 [Lập trình]). Loại SB 8.7 và 8.8 (thuộc phần đọc thêm, QB1).
- **Khoảng trống:** mục tiêu 5 (tối ưu kế hoạch bằng đạo hàm, điều khiển dự báo) và phần MCTS ngoài UCB không có bài trong SB; kiểm Bertsekas (2019) và Puterman (1994) trước (QB3), nếu không có thì dựa vào bài của ghi chú theo BT9, ghi lý do trong `review-log.md`.
- **Trên deck** (NT24): sáu bài có "Lời giải:" trên mặt trang, đều là bài của ghi chú: 11.2 (mạch 2, cụm bất định), 11.4 (mạch 2, cụm Dyna), 11.5 (mạch 3), 11.6 (mạch 4), 11.7 (mạch 5), 11.10 (bài tập tổng hợp của mạch "Tổng kết", NT15, NT-RL-9).

## 1. Ứng viên từ Sutton và Barto (2018), đã đối chiếu đề trên bản trích

Cột "Phát biểu lại" ghi dữ kiện mà đề phải nêu lại để tự chứa (BT6). Cột "Chọn" ghi quyết định đề xuất.

| Bài SB | Mục, trang in | Tóm tắt đề (tiếng Việt) | Mức | Mục ghi chú, mục tiêu | Phát biểu lại (BT6) | Chọn |
|---|---|---|---|---|---|---|
| 2.8 "UCB Spikes" | §2.7, tr. 36 | Ở Hình 2.4, UCB có một đỉnh rõ ở bước thứ 11. Giải thích vì sao phần thưởng tăng ở bước 11 và giảm ở các bước sau; gợi ý: với $c=1$ đỉnh kém rõ hơn. | vận dụng | §3.2; mục tiêu 4 | bộ thử 10 tay của §2.3, tr. 28–29 ($q_*(a)\sim\mathcal N(0,1)$, phần thưởng $\sim\mathcal N(q_*(a),1)$, trung bình trên 2 000 bài toán); Hình 2.4 bằng lời (UCB $c=2$ so với $\varepsilon$-tham lam $\varepsilon=0{,}1$, 1 000 bước); quy tắc (2.10) với $N_t(a)=0$ coi là cực đại | 11.18 |
| 8.1 | §8.2, tr. 166 | Phương pháp không lập kế hoạch trông rất kém ở Hình 8.3 vì là phương pháp một bước; một phương pháp bootstrap nhiều bước sẽ tốt hơn. Một phương pháp bootstrap nhiều bước của Chương 7 có thể làm tốt bằng Dyna không? Giải thích. | vận dụng | §2.4; mục tiêu 2 | mê cung Dyna của Ví dụ 8.1 (47 trạng thái, bốn hành động tất định, phần thưởng $+1$ khi vào đích, $\gamma=0{,}95$, $\alpha=0{,}1$, $\varepsilon=0{,}1$); Hình 8.3 bằng lời (giữa lượt thứ hai: $n=0$ mới học bước cuối; $n=50$ đã có chính sách gần tới ô xuất phát); lợi tức $n$ bước và cập nhật $n$ bước. Ghi chú 05, 06 **không** dạy phương pháp $n$ bước (đã tìm "n bước" trong ghi chú 05–07: không có); lợi tức $n$ bước có ở Định nghĩa 10.11 (dạng lợi thế); đề phải phát biểu lại cập nhật Sarsa $n$ bước (SB (7.4)–(7.5), cần kiểm số công thức) | 11.16 |
| 8.2 | §8.3, tr. 168 | Vì sao tác tử Dyna có thưởng thăm dò, Dyna-Q+, làm tốt hơn cả ở pha thứ nhất lẫn pha thứ hai của thí nghiệm mê cung bị chặn và mê cung có lối tắt? | nhận biết | §2.5; mục tiêu 2 | Ví dụ 8.2, 8.3 và Hình 8.4, 8.5 (tr. 166–167) bằng lời: môi trường đổi sau 1 000 bước (bị chặn) và 3 000 bước (lối tắt); đường lợi tức tích lũy của Dyna-Q+ nằm trên Dyna-Q ở cả hai pha; thưởng $\kappa\sqrt\tau$ và hai thay đổi của chú thích 1, tr. 168 | 11.12 |
| 8.3 | §8.3, tr. 168 | Nhìn kỹ Hình 8.5, khoảng cách giữa Dyna-Q+ và Dyna-Q hẹp lại một chút trong phần đầu thí nghiệm. Lý do? | nhận biết | §2.5; mục tiêu 2 | như 8.2, chỉ Hình 8.5 | 11.13 |
| 8.4 (programming) | §8.3, tr. 168 | Thưởng thăm dò làm đổi giá trị ước lượng. Có cần như vậy không? Giả sử thưởng $\kappa\sqrt\tau$ chỉ dùng khi chọn hành động: luôn chọn hành động cực đại $Q(S_t,a)+\kappa\sqrt{\tau(S_t,a)}$. Làm thí nghiệm trên mê cung lưới để kiểm và minh họa điểm mạnh, điểm yếu của cách này. | vận dụng [Lập trình] | §2.5; mục tiêu 2 | mê cung có lối tắt (Ví dụ 8.3) hoặc mê cung đổi cửa của ghi chú (Ví dụ 11.8); Thuật toán 11.10, Định nghĩa 11.12 | 11.19 (QB4) |
| 8.5 | §8.3, tr. 168 | Sửa Dyna-Q dạng bảng (hộp tr. 164) thế nào để xử lý môi trường ngẫu nhiên? Sửa đổi đó có thể kém thế nào trong môi trường thay đổi như ở mục này? Sửa thế nào để xử lý cả môi trường ngẫu nhiên lẫn thay đổi? | vận dụng | §2.2, §2.4, §2.5; mục tiêu 1, 2 | hộp Dyna-Q (Thuật toán 11.10), giả thiết tất định ở bước (e) | 11.17 |
| 8.6 | §8.5, tr. 174 | Phân tích ở trên giả thiết mọi trạng thái kế đồng khả năng. Nếu phân phối rất lệch (vài trạng thái có xác suất lớn hơn nhiều), lập luận ủng hộ cập nhật mẫu mạnh lên hay yếu đi? Giải thích. | tính toán hoặc chứng minh | §2.6; mục tiêu 3 | thiết lập của Hình 8.7: giá trị kế đúng, sai số ban đầu $1$, trung bình mẫu $\alpha=1/t$, sai số $\sqrt{(b-1)/(bt)}$; Mệnh đề 11.15 | 11.14 |
| 8.7 | §8.6, tr. 176 | Một số đồ thị ở Hình 8.8 có dạng gợn ở phần đầu, nhất là đồ thị trên với $b=1$ và phân phối đều. Vì sao? Dữ liệu nào ủng hộ giả thuyết? | vận dụng | §2.7 (đọc thêm) | thí nghiệm của Hình 8.8 (1 000 và 10 000 trạng thái, xác suất kết thúc $0{,}1$, phần thưởng chuẩn): nhiều dữ kiện phải phát biểu lại | không (QB1) |
| 8.8 (programming) | §8.6, tr. 176 | Lặp lại thí nghiệm của phần dưới Hình 8.8, rồi thử với $b=3$; bàn về ý nghĩa kết quả. | vận dụng [Lập trình] | §2.7 (đọc thêm) | như 8.7 | không (QB1) |
| 17.1 | §17.2, tr. 464 | Mục này trình bày tùy chọn cho trường hợp chiết khấu. Phương trình Bellman tự nhiên cho chính sách phân cấp, tương tự (17.4), trong thiết lập phần thưởng trung bình (§10.3) là gì? Hai phần của mô hình tùy chọn, tương tự (17.2) và (17.3), trong thiết lập đó là gì? | tính toán hoặc chứng minh | §5.2; mục tiêu 6 | thiết lập phần thưởng trung bình: $r(\pi)$ theo (10.6), lợi tức vi phân (10.9), phương trình Bellman vi phân (§10.3, tr. 249–250); học phần **chưa dạy** thiết lập này (đã tìm "phần thưởng trung bình" trong ghi chú 01–10: chỉ là trung bình mẫu) | 11.15 (QB2) |

Đã tìm thêm trong SB: §2.7 chỉ có Bài tập 2.8 về UCB; Chương 16 và §16.6 không có bài tập; Chương 17 chỉ có Bài tập 17.1 (bản trích từ dòng 21 000 trở đi chỉ có 17.1 và hai chỗ nhắc 13.5, 3.19); Chương 8 có đúng 8.1–8.8 (tr. 166, 168, 174, 176). Không có bài nào của SB cho rollout, MCTS (ngoài UCB), tối ưu kế hoạch bằng đạo hàm, điều khiển dự báo, phương pháp entropy chéo.

## 2. Bài tập của ghi chú (Bài tập củng cố, 11.1–11.11)

Bài của ghi chú do học phần soạn (BT-RL-1 chỉ ràng buộc `exercises.md`). Dữ kiện trùng ví dụ của ghi chú phải chép lại trong đề (BT6, GC23); con số lấy từ `ke-hoach-ghi-chu.md` mục 7. Mỗi bài có `hint`, `solution` chia câu, dòng kiểm tra (BT5).

### Mức nhận biết

- **11.1 Phân loại cách dùng mô hình** (mục tiêu 1, 3; mạch 4). Đề: bốn thủ tục (lặp giá trị đồng bộ Thuật toán 04.28 trên mô hình đã biết; bước (f) của Dyna-Q; MCTS tại trạng thái hiện tại; điều khiển dự báo với $\hat f$). (a) Mỗi thủ tục cần mô hình phân phối hay chỉ mô hình mẫu? (b) Lập kế hoạch nền hay tại thời điểm quyết định? (c) Với $b=50$ trạng thái kế, một cập nhật kỳ vọng tốn bao nhiêu lần đánh giá $\max_aQ$, một cập nhật mẫu tốn bao nhiêu? Lời giải: (a) phân phối; mẫu; mẫu; mô hình tất định khả vi (vừa là mô hình phân phối suy biến vừa là mô hình mẫu); (b) nền; nền; quyết định; quyết định; (c) $50$ và $1$. Kiểm: lỗi thường gặp coi Dyna-Q là lập kế hoạch tại thời điểm quyết định vì nó chạy sau mỗi bước thật.
- **11.2 Hai loại bất định** (mục tiêu 1; mạch 2; **trên deck** `L11-2-04`, "Lời giải:" dạng fragment). Đề: đúng hay sai, giải thích một câu: (a) thêm dữ liệu cho $(\mathrm F,\rightarrow)$ làm giảm xác suất trượt $0{,}2$; (b) sau một lần thử $(\mathrm B,\downarrow)\to\mathrm F$, $\hat p(\mathrm F\mid\mathrm B,\downarrow)=1$ nên cặp này không còn bất định; (c) trong môi trường tất định không có bất định nhận thức; (d) với $C(s,a)=8$ và $p=0{,}5$, độ lệch chuẩn của $\hat p$ là $0{,}177$. Lời giải: sai (bất định ngẫu nhiên không giảm); sai (độ lệch chuẩn với $n=1$ là $\sqrt{p(1-p)}$, Mệnh đề 11.5); sai (cặp chưa thử vẫn chưa biết); đúng, $\sqrt{0{,}25/8}=\sqrt{0{,}03125}=0{,}176777$.
- **11.3 Hành động và tùy chọn** (mục tiêu 6; mạch 5). Đề: (a) viết hành động $\downarrow$ thành tùy chọn $\langle\mathcal I,\pi,\beta\rangle$; (b) với $\omega_{\mathrm{cửa}}$, $\tau$ nhỏ nhất có thể là bao nhiêu khi bắt đầu ở $\mathrm F$, ở $\mathrm A$, và với xác suất bao nhiêu $\tau$ đạt giá trị nhỏ nhất đó; (c) nếu đổi $\pi_\omega(\mathrm A)=\leftarrow$ (đụng biên) và giữ $\beta=0$ ở phòng trái thì tùy chọn bắt đầu từ $\mathrm A$ có kết thúc không, kết quả nào của chương không áp dụng. Lời giải: (a) $\mathcal I=\mathcal S$, $\pi(s)=\downarrow$, $\beta\equiv1$; (b) $\mathrm F$: $\tau=1$ với xác suất $0{,}8$; $\mathrm A$: $\tau=3$ với xác suất $0{,}8^3=0{,}512$; (c) không kết thúc (ở yên mãi ở $\mathrm A$), vi phạm giả thiết "kết thúc với xác suất $1$" của Mệnh đề 11.41 và Định lý 11.42.

### Mức tính toán hoặc chứng minh

- **11.4 Bước thật đầu của lượt thứ hai trong Dyna-Q** (mục tiêu 2; mạch 2; **trên deck** `L11-2-10`, `L11-2-11`). Dữ kiện chép lại từ Ví dụ 11.7: $Q(\mathrm K,\rightarrow)=0{,}75$, $Q(\mathrm F,\rightarrow)=0{,}225$, mọi ô khác $0$; mô hình tất định đã có $(\mathrm A,\rightarrow)\mapsto(0,\mathrm B)$, $(\mathrm B,\downarrow)\mapsto(0,\mathrm F)$, $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$, $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$; $\alpha=0{,}5$, $\gamma=0{,}9$, $n=2$. Bước thật $(\mathrm A,\rightarrow,0,\mathrm B)$; bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm B,\downarrow)$. Tính các ô đổi. Lời giải:
  - trực tiếp: mục tiêu $0+0{,}9\cdot\max_aQ(\mathrm B,a)=0$; $Q(\mathrm A,\rightarrow)=0$;
  - $(\mathrm F,\rightarrow)$: mục tiêu $0{,}9\cdot0{,}75=0{,}675$; sai lệch $0{,}45$; $Q=0{,}225+0{,}225=0{,}45$;
  - $(\mathrm B,\downarrow)$: mục tiêu $0{,}9\cdot\max_aQ(\mathrm F,a)=0{,}9\cdot0{,}45=0{,}405$; sai lệch $0{,}405$; $Q=0{,}2025$.
  - Kiểm: giá trị đã tới $\mathrm B$ dù tác tử thật mới ở $\mathrm B$; nếu đảo thứ tự hai cặp lập kế hoạch, $(\mathrm B,\downarrow)$ dùng $Q(\mathrm F,\rightarrow)=0{,}225$ và cho $0{,}10125$.
- **11.5 Vòng MCTS tiếp theo** (mục tiêu 4; mạch 3; **trên deck** `L11-3-09`, `L11-3-10`). Dữ kiện: thống kê sau Ví dụ 11.16: $\rightarrow$: $N=4$, $\bar Q=0{,}70$; $\downarrow$: $N=2$, $0{,}60$; $\uparrow$: $N=2$, $W=1{,}029$, $\bar Q=0{,}5145$; $\leftarrow$: $N=1$, $0{,}20$; $N(\mathrm F)=9$; $c_{\mathrm{ucb}}=1$. (a) Cạnh nào được chọn? (b) Giả sử mở rộng ra $\mathrm E$ và mô phỏng $\mathrm E\xrightarrow{\rightarrow}\mathrm F\xrightarrow{\rightarrow}\mathrm K\xrightarrow{\rightarrow}\mathrm Z$ không trượt; tính thống kê mới của cạnh đó. Lời giải: (a) $\ln9=2{,}197225$; chỉ số $1{,}441152$; $1{,}648147$; $1{,}562647$; $1{,}682304$; chọn $\leftarrow$. (b) $G=\gamma^3=0{,}729$; $N=2$, $W=0{,}929$, $\bar Q=0{,}4645$; $N(\mathrm F)=10$. Kiểm: $\sqrt{2{,}197225}=1{,}482304$.
- **11.6 Kế hoạch hai bước từ $x_0=1$** (mục tiêu 5; mạch 4; **trên deck** `L11-4-09`, `L11-4-10`). Dữ kiện: mô hình $\hat f(x,u)=x+u$, chi phí $x_{t+1}^2+u_t^2$, $h=2$, $x_0=1$. (a) Gradient tại $(0,0)$ bằng khai triển và bằng truy hồi ngược; (b) một bước $\eta=0{,}1$ và $J$ mới; (c) kế hoạch tối ưu và $J^*$. Lời giải: $J(0,0)=2$; (a) $(4,2)$ cả hai cách ($\lambda_2=2$, $\lambda_1=4$); (b) $(-0{,}4;\ -0{,}2)$, $x_1=0{,}6$, $x_2=0{,}4$, $J=0{,}36+0{,}16+0{,}16+0{,}04=0{,}72$; (c) $(-0{,}6;\ -0{,}2)$, $x_1=0{,}4$, $x_2=0{,}2$, $J^*=0{,}6$. Kiểm: bằng một phần tư Ví dụ 11.19 ($J$ bậc hai thuần nhất, $x_0$ giảm một nửa).
- **11.7 Mô hình tùy chọn khi trượt nhiều hơn** (mục tiêu 6; mạch 5; **trên deck** `L11-5-09`, `L11-5-10`). Dữ kiện: mê cung hai phòng, xác suất trượt $q=0{,}5$, $\gamma=0{,}9$, tùy chọn $\omega_{\mathrm{cửa}}$, $\omega_{\mathrm{đích}}$ như Ví dụ 11.24. (a) Chứng minh thừa số của một bước đi đúng là $\rho=(1-q)\gamma/(1-q\gamma)$; (b) tính $p(\mathrm K\mid\mathrm B,\omega_{\mathrm{cửa}})$, $r(\mathrm K,\omega_{\mathrm{đích}})$ và giá trị của $\mathrm B$ theo chính sách phân cấp "cửa rồi đích"; (c) kiểm Mệnh đề 11.41. Lời giải: (a) chuỗi hình học $\sum_j\gamma^jq^{j-1}(1-q)$; (b) $\rho=0{,}45/0{,}55=0{,}818182$; $p=\rho^2=0{,}669421$; $r=(1-q)/(1-q\gamma)=0{,}909091$; $v_\mu(\mathrm B)=0{,}669421\cdot0{,}909091=0{,}608565$; (c) $0{,}669421\le0{,}9$. Kiểm: $q=0{,}2$ cho lại $0{,}878049$ của Ví dụ 11.25.
- **11.8 Số mô phỏng của rollout với bốn hành động** (mục tiêu 4; mạch 3). Dữ kiện: $q_{\pi_0}(\mathrm F,\cdot)$ của Ví dụ 11.12 ($0{,}388554$; $0{,}181399$; $0{,}118132$; $0{,}118132$), lợi tức trong $[0,1]$. (a) Chứng minh: với $K$ hành động và hành động tốt nhất $a^*$ duy nhất, xác suất thuật toán rollout không chọn $a^*$ không vượt $\sum_{a\ne a^*}\exp(-m\Delta_a^2/B^2)$; (b) tìm $m$ nhỏ nhất để chặn này không vượt $0{,}05$ tại $\mathrm F$. Lời giải: (a) chặn hợp trên biến cố "$\bar G(a)\ge\bar G(a^*)$" và Mệnh đề 11.22; (b) $\Delta=0{,}207155$, $\Delta'=0{,}270422$; $m=70$ cho $0{,}0616$; $m=75$ cho $0{,}0483$; đáp số $m=75$. Kiểm: với hai hành động $m=70$ đã đủ (Ví dụ 11.14); thêm hành động làm tăng $m$. Đã kiểm: $m=74$ cho $0{,}0507>0{,}05$, nên $75$ là nhỏ nhất.

### Mức vận dụng

- **11.9 Chọn cách dùng mô hình** (mục tiêu 7; mạch 5). Đề "Giả sử" ba bài toán: (a) trò chơi bàn cờ hai người, luật biết đầy đủ, mỗi nước có thời gian suy nghĩ cố định, hành động rời rạc; (b) cánh tay robot với mô hình động lực khả vi học từ dữ liệu, hành động liên tục, điều khiển ở tần số cao; (c) robot giao hàng trong tòa nhà nhiều phòng, mỗi lượt dài hàng nghìn bước, có các kỹ năng đi tới cửa đã lập trình sẵn. Với mỗi bài: chọn phương pháp của chương, nêu kết quả bảo đảm (số hiệu) và một giả thiết của kết quả đó cần kiểm. Lời giải: (a) MCTS với UCT (Thuật toán 11.26; Định lý 11.27 cần chân trời hữu hạn, phần thưởng chuẩn hóa; trò chơi hai người nằm ngoài giả thiết MDP một tác tử, nêu rõ); (b) MPC với gradient qua mô hình hoặc CEM (Định nghĩa 11.32, Mệnh đề 11.30, 11.36: sai số tích lũy theo $h$); (c) tùy chọn, lặp giá trị với tùy chọn (Định lý 11.44: cần $\Omega(s)\supseteq\mathcal A(s)$ để đạt tối ưu, tùy chọn phải kết thúc với xác suất $1$). Kiểm: lỗi thường gặp chọn Dyna-Q cho (b) (bảng không dùng được cho hành động liên tục).
- **11.10 Bài tập tổng hợp: mô hình đếm và tùy chọn trên mê cung hai phòng** (mục tiêu 1, 6, 7; mạch 5; **bài tập tổng hợp của mạch "Tổng kết"**, trên deck `L11-6-04`, `L11-6-05`). Dữ kiện "Giả sử" sau một số lượt: $C(\mathrm B,\downarrow)=4$ với $3$ lần tới $\mathrm F$, $1$ lần ở yên; $C(\mathrm F,\rightarrow)=10$ với $8$ lần tới $\mathrm K$; $C(\mathrm K,\rightarrow)=5$ với $4$ lần tới $\mathrm Z$; phần thưởng như Ví dụ 11.1; $\gamma=0{,}9$; mọi lần không đi đúng là ở yên. (a) Tính mô hình đếm của ba cặp và độ lệch chuẩn ước lượng (thế $\hat p$ vào Mệnh đề 11.5) của $\hat p(\mathrm F\mid\mathrm B,\downarrow)$; (b) tính mô hình tùy chọn $p(\mathrm K\mid\mathrm B,\omega_{\mathrm{cửa}})$ và $r(\mathrm K,\omega_{\mathrm{đích}})$ trên mô hình đếm; (c) giá trị lập kế hoạch $\hat v(\mathrm B)$ theo "cửa rồi đích" (Định lý 11.42); (d) so với $v_*(\mathrm B)=0{,}752166$ và với giá trị $0{,}81$ của mô hình tất định (Tình huống 11.2); kết luận về loại sai số. Lời giải:
  - (a) $\hat p(\mathrm F\mid\mathrm B,\downarrow)=0{,}75$, $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=0{,}8$, $\hat p(\mathrm Z\mid\mathrm K,\rightarrow)=0{,}8$; độ lệch chuẩn $\sqrt{0{,}75\cdot0{,}25/4}=0{,}216506$;
  - (b) thừa số của $\mathrm B\to\mathrm F$: $0{,}75\cdot0{,}9/(1-0{,}25\cdot0{,}9)=0{,}675/0{,}775=0{,}870968$; của $\mathrm F\to\mathrm K$: $0{,}878049$; $p=0{,}764752$; $r(\mathrm K,\omega_{\mathrm{đích}})=0{,}8/0{,}82=0{,}975610$;
  - (c) $\hat v(\mathrm B)=0{,}764752\cdot0{,}975610=0{,}746100$;
  - (d) sai số $-0{,}006066$ so với $v_*$ (bất định nhận thức tại cặp chỉ có 4 mẫu, cùng bậc với độ lệch chuẩn $0{,}2165$ của $\hat p$); mô hình tất định sai $+0{,}057834$ (sai hệ thống, không giảm khi thêm dữ liệu).
  - Kiểm: thay $\hat p(\mathrm F\mid\mathrm B,\downarrow)=0{,}8$ cho lại $v_*(\mathrm B)$.
- **11.11 Điều khiển dự báo với mô hình sai** (mục tiêu 5, 7; mạch 4). Dữ kiện: luật $u=-0{,}6x$ thiết kế trên mô hình $\hat f(x,u)=x+u$ (Ví dụ 11.20); hệ thật $x'=ax+u$. (a) Với $a=1{,}2$; $1{,}5$; $1{,}7$, tính hệ số vòng kín và ba bước từ $x_0=2$; (b) tìm mọi $a$ để vòng kín co về $0$; (c) giải thích vì sao vòng kín chịu được sai số mô hình còn sai số vòng hở tăng theo Mệnh đề 11.36. Lời giải: (a) $0{,}6$: $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$; $0{,}9$: $2;\ 1{,}8;\ 1{,}62;\ 1{,}458$; $1{,}1$: $2;\ 2{,}2;\ 2{,}42;\ 2{,}662$ (phân kỳ); (b) $\lvert a-0{,}6\rvert<1$, tức $-0{,}4<a<1{,}6$; (c) lập lại kế hoạch tại mỗi bước dùng trạng thái thật nên sai số không tích lũy qua dự báo nhiều bước. Kiểm: $a=1$ cho $0{,}4$ của Ví dụ 11.20.

## 3. Bài của `exercises.md` (11.12–11.19): đề, nguồn, ý lời giải

Mỗi bài theo BT-RL-4: tiêu đề `### Bài tập 11.k. Tên bài` (số SB ghi ở dòng nguồn, BT4); dòng "**Mức độ:**" kèm mục tiêu và mạch; dòng "**Nguồn:**" với số bài, mục, trang; dòng "Trùng trang chiếu" chỉ khi có (không bài nào của tệp này lên deck, mục 8); khối `exercise`, `hint`, `solution`; lời giải "**Câu (a).**", …, kết bằng "**Kiểm tra lại.**" nêu hai hoặc ba lỗi thường gặp cùng kết quả sai (BT-RL-4). Lời giải tự viết theo ký hiệu ghi chú (BT7); sách hướng dẫn giải chỉ đối chiếu sau.

### Mức nhận biết

- **11.12. Dyna-Q+ hơn Dyna-Q ở cả hai pha** (SB Bài tập 8.2, §8.3, tr. 168; Ví dụ 8.2, 8.3 và Hình 8.4, 8.5, tr. 166–167). Mục tiêu 2; mạch 2. Đề nêu lại: hai thí nghiệm (đổi môi trường sau 1 000 và 3 000 bước), mô tả đường lợi tức tích lũy bằng lời, quy tắc thưởng $r+\kappa\sqrt\ell$ và hai thay đổi của chú thích 1. Ý lời giải: thưởng thăm dò làm tác tử thử có hệ thống các cặp lâu chưa thử ngay từ pha đầu, và chú thích 1 cho phép lập kế hoạch cả với cặp chưa thử (mô hình lạc quan "ở yên, thưởng $0$" cộng thưởng), nên Dyna-Q+ tìm đường ngắn nhất sớm hơn và mô hình đầy đủ hơn; ở pha hai, cùng cơ chế giúp phát hiện thay đổi. Kiểm tra lại: lỗi trả lời chỉ về pha hai; lỗi cho rằng thưởng làm ước lượng đúng hơn.
- **11.13. Khoảng cách thu hẹp ở đầu thí nghiệm lối tắt** (SB Bài tập 8.3, §8.3, tr. 168; Hình 8.5, tr. 167). Mục tiêu 2; mạch 2. Ý lời giải: trước khi lối tắt mở, môi trường không đổi; Dyna-Q+ vẫn trả giá thăm dò (đi lệch để thử các cặp có $\ell$ lớn), còn Dyna-Q đã khai thác đường tối ưu, nên tốc độ tăng lợi tức tích lũy của Dyna-Q bắt kịp dần. Kiểm tra lại: lỗi gán cho "Dyna-Q học nhanh hơn"; lỗi bỏ qua việc thưởng tăng theo $\sqrt\ell$ khi cặp lâu không thử.

### Mức tính toán hoặc chứng minh

- **11.14. Phân phối lệch và cập nhật mẫu** (SB Bài tập 8.6, §8.5, tr. 174; thiết lập Hình 8.7, tr. 173–174). Mục tiêu 3; mạch 2. Đề nêu lại thiết lập của Mệnh đề 11.15 và yêu cầu dạng định lượng: (a) với giá trị kế độc lập phương sai $1$ và phân phối $\hat p_1,\dots,\hat p_b$, chứng minh sai số bình phương trung bình kỳ vọng sau $k$ cập nhật mẫu là $(1-\sum_i\hat p_i^2)/k$; (b) tính cho $b=100$ với $\hat p_1=0{,}9$, các trạng thái còn lại chia đều $0{,}1$, so với phân phối đều; (c) kết luận. Ý lời giải: $\mathbb E[\sum_i\hat p_i(x_i-\bar x)^2]=1-\sum_i\hat p_i^2$ (khai triển $\operatorname{Var}(x_i-\sum_j\hat p_jx_j)=1-2\hat p_i+\sum_j\hat p_j^2$); (b) $1-0{,}81-0{,}01/99=0{,}189899$, sau một cập nhật sai số căn $0{,}435774$ so với $\sqrt{0{,}99}=0{,}994987$ khi đều; (c) lập luận ủng hộ cập nhật mẫu **mạnh lên**: mẫu rơi vào trạng thái có xác suất lớn, phương sai nhỏ, trong khi cập nhật kỳ vọng vẫn tốn $b$ phép đánh giá. Kiểm tra lại: phân phối đều cho lại $(b-1)/b$; lỗi dùng phương sai không trọng số. Lưu ý: bài mở rộng Mệnh đề 11.15(b); đề phải nêu rõ (a) là yêu cầu chứng minh, không có trong ghi chú (BT1).
- **11.15. Tùy chọn trong thiết lập phần thưởng trung bình** (SB Bài tập 17.1, §17.2, tr. 464; (17.2)–(17.4), tr. 462–463; §10.3, tr. 249–250, (10.6), (10.9) và phương trình Bellman vi phân). Mục tiêu 6; mạch 5. Đề phải phát biểu lại thiết lập phần thưởng trung bình: tốc độ phần thưởng $r(\mu)$, lợi tức vi phân $\sum_k(R_{t+k}-r(\mu))$, giá trị vi phân, phương trình Bellman vi phân cho hành động. Ý lời giải: $r(s,\omega)=\mathbb E[\sum_{k=1}^{\tau}(R_k-r(\mu))]$ (phần thưởng của tùy chọn trừ $r(\mu)$ nhân thời lượng kỳ vọng); $p(s'\mid s,\omega)=\Pr\{S_\tau=s'\}$ (xác suất thật, tổng bằng $1$, không chiết khấu); $v_\mu(s)=\sum_\omega\mu(\omega\mid s)[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)v_\mu(s')]$. Kiểm tra lại: lỗi giữ $\gamma^k$; lỗi quên trừ $r(\mu)$ theo từng bước (trừ một lần cho cả tùy chọn). Cần kiểm lời giải với Sutton, Precup và Singh (1999) hoặc tài liệu về SMDP phần thưởng trung bình (Puterman 1994, chương bán-MDP) trước khi viết.

### Mức vận dụng

- **11.16. Bootstrap nhiều bước so với Dyna** (SB Bài tập 8.1, §8.2, tr. 166; Ví dụ 8.1, Hình 8.2, 8.3, tr. 164–165). Mục tiêu 2; mạch 2. Đề nêu lại mê cung Dyna, Hình 8.3 bằng lời, cập nhật Sarsa $n$ bước (phát biểu đầy đủ, vì ghi chú 05–07 không dạy; dẫn lợi tức $n$ bước của Định nghĩa 10.11 cho phần lợi tức). Ý lời giải: phương pháp $n$ bước sau lượt đầu cập nhật được tới $n$ trạng thái cuối của quỹ đạo thật, giúp nhiều so với một bước; nhưng (i) chỉ cập nhật dọc quỹ đạo đã đi, theo đúng thứ tự đã đi, kể cả vòng lặp vô ích của lượt đầu khoảng 1 700 bước; (ii) mỗi mẫu dùng một lần; (iii) không ghép các đoạn của nhiều lượt khác nhau. Dyna dùng lại mọi chuyển đã gặp ở mọi lúc, ghép chúng qua mô hình, nên lan giá trị theo đường ngắn nhất dù chưa đi trọn đường đó. Kết luận có điều kiện: $n$ bước có thể tiến gần Dyna với $n$ nhỏ về số lượt, nhưng không bằng Dyna với $n=50$ khi môi trường tất định và mô hình đúng. Kiểm tra lại: lỗi cho rằng Monte Carlo ($n=\infty$) bằng Dyna; lỗi quên rằng $n$ bước vẫn chỉ cập nhật cặp đã đi.
- **11.17. Dyna-Q cho môi trường ngẫu nhiên và thay đổi** (SB Bài tập 8.5, §8.3, tr. 168; hộp Dyna-Q tr. 164). Mục tiêu 1, 2; mạch 2. Ý lời giải: (a) thay bước (e) bằng mô hình đếm (Định nghĩa 11.4), bước lập kế hoạch rút $S'$ theo $\hat p$ hoặc dùng cập nhật kỳ vọng; (b) trong môi trường thay đổi, bộ đếm tích lũy dữ liệu cũ nên $\hat p$ đổi chậm: sau $C$ lần thử cũ, cần cỡ $C$ lần thử mới để $\hat p$ dịch quá nửa; (c) dùng bộ đếm có quên (trọng số giảm theo tuổi mẫu, hoặc cửa sổ trượt) cộng thưởng thăm dò kiểu Dyna-Q+ để thử lại cặp lâu chưa thử. Kiểm tra lại: lỗi giữ bước (e) "ghi đè" (là mô hình tất định); lỗi đề xuất bỏ hẳn dữ liệu cũ (mất khả năng ước lượng xác suất). Số "cỡ $C$" phải tính lại bằng ví dụ trong lời giải (giả sử $C=20$ lần cũ đều thành công, xác suất mới $0$: sau $j$ lần mới $\hat p=20/(20+j)$, dưới $0{,}5$ khi $j>20$).
- **11.18. Đỉnh ở bước 11 của UCB** (SB Bài tập 2.8, §2.7, tr. 36; §2.3, tr. 28–29; Hình 2.4, tr. 36). Mục tiêu 4; mạch 3. Ý lời giải: mười bước đầu thử mỗi tay một lần ($N=0$ được coi là cực đại); ở bước 11 mọi $N=1$, số hạng thăm dò bằng nhau, nên UCB chọn tay có mẫu đầu lớn nhất, thường là tay tốt: phần thưởng trung bình tăng vọt. Ở bước 12, tay đó có $N=2$: số hạng thăm dò của nó là $c\sqrt{\ln11/2}$, của tay khác $c\sqrt{\ln11}$; với $c=2$, chênh $2(1{,}548514-1{,}094965)=0{,}907098$, lớn so với chênh của các ước lượng một mẫu, nên các bước sau quay về thử tay khác và phần thưởng giảm. Với $c=1$, chênh còn $0{,}453549$: đỉnh kém rõ. Kiểm tra lại: lỗi dùng $\ln t$ với $t$ là số lần chọn tay đó; lỗi cho rằng đỉnh do $\varepsilon$.
- **11.19. Thưởng thăm dò chỉ dùng khi chọn hành động [Lập trình]** (SB Bài tập 8.4, §8.3, tr. 168). Mục tiêu 2; mạch 2. Đề: cài đặt hai tác tử trên mê cung có lối tắt (dùng mê cung đổi cửa của Ví dụ 11.8 hoặc mê cung của SB Ví dụ 8.3, nêu đủ dữ kiện): Dyna-Q+ (Định nghĩa 11.12) và biến thể chọn $\arg\max_a[Q(S_t,a)+\kappa\sqrt{\ell(S_t,a)}]$ không cộng thưởng trong cập nhật; so lợi tức tích lũy. Ý lời giải (phải chạy thật, như Bài tập 04.21, kết quả nhúng trong lời giải kèm cấu hình, hạt giống, số lần lặp; không khẳng định kết quả chưa chạy, BT-RL-7 tinh thần): biến thể không làm sai $Q$ nhưng thăm dò chỉ cục bộ, một bước, nên không lập kế hoạch đi xa để thử cặp ở trạng thái khác; dự kiến kém hơn Dyna-Q+ trong việc phát hiện lối tắt. Điểm mạnh: $Q$ vẫn ước lượng $q_*$ của mô hình (Mệnh đề 11.9). Kiểm tra lại: lỗi cộng thưởng cả vào mục tiêu (thành Dyna-Q+); lỗi cập nhật $\ell$ cả khi lập kế hoạch. QB4.

## 4. Bảng phủ mục tiêu học tập ↔ bài tập (BT9, GC26)

| Mục tiêu | Bài của ghi chú | Bài của `exercises.md` |
|---|---|---|
| 1. Mô hình và tính bất định | 11.1, 11.2, 11.10 | 11.17 |
| 2. Dyna | 11.4 | 11.12, 11.13, 11.16, 11.17, 11.19 |
| 3. Cập nhật kỳ vọng và cập nhật mẫu | 11.1 | 11.14 |
| 4. Rollout và tìm kiếm theo cây | 11.5, 11.8 | 11.18 |
| 5. Tối ưu kế hoạch bằng đạo hàm | 11.6, 11.11 | — (khoảng trống, QB3; BT9) |
| 6. Tùy chọn | 11.3, 11.7, 11.10 | 11.15 |
| 7. Chọn cách dùng mô hình | 11.9, 11.10, 11.11 | — |

Mỗi mục tiêu có ít nhất một bài; mục tiêu 5 và 7 chỉ dựa vào bài của ghi chú, ghi lý do trong `review-log.md` (BT-RL-1, BT9).

## 5. Khoảng trống và nguồn khác (BT-RL-1, BT9)

- **Mục tiêu 5** (đạo hàm qua mô hình, MPC, CEM, sai số tích lũy): SB không có bài. Kiểm theo thứ tự danh sách BT-RL-1: Bertsekas (2019) (chương về xấp xỉ trong không gian giá trị, rollout và MPC; cần biết sách có bài tập cuối chương hay không), Puterman (1994) (không có MPC), Szepesvári (2010) (không có bài tập, cần kiểm), Bertsekas và Tsitsiklis (1996), Goodfellow và cộng sự (2016) (không có bài tập). Không có bản trong `sources/` (QB3).
- **MCTS, rollout:** ngoài SB 2.8 chỉ có thể là bài của Bertsekas (2019) về rollout (cần kiểm).
- **Bán-MDP:** Puterman (1994), chương bán-MDP, có bài tập cuối chương (cần kiểm nội dung và số bài) — ứng viên thay hoặc bổ sung cho SB 17.1 nếu QB2 quyết bỏ 17.1.
- Mọi bài thêm từ sách khác ghi lý do trong `review-log.md` (BT-RL-1).

## 6. Số hiệu (BT4)

- Ghi chú: Bài tập 11.1–11.11 (chỉ "Bài tập củng cố").
- `exercises.md`: Bài tập 11.12–11.19, theo thứ tự mức (nhận biết → tính toán hoặc chứng minh → vận dụng), trong mỗi mức theo thứ tự mục của ghi chú.
- Nếu ghi chú đổi số bài khi soạn, `exercises.md` dịch số theo, trước khi deck dẫn số (BT-RL-9: tệp bài tập đạt kiểm định trước khi soạn deck).

## 7. Khung tệp `materials/lec-11/exercises.md` (BT-RL-3, BT-RL-4, BT3)

```
# Bài tập Bài 11 — Lập kế hoạch dựa trên mô hình

<đoạn mở: tám bài 11.12–11.19, tiếp số mười một bài 11.1–11.11 của ghi chú bài giảng
(liên kết material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html),
không lặp đề của ghi chú; mọi bài lấy từ bài tập của Sutton và Barto (2018), ghi số bài, mục, trang;
ba mức: nhận biết (11.12–11.13), tính toán hoặc chứng minh (11.14–11.15), vận dụng (11.16–11.19);
bảng dưới xếp bài của tệp và bài của ghi chú theo mạch của bộ trang chiếu, bài của ghi chú đứng sau chữ "ghi chú".>

| Mạch | Mở phần | Bài tập |
| --- | --- | --- |
| 1. Mở đầu | [Mở phần](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/1/1) | — |
| 2. Tính bất định và lập kế hoạch nền | [Mở phần](…#/2/1) | 11.12, 11.13, 11.14, 11.16, 11.17, 11.19; ghi chú: 11.2, 11.4 |
| 3. Tìm kiếm theo cây Monte Carlo | [Mở phần](…#/3/1) | 11.18; ghi chú: 11.5, 11.8 |
| 4. Tối ưu kế hoạch dựa trên đạo hàm | [Mở phần](…#/4/1) | ghi chú: 11.1, 11.6, 11.11 |
| 5. Học tăng cường phân cấp | [Mở phần](…#/5/1) | 11.15; ghi chú: 11.3, 11.7, 11.9, 11.10 |
| 6. Tổng kết | [Mở phần](…#/6/1) | — |

## Hướng dẫn và ký hiệu
<ký hiệu theo ghi chú Bài 11; S_t, A_t, R_{t+1}, γ, G_t; mô hình đếm C(s,a), p̂; quy ước
"công thức của sách" khi dẫn số công thức SB; chữ của sách khác ghi chú: SB viết τ cho số bước
từ lần thử gần nhất (ghi chú: ℓ), c cho hằng số UCB (ghi chú: c_ucb), γ_ω cho xác suất tiếp tục
(ghi chú: β_ω = 1 − γ_ω); dữ kiện dùng chung: mê cung Dyna của SB Ví dụ 8.1, hai thí nghiệm
của Ví dụ 8.2, 8.3 (nêu lại trong từng bài dùng nó, BT6); số thập phân dấu phẩy.>

## Mức nhận biết
### Bài tập 11.12. Dyna-Q+ ở hai pha của thí nghiệm
### Bài tập 11.13. Khoảng cách giữa Dyna-Q+ và Dyna-Q trước khi có lối tắt
## Mức tính toán hoặc chứng minh
### Bài tập 11.14. Phân phối trạng thái kế lệch và cập nhật mẫu
### Bài tập 11.15. Tùy chọn trong thiết lập phần thưởng trung bình
## Mức vận dụng
### Bài tập 11.16. Bootstrap nhiều bước so với Dyna
### Bài tập 11.17. Dyna-Q cho môi trường ngẫu nhiên và môi trường thay đổi
### Bài tập 11.18. Đỉnh ở bước thứ mười một của quy tắc cận tin cậy trên
### Bài tập 11.19. Thưởng thăm dò chỉ dùng khi chọn hành động [Lập trình]

## Tài liệu tham khảo
- Sutton và Barto (2018): Bài tập 2.8 (§2.7, tr. 36; §2.3, tr. 28–29); 8.1 (§8.2, tr. 166; tr. 164–165);
  8.2–8.5 (§8.3, tr. 168; tr. 166–167); 8.6 (§8.5, tr. 174); 17.1 (§17.2, tr. 464; §10.3, tr. 249–250).
```

- Cột "Mở phần" liên kết `#/N/1` tới trang tiêu đề mạch (`hashOneBasedIndex: true`); điền hoặc kiểm lại sau khi deck xong (BT-RL-9).
- Bảng xếp mỗi bài vào mạch cung cấp kiến thức cuối cùng bài cần (NT15): 11.1 cần MCTS và MPC nên ở mạch 4; 11.9, 11.10 cần tùy chọn nên ở mạch 5; mạch "Tổng kết" không có bài vì không có khái niệm mới.
- Không câu nguồn gốc số liệu (VP18); dữ kiện tự dựng của bài ghi chú viết "Giả sử …".
- Mẫu `_templates/exercises.md` dòng 15 (chia theo mạch) đã bị thay: chia theo mức (mục 6 của `NGUYEN-TAC-HOC-PHAN.md`).

## 8. Bài tập trên bộ trang chiếu (NT24, NT15, NT-RL-9, NT-RL-10, BT11)

| Trang (đề; lời giải) | Bài | Cụm | Hình thức lời giải | Ghi chú diễn giả (NT-RL-10) |
|---|---|---|---|---|
| `L11-2-04` | 11.2 | mô hình và bất định | "Lời giải:" dạng fragment cùng trang (bốn dòng đúng/sai) | năng lực: phân biệt hai loại bất định; "Gợi ý:" đọc Mệnh đề 11.5 với $n=1$ |
| `L11-2-10`; `L11-2-11` | 11.4 | Dyna-Q | trang kế tiếp cùng tiêu đề, ba cập nhật theo khuôn bảng mục tiêu/sai lệch/giá trị mới (NT-RL-5) | năng lực: chạy bước (d)–(f); "Gợi ý:" mục tiêu dùng $\max_aQ$ của bảng hiện tại |
| `L11-3-09`; `L11-3-10` | 11.5 | MCTS | trang kế tiếp; bảng chỉ số cùng khuôn với `L11-3-05` (NT-RL-5) | năng lực: tính chỉ số UCT, cập nhật ngược; "Gợi ý:" $N(\mathrm F)=9$ |
| `L11-4-09`; `L11-4-10` | 11.6 | tối ưu kế hoạch | trang kế tiếp; hai bản gradient | năng lực: truy hồi ngược; "Gợi ý:" $\lambda_2=2x_2$ |
| `L11-5-09`; `L11-5-10` | 11.7 | tùy chọn | trang kế tiếp | năng lực: mô hình tùy chọn; "Gợi ý:" chuỗi hình học |
| `L11-6-04`; `L11-6-05` | 11.10 | tổng hợp (NT15, NT-RL-9) | trang kế tiếp; bốn câu, mỗi câu một dòng kết quả | năng lực: dùng Định nghĩa 11.4, Mệnh đề 11.5, Định nghĩa 11.40, Định lý 11.42 trên một bài toán |

- Đề trên trang giữ dữ liệu, câu chữ và kết quả của bài trong ghi chú, mở bằng "Câu hỏi:", ghi "Bài tập 11.k" (NT24). Đề dài (11.4, 11.10) có thể vượt trần mật độ: ngoại lệ "đề bài tập giữ nguyên câu chữ" của NT17, ghi trong storyboard với số âm tiết.
- Bảng "Bài tập về nhà" (`L11-6-07`) đánh dấu "(trên lớp)" cho 11.2, 11.4, 11.5, 11.6, 11.7, 11.10 (NT15, BT11).
- Không bài nào của `exercises.md` lên trang chiếu; dòng "Trùng trang chiếu" vắng trong mọi bài của tệp (BT-RL-4 chỉ yêu cầu khi có).

## 9. Câu hỏi mở

| Mã | Câu hỏi | Đề xuất |
|---|---|---|
| QB1 | SB Bài tập 8.7 và 8.8 [Lập trình] thuộc lấy mẫu theo quỹ đạo, phần đọc thêm của ghi chú, cần nhiều dữ kiện của Hình 8.8. | Không đưa vào `exercises.md`. |
| QB2 | SB Bài tập 17.1 cần thiết lập phần thưởng trung bình, học phần chưa dạy. | Giữ, với đoạn phát biểu lại §10.3 trong đề (BT6) và mức "tính toán hoặc chứng minh"; đây là bài duy nhất của SB cho mục tiêu 6. Nếu tác giả thấy quá xa, thay bằng bài bán-MDP của Puterman (1994) sau khi kiểm (QB3). |
| QB3 | Mục tiêu 5 và phần MCTS ngoài UCB không có bài của SB. | Điều phối viên kiểm Bertsekas (2019) và Puterman (1994) (không có bản trong `sources/`); nếu không có bài phù hợp, mục tiêu 5 và 7 dựa vào Bài tập 11.6, 11.11, 11.9, 11.10 của ghi chú (BT9) và ghi lý do vào `review-log.md`. |
| QB4 | SB Bài tập 8.4 [Lập trình] cần chạy thí nghiệm thật để viết lời giải. | Giữ như Bài tập 04.21: tác tử soạn chạy mã trong scratchpad, lời giải nêu cấu hình, hạt giống, số lần lặp và kết quả đo, không đưa mã vào repo; nếu không chạy được, bỏ bài và ghi lý do vào `review-log.md` (không thay bằng bài tự dựng, BT-RL-1). |
| QB5 | SB Bài tập 2.8 cần phát biểu lại bộ thử 10 tay và Hình 2.4. | Giữ; UCB là thành phần của MCTS (mục tiêu 4). |
| QB6 | Bài tập tổng hợp của mạch "Tổng kết" (NT15, NT-RL-9) là 11.10 (bài của ghi chú) chứ không phải bài của `exercises.md`. | Đồng ý: NT15 cho phép "lấy từ bài tập của bài"; 11.10 dùng bốn kết quả của bài trên mê cung hai phòng. |
| QB7 | Bài của ghi chú có dùng dữ kiện tự dựng ("Giả sử") cho 11.9, 11.10 không, khi BT-RL-1 cấm bài tự dựng? | BT-RL-1 chỉ ràng buộc `exercises.md`; "Bài tập củng cố" của ghi chú do học phần soạn (BT-RL-5, như ghi chú 06, 10). Ghi rõ trong `review-log.md`. |
