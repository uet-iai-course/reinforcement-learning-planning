# Storyboard Bài 09

## Đợt sửa 2026-10-28: bản đồ bảy mạch

Căn cứ: kế hoạch sửa của điều phối viên ngày 2026-10-28 (D1–D7) và ba báo cáo rà soát chỉ đọc (cấu trúc–mạch, sinh viên–mật độ–trực quan, RL–toán), xem `review-log.md`, mục "Đợt sửa 2026-10-28". Bản đồ này thay bản đồ sáu mạch cũ ở cuối tệp.

**Vấn đề trung tâm.** Ước lượng không chệch từ mẫu hai đại lượng dùng để cập nhật: giá trị của hành động được chọn trong mục tiêu bootstrap, và gradient của $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ theo tham số chính sách. Khung lý thuyết chung (đối tượng, giả thiết, chuỗi định nghĩa → kết quả → phương pháp, giới hạn) ghi trong `outline.md`, mục "Khung lý thuyết chung".

| mạch | loại | chức năng | đầu vào | đầu ra | đóng góp cho vấn đề trung tâm | trang tiêu đề mạch | thời lượng |
|---|---|---|---|---|---|---|---:|
| 1. Mở đầu | mở bài | Nêu ký hiệu, nhắc lại mục tiêu DQN, chính sách, lợi tức, Jensen; mục tiêu, nội dung, vấn đề trung tâm | Bài 03: $\pi$, $G_t$, $q_\pi$; Bài 08: $y_i$, $\operatorname{sg}$, $\theta^-$, $Z$, $U$ | Hai đại lượng cần ước lượng không chệch; câu trả lời có điều kiện của mạch 2–6 | Phát biểu bài toán | không có (bìa là trang tiêu đề của mạch mở đầu) | 8 |
| 2. Độ chệch của phép cực đại | khái niệm, kết quả | Chỉ ra phép cực đại trong mục tiêu DQN vừa chọn vừa đánh giá; ví dụ hai hành động nhiễu $\pm1$; bất đẳng thức kỳ vọng | Mục tiêu DQN (`L09-01c`); Jensen (`L09-01d`) | $\mathbb E[\max_a\widehat Q_a]\ge\max_a\mathbb E[\widehat Q_a]$; nguyên nhân là cùng ước lượng chọn và đánh giá | Giá trị trong mục tiêu bootstrap chệch lên | `L09-M2T`, `id="mach-2"` | 15 |
| 3. Tách chọn và đánh giá | thuật toán | Ví dụ hai bản ước lượng độc lập; mục tiêu và thuật toán Double DQN; phạm vi; Double Q-learning; so sánh | Nguyên nhân độ chệch (mạch 2) | Hai thuật toán, bảng so sánh, phạm vi; giới hạn chung: chính sách tham lam theo $Q$ tất định, cần $\max$ trên $\mathcal A$ hữu hạn | Chọn và đánh giá độc lập thì không chệch lên; Double DQN chỉ giảm | `L09-M3T`, `id="mach-3"` | 30 |
| 4. Chính sách tham số hóa | khái niệm | Lưới gộp trạng thái của nguồn; hành động liên tục; phân phối phân loại, softmax, Gaussian | Giới hạn của chính sách tham lam theo $Q$ (mạch 3) | $\pi_\theta(\cdot\mid s)$ rời rạc hoặc liên tục, chuẩn hóa | Khi nào cần học trực tiếp $\pi_\theta$ | `L09-M4T`, `id="mach-4"` | 15 |
| 5. Hàm mục tiêu và hàm điểm | khái niệm | $J(\theta)$, bước tăng gradient, sai phân hữu hạn (vấn đề), hàm điểm softmax và Gaussian | $\pi_\theta$ (mạch 4) | $\psi_\theta$ cho hai họ; $\mathbb E_{A\sim\pi}[\psi]=0$ | $\nabla\pi=\pi\psi$ khi $\pi>0$, khả vi | `L09-M5T`, `id="mach-5"` | 22 |
| 6. Gradient chính sách và REINFORCE | kết quả, thuật toán | Tỉ số xác suất, xác suất quỹ đạo, lợi tức từ thời điểm $t$, định lý gradient chính sách, REINFORCE | $\psi_\theta$ (mạch 5) | $\nabla J=\mathbb E[\sum_t\gamma^tG_t\psi_t]$; một cập nhật REINFORCE kiểm được | Gradient ước lượng không chệch từ lượt dưới giả thiết nêu rõ | `L09-M6T`, `id="mach-6"` | 20 |
| 7. Tổng kết và chuyển tiếp | kết bài | Bảng kết quả–giả thiết, bảng phương pháp, bài tổng hợp, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, bài tập về nhà và tài liệu đọc | Kết quả mạch 2–6 | Câu trả lời có điều kiện; nối Bài 10 | Tổng hợp; không thêm khái niệm mới | `L09-M7T`, `id="mach-7"` | 10 |

Tổng: $8+15+30+15+22+20+10=120$ phút trên lớp; 30 phút chữa bài ngoài 120 phút. Mã trang tiêu đề mạch dạng `L09-MNT` theo tiền lệ `L08-MNT`, vì mã trang của bài không có tiền tố mạch bằng chữ cái.

### Danh sách trang theo mạch (mục tiêu của đợt sửa)

Cột "C0": vị trí `h.v` (đánh số từ 1) sau bước C0, khi chỉ di chuyển trang. "chưa có" là trang sẽ thêm ở bước của mạch tương ứng. Cột "bước": vị trí sau bước mạch 1.

