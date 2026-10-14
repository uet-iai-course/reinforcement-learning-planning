# Storyboard — Bài 03: Quá trình quyết định Markov

Bản này thay storyboard trước đợt sửa 2026-10-12 và khớp deck hiện tại (`2627-1/lecture-03-qua-trinh-quyet-dinh-markov.html`, 72 trang, 7 mạch; cập nhật sau vòng biên tập năm vai rà soát ngày 2026-10-12). Nguồn nội dung: Bài giảng gốc (2025–2026), trang 28–58; Sutton và Barto (2018), chương 3 và §4.1; ghi chú bài giảng Bài 03 đã commit (`ceab04c`). Kế hoạch: `revision-plan-2026-10-12.md` mục A; quyết định chung: `../quyet-dinh-chuan-2026-10-12.md`. Mọi mã trang có tiền tố `L03R-`; bảng dưới viết gọn phần sau tiền tố.

## 1. Bản đồ mạch

| N | Mạch | Loại | Chức năng | Đầu vào | Đầu ra | Đóng góp cho vấn đề trung tâm | Trang tiêu đề | Trang | Phút |
|---|---|---|---|---|---|---|---|---:|---:|
| 1 | Mở đầu | mở đầu | Nêu luận đề, kết quả kế thừa từ Bài 02, ký hiệu, mục tiêu, bản đồ mạch, vấn đề trung tâm | Bài 02: tính Markov, hàm động lực, lợi tức với hệ thức truy hồi và cận, $v_\pi$ | Nhu cầu: cách tính giá trị mà định nghĩa của Bài 02 chưa cho | Đặt bài toán: giá trị dài hạn của một chính sách khi phản hồi ngẫu nhiên | `01-01` (bìa) | 6 | 9 |
| 2 | Trạng thái Markov và mô hình môi trường | phát triển kiến thức (khái niệm) | Kế thừa tính Markov và hàm động lực của Bài 02; thêm điều kiện xác suất dương, phản ví dụ, bảng $p$ của robot, quy tắc sinh quỹ đạo | Vòng tương tác; hai định nghĩa của Bài 02 | $\mathcal M$ của robot, $p$, $p(s'\mid s,a)$, $r(s,a)$ | Môi trường được mô tả bằng một bảng không phụ thuộc lịch sử | `02-00` | 15 | 26,5 |
| 3 | Lợi tức chiết khấu | phát triển kiến thức (nhắc lại và áp dụng) | Áp lợi tức của Bài 02 vào robot; quy ước hấp thụ; cận cho robot | $p$ chỉ mô tả một bước; lợi tức, hệ thức truy hồi và cận của Bài 02 | $G_t$, quy ước hấp thụ, cận $\lvert G_t\rvert\le6$ của robot | Đại lượng cần lấy kỳ vọng là hữu hạn | `03-00` | 7 | 12 |
| 4 | Chính sách và hàm giá trị | phát triển kiến thức (khái niệm) | Kế thừa $v_\pi$ của Bài 02; định nghĩa trên quá trình xuất phát tại $s$, xác suất đoạn quỹ đạo, $q_\pi$ | $p$, $G_t$, $v_\pi$ của Bài 02 | $\pi$, xác suất đoạn quỹ đạo, $v_\pi$, $q_\pi$ | Định nghĩa đại lượng cần tính | `04-00` | 10 | 14 (+3 trong khối 30 phút) |
| 5 | Phương trình Bellman kỳ vọng | phát triển kiến thức (kết quả và chứng minh) | Thay kỳ vọng vô hạn bằng phương trình hữu hạn ẩn | Định nghĩa $v_\pi$, $q_\pi$; hệ thức truy hồi của Bài 02 | Bellman cho $v_\pi$, $q_\pi$; quan hệ $v$–$q$ | Phương trình mà giá trị phải thỏa | `05-00` | 12 | 22,5 (+2 trong khối 30 phút) |
| 6 | Đánh giá chính sách bằng hệ tuyến tính | phát triển kiến thức (thuật toán) và ứng dụng | Giải hệ, dạng ma trận, nghiệm duy nhất, thuật toán | Hệ Bellman | $v_\pi=(13/4,\,7/4)$, Thuật toán 03.29, lưới 5×5 | Câu trả lời bằng số cho robot và điều kiện nghiệm duy nhất | `06-00` | 14 | 25,5 |
| 7 | Tổng kết và chuyển tiếp | kết luận | Gom kết quả và giả thiết, bài tập tổng hợp, tự kiểm tra, tài liệu | Mọi kết quả | Bốn giới hạn dẫn sang Bài 04–07 | Trả lời có điều kiện vấn đề trung tâm, song song từng dòng với `01-02b` | `07-00` | 8 | 10,5 |
| | **Tổng** | | | | | | | **72** | **120** (+ khối 30 phút) |

Bảy mạch theo kế hoạch A1 và quyết định chung mục 8 (gộp mạch "Từ tương tác đến trạng thái Markov" cũ vào mạch mô hình). Trang "Nội dung" có 7 mục cộng một dòng đọc trước (ngoại lệ mật độ, mục 5).

## 2. Cụm khái niệm

| Cụm | Mạch | Dạng | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Ký hiệu và dữ kiện truyền | Gộp hoặc không áp dụng | Phút |
|---|---|---|---|---|---|---|---|---|---|---|---:|
| K1 Tính Markov | 2 | khái niệm (kế thừa Bài 02) | `02-00` (dòng dẫn), `01-03` ("Nhắc lại:" rồi "Nhu cầu:") | `01-05` | `01-04` (dòng "Ví dụ." trước "Định nghĩa."), `01-05` | `01-04` (quỹ đạo, lịch sử), `01-06` | `01-06b` (phản ví dụ, cách sửa) | `01-07` (sinh viên tự làm 3 phút), `01-07b` (lời giải trên mặt trang) | $(S_t,A_t,R_{t+1},S_{t+1})$, $H_t$, hai lịch sử kết thúc ở L | Ví dụ `01-04` cụ thể hóa vấn đề ở `01-03` trước trực giác; trực giác và ví dụ hai lịch sử chung trang `01-05`; định nghĩa trùng Bài 02, ghi chú diễn giả `01-06` nói rõ | 15 |
| K2 Hàm động lực và MDP | 2 | khái niệm (kế thừa Bài 02, thêm quy tắc sinh) | `02-02` (câu nối "Nhờ tính Markov…") | `02-04` (dòng "Trực quan.") | `02-02`, `02-03` | `02-04`, `02-05`, `02-06` | `02-05` (cặp L–Tìm), `02-06` (bộ MDP robot) | `02-07`, `02-07b` (lời giải trên mặt trang) | Bảng bảy hàng → $p$; $r(\mathrm L,\mathrm{tim})=-1/2$ | Ví dụ dẫn nhập `02-02` đứng cùng vấn đề | 13 |
| K3 Lợi tức | 3 | nhắc lại Bài 02 và áp dụng | `03-00`, `03-01` ("Nhắc lại:"; "Nhu cầu:" mở bằng ví dụ Chờ mãi cho $1+1+\cdots=\infty$) | `03-01` (Chờ mãi; trọng số giảm trong ghi chú diễn giả), ghi chú diễn giả `03-05` (Chờ mãi với $\gamma=1/2$ cho $2$) | `03-01` (hai dãy ba bước) | `03-02`, `03-04`, `03-05` | `03-05` (cận 6 của robot) | `03-06`, `03-06b` (lời giải trên mặt trang) | Trọng số $1,1/2,1/4$ → $\gamma^k$; $3/2$, $7/4$ là lợi tức cắt | `03-01` và `03-03` cũ gộp thành một trang nhắc lại áp vào robot (quyết định của điều phối viên); định nghĩa và mệnh đề giữ để có quy ước hấp thụ và số hiệu của ghi chú | 12 |
| K4 Chính sách | 4 | khái niệm | `04-00`, `04-02` ("Nhắc lại:" $v_\pi$ của Bài 02, "Nhu cầu:") | `04-03` | `04-02` | `04-03`, `04-03b` | `04-03b` (xác suất $1/4$), `04-04` | `04-08` câu (a) | Bảng chính sách chia đều → $\pi(a\mid s)$ | Vấn đề và ví dụ dẫn nhập chung trang `04-02` | 5,5 |
| K5 $v_\pi$ | 4 | khái niệm (kế thừa Bài 02) | `04-04` ("Nhu cầu:" một số cho mỗi trạng thái) | `04-05` (dòng "Trực quan.") | `04-04` | `04-05` | `04-05` (khoảng $[9/8,33/8]$), `06-03` | `04-08` câu (b)(c), `04-08b` | Cây hai bước → $G_0^{[2]}$ → $v_\pi$ | Vấn đề gộp với ví dụ `04-04` | 4 |
| K6 $q_\pi$ | 4 | khái niệm | `04-06` ("Nhu cầu:") | `04-06` (thí nghiệm ấn định) | `04-06` | `04-07` | `05-07`, `06-04` | `04-08` (gián tiếp), câu hỏi tự kiểm tra 4 | Ba thí nghiệm $1/8$, $5/4$, $1$ | Vấn đề, trực giác, ví dụ chung trang `04-06` | 4 |
| K7 Bellman cho $v_\pi$ | 5 | kết quả và chứng minh | `05-00`, `05-01` ("Nhu cầu:") | `05-01` | `05-02` | `05-03`, `05-04`, `05-06`, `05-06b` | `06-02` | `05-10` (tự làm), `05-10b` (lời giải trên mặt trang) | Phương trình tại L (4.1) → (4.5); $v_{\mathrm H}=2+\tfrac14v_{\mathrm H}+\tfrac14v_{\mathrm L}$ | Định lý tách khỏi các bổ đề theo kế hoạch A3 | 16 |
| K8 Quan hệ $v$–$q$, Bellman cho $q_\pi$ | 5 | kết quả | `05-07` ("Nhu cầu:" trên mặt trang) | `05-07` (ví dụ L–Tìm) | `05-07`, `05-08` | `05-07`, `05-08`, `05-09` (mỗi trang có dòng giả thiết; `05-07`, `05-09` có dòng "Chứng minh.") | `06-04` | `05-10` (khối 30 phút) | $q_\pi(\mathrm L,\mathrm{tim})$ theo $v_\pi$ | Ví dụ đứng trên cùng trang với mệnh đề | 6 |
| K9 Đánh giá chính sách bằng giải hệ | 6 | thuật toán | `06-01`, `06-07c` ("Nhu cầu:" khử thế tay không dùng được cho hệ hàng chục ẩn) | `06-05` (gộp nhánh), `06-02` | `06-02`, `06-03`, `06-07` (tính tay đủ các bước) | `06-07`, `06-07b`, `06-07c`, `06-07d` | `06-04`, `06-07e` (lưới 5×5) | `06-08` (sinh viên tự làm 3 phút), `06-08b` (lời giải trên mặt trang) | Hệ (5.1) → $P_\pi$, $r_\pi$ → $(I-\gamma P_\pi)v=r_\pi$ → bước 3–6 | Tính tay (`06-02`–`06-07`) trước giả mã (`06-07d`); nghịch đảo của robot ở ghi chú diễn giả `06-07b` | 20 |
| K10 Chuỗi Markov và MRP cảm sinh | 6 | khái niệm phụ | `06-05` ("Nhu cầu:" gộp $\pi$ với $p$) | `06-05` | `06-05` | `06-06` | `06-07` | `06-08` | Bảng gộp nhánh → $P_\pi$, $r_\pi$ | Chu trình rút gọn vì là phép gộp của K4 và K2; ghi lý do theo kế hoạch A4 | 3,5 |

Mỗi cụm lớn có một bài tập có lời giải trên mặt trang: K1 (`01-07b`), K2 (`02-07b`), K3 (`03-06b`), K4–K6 (`04-08b`), K7–K8 (`05-10b`, fragment), K9 (`06-08b`). Bài tự làm có gợi ý và lời giải trong ghi chú diễn giả: `05-10`.

Ví dụ xuyên suốt: robot thu gom lon hai mức pin, chính sách chia đều tại pin thấp, $\gamma=1/2$. Mỗi lần dùng lại trả lời một câu hỏi mới: một bước (`01-04`), tính Markov (`01-05`), bảng $p$ (`02-03`), lợi tức (`03-01`), cận (`03-05`), kỳ vọng hai bước (`04-04`), thí nghiệm ấn định (`04-06`), phương trình một bước (`05-02`), hệ và nghiệm (`06-02`, `06-03`), kiểm tra bằng $q$ (`06-04`), gộp nhánh (`06-05`), dạng ma trận (`06-07`), chính sách luôn Chờ (`06-08`), rủi ro cứu hộ thấp hơn (`07-01`). Dữ kiện được nêu lại trên trang dùng lại. Không có bài thực hành riêng; lưới 5×5 là môi trường thứ hai, theo Tình huống 03.1 của ghi chú.

## 3. Từng trang

Cột "Quyết định" so với deck trước đợt sửa (50 trang). Cột "Mục tiêu" ghi số mục tiêu học tập (1–5) ở `01-01c`.

### Mạch 1. Mở đầu

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `01-01` | Quá trình quyết định Markov | bìa, điểm vào mạch 1 | Luận đề một câu: giá trị là nghiệm duy nhất của hệ Bellman do mô hình Markov và chính sách sinh ra | — → tiên quyết | tất cả | sửa (luận đề theo RL nhẹ, câu chốt của điều phối viên) | 1 |
| `01-01b` | Tiên quyết và quy ước | mở đầu, kết quả kế thừa | "Nhắc lại (Bài 02):" tác tử, phần thưởng, tính Markov, hàm động lực, chính sách dừng, lợi tức với truy hồi và cận, $v_\pi$; thuật ngữ gốc (agent), (reward), (stationary policy), (discount factor) | bìa → ký hiệu | tất cả | sửa (MACH F1, PB 1: điểm vào nêu kết quả Bài 02; RL thuật ngữ) | 2 |
| `01-01d` | Tiên quyết và quy ước | mở đầu, ký hiệu | Công cụ xác suất, đại số; ký hiệu $t$, $\mathcal S$, $\mathcal S^+$, $\mathcal A(s)$, $\mathcal R$, $\Pr_\pi$, $\mathbb E_\pi$, $\mathrm H$, $\mathrm L$, $\mathrm{tim},\mathrm{cho},\mathrm{sac}$ | tiên quyết → mục tiêu | tất cả | thêm (tách từ `01-01b`: hai khối nhắc lại và ký hiệu vượt 60 âm tiết trên một trang; PB 3, SV 1) | 1 |
| `01-01c` | Mục tiêu học tập | mở đầu | Năm mục tiêu kiểm tra được, khớp ghi chú; "mô hình (model)" lần đầu | ký hiệu → nội dung | tất cả | sửa (thêm "(model)") | 1,5 |
| `01-02` | Nội dung | mở đầu | Bảy mạch đánh số khớp trang tiêu đề mạch; dòng đọc trước | mục tiêu → vấn đề trung tâm | tất cả | sửa (bỏ nhãn "Mục tiêu:", tên mạch mới) | 1 |
| `01-02b` | Vấn đề trung tâm | mở đầu, vấn đề của cả bài | Bài toán một dòng và câu trả lời có điều kiện của mạch 2–6; dòng nào cũng ghi đủ giả thiết ($p$ dừng, $\pi$ Markov dừng) | nội dung → tiêu đề mạch 2 | tất cả | sửa (TOAN 2, PB 15, SV nhẹ 2; song song với `07-02b`) | 2,5 |

### Mạch 2. Trạng thái Markov và mô hình môi trường

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `02-00` | 2. Trạng thái Markov và mô hình môi trường | điểm vào mạch 2 | Mô tả phản hồi một bước theo cặp trạng thái–hành động; ghi chú nêu phần kế thừa (Bài 02) và phần mới | vấn đề trung tâm → lựa chọn của robot | 1 | sửa (RL nhẹ: dòng dẫn; MACH F1: ghi chú) | 0,5 |
| `01-03` | Lựa chọn của robot ở pin thấp | K1 vấn đề | "Nhắc lại (Bài 02):" tính Markov, $p$; "Nhu cầu:" điều kiện để bảng $p$ đủ, quy tắc sinh; dữ kiện ba lựa chọn | tiêu đề mạch → quỹ đạo | 1 | sửa (quyết định (ii) của điều phối viên; MACH F2 câu nối vào ghi chú) | 1,5 |
| `01-04` | Quỹ đạo và lịch sử | K1 ví dụ dẫn nhập rồi định nghĩa | Dòng "Ví dụ." trước "Định nghĩa."; Định nghĩa 03.1 | lựa chọn → hai lịch sử | 1 | sửa (PB 2: tiêu đề và thứ tự) | 2 |
| `01-05` | Hai lịch sử, cùng trạng thái hiện tại | K1 trực giác, ví dụ | Hai lịch sử khác nhau cho cùng phân phối phản hồi | một bước → định nghĩa | 1 | sửa ("Trực quan.", tách dòng 23 âm tiết) | 1,5 |
| `01-06` | Tính Markov | K1 hình thức | Định nghĩa 03.2 với điều kiện xác suất dương; ghi chú nói định nghĩa trùng Bài 02 | hai lịch sử → phản ví dụ | 1 | sửa (ghi chú gọi tên hai lịch sử, PB 22; số hiệu không ngắt dòng) | 2 |
| `01-06b` | Ví dụ: trạng thái thiếu phòng làm việc | K1 ứng dụng (phản ví dụ, cách sửa) | Ví dụ 03.4 với bước suy luận "$R_1=1$ nên robot sang phòng 2" | định nghĩa → bài tập | 1, 4 | sửa (SV 5) | 2 |
| `01-07` | Bài tập: trạng thái của robot | K1 kiểm tra, đề; sinh viên tự làm 3 phút | Bài tập 03.1(b) | phản ví dụ → lời giải | 1 | sửa (lời giải chuyển sang `01-07b`) | 3 |
| `01-07b` | Bài tập: trạng thái của robot | K1 kiểm tra, lời giải trên mặt trang | $\tfrac12\ne\tfrac14$; thêm vị trí vào trạng thái | đề → hai phản hồi | 1 | thêm (PB 4: K1 chưa có lời giải trên mặt trang) | 1,5 |
| `02-02` | Ví dụ: hai phản hồi của hành động Tìm | K2 vấn đề và ví dụ dẫn nhập | Câu nối K1→K2 "Nhờ tính Markov, phản hồi được liệt kê theo cặp $(s,a)$"; cây phản hồi của Tìm | lời giải → bảng | 1 | sửa (MACH F2, PB 12) | 1,5 |
| `02-03` | Ví dụ: bảng phản hồi của robot | K2 ví dụ | Bảy hàng $(s,a,s',r,\text{xác suất})$ | cây → hàm động lực | 1 | sửa (nhãn $\mathrm H$, $\mathrm{tim}$; bỏ `rowspan`, `style`) | 2 |
| `02-04` | Hàm động lực | K2 trực giác, hình thức | Định nghĩa 03.4; ghi chú nêu định nghĩa đã có ở Bài 02 | bảng → xác suất chuyển | 1 | sửa (ghi chú kế thừa; công thức không ngắt dòng) | 2 |
| `02-05` | Xác suất chuyển và thưởng kỳ vọng | K2 ví dụ, kết quả | Ví dụ rồi Mệnh đề 03.6, chứng minh một dòng | hàm động lực → bộ MDP | 1 | sửa (dòng "Lưu ý:" chuyển sang ghi chú, SV nhẹ 11) | 2 |
| `02-06` | Quá trình quyết định Markov hữu hạn | K2 hình thức, ứng dụng | Định nghĩa 03.7 với quy tắc sinh; bộ của robot; "Mô hình của môi trường là $p$"; $\gamma$ ngoài $\mathcal M$ | xác suất chuyển → bài tập | 1 | sửa (RL nhẹ: mô hình là $p$) | 2 |
| `02-07` | Bài tập: đọc hàm động lực của robot | K2 kiểm tra, đề | Bài tập 03.2 với dữ kiện năm cặp | MDP → lời giải | 1 | tách (từ `02-07` cũ 74 âm tiết, bỏ `font-size:32px`) | 1,5 |
| `02-07b` | Bài tập: đọc hàm động lực của robot | K2 kiểm tra, lời giải trên mặt trang | Bảng $p(\mathrm H\mid s,a)$, $p(\mathrm L\mid s,a)$, $r(s,a)$ | đề → tiêu đề mạch 3 | 1 | thêm (tách) | 1,5 |

### Mạch 3. Lợi tức chiết khấu

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `03-00` | 3. Lợi tức chiết khấu | điểm vào mạch 3 | Gộp chuỗi phần thưởng thành một số hữu hạn; ghi chú nêu Mệnh đề 02.13 đã có, phần mới là quy ước hấp thụ và cận của robot | bài tập MDP → lợi tức của robot | 2 | sửa (MACH F1: ghi chú) | 0,5 |
| `03-01` | Lợi tức của robot | K3 nhắc lại, vấn đề, ví dụ | "Nhắc lại (Bài 02):" $G_t$; "Nhu cầu:" Chờ mãi cho $1+1+\cdots=\infty$, cần quy ước chung cho chuỗi hữu hạn và vô hạn và cận cho robot (MACH R1); hai dãy ba bước $3/2<7/4$ | tiêu đề → lượt | 2 | gộp (`03-01` và `03-03` cũ, quyết định (iii) của điều phối viên; bỏ hình trục thời gian vì tràn khung) | 2 |
| `03-02` | Lượt và hai loại nhiệm vụ | K3 hình thức | Định nghĩa 03.8; ghi chú mở bằng câu nối từ tổng có trọng số sang độ dài chuỗi | lợi tức của robot → định nghĩa lợi tức | 2 | sửa (MACH F5, PB 27: ghi chú) | 1,5 |
| `03-04` | Lợi tức chiết khấu | K3 hình thức | Định nghĩa 03.9, Nhận xét 03.10 (trạng thái hấp thụ) | lượt → cận | 2 | sửa ("Định nghĩa. Lợi tức (return) là…", bỏ "tổng thưởng") | 2 |
| `03-05` | Cận của lợi tức | K3 kết quả, ứng dụng | Mệnh đề 03.11 (đã có ở Bài 02); cận 6 của robot | lợi tức → bài tập | 2 | sửa (PB 17: dòng "Trực quan." sang ghi chú; TOAN 10: lập luận cho $-6$) | 2 |
| `03-06` | Bài tập: lợi tức và cận của robot | K3 kiểm tra, đề | Bài tập 03.3 (dãy $2,-3,1$) | cận → lời giải | 2 | tách (dữ kiện theo ghi chú đã commit thay dãy $(0,2,2)$ của kế hoạch) | 2 |
| `03-06b` | Bài tập: lợi tức và cận của robot | K3 kiểm tra, lời giải trên mặt trang | (a) không; (b) $3/4$, $2$; (c) $[0,3/2]$ | đề → tiêu đề mạch 4 | 2 | thêm (tách) | 2 |

### Mạch 4. Chính sách và hàm giá trị

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `04-00` | 4. Chính sách và hàm giá trị | điểm vào mạch 4; vấn đề của K4 | Cố định quy tắc chọn hành động để kỳ vọng có nghĩa | lời giải lợi tức → chính sách chia đều | 3 | thêm (A1) | 0,5 |
| `04-02` | Ví dụ: chính sách chia đều tại pin thấp | K4 vấn đề và ví dụ dẫn nhập | "Nhắc lại (Bài 02):" $v_\pi$; "Nhu cầu:" quá trình xuất phát tại $s$, ấn định hành động đầu; bảng chính sách | tiêu đề → định nghĩa | 3 | sửa (quyết định (ii); mô tả bằng lời chuyển sang ghi chú để giữ 6 dòng) | 1,5 |
| `04-03` | Chính sách Markov dừng | K4 trực giác, hình thức | Định nghĩa 03.13 với $\Pr(H_t=h_t)>0$ | ví dụ → xác suất đoạn quỹ đạo | 3 | sửa (TOAN 3; "(agent)" chuyển lên `01-01b`) | 2 |
| `04-03b` | Xác suất của một đoạn quỹ đạo | K4 kết quả, ứng dụng | Mệnh đề 03.14 với điều kiện xác suất dương; xác suất $1/4$ | định nghĩa → kỳ vọng hai bước | 3 | sửa (TOAN 3; dòng "Ký hiệu:" chuyển lên `01-01d`) | 2 |
| `04-04` | Ví dụ: kỳ vọng hai bước từ pin cao | K5 vấn đề và ví dụ | "Nhu cầu:"; cây hai bước (bản deck `robot-p04-two-step-tree-deck.svg`), $21/8$, kiểm theo tuyến tính | xác suất → giá trị trạng thái | 3 | sửa (PB 18, MACH F6, SV nhẹ 8) | 2 |
| `04-05` | Giá trị trạng thái | K5 trực giác, hình thức, ứng dụng | Định nghĩa 03.15 trên quá trình xuất phát tại $s$; khoảng $[9/8,33/8]$ với $\gamma^2M/(1-\gamma)$ | kỳ vọng hai bước → ba thí nghiệm | 3 | sửa (SV 3; "phần thưởng bị chặn") | 2 |
| `04-06` | Ví dụ: ba thí nghiệm từ pin thấp | K6 vấn đề, trực giác, ví dụ | "Nhu cầu:"; thưởng kỳ vọng bước sau; Tìm viết đủ $\tfrac12(2+\tfrac12\cdot\tfrac12)+\tfrac12(-3+\tfrac12\cdot2)=\tfrac18$ | $v_\pi$ → $q_\pi$ | 3 | sửa (PB 11, SV 2, PB 12) | 2 |
| `04-07` | Giá trị hành động | K6 hình thức | Định nghĩa 03.16, Nhận xét 03.17 | ba thí nghiệm → bài tập | 3 | sửa (dòng 41 âm tiết tách; "(action-value function)") | 2 |
| `04-08` | Bài tập: mô hình, chính sách và giá trị | K4–K6 kiểm tra, đề; khối 30 phút | Bài tập 03.5 (câu a) và 03.4 (câu b, c); ánh xạ ghi trong ghi chú diễn giả | $q_\pi$ → lời giải | 3 | sửa (PB 24; chuyển sang khối 30 phút, SV 6) | 0 (khối 30 phút) |
| `04-08b` | Bài tập: mô hình, chính sách và giá trị | K4–K6 kiểm tra, lời giải trên mặt trang; khối 30 phút | $9/8$, kiểm tra bằng hai thí nghiệm | đề → tiêu đề mạch 5 | 3 | giữ (chuyển sang khối 30 phút) | 0 (khối 30 phút) |

### Mạch 5. Phương trình Bellman kỳ vọng

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `05-00` | 5. Phương trình Bellman kỳ vọng | điểm vào mạch 5 | Tách bước đầu; từ khóa không KaTeX; ghi chú nêu hệ thức truy hồi đã có ở Bài 02 | lời giải → nhóm quỹ đạo | 4 | sửa (PB 13, SV 9, MACH F1) | 0,5 |
| `05-01` | Nhóm quỹ đạo theo bước đầu | K7 vấn đề, trực giác | "Nhu cầu:" cận sai số $3/2$; nhóm theo bước đầu | tiêu đề → phương trình tại L | 4 | sửa (TOAN 9) | 1,5 |
| `05-02` | Ví dụ: phương trình một bước tại pin thấp | K7 ví dụ | Phương trình (4.1) chưa chứng minh | nhóm → hệ thức đệ quy | 4 | sửa ("Ví dụ:", "Lưu ý:" về giả định chưa chứng minh) | 2 |
| `05-03` | Hệ thức đệ quy của lợi tức | K7 hình thức (bổ đề) | Bổ đề 03.18; ghi chú: đã có ở Bài 02 (Mệnh đề 02.13) | ví dụ → hai tầng | 4 | sửa (MACH F1, "phần thưởng bị chặn") | 2 |
| `05-04` | Hai tầng kỳ vọng | K7 hình thức (bổ đề) | Bổ đề 03.19 với $\Pr(H_t=h_t)>0$; dòng "Ký hiệu:" cho điều kiện viết tắt | hệ thức → tính Markov của tương lai | 4 | sửa (TOAN 3, SV 4) | 2,5 |
| `05-06` | Tính Markov của phần tương lai | K7 trực giác, hình thức (bổ đề) | "Trực quan." trước Bổ đề 03.20; điều kiện xác suất dương; "theo $\pi$ từ $t+1$" cho đẳng thức thứ hai | hai tầng → định lý | 4 | sửa (PB 6, TOAN 3; ghi chú theo PB 8) | 3 |
| `05-06b` | Phương trình Bellman kỳ vọng cho giá trị trạng thái | K7 hình thức (định lý) | Định lý 03.21; kết luận viết lại; phạm vi $\gamma=1$ trong ghi chú | bổ đề → $q$ theo $v$ | 4 | sửa (PB 16, RL trung bình) | 3 |
| `05-07` | Giá trị hành động theo giá trị trạng thái | K8 vấn đề, ví dụ, hình thức | "Nhu cầu:"; ví dụ L–Tìm viết trên một dòng; mệnh đề "Giả thiết như Định lý 03.21"; dòng "Chứng minh." | định lý → $v$ theo $q$ | 4 | sửa (PB 5, PB 7, MACH F7, TOAN 4) | 2,5 |
| `05-08` | Giá trị trạng thái theo giá trị hành động | K8 ví dụ, hình thức | Mệnh đề 03.23 với dòng giả thiết | $q$ theo $v$ → Bellman cho $q$ | 4 | sửa (TOAN 4) | 1,5 |
| `05-09` | Phương trình Bellman kỳ vọng cho giá trị hành động | K8 hình thức (hệ quả) | Hệ quả 03.24 với dòng giả thiết và "Chứng minh." một dòng; "sơ đồ cập nhật (backup diagram)" trong ghi chú | $v$ theo $q$ → bài tập | 4 | sửa (PB 7, PB 20, TOAN 4) | 2 |
| `05-10` | Bài tập: chỗ dùng tính Markov | K7–K8 kiểm tra; khối 30 phút | Bài tập 03.7; đề nêu chuỗi tính Markov của phần tương lai → $q$ theo $v$ → $v$ theo $q$ | hệ quả → bài tập tại pin cao | 4 | sửa (PB 7, SV nhẹ 1; chuyển sang khối 30 phút) | 0 (khối 30 phút) |
| `05-10b` | Bài tập: phương trình Bellman tại pin cao | K7 kiểm tra, lời giải trên mặt trang (fragment) | Bài tập 03.6 | bài tập → tiêu đề mạch 6 | 4 | thêm (A3) | 2 |

### Mạch 6. Đánh giá chính sách bằng hệ tuyến tính

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `06-00` | 6. Đánh giá chính sách bằng hệ tuyến tính | điểm vào mạch 6; vấn đề của K9 | Giải hệ Bellman để có giá trị bằng số | bài tập Bellman → bài toán đánh giá | 5 | thêm (A1) | 0,5 |
| `06-01` | Bài toán đánh giá chính sách | K9 vấn đề | "tính $v_\pi$ của một $\pi$ cho trước"; Đầu vào "$p$ đã biết" | tiêu đề → hệ của robot | 5 | sửa (RL nhẹ) | 1,5 |
| `06-02` | Ví dụ: hệ Bellman của robot | K9 ví dụ, ứng dụng của K7 | "Nhắc lại:" phương trình tại H; kiểm giả thiết; hệ (5.1) | bài toán → lời giải | 5 | sửa ("Ví dụ:", "Nhắc lại:") | 1,5 |
| `06-03` | Ví dụ: hệ Bellman của robot, lời giải | K9 ví dụ (tính tay) | Khử thế; thay lại viết đủ $\tfrac14(\tfrac{13}4+\tfrac74)$ | hệ → kiểm tra bằng $q$ | 5 | sửa (SV nhẹ 4, MACH F11) | 2 |
| `06-04` | Ví dụ: kiểm tra nghiệm bằng giá trị hành động | K8, K9 ứng dụng | Ví dụ 03.15: $3/4$, $15/8$, $13/8$; trung bình bằng $7/4$ | lời giải → gộp nhánh | 4, 5 | sửa (thêm $q_\pi(\mathrm L,\mathrm{tim})$, khung thành "Diễn giải:") | 2 |
| `06-05` | Ví dụ: gộp các nhánh của robot | K10 vấn đề, trực giác, ví dụ | "Nhu cầu:" gộp $\pi$ với $p$; bảng gộp | kiểm tra → định nghĩa MRP | 5 | sửa (MACH F3; dòng trung bình sang ghi chú) | 1,5 |
| `06-06` | Chuỗi Markov và quá trình phần thưởng Markov cảm sinh | K10 hình thức | Định nghĩa 03.26 với $s,s'\in\mathcal S$; "véc-tơ thưởng kỳ vọng" | gộp → dạng ma trận | 5 | sửa (TOAN 8, PB 19, PB 23) | 2 |
| `06-07` | Phương trình Bellman dạng ma trận | K9 hình thức, ví dụ | Mệnh đề 03.27 với dòng giả thiết; hệ của robot | MRP → nghiệm duy nhất | 5 | sửa (TOAN 4) | 1,5 |
| `06-07b` | Nghiệm duy nhất của hệ đánh giá chính sách | K9 hình thức (định lý) | Định lý 03.28: "MDP hữu hạn với $n$ trạng thái chưa kết thúc"; "Lưu ý:" $\gamma=1$ cần lượt chắc chắn kết thúc | dạng ma trận → thuật toán | 5 | sửa (TOAN 1, RL trung bình) | 2,5 |
| `06-07c` | Đánh giá chính sách bằng giải hệ tuyến tính | K9 thuật toán (vấn đề, đầu vào, đầu ra) | "Nhu cầu:" hệ hàng chục ẩn; $\pi$ Markov dừng; tập hữu hạn; chi phí $n^3$ không nhắc bước chưa xuất hiện | định lý → giả mã | 5 | sửa (PB 10, MACH F13, SV nhẹ 3, RL nhẹ) | 1,5 |
| `06-07d` | Đánh giá chính sách bằng giải hệ tuyến tính | K9 thuật toán (giả mã bảy bước) | Bước 1 kiểm $p(\cdot,\cdot\mid s,a)$ hoặc $p(\cdot\mid s,a)$ | đầu vào → lưới 5×5 | 5 | sửa (TOAN 5) | 2 |
| `06-07e` | Ví dụ: lưới 5×5 | K9 ứng dụng; có thể bỏ khi thiếu giờ | Dữ kiện đủ (bước khác $0$), "Tính $v_\pi$", kiểm tại A với $-1{,}3452$; hình `gridworld-5x5-deck.svg` lớn hơn, không chú thích lặp; ghi chú thêm Tình huống 03.2 | giả mã → bài tập | 5 | sửa (PB 18, SV nhẹ 5, TOAN 6, RL trung bình) | 2 |
| `06-08` | Bài tập: đánh giá chính sách luôn Chờ tại pin thấp | K9 kiểm tra, đề; sinh viên tự làm 3 phút | Bài tập 03.8 | lưới → lời giải | 5 | sửa (thời lượng theo SV 6) | 3 |
| `06-08b` | Bài tập: đánh giá chính sách luôn Chờ tại pin thấp | K9 kiểm tra, lời giải trên mặt trang | $(10/3,\,2)$; một dòng kết "chưa chứng minh là tối ưu" | đề → tiêu đề mạch 7 | 5 | sửa (PB 25) | 2 |

### Mạch 7. Tổng kết và chuyển tiếp

| Mã | Tiêu đề | Vị trí và bước | Lý do tồn tại, nhu cầu | Trước → sau | Mục tiêu | Quyết định (lý do) | Phút |
|---|---|---|---|---|---|---|---:|
| `07-00` | 7. Tổng kết và chuyển tiếp | điểm vào mạch 7 | Áp dụng đúng phương trình Bellman, giữ đủ giả thiết; từ khóa là khái niệm | lời giải → tổng kết | tất cả | sửa (PB 14, MACH F8) | 0,5 |
| `07-01a` | Tổng kết | kết luận | Bốn hàng: MDP, thưởng kỳ vọng, cận, giá trị $v_\pi$, $q_\pi$ | tiêu đề → tổng kết (tiếp) | 1–3 | sửa (MACH F4: thêm hàng mạch 4) | 1,5 |
| `07-01b` | Tổng kết | kết luận | Bellman, quan hệ $v$–$q$, nghiệm duy nhất; giả thiết đủ ($p$ dừng, $\pi$ Markov dừng); công thức đủ đối số | tổng kết → bài tập tổng hợp | 4–5 | sửa (TOAN 2, TOAN 7, PB 28, SV nhẹ 6) | 1,5 |
| `07-01` | Bài tập: robot với rủi ro cứu hộ thấp hơn | bài tập tổng hợp, đề | Bài tập 03.13: dùng $r(s,a)$, $P_\pi$, nghiệm duy nhất, quan hệ $q$ theo $v$ | tổng kết → lời giải | 1, 4, 5 | sửa (thay "ba hành động tại pin thấp" của A2 để không lặp `06-04`) | 1 |
| `07-02` | Bài tập: robot với rủi ro cứu hộ thấp hơn | bài tập tổng hợp, lời giải trên mặt trang | $v_\pi$ không đổi; $29/16<30/16$ | đề → kết luận vấn đề | 1, 4, 5 | sửa | 1,5 |
| `07-02b` | Kết luận về vấn đề trung tâm | kết luận | Năm dòng song song với `01-02b` (dòng 4 có $v_\pi$, $q_\pi$; dòng 6 "Cùng giả thiết, $\gamma<1$ làm $I-\gamma P_\pi$ khả nghịch"), mỗi dòng một điều kiện và một số liệu của robot; dòng giới hạn theo thứ tự outline; "Nguồn:" | lời giải → tự kiểm tra | tất cả | sửa (quyết định chung 11; RL trung bình; PB 26) | 2 |
| `07-04` | Câu hỏi tự kiểm tra | kết luận | Bốn câu: $r(s,a)$ còn thiếu; $\gamma=0$; trạng thái không ghi vị trí; luôn Chờ có tối ưu không | kết luận → bài tập về nhà | tất cả | sửa (MACH F9, PB 8, PB 9) | 1,5 |
| `07-03` | Bài tập về nhà và tài liệu đọc | kết luận | Bảng `Mạch \| Bài tập \| Chỉ trong ghi chú` theo bảng mạch của `exercises.md` (03.1–03.8, 03.15–03.25; cột thứ ba 03.9–03.14, Bài tập 03.12 ở mạch 5, 03.13 ở mạch 7); liên kết viewer "Ghi chú bài giảng · Bài tập"; Bài 04 | tự kiểm tra → hết | tất cả | sửa (SV nhẹ 10, RL nhẹ, quyết định chung 4; đồng bộ `exercises.md` 2026-10-14) | 1 |

## 4. Thời lượng

| Mạch | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Tổng |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Phút | 9 | 26,5 | 12 | 14 | 22,5 | 25,5 | 10,5 | 120 |

- **Sinh viên tự làm tại lớp (≥ 3 phút):** `01-07` (Bài tập 03.1, 3 phút, lời giải ở `01-07b`) và `06-08` (Bài tập 03.8, 3 phút, lời giải ở `06-08b`). Các trang bài tập khác có lời giải trên mặt trang được giảng như ví dụ mẫu.
- **Khối 30 phút chữa bài (ngoài 120 phút):** `04-08`/`04-08b` (Bài tập 03.4, 03.5; 8 phút), `05-10` (Bài tập 03.7; 8 phút), Bài tập 03.11 (7 phút) và Bài tập 03.12 (7 phút) của ghi chú. Bài tập 03.8 không thuộc khối này vì đã giải trong deck; mỗi bài chỉ được đếm một lần. Không có trình diễn mã.
- **Có thể bỏ khi thiếu giờ:** `06-07e` (lưới 5×5, 2 phút; Tình huống 03.1 có đủ trong ghi chú) và `03-06`/`03-06b` (Bài tập 03.3, 4 phút; chuyển sang khối 30 phút).
- Thời lượng tăng ở mạch 2 (thêm `01-07b`, `01-07` thành 3 phút) và mạch 1 (thêm `01-01d`) được bù bằng gộp `03-01`/`03-03` và chuyển `04-08`/`04-08b`, `05-10` sang khối 30 phút.

## 5. Mật độ mặt trang

Số đo bằng `density.py` của điều phối viên (âm tiết là số từ tách theo khoảng trắng sau khi bỏ tiêu đề, KaTeX và ghi chú; dấu câu đứng riêng sau công thức cũng được đếm). Trước sửa: 50 trang, 22 trang bị đánh dấu vượt. Sau lần soạn đầu (trước vòng biên tập): 71 trang, 0 trang nội dung vượt trần 60 âm tiết, 6 dòng hoặc 20 âm tiết mỗi dòng ngoài các ngoại lệ dưới; trung bình 45 âm tiết; 45 trang trên mức đích 40, trong đó các trang nội dung thường cao nhất 59 (`05-10`, `05-10b`) và hai trang ngoại lệ 66 (`01-01c`, `07-03`). Các trang trên 40 chủ yếu là trang bài tập có dữ kiện nêu lại và trang kết quả có giả thiết đầy đủ; mọi trang đã kiểm vừa khung 16:9. Không dùng lớp hay thuộc tính thu chữ; `style` cục bộ của deck cũ (bảng `font-size:32px`, `margin`, `padding`) đã bỏ.

### Trang vượt trần trước sửa

| Mã cũ | Trước (âm tiết / dòng / dòng dài nhất) | Quyết định | Sau |
|---|---|---|---|
| `01-02` | 56 / 8 / 16 | sửa | 45 / 8 / 8 (ngoại lệ, dưới) |
| `01-05` | 23 / 1 / 23 | sửa | 37 / 3 / 17 |
| `01-06` | 34 / 2 / 22 | sửa | 41 / 3 / 16 |
| `01-07` | 48 / 4 / 27 | sửa | 57 / 4 / 17 |
| `02-02` | 22 / 1 / 22 | sửa (gộp `02-01`) | 38 / 2 / 19 |
| `02-03` | 75 / 9 / 21 | sửa (ô bảng thành ký hiệu) | 21 / 2 / 11 |
| `02-04` | 25 / 2 / 22 | sửa | 51 / 4 / 17 |
| `02-07` | 74 / 8 / 20 | tách (`02-07`, `02-07b`) | 35 / 5 / 14 và 24 / 2 / 12 |
| `03-05` | 24 / 2 / 21 | sửa | 50 / 4 / 15 |
| `04-02` | 59 / 6 / 22 | sửa (gộp `04-01`) | 52 / 5 / 17 |
| `04-05` | 34 / 2 / 22 | sửa | 53 / 4 / 16 |
| `04-06` | 31 / 1 / 31 | sửa | 36 / 3 / 18 |
| `04-07` | 53 / 2 / 41 | sửa | 52 / 4 / 16 |
| `05-06` | 28 / 2 / 22 | tách (`05-06`, `05-06b`) | 56 / 4 / 18 và 42 / 3 / 15 |
| `05-10` | 52 / 4 / 22 | tách (`05-10`, `05-10b`) | 59 / 4 / 20 và 59 / 4 / 16 |
| `06-02` | 40 / 2 / 23 | sửa | 29 / 3 / 11 |
| `06-04` | 27 / 1 / 27 | sửa | 37 / 3 / 20 |
| `06-05` | 68 / 4 / 53 | sửa (đoạn dài sang ghi chú) | 49 / 4 / 14 |
| `06-07` | 45 / 3 / 24 | tách (`06-07`, `06-07b`, `06-07c`, `06-07d`) | 25 / 3 / 11; 47 / 4 / 16; 56 / 5 / 13; 52 / 7 / 14 |
| `06-08` | 78 / 4 / 37 | tách (`06-08`, `06-08b`) | 54 / 6 / 14 và 44 / 4 / 16 |
| `07-03` | 81 / 5 / 20 | sửa | 66 / 10 / 16 (ngoại lệ, dưới) |
| `07-04` | 52 / 4 / 23 | sửa | 56 / 5 / 16 |

### Sau vòng biên tập năm vai (2026-10-12)

`density.py`: 72 trang, trung bình 46,7 âm tiết (trước vòng biên tập 45,0), 44 trang trên mức đích 40. Trang nội dung trên 60: không có, trừ ba ngoại lệ dưới (`01-01c`, `07-02b`, `07-03`). Các trang chạm sát trần 60: `01-01b` 59, `01-03` 59, `04-05` 59, `05-06` 60, `01-02b` 60; mỗi trang đã kiểm vừa khung 16:9. `03-01` (gộp) 57.

Sau rà lại vòng 2: `01-01b` 60, `01-02b` 60, `03-01` 51, `04-02` 46, `04-05` 57, `04-06` 39, `05-04` 40, `05-07` 57, `05-08` 41, `05-09` 37 (3 dòng), `06-07` 33, `06-07b` 52, `07-02b` 73 (7 dòng, ngoại lệ), `07-04` 59. `density.py` đếm cả dấu câu đứng riêng sau công thức; ở `03-01` dấu chấm phẩy được đặt trong công thức để dòng "Nhu cầu:" (20 âm tiết) không bị đếm 21.

### Ngoại lệ được phép

| Mã | Số đo | Lý do |
|---|---|---|
| `01-01` | 22 âm tiết ở dòng luận đề | Bìa: câu luận đề do điều phối viên chốt, một câu; `density.py` dùng trần chung 20 âm tiết mỗi dòng |
| `01-01c` | 67 âm tiết / 5 dòng | Trang mục tiêu, trần 80 (`AGENTS.md` §"Mật độ chữ"); `density.py` dùng trần chung 60 |
| `01-02` | 45 âm tiết / 8 dòng | Trang nội dung với 7 mạch cộng một dòng đọc trước; quyết định chung mục 5 cho phép 7 dòng khi bài có 7 mạch, dòng đọc trước là tùy chọn của `AGENTS.md` |
| `02-00`, `03-00`, `05-00`, `06-00`, `07-00` | dòng dài nhất 21–25 | Trang tiêu đề mạch: dòng dẫn tối đa 25 âm tiết theo `AGENTS.md` §"Trang tiêu đề mạch" (đếm lại: 23, 21, 25, 22, 21); `density.py` dùng trần chung 20 |
| `07-02b` | 73 âm tiết / 7 dòng (trước: 55 / 5) | Trang trả lời vấn đề trung tâm: năm dòng song song với `01-02b` theo quyết định chung mục 11, cộng dòng "Giới hạn:" (bốn giới hạn, RL trung bình) và dòng "Nguồn:" bắt buộc; bỏ khung để giữ 7 dòng; trần 80 như trang tổng kết |
| `06-07d` | 53 âm tiết / 7 dòng | Giả mã bảy bước của Thuật toán 03.29 trên trang riêng (giả mã dưới 8 dòng được phép giữ một trang); giữ đủ bảy bước để khớp ghi chú |
| `07-03` | 76 âm tiết / 10 dòng (trước đợt đồng bộ 2026-10-14: 62 / 10) | Trang bài tập về nhà và tài liệu đọc của mạch kết luận (trần 80); bảng `Mạch | Bài tập | Chỉ trong ghi chú` sáu hàng bắt buộc theo `AGENTS.md`, mỗi hàng được đếm là một dòng; `density.py` đếm cả 33 số hiệu bài trong bảng, không tính chúng thì còn 43 âm tiết |

Kiểm tra trình duyệt xác nhận mọi trang nằm trong khung 16:9 và không chồng lên chân trang (mục "Kiểm tra" trong `review-log.md`).

## 6. Sai khác so với nguồn và kế hoạch A

- Ví dụ của Bài giảng gốc (Student MRP/MDP, trang 30–34, 49–54; xe đua, trang 51) được thay hoàn toàn bằng robot thu gom lon theo quyết định lập lại kế hoạch ngày 2026-09-20 (`storyboard-mdp-replanned.md`, mục "Viết lại deck theo robot — quyết định trước triển khai (20/09/2026)" trong `review-log.md`).
- Bài 03 kế thừa tính Markov, hàm động lực, lợi tức với hệ thức truy hồi và cận, $v_\pi$ từ Bài 02 (quyết định của điều phối viên sau MACH F1): `01-01b` nhắc lại các kết quả này, trang vấn đề của mạch 2–4 mở bằng "Nhắc lại:" rồi "Nhu cầu:", `03-01` và `03-03` cũ gộp làm một trang; định nghĩa và mệnh đề vẫn giữ trên deck vì ghi chú đánh số chúng (03.2, 03.4, 03.9, 03.11, 03.15) và chứng minh ở mạch 5 dùng điều kiện xác suất dương.
- Thứ tự nguồn (Bài giảng gốc: chuỗi Markov → MRP → MDP) được giữ như deck trước đợt sửa: MDP trước, chuỗi Markov và MRP được dựng lại ở mạch 6 bằng cách cố định chính sách (đã ghi từ đợt trước; ghi chú bài giảng theo cùng thứ tự).
- Kế hoạch A3 đề xuất 67 trang; deck có 72 trang sau vòng biên tập (thêm `01-01d`, `01-07b`; gộp `03-03` vào `03-01`). Bản trước vòng biên tập có 71 trang. Thêm `01-06b` (bước ứng dụng của K1), `04-03b` (Mệnh đề 03.14, dùng cho cây và Bổ đề 03.20), `06-07e` (bước ứng dụng ngoài robot), `07-01b` (tách bảng tổng kết vì tràn khung). Bớt: gộp `02-01` vào `02-02`, `04-01` vào `04-02`, `05-05` vào `05-04`; gộp đề hai bài tập ở `04-08`. Thời lượng vẫn 120 phút.
- Ví dụ trọng số (nay ở `03-01`) đặt trước `03-02` theo thứ tự Mục 2.1–2.2 của ghi chú (ví dụ trọng số trước định nghĩa lượt).
- Hai hình bản deck: `robot-p04-two-step-tree-deck.svg` (nhãn cột $G_0^{[2]}$, "3; 1/2 (gộp H, L)") và `gridworld-5x5-deck.svg` (bỏ ba dòng chú thích lặp, cắt khung, chữ lớn hơn, nhãn "+10" có viền trắng). Hai hình gốc giữ nguyên vì ghi chú bài giảng dùng và trích nhãn của chúng.
- Các trang kết quả `05-07`, `05-08`, `05-09`, `06-07` ghi giả thiết bằng lời ("Giả thiết như phương trình Bellman cho $v_\pi$") và giữ số hiệu riêng (03.22, 03.23, 03.24, 03.27) sau phát biểu; mỗi mặt trang có tối đa một số hiệu (MACH R3, vòng rà lại 2).
- Tiếng Anh của thuật ngữ đặt ở lần dùng đầu, nay là `01-01b` (Markov property, dynamics function, return, discount factor, state-value function, agent, reward, stationary policy); các trang định nghĩa hình thức `01-06`, `02-04`, `03-04`, `04-05` và `01-01c` không lặp lại (MACH R7).
- Bài tập tổng hợp `07-01`/`07-02` dùng Bài tập 03.13 (rủi ro cứu hộ thấp hơn) thay cho "ba hành động tại pin thấp" của A2, vì ba giá trị $q_\pi(\mathrm L,\cdot)$ đã là Ví dụ 03.15 ở `06-04` (rủi ro D của kế hoạch).
- Bài tập `03-06` dùng dãy $(2,-3,1)$ của Bài tập 03.3 trong ghi chú đã commit, thay dãy $(0,2,2)$ trong A3.
- Tiêu đề A3 "Bổ đề: tính Markov của phần tương lai" và "Định lý: nghiệm duy nhất khi $\gamma<1$" đổi thành cụm danh từ vì "Bổ đề:", "Định lý:" không thuộc tiền tố tiêu đề được phép.
- Hình `robot-p06-policy-evaluation-setup.svg` dự kiến cho `01-02b` được dùng ở `06-01`; ở `01-02b` hình làm trang tràn khung.
- Sơ đồ cập nhật (`backup-diagrams.svg`, hình mới của ghi chú) không đặt trên deck vì nhãn quá nhỏ ở cỡ trang; ghi chú diễn giả `05-09` dẫn tới hình trong ghi chú.
- Cấu hình RevealJS thêm `scrollActivationWidth:null` (như deck Bài 01, Bài 02) để màn hẹp 390 px giữ chế độ trang chiếu.
