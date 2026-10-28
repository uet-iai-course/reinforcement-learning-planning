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
| 3 | `L09-06b` | Ví dụ: hai bản ước lượng độc lập | thêm | Bước trực giác–ví dụ còn thiếu cho việc tách (nguồn tr. 14) | chưa có | 3.2 (S13) |
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
| 4 | `L09-16b` | Ví dụ: lưới gộp trạng thái, chính sách ngẫu nhiên | thêm | Tách từ `L09-16`; $h_2=h_4=4$ | chưa có | 4.3 (S26) |
| 4 | `L09-17`, `L09-18`, `L09-19` | Phân phối hành động có tham số; Ví dụ: phân phối hành động; Chính sách softmax và chính sách Gaussian | sửa | Số liệu nguồn tr. 27–28; hết tràn `L09-19` | 4.2–4.4 | 4.4–4.6 |
| 5 | `L09-M5T` | 5. Hàm mục tiêu và hàm điểm | thêm | Trang tiêu đề mạch, điểm vào mạch 5 | chưa có | chưa có |
| 5 | `L09-20`, `L09-21` | Hàm mục tiêu của một chính sách; bước tăng gradient | sửa | Vấn đề và ví dụ trước định nghĩa; $\tau$, $p_\theta$ định nghĩa trước khi dùng | 5.1–5.2 | 5.1–5.2 |
| 5 | `L09-30A` | Ước lượng gradient bằng sai phân hữu hạn | sửa, chuyển về | Trang vấn đề của hàm điểm theo nguồn tr. 33 | 5.3 | 5.3 |
| 5 | `L09-23`–`L09-27`, `X02` | Hàm điểm; softmax; ví dụ; Gaussian; ví dụ; bài tập | sửa; `X02` chuyển xuống sau `L09-27` | Bài tập không dùng công thức chưa dạy | 5.4–5.9 | 5.4–5.9 |
| 5 | `L09-25b` | Kỳ vọng của hàm điểm | thêm (bước mạch 5) | Mệnh đề $\mathbb E_{A\sim\pi_\theta}[\psi_\theta]=0$ có giả thiết, sau ví dụ softmax | chưa có | 5.8 (S37) |
| 6 | `L09-M6T` | 6. Gradient chính sách và REINFORCE | thêm | Trang tiêu đề mạch, điểm vào mạch 6 | chưa có | chưa có |
| 6 | `L09-28`, `L09-22`, `L09-28A`, `L09-29` | Gradient của $J$ theo tỉ số xác suất; giả thiết; xác suất quỹ đạo; lợi tức từ thời điểm $t$ | sửa; `L09-22` chuyển về cạnh `L09-28` | Giả thiết đặt cạnh chỗ dùng | 6.1–6.4 | 6.1–6.4 |
| 6 | `L09-29b` | Ví dụ: lượt hai bước | thêm | Ví dụ cho bước bỏ phần thưởng quá khứ | chưa có | chưa có |
| 6 | `X03b` | Bài tập: cập nhật REINFORCE (lời giải) | thêm (bước mạch 6) | Lời giải từng bước trên trang sau vì câu hỏi có thẻ dữ kiện | chưa có | 6.11 (S51) |
| 6 | `L09-30` | Định lý gradient chính sách | sửa, chuyển lên trước REINFORCE | Kết quả chính của nguồn tr. 39 | 6.5 | 6.5 |
| 6 | `L09-32`, `L09-31`, `X03` | Ví dụ: một cập nhật REINFORCE; Thuật toán. REINFORCE; bài tập | sửa; `L09-32` trước `L09-31` | Ví dụ tính tay trước thuật toán | 6.6–6.8 | 6.6–6.8 |
| 7 | `L09-M7T`, `L09-K1`–`L09-K7` | Tổng kết và chuyển tiếp | thêm | Bảng kết quả, bảng phương pháp, bài tổng hợp, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, bài tập về nhà, dòng nối Bài 10 | chưa có | chưa có |
| 7 | `L09-33` | (nội dung vào `L09-K1`) | bỏ (đã bỏ ở bước mạch 7) | Tổng kết dạng thẻ "hợp đồng", vượt trần 80 | 7.1 (tạm) | 7.1 (tạm) |
| 7 | `L09-K1b`, `L09-K2b` | Kết quả và giả thiết của bài (tiếp); So sánh bốn phương pháp (tiếp) | thêm (bước mạch 7) | Tách bảng như `L08-34`/`L08-34b`, `L08-K1`/`L08-K1b` để giữ trần 80 và đáy dưới 702 px | chưa có | 7.3, 7.5 (S54, S56) |

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

#### Mạch 3 "Tách chọn và đánh giá" (bước S12–S23)

| bước | trang | tiêu đề trước → sau | quyết định và lý do | âm tiết trước → sau | dòng, đáy | ghi chú diễn giả |
|---|---|---|---|---|---|---|
| S12 | `L09-M3T` | — → "3. Tách chọn và đánh giá" | thêm; điểm vào mạch 3, `id="mach-3"`; dòng dẫn nêu nhu cầu chung của mạch; `data-note-topic-id` `lec-09-topic-17` | — → dẫn 23, khóa 18 | 2; 364 px | khoảng 106 |
| S13 | `L09-06b` | — → "Ví dụ: hai bản ước lượng độc lập" | thêm; bước trực quan và ví dụ còn thiếu cho việc tách (nguồn tr. 14); hình mới `double-estimator.svg` | — → 37 | 4 + hình; 685 px | khoảng 105 |
| S14 | `L09-07` | "Double DQN tách chọn và đánh giá" → "Mục tiêu Double DQN" | sửa; mở bằng "Nhu cầu:" (giới hạn của mục tiêu DQN), không bằng tên; dạng mặt nạ $(1-Z_i)$ với $\operatorname{sg}$; "Lưu ý:" dạng từng trường hợp cho cùng giá trị; `dqn-vs-ddqn.svg` vẽ lại (hai hàng, "mạng trực tuyến", "mạng mục tiêu", không tràn); bỏ kiểu nội dòng `max-height` | 16 → 27 | 3 + hình; 750 → 608 px | khoảng 91 |
| S15 | `L09-08` | "Hai đích có thể khác nhau" → "Ví dụ: một mẫu chuyển, hai mục tiêu" | sửa; bảng chữ thay bằng hình có số `ddqn-example.svg` (hàng chọn, hàng đánh giá); hai dòng tính; "Diễn giải:" $y^{\mathrm{DDQN}}\le y^{\mathrm{DQN}}$ | 12 + bảng → 24 | 4 + hình; 640 px | khoảng 88 |
| S16 | `L09-09` | "Miền, kích thước và đường gradient" → "Thuật toán Double DQN" | sửa, đứng trước `X01`; "Thuật toán." như Thuật toán 08.13 với năm bước, chỉ bước 3 khác; kích thước mảng | 16 → 44 | 7 (giả mã, ngoại lệ); 606 px | khoảng 91 |
| S17 | `X01` | "Bài tập: sai lệch và hai đích" → "Bài tập: mục tiêu DQN và Double DQN" | sửa; "Câu hỏi:" tự đủ dữ kiện $(2;7)/(4;1)$, $\gamma=0{,}8$, (a) $Z=0$, (b) $Z=1$; bỏ câu bốn cặp; "Lời giải:" từng bước trong fragment | 23 → 29 | 4; 412 px | khoảng 63 |
| S18 | `L09-10` | "Hai mạng vẫn có tương quan" → "Phạm vi của Double DQN" | sửa; bỏ hộp câu chung; bốn dòng có điều kiện, thêm ví dụ chệch âm $-0{,}125$; số đo Lunar Lander trong ghi chú diễn giả | 58 → 60 | 4; 344 px | khoảng 94 |
| S19 | `L09-11` | "Double Q-learning dùng hai bảng riêng" → "Double Q-learning dạng bảng" | sửa; mở bằng "Nhu cầu:"; `double-q-cross-update.svg` vẽ lại (nhãn "chọn ngẫu nhiên, mỗi nhánh 1/2", mũi tên đủ đầu, không tràn) | 27 → 36 | 3 + hình; 560 px | khoảng 82 |
| S20 | `L09-13` | "Áp dụng cập nhật chéo" → "Ví dụ: một cập nhật Double Q-learning" | sửa, chuyển trước `L09-12`; số của ví dụ A $(3;6)/(5;4)$, $Q_1(S,A)=4$ → $4{,}06$; hình `double-q-example.svg`; so với Double DQN trên cùng số | 3 + công thức → 25 | 4 + hình; 694 px | khoảng 73 |
| S21 | `L09-12` | "Cập nhật chéo theo trạng thái kết thúc" → "Thuật toán Double Q-learning" | sửa; đầu vào, khởi tạo, hành vi $Q_1+Q_2$, đồng xu $1/2$, cập nhật có mặt nạ, dừng lượt; ghi chú: độc lập chỉ lý tưởng | 16 → 34 | 7 hiển thị (giả mã, một công thức hiển thị, ngoại lệ); 613 px | khoảng 99 |
| S22 | `L09-14` | "Hai cách tách không đồng nhất" → "So sánh DQN, Double DQN và Double Q-learning" | sửa; ba phương pháp, năm tiêu chí, thêm "quan hệ hai ước lượng" và "chệch lên" | 26 → 55 (trần 80) | bảng 5 hàng; 559 px | khoảng 94 |
| S23 | `L09-15` | "Kiểm tra phần học giá trị" → "Bài tập: Double DQN và Double Q-learning" | sửa; "Câu hỏi:" bốn câu, "Lời giải:" fragment, bỏ "Đáp án"; dòng "Giới hạn chung:" là đầu ra cho mạch 4 | 38 → 57 | 4; 440 px | khoảng 72 |

