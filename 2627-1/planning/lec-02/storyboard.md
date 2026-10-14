# Storyboard Bài 02 — Giao diện tác tử–môi trường

Bản viết lại trong đợt sửa 2026-10-12 (giai đoạn II), khớp deck `2627-1/lecture-02-giao-dien-tac-tu-moi-truong.html`: 7 mạch, 66 trang (bản trước 41 trang; 65 trang trước vòng biên tập sau rà soát), 120 phút. Ghi chú bài giảng đã commit (`39a1bd1`) là nguồn chuẩn: deck tóm tắt ghi chú theo cùng thứ tự khái niệm, cùng số liệu và cùng số hiệu (bộ đếm chung 02.1–02.20, Ví dụ 02.1–02.15, Bài tập 02.1–02.13). Số âm tiết đo bằng `density.py` (đếm cả dấu câu còn lại sau khi bỏ KaTeX, nên cao hơn số âm tiết thật vài đơn vị). Các bản storyboard trước đợt này được thay toàn bộ; lịch sử nằm trong `review-log.md`.

## Bản đồ mạch

| N | Mạch | Loại | Chức năng | Đầu vào | Đầu ra | Đóng góp cho vấn đề trung tâm | Trang tiêu đề mạch | Phút |
|---|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu | mở đầu | Đặt bài toán mê cung, tiên quyết, mục tiêu, nội dung, vấn đề trung tâm | Bài 01: vòng tương tác, lượt, $G_t$ không chiết khấu, chính sách và giá trị trên lịch sử | Nhu cầu đặc tả một bước | Phát biểu vấn đề và năm câu trả lời có điều kiện | `L02-01-01` (bìa) | 9 |
| 2 | Vòng tương tác và tín hiệu thưởng | phát triển kiến thức | Cố định ranh giới và thứ tự tín hiệu; đọc phần thưởng | Ranh giới của Bài 01 | Mẫu chuyển với chỉ số $t+1$; giả thuyết phần thưởng trên mê cung | Dữ liệu của một bước | `L02-02-00` | 16 |
| 3 | Thông tin khả dụng và tính Markov | phát triển kiến thức | Tách $S_t,O_t,X_t$; lịch sử; điều kiện Markov và cách sửa | Mẫu chuyển với quan sát là tọa độ | Biểu diễn $X_t$; tính Markov; lịch sử là trạng thái Markov | Tọa độ là trạng thái Markov; mã bốn ô kề thì không | `L02-03-00` | 27 |
| 4 | Quy tắc chọn hành động | phát triển kiến thức | Viết cách chọn hướng thành phân phối trên biểu diễn | $X_t$ | $\pi(a\mid x)$; xác suất dãy hành động; vai trò của chính sách ngẫu nhiên khi quan sát một phần | Chính sách là phân phối trên bốn hướng | `L02-04-00` | 15 |
| 5 | Lợi tức, hàm giá trị và hàm động lực | phát triển kiến thức | Quy chuỗi phần thưởng về lợi tức, lấy kỳ vọng, tách dự báo một bước | $\pi$, tính Markov | $G_t$, $v_\pi$, $p$, dự đoán và điều khiển | $v_\pi(s)$ đánh giá ô; $p$ dự báo một bước | `L02-05-00` | 27 |
| 6 | Thiết kế phần thưởng | phát triển kiến thức và vận dụng | Dự báo hành vi tối ưu khi đổi phần thưởng | Lợi tức với $\gamma=1$ | Ngưỡng $c^*=(10+c_{\mathrm H})/4$ | Phạt mỗi bước trên $2{,}5$ làm tác tử tối ưu chọn hố | `L02-06-00` | 14 |
| 7 | Tổng kết và chuyển tiếp | kết luận | Kết quả và giả thiết; bài tập tổng hợp; trả lời vấn đề trung tâm; tự kiểm tra; bài tập về nhà | Mọi kết quả của mạch 2–6 | Danh sách giả thiết mang sang Bài 03 | Kết luận có điều kiện | `L02-07-00` | 12 |

Bảy mạch giữ cấu trúc bảy phần của bản trước (kế hoạch A1); số mạch nằm trong khoảng 5–7.

## Cụm khái niệm và sáu bước

| Cụm (mạch) | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Ghi chú |
|---|---|---|---|---|---|---|---|
| Mẫu chuyển (2) | `L02-02-00` (dòng dẫn) | `L02-02-01` | `L02-02-02` | `L02-02-03` | `L02-02-08` | `L02-02-07` | Ví dụ đứng trước định nghĩa; dữ kiện $((0,2),\text{Đông},-1,(1,2))$ chuyển vào công thức |
| Tín hiệu và giả thuyết phần thưởng (2) | `L02-02-04` | `L02-02-04` | `L02-02-05` | `L02-02-05` (nhắc lại) | `L02-02-06` | `L02-07-02` câu 2 | Cụm phụ, chu trình rút gọn: nội dung là Nhắc lại Bài 01 (Định nghĩa 01.5, Nhận xét 01.10) |
| Trạng thái, quan sát, biểu diễn (3) | `L02-03-02` (Nhu cầu + ví dụ dẫn nhập) | `L02-03-11` | `L02-03-02` | `L02-03-12` | `L02-03-06` | `L02-03-08` | Ví dụ dẫn nhập làm cụ thể vấn đề "dữ liệu nào tác tử dùng"; mã $(1,0,1,0)$ truyền sang $X_t=\phi(O_t)$ |
| Lịch sử và quỹ đạo (3) | `L02-03-13` (Nhu cầu) | `L02-03-13` | `L02-03-13` | `L02-03-09` | `L02-03-14` (dùng $H_{17}$) | `L02-03-15` | Cụm phụ; dãy 10 thành phần thành $H_3$ |
| Tính Markov (3) | `L02-03-14` (Nhu cầu) | `L02-03-14` | `L02-03-14` | `L02-03-04` | `L02-03-10` | `L02-03-15`, `L02-03-16` | Hai lịch sử $h,h'$ truyền sang (2.3); cách sửa (ô, $k$) |
| Chính sách (4) | `L02-04-01` (Nhu cầu) | `L02-04-01` | `L02-04-02` | `L02-04-04`, `L02-04-03` | `L02-04-07`, `L02-04-08` | `L02-04-05` | Bảng hai quy tắc truyền sang $\pi(\text{Bắc}\mid(1,2))=0{,}5$ |
| Ưu tiên dừng và chiết khấu (5) | `L02-05-01`, `L02-05-11` (Nhu cầu) | `L02-05-11` (Diễn giải) | `L02-05-11` | `L02-05-10`, `L02-05-12` | `L02-05-15` | `L02-05-09` câu (b) | Trọng số $0{,}5^{i-1}$ truyền sang $\gamma=0{,}5$ |
| Lợi tức (5) | `L02-05-01` | `L02-05-15` (Diễn giải) | `L02-05-15` | `L02-05-03`, `L02-05-16` | `L02-05-16` (ba bước cuối), `L02-06-02` | `L02-05-09` | $-1{,}75$ kiểm bằng hệ thức truy hồi |
| Hàm giá trị (5) | `L02-05-04` (Nhu cầu) | `L02-05-04` | `L02-05-04` | `L02-05-05` | `L02-05-13` | `L02-07-02` câu 3; Bài tập 02.6 | $-4$ truyền sang $v_\pi(s)=-4$ |
| Hàm động lực (5) | `L02-05-08` (Nhu cầu), `L02-05-01` | `L02-05-08` (Ví dụ.) | `L02-05-08` | `L02-05-08` | `L02-05-17` | `L02-05-18` | Ví dụ một bước đứng trước định nghĩa trên cùng trang |
| Thiết kế phần thưởng (6) | `L02-06-01` (Nhu cầu) | `L02-06-04` (đồ thị) | `L02-06-02`, `L02-06-03` | `L02-06-05` | `L02-06-07`, `L02-07-04` | `L02-06-06` | Bảng ba mức $c$ là ba điểm của đồ thị |

