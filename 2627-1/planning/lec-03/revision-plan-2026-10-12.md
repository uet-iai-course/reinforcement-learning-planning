# Kế hoạch sửa Bài 03 theo chuẩn 2026-10-12

Báo cáo của tác tử kiểm toán chỉ đọc (Opus 5.5, `high`, loại `general-purpose`), điều phối viên lưu lại. Quyết định của điều phối viên cho các câu hỏi ở mục D nằm trong `planning/quyet-dinh-chuan-2026-10-12.md`, mục 8.

Đã đọc: deck (50 trang), ghi chú (609 dòng), sáu tệp planning; `density.py` rồi đếm lại công thức và ghi chú bằng lệnh riêng; mẫu math-4-AI Bài 07; `hw02.pdf`; ghi chú Bài 02/04/05; notebook CartPole Bài 04; chương 06 giáo trình *Học máy thống kê*. Số liệu tính lại: $v_\pi=(13/4,\,7/4)$; $q_\pi(\mathrm L,\cdot)=(3/4,\,15/8,\,13/8)$; $q_\pi(\mathrm H,\mathrm{tim})=13/4$, $q_\pi(\mathrm H,\mathrm{cho})=21/8$; kỳ vọng hai bước từ H là $21/8$, từ L là $9/8$; chính sách "luôn Chờ tại L": $v=(10/3,\,2)$; hw02 bài 3: $v\approx(0{,}874;\,-1{,}154;\,0)$.

## A. Deck

### A1. Mạch

Hiện 7 mạch: 1 Từ tương tác đến trạng thái Markov (01-01…07); 2 Mô hình xác suất của MDP (02-01…07); 3 Phần thưởng và tổng thưởng (03-01…06); 4 Chính sách và hàm giá trị (04-01…08); 5 Phương trình Bellman (05-01…10); 6 Đánh giá một chính sách từ mô hình (06-01…08); 7 Tổng hợp và vận dụng (07-01…04). Chưa có `strand-title`. Đề xuất: 7 mạch, gộp nội dung mạch 1 cũ (01-03…07) với mạch 2 cũ (Sutton–Barto §3.1 trình bày Markov và $p$ cùng mục). Mã trang tiêu đề `L03R-0N-00`; 01-03…01-07 giữ mã cũ, thuộc mạch 2.

| N | Tên | Dòng dẫn | Từ khóa | Mã | `id` |
|---|---|---|---|---|---|
| 1 | Mở đầu (bìa) | — | — | `L03R-01-01` | `mach-1` |
| 2 | Trạng thái Markov và mô hình môi trường | Muốn tính trước hậu quả của một hành động, phải mô tả phản hồi một bước bằng xác suất chỉ phụ thuộc trạng thái. (24) | Lịch sử · Tính Markov · Hàm động lực · Thưởng kỳ vọng · Bộ MDP | `L03R-02-00` | `mach-2` |
| 3 | Lợi tức chiết khấu | Muốn so sánh hai chuỗi phần thưởng, phải gộp chúng thành một số hữu hạn có trọng số theo thời gian. (21) | Lượt và nhiệm vụ tiếp diễn · Hệ số chiết khấu · Lợi tức · Cận lợi tức | `L03R-03-00` | `mach-3` |
| 4 | Chính sách và hàm giá trị | Muốn lấy kỳ vọng của lợi tức, phải cố định quy tắc chọn hành động ở mọi trạng thái. (19) | Chính sách · Kỳ vọng theo chính sách · Giá trị trạng thái · Giá trị hành động | `L03R-04-00` | `mach-4` |
| 5 | Phương trình Bellman kỳ vọng | Muốn tính giá trị mà không liệt kê vô hạn quỹ đạo, phải tách bước đầu và dùng lại giá trị trạng thái kế tiếp. (24) | Hệ thức đệ quy · Hai tầng kỳ vọng · Tính Markov · Quan hệ $v$–$q$ | `L03R-05-00` | `mach-5` |
| 6 | Đánh giá chính sách bằng hệ tuyến tính | Muốn có giá trị bằng số của một chính sách, phải giải hệ Bellman do mô hình và chính sách sinh ra. (20) | Hệ Bellman của robot · Chuỗi Markov · Quá trình phần thưởng Markov · Dạng ma trận | `L03R-06-00` | `mach-6` |
| 7 | Tổng kết và chuyển tiếp | Muốn dùng giá trị để chọn hành động, phải giữ đủ giả thiết của từng kết quả và biết điều còn thiếu. (20) | Giả thiết không được bỏ · Bài tập tổng hợp · Câu hỏi tự kiểm tra · Tài liệu đọc | `L03R-07-00` | `mach-7` |

Đổi tên trang nội dung đầu mạch 2–6 để không trùng tên mạch: 01-03, 03-01, 04-01, 05-01, 06-01.

### A2. Mở đầu và kết luận

