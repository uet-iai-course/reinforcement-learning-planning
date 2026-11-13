# Bài 02 — Giao diện tác tử–môi trường

Dàn ý cập nhật trong đợt sửa 2026-10-12 (giai đoạn II: bộ trang chiếu), khớp deck `2627-1/lecture-02-giao-dien-tac-tu-moi-truong.html` (66 trang, 7 mạch, sau vòng biên tập theo năm vai rà soát) và ghi chú bài giảng đã commit `materials/lec-02/lecture-note.md` (commit `39a1bd1`). Deck là bản tóm tắt của ghi chú; số hiệu kết quả, ví dụ và bài tập theo ghi chú.

## Phạm vi và nguồn

- Đối tượng: sinh viên năm 3 đã học học máy, xác suất, thuật toán; đã học Bài 01 (vòng tương tác, lượt, lợi tức không chiết khấu, chính sách và giá trị trên lịch sử).
- Nguồn chính: bài giảng gốc (2025–2026), `lecture2-3-MDPswithKeyConcepts.pptx`, trang 1–27; trang 28 mở Bài 03. Bài tập tuần 2 (2025–2026), bài 1, 2, 5, 6, 10.
- Nguồn đối chiếu: Sutton và Barto (2018), §3.1–3.5, §13.1, §17.3–17.4; Russell và Norvig (2020), §17.1.1; Puterman (1994), §2.1; giáo trình *Học máy thống kê*, mục "Giới thiệu về quá trình quyết định Markov".
- Thời lượng: deck 120 phút; 30 phút chữa bài tập. Không có code demo trong deck.

## Khung lý thuyết chung

- **Vấn đề trung tâm.** Đặc tả chuỗi quyết định trên mê cung $8\times8$ (và mê cung đích–hố) sao cho đánh giá và so sánh được các cách đi.
- **Đối tượng và ký hiệu chung.** $t\in\{0,1,2,\dots\}$; $T$ thời điểm kết thúc; $S_t\in\mathcal S$ (chưa kết thúc), $\mathcal S^+$ thêm trạng thái kết thúc; $O_t\in\mathcal O$; $X_t\in\mathcal X$; $A_t\in\mathcal A$, $\mathcal A(x)$ hành động hợp lệ; $R_{t+1}\in\mathcal R\subset\mathbb R$ là phần thưởng của chuyển từ $t$ sang $t+1$; $H_t$ lịch sử trạng thái, $\tau=H_T$; $\pi(a\mid x)$; $\gamma\in[0,1]$; $G_t$, $G_T=0$; $v_\pi(s)$, $\mathbb E_\pi$ theo chính sách và động lực; $p(s',r\mid s,a)$, $p(s'\mid s,a)$, $r(s,a)$; $c$ chi phí mỗi bước, $c_{\mathrm H}$ phạt hố (ghi chú bài giảng còn viết $h$; chữ $h$ trên deck chỉ dành cho lịch sử); nhãn nút $\mathrm S,\mathrm H,\mathrm G$ chữ đứng. Ô ghi (cột, hàng), đánh số từ $0$, hàng tăng xuống dưới; trạng thái mê cung có chìa khóa ghi (ô, $k$). Quan sát của cảm biến bốn ô kề là bộ mã, $O_t\in\{0,1\}^4$; biểu diễn có nhớ $X_t=(O_t,A_{t-1},O_{t-1})$, cửa sổ độ dài $m$ (chữ $k$ chỉ dành cho bit chìa khóa; ghi chú dùng $k$ cho cả hai). Tên hướng (Bắc, Đông, Nam, Tây) viết ngoài KaTeX.
- **Giả thiết.** Tập trạng thái, phần thưởng đếm được; tính Markov của trạng thái được chọn; môi trường dừng; chính sách dừng; kỳ vọng hữu hạn ($\gamma<1$ và phần thưởng bị chặn, hoặc $\gamma=1$ và $\mathbb E[T-t]<\infty$); riêng ngưỡng đổi hành vi: $c\ge0$, $\gamma=1$, chuyển tất định, tác tử tối ưu.
- **Chuỗi định nghĩa → kết quả → phương pháp.** Mẫu chuyển (02.1) → biểu diễn (02.2), lịch sử (02.3), quan sát đầy đủ (Nhận xét 02.4), tính Markov (02.5), lịch sử là trạng thái Markov (Mệnh đề 02.6) → chính sách trên biểu diễn (02.8) → lợi ích cộng và ưu tiên dừng (02.10) → trọng số hình học (Định lý 02.11) → lợi tức (02.12), truy hồi và chặn (Mệnh đề 02.13) → hàm giá trị (02.14) → hàm động lực (02.16), dự đoán và điều khiển (Nhận xét 02.17) → ngưỡng đổi hành vi (Mệnh đề 02.18). Bài không có thuật toán.
- **Giới hạn áp dụng.** Giá trị chỉ tính được bằng liệt kê quỹ đạo; cách tính tổng quát (phương trình Bellman) thuộc Bài 03, quy hoạch động thuộc Bài 04. Quan sát một phần chỉ được xử lý bằng chính sách ngẫu nhiên hoặc cửa sổ hữu hạn trên ví dụ cụ thể.

