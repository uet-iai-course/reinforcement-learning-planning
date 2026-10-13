# Storyboard Bài 07

Bản viết lại ngày 2026-10-12 (giai đoạn II), cập nhật 2026-10-14 sau vòng rà soát năm vai và biên tập: khớp deck 7 mạch, 75 trang (69 trang trong 120 phút, 6 trang chữa bài); vòng rà lại 2 (2026-10-14) tách `L07-31e`. Ký hiệu, số liệu và số hiệu kết quả theo ghi chú bài giảng đã commit (`7d686bf`). Mục tiêu học tập đánh số M1–M6 như `outline.md`.

## Bản đồ các mạch

Bảy mạch, trong khoảng 5–7. So với deck cũ (6 mạch), mạch Q-learning và mạch kết luận được tách theo quyết định chung mục 8 ("Bài 07: 7 mạch, tách mạch kết luận khỏi Q-learning"), vì `AGENTS.md` yêu cầu mạch kết luận đứng riêng, mở bằng trang tiêu đề mạch và không đưa khái niệm mới.

| N | Mạch | Loại | Chức năng | Đầu vào | Đầu ra | Đóng góp cho vấn đề trung tâm | Trang tiêu đề | Phút |
|---|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu | mở đầu | Bìa, tiên quyết (hai trang: nhắc lại; ký hiệu), mục tiêu, nội dung, vấn đề trung tâm, khung cập nhật chung | Bảo đảm dạng bảng của Bài 05–06 | Bài toán "không lưu được một ô mỗi trạng thái" và ba điểm đối chiếu (mục tiêu, dữ liệu, chính sách) | Đặt bài toán | bìa `L07-01` | 9 |
| 2 | Hàm giá trị tuyến tính theo đặc trưng | phát triển (khái niệm) | Thay bảng bằng $x(s)^\top w$; đo mức lan; định nghĩa $J_\mu$; nhập nhằng | Bài toán và khung từ mạch 1 | Lớp hàm, $J_\mu$, $\Phi$, sai số xấp xỉ, đặc trưng bốn khối (dùng lại ở mạch 5 và 7) | Biểu diễn dùng chung và cái giá của nó | `L07-M2T` | 22,5 |
| 3 | Monte Carlo gradient với hàm xấp xỉ | phát triển (thuật toán) | Thay $v_\pi$ bằng $G_t$; SGD trên $J_\mu$; thuật toán; định lý hội tụ | $J_\mu$ chứa $v_\pi$ chưa biết | $w_{\mathrm{MC}}$, hình chiếu của $v_\pi$; giả thiết | Dự đoán với mục tiêu không chệch | `L07-M3T` | 17 |
| 4 | TD(0) bán gradient và điểm cố định Bellman chiếu | phát triển (thuật toán + kết quả) | Mục tiêu bootstrap; độ chệch; bán gradient; $b-Aw$; điểm cố định Bellman chiếu; định lý Tsitsiklis–Van Roy; so sánh | Monte Carlo chờ hết lượt, bỏ lượt cắt ngắn | $w_{\mathrm{TD}}$ khác $w_{\mathrm{MC}}$; giả thiết theo chính sách | Dự đoán trực tuyến và đích của nó | `L07-M4T` | 30 |
| 5 | Sarsa bán gradient cho điều khiển | phát triển (thuật toán) + ứng dụng | $\hat q$, $\pi_w$, chuỗi năm trạng thái, Sarsa; hai bài chữa | Cập nhật bán gradient với $\pi$ cố định | Sarsa, số liệu $w_1$, $w_3$ trên chuỗi; mất giả thiết $\pi$ cố định | Điều khiển theo chính sách | `L07-M5T` | 14 |
| 6 | Q-learning bán gradient và bộ ba bất ổn | phát triển (biến thể + khái niệm) | Mục tiêu cực đại; thuật toán; ba cập nhật Q-learning; ví dụ phân kỳ của TD(0) khác chính sách; bộ ba bất ổn | Sarsa và mẫu thứ hai của chuỗi | Q-learning, ba yếu tố, ví dụ $w_n=1{,}08^n$ (TD khác chính sách; Q-learning có phản ví dụ tương tự theo Sutton và Barto §11.2) | Điều khiển khác chính sách và giới hạn | `L07-M6T` | 16 |
| 7 | Tổng kết và chuyển tiếp | kết luận | Bảng kết quả không phải hội tụ (hai trang), bảng khung, bảng phạm vi hội tụ, bài tập tổng hợp Flappy Bird, trả lời vấn đề trung tâm, tự kiểm tra, bài tập về nhà | Kết quả mạch 2–6 | Bảng giả thiết; nối Bài 08 | Trả lời có điều kiện | `L07-M7T` | 11,5 |

Tổng $9+22{,}5+17+30+14+16+11{,}5=120$ phút. Khối 30 phút ngoài 120 phút: chữa `X01`/`X01b` 6, `X02`/`X02b` 7, `X03`/`X03b` 9, trình diễn notebook Lunar Lander hoặc Flappy Bird 8.

Chia chức năng ba bảng của mạch 7 (rà soát MACH 1): `L07-36`, `L07-36b` chỉ gồm kết quả không phải hội tụ (mức lan, nhập nhằng, SGD, $b-Aw$, Bellman chiếu, phân kỳ trong ví dụ hai trạng thái); ba kết quả hội tụ/không bảo đảm chỉ ở `L07-34`; `L07-36c` là khung thuật toán. Bảng sáu hàng thử trên một trang tràn khung 71 px nên tách hai trang ba hàng.

## Cụm khái niệm và sáu bước