Ngoại lệ mật độ mạch 3: `L09-09` 7 dòng (một dòng mở, năm bước giả mã, một dòng kích thước) và `L09-12` 7 dòng hiển thị (giả mã có một công thức hiển thị): `CLAUDE.md` cho phép giả mã tới tám dòng trên một trang; tách sẽ cắt rời thứ tự bước. `L09-14` 55 âm tiết theo trần 80 của bảng so sánh.

##### Hành trình khái niệm, mạch 3, cụm "Ước lượng kép và Double DQN" (khoảng 17 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-M3T`, `L09-06b` ("Nhu cầu:"), `L09-07` ("Nhu cầu:") | Nguyên nhân độ chệch (mạch 2) | Biết cần tách chọn khỏi đánh giá | Dòng dẫn của trang tiêu đề là vấn đề chung |
| Trực quan + ví dụ | `L09-06b` | $q=(0;\,0)$, hai bản nhiễu $\pm1$ | Giá trị báo cáo kỳ vọng $0$ | Trực quan nằm trong ghi chú diễn giả và ghi chú bài giảng |
| Hình thức | `L09-06c` (mệnh đề, thêm ở R3), `L09-07` (mục tiêu), `L09-09` (thuật toán) | Thuật toán 08.13 | Mệnh đề ước lượng kép; mục tiêu dạng mặt nạ; năm bước, chỉ bước 3 khác | Mệnh đề 09.4 của ghi chú bài giảng ánh xạ `L09-06c` |
| Ứng dụng | `L09-08` | $(5;4)/(3;6)$ | $5{,}5$ và $4{,}6$ | Ví dụ số đặt sau trang mục tiêu, trước trang thuật toán |
| Kiểm tra | `X01`, `L09-10` | $(2;7)/(4;1)$; ví dụ $(0{,}5;0)$ | $6{,}6$ và $2{,}6$; chệch âm $-0{,}125$ | Phạm vi gộp vào kiểm tra |

##### Hành trình khái niệm, mạch 3, cụm "Double Q-learning" (khoảng 13 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-11` ("Nhu cầu:") | Mạng mục tiêu là bản sao trễ | Cần hai ước lượng học trên mẫu khác nhau | Không gộp |
| Trực quan | `L09-11` (hình cập nhật chéo) | Hai bảng, đồng xu | Mỗi mẫu một bảng | Gộp với vấn đề |
| Ví dụ | `L09-13` | $(3;6)/(5;4)$, $Q_1(S,A)=4$ | $a^*=2$, $y_1=4{,}6$, $4{,}06$ | Đặt trước thuật toán |
| Hình thức | `L09-12` | Q-learning (Bài 06) | Thuật toán đầy đủ | Không gộp |
| Ứng dụng | `L09-14` | Ba phương pháp | So sánh theo năm tiêu chí | Không gộp |
| Kiểm tra | `L09-15` | Bốn phân biệt | Lời giải; giới hạn chung cho mạch 4 | Không gộp |

Thời lượng mạch 3: `L09-M3T` 1, `L09-06b` 3, `L09-07` 3, `L09-08` 3, `L09-09` 3, `X01` 2, `L09-10` 2, `L09-11` 2, `L09-13` 3, `L09-12` 3, `L09-14` 2, `L09-15` 3 phút; tổng 30. Dữ kiện truyền: số của ví dụ A dùng lại ở `L09-13` với vai đổi tên ($Q_1$ vai $Q_\theta$, $Q_2$ vai $Q_{\theta^-}$); dòng "Giới hạn chung:" của `L09-15` là đầu vào của `L09-M4T`.


##### Rà lại mạch 3 (bước R3): thay đổi trang và mật độ

| trang | thay đổi ở R3 | âm tiết sau R3 | đáy |
|---|---|---|---|
| `L09-M3T` | ghi chú diễn giả rút còn khoảng 91 (trần 100 của trang tiêu đề mạch) | dẫn 23, khóa 18 | 364 px |
| `L09-06b` | dữ kiện một dòng (xác suất $1/2$); "Diễn giải:" nêu hai giả thiết; nhãn hình là kỳ vọng có điều kiện; hình thấp hơn | 40 | 654 px |
| `L09-06c` (mới) | "Ước lượng kép không chệch lên": "Mệnh đề." (giả thiết độc lập, bản đánh giá không chệch, $a^*$ là hàm của bản A), "Chứng minh." một dòng, "Ý nghĩa:" chệch âm với $q=(0{,}5;\,0)$; ánh xạ Mệnh đề 09.4 của ghi chú bài giảng. Lý do thêm: kết quả chính của mạch (dòng 3 của `L09-02c`) chưa có trang kết quả | 45 | 447 px |
| `L09-09` | ngân sách $t_{\mathrm{end}}$ ($T$ dành cho bước kết thúc lượt); gọi tên $\mathcal D$, $\epsilon_{\mathrm{exp}}$, $N_{\mathrm{start}}$, $F$ tại chỗ | 58 | 614 px |
| `L09-10` | bỏ dòng chệch âm (đã ở `L09-06c`); "việc thiếu bảo đảm hội tụ" | 52 | 316 px |
| `L09-13` | nhãn hàng trên của hình "bảng chọn" | 25 | 694 px |
| `L09-14` | hàng "độ chệch của mục tiêu": $\ge0$ (Mệnh đề 09.2) / không bảo đảm hết chệch lên; phải đo / $\le0$ nếu bản đánh giá không chệch, độc lập (chỉ lý tưởng) | 73 (trần 80) | 654 px |
| `L09-15` | "Giới hạn chung:" phân biệt xác suất hành động được học với $\epsilon_{\mathrm{exp}}$-tham lam (ghi chú diễn giả); Lời giải (4) "một ô của một bảng" | 58 | 446 px |

Hành trình khái niệm cụm "Ước lượng kép và Double DQN", sau R3: bước "Hình thức" gồm `L09-06c` (mệnh đề ước lượng kép), `L09-07` (mục tiêu), `L09-09` (thuật toán); bước "Kiểm tra" gồm `X01` và `L09-10`; dòng "Ý nghĩa:" của `L09-06c` thay dòng chệch âm cũ ở `L09-10`. Thời lượng mạch 3 sau R3: `L09-06c` 2 phút; `L09-10` 1 và `L09-11` 1 (mỗi trang bớt 1 phút); tổng vẫn 30.

#### Mạch 4 "Chính sách tham số hóa" (bước S24–S29)

