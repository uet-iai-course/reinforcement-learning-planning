# Kiểm lại độ chính xác sau vòng sửa 3, deck Bài 11, mạch 1–2 (2026-11-22)

- Vai: người rà độ chính xác toán học và thuật toán (chỉ đọc), cùng vai với ba báo cáo trước; sub-agent `general-purpose`, Opus 5.5.
- Đối tượng: hai section đầu của deck sau vòng sửa 3, theo `sua-vong3-mach12-2026-11-22.md`.
  - Các trang đổi: 1-01 (ghi chú diễn giả), 1-02, 1-03, 1-04, 1-05, 1-06, 1-07, 1-09, 2-03, 2-04, 2-07, 2-08, 2-09, 2-10, 2-13, 2-15, 2-17, 2-19.
  - Hình: SVG mới `dai-f-k-z-slide.svg` và 13 SVG sửa.
- Nguồn đối chiếu: `materials/lec-11/lecture-note.md` (3609690).
- Cách kiểm:
  - `diff` mặt trang và ghi chú diễn giả giữa bản vòng 2 (đã lưu ở lượt trước) và bản vòng 3. Mỗi thay đổi đối chiếu với ghi chú; số tính lại.
  - Đọc nhãn và tọa độ SVG.
  - Chụp 1600×900 tám trang (`Reveal.configure({transition:'none'})`): không lỗi trang, không `.katex-error`. Ảnh nằm trong scratchpad của phiên.

