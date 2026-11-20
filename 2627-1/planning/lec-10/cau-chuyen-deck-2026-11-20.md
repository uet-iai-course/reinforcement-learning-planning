# Câu chuyện của deck Bài 10 (dựng lại theo TB1–TB23), 2026-11-20

Bước 1–2 của quy trình mới (`nhat-ky/su-pham-trinh-bay-2026-11-20/quy-tac-trinh-bay.md`, mục 3), chờ tác giả duyệt trước storyboard. Căn cứ: TB1–TB23 và trả lời của tác giả (câu 1–10); hai báo cáo phân tích deck 10 (`phan-tich-deck10-mach1-4.md`, `phan-tich-deck10-mach5-8.md`); `phan-tich-slide-mau.md` (Levine CS285 lec-10, lec-14; Brunskill CS234 bài 6, bài 8; Silver L7); ghi chú `materials/lec-10/lecture-note.md`. Mọi con số dưới đây đã tính lại bằng Python: các tệp `tinh.py`, `chuoi.py`, `mach4.py`, `mach6.py`, `kiem_them.py`, `hanhlang_mc.py` và kết quả `ket-qua.txt` trong `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10/cau-chuyen/`.

Ba đối tượng dùng trong cả bài, đều có trong ghi chú:

- **Hành lang ngắn** (Ví dụ 10.2): chỉ ở mở đầu, vì chỉ nó có $J(p)$ với đỉnh ở giữa, nên mới cho thấy bước đúng hướng mà quá dài làm $J$ giảm.
- **Chuỗi hai trạng thái** (Ví dụ 10.6): $s_A$ chọn 1 thì sang $s_B$ (thưởng 0), chọn 2 thì kết thúc (thưởng 1); $s_B$ chọn 1 thưởng 3, chọn 2 thưởng 0; $\gamma=0{,}9$; chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$. Dùng ở mạch 2, 3, 4 và bài tổng hợp.
- **Trạng thái $s_B$ đứng riêng** (bài toán một bước, $\pi_{\mathrm{old}}=(\tfrac23;\tfrac13)$, thưởng 3 và 0): dùng ở mạch 5 (PPO); cùng xác suất $(\tfrac23;\tfrac13)$ quay lại ở mạch 6 thành lời nhắc có hai câu trả lời.

---

## 1. Câu chuyện của bài

1. Trên hành lang ngắn, ba lượt REINFORCE cho ba hướng cập nhật khác nhau (tọa độ thứ nhất $-5{,}5$; $-1$; $1$, trong khi gradient đúng là $2$), và một bước theo đúng gradient nhưng quá dài kéo $J$ từ $-12$ xuống khoảng $-21$.
2. So lợi tức với giá trị của trạng thái thì hướng trung bình giữ nguyên mà dao động giảm; nếu một hàm giá trị (critic) đánh giá đúng, mỗi bước cho ngay hệ số đúng: trên chuỗi hai trạng thái, cả ba loại lượt cùng cho $0{,}2$.
3. Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt không lệch nhưng dao động; GAE trộn hai cách bằng một tham số $\lambda$.
4. Muốn đi bước lớn bằng dữ liệu cũ, ta đoán $J$ của chính sách mới bằng hàm thay thế; trên chuỗi, hàm thay thế báo tăng $0{,}175$ trong khi $J$ thật giảm $0{,}05$, nên chỉ được tin nó khi chính sách mới ở gần chính sách cũ: đó là miền tin cậy, mà TRPO giải bằng gradient tự nhiên.
5. PPO giữ chính sách mới ở gần bằng cách cắt tỉ số xác suất, nên chỉ cần Adam: trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$.
6. Khi chỉ có người so sánh hai câu trả lời, ta khớp phần thưởng từ các so sánh và phạt việc rời mô hình ban đầu; RLHF (dùng PPO) và DPO (một hàm mất mát phân loại) cùng đi tới một chính sách, trên ví dụ là $(\tfrac45;\tfrac15)$.

---

## 2. Các mạch

Đề xuất **7 mạch** (gồm mở đầu và tổng kết), thay cho 8 mạch hiện có: gộp mạch 4 (hàm thay thế, chặn cải thiện) và mạch 5 (TRPO) cũ thành một mạch, vì TRPO là cách giải bài toán miền tin cậy mà mạch đó dẫn tới, và trên trang chỉ còn ý "đo bước bằng độ cong của KL" cùng một sơ đồ vòng lặp (gradient liên hợp tính tay ở lại ghi chú). Thứ tự mạch vẫn theo thứ tự mục của ghi chú (P1): §1 → mạch 1; §2 → 2; §3 → 3; §4 và §5 → 4; §6 → 5; §7 → 6; §8 → 7.

### Mạch 1. Mở đầu (hành lang ngắn)

- **Câu hỏi của mạch** (trang "Vấn đề trung tâm", TB20): 1. Làm sao ước lượng gradient ít dao động hơn? 2. Làm sao đi bước lớn mà $J$ không giảm?
- **Câu chuyện.** Trên hành lang ngắn, mọi ô cùng xác suất $p=\tfrac12$ chọn "sang phải", và gradient đúng là $(2;-2)$: cần tăng $p$. Ba lượt cho ba hướng: lượt ngắn nhất (3 bước) cho $(-1;1)$, lượt 5 bước cho $(-5{,}5;5{,}5)$, lượt 4 bước cho $(1;-1)$; hai trong ba lượt đẩy $p$ xuống. Đi theo đúng gradient: bước $\alpha=0{,}1$ đưa $p$ lên $0{,}60$ và $J$ từ $-12$ lên $-11{,}7$; bước $\alpha=0{,}5$ đưa $p$ lên $0{,}88$, vượt đỉnh $p^*\approx0{,}59$, và $J$ xuống $-21{,}3$. Còn thiếu: một cách ước lượng ít dao động, và một cách chọn bước dài mà không vượt đỉnh.
- **Hiện tượng mở mạch.** (a) Trục số tọa độ thứ nhất của $\widehat g$: ba chấm $-5{,}5$; $-1$; $1$, một vạch đỏ ở $2$ (gradient đúng); cạnh đó hình hành lang với ba lượt vẽ bằng ba màu. (b) Đồ thị $J(p)$ trên $(0,1)$: điểm $p=0{,}5$ ($J=-12$), đỉnh $p^*\approx0{,}59$, hai mũi tên tới $p\approx0{,}60$ ($J\approx-11{,}7$) và $p\approx0{,}88$ ($J\approx-21{,}3$).
- **Câu hỏi nhanh** (TB22, trên trang (a), lời giải là fragment): "Lượt ngắn nhất, sang phải – sang trái – sang phải, đẩy $p$ lên hay xuống?" Lời giải: xuống, $\widehat g=(-1;1)$, vì mọi lợi tức đều âm nên mọi hành động đã chọn bị giảm xác suất, và "sang phải" được chọn hai lần.
- **Trạm dừng.** Trang "Vấn đề trung tâm" với hai hình (a), (b) thu nhỏ và hai câu hỏi.
- **Trang chữ trước ví dụ** (TB19): bìa; "Tiên quyết và quy ước" (nhắc $\widehat g=\sum_t\gamma^tG_t\psi_t$ có trung bình bằng $\nabla J$; $\psi$ của softmax hai hành động; $J(p)$ của hành lang từ Bài 09). Sau "Vấn đề trung tâm": "Mục tiêu học tập" (bốn dòng lời thường, mục 5), "Nội dung" cùng sơ đồ neo (mục 3).
- Câu hỏi thứ ba của ghi chú (phần thưởng chỉ biết qua so sánh) không đặt ở đây: sinh viên chưa thấy hiện tượng nào dẫn tới nó. Nó là câu hỏi mở mạch 6.

### Mạch 2. Đường cơ sở và critic (chuỗi hai trạng thái)

