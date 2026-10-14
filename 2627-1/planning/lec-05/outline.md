# Dàn bài Bài 05: Dự đoán phi mô hình

Cập nhật 2026-10-12, đợt sửa theo chuẩn 2026-10-12, giai đoạn II (bộ trang chiếu); cập nhật 2026-10-14 sau năm vai rà soát và rà lại vòng 2. Dàn bài này khớp `2627-1/lecture-05-du-doan-phi-mo-hinh.html` hiện tại và ghi chú bài giảng đã commit (`e251162`). Lý do từng trang, cụm khái niệm, thời lượng và ngoại lệ mật độ nằm trong [storyboard.md](storyboard.md); quyết định, sai lệch và kiểm tra nằm trong [review-log.md](review-log.md). `analysis.md` là hồ sơ lịch sử trước đợt sửa. Mã trang, phút và nhãn mạch bằng chữ cái không xuất hiện trên mặt trang chiếu hay trong ghi chú diễn giả.

## Thông tin chung

- Học phần Học tăng cường, học kỳ 1, năm học 2026–2027; Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội.
- Tiên quyết: lợi tức và hàm giá trị, phương trình Bellman kỳ vọng (Bài 03); đánh giá chính sách bằng quy hoạch động, toán tử $T_\pi$, phần dư Bellman (Bài 04); luật kỳ vọng lặp, luật phương sai toàn phần, luật mạnh số lớn.
- Nguồn chính: bài giảng gốc (2025–2026), trang 15–33; Bài tập tuần 5 (2025–2026); Sutton và Barto (2018), §2.4–2.5, §5.1, §6.1–6.3. Nguồn đối chiếu cho chứng minh: ghi chú bài giảng Bài 05 (Mục 1–5, Tình huống 05.1–05.2).
- Quy mô: **70 trang, 6 mạch, 120 phút** trình chiếu; 30 phút còn lại dùng chữa bài tập và trình diễn notebook thực hành Lunar Lander đã có (`materials/lec-05/thuc-hanh-lunarlander-du-doan-phi-mo-hinh.ipynb`). Deck không thêm chương trình mới.

## Khung lý thuyết chung

- **Bài toán trung tâm.** Ước lượng $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ của một chính sách Markov cố định $\pi$ chỉ từ các lượt sinh theo $\pi$, không nhận mô hình $p$ làm đầu vào (Định nghĩa 05.1).
- **Đối tượng và ký hiệu chung.** $\mathcal S$ hữu hạn gồm trạng thái không kết thúc, $\mathcal S^+$ thêm trạng thái kết thúc; mẫu chuyển $(S_t,A_t,R_{t+1},S_{t+1})$; lượt dừng tại $T$; lợi tức $G_t$, $G_T=0$; giá trị thật $v_\pi$, bảng đang học $V$ (bằng $0$ tại trạng thái kết thúc); bước học $\alpha_n(s)$ với $n$ đếm cập nhật của riêng $s$.
- **Giả thiết chung.** $\pi$ cố định; môi trường Markov dừng; trạng thái quan sát đầy đủ; dữ liệu theo chính sách. Mạch 2 thêm: lượt kết thúc hầu chắc chắn, các lượt độc lập cùng phân phối. Mạch 4 thêm: điều kiện Robbins–Monro theo trạng thái. Mạch 5 bỏ giả thiết "dữ liệu mới tiếp tục đến".
- **Chuỗi định nghĩa → kết quả → phương pháp.** Khung cập nhật $V(s)\leftarrow V(s)+\alpha[Y-V(s)]$ (Định nghĩa 05.10) → mục tiêu Monte Carlo $Y=G_t$ (Định nghĩa 05.3, 05.6, Mệnh đề 05.7, Thuật toán 05.13, Định lý 05.16–05.17) → mục tiêu TD $Y=R_{t+1}+\gamma V(S_{t+1})$ (Định nghĩa 05.20, Thuật toán 05.21) → độ chệch (Mệnh đề 05.25), phương sai (Định lý 05.28), hội tụ (Định lý 05.30) → cập nhật theo lô (Thuật toán 05.32, Mệnh đề 05.33–05.34).
- **Giới hạn áp dụng.** Không áp dụng nguyên văn cho trạng thái không Markov (ô gộp của Lunar Lander), cho lượt bị cắt ngắn với Monte Carlo, cho bước hằng (về hội tụ), cho dữ liệu khác chính sách; chính sách chưa được cải thiện (Bài 06); bảng thay bằng hàm xấp xỉ ở Bài 07.

