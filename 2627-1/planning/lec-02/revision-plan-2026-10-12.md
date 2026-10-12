# Kế hoạch sửa Bài 02 theo chuẩn 2026-10-12

Báo cáo của tác tử kiểm toán chỉ đọc (Opus 5.5, `high`, loại `general-purpose`), được điều phối viên lưu nguyên văn kèm phần "Quyết định của điều phối viên" ở cuối.

Phạm vi: kiểm toán chỉ đọc. Đầu vào đã đọc toàn bộ: deck `2627-1/lecture-02-giao-dien-tac-tu-moi-truong.html` (41 trang, 7 mạch), ghi chú `materials/lec-02/lecture-note.md` (499 dòng) và năm tệp planning; `density.py` trên deck; đối chiếu thêm `hw02.pdf`, ghi chú Bài 01 và Bài 03, `index.html`, SML `sec_mdp_introduction.tex` và mẫu math-4-AI Bài 07.

## A. Deck

### A1. Mạch hiện tại và mạch đề xuất

Giữ 7 mạch. Mã `L02-0N-00` chưa từng dùng.

| N | Hiện tại (trang) | Tên đề xuất | Dòng dẫn (âm tiết) | Từ khóa (≤5) | Trang tiêu đề | id |
|---|---|---|---|---|---|---|
| 1 | Bài toán ra quyết định tuần tự (01-01…05) | Mở đầu (bìa là trang tiêu đề) | — | — | L02-01-01 | `mach-1` |
| 2 | Tương tác và phần thưởng (02-01…07) | Vòng tương tác và tín hiệu thưởng | "Muốn mô tả một chuỗi quyết định bằng dữ liệu, phải cố định thứ tự quan sát, hành động và phần thưởng." (22) | Tác tử · Môi trường · Bước tương tác · Tín hiệu học · Giả thuyết phần thưởng | L02-02-00 | `mach-2` |
| 3 | Trạng thái và thông tin quan sát (03-02…08) | Thông tin khả dụng và tính Markov | "Muốn chọn hành động khi cảm biến chỉ thấy bốn ô kề, phải tách vị trí thật khỏi dữ liệu tác tử nhận." (23) | Trạng thái · Quan sát · Biểu diễn · Lịch sử và quỹ đạo · Tính Markov | L02-03-00 | `mach-3` |
| 4 | Chính sách lựa chọn hành động (04-01…05) | Quy tắc chọn hành động | "Muốn so sánh hai tác tử trên cùng mê cung, phải viết cách chọn hướng thành hàm hoặc phân phối." (20) | Chính sách xác định · Chính sách ngẫu nhiên · Phân phối hành động | L02-04-00 | `mach-4` |
| 5 | Hàm giá trị và mô hình môi trường (05-01…09) | Lợi tức, hàm giá trị và mô hình | "Muốn so sánh hai chính sách có cùng thưởng tức thời, phải đánh giá cả chuỗi thưởng về sau." (19) | Ưu tiên dừng · Hệ số chiết khấu · Lợi tức · Hàm giá trị trạng thái · Mô hình môi trường | L02-05-00 | `mach-5` |
| 6 | Phần thưởng định hướng hành vi (06-01…07) | Thiết kế phần thưởng | "Muốn biết hàm thưởng dẫn tới hành vi nào, phải so sánh lợi tức của các đường kết thúc." (19) | Chi phí mỗi bước · Trạng thái kết thúc · Ngưỡng đổi hành vi · Phạt bổ sung · Khuyến khích và chế tài | L02-06-00 | `mach-6` |
| 7 | Tổng kết và tự kiểm tra (07-01…03) | Tổng kết và chuyển tiếp | "Muốn dùng các thành phần của giao diện cho mô hình quyết định Markov, phải giữ đủ giả thiết của từng định nghĩa." (23) | Giả thiết không được bỏ · Câu hỏi tự kiểm tra · Bài tập về nhà · Quá trình quyết định Markov | L02-07-00 | `mach-7` |

Thời lượng đề xuất (120 phút): mạch 1: 9, 2: 17, 3: 27, 4: 14, 5: 26, 6: 15, 7: 12.

### A2. Mạch mở đầu và mạch kết luận

Mạch mở đầu, thứ tự: 01-01 bìa → 01-06 (mới) Tiên quyết và quy ước → 01-03 Mục tiêu → 01-04 Nội dung → 01-02 (thành Vấn đề trung tâm).

