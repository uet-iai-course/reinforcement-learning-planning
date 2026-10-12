# Kế hoạch sửa Bài 01 theo chuẩn 2026-10-12

Báo cáo của tác tử kiểm toán chỉ đọc (Opus 5.5, `high`, loại `general-purpose`), điều phối viên lưu lại. Quyết định của điều phối viên cho các câu hỏi ở mục D nằm trong `planning/quyet-dinh-chuan-2026-10-12.md`, mục 8.

Đã đọc: `AGENTS.md`, `CLAUDE.md`, hai mẫu học liệu, bộ mẫu math-4-AI Bài 07, deck (42 `data-slide-id` trong 7 `<section>` ngoài), ghi chú (310 dòng), ba tệp planning, văn bản trang 5–30 của PPTX nguồn, mục lục Sutton–Barto (bản tại `/data/tqlong/qa/sources/sutton-barto-rl2020`, trang in bằng trang PDF trừ 22).

**Phát hiện chặn bàn giao hoặc nghiêm trọng**
1. CSS cục bộ thu nhỏ chữ cho mọi trang: dòng 6 của deck có `.reveal .slides section[data-slide-id]{font-size:.84em}` và `.reveal table{font-size:.82em}`; deck tự định nghĩa hệ lớp riêng (`.box`, `.card`, `.grid2`, `.check`) và đổi màu `h1/h2`.
2. Chưa có trang tiêu đề mạch; các trang A00…G00 đặt chữ cái phần trên mặt trang.
3. Mạch 1 trộn mở đầu với nội dung (P + A + B); thiếu câu luận đề, "Tiên quyết và quy ước", "Vấn đề trung tâm"; mạch kết luận thiếu bảng tổng kết, bài tổng hợp, trang trả lời vấn đề trung tâm.
4. Tic-tac-toe không nhất quán: `tictactoe-board.svg` có X ở ô 1, 5; O ở ô 2, 4, 8; ô trống 3, 6, 7, 9 (4 hành động hợp lệ; 3 O so với 2 X nên O đi trước, chưa nêu). Hình cây (G01) và hình giá trị (G03) chỉ vẽ $a=3,7,9$; ghi chú L258 viết $\mathcal A(S_t)=\{3,7,9\}$; $\arg\max$ ở G03 bỏ sót nước 6. Chỉ số thời gian mơ hồ: trạng thái "gồm lượt chơi" (G02) trong khi $A_t$ chỉ do X chọn; G03 vẽ thế cờ sau nước của X (afterstate) nhưng gọi là $S_{t+1}$.
5. Lỗi toán trong ghi chú: L202 viết giá trị thế cờ sau nước thắng là $+1$, mâu thuẫn quy ước $v_\pi(S_T)=0$ với $R_{t+1}=+1$ (L105, L258).
6. Ghi chú lộ lời quy trình: L272 "sai khác so với nguồn cần ghi vào nhật ký rà soát"; L118, L241, L270 "bước 'thuật toán' không áp dụng"; L12 "note cũng không có [code demo]".
7. Ghi chú chưa đạt cấu trúc chương: không có khối định nghĩa, ví dụ, bài tập hay gợi ý (chỉ 7 khối `solution`), không hình; mục không đánh số, không kết mục, không "Trong thực hành", không tình huống, không tóm tắt; 5 886 từ.

## A. Deck

### A1. Mạch

Hiện tại 7 mạch: 1 = P00–P02 + A00–A04 + B00–B02; 2 = C00–C05; 3 = D00–D03; 4 = E00–E02; 5 = F00–F03; 6 = G00–G04; 7 = H04–H07, Z00 và phụ lục H00–H03. Đề xuất 7 mạch: gộp E và F thành mạch 5 (nguồn đặt liền tr. 26–27; thăm dò và khai thác định nghĩa qua chính sách và giá trị ước lượng).

| Mạch | Tên | Dòng dẫn | Từ khóa | Trang tiêu đề | `id` | Trang hiện có | Phút |
|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu (bìa) | — | — | P00 | — | P00, P01a*, P01, P02, P03* | 8 |
| 2 | Tác tử học từ tương tác | "Muốn cải thiện quyết định khi mô hình môi trường không cố định, tác tử phải học từ hậu quả của hành động." (23) | Tác tử · Môi trường · Trạng thái và quan sát · Mô hình cố định · Thao tác robot | `AT` | `mach-2` | A00–A04, B01–B02 | 20 |
| 3 | Tín hiệu học và dữ liệu tương tác | "Muốn nhận dạng một bài toán Học tăng cường, phải so tín hiệu học với học có giám sát và không giám sát." (23) | Học có giám sát · Học không giám sát · Phản hồi trễ · Dữ liệu không độc lập | `CT` | `mach-3` | C00–C05 | 15 |
| 4 | Phần thưởng và lợi tức | "Muốn đo hậu quả dài hạn của một hành động, phải cộng các phần thưởng từ sau hành động đến khi kết thúc lượt." (24) | Phần thưởng · Quỹ đạo · Lợi tức · Giả thuyết phần thưởng | `DT` | `mach-4` | D00–D03 | 20 |
| 5 | Chính sách, hàm giá trị và thăm dò | "Muốn chọn hành động cực đại hóa kỳ vọng của lợi tức, phải tách việc chọn hành động khỏi việc đánh giá tình huống." (24) | Chính sách · Hàm giá trị · Mô hình môi trường · Thăm dò · Khai thác | `ET` | `mach-5` | E00–E02, F00–F03 | 27 |
| 6 | Tic-tac-toe như một bài toán Học tăng cường | "Muốn kiểm chứng khung tác tử trên một trò chơi, phải xác định trạng thái, hành động hợp lệ, phần thưởng và giá trị." (24) | Cây trò chơi · Tập hành động hợp lệ · Đối thủ chọn đều · Nước khai thác một bước | `GT` | `mach-6` | G00–G04 | 18 |
| 7 | Tổng kết và chuyển tiếp | "Muốn dùng khung của bài cho bài toán mới, phải giữ đủ giả thiết của từng khái niệm và kết quả." (21) | Giả thiết không được bỏ · Câu hỏi tự kiểm tra · Tài liệu đọc · Bài 02 | `ZT` | `mach-7` | H04–H07, Z00 | 12 |