- **Dòng dẫn mạch** (TB3, nêu việc, không nêu lời giải): "Một nửa số lượt trên chuỗi hai trạng thái đẩy chính sách sai hướng."
- **Câu hỏi.** Làm sao để mỗi lượt chỉ tăng xác suất của hành động tốt hơn mức thường có ở trạng thái đó, mà trung bình vẫn bằng gradient?
- **Câu chuyện.** Trên chuỗi, lượt "$s_A$ chọn 2, nhận 1" xảy ra một nửa số lần và đẩy $p_A$ xuống, vì phần thưởng 1 dương, dù hành động 2 kém mức thường có của $s_A$ ($1<1{,}4$). Ý tưởng: lấy lợi tức trừ giá trị của trạng thái, $G_t-v(S_t)$; trung bình không đổi vì $\sum_a\pi(a\mid s)\psi(s,a)=0$, và hệ số trung bình là lợi thế $A=q-v$. Không chờ hết lượt: critic cho $\delta_t=R_{t+1}+\gamma\hat v(S_{t+1})-\hat v(S_t)$ ngay sau một bước. Kết quả: tọa độ $\theta_A$ của ước lượng trên ba loại lượt là $(1{,}35;\,0;\,-0{,}5)$, rồi $(0{,}65;\,-0{,}7;\,0{,}2)$ khi trừ $v$, rồi $(0{,}2;\,0{,}2;\,0{,}2)$ với critic đúng; trung bình luôn $0{,}2$, phương sai $0{,}69\to0{,}20\to0$. Còn thiếu: critic phải học; khi $\hat v(s_B)=1$ thay cho $2$, $\delta_0=-0{,}5$ cho hành động 1 (lợi thế thật $+0{,}4$) và gradient theo $\theta_A$ trung bình $-0{,}025$, ngược dấu.
- **Hiện tượng mở mạch.** Hình chuỗi (giá trị ghi trên hình) cạnh bảng ba hàng "loại lượt · xác suất · lợi tức · tọa độ $\theta_A$ của $\widehat g$": $s_A\!\xrightarrow1\!s_B\!\xrightarrow1$ ($\tfrac13$; $1{,}35$), $s_A\!\xrightarrow1\!s_B\!\xrightarrow2$ ($\tfrac16$; $0$), $s_A\!\xrightarrow2$ ($\tfrac12$; $-0{,}5$); vạch "đúng: $0{,}2$". Hàng thứ ba tô đỏ.
- **Trạm dừng.** Cùng bảng, dựng dần ba cột "REINFORCE · trừ $v$ · $\delta$ với critic đúng" (TB17), dưới bảng một dòng lớn "trung bình $0{,}2$ ở cả ba cột; phương sai $0{,}69$, $0{,}20$, $0$". Đây cũng là dòng thứ hai của sơ đồ neo đổi từ $G_t$ sang $G_t-v$ sang $\delta_t$.
- **Câu hỏi nhanh.** "Trừ $q(S_t,A_t)$ thay cho $v(S_t)$ có giữ trung bình không?" Lời giải: không; $b$ phụ thuộc hành động, nên trên chuỗi tọa độ $\theta_A$ trung bình thành $0$ thay cho $0{,}2$.

### Mạch 3. Ước lượng lợi thế tổng quát (chuỗi hai trạng thái, critic học dở)

- **Dòng dẫn mạch.** "Critic học dở thì đánh giá một bước bị lệch; lợi tức cả lượt thì dao động."
- **Câu hỏi.** Có cách nào ít lệch hơn đánh giá một bước mà ít dao động hơn lợi tức cả lượt không?
- **Câu chuyện.** Critic $\hat v=(1{,}4;\,1)$ đúng ở $s_A$, đánh giá thấp $s_B$. Hai lượt cùng bắt đầu bằng hành động 1 ở $s_A$: một bước cho $-0{,}5$ ở cả hai (đều, nhưng sai dấu, vì lợi thế thật là $0{,}4$); lợi tức cả lượt cho $1{,}3$ hoặc $-1{,}4$ (trung bình đúng $0{,}4$, nhưng dao động). Ý tưởng: dùng vài phần thưởng thật rồi mới dựa vào critic, và trộn các mức đó với trọng số $(\gamma\lambda)^k$: $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$, tính lùi $\widehat A_t=\delta_t+\gamma\lambda\widehat A_{t+1}$, ngắt ở bước kết thúc. Kết quả: $\lambda=0{,}5$ cho $0{,}4$ hoặc $-0{,}95$, trung bình $-0{,}05$; độ lệch là $-0{,}9(1-\lambda)$, khoảng cách hai giá trị là $2{,}7\lambda$. Còn thiếu: dao động đã giảm, nhưng mỗi lượt vẫn chỉ dùng cho một bước cập nhật nhỏ.
- **Hiện tượng mở mạch.** Bảng hai hàng (hai lượt, xác suất $\tfrac23$, $\tfrac13$) × hai cột "một bước · cả lượt", cột đúng ghi $0{,}4$; cột "một bước" tô cam (lệch), cột "cả lượt" tô xanh (dao động).
- **Trạm dừng.** Cùng bảng thêm cột $\lambda=0{,}5$ và hàng "trung bình": $-0{,}5$; $-0{,}05$; $0{,}4$. Một câu: "Với $\lambda=1$ trên lượt đầy đủ, hoặc khi critic đúng, GAE không làm lệch gradient."
- **Câu hỏi nhanh.** "Lượt bị cắt vì hết giờ ngay khi vừa tới $s_B$. Hệ số của $s_A$ dùng $0{,}9\,\hat v(s_B)$ hay $0$?" Lời giải: dùng $0{,}9\,\hat v(s_B)$, vì $s_B$ còn tương lai: $\delta_0=-0{,}5$; coi nhầm là kết thúc cho $-1{,}4$.

### Mạch 4. Hàm thay thế, miền tin cậy và TRPO (chuỗi hai trạng thái)

- **Dòng dẫn mạch.** "Muốn bước lớn, ta phải đánh giá chính sách mới trước khi chạy nó."
- **Câu hỏi.** Đoán $J$ của chính sách mới từ dữ liệu của chính sách cũ thế nào, và tin được đến đâu?
- **Câu chuyện.** Hành lang đã cho thấy bước dài làm $J$ giảm; trên chuỗi, dữ liệu của $\pi_{\mathrm{old}}$ chỉ cho biết lợi thế cũ và tần suất thăm cũ ($s_B$ được thăm ở một nửa số lượt). Hiệu $J$ của hai chính sách bằng lợi thế cũ cộng theo số lần chính sách *mới* thăm mỗi trạng thái; thay số lần thăm mới bằng số lần thăm cũ được hàm thay thế, tính được từ dữ liệu cũ. Trên chuỗi, $\Delta J=0{,}8\Delta p_A+1{,}35\Delta p_B+2{,}7\,\Delta p_A\Delta p_B$, và hàm thay thế là đúng phần tuyến tính: bước $(0{,}7;0{,}6)$ được đoán $+0{,}07$, thật $+0{,}034$; bước $(1;0{,}5)$ được đoán $+0{,}175$, thật $-0{,}05$. Sai số $2{,}7\,\Delta p_A\Delta p_B$ nhỏ khi bước ngắn, nên ta tối đa hàm thay thế trong một miền quanh chính sách cũ (miền tin cậy); TRPO đo miền đó bằng KL, gần chính sách cũ là một elip $\tfrac12\Delta^\top F\Delta\le\kappa$, và đi theo gradient tự nhiên $F^{-1}g$: trên chuỗi $g=(0{,}2;0{,}3)$ còn $F^{-1}g=(8;30)$, dồn bước về $\theta_B$ vì $s_B$ ít được thăm. Còn thiếu: mỗi bước TRPO cần tích Fisher–vector, gradient liên hợp và tìm kiếm lùi, và TRPO như cài đặt không còn bảo đảm $J$ tăng.
- **Hiện tượng mở mạch.** Hình hành lang $J(p)$ thu nhỏ (mũi tên $\alpha=0{,}5$ vượt đỉnh) cạnh hình chuỗi với hai thanh "tần suất tới $s_B$": chính sách cũ $0{,}5$, chính sách $(1;0{,}5)$ là $1$. Hộp "Câu hỏi:".
- **Hình kết quả.** Dọc đường thẳng từ $\pi_{\mathrm{old}}$ tới $(1;0{,}5)$, tham số $t\in[0,1]$: đường thẳng $\Delta\mathcal L=0{,}175t$ và parabol $\Delta J=0{,}175t-0{,}225t^2$, tiếp xúc tại $t=0$; hai điểm $t=0{,}4$ và $t=1$ ghi số. Đây là hình "hàm thay thế tiếp xúc $J$" mà báo cáo mạch 1–4 thấy thiếu.
- **Trạm dừng** (sau trang hình): công thức $\Delta J=\Delta\mathcal L+2{,}7\,\Delta p_A\Delta p_B$, câu "Hàm thay thế đoán đúng $J$ khi chính sách mới gần chính sách cũ", câu "Còn thiếu: gần đến mức nào." Câu hỏi nhanh đặt trên trang này (fragment): "Bước $(0{,}5;1)$ chỉ đổi $p_B$: hàm thay thế đoán đúng hay sai?" Lời giải: đúng, $\Delta J=\Delta\mathcal L=0{,}45$, vì $p_A$ không đổi nên số lần thăm $s_B$ không đổi.
- **Trạm dừng cuối mạch.** Sơ đồ vòng TRPO (thu dữ liệu → GAE → $g$ → gradient liên hợp chỉ cần $v\mapsto Fv$ → tìm kiếm lùi kiểm KL thật và hàm thay thế tăng) với hộp "TRPO như cài đặt không bảo đảm $J$ tăng".