## Thuật ngữ Việt–Anh của bài

| Tiếng Việt | Tiếng Anh | Lần đầu trên deck |
|---|---|---|
| dự đoán; bài toán dự đoán | prediction | L05-A01 |
| sai phân thời gian (TD) | temporal difference | L05-A01 |
| lợi tức | return | L05-A01 |
| lượt | episode | L05-A04 |
| mẫu chuyển | transition sample | L05-A04 |
| bước học | step size | L05-A07 |
| mục tiêu cập nhật | update target | L05-A07 |
| hầu chắc chắn | almost surely | L05-B03 |
| lượt bị cắt ngắn | truncated episode | L05-B03 |
| lần ghé; lần ghé đầu tiên; mọi lần ghé | visit; first-visit; every-visit | L05-B04 |
| không chệch | unbiased | L05-B12c |
| mục tiêu bootstrap | bootstrap target | L05-C02 |
| sai số TD | TD error | L05-C03 |
| tự chuyển | self-transition | L05-C06 |
| độ chệch | bias | L05-D05b |
| phần dư Bellman | Bellman residual | Bài 04; nhắc ở ghi chú diễn giả L05-D05b, L05-D07 |
| lượt quét | sweep | L05-D09 |
| cập nhật theo lô | batch updating | L05-A07 |
| quá trình phần thưởng Markov thực nghiệm | Markov reward process | L05-D11 |
| ước lượng tương đương chắc chắn | certainty-equivalence estimate | L05-D11 (ghi chú diễn giả) |
| dữ liệu theo chính sách | on-policy | L05-A04 (ghi chú diễn giả) |
| trạng thái kết thúc | terminal state | L05-A04 |
| chính sách Markov dừng | stationary policy | L05-A04 |
| TD một bước, ký hiệu TD(0) | one-step TD | L05-A07 |
| trung bình gia tăng | incremental mean | L05-B07 |
| lịch bước học | step-size schedule | L05-B10 |
| xấp xỉ ngẫu nhiên | stochastic approximation | L05-D07 (ghi chú diễn giả) |
| bán gradient | semi-gradient | L05-A07 (ghi chú diễn giả; Bài 07) |

Tên tiếng Anh đặt ở lần dùng đầu trên mặt trang; khi trang dùng đầu đã ở trần (A03, A06), tên tiếng Anh đặt ở trang định nghĩa (không chệch ở L05-B12c, lượt bị cắt ngắn ở L05-B03, lần ghé đầu tiên ở L05-B04, độ chệch ở L05-D05b). Thống nhất với `planning/quyet-dinh-chuan-2026-10-12.md`: "lần ghé đầu tiên (first-visit)", "hầu chắc chắn", $T_\pi$ chỉ số dưới, $p$ và $r$ chữ thường, "lượt", "Lời giải". Tên ô và trạng thái viết chữ đứng ($\mathrm L,\mathrm S,\mathrm X,\mathrm G,\mathrm A,\mathrm B,\mathrm x_1,\ldots$); hành động $\mathrm{tien}$; dấu thập phân phẩy (`0{,}5`); ngưỡng dừng $\theta$; $\Delta_k(s)$ là "tổng gia số của lượt quét $k$ tại $s$".

## Ví dụ xuyên suốt

- **Tàu đổ bộ thu nhỏ** trên dãy bốn ô $\mathrm L,\mathrm S,\mathrm X,\mathrm G$ (Ví dụ 05.1): tiến với xác suất $0{,}8$, lùi $0{,}2$; $-1$ khi vào $\mathrm L$ (rơi), $+1$ khi vào $\mathrm G$ (nằm yên); $\gamma=1$; $v_\pi=(11/21;\ 19/21)$. Ba lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$, $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$, $e_3:\mathrm S\to\mathrm X\to\mathrm G$. Dùng ở mạch 2 (lợi tức, lần ghé, bốn cấu hình, một lượt Monte Carlo, phương sai mẫu), mạch 3 (một bước TD, TD(0) trên $e_1$, $e_2$), mạch 4 (so sánh, giá trị chuẩn, độ chệch, phương sai) và bài tập tổng hợp ($e_3$, Bài tập 05.8).
- **Dãy bảy ô** $\mathrm L,\mathrm x_1,\mathrm S,\mathrm x_3,\mathrm x_4,\mathrm x_5,\mathrm G$ với $\gamma=0{,}99$ (Ví dụ 05.17–05.18): biến thiên của lợi tức và bảng phương sai.
- **Tám lượt hai trạng thái $\mathrm A$, $\mathrm B$** (Sutton và Barto, Ví dụ 6.4; Ví dụ 05.20–05.22): mạch 5.
- **Lunar Lander** (notebook thực hành, một lần chạy đã nhúng, gymnasium 1.3.0): hai chuyển thật cho tự chuyển và trạng thái kết thúc (L05-C06), cùng các con số $J$ trong ghi chú diễn giả.

