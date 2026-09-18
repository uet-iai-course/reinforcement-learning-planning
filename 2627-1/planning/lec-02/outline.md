# Bài 02 — Giao diện tác tử–môi trường

## Phạm vi

Bản viết lại từ đầu cho sinh viên năm 3 đã học học máy, học sâu, xác suất và thuật toán. Nguồn chính: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 1–27 trong tổng 58 trang; trang 28 mở Bài 03. Nguồn bài tập: `resources/hw02.pdf`, Bài 1, 2, 5, 6 và 10. Không có code demo trong phạm vi này.

Phần trình chiếu chính 120 phút; 30 phút chữa bài tập nguồn. Mục tiêu: mô tả tương tác; phân biệt trạng thái/quan sát/biểu diễn; định nghĩa và áp dụng chính sách, giá trị, mô hình; phân biệt dự đoán/điều khiển; đặc tả mê cung.

## Bảy phần

| Phần | Tên | Phút |
|---|---|---:|
| 1 | Bài toán ra quyết định tuần tự | 8 |
| 2 | Tương tác và phần thưởng | 17 |
| 3 | Trạng thái và thông tin quan sát | 28 |
| 4 | Chính sách lựa chọn hành động | 15 |
| 5 | Hàm giá trị và mô hình môi trường | 25 |
| 6 | Dự đoán, điều khiển và bài toán mê cung | 20 |
| 7 | Tổng kết và tự kiểm tra | 7 |

## Trạng thái triển khai

Đã hoàn tất 7/7 phần: 43 trang, 120 phút; đủ năm báo cáo độc lập và kiểm định lại. Giới hạn rà trực quan Codex Slides được ghi trong review-log.md.

## Trang đích