Mọi `<tiền tố>00` đã tồn tại nên dùng `<tiền tố>T`. A00, C00, D00, E00, G00 giữ làm trang nội dung, đổi tiêu đề (A00 "Vòng tương tác tác tử–môi trường", C00 "Ba nhiệm vụ học", D00 "Ví dụ: một lượt trên dãy bốn ô", E00 "Chọn nước và đánh giá thế cờ", G00 "Ví dụ: một thế cờ Tic-tac-toe", Z01 "Tổng kết").

### A2. Mạch mở đầu và kết luận

Mở đầu: P00 bìa thêm câu luận đề "Tác tử học chính sách từ phần thưởng trễ, trên dữ liệu do chính hành động của nó sinh ra." và "Học tăng cường (reinforcement learning)"; ghi chú nêu phạm vi (không chiết khấu, không giả thiết Markov) và quan hệ với Bài 02. P01a "Tiên quyết và quy ước" (mới): "Nhắc lại:" biến ngẫu nhiên rời rạc, kỳ vọng có điều kiện; học có giám sát với $(x_i,y_i)$ và hàm mất mát; "Ký hiệu:" $t=0,1,\dots$, kết thúc tại $T$; $S_t$, $O_t$, $A_t\in\mathcal A(S_t)$, $R_{t+1}\in\mathbb R$; lịch sử $H_t$; $\mathbb E_\pi$ theo chính sách và môi trường; bài không dùng chiết khấu, không giả thiết Markov. P01 mục tiêu: 5 mục ≤16 âm tiết gắn bài tập: (1) mô hình hóa bằng tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng (01.1, 01.13); (2) phân biệt phần thưởng với nhãn (01.2); (3) tính lợi tức $G_t$ của lượt hữu hạn (01.3); (4) phân biệt chính sách, hàm giá trị, mô hình; nhận diện thăm dò và khai thác (01.5, 01.6); (5) tập hành động hợp lệ và nước khai thác một bước trong Tic-tac-toe (01.7, 01.8). P02 "Nội dung" đánh số 1–7, dòng "Tài liệu đọc trước: Sutton và Barto (2018), Chương 1 và §3.1–3.3". P03 "Vấn đề trung tâm" (mới, ≤60 âm tiết): bài toán "Chọn hành động khi đánh giá chỉ đến sau cả chuỗi hành động."; mạch 2 "Mô hình cố định không đủ: học từ tương tác."; mạch 3 "Tín hiệu là phần thưởng, không là nhãn; mẫu không độc lập."; mạch 4 "Lượt hữu hạn: đo bằng lợi tức $G_t$."; mạch 5 "$\pi$ chọn, $v_\pi$ đánh giá; ước lượng thiếu dữ liệu thì thăm dò."; mạch 6 "Quan sát đầy đủ, đối thủ cố định: chọn theo $R_{t+1}+v_\pi(S_{t+1})$."; dùng lại `agent-environment.svg`.

Kết luận (ZT → Z01 → Z02/Z02b → Z03 → H04 → Z00):

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Vòng tương tác | sau $A_t$ môi trường trả $R_{t+1}$ và $O_{t+1}$ | $S_t\xrightarrow{A_t}(R_{t+1},S_{t+1})$ |
| Trạng thái và quan sát | quan sát có thể thiếu thông tin | dùng lịch sử $H_t$ khi $O_t\neq S_t$ |
| Lợi tức | lượt hữu hạn, kết thúc tại $T$, không chiết khấu | $G_t=\sum_{k=t+1}^T R_k$, $G_t=R_{t+1}+G_{t+1}$, $G_T=0$ |
| Giả thuyết phần thưởng | mục tiêu mã hóa được bằng một số cộng dồn | $\max_\pi \mathbb E_\pi[G_0]$ |
| Hàm giá trị | $\pi$ cố định; kỳ vọng theo $\pi$ và môi trường | $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$ |
| Thăm dò–khai thác | ước lượng từ ít mẫu còn bất định | khai thác: $\arg\max_a \bar r(a)$; thăm dò: $\pi(a)>0$ |
| Nước khai thác một bước | quan sát đầy đủ; đối thủ cố định; giá trị kết thúc bằng 0 | $\arg\max_{a\in\mathcal A(s)}\mathbb E[R_{t+1}+v_\pi(S_{t+1})\mid s,a]$, chưa chắc tối ưu |

