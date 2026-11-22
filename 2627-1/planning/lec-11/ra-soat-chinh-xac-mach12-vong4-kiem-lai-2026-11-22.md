# Kiểm lại độ chính xác sau vòng sửa 4, deck Bài 11, mạch 1–2 (2026-11-22)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc), cùng vai với bốn báo cáo trước; sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** hai section đầu của deck sau vòng sửa 4, theo `sua-vong4-mach12-2026-11-22.md`.
  - Trang đổi: 1-03, 1-04, 1-06, 1-07, 1-09, 2-04, 2-06, 2-07, 2-09, 2-10, 2-13, 2-15, 2-17, 2-18; cùng 1-02, 1-05 (chỉ hình).
  - Ghi chú diễn giả: 2-03, 2-07, 2-10, 2-15, 2-19.
  - Hình: SVG mới `hai-cach-luu-slide.svg` và các SVG sửa.
- **Nguồn đối chiếu:** `materials/lec-11/lecture-note.md` (3609690).
- **Cách kiểm:**
  - `diff` mặt trang, alt và ghi chú diễn giả giữa bản vòng 3 (đã lưu ở lượt trước) và bản vòng 4.
  - Tính lại mọi số; đọc nhãn và tọa độ SVG.
  - Chụp 1600×900 chín trang (`Reveal.configure({transition:'none'})`): không lỗi trang, không `.katex-error`. Ảnh nằm trong scratchpad của phiên.