- Bìa 01-01: thêm "Bài 02", `h1` "Giao diện tác tử–môi trường", câu luận đề "Hành vi của tác tử được quyết định bởi thông tin nó có và lợi tức kỳ vọng mà nó cực đại hóa." (hoặc "Đặc tả một chuỗi quyết định: thông tin, quy tắc chọn hành động và lợi tức kỳ vọng.").
- 01-06 mới "Tiên quyết và quy ước": "Nhắc lại:" xác suất có điều kiện, kỳ vọng; Bài 01 giới thiệu tác tử học từ tương tác, phần thưởng là tín hiệu số, chính sách, giá trị, mô hình ở mức trực quan. "Ký hiệu:" $t\in\{0,1,\dots\}$; $\mathcal A$ bốn hướng; $\mathcal S$ tọa độ ô (cột, hàng) từ 0, hàng tăng xuống dưới; $R_{t+1}\in\mathbb R$; $T$ thời điểm kết thúc; $\mathbb E_\pi$ theo chính sách và môi trường.
- 01-03 Mục tiêu: 5 mục tiêu gắn bài tập: (1) ghi một bước $(O_t,A_t,R_{t+1},O_{t+1})$ (02.1); (2) phân biệt $S_t,O_t,X_t$ và kiểm Markov (02.3, 02.4); (3) viết và kiểm chính sách xác định/ngẫu nhiên (02.5); (4) tính lợi tức chiết khấu, $v_\pi$, đọc $p(s',r\mid s,a)$ (02.6–02.8); (5) tìm ngưỡng chi phí đổi hành vi (02.9).
- 01-04 "Nội dung": `<ol>` 7 mục trùng tên trang tiêu đề mạch; ngoại lệ 7 dòng ghi trong storyboard; dòng đọc trước (Sutton–Barto §3.1–3.5) trong ghi chú.
- 01-02 thành "Vấn đề trung tâm", giữ `source-maze.svg`: một dòng bài toán "Đặc tả chuỗi quyết định trên mê cung 8×8 sao cho đánh giá và so sánh được các cách đi." và mỗi mạch một dòng trả lời có điều kiện (mạch 2: một bước sinh $(A_t,R_{t+1},O_{t+1})$; mạch 3: tọa độ là trạng thái Markov khi bản đồ cố định, bốn ô kề thì không; mạch 4: chính sách gán một phân phối trên bốn hướng; mạch 5: với $\pi,\gamma$ cố định, $v_\pi(s)$ đánh giá trạng thái, mô hình dự báo một bước; mạch 6: chi phí mỗi bước trên 2,5 thì tác tử tối ưu chọn hố). Giữ ≤60 âm tiết bằng hai cột.
- 01-05 "Câu hỏi kiểm tra": bỏ; câu 2–3 vào ghi chú trang Vấn đề trung tâm.

Mạch kết luận, thứ tự: 07-00 → 07-01 (Tổng kết, tách hai trang) → 07-04 (bài tập tổng hợp, mới) → 07-05 (Trả lời vấn đề trung tâm, mới) → 07-02 (Câu hỏi tự kiểm tra) → 07-03 (Bài tập về nhà và tài liệu đọc).

| Kết quả | Giả thiết không được bỏ | Công thức |
|---|---|---|
| Bước tương tác (Định nghĩa 02.2) | ranh giới tác tử–môi trường cố định; phản hồi đến sau $A_t$ | $(O_t,A_t,R_{t+1},O_{t+1})$ |
| Biểu diễn (02.7) | chỉ dùng thông tin có trước $A_t$ | $X_t=f_t(O_{0:t},A_{0:t-1},R_{1:t})$ |
| Tính Markov (02.10) | đúng với mọi lịch sử kết thúc tại $s$; trạng thái do người mô hình chọn | $\Pr(\cdot\mid H_t,A_t)=\Pr(\cdot\mid S_t,A_t)$ |
| Lịch sử là trạng thái Markov (Mệnh đề 02.11) | kích thước tăng theo $t$ | $\tilde S_t=H_t$ |
| Chính sách (02.13–02.14) | $\pi(\cdot\mid x)\ge0$, tổng bằng 1; không đổi theo thời gian | $\pi(a\mid x)=\Pr(A_t=a\mid X_t=x)$ |
| Trọng số hình học (Định lý 02.18) | lợi ích cộng; trọng số dương, không tăng, dùng chung cho mọi độ dài | $w_i=\gamma^{i-1}$ |
| Lợi tức (02.20–02.21) | $T$ hữu hạn, hoặc $\gamma<1$ và thưởng bị chặn | $G_t=\sum_k\gamma^kR_{t+k+1}$, $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$ |
| Hàm giá trị (02.22) | $\pi$ Markov cố định; môi trường dừng; kỳ vọng hữu hạn | $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ |
| Mô hình (02.24) | trạng thái và thưởng rời rạc; Markov; dừng | $p(s',r\mid s,a)$, $\sum_{s',r}p=1$ |
| Ngưỡng đổi hành vi (Mệnh đề 02.27) | $\gamma=1$; chuyển xác định; tác tử tối ưu | $c^*=(10+h)/4$ |

- Bài tập tổng hợp 07-04 (= Bài tập 02.16): mê cung đích–hố với $\gamma=0{,}9$; $c=1$: $G_{\text{đích}}\approx1{,}22$, $G_{\text{hố}}=-1{,}9$ chọn đích; $c=3$: $G_{\text{đích}}\approx-8{,}15$, $G_{\text{hố}}=-5{,}7$ chọn hố; ngưỡng $c^*=10\gamma^5/[(1-\gamma^6)/(1-\gamma)-(1+\gamma)]\approx2{,}12<2{,}5$. Tác tử rà toán tính lại.
- 07-05 "Kết luận:" khi trạng thái thỏa Markov và $\pi$ cố định, mỗi trạng thái được đánh giá bằng $v_\pi(s)$; quan sát một phần cần biểu diễn từ lịch sử; thứ tự các đường kết thúc phụ thuộc $c$ và $\gamma$. "Nguồn: PPTX trang 1–27; Sutton và Barto (2018), §3.1–3.5".
- 07-02: "Câu hỏi: trả lời và nêu kết quả đã dùng." 3–4 câu từ 07-02 hiện tại và câu 2–3 của 02-07, 03-08, 05-09.
- 07-03: bảng `Mạch | Bài tập`; "Tài liệu đọc: Sutton và Barto (2018), §3.1–3.5, §17.3; Tạ Việt Cường, bài giảng 2–3, trang 1–27."; liên kết "Ghi chú bài giảng · Bài tập"; dòng nối sang Bài 03.

### A3. Bảng từng trang

Chung: mọi trang thiếu thuật ngữ tiếng Anh ở lần đầu; không trang nào có ghi chú mở bằng "Trang này", mã nội bộ hay thời lượng.

| Mã | Âm tiết | Vấn đề theo chuẩn mới | Quyết định | Đề xuất cụ thể |
|---|---|---|---|---|
| L02-01-01 | 20 | Thiếu "Bài 02" và tên bài; thiếu câu luận đề; ghi chú dùng "Bài học" làm chủ ngữ | sửa | Như A2 |
| L02-01-06 | — | Thiếu trang Tiên quyết và quy ước | thêm | Như A2 |
| L02-01-03 | 40 | Mục tiêu 3 không đo được; ghi chú có "ta có thể ghi" | sửa | 5 mục tiêu; ghi chú nêu bài tập đo từng mục tiêu |
| L02-01-04 | 45; 7 dòng | Hơn 6 dòng; tiêu đề "Nội dung"; danh sách không đánh số | sửa | `<ol>` 7 mạch, ngoại lệ 7 dòng; dòng đọc trước trong ghi chú |
| L02-01-02 | 21 | Nhãn "Nhiệm vụ:" ngoài danh sách; chưa có bài toán trung tâm | sửa, chuyển vị trí | Thành "Vấn đề trung tâm", cuối mạch 1 |
| L02-01-05 | 39 | Trang câu hỏi ngoài cấu trúc mạch mở đầu; thiếu "Câu hỏi:"; không có lời giải | bỏ | Câu 2–3 vào ghi chú trang Vấn đề trung tâm |
| L02-02-00 | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| L02-02-02 | 24 | Thiếu "Ví dụ:"; khung dùng "=" thay "là"; chưa mở bằng "Nhu cầu:" | sửa, đưa lên đầu mạch | "Ví dụ: một bước trên mê cung 8×8"; "Nhu cầu:" trước dữ kiện; khung "Một bước tương tác gồm quan sát, hành động, phần thưởng và quan sát mới."; thuật ngữ gốc |
| L02-02-01 | 38; dòng 23 | Dòng >20; mở bằng định nghĩa; "Ví dụ:" sai nhãn; hình dùng ký hiệu trước 02-03 | sửa | Đặt sau 02-02; "Định nghĩa." tác tử (agent), môi trường (environment); "Ví dụ." ≤20 âm tiết |
| L02-02-03 | 16 | Thiếu "Định nghĩa."; thiếu số hiệu | sửa nhẹ | "Định nghĩa." và "(Định nghĩa 02.2)" |
| L02-02-04 | 44 (bảng) | "đúng/sai"; thiếu thuật ngữ gốc | sửa nhẹ | "đúng hay sai"; thuật ngữ; ghi chú dẫn hw02 Bài 1 |
| L02-02-05 | 58; dòng 22 | Trên đích 40; dòng >20; "Ví dụ:" sai nhãn; "điểm thưởng"; "kỳ vọng", "tích lũy" dùng trước định nghĩa | sửa | Tách câu giả thuyết hai dòng; "Ví dụ."; dòng cuối vào ghi chú; tiêu đề "Giả thuyết phần thưởng" |
| L02-02-06 | 30 | Nhãn "Ví dụ trò chơi:" sai; chỉ số $O_i$ | sửa nhẹ | "Ví dụ."; phản hồi trễ (delayed reward); chỉ số $t$ |
| L02-02-07 | 42 | Thiếu "Câu hỏi:"; "Hãy ghi"; không có "Lời giải:" trên mặt trang | tách | "Bài tập: một bước từ ô (1,2)" với "Câu hỏi:" và "Lời giải:" fragment (= 02.1); câu 2–3 sang 07-02; ghi chú "Gợi ý:" |
| L02-03-00 | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| L02-03-02 | 27 | $S_t,O_t,X_t$ trước định nghĩa; không "Nhu cầu:"; ghi chú 175 âm tiết | sửa | "Ví dụ: cảm biến bốn ô kề tại ô (2,1)"; "Nhu cầu:"; bằng lời; rút ghi chú |
| L02-03-11 | 63 | Vượt 60; ba định nghĩa và $f_t$ trên một trang; ghi chú câu mảnh | sửa và tách | Bảng định nghĩa ≤40, "Định nghĩa.", thuật ngữ gốc; $f_t$ sang 03-12 |
| L02-03-12 | — | (từ 03-11) | thêm | "Biểu diễn từ thông tin khả dụng": $X_t=f_t(\cdot)$, "Ý nghĩa:", trường hợp $X_t=\phi(O_t)$ |
| L02-03-13 | — | Cụm lịch sử/quỹ đạo chưa có ví dụ | thêm | "Ví dụ: ba bước đầu trên mê cung 8×8": (0,2) Đông, (1,2) Bắc, (1,1) Đông tới (2,1), thưởng −1 mỗi bước; $H_3$ |
| L02-03-09 | 22 | Mở bằng định nghĩa; nhãn ngoài danh sách | sửa | "Định nghĩa." mẫu, lịch sử $H_t$, quỹ đạo $\tau$ (trajectory); dùng dữ kiện 03-13 |
| L02-03-06 | 17 | Nhãn "Đầy đủ:", "Một phần:" | sửa nhẹ | "Định nghĩa." hai dòng; full/partial observability |
| L02-03-14 | — | Tính Markov thiếu vấn đề, trực giác, ví dụ | thêm | "Ví dụ: mê cung có chìa khóa": "Nhu cầu:"; cùng ô cửa, có hay không chìa khóa cho kết quả khác |
| L02-03-04 | 26 | Thiếu "Định nghĩa."; trực giác chỉ trong ghi chú | sửa | "Định nghĩa." tính Markov (Markov property); ghi chú nêu quy ước xác suất dương |
| L02-03-10 | 39 | Tiêu đề dạng câu hỏi; câu mảnh; kết quả chưa gắn nhãn | sửa | "Mở rộng trạng thái bằng lịch sử"; "Mệnh đề." (02.11); "Chứng minh." một dòng; "Lưu ý:" kích thước tăng theo $t$ |
| L02-03-08 | 88; dòng 24 | Vượt 1,47 lần; 4 câu không nhãn; không lời giải | tách | "Bài tập: cảm biến bốn ô kề (a)/(b)" (= 02.3): mã tại (1,2), (2,1), (3,1), cặp trùng, phân loại; lời giải ở 03-15 mới; câu 3–4 sang 07-02 |
| L02-04-00 | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| L02-04-01 | 12 | Mở bằng định nghĩa; thiếu "Nhu cầu:"; "trạng thái" lệch "biểu diễn" | sửa | "Nhu cầu: hai tác tử ở cùng ô (1,2) có thể chọn hai hướng khác nhau."; giữ câu định nghĩa; ghi chú nói rõ $X_t=S_t$; chính sách (policy) |
| L02-04-02 | 46 | Trên đích 40; thiếu "Ví dụ:" | sửa | "Ví dụ: hai quy tắc tại ô (1,2)"; rút chú thích |
| L02-04-03 | 17 | Thiếu "Định nghĩa." | sửa nhẹ | deterministic policy |
| L02-04-04 | 30 | "Ví dụ từ bảng trước"; thiếu "Định nghĩa." | sửa | Nêu lại dữ kiện; stochastic policy |
| L02-04-07 | — | Cụm chính sách thiếu ứng dụng | thêm | "Ví dụ: xác suất một dãy hai hành động" |
| L02-04-05 | 29 | Thiếu "Câu hỏi:"; không lời giải | sửa | "Bài tập: chính sách ngẫu nhiên tại một ô" với "Lời giải:" fragment (= 02.5) |
| L02-05-00 | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| L02-05-01 | 39; 7 dòng; 3 khung | >6 dòng; >1 khung; lặp Bài 01 | sửa | "Nhu cầu:" và ví dụ hai đường 16 và 18 bước; bỏ thẻ |
| L02-05-11 | — | Ví dụ (2,0), (1,1) chỉ trong ghi chú | thêm | "Ví dụ: hai chuỗi thưởng (2,0) và (1,1)", $\gamma=1$ và $0{,}5$ |
| L02-05-10 | 71; dòng 22 | Vượt 60; định nghĩa, định lý, bảng trên một trang; "Định lý:" sai dấu; ghi chú 458 âm tiết có chứng minh và URL | tách | "Ưu tiên dừng" với "Định nghĩa."; định lý sang 05-12; chứng minh sang ghi chú bài giảng |
| L02-05-12 | — | (từ 05-10) | thêm | "Trọng số hình học": "Định lý." đủ giả thiết, "Ý nghĩa:", "Chứng minh." một dòng "(Định lý 02.18)" |
| L02-05-03 | 19 | Thiếu ví dụ trước công thức; thiếu "Định nghĩa."; $\gamma<1$ chỉ trong ghi chú | sửa | "Ví dụ." ba bước −1, $\gamma=0{,}5$ cho $-1{,}75$; lợi tức (return); "Lưu ý:" tiếp diễn cần $\gamma<1$ |
| L02-05-04 | 39; dòng 21 | Dòng >20; thiếu "Ví dụ:" | sửa | "Ví dụ: hai nhánh kết thúc từ $s$" |
| L02-05-05 | 45 | Trên đích 40; thiếu "Định nghĩa."; "Hai nhánh trên" | sửa | state-value function; nêu lại dữ kiện |
| L02-05-13 | — | Hàm giá trị thiếu ứng dụng; bảng giá trị nguồn chưa dùng | thêm | "Ví dụ: giá trị của chính sách trên mê cung 8×8" dùng `source-values.svg`: xuất phát −16, (7,6) là −1; "Nhận xét." dự đoán (prediction) và điều khiển (control) |
| L02-05-08 | 37 | Mở bằng định nghĩa; $P$ lệch $p$ | sửa | Ví dụ một bước lên trước; "Định nghĩa."; mô hình (model); dùng $p$ |
| L02-05-09 | 51 | Trên đích 40; thiếu "Câu hỏi:"; không lời giải | tách | "Bài tập: lợi tức ba bước" (câu 1 và 4) với "Lời giải:" (= 02.6); câu 2–3 sang 07-02 hoặc ghi chú |
| L02-06-00 | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| L02-06-01 | 31 | Tiêu đề không theo dạng ví dụ; thiếu "Nhu cầu:"; $\alpha$ trùng bước học; nhãn G, H trùng $G_t,H_t$ | sửa | "Ví dụ: mê cung đích–hố"; $\alpha\to c$; nhãn $\mathrm G,\mathrm H$ (sửa SVG) |
| L02-06-02 | 33; 2 khung | >1 khung; $G_{\text{đích}}$ lẫn $G_t$ | sửa | Bảng hai hàng; "Ví dụ: mê cung đích–hố, hai lợi tức" |
| L02-06-03 | 20 | Tiêu đề kiểu khẩu hiệu | sửa nhẹ | "Ví dụ: mê cung đích–hố, ba mức chi phí" |
| L02-06-04 | 8 | Kết quả chưa nhãn; thiếu giả thiết | sửa | "Mệnh đề." với $\gamma=1$, chuyển xác định, tác tử tối ưu |
| L02-06-05 | 35 | Ngưỡng tổng quát chưa nhãn | sửa nhẹ | "Mệnh đề." (02.27); "Lưu ý:" $h$ hữu hạn |
| L02-06-06 | 42 | Thiếu "Câu hỏi:"; không lời giải | sửa | "Bài tập: phạt hố bổ sung" với "Lời giải:" (= 02.9) |
| L02-06-07 | 80; dòng 24; 2 khung | Vượt 1,33 lần; >20/dòng; 2 khung; không dòng nguồn | sửa | ≤60 âm tiết, một khung; pháp lý và đạo đức vào ghi chú; giữ vị trí cuối mạch |
| L02-07-00 | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| L02-07-01 | 53 (bảng) | Không theo khuôn ba cột | sửa, tách đôi | Bảng A2 |
| L02-07-04 | — | Thiếu bài tập tổng hợp | thêm | A2 (= 02.16) |
| L02-07-05 | — | Thiếu trang trả lời vấn đề trung tâm | thêm | A2 |
| L02-07-02 | 34 | Tiêu đề và nhãn chưa đúng; ghi chú chỉ đáp số | sửa, đặt trước 07-03 | "Câu hỏi tự kiểm tra"; "Câu hỏi: trả lời và nêu kết quả đã dùng." |
| L02-07-03 | 62; 6 dòng | Vượt 60; h3 thay nhãn; thiếu bảng `Mạch | Bài tập` và liên kết viewer | sửa | Theo A2; "Bài tập về nhà và tài liệu đọc" |

Mã mới không dùng lại các mã đã bỏ (03-01, 03-03, 03-05, 03-07, 04-06, 05-02, 05-06, 05-07).

### A4. Cụm khái niệm và sáu bước

| Cụm (mạch) | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Thiếu hoặc lỗi |
|---|---|---|---|---|---|---|---|
| Giao diện (2) | thiếu | 02-01 | 02-02 | 02-03 | thiếu | 02-07 | Thiếu vấn đề và ứng dụng; định nghĩa trước ví dụ; thiếu bài có lời giải |
| Tín hiệu và phần thưởng (2) | 02-04 | 02-05 | 02-05 | 02-05 | 02-06 | 02-07 câu 2–3 | Cụm phụ, dạng rút gọn, ghi lý do |
| S/O/X (3) | 03-02 | 03-02 | 03-02 | 03-11 | thiếu | 03-08 câu 1 | Ký hiệu trước định nghĩa; thiếu "Nhu cầu:" |
| Lịch sử và quỹ đạo (3) | thiếu | thiếu | thiếu | 03-09 | thiếu | 03-08 câu 4 | Mở bằng định nghĩa; thêm 03-13 |
| Quan sát đầy đủ/một phần (3) | 03-06 | 03-06 | 03-06 | 03-06 | thiếu | 03-08 câu 1 | Gộp chấp nhận được |
| Tính Markov (3) | thiếu | ghi chú | thiếu | 03-04 | 03-10 | 03-08 câu 2–3 | Thêm 03-14 |
| Chính sách (4) | thiếu | 04-01 | 04-02 | 04-03, 04-04 | thiếu | 04-05 | "Nhu cầu:" và 04-07 |
| Ưu tiên dừng và chiết khấu (5) | 05-01 | ghi chú | ghi chú | 05-10 | 05-03 | 05-09 câu 4 | Ví dụ lên mặt trang (05-11); chứng minh sang ghi chú |
| Lợi tức (5) | 05-01 | 05-10 | thiếu | 05-03 | 06-02 | 05-09 câu 1 | Thiếu ví dụ trước công thức |
| Hàm giá trị (5) | 05-01 | 05-04 | 05-04 | 05-05 | yếu | 05-09 câu 2 | Ứng dụng 05-13 |
| Mô hình (5) | 05-08 | 05-08 | 05-08 (sau công thức) | 05-08 | thiếu | 05-09 câu 3 | Ví dụ lên trước |
| Thiết kế phần thưởng (6) | 06-01 | 06-01 | 06-02, 06-03 | 06-04 | 06-05, 06-07 | 06-06 | Thiếu bài có lời giải trên mặt trang |

Không cụm nào có bài tập "Lời giải:" trên mặt trang: lỗi hệ thống của deck.

### A5. Ví dụ xuyên suốt

- "Mê cung 8×8" (PPTX tr. 25–26): xuất phát (0,2), đích $\mathrm G=(8,6)$ ngoài lưới, thưởng −1 mỗi bước, 16 bước; dùng thêm ở 03-13, 03-14, 04-07, 05-13.
- "Mê cung đích–hố": mạch 6 và 07-04, so $\gamma=1$ với $0{,}9$.
- Ví dụ một lần: "bộ điều khiển robot", "trò chơi thắng–thua", "môi trường hai nhánh", "hai chuỗi thưởng (2,0) và (1,1)".

## B. Ghi chú bài giảng

### B1. Đối chiếu từng mục hiện có

Quy ước: mục ghi chú §k ứng với mạch k+1 của deck.

| Dòng | Mục hiện có | Mạch | Thành phần chuẩn | Thiếu hoặc cần đổi |
|---|---|---|---|---|
| 1 | `# Bài 02 — …` | — | 1 | Đạt |
| 3 | Dòng học phần | — | 2 | Giữ hoặc bỏ |
| 7 | `## 1. Bài toán ra quyết định tuần tự` | 1 | — | Giải thể: vấn đề và hình mê cung vào đầu §1 mới |
| 11 | `### Mê cung và chuỗi quyết định` | 1 | 7 | Thành Ví dụ 02.1 ở đoạn mở §1 cùng kết quả Bài 01 |
| 17 | `### Mục tiêu và kiến thức tiên quyết` | 1 | 3, 4 | Tách thành hai mục `##` |
| 23 | `### Nội dung bài học` | 1 | — | Bỏ; thay bằng Bản đồ chủ đề (hiện chỉ ở outline dòng 128–131) |
| 35 | Câu hỏi kiểm tra (mạch 1) | 1 | 8 | Bỏ hoặc gộp |
| — | (không có) | — | 5 Bảng ký hiệu | Thiếu (B6) |
| 53 | `## 2. Tương tác và phần thưởng` | 2 | §1 mới | Đổi tên "Vòng tương tác và tín hiệu thưởng"; mở bằng bài toán |
| 55, 59 | Tác tử và môi trường; Một bước | 2 | tám bước | Ví dụ một bước (02.3) trước Định nghĩa 02.1–02.2; "Một cách trực quan" |
| 67, 77, 81 | Tín hiệu học; Giả thuyết; Phản hồi trễ | 2 | — | Nhận xét 02.3–02.5; thiếu hình `delayed-feedback.svg` |
| 85 | Câu hỏi kiểm tra | 2 | 8 | Bài tập 02.1 có `hint`; kết mục |
| 103 | `## 3. Trạng thái…` | 3 | §2 | Mở bằng thiếu hụt của §1 |
| 105–149 | S/O/X; lịch sử; đầy đủ; Markov; mở rộng | 3 | — | Thêm Ví dụ 02.7 trước Định nghĩa 02.8; Ví dụ 02.9 trước Định nghĩa 02.10; Mệnh đề 02.11 có `proof` |
| 153 | Câu hỏi kiểm tra | 3 | 8 | Bài tập 02.3, 02.4 |
| 175 | `## 4. Chính sách…` | 4 | §3 | Đoạn mở là định nghĩa; nhúng `source-policy.svg` |
| 179, 190, 204 | Ví dụ; xác định; ngẫu nhiên | 4 | — | Định nghĩa 02.13–02.14 trong khối; Ví dụ dãy hai hành động |
| 216 | Câu hỏi kiểm tra | 4 | 8 | Bài tập 02.5 |
| 234 | `## 5. Hàm giá trị…` | 5 | §4 | — |
| 236, 240 | Kết quả dài hạn; Ưu tiên dừng | 5 | — | Định lý (254) vào `theorem` bốn phần; chứng minh (265–302) chia bước |
| 325–354 | Lợi tức; Kỳ vọng; $v_\pi$; Mô hình | 5 | — | Chặn 333–335 thành Mệnh đề 02.21 có `proof`; Ví dụ 02.16 (giá trị trên mê cung); đoạn 364 có 9 câu |
| 366 | Câu hỏi kiểm tra | 5 | 8 | Bài tập 02.6–02.8 |
| 382 | `## 6. Phần thưởng định hướng…` | 6 | §5 | — |
| 384–422 | Quy tắc; hai lựa chọn; ngưỡng; phạt hố | 6 | — | Mệnh đề 02.27 có `proof`; dự đoán/điều khiển (430) lên §4 thành Nhận xét 02.26 |
| 432 | Câu hỏi kiểm tra | 6 | 8 | Bài tập 02.9 |
| 448 | Khuyến khích và chế tài | 6 | — | Nhận xét 02.29 |
| 458 | `## 7. Tổng kết và tự kiểm tra` | 7 | 9 | `## Tóm tắt chương` theo cấu trúc mới |
| 471 | Câu hỏi kiểm tra (mạch 7) | 7 | 10 | `## Bài tập củng cố` ba mức (02.10–02.14) |
| 487 | `### Bài tập và tài liệu đọc` | 7 | 11 | `## Hướng dẫn đọc thêm và tài liệu tham khảo`; bỏ "slide" (497) |
| — | (không có) | — | 8 Tình huống áp dụng | Thiếu (B4) |

Thêm `note-topic-id` theo chủ đề `lec-02-topic-NN`, giữ id cũ `lec-02-part-0N` cho mục.

### B2. Kế hoạch đánh số

Không có thuật toán. Bộ đếm chung (số dòng là vị trí hiện tại): 02.1 Định nghĩa tác tử, môi trường, ranh giới (57); 02.2 Định nghĩa bước tương tác (63); 02.3 Nhận xét ba dạng tín hiệu học (75); 02.4 Nhận xét giả thuyết phần thưởng (79); 02.5 Nhận xét phản hồi trễ (83); 02.6 Định nghĩa trạng thái, quan sát, biểu diễn (111); 02.7 Định nghĩa hàm biểu diễn $f_t$ (113–121); 02.8 Định nghĩa mẫu, lịch sử, quỹ đạo, $T$ (125–133); 02.9 Định nghĩa quan sát đầy đủ và một phần (137); 02.10 Định nghĩa tính Markov (143–147); 02.11 Mệnh đề lịch sử là trạng thái Markov, có `proof` (151); 02.12 Nhận xét cửa sổ hữu hạn và chi phí (151); 02.13 Định nghĩa chính sách xác định (192); 02.14 Định nghĩa chính sách ngẫu nhiên (206–212); 02.15 Nhận xét trường hợp riêng, $X_t=S_t$, chính sách khác thuật toán học (202, 214); 02.16 Định nghĩa lợi ích cộng $U$, $\succ$, $[r,a]$ (244–248); 02.17 Định nghĩa ưu tiên dừng (250–252); 02.18 Định lý ưu tiên dừng buộc trọng số hình học, có `proof` (254–302); 02.19 Nhận xét vai trò giả thiết, phản ví dụ lập phương, $\gamma>1$, $\gamma=0$ (315–323); 02.20 Định nghĩa lợi tức (329–332); 02.21 Mệnh đề chặn $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$, có `proof` (333–335); 02.22 Định nghĩa $v_\pi$ (350); 02.23 Nhận xét kỳ vọng hữu hạn khi $\gamma=1$, hạn chót (352); 02.24 Định nghĩa mô hình $p(s',r\mid s,a)$ (358–360); 02.25 Định nghĩa $p(s'\mid s,a)$ và $\bar r(s,a)$ (360–364); 02.26 Nhận xét dự đoán và điều khiển (từ 430); 02.27 Mệnh đề ngưỡng $c^*=(10+h)/4$, có `proof` (420–428); 02.28 Nhận xét phạt mỗi bước, $c=0$, tác tử tối ưu khác tác tử đang học (404, 428); 02.29 Nhận xét khuyến khích và chế tài (448–454).

Ví dụ (bộ đếm riêng): 02.1 mê cung 8×8 (15); 02.2 robot (57); 02.3 một bước Đông (61); 02.4 đường 16 và 18 bước (79); 02.5 trò chơi (83); 02.6 ô (2,1) và bốn ô kề (107); 02.7 ba bước đầu (mới); 02.8 (2,1) và (3,1) (137); 02.9 chìa khóa (mới); 02.10 hai quy tắc tại (1,2) (181); 02.11 bảng chính sách xác định (196); 02.12 xác suất dãy hai hành động (mới); 02.13 (2,0) và (1,1) (242, 304–313); 02.14 ba bước −1, $\gamma=0{,}5$ (327); 02.15 hai nhánh (339); 02.16 giá trị trên mê cung, −16 (mới, PPTX tr. 26); 02.17 mô hình một bước (356); 02.18 mê cung đích–hố (386–390); 02.19 hai lợi tức (394–402); 02.20 bảng $c=0,1,3$ (408–416).

Bài tập (bộ đếm riêng, chung với `exercises.md`): 02.1–02.9 cuối mỗi mục (C); 02.10–02.14 Bài tập củng cố, chỉ trong ghi chú; 02.15–02.17 chỉ trong `exercises.md`. Tình huống: 02.1 và 02.2.

### B3. Tiêu chuẩn thứ nhất và trình bày sáng sủa

| Tiêu chí | Vi phạm (dòng) | Cách sửa |
|---|---|---|
| Giọng kể | Giọng khách quan, không ngôi; "chúng ta" 0 lần, "ta" 5 lần (15, 107, 202, 430) | "chúng ta" cho kế hoạch và lựa chọn, "ta" trong tính toán; câu khách quan trong khối |
| Tài liệu làm chủ ngữ | 25 "Bài học gồm bảy phần"; 19 "Sau bài học, người học cần…"; 491 "Bài 03 sẽ trình bày…" | Chủ ngữ là đối tượng hoặc "chúng ta"; bỏ dòng 25 |
| Vấn đề đi trước công cụ | 177, 57, 238 mở bằng định nghĩa | Mỗi `##` mở bằng bài toán có số liệu trên mê cung |
| Câu mảnh | 63, 121, 331, 346, 390, 352 | Câu đủ thành phần; giả thiết trong khối định nghĩa |
| Công thức có câu dẫn và câu đọc | 115→119; 194; 328–334; 396/400; 426 | Câu trước và sau mỗi công thức; tách 426 thành suy diễn có căn cứ |
| Bước suy diễn có căn cứ | 334 (không ghi căn cứ); 151 (Markov của $H_t$ bằng lời); 319 (dấu của $V(a)^3-V(b)^3$); 404 ("chỉ cần so sánh hai đường ngắn nhất") | `aligned` với `&&\text{(…)}`; Mệnh đề 02.11 và 02.27 có `proof` |
| Chứng minh theo bước | 265–302 chưa có "Bước k" | Ba bước: hai hiệu lợi ích; truy hồi $w_{j+1}=\gamma w_j$; chiều ngược; $\square$ |
| Một ý một đoạn | 15 (9 câu), 111, 121, 137, 151, 352 (8 câu), 364 (9 câu), 404, 428 | Tách đoạn |
| Bản đọc bằng lời và phản ví dụ | Định lý 254 có phản ví dụ nhưng chưa theo khuôn "Bỏ <giả thiết>: …"; Markov thiếu phản ví dụ | Danh sách "Bỏ…: …"; Markov có phản ví dụ chìa khóa |
| Ví dụ trước phát biểu | Vi phạm ở 125, 143, 192 | Ví dụ 02.7 và 02.9; bảng 196 lên trước |
| Không tham chiếu ra ngoài tệp | 497 "ký hiệu của slide"; 177 "mỗi mũi tên"; 214 "bảng trước"; 352 "hai nhánh trên" | Dẫn số hiệu; nhúng `source-policy.svg`; nêu lại dữ kiện |
| Hình được đọc | 65, 139 không có đoạn đọc hình | Thêm; nhúng `agent-environment-loop.svg`, `delayed-feedback.svg` |
| Thuật ngữ gốc ở lần đầu | Không có | Thêm theo bảng Việt–Anh (outline chưa có bảng) |
| Bài tập | 7 khối không đánh số, không `hint`; tiêu đề "Câu hỏi kiểm tra" | Đánh số; `hint`; lời giải có "Kiểm tra lại" |

### B4. Phần cần thêm

Móc nối: sau 02.6 ($O_t$ khác $S_t$; $X_t$ là hàm của dữ liệu); sau 02.10 (Markov là tính chất của cách chọn trạng thái, khác quan sát đầy đủ); sau 02.22 ($v_\pi$ là kỳ vọng của $G_t$); sau 02.24 (mô hình dự báo một bước, khác hàm giá trị); trước và sau Định lý 02.18 (cần 02.16–02.17, dẫn tới 02.20).

"Trong thực hành" sau 02.11, 02.18, 02.21, 02.22, 02.24, 02.27: cửa sổ khung hình chồng (CartPole Bài 04, Flappy Bird Bài 07) không bảo đảm Markov; $\gamma<1$ cho lợi tức hữu hạn trong LunarLander (Bài 05–06); $v_\pi$ ước lượng bằng bảng $V$ (Bài 05); mô hình dùng bởi quy hoạch động (Bài 04), không cần trong phi mô hình; phạt mỗi bước làm tác tử kết thúc sớm.

Tình huống áp dụng: 02.1 Robot giao hàng trong kho dạng lưới (hw02 Bài 10): trạng thái (ô, mức pin); thưởng −1 mỗi bước, +10 khi giao; $\gamma=0{,}9$; kiểm Markov (mức pin trong trạng thái), quan sát một phần (cảm biến va chạm), $G_0$ một lộ trình, $p$ cho một bước có trượt; dẫn ngược 02.6, 02.10, 02.20, 02.24. 02.2 Giả thiết không thỏa: biểu diễn bốn ô kề trùng nhau trên mê cung 8×8: hai ô cùng mã cần hai hướng khác nhau nên mọi chính sách xác định trên $X$ sai ở ít nhất một ô; tác tử lặp vòng; khắc phục bằng chính sách ngẫu nhiên hoặc biểu diễn có bộ nhớ; tìm cặp ô trên `source-policy.svg`, nếu không có dùng Sutton–Barto Ví dụ 13.1; nối 02.9, 02.13, 02.14 với hw02 Bài 6.

Ứng dụng: Bài 03 (MDP, Bellman), Bài 04 (CartPole), Bài 05–06 (LunarLander), Bài 07 (Flappy Bird). Kết mục bằng văn xuôi ở §1–§5. Tóm tắt chương: 02.2 → 02.6 → 02.10 → 02.14 → Định lý 02.18 → 02.22 → 02.24 → Mệnh đề 02.27. Bài tập củng cố 02.10–02.14: nhận biết (ghép phát biểu với chính sách, giá trị, mô hình; ý nghĩa $\gamma=0$, $0{,}5$, gần 1); tính toán (chặn $\lvert G_t\rvert\le10$ với $R_{\max}=1$, $\gamma=0{,}9$; cửa sổ $k=1$ không Markov bằng cặp (2,1)/(3,1)); vận dụng (vì sao cần chính sách ngẫu nhiên khi quan sát một phần).

Độ dài: hiện ~6 440 từ; đích 12 000–14 000 từ.

### B5. Giáo trình đối chiếu theo mục

| Mục | Nguồn |
|---|---|
| Mở chương | PPTX tr. 1–2, 25–26; Sutton–Barto (SB) §1.1, §1.3; SML `sec_intro.tex`, `sec_mdp_introduction.tex` |
| §1 Vòng tương tác | PPTX tr. 4, 7–9, 11, 14–15; SB §3.1, §3.2, §1.1; hw02 Bài 1 |
| §2 Thông tin và Markov | PPTX tr. 16–19; SB §3.1, §17.3; SML định nghĩa tính chất Markov; hw02 Bài 2 |
| §3 Chính sách | PPTX tr. 20–21; SB §3.5; Puterman (1994) Ch. 2 §2.1; SB §13.1 và Ví dụ 13.1; hw02 Bài 6 |
| §4 Lợi tức, giá trị, mô hình | PPTX tr. 10, 13, 22–24; SB §3.3–3.5, §4.1; Szepesvári (2010) Ch. 1; Berkeley CS188 bài 09 tr. 22; đề xuất Russell–Norvig AIMA §17.1 cho ưu tiên dừng (cần xác minh); SML "Giá trị của quỹ đạo" $U(\tau)$ |
| §5 Thiết kế phần thưởng | Ví dụ do người dùng duyệt; SB §17.4; hw02 Bài 5 |
| Tình huống | hw02 Bài 10; SB Ví dụ 13.1 |

Số mục cần tác tử soạn xác minh trên bản in.

### B6. Bảng ký hiệu đề xuất và chỗ lệch

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$, $T$ | chỉ số bước; thời điểm kết thúc | $\{0,1,\dots\}$; $\mathbb N$ hoặc $\infty$ |
| $\mathcal S$, $S_t$, $s,s'$ | tập trạng thái; trạng thái tại $t$; giá trị | hữu hạn trong ví dụ |
| $\mathcal O$, $O_t$, $o$ | quan sát | — |
| $\mathcal X$, $X_t$, $x$ | biểu diễn | — |
| $f_t$ | hàm biểu diễn | $\mathcal O^{t+1}\times\mathcal A^t\times\mathbb R^t\to\mathcal X$ |
| $\mathcal A$, $\mathcal A(s)$, $A_t$, $a$ | hành động; hành động hợp lệ tại $s$ | hữu hạn |
| $\mathcal R$, $R_{t+1}$, $r$ | phần thưởng | $\mathbb R$; $\mathcal R$ rời rạc trong mô hình |
| $H_t$, $h$ | lịch sử | dãy hữu hạn |
| $\tau$ | quỹ đạo, $\tau=H_T$ | — |
| $\tilde S_t$ | trạng thái mở rộng | — |
| $\pi(x)$, $\pi(a\mid x)$ | chính sách xác định; ngẫu nhiên | $\mathcal X\to\mathcal A$; phân phối trên $\mathcal A$ |
| $U$, $w_i$, $\succ$, $[r,a]$ | lợi ích chuỗi; trọng số; ưu tiên; phép nối | — |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $<1$ khi $T=\infty$ |
| $G_t$, $R_{\max}$ | lợi tức; chặn thưởng | $\mathbb R$; $\ge0$ |
| $v_\pi(s)$, $\mathbb E_\pi$ | hàm giá trị trạng thái; kỳ vọng theo $\pi$ và động lực | $\mathbb R$ |
| $p(s',r\mid s,a)$, $p(s'\mid s,a)$, $\bar r(s,a)$ | mô hình | xác suất; $\mathbb R$ |
| $c$, $h$ | chi phí mỗi bước; phạt hố | $\ge0$ |
| $\mathrm G$, $\mathrm H$, $\mathrm S$ | nhãn nút đích, hố, xuất phát | nhãn |

Tương ứng SML: $v_\pi$ ↔ $V^\pi$; $p(s',r\mid s,a)$ ↔ $T(s,a,s')$, $R(s,a,s')$; $G_0$ ↔ $U(\tau)$.

Chỗ lệch: (1) $P$ (deck 05-08, ghi chú 359) và $p$ (Bài 03, SB); (2) $\alpha$ là chi phí mỗi bước nhưng là bước học ở Bài 05; (3) nhãn "G", "H" trùng $G_t$, $H_t$; (4) $V$ trong phản ví dụ lập phương trùng bảng $V(s)$, đổi thành $W$; (5) outline dòng 105 dùng "cột $x$, hàng $y$"; (6) chính sách "cho từng trạng thái" (04-01) so với "biểu diễn" (04-03/04-04, ghi chú 177); (7) $\mathcal A$ và $\mathcal A(s)$ chưa nối; (8) 05-03 chỉ có $T$ hữu hạn, ghi chú có nhiệm vụ vô hạn; (9) "phần thưởng tích lũy", "điểm thưởng", "tổng thưởng", "lợi tức"; (10) mục tiêu học tập deck khác ghi chú.

## C. Bài tập (`exercises.md` mới, 12 bài)

| Số hiệu | Mạch | Mức | Đối tượng và dữ kiện | Trùng hay mới | Năng lực đo |
|---|---|---|---|---|---|
| 02.1 | 2 | nhận biết | Từ (1,2) đi Bắc tới (1,1), thưởng −1; ghi $A_t,R_{t+1},O_{t+1}$ | trùng 02-07 | chỉ số thời gian của bước |
| 02.2 | 2 | nhận biết | Ba tình huống: ảnh có nhãn; phân cụm; robot thưởng cuối lượt | mới (hw02 Bài 1) | nhãn, thưởng, phản hồi trễ |
| 02.3 | 3 | tính toán | Mã bốn ô kề tại (1,2), (2,1), (3,1); cặp trùng; phân loại | trùng 03-08, 03-15 | S, O, X |
| 02.4 | 3 | vận dụng | Mê cung chìa khóa và cửa: chọn trạng thái Markov, đếm $\lvert\mathcal S\rvert$ | mới | kiểm và sửa Markov |
| 02.5 | 4 | tính toán | $\pi(\cdot\mid x)$ thiếu một giá trị; hợp lệ; xác suất dãy hai hành động | trùng 04-05 | phân phối; xác định/ngẫu nhiên |
| 02.6 | 5 | tính toán | Ba bước −1, $\gamma\in\{0;0{,}5;1\}$; so (2,0) với (1,1) | trùng 05-09 | lợi tức chiết khấu |
| 02.7 | 5 | tính toán | Hai nhánh 3 và 5 bước, xác suất 0,5; $v_\pi$ với $\gamma=1$ và $0{,}5$ | mới | $G_t$ và $v_\pi$ |
| 02.8 | 5 | tính toán | Bước Đông trượt: 0,8 thành công, 0,2 đứng yên, thưởng −1; viết $p$, $p(s'\mid s,a)$, $\bar r$ | mới | đọc và kiểm mô hình |
| 02.9 | 6 | tính toán | Mê cung đích–hố, $c=3$: điều kiện $h>2$ | trùng 06-06 | ngưỡng đổi hành vi |
| 02.15 | 5 | chứng minh | $U([r,a])=r+\gamma U(a)$ suy ra tính dừng; $\gamma=0$ phá tương đương chặt | mới | chứng minh có giả thiết |
| 02.16 | 6 | vận dụng | Mê cung đích–hố, $\gamma=0{,}9$, $c=1$ và $3$; ngưỡng ~2,12 | trùng 07-04 | tổng hợp |
| 02.17 | 2–6 | vận dụng | Mô hình hóa robot hút bụi hoặc đèn giao thông: $\mathcal S,\mathcal A,p,R$, kết thúc, quan sát, Markov | mới (hw02 Bài 10) | đặc tả bài toán |

hw02 Bài 3, 4, 7, 8, 9 để lại cho Bài 03.

## D. Rủi ro và thứ tự

Thứ tự: planning (outline thêm bảng thuật ngữ Việt–Anh, sửa dòng 105; storyboard: bản đồ mạch, mục cho trang tiêu đề mạch, âm tiết trước/sau, loại bài tập, 120 phút; `concept-flow-audit.md` đánh dấu lịch sử) → ghi chú → deck (sửa SVG G/H và $\alpha$) → `exercises.md` → index thêm nhóm Bài tập.

Rủi ro: nhiều quyết định cũ là chỉ dẫn của người dùng (tiêu đề câu hỏi 03-10; câu định nghĩa 04-01; bỏ 05-02, 05-07; trang xã hội cuối mạch 6; quy tắc "Câu hỏi kiểm tra" cuối mỗi phần; tiêu đề 06-01); các lượt rà soát cũ dùng OpenRouter không được coi là bằng chứng; đổi ký hiệu và thuật ngữ kéo theo Bài 03; giữ liên kết index khi viết lại; không cần ngoại lệ raster.

Câu hỏi tác tử nêu: (1) giữ hay bỏ "Câu hỏi kiểm tra" cuối mỗi mạch; (2) đổi tiêu đề 03-10; (3) "Nhu cầu:" ở 04-01 và "trạng thái" với "biểu diễn"; (4) ví dụ ba bước ở 05-03; (5) $p$ thay $P$; (6) $\alpha\to c$; (7) "lợi tức (return)"; (8) "điểm thưởng"→"phần thưởng"; (9) rút 06-07; (10) tên giảng viên trên bìa; (11) Bài 01 chưa có số hiệu; (12) nguồn AIMA §17.1; (13) bỏ 01-05.

## Quyết định của điều phối viên (2026-10-12)

Yêu cầu hiện hành của người dùng là áp dụng chuẩn 2026-10-12 cho mọi học liệu Bài 01–07; chuẩn này thay các chỉ dẫn trang lẻ trước đó khi hai bên mâu thuẫn. Quyết định:

1. Trang "Câu hỏi kiểm tra" cuối mỗi mạch đổi thành trang "Bài tập: <chủ đề>" có "Câu hỏi:" và "Lời giải:" trên mặt trang; các câu tự kiểm tra còn lại gom về trang "Câu hỏi tự kiểm tra" của mạch kết luận. Ghi trong review-log là thay thế quy tắc 2026-09-18.
2. Đổi tiêu đề L02-03-10 thành "Mở rộng trạng thái bằng lịch sử".
3. Thêm "Nhu cầu:" trước câu định nghĩa ở 04-01, giữ câu định nghĩa; chính sách định nghĩa trên biểu diễn $X_t$, ghi chú nêu $X_t=S_t$ khi quan sát đầy đủ.
4. Thêm một dòng "Ví dụ." ba bước vào 05-03.
5. Dùng $p$ chữ thường thống nhất với Bài 03 và Sutton–Barto.
6. Đổi $\alpha$ thành $c$ trong mạch 6, sửa SVG tương ứng; nhãn nút viết chữ đứng $\mathrm G,\mathrm H,\mathrm S$.
7. Dùng "lợi tức (return)" ở lần đầu, "lợi tức" về sau trong toàn bộ Bài 02; Bài 03 đồng bộ trong đợt sửa của bài đó.
8. "điểm thưởng" → "phần thưởng".
9. Rút 06-07 xuống ≤60 âm tiết, phần còn lại vào ghi chú diễn giả; giữ vị trí cuối mạch 6.
10. Không thêm tên giảng viên trên bìa.
11. Dẫn kết quả Bài 01 bằng tên mục và phát biểu lại; khi ghi chú Bài 01 có số hiệu (đang sửa song song), một đợt đồng bộ sau sẽ thêm số hiệu. Ghi giới hạn này trong review-log.
12. Chỉ dẫn Russell–Norvig AIMA §17.1 nếu tác tử soạn xác minh được nội dung và số mục; nếu không, bỏ.
13. Bỏ 01-05; câu 2–3 vào ghi chú trang Vấn đề trung tâm.
