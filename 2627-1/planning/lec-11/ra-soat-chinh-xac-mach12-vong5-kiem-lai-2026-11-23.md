# Kiểm lại độ chính xác sau vòng sửa 5, deck Bài 11, mạch 1–2 (2026-11-23)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc), cùng vai với năm báo cáo trước. Sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** hai section đầu của deck sau vòng sửa 5, theo `sua-vong5-mach12-2026-11-22.md`.
  - Các trang đổi: 1-02, 1-03, 1-05, 1-06, 1-07, 1-09, 2-08.
  - Kiểm lại 2-06, 2-15 (phát hiện cũ).
  - Các SVG dịch chuyển ở 2-04, 2-10, 2-17.
- **Nguồn đối chiếu:** `materials/lec-11/lecture-note.md` (3609690).
- **Cách kiểm:**
  - `diff` mặt trang, alt và ghi chú diễn giả giữa bản vòng 4 (lưu ở lượt trước) và bản vòng 5.
  - Tính lại các số; đọc nhãn, `viewBox` và tọa độ SVG.
  - Chụp 1600×900 tám trang (`Reveal.configure({transition:'none'})`, `Reveal.slide(h,v,99)`): không lỗi trang, không `.katex-error`. Ảnh nằm trong scratchpad của phiên.

## 1. Hai phát hiện nhẹ của lượt trước

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| L11-2-06, "cặp có mô hình" lệch Thuật toán 11.3 | đã sửa đúng | Câu mới: "chọn ngẫu nhiên một cặp hợp lệ $(S,A)$; mô hình mẫu (sample model), xác định ở mọi cặp, trả $(R,S')$". Khớp Đầu vào và bước 1 của Thuật toán 11.3 (dòng 196, 208). |
| L11-2-15, kỳ vọng thiếu điều kiện | đã sửa đúng | ${\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k}$, khớp Bước 3 chứng minh Mệnh đề 11.15. Phần còn lại không đổi và đúng: $\sigma^2=\frac1b\sum_{s'}(y_{s'}-\bar y)^2$, $\mathbb E\sigma^2=1-1/b$, $\operatorname{Var}\bar y=1/b$. |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| — | — | Không có phát hiện mới. | — | — |

Tổng phát hiện mới: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 0 nhẹ.

## 3. Các điểm điều phối viên hỏi riêng

### L11-2-08, bước (f) so với ghi chú dòng 387, 193, 417: đúng.

Ghi chú (dòng 387) viết "chọn ngẫu nhiên một trạng thái $\tilde S$ đã gặp và một hành động $\tilde A$ đã thử tại $\tilde S$". Deck viết "chọn ngẫu nhiên $\tilde S$ có cặp trong $\mathrm{Model}$, rồi $\tilde A$ đã lưu tại đó". Hai cách viết cho cùng một thuật toán:

- Mỗi hành động đã thử đều được (e) lưu vào $\mathrm{Model}$ ngay ở bước đó.
- Vì vậy "hành động đã thử tại $\tilde S$" trùng "hành động đã lưu tại $\tilde S$".
- Một trạng thái đã gặp mà chưa có hành động nào được thử không thể chọn tiếp $\tilde A$. Ví dụ là ô vừa tới lần đầu, hay ô kết thúc $\mathrm Z$ (ghi chú diễn giả nêu đúng hai ví dụ này).
- Do đó điều kiện "có cặp trong $\mathrm{Model}$" chỉ nói rõ điều mà bước (f) của ghi chú ngầm cần. Đây cũng là "previously observed state" kèm "action previously taken in $S$" của Sutton và Barto (tr. 164).

Hai dòng cuối trang cũng đúng:

- "Giữ kết cục gần nhất: (e) ghi đè, (f) đọc kết cục đã lưu" khớp bước (e), (f) và Ví dụ 11.6.
- "Đếm kết cục (có trượt): (e) tăng đếm $(R,S')$, (f) rút cả $(R,S')$ theo tần suất" khớp dòng 193 ("rút đều một lần thử cũ") và dòng 417 ("rút $(\tilde R,\tilde S')$ theo $\hat p$"). Rút theo tần suất của các cặp $(R,S')$ đã đếm là rút theo phân phối thực nghiệm chung, tức theo $\hat p(\cdot,\cdot\mid s,a)$.

Ghi nhận cho tác giả, không tính là phát hiện: có thể đề xuất làm rõ dòng 387 của ghi chú theo cách viết của deck (NT3).

### L11-1-03, mục 1, "mô hình đếm của $(\mathrm A,\rightarrow)$ từ hai lần thử": đúng.

- $C(\mathrm A,\rightarrow)=2$ với $C(\mathrm A,\rightarrow,\mathrm A)=C(\mathrm A,\rightarrow,\mathrm B)=1$, nên $\hat p=1/2$ mỗi kết cục (Ví dụ 11.2). Ghi chú diễn giả ghi đúng điều này.
- Phần sau giữ cỡ mẫu giả định $C=5$, $C=50$ với $p=0{,}8$, nên không áp Mệnh đề 11.5 cho số đếm của lượt: $\sqrt{50/5}=3{,}162$; $0{,}1789\to0{,}0566$.
- Mục 3: với $10<b=100$ lần đánh giá, chỉ cập nhật mẫu chạy được. RMSE so với $\bar y$ là $0$ cho cập nhật kỳ vọng (đủ $100$ lần) và $\sqrt{99/1000}=0{,}3146$ cho $k=10$ cập nhật mẫu (Ví dụ 11.11, Mệnh đề 11.15(b)).

### L11-1-06, hình F → K → Z và `me-cung-he-so-slide.svg`: đúng.

- Lớp giá trị: "K → Z 0,8, thưởng +1", "vòng tại K 0,2, thưởng 0".
- Lớp hệ số: "F → K 0,8, thưởng 0", "vòng tại F 0,2, thưởng 0". Khớp động lực của Ví dụ 11.1 (dòng 86).
- Mảnh 2 ("mỗi bước thêm nhân $0{,}8\gamma/(1-0{,}2\gamma)=0{,}8780$") hiện cùng lớp F, đúng thứ tự: chỉ sau khi có $v(1)$ mới suy ra $v(2)$.
- Ghi chú diễn giả: $v(2)=0{,}8\gamma\,v(1)+0{,}2\gamma\,v(2)$, nên $v(2)=(0{,}72/0{,}82)\cdot0{,}97561=0{,}85663$. Kết quả khớp $v_*(\mathrm F)=0{,}8566$ (dòng 94).
- $v(1)=0{,}8/0{,}82=0{,}9756$ không đổi.

### L11-1-07: đúng.

- Cột "$Q(\mathrm F,\cdot)$ sau bước thật 5".
- Hàng Q-learning: $0;0;0;0$.
- Hàng "lập kế hoạch tại $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$": $0;0;0;0{,}225$. Theo Ví dụ 11.6, các cập nhật lập kế hoạch ở bước 1–4 đều có mục tiêu $0$; ở bước 5 chỉ $(\mathrm F,\rightarrow)$ tại $\mathrm F$ đổi, thành $0{,}5\cdot0{,}9\cdot0{,}5=0{,}225$.
- "Tham lam tại $\mathrm F$: hàng đầu hòa, hàng sau $\rightarrow$" đúng: $\arg\max$ của bốn số $0$ là cả bốn hành động; $\arg\max$ hàng sau là $\rightarrow$.

### L11-1-09, bảng "Bảng Q / Mô hình" ba mốc: đúng.

| mốc | Bảng Q | Mô hình |
|---|---|---|
| bước thật 4 | $Q(\mathrm F,\rightarrow)=0$ (mục tiêu $0+0{,}9\max_aQ(\mathrm K,a)=0$) | ghi $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$ |
| bước thật 5 | $Q(\mathrm K,\rightarrow)=0+0{,}5(1-0)=0{,}5$ | ghi $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$ |
| lập kế hoạch | $Q(\mathrm F,\rightarrow)=0+0{,}5(0{,}9\cdot0{,}5-0)=0{,}225$ | đọc $(\mathrm F,\rightarrow)$: $(0,\mathrm K)$ |

- Cả mô hình lưu kết cục gần nhất lẫn mô hình đếm đều cho các mục trên, vì mỗi cặp chỉ có một lần thử.
- Số $0{,}5$ được tô xanh lục ở ô K, trong bảng và trong ${0{,}9\cdot0{,}5=0{,}45}$, đúng là cùng một giá trị.
- Nhãn lưới "mục tiêu 0" (bước 4) và "mục tiêu 0,45" (lập kế hoạch) đúng.
- Thứ tự dựng dần đúng: mảnh 1 có bước 4–5; mảnh 2 là câu hỏi; mảnh 3 có lớp kế hoạch và $0{,}225$.

### L11-1-02, `mo-hinh-hai-dang-slide.svg`: đúng.

- "trả cả bảng (S′, R): (Z, +1) 0,8; (K, 0) 0,2".
- Khung mẫu ghi "mỗi lần gọi rút một kết cục theo phân phối của mô hình; ví dụ: (S′, R) = (K, 0)". Thứ tự $(S',R)$ khớp dòng Nhắc lại.
- Câu mới trong ghi chú diễn giả đúng: các ví dụ dùng $\alpha=0{,}5$ hằng, nên chỉ kiểm phép cập nhật, không thuộc phạm vi bảo đảm hội tụ, vì $\sum\alpha^2=\infty$ không thỏa Định nghĩa 06.19.

### L11-1-05, `so-do-neo-slide.svg`: đúng.

Nhánh 4 ghi "tối ưu chuỗi hành động nhận giá trị thực" (Mục 4, Định nghĩa 11.31).

### SVG dịch chuyển: không đổi số liệu.

- `hai-loai-bat-dinh-A-slide.svg` (`viewBox` 620×532): hai điểm $(172{,}6;164{,}0)$ và $(584;304{,}8)$, ba cột cao $2{,}8;22{,}4;44{,}8$ (tỉ lệ $0{,}04:0{,}32:0{,}64$), đều giữ nguyên. Chỉ nhãn trục dọc dịch.
- `kien-truc-dyna-def-slide.svg` (`viewBox` 580×404) và `so-do-cap-nhat-hai-lan-thu-slide.svg` (`viewBox` 660×420): nhãn và số trùng vòng 4.

## 4. Trang và hình đã kiểm

| trang | kết luận |
|---|---|
| L11-1-02 (`mo-hinh-hai-dang-slide.svg`) | không lỗi |
| L11-1-03 | không lỗi |
| L11-1-05 (`so-do-neo-slide.svg`) | không lỗi |
| L11-1-06 (`me-cung-luat-slide.svg`, `me-cung-gia-tri-slide.svg`, `me-cung-he-so-slide.svg`) | không lỗi |
| L11-1-07 | không lỗi |
| L11-1-09 (`luot-mot-q-learning-slide.svg`, `luot-mot-ql-ket-qua-slide.svg`, `luot-mot-ke-hoach-slide.svg`) | không lỗi |
| L11-2-04 (`hai-loai-bat-dinh-A-slide.svg`) | không lỗi |
| L11-2-06 | không lỗi (phát hiện cũ đã sửa) |
| L11-2-08 | không lỗi |
| L11-2-10 (`so-do-cap-nhat-hai-lan-thu-slide.svg`) | không lỗi |
| L11-2-15 | không lỗi (phát hiện cũ đã sửa) |
| L11-2-17 (`kien-truc-dyna-def-slide.svg`) | không lỗi |

Kết luận: hai phát hiện nhẹ của lượt trước đã sửa đúng. Vòng 5 không sinh phát hiện mới. Mọi số, công thức, khẳng định và nhãn hình trên các trang đổi khớp ghi chú bài giảng.