### Mạch 5. PPO: mục tiêu cắt (trạng thái $s_B$)

- **Dòng dẫn mạch.** "Giữ chính sách mới ở gần mà chỉ dùng Adam."
- **Câu hỏi.** Sửa hàm mục tiêu thế nào để bộ tối ưu bậc một tự dừng khi chính sách đã đi đủ xa?
- **Câu chuyện.** Trên $s_B$ với bộ đệm ba mẫu $1,1,2$ (lợi thế $1,1,-2$), hàm thay thế mẫu là $3p-2$: tăng mãi theo $p$, nên tối ưu không ràng buộc đẩy $p$ về $1$, ra khỏi vùng nó đáng tin. Ý tưởng: cắt tỉ số $\rho=\pi/\pi_{\mathrm{old}}$ vào $[1-\epsilon,1+\epsilon]$ và lấy giá trị nhỏ hơn, để chỉ bỏ phần thưởng của việc đi quá xa, giữ nguyên phần phạt. Kết quả với $\epsilon=0{,}2$: mục tiêu cắt trùng $3p-2$ tới $p\approx0{,}73$, rồi nằm ngang từ $p=0{,}8$, gradient bằng $0$. Còn thiếu: cắt không chặn KL (nếu tham số trôi từ $p=0{,}75$ tới $0{,}85$, KL tăng từ $0{,}017$ lên $0{,}10$ trong khi gradient bằng $0$), nên PPO đo approxKL và dừng sớm; và cả TRPO lẫn PPO đều cần một hàm phần thưởng.
- **Hiện tượng mở mạch.** Đồ thị đường thẳng $3p-2$ trên $p\in[\tfrac23;1]$ với mũi tên "tăng mãi", vạch mờ "vùng hàm thay thế đáng tin" quanh $p=\tfrac23$.
- **Trạm dừng.** Cùng đồ thị, thêm đường gấp khúc (dựng dần: mốc $0{,}73$ rồi mốc $0{,}8$), rồi hình hai khung theo dấu lợi thế (theo Hình 1 của bài báo PPO), nhãn ≥ 20 px. Trạm dừng cuối mạch: bảng ba hàng so TRPO và PPO (giữ gần bằng gì, chi phí mỗi bước, bảo đảm $J$ tăng: không ở cả hai).
- **Câu hỏi nhanh.** "Mẫu chọn hành động 2 (lợi thế $-2$) có $\rho=1{,}3$ (tức $p$ đã giảm còn $0{,}57$), $\epsilon=0{,}2$: có bị cắt không?" Lời giải: không; $-2\cdot1{,}3<-2\cdot1{,}2$, phép lấy nhỏ hơn giữ $-2{,}6$, gradient khác $0$ kéo $p$ trở lại.

### Mạch 6. Học từ so sánh: RLHF và DPO (lời nhắc có hai câu trả lời)

- **Dòng dẫn mạch.** "Không có phần thưởng, chỉ có người chọn câu trả lời tốt hơn."
- **Câu hỏi.** Chính sách mới nên chọn mỗi câu trả lời với xác suất bao nhiêu, và có cần một vòng học tăng cường để tìm nó không?
- **Câu chuyện.** Mô hình hiện tại trả lời một lời nhắc bằng $y_1$ hay $y_2$ với xác suất $\tfrac23$, $\tfrac13$; sáu lần người chọn: bốn lần $y_1$, hai lần $y_2$. Khớp mô hình Bradley–Terry (xác suất người chọn là $\sigma$ của hiệu phần thưởng) cho $\hat r=(\log2;0)$; chính sách tham lam theo $\hat r$ bỏ hẳn $y_2$, nên ta trừ $\beta$ lần KL tới mô hình ban đầu, và nghiệm là $\pi^*\propto\pi_{\mathrm{ref}}e^{\hat r/\beta}=(\tfrac45;\tfrac15)$ với $\beta=1$. RLHF tìm nghiệm đó bằng PPO trên phần thưởng đã trừ KL (tại $\pi^*$ hai câu có cùng phần thưởng $0{,}51$, lợi thế bằng $0$, PPO đứng yên); DPO viết phần thưởng theo chính sách, $r=\beta\log(\pi/\pi_{\mathrm{ref}})+$ hằng, hằng triệt tiêu trong phép so sánh, nên học thẳng chính sách bằng hồi quy logistic: một bước đưa $\pi(y_1)$ từ $0{,}67$ lên $0{,}74$, rồi dần tới $0{,}8$. Còn thiếu: khi người luôn chọn một phía (sáu trên sáu), cả hai con đường đẩy $\pi(y_2)$ về $0$ với mọi $\beta$; DPO không đánh giá câu trả lời ngoài dữ liệu, RLHF thì đánh giá chúng bằng $\hat r$ có thể sai.
- **Hiện tượng mở mạch.** Hình một lời nhắc, hai thẻ câu trả lời, cột "mô hình hiện tại $\tfrac23$ · $\tfrac13$", sáu dấu chọn (4 cho $y_1$, 2 cho $y_2$). Không ký hiệu.
- **Trạm dừng.** (i) Biểu đồ cột $\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$ → $\pi^*=(\tfrac45;\tfrac15)$, cạnh khối Định lý 10.57; (ii) sơ đồ hai con đường từ dữ liệu so sánh ("khớp $\hat r$ rồi PPO", bốn mô hình; "DPO trực tiếp", hai mô hình) cùng tới $(\tfrac45;\tfrac15)$, một dòng điều kiện quyết định: "mỗi cặp được chọn theo cả hai chiều ít nhất một lần".
- **Dựng dần** (TB17, theo CS234 bài 8 tr. 46–55): ba hàng có nhãn trái "mục tiêu có phạt KL", "nghiệm", "đổi chiều", rồi "phương trình ý tưởng": mất mát trên phần thưởng + đổi biến phần thưởng ↔ chính sách = mất mát trên chính sách.
- **Câu hỏi nhanh.** "Nếu cả sáu lần người đều chọn $y_1$, $\hat r$ và $\pi^*$ ra sao?" Lời giải: hiệu $\hat r(y_1)-\hat r(y_2)$ tăng vô hạn, $\pi^*\to(1;0)$ với mọi $\beta$.

### Mạch 7. Tổng kết

- **Câu chuyện.** Sơ đồ neo lần cuối, mỗi khối một công thức; ba câu trả lời cho câu hỏi trung tâm (mục 5); một bài tổng hợp trên chuỗi nối mạch 2, 4, 5; câu hỏi tự kiểm tra về hành vi trên ví dụ; bài tập về nhà; tài liệu.
- **Bài tổng hợp đề xuất** (mới, cần tác giả duyệt, mục 7 đề xuất 6): "Trên chuỗi với lợi thế đúng $(0{,}4;-0{,}4)$ và $(1;-2)$, một vòng PPO-Clip, $\epsilon=0{,}2$, dừng ở đâu? Hàm thay thế đoán $J$ tăng bao nhiêu, $J$ thật tăng bao nhiêu?" Lời giải: tại $s_A$ hai mốc cắt trùng nhau ở $p_A=0{,}6$; tại $s_B$ mục tiêu phẳng từ $p_B=0{,}8$; chính sách $(0{,}6;0{,}8)$, đúng $\pi'$ của Ví dụ 10.11; đoán $0{,}26$, thật $0{,}296$, sai số $2{,}7\cdot0{,}1\cdot\tfrac2{15}=0{,}036$.
- **Câu hỏi tự kiểm tra** (thay ba câu của §8.4, hỏi hành vi): (1) Trên chuỗi, với critic $(1{,}4;1)$, hệ số GAE của lượt $s_A\xrightarrow1s_B\xrightarrow1$ với $\lambda=1$ là bao nhiêu? ($1{,}3$.) (2) Bước $(0{,}6;0{,}7)$: hàm thay thế đoán thấp hay cao hơn $J$ thật? (Thấp hơn: sai số $2{,}7\cdot0{,}1\cdot\tfrac1{30}=+0{,}009$.) (3) Trên $s_B$, PPO-Clip với $\epsilon=0{,}1$ dừng ở $p$ nào? ($\tfrac23\cdot1{,}1\approx0{,}73$.)

