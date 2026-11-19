# Dàn ý Bài 11: Lập kế hoạch dựa trên mô hình

## Phạm vi và nguồn (giai đoạn I.1, 2026-11-19)

- **Sản phẩm của dàn ý:** ghi chú mới `2627-1/materials/lec-11/lecture-note.md` (giai đoạn I); dàn ý này cũng là đầu vào của `exercises.md` (giai đoạn II) và `storyboard.md` (giai đoạn III). Dàn ý thay hoàn toàn dàn ý của Bài 11 cũ (gradient chính sách nâng cao, bản cũ còn trong git) theo quyết định Q2 của `prompt-xay-dung-bai-11.md`.
- **Đầu vào đã duyệt:** `ke-hoach-ghi-chu.md` (đầu vào chính), `ke-hoach-bai-tap.md`, `ke-hoach-trang-chieu.md` cùng bảng Q của `prompt-xay-dung-bai-11.md` (mọi ô Q1–Q18 chốt "Theo đề xuất", người dùng 2026-11-19). Số liệu của hai ví dụ xuyên suốt lấy nguyên từ mục 7 của `ke-hoach-ghi-chu.md` (điều phối viên đã tính lại, `review-log.md` mục "Lập kế hoạch Bài 11 mới (2026-11-19)"); người lập dàn ý chạy lại $v_*$, $v_{\pi_0}$, $q_{\pi_0}(\mathrm F,\cdot)$, bảng lặp giá trị một bước và $m=70$ trong scratchpad: khớp, chỉ lệch chữ số thứ sáu do làm tròn (xem Đ9).
- **Nguồn phạm vi và thứ tự** (Q1; `NGUYEN-TAC-HOC-PHAN.md` mục 3, "P1, Bài 11 (riêng)"): mục lục Chương 11 của *Giáo trình Học tăng cường và lập kế hoạch* (Tạ Việt Cường – Trần Quốc Long): 11.1 Tính bất định của môi trường; 11.2 Tìm kiếm theo cây Monte Carlo; 11.3 Tối ưu kế hoạch dựa trên đạo hàm; 11.4 Học tăng cường phân cấp (11.4.1 Tuỳ chọn và mô hình bán-MDP; 11.4.2 Lập kế hoạch ở nhiều mức trừu tượng thời gian); 11.5 Tổng kết chương. Không có bộ trang chiếu nguồn trong `RL-hk2-2025-2026/`.
- **Nguồn nội dung** (GC-RL-5, GC25): Sutton và Barto (2018), viết tắt **SB**, §2.7, Chương 8 (§8.1–8.11), §16.6, §17.1–17.2, trang in = trang PDF − 22 (đã kiểm lại trên `/data/tqlong/qa/sources/sutton-barto-rl2020/extracted.md`, xem mục "Giáo trình tham khảo theo mục"); Bertsekas (2019) cho rollout và điều khiển dự báo (§2.4, §2.5.1, §5.1.2, theo mục lục chính thức; nội dung kiểm trên Bertsekas 2020); Szepesvári (2010) cho phát biểu gọn của quy tắc cận tin cậy trên (§4.2.1, bản nháp 2009 của tác giả); Puterman (1994) cho bán-MDP (theo tên chương). Không ghi số mục chưa kiểm (Q1, GC-RL-5). Bài báo gốc chỉ để kiểm chứng một mệnh đề cụ thể (P8); hằng số, bậc hội tụ, số định lý chỉ ghi sau khi kiểm trên bản gốc, chưa kiểm thì giữ câu định tính có nguồn và ghi "chờ kiểm" trong dàn ý (Q9). Người dùng cho phép tải bài báo (2026-11-19); bản gốc nằm ở `/data/tqlong/qa/sources/*-20261119/` và được kiểm trong `kiem-nguon-goc.md` của điều phối viên: Auer, Cesa-Bianchi và Fischer (2002); Kocsis và Szepesvári (2006) cùng bản dài của Kocsis, Szepesvári và Willemson (2006); Sutton, Precup và Singh (1999), viết tắt **SPS**; Chua và cộng sự (2018); Silver và cộng sự (2017); Deisenroth và Rasmussen (2011); Szepesvári (2010, bản nháp 2009); mục lục của Bertsekas (2019); Bertsekas (2020). Với các nguồn này, dàn ý ghi số định lý, phương trình, mục, trang đúng như báo cáo kiểm. Không có bản: Hoeffding (1963) (dẫn tên, không số định lý, số trang), nội dung chương của Bertsekas (2019) (chỉ tên và số mục), Puterman (1994), Goodfellow, Bengio và Courville (2016), Botev và cộng sự (2013).
- **Công cụ của Chương 4 giáo trình** (rollout, quy tắc cận tin cậy trên UCB1, điều khiển dự báo theo chân trời lùi) không có bài giảng trong học phần (đã kiểm: ghi chú 01–10 không có Dyna, rollout, UCB, MCTS); chúng được trình bày đầy đủ trong bài, nhóm `cầu nối` (Q3).
- **Đối tượng** (GC-RL-16): sinh viên đã học học máy, học sâu, thuật toán và Bài 01–10.
- **Bài tập:** không bài tập cuối mục; chỉ "Bài tập củng cố" 11.1–11.11; `exercises.md` tiếp số 11.12–11.19 (Q4, BT-RL-6).
- **Độ dài:** theo GC-RL-4 (8 000–30 000 từ `prose`); người dùng bỏ trần riêng 15 000–18 000 của Q5 (2026-11-19); ghi chú sau biên tập vòng 1 có khoảng 21 750 từ `prose`. **Thời lượng** 120 phút trình chiếu chỉ ghi trong dàn ý và storyboard.
- **Không có trong ghi chú:** bản đồ chủ đề, bảng phân loại, bảng thuật ngữ (chỉ ở dàn ý, GC-RL-12, GC-RL-13); câu nối nội dung sang bài sau hay sang Chương 14 của giáo trình (Q8, VP20); câu nguồn gốc số liệu (VP18); câu về trạng thái của văn bản (VP19).

## Câu hỏi trung tâm và hai ví dụ xuyên suốt

### Kết quả kế thừa (mở §1.1, GC-RL-2)

- Định lý 06.21: dưới các giả thiết nền của Nhận xét 06.20 (MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, mẫu theo $p(\cdot,\cdot\mid s,a)$), khi mọi cặp được cập nhật vô hạn lần và bước học thỏa Định nghĩa 06.19, Q-learning dạng bảng hội tụ hầu chắc chắn tới $q_*$; mỗi mẫu thật chỉ dùng cho một cập nhật.
- Định lý 04.32: lặp giá trị bất đồng bộ hội tụ tới $v_*$ khi biết mô hình và mọi trạng thái được cập nhật vô hạn lần, theo lịch tùy ý.

### Bài toán có số liệu (đoạn mở §1.1)

- Trên mê cung hai phòng, sau lượt thật thứ nhất $(\mathrm A,\rightarrow,0,\mathrm A)$, $(\mathrm A,\rightarrow,0,\mathrm B)$, $(\mathrm B,\downarrow,0,\mathrm F)$, $(\mathrm F,\rightarrow,0,\mathrm K)$, $(\mathrm K,\rightarrow,+1,\mathrm Z)$, Q-learning với bảng khởi tạo $0$, $\alpha=0{,}5$, $\gamma=0{,}9$ chỉ có một ô khác $0$: $Q(\mathrm K,\rightarrow)=0{,}5$. Bốn mẫu chuyển còn lại không được dùng thêm.
- Trên mê cung Dyna của SB (Ví dụ 8.1, tr. 164), tác tử không lập kế hoạch cần khoảng 25 lượt để đạt hiệu năng gần tối ưu, tác tử làm 50 cập nhật lập kế hoạch sau mỗi bước thật chỉ cần 3 lượt (một câu có nguồn).
- Mô hình học từ một lượt sai ở những chỗ khác nhau: $(\mathrm A,\rightarrow)$ mới được thử hai lần, một lần trượt; các cặp tại $\mathrm C$ chưa được thử lần nào.

### Câu hỏi trung tâm (chuỗi đến tay sinh viên; đã sửa bằng `no-ai-slop` Edit)

> Tác tử chỉ được đi ít bước thật, nhưng sau mỗi bước được tính thêm trên một mô hình học từ các bước đã đi. Dùng mô hình đó thế nào để chọn hành động tốt hơn phương pháp phi mô hình với cùng số bước thật, và sai số của mô hình làm mất những bảo đảm nào?

Câu hỏi đặt ở đoạn mở §1.1, sau đoạn bài toán có số liệu (VP-RL-2); trên deck là hộp "Câu hỏi:" của trang "Vấn đề trung tâm" (`L11-1-06`). Câu trả lời có điều kiện nằm ở §6.2 (bốn ý, mỗi ý có số hiệu và số liệu, theo mục 2 của `ke-hoach-ghi-chu.md`):

1. **Lập kế hoạch nền** (§2): Q-planning hội tụ tới $\hat q_*$ của mô hình khi mô hình cố định, xác định ở mọi cặp (Mệnh đề 11.9); Dyna-Q xen kẽ học mô hình với Q-planning, chương không phát biểu định lý hội tụ cho Dyna-Q (Nhận xét 11.11, quyết định Q-A); Dyna-Q dùng mỗi bước thật thêm $n$ lần, hai cập nhật lập kế hoạch sau lượt thứ nhất cho $Q(\mathrm F,\rightarrow)=0{,}225$ (Ví dụ 11.7); điều kiện: mô hình đúng trên các cặp được lấy mẫu; môi trường ngẫu nhiên cần mô hình đếm (Định nghĩa 11.4), môi trường thay đổi cần thưởng thăm dò (Định nghĩa 11.12); bất định nhận thức giảm theo $1/\sqrt{C(s,a)}$ (Mệnh đề 11.5).
2. **Lập kế hoạch tại thời điểm quyết định** (§3): với $q_{\pi_0}$ chính xác, rollout không làm giảm giá trị (Mệnh đề 11.21); tại $\mathrm F$, $v_{\pi_0}=0{,}2016$, chính sách rollout đạt $0{,}8566=v_*(\mathrm F)$; $m=70$ mô phỏng mỗi hành động đủ để xác suất chọn $\downarrow$ thay vì $\rightarrow$ không vượt $0{,}05$ (chặn $0{,}0496$, Mệnh đề 11.22); với bài toán cắt ở độ sâu $D=20$, phần thưởng trong $[0,1]$ và $c_{\mathrm{ucb}}=\sqrt2D$, xác suất UCT của Kocsis và Szepesvári chọn sai ở gốc tiến về $0$ khi số vòng lặp tăng (Kocsis và Szepesvári 2006, Định lý 6), còn sai số do cắt không vượt $\gamma^{20}=0{,}1216$ khi lợi tức trong $[0,1]$ (Định lý 11.27).
3. **Tối ưu kế hoạch bằng đạo hàm** (§4): một bước hạ gradient giảm chi phí của xe trên đường ray từ $8$ xuống $2{,}88$, nghiệm tối ưu $2{,}4$ (Ví dụ 11.18, 11.19); điều khiển dự báo với mô hình $a=1$ trên hệ thật $a=1{,}2$ vẫn co về $0$ với hệ số $0{,}6$ (Ví dụ 11.23), còn sai số dự báo vòng hở tăng theo $\bar e(L^k-1)/(L-1)$ (Mệnh đề 11.36).
4. **Tùy chọn** (§5): lặp giá trị với hai tùy chọn cho đúng $v_*(\mathrm A)=0{,}6604$ sau hai vòng, lặp giá trị trên hành động một bước sau sáu lượt quét mới cho $0{,}6103$ (Ví dụ 11.26); chỉ dùng tùy chọn thì giới hạn là $v_\Omega\le v_*$; thêm mọi hành động một bước vào $\Omega(s)$ thì $v_\Omega=v_*$ (Định lý 11.44).

### Ví dụ xuyên suốt thứ nhất: mê cung hai phòng (Ví dụ 11.1; §1–§3, §5, §6)

```
            cột 1   cột 2 ‖ cột 3   cột 4
hàng trên:    A       B   ‖   C       D
hàng dưới:    E       F       K       Z
```

- Tám ô; $\mathrm Z$ là ô đích, trạng thái kết thúc. Tường đứng giữa $\mathrm B$ và $\mathrm C$ (chỉ hàng trên); cửa giữa hai phòng là cạnh $\mathrm F$–$\mathrm K$. Phòng trái $\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$, phòng phải $\{\mathrm C,\mathrm D,\mathrm K\}$ cùng $\mathrm Z$. Lượt bắt đầu ở $\mathrm A$.
- $\mathcal A(s)=\{\uparrow,\downarrow,\leftarrow,\rightarrow\}$ tại mọi ô không kết thúc. Với xác suất $0{,}8$ tác tử sang ô kề theo hướng đã chọn (đụng tường hoặc biên thì ở yên); với xác suất $0{,}2$ tác tử trượt và ở yên. Phần thưởng $+1$ cho chuyển vào $\mathrm Z$, $0$ cho chuyển khác; $\gamma=0{,}9$.
- Khoảng cách tới đích $d$: $\mathrm K,\mathrm D$: $1$; $\mathrm F,\mathrm C$: $2$; $\mathrm B,\mathrm E$: $3$; $\mathrm A$: $4$. Giá trị tối ưu $v(1)=0{,}8/0{,}82$, $v(d)=(0{,}72/0{,}82)\,v(d-1)$:

| $s$ | $\mathrm K$, $\mathrm D$ | $\mathrm F$, $\mathrm C$ | $\mathrm B$, $\mathrm E$ | $\mathrm A$ |
|---|---:|---:|---:|---:|
| $v_*(s)$ | $0{,}975610$ | $0{,}856633$ | $0{,}752166$ | $0{,}660438$ |

- Lượt thật thứ nhất (năm mẫu chuyển ở trên) là dữ kiện "Giả sử" của Ví dụ 11.3, 11.7. Các dùng lại (mỗi lần trả lời một câu hỏi mới, GC-RL-11): mô hình phân phối và mô hình mẫu (Ví dụ 11.2); bảng đếm, hai loại bất định (11.3, 11.4); tập mô hình (11.5); Q-planning, Dyna-Q (11.6, 11.7); mê cung đổi cửa, Dyna-Q+ (11.8, 11.9); cập nhật kỳ vọng và mẫu (11.10); rollout với chính sách ngẫu nhiên đều (11.12–11.14); một vòng MCTS (11.16); hai tùy chọn, mô hình tùy chọn, lặp giá trị với tùy chọn, Q-learning bán-MDP (11.24–11.27); Tình huống 11.2; Bài tập 11.2–11.5, 11.7, 11.8, 11.10.

### Ví dụ xuyên suốt thứ hai: xe trên đường ray (Ví dụ 11.17; §4)

- Vị trí $x_t\in\mathbb R$ của xe trên đường ray thẳng, mốc $0$ là vị trí cần giữ; hành động $u_t\in\mathbb R$ là độ dịch chuyển lệnh cho bước $t$. Mô hình $\hat f(x,u)=x+u$; hệ thật ở §4.5 và Tình huống 11.1 là $f(x,u)=1{,}2x+u$. Chi phí mỗi bước $c(x_{t+1},u_t)=x_{t+1}^2+u_t^2$; chân trời $h=2$; không chiết khấu; $x_0=2$; $J(u_0,u_1)=x_1^2+u_0^2+x_2^2+u_1^2$ với $x_1=x_0+u_0$, $x_2=x_1+u_1$. Ghi chú nêu một câu: cực tiểu chi phí tương đương cực đại phần thưởng $-c$.
- Số liệu then chốt: $J(0,0)=8$; gradient tại $(0,0)$ bằng $(8,4)$ cả bằng khai triển lẫn truy hồi ngược ($\lambda_2=4$, $\lambda_1=8$); một bước $\eta=0{,}1$ cho $(-0{,}8;\,-0{,}4)$, $J=2{,}88$; tối ưu $(-1{,}2;\,-0{,}4)$, $J^*=2{,}40$, Hessian $\begin{pmatrix}6&2\\2&4\end{pmatrix}$; luật dự báo $u=-0{,}6x$; vòng kín trên mô hình $2;\ 0{,}8;\ 0{,}32;\ 0{,}128$; trên hệ thật $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$; vòng hở trên hệ thật $x_1=1{,}2$, $x_2=1{,}04$; sai số $e_k=2(1{,}2^k-1)$: $0{,}4;\ 0{,}88;\ 1{,}456;\ 2{,}1472;\ 2{,}97664$; bốn ứng viên bắn ngẫu nhiên $J=8;\ 3;\ 2{,}5;\ 4$, trung bình ưu tú $(-1;\,-0{,}25)$, độ lệch chuẩn $(0;\,0{,}25)$; luật với $\hat a=1{,}2$: $u=-0{,}758824x$, vòng kín $2;\ 0{,}882353;\ 0{,}389273;\ 0{,}171738$.
- Các dùng lại: 11.17–11.23, Tình huống 11.1, Bài tập 11.6, 11.11.

## Khung lý thuyết chung

**Bài toán trung tâm.** Tác tử có một mô hình của môi trường, cho sẵn hoặc học từ ít bước thật, và một ngân sách tính toán trên mô hình sau mỗi bước thật. Cần dùng ngân sách đó để chọn hành động tốt hơn phương pháp phi mô hình với cùng số bước thật, và biết bảo đảm nào còn đúng khi mô hình sai. Bốn cách dùng mô hình ứng với bốn mục nội dung: cập nhật bảng giá trị cho nhiều trạng thái trong lúc hành động (§2); tìm kiếm từ trạng thái hiện tại với hành động rời rạc (§3) hoặc hành động liên tục (§4); gộp nhiều bước thành tùy chọn để lập kế hoạch trên thang thời gian dài hơn (§5). Hình `cau-truc-chuong.svg` (§1.2) vẽ khung "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách" (SB §8.1, tr. 160) với ba nhánh.

**Đối tượng và ký hiệu chung** (bảng ký hiệu ở mục sau).

