# Kế hoạch sửa Bài 07 theo chuẩn 2026-10-12

Tôi chỉ đọc. Không sửa, tạo hay xóa tệp nào và không commit; mọi tệp tạm nằm trong scratchpad.

Tệp đã đọc: deck `/data/tqlong/rl-plan/2627-1/lecture-07-xap-xi-ham.html`, gồm 40 trang và mọi ghi chú diễn giả; ghi chú `/data/tqlong/rl-plan/2627-1/materials/lec-07/lecture-note.md`, gồm 1 097 dòng, đọc toàn bộ; ô Markdown của hai notebook; `outline.md`, `storyboard.md`, `note-for-author.md` và các phần chính của `review-log.md`; các mục được giao trong AGENTS.md; hai mẫu học liệu; sản phẩm mẫu math-4-AI Bài 07. Tôi cũng xem thêm `sec_approximate_learning.tex` của giáo trình *Học máy thống kê*.

**Bốn điểm cần biết trước khi đọc:**

1. **Brief dùng tên "MC bán gradient", nhưng tên này sai với deck và quy ước của bài.** Deck, ghi chú và `note-for-author.md` đều khẳng định Monte Carlo là gradient đầy đủ, vì $G_t$ không chứa $w$; `note-for-author.md` cấm viết "bán gradient MC". Kế hoạch dùng tên "Monte Carlo gradient", theo Sutton–Barto §9.3.
2. **`density.py` đếm thừa công thức.** Script cộng thêm một lần cho mỗi `div.math-large` bao quanh `$$`. Đếm lại theo khối `$$` thì L07-14 có 2 khối; L07-15, L07-19, L07-20 và L07-30 có đúng 3 khối, nằm trong trần. Các cờ "công_thức" của năm trang này là giả. Số âm tiết và số dòng của script thì dùng được.
3. **Đây sẽ là deck Học tăng cường đầu tiên có trang tiêu đề mạch.** Các deck 01–12 chưa có `strand-title` nào. Lớp CSS đã có trong `lecture-slide.css` (11 lần xuất hiện).
4. **Ghi chú Bài 03–06 chưa có môi trường đánh số.** Không ghi chú nào có số hiệu `Định lý 0N.k`, nên mục "Kiến thức tiên quyết" chưa dẫn được số hiệu bài trước (câu hỏi D-Q4).

---

## A. Deck

### A1. Bảng mạch: hiện tại → đề xuất

Hiện deck có 6 mạch. Mạch M6 trộn nội dung mới (Q-learning, bộ ba bất ổn) với phần kết luận (L07-34, L07-35, L07-36) và ba trang chữa bài X01–X03. AGENTS yêu cầu mạch kết luận đứng riêng, mở bằng trang tiêu đề mạch và không đưa khái niệm mới.

**Đề xuất: 7 mạch**, vẫn trong khoảng 5–7.
- Lý do: tách M6 thành "Học khác chính sách và bộ ba bất ổn" và "Tổng kết và chuyển tiếp".
- Phương án thay thế 6 mạch: gộp mạch 5 và 6 thành "Điều khiển với xấp xỉ hàm". Tôi không khuyến nghị, vì Sarsa (theo chính sách) và Q-learning cùng bộ ba bất ổn là hai bước tiến riêng.
- Ghi lý do vào storyboard và review-log.

**Quy ước mã trang tiêu đề mạch.**
- Mã cũ `L07-NN` không có tiền tố mạch. Đề xuất `L07-<chữ mạch>00`, với A = mạch 1, B = mạch 2, …, G = mạch 7. Cách này giống kiểu `L05-B..` và `L06-C..` của Bài 05–06 và không trùng mã cũ.
- Hiện không trang nào có thuộc tính `id`, nên thêm `id="mach-N"` không làm hỏng liên kết nào.
- Trang mới khác dùng hậu tố `b`, `c`, … sau mã gần nhất, theo tiền lệ `L07-20b`.
- X01–X03 giữ mã khi chuyển vị trí.

| N | Mạch hiện tại (trang) | Tên mạch đề xuất | Dòng dẫn (âm tiết) | Từ khóa | Mã tiêu đề / `id` |
|---|---|---|---|---|---|
| 1 | M1 Mở đầu (L07-01–03) | Mở đầu; bìa là trang tiêu đề | — | — | L07-01 / không cần |
| 2 | M2 (L07-04–11) | Hàm giá trị tuyến tính theo đặc trưng | "Muốn ước lượng giá trị trên không gian trạng thái lớn, phải thay bảng bằng hàm tham số dùng chung." (20) | bảng tra · đặc trưng · tham số dùng chung · nhập nhằng · sai số xấp xỉ | `L07-B00` / `mach-2` |
| 3 | M3 (L07-12–17), nhận thêm X01 | Monte Carlo gradient với hàm xấp xỉ | "Muốn học $w$ khi chưa biết $v_\pi$, phải thay giá trị thật bằng lợi tức quan sát được." (16) | mục tiêu cập nhật · lợi tức · gradient đầy đủ · hạ gradient ngẫu nhiên · Robbins–Monro | `L07-C00` / `mach-3` |
| 4 | M4 (L07-18–25) | Bán gradient TD(0) và điểm cố định Bellman chiếu | "Muốn cập nhật sau từng chuyển tiếp, phải dùng mục tiêu bootstrap và xác định điểm mà cập nhật hướng tới." (21) | sai số TD · bán gradient · Bellman chiếu · phân phối dừng · Tsitsiklis–Van Roy | `L07-D00` / `mach-4` |
| 5 | M5 (L07-26–30), nhận thêm X02, X03 | Sarsa bán gradient cho điều khiển | "Muốn chọn hành động mà không cần mô hình, phải học $\hat q$ trong khi chính sách đổi theo $w$." (17) | giá trị hành động · ε-tham lam · chuỗi năm trạng thái · học theo chính sách | `L07-E00` / `mach-5` |
| 6 | Phần đầu M6 (L07-31–33) | Học khác chính sách và bộ ba bất ổn | "Muốn học $q_*$ từ dữ liệu thăm dò, phải xét khi nào bootstrap, khác chính sách và xấp xỉ hàm gây phân kỳ." (22) | Q-learning · mục tiêu cực đại · khác chính sách · bộ ba bất ổn | `L07-F00` / `mach-6` |
| 7 | Phần cuối M6 (L07-34–36) | Tổng kết và chuyển tiếp | "Nhu cầu: đối chiếu mỗi phương pháp với giả thiết bảo đảm của nó trước khi dùng mạng nơ-ron ở Bài 08." (22) | kết quả và giả thiết · khung cập nhật · phạm vi hội tụ · Bài 08 | `L07-G00` / `mach-7` |

Kiểm tra tên mạch:
- Không tên nào trùng tiêu đề trang nội dung đầu tiên của mạch. Các trang đầu lần lượt là L07-04 "Giới hạn của bảng tra", L07-12 "Mục tiêu mẫu thay cho giá trị thật", L07-18 "Mục tiêu TD(0) với hàm xấp xỉ", L07-26 "Giá trị hành động cho điều khiển", L07-31 "Mục tiêu Q-learning với hàm xấp xỉ".
- Ghi chú diễn giả của mỗi trang tiêu đề mạch dài 40–100 âm tiết, nêu: điều kế thừa, nhiệm vụ của mạch, điều giao cho mạch sau.

**Thời lượng mục tiêu theo mạch (120 phút):** 9 + 24 + 17 + 30 + 14 + 12 + 14.
- Chữa bài 30 phút (X01: 8, X02: 10, X03: 12) vẫn tính ngoài 120 phút. Các trang này nay nằm trong mạch 3 và 5.
- Deck tăng từ 40 lên khoảng 66 trang, nên phải rút ghi chú diễn giả và chuyển phần diễn giải dài sang ghi chú bài giảng.

### A2. Mạch mở đầu và mạch kết luận

**Mạch mở đầu, đối chiếu yêu cầu.** Thứ tự đích: bìa → Tiên quyết và quy ước → Mục tiêu → Nội dung → Vấn đề trung tâm → Khung chung.

- **Bìa (L07-01)** không có câu luận đề và không có dòng đơn vị.
  - Deck 01–04 dùng dòng đơn vị "Trường Đại học Công nghệ · Đại học Quốc gia Hà Nội".
  - Câu luận đề đề xuất: "Một vector tham số dùng chung thay cho bảng giá trị; loại mục tiêu cập nhật quyết định điểm hội tụ và giả thiết của bảo đảm."
  - Liên kết "Ghi chú bài giảng và bài tập" chuyển sang trang Bài tập về nhà.
- **Tiên quyết và quy ước**: chưa có. Thêm `L07-01b`, lấy phần cầu nối của L07-02.
  - "Nhắc lại: $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$; TD(0), Sarsa, Q-learning dạng bảng hội tụ khi mọi cặp được thăm vô hạn lần và bước học thỏa Robbins–Monro (Bài 05–06)."
  - "Ký hiệu: $t=0,1,\dots$; $R_{t+1}$ nhận sau $S_t$; $\mathbb E_\pi$ lấy theo quỹ đạo của $\pi$; $x(s)\in\mathbb R^d$, $w\in\mathbb R^d$, $\hat v(s,w)=x(s)^\top w$."
  - Phân biệt kết thúc lượt với dừng thuật toán.
- **Mục tiêu học tập (L07-03)** đang gộp với "Nội dung", 87 âm tiết và 12 dòng. Tách thành `L07-03`, gồm 5 mục tiêu; ghi chú diễn giả nêu sản phẩm kiểm tra của từng mục tiêu: Bài tập 07.1, 07.5, 07.7, 07.8, 07.13.
- **Nội dung (`L07-03b`)**: hiện chưa có, và danh sách cũ ("… Bài tập") không khớp mạch.
  - Đề xuất: "1. Mở đầu · 2. Hàm giá trị tuyến tính theo đặc trưng · 3. Monte Carlo gradient với hàm xấp xỉ · 4. Bán gradient TD(0) và điểm cố định Bellman chiếu · 5. Sarsa bán gradient cho điều khiển · 6. Học khác chính sách và bộ ba bất ổn · 7. Tổng kết và chuyển tiếp".
  - Thêm dòng "Đọc trước: Sutton và Barto (2018), §9.1–9.4, §10.1, §11.1–11.3."
- **Vấn đề trung tâm (`L07-03c`)**: chưa có.
  - "Vấn đề: học giá trị và chính sách khi không lưu được một ô cho mỗi trạng thái."
  - Năm dòng trả lời có điều kiện, mỗi mạch nội dung một dòng (tóm tắt các dòng của trang trả lời ở mạch kết luận).
  - Hình: dùng lại `tabular-vs-parametric.svg`.