## Bản đồ mạch

| N | Mạch (nhãn) | Trang tiêu đề | Trang | Phút | Đầu ra cho mạch sau |
|---|---|---|---|---:|---|
| 1 | Mở đầu (A) | bìa L05-A01 | L05-A01, A04, A06, A02, A03, A07 (6) | 8 | Bài toán, ký hiệu, khung cập nhật chung |
| 2 | Lợi tức và ước lượng Monte Carlo (B) | L05-B00, `#mach-2` | 19 | 34 | Mục tiêu $G_t$, Thuật toán 05.13, hội tụ với $1/N(s)$; giới hạn phải chờ lượt kết thúc |
| 3 | Sai phân thời gian TD(0) (C) | L05-C00, `#mach-3` | 12 | 22 | Mục tiêu một bước, Thuật toán 05.21, trường hợp biên, hai bảng trên $e_1$, $e_2$ |
| 4 | Độ chệch, phương sai và hội tụ (D, phần đầu) | L05-D00, `#mach-4` | 14 | 26 | Mệnh đề 05.25, Định lý 05.28, 05.30 kèm giả thiết |
| 5 | Dữ liệu cố định và cập nhật theo lô (D, phần sau) | L05-DT, `#mach-5` | 9 | 14 | Thuật toán 05.32, hai nghiệm theo lô và tiêu chuẩn |
| 6 | Tổng kết và chuyển tiếp (E) | L05-E00, `#mach-6` | 10 | 16 | Lựa chọn có điều kiện, nối sang Bài 06 |

Tổng 70 trang, 120 phút.

## Mục tiêu học tập

| Mã | Mục tiêu (mặt trang L05-A06) | Kiểm tra trên deck | Bài tập ghi chú |
|---|---|---|---|
| MT1 | Tính lợi tức bằng truy hồi ngược; phân biệt lượt bị cắt ngắn | L05-B03, L05-E04 câu 1 | 05.2 |
| MT2 | Lập tập mẫu theo hai quy tắc lần ghé; tính trung bình | L05-B13/B13b | 05.3 |
| MT3 | Chạy một lượt Monte Carlo với $1/N(s)$ và bước hằng | L05-B09c, B13b, E06b | 05.4, 05.5, 05.8 |
| MT4 | Chạy TD(0) trên một lượt có trạng thái kết thúc và tự chuyển | L05-C10/C10b, E06b | 05.6, 05.7, 05.8 |
| MT5 | Tính độ chệch, phương sai của mục tiêu; nêu giả thiết hội tụ TD(0) | L05-D13/D13b, E04 câu 2–3 | 05.9–05.11, 05.14 |
| MT6 | Tính hai nghiệm theo lô; chọn phương pháp kèm tiêu chuẩn và giả thiết | L05-D12/D12b, E01, E04 câu 4 | 05.12, 05.13, 05.15 |

## Dàn bài từng trang

Cột "Ghi chú" là số hiệu trong ghi chú bài giảng; cột "Nguồn" là trang bài giảng gốc (2025–2026) hoặc mục Sutton và Barto (2018).

### Mạch 1. Mở đầu