Mở đầu 5 trang: 01-01 bìa (câu luận đề "Giá trị của một chính sách là nghiệm của phương trình Bellman do mô hình Markov sinh ra."; "Quá trình quyết định Markov (Markov decision process, MDP)"; ghi chú viết lại); 01-01b "Tiên quyết và quy ước" (mới): "Nhắc lại:" giao diện, một bước $(S_t,A_t,R_{t+1})$, chính sách xác định và ngẫu nhiên, hệ số chiết khấu (ghi chú Bài 02, Mục 2–5), xác suất có điều kiện, kỳ vọng toàn phần, hệ tuyến tính; "Ký hiệu:" $t=0,1,2,\dots$; $\mathcal S$, $\mathcal A(s)$, $\mathcal R$ hữu hạn; chữ hoa là biến ngẫu nhiên; $R_{t+1}$ đến sau $A_t$; $\mathbb E_\pi$; nhãn $\mathrm{tim},\mathrm{cho},\mathrm{sac}$. 01-01c "Mục tiêu học tập" (mới): lập bộ MDP và bảng $p$ (03.2, 03.18); tính lợi tức và cận (03.3); suy ra Bellman cho $v_\pi$, $q_\pi$ và chỗ dùng Markov (03.6, 03.7); lập, giải, kiểm hệ đánh giá chính sách (03.8, 03.16). 01-02 "Nội dung" (bỏ nhãn "Mục tiêu:"; bảy mạch; "Tài liệu đọc trước: Sutton và Barto (2018), §3.1–3.5"; 8 dòng, ghi ngoại lệ hoặc dàn hai cột). 01-02b "Vấn đề trung tâm" (mới): "Tính giá trị dài hạn của một cách chọn hành động khi phản hồi của môi trường là ngẫu nhiên."; mạch 2: trạng thái Markov ⇒ một bảng $p(s',r\mid s,a)$ đủ mô tả môi trường; mạch 3: thưởng bị chặn và $\gamma<1$ ⇒ lợi tức hữu hạn; mạch 4: cố định $\pi$ ⇒ $v_\pi$, $q_\pi$ xác định; mạch 5: Markov và $\pi$ dừng ⇒ Bellman; mạch 6: hữu hạn và $\gamma<1$ ⇒ $v_\pi=(I-\gamma P^\pi)^{-1}r^\pi$; dùng `robot-p06-policy-evaluation-setup.svg`.

Kết luận 7 trang: 07-00 tiêu đề mạch; 07-01a "Tổng kết" (mới):

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Mô hình MDP (Định nghĩa 03.4, 03.7) | trạng thái Markov; quy luật không đổi theo thời gian | $p(s',r\mid s,a)$, mỗi nhóm tổng bằng 1 |
| Thưởng kỳ vọng (Mệnh đề 03.6) | các tập hữu hạn | $r(s,a)=\sum_{s',r} r\,p(s',r\mid s,a)$ |
| Cận lợi tức (Mệnh đề 03.11) | $\lvert R\rvert\le M$; $\gamma<1$ | $\lvert G_t\rvert\le M/(1-\gamma)$ |
| Bellman cho $v_\pi$ (Định lý 03.21) | Markov; $\pi$ Markov dừng; lợi tức khả tích | $v_\pi(s)=\sum_a\pi\sum_{s',r}p[r+\gamma v_\pi(s')]$ |
| Quan hệ $v$–$q$ (Mệnh đề 03.22–03.23, Hệ quả 03.24) | như trên | $q_\pi=\sum p[r+\gamma v_\pi]$; $v_\pi=\sum\pi q_\pi$ |
| Nghiệm đánh giá chính sách (Định lý 03.28) | $\mathcal S$ hữu hạn; $\gamma<1$ | $(I-\gamma P^\pi)v=r^\pi$ |

07-01 và 07-02 → "Bài tập: ba hành động tại pin thấp" (đề và lời giải trên mặt trang: $q_\pi(\mathrm L,\cdot)=3/4,\,15/8,\,13/8$; kiểm $v_L=\tfrac12\cdot\tfrac{15}8+\tfrac12\cdot\tfrac{13}8=\tfrac74$; so sánh này không chứng minh tối ưu). 07-02b "Vấn đề trung tâm: kết luận" (mới): "Khi tập trạng thái hữu hạn, trạng thái Markov, $\pi$ Markov dừng và $\gamma<1$, giá trị dài hạn của $\pi$ là nghiệm duy nhất của hệ $n$ ẩn, thay cho trung bình trên vô hạn quỹ đạo."; "Nguồn: Sutton và Barto (2018) §3.1–3.5; Puterman (1994) §6.1". 07-04 → "Câu hỏi tự kiểm tra" (bốn câu: chỉ có $p(s'\mid s,a)$ thiếu $r(s,a)$; robot với $\gamma=1$; trạng thái thiếu vị trí; $q_\pi(\mathrm L,\mathrm{cho})>q_\pi(\mathrm L,\mathrm{sac})$ có chứng minh tối ưu không). 07-03 → "Bài tập về nhà và tài liệu đọc" (bảng `Mạch | Bài tập` theo `exercises.md`; "Tài liệu đọc:"; liên kết viewer; dòng nối sang Bài 04).

### A3. Bảng từng trang (NT = vượt 1,5 lần trần)

| Mã | Âm tiết | Vấn đề | Quyết định | Đề xuất |
|---|---|---|---|---|
| 01-01 | 25 | Thiếu luận đề; thiếu "(Markov decision process, MDP)"; ghi chú "Bài này…", "ta" | sửa | A2 |
| 01-01b, 01-01c | — | Thiếu | thêm | A2 |
| 01-02 | 56 | 8 dòng; "Mục tiêu:"; mục "Từ tương tác đến…"; ghi chú "người soạn" | sửa | "Nội dung" |
| 01-02b | — | Thiếu | thêm | A2 |
| 02-00 | — | Thiếu tiêu đề mạch 2 | thêm | A1 |
| 01-03 | 24 | Không mở bằng "Muốn…"; tiêu đề trùng vai ví dụ | sửa | "Lựa chọn của robot ở pin thấp"; "Muốn chọn giữa Tìm, Chờ, Sạc, phải biết hậu quả của từng hành động."; nguồn vào ghi chú |
| 01-04 | 21 | Thiếu "Ví dụ:"; nhãn $\mathrm{tim}$ chỉ trong ghi chú; ghi chú "trong lớp" | sửa | "Ví dụ: một bước của robot"; "Ký hiệu:" hoặc dời sang 01-01b |
| 01-05 | 23 | Một dòng 23 | sửa | "Trực quan."; tách hai dòng |
| 01-06 | 34 | Dòng 22; định nghĩa bằng ":"/"="; thiếu "Định nghĩa."; thiếu "(Markov property)" | sửa | "Định nghĩa. Trạng thái $S_t$ gọi là có tính Markov (Markov property) nếu…"; "(Định nghĩa 03.2)" |
| 01-07 | 48 | "Câu hỏi kiểm tra"; dòng 27; "Đáp án"; lời chỉ đường; thiếu "Gợi ý:" | sửa | "Bài tập: trạng thái của robot" (tự làm); "Gợi ý:" và "Lời giải:" trong ghi chú |
| 02-01 | 14 | Tiêu đề trùng mạch cũ; thiếu "Muốn…"; ghi chú "Phần trước ta…" | gộp | Vào 02-02: "Muốn dự đoán phản hồi sau L–Tìm, phải biết mọi phản hồi và xác suất." |
| 02-02 | 22 | Thiếu "Ví dụ:"; chú thích 22; alt "thưởng2" | sửa | "Ví dụ: hai phản hồi của hành động Tìm" |
| 02-03 | 75 | Bảng 7 hàng; chú thích 21; thiếu "Ví dụ:" | sửa | "Ví dụ: bảng phản hồi của robot"; ô dùng H/L và tim/cho/sac (~35 âm tiết); ngoại lệ bảng 7 hàng |
| 02-04 | 25 | Dòng 22; thiếu "Định nghĩa."; thiếu "(dynamics function)"; ghi chú dẫn "phần 1" | sửa | Định nghĩa dùng "là"; tách dòng |
| 02-05 | 22 | 3 công thức + 2 dòng | sửa | "Mệnh đề." "(Mệnh đề 03.6)"; dòng ví dụ dưới "Ví dụ." |
| 02-06 | 56 | Chú thích câu mảnh; thiếu "Định nghĩa." cho $\mathcal M$ | sửa | "Định nghĩa. MDP hữu hạn là bộ…"; "Giả thiết: …" |
| 02-07 | 74 | Vượt 60; 8 dòng; "Câu hỏi kiểm tra"; "Đáp án"; `font-size:32px` | tách | 02-07 "Bài tập: đọc hàm động lực của robot" + 02-07b "Lời giải:"; bỏ style |
| 03-00 | — | Thiếu | thêm | A1 |
| 03-01 | 9 | Tiêu đề trùng mạch; thiếu "Muốn…"; "tổng thưởng" | sửa | "Chuỗi phần thưởng của robot"; "Muốn so sánh hai cách hành động, phải gộp cả chuỗi thưởng thành một số." |
| 03-02 | 15 | Thiếu thuật ngữ gốc (episodic task, continuing task, episode, terminal state) | sửa | Định nghĩa dùng "là"; $\mathcal S^+$, $G_T=0$ từ 03-04 sang đây |
| 03-03 | 12 | Thiếu "Ví dụ:"; $\gamma$ thiếu "(discount factor)"; ghi chú "người soạn" | sửa | "Ví dụ: hai dãy thưởng ba bước của robot"; "Diễn giải:" $3/2<7/4$ |
| 03-04 | 51 | 7 dòng; "Tổng thưởng…" | sửa | "Lợi tức chiết khấu"; "Định nghĩa. Lợi tức (return) là…" |
| 03-05 | 24 | Dòng 21; định lý, ví dụ, hình chung trang | sửa | "Mệnh đề." + "Chứng minh." một dòng; ví dụ $\lvert G\rvert\le6$ thành "Ví dụ." một dòng |
| 03-06 | 50 | "Câu hỏi kiểm tra"; "Đáp án"; không lời giải trên mặt trang | tách | 03-06 "Bài tập: lợi tức và cận của robot" + 03-06b "Lời giải:" ($3/2$; $\gamma=0$ cho $0$; $-6\le G_t\le6$) |
| 04-00 | — | Thiếu | thêm | A1 |
| 04-01 | 9 | Tiêu đề trùng mạch; thiếu "Muốn…" | sửa | "Lựa chọn hành động tại pin thấp"; "Muốn lấy trung bình lợi tức, phải biết quy tắc chọn hành động." |
| 04-02 | 59 | Dòng 22; 6 dòng; ghi chú "người soạn", "cho lớp" | sửa | "Ví dụ: chính sách chia đều tại pin thấp"; "số liệu sư phạm tự xây dựng" |
| 04-03 | 0 | Chỉ công thức; không "là"; thiếu "(policy)"; $\mathbb E_\pi$ chưa định nghĩa | sửa | "Định nghĩa. Chính sách Markov dừng là…"; "Ký hiệu: $\mathbb E_\pi$ …" |
| 04-04 | 7 | Thiếu "Ví dụ:"; $G_0^{[2]}$ chưa gọi tên; ghi chú 260 từ | sửa | "Ví dụ: kỳ vọng hai bước từ pin cao"; "lợi tức cắt sau hai bước" |
| 04-05 | 34 | Dòng 22; định nghĩa bằng "="; thiếu "(state-value function)" | sửa | "Định nghĩa. Giá trị trạng thái … là $v_\pi(s)=…$" |
| 04-06 | 31 | Dòng 31 (NT); thiếu ví dụ số trước $q$ | sửa | Hai dòng; "Ví dụ: ba thí nghiệm từ pin thấp" |
| 04-07 | 53 | Dòng 41 (NT); thiếu "Định nghĩa."; thiếu "(action-value function)" | sửa | Một dòng định nghĩa, một dòng quy ước $\pi(a\mid s)=0$ |
| 04-08 | 48 | "Câu hỏi kiểm tra"; "vừa"; "Đáp án" | tách | 04-08 "Bài tập: mô hình, chính sách và giá trị" (tự làm) + 04-08b "Bài tập: kỳ vọng hai bước từ pin thấp" với "Lời giải:" $9/8$ |
| 05-00 | — | Thiếu | thêm | A1 |
| 05-01 | 11 | Tiêu đề trùng mạch; thiếu "Muốn…" | sửa | "Nhóm quỹ đạo theo bước đầu" |
| 05-02 | 25 | Thiếu "Ví dụ:"; ghi chú "của lớp" | sửa | "Ví dụ: phương trình một bước tại pin thấp" |
| 05-03 | 16 | "phần thưởng tích lũy"; thiếu nhãn | sửa | "Hệ thức đệ quy của lợi tức"; "Bổ đề." + "Chứng minh." |
| 05-04 | 11 | "vừa chứng minh"; chưa ghi miền tổng | sửa | "Thế (Bổ đề 03.18) vào định nghĩa $v_\pi$:"; $a\in\mathcal A(s)$ |
| 05-05 | 31 | Khung chứa quy ước | sửa | "Ký hiệu:" |
| 05-06 | 28 | "Từ…đến…"; dòng 22; bổ đề và định lý chung trang | tách | 05-06 "Bổ đề: tính Markov của phần tương lai" + 05-06b "Phương trình Bellman kỳ vọng cho $v_\pi$" ("Định lý." đủ giả thiết, "Bellman expectation equation") |
| 05-07, 05-08 | 19, 27 | Thiếu nhãn | sửa | "Mệnh đề." |
| 05-09 | 6 | Tiêu đề chưa chuẩn; thiếu nhãn | sửa | "Phương trình Bellman kỳ vọng cho $q_\pi$"; "Hệ quả." |
| 05-10 | 52 | "Câu hỏi kiểm tra"; dòng 22; "Đáp án" | tách | 05-10 "Bài tập: chỗ dùng tính Markov" (tự làm) + 05-10b "Bài tập: phương trình Bellman tại pin cao" với "Lời giải:" $v_H=2+\tfrac14v_H+\tfrac14v_L$ |
| 06-00 | — | Thiếu | thêm | A1 |
| 06-01 | 8 | Tiêu đề trùng mạch; ghi chú "Phần này…"; thiếu "(policy evaluation)", "(prediction)" | sửa | "Bài toán đánh giá chính sách"; "Đầu vào: $p,\pi,\gamma$", "Đầu ra: $v_\pi$" |
| 06-02 | 40 | Dòng 23; thiếu "Ví dụ:" | sửa | "Ví dụ: hệ Bellman của robot"; "Nhắc lại" phương trình H của 05-10b |
| 06-03 | 0 | Thiếu kiểm tra lại | sửa | "Ví dụ: hệ Bellman của robot, lời giải"; dòng kiểm tra |
| 06-04 | 27 | Khung 27 âm tiết | sửa | "Ví dụ: kiểm tra nghiệm bằng giá trị hành động"; khung ≤20 |
| 06-05 | 68 | Vượt 60; dòng 53 (NT) | sửa | "Ví dụ: gộp các nhánh của robot"; đoạn dài sang ghi chú; giữ bảng và $r^\pi(\mathrm L)=\tfrac12$ |
| 06-06 | 16 | Định nghĩa bằng ":"; thiếu "(Markov chain)", "(Markov reward process)" | sửa | "Định nghĩa." |
| 06-07 | 45 | Dòng 24; kết quả, ví dụ, điều kiện chung trang; chưa có thuật toán | tách | 06-07 "Phương trình Bellman dạng ma trận" + 06-07b "Định lý: nghiệm duy nhất khi $\gamma<1$" (giả thiết, kết luận, "Chứng minh." một dòng, "Lưu ý:" $\gamma=1$) + "Thuật toán." bốn bước, chi phí $O(n^3)$ |
| 06-08 | 78 | Vượt 60; dòng 37 (NT); `span.keyword`; "Đáp án" | tách | 06-08 "Bài tập: đánh giá chính sách luôn Chờ tại pin thấp" + 06-08b "Lời giải:" $v=(10/3,\,2)$; câu $q(\mathrm L,\mathrm{tim})$ sang 07-01 |
| 07-00, 07-01a, 07-02b | — | Thiếu | thêm | A2 |
| 07-01 | 14 | Tiêu đề trùng mạch; trùng 06-04 | sửa | "Bài tập: ba hành động tại pin thấp" (đề) |
| 07-02 | 19 | Lặp 06-04 | sửa | Cùng tiêu đề, "Lời giải:" ba giá trị $q$ |
| 07-04 | 52 | Dòng 23; "Đáp án" | sửa | "Câu hỏi tự kiểm tra" |
| 07-03 | 81 | Vượt 80; mã "hw02" | sửa | A2 |

Toàn deck: ghi chú bảy trang đề bài thiếu "Gợi ý:"; gạch dài trong ghi chú (01-04, 01-05, 01-06, 05-05, 05-07, 06-02/03/04/07/08); ghi chú dẫn "phần N"; alt SVG dính chữ (02-02, 03-02, 03-03, 04-03, 04-04, 05-01, 05-02). Thời lượng sau sửa (~67 trang): mạch 1–7 lần lượt 8, 24, 14, 17, 27, 20, 10 phút.

### A4. Cụm khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Thiếu |
|---|---|---|---|---|---|---|---|
| K1 Tính Markov | 01-03 | 01-05 | 01-04, 01-05 | 01-06 | — | 01-07 | Ứng dụng (thêm "Ví dụ." trạng thái pin là Markov; phản ví dụ vị trí); "Muốn…" |
| K2 Hàm động lực và MDP | 02-01 (gộp) | 02-02 | 02-03 | 02-04, 02-06 | 02-05 | 02-07/07b | Lời giải trên mặt trang |
| K3 Lợi tức | 03-01 | 03-02, 03-03 | 03-03 | 03-04, 03-05 | 03-05 | 03-06/06b | "Muốn…"; lời giải |
| K4 Chính sách | 04-01 | 04-02 | 04-02 | 04-03 | 04-04 | 04-08 | Trực giác gộp ví dụ: ghi storyboard |
| K5 $v_\pi$ | 04-04 | 04-05 | 04-04 | 04-05 | 06-03 | 04-08 | Dòng vấn đề; ứng dụng xa |
| K6 $q_\pi$ | ghi chú 04-05 | 04-06 | thiếu | 04-07 | 05-07, 06-04 | 04-08 | Vấn đề; ví dụ số |
| K7 Bellman cho $v_\pi$ | 05-01 | 05-01, 05-03 | 05-02 | 05-03…05-06b | 06-02 | 05-10/10b | Tách định lý khỏi suy diễn |
| K8 $v$–$q$, Bellman cho $q$ | thiếu | 05-07 | 05-07, 05-08 | 05-07…05-09 | 06-04 | 05-10 | Dòng vấn đề |
| K9 Đánh giá chính sách | 06-01 | 06-02 | 06-02, 06-03 | 06-07/07b | 06-04 | 06-08/08b | "Thuật toán." với đầu vào, đầu ra, bước, chi phí |
| K10 Chuỗi Markov / MRP (phụ) | 06-04 | 06-05 | 06-05 | 06-06 | 06-07 | 06-08 | Chu trình rút gọn, ghi lý do |

### A5. Ví dụ xuyên suốt

Robot thu gom lon hai mức pin (Sutton–Barto ví dụ 3.3): $\alpha=\beta=1/2$, thưởng Tìm 2, Chờ 1, cứu hộ $-3$, Sạc 0; $\pi$: Tìm tại H; Chờ hoặc Sạc mỗi hành động $1/2$ tại L; $\gamma=1/2$. Tên gọi: "robot thu gom lon hai mức pin"; "chính sách chia đều tại pin thấp"; "chính sách luôn Chờ tại pin thấp". Nêu lại dữ kiện ở 03-03, 05-04…05-06, 07-01. Hai tình huống của ghi chú dùng lưới 5×5 (Sutton–Barto) và CartPole rời rạc hóa (Bài 04).

## B. Ghi chú bài giảng

### B1. Đối chiếu từng mục (mục ghi chú §k ứng với mạch k+1; còn 5 mục nội dung)

| Dòng | Mục hiện có | Mạch mới | TP | Hành động |
|---|---|---|---|---|
| 1 | `# Bài 03 — …` | — | 1 | Giữ |
| 6 | `## 1. Từ tương tác đến trạng thái Markov` | 2 | 7 | `## 1. Trạng thái Markov và mô hình môi trường`; đoạn mở dòng 8 thành bài toán có số và móc nối Bài 02 |
| 10 | `### Mục tiêu và kiến thức tiên quyết` | 1 | 3, 4 | Tách hai mục `##`, trước Mục 1 |
| 14 | `### Nội dung bài học` | 1 | — | Bỏ; thay `## Bảng ký hiệu`, `## Bản đồ chủ đề` |
| 24 | `### Robot thu gom lon` | 2 | vấn đề | `### 1.1`, Ví dụ 03.1 |
| 28 | `### Mẫu đơn của một bước tương tác` | 2 | ví dụ, định nghĩa | Ví dụ 03.2 → Định nghĩa 03.1 |
| 36 | `### Hai lịch sử, cùng trạng thái hiện tại` | 2 | trực giác | "Một cách trực quan…"; Ví dụ 03.3 |
| 42 | `### Tính Markov` | 2 | định nghĩa | Định nghĩa 03.2 + diễn giải + phản ví dụ (Ví dụ 03.4) + Nhận xét 03.3 |
| 50 | exercise | 2 | bài tập | Bài tập 03.1 + `hint` |
| 64 | `## 2. Mô hình xác suất của MDP` | 2 | 7 | Gộp vào Mục 1 thành `### 1.3`; dòng 66 "Phần trước…" |
| 68, 74 | Hai phản hồi; Bảng phản hồi | 2 | ví dụ | Ví dụ 03.5 |
| 88 | `### Định nghĩa hàm p` | 2 | định nghĩa | Định nghĩa 03.4 + Nhận xét 03.5 |
| 100 | `### Xác suất chuyển và thưởng trung bình` | 2 | kết quả | Ví dụ 03.6 trước Mệnh đề 03.6 + `proof` |
| 114 | `### Các thành phần của MDP` | 2 | định nghĩa | Định nghĩa 03.7, Ví dụ 03.7; "Trong thực hành" |
| 127 | exercise | 2 | bài tập | Bài tập 03.2 |
| 141 | `## 3. Phần thưởng và tổng thưởng` | 3 | 7 | `## 2. Lợi tức chiết khấu`; đoạn mở 143 là khẳng định |
| 145 | `### Nhiệm vụ có kết thúc và tiếp diễn` | 3 | định nghĩa | Định nghĩa 03.8; danh sách hai trường hợp |
| 149 | `### Điểm thưởng ở các thời điểm` | 3 | ví dụ | Ví dụ 03.8 |
| 159 | `### Tổng thưởng từ thời điểm hiện tại` | 3 | định nghĩa | Định nghĩa 03.9 + Mệnh đề 03.10 |
| 171 | `### Điều kiện để tổng thưởng hữu hạn` | 3 | kết quả | Mệnh đề 03.11 + `proof`, Ví dụ 03.9, Nhận xét 03.12 |
| 181 | exercise | 3 | bài tập | Bài tập 03.3 |
| 195 | `## 4. Chính sách và hàm giá trị` | 4 | 7 | `## 3.` |
| 199 | `### Một cách điều khiển robot` | 4 | ví dụ | Ví dụ 03.10 |
| 212 | `### Chính sách là phân phối trên hành động` | 4 | định nghĩa | Định nghĩa 03.13 + Mệnh đề 03.14 |
| 224 | `### Trung bình trên các nhánh quỹ đạo` | 4 | ví dụ | Ví dụ 03.11 |
| 238 | `### Giá trị trạng thái` | 4 | định nghĩa | Định nghĩa 03.15 |
| 246 | `### Ấn định hành động đầu tiên` | 4 | trực giác | Thêm Ví dụ 03.12 có số |
| 252 | `### Giá trị hành động` | 4 | định nghĩa | Định nghĩa 03.16 + Nhận xét 03.17 |
| 261 | exercise | 4 | bài tập | Bài tập 03.4, 03.5 |
| 274 | `## 5. Phương trình Bellman` | 5 | 7 | `## 4. Phương trình Bellman kỳ vọng`; dòng 276 "Ta thử…" |
| 278 | `### Một bước từ pin thấp` | 5 | vấn đề, ví dụ | Ví dụ 03.13 |
| 291 | `### Tách phần thưởng tích lũy` | 5 | kết quả | Bổ đề 03.18 + `proof` |
| 303, 317 | Lấy trung bình theo hành động đầu; theo phản hồi | 5 | kết quả | Bổ đề 03.19 (a), (b), Ví dụ 03.14 |
| 335 | `### Từ trạng thái kế tiếp đến giá trị tương lai` | 5 | kết quả | Đổi tiêu đề; Bổ đề 03.20 + Định lý 03.21 + `proof` theo bước |
| 358, 375 | Giá trị hành động từ phản hồi; giá trị trạng thái từ $q$ | 5 | kết quả | Mệnh đề 03.22, 03.23 |
| 390 | `### Bellman kỳ vọng cho giá trị hành động` | 5 | kết quả | Hệ quả 03.24; "Nguồn:" dòng 403 vào câu |
| 407 | exercise | 5 | bài tập | Bài tập 03.6, 03.7; Nhận xét 03.25 |
| 420 | `## 6. Đánh giá một chính sách từ mô hình` | 6 | 7 | `## 5.` |
| 424, 435 | Hệ Bellman của robot; Giải hai phương trình | 6 | ví dụ tính tay | Ví dụ 03.15 có nhãn giai đoạn |
| 458 | `### Kiểm tra giá trị bằng các hành động` | 6 | ứng dụng | Ví dụ 03.16 |
| 477 | `### Gộp các nhánh dưới chính sách` | 6 | trực giác MRP | Ví dụ 03.17 |
| 490 | `### Chuỗi Markov và MRP dưới chính sách` | 6 | định nghĩa | Định nghĩa 03.26 |
| 506 | `### Bellman dưới dạng ma trận` | 6 | kết quả, thuật toán | Mệnh đề 03.27, Định lý 03.28 + `proof` (524), Thuật toán 03.29, Nhận xét 03.30 |
| 540 | exercise | 6 | bài tập | Bài tập 03.8 |
| 556 | `## 7. Tổng hợp và vận dụng` | 7 | 8, 9 | Giải thể: ba giá trị $q$ thành Bài tập 03.9 (cuối Mục 5); dòng 566 vào Tóm tắt |
| 568 | `### Đọc một quyết định…` | 7 | — | Gộp vào Bài tập 03.9 |
| 580 | `### Bài tập và bước tiếp theo` | 7 | 10 | Bỏ bảng hw02 |
| 591 | exercise | 7 | 9, 10 | "Giả thiết hay bị bỏ quên" và bài củng cố nhận biết |
| 604 | `### Tài liệu đọc` | 7 | 11 | `## Hướng dẫn đọc thêm và tài liệu tham khảo` |

Thiếu hẳn: TP5, TP6, TP8, TP9, TP10. Thứ tự: mục tiêu và tiên quyết lên trước Mục 1; Định lý 03.21 sau ví dụ và bổ đề, chứng minh ngay sau; Thuật toán 03.29 sau Ví dụ 03.15 và Định lý 03.28. `note-topic-id` `lec-03-part-01…07` ánh xạ lại sang 5 mục.

### B2. Đánh số

| Số | Loại | Nội dung (dòng) |
|---|---|---|
| 03.1 | definition | Quỹ đạo, lịch sử, quy ước $R_{t+1}$ (28–34, 44) |
| 03.2 | definition | Tính Markov (42–48) |
| 03.3 | remark | Trạng thái đủ thông tin khác biết quy luật; mở rộng trạng thái (40, 48, 59) |
| 03.4 | definition | Hàm động lực $p$ và chuẩn hóa (88–98) |
| 03.5 | remark | Tính dừng khác Markov; $(s',r)$ rút cùng nhau (72, 98) |
| 03.6 | proposition + proof | Xác suất chuyển và thưởng kỳ vọng (100–112) |
| 03.7 | definition | MDP hữu hạn $\mathcal M$ (114–125) |
| 03.8 | definition | Lượt, nhiệm vụ có kết thúc và tiếp diễn, $\mathcal S^+$ (145–147) |
| 03.9 | definition | Lợi tức chiết khấu (159–169) |
| 03.10 | proposition + proof | Hai dạng lợi tức trùng nhau khi đệm 0 (169) |
| 03.11 | proposition + proof | Cận $M/(1-\gamma)$ (171–177) |
| 03.12 | remark | $\gamma=1$ với nhiệm vụ có lượt (179) |
| 03.13 | definition | Chính sách Markov dừng (212–222) |
| 03.14 | proposition | Xác suất đoạn quỹ đạo là tích $\pi\cdot p$ (222, 232) |
| 03.15 | definition | $v_\pi$ (238–244) |
| 03.16 | definition | $q_\pi$ (252–259) |
| 03.17 | remark | $q_\pi$ khi $\pi(a\mid s)=0$; $q\ne r(s,a)$; $G_t\ne v_\pi$ (259, 600) |
| 03.18 | lemma + proof | $G_t=R_{t+1}+\gamma G_{t+1}$ (291–301) |
| 03.19 | lemma + proof | Hai tầng kỳ vọng (303–333) |
| 03.20 | lemma + proof | Tính Markov của phần tương lai (335–347); thiếu chứng minh |
| 03.21 | theorem + proof | Bellman kỳ vọng cho $v_\pi$ (349–356) |
| 03.22 | proposition | $q_\pi$ theo $v_\pi$ (358–373) |
| 03.23 | proposition | $v_\pi$ theo $q_\pi$ (375–388) |
| 03.24 | corollary + proof | Bellman cho $q_\pi$ (390–405) |
| 03.25 | remark | Chỗ dùng từng giả thiết; trung bình khác cực đại (300, 315, 346) |
| 03.26 | definition | Chuỗi Markov và MRP cảm sinh (490–504) |
| 03.27 | proposition | Bellman dạng ma trận (506–522) |
| 03.28 | theorem + proof | Tồn tại, duy nhất, $v_\pi=(I-\gamma P^\pi)^{-1}r^\pi$ (524–536) |
| 03.29 | algorithm | Đánh giá chính sách bằng giải hệ (420–538) |
| 03.30 | remark | $\gamma=1$, hấp thụ, $O(n^3)$, dẫn Bài 04 (535–538) |
| 03.31 | remark | So sánh $q_\pi$ chưa chứng minh tối ưu (475, 601) |

Ví dụ 03.1 robot (24); 03.2 một bước (28); 03.3 hai lịch sử (36); 03.4 phản ví dụ vị trí (mới); 03.5 bảng phản hồi (68–86); 03.6 L–Tìm $-1/2$ (100); 03.7 bộ MDP (114); 03.8 hai dãy thưởng $3/2$, $7/4$ (149); 03.9 cận 6 (177); 03.10 chính sách chia đều (199); 03.11 $21/8$ (224); 03.12 ba thí nghiệm (246); 03.13 phương trình tại L (278); 03.14 hai nhánh L–Tìm (319, 362); 03.15 hệ và nghiệm (424–456); 03.16 kiểm bằng $q$ (458); 03.17 MRP và ma trận (477–522). Bài tập trong mục 03.1–03.9; củng cố 03.10–03.15; chỉ `exercises.md` 03.16–03.19. Tình huống 03.1, 03.2. Các khối `derivation` (293, 339, 437) thành `proof` hoặc phần tính của ví dụ.

### B3. Tiêu chuẩn thứ nhất và trình bày sáng sủa

Giọng kể hiện khách quan ("ta" 6 lần: 86, 276, 289, 356, 558). Chuyển sang "chúng ta" cho kế hoạch, "ta" trong tính toán (276 → "Để tránh liệt kê vô hạn quỹ đạo, chúng ta nhóm các quỹ đạo theo bước đầu…"; 422 → "Chúng ta cần hai con số…").

| Tiêu chí | Vi phạm | Cách sửa |
|---|---|---|
| Tài liệu làm chủ ngữ | 8, 66, 589 | Chủ ngữ là người viết cùng người đọc hoặc đối tượng |
| Vấn đề đi trước công cụ | 143, 422, 8 | Mở mục bằng bài toán có số trên robot |
| Công thức có câu dẫn và đọc | 108→110; 123; 161, 165; 228 | Thêm câu trước và sau |
| Ký hiệu gọi tên | 153 ($\gamma$); 228 ($G_0^{[2]}$) | Gọi tên, kiểu, miền tại chỗ |
| Bước suy diễn có căn cứ | 300, 179 (đổi thứ tự kỳ vọng); 346 (Markov phần tương lai); 529 (Neumann) | Căn cứ cột phải; Bổ đề 03.20 chứng minh quy nạp |
| Bản đọc; bỏ giả thiết → phản ví dụ | sau 356, 535 | "Bỏ $\gamma<1$: robot luôn Chờ có $G=\infty$"; "Bỏ Markov: trạng thái thiếu vị trí"; "Bỏ tính dừng của $\pi$: $v_\pi$ phụ thuộc $t$" |
| Ví dụ trước tổng quát, nhắc lại sau | 246–259; 167 | Ví dụ số cho $q$; câu nhắc lại sau định nghĩa $G_t$ |
| Nối mục bằng kết quả | Mọi mục kết bằng bài tập (61, 138, 192, 271, 417, 553) | Đoạn kết văn xuôi |
| Không tham chiếu ra ngoài | 98, 244, 259, 422 "phần N"; 589 hw02 | Số hiệu; bỏ hw02 khỏi văn bản |
| Câu đủ thành phần | 30, 40, 161, 165, 254, 280, 337, 360, 460, 464, 471 | Viết lại |
| Nhầm lẫn thường gặp | Thiếu: $\gamma$ nhỏ ≠ tham lam; $v_\pi$ ≠ lợi tức một quỹ đạo | Nhận xét |
| Hình được đọc | 38, 564; 151, 230 một phần | Đoạn đọc hình |
| Độ dài | ~7 400 từ văn xuôi | Đích 13 000–15 000 |
| Một ý một đoạn | 26, 86, 147, 169, 222, 232, 244, 433, 504 | Tách |
| Chứng minh theo bước | 524–536 nhãn nghiêng, thiếu Bước, $\square$ | Chuẩn hóa |
| Trường hợp thành danh sách | 147, 169, 179 | Danh sách |
| `\tag` | Không có; 456, 177 trong dòng | `$$…\tag{k.m}$$` |
| Định lý bốn phần | Chưa có | Viết đủ |
| Giai đoạn của ví dụ | 424–456 | Nhãn in đậm |

### B4. Phần cần thêm

Móc nối sau Định nghĩa 03.2 (so với Markov không hình thức Bài 02), 03.4 ($p$ khác mẫu chuyển), 03.7, 03.9, 03.13, 03.15/03.16 ($v$ khác $q$), 03.26 (MRP là MDP cộng chính sách); trước Định lý 03.21 (cần Bổ đề 03.18–03.20); sau Định lý 03.28 (mạnh hơn 03.21, trả giá $\gamma<1$ và hữu hạn); mở chương từ Bài 02; kết chương sang Bài 04 (chọn chính sách, lặp) và Bài 05–06 (không biết $p$). "Trong thực hành": sau 03.4 ($p$ thường không biết; notebook Bài 04 ước lượng $\hat p$ cho 324 ô CartPole); sau 03.11 (cận $1/(1-\gamma)$ cho CartPole thưởng $+1$); sau 03.21 (mục tiêu $r+\gamma V(s')$ của TD(0) Bài 05, DQN Bài 08); sau 03.24 (Sarsa Bài 06); sau 03.28/03.29 ($n=324$ giải trực tiếp; $n$ lớn thì lặp Bài 04). Tình huống 03.1 lưới 5×5 (Sutton–Barto ví dụ 3.5, chính sách đều, $\gamma=0{,}9$; 25 trạng thái; kiểm giả thiết 03.28; $v(A)=10+0{,}9\cdot v(A')\approx8{,}8$; rà toán tính lại $v(B)$; vẽ SVG). Tình huống 03.2 CartPole rời rạc hóa: gộp trạng thái liên tục làm mất Markov; $v$ từ $\hat p$ là giá trị của MDP thay thế. Ứng dụng: Bài 04, 05, 06, 08, notebook Bài 04. Kết mục 5 đoạn. Tóm tắt: $p$, $G_t$, Bellman $v$ và $q$, dạng ma trận; giả thiết hay bỏ quên: Markov, dừng, $\gamma<1$, thưởng cố định trên nhánh. Củng cố 03.10–03.15: nhận biết (phân loại nhiệm vụ và chọn $\gamma$; quan sát chỉ vị trí CartPole có Markov không); tính toán ($q_\pi(\mathrm H,\mathrm{tim})=13/4$, $q_\pi(\mathrm H,\mathrm{cho})=21/8$, kiểm $v_H$; lượt $T=3$, $R=(1,-1,2)$, $\gamma=0{,}9$: $G_0=1{,}72$, $G_1=0{,}8$); vận dụng (mô hình hóa theo hw02 bài 10; robot $\beta=3/4$). Độ dài đích 13 000–15 000 (mở 600; ký hiệu 500; §1 3 000; §2 1 800; §3 2 000; §4 2 800; §5 2 200; tình huống 1 200; tóm tắt 1 200).

### B5. Giáo trình

Mục 1: Sutton–Barto §3.1 (tr. 47–50), (3.2)–(3.6), ví dụ 3.3 (tr. 52–53); Puterman §2.1; Szepesvári §1.2; SML `sec_mdp_introduction.tex`. Mục 2: Sutton–Barto §3.2–3.4 (tr. 53–57); SML "Giá trị của quỹ đạo"; Puterman chương 5. Mục 3: Sutton–Barto §3.5 (tr. 58); Puterman §2.1; SML `sec_dynamic_progamming.tex`. Mục 4: Sutton–Barto (3.14), sơ đồ dự phòng tr. 59, bài tập 3.12–3.13, 3.17–3.19; Szepesvári §1.3; Puterman §6.1. Mục 5: Puterman §6.1 (Định lý 6.1.1, Neumann); Bertsekas (2019) bài toán vô hạn chiết khấu; Sutton–Barto ví dụ 3.5; hw02 bài 3–4. Tình huống: Sutton–Barto ví dụ 3.5, hình 3.2; notebook Bài 04.

### B6. Bảng ký hiệu và chỗ lệch

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $t$ | thời điểm quyết định | $\{0,1,2,\dots\}$ |
| $\mathcal S$, $\mathcal S^+$ | trạng thái không kết thúc; cùng kết thúc | hữu hạn, $\lvert\mathcal S\rvert=n$ |
| $\mathcal A(s)$ | hành động hợp lệ | hữu hạn, khác rỗng |
| $\mathcal R$ | tập thưởng | hữu hạn $\subset\mathbb R$ |
| $S_t,A_t,R_{t+1}$; $s,a,s',r$ | biến ngẫu nhiên; giá trị | — |
| $H_t$ | lịch sử | dãy hữu hạn |
| $p(s',r\mid s,a)$, $p(s'\mid s,a)$, $r(s,a)$ | hàm động lực; xác suất chuyển; thưởng kỳ vọng | $[0,1]$; $[0,1]$; $\mathbb R$ |
| $T$ | thời điểm kết thúc lượt | $\mathbb N\cup\{\infty\}$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $[0,1)$ với tiếp diễn |
| $G_t$, $M$ | lợi tức; cận $\lvert R\rvert$ | thực; $\ge0$ |
| $\pi(a\mid s)$, $\mathbb E_\pi$ | chính sách Markov dừng; kỳ vọng | phân phối; — |
| $v_\pi(s)$, $q_\pi(s,a)$ | giá trị trạng thái; giá trị hành động | $\mathbb R$; bằng 0 tại kết thúc |
| $P^\pi$, $r^\pi$, $v$ | ma trận chuyển, véc-tơ thưởng, véc-tơ giá trị | $\mathbb R^{n\times n}$; $\mathbb R^n$ |
| $\mathrm H,\mathrm L$; $\mathrm{tim},\mathrm{cho},\mathrm{sac}$ | nhãn robot | — |

SML: $V^\pi$ ↔ $v_\pi$; $T(s,a,s')$, $R(s,a,s')$ ↔ $p(s'\mid s,a)$ và thưởng theo nhánh; $U(\tau)$ ↔ $G_0$; SML đưa $\gamma$ vào bộ MDP, Bài 03 để ngoài. Chỗ lệch deck–ghi chú: "tổng thưởng"; miền tổng (ghi chú 305 có, deck 05-04, 05-06 không); $P^\pi$, $r^\pi$ (ghi chú 516, deck 06-07 bỏ); $\mathbb E_\pi$ (ghi chú 222, deck chỉ ghi chú diễn giả 04-03); "$\pi$ Markov dừng" (ghi chú 222, deck chỉ 05-06); "phần N" và hw02.

## C. Bài tập (`exercises.md`)

03.1–03.9 giữ số hiệu và lời giải của ghi chú; 03.16–03.19 chỉ tệp này; 03.10–03.15 không chép lại.

| Số | Mạch | Mức | Dữ kiện | Trùng/mới | Năng lực |
|---|---|---|---|---|---|
| 03.1 | 2 | nhận biết | Chỉ số $R_{t+1}$; robot hai vị trí cơ hội lon khác nhau | 01-07 | trạng thái không Markov |
| 03.2 | 2 | tính toán | Bảng $p$: $p(s'\mid s,a)$ và $r(s,a)$ cho 5 cặp (2; 1; $-1/2$; 1; 0), chuẩn hóa | 02-07/07b | hàm động lực |
| 03.3 | 3 | tính toán | Dãy $(0,2,2)$, $\gamma=1/2$ và $0$; cận $\pm6$ | 03-06/06b | lợi tức, cận |
| 03.4 | 4 | tính toán | Kỳ vọng hai bước từ L bằng $9/8$, so $v_\pi(\mathrm L)=7/4$ | 04-08b | kỳ vọng cắt với giá trị |
| 03.6 | 5 | chứng minh | Bellman tại H: $v_H=2+\tfrac14v_H+\tfrac14v_L$ | 05-10b | Định lý 03.21 |
| 03.7 | 5 | chứng minh | Bellman cho $q_\pi$, chỗ dùng Markov (hw02 bài 7–8) | 05-10 | lập luận theo giả thiết |
| 03.8 | 6 | vận dụng | Luôn Chờ tại L: $P^\pi=\begin{pmatrix}1/2&1/2\\0&1\end{pmatrix}$, $r=(2,1)$, $v=(10/3,\,2)$ | 06-08/08b | đánh giá chính sách mới |
| 03.9 | 7 | vận dụng | $q_\pi(\mathrm L,\cdot)=3/4,\,15/8,\,13/8$; đối chiếu 03.8 | 07-01/02 | tổng hợp |
| 03.16 | 6 | tính toán | hw02 bài 3: ba trạng thái có hấp thụ, $R=(1,-1,0)$, $\gamma=0{,}9$, $v\approx(0{,}874;-1{,}154;0)$ | mới | ma trận ngẫu nhiên; giải hệ |
| 03.17 | 6 | chứng minh | hw02 bài 4: MDP + $\pi$ cố định cho MRP $(P^\pi,r^\pi)$ | mới | phép gộp |
| 03.18 | 2 | vận dụng | Robot ba mức pin (số liệu sư phạm): $\mathcal A(s)$, bảng $p$, chuẩn hóa, hệ Bellman | mới | mô hình hóa |
| 03.19 | 6 | vận dụng | Robot $\gamma=1$: $(I-P^\pi)\mathbf 1=0$ suy biến; thưởng trung bình dừng $1{,}25>0$ phân kỳ | mới | kiểm giả thiết 03.28 |

Độ phủ: mạch 2: 03.1, 03.2, 03.18; 3: 03.3; 4: 03.4; 5: 03.6, 03.7; 6: 03.8, 03.16, 03.17, 03.19; 7: 03.9. Nguồn hw02 (Tạ Việt Cường, 12/3/2026, bài 3, 4, 7, 8). 30 phút chữa bài: 03.16, 03.17, 03.7.

## D. Rủi ro và thứ tự

Thứ tự: ghi chú → deck (tiêu đề mạch, mở đầu, kết luận, A3, outline, storyboard, review-log) → `exercises.md` (khớp 02-07b, 03-06b, 04-08b, 05-10b, 06-08b, 07-02) → index. Rủi ro: ~67 trang cho 120 phút (có thể bỏ 07-02 trùng 06-04 hoặc gộp 04-01 vào 04-02); planning cũ (outline gọi X-01 là "slide tiêu đề phần", thiếu bảng Việt–Anh; storyboard §13 mô tả OpenRouter; review-log ghi 47 trang; `detailed-slide-plan.md`, `storyboard-mdp-replanned.md`, `note-for-author.md` lỗi thời); Bài 04 dẫn Bài 03 bằng tên; Bài 02 chưa đánh số; hình mới SVG: sơ đồ dự phòng $v_\pi$, $q_\pi$, cấu trúc chương, lưới 5×5.