| mạch | mã | tiêu đề dự kiến | quyết định | lý do | C0 | bước mạch 1 |
|---|---|---|---|---|---|---|
| 1 | `L09-01` | Double DQN và gradient chính sách (bìa) | sửa | Câu luận đề một câu thay phụ đề "…, rồi …"; thêm đơn vị, năm học | 1.1 | 1.1 (S1) |
| 1 | `L09-01b` | Tiên quyết và quy ước (Ký hiệu) | thêm | Dòng "Ký hiệu:" và bảng: MDP quan sát đầy đủ, $\mathcal A$, $m$, $R_{t+1}$, $T$, $\rho_0$, $P$, $Z$, $U$, mẫu chuyển của mini-batch | chưa có | 1.2 (S2) |
| 1 | `L09-01c` | Tiên quyết và quy ước (Nhắc lại Bài 08) | thêm | "Nhắc lại:" mục tiêu DQN dạng mặt nạ, $L_B$ với $\operatorname{sg}$, đồng bộ $\theta^-$, cắt ngắn vẫn bootstrap | chưa có | 1.3 (S3) |
| 1 | `L09-01d` | Tiên quyết và quy ước (Nhắc lại Bài 03, Jensen) | thêm | "Nhắc lại:" chính sách, $\mathbb E_\pi$, $G_t$, $q_\pi$, bất đẳng thức Jensen | chưa có | 1.4 (S3) |
| 1 | `L09-02` | Mục tiêu học tập | sửa | Năm mục ứng mạch 2–6 thay bốn thẻ | 1.2 | 1.5 (S4) |
| 1 | `L09-02b` | Nội dung | thêm | Bảy mục khớp tên trang tiêu đề mạch và `#/N`; dòng đọc trước | chưa có | 1.6 (S5) |
| 1 | `L09-02c` | Vấn đề trung tâm | thêm | Hộp bài toán và năm câu trả lời có điều kiện | chưa có | 1.7 (S6) |
| 2 | `L09-M2T` | 2. Độ chệch của phép cực đại | thêm | Trang tiêu đề mạch, điểm vào mạch 2 | chưa có | chưa có |
| 2 | `L09-03` | Phép cực đại trong mục tiêu DQN | sửa | Trang vấn đề "Nhu cầu:"; ví dụ dẫn nhập CartPole ($108{,}5>100$) với hình trục số; quy ước $O=S$ đã sang `L09-01b` | 2.1 | 2.2 (S8) |
| 2 | `L09-04` | Độ chệch của phép cực đại (trực quan) | sửa | Hình hai hành động nhiễu chuyển xuống `L09-05`; đọc $q_a$ và $\widehat Q_a$ thành lời | 2.2 | 2.2 |
| 2 | `L09-05` | Ví dụ: hai hành động có nhiễu ±1 | sửa | Tiêu đề dạng "Ví dụ: …"; đặt hình; "Diễn giải:" | 2.3 | 2.3 |
| 2 | `L09-06` | Độ chệch của phép cực đại không âm | sửa | "Mệnh đề." với giả thiết khả tích; "Chứng minh." một dòng; dòng nối nguyên nhân | 2.4 | 2.4 |
| 3 | `L09-M3T` | 3. Tách chọn và đánh giá | thêm | Trang tiêu đề mạch, điểm vào mạch 3 | chưa có | chưa có |
| 3 | `L09-06b` | Ví dụ: hai bản ước lượng độc lập | thêm | Bước trực giác–ví dụ còn thiếu cho việc tách (nguồn tr. 14) | chưa có | chưa có |
| 3 | `L09-07` | Mục tiêu Double DQN | sửa | Dòng giới hạn của DQN; dạng mặt nạ như Bài 08 | 3.1 | 3.1 |
| 3 | `L09-08` | Ví dụ: một mẫu chuyển, hai mục tiêu | sửa | Đặt hình có số; "Diễn giải:"; giữ bộ số đã kiểm bằng `assert` ở bài thực hành Bài 08 | 3.2 | 3.2 |
| 3 | `L09-09` | Thuật toán. Double DQN | sửa, chuyển lên trước `X01` | Bước hình thức của thuật toán đứng trước bài tập | 3.3 | 3.3 |
| 3 | `X01` | Bài tập: tách chọn và đánh giá | sửa | "Câu hỏi:", "Lời giải:", dữ kiện nêu lại | 3.4 | 3.4 |
| 3 | `L09-10` | Phạm vi của Double DQN | sửa | Bỏ câu chung, giữ hai luận điểm có điều kiện | 3.5 | 3.5 |
| 3 | `L09-11` | Double Q-learning dạng bảng | sửa | Dòng giới hạn dẫn tới hai bảng | 3.6 | 3.6 |
| 3 | `L09-13` | Ví dụ: một cập nhật Double Q-learning | sửa, chuyển lên trước `L09-12` | Ví dụ tính tay trước công thức; dùng lại số của `L09-08` | 3.7 | 3.7 |
| 3 | `L09-12` | Quy trình Double Q-learning | sửa | Thuật toán đủ đầu vào, khởi tạo, hành vi, dừng | 3.8 | 3.8 |
| 3 | `L09-14` | So sánh Double Q-learning và Double DQN | sửa | Thêm tiêu chí quan hệ giữa hai ước lượng | 3.9 | 3.9 |
| 3 | `L09-15` | Bài tập: Double DQN và Double Q-learning | sửa | "Lời giải" thay "Đáp án" | 3.10 | 3.10 |
| 4 | `L09-M4T` | 4. Chính sách tham số hóa | thêm | Trang tiêu đề mạch, điểm vào mạch 4 | chưa có | chưa có |
| 4 | `L09-16` | Giới hạn của chính sách tham lam theo $Q$ | tách, sửa | Lưới gộp trạng thái theo nguồn tr. 23–25; hai mệnh đề có điều kiện; hết tràn | 4.1 | 4.1 |
| 4 | `L09-16b` | Hành động liên tục | thêm (hoặc gộp) | Tách từ `L09-16` | chưa có | chưa có |
| 4 | `L09-17`, `L09-18`, `L09-19` | Chính sách cho xác suất hành động; Ví dụ: chính sách trên bốn hành động; Chính sách softmax và chính sách Gaussian | sửa | Số liệu nguồn tr. 28; hết tràn `L09-19` | 4.2–4.4 | 4.2–4.4 |
| 5 | `L09-M5T` | 5. Hàm mục tiêu và hàm điểm | thêm | Trang tiêu đề mạch, điểm vào mạch 5 | chưa có | chưa có |
| 5 | `L09-20`, `L09-21` | Hàm mục tiêu của một chính sách; bước tăng gradient | sửa | Vấn đề và ví dụ trước định nghĩa; $\tau$, $p_\theta$ định nghĩa trước khi dùng | 5.1–5.2 | 5.1–5.2 |
| 5 | `L09-30A` | Ước lượng gradient bằng sai phân hữu hạn | sửa, chuyển về | Trang vấn đề của hàm điểm theo nguồn tr. 33 | 5.3 | 5.3 |
| 5 | `L09-23`–`L09-27`, `X02` | Hàm điểm; softmax; ví dụ; Gaussian; ví dụ; bài tập | sửa; `X02` chuyển xuống sau `L09-27` | Bài tập không dùng công thức chưa dạy | 5.4–5.9 | 5.4–5.9 |
| 6 | `L09-M6T` | 6. Gradient chính sách và REINFORCE | thêm | Trang tiêu đề mạch, điểm vào mạch 6 | chưa có | chưa có |
| 6 | `L09-28`, `L09-22`, `L09-28A`, `L09-29` | Gradient của $J$ theo tỉ số xác suất; giả thiết; xác suất quỹ đạo; lợi tức từ thời điểm $t$ | sửa; `L09-22` chuyển về cạnh `L09-28` | Giả thiết đặt cạnh chỗ dùng | 6.1–6.4 | 6.1–6.4 |
| 6 | `L09-29b` | Ví dụ: lượt hai bước | thêm | Ví dụ cho bước bỏ phần thưởng quá khứ | chưa có | chưa có |
| 6 | `L09-30` | Định lý gradient chính sách | sửa, chuyển lên trước REINFORCE | Kết quả chính của nguồn tr. 39 | 6.5 | 6.5 |
| 6 | `L09-32`, `L09-31`, `X03` | Ví dụ: một cập nhật REINFORCE; Thuật toán. REINFORCE; bài tập | sửa; `L09-32` trước `L09-31` | Ví dụ tính tay trước thuật toán | 6.6–6.8 | 6.6–6.8 |
| 7 | `L09-M7T`, `L09-K1`–`L09-K7` | Tổng kết và chuyển tiếp | thêm | Bảng kết quả, bảng phương pháp, bài tổng hợp, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, bài tập về nhà, dòng nối Bài 10 | chưa có | chưa có |
| 7 | `L09-33` | (nội dung vào `L09-K1`) | bỏ | Tổng kết dạng thẻ "hợp đồng", vượt trần 80 | 7.1 (tạm) | 7.1 (tạm) |

### Lệch khỏi trật tự nguồn (đợt sửa 2026-10-28)