Z02/Z02b "Bài tập: robot dọn dãy bốn ô, tổng hợp" (= 01.13): 4 ô; robot ở ô 1; rác ở ô 4; hành động {trái, phải, hút}; $+1$ khi hút ở ô 4 và lượt kết thúc; cắt sau 5 bước; (a) $S_0$, $O_0$; (b) $G_0$ của quỹ đạo phải, phải, phải, hút; (c) $v_\pi$ của chính sách "sang phải, hút khi thấy bẩn"; (d) nước khai thác ở ô 3 với giá trị cho trước. Z03 kết luận có điều kiện kèm "Nguồn: Sutton và Barto (2018), Chương 1, §3.1–3.3; Silver (2015), Bài 1." H04 "Câu hỏi tự kiểm tra" với bốn câu (cảm biến chỉ đọc ô hiện tại; $G_4$ với $T=4$, $R=(0,0,0,1)$; nước tham lam theo $v_\pi$ của chính sách chọn đều; không có mô hình thì có còn là tác tử Học tăng cường). Z00 "Bài tập về nhà và tài liệu đọc": bảng `Mạch | Bài tập`, "Tài liệu đọc: Sutton và Barto (2018), Chương 1 (tr. 1–13), §3.1–3.3 (tr. 47–57); Silver (2015), Bài 1; Silver và cộng sự (2016)", liên kết viewer, dòng nối sang Bài 02.

### A3. Bảng từng trang