---

## 3. Sơ đồ neo (TB2)

**Hình "vòng cập nhật chính sách", năm khối, nhãn bằng lời**, vẽ một lần ở trang "Nội dung" và dùng lại thu nhỏ ở trang tiêu đề mỗi mạch (phần của mạch tô màu, phần khác mờ, theo trả lời câu 9 của tác giả).

```
 ┌──────────────┐      ┌────────────────────────────┐
 │ ① Phần thưởng │ ───▶ │ ② Thu dữ liệu bằng π_old    │
 └──────────────┘      └────────────────────────────┘
                              │                ▲
                              ▼                │ chính sách mới thành π_old
 ┌──────────────┐      ┌───────────────────┐   │
 │ ③ Critic v̂   │ ───▶ │ ④ Hệ số mỗi bước   │   │
 └──────────────┘      └───────────────────┘   │
                              │                │
                              ▼                │
                       ┌───────────────────┐   │
                       │ ⑤ Cập nhật θ       │ ──┘
                       └───────────────────┘
```

Nhãn ban đầu (mạch 1): ① "phần thưởng của môi trường"; ② "thu lượt bằng chính sách cũ"; ③ để trống, viền nét đứt (chưa có); ④ "lợi tức $G_t$"; ⑤ "một bước gradient". Mỗi mạch đổi đúng một nhãn hoặc thêm đúng một mũi tên:

| Mạch | Phần tô | Thay đổi trên sơ đồ |
|---|---|---|
| 1 | ④ và ⑤ | hai dấu "?" đỏ: ở ④ "dao động", ở ⑤ "bước dài làm $J$ giảm" |
| 2 | ③ và ④ | ③ thành khối liền "critic $\hat v$"; ④: $G_t\to G_t-v(S_t)\to\delta_t$ |
| 3 | ④ | $\delta_t\to\widehat A_t$ (trộn bằng $\lambda$) |
| 4 | ⑤ | "một bước gradient" → "tối đa hàm thay thế trong miền tin cậy (TRPO)"; thêm mũi tên ② → ⑤ "dùng lại dữ liệu cũ" |
| 5 | ⑤ | → "tối đa mục tiêu cắt, nhiều lượt qua dữ liệu (PPO)" |
| 6 | ① | "phần thưởng của môi trường" → "phần thưởng học từ so sánh, trừ phạt KL tới mô hình ban đầu (RLHF)"; thêm mũi tên nét đứt "DPO" từ dữ liệu so sánh thẳng tới ⑤, bỏ qua ①, ②, ③, ④ |
| 7 | cả hình | mỗi khối một công thức: ④ $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$; ⑤ $\min(\rho\widehat A,\operatorname{clip}(\rho)\widehat A)$; ① $\pi^*\propto\pi_{\mathrm{ref}}e^{\hat r/\beta}$; ③ $\delta_t$ |

Ở tổng kết, sơ đồ đi kèm bảng thẳng hàng kiểu Silver L7 tr. 41 (≤ 6 hàng, phần đổi tô màu): hệ số $G_t$ (REINFORCE) → $G_t-\hat v(S_t)$ → $\delta_t$ (actor–critic) → $\widehat A_t$ (GAE); cập nhật một bước → hàm thay thế trong miền tin cậy (TRPO) → mục tiêu cắt (PPO).

---

## 4. Ví dụ chạy và kiểm thông điệp (TB14–TB16)

### 4.1 Thông điệp và kiểm từng con số

| Mạch | Ví dụ | Thông điệp (một câu) | Sinh viên nhìn số sẽ kết luận | Khớp? |
|---|---|---|---|---|
| 1 | hành lang, ba lượt và hai bước | Một lượt cho hướng ngẫu nhiên; bước đúng hướng mà dài vẫn làm $J$ giảm. | $-5{,}5$; $-1$; $1$ quanh $2$: mỗi lượt một hướng, hai lượt ngược. $-12\to-11{,}7$ và $-12\to-21{,}3$: bước dài hỏng. | khớp |
| 2 | chuỗi, ba loại lượt | So với giá trị của trạng thái, hệ số ít dao động mà trung bình giữ nguyên; critic đúng cho hệ số đúng ngay. | Cột REINFORCE $1{,}35;0;-0{,}5$, cột trừ $v$ $0{,}65;-0{,}7;0{,}2$, cột $\delta$ $0{,}2;0{,}2;0{,}2$; trung bình $0{,}2$, phương sai $0{,}69$, $0{,}20$, $0$. | khớp; lưu ý ở dưới |
| 3 | chuỗi, critic $(1{,}4;1)$, hai lượt từ $(s_A,1)$ | Một bước: đều nhưng lệch; cả lượt: không lệch nhưng dao động; $\lambda$ ở giữa. | $-0{,}5;-0{,}5$ (đúng $0{,}4$); $1{,}3;-1{,}4$ (trung bình $0{,}4$); $\lambda=0{,}5$: $0{,}4;-0{,}95$ (trung bình $-0{,}05$). | khớp; lưu ý ở dưới |
| 4 | chuỗi, bước $(0{,}7;0{,}6)$ và $(1;0{,}5)$ | Hàm thay thế đoán đúng khi bước ngắn, có thể sai chiều khi bước dài đổi tần suất thăm. | $+0{,}07$ so với $+0{,}034$ (cùng chiều); $+0{,}175$ so với $-0{,}05$ (ngược chiều); sai số $-0{,}036$ rồi $-0{,}225$. | khớp |
| 5 | $s_B$, bộ đệm $1,1,2$ | Cắt bỏ phần thưởng của việc đi xa, nhưng không chặn KL. | $3p-2$ tăng tới $1$; mục tiêu cắt phẳng $0{,}27$ từ $p=0{,}8$; KL $0{,}017\to0{,}10$ khi gradient $0$. | khớp |
| 6 | lời nhắc, sáu so sánh | Hai con đường khác nhau tới cùng một chính sách. | $\tfrac46\to\hat r=(\log2;0)\to\pi^*=(0{,}8;0{,}2)$; PPO dừng ở đó (phần thưởng $0{,}51$ cả hai câu); DPO $0{,}67\to0{,}74\to\dots\to0{,}8$. | khớp |

Lưu ý khi dựng:

- **Mạch 2.** Cột "trừ $v$" làm lượt $s_A\xrightarrow1s_B\xrightarrow2$ xấu đi ($0\to-0{,}7$). Trang phải ghi phương sai của cả cột ($0{,}69\to0{,}20$) và xác suất sai dấu ($\tfrac12\to\tfrac16\to0$), nếu không sinh viên có thể kết luận đường cơ sở làm hỏng một số lượt mà không được gì. Chỉ đưa tọa độ $\theta_A$ lên trang: ở $\theta_B$ phương sai giữ $0{,}18$ ở cả ba cách (ghi ở ghi chú), nên đưa lên sẽ làm loãng thông điệp mà không sai.
- **Mạch 3.** Với $\lambda=0{,}5$, lượt đầu cho đúng $0{,}4$ một cách trùng hợp. Hàng "trung bình" ($-0{,}05$) phải có trên trang để sinh viên không kết luận "$\lambda=0{,}5$ cho kết quả đúng".
- **Mạch 6.** Không đưa lên trang hai vòng PPO của Ví dụ 10.27: vòng 1 dừng đúng ở $0{,}8$ chỉ vì $\tfrac23\cdot1{,}2=0{,}8$, dễ làm sinh viên kết luận "PPO tới $\pi^*$ sau một vòng". Trang chỉ kiểm $\pi^*$ là điểm đứng yên.
- **Ví dụ GAE hiện tại** ($\hat v=(1;1{,}5)$, một lượt): $\delta_0=0{,}35$ gần lợi thế đúng $0{,}4$ hơn hệ số Monte Carlo $1{,}7$, và trung bình hệ số Monte Carlo là $0{,}8$ chứ không phải $0{,}4$ (critic sai ở $s_A$, độ lệch như nhau cho hai hành động nên chỉ không làm lệch gradient). Cả hai điều đều ngược thông điệp, nên đề xuất đổi critic (mục 7).
- **Mạch 4, sai sót trong tệp quy tắc.** TB15 của `quy-tac-trinh-bay.md` "sửa" số của báo cáo mạch 1–4 bằng gốc $(0{,}5;0{,}5)$, $J=\mathcal L=1{,}175$. Gốc đó sai: hàm thay thế $\mathcal L=0{,}1+0{,}8p_A+1{,}35p_B$ được lập tại $\pi_{\mathrm{old}}=(0{,}5;\tfrac23)$, nơi $J=\mathcal L=1{,}4$. Tính lại: bước $(1;0{,}5)$ cho $\Delta\mathcal L=+0{,}175$, $\Delta J=-0{,}05$, tức đúng là bước hỏng, như báo cáo mạch 1–4 đã nêu; bước $(1;0{,}3)$ cho $\Delta\mathcal L=-0{,}095$, $\Delta J=-0{,}59$, không phải bước hỏng. Cần điều phối viên sửa câu đó trong tệp quy tắc.