1. Nguồn tr. 3–10 (ôn DQN) gộp vào `L09-01c` dạng "Nhắc lại:"; tr. 11 (ba câu hỏi thảo luận về DQN) không đưa lên mặt trang, như bản trước.
2. Ở bước C0, `L09-09` và `X01` đổi chỗ, `L09-13` lên trước `L09-12`, `L09-30A` về mạch 5 trước `L09-23`, `L09-22` về mạch 6 sau `L09-28`, `L09-30` lên trước `L09-32`, `L09-32` lên trước `L09-31`, `X02` xuống sau `L09-27`. Lý do: đặt ví dụ trước công thức, bài tập sau phần đã dạy, và khôi phục thứ tự nguồn tr. 33 → 34 → 39 → 40.
3. Các lệch còn lại được ghi khi sửa trang tương ứng.

### Ngoại lệ mật độ

`L09-01` (bìa): sau R1 65 âm tiết (trước R1 58), trong đó câu luận đề một câu 46 âm tiết trong hộp, hiển thị trên ba dòng, mỗi dòng dưới 20 âm tiết; R1 thêm hai điều kiện vào luận đề (ước lượng không chệch có nhiễu; giả thiết của định lý gradient chính sách); cùng khuôn và lý do với `L08-01` (luận đề phải là một câu). `L09-02b` (Nội dung): 8 dòng > 6 vì phải liệt kê đủ bảy mạch cùng dòng đọc trước, như `L08-02b`; 39 âm tiết. `L09-02c` (Vấn đề trung tâm): sau R1 83 âm tiết > 60 (1,38 lần trần, dưới 1,5 lần; trước R1 71); hộp bài toán 21 âm tiết trên hai dòng hiển thị và năm dòng trả lời có điều kiện 7, 23, 16, 7, 9. Dòng 3 (23 âm tiết, câu do điều phối viên chốt ở R1) hiển thị trên hai dòng, ngắt trước "Double DQN chỉ gần thỏa" bằng dấu cách không ngắt, mỗi dòng dưới 20; dòng 6 hiển thị trên hai dòng vì công thức giữ nguyên khối. R1 thêm giả thiết quyết định vào dòng 3 (bản đánh giá không chệch, độc lập) và dòng 6 (đổi được đạo hàm và tích phân), nên số âm tiết tăng; đáy 630 px. Cùng khuôn và lý do với `L08-02c` (88 âm tiết): trang phải có dòng bài toán và một dòng trả lời cho mỗi mạch 2–6; rút thêm sẽ bỏ điều kiện của câu trả lời.

### Hành trình khái niệm (đợt sửa 2026-10-28)

Mạch 1 không mở khái niệm cốt lõi nào: các trang nhắc lại kết quả đã học (Bài 03, Bài 08, bất đẳng thức Jensen) và nêu bài toán; sáu bước vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra ghi `không áp dụng`. Ví dụ dẫn nhập CartPole của bài toán trung tâm nằm ở ghi chú bài giảng (Mục 1) và ở `L09-03` (mạch 2, bước vấn đề của độ chệch của phép cực đại). Bảng hành trình của mạch 2–7 thêm khi sửa xong mạch tương ứng.

### Mục từng trang (đợt sửa 2026-10-28)

#### `L09-01` Bìa: Double DQN và gradient chính sách (bước S1)

- **Trang muốn nói gì:** tên bài và câu luận đề: phép cực đại trên ước lượng có nhiễu cho giá trị chệch lên; tách chọn khỏi đánh giá làm giảm độ chệch này; hàm điểm cho ước lượng không chệch của gradient chính sách.
- **Phục vụ mạch nào và thế nào:** trang tiêu đề của mạch 1. Câu luận đề nêu trước khung "ước lượng từ mẫu và độ chệch" của `L09-02c` cho cả hai nửa bài, thay phụ đề nối hai nửa bằng "rồi".
- **Vấn đề còn lại trước sửa:** phụ đề kể tiến trình, không phải câu luận đề; thiếu đơn vị, năm học; ghi chú diễn giả lấy bài học làm chủ ngữ (CT P01; SV mục 2).
- **Quyết định:** sửa theo khuôn `L08-01`: `h1` tên bài, `h3` "Bài 09 · Học tăng cường", câu luận đề trong `.box`, đơn vị, năm học. Thuật ngữ "hàm điểm (score function)" có tên tiếng Anh ở lần dùng đầu là trang này.
- **Liên kết:** điểm vào bài; trang sau `L09-01b`. Ghi chú diễn giả: mục tiêu DQN của Bài 08 vừa chọn vừa đánh giá → Double DQN, Double Q-learning → chính sách học trực tiếp, hàm điểm, REINFORCE → câu hỏi chung về độ chệch. Mục tiêu hỗ trợ: định hướng cho cả năm mục tiêu.
- **Mật độ:** trước sửa 20 âm tiết, 2 dòng, ghi chú 49 âm tiết. Sau S1 58 âm tiết; sau R1 65 âm tiết (không tính `h1`), 4 dòng nội dung, 0 công thức hiển thị, 1 hộp chữ 1 câu (46 âm tiết, ba dòng hiển thị), ghi chú khoảng 133 âm tiết.
- **Ghi chú bài giảng:** đoạn mở đầu (một đoạn, bốn câu) thay các dòng giảng viên, học kỳ, thời lượng, nguồn; khớp câu luận đề.

#### `L09-01b` Tiên quyết và quy ước, phần Ký hiệu (bước S2)

- **Trang muốn nói gì:** quy ước của bài: MDP quan sát đầy đủ ($S_t$ là quan sát $O_t$ của Bài 08), $\gamma\in[0,1)$, $\mathcal A$ và $m$, $R_{t+1}$ sau $A_t$, $T$, $\rho_0$, $P$, hai cờ $Z_i$, $U_i$, mẫu chuyển của mini-batch.
- **Phục vụ mạch nào và thế nào:** mạch 1; cố định ký hiệu cho công thức nhắc lại ở `L09-01c` (dùng $S$, $Z$, $U$) và cho mạch 5–6 ($\rho_0$, $P$ không phụ thuộc $\theta$).
- **Vấn đề còn lại trước sửa:** không có trang Tiên quyết; quy ước $O=S$ nằm ở `L09-03` với câu "Bài này giả sử…"; $\rho_0$, $P$ dùng ở `L09-20`, `L09-22` mà không định nghĩa; $U$ của Bài 08 không xuất hiện (CT G02, G09, P03; TH "cờ cắt ngắn"; SV mục 2).
- **Quyết định:** thêm. Trang Ký hiệu đặt trước trang Nhắc lại (deck 08 đặt sau) vì công thức nhắc lại viết bằng $S_i$, $Z_i$, $U_i$; đặt ký hiệu trước tránh dùng ký hiệu trước khi nêu. Bảng hai cột như `L08-01c`, năm hàng. Quy ước kỳ vọng $\mathbb E_\pi$ đặt ở `L09-01d`, cạnh chính sách $\pi$.
- **Liên kết:** trước là bìa; sau là `L09-01c`. Mục tiêu hỗ trợ: mục tiêu 2 (cờ trong mục tiêu), mục tiêu 5 ($\rho_0$, $P$ trong giả thiết của định lý).
- **Mật độ:** trang mới. Sau R1 60 âm tiết, bằng trần (dòng Ký hiệu 19, tiêu đề cột 2, năm hàng 9, 8, 8, 8, 6), 6 dòng nội dung, 0 công thức hiển thị, 0 hộp chữ, ghi chú khoảng 131 âm tiết (thêm tương ứng $\mu$, $p$ của Bài 03).
- **Ghi chú bài giảng:** mục "Bảng ký hiệu" (27 hàng, ba cột), đoạn "Quy ước đọc", đoạn về hai vai của $\theta$, tương ứng với giáo trình *Học máy thống kê* và Bài 03; thay mục "Ký hiệu và quy ước" cũ.

