# Bài 11 — Lập kế hoạch dựa trên mô hình: kế hoạch bộ trang chiếu

> **Mục đích.** Kế hoạch dựng bộ trang chiếu mới của Bài 11 theo NT1–NT28 với tham số P1–P11 của học phần, nhất quán với `ke-hoach-ghi-chu.md` (mục, số hiệu khối, ví dụ, số liệu) và `ke-hoach-bai-tap.md` (bài trên trang). Tệp planning nội bộ; là đầu vào của `storyboard.md` (giai đoạn III), không thay storyboard.
>
> **Ngày:** 2026-11-19. **Trạng thái:** kế hoạch, chưa duyệt (chờ quyết QT ở mục 13; deck chỉ soạn sau khi ghi chú và `exercises.md` đạt kiểm định, BT-RL-9).
>
> **Đầu vào.** `NGUYEN-TAC-TRANG-CHIEU.md` (NT1–NT28); `NGUYEN-TAC-HOC-PHAN.md` mục 3 (P1–P11, NT-RL-7…11, P7 khung kỹ thuật lấy từ deck 01), mục 5 (lược đồ mã trang `LNN-k-mm`, `deck_lint.py --course rl-plan`); `AGENTS.md` mục "Tham số trang chiếu của học phần" (P1–P11, NT-RL-1…6), "Mẫu RevealJS bắt buộc", "Trang tiêu đề mạch"; `CLAUDE.md` mục "Deck structure and content"; `ke-hoach-ghi-chu.md`, `ke-hoach-bai-tap.md`; mẫu cấu trúc `ds-foundation-algorithms/2627-1/planning/lec-11/storyboard.md`.

## 0. Tóm tắt quyết định

- **Tệp:** `rl-plan/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` (slug ASCII từ tên bài "Lập kế hoạch dựa trên mô hình", NT26). Deck cũ `lecture-11-cac-phuong-phap-gradient-chinh-sach-nang-cao.html` và 11 SVG cũ trong `img/lec-11/`: QT1.
- **Nguồn nội dung:** ghi chú Bài 11 đã kiểm định và bài tập của bài; không có deck nguồn (ngoại lệ P1, QG1 của `ke-hoach-ghi-chu.md`). Mọi chỗ deck khác thứ tự ghi chú ghi trong storyboard (NT1, NT2); lỗi ghi chú phát hiện khi làm deck chỉ ghi đề xuất (NT3).
- **Sáu mạch** (NT10): 1 Mở đầu; 2 Tính bất định và lập kế hoạch nền (giáo trình 11.1); 3 Tìm kiếm theo cây Monte Carlo (11.2); 4 Tối ưu kế hoạch dựa trên đạo hàm (11.3); 5 Học tăng cường phân cấp (11.4); 6 Tổng kết (11.5). Phương án bảy mạch: QT2.
- **60 trang** (6 + 12 + 11 + 11 + 11 + 9), đúng trần P6 khi có lý do (mục 8); phương án 58 trang ở QT3.
- **Mã trang** theo `NGUYEN-TAC-HOC-PHAN.md` mục 5: bìa `L11-1-01`; trang tiêu đề mạch `L11-k-00` với `id="mach-k"`, $k=2,\dots,6$; trang khác `L11-k-mm`, `mm` từ `01`; mạch 1 không có trang tiêu đề mạch (bìa mở mạch). Mạch $k$ mở tại `#/k/1` (`hashOneBasedIndex: true`).
- **Khung kỹ thuật** (P7 theo `NGUYEN-TAC-HOC-PHAN.md` mục 3): phần `<head>`, cấu hình `Reveal.initialize`, plugin cục bộ, chân trang lấy từ `2627-1/lecture-01-gioi-thieu-hoc-tang-cuong.html`; không dùng `lecture-template.html` (là deck math-4-AI); `<html lang="vi" data-lecture="11">`; chân trang "Học tăng cường · Học kỳ 1, 2026–2027 · Bài 11"; không `<style>`, không `style=""` trừ nhu cầu riêng một trang đã ghi trong storyboard.
- **Hai ví dụ xuyên suốt** của ghi chú: mê cung hai phòng (mạch 1, 2, 3, 5, 6) và xe trên đường ray (mạch 4); mỗi lần dùng lại trả lời một câu hỏi mới và nêu lại dữ kiện trên trang (NT23).

## 1. Bảng mạch (NT10, NT12, NT13; `CLAUDE.md` "Storyboard")

| Mạch | Tên (trang tiêu đề mạch) | Loại | Chức năng | Đầu vào | Đầu ra | Góp vào câu hỏi trung tâm | Trang tiêu đề | Phút |
|---:|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu | giới thiệu, động lực | đặt bài toán: mẫu thật đắt, phép tính rẻ, mô hình học được có sai số | Định lý 06.21, 04.32; Định nghĩa 01.14 | mê cung hai phòng, khung "mô hình → kinh nghiệm mô phỏng → cập nhật → chính sách", câu hỏi trung tâm | đặt câu hỏi | (bìa `L11-1-01`) | 8 |
| 2 | Tính bất định và lập kế hoạch nền | khái niệm; thuật toán | mô hình là gì, sai đến đâu; dùng lại mẫu bằng Dyna | khung của mạch 1 | Định nghĩa 11.1, 11.4, 11.6; Mệnh đề 11.5, 11.9, 11.15; Thuật toán 11.10; Định nghĩa 11.12. Giới hạn: tính cho mọi trạng thái | câu trả lời "lập kế hoạch nền" | `L11-2-00` | 30 |
| 3 | Tìm kiếm theo cây Monte Carlo | thuật toán; kết quả | dồn tính toán vào quyết định tại trạng thái hiện tại | giới hạn của mạch 2; mô hình mẫu | Mệnh đề 11.21, 11.22; Định nghĩa 11.23; Thuật toán 11.26; Định lý 11.27. Giới hạn: cần hành động rời rạc | câu trả lời "tại thời điểm quyết định, rời rạc" | `L11-3-00` | 26 |
| 4 | Tối ưu kế hoạch dựa trên đạo hàm | thuật toán; kết quả | lập kế hoạch cho hành động liên tục bằng gradient qua mô hình; sai số tích lũy | giới hạn của mạch 3 | Định nghĩa 11.29, 11.32; Mệnh đề 11.30, 11.36; Thuật toán 11.31, 11.34. Giới hạn: chân trời dài | câu trả lời "liên tục, MPC" và "sai số tích lũy" | `L11-4-00` | 24 |
| 5 | Học tăng cường phân cấp | khái niệm; kết quả; thuật toán | rút ngắn chân trời lập kế hoạch bằng tùy chọn | giới hạn của mạch 4; lặp giá trị Bài 04 | Định nghĩa 11.38, 11.40; Mệnh đề 11.41; Định lý 11.42, 11.44; Thuật toán 11.46 | câu trả lời "trừu tượng thời gian" | `L11-5-00` | 22 |
| 6 | Tổng kết | tổng kết | so sánh bốn cách dùng mô hình, trả lời câu hỏi trung tâm, bài tập tổng hợp | mọi kết quả | bảng tổng kết, bảng phương pháp, câu trả lời có điều kiện | trả lời | `L11-6-00` | 10 |
| | **Tổng** | | | | | | | **120** |