| Mã | Tiêu đề | Nội dung chính | Ghi chú | Nguồn |
|---|---|---|---|---|
| L05-A01 | Dự đoán phi mô hình | Bìa: học phần, Bài 05, phụ đề có "dự đoán (prediction)", "sai phân thời gian (temporal difference, TD)"; câu luận đề; năm học; đơn vị | Mục 1 | tr. 1, 15 |
| L05-A04 | Tiên quyết và quy ước | Nhắc lại lợi tức, $v_\pi$, Bellman kỳ vọng, quy hoạch động cần $P_\pi,r_\pi$; ký hiệu $\mathcal S$, $\mathcal S^+$, mẫu chuyển, $V$; giả thiết | Tiên quyết | tr. 3, 15–17; S&B §3.5, §5.1 |
| L05-A06 | Mục tiêu học tập | MT1–MT6 | Mục tiêu học tập | tr. 2 |
| L05-A02 | Nội dung | Sáu mạch, khớp trang tiêu đề mạch và `#/N` | — | tr. 2 |
| L05-A03 | Vấn đề trung tâm | Bài toán một dòng; năm câu trả lời có điều kiện của mạch 2–6, mỗi dòng có tiền tố điều kiện (dòng 4 "Bảng cố định:" với vế độ chệch, dao động và "hội tụ khi bước giảm"); bỏ hình `learning-route.svg` | Mục 1 | tr. 6, 15–16, 28, 33 |
| L05-A07 | Khung chung của quy tắc cập nhật | Bốn dòng: ước lượng mới bằng lời; mục tiêu Monte Carlo; TD một bước, ký hiệu TD(0); cập nhật theo lô (batch updating) | Mục 1.2 | S&B §2.4, §9.3 (ghi chú diễn giả) |

### Mạch 2. Lợi tức và ước lượng Monte Carlo