#### `L09-01c`, `L09-01d` Tiên quyết và quy ước, phần Nhắc lại (bước S3)

- **Trang muốn nói gì:** `L09-01c`: mục tiêu DQN dạng mặt nạ, hàm mất mát với $\operatorname{sg}$, đồng bộ $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu, mẫu cắt ngắn vẫn bootstrap (Bài 08). `L09-01d`: chính sách là phân phối, $\mathbb E_\pi$ theo $\rho_0$, $\pi$, $P$, lợi tức $G_t$, $q_\pi$ (Bài 03); bất đẳng thức Jensen.
- **Phục vụ mạch nào và thế nào:** mạch 1; cho mạch 2 đối tượng (phép cực đại trong $y_i$) và công cụ (Jensen); cho mạch 3 công thức để sửa thành mục tiêu Double DQN; cho mạch 4–6 chính sách, lợi tức và $q_\pi$.
- **Vấn đề còn lại trước sửa:** mục tiêu DQN không được nhắc lại trên mặt trang nào (SV nghiêm trọng); Jensen dùng ở `L09-06` mà không nhắc lại; $q_\pi$ chỉ xuất hiện ở `L09-30` (CT G09; TH).
- **Quyết định:** thêm hai trang cùng tiêu đề. Một trang không đủ chỗ: bản gộp đầu tiên có đáy 808 px và tràn phải 1 395 px ở 1280×720 (đo bằng `check.py`), nên tách theo nguồn kết quả (Bài 08 | Bài 03 và Jensen). Kế hoạch cho phép thêm `L09-01c` khi cần; trang thứ ba `L09-01d` là lệch nhỏ khỏi chữ của kế hoạch, cùng cách deck 08 dùng ba trang (`L08-01b`, `L08-01b2`, `L08-01c`). Ký hiệu giá trị hành động đúng là $q_\pi$ như Bài 03–08, không phải $Q^\pi$ (xem `outline.md`, mục Ký hiệu).
- **Liên kết:** `L09-01b` → `L09-01c` → `L09-01d` → `L09-02`. Mục tiêu hỗ trợ: mục tiêu 1 (Jensen), 2 (mục tiêu DQN), 5 ($G_t$).
- **Mật độ:** trang mới. Sau R1: `L09-01c` 40 âm tiết (thêm tên tiếng Anh, dòng gọi tên mạng trực tuyến và mạng mục tiêu), 5 dòng (hai công thức hiển thị), 0 hộp chữ, đáy 651 px, ghi chú khoảng 95 âm tiết. `L09-01d` 35 âm tiết ($q_\pi$ viết theo $G_0\mid S_0$ như Định nghĩa 03.16; Jensen cho vector), 4 dòng, 0 hộp chữ, ghi chú khoảng 96 âm tiết.
- **Ghi chú bài giảng:** mục "Kiến thức tiên quyết" tám nhóm in đậm có số hiệu và phát biểu lại: mục tiêu DQN và mạng mục tiêu; hàm mất mát và dừng gradient; kết thúc và cắt ngắn; phạm vi bảo đảm của DQN; hạ gradient; chính sách, lợi tức và giá trị hành động; bất đẳng thức Jensen; kỳ vọng có điều kiện. Bỏ phần ôn DQN dạng "Hai công cụ đã học ở Bài 08" khỏi phần mở đầu (phần này vẫn còn ở mục con của topic-01, viết lại ở bước `L09-03`).

#### `L09-02` Mục tiêu học tập (bước S4)

- **Trang muốn nói gì:** năm việc người học làm được sau bài, mỗi việc ứng một mạch 2–6 và có sản phẩm kiểm được.
- **Phục vụ mạch nào và thế nào:** mạch 1; báo trước sản phẩm của từng mạch để trang Nội dung, trang tiêu đề mạch và bảng tổng kết đối chiếu được.
- **Vấn đề còn lại trước sửa:** tiêu đề "Kết quả học tập" lệch deck 08; bốn thẻ lệch sáu mục tiêu của `outline.md` và không ứng mạch; thẻ "Chính sách: Đọc chính sách như một phân phối…" không kiểm được; ghi chú có câu siêu văn bản (CT P02; SV mục 2).
- **Quyết định:** sửa. Danh sách đánh số năm mục, động từ học tập (Tính, Chọn, Thực hiện), theo đề xuất CT §3.1; mục 2 viết "mục tiêu … Double Q-learning trên cùng mẫu chuyển" để một dòng; mục 4 dùng "hàm mục tiêu $J(\theta)$" để tách khỏi "mục tiêu" $y_i$. Ghi chú diễn giả nêu sản phẩm của từng mục.
- **Liên kết:** trước là `L09-01d`; sau là `L09-02b`.
- **Mật độ:** trước sửa 52 âm tiết, 4 thẻ (8 dòng tính cả tiêu đề thẻ), ghi chú 37 âm tiết. Sau S4 69 âm tiết; sau R1 71 âm tiết (trần 80 của trang mục tiêu; thêm "(maximization bias)" ở lần dùng đầu), 5 dòng (15, 13, 16, 12, 15), 0 công thức hiển thị, 0 hộp chữ, ghi chú khoảng 135 âm tiết (bỏ câu cuối).
- **Ghi chú bài giảng:** mục "Mục tiêu học tập" năm mục cùng thứ tự với trang, mỗi mục có sản phẩm; thay "Mục tiêu quan sát được" bốn mục.

#### `L09-02b` Nội dung (bước S5)

- **Trang muốn nói gì:** bảy phần của bài, mỗi tên trùng tên trang tiêu đề mạch và trỏ tới `#/N`; tài liệu đọc trước.
- **Phục vụ mạch nào và thế nào:** mạch 1; bản đồ bài cho người học và số mạch để đối chiếu với `#/N`.
- **Vấn đề còn lại trước sửa:** không có trang Nội dung (CT G02; SV).
- **Quyết định:** thêm. Bảy mục, mỗi mục là liên kết `#/N` (đã thử bấm cả bảy: mở `L09-01`, `L09-03`, `L09-07`, `L09-16`, `L09-20`, `L09-28`, `L09-33`, là trang đầu mỗi section ngoài; từ bước mạch 2, trang đầu sẽ là trang tiêu đề mạch). Tên mạch theo kế hoạch D1, trừ mạch 5 "Hàm mục tiêu và hàm điểm" (xem `outline.md`). Dòng "Đọc trước:" thêm §13.7 (chính sách Gaussian cho hành động liên tục, dùng ở mạch 4–5) vào danh sách §6.7, §13.1–13.3 của kế hoạch.
- **Liên kết:** trước là `L09-02`; sau là `L09-02c`.
- **Mật độ và ngoại lệ:** 39 âm tiết, 8 dòng (ngoại lệ số dòng như `L08-02b`), 0 công thức, 0 hộp chữ, ghi chú khoảng 118 âm tiết.
- **Ghi chú bài giảng:** "Bảy phần của chương" (mỗi phần kèm `note-topic-id`) và dòng "Đọc trước:" thay bảng "Bảy mạch — 120 phút"; bỏ thời lượng.

