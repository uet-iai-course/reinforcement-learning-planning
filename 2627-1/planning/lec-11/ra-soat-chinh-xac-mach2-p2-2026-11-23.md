# Kiểm lại độ chính xác mạch 2, Bài 11, sau lượt sửa P2 (2026-11-23)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc). Sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** mạch 2 sau lượt sửa theo `sua-m2-p2-2026-11-23.md`.
  - Các trang đổi: 2-03, 2-04, 2-06, 2-07, 2-08, 2-09, 2-13, 2-14, 2-15, 2-16, 2-18, 2-19, 2-20, 2-21.
  - Các SVG đổi.
  - Ghi chú diễn giả.
- **Nguồn đối chiếu:** `materials/lec-11/lecture-note.md` (3609690).
- **Cách kiểm:**
  - `diff` mặt trang và ghi chú diễn giả giữa bản P1 (lưu ở lượt trước) và bản P2.
  - Đọc nhãn SVG.
  - Sinh lại các số của 2-21 bằng đúng hàm vẽ: `random.Random(11)`, chín lượt `randrange`, lượt thứ mười lặp lại lượt đầu.
  - Chụp 1600×900 bảy trang (`Reveal.configure({transition:'none'})`): không lỗi trang, không `.katex-error`. Ảnh lưu trong scratchpad của phiên.

## 1. Năm phát hiện nhẹ của lượt trước

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| 2-06: gán mô hình giữ kết cục gần nhất cho Ví dụ 11.3 | đã sửa đúng | Câu mới: "Ở $(\mathrm F,\rightarrow)$, mô hình đếm và mô hình giữ kết cục gần nhất trùng nhau vì mới có một lần quan sát." Câu này không còn gán mô hình cho Ví dụ 11.3 và khớp dòng 175, 344. |
| 2-14, mặt trang: "Nhắc lại" thiếu điều kiện | đã sửa đúng | "Nhắc lại: **trong ví dụ**, nhờ mô hình, Dyna-Q đưa giá trị từ K về F ngay lượt đầu." |
| 2-14, ghi chú diễn giả: "mô hình đúng với môi trường" | đã sửa đúng | Câu mới: "dựa vào mô hình ghi đúng các chuyển đã thấy trước khi môi trường đổi". |
| 2-09: "cửa B–C" | đã sửa đúng | Mốc thứ hai nay ghi "tường B–C mở", khớp Ví dụ 11.1, 11.7. |
| 2-21, ghi chú diễn giả: RMSE lấy trung bình theo gì | đã sửa đúng | Ghi chú nay có: "Lặp lại với cùng 100 giá trị thì căn trung bình bình phương độ dài đoạn là $\sigma/\sqrt k$ của bộ giá trị này, $0{,}2972$…; công thức của mệnh đề lấy thêm trung bình theo giá trị nhánh, cho $0{,}3146$". Câu đầu đổi thành "một lần thể hiện của giả thiết". Tính lại: $\sigma^2=0{,}8831$; $\sqrt{0{,}8831/10}=0{,}2972$; $\sqrt{99/1000}=0{,}3146$. |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nhẹ | L11-2-19, ghi chú diễn giả ("Bậc thang xám đặt sai số ban đầu giả định bằng $1$ để chuẩn hóa, như Hình 8.7…") | Hình đã đổi: không còn bậc thang ở mức 1. Thay vào đó là dải xám "chưa hoàn tất cập nhật kỳ vọng" từ $k/b=0$ tới $1$, rồi đường ở mức 0. Câu ghi chú diễn giả mô tả hình cũ. Phần "(2.5) chỉ mô tả các điểm $k\ge1$" vẫn đúng. | Nhãn SVG `cap-nhat-mau-sai-so-slide.svg`: "chưa hoàn tất / cập nhật / kỳ vọng", "kỳ vọng: dải xám, sai số 0 khi đủ k = b". Ghi chú diễn giả 2-19 không đổi so với P1. Mệnh đề 11.15, Phạm vi (dòng ~533). | "Dải xám là đoạn cập nhật kỳ vọng chưa xong, chưa cho giá trị mới; Hình 8.7 của Sutton và Barto vẽ đoạn này ở mức sai số ban đầu chuẩn hóa bằng $1$. Công thức (2.5) chỉ mô tả các điểm $k\ge1$." |
| nhẹ | L11-2-13, hình `hai-gioi-han-duong-di-slide.svg` (nhãn "→ q̂* (Q-planning)", "→ q* (Q-learning)") | Các số dưới ô là giá trị trạng thái: trên mô hình là $\max_a\hat q_*(s,a)$, trên mê cung thật là $v_*(s)=\max_aq_*(s,a)$, ví dụ $0{,}729$ và $0{,}6604$ tại $\mathrm A$. Chúng không phải giá trị hành động $\hat q_*$, $q_*$. Nhãn mũi tên đúng ở chỗ Q-planning hội tụ tới $\hat q_*$, nhưng đặt cạnh dải số thì đọc thành "các số này là $\hat q_*$". Mặt trang vòng trước có $\max_a\hat q_*(\mathrm A,a)$; Diễn giải P2 rút còn "mô hình $0{,}9^3=0{,}729$". | Mệnh đề 11.4 (Kết luận: $Q\to\hat q_*$); Ví dụ 11.1 (bảng $v_*$, dòng 92–94); Tình huống 11.2 ("giá trị $\gamma^{d-1}$"). | Thêm một dòng nhỏ trong hình, "số dưới ô: $\max_a$ của giá trị hành động". Hoặc viết Diễn giải "mô hình: $\max_a\hat q_*(\mathrm A,a)=0{,}9^3=0{,}729$; mê cung thật: $v_*(\mathrm A)=\ldots$". |