## Bảy mạch

| N | Tên mạch (trùng mục ghi chú) | Trang tiêu đề mạch | Mục ghi chú | Phút |
|---|---|---|---|---:|
| 1 | Mở đầu (bìa là trang tiêu đề) | `L02-01-01` | Mục tiêu, Kiến thức tiên quyết | 9 |
| 2 | Vòng tương tác và tín hiệu thưởng | `L02-02-00`, `id="mach-2"` | §1 | 16 |
| 3 | Thông tin khả dụng và tính Markov | `L02-03-00`, `id="mach-3"` | §2 | 27 |
| 4 | Quy tắc chọn hành động | `L02-04-00`, `id="mach-4"` | §3, Tình huống 02.2 | 15 |
| 5 | Lợi tức, hàm giá trị và hàm động lực | `L02-05-00`, `id="mach-5"` | §4 | 27 |
| 6 | Thiết kế phần thưởng | `L02-06-00`, `id="mach-6"` | §5 | 14 |
| 7 | Tổng kết và chuyển tiếp | `L02-07-00`, `id="mach-7"` | Tóm tắt chương | 12 |

Tổng 120 phút.

## Mục tiêu học tập (khớp ghi chú)

1. Ghi một mẫu chuyển $(O_t,A_t,R_{t+1},O_{t+1})$ với chỉ số thời gian đúng, tách thành phần của tác tử và của môi trường (Bài tập 02.1, 02.9, 02.14).
2. Phân biệt $S_t$, $O_t$, $X_t$; kiểm tra và sửa tính Markov bằng cách mở rộng trạng thái (Bài tập 02.2, 02.3, 02.11).
3. Viết chính sách xác định và ngẫu nhiên trên một biểu diễn, tính xác suất của một dãy hành động (Bài tập 02.4, 02.13, 02.20).
4. Tính lợi tức chiết khấu, $v_\pi(s)$; đọc hàm động lực $p$; giải thích trọng số hình học (Bài tập 02.5–02.7, 02.10, 02.12, 02.15–02.22).
5. Tìm ngưỡng chi phí làm tác tử tối ưu đổi hành vi; nêu giả thiết khi phần thưởng mỗi bước đổi dấu (Bài tập 02.8, 02.10, 02.21–02.24).

Danh sách bài tập chép đúng phần Mục tiêu học tập của ghi chú (đợt sửa 2026-11-13, theo bộ `exercises.md` đánh số lại 2026-11-12): 02.1–02.13 nằm trong ghi chú, 02.14–02.24 trong `exercises.md`.

## Ví dụ xuyên suốt