| Mã | Âm tiết | Vấn đề | Quyết định | Đề xuất |
|---|---:|---|---|---|
| P00 | 25 | Thiếu câu luận đề; thiếu "(reinforcement learning)"; ghi chú có lời quy trình | sửa | A2 |
| P01a | — | Thiếu | thêm | A2 |
| P01 | 80 | Chạm trần; dòng 26; mục tiêu chưa gắn sản phẩm; ghi chú nhắc "trắc nghiệm" | sửa | 5 mục tiêu; dòng tiên quyết sang P01a |
| P02 | 63 | Vượt 60; 8 dòng; >1 khung; nhãn "Trọng tâm:"; lời chỉ đường; chưa đánh số | sửa | "Nội dung" |
| P03 | — | Thiếu | thêm | A2 |
| AT | — | Thiếu trang tiêu đề mạch | thêm | A1 |
| A00 | 16 | "A." và `h1`; ghi chú kể chức năng trang | sửa | "Vòng tương tác tác tử–môi trường"; "Nhu cầu:" và ví dụ robot dọn dãy bốn ô có số; giữ hình |
| A01 | 57 | Trên 40; dòng 27; >1 khung; thiếu tiếng Anh; chưa đưa $S_t$, $O_t$ | sửa | "Định nghĩa." tác tử (agent), môi trường (environment); trạng thái (state), quan sát (observation) với $S_t$, $O_t$; một khung |
| A02 | 43 | Nhãn "Ghi nhớ:/Thích nghi:/Khái quát:"; ghi chú "Đáp án:" | sửa | Ba dòng "… là …"; "Lời giải:" |
| A03 | 33 | Đạt | giữ | "điều khiển (control)" |
| A04 | 53 | Dòng 26; hộp chỉ đường; >1 khung; ghi chú "phần E" | sửa | Bỏ hộp; một câu kết luận có điều kiện |
| B00 | 34 | Nhãn "B."; dòng 34; lời chỉ đường; ghi chú tự mâu thuẫn | bỏ | Lời dẫn vào ghi chú B01 |
| B01 | 53 | Thiếu "Ví dụ:"; dòng 26; hộp chỉ đường; >1 khung | sửa | "Ví dụ: AlphaGo trong cờ vây"; "tìm kiếm cây (tree search)" |
| B02 | 33 | Thiếu "Ví dụ:"; dòng 21; "Tiếp theo:"; ghi chú "Đáp án" | sửa | "Ví dụ: thao tác robot"; bỏ "Tiếp theo" |
| A05, A06 | — | Cụm thiếu bài có "Lời giải:" | thêm | "Bài tập: trạng thái và quan sát của robot dọn dãy bốn ô" (= 01.1) + trang lời giải |
| CT | — | Thiếu | thêm | A1 |
| C00 | 29 | Nhãn "C."; dòng 29; câu chỉ đường; ghi chú "Trang này…" | sửa | "Ba nhiệm vụ học": "Nhu cầu:" và ba ví dụ dẫn nhập có số; `rl-fields.svg` sang ghi chú §2 |
| C01 | 59 | Sát trần; dòng 23; định nghĩa không dùng "là"; "i.i.d." thiếu dạng đầy đủ; ghi chú có mã | sửa | "Học tăng cường là …"; ba đặc điểm ≤14 âm tiết; i.i.d. viết đầy đủ |
| C02 | 0 | Chỉ hình; ghi chú 29 âm tiết | giữ | Thêm chú thích kết luận; ghi chú "phần thưởng không phải nhãn" |
| C03 | 40 | Chuỗi mũi tên; ghi chú "Đáp án" | sửa | $\{(x_i,y_i)\}$ và $\ell(f(x_i),y_i)$; "supervised learning" |
| C04 | 34 | Dòng 21; nhãn "Ví dụ nhiệm vụ:" | sửa | "unsupervised learning"; "Ví dụ." |
| C05, C06 | 49 | Dòng 25; 2 khung; không lời giải | sửa, thêm | "Bài tập: nhận dạng tín hiệu học" với 4 mẫu (= 01.2) + trang lời giải |
| DT | — | Thiếu | thêm | A1 |
| D00 | 9 | Nhãn "D." và `h1`; $T$ chưa định nghĩa | sửa | "Ví dụ: một lượt trên dãy bốn ô": phải, phải, phải, hút; $R_4=+1$, $T=4$; "quỹ đạo (trajectory)", "lượt (episode)" |
| D01 | 32 | $T$ trước định nghĩa; không dùng "là"; 2 thẻ | sửa | "Định nghĩa. Phần thưởng (reward) $R_{t+1}$ là …"; định nghĩa $T$ |
| D02 | 38 | Dòng 24; $T$ sau công thức; tên "phần thưởng tích lũy" | sửa | "Lợi tức": "Định nghĩa. Lợi tức (return) là …" |
| D02b | — | Hệ thức đệ quy chỉ trong ghi chú | thêm | "Mệnh đề." $G_t=R_{t+1}+G_{t+1}$, $G_T=0$; "Chứng minh." một dòng; kiểm $G_2=0+1$ (Mệnh đề 01.11) |
| D03 | 76 | Vượt 60; dòng 25; >1 khung; thiếu "(reward hypothesis)"; ghi chú điều phối | tách | D03 phát biểu, "Ý nghĩa:", "Lưu ý:" giả thuyết không phải định lý |
| D03b | — | — | thêm | "Ví dụ: phần thưởng bỏ sót mục tiêu" (đổ bình hoa vẫn $G_0=1$) với "Câu hỏi:" |
| D04, D05 | — | Thiếu bài có lời giải | thêm | "Bài tập: lợi tức trên dãy bốn ô" (va ghế $-1$): $G_0,G_1,G_3$ và kiểm hệ thức (= 01.3) |
| ET | — | Thiếu | thêm | A1 |
| E00 | 22 | Nhãn "E."; dòng 22; hình trước vấn đề; ghi chú "bản chuyển đổi" | sửa | "Chọn nước và đánh giá thế cờ": "Nhu cầu:"; `rl-components.svg` xuống E02 |
| E00b | — | Thiếu ví dụ trước định nghĩa | thêm | "Ví dụ: giá trị của thế cờ hai ô trống": X chọn đều, đối thủ chọn đều; giá trị kết thúc 0 |
| E01 | 32 | Hai định nghĩa; "=" thay "là"; $H_t$ trước định nghĩa | tách | E01 "Chính sách": chính sách (policy) là phân phối $\pi(\cdot\mid h)$ |
| E01b | — | — | thêm | "Hàm giá trị": $v_\pi(h)=\mathbb E_\pi[G_t\mid H_t=h]$; "Ý nghĩa:" |
| E02 | 62 | Vượt 60; $\widehat O$ chưa định nghĩa; nhãn ngoài danh sách; thiếu (model-based)/(model-free); ghi chú "Đáp án", "Trang này" | sửa | ≤40 âm tiết; "Định nghĩa. Mô hình (model) là …"; ví dụ mô hình của robot |
| E03, E04 | — | Thiếu bài có lời giải | thêm | "Bài tập: giá trị của robot dưới chính sách ngẫu nhiên" ($v_\pi(h_0)=1/16$; = 01.5) |
| F00 | 17 | Nhãn "F."; "Vấn đề:"; ví dụ sau định nghĩa | sửa | "Chọn chế độ hút khi thiếu dữ liệu": "Nhu cầu:" và bảng A (20 lần; 0,60), B (2 lần; 0,55) |
| F01, F02 | 32, 32 | Nhãn "Chi phí:", "Rủi ro:"; thiếu (exploration)/(exploitation) | gộp | "Thăm dò và khai thác", hai định nghĩa song song, "Lưu ý:", ≤40 |
| F03, F04 | 46 | Nhãn "Ví dụ giả định:"; không lời giải | sửa, thêm | "Bài tập: chọn chế độ hút" (= 01.6) + trang lời giải |
| GT | — | Thiếu | thêm | A1 |
| G00 | 45 | Nhãn "G."; dòng 45; tài liệu làm chủ ngữ; "Bài toán:"; chưa nói O đi trước | sửa | "Ví dụ: một thế cờ Tic-tac-toe": dữ kiện, "Giả thiết:" đối thủ chọn đều; O đi trước hoặc sửa hình |
| G01 | 28 | Hình chỉ 3/4 nhánh; ghi chú kể nguồn | sửa | Thêm nhánh $a=6$; "cây trò chơi (game tree)"; ghi chú nêu số nút |
| G02 | 41 | 3 thẻ; chưa nêu $t$ là lượt của X; ghi chú có mã | sửa | "Lưu ý: bước $t$ là lượt của X; nước của đối thủ thuộc môi trường" |
| G03 | 13 | Công thức trước ví dụ; thiếu $a=6$; afterstate gọi là $S_{t+1}$; ghi chú mở "Ghi chú:" | sửa | "Ví dụ: chọn nước trên thế cờ bốn ô trống": bảng $a \mid R_{t+1}\mid v_\pi(S_{t+1})\mid$ tổng |
| G03b | — | — | thêm | "Nước khai thác một bước": công thức, "Ý nghĩa:", "Lưu ý:" chưa chắc tối ưu; dẫn Mệnh đề 01.11 |
| G04, G05 | 52 | Dòng 26; "Đáp án"; thiếu "Bài tập:" | sửa, thêm | "Bài tập: biểu diễn thế cờ có ô 2, 6, 8 trống" (a)(b)(c) (= 01.7) + lời giải |
| ZT | — | Thiếu | thêm | A1 |
| Z01, Z02, Z02b, Z03 | — | Thiếu | thêm | A2 |
| H04 | 63 | Vượt; dòng điều phối; câu hỏi không nhãn; ghi chú "Đáp án", mã | sửa | "Câu hỏi tự kiểm tra" |
| H05 | 43 | Câu hỏi không nhãn; trùng H04 | gộp | Ý vào H04; robot dọn nhà thành Bài tập 01.14 |
| H06, H07 | 73, 60 | Vượt; dòng điều phối; "AGI", "foundation agent" chưa giải thích | bỏ | Thành Bài tập 01.16 [Tìm hiểu] (quyết định điều phối viên) |
| Z00 | 82 | Vượt 80; nhãn "Ba dấu hiệu:", "Tự kiểm tra:"; ghi chú chứa URL | sửa | "Bài tập về nhà và tài liệu đọc" |
| H00–H03 | — | Phụ lục thông tin tổ chức chưa xác nhận; "Phụ lục:" không thuộc danh sách; H03 chỉ dẫn giảng viên | bỏ | Ghi lý do trong review-log (quyết định điều phối viên) |