| bước | trang | tiêu đề trước → sau | quyết định và lý do | âm tiết trước → sau | dòng, đáy | ghi chú diễn giả |
|---|---|---|---|---|---|---|
| S24 | `L09-M4T` | — → "4. Chính sách tham số hóa" | thêm; `id="mach-4"`; dòng dẫn nhận giới hạn chung của mạch 3 (xác suất hành động không được học, cần $\max$ trên $\mathcal A$); `data-note-topic-id` `lec-09-topic-06` | — → dẫn 18, khóa 13 | 2; 328 px | khoảng 94 |
| S25 | `L09-16` | "Chính sách trực tiếp là một lựa chọn biểu diễn" → "Giới hạn của chính sách tham lam theo $Q$" | tách, sửa; mở bằng "Nhắc lại:" giới hạn vừa nêu ở `L09-15`; ví dụ lưới gộp trạng thái vẽ lại đúng nguồn tr. 23 (`aliased-grid-policy.svg`: năm ô, hai ô xám $x=1$, X, \$, chính sách Đông ở hai ô xám, kẹt ô 4 ↔ ô 5); bỏ kết luận ngược nguồn và hai thẻ; hết tràn | 75 → 47 | 3 + hình; 846 → 634 px | khoảng 103 |
| S26 | `L09-16b` (mới) | — → "Ví dụ: lưới gộp trạng thái, chính sách ngẫu nhiên" | thêm (tách từ `L09-16`); nguồn tr. 25: Đông/Tây xác suất $\tfrac12$; $h_2=\tfrac12\cdot2+\tfrac12(2+h_2)=4$; "Diễn giải:" so với chính sách tất định (kẹt) và chính sách theo ô ($h_2=2$); "Lưu ý:" Định lý 04.25 có điều kiện; hình mới `aliased-grid-stochastic.svg` | — → 56 | 4 + hình; 680 px | khoảng 102 |
| S27 | `L09-17` | "Chính sách cho xác suất hành động" → "Chính sách tham số hóa" | sửa; "Nhu cầu:" nêu hai lý do (học xác suất; hành động thực như góc lái); "Định nghĩa." có tên tiếng Anh (lần dùng đầu trên mặt trang mạch 4); điều khiển, học; "lợi tức" thay "return"; bỏ "kernel", "sigma-đại số" trong ghi chú | 40 → 51 | 4; 410 px | khoảng 87 |
| S28 | `L09-18` | "Hai họ phân phối theo miền hành động" → "Ví dụ: phân phối hành động" | sửa; số liệu nguồn tr. 27–28 (đều $\tfrac14$; phân loại $(0{,}1;0{,}2;0{,}2;0{,}5)$); `policy-distributions.svg` vẽ lại (cột có số, Gaussian có $a_{\min}$, $a_{\max}$ và đuôi ngoài miền); bỏ hai thẻ | 25 → 27 | 2 + hình; 546 px | khoảng 88 |
| S29 | `L09-19` | "Hai giao diện chính sách" → "Chính sách softmax và chính sách Gaussian" | sửa; bảng ba hàng (miền, công thức $\pi_\theta$, chuẩn hóa); "Câu hỏi:"/"Lời giải:" có lý do; dòng cuối là đầu ra cho mạch 5 ($J(\theta)$); bỏ "Đáp án"; hết tràn | 30 → 49 | bảng 3 hàng + 3 dòng; 792 → 596 px | khoảng 85 |

##### Hành trình khái niệm, mạch 4, cụm "Chính sách tham số hóa" (15 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-M4T`, `L09-16` | Giới hạn chung của mạch 3; lưới năm ô | Mọi chính sách tất định theo đặc trưng có ô kẹt | Ví dụ dẫn nhập đặt cùng vấn đề |
| Trực quan | `L09-16b` (ghi chú diễn giả), ghi chú bài giảng | Ngẫu nhiên tránh kẹt, không biết ô | — | Gộp với ví dụ |
| Ví dụ | `L09-16b` | Đông/Tây $\tfrac12$ | $h_2=h_4=4$; theo ô $h_2=2$ | Không gộp |
| Hình thức | `L09-17` (Định nghĩa), `L09-19` (hai họ) | Chính sách Markov dừng (Bài 03) | $\pi_\theta$ khả vi; softmax, Gaussian | Không gộp |
| Ứng dụng | `L09-18` | Bốn hành động; góc lái | Phân phối phân loại, Gaussian, miền bị chặn | Ví dụ số của nguồn đặt trước bảng hình thức của hai họ |
| Kiểm tra | `L09-19` (Câu hỏi, Lời giải) | Góc lái trong một khoảng | Chọn Gaussian, cắt hoặc biến đổi | Gộp với hình thức |

Thời lượng mạch 4: `L09-M4T` 1, `L09-16` 3, `L09-16b` 3, `L09-17` 3, `L09-18` 2, `L09-19` 3 phút; tổng 15. Dữ kiện truyền: dòng cuối `L09-19` ("Còn thiếu: $J(\theta)$") là đầu vào của `L09-M5T`; ví dụ softmax hai hành động $\theta=(\ln2;0)$ của ghi chú bài giảng là bài toán một bước dùng ở mạch 5–6.

Lệch khỏi nguồn (mạch 4): nguồn tr. 22 (học tăng cường dựa trên giá trị, tham số hóa tuyến tính, $\epsilon$-tham lam) gộp vào "Nhắc lại:" của `L09-16`; tr. 24 (câu hỏi "chuyện gì xảy ra nếu có hai hành động tốt gần nhau?") chuyển thành phép tính tất định của `L09-16`; tr. 29 (softmax theo khoảng cách tới vật cản) chỉ nêu trong ghi chú bài giảng; tr. 31 (leo đồi, giải thuật di truyền) để cho mạch 5.


##### Rà lại mạch 4 (bước R4): thay đổi trang và mật độ

| trang | thay đổi ở R4 | âm tiết sau R4 | đáy |
|---|---|---|---|
| `L09-16` | đặc trưng $x(s)$ phân biệt ô 1, 3, 5, gộp ô 2 và ô 4 ($x=\mathrm g$); mô hình chuyển trong chú thích hình (đi một ô, tường đứng yên, X là ô kẹt); ghi chú diễn giả: hai trong năm ô, Bắc/Nam, sai khác có chủ ý | 47 | 678 px |
| `L09-16b` | dữ kiện nêu ô 1 Đông, ô 3 Nam, ô 5 Tây; "Diễn giải:" tiêu chí trung bình trên năm ô ($3{,}8$ bước); "Lưu ý:" đủ điều kiện (chính sách theo ô); nguồn ghi phép tính bổ sung | 51 | 637 px |
| `L09-17` | tiêu đề "Phân phối hành động có tham số" (khác tên mạch) | 51 | 410 px |
| `L09-19` | dòng cuối dùng nhãn "Lưu ý:" | 51 | 598 px |

Sai khác có chủ ý so với nguồn (mạch 4): nguồn tr. 23 viết $x(s,a)=1$ ở ô xám, $0$ nơi khác; đặc trưng đó gộp cả ba ô trắng nên lớp chính sách tất định theo đặc trưng còn hẹp hơn, và chính sách ô trắng dùng trong ví dụ không thuộc lớp. Bài dùng đặc trưng chỉ gộp hai ô xám để giữ đúng kết luận tr. 24–25. Mô hình chuyển (đi một ô, tường đứng yên, X là ô kẹt) và mọi số bước, giá trị là phần bổ sung; nguồn chỉ cho xác suất $0{,}5$.

#### Mạch 5 "Hàm mục tiêu và hàm điểm" (bước S30–S40)