Mỗi cụm lớn có một trang "Bài tập: …" với "Lời giải:" trên mặt trang (fragment hoặc trang kế): `L02-02-07`, `L02-03-08`, `L02-03-15`/`03-16`, `L02-04-05`, `L02-05-09`, `L02-05-18`, `L02-06-06`, `L02-07-04`/`07-07`. Không có thuật toán trong bài, nên không có trang tính tay một bước lặp.

## Ngoại lệ mật độ

| Trang | Âm tiết theo `density.py` (trước đợt → hiện tại) | Dòng | Lý do |
|---|---|---|---|
| `L02-01-03` Mục tiêu học tập | 40 → 79 | 5 | Trang mục tiêu, trần 80; năm mục tiêu kèm số hiệu bài tập đo từng mục tiêu. |
| `L02-01-04` Nội dung | 45 → 39 | 7 | Bài có 7 mạch; trang "Nội dung" được phép 7 dòng (quyết định chung §5). |
| `L02-07-06` Kết quả về lợi tức, giá trị và phần thưởng | — → 70 | 6 | Bảng tổng kết, trần 80. |
| `L02-07-05` Trả lời vấn đề trung tâm | — → 77 | 6 | Trang tổng kết viết song song năm dòng với Vấn đề trung tâm, mỗi dòng có điều kiện và số liệu, cộng dòng "Nguồn:"; trần 80. |
| `L02-07-03` Bài tập về nhà và tài liệu đọc | 62 → 70 → 80 | 6 | Trang tổng kết bắt buộc: bảng `Mạch \| Bài tập` (chuyển vị, hai hàng "Tệp bài tập" và "Chỉ trong ghi chú" cho mạch 2–7, theo bảng của `exercises.md`), "Tài liệu đọc:", liên kết "Ghi chú bài giảng · Bài tập", dòng nối Bài 03 có thuật ngữ gốc; trần 80 (đợt 2026-10-14: 70 → 80 theo `density.py`, đếm cả số hiệu bài trong bảng; mỗi dòng ≤ 20). |

`L02-03-16` (lời giải bài kiểm tra tính Markov) có 66 âm tiết ở vòng biên tập trước theo `density.py` (khoảng 57 đếm tay, do dấu câu còn lại sau khi bỏ KaTeX); vòng rà lại 2 rút dòng (b), nay 58.

Trang vượt trần trước đợt sửa và cách xử lý: `L02-03-08` 88 → 55 (tách đề thành bài tập 02.2 có lời giải; câu Markov chuyển sang `L02-03-15`/`03-16` và tự kiểm tra); `L02-05-10` 71 → 42 (tách định nghĩa, định lý `L02-05-12`, ví dụ `L02-05-11`; chứng minh sang ghi chú diễn giả); `L02-06-07` 80 → 59 (một khung, hai dòng có nhãn; pháp lý và đạo đức vào ghi chú diễn giả); `L02-03-11` 63 → 58; `L02-02-05` 58 → 58 (dòng >20 âm tiết tách); `L02-02-01`, `L02-05-04` (dòng >20 âm tiết rút); `L02-05-01` (7 dòng, 3 khung → 5 dòng, 0 khung). Trong vòng biên tập, đề và lời giải của bài kiểm tra tính Markov tách thành `L02-03-15` (đề) và `L02-03-16` (lời giải) vì một trang vượt 60. Không dùng lớp hay CSS thu chữ; deck không có khối `<style>`.

## Thời lượng

Mạch 1: 9 phút; mạch 2: 16; mạch 3: 27; mạch 4: 15; mạch 5: 27; mạch 6: 14; mạch 7: 12. Tổng 120 phút. Thời lượng từng trang ghi trong mục của trang; tổng mỗi mạch khớp bảng trên.

- **Có thể bỏ khi thiếu giờ:** `L02-02-08` (Gymnasium, 2 phút), `L02-04-08` (hai ô cùng mã, 2 phút), `L02-05-17` (1 phút, nội dung có trong ghi chú diễn giả `L02-05-13`), `L02-06-07` (1 phút). Bỏ cả bốn trang tiết kiệm 6 phút, dùng cho `L02-05-18` và `L02-07-04`/`07-07`.
- **Khối 30 phút chữa bài và vận dụng:** Bài tập 02.6 (môi trường hai nhánh, $\gamma=0{,}5$), Bài tập 02.10 (dấu của phần thưởng mỗi bước), Tình huống 02.1 của ghi chú (hành lang pin, $v_\pi((0,5))\approx2{,}840$); nếu thiếu giờ trong phần trình chiếu, `L02-05-18` chuyển sang khối này.

## Vòng biên tập sau năm vai rà soát (2026-10-12)