#### `L09-02c` Vấn đề trung tâm (bước S6)

- **Trang muốn nói gì:** bài toán của bài (ước lượng không chệch từ mẫu giá trị hành động trong mục tiêu bootstrap và gradient của $J(\theta)$) và câu trả lời có điều kiện của mỗi mạch 2–6.
- **Phục vụ mạch nào và thế nào:** mạch 1; nêu trước kết luận của từng mạch để trang tiêu đề mạch và trang trả lời vấn đề trung tâm `L09-K5` đối chiếu được. Định nghĩa tại chỗ $J(\theta)$, $\widehat Q_a$, $\psi_\theta$.
- **Vấn đề còn lại trước sửa:** không có trang Vấn đề trung tâm và không có khung chung; hai nửa bài nối bằng "rồi" (CT G02, G04).
- **Quyết định:** thêm theo CT §2.3, khuôn `L08-02c` (hộp bài toán, danh sách đánh số từ 2). Dòng 3 viết "Khi chọn và đánh giá độc lập: không chệch lên; Double DQN chỉ giảm độ chệch" để giữ cả kết luận độc lập lẫn giới hạn của Double DQN trong một dòng. Dòng 6 nêu điều kiện đủ đơn giản theo kế hoạch D4 ($\rho_0$, $P$ không phụ thuộc $\theta$; $R$, $\psi_\theta$, $T$ bị chặn); công thức để trong nhóm KaTeX để không ngắt sau dấu bằng. Không đặt hình trên trang (đã đủ sáu dòng); hình `central-problem.svg` nằm trong ghi chú bài giảng.
- **Liên kết:** trước là `L09-02b`; sau là `L09-03` (từ bước mạch 2 là `L09-M2T`).
- **Mật độ và ngoại lệ:** sau R1 83 âm tiết (ngoại lệ, xem mục Ngoại lệ mật độ), 6 dòng, 0 công thức hiển thị, 1 hộp chữ 1 câu, ghi chú khoảng 133 âm tiết (bỏ câu số trang nguồn; thêm lý do không đòi hàm điểm bị chặn và việc $\theta$ đổi vai).
- **Ghi chú bài giảng:** `## 1. Mở đầu` với "Bài toán trung tâm của chương": kết quả kế thừa (Thuật toán 08.13, Nhận xét 08.19), bài toán có số liệu (CartPole: cận $100$, $\max_aQ_\theta(O_0,a)=108{,}5$, $G_0=99{,}3$, bài thực hành Bài 08 mục 7), giới hạn dẫn tới nửa sau (hành động liên tục, lưới gộp trạng thái nguồn tr. 23–25), hình `central-problem.svg` có đoạn đọc hình, năm câu trả lời có điều kiện, đoạn kết nối sang Mục 2.

#### `L09-M2T` Trang tiêu đề mạch 2 (bước S7), điểm vào mạch 2

- **Trang muốn nói gì:** mạch 2 "Độ chệch của phép cực đại" đo độ lệch của phép cực đại trong mục tiêu bootstrap khi ước lượng có nhiễu.
- **Phục vụ mạch nào và thế nào:** điểm vào mạch 2; số "2." khớp mục 2 của `L09-02b` và `#/2` (đã thử: `#/2` và liên kết mục 2 cùng mở `L09-M2T`). Dòng dẫn nêu nhu cầu chung của mạch, trùng nhu cầu của `L09-03`, nên trang là bước `vấn đề` chung của cụm (ghi trong bảng hành trình).
- **Vấn đề còn lại trước sửa:** không có trang tiêu đề mạch (CT G01; SV).
- **Quyết định:** thêm theo khuôn `L08-M2T`; `id="mach-2"`; tên khác tiêu đề `L09-03`; bốn từ khóa là khái niệm của mạch; `data-note-topic-id` là `lec-09-topic-01` (chủ đề của trang nội dung đầu mạch).
- **Liên kết:** kế thừa mục tiêu DQN (`L09-01c`) và Jensen (`L09-01d`); giao cho mạch 3 nguyên nhân của độ chệch.
- **Mật độ:** dòng dẫn 20 âm tiết (trần 25), từ khóa 17 âm tiết, 4 cụm; ghi chú diễn giả khoảng 91 âm tiết.

#### `L09-03` Phép cực đại trong mục tiêu DQN (bước S8)

- **Trang muốn nói gì:** phép cực đại trong $y_i$ có thể làm mục tiêu lệch lên; số đo CartPole cho giá trị ước lượng vượt cận trên của mọi lợi tức.
- **Phục vụ mạch nào và thế nào:** bước vấn đề và ví dụ dẫn nhập của cụm độ chệch; công thức $y_i$ nhắc lại tại chỗ.
- **Vấn đề còn lại trước sửa:** tiêu đề là câu đối lập; hai luận điểm khác loại; "Bài này giả sử…", quy ước $O=S$ lặp; "Replay", "đích"; không "Muốn…/Nhu cầu:", không ví dụ số; SVG `dqn-stability.svg` có câu khẩu hiệu và nhãn tràn (CT P03; SV; R1).
- **Quyết định:** sửa. "Nhu cầu:" với công thức $y_i$ trong dòng; "Ví dụ." CartPole với cận $1/(1-\gamma)=100$; hình mới `cartpole-overestimate.svg` (trục số 90–110: cận 100, $G_0=99{,}3$, $\max_aQ_\theta(S_0,a)=108{,}5$, vượt cận $8{,}5$) thay `dqn-stability.svg`; "Lưu ý:" con số gộp nhiều nguồn sai số. Bỏ quy ước $O=S$ (đã ở `L09-01b`). `dqn-stability.svg` không còn dùng trong deck; tệp đã xóa ở R2.
- **Liên kết:** trước `L09-M2T`; sau `L09-04`. Mục tiêu hỗ trợ: 1.
- **Mật độ:** trước 45 âm tiết, 4 dòng, ghi chú 62; sau S8 43; sau R2 48 âm tiết (cận 100 cho cả lợi tức và giá trị đúng; "chệch" thay "lệch"), 4 dòng chữ và 1 hình, 0 công thức hiển thị, 0 hộp chữ, đáy 650 px, ghi chú khoảng 142.

#### `L09-04` Nhiễu của hành động được chọn (bước S9; tiêu đề đổi ở R2)

- **Trang muốn nói gì:** với $\widehat Q_a=q_a+\varepsilon_a$ không chệch, phép cực đại chọn nhiễu dương lớn và báo nó; đại lượng cần đo là $\mathbb E[\max_a\widehat Q_a]-\max_aq_a$.
- **Phục vụ:** bước trực quan; đặt tên đại lượng cho ví dụ ở trang sau.
- **Vấn đề còn lại trước sửa:** tiêu đề câu kèm tiếng Anh; hình đứng trước khi ví dụ được đặt; $Q_a$ cho giá trị đúng; "sai lệch" (CT P04; SV; TH; R1).
- **Quyết định:** sửa. Chuyển hình xuống `L09-05`; dùng $q_a$ cho giá trị đúng; nhãn "Trực quan."; tên tiếng Anh đã ở `L09-02`.
- **Liên kết:** trước `L09-03`; sau `L09-05`.
- **Mật độ:** trước 13 âm tiết, 2 dòng, 1 hình; sau S9 43; sau R2 46 âm tiết (tiêu đề "Nhiễu của hành động được chọn", nhãn "Định nghĩa."), 5 dòng (một công thức hiển thị), đáy 457 px, ghi chú khoảng 83.