| Mã | Tiêu đề | Nội dung chính | Ghi chú | Nguồn |
|---|---|---|---|---|
| L05-B00 | (tiêu đề mạch) Lợi tức và ước lượng Monte Carlo | Dòng dẫn, từ khóa | — | — |
| L05-B01 | Ví dụ: tàu đổ bộ thu nhỏ | Nhu cầu "(mô hình chỉ để kiểm tra)"; hình `short-walk.svg`; "tàu đổ bộ thu nhỏ (còn gọi là dãy bốn ô)"; chính sách, phần thưởng, $\gamma=1$; Trực quan Monte Carlo; $e_1$, $e_2$ trong ghi chú diễn giả và hình của L05-B02 | Ví dụ 05.1, Định nghĩa 05.1 | tr. 15–17 |
| L05-B02 | Ví dụ: lợi tức trên hai lượt | Hình `episode-one.svg`, `episode-two.svg`; $G_t$ với $\gamma=1$; Diễn giải | Ví dụ 05.2 | tr. 20, 22, 29 |
| L05-B03 | Lượt và lợi tức | Định nghĩa $T$, $G_t$, $G_T=0$; Mệnh đề truy hồi, Chứng minh; Lưu ý $\gamma=1$, lượt bị cắt ngắn | Định nghĩa 05.3, Mệnh đề 05.4, Bổ đề 05.5 (ghi chú diễn giả) | tr. 17; S&B §3.3–3.4 |
| L05-B04 | Lần ghé đầu tiên và mọi lần ghé | Nhu cầu; bảng hai quy tắc tại $\mathrm S$, $\mathrm X$; Định nghĩa lần ghé, hai quy tắc | Ví dụ 05.3, Định nghĩa 05.6 | tr. 18, 20, 22; S&B §5.1 |
| L05-B04c | Kỳ vọng của lợi tức sau lần ghé | Trực quan; Giả thiết; Mệnh đề $\mathbb E_\pi[G_{t_k}\mid N_e(s)\ge k]=v_\pi(s)$; Chứng minh; Ý nghĩa | Mệnh đề 05.7 | S&B §5.1 |
| L05-B05 | Ước lượng Monte Carlo | Định nghĩa $V_n(s)$; $n$ đếm mẫu riêng; Lưu ý $V_2(\mathrm S)=0$ | Định nghĩa 05.8 | tr. 18 |
| L05-B06 | Ví dụ: trung bình tại $\mathrm X$ khi thêm mẫu thứ ba | Nhu cầu; hai cách tính $1/3$; trục số nội dòng | Ví dụ 05.4 | S&B §2.4 |
| L05-B07 | Trung bình gia tăng | Mệnh đề; Chứng minh; Ý nghĩa: mục tiêu cập nhật, bước học; Lưu ý bộ đếm riêng | Mệnh đề 05.9, Định nghĩa 05.10 (ghi chú diễn giả) | tr. 21; S&B §2.4 |
| L05-B08 | Bước học hằng | Nhu cầu; bảng hai mẫu tại $\mathrm X$; Mệnh đề trọng số; Ý nghĩa | Mệnh đề 05.11 | tr. 20–23; S&B §2.5 |
| L05-B09 | Ví dụ: bốn cấu hình Monte Carlo trên hai lượt | Bảng bốn cấu hình sau $e_1$, $e_2$; Nhận xét hai trục | Ví dụ 05.5, Nhận xét 05.12 | tr. 22, 29; Bài tập tuần 5, bài 5, 7 |
| L05-B09c | Ví dụ: một lượt của Monte Carlo lần ghé đầu tiên | Hai pha trên $e_2$ từ bảng sau $e_1$, bước $1/N(s)$ | Ví dụ 05.6 | S&B §5.1 |
| L05-B10 | Thuật toán dự đoán Monte Carlo | Đầu vào, Đầu ra, Giả thiết, khởi tạo, bước 1 và bước 2–3 thụt lề (đánh số như Thuật toán 05.13) | Thuật toán 05.13 | S&B §5.1 |
| L05-B10b | Thuật toán dự đoán Monte Carlo | "Trong vòng lặp của bước 1:"; bước 4 (duyệt xuôi), bước 5 (điều kiện lần ghé gồm cả phép cập nhật), bước 6; Lưu ý lượt bị cắt và trạng thái kết thúc | Thuật toán 05.13, Nhận xét 05.14 | S&B §5.1 |
| L05-B12 | Ví dụ: sai số của trung bình lần ghé đầu tiên tại $\mathrm S$ | Nhu cầu; phân phối mẫu; $11/21$ "(giải từ mô hình, chỉ để đo sai số)"; $\operatorname{Var}=320/441$; độ lệch chuẩn $0{,}852/\sqrt n$; Trực quan | Ví dụ 05.7 | S&B §5.1 |
| L05-B12c | Hội tụ của Monte Carlo lần ghé đầu tiên | Định nghĩa không chệch và hội tụ hầu chắc chắn (cùng chỉ số $n$); Giả thiết đủ (lượt độc lập cùng phân phối, phần thưởng bị chặn); Định lý; chứng minh trong ghi chú diễn giả | Định nghĩa 05.15, Định lý 05.16 | S&B §5.1 tr. 93 |
| L05-B12d | Hội tụ của Monte Carlo mọi lần ghé | Định lý; Kết luận; Lưu ý chệch ở số lượt hữu hạn; Lưu ý bước hằng với mẫu độc lập cùng phân phối, phương sai $\sigma^2$; chứng minh và định nghĩa $J$ trong ghi chú diễn giả | Định lý 05.17, Nhận xét 05.18, 05.19 | S&B §5.1 |
| L05-B13 | Bài tập: chọn mẫu Monte Carlo tại $\mathrm S$ | Đề (a), (b) với $\gamma=0{,}9$ trong một khung "Câu hỏi:" | Bài tập tuần 5, bài 5, 7, đổi hệ số chiết khấu | tr. 20, 22 |
| L05-B13b | Bài tập: chọn mẫu Monte Carlo tại $\mathrm S$ | Lời giải: lợi tức $0{,}729$, $0{,}9$, $-0{,}81$, $-1$; trung bình $-0{,}0405$ và $-0{,}04525$; bước hằng $-0{,}22275$ | Định nghĩa 05.3, 05.6, Mệnh đề 05.11 | — |

### Mạch 3. Sai phân thời gian TD(0)

