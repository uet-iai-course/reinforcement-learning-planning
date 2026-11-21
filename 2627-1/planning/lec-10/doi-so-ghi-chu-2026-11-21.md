# Đối chiếu số hiệu ghi chú Bài 10 sau khi viết lại §4–§5 (2026-11-21)

Căn cứ: đề xuất trình bày TRPO của tác giả (`de-xuat-trinh-bay-trpo-2026-11-21.md`) và quyết định của tác giả ghi ở `gop-y-tac-gia-deck-2026-11-21.md`, mục #5: sửa ghi chú §4 theo đề xuất, gom chứng minh thành cụm "Cơ sở lý thuyết" sau bài toán miền tin cậy. Bảng dùng để sửa các dòng nguồn (số hiệu ghi chú) trong deck `lecture-10-trpo-va-ppo.html`, storyboard và `outline.md`.

## 1. Mục và chủ đề

| Mục cũ | Mục mới | `note-topic-id` | Nội dung |
|---|---|---|---|
| §4 "Hàm thay thế và chặn cải thiện" | §4 "Hàm thay thế và miền tin cậy" | — | đổi tên mục cho khớp mạch 4 của deck |
| 4.1 Bổ đề chênh lệch hiệu năng | 4.1 Đánh giá chính sách mới trước khi chạy | `lec-10-topic-10` (giữ) | thêm luồng 100 lượt, phân phối hành động và phân bố trạng thái, ba thành phần; Định nghĩa 10.18, Bổ đề 10.19, Hệ quả 10.20 |
| 4.2 Tỉ số chính sách và hàm thay thế | 4.2 Hàm thay thế | `lec-10-topic-11` (giữ) | thay $\eta_{\pi'}$ bằng $\eta_\pi$, lấy mẫu quan trọng (importance sampling), mục tiêu mẫu, bảng đã hiệu chỉnh/chưa hiệu chỉnh; Định nghĩa 10.21, Mệnh đề 10.22 |
| (mới) | 4.3 Sai số dự báo theo độ dài bước | `lec-10-topic-25` (mới) | đóng góp từng trạng thái, đẳng thức sai số, Ví dụ 10.12 (độ dài bước) |
| 4.3 Khoảng cách giữa hai chính sách | 4.4 Đo thay đổi chính sách | `lec-10-topic-12` (giữ) | Ví dụ 10.13 (sigmoid), Định nghĩa 10.23, bảng KL ba chính sách Bernoulli, KL trung bình trên chuỗi |
| 4.5 Cải thiện đơn điệu và bài toán miền tin cậy (phần định nghĩa) | 4.5 Bài toán miền tin cậy | `lec-10-topic-14` (giữ) | Định nghĩa 10.24, ví dụ $\kappa=0{,}01$ trên đoạn thẳng, đoạn dẫn "KL nhỏ → TV nhỏ → phân bố chiếm dụng ít đổi → sai số nhỏ" |
| 4.3 (Mệnh đề KL), 4.4 Chặn cải thiện, 4.5 (hai hệ quả) | 4.6 Cơ sở lý thuyết | `lec-10-topic-13` (giữ) | Mệnh đề 10.25, Bổ đề 10.26, Định lý 10.27, Ví dụ 10.14, Hệ quả 10.28, Nhận xét 10.29, Hệ quả 10.30, Hệ quả 10.31 |
| 5.1 KL bậc hai và gradient tự nhiên | 5.1 (giữ tên) | `lec-10-topic-15` (giữ) | thêm đoạn hình học tròn/elip trước Định nghĩa 10.32; hai quyết định hướng và độ dài; tỉ trọng 40/60 và 21/79 trên chuỗi |
| 5.2 TRPO thực hành | 5.2 (giữ tên) | `lec-10-topic-16` (giữ) | Thuật toán 10.37 lưu phân phối cũ, bước 2 có công thức $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$; đoạn kết TRPO giải quyết gì, còn khó khăn gì |

## 2. Bộ đếm chung (Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán)

Chỉ bảy số đổi; các số khác (10.1–10.23, 10.31–10.51) giữ nguyên.

| Số cũ | Số mới | Khối |
|---|---|---|
| Mệnh đề 10.24 | Mệnh đề 10.25 | Hai tính chất của KL (KL không âm, Pinsker) |
| Bổ đề 10.25 | Bổ đề 10.26 | Dịch chuyển phân bố chiếm dụng |
| Định lý 10.26 | Định lý 10.27 | Chặn cải thiện |
| Hệ quả 10.27 | Hệ quả 10.28 | Chặn cải thiện dạng KL trung bình |
| Nhận xét 10.28 | Nhận xét 10.29 | Định lý 1 của Schulman và cộng sự (2015) |
| Hệ quả 10.29 | Hệ quả 10.30 | Cải thiện đơn điệu qua hàm chặn dưới |
| Định nghĩa 10.30 | Định nghĩa 10.24 | Bài toán miền tin cậy |

Thay đổi nội dung (không đổi số): Định nghĩa 10.21 lấy dạng tổng $\sum_s\nu^{\mathrm{old}}(s)A_{\mathrm{old}}(s,\pi_\theta)$ làm định nghĩa, dạng tỉ số đúng khi có điều kiện hỗ trợ; Định lý 10.27 (cũ 10.26) bỏ điều kiện hỗ trợ khỏi giả thiết; Định nghĩa 10.24 (cũ 10.30) thêm giả thiết $\pi_{\mathrm{old}}(a\mid s)>0$.

## 3. Bộ đếm Ví dụ

| Số cũ | Số mới | Ghi chú |
|---|---|---|
| Ví dụ 10.1–10.10 | giữ nguyên | |
| Ví dụ 10.11 (Đổi chính sách trên chuỗi hai trạng thái) | Ví dụ 10.11 (Hai chính sách mới trên chuỗi hai trạng thái) và Ví dụ 10.12 | 10.11 giữ giá trị thật của $\pi'$, $\tilde\pi$ và thêm luồng 100 lượt; phép cộng theo bước thời gian chuyển ra văn bản ngay sau ví dụ; khai triển $\Delta J=0{,}8\Delta p_A+1{,}35\Delta p_B+2{,}7\Delta p_A\Delta p_B$ và đoạn thẳng tới $\tilde\pi$ chuyển sang Ví dụ 10.12; sai số $0{,}036$ chuyển sang §4.2–4.3 |
| (mới) | Ví dụ 10.12 (Độ dài bước trên đoạn thẳng từ $\pi$ tới $\tilde\pi$) | bảng $t=0;0{,}25;0{,}5;1$ |
| Ví dụ 10.12 (Chặn cải thiện trên chuỗi hai trạng thái) | Ví dụ 10.14 | nội dung giữ |
| Ví dụ 10.13 (Cùng một bước tham số, hai khoảng cách chính sách) | Ví dụ 10.13 (Cùng một bước tham số, hai mức thay đổi chính sách) | thay điểm $p=0{,}99$ bằng $\theta=5$ theo đề xuất; ví dụ đặt trước định nghĩa KL nên chỉ tính $\Delta p$ ($0{,}2311$ và $0{,}0042$); KL $0{,}1201$ và $0{,}00245$ nằm ở đoạn sau Định nghĩa 10.23 |
| Ví dụ 10.14 (Ma trận Fisher của bài toán một bước) | Ví dụ 10.15 | |
| Ví dụ 10.15 (Bước gradient tự nhiên trên bài toán một bước) | Ví dụ 10.16 | |
| Ví dụ 10.16 (Hai vòng gradient liên hợp) | Ví dụ 10.17 | |
| Ví dụ 10.17 (Hai hàm thay thế mẫu trên bài toán một bước) | Ví dụ 10.18 | §6 |
| Ví dụ 10.18 (Bốn mẫu) | Ví dụ 10.19 | §6 |
| Ví dụ 10.19 (Một lần điều chỉnh hệ số phạt) | Ví dụ 10.20 | §6 |
| Ví dụ 10.20 (Một mini-batch tính tay) | Ví dụ 10.21 | §6 |
| Ví dụ 10.21 (Chẩn đoán trên đoạn phẳng) | Ví dụ 10.22 | §6 |
| Ví dụ 10.22 (Cắt mất mát giá trị trên một mẫu) | Ví dụ 10.23 | §6 |

Bài tập: không đổi số (10.1–10.17, 10.22, 10.23).

## 4. Số dẫn hiện có trong deck cần đổi

Đếm trên `lecture-10-trpo-va-ppo.html` lúc lập bảng: Mệnh đề 10.24 (1 lần), Bổ đề 10.25 (1), Định lý 10.26 (3), Hệ quả 10.27 (2), Nhận xét 10.28 (2), Hệ quả 10.29 (2), Định nghĩa 10.30 (1), Ví dụ 10.12 (2), Ví dụ 10.13 (2, nội dung đổi), Ví dụ 10.17 (1), Ví dụ 10.18 (2); Ví dụ 10.11 (8 lần) cần xem từng chỗ: chỗ dẫn khai triển $\Delta J$ hay đoạn thẳng tới $\tilde\pi$ đổi thành Ví dụ 10.12.