### 4.2 Bảng số đã tính lại

**Hành lang** ($p=\tfrac12$, $\psi$ tọa độ thứ nhất $\pm\tfrac12$, $J(p)=-2(2-p)/(p(1-p))$):

| Lượt (hành động) | Trạng thái | $T$ | Xác suất | $\widehat g_1$ | $\widehat g_1$ với $b=v_\pi$ |
|---|---|---|---|---|---|
| 1, 2, 1 | $s_1,s_2,s_3$ | 3 | $\tfrac18$ | $-1$ | $3$ |
| 2, 1, 2, 1 | $s_1,s_1,s_2,s_3$ | 4 | $\tfrac1{16}$ | $1$ | $-1$ |
| 1, 1, 1, 2, 1 | $s_1,s_2,s_1,s_2,s_3$ | 5 | $\tfrac1{32}$ | $-5{,}5$ | $9{,}5$ |

$J(\tfrac12)=-12$, $J'(\tfrac12)=8$, $\nabla J=(2;-2)$; $p^*=2-\sqrt2\approx0{,}586$, $J(p^*)\approx-11{,}66$. Bước theo gradient: $\alpha=0{,}1$: $p=\sigma(0{,}4)=0{,}5987$, $J=-11{,}665$; $\alpha=0{,}5$: $p=\sigma(2)=0{,}8808$, $J=-21{,}319$. Bước theo lượt 5 bước, $\alpha=0{,}1$: $p=0{,}2497$, $J=-18{,}68$. Mô phỏng $4\cdot10^5$ lượt (chỉ để kiểm, không lên trang): phương sai tọa độ thứ nhất $727\to292$ khi trừ $v_\pi$, tỉ lệ lượt ngược chiều $0{,}49\to0{,}43$; vì vậy hành lang không dùng để minh họa đường cơ sở trên trang.

**Chuỗi, chính sách cũ** ($\gamma=0{,}9$, $p_A=\tfrac12$, $p_B=\tfrac23$): $v=(1{,}4;\,2)$, $q(s_A,\cdot)=(1{,}8;\,1)$, $A(s_A,\cdot)=(0{,}4;-0{,}4)$, $A(s_B,\cdot)=(1;-2)$, $J=2{,}7p_Ap_B+1-p_A=1{,}4$, $\nabla J=(0{,}2;0{,}3)$; $\psi(s_A,\cdot)=\pm0{,}5\,e_A$, $\psi(s_B,1)=\tfrac13e_B$, $\psi(s_B,2)=-\tfrac23e_B$.

**Mạch 2** (tọa độ $\theta_A$; $\theta_B$ trong ngoặc):

| Loại lượt | Xác suất | REINFORCE | trừ $v$ | $\delta$, critic đúng $(1{,}4;2)$ | $\delta$, critic $(1{,}4;1)$ |
|---|---|---|---|---|---|
| $s_A\xrightarrow1s_B\xrightarrow1$ | $\tfrac13$ | $1{,}35$ ($0{,}9$) | $0{,}65$ ($0{,}3$) | $0{,}2$ ($0{,}3$) | $-0{,}25$ ($0{,}6$) |
| $s_A\xrightarrow1s_B\xrightarrow2$ | $\tfrac16$ | $0$ ($0$) | $-0{,}7$ ($1{,}2$) | $0{,}2$ ($1{,}2$) | $-0{,}25$ ($0{,}6$) |
| $s_A\xrightarrow2$ | $\tfrac12$ | $-0{,}5$ ($0$) | $0{,}2$ ($0$) | $0{,}2$ ($0$) | $0{,}2$ ($0$) |
| trung bình | | $0{,}2$ ($0{,}3$) | $0{,}2$ ($0{,}3$) | $0{,}2$ ($0{,}3$) | $-0{,}025$ ($0{,}3$) |
| phương sai | | $0{,}6925$ ($0{,}18$) | $0{,}2025$ ($0{,}18$) | $0$ ($0{,}18$) | $0{,}0506$ ($0{,}09$) |

Đường cơ sở $b=q$: trung bình tọa độ $\theta_A$ bằng $\tfrac13\cdot0{,}45+\tfrac16\cdot(-0{,}9)+0=0$. Một bước actor–critic với critic $(1{,}4;1)$, $\alpha_w=0{,}5$, $\alpha_\theta=1$, lượt $s_A\xrightarrow1s_B\xrightarrow1$: $\delta_0=-0{,}5$, $w_A=1{,}15$, $\theta_A=-0{,}25$, $p_A=0{,}438$; $\delta_1=2$, $w_B=2$ (bằng $v(s_B)$), $\theta_B=\log2+0{,}6$, $p_B=0{,}785$ (chỉ cho ghi chú).

**Mạch 3** (critic $(1{,}4;1)$, lượt bắt đầu bằng hành động 1 ở $s_A$; $\delta_0=-0{,}5$, $\delta_1=2$ hoặc $-1$):

| $\lambda$ | lượt $R_2=3$ ($\tfrac23$) | lượt $R_2=0$ ($\tfrac13$) | trung bình | độ lệch so với $0{,}4$ | khoảng cách hai giá trị | gradient $\theta_A$ (cả hai hành động) |
|---|---|---|---|---|---|---|
| 0 | $-0{,}5$ | $-0{,}5$ | $-0{,}5$ | $-0{,}9$ | $0$ | $-0{,}025$ |
| 0,5 | $0{,}4$ | $-0{,}95$ | $-0{,}05$ | $-0{,}45$ | $1{,}35$ | $0{,}0875$ |
| 1 | $1{,}3$ | $-1{,}4$ | $0{,}4$ | $0$ | $2{,}7$ | $0{,}2$ |

($\lambda=0{,}8$ của ghi chú hiện tại: $0{,}94$; $-1{,}22$; trung bình $0{,}22$.) Cắt ngắn tại $s_B$: $\delta_0=0{,}9\cdot1-1{,}4=-0{,}5$; coi nhầm là kết thúc: $-1{,}4$.

**Mạch 4** ($\Delta J=0{,}8\Delta p_A+1{,}35\Delta p_B+2{,}7\Delta p_A\Delta p_B$, $\Delta\mathcal L$ là phần tuyến tính; $\nu^{\mathrm{old}}=(0{,}1;0{,}045)$; KL theo chiều cũ‖mới):

| Bước $(p'_A;p'_B)$ | $\Delta\mathcal L$ | $\Delta J$ | sai số | $D_{\mathrm{TV}}$ ($s_A$; $s_B$) | KL ($s_A$; $s_B$) | cận của Định lý 10.26 |
|---|---|---|---|---|---|---|
| $(0{,}7;0{,}6)$, $t=0{,}4$ | $0{,}07$ | $0{,}034$ | $-0{,}036$ | $0{,}2$; $0{,}067$ | $0{,}087$; $0{,}0095$ | $-0{,}758$ |
| $(1;0{,}5)$, $t=1$ | $0{,}175$ | $-0{,}05$ | $-0{,}225$ | $0{,}5$; $0{,}167$ | $\infty$; $0{,}057$ | $-5{,}0$ |
| $(0{,}6;0{,}8)$, $\pi'$ của Ví dụ 10.11 | $0{,}26$ | $0{,}296$ | $+0{,}036$ | $0{,}1$; $0{,}133$ | $0{,}020$; $0{,}049$ | $-0{,}892$ |
| $(0{,}5;1)$, câu hỏi nhanh | $0{,}45$ | $0{,}45$ | $0$ | $0$; $0{,}333$ | $0$; $\infty$ | $-2{,}25$ |
| $(0{,}6;0{,}7)$, câu tự kiểm tra | $0{,}125$ | $0{,}134$ | $+0{,}009$ | $0{,}1$; $0{,}033$ | | |