Chung: bỏ `<style>` thu nhỏ chữ; thay lớp cục bộ bằng lớp chung (`question-box`, `outline-card`, `outline-grid-2/3`, `caption`); thêm thuật ngữ gốc ở lần đầu cho tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng, quỹ đạo, lượt, lợi tức, chính sách, hàm giá trị, mô hình, có mô hình, phi mô hình, thăm dò, khai thác, học có giám sát, học không giám sát, giả thuyết phần thưởng, cây trò chơi, lập kế hoạch (planning). Ghi chú cần sửa: "Đáp án" (A02, B02, C03, E02, G04, H04, H05); mã hoặc chữ cái phần (A04, B00, B01, B02, C01, E02, G02, H04); kể về tài liệu (B00, B01, C00, E00, G01, G02, H06); lời điều phối (D03, H03, Z00); dưới 40 âm tiết (C02, F01, G01).

### A4. Cụm khái niệm (vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra)

| Cụm | Đề xuất |
|---|---|
| Tác tử, môi trường, trạng thái và quan sát | A00 (vấn đề + ví dụ dẫn nhập số) → hình A00 → A01 → B01–B02 → A05–A06 |
| Nhu cầu học, mô hình cố định (phụ) | Chu trình rút gọn, ghi lý do: nguồn chỉ đối chiếu, không có định nghĩa |
| Ba dạng tín hiệu học | C00 (3 ví dụ dẫn nhập) → C01–C02 → C03–C04 → C05 → C05–C06 |
| Phần thưởng và lợi tức | DT + D00 → D00 → D01, D02, D02b → D03, D03b → D04–D05 |
| Chính sách và hàm giá trị | E00 → E00 → E00b → E01, E01b → G03, G03b → E03–E04 |
| Mô hình môi trường (phụ) | Một dòng ví dụ mô hình của robot ở E02; chu trình rút gọn có lý do |
| Thăm dò và khai thác | F00 (vấn đề + bảng) → hình F00 → F01 gộp → "Lưu ý:" về Tic-tac-toe → F03–F04 |
| Tic-tac-toe và nước khai thác một bước | G00 → G01 → G02 → G03 (ví dụ) → G03b → Z02 → G04–G05 |

### A5. Ví dụ xuyên suốt

Hai ví dụ: (1) "Robot dọn dãy bốn ô" (gộp robot dọn nhà, robot chọn đường, quỹ đạo $S_0$–$S_4$ với $R_4=+1$, $T=4$, bảng hai chế độ hút), dùng ở A05, C05, D00–D05, E03, F00, F03, Z02, mỗi lần một câu hỏi mới; (2) "Thế cờ Tic-tac-toe bốn ô trống" (và thế cờ hai ô trống suy ra), dùng ở E00, E00b, G00–G05. Dữ kiện robot là số liệu sư phạm tự xây dựng. Bài không có bài thực hành.

## B. Ghi chú bài giảng

### B1. Đối chiếu từng mục (TP1–TP11 là 11 thành phần của chương)

| Dòng | Mục hiện có | Mạch | TP | Hành động |
|---|---|---|---|---|
| 1 | `# Bài 01 — Giới thiệu Học tăng cường` | — | 1 | Đạt |
| 3 | `## Mục tiêu và kiến thức tiên quyết` | 1 | 3, 4 | Tách hai mục; L12 chứa lời quy trình: xóa |
| 14 | `## Bản đồ chủ đề` | — | 6 | Đặt sau Bảng ký hiệu; mỗi chủ đề thêm "Mục: `## N.`" |
| 16–56 | sáu chủ đề cốt lõi | 2–6 | 6 | topic-01 → §1, 02 → §2, 03 → §3, 04 và 05 → §4, 06 → §5 |
| 64 | `### Cầu nối: từ lịch sử… đến trạng thái…` | 5–6 | 6 | Đổi "Lịch sử và thế cờ trong Tic-tac-toe" |
| 71, 77, 83 | `### Bổ sung: …` | 2, 4 | 6 | Ghi mục §1.3, §1.4, §3.4 |
| 89 | `### Đọc thêm` | — | 6 | Giữ; AGI và foundation agent có tên tiếng Việt |
| 96 | `## Ký hiệu và quy ước` | — | 5 | Bảng 3 cột ~20 dòng (B6) |
| 110 | `## Tác tử học từ tương tác` | 2 | 7 (§1) | `## 1.`; mở bằng bài toán robot có số; nhãn in đậm thay bằng `###` và khối; thêm kết mục |
| 129 | `### Bổ sung: AlphaGo và thao tác robot` | 2 | §1.4 | Đặt sau L134; Ví dụ 01.2, 01.3 |
| 134 | `### Bổ sung: giới hạn mô hình điều khiển cố định` | 2 | §1.3 | Nhận xét 01.5; ba vấn đề thành danh sách |
| 139 | `## Khung Học tăng cường và ba dạng tín hiệu` | 3 | §2 | `## 2. Tín hiệu học và dữ liệu tương tác`; tách định nghĩa L143 khỏi trực giác |
| 164 | `## Phần thưởng và kết quả dài hạn` | 4 | §3 | `## 3. Phần thưởng và lợi tức`; thêm Mệnh đề 01.11 và chứng minh |
| 191 | `### Bổ sung: giả thuyết phần thưởng` | 4 | §3.4 | Nhận xét 01.12 và Ví dụ 01.7 |
| 196 | `## Chính sách, hàm giá trị và mô hình tùy chọn` | 5 | §4.1–4.3 | Gộp với L226 thành `## 4.`; sửa L202 |
| 221 | `### Cầu nối: từ $V^\pi(h_t)$ đến $V^\pi(S_t)$` | 6 | §5.2 | Nhận xét 01.21 với đủ giả thiết |
| 226 | `## Thăm dò và khai thác` | 5 | §4.4 | Hạ thành `###` trong §4 |
| 252 | `## Mô hình hóa Tic-tac-toe` | 6 | §5 | `## 5.`; sửa $\{3,7,9\}$ thành $\{3,6,7,9\}$; L266 thành Mệnh đề 01.22 có chứng minh |
| — | thiếu | — | 8, 9 | Thêm Tình huống áp dụng; Tóm tắt chương |
| 280 | `## Nội dung tự học` | 7 | 11 | Gộp vào Hướng dẫn đọc thêm |
| 287 | `## Bài kiểm tra` | 7 | 10 | `## Bài tập củng cố` ba mức với `exercise`, `hint`, `solution` |
| 300 | `## Thảo luận mở rộng (không kết luận)` | 7 | 8/11 | Thành Bài tập 01.16 [Tìm hiểu] và "Ứng dụng" |
| 305 | `## Tài liệu tham khảo` | — | 11 | Đổi tên; nêu mục nào dựa trên nguồn nào |