- **Quan sát và biểu diễn (RL nghiêm trọng 1):** cảm biến trả về bộ mã, $O_t\in\{0,1\}^4$; biểu diễn khác quan sát được minh họa bằng cửa sổ $(O_t,A_{t-1},O_{t-1})$ ở `L02-03-13`, nối sang `L02-04-08`. `L02-03-02`, `03-11`, hình `state-observation-representation.svg` sửa theo.
- **Hai nghĩa của "trạng thái" (RL nghiêm trọng 2):** `L02-03-04` có "Lưu ý:" tính Markov thuộc biến chọn làm trạng thái; ghi chú diễn giả `L02-03-06` nêu cấu hình đầy đủ luôn Markov, MDP và POMDP (bài giảng gốc, trang 18–19).
- **Thứ tự:** `L02-02-07` dời lên ngay sau `L02-02-08` (cụm mẫu chuyển kết bằng bài kiểm tra; cụm tín hiệu thưởng kết mạch 2); `L02-05-09` dời lên ngay sau `L02-05-16`.
- **Ký hiệu:** mức phạt hố đổi $h\to c_{\mathrm H}$ trên deck (chữ $h$ dành cho lịch sử); tọa độ ghi "(cột, hàng)", trạng thái chìa khóa ghi (ô, $k$); tên hướng không đặt trong `\text{}` của KaTeX. Ghi chú bài giảng còn dùng $h$, $(x,y)$, $(x,y,k)$: lệch tạm thời, có đề nghị sửa ghi chú trong review-log.
- **Nguồn trang 10, 20 (ba thành phần của tác tử):** mô hình $\hat p$ của tác tử trở lại mặt trang ở `L02-05-17`.
- **Nguồn trang 27 (câu đố phân loại cờ vua, Dota hoặc CS:GO, robot hút bụi):** không đưa lên deck; để dành cho `exercises.md` (giai đoạn III); nay là Bài tập 02.15.
- **Hình riêng cho trang chiếu:** `aliasing-pair-deck.svg` (bỏ chú giải trong hình, chú giải viết trên mặt trang `L02-04-08`, cỡ nhãn lớn hơn); `aliasing-pair.svg` của ghi chú giữ nguyên chú giải.

## Mạch 1: Mở đầu — 9 phút

Chức năng: phát biểu vấn đề trung tâm trên mê cung $8\times8$, nhắc lại kết quả Bài 01, nêu năm mục tiêu và bảy mạch. Đầu ra: nhu cầu ghi một bước tương tác thành dữ liệu. Cụm mở bài dùng chu trình rút gọn (không có khái niệm mới).

### L02-01-01 — Giao diện tác tử–môi trường (bìa)
- Vị trí: trang tiêu đề của mạch 1. 1 phút. Nguồn: PPTX tr. 1.
- Lý do tồn tại: tên bài, số bài, đơn vị, câu luận đề "Thông tin tác tử có và lợi tức kỳ vọng nó cực đại quyết định hành vi của tác tử."
- Kết nối vào: Bài 01. Kết nối ra: tiên quyết.
- Quyết định: sửa (thêm "Bài 02", tên bài làm `h1`, câu luận đề, đơn vị dạng "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội"; không tên giảng viên). Âm tiết 20 → 43.

### L02-01-06 — Tiên quyết và quy ước
- Vị trí: mạch 1, sau bìa. 2 phút. Nguồn: ghi chú, Kiến thức tiên quyết và Bảng ký hiệu.
- Lý do tồn tại: ba dòng "Nhắc lại:" (vòng tương tác, lượt và $G_t$ không chiết khấu, chính sách và giá trị trên lịch sử) và một dòng "Ký hiệu:" (hướng, tọa độ (cột, hàng)); chỉ số $t$, $\mathcal A$, tọa độ ô, $\mathbb E_\pi$).
- Kết nối vào: bìa. Kết nối ra: mục tiêu dùng các ký hiệu này.
- Mục tiêu hỗ trợ: tất cả. Quyết định: thêm. Âm tiết 60.

### L02-01-03 — Mục tiêu học tập
- Vị trí: mạch 1. 2 phút. Nguồn: ghi chú, Mục tiêu học tập.
- Lý do tồn tại: năm mục tiêu, mỗi mục tiêu kèm bài tập đo nó; khớp ghi chú.
- Quyết định: sửa (ba mục tiêu cũ không đo được → năm mục tiêu). Âm tiết 40 → 79 (ngoại lệ trang mục tiêu).

### L02-01-04 — Nội dung
- Vị trí: mạch 1. 1 phút. Nguồn: bản đồ bảy mạch.
- Lý do tồn tại: `<ol>` bảy mạch, tên trùng trang tiêu đề mạch; đọc trước trong ghi chú diễn giả.
- Quyết định: sửa (tiêu đề "Nội dung", danh sách đánh số, tên mạch mới). 7 dòng (ngoại lệ).

### L02-01-02 — Vấn đề trung tâm
- Vị trí: cuối mạch 1. 3 phút. Nguồn: PPTX tr. 25–26.
- Lý do tồn tại: bài toán một dòng ("Nhu cầu:") và năm câu trả lời có điều kiện đánh số 2–6, cạnh hình mê cung.
- Kết nối vào: nội dung. Kết nối ra: nhu cầu ghi một bước (mạch 2).
- Quyết định: sửa và chuyển vị trí (trước là "Mê cung và chuỗi quyết định", nhãn "Nhiệm vụ:" bị bỏ). Câu hỏi 2–3 của trang `L02-01-05` cũ chuyển vào ghi chú diễn giả. Âm tiết 21 → 60.

### L02-01-05 — (bỏ)
- Quyết định: bỏ (trang câu hỏi ngoài cấu trúc mạch mở đầu, không có lời giải); nội dung vào ghi chú diễn giả của `L02-01-02`.

## Mạch 2: Vòng tương tác và tín hiệu thưởng — 16 phút

Chức năng: cố định ranh giới tác tử–môi trường trên mê cung, ghi một bước thành mẫu chuyển với chỉ số $t+1$, đọc phần thưởng $-1$ qua giả thuyết phần thưởng. Đầu vào: vòng tương tác của Bài 01. Đầu ra: chỉ số thời gian dùng cho lịch sử (mạch 3) và lợi tức (mạch 5).

### L02-02-00 — 2. Vòng tương tác và tín hiệu thưởng (trang tiêu đề mạch)
- Vị trí: điểm vào mạch 2. 1 phút. Bước `vấn đề` của cụm mẫu chuyển (dòng dẫn "Muốn ghi chuỗi quyết định thành dữ liệu, phải cố định thứ tự quan sát, hành động, phần thưởng.", 19 âm tiết).
- Ghi chú diễn giả: kết quả kế thừa (vòng tương tác Bài 01), nhiệm vụ, đầu ra (chỉ số thời gian cho mạch 3 và 5).
- Quyết định: thêm.

