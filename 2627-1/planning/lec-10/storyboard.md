# Storyboard Bài 10: TRPO và PPO

Giai đoạn II, viết lại 2026-11-04 trên ghi chú bài giảng đã duyệt (commit `1c9ef05`; commit `567c96c` chỉ bỏ mục "Bản đồ chủ đề", số hiệu khối không đổi) và kế hoạch bộ trang chiếu đã duyệt, với phương án nén về 90 trang; đợt sửa sau cổng storyboard (cùng ngày) tách lại bốn trang, còn 94 trang. Bản viết tách thêm `L10-212b`, `L10-702b` (95 → 97 trang). Đợt sửa D1 (sau năm báo cáo rà soát độc lập, cùng ngày) tách `L10-412b`, `L10-502b`, `L10-611b`, `L10-617b`: 101 trang, tổng vẫn 120 phút; mục "Đợt sửa D1" cuối tệp ghi thay đổi từng trang và số đo cuối. Khung lý thuyết chung, bảng thuật ngữ, ánh xạ chủ đề và sai khác có chủ ý nằm trong `outline.md`. Bản storyboard cũ (42 trang, còn trong git) chỉ dùng để ghi quyết định so với bộ trang chiếu cũ.

Ký hiệu cột "quyết định": so với bộ trang chiếu cũ (mã cũ trong ngoặc) và với nguồn; `thêm` là trang không có tương ứng trong bộ cũ. Âm tiết: số từ tách theo khoảng trắng, không tính tiêu đề, KaTeX, ô số của bảng, nhãn hình và ghi chú diễn giả; số trong storyboard là ước lượng trên câu dự kiến, tác tử soạn đếm lại trên HTML. Ghi chú diễn giả mọi trang 40–150 âm tiết (trang tiêu đề mạch 40–100; chứng minh và lời giải đến khoảng 250), mở bằng đối tượng toán học hoặc kết quả kế thừa.

## Bản đồ mạch

**Bài toán trung tâm.** Giảm phương sai của ước lượng gradient chính sách mà vẫn giữ kỳ vọng của nó, và dùng lại dữ liệu của $\pi_{\mathrm{old}}$ để chọn một bước cập nhật lớn mà chính sách mới không kém chính sách cũ.

| mạch | loại | chức năng | đầu vào | đầu ra | đóng góp cho bài toán trung tâm | trang tiêu đề mạch | trang | phút |
|---|---|---|---|---|---|---|---:|---:|
| 1. Mở đầu và hai giới hạn của REINFORCE | mở bài | Ký hiệu, nhắc lại Bài 03–09; mục tiêu; nội dung; hai ví dụ định lượng; bài toán và khung hai hàng | REINFORCE, (G1)–(G4), hàm điểm (Bài 09); $q_\pi$, $v_\pi$ (Bài 03) | Hai nhu cầu: giảm phương sai giữ kỳ vọng; bước lớn bằng dữ liệu cũ; năm câu trả lời có điều kiện | Phát biểu bài toán | không có (bìa `L10-101` là trang tiêu đề của mạch mở đầu) | 10 | 12 |
| 2. Đường cơ sở, hàm lợi thế và actor–critic | khái niệm, kết quả, thuật toán | Trừ đường cơ sở; đặt tên lợi thế; bootstrap bằng critic; hai thuật toán | $\operatorname{Var}$ tăng $\tfrac49\to\tfrac{16}9$ (`L10-106`); lượt hành lang (`L10-107`) | $\widehat g_b$ không chệch; $\nabla J$ dạng lợi thế; $\mathbb E[\delta_t\mid s,a]=A_\pi$ khi critic đúng; Thuật toán 10.6, 10.9; $\delta_0=0{,}35\ne0{,}4$ khi critic sai | Hai đầu của hệ số nhân với hàm điểm: Monte Carlo và một bước | `L10-200`, `id="mach-2"` | 18 | 23 |
| 3. Ước lượng lợi thế tổng quát | khái niệm, kết quả, thuật toán | Nối $\delta_t$ và $G_t-\hat v$ bằng $\lambda$; điều kiện γ-just; GAE trên đoạn thu có cờ | Hai ước lượng $0{,}35$, $1{,}7$ của cùng $A_\pi(s_A,1)=0{,}4$ | $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$; Thuật toán 10.16 với $Z$, $U$; $V^{\mathrm{targ}}_t$ | Hoàn tất nửa thứ nhất; giao $\widehat A_t$, $V^{\mathrm{targ}}_t$ cho mạch 6 | `L10-300`, `id="mach-3"` | 10 | 14,5 |
| 4. Hàm thay thế và chặn cải thiện | kết quả | Hiệu hiệu năng; hàm thay thế; TV và KL; chặn cải thiện; cải thiện đơn điệu; miền tin cậy | Giới hạn thứ hai (`L10-108`): lượt cũ không cho mẫu của gradient sau một bước | Bài toán miền tin cậy với mức giảm bị chặn khi giải chính xác (Hệ quả 10.31) | Căn cứ định lượng cho việc giới hạn bước | `L10-400`, `id="mach-4"` | 16 | 22,5 |
| 5. TRPO và gradient tự nhiên | kết quả, thuật toán | KL bậc hai, Fisher, gradient tự nhiên, gradient liên hợp, tìm kiếm lùi, TRPO | Bài toán miền tin cậy phi tuyến (`L10-411`) | Thuật toán 10.37; TRPO thực hành chỉ bảo đảm KL trung bình mẫu $\le\kappa$ và hàm thay thế mẫu tăng | Giải xấp xỉ bài toán của mạch 4 | `L10-500`, `id="mach-5"` | 12 | 13,5 |
| 6. Tối ưu chính sách gần kề (PPO) | khái niệm, kết quả, thuật toán | Mục tiêu cắt, PPO-Penalty, mất mát tổng, chẩn đoán, thuật toán, siêu tham số, cài đặt, phạm vi lý thuyết | Chi phí bậc hai của TRPO; hàm thay thế mẫu tuyến tính theo $\rho_t$; $\widehat A_t$, $V^{\mathrm{targ}}_t$ (mạch 3) | Thuật toán 10.49; mục tiêu cắt không chặn KL; approxKL chỉ không chệch khi $\theta$ không phụ thuộc mẫu | Hai hàng gặp nhau | `L10-600`, `id="mach-6"` | 23 | 25,5 |
| 7. Tổng kết và chuyển tiếp | kết bài | Ba bảng tổng kết, bài tổng hợp, trả lời bài toán, câu hỏi, bài về nhà, nối Bài 11 | Kết quả mạch 2–6 | Câu trả lời có điều kiện; giới hạn dữ liệu theo chính sách sang Bài 11 | Tổng hợp, không khái niệm mới | `L10-700`, `id="mach-7"` | 12 | 9 |
| **Tổng** | | | | | | | **101** | **120** |

Mã trang tiêu đề mạch theo quy ước `<tiền tố mạch>00`: mã trang của bài có dạng `L10-NXX` với $N$ là số mạch, nên trang tiêu đề mạch $N$ là `L10-N00`. Số mạch $N$ trùng số mục $N$ của ghi chú với $N=2,\dots,7$.

## Danh sách trang và thời lượng

| mạch | mã | tiêu đề | loại | khối ghi chú | hình | phút |
|---|---|---|---|---|---|---:|
| 1 | `L10-101` | TRPO và PPO | bìa | §1.1 | — | 0,5 |
| 1 | `L10-102` | Tiên quyết và quy ước | tiên quyết (Ký hiệu) | Bảng ký hiệu, Quy ước đọc | — | 1,5 |
| 1 | `L10-103` | Tiên quyết và quy ước | tiên quyết (Nhắc lại) | Kiến thức tiên quyết | — | 1,5 |
| 1 | `L10-104` | Mục tiêu học tập | mục tiêu | Mục tiêu học tập 1–7 | — | 1 |
| 1 | `L10-105` | Nội dung | nội dung | Bảy phần của chương | — | 0,5 |
| 1 | `L10-106` | Ví dụ: bài toán một bước, phương sai của REINFORCE | ví dụ dẫn nhập | Ví dụ 10.1 | `img/lec-09/one-step-card.svg` | 2 |
| 1 | `L10-107` | Ví dụ: hành lang ngắn, một lượt REINFORCE | ví dụ dẫn nhập | Ví dụ 10.2 | `img/lec-09/short-corridor.svg` | 2 |
| 1 | `L10-108` | Ví dụ: hành lang ngắn, một bước theo đúng gradient | ví dụ dẫn nhập | §1.1 sau Ví dụ 10.2 | — | 1 |
| 1 | `L10-109` | Vấn đề trung tâm | vấn đề trung tâm | §1.1, năm câu trả lời | — | 1,5 |
| 1 | `L10-110` | Hệ số của hàm điểm và độ lớn bước | khung chung | §1.1, hình | `img/lec-10/central-problem.svg` | 0,5 |
| 2 | `L10-200` | 2. Đường cơ sở, hàm lợi thế và actor–critic | tiêu đề mạch | §2 | — | 0,5 |
| 2 | `L10-201` | Mức so sánh của trạng thái | vấn đề, trực giác | §2.1 đoạn đầu | — | 1 |
| 2 | `L10-202` | Ví dụ: ba đường cơ sở trên bài toán một bước | ví dụ | Ví dụ 10.3; Mệnh đề 10.3 | `one-step-card.svg` (nhỏ) | 2 |
| 2 | `L10-203` | Đường cơ sở | định nghĩa | Định nghĩa 10.1 | — | 1 |
| 2 | `L10-204` | Đường cơ sở không làm chệch | kết quả | Mệnh đề 10.2 | — | 1,5 |
| 2 | `L10-205` | Chứng minh: đường cơ sở không làm chệch | chứng minh | chứng minh Mệnh đề 10.2 | — | 1,5 |
| 2 | `L10-206` | Ví dụ: đường cơ sở trên lượt hành lang | ứng dụng | Ví dụ 10.4 | — | 1,5 |
| 2 | `L10-207` | Hàm lợi thế | trực giác, định nghĩa, ví dụ | §2.3, Định nghĩa 10.4, Ví dụ 10.5 | — | 1 |
| 2 | `L10-208` | Gradient dạng lợi thế | kết quả | Mệnh đề 10.5 | — | 1,5 |
| 2 | `L10-209` | Thuật toán REINFORCE có đường cơ sở | thuật toán | Thuật toán 10.6 | — | 1 |
| 2 | `L10-210` | Bài tập: đường cơ sở hợp lệ | bài tập, lời giải (fragment) | Bài tập 10.1 | — | 1 |
| 2 | `L10-211` | Ví dụ: chuỗi hai trạng thái | ví dụ dẫn nhập, ứng dụng | Ví dụ 10.6 | `img/lec-10/two-state-chain.svg` | 2 |
| 2 | `L10-212` | Critic, actor và phương pháp actor–critic | vấn đề, trực giác, định nghĩa | §2.4, Định nghĩa 10.7 | — | 1 |
| 2 | `L10-212b` | Critic, actor và phương pháp actor–critic | nhắc lại sai số TD, hình | §2.4, hình sơ đồ actor–critic | `img/lec-10/actor-critic-advantage.svg` | 0,5 |
| 2 | `L10-213` | Sai số TD và lợi thế | kết quả | Mệnh đề 10.8 | — | 1,5 |
| 2 | `L10-214` | Ví dụ: hai bước actor–critic | ví dụ tính tay | Ví dụ 10.7 | — | 2 |
| 2 | `L10-215` | Thuật toán actor–critic một bước | thuật toán | Thuật toán 10.9, Nhận xét 10.10 | — | 1 |
| 2 | `L10-216` | Bài tập: sai số TD khi critic sai | bài tập, lời giải (fragment) | Bài tập 10.5 | — | 1,5 |
| 3 | `L10-300` | 3. Ước lượng lợi thế tổng quát | tiêu đề mạch | §3 | — | 0,5 |
| 3 | `L10-301` | Ví dụ: ba ước lượng lợi thế trên một lượt | vấn đề, ví dụ dẫn nhập | Ví dụ 10.8 | `two-state-chain.svg` (nhỏ) | 1,5 |
| 3 | `L10-302` | Lợi tức n bước | định nghĩa, bổ đề | Định nghĩa 10.11, Bổ đề 10.12 | — | 1 |
| 3 | `L10-303` | Lợi tức λ và GAE | trực giác, định nghĩa | §3.2, Định nghĩa 10.13 | `img/lec-10/gae-weights.svg` | 1,5 |
| 3 | `L10-304` | Dạng tổng và truy hồi của GAE | kết quả | Mệnh đề 10.14 và chứng minh | — | 2,5 |
| 3 | `L10-305` | Ví dụ: GAE và gradient trên chuỗi hai trạng thái | ví dụ | Ví dụ 10.9 | — | 1,5 |
| 3 | `L10-306` | GAE và tính không chệch cho gradient | kết quả | Mệnh đề 10.15 | — | 1,5 |
| 3 | `L10-307` | Ví dụ: kết thúc và cắt ngắn | vấn đề, ví dụ tính tay | §3.3, Ví dụ 10.10 | — (bỏ hình Bài 08 ở D1) | 1,5 |
| 3 | `L10-308` | Thuật toán tính GAE lùi trên đoạn thu | thuật toán | Thuật toán 10.16, Nhận xét 10.17 | — | 1 |
| 3 | `L10-309` | Bài tập: GAE trên đoạn thu | bài tập, lời giải (fragment) | Bài tập 10.7 | — | 2 |
| 4 | `L10-400` | 4. Hàm thay thế và chặn cải thiện | tiêu đề mạch | §4 | — | 0,5 |
| 4 | `L10-401` | Dữ liệu cũ và chính sách mới | vấn đề | §4 đoạn đầu | `img/lec-10/policy-update-feedback.svg` | 1 |
| 4 | `L10-402` | Ví dụ: đổi chính sách trên chuỗi hai trạng thái | trực giác, ví dụ | §4.1, Ví dụ 10.11 | — (bản viết bỏ hình nhỏ) | 2 |
| 4 | `L10-403` | Bổ đề hiệu hiệu năng | định nghĩa, kết quả | Định nghĩa 10.18, Bổ đề 10.19, Hệ quả 10.20 | — | 2,5 |
| 4 | `L10-404` | Chứng minh: bổ đề hiệu hiệu năng | chứng minh | chứng minh Bổ đề 10.19 | — | 1,5 |
| 4 | `L10-405` | Tỉ số chính sách và hàm thay thế | trực giác, định nghĩa | §4.2, Định nghĩa 10.21 | — | 1,5 |
| 4 | `L10-406` | Khớp giá trị và gradient tại tham số cũ | kết quả | Mệnh đề 10.22 | — | 1 |
| 4 | `L10-407` | Biến phân toàn phần và phân kỳ KL | định nghĩa, kết quả | Định nghĩa 10.23, Mệnh đề 10.24 | — | 1,5 |
| 4 | `L10-408` | Chặn cải thiện | trực giác, kết quả | §4.4, Định lý 10.26, Hệ quả 10.27 | — | 2,5 |
| 4 | `L10-409` | Chứng minh: chặn cải thiện | chứng minh | chứng minh Định lý 10.26, Bổ đề 10.25 | — | 1,5 |
| 4 | `L10-410` | Ví dụ: chặn cải thiện trên chuỗi hai trạng thái | ứng dụng | Ví dụ 10.12 | — | 2 |
| 4 | `L10-411` | Cải thiện đơn điệu | kết quả (vấn đề của cụm miền tin cậy) | Hệ quả 10.29 | — | 1 |
| 4 | `L10-412` | Bài toán miền tin cậy | trực giác, định nghĩa | Định nghĩa 10.30 | — | 0,5 |
| 4 | `L10-412b` | Mức giảm tối đa của bước miền tin cậy | kết quả, ứng dụng | Hệ quả 10.31 và đoạn sau | — | 1 |
| 4 | `L10-413` | Bài tập: đánh giá một bước cập nhật | bài tập (đề) | Bài tập 10.11 | — | 1,5 |
| 4 | `L10-414` | Bài tập: đánh giá một bước cập nhật | lời giải | Bài tập 10.11 | — | 1 |
| 5 | `L10-500` | 5. TRPO và gradient tự nhiên | tiêu đề mạch | §5 | — | 0,5 |
| 5 | `L10-501` | Ví dụ: cùng một bước tham số, hai khoảng cách chính sách | vấn đề, ví dụ dẫn nhập | §5 đoạn đầu, Ví dụ 10.13 | — | 1 |
| 5 | `L10-502` | Ma trận Fisher | trực giác, định nghĩa, ví dụ | Định nghĩa 10.32 | — | 0,5 |
| 5 | `L10-502b` | KL trung bình bậc hai | kết quả | Mệnh đề 10.33 | — | 1 |
| 5 | `L10-503` | Bước gradient tự nhiên | kết quả | Mệnh đề 10.34 | — | 1,5 |
| 5 | `L10-504` | Ví dụ: bước gradient tự nhiên trên bài toán một bước | ứng dụng | Ví dụ 10.14, 10.15, Nhận xét 10.35 | `one-step-card.svg` (nhỏ) | 1,5 |
| 5 | `L10-505` | Ví dụ: hai vòng gradient liên hợp | vấn đề, ví dụ tính tay | §5.2 đoạn đầu, Ví dụ 10.16 | `img/lec-10/trpo-trust-region.svg` | 2 |
| 5 | `L10-506` | Thuật toán gradient liên hợp với tích Fisher–vector | thuật toán | Thuật toán 10.36 | — | 1 |
| 5 | `L10-507` | Thuật toán TRPO với lợi thế GAE | thuật toán | Thuật toán 10.37 | — | 1,5 |
| 5 | `L10-508` | Phạm vi bảo đảm của TRPO thực hành | nhận xét | Nhận xét 10.38 | — | 1 |
| 5 | `L10-509` | Bài tập: gradient liên hợp và bước TRPO | bài tập (đề) | Bài tập 10.8 | — | 1 |
| 5 | `L10-510` | Bài tập: gradient liên hợp và bước TRPO | lời giải | Bài tập 10.8 | — | 1 |
| 6 | `L10-600` | 6. Tối ưu chính sách gần kề (PPO) | tiêu đề mạch | §6 | — | 0,5 |
| 6 | `L10-601` | Giới hạn của TRPO | vấn đề, trực giác | §5 cuối, §6.1 đoạn đầu | — | 1 |
| 6 | `L10-602` | Ví dụ: hai hàm thay thế mẫu trên bài toán một bước | ví dụ | Ví dụ 10.17 | `img/lec-10/ppo-one-step-plateau.svg` | 2 |
| 6 | `L10-603` | Mục tiêu PPO-Clip | định nghĩa | Định nghĩa 10.39 | — | 1 |
| 6 | `L10-604` | Dạng theo dấu của lợi thế | kết quả | Mệnh đề 10.40 | — | 1,5 |
| 6 | `L10-605` | Ví dụ: bốn mẫu | ứng dụng | Ví dụ 10.18 | `img/lec-10/ppo-clipping-signs.svg` | 1 |
| 6 | `L10-606` | Chặn dưới bi quan | kết quả | Mệnh đề 10.41, Nhận xét 10.42 | — | 1,5 |
| 6 | `L10-607` | PPO-Penalty | vấn đề, trực giác, ví dụ | §6.2, Ví dụ 10.19 | — | 1 |
| 6 | `L10-608` | PPO-Penalty | định nghĩa, kiểm tra (fragment) | Định nghĩa 10.43, Nhận xét 10.44, Bài tập 10.12(d) | — | 1 |
| 6 | `L10-609` | Hàm mất mát tổng | vấn đề, định nghĩa | Định nghĩa 10.45, 10.46 | — | 1 |
| 6 | `L10-610` | Ví dụ: một mini-batch tính tay | ví dụ tính tay | Ví dụ 10.20 | — (bản viết bỏ thẻ nhỏ) | 1,5 |
| 6 | `L10-611` | Đại lượng chẩn đoán và approxKL | vấn đề, định nghĩa | Định nghĩa 10.47 | — | 1,5 |
| 6 | `L10-611b` | Tính không chệch của approxKL | kết quả | Mệnh đề 10.48 | — | 1 |
| 6 | `L10-612` | Đường dữ liệu của PPO | trực giác | §6.3 sau Thuật toán 10.49 | `img/lec-10/ppo-data-pipeline.svg` | 1 |
| 6 | `L10-613` | Thuật toán PPO kiểu actor–critic | thuật toán | Thuật toán 10.49 | — | 1,5 |
| 6 | `L10-614` | Ví dụ: chẩn đoán trên đoạn phẳng | ứng dụng | Ví dụ 10.21 | — | 1 |
| 6 | `L10-615` | Siêu tham số của bài báo PPO | bảng | §6.4, bảng siêu tham số | — | 1 |
| 6 | `L10-616` | So sánh TRPO và PPO | bảng so sánh | §6.4, bảng so sánh | — | 1 |
| 6 | `L10-617` | Ví dụ: cắt mất mát giá trị | vấn đề, ví dụ | §6.5, Định nghĩa 10.46 (biến thể), Ví dụ 10.22 | — | 1 |
| 6 | `L10-617b` | Chi tiết cài đặt | bảng, kết luận | Nhận xét 10.50, kết luận của Engstrom và cộng sự | — | 0,5 |
| 6 | `L10-618` | Hội tụ về điểm dừng của PPO-Clip | nhận xét (đọc thêm) | §6.6, Nhận xét 10.51 | — | 1 |
| 6 | `L10-619` | Bài tập: kiểm một mini-batch PPO | bài tập (đề) | Bài tập 10.12 (a)–(c) | — | 1 |
| 6 | `L10-620` | Bài tập: kiểm một mini-batch PPO | lời giải | Bài tập 10.12 (a)–(c) | — | 1 |
| 7 | `L10-700` | 7. Tổng kết và chuyển tiếp | tiêu đề mạch | §7 | — | 0,5 |
| 7 | `L10-701` | Kết quả và giả thiết của bài | bảng tổng kết | §7.1, sáu hàng đầu | — | 1 |
| 7 | `L10-702` | Kết quả và giả thiết của bài | bảng tổng kết (tiếp) | §7.1, năm hàng của mục 4 | — | 0,5 |
| 7 | `L10-702b` | Kết quả và giả thiết của bài | bảng tổng kết (tiếp) | §7.1, bốn hàng của mục 5–6 | — | 0,5 |
| 7 | `L10-703` | So sánh bốn phương pháp | bảng phương pháp | §7.2 bảng thứ nhất | — | 1 |
| 7 | `L10-704` | Các kết luận có bảo đảm | bảng hội tụ | §7.2 bảng thứ hai | — | 0,5 |
| 7 | `L10-705` | Bài tập: GAE ở bước cắt ngắn trên CartPole | bài tập tổng hợp (đề) | Tình huống 10.1, 10.2 | — | 1,5 |
| 7 | `L10-706` | Bài tập: GAE ở bước cắt ngắn trên CartPole | lời giải | Tình huống 10.1, 10.2 | — | 1 |
| 7 | `L10-707` | Trả lời vấn đề trung tâm | trả lời có điều kiện | §7.3 | — | 1 |
| 7 | `L10-708` | Câu hỏi tự kiểm tra | câu hỏi | §7.4 | — | 0,5 |
| 7 | `L10-709` | Bài tập về nhà và tài liệu đọc | bài về nhà | §7.5; `exercises.md` (bảng mạch) | — | 0,5 |
| 7 | `L10-710` | Bài tập về nhà và tài liệu đọc | tài liệu đọc, nối Bài 11 | §7.5, §7.6 | — | 0,5 |

Kiểm tổng phút theo mạch. Mạch 1: $0{,}5+1{,}5+1{,}5+1+0{,}5+2+2+1+1{,}5+0{,}5=12$. Mạch 2: $0{,}5+1+2+1+1{,}5+1{,}5+1{,}5+1+1{,}5+1+1+2+1{,}5+1{,}5+2+1+1{,}5=23$. Mạch 3: $0{,}5+1{,}5+1+1{,}5+2{,}5+1{,}5+1{,}5+1{,}5+1+2=14{,}5$. Mạch 4: $0{,}5+1+2+2{,}5+1{,}5+1{,}5+1+1{,}5+2{,}5+1{,}5+2+1+1{,}5+1{,}5+1=22{,}5$. Mạch 5: $0{,}5+1+1{,}5+1{,}5+1{,}5+2+1+1{,}5+1+1+1=13{,}5$. Mạch 6: $0{,}5+1+2+1+1{,}5+1+1{,}5+1+1+1+1{,}5+2{,}5+1+1{,}5+1+1+1+1{,}5+1+1+1=25{,}5$. Mạch 7: $0{,}5+1+1+1+0{,}5+1{,}5+1+1+0{,}5+0{,}5+0{,}5=9$. Tổng $120$ phút, 95 trang; lời giải đầy đủ của bài tập thuộc 30 phút chữa bài. Đợt sửa sau cổng thêm năm trang (`L10-110`, `L10-412`, `L10-510`, `L10-608`, `L10-710`) mà không đổi phút của mạch: phút của trang mới lấy từ trang được tách, riêng `L10-710` lấy 0,5 phút từ `L10-708`. Bản viết và đợt sửa D1 thêm sáu trang tách, cũng không đổi phút của mạch: `L10-212` 1 + `L10-212b` 0,5 (từ 1,5); `L10-412` 0,5 + `L10-412b` 1 (từ 1,5); `L10-502` 0,5 + `L10-502b` 1 (từ 1,5); `L10-611` 1,5 + `L10-611b` 1 (từ 2,5); `L10-617` 1 + `L10-617b` 0,5 (từ 1,5); `L10-702` 0,5 + `L10-702b` 0,5 (từ 1). Tổng $120$ phút, 101 trang.

## Ngoại lệ mật độ

**Quy ước đếm** (như Bài 09): mỗi gạch đầu dòng, câu, dòng nhãn, khối công thức hiển thị và mỗi hàng bảng là một dòng; hàng tiêu đề cột không tính; dòng giả mã tính như dòng chữ. Âm tiết không tính ô số của bảng. Mỗi dòng chữ không quá 20 âm tiết; câu dài hơn được ngắt thành nhiều dòng, và số âm tiết từng dòng ghi trong mục của trang ở những trang chạm trần. Trang quá 6 dòng chỉ được phép ở trang nội dung, trang bảng tổng kết hoặc so sánh (trần 80 âm tiết), với lý do ghi dưới đây; mọi trang khác đã được tách hoặc rút về tối đa 6 dòng (đợt sửa sau cổng).

| trang | trần vượt | số đo dự kiến | lý do |
|---|---|---|---|
| `L10-105` | 6 dòng | 8 dòng (bảy mạch, dòng đọc trước), khoảng 40 âm tiết (trần 80 của trang nội dung) | Trang nội dung phải liệt kê đủ bảy mạch; như `L09-02b`. Nếu điều phối viên không chấp nhận, dòng "Đọc trước:" chuyển vào ghi chú diễn giả (còn 7 dòng) |
| `L10-109` | 60 âm tiết | 79 âm tiết sau D1 (hộp 14; năm dòng 13, 12, 14, 13, 13; trước D1: 80), 6 dòng; sau sửa 2026-11-13: 80 âm tiết theo `deck_check` (hộp 14; năm dòng 13, 12, 14, 15, 12) | Quyết định của điều phối viên: trang vấn đề trung tâm theo trần 80; mỗi mạch 2–6 một dòng trả lời có điều kiện. Hình đã tách sang `L10-110` |
| `L10-702` | (đã gỡ) | bản viết tách thành `L10-702` (5 hàng, 46 âm tiết) và `L10-702b` (4 hàng, 42 âm tiết sau D1), trần 80 của bảng tổng kết | Không còn ngoại lệ số dòng |

Dòng dẫn của sáu trang tiêu đề mạch (16–24 âm tiết) theo trần 25 riêng của `p.strand-lead` (`AGENTS.md` §"Trang tiêu đề mạch"), hiển thị trên hai dòng. Trang theo trần 80 không phải ngoại lệ: `L10-104` (mục tiêu, 80; 6 dòng sau sửa 2026-11-13), `L10-701`–`L10-704` (bảng tổng kết và so sánh), `L10-707` (trả lời bài toán, 80 sau sửa 2026-11-13), `L10-615`, `L10-616` (bảng). Các ngoại lệ của bản trước đã gỡ: `L10-101` (rút còn 49 âm tiết), các trang giả mã `L10-209`, `L10-215`, `L10-308`, `L10-506`, `L10-507`, `L10-613` (rút về 6 dòng).

## Khuôn bảng cố định

Một phép tính lặp dùng một khuôn bảng với cùng tên cột trong toàn bài.

| khuôn | cột | trang |
|---|---|---|
| actor–critic | `t` · `I` · mục tiêu · $\delta_t$ · $w$ mới · hướng actor · $\theta$ mới · $p$ mới | `L10-214`, `L10-216` (lời giải) |
| GAE trên đoạn thu | `t` · $R_{t+1}$ · $Z_{t+1}$ · $U_{t+1}$ · $\hat v_{\mathrm{old}}(S_t)$ · $\delta_t$ · $\widehat A_t$ (· $V^{\mathrm{targ}}_t$) | `L10-307`, `L10-309` |
| chính sách trên chuỗi | chính sách · $p_A$ · $p_B$ · $J$ (· $\mathcal L-J$ · cận) | `L10-402`, `L10-413`, `L10-414` |
| vòng gradient liên hợp | $k$ · $x_k$ · $\tilde g_k$ · $\omega_k$ | `L10-505`, `L10-509` |
| mẫu PPO | mẫu · $\widehat A$ · $\rho$ · $\ell^{\mathrm{CLIP}}$ · gradient bằng $0$ | `L10-605`, `L10-610`, `L10-614`, `L10-619`, `L10-620` |

## Mục từng trang

Mỗi mục ghi: vị trí và loại; lý do tồn tại và nhu cầu lấp; liên kết trước/sau; mục tiêu học tập hỗ trợ (đánh số theo `L10-104`); khối ghi chú và trang nguồn; nội dung mặt trang dự kiến; mật độ (âm tiết, dòng, công thức hiển thị); hình; phút; quyết định; ý chính của ghi chú diễn giả.

### Mạch 1. Mở đầu và hai giới hạn của REINFORCE (12 phút)

#### `L10-101` TRPO và PPO (bìa)
- **Vị trí, loại:** trang 1 của mạch 1; bìa, là trang tiêu đề của mạch mở đầu.
- **Lý do tồn tại, nhu cầu:** nêu tên bài, tên đầy đủ của TRPO và PPO, và câu luận đề nối hai nửa bài.
- **Liên kết:** trước: —; sau: `L10-102` (ký hiệu cho mọi đại lượng của luận đề).
- **Mục tiêu:** định hướng cả năm mục tiêu.
- **Khối ghi chú, nguồn:** đoạn mở và §1.1 (`topic-02`); nguồn tr. 1–2.
- **Mặt trang:** `h1` "TRPO và PPO"; `h2` "Tối ưu chính sách miền tin cậy (TRPO) và tối ưu chính sách gần kề (PPO)" (dòng tiêu đề, không đếm theo quyết định của điều phối viên); `h3` "Bài 10 · Học tăng cường"; hộp luận đề, ba dòng hiển thị: "Đường cơ sở giữ kỳ vọng của gradient; / sai số hàm thay thế bị chặn theo khoảng cách chính sách, / nên TRPO ràng buộc khoảng cách, PPO cắt tỉ số." (8, 12, 10); "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội"; "Năm học 2026–2027, học kỳ 1". Không tên tiếng Anh trong luận đề; tên tiếng Anh của đường cơ sở, hàm thay thế, tỉ số chính sách ở `L10-104`.
- **Mật độ:** 49 âm tiết (luận đề 30, "Bài 10 · Học tăng cường" 4, đơn vị 10, năm học 5), 0 công thức, 1 hộp chữ 1 câu. Không còn là ngoại lệ.
- **Hình, phút:** —; 0,5.
- **Quyết định:** sửa (`L10-01` "Tối ưu chính sách theo miền tin cậy (TRPO)"): bìa cũ chỉ nêu TRPO; thêm PPO, luận đề một câu, đơn vị, năm học. Luận đề rút từ 47 xuống 30 âm tiết theo cổng storyboard.
- **Ghi chú diễn giả:** REINFORCE của Bài 09 cho mẫu không chệch của gradient nhưng phương sai lớn và mỗi lượt dùng cho một bước; critic và GAE chỉ giữ kỳ vọng khi critic đúng (GAE: cả khi $\lambda=1$ trên lượt đầy đủ); "khoảng cách" là KL trung bình theo phân bố trạng thái của chính sách cũ.

#### `L10-102` Tiên quyết và quy ước (Ký hiệu)
- **Vị trí, loại:** trang 2 của mạch 1; tiên quyết, phần "Ký hiệu:".
- **Lý do tồn tại, nhu cầu:** cố định miền, chỉ số thời gian, quy ước kỳ vọng và cờ trước mọi công thức; phân biệt hai vai của chữ $A$.
- **Liên kết:** trước: `L10-101`; sau: `L10-103` (các công thức nhắc lại viết bằng ký hiệu này).
- **Mục tiêu:** 1–5 (ký hiệu chung).
- **Khối ghi chú, nguồn:** Bảng ký hiệu, Quy ước đọc (`topic-01`); nguồn tr. 5.
- **Mặt trang:** dòng "Ký hiệu: $\mathbb E_{\pi_\theta}$ lấy theo $S_0\sim\mu_0$, $A_t\sim\pi_\theta(\cdot\mid S_t)$, $P$; $\log$ tự nhiên." rồi bảng hai cột bốn hàng: (1) $\mathcal S$ trạng thái chưa kết thúc, $\mathcal A$ hữu hạn, $m$ hành động; $\mu_0$ phân phối đầu, $P(s'\mid s,a)$; (2) $R_{t+1}$ sau $A_t$; lượt kết thúc tại $T$, $G_T=0$; $\gamma\in[0,1)$ trong các định lý; (3) $Z_{t+1}$ kết thúc của MDP (termination), $U_{t+1}$ cắt ngắn (truncation); (4) $\pi_\theta$; $\theta_{\mathrm{old}}$, $\pi_{\mathrm{old}}$ sinh dữ liệu; $\psi_t=\nabla_\theta\log\pi_\theta(A_t\mid S_t)$; $H_t$. Dòng cuối "Lưu ý: $A_t$ là hành động; $A_\pi$, $\widehat A_t$ là lợi thế (advantage)."
- **Mật độ:** khoảng 50 âm tiết, 6 dòng (dòng ký hiệu, bốn hàng bảng, dòng lưu ý; mỗi hàng bảng tính một dòng), 0 công thức hiển thị.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-04` "Quy ước của bài"): đổi $d^\pi$, $m_t$, $c_t$, $H$ sang $\nu^\pi$ (để `L10-403`), $1-Z_{t+1}$, $U_{t+1}$, $h$; thêm $\mu_0$; ghi "$\gamma\in[0,1)$ trong các định lý" vì `L10-107`, `L10-108` dùng $\gamma=1$.
- **Ghi chú diễn giả:** Bài 09 viết $\rho_0$, ở đây $\mu_0$ vì $\rho$ dành cho tỉ số chính sách; sau $T$ là trạng thái hấp thụ với $v_\pi=q_\pi=A_\pi=0$; hành lang ngắn có $\gamma=1$, nằm ngoài giả thiết các định lý; hai loại trung bình (có chiết khấu và đều trên bộ đệm) sẽ tách ở mạch 4 và 6.
- **Sửa 2026-11-13 (bảng phát hiện):** ô cờ thành "cờ kết thúc (termination); cờ cắt ngắn (truncation)", bỏ "của MDP" để giữ 57 âm tiết (trước 59); tên đầy đủ của MDP lên `L10-103`; ghi chú diễn giả thêm nghĩa của $Z_{t+1}$, $U_{t+1}$ với tên đầy đủ "quá trình quyết định Markov (MDP)". `deck_check`: 57 âm tiết, ghi chú 139.

#### `L10-103` Tiên quyết và quy ước (Nhắc lại)
- **Vị trí, loại:** trang 3 của mạch 1; tiên quyết, phần "Nhắc lại:".
- **Lý do tồn tại, nhu cầu:** phát biểu lại các kết quả của Bài 03 và Bài 09 dùng ngay ở mạch 1–2; các nhắc lại khác đặt tại chỗ dùng (sai số TD ở `L10-212`, cờ $Z$, $U$ ở `L10-307`, $\Gamma_\pi$ ở `L10-403`, Định lý 04.13 ở `L10-403`, tỉ số lấy mẫu quan trọng ở `L10-405`).
- **Liên kết:** trước: `L10-102`; sau: `L10-104`.
- **Mục tiêu:** 1 (chứng minh đường cơ sở dùng hàm điểm có kỳ vọng $0$).
- **Khối ghi chú, nguồn:** Kiến thức tiên quyết (`topic-01`); nguồn tr. 6–10.
- **Mặt trang:** "Nhắc lại:" (1) REINFORCE $\widehat g=\sum_{t<T}\gamma^tG_t\psi_t$, dưới (G1)–(G4) $\mathbb E[\widehat g\mid\theta_{\mathrm{old}}]=\nabla_\theta J(\theta_{\mathrm{old}})$ (Hệ quả 09.26); (2) (G1)–(G4): $\mu_0$, $P$ không phụ thuộc $\theta$; $\pi_\theta$ khả vi, miền hỗ trợ cố định; $\lvert R\rvert$, $T$, đặc trưng bị chặn; (3) $\mathbb E_{A\sim\pi_\theta(\cdot\mid s)}[c\,\psi_\theta(s,A)]=0$ khi $c$ không phụ thuộc $A$; (4) softmax hai hành động, $p=\pi_\theta(1\mid s)$: $\psi_\theta(s,1)=(1-p)(1;\,-1)$, $\psi_\theta(s,2)=-p\,(1;\,-1)$; (5) $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)v_\pi(s')$, $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$.
- **Mật độ:** khoảng 45 âm tiết, 6 dòng, 1 công thức hiển thị (dòng 5); một số hiệu kết quả trên mặt trang.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-05` "REINFORCE dùng return toàn phần"): thêm giả thiết (G1)–(G4), kỳ vọng của hàm điểm, công thức $q_\pi$, $v_\pi$.
- **Ghi chú diễn giả:** số hiệu Mệnh đề 09.16, 09.17, 03.22, 03.23; lịch sử $H_t$ và tính chất tháp $\mathbb E[\mathbb E[X\mid Y]]=\mathbb E[X]$ dùng ở `L10-205`; bỏ trọng số $\gamma^t$ làm mất tính không chệch (Ví dụ 09.21).
- **Sửa 2026-11-13 (bảng phát hiện):** dòng (G1) thành "$\mu_0$, $P$ của quá trình quyết định Markov (MDP) không phụ thuộc $\theta$, $S_t$ Markov": lần đầu MDP trên mặt trang có tên đầy đủ. `deck_check`: 44 âm tiết (trước 37), 6 dòng, dòng dài nhất 19.

#### `L10-104` Mục tiêu học tập
- **Vị trí, loại:** trang 4 của mạch 1; mục tiêu.
- **Lý do tồn tại, nhu cầu:** báo trước sản phẩm kiểm được của từng mạch 2–6 để bảng tổng kết và trang trả lời bài toán đối chiếu; nơi các thuật ngữ của luận đề có tên tiếng Anh lần đầu.
- **Liên kết:** trước: `L10-103`; sau: `L10-105`.
- **Mục tiêu:** 1–5.
- **Khối ghi chú, nguồn:** Mục tiêu học tập 1–7 (`topic-02`); nguồn tr. 2.
- **Mặt trang:** sáu dòng đánh số (2026-11-13; trước năm dòng), chép đúng câu trong `outline.md`, mục "Mục tiêu học tập": thêm dòng 6 "Chứng minh chặn dưới bi quan; approxKL không chệch." (sản phẩm của mục tiêu 6–7 của ghi chú); dòng 3–4 gộp bằng dấu phẩy; dòng 5 bỏ "của tỉ số chính sách (probability ratio)" (tên tiếng Anh chuyển sang `L10-405`).
- **Mật độ:** 80 âm tiết theo `deck_check` (trần 80 của trang mục tiêu; trước 80), 6 dòng, dòng dài nhất 19, 0 công thức.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-02` "Kết quả học tập"): đổi tiêu đề; mỗi dòng một mạch, động từ học tập, tên tiếng Anh ở lần đầu (gồm ba tên chuyển từ bìa: baseline, surrogate objective, probability ratio).
- **Ghi chú diễn giả:** sản phẩm của từng dòng: $\tfrac49(b-1)^2$ và $p_A=0{,}5436$; $\widehat A_0=0{,}98$ và $3{,}572$, điều kiện γ-just; $\Delta J=0{,}296$, $\mathcal L-J=0{,}26$, cận chặn cải thiện $-0{,}892$; $\Delta^*=(0{,}15;\,-0{,}15)$, $\Delta=(0{,}05;\,0{,}1)$; $\mathcal L^{\mathrm{CLIP}}=0{,}2167$, approxKL $0{,}01737$, điều PPO không bảo đảm.
- **Sửa 2026-11-13 (bảng phát hiện):** xem "Mặt trang", "Mật độ" đã cập nhật.

#### `L10-105` Nội dung
- **Vị trí, loại:** trang 5 của mạch 1; nội dung.
- **Lý do tồn tại, nhu cầu:** bản đồ bảy mạch, số trùng `#/N` và trang tiêu đề mạch.
- **Liên kết:** trước: `L10-104`; sau: `L10-106`.
- **Mục tiêu:** —.
- **Khối ghi chú, nguồn:** Bảy phần của chương (`topic-02`); nguồn tr. 3.
- **Mặt trang:** bảy mục đánh số, mỗi mục là liên kết `#/N` với tên trong bảng "Bảy mạch" của `outline.md`; dòng "Đọc trước: Sutton và Barto (2018), §13.4–13.5, §12.1–12.3; Schulman và cộng sự (2017), §3–5."
- **Mật độ:** khoảng 40 âm tiết, 8 dòng (ngoại lệ), 0 công thức.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm (bộ cũ không có trang Nội dung).
- **Ghi chú diễn giả:** hàng trên của bài toán (mạch 2–3) và hàng dưới (mạch 4–6); mạch 7 tổng kết; Phần II của nguồn thuộc Bài 11.

#### `L10-106` Ví dụ: bài toán một bước, phương sai của REINFORCE
- **Vị trí, loại:** trang 6 của mạch 1; ví dụ dẫn nhập của giới hạn thứ nhất, làm cụ thể vấn đề "phương sai phụ thuộc mức chung của phần thưởng" mà `L10-201` dùng lại.
- **Lý do tồn tại, nhu cầu:** tính không chệch của Hệ quả 09.26 là khẳng định về trung bình; cần một số đo cho độ dao động trên từng lượt.
- **Liên kết:** trước: `L10-105`; sau: `L10-107` (hậu quả trên một lượt dài hơn).
- **Mục tiêu:** 1.
- **Khối ghi chú, nguồn:** Ví dụ 10.1 (`topic-02`); nguồn tr. 9–10.
- **Mặt trang:** thẻ dữ kiện bên trái; bên phải: "Nhu cầu: đo độ dao động của $\widehat g$ giữa các lượt." $\widehat g=(1;\,-1)$ với xác suất $\tfrac23$, $(0;\,0)$ với xác suất $\tfrac13$; kỳ vọng $(\tfrac23;\,-\tfrac23)=\nabla_\theta J$; $\operatorname{Var}(\widehat g)=\mathbb E\lVert\widehat g-\mathbb E\widehat g\rVert^2=\tfrac49$; với $r=(4;\,1)$: kỳ vọng không đổi, $\operatorname{Var}=\tfrac{16}9$. "Diễn giải:" cộng $1$ vào mọi phần thưởng không đổi gradient, phương sai tăng gấp bốn.
- **Mật độ:** khoảng 35 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** `img/lec-09/one-step-card.svg`; 2.
- **Quyết định:** thêm (bộ cũ không định lượng phương sai).
- **Ghi chú diễn giả:** mỗi tọa độ có phương sai $\tfrac29$ rồi $\tfrac89$; kiểm $\mathbb E\lVert\widehat g\rVert^2-\lVert\nabla J\rVert^2$; mức chung của phần thưởng không ảnh hưởng tới việc chọn hành động.
- **Sửa 2026-11-13 (bảng phát hiện):** `style="grid-template-columns:2fr 3fr"` thay bằng lớp `.grid2.wide-right` của `lecture-course.css` (G8); ảnh chụp không đổi bố cục.

#### `L10-107` Ví dụ: hành lang ngắn, một lượt REINFORCE
- **Vị trí, loại:** trang 7 của mạch 1; ví dụ dẫn nhập của giới hạn thứ nhất (hậu quả trên một lượt); dữ kiện dùng lại ở `L10-206`.
- **Lý do tồn tại, nhu cầu:** cho thấy ước lượng không chệch vẫn có thể cho bước ngược chiều gradient.
- **Liên kết:** trước: `L10-106`; sau: `L10-108` (cùng hành lang, bước theo đúng gradient).
- **Mục tiêu:** 1.
- **Khối ghi chú, nguồn:** Ví dụ 10.2 (`topic-02`); nguồn tr. 10.
- **Mặt trang:** hình hành lang; dữ kiện $\theta=(0;\,0)$, $p=\tfrac12$, $\gamma=1$, $J=-12$, $\nabla_\theta J=(2;\,-2)$, $\alpha=0{,}1$; lượt $A_{0:4}=1,1,1,2,1$, $G_t=-5,\dots,-1$; "Tính $\widehat g$." $\widehat g=(-5{,}5;\,5{,}5)$; $p$ từ $0{,}5$ xuống $0{,}2497$, $J$ từ $-12$ xuống $-18{,}68$. "Diễn giải:" mọi $G_t<0$ nên hành động đã chọn bị giảm xác suất.
- **Mật độ:** khoảng 35 âm tiết, 5 dòng, 0–1 công thức hiển thị.
- **Hình, phút:** `img/lec-09/short-corridor.svg`; 2.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.2 của ghi chú.
- **Ghi chú diễn giả:** tọa độ thứ nhất $\tfrac12(-13)+(-\tfrac12)(-2)=-5{,}5$; hành lang không thỏa (G3), ước lượng vẫn không chệch vì $T$ có đuôi hình học (ghi chú, đoạn sau Ví dụ 10.4); $p^*=2-\sqrt2\approx0{,}59$.
- **Sửa 2026-11-13 (bảng phát hiện):** `style="max-height:200px"` thay bằng lớp `.figure.short-m` (210 px, G8); ghi chú diễn giả bỏ lời trỏ "ghi chú bài giảng, đoạn sau Ví dụ 10.4", giữ nội dung: "không thỏa (G3), nhưng $T$ có đuôi hình học nên ước lượng vẫn không chệch".

#### `L10-108` Ví dụ: hành lang ngắn, một bước theo đúng gradient
- **Vị trí, loại:** trang 8 của mạch 1; ví dụ dẫn nhập của giới hạn thứ hai, làm cụ thể vấn đề mà `L10-401` mở lại.
- **Lý do tồn tại, nhu cầu:** muốn mỗi lượt cho nhiều tiến bộ hơn thì cần bước lớn; cần thấy bước lớn theo đúng hướng vẫn có thể làm $J$ giảm.
- **Liên kết:** trước: `L10-107`; sau: `L10-109`.
- **Mục tiêu:** 3 (động cơ của chặn cải thiện).
- **Khối ghi chú, nguồn:** §1.1 đoạn sau Ví dụ 10.2 (`topic-02`); nguồn tr. 4, 14.
- **Mặt trang:** từ $\theta=(0;\,0)$ theo $(2;\,-2)$: $\alpha=0{,}1$: $p=0{,}5987$, $J=-11{,}66$; $\alpha=0{,}5$: $p=0{,}8808>p^*\approx0{,}59$, $J=-21{,}32$. Dòng: Hệ quả 09.26 cần lượt của chính $\pi_{\theta_{\mathrm{old}}}$, nên mỗi lượt cho một bước. Kết luận: "Với $\alpha=0{,}5$, $J$ giảm $9{,}32$."
- **Mật độ:** khoảng 35 âm tiết, 4 dòng, 0 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-03` "Dữ liệu đổi sau mỗi lần cập nhật"): câu khẳng định không số thay bằng hai bước có số.
- **Ghi chú diễn giả:** $J$ chỉ gần tuyến tính trong lân cận nhỏ của chính sách cũ; bước lớn đổi phân bố trạng thái mà chính sách mới thăm; hai giới hạn không mâu thuẫn với Hệ quả 09.26.

#### `L10-109` Vấn đề trung tâm
- **Vị trí, loại:** trang 9 của mạch 1; vấn đề trung tâm.
- **Lý do tồn tại, nhu cầu:** nêu bài toán một dòng và câu trả lời có điều kiện của mạch 2–6.
- **Liên kết:** trước: `L10-108`; sau: `L10-110` (hình xếp năm câu trả lời thành hai hàng).
- **Mục tiêu:** 1–5.
- **Khối ghi chú, nguồn:** §1.1, năm câu trả lời (`topic-02`); nguồn tr. 4, 14.
- **Mặt trang:** hộp, hai dòng hiển thị: "Giảm phương sai, giữ kỳ vọng; / dùng dữ liệu cũ cho bước lớn, $J$ không giảm." (15); danh sách đánh số từ 2: (2) "Đường cơ sở không phụ thuộc $A_t$, critic đúng: giữ kỳ vọng." (11); (3) "GAE không chệch cho gradient: lượt đầy đủ, hàm giá trị cố định, $\lambda=1$ hoặc critic đúng." (16); (4) "Lợi thế chính xác: sai số hàm thay thế bị chặn theo khoảng cách." (14); (5) "Bậc hai: bước gradient tự nhiên; khoảng cách mẫu dưới bán kính." (12); (6) "Mục tiêu cắt: chặn dưới hàm thay thế mẫu, không chặn khoảng cách." (12). Không dùng $\delta_t$, $\nu^\pi$, $\kappa$, chữ KL trước trang định nghĩa của chúng.
- **Mật độ:** 80 âm tiết (ngoại lệ trần 60, trong trần 80 theo quyết định của điều phối viên), 6 dòng, 1 hộp chữ 1 câu, không hình.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo §1.1, năm câu trả lời của ghi chú. Đợt sửa sau cổng: tách hình sang `L10-110`; rút từ khoảng 85 xuống 80 âm tiết; dòng 3 thêm điều kiện "lượt đầy đủ, hàm giá trị cố định".
- **Ghi chú diễn giả:** "khoảng cách" là TV hoặc KL trung bình (định nghĩa ở mạch 4); dòng 5: TRPO chỉ bảo đảm KL trung bình mẫu không vượt bán kính $\kappa$; dòng 3 là Mệnh đề 10.15, không khẳng định không chệch cho lợi thế.
- **Sửa 2026-11-13 (bảng phát hiện):** dòng (2) thành "… giữ kỳ vọng; hệ số $\delta_t$ cần $\hat v=v_\pi$." (sửa sau kiểm lại; tránh viết tắt "sai số TD" trước `L10-212b`); dòng (5) thành "TRPO xấp xỉ; trên bộ đệm: KL trung bình mẫu ${\le\kappa}$, hàm thay thế mẫu tăng." theo Nhận xét 10.38 (D10); dòng (6) "… không chặn KL.". Ghi chú diễn giả sửa theo (dòng 2: "còn $\delta_t$, mục tiêu bootstrap một bước trừ $\hat v(S_t)$, chỉ ước lượng đúng lợi thế khi critic đúng"; dòng 5: hai bất đẳng thức kiểm được trên bộ đệm), 149 token (trước 151). `deck_check`: 79 âm tiết (trước 79), 6 dòng, dòng dài nhất 15; vẫn là ngoại lệ trần 60 đã duyệt, trong trần 80.

#### `L10-110` Hệ số của hàm điểm và độ lớn bước
- **Vị trí, loại:** trang 10 của mạch 1; trang khung chung (mọi phương pháp của bài là một trong hai hàng của cùng một khung).
- **Lý do tồn tại, nhu cầu:** xếp năm câu trả lời của `L10-109` thành hai chuỗi và cho thấy chỗ hai chuỗi gặp nhau, trước khi mạch 2 bắt đầu chuỗi trên.
- **Liên kết:** trước: `L10-109`; sau: `L10-200` (hàng trên mở đầu bằng đường cơ sở).
- **Mục tiêu:** 1–5.
- **Khối ghi chú, nguồn:** §1.1, hình và đoạn đọc hình (`topic-02`).
- **Mặt trang:** hình `central-problem.svg` chiếm phần lớn trang; ba dòng: "Hàng trên: hệ số nhân với hàm điểm (phần 2–3)." (10); "Hàng dưới: độ lớn bước tính từ $\theta_{\mathrm{old}}$ (phần 4–6)." (9); "Hai hàng gặp nhau ở PPO kiểu actor–critic." (8). Không chuỗi mũi tên trên mặt trang.
- **Mật độ:** 27 âm tiết, 3 dòng, 1 hình.
- **Hình, phút:** `img/lec-10/central-problem.svg`; 0,5.
- **Quyết định:** tách (từ `L10-109` của bản storyboard trước, theo quyết định của điều phối viên ở cổng); trang này là trang khung của kế hoạch đã duyệt.
- **Ghi chú diễn giả:** đọc hình: hàng trên viền liền gồm đường cơ sở và critic, rồi GAE; hàng dưới nét đứt gồm hàm thay thế và chặn cải thiện, TRPO, PPO; khung cuối viền đậm là Thuật toán 10.49, nơi GAE cho lợi thế và mục tiêu cắt cho chính sách.

**Hành trình khái niệm, mạch 1.** Mạch 1 không mở khái niệm cốt lõi: các trang nhắc lại kết quả đã học, phát biểu bài toán (`L10-109`) và nêu khung chung (`L10-110`). Ba ví dụ dẫn nhập (`L10-106`–`L10-108`) là bước vấn đề của cụm đường cơ sở (mạch 2) và của cụm hiệu hiệu năng (mạch 4); sáu bước của mạch 1 ghi `không áp dụng`.

### Mạch 2. Đường cơ sở, hàm lợi thế và actor–critic (23 phút)

#### `L10-200` 2. Đường cơ sở, hàm lợi thế và actor–critic (trang tiêu đề mạch), điểm vào mạch 2
- **Vị trí, loại:** điểm vào mạch 2; `section.strand-title`, `id="mach-2"`, `data-note-topic-id="lec-10-topic-03"`.
- **Lý do tồn tại, nhu cầu:** mở nửa thứ nhất của bài toán; dòng dẫn nêu đúng nhu cầu của khái niệm đầu tiên (đường cơ sở), nên trang là bước `vấn đề` chung của cụm đường cơ sở.
- **Liên kết:** trước: `L10-110` (hàng trên của khung); sau: `L10-201`. Kế thừa $\operatorname{Var}$ $\tfrac49\to\tfrac{16}9$ và lượt hành lang; giao cho mạch 3 lợi thế $A_\pi$ và sai số TD $\delta_t$ cùng hai đầu Monte Carlo và một bước.
- **Mục tiêu:** 1.
- **Mặt trang:** "2." + tên mạch; dòng dẫn "Muốn giảm phương sai mà giữ kỳ vọng của gradient, phải trừ khỏi lợi tức một mức không phụ thuộc hành động đã chọn." (24); từ khóa "Đường cơ sở · Hàm lợi thế · Critic · Sai số TD · Actor–critic một bước" (13).
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm (trang tiêu đề mạch theo `AGENTS.md`).
- **Ghi chú diễn giả (40–100):** kết quả kế thừa (phương sai phụ thuộc mức chung của phần thưởng; một lượt cho bước ngược chiều); nhiệm vụ (trừ đường cơ sở, đặt tên lợi thế, bootstrap bằng critic); đầu ra ($\delta_t$ ước lượng lợi thế khi critic đúng).
- **Sửa 2026-11-13 (bảng phát hiện):** từ khóa "Sai số TD" thành "Sai số sai phân thời gian" (viết tắt chỉ dùng sau `L10-212b`). `deck_check`: 40 âm tiết.

#### `L10-201` Mức so sánh của trạng thái
- **Vị trí, loại:** mạch 2; vấn đề và trực giác của cụm đường cơ sở.
- **Lý do tồn tại, nhu cầu:** đưa phép so sánh với một mức của trạng thái trước khi đặt ký hiệu $b$.
- **Liên kết:** trước: `L10-200`; sau: `L10-202` (ba mức cụ thể). **Mục tiêu:** 1. **Ghi chú:** §2 đoạn đầu, §2.1 đoạn 1 (`topic-03`); nguồn tr. 11.
- **Mặt trang:** bốn dòng: "Nhu cầu: tách khỏi $G_t$ phần chung không phân biệt hành động." (10); "Bài toán một bước: cộng $1$ vào phần thưởng, phương sai từ $\tfrac49$ lên $\tfrac{16}9$." (12); "Trực quan. So $G_t$ với một mức $b(S_t)$ chỉ phụ thuộc trạng thái." (11); "Hệ số của $\psi_t$ là $G_t-b(S_t)$: dương thì tăng, âm thì giảm xác suất hành động đã chọn." (16). Dòng "Trực quan." cũ khoảng 30 âm tiết tách thành hai dòng.
- **Mật độ:** 49 âm tiết, 4 dòng, 0 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-06` "Baseline loại phần chung của return"): tiêu đề danh từ, "baseline" thành "đường cơ sở", thêm số dẫn nhập.
- **Ghi chú diễn giả:** liên hệ bài toán nhiều cần gạt (multi-armed bandit) (Sutton và Barto, 2018, §13.4, tr. 329); mức so sánh phải không phụ thuộc hành động đã chọn, điều kiện được chứng minh ở `L10-204`.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả bỏ câu về bài toán nhiều cần gạt (không có trong ghi chú); 98 token.

#### `L10-202` Ví dụ: ba đường cơ sở trên bài toán một bước
- **Vị trí, loại:** mạch 2; bước ví dụ của cụm đường cơ sở; bước ví dụ và hình thức rút gọn của cụm "đường cơ sở tối ưu" (`topic-04`).
- **Lý do tồn tại, nhu cầu:** cho thấy kỳ vọng không phụ thuộc $b$ còn phương sai thì phụ thuộc, trước khi phát biểu tổng quát.
- **Liên kết:** trước: `L10-201`; sau: `L10-203` (đặt tên đại lượng $X_b$ thành $\widehat g_b$). **Mục tiêu:** 1. **Ghi chú:** Ví dụ 10.3; Mệnh đề 10.3 (`topic-03`, `topic-04`); nguồn tr. 11; Greensmith và cộng sự (2004), §5.
- **Mặt trang:** thẻ nhỏ; "Tính" $X_b=(r(A)-b)\,\psi_\theta(s,A)$ với $b=0$, $2$, $1$; $\mathbb E X_b=(\tfrac23;\,-\tfrac23)$ với mọi $b$; $\operatorname{Var}(X_b)$: $\tfrac49$, $\tfrac49$, $0$; dạng chung $\operatorname{Var}(X_b)=\tfrac49(b-1)^2$ ($b=3$: $\tfrac{16}9$). "Lưu ý: đường cơ sở hằng tốt nhất là $b^*=\mathbb E[R\lVert\psi\rVert^2]/\mathbb E\lVert\psi\rVert^2=1\ne v_\pi(s)=2$ (Mệnh đề 10.3)."
- **Mật độ:** khoảng 35 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** thẻ `one-step-card.svg` (nhỏ); 2.
- **Quyết định:** thêm; gộp trang "Đường cơ sở có phương sai nhỏ nhất" của kế hoạch thành dòng "Lưu ý:" (phương án nén).
- **Ghi chú diễn giả:** $\operatorname{Var}(X_b)=\operatorname{Var}(X_{b^*})+\mathbb E\lVert\psi\rVert^2(b-b^*)^2$ với $\mathbb E\lVert\psi\rVert^2=\tfrac49$; chứng minh khai triển bậc hai theo $b$; $b=3$ làm tăng phương sai nên đường cơ sở không luôn giảm phương sai; $v_\pi$ không phải đường cơ sở tối ưu.
- **Sửa 2026-11-13 (bảng phát hiện):** `.grid2.wide-right` thay `style=""` (G8).

#### `L10-203` Đường cơ sở
- **Vị trí, loại:** mạch 2; bước hình thức (định nghĩa).
- **Lý do tồn tại, nhu cầu:** cố định miền của $b$ và dạng $\widehat g_b$ trên lượt nhiều bước.
- **Liên kết:** trước: `L10-202` ($X_b$ là $\widehat g_b$ với $T=1$); sau: `L10-204`. **Mục tiêu:** 1. **Ghi chú:** Định nghĩa 10.1 (`topic-03`); nguồn tr. 11.
- **Mặt trang:** "Định nghĩa." Hàm bị chặn $b:\mathcal S\to\mathbb R$ gọi là đường cơ sở; ước lượng có đường cơ sở $\widehat g_b=\sum_{t<T}\gamma^t\bigl(G_t-b(S_t)\bigr)\psi_t$. Dòng: đường cơ sở ngẫu nhiên $B_t$ được phép nếu khi biết $(H_t,B_t)$, $A_t$ vẫn có phân phối $\pi_\theta(\cdot\mid S_t)$.
- **Mật độ:** khoảng 35 âm tiết, 3 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Định nghĩa 10.1 của ghi chú.
- **Ghi chú diễn giả:** $\hat v(S_t,w)$ với $w$ cố định trong lượt là một đường cơ sở; $G_t$ thì không vì phụ thuộc $A_t$.

#### `L10-204` Đường cơ sở không làm chệch
- **Vị trí, loại:** mạch 2; bước hình thức (kết quả).
- **Lý do tồn tại, nhu cầu:** kết quả chính của cụm: phép trừ không đổi kỳ vọng.
- **Liên kết:** trước: `L10-203`; sau: `L10-205`. **Mục tiêu:** 1. **Ghi chú:** Mệnh đề 10.2 (`topic-03`); nguồn tr. 11.
- **Mặt trang:** "Mệnh đề." "Giả thiết:" (G1)–(G4); $\lvert b\rvert\le\bar b$; lượt sinh bởi $\pi_\theta$; $b$ cố định trong lượt. "Kết luận:" $\mathbb E\bigl[\sum_{t<T}\gamma^tb(S_t)\psi_t\bigr]=0$, nên $\mathbb E[\widehat g_b]=\nabla_\theta J$. "Ý nghĩa:" phép trừ không đổi hướng trung bình, chỉ đổi độ phân tán.
- **Mật độ:** khoảng 35 âm tiết, 4 dòng, 1 công thức hiển thị. Điều kiện áp dụng và phạm vi chỉ trong ghi chú diễn giả.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-07` "Baseline không đổi kỳ vọng hàm điểm"): thêm giả thiết và kết luận trên lượt.
- **Ghi chú diễn giả:** ba phản ví dụ của ghi chú: $b$ phụ thuộc hành động ($b=r(A)$ cho $\widehat g_b\equiv0$); hành động lấy đều thay $\pi_\theta$; phần thưởng không khả tích.

#### `L10-205` Chứng minh: đường cơ sở không làm chệch
- **Vị trí, loại:** mạch 2; chứng minh, trang riêng.
- **Lý do tồn tại, nhu cầu:** chứng minh quan trọng của mạch (mục tiêu 1 đòi chứng minh).
- **Liên kết:** trước: `L10-204`; sau: `L10-206`. **Mục tiêu:** 1. **Ghi chú:** chứng minh Mệnh đề 10.2 (`topic-03`).
- **Mặt trang:** ba dòng bước: (1) tách $\widehat g_b=\widehat g-\sum_t\gamma^tb(S_t)\psi_t$; (2) $\mathbb E[b(S_t)\psi_t\mid H_t]=b(S_t)\sum_a\pi_\theta(a\mid S_t)\psi_\theta(S_t,a)=0$; (3) tính chất tháp, cộng tối đa $T_{\max}$ số hạng, dùng Hệ quả 09.26 cho $\widehat g$. Kết thúc $\square$.
- **Mật độ:** khoảng 30 âm tiết, 4 dòng, 1 khối `aligned`.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo chứng minh Mệnh đề 10.2 của ghi chú.
- **Ghi chú diễn giả (đến khoảng 200):** chỗ dùng từng giả thiết: $b$ không phụ thuộc $A_t$ ở bước 2, (G3) cho đổi tổng và kỳ vọng ở bước 3; $\psi_t=0$ khi $t\ge T$.

#### `L10-206` Ví dụ: đường cơ sở trên lượt hành lang
- **Vị trí, loại:** mạch 2; bước ứng dụng của cụm đường cơ sở; bước tính tay trước `L10-209`.
- **Lý do tồn tại, nhu cầu:** áp dụng $b=v_\pi$ cho đúng lượt đã cho bước ngược chiều ở `L10-107`.
- **Liên kết:** trước: `L10-205`; sau: `L10-207` (hệ số $7,6,9,8,5$ ước lượng đại lượng nào). **Mục tiêu:** 1. **Ghi chú:** Ví dụ 10.4 (`topic-03`); nguồn tr. 11.
- **Mặt trang:** dữ kiện nêu lại (lượt $1,1,1,2,1$, $G_t=-5,\dots,-1$); $v_\pi=(-12;\,-10;\,-6)$ tại $s_1,s_2,s_3$; $G_t-v_\pi(S_t)=7,6,9,8,5$; $\widehat g_b=(9{,}5;\,-9{,}5)$, cùng chiều $\nabla_\theta J=(2;\,-2)$. "Diễn giải:" lượt dài $5<12$ bước nên mọi chênh lệch dương.
- **Mật độ:** khoảng 30 âm tiết, 4 dòng, 0–1 công thức hiển thị.
- **Hình, phút:** — (dữ kiện nêu lại bằng chữ); 1,5.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.4 của ghi chú.
- **Ghi chú diễn giả:** $v_\pi$ giải từ hệ ba phương trình Bellman với $p=\tfrac12$; tọa độ thứ nhất $\tfrac12\cdot27-\tfrac12\cdot8=9{,}5$; một lượt không chứng minh được giảm phương sai, chỉ minh họa đổi dấu.

#### `L10-207` Hàm lợi thế
- **Vị trí, loại:** mạch 2; vấn đề, trực giác, định nghĩa, ví dụ của cụm lợi thế trên một trang (khái niệm ngắn).
- **Lý do tồn tại, nhu cầu:** đặt tên cho đại lượng mà hệ số $G_t-v_\pi(S_t)$ ước lượng.
- **Liên kết:** trước: `L10-206`; sau: `L10-208`. **Mục tiêu:** 1. **Ghi chú:** §2.3 đoạn đầu, Định nghĩa 10.4, Ví dụ 10.5 (`topic-05`); nguồn tr. 5, 8.
- **Mặt trang:** bốn dòng theo thứ tự vấn đề, ví dụ, định nghĩa: "Hệ số $G_t-v_\pi(S_t)$ có kỳ vọng $q_\pi(S_t,A_t)-v_\pi(S_t)$ khi biết $(H_t,A_t)$." (6); "Ví dụ. Bài toán một bước: $q_\pi=(3;\,0)$, $v_\pi=2$, hiệu $(1;\,-2)$; với $r=(4;\,1)$ hiệu vẫn $(1;\,-2)$." (9); "Định nghĩa." $A_\pi(s,a)=q_\pi(s,a)-v_\pi(s)$ gọi là hàm lợi thế (advantage function) (công thức hiển thị); "$A_\pi=0$ sau khi lượt kết thúc." (6).
- **Mật độ:** khoảng 40 âm tiết, 4 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không có trang định nghĩa lợi thế; Định nghĩa 10.4 và Ví dụ 10.5 của ghi chú. Đợt sửa sau cổng: ví dụ đưa lên trước định nghĩa.
- **Ghi chú diễn giả:** Bổ đề 03.20(d) cho kỳ vọng có điều kiện; lợi thế không đổi khi cộng hằng vào phần thưởng, nối với $\tfrac{16}9$ của `L10-106`; $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$ dùng ở mạch 4.

#### `L10-208` Gradient dạng lợi thế
- **Vị trí, loại:** mạch 2; hình thức (kết quả) của cụm lợi thế.
- **Lý do tồn tại, nhu cầu:** viết $\nabla J$ theo $A_\pi$ để mọi phương pháp sau chỉ cần ước lượng lợi thế.
- **Liên kết:** trước: `L10-207`; sau: `L10-209`. **Mục tiêu:** 1. **Ghi chú:** Mệnh đề 10.5, Ví dụ 10.5 (`topic-05`).
- **Mặt trang:** "Mệnh đề." Giả thiết của Mệnh đề 10.2, chính sách Markov dừng. (a) $\sum_a\pi_\theta(a\mid s)A_\pi(s,a)=0$; (b) $\nabla_\theta J=\mathbb E\bigl[\sum_{t<T}\gamma^tA_\pi(S_t,A_t)\psi_t\bigr]$ với $A_\pi$ của chính $\pi_\theta$. Kiểm trên bài toán một bước: $\tfrac23\cdot1\cdot\psi(s,1)+\tfrac13(-2)\psi(s,2)=(\tfrac29;\,-\tfrac29)+(\tfrac49;\,-\tfrac49)=(\tfrac23;\,-\tfrac23)$. "Chứng minh." Mệnh đề 10.2 với $b=v_\pi$, rồi tính chất tháp theo $(H_t,A_t)$.
- **Mật độ:** khoảng 30 âm tiết, 5 dòng, 2 công thức hiển thị.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Mệnh đề 10.5, Ví dụ 10.5 của ghi chú. Dạng chiếm dụng $\tfrac1{1-\gamma}\mathbb E_{\nu^\pi,\pi_\theta}[A_\pi\psi]$ chỉ trong ghi chú diễn giả vì $\nu^\pi$ được định nghĩa ở `L10-403`.
- **Ghi chú diễn giả:** dạng chiếm dụng theo Định lý 09.23; lợi thế phải của chính $\pi_\theta$; (a) là lý do $A_\pi$ có trung bình $0$ tại mỗi trạng thái.
- **Sửa 2026-11-13 (bảng phát hiện):** giả thiết theo Mệnh đề 10.5 của ghi chú: "MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$, $\pi=\pi_\theta$ Markov dừng; (b) thêm (G1)–(G4)". `deck_check`: 37 âm tiết, dòng dài nhất 20.

#### `L10-209` Thuật toán REINFORCE có đường cơ sở
- **Vị trí, loại:** mạch 2; thuật toán (hình thức) của cụm đường cơ sở; bước tính tay ở `L10-206`.
- **Lý do tồn tại, nhu cầu:** ghép đường cơ sở học được $\hat v(\cdot,w)$ với REINFORCE.
- **Liên kết:** trước: `L10-208`; sau: `L10-210`. **Mục tiêu:** 1. **Ghi chú:** Thuật toán 10.6 (`topic-05`); nguồn tr. 11.
- **Mặt trang:** "Thuật toán." sáu dòng: (1) "Đầu vào: $\pi_\theta$, $\hat v(s,w)$, $\alpha_\theta$, $\alpha_w$, $\gamma$; dừng sau $E$ lượt. Đầu ra: $\theta$, $w$." (2) "Mỗi lượt: đặt $\theta_{\mathrm{old}}$, $w_{\mathrm{old}}$; thu một lượt bằng $\pi_{\theta_{\mathrm{old}}}$." (3) "Tính $G_t$ lùi từ cuối lượt." (4) $w\leftarrow w_{\mathrm{old}}+\alpha_w\sum_t\bigl(G_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\nabla_w\hat v(S_t,w_{\mathrm{old}})$. (5) $\theta\leftarrow\theta_{\mathrm{old}}+\alpha_\theta\sum_t\gamma^t\bigl(G_t-\hat v(S_t,w_{\mathrm{old}})\bigr)\psi_t$. (6) "Lặp lại với lượt mới."
- **Mật độ:** khoảng 30 âm tiết, 6 dòng, 2 công thức trong giả mã. Không còn là ngoại lệ (bản trước 7 dòng).
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không có giả mã REINFORCE có đường cơ sở; Thuật toán 10.6 của ghi chú.
- **Ghi chú diễn giả:** $\hat v$ dùng $w_{\mathrm{old}}$ cố định trong lượt nên là đường cơ sở hợp lệ; thuật toán không là actor–critic theo Định nghĩa 10.7 (nối sang `L10-212`). Bước tính tay `L10-206` chỉ làm bước cập nhật chính sách với $b=v_\pi$ và $\gamma=1$, ngoài giả thiết $\gamma<1$ của thuật toán, đúng như ghi chú; bước cập nhật critic không được tính tay.
- **Sửa 2026-11-13 (bảng phát hiện):** "Giả thiết: (G1)–(G4); $\hat v(\cdot,w)$ bị chặn." nối vào dòng Đầu vào/Đầu ra, rồi câu thường riêng "Khởi tạo $\theta$, $w$ tùy ý; lặp $E$ lượt:" (không có nhãn "Khởi tạo:", vì nhãn này không thuộc danh sách nhãn được phép) theo Thuật toán 10.6 của ghi chú; bỏ bước 5 "Lặp lại với lượt mới" (đã nằm trong "lặp $E$ lượt"); vẫn 6 dòng. Ghi chú diễn giả bỏ câu "bước cập nhật critic không được tính tay". `deck_check`: 28 âm tiết, 6 dòng.

#### `L10-210` Bài tập: đường cơ sở hợp lệ
- **Vị trí, loại:** mạch 2; bước kiểm tra của cụm đường cơ sở; bài tập có lời giải trên mặt trang (fragment).
- **Lý do tồn tại, nhu cầu:** kiểm năng lực nhận diện đường cơ sở hợp lệ (điều kiện "không phụ thuộc $A_t$ khi biết $H_t$").
- **Liên kết:** trước: `L10-209`; sau: `L10-211`. **Mục tiêu:** 1. **Ghi chú:** Bài tập 10.1 (`topic-03`).
- **Mặt trang:** "Câu hỏi:" xác định lựa chọn nào là đường cơ sở hợp lệ: (a) $\hat v(S_t,w)$, $w$ cố định; (b) trung bình $G_0$ của các lượt khác; (c) $r(A_t)$ trên bài toán một bước; (d) $G_t$. "Lời giải:" (fragment) (a), (b) hợp lệ theo Mệnh đề 10.2; (c), (d) cho $\widehat g_b\equiv0\ne(\tfrac23;\,-\tfrac23)$.
- **Mật độ:** khoảng 45 âm tiết, 6 dòng, 0 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa và tách (`X01` "Bài tập: baseline và GAE"): phần đường cơ sở về đây, phần GAE về `L10-309`.
- **Ghi chú diễn giả:** "Gợi ý:" kiểm xem $B_t$ có phụ thuộc $A_t$ khi biết $H_t$ không; (b) cần các lượt khác độc lập với lượt đang xét.
- **Sửa 2026-11-13 (bảng phát hiện):** dòng lời giải thứ hai thành "(c), (d): $G_t-B_t=0$, nên $\widehat g_B\equiv0\ne\nabla_\theta J$; ở (c), $\nabla_\theta J=(\tfrac23;\,-\tfrac23)$." vì $(\tfrac23;-\tfrac23)$ chỉ là gradient của bài toán một bước.

#### `L10-211` Ví dụ: chuỗi hai trạng thái
- **Vị trí, loại:** mạch 2; ví dụ dẫn nhập của cụm critic (làm cụ thể vấn đề "Thuật toán 10.6 chờ hết lượt; $\hat v$ chỉ đánh giá $S_t$") và ứng dụng của Mệnh đề 10.5; ví dụ xuyên suốt của mạch 2–4.
- **Lý do tồn tại, nhu cầu:** môi trường hai bước để lợi thế tại $s_A$ phụ thuộc $s_B$; dữ kiện dùng lại ở `L10-212`–`L10-216`, mạch 3 và mạch 4.
- **Liên kết:** trước: `L10-210`; sau: `L10-212`. **Mục tiêu:** 1. **Ghi chú:** Ví dụ 10.6 (`topic-06`); nguồn tr. 12.
- **Mặt trang:** hình; $\theta=(0;\,\log2)$, $p_A=\tfrac12$, $p_B=\tfrac23$, $\gamma=0{,}9$; $v_\pi(s_B)=2$, $q_\pi(s_A,\cdot)=(1{,}8;\,1)$, $v_\pi(s_A)=1{,}4=J$; $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$; $\nabla_\theta J=(0{,}2;\,0{,}3)$ tính trực tiếp và theo Mệnh đề 10.5(b). "Câu hỏi:" kiểm (a) của Mệnh đề 10.5 tại hai trạng thái. "Lời giải:" (fragment) $\tfrac12\cdot0{,}4+\tfrac12(-0{,}4)=0$; $\tfrac23\cdot1+\tfrac13(-2)=0$.
- **Mật độ:** khoảng 35 âm tiết, 6 dòng, 0 công thức hiển thị; hình bên trái.
- **Hình, phút:** `img/lec-10/two-state-chain.svg`; 2.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.6 của ghi chú.
- **Ghi chú diễn giả:** $\psi_\theta(s,1)=(1-p_s)e_s$; đóng góp $0{,}2\,e_A$ của bước $0$ và $0{,}3\,e_B$ của bước $1$ (xác suất $p_A$, trọng số $\gamma$); $\nu^\pi=(0{,}1;\,0{,}045)$ sẽ dùng ở mạch 4.
- **Sửa 2026-11-13 (bảng phát hiện):** `.grid2.wide-right` thay `style=""` (G8).

#### `L10-212` Critic, actor và phương pháp actor–critic
- **Vị trí, loại:** mạch 2; vấn đề, trực giác, định nghĩa của cụm critic.
- **Lý do tồn tại, nhu cầu:** giới hạn một dòng của Thuật toán 10.6 (chờ hết lượt) rồi ý tưởng đánh giá hành động bằng $\hat v(S_{t+1})$.
- **Liên kết:** trước: `L10-211`; sau: `L10-212b`. **Mục tiêu:** 1. **Ghi chú:** §2.4 đoạn đầu, Định nghĩa 10.7 (`topic-06`); nguồn tr. 12.
- **Mặt trang (D1):** "Nhu cầu: cập nhật sau mỗi bước, không chờ hết lượt." "Trực quan. Chuỗi hai trạng thái, $\hat v=(1;\,1{,}5)$: sau một bước, $0+0{,}9\cdot1{,}5=1{,}35>\hat v(s_A)=1$, hành động 1 tốt hơn dự báo." "Định nghĩa 10.7." critic, actor qua mục tiêu $R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)$; "Phương pháp actor–critic cập nhật $\theta$ theo hệ số lập từ mục tiêu này, và $w$ để $\hat v$ xấp xỉ $v_{\pi_\theta}$." Dòng "Nhắc lại:" sai số TD chuyển sang `L10-212b`.
- **Mật độ:** 59 âm tiết, 4 dòng, 0 công thức hiển thị.
- **Hình, phút:** — (hình chuyển sang `L10-212b` ở bản viết); 1.
- **Quyết định:** sửa (`L10-08` "Actor–critic có thể dùng đích Monte Carlo hoặc bootstrap"): theo Định nghĩa 10.7, REINFORCE có đường cơ sở không là actor–critic; bỏ "đích". D1: thêm bước trực giác (diễn giải $1{,}35>1$), vế cập nhật $w$ của Định nghĩa 10.7, số hiệu.
- **Ghi chú diễn giả:** vì sao $1{,}35>1$ cho biết hành động 1 tốt hơn mức critic chờ đợi ngay sau một bước; Sutton và Barto (2018, §13.5, tr. 331): phép bootstrap phân biệt critic với đường cơ sở; nguồn tr. 12 dùng nghĩa rộng; mặt nạ $(1-Z_{t+1})$ (Định nghĩa 05.20, 07.19); bán gradient (Định nghĩa 07.21).

#### `L10-212b` Critic, actor và phương pháp actor–critic
- **Vị trí, loại:** mạch 2; nhắc lại sai số TD và đọc hình của cụm critic (trang tách ở bản viết, ghi vào storyboard ở D1).
- **Lý do tồn tại, nhu cầu:** một số $\delta_t$ dùng cho cả critic và actor; hình sơ đồ một bước chuyển cần chỗ đủ lớn.
- **Liên kết:** trước: `L10-212`; sau: `L10-213`. **Mục tiêu:** 1. **Ghi chú:** §2.4, hình sơ đồ actor–critic (`topic-06`).
- **Mặt trang:** "Nhắc lại: sai số TD (temporal-difference error) $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)-\hat v(S_t,w)$."; hình (cao tối đa 330 px); "Cùng một số $\delta_t$: sai lệch cho critic, hệ số của hàm điểm cho actor."
- **Mật độ:** 21 âm tiết, 2 dòng.
- **Hình, phút:** `img/lec-10/actor-critic-advantage.svg`; 0,5.
- **Quyết định:** tách (từ `L10-212`, bản viết); D1 chuyển dòng "Nhắc lại:" từ `L10-212` sang đây.
- **Ghi chú diễn giả:** sai số TD của Bài 05, 07 với mặt nạ của Bài 08; đọc hình (hai giá trị của critic, khung dừng gradient, hai mũi tên cập nhật, $I=\gamma^t$).
- **Sửa 2026-11-13 (bảng phát hiện):** "Nhắc lại: sai số sai phân thời gian (sai số TD, temporal-difference error)": lần đầu viết tắt có tên đầy đủ; hình dùng `.figure.short-l` (310 px) thay `max-height:330px`. `deck_check`: 27 âm tiết.

#### `L10-213` Sai số TD và lợi thế
- **Vị trí, loại:** mạch 2; hình thức (kết quả) và ví dụ (critic đúng) của cụm sai số TD.
- **Lý do tồn tại, nhu cầu:** cho biết $\delta_t$ ước lượng gì và độ chệch khi critic sai.
- **Liên kết:** trước: `L10-212`; sau: `L10-214`. **Mục tiêu:** 1. **Ghi chú:** Mệnh đề 10.8 (`topic-06`); nguồn tr. 12.
- **Mặt trang:** "Mệnh đề." "Giả thiết:" MDP hữu hạn, Markov, $\gamma<1$; critic cố định; $Z_{t+1}=1$ chỉ khi kết thúc; $e=\hat v-v_\pi$. "Kết luận:" (a) $\hat v=v_\pi\Rightarrow\mathbb E[\delta_t\mid S_t=s,A_t=a]=A_\pi(s,a)$; (b) tổng quát cộng thêm $\gamma\sum_{s'}P(s'\mid s,a)e(s')-e(s)$. Kiểm critic đúng $(1{,}4;\,2)$: $\delta_0=0{,}4$ hoặc $-0{,}4$, $\delta_1=1$. "Lưu ý:" điều kiện theo $(S_t,A_t)$; theo $S_t$ thì kỳ vọng bằng $0$. "Chứng minh." kỳ vọng của mục tiêu một bước là $q_\pi(s,a)+\gamma\sum P e$.
- **Mật độ:** khoảng 50 âm tiết, 6 dòng, 2 công thức hiển thị.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-09` "Critic tạo sai số sai phân thời gian"): thêm giả thiết, độ chệch (b), kiểm số.
- **Ghi chú diễn giả:** phản ví dụ bỏ critic đúng (bài toán một bước, $\hat v=1$: $\mathbb E[\delta_0\mid A_0=1]=2\ne1$); bỏ mặt nạ ($\delta_0=0{,}5$ thay $-0{,}4$); độ chệch không do bootstrap (Sutton và Barto, 2018, §13.5).
- **Sửa 2026-11-13 (bảng phát hiện):** "$Z_{t+1}=1$ khi và chỉ khi kết thúc" theo Mệnh đề 10.8 của ghi chú. `deck_check`: 55 âm tiết.

#### `L10-214` Ví dụ: hai bước actor–critic
- **Vị trí, loại:** mạch 2; bước ví dụ tính tay của cụm critic, đứng trước giả mã `L10-215`; ứng dụng của Mệnh đề 10.8(b).
- **Lý do tồn tại, nhu cầu:** thực hiện hai vòng lặp với giá trị khởi tạo, mục tiêu, sai lệch, giá trị mới.
- **Liên kết:** trước: `L10-213`; sau: `L10-215` (bảng thành giả mã). **Mục tiêu:** 1. **Ghi chú:** Ví dụ 10.7 (`topic-06`).
- **Mặt trang:** dòng dữ kiện: $w=(1;\,1{,}5)$, $\theta=(0;\,\log2)$, $\alpha_w=0{,}5$, $\alpha_\theta=1$, lượt $s_A\xrightarrow{1}s_B\xrightarrow{1}$ kết thúc, $R=(0;\,3)$. Bảng khuôn actor–critic: $t=0$: $I=1$, mục tiêu $1{,}35$, $\delta_0=0{,}35$, $w_A=1{,}175$, hướng $0{,}175\,e_A$, $\theta_A=0{,}175$, $p_A=0{,}5436$; $t=1$: $I=0{,}9$, mục tiêu $3$, $\delta_1=1{,}5$, $w_B=2{,}25$, hướng $0{,}45\,e_B$, $\theta_B=1{,}1431$, $p_B=0{,}7583$. "Diễn giải:" $\delta_0=0{,}35\ne A_\pi(s_A,1)=0{,}4$ vì critic sai.
- **Mật độ:** khoảng 25 âm tiết, 3 dòng và bảng 2 hàng × 8 cột.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.7 của ghi chú.
- **Ghi chú diễn giả:** $I=\gamma^t$ đóng vai trọng số $\gamma^t$; mặt nạ bằng $0$ ở bước $1$; kiểm $\sigma(0{,}175)$, $\sigma(1{,}1431)$.

#### `L10-215` Thuật toán actor–critic một bước
- **Vị trí, loại:** mạch 2; thuật toán của cụm critic.
- **Lý do tồn tại, nhu cầu:** quy trình đầy đủ khớp bảng của `L10-214`.
- **Liên kết:** trước: `L10-214`; sau: `L10-216`. **Mục tiêu:** 1. **Ghi chú:** Thuật toán 10.9, Nhận xét 10.10 (`topic-06`); nguồn tr. 12–13.
- **Mặt trang:** "Thuật toán." sáu dòng: (1) "Đầu vào: $\pi_\theta$, $\hat v(s,w)$, $\alpha_\theta$, $\alpha_w$, $\gamma$; dừng sau $E$ lượt. Mỗi lượt: $I\leftarrow1$, lặp tới khi kết thúc:" (2) "$A\sim\pi_\theta(\cdot\mid S)$; quan sát $R$, $S'$, $Z$." (3) $\delta\leftarrow R+\gamma(1-Z)\hat v(S',w)-\hat v(S,w)$. (4) $w\leftarrow w+\alpha_w\delta\nabla_w\hat v(S,w)$. (5) $\theta\leftarrow\theta+\alpha_\theta I\delta\psi_\theta(S,A)$. (6) $I\leftarrow\gamma I$, $S\leftarrow S'$.
- **Mật độ:** khoảng 25 âm tiết, 6 dòng. Không còn là ngoại lệ (bản trước 7 dòng).
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không có giả mã actor–critic; Thuật toán 10.9 của ghi chú.
- **Ghi chú diễn giả:** $\delta$ là hệ số đã dừng gradient trong cập nhật actor; khi cắt ngắn ($U=1$, $Z=0$) vẫn bootstrap từ quan sát cuối; bộ nhớ không phụ thuộc độ dài lượt; ước lượng chệch khi critic sai (Nhận xét 10.10).
- **Sửa 2026-11-13 (bảng phát hiện):** "Giả thiết: môi trường trả cờ $Z$." nối vào dòng Đầu vào/Đầu ra, rồi câu thường riêng "Khởi tạo $\theta$, $w$ tùy ý; mỗi lượt: $I\leftarrow1$, lặp tới khi kết thúc:" theo Thuật toán 10.9; bước 5 cũ ($I\leftarrow\gamma I$, $S\leftarrow S'$) gộp vào bước 4; vẫn 6 dòng. `deck_check`: 28 âm tiết, dòng dài nhất 17.

#### `L10-216` Bài tập: sai số TD khi critic sai
- **Vị trí, loại:** mạch 2; bước kiểm tra của cụm critic; lời giải trên mặt trang (fragment).
- **Lý do tồn tại, nhu cầu:** kiểm việc dùng Mệnh đề 10.8(b) và hệ quả lên gradient.
- **Liên kết:** trước: `L10-215`; sau: `L10-300` (hai đầu $\delta_t$ và $G_t-\hat v$ chờ được nối). **Mục tiêu:** 1. **Ghi chú:** Bài tập 10.5 (`topic-06`).
- **Mặt trang:** "Câu hỏi:" chuỗi hai trạng thái, critic $\hat v=(1;\,1{,}5)$; tính $\mathbb E[\delta_0\mid s_A,a]$ với hai hành động và tọa độ $\theta_A$ của $\mathbb E[\delta_0\psi_0]$. "Lời giải:" (fragment) $e=(-0{,}4;\,-0{,}5)$; hành động 1: $0{,}4-0{,}45+0{,}4=0{,}35$; hành động 2: $-0{,}4+0{,}4=0$; tọa độ $\theta_A$: $0{,}0875\ne0{,}2$.
- **Mật độ:** khoảng 35 âm tiết, 6 dòng.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Bài tập 10.5 của ghi chú.
- **Ghi chú diễn giả:** "Gợi ý:" lập $e$ rồi dùng (b); hành động 2 kết thúc nên không có số hạng $\gamma e(s')$; actor một bước bị chệch dù mỗi bước đúng dấu.

**Hành trình khái niệm, mạch 2.**

| cụm (dạng) | vấn đề | trực giác | ví dụ | hình thức/thuật toán | ứng dụng | kiểm tra | truyền từ ví dụ sang công thức | gộp hoặc `không áp dụng` | phút |
|---|---|---|---|---|---|---|---|---|---:|
| Đường cơ sở (khái niệm, kết quả) | `L10-106` (ví dụ dẫn nhập), `L10-200`, `L10-201` | `L10-201` | `L10-202` | `L10-203`, `L10-204`, `L10-205` | `L10-206` | `L10-210` | $X_b=(r(A)-b)\psi$ → $\widehat g_b$; $\mathbb E X_b$ không phụ thuộc $b$ → $\mathbb E[b(S_t)\psi_t\mid H_t]=0$ | vấn đề và trực giác chung `L10-201`; ví dụ dẫn nhập `L10-106` ở mạch 1 làm cụ thể vấn đề | 9,5 (gồm cụm dưới) |
| Đường cơ sở tối ưu (kết quả, bổ sung) | `L10-202` ($b=1$ cho phương sai $0$) | `không áp dụng` (hàm bậc hai của $b$ chỉ nêu trong ghi chú diễn giả) | `L10-202` | `L10-202` dòng "Lưu ý:" | `L10-202` ($b^*=1\ne2$) | Bài tập 10.4 (về nhà) | $\tfrac49(b-1)^2$ → $\mathbb E\lVert\psi\rVert^2(b-b^*)^2$ | chu trình rút gọn trên một trang (chủ đề bổ sung, phương án nén) | (trong `L10-202`) |
| Hàm lợi thế (khái niệm, kết quả) | `L10-207` (hệ số $7,6,9,8,5$ ước lượng gì) | `L10-207` | `L10-207` ($A_\pi=(1;\,-2)$) | `L10-207`, `L10-208` | `L10-209`, `L10-211` | `L10-211` ("Câu hỏi:" $\sum_a\pi A_\pi=0$) | $G_t-v_\pi(S_t)$ → $q_\pi-v_\pi$ → $A_\pi$ → $\sum\gamma^tA_\pi\psi_t$ | vấn đề, trực giác, ví dụ, định nghĩa chung `L10-207` (khái niệm ngắn) | 3,5 |
| Critic và actor–critic (khái niệm, thuật toán) | `L10-211` (ví dụ dẫn nhập), `L10-212` dòng "Nhu cầu:" | `L10-212` ($1{,}35>1$) | `L10-214` | `L10-212` (định nghĩa), `L10-212b` (sai số TD, hình), `L10-215` (thuật toán) | `L10-214` | `L10-216` | mục tiêu $0+0{,}9\cdot1{,}5$ → $R+\gamma(1-Z)\hat v(S')$ → $\delta_t$ → bước (2) của giả mã | ví dụ dẫn nhập chuỗi hai trạng thái làm cụ thể vấn đề "chờ hết lượt"; tay trước thuật toán | 9,5 (gồm cụm dưới) |
| Sai số TD và lợi thế (kết quả) | `L10-212` | `L10-212` | `L10-213` (critic đúng: $0{,}4$; $-0{,}4$; $1$) | `L10-213` | `L10-214` ($0{,}35\ne0{,}4$) | `L10-216` | $\hat v=v_\pi+e$ | ví dụ và hình thức cùng trang | (trong cụm trên) |

Phút mạch 2: trang tiêu đề $0{,}5$ + đường cơ sở $9{,}5$ (`L10-201` 1, `L10-202` 2, `L10-203` 1, `L10-204` 1,5, `L10-205` 1,5, `L10-206` 1,5, `L10-210` 1; phần "Lưu ý:" của `L10-202` thuộc cụm đường cơ sở tối ưu) + lợi thế $3{,}5$ (`L10-207` 1, `L10-208` 1,5, `L10-209` 1) + critic $9{,}5$ (`L10-211` 2, `L10-212` 1, `L10-212b` 0,5, `L10-213` 1,5, `L10-214` 2, `L10-215` 1, `L10-216` 1,5) $=23$. Câu nối giữa các bước: "phép trừ không đổi kỳ vọng" (`L10-202` → `L10-204`); "hệ số $7,6,9,8,5$ ước lượng $q_\pi-v_\pi$" (`L10-206` → `L10-207`); "Thuật toán 10.6 chờ hết lượt" (`L10-209`, `L10-211` → `L10-212`); "$\delta_0=0{,}35\ne0{,}4$" (`L10-214` → `L10-216`).

### Mạch 3. Ước lượng lợi thế tổng quát (14,5 phút)

#### `L10-300` 3. Ước lượng lợi thế tổng quát (trang tiêu đề mạch), điểm vào mạch 3
- **Vị trí, loại:** điểm vào mạch 3; `id="mach-3"`, `data-note-topic-id="lec-10-topic-07"`.
- **Lý do tồn tại, nhu cầu:** dòng dẫn nêu nhu cầu của cụm lợi tức $n$ bước và GAE (trộn hai đầu của mạch 2), nên trang là bước `vấn đề` chung của cụm.
- **Liên kết:** trước: `L10-216`; sau: `L10-301`. Kế thừa $\delta_t$ và hệ số Monte Carlo $G_t-\hat v(S_t)$; giao $\widehat A_t$, $V^{\mathrm{targ}}_t$ và Thuật toán 10.16 cho mạch 6.
- **Mục tiêu:** 2.
- **Mặt trang:** "3." + tên mạch; dòng dẫn "Muốn chọn mức trung gian giữa sai số TD và lợi tức Monte Carlo, phải trộn các lợi tức nhiều bước bằng một tham số." (25; D1 thay "điều chỉnh giữa"); từ khóa "Lợi tức n bước · Lợi tức λ · GAE · Tính không chệch cho gradient · Đoạn thu" (15).
- **Hình, phút:** —; 0,5. **Quyết định:** thêm: trang tiêu đề mạch theo `AGENTS.md` §"Trang tiêu đề mạch"; bộ cũ không có.
- **Ghi chú diễn giả (40–100):** hai ước lượng của cùng lợi thế $A_\pi(s_A,1)=0{,}4$ cho $0{,}35$ và $1{,}7$; mạch trộn chúng bằng $\lambda$, nêu khi nào gradient không chệch, và tính trên dữ liệu có cờ $Z$, $U$.

#### `L10-301` Ví dụ: ba ước lượng lợi thế trên một lượt
- **Vị trí, loại:** mạch 3; vấn đề và ví dụ dẫn nhập của cụm GAE (làm cụ thể vấn đề "chọn số phần thưởng thực trong ước lượng lợi thế"); dữ kiện dùng tiếp ở `L10-303`, `L10-304`, `L10-305`.
- **Lý do tồn tại, nhu cầu:** đặt hai đầu Monte Carlo và một bước lên cùng một lượt có số.
- **Liên kết:** trước: `L10-300`; sau: `L10-302`. **Mục tiêu:** 2. **Ghi chú:** Ví dụ 10.8 (`topic-07`); nguồn tr. 13.
- **Mặt trang:** "Nhu cầu: chọn số phần thưởng thực trong ước lượng lợi thế." Lượt $s_A\xrightarrow{1}s_B\xrightarrow{1}$ kết thúc, $R=(0;\,3)$, $\hat v=(1;\,1{,}5)$; $\delta_0=0{,}35$, $\delta_1=1{,}5$; một bước: $0{,}35$; hai bước (Monte Carlo): $3\cdot0{,}9-1=1{,}7$; trộn $0{,}2\cdot0{,}35+0{,}8\cdot1{,}7=1{,}43$; lợi thế đúng $0{,}4$. Dòng kiểm: $1{,}7=\delta_0+\gamma\delta_1$, $1{,}43=\delta_0+0{,}72\,\delta_1$.
- **Mật độ:** khoảng 30 âm tiết, 5 dòng, 0–1 công thức hiển thị; hình nhỏ bên phải.
- **Hình, phút:** `two-state-chain.svg` (nhỏ); 1,5.
- **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.8 của ghi chú.
- **Ghi chú diễn giả:** ước lượng một bước dựa vào critic sai, ước lượng Monte Carlo dựa vào một phần thưởng ngẫu nhiên; hệ số $0{,}72=\gamma\lambda$ báo trước dạng tổng.
- **Sửa 2026-11-13 (bảng phát hiện):** hình dùng `.figure.short-s` (160 px) thay `max-height:170px` (đã thử `.figure.short-m`: dòng "Kiểm:" đè chân trang, nên giữ `short-s`); ghi chú diễn giả dùng dạng khẳng định của ghi chú: "Muốn so độ chệch của ba ước lượng, cần lấy kỳ vọng theo lượt." Cờ OVERFLOW của `\xrightarrow` là dương tính giả (ảnh chụp không tràn).

#### `L10-302` Lợi tức n bước
- **Vị trí, loại:** mạch 3; hình thức (định nghĩa và bổ đề) của bước trung gian.
- **Lý do tồn tại, nhu cầu:** họ ước lượng nằm giữa hai đầu; viết thành tổng sai số TD.
- **Liên kết:** trước: `L10-301`; sau: `L10-303`. **Mục tiêu:** 2. **Ghi chú:** Định nghĩa 10.11, Bổ đề 10.12 (`topic-07`); Sutton và Barto (2018), §7.1.
- **Mặt trang:** "Định nghĩa." $G_{t:t+n}=\sum_{k<n}\gamma^kR_{t+k+1}+\gamma^n\hat v(S_{t+n},w)$ nếu $t+n<T$, $G_{t:t+n}=G_t$ nếu $t+n\ge T$, gọi là lợi tức $n$ bước (n-step return); $\widehat A^{(n)}_t=G_{t:t+n}-\hat v(S_t,w)$. "Bổ đề." với $w$ cố định, $\widehat A^{(n)}_t=\sum_{k<n}\gamma^k\delta_{t+k}$. "Chứng minh." tổng lồng nhau.
- **Mật độ:** khoảng 30 âm tiết, 4 dòng, 2 công thức hiển thị.
- **Hình, phút:** —; 1. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Định nghĩa 10.11, Bổ đề 10.12 của ghi chú.
- **Ghi chú diễn giả:** $n=1$ cho $\delta_t$, $n\ge T-t$ cho $G_t-\hat v$; trên `L10-301`, $\widehat A^{(1)}_0=0{,}35$, $\widehat A^{(2)}_0=1{,}7$.

#### `L10-303` Lợi tức λ và GAE
- **Vị trí, loại:** mạch 3; trực giác và định nghĩa của cụm GAE.
- **Lý do tồn tại, nhu cầu:** chọn một họ trọng số cho mọi lợi tức $n$ bước bằng một tham số.
- **Liên kết:** trước: `L10-302`; sau: `L10-304`. **Mục tiêu:** 2. **Ghi chú:** §3.2, Định nghĩa 10.13 (`topic-08`); Sutton và Barto (2018), §12.1; nguồn tr. 13.
- **Mặt trang:** "Trực quan." trọng số $(1-\lambda)\lambda^{n-1}$ cộng lại bằng $1$; phần dư $\lambda^{T-t-1}$ dồn vào lợi tức thực; $\lambda$ nhỏ dựa vào critic, $\lambda$ gần $1$ dựa vào phần thưởng thực. "Định nghĩa." $G^\lambda_t=(1-\lambda)\sum_{n<T-t}\lambda^{n-1}G_{t:t+n}+\lambda^{T-t-1}G_t$ gọi là lợi tức λ (λ-return); $\widehat A_t=G^\lambda_t-\hat v(S_t,w)$ gọi là GAE. Trên lượt ví dụ: $G^\lambda_0=2{,}43$, $\widehat A_0=1{,}43$.
- **Mật độ:** khoảng 40 âm tiết, 5 dòng, 2 công thức hiển thị; hình bên phải.
- **Hình, phút:** `img/lec-10/gae-weights.svg`; 1,5.
- **Quyết định:** sửa (`L10-10` "GAE trộn nhiều tầm bootstrap"): tiêu đề danh từ; định nghĩa qua lợi tức λ trước dạng tổng.
- **Ghi chú diễn giả:** đọc hình (nửa trái trọng số lợi tức $n$ bước, cột sọc $\lambda^6=0{,}262$; nửa phải $(\gamma\lambda)^k$); $\lambda=1$ đặt $G^1_t=G_t$; (12.3) của Sutton và Barto.

#### `L10-304` Dạng tổng và truy hồi của GAE
- **Vị trí, loại:** mạch 3; hình thức (kết quả) và ứng dụng (kiểm số) của cụm GAE.
- **Lý do tồn tại, nhu cầu:** dạng tính được bằng một lượt quét lùi; hai đầu mút.
- **Liên kết:** trước: `L10-303`; sau: `L10-305` (dùng dạng tổng để tính kỳ vọng). **Mục tiêu:** 2. **Ghi chú:** Mệnh đề 10.14 và chứng minh (`topic-08`); Schulman và cộng sự (2016), (16).
- **Mặt trang:** "Mệnh đề." critic cố định trong lượt. (a) $\widehat A_t=\sum_{k<T-t}(\gamma\lambda)^k\delta_{t+k}$; (b) $\lambda=0$: $\delta_t$; $\lambda=1$: $G_t-\hat v(S_t,w)$; (c) $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$, $\widehat A_T=0$. Kiểm: $0{,}35+0{,}72\cdot1{,}5=1{,}43$. "Chứng minh." thay Bổ đề 10.12 vào định nghĩa, đổi thứ tự lấy tổng với $(1-\lambda)\sum_{n>k}\lambda^{n-1}=\lambda^k$; $\lambda=1$ theo Bổ đề 10.12 với $n=T-t$; (c) tách số hạng $k=0$.
- **Mật độ:** khoảng 45 âm tiết, 6 dòng, 2 công thức hiển thị.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm; gộp trang chứng minh của kế hoạch thành dòng "Chứng minh." (phương án nén).
- **Ghi chú diễn giả (đến khoảng 200):** khối đổi thứ tự lấy tổng của Bước 2 trong ghi chú, lý do được đổi (hữu hạn số hạng khác $0$, hội tụ tuyệt đối); vì sao $\lambda=1$ xử lý riêng (thừa số $1-\lambda=0$); mệnh đề là đồng nhất thức trên từng lượt, không nói về kỳ vọng hay phương sai.

#### `L10-305` Ví dụ: GAE và gradient trên chuỗi hai trạng thái
- **Vị trí, loại:** mạch 3; vấn đề và ví dụ của cụm γ-just, đặt trước `L10-306` (sai khác thứ tự so với ghi chú, xem `outline.md`).
- **Lý do tồn tại, nhu cầu:** hỏi GAE có làm chệch ước lượng gradient không, và tách "chệch cho lợi thế" khỏi "chệch cho gradient" trên số.
- **Liên kết:** trước: `L10-304`; sau: `L10-306` (điều kiện tổng quát). **Mục tiêu:** 2. **Ghi chú:** Ví dụ 10.9 (`topic-08`); nguồn tr. 13.
- **Mặt trang:** dòng "Nhu cầu: biết GAE có làm chệch ước lượng gradient không." (10); dòng dữ kiện ($\hat v=(1;\,1{,}5)$, $p_A=\tfrac12$, $p_B=\tfrac23$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$); bảng ba hàng, ba cột $\lambda=0;\,0{,}8;\,1$: $\mathbb E[\widehat A_0\mid s_A,1]=0{,}35+0{,}45\lambda$: $0{,}35$; $0{,}71$; $0{,}8$; $\mathbb E[\widehat A_0\mid s_A,2]$: $0$ với mọi $\lambda$; tọa độ $\theta_A$ của $\mathbb E[\widehat A_0\psi_0]$: $0{,}0875$; $0{,}1775$; $0{,}2$, so với $0{,}2$. "Diễn giải: với $\lambda=1$, độ chệch $+0{,}4$ như nhau cho hai hành động nên bị khử bởi hàm điểm." (17).
- **Mật độ:** khoảng 35 âm tiết, 6 dòng (2 + 3 hàng bảng + 1).
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có; Ví dụ 10.9 của ghi chú, đặt trước Mệnh đề 10.15. Đợt sửa sau cổng: thêm dòng "Nhu cầu:".
- **Ghi chú diễn giả:** $\delta_1=R_2-1{,}5$ có kỳ vọng $0{,}5$; với $\lambda=0$ độ chệch $-0{,}05$ và $+0{,}4$ khác nhau nên không bị khử; lý do đặt ví dụ trước mệnh đề.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả thay câu siêu ngôn bằng số: "Với $\lambda=1$, lợi thế ước lượng chệch ($0{,}8$ so với $0{,}4$) nhưng tọa độ gradient đúng bằng $0{,}2$."

#### `L10-306` GAE và tính không chệch cho gradient
- **Vị trí, loại:** mạch 3; hình thức (kết quả) của cụm γ-just.
- **Lý do tồn tại, nhu cầu:** hai điều kiện đủ để GAE không làm chệch gradient.
- **Liên kết:** trước: `L10-305`; sau: `L10-307` (dữ liệu thực hành không phải lượt đầy đủ). **Mục tiêu:** 2. **Ghi chú:** Mệnh đề 10.15 (`topic-08`); Schulman và cộng sự (2016), Định nghĩa 1, Mệnh đề 1.
- **Mặt trang:** "Mệnh đề." "Giả thiết:" (G1)–(G4), MDP hữu hạn, critic cố định bị chặn, GAE tính trên lượt đầy đủ. "Kết luận:" nếu $\lambda=1$ hoặc $\hat v=v_\pi$ thì $\mathbb E[\widehat A_t\psi_t]=\mathbb E[A_\pi(S_t,A_t)\psi_t]$, nên $\mathbb E\bigl[\sum_t\gamma^t\widehat A_t\psi_t\bigr]=\nabla_\theta J$; ước lượng như vậy gọi là γ-just. "Lưu ý:" mệnh đề không khẳng định $\mathbb E[\widehat A_t\mid S_t,A_t]=A_\pi$ (ví dụ trước: $0{,}8\ne0{,}4$). "Chứng minh." (a) Mệnh đề 10.2 với $b=\hat v$; (b) Mệnh đề 10.8(a) cho từng $\delta_{t+k}$.
- **Mật độ:** khoảng 50 âm tiết, 5 dòng, 1 công thức hiển thị. Điều kiện áp dụng, phạm vi trong ghi chú diễn giả.
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Mệnh đề 10.15 của ghi chú.
- **Ghi chú diễn giả:** đánh đổi chệch–phương sai theo $\lambda$ chỉ định tính (Schulman và cộng sự, 2016, §3; nguồn tr. 13); "λ tốt nhỏ hơn γ" là quan sát thực nghiệm của bài báo; critic học được và $\lambda<1$ nên thực hành không có bảo đảm; lượt bị cắt phá điều kiện (a).
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả bỏ khẳng định "về thực nghiệm $\lambda$ tốt thường nhỏ hơn hẳn $\gamma$ tốt" (không có trong ghi chú); 137 token (trước 151).

#### `L10-307` Ví dụ: kết thúc và cắt ngắn
- **Vị trí, loại:** mạch 3; vấn đề, trực giác và ví dụ tính tay của cụm GAE trên đoạn thu; đứng trước thuật toán `L10-308`.
- **Lý do tồn tại, nhu cầu:** đoạn thu độ dài $h$ trên $N$ môi trường có bước kết thúc, bước cắt ngắn và bước dở ở biên; cờ đặt sai đổi kết quả.
- **Liên kết:** trước: `L10-306`; sau: `L10-308`. **Mục tiêu:** 2. **Ghi chú:** §3.3 đoạn đầu, Ví dụ 10.10 (`topic-09`); nguồn tr. 24.
- **Mặt trang:** "Nhu cầu: tính GAE trên đoạn thu có lượt kết thúc, bị cắt, hoặc dở ở biên." Dòng dữ kiện và bảng khuôn GAE hai hàng: $R=(1;\,2)$, $\hat v(S_0)=2$, $\hat v(S_1)=3$, $\gamma=0{,}9$, $\lambda=0{,}8$; $\delta_0=1{,}7$; (i) $Z_2=1$: $\delta_1=-1$, $\widehat A_0=0{,}98$; (ii) $U_2=1$, $\hat v(S_2)=4$: $\delta_1=2{,}6$, $\widehat A_0=3{,}572$. Kết luận: "Cùng phần thưởng và critic, hai cờ cho hai kết quả cách nhau $2{,}592$."
- **Mật độ:** 40 âm tiết, 5 dòng (Nhu cầu, dữ kiện, 2 hàng bảng, kết luận).
- **Hình, phút:** — (D1 bỏ `img/lec-08/termination-truncation.svg`: nhãn mục tiêu DQN gây nhầm, bảng đủ dữ kiện); 1,5.
- **Quyết định:** sửa (`L10-12` "Ví dụ GAE phân biệt kết thúc và truncation"): thuật ngữ "cắt ngắn"; số của Ví dụ 10.10.
- **Ghi chú diễn giả:** nhắc lại cờ ($Z_{t+1}=1$ khi MDP kết thúc; $U_{t+1}=1$ khi dừng vì giới hạn ngoài MDP; đã nêu ở `L10-102`), dòng "Nhắc lại:" của bản trước chuyển xuống đây; mục tiêu một bước theo từng cờ (D1, thay chú thích hình): $Z_2=1$ cho $R_2$, $U_2=1$ cho $R_2+\gamma\hat v(S_2)$ của quan sát cuối; kiểm (ii) bằng lợi tức λ cắt (truncated λ-return): $0{,}2\cdot3{,}7+0{,}8\cdot6{,}04=5{,}572$ (Định nghĩa 08.4, 08.6).

#### `L10-308` Thuật toán tính GAE lùi trên đoạn thu
- **Vị trí, loại:** mạch 3; thuật toán của cụm GAE trên đoạn thu.
- **Lý do tồn tại, nhu cầu:** quy tắc cờ cho đoạn thu tổng quát và mục tiêu của critic.
- **Liên kết:** trước: `L10-307` (hai bước là hai vòng của bước 3); sau: `L10-309`. **Mục tiêu:** 2. **Ghi chú:** Thuật toán 10.16, Nhận xét 10.17 (`topic-09`); nguồn tr. 24.
- **Mặt trang:** "Thuật toán." sáu dòng: (1) "Thuật toán 10.16. Đầu vào: đoạn thu $h$ bước: $R_{t+1}$, $Z_{t+1}$, $U_{t+1}$, $V_t=\hat v_{\mathrm{old}}(S_t)$, $t\le h$; $V'_{t+1}$ của quan sát cuối khi cắt. Đầu ra: …" (D1: nêu $h$, $V_h$) (2) "Nếu $Z_h=0$ và $U_h=0$, coi như cắt ngắn: $U_h\leftarrow1$, $V'_h\leftarrow V_h$." (D1: thêm điều kiện) (3) $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})V^{\mathrm{next}}_{t+1}-V_t$, $V^{\mathrm{next}}=V'$ khi $U=1$. (4) $\widehat A_h=0$; lùi: $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})(1-U_{t+1})\widehat A_{t+1}$. (5) $V^{\mathrm{targ}}_t=\widehat A_t+V_t$. (6) "Lưu ý: ghi cắt ngắn thành $Z=1$ xóa $\gamma\hat v$ của quan sát cuối." (12).
- **Mật độ:** khoảng 35 âm tiết, 6 dòng. Không còn là ngoại lệ (bản trước 7 dòng; $\gamma$, $\lambda$ ghi trong ghi chú diễn giả).
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-11` "Hai mặt nạ có hai nhiệm vụ"): thay $m_t$, $c_t$ bằng $1-Z_{t+1}$ và $(1-Z_{t+1})(1-U_{t+1})$; thêm đầu vào, $V^{\mathrm{targ}}$.
- **Ghi chú diễn giả:** giá trị bootstrap sau bước cắt là của quan sát cuối, không của quan sát đầu lượt mới; chi phí $O(hN)$; ước lượng thực hành $\sum_t\widehat A_t\psi_t$ bỏ $\gamma^t$ nên không có kỳ vọng $\nabla J$ (Nhận xét 10.17).

#### `L10-309` Bài tập: GAE trên đoạn thu
- **Vị trí, loại:** mạch 3; bước kiểm tra của cụm GAE; lời giải trên mặt trang (fragment).
- **Lý do tồn tại, nhu cầu:** kiểm việc chạy Thuật toán 10.16 khi một đoạn có cả cắt ngắn và kết thúc.
- **Liên kết:** trước: `L10-308`; sau: `L10-400` (giới hạn dữ liệu theo chính sách còn nguyên). **Mục tiêu:** 2. **Ghi chú:** Bài tập 10.7 (`topic-09`).
- **Mặt trang:** dòng "Câu hỏi: với $\gamma=0{,}9$, $\lambda=0{,}8$, quan sát cuối sau $U_2$ có $\hat v=4$, tính $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$." (11); bảng khuôn GAE bốn hàng $t=0,\dots,3$ với $R_{t+1}=1;\,2;\,0;\,3$, $Z_{t+1}$ ($Z_4=1$), $U_{t+1}$ ($U_2=1$), $\hat v_{\mathrm{old}}(S_t)=2;\,3;\,1;\,2$; ba cột $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$ hiện bằng fragment ("Lời giải:"): $\delta=1{,}7;\,2{,}6;\,0{,}8;\,1$; $\widehat A=3{,}572;\,2{,}6;\,1{,}52;\,1$ (ngắt ở $U_2$); $V^{\mathrm{targ}}=5{,}572;\,5{,}6;\,2{,}52;\,3$. Kết luận (fragment): "$\widehat A_0$ trùng trường hợp (ii) của ví dụ kết thúc và cắt ngắn." (12).
- **Mật độ:** khoảng 25 âm tiết, 6 dòng (1 + 4 hàng bảng + 1).
- **Hình, phút:** —; 2.
- **Quyết định:** sửa và tách (`X01`, phần GAE); gộp trang đề và trang lời giải của kế hoạch bằng fragment (phương án nén).
- **Ghi chú diễn giả:** "Gợi ý:" giá trị kế ở bước 1 là của quan sát cuối; hai lỗi thường gặp: bootstrap bằng $\hat v(S_2)=1$ của lượt mới cho $\delta_1=2+0{,}9-3=-0{,}1$ (còn ghi $Z_2=1$ cho $\delta_1=2-3=-1$); không ngắt truy hồi ở $U_2$ cho $\widehat A_1=3{,}6944$. D1: thêm câu nêu năng lực bài tập kiểm và câu nối sang mạch 4 (dữ liệu của chính $\pi_{\mathrm{old}}$).

**Hành trình khái niệm, mạch 3.**

| cụm (dạng) | vấn đề | trực giác | ví dụ | hình thức/thuật toán | ứng dụng | kiểm tra | truyền từ ví dụ sang công thức | gộp hoặc `không áp dụng` | phút |
|---|---|---|---|---|---|---|---|---|---:|
| Lợi tức $n$ bước và GAE (khái niệm, kết quả) | `L10-300`, `L10-301` | `L10-302` "Trực quan." (D1), `L10-303` | `L10-301` | `L10-302`, `L10-303`, `L10-304` | `L10-304` (kiểm $1{,}43$) | `L10-309` | $0{,}2\cdot0{,}35+0{,}8\cdot1{,}7$ → $\delta_0+\gamma\lambda\delta_1$ → $\sum_k(\gamma\lambda)^k\delta_{t+k}$ | ví dụ dẫn nhập đứng cùng vấn đề, trước trực giác; chứng minh bổ đề chuyển vào ghi chú diễn giả (D1) | 6,5 |
| γ-just (kết quả) | `L10-305` (câu hỏi đầu trang) | `L10-305` "Diễn giải:" | `L10-305` | `L10-306` | `L10-705` (c), `L10-706` | `L10-706` (c) | độ chệch $+0{,}4$ cho hai hành động → bị khử bởi $\mathbb E[\psi]=0$ → Mệnh đề 10.2 với $b=\hat v$ | ví dụ trước mệnh đề (lệch thứ tự so với ghi chú); ứng dụng và kiểm tra nằm ở bài tổng hợp mạch 7 | 3 |
| GAE trên đoạn thu (thuật toán) | `L10-307` | `L10-307` (hai loại bước cuối) | `L10-307` | `L10-308` | `L10-705`, `L10-706` | `L10-309` | $\delta_1=-1$ và $2{,}6$ → $(1-Z)$ trong $\delta_t$, $(1-U)$ trong truy hồi | vấn đề, trực giác, ví dụ cùng trang; tay trước thuật toán | 4,5 |

Phút mạch 3: $0{,}5$ + cụm 1 ($1{,}5+1+1{,}5+2{,}5$) + cụm 2 ($1{,}5+1{,}5$) + cụm 3 ($1{,}5+1+2$) $=14{,}5$; bài tập `L10-309` tính trong cụm 3 và là kiểm tra chung của mạch. Câu nối: "$1{,}43=\delta_0+0{,}72\,\delta_1$" (`L10-301` → `L10-304`); "GAE có làm chệch ước lượng gradient không" (`L10-304` → `L10-305`); "Mệnh đề 10.14 giả sử có cả lượt" (`L10-306` → `L10-307`).

### Mạch 4. Hàm thay thế và chặn cải thiện (22,5 phút)

#### `L10-400` 4. Hàm thay thế và chặn cải thiện (trang tiêu đề mạch), điểm vào mạch 4
- **Vị trí, loại:** điểm vào mạch 4; `id="mach-4"`, `data-note-topic-id="lec-10-topic-10"`.
- **Lý do tồn tại, nhu cầu:** mở nửa thứ hai của bài toán; dòng dẫn nêu nhu cầu của cụm hiệu hiệu năng, nên trang là bước `vấn đề` chung của cụm.
- **Liên kết:** trước: `L10-309`; sau: `L10-401`. Kế thừa giới hạn thứ hai (`L10-108`) và $A_\pi$, $\nu^\pi$ của chuỗi hai trạng thái; giao bài toán miền tin cậy cho mạch 5.
- **Mục tiêu:** 3.
- **Mặt trang:** "4." + tên mạch; dòng dẫn "Muốn dùng dữ liệu cũ cho một bước lớn, phải chặn sai số khi đánh giá chính sách mới bằng dữ liệu đó." (23); từ khóa "Hiệu hiệu năng · Hàm thay thế · Phân kỳ KL · Chặn cải thiện · Miền tin cậy" (15).
- **Hình, phút:** —; 0,5. **Quyết định:** thêm: trang tiêu đề mạch theo `AGENTS.md` §"Trang tiêu đề mạch"; bộ cũ không có.
- **Ghi chú diễn giả (40–100):** mọi ước lượng của mạch 2–3 cần dữ liệu của chính sách đang cập nhật; mạch tìm công thức chính xác cho $J(\pi')-J(\pi)$, xấp xỉ nó bằng dữ liệu của $\pi$, chặn sai số, rồi đặt bài toán miền tin cậy.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả rút còn 100 token (trước 101).

#### `L10-401` Dữ liệu cũ và chính sách mới
- **Vị trí, loại:** mạch 4; vấn đề của cụm hiệu hiệu năng.
- **Lý do tồn tại, nhu cầu:** muốn đánh giá một chính sách cụ thể trước khi chạy nó, bằng mẫu của chính sách cũ.
- **Liên kết:** trước: `L10-400`; sau: `L10-402`. **Mục tiêu:** 3. **Ghi chú:** §4 đoạn đầu (`topic-10`); nguồn tr. 4, 14.
- **Mặt trang:** "Muốn đánh giá $\pi'$ với $p'_A=0{,}6$, $p'_B=0{,}8$ trên chuỗi hai trạng thái trước khi chạy nó." Mẫu của $\pi$ chỉ cho gradient $(0{,}2;\,0{,}3)$ tại $\pi$. Hình vòng phản hồi: dữ liệu theo trạng thái mà $\pi_{\mathrm{old}}$ thăm, chất lượng của $\pi_\theta$ theo trạng thái mà $\pi_\theta$ thăm.
- **Mật độ:** khoảng 35 âm tiết, 3 dòng; hình chiếm nửa trang.
- **Hình, phút:** `img/lec-10/policy-update-feedback.svg`; 1.
- **Quyết định:** sửa (`L10-13` "Gradient lớn có thể phá chính sách"): tiêu đề danh từ; câu chung thay bằng chính sách mới cụ thể.
- **Ghi chú diễn giả:** đọc hình; nối $J=-21{,}32$ của `L10-108`; bước lớn đổi phân bố trạng thái.
- **Sửa 2026-11-13 (bảng phát hiện):** hình dùng `.figure.short-l` (310 px) thay `max-height:300px`.

#### `L10-402` Ví dụ: đổi chính sách trên chuỗi hai trạng thái
- **Vị trí, loại:** mạch 4; trực giác và ví dụ của cụm hiệu hiệu năng; dữ kiện dùng lại ở `L10-403`, `L10-405`, `L10-408`, `L10-410`.
- **Lý do tồn tại, nhu cầu:** tính mức tăng thật và hai cách cộng lợi thế trước khi phát biểu bổ đề.
- **Liên kết:** trước: `L10-401`; sau: `L10-403`. **Mục tiêu:** 3. **Ghi chú:** §4.1, Ví dụ 10.11 (`topic-10`); nguồn tr. 15.
- **Mặt trang:** "Trực quan." $\pi'$ tốt hơn nếu chọn hành động có lợi thế dương ở trạng thái nó hay thăm. Bảng khuôn chính sách: cũ $\tfrac12$, $\tfrac23$, $J=1{,}4$; mới $0{,}6$, $0{,}8$, $J=1{,}696$; $\Delta J=0{,}296$. $A_\pi(s_A,\pi')=0{,}08$, $A_\pi(s_B,\pi')=0{,}4$; $0{,}08+0{,}9\cdot0{,}6\cdot0{,}4=0{,}296$; với $p_A=0{,}5$ của chính sách cũ: $0{,}26$, lệch $0{,}036$.
- **Mật độ:** khoảng 35 âm tiết, 4 dòng và bảng 2 hàng.
- **Hình, phút:** — (bản viết bỏ hình nhỏ); 2. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo §4.1, Ví dụ 10.11 của ghi chú. D1: dòng "Tính $\Delta J$ và $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$" (định nghĩa lợi thế trung bình trên mặt trang).
- **Ghi chú diễn giả:** $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$; trọng số $0{,}9\cdot0{,}6$ là xác suất chiết khấu để $\pi'$ thăm $s_B$; dùng $0{,}5$ thay $0{,}6$ là dùng tần suất thăm của chính sách cũ.

#### `L10-403` Bổ đề hiệu hiệu năng
- **Vị trí, loại:** mạch 4; hình thức (định nghĩa phân bố chiếm dụng, bổ đề, hệ quả) và ứng dụng (Hệ quả 10.20) của cụm hiệu hiệu năng.
- **Lý do tồn tại, nhu cầu:** đẳng thức chính xác cho $J(\pi')-J(\pi)$; phân bố chiếm dụng cần cho dạng theo trạng thái.
- **Liên kết:** trước: `L10-402`; sau: `L10-404`. **Mục tiêu:** 3. **Ghi chú:** Định nghĩa 10.18, Bổ đề 10.19, Hệ quả 10.20 (`topic-10`); Kakade và Langford (2002), Bổ đề 6.1; nguồn tr. 15.
- **Mặt trang:** bốn dòng: "Định nghĩa." $\nu^\pi(s)=(1-\gamma)\sum_t\gamma^t\Pr_\pi(S_t=s,\,t<T)$ trên $\mathcal S$ gọi là phân bố chiếm dụng (occupancy distribution); "Trên chuỗi: $\nu^\pi=(0{,}1;\,0{,}045)$, $\nu^{\pi'}=(0{,}1;\,0{,}054)$." "Bổ đề. MDP hữu hạn, cùng $P$ và $\mu_0$, $\gamma<1$, chính sách Markov dừng:" $J(\pi')-J(\pi)=\tfrac1{1-\gamma}\sum_s\nu^{\pi'}(s)A_\pi(s,\pi')$ (công thức hiển thị); "Kiểm: $10(0{,}1\cdot0{,}08+0{,}054\cdot0{,}4)=0{,}296$."
- **Mật độ:** khoảng 35 âm tiết, 5 dòng, 2 công thức hiển thị. Hệ quả 10.20 chuyển vào ghi chú diễn giả (quyết định sau cổng).
- **Hình, phút:** —; 2,5.
- **Quyết định:** sửa và tách (`L10-16` "Đẳng thức, xấp xỉ rồi ràng buộc thực nghiệm"): đẳng thức đứng riêng, xấp xỉ sang `L10-405`, ràng buộc sang `L10-412`; gộp định nghĩa phân bố chiếm dụng của kế hoạch (phương án nén).
- **Ghi chú diễn giả:** "Nhắc lại:" $\nu^{\pi\top}=(1-\gamma)\mu_0^\top\Gamma_\pi$ với $\Gamma_\pi=\sum_k\gamma^kP_\pi^k$ (Định lý 03.28); khối $1-\mathbb E_\pi[\gamma^T]\le1$, ở đây $0{,}145$; "Hệ quả." (Hệ quả 10.20) $A_\pi(s,\pi')\ge0$ mọi $s$ thì $v_{\pi'}\ge v_\pi$, mở rộng Định lý 04.13 sang chính sách mới ngẫu nhiên; trên chuỗi $(1{,}696;\,2{,}4)\ge(1{,}4;\,2)$; nguồn gốc của $d^\pi$ trong nguồn.

#### `L10-404` Chứng minh: bổ đề hiệu hiệu năng
- **Vị trí, loại:** mạch 4; chứng minh, trang riêng (chứng minh quan trọng).
- **Lý do tồn tại, nhu cầu:** mục tiêu 3 đòi chứng minh; lập luận tổng lồng nhau dùng lại ở chặn cải thiện.
- **Liên kết:** trước: `L10-403`; sau: `L10-405`. **Mục tiêu:** 3. **Ghi chú:** chứng minh Bổ đề 10.19 (`topic-10`).
- **Mặt trang:** năm bước một dòng mỗi bước, hoặc một khối `aligned`: (1) $A_\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)v_\pi(s')-v_\pi(s)$, không chứa $\pi'$; (2) cùng $P$: $\mathbb E_{\pi'}[A_\pi(S_t,A_t)]=\mathbb E_{\pi'}[R_{t+1}+\gamma v_\pi(S_{t+1})-v_\pi(S_t)]$; (3)–(4) nhân $\gamma^t$, cộng, tổng lồng nhau và hội tụ trội cho $J(\pi')-\mathbb E_{\mu_0}[v_\pi(S_0)]=J(\pi')-J(\pi)$; (5) gom theo trạng thái được dạng $\nu^{\pi'}$. $\square$
- **Mật độ:** khoảng 40 âm tiết, 5 dòng, tối đa 2 khối công thức. Nếu vượt, tách thành hai trang cùng tiêu đề (Bước 1–2; Bước 3–5), giữ 1,5 phút.
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo chứng minh Bổ đề 10.19 của ghi chú.
- **Ghi chú diễn giả (đến khoảng 250):** chỗ dùng từng giả thiết: cùng $P$ ở bước 2, cùng $\mu_0$ ở bước 4, $\gamma<1$ và $R$ bị chặn cho hội tụ trội; $v_\pi=0$ sau kết thúc.

#### `L10-405` Tỉ số chính sách và hàm thay thế
- **Vị trí, loại:** mạch 4; trực giác và định nghĩa của cụm hàm thay thế.
- **Lý do tồn tại, nhu cầu:** $\nu^{\pi'}$ chưa biết; giữ phân bố của chính sách cũ và đổi phân phối hành động bằng tỉ số.
- **Liên kết:** trước: `L10-404`; sau: `L10-406`. **Mục tiêu:** 3. **Ghi chú:** §4.2, Định nghĩa 10.21 (`topic-11`); Schulman và cộng sự (2015); nguồn tr. 15.
- **Mặt trang:** "Trực quan." thay $\nu^{\pi'}$ bằng $\nu^{\mathrm{old}}$, viết $A(s,\pi_\theta)$ qua mẫu của $\pi_{\mathrm{old}}$. "Nhắc lại:" tỉ số lấy mẫu quan trọng (importance sampling ratio) với chính sách hành vi $\pi_{\mathrm{old}}$. "Định nghĩa." $\rho_t(\theta)=\pi_\theta(A_t\mid S_t)/\pi_{\mathrm{old}}(A_t\mid S_t)$ gọi là tỉ số chính sách; $\mathcal L_{\theta_{\mathrm{old}}}(\theta)=J(\theta_{\mathrm{old}})+\tfrac1{1-\gamma}\mathbb E_{S\sim\nu^{\mathrm{old}},A\sim\pi_{\mathrm{old}}}[\rho_\theta(S,A)A_{\mathrm{old}}(S,A)]$ gọi là hàm thay thế; điều kiện hỗ trợ $\pi_\theta>0\Rightarrow\pi_{\mathrm{old}}>0$. Chuỗi: $\mathcal L-J=0{,}26$.
- **Mật độ:** khoảng 50 âm tiết, 5 dòng, 2 công thức hiển thị.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa và gộp (`L10-15` "Dữ liệu cũ vẫn cho biết hướng thay đổi", `L10-22` "Tỷ số tại hành động đã lấy mẫu"): $w_t$ thành $\rho_t$, "tỷ số" thành "tỉ số"; tỉ số định nghĩa một lần ở đây, `L10-603` dùng lại.
- **Ghi chú diễn giả:** Định nghĩa 06.24; dạng $\tfrac1{1-\gamma}\sum_s\nu^{\mathrm{old}}(s)A_{\mathrm{old}}(s,\pi_\theta)$; $A_{\mathrm{old}}=A_{\pi_{\mathrm{old}}}$; $0{,}26$ là số của `L10-402` với $p_A=0{,}5$.
- **Sửa 2026-11-13 (bảng phát hiện):** thêm tên tiếng Anh "(probability ratio)" ở định nghĩa tỉ số chính sách (chuyển từ `L10-104`). `deck_check`: 50 âm tiết.

#### `L10-406` Khớp giá trị và gradient tại tham số cũ
- **Vị trí, loại:** mạch 4; hình thức (kết quả) và ứng dụng của cụm hàm thay thế.
- **Lý do tồn tại, nhu cầu:** biết hàm thay thế đúng đến bậc một tại $\theta_{\mathrm{old}}$, sai khi bước hữu hạn.
- **Liên kết:** trước: `L10-405`; sau: `L10-407` (đo khoảng cách để chặn sai số $0{,}036$). **Mục tiêu:** 3. **Ghi chú:** Mệnh đề 10.22 (`topic-11`).
- **Mặt trang:** "Mệnh đề." $\pi_{\mathrm{old}}>0$, $\nu^{\mathrm{old}}$ và $A_{\mathrm{old}}$ chính xác: $\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}})=J(\theta_{\mathrm{old}})$, $\nabla_\theta\mathcal L_{\theta_{\mathrm{old}}}(\theta_{\mathrm{old}})=\nabla_\theta J(\theta_{\mathrm{old}})$. Kiểm: $\nabla\mathcal L=10(0{,}1\cdot0{,}2;\,0{,}045\cdot\tfrac23)=(0{,}2;\,0{,}3)$. "Ý nghĩa:" bước đủ nhỏ làm $\mathcal L$ tăng thì làm $J$ tăng; bước hữu hạn thì tách ($0{,}26$ so với $0{,}296$). "Chứng minh." tại $\theta_{\mathrm{old}}$, $\rho=1$ và $\sum_a\pi A=0$; $\nabla\rho=\rho\psi$ rồi dạng chiếm dụng của Mệnh đề 10.5.
- **Mật độ:** khoảng 45 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Mệnh đề 10.22 của ghi chú.
- **Ghi chú diễn giả:** $(0{,}2;\,\tfrac23)$ là tọa độ của $\sum_a\pi A\psi$ tại hai trạng thái; khớp bậc một không cho biết bước bao xa thì còn đúng.

#### `L10-407` Biến phân toàn phần và phân kỳ KL
- **Vị trí, loại:** mạch 4; khái niệm cầu nối (`topic-12`): nhu cầu, định nghĩa, ví dụ, hai tính chất trên một trang.
- **Lý do tồn tại, nhu cầu:** sai số $0{,}036$ đến từ khác biệt phân phối hành động; cần đo khoảng cách giữa hai phân phối.
- **Liên kết:** trước: `L10-406`; sau: `L10-408`. **Mục tiêu:** 3. **Ghi chú:** Định nghĩa 10.23, Mệnh đề 10.24 (`topic-12`); Cover và Thomas (2006), Bổ đề 11.6.1; nguồn tr. 14–16.
- **Mặt trang:** "Nhu cầu: đo khác biệt giữa $\pi(\cdot\mid s)$ và $\pi'(\cdot\mid s)$." "Định nghĩa." $D_{\mathrm{TV}}(q,q')=\tfrac12\sum_a\lvert q(a)-q'(a)\rvert$ gọi là biến phân toàn phần (total variation distance, TV); $D_{\mathrm{KL}}(q\Vert q')=\sum_aq(a)\log\frac{q(a)}{q'(a)}$ gọi là phân kỳ Kullback–Leibler (Kullback–Leibler divergence, KL); KL trung bình $\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)=\mathbb E_{S\sim\nu^{\mathrm{old}}}\bigl[D_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid S)\Vert\pi_\theta(\cdot\mid S))\bigr]$. Tại $s_B$: TV $\tfrac2{15}$; KL $0{,}04873$ (cũ‖mới), $0{,}04369$ (mới‖cũ). "Mệnh đề." $D_{\mathrm{KL}}\ge0$; $D_{\mathrm{TV}}\le\sqrt{D_{\mathrm{KL}}/2}$ (Pinsker): $0{,}1333\le0{,}1561$.
- **Mật độ:** khoảng 50 âm tiết, 6 dòng, 2 công thức hiển thị. Nếu vượt 6 dòng, tách "Mệnh đề." sang trang cùng tiêu đề (0,5 phút lấy từ `L10-410`) và báo điều phối viên.
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Định nghĩa 10.23, Mệnh đề 10.24 của ghi chú.
- **Ghi chú diễn giả:** KL không đối xứng (hai số tại $s_B$); chiều cũ‖mới dùng trong TRPO, PPO-Penalty, approxKL; chứng minh $D_{\mathrm{KL}}\ge0$ bằng Jensen. $\mathbb E_{S\sim\nu}$ là tổng theo $\nu$ có khối $\le1$, không chuẩn hóa: $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}1\cdot0{,}1+0{,}045\cdot\tfrac2{15}=0{,}016$; $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)=\mathbb E_{\pi_{\mathrm{old}}}[-\log\rho_\theta]$ nối với tỉ số của `L10-405`.

#### `L10-408` Chặn cải thiện
- **Vị trí, loại:** mạch 4; trực giác và hình thức (định lý, hệ quả) của cụm chặn cải thiện.
- **Lý do tồn tại, nhu cầu:** chặn sai số của hàm thay thế theo khoảng cách trung bình giữa hai chính sách.
- **Liên kết:** trước: `L10-407`; sau: `L10-409`. **Mục tiêu:** 3. **Ghi chú:** §4.4 đoạn đầu, Định lý 10.26, Hệ quả 10.27 (`topic-13`); Achiam và cộng sự (2017), Hệ quả 1; nguồn tr. 14, 16.
- **Mặt trang:** dòng: sai số $0{,}036=10(0{,}054-0{,}045)\cdot0{,}4$ đến từ $\nu^{\pi'}-\nu^\pi$. "Trực quan." khác biệt nhỏ ở mỗi bước tích lũy dọc lượt, thừa số $\gamma/(1-\gamma)$. "Định lý." giả thiết của Bổ đề 10.19 và điều kiện hỗ trợ; $\chi_{\pi'}=\max_s\lvert A_\pi(s,\pi')\rvert$: $J(\pi')-J(\pi)\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]-\frac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}\bigr]$. "Hệ quả." thay $\mathbb E[D_{\mathrm{TV}}]$ bằng $\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$. "Ý nghĩa:" với $\gamma=0{,}9$, $1/(1-\gamma)^2=100$.
- **Mật độ:** khoảng 50 âm tiết, 6 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm; gộp trang "Sai số của hàm thay thế" của kế hoạch (Bổ đề 10.25 chuyển vào `L10-409` và ghi chú diễn giả, phương án nén).
- **Ghi chú diễn giả:** Bổ đề 10.25 và số kiểm $0{,}009\le18\cdot0{,}016=0{,}288$; Hệ quả 10.27 dùng Pinsker và Jensen; Nhận xét 10.28: Định lý 1 của Schulman và cộng sự (2015) dùng dạng lớn nhất theo trạng thái; với $\gamma=0{,}99$ thừa số là $19\,800$, nên cận không tính được từ bộ đệm.

#### `L10-409` Chứng minh: chặn cải thiện
- **Vị trí, loại:** mạch 4; chứng minh, trang riêng.
- **Lý do tồn tại, nhu cầu:** chứng minh quan trọng của mạch; nối bổ đề hiệu hiệu năng với khoảng cách.
- **Liên kết:** trước: `L10-408`; sau: `L10-410`. **Mục tiêu:** 3. **Ghi chú:** chứng minh Định lý 10.26; Bổ đề 10.25 (`topic-13`).
- **Mặt trang:** đặt $\bar a(s)=A_\pi(s,\pi')$; một khối `aligned`: (1) Bổ đề 10.19: $J(\pi')-J(\pi)=\tfrac1{1-\gamma}\langle\nu',\bar a\rangle$; (2) $\langle\nu',\bar a\rangle=\langle\nu,\bar a\rangle+\langle\nu'-\nu,\bar a\rangle$; (3) $\tfrac1{1-\gamma}\langle\nu,\bar a\rangle=\mathcal L_\pi(\pi')-J(\pi)$; (4) Hölder: $\langle\nu'-\nu,\bar a\rangle\ge-\lVert\nu'-\nu\rVert_1\chi_{\pi'}$; (5) dòng "Bổ đề 10.25: $\lVert\nu'-\nu\rVert_1\le\frac{2\gamma}{1-\gamma}\mathbb E_{S\sim\nu}[D_{\mathrm{TV}}]$ (chứng minh trong ghi chú bài giảng)." $\square$
- **Mật độ:** khoảng 30 âm tiết, 5 dòng, 2 khối công thức.
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo chứng minh Định lý 10.26 của ghi chú.
- **Ghi chú diễn giả (đến khoảng 250):** ý chính của Bổ đề 10.25 (dạng ma trận $\nu'^\top-\nu^\top=\gamma\nu^\top(P_{\pi'}-P_\pi)\Gamma_{\pi'}$, chuẩn của hàng); chỗ dùng cùng $P$, $\gamma<1$, điều kiện hỗ trợ.
- **Sửa 2026-11-13 (bảng phát hiện):** bỏ lời trỏ "(chứng minh trong ghi chú bài giảng)" trên mặt trang; ý chính của Bổ đề 10.25 vẫn trong ghi chú diễn giả. `deck_check`: 21 âm tiết.

#### `L10-410` Ví dụ: chặn cải thiện trên chuỗi hai trạng thái
- **Vị trí, loại:** mạch 4; ứng dụng của cụm chặn cải thiện.
- **Lý do tồn tại, nhu cầu:** cho thấy cận rất bảo thủ và chỉ chứng nhận bước rất nhỏ.
- **Liên kết:** trước: `L10-409`; sau: `L10-411` (cận dưới dùng như mục tiêu). **Mục tiêu:** 3. **Ghi chú:** Ví dụ 10.12, đoạn sau Hệ quả 10.27 (`topic-13`); nguồn tr. 14, 16.
- **Mặt trang:** "Tính" cận cho bước của ví dụ đổi chính sách: $\chi=0{,}4$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}016$, phạt $\frac{2\cdot0{,}9\cdot0{,}4}{0{,}01}\cdot0{,}016=1{,}152>0{,}26$, cận $-0{,}892$ dù $\Delta J=0{,}296$. Bước nhỏ chỉ đổi $p_B$: $\Delta J=\mathcal L-J=1{,}35\,\Delta p$, phạt $24{,}3\,(\Delta p)^2$, cận dương khi $\Delta p<0{,}0556$. "Diễn giải:" cận chỉ chứng nhận bước rất nhỏ.
- **Mật độ:** khoảng 35 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 2. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.12, đoạn sau Hệ quả 10.27 của ghi chú.
- **Ghi chú diễn giả:** dạng KL: $\bar D_{\mathrm{KL}}=0{,}004234$, phạt $3{,}31$; bước nhỏ tại $s_B$ không đổi phân bố trạng thái nên hàm thay thế đúng, cận vẫn phạt (Câu hỏi 2 của `L10-708`).

#### `L10-411` Cải thiện đơn điệu
- **Vị trí, loại:** mạch 4; kết quả (Hệ quả 10.29), đồng thời là bước vấn đề của cụm miền tin cậy.
- **Lý do tồn tại, nhu cầu:** cận dưới của `L10-408` cho một lược đồ lặp có $J$ không giảm; trên chuỗi, hằng phạt lớn tới mức lược đồ đứng yên, nên cần đổi phạt thành ràng buộc.
- **Liên kết:** trước: `L10-410`; sau: `L10-412`. **Mục tiêu:** 3. **Ghi chú:** Hệ quả 10.29 (`topic-14`); Schulman và cộng sự (2015), §3; nguồn tr. 16.
- **Mặt trang:** "Hệ quả." $\mathcal M_k(\pi)=\mathcal L_{\pi_k}(\pi)-C_k\,\mathbb E_{\nu^{\pi_k}}[D_{\mathrm{TV}}]$ với $C_k=\frac{2\gamma\bar\chi_k}{(1-\gamma)^2}$ (công thức hiển thị); dòng "Đánh giá và cực đại hóa chính xác: $\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)$ kéo theo $J(\pi_{k+1})\ge J(\pi_k)$."; "Chứng minh." $J\ge\mathcal M_k$ và $\mathcal M_k(\pi_k)=J(\pi_k)$. Kết luận: "Trên chuỗi, $C_k=360$: mọi bước khác $\pi_k$ làm $\mathcal M_k$ giảm, lược đồ đứng yên."
- **Mật độ:** khoảng 35 âm tiết, 4 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** tách (từ trang gộp `L10-411` của bản trước, theo cổng storyboard); nội dung lấy từ `L10-14` cũ.
- **Ghi chú diễn giả:** cực đại hóa qua hàm chặn dưới (minorize–maximize, MM); $\bar\chi_k=2$ trên chuỗi; bảo đảm cần lợi thế, phân bố chiếm dụng và phép cực đại hóa chính xác.

#### `L10-412` Bài toán miền tin cậy
- **Vị trí, loại:** mạch 4; trực giác và định nghĩa của cụm miền tin cậy.
- **Lý do tồn tại, nhu cầu:** thay phạt quá lớn ($C_k=360$) bằng ràng buộc khoảng cách.
- **Liên kết:** trước: `L10-411`; sau: `L10-412b`. **Mục tiêu:** 3. **Ghi chú:** Định nghĩa 10.30 (`topic-14`); nguồn tr. 16.
- **Mặt trang (D1):** "Trực quan. Thay phạt $C_k\mathbb E[D_{\mathrm{TV}}]$ bằng giới hạn trực tiếp cho khoảng cách giữa hai chính sách." "Định nghĩa 10.30. Bài toán miền tin cậy (trust region problem) với bán kính $\kappa>0$:" công thức hiển thị $\max_{\theta:\,\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)\le\kappa}\mathbb E_{\nu^{\mathrm{old}},\pi_{\mathrm{old}}}[\rho_\theta A_{\mathrm{old}}]$ (ràng buộc viết dưới $\max$, bỏ chữ Việt trong KaTeX). "Mục tiêu bằng $(1-\gamma)(\mathcal L-J)$, nên bài toán cực đại hóa hàm thay thế trong lân cận KL của $\pi_{\mathrm{old}}$."
- **Mật độ:** 47 âm tiết, 4 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 0,5.
- **Quyết định:** tách (từ trang gộp `L10-411` của bản trước; D1 tách tiếp phần hệ quả sang `L10-412b`).
- **Ghi chú diễn giả:** chiều KL cũ‖mới, kỳ vọng theo phân bố của chính sách cũ; $\kappa$ là $\delta$ của Schulman và cộng sự (2015); ràng buộc thay phạt của lược đồ cải thiện đơn điệu; bài toán vẫn phi tuyến.

#### `L10-412b` Mức giảm tối đa của bước miền tin cậy
- **Vị trí, loại:** mạch 4; kết quả và ứng dụng số của cụm miền tin cậy (trang mới của D1).
- **Lý do tồn tại, nhu cầu:** điều nghiệm chính xác bảo đảm, tính trên chuỗi hai trạng thái với $\chi$ của chính nghiệm (quyết định E1).
- **Liên kết:** trước: `L10-412`; sau: `L10-413`; giao bài toán cho mạch 5. **Mục tiêu:** 3. **Ghi chú:** Hệ quả 10.31 và đoạn sau (`topic-14`, ghi chú đã sửa ở commit `9a5478a`); Achiam và cộng sự (2017), Mệnh đề 1; nguồn tr. 16.
- **Mặt trang:** "Hệ quả 10.31. Nghiệm chính xác $\pi_{k+1}$ của bài toán miền tin cậy thỏa" công thức hiển thị $J(\pi_{k+1})-J(\pi_k)\ge-\sqrt{2\kappa}\,\gamma\,\chi_{\pi_{k+1}}/(1-\gamma)^2$; "Chuỗi hai trạng thái, $\kappa=0{,}004234$, bằng KL trung bình của bước $p'=(0{,}6;\,0{,}8)$."; "Nghiệm: $p_A\approx0{,}571$, $p_B\approx0{,}824$; $\chi_{\pi_{k+1}}\approx0{,}472$; cận $\approx-3{,}91$; $\Delta J\approx0{,}299$."; "Lưu ý: bài toán chỉ chặn mức giảm, không bảo đảm $J$ tăng."
- **Mật độ:** 37 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** tách (D1, từ `L10-412`); sửa số theo E1: thay "$\chi=0{,}4$: mức giảm không quá $3{,}31$" (dùng $\chi$ của bước $\pi'$) bằng nghiệm chính xác với $\chi_{\pi_{k+1}}\approx0{,}472$, cận $\approx-3{,}91$.
- **Ghi chú diễn giả:** chứng minh ($\pi_k$ khả thi nên $\mathcal L-J\ge0$, rồi chặn cải thiện dạng KL, $2\sqrt{\kappa/2}=\sqrt{2\kappa}$); phép tính $-\sqrt{0{,}008468}\cdot0{,}9\cdot0{,}472/0{,}01$; $\chi$ của nghiệm khác $\chi_{\pi'}=0{,}4$, nên $3{,}91$ khác phạt $3{,}31$ của bước $p'$; TRPO thực hành không thỏa "nghiệm chính xác".

#### `L10-413` Bài tập: đánh giá một bước cập nhật
- **Vị trí, loại:** mạch 4; bước kiểm tra chung của mạch 4 (đề); lời giải ở trang sau.
- **Lý do tồn tại, nhu cầu:** kiểm bốn công cụ của mạch trên một chính sách mới.
- **Liên kết:** trước: `L10-412`; sau: `L10-414`. **Mục tiêu:** 3. **Ghi chú:** Bài tập 10.11 (`topic-14`).
- **Mặt trang:** dòng "Câu hỏi: trên chuỗi hai trạng thái, đánh giá bước từ chính sách cũ sang $\pi''$." Bảng khuôn chính sách hai hàng (cũ: $\tfrac12$, $\tfrac23$, $J=1{,}4$; $\pi''$: $0{,}55$, $0{,}7$, $J$ cần tính). Hai dòng yêu cầu: "(a) $\Delta J$; (b) $\mathcal L-J$; (c) cận của Định lý 10.26." và "(d) $\bar D_{\mathrm{KL}}(\pi\Vert\pi'')$; xác định bước có thuộc miền tin cậy $\kappa=0{,}001$ không."
- **Mật độ:** khoảng 35 âm tiết, 5 dòng (1 + 2 hàng bảng + 2).
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm: bộ cũ không có bài tập cho mạch hàm thay thế; Bài tập 10.11 (a)–(d) của ghi chú.
- **Ghi chú diễn giả:** "Gợi ý:" tính $J$ bằng $p_A\cdot2{,}7p_B+(1-p_A)$; $A_\pi(s,\pi'')$ tại hai trạng thái; $\chi$ là giá trị lớn hơn.

#### `L10-414` Bài tập: đánh giá một bước cập nhật
- **Vị trí, loại:** mạch 4; lời giải trên mặt trang (trang kế tiếp cùng tiêu đề).
- **Lý do tồn tại, nhu cầu:** lời giải mẫu của cụm lớn hàm thay thế và chặn cải thiện.
- **Liên kết:** trước: `L10-413`; sau: `L10-500`. **Mục tiêu:** 3. **Ghi chú:** Bài tập 10.11, lời giải (`topic-14`).
- **Mặt trang:** "Lời giải:" (a) $J(\pi'')=1{,}4895$, $\Delta J=0{,}0895$; (b) $\mathcal L-J=0{,}085$; (c) $\chi=0{,}1$, $\mathbb E_\nu[D_{\mathrm{TV}}]=0{,}0065$, phạt $0{,}117$, cận $-0{,}032$; (d) $\bar D_{\mathrm{KL}}=0{,}000619\le0{,}001$. Kết luận: bước thuộc miền tin cậy và tăng $J$, dù cận âm.
- **Mật độ:** khoảng 30 âm tiết, 5 dòng.
- **Hình, phút:** —; 1. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Bài tập 10.11, lời giải của ghi chú.
- **Ghi chú diễn giả:** câu (e) của ghi chú ($0{,}317$); cận âm không có nghĩa $J$ giảm; mọi bảo đảm cần $\nu$, $A$ chính xác.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả bỏ lời trỏ "Câu (e) của ghi chú", giữ "Phạt dạng KL: $18\sqrt{0{,}000619/2}=0{,}317$".

**Hành trình khái niệm, mạch 4.**

| cụm (dạng) | vấn đề | trực giác | ví dụ | hình thức | ứng dụng | kiểm tra | truyền từ ví dụ sang công thức | gộp hoặc `không áp dụng` | phút |
|---|---|---|---|---|---|---|---|---|---:|
| Hiệu hiệu năng (kết quả) | `L10-108` (ví dụ dẫn nhập), `L10-400`, `L10-401` | `L10-402` | `L10-402` | `L10-403`, `L10-404` | `L10-403` (kiểm $0{,}296$ trên chuỗi); Hệ quả 10.20 trong ghi chú diễn giả | `L10-414` (a) | $0{,}08+0{,}9\cdot0{,}6\cdot0{,}4$ → $\tfrac1{1-\gamma}\sum_s\nu^{\pi'}A_\pi(s,\pi')$ | định nghĩa $\nu^\pi$ cùng trang với bổ đề (phương án nén); Hệ quả 10.20 rời khỏi mặt trang sau cổng | 7 |
| Hàm thay thế (khái niệm, kết quả) | `L10-402` ($0{,}26$ so với $0{,}296$) | `L10-405` | `L10-402`, `L10-405` ($0{,}26$) | `L10-405`, `L10-406` | `L10-406` ($\nabla\mathcal L=(0{,}2;\,0{,}3)$) | `L10-414` (b) | $p_A=0{,}5$ thay $0{,}6$ → $\nu^{\mathrm{old}}$ thay $\nu^{\pi'}$ → $\rho_\theta$ | ví dụ dùng lại `L10-402` | 2,5 |
| TV và KL (khái niệm cầu nối) | `L10-407` | `L10-407` | `L10-407` (tại $s_B$) | `L10-407` | `L10-408`, `L10-410` | `L10-414` (d) | khác biệt $\tfrac2{15}$ tại $s_B$ → $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$ | một trang (chủ đề cầu nối) | 1,5 |
| Chặn cải thiện (kết quả) | `L10-408` dòng đầu | `L10-408` "Trực quan." | `L10-408` ($0{,}036$) | `L10-408`, `L10-409` | `L10-410` | `L10-414` (c) | $10(0{,}054-0{,}045)\cdot0{,}4$ → $\langle\nu'-\nu,\bar a\rangle$ → Hölder | Bổ đề 10.25 trong bước cuối của chứng minh (phương án nén) | 6 |
| Miền tin cậy (kết quả, định nghĩa) | `L10-411` ($C_k=360$, lược đồ đứng yên) | `L10-412` "Trực quan." (phạt thành ràng buộc) | `L10-412b` (nghiệm chính xác, cận $-3{,}91$) | `L10-411`, `L10-412`, `L10-412b` | mạch 5 | `L10-413`, `L10-414` | $\mathcal M_k$ → ràng buộc $\bar D_{\mathrm{KL}}\le\kappa$ | vấn đề là kết quả của Hệ quả 10.29; hai trang sau khi tách; bài tập `L10-413`–`L10-414` (2,5 phút) kiểm cả mạch | 1 + 1,5 + 2,5 |

Phút mạch 4: $0{,}5+7+2{,}5+1{,}5+6+2{,}5+2{,}5=22{,}5$ (cụm hiệu hiệu năng: `L10-401` 1, `L10-402` 2, `L10-403` 2,5, `L10-404` 1,5; chặn cải thiện: `L10-408` 2,5, `L10-409` 1,5, `L10-410` 2; miền tin cậy: `L10-411` 1, `L10-412` 0,5, `L10-412b` 1). Câu nối: "mẫu của $\pi$ chỉ cho gradient tại $\pi$" (`L10-401`); "$0{,}26$ so với $0{,}296$" (`L10-402` → `L10-405` → `L10-406`); "sai số $0{,}036$ đến từ khác biệt phân phối hành động" (`L10-406` → `L10-407` → `L10-408`); "cận chỉ chứng nhận bước rất nhỏ" (`L10-410` → `L10-411`).

### Mạch 5. TRPO và gradient tự nhiên (13,5 phút)

#### `L10-500` 5. TRPO và gradient tự nhiên (trang tiêu đề mạch), điểm vào mạch 5
- **Vị trí, loại:** điểm vào mạch 5; `id="mach-5"`, `data-note-topic-id="lec-10-topic-15"`.
- **Lý do tồn tại, nhu cầu:** dòng dẫn nêu nhu cầu của cụm gradient tự nhiên (giải bài toán miền tin cậy với nhiều tham số), nên trang là bước `vấn đề` chung của cụm.
- **Liên kết:** trước: `L10-414`; sau: `L10-501`. Kế thừa bài toán miền tin cậy phi tuyến (`L10-411`); giao Thuật toán 10.37 và chi phí khoảng mười tích Fisher–vector mỗi vòng cho mạch 6.
- **Mục tiêu:** 4.
- **Mặt trang:** "5." + tên mạch; dòng dẫn "Muốn giải bài toán miền tin cậy với nhiều tham số, phải xấp xỉ KL bậc hai và tránh lập ma trận Fisher." (23); từ khóa "Ma trận Fisher · Gradient tự nhiên · Gradient liên hợp · Tìm kiếm lùi" (12).
- **Hình, phút:** —; 0,5. **Quyết định:** thêm: trang tiêu đề mạch theo `AGENTS.md` §"Trang tiêu đề mạch"; bộ cũ không có.
- **Ghi chú diễn giả (40–100):** bài toán của mạch 4 phi tuyến cả ở mục tiêu lẫn ràng buộc; xấp xỉ mục tiêu bậc một, KL bậc hai, giải bằng gradient liên hợp, kiểm bằng tìm kiếm lùi; điều còn bảo đảm sau các xấp xỉ.

#### `L10-501` Ví dụ: cùng một bước tham số, hai khoảng cách chính sách
- **Vị trí, loại:** mạch 5; vấn đề và ví dụ dẫn nhập của cụm gradient tự nhiên (làm cụ thể vấn đề "độ dài bước phải đo bằng mức đổi chính sách").
- **Lý do tồn tại, nhu cầu:** cho thấy cùng một bước trong không gian tham số đổi chính sách rất khác nhau.
- **Liên kết:** trước: `L10-500`; sau: `L10-502` (độ cong $p(1-p)$). **Mục tiêu:** 4. **Ghi chú:** §5 đoạn đầu, Ví dụ 10.13 (`topic-15`); nguồn tr. 17.
- **Mặt trang:** "Nhu cầu: đo độ dài bước bằng mức đổi chính sách." $p=\sigma(\theta)$, bước $+1$: tại $p=0{,}5$: $p'=0{,}7311$, KL $0{,}1201$; tại $p=0{,}99$: $p'=0{,}99630$, KL $0{,}00366$. Kết luận: "Cùng bước $+1$, KL ở $p=0{,}5$ gấp khoảng $33$ lần KL ở $p=0{,}99$."
- **Mật độ:** khoảng 30 âm tiết, 4 dòng.
- **Hình, phút:** —; 1. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo §5 đoạn đầu, Ví dụ 10.13 của ghi chú.
- **Ghi chú diễn giả:** KL theo chiều cũ‖mới; bước gradient thông thường dùng khoảng cách Euclid trên $\theta$, không gắn với chính sách.

#### `L10-502` Ma trận Fisher
- **Vị trí, loại:** mạch 5; trực giác (độ cong), định nghĩa và ví dụ Bernoulli.
- **Lý do tồn tại, nhu cầu:** hệ số của xấp xỉ bậc hai của KL quanh $\theta_{\mathrm{old}}$.
- **Liên kết:** trước: `L10-501`; sau: `L10-502b`. **Mục tiêu:** 4. **Ghi chú:** Định nghĩa 10.32 (`topic-15`); Schulman và cộng sự (2015), §7; nguồn tr. 17.
- **Mặt trang (D1):** "Trực quan. KL tăng theo bình phương độ dài bước; hệ số là độ cong của KL tại $\theta_{\mathrm{old}}$." "Định nghĩa 10.32." $F=\mathbb E_{S\sim\nu^{\mathrm{old}},A\sim\pi_{\mathrm{old}}}[\psi\psi^\top]$ gọi là ma trận thông tin Fisher (Fisher information matrix), nửa xác định dương. "Bernoulli logit, $p=\sigma(\theta)$: $\psi=1-p$ với xác suất $p$, $\psi=-p$ với xác suất $1-p$." "Do đó $F=p(1-p)$: $0{,}25$ tại $p=0{,}5$, $0{,}0099$ tại $p=0{,}99$."
- **Mật độ:** 47 âm tiết, 4 dòng.
- **Hình, phút:** —; 0,5.
- **Quyết định:** sửa (`L10-17` "Fisher cục bộ và ước lượng từ batch"); D1 tách theo E7 (trang kết quả quá tải): định nghĩa ở đây, Mệnh đề 10.33 sang `L10-502b`.
- **Ghi chú diễn giả:** $F$ ước lượng được từ bộ đệm; $x^\top Fx=\mathbb E[(x^\top\psi)^2]\ge0$; phép tính $\mathbb E[\psi^2]=p(1-p)$; độ cong giải thích tỉ số $33$ của `L10-501`.

#### `L10-502b` KL trung bình bậc hai
- **Vị trí, loại:** mạch 5; kết quả của cụm gradient tự nhiên (trang mới của D1).
- **Lý do tồn tại, nhu cầu:** xấp xỉ bậc hai của KL trung bình, đầu vào của Mệnh đề 10.34.
- **Liên kết:** trước: `L10-502`; sau: `L10-503`. **Mục tiêu:** 4. **Ghi chú:** Mệnh đề 10.33 (`topic-15`); nguồn tr. 17.
- **Mặt trang:** "Mệnh đề 10.33. $\pi_\theta>0$, khả vi hai lần, $\nu^{\mathrm{old}}$ cố định:" công thức hiển thị $\bar D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_{\theta_{\mathrm{old}}+\Delta})=\tfrac12\Delta^\top F\Delta+o(\lVert\Delta\rVert^2)$; "Bernoulli, bước $+1$: bậc hai $\tfrac12F$ cho $0{,}125$ và $0{,}00495$; KL thật $0{,}1201$ và $0{,}00366$."; "Chứng minh. Tại $\theta_{\mathrm{old}}$, KL và gradient bằng $0$ vì $\mathbb E[\psi]=0$; Hessian là $F$."
- **Mật độ:** 28 âm tiết, 4 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** tách (D1, từ `L10-502`).
- **Ghi chú diễn giả:** sai số bậc cao khi bước dài $1$; Hessian là $F$; hai chiều KL cùng xấp xỉ bậc hai; ràng buộc KL thành elip trong không gian tham số.

#### `L10-503` Bước gradient tự nhiên
- **Vị trí, loại:** mạch 5; hình thức (kết quả) của cụm gradient tự nhiên.
- **Lý do tồn tại, nhu cầu:** nghiệm của bài toán xấp xỉ: mục tiêu tuyến tính, ràng buộc toàn phương.
- **Liên kết:** trước: `L10-502`; sau: `L10-504`. **Mục tiêu:** 4. **Ghi chú:** Mệnh đề 10.34 (`topic-15`); Kakade (2002) theo Schulman và cộng sự (2015).
- **Mặt trang:** "Mệnh đề." Bài toán $\max_\Delta g^\top\Delta$ với $\tfrac12\Delta^\top F\Delta\le\kappa$. (a) $F$ xác định dương: $\Delta^*=\sqrt{2\kappa/(g^\top F^{-1}g)}\,F^{-1}g$, gọi là bước gradient tự nhiên (natural gradient); (b) $F$ suy biến, $g\in\operatorname{range}F$: thay $F^{-1}$ bằng $F^+$, nghiệm là $\Delta^*+\ker F$; (c) $g\notin\operatorname{range}F$: bài toán không bị chặn. "Lưu ý:" đây là nghiệm của bài toán xấp xỉ, không của bài toán miền tin cậy. "Chứng minh." bất đẳng thức Cauchy–Schwarz theo tích vô hướng $\langle u,v\rangle_F$.
- **Mật độ:** khoảng 50 âm tiết, 6 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Mệnh đề 10.34 của ghi chú.
- **Ghi chú diễn giả:** $g=\nabla\mathcal L(\theta_{\mathrm{old}})=\nabla J(\theta_{\mathrm{old}})$ theo `L10-406`; hướng $F^{-1}g$ không phụ thuộc cách tham số hóa theo nghĩa bậc nhất; (b) xảy ra ngay ở bài toán một bước (`L10-504`).

#### `L10-504` Ví dụ: bước gradient tự nhiên trên bài toán một bước
- **Vị trí, loại:** mạch 5; ứng dụng của cụm gradient tự nhiên; bước tính tay cho bước 5–6 của Thuật toán 10.37 (`L10-507` nhận ngay $j=0$).
- **Lý do tồn tại, nhu cầu:** tính $F$ suy biến, $F^+$, bước và kiểm KL thật.
- **Liên kết:** trước: `L10-503`; sau: `L10-505`. **Mục tiêu:** 4. **Ghi chú:** Ví dụ 10.14, 10.15, Nhận xét 10.35 (`topic-15`).
- **Mặt trang:** thẻ nhỏ; $F_s=\tfrac29uu^\top$, $u=(1;\,-1)$, suy biến theo hướng $(1;\,1)$; $F_s^+=\tfrac98uu^\top$; $F_s^+g=(1{,}5;\,-1{,}5)$, $g^\top F_s^+g=2$; $\kappa=0{,}01$: $\Delta^*=(0{,}15;\,-0{,}15)$. Kết quả: $\pi(1\mid s)=0{,}7297$, $J$ từ $2$ lên $2{,}189$, KL thật $0{,}009644\le\kappa$.
- **Mật độ:** khoảng 30 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** `one-step-card.svg` (nhỏ); 1,5.
- **Quyết định:** sửa (`L10-18` "Ví dụ bước natural gradient"): tiêu đề "Ví dụ: …", thuật ngữ tiếng Việt, xử lý $F$ suy biến.
- **Ghi chú diễn giả:** hướng $(1;\,1)$ cộng cùng hằng vào hai logit, không đổi chính sách, nên $\ker F$ không ảnh hưởng; $g=(\tfrac23;\,-\tfrac23)\in\operatorname{range}F_s$.
- **Sửa 2026-11-13 (bảng phát hiện):** `.grid2.wide-right` thay `style=""` (G8).

#### `L10-505` Ví dụ: hai vòng gradient liên hợp
- **Vị trí, loại:** mạch 5; vấn đề (giới hạn của việc lập $F$) và ví dụ tính tay của cụm TRPO thực hành, trước `L10-506`.
- **Lý do tồn tại, nhu cầu:** $d$ tới hàng triệu; lập $F$ tốn $O(d^2)$ bộ nhớ, nghịch đảo $O(d^3)$; chỉ cần tích $Fv$.
- **Liên kết:** trước: `L10-504`; sau: `L10-506`. **Mục tiêu:** 4. **Ghi chú:** §5.2 đoạn đầu, Ví dụ 10.16 (`topic-16`); Nocedal và Wright (2006), Chương 5; nguồn tr. 18.
- **Mặt trang:** "Nhu cầu: với $d$ cỡ $10^6$, không lập được $F$; chỉ dùng tích $Fv$." $F=\operatorname{diag}(4;\,1)$, $g=(2;\,1)$, $x_0=0$. Bảng khuôn vòng gradient liên hợp: $k=0$: $x_1=(\tfrac{10}{17};\,\tfrac5{17})$; $k=1$: $x_2=(0{,}5;\,1)=F^{-1}g$, $\tilde g_2=0$; $\tau=x_2^\top Fx_2=2$; $\kappa=0{,}01$: $\Delta=(0{,}05;\,0{,}1)$. Hình elip: bước lệch hướng $g$.
- **Mật độ:** khoảng 30 âm tiết, 4 dòng và bảng 2 hàng; hình bên phải.
- **Hình, phút:** `img/lec-10/trpo-trust-region.svg`; 2. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo §5.2 đoạn đầu, Ví dụ 10.16 của ghi chú.
- **Ghi chú diễn giả:** $F$ có hai giá trị riêng phân biệt nên hai vòng cho nghiệm đúng (Nocedal và Wright, 2006, Định lý 5.4); $\omega_0=\tfrac5{17}$, $\omega_1=0{,}85$; đọc hình (miền $\tfrac12\Delta^\top F\Delta\le\kappa$ là elip).

#### `L10-506` Thuật toán gradient liên hợp với tích Fisher–vector
- **Vị trí, loại:** mạch 5; thuật toán (bước 4 của TRPO).
- **Lý do tồn tại, nhu cầu:** quy trình khớp bảng của `L10-505`.
- **Liên kết:** trước: `L10-505`; sau: `L10-507`. **Mục tiêu:** 4. **Ghi chú:** Thuật toán 10.36 (`topic-16`); nguồn tr. 18.
- **Mặt trang:** "Thuật toán." sáu dòng: (1) "Đầu vào: $v\mapsto Fv$ (hai lần vi phân tự động), $g$, $k_{\max}$, $\varepsilon_{\mathrm{cg}}$. Đầu ra: $x\approx F^{-1}g$, $\tau\approx x^\top Fx$." (2) "Khởi tạo $x_0=0$, $\tilde g_0=-g$, $p_0=g$, $\tau_0=0$." (3) $y_k=Fp_k$, $\omega_k=\tilde g_k^\top\tilde g_k/(p_k^\top y_k)$. (4) $x_{k+1}=x_k+\omega_kp_k$, $\tilde g_{k+1}=\tilde g_k+\omega_ky_k$, $\tau_{k+1}=\tau_k+\omega_k\tilde g_k^\top\tilde g_k$. (5) "Dừng nếu $\lVert\tilde g_{k+1}\rVert\le\varepsilon_{\mathrm{cg}}$ hoặc $k+1=k_{\max}$." (6) $\xi_{k+1}=\tilde g_{k+1}^\top\tilde g_{k+1}/\tilde g_k^\top\tilde g_k$, $p_{k+1}=-\tilde g_{k+1}+\xi_{k+1}p_k$.
- **Mật độ:** khoảng 25 âm tiết, 6 dòng. Không còn là ngoại lệ (bản trước 7 dòng; công thức $Fv=\nabla_\theta((\nabla_\theta\widehat D)^\top v)$ chuyển vào ghi chú diễn giả).
- **Hình, phút:** —; 1.
- **Quyết định:** sửa và tách (`L10-19` "TRPO giải hệ rồi tìm đường"): gradient liên hợp thành trang riêng, tiêu đề danh từ.
- **Ghi chú diễn giả:** ký hiệu $\tilde g_k$, $\omega_k$, $\xi_k$ thay $r_k$, $\alpha_k$, $\beta_k$ của Nocedal và Wright (Thuật toán 5.2) vì các chữ đó đã có nghĩa; $k_{\max}=10$, tích trên khoảng $10\%$ dữ liệu (Schulman và cộng sự, 2015, Phụ lục C); $Fv=\nabla_\theta\bigl((\nabla_\theta\widehat D)^\top v\bigr)$ tại $\theta_{\mathrm{old}}$, tính bằng hai lần vi phân tự động mà không lập $F$.

#### `L10-507` Thuật toán TRPO với lợi thế GAE
- **Vị trí, loại:** mạch 5; thuật toán, trang riêng chỉ chứa giả mã.
- **Lý do tồn tại, nhu cầu:** ghép GAE (mạch 3), gradient liên hợp và tìm kiếm lùi thành một vòng lặp.
- **Liên kết:** trước: `L10-506`; sau: `L10-508`. **Mục tiêu:** 4. **Ghi chú:** Thuật toán 10.37 (`topic-16`); nguồn tr. 18–19.
- **Mặt trang:** "Thuật toán." sáu dòng: (1) "Đầu vào: $\pi_\theta$, $\hat v$, $\kappa$, $\zeta$, $j_{\max}$, $N$, $h$, $\gamma$, $\lambda$." (2) "Mỗi vòng: $\theta_{\mathrm{old}}\leftarrow\theta$; thu $h$ bước trên $N$ môi trường; bộ đệm (buffer) $\mathcal D$ gồm $hN$ mẫu, lưu $\log\pi_{\mathrm{old}}$." (3) "Tính $\widehat A_t$, $V^{\mathrm{targ}}_t$ (Thuật toán 10.16); $g=\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$." (4) "Giải $Fx=g$ (Thuật toán 10.36); $\Delta_0=\sqrt{2\kappa/(x^\top Fx)}\,x$." (5) "Tìm kiếm lùi (backtracking line search): nhận $j$ nhỏ nhất có $\widehat{\mathcal L}$ tăng và $\widehat D\le\kappa$ tại $\theta_{\mathrm{old}}+\zeta^j\Delta_0$; không có thì giữ $\theta_{\mathrm{old}}$." (6) "Vài bước hạ gradient cho critic về $V^{\mathrm{targ}}_t$."
- **Mật độ:** khoảng 55 âm tiết, 6 dòng, mỗi dòng không quá 20 âm tiết. Không còn là ngoại lệ (bản trước 9 dòng).
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa và gộp (`L10-19`, `L10-20` "TRPO chỉ nhận bước qua đủ hai kiểm tra").
- **Ghi chú diễn giả:** $\widehat{\mathcal L}(\theta)=\widehat{\mathbb E}_{\mathcal D}[\rho_t(\theta)\widehat A_t]$, $\widehat D$ là KL trung bình mẫu cũ‖mới; `L10-504` nhận ngay $j=0$; bài báo TRPO gốc dùng lợi tức Monte Carlo, bước 2 và 7 theo Schulman và cộng sự (2016); chi phí mỗi vòng.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả thêm "Giả thiết: chính sách khả vi hai lần, $\pi_\theta>0$; dữ liệu mỗi vòng do $\pi_{\mathrm{old}}$ sinh ra" (Thuật toán 10.37 của ghi chú; mặt trang ở 59 âm tiết, 6 dòng nên giả thiết đặt trong ghi chú diễn giả); bỏ câu về cách bài báo GAE khớp critic (không có trong ghi chú) và câu chi phí; câu nguồn thành "bước 2 theo cách Schulman và cộng sự (2016) ghép TRPO với GAE" (ghi chú, đoạn sau Thuật toán 10.37); 136 token (trước 176).

#### `L10-508` Phạm vi bảo đảm của TRPO thực hành
- **Vị trí, loại:** mạch 5; ứng dụng và đánh giá của cụm TRPO (nhận xét).
- **Lý do tồn tại, nhu cầu:** tách bảo đảm lý thuyết của mạch 4 khỏi điều thuật toán thực sự kiểm.
- **Liên kết:** trước: `L10-507`; sau: `L10-509`. **Mục tiêu:** 4. **Ghi chú:** Nhận xét 10.38 (`topic-16`); nguồn tr. 19.
- **Mặt trang:** sáu dòng: "Nhận xét. So với Định lý 10.26, Thuật toán 10.37 thay năm điểm:" (11); "trung bình đều thay $\nu^{\mathrm{old}}$; GAE thay $A_{\mathrm{old}}$;" (6); "mục tiêu bậc một, KL bậc hai thay hai hàm thật;" (11); "gradient liên hợp dừng sớm; ràng buộc KL thay phạt TV." (11); "Kết luận: còn lại hai bất đẳng thức trên bộ đệm:" (10); "KL trung bình mẫu $\le\kappa$; hàm thay thế mẫu tăng." (9).
- **Mật độ:** 58 âm tiết, 6 dòng, mỗi dòng không quá 11 âm tiết.
- **Hình, phút:** —; 1. **Quyết định:** sửa (phần "hai kiểm tra" của `L10-20`).
- **Ghi chú diễn giả:** TRPO thực hành không bảo đảm $J$ không giảm (Câu hỏi 4 của `L10-708`); "khoảng cách mẫu dưới bán kính" ở `L10-109` là kết luận này.

#### `L10-509` Bài tập: gradient liên hợp và bước TRPO
- **Vị trí, loại:** mạch 5; bước kiểm tra chung của mạch 5 (đề); lời giải ở trang sau.
- **Lý do tồn tại, nhu cầu:** kiểm hai vòng gradient liên hợp với $F$ không chéo và công thức bước.
- **Liên kết:** trước: `L10-508`; sau: `L10-510`. **Mục tiêu:** 4. **Ghi chú:** Bài tập 10.8 (`topic-16`).
- **Mặt trang:** "Câu hỏi:" $F=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $g=(1;\,0)$, $\kappa=0{,}01$, $x_0=0$ (dòng dữ kiện, công thức hiển thị); "Chạy hai vòng Thuật toán 10.36; tính $\tau$, $\Delta$ và kiểm $\tfrac12\Delta^\top F\Delta$." (8); "Giải thích vì sao thuật toán dừng sau hai vòng." (10); bảng khuôn vòng gradient liên hợp hai hàng ($k=0$, $1$) để trống.
- **Mật độ:** khoảng 25 âm tiết, 5 dòng (3 + 2 hàng bảng), 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa và tách (`X02` "Bài tập: bước TRPO cục bộ"): đề và lời giải hai trang như kế hoạch, vì bản gộp có 7 dòng theo quy ước đếm hàng bảng (cổng storyboard lần 2).
- **Ghi chú diễn giả:** "Gợi ý:" $\tilde g_0=-g$, $p_0=g$, $y_0=Fp_0=(2;\,1)$; kiểm $x_2=F^{-1}g$.

#### `L10-510` Bài tập: gradient liên hợp và bước TRPO
- **Vị trí, loại:** mạch 5; lời giải trên mặt trang (trang kế tiếp cùng tiêu đề).
- **Lý do tồn tại, nhu cầu:** lời giải mẫu của cụm TRPO.
- **Liên kết:** trước: `L10-509`; sau: `L10-600`. **Mục tiêu:** 4. **Ghi chú:** Bài tập 10.8, lời giải (`topic-16`).
- **Mặt trang:** "Lời giải:" bảng khuôn vòng hai hàng: $k=0$: $\omega_0=\tfrac12$, $x_1=(0{,}5;\,0)$, $\tilde g_1=(0;\,0{,}5)$; $k=1$: $\xi_1=0{,}25$, $\omega_1=\tfrac23$, $x_2=(\tfrac23;\,-\tfrac13)$, $\tilde g_2=0$. Dòng "$\tau=\tfrac23$; $\Delta=(0{,}1155;\,-0{,}0577)$; $\tfrac12\Delta^\top F\Delta=0{,}01$." Kết luận: "$F$ có hai giá trị riêng phân biệt $3$ và $1$, nên hai vòng cho nghiệm đúng." (12).
- **Mật độ:** khoảng 15 âm tiết, 5 dòng (lời giải, 2 hàng bảng, 2 dòng).
- **Hình, phút:** —; 1.
- **Quyết định:** tách (từ `L10-509` của bản trước, cổng storyboard lần 2); tương ứng trang lời giải `L10-510` của kế hoạch.
- **Ghi chú diễn giả:** bước đầy đủ thỏa ràng buộc bậc hai đúng bằng $\kappa$; Nocedal và Wright (2006), Định lý 5.4; lỗi thường gặp: quên dấu của $\tilde g_0=-g$.

**Hành trình khái niệm, mạch 5.**

| cụm (dạng) | vấn đề | trực giác | ví dụ | hình thức/thuật toán | ứng dụng | kiểm tra | truyền từ ví dụ sang công thức | gộp hoặc `không áp dụng` | phút |
|---|---|---|---|---|---|---|---|---|---:|
| Gradient tự nhiên (kết quả) | `L10-500`, `L10-501` | `L10-502` (độ cong $p(1-p)$) | `L10-501`, `L10-504` | `L10-502`, `L10-502b`, `L10-503` | `L10-504` | `L10-510` (bước $\Delta$) | $F=p(1-p)$ → $\tfrac12\Delta^\top F\Delta$ → $F^{-1}g$ | ví dụ dẫn nhập cùng vấn đề | 5,5 |
| TRPO thực hành (thuật toán) | `L10-505` dòng "Nhu cầu:" | `L10-505` (hướng liên hợp, hình elip) | `L10-505` | `L10-506`, `L10-507` | `L10-504` ($j=0$), `L10-508` | `L10-509`, `L10-510` | $\tau=x_2^\top Fx_2=2$ → bước 5 của Thuật toán 10.37 | vấn đề, trực giác, ví dụ cùng trang; tay trước thuật toán | 7,5 |

Phút mạch 5: $0{,}5+(1+1{,}5+1{,}5+1{,}5)+(2+1+1{,}5+1+1+1)=13{,}5$. Câu nối: "cùng bước $+1$, KL gấp $33$ lần" (`L10-501` → `L10-502`); "nghiệm của bài toán xấp xỉ" (`L10-503` → `L10-504`); "không lập được $F$" (`L10-504` → `L10-505`); "còn lại hai bất đẳng thức trên bộ đệm" (`L10-508` → `L10-509`, `L10-510` → `L10-600`).

### Mạch 6. Tối ưu chính sách gần kề (PPO) (25,5 phút)

#### `L10-600` 6. Tối ưu chính sách gần kề (PPO) (trang tiêu đề mạch), điểm vào mạch 6
- **Vị trí, loại:** điểm vào mạch 6; `id="mach-6"`, `data-note-topic-id="lec-10-topic-17"`.
- **Lý do tồn tại, nhu cầu:** dòng dẫn nêu nhu cầu của cụm PPO-Clip, nên trang là bước `vấn đề` chung của cụm.
- **Liên kết:** trước: `L10-509`; sau: `L10-601`. Kế thừa chi phí và bộ máy bậc hai của TRPO, $\widehat A_t$, $V^{\mathrm{targ}}_t$ của mạch 3; giao Thuật toán 10.49 và danh sách điều không được bảo đảm cho mạch 7.
- **Mục tiêu:** 5.
- **Mặt trang:** "6." + tên mạch; dòng dẫn "Muốn giữ chính sách mới gần chính sách cũ bằng tối ưu bậc một, phải đưa giới hạn khoảng cách vào hàm mục tiêu." (24); từ khóa "Mục tiêu cắt · PPO-Penalty · Hàm mất mát tổng · Đại lượng chẩn đoán · Chi tiết cài đặt" (16).
- **Hình, phút:** —; 0,5. **Quyết định:** thêm: trang tiêu đề mạch theo `AGENTS.md` §"Trang tiêu đề mạch"; bộ cũ không có.
- **Ghi chú diễn giả (40–100):** hai hàng của bài toán gặp nhau: lợi thế GAE đi vào một mục tiêu cắt tối ưu bằng Adam trên mini-batch; cái giá là không còn cận KL.

#### `L10-601` Giới hạn của TRPO
- **Vị trí, loại:** mạch 6; vấn đề và trực giác của cụm PPO-Clip.
- **Lý do tồn tại, nhu cầu:** giới hạn một dòng của TRPO, rồi ý tưởng cắt tỉ số.
- **Liên kết:** trước: `L10-600`; sau: `L10-602`. **Mục tiêu:** 5. **Ghi chú:** §5 cuối, §6 đoạn đầu, §6.1 đoạn 1 (`topic-17`); Schulman và cộng sự (2017), §1; nguồn tr. 19–20.
- **Mặt trang:** hai dòng giới hạn: "Mỗi vòng TRPO cần khoảng $10$ tích Fisher–vector và một lượt tìm kiếm lùi." (13) / "TRPO cần bộ máy bậc hai riêng cho chính sách." (10). Dòng: hàm thay thế mẫu $\widehat{\mathbb E}_{\mathcal D}[\rho_t\widehat A_t]$ tuyến tính theo $\rho_t$, nên tối ưu không ràng buộc đẩy $\rho_t$ đi xa. "Trực quan." bỏ phần thưởng khi $\rho_t$ ra ngoài $[1-\epsilon,\,1+\epsilon]$ theo hướng có lợi, giữ phần phạt theo hướng bất lợi.
- **Mật độ:** khoảng 50 âm tiết, 4 dòng (dòng giới hạn cũ 22 âm tiết tách thành hai dòng).
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-21` "PPO cần bước gần nhưng chỉ dùng tối ưu bậc nhất"): tiêu đề danh từ; giới hạn có số.
- **Ghi chú diễn giả:** Schulman và cộng sự (2017, §1): TRPO tương đối phức tạp, không tương thích với dropout hoặc dùng chung tham số giữa chính sách và critic; $\epsilon$ là bán kính cắt (clip range), không phải bán kính KL.

#### `L10-602` Ví dụ: hai hàm thay thế mẫu trên bài toán một bước
- **Vị trí, loại:** mạch 6; ví dụ của cụm PPO-Clip.
- **Lý do tồn tại, nhu cầu:** thấy đoạn phẳng của mục tiêu cắt trên một hàm một biến.
- **Liên kết:** trước: `L10-601`; sau: `L10-603`. **Mục tiêu:** 5. **Ghi chú:** Ví dụ 10.17 (`topic-17`); nguồn tr. 21.
- **Mặt trang:** dữ kiện: bộ đệm hành động $1,1,2$, $\widehat A=(1;\,1;\,-2)$, $\epsilon=0{,}2$, $\rho(1)=1{,}5p$, $\rho(2)=3(1-p)$. $\mathcal L^{\mathrm{CPI}}=3p-2$; $\mathcal L^{\mathrm{CLIP}}=3p-2$ khi $p\le0{,}7\overline3$, $p-0{,}5\overline3$ khi $0{,}7\overline3\le p\le0{,}8$, $0{,}2\overline6$ khi $p\ge0{,}8$. "Diễn giải:" từ $p=0{,}8$ gradient của mục tiêu cắt bằng $0$.
- **Mật độ:** khoảng 30 âm tiết, 4 dòng, 1 công thức hiển thị (dạng cases); hình bên phải.
- **Hình, phút:** `img/lec-10/ppo-one-step-plateau.svg`; 2. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Ví dụ 10.17 của ghi chú.
- **Ghi chú diễn giả:** khúc gấp thứ nhất: mẫu hành động 2 có $\rho<0{,}8$ với lợi thế âm; khúc thứ hai: $\rho(1)>1{,}2$; đọc hình; $\mathcal L^{\mathrm{CPI}}$ tăng không giới hạn trên $[0,1]$ theo $p$.
- **Sửa 2026-11-13 (bảng phát hiện):** "hàm thay thế mẫu ${\mathcal L^{\mathrm{CPI}}=3p-2}$" gọi tên đại lượng trước khi `L10-603` định nghĩa. `deck_check`: 20 âm tiết.

#### `L10-603` Mục tiêu PPO-Clip
- **Vị trí, loại:** mạch 6; hình thức (định nghĩa) của cụm PPO-Clip.
- **Lý do tồn tại, nhu cầu:** công thức chung của hai hàm trên `L10-602`.
- **Liên kết:** trước: `L10-602`; sau: `L10-604`. **Mục tiêu:** 5. **Ghi chú:** Định nghĩa 10.39 (`topic-17`); Schulman và cộng sự (2017), (6)–(7); nguồn tr. 21.
- **Mặt trang:** "Định nghĩa." với $\epsilon\in(0,1)$ và lợi thế cố định $\widehat A_t$: $\ell^{\mathrm{CLIP}}_t(\theta)=\min\bigl(\rho_t(\theta)\widehat A_t,\ \operatorname{clip}(\rho_t(\theta),1-\epsilon,1+\epsilon)\widehat A_t\bigr)$; $\mathcal L^{\mathrm{CLIP}}=\widehat{\mathbb E}_{\mathcal D}[\ell^{\mathrm{CLIP}}_t]$ gọi là mục tiêu cắt; $\mathcal L^{\mathrm{CPI}}=\widehat{\mathbb E}_{\mathcal D}[\rho_t\widehat A_t]$.
- **Mật độ:** khoảng 25 âm tiết, 3 dòng, 2 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa và gộp (`L10-22`, phần công thức của `L10-24` "Công thức PPO-Clip phụ thuộc dấu lợi thế"): $w_t$ thành $\rho_t$; tỉ số đã định nghĩa ở `L10-405`.
- **Ghi chú diễn giả:** CPI là lặp chính sách bảo thủ (conservative policy iteration) (Kakade và Langford, 2002); $\widehat{\mathbb E}_{\mathcal D}$ là trung bình đều trên bộ đệm, khác $\mathbb E_{\nu}$ của mạch 4.
- **Sửa 2026-11-13 (bảng phát hiện):** thêm dòng "Chỉ số CPI: lặp chính sách bảo thủ (conservative policy iteration)." trên mặt trang (trước chỉ trong ghi chú diễn giả). `deck_check`: 31 âm tiết, 5 dòng.

#### `L10-604` Dạng theo dấu của lợi thế
- **Vị trí, loại:** mạch 6; hình thức (kết quả) của cụm PPO-Clip.
- **Lý do tồn tại, nhu cầu:** đọc phép $\min$ thành hai trường hợp và xác định miền gradient bằng $0$.
- **Liên kết:** trước: `L10-603`; sau: `L10-605`. **Mục tiêu:** 5. **Ghi chú:** Mệnh đề 10.40 (`topic-17`); nguồn tr. 22.
- **Mặt trang:** "Mệnh đề." (a) $\widehat A_t>0$: $\ell^{\mathrm{CLIP}}_t=\widehat A_t\min(\rho_t,1+\epsilon)$; (b) $\widehat A_t<0$: $\ell^{\mathrm{CLIP}}_t=\widehat A_t\max(\rho_t,1-\epsilon)$; (c) gradient bằng $0$ trên $\{\widehat A_t>0,\rho_t>1+\epsilon\}\cup\{\widehat A_t<0,\rho_t<1-\epsilon\}$, bằng $\widehat A_t\rho_t\psi_t$ ở phần còn lại. "Ý nghĩa:" phía bất lợi không bị cắt. "Chứng minh." xét ba khoảng của $\rho_t$.
- **Mật độ:** khoảng 35 âm tiết, 5 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-24`): tiêu đề danh từ; thêm miền gradient bằng $0$. Đánh số (a)–(c) trên mặt trang ứng với (a), (b), (d) của Mệnh đề 10.40; ghi chú diễn giả nêu ứng số.
- **Ghi chú diễn giả:** trường hợp $\widehat A_t=0$; gradient $\nabla\rho=\rho\psi$; tập gradient bằng $0$ phụ thuộc dấu, khác tỉ lệ cắt (nối `L10-611`).
- **Sửa 2026-11-13 (bảng phát hiện):** nhãn ý theo ghi chú: thêm "(c) $\widehat A_t=0$: $\ell^{\mathrm{CLIP}}_t=0$" và đổi "(c) gradient bằng $0$" thành "(d)"; ghi chú diễn giả bỏ câu đối chiếu nhãn. `deck_check`: 38 âm tiết, 6 dòng.

#### `L10-605` Ví dụ: bốn mẫu
- **Vị trí, loại:** mạch 6; ứng dụng của cụm PPO-Clip.
- **Lý do tồn tại, nhu cầu:** áp dạng theo dấu cho bốn tổ hợp dấu–phía.
- **Liên kết:** trước: `L10-604`; sau: `L10-606`. **Mục tiêu:** 5. **Ghi chú:** Ví dụ 10.18 (`topic-17`); nguồn tr. 22.
- **Mặt trang:** $\epsilon=0{,}2$; bảng khuôn mẫu PPO: $(\widehat A;\,\rho)=(2;\,1{,}3)$: $\ell=2{,}4$, gradient bằng $0$: có; $(-2;\,0{,}7)$: $-1{,}6$, có; $(2;\,0{,}7)$: $1{,}4$, không; $(-2;\,1{,}3)$: $-2{,}6$, không. Hình hai khung theo dấu của lợi thế.
- **Mật độ:** khoảng 15 âm tiết, 2 dòng và bảng 4 hàng; hình bên phải.
- **Hình, phút:** `img/lec-10/ppo-clipping-signs.svg`; 1.
- **Quyết định:** sửa và gộp (`L10-23` "Hai số đại diện cho phần bị chặn", `L10-25` "Trong và ngoài dải clipping"): bốn mẫu một bảng.
- **Ghi chú diễn giả:** hai mẫu có gradient khác $0$ nằm ngoài khoảng ở phía bất lợi; đọc hình.

#### `L10-606` Chặn dưới bi quan
- **Vị trí, loại:** mạch 6; hình thức (kết quả) và nhận xét phạm vi của cụm PPO-Clip.
- **Lý do tồn tại, nhu cầu:** quan hệ của mục tiêu cắt với hàm thay thế mẫu; điều mục tiêu cắt không bảo đảm.
- **Liên kết:** trước: `L10-605`; sau: `L10-607`. **Mục tiêu:** 5. **Ghi chú:** Mệnh đề 10.41, Nhận xét 10.42 (`topic-17`); nguồn tr. 21–22, 35.
- **Mặt trang:** "Mệnh đề." lợi thế cố định, $\pi_{\mathrm{old}}>0$, bộ đệm hữu hạn: (a) $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, gọi là chặn dưới bi quan (pessimistic bound); (b) hai hàm trùng nhau trên một lân cận của $\theta_{\mathrm{old}}$, cùng giá trị và gradient $\widehat{\mathbb E}_{\mathcal D}[\widehat A_t\psi_t]$. "Chứng minh." $\min$ không vượt số hạng thứ nhất; gần $\theta_{\mathrm{old}}$ mọi $\rho_t\in(1-\epsilon,1+\epsilon)$. "Lưu ý: mục tiêu cắt không chặn KL." / "Tỉ số vẫn ra ngoài khoảng qua Adam, mini-batch khác, mẫu khác cùng trạng thái."
- **Mật độ:** khoảng 50 âm tiết, 5 dòng (dòng "Lưu ý:" cũ 22 âm tiết tách thành hai dòng 7 và 12), 1 công thức hiển thị.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-26` "Clipping không phải ràng buộc KL"): tiêu đề gọi tên kết quả; câu phạm vi thành "Lưu ý:".
- **Ghi chú diễn giả:** bước đầu tiên của PPO trùng bước CPI, mọi $\rho_t=1$ là phép kiểm cài đặt; ví dụ $p=0{,}85$ ở `L10-614` cho KL $0{,}1042$ dù mục tiêu phẳng từ $p=0{,}8$; $\epsilon$ không phải bán kính KL.
- **Sửa 2026-11-13 (bảng phát hiện):** ý "hai hàm trùng nhau quanh $\theta_{\mathrm{old}}$" đổi nhãn (b) thành (c) theo Mệnh đề 10.41 của ghi chú; ghi chú diễn giả "Theo (c)". 135 token.

#### `L10-607` PPO-Penalty
- **Vị trí, loại:** mạch 6; vấn đề, trực giác và ví dụ tính tay của cụm PPO-Penalty (trang thứ nhất của hai trang cùng tiêu đề).
- **Lý do tồn tại, nhu cầu:** `L10-606` cho thấy mục tiêu cắt không chặn KL; biến thể này đưa KL vào mục tiêu dưới dạng phạt, với hệ số chỉnh theo KL đo được.
- **Liên kết:** trước: `L10-606`; sau: `L10-608` (quy tắc tổng quát). **Mục tiêu:** 5. **Ghi chú:** §6.2, Ví dụ 10.19 (`topic-18`); Schulman và cộng sự (2017), §4; nguồn tr. 38.
- **Mặt trang:** "Nhu cầu: một hệ số phạt $\beta$ cố định khó cho kết quả tốt trên nhiều bài toán." (13); "Trực quan. KL đi vào mục tiêu như một chi phí; $\beta$ tăng khi KL đo được lớn, giảm khi nhỏ." (17); "Ví dụ. Bộ đệm hành động $1,1,2$, $\beta=1$, KL mục tiêu $0{,}01$, hai ngưỡng $0{,}00667$ và $0{,}015$." (14); "$p=0{,}75$: KL $0{,}01737>0{,}015$, nên $\beta=2$." (3); "$p=0{,}7$: KL $0{,}00259<0{,}00667$, nên $\beta=0{,}5$." (3).
- **Mật độ:** khoảng 50 âm tiết, 5 dòng, 0 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** tách (từ trang gộp `L10-607` của bản trước, theo cổng storyboard); trực giác chuyển từ ghi chú diễn giả lên mặt trang; ví dụ đứng trước quy tắc.
- **Ghi chú diễn giả:** mục tiêu phạt KL (KL-penalized objective); hai ngưỡng là $\kappa_{\mathrm{targ}}/1{,}5$ và $1{,}5\,\kappa_{\mathrm{targ}}$; KL theo chiều cũ‖mới tính dạng đóng trên bộ đệm của bài toán một bước.

#### `L10-608` PPO-Penalty
- **Vị trí, loại:** mạch 6; hình thức (định nghĩa), nhận xét phạm vi và kiểm tra của cụm PPO-Penalty (trang thứ hai cùng tiêu đề).
- **Lý do tồn tại, nhu cầu:** quy tắc tổng quát khớp hai trường hợp của `L10-607`; câu hỏi kiểm việc dùng hai ngưỡng.
- **Liên kết:** trước: `L10-607`; sau: `L10-609`. **Mục tiêu:** 5. **Ghi chú:** Định nghĩa 10.43, Nhận xét 10.44, Bài tập 10.12(d) (`topic-18`); nguồn tr. 38.
- **Mặt trang:** "Định nghĩa." $\mathcal L^{\mathrm{KLPEN}}(\theta)=\widehat{\mathbb E}_{\mathcal D}[\rho_t\widehat A_t-\beta D_t(\theta)]$, $D_t$ là KL cũ‖mới tại $S_t$ (công thức hiển thị); quy tắc sau mỗi lần cập nhật, hai dòng: "$\widehat D<\kappa_{\mathrm{targ}}/1{,}5$: $\beta\leftarrow\beta/2$." và "$\widehat D>1{,}5\,\kappa_{\mathrm{targ}}$: $\beta\leftarrow2\beta$; còn lại giữ $\beta$." "Lưu ý: không có bảo đảm $J$ tăng; hằng $1{,}5$ và $2$ chọn theo kinh nghiệm." "Câu hỏi: $\beta=1$, $\kappa_{\mathrm{targ}}=0{,}01$; tính $\beta$ mới khi $\widehat D=0{,}018$, khi $\widehat D=0{,}008$." "Lời giải:" (fragment) "$\beta=2$; giữ $\beta=1$ vì $0{,}008$ nằm giữa hai ngưỡng."
- **Mật độ:** khoảng 45 âm tiết, 6 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** tách (từ trang gộp `L10-607` của bản trước); câu hỏi lấy từ Bài tập 10.12(d), chuyển từ trang bài tập PPO lên đây để `L10-619` không quá 6 dòng và cụm PPO-Penalty có bước kiểm tra ngay sau định nghĩa.
- **Ghi chú diễn giả:** hệ số phạt thích nghi (adaptive KL penalty coefficient); $\kappa_{\mathrm{targ}}$ không phải ràng buộc; trong thí nghiệm MuJoCo của bài báo, cắt với $\epsilon=0{,}2$ có điểm trung bình cao nhất (Schulman và cộng sự, 2017, Bảng 1), một kết luận thực nghiệm của bài báo đó; lỗi thường gặp là so KL trực tiếp với $\kappa_{\mathrm{targ}}$.

#### `L10-609` Hàm mất mát tổng
- **Vị trí, loại:** mạch 6; vấn đề và định nghĩa của cụm thuật toán PPO.
- **Lý do tồn tại, nhu cầu:** huấn luyện actor và critic trong cùng một bước tối ưu.
- **Liên kết:** trước: `L10-608`; sau: `L10-610`. **Mục tiêu:** 5. **Ghi chú:** Định nghĩa 10.45, 10.46 (`topic-19`); nguồn tr. 23.
- **Mặt trang:** "Nhu cầu: huấn luyện actor và critic bằng một hàm mất mát." "Định nghĩa." entropy $\mathcal H(\pi(\cdot\mid s))=-\sum_a\pi(a\mid s)\log\pi(a\mid s)$; $L(\theta,w)=-\mathcal L^{\mathrm{CLIP}}(\theta)+c_1L^V(w)-c_2\widehat{\mathbb E}_{\mathcal B}[\mathcal H]$, $L^V=\widehat{\mathbb E}_{\mathcal B}[(\hat v(S_t,w)-V^{\mathrm{targ}}_t)^2]$, gọi là hàm mất mát tổng. "Lưu ý: $V^{\mathrm{targ}}_t$ dùng $\widehat A^{\mathrm{raw}}_t$." (3) / "Chuẩn hóa lợi thế theo mini-batch phụ thuộc hành động của mẫu," (11) / "nên không thỏa giả thiết của Mệnh đề 10.2." (8)
- **Mật độ:** khoảng 45 âm tiết, 6 dòng (dòng "Lưu ý:" cũ 22 âm tiết tách thành ba dòng), 2 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-27` "Actor chuẩn hóa lợi thế, critic giữ đích thô"): $\widehat A^{\mathrm{actor}}$ thành $\widehat A_t$, "đích" thành "mục tiêu".
- **Ghi chú diễn giả:** dấu: $\mathcal L^{\mathrm{CLIP}}$ cực đại hóa, $L$ cực tiểu hóa; $c_1$ chỉ có tác dụng khi dùng chung tham số; số hạng entropy giữ chính sách khỏi tất định; biến thể cắt mất mát giá trị trình bày ở `L10-617`.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả sửa câu về $c_1$: "Khi chính sách và critic dùng chung tham số, $c_1$ cân hai mục tiêu trên cùng một gradient; với hai mạng tách, $c_1$ chỉ đổi thang mất mát của critic."; bỏ câu lặp về trung bình trên mini-batch để giữ độ dài.

#### `L10-610` Ví dụ: một mini-batch tính tay
- **Vị trí, loại:** mạch 6; ví dụ tính tay của cụm thuật toán PPO, trước giả mã `L10-613`.
- **Lý do tồn tại, nhu cầu:** tính mọi số hạng của $L$ trên một mini-batch có giá trị khởi tạo.
- **Liên kết:** trước: `L10-609`; sau: `L10-611` (chẩn đoán trên cùng mini-batch). **Mục tiêu:** 5. **Ghi chú:** Ví dụ 10.20 (`topic-19`); nguồn tr. 23.
- **Mặt trang:** một dòng dữ kiện (D1 thêm "Tính $\ell^{\mathrm{CLIP}}$, $L^V$, $L$.") "$p=0{,}75$, $\hat v=2{,}2$, $\hat v_{\mathrm{old}}=2$, $V^{\mathrm{targ}}=(3;\,3;\,0)$, $\epsilon=0{,}2$, $c_1=1$, $c_2=0{,}01$."; bảng khuôn mẫu PPO ba hàng (hành động $1,1,2$; $\widehat A=1;\,1;\,-2$; $\rho=1{,}125;\,1{,}125;\,0{,}75$; $\ell^{\mathrm{CLIP}}=1{,}125;\,1{,}125;\,-1{,}6$; gradient bằng $0$: không, không, có); dòng "$\mathcal L^{\mathrm{CLIP}}=0{,}2167$; $L^V=2{,}04$; $\mathcal H=0{,}5623$; $L=1{,}8177$."; kết luận (D1) "$\nabla_\theta\mathcal L^{\mathrm{CLIP}}=(0{,}1875;\,-0{,}1875)$, so với $(0{,}5625;\,-0{,}5625)$ của $\mathcal L^{\mathrm{CPI}}$."
- **Mật độ:** khoảng 20 âm tiết, 6 dòng (1 + 3 hàng bảng + 2).
- **Hình, phút:** — (bản viết bỏ thẻ nhỏ); 1,5.
- **Quyết định:** thêm: bộ cũ không có mini-batch tính tay; Ví dụ 10.20 của ghi chú là bước tính tay trước Thuật toán 10.49.
- **Ghi chú diễn giả:** mẫu thứ ba ở phía có lợi ngoài khoảng ($\rho<0{,}8$, lợi thế âm) nên chỉ hai mẫu đầu đóng góp gradient; $L^V=\tfrac13(0{,}64+0{,}64+4{,}84)$; $L=-0{,}2167+2{,}04-0{,}0056$.

#### `L10-611` Đại lượng chẩn đoán và approxKL
- **Vị trí, loại:** mạch 6; vấn đề, định nghĩa và số tính tay của cụm chẩn đoán.
- **Lý do tồn tại, nhu cầu:** mục tiêu cắt không chặn KL (`L10-606`), nên cần đo mức đổi chính sách trên mini-batch.
- **Liên kết:** trước: `L10-610`; sau: `L10-611b`. **Mục tiêu:** 5. **Ghi chú:** Định nghĩa 10.47, cuối Ví dụ 10.20 (`topic-19`); nguồn tr. 25, 27.
- **Mặt trang (D1):** "Nhu cầu: mục tiêu cắt không chặn KL; cần đo mức đổi chính sách trên mini-batch $\mathcal B$." "Định nghĩa 10.47." approxKL $=\tfrac1{\lvert\mathcal B\rvert}\sum_{i\in\mathcal B}[(\rho_i-1)-\log\rho_i]$; tỉ lệ cắt (clip fraction). "Dạng khác: approxKL bằng trung bình của $-\log\rho_i$, có thể có số hạng âm." "Phương sai được giải thích (explained variance): $1-\operatorname{Var}(y-\hat y)/\operatorname{Var}(y)$, $y=V^{\mathrm{targ}}$, $\hat y=\hat v_{\mathrm{old}}$." "Mini-batch tính tay: approxKL $0{,}01737$, tỉ lệ cắt $\tfrac13$."
- **Mật độ:** 56 âm tiết, 5 dòng.
- **Hình, phút:** —; 1,5.
- **Quyết định:** sửa (`L10-31` "Bốn chẩn đoán, ba phép giảm"); D1 tách Mệnh đề 10.48 sang `L10-611b` (E7), đưa dạng $-\log\rho$ và định nghĩa phương sai được giải thích lên mặt trang (E3; dùng ở `L10-619`, `L10-614`).
- **Ghi chú diễn giả:** hai chẩn đoán phụ còn lại; ý nghĩa các giá trị $1$, $0$, âm của phương sai được giải thích; số hạng của hai dạng trên mini-batch tính tay; tỉ lệ cắt khác tập gradient bằng $0$.

#### `L10-611b` Tính không chệch của approxKL
- **Vị trí, loại:** mạch 6; kết quả của cụm chẩn đoán (trang mới của D1).
- **Lý do tồn tại, nhu cầu:** điều kiện để approxKL không chệch, đủ cả hai điều kiện miền hỗ trợ (E9).
- **Liên kết:** trước: `L10-611`; sau: `L10-612`. **Mục tiêu:** 5. **Ghi chú:** Mệnh đề 10.48 (`topic-19`); nguồn tr. 35.
- **Mặt trang:** "Mệnh đề 10.48. $A\sim\pi_{\mathrm{old}}(\cdot\mid s)$; $\theta$ không phụ thuộc mẫu; $\pi_\theta(\cdot\mid s)$ và $\pi_{\mathrm{old}}(\cdot\mid s)$ cùng miền hỗ trợ. Khi đó" công thức hiển thị $\mathbb E[(\rho-1)-\log\rho]=D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$, $(\rho-1)-\log\rho\ge0$; "Chứng minh. Cùng miền hỗ trợ cho $\mathbb E[\rho]=1$; $x-1-\log x\ge0$ với $x>0$."; "Lưu ý: từ epoch thứ hai, $\theta$ đã tối ưu trên chính các mẫu đó."
- **Mật độ:** 36 âm tiết, 4 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** tách (D1, từ `L10-611`).
- **Ghi chú diễn giả:** hai chiều của điều kiện miền hỗ trợ và vai trò của mỗi chiều; phản ví dụ $\pi_{\mathrm{old}}=(1;\,0)$, $\pi_\theta=(0{,}9;\,0{,}1)$ ($0{,}00536\ne0{,}10536$); phản ví dụ $\theta$ chọn sau khi thấy mẫu ($0$ so với $0{,}0959$).

#### `L10-612` Đường dữ liệu của PPO
- **Vị trí, loại:** mạch 6; trực giác (khung thuật toán) của cụm thuật toán PPO.
- **Lý do tồn tại, nhu cầu:** phân biệt đại lượng giữ cố định với đại lượng tính lại trước khi đọc giả mã.
- **Liên kết:** trước: `L10-611`; sau: `L10-613`. **Mục tiêu:** 5. **Ghi chú:** §6.3 đoạn sau Thuật toán 10.49 (`topic-19`); nguồn tr. 24.
- **Mặt trang:** hình đường dữ liệu; bảng hai cột một hàng như bảng của ghi chú: "Giữ cố định trong $K$ epoch": $\log\pi_{\mathrm{old}}(A_t\mid S_t)$, $\widehat A^{\mathrm{raw}}_t$, $V^{\mathrm{targ}}_t$, $\hat v_{\mathrm{old}}(S_t)$ | "Tính lại ở mỗi mini-batch": $\log\pi_\theta(A_t\mid S_t)$, $\rho_t(\theta)$, $\hat v(S_t,w)$, $\mathcal H$. Hai dòng: "Từ mini-batch thứ hai, $\theta\ne\theta_{\mathrm{old}}$: dữ liệu đã khác chính sách." (9); "$\rho_t$ chỉ hiệu chỉnh phân phối hành động; phân bố trạng thái vẫn của $\pi_{\mathrm{old}}$." (14).
- **Mật độ:** khoảng 30 âm tiết, 3 dòng (1 hàng bảng + 2), 1 hình.
- **Hình, phút:** `img/lec-10/ppo-data-pipeline.svg`; 1.
- **Quyết định:** gộp (`L10-28` "Kích thước từ rollout đến batch", `L10-29` "Đường dữ liệu PPO", `L10-30` "Cấu trúc dữ liệu của một batch PPO"): ba trang thành một; kích thước mảng $h\times N$ chuyển vào ghi chú diễn giả.
- **Ghi chú diễn giả:** mảng cỡ $h\times N$ phẳng thành $hN$ mẫu; giá trị quan sát cuối khi cắt ngắn lấy trước khi môi trường tự đặt lại; hành động nhiều chiều cộng log-xác suất các thành phần trước khi lập tỉ số; đọc hình.
- **Sửa 2026-11-13 (bảng phát hiện):** hình dùng `.figure.short` (260 px) thay `max-height:270px`.

#### `L10-613` Thuật toán PPO kiểu actor–critic
- **Vị trí, loại:** mạch 6; thuật toán; nơi hai hàng của bài toán gặp nhau.
- **Lý do tồn tại, nhu cầu:** quy trình đầy đủ khớp `L10-610`–`L10-612`.
- **Liên kết:** trước: `L10-612`; sau: `L10-614`. **Mục tiêu:** 5. **Ghi chú:** Thuật toán 10.49 (`topic-19`); Schulman và cộng sự (2017), Thuật toán 1; nguồn tr. 24–25.
- **Mặt trang:** "Thuật toán." sáu dòng: (1) "Đầu vào: $\pi_\theta$, $\hat v$; $N$, $h$, $K$, $M$; $\gamma$, $\lambda$, $\epsilon$, $c_1$, $c_2$; bước học Adam $\alpha$." (2) "Mỗi vòng: $\theta_{\mathrm{old}}\leftarrow\theta$, thu $h$ bước trên $N$ môi trường, lưu $R$, $Z$, $U$, $\log\pi_{\mathrm{old}}$, $\hat v_{\mathrm{old}}$, $V'$ khi cắt ngắn." (3) "Tính $\widehat A^{\mathrm{raw}}_t$, $V^{\mathrm{targ}}_t$ bằng Thuật toán 10.16." (4) "Lặp $K$ epoch: xáo bộ đệm, chia mini-batch cỡ $M$; với mỗi mini-batch:" (5) "(tùy chọn) chuẩn hóa lợi thế; tính lại $\log\pi_\theta$, $\rho_i$, $\hat v$, $\mathcal H$; một bước Adam trên $L(\theta,w)$;" (6) "ghi approxKL, tỉ lệ cắt; (tùy chọn) dừng sớm (early stopping) khi approxKL vượt ngưỡng."
- **Mật độ:** khoảng 60 âm tiết, 6 dòng, mỗi dòng không quá 20 âm tiết. Không còn là ngoại lệ (bản trước 10 dòng).
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm: bộ cũ không có giả mã PPO đầy đủ; Thuật toán 10.49 của ghi chú. Đợt sửa sau cổng: rút từ 10 xuống 6 dòng; chi phí $K\lceil hN/M\rceil$ chuyển vào ghi chú diễn giả và bảng `L10-616`.
- **Ghi chú diễn giả:** bước tính tay là `L10-610`; lưu cả giá trị quan sát cuối ở mỗi bước cắt ngắn; mỗi lần thu $hN$ bước cho $K\lceil hN/M\rceil$ bước gradient thay vì một, đó là cách PPO giải giới hạn thứ hai của `L10-108`; điều kiện dừng là ngân sách, không phải tiêu chuẩn hội tụ.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả thêm giả thiết của Thuật toán 10.49 ($\pi_\theta>0$; môi trường trả $Z$, $U$, quan sát cuối); bỏ câu chuẩn hóa lợi thế (đã ở `L10-609`).

#### `L10-614` Ví dụ: chẩn đoán trên đoạn phẳng
- **Vị trí, loại:** mạch 6; ứng dụng và đánh giá của cụm thuật toán PPO (đọc chẩn đoán).
- **Lý do tồn tại, nhu cầu:** đọc các chẩn đoán khi mọi mẫu đã trên đoạn phẳng.
- **Liên kết:** trước: `L10-613`; sau: `L10-615`. **Mục tiêu:** 5. **Ghi chú:** Ví dụ 10.21 (`topic-20`); nguồn tr. 27.
- **Mặt trang:** dòng "Sau vài mini-batch, $p=0{,}85$: mọi mẫu trên đoạn phẳng, $\mathcal L^{\mathrm{CLIP}}=0{,}2\overline6$." (11); bảng khuôn mẫu PPO ba hàng ($\rho=1{,}275;\,1{,}275;\,0{,}45$, gradient bằng $0$ ở cả ba); dòng "Tỉ lệ cắt $\tfrac33$; approxKL $0{,}1042$, gấp sáu lần $0{,}01737$." (8); "Diễn giải: phương sai được giải thích bằng $0$ với critic đúng; giá trị thấp không có nghĩa critic sai." (17).
- **Mật độ:** khoảng 36 âm tiết, 6 dòng (1 + 3 hàng bảng + 2).
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không đọc chẩn đoán trên số; Ví dụ 10.21 của ghi chú. Đợt sửa sau cổng: phép tính $-\log1{,}275=-0{,}2430$ chuyển vào ghi chú diễn giả.
- **Ghi chú diễn giả:** một mẫu: $-\log1{,}275=-0{,}2430<0$ trong khi $(\rho-1)-\log\rho=0{,}0321$; KL tăng dù mục tiêu phẳng từ $p=0{,}8$ (Adam, mini-batch khác); một trạng thái nên mọi biến thiên của mục tiêu critic đến từ hành động; tỉ lệ cắt $\tfrac33$ ở đây trùng tập gradient bằng $0$, nói chung không trùng.
- **Sửa 2026-11-13 (bảng phát hiện):** "Diễn giải:" thành "gradient của mục tiêu cắt bằng $0$ mà KL vẫn tăng, nên mục tiêu cắt không chặn KL." (không lặp số của dòng trên).

#### `L10-615` Siêu tham số của bài báo PPO
- **Vị trí, loại:** mạch 6; bảng (đọc cấu hình có nguồn, so sánh hai bộ thí nghiệm của bài báo).
- **Lý do tồn tại, nhu cầu:** giá trị điển hình có nguồn, thay bảng không nguồn của nguồn tr. 26.
- **Liên kết:** trước: `L10-614`; sau: `L10-616`. **Mục tiêu:** 5. **Ghi chú:** §6.4, bảng siêu tham số (`topic-20`); Schulman và cộng sự (2017), Bảng 3, 5; nguồn tr. 26.
- **Mặt trang:** bảng `Siêu tham số | MuJoCo (Bảng 3) | Atari (Bảng 5)`, sáu hàng: $h$; $N$ ($2048$; không ghi | $128$; $8$); $\alpha$ ($3\cdot10^{-4}$ | $2{,}5\cdot10^{-4}$, giảm tuyến tính); $K$; $M$ ($10$; $64$ | $3$; $32\cdot8$); $\gamma$; $\lambda$ ($0{,}99$; $0{,}95$ ở cả hai); $\epsilon$ (Bảng 1 thử $0{,}1$; $0{,}2$; $0{,}3$ | $0{,}1$, giảm tuyến tính); $c_1$; $c_2$ (không dùng | $1$; $0{,}01$).
- **Mật độ:** khoảng 30 âm tiết (ô số không tính), 6 dòng (6 hàng bảng).
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-32` "Siêu tham số tương tác với nhau"): bảng không nguồn thay bằng hai bảng của bài báo. Đợt sửa sau cổng: gộp hàng thành sáu hàng.
- **Ghi chú diễn giả:** cắt chuẩn gradient $0{,}5$ và hằng ổn định số $10^{-5}$ của Adam theo Huang và cộng sự (2022); bảng là cấu hình của một bài báo, không phải giá trị tối ưu chung.

#### `L10-616` So sánh TRPO và PPO
- **Vị trí, loại:** mạch 6; bảng so sánh hai phương pháp.
- **Lý do tồn tại, nhu cầu:** đặt hai cách giới hạn bước cạnh nhau theo điều được bảo đảm.
- **Liên kết:** trước: `L10-615`; sau: `L10-617`. **Mục tiêu:** 4, 5. **Ghi chú:** §6.4, bảng so sánh (`topic-20`); nguồn tr. 28.
- **Mặt trang:** bảng `Tiêu chí | TRPO | PPO`: cách giữ gần (ràng buộc KL trung bình mẫu $\le\kappa$ | cắt tỉ số, hoặc phạt KL); chi phí mỗi vòng ($k_{\max}$ tích Fisher–vector, tìm kiếm lùi | $K\lceil hN/M\rceil$ bước gradient); điều được bảo đảm trên bộ đệm (KL trung bình mẫu $\le\kappa$, hàm thay thế mẫu tăng | không có cận KL); giả thiết lý thuyết còn thiếu (lợi thế, $\nu^{\mathrm{old}}$, nghiệm chính xác | như TRPO, thêm cắt thay ràng buộc).
- **Mật độ:** khoảng 55 âm tiết, bảng 4 hàng (trần 80).
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-36` "TRPO và PPO kiểm soát bước theo hai cách"): tiêu đề danh từ; tiêu chí theo bảo đảm.
- **Ghi chú diễn giả:** không kết luận phương pháp nào tốt hơn ngoài thí nghiệm của bài báo (Schulman và cộng sự, 2017, §6); bảng viết lại bảng tr. 28 của nguồn.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả cắt câu phủ định "Không kết luận phương pháp nào tốt hơn …" (sau kiểm lại: không thay bằng câu so sánh không có trong ghi chú).

#### `L10-617` Ví dụ: cắt mất mát giá trị
- **Vị trí, loại:** mạch 6; vấn đề và ví dụ dẫn nhập của cụm chi tiết cài đặt (D1: trang ví dụ đứng trước bảng).
- **Lý do tồn tại, nhu cầu:** một tối ưu mức mã đổi hành vi của critic trên số; nêu công thức phép cắt và $\epsilon$ để sinh viên tự kiểm được (E9, phát hiện của vai sinh viên và chuyên gia).
- **Liên kết:** trước: `L10-616`; sau: `L10-617b`. **Mục tiêu:** 5. **Ghi chú:** §6.5, Định nghĩa 10.46 (biến thể), Ví dụ 10.22 (`topic-21`); nguồn tr. 30.
- **Mặt trang:** "Nhu cầu: tách tác dụng của phép cắt khỏi tối ưu mức mã (code-level optimizations)."; "Cắt mất mát giá trị (value function clipping) thay $(\hat v-V^{\mathrm{targ}})^2$ trong $L^V$ bằng" công thức hiển thị $\max[(\hat v-V^{\mathrm{targ}})^2,(\operatorname{clip}(\hat v,\hat v_{\mathrm{old}}\pm\epsilon)-V^{\mathrm{targ}})^2]$; "$\epsilon=0{,}2$, $\hat v_{\mathrm{old}}=2$, $\hat v=2{,}5$, giá trị cắt $2{,}2$. Tính gradient theo $\hat v$."; hai trường hợp $\max(0{,}25;\,0{,}64)$, gradient $0$; $\max(6{,}25;\,4{,}84)$, gradient $5$; "Diễn giải: ở mục tiêu $3$, critic đã ra ngoài khoảng cắt theo hướng mục tiêu nên bị dừng."
- **Mật độ:** 52 âm tiết, 6 dòng, 1 công thức hiển thị.
- **Hình, phút:** —; 1.
- **Quyết định:** gộp (`L10-33`, `L10-34`, `L10-35` của bộ cũ) rồi D1 tách (E6: 66 âm tiết, hai luận điểm): ví dụ ở đây, bảng và kết luận ở `L10-617b`.
- **Ghi chú diễn giả:** phép cắt dùng chính $\epsilon$ của tỉ số; vì sao nhánh cắt cho gradient $0$; critic cực tiểu hóa $\max$ của hai bình phương; nhận định của Huang và cộng sự (2022) về Engstrom và cộng sự, Andrychowicz và cộng sự (2021).
- **Sửa 2026-11-13 (bảng phát hiện):** "Nhu cầu: đo tác động của một tối ưu mức mã (code-level optimization) lên critic." khớp nội dung trang và câu dẫn trước Ví dụ 10.22 của ghi chú; ghi chú diễn giả bỏ câu dẫn Huang/Engstrom/Andrychowicz (không có trong ghi chú và danh mục tài liệu); 122 token (trước 154).

#### `L10-617b` Chi tiết cài đặt
- **Vị trí, loại:** mạch 6; bảng rút gọn của Nhận xét 10.50 và kết luận trả lời "Nhu cầu:" của `L10-617`.
- **Lý do tồn tại, nhu cầu:** các tối ưu mức mã theo thành phần chúng thay đổi; mức cải thiện của PPO đến từ đâu (E7, phát hiện của vai sư phạm).
- **Liên kết:** trước: `L10-617`; sau: `L10-618`. **Mục tiêu:** 5. **Ghi chú:** Nhận xét 10.50 (`topic-21`); Engstrom và cộng sự (2020), §3–6; Huang và cộng sự (2022); nguồn tr. 29–34, 36.
- **Mặt trang:** bảng `Thành phần bị thay đổi | Chi tiết`, ba hàng (dữ liệu; mục tiêu; bộ tối ưu, mạng); "Kết luận: Engstrom và cộng sự thấy tối ưu mức mã tạo phần lớn ưu thế của PPO trước TRPO."
- **Mật độ:** 60 âm tiết (54 không tính hàng tiêu đề), 4 dòng.
- **Hình, phút:** —; 0,5.
- **Quyết định:** tách (D1, từ `L10-617`); thêm dòng kết luận.
- **Ghi chú diễn giả:** môi trường vector hóa (vectorized environments); ba kết luận định tính của Engstrom và cộng sự (2020, §5–6) trong thí nghiệm loại bỏ của họ; chuẩn hóa và cắt phần thưởng đổi hàm mục tiêu; báo cáo PPO cần ghi đủ chi tiết. Ghi chú dưới 150 âm tiết.

#### `L10-618` Hội tụ về điểm dừng của PPO-Clip
- **Vị trí, loại:** mạch 6; nhận xét đọc thêm (`topic-22`), phát biểu không chứng minh.
- **Lý do tồn tại, nhu cầu:** nêu đúng phạm vi của tuyên bố lý thuyết hiện có về PPO-Clip.
- **Liên kết:** trước: `L10-617`; sau: `L10-619`. **Mục tiêu:** 5 (điều PPO không bảo đảm). **Ghi chú:** §6.6, Nhận xét 10.51 (`topic-22`); Jin, Li và Wang (2024); nguồn tr. 37, 39–42.
- **Mặt trang:** năm dòng: "Nhận xét. Mô hình: MDP hữu hạn, hai thang thời gian, không Adam, không xáo mini-batch." (15); "Giả thiết: gradient của $\pi_\theta$ Lipschitz, phần thưởng bị chặn, điều kiện bước học." (13); "Kết luận: độ chệch $\varphi_n$ của lợi thế bằng $0$ từ một vòng: $\nabla V(\theta_n)\to0$ hầu chắc chắn (almost surely)." (16); "$\varphi_n>0$: chỉ có cận cho $\liminf_n\lVert\nabla V(\theta_{n,1})\rVert^2$." (4); "Lưu ý: không khẳng định tham số hội tụ hay chính sách tối ưu." (11).
- **Mật độ:** khoảng 59 âm tiết, 5 dòng, mỗi dòng không quá 16 âm tiết (dòng kết luận cũ khoảng 30 âm tiết tách thành hai dòng).
- **Hình, phút:** —; 1.
- **Quyết định:** gộp (`L10-37` "Mô hình lý thuyết tách vòng ngoài và vòng trong", `L10-37B` "Kết quả điểm dừng có phạm vi hẹp"): tiêu đề gọi tên kết quả.
- **Ghi chú diễn giả:** Định lý 3.1, 3.2 của bài báo; cận $C\sqrt{\lvert\mathcal A\rvert}\limsup\varphi_n$; GAE với critic học được cho $\varphi_n>0$; bài báo dùng $\min\{\rho,\operatorname{clip}(\rho)\}\tilde A$ và coi gradient bằng $0$ ở hai phía, khác dạng theo dấu của `L10-604`; điểm dừng (stationary point); bốn khó khăn phân tích ở nguồn tr. 37.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả bỏ hai tên tiếng Anh đã có trên mặt trang; 145 token (trước 154).

#### `L10-619` Bài tập: kiểm một mini-batch PPO
- **Vị trí, loại:** mạch 6; bước kiểm tra chung của cụm PPO-Clip và cụm chẩn đoán (đề); lời giải ở trang sau.
- **Lý do tồn tại, nhu cầu:** kiểm mục tiêu cắt, tỉ lệ cắt, approxKL và dừng sớm trên một mini-batch.
- **Liên kết:** trước: `L10-618`; sau: `L10-620`. **Mục tiêu:** 5. **Ghi chú:** Bài tập 10.12 (a)–(c) (`topic-19`).
- **Mặt trang:** dòng "Câu hỏi: $\epsilon=0{,}2$, ngưỡng dừng sớm $0{,}015$; bốn mẫu như bảng." (9); bảng khuôn mẫu PPO bốn hàng với cột $\widehat A=(2;\,-1;\,-1;\,0{,}5)$ và $\log\rho=(0{,}1;\,-0{,}3;\,0{,}25;\,-0{,}05)$, các cột $\rho$, $\ell^{\mathrm{CLIP}}$, gradient bằng $0$ để trống; dòng "Tính (a) $\rho$, $\ell^{\mathrm{CLIP}}$, $\mathcal L^{\mathrm{CLIP}}$; (b) tỉ lệ cắt, mẫu có gradient bằng $0$; (c) hai dạng approxKL, có dừng sớm không." (19).
- **Mật độ:** khoảng 30 âm tiết, 6 dòng (1 + 4 hàng bảng + 1).
- **Hình, phút:** —; 1.
- **Quyết định:** sửa và tách (`X03` "Bài tập: kiểm toán một batch PPO"): "kiểm toán" thành "kiểm"; đề và lời giải hai trang. Câu (d) chuyển lên `L10-608`.
- **Ghi chú diễn giả:** "Gợi ý:" $\rho=e^{\log\rho}$; xét dấu của lợi thế trước khi cắt; dạng $-\log\rho$ có thể bằng $0$ dù chính sách đã đổi.
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả bỏ câu trỏ về câu (d) của Bài tập 10.12.

#### `L10-620` Bài tập: kiểm một mini-batch PPO
- **Vị trí, loại:** mạch 6; lời giải trên mặt trang (trang kế tiếp cùng tiêu đề).
- **Lý do tồn tại, nhu cầu:** lời giải mẫu của cụm lớn PPO.
- **Liên kết:** trước: `L10-619`; sau: `L10-700`. **Mục tiêu:** 5. **Ghi chú:** Bài tập 10.12, lời giải (a)–(c) (`topic-19`).
- **Mặt trang:** "Lời giải:" bảng của `L10-619` điền đủ bốn hàng ($\rho=1{,}1052;\,0{,}7408;\,1{,}2840;\,0{,}9512$; $\ell^{\mathrm{CLIP}}=2{,}2103;\,-0{,}8;\,-1{,}2840;\,0{,}4756$; gradient bằng $0$ chỉ ở mẫu 2); dòng "$\mathcal L^{\mathrm{CLIP}}=0{,}1505$; tỉ lệ cắt $\tfrac24$." (3); dòng "Trung bình $-\log\rho=0$; approxKL $0{,}0203>0{,}015$: dừng sớm." (6).
- **Mật độ:** khoảng 15 âm tiết, 6 dòng (4 hàng bảng + 2).
- **Hình, phút:** —; 1. **Quyết định:** sửa (`X03`, phần lời giải).
- **Ghi chú diễn giả:** mẫu 3 ra ngoài khoảng ở phía bất lợi nên vẫn có gradient; tỉ lệ cắt đếm cả mẫu 2 và mẫu 3; mọi số hạng $(\rho-1)-\log\rho$ không âm (Mệnh đề 10.48).

**Hành trình khái niệm, mạch 6.**

| cụm (dạng) | vấn đề | trực giác | ví dụ | hình thức/thuật toán | ứng dụng | kiểm tra | truyền từ ví dụ sang công thức | gộp hoặc `không áp dụng` | phút |
|---|---|---|---|---|---|---|---|---|---:|
| PPO-Clip (khái niệm, kết quả) | `L10-600`, `L10-601` | `L10-601` | `L10-602` | `L10-603`, `L10-604`, `L10-606` | `L10-605` | `L10-619`, `L10-620` (a), (b) | khúc gấp $p=0{,}7\overline3$ và $0{,}8$ → $\min$, $\max$ theo dấu → miền gradient bằng $0$ | vấn đề và trực giác cùng trang; bài tập `L10-619`–`L10-620` (2 phút) kiểm cả ba cụm | 8 |
| PPO-Penalty (khái niệm) | `L10-607` "Nhu cầu:" | `L10-607` "Trực quan." (KL thành chi phí) | `L10-607` | `L10-608` | `L10-608` (vai của $\kappa_{\mathrm{targ}}$, "Lưu ý:") | `L10-608` ("Câu hỏi:", Bài tập 10.12(d)) | $0{,}01737>0{,}015$ → quy tắc $\beta\leftarrow2\beta$ | hai trang sau khi tách; ví dụ tính tay trước quy tắc | 2 |
| Mất mát tổng, chẩn đoán, thuật toán PPO (khái niệm, thuật toán) | `L10-609`, `L10-611` "Nhu cầu:" | `L10-609` "Trực quan." (D1), `L10-612` (hai loại đại lượng) | `L10-610` | `L10-609`, `L10-611`, `L10-611b`, `L10-613` | `L10-614` | `L10-619`, `L10-620` (c) | bảng mẫu của `L10-610` → bước 3 của Thuật toán 10.49 | tay trước thuật toán; D1 tách Mệnh đề 10.48 sang `L10-611b`; `L10-612` đứng trước `L10-613` (lệch thứ tự so với ghi chú, xem `outline.md`) | 8,5 |
| Siêu tham số, so sánh (bảng) | `L10-614` | `không áp dụng` (đọc bảng có nguồn) | `L10-614` | `L10-615`, `L10-616` | `không áp dụng` | `L10-708` câu 3–4 | — | chu trình rút gọn: khái niệm phụ, đọc bảng | 2 |
| Chi tiết cài đặt (nhận xét) | `L10-617` "Nhu cầu:" | `không áp dụng` | `L10-617` | `L10-617b` | `không áp dụng` | Bài tập 10.3(d) (về nhà) | công thức cắt mất mát giá trị → hàng "mục tiêu" của bảng | hai trang sau D1: ví dụ dẫn nhập trước bảng và kết luận | 1,5 |
| Hội tụ PPO-Clip (nhận xét, đọc thêm) | `L10-618` | `không áp dụng` | `không áp dụng` | `L10-618` | `không áp dụng` | Bài tập 10.3(c) (về nhà) | — | đọc thêm, phát biểu không chứng minh | 1 |

Phút mạch 6: $0{,}5$ + PPO-Clip ($1+2+1+1{,}5+1+1{,}5$) + PPO-Penalty $2$ + thuật toán ($1+1{,}5+2{,}5+1+1{,}5+1$) + bảng ($1+1$) + cài đặt $1{,}5$ + hội tụ $1$ + bài tập ($1+1$) $=25{,}5$; cột phút của cụm PPO-Clip ($8$) không tính bài tập, cụm thuật toán ($8{,}5$) tính `L10-614`. Câu nối: "hàm thay thế mẫu tuyến tính theo $\rho_t$" (`L10-601` → `L10-602`); "từ $p=0{,}8$ gradient bằng $0$" (`L10-602` → `L10-603`); "mục tiêu cắt không chặn KL" (`L10-606` → `L10-607`); "huấn luyện actor và critic bằng một hàm mất mát" (`L10-608` → `L10-609`); "tỉ lệ cắt $\tfrac13$" (`L10-610` → `L10-611`); "từ mini-batch thứ hai dữ liệu đã khác chính sách" (`L10-612` → `L10-613`); "mức cải thiện đến từ đâu" (`L10-616` → `L10-617`).

### Mạch 7. Tổng kết và chuyển tiếp (9 phút)

#### `L10-700` 7. Tổng kết và chuyển tiếp (trang tiêu đề mạch), điểm vào mạch 7
- **Vị trí, loại:** điểm vào mạch 7; `id="mach-7"`, `data-note-topic-id="lec-10-topic-23"`; ngoài hành trình khái niệm (mạch kết luận không mở khái niệm mới).
- **Lý do tồn tại, nhu cầu:** đặt mỗi kết quả cạnh giả thiết của nó và trả lời bài toán có điều kiện.
- **Liên kết:** trước: `L10-620`; sau: `L10-701`. Kế thừa mọi kết quả của mạch 2–6; giao giới hạn dữ liệu theo chính sách cho Bài 11.
- **Mục tiêu:** 1–5.
- **Mặt trang:** "7." + tên mạch; dòng dẫn "Muốn dùng đúng các phương pháp của bài, phải giữ giả thiết của từng kết quả." (16); từ khóa "Kết quả và giả thiết · Bốn phương pháp · Vấn đề trung tâm · Bài 11" (14).
- **Hình, phút:** —; 0,5. **Quyết định:** thêm: trang tiêu đề mạch theo `AGENTS.md` §"Trang tiêu đề mạch"; bộ cũ không có.
- **Ghi chú diễn giả (40–100):** hai nửa của bài toán và các kết quả đã có; mỗi bảo đảm có giả thiết riêng; giới hạn còn lại là dữ liệu theo chính sách.

#### `L10-701` Kết quả và giả thiết của bài
- **Vị trí, loại:** mạch 7; bảng tổng kết, nửa giảm phương sai.
- **Lý do tồn tại, nhu cầu:** bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` theo quy định mạch kết luận.
- **Liên kết:** trước: `L10-700`; sau: `L10-702`. **Mục tiêu:** 1, 2. **Ghi chú:** §7.1, sáu hàng đầu (`topic-23`).
- **Mặt trang:** sáu hàng chép từ §7.1: đường cơ sở không làm chệch (Mệnh đề 10.2); đường cơ sở tối ưu (Mệnh đề 10.3); gradient dạng lợi thế (Mệnh đề 10.5, dạng quỹ đạo $\nabla J=\mathbb E[\sum_t\gamma^tA_\pi\psi_t]$); sai số TD và lợi thế (Mệnh đề 10.8); dạng tổng của GAE (Mệnh đề 10.14); GAE và gradient (Mệnh đề 10.15).
- **Mật độ:** khoảng 55 âm tiết (trần 80), bảng 6 hàng.
- **Hình, phút:** —; 1.
- **Quyết định:** sửa (`L10-38` "Bốn hợp đồng cần giữ"): bỏ "hợp đồng", thẻ thành bảng ba cột theo quy định.
- **Ghi chú diễn giả:** sáu hàng là nửa giảm phương sai; giả thiết hay bị bỏ: đường cơ sở không phụ thuộc hành động; γ-just không có nghĩa không chệch cho lợi thế; cờ $Z$ chỉ ghi kết thúc.

#### `L10-702` Kết quả và giả thiết của bài
- **Vị trí, loại:** mạch 7; bảng tổng kết (tiếp), mạch 4.
- **Lý do tồn tại, nhu cầu:** năm hàng của §7.1 thuộc mạch 4.
- **Liên kết:** trước: `L10-701`; sau: `L10-702b`. **Mục tiêu:** 3. **Ghi chú:** §7.1 (`topic-23`).
- **Mặt trang:** năm hàng: hiệu hiệu năng; khớp bậc một; chặn cải thiện; cải thiện đơn điệu; bước miền tin cậy.
- **Mật độ:** 46 âm tiết (trần 80), bảng 5 hàng.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm; bản viết tách bảng chín hàng thành `L10-702` và `L10-702b` (đáy quá 680 px).
- **Ghi chú diễn giả (D1):** mở bằng các kết quả (Bổ đề 10.19, Mệnh đề 10.22, Định lý 10.26, Hệ quả 10.29, 10.31); mọi bảo đảm cần lợi thế, $\nu^\pi$ và tối ưu chính xác; dạng KL của chặn cải thiện; điều kiện hỗ trợ.
- **Sửa 2026-11-13 (bảng phát hiện):** "${\pi_{\mathrm{old}}>0}$" bọc nhóm KaTeX để không ngắt "0" xuống dòng riêng (ảnh chụp 1600×900 đã kiểm).

#### `L10-702b` Kết quả và giả thiết của bài
- **Vị trí, loại:** mạch 7; bảng tổng kết (tiếp), mạch 5–6 (trang tách ở bản viết, ghi vào storyboard ở D1).
- **Lý do tồn tại, nhu cầu:** bốn hàng của §7.1 thuộc mạch 5–6.
- **Liên kết:** trước: `L10-702`; sau: `L10-703`. **Mục tiêu:** 4–5. **Ghi chú:** §7.1 (`topic-23`).
- **Mặt trang (D1):** bốn hàng: KL bậc hai; gradient tự nhiên; mục tiêu cắt ("gradient $0$ ngoài khoảng ở phía có lợi; $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, trùng quanh $\theta_{\mathrm{old}}$"); approxKL ("$\theta$ không phụ thuộc mẫu; cùng miền hỗ trợ").
- **Mật độ:** 42 âm tiết (trần 80), bảng 4 hàng.
- **Hình, phút:** —; 0,5.
- **Quyết định:** tách (bản viết); D1 thêm tập gradient bằng $0$ (Mệnh đề 10.40) và điều kiện miền hỗ trợ của approxKL.
- **Ghi chú diễn giả:** Mệnh đề 10.33, 10.34 cho bước TRPO; hàng mục tiêu cắt gộp Mệnh đề 10.40, 10.41; hàng approxKL là Mệnh đề 10.48 với hai chiều của điều kiện hỗ trợ.

#### `L10-703` So sánh bốn phương pháp
- **Vị trí, loại:** mạch 7; bảng phương pháp.
- **Lý do tồn tại, nhu cầu:** bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng` cho bài nhiều thuật toán.
- **Liên kết:** trước: `L10-702`; sau: `L10-704`. **Mục tiêu:** 1, 4, 5. **Ghi chú:** §7.2 bảng thứ nhất (`topic-23`); nguồn tr. 28.
- **Mặt trang:** bốn hàng: REINFORCE có đường cơ sở (Thuật toán 10.6); actor–critic một bước (Thuật toán 10.9); TRPO (Thuật toán 10.37); PPO (Thuật toán 10.49), mỗi hàng quy tắc, dữ liệu, điều kiện dừng như §7.2. Dòng: không điều kiện dừng nào là tiêu chuẩn hội tụ; cả bốn là ngân sách.
- **Mật độ:** khoảng 60 âm tiết (trần 80), bảng 4 hàng và 1 dòng.
- **Hình, phút:** —; 1. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo §7.2 bảng thứ nhất của ghi chú.
- **Ghi chú diễn giả:** dữ liệu dùng một lần (hai thuật toán đầu, TRPO) và $K$ epoch (PPO); mọi phương pháp cần dữ liệu của chính sách hiện tại.

#### `L10-704` Các kết luận có bảo đảm
- **Vị trí, loại:** mạch 7; bảng `Phương pháp | Giả thiết không được bỏ | Kết luận`.
- **Lý do tồn tại, nhu cầu:** tách ba kết luận có bảo đảm khỏi các thuật toán thực hành.
- **Liên kết:** trước: `L10-703`; sau: `L10-705`. **Mục tiêu:** 3, 5. **Ghi chú:** §7.2 bảng thứ hai (`topic-23`); nguồn tr. 40–42.
- **Mặt trang:** ba hàng: lặp chính sách với $\mathcal M_k$ (Hệ quả 10.29: đánh giá và cực đại hóa chính xác; $J$ không giảm); bài toán miền tin cậy (Hệ quả 10.31: nghiệm chính xác; mức giảm $\le\sqrt{2\kappa}\gamma\chi/(1-\gamma)^2$); PPO-Clip trong mô hình của Jin, Li và Wang (MDP hữu hạn, hai thang, không Adam, không mini-batch; cận cho $\liminf\lVert\nabla V\rVert^2$).
- **Mật độ:** khoảng 50 âm tiết, bảng 3 hàng.
- **Hình, phút:** —; 0,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo §7.2 bảng thứ hai của ghi chú.
- **Ghi chú diễn giả:** không hàng nào áp dụng cho TRPO hay PPO như cài đặt thực tế.
- **Sửa 2026-11-13 (bảng phát hiện):** giữ `<colgroup>` với `col style="width:17%"` và `"width:39%"` (D10): nhu cầu một trang, vì bảng ba cột có cột "Kết luận" chứa công thức dài của Jin, Li và Wang; không lớp nào trong `lecture-course.css` đặt độ rộng cột bảng. Đây là `style=""` duy nhất còn lại của deck.

#### `L10-705` Bài tập: GAE ở bước cắt ngắn trên CartPole
- **Vị trí, loại:** mạch 7; bài tập tổng hợp (đề), dùng nhiều kết quả trên một bài toán Học tăng cường cụ thể; ứng dụng của cụm γ-just và GAE trên đoạn thu.
- **Lý do tồn tại, nhu cầu:** áp dụng truy hồi GAE, cờ $Z$, $U$ và kiểm giả thiết γ-just ở bước cắt ngắn; tình huống cờ sai.
- **Liên kết:** trước: `L10-704`; sau: `L10-706`. **Mục tiêu:** 2. **Ghi chú:** Tình huống 10.1, 10.2 (`topic-23`); nguồn tr. 24.
- **Mặt trang:** "Câu hỏi:" CartPole giới hạn $500$ bước, phần thưởng $1$ mỗi bước, $\gamma=0{,}99$, $\lambda=0{,}95$, $\hat v_{\mathrm{old}}\equiv95$ kể cả quan sát cuối; lượt chạm giới hạn: $U_{500}=1$, $Z_{500}=0$. (a) tính $\widehat A_{499}$, $\widehat A_{498}$, $V^{\mathrm{targ}}_{498}$; (b) tính lại khi bản cài đặt ghi $Z_{500}=1$; (c) xác định Mệnh đề 10.15 có áp dụng không và giả thiết nào bị vi phạm ở (b).
- **Mật độ:** khoảng 55 âm tiết, 5 dòng.
- **Hình, phút:** —; 1,5. **Quyết định:** thêm: bộ cũ không có trang tương ứng; nội dung theo Tình huống 10.1, 10.2 của ghi chú.
- **Ghi chú diễn giả:** "Gợi ý:" bước 2–3 của Thuật toán 10.16; giá trị đúng của chuỗi phần thưởng $1$ không kết thúc là $100$; dùng Mệnh đề 10.8, 10.14(c), 10.15, Thuật toán 10.16, 10.49.

#### `L10-706` Bài tập: GAE ở bước cắt ngắn trên CartPole
- **Vị trí, loại:** mạch 7; lời giải trên mặt trang (trang kế tiếp cùng tiêu đề); kiểm tra của cụm γ-just và GAE trên đoạn thu.
- **Lý do tồn tại, nhu cầu:** lời giải mẫu của bài tổng hợp.
- **Liên kết:** trước: `L10-705`; sau: `L10-707`. **Mục tiêu:** 2. **Ghi chú:** Tình huống 10.1, 10.2 (`topic-23`).
- **Mặt trang:** "Lời giải:" năm dòng: (a) "$\delta_{499}=1+0{,}99\cdot95-95=0{,}05=\widehat A_{499}$ vì $U_{500}=1$."; (a, tiếp) "$\widehat A_{498}=0{,}05+0{,}9405\cdot0{,}05=0{,}0970$; $V^{\mathrm{targ}}_{498}=95{,}097$."; (b) "$Z_{500}=1$: $\delta_{499}=1-95=-94$, $\widehat A_{498}=-88{,}36$."; (c) "Mệnh đề 10.15 không áp dụng: $\lambda<1$, critic khác $v_\pi$, lượt bị cắt; ở (b), $Z$ ghi cả cắt ngắn." (17 âm tiết); kết luận "Với cờ sai, thuật toán giải một MDP kết thúc tại bước $500$." (11 âm tiết). Ba dòng đầu gần như chỉ có công thức.
- **Mật độ:** khoảng 30 âm tiết, 5 dòng, không bảng.
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không có bài tổng hợp; Tình huống 10.1, 10.2 của ghi chú. Đợt sửa sau cổng: bỏ bảng hai hàng để trang còn 5 dòng.
- **Ghi chú diễn giả (đến khoảng 200):** ở (a) lợi thế nhỏ và dương như mọi bước khác, critic được kéo về $100$; ở (b) actor giảm xác suất của chính các hành động giữ cột, critic học mục tiêu $1$ cho trạng thái cuối; Tình huống 10.3 (Breakout) chỉ nêu tên, số đo không trình chiếu.
- **Sửa 2026-11-13 (bảng phát hiện):** dòng kết luận thành hai câu theo Tình huống 10.2 của ghi chú: "Với cờ sai, thuật toán học như thể lượt kết thúc thật ở bước $500$." và "Bài toán này không còn tính Markov trên trạng thái quan sát." (trước: "Kết luận: … giải một MDP kết thúc tại bước 500"; tách hai câu vì một câu 26 âm tiết vượt trần dòng; 6 dòng); ghi chú diễn giả thêm lý do (trạng thái không chứa chỉ số thời gian) và bỏ câu Breakout. `deck_check`: 48 âm tiết, 6 dòng, dòng dài nhất 17; ghi chú 176 token (lời giải, trần 250).

#### `L10-707` Trả lời vấn đề trung tâm
- **Vị trí, loại:** mạch 7; trả lời có điều kiện.
- **Lý do tồn tại, nhu cầu:** đóng bài toán của `L10-109` bằng năm câu trả lời có điều kiện và dòng "Nguồn:".
- **Liên kết:** trước: `L10-706`; sau: `L10-708`. **Mục tiêu:** 1–5. **Ghi chú:** §7.3 (`topic-23`).
- **Mặt trang:** năm dòng đánh số và dòng nguồn: (1) "Đường cơ sở không phụ thuộc $A_t$ giữ kỳ vọng; critic sai làm chệch." (11); (2) "GAE γ-just khi $\lambda=1$ trên lượt đầy đủ hoặc critic đúng." (10); (3) "Hàm thay thế đúng bậc một, sai số bị chặn; bước miền tin cậy chặn mức giảm." (15); (4) "TRPO giải xấp xỉ, chỉ bảo đảm KL trung bình mẫu $\le\kappa$." (11); (5) "PPO dùng lại đoạn thu $K$ epoch với mục tiêu cắt, không cận KL." (13); "Nguồn: Sutton và Barto (2018); Schulman và cộng sự (2015–2017); Achiam và cộng sự (2017)." (15).
- **Mật độ:** khoảng 75 âm tiết (trần 80 của trang tổng kết), 6 dòng, mỗi dòng không quá 15 âm tiết; số hiệu kết quả trong ghi chú diễn giả.
- **Hình, phút:** —; 1.
- **Quyết định:** thêm: bộ cũ không có trang trả lời bài toán; §7.3 của ghi chú. Đợt sửa sau cổng: dòng (3) và dòng nguồn rút về dưới 20 âm tiết; trang nguồn của bài giảng gốc và Jin, Li và Wang (2024) chuyển vào ghi chú diễn giả.
- **Ghi chú diễn giả:** số hiệu kết quả của từng dòng (Mệnh đề 10.2, 10.3, 10.8, 10.14, 10.15, 10.22, Định lý 10.26, Hệ quả 10.27, 10.31, Mệnh đề 10.34, Nhận xét 10.38, Mệnh đề 10.41, Định nghĩa 10.43); kết quả hội tụ hiện có cho PPO-Clip chỉ nói về điểm dừng trong một mô hình đơn giản hóa (Nhận xét 10.51; Jin, Li và Wang, 2024); bài giảng gốc tr. 3–42; đối chiếu với năm dòng của `L10-109`.
- **Sửa 2026-11-13 (bảng phát hiện):** dòng (4) "…; sai số, mức giảm bị chặn."; dòng (5) "TRPO xấp xỉ; trên bộ đệm: KL trung bình mẫu ${\le\kappa}$, hàm thay thế mẫu tăng." theo Nhận xét 10.38 (D10). `deck_check`: 80 âm tiết (trước 77; trần 80 của trang tổng kết), 6 dòng, dòng dài nhất 17.

#### `L10-708` Câu hỏi tự kiểm tra
- **Vị trí, loại:** mạch 7; câu hỏi tự kiểm tra.
- **Lý do tồn tại, nhu cầu:** bốn câu, mỗi câu kiểm một giả thiết hoặc một phân biệt.
- **Liên kết:** trước: `L10-707`; sau: `L10-709`. **Mục tiêu:** 2, 3, 4, 5. **Ghi chú:** §7.4 (`topic-23`).
- **Mặt trang:** "Câu hỏi: trả lời và nêu kết quả đã dùng." (9) rồi bốn dòng: (1) "Giải thích: $G_t-\hat v(S_t,w)$ không chệch cho gradient, chệch cho lợi thế khi $\hat v\ne v_\pi$." (12); (2) "Với bước chỉ đổi $p_B$, giải thích vì sao hàm thay thế đúng mà chặn cải thiện vẫn phạt." (16); (3) "Tỉ lệ cắt $\tfrac33$: xác định mọi mẫu có gradient $0$ hay không." (11); (4) "Xác định TRPO thực hành có bảo đảm $J$ không giảm hay không." (12). Câu viết dạng yêu cầu, không dấu hỏi tu từ.
- **Mật độ:** 60 âm tiết, 5 dòng.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm: bộ cũ không có câu hỏi tự kiểm tra; §7.4 của ghi chú. Phút giảm từ 1 xuống 0,5 để nhường cho trang `L10-710`; lời giải ngắn nằm trong ghi chú diễn giả và thuộc 30 phút chữa bài.
- **Ghi chú diễn giả:** lời giải ngắn của §7.4 (Mệnh đề 10.2; Bổ đề 10.19 trùng hàm thay thế khi phân bố trạng thái không đổi; Mệnh đề 10.40(d) và Định nghĩa 10.47; Hệ quả 10.29 và Nhận xét 10.38).
- **Sửa 2026-11-13 (bảng phát hiện):** ghi chú diễn giả: lời giải câu 4 nêu hai bất đẳng thức trên bộ đệm; dòng nguồn dẫn khối có thật cho từng câu: "§7.4 (câu 1–2); Mệnh đề 10.40, Định nghĩa 10.47 (câu 3); Hệ quả 10.29, Nhận xét 10.38 (câu 4)" (D10). Ghi chú 152 token (lời giải).

#### `L10-709` Bài tập về nhà và tài liệu đọc
- **Vị trí, loại:** mạch 7; bài về nhà (trang thứ nhất của hai trang cùng tiêu đề).
- **Lý do tồn tại, nhu cầu:** ánh xạ Bài tập 10.13–10.17 của `materials/lec-10/exercises.md` và Bài tập củng cố 10.1–10.12 của ghi chú tới các mạch.
- **Liên kết:** trước: `L10-708`; sau: `L10-710`. **Mục tiêu:** 1–5. **Ghi chú:** §7.5 (`topic-23`); `exercises.md`, bảng `Mạch | Mở phần | Bài tập`.
- **Mặt trang (cập nhật 2026-11-13):** bảng `Mạch | Bài tập (tệp bài tập) | Bài tập củng cố (ghi chú)`, bảy hàng chép đúng bảng mạch hiện tại của `exercises.md` (làm lại 2026-11-12): 1. Mở đầu: — | —; 2: 10.14 | 10.1, 10.4, 10.5, 10.10; 3: 10.13, 10.15 | 10.6, 10.7; 4: 10.16 | 10.11; 5: 10.17 | 10.8, 10.9; 6: 10.14 | 10.2, 10.12; 7: — | 10.3. Tên mạch theo trang tiêu đề mạch. Bản 2026-11-05 (bộ 10.13–10.21 cũ, gộp mạch 1–2) đã thay.
- **Mật độ:** 50 âm tiết theo `deck_check` (2026-11-13; ô chỉ chứa số không tính), 7 hàng bảng; bảng là trang bài về nhà theo trần 80 của bảng, không vượt trần; ảnh chụp 1600×900 vừa khung.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm: bộ cũ không có trang bài về nhà. Đợt sửa sau cổng: tách khỏi trang tài liệu đọc (`L10-710`). Cập nhật 2026-11-05: có `exercises.md`, nên bảng chuyển sang ánh xạ của tệp đó (bỏ hàng "4–6. Các kết quả có bảo đảm"; Bài tập 10.3 ở mạch 7 như `exercises.md`), thêm cột Bài tập củng cố; liên kết viewer "Bài tập" đặt ở `L10-710`.
- **Ghi chú diễn giả (cập nhật 2026-11-13):** Bài tập 10.13–10.17 trong tệp bài tập, lấy từ bài tập của Sutton và Barto (2018), hai mức: nhận biết (10.13); tính toán hoặc chứng minh (10.14–10.17); Bài tập 10.14 thuộc mạch 2 và mạch 6; Bài tập củng cố 10.1–10.12 có lời giải trong ghi chú, các bài có phiên bản trên trang chiếu; Bài tập 10.3 kiểm các kết quả có bảo đảm.
- **Sửa 2026-11-13 (bảng phát hiện):** xem "Mặt trang" và "Ghi chú diễn giả" đã cập nhật. `deck_check`: 50 âm tiết (bảng 7 hàng), ghi chú 106 token.

#### `L10-710` Bài tập về nhà và tài liệu đọc
- **Vị trí, loại:** mạch 7; tài liệu đọc, liên kết viewer, dòng nối Bài 11 (trang thứ hai cùng tiêu đề; trang cuối bài).
- **Lý do tồn tại, nhu cầu:** tài liệu đọc có mục cụ thể và nối sang bài kế tiếp.
- **Liên kết:** trước: `L10-709`; sau: — (cuối bài). **Mục tiêu:** 1–5. **Ghi chú:** §7.5, §7.6 (`topic-23`; dòng Bài 11 là `topic-24`); nguồn tr. 43.
- **Mặt trang (cập nhật 2026-11-13, theo "Hướng dẫn đọc thêm" của ghi chú):** "Tài liệu đọc: Sutton và Barto (2018), §13.4–13.5, §7.1, §12.1–12.3."; "Schulman và cộng sự (2015), §2–3, Phụ lục C; (2016), §2–3; (2017), §3–5."; "Achiam và cộng sự (2017), §5; Huang và cộng sự (2022); Engstrom và cộng sự (2020)."; một dòng nối "Bài 11: SPO đổi mục tiêu, SAM+PPO đổi bước tối ưu; học khác chính sách có bộ nhớ phát lại." (20 âm tiết) thay hai dòng D2. Bản trước: dòng liên kết "Ghi chú bài giảng · Bài tập" tới `material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html` và `material-viewer.html?doc=materials/lec-10/exercises.md&deck=lecture-10-trpo-va-ppo.html` (cập nhật 2026-11-05); "Bài 11: biến thể SPO, SAM+PPO đổi mục tiêu tỉ số, bước tối ưu." và "Bài 11 dùng bộ nhớ phát lại, tỉ số theo chính sách hành vi." (D2), liên kết `lecture-11-cac-phuong-phap-gradient-chinh-sach-nang-cao.html`. Ghi chú: dòng Schulman và cộng sự có mục (D1).
- **Mật độ:** 50 âm tiết theo `deck_check` (2026-11-13; trước 46), 5 dòng.
- **Hình, phút:** —; 0,5.
- **Quyết định:** tách (từ trang `L10-709` của bản trước, theo quy ước đếm hàng bảng của cổng storyboard).
- **Ghi chú diễn giả:** Bài 11 viết tỉ số $\rho_t(\theta)$ của bài này là $w_t$ và dùng $\rho_t$ cho tỉ số với chính sách hành vi; Phần II của nguồn (A3C, DDPG, SAC, …) thuộc Bài 11.
- **Sửa 2026-11-13 (bảng phát hiện):** xem "Mặt trang" đã cập nhật. `deck_check`: 50 âm tiết, 5 dòng, dòng dài nhất 19.

**Mạch 7 và hành trình khái niệm.** Mạch kết luận không mở khái niệm mới; sáu bước ghi `không áp dụng`. `L10-705`–`L10-706` là bước ứng dụng và kiểm tra của cụm γ-just và cụm GAE trên đoạn thu (mạch 3). Phút: $0{,}5+1+1+1+0{,}5+1{,}5+1+1+0{,}5+0{,}5+0{,}5=9$.

## Bài tập trên mặt trang

| cụm | trang đề | trang lời giải | khối của ghi chú | loại | kết quả trên mặt trang (trùng ghi chú) |
|---|---|---|---|---|---|
| Đường cơ sở (mạch 2) | `L10-210` | `L10-210` (fragment) | Bài tập 10.1 | lời giải mẫu trên mặt trang | (a), (b) hợp lệ; (c), (d) $\widehat g_b\equiv0$ |
| Lợi thế (mạch 2) | `L10-211` ("Câu hỏi:") | `L10-211` (fragment) | Ví dụ 10.6, kiểm tra lại | câu hỏi có lời giải | $0$; $0$ |
| Actor–critic (mạch 2) | `L10-216` | `L10-216` (fragment) | Bài tập 10.5 | lời giải mẫu trên mặt trang | $0{,}35$; $0$; $0{,}0875\ne0{,}2$ |
| GAE (mạch 3) | `L10-309` | `L10-309` (fragment) | Bài tập 10.7 | lời giải mẫu trên mặt trang | $\widehat A=(3{,}572;\,2{,}6;\,1{,}52;\,1)$, $V^{\mathrm{targ}}=(5{,}572;\,5{,}6;\,2{,}52;\,3)$ |
| Hàm thay thế, chặn cải thiện (mạch 4) | `L10-413` | `L10-414` | Bài tập 10.11 (a)–(d) | lời giải mẫu, trang kế tiếp | $0{,}0895$; $0{,}085$; $-0{,}032$; $0{,}000619\le0{,}001$ |
| TRPO (mạch 5) | `L10-509` | `L10-510` | Bài tập 10.8 | lời giải mẫu trên mặt trang | $x_2=(\tfrac23;\,-\tfrac13)$, $\tau=\tfrac23$, $\Delta=(0{,}1155;\,-0{,}0577)$ |
| PPO-Clip, chẩn đoán (mạch 6) | `L10-619` | `L10-620` | Bài tập 10.12 (a)–(c) | lời giải mẫu, trang kế tiếp | $\mathcal L^{\mathrm{CLIP}}=0{,}1505$; $\tfrac24$; approxKL $0{,}0203$, dừng sớm |
| PPO-Penalty (mạch 6) | `L10-608` | `L10-608` (fragment) | Bài tập 10.12 (d) | câu hỏi có lời giải trên mặt trang | $\beta=2$; giữ $\beta=1$ |
| Tổng hợp (mạch 7) | `L10-705` | `L10-706` | Tình huống 10.1, 10.2 | bài tổng hợp, lời giải trang kế tiếp | $0{,}05$; $0{,}0970$; $95{,}097$; $-94$; $-88{,}36$ |

Ghi chú diễn giả của mỗi trang đề có dòng "Gợi ý:" lấy từ khối `hint` của ghi chú. Bài về nhà (lời giải chỉ trong ghi chú): 10.2, 10.3, 10.4, 10.6, 10.9, 10.10. Mỗi cụm khái niệm lớn (đường cơ sở, actor–critic, GAE, hàm thay thế và chặn cải thiện, TRPO, PPO) có ít nhất một bài tập có lời giải mẫu trên mặt trang.

## Chứng minh

- Trang riêng: `L10-205` (Mệnh đề 10.2), `L10-404` (Bổ đề 10.19), `L10-409` (Định lý 10.26, kèm phát biểu Bổ đề 10.25).
- Dòng "Chứng minh." trên trang kết quả: Mệnh đề 10.5 (`L10-208`), 10.8 (`L10-213`), Bổ đề 10.12 (`L10-302`), Mệnh đề 10.14 (`L10-304`, chứng minh bốn bước nén thành một dòng, chi tiết trong ghi chú diễn giả), 10.15 (`L10-306`), 10.22 (`L10-406`), 10.33 (`L10-502`), 10.34 (`L10-503`), 10.40 (`L10-604`), 10.41 (`L10-606`); Mệnh đề 10.48 trong ghi chú diễn giả `L10-611`; Mệnh đề 10.3 và 10.24 trong ghi chú diễn giả `L10-202`, `L10-407`; Hệ quả 10.20, 10.27, 10.29, 10.31 nêu ý chứng minh trong ghi chú diễn giả.
- Không chứng minh (ghi trên trang hoặc trong ghi chú diễn giả): Nhận xét 10.28 (`L10-408`), Nhận xét 10.51 (`L10-618`).

## Đối chiếu mã trang

**Bộ trang chiếu cũ → bộ mới.**

| mã cũ | tiêu đề cũ | quyết định | mã mới |
|---|---|---|---|
| `L10-01` | Tối ưu chính sách theo miền tin cậy (TRPO) | sửa | `L10-101` |
| `L10-02` | Kết quả học tập | sửa | `L10-104` |
| `L10-03` | Dữ liệu đổi sau mỗi lần cập nhật | sửa | `L10-108` |
| `L10-04` | Quy ước của bài | sửa | `L10-102` |
| `L10-05` | REINFORCE dùng return toàn phần | sửa | `L10-103` |
| `L10-06` | Baseline loại phần chung của return | sửa | `L10-201` |
| `L10-07` | Baseline không đổi kỳ vọng hàm điểm | sửa | `L10-204` |
| `L10-08` | Actor–critic có thể dùng đích Monte Carlo hoặc bootstrap | sửa | `L10-212` |
| `L10-09` | Critic tạo sai số sai phân thời gian | sửa | `L10-213` |
| `L10-10` | GAE trộn nhiều tầm bootstrap | sửa | `L10-303` |
| `L10-11` | Hai mặt nạ có hai nhiệm vụ | sửa | `L10-308` |
| `L10-12` | Ví dụ GAE phân biệt kết thúc và truncation | sửa | `L10-307` |
| `X01` | Bài tập: baseline và GAE | sửa, tách | `L10-210`, `L10-309` |
| `L10-13` | Gradient lớn có thể phá chính sách | sửa | `L10-401` |
| `L10-14` | Miền tin cậy giới hạn nơi xấp xỉ có ích | sửa, tách | `L10-411`, `L10-412` |
| `L10-15` | Dữ liệu cũ vẫn cho biết hướng thay đổi | sửa, gộp | `L10-405` |
| `L10-16` | Đẳng thức, xấp xỉ rồi ràng buộc thực nghiệm | sửa, tách | `L10-403` (đẳng thức), `L10-405`, `L10-412` |
| `L10-17` | Fisher cục bộ và ước lượng từ batch | sửa | `L10-502` |
| `L10-18` | Ví dụ bước natural gradient | sửa | `L10-504` |
| `L10-19` | TRPO giải hệ rồi tìm đường | sửa, tách | `L10-506`, `L10-507` |
| `L10-20` | TRPO chỉ nhận bước qua đủ hai kiểm tra | sửa, gộp | `L10-507`, `L10-508` |
| `X02` | Bài tập: bước TRPO cục bộ | sửa, tách | `L10-509`, `L10-510` |
| `L10-21` | PPO cần bước gần nhưng chỉ dùng tối ưu bậc nhất | sửa | `L10-601` |
| `L10-22` | Tỷ số tại hành động đã lấy mẫu | gộp | `L10-405`, `L10-603` |
| `L10-23` | Hai số đại diện cho phần bị chặn | gộp | `L10-605` |
| `L10-24` | Công thức PPO-Clip phụ thuộc dấu lợi thế | sửa, tách | `L10-603`, `L10-604` |
| `L10-25` | Trong và ngoài dải clipping | gộp | `L10-605` |
| `L10-26` | Clipping không phải ràng buộc KL | sửa | `L10-606` |
| `L10-27` | Actor chuẩn hóa lợi thế, critic giữ đích thô | sửa | `L10-609` |
| `L10-28` | Kích thước từ rollout đến batch | gộp | `L10-612` |
| `L10-29` | Đường dữ liệu PPO | sửa, gộp | `L10-612` |
| `L10-30` | Cấu trúc dữ liệu của một batch PPO | gộp | `L10-612` |
| `L10-31` | Bốn chẩn đoán, ba phép giảm | sửa | `L10-611` |
| `L10-32` | Siêu tham số tương tác với nhau | sửa | `L10-615` |
| `L10-33` | Value clipping là một biến thể | gộp | `L10-617` |
| `L10-34` | Tiền xử lý và khởi tạo đổi động lực học | gộp | `L10-617` |
| `L10-35` | Báo cáo PPO như một thuật toán đầy đủ | gộp | `L10-617` (ghi chú diễn giả) |
| `X03` | Bài tập: kiểm toán một batch PPO | sửa, tách | `L10-619`, `L10-620` |
| `L10-36` | TRPO và PPO kiểm soát bước theo hai cách | sửa | `L10-616` |
| `L10-37` | Mô hình lý thuyết tách vòng ngoài và vòng trong | gộp | `L10-618` |
| `L10-37B` | Kết quả điểm dừng có phạm vi hẹp | gộp | `L10-618` |
| `L10-38` | Bốn hợp đồng cần giữ | sửa | `L10-701` |

Không mã cũ nào bị bỏ hẳn nội dung; mọi mã cũ đều đổi. Viewer không liên kết neo trang của bộ trang chiếu, `index.html` và Bài 09 chỉ liên kết tên tệp, nên đổi mã không làm gãy liên kết. Các trang mới không có mã cũ tương ứng ghi `thêm` trong mục của trang.

**Kế hoạch đã duyệt (101 trang) → bộ mới (95 trang).** Mạch 1: `L10-101`–`L10-110` giữ mã (trang khung `L10-110` được gộp ở bản trước rồi tách lại sau cổng). Mạch 2: `L10-200`–`L10-206` giữ mã; kế hoạch `L10-207` gộp vào `L10-202`; kế hoạch `L10-208`…`L10-217` thành `L10-207`…`L10-216`. Mạch 3: `L10-300`–`L10-304` giữ mã, kế hoạch `L10-305` gộp vào `L10-304`; kế hoạch `L10-306`…`L10-309` thành `L10-305`…`L10-308`; kế hoạch `L10-310` + `L10-311` thành `L10-309`. Mạch 4: `L10-400`–`L10-402` giữ mã; kế hoạch `L10-403` + `L10-404` thành `L10-403`; kế hoạch `L10-405`…`L10-408` thành `L10-404`…`L10-407`; kế hoạch `L10-409` + `L10-410` thành `L10-408`; kế hoạch `L10-411`, `L10-412`, `L10-413`, `L10-414` thành `L10-409`, `L10-410`, `L10-411`, `L10-412`; kế hoạch `L10-415`, `L10-416` thành `L10-413`, `L10-414`. Mạch 5: `L10-500`–`L10-510` giữ mã (cặp đề và lời giải `L10-509`, `L10-510` gộp ở bản trước rồi tách lại ở cổng lần 2). Mạch 6: `L10-600`–`L10-610` giữ mã (cặp `L10-607`, `L10-608` gộp ở bản trước rồi tách lại sau cổng); kế hoạch `L10-611` + `L10-612` thành `L10-611`; kế hoạch `L10-613`…`L10-621` thành `L10-612`…`L10-620`. Mạch 7: `L10-700`–`L10-702` giữ mã, kế hoạch `L10-703` gộp vào `L10-702`; kế hoạch `L10-704`…`L10-710` thành `L10-703`…`L10-709`; `L10-710` là trang mới tách từ trang bài về nhà.

**Bộ 95 trang → bộ 101 trang (bản viết và đợt sửa D1).** Mọi mã cũ giữ nguyên nội dung chính. Trang mới: `L10-212b` (tách từ `L10-212`, bản viết), `L10-702b` (tách từ `L10-702`, bản viết), `L10-412b` (Hệ quả 10.31, tách từ `L10-412`), `L10-502b` (Mệnh đề 10.33, tách từ `L10-502`), `L10-611b` (Mệnh đề 10.48, tách từ `L10-611`), `L10-617b` (bảng chi tiết cài đặt và kết luận, tách từ `L10-617`). Riêng `L10-617` đổi vai: mã cũ "Chi tiết cài đặt" nay là "Ví dụ: cắt mất mát giá trị" (ví dụ dẫn nhập), còn bảng chuyển sang `L10-617b`. Số trang theo mạch: 10, 18, 10, 16, 12, 23, 12.

## Bảng kiểm `quill` (Outline, Threads, Concept)

Dùng như danh sách kiểm; không tạo `quill.json`.

**Outline (thứ tự tiên quyết).** Mỗi trang dùng một ký hiệu sau trang định nghĩa hoặc nhắc lại của nó: $\mu_0$, $Z$, $U$, $\psi_t$ (`L10-102`); hàm điểm softmax, $q_\pi$, $v_\pi$ (`L10-103`); $b$, $\widehat g_b$ (`L10-203`); $A_\pi$ (`L10-207`); $\delta_t$ (`L10-212`); $G_{t:t+n}$ (`L10-302`); $\widehat A_t$, $\lambda$ (`L10-303`); $\nu^\pi$ (`L10-403`); $\rho_t$, $\mathcal L$ (`L10-405`); $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$ (`L10-407`); $\kappa$ (`L10-412`); $F$ (`L10-502`); $\widehat D$, $\mathcal D$ (`L10-507`); $\epsilon$, $\mathcal L^{\mathrm{CLIP}}$ (`L10-603`); $\beta$ (`L10-607`), $\kappa_{\mathrm{targ}}$ (`L10-608`); $\mathcal H$, $L$, $L^V$, $c_1$, $c_2$, $\widehat A^{\mathrm{raw}}$ (`L10-609`); approxKL, tỉ lệ cắt (`L10-611`). Đã sửa trong lúc soạn: `L10-208` không dùng $\nu^\pi$ trên mặt trang (dạng chiếm dụng sang ghi chú diễn giả); `L10-109` không dùng $\delta_t$, $\nu^\pi$, $\kappa$ và chữ KL; thuật toán đều đứng sau ví dụ tính tay (`L10-206`→`L10-209`, `L10-214`→`L10-215`, `L10-307`→`L10-308`, `L10-505`→`L10-506`, `L10-504`/`L10-505`→`L10-507`, `L10-607`→`L10-608`, `L10-610`→`L10-613`). Sau cổng: mọi khái niệm cốt lõi có bước vấn đề hoặc trực giác trên mặt trang trước định nghĩa (`L10-305`, `L10-412`, `L10-502`, `L10-607`, `L10-611`).

**Threads (sợi mở và đóng).**

| sợi | mở | đóng |
|---|---|---|
| Phương sai phụ thuộc mức chung của phần thưởng | `L10-106` | `L10-202` ($\tfrac49(b-1)^2$), `L10-207` (lợi thế không đổi khi cộng hằng) |
| Một lượt cho bước ngược chiều | `L10-107` | `L10-206` (cùng lượt, đường cơ sở cho bước cùng chiều) |
| Bước lớn theo đúng gradient làm $J$ giảm | `L10-108` | `L10-401`–`L10-411` (chặn cải thiện, miền tin cậy), `L10-613` (PPO dùng lại dữ liệu) |
| Critic sai làm chệch | `L10-213` (b) | `L10-214`, `L10-216`, `L10-305`, `L10-306` |
| γ-just khác không chệch cho lợi thế | `L10-305` | `L10-306` "Lưu ý:", `L10-708` câu 1 |
| Cờ kết thúc và cắt ngắn | `L10-102` | `L10-307`, `L10-308`, `L10-309`, `L10-705`–`L10-706` |
| $0{,}26$ so với $0{,}296$ (sai số $0{,}036$) | `L10-402` | `L10-406`, `L10-408`, `L10-410` |
| Cận chỉ chứng nhận bước rất nhỏ | `L10-410` | `L10-411` (lược đồ đứng yên), `L10-412` (ràng buộc thay phạt), `L10-708` câu 2 |
| Bảo đảm của TRPO thực hành | `L10-412` (nghiệm chính xác) | `L10-508`, `L10-616`, `L10-708` câu 4 |
| Mục tiêu cắt không chặn KL | `L10-606` | `L10-614` (KL $0{,}1042$), `L10-616`, `L10-707` |
| Tỉ lệ cắt khác tập gradient bằng $0$ | `L10-604`, `L10-611` | `L10-614`, `L10-620`, `L10-708` câu 3 |
| Dữ liệu theo chính sách | `L10-108` | `L10-612` (từ mini-batch thứ hai đã khác chính sách), `L10-710` (Bài 11) |

**Concept (năng lực kiểm tra và nhất quán thuật ngữ).** Mỗi khái niệm cốt lõi có năng lực kiểm được: nhận diện đường cơ sở hợp lệ (`L10-210`); tính lợi thế và kiểm $\sum_a\pi A_\pi=0$ (`L10-211`); tính sai số TD khi critic sai (`L10-216`); chạy GAE lùi với cờ (`L10-309`); đánh giá một bước bằng bổ đề, hàm thay thế, cận và KL (`L10-413`–`L10-414`); chạy gradient liên hợp và tính bước (`L10-509`–`L10-510`); kiểm mini-batch PPO (`L10-619`–`L10-620`); kiểm giả thiết trên CartPole (`L10-705`–`L10-706`). Thuật ngữ thống nhất với bảng Việt–Anh của `outline.md`: "đường cơ sở", "lợi tức", "cắt ngắn", "đoạn thu", "bộ đệm", "tỉ số", "tỉ lệ cắt", "hàm thay thế", "chặn cải thiện", "mục tiêu" (không "đích").

## Câu chữ dự kiến và `no-ai-slop`

Câu dự kiến trên mặt trang (luận đề, mười hai dòng của `L10-104` và `L10-109`, dòng dẫn và từ khóa của sáu trang tiêu đề mạch, các dòng "Nhu cầu:", "Diễn giải:", "Lưu ý:" trong các mục trên) được soát theo `no-ai-slop` chế độ Edit và `eval.md`: không câu tương phản kiểu "không phải X mà là Y", không câu hỏi tu từ, không khẩu hiệu hay chuỗi mũi tên, không lời chỉ đường; mỗi câu kết luận là một kết luận có điều kiện hoặc một con số; động từ trực tiếp ("cắt", "giữ", "chặn", "tính"). Các chỗ đã sửa khi soát: luận đề bỏ "đổi phương sai lấy độ chệch" (khẳng định vượt ghi chú); dòng 2–6 của `L10-109` bỏ ký hiệu chưa định nghĩa; tiêu đề bộ cũ dạng câu ("Gradient lớn có thể phá chính sách", "TRPO giải hệ rồi tìm đường") thay bằng cụm danh từ; "Những gì TRPO thực hành mất" thành "Phạm vi bảo đảm của TRPO thực hành". Tác tử soạn đếm lại âm tiết trên HTML ở bước B.

Đợt sửa sau cổng storyboard (2026-11-04): luận đề rút từ 47 xuống 30 âm tiết, bỏ tên tiếng Anh; các câu dự kiến quá 20 âm tiết (`L10-201`, `L10-601`, `L10-606`, `L10-609`, `L10-618`, `L10-707`) đã ngắt dòng, kiểm bằng script đếm trên các câu trong ngoặc kép của mục "Mặt trang" (không dòng nào quá 20, trừ sáu dòng dẫn trang tiêu đề mạch theo trần 25 riêng); bốn khái niệm thiếu bước trực giác trên mặt trang (`L10-502`, `L10-412`, `L10-607`, `L10-611`) và `L10-305` có thêm dòng "Trực quan." hoặc "Nhu cầu:" viết theo lời của ghi chú, không thêm khẳng định mới.

## Đợt sửa D1

Đợt sửa sau năm báo cáo rà soát độc lập trên bản cố định 97 trang (vai sinh viên, chuyên gia, toán–thuật toán, sư phạm với `no-ai-slop` Detect, mạch), theo quyết định E1–E11 của điều phối viên. Bảng xử lý từng phát hiện nằm ở tệp `d1-disposition.md` của tác tử biên tập; `review-log.md` do điều phối viên ghi. Với các trang dưới đây, mặt trang hiện hành là bản trong bộ trang chiếu; mục từng trang ở trên đã được viết lại cho các trang tách, trang mới và trang đổi cấu trúc (`L10-212`, `L10-212b`, `L10-307`, `L10-308`, `L10-309`, `L10-402`, `L10-412`, `L10-412b`, `L10-502`, `L10-502b`, `L10-610`, `L10-611`, `L10-611b`, `L10-617`, `L10-617b`, `L10-702`, `L10-702b`).

| trang | thay đổi mặt trang | căn cứ |
|---|---|---|
| `L10-103` | (G1)–(G4) tách đủ bốn nhãn, có $R_{\max}$, $T_{\max}$, Markov, softmax hoặc Gauss; $v_\pi$, $q_\pi$ trên một dòng | E3 |
| `L10-106`, `L10-108`, `L10-301`, `L10-305`, `L10-402`, `L10-501`, `L10-504`, `L10-505`, `L10-602`, `L10-610`, `L10-614` | thêm dòng hoặc vế "Tính …"; `L10-108` chuyển câu Hệ quả 09.26 vào ghi chú; `L10-301` thêm $\gamma=0{,}9$ và $0{,}9\cdot0{,}8$ thay $0{,}72$; `L10-505` nêu $p_0=g$, $\omega_k$, $\theta\in\mathbb R^d$; `L10-602` nêu $\pi_{\mathrm{old}}$ | E7, E3 |
| `L10-109` | năm dòng trả lời viết thành câu có điều kiện; dòng 2 tách đường cơ sở và sai số TD | phát hiện của vai sư phạm, chuyên gia, sinh viên |
| `L10-203`, `L10-204`, `L10-207`, `L10-208`, `L10-209`, `L10-212`, `L10-213`, `L10-215`, `L10-302`, `L10-303`, `L10-304`, `L10-306`, `L10-308`, `L10-403`, `L10-405`, `L10-406`, `L10-407`, `L10-408`, `L10-411`, `L10-412`, `L10-412b`, `L10-502`, `L10-502b`, `L10-503`, `L10-506`, `L10-507`, `L10-508`, `L10-603`, `L10-604`, `L10-606`, `L10-608`, `L10-609`, `L10-611`, `L10-611b`, `L10-613`, `L10-618` | số hiệu của ghi chú trong nhãn kết quả, một số hiệu mỗi trang; số hiệu khác trên cùng trang thay bằng tên kết quả (`L10-208`, `L10-212`, `L10-306`, `L10-406`, `L10-408`, `L10-507`, `L10-609`, `L10-613`) | E2 |
| `L10-204`, `L10-206` | "Ý nghĩa:" giữ nguyên kỳ vọng; "Diễn giải:" so số bước còn lại với số bước kỳ vọng | phát hiện nhẹ |
| `L10-207` | thêm "Nhu cầu:" và "Trực quan." trước định nghĩa | E7 |
| `L10-211` | dòng chữ nêu phần thưởng, chuyển tiếp và $\gamma$; hình thu nhỏ trong lưới hai cột; $\theta=(\theta_A;\,\theta_B)$ | E5 |
| `L10-212`, `L10-212b` | trực giác $1{,}35>1$; vế cập nhật $w$; "Nhắc lại:" sai số TD sang `L10-212b` | E7, phát hiện của vai chuyên gia |
| `L10-213` | $\delta_1=1$ cho hành động 1 tại $s_B$; "với critic đúng" | E9 |
| `L10-214`, `L10-216`, `L10-305` | bỏ $e_A$, $e_B$ trên mặt trang (tọa độ viết trực tiếp) | phát hiện nhẹ (sinh viên, mạch) |
| `L10-302` | thêm "Trực quan."; dòng "Chứng minh." chuyển vào ghi chú diễn giả | E7 |
| `L10-303` | $\lambda=1$: $G^\lambda_t=G_t$ | phát hiện nhẹ |
| `L10-306` | "Lưu ý:" gọi ví dụ bằng tên đối tượng | phát hiện nhẹ (mạch) |
| `L10-307` | bỏ hình Bài 08 | E5 |
| `L10-308` | nêu $h$, $V_h$; bước 1 có điều kiện $Z_h=0$, $U_h=0$ | E3, E9 |
| `L10-403` | khối $0{,}145\le1$ của $\nu^\pi$ | phát hiện nhẹ |
| `L10-405` | $\rho_\theta(s,a)$, $\nu^{\mathrm{old}}$, $A_{\mathrm{old}}$ nêu trên mặt trang | phát hiện nhẹ |
| `L10-406` | "Ý nghĩa:" theo hướng có $\nabla\mathcal L^\top\Delta>0$ | phát hiện nhẹ (chuyên gia) |
| `L10-407` | "Nhu cầu:" có hai phân phối tại $s_B$ | phát hiện nhẹ |
| `L10-408` | giả thiết viết bằng lời; "Ý nghĩa:" đọc thành lời | phát hiện nhẹ, E2 |
| `L10-410` | bỏ chữ Việt trong KaTeX; gộp "Diễn giải:" với điều kiện $\Delta p<0{,}0556$ | phát hiện nhẹ |
| `L10-412`, `L10-412b` | tách; số của nghiệm chính xác ($\chi_{\pi_{k+1}}\approx0{,}472$, cận $\approx-3{,}91$, $\Delta J\approx0{,}299$) | E1, E7 |
| `L10-414` | lời giải điền khuôn bảng của đề | E10 |
| `L10-502`, `L10-502b` | tách định nghĩa Fisher và Mệnh đề 10.33 | E7 |
| `L10-503` | $g\ne0$, $F$ đối xứng; "giả nghịch đảo $F^+$ (pseudoinverse)" | phát hiện nhẹ |
| `L10-507` | "Đầu ra:", điều kiện dừng; $\widehat{\mathbb E}_{\mathcal D}$ nêu ở bước 1; hàm thay thế mẫu và KL trung bình mẫu ở bước 4 | E8, E3 |
| `L10-601` | "Nhu cầu:"; bỏ câu lặp; "phần tăng/phần giảm của mục tiêu"; "một lần tìm kiếm lùi"; gọi tên bán kính cắt $\epsilon$ | E7 |
| `L10-604` | "trừ $\rho_t=1\pm\epsilon$" | E9 |
| `L10-605` | thêm "Diễn giải:" | E7 |
| `L10-606` | câu cơ chế tỉ số ra ngoài khoảng chuyển vào ghi chú diễn giả | E6 |
| `L10-607` | "Nhu cầu:" nêu nhu cầu chỉnh $\beta$ | phát hiện nhẹ |
| `L10-609` | thêm "Trực quan."; $\widehat{\mathbb E}_{\mathcal D}$ thay $\widehat{\mathbb E}_{\mathcal B}$; câu chuẩn hóa lợi thế chuyển vào ghi chú diễn giả | E6, E7 |
| `L10-610` | "Kết luận:" ghi $\nabla_\theta\mathcal L^{\mathrm{CLIP}}$ | phát hiện nhẹ |
| `L10-611`, `L10-611b` | tách; dạng $-\log\rho$; định nghĩa phương sai được giải thích; điều kiện cùng miền hỗ trợ | E3, E7, E9 |
| `L10-613` | "Đầu ra:", điều kiện dừng; bỏ "(tùy chọn)" ở bước (a) | E6, E8 |
| `L10-614` | "Diễn giải:" về KL; nhận xét phương sai được giải thích chuyển vào ghi chú | E3 |
| `L10-616` | ô giả thiết viết đủ "đều chính xác" | phát hiện nhẹ |
| `L10-617`, `L10-617b` | tách: ví dụ cắt mất mát giá trị có công thức và $\epsilon$; bảng và kết luận của Engstrom và cộng sự | E6, E9 |
| `L10-618` | $V(\theta)$, $s_0$, $\theta_{n,1}$, $\varphi_n$ nêu trên mặt trang; giả thiết quyết định; kết luận dạng $\liminf\le C\sqrt{\lvert\mathcal A\rvert}\limsup\varphi_n$ | E3, E4 |
| `L10-700` | từ khóa "Vấn đề trung tâm" | phát hiện nhẹ |
| `L10-702b` | tập gradient bằng $0$; điều kiện cùng miền hỗ trợ | phát hiện nhẹ, E9 |
| `L10-703` | dòng kết mở bằng khẳng định | phát hiện nhẹ |
| `L10-704` | hàng Jin, Li và Wang: giả thiết quyết định và dạng cận | E4 |
| `L10-707` | đánh số 2–6 như `L10-109`; dòng 4 nêu điều kiện | E10 |
| `L10-708` | câu 1–3 viết lại (ngữ pháp; 57 âm tiết) | phát hiện nhẹ |
| `L10-710` | "Tài liệu đọc:" có mục; dòng nối Bài 11 có SPO, SAM+PPO | E10, phát hiện nhẹ |

Ghi chú diễn giả sửa theo E9, E10, E11 ở các trang: `L10-101`, `102`, `103`, `104`, `105`, `108`, `109`, `110`, `200`, `201`, `206`, `207`, `208`, `210`, `211`, `212`, `212b`, `215`, `216`, `300`, `302`, `303`, `305`, `306`, `307`, `308`, `309`, `402`, `403`, `404`, `406`, `408`, `412`, `412b`, `414`, `502`, `502b`, `503`, `504`, `505`, `506`, `507`, `508`, `509`, `510`, `600`, `601`, `602`, `603`, `606`, `609`, `611`, `611b`, `613`, `614`, `615`, `616`, `617`, `617b`, `618`, `619`, `620`, `700`, `701`, `702`, `702b`, `703`, `704`, `707`, `709`, `710`.

**Số đo cuối (Playwright, 1600×900).** Âm tiết: token có chữ hoặc số, không tính tiêu đề, KaTeX, ô số, hình, ghi chú; tính cả hàng tiêu đề bảng. Dòng: mỗi `p`, `li`, hàng thân bảng, công thức hiển thị (hàng tiêu đề bảng không tính). Đáy tính trong khung 1280×720. Âm tiết ghi chú không tính `note-source` và KaTeX.

| trang | âm tiết | dòng | âm tiết lớn nhất mỗi dòng | công thức hiển thị | đáy (px) | âm tiết ghi chú |
|---|---:|---:|---:|---:|---:|---:|
| `L10-101` | 66 | 2 | 28 | 0 | 609 | 126 |
| `L10-102` | 59 | 6 | 12 | 0 | 632 | 89 |
| `L10-103` | 38 | 6 | 12 | 0 | 615 | 102 |
| `L10-104` | 80 | 5 | 20 | 0 | 520 | 86 |
| `L10-105` | 60 | 8 | 14 | 0 | 604 | 88 |
| `L10-106` | 34 | 5 | 15 | 1 | 657 | 62 |
| `L10-107` | 21 | 5 | 13 | 0 | 654 | 76 |
| `L10-108` | 24 | 5 | 13 | 0 | 536 | 101 |
| `L10-109` | 79 | 5 | 14 | 0 | 517 | 145 |
| `L10-110` | 27 | 3 | 10 | 0 | 639 | 69 |
| `L10-200` | 37 | 2 | 24 | 0 | 442 | 92 |
| `L10-201` | 50 | 4 | 16 | 0 | 361 | 99 |
| `L10-202` | 17 | 4 | 13 | 1 | 523 | 71 |
| `L10-203` | 34 | 3 | 18 | 1 | 487 | 57 |
| `L10-204` | 34 | 4 | 19 | 1 | 446 | 78 |
| `L10-205` | 24 | 4 | 9 | 1 | 433 | 121 |
| `L10-206` | 36 | 5 | 17 | 0 | 528 | 83 |
| `L10-207` | 58 | 6 | 16 | 1 | 632 | 69 |
| `L10-208` | 32 | 4 | 15 | 1 | 559 | 60 |
| `L10-209` | 24 | 6 | 10 | 0 | 521 | 89 |
| `L10-210` | 46 | 5 | 14 | 0 | 440 | 72 |
| `L10-211` | 24 | 5 | 12 | 0 | 635 | 59 |
| `L10-212` | 59 | 4 | 17 | 0 | 508 | 113 |
| `L10-212b` | 21 | 2 | 14 | 0 | 612 | 77 |
| `L10-213` | 55 | 6 | 16 | 1 | 634 | 70 |
| `L10-214` | 23 | 4 | 12 | 0 | 522 | 53 |
| `L10-215` | 19 | 6 | 17 | 0 | 526 | 92 |
| `L10-216` | 35 | 6 | 13 | 0 | 559 | 94 |
| `L10-300` | 40 | 2 | 25 | 0 | 321 | 78 |
| `L10-301` | 34 | 5 | 12 | 0 | 668 | 75 |
| `L10-302` | 37 | 5 | 14 | 1 | 564 | 67 |
| `L10-303` | 42 | 5 | 14 | 0 | 679 | 78 |
| `L10-304` | 32 | 5 | 17 | 1 | 595 | 78 |
| `L10-305` | 40 | 6 | 16 | 0 | 646 | 51 |
| `L10-306` | 50 | 6 | 20 | 1 | 636 | 116 |
| `L10-307` | 40 | 5 | 17 | 0 | 483 | 58 |
| `L10-308` | 37 | 6 | 16 | 0 | 551 | 115 |
| `L10-309` | 28 | 6 | 19 | 0 | 582 | 83 |
| `L10-400` | 38 | 2 | 23 | 0 | 321 | 96 |
| `L10-401` | 35 | 3 | 15 | 0 | 652 | 72 |
| `L10-402` | 36 | 6 | 18 | 0 | 618 | 42 |
| `L10-403` | 26 | 5 | 12 | 1 | 580 | 61 |
| `L10-404` | 26 | 5 | 13 | 1 | 569 | 113 |
| `L10-405` | 49 | 5 | 18 | 1 | 646 | 59 |
| `L10-406` | 42 | 5 | 18 | 1 | 559 | 89 |
| `L10-407` | 39 | 6 | 15 | 0 | 605 | 70 |
| `L10-408` | 53 | 6 | 17 | 1 | 647 | 102 |
| `L10-409` | 29 | 4 | 18 | 1 | 632 | 82 |
| `L10-410` | 26 | 4 | 13 | 0 | 510 | 40 |
| `L10-411` | 35 | 5 | 13 | 1 | 519 | 81 |
| `L10-412` | 47 | 4 | 17 | 1 | 509 | 75 |
| `L10-412b` | 37 | 5 | 13 | 1 | 562 | 91 |
| `L10-413` | 44 | 6 | 15 | 0 | 619 | 69 |
| `L10-414` | 28 | 6 | 12 | 0 | 621 | 48 |
| `L10-500` | 35 | 2 | 23 | 0 | 321 | 97 |
| `L10-501` | 36 | 5 | 11 | 0 | 485 | 72 |
| `L10-502` | 47 | 4 | 18 | 0 | 412 | 47 |
| `L10-502b` | 28 | 4 | 10 | 1 | 392 | 61 |
| `L10-503` | 60 | 6 | 17 | 1 | 651 | 79 |
| `L10-504` | 20 | 5 | 10 | 1 | 663 | 68 |
| `L10-505` | 13 | 6 | 10 | 0 | 650 | 94 |
| `L10-506` | 14 | 6 | 8 | 0 | 587 | 85 |
| `L10-507` | 60 | 6 | 18 | 0 | 625 | 134 |
| `L10-508` | 60 | 6 | 12 | 0 | 471 | 60 |
| `L10-509` | 21 | 6 | 10 | 1 | 618 | 81 |
| `L10-510` | 19 | 6 | 16 | 0 | 600 | 73 |
| `L10-600` | 40 | 2 | 24 | 0 | 321 | 97 |
| `L10-601` | 60 | 5 | 17 | 0 | 425 | 101 |
| `L10-602` | 16 | 4 | 9 | 1 | 655 | 70 |
| `L10-603` | 21 | 4 | 12 | 2 | 455 | 81 |
| `L10-604` | 38 | 6 | 14 | 1 | 585 | 91 |
| `L10-605` | 31 | 6 | 17 | 0 | 575 | 71 |
| `L10-606` | 55 | 5 | 15 | 0 | 422 | 107 |
| `L10-607` | 55 | 5 | 20 | 0 | 569 | 89 |
| `L10-608` | 52 | 6 | 15 | 1 | 628 | 98 |
| `L10-609` | 53 | 6 | 14 | 1 | 627 | 118 |
| `L10-610` | 21 | 6 | 5 | 0 | 649 | 64 |
| `L10-611` | 56 | 5 | 16 | 0 | 547 | 92 |
| `L10-611b` | 36 | 4 | 14 | 1 | 431 | 85 |
| `L10-612` | 32 | 3 | 13 | 0 | 639 | 93 |
| `L10-613` | 58 | 6 | 16 | 0 | 583 | 135 |
| `L10-614` | 50 | 6 | 18 | 0 | 628 | 106 |
| `L10-615` | 26 | 6 | 9 | 0 | 522 | 120 |
| `L10-616` | 69 | 4 | 20 | 0 | 561 | 93 |
| `L10-617` | 52 | 6 | 18 | 1 | 571 | 129 |
| `L10-617b` | 60 | 4 | 20 | 0 | 434 | 118 |
| `L10-618` | 60 | 6 | 14 | 1 | 557 | 137 |
| `L10-619` | 29 | 6 | 18 | 0 | 581 | 82 |
| `L10-620` | 16 | 6 | 5 | 0 | 536 | 96 |
| `L10-700` | 30 | 2 | 16 | 0 | 321 | 92 |
| `L10-701` | 57 | 6 | 11 | 0 | 612 | 108 |
| `L10-702` | 46 | 5 | 10 | 0 | 626 | 104 |
| `L10-702b` | 42 | 4 | 15 | 0 | 523 | 105 |
| `L10-703` | 58 | 5 | 16 | 0 | 660 | 102 |
| `L10-704` | 52 | 3 | 19 | 0 | 663 | 127 |
| `L10-705` | 50 | 5 | 19 | 0 | 425 | 72 |
| `L10-706` | 37 | 5 | 18 | 0 | 476 | 163 |
| `L10-707` | 80 | 6 | 18 | 0 | 567 | 105 |
| `L10-708` | 57 | 5 | 14 | 0 | 522 | 122 |
| `L10-709` | 37 | 6 | 9 | 0 | 557 | 133 |
| `L10-710` | 60 | 5 | 16 | 0 | 435 | 135 |

Cờ còn lại: `L10-101` (trang bìa, dòng phụ đề 28 token, không tính như Bài 09); `L10-105` (8 dòng, ngoại lệ đã duyệt). Trang tiêu đề mạch: dòng dẫn tính theo trần 25.

---

## Bổ sung DPO (2026-11-19)

Giai đoạn III.1 của lượt bổ sung DPO (`prompt-bo-sung-dpo-bai-10.md`, bảng Q, tác giả 2026-11-19 "Accept all proposals"; kế hoạch `ke-hoach-bo-sung-dpo.md` phần C). Phần này thêm mạch 7 mới vào deck đã có và ghi mọi trang cũ phải sửa; các phần ở trên giữ nguyên làm hồ sơ của bản 101 trang. Chỗ phần này khác phần trên thì phần này thắng cho deck sau bổ sung.

- **Nguồn nội dung** (Q1, "P1, Bài 10, Mục 7 (riêng)" ở mục 3 `NGUYEN-TAC-HOC-PHAN.md`; NT1, NT2): ghi chú đã duyệt và commit, `materials/lec-10/lecture-note.md` §7 (7.1–7.6, khối 10.52–10.70, Ví dụ 10.23–10.28, `lec-10-topic-25` … `-30`), Tình huống 10.4–10.5, §8, Tóm tắt chương, Bài tập 10.18–10.21; `exercises.md` Bài tập 10.22. Thuật ngữ, ký hiệu, giả thiết, số liệu trên mặt trang lấy đúng từ đó; mọi số trong mục dưới đã đối chiếu với dòng của ghi chú. Bài báo chỉ xuất hiện trong dòng nguồn của ghi chú diễn giả, đúng như ghi chú dẫn.
- **Quy định áp dụng.** Trang mới (`L10-D00` … `L10-D18`, `L10-104b`, `L10-702c`, `L10-703b`) theo NT1–NT28, P1–P11, NT-RL-1 … NT-RL-11. Trang cũ giữ quy định cũ (mục 3 `NGUYEN-TAC-HOC-PHAN.md`), trừ các trang liệt kê ở mục "Trang đã có phải sửa"; trên trang đã sửa, phần bị sửa theo NT1–NT28, và trang phải sạch `deck_lint.py` ngoài các ngoại lệ ghi ở mục "Ngoại lệ mật độ và ngoại lệ đã biết của `deck_lint`".
- **Luận điểm trọng tâm** (tác giả; phải thấy trên trang kết quả `L10-D04`, trang so sánh `L10-D16` và mạch "Tổng kết" `L10-702c`, `L10-707`, `L10-708`): RLHF với PPO và DPO xuất phát từ cùng một mục tiêu, cực đại hóa phần thưởng trong khi giữ chính sách gần một chính sách tham chiếu cố định bằng phạt KL, với nghiệm dạng đóng $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57). PPO nhắm tới nghiệm đó bằng mẫu sinh trực tuyến, không có bảo đảm hội tụ. DPO giải cùng bài toán mà không dùng PPO hay vòng học tăng cường trực tuyến nào; cực tiểu của $L^{\mathrm{DPO}}$ là nghiệm của con đường RLHF lý tưởng chỉ dưới (H1)–(H3), (H4a), (H4b) của Định lý 10.65. Hai mỏ neo khác nhau ($\pi_{\mathrm{old}}$ đổi sau mỗi vòng, $\pi_{\mathrm{ref}}$ cố định) và hai chiều KL khác nhau ($D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$ ở Định nghĩa 10.43, $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ ở Định nghĩa 10.56).
- **Âm tiết** như quy ước ở đầu tệp (token theo khoảng trắng, không tính tiêu đề, KaTeX, số trong ô bảng, nhãn hình, ghi chú diễn giả; số viết trong câu có tính); số trong phần này đếm bằng script trên các dòng trong ngoặc kép “…” của mục "Mặt trang" (cùng quy tắc với `deck_lint.py`: chữ trong ô bảng có tính), là số dự kiến; tác tử viết đếm lại trên HTML bằng `deck_lint.py` (NT17).
- **Bước của hành trình khái niệm** (NT8) ghi bằng các chữ: vấn đề, trực quan, ví dụ, phát biểu, ý tưởng chứng minh, ứng dụng, kiểm tra.

### Bản đồ mạch sau bổ sung

**Bài toán trung tâm** (§1.1 của ghi chú, ba phần): giảm phương sai của ước lượng gradient mà vẫn giữ kỳ vọng của nó; dùng lại dữ liệu của $\pi_{\mathrm{old}}$ để chọn một bước cập nhật lớn mà chính sách mới không kém chính sách cũ; khi phần thưởng chỉ được biết qua các phép so sánh ưu tiên, tìm chính sách cực đại hóa phần thưởng mà vẫn ở gần một chính sách tham chiếu cố định.

| mạch | loại | câu hỏi của mạch (NT13) | chức năng | đầu vào | đầu ra | đóng góp cho bài toán trung tâm | trang tiêu đề mạch | trang | phút |
|---|---|---|---|---|---|---|---|---:|---:|
| 1–6 | như bảng "Bản đồ mạch" ở trên | như trên | như trên | như trên | như trên (mạch 6 giao Thuật toán 10.49 cho mạch 7) | phần thứ nhất và thứ hai | như trên | 90 (mạch 1 thêm `L10-104b`) | 104 |
| 7. Tối ưu chính sách từ phản hồi ưu tiên | khái niệm, kết quả, thuật toán | Khi chỉ có các phép so sánh ưu tiên, chính sách mới nên chọn mỗi câu trả lời với xác suất nào nếu vẫn phải gần chính sách tham chiếu, và có cần một vòng học tăng cường để tìm chính sách đó không? (câu hỏi của §7.1) | Mô hình Bradley–Terry cho mô hình phần thưởng; mục tiêu có phạt KL theo chính sách tham chiếu và nghiệm dạng đóng; RLHF với PPO; phép đổi biến và DPO; định lý tương đương; so sánh hai con đường; giới hạn khi giả thiết hỏng | Thuật toán 10.49 (PPO kiểu actor–critic, cần $R_{t+1}$ của môi trường); phạt KL theo $\pi_{\mathrm{old}}$ của Định nghĩa 10.43 (chỉ giới hạn từng bước); KL và Mệnh đề 10.24 (mạch 4); hàm điểm softmax, bài toán một bước của Ví dụ 10.1 và bộ đệm $y_1,y_1,y_2$ của Ví dụ 10.17 | Định lý 10.57 ($\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$), Định lý 10.65 (tương đương dưới (H1)–(H3), (H4a), (H4b)); Thuật toán 10.61, 10.67; bảng so sánh RLHF với PPO và DPO; phản ví dụ ưu tiên tất định; năm hàng của bảng tổng kết, hai hàng của bảng phương pháp, một hàng của bảng kết luận có bảo đảm | Phần thứ ba: cùng công cụ phạt KL của mạch 4–6 với một mỏ neo cố định, quyết định nghiệm cuối; trả lời có điều kiện ở phần 6 của §8.3 | `L10-D00`, `id="mach-7"`, `data-note-topic-id="lec-10-topic-25"` | 19 | 22 |
| 8. Tổng kết | kết bài | Mỗi kết quả của bài đúng dưới giả thiết nào, và bài toán trung tâm được trả lời đến đâu? | Bảng kết quả–giả thiết (thêm `L10-702c`), bảng phương pháp (sáu phương pháp, thêm `L10-703b`), bảng kết luận có bảo đảm (thêm hàng DPO), bài tổng hợp, vấn đề trung tâm (sáu phần), câu hỏi tự kiểm tra, bài tập về nhà, tài liệu tham khảo | Kết quả mạch 2–7 | Câu trả lời có điều kiện cho cả ba phần; giới hạn còn lại (§8.6) chỉ trong ghi chú diễn giả, không trỏ bài sau (Q8) | Tổng hợp, không khái niệm mới | `L10-700`, `id="mach-8"` (đổi từ `mach-7`), `data-note-topic-id="lec-10-topic-23"` | 14 | 9 |
| **Tổng** | | | | | | | | **123** | **135** |

**Tám mạch.** NT10 và `AGENTS.md` cho 5–7 mạch. Deck có tám mạch theo yêu cầu cụ thể của tác giả (Q7, QT1; "P1, Bài 10, Mục 7 (riêng)"): Mục 7 mới của ghi chú là một chủ đề trọn vẹn với câu hỏi, hai định lý và hai thuật toán riêng, và số mạch $N$ phải trùng số mục $N$ của ghi chú với $N=2,\dots,8$ (GC16). Ảnh hưởng tới mạch bài: phương án gộp DPO vào mạch 6 cho một mạch 42 trang và tách một mục của ghi chú khỏi mạch của nó, nên bị loại (kế hoạch QT1). "Tổng kết" thành mạch 8 (`#/8`), mạch 7 mới mở tại `#/7`; liên kết `#/7/1`, `#/8/1` của `exercises.md` (đã có) mở đúng `L10-D00` và `L10-700`. `deck_lint.py` báo `STRUCT 8 mạch (cần 5–7)`: ngoại lệ đã biết. Điều phối viên ghi cùng lý do vào `review-log.md`.

**Mã trang của mạch 7** (Q7, QT2, P7): tiền tố `L10-D`, trang tiêu đề mạch `L10-D00`, các trang `L10-D01` … `L10-D18`; không dùng `L10-8xx` vì "Tổng kết" giữ `L10-7xx`; mọi `data-slide-id` cũ giữ nguyên. Trang tách mới của phần cũ theo khuôn hậu tố chữ đã có: `L10-104b`, `L10-702c`, `L10-703b`.

**Dòng dẫn và từ khóa của hai trang tiêu đề mạch** (NT12; không khuôn "Muốn …, phải …", không mở bằng "Người học", khác khuôn câu của nhau):

- `L10-D00`: “Từ phép so sánh ưu tiên, PPO với mẫu trực tuyến và DPO trên dữ liệu cố định nhắm tới cùng một chính sách.” Từ khóa: “Mô hình Bradley–Terry · Mục tiêu có phạt KL · RLHF với PPO · DPO · Hai mỏ neo”.
- `L10-700`: “Mỗi kết quả của bài đúng dưới một bộ giả thiết riêng.” Từ khóa: “Kết quả và giả thiết · Sáu phương pháp · Vấn đề trung tâm · Câu hỏi tự kiểm tra”.

Lý do đổi bản nháp của kế hoạch C1 ("Cùng một mục tiêu có phạt KL được giải bằng PPO …"): "mục tiêu có phạt KL" là khái niệm chưa có ở điểm vào mạch (định nghĩa ở `L10-D03`), trong khi NT12 chỉ cho dùng từ thông thường và khái niệm đã có; "nhắm tới" giữ đúng mức của luận điểm (PPO không có bảo đảm hội tụ, DPO chỉ trùng nghiệm dưới giả thiết). Dòng dẫn của `L10-700` lấy câu mở §8 của ghi chú.

### Danh sách trang và thời lượng của mạch 7

| mã | tiêu đề | loại, bước NT8 | khối ghi chú | `data-note-topic-id` | hình | phút |
|---|---|---|---|---|---|---:|
| `L10-D00` | 7. Tối ưu chính sách từ phản hồi ưu tiên | tiêu đề mạch | §7 | `lec-10-topic-25` | — | 0,5 |
| `L10-D01` | Phần thưởng từ so sánh ưu tiên | vấn đề (NT-RL-3, NT13), ví dụ dẫn nhập | §7.1 đoạn mở, Câu hỏi, Định nghĩa 10.52(a), Ví dụ 10.23 | `lec-10-topic-25` | — | 1 |
| `L10-D02` | Mô hình Bradley–Terry | trực quan, phát biểu (định nghĩa, kết quả phụ), ví dụ | Định nghĩa 10.53, Mệnh đề 10.54, Ví dụ 10.24 | `lec-10-topic-25` | — | 1,5 |
| `L10-D03` | Mục tiêu có phạt KL | vấn đề, trực quan, ví dụ, phát biểu (định nghĩa) | §7.2 đoạn mở, Ví dụ 10.25, Định nghĩa 10.56 | `lec-10-topic-26` | — | 1 |
| `L10-D04` | Nghiệm của mục tiêu có phạt KL | phát biểu (kết quả chính; luận điểm, phần 1) | Định lý 10.57 | `lec-10-topic-26` | — | 1,5 |
| `L10-D05` | Ý tưởng chứng minh: nghiệm của mục tiêu có phạt KL | ý tưởng chứng minh (NT6) | chứng minh Định lý 10.57 | `lec-10-topic-26` | — | 1,5 |
| `L10-D06` | Ví dụ: nghiệm có phạt KL trên bài toán một bước | ứng dụng | Ví dụ 10.26 | `lec-10-topic-26` | — | 1 |
| `L10-D07` | Phần thưởng đã trừ KL theo token | vấn đề (NT-RL-3), phát biểu (kết quả phụ) | §7.3 đoạn mở, Định nghĩa 10.52(b), Bổ đề 10.59, Mệnh đề 10.60, (7.1) | `lec-10-topic-27` | — | 1 |
| `L10-D08` | Ví dụ: hai vòng PPO trên phần thưởng đã trừ KL | ví dụ tính tay trước giả mã (NT-RL-2); hai mỏ neo (NT-RL-4) | Ví dụ 10.27, Nhận xét 10.58 | `lec-10-topic-27` | — | 1,5 |
| `L10-D09` | Thuật toán RLHF với PPO | phát biểu (thuật toán) | Thuật toán 10.61, Nhận xét 10.62 (ghi chú diễn giả) | `lec-10-topic-27` | — | 1 |
| `L10-D10` | Đổi biến giữa phần thưởng và chính sách | vấn đề (NT-RL-3), ví dụ, trực quan, phát biểu (kết quả phụ) | §7.4 đoạn mở, Mệnh đề 10.63 | `lec-10-topic-28` | — | 1 |
| `L10-D11` | Hàm mất mát DPO | phát biểu (định nghĩa) | Định nghĩa 10.64 và đoạn sau | `lec-10-topic-28` | — | 1 |
| `L10-D12` | Tương đương giữa RLHF và DPO | phát biểu (kết quả chính; luận điểm, phần 2) | Định lý 10.65 | `lec-10-topic-28` | — | 1,5 |
| `L10-D13` | Ý tưởng chứng minh: tương đương giữa RLHF và DPO | ý tưởng chứng minh (NT6), kiểm tra (bỏ (H4b)) | chứng minh Định lý 10.65, đoạn "Mỗi giả thiết có vai trò riêng" | `lec-10-topic-28` | — | 1 |
| `L10-D14` | Ví dụ: một bước DPO tính tay | phát biểu (kết quả phụ), ví dụ tính tay trước giả mã (NT-RL-2) | Mệnh đề 10.66, Ví dụ 10.28 | `lec-10-topic-28` | — | 1,5 |
| `L10-D15` | Thuật toán DPO | phát biểu (thuật toán); ngoại tuyến, khác chính sách (NT-RL-4) | Thuật toán 10.67, "Trong thực hành" của §7.4 | `lec-10-topic-28` | — | 1 |
| `L10-D16` | So sánh PPO trong RLHF và DPO | ứng dụng, bảng so sánh (luận điểm, phần 3) | §7.5, bảng so sánh; Nhận xét 10.70 (đọc thêm, chỉ ghi chú diễn giả) | `lec-10-topic-29` | — (hình hai con đường chỉ ở ghi chú, Q7) | 1,5 |
| `L10-D17` | Ưu tiên tất định từ ít dữ liệu | ứng dụng khi giả thiết hỏng, phản ví dụ | Tình huống 10.5, Nhận xét 10.69 | `lec-10-topic-29` | — | 1 |
| `L10-D18` | Bài tập: nghiệm có phạt KL trên ba câu trả lời | kiểm tra (đề và "Lời giải:" bằng fragment) | Bài tập 10.18 (a)–(b) | `lec-10-topic-26` | — | 1 |

Phút mạch 7: $0{,}5+1+1{,}5+1+1{,}5+1{,}5+1+1+1{,}5+1+1+1+1{,}5+1+1{,}5+1+1{,}5+1+1=22$, đúng kế hoạch C2. `topic-30` (đọc thêm) không mang thuộc tính trang nào, chỉ có trong ghi chú diễn giả `L10-D16`, `L10-D17` (NT5: nói rõ là đọc thêm). Không hình mới: hình `rlhf-dpo-hai-con-duong.svg` ở lại ghi chú (Q7, QT7), hình tùy chọn `muc-tieu-phat-kl.svg` không được vẽ ở giai đoạn I nên không dùng; tác tử viết chỉ được thêm `-slide.svg` (prompt III.3).

**Sai khác so với danh sách C2 của kế hoạch** (vẫn 19 trang, cùng mã `L10-D00` … `L10-D18`, cùng 22 phút; điều phối viên duyệt ở cổng storyboard):

1. C2 đặt Thuật toán 10.61 trên `L10-D08` trước ví dụ tính tay `L10-D09`, trái NT-RL-2 (bước tính tay trước giả mã) và trái thứ tự của ghi chú (Bổ đề 10.59, Mệnh đề 10.60, (7.1), Ví dụ 10.27, Thuật toán 10.61; NT2). Storyboard tách: `L10-D07` phát biểu phần thưởng đã trừ KL theo token, `L10-D08` ví dụ tính tay, `L10-D09` thuật toán.
2. C2 không có trang ý tưởng chứng minh cho Định lý 10.65, trong khi định lý mang phần 2 của luận điểm và là kết quả chính (NT6: mỗi kết quả chính có trang ý tưởng chứng minh riêng). Thêm `L10-D13`.
3. Để giữ 19 trang (Q7): ví dụ khớp mô hình phần thưởng (C2 `L10-D03`, Ví dụ 10.24, ba con số) thành dòng cuối của `L10-D02`; đề và lời giải Bài tập 10.18 (C2 `L10-D17`, `L10-D18`) thành một trang, "Lời giải:" hiện bằng fragment (NT24 cho phép fragment hoặc trang kế tiếp). Cụm Bradley–Terry là chủ đề `cầu nối` (`outline.md`, "Phân loại chủ đề"), dựa trên hồi quy logistic người học đã biết (GC-RL-16), nên gộp ở đây ít tốn nhất.
4. Mệnh đề 10.66 (gradient của $L^{\mathrm{DPO}}$) đặt trên trang ví dụ tính tay `L10-D14`, không trên trang định nghĩa như C2 `L10-D11`: theo ghi chú, Mệnh đề 10.66 đứng sau Định lý 10.65 và ngay trước Ví dụ 10.28 (NT2).
5. Số hiệu bài tập theo Q4: bài trên mặt trang là Bài tập 10.18 của ghi chú (C2 ghi 10.13). Tiêu đề `L10-D17` là "Ưu tiên tất định từ ít dữ liệu" (tên của Tình huống 10.5), không "Giới hạn: …": NT16 chỉ cho các tiền tố chức năng "Ví dụ:", "Bài tập:", "Chứng minh:", "Ý tưởng chứng minh:".
6. Nhận xét 10.58 (hai mỏ neo, hai chiều KL; cuối §7.2 của ghi chú) lên `L10-D08`, trang ví dụ hai vòng PPO của §7.3: đổi chỗ cục bộ trong cùng mạch, nội dung giữ (NT2), vì ví dụ đó làm cụ thể hai mỏ neo.
7. Bảng so sánh ở `L10-D16`, không ở `L10-D15` như Q7 ghi: Q7 chốt hình thức (bảng trên mặt trang, hình ở ghi chú); mã dịch một bậc do sai khác 2; không liên kết nào trỏ mã này.

Điều phối viên chấp nhận các sai khác 1–7 ở cổng III.2. Phương án "chỉ một hộp Câu hỏi:" cho `L10-109` của bản trước bị bác (Q3: giữ cấu trúc, thêm một dòng); mục `L10-109` đã viết lại.

### Thời lượng của cả deck (135 phút; Q7, kế hoạch C4; chỉ trong planning, NT27)

| mạch | trang | số trang | phút trước | phút sau | trang đổi phút |
|---|---|---:|---:|---:|---|
| 1 | `L10-101`–`L10-110`, `L10-104b` | 11 | 12 | 12 | `L10-104` 1 → 0,5; `L10-104b` 0,5 |
| 2 | `L10-200`–`L10-216` | 18 | 23 | 22,5 | `L10-205` 1,5 → 1 |
| 3 | `L10-300`–`L10-309` | 10 | 14,5 | 14,5 | — |
| 4 | `L10-400`–`L10-414` | 16 | 22,5 | 20,5 | `L10-404` 1,5 → 1; `L10-409` 1,5 → 1; `L10-414` 1 → 0 |
| 5 | `L10-500`–`L10-510` | 12 | 13,5 | 12 | `L10-505` 2 → 1,5; `L10-510` 1 → 0 |
| 6 | `L10-600`–`L10-620` | 23 | 25,5 | 22,5 | `L10-614`, `L10-615`, `L10-617`, `L10-618` 1 → 0,5 mỗi trang; `L10-617b` 0,5; `L10-620` 1 → 0 |
| 7 (mới) | `L10-D00`–`L10-D18` | 19 | — | 22 | bảng trên |
| 8 | `L10-700`–`L10-710`, `L10-702c`, `L10-703b` | 14 | 9 | 9 | `L10-706` 1 → 0; `L10-702c` 0,5; `L10-703b` 0,5 |
| **Tổng** | | **123** | **120** | **135** | |

Kiểm: $12+22{,}5+14{,}5+20{,}5+12+22{,}5+22+9=135$; $11+18+10+16+12+23+19+14=123$. Trang có 0 phút (`L10-414`, `L10-510`, `L10-620`, `L10-706`) là trang lời giải, giữ nguyên trong deck và dùng trong 15 phút chữa bài (Q7: deck 135 phút, chữa bài 15 phút); mạch 4–6 giảm $2+1{,}5+3=6{,}5$ phút, mạch 2 giảm $0{,}5$, mạch 8 giảm $1$ ở `L10-706` và tăng $1$ ở hai trang bảng mới, tổng giảm $8$ phút như C4 ($143-8=135$). Phút mạch 8: `L10-700` 0,5; `L10-701` 1; `L10-702` 0,5; `L10-702b` 0,5; `L10-702c` 0,5; `L10-703` 1; `L10-703b` 0,5; `L10-704` 0,5; `L10-705` 1,5; `L10-706` 0; `L10-707` 1; `L10-708` 0,5; `L10-709` 0,5; `L10-710` 0,5; tổng 9. Không trang cũ nào bị bỏ (mục 3 `NGUYEN-TAC-HOC-PHAN.md`, "Số trang ở đợt sửa"). Số trang 123 vượt mặc định P6 vì deck đã có giữ số trang; con số nằm trong khoảng 120–123 của C4.

### Mục từng trang, mạch 7. Tối ưu chính sách từ phản hồi ưu tiên (22 phút)

Các ngoặc dẫn số quy định (NTk, Pk, NT-RL-k) trong bản phác ghi chú diễn giả dưới đây là chú thích cho tác tử viết, không chép vào HTML (VP8, NT22); tác tử viết kiểm bằng grep "NT[0-9-]" trên các khối `aside.notes`. Mỗi mục ghi như phần trên (vị trí và loại; lý do tồn tại; liên kết; mục tiêu học tập theo số của ghi chú, 8 và 9 là hai mục tiêu mới, trên deck là dòng 7–12 của `L10-104b`; khối ghi chú; mặt trang; mật độ; phút; quyết định; ý chính của ghi chú diễn giả). Mặt trang ghi từng dòng trong “…”; công thức hiển thị ghi riêng. Mọi câu đã soát `no-ai-slop` chế độ Edit (mục "Câu chữ dự kiến" của phần này). Mỗi ghi chú diễn giả 40–150 âm tiết (đến khoảng 250 cho ý tưởng chứng minh và bài tập), mở bằng đối tượng toán học hoặc kết quả kế thừa, kết bằng `<p class="note-source"><strong>Nguồn:</strong> ghi chú bài giảng Bài 10, §7.k (khối); <bài báo mà ghi chú dẫn cho khối đó>.</p>` (NT22).

#### `L10-D00` 7. Tối ưu chính sách từ phản hồi ưu tiên (trang tiêu đề mạch), điểm vào mạch 7
- **Vị trí, loại:** điểm vào mạch 7; `section.strand-title`, `id="mach-7"`, `data-note-topic-id="lec-10-topic-25"`; ngoài hành trình khái niệm.
- **Lý do tồn tại:** mở phần thứ ba của bài toán trung tâm; nêu điều người học làm được sau mạch.
- **Liên kết:** trước: `L10-620` (lời giải bài tập PPO, dùng phần thưởng của môi trường); sau: `L10-D01`. Kế thừa Thuật toán 10.49 và phạt KL theo $\pi_{\mathrm{old}}$; giao cho "Tổng kết" hai định lý, hai thuật toán, bảng so sánh.
- **Mục tiêu:** 8, 9.
- **Mặt trang:** `span.strand-number` “7.” + `h2` “Tối ưu chính sách từ phản hồi ưu tiên” (khác tiêu đề `L10-D01`); `p.strand-lead` “Từ phép so sánh ưu tiên, PPO với mẫu trực tuyến và DPO trên dữ liệu cố định nhắm tới cùng một chính sách.”; `p.strand-keys` “Mô hình Bradley–Terry · Mục tiêu có phạt KL · RLHF với PPO · DPO · Hai mỏ neo”.
- **Mật độ:** dòng dẫn 24 âm tiết (trần 25, đếm bằng script); 5 cụm từ khóa.
- **Phút:** 0,5. **Quyết định:** thêm (Q7).
- **Ghi chú diễn giả (40–100):** Thuật toán PPO của phần 6 cần phần thưởng do môi trường trả về sau mỗi hành động, còn phạt KL của PPO-Penalty chỉ giữ mỗi bước gần chính sách vừa sinh dữ liệu. Ở đây phần thưởng chỉ được biết qua so sánh của người gán nhãn; một mục tiêu có phạt KL theo chính sách tham chiếu cố định quyết định nghiệm cuối, và RLHF với PPO cùng DPO nhắm tới nghiệm đó. Kết quả trao cho phần tổng kết: hai định lý, hai thuật toán, một bảng so sánh. Nguồn: §7.

#### `L10-D01` Phần thưởng từ so sánh ưu tiên
- **Vị trí, loại:** trang nội dung đầu của mạch 7; bước vấn đề của cụm Bradley–Terry và của cả mạch; ví dụ dẫn nhập (dữ liệu của Ví dụ 10.23, dùng lại ở `L10-D02`, `L10-D03`, `L10-D06`, `L10-D08`, `L10-D14`).
- **Lý do tồn tại:** NT-RL-3 (mở bằng giới hạn cụ thể của phương pháp trước trong một dòng), NT13 (câu nối giữa hai mạch và câu hỏi của mạch trên mặt trang nội dung đầu tiên), NT14 (liệt kê dữ kiện ngay), NT-RL-4 (trạng thái, hành động, kết thúc trước khi dùng: Định nghĩa 10.52(a)).
- **Liên kết:** trước: `L10-D00`; sau: `L10-D02` (mô hình cho xác suất của từng phép so sánh).
- **Mục tiêu:** 8.
- **Khối ghi chú:** §7.1 đoạn mở và "**Câu hỏi.**", Định nghĩa 10.52(a), Ví dụ 10.23 (`topic-25`).
- **Mặt trang:**
  1. “PPO cần phần thưởng $R_{t+1}$ của môi trường; ở đây chỉ có so sánh.”
  2. “Một bước: trạng thái là lời nhắc (prompt) $x$, hành động là câu trả lời (response, completion) $y\in\mathcal Y(x)$.”
  3. “Chính sách tham chiếu $\pi_{\mathrm{ref}}(\cdot\mid x)=(\tfrac23;\,\tfrac13)$.”
  4. bảng hai cột: “bộ ba $(x,y_w,y_l)\in\mathcal D_{\mathrm{pref}}$ (lời nhắc, được chọn, bị loại)” | “số lần”; hàng $(x,y_1,y_2)$ | $4$; hàng $(x,y_2,y_1)$ | $2$.
  5. hộp: “**Câu hỏi:** nếu phải gần $\pi_{\mathrm{ref}}$, chính sách chọn $y_1$, $y_2$ với xác suất nào?<br>Có cần vòng học tăng cường không?”
- **Mật độ:** khoảng 62 âm tiết (dòng 13, 16, 4, bảng 10, hộp 19), 5 dòng, 1 hộp 2 câu, 0 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT9 (tập $\mathcal Y(x)$ dùng trong giả thiết của `L10-D04`, `L10-D12` phải có tên trước) và NT21 (tên tiếng Anh của câu trả lời ở lần đầu). "Một bước" là bài toán một bước của Ví dụ 10.1 (lượt dừng sau một hành động); $y_w$, $y_l$, $\mathcal D_{\mathrm{pref}}$ có tên ở đầu cột bảng, định nghĩa đầy đủ ở `L10-D02`.
- **Phút:** 1. **Quyết định:** thêm.
- **Ghi chú diễn giả:** mô hình ngôn ngữ nhận lời nhắc và đáp bằng một câu trả lời (response, completion); $\pi_{\mathrm{ref}}$ là chính sách softmax của Ví dụ 10.1 với $\theta_{\mathrm{ref}}=(\log2;\,0)$; đây là dạng một bước của Định nghĩa 10.52 ($s=x$, $a=y$), dạng mức token đến ở RLHF; $y_1$ được chọn 4 trên 6 lần, tức $\tfrac23$; câu hỏi có hai nửa, nửa đầu được trả lời bằng nghiệm có phạt KL, nửa sau bằng định lý tương đương và giả thiết của nó. Nguồn: §7.1, Định nghĩa 10.52, Ví dụ 10.23.

#### `L10-D02` Mô hình Bradley–Terry
- **Vị trí, loại:** mạch 7; trực quan, định nghĩa, kết quả phụ (Mệnh đề 10.54), ví dụ (Ví dụ 10.24) của cụm Bradley–Terry (`cầu nối`).
- **Lý do tồn tại:** biến các phép so sánh thành một mô hình phần thưởng bằng hợp lý cực đại; nêu sớm hai sự thật dùng về sau: chỉ hiệu phần thưởng được xác định (lớp $[r]$, dùng ở `L10-D10`, `L10-D12`), và $k=n$ không có cực tiểu (dùng ở `L10-D17`).
- **Liên kết:** trước: `L10-D01` (dữ liệu sáu phép so sánh); sau: `L10-D03` (chính sách tham lam theo $\hat r$ vừa khớp).
- **Mục tiêu:** 8.
- **Khối ghi chú:** đoạn "Một cách trực quan" sau Ví dụ 10.23, Định nghĩa 10.53, Mệnh đề 10.54, Ví dụ 10.24 (`topic-25`).
- **Mặt trang:**
  1. “**Trực quan.** Xác suất chọn chỉ phụ thuộc hiệu phần thưởng, tăng theo hiệu.”
  2. “**Định nghĩa 10.53.** Các phép so sánh độc lập, $\Pr(y\succ y'\mid x)=\sigma\bigl(r(x,y)-r(x,y')\bigr)$, $\sigma(z)=1/(1+e^{-z})$.”
  3. “**Mệnh đề 10.54.** **Giả thiết:** $\mathcal D_{\mathrm{pref}}$ hữu hạn, bộ ba độc lập theo Bradley–Terry; mô hình phần thưởng (reward model) $\hat r$ tùy ý. **Kết luận:** (a)”
  4. công thức hiển thị $$L^{\mathrm{BT}}(\hat r)=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\log\sigma\bigl(\hat r(x,y_w)-\hat r(x,y_l)\bigr)$$ (đối log-hợp lý, mất mát của hồi quy logistic; `aligned` khi tràn ở 390 px).
  5. “(b) chỉ lớp $[\hat r]=\{\hat r+f(x)\}$ được xác định; (c) hai câu trả lời, $n$ phép so sánh, $k$ chọn $y_1$: $\Delta\hat r=\hat r(y_1)-\hat r(y_2)=\log\frac k{n-k}$ nếu $0<k<n$; không có cực tiểu nếu $k=n$.”
  6. “Ví dụ 10.24, $n=6$, $k=4$: $\hat r=(\log2;\,0)$, $L^{\mathrm{BT}}$ từ $0{,}6931$ xuống $0{,}6365$; $\sigma(\log2)=\tfrac23$.”
- **Mật độ:** khoảng 73 âm tiết (14, 9, 24, 0, 21, 5 theo dòng), 6 dòng, 1 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT2 (giả thiết "$\mathcal D_{\mathrm{pref}}$ hữu hạn" và thuật ngữ "mô hình phần thưởng" của Mệnh đề 10.54) và NT9 (định nghĩa $n$, $k$, $\Delta\hat r$ tại chỗ). Dòng 3 và dòng 5 dài hơn 20 âm tiết nhưng mỗi dòng hiển thị thành hai dòng (NT17: mỗi gạch đầu dòng ≤ 2 dòng hiển thị); tác tử viết có thể ngắt sau "tùy ý." thành hai đoạn `p` chỉ khi tổng dòng vẫn ≤ 6. Lớp tương đương $[\hat r]$ của Định nghĩa 10.53 đặt ở kết luận (b), chỗ nó được dùng, cùng nghĩa với ghi chú. Không có dòng "Nhắc lại:" riêng cho hồi quy logistic (kiến thức tiên quyết mới của ghi chú): trang đã đủ 6 dòng, nên dòng 4 gọi tên "mất mát của hồi quy logistic" (đúng Mệnh đề 10.54(a)) và ghi chú diễn giả nhắc $\sigma'(z)=\sigma(z)\sigma(-z)$, $1-\sigma(z)=\sigma(-z)$; `L10-103` không nằm trong danh sách sửa (Q7, C3). Rủi ro chiều cao ở 1600×900; nếu tràn, tác tử viết báo điều phối viên, không tự bỏ dòng.
- **Phút:** 1,5. **Quyết định:** thêm; gộp C2 `L10-D02`, `L10-D03` (sai khác 3).
- **Ghi chú diễn giả:** $L^{\mathrm{BT}}$ là mất mát của hồi quy logistic với biến $\hat r(x,y_w)-\hat r(x,y_l)$ và mọi nhãn dương (Mệnh đề 10.54(a)), kiến thức học máy đã có: $\sigma'(z)=\sigma(z)\sigma(-z)$, $1-\sigma(z)=\sigma(-z)$; chứng minh (c) một dòng: đạo hàm theo $\Delta\hat r$ là $\sigma(\Delta\hat r)-\tfrac kn$, tăng ngặt; chuẩn hóa $\hat r(x,y_2)=0$ hợp lệ theo (b); "Điều kiện áp dụng" (cực tiểu trên mọi hàm, không trong lớp tham số) và "Phạm vi" (câu trả lời vắng mặt trong dữ liệu không bị ràng buộc); $k=n$ là ưu tiên tất định (deterministic preference); Nhận xét 10.55: InstructGPT xếp hạng 4–9 câu trả lời và chuẩn hóa trung bình $0$; nhầm lẫn: coi $\hat r$ là điểm tuyệt đối. Nguồn: §7.1, Định nghĩa 10.53, Mệnh đề 10.54, Ví dụ 10.24, Nhận xét 10.55; Rafailov và cộng sự (2023), Bổ đề 1; Ouyang và cộng sự (2022), §3.5.

#### `L10-D03` Mục tiêu có phạt KL
- **Vị trí, loại:** mạch 7; vấn đề, trực quan, ví dụ (Ví dụ 10.25), định nghĩa (Định nghĩa 10.56) của cụm mục tiêu có phạt KL (`cốt lõi`).
- **Lý do tồn tại:** hai giới hạn cụ thể dẫn tới mỏ neo cố định: chính sách tham lam theo $\hat r$ bỏ hẳn $y_2$; phạt KL của PPO-Penalty chỉ giữ từng bước (NT-RL-3, NT13 câu nối với mạch 6). Ví dụ ba chính sách cho thấy $(0{,}8;\,0{,}2)$ tốt hơn cả $\pi_{\mathrm{ref}}$ lẫn chính sách tham lam trước khi có định lý.
- **Liên kết:** trước: `L10-D02` ($\hat r=(\log2;\,0)$); sau: `L10-D04` (nghiệm chính xác của mục tiêu vừa định nghĩa).
- **Mục tiêu:** 8.
- **Khối ghi chú:** §7.2 đoạn mở (gồm "Một cách trực quan"), Ví dụ 10.25, Định nghĩa 10.56 và đoạn sau (`topic-26`); câu "phạt KL của PPO-Penalty … chỉ giữ mỗi bước gần $\pi_{\mathrm{old}}$" ở đoạn kết §6.6.
- **Mặt trang:**
  1. “Với $\hat r=(\log2;\,0)$, chính sách cực đại $\mathbb E_\pi\hat r$ là $(1;\,0)$: bỏ hẳn $y_2$.”
  2. “Phạt KL của PPO-Penalty chỉ giữ mỗi bước gần $\pi_{\mathrm{old}}$.”
  3. “**Trực quan.** Mỗi đơn vị KL rời $\pi_{\mathrm{ref}}$ tốn chi phí $\beta$; chỉ đi xa khi phần thưởng bù được.”
  4. bảng (khuôn "chính sách có phạt KL"): “chính sách” | $\mathbb E_\pi\hat r$ | $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ | $J_1$; hàng $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ | $0{,}4621$ | $0$ | $0{,}4621$; hàng “tham lam $(1;\,0)$” | $0{,}6931$ | $0{,}4055$ | $0{,}2877$; hàng $(0{,}8;\,0{,}2)$ | $0{,}5545$ | $0{,}0437$ | $0{,}5108$ (dữ kiện $\beta=1$ ghi ở đầu cột $J_1$: $J_1=\mathbb E_\pi\hat r-D_{\mathrm{KL}}$).
  5. “**Định nghĩa 10.56.** Mục tiêu có phạt KL (KL-regularized objective) theo chính sách tham chiếu (reference policy) $\pi_{\mathrm{ref}}$ cố định, $\beta>0$:”
  6. công thức hiển thị $$J_\beta(\pi)=\mathbb E_{x\sim\mu_0}\Bigl[\mathbb E_{y\sim\pi(\cdot\mid x)}r(x,y)-\beta D_{\mathrm{KL}}\bigl(\pi(\cdot\mid x)\Vert\pi_{\mathrm{ref}}(\cdot\mid x)\bigr)\Bigr]$$ (`aligned` ba dòng như ghi chú khi tràn ở 390 px).
- **Mật độ:** khoảng 58 âm tiết (8, 9, 18, bảng 4, 19), 6 dòng (bảng tính một dòng), 1 công thức hiển thị. Rủi ro chiều cao (bảng bốn hàng và công thức ba dòng ở màn hẹp); xử lý nếu tràn ở 1600×900: dòng 2 gộp vào dòng 1 bằng dấu chấm phẩy, không bỏ.
- **Phút:** 1. **Quyết định:** thêm.
- **Ghi chú diễn giả:** với mô hình ngôn ngữ, chính sách tham lam có thể sinh câu trả lời khác xa các câu mà $\hat r$ đã được khớp (Stiennon và cộng sự, 2020, §3.4); KL ở đây là $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$, kỳ vọng theo chính sách đang tối ưu; $0{,}0437$ chính là KL tại $s_B$ của Ví dụ 10.11 ở phần 4; $J_\beta$ là (3) của Rafailov và cộng sự (2023), và (2) của Ouyang và cộng sự (2022) khi hệ số tiền huấn luyện bằng $0$. Nguồn: §6.6 đoạn kết, §7.2, Ví dụ 10.25, Định nghĩa 10.56.

#### `L10-D04` Nghiệm của mục tiêu có phạt KL
- **Vị trí, loại:** mạch 7; phát biểu kết quả chính (Định lý 10.57); trang kết quả của luận điểm, phần 1 (cùng mục tiêu, nghiệm dạng đóng là điểm gặp).
- **Lý do tồn tại:** NT5 trang kết quả với "Giả thiết:" và "Kết luận:" đủ lượng từ; nêu $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$ cùng các kết luận (c), (d) mà `L10-D06`, `L10-D10`, `L10-D13` dùng.
- **Liên kết:** trước: `L10-D03` (ví dụ cho thấy $(0{,}8;\,0{,}2)$ tốt nhất trong ba); sau: `L10-D05` (vì sao đúng).
- **Mục tiêu:** 8.
- **Khối ghi chú:** Định lý 10.57 (Giả thiết, Kết luận (a)–(e), Điều kiện áp dụng, Phạm vi) (`topic-26`).
- **Mặt trang:**
  1. “**Giả thiết:** mỗi $\mathcal Y(x)$ hữu hạn, $\pi_{\mathrm{ref}}(\cdot\mid x)$ là phân phối trên đó; $r$ thực; $\beta>0$; chính sách chọn tự do theo $x$.”
  2. “**Kết luận:** với hàm phân hoạch (partition function) $\mathcal Z_r(x)=\sum_y\pi_{\mathrm{ref}}(y\mid x)\,e^{r(x,y)/\beta}$,”
  3. công thức hiển thị $$\pi^*_r(y\mid x)=\frac{\pi_{\mathrm{ref}}(y\mid x)\,e^{r(x,y)/\beta}}{\mathcal Z_r(x)};$$
  4. “(a) với mọi $\pi(\cdot\mid x)$ có KL hữu hạn, $\mathbb E_\pi r-\beta D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})=\beta\log\mathcal Z_r(x)-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r)$; (b) $\pi^*_r$ cực đại $J_\beta$, duy nhất tại mọi $x$ có $\mu_0(x)>0$;” (công thức (a) trong dòng, không hiển thị, để trang có 6 dòng theo cách đếm của `deck_lint.py`: mỗi công thức hiển thị là một dòng)
  5. “(c) $r-\beta\log\frac{\pi^*_r}{\pi_{\mathrm{ref}}}=\beta\log\mathcal Z_r(x)$ khi $\pi_{\mathrm{ref}}(y\mid x)>0$; (d) cùng miền hỗ trợ với $\pi_{\mathrm{ref}}$; (e) $\pi^*_{r+f}=\pi^*_r$ khi $f$ chỉ phụ thuộc $x$.”
  6. “**Ý nghĩa:** PPO trong RLHF và DPO cùng cực đại hóa $J_\beta$, nên cùng nhắm tới $\pi^*_r$.”
- **Mật độ:** khoảng 68 âm tiết (17, 8, 0, 15, 13, 15), 6 dòng, 1 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT2 (đủ giả thiết "$r$ thực" và đủ kết luận (a)–(e) của Định lý 10.57; (e) dùng ở `L10-D13`, NT9). "RLHF" và "DPO" trên dòng 6 là hai tên đã có ở `L10-104b` (tên tiếng Việt đầy đủ); tên tiếng Anh đầy đủ của RLHF ở `L10-D07`, của DPO ở `L10-D11`, nơi phương pháp được trình bày.
- **Phút:** 1,5. **Quyết định:** thêm.
- **Ghi chú diễn giả:** "Ý nghĩa" là phần 1 của luận điểm: hai con đường của các trang sau cực đại hóa cùng $J_\beta$, nên cùng một đích; (e) phần thưởng hơn kém một hàm $f(x)$ cho cùng nghiệm; $\max J_\beta=\mathbb E_x\beta\log\mathcal Z_r(x)$; "phần thưởng đã trừ KL" (vế trái của (c)) bằng nhau trên miền hỗ trợ; Điều kiện áp dụng: cực đại riêng từng $x$, với lớp tham số chỉ khi $\pi^*_r$ thuộc lớp; Phạm vi: dạng của nghiệm, không cho thuật toán khi không tính được $\mathcal Z_r(x)$; trường hợp cực biên $\beta\to\infty$ cho $\pi_{\mathrm{ref}}$, $\beta\to0^+$ cho chính sách tham lam. Nguồn: §7.2, Định lý 10.57; Rafailov và cộng sự (2023), (4), Phụ lục A.1, Bổ đề 2.

#### `L10-D05` Ý tưởng chứng minh: nghiệm của mục tiêu có phạt KL
- **Vị trí, loại:** mạch 7; ý tưởng chứng minh của kết quả chính (NT4, NT6), trang riêng.
- **Lý do tồn tại:** lộ trình bốn bước; bất đẳng thức then chốt $D_{\mathrm{KL}}\ge0$ (Mệnh đề 10.24(a) của mạch 4) ở một công thức hiển thị; chỗ vào của $\beta>0$ và "chọn tự do theo $x$"; mẹo gộp phần thưởng vào phân phối (NT7, một dòng "Kỹ thuật.").
- **Liên kết:** trước: `L10-D04`; sau: `L10-D06` (kiểm (a), (c), (d) trên số).
- **Mục tiêu:** 8 ("chứng minh nghiệm dạng đóng").
- **Khối ghi chú:** chứng minh Định lý 10.57, Bước 1–4; đoạn "Hai giả thiết có vai trò riêng" (`topic-26`).
- **Mặt trang:** danh sách đánh số
  1. “Cố định $x$. KL hữu hạn nên $\pi(y)>0\Rightarrow\pi_{\mathrm{ref}}(y)>0$; từ $\pi^*_r/\pi_{\mathrm{ref}}=e^{r/\beta}/\mathcal Z_r$ (giả thiết $\beta>0$): $\log\frac{\pi}{\pi_{\mathrm{ref}}}-\frac r\beta=\log\frac{\pi}{\pi^*_r}-\log\mathcal Z_r$.”
  2. “Nhân với $-\beta$, lấy kỳ vọng theo $y\sim\pi$, một tổng hữu hạn: được (a).”
  3. công thức hiển thị $$D_{\mathrm{KL}}(\pi\Vert\pi^*_r)\ge0$$ rồi “dấu bằng chỉ khi $\pi=\pi^*_r$ (Mệnh đề 10.24(a)): được (b).”
  4. “Chính sách chọn tự do theo $x$ (giả thiết): cực đại từng $x$ cho cực đại $J_\beta$; $e^{r/\beta}>0$ cho (d).”
  và dòng “**Kỹ thuật.** Gộp phần thưởng vào phân phối $\pi_{\mathrm{ref}}e^{r/\beta}/\mathcal Z_r$ để đọc mục tiêu bằng KL.”
- **Mật độ:** khoảng 60 âm tiết (9, 12, 9, 16, 14), 6 dòng (4 bước, 1 công thức, 1 dòng kỹ thuật), 1 công thức hiển thị.
- **Phút:** 1,5. **Quyết định:** thêm (NT6).
- **Ghi chú diễn giả (đến khoảng 250):** bỏ $\beta>0$: với $\beta=0$, $J_0=\mathbb E\,r$ có nghiệm tất định $(1;\,0)$ của trang trước, (d) sai và $e^{r/\beta}$ không xác định; bỏ "chọn tự do theo $x$": một lớp tham số dùng chung cho mọi lời nhắc có thể không chứa $\pi^*_r$; chính sách có KL vô hạn cho $-\infty$, nên bị loại ở Bước 3; (c) là logarit của định nghĩa $\pi^*_r$; (e): $\mathcal Z_{r+f}=e^{f/\beta}\mathcal Z_r$ triệt tiêu giữa tử và mẫu; "Trong thực hành": ở dạng mức token, $\mathcal Z_r(x)$ là tổng trên tới $\lvert\mathcal V\rvert^{T_{\max}}$ chuỗi, ước lượng cũng tốn kém. Nguồn: §7.2, chứng minh Định lý 10.57; Rafailov và cộng sự (2023), Phụ lục A.1, §4.

#### `L10-D06` Ví dụ: nghiệm có phạt KL trên bài toán một bước
- **Vị trí, loại:** mạch 7; ứng dụng của Định lý 10.57 trên ví dụ xuyên suốt; vai trò của $\beta$.
- **Lý do tồn tại:** cho đúng $\pi^*=(\tfrac45;\,\tfrac15)$, điểm gặp mà `L10-D08` (PPO) và `L10-D14` (DPO) cùng tới; kiểm (a), (c), (d) trên số; giới thiệu tên "phần thưởng đã trừ KL" dùng ở `L10-D07`, `L10-D08`.
- **Liên kết:** trước: `L10-D05`; sau: `L10-D07` (với mô hình ngôn ngữ, $\mathcal Z$ không tính được).
- **Mục tiêu:** 8.
- **Khối ghi chú:** Ví dụ 10.26, đoạn sau Định lý 10.57 (tên phần thưởng đã trừ KL) (`topic-26`).
- **Mặt trang:**
  1. “$\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$. Tính $\pi^*$ với $\beta=1$, rồi với $\beta=\tfrac12$, $\beta=2$.”
  2. “$\beta=1$: $\pi_{\mathrm{ref}}e^{\hat r}=(\tfrac43;\,\tfrac13)$, $\mathcal Z=\tfrac53$, $\pi^*=(\tfrac45;\,\tfrac15)$, $\max J_1=\log\tfrac53=0{,}5108$.”
  3. “Kiểm (a): $0{,}5108-D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi^*)=0{,}5108-0{,}0487=0{,}4621=J_1(\pi_{\mathrm{ref}})$.”
  4. “Kiểm (c): phần thưởng đã trừ KL (KL-penalized reward) $\log2-\log1{,}2=-\log0{,}6=0{,}5108$ ở cả hai câu trả lời.”
  5. “$\pi^*(y_1)/\pi^*(y_2)=2\cdot2^{1/\beta}$: $\beta=\tfrac12$ cho $\pi^*=(\tfrac89;\,\tfrac19)$; $\beta=2$ cho $(0{,}7388;\,0{,}2612)$.”
  6. “**Diễn giải:** $\beta$ nhỏ cho phép đi xa $\pi_{\mathrm{ref}}$; với mọi $\beta>0$, $\pi^*(y_2)>0$, đúng (d).”
- **Mật độ:** khoảng 32 âm tiết, 6 dòng, 0 công thức hiển thị.
- **Phút:** 1. **Quyết định:** thêm.
- **Ghi chú diễn giả:** $0{,}5108$ đúng $J_1$ của $(0{,}8;\,0{,}2)$ ở bảng trang trước; với chính sách tham lam, $0{,}5108-\log\tfrac1{0{,}8}=0{,}2877$, cũng đúng (a); $\beta=\tfrac12$: $\mathcal Z=3$, giá trị tối ưu $\tfrac12\log3=0{,}5493$; $\beta=2$: $\mathcal Z=1{,}2761$, giá trị $0{,}4877$; $\beta\to\infty$ cho $\pi_{\mathrm{ref}}$, $\beta\to0^+$ cho $(1;\,0)$; phần thưởng đã trừ KL bằng nhau và bằng $\beta\log\mathcal Z$ là dấu hiệu của nghiệm, dùng lại ở vòng 2 của PPO. Nguồn: §7.2, Ví dụ 10.26.

#### `L10-D07` Phần thưởng đã trừ KL theo token
- **Vị trí, loại:** mạch 7; vấn đề của cụm RLHF với PPO (NT-RL-3: Định lý 10.57 cần $\mathcal Z_r(x)$), dạng mức token, hai kết quả phụ (Bổ đề 10.59, Mệnh đề 10.60) và phần thưởng (7.1) đưa vào PPO.
- **Lý do tồn tại:** nối mục tiêu có phạt KL với Thuật toán 10.49: gradient của $J_\beta$ là gradient chính sách với phần thưởng đã trừ KL giữ cố định tại $\theta_{\mathrm{old}}$, chia theo token thành (7.1). Nhắc lại mô hình ngôn ngữ tự hồi quy (kiến thức tiên quyết mới của ghi chú) tại chỗ dùng.
- **Liên kết:** trước: `L10-D06`; sau: `L10-D08` (hai vòng PPO với phần thưởng này).
- **Mục tiêu:** 8.
- **Khối ghi chú:** §7.3 đoạn mở, Định nghĩa 10.52(b), Bổ đề 10.59, Mệnh đề 10.60, đoạn có (7.1); Kiến thức tiên quyết, gạch "Hồi quy logistic và mô hình ngôn ngữ tự hồi quy" (`topic-27`).
- **Mặt trang:**
  1. “Định lý 10.57 cần $\mathcal Z_r(x)$, tổng trên mọi câu trả lời.”
  2. “Học tăng cường từ phản hồi con người (reinforcement learning from human feedback, RLHF) cực đại $J_\beta$ bằng mẫu.”
  3. “Dạng mức token: $S_0=x$, hành động $A_t$ là token, $S_{t+1}=(S_t,A_t)$, $\pi(y\mid x)=\prod_t\pi(A_t\mid S_t)$; dừng ở token kết thúc hoặc $T_{\max}$; chỉ $R_T=r(x,y)$ khác $0$; $\gamma=1$.”
  4. “**Bổ đề 10.59.** Khi $\pi>0\Rightarrow\pi_{\mathrm{ref}}>0$: (a) $\log\frac{\pi(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}=\sum_t\log\frac{\pi(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}$; (b) KL của câu trả lời bằng kỳ vọng tổng KL theo token.”
  5. “**Mệnh đề 10.60.** Dạng một bước, $\pi_\theta>0$ khả vi, $\pi_{\mathrm{ref}}>0$, $\tilde r_\theta=r-\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$: $\nabla_\theta J_\beta=\mathbb E[\tilde r_\theta\nabla_\theta\log\pi_\theta]$; tại $\theta_{\mathrm{old}}$ là gradient chính sách với $\tilde r_{\theta_{\mathrm{old}}}$ cố định; phần thưởng của bước $t$:”
  6. công thức hiển thị (7.1), không `\tag`: $$R_{t+1}=-\beta\log\frac{\pi_{\mathrm{old}}(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}+\mathbb 1\{t+1=T\}\,\hat r(x,y)$$
- **Mật độ:** khoảng 81 âm tiết (10, 18, 15, 18, 20), 6 dòng, 1 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT-RL-3 (dòng 1: giới hạn của Định lý 10.57, như câu cuối §7.2), NT-RL-4 (dạng mức token đủ $S_0$, điều kiện kết thúc, phần thưởng $0$ trước $T$, như Định nghĩa 10.52(b)), NT2 (giả thiết "dạng một bước", "khả vi" của Mệnh đề 10.60), NT21 (tên đầy đủ và tên tiếng Anh của RLHF). Câu "(7.1) có tổng bằng $\tilde r_{\theta_{\mathrm{old}}}(x,y)$ khi $r=\hat r$" chuyển vào ghi chú diễn giả. Dòng 4 và 5 dài, mỗi dòng hiển thị tối đa hai dòng; nếu tràn khung ở 1600×900, tác tử viết báo điều phối viên.
- **Phút:** 1. **Quyết định:** thêm; tách từ C2 `L10-D08` (sai khác 1).
- **Ghi chú diễn giả:** (7.1) có tổng bằng $\tilde r_{\theta_{\mathrm{old}}}(x,y)$ khi $r=\hat r$; với mô hình ngôn ngữ, Định lý 10.57 cho dạng nghiệm nhưng cần cực đại hóa $J_\beta$ bằng mẫu; chứng minh hai kết quả: Bổ đề 10.59(a) là logarit của tích theo token vì chuyển tất định, (b) theo tính chất tháp; ví dụ hai token cho KL $0{,}2410=0{,}0201+0{,}6\cdot0{,}3681$; Mệnh đề 10.60 dùng $\nabla\tilde r_\theta=-\beta\nabla\log\pi_\theta$ và Mệnh đề 09.17; theo Mệnh đề 10.41(c), gradient của hàm thay thế mẫu tại $\theta_{\mathrm{old}}$ có kỳ vọng $\nabla J_\beta(\theta_{\mathrm{old}})$ khi lợi thế đúng; trên một câu trả lời tổng KL theo token có thể âm, chỉ bằng KL theo kỳ vọng; đây là phạt KL theo từng token (per-token KL penalty) của InstructGPT. Nguồn: §7.3, Định nghĩa 10.52, Bổ đề 10.59, Mệnh đề 10.60, (7.1); Ouyang và cộng sự (2022), §3.5.

#### `L10-D08` Ví dụ: hai vòng PPO trên phần thưởng đã trừ KL
- **Vị trí, loại:** mạch 7; ví dụ tính tay của RLHF với PPO trước giả mã (NT-RL-2); hai mỏ neo và hai chiều KL (Nhận xét 10.58; NT-RL-4).
- **Lý do tồn tại:** cho thấy trên số rằng phép cắt (theo $\pi_{\mathrm{old}}$) giới hạn bước, còn $\pi_{\mathrm{ref}}$ và $\hat r$ quyết định điểm dừng, và PPO dừng ở $\pi^*$ của `L10-D06` trong ví dụ này chỉ do $\epsilon=0{,}2$.
- **Liên kết:** trước: `L10-D07`; sau: `L10-D09` (giả mã ba giai đoạn, bước 3 là đúng hai vòng này).
- **Mục tiêu:** 8 ("phân biệt chính sách cũ của PPO với chính sách tham chiếu").
- **Khối ghi chú:** Ví dụ 10.27; Nhận xét 10.58 (`topic-27`; Nhận xét 10.58 nằm ở §7.2 nhưng mang hai mỏ neo mà ví dụ này làm cụ thể, NT2: nội dung giữ nguyên, chỉ đổi chỗ trình bày trong cùng mạch).
- **Mặt trang:**
  1. “$\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$, $\beta=1$, $\epsilon=0{,}2$, $p=\pi(y_1)$; bộ đệm $y_1,y_1,y_2$; mỗi vòng cố định $\tilde r$ và lợi thế đúng. Tính hai vòng.”
  2. “Vòng 1, $\pi_{\mathrm{old}}=\pi_{\mathrm{ref}}$: $\tilde r=\hat r$, lợi thế $\tfrac13\log2\,(1;\,1;\,-2)$; $\mathcal L^{\mathrm{CLIP}}$ tăng tới $p=\tfrac23\cdot1{,}2=0{,}8$ rồi nằm ngang.”
  3. “Vòng 2, $\pi_{\mathrm{old}}=(0{,}8;\,0{,}2)$: $\tilde r=(0{,}5108;\,0{,}5108)$, lợi thế $0$; chính sách đứng yên ở $\pi^*$.”
  4. “**Diễn giải:** $\pi_{\mathrm{old}}$ giới hạn bước; $\pi_{\mathrm{ref}}$ và $\hat r$ quyết định điểm dừng.”
  5. “**Nhận xét 10.58.** Mỏ neo là chính sách mà phép phạt giữ gần: $\pi_{\mathrm{old}}$ đổi mỗi vòng, trong $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$; $\pi_{\mathrm{ref}}$ cố định, trong $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$.”
  6. “**Lưu ý:** vòng 1 dừng đúng ở $\pi^*$ chỉ vì $\tfrac23(1+\epsilon)=0{,}8$.”
- **Mật độ:** khoảng 70 âm tiết (13, 9, 9, 10, 20, 9), 6 dòng, 0 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT9 (định nghĩa $p$ và thuật ngữ "mỏ neo" trên mặt trang trước khi dùng), NT23 (dòng "Tính …"). Khuôn bảng "mẫu PPO" của mạch 6 không dùng: ba mẫu chỉ có hai giá trị lợi thế, viết thành vector trong dòng 2.
- **Phút:** 1,5. **Quyết định:** thêm.
- **Ghi chú diễn giả:** lợi thế vòng 1 là $(0{,}2310;\,0{,}2310;\,-0{,}4621)$, đúng $\tfrac13\log2$ lần lợi thế của bộ đệm ở phần 6, nên đoạn phẳng bắt đầu ở cùng $p=0{,}8$; gradient tại $\theta_{\mathrm{ref}}$ là $\tfrac29\log2\,(1;\,-1)=(0{,}1540;\,-0{,}1540)$, đúng Mệnh đề 10.60; vòng 2: mọi số hạng cắt bằng $0$ (Mệnh đề 10.40(c)); $J_1(0{,}8)=0{,}5545-0{,}0437=0{,}5108$; "mỏ neo" là chính sách mà phép phạt giữ chính sách mới ở gần; chiều KL: với $\pi=(1;\,0)$, $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})=\log\tfrac32$ còn $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi)=+\infty$; dữ liệu của mỗi vòng do $\pi_{\mathrm{old}}$ sinh, theo chính sách và trực tuyến; với $\epsilon=0{,}1$ dãy dao động quanh $0{,}8$ (Bài tập 10.21 của ghi chú). Nguồn: §7.2, §7.3, Ví dụ 10.27, Nhận xét 10.58; Ziegler và cộng sự (2019), §2.2.

#### `L10-D09` Thuật toán RLHF với PPO
- **Vị trí, loại:** mạch 7; phát biểu thuật toán (Thuật toán 10.61), sau ví dụ tính tay (NT-RL-2).
- **Lý do tồn tại:** mục tiêu 8 đòi mô tả ba giai đoạn; nêu bốn mô hình trong bộ nhớ và dữ liệu sinh trực tuyến, đúng hai điểm mà DPO bỏ đi (NT-RL-4: theo chính sách, trực tuyến).
- **Liên kết:** trước: `L10-D08` (bước 3 với một lời nhắc); sau: `L10-D10` (bốn mô hình và việc sinh mẫu ở mọi vòng là giới hạn mở cụm DPO).
- **Mục tiêu:** 8.
- **Khối ghi chú:** Thuật toán 10.61, đoạn "Trong thực hành" sau nó, Nhận xét 10.62 (`topic-27`).
- **Mặt trang:**
  1. “**Thuật toán 10.61.** **Giả thiết:** dạng mức token; người gán nhãn theo Bradley–Terry; $\pi_\theta$, $\pi_{\mathrm{ref}}$ softmax trên token.”
  2. “**Đầu vào:** mô hình tiền huấn luyện, bản mẫu, lời nhắc, $\beta>0$.”
  3. “1. Tinh chỉnh có giám sát (supervised fine-tuning, SFT) được $\pi^{\mathrm{SFT}}$; $\pi_{\mathrm{ref}}\leftarrow\pi^{\mathrm{SFT}}$ cố định, $\pi_\theta\leftarrow\pi^{\mathrm{SFT}}$.”
  4. “2. So sánh câu trả lời của $\pi^{\mathrm{SFT}}$ thành $\mathcal D_{\mathrm{pref}}$; khớp $\hat r$ bằng $L^{\mathrm{BT}}$.”
  5. “3. Mỗi vòng: Thuật toán 10.49 với phần thưởng (7.1), $\gamma=1$, trên mẫu trực tuyến (online) của $\pi_{\mathrm{old}}$.”
  6. “**Đầu ra:** $\pi_\theta$ sau ngân sách số lượt; bộ nhớ: $\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic.”
- **Mật độ:** khoảng 72 âm tiết (16, 11, 11, 9, 15, 10; số thứ tự của `ol` không tính), 6 dòng (các bước 1–3 là `ol` trong khối thuật toán), 0 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT2 (dòng "Giả thiết" của Thuật toán 10.61). "Bản mẫu" là câu trả lời mẫu do người gán nhãn viết; ghi chú diễn giả nêu đủ.
- **Phút:** 1. **Quyết định:** thêm; tách từ C2 `L10-D08` (sai khác 1).
- **Ghi chú diễn giả:** giả thiết của thuật toán (dạng mức token, người gán nhãn theo Bradley–Terry, softmax trên token); bước 2 chuẩn hóa $\hat r$ và khởi tạo critic từ $\hat r$; với một lời nhắc và lợi thế đúng, bước 3 là hai vòng của trang trước; chi phí mỗi vòng: sinh $N$ câu trả lời, một lần $\hat r$ mỗi câu, log-xác suất của $\pi_{\mathrm{ref}}$ mỗi token; InstructGPT dùng $\beta=0{,}02$, bán kính cắt $0{,}2$, một epoch, và biến thể PPO-ptx thêm số hạng tiền huấn luyện nên Định lý 10.57 không áp dụng nguyên dạng; Nhận xét 10.62: tối ưu mạnh làm ưu tiên thật giảm so với dự đoán của mô hình phần thưởng (tối ưu quá mức, over-optimization). Nguồn: §7.3, Thuật toán 10.61, Nhận xét 10.62; Ziegler và cộng sự (2019), §2; Stiennon và cộng sự (2020), §3.4, §4.3; Ouyang và cộng sự (2022), §3.1, Phụ lục C.4.

#### `L10-D10` Đổi biến giữa phần thưởng và chính sách
- **Vị trí, loại:** mạch 7; vấn đề của cụm DPO (NT-RL-3: giới hạn cụ thể của Thuật toán 10.61 trong một dòng), ví dụ số, trực quan, kết quả phụ (Mệnh đề 10.63).
- **Lý do tồn tại:** phép đổi biến là bước then chốt của DPO; trên số, hàm phân hoạch triệt tiêu trong hiệu hai phần thưởng trước khi có phát biểu tổng quát (NT8: ví dụ trước phát biểu, như ghi chú).
- **Liên kết:** trước: `L10-D09` (bốn mô hình, sinh mẫu ở mọi vòng); sau: `L10-D11` (thay phần thưởng bằng log-tỉ số trong $L^{\mathrm{BT}}$).
- **Mục tiêu:** 9 ("bằng phép đổi biến giữa phần thưởng và chính sách").
- **Khối ghi chú:** đoạn kết §7.3 (bốn mô hình), §7.4 đoạn mở (số và "Một cách trực quan"), Mệnh đề 10.63 và đoạn sau (`topic-28`).
- **Mặt trang:**
  1. “Thuật toán 10.61 cần bốn mô hình, sinh mẫu ở mọi vòng; $\hat r$ chỉ để xác định $\pi^*_{\hat r}$.”
  2. “$\beta\log\frac{\pi^*}{\pi_{\mathrm{ref}}}+\beta\log\mathcal Z$ với $\pi^*=(\tfrac45;\,\tfrac15)$, $\mathcal Z=\tfrac53$, $\beta=1$: $\log1{,}2+\log\tfrac53=\log2=\hat r(y_1)$, $\log0{,}6+\log\tfrac53=0=\hat r(y_2)$.”
  3. “**Trực quan.** Mỗi chính sách là nghiệm có phạt KL của một phần thưởng.”
  4. “**Mệnh đề 10.63.** **Giả thiết:** như Định lý 10.57 và $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $x$, $y$.”
  5. “**Kết luận:** (a) $r=\beta\log\frac{\pi^*_r}{\pi_{\mathrm{ref}}}+\beta\log\mathcal Z_r(x)$; (b) trong $\Pr(y\succ y'\mid x)$ của Bradley–Terry, $\mathcal Z_r(x)$ triệt tiêu.”
  6. “(c) Mỗi $\pi>0$ là $\pi^*_{r_\pi}$ với $r_\pi=\beta\log(\pi/\pi_{\mathrm{ref}})$; trong $[r]$, chỉ $r_{\pi^*_r}$ có dạng $r_\pi$.”
- **Mật độ:** khoảng 60 âm tiết (16, 1, 14, 12, 9, 8), 6 dòng, 0 công thức hiển thị (ý "học thẳng chính sách" của ghi chú ở ghi chú diễn giả; công thức trong dòng; tác tử viết dùng `\dfrac` hoặc `/` cho phân số trong dòng nếu chữ quá nhỏ).
- **Phút:** 1. **Quyết định:** thêm.
- **Ghi chú diễn giả:** hiệu hai vế trái ở dòng 2 là $\log1{,}2-\log0{,}6=\log2$, không chứa $\mathcal Z$; chứng minh ba bước: (a) là Định lý 10.57(c), (b) vì $\beta\log\mathcal Z_r(x)$ có ở cả hai phần thưởng của cùng lời nhắc, (c) vì $\mathcal Z_{r_\pi}=1$; mỗi lớp $[r]$ ứng với đúng một chính sách có miền hỗ trợ đầy đủ; đây là phép đổi biến (reparameterization) của DPO. Nguồn: §7.4, Mệnh đề 10.63; Rafailov và cộng sự (2023), (5), (6), Định lý 1, Mệnh đề 1, Phụ lục A.6.

#### `L10-D11` Hàm mất mát DPO
- **Vị trí, loại:** mạch 7; định nghĩa (Định nghĩa 10.64) và cách đọc trên ví dụ xuyên suốt.
- **Lý do tồn tại:** thế (b) của Mệnh đề 10.63 vào $L^{\mathrm{BT}}$ cho một hàm mất mát phân loại theo $\theta$; tên đầy đủ của DPO trên trang nội dung (NT21).
- **Liên kết:** trước: `L10-D10`; sau: `L10-D12` (cực tiểu của hàm mất mát này là gì).
- **Mục tiêu:** 9.
- **Khối ghi chú:** Định nghĩa 10.64 và đoạn sau (`topic-28`).
- **Mặt trang:**
  1. “**Định nghĩa 10.64.** Với $\pi_\theta>0$, $\pi_{\mathrm{ref}}>0$, $\beta>0$: phần thưởng ngầm định (implicit reward) và hiệu của nó trên bộ ba”
  2. công thức hiển thị $$r_\theta(x,y)=\beta\log\frac{\pi_\theta(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)},\qquad\Delta r_\theta=r_\theta(x,y_w)-r_\theta(x,y_l);$$
  3. “Tối ưu ưu tiên trực tiếp (Direct Preference Optimization, DPO) cực tiểu hóa theo $\theta$”
  4. công thức hiển thị $$L^{\mathrm{DPO}}(\theta)=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\bigl[\log\sigma(\Delta r_\theta)\bigr]=L^{\mathrm{BT}}(r_\theta).$$
  5. “Theo Mệnh đề 10.54(a): hồi quy logistic với biến $\Delta r_\theta$.”
  6. “Softmax đặc trưng đơn vị, $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$: bộ ba chọn $y_1$ có $\Delta r_\theta=\beta(\theta_1-\theta_2-\log2)$.”
- **Mật độ:** khoảng 49 âm tiết, 6 dòng, 2 công thức hiển thị.
- **Phút:** 1. **Quyết định:** thêm; Mệnh đề 10.66 chuyển sang `L10-D14` (sai khác 4).
- **Ghi chú diễn giả:** với softmax, $\log\frac{\pi_\theta(y_1)}{\pi_\theta(y_2)}=\theta_1-\theta_2$; bộ ba chọn $y_2$ có $\Delta r_\theta$ ngược dấu; tại $\theta_{\mathrm{ref}}$, $\Delta r_\theta=0$ và $L^{\mathrm{DPO}}=\log2$; không có mô hình phần thưởng riêng: phần thưởng ngầm định đọc thẳng từ $\pi_\theta$ và $\pi_{\mathrm{ref}}$; ký hiệu của bài báo ($\hat r_\theta$, $\mathcal L_{\mathrm{DPO}}$) khác ký hiệu của bài. Nguồn: §7.4, Định nghĩa 10.64; Rafailov và cộng sự (2023), (7).

#### `L10-D12` Tương đương giữa RLHF và DPO
- **Vị trí, loại:** mạch 7; phát biểu kết quả chính (Định lý 10.65); trang kết quả của luận điểm, phần 2 (cùng nghiệm, không vòng học tăng cường, chỉ dưới đủ giả thiết).
- **Lý do tồn tại:** NT5, NT2: đủ năm giả thiết với lượng từ "với mọi $x$, $y$" và "trên mọi hàm phần thưởng", cùng điều kiện "cùng $\mathcal D_{\mathrm{pref}}$, $\beta$, $\pi_{\mathrm{ref}}$"; kết luận tách phần cần (H4a) và phần cần thêm (H4b).
- **Liên kết:** trước: `L10-D11`; sau: `L10-D13` (vì sao đúng, giả thiết vào ở đâu).
- **Mục tiêu:** 9 ("phát biểu các giả thiết để DPO và RLHF cho cùng chính sách tối ưu").
- **Khối ghi chú:** Định lý 10.65 (Giả thiết, đoạn hai con đường, Kết luận (a)–(c), Điều kiện áp dụng, Phạm vi) và đoạn sau chứng minh (`topic-28`).
- **Mặt trang:**
  1. “**Giả thiết:** (H1) mọi $\mathcal Y(x)$ hữu hạn, $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $x$, $y$; (H2) $\beta>0$;”
  2. “(H3) lớp chính sách gồm mọi phân phối có miền hỗ trợ đầy đủ, chọn tự do theo $x$;”
  3. “(H4a) $L^{\mathrm{BT}}$ trên mọi hàm phần thưởng đạt cực tiểu; (H4b) tập cực tiểu là đúng một lớp $[\hat r]$.”
  4. “Cùng $\mathcal D_{\mathrm{pref}}$, $\beta$, $\pi_{\mathrm{ref}}$; con đường RLHF lý tưởng: cực tiểu $\hat r$ của $L^{\mathrm{BT}}$, rồi $\pi^*_{\hat r}$.”
  5. “**Kết luận:** dưới (H1)–(H3), (H4a): $\pi^*_{\hat r}$ cực tiểu $L^{\mathrm{DPO}}$ và $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$; thêm (H4b): $\arg\min L^{\mathrm{DPO}}=\{\pi^*_{\hat r}\}$.”
  6. “**Ý nghĩa:** dưới các giả thiết đó, cực tiểu $L^{\mathrm{DPO}}$ là nghiệm này, không qua PPO hay học tăng cường trực tuyến.”
- **Mật độ:** khoảng 84 âm tiết (9, 18, 17, 10, 10, 20), 6 dòng, 0 công thức hiển thị: ngoại lệ trần 60 (≤ 90, kế hoạch C5), lý do: NT2 cấm bỏ giả thiết, lượng từ; năm giả thiết và điều kiện cùng dữ liệu là nội dung của phần 2 luận điểm.
- **Phút:** 1,5. **Quyết định:** thêm.
- **Ghi chú diễn giả:** kết luận (b) đầy đủ: dưới (H1)–(H3), (H4a), mọi cực tiểu $\pi$ có $r_\pi$ cực tiểu $L^{\mathrm{BT}}$ và $\pi=\pi^*_{r_\pi}$; Điều kiện áp dụng: cực tiểu hóa chính xác cả hai hàm mất mát và giải chính xác $J_\beta$; Phạm vi: định lý nói về nghiệm, không về các bước lặp của PPO hay của hạ gradient; khi (H4a) hỏng cả hai hàm mất mát không có cực tiểu, khi chỉ (H4b) hỏng nghiệm không duy nhất; (H4a), (H4b) thỏa khi $0<k<n$ với hai câu trả lời, và khi mỗi cặp được so sánh có cả hai kết quả và các cặp nối mọi câu trả lời; mô hình Bradley–Terry chỉ cần để đọc $\hat r$ là ước lượng hợp lý cực đại; phát biểu ghép Định lý 1, Mệnh đề 1 của DPO và nửa đầu Định lý 4.1 của Xu và cộng sự; ứng dụng dương của định lý (Tình huống 10.4, không lên mặt trang): ba bản tóm tắt, $\pi_{\mathrm{ref}}=(0{,}5;\,0{,}3;\,0{,}2)$, 45 phép so sánh, mỗi cặp có cả hai kết quả và ba cặp nối ba bản nên (H4a), (H4b) thỏa, $\hat r=(\log4;\,\log2;\,0)$, $\pi^*=(0{,}7143;\,0{,}2143;\,0{,}0714)$, và DPO trên 45 phép so sánh cho cùng chính sách. Nguồn: §7.4, Định lý 10.65; Tình huống 10.4; Rafailov và cộng sự (2023), Phụ lục A.6; Xu và cộng sự (2024), Định lý 4.1; Gheshlaghi Azar và cộng sự (2024), Phụ lục B.

#### `L10-D13` Ý tưởng chứng minh: tương đương giữa RLHF và DPO
- **Vị trí, loại:** mạch 7; ý tưởng chứng minh của kết quả chính (NT4, NT6), trang riêng; bước kiểm tra (vai của (H4b)).
- **Lý do tồn tại:** bốn bước: đẳng thức đại số $L^{\mathrm{DPO}}(\pi)=L^{\mathrm{BT}}(r_\pi)$, cận dưới, dấu bằng tại $\pi^*_{\hat r}$, duy nhất; mỗi giả thiết ghi ở bước dùng nó; một dòng "bỏ giả thiết thì hỏng ở đâu" (NT4) cho (H4b). Trường hợp (H4a) hỏng để cho `L10-D17` (NT13: không trùng ví dụ).
- **Liên kết:** trước: `L10-D12`; sau: `L10-D14` (hạ gradient trên $L^{\mathrm{DPO}}$ tiến về cực tiểu nào trên số).
- **Mục tiêu:** 9.
- **Khối ghi chú:** chứng minh Định lý 10.65, Bước 1–4; gạch "Bỏ (H4b)" của đoạn "Mỗi giả thiết có vai trò riêng" (`topic-28`).
- **Mặt trang:** danh sách đánh số
  1. “Với mọi $\pi$ của (H3), $r_\pi$ hữu hạn (giả thiết (H1)) và $L^{\mathrm{DPO}}(\pi)=L^{\mathrm{BT}}(r_\pi)$.”
  2. “Cực tiểu của (H4a) lấy trên mọi hàm phần thưởng, kể cả $r_\pi$:” và công thức hiển thị $$L^{\mathrm{DPO}}(\pi)\ge\min L^{\mathrm{BT}}.$$
  3. “$\pi^*_{\hat r}$ thuộc lớp (Định lý 10.57(d), (H1)) và $r_{\pi^*_{\hat r}}\in[\hat r]$ (Mệnh đề 10.63(c)): dấu bằng đạt.”
  4. “Mọi cực tiểu $\pi$ có $r_\pi$ cực tiểu $L^{\mathrm{BT}}$; dưới (H4b), $r_\pi=\hat r+f$, nên $\pi=\pi^*_{\hat r+f}=\pi^*_{\hat r}$ theo (e).”
  và dòng “Bỏ (H4b): tập cực tiểu của $L^{\mathrm{BT}}$ không là một lớp, nghiệm không duy nhất.”
- **Mật độ:** khoảng 58 âm tiết (10, 12, 13, 9, 14), 6 dòng, 1 công thức hiển thị; ý "đẳng thức đại số" của Bước 1 nói trong ghi chú diễn giả. Số hiệu Định lý 10.57 chỉ xuất hiện một lần (NT5); bước 4 dẫn kết luận (e), có trên `L10-D04` sau cổng III.2 (NT9).
- **Phút:** 1. **Quyết định:** thêm (sai khác 2).
- **Ghi chú diễn giả (đến khoảng 250):** Bước 1 không cần mô hình Bradley–Terry: đó là định nghĩa $L^{\mathrm{DPO}}(\theta)=L^{\mathrm{BT}}(r_\theta)$; Bước 3 dùng thêm Mệnh đề 10.54(b) ($L^{\mathrm{BT}}$ không đổi trong một lớp); Bước 4 dùng (c) của định lý để có $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$ và kết luận (e) của Định lý 10.57; bỏ (H1): với $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac12;\,0)$ và bốn so sánh chọn $y_1$ trước $y_2$, hai so sánh ngược lại, mọi chính sách có $\pi(y_2)=2^{-1/\beta}\pi(y_1)>0$ cực tiểu $L^{\mathrm{DPO}}$ dù $\pi(y_3)$ lớn, trong khi $\pi^*_{\hat r}(y_3)=0$; bỏ (H4b): với $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, sáu so sánh chỉ giữa $y_1$, $y_2$, mọi chính sách có $\pi(y_1)=4\pi(y_2)$ cực tiểu (Bài tập 10.20 của ghi chú); bỏ (H3): trên lớp tham số không chứa $\pi^*_{\hat r}$, hai nghiệm không nhất thiết trùng. Nguồn: §7.4, chứng minh Định lý 10.65.

#### `L10-D14` Ví dụ: một bước DPO tính tay
- **Vị trí, loại:** mạch 7; kết quả phụ (Mệnh đề 10.66, gradient) và ví dụ tính tay trước giả mã (NT-RL-2) trên dữ liệu của `L10-D01`.
- **Lý do tồn tại:** một bước hạ gradient với giá trị khởi tạo $\theta_{\mathrm{ref}}$; các bước sau tiến về $(\tfrac45;\,\tfrac15)$, đúng $\pi^*$ của `L10-D06`: hai con đường gặp nhau trên số (Định lý 10.65).
- **Liên kết:** trước: `L10-D13`; sau: `L10-D15` (giả mã cho cùng bước).
- **Mục tiêu:** 9 ("tính bằng tay một bước DPO").
- **Khối ghi chú:** Mệnh đề 10.66 và đoạn sau (trọng số), Ví dụ 10.28 (`topic-28`).
- **Mặt trang:**
  1. “**Mệnh đề 10.66.** **Giả thiết:** như Định nghĩa 10.64; $\pi_\theta$ khả vi; không lấy đạo hàm qua $\pi_{\mathrm{ref}}$. **Kết luận:**”
  2. công thức hiển thị $$\nabla_\theta L^{\mathrm{DPO}}=-\beta\,\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\bigl[\sigma(-\Delta r_\theta)\bigl(\nabla_\theta\log\pi_\theta(y_w\mid x)-\nabla_\theta\log\pi_\theta(y_l\mid x)\bigr)\bigr]$$ (`aligned` khi tràn).
  3. “Sáu phép so sánh, $\beta=1$, bước học $1$, từ $\theta_{\mathrm{ref}}=(\log2;\,0)$. Tính một bước.”
  4. “Trọng số $\sigma(0)=\tfrac12$, $\psi(y_1)-\psi(y_2)=(1;\,-1)$: $\nabla L^{\mathrm{DPO}}=-\bigl[\tfrac46\cdot\tfrac12\,(1;\,-1)+\tfrac26\cdot\tfrac12\,(-1;\,1)\bigr]=(-\tfrac16;\,\tfrac16)$.”
  5. “$\theta=(0{,}8598;\,-0{,}1667)$, $\pi_\theta(y_1)=0{,}7362$, $\Delta r_\theta=\tfrac13$, $L^{\mathrm{DPO}}$ từ $0{,}6931$ xuống $0{,}6514$.”
  6. “**Diễn giải:** các bước sau cho $\pi_\theta(y_1)=0{,}7676;\ 0{,}7829;\ 0{,}7907;\ 0{,}7949$, tiến về cực tiểu $\pi^*=(\tfrac45;\,\tfrac15)$ của Định lý 10.65.”
- **Mật độ:** khoảng 46 âm tiết, 6 dòng, 1 công thức hiển thị.
- **Phút:** 1,5. **Quyết định:** thêm; Mệnh đề 10.66 lên trang này theo thứ tự của ghi chú (sai khác 4).
- **Ghi chú diễn giả:** mỗi bộ ba đẩy $\theta$ theo hướng tăng $\log\pi_\theta(y_w)-\log\pi_\theta(y_l)$ với trọng số $\sigma(-\Delta r_\theta)$, lớn khi phần thưởng ngầm định xếp sai cặp; ở bước 2, trọng số $0{,}4174$ cho bốn bộ chọn $y_1$ và $0{,}5826$ cho hai bộ bị xếp sai; bỏ trọng số có thể làm mô hình ngôn ngữ suy biến (Rafailov và cộng sự, 2023, §4); phần thưởng ngầm định sau bước 1: $0{,}0993$ và $-0{,}2341$; cực tiểu đạt tại $\Delta r_\theta=\log2$, tức $\theta_1-\theta_2=2\log2$, với $\min L^{\mathrm{DPO}}=0{,}6365=\min L^{\mathrm{BT}}$; với $\beta$ tùy ý, tỉ số cực tiểu $2\cdot2^{1/\beta}$, đúng trang nghiệm có phạt KL; Nhận xét 10.68: $\mathbb E_{\pi_{\mathrm{ref}}}r_\theta=-\beta D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)\le0$, sau bước 1 bằng $-0{,}0119$, nên DPO không tăng xác suất của mọi câu được chọn. Nguồn: §7.4, Mệnh đề 10.66, Ví dụ 10.28, Nhận xét 10.68; Rafailov, Hejna, Park và Finn (2024), (16).

#### `L10-D15` Thuật toán DPO
- **Vị trí, loại:** mạch 7; phát biểu thuật toán (Thuật toán 10.67) sau ví dụ tính tay; phân biệt ngoại tuyến và khác chính sách (NT-RL-4).
- **Lý do tồn tại:** đầu vào, khởi tạo, các bước theo mini-batch, điều kiện dừng, mô hình trong bộ nhớ (P3: "Đầu vào:", "Đầu ra:"); ví dụ, công thức và giả mã cho cùng bước (NT-RL-2).
- **Liên kết:** trước: `L10-D14`; sau: `L10-D16` (đặt hai thuật toán cạnh nhau).
- **Mục tiêu:** 9.
- **Khối ghi chú:** Thuật toán 10.67, đoạn sau nó và "Trong thực hành" của §7.4 (`topic-28`).
- **Mặt trang:**
  1. “**Thuật toán 10.67.** **Giả thiết:** (H1), (H2); $\pi_\theta$ softmax trên token.”
  2. “**Đầu vào:** $\mathcal D_{\mathrm{pref}}$ cố định (ngoại tuyến, offline; khác chính sách), $\pi_{\mathrm{ref}}$ đóng băng, $\beta>0$, cỡ mini-batch $M$; khởi tạo $\theta\leftarrow\theta_{\mathrm{ref}}$.”
  3. “Mỗi mini-batch: (1) $\log\pi_\theta$, $\log\pi_{\mathrm{ref}}$ của $y_w$, $y_l$, mỗi đại lượng là tổng log-xác suất token;”
  4. “(2) $\Delta r_\theta$ và $L^{\mathrm{DPO}}$ trung bình trên mini-batch;”
  5. “(3) một bước của bộ tối ưu theo Mệnh đề 10.66.”
  6. “**Đầu ra:** $\pi_\theta$ sau số epoch đã định; chỉ $\pi_\theta$, $\pi_{\mathrm{ref}}$; không sinh mẫu, không critic.”
- **Mật độ:** khoảng 68 âm tiết (10, 16, 12, 6, 11, 13), 6 dòng, 0 công thức hiển thị: ngoại lệ trần 60 (≤ 90; sửa sau cổng III.2), lý do NT2 (dòng "Giả thiết" của Thuật toán 10.67) và NT21 ("offline"). $\log\pi_{\mathrm{ref}}$ tính trước một lần cho mọi bộ ba (ghi chú diễn giả).
- **Phút:** 1. **Quyết định:** thêm.
- **Ghi chú diễn giả:** giả thiết (H1), (H2) và $\pi_\theta$ softmax trên token nên dương; với sáu bộ ba của ví dụ trong một mini-batch, hạ gradient bước học $1$ và $\theta\leftarrow\theta_{\mathrm{ref}}$, bước đầu cho gradient $(-\tfrac16;\,\tfrac16)$ và $\pi_\theta(y_1)=0{,}7362$, đúng trang trước; chi phí mỗi bộ ba: hai lượt tính $\log\pi_\theta$ trên chuỗi có sẵn và một lượt lan truyền ngược; dữ liệu cố định do $\pi^{\mathrm{SFT}}$ sinh, nên DPO là phương pháp ngoại tuyến (offline) trên dữ liệu khác chính sách, còn RLHF với PPO là trực tuyến (online); không cần tỉ số $\rho_t$ vì $L^{\mathrm{DPO}}$ không là kỳ vọng theo $\pi_\theta$; khi không có mô hình SFT, bài báo khớp $\pi_{\mathrm{ref}}$ bằng hợp lý cực đại trên các cặp $(x,y_w)$; bài báo dùng $\beta=0{,}1$, cỡ mini-batch $64$, RMSprop với bước học $10^{-6}$. Nguồn: §7.4, Thuật toán 10.67; Rafailov và cộng sự (2023), §4, Phụ lục B.

#### `L10-D16` So sánh PPO trong RLHF và DPO
- **Vị trí, loại:** mạch 7; bảng so sánh hai phương pháp trên cùng tiêu chí; trang so sánh của luận điểm, phần 3 (khác nhau ở dữ liệu, mô hình, lấy mẫu, mỏ neo; giống nhau ở mục tiêu; bảo đảm có điều kiện). Ứng dụng của cả cụm: đọc hai thuật toán qua định lý.
- **Lý do tồn tại:** bảng §7.5 của ghi chú; NT-RL-4 (trực tuyến và ngoại tuyến, theo và khác chính sách, mỏ neo $\pi_{\mathrm{old}}$ và $\pi_{\mathrm{ref}}$, chiều KL). Bảng trên mặt trang, hình hai con đường ở ghi chú (Q7, QT7).
- **Liên kết:** trước: `L10-D15`; sau: `L10-D17` (khi giả thiết của hàng "Bảo đảm" hỏng).
- **Mục tiêu:** 8, 9.
- **Khối ghi chú:** §7.5 (đoạn đọc hình, bảng, câu sau bảng) (`topic-29`); Nhận xét 10.70 (`topic-30`, đọc thêm) chỉ trong ghi chú diễn giả.
- **Mặt trang:** bảng `Tiêu chí | RLHF với PPO | DPO`, sáu hàng rút từ bảng §7.5 (hàng "Điều kiện dừng" vào ghi chú diễn giả):
  1. “Mục tiêu” | “$\max J_\beta$, $\pi_{\mathrm{ref}}$ cố định” | “cùng mục tiêu”;
  2. “Tối ưu” | “$L^{\mathrm{BT}}$ cho $\hat r$, rồi $\mathcal L^{\mathrm{CLIP}}$ trên $\tilde r$” | “$L^{\mathrm{DPO}}$”;
  3. “Dữ liệu” | “$\mathcal D_{\mathrm{pref}}$ và mẫu trực tuyến của $\pi_{\mathrm{old}}$” | “chỉ $\mathcal D_{\mathrm{pref}}$, ngoại tuyến, khác chính sách”;
  4. “Mô hình” | “$\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic” | “$\pi_\theta$, $\pi_{\mathrm{ref}}$”;
  5. “Mỏ neo, chiều KL” | “$\pi_{\mathrm{ref}}$, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$; thêm $\pi_{\mathrm{old}}$ của phép cắt” | “chỉ $\pi_{\mathrm{ref}}$, cùng chiều KL”;
  6. “Bảo đảm” | “nghiệm của $J_\beta$ là $\pi^*_{\hat r}$; mỗi bước: gradient đúng tại $\theta_{\mathrm{old}}$ khi lợi thế đúng; không bảo đảm hội tụ” | “cực tiểu là $\pi^*_{\hat r}$ dưới (H1)–(H3), (H4a), (H4b); hạ gradient không bảo đảm hội tụ”.
- **Mật độ:** khoảng 79 âm tiết (bảng tính một dòng, gồm hàng đầu cột; sau cổng III.2 ô "Bảo đảm" của PPO theo đúng chữ ghi chú; trần 80 của bảng so sánh, `deck_lint` nhận tiêu đề "So sánh …"). Hàng "Điều kiện dừng" của ghi chú (hai cột đều là ngân sách, không phân biệt hai phương pháp) và cụm "phần thưởng đã trừ KL" (viết $\tilde r$) vào ghi chú diễn giả để giữ trần 80; bảy hàng đủ cho khoảng 89. Nếu vẫn vượt 80 hoặc chạm chân trang: (1) hàng 5 cột DPO thành "chỉ $\pi_{\mathrm{ref}}$, cùng chiều"; (2) phương án QT7 (hình thay hàng "Dữ liệu", "Mô hình"), chỉ khi điều phối viên duyệt.
- **Phút:** 1,5. **Quyết định:** thêm.
- **Ghi chú diễn giả:** hàng "Điều kiện dừng": ngân sách số lượt và ngân sách số epoch, cả hai không là tiêu chuẩn hội tụ; luận điểm: hai con đường xuất phát từ cùng $J_\beta$ với $\pi_{\mathrm{ref}}$ cố định; PPO nhắm tới $\pi^*_{\hat r}$ bằng mẫu sinh trực tuyến và bốn mô hình, không bảo đảm hội tụ; DPO giải cùng bài toán trên dữ liệu cố định, không qua PPO hay vòng học tăng cường nào, và cực tiểu của nó là nghiệm của con đường RLHF lý tưởng chỉ dưới (H1)–(H3), (H4a), (H4b); hàng mỏ neo: DPO giữ $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$ của $J_\beta$ qua phép đổi biến; Rafailov và cộng sự (2023, §6.1) viết rằng DPO và PPO tối ưu cùng một mục tiêu; đọc thêm (Nhận xét 10.70, không thuộc nội dung kiểm tra): IPO, cách viết DPO trên MDP mức token, và hai so sánh thực nghiệm đo trên các bài toán khác nhau, nên không cho biết con đường nào tốt hơn. Nguồn: §7.5, bảng so sánh; §7.6, Nhận xét 10.70; Rafailov và cộng sự (2023), §6.1; Xu và cộng sự (2024), §5–6.

#### `L10-D17` Ưu tiên tất định từ ít dữ liệu
- **Vị trí, loại:** mạch 7; ứng dụng khi giả thiết hỏng (phản ví dụ của (H4a)); bước kiểm tra của cụm DPO và của phần 3 luận điểm.
- **Lý do tồn tại:** cho thấy trên số điều xảy ra khi (H4a) hỏng: cả hai con đường lý tưởng đẩy $\pi(y_2)$ về $0$ với mọi $\beta$, và $J_1$ theo phần thưởng thật giảm từ $0{,}5108$ về $0{,}2877$; nêu vì sao dữ liệu thật thường làm hỏng (H4a), (H4b).
- **Liên kết:** trước: `L10-D16` (hàng "Bảo đảm"); sau: `L10-D18` (bài kiểm của cụm mục tiêu có phạt KL).
- **Mục tiêu:** 9 ("nêu hậu quả khi một giả thiết không thỏa").
- **Khối ghi chú:** Tình huống 10.5; Nhận xét 10.69 (`topic-29`).
- **Mặt trang:**
  1. “Phần thưởng thật $r=(\log2;\,0)$, $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\beta=1$; ba phép so sánh đều chọn $y_1$, xác suất $\tfrac8{27}$.”
  2. “$k=n=3$: (H4a) hỏng; $L^{\mathrm{DPO}}=-\log\sigma\bigl(\beta(\theta_1-\theta_2-\log2)\bigr)$ giảm ngặt theo $\theta_1-\theta_2$, với mọi $\beta$.”
  3. bảng (khuôn "chính sách có phạt KL", thêm cột): $\theta_1-\theta_2$ | $\pi_\theta(y_1)$ | $L^{\mathrm{DPO}}$ | $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$ | $J_1$; hàng $2$ | $0{,}8808$ | $0{,}2395$ | $0{,}1228$ | $0{,}4878$; hàng $4$ | $0{,}9820$ | $0{,}0360$ | $0{,}3278$ | $0{,}3528$; hàng $10$ | $0{,}99995$ | $0{,}0001$ | $0{,}4050$ | $0{,}2881$; hàng $\to\infty$ | $\to1$ | $\to0$ | $\to\log\tfrac32$ | $\to0{,}2877$.
  4. “**Diễn giải:** $J_1$ giảm từ $0{,}5108$ của nghiệm thật về $0{,}2877$; KL bị chặn bởi $\log\tfrac32$, còn $r_\theta(y_2)\to-\infty$.”
  5. “RLHF lý tưởng cũng vậy: $L^{\mathrm{BT}}$ không có cực tiểu, nghiệm tiến tới $(1;\,0)$.”
  6. “**Lưu ý:** mỗi cặp thường chỉ gán nhãn một lần, nên (H4a), (H4b) nói chung không thỏa.”
- **Mật độ:** khoảng 60 âm tiết (11, 7, bảng 0, 13, 12, 17), 6 dòng (bảng tính một dòng), 0 công thức hiển thị. Rủi ro chiều cao (bảng năm cột năm hàng): nếu tràn ở 1600×900, dòng 5 ("RLHF lý tưởng cũng vậy …") chuyển vào ghi chú diễn giả, chỉ khi điều phối viên duyệt.
- **Phút:** 1. **Quyết định:** thêm (C2 `L10-D16`).
- **Ghi chú diễn giả:** $J_1$ tính với phần thưởng thật; KL theo chiều của mục tiêu bị chặn, đại lượng không bị chặn là phần thưởng ngầm định của câu thua và KL chiều ngược; với mô hình phần thưởng có điều chuẩn (điều chuẩn $\ell_2$ của Christiano và cộng sự, 2017, §2.2.3) $\hat r$ hữu hạn và nghiệm giữ $\pi(y_2)>0$; Gheshlaghi Azar và cộng sự (2024, §4.2) lập luận, không thành định lý, rằng RLHF trong thực hành tránh được suy biến nhờ điều này; Nhận xét 10.69: (1) khi (H1) hỏng, ví dụ của Xu và cộng sự với $\pi_{\mathrm{ref}}=(0{,}5;\,0{,}5;\,0)$ cho cận dưới $0$ đạt tại $(0{,}1;\,0;\,0{,}9)$, ngoài lớp của (H3); (2) DPO không đánh giá câu trả lời ngoài dữ liệu, còn $\hat r$ có thể sai ở đó; đọc thêm: IPO trên cùng ba so sánh cho $\pi(y_1)=\sigma(\log2+0{,}5)=0{,}7673$ thay cho $1$. Nguồn: Tình huống 10.5, Nhận xét 10.69, 10.70; Gheshlaghi Azar và cộng sự (2024), §4.2, §5; Xu và cộng sự (2024), Định lý 4.1.

#### `L10-D18` Bài tập: nghiệm có phạt KL trên ba câu trả lời
- **Vị trí, loại:** mạch 7; bài tập có "Lời giải:" trên mặt trang (fragment) của cụm mục tiêu có phạt KL và DPO (NT24, kế hoạch B6); bước kiểm tra.
- **Lý do tồn tại:** áp dụng Định lý 10.57 trên ba câu trả lời và nhận ra phần thưởng ngầm định của nghiệm thuộc $[r]$ (nối Mệnh đề 10.63(c)); giữ dữ liệu, câu chữ và kết quả của Bài tập 10.18 (NT24).
- **Liên kết:** trước: `L10-D17`; sau: `L10-700` (mạch "Tổng kết").
- **Mục tiêu:** 8.
- **Khối ghi chú:** Bài tập 10.18 (đề, gợi ý, lời giải) (`topic-26`, theo `outline.md`).
- **Mặt trang:**
  1. “**Câu hỏi:** một lời nhắc, ba câu trả lời, $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, phần thưởng $r=(\log2;\,0;\,0)$ (Bài tập 10.18).”
  2. “(a) Với $\beta=1$, tính $\mathcal Z$, $\pi^*$, $\max J_1$, và kiểm bằng $\mathbb E_{\pi^*}r-D_{\mathrm{KL}}(\pi^*\Vert\pi_{\mathrm{ref}})$.”
  3. “(b) Tính phần thưởng ngầm định $\beta\log(\pi^*/\pi_{\mathrm{ref}})$ và chỉ ra nó thuộc $[r]$.”
  4. fragment: “**Lời giải:** (a) $\pi_{\mathrm{ref}}e^{r}=(1;\,\tfrac14;\,\tfrac14)$, $\mathcal Z=\tfrac32$, $\pi^*=(\tfrac23;\,\tfrac16;\,\tfrac16)$, $\max J_1=\log\tfrac32=0{,}4055$.”
  5. fragment: “Kiểm: $\mathbb E_{\pi^*}r=0{,}4621$, $D_{\mathrm{KL}}=0{,}1918-0{,}1352=0{,}0566$, hiệu $0{,}4055$.”
  6. fragment: “(b) $(\log\tfrac43;\,\log\tfrac23;\,\log\tfrac23)=r-\log\tfrac32$: hơn kém $r$ một hằng của lời nhắc, nên thuộc $[r]$.”
- **Mật độ:** khoảng 46 âm tiết, 6 dòng, 0 công thức hiển thị.
- **Phút:** 1. **Quyết định:** thêm; gộp C2 `L10-D17`, `L10-D18` (sai khác 3).
- **Ghi chú diễn giả (đến khoảng 250; NT-RL-10):** năng lực kiểm tra: áp dụng nghiệm dạng đóng với $\pi_{\mathrm{ref}}$ không đều, kiểm bằng đẳng thức (a) của Định lý 10.57, và đọc phần thưởng ngầm định của nghiệm như một phần tử của lớp tương đương. "Gợi ý: $\pi^*$ tỉ lệ với $\pi_{\mathrm{ref}}e^{r/\beta}$; hằng chuẩn hóa là tổng có trọng số $\pi_{\mathrm{ref}}$." Câu (c), tự làm: với $\beta=\tfrac12$, $\pi_{\mathrm{ref}}e^{2r}=(2;\,\tfrac14;\,\tfrac14)$, $\mathcal Z=\tfrac52$, $\pi^*=(0{,}8;\,0{,}1;\,0{,}1)$, $\max J_{1/2}=\tfrac12\log\tfrac52=0{,}4581$. Lỗi thường gặp: chuẩn hóa bằng $\sum_ye^{r(y)/\beta}$ thay cho tổng có trọng số $\pi_{\mathrm{ref}}$ cho $(\tfrac12;\,\tfrac14;\,\tfrac14)$ ở (a); dùng $e^{\beta r}$ thay cho $e^{r/\beta}$ ở (c) cho $\pi^*(y_1)=0{,}5858$, sai chiều tác dụng của $\beta$. Nguồn: Bài tập củng cố, Bài tập 10.18.

### Hành trình khái niệm, mạch 7 (NT8)

| cụm (dạng) | vấn đề | trực quan | ví dụ | phát biểu | ý tưởng chứng minh | ứng dụng | kiểm tra | truyền từ ví dụ sang công thức | gộp hoặc `không áp dụng` | phút |
|---|---|---|---|---|---|---|---|---|---|---:|
| Dữ liệu ưu tiên, mô hình Bradley–Terry (cầu nối; kết quả phụ) | `L10-D00`, `L10-D01` (PPO cần $R_{t+1}$; câu hỏi của mạch) | `L10-D02` dòng 1 | `L10-D01` (dữ liệu), `L10-D02` dòng 6 (Ví dụ 10.24) | `L10-D02` (Định nghĩa 10.53, Mệnh đề 10.54) | `không áp dụng` (kết quả phụ; một dòng trong ghi chú diễn giả) | `L10-D03` (dùng $\hat r$), `L10-D09` bước 2 | `L10-D17` ($k=n$); Bài tập 10.22 của `exercises.md` (về nhà) | bốn trên sáu → $\sigma(\Delta\hat r)=\tfrac23$ → $\Delta\hat r=\log\frac k{n-k}$ | ví dụ sau phát biểu như ghi chú, "Trực quan." đứng trước (NT8) | 2,5 |
| Mục tiêu có phạt KL, nghiệm dạng đóng (cốt lõi; kết quả chính) | `L10-D03` dòng 1–2 | `L10-D03` dòng 3 | `L10-D03` (ba chính sách) | `L10-D03` (Định nghĩa 10.56), `L10-D04` (Định lý 10.57) | `L10-D05` | `L10-D06` | `L10-D18` (Bài tập 10.18, lời giải trên mặt trang) | $(0{,}8;\,0{,}2)$ có $J_1$ lớn nhất trong ba → $\pi_{\mathrm{ref}}e^{\hat r}/\mathcal Z=(\tfrac45;\,\tfrac15)$ | phút gồm `L10-D18` | 6 |
| RLHF với PPO (cốt lõi; thuật toán, hai kết quả phụ) | `L10-D07` dòng 1 ($\mathcal Z$ không tính được) | `L10-D08` "Diễn giải:" (mỏ neo giới hạn bước, mỏ neo cố định quyết định điểm dừng) | `L10-D08` (hai vòng, tính tay) | `L10-D07` (Bổ đề 10.59, Mệnh đề 10.60, (7.1)), `L10-D09` (Thuật toán 10.61) | `không áp dụng` (kết quả phụ, lý do trong ghi chú diễn giả `L10-D07`) | `L10-D16` | `L10-D08` "Lưu ý:"; Bài tập 10.21 của ghi chú (về nhà) | lợi thế $\tfrac13\log2\,(1;\,1;\,-2)$ → bước 3 của Thuật toán 10.61 với một lời nhắc | tay trước giả mã (NT-RL-2): `L10-D08` → `L10-D09`; ứng dụng không có trang riêng (Q7, 19 trang): bảng `L10-D16` đặt thuật toán cạnh DPO, "Trong thực hành" của InstructGPT ở ghi chú diễn giả `L10-D09` | 3,5 |
| DPO, định lý tương đương (cốt lõi; kết quả chính, thuật toán) | `L10-D10` dòng 1 (bốn mô hình, sinh mẫu) | `L10-D10` "Trực quan." | `L10-D10` dòng 2 ($\mathcal Z$ triệt tiêu trên số), `L10-D14` | `L10-D10` (Mệnh đề 10.63), `L10-D11` (Định nghĩa 10.64), `L10-D12` (Định lý 10.65), `L10-D14` (Mệnh đề 10.66), `L10-D15` (Thuật toán 10.67) | `L10-D13` | `L10-D17` (ứng dụng khi (H4a) hỏng); Tình huống 10.4 (ứng dụng khi giả thiết thỏa) chỉ trong ghi chú diễn giả `L10-D12` | `L10-D13` (bỏ (H4b)), `L10-D17` (bỏ (H4a)); Bài tập 10.19, 10.20 của ghi chú (về nhà) | $\log1{,}2-\log0{,}6=\log2$ → $\Delta r_\theta$ → gradient $(-\tfrac16;\,\tfrac16)$ → giả mã | tay trước giả mã: `L10-D14` → `L10-D15` | 7 |
| So sánh và giới hạn (cốt lõi) | `L10-D15` → `L10-D16` (hai thuật toán đã đủ) | `không áp dụng` (bảng đọc lại hai thuật toán) | `L10-D17` | `L10-D16` (bảng) | `không áp dụng` | `L10-D17` | `L10-708` câu 3 (hai mỏ neo) | hàng "Bảo đảm" → giả thiết hỏng ở `L10-D17` | chu trình rút gọn: bảng tổng hợp hai thuật toán đã có hành trình đầy đủ | 2,5 |

Phút theo cụm (cột cuối): cụm 1 = `L10-D01`, `L10-D02` ($1+1{,}5$); cụm 2 = `L10-D03`–`L10-D06` và trang bài tập `L10-D18` ($1+1{,}5+1{,}5+1+1$); cụm 3 = `L10-D07`–`L10-D09` ($1+1{,}5+1$); cụm 4 = `L10-D10`–`L10-D15` ($1+1+1{,}5+1+1{,}5+1$); cụm 5 = `L10-D16`, `L10-D17` ($1{,}5+1$); cộng trang tiêu đề mạch: $0{,}5+2{,}5+6+3{,}5+7+2{,}5=22$. Mỗi cụm cốt lõi có ít nhất một trang nội dung; `L10-D18` là bài có lời giải duy nhất trên mặt trang của mạch (NT24), vì Q7 giữ 19 trang; các cụm RLHF và DPO có bước kiểm tra bằng phản ví dụ hoặc "Lưu ý:" trên mặt trang và bài về nhà của ghi chú.

**Câu nối giữa các trang của mạch 7 (trên mặt trang, NT13):** "PPO cần phần thưởng $R_{t+1}$ từ môi trường" (`L10-620` → `L10-D01`); "chính sách cực đại $\mathbb E_\pi\hat r$ là $(1;\,0)$" (`L10-D02` → `L10-D03`); "RLHF … cực đại hóa $J_\beta$ bằng mẫu, không tính $\mathcal Z_r(x)$" (`L10-D06` → `L10-D07`); "Thuật toán 10.61 cần bốn mô hình và sinh mẫu ở mọi vòng" (`L10-D09` → `L10-D10`); hàng "Bảo đảm" của bảng (`L10-D16` → `L10-D17`).

### Trang đã có phải sửa (giữ mọi `data-slide-id`; Q7, kế hoạch C3)

Chỉ các trang dưới đây đổi; mọi trang cũ khác giữ nguyên mặt trang và ghi chú diễn giả. Câu mới trên các trang này theo NT1–NT28; phần không nhắc tới giữ nguyên.

#### Toàn deck
- `<title>` "Bài 10: TRPO, PPO và DPO" (Q6); tên tệp `lecture-10-trpo-va-ppo.html` giữ nguyên.
- Thêm `section` ngoài thứ bảy (mạch 7, `L10-D00` … `L10-D18`) giữa `section` của mạch 6 và của "Tổng kết"; `L10-700` đổi `id="mach-7"` thành `id="mach-8"`. Tám `section` ngoài.
- Không thêm `data-lecture` (deck đã có, mục 3; ngoại lệ đã biết), không thêm `<style>`; lớp CSS mới chỉ khi cần cho bảng năm cột của `L10-D17`, do điều phối viên thêm vào `lecture-course.css` (NT26).

#### `L10-101` Bìa
- **Sửa:** `h1` “TRPO, PPO và DPO”; `h2` “Tối ưu chính sách miền tin cậy (TRPO), tối ưu chính sách gần kề (PPO) và tối ưu ưu tiên trực tiếp (DPO)”; `h3` giữ. Hộp luận điểm, một câu có điều kiện (NT11, NT-RL-8), bốn dòng hiển thị: “Đường cơ sở giữ kỳ vọng của gradient;<br>sai số hàm thay thế bị chặn theo khoảng cách chính sách,<br>nên TRPO ràng buộc khoảng cách, PPO cắt tỉ số;<br>khi phạt khoảng cách tới chính sách tham chiếu cố định, PPO và DPO nhắm tới cùng một nghiệm.”
- **Lý do:** luận điểm của bài thêm phần thứ ba, ở dạng có điều kiện và đúng mức của Định lý 10.57, 10.65 ("nhắm tới", không "trùng nghiệm"); "khoảng cách" thay "KL" vì bìa không dùng chữ viết tắt chưa giới thiệu (NT9), như phần cũ của luận điểm.
- **Mật độ:** luận điểm khoảng 49 âm tiết (bốn dòng hiển thị 8, 12, 10, 19), cả trang khoảng 71 (đơn vị 11, năm học 6, `h3` 5). `deck_lint.py` chỉ miễn trang bìa có mã `LNN-1-01`, nên báo `SYLL60` ở `L10-101`: ngoại lệ đã biết (mã bìa giữ, mục 3), không phải lỗi mật độ của trang nội dung.
- **Ghi chú diễn giả:** thêm câu: "Phần 7 giữ chính sách gần một chính sách tham chiếu cố định bằng phạt KL; mục tiêu đó có nghiệm dạng đóng, RLHF nhắm tới nghiệm bằng PPO với mẫu trực tuyến, còn DPO (Direct Preference Optimization) cực tiểu hóa một hàm mất mát phân loại trên dữ liệu cố định và cho cùng nghiệm khi các giả thiết của định lý tương đương thỏa." Dòng nguồn thêm "§7".

#### `L10-104` và `L10-104b` Mục tiêu học tập
- **`L10-104`:** giữ sáu dòng và ghi chú diễn giả; phút 1 → 0,5.
- **`L10-104b`** (mới, tách; `data-note-topic-id="lec-10-topic-02"`; tiêu đề “Mục tiêu học tập”; `ol start="7"`): sáu dòng cho mục tiêu 8 và 9 của ghi chú, đủ nghĩa và đủ động từ (NT11), viết bằng lời (NT9; tên tiếng Anh ở trang nội dung dùng lần đầu, trừ chữ viết tắt cần tên đầy đủ):
  7. “Ước lượng mô hình phần thưởng từ dữ liệu ưu tiên theo Bradley–Terry bằng hợp lý cực đại.”
  8. “Chứng minh nghiệm dạng đóng của mục tiêu có phạt KL theo một chính sách tham chiếu cố định.”
  9. “Mô tả ba giai đoạn của học tăng cường từ phản hồi con người (RLHF) với PPO.”
  10. “Phân biệt chính sách cũ của PPO với chính sách tham chiếu.”
  11. “Suy ra hàm mất mát tối ưu ưu tiên trực tiếp (DPO) bằng đổi biến; tính tay một bước.”
  12. “Phát biểu giả thiết để DPO và RLHF cho cùng chính sách tối ưu, và hậu quả khi giả thiết hỏng.”
- **Mật độ `L10-104b`:** khoảng 105 âm tiết (18, 19, 17, 12, 19, 20), 6 dòng: ngoại lệ trần 80 của trang mục tiêu (≤ 120), lý do: NT11 giữ đủ hai mục tiêu nhiều vế của ghi chú; NT17 nêu đúng loại ngoại lệ này. Phương án nếu điều phối viên không nhận: chỉ còn cách tách thêm một trang, trái Q7.
- **Ghi chú diễn giả `L10-104b`:** dòng 7–10 ứng với mục tiêu 8, dòng 11–12 với mục tiêu 9 của ghi chú; sản phẩm kiểm được: $\hat r=(\log2;\,0)$; $\pi^*=(\tfrac45;\,\tfrac15)$ và $\max J_1=0{,}5108$; bốn mô hình của RLHF với PPO; $\pi_{\mathrm{old}}$ giới hạn bước, $\pi_{\mathrm{ref}}$ quyết định nghiệm; gradient DPO $(-\tfrac16;\,\tfrac16)$ và $\pi_\theta(y_1)=0{,}7362$; (H1)–(H3), (H4a), (H4b) và ưu tiên tất định. Tên tiếng Anh: reward model, preference data, KL-regularized objective, reference policy (reference model), reinforcement learning from human feedback, Direct Preference Optimization. Nguồn: Mục tiêu học tập 8–9.
- **Phút:** 0,5.

#### `L10-105` Nội dung
- **Sửa:** tám mục, liên kết `#/1` … `#/8`; mục 7 “Tối ưu chính sách từ phản hồi ưu tiên” (`#/7`), mục 8 “Tổng kết” (`#/8`); dòng đọc trước thêm “Rafailov và cộng sự (2023), §3–5.” (nguồn mà "Hướng dẫn đọc thêm" của ghi chú dẫn cho Mục 7).
- **Mật độ:** khoảng 70 âm tiết (trước 60; trần 80), 9 dòng: ngoại lệ số dòng đã có của trang này (bảng "Ngoại lệ mật độ" ở trên) mở rộng từ 8 lên 9 dòng; `deck_lint.py` không đếm dòng với tiêu đề "Nội dung".
- **Ghi chú diễn giả:** thay câu "Phần 7 đặt mỗi kết quả cạnh giả thiết của nó." bằng "Phần 7 dùng lại phép phạt KL với một chính sách tham chiếu cố định khi phần thưởng chỉ được biết qua so sánh ưu tiên, và giải bằng PPO hoặc DPO. Phần 8 đặt mỗi kết quả cạnh giả thiết của nó."; bỏ câu "Phần II của bài giảng gốc (A3C, DDPG, SAC) thuộc Bài 11." (Q8: Bài 11 đang dựng lại thành bài khác, câu trỏ sai). Nguồn thêm "ghi chú bài giảng Bài 10, §7; Rafailov và cộng sự (2023), §3–5".

#### `L10-109` Vấn đề trung tâm
- **Sửa** (bài toán trung tâm của §1.1 có phần thứ ba, QG4; Q3 "một dòng trên `L10-109`"; quyết định của điều phối viên sau cổng III.2: giữ cấu trúc hộp và danh sách của trang cũ): hộp thêm một dòng hiển thị cho phần thứ ba; năm dòng trả lời của phần 2–6 giữ nguyên chữ.
  Hộp: “Giảm phương sai, giữ kỳ vọng;<br>dùng dữ liệu cũ cho bước lớn, $J$ không giảm;<br>so sánh ưu tiên: gần một chính sách cố định.”
  Danh sách `ol start="2"`: năm dòng cũ, không đổi. Câu trả lời của phần 7 chỉ trong ghi chú diễn giả (kế hoạch C3), vì thêm dòng thứ sáu làm trang vượt 1,5 lần trần.
- **Mật độ:** khoảng 89 âm tiết (bản cũ 80 theo `deck_lint.py`, dòng mới của hộp 9; với "chính sách tham chiếu cố định" trang lên 91, quá 1,5 lần trần, nên dòng mới viết "một chính sách cố định", và ghi chú diễn giả gọi đủ tên "chính sách tham chiếu cố định"), 6 dòng, 1 hộp: ngoại lệ trần 60 (≤ 90), mở rộng ngoại lệ đã có của trang (bảng "Ngoại lệ mật độ" ở trên: trang vấn đề trung tâm theo trần 80); lý do Q3 (giữ cấu trúc, thêm một dòng). Dòng mới viết gọn theo khuôn của hai dòng cũ trong hộp; không ký hiệu mới, không chữ viết tắt (NT9). `deck_lint.py` vẫn báo `STRUCT` "trang 'Vấn đề trung tâm' mở đầu có danh sách" và `SYLL60` ở trang này: ngoại lệ đã biết (deck đã có, cấu trúc giữ theo Q3).
- **Ghi chú diễn giả (≤ 150; trước 154):** "Vấn đề trung tâm có ba phần: giảm phương sai của ước lượng gradient mà vẫn giữ kỳ vọng; dùng lại dữ liệu của $\pi_{\mathrm{old}}$ cho một bước lớn mà chính sách mới không kém chính sách cũ; khi phần thưởng chỉ được biết qua so sánh ưu tiên, cực đại hóa phần thưởng mà vẫn gần một chính sách tham chiếu cố định. Năm dòng ứng với năm phần 2 đến 6. Phần 7 trả lời phần thứ ba: RLHF với PPO và DPO cực đại hóa cùng mục tiêu có phạt KL, và DPO cho cùng nghiệm khi các giả thiết của định lý tương đương thỏa. "Khoảng cách" là biến phân toàn phần hoặc KL trung bình theo phân bố trạng thái của chính sách cũ. Dòng 5: TRPO chỉ còn hai bất đẳng thức kiểm được trên bộ đệm, với bán kính miền tin cậy $\kappa$." (bỏ câu "Dòng 2 ghép hai kết quả …" và câu "Dòng 3 nói về ước lượng gradient …" của bản cũ để giữ ≤ 150; tác tử viết đếm lại). Nguồn giữ, thêm "§1.1 (ba phần)".
- **Không chấp nhận** (cổng III.2): phương án trước của storyboard (chỉ một hộp "Câu hỏi:", năm dòng trả lời vào ghi chú diễn giả).

#### `L10-110` Khung chung
- **Sửa:** tiêu đề “Ba hàng của vấn đề trung tâm” (tiêu đề cũ "Hệ số của hàm điểm và độ lớn bước" chỉ gọi tên hai hàng; NT16); hình `central-problem.svg` (đã có hàng thứ ba từ giai đoạn I); `alt` chép đúng câu mô tả hình của ghi chú §1.1 (ba hàng, hàng thứ ba viền chấm, mũi tên từ khung PPO xuống khung "RLHF với PPO, DPO, phạt KL theo pi ref cố định (Mục 7)"); ba dòng cũ giữ, dòng 3 thành “Hai hàng đầu gặp nhau ở PPO kiểu actor–critic.”, thêm dòng 4 “Hàng thứ ba: phần thưởng từ so sánh ưu tiên, giải bằng PPO hoặc DPO (phần 7).”
- **Mật độ:** khoảng 44 âm tiết (10, 9, 9, 16), 4 dòng, 1 hình.
- **Hình (NT25):** SVG có 11 nhãn cỡ 14,7 trên `viewBox` rộng 1245; ở 1600×900 chữ dưới 16 px. Tác tử viết đo cỡ chữ hiển thị; nếu dưới 16 px, vẽ `img/lec-10/central-problem-slide.svg` cùng dữ liệu, chữ lớn hơn (và bản `-slide-narrow.svg` nếu cần ở 390 px), không sửa SVG của ghi chú.
- **Ghi chú diễn giả:** thêm câu đọc hàng thứ ba: "Hàng thứ ba, viền chấm, nhận PPO làm công cụ: phần thưởng học từ so sánh ưu tiên, phạt KL theo chính sách tham chiếu cố định, rồi giải bằng PPO hoặc DPO." Nguồn giữ.

#### `L10-600`, `L10-620` (mạch 6)
- **`L10-600`:** không sửa. Câu "Kết quả giao cho phần 7 là thuật toán PPO kiểu actor–critic và phạm vi bảo đảm của nó" vẫn đúng: mạch 7 mới dùng Thuật toán 10.49 ở bước 3 của Thuật toán 10.61 và hàng "Bảo đảm" của `L10-D16`. Giữ trang ngoài lượt sửa để không kéo dòng dẫn "Muốn …, phải …" của nó vào phạm vi sửa.
- **`L10-620`:** chỉ ghi chú diễn giả, thêm cuối đoạn: "Mọi phép tính của PPO ở đây dùng phần thưởng $R_{t+1}$ do môi trường trả về sau mỗi hành động." (câu nối một phía; câu nối trên mặt trang ở `L10-D01`, NT13). Ghi chú vẫn dưới 250 (trang lời giải).

#### `L10-700` 8. Tổng kết (trang tiêu đề mạch), điểm vào mạch 8
- **Sửa:** `id="mach-8"`; `span.strand-number` “8.”; `h2` “Tổng kết” (NT15, GC-RL-15, Q3); `p.strand-lead` “Mỗi kết quả của bài đúng dưới một bộ giả thiết riêng.” (11 âm tiết; thay dòng "Muốn dùng đúng …, phải …" bị NT12 cấm); `p.strand-keys` “Kết quả và giả thiết · Sáu phương pháp · Vấn đề trung tâm · Câu hỏi tự kiểm tra” (bỏ "Bài 11", Q8). `data-note-topic-id="lec-10-topic-23"` giữ.
- **Ghi chú diễn giả (40–100):** "Đường cơ sở, lợi thế, critic và GAE tạo phần giảm phương sai; hàm thay thế, chặn cải thiện, miền tin cậy, TRPO và PPO tạo phần giới hạn bước; mô hình Bradley–Terry, mục tiêu có phạt KL, RLHF với PPO và DPO tạo phần thứ ba. Mỗi kết quả được đặt cạnh giả thiết không được bỏ, sáu phương pháp được so trên cùng tiêu chí, và vấn đề trung tâm được trả lời có điều kiện." (bỏ "chuyển sang Bài 11"). Không dòng nguồn mới.

#### `L10-701`, `L10-702`, `L10-702b`, `L10-702c` Kết quả và giả thiết của bài
- **`L10-701`, `L10-702`, `L10-702b`:** mặt trang giữ; ghi chú diễn giả chỉ đổi dòng nguồn "§7.1" thành "§8.1", viết khác nhau để `deck_lint.py` hết `REPEAT`: "§8.1, sáu hàng đầu", "§8.1, năm hàng của Mục 4", "§8.1, bốn hàng của Mục 5–6".
- **`L10-702c`** (mới, tách; `data-note-topic-id="lec-10-topic-23"`; tiêu đề “Kết quả và giả thiết của bài”; P4 `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`), năm hàng của §8.1 thuộc Mục 7, chép đúng ghi chú:
  1. “Hợp lý cực đại của mô hình phần thưởng” | “mô hình Bradley–Terry; $0<k<n$” | $L^{\mathrm{BT}}=-\widehat{\mathbb E}\log\sigma\bigl(\hat r(x,y_w)-\hat r(x,y_l)\bigr)$; “cực tiểu” $\log\frac k{n-k}$;
  2. “Nghiệm có phạt KL” | “$\beta>0$; chính sách chọn tự do theo $x$” | $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$; $J_\beta(\pi)=\mathbb E_x[\beta\log\mathcal Z_r-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r)]$;
  3. “Gradient có phạt KL” | “$\pi_\theta>0$; $\pi_{\mathrm{ref}}>0$” | $\nabla J_\beta=\mathbb E[\tilde r_\theta\nabla\log\pi_\theta]$, $\tilde r_\theta=r-\beta\log\frac{\pi_\theta}{\pi_{\mathrm{ref}}}$;
  4. “Tương đương RLHF và DPO” | “(H1)–(H3), (H4a), (H4b); cực tiểu trên mọi hàm phần thưởng; cùng dữ liệu, $\beta$, $\pi_{\mathrm{ref}}$” | $\arg\min L^{\mathrm{DPO}}=\{\pi^*_{\hat r}\}$;
  5. “Gradient DPO” | “$\pi_{\mathrm{ref}}$ cố định; $\beta>0$” | $-\beta\widehat{\mathbb E}\bigl[\sigma(-\Delta r_\theta)(\nabla\log\pi_\theta(y_w)-\nabla\log\pi_\theta(y_l))\bigr]$.
- **Mật độ `L10-702c`:** khoảng 50 âm tiết (bảng 5 hàng; trần 80 của bảng tổng kết, trần 60 theo `deck_lint.py` cũng đạt). Rủi ro tràn công thức ở 390 px (cột thứ ba): tác tử viết đo theo NT26; được ngắt bằng `aligned` trong ô.
- **Ghi chú diễn giả `L10-702c`:** "Mệnh đề 10.54, Định lý 10.57, Mệnh đề 10.60, Định lý 10.65 và Mệnh đề 10.66 tạo phần thứ ba của bài toán trung tâm. Hai hàng giữa mang luận điểm của phần 7: RLHF với PPO và DPO cùng cực đại hóa $J_\beta$ với $\pi_{\mathrm{ref}}$ cố định, có nghiệm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$; cực tiểu của $L^{\mathrm{DPO}}$ là nghiệm đó chỉ dưới (H1)–(H3), (H4a), (H4b). Giả thiết hay bị bỏ: $0<k<n$, tức không có ưu tiên tất định; $\pi_{\mathrm{ref}}>0$ ở mọi câu trả lời; $\pi_{\mathrm{ref}}$ không lấy đạo hàm." Nguồn: "§8.1, năm hàng của Mục 7".
- **Phút:** `L10-702c` 0,5.

#### `L10-703`, `L10-703b` So sánh sáu phương pháp
- **Kiểm trần:** `L10-703` hiện 67 âm tiết (bảng 51, dòng 16); thêm hai hàng của §8.2 (khoảng 39) thành khoảng 106, vượt 80: tách `L10-703b` (Q7, QT6).
- **`L10-703`:** tiêu đề “So sánh sáu phương pháp”; bốn hàng giữ; bỏ dòng "Cả bốn điều kiện dừng …" (chuyển sang `L10-703b` với "sáu"). Khoảng 51 âm tiết. Ghi chú diễn giả: câu "Cả bốn đều cần dữ liệu của chính sách hiện tại …" giữ (nói về bốn hàng của trang), nguồn "§7.2" thành "§8.2, bốn hàng đầu".
- **`L10-703b`** (mới, tách; `data-note-topic-id="lec-10-topic-23"`; cùng tiêu đề; P4 `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng`):
  1. “RLHF với PPO” | “khớp $\hat r$ bằng $L^{\mathrm{BT}}$; rồi Thuật toán 10.49 với phần thưởng (7.1)” | “$\mathcal D_{\mathrm{pref}}$; câu trả lời sinh trực tuyến bằng $\pi_{\mathrm{old}}$” | “ngân sách số lượt”;
  2. “DPO” | “bước của bộ tối ưu trên $L^{\mathrm{DPO}}$ của mỗi mini-batch” | “$\mathcal D_{\mathrm{pref}}$ cố định, ngoại tuyến” | “số epoch đã định”;
  dòng “Cả sáu điều kiện dừng là ngân sách tính toán, không là tiêu chuẩn hội tụ.”
- **Mật độ `L10-703b`:** khoảng 67 âm tiết (trần 80; `deck_lint.py` nhận "So sánh …").
- **Ghi chú diễn giả `L10-703b`:** "Thuật toán 10.61 và 10.67 dừng theo ngân sách. Bốn phương pháp trước và RLHF với PPO cần dữ liệu của chính sách hiện tại, sinh trực tuyến; DPO dùng $\mathcal D_{\mathrm{pref}}$ cố định do $\pi^{\mathrm{SFT}}$ sinh, ngoại tuyến và khác chính sách, không cần tỉ số $\rho_t$. RLHF với PPO giữ bốn mô hình trong bộ nhớ, DPO hai." Nguồn: "§8.2, hai hàng cuối".
- **Phút:** `L10-703` 1, `L10-703b` 0,5.

#### `L10-704` Các kết luận có bảo đảm
- **Sửa:** thêm hàng thứ tư theo §8.2, bảng thứ hai: “DPO” | “(H1)–(H3), (H4a), (H4b); cực tiểu trên mọi hàm phần thưởng; cùng dữ liệu, $\beta$, $\pi_{\mathrm{ref}}$” | “mọi cực tiểu của $L^{\mathrm{DPO}}$ là $\pi^*_{\hat r}$ của RLHF lý tưởng”.
- **Mật độ:** khoảng 76 âm tiết (trước 54; trần 80 của bảng tổng kết). `deck_lint.py` dùng trần 60 cho tiêu đề này nên báo `SYLL60`: ngoại lệ đã biết (tiêu đề bảng tổng kết không khớp biểu thức của công cụ; NT17 cho 80). `<colgroup style="">` giữ (ngoại lệ P7 đã ghi, mục 5 `NGUYEN-TAC-HOC-PHAN.md`).
- **Ghi chú diễn giả:** thêm "Hàng DPO là Định lý 10.65: một kết luận về cực tiểu của hàm mất mát, không về các bước lặp của hạ gradient." và đổi "Cả ba kết luận đều không khẳng định hội tụ tới chính sách tối ưu." thành "Không kết luận nào trong bốn khẳng định hội tụ của thuật toán thực hành."; nguồn "§7.2" thành "§8.2, bảng thứ hai".

#### `L10-707` Vấn đề trung tâm (trả lời)
- **Sửa:** tiêu đề “Vấn đề trung tâm” (NT15; tiêu đề cũ "Trả lời vấn đề trung tâm" bị `deck_lint.py` báo `STRUCT` "tiêu đề cũ"); dòng "Nguồn: …" chuyển vào ghi chú diễn giả (NT15: nguồn trong ghi chú diễn giả); thêm mục 7 theo phần 6 của §8.3 (sửa sau cổng III.2: đủ "cùng mục tiêu" và "không bảo đảm hội tụ"): “Cùng $\max J_\beta$: PPO nhắm tới $\pi^*_{\hat r}$ bằng mẫu trực tuyến, không bảo đảm hội tụ; $\arg\min L^{\mathrm{DPO}}=\{\pi^*_{\hat r}\}$ dưới (H1)–(H3), (H4a), (H4b).”
- **Mật độ:** khoảng 85 âm tiết (năm dòng cũ 68, dòng mới 17), 6 dòng: ngoại lệ trần 60 (≤ 90), lý do như `L10-109`: sáu phần trả lời có điều kiện, mỗi phần một dòng (NT15 trả lời câu hỏi trung tâm của cả bài). Phương án dự phòng nếu `deck_lint.py` đếm quá 90: dòng 4 cũ "Lợi thế, $\nu$, nghiệm chính xác: hàm thay thế đúng bậc một; sai số, mức giảm bị chặn." rút "hàm thay thế" thành "$\mathcal L$" (đã định nghĩa ở mạch 4).
- **Ghi chú diễn giả:** câu đầu giữ ("Mệnh đề 10.2, 10.3, 10.8 trả lời dòng 2 của vấn đề trung tâm; các dòng sau trả lời dòng cùng số: …", vì `L10-109` giữ danh sách), thêm "dòng 7, Định lý 10.57, 10.65, trả lời dòng thứ ba của hộp."; thêm "Dòng 7: hai con đường cực đại hóa cùng mục tiêu có phạt KL theo chính sách tham chiếu cố định, có nghiệm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$; PPO dùng bốn mô hình; DPO không qua vòng học tăng cường; với ưu tiên tất định, cả hai con đường lý tưởng tiến tới chính sách tất định với mọi $\beta$."; dòng nguồn: "ghi chú bài giảng Bài 10, §8.3; Sutton và Barto (2018); Schulman và cộng sự (2015–2017); Achiam và cộng sự (2017); Rafailov và cộng sự (2023); bài giảng gốc lecture10_policy_gradient_part2.pdf (2025–2026), trang 3–42." Ghi chú khoảng 150; nếu vượt, câu về Nhận xét 10.51 rút gọn.

#### `L10-708` Câu hỏi tự kiểm tra
- **Sửa** (QT8; NT15 tối đa bốn câu): câu 3 thay bằng “Giải thích vì sao $\beta$ của PPO-Penalty không giữ chính sách gần $\pi_{\mathrm{ref}}$.” (câu 3 của §8.4; một phân biệt, NT-RL-9). Ba câu còn lại giữ.
- **Mật độ:** khoảng 56 âm tiết (trước 57), 5 dòng.
- **Ghi chú diễn giả:** lời giải (3) mới: "(3) Định nghĩa 10.43 đo KL tới $\pi_{\mathrm{old}}$, đổi sau mỗi lần cập nhật, nên chỉ giới hạn từng bước; nghiệm cuối do mỏ neo cố định $\pi_{\mathrm{ref}}$ của mục tiêu có phạt KL quyết định (Nhận xét 10.58)."; câu cũ chuyển thành một câu hỏi thêm cuối ghi chú: "Câu hỏi thêm: tỉ lệ cắt bằng $\tfrac33$ có nghĩa mọi mẫu có gradient $0$ không? Không nói chung: tỉ lệ cắt đếm $\lvert\rho-1\rvert>\epsilon$ bất kể dấu, còn tập gradient bằng $0$ phụ thuộc dấu của lợi thế (Mệnh đề 10.40(d), Định nghĩa 10.47)."; dòng nguồn: "ghi chú bài giảng Bài 10, §8.4 (câu 1–3); Nhận xét 10.58 (câu 3); Hệ quả 10.29, Nhận xét 10.38 (câu 4); Mệnh đề 10.40, Định nghĩa 10.47 (câu hỏi thêm)". Ghi chú khoảng 210 âm tiết: là lời giải của bốn câu, NT22 cho đến khoảng 250; `deck_lint.py` báo `NOTES150` vì tiêu đề không chứa "Lời giải": ngoại lệ đã biết.

#### `L10-709` Bài tập về nhà
- **Sửa:** tiêu đề “Bài tập về nhà” (NT15; trang tài liệu tách sang `L10-710`). Bảng ba cột, đầu cột “Mạch” | “Tệp bài tập” | “Ghi chú bài giảng” (rút từ "Bài tập (tệp bài tập)", "Bài tập củng cố (ghi chú)"); bỏ hàng "1. Mở đầu" (không có bài); hàng 2–6 giữ số, thêm “(trên lớp)” sau mọi bài có trên trang chiếu: hàng 2 “10.1 (trên lớp), 10.4, 10.5 (trên lớp), 10.10”, hàng 3 “10.6, 10.7 (trên lớp)”, hàng 4 “10.11 (trên lớp)”, hàng 5 “10.8 (trên lớp), 10.9”, hàng 6 “10.2, 10.12 (trên lớp)”; hàng “7. Tối ưu chính sách từ phản hồi ưu tiên” | “10.22” | “10.18 (trên lớp), 10.19, 10.20, 10.21”; hàng “8. Tổng kết” | “—” | “10.3” (thay hàng "7. Tổng kết và chuyển tiếp"). Bảng khớp bảng mạch của `exercises.md` (hàng 7, 8). Thêm dòng liên kết “Ghi chú bài giảng · Bài tập” (hai liên kết viewer hiện ở `L10-710`, chuyển sang đây theo NT15).
- **Mật độ:** khoảng 71 âm tiết (bảng 65, liên kết 6), 2 dòng: ngoại lệ trần 60 (≤ 90; quyết định của điều phối viên sau cổng III.2), lý do NT15 (đánh dấu "(trên lớp)" nhất quán cho cả bảy bài có trên trang chiếu: 10.1, 10.5, 10.7, 10.8, 10.11, 10.12, 10.18).
- **Ghi chú diễn giả:** "Bài tập 10.13–10.17 và 10.22 nằm trong tệp bài tập của bài, lấy từ bài tập của Sutton và Barto (2018), ở hai mức: nhận biết (10.13, 10.22); tính toán hoặc chứng minh (10.14–10.17). Bài tập 10.22 nối phân phối softmax hai hành động với hàm logistic của mô hình Bradley–Terry. Bài tập 10.14, về biến điều khiển không đổi kỳ vọng của lợi tức, thuộc cả mạch 2 và mạch 6. Bài tập 10.1–10.12 và 10.18–10.21 là mục "Bài tập củng cố" của ghi chú bài giảng, có gợi ý và lời giải tại đó; Bài 10.1, 10.5, 10.7, 10.8, 10.11, 10.12 và 10.18 có phiên bản trên trang chiếu. Bài 10.3 kiểm các kết quả có bảo đảm." Nguồn: "tệp bài tập Bài 10, bảng mạch; ghi chú bài giảng Bài 10, §8.5, Bài tập củng cố".

#### `L10-710` Tài liệu tham khảo
- **Sửa:** tiêu đề “Tài liệu tham khảo” (NT15); bỏ nhãn "Tài liệu đọc:" (`deck_lint.py` báo `LABEL`); bỏ dòng "Bài 11: SPO …, SAM+PPO …" và liên kết tới deck Bài 11 cũ (Q8: không câu nối tới bài sau trong lượt này); hai liên kết viewer chuyển sang `L10-709`. Mặt trang năm dòng theo "Hướng dẫn đọc thêm" của ghi chú:
  1. “Sutton và Barto (2018), §13.4–13.5, §7.1, §12.1–12.3.”
  2. “Schulman và cộng sự (2015), §2–3, Phụ lục C; (2016), §2–3; (2017), §3–5.”
  3. “Achiam và cộng sự (2017), §5; Huang và cộng sự (2022); Engstrom và cộng sự (2020).”
  4. “Rafailov và cộng sự (2023), §3–5, Phụ lục A; Ouyang và cộng sự (2022), §3.”
  5. “Stiennon và cộng sự (2020), §3.4.”
- **Mật độ:** khoảng 56 âm tiết, 5 dòng (trần 80 của trang tài liệu tham khảo, NT17; trần 60 của `deck_lint.py` cũng đạt).
- **Sai khác với NT15:** NT15 đòi một dòng nối sang bài sau; Q8 (tác giả) bỏ dòng đó cho tới khi Bài 11 mới được commit. Q8 thắng (thứ tự ưu tiên của NT, mục 0).
- **Ghi chú diễn giả (thay toàn bộ):** "Giới hạn còn lại của Mục 2–6 là dữ liệu theo chính sách: đường cơ sở và GAE cần lượt do chính sách đang cập nhật sinh ra, và PPO bỏ mỗi đoạn thu sau $K$ epoch. RLHF với PPO giữ giới hạn đó và còn phụ thuộc độ đúng của $\hat r$ trên câu trả lời mới; DPO dùng dữ liệu cố định và chỉ đánh giá các câu trả lời có trong dữ liệu. Định lý tương đương ghép Định lý 1 và Mệnh đề 1 của Rafailov và cộng sự (2023, Phụ lục A.6), nửa đầu chứng minh Định lý 4.1 của Xu và cộng sự (2024) và Mệnh đề 4 của Gheshlaghi Azar và cộng sự (2024, Phụ lục B)." Nguồn: "ghi chú bài giảng Bài 10, §8.6, Hướng dẫn đọc thêm và tài liệu tham khảo". Bỏ mọi câu về Bài 11 (SPO, SAM+PPO, ký hiệu $w_t$, Phần II của bài giảng gốc). `data-note-topic-id="lec-10-topic-23"` giữ; nội dung §8.6 (`topic-24`) chỉ ở ghi chú diễn giả.

#### Chỗ dẫn số mục cũ của ghi chú
Ngoài các trang trên, deck không còn chỗ nào dẫn "§7.x" của ghi chú (các "§7" ở `L10-502`, `L10-502b` là của Schulman và cộng sự (2015), giữ). Tác tử viết kiểm lại bằng `grep -n '§7' lecture-10-trpo-va-ppo.html` sau khi sửa: mọi "ghi chú bài giảng Bài 10, §7.k" còn lại phải là §7 mới (mạch 7).

### Ngoại lệ mật độ và ngoại lệ đã biết của `deck_lint`

**Ngoại lệ mật độ có lý do** (NT17, NT-RL-7; không trang nào vượt 1,5 lần trần; không thu nhỏ chữ, chữ thân bài từ `0.75em`):

| trang | trần | số dự kiến | lý do |
|---|---|---|---|
| `L10-104b` | 80 (mục tiêu) | khoảng 105, 6 dòng | NT11 giữ đủ hai mục tiêu nhiều vế của ghi chú (8, 9); NT17 nêu "trang mục tiêu giữ đúng nghĩa ghi chú" là ngoại lệ thường gặp; Q7 chỉ cho một trang tách |
| `L10-D12` | 60 | khoảng 84, 6 dòng | NT2: năm giả thiết (H1)–(H4b) với lượng từ, điều kiện cùng dữ liệu, kết luận hai tầng; phần 2 của luận điểm; kế hoạch C5 dự liệu đến 90 |
| `L10-707` | 60 | khoảng 85, 6 dòng | sáu phần trả lời có điều kiện của câu hỏi trung tâm, mỗi phần một dòng (NT15); dòng 7 đủ "cùng mục tiêu", "không bảo đảm hội tụ" (cổng III.2) |
| `L10-109` | 60 | khoảng 89, 6 dòng | Q3: giữ cấu trúc hộp và năm dòng của trang cũ, thêm một dòng cho phần thứ ba (cổng III.2); mở rộng ngoại lệ đã có (80) |
| `L10-709` | 60 | khoảng 71, 2 dòng | NT15: "(trên lớp)" cho cả bảy bài có trên trang chiếu (cổng III.2) |
| `L10-D01` | 60 | khoảng 62, 5 dòng | NT9 (tập $\mathcal Y(x)$), NT21 (response, completion) (cổng III.2) |
| `L10-D02` | 60 | khoảng 73, 6 dòng | NT2 ($\mathcal D_{\mathrm{pref}}$ hữu hạn, "mô hình phần thưởng"), NT9 ($n$, $k$, $\Delta\hat r$) (cổng III.2) |
| `L10-D04` | 60 | khoảng 68, 6 dòng | NT2 ("$r$ thực", kết luận (e)), luận điểm phần 1 đủ chữ (cổng III.2) |
| `L10-D07` | 60 | khoảng 81, 6 dòng | NT-RL-3, NT-RL-4 (dạng mức token đủ), NT2 ("dạng một bước", "khả vi"), NT21 (cổng III.2) |
| `L10-D08` | 60 | khoảng 70, 6 dòng | NT9 ($p$, "mỏ neo"), NT23 ("Tính …") (cổng III.2) |
| `L10-D09` | 60 | khoảng 72, 6 dòng |
| `L10-D15` | 60 | khoảng 68, 6 dòng | NT2 (dòng "Giả thiết" của Thuật toán 10.67), NT21 ("offline") (cổng III.2) | NT2 (dòng "Giả thiết" của Thuật toán 10.61) (cổng III.2) |
| `L10-105` | 6 dòng | 9 dòng, khoảng 70 âm tiết | tám mạch và dòng đọc trước; mở rộng ngoại lệ đã có (8 dòng) |

Các trang mới khác dự kiến trong trần (đếm bằng script trên bản nháp, sau cổng III.2): `L10-D03` 58, `L10-D05` 60, `L10-D10` 61, `L10-D13` 60, `L10-D17` 60 sát trần 60; `L10-D06` 34, `L10-D11` 49, `L10-D14` 46, `L10-D18` 46; `L10-D16` khoảng 79 (trần 80): tác tử viết đếm bằng `deck_lint.py` và dùng phương án rút ghi trong mục của trang; không thêm ngoại lệ mới nếu chưa báo điều phối viên. Không trang mới nào quá 6 dòng, quá 3 công thức hiển thị, hay có hộp chữ quá 2 câu; mỗi dòng không quá 20 âm tiết (dòng dẫn trần 25).

**Ngoại lệ đã biết của `deck_lint.py` sau bổ sung** (NT28; mục 3, 5 `NGUYEN-TAC-HOC-PHAN.md`):

- Cấp deck: `STRUCT 8 mạch (cần 5–7)` (Q7, QT1); `STRUCT thiếu data-lecture`, `STRUCT chân trang không kết thúc bằng "Bài NN"` (hệ quả của dòng trước; chân trang đúng "… · Bài 10"), `STRUCT có style="" tĩnh` (`<colgroup>` của `L10-704`, P7) và `STRUCT bìa không có ID LNN-1-01` (`L10-101`): deck đã có, mã giữ.
- Trang đã sửa, do biểu thức tiêu đề của công cụ hẹp hơn NT17: `L10-101` `SYLL60` (bìa; công cụ chỉ miễn bìa mã `LNN-1-01`); `L10-704` `SYLL60` (bảng tổng kết, NT17 trần 80); `L10-708` `NOTES150` (lời giải bốn câu, NT22 đến khoảng 250); các ngoại lệ có lý do ở bảng trên (`L10-104b` vượt 80; `L10-109`, `L10-707`, `L10-709` vượt 60); `L10-109` còn `STRUCT` "trang Vấn đề trung tâm mở đầu có danh sách" (cấu trúc giữ theo Q3).
- Trang cũ không sửa (giữ quy định cũ, mục 3): nhãn "Nhu cầu:" và cụm bị cấm ở `L10-106`, `L10-201`, `L10-207`, `L10-212`, `L10-301`, `L10-305`, `L10-307`, `L10-407`, `L10-501`, `L10-505`, `L10-601`, `L10-607`, `L10-609`, `L10-611`, `L10-617`; dòng dẫn "Muốn …, phải …" ở `L10-200`, `L10-300`, `L10-400`, `L10-500`, `L10-600`; nhãn "Bước k." ở `L10-205`, `L10-404`; `L10-617b` `SYLL60` 63; `L10-618` `NOTES150` 155; `L10-701` `SYLL60` 64 (bảng tổng kết, chỉ đổi dòng nguồn); `REPEAT` ở `L10-108`, `L10-109`, `L10-401` (câu nguồn của bài giảng gốc; nếu `L10-109` đổi ghi chú thì hết).
- Hết sau bổ sung: `STRUCT` tiêu đề cũ ở `L10-700`, `L10-707`; mạch cuối không tên "Tổng kết"; trang cuối không tên "Tài liệu tham khảo"; `L10-109` `NOTES150` (nếu ghi chú mới ≤ 150); `L10-700` `BANNED`; `L10-710` `SYLL60`, `LABEL`; `REPEAT` ở `L10-701`, `L10-702`, `L10-702b`.
- Mọi trang `L10-D00` … `L10-D18`, `L10-702c`, `L10-703b` phải 0 phát hiện, trừ `SYLL60` của các trang có ngoại lệ ở bảng trên (`L10-D01`, `L10-D02`, `L10-D04`, `L10-D07`, `L10-D08`, `L10-D09`, `L10-D12`, `L10-D15`).

### Khuôn bảng cố định (bổ sung, NT-RL-5)

| khuôn | cột | trang |
|---|---|---|
| chính sách có phạt KL | chính sách (hoặc $\theta_1-\theta_2$, $\pi_\theta(y_1)$) · ($L^{\mathrm{DPO}}$ ·) $\mathbb E_\pi\hat r$ hoặc bỏ · $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ · $J_1$ | `L10-D03` (Ví dụ 10.25), `L10-D17` (Tình huống 10.5) |
| so sánh hai con đường | Tiêu chí · RLHF với PPO · DPO | `L10-D16` |
| bảng tổng kết, bảng phương pháp | như phần trên (P4) | `L10-702c`, `L10-703b`, `L10-704` |

Hai trang dùng khuôn thứ nhất có chung hai cột cuối $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ và $J_1$, cùng tên cột; `L10-D17` thay cột "chính sách" bằng hai cột tham số và xác suất, vì chính sách chạy theo $\theta_1-\theta_2$.

### Bài tập trên mặt trang, chứng minh, kỹ thuật (bổ sung)

| cụm | trang đề | trang lời giải | khối của ghi chú | loại | kết quả trên mặt trang (trùng ghi chú) |
|---|---|---|---|---|---|
| Mục tiêu có phạt KL, DPO (mạch 7) | `L10-D18` | `L10-D18` (fragment) | Bài tập 10.18 (a)–(b) | lời giải mẫu trên mặt trang; (c) trong ghi chú diễn giả | $\mathcal Z=\tfrac32$, $\pi^*=(\tfrac23;\,\tfrac16;\,\tfrac16)$, $\max J_1=0{,}4055$, KL $0{,}0566$; $r-\log\tfrac32\in[r]$ |

`exercises.md` không lặp Bài tập 10.18, nên không có dòng "Trùng trang chiếu" mới (BT11). Bài về nhà của mạch 7 (lời giải trong ghi chú hoặc tệp bài tập): 10.19, 10.20, 10.21, 10.22.

- **Kết quả chính** (NT6, trang ý tưởng chứng minh riêng): Định lý 10.57 (`L10-D05`), Định lý 10.65 (`L10-D13`).
- **Kết quả phụ** (lý do không có trang chứng minh ghi trong ghi chú diễn giả của trang phát biểu): Mệnh đề 10.54 (`L10-D02`: hồi quy logistic, đạo hàm $\sigma(\Delta\hat r)-\tfrac kn$), Bổ đề 10.59 và Mệnh đề 10.60 (`L10-D07`: logarit của tích, tính chất tháp; đạo hàm tích và Mệnh đề 09.17), Mệnh đề 10.63 (`L10-D10`: ba bước), Mệnh đề 10.66 (`L10-D14`: quy tắc dây chuyền).
- **Kỹ thuật** (NT7): chỉ một dòng "Kỹ thuật." trên `L10-D05` (gộp phần thưởng vào phân phối $\pi_{\mathrm{ref}}e^{r/\beta}/\mathcal Z_r$ để đọc mục tiêu bằng KL), mẹo chỉ dùng trong một chứng minh. Phép đổi biến (reparameterization) của `L10-D10` là một kết quả có số hiệu (Mệnh đề 10.63), không phải trang kỹ thuật; tên tiếng Anh ở ghi chú diễn giả. Danh sách kỹ thuật đã giới thiệu của deck 10: thêm "gộp phần thưởng vào KL" (`L10-D05`).

### Đối chiếu mã trang (bổ sung)

**Chủ đề mới → trang** (chốt cột "dự kiến" của `outline.md`, mục "Ánh xạ hai chiều"; điều phối viên chép lại vào outline):

| `note-topic-id` | nhóm | khối của ghi chú | trang mang thuộc tính | trang khác dùng |
|---|---|---|---|---|
| `lec-10-topic-25` | cầu nối | §7.1, Định nghĩa 10.52, 10.53, Mệnh đề 10.54, Nhận xét 10.55, Ví dụ 10.23, 10.24 | `L10-D00`, `L10-D01`, `L10-D02` | — |
| `lec-10-topic-26` | cốt lõi | §7.2, Ví dụ 10.25, 10.26, Định nghĩa 10.56, Định lý 10.57, Nhận xét 10.58; Bài tập 10.18 | `L10-D03`, `L10-D04`, `L10-D05`, `L10-D06`, `L10-D18` | Nhận xét 10.58 trên `L10-D08` (thuộc tính `topic-27`) |
| `lec-10-topic-27` | cốt lõi | §7.3, Bổ đề 10.59, Mệnh đề 10.60, Ví dụ 10.27, Thuật toán 10.61, Nhận xét 10.62 | `L10-D07`, `L10-D08`, `L10-D09` | — |
| `lec-10-topic-28` | cốt lõi | §7.4, Mệnh đề 10.63, Định nghĩa 10.64, Định lý 10.65, Mệnh đề 10.66, Ví dụ 10.28, Thuật toán 10.67, Nhận xét 10.68 | `L10-D10` … `L10-D15` | — |
| `lec-10-topic-29` | cốt lõi | §7.5, bảng so sánh, Nhận xét 10.69; Tình huống 10.5 | `L10-D16`, `L10-D17` | Tình huống 10.4 chỉ trong ghi chú (không lên deck) |
| `lec-10-topic-30` | đọc thêm | §7.6, Nhận xét 10.70 | không trang nào | ghi chú diễn giả `L10-D16`, `L10-D17` |
| `lec-10-topic-02` | (đã có) | Mục tiêu 8–9 | `L10-104b` | — |
| `lec-10-topic-23` | (đã có) | §8.1, §8.2 | `L10-702c`, `L10-703b` | — |

Tổng sau bổ sung: 30 chủ đề, 123 `data-slide-id` duy nhất; mọi chủ đề cốt lõi mới (26–29) có trang nội dung; Tình huống 10.4 (ba bản tóm tắt) chỉ ở ghi chú: không có chỗ trong 19 trang, và Định lý 10.65 đã có ví dụ tính tay `L10-D14` trên ví dụ xuyên suốt.

**Kế hoạch C2 → storyboard.**

| C2 | storyboard | quan hệ |
|---|---|---|
| `L10-D00`, `L10-D01` | `L10-D00`, `L10-D01` | giữ |
| `L10-D02` (Định nghĩa 10.53, Mệnh đề 10.54) + `L10-D03` (Ví dụ 10.24) | `L10-D02` | gộp |
| `L10-D04`, `L10-D05`, `L10-D06`, `L10-D07` | `L10-D03`, `L10-D04`, `L10-D05`, `L10-D06` | giữ nội dung, đổi mã |
| `L10-D08` (RLHF với PPO) | `L10-D07` (phần thưởng theo token), `L10-D09` (thuật toán) | tách |
| `L10-D09` (ví dụ hai vòng PPO) | `L10-D08` | giữ nội dung, đặt trước thuật toán |
| `L10-D10`, `L10-D11` | `L10-D10`, `L10-D11` (Mệnh đề 10.66 chuyển đi) | giữ |
| `L10-D12` | `L10-D12` | giữ |
| — | `L10-D13` (ý tưởng chứng minh Định lý 10.65) | thêm |
| `L10-D13`, `L10-D14` | `L10-D14` (thêm Mệnh đề 10.66), `L10-D15` | giữ nội dung, đổi mã |
| `L10-D15`, `L10-D16` | `L10-D16`, `L10-D17` | giữ nội dung, đổi mã; đổi tiêu đề `L10-D17` |
| `L10-D17` + `L10-D18` (Bài tập 10.13 cũ = 10.18) | `L10-D18` | gộp (fragment) |

### Bảng kiểm `quill` (bổ sung; không tạo `quill.json`)

**Outline (thứ tự tiên quyết).** Ký hiệu mới có trước khi dùng: $x$, $y$, $\mathcal Y(x)$, $\pi_{\mathrm{ref}}$, $y_1$, $y_2$, $y_w$, $y_l$, $\mathcal D_{\mathrm{pref}}$ (`L10-D01`); $\sigma$, $\Pr(y\succ y'\mid x)$, $[\hat r]$, $\hat r$, $L^{\mathrm{BT}}$, $n$, $k$, $\Delta\hat r$ (`L10-D02`, định nghĩa tại dòng dùng); $\beta$ (nghĩa mới), $J_\beta$, $J_1$ (`L10-D03`); $\mathcal Z_r$, $\pi^*_r$ (`L10-D04`); phần thưởng đã trừ KL (`L10-D06`, tên), $\tilde r_\theta$, dạng mức token, (7.1) (`L10-D07`); $p=\pi(y_1)$, mỏ neo (`L10-D08`, định nghĩa trên mặt trang); $\pi^{\mathrm{SFT}}$, SFT (`L10-D09`); $r_\pi$ (`L10-D10`); $r_\theta$, $\Delta r_\theta$, $L^{\mathrm{DPO}}$ (`L10-D11`); (H1)–(H4b) (`L10-D12`). Trang tổng quan dùng lời: `L10-101` không dùng "KL", `L10-104b` và `L10-109` không dùng ký hiệu mới. $\mathcal Z_r$ và (e) của Định lý 10.57 có trên `L10-D04` trước khi `L10-D13` dùng. $\beta$ đã có nghĩa hệ số phạt của PPO-Penalty (`L10-607`); `L10-D03` dùng lại chữ với mỏ neo $\pi_{\mathrm{ref}}$, và `L10-D08`, `L10-708` câu 3 nói rõ hai hệ số đo KL tới hai chính sách khác nhau.

**Threads (sợi mở và đóng).**

| sợi | mở | đóng |
|---|---|---|
| PPO cần phần thưởng của môi trường | `L10-620` (ghi chú diễn giả), `L10-D01` | `L10-D02` ($\hat r$ học từ so sánh), `L10-D07` ((7.1)) |
| Phạt KL của PPO-Penalty chỉ giữ từng bước | `L10-D03` dòng 2 | `L10-D08` (Nhận xét 10.58), `L10-D16` hàng mỏ neo, `L10-708` câu 3 |
| $(0{,}8;\,0{,}2)$ tốt nhất trong ba chính sách | `L10-D03` | `L10-D06` ($\pi^*=(\tfrac45;\,\tfrac15)$), `L10-D08` (PPO dừng ở đó), `L10-D14` (DPO tiến về đó) |
| $\mathcal Z_r(x)$ không tính được | `L10-D05` (ghi chú diễn giả), `L10-D07` dòng 1 | `L10-D10` ($\mathcal Z$ triệt tiêu), `L10-D11` |
| Chỉ hiệu phần thưởng được xác định, lớp $[r]$ | `L10-D02` | `L10-D10` (c), `L10-D13` bước 3–4, `L10-D18` (b) |
| $k=n$ không có cực tiểu | `L10-D02` dòng 5 | `L10-D17`, `L10-707` dòng 7 (ghi chú diễn giả) |
| Bốn mô hình và sinh mẫu ở mọi vòng | `L10-D09` | `L10-D10` dòng 1, `L10-D15` (hai mô hình), `L10-D16` hàng mô hình |
| Cùng mục tiêu, cùng nghiệm khi đủ giả thiết (luận điểm) | `L10-101`, `L10-D04` "Ý nghĩa:" | `L10-D12` "Ý nghĩa:", `L10-D16`, `L10-702c`, `L10-707` dòng 7 |

**Concept (năng lực kiểm tra, thuật ngữ).** Năng lực kiểm được của mạch 7: tính nghiệm có phạt KL và kiểm đẳng thức (a) (`L10-D06`, `L10-D18`); tách vai hai mỏ neo trên một ví dụ PPO (`L10-D08`); tính một bước DPO (`L10-D14`); nhận ra giả thiết hỏng (`L10-D13`, `L10-D17`). Thuật ngữ thống nhất với bảng Việt–Anh của `outline.md` và ghi chú: "lời nhắc", "câu trả lời", "chính sách tham chiếu", "mô hình phần thưởng", "dữ liệu ưu tiên", "phép so sánh ưu tiên", "câu trả lời được chọn/bị loại", "hàm phân hoạch", "mục tiêu có phạt KL", "phần thưởng đã trừ KL", "phần thưởng ngầm định", "học tăng cường từ phản hồi con người", "tối ưu ưu tiên trực tiếp", "tinh chỉnh có giám sát", "mỏ neo", "ưu tiên tất định", "ngoại tuyến/trực tuyến", "theo chính sách/khác chính sách", "token" (giữ nguyên).

### Câu chữ dự kiến và `no-ai-slop` (chế độ Edit)

Phạm vi: mọi câu trong “…” của phần này (dòng dẫn, từ khóa, mặt trang của 19 trang mới và các trang sửa, câu ghi chú diễn giả viết sẵn). Đã soát: không câu tương phản "không phải X mà là Y", không câu hỏi tu từ (hai câu hỏi trên mặt trang đều trong hộp "Câu hỏi:" và được trả lời trong mạch), không khẩu hiệu hay chuỗi mũi tên, không câu chỉ đường, không "chúng ta", "ta thấy", "hãy", không câu về trạng thái của chính văn bản, không câu nguồn gốc số liệu (VP11–VP24, NT18, NT20). Chỗ đã sửa khi soát: dòng dẫn C1 "Cùng một mục tiêu có phạt KL được giải bằng PPO …" (khái niệm chưa có, khẳng định "được giải" mạnh hơn định lý) thành "… nhắm tới cùng một chính sách"; "Ý nghĩa:" của `L10-D12` "cùng nghiệm, không vòng học tăng cường" thành câu có điều kiện "khi đủ giả thiết, …"; tiêu đề C2 "Giới hạn: ưu tiên tất định" thành cụm danh từ của ghi chú; "Lưu ý:" của `L10-D08` giữ con số ($\tfrac23(1+\epsilon)=0{,}8$) thay cho câu "PPO tới đúng nghiệm". Các câu "Diễn giải:" chỉ dùng số có trên chính trang (NT19). Tác tử viết soát lại bằng `no-ai-slop` Edit trên HTML và đếm lại âm tiết bằng `deck_lint.py`.

### Câu hỏi đã có quyết định ở cổng storyboard (III.2)

Báo cáo cổng: `III2-cong-storyboard.md` (scratchpad của phiên). Quyết định của điều phối viên:

1. Sai khác 1–7 so với C2: chấp nhận. Phương án một hộp cho `L10-109`: bác; `L10-109` giữ cấu trúc, thêm một dòng (Q3), ngoại lệ khoảng 89.
2. Phát hiện nghiêm trọng (NT2): đã thêm lại giả thiết và thuật ngữ bị bỏ ở `L10-D02` ($\mathcal D_{\mathrm{pref}}$ hữu hạn, "mô hình phần thưởng"), `L10-D04` ("$r$ thực", kết luận (e)), `L10-D07` ("dạng một bước", "khả vi"), `L10-D14` ("như Định nghĩa 10.64").
3. Phát hiện trung bình: $\mathcal Y(x)$ (`L10-D01`), $n$, $k$, $\Delta\hat r$ (`L10-D02`), $p$ và "mỏ neo" (`L10-D08`) có trên mặt trang trước khi dùng; `L10-D07` mở bằng giới hạn của Định lý 10.57 và có dạng mức token đủ; `L10-D09`, `L10-D15` có dòng "Giả thiết"; ô "Bảo đảm" của PPO trên `L10-D16` theo chữ ghi chú; dòng 7 của `L10-707` có "cùng mục tiêu" và "không bảo đảm hội tụ"; `L10-709` đánh dấu "(trên lớp)" cho cả bảy bài.
4. Phát hiện nhẹ đã làm: "Ý nghĩa:" của `L10-D12` nói về cực tiểu; "Ý nghĩa:" của `L10-D04` nêu cùng mục tiêu; "tiến về" ở `L10-D14`; tên tiếng Anh ở `L10-D01`, `L10-D02`, `L10-D07`, `L10-D15`; "Tính …" ở `L10-D08`, tên đại lượng ở dòng 2 `L10-D10`; lượng từ "theo $\theta_1-\theta_2$" ở `L10-D17`; chú thích quy định trong bản phác ghi chú diễn giả được đánh dấu; dòng nguồn `L10-708`; phương án chiều cao `L10-D17`; bước ứng dụng trong bảng hành trình; Tình huống 10.4 vào ghi chú diễn giả `L10-D12`. Không làm (vượt trần): dòng "Nhắc lại:" hồi quy logistic (lý do ở mục `L10-D02`); câu (c) của Bài tập 10.18 trên mặt trang (kế hoạch B6).
5. `L10-110`: đổi tiêu đề; vẽ `central-problem-slide.svg` nếu đo dưới 16 px.

### Sửa sau rà deck (III.5)

Mục này ghi những chỗ deck đã dựng khác storyboard ở trên. Nguồn: báo cáo dựng deck `III3-deck-report.md`, quyết định biên tập của điều phối viên `III5-quyet-dinh-bien-tap.md` và báo cáo của biên tập viên `III5-editor-report.md`. Chỗ nào mục này khác các mục từng trang ở trên thì deck và mục này thắng.

**Số trang.** 127 trang, 127 mã duy nhất, 8 mạch (11, 18, 10, 16, 12, 23, 21, 16). `#/7/1` mở `L10-D00`; `#/8/1` mở `L10-700`.

**Mã mới (bốn trang tách).**

| mã mới | tiêu đề | `data-note-topic-id` | tách từ | nội dung |
|---|---|---|---|---|
| `L10-702d` | Kết quả và giả thiết của bài | `lec-10-topic-23` | `L10-702c` (năm hàng tràn chân trang) | hai hàng của §8.1: tương đương RLHF và DPO; gradient DPO ($\nabla_\theta L^{\mathrm{DPO}}=\dots$, có vế trái, `aligned`) |
| `L10-704b` | Các kết luận có bảo đảm | `lec-10-topic-23` | `L10-704` (hàng DPO tràn) | hàng DPO (Định lý 10.65), đủ giả thiết trên mặt trang, không `colgroup`; `L10-704` trở về ba hàng cũ |
| `L10-D02b` | Ví dụ: khớp mô hình phần thưởng | `lec-10-topic-25` | `L10-D02` | Ví dụ 10.24 theo các bước của ghi chú; Nhận xét 10.55 trong ghi chú diễn giả |
| `L10-D07b` | Phần thưởng đã trừ KL theo token | `lec-10-topic-27` | `L10-D07` (nay tiêu đề "Dạng mức token") | Mệnh đề 10.60 (dạng một bước, "khả vi", công thức hiển thị); (7.1) là hệ quả trên dạng mức token qua Bổ đề 10.59(a) |

Tiêu đề khác đã đổi: `L10-D05` "Ý tưởng chứng minh: nghiệm có phạt KL"; `L10-D13` "Ý tưởng chứng minh: tương đương RLHF và DPO".

**Đối chiếu mã mới với chủ đề** (bổ sung cho mục "Đối chiếu mã trang (bổ sung)"):
- `lec-10-topic-25`: `L10-D00`, `L10-D01`, `L10-D02`, `L10-D02b`.
- `lec-10-topic-27`: `L10-D07`, `L10-D07b`, `L10-D08`, `L10-D09`.
- `lec-10-topic-23`: thêm `L10-702d`, `L10-704b`.

**Thời lượng mạch 7** (22 phút, không đổi):

| trang | D00 | D01 | D02 | D02b | D03 | D04 | D05 | D06 | D07 | D07b | D08 | D09 | D10 | D11 | D12 | D13 | D14 | D15 | D16 | D17 | D18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| phút | 0,5 | 1 | 1 | 1 | 1 | 1,5 | 1,5 | 1 | 0,75 | 0,75 | 1,5 | 1 | 1 | 1 | 1,5 | 1 | 1,5 | 1 | 1,5 | 0,5 | 0,5 |

- D02 + D02b lấy 2 phút (1,5 + 0,5); D07 + D07b lấy 1,5 phút (1 + 0,5).
- Phút thêm đó lấy từ D17 (1 → 0,5) và D18 (1 → 0,5). Lời giải của D18 chữa trong 15 phút bài tập.

**Thời lượng mạch 8** (9 phút, không đổi): `L10-702c` 0,25 + `L10-702d` 0,25 (trước 0,5); `L10-704` 0,25 + `L10-704b` 0,25 (trước 0,5). Cả deck khoảng 135 phút.

**`section.compact`** (lớp mới trong `lecture-course.css`): thu lề `p`/`li`, `line-height` (1,2; ô bảng 1,15), lề công thức hiển thị và lề dưới `h2`. Cỡ chữ không đổi (NT-RL-7). Đây là quy định cục bộ theo P7 của deck 10, điều phối viên chấp nhận ở III.5 (A5). Lớp chỉ còn trên các trang vẫn cần sau khi tách: `L10-D03`, `L10-D04`, `L10-D07`, `L10-D08`, `L10-D09`, `L10-D11`, `L10-D12`, `L10-D14`, `L10-D16`, `L10-D17`.

**Ngoại lệ mật độ hiện hành** (`deck_lint.py --course rl-plan`, 2026-11-19: 71 phát hiện trên 127 trang). Số này thay cho số ở bảng "Ngoại lệ mật độ và ngoại lệ đã biết của `deck_lint`" ở trên. Không trang nào vượt 1,5 lần trần:

| trang | phát hiện | trần | lý do |
|---|---|---|---|
| `L10-101` | 71 | 60 | bìa; công cụ chỉ miễn bìa mã `LNN-1-01` |
| `L10-104b` | 106 | 80 | giữ đủ mục tiêu 8–9 (NT11) |
| `L10-109` | 90 | 60 | Q3: giữ hộp và năm dòng; dòng 2 "dữ liệu cũ, bước lớn, $J$ không giảm;", dòng 3 "so sánh ưu tiên: tăng phần thưởng, gần chính sách cố định." |
| `L10-D01` | 62 | 60 | NT9, NT21 |
| `L10-D02` | 78 | 60 | NT2: Mệnh đề 10.54 đầy đủ, (b) đúng như ghi chú, (c) có $k\in\{0,n\}$ |
| `L10-D04` | 68; `LINES6` 7 | 60; 6 dòng | NT2: Định lý 10.57 (a)–(e); hai công thức hiển thị, mỗi công thức tính một dòng; năm `li` riêng làm trang tràn khoảng 150 px |
| `L10-D05` | 68 | 60 | NT9: "Nhắc lại:" Mệnh đề 10.24(a) |
| `L10-D07` | 66 | 60 | NT-RL-3, NT-RL-4, Bổ đề 10.59 đầy đủ |
| `L10-D08` | 74 | 60 | NT9 ($p$, "mỏ neo"), NT23 |
| `L10-D09` | 84 | 60 | NT2 (giả thiết của Thuật toán 10.61; "câu trả lời mẫu do người gán nhãn viết") |
| `L10-D10` | 63 | 60 | viết đủ "lớp tương đương" |
| `L10-D12` | 90 | 60 | NT2: năm giả thiết, kết luận đánh nhãn (a)–(c) |
| `L10-D13` | 69 | 60 | bước 4 đầy đủ ($\pi=\pi^*_{r_\pi}=\pi^*_{\hat r+f}=\pi^*_{\hat r}$) |
| `L10-D15` | 76 | 60 | NT2, NT-RL-4 (giả thiết; ngoại tuyến, khác chính sách; không tỉ số $\rho_t$) |
| `L10-D16` | 99 | 80 | hàng "Giới hạn" (Nhận xét 10.62, 10.69; r3) |
| `L10-707` | 90 | 60 | sáu câu trả lời có điều kiện; dòng 7 nêu hai mỏ neo và "DPO không sinh mẫu" |
| `L10-708` | ghi chú 181 | 150 | lời giải bốn câu cộng một mệnh đề về hai chiều KL (NT22 cho đến khoảng 250) |
| `L10-709` | 72 | 60 | NT15: đánh dấu "(trên lớp)" cho cả bảy bài có trên trang chiếu |
| `L10-710` | 73 | 60 (công cụ); 80 (NT17) | trang tài liệu tham khảo; biểu thức tiêu đề của công cụ không nhận "Tài liệu tham khảo" |

Sạch: `L10-D02b`, `L10-D07b`, `L10-D03`, `L10-D06`, `L10-D11`, `L10-D14`, `L10-D17`, `L10-D18`, `L10-702c`, `L10-702d`, `L10-704`, `L10-704b`.

Phát hiện cấp deck (đã biết):
- `STRUCT 8 mạch`
- thiếu `data-lecture`
- chân trang
- `style=""` trong `colgroup` của `L10-704`
- mã bìa
- trang "Vấn đề trung tâm" mở đầu có danh sách (Q3)

Các phát hiện còn lại nằm trên trang cũ không sửa, như đã liệt kê ở trên.

**Sai khác khác của deck so với storyboard.**
- `L10-D17`: dòng "RLHF lý tưởng cũng vậy …" chuyển vào ghi chú diễn giả (phương án dự phòng điều phối viên đã duyệt trước). Bảng thêm hàng $2\log2$, nên con số của "Diễn giải:" có trên trang.
- `L10-D16`: hàng "Tối ưu" chuyển vào ghi chú diễn giả; "Dữ liệu" và "Mô hình" gộp thành một hàng; thêm hàng "Giới hạn".
- `L10-110`: hình `central-problem-slide.svg` (nhãn 16,8 px ở 1600×900).
- `L10-708`: bỏ "Câu hỏi thêm" về tỉ lệ cắt; ý đó có ở `L10-619`, `L10-620`.
- Đề xuất sửa ghi chú (NT3, cho tác giả): hàng "Gradient DPO" của bảng §8.1 thiếu vế trái $\nabla_\theta L^{\mathrm{DPO}}=\dots$.