- `L02-01-01` — Bài toán ra quyết định tuần tự — PPTX trang 1 (bìa)
- `L02-01-02` — Mê cung và chuỗi quyết định — PPTX trang 25–26 (bài toán mê cung)
- `L02-01-03` — Mục tiêu học tập — Mục tiêu biên tập từ PPTX, trang 15–27; hw02, Bài 1, 2, 5, 6.
- `L02-01-04` — Nội dung bài học — Cấu trúc biên tập từ PPTX, trang 2, 15–27.
- `L02-01-05` — Câu hỏi kiểm tra — PPTX trang1–2,25; câu hỏi mở đầu về mê cung.
- `L02-02-01` — Tác tử và môi trường — PPTX trang 4 (tác tử) và 10, 20 (thành phần giao diện)
- `L02-02-02` — Một bước trong mê cung — PPTX trang 25–26 (bài toán mê cung), 7–9 (tín hiệu thưởng)
- `L02-02-03` — Thứ tự tương tác — PPTX trang 14–15 (giao diện), 16 (trạng thái/quan sát)
- `L02-02-04` — Tín hiệu học — PPTX trang 7–8 (tín hiệu học); hw02 bài 1
- `L02-02-05` — Giả thuyết điểm thưởng — PPTX trang 9 (thưởng) và 25 (mê cung với -1 mỗi bước)
- `L02-02-06` — Phản hồi trễ — PPTX trang 7–8 (phản hồi trễ), 11 (cờ)
- `L02-02-07` — Câu hỏi kiểm tra — PPTX trang 27 (quiz); bài luyện suy ra từ trang 25–26 và hw02 bài 6, 10
- `L02-03-02` — Trạng thái và quan sát — PPTX trang 16 (trạng thái/quan sát); phần biểu diễn ở trang 14-15 và 21.
- `L02-03-09` — Mẫu dữ liệu, lịch sử và quỹ đạo — PPTX trang 14–16; bổ sung theo yêu cầu, đặt sau trạng thái và quan sát
- `L02-03-06` — Quan sát đầy đủ và một phần — PPTX trang 18 (đầy đủ) và trang 19 (một phần); hình full-partial-observation.svg từ trang 25-26.
- `L02-03-04` — Tính Markov — PPTX trang 17 (Markov) và trang 18 (đầy đủ).
- `L02-03-10` — Tính Markov có hạn chế khả năng mô hình hóa? — PPTX trang 17; mở rộng trạng thái bằng lịch sử bổ sung theo yêu cầu
- `L02-03-05` — Trạng thái trong mê cung — PPTX trang 25-26 (mê cung); bài mê cung hw02 bài 10; biến thể chìa khóa là giả thiết sư phạm suy ra.
- `L02-03-07` — Biểu diễn dùng để quyết định — PPTX trang 14–15 (giao diện) và trang 21; ví dụ ghi nhớ chìa khóa trong mê cung.
- `L02-03-08` — Câu hỏi kiểm tra — PPTX trang 27 (quiz); các trường hợp từ trang 16, 18, 19 và hình full-partial-observation.svg.
- `L02-04-01` — Quy tắc lựa chọn hành động — PPTX, trang 21, 25–26; hw02, Bài 6. Ví dụ xác suất là bài luyện suy ra từ định nghĩa.
- `L02-04-02` — Ví dụ về chính sách — PPTX, trang 21, 25–26; hw02, Bài 6. Ví dụ xác suất là bài luyện suy ra từ định nghĩa.
- `L02-04-03` — Chính sách xác định — PPTX, trang 21, 25–26; hw02, Bài 6. Ví dụ xác suất là bài luyện suy ra từ định nghĩa.
- `L02-04-04` — Chính sách ngẫu nhiên — PPTX, trang 21, 25–26; hw02, Bài 6. Ví dụ xác suất là bài luyện suy ra từ định nghĩa.
- `L02-04-05` — Câu hỏi kiểm tra — PPTX, trang 21, 25–26; hw02, Bài 6. Ví dụ xác suất là bài luyện suy ra từ định nghĩa.
- `L02-05-01` — Kết quả dài hạn của chính sách — PPTX trang 10, 21, 22, 23
- `L02-05-02` — Tổng phần thưởng trên quỹ đạo — PPTX trang 26; hw02 bài 1
- `L02-05-03` — Phần thưởng tích lũy — PPTX trang 7–9, 22; hw02 bài 2
- `L02-05-04` — Giá trị kỳ vọng — PPTX trang 22; ví dụ giả định sư phạm theo hw02 bài 5
- `L02-05-05` — Hàm giá trị trạng thái — PPTX trang 16–18, 22; hw02 bài 5
- `L02-05-07` — Dự báo bước tiếp theo — PPTX trang 13, 23; hw02 bài 6
- `L02-05-08` — Mô hình chuyển và phần thưởng — PPTX trang 13, 23; hw02 bài 10
- `L02-05-09` — Câu hỏi kiểm tra — PPTX trang 13, 24, 27; hw02 bài 6
- `L02-06-01` — Hai nhiệm vụ trên mê cung — PPTX trang 24; hw02 bài 1, 5
- `L02-06-02` — Dự đoán và điều khiển — PPTX trang 24–26; hw02 bài 5
- `L02-06-03` — Đặc tả môi trường mê cung — PPTX trang 25; hw02 bài 2
- `L02-06-04` — Chính sách trên mê cung — PPTX trang 26; hw02 bài 2
- `L02-06-05` — Giá trị trên mê cung — PPTX trang 26; hw02 bài 6
- `L02-06-06` — Trạng thái kết thúc trong trò chơi — PPTX, trang 11; bài kiểm tra suy ra từ quy ước phần thưởng và điều kiện kết thúc.
- `L02-06-07` — Câu hỏi kiểm tra — PPTX trang 27; hw02 bài 10
- `L02-07-01` — Các thành phần của bài toán — PPTX trang 10, 20, 25–26; hw02 bài 1
- `L02-07-03` — Bài tập và tài liệu đọc — RL-hk2-2025-2026/resources/hw02.pdf, bài1,2,5,6,10; Sutton và Barto (2018), chương3; PPTX trang1–27.
- `L02-07-02` — Câu hỏi kiểm tra — PPTX trang 16, 19, 22–23, 27; hw02 bài 2, 5

## Ánh xạ toàn bộ nguồn