- **Mê cung $8\times8$** (bài giảng gốc, trang 25–26): 27 ô đi được, xuất phát $(0,2)$, đích $\mathrm G=(8,6)$ sau bước Đông từ $(7,6)$; tường hoặc biên giữ tác tử đứng yên; $-1$ mỗi bước kể cả bước vào $\mathrm G$; đường 16 bước. Dùng ở `L02-01-02`, `02-02`, `02-03`, `02-05`, `02-07`, `03-02`, `03-13`, `03-06`, `03-08`, `04-01`, `04-02`, `04-07`, `04-08`, `05-01`, `05-15`, `05-13`, `05-08`, `05-17`, `05-18`. Mỗi lần dùng trả lời một câu hỏi mới: một bước (mẫu chuyển), hai đường 16/18 bước (giả thuyết phần thưởng), mã bốn ô kề (biểu diễn, quan sát một phần), ba bước đầu (lịch sử), chính sách mũi tên (chính sách nguồn, tên theo ghi chú Mục 3), xác suất dãy hành động, hai ô cùng mã (chính sách ngẫu nhiên), ba bước cuối (lợi tức), bảng giá trị nguồn ($-16$), hai hành động tại $(4,1)$ ($-11$ và $-13$, điều khiển), bước trượt (hàm động lực).
- **Mê cung có chìa khóa** (biến thể sư phạm của mê cung $8\times8$): chìa khóa ở ngõ cụt $(4,2)$, cửa ở lối $(7,6)\to\mathrm G$. Dùng ở `L02-03-14`, `03-04`, `03-10`, `03-15`, `03-16`.
- **Mê cung đích–hố** (ví dụ do người dùng duyệt, số liệu sư phạm tự xây dựng): $-c$ mỗi bước, $+10$ khi vào $\mathrm G$, phạt $c_{\mathrm H}$ khi vào $\mathrm H$ (ghi chú bài giảng và `exercises.md` cùng ký hiệu); đường ngắn nhất 6 bước tới $\mathrm G$, 2 bước tới $\mathrm H$. Dùng ở mạch 6 và bài tập tổng hợp `L02-07-04`/`07-07` ($\gamma=0{,}9$).
- **Ví dụ một lần:** robot (ranh giới), ván cờ (phần thưởng trễ), hai chuỗi $(2,0)$, $(1,1)$ (ưu tiên dừng), môi trường hai nhánh (kỳ vọng), Gymnasium `env.step` (mẫu chuyển trong thực hành).
- **Hành lang pin** (Tình huống 02.1 của ghi chú, robot giao hàng năm ô với mức pin): chỉ có trong ghi chú; deck không có trang riêng, vì mạch 5 đã đủ thời lượng. Ghi trong review-log.

## Bảng thuật ngữ Việt–Anh