Tổng phát hiện mới: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 2 nhẹ.

## 3. Các điểm điều phối viên hỏi riêng

- **2-03, dòng dẫn đường: đúng.** "Đi thật để học mô hình → rút từ mô hình để cập nhật $Q$ → thử lại khi mô hình có thể đã cũ" khớp trình tự §2.1–2.2, §2.4 và §2.5. Định nghĩa 11.1 trên trang giữ đúng (2.1).
- **2-04: đúng.** Nhãn trục "C: số lần thử thật để học xác suất (thang log)" và "độ lệch chuẩn = √phương sai" đúng. Hai điểm $0{,}2828$ và $0{,}0566$ không đổi.
- **2-07: đúng.** "Ví dụ có trượt; để tính tay, mỗi cặp chỉ giữ kết cục vừa thấy" khớp Ví dụ 11.6: trên mê cung có trượt, ví dụ dùng mô hình tất định lưu kết quả gần nhất. Câu này cũng khớp Tình huống 11.2, chỗ giả thiết tất định của Thuật toán 11.8 không thỏa.
- **2-08: đúng.**
  - "$\varepsilon$-tham lam (thường lấy $Q$ lớn nhất, đôi lúc ngẫu nhiên)" khớp định nghĩa ở Kiến thức tiên quyết, dòng 26: với xác suất $\varepsilon$ chọn đều ngẫu nhiên, còn lại chọn hành động cực đại.
  - "Tất định: (e) ghi đè, (f) đọc thẻ đã lưu" khớp bước (e) và (f).
  - "Có trượt: đếm thẻ $(R,S')$; (e) tăng đếm, (f) rút nguyên một thẻ theo tần suất" khớp dòng 193 ("rút đều một lần thử cũ") và dòng 417 ("rút $(\tilde R,\tilde S')$ theo $\hat p$").
- **2-20: đúng.** Dấu vết $Q(\mathrm K,\rightarrow)$ là $0\to0{,}5$ ở (d), rồi $\to0{,}75$ ở (f), vì $0{,}5+0{,}5(1-0{,}5)=0{,}75$. Dấu vết $Q(\mathrm F,\rightarrow)$ là $0\to0{,}225$ ở (f), vì $0+0{,}5(0{,}9\cdot0{,}5-0)=0{,}225$. Mũi tên "đọc 0,5" đi từ ô $0{,}5$ ở hàng K lên hàng F, đúng: (f) đầu tiên đọc giá trị vừa ghi ở (d).
- **2-16: đúng.** Câu hỏi chuyển là "rút thêm làm chính xác hơn mục tiêu theo mô hình, hay xác suất thật sang B?". Đáp án ở ghi chú diễn giả là vế thứ nhất: thêm lượt rút chỉ thu hẹp sai số của mục tiêu trên mô hình cố định (Mệnh đề 11.15). $\hat p$ chỉ tiến gần $p$ khi có thêm lần thử thật (Mệnh đề 11.5).
- **2-13.**
  - Câu hỏi "trượt ở K thì ô nào được đọc lại?" có đáp án $\mathrm K$, đúng.
  - Dòng Nhắc lại đúng: $v(\mathrm K)=0{,}8\cdot1+0{,}2\cdot0{,}9\,v(\mathrm K)$ cho $0{,}8/0{,}82=0{,}97561$; hệ số $0{,}8\cdot0{,}9/(1-0{,}2\cdot0{,}9)=0{,}72/0{,}82=0{,}87805$.
  - Diễn giải đúng: $0{,}9^3=0{,}729$; $0{,}97561\cdot0{,}87805^3=0{,}66044$.
  - Dải dưới ghi "trượt 0,2 ở lại, thưởng 0", đúng.
  - Riêng nhãn "q̂*/q*" cạnh các giá trị trạng thái là phát hiện nhẹ ở mục 2.