| bước | trang | tiêu đề trước → sau | quyết định và lý do | âm tiết trước → sau | dòng, đáy | ghi chú diễn giả |
|---|---|---|---|---|---|---|
| S30 | `L09-M5T` | — → "5. Hàm mục tiêu và hàm điểm" | thêm; `id="mach-5"`; dòng dẫn theo `outline.md` nhận đầu ra của `L09-19` ($J(\theta)$ còn thiếu); khóa kết thúc bằng "Hàm điểm Gaussian" (khoảng trắng không ngắt); `data-note-topic-id` `lec-09-topic-07` | — → dẫn 19, khóa 16 | 2; 371 px | khoảng 95 |
| S31 | `L09-20` | "Mục tiêu episodic và chỉ số quỹ đạo" → "Hàm mục tiêu của chính sách" | sửa; mở bằng "Nhu cầu:" nối từ `L09-19`; ví dụ dẫn nhập trên hình thẻ dữ kiện mới `one-step-card.svg` ($J=2$) trước "Định nghĩa."; bỏ $\tau$, $p_\theta$ (định nghĩa ở mạch 6), viết $\mathbb E_{\pi_\theta}$; "hầu chắc chắn" thay "gần như chắc chắn"; quy ước hấp thụ thành "Giả thiết:"; bỏ câu chỉ đường "$\gamma^t$ sẽ trở lại"; tên tiếng Anh "objective function" | 31 → 42 | 4 + hình; 598 → 649 px | khoảng 74 |
| S32 | `L09-21` | "Tối ưu trực tiếp tham số chính sách" → "Bước tăng gradient" | sửa; "Nhắc lại:" hạ gradient của DQN (dấu trừ) đối chiếu dấu cộng; bỏ hai thẻ (thẻ "Ước lượng" nêu lời giải trước vấn đề); ví dụ $\nabla_\theta J=(\tfrac23;\,-\tfrac23)$ khi biết $r$; "Lưu ý:" chỉ đo được $J$ qua lượt mẫu (dẫn vào `L09-30A`); ghi chú bỏ câu quy trình "Sai phân hữu hạn không còn trong tuyến bài", thêm câu hỏi nguồn tr. 30 và cách không dùng gradient tr. 31 | 24 → 40 | 6; 564 → 597 px | khoảng 112 |
| S33 | `L09-30A` | "Đọc thêm: sai phân hữu hạn" → "Ước lượng gradient bằng sai phân hữu hạn" | sửa, đã chuyển về ở C0; trang vấn đề của hàm điểm theo nguồn tr. 33; định nghĩa $u_k$ trên mặt trang; thẻ dữ kiện cạnh công thức; ví dụ $0{,}655$ so với $\tfrac23$; "Lưu ý:" $d+1$ giá trị $J$, mỗi giá trị từ nhiều lượt; bỏ hai thẻ và câu phân tuyến trong ghi chú | 19 → 42 | 5 + hình; 587 → 608 px | khoảng 116 |
| S34 | `L09-23` | "Hàm điểm (score function) cần xác suất dương trên mẫu" → "Hàm điểm" | sửa; thứ tự trực quan → ví dụ → định nghĩa (trước đây mở bằng định nghĩa); ví dụ tính tay $\nabla_\theta\log\pi_\theta(1\mid s)=(\tfrac13;\,-\tfrac13)$ nêu lại dữ kiện tại chỗ; "Lưu ý:" miền hỗ trợ cố định; ghi chú: $\log$ là logarit tự nhiên, phản ví dụ miền hỗ trợ đổi theo $\theta$ | 26 → 50 | 5; 545 → 622 px | khoảng 97 |
| S35 | `L09-24` | giữ "Hàm điểm của chính sách softmax" | sửa; "Mệnh đề." + "Chứng minh." một dòng; `softmax-score.svg` vẽ lại thành hình học (ba đặc trưng, trọng tâm theo $\pi_\theta$, ba mũi tên $\psi_\theta$, xác suất $0{,}5$; $0{,}3$; $0{,}2$), bỏ câu sai "Tổng kỳ vọng…"; hết tràn | 12 → 24 | 3 + hình; 787 → 655 px, tràn phải 1310 → 1256 | khoảng 86 |
| S36 | `L09-25` | "Ví dụ softmax hai hành động" → "Ví dụ: hàm điểm softmax hai hành động" | sửa; thẻ dữ kiện thay câu dữ kiện; tính cả $\psi_\theta(s,2)$; trung bình $(0;\,0)$ thay "$0\in\mathbb R^d$"; "Diễn giải:"; bỏ câu hỏi trùng `X02` | 20 → 21 | 5 + hình; 561 → 666 px | khoảng 81 |
| S37 | `L09-25b` (mới) | — → "Kỳ vọng của hàm điểm" | thêm; "Mệnh đề." với ba giả thiết (khả vi, miền hỗ trợ cố định, đổi $\nabla$ với tổng hoặc tích phân); "Chứng minh." hai dòng; "Ý nghĩa:" hệ số không phụ thuộc $A$; trước đây kết quả chỉ nằm trong ghi chú diễn giả `L09-24` và câu hình | — → 34 | 3 + 2 công thức; 617 px | khoảng 121 |
| S38 | `L09-26` | "Hàm điểm Gaussian, phương sai cố định" → "Hàm điểm của chính sách Gaussian" | sửa; "Nhắc lại:" chính sách Gaussian (cách tám trang); "Mệnh đề." + "Chứng minh." một dòng; "Ý nghĩa:" hướng dời $\mu$ và vai trò $\sigma$; ghi chú trả lời câu hỏi nguồn tr. 38 | 24 → 25 | 5; 589 → 573 px | khoảng 99 |
| S39 | `L09-27` | "Ví dụ hàm điểm Gaussian" → "Ví dụ: hàm điểm Gaussian tại $a=1{,}5$" | sửa; $(1{,}5;\,3)$ dấu chấm phẩy; câu hỏi dùng hệ số $c$ thay "hệ số return"; "Lời giải:" hai dòng với số: $\Delta\mu=-0{,}75$, ra xa $a$ (kế hoạch D4) | 33 → 18 | 5; 572 → 449 px | khoảng 78 |
| S40 | `X02` | "Bài tập: hai hàm điểm" → "Bài tập: hàm điểm softmax và Gaussian" | sửa, đã chuyển xuống sau `L09-27` ở C0; dữ kiện tự đủ bằng hình `score-exercise-card.svg`; bộ số softmax mới $\theta=(0;\,\log3)$, $\pi=(\tfrac14;\,\tfrac34)$ (không trùng `L09-25`); "Lời giải:" ba dòng; dòng cuối "Lưu ý:" là đầu ra cho mạch 6; `data-note-topic-id` đổi sang `lec-09-topic-09` | 20 → 45 | 5 + hình; 492 → 655 px | khoảng 106 |

Ngoại lệ mật độ mạch 5: không có; trang nhiều nhất `L09-23` 50 âm tiết, 5 dòng, 1 công thức hiển thị.

##### Hành trình khái niệm, mạch 5, cụm "Hàm mục tiêu" (5 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-M5T`, `L09-20` ("Nhu cầu:") | Dòng "Lưu ý:" cuối `L09-19` | Cần một số đo của $\pi_\theta$ | Không gộp |
| Trực quan | ghi chú diễn giả `L09-20`; ghi chú bài giảng | Lợi tức kỳ vọng từ trạng thái đầu (nguồn tr. 30) | — | Gộp với vấn đề |
| Ví dụ | `L09-20` | Thẻ dữ kiện | $J=2$ | Không gộp |
| Hình thức | `L09-20` ("Định nghĩa.", "Giả thiết:") | $G_0$, $\rho_0$, $\mathbb E_{\pi_\theta}$ | $J(\theta)=\mathbb E_{\pi_\theta}[G_0]$ | Không gộp |
| Ứng dụng | `L09-21` | Hạ gradient của Bài 08 | $\theta\leftarrow\theta+\alpha\nabla_\theta J$; $\nabla_\theta J=(\tfrac23;\,-\tfrac23)$ | Không gộp |
| Kiểm tra | `L09-21` ("Lưu ý:"), Bài tập 09.5 của ghi chú | — | $J$ chỉ đo được qua lượt | Kiểm tra trên lớp gộp với trang vấn đề của hàm điểm `L09-30A` |

##### Hành trình khái niệm, mạch 5, cụm "Hàm điểm" (17 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-30A` | Thẻ dữ kiện; $J$ chỉ đo qua lượt | Sai phân $0{,}655$ so với $\tfrac23$; cần $d+1$ giá trị $J$ có nhiễu | Không gộp (trang vấn đề theo nguồn tr. 33) |
| Trực quan | `L09-23` ("Trực quan.") | $\nabla\pi=\pi\nabla\log\pi$ | Tổng có trọng số $\pi$ thành kỳ vọng ước lượng được bằng mẫu | Cùng trang với ví dụ và định nghĩa |
| Ví dụ | `L09-23` ("Ví dụ.") | Hai hành động, $\theta=(\log2;\,0)$ nêu lại tại chỗ | $\nabla_\theta\log\pi_\theta(1\mid s)=(\tfrac13;\,-\tfrac13)$ | Đặt trước định nghĩa trên cùng trang |
| Hình thức | `L09-23` ("Định nghĩa."), `L09-24` (Mệnh đề softmax), `L09-25b` (Mệnh đề kỳ vọng), `L09-26` (Mệnh đề Gaussian) | $\pi_\theta>0$, miền hỗ trợ cố định | $\psi_\theta$; hai công thức đóng; $\mathbb E[\psi_\theta]=0$ | Không gộp |
| Ứng dụng | `L09-25`, `L09-27` | Thẻ dữ kiện; Gaussian $\phi(s)=(1;\,2)$, $a=1{,}5$ | $\psi_\theta(s,1)=(\tfrac13;\,-\tfrac13)$, $\psi_\theta(s,2)=(-\tfrac23;\,\tfrac23)$, trung bình $(0;\,0)$; $(1{,}5;\,3)$, $\Delta\mu=-0{,}75$ | Ví dụ softmax đứng trước mệnh đề kỳ vọng mà nó minh họa |
| Kiểm tra | `L09-27` ("Câu hỏi:"/"Lời giải:"), `X02` | Hình `score-exercise-card.svg` | $(\tfrac34;\,-\tfrac34)$, $(-\tfrac14;\,\tfrac14)$, $(-1;\,-2)$ | Không gộp |