| Mã | Tiêu đề | Nội dung chính | Ghi chú | Nguồn |
|---|---|---|---|---|
| L05-C00 | (tiêu đề mạch) Sai phân thời gian TD(0) | Dòng dẫn, từ khóa | — | — |
| L05-C02 | Mục tiêu một bước | Nhu cầu: chuyển đầu $\mathrm S\to\mathrm X$ của $e_2$; hình `mc-td-targets.svg` (vẽ lại, nhãn lớn); Trực quan; mục tiêu bootstrap | Mục 3.1 | tr. 24–25; S&B §6.1 |
| L05-C03 | Ví dụ: một bước TD(0) sau chuyển $\mathrm S\to\mathrm X$ | Bảng sau $e_1$; chuyển đầu của $e_2$; khuôn bảng TD cố định; sai số TD (TD error) | Ví dụ 05.8 | S&B §6.1 |
| L05-C04 | Mục tiêu và sai số TD | Định nghĩa $Y_t$, $\delta_t$, cập nhật; Lưu ý sai số TD khác sai số thật | Định nghĩa 05.20 | tr. 25; S&B §6.1 |
| L05-C07 | Ví dụ: TD(0) trên lượt thứ nhất | "Tính …"; bảng khuôn cố định trên $e_1$; Diễn giải | Ví dụ 05.9 | tr. 29 |
| L05-C05 | Thuật toán TD(0) dạng bảng | Đầu vào, Đầu ra, Giả thiết, khởi tạo, bước 1 và bước 2–3 thụt lề (đánh số như Thuật toán 05.21) | Thuật toán 05.21 | tr. 25; S&B §6.1 |
| L05-C05b | Thuật toán TD(0) dạng bảng | "Trong vòng lặp của bước 1:"; bước 4–6 (bước 6 gán $S$ khi mở lượt mới), bước 7; Lưu ý đọc rồi ghi | Thuật toán 05.21 | S&B §6.1 |
| L05-C08 | Ví dụ: TD(0) trên lượt thứ hai | Dòng dữ kiện rút gọn; bảng khuôn cố định trên $e_2$, cột Chuyển không ngắt dòng; Diễn giải | Ví dụ 05.10 | tr. 29 |
| L05-C06 | Ví dụ: hai chuyển trên Lunar Lander | Nhu cầu (tự chuyển, self-transition); ô gộp $9216$; bảng khuôn TD cố định; Diễn giải | Ví dụ 05.11 | notebook mục 7.1 |
| L05-C06c | Trường hợp biên của TD(0) | Nhận xét: trạng thái kết thúc, tự chuyển, lượt bị cắt ngắn | Nhận xét 05.22, Ví dụ 05.12 (ghi chú diễn giả) | tr. 19 |
| L05-C10 | Bài tập: một bước TD(0) từ cùng bảng | Đề, bảng khuôn cố định để trống | Bài tập 05.20 của `exercises.md`, câu (a), (b) | Bài tập tuần 5, bài 3, 7 |
| L05-C10b | Bài tập: một bước TD(0) từ cùng bảng | Lời giải trên bảng | Định nghĩa 05.20 | — |

### Mạch 4. Độ chệch, phương sai và hội tụ

| Mã | Tiêu đề | Nội dung chính | Ghi chú | Nguồn |
|---|---|---|---|---|
| L05-D00 | (tiêu đề mạch) Độ chệch, phương sai và hội tụ | Dòng dẫn, từ khóa | — | — |
| L05-D01 | Ví dụ: Monte Carlo và TD(0) trên cùng dữ liệu | Nhu cầu; bảng sau $e_1$, $e_2$; Diễn giải hai cơ chế lan truyền | Ví dụ 05.13 | tr. 29 |
| L05-D02 | Ví dụ: giá trị chuẩn và độ lệch sau hai lượt | Nhắc lại Bellman kỳ vọng; bảng $v_\pi$ và độ lệch; Diễn giải | Ví dụ 05.14, 05.15 | tr. 19 |
| L05-D05 | Ví dụ: kỳ vọng của mục tiêu TD tại $\mathrm S$ | Nhu cầu; Trực quan; $\mathbb E[Y]=0{,}2$; độ chệch $-34/105$ | Ví dụ 05.16 | tr. 26–27 |
| L05-D05b | Độ chệch của mục tiêu TD | Định nghĩa độ chệch; Mệnh đề; Ý nghĩa (số hiệu); Lưu ý Monte Carlo không chệch khi Markov, $\pi$ cố định; chứng minh trong ghi chú diễn giả | Định nghĩa 05.24, Mệnh đề 05.25, Hệ quả 05.26, Mệnh đề 05.27 (ghi chú diễn giả) | S&B §6.1 |
| L05-D03 | Ví dụ: dãy bảy ô | Nhu cầu; hình `long-walk.svg`; dữ kiện; $v_\pi(\mathrm S)\approx0{,}829$ | Ví dụ 05.17 | tr. 30 |
| L05-D04 | Ví dụ: dãy bảy ô, hai lợi tức từ $\mathrm S$ | Hình `long-returns.svg`; $0{,}970299$ và $-0{,}99$; Diễn giải | Ví dụ 05.17 | tr. 31 (sửa số mũ) |
| L05-D04b | Mục tiêu một bước lý tưởng | $Y^*$; hình `target-randomness.svg`; Trực quan; $Y^*$ là kỳ vọng có điều kiện | Mục 4.3 | tr. 26–28 |
| L05-D06 | Ví dụ: phương sai của mục tiêu trên hai dãy | Bảng $\operatorname{Var}(G_t)$, $\operatorname{Var}(Y^*)$, hiệu; Diễn giải | Ví dụ 05.18 | tr. 19, 30 |
| L05-D06b | Phương sai của mục tiêu một bước lý tưởng | Giả thiết; Định lý; Chứng minh; Lưu ý bảng đang học | Định lý 05.28, Nhận xét 05.29 | S&B §6.2 |
| L05-D07a | Ví dụ: ba lịch bước học | Nhu cầu "vừa tới đích vừa tắt nhiễu"; bảng hai lịch; Diễn giải bước hằng và phương sai giới hạn | Ví dụ 05.19, Nhận xét 05.19 | S&B §2.5 |
| L05-D07 | Hội tụ của TD(0) dạng bảng | Trực quan: nhắc lại $T_\pi V=r_\pi+\gamma P_\pi V$ (Bài 04), điểm bất động; Giả thiết; "Lịch bước học Robbins–Monro:" với $\alpha_n(s)\in[0,1]$; Kết luận | Định lý 05.30, Mệnh đề 05.27, Nhận xét 05.31 | S&B §6.2, §2.5 |
| L05-D13 | Bài tập: nhận định về độ chệch, phương sai và bước học | Đề (a), (b), (c) | Nhận xét 05.19, 05.29, Bài tập 05.11(e) | Bài tập tuần 5, bài 4–5 |
| L05-D13b | Bài tập: nhận định về độ chệch, phương sai và bước học | Lời giải | Định lý 05.28 | — |