- **2-18: đúng.**
  - "(f) chỉ chọn cặp đã thử; không bảo đảm mọi cặp được thử, chọn vô hạn lần": bước (f) không tự bảo đảm điều này. Ghi chú diễn giả nêu đúng rằng $\varepsilon>0$ trên mê cung hữu hạn làm giả thiết thỏa trong giới hạn.
  - "Robbins–Monro theo cặp, ví dụ $\alpha_j=1/j$" đúng.
  - Kết luận giữ nguyên ý của lượt trước.
- **2-14: đúng.** Đã sửa như mục 1. "F–K", "B–C" trong một khối KaTeX không đổi nghĩa.
- **2-09: đúng.**
  - Bốn mốc và ngoặc "400 bước thật" từ lần thử thật cuối của $(\mathrm B,\rightarrow)$ tới lần lập kế hoạch khớp $\ell=400$ của Ví dụ 11.8. Định nghĩa 11.11 định nghĩa $\ell(s,a)$ là số bước thật kể từ lần thử thật gần nhất của cặp, và thưởng được tính ở bước (f) đang xét.
  - Mốc đầu "bị chặn, ghi (0, B)" khớp Ví dụ 11.7: "vì trước khi đổi, → tại B đụng tường".
  - Mốc cuối có điều kiện "nếu 0,64 vẫn dẫn đầu", đúng, vì các cập nhật khác có thể đổi thứ hạng trước khi tác tử tới $\mathrm B$.
  - Thang $0{,}54$ / $0{,}6$ / $0{,}64$ đúng thứ tự. Hai nhánh $0{,}8$ / $0{,}2$ và "ℓ ← 0" khớp Định nghĩa 11.11.
- **2-21: đúng.**
  - Chú thích "(×2: rút hai lần)" đúng với cách vẽ: lượt thứ mười lặp lại thẻ của lượt đầu, chỉ số 47. Tính lại: trung bình 10 lượt là $0{,}4098$, đoạn sai lệch dài $0{,}1546$.
  - Bộ lượt rút này được dựng có chủ đích (lượt thứ mười không rút ngẫu nhiên), nhưng vẫn là một kết quả có thể xảy ra khi rút có hoàn lại. Mặt trang không ghi số, nên không có khẳng định sai.
  - Ghi chú diễn giả đúng như mục 1.
- **2-15: đúng.** "Mỗi lần rút $k$ mẫu cho một sai lệch; RMSE là căn trung bình bình phương sai lệch qua các lần lặp" đúng với $\sqrt{\mathbb E(Q_k-\bar y)^2}$ của (2.5): kỳ vọng lấy theo cả việc rút lẫn giá trị nhánh, mà câu này không giới hạn.
- **2-19: đúng.**
  - Dải "chưa hoàn tất cập nhật kỳ vọng" từ $k/b=0$ tới $1$, rồi mức 0, đúng ý Phạm vi của Mệnh đề 11.15: cập nhật kỳ vọng có sai số $0$ sau $b$ lần đánh giá và chưa cho giá trị mới trước đó.
  - Trục "k/b: số lần rút từ mô hình chia b (rút để ước lượng mục tiêu)" đúng.
  - Các điểm $b=2$ ($0{,}7071$; $0{,}5$; $0{,}4082$; $0{,}3536$) và $b=100$, $k=10$ ($0{,}3146$) không đổi.
  - Chỉ có ghi chú diễn giả còn tả hình cũ (phát hiện nhẹ ở mục 2).
- **2-06: đúng.** Câu mới như mục 1. Ba lớp hình không đổi.

## 4. Kết luận

Năm phát hiện của lượt trước đã sửa đúng. Lượt P2 sinh 2 phát hiện nhẹ:

- ghi chú diễn giả 2-19 còn tả bậc thang ở mức 1;
- nhãn "q̂*/q*" đặt cạnh giá trị trạng thái ở 2-13.

Ngoài hai điểm này, mọi số, công thức, khẳng định và nhãn hình trên các trang đổi đều khớp ghi chú bài giảng. Không có phát hiện cản việc commit chu kỳ.