### L02-02-01 — Ranh giới tác tử–môi trường
- Vị trí: mạch 2, bước `trực giác` của cụm mẫu chuyển. 2 phút. Nguồn: PPTX tr. 4, 10, 20; Sutton và Barto §3.1.
- Lý do tồn tại: "Nhắc lại:" Định nghĩa 01.1 và hai "Ví dụ." (mê cung, robot), hình vòng tương tác.
- Kết nối vào: dòng dẫn mạch. Kết nối ra: ví dụ một bước.
- Quyết định: sửa (theo ghi chú, tác tử và môi trường là Nhắc lại, không định nghĩa lại; kế hoạch A3 đề xuất "Định nghĩa.", không làm theo vì ghi chú đã chuyển thành Nhắc lại). Âm tiết 38 → 54; dòng 23 → 18.

### L02-02-02 — Ví dụ: một bước Đông từ ô (0,2)
- Vị trí: mạch 2, bước `ví dụ`. 2 phút. Nguồn: PPTX tr. 25–26; ghi chú Ví dụ 02.2.
- Lý do tồn tại: một bước có số trước định nghĩa; khung "Một bước gồm quan sát, hành động, phần thưởng và quan sát mới." (bỏ dấu "=").
- Kết nối vào: ranh giới. Kết nối ra: định nghĩa mẫu chuyển dùng đúng bước này.
- Mục tiêu: 1. Quyết định: sửa. Âm tiết 24 → 46.

### L02-02-03 — Mẫu chuyển
- Vị trí: mạch 2, bước `hình thức`. 2 phút. Nguồn: PPTX tr. 14–15; ghi chú Định nghĩa 02.1.
- Lý do tồn tại: "Định nghĩa." mẫu chuyển (transition) $(O_t,A_t,R_{t+1},O_{t+1})$, ví dụ trong công thức, hình trục thời gian.
- Kết nối ra: ứng dụng trong Gymnasium. Mục tiêu: 1.
- Quyết định: sửa (tên "Thứ tự tương tác" → "Mẫu chuyển" theo ghi chú). Âm tiết 16 → 30.

### L02-02-08 — Mẫu chuyển trong thư viện Gymnasium
- Vị trí: mạch 2, bước `ứng dụng`. 2 phút. Nguồn: ghi chú Mục 1.2, đoạn "Trong thực hành".
- Lý do tồn tại: cụm thiếu ứng dụng (kế hoạch A4); `env.step` sinh một mẫu chuyển; phân biệt kết thúc với cắt lượt, dùng lại ở Bài 05.
- Quyết định: thêm (sai khác so với kế hoạch A3, lấy từ ghi chú). Âm tiết 53.

### L02-02-07 — Bài tập: mẫu chuyển tại ô (6,1)
- Vị trí: cuối mạch 2, bước `kiểm tra`. 3 phút. Nguồn: ghi chú Bài tập 02.1.
- Lý do tồn tại: bài tập có "Lời giải:" fragment; cùng kết quả với Bài tập 02.1 của ghi chú.
- Loại: bài tập có lời giải mẫu. Mục tiêu: 1.
- Quyết định: sửa (trước là "Câu hỏi kiểm tra" từ ô $(1,2)$; đổi sang đề của ghi chú tại $(6,1)$, $t=7$; câu 2–3 cũ chuyển sang "Câu hỏi tự kiểm tra"). Âm tiết 42 → 57.

### L02-02-04 — Tín hiệu học
- Vị trí: mạch 2, cụm phụ tín hiệu thưởng (`vấn đề`, `trực giác`). 1 phút. Nguồn: PPTX tr. 7–8; hw02 bài 1.
- Lý do tồn tại: bảng ba khung học; khung "Nhắc lại:" phần thưởng không cho biết hành động đúng hay sai.
- Quyết định: sửa nhẹ ("đúng hay sai", nhãn Nhắc lại, thuật ngữ gốc trong ghi chú diễn giả). Âm tiết 44 → 60.

### L02-02-05 — Giả thuyết phần thưởng
- Vị trí: mạch 2, cụm phụ (`ví dụ`, nhắc lại phát biểu). 2 phút. Nguồn: PPTX tr. 9, 25–26; ghi chú Ví dụ 02.3.
- Lý do tồn tại: giả thuyết phần thưởng (reward hypothesis) và hai đường 16 / 18 bước.
- Quyết định: sửa (tiêu đề bỏ "điểm thưởng"; dòng >20 âm tiết tách; "Ví dụ." đúng nhãn). Âm tiết 58 → 58.

### L02-02-06 — Phản hồi trễ
- Vị trí: mạch 2, cụm phụ (`ứng dụng`). 1 phút. Nguồn: PPTX tr. 7–8, 11.
- Lý do tồn tại: hình ván cờ; liên hệ bước Nam tại $(4,1)$.
- Quyết định: sửa nhẹ (nhãn "Ví dụ.", chỉ số $t$ thay $O_i$ trong ghi chú). Âm tiết 30 → 26.

## Mạch 3: Thông tin khả dụng và tính Markov — 27 phút

Chức năng: tách trạng thái, quan sát, biểu diễn; ghi quá khứ bằng lịch sử trạng thái; nêu điều kiện Markov và cách khôi phục. Đầu vào: mẫu chuyển với quan sát là tọa độ. Đầu ra: $X_t$ cho chính sách (mạch 4); tính Markov là giả thiết của $v_\pi$ và $p$ (mạch 5).

### L02-03-00 — 3. Thông tin khả dụng và tính Markov (trang tiêu đề mạch)
- Vị trí: điểm vào mạch 3. 1 phút. Dòng dẫn 20 âm tiết; ngoài hành trình khái niệm (vấn đề của cụm biểu diễn đặt ở `L02-03-02`).
- Quyết định: thêm.

### L02-03-02 — Ví dụ: cảm biến bốn ô kề tại ô (2,1)
- Vị trí: mạch 3, bước `vấn đề` + `ví dụ` dẫn nhập của cụm biểu diễn (làm cụ thể vấn đề "dữ liệu nào tác tử dùng"). 2 phút. Nguồn: PPTX tr. 16, 25–26; ghi chú Ví dụ 02.4.
- Lý do tồn tại: "Nhu cầu:", hình ba lớp thông tin, định nghĩa mã "1 khi bước giữ tác tử đứng yên"; $(2,1)$ và $(3,1)$ cùng mã.
- Kết nối ra: bảng ba đối tượng. Mục tiêu: 2.
- Quyết định: sửa (ký hiệu $S_t,O_t,X_t$ chuyển sang trang sau; mã theo định nghĩa của ghi chú; SVG sửa chú giải). Âm tiết 27 → 32.

### L02-03-11 — Trạng thái, quan sát và biểu diễn
- Vị trí: mạch 3, bước `trực giác`. 2 phút. Nguồn: PPTX tr. 16; ghi chú Mục 2.1.
- Lý do tồn tại: bảng ba đối tượng với giá trị tại $(2,1)$; "Nhắc lại:" $S_t,O_t$ theo Bài 01.
- Quyết định: sửa và tách (công thức $f_t$ sang `L02-03-12`). Âm tiết 63 → 58.