Dọc đường tới $(1;0{,}5)$: $\Delta\mathcal L=0{,}175t$, $\Delta J=0{,}175t-0{,}225t^2$; $\Delta J$ lớn nhất $0{,}034$ tại $t\approx0{,}39$, bằng $0$ tại $t\approx0{,}78$. Sai số luôn bằng $\gamma\,\Delta p_A\,A_\pi(s_B,\pi')=2{,}7\,\Delta p_A\Delta p_B$. Cận dương trên chuỗi chỉ khi bước rất nhỏ, ví dụ chỉ đổi $p_B$ với $\Delta p_B<0{,}056$ (Ví dụ 10.12). TRPO: $F=\operatorname{diag}(0{,}025;0{,}01)$, $F^{-1}g=(8;30)$, $g^\top F^{-1}g=10{,}6$. Cùng bước logit $+1$: tại $p=0{,}5$ KL $0{,}120$ (bậc hai $0{,}125$), tại $p=0{,}99$ KL $0{,}0037$ (bậc hai $0{,}0050$).

**Mạch 5** ($s_B$, bộ đệm $1,1,2$, lợi thế $1,1,-2$, $\epsilon=0{,}2$):

| $p$ | $3p-2$ | mục tiêu cắt | $\rho$ (hành động 1; 2) | approxKL | số mẫu bị cắt |
|---|---|---|---|---|---|
| $\tfrac23$ | $0$ | $0$ | $1$; $1$ | $0$ | 0/3 |
| $0{,}7333$ | $0{,}2$ | $0{,}2$ | $1{,}1$; $0{,}8$ | $0{,}011$ | 0/3 |
| $0{,}75$ | $0{,}25$ | $0{,}2167$ | $1{,}125$; $0{,}75$ | $0{,}0174$ | 1/3 |
| $0{,}8$ | $0{,}4$ | $0{,}2667$ | $1{,}2$; $0{,}6$ | $0{,}0487$ | 1/3 (hai mẫu đầu ở đúng biên) |
| $0{,}85$ | $0{,}55$ | $0{,}2667$ | $1{,}275$; $0{,}45$ | $0{,}1042$ | 3/3 |

Gradient theo logit tại $p=0{,}75$: $0{,}5625$ (không cắt), $0{,}1875$ (cắt). Trên bộ đệm có đúng tần suất của $\pi_{\mathrm{old}}$, approxKL bằng KL thật. Câu hỏi nhanh: $\rho(2)=1{,}3$ ứng với $p=0{,}567$.

**Mạch 6** ($\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$, 4 trên 6 chọn $y_1$): $L^{\mathrm{BT}}$ bằng $\log2=0{,}693$ khi hai phần thưởng bằng nhau, nhỏ nhất $0{,}6365$ tại hiệu $\log2$, $\sigma(\log2)=\tfrac23$. Với $\beta=1$: $J_1(\pi_{\mathrm{ref}})=0{,}462$; tham lam $(1;0)$: thưởng $0{,}693$, KL $0{,}405$, $J_1=0{,}288$; $(0{,}8;0{,}2)$: $0{,}555-0{,}044=0{,}511=\log\tfrac53$. $\pi^*$: $\beta=\tfrac12$: $(0{,}889;0{,}111)$; $\beta=1$: $(0{,}8;0{,}2)$; $\beta=2$: $(0{,}739;0{,}261)$. Phần thưởng đã trừ KL tại $\pi^*$: $\log2-\log1{,}2=-\log0{,}6=0{,}511$ cho cả hai câu. DPO, bước học 1: $\pi(y_1)=0{,}667;\,0{,}736;\,0{,}768;\,0{,}783;\,0{,}791;\,0{,}795$, $L^{\mathrm{DPO}}=0{,}693;\,0{,}651;\,0{,}641;\,0{,}638;\,0{,}637;\,0{,}637$, cực tiểu $0{,}6365$ tại $(0{,}8;0{,}2)$.

---

## 5. Kết quả lên trang

**Ba khối "Giả thiết/Kết luận"** (TB7, trả lời câu 1–2):

| Mạch | Khối | Giả thiết viết trên trang (bằng lời) | Lý do |
|---|---|---|---|
| 2 | Mệnh đề 10.2 (đường cơ sở không làm đổi trung bình) | $b$ chỉ phụ thuộc trạng thái, không phụ thuộc hành động đang chọn; lượt do chính $\pi_\theta$ sinh ra | Câu 2 của câu chuyện dựa vào nó; giả thiết quyết định được kiểm ngay bằng câu hỏi nhanh $b=q$ |
| 4 | Định lý 10.26 (chặn cải thiện), viết $J(\pi')-J(\pi)\ge[\mathcal L_\pi(\pi')-J(\pi)]-C\cdot$(khoảng cách TV trung bình) | lợi thế và tần suất thăm của $\pi$ tính chính xác; cùng môi trường; $\gamma<1$ | Lý do có miền tin cậy (câu 4); hằng $C$ chỉ gọi tên, công thức của $C$ để ở ghi chú diễn giả |
| 6 | Định lý 10.57 (nghiệm có phạt KL) $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ | $\beta>0$; chính sách được chọn tự do theo lời nhắc | Đích chung của RLHF và DPO (câu 6) |

Mạch 3 và 5 không có khối: mạch 3 dựa vào một bảng số, mạch 5 dựa vào đồ thị mục tiêu cắt.

**Trang ý tưởng chứng minh duy nhất** (TB7, câu 3 của tác giả): mạch 2, "$\sum_a\pi(a\mid s)\psi(s,a)=\nabla_\theta\sum_a\pi(a\mid s)=0$, nên trừ $b(s)$ không đổi trung bình", kèm số trên $s_A$: $0{,}5\cdot0{,}5+0{,}5\cdot(-0{,}5)=0$. Lý do: cùng một dòng còn giải thích vì sao lợi thế trung bình bằng 0 và vì sao GAE với $\lambda=1$ không làm lệch gradient. (Phương án khác: dòng tách $\nu'=\nu+(\nu'-\nu)$ của chặn cải thiện; trên chuỗi, đẳng thức $\Delta J=\Delta\mathcal L+2{,}7\Delta p_A\Delta p_B$ đã cho đúng ý đó mà không cần chứng minh.)

**Kết quả nêu bằng một câu lời thường** (kèm một công thức khi cần):

- Mệnh đề 10.5: "Gradient chỉ cần lợi thế: $\nabla J$ là trung bình của $A_\pi(S,A)\,\psi(S,A)$ theo các trạng thái chính sách thăm."
- Mệnh đề 10.8: "Khi critic đúng, $\delta_t$ trung bình bằng lợi thế của hành động vừa chọn; critic sai thì $\delta_t$ lệch."
- Mệnh đề 10.14: "GAE là tổng các $\delta$ với trọng số $(\gamma\lambda)^k$ và tính lùi được: $\widehat A_t=\delta_t+\gamma\lambda\widehat A_{t+1}$, ngắt ở bước kết thúc."
- Mệnh đề 10.15: "Với $\lambda=1$ trên lượt đầy đủ, hoặc khi critic đúng, GAE không làm lệch gradient."
- Bổ đề 10.19: "Hiệu $J$ của hai chính sách bằng lợi thế của chính sách cũ, cộng theo số lần chính sách mới thăm mỗi trạng thái."
- Mệnh đề 10.22: "Tại chính sách cũ, hàm thay thế bằng $J$ và có cùng độ dốc."
- Hệ quả 10.29, 10.31: "Tối đa cận dưới thì $J$ không giảm, nhưng với hằng số của lý thuyết bước gần bằng 0; miền tin cậy KL cho bước lớn, đổi lại chỉ chặn được mức giảm."
- Mệnh đề 10.33, 10.34: "Gần chính sách cũ, KL trung bình xấp xỉ $\tfrac12\Delta^\top F\Delta$; bước tốt nhất trong elip đó đi theo $F^{-1}g$."
- Nhận xét 10.38: "TRPO như cài đặt dùng ước lượng và nghiệm gần đúng, nên không còn bảo đảm $J$ tăng."
- Mệnh đề 10.40, 10.41: "Lợi thế dương thì không thưởng thêm khi $\rho>1+\epsilon$; lợi thế âm thì không thưởng thêm khi $\rho<1-\epsilon$; phía bất lợi không bị cắt. Mục tiêu cắt nằm dưới hàm thay thế và trùng nó quanh chính sách cũ."
- Nhận xét 10.42 và Mệnh đề 10.48: "Mục tiêu cắt không chặn KL, nên PPO đo approxKL và dừng sớm."
- Mệnh đề 10.54: "Khớp Bradley–Terry cho $\sigma(\hat r(y_1)-\hat r(y_2))$ bằng tỉ lệ người chọn $y_1$, khi tỉ lệ đó nằm giữa 0 và 1."
- Mệnh đề 10.63: "Mỗi chính sách là nghiệm có phạt KL của phần thưởng $\beta\log(\pi/\pi_{\mathrm{ref}})$, cộng một hằng chỉ phụ thuộc lời nhắc" (dòng thứ ba của phần dựng dần DPO).
- Định lý 10.65: "Khi mỗi cặp câu trả lời được chọn theo cả hai chiều ít nhất một lần, cực tiểu của DPO là nghiệm $\pi^*$ của RLHF."