| Cụm | Dạng | Mạch | Vấn đề | Trực giác | Ví dụ | Hình thức/thuật toán | Ứng dụng | Kiểm tra | Dữ kiện truyền sang công thức | Phút |
|---|---|---|---|---|---|---|---|---|---|---:|
| K1 Hàm tham số dùng chung | khái niệm | 2 | `L07-04` (Lunar Lander 9 216 ô, Flappy Bird) | `L07-05` | `L07-06` | `L07-08` | `L07-09` (đặc trưng Lunar Lander trong thực hành) | `L07-11b`, `L07-36e` câu 1 | $\Delta w=\alpha e\,x(s)$, mức lan $\alpha e\,x(s')^\top x(s)$ | 10 |
| K2 Bài toán dự đoán, $J_\mu$ | khái niệm | 2 | `L07-07` (Nhu cầu + ví dụ dẫn nhập hai trạng thái, đổi $\mu$) | `L07-07b` (Trực quan.) | `L07-07` (ví dụ dẫn nhập đặt cùng vấn đề, làm cụ thể việc chọn trọng số) | `L07-07b` | `L07-11` (cận $J_\mu$), ghi chú `L07-07b` ($J_{\mathrm{kt}}$ của notebook) | `L07-11b` | $c=2\mu_2$ → $J_\mu$ với $d=1$ | 4,5 |
| K3 Đặc trưng, bốn khối, nhập nhằng | khái niệm | 2 | `L07-09`, `L07-10` (Nhu cầu:) | `L07-10` (Diễn giải của Kronecker) | `L07-10` (Kronecker $k=m=2$), `L07-11` (hai quan sát Lunar Lander) | `L07-10b`, `L07-11` (Mệnh đề) | `L07-10b` ghi chú ($d=785$, $771$), `L07-35` | `L07-11b` (lời giải trên mặt trang) | $\phi\otimes\mathbf 1_a$ → $w^{(3)}_a$ | 9,5 |
| K4 Monte Carlo gradient | thuật toán | 3 | `L07-12` (504 869 chuyển có $G_t$, không có $v_\pi$) | `L07-12` (Trực quan.) | `L07-12` (hai mục tiêu), `L07-14` (một cập nhật, sau định nghĩa chung `L07-13`, trước Mệnh đề SGD và giả mã) | `L07-13`, `L07-15`, `L07-16` | `L07-17` (định lý), ghi chú `L07-16` ($J_{\mathrm{kt}}=2\,190{,}1$) | `X01`/`X01b` (lời giải trên mặt trang, câu (b) kiểm bằng số liệu `L07-14`) | $x(S_t)=(2;1)$, $w_n=(1;-1)$, $G_t=5$ → $(1{,}8;-0{,}6)$ trong công thức (2.1) và thuật toán | 17 |
| K5 TD(0) bán gradient | thuật toán | 4 | `L07-18` (42 lượt cắt ngắn, 7,7 %) | `L07-18` (Trực quan.) | `L07-19` (trước định nghĩa bán gradient và thuật toán) | `L07-18` (mục tiêu), `L07-19b` (Mệnh đề 07.20, độ chệch, đặt sau ví dụ theo thứ tự ghi chú), `L07-20`, `L07-20b` | `L07-20b` (dòng 42 lượt cắt ngắn vẫn dùng được), ghi chú `L07-20b` ($J_{\mathrm{kt}}=1\,855{,}2$) | `L07-20c` (lời giải trên mặt trang) | $\delta_t=-0{,}6$, $w=(0{,}44;0{,}88)$; mục tiêu tính lại $1{,}792$ → độ chệch → số hạng bị bỏ | 12 |
| K6 Điểm cố định Bellman chiếu | khái niệm + kết quả | 4 | `L07-21` (Nhu cầu:) | `L07-21` (Trực quan., hình) | `L07-21` (Ví dụ. hình chiếu Euclid), `L07-23b` (hai trạng thái) | `L07-22`, `L07-23`, `L07-24`, `L07-24b` | `L07-23b` (so $w_{\mathrm{MC}}$ với $w_{\mathrm{TD}}$), `L07-25` | `L07-24c` (lời giải trên mặt trang) | $\Phi=(1;2)$, $d_\pi=(\tfrac12;\tfrac12)$ → $A=0{,}475$ dùng lại ở `L07-24b`, `L07-24c` | 17 |
| K7 So sánh Monte Carlo và TD(0) | tổng hợp | 4 | `L07-25` | không áp dụng: tổng hợp hai cụm đã có trực giác | không áp dụng: số liệu đã có ở `L07-23b` | `L07-25` (bảng) | `L07-25` ghi chú (LSTD 1 622,2 so với 1 481,0) | `L07-36e` câu 2, 3 | — | 1 |
| K8 Sarsa bán gradient | thuật toán | 5 | `L07-26` (Nhu cầu: không biết $p$) | `L07-26` (vòng điều khiển) | `L07-27` (chuỗi, "Nhắc lại:" bốn khối), `L07-30` (một cập nhật, trước công thức) | `L07-28`, `L07-29` | ghi chú `L07-29` (số liệu notebook); `X02`/`X02b` là đối chứng Monte Carlo cho K8 (cùng chuyển đầu $(\mathrm D,0,-1,\mathrm C)$) | `X03`/`X03b` (lời giải trên mặt trang, "Diễn giải:" so mục tiêu $998$ với $1$) | mẫu $(\mathrm D,0,-1,\mathrm C,0)$ → $w_1=(-0{,}2;0{,}6;-1{,}4)$ ở `L07-28`, `L07-29`, `X03b`, `L07-31`, `L07-31d` | 14 |
| K9 Q-learning bán gradient | thuật toán (biến thể) | 6 | `L07-31` (Nhu cầu: hành động thăm dò trong mục tiêu Sarsa) | `L07-31` (Diễn giải: tách hành vi và đích) | `L07-31` (hai mục tiêu trên mẫu thứ hai) | `L07-31b`, `L07-31c` | `L07-31d` (mẫu thứ ba, $\delta=12{,}6$), ghi chú `L07-31c` (notebook) | `L07-31d`/`L07-31e` (Bài tập 07.13, lời giải ở trang kế), `L07-33`/`L07-33b` (c), `L07-35` | $w_1$ của `L07-30` → $\delta=0$, $w_2=w_1$ → $w_3=(7{,}36;-1{,}92;1{,}12)$ so với Sarsa | 7 |
| K10 Bộ ba bất ổn | khái niệm | 6 | `L07-32b` (Nhu cầu: định lý TD(0) cần dữ liệu theo chính sách; Q-learning cập nhật theo hành vi) | `L07-32` (hình tam giác) | `L07-32b`, `L07-32c` (TD(0) dự đoán khác chính sách, $\rho=1$ trên $s_1\to s_2$, $\rho=0$ tại $s_2$; $w_n=1{,}08^n$; Q-learning có phản ví dụ tương tự, Sutton và Barto §11.2) | `L07-32` (Định nghĩa) | `L07-35` (Flappy Bird) | `L07-33`/`L07-33b` (lời giải trên mặt trang) | $\Phi=(1;2)$ dùng lại từ `L07-23b` | 9 |
| K11 Phạm vi hội tụ | tổng hợp | 7 | `L07-M7T` | không áp dụng: tổng hợp | không áp dụng | `L07-36`, `L07-36b` (kết quả không phải hội tụ), `L07-36c` (khung), `L07-34` (hội tụ) | `L07-35` | `L07-35b`, `L07-36e` câu 4 | — | 5 |

Ghi chú về bước:
- K2: ví dụ dẫn nhập đặt cùng trang vấn đề (`L07-07`), trước bước trực giác ở `L07-07b`; ví dụ làm cụ thể việc "ưu tiên trạng thái nào", dữ kiện $c=2\mu_2$ dùng lại ở `L07-11b` với $\mu=(\beta;1-\beta)$.
- K5: công thức mục tiêu (3.1) xuất hiện ở bước trực giác `L07-18` dưới dạng "giữ $R_{t+1}$, thay $G_{t+1}$", trước ví dụ; định nghĩa bán gradient và thuật toán đứng sau ví dụ.
- K10: ví dụ dẫn nhập `L07-32b`/`L07-32c` đặt cùng bước vấn đề, trước trực giác ở `L07-32`: ví dụ làm cụ thể việc "bỏ giả thiết theo chính sách của định lý TD(0)"; dòng kết của `L07-32c` nêu tên ba yếu tố và dẫn thẳng vào định nghĩa.
- K9: trực giác gộp vào dòng "Diễn giải:" của `L07-31` (tách chính sách hành vi và chính sách đích); lý do: một khái niệm biến thể, trang vẫn có một luận điểm.
- Mọi thuật toán (Monte Carlo, TD(0), Sarsa, Q-learning) có bước tính tay trước công thức/giả mã: `L07-14`, `L07-19`, `L07-30`, `L07-31`.

## Bài tập trên trang

| Trang | Loại | Bài tập ghi chú | Cụm |
|---|---|---|---|
| `L07-11b` | lời giải mẫu trên mặt trang (fragment) | 07.3 | K1–K3 |
| `X01`, `X01b` | lời giải mẫu ở trang kế | 07.5 | K4 |
| `L07-20c` | lời giải mẫu trên mặt trang (fragment) | 07.7 | K5 |
| `L07-24c` | lời giải mẫu trên mặt trang (fragment) | 07.8 (b) | K6 |
| `X02`, `X02b` | lời giải mẫu ở trang kế | 07.10 | K8 |
| `X03`, `X03b` | lời giải mẫu ở trang kế | 07.11 | K8 |
| `L07-31d`, `L07-31e` | lời giải mẫu ở trang kế (fragment) | 07.13 | K9 |
| `L07-33`, `L07-33b` | lời giải mẫu ở trang kế | 07.14 | K9–K10 |
| `L07-35`, `L07-35b` | bài tập tổng hợp, lời giải ở trang kế | 07.18 | K11 |
| ghi chú `X03b` | tự làm (gợi ý trong ghi chú diễn giả) | 07.12 | K8 |

## Bảng từng trang

Cột "QĐ" là quyết định so với deck cũ: `giữ | sửa | gộp | tách | thêm | bỏ`. Cột "MT" là mục tiêu học tập được hỗ trợ.

| Mã | Vị trí | Lý do tồn tại, nhu cầu | Trước → sau | MT | QĐ và lý do | Nguồn | Phút |
|---|---|---|---|---|---|---|---:|
| `L07-01` | điểm vào mạch 1 (bìa) | Tên bài, câu luận đề, đơn vị | — → tiên quyết | — | sửa; vòng biên tập 2026-10-14: luận đề nêu cả mục tiêu cập nhật và phân phối dữ liệu (RL 5, PB, MACH 7) | tr. 1 | 1,5 |
| `L07-01b` | mạch 1 | Nhắc lại $G_t$, $v_\pi$, $P_\pi$, $d_\pi$ (stationary distribution), hai điều kiện Robbins–Monro, hội tụ Q-learning dạng bảng với đủ giả thiết | bìa → ký hiệu | M1–M4 | thêm (tách từ `L07-02` cũ); vòng biên tập 2026-10-14: phát biểu Robbins–Monro (PB), thêm $P_\pi$, $d_\pi$ (SV), giả thiết MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$ (TOAN, RL, PB) | tr. 5–20; ghi chú Bài 03, 05, 06 | 1,5 |
| `L07-01c` | mạch 1 | "Ký hiệu:" $\mathcal S$, $m$, $w\in\mathbb R^d$, $\hat v(s,w)$, $\hat q(s,a,w)$, $x(s)$ (feature), xấp xỉ hàm (function approximation), $w_n$, $\alpha_n$, $t$ | nhắc lại → mục tiêu | M1 | thêm (vòng biên tập; MACH 6, PB): khung chung `L07-02` và `L07-03c` dùng $\hat v$, $x^\top w$ trước định nghĩa ở `L07-08`; một trang không đủ chỗ cho cả nhắc lại và ký hiệu (≤ 6 dòng) | ghi chú, Bảng ký hiệu | 1 |
| `L07-03` | mạch 1 | Sáu mục tiêu kiểm tra được | ký hiệu → nội dung | M1–M6 | tách: chỉ giữ mục tiêu; sáu mục tiêu theo ghi chú; vòng biên tập 2026-10-14: thêm "sai phân thời gian (temporal difference)", "gradient đầy đủ (full gradient)" (RL 2) | tr. 2–4 | 1,5 |
| `L07-03b` | mạch 1 | Bảy mạch đánh số khớp `#/N`, dòng đọc trước | mục tiêu → vấn đề trung tâm | — | thêm; vòng biên tập 2026-10-14: đọc trước thống nhất với `L07-36f` (§9.1–9.5, §10.1, §11.1–11.3); ngoại lệ 8 dòng | tr. 2, 21 | 1 |
| `L07-03c` | mạch 1 | Bài toán "học giá trị và chính sách", câu trả lời có điều kiện của mạch 2–6 | nội dung → khung chung | M1–M5 | thêm; vòng biên tập 2026-10-14: thêm "và chính sách" (MACH 8), ghi chú dùng "mạch" | tr. 22–45 | 1,5 |
| `L07-02` | mạch 1 | Khung $w_{n+1}=w_n+\alpha_n(y_t-\hat v)\nabla\hat v$ và ba điểm đối chiếu | vấn đề → mạch 2 | M3 | sửa: đổi tên từ "Từ bảng giá trị đến hàm xấp xỉ", bỏ hai thẻ và nhãn ngoài danh sách, đặt sau `L07-03c` | tr. 3, 27, 32 | 1 |
| `L07-M2T` | điểm vào mạch 2 | Trang tiêu đề mạch | khung chung → giới hạn bảng tra | — | thêm; ngoài hành trình khái niệm (dòng dẫn nêu nhu cầu của cả mạch) | — | 0,5 |
| `L07-04` | mạch 2, K1 vấn đề | Nhu cầu và ví dụ dẫn nhập có số liệu (Lunar Lander, Flappy Bird) | tiêu đề mạch → trực giác | M1 | sửa: "Nhu cầu:", số liệu notebook; khó khăn thứ ba và câu hỏi chuyển sang ghi chú | tr. 22–23; Ví dụ 07.1 | 2,5 |
| `L07-05` | K1 trực giác | Hình bảng và hàm tham số | vấn đề → ví dụ | M1 | sửa: nhãn "Trực quan.", rút gạch đầu dòng | tr. 23 | 1,5 |
| `L07-06` | K1 ví dụ | Một cập nhật lan sang $s'$: $0{,}4$, $0{,}3$ | trực giác → định nghĩa | M1 | sửa: tiền tố "Ví dụ:", bố cục dữ kiện–tính–diễn giải, "trạng thái hai đặc trưng" | tr. 23, 32; Ví dụ 07.2 | 2,5 |
| `L07-08` | K1 hình thức | Định nghĩa xấp xỉ tuyến tính, gradient, mức lan (Mệnh đề 07.2) | ví dụ → bài toán dự đoán | M1 | sửa, đổi chỗ: đặt trước `L07-07` theo thứ tự Mục 1.2–1.3 của ghi chú | tr. 24–26 | 2 |
| `L07-07` | K2 vấn đề + ví dụ dẫn nhập | Ưu tiên trạng thái nào; hai trạng thái, đổi $\mu$ | xấp xỉ tuyến tính → sai số giá trị | M1, M4 | sửa; vòng biên tập 2026-10-14: "Nhu cầu:" viết gọn (PB) | Sutton–Barto §9.2; Ví dụ 07.3 | 2 |
| `L07-07b` | K2 trực giác + hình thức | Định nghĩa $J_\mu$ (value error), $\mu$ là phân phối trên $\mathcal S$, $\Phi$, lớp biểu diễn | ví dụ → thiết kế đặc trưng | M1, M4 | thêm; vòng biên tập 2026-10-14: câu kết dẫn sang đặc trưng ("$\min_wJ_\mu$ do $x$ quyết định"); câu "chưa tính được $J_\mu$" chuyển xuống ghi chú `L07-M3T` (MACH 4) | tr. 23, 27, 34; Định nghĩa 07.5, 07.6 | 2 |
| `L07-09` | K3 vấn đề, K1 ứng dụng | Đặc trưng phải chứa đại lượng quyết định lợi tức; ví dụ CartPole khớp hình; Lunar Lander 9 và 156 | sai số giá trị → cặp $(s,a)$ | M1 | sửa; vòng biên tập 2026-10-14: ví dụ chữ đổi sang CartPole cho khớp hình (SV) | tr. 28–31; Ví dụ 07.4 | 2 |
| `L07-10` | K3 vấn đề + ví dụ | Nhu cầu: với $(\phi(s);\mathbf 1_a)$ hành động tham lam như nhau ở mọi trạng thái (hệ quả Mệnh đề 07.8); "Nhắc lại:" $u\otimes v$; Kronecker $k=m=2$ | thiết kế đặc trưng → bốn khối | M1 | tách; vòng biên tập 2026-10-14: thêm "Nhắc lại:" tích Kronecker và dòng hệ quả (PB); giữ thứ tự theo ghi chú §1.4 (MACH 5) | tr. 31 | 2 |
| `L07-10b` | K3 hình thức | Định nghĩa 07.7, phân tách $\hat q$, Mệnh đề 07.8, "Lưu ý:" cột không độc lập | ví dụ → nhập nhằng | M1 | thêm; vòng biên tập 2026-10-14: "Lưu ý:" bốn khối không đủ hạng cột (SV), ghi chú Fourier $4^4$ (TOAN) | tr. 31 | 2 |
| `L07-11` | K3 ví dụ + hình thức | Hai quan sát Lunar Lander ($z_y$ là độ cao chuẩn hóa); "Định nghĩa." nhập nhằng; Mệnh đề 07.10; sai số xấp xỉ và sai số ước lượng | bốn khối → bài tập | M1 | sửa; vòng biên tập 2026-10-14: thêm định nghĩa nhập nhằng, dòng sai số xấp xỉ/ước lượng (PB), $z_y$ (SV); số hiệu đặt sau phát biểu | tr. 31; Ví dụ 07.6 | 2 |
| `L07-11b` | K1–K3 kiểm tra | Bài tập 07.3 có lời giải | nhập nhằng → mạch 3 | M1 | thêm | Bài tập 07.3 | 1,5 |
| `L07-M3T` | điểm vào mạch 3 | Trang tiêu đề mạch | mạch 2 → mục tiêu mẫu | — | thêm; bước vấn đề của K4 (dòng dẫn nêu đúng nhu cầu thay $v_\pi$) | — | 0,5 |
| `L07-12` | K4 vấn đề + trực giác + ví dụ dẫn nhập | Thiếu $v_\pi$; nhãn mẫu; hai mục tiêu trên cùng mẫu | tiêu đề → định nghĩa | M3 | sửa; vòng biên tập 2026-10-14: chữ Việt ra ngoài KaTeX; $w'$ ghi rõ "sau một cập nhật Monte Carlo" (PB) | tr. 27, 32 | 2 |
| `L07-13` | K4 hình thức | Định nghĩa 07.12, gradient đầy đủ, mục tiêu Monte Carlo | ví dụ → một cập nhật | M3 | gộp: nội dung `L07-13` cũ (lợi tức) gộp với định nghĩa mục tiêu; tính không chệch chuyển ghi chú | tr. 27, 32–34 | 2 |
| `L07-14` | K4 ví dụ tính tay | Một cập nhật Monte Carlo, ba dòng dự đoán–mục tiêu–tham số | định nghĩa → gradient | M2 | sửa; vòng biên tập 2026-10-14: ba dòng thành danh sách HTML, chữ Việt ngoài KaTeX (SV) | tr. 33; Ví dụ 07.8 | 2,5 |
| `L07-15` | K4 hình thức | Mệnh đề 07.14: SGD trên $J_\mu$ | ví dụ → thuật toán | M3 | sửa: "Mệnh đề.", "Ý nghĩa:", "Chứng minh." một dòng | tr. 32–34 | 2,5 |
| `L07-16` | K4 thuật toán | Thuật toán 07.15, bỏ lượt cắt ngắn, mọi lần ghé | gradient → định lý | M2 | sửa: "Đầu vào:"/"Đầu ra:" in đậm; câu hỏi chuyển ghi chú | tr. 33–34 | 2,5 |
| `L07-17` | K4 ứng dụng (định lý) | Định lý 07.17 với "Giả thiết:", "Kết luận:", "Lưu ý:" | thuật toán → chứng minh | M4 | tách: văn xuôi thành danh sách giả thiết; nguồn xuống ghi chú | tr. 34 | 2,5 |
| `L07-17b` | K4 chứng minh | Bổ đề 07.16, cực tiểu duy nhất, bước 4 "Ý tưởng (Bertsekas và Tsitsiklis, 1996)" | định lý → bài tập | M4 | thêm; vòng biên tập 2026-10-14: nhãn ý tưởng ở bước 4 (TOAN 7); có thể rút khi thiếu giờ | Định lý 07.17 | 2,5 |
| `X01` | K4 kiểm tra (đề) | Bài tập 07.5; câu (b) kiểm bằng số liệu `L07-14` | chứng minh → lời giải | M3 | sửa, chuyển từ mạch 6 cũ; vòng biên tập 2026-10-14: thêm phần kiểm bằng số (MACH 12) | HW 4 | 3 (chữa bài) |
| `X01b` | K4 kiểm tra (lời giải) | Lời giải ba câu, $(1{,}8;-0{,}6)$ | đề → mạch 4 | M3 | thêm (tách lời giải) | HW 4 | 3 (chữa bài) |
| `L07-M4T` | điểm vào mạch 4 | Trang tiêu đề mạch | mạch 3 → mục tiêu TD | — | thêm; ngoài hành trình khái niệm | — | 0,5 |
| `L07-18` | K5 vấn đề + trực giác | Bỏ 42 lượt; mục tiêu một bước; sai số TD | tiêu đề → ví dụ | M2, M3 | sửa; vòng biên tập 2026-10-14: Mệnh đề 07.20 chuyển sang `L07-19b` (PB, SV, TOAN 5) | tr. 27, 35–36 | 2 |
| `L07-19` | K5 ví dụ tính tay | Một cập nhật TD(0); mục tiêu tính lại $1{,}792$ | trực giác → bán gradient | M2 | sửa: tiền tố "Ví dụ:", ba dòng | tr. 35–36; Ví dụ 07.9 | 2,5 |
| `L07-19b` | K5 hình thức (kết quả) | Mệnh đề 07.20: với $\pi$, $w$ cố định, mục tiêu TD nói chung chệch; chứng minh một dòng | ví dụ ($1{,}792$) → bán gradient | M3 | thêm (vòng biên tập): theo thứ tự ghi chú Ví dụ 07.9 → Định nghĩa 07.19 → Mệnh đề 07.20; dùng "chệch" (PB) | tr. 27, 35–36; Mệnh đề 07.20 | 1,5 |
| `L07-20` | K5 hình thức | Gradient đầy đủ của $\tfrac12\delta^2$ và Định nghĩa 07.21 | độ chệch → thuật toán | M3 | sửa: đổi tên "Cập nhật bán gradient"; câu kết có điều kiện thay lời chỉ đường | tr. 32, 35–36 | 2 |
| `L07-20b` | K5 thuật toán | Thuật toán 07.22; cắt ngắn vẫn bootstrap, TD dùng được 42 lượt | định nghĩa → bài tập | M2 | sửa; vòng biên tập 2026-10-14: thêm dòng 42 lượt cắt ngắn (PB) | tr. 35–36 | 2 |
| `L07-20c` | K5 kiểm tra | Bài tập 07.7 có lời giải | thuật toán → Bellman chiếu | M3 | thêm. Kế hoạch A ghi phần bỏ $(1{,}08;0)$; dùng $(-1{,}08;0)$ theo ghi chú | Bài tập 07.7 | 2 |
| `L07-21` | K6 vấn đề + trực giác + ví dụ | TD dừng ở đâu; $T_\pi(\Phi w)$ ngoài lớp; hình chiếu Euclid với phần dư | bài tập → hướng trung bình | M4 | sửa; vòng biên tập 2026-10-14: $r_\pi$ trên mặt trang, phần dư $(1;-1)\perp(1;1)$ (PB); hình ghi $\Pi_D$ (RL 13) | tr. 37; HW 5; Ví dụ 07.10 | 2,5 |
| `L07-22` | K6 hình thức | Mệnh đề 07.25: $\mathbb E[\delta x]=b-Aw$ | trực giác → điểm cố định | M4 | sửa: nhãn "Mệnh đề.", "Ý nghĩa:" | HW 5; tr. 37 | 2,5 |
| `L07-23` | K6 hình thức | $\Pi_D$; "Định nghĩa." toán tử Bellman chiếu (projected Bellman operator); Mệnh đề 07.26 với $w$ tổng quát | hướng trung bình → ví dụ | M4 | sửa; vòng biên tập 2026-10-14: thêm định nghĩa (PB, TOAN 6) | HW 5; tr. 43 | 2,5 |
| `L07-23b` | K6 ví dụ / ứng dụng | Hai trạng thái với đặc trưng 1 và 2, đủ bước trung gian ($\bar v=5$, $(I-\gamma P_\pi)\Phi$) | điểm cố định → định lý | M4 | thêm (bổ sung ngoài nguồn, đã duyệt); vòng biên tập 2026-10-14: bước trung gian trong `aligned` (PB); ghi chú $w_{\mathrm{MC}}=\arg\min J_{d_\pi}$ (RL 4) | Ví dụ 07.11; Sutton–Barto §9.4 | 3 |
| `L07-24` | K6 hình thức (định lý) | Định lý 07.29 với đủ giả thiết; tối giản (irreducible), không tuần hoàn (aperiodic) | ví dụ → chứng minh | M4 | tách; vòng biên tập 2026-10-14: tên tiếng Anh (SV, RL 2) | tr. 35–37, 44–45 | 2 |
| `L07-24b` | K6 chứng minh | Bổ đề 07.27, Mệnh đề 07.28; bước 4 "Ý tưởng", "với $\alpha$ đủ nhỏ" | định lý → bài tập | M4 | thêm; vòng biên tập 2026-10-14: TOAN 7; có thể rút khi thiếu giờ | Bổ đề 07.27, Mệnh đề 07.28 | 1,5 |
| `L07-24c` | K6 kiểm tra | Bài tập 07.8 (b) có lời giải: $w_{\mathrm{MC}}=3{,}1$, $w_{\mathrm{TD}}\approx2{,}105$ | chứng minh → so sánh | M4 | thêm; trình bày như lời giải mẫu (SV) | Bài tập 07.8 | 2,5 |
| `L07-25` | K7 tổng hợp | Bảng sáu hàng Monte Carlo–TD(0) | bài tập → mạch 5 | M3, M4 | sửa: bỏ khung câu hỏi (sang `L07-36e`) | tr. 33–37; Nhận xét 07.30 | 1 |
| `L07-M5T` | điểm vào mạch 5 | Trang tiêu đề mạch | mạch 4 → giá trị hành động | — | thêm; bước vấn đề của K8 | — | 0,5 |
| `L07-26` | K8 vấn đề + trực giác | Không biết $p$; nhắc $\varepsilon$-tham lam; vòng điều khiển; $\pi_w$ | tiêu đề → chuỗi | M5 | sửa; vòng biên tập 2026-10-14: hình dùng `figure short` (SV) | tr. 38–39 | 2,5 |
| `L07-27` | K8 ví dụ (môi trường) | Chuỗi năm trạng thái, chú giải nhãn cạnh, "Nhắc lại:" bốn khối, Mệnh đề 07.32 | vòng điều khiển → một cập nhật | M1, M5 | sửa; vòng biên tập 2026-10-14: chú giải nhãn cạnh (SV), "Nhắc lại:" bốn khối (MACH 5, PB) | tr. 40; Ví dụ 07.12 | 3 |
| `L07-30` | K8 ví dụ tính tay | Một cập nhật Sarsa: $\delta=-2$, $w_1$ | chuỗi → mục tiêu Sarsa | M2 | sửa; vòng biên tập 2026-10-14: chú giải nhãn cạnh (SV); ghi chú $\alpha=\kappa/\mathbb E\lVert x\rVert^2$ (RL 6) | HW 8; Ví dụ 07.13 | 3 |
| `L07-28` | K8 hình thức | $\delta_t$, cập nhật, học theo chính sách, Nhận xét 07.34 | ví dụ → thuật toán | M5 | sửa: câu hỏi bỏ (đáp án đã ở `L07-31`), thêm "Nhận xét." | tr. 38–39 | 2,5 |
| `L07-29` | K8 thuật toán | Thuật toán 07.33 | mục tiêu → bài chữa | M2 | sửa: câu phạm vi và nguồn xuống ghi chú | tr. 38–39, 45 | 2,5 |
| `X02` | đối chứng Monte Carlo cho K8 (đề) | Bài tập 07.10: Monte Carlo trên một lượt của chuỗi | thuật toán → lời giải | M2 | sửa, chuyển từ mạch 6 cũ | HW 7 | 3,5 (chữa bài) |
| `X02b` | đối chứng Monte Carlo cho K8 (lời giải) | Bảng ba cập nhật, $\hat q$ cuối | đề → Sarsa ba mẫu | M2 | thêm (tách lời giải) | HW 7 | 3,5 (chữa bài) |
| `X03` | K8 kiểm tra (đề) | Bài tập 07.11: ba cập nhật Sarsa | Monte Carlo lượt → lời giải | M2 | sửa, chuyển; "coi là độc lập" theo ghi chú; bỏ chữ Việt trong KaTeX | HW 8 | 4,5 (chữa bài) |
| `X03b` | K8 kiểm tra (lời giải) | Bảng ba mẫu, hiệu $4{,}128$, tham lam chọn đi phải; "Diễn giải:" mục tiêu Monte Carlo $998$ so với Sarsa $1$ | đề → mạch 6 | M2 | thêm; vòng biên tập 2026-10-14: MACH 3, 11; PB | HW 7–8 | 4,5 (chữa bài) |
| `L07-M6T` | điểm vào mạch 6 | Trang tiêu đề mạch | mạch 5 → mục tiêu Q-learning | — | thêm; ngoài hành trình khái niệm | — | 0,5 |
| `L07-31` | K9 vấn đề + ví dụ | Hành động thăm dò trong mục tiêu Sarsa; hai mục tiêu trên mẫu thứ hai | tiêu đề → định nghĩa | M2, M5 | tách: "Nhu cầu:" và Ví dụ 07.14 | tr. 38, 41; HW 8 | 2 |
| `L07-31b` | K9 hình thức | Định nghĩa 07.35; chính sách hành vi (behavior policy), chính sách đích (target policy) | ví dụ → thuật toán | M5 | thêm; vòng biên tập 2026-10-14: bỏ chữ Việt trong KaTeX (SV), tên tiếng Anh (RL 2) | tr. 38, 41 | 1,5 |
| `L07-31c` | K9 thuật toán | Thuật toán 07.36, "Đầu vào:" liệt kê đủ | định nghĩa → bài tập Q-learning | M2 | thêm (bổ sung ngoài nguồn theo notebook, đã duyệt); vòng biên tập 2026-10-14: liệt kê đầu vào (SV) | Thuật toán 07.36 | 1,5 |
| `L07-31d` | K9 kiểm tra + ứng dụng (đề) | Bài tập 07.13: ba cập nhật Q-learning trên chuỗi, dữ kiện tự chứa | thuật toán → lời giải | M2, M5 | thêm (vòng biên tập, PB); vòng rà lại 2: tách lời giải sang `L07-31e` vì một trang 10 dòng hiển thị (MACH R2) | Bài tập 07.13; HW 8 | 1 |
| `L07-31e` | K9 kiểm tra (lời giải) | Mẫu thứ ba $\delta=12{,}6$, $w_3=(7{,}36;-1{,}92;1{,}12)$, $\hat q(\mathrm D,\cdot,w_3)=(21{,}28;25{,}12)$, so với Sarsa | đề → ví dụ phân kỳ | M2, M5 | thêm (vòng rà lại 2, MACH R2) | Bài tập 07.13 | 1 |
| `L07-32b` | K10 vấn đề + ví dụ | Nhu cầu: định lý TD(0) cần dữ liệu theo chính sách, Q-learning cập nhật theo hành vi; TD(0) dự đoán khác chính sách, $\rho=1$ trên $s_1\to s_2$, $\rho=0$ tại $s_2$; hình một ô chữ lớn | bài tập Q-learning → phép tính | M5 | thêm (Sutton–Barto §11.2, đã duyệt); vòng biên tập 2026-10-14: ghi đúng tên TD khác chính sách (TOAN 2, RL 1, MACH 2, PB, SV); hình mới `two-state-offpolicy.svg`; tách phép tính sang `L07-32c` vì một trang tràn 140 px | Ví dụ 07.15 | 1,5 |
| `L07-32c` | K10 ví dụ (phép tính) | $\delta=0{,}8w_n$, $w_n=1{,}08^n$, Mệnh đề 07.37 với $\gamma>\tfrac12$; dòng "Q-learning có cùng ba yếu tố; phản ví dụ tương tự" | vấn đề → định nghĩa bộ ba | M5 | thêm (tách từ `L07-32b`) | Ví dụ 07.15; Sutton–Barto §11.2 | 1,5 |
| `L07-32` | K10 trực giác + hình thức | Định nghĩa 07.38 với hình tam giác | ví dụ → bài tập | M5 | sửa: hướng khắc phục và nguồn xuống ghi chú; tiêu đề bỏ "(deadly triad)" (đã ở `L07-03`) | tr. 37, 41 | 1,5 |
| `L07-33` | K9–K10 kiểm tra (đề) | Bài tập 07.14: bốn quy tắc; (d) "Monte Carlo gradient tuyến tính" | định nghĩa → lời giải | M5 | tách; vòng biên tập 2026-10-14: tên thống nhất (RL 10); 2 phút (RL 11, SV) | HW 3 | 2 |
| `L07-33b` | K9–K10 kiểm tra (lời giải) | Bảng bốn quy tắc × ba yếu tố | đề → mạch 7 | M5 | thêm; ghi chú (c) nói rõ ví dụ là TD khác chính sách | HW 3 | 2 |
| `L07-M7T` | điểm vào mạch 7 | Trang tiêu đề mạch | mạch 6 → bảng kết quả | — | thêm; ngoài hành trình khái niệm | — | 0,5 |
| `L07-36` | mạch 7 | Bảng kết quả (1): mức lan, nhập nhằng, SGD | tiêu đề → bảng (2) | M1, M3 | sửa; vòng biên tập 2026-10-14: chỉ giữ kết quả không phải hội tụ (MACH 1) | tr. 23, 31–34 | 1 |
| `L07-36b` | mạch 7 | Bảng kết quả (2): $b-Aw$, Bellman chiếu, "Phân kỳ trong ví dụ hai trạng thái" ($\gamma\in(\tfrac12,1)$; chỉ cập nhật $s_1\to s_2$) | bảng (1) → khung chung | M4, M5 | sửa; vòng biên tập 2026-10-14: bỏ hàng hội tụ TD sang `L07-34` (MACH 1); đổi tên hàng 4 (TOAN 3) | tr. 35–43 | 1 |
| `L07-36c` | mạch 7 | Bảng `Phương pháp \| Quy tắc cập nhật \| Dữ liệu dùng \| Điều kiện dừng` | bảng kết quả → phạm vi | M2, M3 | thêm; công thức trong ô không ngắt dòng; có thể rút khi thiếu giờ | Thuật toán 07.15, 07.22, 07.33, 07.36 | 1 |
| `L07-34` | mạch 7 | Bảng phạm vi hội tụ: Monte Carlo gradient tuyến tính; TD(0) "theo chính sách, $\pi$ cố định; tối giản, không tuần hoàn; $\gamma<1$; cột $\Phi$ độc lập; Robbins–Monro"; Sarsa "thiếu: $\pi$ cố định"; Q-learning "phản ví dụ của TD khác chính sách cùng bộ ba" | khung → bài tập tổng hợp | M4, M5, M6 | sửa; vòng biên tập 2026-10-14: TOAN 1, RL 3, PB, RL 1; hàng mạng nơ-ron chuyển vào ghi chú vì bảng chạm đáy khung | tr. 34, 41–44; Nhận xét 07.40 | 1,5 |
| `L07-35` | mạch 7, bài tập tổng hợp (đề) | Năm bước cho Q-learning tuyến tính trên Flappy Bird | phạm vi → lời giải | M5, M6 | tách: thay câu hỏi TD(0) bằng Bài tập 07.18; TD(0) thành ví dụ trong ghi chú diễn giả | Bài tập 07.18; Nhận xét 07.41 | 2 |
| `L07-35b` | mạch 7, lời giải tổng hợp | Năm bước, $d=771$, không suy ra hội tụ | đề → trả lời vấn đề | M5, M6 | thêm | Bài tập 07.18 | 2 |
| `L07-36d` | mạch 7 | Trả lời vấn đề trung tâm song song `L07-03c`, câu kết "Bảo đảm chỉ phủ dự đoán với chính sách cố định", dòng "Nguồn:" | bài tập → tự kiểm tra | M1–M5 | thêm; vòng biên tập 2026-10-14: câu kết phạm vi (MACH 8), ghi chú thêm giả thiết (TOAN) | tr. 22–45 | 1 |
| `L07-36e` | mạch 7 | Bốn câu tự kiểm tra | trả lời → bài tập về nhà | M1, M3, M4 | thêm; gom câu hỏi của `L07-11`, `L07-24`, `L07-25` cũ | HW 1–3 | 1 |
| `L07-36f` | mạch 7 | Bảng `Mạch \| Bài tập`, tài liệu đọc, liên kết ghi chú, "Tệp bài tập: chưa có", nối Bài 08 | tự kiểm tra → Bài 08 | M1–M6 | thêm; vòng biên tập 2026-10-14: quyết định chung mục 4 | ghi chú bài giảng, Bài tập củng cố | 0,5 |

Trang cũ bị bỏ: không có trang nào bị bỏ hẳn; `L07-13` cũ được gộp vào `L07-13` mới (giữ mã), `L07-21` cũ giữ mã.

## Ngoại lệ mật độ

Đếm bằng hai script của phiên: `density.py` (tách theo khoảng trắng, đếm cả dấu câu đứng riêng sau công thức) và `density2.py` (cùng quy tắc nhưng bỏ token chỉ gồm dấu câu, tức đếm âm tiết đúng định nghĩa của `AGENTS.md`). Cột số đo dùng `density2.py`. Tám trang `L07-01b` (56), `L07-11` (58), `L07-12` (52), `X01` (42), `L07-20b` (56), `L07-24b` (43), `X03b` (35), `L07-31b` (54) chỉ bị `density.py` gắn cờ vì token dấu câu hoặc một dòng 21–23 token; theo âm tiết đều dưới trần.

| Trang | Số đo (âm tiết, dòng, tối đa/dòng) | Trần áp dụng | Lý do ngoại lệ |
|---|---|---|---|
| `L07-01` | 51, 4, 29 | bìa | câu luận đề một dòng do điều phối viên chốt (27 âm tiết) |
| `L07-03` | 80, 6, 16 | 80 (trang mục tiêu) | sáu mục tiêu của ghi chú cùng bốn thuật ngữ tiếng Anh lần đầu |
| `L07-03b` | 54, 8, 9 | 80; 8 dòng | bảy mạch và một dòng đọc trước (quyết định chung mục 5 cho trang Nội dung) |
| `L07-03c` | 67, 6, 16 | 80 | trang tổng quan một dòng mỗi mạch |
| `L07-25` | 51, 7, 9 | bảng so sánh 80 | bảng sáu tiêu chí của Nhận xét 07.30 cộng hàng tiêu đề |
| `L07-34` | 75, 5, 19 | bảng so sánh 80 | danh sách giả thiết TD(0) đủ năm mục theo quyết định điều phối viên |
| `L07-36d` | 78, 7, 13 | tổng kết 80; 7 dòng | năm câu trả lời, câu kết phạm vi bảo đảm (MACH 8) và dòng "Nguồn:" bắt buộc |
| `L07-36f` | 69, 10, 10 | tổng kết 80 | bảng `Mạch \| Bài tập` sáu hàng cùng ba dòng bắt buộc |
| `L07-M3T`, `L07-M5T`, `L07-M6T`, `L07-M7T` | dòng dẫn 21, 22, 24, 22 | dòng dẫn ≤ 25 | script áp trần 20 âm tiết/dòng cho mọi trang |

Vòng biên tập 2026-10-14 (trước → sau, `density2.py`): `L07-01b` 50 → 53 (6 dòng, tách phần ký hiệu sang `L07-01c` 50); `L07-11` 48 → 58; `L07-36` 62 và `L07-36b` 61 → 44 và 39 (hàng hội tụ chuyển sang `L07-34`); `L07-34` 69 → 70; `L07-36d` 68 → 78; `L07-32b` 29 → 42, `L07-32c` 30 (mới). Trang mới `L07-19b` 56, `L07-31d` 37. Vòng rà lại 2: `L07-01b` 56, `L07-12` 52, `L07-31d` 20, `L07-31e` 17, `L07-32b` 55 (4 dòng), `L07-32c` 39, `L07-33` 51, `L07-36b` 44.

Trang vượt trần trước khi sửa (đếm cùng script trên deck cũ) và kết quả:

| Trang cũ | Trước (âm tiết, dòng, tối đa/dòng) | Quyết định | Sau |
|---|---|---|---|
| `L07-02` | 85, 6, 27 | tách | `L07-01b` 56; `L07-02` 44 |
| `L07-03` | 87, 12, 16 | tách | `L07-03` 74; `L07-03b` 54 |
| `L07-04` | 92, 6, 23 | sửa | 52, 4, 15 |
| `L07-07` | 67, 5, 22 | tách | `L07-07` 54; `L07-07b` 54 |
| `L07-09` | 71, 5, 27 | sửa | 47, 3, 20 |
| `L07-10` | 68, 7, 19 | tách | `L07-10` 52; `L07-10b` 27 |
| `L07-11` | 86, 5, 26 | tách | `L07-11` 49; `L07-11b` 60 |
| `L07-16` | 68, 7, 20 | sửa | 55, 5, 16 |
| `L07-17` | 84, 3, 38 | tách | `L07-17` 55; `L07-17b` 51 |
| `L07-20b` | 64, 6, 17 | sửa | 56, 5, 18 |
| `L07-23` | 62, 3, 26 | sửa | 42, 3, 16 |
| `L07-24` | 89, 6, 18 | tách | `L07-24` 54; `L07-24b` 40 |
| `L07-25` | 83, 9, 15 | sửa | 47, 7, 9 (ngoại lệ bảng) |
| `L07-28` | 64, 4, 24 | sửa | 49, 4, 20 |
| `L07-29` | 79, 6, 20 | sửa | 57, 6, 15 |
| `L07-32` | 76, 3, 30 | tách | `L07-32b` 33; `L07-32` 59 |
| `L07-33` | 98, 13, 14 | tách | `L07-33` 55; `L07-33b` 50 |
| `L07-34` | 78, 5, 24 | sửa | 72, 6, 18 (ngoại lệ bảng) |
| `L07-35` | 97, 7, 18 | tách | `L07-35` 60; `L07-35b` 47 |
| `L07-36` | 97, 7, 22 | tách | `L07-36` 66; `L07-36b` 64; `L07-36c`–`L07-36f` |
| `X01` | 64, 7, 18 | tách | `X01` 45; `X01b` 40 |

Không còn khối `<style>` cục bộ; không lớp thu nhỏ chữ.

## Thời lượng

Mạch 1: 9; mạch 2: 22,5; mạch 3: 17; mạch 4: 30; mạch 5: 14; mạch 6: 16; mạch 7: 11,5; tổng 120 phút (69 trang). Khối 30 phút ngoài 120 phút: chữa `X01`/`X01b` 6, `X02`/`X02b` 7, `X03`/`X03b` 9, trình diễn notebook 8 (một chính sách học được trên Lunar Lander hoặc Flappy Bird với trình phát `<canvas>`, đọc đường $\lVert w\rVert$). Có thể bỏ khi thiếu giờ: phần trao đổi ở `L07-17b`, `L07-24b`, `L07-36c`; khi đó `L07-31d`/`L07-31e` để sinh viên tự làm (không chuyển vào khối 30 phút vì khối đã đủ 22 + 8 phút). Không bỏ bước của cụm trọng tâm.