**Câu hỏi của từng mạch** (NT13, xuất hiện trên trang nội dung đầu tiên của mạch):

- Mạch 2: "Câu hỏi: mô hình học từ vài bước thật sai đến đâu, và dùng nó thế nào để mỗi bước thật cho nhiều cập nhật?"
- Mạch 3: câu khẳng định "Tại $\mathrm F$ chỉ cần một quyết định; phép tính nên dồn vào các hành động tại $\mathrm F$."
- Mạch 4: câu khẳng định "Hành động $u\in\mathbb R$ không liệt kê được; mô hình khả vi cho đạo hàm theo $u$."
- Mạch 5: câu khẳng định "Giá trị của đích cần nhiều lượt quét để lan tới $\mathrm A$; một bước kế hoạch nên đi được nhiều bước thật."

**Trang tiêu đề mạch** (NT12: `section.strand-title`, `id="mach-k"`, `div.strand-title-body` > `h2` (`span.strand-number` "k." + tên) + `p.strand-lead` (≤ 25 âm tiết, câu trần thuật, không "Nhu cầu:", không "Muốn …, phải …", không mở bằng "Người học", không lặp khuôn câu) + `p.strand-keys` (≤ 5 cụm, ngăn bằng " · "); ghi chú diễn giả 40–100 âm tiết: kết quả kế thừa, việc của mạch, kết quả trao đi). Dự thảo (tác tử soạn deck chỉnh bằng `no-ai-slop` Edit; đã đếm âm tiết bằng tay):

| Trang | `h2` | `p.strand-lead` (âm tiết) | `p.strand-keys` |
|---|---|---|---|
| `L11-2-00` | 2. Tính bất định và lập kế hoạch nền | "Mô hình học từ ít mẫu có sai số, nhưng vẫn cho thêm nhiều cập nhật từ mỗi bước thật." (20) | mô hình phân phối · mô hình đếm · bất định nhận thức · Dyna-Q · cập nhật mẫu |
| `L11-3-00` | 3. Tìm kiếm theo cây Monte Carlo | "Tìm kiếm từ trạng thái hiện tại dồn phép tính vào đúng một quyết định." (15) | thuật toán rollout · cận tin cậy trên · chính sách cây · UCT |
| `L11-4-00` | 4. Tối ưu kế hoạch dựa trên đạo hàm | "Khi mô hình khả vi, đạo hàm theo chuỗi hành động chỉ hướng sửa kế hoạch." (16) | tối ưu quỹ đạo · lan truyền ngược qua mô hình · chân trời lùi · sai số tích lũy |
| `L11-5-00` | 5. Học tăng cường phân cấp | "Gộp nhiều bước thành một tùy chọn giúp kế hoạch nhảy qua những đoạn dài." (15) | tùy chọn · mô hình tùy chọn · bán-MDP · lặp giá trị với tùy chọn |
| `L11-6-00` | 6. Tổng kết | "Mỗi cách dùng mô hình đổi phép tính lấy chất lượng dưới giả thiết riêng." (15) | — |

Tên mạch phải khác tiêu đề trang nội dung đầu tiên của mạch (NT12): mạch 3 có trang đầu "Ví dụ: rollout tại ô F", mạch 5 có trang đầu "Ví dụ: tùy chọn đi tới cửa" — đạt.

## 2. Mạch 1 — Mở đầu (6 trang; NT11, P5, NT-RL-8)

| Mã | Tiêu đề | Chức năng | Nguồn ghi chú | Ghi chú cho người soạn |
|---|---|---|---|---|
| `L11-1-01` | Lập kế hoạch dựa trên mô hình | bìa (NT11, NT-RL-8) | tiêu đề, §2 của kế hoạch | tên học phần; "Bài 11"; tên bài như ghi chú; luận điểm một câu có điều kiện, dự thảo: "Khi mô hình đúng trên những trạng thái mà kế hoạch đi qua, phép tính trên mô hình thay được tương tác thật; ngoài vùng đó, sai số của mô hình tích lũy theo chân trời." (một câu; kiểm lại bằng `no-ai-slop` Edit); "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội"; "Năm học 2026–2027, học kỳ 1"; không tên giảng viên |
| `L11-1-02` | Tiên quyết và quy ước | "Nhắc lại:" theo mục Kiến thức tiên quyết; "Ký hiệu:" | Kiến thức tiên quyết, Bảng ký hiệu | "Nhắc lại:" bốn dòng: Q-learning và hội tụ (Định lý 06.21); cải thiện chính sách (Định lý 04.13); lặp giá trị bất đồng bộ (Định lý 04.32); Hoeffding (Mệnh đề 06.26). "Ký hiệu:" $\mathcal S$, $\mathcal A(s)$, $R_{t+1}$, $\gamma$, $\hat p$, $C(s,a)$; kỳ vọng theo chính sách và động lực. Rủi ro mật độ (mục 9) |
| `L11-1-03` | Mục tiêu học tập | bảy mục tiêu, đủ động từ, rút chữ | Mục tiêu học tập | trần 80 âm tiết; ngoại lệ có thể cần (mục 9) |
| `L11-1-04` | Nội dung | danh sách đánh số sáu mạch, liên kết `#/1` … `#/6`; dòng đọc trước: Sutton và Barto (2018), Chương 8, §17.2 | §6 kế hoạch ghi chú | tên trùng `h2` của trang tiêu đề mạch |
| `L11-1-05` | Ngữ cảnh: mê cung hai phòng | trang bổ sung P5 (gộp "Ngữ cảnh" ≤ 4 dòng và trang khung chung) | Ví dụ 11.1; §1.2 | hình `me-cung-hai-phong-slide.svg`; bốn dòng: tám ô, trượt $0{,}2$, phần thưởng $+1$ vào $\mathrm Z$, $\gamma=0{,}9$; một dòng khung "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách" (trang tổng quan: không ký hiệu mới ngoài tên ô, NT9) |
| `L11-1-06` | Vấn đề trung tâm | một hộp "Câu hỏi:" duy nhất | §1.1 | câu hỏi của `ke-hoach-ghi-chu.md` mục 2; ghi chú diễn giả liệt kê câu trả lời theo mạch 2–5 (NT11) |