Thời lượng mạch 5: `L09-M5T` 1, `L09-20` 2, `L09-21` 2, `L09-30A` 2, `L09-23` 3, `L09-24` 2, `L09-25` 2, `L09-25b` 2, `L09-26` 2, `L09-27` 2, `X02` 2 phút; tổng 22. Dữ kiện truyền: thẻ dữ kiện bài toán một bước (`one-step-card.svg`) ở `L09-20`, `L09-30A`, `L09-25`, dùng lại ở mạch 6 (`L09-28`, `L09-32`, `X03`); $\nabla_\theta J=(\tfrac23;\,-\tfrac23)$ của `L09-21` là số để mạch 6 kiểm $\sum_ar(a)\pi_\theta(a\mid s)\psi_\theta(s,a)$; hệ quả của `L09-25b` ($\mathbb E[c\,\psi_\theta]=0$) là bước bỏ phần thưởng quá khứ ở `L09-29`; dòng "Lưu ý:" cuối `X02` (hàm điểm của một bước, còn thiếu gradient theo cả lượt) là đầu vào của `L09-M6T`.

Lệch khỏi nguồn (mạch 5): nguồn tr. 30–32 (hàm mục tiêu, tối ưu chính sách, gradient chính sách) gộp vào `L09-20`, `L09-21`; nguồn viết $J=V^{\pi}(s_1)$ với trạng thái đầu cố định, bài dùng $S_0\sim\rho_0$ (trường hợp riêng ghi trong ghi chú diễn giả); câu hỏi tr. 30 và cách không dùng gradient tr. 31 (leo đồi, giải thuật di truyền) đưa vào ghi chú diễn giả `L09-21` và ghi chú bài giảng; tr. 33 giữ vị trí nguồn trước hàm điểm (C0 đã chuyển về); tr. 35 và 37 là hai câu hỏi "Quiz" về hàm điểm, trả lời bằng "Mệnh đề." ở `L09-24`, `L09-26`; tr. 38 câu hỏi về vấn đề của Gaussian trả lời trong ghi chú diễn giả `L09-26`. Thêm so với nguồn: `L09-25b` (mệnh đề kỳ vọng của hàm điểm, có trong Sutton và Barto 2018, §13.4, dùng ở mạch 6), các ví dụ số trên bài toán một bước, phần phương sai của sai phân hữu hạn trong ghi chú bài giảng. Ký hiệu: $\log$ là logarit tự nhiên; $\theta=(\log2;\,0)$ (ghi chú bài giảng đổi các chỗ $\ln$ cũ).

##### Rà lại mạch 5 (bước R5): thay đổi trang và mật độ

