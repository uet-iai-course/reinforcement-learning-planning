# Kiểm lại độ chính xác mạch 2, Bài 11, sau lượt sửa P3 (2026-11-23)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc). Sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** mạch 2 sau lượt sửa theo `sua-m2-p3-2026-11-23.md`. Các trang đổi: 2-04, 2-06, 2-09, 2-10, 2-13, 2-14, 2-15, 2-16, 2-19, 2-21. SVG mới `hai-gioi-han-he-so-slide.svg`, cùng các SVG sửa và ghi chú diễn giả 2-13, 2-19, 2-21.
- **Nguồn:** `materials/lec-11/lecture-note.md` (3609690).
- **Cách kiểm:**
  - Chạy `diff` mặt trang và ghi chú diễn giả giữa bản P2 (đã lưu ở lượt trước) và bản P3.
  - Đọc nhãn SVG.
  - Sinh lại hai lần rút phụ của 2-21 bằng đúng hàm vẽ.
  - Chụp 1600×900 bốn trang 2-13, 2-15, 2-16, 2-21 (`Reveal.configure({transition:'none'})`): không lỗi trang, không `.katex-error`.

## 1. Hai phát hiện nhẹ của lượt trước

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| L11-2-19: ghi chú diễn giả còn tả bậc thang ở mức 1 | đã sửa đúng | Ghi chú mới: "Dải xám từ $k/b=0$ tới $1$ là đoạn cập nhật kỳ vọng chưa hoàn tất, chưa cho giá trị mới; từ $k/b=1$ sai số của nó bằng $0$… Hình 8.7 của Sutton và Barto vẽ đoạn này ở mức sai số ban đầu giả định $1$". Khớp hình và Phạm vi của Mệnh đề 11.15. |
| L11-2-13: nhãn "q̂*/q*" cạnh giá trị trạng thái | đã sửa đúng | Nhãn mới "→ maxₐ q̂*" (dải mô hình) và "→ v* = maxₐ q*" (dải mê cung thật). Các số dưới ô ($0{,}729$…; $0{,}6604$…) là đúng giá trị trạng thái. |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| — | — | Không có phát hiện. | — | — |

Tổng: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 0 nhẹ.

## 3. Kiểm từng điểm

- **2-04: đúng.**
  - Khung trái ghi "hai lần thử phát sinh trong một lượt đi": $C$ do kết quả quyết định, đúng (Mệnh đề 11.5, dòng 264, 269).
  - Khung phải ghi "mỗi nhóm được ấn định hai lần thử (p = 0,8)": $C$ chọn trước, ba cột $0{,}04;0{,}32;0{,}64$, độ lệch chuẩn $0{,}2828$, đúng.
- **2-16: đúng.**
  - Câu hỏi "rút thêm từ mô hình làm chính xác hơn điều gì?" có lời chốt đúng.
  - Vế "Xác suất thật sang B: đi thật thêm" đúng: $\hat p$ chỉ tiến gần $p$ khi số lần thử thật $C$ tăng (Mệnh đề 11.5).
  - Vế "Mục tiêu với hai thẻ: rút từ mô hình hoặc xét cả hai nhánh" đúng: rút mẫu cho mục tiêu mẫu, xét cả hai nhánh cho mục tiêu kỳ vọng (Định nghĩa 11.14, Mệnh đề 11.15).
  - Phần "Nhắc lại" rút gọn vẫn đúng. Bảng giữ dòng (e) $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$ qua mẫu của hàng (f) cuối.
  - Diễn giải giữ điều kiện về lần chọn cặp.