#### `L09-05` Ví dụ: hai hành động có nhiễu ±1 (bước S10)

- **Trang muốn nói gì:** $q_1=q_2=0$, nhiễu $\pm1$ độc lập: từng ước lượng không chệch, $\mathbb E[\max]=\tfrac12$, độ chệch $\tfrac12$.
- **Phục vụ:** bước ví dụ, tính tay.
- **Vấn đề còn lại trước sửa:** tiêu đề không theo dạng "Ví dụ: …"; hai thẻ; thiếu "Diễn giải:" (CT P05; SV).
- **Quyết định:** sửa theo khuôn trang ví dụ: dữ kiện, yêu cầu "Tính", hình bốn cặp (`maximization-bias.svg` vẽ lại: dấu trừ chuẩn, phông không chân, bỏ chấm màu không chú giải và câu khẩu hiệu, ba cặp có cực đại dương viền đậm), một dòng tính, "Diễn giải:". Hình này dùng lại ở `X01` khi sửa mạch 3.
- **Mật độ:** trước 24 âm tiết, 4 dòng (6 tính tiêu đề thẻ); sau S10 28; sau R2 34 âm tiết (thêm dòng ứng dụng $q=(0{,}5;\,0)$ và $q=(3;\,0)$; hình có nhãn cặp $(\widehat Q_1;\widehat Q_2)$, bỏ dòng xác suất lặp trong từng khung), 5 dòng chữ và 1 hình, đáy 691 px, ghi chú khoảng 102.

#### `L09-06` Độ chệch của phép cực đại không âm (bước S11)

- **Trang muốn nói gì:** Mệnh đề (Mệnh đề 09.2 của ghi chú): $\mathbb E[\max_a\widehat Q_a]\ge\max_a\mathbb E[\widehat Q_a]$ với $\mathcal A$ hữu hạn, $\widehat Q_a$ khả tích; không chệch thì độ chệch $\ge0$; điều kiện dấu bằng.
- **Phục vụ:** bước hình thức; Câu hỏi và Lời giải là bước kiểm tra của cụm.
- **Vấn đề còn lại trước sửa:** không nhãn, không giả thiết; "Đây là Jensen vì…"; "có thể bằng nhau"; ghi chú có chỉ dẫn giảng viên (CT P06; SV; TH).
- **Quyết định:** sửa. "Mệnh đề." với giả thiết; "Chứng minh." một dòng, phát biểu lại Jensen tại chỗ; "Ý nghĩa:" điều kiện dấu bằng khi và chỉ khi; "Câu hỏi:" và "Lời giải:" (fragment) kiểm điều kiện dấu bằng. Câu nối nguyên nhân sang mạch 3 đặt trong ghi chú diễn giả (trang đã đủ sáu dòng).
- **Mật độ:** trước 35 âm tiết, 4 dòng, ghi chú 28; sau S11 57; sau R2 50 âm tiết ("Ý nghĩa:" viết bằng $b^*\in\arg\max_aq_a$), 5 khối (7 dòng hiển thị), 0 công thức hiển thị, đáy 585 px, ghi chú khoảng 131 (thêm câu ứng dụng vào DQN).