### Mạch 5. Dữ liệu cố định và cập nhật theo lô

| Mã | Tiêu đề | Nội dung chính | Ghi chú | Nguồn |
|---|---|---|---|---|
| L05-DT | (tiêu đề mạch) Dữ liệu cố định và cập nhật theo lô | Dòng dẫn, từ khóa | — | — |
| L05-D08 | Ví dụ: tám lượt $\mathrm A$, $\mathrm B$ | Nhu cầu; bảng tám lượt; Trực quan hai cách đọc | Ví dụ 05.20 | S&B §6.3, Ví dụ 6.4 |
| L05-D09 | Ví dụ: tám lượt $\mathrm A$, $\mathrm B$, lượt quét đầu | $\Delta_0$ của Monte Carlo và TD; $V_1=(0;\ 3/4)$ | Ví dụ 05.21 | S&B §6.3 |
| L05-D09b | Thuật toán cập nhật theo lô | Đầu vào, bước 1–4, Đầu ra | Thuật toán 05.32 | S&B §6.3 |
| L05-D09c | Ví dụ: tám lượt $\mathrm A$, $\mathrm B$, các lượt quét tiếp theo | Monte Carlo đứng yên; công thức đóng của TD; dừng ở $k=18$ với $\theta=0{,}01$ | Ví dụ 05.22 | S&B §6.3 |
| L05-D10 | Nghiệm Monte Carlo theo lô | Mệnh đề; bình phương tối thiểu; Chứng minh; số liệu tám lượt | Mệnh đề 05.33 | S&B §6.3 |
| L05-D11 | Nghiệm TD theo lô | Hình `ab-empirical.svg` (lớn hơn); Ký hiệu; Giả thiết (bước học; lượt kết thúc hoặc $\gamma<1$); Mệnh đề; số liệu; Ý nghĩa | Mệnh đề 05.34, Nhận xét 05.35 (ghi chú diễn giả) | S&B §6.3 |
| L05-D12 | Bài tập: hai nghiệm trên tám lượt $\mathrm A$, $\mathrm B$ | Đề (a) $V_3(\mathrm A)$, (b) tiêu chuẩn | Bài tập 05.12 | S&B Ví dụ 6.4 |
| L05-D12b | Bài tập: hai nghiệm trên tám lượt $\mathrm A$, $\mathrm B$ | Lời giải; Cách khác | Nhận xét 05.35 | — |

### Mạch 6. Tổng kết và chuyển tiếp

