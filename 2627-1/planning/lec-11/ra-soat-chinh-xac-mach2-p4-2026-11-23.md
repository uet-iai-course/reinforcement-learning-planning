# Kiểm lại độ chính xác mạch 2, Bài 11, sau lượt sửa P4 (2026-11-23)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc). Sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** các trang đổi theo `sua-m2-p4-2026-11-23.md`: 2-00, 2-06, 2-08, 2-09, 2-13, 2-19.
  - SVG: `q-planning-doc-ghi-slide.svg`, năm lớp `chuoi-thuong-tham-do*-slide.svg`, `cap-nhat-mau-sai-so-slide.svg`.
  - Ghi chú diễn giả của 2-09.
- **Nguồn đối chiếu:** `materials/lec-11/lecture-note.md` (3609690).
- **Cách kiểm:** `diff` toàn section 2 giữa bản P3 (lưu ở lượt trước) và bản P4; đọc nhãn và tọa độ SVG.

## 1. Phát hiện

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| — | — | Không có phát hiện. | — | — |

Tổng: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 0 nhẹ.

## 2. Kiểm từng điểm

- **2-00.** `strand-keys` mới là "đi thật để học mô hình · rút từ mô hình để cập nhật $Q$ · thử lại khi mô hình đã cũ". Ba cụm này khớp trình tự §2.1–2.2, §2.4, §2.5. Không có khẳng định toán.
- **2-06.**
  - Nhãn "một cập nhật trên cặp đã có thẻ: bảng bốn cặp sau lượt đầu là đủ" đúng. Một lần chạy bước 1–3 tại $(\mathrm F,\rightarrow)$ chỉ cần mô hình ở cặp đó (dòng 217: "Ví dụ 11.3 là một lần chạy bước 1–3 tại một cặp đã có mẫu").
  - Thuật toán 11.3 ghi "mô hình mẫu trả $(R,S')$ ở mọi cặp hợp lệ", khớp Đầu vào (dòng 196) và bước 1–2.
- **2-08.**
  - Bước (f) ghi "chọn ngẫu nhiên $\tilde S$ có cặp trong $\mathrm{Model}$, rồi chọn đều $\tilde A$ đã lưu tại đó". Câu này khớp dòng 387 ("một hành động $\tilde A$ đã thử tại $\tilde S$") và hộp Dyna-Q của Sutton và Barto (tr. 164: "random action previously taken in $S$"). Chữ "đều" chỉ nói rõ phân phối, không đổi thuật toán.
  - Đầu vào "$\alpha$, $\varepsilon$, $n$", bỏ chữ "tham số", không đổi nghĩa.
- **2-13.**
  - Dòng Nhắc lại đúng. Tại $\mathrm K$, đi được thì vào $\mathrm Z$, thưởng $+1$; trượt thì ở lại $\mathrm K$, thưởng $0$; nên $v(\mathrm K)=0{,}8\cdot1+0{,}2\cdot0{,}9\,v(\mathrm K)$, cho $0{,}8/0{,}82=0{,}97561$. Số $0{,}9756$ dưới ô K của hình khớp.
  - Diễn giải đúng. "Mô hình cố định đủ cặp (khác bảng lượt đầu)": $0{,}9^3=0{,}729$, đúng giả thiết của Mệnh đề 11.4. "Mê cung thật, tuyến tối ưu": $0{,}97561\cdot0{,}87805^3=0{,}66044$.
  - Tuyến A→B→F→K→Z là một đường ngắn nhất (Ví dụ 11.1, $d(\mathrm A)=4$), nên giá trị theo tuyến này bằng $v_*(\mathrm A)$.
- **2-09.** Năm lớp dựng dần đúng thứ tự và đúng số:
  1. Thẻ cũ $(0,\mathrm B)$, khớp Ví dụ 11.7.
  2. Tường $\mathrm B$–$\mathrm C$ mở.
  3. Thang $Q(\mathrm B,\cdot)$ với $0{,}54$ và $0{,}6$.
  4. Bước (f) cộng $0{,}01\sqrt{400}=0{,}2$, ngoặc 400 bước thật tính từ thẻ cũ ($\ell=400$, Định nghĩa 11.11 và Ví dụ 11.8), vạch $0{,}64$. Hàng Dyna-Q+ của bảng hiện cùng lúc: $0+0{,}2+0{,}9\cdot0{,}6=0{,}74$, $0{,}54+0{,}5\cdot0{,}2=0{,}64$. Mốc cuối để trống với câu hỏi.
  5. "Chọn → nếu 0,64 vẫn dẫn đầu", hai nhánh $0{,}8$/$0{,}2$, "ghi kết cục; ℓ ← 0".
  - Câu mới trong ghi chú diễn giả về nhịp dựng dần đúng.
- **2-19.**
  - Trục thêm "mỗi lần đánh giá tính một giá trị nhánh", đúng với Định nghĩa 11.14: một lần đánh giá là một lần tính $\max_{a'}Q(s',a')$ tại một trạng thái kế.
  - Mốc xanh lá "10 lượt rút có hoàn lại; sai số 0,3146" đúng: $k$ mẫu độc lập theo $\hat p$ đồng khả năng, $\sqrt{99/1000}=0{,}3146$.
  - Mốc xám "duyệt đủ 100 nhánh: đúng mục tiêu kỳ vọng" đúng: cập nhật kỳ vọng có sai số $0$ sau $b$ lần đánh giá (Phạm vi của Mệnh đề 11.15).
  - Tọa độ các điểm không đổi: $b=2$ cho $116{,}2/170/193{,}9/208{,}1$; chấm $(113;218{,}2)$; chấm $(266;300)$; vòng $(266;170)$.

Kết luận: các thay đổi của lượt P4 đúng về toán và khớp ghi chú bài giảng. Không có phát hiện nào cản việc commit chu kỳ 2.