### L02-03-12 — Biểu diễn từ thông tin khả dụng
- Vị trí: mạch 3, bước `hình thức`. 2 phút. Nguồn: PPTX tr. 14–16, 21; ghi chú Định nghĩa 02.2.
- Lý do tồn tại: "Định nghĩa." $X_t=f_t(O_{0:t},A_{0:t-1},R_{1:t})$ và ba trường hợp ($\phi(O_t)$, cửa sổ, toàn bộ dữ liệu).
- Quyết định: thêm (tách từ `L02-03-11`). Âm tiết 51.

### L02-03-13 — Ví dụ: ba bước đầu trên mê cung 8×8
- Vị trí: mạch 3, bước `vấn đề`, `trực giác`, `ví dụ` của cụm lịch sử. 2 phút. Nguồn: ghi chú Ví dụ 02.5.
- Lý do tồn tại: dãy 10 thành phần và dãy mã tác tử nhận; ví dụ trước định nghĩa lịch sử.
- Quyết định: thêm. Âm tiết 55.

### L02-03-09 — Lịch sử trạng thái và quỹ đạo
- Vị trí: mạch 3, bước `hình thức` của cụm lịch sử. 2 phút. Nguồn: PPTX tr. 14–16; ghi chú Định nghĩa 02.3.
- Lý do tồn tại: định nghĩa $H_t$, $\tau=H_T$; "Lưu ý:" quan hệ với lịch sử quan sát của Bài 01.
- Quyết định: sửa (bỏ "mẫu dữ liệu một bước", đã thành mẫu chuyển; ví dụ đứng trước). Âm tiết 22 → 47.

### L02-03-06 — Quan sát đầy đủ và một phần
- Vị trí: mạch 3, bước `ứng dụng` của cụm biểu diễn. 2 phút. Nguồn: PPTX tr. 18–19, 27; ghi chú Nhận xét 02.4.
- Lý do tồn tại: "Nhận xét." với hàm $g$; năm ô cùng mã $(1,0,1,0)$.
- Quyết định: sửa (nhãn "Đầy đủ:", "Một phần:" ngoài danh sách → "Nhận xét."; hình lớp `short`). Âm tiết 17 → 42.

### L02-03-08 — Bài tập: mã bốn ô kề
- Vị trí: mạch 3, bước `kiểm tra` của cụm biểu diễn. 3 phút. Nguồn: ghi chú Bài tập 02.2.
- Loại: bài tập có lời giải mẫu (fragment). Mục tiêu: 2.
- Quyết định: tách (trang "Câu hỏi kiểm tra" 88 âm tiết cũ; câu phân loại giữ ở đây, câu chìa khóa sang `L02-03-15`, câu lịch sử và cửa sổ sang `L02-07-02` và ghi chú diễn giả). Âm tiết 88 → 55.

### L02-03-14 — Ví dụ: mê cung có chìa khóa
- Vị trí: mạch 3, bước `vấn đề` (Nhu cầu), `trực giác`, `ví dụ` của cụm Markov. 3 phút. Nguồn: ghi chú Ví dụ 02.6.
- Lý do tồn tại: hai lịch sử cùng độ dài $t=17$ cho hai dự báo $0$ và $1$.
- Kết nối ra: (2.3) dùng đúng $h,h'$. Quyết định: thêm. Âm tiết 59.

### L02-03-04 — Tính Markov
- Vị trí: mạch 3, bước `hình thức`. 3 phút. Nguồn: PPTX tr. 17; ghi chú Định nghĩa 02.5.
- Lý do tồn tại: "Định nghĩa." với giả thiết đếm được và xác suất dương; ví dụ chìa khóa: tọa độ vi phạm, (ô, $k$) thỏa; "Lưu ý:" tính Markov thuộc biến chọn làm trạng thái.
- Quyết định: sửa (nhãn, thuật ngữ gốc, ví dụ đứng trước). Âm tiết 26 → 50.

### L02-03-10 — Mở rộng trạng thái bằng lịch sử
- Vị trí: mạch 3, bước `ứng dụng` của cụm Markov. 2 phút. Nguồn: PPTX tr. 17; ghi chú Mệnh đề 02.6, Nhận xét 02.7.
- Lý do tồn tại: "Mệnh đề.", "Chứng minh." một dòng, "Ý nghĩa:", "Ví dụ." cửa sổ $m\le11$ tọa độ (độ dài cửa sổ ký hiệu $m$, chữ $k$ dành cho bit chìa khóa).
- Quyết định: sửa (tiêu đề dạng câu hỏi đổi theo quyết định 2 của điều phối viên). Âm tiết 39 → 56.

### L02-03-15 — Bài tập: kiểm tra tính Markov (đề)
- Vị trí: cuối mạch 3, bước `kiểm tra` của cụm Markov và lịch sử. 2 phút. Nguồn: ghi chú Bài tập 02.3 (câu a) và Bài tập 02.11 (câu b).
- Loại: bài tập có lời giải mẫu ở trang kế `L02-03-16`. Mục tiêu: 2.
- Quyết định: thêm (kế hoạch A3 dùng mã `L02-03-15` cho trang lời giải của bài mã bốn ô kề; lời giải đó nằm ở fragment của `L02-03-08`, nên mã được dùng cho bài tập Markov). Âm tiết 44.

### L02-03-16 — Bài tập: kiểm tra tính Markov (lời giải)
- Vị trí: cuối mạch 3, bước `kiểm tra` của cụm Markov. 1 phút. Nguồn: ghi chú Bài tập 02.3, 02.11.
- Lý do tồn tại: lời giải trên mặt trang, ở trang kế cùng tiêu đề (đề và lời giải trên một trang vượt 60 âm tiết); kết luận mã bốn ô kề không có tính Markov, khớp dòng 3 của Vấn đề trung tâm.
- Loại: bài tập có lời giải mẫu. Mục tiêu: 2.
- Quyết định: thêm (vòng biên tập sau rà soát). Âm tiết 58.

## Mạch 4: Quy tắc chọn hành động — 15 phút

Chức năng: viết cách chọn hướng thành phân phối trên biểu diễn; xác suất của dãy hành động; vai trò của chính sách ngẫu nhiên khi quan sát một phần. Đầu vào: $X_t$. Đầu ra: $\pi$ cho kỳ vọng $\mathbb E_\pi$ (mạch 5).

### L02-04-00 — 4. Quy tắc chọn hành động (trang tiêu đề mạch)
- Vị trí: điểm vào mạch 4. 1 phút. Dòng dẫn 19 âm tiết. Quyết định: thêm.

