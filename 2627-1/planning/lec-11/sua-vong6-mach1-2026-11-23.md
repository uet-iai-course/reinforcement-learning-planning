# Sửa vòng 6, mạch 1, Bài 11 (2026-11-23)

Biên tập viên duy nhất của mạch 1; lượt sửa cuối của chu kỳ 3.

- **Đầu vào:** các dòng "chấp nhận" của bảng "Xét nhận xét vòng 6, mạch 1" trong `review-log.md`; nhận xét gốc `nhan-xet-codex-mach1-2026-11-23.md`. Không làm dòng "bác bỏ" (1-02, 1-03).
- **Không sửa:** mạch 2 (đã đạt điều kiện dừng); phần đầu tệp và mạch 3–6.
- **Không thêm:** trang (vẫn 65), lớp CSS. Không commit.
- **Bản sao trước lượt:** `deck-truoc-v8.html` trong scratchpad. Script vẽ `hinh_m1.py` (bản trước lượt `hinh_m1_v5.py`) nằm trong scratchpad. Lượt này không chạy `hinh_m2.py`.

## 1. Thay đổi theo trang

| Trang | Dòng bảng vòng 6 | Thay đổi |
|---|---|---|
| L11-1-06 | dòng $v(2)$ ở lượt bấm 2 thay mệnh đề "mỗi bước thêm nhân …"; tô màu hai hạng tử theo mũi tên và vòng trượt; ≤ 82 âm tiết | Mảnh 2 (hiện cùng lớp F → K của hình) là một đoạn riêng: "Tại $\mathrm F$: ${v(2)=\textcolor{\#2F3E7A}{0{,}8\gamma\,v(1)}+\textcolor{\#6B7280}{0{,}2\gamma\,v(2)}}$, nên ${v(2)=\frac{0{,}8\gamma}{1-0{,}2\gamma}\,v(1)=0{,}8780\,v(1)=0{,}8566}$." Xanh `#2F3E7A` là màu mũi tên đi đúng, xám `#6B7280` là màu vòng trượt trong hình. Phương trình $v(1)$ ở lượt bấm 1 tô cùng cách. Để vừa khung, câu mở rút thành "Mê cung hai phòng: lượt đi từ $\mathrm A$, kết thúc ở $\mathrm Z$." Âm tiết 74 → 69. |
| L11-1-09 | câu hỏi có mốc thời gian cùng lượt với 0,5; ghi chú khớp lượt bấm; kết cục theo $(S',R)$ như 1-02 | Bỏ hộp "$Q(\mathrm F,\rightarrow)$ đã tăng chưa?". Lượt bấm 1 hiện dòng bước 5 ($0{,}5$) và câu "**Câu hỏi:** ngay sau cập nhật thật ở bước 5, $Q(\mathrm F,\rightarrow)$ bằng bao nhiêu?". Câu này để dạng đoạn thường, không đóng hộp, để vừa khung. Lượt 2 và 3 giữ nguyên. Hàng "Mô hình" của bảng trong SVG: ghi (F,→) ↦ (K, 0); ghi (K,→) ↦ (Z, +1); đọc (F,→): (K, 0). Alt sửa theo. Ghi chú diễn giả viết lại theo ba lượt bấm: lượt 1 có bước 5, cột hai bước thật và câu hỏi ($Q(\mathrm F,\rightarrow)$ vẫn bằng 0); lượt 2 hỏi mục tiêu; lượt 3 có cột lập kế hoạch, mô hình trả $(S',R)=(\mathrm K,0)$, $0{,}45$, $0{,}225$. Ghi chú nói rõ bảng dùng thứ tự $(S',R)$ như trang quy ước. Âm tiết 34 → 42. |
| L11-1-03 (chỉ ghi chú) | đồng bộ thứ tự $(S',R)$ trong mạch 1 | Ghi chú mục tiêu 2: "(e) ghi $(\mathrm K,\rightarrow)\mapsto(S',R)=(\mathrm Z,+1)$". |
| L11-1-05 | dựng dần: Dyna-Q trước, rồi hai nhánh thời điểm quyết định cùng ngoặc, rồi tùy chọn | `so-do-neo-slide.svg` nay là lớp đầu: ô gốc và nhánh 2. Hai lớp mới: `so-do-neo-quyet-dinh-slide.svg` (mảnh 1: nhánh 3, 4 và ngoặc "tại thời điểm quyết định"), `so-do-neo-tuy-chon-slide.svg` (mảnh 2: nhánh 5). Cả ba lớp cùng `viewBox` 760×470, xếp trong `r-stack`. Mỗi lớp có alt riêng. Ghi chú diễn giả thêm thứ tự hiện. Âm tiết không đổi (52). |
| L11-1-07 (chỉ ghi chú) | quy tắc phá hòa | Thêm câu: ở hàng Q-learning, quy tắc phá hòa quyết định hành động; phá hòa ngẫu nhiên chọn $\rightarrow$ với xác suất $1/4$; hàng lập kế hoạch chọn $\rightarrow$ với mọi quy tắc. Mặt trang không đổi (87). |

**Hệ quả với mạch 2:**
- Mạch 2 vẫn ghi mô hình theo thứ tự $(R,S')$ của Thuật toán 11.8, ví dụ $(\mathrm A,\rightarrow)\mapsto(0,\mathrm B)$ ở 2-07, 2-08.
- Mạch 1 nay ghi $(S',R)$ như 1-02. Mạch 2 đã đóng, nên lượt này không sửa (xem mục 5).

## 2. Phép tính

- 1-06:
  - $v(1)=0{,}8\cdot1+0{,}18\,v(1)$, nên $v(1)=0{,}8/0{,}82=0{,}9756$.
  - $v(2)=0{,}72\,v(1)+0{,}18\,v(2)$, nên $v(2)=(0{,}72/0{,}82)\,v(1)=0{,}8780\cdot0{,}9756=0{,}8566$. Khớp ô F trong hình.
- 1-09:
  - Sau bước thật 5, $Q(\mathrm F,\rightarrow)=0$, vì cập nhật duy nhất của cặp này là ở bước 4, với mục tiêu $0+0{,}9\cdot0$.
  - Lập kế hoạch: mô hình trả $(\mathrm K,0)$; mục tiêu $0+0{,}9\cdot0{,}5=0{,}45$; $Q(\mathrm F,\rightarrow)=0+0{,}5(0{,}45-0)=0{,}225$.
- 1-07: phá hòa ngẫu nhiên đều trên bốn hành động hòa nhau cho xác suất chọn $\rightarrow$ bằng $1/4$.

## 3. Kiểm tra (máy chủ 8841)

- `footer_check`: 0 trang chạm chân trang. Lần đo đầu, 1-06 (867) và 1-09 (875) chạm; đã sửa như ghi ở mục 1.
- `formula_overflow`: `[]`.
- `deck_lint`: 54 dòng, không có BANNED.
  - Mạch 1 thêm ba cờ NOTES150 (mức nhẹ): 1-09 166, 1-05 178, 1-07 249.
  - Cờ NOTES150 của 1-07 đã có từ trước: 220 trước lượt này, 249 sau; vẫn dưới mức tối đa khoảng 250 của học phần.
- Playwright 1600×900 và 390×844 trên 1-03, 1-05, 1-06, 1-07, 1-09: không có `.katex-error`, lỗi console, yêu cầu lỗi, hay phần tử quá đáy hoặc mép phải. Đã xem ảnh rộng 1-06, 1-09.
- Cỡ nhãn hiển thị ở 1600×900 ≥ 20 px. Thấp nhất ở mạch 1: 1-09 20,4.
- **Kiểm nhãn SVG** (`svgcheck.py`, hộp bao `<text>` so với `viewBox` và với hình chữ nhật chứa nó):
  - Chạy trên 10 SVG của mạch 1, gồm ba lớp sơ đồ neo và ba lớp lượt thứ nhất.
  - Kết quả: 1 báo, là vòng số ② của `luot-mot-q-learning`. Vòng này cố ý đặt trên vạch A–B như các vòng trước, không phải lỗi tràn.
  - Đã xem ảnh phóng to ×2: bảng của 1-09 (cột "ghi (K,→) ↦ (Z, +1)" nằm trong ô) và ba lớp sơ đồ neo chồng nhau (chữ nhánh 4 cách viền, ngoặc không chạm chữ).
- **Mạch 2 không đổi:** section 2 đến hết tệp trùng từng byte với `deck-truoc-v8.html`; phần đầu tệp trùng. Không SVG nào của mạch 2 được ghi lượt này; `hinh_m2.py` không chạy.
- `git diff --check` sạch. Không alt nào chứa ">".

## 4. Âm tiết (deck_lint)

| Trang | Trước | Sau | Giới hạn |
|---|---|---|---|
| L11-1-06 | 74 | 69 | ≤ 82 |
| L11-1-09 | 34 | 42 | dưới 60 |
| L11-1-05 | 52 | 52 | |
| L11-1-07 | 87 | 87 | mặt trang không đổi |

## 5. Chỗ vướng

- **Thứ tự kết cục lệch giữa hai mạch.** Mạch 1 nay thống nhất $(S',R)$ với 1-02. Mạch 2 (2-07, 2-08, hình hai thẻ, cây 2-10) vẫn ghi $(R,S')$ theo Thuật toán 11.8 của ghi chú. Mạch 2 đã đóng nên không sửa. Đề nghị điều phối viên quyết định:
  - hoặc thêm một dòng "Ký hiệu:" ở 2-07 nói đổi sang thứ tự $(R,S')$ của Thuật toán 11.8;
  - hoặc để lần sửa sau thống nhất hai mạch.
- **1-09:** câu hỏi ở lượt bấm 1 không đóng hộp vì không đủ chỗ.
- **1-06:**
  - Câu mở rút từ "lượt bắt đầu ở A và kết thúc khi vào Z" thành "lượt đi từ A, kết thúc ở Z".
  - Hạng tử trượt tô xám theo màu vòng trượt nên nhạt hơn chữ thường; vẫn đọc được trên ảnh 1600×900.