- **Khung chung**: biến L07-02 thành trang "Khung chung của quy tắc cập nhật".
  - Nội dung: $w\leftarrow w+\alpha_n\,(y_t-\hat v(S_t,w))\,\nabla_w\hat v(S_t,w)$ cùng ba điểm đối chiếu: mục tiêu $y_t$ là lợi tức hay bootstrap; dữ liệu theo hay khác chính sách; cách cải thiện chính sách.
  - Gói trong 3–4 dòng.

**Mạch kết luận (mới, 7 trang sau `L07-G00`).**

1. **`L07-36`, "Kết quả và giả thiết của bài" (a)**, bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`. Bảng có 8 hàng, nên tách hai trang (36 và 36b) để giữ trần 80.
   - (a) Mức lan của một cập nhật | $\hat v$ tuyến tính | $\Delta\hat v(s')=\alpha e\,x(s')^\top x(s)$.
   - (b) Nhập nhằng đặc trưng | $x(s_1)=x(s_2)$ | $\hat v(s_1,w)=\hat v(s_2,w)$ với mọi $w$; sai số xấp xỉ không giảm khi thêm dữ liệu.
   - (c) Monte Carlo là SGD trên $J_\mu$ | $\pi,\mu$ cố định, $\mathbb E[G_t^2]<\infty$ | $\mathbb E[\nabla\ell_t]=\nabla J_\mu$.
   - (d) Hội tụ của Monte Carlo tuyến tính | mẫu iid hoặc chuỗi trộn; đặc trưng bị chặn; Robbins–Monro | $w_t\to\arg\min J_\mu$, tức $\Pi_Dv_\pi$ khi $\mu=d_\pi$.
2. **`L07-36b`, cùng tiêu đề (b).**
   - (e) Hướng trung bình của TD | $S_t\sim d_\pi$, $w$ cố định | $\mathbb E[\delta_tx(S_t)]=b-Aw$.
   - (f) Điểm cố định Bellman chiếu | $\Phi^\top D\Phi$ khả nghịch | $\Phi w=\Pi_DT_\pi\Phi w\iff Aw=b$.
   - (g) Hội tụ của TD tuyến tính | theo chính sách, $\pi$ cố định, ergodic, $\gamma<1$, $\Phi$ đủ hạng cột, Robbins–Monro | $w_t\to w_{\mathrm{TD}}$ với xác suất 1.
   - (h) Bộ ba bất ổn | bootstrap, khác chính sách và xấp xỉ hàm cùng có mặt | có thể phân kỳ.
3. **`L07-36c`, "Khung chung của bốn quy tắc"**, bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng`.
   - Monte Carlo gradient | $w\leftarrow w+\alpha_n(G_t-x(S_t)^\top w)x(S_t)$ | trọn lượt theo $\pi$, $G_t$ tính lùi | sau $K$ lượt.
   - TD(0) bán gradient | $w\leftarrow w+\alpha_n\delta\,x(S)$ | một chuyển $(S,R,S')$ theo $\pi$ | ngân sách $N$ chuyển.
   - Sarsa bán gradient | $w\leftarrow w+\alpha_n[R+\gamma\hat q(S',A',w)-\hat q(S,A,w)]x(S,A)$ | bộ năm $(S,A,R,S',A')$, $\varepsilon$-tham lam theo $\hat q$ | $K$ lượt.
   - Q-learning bán gradient | mục tiêu $R+\gamma\max_{a'}\hat q(S',a',w)$ | bộ bốn $(S,A,R,S')$, hành vi $\varepsilon$-tham lam | $K$ lượt.
   - Deck và nguồn chưa có thuật toán Q-learning. Hai notebook có quy trình này; bổ sung và ghi là sai khác.
   - LSTD và Double Q-learning chỉ có trong notebook, nên chỉ nhắc trong đoạn "Trong thực hành" của ghi chú.
4. **`L07-34` chuyển sang mạch 7**, thành bảng `Phương pháp | Giả thiết không được bỏ | Kết luận`.
   - Monte Carlo tuyến tính | $\pi,\mu$ cố định; $\mathbb E[G^2]<\infty$; đặc trưng bị chặn; iid hoặc chuỗi trộn; Robbins–Monro | cực tiểu $J_\mu$; bằng $v_\pi$ chỉ khi lớp hàm chứa $v_\pi$.
   - TD(0) tuyến tính | như dòng (g) ở trên | $w_{\mathrm{TD}}$; nói chung khác $\Pi_Dv_\pi$.
   - Sarsa tuyến tính | chính sách đổi theo $w$ | bài không có kết quả chung (Zou, Xu và Liang 2019 đặt giả thiết riêng).
   - Q-learning tuyến tính | đủ bộ ba | không có bảo đảm chung; có ví dụ phân kỳ.
   - Phi tuyến | — | cần phân tích riêng (Bài 08).
5. **`L07-35` / `L07-35b`, "Bài tập: phân tích một quy tắc cập nhật"**. Đây là bài tập tổng hợp có lời giải trên mặt trang.
   - Áp năm bước cho Q-learning tuyến tính với đặc trưng bốn khối trên Flappy Bird: $d=3p+3$, bán gradient, khác chính sách, đủ bộ ba, không suy ra hội tụ.
   - Bài nối với notebook. TD(0) chuyển thành ví dụ trong ghi chú diễn giả.
6. **`L07-36d`, "Trả lời vấn đề trung tâm"**: năm kết luận có điều kiện tương ứng mạch 2–6 (như ở `L07-03c`).
   - Dòng nguồn tổng hợp: "Nguồn: Tạ Việt Cường (2026), tr. 22–45; Sutton và Barto (2018), §9.1–9.4, 10.1, 11.1–11.3; Tsitsiklis và Van Roy (1997)."
7. **`L07-36e`, "Câu hỏi tự kiểm tra"**, mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng.", gồm 3–4 câu:
   - Thêm dữ liệu có loại được sai số do hai trạng thái cùng vector đặc trưng.
   - Vì sao Monte Carlo là gradient đầy đủ còn TD(0) là bán gradient.
   - Với $\mu=d_\pi$, Monte Carlo và TD(0) có cùng nghiệm không.
   - Bỏ giả thiết theo chính sách thì kết luận hội tụ của TD tuyến tính còn đúng không.
   - Câu hỏi đang ở L07-11, L07-25 và L07-24 chuyển về đây.
8. **`L07-36f`, "Bài tập về nhà và tài liệu đọc"**:
   - Bảng `Mạch | Bài tập` theo mục C.
   - "Tài liệu đọc: Sutton và Barto (2018), §9.1–9.5, §10.1, §11.1–11.3."
   - Dòng "Ghi chú bài giảng · Bài tập" trỏ tới viewer.
   - Dòng nối: "Bài 08 thay $x(s,a)^\top w$ bằng mạng nơ-ron (Deep Q-Network); bảo đảm tuyến tính không tự chuyển sang."

### A3. Bảng từng trang

Ngưỡng: "trần" là 60 âm tiết cho trang nội dung, 80 cho trang mục tiêu, nội dung, tổng kết và bảng so sánh. Vượt trần không có ngoại lệ là mức trung bình; vượt quá 1,5 lần trần là mức nghiêm trọng. Mọi trang vượt trần phải ghi số âm tiết trước và sau, cùng quyết định, trong storyboard.

**Vấn đề chung của nhiều trang:**
- **(G1)** Ghi chú diễn giả có lời chỉ đường "Trang sau …", "Phần sau …", "Bước tiếp theo …" ở 25 trang: 04, 09–14, 17–22, 24–35 trừ 15, 16, 23 và 36. Thay bằng quan hệ suy luận (kết quả kế thừa, giới hạn dẫn tới nhu cầu).
- **(G2)** Nguồn ghi trên mặt trang, dạng "(nguồn tr. …)" hoặc "Bài N, phiếu bài tập tuần 7", ở các trang 09, 10, 17, 26, 27, 29, 32, X01, X02, X03. Chuyển xuống ghi chú diễn giả.
- **(G3)** Trang có cặp khung `.check` và `.answer` vượt giới hạn một khung. Dòng đáp thiếu nhãn "Lời giải:". Gặp ở 04, 11, 16, 24, 25, 28, 31, 35.
- **(G4)** CSS cục bộ khoảng 100 luật theo mã trang chỉ để ép lề. Riêng L07-09 thu nhỏ chữ bằng `.math-large{font-size:.85em}`, vi phạm quy tắc không thu nhỏ chữ để đạt trần. Lớp `.answer` dùng lại nhiều trang thì đưa vào `lecture-slide.css` hoặc bỏ. Sau khi tách trang, xóa các luật thừa.
- **(G5)** Ký hiệu đổi từ `^T` sang `^\top` cho thống nhất với notebook; xem B6.

| mã | âm tiết | vấn đề theo chuẩn mới | quyết định | đề xuất cụ thể |
|---|---|---|---|---|
| L07-01 | 43 | Thiếu câu luận đề và dòng đơn vị; liên kết học liệu đặt trên bìa | sửa | Thêm câu luận đề (A2) và dòng đơn vị; chuyển liên kết sang `L07-36f` |
| L07-01b | — | Chưa có trang tiên quyết | thêm | "Tiên quyết và quy ước" với "Nhắc lại:" và "Ký hiệu:" (A2); ≤ 45 âm tiết |
| L07-02 | 85 (1,42×) | Tiêu đề dạng "Từ… đến…"; nhãn "Bài 05–06." và "Bài này." ngoài danh sách cho phép; dòng 28 âm tiết; 3 khung (2 card và 1 box) | tách | Phần nhắc lại hội tụ dạng bảng sang `L07-01b`; trang còn lại đổi thành "Khung chung của quy tắc cập nhật", đặt sau `L07-03c`, ≤ 40 âm tiết |
| L07-03 | 87 (trần 80) | 12 dòng; danh sách nội dung không khớp mạch ("Bài tập") | tách | Chỉ giữ "Mục tiêu học tập", 5 dòng, mỗi dòng ≤ 12 âm tiết |
| L07-03b | — | Chưa có trang Nội dung | thêm | "Nội dung" đánh số 1–7 trùng tên mạch, cùng dòng "Đọc trước:" |
| L07-03c | — | Chưa có trang Vấn đề trung tâm | thêm | Một dòng vấn đề và năm dòng trả lời có điều kiện, dưới 80 âm tiết |
| L07-B00 | — | Chưa có trang tiêu đề mạch | thêm | Theo A1; lớp `strand-title`, `id="mach-2"` |
| L07-04 | 92 (1,53×, nghiêm trọng) | Không mở bằng "Muốn …" hay "Nhu cầu:"; thiếu ví dụ dẫn nhập có số liệu; dòng 23 âm tiết; 2 khung; đáp thiếu "Lời giải:" | sửa | "Nhu cầu:" một dòng; ví dụ dẫn nhập "Lunar Lander rời rạc hóa thành 9 216 ô (thực hành Bài 05), 2 187 ô (Bài 06); Flappy Bird có 12 biến liên tục" (ghi nguồn notebook trong ghi chú diễn giả); khó khăn thứ ba (dữ liệu không iid) chuyển sang ghi chú diễn giả; giữ "Câu hỏi:" với "Lời giải:" hiện bằng fragment; ≤ 55 âm tiết |
| L07-05 | 54 | Ghi chú diễn giả dùng $x(s)$ trước khi định nghĩa; "one-hot" chưa có lời giải thích; ghi chú 155 âm tiết | sửa nhẹ | Nhãn "Trực quan." cho dòng ý tưởng; rút ghi chú dưới 150 âm tiết |
| L07-06 | 47 | Dòng 33 âm tiết; viết "sai lệch $e$ = mục tiêu − …", dùng dấu "=" thay "là"; trang ví dụ thiếu tiền tố "Ví dụ:" và thiếu bố cục dữ kiện / yêu cầu / bước / diễn giải; dùng $x(s)^\top w$ trước khi L07-08 định nghĩa | sửa | Tiêu đề "Ví dụ: một cập nhật lan sang trạng thái thứ hai"; dòng "Nhắc lại:" (hoặc "Đặt") cho dạng tuyến tính; "sai lệch $e$ là mục tiêu trừ dự đoán"; công thức mức lan đặt sau nhãn "Diễn giải:" |
| L07-07 | 67 | Dòng 24 âm tiết; mở bằng danh sách giả thiết, chưa có trực giác và ví dụ trước $J_\mu$ | tách | L07-07: "Muốn sửa $w$ có hướng, phải đo $\hat v$ gần $v_\pi$ đến đâu" cùng $J_\mu$, ≤ 45 âm tiết; giả thiết phần thưởng bị chặn chuyển sang ghi chú diễn giả |
| L07-07b | — | Bước ví dụ của cụm $J_\mu$ còn thiếu | thêm | "Ví dụ: hai trạng thái với trọng số μ khác nhau": cùng một vector đặc trưng, $v_\pi=(0;2)$; với $\mu=(\tfrac12;\tfrac12)$ nghiệm là $c=1$, đổi $\mu$ thì $c$ đổi. Tác tử toán tính lại |
| L07-08 | 44 | Dòng 24 âm tiết; "kernel" và "tile coding" chưa dịch; ghi chú 194 âm tiết | sửa | "hàm nhân (kernel)", "mã hóa lưới ô (tile coding)"; tách câu đầu |
| L07-09 | 71 | Dòng 28 âm tiết; nguồn trên mặt trang (G2); ba gạch nhận định; ghi chú 205 âm tiết; CSS thu nhỏ (G4) | sửa | Giữ vector điều hướng và hình `feature-domains.svg`; ba gạch nhận định chuyển sang ghi chú diễn giả; ≤ 40 âm tiết; bỏ luật `.85em` |
| L07-10 | 68 | 7 dòng; dòng 22 âm tiết; mở cụm bằng định nghĩa, ví dụ tích Kronecker chỉ có trong ghi chú diễn giả; nguồn trên mặt trang; ghi chú 292 âm tiết | tách | L07-10: định nghĩa bốn khối và kích thước $p+m+mp+1$, ≤ 40 âm tiết |
| L07-10b | — | — | thêm | "Ví dụ: hai hành động, hai đặc trưng trạng thái": $\phi(s)\otimes e_1=(\phi_1;0;\phi_2;0)$, rồi hệ quả "thiếu khối Kronecker thì hành động tham lam như nhau ở mọi trạng thái" (Mệnh đề 07.8) |
| L07-11 | 86 (1,43×) | 3 khung; dòng 30 âm tiết; đáp thiếu "Lời giải:"; mở bằng phép kéo theo hình thức | tách | L07-11: phát biểu nhập nhằng kèm "Ví dụ." đặc trưng hằng $x(s)=1$; lớp $\{\Phi w\}$ chuyển sang ghi chú diễn giả; ≤ 45 âm tiết; câu hỏi chuyển sang `L07-36e` |
| L07-11b | — | Cụm "xấp xỉ và đặc trưng" chưa có bài tập với lời giải trên mặt trang | thêm | "Bài tập: sai số xấp xỉ của hai trạng thái cùng đặc trưng", có "Lời giải:": $c=1$, $J_\mu=\tfrac12$. Trùng Bài tập 07.3 |
| L07-C00 | — | — | thêm | Theo A1, `id="mach-3"` |
| L07-12 | 49 | Dòng 21 âm tiết; $G_t$ dùng trước L07-13 | sửa nhẹ | Thêm "Nhắc lại: $G_t$ là lợi tức từ $t$ (Bài 03)"; tách dòng dài |
| L07-13 | 57 | Ghi chú diễn giả có G1 | sửa nhẹ | Gắn "(Mệnh đề 07.13)" vào câu không chệch; rút xuống ≤ 45 âm tiết |
| L07-14 | 19 | Thiếu tiền tố "Ví dụ:"; thiếu "Yêu cầu:" và "Diễn giải:" | sửa | Tiêu đề "Ví dụ: một cập nhật Monte Carlo", hoặc tên đối tượng nếu chọn Lunar Lander thu nhỏ (A5); thêm dòng "Tính …" và "Diễn giải: sai lệch giảm từ 4 xuống 2" |
| L07-15 | 44 | Dòng 28 âm tiết; 3 khối công thức (đúng trần) | sửa | Câu "SGD" tách làm hai; nhãn "Mệnh đề."; "(Mệnh đề 07.14)" |
| L07-16 | 68 | 7 dòng; 2 khung; dòng 22 âm tiết; "Đầu vào:" và "Đầu ra:" chưa in đậm | sửa | Chỉ giữ thuật toán, ≤ 55 âm tiết; câu hỏi tổng quát hóa chuyển sang ghi chú diễn giả hoặc gộp vào L07-14 |
| L07-17 | 84 (1,40×) | Hai dòng 38 và 37 âm tiết; định lý viết thành văn xuôi; nguồn trên mặt trang; ghi chú 275 âm tiết | tách | "Định lý: hội tụ của Monte Carlo tuyến tính" với "Giả thiết:" dạng danh sách, "Kết luận:" và "(Định lý 07.17)", ≤ 50 âm tiết |
| L07-17b | — | — | thêm | "Chứng minh: điểm cực tiểu trùng cực tiểu $J_\mu$", đẳng thức phương sai–độ lệch |
| X01 | 64 | 7 dòng; nguồn trên mặt trang; thiếu "Câu hỏi:" và "Lời giải:"; đặt ở M6, xa cụm Monte Carlo | sửa, chuyển | Chuyển về cuối mạch 3; X01 là đề có "Câu hỏi:" |
| X01b | — | — | thêm | Cùng tiêu đề, "Lời giải:" ba bước. Trùng Bài tập 07.5 |
| L07-D00 | — | — | thêm | Theo A1 |
| L07-18 | 48 | Công thức đi trước ví dụ; chấp nhận được vì đây là bước trực giác (mục tiêu và sai lệch) | sửa nhẹ | Ghi chú diễn giả bỏ G1 |
| L07-19 | 42 | Thiếu tiền tố "Ví dụ:"; dòng 24 âm tiết | sửa | "Ví dụ: một chuyển tiếp TD(0)"; ghi mục tiêu, sai lệch và giá trị mới trên ba dòng |
| L07-20 | 42 | Mặt trang có lời chỉ đường "phần sau tìm điểm mà nó hướng tới" | sửa | Câu kết có điều kiện: "Do mục tiêu chứa $w$, cập nhật không giảm một mất mát cố định" |
| L07-20b | 64 | Dòng đầu vào dài | sửa | Rút dòng "Đầu vào:"; ≤ 55 âm tiết |
| L07-20c | — | Cụm TD chưa có bài tập với lời giải trên mặt trang | thêm | "Bài tập: số hạng bị bỏ trong một cập nhật TD(0)": số liệu của L07-19, "Lời giải:" phần giữ $(-0{,}6;-1{,}2)$, phần bỏ $(1{,}08;0)$. Trùng Bài tập 07.7 |
| L07-21 | 58 | Dòng 29 âm tiết; nhãn "Ví dụ:" có dấu hai chấm không thuộc danh sách; $T_\pi$, $P_\pi$, $r_\pi$ thiếu "Nhắc lại:" | sửa | "Nhắc lại: $T_\pi v=r_\pi+\gamma P_\pi v$ có điểm cố định $v_\pi$ (Bài 04)"; "Ví dụ." có dấu chấm |
| L07-22 | 35 | Dòng 21 âm tiết | sửa nhẹ | Tách dòng kết luận |
| L07-23 | 62 | Hai dòng 21 và 29 âm tiết | sửa | Câu "phần dư trực giao" chuyển sang ghi chú diễn giả; ≤ 45 âm tiết |
| L07-23b | — | Cụm Bellman chiếu thiếu ví dụ số; ví dụ ở L07-21 chỉ là hình học Euclid | thêm | "Ví dụ: hai trạng thái với đặc trưng 1 và 2". Dữ kiện: $P_\pi$ đều, $d_\pi=(\tfrac12;\tfrac12)$, $r_\pi=(1;0)$, $\gamma=0{,}9$. Tính sơ bộ: $v_\pi=(5{,}5;4{,}5)$, $w_{\mathrm{MC}}=2{,}9$, $w_{\mathrm{TD}}=0{,}5/0{,}475\approx1{,}053$. Tác tử toán tính lại. Bổ sung theo Sutton–Barto §9.4 và §11.4; ghi sai khác |
| L07-24 | 89 (1,48×) | Nhãn "Dữ liệu:" và "Hệ cập nhật:" ngoài danh sách; 2 khung; ghi chú 330 âm tiết | tách | L07-24: "Định lý: hội tụ của TD tuyến tính" với "Giả thiết:", "Kết luận:" và "(Định lý 07.28)", ≤ 50 âm tiết |
| L07-24b | — | — | thêm | "Chứng minh: tính ổn định của hệ trung bình": $\|P_\pi v\|_D\le\|v\|_D$, rồi $u^\top Au\ge(1-\gamma)\|\Phi u\|_D^2$; nêu tên bất đẳng thức Jensen và Cauchy–Schwarz |
| L07-25 | 83 (trần 80) | Bảng và câu hỏi tạo 2 khung | sửa | Chỉ giữ bảng 6 hàng; câu hỏi chuyển sang `L07-36e` |
| L07-E00 | — | — | thêm | Theo A1 |
| L07-26 | 40 | Hai dòng 23 và 22 âm tiết; nguồn trên mặt trang; ghi chú 369 âm tiết; thiếu "Nhắc lại:" cho $\varepsilon$-tham lam và $q_*$ | sửa | "Nhắc lại: chính sách ε-tham lam và $q_*$ (Bài 06)"; rút ghi chú dưới 150 âm tiết |
| L07-27 | 56 | Thiếu tiền tố "Ví dụ:"; nguồn trên mặt trang | sửa | "Ví dụ: chuỗi năm trạng thái"; chữ đứng $\mathrm A$–$\mathrm E$ cho tên trạng thái (B6) |
| L07-30 | 26 | Ví dụ tính tay đứng sau công thức Sarsa (L07-28), trái thứ tự thuật toán | sửa, chuyển | Đặt trước L07-28; tiêu đề "Ví dụ: chuỗi năm trạng thái, một cập nhật Sarsa"; dòng "Nhắc lại:" cho mục tiêu Sarsa dạng bảng |
| L07-28 | 64 | Dòng 26 âm tiết; 2 khung | sửa | Câu về $A_{t+1}$ chuyển sang ghi chú diễn giả; đáp có "Lời giải:"; ≤ 55 âm tiết |
| L07-29 | 79 (1,32×) | Câu phạm vi kèm nguồn trên mặt trang | sửa | Câu phạm vi chuyển sang ghi chú diễn giả; ≤ 60 âm tiết |
| X02 | 48 | Hai dòng 21 và 23 âm tiết; nguồn trên mặt trang; thiếu "Câu hỏi:" và "Lời giải:"; đặt ở M6 | sửa, chuyển, tách | Chuyển vào mạch 5, sau L07-27, để so Monte Carlo với Sarsa trên cùng chuỗi; X02 là đề, X02b là lời giải. Trùng Bài tập 07.10 |
| X03 | 48 | Hai dòng 22 và 25 âm tiết; như X02 | sửa, chuyển, tách | Cuối mạch 5; X03 là đề, X03b là lời giải. Trùng Bài tập 07.11 |
| L07-F00 | — | — | thêm | Theo A1 |
| L07-31 | 56 | Mở bằng công thức, thiếu "Muốn …"; câu hỏi chứa nhiều dữ liệu; ví dụ hiện có cho hai mục tiêu trùng nhau, không cho thấy khác biệt | tách | L07-31: "Nhu cầu:" một dòng, mục tiêu Q-learning, nhận xét "khác chính sách" |
| L07-31b | — | Chưa có ví dụ trong đó hai mục tiêu khác nhau | thêm | "Ví dụ: chuỗi năm trạng thái, hai mục tiêu trên mẫu thứ hai" $(C,1,-1,D,1)$, $w_1=(-0{,}2;0{,}6;-1{,}4)$: Sarsa có mục tiêu $-3{,}6$, $\delta=-1{,}2$; Q-learning có mục tiêu $-2{,}4$, $\delta=0$ |
| L07-32 | 76 | Ba dòng 23, 23, 30 âm tiết; nguồn trên mặt trang; chưa có bước vấn đề và ví dụ | tách | L07-32: "Nhận xét." bộ ba bất ổn kèm hình; dòng hướng khắc phục chuyển sang ghi chú diễn giả; ≤ 40 âm tiết |
| L07-32b | — | — | thêm | "Ví dụ: hai trạng thái, trọng số tăng không chặn" (Sutton–Barto §11.2): $w_{t+1}=(1+\alpha(2\gamma-1))w_t$; với $\alpha=0{,}1$, $\gamma=0{,}9$ có $w_1=1{,}08$ |
| L07-33 | 98 (1,63×, nghiêm trọng) | 13 dòng; 3 card và 1 khung câu hỏi | tách | "Bài tập: nhận diện bộ ba bất ổn": ba câu kiểm tra và "Câu hỏi:" |
| L07-33b | — | — | thêm | Cùng tiêu đề, bảng "Lời giải:". Trùng Bài tập 07.13 |
| L07-G00 | — | — | thêm | Theo A1 |
| L07-36 | 97 (tổng kết, 1,21×) | 7 dòng; dòng 23 âm tiết; ghi chú 421 âm tiết | tách | Thành `L07-36` và `L07-36b` (bảng kết quả, A2); dòng Bài 08 chuyển sang `L07-36f` |
| L07-36c | — | — | thêm | Bảng khung chung (A2) |
| L07-34 | 78 (bảng, ≤ 80) | Hai dòng 27 và 21 âm tiết; ghi chú 329 âm tiết, có kết quả LSVI | sửa, chuyển | Thành bảng `Phương pháp \| Giả thiết không được bỏ \| Kết luận`; phần LSVI chuyển sang ghi chú bài giảng |
| L07-35 | 97 (1,62×, nghiêm trọng) | 7 dòng; 2 khung; tiêu đề "Kiểm tra…" | tách | "Bài tập: phân tích một quy tắc cập nhật": đề áp cho Q-learning trên Flappy Bird |
| L07-35b | — | — | thêm | Cùng tiêu đề, "Lời giải:" năm bước |
| L07-36d | — | — | thêm | Trả lời vấn đề trung tâm, có dòng "Nguồn:" |
| L07-36e | — | — | thêm | Câu hỏi tự kiểm tra |
| L07-36f | — | — | thêm | Bài tập về nhà và tài liệu đọc |

**Không có trên mặt trang**: "ta thấy", "rõ ràng", "chúng ta", "hãy", "Đáp án", tiêu đề dạng câu hỏi, mã nội bộ hay thời lượng. Ghi chú diễn giả không mở bằng "Trang này". Riêng L07-31 có "Trang này chỉ phân biệt…" ở giữa ghi chú; nên sửa.

### A4. Cụm khái niệm và sáu bước

Mỗi ô ghi mã trang hiện tại; chữ nghiêng là bước thiếu hoặc lệch thứ tự.

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Cần sửa |
|---|---|---|---|---|---|---|---|
| K1 Hàm tham số và tổng quát hóa | 04 | 05 | 06 | 05, 08 | 09 | 04 (câu hỏi về bảng), 16 | Kiểm tra sau L07-06 → `L07-11b` hoặc Bài tập 07.1 |
| K2 Bài toán dự đoán, $J_\mu$ | *07 mở bằng giả thiết* | *thiếu* | *thiếu* | 07 | 17 | *thiếu* | Thêm "Muốn …", trực giác về trọng số và `L07-07b` |
| K3 Đặc trưng, bốn khối, nhập nhằng | 09 | 09 | *09 không có số liệu* | 10, 11 | 27 | 11 | `L07-10b`, `L07-11b` |
| K4 Monte Carlo gradient (thuật toán) | 12 | 13 | 14, tính tay trước công thức | 15, 16 | 17, X02 | 16, X01 | Đưa X01 về mạch 3. Mục tiêu không bootstrap đã nêu đúng |
| K5 TD(0) bán gradient (thuật toán) | 18 | 18 | 19, tính tay trước 20 và 20b | 20, 20b | 25 | *thiếu trên mặt trang* | `L07-20c`. Phân biệt mục tiêu bootstrap với bán gradient đúng (L07-12, L07-20) |
| K6 Điểm cố định Bellman chiếu | 21 | 21 (hình) | *21 chỉ là hình học Euclid* | 22, 23, 24 | 25 | 24 | `L07-23b`, `L07-24b` |
| K7 So sánh Monte Carlo và TD (tổng hợp, rút gọn) | 25 | — | không áp dụng | — | 25 | *25 → 36e* | Ghi `không áp dụng` kèm lý do |
| K8 Sarsa bán gradient (thuật toán) | 26 | 26 (vòng học) | 27, *30 đứng sau 28* | *28 đứng trước ví dụ*, 29 | X03 (đặt ở M6) | 28 | Thứ tự 27 → 30 → 28 → 29 → X02, X03 |
| K9 Q-learning với xấp xỉ (biến thể) | *31 không nêu giới hạn* | *thiếu* | *ví dụ cho hai mục tiêu trùng nhau* | 31, *không có thuật toán* | 33 | 31 | "Nhu cầu:" (giới hạn của Sarsa: chính sách đích trùng chính sách hành vi), `L07-31b`, dòng thuật toán Q-learning |
| K10 Bộ ba bất ổn | *thiếu* | 32 (hình) | *chỉ có trong ghi chú diễn giả (Baird)* | 32 | 33, 34 | 33 | `L07-32b` |
| K11 Phạm vi hội tụ (tổng hợp) | — | — | — | 34 | 35 | 35 | Chuyển sang mạch 7 |

- Mọi thuật toán (Monte Carlo, TD, Sarsa) đều có bước tính tay. Riêng Sarsa có bước tính tay đứng sau công thức mục tiêu; Q-learning chưa có thuật toán.
- Mạng và bộ xấp xỉ: bài chỉ xét lớp tuyến tính, ranh giới với mạng nằm ở L07-08 và L07-36.
- Mạng trực tuyến, mạng mục tiêu và bộ nhớ phát lại chỉ nhắc ở ghi chú diễn giả và thuộc Bài 08. Phù hợp.

### A5. Ví dụ xuyên suốt

**Hiện có:**
- (i) Các vector đặc trưng trừu tượng, mỗi trang một bộ số, không gọi tên: L07-06 $(1;1),(1;0{,}5)$; L07-14 $(2;1)$; L07-19 $(1;2),(2;0)$.
- (ii) "Chuỗi năm trạng thái" (Bài 06, nguồn tr. 40; HW7, HW8): L07-27, 30, 31, X02, X03. Đã gọi bằng tên đối tượng.
- (iii) Phép chiếu $(2;0)\to(1;1)$ ở L07-21.
- (iv) Vector điều hướng (tr. 31) và hình CartPole, Lunar Lander, cờ vua ở L07-09.

**Đề xuất gọi tên:**
- "Chuỗi năm trạng thái" (giữ) cho điều khiển. Cùng chuỗi so được Monte Carlo (X02) với Sarsa (X03) và Sarsa với Q-learning (`L07-31b`, cùng chuyển $(C,1,-1,D,1)$).
- "Hai trạng thái với đặc trưng 1 và 2" cho Bellman chiếu (`L07-23b`) và phân kỳ (`L07-32b`): một bộ số, hai câu hỏi mới.
- Cho dự đoán: hoặc gọi các ví dụ (i) là "trạng thái hai đặc trưng", tốn ít công; hoặc viết lại thành "Lunar Lander thu nhỏ", ví dụ $x(s)=(\text{độ cao chuẩn hóa};1)$, đúng khuyến nghị của AGENTS về phiên bản thu nhỏ môi trường thực hành nhưng phải tính lại L07-06, L07-14, L07-19, mục 3.2, 7.2, 9.2 của ghi chú và Bài tập 07.7. Đây là câu hỏi D-Q2.

**Khả năng nối với notebook:**
- **Lunar Lander**:
  - Phần A dùng cùng chính sách và cùng dữ liệu với thực hành Bài 05. Monte Carlo theo lô đạt $J\approx1481$, LSTD (TD bình phương tối thiểu, cùng dữ liệu) đạt $1622$, bảng 9 216 ô đạt $1627$: minh họa hai đích khác nhau (K6).
  - Bước học hằng không thỏa Robbins–Monro; quan sát thiếu địa hình nên có thể không Markov (K4, K6).
  - Phần B dùng bốn khối với Fourier $p=156$, $d=785$ (K3); Sarsa đạt 200,9 và Q-learning 205,3; một hạt giống Q-learning cho 25,2 nhưng $\|w\|$ không tăng không chặn (K10).
- **Flappy Bird**:
  - Họ đặc trưng `der` ($p=5$) đạt 0,00 ống, Fourier bậc 3 đạt 34,70: sai số xấp xỉ do lớp hàm (K3).
  - Sarsa 38,04, Q-learning 28,86, luật tay 34,30 (K8, K9).
  - Họ `poly2`: $\|w\|$ lớn nhất của Q-learning là 1 895,1, của Sarsa là 15,1 (K10).
  - Double Q-learning 8 000 lượt đạt 38,24 (độ chệch của phép cực đại).
- Chuỗi năm trạng thái không có trong notebook nào.

---

## B. Ghi chú bài giảng

### B1. Đối chiếu từng mục với cấu trúc chương bắt buộc

Hiện ghi chú chia 16 mục `##`, chép gần như từng trang deck, không có môi trường đánh số nào (0 khối `definition`, `theorem` hay `algorithm`) và không có hình nào. Đề xuất gom về 5 mục nội dung ứng với mạch 2–6, thêm các phần bắt buộc.

| Mục hiện có (dòng) | Ánh xạ mạch / thành phần bắt buộc | Thiếu / sai thứ tự | Rút / chuyển |
|---|---|---|---|
| `#` (1) | (1) Tiêu đề | Viết "Bài 07." thay vì "Bài 07 — …" | — |
| Đoạn đầu (3–5) | (2) Giới thiệu | Dòng học phần thừa | Rút còn tối đa một đoạn |
| `## Bản đồ chủ đề` (7–137), gồm 16 tiểu mục `###`: Nhu cầu xấp xỉ hàm; Hàm có tham số dùng chung; Bài toán dự đoán và xấp xỉ tuyến tính; Đặc trưng và giới hạn biểu diễn; Mục tiêu cập nhật; Monte Carlo với hàm xấp xỉ; TD(0) với hàm xấp xỉ; Điểm cố định Bellman chiếu; Hai mục tiêu dự đoán; Điều khiển với xấp xỉ hàm; Q-learning và bộ ba bất ổn; Phạm vi lý thuyết; Kiểm tra tổng hợp và tổng kết; Mở đầu; Hội tụ của Monte Carlo tuyến tính; Thực hành: chuỗi năm trạng thái | (6) | Đứng trước ký hiệu, sai thứ tự. Nhãn nhóm "đọc thêm/thực hành" ngoài bốn nhóm. Đoạn dòng 9 nhiều ý | Từ 1 297 xuống khoảng 500 từ; nhóm lại theo 5 mục mới; giữ các `lec-07-topic-NN` |
| `## Ký hiệu và quy ước` (139–148) | (5) | Danh sách, không phải bảng 3 cột; thiếu câu phạm vi trước bảng và đoạn quy ước sau bảng | Viết lại thành bảng (B6) |
| `## 1. Mở đầu`: 1.1 (153), 1.2 (179) | (3) Mục tiêu, (4) Tiên quyết; phần cầu nối vào đầu mục 1 mới | Mục tiêu và tiên quyết đang nằm trong 1.2; tiên quyết không có tên nhóm in đậm và không phát biểu lại | Tách thành `## Mục tiêu học tập` và `## Kiến thức tiên quyết`. Bài tập GLIE (167) sang Bài tập củng cố hoặc bỏ |
| `## 2.` 2.1 (196) | Mục 1 mới (mạch 2), phần vấn đề | Không có số liệu môi trường | Mở bằng Ví dụ 07.1 (Lunar Lander 9 216 ô) |
| `## 3.` 3.1 (221), 3.2 (233) | Mục 1 | Dòng 229 tham chiếu trang chiếu; 3.2 có ví dụ trước quy tắc | Định nghĩa 07.1, Mệnh đề 07.2 |
| `## 4.` 4.1 (262), 4.2 (274) | Mục 1 | 4.1 mở bằng "Thiết lập:"; $J_\mu$ chưa có ví dụ | Ví dụ 07.3 trước Định nghĩa 07.4 |
| `## 5.` 5.1 (305), 5.2 (333), 5.3 (349) | Mục 1 | 5.2 định nghĩa đi trước ví dụ | Đoạn "Trong thực hành" về các họ đặc trưng của hai notebook |
| `## 6.` 6.1 (377) | Mục 2 mới (mạch 3) | — | Định nghĩa 07.12 |
| `## 7.` 7.1–7.4 (415–459) | Mục 2 | Thuật toán viết thành văn xuôi | Thuật toán 07.15 |
| `## 8.` 8.1 (487), 8.2 (505) | Mục 2 | 8.1 mở bằng định lý; định lý không có khối và thiếu bốn phần | Bổ đề 07.16, Định lý 07.17; HW4, HW6 thành Bài tập 07.5, 07.6 |
| `## 9.` 9.1–9.4 (557–597) | Mục 3 mới (mạch 4) | Thiếu nhận xét về cắt ngắn so với kết thúc | Thêm Nhận xét 07.23 |
| `## 10.` 10.1–10.4 (624–682) | Mục 3 | "Trên hình của mục 10.1" lặp ở dòng 662 và 664 nhưng ghi chú không có hình; chứng minh viết thành dòng, không chia bước | Chèn `projected-bellman.svg` kèm đoạn đọc hình; Ví dụ 07.10; Định lý 07.28 với danh sách "Bỏ …" |
| `## 11.` 11.1 (702) | Mục 3 (nhận xét so sánh) | — | Nhận xét 07.30 |
| `## 12.` 12.1–12.5 (734–784) | Mục 4 mới (mạch 5) | 12.3 công thức Sarsa đi trước 12.4 ví dụ | Đổi thứ tự; chèn `control-loop.svg` và `five-state-features.svg` |
| `## 13.` 13.1–13.3 (812–846) | Mục 5 mới (mạch 6) | Không có ví dụ phân kỳ; dòng 826 viết công thức bằng chữ | Ví dụ 07.13, 07.14; chèn `deadly-triad.svg` |
| `## 14.` 14.1 (872), 14.2 (889) | 14.1 sang (9) Tóm tắt; 14.2 sang (11) đọc thêm | — | Rút 14.2 |
| `## 15.` 15.1 (910), 15.2 (936) | 15.1 sang (10) Bài tập củng cố; 15.2 sang (9) Tóm tắt | 15.2 không theo khuôn tóm tắt | Viết lại thành đoạn 5–8 câu, tiếp theo là các danh mục |
| `## 16.` 16.1, 16.2, 16.3 (976–1064) | 16.1 và 16.2 về cuối mục 4 (Bài tập 07.10, 07.11); 16.3 sang Tóm tắt (bảng khung chung) | — | Câu hỏi ở dòng 1052 gộp vào Bài tập 07.11; dòng 1075 gộp vào Ví dụ 07.13 |
| `## Tài liệu tham khảo` (1087) | (11) | Thiếu Sutton–Barto dù được dẫn ở dòng 33, 272, 828; bốn mục Bhandari, Silver, Zhang, Peng không được dẫn trong văn bản; không ghi mục nào dựa trên nguồn nào | Viết lại (B5) |
| *(chưa có)* | (8) Tình huống áp dụng và ứng dụng; (10) Bài tập củng cố ba mức | Thiếu | Thêm (B4) |

**Độ dài:**
- Hiện 15 777 từ, kể cả ký hiệu công thức.
- Phần thêm ước tính: tiên quyết và bảng ký hiệu 900, "Trong thực hành" 1 000, đoạn móc nối 1 000, tình huống áp dụng 1 600, tóm tắt 700, bài tập củng cố 1 500, chứng minh và danh sách "Bỏ…" 1 000, ví dụ mới 900, đoạn đọc hình 500.
- Phần rút ước tính khoảng 3 500: bản đồ chủ đề −800, mục 15 −800, mục 14.2 −150, các câu "Nguồn …" lặp −300, phần trùng deck −600, các câu hỏi gộp hoặc bỏ −850.
- Đích: 18 000–19 500 từ, dưới trần 20 000.

### B2. Kế hoạch đánh số môi trường

Đánh số theo AGENTS: một bộ đếm chung `07.k` cho Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét và Thuật toán; Ví dụ và Bài tập mỗi loại một bộ đếm riêng. Mẫu math-4-AI dùng bộ đếm riêng cho Thuật toán, trái AGENTS; nên theo AGENTS. Tình huống áp dụng đề xuất có bộ đếm riêng (AGENTS chưa quy định).

**Bộ đếm chung (khối `:::` tương ứng):**
- **Mục 1:**
  - 07.1 `definition` Hàm giá trị có tham số.
  - 07.2 `proposition` Mức lan của một cập nhật tuyến tính.
  - 07.3 `corollary` Đặc trưng one-hot cho lại bảng tra.
  - 07.4 `definition` Bài toán dự đoán và sai số giá trị $J_\mu$.
  - 07.5 `definition` Xấp xỉ tuyến tính, lớp $\{\Phi w\}$.
  - 07.6 `remark` Các lớp hàm khác.
  - 07.7 `definition` Đặc trưng bốn khối.
  - 07.8 `proposition` Vai trò khối Kronecker.
  - 07.9 `remark` Bốn khối không đủ hạng cột.
  - 07.10 `proposition` Nhập nhằng đặc trưng.
  - 07.11 `definition` Sai số xấp xỉ và sai số ước lượng.
- **Mục 2:**
  - 07.12 `definition` Mục tiêu mẫu, mất mát mẫu, gradient đầy đủ và bán gradient.
  - 07.13 `proposition` Lợi tức là mục tiêu không chệch (phát biểu lại từ Bài 03).
  - 07.14 `proposition` Cập nhật Monte Carlo là SGD trên $J_\mu$.
  - 07.15 `algorithm` Monte Carlo gradient tuyến tính.
  - 07.16 `lemma` Phân tích phương sai–độ lệch.
  - 07.17 `theorem` Hội tụ của Monte Carlo tuyến tính, kèm `proof` hoặc "ngoài phạm vi" có nguồn và số trang.
  - 07.18 `remark` Vai trò hai điều kiện Robbins–Monro.
- **Mục 3:**
  - 07.19 `definition` Mục tiêu TD(0) và sai số TD.
  - 07.20 `proposition` Độ chệch của mục tiêu TD.
  - 07.21 `definition` Cập nhật bán gradient.
  - 07.22 `algorithm` TD(0) bán gradient tuyến tính.
  - 07.23 `remark` Kết thúc, cắt ngắn và dừng thuật toán.
  - 07.24 `definition` Phép chiếu $\Pi_D$ và toán tử Bellman chiếu.
  - 07.25 `proposition` $\mathbb E[\delta_tx(S_t)]=b-Aw$.
  - 07.26 `proposition` Điểm dừng trung bình là điểm cố định Bellman chiếu (HW5).
  - 07.27 `lemma` $\|P_\pi v\|_D\le\|v\|_D$.
  - 07.28 `theorem` Tsitsiklis–Van Roy.
  - 07.29 `corollary` $w_{\mathrm{TD}}$ duy nhất.
  - 07.30 `remark` So sánh Monte Carlo và TD(0), cùng chặn $1/(1-\gamma)$ của Sutton–Barto §9.4 dưới dạng đọc thêm; notebook Lunar Lander đang dẫn chặn này.
- **Mục 4:**
  - 07.31 `definition` $\hat q$ và chính sách ε-tham lam theo $\hat q$.
  - 07.32 `proposition` Hiệu hai hành động trên chuỗi: $-2[w]_2$.
  - 07.33 `algorithm` Sarsa bán gradient.
  - 07.34 `remark` Phạm vi bảo đảm của Sarsa.
- **Mục 5:**
  - 07.35 `definition` Mục tiêu Q-learning với hàm xấp xỉ.
  - 07.36 `algorithm` Q-learning bán gradient (bổ sung).
  - 07.37 `proposition` Phân kỳ trong ví dụ hai trạng thái.
  - 07.38 `remark` Bộ ba bất ổn.
  - 07.39 `remark` Phạm vi các kết quả hội tụ.
  - 07.40 `remark` MDP tuyến tính (đọc thêm).

**Ví dụ (`example`):**
- 07.1 Lunar Lander rời rạc hóa (dẫn nhập).
- 07.2 Một cập nhật lan sang trạng thái thứ hai.
- 07.3 Hai trạng thái, đổi $\mu$.
- 07.4 Đặc trưng điều hướng và Lunar Lander.
- 07.5 Tích Kronecker với $p=m=2$.
- 07.6 Hai trạng thái cùng đặc trưng.
- 07.7 Một cập nhật Monte Carlo.
- 07.8 Một cập nhật TD(0).
- 07.9 Hình chiếu lên đường thẳng.
- 07.10 Hai trạng thái với đặc trưng 1 và 2: $w_{\mathrm{TD}}$ và $w_{\mathrm{MC}}$.
- 07.11 Chuỗi năm trạng thái.
- 07.12 Một cập nhật Sarsa.
- 07.13 Hai mục tiêu trên mẫu $(C,1,-1,D,1)$.
- 07.14 Hai trạng thái, phân kỳ.

**Bài tập (`exercise`, mỗi bài có `hint` và `solution`); số cũ → số mới:**

| Số mới | Nguồn trong ghi chú hiện tại | Vị trí mới |
|---|---|---|
| 07.1 | dòng 247 (mức lan ba trạng thái) | mục 1 |
| 07.2 | dòng 290 (lớp $\{\Phi w\}$) | mục 1 |
| 07.3 | dòng 361 (sai số xấp xỉ hai trạng thái) | mục 1 |
| 07.4 | dòng 400 ($y^{\mathrm{TD}}$ chứa $w$) | mục 2 |
| 07.5 | HW4 | mục 2 |
| 07.6 | HW6 | mục 2 |
| 07.7 | dòng 609 (số hạng bị bỏ) | mục 3 |
| 07.8 | dòng 670 gộp HW5 | mục 3 |
| 07.9 | dòng 719 (HW2) | mục 3 |
| 07.10 | HW7 | mục 4 |
| 07.11 | HW8, gộp câu hỏi dòng 1052 | mục 4 |
| 07.12 | dòng 797 | mục 4 |
| 07.13 | dòng 834 (HW3) | mục 5 |
| 07.14–07.19 | dòng 206, 321 (nhận biết); 472 và một bài mới (tính toán); 922, 955 (vận dụng) | Bài tập củng cố |

Câu hỏi dòng 167 (GLIE) và 895 (LSVI) bỏ hoặc chuyển sang đọc thêm. Câu hỏi dòng 1075 gộp vào Ví dụ 07.13.

**Tình huống áp dụng 07.1 và 07.2:** xem B4.

### B3. Bảng kiểm "Tiêu chuẩn thứ nhất" và "Trình bày sáng sủa"

**Giọng kể.** Ghi chú hiện viết theo giọng khách quan, không có lần nào "chúng ta". Chỉ có một chữ "ta", ở dòng 736 ("ta học giá trị hành động").
- Tài liệu làm chủ ngữ:
  - "Bài này": dòng 5, 157, 286.
  - "Mục tiếp theo …": dòng 204. "phần tiếp theo …": dòng 359.
  - "Phần này": dòng 636. "Mục này": dòng 820. "Phần tiếp theo": dòng 717, 867.
  - "Nguồn (tr.) nêu / ghi nhận / gọi …" làm chủ ngữ 14 lần, chẳng hạn dòng 272, 717, 832, 887, 891, 893, 947, 949, 951.
- Sửa toàn bài:
  - Câu nêu kế hoạch hoặc lựa chọn dùng "chúng ta", ví dụ "chúng ta dùng lớp tuyến tính vì …".
  - Dòng tính toán dùng "ta", ví dụ "Thế vào …, ta được …".
  - Nguồn chuyển vào ngoặc tại chỗ.
  - Trong khối định nghĩa và định lý giữ câu khách quan.

| Tiêu chí | Vi phạm (dòng) | Cách sửa |
|---|---|---|
| Vấn đề đi trước công cụ | 264 mở mục bằng "Thiết lập: …"; 489 mở 8.1 bằng phát biểu định lý; 198 không có môi trường hay số liệu | Mở mỗi `##` bằng bài toán có số liệu (Lunar Lander 9 216 ô; Flappy Bird 12 biến) và câu "Để …, chúng ta cần …" |
| Công thức có câu dẫn và câu đọc | 575 và 577: hai khối `$$` liền nhau; 778 và 780: như vậy; 445: hai công thức trong một khối | Chèn câu nối; đọc công thức bằng lời sau mỗi khối |
| Ký hiệu gọi tên tại chỗ | 650 dùng $\phi_j$ cho cột của $\Phi$, trùng $\phi(s)$ ở 5.2; 145 viết $d(s)$, chỗ khác viết $d_\pi$; 322 và 326 viết $d_{\text{left}}$, chỗ khác $d_{\text{trái}}$ | Theo bảng B6 |
| Mỗi bước suy diễn có lý do | 455 và 646: chuỗi dấu bằng không ghi căn cứ; 693: dùng bất đẳng thức Cauchy–Schwarz theo $\langle\cdot,\cdot\rangle_D$ mà không gọi tên | Viết `aligned` có cột `&&\text{(…)}` |
| Bản đọc bằng lời và "Bỏ giả thiết" | 684–697 (định lý TD) và 489–501 (Monte Carlo) không có danh sách "Bỏ …" | Ví dụ cho TD: bỏ "theo chính sách" → Ví dụ 07.14 phân kỳ; bỏ "đủ hạng cột" → nghiệm không duy nhất (bốn khối); bỏ Robbins–Monro → bước hằng dao động (notebook); bỏ $\gamma<1$ → chuẩn co không còn |
| Ví dụ trước phát biểu tổng quát | $J_\mu$ (268) chưa có ví dụ; 10.3 không có ví dụ số; 13.2 không có ví dụ | Ví dụ 07.3, 07.10, 07.14 |
| Nối mục bằng kết quả | 204, 359, 503, 717, 867 dùng lời chỉ đường | Đoạn kết mục ba ý bằng văn xuôi, dẫn số hiệu |
| Không tham chiếu ra ngoài | 229 "Trong hình minh họa của trang chiếu"; 662 và 664 "Trên hình của mục 10.1" (không có hình); 191 "Kiến thức tiên quyết từ Bài 03–06" không phát biểu lại | Chèn hình SVG; mục Tiên quyết phát biểu lại từng kết quả |
| Câu đủ thành phần, một luận điểm mỗi đoạn | 9: đoạn rất dài, nhiều ý; 264: câu mảnh | Viết lại |
| Hình được đọc trong văn bản | Ghi chú có 0 hình, trong khi deck có 10 SVG | Chèn ít nhất sáu hình (pipeline tuyến tính, cập nhật Monte Carlo, Bellman chiếu, vòng điều khiển, chuỗi, bộ ba) kèm đoạn đọc hình; thêm một SVG cấu trúc chương cho đầu mục 1 |
| Một ý một đoạn (tối đa khoảng 4 câu) | 155, 270, 501, 744, 748, 938 | Tách đoạn |
| Chứng minh chia bước | 664 viết chứng minh thành dòng; 691–695 là đoạn liền; lời giải 535 | `**Bước 1 (…).**` cho từng bước |
| Trường hợp thành danh sách | 501 (giả thiết viết thành văn xuôi); 1013 ("vì hai lý do") | Danh sách |
| Công thức quan trọng có số `\tag` | Không có công thức nào được đánh số | `\tag{3.1}` cho $\Phi w=\Pi_DT_\pi\Phi w$, $b-Aw$, $J_\mu$ |
| Tách phần của định lý | Không có khối định lý nào | Giả thiết / Kết luận / Điều kiện áp dụng / Phạm vi |
| Nhãn giai đoạn của ví dụ | 429–439, 573–583, 776–782 không có "Lập mô hình / Tính / Kiểm tra lại" | Thêm nhãn; mục tiêu, sai lệch và giá trị mới trên ba dòng |
| Ngoặc lồng | 9, 393, 686 | Chuyển phần trong ngoặc thành câu riêng |

Nhãn trong văn xuôi ngoài chuẩn: "Ví dụ." (237), "Ý nghĩa." (666), "Chứng minh (Bài tập 5)." (664), "Giới hạn:" (288), "Thiết lập:" (264). Các chỗ này chuyển thành khối `:::`. Số hiệu bài tập theo phiếu ("Bài tập 4/6/7/8") đổi sang `07.k`.

### B4. Phần cần thêm

**Đoạn móc nối:**
- Sau Định nghĩa 07.5 (tuyến tính) nối với 07.1 và bảng tra, qua Hệ quả 07.3.
- Sau 07.12: phân biệt mục tiêu bootstrap với bán gradient.
- Trước Định lý 07.28: kết quả này cần 07.25–07.27; sau định lý: so với 07.17, đổi $\mu$ thành $d_\pi$, nghiệm khác.
- Thuật toán 07.33 so với 07.22, và 07.36 so với 07.33: nêu thành phần thay đổi (mục tiêu, chính sách hành vi).
- Mở chương: Q-learning dạng bảng hội tụ (Bài 06). Kết chương: Bài 08 (Deep Q-Network: mạng mục tiêu, bộ nhớ phát lại); Bài 09 (Double DQN) nối với mục 13 của notebook Flappy Bird.

**Đoạn "Trong thực hành":**
- Sau Mệnh đề 07.2: phần tính tay ở mục 6 của notebook Lunar Lander, nơi dự đoán tại $S_1$ đã khác 0 trước khi $S_1$ được cập nhật.
- Sau Định nghĩa 07.4: thước đo $J$ trên tập kiểm tra, phân rã và cảnh báo về tính Markov (notebook Lunar Lander, mục 5).
- Sau 07.7 và 07.10: các họ đặc trưng của hai notebook; số ống 0,00, 0,40, 34,70.
- Sau Định lý 07.17: bước học hằng; một lượt qua dữ liệu cho $J\approx2190$, nghiệm theo lô cho 1 481.
- Sau 07.26 và 07.28: LSTD 1 622 so với Monte Carlo theo lô 1 481; phân phối ghé theo lượt; cắt ngắn vẫn bootstrap.
- Sau 07.33: Sarsa trên Lunar Lander 200,9; trên Flappy Bird 38,04 so với luật tay 34,30.
- Sau 07.38: Lunar Lander với $\|w\|$ = 52,9 (không phải phân kỳ); Flappy Bird họ `poly2` 1 895 so với 15,1; Double Q-learning.

**Tình huống áp dụng 07.1 (gắn notebook Lunar Lander):** dự đoán $v_\pi$ của chính sách heuristic-ε bằng Monte Carlo và TD tuyến tính trên Fourier bậc 3.
- Kiểm giả thiết: $\pi$ cố định (thỏa); theo chính sách (thỏa); $\Phi$ đủ hạng (thỏa); Robbins–Monro (không thỏa); Markov (chưa chắc).
- Áp dụng Mệnh đề 07.26 qua LSTD; đọc chênh lệch $J$; nêu giới hạn.
- Dẫn ngược 07.4, 07.17, 07.26, 07.28.

**Tình huống áp dụng 07.2 (giả thiết không thỏa):** Q-learning tuyến tính và bộ ba bất ổn.
- Mô hình hóa ví dụ hai trạng thái (Ví dụ 07.14, Mệnh đề 07.37), chỉ ra giả thiết theo chính sách của Định lý 07.28 bị vi phạm.
- Đối chiếu với $\|w\|$ trên Flappy Bird, họ `poly2`.
- Kết luận "có thể phân kỳ", không phải "luôn phân kỳ".

**Danh mục "Ứng dụng":** Bài 08 (Deep Q-Network); Bài 09 (Double DQN; độ chệch của phép cực đại); các bài gradient chính sách 09–11 (thành phần đánh giá dùng TD với xấp xỉ hàm); hai notebook.

**Tóm tắt chương:**
- Đoạn 5–8 câu kể lại chương.
- "Định nghĩa và kết quả theo mục".
- "Công thức cần nhớ": bốn quy tắc cập nhật, $b-Aw$, $\Phi w=\Pi_DT_\pi\Phi w$.
- "Giả thiết hay bị bỏ quên": $\mu$ so với $d_\pi$; theo chính sách; $\Phi$ đủ hạng; Robbins–Monro; cắt ngắn so với kết thúc.

**Bài tập củng cố:** 07.14–07.19, hai bài mỗi mức, không trùng `exercises.md`.

### B5. Giáo trình đối chiếu cho từng mục

Số mục của Bertsekas–Tsitsiklis và Szepesvári ghi dưới đây theo trí nhớ; tác tử soạn phải kiểm số mục chính xác và ghi vào review-log.

| Mục mới | Giáo trình và mục |
|---|---|
| Tiên quyết, giọng kể | *Học máy thống kê*, chương 6: `sec_q_learning.tex`, `sec_approximate_learning.tex`. Thuật toán SARSA1 của giáo trình dùng mục tiêu có phép cực đại, tức là Q-learning; không chép. Bảng ký hiệu nêu tương ứng $Q_w$, $\phi(s,a)$ với $\hat q$, $x(s,a)$ |
| 1. Hàm tuyến tính, đặc trưng | Sutton–Barto (2018) §9.1, §9.2 (VE, $\mu$, phân phối theo chính sách), §9.4, §9.5.1–9.5.4, §9.7 (ranh giới với mạng nơ-ron); Bertsekas–Tsitsiklis (1996), chương về kiến trúc xấp xỉ và đặc trưng (khoảng ch. 3, 6) |
| 2. Monte Carlo gradient | Sutton–Barto §9.3 (khung Gradient Monte Carlo), §2.7 (Robbins–Monro); Goodfellow, Bengio và Courville (2016) §4.3, §8.3.1 (SGD, điều kiện bước học); Szepesvári (2010) §3.2 |
| 3. TD bán gradient, Bellman chiếu | Sutton–Barto §9.3 (TD(0) bán gradient), §9.4 (điểm cố định TD, $A$, $b$, chặn $1/(1-\gamma)$), §9.8 (LSTD, cho đoạn "Trong thực hành"), §11.4 (hình học Bellman chiếu); Tsitsiklis và Van Roy (1997); Bertsekas–Tsitsiklis (1996), phần TD(λ) tuyến tính (khoảng §6.3); Szepesvári (2010) §3.2.1 |
| 4. Sarsa | Sutton–Barto §10.1 (Sarsa bán gradient theo lượt, Mountain Car), §9.5.4; Zou, Xu và Liang (2019) |
| 5. Q-learning, bộ ba bất ổn | Sutton–Barto §11.1, §11.2 (ví dụ w→2w, Baird), §11.3, §6.7 (Double Q-learning, cho phần thực hành); Szepesvári (2010) ch. 4; Jin và cộng sự (2020); Zhang, Yao và Whiteson (2021) |

### B6. Bảng ký hiệu đề xuất và các chỗ lệch

**Bảng ký hiệu (21 dòng):**

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S,\mathcal A$ | tập trạng thái, tập hành động | hữu hạn hoặc liên tục; $\mathcal A$ hữu hạn |
| $t$, $T$ | thời điểm, thời điểm kết thúc lượt | $\{0,1,\dots\}$ |
| $S_t,A_t,R_{t+1}$ | trạng thái, hành động, phần thưởng | $R_{t+1}$ nhận sau $S_t$ |
| $\pi$, $\pi_w$ | chính sách; chính sách tham lam hoặc ε-tham lam theo $\hat q$ | phân phối trên $\mathcal A$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $<1$ trong định lý TD |
| $G_t$ | lợi tức | biến ngẫu nhiên thực |
| $v_\pi,q_\pi,q_*$ | giá trị thật | $\mathbb R$ |
| $x(s)$, $x(s,a)$ | vector đặc trưng | $\mathbb R^d$ |
| $\phi(s)$ | đặc trưng trạng thái trong mã hóa bốn khối | $\mathbb R^p$ |
| $w$, $w_t$, $[w]_i$ | tham số, tham số sau $t$ cập nhật, thành phần thứ $i$ | $\mathbb R^d$ |
| $\hat v(s,w)$, $\hat q(s,a,w)$ | giá trị ước lượng | $\mathbb R$ |
| $\alpha_n$ | bước học ở lần cập nhật thứ $n$ | $(0,\infty)$ |
| $y_t$, $e_t$, $\delta_t$ | mục tiêu; sai lệch Monte Carlo; sai số TD | $\mathbb R$ |
| $\ell_t$, $J_\mu$ | mất mát mẫu; sai số giá trị, $J_\mu=\tfrac12\overline{\mathrm{VE}}$ | $\mathbb R_{\ge0}$ |
| $\mu$ | phân phối trọng số của $J_\mu$ | phân phối trên $\mathcal S$ |
| $d_\pi$, $D$ | phân phối dừng, hoặc phân phối ghé theo lượt; $D=\mathrm{diag}(d_\pi)$ | — |
| $\Phi$ | ma trận đặc trưng | $\mathbb R^{\lvert\mathcal S\rvert\times d}$ |
| $P_\pi,r_\pi,T_\pi$ | ma trận chuyển, phần thưởng kỳ vọng, toán tử Bellman | — |
| $\Pi_D$ | phép chiếu theo $\lVert\cdot\rVert_D$ | — |
| $A,b,w_{\mathrm{TD}}$ | $\Phi^\top D(I-\gamma P_\pi)\Phi$, $\Phi^\top Dr_\pi$, nghiệm của $Aw=b$ | — |
| $\varepsilon$ | xác suất thăm dò | $[0,1]$ |

**Các chỗ lệch cần sửa:**

1. **$A$, $D$ (ma trận) trùng tên trạng thái $A$, $D$ của chuỗi và hành động $A_t$.** Viết tên trạng thái bằng chữ đứng $\mathrm A$–$\mathrm E$, theo tiền lệ math-4-AI ("Tên nút … chữ đứng … phân biệt với ma trận $A$"). Sửa ở deck, ghi chú và các SVG có chữ.
2. **$b$ vừa là hệ số chặn (khối bốn) vừa là $\Phi^\top Dr_\pi$.** Đổi hệ số chặn thành $\beta$; mã notebook giữ biến `Q.b`, chỉ sửa Markdown.
3. **$c$ có bốn nghĩa:** hằng $c_a$ của hành động, vector chỉ số Fourier trong hai notebook, hằng bước học (notebook Lunar Lander mục 11, "$\alpha=c/\mathbb E\lVert x\rVert^2$"; Flappy Bird đã đổi sang $\kappa$), và hệ số $c$ trong câu hỏi dòng 362 và dòng 636 của ghi chú. Đổi hằng bước học của Lunar Lander sang $\kappa$; các nghĩa còn lại chỉ dùng tại chỗ.
4. **$u$ có ba nghĩa:** $u(a)$ dấu của hành động, khối $u_a$, vector $u$ trong chứng minh. Đổi dấu hành động thành $\sigma(a)$, cần sửa HW7, HW8, X02, X03 và hình `five-state-features.svg`; hoặc giữ $u(a)$ và đổi vector trong chứng minh thành $z$.
5. **$\phi$:** $\phi_j$ dùng cho cột của $\Phi$ (ghi chú dòng 650); phiếu bài tập dùng $\phi(s)$ cho cái mà bài gọi là $x(s)$; giáo trình *Học máy thống kê* dùng $\phi(s,a)$. Ghi tương ứng một lần trong bảng ký hiệu.
6. **$\Phi(s)$ là hàm thế (shaping)** trong notebook Lunar Lander, ô 4, trùng ma trận đặc trưng. Đổi tên trong Markdown.
7. **$\overline{\mathrm{VE}}$ có hệ số ½** trong notebook Lunar Lander (ô 24), trong khi Sutton–Barto định nghĩa không có ½; thước đo $J(\hat v)$ trên tập kiểm tra cũng trùng tên $J_\mu$. Viết $J_\mu=\tfrac12\overline{\mathrm{VE}}$ và gọi thước đo là $J_{\mathrm{kt}}$.
8. **`^T` và `^\top` lẫn nhau:** deck dùng `^T`; ghi chú dùng `^T` ở dòng 229–256 và `^\top` ở phần còn lại; notebook dùng `^\top`. Thống nhất `^\top`.
9. **Bước học** viết $\alpha_t$ (ghi chú 6.1, 7.3; deck L07-15), $\alpha_n$ (các thuật toán) và $\alpha$ (ví dụ). Quy ước: $\alpha_n$ chung, $\alpha$ hằng trong ví dụ.
10. **Cắt ngắn (`score_limit=50`, 1 000 bước) vẫn bootstrap trong notebook**; deck và ghi chú chỉ nói về kết thúc. Thêm Nhận xét 07.23.
11. **Thuật toán Q-learning có trong cả hai notebook** (Flappy Bird ô 22: chọn hành động mới bằng $w$ đã cập nhật) nhưng không có trong deck và ghi chú. Thêm Thuật toán 07.36.
12. **Notebook dẫn số mục của ghi chú cũ:** 3.2, 4.1, 4.2, 5.1, 5.2, 7.1–7.3, 8.1, 9.1–9.3, 10.1–10.4, 12.1, 12.3, 12.5, 13.1, 13.2, 14, 14.1. Đánh số lại ghi chú sẽ làm hỏng các tham chiếu này; nên đổi sang dẫn số hiệu `07.k`.
13. **Ký hiệu ε**: ghi chú dòng 863 và 865 viết "ε" ngoài công thức, chỗ khác viết $\varepsilon$.

---

## C. Bài tập (`exercises.md` mới)

Bài trùng ghi chú giữ số hiệu và lời giải của ghi chú. Ba bài 07.20–07.22 chỉ có trong `exercises.md`, theo cách tổ chức của mẫu math-4-AI. Bảng `Mạch | Mở phần | Bài tập` trỏ tới `lecture-07-xap-xi-ham.html#/N/1`.

| số hiệu | mạch | mức | đối tượng / dữ kiện tóm tắt | trùng trang chiếu hay mới | năng lực đo |
|---|---|---|---|---|---|
| 07.1 | 2 | nhận biết | Ba vector đặc trưng; mức lan $\Delta\hat v$ và dấu của tích vô hướng | mới (ghi chú) | đọc tổng quát hóa qua tham số |
| 07.3 | 2 | tính toán | Hai trạng thái cùng đặc trưng, $v=(0;2)$, $\mu=\tfrac12$: $c=1$, $J=\tfrac12$ | trùng `L07-11b` | phân biệt sai số xấp xỉ với sai số ước lượng |
| 07.5 | 3 | tính toán / chứng minh | HW4: gradient Monte Carlo, bước SGD, điều kiện hội tụ | trùng X01, X01b | gradient đầy đủ |
| 07.6 | 3 | nhận biết | HW6 kèm phân loại $\alpha_n\in\{1/n,\ 1/\sqrt n,\ \text{hằng},\ 1/n^2\}$ | mới | điều kiện Robbins–Monro |
| 07.7 | 4 | tính toán | Số liệu của L07-19: phần giữ và phần bỏ của gradient | trùng `L07-20c` | bán gradient |
| 07.8 | 4 | chứng minh | HW5: $b-Aw$ dẫn tới Bellman chiếu; tính $w_{\mathrm{TD}}$, $w_{\mathrm{MC}}$ cho hai trạng thái | mới (gần L07-22, 23, `23b`) | điểm cố định và so sánh nghiệm |
| 07.10 | 5 | tính toán | HW7: Monte Carlo trên một lượt của chuỗi | trùng X02, X02b | cập nhật tuần tự, vượt mục tiêu |
| 07.11 | 5 | tính toán | HW8: ba cập nhật Sarsa | trùng X03, X03b (bước đầu ở L07-30) | Sarsa bán gradient |
| 07.13 | 6 | vận dụng | HW3: phân loại bốn quy tắc (TD theo chính sách, Sarsa, Q-learning, Monte Carlo khác chính sách) theo ba yếu tố | trùng L07-33, `33b` | nhận diện bộ ba bất ổn |
| 07.20 | 6 | vận dụng | Hai trạng thái $w$, $2w$: miền $(\alpha,\gamma)$ gây phân kỳ; cập nhật theo $d_\pi$ thì ổn định | mới, chỉ ở tệp (Sutton–Barto §11.2) | vai trò giả thiết theo chính sách |
| 07.21 | 3–4 | vận dụng [Lập trình] | Notebook Lunar Lander mục 6–8: thay bước hằng bằng $\alpha_n=\kappa/n$; so $J$ với Monte Carlo theo lô và LSTD; giải thích vì sao LSTD có $J$ lớn hơn | mới, chỉ ở tệp | kiểm Robbins–Monro; hai đích |
| 07.22 | 5–6 | vận dụng [Lập trình] | Notebook Flappy Bird mục 6 và 10: họ `der` so với `four3`; theo dõi $\|w\|$ của Q-learning và Sarsa với `poly2`; kết luận theo bảng phạm vi | mới, chỉ ở tệp | phân biệt chính sách kém với phân kỳ |

Mạch 2–6 đều có ít nhất một bài. Có bốn bài vận dụng: 07.13, 07.20, 07.21, 07.22.

---

## D. Rủi ro, thứ tự thực hiện và câu hỏi cho người dùng

**Thứ tự thực hiện** (ghi chú trước, deck sau, bài tập cuối; theo `prompt_lecture_note_deck.md`):
1. Lập kế hoạch: chốt số mạch, ví dụ xuyên suốt, bảng ký hiệu, số hiệu `07.k`.
2. Ghi chú:
   - Một tác tử soạn viết lại ghi chú: `no-ai-slop` chế độ Edit, đối chiếu `eval.md`, dùng `quill` để rà dàn ý.
   - Năm vai rà soát chạy song song, chỉ đọc; tác tử toán tính lại mọi số, kể cả các số mới ở L07-23b, L07-31b, L07-32b.
   - Một tác tử biên tập sửa theo báo cáo, rồi rà lại.
   - Kiểm trên viewer.
   - Commit theo dạng `fix(materials-07)`.
3. Sửa tham chiếu số mục trong Markdown của hai notebook. Chỉ sửa ô Markdown, giữ nguyên output, chạy `nbformat.validate`.
4. Deck:
   - Một tác tử sửa deck, SVG, outline, storyboard (ghi số âm tiết trước và sau mỗi trang vượt trần).
   - Năm vai rà soát; kiểm trên Playwright ở 1600×900 và 390×844 cho mọi trang.
   - Commit theo dạng `fix(lecture-07)`.
5. `exercises.md`: soạn, rà toán, rà văn phong.
6. Thẻ Bài 7 trong `index.html` thêm nhóm "Bài tập". Thẻ hiện thiếu nhóm này; hiển thị `Chưa có` cho tới khi tệp qua kiểm định.

**Rủi ro:**
- **Tăng số trang.** Deck tăng từ 40 lên khoảng 66 trang. Có nguy cơ vượt 120 phút; phải rút ghi chú diễn giả và đưa LSVI cùng chi tiết bốn khối vào ghi chú bài giảng.
- **Liên kết `data-note-topic-id`.** Giữ các mã `lec-07-topic-NN` hiện có. Trang mới nhận mã có sẵn hoặc mã mới từ 17 trở đi; cập nhật bảng ánh xạ hai chiều trong outline và storyboard.
- **Ví dụ thêm ngoài nguồn phải ghi sai khác.** Gồm ví dụ hai trạng thái Bellman chiếu, ví dụ phân kỳ w→2w (Sutton–Barto §11.2), ví dụ hai mục tiêu trên mẫu thứ hai của HW8, thuật toán Q-learning, và số liệu notebook dùng trong L07-04.
- **Đánh số trái mẫu.** Đánh số theo AGENTS (bộ đếm chung cho Thuật toán) khác mẫu math-4-AI.
- **Không cần ngoại lệ raster.** Mọi hình mới đều là SVG: hình cấu trúc chương, sơ đồ hai trạng thái.
- **CSS cục bộ** phải được dọn sau khi tách trang (G4). Tránh sửa `lecture-slide.css`; nếu buộc phải sửa thì phải kiểm lại mọi deck.

**Câu hỏi cho người dùng:**
- **Q1.** Chấp nhận 7 mạch (tách kết luận khỏi Q-learning), hay muốn 6 mạch bằng cách gộp Sarsa với Q-learning?
- **Q2.** Ví dụ dự đoán (L07-06, L07-14, L07-19): chỉ đổi tên ("trạng thái hai đặc trưng"), hay viết lại thành "Lunar Lander thu nhỏ" và tính lại toàn bộ?
- **Q3.** Cho phép sửa ô Markdown của hai notebook (tham chiếu số mục; ký hiệu $c\to\kappa$, $\Phi(s)$, $\overline{\mathrm{VE}}$) mà không chạy lại?
- **Q4.** Ghi chú Bài 03–06 chưa có số hiệu. Mục Tiên quyết tạm dẫn theo "ghi chú Bài 06, mục 6" kèm phát biểu lại, hay đánh số lại các bài trước trước?
- **Q5.** Duyệt các phần bổ sung ngoài nguồn: thuật toán Q-learning, ba ví dụ mới, ví dụ dẫn nhập bằng số liệu notebook.
- **Q6.** Đổi tên trạng thái chuỗi sang chữ đứng và đổi $u(a)\to\sigma(a)$: việc này đụng tới HW7, HW8, X02, X03 và một SVG.