### L02-04-01 — Chính sách
- Vị trí: mạch 4, bước `vấn đề` + `trực giác`. 2 phút. Nguồn: PPTX tr. 20–21, 26; hw02 bài 6.
- Lý do tồn tại: "Nhu cầu:" hai tác tử ở cùng ô; câu định nghĩa bằng lời giữ theo quyết định 3; hình chính sách nguồn.
- Quyết định: sửa. Âm tiết 12 → 50.

### L02-04-02 — Ví dụ: hai quy tắc tại ô (1,2)
- Vị trí: mạch 4, bước `ví dụ`. 2 phút. Nguồn: ghi chú Ví dụ 02.7.
- Quyết định: sửa (tiêu đề "Ví dụ:", rút chú thích). Âm tiết 46 → 44.

### L02-04-04 — Chính sách trên biểu diễn
- Vị trí: mạch 4, bước `hình thức` (chính sách ngẫu nhiên). 2 phút. Nguồn: PPTX tr. 21; ghi chú Định nghĩa 02.8.
- Lý do tồn tại: (3.1)–(3.2) của ghi chú; ví dụ quy tắc thứ hai nêu lại dữ kiện.
- Quyết định: sửa (đặt trước chính sách xác định theo thứ tự của Định nghĩa 02.8; bỏ "Ví dụ từ bảng trước"). Âm tiết 30 → 52.

### L02-04-03 — Chính sách xác định
- Vị trí: mạch 4, bước `hình thức` (trường hợp riêng). 1 phút. Nguồn: PPTX tr. 21, 26.
- Quyết định: sửa nhẹ (nhãn "Định nghĩa.", thuật ngữ gốc, trường hợp riêng $\pi(a\mid x)=1$). Âm tiết 17 → 26.

### L02-04-07 — Ví dụ: xác suất của một dãy hai hành động
- Vị trí: mạch 4, bước `ứng dụng`. 2 phút. Nguồn: ghi chú Ví dụ 02.8.
- Lý do tồn tại: cụm thiếu ứng dụng (kế hoạch A4); chuẩn bị kỳ vọng theo cả chính sách và luật chuyển.
- Quyết định: thêm. Âm tiết 59.

### L02-04-08 — Ví dụ: hai ô cùng mã bốn ô kề
- Vị trí: mạch 4, bước `ứng dụng` (quan sát một phần). 2 phút. Nguồn: ghi chú Tình huống 02.2; Sutton và Barto §13.1; hw02 bài 6.
- Lý do tồn tại: mọi chính sách xác định trên mã thất bại; chính sách ngẫu nhiên cho kỳ vọng 20 bước; dùng hình `aliasing-pair-deck.svg` (bản cho trang chiếu của `aliasing-pair.svg`).
- Quyết định: thêm (ngoài kế hoạch A3; lấy từ tình huống của ghi chú để nối mạch 3 với mạch 4).

### L02-04-05 — Bài tập: chính sách ngẫu nhiên tại một ô
- Vị trí: cuối mạch 4, bước `kiểm tra`. 3 phút. Nguồn: ghi chú Bài tập 02.4.
- Loại: bài tập có lời giải mẫu (fragment). Mục tiêu: 3.
- Quyết định: sửa (thêm câu (b) xác suất ở lại $x$ theo ghi chú: $0{,}57$; câu 2–3 cũ thành câu (a)). Âm tiết 29 → 59.

## Mạch 5: Lợi tức, hàm giá trị và hàm động lực — 27 phút

Chức năng: quy chuỗi phần thưởng về lợi tức (kèm lý do trọng số hình học), lấy kỳ vọng thành hàm giá trị, tách dự báo một bước thành hàm động lực, phân biệt dự đoán với điều khiển. Đầu vào: $\pi$, tính Markov. Đầu ra: $G_t$ với $\gamma=1$ cho mạch 6; $v_\pi$, $p$ cho Bài 03.

### L02-05-00 — 5. Lợi tức, hàm giá trị và hàm động lực (trang tiêu đề mạch)
- Vị trí: điểm vào mạch 5. 1 phút. Dòng dẫn 19 âm tiết; ngoài hành trình khái niệm. Quyết định: thêm.

### L02-05-01 — Kết quả dài hạn của một bước
- Vị trí: mạch 5, bước `vấn đề` chung của ba cụm. 2 phút. Nguồn: PPTX tr. 10, 22–23, 26.
- Lý do tồn tại: "Nhu cầu:" Đông và Nam tại $(4,1)$ cùng $-1$; ba nhu cầu.
- Quyết định: sửa (bỏ ba thẻ và câu lặp Bài 01; ví dụ tại $(4,1)$ theo đoạn mở Mục 4 của ghi chú thay cho hai đường 16/18 bước của kế hoạch A3, vì hai đường đó đã dùng ở `L02-02-05`). Âm tiết 39 → 59; dòng 7 → 5.

### L02-05-11 — Ví dụ: hai chuỗi (2,0) và (1,1)
- Vị trí: mạch 5, bước `ví dụ` và `trực giác` của cụm ưu tiên dừng. 2 phút. Nguồn: ghi chú Ví dụ 02.9.
- Lý do tồn tại: ba bộ trọng số; bộ thứ ba đổi ưu tiên chặt thành ngang nhau.
- Quyết định: thêm (ví dụ trước đây chỉ trong ghi chú diễn giả). Âm tiết 44.

### L02-05-10 — Ưu tiên dừng
- Vị trí: mạch 5, bước `hình thức`. 1 phút. Nguồn: Russell và Norvig (2020) §17.1.1; ghi chú Định nghĩa 02.10.
- Lý do tồn tại: lợi ích cộng, $\succ$, $[r,\sigma]$, điều kiện dừng; ký hiệu $\sigma$ thay $a,b$ theo ghi chú.
- Quyết định: tách (trang cũ 71 âm tiết chứa định nghĩa, định lý và bảng; chứng minh và URL bỏ khỏi ghi chú diễn giả). Âm tiết 71 → 42.

### L02-05-12 — Trọng số hình học
- Vị trí: mạch 5, bước `hình thức` (kết quả). 3 phút. Nguồn: ghi chú Định lý 02.11.
- Lý do tồn tại: "Định lý." với giả thiết, kết luận, "Ý nghĩa:", "Chứng minh." một dòng; phản ví dụ $W$ trong ghi chú diễn giả.
- Quyết định: thêm (tách từ `L02-05-10`). Âm tiết 59.