**Ở lại ghi chú** (không lên trang, hoặc chỉ ở ghi chú diễn giả): Ví dụ 10.1 và 10.3 (bài toán một bước, phương sai $\tfrac49\to\tfrac{16}9$), Mệnh đề 10.3 (đường cơ sở tối ưu), Ví dụ 10.4 (đường cơ sở trên hành lang), Ví dụ 10.5, Thuật toán 10.6 và 10.9 dạng đầy đủ (trên trang chỉ là dòng ④ của sơ đồ neo), Nhận xét 10.10; Định nghĩa 10.11 dạng hai trường hợp, Bổ đề 10.12, Ví dụ 10.9 (γ-just), Ví dụ 10.10 (thay bằng câu hỏi nhanh trên chuỗi), Thuật toán 10.16 dạng đầy đủ; Định nghĩa 10.18 (chuẩn hóa $1-\gamma$), Hệ quả 10.20, Định nghĩa 10.23, Mệnh đề 10.24 (Pinsker), Bổ đề 10.25, Hệ quả 10.27, Nhận xét 10.28, Hệ quả 10.29 và 10.31 dạng khối, các số $-0{,}892$, $-3{,}91$ của Ví dụ 10.12; Định nghĩa 10.32 dạng tổng quát, Ví dụ 10.14, 10.15, 10.16 (gradient liên hợp tính tay), Nhận xét 10.35, Thuật toán 10.36 và 10.37 dạng chữ (trên trang là sơ đồ vòng); Ví dụ 10.18 (thành hình hai khung và câu hỏi nhanh), PPO-Penalty (Định nghĩa 10.43, Ví dụ 10.19: một câu "biến thể phạt KL với hệ số tự chỉnh"), Định nghĩa 10.45–10.47 và tính tay hàm mất mát của Ví dụ 10.20 (trên trang chỉ hàm mất mát tổng với ba ngoặc dưới), Ví dụ 10.22, §6.4–6.6 (bảng siêu tham số, chi tiết cài đặt, hội tụ); Định nghĩa 10.52(b) dạng mức token, Bổ đề 10.59, Mệnh đề 10.60, Nhận xét 10.58, hai vòng của Ví dụ 10.27, Thuật toán 10.61 dạng chữ (trên trang là sơ đồ ba giai đoạn), Mệnh đề 10.66, Thuật toán 10.67, Nhận xét 10.68–10.70 trừ ý ưu tiên tất định, §7.6; §8.1 và §8.2 (bảng giả thiết, theo trả lời câu 5).

---

## 6. Ước lượng số trang và thời lượng

Đếm theo P6 với trả lời câu 10 (chuỗi trang dựng dần cùng bố cục tính một). Thời lượng 120 phút theo đề bài.

| Mạch | Các bước chính | Trang (đếm) | Trang thật | Phút |
|---|---|---|---|---|
| 1. Mở đầu | bìa; tiên quyết; hành lang ba lượt; $J(p)$ hai bước; vấn đề trung tâm; mục tiêu; nội dung và sơ đồ neo | 7 | 7 | 10 |
| 2. Đường cơ sở và critic | tiêu đề mạch; chuỗi và ba loại lượt; cột trừ $v$; khối Mệnh đề 10.2; ý tưởng chứng minh; lợi thế; critic và $\delta$; cột $\delta$ (trạm dừng); critic sai; câu hỏi nhanh | 9 | 10 | 20 |
| 3. GAE | tiêu đề; hai lượt, một bước và cả lượt; dòng thời gian và trộn bằng $\lambda$; bảng $\lambda$ (trạm dừng); tính lùi trên đoạn thu có cờ; câu hỏi nhanh | 6 | 6 | 12 |
| 4. Hàm thay thế, miền tin cậy, TRPO | tiêu đề; hiện tượng; hiệu $J$ theo số lần thăm mới; hàm thay thế (hai công thức chồng nhau); hình $\mathcal L$ và $J$ dọc đường; trạm dừng và câu hỏi nhanh; khối chặn cải thiện; miền tin cậy; elip và gradient tự nhiên; vòng TRPO | 10 | 10 | 23 |
| 5. PPO | tiêu đề; $3p-2$ rồi đường gấp khúc (dựng dần); hai dấu lợi thế; câu hỏi nhanh; cắt không chặn KL; hàm mất mát tổng và vòng PPO; so sánh TRPO và PPO | 7 | 8 | 15 |
| 6. RLHF và DPO | tiêu đề; tình huống; Bradley–Terry; ba chính sách; khối nghiệm có phạt KL và $\beta$; RLHF ba giai đoạn, PPO đứng yên ở $\pi^*$; đổi biến (dựng dần); DPO và một bước; hai con đường; ưu tiên tất định và câu hỏi nhanh | 10 | 12 | 24 |
| 7. Tổng kết | tiêu đề; sơ đồ neo cuối và bảng thẳng hàng; ba câu trả lời; bài tổng hợp (đề, lời giải); câu hỏi tự kiểm tra và bài tập về nhà; tài liệu | 7 | 7 | 9 |
| **Tổng** | | **56** | **60** | **113** (+7 cho câu hỏi nhanh) |

Hiện có 136 trang. 56 vượt mức mặc định 45–55 của P6 một trang, dưới trần 60; lý do: bài có ba chủ đề (dao động, độ dài bước, học từ so sánh) và năm mạch nội dung.

---

## 7. Đề xuất sửa ghi chú (để tác giả duyệt cùng câu chuyện; theo trả lời câu 6, ghi chú sửa trước, deck và ghi chú cùng số)