| Mã | Tiêu đề | Nội dung chính | Ghi chú | Nguồn |
|---|---|---|---|---|
| L05-E00 | (tiêu đề mạch) Tổng kết và chuyển tiếp | Dòng dẫn, từ khóa | — | — |
| L05-E02 | Kết quả và giả thiết không được bỏ | Dòng giả thiết chung; bảng ba cột, bốn kết quả của mạch 2 | Tóm tắt chương | — |
| L05-E02b | Kết quả và giả thiết không được bỏ | Dòng giả thiết chung cho ba hàng đầu; cùng bảng, bốn kết quả của mạch 4–5 | Tóm tắt chương | — |
| L05-E02c | Khung cập nhật của ba phương pháp | Bảng bốn cột Phương pháp / Quy tắc cập nhật / Dữ liệu dùng / Điều kiện dừng | Thuật toán 05.13, 05.21, 05.32 | — |
| L05-E02d | Điều kiện hội tụ | Dòng giả thiết chung; bảng ba cột, bốn hàng: Monte Carlo ($1/N(s)$, hai quy tắc), Monte Carlo bước hằng, TD(0), TD theo lô | Định lý 05.16, 05.17, 05.30, Nhận xét 05.19, Mệnh đề 05.34 | — |
| L05-E06 | Bài tập: tàu đổ bộ thu nhỏ, lượt thứ ba | Đề bài tập tổng hợp trên $e_3$ | Bài tập 05.8 | — |
| L05-E06b | Bài tập: tàu đổ bộ thu nhỏ, lượt thứ ba | Lời giải (Monte Carlo, bảng TD(0) khuôn cố định, độ lệch) | Bài tập 05.8 | — |
| L05-E01 | Trả lời vấn đề trung tâm | Năm dòng đánh số 2–6 song song với L05-A03, mỗi dòng một điều kiện và một kết luận có số (dòng 4: độ chệch $-0{,}324$, $Y^*$ bỏ $20\%$ phương sai, Robbins–Monro); dòng 6 nối sang Bài 06; dòng "Nguồn:" | Tình huống áp dụng | tr. 28, 32–33 |
| L05-E04 | Câu hỏi tự kiểm tra | Bốn câu: lượt bị cắt ngắn, mục tiêu TD không chệch, bước hằng, hai lựa chọn của Monte Carlo | — | — |
| L05-E03 | Bài tập về nhà và tài liệu đọc | Bảng `Mạch \| Bài tập` (sáu mạch, hai cặp cột) theo bảng mạch của `exercises.md`: số hiệu của tệp bài tập, bài chỉ trong ghi chú có nhãn "ghi chú:"; Bài tập 05.8 xếp ở mạch 6 (bài tổng hợp E06); Tài liệu đọc; liên kết "Ghi chú bài giảng · Bài tập" | Bài tập củng cố, các mục 1–5; `exercises.md` | S&B |

## Bài tập trên trang chiếu và tệp bài tập

| Trang | Loại | Trùng |
|---|---|---|
| L05-B13/B13b | có lời giải trên mặt trang | dữ kiện mới tại $\mathrm S$ với $\gamma=0{,}9$ (đợt biên tập sau năm vai rà soát); không trùng bài nào của ghi chú; câu (a), (b) của Bài tập 05.18 trong `exercises.md` |
| L05-C10/C10b | có lời giải trên mặt trang | câu (a), (b) của Bài tập 05.20 trong `exercises.md` (Bài tập 05.9 cũ) |
| L05-D13/D13b | có lời giải trên mặt trang | câu (c) trùng Bài tập 05.11(e) của ghi chú; (a), (b) dùng số liệu của Nhận xét 05.19, 05.29 |
| L05-D12/D12b | có lời giải trên mặt trang | câu (a) trùng Bài tập 05.12 của ghi chú |
| L05-E06/E06b | bài tập tổng hợp, lời giải trên mặt trang | trùng Bài tập 05.8 của ghi chú, cùng kết quả |

Trang L05-E03 ghi số hiệu theo bảng `Mạch | Mở phần | Bài tập` của `exercises.md`: mạch 1 → ghi chú 05.1; mạch 2 → 05.16, 05.18, 05.19, ghi chú 05.2–05.5; mạch 3 → 05.17, 05.20, 05.21, 05.26, ghi chú 05.6, 05.7; mạch 4 → 05.11, 05.22–05.24, 05.27, ghi chú 05.9, 05.10, 05.14; mạch 5 → 05.12, 05.25, 05.28; mạch 6 → 05.8, ghi chú 05.13, 05.15. Dòng liên kết cuối trang dẫn tới viewer của ghi chú bài giảng và của `exercises.md` (đồng bộ 2026-10-14).