### L02-05-15 — Ví dụ: ba bước cuối của đường 16 bước
- Vị trí: mạch 5, bước `ví dụ` của cụm lợi tức (và `ứng dụng` của trọng số hình học). 1 phút. Nguồn: ghi chú Ví dụ 02.10.
- Lý do tồn tại: ví dụ trước định nghĩa lợi tức; $-1{,}75$ với $\gamma=0{,}5$.
- Quyết định: thêm (kế hoạch A3 đề xuất một dòng ví dụ trên `L02-05-03`; ghi chú dùng ba bước cuối $t=13$, nên ví dụ thành trang riêng). Âm tiết 40.

### L02-05-03 — Lợi tức
- Vị trí: mạch 5, bước `hình thức`. 2 phút. Nguồn: PPTX tr. 22; ghi chú Định nghĩa 02.12.
- Lý do tồn tại: lợi tức (return), $G_T=0$; nhiệm vụ tiếp diễn; $\gamma=1$, $\gamma=0$.
- Quyết định: sửa (tiêu đề "Phần thưởng tích lũy" → "Lợi tức"; điều kiện $\gamma<1$ lên mặt trang). Âm tiết 19 → 38.

### L02-05-16 — Hệ thức truy hồi và chặn của lợi tức
- Vị trí: mạch 5, bước `hình thức` (kết quả) và `ứng dụng` của cụm lợi tức. 2 phút. Nguồn: ghi chú Mệnh đề 02.13.
- Quyết định: thêm (ghi chú có mệnh đề này; trước đây chỉ là câu trong ghi chú diễn giả). Âm tiết 38.

### L02-05-09 — Bài tập: lợi tức chiết khấu
- Vị trí: mạch 5, bước `kiểm tra` của cụm ưu tiên dừng và lợi tức. 3 phút. Nguồn: ghi chú Bài tập 02.5.
- Loại: bài tập có lời giải mẫu (fragment). Mục tiêu: 4.
- Quyết định: tách (câu 1, 4 cũ thay bằng đề của ghi chú; câu 2–3 cũ sang `L02-07-02`). Âm tiết 51 → 42.

### L02-05-04 — Ví dụ: môi trường hai nhánh
- Vị trí: mạch 5, bước `vấn đề` (Nhu cầu), `trực giác`, `ví dụ` của cụm hàm giá trị. 1 phút. Nguồn: PPTX tr. 22; ghi chú Ví dụ 02.11.
- Quyết định: sửa (tiêu đề "Ví dụ:"; dòng >20 âm tiết rút). Âm tiết 39 → 53.

### L02-05-05 — Hàm giá trị trạng thái
- Vị trí: mạch 5, bước `hình thức`. 2 phút. Nguồn: PPTX tr. 22, 24; ghi chú Định nghĩa 02.14, Nhận xét 02.15.
- Quyết định: sửa ("Giả thiết:" đủ bốn giả thiết; thuật ngữ gốc; nêu lại dữ kiện hai nhánh). Âm tiết 45 → 53.