- MDP hữu hạn với động lực thật $p(s',r\mid s,a)$, $\gamma\in[0,1)$; mô hình học được $\hat p(s'\mid s,a)$, $\hat r(s,a)$; mô hình phân phối khác mô hình mẫu (Định nghĩa 11.1). Mọi bảo đảm của chương là bảo đảm **trên mô hình**: chúng nói về $\hat q_*$, $\hat v$ của MDP mà mô hình định nghĩa; khoảng cách tới $q_*$, $v_*$ là phần sai số mô hình.
- §4 đổi sang trạng thái và hành động liên tục $x_t,u_t\in\mathbb R$, mô hình tất định khả vi $\hat f$, chi phí $c\ge0$ (cực tiểu chi phí là cực đại phần thưởng $-c$), chân trời $h$, không chiết khấu.
- §5 thêm tùy chọn $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$, thời điểm kết thúc $\tau$, mô hình tùy chọn $r(s,\omega)$, $p(s'\mid s,\omega)$ với chiết khấu nằm trong $p$.

**Giả thiết chung.** (M1) MDP hữu hạn, trạng thái quan sát được và có tính Markov, động lực dừng; (M2) phần thưởng bị chặn, $0\le\gamma<1$ (§2, §3, §5); (M3) mô hình cố định trong lúc lập kế hoạch; (M4) mô hình đúng trên những cặp mà kế hoạch đi qua. Từng kết quả nói rõ giả thiết nào nó dùng; (M4) là giả thiết bị vi phạm trong Tình huống 11.2.

**Chuỗi định nghĩa → kết quả → phương pháp.** Mô hình phân phối, mô hình mẫu, lập kế hoạch nền và tại thời điểm quyết định (Định nghĩa 11.1, 11.2) → mô hình đếm (Định nghĩa 11.4), kỳ vọng và phương sai của xác suất ước lượng (Mệnh đề 11.5), hai loại bất định (Định nghĩa 11.6) → Q-planning (Thuật toán 11.8), hội tụ tới $\hat q_*$ (Mệnh đề 11.9) → Dyna-Q (Thuật toán 11.10) → thưởng thăm dò của Dyna-Q+ (Định nghĩa 11.12) → cập nhật kỳ vọng và cập nhật mẫu (Định nghĩa 11.14, Mệnh đề 11.15) → thuật toán rollout (Thuật toán 11.20), cải thiện chính sách (Mệnh đề 11.21), số mô phỏng (Mệnh đề 11.22) → quy tắc cận tin cậy trên (Định nghĩa 11.23) và bảo đảm của UCB1 (Định lý 11.24) → MCTS với UCT (Định nghĩa 11.25, Thuật toán 11.26), tính nhất quán cho bài toán cắt (Định lý 11.27) → bài toán tối ưu kế hoạch (Định nghĩa 11.29), gradient bằng truy hồi ngược (Mệnh đề 11.30), hạ gradient (Thuật toán 11.31) → điều khiển dự báo (Định nghĩa 11.32, Thuật toán 11.33) → phương pháp entropy chéo (Thuật toán 11.34) → sai số dự báo tích lũy (Mệnh đề 11.36) → tùy chọn, chính sách phân cấp (Định nghĩa 11.38, 11.39) → mô hình tùy chọn (Định nghĩa 11.40, Mệnh đề 11.41) → phương trình Bellman phân cấp (Định lý 11.42) → hội tụ của lặp giá trị với tùy chọn (Định lý 11.44, Thuật toán 11.45) → Q-learning bán-MDP (Thuật toán 11.46).

**Giới hạn áp dụng** (nguồn của "Giả thiết hay bị bỏ quên" trong Tóm tắt chương).

- Mệnh đề 11.9 nói về $\hat q_*$ của mô hình cố định, xác định ở mọi cặp; Dyna-Q chỉ lập kế hoạch trên cặp đã thử và mô hình còn đổi sau mỗi bước thật, nên chương không phát biểu giới hạn hay định lý hội tụ cho Dyna-Q; Dyna-Q dạng hộp của SB giả thiết môi trường tất định.
- Thưởng thăm dò làm bảng không còn ước lượng $\hat q_*$.
- Mệnh đề 11.21 cần $q_{\pi_0}$ chính xác; Mệnh đề 11.22 cần $m$ chọn trước và mô phỏng độc lập.
- Định lý 11.24 cần phần thưởng trong $[0,1]$, độc lập, phân phối của mỗi hành động không đổi, điều không đúng ở các nút trong của cây; Định lý 11.27(a) phát biểu cho UCT của Kocsis và Szepesvári (chỉ số ở mọi nút tới độ sâu $D$, $c_{\mathrm{ucb}}=\sqrt2D$, phần thưởng trong $[0,1]$, hành động tối ưu duy nhất ở gốc; Kocsis và Szepesvári 2006, Định lý 6), không cho Thuật toán 11.26, và chỉ có kết luận định tính; Định lý 11.27(b) chặn sai số cắt bởi $\gamma^{20}=0{,}121577$ khi lợi tức trong $[0,1]$.
- Mệnh đề 11.30 cho gradient trên mô hình, điểm dừng có thể là cực tiểu địa phương khi $\hat f$ phi tuyến; Mệnh đề 11.36 chỉ cho chuỗi hành động cố định (vòng hở), sai số một bước đo trên quỹ đạo dự báo.
- Định lý 11.42, 11.44 cần tùy chọn kết thúc với xác suất $1$ và kết thúc chỉ phụ thuộc trạng thái; $v_\Omega=v_*$ chỉ khi $\Omega(s)\supseteq\mathcal A(s)$.
- Phạm vi của chương: mô hình là bảng hoặc hàm tường minh của trạng thái quan sát được (nêu trong "Phạm vi." của các kết quả, không trỏ tới chương sau).

## Mục tiêu học tập (chuỗi đến tay sinh viên; đã sửa bằng `no-ai-slop` Edit)

Sau chương này, người học có thể:

1. **Mô hình và tính bất định.** Phân biệt mô hình phân phối với mô hình mẫu, lập kế hoạch nền với lập kế hoạch tại thời điểm quyết định; ước lượng mô hình bằng tần suất từ dữ liệu, tách bất định ngẫu nhiên khỏi bất định nhận thức và tính độ lệch chuẩn của xác suất ước lượng (Mục 2).
2. **Dyna.** Thực hiện bằng tay một bước thật của Dyna-Q gồm cập nhật trực tiếp, cập nhật mô hình và các cập nhật lập kế hoạch; nêu điều kiện hội tụ của Q-planning; giải thích vì sao mô hình sai cần thưởng thăm dò (Mục 2).
3. **Cập nhật kỳ vọng và cập nhật mẫu.** So sánh hai loại cập nhật theo số phép tính và sai số khi ngân sách tính toán nhỏ hơn hệ số phân nhánh (Mục 2).
4. **Rollout và tìm kiếm theo cây.** Phát biểu tính chất cải thiện của thuật toán rollout cùng giả thiết; tính số mô phỏng đủ cho một xác suất chọn sai cho trước; tính chỉ số cận tin cậy trên; thực hiện một vòng tìm kiếm theo cây Monte Carlo qua bốn pha (Mục 3).
5. **Tối ưu kế hoạch bằng đạo hàm.** Tính gradient của chi phí kế hoạch theo chuỗi hành động qua mô hình khả vi bằng truy hồi ngược; thực hiện một bước hạ gradient và một vòng phương pháp entropy chéo; mô tả điều khiển dự báo theo chân trời lùi và chặn sai số dự báo tích lũy (Mục 4).
6. **Tùy chọn.** Định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của một tùy chọn; viết phương trình Bellman bán-MDP; thực hiện lặp giá trị và một cập nhật Q-learning với tùy chọn (Mục 5).
7. **Chọn cách dùng mô hình.** Với một bài toán cụ thể, chọn cách dùng mô hình phù hợp và kiểm các giả thiết mà bảo đảm của cách đó cần (Mục 6, Tình huống áp dụng).

Sửa so với kế hoạch (chỉ câu chữ): mục tiêu 4 thêm "cho trước" sau "xác suất chọn sai" để đối tượng tính đủ nghĩa. Câu cuối mỗi mục tiêu có thể kèm danh sách bài tập như ghi chú 06 ("(Bài tập 11.1, 11.2, 11.10, 11.17)"), theo bảng phủ ở mục "Bài tập củng cố" dưới đây.

## Kiến thức tiên quyết (số hiệu đã kiểm bằng grep, 2026-11-19)

Mọi số hiệu dưới đây đã đối chiếu với dòng `::: definition|theorem|proposition|lemma|corollary|remark|algorithm …` của ghi chú 01, 03–06, 08, 10 trong `2627-1/materials/lec-NN/lecture-note.md`. Câu quy ước đầu mục của ghi chú: "Số hiệu `01.k`, …, `10.k` chỉ khối trong ghi chú Bài 01–10; `11.k` chỉ ghi chú này. Bài tập 11.12–11.19 thuộc tệp bài tập `exercises.md` của Bài 11." Mỗi gạch đầu dòng: tên nhóm in đậm, số hiệu, rồi phát biểu lại trong một đến hai câu (tác tử soạn chép đúng nghĩa của khối gốc). Chú thích `<!-- note-topic-id: lec-11-topic-01 -->` đặt trước `## Kiến thức tiên quyết`, như ghi chú 10.

| # | Nhóm (tên in đậm) | Số hiệu đã kiểm (tên khối trong ghi chú gốc) | Phát biểu lại một câu | Dùng ở |
|---|---|---|---|---|
| 1 | Mô hình, lập kế hoạch, thăm dò | Định nghĩa 01.14 (Mô hình, lập kế hoạch, có mô hình và phi mô hình); Định nghĩa 01.16 (Hành động tham lam, khai thác, thăm dò) | Mô hình cho dự báo $(\widehat S_{t+1},\widehat R_{t+1})$ hoặc phân phối của chúng khi biết trạng thái và hành động; lập kế hoạch là dùng mô hình để chọn hành động bằng cách xét diễn biến tương lai trước khi chúng xảy ra. Khi chọn lặp lại trong một tập hữu hạn hành động, $N(a)$ là số lần chọn $a$, $\bar r(a)$ là trung bình mẫu phần thưởng; thăm dò là chọn hành động không tham lam theo $\bar r$. | §1.2, §2.1, §3.2 |
| 2 | MDP hữu hạn, động lực, giá trị | Định nghĩa 03.4 (Hàm động lực), 03.7 (Quá trình quyết định Markov hữu hạn), 03.9 (Lợi tức chiết khấu), 03.13 (Chính sách Markov dừng); Mệnh đề 03.6 (Xác suất chuyển và thưởng kỳ vọng từ hàm động lực), 03.22 (Giá trị hành động theo giá trị trạng thái); Bổ đề 03.20 (Tính Markov của phần tương lai); Định lý 03.21 (Phương trình Bellman kỳ vọng cho $v_\pi$), 03.28 (Nghiệm duy nhất của hệ đánh giá chính sách) | $p(s',r\mid s,a)$ cho $p(s'\mid s,a)$ và $r(s,a)$; $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$; với chính sách Markov dừng, phần tương lai của lượt khi biết lịch sử tới $s$ có cùng phân phối với quá trình xuất phát tại $s$; $v_\pi$ thỏa phương trình Bellman kỳ vọng, và với $0\le\gamma<1$ hệ đánh giá chính sách có nghiệm duy nhất. | Ví dụ 11.12 (giải hệ bảy phương trình), Định lý 11.42 (bước 3 và điều kiện áp dụng) |
| 3 | Toán tử Bellman và ánh xạ co | Định nghĩa 04.1 (Toán tử Bellman đánh giá, lượt quét đồng bộ), 04.22 (Toán tử Bellman tối ưu, phần dư tối ưu); Bổ đề 04.23 (Cực đại không làm tăng chênh lệch); Mệnh đề 04.4 ($T_\pi$ là ánh xạ co), 04.24 ($T_*$ là ánh xạ co); Định lý 04.5 (Điểm bất động của ánh xạ co trên $\mathbb R^n$), 04.25 (Tồn tại chính sách tối ưu Markov dừng, xác định) | $\lvert\max_ax_a-\max_ay_a\rvert\le\max_a\lvert x_a-y_a\rvert$; ánh xạ co hệ số $\beta<1$ theo chuẩn vô cùng có điểm bất động duy nhất và $\lVert V_k-\bar V\rVert_\infty\le\beta^k\lVert V_0-\bar V\rVert_\infty$; $v_*$ là điểm bất động duy nhất của $T_*$ và chính sách tham lam theo $v_*$ là tối ưu. | Ví dụ 11.1 (kiểm $v_*$), Định lý 11.44 (a), (b) |
| 4 | Cải thiện chính sách | Định lý 04.13 (Cải thiện chính sách) | Nếu $\pi$ Markov dừng có giá trị chính xác $v_\pi$ và $\pi'$ Markov dừng xác định thỏa $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$ thì $v_{\pi'}\ge v_\pi$, nghiêm ngặt tại $s$ khi điều kiện nghiêm ngặt tại $s$. | Mệnh đề 11.21 |
| 5 | Lặp giá trị đồng bộ và bất đồng bộ | Thuật toán 04.28 (Lặp giá trị đồng bộ có kiểm tra dừng), 04.31 (Lặp giá trị bất đồng bộ); Định lý 04.32 (Hội tụ của lặp giá trị bất đồng bộ) | Lặp giá trị cần mô hình phân phối đã biết; bản bất đồng bộ cập nhật từng trạng thái theo lịch tùy ý, mỗi trạng thái vô hạn lần, và hội tụ về $v_*$. | Nhận xét 11.3, 11.17, Thuật toán 11.45, Ví dụ 11.26 |
| 6 | Trung bình mẫu, mô hình thực nghiệm | Định nghĩa 05.8 (Ước lượng Monte Carlo); Mệnh đề 05.9 (Trung bình gia tăng), 05.34 (Nghiệm TD theo lô) | $V_n=V_{n-1}+(g_n-V_{n-1})/n$; nghiệm TD theo lô là nghiệm của MDP thực nghiệm với $\hat r(s)$ và $\hat P(s'\mid s)$ là tần suất tính từ dữ liệu (Bài 05 viết bộ đếm là $N(s)$). | Định nghĩa 11.4, Mệnh đề 11.15, §3.3 |
| 7 | Q-learning và hội tụ | Định nghĩa 06.3 (Chính sách $\varepsilon$-tham lam), 06.15 (Mục tiêu Q-learning), 06.19 (Điều kiện Robbins–Monro theo cặp); Thuật toán 06.16 (Q-learning dạng bảng); Nhận xét 06.20 (Giả thiết nền và vị trí của dãy năm ô); Định lý 06.21 (Hội tụ của Q-learning dạng bảng) | Mục tiêu $R+\gamma\max_{a'}Q(S',a')$ (bằng $R$ khi $S'$ kết thúc); dưới các giả thiết nền (MDP hữu hạn, động lực dừng, phần thưởng bị chặn, $0\le\gamma<1$, mẫu theo $p(\cdot,\cdot\mid s,a)$), mọi cặp cập nhật vô hạn lần và bước học thỏa Robbins–Monro theo cặp thì $Q_t\to q_*$ hầu chắc chắn. | §1.1, Thuật toán 11.8, Mệnh đề 11.9, Thuật toán 11.10, 11.46 |
| 8 | Bất đẳng thức Hoeffding | Mệnh đề 06.26 (Chặn Hoeffding cho đánh giá một chính sách cố định); Hoeffding (1963), không ghi số định lý, số trang (chưa kiểm trên bản gốc, Đ1) | Mệnh đề 06.26 chỉ có dạng hai phía cho trung bình lợi tức cùng phân phối; ghi chú phát biểu lại đầy đủ dạng một phía cho tổng biến độc lập không cùng phân phối: nếu $X_i\in[a_i,b_i]$ độc lập thì $\Pr\{\sum_iX_i-\mathbb E\sum_iX_i\le-t\}\le\exp\bigl(-2t^2/\sum_i(b_i-a_i)^2\bigr)$ (GC3). | Mệnh đề 11.22, Bài tập 11.8 |
| 9 | Bộ nhớ phát lại, hạ gradient | Định nghĩa 08.7 (Bộ nhớ phát lại), 08.15 (Bộ tối ưu theo gradient), 08.16 (Hạ gradient ngẫu nhiên) | Bộ nhớ phát lại giữ $N$ mẫu chuyển gần nhất và rút đều; hạ gradient với tốc độ học $\eta>0$ cập nhật $\theta\leftarrow\theta-\eta g$. | Nhận xét 11.11, Thuật toán 11.31 |
| 10 | Đoạn thu, lợi tức $n$ bước | Định nghĩa 10.11 (Lợi tức $n$ bước, lợi thế $n$ bước); "đoạn thu (rollout)" ở §3.3 "GAE trên đoạn thu" của ghi chú 10 (văn xuôi trước Thuật toán 10.16, không phải khối riêng) | Đoạn thu của Bài 10 là đoạn dữ liệu độ dài $h$ thu theo chính sách hiện hành, khác "thuật toán rollout" của chương này; lợi tức $n$ bước dùng $n$ phần thưởng thật rồi bootstrap từ giá trị ước lượng. | Thuật toán 11.20 (câu phân biệt thuật ngữ, Q6); Bài tập 11.16 của `exercises.md` |
| 11 | Giải tích và xác suất (kiến thức đại học, GC-RL-16) | — | Quy tắc dây chuyền; phân phối nhị thức, phương sai của trung bình mẫu độc lập; bất đẳng thức hợp (union bound); chuỗi hình học. | Mệnh đề 11.5, 11.15, 11.30, Ví dụ 11.25 |

**Công cụ của Chương 4 giáo trình, phát biểu lại trong bài** (không có trong Bài 01–10; nhóm `cầu nối`, Q3). Đoạn ngay sau danh sách tiên quyết nêu tên ba công cụ để sinh viên biết chúng được trình bày đầy đủ trong chương (một câu, không trỏ số mục, VP20):

| Công cụ | Giáo trình (mục lục) | Khối trong ghi chú này | Nguồn nội dung |
|---|---|---|---|
| Thuật toán rollout, chính sách cơ sở, chính sách rollout | 4.3.1 | Thuật toán 11.20, Mệnh đề 11.21, 11.22 | SB §8.10, tr. 183–185; Bertsekas (2019), §2.4 (Rollout and the Policy Improvement Principle) và §5.1.2 (Rollout); Bertsekas (2020), Mệnh đề 5.4.2 |
| Quy tắc cận tin cậy trên, UCB1, chặn hối tiếc | 4.7.1–4.7.2 | Định nghĩa 11.23, Định lý 11.24 | SB §2.7, tr. 35–36, tên UCB1 ở ghi chú lịch sử tr. 44; Auer, Cesa-Bianchi và Fischer (2002), Hình 1 (tr. 237) và Định lý 1 (tr. 237); Szepesvári (2010), §4.2.1 (Online learning in bandits) |
| Điều khiển dự báo theo chân trời lùi | 4.3.2 | Định nghĩa 11.32, Thuật toán 11.33 | Bertsekas (2019), §2.5.1 (Model Predictive Control); nội dung kiểm trên Bertsekas (2020), §3.1 |

**Thay đổi so với mục 4 của `ke-hoach-ghi-chu.md`** (đều là bổ sung số hiệu đã tồn tại, xem mục "Sai khác so với kế hoạch"): thêm Định nghĩa 03.13 và Định lý 03.21 vào nhóm 2 (Định lý 11.42 dẫn 03.21 ở "Điều kiện áp dụng"); thêm Bổ đề 04.23 vào nhóm 3 (dùng trong chứng minh Định lý 11.44); thêm Thuật toán 04.28 vào nhóm 5 (Nhận xét 11.3, Thuật toán 11.45, Bài tập 11.1); thêm nhóm 10 (Bài 10). Ghi chú: Mệnh đề 04.24 giả thiết trọng số của mô hình có tổng bằng $1$, nên không áp dụng nguyên văn cho mô hình tùy chọn (tổng $\le\gamma$); chứng minh Định lý 11.44(a) dùng Bổ đề 04.23 và Mệnh đề 11.41, không dẫn 04.24.

## Bảng ký hiệu dự kiến (24 dòng; GC-RL-6, VP-RL-5)

Câu dẫn của ghi chú: bảng gồm ký hiệu dùng xuyên suốt chương; mỗi chữ giữ một nghĩa trong cả chương; ký hiệu cục bộ giới thiệu tại chỗ.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái không kết thúc; thêm trạng thái kết thúc | tập hữu hạn (§1–§3, §5) |
| $\mathcal A(s)$ | tập hành động hợp lệ tại $s$ | tập hữu hạn khác rỗng |
| $t$, $T$ | chỉ số bước; thời điểm kết thúc lượt | $\{0,1,\dots\}$; nguyên dương hoặc $\infty$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động, phần thưởng của chuyển từ $t$ sang $t+1$ | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathbb R$ |
| $p(s',r\mid s,a)$; $p(s'\mid s,a)$, $r(s,a)$ | động lực thật; xác suất chuyển, phần thưởng kỳ vọng | phân phối; $[0,1]$; $\mathbb R$ |
| $\hat p(s'\mid s,a)$, $\hat r(s,a)$ | mô hình học được (mô hình đếm ở §2) | phân phối trên $\mathcal S^+$; $\mathbb R$ |
| $C(s,a)$, $C(s,a,s')$ | số lần thử thật cặp $(s,a)$; số lần trong đó đi tới $s'$ | $\{0,1,\dots\}$ |
| $\gamma$ | hệ số chiết khấu | $[0,1)$ |
| $\pi$, $\pi_0$ | chính sách; chính sách cơ sở của rollout | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $v_\pi$, $q_\pi$, $v_*$, $q_*$ | giá trị thật của $\pi$; giá trị tối ưu | hàm thực |
| $Q$ | bảng giá trị hành động đang học hoặc đang lập kế hoạch | $\mathbb R$ trên mỗi cặp hợp lệ |
| $\alpha$, $\varepsilon$ | bước học; tham số của chính sách $\varepsilon$-tham lam | $(0,1]$; $[0,1]$ |
| $n$ | số cập nhật lập kế hoạch sau mỗi bước thật | số nguyên không âm |
| $\kappa$, $\ell(s,a)$ | hệ số thưởng thăm dò; số bước thật kể từ lần thử gần nhất của $(s,a)$ | $\kappa>0$; $\{0,1,\dots\}$ |
| $b$ | hệ số phân nhánh: số trạng thái kế có xác suất dương | số nguyên dương |
| $m$ | số mô phỏng cho mỗi hành động của thuật toán rollout | số nguyên dương |
| $N(s)$, $N(s,a)$, $W(s,a)$, $\bar Q(s,a)$ | số lần thăm nút, cạnh trên cây; tổng lợi tức; trung bình $W/N$ | $\{0,1,\dots\}$; $\mathbb R$ |
| $c_{\mathrm{ucb}}$, $D$ | hằng số thăm dò của quy tắc cận tin cậy trên; độ sâu cắt của MCTS | $c_{\mathrm{ucb}}>0$; nguyên dương |
| $x_t$, $u_t$; $f$, $\hat f$ | trạng thái, hành động liên tục của §4; động lực thật, mô hình | $\mathbb R$; $\mathbb R\times\mathbb R\to\mathbb R$ |
| $h$, $c(x,u)$, $J$ | chân trời; chi phí mỗi bước; chi phí của một kế hoạch | nguyên dương; $\mathbb R_{\ge0}$; $\mathbb R^h\to\mathbb R$ |
| $\eta$; $\bar e$, $e_k$, $L$ | tốc độ học; chặn sai số một bước của mô hình, sai số dự báo $k$ bước, hằng số Lipschitz | dương; $\mathbb R_{\ge0}$; $L\ge0$ |
| $\omega$, $\Omega(s)$; $\mathcal I_\omega$, $\pi_\omega$, $\beta_\omega$ | tùy chọn, tập tùy chọn dùng được tại $s$; tập khởi đầu, chính sách, hàm kết thúc | $\mathcal I_\omega\subseteq\mathcal S$; $\beta_\omega:\mathcal S^+\to[0,1]$ |
| $\tau$; $r(s,\omega)$, $p(s'\mid s,\omega)$ | thời điểm kết thúc của tùy chọn; hai phần của mô hình tùy chọn | $\{1,2,\dots\}$; $\mathbb R$; $[0,\gamma]$ |
| $\mu$, $v_\mu$, $v_\Omega$ | chính sách phân cấp; giá trị của nó; giá trị tối ưu trên tập tùy chọn | phân phối trên $\Omega(s)$; hàm thực |

Dòng $c_{\mathrm{ucb}}$ thêm $D$ (độ sâu cắt, Q9); kế hoạch không có $D$ trong bảng. Đoạn quy ước sau bảng (GC-RL-6): $R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$; giá trị của trạng thái kết thúc bằng $0$ trong hàm thật, bảng và mô hình; $\mathbb E_\pi$ lấy theo chính sách và động lực thật, $\hat{\mathbb E}$ theo mô hình; bất đẳng thức giữa hai hàm hiểu theo từng trạng thái; $k$, $j$ là chỉ số cục bộ, nghĩa nêu tại chỗ; tên ô viết chữ đứng ($\mathrm A$, …, $\mathrm Z$), hành động của mê cung viết bằng mũi tên; dấu phẩy thập phân (VP-RL-6). Tương ứng với *Học máy thống kê* nêu một lần: $v_\pi$ ứng với $V^\pi$, $p(s'\mid s,a)$ ứng với $T(s,a,s')$.

### Quyết định ký hiệu (Q6)

- $c_{\mathrm{ucb}}$ cho hằng số của quy tắc cận tin cậy trên (SB (2.10) viết $c$), vì $c$ dành cho chi phí mỗi bước (VP-RL-5).
- $\ell(s,a)$ cho số bước kể từ lần thử gần nhất trong Dyna-Q+ (SB tr. 168 viết $\tau$), vì $\tau$ chỉ thời điểm kết thúc của tùy chọn.
- $C(s,a)$, $C(s,a,s')$ cho bộ đếm của mô hình, vì $N(s,a)$ chỉ số lần thăm trên cây tìm kiếm; $N(a)$ của bài toán chọn lặp lại giữ như Định nghĩa 01.16.
- $h$ cho chân trời (như SB (7.13)); $H_t$ giữ nghĩa lịch sử.
- $x_t$, $u_t$ cho trạng thái và hành động liên tục của §4, tách khỏi $S_t$, $A_t$ của MDP hữu hạn.
- $\beta_\omega$ là xác suất **kết thúc**, kèm tập khởi đầu $\mathcal I_\omega$ theo Sutton, Precup và Singh (1999); SB §17.2 (tr. 461–462) viết tùy chọn $\langle\pi_\omega,\gamma_\omega\rangle$ và **gọi** $\gamma_\omega$ là hàm kết thúc (termination function), dù tùy chọn kết thúc với xác suất $1-\gamma_\omega$; câu tương ứng sau bảng: "Sutton và Barto gọi $\gamma_\omega$ là hàm kết thúc; tùy chọn kết thúc với xác suất $1-\gamma_\omega$, nên $\beta_\omega=1-\gamma_\omega$."
- Tên hai tùy chọn: ghi chú dùng $\omega_1$ (đi tới cửa) và $\omega_2$ (đi tới đích), gọi tên bằng lời (Q6; NT26 cấm `\text{}` tiếng Việt); không dùng chỉ số có dấu trong `\mathrm{}`.
- Nhãn công thức theo số mục như ghi chú 04 (quyết định Q-C): `\tag{2.1}`–`\tag{2.5}` (mô hình đếm; kỳ vọng và phương sai của $\hat p$; cập nhật kỳ vọng; cập nhật mẫu; sai số $\sqrt{(b-1)/(bk)}$), `\tag{3.1}`–`\tag{3.3}` (chặn chọn sai của rollout; quy tắc cận tin cậy trên; chỉ số UCT), `\tag{4.1}`–`\tag{4.4}` (bài toán tối ưu kế hoạch; hai công thức truy hồi ngược; chặn sai số dự báo), `\tag{5.1}`–`\tag{5.3}` (mô hình tùy chọn; phương trình Bellman phân cấp; cập nhật Q-learning bán-MDP); không dùng dạng (11.k), trùng dạng số hiệu khối. Trang chiếu không dùng `\tag` (NT26).
- $\pi_0$ là **chính sách cơ sở**, $\pi_{\mathrm{ro}}$ là **chính sách rollout** (theo Bertsekas và mục lục giáo trình 4.3.1); tương ứng với SB nêu một lần: SB gọi $\pi_0$ là "rollout policy" (Q6).
- $\hat p$ cho mọi mô hình học được; $\hat q_*$ cho giá trị hành động tối ưu của MDP mà mô hình định nghĩa; $\hat f$ cho mô hình liên tục.
- $D$ cho độ sâu cắt của MCTS (Q9), không trùng ký hiệu nào khác của chương.
- $k$ và $j$ là chỉ số cục bộ, giới thiệu tại chỗ: số cập nhật mẫu ở §2.6, số bước dự báo ở §4.5, số bước thật của một tùy chọn ở §5.3, chỉ số lặp trong thuật toán; đoạn quy ước sau bảng ghi một câu như vậy (phân tích nguồn, phát hiện nhẹ).
- Chữ $C_t$ (tín hiệu tích lũy của hàm giá trị tổng quát ở SB §17.1) không dùng, vì $C$ đã là bộ đếm của mô hình; ý đó nói bằng lời ở Nhận xét 11.47.
- Hệ số phân nhánh $b$ chỉ dùng ở §2.6; Bài 08 dùng $b$ cho cỡ mini-batch, nhưng nghĩa đó không xuất hiện trong chương.

## Cấu trúc chương, mạch và `note-topic-id` (GC-RL-1, GC-RL-12)

Tiêu đề là cụm danh từ (VP7), không "Nhu cầu" (GC-RL-17); chú thích `<!-- note-topic-id: … -->` đặt ngay trước tiêu đề `###` (hoặc `##` với phần không có tiểu mục), như ghi chú 10. Hai mươi tám mã, mỗi mã một lần, `lec-11-topic-01` … `lec-11-topic-28`.

| Phần ghi chú | Tiêu đề (chuỗi đến tay sinh viên) | `note-topic-id` | Mạch deck |
|---|---|---|---|
| Tiêu đề | `# Bài 11 — Lập kế hoạch dựa trên mô hình` | — | — |
| Giới thiệu | bỏ (GC-RL-1 cho phép) | — | — |
| Mục tiêu | `## Mục tiêu học tập` | — | 1 |
| Tiên quyết | `## Kiến thức tiên quyết` | `lec-11-topic-01` | 1 |
| Ký hiệu | `## Bảng ký hiệu` | (thuộc `topic-01`) | 1 |
| §1 | `## 1. Bài toán lập kế hoạch với mô hình học được` | — | 1 Mở đầu |
| 1.1 | `### 1.1 Kết quả kế thừa và bài toán trung tâm` | `lec-11-topic-02` | 1 |
| 1.2 | `### 1.2 Ba cách dùng mô hình` | `lec-11-topic-03` | 1 |
| §2 | `## 2. Tính bất định của môi trường và lập kế hoạch nền` | — | 2 |
| 2.1 | `### 2.1 Mô hình phân phối và mô hình mẫu` | `lec-11-topic-04` | 2 |
| 2.2 | `### 2.2 Mô hình đếm và hai loại bất định` | `lec-11-topic-05` | 2 |
| 2.3 | `### 2.3 Tập mô hình` | `lec-11-topic-06` | 2 |
| 2.4 | `### 2.4 Q-planning và kiến trúc Dyna` | `lec-11-topic-07` | 2 |
| 2.5 | `### 2.5 Mô hình sai và thưởng thăm dò` | `lec-11-topic-08` | 2 |
| 2.6 | `### 2.6 Cập nhật kỳ vọng và cập nhật mẫu` | `lec-11-topic-09` | 2 |
| 2.7 | `### 2.7 Đọc thêm: phân bổ các cập nhật` | `lec-11-topic-10` | 2 (chỉ ghi chú diễn giả) |
| §3 | `## 3. Tìm kiếm theo cây Monte Carlo` | — | 3 |
| 3.1 | `### 3.1 Lập kế hoạch tại thời điểm quyết định và thuật toán rollout` | `lec-11-topic-11` | 3 |
| 3.2 | `### 3.2 Chọn hành động theo cận tin cậy trên` | `lec-11-topic-12` | 3 |
| 3.3 | `### 3.3 Bốn pha của tìm kiếm theo cây Monte Carlo` | `lec-11-topic-13` | 3 |
| 3.4 | `### 3.4 Bảo đảm của UCT và giá trị học được` | `lec-11-topic-14` | 3 |
| §4 | `## 4. Tối ưu kế hoạch dựa trên đạo hàm` | — | 4 |
| 4.1 | `### 4.1 Bài toán tối ưu kế hoạch trên mô hình khả vi` | `lec-11-topic-15` | 4 |
| 4.2 | `### 4.2 Đạo hàm qua mô hình` | `lec-11-topic-16` | 4 |
| 4.3 | `### 4.3 Điều khiển dự báo theo chân trời lùi` | `lec-11-topic-17` | 4 |
| 4.4 | `### 4.4 Bắn ngẫu nhiên và phương pháp entropy chéo` | `lec-11-topic-18` | 4 |
| 4.5 | `### 4.5 Sai số mô hình tích lũy` | `lec-11-topic-19` | 4 |
| §5 | `## 5. Học tăng cường phân cấp` | — | 5 |
| 5.1 | `### 5.1 Tùy chọn và chính sách phân cấp` | `lec-11-topic-20` | 5 |
| 5.2 | `### 5.2 Mô hình tùy chọn và bán-MDP` | `lec-11-topic-21` | 5 |
| 5.3 | `### 5.3 Lập kế hoạch ở nhiều mức trừu tượng thời gian` | `lec-11-topic-22` | 5 |
| 5.4 | `### 5.4 Đọc thêm: học mô hình tùy chọn` | `lec-11-topic-23` | 5 (chỉ ghi chú diễn giả) |
| §6 | `## 6. Tổng kết` với `### 6.1 So sánh bốn cách dùng mô hình`, `### 6.2 Trả lời bài toán trung tâm`, `### 6.3 Câu hỏi tự kiểm tra` | `lec-11-topic-24` (trước `## 6.`) | 6 Tổng kết |
| Tình huống | `## Tình huống áp dụng và ứng dụng` | `lec-11-topic-25` | 6 |
| Tóm tắt | `## Tóm tắt chương` | `lec-11-topic-26` | 6 |
| Bài tập | `## Bài tập củng cố` | `lec-11-topic-27` | 6 (trang "Bài tập về nhà") |
| Tham khảo | `## Hướng dẫn đọc thêm và tài liệu tham khảo` | `lec-11-topic-28` | 6 (trang "Tài liệu tham khảo") |

Tên mạch trên deck (ke-hoach-trang-chieu.md mục 1) trùng tên mục ghi chú, trừ mạch 2 "Tính bất định và lập kế hoạch nền" (ghi chú: "Tính bất định của môi trường và lập kế hoạch nền", theo mục lục 11.1); xem Đ7.

## Kế hoạch từng mục

Quy ước: mỗi tiểu mục có khái niệm mới có đoạn "Một cách trực quan" 3–5 câu (quyết định Q-K, kể cả §2.6, §3.4, §4.1–4.5, §5.2); mỗi khái niệm trọng tâm theo GC18 (bài toán → "Một cách trực quan" → định nghĩa → kết quả hoặc thuật toán → chứng minh → ví dụ → nhận xét); mỗi thuật toán có một lượt tính tay với giá trị khởi tạo đứng trước khối `algorithm` và hai bản cho cùng kết quả (GC-RL-11). Kết quả theo bốn phần **Giả thiết.**, **Kết luận.**, **Điều kiện áp dụng.**, **Phạm vi.** (GC-RL-7, GC21); thuật toán ghi đầu vào, đầu ra, giả thiết, khởi tạo, tham số, bước đánh số, điều kiện dừng, chi phí mỗi bước. Mức chứng minh: **đầy đủ** (khối `proof` chia bước, GC22), **phác thảo** (một đoạn ý tưởng, không khối `proof` đầy đủ), **dẫn nguồn** (phát biểu kèm nguồn cụ thể, không chứng minh). Một bộ đếm chung cho Định nghĩa/Định lý/Mệnh đề/Bổ đề/Hệ quả/Nhận xét/Thuật toán (11.1–11.47); Ví dụ đếm riêng (11.1–11.27); Bài tập đếm riêng (11.1–11.19, gồm `exercises.md`); Tình huống đếm riêng. Câu hỏi nghiên cứu "**Câu hỏi.**" theo VP-RL-2: đặt sau đoạn bài toán và được trả lời trong cùng tiểu mục. Kết mục theo GC15, GC-RL-2: câu nối chỉ ở phía kết mục; mục sau mở thẳng bằng bài toán trên ví dụ xuyên suốt. "Trong thực hành." sau mỗi kết quả chính (GC-RL-9).

### §1. Bài toán lập kế hoạch với mô hình học được (mạch 1; mở chương)

- **1.1 Kết quả kế thừa và bài toán trung tâm** (`cốt lõi`). Mở bằng Định lý 06.21 và Định lý 04.32 (mỗi định lý một câu phát biểu lại). **Ví dụ 11.1 (Mê cung hai phòng)**: bố cục, động lực, $v_*$ theo khoảng cách (kiểm bằng phương trình Bellman tối ưu tại $\mathrm F$: $q_*(\mathrm F,\rightarrow)=0{,}856633$, $q_*(\mathrm F,\downarrow)=0{,}770970$, $q_*(\mathrm F,\uparrow)=q_*(\mathrm F,\leftarrow)=0{,}695753$), lượt thật thứ nhất, bảng Q-learning sau lượt thứ nhất. Một câu có nguồn về mê cung Dyna của SB (tr. 164). Đoạn câu hỏi trung tâm. Hình `me-cung-hai-phong.svg`. Không có câu hỏi nghiên cứu "**Câu hỏi.**" ở §1.1 (Đ4: câu của kế hoạch được trả lời ở §2.4, trái VP-RL-2).
- **1.2 Ba cách dùng mô hình** (`cốt lõi`). Đoạn "Về mặt ý tưởng" theo SB §8.1, tr. 160: mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách. Ba cách dùng (văn xuôi, không trỏ số mục, VP20): cập nhật bảng giá trị cho mọi trạng thái trong lúc hành động; tìm kiếm từ trạng thái hiện tại lúc ra quyết định, cho hành động rời rạc hoặc liên tục; gộp nhiều bước thành tùy chọn. Hình `cau-truc-chuong.svg` có đoạn đọc hình (GC12, GC-RL-2). Không khối có số hiệu ngoài Ví dụ 11.1.
- **Kết mục §1:** Q-learning bỏ phí mẫu đã có; muốn dùng lại mẫu cần biết mô hình là gì, ước lượng từ dữ liệu ra sao và sai đến đâu.
- **Nguồn:** SB §8.1, tr. 159–161; §8.2, Ví dụ 8.1, Hình 8.2–8.3, tr. 164–165.

### §2. Tính bất định của môi trường và lập kế hoạch nền (mạch 2; giáo trình 11.1)

**2.1 Mô hình phân phối và mô hình mẫu** (`cốt lõi`; SB §8.1, tr. 159–160; §8.8, tr. 180–181).

- Bài toán: cặp $(\mathrm F,\rightarrow)$ có hai kết cục; cập nhật $Q(\mathrm F,\rightarrow)$ cần cả phân phối hay một mẫu. Trực quan: ví dụ mười hai con xúc xắc của SB tr. 159 (một câu, có nguồn).
- **Ví dụ 11.2 (Mô hình phân phối và mô hình mẫu của $(\mathrm F,\rightarrow)$)**: $\{\mathrm K:0{,}8;\ \mathrm F:0{,}2\}$; mục tiêu kỳ vọng $0{,}36$; mẫu $0{,}45$ hoặc $0$, trung bình $0{,}36$.
- **Định nghĩa 11.1 (Mô hình phân phối, mô hình mẫu, kinh nghiệm mô phỏng)**. Trường hợp riêng của "mô hình" ở Định nghĩa 01.14; mô hình phân phối sinh được mẫu, mô hình mẫu dễ có hơn (SB tr. 160).
- **Định nghĩa 11.2 (Lập kế hoạch nền, lập kế hoạch tại thời điểm quyết định)**. Lập kế hoạch trong không gian trạng thái: nhận mô hình, trả hoặc cải thiện chính sách (SB tr. 160); nền: cải thiện bảng hoặc chính sách cho nhiều trạng thái trước khi gặp chúng; tại thời điểm quyết định: bắt đầu và kết thúc sau khi gặp $S_t$, đầu ra là $A_t$ (SB tr. 180–181).
- **Nhận xét 11.3 (Quy hoạch động là lập kế hoạch nền với mô hình phân phối)**. Lượt quét của Thuật toán 04.28, 04.31 dùng mô hình phân phối đã biết; chương bỏ giả thiết biết mô hình.

**2.2 Mô hình đếm và hai loại bất định** (`cốt lõi`; giáo trình 11.1).

- Bài toán: $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$ dựa trên hai mẫu. Trực quan: trượt là thuộc tính của môi trường; sai lệch của $\hat p$ do ít dữ liệu; SB §8.3, tr. 166 nêu các nguyên nhân làm mô hình sai (môi trường ngẫu nhiên và số mẫu hạn chế, xấp xỉ hàm chưa tốt, môi trường thay đổi), cơ sở của đoạn này.
- **Ví dụ 11.3 (Bảng đếm sau lượt thứ nhất)**: $C(\mathrm A,\rightarrow)=2$, $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$; ba cặp một mẫu; các cặp khác chưa xác định.
- **Định nghĩa 11.4 (Mô hình đếm)**: $\hat p(s'\mid s,a)=C(s,a,s')/C(s,a)$, $\hat r$ trung bình phần thưởng, xác định khi $C(s,a)\ge1$. Nguồn: SB §8.4, tr. 170 (mô hình đếm số lần mỗi trạng thái kế xuất hiện, cho môi trường ngẫu nhiên). Móc nối: cùng tần suất của Mệnh đề 05.34, cho cặp thay vì trạng thái. Câu "ước lượng hợp lý cực đại của phân phối phân loại": tác tử soạn giữ hoặc bỏ theo VP21.
- **Mệnh đề 11.5 (Kỳ vọng và phương sai của xác suất ước lượng)**. Giả thiết: $C(s,a)=n\ge1$ cố định trước; $n$ trạng thái kế độc lập, cùng phân phối $p(\cdot\mid s,a)$ (môi trường dừng, Markov). Kết luận: $\mathbb E\hat p(s'\mid s,a)=p$, $\operatorname{Var}\hat p(s'\mid s,a)=p(1-p)/n$. Điều kiện áp dụng: $n$ không phụ thuộc kết quả thử. Phạm vi: chỉ bảng; không nói về sai số của giá trị lập kế hoạch. **Chứng minh đầy đủ** (tổng $n$ biến Bernoulli độc lập).
- **Ví dụ 11.4 (Hai loại bất định trên $(\mathrm F,\rightarrow)$)**: giả sử $C=5$ với $4$ lần tới $\mathrm K$; độ lệch chuẩn $\sqrt{0{,}16/C}$: $0{,}282843$ ($C=2$), $0{,}178885$ ($C=5$), $0{,}056569$ ($C=50$); phương sai Bernoulli $0{,}16$ không đổi.
- **Định nghĩa 11.6 (Bất định ngẫu nhiên, bất định nhận thức)**, phát biểu bằng hai đại lượng $p(1-p)$ và $p(1-p)/n$ của Mệnh đề 11.5. Phản ví dụ (GC9): môi trường tất định không có bất định ngẫu nhiên nhưng vẫn có bất định nhận thức ở cặp chưa thử. Nhầm lẫn (GC11): coi $\hat p=1$ sau một lần thử là chắc chắn. Nguồn thuật ngữ: Chua và cộng sự (2018, §4): bất định ngẫu nhiên do tính ngẫu nhiên vốn có của hệ, bất định nhận thức do thiếu dữ liệu và mất đi khi dữ liệu vô hạn; hai đại lượng $p(1-p)$ (không đổi theo $n$) và $p(1-p)/n$ (về $0$) khớp hai mô tả đó.

**2.3 Tập mô hình** (`bổ sung`, Q1).

- Bài toán: mô hình là mạng nơ-ron thì không có công thức của Mệnh đề 11.5.
- **Ví dụ 11.5 (Tập ba mô hình tại $(\mathrm A,\rightarrow)$)**: ba lần lấy lại mẫu có hoàn lại cho $0$; $0{,}5$; $1$; trung bình $0{,}5$, độ lệch chuẩn $0{,}408248$; tại $(\mathrm B,\downarrow)$ (một mẫu) mọi mô hình cho $1$.
- **Nhận xét 11.7 (Tập mô hình)**: độ phân tán giữa các dự báo đo bất định nhận thức; giới hạn ở cặp một mẫu; mỗi mô hình học trên tập dữ liệu lấy lại có hoàn lại, độ phân tán xa vùng có dữ liệu đo bất định nhận thức (Chua và cộng sự 2018, §4 và chú thích Hình 1); ý "giới hạn ở cặp một mẫu" là suy luận của chương, không gắn nguồn. Không định lý. Viết "lấy lại mẫu có hoàn lại", không "bootstrap" trơn (VP-RL-3).

**2.4 Q-planning và kiến trúc Dyna** (`cốt lõi`; SB §8.1, tr. 161; §8.2, tr. 161–166).

- Bài toán: sau lượt thứ nhất chỉ một ô khác $0$ (Ví dụ 11.1). Trực quan, mở bằng giới hạn của Q-learning trong một dòng (NT-RL-3): áp dụng quy tắc Q-learning lên mẫu do mô hình sinh.
- **Ví dụ 11.6 (Một cập nhật Q-planning)**: mục tiêu $0{,}45$, sai lệch $0{,}45$, $Q(\mathrm F,\rightarrow)=0{,}225$.
- **Thuật toán 11.8 (Q-planning một bước, chọn ngẫu nhiên, dạng bảng)** (SB tr. 161): bước 1 chọn ngẫu nhiên một cặp hợp lệ $(S,A)$ trong **mọi** cặp, mô hình mẫu xác định ở mọi cặp; chi phí mỗi bước $O(\lvert\mathcal A\rvert)$. Giới hạn "chỉ chọn cặp đã thử" thuộc Thuật toán 11.10.
- **Mệnh đề 11.9 (Hội tụ của Q-planning)** — bảo đảm. Giả thiết quyết định: mô hình mẫu cố định, xác định ở **mọi** cặp hợp lệ (như hộp Q-planning của SB tr. 161); phần thưởng mô hình bị chặn; $0\le\gamma<1$; mọi cặp được chọn vô hạn lần ở bước 1; bước học thỏa Định nghĩa 06.19. Kết luận: $Q\to\hat q_*$ hầu chắc chắn. Điều kiện áp dụng: mô hình không đổi trong lúc lập kế hoạch. Phạm vi: $\hat q_*$ khác $q_*$ khi mô hình sai (Tình huống 11.2). **Chứng minh đầy đủ ngắn**: mẫu do mô hình sinh thỏa giả thiết nền của Nhận xét 06.20 cho MDP của mô hình; áp dụng Định lý 06.21. Nguồn: SB tr. 161 (điều kiện hội tụ nêu bằng lời: cùng điều kiện với Q-learning một bước dạng bảng).
- **Ví dụ 11.7 (Lượt thứ nhất của Dyna-Q, $n=2$)**: bước thứ năm: trực tiếp $Q(\mathrm K,\rightarrow)=0{,}5$; mô hình $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$; lập kế hoạch $(\mathrm F,\rightarrow)$: $0{,}225$, rồi $(\mathrm K,\rightarrow)$: $0{,}75$; kiểm thứ tự ngược cho $0{,}3375$; so với $n=0$.
- **Thuật toán 11.10 (Dyna-Q dạng bảng)**, các bước (a)–(f) của hộp SB tr. 164; giả thiết: môi trường tất định; chi phí mỗi bước thật $O((n+1)\lvert\mathcal A\rvert)$. Hình `kien-truc-dyna.svg` (vẽ lại ý SB Hình 8.1, tr. 163) có đoạn đọc hình.
- **Nhận xét 11.11 (Dyna-Q, bộ nhớ phát lại và bảo đảm)**: bước (f) giống rút từ bộ nhớ phát lại (Định nghĩa 08.7) rồi cập nhật Q-learning; mô hình gộp bộ chuyển theo cặp. Nêu định tính: Dyna-Q chỉ chọn cặp đã thử (SB tr. 163), nên cặp chưa thử giữ giá trị khởi tạo và vẫn đi vào mục tiêu $\max_aQ(S',a)$; Mệnh đề 11.9 không áp dụng nguyên văn, và chương không phát biểu giới hạn của Dyna-Q, kể cả khi mô hình đổi sau mỗi bước thật (không có nguồn trong GC-RL-5; SB không so sánh Dyna với bộ nhớ phát lại, nên phép so sánh là của học phần, chỉ về cấu trúc).
- **Trong thực hành:** bảng $Q$ và từ điển mô hình; giả thiết tất định bị vi phạm khi có trượt; $n$ điều chỉnh giữa phép tính và số bước thật (SB Hình 8.2: $n=0,5,50$).

**2.5 Mô hình sai và thưởng thăm dò** (`cốt lõi`; SB §8.3, tr. 166–168).

- Bài toán: **Ví dụ 11.8 (Mê cung đổi cửa)**: sau 3 000 bước, cửa $\mathrm F$–$\mathrm K$ bị chặn, tường $\mathrm B$–$\mathrm C$ được dỡ; mô hình quá lạc quan tại $(\mathrm F,\rightarrow)$ (kiểu SB Ví dụ 8.2, tr. 166) và quá bi quan tại $(\mathrm B,\rightarrow)$ (kiểu SB Ví dụ 8.3, tr. 167). Trực quan: chính sách tham lam tự kiểm lại mô hình lạc quan, không kiểm lại mô hình bi quan.
- **Ví dụ 11.9 (Một cập nhật Dyna-Q+)**: $\kappa\sqrt\ell=0{,}2$; mục tiêu $0{,}74$; $Q(\mathrm B,\rightarrow)$ từ $0{,}54$ lên $0{,}64>0{,}6$; không có thưởng thì $0{,}54$ là điểm bất động. Ví dụ đứng trước Định nghĩa 11.12 như trong ghi chú (ví dụ trước định nghĩa, GC18).
- **Định nghĩa 11.12 (Thưởng thăm dò của Dyna-Q+)**: phần thưởng mô phỏng $\hat r+\kappa\sqrt{\ell(s,a)}$ trong bước lập kế hoạch, cùng hai thay đổi ở chú thích 1, SB tr. 168.
- **Nhận xét 11.13 (Thăm dò trong lập kế hoạch)**: với thưởng, bảng không còn ước lượng $\hat q_*$ của mô hình (Mệnh đề 11.9 không áp dụng). Không trỏ tới Bài tập 11.19 (Đ5, VP20).

**2.6 Cập nhật kỳ vọng và cập nhật mẫu** (`cốt lõi`; SB §8.5, tr. 172–174).

- Bài toán: $(\mathrm A,\rightarrow)$ có hai trạng thái kế theo mô hình đếm. **Ví dụ 11.10**: kỳ vọng $0{,}45$ ($b=2$ đánh giá); mẫu $0{,}54$ hoặc $0{,}36$, trung bình $0{,}45$.
- **Định nghĩa 11.14 (Cập nhật kỳ vọng, cập nhật mẫu, hệ số phân nhánh)**, dạng cho $q_*$ (thu gọn SB Hình 8.6).
- **Mệnh đề 11.15 (Sai số của trung bình các cập nhật mẫu)**. Giả thiết: giá trị kế $x_{s'}$ đúng và cố định; $k$ trạng thái kế rút độc lập theo $\hat p$ ($k$ là chỉ số cục bộ của tiểu mục); $\alpha_j=1/j$. Kết luận: (a) sai số bình phương trung bình $\sigma^2/k$; (b) với $b$ trạng thái kế đồng khả năng và $x_{s'}$ độc lập phương sai $1$, $\mathbb E\sigma^2=(b-1)/b$, sai số căn bình phương trung bình $\sqrt{(b-1)/(bk)}$. Ghi chú viết "mô hình sau cho công thức của Sutton và Barto (2018, tr. 174)": sách chỉ nêu công thức, không nêu mô hình xác suất, và lấy sai số ban đầu bằng $1$ làm mức chuẩn hóa; mô hình này cho đúng công thức với $k\ge1$, không cho sai số ban đầu $1$. Điều kiện áp dụng: cập nhật kỳ vọng cho sai số $0$ sau $b$ đánh giá. Phạm vi: trong bài toán thật giá trị kế cũng đang đổi; nhận định của SB tr. 174 nêu như nhận định của nguồn. **Chứng minh đầy đủ**. Dạng tổng quát $1-\sum\hat p_i^2$ không đưa vào (lời giải của Bài tập 11.14).
- **Ví dụ 11.11 (Sai số của cập nhật mẫu)**: $0{,}707107$ ($b=2,k=1$); $0{,}314643$ ($b=100,k=10$); $0{,}099499$ ($b=100,k=100$). Hình `cap-nhat-ky-vong-va-mau.svg`: điểm $k=0$ ghi là mức chuẩn hóa $1$, đường cập nhật mẫu vẽ từ $k=1$.
- **Nhận xét 11.16 (Điều kiện ưu tiên cập nhật mẫu)**: hệ số phân nhánh lớn, quá nhiều trạng thái để giải chính xác (SB tr. 174). Tên khối sửa so với kế hoạch ("Khi nào chọn cập nhật mẫu") để không mang dạng câu hỏi (VP7).

**2.7 Đọc thêm: phân bổ các cập nhật** (`đọc thêm`; phát biểu lại giáo trình 4.4.1: quét ưu tiên, RTDP).

- **Nhận xét 11.17 (Quét ưu tiên)**: SB §8.4, tr. 168–171; nối với Định lý 04.32 (mọi trạng thái vẫn phải được cập nhật vô hạn lần); động lực: thứ tự ngược ở Ví dụ 11.7 cho $0{,}3375$.
- **Nhận xét 11.18 (Lấy mẫu theo quỹ đạo)**: SB §8.6, tr. 174–177; Hình 8.8 (tr. 176) nêu bằng lời.
- **Định lý 11.19 (Hội tụ của RTDP)** — **dẫn nguồn** (Barto, Bradtke và Singh 1995, qua SB tr. 178). Giả thiết: bài toán có kết thúc, không chiết khấu, đích hấp thụ phần thưởng $0$; mỗi lượt bắt đầu ở một trạng thái chọn ngẫu nhiên trong tập trạng thái đầu và kết thúc ở đích (SB tr. 178); bốn điều kiện (giá trị đầu tại đích bằng $0$; tồn tại chính sách tới đích với xác suất $1$ từ mọi trạng thái đầu; phần thưởng ngoài đích âm ngặt; giá trị đầu không nhỏ hơn giá trị tối ưu). Kết luận: hội tụ với xác suất $1$ tới chính sách tối ưu trên các trạng thái liên quan. Phạm vi: mê cung hai phòng (phần thưởng $+1$ ở đích, $0$ ở chỗ khác) không thỏa điều kiện thứ ba.
- **Kết mục §2:** đã có Mệnh đề 11.5, 11.9, 11.15, Thuật toán 11.10; lập kế hoạch nền tốn phép tính cho mọi trạng thái, kể cả trạng thái tác tử không tới gần; khi chỉ cần quyết định tại trạng thái hiện tại, phép tính nên dồn vào đó.

### §3. Tìm kiếm theo cây Monte Carlo (mạch 3; giáo trình 11.2)

**3.1 Lập kế hoạch tại thời điểm quyết định và thuật toán rollout** (`cầu nối`, phát biểu lại giáo trình 4.3.1; SB §8.10, tr. 183–185; Bertsekas 2019, §2.4 và §5.1.2).

- Bài toán: tác tử ở $\mathrm F$, có mô hình mẫu đúng và chính sách cơ sở $\pi_0$ ngẫu nhiên đều. Trực quan: thử từng hành động trong mô hình rồi đi tiếp theo $\pi_0$, lấy trung bình lợi tức.
- **Ví dụ 11.12 (Rollout tại $\mathrm F$ với chính sách ngẫu nhiên đều)**: gồm cả lượt tính tay của Thuật toán 11.20 (không thêm số Ví dụ). Dữ kiện: $\pi_0$ ngẫu nhiên đều, $m=2$ mô phỏng mỗi hành động, không cắt ($D=\infty$, lượt kết thúc với xác suất $1$). Bảng $v_{\pi_0}$ ($\mathrm A$ $0{,}088969$; $\mathrm B$, $\mathrm E$ $0{,}113683$; $\mathrm C$ $0{,}426962$; $\mathrm D$ $0{,}601855$; $\mathrm F$ $0{,}201554$; $\mathrm K$ $0{,}489270$); $q_{\pi_0}(\mathrm F,\cdot)$: $\rightarrow$ $0{,}388554$, $\downarrow$ $0{,}181398$, $\uparrow$ và $\leftarrow$ $0{,}118131$ (ghi chú viết bốn chữ số: $0{,}3886$; $0{,}1814$; $0{,}1181$, Đ9). Hai mô phỏng "Giả sử" mỗi hành động, lợi tức $\gamma^{j-1}$ khi vào $\mathrm Z$ ở bước $j$: $\rightarrow$: $0{,}9$ và $\gamma^{12}=0{,}2824$, $\bar G=0{,}5912$; $\downarrow$: $0{,}81$ và $\gamma^{20}=0{,}1216$, $\bar G=0{,}4658$; $\uparrow$: $\gamma^5=0{,}5905$ và $\gamma^{25}=0{,}0718$, $\bar G=0{,}3311$; $\leftarrow$: $\gamma^8=0{,}4305$ và $\gamma^{30}=0{,}0424$, $\bar G=0{,}2364$; chọn $\rightarrow$, trùng hành động tham lam theo $q_{\pi_0}$, nhưng $\bar G(\rightarrow)-q_{\pi_0}(\mathrm F,\rightarrow)=0{,}2027$. Kiểm trung bình $0{,}2016$.
- **Thuật toán 11.20 (Thuật toán rollout)** (đổi từ Định nghĩa 11.20, giữ số hiệu; quyết định Q-B của điều phối viên, GC-RL-11): đầu vào mô hình mẫu, chính sách cơ sở $\pi_0$ Markov dừng, trạng thái $s$, $\gamma$; tham số $m\ge1$ và độ sâu cắt $D\in\{1,2,\dots\}\cup\{\infty\}$ ($D=\infty$ chỉ khi lượt kết thúc với xác suất $1$); mỗi mô phỏng dừng khi tới trạng thái kết thúc hoặc ở độ sâu $D$, lợi tức chiết khấu; đầu ra $A_t\in\arg\max_a\bar G(a)$, phá hòa cố định; chi phí $O(\lvert\mathcal A(s)\rvert\,m\,D)$ lần gọi mô hình khi $D$ hữu hạn. Chính sách rollout $\pi_{\mathrm{ro}}(s)\in\arg\max_aq_{\pi_0}(s,a)$ định nghĩa trong đoạn văn sau khối; khi mô hình đúng, không cắt và $m\to\infty$, $\bar G(a)\to q_{\pi_0}(s,a)$ hầu chắc chắn. Một câu phân biệt với "đoạn thu (rollout)" của Bài 10; một câu tương ứng: Sutton và Barto gọi $\pi_0$ là "rollout policy" (Q6, Đ3).
- **Mệnh đề 11.21 (Tính chất cải thiện của rollout)** — bảo đảm. Giả thiết quyết định: MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; $\pi_0$ Markov dừng; $q_{\pi_0}$ **chính xác**; $\pi_{\mathrm{ro}}$ tham lam theo $q_{\pi_0}$ tại mọi trạng thái. Kết luận: $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$, nghiêm ngặt tại $s$ khi $\max_aq_{\pi_0}(s,a)>v_{\pi_0}(s)$. Điều kiện áp dụng: $q_{\pi_0}$ chính xác (với ước lượng từ $m$ mô phỏng, xác suất chọn sai được chặn ở mệnh đề kế tiếp; câu này viết không trỏ số hiệu phía sau, Đ6). Phạm vi: không bảo đảm tối ưu (SB tr. 184). **Chứng minh đầy đủ**: $q_{\pi_0}(s,\pi_{\mathrm{ro}}(s))=\max_aq_{\pi_0}(s,a)\ge\sum_a\pi_0(a\mid s)q_{\pi_0}(s,a)=v_{\pi_0}(s)$, rồi Định lý 04.13(a), (b). Nguồn: SB tr. 184 (định lý cải thiện chính sách áp dụng cho rollout, nêu định tính); Bertsekas (2019), §2.4 (tên và số mục theo mục lục); Bertsekas (2020, Mệnh đề 5.4.2, tr. 386), phát biểu dạng chi phí và cực tiểu hóa: chính sách rollout có chi phí không lớn hơn chính sách cơ sở; tr. 385–386 gọi rollout là một bước lặp chính sách. Kết quả chính của mạch 3, có trang "Ý tưởng chứng minh" (Q16). Móc nối: thực hiện rollout ở mỗi trạng thái gặp chính là thực hiện $\pi_{\mathrm{ro}}$; SB tr. 184 so với một bước lặp chính sách, và nói thêm rằng vì chỉ đổi hành động tại trạng thái hiện tại, nó giống một bước lặp giá trị bất đồng bộ hơn; ghi chú giữ cả hai ý.
- **Ví dụ 11.13 (Chính sách rollout trên cả mê cung)**: mọi lựa chọn là một bước của đường ngắn nhất ($\mathrm C$: $0{,}510189$ so với $\downarrow$ $0{,}4291$); tại $\mathrm F$ từ $0{,}2016$ lên $0{,}8566=v_*(\mathrm F)$; bảo đảm chỉ là "không giảm".
- **Mệnh đề 11.22 (Xác suất chọn sai của rollout với $m$ mô phỏng)** — bảo đảm. Giả thiết: mô hình mẫu đúng; $\Delta=q_{\pi_0}(s,a)-q_{\pi_0}(s,a')>0$; Thuật toán 11.20 với $m$ cố định trước; mô phỏng **không cắt** ($D=\infty$, lượt kết thúc với xác suất $1$); $2m$ lợi tức độc lập, mỗi lợi tức trong đoạn độ rộng $B$. Kết luận (3.1): $\Pr\{\bar G(a')\ge\bar G(a)\}\le\exp(-m\Delta^2/B^2)$. Điều kiện áp dụng: nhiều hành động dùng bất đẳng thức hợp (Bài tập 11.8). Phạm vi: không áp dụng khi $m$ chọn theo kết quả; khi cắt ở $D$ hữu hạn, (3.1) đúng với $\Delta^D=q^D_{\pi_0}(s,a)-q^D_{\pi_0}(s,a')$, trong đó $q^D_{\pi_0}$ là kỳ vọng của lợi tức trong $D$ bước đầu. **Chứng minh đầy đủ**: Hoeffding một phía (tiên quyết 8) với $t=m\Delta$, tổng bình phương độ rộng $2mB^2$.
- **Ví dụ 11.14 (Số mô phỏng của rollout)**: $B=1$, $\Delta=0{,}207156$; $m\ge\ln20/\Delta^2=69{,}81$; $m=70$ cho $0{,}049591$; $m=50$ cho $0{,}116988$ (ghi chú viết $\Delta=0{,}2072$, $m\ge69{,}8$, $0{,}0496$, $0{,}1170$, Đ9). Thêm dòng cho cắt ở $D=20$: $q^{20}_{\pi_0}(\mathrm F,\rightarrow)=0{,}3792$, $q^{20}_{\pi_0}(\mathrm F,\downarrow)=0{,}1670$, $\Delta^{20}=0{,}2122$, với $m=70$ chặn bằng $0{,}0428$ (số của ghi chú; tác tử rà toán tính lại).
- **Trong thực hành:** mô phỏng độc lập chạy song song; cắt mô phỏng sớm và cộng giá trị ước lượng (SB tr. 185); thời gian quyết định giới hạn $m$.

**3.2 Chọn hành động theo cận tin cậy trên** (`cầu nối`, phát biểu lại giáo trình 4.7.1–4.7.2; SB §2.7, tr. 35–36).

- Bài toán: rollout chia đều $m$ mô phỏng, kể cả cho $\uparrow$ tại $\mathrm F$ đã thấy rõ là kém. Trực quan: lựa chọn ở gốc là bài toán chọn lặp lại (Định nghĩa 01.16); ưu tiên hành động có trung bình cao hoặc còn ít mẫu.
- **Ví dụ 11.15 (Quy tắc cận tin cậy trên, hai hành động)**: sau $8$ lần chọn, lần chọn kế là bước $t=9$ theo quy ước của (3.2), $\ln9=2{,}1972$; dòng "Quy tắc." nêu phép tính trước; chỉ số $0{,}6+0{,}6051=1{,}2051$ và $0{,}4+1{,}0481=1{,}4481$; chọn hành động 2 (quyết định Q-D; kế hoạch dùng $\ln8$, cho $1{,}1887$ và $1{,}4197$).
- **Định nghĩa 11.23 (Quy tắc cận tin cậy trên)**: $A=\arg\max_a[\bar r(a)+c_{\mathrm{ucb}}\sqrt{\ln t/N(a)}]$, $N(a)=0$ coi là cực đại (SB (2.10), tr. 35); $t$ là bước hiện tại, $N(a)$ đếm các lần chọn trước bước $t$ (quy ước này cũng ghi trong "Hướng dẫn và ký hiệu" của `exercises.md` cho Bài tập 11.18). Một câu: UCB1 của Auer, Cesa-Bianchi và Fischer (2002, Hình 1, tr. 237) là quy tắc này với $c_{\mathrm{ucb}}=\sqrt2$, trong đó $\ln t$ thay bằng $\ln(t-1)$ ($t-1$ là số lần chọn đã thực hiện), và bước khởi tạo "chọn mỗi hành động một lần" ứng với quy ước $N(a)=0$ coi là cực đại. Szepesvári (2010, §4.2.1) viết cùng quy tắc cho phần thưởng trong $[-R,R]$; ghi chú dùng dạng chuẩn hóa của Auer.
- **Định lý 11.24 (Bảo đảm của UCB1)** — bảo đảm, **dẫn nguồn, không chứng minh** (Auer, Cesa-Bianchi và Fischer 2002, Định lý 1, tr. 237; quyết định của điều phối viên sau kiểm nguồn gốc). Giả thiết: $K>1$ hành động; phần thưởng của mỗi hành động độc lập, cùng phân phối theo thời gian, độc lập giữa các hành động, có miền giá trị trong $[0,1]$; $\Delta_a=\mu^*-\mu_a$ với $\mu_a$ là phần thưởng kỳ vọng của $a$, $\mu^*$ là kỳ vọng lớn nhất. Kết luận, ghi rõ đại lượng được chặn: (i) **số lần chọn** kỳ vọng của mỗi hành động không tối ưu sau $n$ bước, $\mathbb E[N_n(a)]\le 8\ln n/\Delta_a^2+1+\pi^2/3$ (từ chứng minh, tr. 243); (ii) **hối tiếc** kỳ vọng sau $n$ bước, $\mu^*n-\sum_a\mu_a\mathbb E[N_n(a)]$, không vượt $8\sum_{a:\Delta_a>0}\ln n/\Delta_a+(1+\pi^2/3)\sum_a\Delta_a$ (Định lý 1 và (2), tr. 237–238), nên tăng theo $\ln n$. Trong (ii), $\Delta_a$ ở mẫu số bậc một; trong (i), bậc hai. Điều kiện áp dụng: UCB1 với $c_{\mathrm{ucb}}=\sqrt2$ như Định nghĩa 11.23. Phạm vi: không áp dụng khi phân phối đổi theo thời gian (SB tr. 36), như ở các nút trong của cây, nơi dãy lợi tức trôi theo thời gian (Kocsis và Szepesvári 2006, §2.2). Ý tưởng (một đoạn, không khối `proof`): hành động kém chỉ bị chọn khi cận trên của nó vượt cận trên của hành động tốt nhất; khi $a$ đã được chọn ít nhất $8\ln n/\Delta_a^2$ lần, bất đẳng thức Chernoff–Hoeffding chặn xác suất của biến cố đó (Auer và cộng sự 2002, tr. 242–243).
- Hiện tượng "đỉnh ở bước 11" của SB Hình 2.4 là Bài tập 11.18 (SB Bài tập 2.8); không giải trong ghi chú, không khối riêng.

**3.3 Bốn pha của tìm kiếm theo cây Monte Carlo** (`cốt lõi`; SB §8.11, tr. 185–188; Kocsis và Szepesvári 2006, §2.2–2.3, cho quy tắc UCT).

- Bài toán: rollout không nhớ gì giữa các mô phỏng (SB tr. 185). Trực quan: giữ một cây gốc $\mathrm F$; trong cây chọn bằng chỉ số cận tin cậy trên; ngoài cây mô phỏng theo chính sách cơ sở $\pi_0$ (Đ3).
- **Ví dụ 11.16 (Một vòng tìm kiếm theo cây Monte Carlo tại $\mathrm F$, $c_{\mathrm{ucb}}=1$)**: $\pi_0$ ngẫu nhiên đều, $D=20$. Dữ kiện "Giả sử": lần chọn $\uparrow$ và $\leftarrow$ trước đó đều trượt (nên $\mathrm B$, $\mathrm E$ ở độ sâu $1$ chưa có trong cây); tám lợi tức đã nhận $\gamma,\gamma^2,\gamma^6,\gamma^6$ qua $\rightarrow$, $\gamma^4,\gamma^6$ qua $\downarrow$, $\gamma^{11}$ qua $\uparrow$, $\gamma^{15}$ qua $\leftarrow$. Bảng cạnh gốc (bốn chữ số): $\rightarrow$ $N=4$, $W=2{,}7729$, $\bar Q=0{,}6932$, chỉ số $1{,}4142$; $\downarrow$ $N=2$, $W=1{,}1875$, $\bar Q=0{,}5938$, $1{,}6134$; $\uparrow$ $N=1$, $W=0{,}3138$, $1{,}7558$; $\leftarrow$ $N=1$, $W=0{,}2059$, $1{,}6479$; $N(\mathrm F)=8$. Chọn $\uparrow$; mở rộng ra $\mathrm B$; mô phỏng $\mathrm B\to\mathrm F\to\mathrm K\to\mathrm Z$, $G=\gamma^3=0{,}729$, bốn bước ít hơn $D$; cập nhật ngược $N(\mathrm F,\uparrow)=2$, $W=1{,}0428$, $\bar Q=0{,}5214$, $N(\mathrm F)=9$; nút $\mathrm B$ giữ mọi thống kê bằng $0$, kể cả $N(\mathrm B)=0$ (quyết định Q-E; kế hoạch ghi $N(\mathrm B)=1$ và $W$ một chữ số $2{,}8$; $1{,}2$; $0{,}3$; $0{,}2$); hành động thật $\rightarrow$ ($N=4$). Hình `mcts-bon-pha.svg` khớp các số này. Câu bắt buộc: $c_{\mathrm{ucb}}=1$ là hệ số của ví dụ, không phải hệ số mà Định lý 11.27(a) đòi hỏi.
- **Định nghĩa 11.25 (Cây tìm kiếm, chính sách cây, thống kê cạnh)**: nút là trạng thái gặp trong mô phỏng; cạnh $(s,a)$ giữ $N(s,a)$, $W(s,a)$; $\bar Q=W/N$; chính sách cây chọn theo chỉ số UCT $\bar Q(s,a)+c_{\mathrm{ucb}}\sqrt{\ln N(s)/N(s,a)}$; ngoài cây, pha mô phỏng dùng chính sách cơ sở $\pi_0$ của Thuật toán 11.20 (Đ3; "chính sách rollout" chỉ dành cho $\pi_{\mathrm{ro}}$, Q6). Một câu tương ứng: Sutton và Barto gọi chính sách ngoài cây là "rollout policy". Chỉ số UCT ứng với $c_{t,s}=2C_p\sqrt{\ln t/s}$ của Kocsis và Szepesvári (2006, §2.2) với $c_{\mathrm{ucb}}=2C_p$; nút của họ là cặp (trạng thái, độ sâu), tương thích với cây của chương khi nêu rõ rằng cùng một trạng thái gặp ở hai độ sâu là hai nút.
- **Thuật toán 11.26 (Tìm kiếm theo cây Monte Carlo với UCT)**: đầu vào gồm trạng thái hiện tại, mô hình mẫu, chính sách cơ sở $\pi_0$, $c_{\mathrm{ucb}}$, ngân sách vòng lặp và **độ sâu cắt $D$** (Q9; ví dụ của chương dùng $D=20$): mọi mô phỏng dừng khi tới trạng thái kết thúc hoặc khi tổng độ sâu tính từ gốc đạt $D$, lợi tức là tổng chiết khấu của tối đa $D$ phần thưởng. Bốn bước chọn, mở rộng, mô phỏng, cập nhật ngược (SB tr. 187); lợi tức cập nhật cho cạnh ở độ sâu $j$ là lợi tức chiết khấu tính từ cạnh đó; đầu ra: hành động ở gốc có $N$ lớn nhất (hoặc $\bar Q$ lớn nhất, SB tr. 187); dùng lại cây con của trạng thái kế (SB tr. 187). Chi phí mỗi vòng $O(D)$ lần gọi mô hình.
- **Trong thực hành:** mô hình mẫu phải nhanh (SB tr. 185); MCTS không cần xấp xỉ hàm toàn cục (SB tr. 188).

**3.4 Bảo đảm của UCT và giá trị học được** (`cốt lõi` cho định lý; `đọc thêm` cho Nhận xét 11.28, kế hoạch ghi `bổ sung`, Đ8).

- **Định lý 11.27 (Tính nhất quán của UCT cho bài toán cắt)** — bảo đảm (Q9, Đ2, quyết định Q-F). Giả thiết chung: tập hành động hữu hạn; mô hình mẫu đúng; bài toán cắt ở độ sâu $D$ (chương dùng $D=20$). Giả thiết của (a), tách khỏi (b): mỗi **phần thưởng** nằm trong $[0,1]$, nên lợi tức của bài toán cắt nằm trong $[0,D]$; thuật toán là **UCT của Kocsis và Szepesvári (2006)**, không phải Thuật toán 11.26: chỉ số (3.3) áp ở mọi nút (trạng thái, độ sâu) tới độ sâu $D$, mỗi vòng đi từ gốc tới độ sâu $D$ hoặc tới trạng thái kết thúc, với $c_{\mathrm{ucb}}=\sqrt2\,D$ (hệ số thăm dò của UCB1 nhân $D$, tương đương chia mọi phần thưởng cho $D$ rồi dùng UCB1); hành động tối ưu của bài toán cắt ở gốc là duy nhất. Giả thiết của (b): phần thưởng không âm và **lợi tức** của mọi lượt, cắt hay không, nằm trong $[0,1]$. Kết luận: (a) **dẫn nguồn, định tính** (Kocsis và Szepesvári 2006, Định lý 6): xác suất UCT chọn ở gốc một hành động khác hành động tối ưu của bài toán cắt tiến về $0$ khi số vòng lặp tiến ra vô hạn; không ghi bậc độ chệch, không "tốc độ đa thức"; (b) **chứng minh đầy đủ**, bốn bước: với mọi chính sách Markov dừng $\pi$, $0\le v_\pi(s)-v^D_\pi(s)=\gamma^D\mathbb E_\pi[\mathbb 1\{D<T\}v_\pi(S_D)]\le\gamma^D$ (Bổ đề 03.20), và $0\le v_*(s)-v^D_*(s)\le\gamma^D$ (Định lý 04.25(b)); với $D=20$, $\gamma^{20}=0{,}1216$ và (a) cần $c_{\mathrm{ucb}}=20\sqrt2=28{,}28$. Chứng minh (a): ngoài phạm vi học phần, ý tưởng quy nạp theo $D$, dẫn phác thảo của Kocsis và Szepesvári (2006, Định lý 6) và chứng minh đầy đủ của Kocsis, Szepesvári và Willemson (2006, Định lý 7) cho cây trò chơi có phần thưởng ở lá. Đoạn sau định lý: câu mở rộng cho MDP chiết khấu (bài ECML, sau chứng minh Định lý 6); Thuật toán 11.26 là biến thể thực hành (cây mọc mỗi vòng một nút, ngoài cây mô phỏng theo $\pi_0$) và kết luận (a) không được chứng minh cho biến thể này; ba phản ví dụ khi bỏ giả thiết (lợi tức trong $[0,1]$; phần thưởng không âm; mô hình đúng). Phạm vi: (a) là tiệm cận; không áp dụng khi mô hình sai; $c_{\mathrm{ucb}}=1$ của Ví dụ 11.16 không thỏa (a). Hệ quả về khoảng cách $>2\gamma^D$ không có trong ghi chú.
- **Nhận xét 11.28 (Xác suất tiên nghiệm và giá trị học được trong AlphaGo Zero)** (`đọc thêm`): SB §16.6.2, tr. 447–450; mạng cho xác suất tiên nghiệm $P(s,a)$ và giá trị nút lá thay mô phỏng ngẫu nhiên; MCTS dùng làm toán tử cải thiện chính sách khi tự chơi (Silver và cộng sự 2017, thân bài). Công thức chọn (một biến thể của PUCT, Silver và cộng sự 2017, phần Phương pháp, mục "Select"; bản thảo tác giả không có số trang của *Nature*, nên không ghi trang): $a=\arg\max_a[Q(s,a)+U(s,a)]$, $U(s,a)=c_{\mathrm{puct}}P(s,a)\sqrt{\sum_bN(s,b)}/(1+N(s,a))$, $c_{\mathrm{puct}}$ là hằng số thăm dò; ban đầu ưu tiên hành động có xác suất tiên nghiệm cao và ít lượt thăm, về sau ưu tiên giá trị cao. $P$, $c_{\mathrm{puct}}$ là ký hiệu cục bộ của nhận xét (trong ghi chú viết $\bar Q$ thay $Q$ cho thống nhất với Định nghĩa 11.25). Không câu đánh giá thành tích ngoài dữ kiện của SB tr. 442 (kết quả với Fan Hui và Lee Sedol) và tr. 185 (VP6); không nhắc MuZero (VP20). Lịch sử theo NT-RL-11 nếu lên deck.
- **Trong thực hành:** khi trạng thái chỉ quan sát được một phần hoặc mô hình là mạng học được, giả thiết "mô hình đúng" của Mệnh đề 11.21 và Định lý 11.27 không còn; MCTS vẫn chạy nhưng bảo đảm không áp dụng.
- **Kết mục §3:** MCTS cần tập hành động hữu hạn và mô hình mẫu nhanh; với hành động liên tục (xe trên đường ray) không liệt kê được cạnh, nhưng mô hình khả vi cho đạo hàm chỉ hướng sửa kế hoạch.

### §4. Tối ưu kế hoạch dựa trên đạo hàm (mạch 4; giáo trình 11.3)

**4.1 Bài toán tối ưu kế hoạch trên mô hình khả vi** (`cốt lõi`). Mở thẳng bằng **Ví dụ 11.17 (Xe trên đường ray: kế hoạch không làm gì)**, $J(0,0)=8$. **Định nghĩa 11.29 (Bài toán tối ưu kế hoạch chân trời $h$, phép bắn)**: biến quyết định $u_{0:h-1}$; trạng thái thế bằng $x_{t+1}=\hat f(x_t,u_t)$ (phép bắn đơn); cực tiểu $J=\sum_{t=0}^{h-1}c(x_{t+1},u_t)$. Móc nối: tìm một chuỗi hành động cho một trạng thái đầu (vòng hở), không tìm chính sách như Bài 03–04; hành động liên tục. Một câu: cực tiểu chi phí tương đương cực đại phần thưởng $-c$.

**4.2 Đạo hàm qua mô hình** (`cốt lõi`; quy tắc dây chuyền; Goodfellow, Bengio và Courville 2016, theo tên mục về lan truyền ngược, không số mục).

- **Ví dụ 11.18 (Một bước hạ gradient)**: gradient $(8,4)$ bằng khai triển; $\eta=0{,}1$ cho $(-0{,}8;\,-0{,}4)$, $J=2{,}88$.
- **Mệnh đề 11.30 (Gradient theo chuỗi hành động bằng truy hồi ngược)**. Giả thiết: $\hat f$, $c$ khả vi liên tục. Kết luận: $\lambda_h=\partial c(x_h,u_{h-1})/\partial x_h$, $\lambda_t=\partial c(x_t,u_{t-1})/\partial x_t+\lambda_{t+1}\partial\hat f(x_t,u_t)/\partial x_t$ ($t=h-1,\dots,1$), $\partial J/\partial u_t=\partial c(x_{t+1},u_t)/\partial u_t+\lambda_{t+1}\partial\hat f(x_t,u_t)/\partial u_t$. Điều kiện áp dụng: một lượt xuôi và một lượt ngược, $O(h)$ lần đạo hàm của $\hat f$. Phạm vi: gradient trên mô hình; điểm dừng có thể là cực tiểu địa phương khi $\hat f$ phi tuyến. **Chứng minh đầy đủ** (quy nạp ngược theo $t$). Bản thứ hai của Ví dụ 11.18 ($\lambda_2=4$, $\lambda_1=8$, gradient $(8,4)$) đặt ngay sau mệnh đề. Dạng một chiều, một câu nêu dạng ma trận Jacobi.
- **Thuật toán 11.31 (Tối ưu kế hoạch bằng hạ gradient)**: lượt xuôi, lượt ngược, $u\leftarrow u-\eta\nabla J$; dừng khi $\lVert\nabla J\rVert\le\theta$ hoặc hết ngân sách; chi phí mỗi vòng $O(h)$.
- **Ví dụ 11.19 (Kế hoạch tối ưu)**: $u^*=(-1{,}2;\,-0{,}4)$, $x_1=0{,}8$, $x_2=0{,}4$, $J^*=2{,}40$; Hessian xác định dương nên là cực tiểu toàn cục; bước ở Ví dụ 11.18 còn cách tối ưu $0{,}48$.
- Đoạn móc nối (`đọc thêm`, một câu có nguồn): PILCO học mô hình động lực xác suất (quá trình Gauss) và tính giải tích gradient của chi phí dài hạn theo tham số chính sách (Deisenroth và Rasmussen 2011, §2.3).

**4.3 Điều khiển dự báo theo chân trời lùi** (`cầu nối`, phát biểu lại giáo trình 4.3.2; Bertsekas 2019, §2.5.1; nội dung kiểm trên Bertsekas 2020, §3.1, tr. 199–201).

- Bài toán: kế hoạch vòng hở tính một lần không phản ứng với trạng thái thật.
- **Ví dụ 11.20 (Điều khiển dự báo trên mô hình)**: $u_0^*=-0{,}6x_0$; luật vòng kín $u_t=-0{,}6x_t$; $2;\ 0{,}8;\ 0{,}32;\ 0{,}128$. Lượt chạy tay đứng trước Định nghĩa 11.32 như trong ghi chú (quyết định Q-K).
- **Định nghĩa 11.32 (Điều khiển dự báo theo chân trời lùi)**: tại mỗi $t$, giải bài toán của Định nghĩa 11.29 từ $x_t$, thực hiện $u_t$ đầu tiên, bỏ phần còn lại. Tên tiếng Anh: model predictive control (MPC), receding horizon control.
- **Thuật toán 11.33 (Điều khiển dự báo)**: bao Thuật toán 11.31 trong vòng lặp thời gian. Khởi động bộ giải bằng phần đuôi của kế hoạch trước chỉ được nêu như một lựa chọn cài đặt, không tuyên bố hiệu quả, không gắn nguồn (VP6), hoặc bỏ. Không phát biểu bảo đảm ổn định hay khả thi tổng quát của điều khiển dự báo (Bertsekas 2020, tr. 200–201 cần ràng buộc cuối hoặc chi phí cuối và điều kiện điều khiển được); tính ổn định chỉ xuất hiện qua phép tính của Ví dụ 11.20, 11.23. Kế hoạch ghi "bao Thuật toán 11.31 (hoặc 11.34)"; 11.34 đứng sau, nên dàn ý chỉ dẫn 11.31 và nêu khả năng thay bộ giải ở §4.4 (Đ6).
- Móc nối: điều khiển dự báo là lập kế hoạch tại thời điểm quyết định cho hành động liên tục (Định nghĩa 11.2), như rollout và MCTS cho hành động rời rạc.

**4.4 Bắn ngẫu nhiên và phương pháp entropy chéo** (`bổ sung`, Q1; Chua và cộng sự 2018, §5 và Thuật toán 1, chỉ cho việc dùng CEM trong điều khiển dự báo của PETS và thuật ngữ "mẫu ưu tú").

- Bài toán: mô hình không khả vi (bảng, mô phỏng hộp đen) hoặc $J$ nhiều cực tiểu địa phương.
- **Ví dụ 11.21 (Bắn ngẫu nhiên và một vòng entropy chéo)**: bốn ứng viên $J=8;\ 3;\ 2{,}5;\ 4$; bắn ngẫu nhiên chọn ứng viên 3; hai mẫu ưu tú cho trung bình $(-1;\,-0{,}25)$, độ lệch chuẩn $(0;\,0{,}25)$. Nhận xét độ lệch chuẩn $0$ ở tọa độ $u_0$ làm phân phối suy biến sau một vòng (đọc trực tiếp từ số liệu); việc đặt sàn cho độ lệch chuẩn chỉ nêu như lựa chọn cài đặt, không tuyên bố hiệu quả, không gắn nguồn (VP6), hoặc bỏ.
- **Thuật toán 11.34 (Tối ưu kế hoạch bằng phương pháp entropy chéo)**: rút $M$ chuỗi từ phân phối chuẩn theo tọa độ, đánh giá $J$ trên mô hình, giữ $M_{\mathrm e}$ chuỗi tốt nhất, khớp lại trung bình và độ lệch chuẩn, lặp; có thể thay Thuật toán 11.31 trong vòng lặp của Thuật toán 11.33. Phát biểu như cách cài đặt chuẩn, mức `bổ sung`; chi tiết "phân phối chuẩn theo tọa độ, khớp lại trung bình và độ lệch chuẩn" **không gán cho Chua và cộng sự** (bài chỉ dùng CEM và dẫn Botev và cộng sự 2013, chưa kiểm). Không định lý hội tụ. Sau thuật toán có đoạn "Trong thực hành." (quyết định Q-K).
- **Nhận xét 11.35 (So sánh tối ưu bằng đạo hàm và bằng lấy mẫu)**: bảng yêu cầu về mô hình, số lần gọi mô hình mỗi vòng ($O(h)$ cộng lượt ngược so với $M$ lượt xuôi), độ nhạy với cực tiểu địa phương. Tên khối sửa so với kế hoạch ("Đạo hàm hay lấy mẫu") để gọi tên nội dung (VP7).

**4.5 Sai số mô hình tích lũy** (`cốt lõi`; giáo trình 11.3).

- Bài toán: **Ví dụ 11.22 (Sai số tích lũy của mô hình)**: hệ thật $1{,}2x+u$, mô hình $x+u$, $u\equiv0$, $x_0=2$; $e_k=2(1{,}2^k-1)$: $0{,}4;\ 0{,}88;\ 1{,}456;\ 2{,}1472;\ 2{,}97664$. Hình `sai-so-tich-luy.svg`.
- **Mệnh đề 11.36 (Chặn sai số dự báo $k$ bước)**. Giả thiết: $f$ Lipschitz theo $x$ với hằng số $L$ (với mọi $u$); $\lvert f(\hat x_j,u_j)-\hat f(\hat x_j,u_j)\rvert\le\bar e$ tại các trạng thái **dự báo** $\hat x_j$, $j<k$; cùng chuỗi hành động; cùng $x_0$. Kết luận: $e_k\le\bar e\sum_{j=0}^{k-1}L^j$, bằng $\bar e(L^k-1)/(L-1)$ khi $L\ne1$, $k\bar e$ khi $L=1$. Điều kiện áp dụng: chuỗi hành động cố định (vòng hở). Phạm vi: chặn tăng theo cấp số nhân khi $L>1$; không áp dụng trực tiếp cho vòng kín; mô hình là hàm tường minh của trạng thái quan sát được. **Chứng minh đầy đủ**: $e_{j+1}\le Le_j+\bar e$, quy nạp. Kiểm: chặn đạt dấu bằng ở Ví dụ 11.22 ($\bar e=0{,}4$, $L=1{,}2$).
- **Ví dụ 11.23 (Vòng hở và điều khiển dự báo với mô hình sai)**: vòng hở $x_1=1{,}2$, $x_2=1{,}04$ (mô hình dự báo $0{,}8$; $0{,}4$); điều khiển dự báo $x_{t+1}=0{,}6x_t$: $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$. Hình `xe-tren-duong-ray.svg`.
- **Nhận xét 11.37 (Tính bất định khi lập kế hoạch liên tục)** (`đọc thêm`): PETS lập kế hoạch qua tập mô hình (Nhận xét 11.7; Chua và cộng sự 2018, §4–5); PILCO đưa bất định của mô hình vào dự báo dài hạn (Deisenroth và Rasmussen 2011, §2.2 "Policy Evaluation"; §2.3 dành cho gradient giải tích ở §4.2); một đến hai câu.
- **Trong thực hành:** $h$ dài làm sai số tích lũy lớn; gradient qua nhiều lần nhân $\partial\hat f/\partial x$ dễ bùng nổ hoặc tiêu biến (Goodfellow, Bengio và Courville 2016, theo tên mục về phụ thuộc dài hạn trong mô hình chuỗi, không số chương, số mục).
- **Kết mục §4:** gradient và điều khiển dự báo xử lý hành động liên tục ở bước thời gian nhỏ; nhìn xa cần nhiều bước, sai số tích lũy và chi phí tăng theo $h$; cần một đơn vị hành động kéo dài nhiều bước.

### §5. Học tăng cường phân cấp (mạch 5; giáo trình 11.4)

**5.1 Tùy chọn và chính sách phân cấp** (`cốt lõi`; giáo trình 11.4.1; SB §17.2, tr. 461–462; SPS §2, tr. 186–187).

- Bài toán, mở thẳng trên mê cung: lặp giá trị trên hành động một bước cần nhiều lượt quét để giá trị của $\mathrm Z$ lan về $\mathrm A$: sau sáu lượt quét $v(\mathrm A)=0{,}6103$, còn cách $v_*(\mathrm A)=0{,}6604$. Số liệu viết thẳng tại đây, không dẫn tới Ví dụ 11.26 đứng sau (Đ6). Trực quan: SB tr. 461 (các thang thời gian của cùng một MDP), một đoạn.
- **Ví dụ 11.24 (Hai tùy chọn trên mê cung hai phòng)**: tùy chọn đi tới cửa ($\mathcal I=\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$; $\mathrm A,\mathrm E,\mathrm F\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$; kết thúc tại $\mathrm K$); tùy chọn đi tới đích ($\mathcal I=\{\mathrm C,\mathrm D,\mathrm K\}$; $\mathrm C,\mathrm K\mapsto\rightarrow$, $\mathrm D\mapsto\downarrow$; kết thúc khi vào $\mathrm Z$). Hình `tuy-chon-hai-phong.svg`.
- **Định nghĩa 11.38 (Tùy chọn)**: $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$; $A_t\sim\pi_\omega(\cdot\mid S_t)$, kết thúc tại $t+1$ với xác suất $\beta_\omega(S_{t+1})$; $\tau$ là bước kết thúc; hành động một bước là tùy chọn với $\pi_\omega(s)=a$, $\beta_\omega\equiv1$ (SB tr. 462: $\gamma_\omega\equiv0$). Nguồn: SPS §2, tr. 186–187 (ba thành phần chính sách, điều kiện kết thúc, tập khởi đầu; hành động là tùy chọn với $\mathcal I=\{s:a\in\mathcal A(s)\}$, $\beta\equiv1$). Giả thiết tự nhiên $\{s:\beta_\omega(s)<1\}\subseteq\mathcal I_\omega$ (SPS tr. 186) ghi trong định nghĩa; Ví dụ 11.24 thỏa. Phản ví dụ (GC9): $\beta_\omega\equiv0$ trên một vùng không ra được thì tùy chọn không kết thúc; giả thiết "kết thúc với xác suất $1$" ghi trong giả thiết các kết quả sau.
- **Định nghĩa 11.39 (Chính sách phân cấp, giá trị của chính sách phân cấp)**: $\mu(\omega\mid s)$ trên $\Omega(s)=\{\omega:s\in\mathcal I_\omega\}$; $v_\mu$, $q_\mu(s,\omega)$. Móc nối: $\mu$ sinh một chính sách trên MDP gốc, nói chung không Markov theo trạng thái khi có tùy chọn nhiều bước (SPS tr. 187).

**5.2 Mô hình tùy chọn và bán-MDP** (`cốt lõi`; giáo trình 11.4.1; SB tr. 462–463, (17.2)–(17.4)).

- **Ví dụ 11.25 (Mô hình của hai tùy chọn)**: $\rho=0{,}8\gamma/(1-0{,}2\gamma)=0{,}878049$; tùy chọn đi tới cửa: $r=0$, $p(\mathrm K\mid\mathrm F,\cdot)=0{,}878049$, $p(\mathrm K\mid\mathrm B,\cdot)=p(\mathrm K\mid\mathrm E,\cdot)=0{,}770970$, $p(\mathrm K\mid\mathrm A,\cdot)=0{,}676949$; tùy chọn đi tới đích: $r(\mathrm K,\cdot)=r(\mathrm D,\cdot)=0{,}975610$, $r(\mathrm C,\cdot)=0{,}856633$, chuyển chỉ vào trạng thái kết thúc.
- **Định nghĩa 11.40 (Mô hình tùy chọn)**: $r(s,\omega)$ theo SB (17.2), $p(s'\mid s,\omega)=\sum_{k\ge1}\gamma^k\Pr\{S_k=s',\tau=k\}$ theo SB (17.3), tr. 462 và SPS (6)–(7), tr. 189; $p$ đã chứa chiết khấu, không phải xác suất (với hành động một bước, $p$ là xác suất chuyển nhân $\gamma$, SPS chú thích 5).
- **Mệnh đề 11.41 (Tổng hệ số chuyển của mô hình tùy chọn)**. Giả thiết: tùy chọn kết thúc với xác suất $1$; $0\le\gamma<1$. Kết luận: $\sum_{s'}p(s'\mid s,\omega)=\mathbb E[\gamma^\tau\mid S_0=s]\le\gamma$. **Chứng minh đầy đủ** ($\tau\ge1$). Kiểm: $0{,}676949\le0{,}9$.
- **Định lý 11.42 (Phương trình Bellman cho chính sách phân cấp)**. Giả thiết: MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; mọi tùy chọn có $\pi_\omega$ Markov, $\beta_\omega$ chỉ phụ thuộc trạng thái, kết thúc với xác suất $1$; $\mu$ Markov theo trạng thái tại các thời điểm chọn. Kết luận: $v_\mu(s)=\sum_{\omega\in\Omega(s)}\mu(\omega\mid s)[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)v_\mu(s')]$ (SB (17.4), tr. 463; SPS (8), tr. 190). Điều kiện áp dụng: khi $\Omega(s)$ chỉ gồm hành động một bước, trở về Định lý 03.21 với $\gamma$ nằm trong $p$. Phạm vi: chứng minh trong ghi chú cho tùy chọn Markov ($\beta_\omega$ chỉ phụ thuộc trạng thái); SPS phát biểu phương trình (8) và Định lý 1 cho cả tùy chọn bán-Markov, có chính sách và điều kiện kết thúc phụ thuộc lịch sử từ lúc tùy chọn bắt đầu. **Chứng minh đầy đủ**, bốn bước: tách lợi tức tại $\tau$; kỳ vọng phần đầu là $r(s,\omega)$; phân hoạch theo các biến cố $\{\tau=k\}$, $k\ge1$: trên mỗi biến cố, phần sau có kỳ vọng $v_\mu(S_k)$ nhờ Bổ đề 03.20 áp tại thời điểm cố định $k$ (biến cố $\{\tau=k\}$ chỉ phụ thuộc lịch sử tới $k$ vì $\beta_\omega$ chỉ phụ thuộc trạng thái); không dùng thuật ngữ "thời điểm dừng" khi chưa định nghĩa (quyết định Q-H); gom theo $\mu$. Sau định lý có đoạn "Trong thực hành." (Q-K). Kết quả chính của mạch 5, có trang "Ý tưởng chứng minh" (Q16).
- **Nhận xét 11.43 (Bán-MDP)**: ở các thời điểm chọn tùy chọn, quá trình là quá trình quyết định bán-Markov (thời gian lưu trú ngẫu nhiên): với mọi MDP và mọi tập tùy chọn trên nó, quá trình chỉ chọn giữa các tùy chọn và chạy mỗi tùy chọn tới khi kết thúc là một bán-MDP (SPS, Định lý 1, tr. 188; phác thảo chứng minh tr. 189). Lý thuyết bán-MDP tổng quát: Puterman (1994), theo tên chương (SPS tr. 188 và SB tr. 478 dẫn tới).

**5.3 Lập kế hoạch ở nhiều mức trừu tượng thời gian** (`cốt lõi`; giáo trình 11.4.2; SB tr. 463).

- **Ví dụ 11.26 (Lặp giá trị với tùy chọn)**: vòng 1 cho phòng phải $0{,}975610$, $0{,}856633$, phòng trái $0$; vòng 2 cho $v(\mathrm F)=0{,}856633$, $v(\mathrm B)=v(\mathrm E)=0{,}752166$, $v(\mathrm A)=0{,}660438$; vòng 3 không đổi, trùng $v_*$. Bảng so sánh lặp giá trị một bước (lượt quét 1, 2, 3, 4, 6: $v(\mathrm A)=0;\ 0;\ 0;\ 0{,}2986;\ 0{,}6103$). Câu "chi phí công bằng phải tính cả việc tính mô hình tùy chọn" đặt ở đoạn sau Thuật toán 11.45, không trỏ tới phía sau từ trong ví dụ (Đ6).
- **Định lý 11.44 (Hội tụ của lặp giá trị với tùy chọn)** — bảo đảm. Giả thiết quyết định: như Định lý 11.42; $\Omega(s)$ **hữu hạn**, khác rỗng với mọi $s$ (quyết định Q-I); mô hình tùy chọn (5.1) đúng. Kết luận: (a) $(T_\Omega V)(s)=\max_{\omega\in\Omega(s)}[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)V(s')]$ co với hệ số $\gamma$; (b) $V_{k+1}=T_\Omega V_k$ hội tụ tới điểm bất động duy nhất $v_\Omega$, $\lVert V_k-v_\Omega\rVert_\infty\le\gamma^k\lVert V_0-v_\Omega\rVert_\infty$ (bảng lặp viết chữ hoa $V_0$, $V_k$, $(T_\Omega V)(s)$; giữ $v_\Omega$, $v_*$ cho giá trị thật, quyết định Q-J); (c) $v_\Omega$ là giá trị của chính sách phân cấp tốt nhất trên $\Omega$, và nếu $\Omega(s)\supseteq\mathcal A(s)$ với mọi $s$ thì $v_\Omega=v_*$. Điều kiện áp dụng, phạm vi: với $\Omega$ chỉ gồm tùy chọn, $v_\Omega\le v_*$ và có thể nhỏ hơn ngặt. **Chứng minh**: (a), (b) **đầy đủ** (Mệnh đề 11.41 cho hệ số co, Bổ đề 04.23 cho phép cực đại với $\Omega(s)$ hữu hạn, Định lý 04.5). Tính co không cần tùy chọn kết thúc với xác suất $1$: nếu vẫn tính (5.1) cho tùy chọn có thể không kết thúc, $\sum_{s'}p(s'\mid s,\omega)\le\gamma\Pr\{\tau<\infty\}\le\gamma$ (quyết định Q-G); giả thiết đó chỉ cần cho Định lý 11.42 (tách lợi tức tại $\tau$ hữu hạn). Ghi chú nêu ý này ở đoạn sau Mệnh đề 11.41 và trong phản ví dụ "Bỏ kết thúc với xác suất $1$" sau Định lý 11.44; (c) **dẫn nguồn**: SB tr. 463 nêu lặp giá trị với tùy chọn hội tụ tới chính sách phân cấp tốt nhất, và tới chính sách tối ưu khi tập tùy chọn chứa mọi hành động một bước; SPS (10), tr. 190 định nghĩa $v_\Omega$ là giá trị tốt nhất trên các chính sách phân cấp và cho phương trình Bellman tối ưu tương ứng, (13) và đoạn sau, tr. 191, cho lặp giá trị đồng bộ và sự hội tụ $\lim_kv_k=v_\Omega$ theo lý thuyết bán-MDP; SPS không có số định lý cho phần này; vế $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$ chỉ có dạng rõ ở SB tr. 463 (SPS tr. 190 nêu giá trị tối ưu thông thường không đổi khi thêm tùy chọn); **phác thảo** một đoạn. Phân tích nguồn ghi rằng vế "$\Omega(s)\supseteq\mathcal A(s)$ thì $v_\Omega=v_*$" có thể chứng minh ngắn tại chỗ ($T_\Omega v_*\ge T_*v_*=v_*$ và mỗi số hạng của $T_\Omega v_*$ là giá trị của một chính sách nên không vượt $v_*$) nếu Bài 03–04 có kết quả "$v_*$ trội mọi chính sách, kể cả phụ thuộc lịch sử"; tác tử soạn kiểm trong ghi chú 04 (Định lý 04.25 nói tối ưu trên toàn bộ $\Pi$) và chọn chứng minh đầy đủ hay giữ phác thảo.
- **Thuật toán 11.45 (Lặp giá trị với tùy chọn)**: giả thiết $\Omega(s)$ hữu hạn, khác rỗng (Q-I); các bước như Thuật toán 04.28 với $T_\Omega$ trên bảng $V$; chi phí mỗi lượt quét $O(\sum_s\lvert\Omega(s)\rvert\cdot\lvert\mathcal S\rvert)$; đoạn sau thuật toán: tính mô hình tùy chọn cũng tốn, lợi ích đến khi dùng lại mô hình cho nhiều bài toán (SB tr. 463).
- **Ví dụ 11.27 (Một cập nhật Q-learning bán-MDP)**: tại $\mathrm B$ chạy tùy chọn đi tới cửa, kết thúc ở $\mathrm K$ sau $k=3$ bước, phần thưởng trên đường $0$, $\max_{\omega'}Q(\mathrm K,\omega')=0{,}9$, $\alpha=0{,}5$: mục tiêu $0{,}729\cdot0{,}9=0{,}6561$; giá trị mới $0{,}32805$; nhầm lẫn dùng $\gamma$ một lần cho $0{,}405$.
- **Thuật toán 11.46 (Q-learning bán-MDP)**: đầu vào tập tùy chọn với $\Omega(s)$ hữu hạn, khác rỗng (Q-I); giả thiết mọi tùy chọn kết thúc với xác suất $1$; khi tùy chọn kết thúc sau $k$ bước, $Q(s,\omega)\leftarrow Q(s,\omega)+\alpha[\sum_{j=1}^{k}\gamma^{j-1}R_j+\gamma^k\max_{\omega'}Q(S_k,\omega')-Q(s,\omega)]$ (SPS §3.2, tr. 195–196; thuật toán gốc của Bradtke và Duff, SPS dẫn). Công thức suy trực tiếp từ (17.2)–(17.4) trong ghi chú. **Không phát biểu định lý hội tụ**: SPS không có định lý cho thuật toán này; chỉ một câu định tính có nguồn, đúng như SPS: "Sutton, Precup và Singh (1999, tr. 195–196) nêu rằng ước lượng hội tụ tới giá trị tối ưu trên tập tùy chọn dưới các điều kiện tương tự Q-learning thông thường, dẫn luận án của Parr." SB tr. 462 nêu ý cập nhật từ lúc bắt đầu tới lúc kết thúc tùy chọn.
- Đoạn văn: tùy chọn chỉ giúp khi được chọn tốt; tùy chọn sai mục tiêu cho $v_\Omega<v_*$ (Bài tập 11.9 và, nếu tác giả muốn, Tình huống 11.3, Q10).
- **Trong thực hành:** tùy chọn thường do người thiết kế viết (như "đi tới cửa") hoặc học được; mô hình tùy chọn cũng phải học.

**5.4 Đọc thêm: học mô hình tùy chọn** (`đọc thêm`). **Nhận xét 11.47 (Học mô hình tùy chọn và học trong tùy chọn)**: mô hình tùy chọn là các hàm giá trị tổng quát (SB §17.1, tr. 459–461), nói bằng lời: tín hiệu tích lũy là phần thưởng, chiết khấu dừng khi tùy chọn kết thúc; không dùng chữ $C_t$ của SB (trùng $C(s,a)$), không thêm nghĩa mới cho $\gamma$; học trong tùy chọn cần học khác chính sách (SB tr. 462–463). Có thể thêm một câu có nguồn: với tập tùy chọn Markov có chính sách tất định, Q-learning trong tùy chọn một bước hội tụ với xác suất $1$ tới giá trị tối ưu trên tập tùy chọn, miễn mọi hành động được thực hiện ở mọi trạng thái vô hạn lần (SPS, Định lý 3, tr. 205); nêu đủ hai giả thiết. Văn xuôi, nhiều nhất một dòng công thức.

**Kết mục §5** (quyết định Q-M, GC15): một đoạn ngắn nêu kết quả (Định nghĩa 11.40, Định lý 11.42, 11.44; hai vòng cho $v_*(\mathrm A)=0{,}6604$ so với $0{,}6103$ sau sáu lượt quét một bước) và giới hạn (phải tính hoặc học mô hình tùy chọn; $v_\Omega=v_*$ chỉ được bảo đảm khi $\Omega(s)\supseteq\mathcal A(s)$); không nối sang bài sau (Q8).

### §6. Tổng kết (mạch 6; giáo trình 11.5; tên theo GC-RL-15)

- **6.1 So sánh bốn cách dùng mô hình**: câu mở (quyết định Q-O): cách thứ hai của §1.2, tìm kiếm lúc ra quyết định, tách theo loại hành động thành rời rạc (§3) và liên tục (§4), nên bảng có bốn hàng; §1.2 giữ tiêu đề "Ba cách dùng mô hình". Bảng `Phương pháp | Mô hình cần có | Khi nào tính | Đầu ra | Bảo đảm (số hiệu) | Sai số mô hình ảnh hưởng thế nào`, bốn hàng: Dyna-Q (Thuật toán 11.10; ô "Bảo đảm" ghi Q-planning hội tụ tới $\hat q_*$ khi mô hình cố định, xác định ở mọi cặp (Mệnh đề 11.9) và Dyna-Q không thỏa giả thiết đó (Nhận xét 11.11), quyết định Q-A); tìm kiếm theo cây Monte Carlo (Thuật toán 11.26; Mệnh đề 11.21; Định lý 11.27(a) cho UCT của Kocsis và Szepesvári với $c_{\mathrm{ucb}}=\sqrt2D$, Thuật toán 11.26 không có bảo đảm này); tối ưu bằng đạo hàm và điều khiển dự báo (Thuật toán 11.31, 11.33; Mệnh đề 11.36); lặp giá trị với tùy chọn (Thuật toán 11.45; Định lý 11.44). Nguồn của hai bảng P4 trên deck (Q16: bảng thứ ba gộp vào bảng tổng kết).
- **6.2 Trả lời bài toán trung tâm**: bốn câu trả lời có điều kiện của mục "Câu hỏi trung tâm" ở trên, văn xuôi, có số hiệu và số liệu.
- **6.3 Câu hỏi tự kiểm tra** (NT-RL-9; trả lời ngắn ngay sau mỗi câu hoặc trong khối `solution`): (1) Mệnh đề 11.9 bảo đảm hội tụ tới $q_*$ của môi trường hay của mô hình, dưới giả thiết nào; (2) vì sao tập mô hình không thấy bất định ở cặp chỉ có một mẫu (Nhận xét 11.7); (3) Mệnh đề 11.21 còn áp dụng không khi $q_{\pi_0}$ thay bằng trung bình của $m=5$ mô phỏng (Mệnh đề 11.22); (4) khi tập tùy chọn không chứa hành động một bước, lặp giá trị với tùy chọn hội tụ tới đâu (Định lý 11.44(b), (c)). Mỗi câu kiểm một giả thiết hoặc một phân biệt; mỗi câu kết bằng dấu hỏi và có lời đáp ngay (VP17), nên không là câu hỏi tu từ.
- Không câu nối sang bài sau (Q8). Bài tập tổng hợp của mạch "Tổng kết" là Bài tập 11.10 (Q13), nằm ở "Bài tập củng cố".

### Phân vai giữa §6 "Tổng kết" và "Tóm tắt chương" (Q7)

| Phần | Nội dung | Không lặp |
|---|---|---|
| §6 Tổng kết | bảng so sánh bốn phương pháp; bốn câu trả lời có điều kiện kèm số liệu; câu hỏi tự kiểm tra | không có danh sách định nghĩa theo mục, không có "Công thức cần nhớ" |
| Tóm tắt chương (GC-RL-3) | đoạn kể 5–8 câu có số hiệu; **Định nghĩa và kết quả theo mục** (§2–§5, mỗi mục một gạch); **Công thức cần nhớ**; **Giả thiết hay bị bỏ quên** | không chép lại bảng §6.1, không lặp câu trả lời §6.2; đoạn kể nêu đường đi của chương, không kể lại số liệu của §6.2 |

- **Đoạn kể** (5–8 câu): mẫu thật đắt, phép tính rẻ; mô hình đếm và hai loại bất định (Định nghĩa 11.4, 11.6, Mệnh đề 11.5); Q-planning hội tụ tới $\hat q_*$ khi mô hình cố định, xác định ở mọi cặp (Mệnh đề 11.9), Dyna-Q dùng lại mẫu (Thuật toán 11.10) mà chương không phát biểu hội tụ cho nó (Nhận xét 11.11) và thưởng thăm dò khi mô hình sai (Định nghĩa 11.12); rollout và MCTS (Mệnh đề 11.21, Thuật toán 11.26, Định lý 11.27); gradient qua mô hình và điều khiển dự báo (Mệnh đề 11.30, Định nghĩa 11.32), cái giá là sai số tích lũy (Mệnh đề 11.36); tùy chọn rút ngắn chân trời (Định lý 11.42, 11.44); giới hạn còn lại: mọi bảo đảm là theo mô hình. Không câu chỉ bài sau xử lý tiếp (Q8; khác dòng cuối của mẫu `_templates/lecture-note.md`).
- **Công thức cần nhớ**: mô hình đếm; $\operatorname{Var}\hat p=p(1-p)/n$; mục tiêu Dyna-Q+ với $\kappa\sqrt\ell$; $\sqrt{(b-1)/(bk)}$; chỉ số UCT; $\exp(-m\Delta^2/B^2)$; truy hồi ngược $\lambda_t$; $\bar e(L^k-1)/(L-1)$; $r(s,\omega)$, $p(s'\mid s,\omega)$ và phương trình Bellman phân cấp; mục tiêu Q-learning bán-MDP.
- **Giả thiết hay bị bỏ quên**: mô hình cố định, xác định ở mọi cặp (Mệnh đề 11.9, cho Q-planning, không cho Dyna-Q); mô phỏng không cắt, hoặc dùng $\Delta^D$ khi cắt (Mệnh đề 11.22); $\Omega(s)$ hữu hạn (Định lý 11.44); $q_{\pi_0}$ chính xác (Mệnh đề 11.21); $m$ chọn trước (Mệnh đề 11.22); phần thưởng trong $[0,1]$, độc lập, phân phối không đổi (Định lý 11.24); chân trời hữu hạn và hệ số thăm dò nhân $D$ (Định lý 11.27(a)); bài toán cắt ở $D=20$ và sai số cắt $\gamma^D$ (Định lý 11.27); chuỗi hành động cố định, sai số đo trên quỹ đạo dự báo (Mệnh đề 11.36); tùy chọn kết thúc với xác suất $1$ (Định lý 11.42; chứng minh của chương dùng kết thúc chỉ phụ thuộc trạng thái); $\Omega(s)\supseteq\mathcal A(s)$ mới có $v_\Omega=v_*$ (Định lý 11.44); chiết khấu $\gamma^k$ theo số bước thật (Thuật toán 11.46).

## Danh sách khối có số hiệu (bộ đếm chung 11.1–11.47)

Ký hiệu cột "Mức": Đ = chứng minh đầy đủ; P = phác thảo; N = dẫn nguồn (phát biểu theo nguồn đã kiểm, không chứng minh); — = không phải kết quả. Số định lý, phương trình, trang của bài báo chỉ ghi theo bản gốc đã kiểm (`kiem-nguon-goc.md`).

| Số | Loại, tên | Tiểu mục | Vai | Mức |
|---|---|---|---|---|
| 11.1 | Định nghĩa (Mô hình phân phối, mô hình mẫu, kinh nghiệm mô phỏng) | 2.1 | khái niệm nền | — |
| 11.2 | Định nghĩa (Lập kế hoạch nền, lập kế hoạch tại thời điểm quyết định) | 2.1 | phân biệt NT-RL-4 | — |
| 11.3 | Nhận xét (Quy hoạch động là lập kế hoạch nền với mô hình phân phối) | 2.1 | móc nối Bài 04 | — |
| 11.4 | Định nghĩa (Mô hình đếm) | 2.2 | khái niệm | — |
| 11.5 | Mệnh đề (Kỳ vọng và phương sai của xác suất ước lượng) | 2.2 | kết quả | Đ |
| 11.6 | Định nghĩa (Bất định ngẫu nhiên, bất định nhận thức) | 2.2 | khái niệm | — |
| 11.7 | Nhận xét (Tập mô hình) | 2.3 | bổ sung | — |
| 11.8 | Thuật toán (Q-planning một bước, chọn ngẫu nhiên, dạng bảng), chọn trên mọi cặp | 2.4 | thuật toán | — |
| 11.9 | Mệnh đề (Hội tụ của Q-planning), mô hình xác định ở mọi cặp | 2.4 | bảo đảm | Đ (qua Định lý 06.21) |
| 11.10 | Thuật toán (Dyna-Q dạng bảng) | 2.4 | thuật toán chính | — |
| 11.11 | Nhận xét (Dyna-Q, bộ nhớ phát lại và bảo đảm) | 2.4 | móc nối Bài 08; giới hạn của Dyna-Q chỉ định tính | — |
| 11.12 | Định nghĩa (Thưởng thăm dò của Dyna-Q+) | 2.5 | khái niệm | — |
| 11.13 | Nhận xét (Thăm dò trong lập kế hoạch) | 2.5 | giới hạn | — |
| 11.14 | Định nghĩa (Cập nhật kỳ vọng, cập nhật mẫu, hệ số phân nhánh) | 2.6 | khái niệm | — |
| 11.15 | Mệnh đề (Sai số của trung bình các cập nhật mẫu); (b) là mô hình cho công thức của SB tr. 174 | 2.6 | kết quả | Đ |
| 11.16 | Nhận xét (Điều kiện ưu tiên cập nhật mẫu) | 2.6 | áp dụng | — |
| 11.17 | Nhận xét (Quét ưu tiên) | 2.7 | đọc thêm | — |
| 11.18 | Nhận xét (Lấy mẫu theo quỹ đạo) | 2.7 | đọc thêm | — |
| 11.19 | Định lý (Hội tụ của RTDP) | 2.7 | đọc thêm | N (Barto, Bradtke và Singh 1995, qua SB tr. 178) |
| 11.20 | Thuật toán (Thuật toán rollout), đổi từ Định nghĩa, $D$ cho phép $\infty$ | 3.1 | cầu nối | — |
| 11.21 | Mệnh đề (Tính chất cải thiện của rollout) | 3.1 | bảo đảm chính mạch 3 | Đ (qua Định lý 04.13; đối chiếu Bertsekas 2020, Mệnh đề 5.4.2) |
| 11.22 | Mệnh đề (Xác suất chọn sai của rollout với $m$ mô phỏng); mô phỏng không cắt, dạng $\Delta^D$ ở Phạm vi | 3.1 | bảo đảm | Đ |
| 11.23 | Định nghĩa (Quy tắc cận tin cậy trên); UCB1 ứng với $c_{\mathrm{ucb}}=\sqrt2$ | 3.2 | cầu nối | — |
| 11.24 | Định lý (Bảo đảm của UCB1) | 3.2 | bảo đảm | N (Auer, Cesa-Bianchi và Fischer 2002, Định lý 1, tr. 237); ý tưởng một đoạn |
| 11.25 | Định nghĩa (Cây tìm kiếm, chính sách cây, thống kê cạnh); pha mô phỏng dùng $\pi_0$ | 3.3 | khái niệm | — |
| 11.26 | Thuật toán (Tìm kiếm theo cây Monte Carlo với UCT), có độ sâu cắt $D$ ($D=20$ trong ví dụ) | 3.3 | thuật toán chính | — |
| 11.27 | Định lý (Tính nhất quán của UCT cho bài toán cắt); (a) cho UCT của Kocsis và Szepesvári với $c_{\mathrm{ucb}}=\sqrt2D$, không cho Thuật toán 11.26 | 3.4 | bảo đảm | (a) N, định tính (Kocsis và Szepesvári 2006, Định lý 6); (b) Đ, $\gamma^{20}$ |
| 11.28 | Nhận xét (Xác suất tiên nghiệm và giá trị học được trong AlphaGo Zero), có công thức PUCT | 3.4 | đọc thêm (Đ8) | — |
| 11.29 | Định nghĩa (Bài toán tối ưu kế hoạch chân trời $h$, phép bắn) | 4.1 | khái niệm | — |
| 11.30 | Mệnh đề (Gradient theo chuỗi hành động bằng truy hồi ngược) | 4.2 | kết quả | Đ |
| 11.31 | Thuật toán (Tối ưu kế hoạch bằng hạ gradient) | 4.2 | thuật toán | — |
| 11.32 | Định nghĩa (Điều khiển dự báo theo chân trời lùi) | 4.3 | cầu nối | — |
| 11.33 | Thuật toán (Điều khiển dự báo) | 4.3 | thuật toán | — |
| 11.34 | Thuật toán (Tối ưu kế hoạch bằng phương pháp entropy chéo); chi tiết không gán cho Chua và cộng sự | 4.4 | bổ sung | — |
| 11.35 | Nhận xét (So sánh tối ưu bằng đạo hàm và bằng lấy mẫu) | 4.4 | bổ sung | — |
| 11.36 | Mệnh đề (Chặn sai số dự báo $k$ bước) | 4.5 | kết quả | Đ |
| 11.37 | Nhận xét (Tính bất định khi lập kế hoạch liên tục) | 4.5 | đọc thêm | — |
| 11.38 | Định nghĩa (Tùy chọn); SPS §2 | 5.1 | khái niệm | — |
| 11.39 | Định nghĩa (Chính sách phân cấp, giá trị của chính sách phân cấp) | 5.1 | khái niệm | — |
| 11.40 | Định nghĩa (Mô hình tùy chọn); SB (17.2)–(17.3), SPS (6)–(7) | 5.2 | khái niệm | — |
| 11.41 | Mệnh đề (Tổng hệ số chuyển của mô hình tùy chọn); chặn $\le\gamma$ vẫn đúng khi bỏ "kết thúc với xác suất $1$" | 5.2 | kết quả phụ | Đ |
| 11.42 | Định lý (Phương trình Bellman cho chính sách phân cấp); SB (17.4), SPS (8) | 5.2 | kết quả chính mạch 5 | Đ (cho tùy chọn Markov) |
| 11.43 | Nhận xét (Bán-MDP) | 5.2 | móc nối | N (SPS, Định lý 1, tr. 188) |
| 11.44 | Định lý (Hội tụ của lặp giá trị với tùy chọn); $\Omega(s)$ hữu hạn | 5.3 | bảo đảm | (a), (b) Đ; (c) N (SB tr. 463; SPS (10), (13), tr. 190–191), P hoặc Đ ngắn |
| 11.45 | Thuật toán (Lặp giá trị với tùy chọn); $\Omega(s)$ hữu hạn | 5.3 | thuật toán | — |
| 11.46 | Thuật toán (Q-learning bán-MDP); $\Omega(s)$ hữu hạn | 5.3 | thuật toán | không phát biểu hội tụ; một câu định tính theo SPS tr. 195–196 |
| 11.47 | Nhận xét (Học mô hình tùy chọn và học trong tùy chọn) | 5.4 | đọc thêm | có thể dẫn SPS, Định lý 3, tr. 205 |

Ví dụ 11.1–11.27 theo thứ tự xuất hiện: 11.1 (§1.1); 11.2 (§2.1); 11.3, 11.4 (§2.2); 11.5 (§2.3); 11.6, 11.7 (§2.4); 11.8, 11.9 (§2.5); 11.10, 11.11 (§2.6); 11.12–11.14 (§3.1); 11.15 (§3.2); 11.16 (§3.3); 11.17 (§4.1); 11.18, 11.19 (§4.2); 11.20 (§4.3); 11.21 (§4.4); 11.22, 11.23 (§4.5); 11.24 (§5.1); 11.25 (§5.2); 11.26, 11.27 (§5.3).

## Tình huống áp dụng và ứng dụng (GC24, GC-RL-8)

| Tình huống | Tên (chuỗi đến tay sinh viên) | Giả thiết | Kết quả dùng | Số liệu |
|---|---|---|---|---|
| 11.1 | Điều khiển dự báo cho xe trên đường ray với mô hình học bằng bình phương tối thiểu | thỏa: lớp mô hình tuyến tính chứa hệ thật, dữ liệu không nhiễu | Định nghĩa 11.29, 11.32; Mệnh đề 11.30; Thuật toán 11.33; so với Ví dụ 11.23 | ba mẫu $(2;\,0;\,2{,}4)$, $(1;\,-1;\,0{,}2)$, $(0;\,1;\,1)$; phương trình chuẩn $\sum x^2=5$, $\sum xu=-1$, $\sum u^2=2$, $\sum xx'=5$, $\sum ux'=0{,}8$; $\hat a=1{,}2$, $\hat b=1$; $u=-0{,}758824x$; $2;\ 0{,}882353;\ 0{,}389273;\ 0{,}171738$ |
| 11.2 | Dyna-Q với mô hình tất định trên mê cung có trượt | **không thỏa**: Thuật toán 11.10 giả thiết môi trường tất định, mê cung trượt với xác suất $0{,}2$ | Thuật toán 11.10; Mệnh đề 11.9 (hội tụ tới $\hat q_*$ của mô hình sai); Định nghĩa 11.4 (cách sửa) | lưu kết quả đi đúng: $1;\ 0{,}9;\ 0{,}81;\ 0{,}729$ so với $v_*$ $0{,}9756;\ 0{,}8566;\ 0{,}7522;\ 0{,}6604$, chênh tại $\mathrm A$ $0{,}0686$; lưu kết quả trượt cho $(\mathrm A,\rightarrow)$: tác tử chọn $\downarrow$ (vẫn là một đường ngắn nhất) |
| 11.3 (không bắt buộc, Q10) | Tùy chọn viết cho đích cũ khi đích đổi | không thỏa: tập tùy chọn không chứa chính sách tối ưu mới | Định lý 11.44(b), (c) | chỉ thêm nếu tác giả muốn một ví dụ số $v_\Omega<v_*$; mặc định không có |

Đoạn "Ứng dụng" cuối mục: mỗi chỗ một câu có nguồn, không liệt kê bài sau (mục 6 của `NGUYEN-TAC-HOC-PHAN.md`): MCTS trong AlphaGo và AlphaGo Zero (SB §16.6); tập mô hình cùng phương pháp entropy chéo trong PETS (Chua và cộng sự 2018). Không có bài thực hành cho Bài 11, nên phần đối chiếu bài thực hành của GC-RL-8 không áp dụng.

## Bài tập củng cố 11.1–11.11 (BT-RL-5, BT-RL-6; chi tiết đề và lời giải trong `ke-hoach-bai-tap.md` mục 2)

Ba tiểu mục; mỗi bài có `exercise`, đúng một `hint`, `solution` chia câu và dòng kiểm tra (BT5); dữ kiện chép lại trong đề (BT6, GC23). Câu cuối mục: một câu và liên kết tới `exercises.md` (Bài tập 11.12–11.19), như ghi chú 06, 10.

| Bài | Tên (chuỗi đến tay sinh viên) | Mức | Mục tiêu | Mạch | Trên deck |
|---|---|---|---|---|---|
| 11.1 | Phân loại cách dùng mô hình | nhận biết | 1, 3 | 4 (kế hoạch) | — |
| 11.2 | Hai loại bất định | nhận biết | 1 | 2 | `L11-2-04` |
| 11.3 | Hành động và tùy chọn | nhận biết | 6 | 5 | — |
| 11.4 | Bước thật đầu của lượt thứ hai trong Dyna-Q | tính toán hoặc chứng minh | 2 | 2 | `L11-2-10`, `L11-2-11` |
| 11.5 | Vòng tìm kiếm theo cây Monte Carlo tiếp theo | tính toán hoặc chứng minh | 4 | 3 | `L11-3-09`, `L11-3-10` |
| 11.6 | Kế hoạch hai bước từ $x_0=1$ | tính toán hoặc chứng minh | 5 | 4 | `L11-4-09`, `L11-4-10` |
| 11.7 | Mô hình tùy chọn khi trượt nhiều hơn | tính toán hoặc chứng minh | 6 | 5 | `L11-5-09`, `L11-5-10` |
| 11.8 | Số mô phỏng của rollout với bốn hành động | tính toán hoặc chứng minh | 4 | 3 | — |
| 11.9 | Chọn cách dùng mô hình | vận dụng | 7 | 5 | — |
| 11.10 | Mô hình đếm và tùy chọn trên mê cung hai phòng (bài tổng hợp của "Tổng kết", Q13) | vận dụng | 1, 6, 7 | 5 | `L11-6-04`, `L11-6-05` |
| 11.11 | Điều khiển dự báo với mô hình sai | vận dụng | 5, 7 | 4 | — |

Tên 11.5 sửa so với kế hoạch ("Vòng MCTS tiếp theo") để tiêu đề không dùng chữ viết tắt khi có tên tiếng Việt (VP2). Mạch của 11.1 trong kế hoạch là 4; bài phân loại bốn thủ tục của §2–§4 nên mạch 4 là mạch cấp kiến thức cuối cùng, giữ như kế hoạch.

**`exercises.md` (giai đoạn II; Q11):** 11.12 (SB Bài tập 8.2, tr. 168), 11.13 (8.3, tr. 168), 11.14 (8.6, tr. 174), 11.15 (17.1, tr. 464, kèm phát biểu lại thiết lập phần thưởng trung bình), 11.16 (8.1, tr. 166), 11.17 (8.5, tr. 168), 11.18 (2.8, tr. 36), 11.19 (8.4 [Lập trình], tr. 168; chạy thật, không thì bỏ). Bỏ SB 8.7, 8.8 (tr. 177; phần đọc thêm). Lời giải 11.18 dùng quy ước $t$ của (2.10): ở bước 12, số hạng thăm dò dùng $\ln12$.

**Bảng phủ mục tiêu** (BT9): mục tiêu 1: 11.1, 11.2, 11.10, 11.17; 2: 11.4, 11.12, 11.13, 11.16, 11.17, 11.19; 3: 11.1, 11.14; 4: 11.5, 11.8, 11.18; 5: 11.6, 11.11 (không có bài giáo trình, Q12, lý do ghi `review-log.md`); 6: 11.3, 11.7, 11.10, 11.15; 7: 11.9, 11.10, 11.11.

## Phân loại chủ đề (GC-RL-12; chỉ trong dàn ý)

| `note-topic-id` | Chủ đề | Nhóm | Lý do, nguồn |
|---|---|---|---|
| `lec-11-topic-01` | Kiến thức tiên quyết, bảng ký hiệu | cầu nối | nhắc 01.14, 01.16, Bài 03–06, 08, 10 |
| `lec-11-topic-02` | Kết quả kế thừa và bài toán trung tâm | cốt lõi | SB §8.2, Ví dụ 8.1 |
| `lec-11-topic-03` | Ba cách dùng mô hình | cốt lõi | SB §8.1, tr. 160 |
| `lec-11-topic-04` | Mô hình phân phối, mô hình mẫu; lập kế hoạch nền và tại thời điểm quyết định | cốt lõi | SB §8.1, §8.8 |
| `lec-11-topic-05` | Mô hình đếm và hai loại bất định | cốt lõi | giáo trình 11.1; SB §8.4, tr. 170; Chua và cộng sự 2018, §4 cho thuật ngữ |
| `lec-11-topic-06` | Tập mô hình | bổ sung | khoảng trống: đo bất định nhận thức khi không có công thức; nguồn chủ yếu là bài báo (Q1) |
| `lec-11-topic-07` | Q-planning và Dyna-Q | cốt lõi | SB §8.1–8.2 |
| `lec-11-topic-08` | Mô hình sai, Dyna-Q+ | cốt lõi | SB §8.3 |
| `lec-11-topic-09` | Cập nhật kỳ vọng và cập nhật mẫu | cốt lõi | SB §8.5 |
| `lec-11-topic-10` | Quét ưu tiên, lấy mẫu theo quỹ đạo, RTDP | đọc thêm | SB §8.4, §8.6, §8.7 |
| `lec-11-topic-11` | Thuật toán rollout | cầu nối | khoảng trống: giáo trình 4.3.1 chưa có bài giảng (Q3); SB §8.10, Bertsekas 2019 |
| `lec-11-topic-12` | Quy tắc cận tin cậy trên, UCB1 | cầu nối | khoảng trống: giáo trình 4.7 chưa có bài giảng (Q3); SB §2.7 |
| `lec-11-topic-13` | Bốn pha của MCTS | cốt lõi | SB §8.11 |
| `lec-11-topic-14` | Bảo đảm của UCT (cốt lõi); chi tiết AlphaGo Zero, Nhận xét 11.28 (đọc thêm) | cốt lõi; đọc thêm | Kocsis và Szepesvári 2006; SB §16.6 |
| `lec-11-topic-15` | Bài toán tối ưu kế hoạch | cốt lõi | giáo trình 11.3 |
| `lec-11-topic-16` | Đạo hàm qua mô hình | cốt lõi | giáo trình 11.3; Goodfellow và cộng sự 2016 (mục về lan truyền ngược) |
| `lec-11-topic-17` | Điều khiển dự báo theo chân trời lùi | cầu nối | khoảng trống: giáo trình 4.3.2 chưa có bài giảng (Q3); Bertsekas 2019 |
| `lec-11-topic-18` | Bắn ngẫu nhiên, phương pháp entropy chéo | bổ sung | khoảng trống: mô hình không khả vi; nguồn chủ yếu là bài báo (Q1) |
| `lec-11-topic-19` | Sai số mô hình tích lũy | cốt lõi | giáo trình 11.3 |
| `lec-11-topic-20` | Tùy chọn, chính sách phân cấp | cốt lõi | giáo trình 11.4.1; SB §17.2 |
| `lec-11-topic-21` | Mô hình tùy chọn, bán-MDP | cốt lõi | giáo trình 11.4.1; SB (17.2)–(17.4) |
| `lec-11-topic-22` | Lập kế hoạch nhiều mức, Q-learning bán-MDP | cốt lõi | giáo trình 11.4.2; SB tr. 463 |
| `lec-11-topic-23` | Học mô hình tùy chọn (tùy chọn học được) | đọc thêm | SB §17.1–17.2 |
| `lec-11-topic-24` | Tổng kết | cốt lõi | GC-RL-1, GC-RL-15 |
| `lec-11-topic-25` | Tình huống áp dụng và ứng dụng | cốt lõi | GC-RL-8 |
| `lec-11-topic-26` | Tóm tắt chương | cốt lõi | GC-RL-3 |
| `lec-11-topic-27` | Bài tập củng cố | cốt lõi | BT-RL-5 |
| `lec-11-topic-28` | Hướng dẫn đọc thêm và tài liệu tham khảo | cốt lõi | GC25 |

Theo Q1 và brief: `bổ sung` gồm tập mô hình (topic-06) và phương pháp entropy chéo (topic-18); `đọc thêm` gồm quét ưu tiên, lấy mẫu quỹ đạo, RTDP (topic-10), chi tiết AlphaZero/AlphaGo Zero (Nhận xét 11.28 trong topic-14), học mô hình tùy chọn (topic-23). Kế hoạch xếp Nhận xét 11.28 là `bổ sung`; dàn ý xếp `đọc thêm` theo brief (Đ8). Nhận xét 11.37 và đoạn PILCO là `đọc thêm` bên trong chủ đề cốt lõi topic-19, topic-16.

## Bảng thuật ngữ Việt–Anh (GC-RL-13, VP2–VP4, VP-RL-3, VP-RL-4; chỉ trong dàn ý)

Lần đầu trong ghi chú: tên tiếng Việt kèm mọi tên tiếng Anh thông dụng trong ngoặc; sau đó chỉ tên tiếng Việt. Thuật ngữ đã chốt của học phần giữ nguyên: lợi tức (return), phần thưởng (reward), lượt (episode), quỹ đạo (trajectory), lượt quét (sweep), mục tiêu bootstrap (bootstrap target), theo/khác chính sách, tác tử (agent), hầu chắc chắn, "vector" (VP-RL-8).

| Tiếng Việt | Tiếng Anh (mọi tên thông dụng) | Ghi chú |
|---|---|---|
| mô hình phân phối | distribution model | |
| mô hình mẫu | sample model | |
| kinh nghiệm mô phỏng | simulated experience | |
| lập kế hoạch | planning | Định nghĩa 01.14 |
| lập kế hoạch trong không gian trạng thái | state-space planning | |
| lập kế hoạch nền | background planning | |
| lập kế hoạch tại thời điểm quyết định | decision-time planning | |
| học tăng cường trực tiếp | direct reinforcement learning, direct RL | |
| học mô hình | model learning | |
| điều khiển tìm kiếm | search control | |
| mô hình đếm | count-based model; maximum-likelihood model | tên chốt theo Q6 |
| bất định ngẫu nhiên | aleatoric uncertainty | |
| bất định nhận thức | epistemic uncertainty | |
| tập mô hình | ensemble of models, model ensemble | |
| lấy lại mẫu có hoàn lại | bootstrap resampling | không viết "bootstrap" trơn (trùng "mục tiêu bootstrap") |
| Q-planning một bước, chọn ngẫu nhiên, dạng bảng | random-sample one-step tabular Q-planning | |
| thưởng thăm dò | exploration bonus | |
| cập nhật kỳ vọng; cập nhật mẫu | expected update; sample update | SB cũng gọi "backup" |
| hệ số phân nhánh | branching factor | |
| quét ưu tiên | prioritized sweeping | |
| lấy mẫu theo quỹ đạo | trajectory sampling | |
| phân phối theo chính sách | on-policy distribution | |
| quy hoạch động thời gian thực | real-time dynamic programming, RTDP | |
| thuật toán rollout | rollout algorithm | giữ "rollout" như mục lục giáo trình 4.3.1 (Q6) |
| chính sách cơ sở | base policy (SB: rollout policy) | $\pi_0$ (Q6) |
| chính sách rollout | rollout policy (theo Bertsekas) | $\pi_{\mathrm{ro}}$; phân biệt với "đoạn thu (rollout)" của Bài 10 (Q6) |
| quy tắc cận tin cậy trên | upper confidence bound, UCB; UCB1 | |
| hối tiếc | regret | |
| bài toán chọn lặp lại một bước | multi-armed bandit | như Bài 01 |
| tìm kiếm theo cây Monte Carlo | Monte Carlo tree search, MCTS | như mục lục giáo trình 11.2 |
| chính sách cây | tree policy | |
| chọn; mở rộng; mô phỏng; cập nhật ngược | selection; expansion; simulation; backup | "cập nhật ngược (backup)" theo Q6, tránh trùng "lan truyền ngược" |
| cận tin cậy trên áp dụng cho cây | upper confidence bounds applied to trees, UCT | |
| PUCT (quy tắc chọn có xác suất tiên nghiệm) | predictor + UCT, PUCT; prior probability | chỉ ở Nhận xét 11.28 (`đọc thêm`); $P(s,a)$, $c_{\mathrm{puct}}$ cục bộ |
| độ sâu cắt | truncation depth, search depth | $D$ (Q9); thêm so với kế hoạch |
| tối ưu kế hoạch dựa trên đạo hàm | gradient-based planning | như mục lục giáo trình 11.3 |
| tối ưu quỹ đạo | trajectory optimization | |
| phép bắn (đơn) | (single) shooting | |
| chân trời | horizon | $h$ |
| điều khiển dự báo; chân trời lùi | model predictive control, MPC; receding horizon control | như mục lục giáo trình 4.3.2 |
| vòng hở; vòng kín | open-loop; closed-loop | |
| truy hồi ngược | backward recursion | Mệnh đề 11.30 |
| lan truyền ngược | backpropagation | |
| bắn ngẫu nhiên | random shooting | |
| phương pháp entropy chéo; mẫu ưu tú | cross-entropy method, CEM; elite samples | |
| sai số tích lũy | compounding error | |
| học tăng cường phân cấp | hierarchical reinforcement learning, hierarchical RL | |
| tùy chọn | option | "tùy" theo chính tả học phần; mục lục viết "tuỳ" (Q6); xem Đ10 |
| tập khởi đầu; hàm kết thúc | initiation set; termination function, termination condition | |
| chính sách phân cấp | hierarchical policy | |
| mô hình tùy chọn | option model | |
| bán-MDP, quá trình quyết định bán-Markov | semi-Markov decision process, SMDP | "bán-MDP" có gạch nối (Q6) |
| trừu tượng thời gian | temporal abstraction | |
| hàm giá trị tổng quát | general value function, GVF | |
| học trong tùy chọn | intra-option learning | |
| đoạn thu | rollout (Bài 10) | chỉ nhắc để phân biệt |

## Giáo trình tham khảo theo mục (GC-RL-5, GC25)

Trang SB là trang in, kiểm lại ngày 2026-11-19 trên bản trích (trang PDF − 22): §2.7 bắt đầu tr. 35, (2.10) tr. 35, Hình 2.4 và Bài tập 2.8 tr. 36; §8.1 tr. 159, hộp Q-planning tr. 161; §8.2 tr. 161, sơ đồ vòng không đánh số tr. 162, Hình 8.1 tr. 163, Dyna-Q chỉ lấy mẫu cặp đã gặp tr. 163, Ví dụ 8.1 và hộp Dyna-Q tr. 164, Hình 8.2–8.3 tr. 165, Bài tập 8.1 tr. 166; §8.3 tr. 166, Ví dụ 8.2 tr. 166, Ví dụ 8.3 và Hình 8.4–8.5 tr. 167, chú thích 1 và Bài tập 8.2–8.5 tr. 168; §8.4 tr. 168–171, mô hình đếm cho môi trường ngẫu nhiên tr. 170; §8.5 tr. 172, Hình 8.7 và Bài tập 8.6 tr. 174; §8.6 tr. 174, Hình 8.8 tr. 176, Bài tập 8.7–8.8 tr. 177; §8.7 tr. 177, bốn điều kiện RTDP tr. 178; §8.8 tr. 180; §8.9 (tìm kiếm có chân trời cắt) tr. 182; §8.10 tr. 183, mục đích của rollout và so sánh với lặp chính sách, lặp giá trị bất đồng bộ tr. 184; §8.11 tr. 185, Hình 8.10 tr. 186, bốn bước tr. 187; §16.6 tr. 441, kết quả với Fan Hui và Lee Sedol tr. 442, §16.6.1 tr. 444, §16.6.2 tr. 447; §17.1 tr. 459; §17.2 tr. 461, (17.2)–(17.3) tr. 462, (17.4) tr. 463, Bài tập 17.1 tr. 464; ghi chú lịch sử: tên UCB1 tr. 44, bán-MDP và Puterman (1994) tr. 478. Nguồn đã tải ngày 2026-11-19 ghi số định lý, phương trình, mục, trang theo `kiem-nguon-goc.md` (bảng dưới). Nguồn không có bản (Hoeffding 1963, nội dung chương của Bertsekas 2019, Puterman 1994, Goodfellow và cộng sự 2016): chỉ tên tác giả, năm, tên chương hoặc tên mục; Bertsekas (2019) thêm số mục theo mục lục chính thức (Q1, Đ1).

| Mục ghi chú | Sutton và Barto (2018) | Giáo trình chuẩn khác (tên mục, không số mục chưa kiểm) | Kiểm chứng mệnh đề cụ thể (P8; trạng thái) |
|---|---|---|---|
| §1 | §8.1, tr. 159–161; §8.2, Ví dụ 8.1, Hình 8.2–8.3, tr. 164–165 | — | — |
| §2.1 | §8.1, tr. 159–160; §8.8, tr. 180–181 | — | — |
| §2.2 | §8.3, tr. 166 (nguyên nhân mô hình sai); §8.4, tr. 170 (mô hình đếm) | — | Chua và cộng sự (2018, §4, tr. 4), hai loại bất định |
| §2.3 | — | — | Chua và cộng sự (2018, §4, tr. 4–5 và chú thích Hình 1, tr. 2), tập mô hình |
| §2.4 | §8.1, tr. 161 (hộp Q-planning chọn trên mọi cặp); §8.2, tr. 161–166 (Dyna-Q chỉ lấy cặp đã gặp, tr. 163) | — | — |
| §2.5 | §8.3, tr. 166–168 | — | — |
| §2.6 | §8.5, tr. 172–174 | — | — |
| §2.7 | §8.4, tr. 168–171; §8.6, tr. 174–177; §8.7, tr. 177–180 | — | Barto, Bradtke và Singh (1995), qua SB tr. 178 |
| §3.1 | §8.10, tr. 183–185 | Bertsekas (2019), §2.4 (Rollout and the Policy Improvement Principle), §5.1.2 (Rollout), chỉ tên và số mục theo mục lục | Bertsekas (2020), Mệnh đề 5.4.2, tr. 386; Hoeffding (1963), không số định lý, số trang (không có bản) |
| §3.2 | §2.7, tr. 35–36; ghi chú lịch sử tr. 44 (tên UCB1) | Szepesvári (2010), §4.2.1 (Online learning in bandits; tr. 47–48 theo bản nháp 2009) | Auer, Cesa-Bianchi và Fischer (2002), Hình 1 và Định lý 1, tr. 237; (2), tr. 238; chứng minh tr. 242–243 |
| §3.3 | §8.11, tr. 185–188 | — | Kocsis và Szepesvári (2006), §2.2–2.3 (quy tắc UCT, $c_{t,s}=2C_p\sqrt{\ln t/s}$) |
| §3.4 | §8.9, tr. 182 và §8.11, tr. 185 (cắt độ sâu); §16.6, tr. 441–450 (tr. 442 cho kết quả thi đấu) | — | Kocsis và Szepesvári (2006), Định lý 6 (định tính; không ghi bậc, tốc độ); Kocsis, Szepesvári và Willemson (2006), bản dài, chỉ để biết không có tốc độ có ý nghĩa cho xác suất thất bại; Silver và cộng sự (2017), phần Phương pháp, mục "Select" (PUCT) |
| §4.1–4.2 | — | Goodfellow, Bengio và Courville (2016), theo tên mục về lan truyền ngược (không có bản) | Deisenroth và Rasmussen (2011), §2.3 |
| §4.3 | — | Bertsekas (2019), §2.5.1 (Model Predictive Control), chỉ tên và số mục | Bertsekas (2020), §3.1, tr. 199–201 (định nghĩa, điều kiện ổn định) |
| §4.4 | — | — | Chua và cộng sự (2018), §5, Thuật toán 1, Phụ lục A.8 (việc dùng CEM trong PETS); chi tiết thuật toán CEM không gán nguồn |
| §4.5 | — | Goodfellow, Bengio và Courville (2016), theo tên mục về phụ thuộc dài hạn (không có bản) | Deisenroth và Rasmussen (2011), tóm tắt (Nhận xét 11.37); Chua và cộng sự (2018), §4–5 |
| §5.1–5.3 | §17.2, tr. 461–464 | Puterman (1994), theo tên chương về bán-MDP (không có bản; SB tr. 478, SPS tr. 188 dẫn tới) | SPS §2, tr. 186–187; Định lý 1, tr. 188; (6)–(7), tr. 189; (8), (10), tr. 190; (13), tr. 191; §3.2, tr. 195–196 |
| §5.4 | §17.1–17.2, tr. 459–463 | — | SPS, Định lý 3, tr. 205 (tùy chọn) |
| §6, Tình huống | tổng hợp; §16.6 cho đoạn "Ứng dụng" | — | Chua và cộng sự (2018), §6, Thuật toán 1, cho PETS |

Mục "Hướng dẫn đọc thêm và tài liệu tham khảo" của ghi chú ghi tác giả, năm, tên, mục, trang (SB) hoặc tên mục (sách khác), và mục nào của chương dựa trên nguồn nào; chỉ ghi số định lý, số trang của bài báo đã kiểm. Dòng nối sang bài sau chỉ ở trang "Tài liệu tham khảo" của deck, sau khi tác giả xác nhận thứ tự Bài 12 (Q8).

## Hình SVG mới (GC12, VP10, NT25)

Thư mục `2627-1/img/lec-11/`; script vẽ trong `tools/courses/rl-plan/2627-1/img/lec-11/`. Không dùng lại 11 SVG cũ của Bài 11 cũ (`a3c-a2c-workers.svg`, `acer-acktr.svg`, `d4pg-maddpg.svg`, `ddpg-data-targets.svg`, `dpg-chain-rule.svg`, `offpolicy-corrections.svg`, `sac-td3-targets.svg`, `sam-claim-scope.svg`, `sam-parameter-neighborhood.svg`, `spo-ratio-field.svg`, `survey-three-methods.svg`); tên mới không trùng tên cũ (đã đối chiếu). Mỗi hình có `role="img"`, `<title>`, `alt` nêu đủ nội dung toán học, đoạn đọc hình trong văn bản; màu không là tín hiệu duy nhất; bản `-slide.svg` khi chữ nhỏ trên deck; không raster.

| Tệp | Nội dung | Dùng ở (ghi chú; deck dự kiến) |
|---|---|---|
| `cau-truc-chuong.svg` | khung "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách" với ba nhánh: lập kế hoạch nền; tại thời điểm quyết định (rời rạc, liên tục); trừu tượng thời gian; nhánh tối ưu kế hoạch liên tục đi thẳng từ mô hình tới hành động, không qua khâu giá trị (quyết định Q-P); ý vòng "kinh nghiệm → mô hình → lập kế hoạch → giá trị, chính sách → hành động" lấy từ sơ đồ không đánh số ở SB tr. 162 (dẫn "sơ đồ tr. 162", không gọi là Hình 8.1) | §1.2; trên deck thay bằng một dòng khung ở `L11-1-05` |
| `me-cung-hai-phong.svg` | lưới 2 × 4, tường $\mathrm B$–$\mathrm C$, cửa $\mathrm F$–$\mathrm K$, đích $\mathrm Z$, $v_*$ ghi trong ô, ghi chú trượt $0{,}2$ | Ví dụ 11.1; `L11-1-05` (bản `-slide.svg`) |
| `kien-truc-dyna.svg` | vẽ lại ý SB Hình 8.1: học trực tiếp, học mô hình, điều khiển tìm kiếm, lập kế hoạch | §2.4; `L11-2-05` |
| `cap-nhat-ky-vong-va-mau.svg` | sai số theo số phép đánh giá cho $b=2,10,100$: đường $\sqrt{(b-1)/(bk)}$ và bậc thang của cập nhật kỳ vọng tại $k=b$ | §2.6; `L11-2-09` |
| `mcts-bon-pha.svg` | cây gốc $\mathrm F$ với bốn cạnh và số liệu Ví dụ 11.16; bốn khung chọn, mở rộng, mô phỏng, cập nhật ngược | §3.3; `L11-3-05`, `L11-3-06` |
| `xe-tren-duong-ray.svg` | trục $x$, mốc $0$; quỹ đạo kế hoạch trên mô hình, vòng hở trên hệ thật, điều khiển dự báo với mô hình đúng và mô hình sai (Ví dụ 11.20, 11.23) | §4.3, §4.5; `L11-4-05`, `L11-4-08` |
| `sai-so-tich-luy.svg` | $e_k$ theo $k=1,\dots,5$ và chặn $\bar e(L^k-1)/(L-1)$ | §4.5; `L11-4-07` |
| `tuy-chon-hai-phong.svg` | mê cung với hai tùy chọn tô theo phòng, mũi tên $\pi_\omega$, hệ số $p$ và $r$ ghi cạnh ô | §5.1–5.2; `L11-5-01`, `L11-5-03` |

## Độ dài (Q5, GC-RL-4) và thời lượng

Phân bổ ban đầu (kế hoạch): phần đầu khoảng 800; §1 1 000; §2 5 000; §3 3 500; §4 3 000; §5 3 000; §6, Tình huống, Tóm tắt 1 500; tổng khoảng 17 800. Trần riêng 15 000–18 000 của Q5 đã bỏ theo quyết định của người dùng (2026-11-19); chỉ còn GC-RL-4 (8 000–30 000 từ `prose`). Đo ngày 2026-11-19 bằng `tools/courses/rl-plan/count_note_words.py 11` trên ghi chú sau biên tập vòng 1: `raw` 26 767, `prose` 21 754, "trong khoảng". Được thêm chữ để khôi phục giải thích, đoạn trực quan, bước lời giải, lý do trong chứng minh; không thêm nội dung ngoài dàn ý.

**Thời lượng** (chỉ trong dàn ý và storyboard; 120 phút trình chiếu, 30 phút chữa bài): mạch 1: 8; mạch 2: 30; mạch 3: 26; mạch 4: 24; mạch 5: 22; mạch 6: 10 (theo `ke-hoach-trang-chieu.md` mục 1). Số trang deck mục tiêu 58 theo Q15 (kế hoạch trang chiếu ghi 60; storyboard chốt).

## Quyết định của điều phối viên (2026-11-19)

Căn cứ: `quyet-dinh-I3.md`, `phan-tich-nguon.md` mục 6–7 và `kiem-nguon-goc.md` của điều phối viên (scratchpad của phiên); người dùng cho phép tải bài báo (2026-11-19). Mỗi dòng ghi quyết định và nơi đã áp trong dàn ý.

| Mã | Quyết định đã áp |
|---|---|
| Đ1 | **Đã giải quyết** (người dùng cho phép tải bài báo; kiểm trong `kiem-nguon-goc.md`). Với nguồn đã tải (Auer và cộng sự 2002; Kocsis và Szepesvári 2006 và bản dài; SPS 1999; Chua và cộng sự 2018; Silver và cộng sự 2017; Deisenroth và Rasmussen 2011; Szepesvári 2010; mục lục Bertsekas 2019; Bertsekas 2020), dàn ý ghi số định lý, phương trình, mục, trang theo báo cáo kiểm. Còn không có bản: Hoeffding (1963) dẫn tên, không số định lý, số trang; Bertsekas (2019) chỉ tên và số mục §2.4, §2.5.1, §5.1.2; Puterman (1994), Goodfellow và cộng sự (2016) theo tên chương hoặc mục; Botev và cộng sự (2013) không dẫn. Đã áp ở mục "Phạm vi và nguồn", bảng công cụ Chương 4, các khối của §2–§5, bảng khối, "Giáo trình tham khảo theo mục". |
| Đ2 | $D=20$, $\gamma^{20}=0{,}121577$ (ghi chú $0{,}1216$); Định lý 11.27(b) chứng minh đầy đủ $0\le v_*-v^D_*\le\gamma^D$ cho bài toán có phần thưởng không âm, lợi tức trong $[0,1]$, dẫn SB §8.9 tr. 182 và §8.11 tr. 185; hệ quả khoảng cách $>2\gamma^D$ chỉ thêm khi chứng minh được tại chỗ. Đã áp ở câu trả lời 2, "Giới hạn áp dụng", §3.3–3.4, bảng khối, "Giả thiết hay bị bỏ quên". |
| Đ3 | Chính sách ngoài cây của MCTS là chính sách cơ sở $\pi_0$; "chính sách rollout" chỉ cho $\pi_{\mathrm{ro}}$; Định nghĩa 11.25 đổi tên "(Cây tìm kiếm, chính sách cây, thống kê cạnh)"; một câu tương ứng SB ("rollout policy"). Đã áp ở §3.1, §3.3, bảng khối. |
| Đ4 | Bỏ câu hỏi nghiên cứu ở §1.1. Đã áp. |
| Đ5 | Bỏ câu trỏ tới Bài tập 11.19 ở Nhận xét 11.13. |
| Đ6 | Chấp nhận các cách viết không trỏ tiến: Mệnh đề 11.21 không dẫn 11.22; Thuật toán 11.33 chỉ dẫn 11.31, khả năng thay bộ giải nêu ở Thuật toán 11.34; §5.1 nêu thẳng số liệu lặp giá trị một bước; câu chi phí đặt sau Thuật toán 11.45. |
| Đ7 | Tên mục ghi chú theo mục lục giáo trình ("Tính bất định của môi trường và lập kế hoạch nền"); tên rút gọn của deck ghi ở storyboard. |
| Đ8 | Nhận xét 11.28 là `đọc thêm`. Đã áp ở §3.4, bảng khối, "Phân loại chủ đề". |
| Đ9 | Ghi chú làm tròn bốn chữ số từ giá trị chưa làm tròn: $0{,}3886$; $0{,}1814$; $0{,}1181$; $\Delta=0{,}2072$; $\exp(-70\Delta^2)=0{,}0496$; $m\ge69{,}8$. Trong dàn ý, phép tính trung gian dùng giá trị chưa làm tròn ($0{,}181398$; $0{,}118131$; $\Delta=0{,}207156$; $0{,}049591$). Đã áp ở Ví dụ 11.12, 11.14 và câu trả lời 2. |
| Đ10 | Không sửa Bài 01; điều phối viên ghi đề xuất cho tác giả vào `review-log.md`. Không thay đổi trong dàn ý. |
| Đ11 | Thay bằng quyết định của người dùng (2026-11-19): bỏ trần riêng của bài, chỉ theo GC-RL-4 (8 000–30 000 từ `prose`); ghi chú sau biên tập vòng 1 có khoảng 21 750 từ `prose`. |
| Đ12 | Giữ mục tiêu 5. |
| Phân tích nguồn | Áp toàn bộ đề xuất sửa (vai của khối 11.24 sau đó đổi lại theo dòng "Kiểm nguồn gốc"); Thuật toán 11.8 chọn trên mọi cặp và Mệnh đề 11.9 cho mô hình xác định ở mọi cặp (SB tr. 161); Nhận xét 11.11 nêu định tính giới hạn của Dyna-Q (cặp chưa thử giữ giá trị khởi tạo); Mệnh đề 11.15(b) là "mô hình cho công thức của SB tr. 174", hình ghi điểm $k=0$ là mức chuẩn hóa; không dùng $C_t$ của SB; câu sàn độ lệch chuẩn (CEM) và khởi động ấm (MPC) chỉ là lựa chọn cài đặt không tuyên bố hiệu quả, hoặc bỏ; không phát biểu bảo đảm tổng quát của điều khiển dự báo; trang: §8.4 tr. 168–171, Bài tập 8.7–8.8 tr. 177, kết quả thi đấu tr. 442, mô hình đếm tr. 170, nguyên nhân mô hình sai tr. 166, tên UCB1 tr. 44, sơ đồ không số tr. 162; "lặp giá trị bất đồng bộ" bên cạnh "lặp chính sách" (tr. 184); §2.7 phát biểu lại giáo trình 4.4.1; SB gọi $\gamma_\omega$ là hàm kết thúc; giả thiết lượt của Định lý 11.19 (tr. 178); $k$, $j$ là chỉ số cục bộ; $\ln12$ ở bước 12 của Bài tập 11.18. |
| Kiểm nguồn gốc | (1) Đ1 như trên. (2) Định lý 11.24 (Bảo đảm của UCB1) trở lại vai Định lý, dẫn nguồn không chứng minh, theo Auer và cộng sự (2002, Định lý 1): $K>1$, phần thưởng trong $[0,1]$; chặn số lần chọn $8\ln n/\Delta_a^2+1+\pi^2/3$ và chặn hối tiếc $8\sum\ln n/\Delta_a+(1+\pi^2/3)\sum\Delta_a$, ghi rõ đại lượng; UCB1 ứng với $c_{\mathrm{ucb}}=\sqrt2$, một câu về $\ln(t-1)$ so với $\ln t$. (3) Định lý 11.27(a) định tính, dẫn Kocsis và Szepesvári (2006, Định lý 6), giả thiết chân trời hữu hạn $D$, phần thưởng trong $[0,1]$, hệ số thăm dò của UCB1 nhân $D$; không "tốc độ đa thức", không bậc độ chệch; Ví dụ 11.16 thêm câu về $c_{\mathrm{ucb}}=1$; (b) giữ, dẫn thêm câu mở rộng cho MDP chiết khấu của bài ECML. (4) Định lý 11.42: phạm vi theo SPS (8) và Định lý 1 (cả tùy chọn bán-Markov); chỉ chứng minh của ghi chú dùng $\beta$ phụ thuộc trạng thái. (5) Thuật toán 11.46: không định lý hội tụ; một câu định tính theo SPS tr. 195–196 (dẫn Parr). (6) Thuật toán 11.34: Chua và cộng sự chỉ là nguồn cho việc dùng CEM trong PETS. (7) Nhận xét 11.28: công thức PUCT theo Silver và cộng sự (2017), phần Phương pháp. (8) SPS Định lý 1 (tr. 188), (6)–(10), (13), Định lý 3 (tr. 205); Chua §4–5; PILCO §2.3; Szepesvári §4.2.1 ghi vào khối và bảng tham khảo. Rollout dẫn thêm Bertsekas (2020, Mệnh đề 5.4.2); điều khiển dự báo dẫn Bertsekas (2019, §2.5.1), nội dung kiểm trên Bertsekas (2020, §3.1). |

## Sai khác so với kế hoạch

- **Kiến thức tiên quyết:** thêm Định nghĩa 03.13, Định lý 03.21, Bổ đề 04.23, Thuật toán 04.28 (đều đã tồn tại, được kế hoạch dùng ở chỗ khác) và nhóm 10 (Định nghĩa 10.11, đoạn thu của Bài 10), vì Thuật toán 11.20 phân biệt với "đoạn thu" (Q6) và Bài tập 11.16 cần lợi tức $n$ bước. Mọi số hiệu của kế hoạch đều tồn tại đúng tên. Hoeffding (1963) bỏ "Định lý 2, tr. 16" (Đ1).
- **Bảng ký hiệu:** thêm $D$ (độ sâu cắt, Q9) vào dòng $c_{\mathrm{ucb}}$, vẫn 24 dòng; thêm quy ước $k$, $j$ là chỉ số cục bộ; không dùng $C_t$; câu tương ứng với SB nói $\gamma_\omega$ là "hàm kết thúc" theo cách gọi của sách.
- **Thuật toán 11.8, Mệnh đề 11.9:** chọn trên mọi cặp, mô hình xác định ở mọi cặp (SB tr. 161), thay "tập cặp $\mathcal P$ đóng"; Nhận xét 11.11 chỉ nêu định tính giới hạn của Dyna-Q.
- **Mệnh đề 11.15(b):** ghi rõ là mô hình do học phần chọn cho công thức của SB tr. 174; hình ghi điểm $k=0$ là mức chuẩn hóa.
- **Định lý 11.24 (Bảo đảm của UCB1):** đổi tên từ "Chặn hối tiếc của UCB1"; sau lượt Đ1 từng là Nhận xét 11.24, nay trở lại vai Định lý, dẫn nguồn (Auer và cộng sự 2002, Định lý 1, tr. 237), không chứng minh. Khác kế hoạch: kế hoạch ghi $8\ln t/\Delta_a^2+1+\pi^2/3$ như chặn hối tiếc; đó là chặn cho **số lần chọn**; chặn hối tiếc có $\Delta_a$ bậc một ở mẫu số; dàn ý ghi cả hai, đúng đại lượng. Định nghĩa 11.23 ghi UCB1 ứng với $c_{\mathrm{ucb}}=\sqrt2$, kèm sai khác $\ln(t-1)$ và $\ln t$.
- **Định lý 11.27:** bài toán cắt ở $D=20$; (a) định tính, dẫn Kocsis và Szepesvári (2006, Định lý 6), giả thiết hệ số thăm dò của UCB1 nhân $D$; bỏ $O(\ln n/n)$ và "tốc độ đa thức" của kế hoạch (bản dài của chính các tác giả rút lại khẳng định tốc độ); (b) chứng minh đầy đủ chặn $\gamma^{20}=0{,}121577$, dẫn SB §8.9 tr. 182, §8.11 tr. 185 và câu mở rộng cho MDP chiết khấu của bài ECML. Ví dụ 11.16 thêm câu: $c_{\mathrm{ucb}}=1$ là hệ số của ví dụ, không phải hệ số định lý đòi hỏi.
- **Thuật toán 11.26:** tham số $D$ ($D=20$ trong ví dụ), chi phí $O(D)$ lần gọi mô hình mỗi vòng; pha mô phỏng dùng $\pi_0$.
- **Định nghĩa 11.25:** đổi tên "(Cây tìm kiếm, chính sách cây, thống kê cạnh)" (Đ3).
- **Định lý 11.42:** phạm vi sửa so với kế hoạch: SPS (8) và Định lý 1 phát biểu cả cho tùy chọn bán-Markov; chỉ chứng minh của ghi chú dùng $\beta_\omega$ phụ thuộc trạng thái (kế hoạch ghi "không áp dụng cho tùy chọn bán-Markov").
- **Định lý 11.44(c), Nhận xét 11.43, Thuật toán 11.46, Nhận xét 11.47:** 11.43 dẫn SPS Định lý 1 (tr. 188); 11.44(c) dẫn SB tr. 463 và SPS (10), (13), tr. 190–191 (SPS không có số định lý cho phần này); 11.46 không phát biểu hội tụ, một câu định tính theo SPS tr. 195–196 (dẫn Parr), khác kế hoạch (kế hoạch giả định SPS có định lý hội tụ); 11.47 có thể dẫn SPS Định lý 3 (tr. 205). Định nghĩa 11.38 thêm giả thiết $\{s:\beta_\omega(s)<1\}\subseteq\mathcal I_\omega$ (SPS tr. 186).
- **§4.3, §4.4:** không bảo đảm tổng quát cho điều khiển dự báo (Bertsekas 2020, tr. 200–201 cần ràng buộc hoặc chi phí cuối); khởi động ấm và sàn độ lệch chuẩn chỉ là lựa chọn cài đặt, hoặc bỏ. Thuật toán 11.34 phát biểu như cách cài đặt chuẩn, không gán chi tiết cho Chua và cộng sự (kế hoạch gán nguồn mô tả cho Chua); Chua (2018, §5, Thuật toán 1) chỉ là nguồn cho việc dùng CEM trong PETS.
- **Nhận xét 11.28:** thêm công thức PUCT (Silver và cộng sự 2017, phần Phương pháp, mục "Select"); kế hoạch để "cần kiểm, chưa kiểm thì chỉ nêu bằng lời".
- **Nguồn ghi số mục, số định lý mới:** Chua (2018, §4, §5); Deisenroth và Rasmussen (2011, §2.3); Szepesvári (2010, §4.2.1); Bertsekas (2019, §2.4, §2.5.1, §5.1.2, chỉ tên và số mục); Bertsekas (2020, Mệnh đề 5.4.2; §3.1); Kocsis và Szepesvári (2006, §2.2–2.3, Định lý 6); Auer và cộng sự (2002, Hình 1, Định lý 1). Kế hoạch ghi các số mục tạm "§2.4", "§2.5", "§4.2.1", "Chương 11" với chú "cần kiểm"; nay §2.4 và §4.2.1 khớp, "§2.5" thành §2.5.1, "Chương 11" của Puterman không ghi.
- **Nhận xét 11.47:** nói bằng lời, không dùng $C_t$, không thêm nghĩa cho $\gamma$.
- **Trang SB sửa:** §8.4 tr. 168–171; Bài tập 8.7–8.8 tr. 177; kết quả thi đấu của AlphaGo tr. 442; thêm tr. 44, 162, 163, 166, 170, 182, 478.
- **Số liệu:** giá trị trung gian theo bản chưa làm tròn ($0{,}181398$; $0{,}118131$; $\Delta=0{,}207156$); ghi chú làm tròn bốn chữ số (Đ9).
- **Tên khối và tiêu đề (chỉ câu chữ, VP7, VP2):** Nhận xét 11.16 "(Điều kiện ưu tiên cập nhật mẫu)"; Nhận xét 11.35 "(So sánh tối ưu bằng đạo hàm và bằng lấy mẫu)"; Nhận xét 11.28 "(… trong AlphaGo Zero)"; Định nghĩa 11.39 "(Chính sách phân cấp, giá trị của chính sách phân cấp)"; Ví dụ 11.4 "(Hai loại bất định trên $(\mathrm F,\rightarrow)$)"; Bài tập 11.5 "Vòng tìm kiếm theo cây Monte Carlo tiếp theo"; Định lý 11.24 "(Bảo đảm của UCB1)" thay "(Chặn hối tiếc của UCB1)", vì định lý chặn cả số lần chọn lẫn hối tiếc; Định nghĩa 11.25 như trên.
- **Câu hỏi trung tâm:** sửa câu chữ bằng `no-ai-slop` Edit ("đi ít bước thật", "tính thêm trên một mô hình", "phương pháp phi mô hình", "sai số của mô hình làm mất những bảo đảm nào"), giữ nghĩa và hai vế của kế hoạch. Mục tiêu 4 thêm "cho trước".
- **Phân loại:** Nhận xét 11.28 sang `đọc thêm` (Đ8).
- **Bỏ:** câu hỏi nghiên cứu ở §1.1 (Đ4); câu trỏ Bài tập 11.19 ở Nhận xét 11.13 (Đ5); các chỗ trỏ tiến (Đ6).
- **Đồng bộ với ghi chú sau biên tập vòng 1 (2026-11-19, `bang-phat-hien-I6.md`):** Định nghĩa 11.20 thành Thuật toán 11.20 (Thuật toán rollout), giữ số hiệu, $D\in\{1,2,\dots\}\cup\{\infty\}$, lượt tính tay $m=2$, $D=\infty$ đặt trong Ví dụ 11.12 (Q-B); nhãn công thức theo số mục (2.1)–(5.3) thay (11.k) (Q-C); Ví dụ 11.15 dùng $t=9$, $\ln9$, chỉ số $1{,}2051$ và $1{,}4481$ (Q-D, kế hoạch dùng $\ln8$); Ví dụ 11.16 có dữ kiện lợi tức mới, $W$ bốn chữ số ($2{,}7729$; $1{,}1875$; $0{,}3138$; $0{,}2059$), $\bar Q(\mathrm F,\uparrow)=0{,}5214$ sau cập nhật, $N(\mathrm B)=0$ (Q-E, kế hoạch ghi $N(\mathrm B)=1$), kèm câu về $c_{\mathrm{ucb}}=1$; Bài tập 11.5 theo số mới (chỉ số $1{,}4344$; $1{,}6419$; $1{,}5696$; $1{,}6882$; $W=0{,}9349$; $N(\mathrm E)=0$); Định lý 11.27(a) cho UCT của Kocsis và Szepesvári với $c_{\mathrm{ucb}}=\sqrt2D$ ($28{,}28$ khi $D=20$), hành động tối ưu duy nhất, phần thưởng trong $[0,1]$ tách khỏi lợi tức trong $[0,1]$ của (b), không cho Thuật toán 11.26 (Q-F); Mệnh đề 11.22 giả thiết mô phỏng không cắt, dạng $\Delta^D$ với $q^{20}$ ở Phạm vi và Ví dụ 11.14 (kế hoạch không có); $\Omega(s)$ hữu hạn ở 11.44–11.46 (Q-I); tính co không cần kết thúc với xác suất $1$ (Q-G); chứng minh Định lý 11.42 phân hoạch theo $\{\tau=k\}$ (Q-H); bảng lặp viết $V_k$ (Q-J); đoạn trực quan và "Trong thực hành." thêm theo Q-K; Ví dụ 11.9 đứng trước Định nghĩa 11.12, Ví dụ 11.20 đứng trước Định nghĩa 11.32 (thứ tự của ghi chú); kết mục §5 thêm (Q-M); §6.1 giải thích bốn hàng so với "Ba cách" của §1.2 (Q-O); Mệnh đề 11.9 không gán cho Dyna-Q ở §6, Tóm tắt (Q-A); tên Thuật toán 11.26 "(Tìm kiếm theo cây Monte Carlo với UCT)" và Ví dụ 11.16 "(Một vòng tìm kiếm theo cây Monte Carlo tại …)" theo ghi chú (VP2); tùy chọn viết $\omega_1$, $\omega_2$; Nhận xét 11.37 dẫn PILCO §2.2; độ dài: bỏ trần riêng (người dùng), hiện khoảng 21 750 từ `prose`.