### B2. Đánh số

§1: Ví dụ 01.1 (robot dọn dãy bốn ô: một lượt) · Định nghĩa 01.1 (tác tử, môi trường, vòng tương tác) · Định nghĩa 01.2 (trạng thái, quan sát, lịch sử $H_t$) · Nhận xét 01.3 (trạng thái khác quan sát) · Nhận xét 01.4 (ghi nhớ, thích nghi, khái quát) · Nhận xét 01.5 (giới hạn mô hình cố định) · Ví dụ 01.2 (AlphaGo) · Ví dụ 01.3 (thao tác robot) · Bài tập 01.1.
§2: Ví dụ 01.4 (đổi thứ tự mẫu) · Định nghĩa 01.6 (ba dạng tín hiệu học) · Nhận xét 01.7 (bốn khác biệt) · Nhận xét 01.8 (dữ liệu không i.i.d.) · Bài tập 01.2.
§3: Ví dụ 01.5 (một lượt trên dãy bốn ô) · Định nghĩa 01.9 (phần thưởng, lượt, $T$) · Định nghĩa 01.10 (lợi tức) · Mệnh đề 01.11 (hệ thức đệ quy) + `proof` · Ví dụ 01.6 (kiểm hệ thức) · Nhận xét 01.12 (giả thuyết phần thưởng) · Ví dụ 01.7 (phần thưởng bỏ sót mục tiêu) · Bài tập 01.3, 01.4.
§4: Ví dụ 01.8 (hai việc trên một thế cờ) · Định nghĩa 01.13 (chính sách) · Ví dụ 01.9 (giá trị thế cờ hai ô trống) · Định nghĩa 01.14 (hàm giá trị) · Nhận xét 01.15 · Định nghĩa 01.16 (mô hình; có/phi mô hình) · Nhận xét 01.17 · Ví dụ 01.10 (hai chế độ hút) · Định nghĩa 01.18 (thăm dò, khai thác, tham lam theo ước lượng) · Nhận xét 01.19 · Bài tập 01.5, 01.6.
§5: Ví dụ 01.11 (thế cờ bốn ô trống) · Định nghĩa 01.20 (mô hình hóa Tic-tac-toe) · Nhận xét 01.21 (rút gọn lịch sử thành thế cờ) · Ví dụ 01.12 (chọn nước tính tay) · Mệnh đề 01.22 (phân tích một bước) + `proof` · Định nghĩa 01.23 (nước khai thác một bước) · Nhận xét 01.24 · Bài tập 01.7, 01.8.
Cuối chương: Tình huống 01.1, 01.2 · Bài tập củng cố 01.9–01.12 · chỉ trong `exercises.md`: 01.13–01.16. Không có `algorithm` (nguồn không có thuật toán; ghi lý do trong storyboard và review-log).

### B3. Tiêu chuẩn thứ nhất và trình bày sáng sủa

Giọng kể hiện khách quan; tài liệu làm chủ ngữ ở L12, L101, L107, L118, L241, L270 ("Bài này…"), L193, L272 ("bản note…"), L120, L180 ("nguồn…"). Chuyển sang "chúng ta/ta"; lời quy trình chuyển vào review-log.