### L02-05-13 — Ví dụ: giá trị của chính sách trên mê cung 8×8
- Vị trí: mạch 5, bước `ứng dụng` của cụm hàm giá trị. 2 phút. Nguồn: PPTX tr. 26; ghi chú Ví dụ 02.12.
- Lý do tồn tại: bảng giá trị nguồn ($-16$, $-1$, $-12$) và hệ thức $v_\pi(s)=-1+v_\pi(s')$.
- Quyết định: thêm (`source-values.svg` trước đây không dùng). Âm tiết 40.

### L02-05-08 — Hàm động lực
- Vị trí: mạch 5, bước `ví dụ` + `hình thức` của cụm hàm động lực. 2 phút. Nguồn: PPTX tr. 13, 23; ghi chú Ví dụ 02.13, Định nghĩa 02.16.
- Lý do tồn tại: ví dụ một bước đứng trước định nghĩa; $p$ chữ thường; $p(s'\mid s,a)$, $r(s,a)$.
- Quyết định: sửa (tiêu đề "Mô hình chuyển trạng thái và phần thưởng" → "Hàm động lực" theo ghi chú; $P\to p$). Âm tiết 37 → 56.

### L02-05-17 — Dự đoán và điều khiển
- Vị trí: mạch 5, bước `ứng dụng` của cụm hàm động lực và hàm giá trị. 1 phút. Nguồn: PPTX tr. 24; ghi chú Nhận xét 02.17.
- Quyết định: thêm (trước đây nằm trong ghi chú diễn giả mạch 6). Âm tiết 60.

### L02-05-18 — Bài tập: hàm động lực của bước trượt
- Vị trí: cuối mạch 5, bước `kiểm tra` của cụm hàm động lực. 2 phút. Nguồn: ghi chú Bài tập 02.7.
- Loại: bài tập có lời giải mẫu (fragment). Mục tiêu: 4.
- Quyết định: thêm. Âm tiết 34.

## Mạch 6: Thiết kế phần thưởng — 14 phút

Chức năng: dùng lợi tức với $\gamma=1$ để dự báo hành vi tối ưu khi người thiết kế đổi phần thưởng. Đầu vào: lợi tức, điều khiển. Đầu ra: ngưỡng $c^*=(10+c_{\mathrm H})/4$ và giới hạn của phép so sánh khuyến khích–chế tài.

### L02-06-00 — 6. Thiết kế phần thưởng (trang tiêu đề mạch)
- Vị trí: điểm vào mạch 6. 1 phút. Dòng dẫn 20 âm tiết. Quyết định: thêm.

### L02-06-01 — Ví dụ: mê cung đích–hố
- Vị trí: mạch 6, bước `vấn đề` (Nhu cầu) và dữ kiện. 2 phút. Nguồn: ví dụ do người dùng duyệt; ghi chú Ví dụ 02.14.
- Quyết định: sửa ($\alpha\to c$; tiêu đề "Ví dụ:"; nhãn nút chữ đứng $\mathrm S,\mathrm H,\mathrm G$). Âm tiết 31 → 50.

### L02-06-02 — Ví dụ: mê cung đích–hố, hai lợi tức
- Vị trí: mạch 6, bước `ví dụ`. 2 phút. Nguồn: ghi chú Ví dụ 02.15.
- Quyết định: sửa (hai thẻ, hai khung → một bảng; chú thích chỉ số dưới). Âm tiết 33 → 30.

### L02-06-03 — Ví dụ: mê cung đích–hố, ba mức chi phí
- Vị trí: mạch 6, bước `ví dụ`. 1 phút. Quyết định: sửa nhẹ (tiêu đề khẩu hiệu → "Ví dụ: …"). Âm tiết 20 → 27.

### L02-06-04 — Ngưỡng chi phí mỗi bước
- Vị trí: mạch 6, bước `trực giác` (đồ thị). 1 phút. Nguồn: ghi chú, hình `goal-hole-threshold.svg`.
- Quyết định: sửa (hình `incentive-threshold.svg` dùng $\alpha$ được thay bằng `goal-hole-threshold.svg` dùng $c$; tiêu đề cũ "Ngưỡng thay đổi hành vi" chuyển cho `L02-06-05`). Âm tiết 8 → 9.

### L02-06-05 — Ngưỡng đổi hành vi
- Vị trí: mạch 6, bước `hình thức`. 3 phút. Nguồn: ghi chú Mệnh đề 02.18.
- Lý do tồn tại: "Mệnh đề." đủ giả thiết, kể cả định nghĩa tác tử tối ưu và lợi tức của quỹ đạo không kết thúc; $c^*=(10+c_{\mathrm H})/4$; "Ý nghĩa:"; chứng minh và vai trò giả thiết trong ghi chú diễn giả (dòng "Chứng minh." chuyển xuống ghi chú để giữ trần 60).
- Quyết định: sửa (trang "Thiết kế thưởng và hành vi" cũ thành mệnh đề có nhãn). Âm tiết 35 → 58.

### L02-06-06 — Bài tập: phạt hố bổ sung
- Vị trí: mạch 6, bước `kiểm tra`. 3 phút. Nguồn: ghi chú Bài tập 02.8.
- Loại: bài tập có lời giải mẫu (fragment). Mục tiêu: 5.
- Quyết định: sửa (đề theo ghi chú: (a) $c=3$, (b) $c_{\mathrm H}=4$; ghi chú bài giảng và `exercises.md` cùng viết $c_{\mathrm H}$; ghi chú diễn giả sửa theo đợt 2026-10-14). Âm tiết 42 → 55.

### L02-06-07 — Khuyến khích và chế tài
- Vị trí: cuối mạch 6, bước `ứng dụng`. 1 phút. Nguồn: ghi chú Nhận xét 02.19, 02.20.
- Quyết định: sửa (giữ vị trí cuối mạch theo quyết định 9; một khung; pháp lý, đạo đức vào ghi chú diễn giả). Âm tiết 80 → 59; dòng tối đa 24 → 20.

## Mạch 7: Tổng kết và chuyển tiếp — 12 phút

Chức năng: đặt kết quả cạnh giả thiết không được bỏ, vận dụng tổng hợp, trả lời vấn đề trung tâm, tự kiểm tra, giao bài tập. Không có khái niệm mới.

### L02-07-00 — 7. Tổng kết và chuyển tiếp (trang tiêu đề mạch)
- Vị trí: điểm vào mạch 7. 1 phút. Dòng dẫn 18 âm tiết. Quyết định: thêm.

### L02-07-01 — Kết quả về thông tin và chính sách
- Vị trí: mạch 7. 2 phút. Bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`, năm hàng (02.1, 02.2, 02.5, 02.6, 02.8).
- Quyết định: sửa và tách đôi (bảng "Các thành phần của bài toán" cũ). Âm tiết 53 → 58.

### L02-07-06 — Kết quả về lợi tức, giá trị và phần thưởng
- Vị trí: mạch 7. 2 phút. Năm hàng (02.11, 02.12–02.13, 02.14, 02.16, 02.18). Bài không có thuật toán, nên không có bảng `Phương pháp | Quy tắc cập nhật | …`.
- Quyết định: thêm. Âm tiết 70 (ngoại lệ bảng tổng kết).

### L02-07-04 — Bài tập: mê cung đích–hố có chiết khấu
- Vị trí: mạch 7, bài tập tổng hợp. 2 phút. Nguồn: kế hoạch A2; trùng Bài tập 02.21 của `exercises.md`, câu (a), (b) (ghi chú diễn giả dẫn số hiệu từ đợt 2026-10-14).
- Lý do tồn tại: dùng lợi tức chiết khấu, tổng hình học và cách so sánh đường kết thúc khi bỏ giả thiết $\gamma=1$.
- Loại: bài tập tổng hợp có lời giải mẫu ở trang kế. Quyết định: thêm. Âm tiết 53.

### L02-07-07 — Bài tập: mê cung đích–hố có chiết khấu (lời giải)
- Vị trí: mạch 7. 2 phút. Số liệu tính lại: $(1-0{,}9^6)/0{,}1=4{,}68559$; $10\cdot0{,}9^5=5{,}9049$; $c=1$: $1{,}219$ và $-1{,}9$; $c=3$: $-8{,}152$ và $-5{,}7$; $c^*=5{,}9049/2{,}78559\approx2{,}120$.
- Quyết định: thêm. Âm tiết 41.

### L02-07-05 — Trả lời vấn đề trung tâm
- Vị trí: mạch 7. 1 phút. "Kết luận:" có điều kiện và dòng "Nguồn:".
- Quyết định: thêm. Âm tiết 77.

### L02-07-02 — Câu hỏi tự kiểm tra
- Vị trí: mạch 7. 1 phút. "Câu hỏi: trả lời và nêu kết quả đã dùng." và bốn câu (mê cung có chìa khóa: quan sát đầy đủ hay một phần, có Markov không, tùy biến chọn làm trạng thái; phản hồi một bước; $G_t$ với $v_\pi$, $p$ với chính sách tốt nhất); lời giải trong ghi chú diễn giả.
- Quyết định: sửa và đặt trước `L02-07-03` (gom câu tự kiểm tra từ các trang "Câu hỏi kiểm tra" cũ). Âm tiết 34 → 60.

### L02-07-03 — Bài tập về nhà và tài liệu đọc
- Vị trí: cuối mạch 7. 1 phút. Bảng `Mạch | Bài tập` chuyển vị theo bảng của `exercises.md`: hàng "Tệp bài tập" (02.1–02.5, 02.7, 02.8, 02.14–02.22 theo mạch 2–7), hàng "Chỉ trong ghi chú" (02.6, 02.9–02.13); "Tài liệu đọc:"; liên kết "Ghi chú bài giảng · Bài tập" tới hai trang viewer; dòng nối Bài 03 (MDP, phương trình Bellman).
- Quyết định: sửa (bỏ `h3` thay nhãn, thêm bảng và liên kết viewer, bỏ đường dẫn tệp nguồn khỏi ghi chú diễn giả). Âm tiết 62 → 70. Đợt 2026-10-14: đồng bộ với `exercises.md` (bảng sáu mạch, liên kết viewer bài tập, ghi chú diễn giả nêu phân bố bài giữa tệp bài tập và ghi chú); âm tiết 70 → 80, trong trần trang tổng kết.