#### Hành trình khái niệm, mạch 2, cụm "Độ chệch của phép cực đại" (15 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-M2T`, `L09-03` | Mục tiêu DQN (`L09-01c`); CartPole: cận 100, $108{,}5$ | Thấy giá trị ước lượng vượt cận; biết con số gộp nhiều nguồn | Ví dụ dẫn nhập đặt cùng vấn đề |
| Trực giác | `L09-04` | $\widehat Q_a=q_a+\varepsilon_a$ | Phép cực đại chọn nhiễu dương; đại lượng cần đo | Không gộp |
| Ví dụ | `L09-05` | $q=(0;\,0)$, nhiễu $\pm1$ | Độ chệch $\tfrac12$ | Không gộp |
| Hình thức | `L09-06` | Jensen (`L09-01d`) | Mệnh đề có giả thiết, điều kiện dấu bằng | Không gộp |
| Ứng dụng | `L09-05` (dòng cuối, R2), ghi chú diễn giả `L09-06`; ghi chú bài giảng Ví dụ 09.3 | Khoảng cách giá trị đúng $0{,}5$ và $3$; $\widehat Q_a=Q_{\theta^-}(S'_i,a)$ | Độ chệch $0{,}375$ và $0$; độ chệch lớn khi giá trị đúng gần nhau | Gộp với ví dụ trên cùng trang (trang `L09-06` đã đủ dòng) |
| Kiểm tra | `L09-06` (Câu hỏi, Lời giải) | $\widehat Q_1>\widehat Q_2$ hầu chắc chắn | Độ chệch $0$ | Gộp với bước hình thức |

Thời lượng: `L09-M2T` 1, `L09-03` 4, `L09-04` 3, `L09-05` 3, `L09-06` 4 phút. Dữ kiện truyền: hình bốn cặp của `L09-05` dùng lại ở `X01` (mạch 3); nguyên nhân "cùng ước lượng chọn và đánh giá" là đầu vào của `L09-M3T`.

## Bản trước đợt sửa 2026-10-28

Các mục dưới đây mô tả bản trước đợt sửa (sáu section ngoài, 38 trang).


### Hành trình khái niệm

| cụm | chu trình | trang | đầu vào → sản phẩm | cốt lõi | linh hoạt |
|---|---|---|---|---:|---:|
| Cầu nối và sai lệch cực đại | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L09-01`–`L09-10`, `X01` | DQN → nhận dạng, tính và giảm liên hệ chọn–đánh giá | 32 phút | 0 |
| Hai ước lượng dạng bảng | chu trình rút gọn: trực giác → thuật toán → ứng dụng → so sánh → kiểm tra | `L09-11`–`L09-15` | Double DQN → Double Q-learning và cập nhật chéo | 11 phút | 5 phút |
| Chính sách trực tiếp | vấn đề → trực giác → ví dụ → hình thức → kiểm tra | `L09-16`–`L09-19` | giới hạn của aliasing và argmax liên tục → phân phối hành động | 14 phút | 0 |
| Mục tiêu và hàm điểm | vấn đề → trực giác → hình thức → ví dụ → ứng dụng → kiểm tra | `L09-20`–`L09-27`, `X02` | mục tiêu episodic → hàm điểm softmax và Gaussian | 27 phút | 5 phút |
| Gradient chính sách | hình thức → nhân quả → định lý → thuật toán → ứng dụng → kiểm tra | `L09-28`–`L09-33`, `X03` (gồm `L09-28A`, `L09-30A`) | tỷ số xác suất → reward-to-go → phân bố chiếm dụng → REINFORCE | 26 phút | 0 |

### Bản đồ sáu mạch ngoài

| mạch | range | chức năng | kết nối vào | đầu ra |
|---|---|---|---|---|
| 1 | `L09-01`–`L09-03` | Cầu nối từ DQN; quy ước $O=S$. | Bài 08 về DQN | Vấn đề sai lệch cực đại cho mạch 2. |
| 2 | `L09-04`–`L09-10`, `X01` | Nhận dạng, tính và giảm sai lệch cực đại. | Cơ chế còn thiếu ở mạch 1 | Nguyên tắc tách chọn–đánh giá cho mạch 3. |
| 3 | `L09-11`–`L09-15` | Double Q-learning dạng bảng, cập nhật chéo. | Nguyên tắc tách ở mạch 2 | Giới hạn argmax mở đường cho mạch 4. |
| 4 | `L09-16`–`L09-19` | Chính sách là phân phối; hai giao diện softmax/Gaussian. | Giới hạn argmax ở mạch 3 | Giao diện lấy mẫu khả vi cho mạch 5. |
| 5 | `L09-20`–`L09-27`, `X02` | Mục tiêu episodic, giả thiết, hàm điểm. | Giao diện chính sách ở mạch 4 | Hàm điểm softmax và Gaussian cho mạch 6. |
| 6 | `L09-28`–`L09-33` (gồm `L09-28A`, `L09-30A`), `X03` | Tỷ số xác suất, nhân quả, phân bố chiếm dụng, REINFORCE; đọc thêm sai phân hữu hạn. | Hàm điểm ở mạch 5 | Bốn hợp đồng kết bài và cầu nối sang Bài 10. |

Thứ tự vật lý trong mạch 6 là `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33` (thứ tự `lec-09-topic-10` → `lec-09-topic-12` → `lec-09-topic-11` → `lec-09-topic-14` → `lec-09-topic-13`). Lý do đổi thứ tự: giữ chu trình học tập REINFORCE (định lý → thuật toán → ứng dụng → kiểm tra) liền mạch trước khi vào phần mở rộng có thể lược, rồi chốt bằng trang tổng hợp `L09-33`.

Lý do thêm `L09-30A`: nội dung sai phân hữu hạn ở nguồn tr. 33 đã bị bỏ khỏi tuyến chính. Bản đồng bộ khôi phục thành trang “Đọc thêm: sai phân hữu hạn” ngoài tuyến chính, có thể lược, gồm một công thức xấp xỉ gradient và hai thẻ ưu điểm/giới hạn, nối từ hai cách viết gradient sang cầu nối Bài 10. Không thêm ảnh.

Tổng mã: 35 trang không mang mã X + 3 bài tập = 38 mã.

### Bảng note-topic-id → data-slide-id

| note-topic-id | data-slide-id |
|---|---|
| `lec-09-topic-01` | `L09-01`, `L09-02`, `L09-03` |
| `lec-09-topic-02` | `L09-04`, `L09-05`, `L09-06` |
| `lec-09-topic-03` | `L09-07`, `L09-08`, `X01` |
| `lec-09-topic-04` | `L09-09`, `L09-10` |
| `lec-09-topic-05` | `L09-11`–`L09-15` |
| `lec-09-topic-06` | `L09-16`–`L09-19` |
| `lec-09-topic-07` | `L09-20`–`L09-22` |
| `lec-09-topic-08` | `L09-23`–`L09-25`, `X02` |
| `lec-09-topic-09` | `L09-26`, `L09-27` |
| `lec-09-topic-10` | `L09-28`, `L09-28A`, `L09-29` |
| `lec-09-topic-11` | `L09-30` |
| `lec-09-topic-12` | `L09-31`, `L09-32`, `X03` |
| `lec-09-topic-13` | `L09-33` |
| `lec-09-topic-14` | `L09-30A` |

Tổng: 38 `data-slide-id` duy nhất, 38 `data-note-topic-id`, đủ 14 topic và 6 section ngoài.

Các cột thời lượng không tính các trang `X`. Tổng thời lượng vẫn 110 phút cốt lõi + 10 phút linh hoạt = 120 phút chính, cộng 30 phút chữa bài nằm ngoài 120 phút chính, không gọi là vượt giờ. Toàn bộ cầu nối tỷ số xác suất, nhân quả và phân bố chiếm dụng là cốt lõi, riêng `L09-30` và `L09-30A` là mở rộng có thể lược. Phần linh hoạt gồm bảng so sánh ở `L09-14` và nhánh Gaussian ở `L09-26`–`L09-27`; sai phân hữu hạn chỉ còn ở trang đọc thêm `L09-30A`.

### Truyền dữ kiện

- Ví dụ Rademacher từ `L09-05` đi vào `X01`; Jensen ở `L09-06` giải thích kết quả.
- Hai vector $Q_{\theta^-}=(2,7)$ và $Q_\theta=(4,1)$ đi từ bài tập `X01`; bộ số trên trang chiếu `L09-08` là $(5,4)$ và $(3,6)$, hai bộ khác nhau có chủ ý.
- Giao diện chọn–đánh giá ở `L09-07` được đối chiếu với cập nhật chéo ở `L09-11`–`L09-14`.
- Trực giác lấy mẫu ở `L09-17` và hai giao diện ở `L09-19` định kiểu cho softmax `L09-24` và Gaussian `L09-26`.
- Quy ước $(S_t,A_t,R_{t+1})$, $0\le\gamma&lt;1$ và $G_t$ ở `L09-20` được giữ nguyên trong định lý, ước lượng, thuật toán và bài tập.
- Hàm điểm ở `L09-23` đi qua hai ví dụ rồi thành nhân tử trong xác suất quỹ đạo `L09-28` và ước lượng `L09-31`.
- Đặc trưng softmax và xác suất $2/3$ đi từ `L09-25` đến cập nhật `L09-32`; `X03` đổi dấu return để kiểm một cập nhật mới, không chép lại đáp án.

### Chu trình trọng tâm

#### Sai lệch cực đại và Double DQN

Vấn đề ở `L09-03`–`L09-04`; trực giác và ví dụ ở `L09-04`–`L09-05`; hình thức ở `L09-06`–`L09-07`; ví dụ số ở `L09-08`; kiểm tra ở `X01`; hợp đồng tensor ở `L09-09`; giới hạn ở `L09-10`, sau khi công thức Double DQN đã xuất hiện và bài tập đã kiểm cơ chế. `X01` kiểm cơ chế; `L09-10` chốt giới hạn rồi chuyển sang hai bảng.

#### Double Q-learning

Đây là chu trình rút gọn vì vấn đề chọn–đánh giá đã được thiết lập ở cụm trước. Trực giác ở `L09-11`; thuật toán ở `L09-12`; ứng dụng số ở `L09-13`; so sánh ở `L09-14`; kiểm tra ở `L09-15`. `L09-13` được đánh dấu rõ là ứng dụng, không chỉ là ví dụ số.

#### Chính sách trực tiếp và hàm điểm

Vấn đề biểu diễn ở `L09-16`: chính sách tối ưu tất định có thể tồn tại trong MDP quan sát đầy đủ, còn chính sách trực tiếp cung cấp phân phối khả vi, lấy mẫu và hành động liên tục. Trực giác ở `L09-17`; ví dụ hai họ phân phối ở `L09-18`; hình thức và kiểm tra chuẩn hóa ở `L09-19`. Mục tiêu ở `L09-20`–`L09-21`; hợp đồng đạo hàm ở `L09-22`; hình thức hàm điểm ở `L09-23`, `L09-24`, `L09-26`; ví dụ ở `L09-25`, `L09-27`; kiểm tra ở `X02`.

#### REINFORCE

Tỷ số xác suất ở `L09-28` viết $J=\int G_0p_\theta d\tau$ rồi likelihood ratio; `L09-28A` tách phân tích quỹ đạo $p_\theta(\tau)=\rho_0\prod\pi_\theta P$ và $\nabla\log p=\sum_t\psi_t$, một luận điểm trung tâm nối sang `L09-29`. Hai trang lân cận quanh `L09-28A` đã rà: `L09-27` kết cụm hàm điểm, `L09-29` mở cầu nối nhân quả; ranh giới section 5→6 nằm giữa `X02` và `L09-28`. `L09-30` là phần mở rộng về phân bố chiếm dụng, có thể lược khi thiếu thời gian; `L09-30A` là trang đọc thêm sai phân hữu hạn, cũng có thể lược. Thuật toán ở `L09-31`; ứng dụng softmax ở `L09-32`; kiểm tra ở `X03`; tổng hợp ở `L09-33`. Thứ tự vật lý trong mạch 6 là `L09-28`, `L09-28A`, `L09-29`, `L09-31`, `L09-32`, `X03`, `L09-30`, `L09-30A`, `L09-33`: chu trình REINFORCE cốt lõi đi liền trước, phần mở rộng có thể lược nằm giữa `X03` và trang tổng hợp.

### Từng trang chiếu

| mã | luận điểm trung tâm | bước | câu nối |
|---|---|---|---|
| `L09-01` | Bài tách chọn–đánh giá rồi tối ưu chính sách. | mở | Nối từ DQN. |
| `L09-02` | Bốn kết quả kiểm chứng được. | định hướng | Chuyển vào cầu nối. |
| `L09-03` | Cơ chế ổn định DQN chưa sửa max bias. | vấn đề | Mở sai lệch. |
| `L09-04` | max chọn cả nhiễu thuận lợi. | trực giác | Dẫn tới ví dụ. |
| `L09-05` | Hai ước lượng không chệch tạo max lệch $0,5$. | ví dụ | Chuẩn bị Jensen. |
| `L09-06` | Jensen cho dấu không nghiêm. | hình thức | Cần tách hai vai trò. |
| `L09-07` | Online chọn, target đánh giá. | thuật toán | Đi vào ca số. |
| `L09-08` | DQN và DDQN cho 5,5 và 4,6. | ví dụ | Bổ sung hợp đồng. |
| `L09-09` | Miền, kích thước lô và đường gradient là một hợp đồng. | hình thức | Chốt thuật toán. |
| `L09-10` | Hai mạng sâu còn tương quan. | giới hạn | Kiểm lại cơ chế bằng số. |
| `X01` | Tính max bias và hai đích sau khi đã có công thức; bộ số mới $(2,7)$, $(4,1)$ cho $6{,}6$ và $2{,}6$. | kiểm tra | Sang hai bảng độc lập hơn. |
| `L09-11` | Double Q dùng cập nhật chéo. | trực giác | Viết công thức. |
| `L09-12` | Đích từng trường hợp chỉ lấy argmax khi không kết thúc. | thuật toán | Đi vào số. |
| `L09-13` | Áp dụng cập nhật cho $y=1,9$, $Q_1^{new}=3,79$. | ứng dụng | So sánh hai thuật toán. |
| `L09-14` | Double Q khác Double DQN. | so sánh | Kiểm hiểu. |
| `L09-15` | Bốn câu chốt học giá trị. | kiểm tra | Mở chính sách. |
| `L09-16` | Chính sách trực tiếp cho phân phối khả vi và miền liên tục; không sửa aliasing. | vấn đề, phạm vi | Xây giao diện lấy mẫu. |
| `L09-17` | Chính sách gán xác suất hoặc mật độ để lấy mẫu hành động. | trực giác | Chọn họ phân phối. |
| `L09-18` | Miền hành động quyết định họ phân phối. | ví dụ | So giao diện. |
| `L09-19` | Softmax và Gaussian có giao diện khác nhau. | hình thức, kiểm tra | Đặt mục tiêu học. |
| `L09-20` | $J$, $G_t$ và miền $0\le\gamma&lt;1$ dùng quy ước nhất quán. | vấn đề | Tối ưu theta. |
| `L09-21` | Gradient ascent tối ưu trực tiếp $J$. | hình thức | So với sai phân. |
| `L09-22` | Đạo hàm cần $\rho_0,P$ độc lập tham số, support cố định và khả tích. | giả thiết | Định nghĩa hàm điểm. |
| `L09-23` | Hàm điểm cần xác suất dương. | hình thức | Tính cho softmax. |
| `L09-24` | Hàm điểm softmax giữ $\phi$ cố định và nằm trong $\mathbb R^d$. | hình thức | Đi vào ví dụ. |
| `L09-25` | Hàm điểm chọn hành động 1 là $(1/3,-1/3)$. | ví dụ | Sang hành động liên tục. |
| `L09-26` | Hàm điểm Gaussian giữ $\phi,\sigma^2$ cố định và có kích thước $d$. | hình thức | Đi vào ví dụ. |
| `L09-27` | Hàm điểm Gaussian là $(1,5,3)$. | ví dụ | Kiểm hai họ. |
| `X02` | Tính hàm điểm và kiểm kỳ vọng bằng không. | kiểm tra | Sang tỷ số xác suất. |
| `L09-28` | $J=\int G_0p_\theta d\tau$ và $\nabla J=\mathbb E[G_0\nabla\log p]$. | hình thức | Tách phân tích quỹ đạo. |
| `L09-28A` | $p_\theta(\tau)=\rho_0\prod\pi_\theta P$ và $\nabla\log p=\sum_t\psi_t$. | hình thức | Dùng nhân quả. |
| `L09-29` | Kỳ vọng có điều kiện của hàm điểm bằng không cho tổng hoặc tích phân. | cầu nối nhân quả | Gom theo phân bố chiếm dụng. |
| `L09-30` | Mở rộng: trọng số $\gamma^t$ tạo phân bố chiếm dụng và nối $G_t$ với $Q^\pi$; có thể lược. | định lý | Thành ước lượng mẫu. |
| `L09-31` | Thu dưới $\theta_{old}$, cộng $\gamma^tG_t\psi_t$ rồi cập nhật. | thuật toán | Đi vào số. |
| `L09-32` | Cập nhật softmax tăng xác suất từ $2/3$ lên khoảng $0,710$. | ứng dụng | Kiểm cả tham số và xác suất. |
| `X03` | Tính tham số, xác suất mới khi return âm và return hai bước; giữ $\theta_{old}$. | kiểm tra | Sang phần mở rộng. |
| `L09-30A` | Đọc thêm: sai phân hữu hạn, xấp xỉ $\partial J/\partial\theta_k\approx[J(\theta+\epsilon u_k)-J(\theta)]/\epsilon$; ưu điểm không cần đạo hàm giải tích, giới hạn nhiễu và chi phí đánh giá; có thể lược. | đọc thêm | Nối hai cách viết gradient sang cầu nối Bài 10. |
| `L09-33` | Bốn hợp đồng cần giữ: sai lệch cực đại, Double DQN, chính sách, REINFORCE. | tổng hợp | Cầu nối baseline và actor–critic. |