| Tiêu chí | Vi phạm | Cách sửa |
|---|---|---|
| Vấn đề đi trước công cụ | L141, L198, L166 | Mở mỗi `##` bằng bài toán robot hoặc thế cờ có số |
| Công thức bao bởi lời | L176–178, L268, L207 | Câu dẫn và câu đọc |
| Ký hiệu gọi tên lần đầu | $O_t$ chưa định nghĩa (L208 dùng $\widehat O_{t+1}$); L102 thiếu thành phần $H_t$; L98 không nói $T$ ngẫu nhiên | Định nghĩa 01.2; nêu miền tại chỗ |
| Bước suy diễn có lý do | L266 thiếu tuyến tính, tính chất tháp, độc lập có điều kiện; L223 chưa nói $\pi$ chỉ phụ thuộc thế cờ | Mệnh đề 01.22 chứng minh theo bước |
| Bản đọc và phản ví dụ | L178, L207, L193 | Danh sách "Bỏ <giả thiết>: <phản ví dụ>" |
| Ví dụ trước phát biểu | L116, L145, L202 | Ví dụ 01.1, 01.4, 01.9 có số |
| Nối mục bằng kết quả | Không có kết mục (L126, 161, 188, 218, 249, 278 kết bằng `solution`) | Thêm đoạn văn xuôi |
| Không tham chiếu ra ngoài | L272, L112, L120, L131 | Số hiệu; bỏ lời quy trình |
| Tự chứa | L157, L245 | Chép lại dữ kiện |
| Câu đủ thành phần | L98–107, L149–151, L289–294 | Viết lại |
| Nhầm lẫn thường gặp | Thiếu: phần thưởng với giá trị; chỉ số $R_{t+1}$; giá trị kết thúc; lượt so với $t$ | Nhận xét 01.3, 01.15, 01.21 |
| Hình được đọc | Không có hình | Đưa `agent-environment`, `delayed-reward`, `learning-signals`, `tictactoe-board`, `tictactoe-value` kèm đoạn đọc |
| Một ý một đoạn | L114, L136, L143 | Tách |
| Chứng minh theo bước | Chưa có | Mệnh đề 01.11, 01.22 |
| Trường hợp thành danh sách | L136, L153 | Danh sách |
| Công thức trên dòng riêng | L174, L202, L266 | `$$…\tag{3.1}$$` |
| Ví dụ, lời giải theo giai đoạn | Lời giải một dòng "Trả lời:" | Nhãn Lập mô hình / Tính / Diễn giải / Kiểm tra lại |
| Ngoặc lồng | L118, L155 | Tách câu |

### B4. Phần cần thêm

Móc nối sau Định nghĩa 01.2, 01.10, 01.14, 01.16, 01.18; mở chương từ học có giám sát (nhãn, mất mát) và giới hạn; kết chương sang Bài 02 (Markov, chiết khấu, mở rộng trạng thái) và Bài 03 (MDP và Bellman tổng quát hóa Mệnh đề 01.22). "Trong thực hành": Mệnh đề 01.11 (tính $G_t$ ngược, $O(T)$, Monte Carlo Bài 05); Định nghĩa 01.14 (bảng ở Bài 05, mạng ở Bài 08); Định nghĩa 01.16 (bộ mô phỏng hoặc mô hình học được; sai số tích lũy); Định nghĩa 01.18 ($\varepsilon$-tham lam Bài 06); Định nghĩa 01.23 (Sutton–Barto §1.5, trạng thái sau nước đi). Tình huống 01.1 (robot dọn dãy bốn ô: mô hình hóa đầy đủ, lượt cắt sau 6 bước, trạng thái gồm vị trí và tình trạng ô 4, so $v_\pi$ của "luôn sang phải rồi hút" bằng 1 với chính sách chọn đều); Tình huống 01.2 (robot chỉ cảm nhận ô hiện tại: hai lịch sử cùng $O_t$ nhưng giá trị khác; dẫn Bài 02). Ứng dụng: Bài 02–06, 08–10. Tóm tắt chương theo cấu trúc mới; giả thiết hay bỏ quên: giá trị kết thúc bằng 0, $\pi$ cố định, quan sát đầy đủ, lượt hữu hạn. Bài tập củng cố: 01.9 (chính sách, giá trị, mô hình trong AlphaGo), 01.10 (lợi tức ván thua $R=(0,0,0,-1)$), 01.11 (chứng minh $v_\pi(h)$ bằng lợi tức quỹ đạo duy nhất khi tất định), 01.12 (robot xoay khối, chọn có/phi mô hình). Độ dài đích 12 000–14 000 từ (phần đầu 900; §1 2 200; §2 1 500; §3 2 000; §4 2 800; §5 2 000; tình huống 1 000; tóm tắt 500; củng cố 1 200).

### B5. Giáo trình

§1: Sutton–Barto §1.1 (tr. 1), §1.2 (tr. 4), §3.1 (tr. 47), §17.3 (tr. 464); Silver (2015) Bài 1; Silver và cộng sự (2016); Bertsekas (2019) Chương 1; SML `sec_mdp_introduction.tex` (giáo trình dùng "tác nhân", học phần dùng "tác tử"). §2: Sutton–Barto §1.1; Goodfellow và cộng sự (2016) §5.1.3; Silver (2015) Bài 1. §3: Sutton–Barto §3.2 (tr. 53), §3.3 (tr. 54), §3.4 (tr. 57), §17.4 (tr. 469); Puterman §2.1; SML "Giá trị của quỹ đạo". §4: Sutton–Barto §1.3 (tr. 6), §3.5 (tr. 58), §2.1–2.2 (tr. 25–27), §8.1 (tr. 159); Szepesvári §4.2.1. §5: Sutton–Barto §1.5 (tr. 8–13), §6.8 (tr. 136). Tình huống: Sutton–Barto §1.2; SML `sec_rl_applications.tex`.