| Tiếng Việt | Tiếng Anh | Ghi chú |
|---|---|---|
| tác tử | agent | không dùng "tác nhân" |
| môi trường | environment | |
| hành động | action | |
| phần thưởng | reward | không dùng "điểm thưởng" |
| mẫu chuyển | transition | Định nghĩa 02.1 |
| trạng thái | state | |
| quan sát | observation | |
| biểu diễn | representation | Định nghĩa 02.2 |
| lịch sử | history | lịch sử trạng thái, Định nghĩa 02.3 |
| quỹ đạo | trajectory | $\tau=H_T$ |
| lượt | episode | không dùng "tập", "hồi" |
| quan sát đầy đủ | full observability | Nhận xét 02.4 |
| quan sát một phần | partial observability | |
| tính Markov | Markov property | Định nghĩa 02.5 |
| chính sách | policy | |
| chính sách xác định | deterministic policy | dạng chốt cho học phần; giáo trình *Học máy thống kê*: "chính sách đơn định" |
| chính sách dừng | stationary policy | quy tắc không đổi theo $t$; khác "dừng thuật toán" |
| môi trường dừng | (stationary environment) | xác suất chuyển không đổi theo $t$ |
| chính sách ngẫu nhiên | stochastic policy | |
| lợi ích | utility | |
| ưu tiên dừng | stationary preference | Định nghĩa 02.10 |
| hệ số chiết khấu | discount factor | $\gamma$ |
| lợi tức | return | không dùng "tổng thưởng", "phần thưởng tích lũy" |
| cận thị | myopic | $\gamma=0$ |
| hàm giá trị trạng thái | state-value function | $v_\pi$ |
| hàm động lực | dynamics function | $p(s',r\mid s,a)$, Định nghĩa 02.16; mô hình đúng của môi trường |
| mô hình | model | mô hình tác tử mang theo, xấp xỉ $\hat p$ của $p$ |
| dự đoán | prediction | Nhận xét 02.17 |
| điều khiển | control | |
| giả thuyết phần thưởng | reward hypothesis | |
| phần thưởng trễ | delayed reward | không dùng "phản hồi trễ" làm thuật ngữ (đợt sửa 2026-11-13, theo ghi chú) |
| nhiệm vụ tiếp diễn | continuing task | $T=\infty$, Định nghĩa 02.12 |
| chân trời hiệu dụng | effective horizon | $1/(1-\gamma)$; không dùng "chân trời có hiệu lực" |
| chính sách mũi tên | (tên ví dụ) | chính sách xác định trên tọa độ của hình bài giảng gốc, trang 26 |
| học có giám sát, học không giám sát | supervised learning, unsupervised learning | |
| quá trình quyết định Markov | Markov decision process, MDP | Bài 03 |
| quá trình quyết định Markov quan sát một phần | partially observable Markov decision process, POMDP | ghi chú diễn giả `L02-03-06` |

## Ánh xạ nguồn

| Trang nguồn | Quyết định | Mạch | Ghi chú |
|---|---|---|---|
| 1 | sửa | 1 | Bìa theo chuẩn: tên bài, câu luận đề, đơn vị. |
| 2–3 | gộp | 1 | Thay bằng "Nội dung" bảy mạch và "Tiên quyết và quy ước". |
| 4 | giữ, sửa | 2 | Ranh giới tác tử–môi trường (`L02-02-01`). |
| 5–6 | bỏ | — | Niên biểu, ảnh raster, nhận định AGI ngoài phạm vi (giữ quyết định cũ). |
| 7–8 | gộp | 2 | Tín hiệu học, phần thưởng trễ (`L02-02-04`, `02-06`). |
| 9 | sửa | 2 | Giả thuyết phần thưởng là giả thuyết, không phải định lý (`L02-02-05`). |
| 10 | gộp | 5, 7 | Ba thành phần chính sách, giá trị, mô hình (`L02-05-01`, bảng tổng kết). |
| 11 | gộp | 2 | Ví dụ ván cờ thưởng khi kết thúc (`L02-02-06`). |
| 12 | sửa | 2 | Robot làm ví dụ ranh giới. |
| 13 | sửa | 5 | Mô hình theo tác vụ; hàm động lực (`L02-05-08`). |
| 14–15 | gộp, sửa | 2, 3 | Mẫu chuyển, chỉ số $t+1$ (`L02-02-03`); lịch sử (`L02-03-09`). |
| 16 | tách | 3 | Trạng thái, quan sát, biểu diễn (`L02-03-02`, `03-11`, `03-12`). |
| 17 | tách, sửa | 3 | Ví dụ chìa khóa trước định nghĩa Markov; mở rộng bằng lịch sử (`L02-03-14`, `03-04`, `03-10`). |
| 18–19 | sửa | 3 | Quan sát đầy đủ và một phần (`L02-03-06`). |
| 20–21 | tách | 4 | Chính sách xác định, ngẫu nhiên trên biểu diễn. |
| 22 | tách | 5 | Lợi tức, chiết khấu, kỳ vọng, hàm giá trị. |
| 23 | sửa | 5 | Hàm động lực $p$ chữ thường. |
| 24 | sửa | 5 | Dự đoán và điều khiển (`L02-05-17`). |
| 25–26 | giữ | 1–5 | Mê cung, chính sách, bảng giá trị (`L02-05-13`). |
| 27 | sửa | 3, 7 | Phân loại quan sát; câu hỏi tự kiểm tra. |
| hw02 bài 1, 2, 5, 6, 10 | phân bổ | 2–7 | Theo ghi chú: bài 2 → Mục 2, bài 5 → Bài tập 02.10, bài 6 → Tình huống 02.2, bài 10 → Tình huống 02.1. Từ 2026-11-12, `exercises.md` (02.14–02.24) chỉ lấy bài tập chương 3 của Sutton và Barto (2018), không còn bài của hw02; bảng `Mạch | Bài tập` ở `L02-07-03` chép bảng mạch của `exercises.md` hiện tại (đợt sửa 2026-11-13); bài 3, 4, 7, 8, 9 cho Bài 03. |
| (bổ sung) | thêm | 5 | Ưu tiên dừng và trọng số hình học: Russell và Norvig (2020), §17.1.1; chứng minh trong ghi chú. |
| (bổ sung) | thêm | 6 | Mê cung đích–hố, ngưỡng $c^*$: ví dụ do người dùng duyệt. |

## Phân loại chủ đề (chuyển từ ghi chú, 2026-11-08)

Ngày 2026-11-04, người dùng quyết định bỏ mục "Bản đồ chủ đề" khỏi ghi chú bài giảng và giữ phân loại bốn nhóm trong `outline.md`; các chú thích `note-topic-id` vẫn nằm trong thân ghi chú. Mỗi hàng dưới đây chép từ khối tương ứng của mục "Bản đồ chủ đề" trong ghi chú bản HEAD trước đợt siết 2026-11-08.

| `note-topic-id` | Chủ đề | Nhóm | Mạch | Vai trò trong mạch | Kết nối vào → ra | Nguồn |
|---|---|---|---|---|---|---|
| `lec-02-topic-01` | Mẫu chuyển và chỉ số thời gian | `cốt lõi` | `## 1.` (mạch 2) | cố định thứ tự quan sát, hành động, phần thưởng của một bước | vòng tương tác (Định nghĩa 01.1) → lịch sử ở Mục 2, lợi tức ở Mục 4 | bài giảng gốc, trang 4, 7–11, 14–15; Sutton và Barto (2018), §3.1 |
| `lec-02-topic-03` | Trạng thái, quan sát và biểu diễn | `cốt lõi` | `## 2.` (mạch 3) | tách điều môi trường ở, điều tác tử nhận và điều tác tử dùng để quyết định | Định nghĩa 01.2 → đầu vào của chính sách ở Mục 3 | bài giảng gốc, trang 16, 18–19, 25–27; Bài tập tuần 2 (2025–2026), bài 2 |
| `lec-02-topic-05` | Tính Markov, lịch sử trạng thái và mở rộng trạng thái | `cốt lõi` | `## 2.` (mạch 3) | điều kiện để trạng thái hiện tại đủ cho dự báo một bước, và cách khôi phục điều kiện đó | lịch sử của Bài 01; hai ô cùng quan sát → giả thiết của hàm giá trị, hàm động lực và MDP ở Bài 03 | bài giảng gốc, trang 15, 17; Sutton và Barto (2018), §3.1 (trang 49), §17.3 |
| `lec-02-topic-06` | Chính sách trên biểu diễn | `cốt lõi` | `## 3.` (mạch 4) | viết cách chọn hướng thành đối tượng toán học trên dữ liệu tác tử thật sự có | Định nghĩa 01.11; biểu diễn $X_t$ → kỳ vọng $\mathbb E_\pi$ ở Mục 4 | bài giảng gốc, trang 20–21, 26; Sutton và Barto (2018), §3.5; Bài tập tuần 2, bài 6 |
| `lec-02-topic-07` | Ưu tiên dừng và trọng số hình học | `bổ sung` | `## 4.` (mạch 5) | chứng minh dạng $\gamma^k$ của trọng số chiết khấu từ ưu tiên dừng, khi lợi ích có dạng cộng | lợi tức của Bài 01 → Định nghĩa 02.12 | Russell và Norvig (2020), §17.1.1, trang 565–566 (phát biểu không kèm chứng minh) |
| `lec-02-topic-08` | Lợi tức chiết khấu | `cốt lõi` | `## 4.` (mạch 5) | đo cả chuỗi phần thưởng sau một hành động bằng một số, kể cả khi tương tác không kết thúc | Định nghĩa 01.8, Định lý 02.11 → hàm giá trị; phương trình Bellman ở Bài 03 | bài giảng gốc, trang 7–9, 22; Sutton và Barto (2018), §3.3–3.4; Bài tập tuần 2, bài 5 |
| `lec-02-topic-09` | Từ lợi tức của một lượt đến kỳ vọng | `cầu nối` | `## 4.` (mạch 5) | khoảng trống giữa lợi tức của một lượt và một con số đại diện cho trạng thái khi có yếu tố ngẫu nhiên | Định nghĩa 02.12 → Định nghĩa 02.14 | bài giảng gốc, trang 22 (câu hỏi vì sao cần kỳ vọng) |
| `lec-02-topic-10` | Hàm giá trị trạng thái | `cốt lõi` | `## 4.` (mạch 5) | đánh giá mỗi trạng thái dưới một chính sách cố định | Định nghĩa 01.12, tính Markov → dự đoán, điều khiển; Bài 03 | bài giảng gốc, trang 22, 24, 26; Sutton và Barto (2018), §3.5 |
| `lec-02-topic-11` | Hàm động lực | `cốt lõi` | `## 4.` (mạch 5) | dự báo một bước của môi trường, tách khỏi đánh giá dài hạn | Định nghĩa 01.14, tính Markov → MDP (Bài 03), quy hoạch động (dynamic programming) ở Bài 04 | bài giảng gốc, trang 10, 13, 23; Sutton và Barto (2018), §3.1 |
| `lec-02-topic-12` | Thiết kế phần thưởng và ngưỡng đổi hành vi | `cốt lõi` | `## 5.` (mạch 6) | dự báo hành vi của tác tử tối ưu khi người thiết kế đổi phần thưởng; liên hệ với khuyến khích và chế tài | lợi tức với $\gamma=1$ → phần thưởng của các bài thực hành Bài 04–07 | ví dụ mê cung đích–hố do người dùng duyệt; Sutton và Barto (2018), §3.2, §17.4 |
| `lec-02-topic-14` | Quan sát một phần và chính sách ngẫu nhiên | `bổ sung` | `## Tình huống áp dụng và ứng dụng` | hậu quả khi biểu diễn gộp hai trạng thái cần hai hành động khác nhau | Nhận xét 02.4, Định nghĩa 02.8 → chính sách ngẫu nhiên và biểu diễn có bộ nhớ ở các bài sau | Sutton và Barto (2018), §13.1, Ví dụ 13.1; Bài tập tuần 2, bài 6 |
| `lec-02-topic-15` | Trạng thái Markov từ lịch sử quan sát; thiết kế tín hiệu thưởng | `đọc thêm` | `## Hướng dẫn đọc thêm và tài liệu tham khảo` | mở rộng Mệnh đề 02.6 sang lịch sử của tác tử và Mục 5 sang thiết kế phần thưởng thực tế | Mệnh đề 02.6, Mệnh đề 02.18 → quan sát một phần trong Học tăng cường sâu | Sutton và Barto (2018), §17.3 (trang 464–468), §17.4 (trang 469–470) |

Ghi chú không có `lec-02-topic-02`, `topic-04`, `topic-13`; các id `lec-02-part-01` … `part-07` gắn với khối mở đầu, năm mục nội dung và Tóm tắt, không có hàng trong bảng trên.

## Bản đồ chủ đề (`note-topic-id`) ↔ trang

| `note-topic-id` | Chủ đề | Trang |
|---|---|---|
| `lec-02-part-01` | Mục tiêu, tiên quyết | `L02-01-01` … `01-02` |
| `lec-02-part-02`, `lec-02-topic-01` | Mẫu chuyển, phần thưởng | `L02-02-00` … `02-06` |
| `lec-02-part-03`, `topic-03`, `topic-05` | Trạng thái, quan sát, biểu diễn, lịch sử, Markov | `L02-03-00` … `03-16` |
| `lec-02-part-04`, `topic-06`, `topic-14` | Chính sách; hai ô cùng mã | `L02-04-00` … `04-05` |
| `lec-02-part-05`, `topic-07` … `topic-11` | Ưu tiên dừng, lợi tức, kỳ vọng, giá trị, hàm động lực | `L02-05-00` … `05-18` |
| `lec-02-part-06`, `topic-12` | Thiết kế phần thưởng | `L02-06-00` … `06-07` |
| `lec-02-part-07`, `topic-15` | Tóm tắt, đọc thêm | `L02-07-00` … `07-03` |