- **2-10: đúng.** Hộp nhắc lại lời chốt của 2-16 rồi hỏi "mở mọi thẻ hay rút một thẻ?", khớp §2.6.
- **2-06: đúng.** Nhãn "một cập nhật trên cặp đã có thẻ" khớp đoạn sau Thuật toán 11.3 (dòng 217): "Ví dụ 11.3 là một lần chạy bước 1–3 tại một cặp đã có mẫu". Câu Thuật toán 11.3 vẫn đòi mô hình xác định ở mọi cặp.
- **2-13: đúng.**
  - Nhãn nhánh tại K đúng: "0,8: +1" (vào $\mathrm Z$) và "0,2: 0" (trượt, ở lại K).
  - Lớp mới tại F đúng: "0,8·0,9" cho nhánh đi tiếp, "0,2·0,9" cho nhánh trượt. Dòng "v(F) = 0,72 v(K) + 0,18 v(F) ⇒ × 0,72/0,82 mỗi bước" cho $v(\mathrm F)=0{,}87805\cdot0{,}97561=0{,}85663$, khớp ô F và Ví dụ 11.1 (dòng 89–94).
  - Câu hỏi "trượt ở K thì ô nào được đọc lại?" có đáp án $\mathrm K$. Dòng Nhắc lại $v(\mathrm K)=0{,}8/0{,}82=0{,}9756$ đúng.
  - Diễn giải "mô hình cố định đủ mọi cặp (khác bốn cặp của lượt đầu)" đúng. Mệnh đề 11.4 cần mô hình xác định ở mọi cặp, còn mô hình của lượt đầu chỉ có bốn cặp (Nhận xét 11.10). Hai giá trị $0{,}729$ và $0{,}6604$ đúng.
  - Câu mới trong ghi chú diễn giả về lượt bấm thứ ba đúng.
- **2-14 và 2-09: đúng, khớp Ví dụ 11.7 và 11.8.**
  - Thẻ cũ "$(\mathrm B,\rightarrow)$: thưởng 0, ở lại B" là $\mathrm{Model}(\mathrm B,\rightarrow)=(0,\mathrm B)$ của Ví dụ 11.7. Theo dòng 429, thẻ này có vì trước khi đổi, $\rightarrow$ tại $\mathrm B$ đụng tường.
  - Thẻ do bước (e) ghi ở lần thử thật gần nhất. Vì vậy mốc bắt đầu ngoặc "400 bước thật" trùng mốc bắt đầu đếm $\ell(\mathrm B,\rightarrow)$ (Định nghĩa 11.11). Tại lần lập kế hoạch, $\ell=400$ như Ví dụ 11.8, dòng 437.
  - Nếu tác tử từng thử $(\mathrm B,\rightarrow)$ nhiều lần trước khi đổi, mỗi lần đều ghi lại cùng thẻ, nên "thẻ cũ" vẫn là thẻ của lần thử cuối.
- **2-21: đúng.**
  - Hai vạch cam mảnh không ghi số. Sinh lại: hai lần rút lại 10 thẻ trên cùng bộ 100 giá trị cho trung bình $0{,}0459$ và $0{,}0969$, khớp `sua-m2-p3`.
  - Ghi chú diễn giả "mỗi lần cho một sai lệch khác" đúng.
- **2-15: đúng.**
  - Câu "Trung bình bình phương sai lệch khi giữ bộ nhánh, rồi trung bình qua các bộ giá trị nhánh; căn của nó là RMSE" đúng với $\sqrt{\mathbb E_y\,\mathbb E[(Q_k-\bar y)^2\mid y]}$, tức (2.5) theo Bước 3 của chứng minh.
  - Kết luận "so với $\bar y$" đúng. $\bar y$ đã định nghĩa ở 2-10 (hình) và ghi chú diễn giả.
- **2-19: đúng.** Nhãn trục "k/b: số lần đánh giá nhánh / tổng số nhánh b (rút từ mô hình để ước lượng mục tiêu)" đúng: một mẫu là một lần đánh giá (Định nghĩa 11.14). Các điểm và đường không đổi.

## 4. Kết luận

Hai phát hiện nhẹ của lượt trước đã sửa đúng. Lượt P3 không sinh phát hiện mới. Mọi số, công thức, khẳng định và nhãn hình trên các trang đổi khớp ghi chú bài giảng.
