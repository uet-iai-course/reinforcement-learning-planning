# Kiểm lại độ chính xác sau lượt sửa vòng 6, deck Bài 11, mạch 1 (2026-11-23)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc), cùng vai với sáu báo cáo trước; sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** mạch 1 sau lượt sửa theo `sua-vong6-mach1-2026-11-23.md`.
  - Trang 1-03 (ghi chú diễn giả), 1-05 (ba lớp sơ đồ neo), 1-06, 1-07 (ghi chú diễn giả), 1-09.
  - SVG `so-do-neo-slide.svg`, `so-do-neo-quyet-dinh-slide.svg`, `so-do-neo-tuy-chon-slide.svg`, `luot-mot-ql-ket-qua-slide.svg`, `luot-mot-ke-hoach-slide.svg`, `me-cung-he-so-slide.svg`.
- **Nguồn đối chiếu:** `materials/lec-11/lecture-note.md` (3609690); `materials/lec-01/lecture-note.md` (Định nghĩa 01.14).
- **Cách kiểm:**
  - `diff` mạch 1–2 giữa bản vòng 5 (lưu ở lượt trước) và bản hiện tại; mạch 2 không đổi.
  - Đọc nhãn và `viewBox` SVG.
  - Chụp 1600×900 ba trang 1-05, 1-06, 1-09: không lỗi trang, không `.katex-error`.

## 1. Phát hiện

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| — | — | Không có phát hiện. | — | — |

Tổng: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 0 nhẹ.

## 2. Kiểm từng điểm

### L11-1-06

- **Dòng $v(1)$:** $v(1)=0{,}8\cdot1+0{,}2\gamma\,v(1)$, nên $v(1)=0{,}8/0{,}82=0{,}97561$. Khớp dòng 89–90.
- **Dòng $v(2)$:** $v(2)=0{,}8\gamma\,v(1)+0{,}2\gamma\,v(2)$, nên $v(2)=\frac{0{,}8\gamma}{1-0{,}2\gamma}v(1)=\frac{0{,}72}{0{,}82}\cdot0{,}97561=0{,}87805\cdot0{,}97561=0{,}85663$. Kết quả khớp $v_*(\mathrm F)=0{,}8566$ (dòng 94) và $\rho$ ở dòng 1338.
- **Màu hai hạng tử:** xanh cho phần đi đúng, xám cho phần trượt, khớp màu mũi tên và vòng trượt trong hình. Màu không đổi nội dung toán.
- **Câu mở:** "lượt đi từ A, kết thúc ở Z" đúng với Ví dụ 11.1: lượt bắt đầu ở $\mathrm A$, $\mathrm Z$ là trạng thái kết thúc. Luật, phần thưởng và $\gamma$ giữ nguyên ở dòng sau.

### L11-1-07, ghi chú diễn giả

- Tại $\mathrm F$, hàng Q-learning có bốn giá trị bằng $0$. Phá hòa ngẫu nhiên đều chọn $\rightarrow$ với xác suất $1/4$; câu này đúng.
- Hàng lập kế hoạch có $0{,}225>0$ ở $\rightarrow$, nên mọi quy tắc phá hòa đều chọn $\rightarrow$; câu này cũng đúng.
- Khớp định nghĩa $\varepsilon$-tham lam ở Kiến thức tiên quyết (dòng 26: "chọn một hành động cực đại $Q(s,\cdot)$").

### L11-1-09

- **Câu hỏi mới:** "ngay sau cập nhật thật ở bước 5, $Q(\mathrm F,\rightarrow)$ bằng bao nhiêu?". Đáp án $0$ đúng, vì cập nhật duy nhất của $(\mathrm F,\rightarrow)$ là ở bước 4, với mục tiêu $0+0{,}9\cdot\max_aQ(\mathrm K,a)=0$.
- **Bảng SVG:**
  - Hàng "Mô hình": ghi $(\mathrm F,\rightarrow)\mapsto(\mathrm K,0)$; ghi $(\mathrm K,\rightarrow)\mapsto(\mathrm Z,+1)$; đọc $(\mathrm F,\rightarrow)$: $(\mathrm K,0)$.
  - Hàng "Bảng Q": $0$; $0{,}5$; $0{,}225$.
  - Cả hai hàng đúng.
- **Ghi chú diễn giả:** mô tả ba lượt bấm khớp chỉ số mảnh của trang.
  - Lượt 1: hình kết quả, dòng bước 5, câu hỏi.
  - Lượt 2: câu hỏi mục tiêu.
  - Lượt 3: lớp kế hoạch, $0{,}45$, $0{,}225$.

### L11-1-05

- Ba lớp cùng `viewBox` 760×470.
  - Lớp đầu: nhánh 2.
  - Mảnh 1: nhánh 3, 4 và ngoặc "tại thời điểm quyết định".
  - Mảnh 2: nhánh 5.
- Nhãn giữ như vòng 5 và khớp §1.2, Định nghĩa 11.21 (lập kế hoạch tại thời điểm quyết định gồm tìm kiếm theo cây và tối ưu kế hoạch). Tùy chọn được ghi là lập kế hoạch nền ở bảng §6.1, nên đặt ngoài ngoặc là đúng.

### L11-1-03, ghi chú diễn giả

- "(e) ghi $(\mathrm K,\rightarrow)\mapsto(S',R)=(\mathrm Z,+1)$" đúng.

## 3. Thứ tự $(S',R)$ ở mạch 1 và $(R,S')$ ở mạch 2

Ghi chú bài giảng tự dùng cả hai thứ tự, nên không có khẳng định nào sai:

- Định nghĩa 01.14 và Kiến thức tiên quyết (dòng 20) viết dự báo của mô hình là $(\widehat S_{t+1},\widehat R_{t+1})$, tức $(S',R)$.
- Định nghĩa 11.2 (dòng 189), Thuật toán 11.3 (bước 2) và Thuật toán 11.8 (bước (e), (f)) viết $(R,S')$, ví dụ $\mathrm{Model}(S,A)\leftarrow(R,S')$.

Mạch 1 theo Định nghĩa 01.14 và trang quy ước 1-02. Ở 1-09 và ghi chú diễn giả 1-03, mỗi lần thứ tự đổi đều ghi rõ "$(S',R)=$…", nên đọc không nhầm. Mạch 2 theo Thuật toán 11.8: $(\mathrm A,\rightarrow)\mapsto(0,\mathrm B)$, ${(\tilde R,\tilde S')\leftarrow\mathrm{Model}(\tilde S,\tilde A)}$.

Mọi bộ số ở hai mạch đều đúng khi đọc theo thứ tự được ghi tại chỗ: phần thưởng là $0$ hoặc $+1$, trạng thái là chữ cái, nên không bộ nào hiểu nhầm được. Đây chỉ là lệch ký hiệu giữa hai mạch, không tính là phát hiện độ chính xác. Đề xuất của biên tập viên (một dòng "Ký hiệu:" ở 2-07, hoặc thống nhất ở lần sửa sau) là việc trình bày, để điều phối viên quyết định.

Kết luận: các thay đổi của lượt sửa vòng 6 ở mạch 1 đúng về toán và khớp ghi chú bài giảng. Không có phát hiện.