## 3. Mạch 2 — Tính bất định và lập kế hoạch nền (12 trang; §2 của ghi chú)

Hành trình (NT8): mô hình (vấn đề → trực quan → ví dụ → định nghĩa) → bất định (ví dụ → mệnh đề → định nghĩa → bài tập) → Dyna (giới hạn của Q-learning → ví dụ tính tay → thuật toán → bảo đảm) → mô hình sai (ví dụ → định nghĩa → ví dụ số) → cập nhật kỳ vọng và mẫu (ví dụ → mệnh đề) → bài tập.

| Mã | Tiêu đề | Chức năng, bước hành trình | Nguồn ghi chú | Nội dung mặt trang (rút gọn) |
|---|---|---|---|---|
| `L11-2-00` | 2. Tính bất định và lập kế hoạch nền | tiêu đề mạch | §2 | mục 1 |
| `L11-2-01` | Ví dụ: mô hình của cặp $(\mathrm F,\rightarrow)$ | vấn đề + ví dụ + định nghĩa gọn | Ví dụ 11.2; Định nghĩa 11.1, 11.2 | "Câu hỏi:" của mạch; mô hình phân phối $\{\mathrm K:0{,}8;\ \mathrm F:0{,}2\}$ so với mô hình mẫu; kỳ vọng mục tiêu $0{,}36$ hai cách; một dòng "lập kế hoạch nền / tại thời điểm quyết định" |
| `L11-2-02` | Mô hình đếm | ví dụ → định nghĩa → mệnh đề | Ví dụ 11.3; Định nghĩa 11.4; Mệnh đề 11.5 | bảng đếm sau lượt thứ nhất ($\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$); $\hat p=C(s,a,s')/C(s,a)$; "Kết luận:" $\mathbb E\hat p=p$, $\operatorname{Var}\hat p=p(1-p)/n$ với giả thiết lần thử độc lập, $n$ cố định; "Chứng minh." một dòng (tổng Bernoulli) |
| `L11-2-03` | Bất định ngẫu nhiên và bất định nhận thức | trực quan → định nghĩa → ví dụ số | Ví dụ 11.4, 11.5; Định nghĩa 11.6; Nhận xét 11.7 | "Trực quan." một dòng; bảng $C=2,5,50$: $0{,}283$; $0{,}179$; $0{,}057$ so với $p(1-p)=0{,}16$; một dòng tập ba mô hình ($0$; $0{,}5$; $1$) |
| `L11-2-04` | Bài tập: hai loại bất định | kiểm tra (NT24) | Bài tập 11.2 | đề bốn câu đúng/sai; "Lời giải:" fragment |
| `L11-2-05` | Ví dụ: lượt thứ nhất của Dyna-Q, cập nhật trực tiếp | giới hạn của Q-learning (NT-RL-3) → ví dụ | §2.4; Ví dụ 11.7 (nửa đầu) | dòng mở: "Q-learning dùng mỗi mẫu thật một lần: sau lượt thứ nhất chỉ $Q(\mathrm K,\rightarrow)=0{,}5$."; năm mẫu chuyển; bước (d), (e); hình `kien-truc-dyna-slide.svg` (có thể đặt ở ghi chú diễn giả nếu chật, mục 9) |
| `L11-2-06` | Ví dụ: lượt thứ nhất của Dyna-Q, hai cập nhật lập kế hoạch | ví dụ tính tay trước giả mã (NT-RL-2) + bảo đảm | Ví dụ 11.6, 11.7; Mệnh đề 11.9 | khuôn bảng cố định `cặp | mục tiêu | sai lệch | giá trị mới` (NT-RL-5): $(\mathrm F,\rightarrow)$: $0{,}45$; $0{,}45$; $0{,}225$. $(\mathrm K,\rightarrow)$: $1$; $0{,}5$; $0{,}75$. "Bảo đảm:" Q-planning hội tụ tới $\hat q_*$ của mô hình khi mô hình cố định, mọi cặp được chọn vô hạn lần, bước học Robbins–Monro (Mệnh đề 11.9) |
| `L11-2-07` | Thuật toán Dyna-Q | thuật toán | Thuật toán 11.10 | "Đầu vào:", "Đầu ra:", bước (a)–(f), giả thiết tất định ở (e); trang riêng vì giả mã > 8 dòng (`CLAUDE.md` "Density") |
| `L11-2-08` | Mô hình sai và thưởng thăm dò | ví dụ → định nghĩa → ví dụ số | Ví dụ 11.8, 11.9; Định nghĩa 11.12 | mê cung đổi cửa: $(\mathrm F,\rightarrow)$ lạc quan tự sửa, $(\mathrm B,\rightarrow)$ bi quan không tự sửa; $\hat r+\kappa\sqrt{\ell}$; $\kappa=0{,}01$, $\ell=400$: mục tiêu $0{,}74$, giá trị mới $0{,}64>0{,}6$ |
| `L11-2-09` | Cập nhật kỳ vọng và cập nhật mẫu | ví dụ → định nghĩa → mệnh đề | Ví dụ 11.10, 11.11; Định nghĩa 11.14; Mệnh đề 11.15 | $(\mathrm A,\rightarrow)$: $0{,}45$ so với $0{,}54$/$0{,}36$; "Kết luận:" sai số $\sqrt{(b-1)/(bk)}$ dưới giả thiết của Mệnh đề 11.15(b); $b=100$, $k=10$: $0{,}315$ với một phần mười chi phí; hình `cap-nhat-ky-vong-va-mau-slide.svg` hoặc chỉ bảng (mục 9) |
| `L11-2-10` | Bài tập: bước thật đầu của lượt thứ hai | kiểm tra (NT24) | Bài tập 11.4 | đề với dữ kiện chép lại |
| `L11-2-11` | Bài tập: bước thật đầu của lượt thứ hai | lời giải | Bài tập 11.4 | "Lời giải:" cùng khuôn bảng: $Q(\mathrm A,\rightarrow)=0$; $Q(\mathrm F,\rightarrow)=0{,}45$; $Q(\mathrm B,\downarrow)=0{,}2025$; câu nối mạch trên mặt trang (NT13): "Dyna cập nhật mọi cặp đã gặp, kể cả cặp xa trạng thái hiện tại." |

Đọc thêm (§2.7: quét ưu tiên, lấy mẫu theo quỹ đạo, RTDP và Định lý 11.19) chỉ nằm ở ghi chú diễn giả của `L11-2-06` hoặc `L11-2-09`, có câu "nội dung đọc thêm của ghi chú" (NT5).

## 4. Mạch 3 — Tìm kiếm theo cây Monte Carlo (11 trang; §3 của ghi chú)

Hành trình: rollout (vấn đề → ví dụ → phát biểu → ý tưởng chứng minh → ứng dụng: số mô phỏng) → UCB (vấn đề: chia đều lãng phí → ví dụ → định nghĩa → bảo đảm) → MCTS (ví dụ tính tay → thuật toán → bảo đảm → thực hành) → bài tập.

| Mã | Tiêu đề | Chức năng | Nguồn ghi chú | Nội dung mặt trang |
|---|---|---|---|---|
| `L11-3-00` | 3. Tìm kiếm theo cây Monte Carlo | tiêu đề mạch | §3 | mục 1 |
| `L11-3-01` | Ví dụ: rollout tại ô $\mathrm F$ | vấn đề + ví dụ | Ví dụ 11.12; Định nghĩa 11.20 | câu khẳng định của mạch; chính sách cơ sở ngẫu nhiên đều; $q_{\pi_0}(\mathrm F,\cdot)$: $\rightarrow$ $0{,}389$; $\downarrow$ $0{,}181$; $\uparrow$, $\leftarrow$ $0{,}118$; chọn $\rightarrow$ |
| `L11-3-02` | Tính chất cải thiện của rollout | phát biểu + ví dụ + ứng dụng | Mệnh đề 11.21, 11.22; Ví dụ 11.13, 11.14 | "Giả thiết:" $q_{\pi_0}$ chính xác, $\pi_0$ Markov dừng, $\gamma<1$; "Kết luận:" $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$; số: $0{,}2016\to0{,}8566$; "Lưu ý:" với $m$ mô phỏng, xác suất chọn sai $\le\exp(-m\Delta^2/B^2)$; $m=70$ cho $\le0{,}05$ |
| `L11-3-03` | Ý tưởng chứng minh: tính chất cải thiện của rollout | NT6 | chứng minh Mệnh đề 11.21 | ba bước: $q_{\pi_0}(s,\pi_{\mathrm{ro}}(s))=\max_aq_{\pi_0}(s,a)$; $\ge\sum_a\pi_0(a\mid s)q_{\pi_0}(s,a)=v_{\pi_0}(s)$; áp dụng Định lý 04.13 "(giả thiết $q_{\pi_0}$ chính xác)" |
| `L11-3-04` | Quy tắc cận tin cậy trên | vấn đề → ví dụ → định nghĩa → bảo đảm | Ví dụ 11.15; Định nghĩa 11.23; Định lý 11.24 | dòng mở: rollout chia đều $m$ cho cả hành động đã rõ là kém; hai hành động: $1{,}189$ so với $1{,}420$; công thức chỉ số; "Bảo đảm:" UCB1, phần thưởng trong $[0,1]$, phân phối không đổi: hối tiếc tăng theo $\ln t$ |
| `L11-3-05` | Ví dụ: một vòng MCTS tại $\mathrm F$, pha chọn | ví dụ tính tay (NT-RL-2) | Ví dụ 11.16 (bước 1); Định nghĩa 11.25 | khuôn bảng cố định `cạnh | N | Q̄ | số hạng thăm dò | chỉ số` (NT-RL-5): $1{,}421$; $1{,}620$; $1{,}742$; $1{,}642$; chọn $\uparrow$; hình `mcts-bon-pha-slide.svg` |
| `L11-3-06` | Ví dụ: một vòng MCTS tại $\mathrm F$, mở rộng, mô phỏng, cập nhật ngược | ví dụ tính tay | Ví dụ 11.16 (bước 2–5) | mở rộng $\mathrm B$; mô phỏng ba bước; $G=\gamma^3=0{,}729$; $N=2$, $W=1{,}029$, $\bar Q=0{,}5145$; $N(\mathrm F)=9$; hành động thật: $N$ lớn nhất |
| `L11-3-07` | Thuật toán MCTS với UCT | thuật toán | Thuật toán 11.26 | "Đầu vào:", "Đầu ra:", bốn pha đánh số, điều kiện dừng (ngân sách) |
| `L11-3-08` | Bảo đảm của UCT | phát biểu + thực hành | Định lý 11.27; Nhận xét 11.28 | "Giả thiết:" chân trời hữu hạn, phần thưởng trong $[0,1]$, số hạng thăm dò theo bài báo; "Bảo đảm:" xác suất chọn sai tại gốc $\to0$ (dạng định lượng chỉ khi ghi chú đã kiểm, QG3 của ghi chú); một dòng AlphaGo Zero (SB §16.6.2): mạng cho xác suất tiên nghiệm và giá trị lá; ghi chú diễn giả: chứng minh nằm ngoài phạm vi, ý tưởng quy nạp theo độ sâu (NT6 cho kết quả dẫn) |
| `L11-3-09` | Bài tập: vòng MCTS tiếp theo | kiểm tra | Bài tập 11.5 | đề với bảng cùng khuôn `L11-3-05` |
| `L11-3-10` | Bài tập: vòng MCTS tiếp theo | lời giải | Bài tập 11.5 | chỉ số $1{,}441$; $1{,}648$; $1{,}563$; $1{,}682$; chọn $\leftarrow$; $\bar Q(\mathrm F,\leftarrow)=0{,}4645$; câu nối (NT13): "MCTS liệt kê cạnh của một tập hành động hữu hạn." |

## 5. Mạch 4 — Tối ưu kế hoạch dựa trên đạo hàm (11 trang; §4 của ghi chú)

Hành trình: tối ưu kế hoạch (giới hạn của MCTS → ví dụ dẫn nhập → định nghĩa và một bước gradient tính tay → mệnh đề truy hồi ngược với hai bản cùng kết quả → thuật toán → nghiệm) → MPC (vòng hở không phản ứng → định nghĩa → ví dụ → thuật toán gọn) → phương án không đạo hàm (ví dụ → thuật toán) → sai số tích lũy (ví dụ → mệnh đề → ứng dụng với mô hình sai) → bài tập. Bước tính tay đứng trước mọi giả mã (NT-RL-2): `L11-4-02` trước `L11-4-04`; `L11-4-05` có ví dụ trước dòng thuật toán.

| Mã | Tiêu đề | Chức năng | Nguồn ghi chú | Nội dung mặt trang |
|---|---|---|---|---|
| `L11-4-00` | 4. Tối ưu kế hoạch dựa trên đạo hàm | tiêu đề mạch | §4 | mục 1 |
| `L11-4-01` | Ví dụ: xe trên đường ray | vấn đề + ví dụ dẫn nhập | Ví dụ 11.17 | câu khẳng định của mạch; dữ kiện liệt kê ngay (NT14): $\hat f(x,u)=x+u$, $c=x_{t+1}^2+u_t^2$, $h=2$, $x_0=2$; $J(0,0)=8$ |
| `L11-4-02` | Bài toán tối ưu kế hoạch | định nghĩa + ví dụ tính tay | Định nghĩa 11.29; Ví dụ 11.18 | biến là $(u_0,u_1)$, trạng thái thế bằng mô hình; gradient khai triển $(8,4)$; $\eta=0{,}1$: $(-0{,}8;\ -0{,}4)$, $J=2{,}88$ |
| `L11-4-03` | Đạo hàm qua mô hình bằng truy hồi ngược | mệnh đề + hai bản cùng kết quả (GC-RL-11) | Mệnh đề 11.30 | $\lambda_2=2x_2=4$, $\lambda_1=2x_1+\lambda_2=8$; $\partial J/\partial u_1=4$, $\partial J/\partial u_0=8$; "Kết luận:" công thức $\lambda_t$; "Chứng minh." một dòng (quy tắc dây chuyền) |
| `L11-4-04` | Thuật toán tối ưu kế hoạch bằng hạ gradient | thuật toán + kết quả số | Thuật toán 11.31; Ví dụ 11.19 | bước xuôi, bước ngược, cập nhật, dừng; nghiệm $(-1{,}2;\ -0{,}4)$, $J^*=2{,}4$ |
| `L11-4-05` | Điều khiển dự báo theo chân trời lùi | định nghĩa + ví dụ + thuật toán gọn | Định nghĩa 11.32; Ví dụ 11.20; Thuật toán 11.33 | luật $u=-0{,}6x$; $2;\ 0{,}8;\ 0{,}32;\ 0{,}128$; hình `xe-tren-duong-ray-slide.svg` (phần kế hoạch và MPC) |
| `L11-4-06` | Bắn ngẫu nhiên và phương pháp entropy chéo | phương án không đạo hàm (bổ sung) | Ví dụ 11.21; Thuật toán 11.34; Nhận xét 11.35 | bảng bốn ứng viên ($8$; $3$; $2{,}5$; $4$); mẫu ưu tú, trung bình mới $(-1;\ -0{,}25)$; một dòng so sánh với gradient. Trang có thể bỏ ở phương án 58 trang (QT3) |
| `L11-4-07` | Sai số mô hình tích lũy | ví dụ → mệnh đề | Ví dụ 11.22; Mệnh đề 11.36 | hệ thật $1{,}2x+u$; $e_k$: $0{,}4$; $0{,}88$; $1{,}456$; "Kết luận:" $e_k\le\bar e(L^k-1)/(L-1)$; "Chứng minh." một dòng ($e_{j+1}\le Le_j+\bar e$); hình `sai-so-tich-luy-slide.svg` |
| `L11-4-08` | Ví dụ: vòng hở và điều khiển dự báo với mô hình sai | ứng dụng | Ví dụ 11.23; Tình huống 11.1 | vòng hở $1{,}2$; $1{,}04$ (mô hình dự báo $0{,}8$; $0{,}4$); MPC với mô hình sai $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$; "Diễn giải:" lập lại kế hoạch dùng trạng thái thật |
| `L11-4-09` | Bài tập: kế hoạch hai bước từ $x_0=1$ | kiểm tra | Bài tập 11.6 | đề |
| `L11-4-10` | Bài tập: kế hoạch hai bước từ $x_0=1$ | lời giải | Bài tập 11.6 | $(4,2)$ hai cách; $(-0{,}4;\ -0{,}2)$, $J=0{,}72$; $(-0{,}6;\ -0{,}2)$, $J^*=0{,}6$; câu nối (NT13): "Chân trời dài làm sai số và số bước tính cùng tăng." |

## 6. Mạch 5 — Học tăng cường phân cấp (11 trang; §5 của ghi chú)

Hành trình: tùy chọn (giới hạn của lập kế hoạch từng bước → ví dụ → định nghĩa) → mô hình tùy chọn (ví dụ tính tay → định nghĩa → mệnh đề) → phương trình Bellman bán-MDP (phát biểu → ý tưởng chứng minh) → lập kế hoạch nhiều mức (ví dụ → định lý) → Q-learning bán-MDP (ví dụ tính tay → thuật toán) → bài tập.

| Mã | Tiêu đề | Chức năng | Nguồn ghi chú | Nội dung mặt trang |
|---|---|---|---|---|
| `L11-5-00` | 5. Học tăng cường phân cấp | tiêu đề mạch | §5 | mục 1 |
| `L11-5-01` | Ví dụ: tùy chọn đi tới cửa | vấn đề + ví dụ | §5.1; Ví dụ 11.24, 11.26 (bảng lượt quét) | câu khẳng định của mạch; sau sáu lượt quét $v(\mathrm A)=0{,}6103$ so với $v_*(\mathrm A)=0{,}6604$; tùy chọn "đi tới cửa", "đi tới đích" trên hình `tuy-chon-hai-phong-slide.svg` |
| `L11-5-02` | Tùy chọn và chính sách phân cấp | định nghĩa | Định nghĩa 11.38, 11.39 | $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$; hành động một bước là tùy chọn với $\beta\equiv1$; chính sách phân cấp $\mu(\omega\mid s)$; "Lưu ý:" SB viết $\gamma_\omega=1-\beta_\omega$ |
| `L11-5-03` | Ví dụ: mô hình của hai tùy chọn | ví dụ tính tay | Ví dụ 11.25 | $\rho=0{,}72/0{,}82=0{,}878$; $p(\mathrm K\mid\mathrm F)=0{,}878$; $p(\mathrm K\mid\mathrm B)=0{,}771$; $p(\mathrm K\mid\mathrm A)=0{,}677$; $r(\mathrm K,\omega_{\mathrm{đích}})=0{,}976$ |
| `L11-5-04` | Mô hình tùy chọn | định nghĩa + mệnh đề | Định nghĩa 11.40; Mệnh đề 11.41 | $r(s,\omega)$, $p(s'\mid s,\omega)$ dạng (17.2), (17.3) (không ghi số công thức của sách trên mặt trang, chỉ ghi chú diễn giả); "Kết luận:" $\sum_{s'}p(s'\mid s,\omega)=\mathbb E[\gamma^\tau]\le\gamma$; "Chứng minh." một dòng ($\tau\ge1$) |
| `L11-5-05` | Phương trình Bellman cho chính sách phân cấp | kết quả chính | Định lý 11.42 | "Giả thiết:" MDP hữu hạn, $\gamma<1$, tùy chọn Markov, kết thúc với xác suất $1$, $\beta_\omega$ chỉ phụ thuộc trạng thái; "Kết luận:" phương trình; "Ý nghĩa:" với hành động một bước, trở về Định lý 03.21 |
| `L11-5-06` | Ý tưởng chứng minh: phương trình Bellman cho chính sách phân cấp | NT6 | chứng minh Định lý 11.42 | bốn bước: tách lợi tức tại $\tau$; kỳ vọng phần đầu là $r(s,\omega)$; phần sau có kỳ vọng $v_\mu(S_\tau)$ "(giả thiết: kết thúc chỉ phụ thuộc trạng thái, tính Markov)"; gom theo $\mu$ |
| `L11-5-07` | Lặp giá trị với tùy chọn | ví dụ + định lý | Ví dụ 11.26; Định lý 11.44; Thuật toán 11.45 | vòng 1, vòng 2: $v_2(\mathrm A)=0{,}677\cdot0{,}976=0{,}660=v_*(\mathrm A)$; "Bảo đảm:" $T_\Omega$ co hệ số $\gamma$, hội tụ tới $v_\Omega$; $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$ |
| `L11-5-08` | Q-learning bán-MDP | ví dụ + thuật toán gọn | Ví dụ 11.27; Thuật toán 11.46 | mục tiêu $\sum_j\gamma^{j-1}R_j+\gamma^k\max_{\omega'}Q(S_k,\omega')$; $k=3$: $0{,}729\cdot0{,}9=0{,}6561$, giá trị mới $0{,}328$; "Lưu ý:" chiết khấu $\gamma^k$, không phải $\gamma$ ($0{,}405$ là kết quả sai) |
| `L11-5-09` | Bài tập: mô hình tùy chọn khi trượt nhiều hơn | kiểm tra | Bài tập 11.7 | đề |
| `L11-5-10` | Bài tập: mô hình tùy chọn khi trượt nhiều hơn | lời giải | Bài tập 11.7 | $\rho=0{,}818$; $p=0{,}669$; $r=0{,}909$; $v_\mu(\mathrm B)=0{,}609$; kiểm $q=0{,}2$ cho $0{,}878$ |

## 7. Mạch 6 — Tổng kết (9 trang; §6, Tình huống, Tóm tắt của ghi chú; NT15, NT-RL-9, P4)

| Mã | Tiêu đề | Nội dung |
|---|---|---|
| `L11-6-00` | 6. Tổng kết | trang tiêu đề mạch (mục 1) |
| `L11-6-01` | Bảng tổng kết | `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` (P4), mỗi kết quả chính một hàng, giữ lượng từ và loại bảo đảm (NT2): Mệnh đề 11.5 (lần thử độc lập, $n$ cố định; $\operatorname{Var}\hat p=p(1-p)/n$); Mệnh đề 11.9 (mô hình cố định, mọi cặp vô hạn lần, Robbins–Monro; $Q\to\hat q_*$ hầu chắc chắn); Mệnh đề 11.15 (giá trị kế đúng, mẫu độc lập; $\sqrt{(b-1)/(bk)}$); Mệnh đề 11.21 ($q_{\pi_0}$ chính xác; $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$); Định lý 11.27 (chân trời hữu hạn, phần thưởng $[0,1]$; xác suất chọn sai $\to0$); Mệnh đề 11.36 (vòng hở, $f$ Lipschitz; $\bar e(L^k-1)/(L-1)$); Định lý 11.42, 11.44 (tùy chọn Markov kết thúc với xác suất $1$; phương trình bán-MDP, co hệ số $\gamma$). Trần 80 âm tiết; ngoại lệ có thể cần (mục 9) |
| `L11-6-02` | So sánh bốn cách dùng mô hình | bảng P4 bổ sung `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng`, bốn hàng: Dyna-Q (Q-learning trên mẫu thật và mẫu mô hình; mẫu thật và mô hình đếm; ngân sách bước thật); MCTS (trung bình lợi tức trên cạnh, chỉ số UCT; mô phỏng từ trạng thái hiện tại; hết ngân sách vòng lặp); tối ưu bằng gradient trong MPC ($u\leftarrow u-\eta\nabla J$; mô hình khả vi; gradient nhỏ hoặc hết ngân sách, lặp mỗi bước thời gian); lặp giá trị với tùy chọn ($T_\Omega$; mô hình tùy chọn; phần dư dưới ngưỡng). Bảng thứ ba của P4 (`Phương pháp | Giả thiết không được bỏ | Kết luận`) gộp vào `L11-6-01` (QT5) |
| `L11-6-03` | Vấn đề trung tâm | câu trả lời có điều kiện cho cả bài, không theo mạch (NT15): bốn dòng từ `ke-hoach-ghi-chu.md` mục 2 (Dyna: $Q(\mathrm F,\rightarrow)=0{,}225$ sau một lượt; rollout: $0{,}2016\to0{,}8566$, $m=70$; MPC: $8\to2{,}88$, vòng kín co với hệ số $0{,}6$ dù mô hình sai; tùy chọn: hai vòng so với sáu lượt quét); nguồn ở ghi chú diễn giả |
| `L11-6-04` | Bài tập: mô hình đếm và tùy chọn trên mê cung hai phòng | bài tập tổng hợp (NT15, NT-RL-9): Bài tập 11.10, đề bốn câu |
| `L11-6-05` | Bài tập: mô hình đếm và tùy chọn trên mê cung hai phòng | "Lời giải:" bốn dòng: $0{,}75$ và $0{,}2165$; $0{,}7648$ và $0{,}9756$; $\hat v(\mathrm B)=0{,}7461$; sai số $-0{,}0061$ so với $+0{,}0578$ của mô hình tất định |
| `L11-6-06` | Câu hỏi tự kiểm tra | "Câu hỏi: trả lời và nêu kết quả đã dùng." rồi ba hoặc bốn câu của §6.3 ghi chú, mỗi câu kiểm một giả thiết hoặc một phân biệt (NT-RL-9); lời đáp ở ghi chú diễn giả |
| `L11-6-07` | Bài tập về nhà | bảng `Mục | Bài tập` theo mạch (đúng bảng của `ke-hoach-bai-tap.md` mục 7), "(trên lớp)" cho 11.2, 11.4, 11.5, 11.6, 11.7, 11.10; liên kết "Ghi chú bài giảng · Bài tập" tới `material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` và `…exercises.md…` |
| `L11-6-08` | Tài liệu tham khảo | nguồn mà ghi chú dẫn (Sutton và Barto 2018, §2.7, Chương 8, §16.6, §17.2; Bertsekas 2019; Szepesvári 2010; Puterman 1994; bài báo gốc theo QG3), tác giả, năm, mục; một dòng nối sang bài sau theo QG7 |

Không khái niệm mới trong mạch 6 (NT15).

## 8. Số trang và thời lượng (P6, NT27; thời lượng chỉ ở planning)

| Mạch | Trang | Phút | Ghi chú |
|---:|---:|---:|---|
| 1 | 6 | 8 | |
| 2 | 12 | 30 | hai cụm (bất định; Dyna), hai bài trên lớp |
| 3 | 11 | 26 | |
| 4 | 11 | 24 | |
| 5 | 11 | 22 | |
| 6 | 9 | 10 | |
| **Tổng** | **60** | **120** | P6: 45–55, trần 60 khi có lý do |

**Lý do vượt 55** (ghi vào storyboard và `review-log.md`): bài gồm bốn họ phương pháp ứng với bốn mục 11.1–11.4 của giáo trình; mỗi họ cần ví dụ tính tay trước giả mã (NT-RL-2), trang thuật toán riêng khi giả mã quá tám dòng, và một bài có lời giải trên mặt trang (NT24); mạch 2 có hai cụm khái niệm (bất định; Dyna). Không có trang chỉ để trang trí. Phương án 58 trang ở QT3.

## 9. Mật độ: rủi ro và ngoại lệ dự kiến (NT17, NT18, NT-RL-7)

Số âm tiết lấy bằng `deck_lint.py --course rl-plan`, không đếm tay (NT17). Ngoại lệ ghi trong storyboard kèm lý do và số âm tiết, không vượt 1,5 lần trần.

| Trang | Rủi ro | Cách xử lý dự kiến |
|---|---|---|
| `L11-1-02` | bốn dòng "Nhắc lại:" kèm phát biểu | rút còn tên kết quả và một mệnh đề; phần phát biểu đầy đủ ở ghi chú diễn giả; nếu vẫn vượt 60, ngoại lệ có lý do |
| `L11-1-03` | bảy mục tiêu | trần 80; ngoại lệ "giữ đúng nghĩa ghi chú" nếu vượt |
| `L11-2-03`, `L11-2-09` | định nghĩa, mệnh đề và bảng số cùng trang | tách hình sang ghi chú diễn giả; nếu vẫn vượt, tách thành hai trang và bỏ `L11-4-06` để giữ 60 |
| `L11-2-05`, `L11-2-06` | năm mẫu chuyển và bảng cập nhật | mẫu chuyển dạng danh sách một dòng mỗi mẫu (VP12); bảng số không tính âm tiết |
| `L11-2-07`, `L11-3-07` | giả mã | trang riêng; giả mã không quá 10 dòng; chi tiết chi phí ở ghi chú diễn giả |
| `L11-2-08` | hai kiểu sai của mô hình và một phép tính | hai gạch đầu dòng ngắn; phép tính ba dòng mục tiêu/sai lệch/giá trị mới |
| `L11-3-02` | mệnh đề, số liệu và "Lưu ý:" Hoeffding | "Lưu ý:" một dòng; có thể chuyển Mệnh đề 11.22 sang ghi chú diễn giả |
| `L11-3-08` | định lý dẫn với nhiều giả thiết và dòng AlphaGo Zero | giả thiết dạng danh sách ba mục; AlphaGo Zero một dòng |
| `L11-6-01`, `L11-6-02` | bảng tám hàng, bảng bốn hàng | trần 80 (bảng tổng kết, bảng so sánh); công thức trong ô dùng KaTeX |
| `L11-2-10`, `L11-6-04` | đề giữ nguyên câu chữ | ngoại lệ thường gặp của NT17 |

Chữ thân bài từ `0.75em` (NT-RL-7); không thu nhỏ chữ để vừa trang.

## 10. Hình (NT25; dùng chung với ghi chú, `ke-hoach-ghi-chu.md` mục 14)

| Hình ghi chú | Bản trang chiếu | Trang |
|---|---|---|
| `me-cung-hai-phong.svg` | `me-cung-hai-phong-slide.svg` (chữ ≥ 16 px ở 390 px; bản `-slide-narrow.svg` nếu cần) | `L11-1-05` |
| `kien-truc-dyna.svg` | `kien-truc-dyna-slide.svg` | `L11-2-05` |
| `cap-nhat-ky-vong-va-mau.svg` | `cap-nhat-ky-vong-va-mau-slide.svg` (tùy mật độ) | `L11-2-09` |
| `mcts-bon-pha.svg` | `mcts-bon-pha-slide.svg` | `L11-3-05`, `L11-3-06` |
| `xe-tren-duong-ray.svg` | `xe-tren-duong-ray-slide.svg` | `L11-4-05`, `L11-4-08` |
| `sai-so-tich-luy.svg` | `sai-so-tich-luy-slide.svg` | `L11-4-07` |
| `tuy-chon-hai-phong.svg` | `tuy-chon-hai-phong-slide.svg` | `L11-5-01` (và `L11-5-03` nếu cần) |

`cau-truc-chuong.svg` chỉ dùng trong ghi chú; `L11-1-05` thay bằng một dòng khung. Mọi số trên hình mà chữ hoặc trang sau dùng tới cũng có trong chữ trên mặt trang (NT25). Không dùng lại SVG của Bài 11 cũ; không raster. Hình vẽ bằng script đặt trong `tools/courses/rl-plan/2627-1/img/lec-11/` (workspace `CLAUDE.md` "Tooling stays out of course repos").

## 11. Kỹ thuật, nhãn và kiểm tra

- **Nhãn** (NT19, P3): "Kết luận:" cho mệnh đề tất định (11.5, 11.15, 11.21, 11.30, 11.36, 11.41, 11.42); "Bảo đảm:" cho kết quả hội tụ hoặc xác suất (11.9, 11.24, 11.27, 11.44); "Đầu vào:", "Đầu ra:" cho trang thuật toán; không "Nhu cầu:", không "Đáp án".
- **Kỹ thuật** (NT7): "Kỹ thuật." một trang không cần: chặn hợp và Hoeffding đã có ở Bài 06 ("Nhắc lại:" ở `L11-1-02`); quy tắc dây chuyền ngược là nội dung của Mệnh đề 11.30, không phải kỹ thuật dùng lại. Storyboard giữ danh sách: "tách lợi tức tại thời điểm dừng" (Định lý 11.42) ghi một dòng "Kỹ thuật." trên `L11-5-06`.
- **Câu trên mặt trang** (NT18): không "chúng ta", "ta thấy", "hãy"; một câu kết có điều kiện hoặc con số.
- **Ghi chú diễn giả** (NT22): 40–150 âm tiết (đến ~250 cho ý tưởng chứng minh, bài tập, lời giải); kết bằng `<p class="note-source"><strong>Nguồn:</strong> ghi chú bài giảng Bài 11, §k (…); Sutton và Barto (2018), §… .</p>`; không mã trang, không thời lượng (VP8).
- **Công thức** (NT26, VP14): đo tràn ở 390 px; ngắt bằng `aligned`; không `\tag`; không `\text{}` tiếng Việt (tên tùy chọn theo QG5 của ghi chú).
- **Kiểm tra máy** (NT28, P10, `NGUYEN-TAC-HOC-PHAN.md` mục 5): `deck_check.py` (bản math-4-AI), `footer_check.py`, `deck_lint.py --course rl-plan` (0 phát hiện ngoài ngoại lệ đã ghi; với lược đồ `L11-k-mm`, phép kiểm bìa `L11-1-01` đạt), `formula_overflow.py` ở 390 × 844, ảnh 1600 × 900 và 390 × 844 (màn hẹp cuộn tới cuối), bàn phím, liên kết `#/k` của "Nội dung", trình xem ghi chú và bài tập với `&deck=`; máy chủ tĩnh tạm `python -m http.server <cổng> --bind 127.0.0.1` từ gốc repo.
- **Chỉ mục:** thẻ Bài 11 trên `2627-1/index.html` chỉ thêm sau khi ghi chú, bài tập, deck đều đạt kiểm định; bốn nhóm, "Thực hành: Chưa có" (P10).

## 12. Deck và tệp cũ của Bài 11

- Deck cũ `2627-1/lecture-11-cac-phuong-phap-gradient-chinh-sach-nang-cao.html` (đang theo dõi trong git; `.pdf` cạnh nó không theo dõi), 11 SVG cũ trong `2627-1/img/lec-11/` (đang theo dõi), `planning/lec-11/{outline,storyboard,review-log,note-for-author}.md` (đang theo dõi). Không sửa các tệp này trong giai đoạn kế hoạch.
- Đề xuất (QT1, QT6): xóa deck cũ và SVG cũ trong commit thêm deck mới (lịch sử git giữ bản cũ); `outline.md`, `storyboard.md` mới thay bản cũ; `review-log.md` giữ phần cũ và thêm mục mới "Dựng lại Bài 11: Lập kế hoạch dựa trên mô hình (2026-11)"; `note-for-author.md` cũ xóa cùng deck cũ hoặc giữ nếu tác giả còn cần các đề xuất trong đó.

## 13. Câu hỏi mở

| Mã | Câu hỏi | Đề xuất |
|---|---|---|
| QT1 | Tên tệp deck mới và số phận deck cũ, SVG cũ. | Tên `lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html`; xóa deck cũ và 11 SVG cũ trong commit thêm deck mới (không liên kết nào từ `index.html` tới deck cũ); nếu tác giả muốn giữ chủ đề gradient chính sách nâng cao, chuyển deck cũ sang số bài khác do tác giả chọn thay vì xóa. |
| QT2 | Sáu mạch (mỗi mục 11.1–11.4 một mạch) hay bảy mạch (tách 11.1 thành "Mô hình và tính bất định" và "Lập kế hoạch nền với Dyna")? | Sáu mạch: khớp mục lục giáo trình; bảy mạch thêm một trang tiêu đề mạch và tách cụm bất định khỏi Dyna, chỉ chọn nếu storyboard thấy mạch 2 quá tải (30 phút, 12 trang). |
| QT3 | 60 trang (trần P6) hay giảm. | 60 trang với lý do ở mục 8; phương án 58: bỏ `L11-4-06` (CEM chỉ ở ghi chú, một dòng "Cách khác:" trên `L11-4-04`) và gộp `L11-5-09`/`L11-5-10` thành một trang với "Lời giải:" dạng fragment nếu mật độ cho phép. |
| QT4 | Kết quả nào có trang "Ý tưởng chứng minh" riêng (NT6)? | Mệnh đề 11.21 (`L11-3-03`) và Định lý 11.42 (`L11-5-06`). Kết quả phụ có một dòng "Chứng minh." trên trang phát biểu: 11.5, 11.9, 11.15, 11.30, 11.36, 11.41. Kết quả dẫn (11.19, 11.24, 11.27, 11.44 phần (c)): lý do và ý tưởng trong ghi chú diễn giả. |
| QT5 | P4: bài nhiều thuật toán thêm hai bảng; có cần bảng thứ ba `Phương pháp | Giả thiết không được bỏ | Kết luận`? | Gộp vào bảng tổng kết `L11-6-01` (các định lý hội tụ đã là hàng của bảng đó); ghi lý do trong storyboard. |
| QT6 | `outline.md`, `storyboard.md`, `review-log.md` cũ của Bài 11. | Thay `outline.md`, `storyboard.md` bằng bản mới (bản cũ còn trong git); `review-log.md` giữ phần cũ, thêm mục mới. |
| QT7 | Trang "Ngữ cảnh" gộp với trang khung chung (P5) ở `L11-1-05`. | Gộp: bốn dòng dữ kiện mê cung và một dòng khung; không thêm trang khung riêng. |
| QT8 | Dòng nối sang bài sau trên `L11-6-08`. | Theo QG7 của `ke-hoach-ghi-chu.md`. |