| Trang nguồn | Quyết định | Phần đích | Lý do |
|---|---|---|---|
| 1 | sửa | 1 | Cập nhật học kỳ, giữ tên bài trong phạm vi giao diện. |
| 2 | sửa | 1 | Bản đồ bảy phần đã được chấp nhận. |
| 3 | gộp | 1, 7 | Trang ôn tập chỉ có tiêu đề; mục tiêu và tự kiểm tra thay thế. |
| 4 | giữ, sửa | 1, 2 | Tác tử và quan hệ nhận thông tin–quyết định–hành động. |
| 5 | bỏ | — | Niên biểu thành tựu và ảnh robot không phục vụ mục tiêu giao diện; không giữ raster. |
| 6 | bỏ | — | Nhận định AGI và dự báo dữ liệu không thuộc phạm vi đã duyệt, thiếu căn cứ để giảng như kết luận. |
| 7–8 | gộp, sửa | 2 | So sánh tín hiệu, ảnh hưởng hành động tới dữ liệu, phân biệt phản hồi trễ với thưởng mỗi bước. |
| 9 | sửa | 2, 5 | Giả thuyết phần thưởng không phải định lý; tách trực giác tích lũy và công thức. |
| 10 | gộp | 5, 7 | Tránh lặp danh mục ba thành phần với trang 20. |
| 11 | sửa | 6 | Giữ bàn cờ kết thúc để vận dụng phần thưởng và tổng thưởng; lược cây sao lưu giá trị (ôn bài 01), vì cơ chế cập nhật nằm ngoài mục tiêu bài 02. |
| 12 | sửa | 2 | Dùng bộ điều khiển robot để minh họa ranh giới tác tử–môi trường; ví dụ xe đã bỏ theo yêu cầu. |
| 13 | sửa | 5 | Phạm vi mô hình theo tác vụ; bỏ câu hỏi tu từ về mô hình hoàn thiện thế giới. |
| 14–15 | gộp, sửa | 2 | Môi trường trả quan sát/phần thưởng, không trả hành động; chỉ số phản hồi là t+1. |
| 16 | tách | 3 | Trạng thái, quan sát và biểu diễn quyết định có miền riêng. |
| 17 | tách, sửa | 3 | Ví dụ trước phát biểu Markov có điều kiện theo hành động và lịch sử, cả trạng thái kế tiếp và thưởng. |
| 18 | sửa | 3 | Quan sát đầy đủ không tự là định nghĩa MDP, không đồng nghĩa biết mô hình. |
| 19 | tách, sửa | 3 | Cùng quan sát có thể ứng với nhiều trạng thái; lịch sử hữu hạn không mặc nhiên Markov. |
| 20–21 | tách | 4, 5 | Chính sách xác định/ngẫu nhiên; cùng ký hiệu X khi quan sát chưa đầy đủ. |
| 22 | tách | 5 | Quỹ đạo, chiết khấu, tổng và kỳ vọng trước hàm giá trị; giả thiết kỳ vọng tồn tại. |
| 23 | tách | 5 | Giữ phân phối chuyển và thưởng kỳ vọng của nguồn; KaTeX, không SVG công thức. |
| 24 | sửa | 6 | Dự đoán giữ chính sách cố định; điều khiển tìm/cải thiện chính sách. |
| 25 | giữ, tách | 1, 2, 3, 6 | Dùng mê cung sớm để chuẩn bị khái niệm; giữ hình học nguồn. |
| 26 | giữ, tách | 4, 5, 6 | Vẽ lại chính sách và giá trị; gamma=1, đích ngoài lưới, 16 bước từ đầu. |
| 27 | sửa | 3, 6 | Phân loại dựa trên thông tin quan sát và giả thiết; không giữ screenshot game. |
| hw02 Bài 1,2,5,6,10 | giữ phạm vi, sửa cách giao | 2–7 | Câu hỏi ngắn lồng trong bài, 30 phút chữa bài; Bài10 chỉ đặc tả, không Bellman. |

## Quy ước và dữ kiện xuyên suốt

- $S_t\in\mathcal S$: trạng thái môi trường; $O_t\in\mathcal O$: quan sát; $X_t\in\mathcal X$: biểu diễn dùng để quyết định; $H_t$: lịch sử trạng thái–hành động–thưởng; $H_t^O$: lịch sử quan sát–hành động–thưởng; $\tau=H_T$: quỹ đạo trạng thái hữu hạn.
- $A_t\in\mathcal A$: hành động; $R_{t+1}\in\mathbb R$: thưởng sau hành động; $t$ là chỉ số thời gian không âm.
- $\pi(a\mid x)$: chính sách trên biểu diễn; khi quan sát đầy đủ dùng $X_t=S_t$.
- $T$: thời điểm kết thúc của quỹ đạo; $G_t$: thưởng tích lũy chiết khấu; $\gamma\in[0,1]$; $v_\pi(s)$: kỳ vọng dưới chính sách cố định trong thiết lập Markov với kỳ vọng hữu hạn.
- Mê cung nguồn: 8×8, 27 ô đi được và 37 ô tường. Cột $x$ và hàng $y$ đánh số từ 0, hàng tăng xuống. Bắt đầu $(0,2)$; đích $G=(8,6)$ nằm ngoài bên phải. Tường/biên giữ nguyên vị trí, trừ bước Đông từ $(7,6)$ vào $G$; thưởng $-1$ mỗi bước kể cả bước vào đích; tới $G$ thì dừng.
- Bảng giá trị nguồn tương ứng chính sách được vẽ, chuyển xác định, $\gamma=1$: đầu $-16$, ô $(7,6)$ là $-1$, $v_\pi(G)=0$.
- Tham khảo bố cục: [SLIDE_STYLE_GUIDE.md](https://raw.githubusercontent.com/uet-iai-course/machine-learning/main/SLIDE_STYLE_GUIDE.md), chỉ nguyên tắc một ý/trang và trung tâm thị giác; mẫu và CSS cục bộ ưu tiên.
