# Dàn bài Bài 06: Điều khiển phi mô hình

Ngày lập lại: 2026-10-12, đợt sửa theo chuẩn 2026-10-12 (giai đoạn II, bộ trang chiếu); cập nhật cùng ngày sau vòng biên tập theo năm báo cáo rà soát (xem `review-log.md`, mục "Rà soát năm vai và biên tập (giai đoạn II)"). Bản này thay dàn bài ngày 29-09-2026. Căn cứ: ghi chú bài giảng đã commit `19323ad` (`materials/lec-06/lecture-note.md`), kế hoạch `revision-plan-2026-10-12.md` mục A và D, `planning/quyet-dinh-chuan-2026-10-12.md`. Đặc tả từng trang ở [storyboard.md](storyboard.md); nhật ký ở [review-log.md](review-log.md). Mã trang chỉ dùng nội bộ, không xuất hiện trên mặt trang hay trong ghi chú diễn giả.

## Thông tin chung

Học phần Học tăng cường, năm học 2026–2027, học kỳ 1; sinh viên đã học học máy, học sâu, thuật toán và Bài 01–05. Nguồn bắt buộc: bài giảng gốc (2025–2026) `lecture-06-model-free-control.pdf`, 30 trang. Đơn vị trên bìa: "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội" (quyết định chung §5). Deck có 75 trang trong 7 mạch, 120 phút trình chiếu; 30 phút còn lại dành cho chữa bài và bài thực hành LunarLander đã có, không tạo code demo mới.

## Mục tiêu học tập (trùng ghi chú bài giảng)

| Mục tiêu | Năng lực | Trang xây dựng | Trang kiểm tra (lời giải trên mặt trang) |
|---|---|---|---|
| MT1 | Phân biệt $q_\pi$, $q_*$, bảng $Q$; xác định thông tin trong một mẫu chuyển | A05, B01, B08, B02 | A05 (fragment), B07/B10 câu 3 |
| MT2 | Tính phân phối $\varepsilon$-tham lam, kể cả đồng hạng; kiểm điều kiện của Mệnh đề 06.6 | B03, B04, B05, B11, B06, B09 | B07/B10 |
| MT3 | Thực hiện Monte Carlo lần ghé đầu tiên theo cặp, bộ đếm $N$ đúng | C01–C07, C05, C06, C10 | C08/C09 |
| MT4 | Thực hiện cập nhật Sarsa và Q-learning; xử lý trạng thái kết thúc, cắt ngắn; phân biệt hành vi với đích | D01–D07, D06, E01–E07, E11 | D08/D11, E08/E12 |
| MT5 | Kiểm giả thiết của các định lý hội tụ; phân biệt với dừng theo ngân sách | F12–F13 | F05/F09, G03/G07, G08 |

## Khung lý thuyết chung