## 1. Bốn phát hiện nhẹ của lượt trước

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| L11-2-18, ghi chú diễn giả gọi "mọi cặp chọn vô hạn lần" là hỏng | đã sửa đúng | Ghi chú diễn giả: "Hai giả thiết hỏng chắc chắn: mô hình không cố định… và $\alpha=0{,}5$ hằng… Giả thiết 'mọi cặp chọn vô hạn lần' chỉ không được bước (f) bảo đảm sẵn: với $\varepsilon>0$ trên mê cung hữu hạn, mọi cặp hầu chắc chắn được thử thật sau hữu hạn bước, rồi được (f) chọn lại vô hạn lần." Đúng: mọi ô tới được từ $\mathrm A$, lượt khởi động lại ở $\mathrm A$, mỗi hành động có xác suất ít nhất $\varepsilon/4$. |
| L11-2-08, phân phối rút ở (f) | đã sửa đúng | "(f) rút đều một lần thử cũ của cặp và lấy cả cặp $(\tilde R,\tilde S')$ của lần đó, tức rút theo $\hat p$", khớp ghi chú dòng 193 và 417. |
| L11-2-10, thiếu "giả sử" | đã sửa đúng | Mặt trang: "giả sử $\max_aQ(\mathrm B,a)=0{,}6$, $\max_aQ(\mathrm A,a)=0{,}4$". Hình: "các giá trị max Q là giả sử". Khớp Ví dụ 11.10, dòng 496. |
| L11-2-15, dòng chứng minh thiếu bước | đã sửa đúng | "Ý tưởng chứng minh." nay có đủ hai bước, xem mục 3. |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nhẹ | L11-2-15, "Ý tưởng chứng minh." | Ký hiệu $\sigma^2$ xuất hiện lần đầu trên mặt trang mà không được định nghĩa. Người đọc không biết $\sigma^2$ là phương sai của giá trị nhánh quanh $\bar y$ dưới phân phối rút. Hai bước của ý tưởng đều đúng. | Mệnh đề 11.15(a) (dòng ~524): $\sigma^2=\sum_{s'}\hat p(s'\mid s,a)(y_{s'}-\bar y)^2$. Ghi chú diễn giả có $\bar y$, $Q_k$, nhưng không định nghĩa $\sigma^2$. | Thêm vào câu đầu: "…bình phương trung bình $\sigma^2/k$, với $\sigma^2$ là phương sai của giá trị nhánh quanh $\bar y$." Hoặc đưa định nghĩa vào ghi chú diễn giả. |
| nhẹ | L11-1-06, dòng lượt bấm "Tại $\mathrm K$: $v(1)=0{,}8\cdot1+0{,}2\gamma\,v(1)$… Xa $\mathrm Z$ thêm một bước, giá trị nhân $0{,}8780$." | Chỉ số trong $v(1)$ là số bước đi đúng tối thiểu $d$ tới $\mathrm Z$. Mặt trang vòng 3 đã bỏ định nghĩa $d$ ("Với $d\ge2$ bước đi đúng tối thiểu tới Z"), nên trên mặt trang $v(\cdot)$ không còn được định nghĩa. Phép tính vẫn đúng: $v(1)=0{,}8/(1-0{,}18)=0{,}9756$. | Ví dụ 11.1 (dòng 88–90): "Gọi $d(s)$ là số bước đi đúng tối thiểu… $v(d)$"; ghi chú diễn giả của trang có định nghĩa $d$. | Viết $v_*(\mathrm K)=0{,}8\cdot1+0{,}2\gamma\,v_*(\mathrm K)$, nên $v_*(\mathrm K)=0{,}9756$. Hoặc thêm "($v(d)$: giá trị ở ô cách $\mathrm Z$ $d$ bước đi đúng)". |

Tổng phát hiện mới: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 2 nhẹ.

## 3. Các điểm điều phối viên hỏi riêng

- **L11-2-07, câu thay mới: đúng.** Câu là "Một cập nhật cần mô hình ở cặp được chọn. Mệnh đề 11.4 xét hội tụ toàn bảng, với mô hình cố định, đủ mọi cặp."
  - Bước 2–3 của Thuật toán 11.3 chỉ gọi mô hình tại cặp được chọn.
  - Mệnh đề 11.4 đòi mô hình cố định, xác định ở mọi cặp hợp lệ (dòng 220).
  - Câu không liệt kê hai giả thiết còn lại của mệnh đề ("vô hạn lần", Robbins–Monro). Câu không khẳng định mình đủ, và 2-13, 2-18 ghi đủ, nên không phải lỗi.
  - Hàng bước 2 "$(\mathrm A,\rightarrow)\mapsto\cancel{(0,\mathrm A)}\ (0,\mathrm B)$; đếm: A:1, B:1" đúng với Ví dụ 11.6 ("Bốn bước đầu", "Mô hình đếm").
- **L11-2-15, hai bước của ý tưởng chứng minh: đúng, khớp chứng minh Mệnh đề 11.15.**
  - Bước 1, giữ nguyên giá trị nhánh: $\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k$ (phần (a), Bước 2).
  - Bước 2, lấy kỳ vọng theo giá trị nhánh: $\mathbb E\sigma^2=\tfrac1b\bigl(\mathbb E\sum_i(y_i-m)^2-b\,\mathbb E(\bar y-m)^2\bigr)=\tfrac1b(b-b\cdot\tfrac1b)=1-\tfrac1b$. Lý do "trung bình $b$ nhánh có phương sai $1/b$" chính là $\operatorname{Var}\bar y=1/b$ ở Bước 3.
  - Ghép lại: $(1-1/b)/k=(b-1)/(bk)$.
  - Thiếu định nghĩa $\sigma^2$ (nhẹ, ở trên).
- **L11-2-04, "C = 2 vì lần đầu trượt" và $\hat p\in\{0;0{,}5;1\}$: đúng.**
  - Trong lượt, $(\mathrm A,\rightarrow)$ được thử lại chỉ vì lần 1 trượt. Nếu lần 1 đi đúng thì $C=1$, nên $C$ phụ thuộc kết quả.
  - Với $C=2$ ấn định trước, $\hat p\in\{0;0{,}5;1\}$ với xác suất $0{,}04$; $0{,}32$; $0{,}64$. Từ đó $\mathbb E\hat p=0{,}16+0{,}64=0{,}8$, $\mathbb E\hat p^2=0{,}08+0{,}64=0{,}72$, $\operatorname{Var}\hat p=0{,}72-0{,}64=0{,}08$, độ lệch chuẩn $0{,}2828$. Kết quả khớp (2.2).
  - Dòng "lệch $0{,}3$" đúng: $\lvert0{,}5-0{,}8\rvert$.
  - Tọa độ điểm không đổi.
- **L11-1-06, $v(1)=0{,}8/(1-0{,}18)$: đúng.** $v(1)=0{,}8\cdot1+0{,}18\,v(1)$, nên $0{,}82\,v(1)=0{,}8$ và $v(1)=0{,}97561$ (dòng 89–90). Hình nhỏ "tại K" đúng: "đi đúng 0,8: +1" và "trượt 0,2: ở lại K, 0". "Nhân $0{,}8780$ mỗi bước" khớp dòng 107. Chỉ có ký hiệu $v(\cdot)$ chưa định nghĩa (nhẹ, ở trên).
- **L11-1-03, thứ tự hai cặp lập kế hoạch: đúng.** "$(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$" khớp Ví dụ 11.6 ("Giả sử bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$"). Ghi chú diễn giả cho đúng $0{,}225$ rồi $0{,}75$. Mục 1, với $C=5$ và $C=50$ giả định, $p=0{,}8$: $0{,}1789\to0{,}0566$, giảm $\sqrt{10}=3{,}162$ lần. Mục 2 "hành động mà thưởng thăm dò giúp thử lại" là $(\mathrm B,\rightarrow)$ (Ví dụ 11.8).
- **L11-2-19, mốc $b=2$, $k=2$, RMSE $0{,}5$: đúng.**
  - $\sqrt{(2-1)/(2\cdot2)}=\sqrt{1/4}=0{,}5$ tại $k/b=1$.
  - Vòng xanh ở tọa độ $(266;\,170)$ khớp $x=96+170\cdot1$ và $y=300-260\cdot0{,}5$, trùng điểm $k=2$ của đường $b=2$.
  - Chấm xám $(1;0)$ "đã tính đúng mục tiêu kỳ vọng" nằm ở $(266;300)$. Chấm $b=100$, $k=10$ vẫn ở $(113;\,218{,}2)$.
- **L11-2-17, "tác tử đang ở $\mathrm B$ khi (f) cập nhật $Q(\mathrm F,\rightarrow)$": khớp Bài tập 11.4.** Bước thật $(\mathrm A,\rightarrow,0,\mathrm B)$ cho $S'=\mathrm B$. Theo Thuật toán 11.8, (d), (e), (f) chạy sau khi quan sát $S'$, và bước chọn cặp đầu tiên lấy $(\mathrm F,\rightarrow)$. $\mathrm F\ne\mathrm B$, nên đây là cập nhật ở trạng thái khác, đúng nghĩa Định nghĩa 11.9.

## 4. Trang và hình đã kiểm

| trang | kết luận | số và nhãn đã kiểm |
|---|---|---|
| L11-1-01 (ghi chú diễn giả) | không lỗi | $0{,}225$ với thứ tự $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$; đảo thứ tự cho $Q(\mathrm F,\rightarrow)=0{,}5\cdot0{,}9\cdot0{,}75=0{,}3375$ |
| L11-1-06 (`me-cung-luat-slide.svg`, `me-cung-gia-tri-slide.svg`) | một nhẹ | $v_*$ bốn mức đúng ô; $v(1)=0{,}9756$; $0{,}8780$; hình nhỏ tại $\mathrm K$ |
| L11-1-09 (`luot-mot-q-learning-slide.svg`, `luot-mot-ql-ket-qua-slide.svg`, `luot-mot-ke-hoach-slide.svg`) | không lỗi | lượt bấm 1: "bước thật 4: đọc max Q(K,·) = 0", "bước thật 5: vào Z, nhận +1", "mục tiêu 0" ở F, "Q(K,→) = 0,5"; lượt bấm 2: "S′ = K, R = 0, mục tiêu 0,45", "Q(F,→) = 0,225"; thứ tự đúng |
| L11-1-07 | không lỗi | "bảng đầu để bốn hành động hòa": $Q(\mathrm F,\cdot)=0$ sau Q-learning; "bảng sau chọn →": $Q(\mathrm F,\rightarrow)=0{,}225>0$ |
| L11-1-02 (`mo-hinh-hai-dang-slide.svg`) | không lỗi | "với động lực dừng" khớp Nhận xét 06.20; "mỗi lần gọi rút một kết cục theo phân phối của mô hình" khớp Định nghĩa 11.2; $0{,}8$/$0{,}2$ |
| L11-1-05 (`so-do-neo-slide.svg`) | không lỗi | "ví dụ: bước 5 vừa xong" (Ví dụ 11.6); "ví dụ: phòng trái → K" ($\omega_1$, Ví dụ 11.24, 11.25) |
| L11-1-03 | không lỗi | như mục 3 |
| L11-1-04 | không lỗi | "chặn xác suất rollout xếp nhầm $\downarrow$ cao hơn $\rightarrow$ theo số mô phỏng" là biến cố $\bar G(\downarrow)\ge\bar G(\rightarrow)$ của (3.1); ghi chú diễn giả không đổi ($0{,}0496$, $m=75$: $0{,}0483$) |
| L11-2-03 (`dai-f-k-z-slide.svg`) | không lỗi | F→K thưởng $0$, "lúc đọc K: giá trị 0" (bước 4); K→Z thưởng $+1$, "sau bước: Q(K,→) = 0,5" |
| L11-2-04 (`hai-loai-bat-dinh-A-slide.svg`) | không lỗi | như mục 3 |
| L11-2-07 | không lỗi | như mục 3; bước 5: $0{,}5$, $0{,}225$, $0{,}75$ |
| L11-2-08 | không lỗi | như mục 1 |
| L11-2-09 (`chuoi-thuong-tham-do-slide.svg`) | không lỗi | hai nhánh $0{,}8$ (sang C) và $0{,}2$ (ở lại B); cả hai tới "(e) ghi kết cục quan sát; ℓ(B,→) ← 0" (Định nghĩa 11.11); $0{,}2$, $0{,}74$, $0{,}64$ |
| L11-2-10 (`so-do-cap-nhat-hai-lan-thu-slide.svg`) | không lỗi | $\bar y=0{,}9(0{,}5\cdot0{,}6+0{,}5\cdot0{,}4)=0{,}45$; $(0{,}54+0{,}36)/2=0{,}45=\bar y$ (Ví dụ 11.10, Kiểm tra lại) |
| L11-2-13 (`hai-gioi-han-duong-di-slide.svg`) | không lỗi | "kết cục lưu trên đường này đều đi đúng": $0{,}729;0{,}81;0{,}9;1$; mặt trang có "đủ các cặp, cố định" |
| L11-2-15 | một nhẹ | như mục 3 |
| L11-2-17 | không lỗi | như mục 3 |
| L11-2-19 (`cap-nhat-mau-sai-so-slide.svg`) | không lỗi | như mục 3; các điểm $b=2$, $k=1..4$ và đầu các đường $b=10$, $b=100$ không đổi |
| `so-do-neo-mach2-slide.svg` (L11-2-00) | không lỗi | nhãn như vòng 2 |
| L11-2-18 (ghi chú diễn giả) | không lỗi | như mục 1 |

Kết luận: bốn phát hiện nhẹ của lượt trước đã sửa đúng. Vòng 3 chỉ sinh 2 phát hiện nhẹ, đều là ký hiệu chưa định nghĩa trên mặt trang: $\sigma^2$ ở 2-15 và $v(\cdot)$ theo $d$ ở 1-06. Mọi số, công thức, khẳng định và nhãn của các trang đổi, của SVG mới và của 13 SVG sửa đều khớp ghi chú bài giảng.