1. **Ví dụ 10.2 (hành lang).** Thêm hai lượt: $1,2,1$ (3 bước, $\widehat g=(-1;1)$) và $2,1,2,1$ (4 bước, $\widehat g=(1;-1)$), để thông điệp về dao động có ba lượt; viết các số hiển thị là $p\approx0{,}60$, $J\approx-11{,}7$; $p\approx0{,}88$, $J\approx-21{,}3$; $p\approx0{,}25$, $J\approx-18{,}7$ (giữ số đủ ở dòng kiểm tra lại).
2. **Mục 2, chuỗi hai trạng thái.** Thêm (vào Ví dụ 10.6 hoặc thành ví dụ mới ngay sau Mệnh đề 10.2) bảng ba loại lượt với xác suất $\tfrac13$, $\tfrac16$, $\tfrac12$ và ba cột REINFORCE / trừ $v$ / $\delta$ với critic đúng (bảng mạch 2, mục 4.2), cùng phương sai $0{,}6925$, $0{,}2025$, $0$ và câu "ở $\theta_B$ phương sai giữ $0{,}18$".
3. **Đổi critic của chuỗi từ $\hat v=(1;1{,}5)$ sang $(1{,}4;1)$** (đúng ở $s_A$, đánh giá thấp $s_B$) trong đoạn sau Định nghĩa 10.7, Ví dụ 10.7, đoạn mở Mục 3, Ví dụ 10.8, 10.9, Bài tập 10.5 và Tóm tắt chương. Số mới: $\delta_0=-0{,}5$ (lợi thế đúng $0{,}4$); Ví dụ 10.7: $w_A=1{,}15$, $\theta_A=-0{,}25$, $p_A=0{,}438$, $\delta_1=2$, $w_B=2$, $p_B=0{,}785$; gradient $\theta_A$ với $\delta$: $-0{,}025$.
4. **Ví dụ 10.8:** thêm lượt thứ hai ($s_B$ chọn 2, $R_2=0$) và đổi $\lambda=0{,}8$ thành $\lambda=0{,}5$ (bảng mạch 3); Ví dụ 10.9 tính lại với critic mới ($-0{,}025$; $0{,}0875$; $0{,}2$ cho $\lambda=0;0{,}5;1$). Thêm một đoạn (sau Ví dụ 10.10) cho trường hợp cắt ngắn ngay khi tới $s_B$: $\delta_0=-0{,}5$, coi nhầm là kết thúc $-1{,}4$.
5. **Ví dụ 10.11:** thêm hai bước dọc đường tới $(1;0{,}5)$: $(0{,}7;0{,}6)$ với $\Delta\mathcal L=0{,}07$, $\Delta J=0{,}034$; $(1;0{,}5)$ với $\Delta\mathcal L=0{,}175$, $\Delta J=-0{,}05$; và đẳng thức $\Delta J=0{,}8\Delta p_A+1{,}35\Delta p_B+2{,}7\Delta p_A\Delta p_B$ (sai số $=\gamma\,\Delta p_A\,A_\pi(s_B,\pi')$), kèm hình $\mathcal L$, $J$ theo $t$. Thêm câu: tại $p'_A=1$, KL theo chiều cũ‖mới ở $s_A$ là vô hạn.
6. **Bài tập mới (bài tổng hợp ở Tổng kết):** một vòng PPO-Clip trên chuỗi với lợi thế đúng, $\epsilon=0{,}2$, dừng ở $(0{,}6;0{,}8)$; hàm thay thế $0{,}26$, $J$ thật $0{,}296$, sai số $0{,}036$. Thêm vào "Bài tập củng cố" mức vận dụng.
7. **§8.4 Câu hỏi tự kiểm tra:** thay ba câu hiện có (hỏi kết quả và giả thiết) bằng ba câu về hành vi trên ví dụ (mạch 7), hoặc thêm ba câu đó; bỏ câu dẫn "nêu kết quả đã dùng" (NT-RL-9 theo TB21, TB22).
8. **Ví dụ 10.13** (cùng bước logit, hai mức KL): gọi trạng thái là $s_B$ để giữ một đối tượng; số giữ nguyên, hiển thị $0{,}12$ và $0{,}0037$.
9. **Hai tệp quy định** (không thuộc ghi chú, báo để điều phối viên xử lý): sửa câu "lưu ý cho người dựng" trong TB15 của `quy-tac-trinh-bay.md` (mục 4.1); và quyết định 2026-11-19 "deck 10 có tám mạch, 135 phút" trong `rl-plan/NGUYEN-TAC-HOC-PHAN.md` nếu tác giả duyệt 7 mạch, 120 phút.

---

## 8. Câu hỏi cho tác giả

1. **Số mạch và thời lượng.** Dựng lại với 7 mạch và 120 phút, thay quyết định ngày 2026-11-19 (8 mạch, 135 phút)?
2. **Gộp mạch.** Gộp TRPO vào mạch hàm thay thế và miền tin cậy (mạch 4), PPO riêng (đề xuất); hay giữ TRPO riêng và gộp đường cơ sở, critic, GAE thành một mạch?
3. **Ví dụ mạch 3.** Ngày 2026-11-20 tác giả chọn giữ Ví dụ 10.10 (kết thúc và cắt ngắn) cho mạch GAE. Đề xuất này đổi sang chuỗi hai trạng thái với hai lượt (đúng thông điệp lệch và dao động), còn kết thúc và cắt ngắn thành câu hỏi nhanh trên chuỗi. Đồng ý?
4. **Critic của chuỗi.** Đổi $\hat v=(1;1{,}5)$ thành $(1{,}4;1)$ và $\lambda=0{,}8$ thành $0{,}5$ trong ghi chú (đề xuất 3–4)?
5. **Bước hỏng của mạch 4.** Chấp nhận điểm cuối $(1;0{,}5)$ (số tròn, nhưng $p'_A=1$ nên KL ở $s_A$ vô hạn), hay dùng $(0{,}9;0{,}5)$ ($\Delta\mathcal L=0{,}095$, $\Delta J=-0{,}085$)?
6. **Bài tổng hợp.** Dùng bài mới "một vòng PPO trên chuỗi dừng ở $(0{,}6;0{,}8)$" (đề xuất 6), hay một bài có sẵn (10.3 hoặc 10.21)?
7. **Trang ý tưởng chứng minh.** Chọn $\sum_a\pi\psi=0$ (đường cơ sở) hay dòng tách $\nu'=\nu+(\nu'-\nu)$ (chặn cải thiện)?
8. **Vấn đề trung tâm.** Chỉ hai câu hỏi ở mở đầu; câu hỏi về học từ so sánh đặt ở trang mở mạch 6?
9. **Hai đối tượng.** Chấp nhận hành lang chỉ ở mở đầu, chuỗi hai trạng thái từ mạch 2 tới mạch 5 và bài tổng hợp, còn $(\tfrac23;\tfrac13)$ của $s_B$ quay lại làm lời nhắc ở mạch 6?
10. **Số trang.** Chấp nhận 56 trang đếm (60 trang thật), trên mức mặc định 45–55 một trang?

---

## Quyết định của tác giả (2026-11-20)

Tác giả: "Duyệt" (sau khi xem câu chuyện liệt kê trong phiên). Điều phối viên áp các đề xuất của tệp cho mười câu hỏi ở mục 8:

1. 7 mạch, 120 phút (thay 8 mạch, 135 phút ngày 2026-11-19; đã sửa dòng P1 Bài 10 của `NGUYEN-TAC-HOC-PHAN.md`).
2. TRPO gộp vào mạch 4 (hàm thay thế, miền tin cậy); PPO là mạch riêng.
3. Mạch 3 dùng chuỗi hai trạng thái với hai lượt; kết thúc và cắt ngắn thành câu hỏi nhanh.
4. Critic của chuỗi đổi thành $(1{,}4;1)$, $\lambda=0{,}5$ trong ghi chú (đề xuất 3–4 mục 7).
5. Bước hỏng là $(1;0{,}5)$ như câu chuyện đã duyệt; thêm câu "tại $p'_A=1$, KL ở $s_A$ vô hạn" (đề xuất 5).
6. Bài tổng hợp mới: một vòng PPO-Clip trên chuỗi dừng ở $(0{,}6;0{,}8)$ (đề xuất 6).
7. Trang ý tưởng chứng minh duy nhất: $\sum_a\pi\psi=0$ (đường cơ sở không đổi trung bình), vì là lý do một dòng sinh viên cần mang về (TB7).
8. Mở đầu chỉ hai câu hỏi trung tâm; câu hỏi về học từ so sánh mở mạch 6.
9. Hành lang ở mở đầu; chuỗi hai trạng thái ở mạch 2–5 và bài tổng hợp; $(\tfrac23;\tfrac13)$ làm lời nhắc ở mạch 6.
10. Khoảng 56 trang đếm (khoảng 60 trang thật).

Bước tiếp theo: sửa ví dụ của ghi chú theo mục 7 (đề xuất 1–8), rà toán, commit; rồi storyboard theo TB1–TB23; rồi deck.

## Sửa sau cổng storyboard (2026-11-20, điều phối viên)

Câu 5 của câu chuyện và hiện tượng mở mạch 5 đổi vì bản đã duyệt nêu một vấn đề không có thật: trên $s_B$ đứng riêng, hàm thay thế $3p-2$ bằng đúng $J-J_{\mathrm{old}}$, nên "tăng mãi" không phải lỗi. Câu 5 mới: "Hàm thay thế dùng lợi thế ước lượng từ ít lượt có thể sai chiều: với bộ đệm hai lượt trên chuỗi, nó đẩy chính sách tới $(0;1)$ và $J$ giảm $0{,}4$; PPO cắt tỉ số xác suất nên dừng ở $(0{,}4;\tfrac{11}{15})$, $J$ chỉ giảm $0{,}008$, và chỉ cần Adam." Cổng kiểm lại đã tính lại các số này.

Thêm (cổng storyboard, rà toán vòng 2): bước nhỏ trên hành lang đổi từ $\alpha=0{,}1$ thành $\alpha=0{,}05$, vì $\alpha=0{,}1$ cho $p=0{,}5987$ đã vượt đỉnh $p^*\approx0{,}586$; với $\alpha=0{,}05$, $p\approx0{,}55$, $J\approx-11{,}72$, còn dưới đỉnh $-11{,}66$. Mục 2 và 4 của tệp này còn ghi $\alpha=0{,}1$: số đúng là số trong ghi chú và storyboard.