- **Vấn đề trung tâm.** Chọn hành động tại D của dãy năm ô khi không biết mô hình; tác tử chỉ thấy mẫu.
- **Đối tượng và ký hiệu chung.** MDP hữu hạn với $p(s',r\mid s,a)$ tác tử không biết; $\mathcal S$ (không kết thúc), $\mathcal S^+$; $\mathcal A(s)$, $m(s)$; $R_{t+1}$, $G_t$, $G_T=0$; giá trị trạng thái kết thúc bằng $0$; $q_\pi$, $q_*$ (giá trị thật) khác bảng $Q$ (ước lượng, Định nghĩa 06.1); tên ô viết chữ đứng $\mathrm A,\dots,\mathrm E$.
- **Khung cập nhật chung (trang A09).** $Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha_t[Y_t-Q(S_t,A_t)]$; ba phương pháp khác nhau ở dữ liệu tạo $Y_t$ và thời điểm cập nhật.
- **Giả thiết.** Phép tính tay dùng dãy năm ô với $\gamma=1$, bước học hằng $0{,}8$ (ngoài miền định lý); các định lý dùng giả thiết nền (MDP hữu hạn, động lực dừng, phần thưởng bị chặn, $0\le\gamma<1$, $Q_0$ hữu hạn, mẫu sinh từ MDP) cộng độ phủ, Robbins–Monro theo cặp, GLIE với Sarsa; mạch 6 dùng dãy năm ô với $\gamma=0{,}9$.
- **Chuỗi định nghĩa → kết quả → phương pháp.** Bảng $Q$ (06.1) → chính sách $\varepsilon$-tham lam, $\varepsilon$-mềm (06.3, 06.4) → cải thiện $\varepsilon$-tham lam (Mệnh đề 06.6) → lần ghé đầu tiên của cặp (06.8) → Monte Carlo (Thuật toán 06.9) → mục tiêu Sarsa (06.11) → Sarsa (06.12) → hành vi và đích (06.14) → mục tiêu Q-learning (06.15) → Q-learning (06.16) → GLIE (06.18), Robbins–Monro theo cặp (06.19) → Định lý 06.21 (Q-learning), 06.22 (Sarsa).
- **Giới hạn áp dụng.** Biểu diễn bảng; kết luận tiệm cận; điều khiển Monte Carlo không có định lý hội tụ trong bài (Nhận xét 06.23; nêu trên mặt F08 và G06); $\gamma=1$ nằm ngoài giả thiết của hai định lý vì toán tử Bellman tối ưu không còn co theo chuẩn cực đại (F13); bài thực hành LunarLander vi phạm tính Markov, Robbins–Monro và GLIE; bảng không tổng quát hóa giữa các ô (dẫn sang Bài 07).

## Bảng thuật ngữ Việt–Anh

| Tiếng Việt | Tiếng Anh | Trang xuất hiện đầu trên mặt trang |
|---|---|---|
| mục tiêu cập nhật | update target | A01 |
| giá trị hành động | action value | B02 |
| tham lam | greedy | A07 |
| phần thưởng | reward | A07 |
| chính sách $\varepsilon$-tham lam | $\varepsilon$-greedy policy | A02 |
| thăm dò | exploration | A02 |
| lần ghé đầu tiên | first-visit | A02 |
| lượt | episode | A02 |
| học theo chính sách | on-policy | A02 |
| học khác chính sách | off-policy | A02 |
| ngân sách | budget | A02 |
| lợi tức | return | A03 |
| bước học | step size | A09 |
| tác tử | agent | A05 |
| khai thác | exploitation | B04 |
| chính sách $\varepsilon$-mềm | $\varepsilon$-soft policy | B05 |
| quy tắc phá hòa | tie-breaking | B05 |
| quá trình quyết định Markov (MDP) | Markov decision process | B06 (đủ tên tiếng Anh và viết tắt trên mặt trang) |
| hầu chắc chắn | almost surely | C05 |
| cắt ngắn | truncation | C10 |
| mọi lần ghé | every-visit | C08 |
| sai phân thời gian TD(0) | temporal difference | A07 (tên Việt trên mặt trang; tên tiếng Anh trong ghi chú diễn giả A07), D01 |
| chính sách hành vi | behavior policy | E09 |
| chính sách đích | target policy | E09 |
| tỉ số lấy mẫu quan trọng | importance sampling ratio | E07 |
| tham lam trong giới hạn với thăm dò vô hạn (GLIE) | greedy in the limit with infinite exploration | F02 (mặt trang) |
| điều kiện Robbins–Monro theo cặp | Robbins–Monro conditions | F03 |
| tàu đổ bộ | LunarLander | C10 |
| mục tiêu bootstrap | bootstrap target | ghi chú diễn giả A09 |
| sai số TD | TD error | D04 (nhắc lại Bài 05; thay chữ "sai lệch" của bản trước) |
| khối cực đại (tổng xác suất trên tập cực đại) | — (thuật ngữ nội bộ của học phần) | F06; dùng thống nhất ở F09, G07 và ghi chú diễn giả, thay "khối trên cực đại", "khối xác suất tham lam" |
| điều khiển Monte Carlo | Monte Carlo control | C00 (tên mạch 3); dạng duy nhất, không viết "Monte Carlo điều khiển" |
| thăm dò vô hạn (độ phủ) | infinite exploration (coverage) | A03 (độ phủ), F02 |
| chính sách Markov dừng | stationary policy | ghi chú diễn giả B02 (phân biệt với dừng thuật toán) |
| chính sách xác định | deterministic policy | ghi chú diễn giả B06 |
| điểm bắt đầu thăm dò | exploring starts | ghi chú diễn giả F08 |
| bán gradient | semi-gradient | ghi chú diễn giả A09 (cầu sang Bài 07) |

## Bản đồ bảy mạch

| N | Mạch | Trang tiêu đề mạch (`id`) | Chức năng | Đầu vào → đầu ra | Trang | Phút |
|---|---|---|---|---|---|---:|
| 1 | Mở đầu | A01 (bìa) | Đặt bài toán, tiên quyết, mục tiêu, khung cập nhật | Bài 03–05 → bài toán tại D và khung $Q\leftarrow Q+\alpha[Y-Q]$ | A01, A07, A02, A08, A03, A09 | 8 |
| 2 | Giá trị hành động và thăm dò | B00 (`mach-2`) | Khái niệm $Q$, $\varepsilon$-tham lam, cải thiện trong lớp $\varepsilon$-mềm | $q_\pi$, định lý cải thiện → bảng $Q$ và quy tắc chọn hành động | 13 | 21 |
| 3 | Điều khiển Monte Carlo | C00 (`mach-3`) | Thuật toán học từ lượt hoàn chỉnh | $q_\pi$ cần đo từ mẫu → Thuật toán 06.9 và giới hạn chờ lượt | 11 | 18 |
| 4 | Sarsa và mục tiêu một bước | D00 (`mach-4`) | Thuật toán với mục tiêu bootstrap theo hành động kế tiếp | giới hạn Monte Carlo, TD(0) → Thuật toán 06.12, ba sự kiện dừng | 11 | 18 |
| 5 | Q-learning và học khác chính sách | E00 (`mach-5`) | Tách hành vi và đích; mục tiêu cực đại | mục tiêu Sarsa phụ thuộc thăm dò → Thuật toán 06.16, so sánh trên cùng dữ liệu | 12 | 19,5 |
| 6 | Điều kiện hội tụ | F00 (`mach-6`) | Giả thiết để $Q_t\to q_*$ | bảng hữu hạn mẫu → GLIE, Robbins–Monro theo cặp, Định lý 06.21–06.22 | 12 | 19,5 |
| 7 | Tổng kết và chuyển tiếp | G00 (`mach-7`) | Tổng kết, áp dụng LunarLander, trả lời vấn đề trung tâm | toàn bài → bảng giả thiết, bài tập, Bài 07 | 10 | 16 |
| | **Tổng** | | | | **75** | **120** |

## Dàn từng trang

Mỗi hàng là luận điểm trung tâm của trang; mã đầy đủ có tiền tố `L06-`. Phút cộng theo mạch ở bản đồ trên.

| Vị trí | Mã | Tiêu đề | Luận điểm trung tâm | Phút |
|---|---|---|---|---:|
| #/1/1 | A01 | Điều khiển phi mô hình | Bìa; luận đề: ba phương pháp khác nhau ở mục tiêu cập nhật | 0,5 |
| #/1/2 | A07 | Tiên quyết và quy ước | Nhắc lại $q_\pi$, $v_\pi$ (Bài 03); cải thiện tham lam, $v_*=T_*v_*$ với $T_*$ co, $q_*$ từ $v_*$ (Bài 04); Monte Carlo, TD(0), Robbins–Monro theo trạng thái (Bài 05); ký hiệu $\mathcal S$, $\mathcal S^+$, $m(s)$, $R_{t+1}$, $d_0$ (quy ước $\mathbb E_\pi$ trong ghi chú diễn giả) | 1,5 |
| #/1/3 | A02 | Mục tiêu học tập | Năm mục tiêu trùng ghi chú | 1 |
| #/1/4 | A08 | Nội dung | Bảy mạch đánh số khớp trang tiêu đề mạch | 1 |
| #/1/5 | A03 | Vấn đề trung tâm | Chọn hành động tại D; câu trả lời có điều kiện của mạch 2–6 | 2,5 |
| #/1/6 | A09 | Khung chung của quy tắc cập nhật | Bài 05 cập nhật $V$ với $\pi$ cố định; chọn hành động theo $V$ cần $p$, $r$, theo $Q$ thì không; $Q\leftarrow Q+\alpha_t[Y_t-Q]$; ba phương pháp khác ở $Y_t$ | 1,5 |
| #/2/1 | B00 | Giá trị hành động và thăm dò | Trang tiêu đề mạch 2 | 0,5 |
| #/2/2 | A05 | Thông tin trong một mẫu chuyển | Nhu cầu và ví dụ dẫn nhập $(\mathrm D,1,10,\mathrm E)$: không có dữ liệu về $(\mathrm D,0)$ | 1,5 |
| #/2/3 | B01 | Ví dụ: bảng khởi tạo nghiêng phải | Bảng số khởi tạo chưa là quan sát; xếp phải trên trái tại D | 1,5 |
| #/2/4 | B08 | Ví dụ: chính sách luôn đi trái | Hành động đầu cố định, tiếp nối theo $\pi_L$: 998 và 10 | 1,5 |
| #/2/5 | B02 | Bảng giá trị hành động | Nhắc lại $q_\pi$; Định nghĩa 06.1; nhắc lại $q_*$ | 2 |
| #/2/6 | B03 | Nhu cầu thăm dò | Tham lam theo bảng nghiêng phải không bao giờ thử $(\mathrm D,0)$ | 1,5 |
| #/2/7 | B04 | Ví dụ: xác suất chọn hành động tại D | $\varepsilon=\tfrac14$: $(\tfrac18,\tfrac78)$; đồng hạng $(\tfrac12,\tfrac12)$ | 1,5 |
| #/2/8 | B05 | Chính sách $\varepsilon$-tham lam | Định nghĩa 06.3, 06.4 | 2 |
| #/2/9 | B11 | Cải thiện chính sách khi giữ thăm dò | Nhu cầu, ví dụ một trạng thái ba hành động ($-0{,}2\to2{,}6$), trực quan phần sàn | 2 |
| #/2/10 | B06 | Cải thiện chính sách $\varepsilon$-tham lam | Mệnh đề 06.6 với giả thiết và kết luận | 1,5 |
| #/2/11 | B09 | Chứng minh: cải thiện chính sách $\varepsilon$-tham lam | Trọng số $w_a=w(a\mid s)$, bất đẳng thức một bước, $q_\pi=r+\gamma\sum p\,v_\pi$ cho vế trái $T_{\pi'}v_\pi$, đơn điệu và co của $T_{\pi'}$ | 2,5 |
| #/2/12 | B07 | Bài tập: chính sách $\varepsilon$-tham lam trên dãy năm ô | Đề Bài tập 06.2 của ghi chú | 1,5 |
| #/2/13 | B10 | Bài tập: chính sách $\varepsilon$-tham lam trên dãy năm ô | Lời giải: $(0{,}1;0{,}9)$, $(0{,}6;0{,}2;0{,}2)$, chưa đủ điều kiện của mệnh đề | 1,5 |
| #/3/1 | C00 | Điều khiển Monte Carlo | Trang tiêu đề mạch 3 | 0,5 |
| #/3/2 | C01 | Lợi tức của cặp trạng thái–hành động | Nhu cầu đo $q_\pi$ từ lượt; trực quan vòng sinh lượt–gắn lợi tức–lập chính sách | 1,5 |
| #/3/3 | C02 | Ví dụ: một lượt tham lam D→E | $N(\mathrm D,1)=1$, $Q(\mathrm D,1)=10$; khởi tạo không là quan sát | 1,5 |
| #/3/4 | C03 | Lần ghé đầu tiên của cặp | Định nghĩa 06.8; trung bình gia tăng với $N$ từ 0 | 2 |
| #/3/5 | C04 | Ví dụ: lượt thăm dò trên dãy năm ô | Dãy số cho trước sinh lượt D→C→B→A | 2 |
| #/3/6 | C07 | Ví dụ: lượt thăm dò trên dãy năm ô, cập nhật lần ghé đầu tiên | $998,999,1000$; hàng D xếp trái | 2 |
| #/3/7 | C05 | Thuật toán điều khiển Monte Carlo: đầu vào | Thuật toán 06.9: đầu vào, đầu ra, giả thiết kết thúc, ngân sách $K$ | 1,5 |
| #/3/8 | C06 | Thuật toán điều khiển Monte Carlo: các bước | Năm bước; $Q$, $\pi_k$ cố định trong lượt | 2 |
| #/3/9 | C10 | Điều khiển Monte Carlo trên lượt bị cắt | Nhận xét 06.10; tàu đổ bộ (chính sách tham lam học trong bài thực hành): lượt dài, 44% bị cắt | 1,5 |
| #/3/10 | C08 | Bài tập: lần ghé đầu tiên trên lượt có cặp lặp | Đề Bài tập 06.3 | 1,5 |
| #/3/11 | C09 | Bài tập: lần ghé đầu tiên trên lượt có cặp lặp | Lời giải 996, 997 | 2 |
| #/4/1 | D00 | Sarsa và mục tiêu một bước | Trang tiêu đề mạch 4 | 0,5 |
| #/4/2 | D01 | Mục tiêu một bước cho giá trị hành động | Nhu cầu sau D→C; nhắc lại TD(0); trực quan $-1+\gamma Q(\mathrm C,A')$ | 2 |
| #/4/3 | D02 | Ví dụ: năm mẫu chuyển trên dãy năm ô | Dữ kiện năm mẫu dùng chung | 1,5 |
| #/4/4 | D03 | Ví dụ: năm mẫu chuyển, Sarsa ở mẫu 1–2 | $0$ và $-0{,}6$; hành động đã lấy mẫu vào mục tiêu | 2 |
| #/4/5 | D04 | Mục tiêu Sarsa | Định nghĩa 06.11; sai số TD; bộ năm; $A_{t+1}$ từ chính sách sinh dữ liệu | 1,5 |
| #/4/6 | D05 | Thuật toán Sarsa: đầu vào | Thuật toán 06.12: đầu vào, đầu ra, giả thiết, khởi tạo, dừng | 1,5 |
| #/4/7 | D10 | Thuật toán Sarsa: các bước | Năm bước; $A'$ chọn một lần trước cập nhật | 2 |
| #/4/8 | D07 | Ví dụ: năm mẫu chuyển, Sarsa ở mẫu 3–5 | $800$, $8{,}2$, $-1{,}28$; 1000 chưa truyền về D | 2 |
| #/4/9 | D06 | Kết thúc lượt, cắt ngắn và hết ngân sách | Nhận xét 06.13 dạng bảng: chỉ kết thúc lượt bỏ số hạng $\gamma Q_t(S_{t+1},A_{t+1})$; tàu đổ bộ | 1,5 |
| #/4/10 | D08 | Bài tập: cập nhật Sarsa với bước học khác | Đề Bài tập 06.4 ($\alpha=0{,}5$) | 1,5 |
| #/4/11 | D11 | Bài tập: cập nhật Sarsa với bước học khác | Lời giải $-0{,}8$, $-0{,}5$; mục tiêu không đổi khi hết ngân sách | 2 |
| #/5/1 | E00 | Q-learning và học khác chính sách | Trang tiêu đề mạch 5 | 0,5 |
| #/5/2 | E01 | Mục tiêu Sarsa và hành động thăm dò | Nhu cầu, ví dụ mẫu 2, trực quan hai vai | 1,5 |
| #/5/3 | E09 | Chính sách hành vi và chính sách đích | Định nghĩa 06.14; hình hai đường | 2 |
| #/5/4 | E02 | Ví dụ: năm mẫu chuyển, Q-learning ở mẫu 1–2 | Mẫu 2 cho $0{,}2$ thay vì $-0{,}6$ | 2 |
| #/5/5 | E03 | Mục tiêu Q-learning | Định nghĩa 06.15; bộ bốn (điều kiện trùng mục tiêu chuyển vào ghi chú diễn giả, để bài tập E08 câu 2 là bước suy luận) | 1,5 |
| #/5/6 | E04 | Thuật toán Q-learning: đầu vào | Thuật toán 06.16: đầu vào, đầu ra, khởi tạo | 1,5 |
| #/5/7 | E10 | Thuật toán Q-learning: các bước | Bốn bước; chọn hành động sau cập nhật | 1,5 |
| #/5/8 | E06 | Ví dụ: năm mẫu chuyển, Sarsa và Q-learning | Bảng so sánh năm mẫu; $-1{,}28$ và $-0{,}64$ | 2 |
| #/5/9 | E07 | Dữ liệu hành vi trong Q-learning | Tỉ số $\rho=\pi/b$ của dự đoán TD(0) khác chính sách; Nhận xét 06.17: Q-learning một bước không cần $\rho$, vẫn cần độ phủ | 2 |
| #/5/10 | E11 | Ví dụ: một chuyển của tàu đổ bộ | $2{,}748$ và $3{,}045$ trên dữ liệu notebook; đứng sát bài tập E08 vì cùng so hai mục tiêu trên một chuyển | 1,5 |
| #/5/11 | E08 | Bài tập: mục tiêu Sarsa và Q-learning trên cùng chuyển | Đề Bài tập 06.5 | 1,5 |
| #/5/12 | E12 | Bài tập: mục tiêu Sarsa và Q-learning trên cùng chuyển | Lời giải $0$, $799$, điều kiện $A'\in\mathcal G_Q$ | 2 |
| #/6/1 | F00 | Điều kiện hội tụ | Trang tiêu đề mạch 6 | 0,5 |
| #/6/2 | F12 | Bảng Q khi một cặp không được thử | Nhu cầu; $\gamma=0{,}9$: $q_*(\mathrm D,0)=808{,}1$, ô giữ 0 | 2 |
| #/6/3 | F10 | Cập nhật mẫu và phương trình Bellman tối ưu | Trực quan: bước lặp có nhiễu của toán tử co | 2 |
| #/6/4 | F06 | Ví dụ: khối cực đại khi $\varepsilon$ giảm | $\tfrac14$, $1/k$, $1/k^2$; Borel–Cantelli | 2 |
| #/6/5 | F02 | Tham lam trong giới hạn với thăm dò vô hạn | Định nghĩa 06.18 | 1,5 |
| #/6/6 | F07 | Ví dụ: một cặp được cập nhật thưa | $\sum2^{-n}=1$; lịch toàn cục không đủ | 1,5 |
| #/6/7 | F03 | Điều kiện Robbins–Monro theo cặp | Định nghĩa 06.19 | 1,5 |
| #/6/8 | F04 | Hội tụ của Q-learning dạng bảng | Định lý 06.21 | 2 |
| #/6/9 | F08 | Hội tụ của Sarsa dạng bảng | Định lý 06.22; điều khiển Monte Carlo trộn lợi tức nhiều $\pi_k$, chưa có định lý hội tụ tổng quát | 2 |
| #/6/10 | F13 | Vai trò của từng giả thiết | Bốn phản ví dụ khi bỏ giả thiết; $\gamma=1$: toán tử không còn co, định lý không áp dụng | 1,5 |
| #/6/11 | F05 | Bài tập: kiểm giả thiết hội tụ | Đề Bài tập 06.6 | 1,5 |
| #/6/12 | F09 | Bài tập: kiểm giả thiết hội tụ | Lời giải a/b/c | 1,5 |
| #/7/1 | G00 | Tổng kết và chuyển tiếp | Trang tiêu đề mạch 7 | 0,5 |
| #/7/2 | G05 | Kết quả về giá trị hành động và thăm dò | Bảng kết quả–giả thiết–công thức: ba khái niệm | 1,5 |
| #/7/3 | G09 | Kết quả về ba thuật toán | Bảng kết quả–giả thiết–công thức: ba thuật toán | 1,5 |
| #/7/4 | G01 | Khung chung của ba phương pháp | Phương pháp–quy tắc–dữ liệu (kèm theo/khác chính sách)–dừng | 1,5 |
| #/7/5 | G06 | Điều kiện hội tụ của ba phương pháp | Phương pháp–giả thiết–kết luận; thứ tự hàng Monte Carlo, Sarsa, Q-learning như G09, G01 | 1,5 |
| #/7/6 | G03 | Bài tập: chọn phương pháp cho tàu đổ bộ | Bài tập tổng hợp trên LunarLander | 2 |
| #/7/7 | G07 | Bài tập: chọn phương pháp cho tàu đổ bộ | Lời giải; số liệu một lần chạy (trung bình ± sai số chuẩn); hiệu ghép cặp chứa 0, chưa xếp hạng được | 2 |
| #/7/8 | G02 | Trả lời vấn đề trung tâm | Nhắc lại bài toán tại D; bảng ba hàng D có cột khởi tạo; kết luận có điều kiện; dòng "Nguồn:" | 2 |
| #/7/9 | G08 | Câu hỏi tự kiểm tra | Bốn câu, mỗi câu kiểm một giả thiết | 2 |
| #/7/10 | G04 | Bài tập về nhà và tài liệu đọc | Bảng Mạch–Bài tập chỉ gồm Bài tập 06.1–06.12 của ghi chú; "Tệp bài tập: chưa có"; tài liệu đọc; ghi chú; Bài 07 | 1,5 |

## Ánh xạ 30 trang nguồn

| Trang nguồn | Nội dung | Đích trong deck | Quyết định |
|---:|---|---|---|
| 1 | Giới thiệu | A01 | sửa: luận đề, đơn vị theo quyết định chung |
| 2 | Mục lục | A02, A08 | tách: mục tiêu và nội dung |
| 3 | Dự đoán phi mô hình | A07, A05 | gộp vào nhắc lại và trang vấn đề |
| 4 | Monte Carlo dự đoán | A07, C01 | nhắc lại, chuyển từ trạng thái sang cặp |
| 5 | TD(0) | A09, D01 | nhắc lại, khung chung |
| 6 | Vòng tương tác, điều khiển | A03, B03 | giữ ý, hình vòng điều khiển |
| 7 | $Q$, chính sách tham lam | B02, B04, B05 | tách khái niệm và ví dụ |
| 8 | Theo/khác chính sách | E09, E07 | định nghĩa bằng hai vai |
| 9 | Một bước, lượt | C01, D01 | gộp vào nhu cầu |
| 10 | Cập nhật Monte Carlo | C03, C05, C06 | lần ghé đầu tiên theo cặp, $N$ từ 0 |
| 11 | Cải thiện Monte Carlo, $\varepsilon_k=1/k$ | C05, F06 | lịch thăm dò; ghi chú diễn giả |
| 12 | Từ Monte Carlo sang TD điều khiển | D01 | tiêu đề không dùng "Từ…sang…" |
| 13 | Sarsa | D03, D04 | ví dụ trước định nghĩa |
| 14 | Giả mã Sarsa | D05, D10 | tách đầu vào và các bước |
| 15 | Dãy năm ô, bảng nghiêng phải | A03, A05, B01 | ví dụ xuyên suốt |
| 16 | Monte Carlo tham lam, quá trình cảm sinh | C02; vòng B–C trong ghi chú diễn giả B02, F13 | ví dụ, phản ví dụ $\gamma=1$ |
| 17 | Monte Carlo thăm dò, bảng nghiêng trái, dãy số | C04, C07 | giữ, đổi ký hiệu $u_j$ |
| 18 | Sarsa năm mẫu, $\alpha=0{,}8$ | D02, D03, D07 | hoàn thiện $A'$ và biên lượt |
| 19 | TD(0) khác chính sách | E07 (một dòng trên mặt trang về tỉ số $\rho$; chi tiết ở ghi chú diễn giả); đọc thêm Mục 6 của ghi chú | chuyển đọc thêm, giữ nhu cầu trên mặt trang |
| 20 | Q-learning | E02, E03, E04, E10 | ví dụ trước công thức; giả mã bổ sung |
| 21 | Q-learning năm mẫu (bảng nghiêng trái) | E02, E06 | dùng bảng nghiêng phải cho cả hai thuật toán |
| 22 | Dự đoán/điều khiển, so sánh | G01 | bảng khung chung |
| 23 | Ma trận họ thuật toán | không dùng | lược: ngoài phạm vi bài |
| 24 | Cải thiện $\varepsilon$-tham lam | B11, B06, B09 | ví dụ, mệnh đề, chứng minh |
| 25 | GLIE | F06, F02 | ví dụ trước định nghĩa |
| 26 | Hội tụ Monte Carlo với GLIE | ghi chú diễn giả F08, G06 | không phát biểu thành định lý |
| 27 | Hội tụ Sarsa | F07, F03, F08 | Robbins–Monro theo cặp, GLIE |
| 28 | Hội tụ Q-learning; Q-learning nhạy hơn với sai số do cực đại | F04, E07; ghi chú diễn giả E03, G01 (ước lượng cao do cực đại, Sutton và Barto §6.7, nối sang Bài 09) | độ phủ, không cần GLIE; nhận định về cực đại giữ ở ghi chú diễn giả |
| 29 | Chặn Monte Carlo hữu hạn mẫu | đọc thêm Mục 6 của ghi chú (G04 ghi chú diễn giả) | chuyển đọc thêm |
| 30 | Tổng kết | G05, G09, G02 | bảng giả thiết, trả lời vấn đề trung tâm |

Phần bổ sung ngoài nguồn có căn cứ trong ghi chú bài giảng: ví dụ một trạng thái ba hành động (B11), lượt có cặp lặp (C08), mẫu tàu đổ bộ (C10, E11, G03), dãy năm ô với $\gamma=0{,}9$ (F12, F13), phản ví dụ bước hằng (F13). Các bộ số tự xây dựng là số liệu sư phạm, ghi trong ghi chú diễn giả.