### B6. Bảng ký hiệu và chỗ lệch

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$ | bước quyết định | $\{0,1,\dots\}$ |
| $T$ | thời điểm kết thúc lượt | nguyên dương, có thể ngẫu nhiên |
| $\mathcal S$, $S_t$ | tập trạng thái; trạng thái | hữu hạn; biến ngẫu nhiên |
| $\mathcal O$, $O_t$ | tập quan sát; quan sát | — |
| $\mathcal A(s)$, $A_t$ | hành động hợp lệ; hành động | hữu hạn; $A_t\in\mathcal A(S_t)$ |
| $R_{t+1}$ | phần thưởng sau $A_t$ | $\mathbb R$ |
| $H_t$, $h$ | lịch sử và một giá trị | $(O_0,A_0,R_1,\dots,R_t,O_t)$ |
| $G_t$ | lợi tức | thực; $G_T=0$ |
| $\pi(a\mid h)$ | chính sách | phân phối trên $\mathcal A$ |
| $\mathbb E_\pi$ | kỳ vọng theo $\pi$ và môi trường | — |
| $v_\pi(h)$, $v_\pi(s)$ | hàm giá trị | $\mathbb R$; tương ứng $V^\pi$ của SML |
| $\widehat S_{t+1}$, $\widehat O_{t+1}$, $\widehat R_{t+1}$ | dự báo của mô hình | cùng miền |
| $N(a)$, $\bar r(a)$ | số lần thử; trung bình mẫu | $\mathbb N$; $\mathbb R$ |
| $a^*$ | nước khai thác một bước | $\mathcal A(s)$ |
| $(x_i,y_i)$, $\ell$ | mẫu có nhãn; mất mát | — |
| $\gamma$ | không dùng ($\gamma=1$) | đưa vào ở Bài 02 |

Chỗ lệch: $V^\pi$ (deck E01, G03; ghi chú L104) so với $v_\pi$; "phần thưởng tích lũy" so với "lợi tức"; $O_t$ chưa định nghĩa; $T$ dùng ở D01 trước D02; thành phần $H_t$; tập hợp lệ 4 so với 3; giá trị sau nước thắng; "phòng ba ô" (L116) so với dãy 4 bước (D00); chỉ số bước Tic-tac-toe và afterstate; rút gọn lịch sử thiếu giả thiết; mục tiêu 4 lệch; tiên quyết "đại số tuyến tính" không dùng, H03 liệt kê Python.

## C. Bài tập (`exercises.md`)

`hw01` không có trong `resources/`; mọi bài tự xây dựng. 01.1–01.8 giữ số hiệu và lời giải của ghi chú; 01.9–01.12 không chép lại; 01.13–01.16 chỉ trong tệp này.

| Số hiệu | Mạch | Mức | Dữ kiện | Trùng hay mới | Năng lực |
|---|---|---|---|---|---|
| 01.1 | 2 | nhận biết | Robot dãy bốn ô, cảm biến bẩn/sạch ô hiện tại; $S_0$, $O_0$, $\mathcal A$, $R_1$ | A05–A06 | trạng thái và quan sát |
| 01.2 | 3 | nhận biết | 4 mẫu $(O_t,A_t,R_{t+1})$; vì sao không đổi thứ tự; dấu hiệu Học tăng cường | C05–C06 | tín hiệu học |
| 01.3 | 4 | tính toán | $(0,-1,0,+1)$: $G_0,G_1,G_3$; kiểm hệ thức | D04–D05 | lợi tức |
| 01.4 | 4 | chứng minh | $G_0=\sum_{k=1}^{t}R_k+G_t$; tính ngược $O(T)$ | mới | chỉ số |
| 01.5 | 5 | tính toán | "phải" hoặc "hút" xác suất 1/2, cắt sau 4 bước; $v_\pi(h_0)=1/16$ | E03–E04 | giá trị theo định nghĩa |
| 01.6 | 5 | nhận biết, tính | A (20 lần; 0,60), B (2 lần; 0,55) | F03–F04 | thăm dò và khai thác |
| 01.7 | 6 | nhận biết | Thế cờ ô 2, 6, 8 trống; X chọn ô 5 | G04–G05 | mô hình hóa |
| 01.8 | 6 | tính toán | Thế cờ bốn ô trống với giá trị cho sẵn; $\arg\max$ | mới, cùng khuôn G03 | nước khai thác |
| 01.13 | 7 | vận dụng | Robot dãy bốn ô (a)–(d) | Z02–Z02b | tổng hợp |
| 01.14 | 4 | vận dụng | Hai thiết kế phần thưởng robot dọn nhà (phạt đổ đồ); $G$ trên hai quỹ đạo | mới (nguồn tr. 24–25) | thiết kế phần thưởng |
| 01.15 | 3, 5 | vận dụng | Đăng ký môn học hoặc xe tự hành (nguồn tr. 8): S, O, A, R, phản hồi trễ, có/phi mô hình | mới | mô hình hóa |
| 01.16 | 7 | [Tìm hiểu] | Tác tử nhiều nhiệm vụ và mô hình thế giới (nguồn tr. 14–15, 43–44) | gộp H06–H07 | lập luận có giới hạn |

## D. Rủi ro và thứ tự

Thứ tự: outline (bảng Việt–Anh, sườn lý thuyết, 7 mạch, mã mới) → ghi chú (soạn, rà toán tính lại Ví dụ 01.9, 01.12, Bài tập 01.5 = 1/16, Mệnh đề 01.22; rà mạch; viewer; commit) → deck (tiêu đề mạch, mở đầu, kết luận, A3, dọn CSS, storyboard, năm rà soát, trực quan hai khung) → `exercises.md` (khớp A06, C06, D05, E04, F04, G05, Z02b; bảng Z00; index). Rủi ro: trùng Bài 02 (giữ Bài 01 ở mức nhập môn, dẫn sang Bài 02 cho Markov và $\gamma$); bỏ CSS thu nhỏ có thể tràn, phải giảm mật độ trước; số trang tăng từ 38 lên khoảng 58; phần Tic-tac-toe cần rà toán tính lại; giá trị trên lịch sử đòi hỏi mô tả môi trường như phân phối có điều kiện cố định. Kiểm thế cờ gốc từ PPTX tr. 28–30 (chỉ đọc).