## 1. Hai phát hiện nhẹ của lượt trước

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| L11-1-06, ký hiệu $v(\cdot)$ theo $d$ chưa định nghĩa | đã sửa đúng | Mặt trang: "Với $v(d)$ là giá trị ở ô cách $\mathrm Z$ $d$ lần đi đúng tối thiểu: $v(1)=0{,}8\cdot1+0{,}2\gamma\,v(1)$ cho $v(1)=0{,}9756$; mỗi bước thêm nhân $0{,}8\gamma/(1-0{,}2\gamma)=0{,}8780$". Khớp Ví dụ 11.1 (dòng 88–90) và $\rho$ ở dòng 1338. Tính lại: $0{,}72/0{,}82=0{,}87805$; $0{,}97561\cdot0{,}87805=0{,}85663$; $\cdot0{,}87805=0{,}75217$; $\cdot0{,}87805=0{,}66044$. |
| L11-2-15, $\sigma^2$ chưa định nghĩa | đã sửa đúng | Mặt trang: $\sigma^2=\frac1b\sum_{s'}(y_{s'}-\bar y)^2$. Ghi chú diễn giả dẫn định nghĩa tổng quát của Mệnh đề 11.15(a), $\sigma^2=\sum_{s'}\hat p(s'\mid s,a)(y_{s'}-\bar y)^2$, rồi nói rõ với $b$ nhánh đồng khả năng thì bằng $\frac1b\sum$. Xem mục 3 về hệ số $\frac1b$. |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nhẹ | L11-2-06, dòng Thuật toán 11.3 | "chọn ngẫu nhiên một cặp $(S,A)$ **có mô hình**" đổi nghĩa thuật toán so với ghi chú. Thuật toán 11.3 nhận mô hình xác định ở **mọi** cặp hợp lệ và chọn trong mọi cặp hợp lệ. Câu mới để ngỏ khả năng mô hình chỉ có ở một phần các cặp, tức là bước (f) của Dyna-Q chứ không còn là Q-planning. Câu này cũng lệch với ghi chú diễn giả L11-2-07 ("Q-planning theo Thuật toán 11.3 chọn trong mọi cặp hợp lệ và cần mô hình xác định ở mọi cặp") và với giả thiết "xác định ở mọi cặp" của Mệnh đề 11.4 ở trang kế. | Thuật toán 11.3, Đầu vào và bước 1 (dòng 196, 208): "Mô hình mẫu xác định ở mọi cặp hợp lệ"; "Chọn ngẫu nhiên một cặp hợp lệ $(S,A)$ trong mọi cặp hợp lệ". Đoạn sau thuật toán (dòng 217): "Thuật toán 11.3 cần mô hình cho sẵn ở mọi cặp". | "Lặp: chọn ngẫu nhiên một cặp hợp lệ $(S,A)$; mô hình mẫu, xác định ở mọi cặp, trả $(R,S')$; …", hoặc giữ câu cũ của vòng 3. |
| nhẹ | L11-2-15, "Ý tưởng chứng minh." | Dòng này viết $\mathbb E(Q_k-\bar y)^2=\sigma^2/k$ không có điều kiện, rồi lại viết $\mathbb E\sigma^2=1-1/b$. Dưới giả thiết (b), $\sigma^2$ là biến ngẫu nhiên, nên đẳng thức thứ nhất chỉ đúng khi lấy kỳ vọng có điều kiện theo các giá trị nhánh $y$. Viết không điều kiện thì vế trái là một số, vế phải là biến ngẫu nhiên. Kết luận cuối vẫn đúng: $\mathbb E(Q_k-\bar y)^2=\mathbb E\sigma^2/k=(b-1)/(bk)$. | Chứng minh Mệnh đề 11.15, Bước 3 (dòng ~543): "$\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k$. Lấy kỳ vọng theo $y$…". Phần (a) phát biểu "với mọi giá trị cố định của các $y_{s'}$". | Viết ${\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k}$, hoặc giữ cách diễn đạt bằng lời của vòng 3 ("giữ nguyên giá trị nhánh: …"). |

Tổng phát hiện mới: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 2 nhẹ.

## 3. Các điểm điều phối viên hỏi riêng

- **$\sigma^2$ với hệ số $\frac1b$: khớp ghi chú.**
  - Mệnh đề 11.15(a) định nghĩa $\sigma^2=\sum_{s'}\hat p(s'\mid s,a)(y_{s'}-\bar y)^2$. Đây là phương sai của giá trị nhánh dưới phân phối rút, dạng chia cho số phần tử, không phải phương sai mẫu hiệu chỉnh chia $b-1$.
  - Dưới (b), $\hat p=1/b$ ở mỗi nhánh. Bước 3 của chứng minh viết đúng $\sigma^2=\frac1b\sum_{i=1}^b(y_i-\bar y)^2$, và từ đó $\mathbb E\sigma^2=(b-1)/b$. Nếu chia cho $b-1$ thì kỳ vọng sẽ bằng $1$ và công thức (2.5) không còn đúng.
  - $\operatorname{Var}\bar y=1/b$ đúng, vì $\bar y$ là trung bình $b$ biến độc lập phương sai $1$. Khi đó $\mathbb E\sigma^2=1-\operatorname{Var}\bar y=1-1/b$.
- **L11-1-09, "lưu kết cục" ở bước 4 và 5: đúng với mô hình đang dùng.**
  - Mốc bước 4 ghi "lưu (F,→) ↦ (0, K), max Q(K,·) = 0"; mốc bước 5 ghi "lưu (K,→) ↦ (+1, Z), Q(K,→) = 0,5".
  - Cả mô hình lưu kết cục gần nhất lẫn mô hình đếm đều ghi đúng các mục này, vì $(\mathrm F,\rightarrow)$ và $(\mathrm K,\rightarrow)$ mỗi cặp có một lần thử. Lượt bấm 3 gọi mô hình tại $(\mathrm F,\rightarrow)$ trả $(0,\mathrm K)$, khớp mục đã lưu.
  - Mốc bước 4 nằm trước bước 5, nên $\max_aQ(\mathrm K,a)=0$ lúc đó là đúng.
  - Thứ tự dựng dần đúng: (1) bước 5 cho $0{,}5$; (2) câu hỏi về mục tiêu; (3) $0{,}9\cdot0{,}5=0{,}45$, rồi $0+0{,}5[0{,}45-0]=0{,}225$.
- **L11-1-07, bảng $Q(\mathrm F,\cdot)$ hai hàng: đúng.** Hàng Q-learning: bốn ô bằng $0$, vì $(\mathrm F,\rightarrow)$ được cập nhật ở bước 4 với mục tiêu $0$ và các hành động khác tại $\mathrm F$ chưa thử. Hàng "lượt lấy mẫu đã chọn": $0;0;0;0{,}225$, vì bước 1–4 lập kế hoạch đều cho mục tiêu $0$, còn bước 5 chỉ sửa $(\mathrm F,\rightarrow)$ (Ví dụ 11.6).
- **L11-2-04, ba cột: đúng.** $P(\hat p=0)=0{,}2^2=0{,}04$, $P(\hat p=0{,}5)=2\cdot0{,}8\cdot0{,}2=0{,}32$, $P(\hat p=1)=0{,}64$. Chiều cao cột trong SVG là $2{,}8;\,22{,}4;\,44{,}8$, đúng tỉ lệ $1:8:16$. Độ lệch chuẩn $\sqrt{0{,}72-0{,}64}=0{,}2828$.
- **L11-2-07, dải "đếm kết cục" / "giữ kết cục gần nhất": đúng.** Thẻ đếm cho ① $(0,\mathrm A)$: $1\to1/2$, ② $(0,\mathrm B)$: $1\to1/2$. Thẻ "giữ kết cục gần nhất": ① bị ghi đè, ② $(0,\mathrm B)$ được giữ. Khớp Ví dụ 11.2 và Ví dụ 11.6 ("Bốn bước đầu", "Mô hình đếm"). Câu đầu trang "Mệnh đề 11.4 cần mô hình cố định, đủ mọi cặp" đúng.
- **L11-2-17, chấm ở B, ô F: đúng với Bài tập 11.4.** Sau bước thật $(\mathrm A,\rightarrow,0,\mathrm B)$, $S'=\mathrm B$; cặp đầu tiên bước chọn cặp lấy là $(\mathrm F,\rightarrow)$.
- **L11-2-18, Robbins–Monro: đúng.** Ví dụ $\alpha_j=1/j$ ở lần cập nhật thứ $j$ của cặp thỏa $\sum_j1/j=\infty$ và $\sum_j1/j^2=\pi^2/6<\infty$, khớp Định nghĩa 06.19 (chỉ số theo lần cập nhật của cặp).

## 4. Trang và hình đã kiểm

| trang | kết luận | số và nhãn đã kiểm |
|---|---|---|
| L11-1-02 (`mo-hinh-hai-dang-slide.svg`) | không lỗi | hộp nổi bật "ví dụ: mô hình khớp luật mê cung"; $0{,}8$/$0{,}2$ |
| L11-1-03 | không lỗi | $\sqrt{50/5}=3{,}162$; $0{,}4/\sqrt5=0{,}1789$, $0{,}4/\sqrt{50}=0{,}0566$; mục 3: với $10<100$ lần đánh giá chỉ cập nhật mẫu thực hiện được (Ví dụ 11.11) |
| L11-1-04 | không lỗi | "so sánh $\downarrow$ và $\rightarrow$ với $m$ mô phỏng mỗi hành động: chặn xác suất xếp nhầm $\downarrow$ cao hơn $\rightarrow$" là (3.1) cho một cặp |
| L11-1-05 (`so-do-neo-slide.svg`) | không lỗi | nhánh 4 "tối ưu chuỗi hành động giá trị thực" |
| L11-1-06 (`me-cung-luat-slide.svg`, `me-cung-gia-tri-slide.svg`) | không lỗi | như mục 1 |
| L11-1-07 | không lỗi | như mục 3 |
| L11-1-09 (`luot-mot-q-learning-slide.svg`, `luot-mot-ql-ket-qua-slide.svg`, `luot-mot-ke-hoach-slide.svg`) | không lỗi | như mục 3; nhãn "chọn (F,→), mục tiêu 0,45", "Q(F,→) = 0,225" |
| L11-2-03 (ghi chú diễn giả) | không lỗi | gộp bảng đếm theo kết cục $(R,S')$ theo $r$ cho $C(s,a,s')$, $\hat p$; trung bình $R$ cho $\hat r$; khớp Định nghĩa 11.1 |
| L11-2-04 (`hai-loai-bat-dinh-A-slide.svg`) | không lỗi | như mục 3; hai mốc cũ không đổi |
| L11-2-06 | một nhẹ | các số không đổi: $0{,}45$, $0{,}225$ |
| L11-2-07 (`hai-cach-luu-slide.svg`) | không lỗi | như mục 3; hàng 5: $0{,}5$, $0{,}225$, $0{,}75$. Ghi chú diễn giả: "một cập nhật vẫn chạy được khi chọn cặp đã thử; bước (f) làm đúng như vậy" là đúng |
| L11-2-09 (`chuoi-thuong-tham-do-slide.svg`) | không lỗi | "thưởng chỉ cộng ở (f)" khớp câu sau Định nghĩa 11.11; nhánh $0{,}2$ "lại (0, B)"; "ℓ ← 0 cả khi trượt" khớp Định nghĩa 11.11 |
| L11-2-10 (`so-do-cap-nhat-hai-lan-thu-slide.svg`) | không lỗi | "đếm kết cục của (A,→); các giá trị max Q là giả sử". Ghi chú diễn giả: $Q_1=0{,}54$, $Q_2=0{,}54+0{,}5(0{,}36-0{,}54)=0{,}45=\bar y$; rút B hai lần cho $0{,}54$ |
| L11-2-13 (`hai-gioi-han-duong-di-slide.svg`) | không lỗi | "giả sử mô hình đủ các cặp, giữ cố định; kết cục lưu trên đường này đều đi đúng": $0{,}729;0{,}81;0{,}9;1$ |
| L11-2-15 | một nhẹ | như mục 1 và 3 |
| L11-2-17 (`kien-truc-dyna-def-slide.svg`) | không lỗi | như mục 3 |
| L11-2-18 | không lỗi | như mục 3; các hàng còn lại không đổi |
| L11-2-19 (ghi chú diễn giả) | không lỗi | "tăng $k$ không sửa được sai số của $\hat p$" đúng: Mệnh đề 11.15 đo sai số quanh $\bar y$ của mô hình cố định, còn độ lệch giữa $\hat p$ và $p$ chỉ giảm theo $C$ (Mệnh đề 11.5) |

**Kết luận.** Hai phát hiện nhẹ của lượt trước đã sửa đúng. Vòng 4 sinh 2 phát hiện nhẹ:

- câu "cặp có mô hình" ở Thuật toán 11.3 (2-06) lệch đầu vào của ghi chú;
- kỳ vọng thiếu điều kiện trong "Ý tưởng chứng minh" (2-15).

Ngoài ra, mọi số, công thức, khẳng định và nhãn hình trên các trang đổi đều khớp ghi chú. Không có phát hiện chặn bàn giao, nghiêm trọng hay trung bình nên không cản việc commit chu kỳ 2.