| trang | thay đổi ở R5 | âm tiết sau R5 | đáy |
|---|---|---|---|
| `L09-21` | "Ví dụ." nêu softmax, $\phi$ đơn vị, $r=(3;\,0)$ đã biết và đạo hàm $\nabla_\theta\pi_\theta(1\mid s)$; dòng sau "Tính trực tiếp" cho $(\tfrac23;\,-\tfrac23)$; ghi chú diễn giả có đạo hàm softmax. Thẻ dữ kiện không đặt vì không đủ chỗ (dữ kiện nêu tại chỗ) | 49 | 597 px |
| `L09-20`, `L09-30A`, `L09-25` | thẻ `one-step-card.svg` ghi "chính sách softmax"; `alt` theo | 42; 42; 21 | 649; 608; 666 px |
| `X02` | (b) viết "Với $a=-1$: $\psi_\theta(s,a)$", "bước nhỏ" | 49 | 655 px |
| `L09-30A`, `L09-26`, `L09-25b` | chỉ ghi chú diễn giả: $0{,}011$; câu Gaussian bị chặn khớp Mục 4 (cắt: hàm điểm của mẫu trước khi cắt; $\tanh$: mật độ sau đổi biến); điều kiện đổi đạo hàm–tích phân chặn $\lVert\nabla_\theta\pi_{\theta'}\rVert$ đều trong lân cận | — | — |

#### Mạch 6 "Gradient chính sách và REINFORCE" (bước S41–S51)

Thứ tự sau bước: `L09-M6T`, `L09-28`, `L09-28A`, `L09-29`, `L09-29b`, `L09-22`, `L09-30`, `L09-32`, `L09-31`, `X03`, `X03b`. `L09-22` đặt ngay trước định lý (kế hoạch D1 cho phép đặt trước hoặc gộp); đặt sau `L09-28A`, `L09-29` vì giả thiết gom các điều kiện mà ba trang đó dùng.

| bước | trang | tiêu đề trước → sau | quyết định và lý do | âm tiết trước → sau | dòng, đáy | ghi chú diễn giả |
|---|---|---|---|---|---|---|
| S41 | `L09-M6T` | — → "6. Gradient chính sách và REINFORCE" | thêm; `id="mach-6"`; dòng dẫn theo `outline.md` nhận đầu ra của `X02`; `data-note-topic-id` `lec-09-topic-10` | — → dẫn 19, khóa 18 | 2; 450 px | khoảng 94 |
| S42 | `L09-28` | "Tỷ số xác suất biến return thành gradient (likelihood ratio)" → "Gradient của $J$ theo tỉ số xác suất" | sửa; "Nhu cầu:" nối `X02`; ví dụ một bước với thẻ dữ kiện: $\sum_ar(a)\pi\psi=(\tfrac23;\,-\tfrac23)$ khớp tính trực tiếp; "Ký hiệu:" định nghĩa $\tau$, $p_\theta(\tau)$ trước khi dùng; "tỉ", "lợi tức"; ghi chú: $G_0(\tau)$ không phụ thuộc $\theta$, khớp sai phân $0{,}655$ | 0 → 27 | 4 + hình + 1 công thức; 563 → 670 px | khoảng 82 |
| S43 | `L09-28A` | "Phân tích xác suất quỹ đạo" → "Xác suất của quỹ đạo" | sửa; tích $p_\theta(\tau)$ với chữ hoa; "$\rho_0$, $P$ không phụ thuộc $\theta$"; định nghĩa $\psi_t$ tại chỗ; "Ý nghĩa:" không cần $P$; bỏ câu "luận điểm trung tâm", "Trang sau dùng…" | 8 → 29 | 3 + 2 công thức; 572 → 681 px | khoảng 80 |
| S44 | `L09-29` | "Điều kiện theo lịch sử loại phần thưởng quá khứ" → "Phần thưởng quá khứ và hàm điểm" | sửa; thứ tự lập luận: tách $G_0=G_{<t}+\gamma^tG_t$ → $\mathbb E[G_{<t}\psi_t]=0$ (Mệnh đề 09.17) → kết luận; $\psi_t$ đã định nghĩa ở `L09-28A` | 20 → 16 | 3 + 2 công thức; 683 → 606 px | khoảng 87 |
| S45 | `L09-29b` (mới) | — → "Ví dụ: lượt hai bước" | thêm; $G_0=2{,}8$, $G_1=2$; $5{,}6\psi$ và $4{,}6\psi$ chênh $R_1\psi_1$ (kỳ vọng $0$); bỏ $\gamma^t$: $4{,}8\psi$, lệch; ghi chú dẫn Nota và Thomas (2020) | — → 31 | 6; 557 px | khoảng 94 |
| S46 | `L09-22` | "Hợp đồng cho đạo hàm theo chính sách" → "Giả thiết cho gradient của $J$" | sửa, chuyển xuống ngay trước định lý; bốn giả thiết đánh số (G1)–(G4), điều kiện đủ cụ thể ($|R|\le R_{\max}$, $T\le T_{\max}$, đặc trưng bị chặn) bao softmax và Gaussian; "Ý nghĩa:"; bỏ "hợp đồng", câu "sai phân hữu hạn đã bị lược", câu phóng đại; `data-note-topic-id` sang `lec-09-topic-11` | 47 → 51 | 6; 510 → 507 px | khoảng 114 |
| S47 | `L09-30` | "Mở rộng: phân bố chiếm dụng (occupancy measure)" → "Định lý gradient chính sách" | sửa, chuyển lên trước REINFORCE (cốt lõi, nguồn tr. 39); "Định lý." dạng quỹ đạo dưới (G1)–(G4); "Chứng minh." một dòng; "Dạng khác:" $\tfrac1{1-\gamma}\mathbb E_{\nu^\pi_\gamma}[q_\pi\psi]$ với $\nu^\pi_\gamma$ chuẩn hóa; "Ý nghĩa:" một lượt cho mẫu không chệch; $q_\pi$ thay $Q^\pi$; bỏ "Trực giác:", gạch ngang dài, câu "có thể lược"; hết tràn phải (1282 → 1256) | 32 → 26 | 4 + 1 công thức; 638 → 607 px | khoảng 102 |
| S48 | `L09-32` | "Áp dụng REINFORCE cho softmax" → "Ví dụ: một cập nhật REINFORCE" | sửa, đứng trước thuật toán; thẻ dữ kiện thay "Dùng lại…"; $(1;\,-1)$, $0{,}710$; "Kiểm tra lại:" $\mathbb E[\widehat g]=\nabla J$; dấu chấm phẩy trong vector | 13 → 5 | 5 + hình; 551 → 557 px | khoảng 90 |
| S49 | `L09-31` | "REINFORCE: thu rồi cập nhật" → "Thuật toán REINFORCE" | sửa; "Thuật toán." đủ đầu vào, khởi tạo, bốn bước, dừng; $\mathbb E[\widehat g]=\nabla J(\theta_{\mathrm{old}})$ dưới (G1)–(G4); "Lưu ý:" theo chính sách, bộ nhớ phát lại phải hiệu chỉnh; bỏ hình (chuyển sang ghi chú bài giảng, vẽ lại); ghi chú sửa lý do bỏ $\gamma^t$, biến thể cập nhật theo từng $t$, lượt bị cắt ngắn; hết tràn (748 → 565 px) | 11 → 37 | 7 (giả mã, ngoại lệ); 565 px | khoảng 115 |
| S50 | `X03` | "Bài tập: kiểm cập nhật chính sách" → "Bài tập: cập nhật REINFORCE" | sửa; thẻ dữ kiện; (a) "phần thưởng của hành động 1 đổi thành $-3$"; (b) lượt hai bước mới $A_0=1$, $A_1=2$ (không lặp `L09-29b`); câu hỏi tham số cố định chuyển vào ghi chú | 36 → 28 | 3 + hình; 566 → 626 px | khoảng 68 |
| S51 | `X03b` (mới) | — → "Bài tập: cập nhật REINFORCE" (lời giải) | thêm; "Lời giải:" từng bước; "Lưu ý:" phương sai $\tfrac49$, cộng $1$ vào mọi phần thưởng thành $\tfrac{16}9$, là đầu ra cho mạch 7 | — → 31 | 6; 545 px | khoảng 97 |

Ngoại lệ mật độ mạch 6: `L09-31` 7 dòng (một dòng mở, bốn bước giả mã, một dòng dừng và kết luận không chệch, một dòng "Lưu ý:"), cùng lý do với `L09-09`, `L09-12`: giả mã một thuật toán trên một trang, dưới tám dòng; 37 âm tiết. Các trang khác ≤ 6 dòng, ≤ 51 âm tiết.

##### Hành trình khái niệm, mạch 6, cụm "Định lý gradient chính sách" (13 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-M6T`, `L09-28` ("Nhu cầu:") | Dòng "Lưu ý:" cuối `X02` | Hàm điểm của một bước chưa đủ cho cả lượt | Không gộp |
| Trực quan | `L09-28` (ví dụ một bước, $\nabla\pi=\pi\psi$), ghi chú diễn giả `L09-29` | Thẻ dữ kiện | Thay một hành động bằng cả quỹ đạo; phần thưởng trước $A_t$ không do $A_t$ gây ra | Gộp với ví dụ |
| Ví dụ | `L09-28`, `L09-29b` | Thẻ dữ kiện; lượt hai bước | $(\tfrac23;\,-\tfrac23)$; $5{,}6\psi$ và $4{,}6\psi$ cùng kỳ vọng | Ví dụ hai bước đặt sau phép suy diễn mà nó minh họa, trước định lý |
| Hình thức | `L09-28` (tỉ số xác suất), `L09-28A`, `L09-29`, `L09-22`, `L09-30` | $\tau$, $p_\theta$, $H_t$ | Định lý dạng quỹ đạo và dạng phân bố chiếm dụng | Ba bước suy diễn trước định lý |
| Ứng dụng | `L09-32` | Thẻ dữ kiện | Một mẫu $\widehat g=(1;\,-1)$, kỳ vọng bằng $\nabla J$ | Gộp với ví dụ của REINFORCE |
| Kiểm tra | `L09-30` ("Ý nghĩa:"), `X03`, `X03b` | — | Mẫu không chệch; cập nhật kiểm được | Không gộp |

##### Hành trình khái niệm, mạch 6, cụm "REINFORCE" (7 phút)

| bước | mã trang | dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L09-30` ("Ý nghĩa:") | Định lý | Lấy mẫu kỳ vọng bằng một lượt | Gộp với kết quả định lý |
| Trực quan | ghi chú diễn giả `L09-32` | Lợi tức dương tăng xác suất hành động đã chọn | — | Gộp với ví dụ |
| Ví dụ | `L09-32` | Thẻ dữ kiện, $G_0=3$, $\alpha=0{,}1$ | $\pi(1\mid s)$: $\tfrac23\to0{,}710$; $\mathbb E[\widehat g]=\nabla J$ | Ví dụ tính tay trước thuật toán |
| Hình thức | `L09-31` | Định lý | Thuật toán đủ đầu vào, khởi tạo, thứ tự, dừng; không chệch | Không gộp |
| Ứng dụng | `X03` (b) | Lượt hai bước hai hành động | $\widehat g=(-0{,}267;\,0{,}267)$ | Gộp với kiểm tra |
| Kiểm tra | `X03`, `X03b` | Thẻ dữ kiện; phần thưởng $-3$ | $0{,}621$; phương sai $\tfrac49$ | Không gộp |

Thời lượng mạch 6: `L09-M6T` 1, `L09-28` 3, `L09-28A` 2, `L09-29` 2, `L09-29b` 2, `L09-22` 1, `L09-30` 3, `L09-32` 2, `L09-31` 2, `X03` 1, `X03b` 1 phút; tổng 20. Dữ kiện truyền: thẻ dữ kiện bài toán một bước ở `L09-28`, `L09-32`, `X03`; lượt hai bước ($R_1=1$, $R_2=2$, $\gamma=0{,}9$) của `L09-29b` và `X03`; dòng "Lưu ý:" cuối `X03b` (không chệch, phương sai $\tfrac49\to\tfrac{16}9$ khi cộng hằng) là đầu vào của mạch 7 và dòng nối Bài 10.

Lệch khỏi nguồn (mạch 6): nguồn tr. 39 (định lý gradient chính sách) tách thành `L09-28`, `L09-28A`, `L09-29`, `L09-22`, `L09-30`, giữ thứ tự nguồn định lý trước REINFORCE (tr. 40); thêm `L09-29b`, `X03b`; nguồn tr. 40 viết REINFORCE không có $\gamma^t$ và cập nhật theo từng bước: bài giữ $\gamma^t$ (nhất quán với $J=\mathbb E[G_0]$, Nota và Thomas 2020) và cập nhật một lần mỗi lượt (sai khác có chủ ý, ghi trong ghi chú diễn giả `L09-31`). Hình `reinforce-trajectory.svg` vẽ lại (bỏ "return", "episode"; phông chữ theo deck) và chuyển sang ghi chú bài giảng.

##### Rà lại mạch 6 (bước R6): thay đổi trang và mật độ

| trang | thay đổi ở R6 | âm tiết sau R6 | đáy |
|---|---|---|---|
| `L09-30` | "Định lý." nêu bốn giả thiết tại chỗ (G1)–(G4); "Dạng khác" thêm điều kiện lượt kết thúc do MDP, viết $q_{\pi_\theta}$; dòng "Chứng minh." chuyển vào ghi chú diễn giả (ba bước đã làm ở `L09-28`, `L09-28A`, `L09-29`) để giữ đáy | 44 | 639 px |
| `L09-28` | "Ký hiệu:" thêm "đổi $\nabla$ với $\int$ cần giả thiết (G1)–(G4)"; bỏ "khớp tính trực tiếp" khỏi mặt trang (còn trong ghi chú diễn giả) | 28 | 670 px |
| `L09-28A` | bỏ dòng mở "Quỹ đạo sinh bởi…" (tiêu đề và công thức đã nêu) | 24 | 681 → 596 px |
| `L09-29` | số hiệu mệnh đề theo sau phát biểu bằng lời; nêu "$A_t\sim\pi_\theta(\cdot\mid S_t)$ khi biết $H_t$" | 23 | 649 px |
| `L09-29b` | "nói chung có kỳ vọng khác $0$" | 31 | 557 px |
| `L09-22` | (G4) viết "$\pi_\theta$ là softmax, hoặc Gaussian với $\sigma$ cố định; đặc trưng bị chặn"; ghi chú diễn giả bỏ câu $\mathbb E[T]$ hữu hạn | 52 | 507 px |
| `L09-31` | "Lưu ý:" nêu trọng số $p_{\theta_{\mathrm{old}}}(\tau)/p_{\theta'}(\tau)$ | 37 | 626 px |
| `X03`, `X03b` | (b) "Bỏ điều kiện dừng sau $A_0$"; lý do nghiêng về hành động 2 so đóng góp $1{,}2$ với $0{,}933$ | 33; 31 | 626; 545 px |

#### Mạch 7 "Tổng kết và chuyển tiếp" (bước S52–S61)

Khuôn theo mạch tổng kết của deck 08 (`L08-M7T`, `L08-34`/`L08-34b`, `L08-K1`/`L08-K1b`, `L08-K2`–`L08-K5`, `L08-33`). Không khái niệm mới; hành trình sáu bước `không áp dụng` cho mạch này (mọi khái niệm đã có hành trình ở mạch 2–6). `L09-33` bỏ, nội dung vào `L09-K1`, `L09-K1b`, `L09-K2b`.

| bước | trang | tiêu đề | lý do tồn tại; nối trước → sau | âm tiết | dòng, đáy | ghi chú diễn giả |
|---|---|---|---|---|---|---|
| S52 | `L09-M7T` | 7. Tổng kết và chuyển tiếp | điểm vào mạch 7; nhận dòng "Lưu ý:" cuối `X03b` (không chệch, phương sai) → `L09-K1` | dẫn 17, khóa 14 | 2; 321 px | khoảng 89 |
| S53 | `L09-K1` | Kết quả và giả thiết của bài | bảng `Kết quả \| Giả thiết không được bỏ \| Công thức hoặc thuật toán`, ba hàng của mạch 2–3 (phép cực đại, ước lượng kép, mục tiêu Double DQN) → `L09-K1b` | 48 | bảng 3 hàng; 501 px | khoảng 83 |
| S54 | `L09-K1b` | Kết quả và giả thiết của bài | bốn hàng: Double Q-learning, kỳ vọng hàm điểm, định lý gradient chính sách, REINFORCE → `L09-K2` | 46 | bảng 4 hàng; 584 px | khoảng 125 |
| S55 | `L09-K2` | So sánh bốn phương pháp | bảng `Phương pháp \| Quy tắc cập nhật \| Dữ liệu dùng \| Điều kiện dừng` cho DQN, Double DQN, Double Q-learning, REINFORCE; dòng "không điều kiện dừng nào là tiêu chuẩn hội tụ" → `L09-K2b` | 63 | bảng 4 hàng + 1 dòng; 666 px | khoảng 97 |
| S56 | `L09-K2b` | So sánh bốn phương pháp | bảng `Phương pháp \| Giả thiết không được bỏ \| Kết luận` cho kết luận về độ chệch (không viết "hội tụ") → `L09-K3` | 70 | bảng 4 hàng; 540 px | khoảng 101 |
| S57 | `L09-K3` | Bài tập: tổng hợp trên bài toán một bước | một bài nối hai nhóm trên thẻ dữ kiện: (a) $J$, $\nabla J$; (b) $\widehat g$ từng hành động, $\mathbb E[\widehat g]=\nabla J$; (c) $\mathbb E[\max_a\widehat r_a]$ với nhiễu $\pm1$, rồi với $r(2)=2{,}5$ → `L09-K4` | 31 | 4 + hình; 500 px | khoảng 71 |
| S58 | `L09-K4` | Bài tập: tổng hợp trên bài toán một bước | "Lời giải:" từng câu, "Kết luận:" ($J=2$; $(\tfrac23;-\tfrac23)$; $3$ không chệch; $3{,}375$ chệch $+0{,}375$) → `L09-K5` | 31 | 5; 475 px | khoảng 100 |
| S59 | `L09-K5` | Trả lời vấn đề trung tâm | hộp bài toán giống `L09-02c`; năm dòng có điều kiện cho mạch 2–6 kèm số; dòng "Nguồn:" → `L09-K6` | 72 | hộp + 5 dòng + nguồn; 647 px | khoảng 130 |
| S60 | `L09-K6` | Câu hỏi tự kiểm tra | "Câu hỏi: trả lời và nêu kết quả đã dùng." và bốn câu (CT §3.2); lời giải trong ghi chú diễn giả → `L09-K7` | 52 | 5; 462 px | khoảng 100 |
| S61 | `L09-K7` | Bài tập về nhà và tài liệu đọc | bảng `Mạch \| Bài tập` trỏ Bài tập 09.1–09.10 của ghi chú bài giảng (số sau R7) (chưa có `exercises.md`, không liên kết "Bài tập"); "Tài liệu đọc:"; liên kết "Ghi chú bài giảng"; dòng nối Bài 10 có liên kết `lecture-10-trpo-va-ppo.html` | 52 | bảng 6 hàng + 4 dòng; 586 px | khoảng 100 |

Ngoại lệ mật độ mạch 7: không có; `L09-K2`, `L09-K2b`, `L09-K5` là trang so sánh, tổng kết (trần 80 âm tiết).

Thời lượng mạch 7: `L09-M7T` 1, `L09-K1` 1, `L09-K1b` 1, `L09-K2` 1, `L09-K2b` 1, `L09-K3` 1, `L09-K4` 1,5, `L09-K5` 1, `L09-K6` 1, `L09-K7` 0,5 phút; tổng 10. Tổng toàn bài: $8+15+30+15+22+20+10=120$ phút.

Lệch khỏi nguồn (mạch 7): nguồn không có mạch tổng kết; trang tổng kết cũ `L09-33` bỏ. Câu hỏi thảo luận của nguồn tr. 11 và 21 không đưa lên mặt trang; ghi chú bài giảng nhắc lại ở mục Câu hỏi tự kiểm tra.

Rà toàn deck ở bước mạch 7: `L09-02b` liệt kê bảy tên khớp bảy tên trang tiêu đề mạch (mạch 1 là bìa); liên kết `#/1`…`#/7` mở `L09-01`, `L09-M2T`, …, `L09-M7T` (đã bấm thử); năm mục tiêu của `L09-02` ứng mạch 2–6; năm dòng của `L09-K5` ứng năm dòng của `L09-02c`; mọi `data-note-topic-id` có trong ghi chú bài giảng và ngược lại (17 mã).

##### Rà lại mạch 7 (bước R7): thay đổi trang và mật độ

| trang | thay đổi ở R7 | âm tiết sau R7 | đáy |
|---|---|---|---|
| `L09-K1` | thêm hàng "Chính sách ngẫu nhiên khi gộp trạng thái" (mục tiêu 3 của `L09-02`); bốn hàng | 75 | 635 px |
| `L09-K1b` | hàng "Kỳ vọng của hàm điểm" thay bằng hàng "Hàm điểm" (công thức softmax, Gaussian, kỳ vọng $0$; mục tiêu 4); hàng định lý nêu đủ (G2); "Double Q&#8209;learning" không ngắt | 50 | 633 px |
| `L09-K2` | ô dữ liệu REINFORCE bỏ `<br>`; "Double Q&#8209;learning" không ngắt | 64 | 625 px |
| `L09-K2b` | ô Double DQN: "không bảo đảm hết chệch lên; mức giảm phải đo" | 71 | 502 px |
| `L09-K5` | năm dòng khớp `L09-02c`: "chệch lên hoặc bằng" với điều kiện của số $\tfrac12$; "bản đánh giá không chệch, độc lập", "Double DQN chỉ gần thỏa" (bỏ $5{,}5\to4{,}6$); hành động liên tục và tiêu chí của $3{,}8$; dòng nguồn rút gọn | 76 | 644 px |
| `L09-K6` | ghi chú diễn giả (2) có điều kiện | 52 | 462 px |
| `L09-K7` | bảng `Mạch \| Bài tập` theo số mới (09.1–09.10; 09.1 mức nhận biết); dòng Bài 10 nêu "TRPO và PPO" | 60 | 630 px |
| `L09-16` | ghi chú diễn giả bỏ câu về $\epsilon_{\mathrm{exp}}$-tham lam (đã có ở `L09-M4T`): 166 → 143 | 47 | 678 px |

Không thêm `L09-K1c`: hai trang bảng kết quả đều dưới trần 80 âm tiết và đáy 702 px. Thời lượng mạch 7 giữ 10 phút.

#### Rà cuối từ góc nhìn sinh viên (bước F): thay đổi trang và mật độ

| trang | thay đổi ở F | âm tiết sau F | đáy |
|---|---|---|---|
| `L09-01` | luận đề: "tách việc chọn hành động khỏi việc đánh giá nó" | 70 (ngoại lệ bìa, xem mục ngoại lệ) | 499 px |
| `L09-02c` | dòng 2–6 viết bằng lời cho người đọc lần đầu (công thức để lại cho `L09-K5`); bỏ chữ "Khi" ở đầu dòng | 79 → 94 (ngoại lệ: thay ba công thức bằng lời, mỗi dòng ≤ 2 dòng hiển thị) | 673 px |
| `L09-03` | nguồn của $108{,}5$ (một lần chạy DQN, thực hành Bài 08) trên mặt trang; γ trong `cartpole-overestimate.svg` đặt phông có chân | 56 | 650 px |
| `L09-06b` | "Diễn giải:" nêu lại $\mathbb E[\max_a\widehat Q^A_a]=\tfrac12$ thay cụm "một bản cho cả hai việc" | 39 | 654 px |
| `L09-06c` | phép tính $\tfrac34\cdot0{,}5=0{,}375$, chệch $-0{,}125$ | 45 | 497 px |
| `L09-07` | "Lưu ý:" mặt nạ cho $y_i=R_i$, $a_i^*$ không ảnh hưởng | 27 | 612 px |
| `L09-13` | `double-q-example.svg` đảo hàng cho khớp `L09-08` (hàng trên đánh giá, mũi tên đi lên); "Diễn giải:" nêu vai tại chỗ | 21 | 694 px |
| `L09-14` | bỏ số hiệu ghi chú trong ô bảng | 76 | 654 px |
| `L09-15` | "Giới hạn chung:" đổi thành "Lưu ý:" | 57 | 446 px |
| `L09-16` | "đặc trưng $x(s)$"; "tất định (Bài 04: xác định)" ở lần dùng đầu; ghi chú bỏ câu quy trình về nguồn | 52 | 678 px |
| `L09-16b` | định nghĩa $h_i$ trên mặt trang; `aliased-grid-stochastic.svg` thêm hàng $h_i=5,4,1,4,5$; "Diễn giải:" $(5+4+1+4+5)/5=3{,}8$; ghi chú rút còn 108 | 48 | 638 px |
| `L09-17` | "(từ đây $\theta$ là tham số của chính sách)" | 59 | 410 px |
| `L09-19` | "Ký hiệu:" $\phi(s,a)$, $\phi(s)$ là vector đặc trưng cố định | 58 | 669 px |
| `L09-20` | "Định nghĩa." nêu hàm mục tiêu khác mục tiêu $y_i$ của DQN | 47 | 649 px |
| `L09-21` | "Ví dụ." nêu $\phi(s,1)$, $\phi(s,2)$ tại chỗ; ghi chú bỏ "Nguồn hỏi…" | 44 | 597 px |
| `L09-22` | danh sách không đánh số kép | 52 | 507 px |
| `L09-23` | "Trực quan." nêu tổng $\sum_ar(a)\nabla\pi_\theta$ thiếu trọng số $\pi_\theta$ | 43 | 630 px |
| `L09-26` | "Chứng minh." đưa "hằng số" ra ngoài KaTeX; ghi chú bỏ "Nguồn hỏi…" | 32 | 625 px |
| `L09-27` | nghĩa của hệ số $c$ | 25 | 501 px |
| `L09-28` | thay "(G1)–(G4)" bằng giả thiết tại chỗ: đổi được $\nabla_\theta$ với tích phân, điều kiện đủ nêu cùng định lý | 36 | 676 px |
| `L09-29` | bỏ số hiệu ghi chú | 21 | 606 px |
| `L09-29b` | nhãn (i), (ii), (iii) cho ba ước lượng; hai hiệu (i) − (ii), (iii) − (ii) | 38 | 609 px |
| `L09-30` | "Dạng khác" nêu tên và nghĩa của $\nu^\pi_\gamma$ (tần suất thăm, lượt muộn tính nhẹ hơn) | 56 | 647 px |
| `L09-30A` | "thương sai phân" | 44 | 608 px |
| `L09-K1` | hàng gộp trạng thái phát biểu đủ ($3{,}8$ bước, tất định có ô không tới đích); rút cột giả thiết | 72 | 676 px |
| `L09-K1b` | giả thiết Double Q-learning là độc lập và không chệch | 53 | 633 px |
| `L09-K2b` | thứ tự hàng DQN, Double DQN, Double Q-learning, REINFORCE như `L09-K2`; tên "DQN" | 69 | 502 px |
| `L09-K5` | dòng 4, 6 phát biểu lại dữ kiện; ghi chú bỏ câu mở siêu văn bản | 80 | 645 px |
| `L09-K7` | "Bài tập: mục Bài tập củng cố của ghi chú bài giảng." | 53 | 630 px |

Ngoại lệ mật độ ở F: `L09-01` (bìa) 70 âm tiết; `L09-02c` 94 âm tiết, gỡ ở F2 (xem dưới).

#### Bước F2: thay đổi trang và mật độ

| trang | thay đổi ở F2 | âm tiết sau F2 | đáy |
|---|---|---|---|
| `L09-01` | luận đề có điều kiện: "đánh giá bằng một ước lượng không chệch, độc lập với ước lượng chọn bỏ được phần chệch lên này" (vẫn một câu) | 75 (ngoại lệ bìa: luận đề một câu, như `L08-01`; trước đợt sửa 58, sau R1 65) | 499 px |
| `L09-02c` | hộp rút gọn; dòng 3 "Ước lượng đánh giá không chệch, độc lập với ước lượng chọn: …"; dòng 4 "Hành động thực, …"; dòng 6 đủ giả thiết "$R$, $T$, $\phi$ bị chặn"; mỗi dòng ≤ 19 âm tiết | 94 → 78 (gỡ ngoại lệ) | 673 px |
| `L09-K5` | hộp và dòng 3 cùng câu với `L09-02c`; dòng "Nguồn:" rút gọn (nguồn đầy đủ trong ghi chú diễn giả) | 78 | 649 px |
| `L09-14` | ô dữ liệu của Double DQN: "như DQN" | 72 | 654 px |
| `L09-16b` | dòng đầu nêu chính sách ở hai ô xám bằng chữ; `alt` có hàng $h_i$ | 55 | 690 px |
| `L09-23` | "Trực quan." mở bằng "Bài toán một bước:" | 47 | 630 px |
| `L09-28` | câu giả thiết tách sang dòng "Giả thiết:" | 36 | 696 px |
| `L09-30` | $\nu^\pi_\gamma$: "lần thăm ở bước muộn tính nhẹ hơn" | 59 | 647 px |

Sau F2, mọi trang so sánh, tổng kết ≤ 80 âm tiết; mọi trang nội dung khác ≤ 60, trừ ngoại lệ bìa `L09-01`.

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
