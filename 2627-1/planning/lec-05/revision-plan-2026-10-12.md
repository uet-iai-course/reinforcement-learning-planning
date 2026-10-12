# Kế hoạch sửa Bài 05 theo chuẩn 2026-10-12

Đây là báo cáo chỉ đọc. Tôi không sửa, tạo hay xóa tệp nào và không commit. Báo cáo dựa trên các tệp sau:
- `AGENTS.md`: các mục được giao.
- `CLAUDE.md`.
- Hai mẫu `materials/_templates/{lecture-note,exercises}.md`.
- Deck `2627-1/lecture-05-du-doan-phi-mo-hinh.html`: đã đọc đủ 45 trang và chạy `density.py`.
- Ghi chú `materials/lec-05/lecture-note.md`: 714 dòng, khoảng 9 664 từ theo `wc -w`, số này tính cả ký hiệu LaTeX.
- Các ô Markdown của notebook LunarLander.
- `planning/lec-05/{outline,storyboard,review-log}.md`.
- Bộ mẫu deck, ghi chú và bài tập Bài 07 của math-4-AI.

**Bốn phát hiện ngoài phạm vi trang:**
1. **Kế hoạch không khớp HTML.** Commit `bc95338` (D02–D06) chỉ sửa HTML. `outline.md`, `storyboard.md` và `review-log.md` chưa ghi thay đổi: không có bảng $\operatorname{Var}=320/441$, và thứ tự trang khác. HTML đặt D05 trước D03, còn outline và storyboard xếp D03, D04, D05. Ngoài ra, outline vẫn ghi "không tạo notebook".
2. **Index thiếu nhóm "Bài tập".** Thẻ Bài 5 trong `index.html` không có nhóm này. Theo `AGENTS.md`, nhóm phải có mặt và ghi `Chưa có` cho đến khi tệp đạt kiểm định.
3. **Liên kết tới tệp không được theo dõi.** E03 (deck) và các dòng 652, 712–713 (ghi chú) trỏ tới `../RL-hk2-2025-2026/...pdf`. Các tệp này không nằm trong git nên liên kết hỏng khi công khai.
4. **CSS cục bộ thu nhỏ chữ.** B10 và C05 dùng `.92em`, D09 dùng `.9em`, D05 đặt `.math-large` về `1em`. Chuẩn mới cấm cách làm này.

---

## A. Deck

### A1. Mạch hiện tại và đề xuất

Hiện có 5 mạch (A–E), không mạch nào có trang tiêu đề mạch.

Đề xuất 6 mạch: tách mạch D thành hai mạch, vì storyboard đã chia sẵn hai cụm D1 và D2 với hai chức năng khác nhau.
- D1 so sánh mục tiêu cập nhật trên mẫu mới.
- D2 xử lý dữ liệu cố định.

Lý do tách: sau khi tách các trang vượt trần, mạch D sẽ có khoảng 18 trang. Số 6 vẫn trong khoảng 5–7.

Có một phương án 7 mạch: tách tiếp mạch B thành "Lợi tức và mẫu Monte Carlo" (B01–B05) và "Cập nhật gia tăng và thuật toán Monte Carlo" (B06–B13). Phương án này chỉ nên dùng khi người dùng muốn.

| N | Mạch (nhãn) | Tên mạch | Dòng dẫn (≤25 âm tiết) | Từ khóa | Mã trang tiêu đề | `id` |
|---|---|---|---|---|---|---|
| 1 | Mở đầu (A) | Bài toán dự đoán phi mô hình (bìa là tiêu đề mạch) | — | — | L05-A01 | — |
| 2 | B | Lợi tức và ước lượng Monte Carlo | "Muốn ước lượng giá trị khi chưa biết mô hình, phải lấy trung bình lợi tức của các lượt đã kết thúc" (22) | Lượt · Lợi tức · Lần ghé · Trung bình gia tăng · Bước học | L05-B00 | `mach-2` |
| 3 | C | Sai phân thời gian TD(0) | "Muốn cập nhật trước khi lượt kết thúc, phải thay phần lợi tức chưa quan sát bằng giá trị ước lượng" (21) | Mục tiêu một bước · Sai số TD · Trạng thái kết thúc · Tự chuyển · Chi phí mỗi bước | L05-C00 | `mach-3` |
| 4 | D (D01–D07) | Độ chệch, phương sai và hội tụ | "Muốn so sánh MC và TD(0), phải tách độ chệch, phương sai của mục tiêu và điều kiện hội tụ" (20) | Giá trị chuẩn · Độ chệch · Phương sai · Điều kiện bước học · Hội tụ | L05-D00 | `mach-4` |
| 5 | D (D08–D12) | Dữ liệu cố định và cập nhật theo lô | "Muốn dự đoán khi không thu thêm lượt, phải chọn tiêu chuẩn khớp dữ liệu trước khi quét lại" (19) | Cập nhật theo lô · Lượt quét · Khớp lợi tức · Mô hình Markov thực nghiệm | L05-DT (vì `L05-D00` đã dùng; ghi ngoại lệ trong storyboard) | `mach-5` |
| 6 | E | Tổng kết và chuyển tiếp | "Muốn chọn phương pháp dự đoán, phải nêu dữ liệu có sẵn, mục tiêu cập nhật và giả thiết của bảo đảm" (22) | Giả thiết không được bỏ · Câu hỏi tự kiểm tra · Tài liệu đọc · Điều khiển phi mô hình | L05-E00 | `mach-6` |

Kiểm tra tên mạch:
- Không tên nào trùng tiêu đề trang nội dung đầu của mạch đó (B01 mới, C01, D01, D08 mới, E01 mới; xem A3).
- Ghi chú diễn giả của mỗi trang tiêu đề dài 40–100 âm tiết và nêu ba điều: kết quả kế thừa, nhiệm vụ của mạch, đầu ra cho mạch sau.

### A2. Mạch mở đầu và mạch kết luận

**Mạch mở đầu: trạng thái hiện tại (A01–A05)**
- **Bìa A01:**
  - Thiếu đơn vị.
  - Dòng hộp "Đánh giá một chính sách cố định từ dữ liệu tương tác." là cụm danh từ, chưa phải câu luận đề.
  - "sai phân thời gian (TD)" thiếu thuật ngữ gốc "temporal difference".
- **Thiếu trang "Tiên quyết và quy ước".** Phần tiên quyết hiện chỉ là chú thích trong A02.
- **Mục tiêu và nội dung bị gộp** trong A02. Mục tiêu chưa đo được, nội dung chưa đánh số mạch.
- **Vấn đề trung tâm** nằm rải ở A03 dưới dạng hai thẻ so sánh đầu vào, chưa có câu trả lời của từng mạch.
- **Thiếu trang khung chung**, dù bài có cấu trúc cập nhật chung $V\leftarrow V+\alpha[\text{mục tiêu}-V]$. Hiện cấu trúc này chỉ được nhắc ở B07.

**Mạch mở đầu: thứ tự đề xuất**
1. **A01 Bìa.**
   - h1 "Dự đoán phi mô hình"; h3 "Monte Carlo và sai phân thời gian · Bài 05".
   - Dòng "Học tăng cường · Học kỳ 1, 2026–2027" và dòng "Trường Đại học Công nghệ · Đại học Quốc gia Hà Nội" (như deck 02, 04).
   - Câu luận đề, ví dụ: "Giá trị của một chính sách cố định được ước lượng từ các lượt quan sát, bằng lợi tức đầy đủ hoặc bằng mục tiêu một bước."
2. **A04, đổi chức năng thành "Tiên quyết và quy ước"** (giữ mã và `lec-05-topic-01`).
   - "Nhắc lại:" $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ và lợi tức (return) (Bài 03); phương trình Bellman kỳ vọng (Bài 03); đánh giá chính sách bằng quy hoạch động cần $P_\pi,r_\pi$ (Bài 04).
   - "Ký hiệu:" $\mathcal S$ hữu hạn gồm các trạng thái không kết thúc, $\mathcal S^+$ gồm cả trạng thái kết thúc; mẫu chuyển $(S_t,A_t,R_{t+1},S_{t+1})$ với $A_t\sim\pi(\cdot\mid S_t)$; $V$ là bảng ước lượng, $v_\pi$ là giá trị thật.
   - "Giả thiết:" $\pi$ Markov cố định; môi trường Markov dừng; trạng thái quan sát đầy đủ.
   - Giới hạn: ≤6 dòng, ≤55 âm tiết.
3. **L05-A06 "Mục tiêu học tập"** (trang mới), giữ MT1–MT6 của outline, mỗi mục ứng với một sản phẩm kiểm tra được:
   - Tính lợi tức chiết khấu của một lượt.
   - Lập tập mẫu theo hai quy tắc lần ghé.
   - Thực hiện một lượt MC với $1/N(s)$ và bước hằng.
   - Thực hiện một lượt TD(0).
   - Tính độ chệch, phương sai của mục tiêu và nêu điều kiện hội tụ.
   - Chọn phương pháp kèm tiêu chuẩn trên dữ liệu cố định.
4. **A02, đổi thành "Nội dung":** danh sách 1–6 khớp A1 và dòng "Tài liệu đọc trước: Sutton và Barto (2018), §5.1, §6.1–6.3."
5. **A03, đổi thành "Vấn đề trung tâm":**
   - Một dòng bài toán: ước lượng $v_\pi$ chỉ từ các lượt sinh theo $\pi$.
   - Năm dòng trả lời có điều kiện:
     - (2) Trung bình lợi tức sau lần ghé, khi lượt kết thúc.
     - (3) Mục tiêu một bước, khi trạng thái Markov.
     - (4) Mục tiêu MC không chệch; TD có thể chệch; hội tụ chỉ khi đủ điều kiện bước học.
     - (5) Trên dữ liệu cố định, hai nghiệm khác nhau theo tiêu chuẩn.
     - (6) Lựa chọn theo dữ liệu có sẵn.
   - Có thể đặt hình `learning-route.svg` ở trang này.
6. **L05-A07 "Khung chung của quy tắc cập nhật"** (trang mới, 3–4 dòng):
   - Ước lượng mới bằng ước lượng cũ cộng bước học nhân hiệu giữa mục tiêu cập nhật và ước lượng cũ.
   - MC: mục tiêu là lợi tức.
   - TD(0): mục tiêu là thưởng cộng giá trị chiết khấu ở trạng thái sau.
   - Theo lô: quét lại tập cố định.
7. **A05 gộp đi.** Câu hỏi 1 và 3 chuyển sang "Câu hỏi tự kiểm tra" và Bài tập 05.1. Ý "một mẫu chỉ là một kết quả" chuyển vào trang vấn đề B01.

**Mạch kết luận (6)**
- **L05-E00:** trang tiêu đề mạch.
- **Bảng "Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán"** (có thể thành hai trang, E02 và E02b, để không vượt trần 80):
  - Lợi tức truy hồi | lượt kết thúc tại $T$, $G_T=0$; $\gamma=1$ chỉ khi kết thúc hợp lệ | $G_t=R_{t+1}+\gamma G_{t+1}$.
  - Kỳ vọng mẫu sau mỗi lần ghé | $\pi$ Markov cố định, môi trường Markov dừng | $\mathbb E_\pi[G_{t_k}\mid\cdot]=v_\pi(s)$.
  - Trung bình gia tăng | đếm riêng $N(s)$ | $V_n=V_{n-1}+\frac1n(g_n-V_{n-1})$.
  - Hội tụ MC | lượt độc lập cùng phân phối, kết thúc hầu chắc chắn, thưởng bị chặn, xác suất ghé dương, bước $1/N(s)$ | $V_n(s)\to v_\pi(s)$.
  - Độ chệch mục tiêu TD | bảng $V$ cố định, dữ liệu theo $\pi$ | $\gamma\mathbb E_\pi[V(S_{t+1})-v_\pi(S_{t+1})\mid s]$.
  - Phương sai mục tiêu lý tưởng | dùng $v_\pi$, mômen bậc hai hữu hạn | $\operatorname{Var}(Y^*)\le\operatorname{Var}(G_t)$.
  - Hội tụ TD(0) | hữu hạn, $\pi$ cố định, mỗi trạng thái cập nhật vô hạn lần, $\sum\alpha=\infty$, $\sum\alpha^2<\infty$, $\gamma<1$ hoặc kết thúc hợp lệ | $V\to v_\pi$ với xác suất 1.
  - Nghiệm theo lô | dữ liệu cố định, bước đủ nhỏ, quét đến ổn định | MC: trung bình lợi tức; TD: $V=\hat r+\gamma\hat PV$.
- **Bảng "Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng"** (E02c):
  - MC (lần ghé đầu tiên hoặc mọi lần ghé) | $V(S_t)\leftarrow V(S_t)+\alpha_{N}[G_t-V(S_t)]$ | lượt hoàn chỉnh theo $\pi$ | hết $M$ lượt.
  - TD(0) | $V(S_t)\leftarrow V(S_t)+\alpha_n[R_{t+1}+\gamma V(S_{t+1})-V(S_t)]$ | từng chuyển theo $\pi$ | hết $B$ chuyển.
  - Theo lô (MC hoặc TD) | $V_{k+1}=V_k+$ tổng gia số | tập $\mathcal D$ quét lại | $\max_s|V_{k+1}-V_k|<\varepsilon$ hoặc hết $K$ lượt quét.
- **Bảng hội tụ "Phương pháp | Giả thiết không được bỏ | Kết luận"** (E02d), vì bài có nhiều thuật toán:
  - MC lần ghé đầu tiên.
  - MC mọi lần ghé.
  - MC bước hằng: không có bảo đảm, có dao động.
  - TD(0) với điều kiện Robbins–Monro.
  - TD theo lô.
- **Bài tập tổng hợp có lời giải trên mặt trang** (thêm L05-E06 và E06b), ví dụ "Bài tập: dãy bốn ô, lượt thứ ba".
  - Dữ kiện: lượt $S\to X\to G$, thưởng $(0,1)$. Tiếp tục MC lần ghé đầu tiên ($\alpha=0.5$) từ $(-0.25,-0.25)$ và TD(0) từ $(-0.375,0.375)$.
  - Số đề xuất: MC cho $(0.375,0.375)$; TD cho $V(S)=0$, $V(X)=0.6875$.
  - Đối chiếu với $(11/21,19/21)$.
  - Tác tử rà toán phải tính lại.
- **Trang trả lời vấn đề trung tâm** (E01 sửa):
  - Ba kết luận có điều kiện: có lượt hoàn chỉnh thì dùng MC; cần cập nhật sau mỗi chuyển và trạng thái Markov thì dùng TD(0); dữ liệu cố định thì phải chọn tiêu chuẩn.
  - Dòng "Nguồn: Sutton và Barto (2018), §5.1, §6.1–6.3; bài giảng gốc, tr. 28, 33."
- **"Câu hỏi tự kiểm tra"** (E04 sửa), mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng.", gồm bốn câu:
  - Lượt bị cắt ngắn có cho mẫu MC không.
  - Khi nào mục tiêu TD không chệch.
  - Bước hằng có thỏa $\sum\alpha^2<\infty$ không.
  - Hai nghiệm theo lô khác nhau vì tiêu chuẩn nào.
- **"Bài tập về nhà và tài liệu đọc"** (E03 gộp E05):
  - Bảng `Mạch | Bài tập` theo mục C.
  - Dòng "Tài liệu đọc: Sutton và Barto (2018), §2.4–2.5, §5.1, §6.1–6.3".
  - Dòng "Ghi chú bài giảng · Bài tập" trỏ viewer.
  - Một dòng nối sang Bài 06 (nguồn tr. 32).
  - Bỏ liên kết PDF HW05.

### A3. Bảng từng trang

Quy ước: "dòng" và "max/dòng" lấy từ `density.py`. Với trang mục tiêu, nội dung, tổng kết và bảng so sánh, trần là 80 âm tiết; các trang khác trần là 60.

| mã | âm tiết | vấn đề theo chuẩn mới | quyết định | đề xuất cụ thể |
|---|---|---|---|---|
| A01 | 34 | Câu luận đề là cụm danh từ; thiếu đơn vị; "(TD)" thiếu "temporal difference" | sửa | Theo A2. Câu luận đề trần thuật; thêm dòng đơn vị; "sai phân thời gian (temporal difference, TD)" |
| A02 | 64/80 | 7 dòng; gộp lộ trình, mục tiêu, tiên quyết; caption "Tiên quyết:" là nhãn ngoài danh sách; mục tiêu không đánh số mạch | tách | A02 thành "Nội dung"; thêm A06 "Mục tiêu học tập"; tiên quyết chuyển sang A04 |
| A03 | 80 | Vượt trần (1,33×); 10 dòng; 2 thẻ và 1 hộp (>1 khung) | sửa | Thành "Vấn đề trung tâm" (A2); danh sách đầu vào quy hoạch động và mẫu chuyển sang ghi chú diễn giả |
| A04 | 56 | 7 dòng; 2 thẻ; định nghĩa bằng dấu hai chấm ("$v_\pi$: giá trị thật"); "lợi tức" thiếu "(return)" | sửa | Thành "Tiên quyết và quy ước" (A2); viết "là"; đặt ngay sau A01 |
| A05 | 68 | Dòng 22 âm tiết; tiêu đề "Kiểm tra…"; mạch mở đầu không còn chỗ cho trang kiểm tra | gộp | Câu 1 và 3 sang E04 và Bài tập 05.1; ý chính sang B01 |
| A06 (mới) | — | Thiếu trang mục tiêu | thêm | Sáu mục tiêu kèm sản phẩm (≤80) |
| A07 (mới) | — | Thiếu trang khung cập nhật chung | thêm | 3–4 dòng (A2) |
| B00 (mới) | — | Thiếu trang tiêu đề mạch | thêm | Theo A1 |
| B01 | 58 | Dòng 31 âm tiết; hộp một câu khoảng 40 âm tiết; nhãn "Lượt:", "Ý tưởng Monte Carlo:" ngoài danh sách; gộp vấn đề, ví dụ, định nghĩa lượt và trực giác; không mở bằng "Muốn…"/"Nhu cầu:" | tách | **B01 "Ví dụ: dãy bốn ô"**: "Nhu cầu:" ước lượng $v_\pi(S),v_\pi(X)$ khi chưa biết xác suất 0.8/0.2; hình; dữ kiện; "Lượt (episode) là…". **B01b "Ước lượng bằng trung bình lợi tức"**: **Trực quan.** hai dòng |
| B02 | 36 | Dòng 28 âm tiết; thiếu "(visit)" | sửa | Tách câu định nghĩa lần ghé (visit) thành hai dòng; hộp giữ |
| B03 | 28 | Đạt; lợi tức chưa có nhãn định nghĩa | giữ | Thêm **Định nghĩa.** và "(Định nghĩa 05.2)" |
| B04 | 105 | **>1,5× trần (nghiêm trọng)**; 7 dòng; dòng 33 âm tiết; hộp hai câu chứa mệnh đề Markov; ghi chú 257 âm tiết và dẫn tên trang khác | tách | **B04 "Lần ghé đầu tiên và mọi lần ghé"**: hai định nghĩa, "(first-visit)", "(every-visit)", bảng; khoảng 40 âm tiết. **B04b "Kỳ vọng của lợi tức sau mỗi lần ghé"**: **Mệnh đề.** giả thiết và kết luận; **Chứng minh.** một dòng (tính Markov mạnh). Câu trọng số 2/3 sang ghi chú diễn giả; bỏ "ở trang 'Tính không chệch…'" |
| B05 | 36 | Định nghĩa ký hiệu bằng dấu hai chấm ("$g_i(s)$: …") | sửa | "Đặt $g_i(s)$ là…"; nhãn **Định nghĩa.** cho $V_n(s)$ |
| B06 | 53 | Dòng 27 âm tiết; nhãn "Yêu cầu:" không cho phép; 2 thẻ và 1 hộp; trang ví dụ thiếu tiền tố | sửa | Tiêu đề "Ví dụ: trung bình tại X khi thêm mẫu thứ ba"; dữ kiện, "Tính…", hai dòng tính thay hai thẻ; hộp thành "Diễn giải:"; giữ SVG |
| B07 | 54 | 4 khối công thức theo phép đo (>3); hộp và chú thích; khung chung lặp lại | sửa | Một khối `aligned` (Mệnh đề 05.7) và "Chứng minh." một dòng; dòng khung chung sang A07; dòng khởi tạo $N(s)$ sang B10; "mục tiêu cập nhật (update target)" |
| B08 | 72 | Vượt trần; dòng 32 âm tiết; câu "môi trường không dừng…" là diễn giải | tách | **B08 "Ví dụ: bước học hằng trên hai mẫu"** (bảng). **B08b "Bước học hằng"**: **Định nghĩa.**, trọng số $\alpha(1-\alpha)^{n-i}$, "Ý nghĩa:", **Nhận xét.** dao động (nhận thẻ bước hằng từ B12) |
| B09 | 50 | Tiêu đề chưa theo "Ví dụ:"; chú thích dạng chuỗi mũi tên "0→0.5→0.75" | sửa | "Ví dụ: bốn cấu hình Monte Carlo trên lượt thứ nhất"; chuỗi mũi tên đổi thành câu có số |
| B10 | 77 | Vượt trần; giả mã khoảng 10 dòng (>8); CSS thu chữ .92em | tách | **B10**: đầu vào, đầu ra, giả thiết, khởi tạo, sinh lượt, tính lùi $G_t$. **B10b** cùng tiêu đề: chọn lần ghé xuôi, cập nhật, dừng sau $M$ lượt. Xóa luật CSS; ghi "(Thuật toán 05.11)" |
| B11 | 39 | Tiêu đề thiếu "Ví dụ:" | sửa | "Ví dụ: dãy bốn ô, Monte Carlo trên lượt thứ hai"; dùng khuôn bảng cố định |
| B12 | 132 | **>2× trần (nghiêm trọng)**; 11 dòng; dòng 38 âm tiết; 3 thẻ; ghi chú 295 âm tiết; "không chệch" định nghĩa bằng dấu hai chấm | tách | **B12 "Hội tụ của Monte Carlo lần ghé đầu tiên"** (Mệnh đề, đủ giả thiết). **B12b "Hội tụ của Monte Carlo mọi lần ghé"** (Định lý, đủ giả thiết; "Lưu ý:" không bảo đảm không chệch ở số lượt hữu hạn). Thẻ bước hằng sang B08b. "không chệch (unbiased) là…". Ghi chú diễn giả chia theo hai trang |
| B13 | 50 | Tiêu đề "Kiểm tra…"; cụm MC thiếu bài tập có "Lời giải:" trên mặt trang | sửa và thêm | **B13 "Bài tập: chọn mẫu Monte Carlo tại X"**. **B13b** cùng tiêu đề với "Lời giải:" từng dòng: $(1,-1)\to0$; $(1,1,-1)\to1/3$; $0.5$; $-0.25$; một câu kết. Ghi chú diễn giả nêu năng lực và "Gợi ý:" |
| C00 (mới) | — | Thiếu trang tiêu đề mạch | thêm | Theo A1 |
| C01 | 38 | 2 thẻ và hộp; không mở bằng "Nhu cầu:"; chưa nêu giới hạn của MC trong một dòng | sửa | "Nhu cầu: cập nhật sau chuyển $S\to X$ khi lượt chưa kết thúc"; một dòng "MC cần lượt kết thúc nên chưa có $G_0$"; hai thẻ thành hai dòng; giữ hình |
| C02 | 37 | Dòng 24 âm tiết; hộp hai câu; "bootstrap" không có tên tiếng Việt | sửa | Nhãn **Trực quan.**; "mục tiêu bootstrap (bootstrap target)"; tách dòng |
| C03 | 28 | 3 thẻ dạng bước; tiêu đề thiếu "Ví dụ:"; chú thích tham chiếu tiến tới C07 | sửa | "Ví dụ: dãy bốn ô, một bước TD(0)": dữ kiện, "Tính…", ba dòng (mục tiêu, sai lệch, giá trị mới), "Diễn giải:"; câu về nguồn gốc bảng sang ghi chú diễn giả |
| C04 | 46 | Chú thích dòng 23 âm tiết; thiếu nhãn định nghĩa | sửa | **Định nghĩa.** mục tiêu TD, sai số TD (TD error); "(Định nghĩa 05.15)"; chú thích một dòng |
| C05 | 84 | Vượt trần (1,4×); giả mã >8 dòng; CSS thu chữ | tách | **C05**: đầu vào, đầu ra, giả thiết, khởi tạo, bước 1–4. **C05b** cùng tiêu đề: đọc trước rồi ghi, chuyển trạng thái, hai loại dừng. Xóa CSS |
| C06 | 61 | 10 dòng; dòng 26 âm tiết; 2 thẻ và hộp | tách | **C06 "Ví dụ: chuyển vào trạng thái kết thúc"** ($X\to G$). **C06b "Ví dụ: tự chuyển"**: hoặc giữ số liệu minh họa và ghi rõ, hoặc dùng ô tự chuyển Lunar Lander của notebook (§7.1; cần người dùng duyệt) |
| C07 | 47 | 7 dòng; khuôn bảng khác C08 và ghi chú (có cột $t$, thiếu cột sai số TD) | sửa | "Ví dụ: dãy bốn ô, TD(0) trên lượt thứ nhất"; khuôn bảng cố định `Chuyển | Thưởng | Mục tiêu | Sai số TD | V(S) | V(X)` dùng chung cho C07, C08 và ghi chú |
| C08 | 36 | 7 dòng | sửa | "Ví dụ: dãy bốn ô, TD(0) trên lượt thứ hai"; cùng khuôn bảng; bỏ khối công thức đã có trong bảng |
| C09 | 87/80 | Bảng so sánh vượt trần; dòng 22 âm tiết; hộp | sửa | Chú thích và hộp sang ghi chú diễn giả. Nếu thiếu thời lượng, chuyển cả trang vào ghi chú bài giảng |
| C10 | 48 | 7 dòng; 2 thẻ và hộp câu hỏi; tiêu đề "Kiểm tra…"; thiếu lời giải trên mặt trang | sửa và thêm | **C10 "Bài tập: một bước TD(0) từ cùng bảng"**. **C10b** "Lời giải:": (a) $0.5$, $0.25$, $0.375$; (b) $-1$, $-1.25$, $-0.375$; các phần tử giữ nguyên |
| D00 (mới) | — | Thiếu trang tiêu đề mạch | thêm | Theo A1 |
| D01 | 84/80 | Bảng so sánh vượt trần; dòng 28 âm tiết; danh sách và hộp | sửa | "Ví dụ: dãy bốn ô, MC và TD(0) sau hai lượt"; "Nhu cầu:" một dòng; giữ bảng và một câu kết; hai gạch đầu dòng sang ghi chú diễn giả |
| D02 | 61 | Vượt trần nhẹ; dòng 25 âm tiết; dùng Bellman kỳ vọng mà không có "Nhắc lại:" | sửa | "Nhắc lại: phương trình Bellman kỳ vọng (Bài 03)"; bỏ câu dẫn dài; giữ bảng độ lệch |
| D05 | 72 | Vượt trần; dòng 27 âm tiết; 3 khối công thức; gộp ví dụ, định nghĩa, công thức tổng quát, kiểm và so với MC; độ chệch định nghĩa bằng dấu hai chấm; CSS `.math-large` | tách | **D05 "Ví dụ: kỳ vọng mục tiêu TD tại S"**: $0.2$ so với $11/21$, "Diễn giải:". **D05b "Độ chệch của mục tiêu TD"**: **Định nghĩa.** "độ chệch (bias) là…", **Mệnh đề.** công thức, "Ý nghĩa:". Bỏ CSS; ghi chú diễn giả chia đôi |
| D03 | 38 | Dòng 21 âm tiết; tiêu đề chưa theo "Ví dụ:" | sửa | "Ví dụ: dãy bảy ô với thưởng thưa" |
| D04 | 31 | Chú thích hai dòng >20 âm tiết | sửa | "Ví dụ: dãy bảy ô, hai lợi tức từ S"; một câu kết có số |
| D06 | 54 | Dòng 28 âm tiết; hộp hai câu; phát biểu kết quả trộn với bảng số; ghi chú 309 âm tiết | tách | **D06 "Ví dụ: phương sai mục tiêu trên hai dãy"** (bảng, "Diễn giải:" 84 % và 20 %), đặt trước. **D06b "Phương sai của mục tiêu lý tưởng"**: **Mệnh đề.**, **Chứng minh.** một dòng (luật phương sai toàn phần), "Lưu ý:" về $V$ đang học. Ghi chú diễn giả chia đôi |
| D07 | 68 | 8 dòng; dòng 29 âm tiết; 2 thẻ và hộp; ghi chú 195 âm tiết lặp điều kiện MC và dẫn tên trang | sửa | **Định lý.** bốn dòng giả thiết và kết luận "(Định lý 05.25)"; hộp chuyển sang B08b; ghi chú bỏ phần lặp MC và tham chiếu tên trang |
| D13 và D13b (mới) | — | Mạch 4 chưa có bài tập riêng (D12 đang kiểm cả hai cụm) | thêm | "Bài tập: nhận định về độ chệch, phương sai và bước học", nhận câu 2–4 của D12; lời giải trên mặt trang. Đặt sau D07 |
| DT (mới) | — | Thiếu trang tiêu đề mạch 5 | thêm | Theo A1 |
| D08 | 68 | Vượt trần; dòng 30 âm tiết; 7 dòng; tiêu đề gần trùng tên mạch | sửa | "Ví dụ: tám lượt hai trạng thái A, B"; "Nhu cầu:" một dòng; bảng; hai cách đọc thành **Trực quan.** hai dòng ngắn. Đích ≤50 âm tiết |
| D09 | 94 | **>1,5× trần (nghiêm trọng)**; 12 dòng; CSS thu chữ .9em; ký hiệu định nghĩa bằng dấu hai chấm | tách | **D09 "Ví dụ: tám lượt A, B, lượt quét đầu"**. **D09b "Thuật toán cập nhật theo lô"** (≤8 dòng). Xóa CSS; "Đặt $k$ là…" |
| D10 | 38 | Đạt (3 khối công thức, đúng trần) | giữ | Nhãn **Mệnh đề.** và số hiệu |
| D11 | 38 | 7 dòng; dòng 22 âm tiết | sửa | Công thức đóng của $V_k(A)$ sang ghi chú diễn giả; nhãn **Mệnh đề.** |
| D12 | 98 | **>1,5× trần (nghiêm trọng)**; 4 câu hỏi; mặt trang dẫn "trang Giá trị chuẩn…" (lời chỉ đường); tiêu đề "Kiểm tra…"; thiếu lời giải trên mặt trang | tách | **D12 "Bài tập: hai nghiệm trên tám lượt A, B"** giữ câu 1. **D12b** "Lời giải:". Câu 2–4 sang D13 |
| E00 (mới) | — | Thiếu trang tiêu đề mạch | thêm | "Tổng kết và chuyển tiếp" |
| E01 | 89/80 | Bảng so sánh vượt trần; dòng 21 âm tiết | sửa | Thành trang trả lời vấn đề trung tâm, kèm dòng "Nguồn:" (A2) |
| E02 | 122/80 | **>1,5× trần 80 (nghiêm trọng)**; 8 dòng; dòng 39 âm tiết; dòng nối Bài 06 nằm trong chú thích; ghi chú mở bằng "Bảng thu gọn…" (tài liệu làm chủ ngữ) | tách | E02 và E02b (bảng Kết quả, Giả thiết, Công thức); E02c (khung cập nhật); E02d (điều kiện hội tụ). Dòng nối Bài 06 sang E03; ghi chú mở bằng đối tượng |
| E06 và E06b (mới) | — | Thiếu bài tập tổng hợp có lời giải | thêm | Theo A2 |
| E03 | 88 | Vượt trần; 11 dòng; 3 thẻ và hộp; liên kết PDF HW05 không được theo dõi | sửa | "Bài tập về nhà và tài liệu đọc" (A2); lời giải HW6 và HW7 trong ghi chú diễn giả chuyển sang `exercises.md` |
| E04 | 65 | Vượt trần; 3 thẻ và hộp; không mở bằng câu chuẩn | sửa | "Câu hỏi tự kiểm tra" (A2) |
| E05 | 78 | Vượt trần | gộp | Gộp vào E03 |

**Ước lượng sau sửa:** khoảng 69 trang. Phân bổ đề xuất: mở đầu 10 phút, mạch 2 32 phút, mạch 3 24 phút, mạch 4 24 phút, mạch 5 14 phút, mạch 6 16 phút; tổng 120. Nếu thời lượng vượt, đưa C09, B09 và D04 sang ghi chú bài giảng, đồng thời ghi lý do trong storyboard.

### A4. Cụm khái niệm và sáu bước

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Thiếu |
|---|---|---|---|---|---|---|---|
| Lợi tức và mẫu MC (khái niệm) | B01 | B01 (hộp) | B02 | B03, B04, B05 | B09, B11 | B13 | Vấn đề không mở bằng "Muốn…"; trực giác chung trang với vấn đề |
| Trung bình gia tăng (thuật toán con) | B06 | B06 (trục số) | B06: tính tay hai cách trước B07 ✓ | B07 | B09 | B13 (câu 2) | — |
| Bước học hằng | thiếu nhu cầu trong giả thiết của bài (môi trường không dừng nằm ngoài phạm vi) | — | B08 (bảng trước công thức ✓) | B08 | B09, B11 | B13 | Nhu cầu và trực giác. Có thể nối nhiệm vụ "gió" của notebook §12 |
| Thuật toán MC | ngầm ở B09 | — | B03 tính lùi; B05, B09 trước giả mã ✓ | B10 | B11 | B13 | Chưa có câu vấn đề nêu rõ; chưa có lời giải trên mặt trang |
| Hội tụ MC (kết quả) | không có | không có | không có | B12 | không có | D12 (câu 3) | Vấn đề, trực giác, ví dụ, ứng dụng |
| TD(0) (thuật toán) | C01 | C02 | C03: tính tay trước C04, C05 ✓ | C04, C05, C06 | C07, C08, C09 | C10 | Lời giải trên mặt trang |
| Độ chệch mục tiêu | D01, D02 | **thiếu** | D05 (số trước định nghĩa ✓) | D05 | **thiếu** | D12 (câu 2) | Trực giác, ứng dụng, kiểm tra riêng |
| Phương sai mục tiêu | D03 | D04 | D06 (bảng) | D06 | **thiếu** (có thể nối $J$ trong notebook §8) | D12 (câu 2) | Ứng dụng; kiểm tra riêng |
| Hội tụ TD(0) | **thiếu** | **thiếu** (ý Robbins–Monro chỉ có ở ghi chú dòng 513) | $1/n$ | D07 | **thiếu** | D12 (câu 3) | Vấn đề, trực giác, ứng dụng |
| Cập nhật theo lô | D08 | D08 | D09 (tính tay cùng trang với quy trình, đúng thứ tự) | D09 | D10, D11 | D12 | Lời giải trên mặt trang |

Ba thuật toán cần có bước tính tay trước giả mã. Hiện trạng:
- **MC lần ghé đầu tiên:** B03 và B05 có trước B10 ✓.
- **Trung bình gia tăng:** B06 có trước B07 ✓.
- **TD(0):** C03 có trước C04 và C05 ✓.

Khi tách B10, C05 và D09, phải giữ ví dụ đứng trước cả hai trang giả mã.

### A5. Ví dụ xuyên suốt

**Ví dụ hiện có**
- **"Chuỗi ngắn":** $L,S,X,G$; xác suất 0.8/0.2; thưởng ±1; $\gamma=1$. Hai lượt $e_1:S\to X\to S\to X\to G$ và $e_2:S\to X\to S\to L$.
  - Dùng ở B01–B13, C03–C10, D01, D02, D05.
- **"Chuỗi dài":** $L,x_1,S,x_3,x_4,x_5,G$; $\gamma=0.99$. Dùng ở D03, D04, D06.
- **Tám lượt A–B:** Ví dụ 6.4 của Sutton và Barto. Dùng ở D08–D12.
- **Hai ví dụ phụ:** "dãy ô" ở A05 và tự chuyển minh họa ở C06. Ngoài ra còn chuỗi năm ô $c_1..c_5$ của HW05 bài 6, chỉ có trong ghi chú diễn giả E03 và ghi chú bài giảng.

**Tên gọi đề xuất (gọi theo đối tượng)**
- "dãy bốn ô" (thay "chuỗi ngắn").
- "dãy bảy ô" (thay "chuỗi dài").
- "lượt thứ nhất $e_1$ (về $G$)" và "lượt thứ hai $e_2$ (vào $L$)".
- "tám lượt hai trạng thái A, B".
- "dãy năm ô có đứng yên".

Tên trạng thái $S$ trùng chữ với biến ngẫu nhiên $S_t$; nguồn cũng dùng $S(s)$ cho tổng. Đề xuất viết tên ô bằng chữ đứng $\mathrm S,\mathrm X,\mathrm L,\mathrm G,\mathrm A,\mathrm B$, như bộ mẫu math-4-AI làm.

**Nối với LunarLander.** Notebook không dùng dãy ô, nhưng có ba điểm nối trực tiếp:
1. **Tự chuyển (notebook §5, §7.1):** đa số chuyển là tự chuyển. Câu hỏi có lời giải giải tích: $V^*=r/(1-\gamma)$, và $0.995^{100}\approx0.61$ với $\alpha=0.5,\gamma=0.99$. Có thể thay số liệu minh họa của C06b và dùng cho "Trong thực hành" của TD(0).
2. **Cắt ngắn ở bước 1000 (notebook §3, §6):** MC loại các lượt này, còn TD dùng được chuyển của chúng. Đây là ứng dụng của nguyên tắc "kết thúc lượt khác dừng thu thập" (B03, C05).
3. **MC và TD theo lô trên 9216 ô (notebook §9.2):** ô gộp không Markov nên hai nghiệm khác nhau. Đây là phiên bản lớn của ví dụ tám lượt A–B.

Có thể đặt cho dãy bốn ô một câu chuyện "tàu đổ bộ thu nhỏ" (trạng thái kết thúc "rơi" −1 và "nằm yên" +1). Cách này đổi diễn giải ví dụ nguồn, nên chỉ làm khi người dùng đồng ý (D).

---

## B. Ghi chú bài giảng

### B1. Đối chiếu các mục với mạch deck và 11 thành phần

| Dòng | Mục hiện có (topic) | Mạch deck | Thành phần | Thiếu / đổi thứ tự |
|---|---|---|---|---|
| 1 | `# Bài 05: Dự đoán phi mô hình` | — | (1) Tiêu đề | Đổi thành "# Bài 05 — Dự đoán phi mô hình" |
| 3–5 | Hai đoạn mở, không heading | 1 | (2) Giới thiệu | Rút còn ≤1 đoạn. Tách ra (3) **Mục tiêu học tập** dạng danh sách MT1–MT6 và (4) **Kiến thức tiên quyết** dạng gạch đầu dòng có số hiệu, câu quy ước "Số hiệu `04.k`…" |
| — | thiếu | — | (5) Bảng ký hiệu; (6) Bản đồ chủ đề bốn nhóm | Thêm (B6). Bản đồ chủ đề gồm cốt lõi topic-01…16, các nhóm cầu nối, bổ sung, đọc thêm, kèm mục tương ứng |
| 7 | `## Bài toán dự đoán từ dữ liệu` | 1 | (7), phần mở | Thành các đoạn mở của `## 1.`: kết quả Bài 04, bài toán có số liệu (dãy bốn ô), điều chương xây dựng, hình `learning-route.svg` kèm đoạn đọc hình |
| 10 | `### Mẫu chuyển…` (topic-01) | 1 | (7) | Thành `### 1.1` với Định nghĩa 05.1; câu hỏi thành Bài tập 05.1 |
| 40 | `## Dự đoán Monte Carlo` | 2 | (7) | Đổi thành `## 1. Lợi tức và ước lượng Monte Carlo` |
| 43 | `### Lượt và lợi tức` (02) | 2 | (7) | `### 1.2` |
| 98 | `### Ước lượng Monte Carlo` (04) | 2 | (7) | **Lệch thứ tự**: deck đặt định nghĩa lần ghé (B04) trước B05. Chuyển bảng lần ghé và mệnh đề Markov (dòng 140–151) lên trước; mục này thành `### 1.4` |
| 138 | `### Quy tắc lần ghé và bước học` (06) | 2 | (7) | Tách thành `### 1.3 Lần ghé và kỳ vọng mẫu`, `### 1.5 Trung bình gia tăng`, `### 1.6 Bước học hằng và bốn cấu hình` |
| 203 | `### Thuật toán dự đoán Monte Carlo` (03) | 2 | (7) | `### 1.7`. Thêm `### 1.8 Tính không chệch và hội tụ của Monte Carlo`, lấy phần MC của dòng 497–507 để khớp B12 |
| 240 | `## Dự đoán sai phân thời gian TD(0)` | 3 | (7) | `## 2.` |
| 243 | `### Mục tiêu một bước và sai số TD` (07) | 3 | (7) | `### 2.1` |
| 279 | `### Thuật toán TD(0)…` (08) | 3 | (7) | `### 2.2` |
| 313 | `### TD(0) trên hai lượt…` (09) | 3 và 4 | (7) | `### 2.3`. Đoạn 334 và bài tập 336 chuyển sang `### 3.1`, vì D01 thuộc mạch 4 |
| 350 | `## So sánh theo dữ liệu và giả thiết` | 4 và 5 | (7) | Tách thành `## 3. Độ chệch, phương sai và hội tụ` và `## 4. Dữ liệu cố định và cập nhật theo lô` |
| 353 | `### Giá trị chuẩn…` (05) | 4 | (7) | `### 3.1`. **Thiếu bảng độ lệch MC/TD so với chuẩn** có ở D02 |
| 380 | `### Chuỗi dài…` (12) | 4 | (7) | **Lệch thứ tự**: deck đặt D05 (độ chệch) trước D03. Thành `### 3.3` |
| 407 | `### Độ chệch của mục tiêu TD` (10) | 4 | (7) | `### 3.2` |
| 456 | `### Phương sai của mục tiêu` (13) | 4 | (7) | `### 3.4`. **Thiếu bảng số** $320/441$, $256/441$, $0.217$, $0.036$ có ở D06; thiếu phản ví dụ với $V$ đang học |
| 497 | `### Tính không chệch và điều kiện hội tụ` (11) | 2 và 4 | (7) | Phần MC chuyển sang 1.8; phần TD thành `### 3.5` |
| 534 | `### Dự đoán trên dữ liệu cố định` (16) | 5 | (7) | `## 4` gồm 4.1 (vấn đề và lượt quét đầu), 4.2 (thuật toán theo lô), 4.3 (hai nghiệm) |
| 593 | `## Lựa chọn phương pháp và tự kiểm tra` | 6 | (8), (9) | Bỏ heading này; nội dung chia sang (8) và (9) |
| 596 | `### Lựa chọn theo thông tin sẵn có` (14) | 6 | (8) | Thành đoạn mở của `## Tình huống áp dụng và ứng dụng`, giữ topic-14; bài tập 606 sang củng cố mức vận dụng |
| 621 | `### Tổng kết, bài tập và tài liệu đọc` (15) | 6 | (9) | Thành `## Tóm tắt chương` theo cấu trúc mới; bài tập 638 sang củng cố mức nhận biết |
| 650 | `#### Tự luyện với Bài tập tuần 5` | 6 | — | Chuyển sang `exercises.md` (đoạn mở); bỏ liên kết PDF |
| 660 | `#### Bài 5…` | 2, 4 | — | Sang `exercises.md` |
| 668 | `#### Bài 6…` | 4 | — | Sang `exercises.md` |
| 698 | `#### Bài 7…` | 2, 3 | — | Sang `exercises.md` |
| 710 | `#### Tài liệu đọc` | 6 | (11) | Thành `## Hướng dẫn đọc thêm và tài liệu tham khảo`, nêu mục nào dựa trên nguồn nào; bỏ liên kết PDF không được theo dõi |
| — | thiếu | — | (8) hai tình huống áp dụng và danh mục ứng dụng; (10) `## Bài tập củng cố` ba mức | Thêm (B4) |

### B2. Kế hoạch đánh số môi trường

**Bộ đếm chung** (Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán):

| Số hiệu | Khối | Nội dung (mục) |
|---|---|---|
| 05.1 | `definition` | Bài toán dự đoán, mẫu chuyển, dữ liệu theo $\pi$ (1.1) |
| 05.2 | `definition` | Lượt, thời điểm kết thúc $T$, lợi tức chiết khấu, $G_T=0$ (1.2) |
| 05.3 | `proposition` + `proof` | Truy hồi $G_t=R_{t+1}+\gamma G_{t+1}$ (1.2) |
| 05.4 | `definition` | Lần ghé; lần ghé đầu tiên; mọi lần ghé (1.3) |
| 05.5 | `proposition` | Kỳ vọng lợi tức sau lần ghé thứ $k$ bằng $v_\pi(s)$ (tính Markov mạnh). Chứng minh ở mức giáo trình hoặc nguồn có số trang (1.3) |
| 05.6 | `definition` | Ước lượng Monte Carlo $V_n(s)$ (1.4) |
| 05.7 | `proposition` + `proof` | Trung bình gia tăng (1.5) |
| 05.8 | `definition` | Mục tiêu cập nhật, bước học, dạng $V\leftarrow V+\alpha[\text{mục tiêu}-V]$ (1.5) |
| 05.9 | `proposition` + `proof` (quy nạp) | Trọng số của bước học hằng (1.6) |
| 05.10 | `remark` | Hai trục lựa chọn của MC, bốn cấu hình (1.6) |
| 05.11 | `algorithm` | Dự đoán Monte Carlo (1.7) |
| 05.12 | `theorem` | Hội tụ MC lần ghé đầu tiên, luật số lớn (1.8) |
| 05.13 | `theorem` | Hội tụ MC mọi lần ghé. Chứng minh ngoài phạm vi, dẫn nguồn có trang (1.8) |
| 05.14 | `remark` | Bước học hằng không bảo đảm hội tụ; dao động (1.8) |
| 05.15 | `definition` | Mục tiêu TD, sai số TD, mục tiêu bootstrap (2.1) |
| 05.16 | `algorithm` | TD(0) dạng bảng (2.2) |
| 05.17 | `remark` | Trạng thái kết thúc, tự chuyển, cắt ngắn so với kết thúc (2.2) |
| 05.18 | `remark` | Chi phí bộ nhớ và tính toán của MC và TD(0) (2.2) |
| 05.19 | `definition` | Độ chệch của mục tiêu (3.2) |
| 05.20 | `proposition` + `proof` | Công thức độ chệch của mục tiêu TD (3.2) |
| 05.21 | `corollary` | Mục tiêu MC không chệch; mục tiêu TD không chệch khi $V=v_\pi$ tại trạng thái kế tiếp (3.2) |
| 05.22 | `proposition` + `proof` | $\mathbb E[\delta_t\mid S_t=s,V_t]=(T_\pi V_t)(s)-V_t(s)$ (3.2) |
| 05.23 | `theorem` + `proof` theo bước | Phương sai mục tiêu lý tưởng (3.4) |
| 05.24 | `remark` | Không có thứ tự phương sai phổ quát với $V$ đang học, kèm phản ví dụ (3.4) |
| 05.25 | `theorem` | Hội tụ TD(0) dạng bảng. Chứng minh ngoài phạm vi, dẫn nguồn (3.5) |
| 05.26 | `remark` | Ý nghĩa hai điều kiện bước học; bỏ từng giả thiết thì sao (3.5) |
| 05.27 | `algorithm` | Cập nhật theo lô (4.2) |
| 05.28 | `proposition` + `proof` | Nghiệm MC theo lô là trung bình lợi tức (bình phương tối thiểu) (4.3) |
| 05.29 | `proposition` + `proof` | Nghiệm TD theo lô là nghiệm MRP thực nghiệm $V=\hat r+\gamma\hat PV$ (4.3) |
| 05.30 | `remark` | Hai tiêu chuẩn; điều kiện $\alpha<1/4$ chỉ đúng riêng ví dụ A–B; không xếp hạng phổ quát (4.3) |

**Ví dụ** (bộ đếm riêng, khối `example`):
- 05.1 Dãy bốn ô và hai lượt.
- 05.2 Lợi tức của $e_1$ tính ngược.
- 05.3 Hai quy tắc lần ghé trên hai lượt.
- 05.4 Trung bình mẫu tại $X$.
- 05.5 Hai cách tính trung bình khi thêm mẫu $-1$.
- 05.6 Bước hằng $\alpha=0.5$ trên mẫu $(1,-1)$.
- 05.7 Bốn cấu hình MC trên hai lượt.
- 05.8 Tiền tố chưa kết thúc $S\to X$.
- 05.9 Một bước TD(0).
- 05.10 Chuyển vào trạng thái kết thúc; tự chuyển.
- 05.11 TD(0) trên hai lượt.
- 05.12 Giá trị chuẩn của dãy bốn ô.
- 05.13 Độ lệch của hai bảng so với chuẩn.
- 05.14 Độ chệch mục tiêu TD tại $S$ ($-34/105$).
- 05.15 Dãy bảy ô, hai lợi tức từ $S$.
- 05.16 Phương sai $G_t$ và $Y^*$ trên hai dãy.
- 05.17 Tám lượt A–B, lượt quét đầu.
- 05.18 A–B, quét thứ hai và hai nghiệm.
- 05.19 Ô tự chuyển trên Lunar Lander ($V^*=r/(1-\gamma)$).

**Tình huống áp dụng** (`application`): 05.1 và 05.2 (B4).

**Bài tập** (bộ đếm riêng, khối `exercise` + `hint` + `solution`). Số tạm theo thứ tự hiện tại, đánh lại sau khi sắp mục:
- Mười sáu khối "Câu hỏi:" hiện có (dòng 26, 83, 123, 188, 224, 264, 298, 336, 365, 392, 441, 482, 519, 577, 606, 638) thành Bài tập 05.1–05.16.
  - Bài ở dòng 606 và 638 chuyển xuống "Bài tập củng cố".
- Củng cố mới: 05.17–05.22.
- Bài chỉ có trong `exercises.md`: từ 05.23 (C).

### B3. Bảng kiểm "Tiêu chuẩn thứ nhất" và "Trình bày sáng sủa"

**Giọng kể.** Hiện văn bản dùng giọng khách quan và bị động; không có lần nào dùng "chúng ta" hay "ta".
- Đổi sang "chúng ta" ở câu nêu kế hoạch hoặc nhu cầu: dòng 12, 100 ("nên cần quy tắc"), 153, 245, 355, 536.
- Đổi sang "ta" trong phép tính: dòng 159 ("Vì thế,"), 359 ("Thay … cho"), 424 ("trừ … cho"), 470 ("Luật phương sai toàn phần suy ra"), 564.

| Tiêu chí | Vi phạm (dòng) | Cách sửa |
|---|---|---|
| Vấn đề trước công cụ | 12: mở bằng phát biểu bài toán như định nghĩa. 40–45: mở bằng "Xét chuỗi…" nhưng không nêu công cụ cũ thiếu gì. 536: mở bằng điều kiện | Mỗi `##` mở bằng bài toán có số liệu và câu "Để …, chúng ta cần…". Mục 1 nêu giới hạn của Bài 04 (cần $P_\pi,r_\pi$) |
| Công thức bao bởi lời | 53–54, 172–173, 259–260, 421–422, 566–567, 678–681: hai hoặc nhiều công thức liền nhau không có câu nối hay câu đọc. 155: hai phép tính trên một dòng | Câu dẫn trước, câu đọc sau từng công thức; hoặc gộp vào `aligned` kèm câu đọc |
| Ký hiệu gọi tên tại chỗ | 35: $p(s',r\mid s,a)$ chưa giới thiệu. 466: $\sigma(\cdot)$ (σ-đại số) vượt tiên quyết. 18 rồi 79: $\mathcal S$ được định nghĩa hai lần với phạm vi khác nhau | Giới thiệu một lần ở bảng ký hiệu và tại chỗ. Thay $\sigma$ bằng "thông tin của chuyển đầu" hoặc định nghĩa ngắn |
| Mỗi bước có lý do | 147: "tính Markov mạnh cho thấy" không có căn cứ. 468: thiếu bước kỳ vọng lặp. 513: hội tụ TD "dưới các giả thiết chuẩn" không dẫn trang. 569: $0<\alpha<1/4$ không suy diễn. 694: "Khử các ẩn cho" bỏ bước. 81: thời gian kết thúc có kỳ vọng hữu hạn không có lý do | Ghi căn cứ `&&\text{(…)}`; dẫn nguồn có trang; viết đủ phép khử |
| Bản đọc bằng lời, vai trò giả thiết | 503, 513: không có danh sách "Bỏ <giả thiết>: <phản ví dụ>". 478: chưa có phản ví dụ số | Thêm danh sách. Ví dụ: bỏ "bước giảm" thì có dao động (bảng B08); bỏ $v_\pi$ thì với $V(X)=10$ ta có $\operatorname{Var}(Y)=19.36>0.726$; bỏ kết thúc thì xem cắt ngắn ở notebook |
| Ví dụ trước phát biểu | 462: phương sai thiếu ví dụ số trước định lý. 497: hội tụ không có ví dụ | Đưa bảng D06 lên trước 05.23; dùng bảng B08 và đường học notebook §8.1 cho hội tụ |
| Nối mục bằng kết quả | 236 là lời dẫn tới mục khác, không phải đoạn kết ba ý. 348, 591 chỉ có dòng nguồn | Mỗi `##` kết bằng 1–2 đoạn: kết quả kèm số hiệu, giới hạn, mục sau làm gì |
| Không tham chiếu ra ngoài | 310: "đã dùng trong bài giảng". 255: "phép tính đầy đủ nằm ở mục TD(0)…" (tham chiếu theo tên, không theo số). 236, 634: "mục Tính không chệch…". 652, 712–713: liên kết PDF không được theo dõi | Dẫn bằng số hiệu; bỏ liên kết PDF; nêu rõ điều đang tạm chấp nhận |
| Tài liệu không làm chủ ngữ | 3 "Bài học gồm ba phần"; 111 "ghi chú này gọi…"; 623 "Bảng dưới thu gọn…"; 652 "Các yêu cầu dưới đây làm rõ"; 708 "Các bước trung gian nằm trong phần…" | Chủ ngữ là "chúng ta" hoặc đối tượng toán học |
| Câu đủ thành phần | 70 "Trong $e_1$, $T=4$:" là câu mảnh | Viết thành câu |
| Định nghĩa không trộn vào đoạn | 413 (độ chệch), 499 (không chệch), 62 (lợi tức), 45 (lượt) | Dùng khối `definition` |
| Trực giác | Không mục nào có "Một cách trực quan…" kèm câu "đây chưa phải định nghĩa" | Thêm cho 1.2, 1.3, 1.5, 2.1, 3.2, 3.4, 4.1 |
| Nhầm lẫn thường gặp | Có dạng văn xuôi ở 175, 262, 290, 292, 429, 480, 517 | Gom thành `remark` có số |
| Hình được đọc | 47, 58, 60, 253, 384, 388, 460 không có đoạn đọc hình. 573 có đoạn đọc một phần | Thêm đoạn "trên hình cần nhìn…" nối với công thức |
| Một ý một đoạn (≤4 câu) | 151 (khoảng 9 câu, nhiều ý), 164, 175, 262, 517, 575 | Tách đoạn; danh sách cho trường hợp |
| Chứng minh theo bước | 159–162 (trung bình gia tăng), 424–427 (độ chệch), 466–478 (phương sai): nằm trong văn xuôi, không có khối `proof` hay nhãn bước | Khối `proof` với **Bước 1/2**, `aligned` mỗi dấu một dòng, $\square$ |
| Ngoặc lồng (≤1 mỗi câu) | 363, 390: hai ngoặc trong một câu | Tách câu |
| Định lý đủ bốn phần | Không có định lý nào được viết dạng khối | Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi |
| Thuật ngữ gốc ở lần đầu | lợi tức (return) dòng 22; lượt (episode) 45; lần ghé (visit), (first-visit), (every-visit) 56, 100, 113; bước học (step size) 164; mục tiêu cập nhật (update target) 164; bootstrap 251; sai số TD (TD error) 262; độ chệch (bias) 413; phương sai (variance); cập nhật theo lô (batch updating) 548; trạng thái kết thúc (terminal state); "sai phân thời gian" thiếu "temporal difference" | Thêm thuật ngữ gốc ở lần đầu; đồng bộ bảng thuật ngữ trong outline |
| Nhãn bài tập | 16 khối có tiêu đề "Câu hỏi:" | Đổi thành "Bài tập 05.k". Đã dùng "Lời giải", không có "Đáp án" ✓ |

### B4. Các phần cần thêm

**Đoạn móc nối**
- Sau 05.4: quan hệ giữa lần ghé đầu tiên và mọi lần ghé (cùng kỳ vọng, khác số mẫu).
- Sau 05.8: MC và TD là hai lựa chọn mục tiêu trong cùng một khung.
- Sau 05.15: mục tiêu TD là phiên bản một mẫu của $(T_\pi V)(s)$ ở Bài 04.
- Trước và sau 05.25: so với 05.12 và 05.13, kết luận giống nhau nhưng giả thiết bước học khác.
- 05.29 nối với dạng ma trận $(I-\gamma P_\pi)V=r_\pi$ ở Bài 04.

**Đoạn "Trong thực hành"** (dẫn tới notebook):
- **Sau 05.11:** bảng 9216 ô; lượt bị cắt ở bước 1000 bị loại; ô xuất hiện nhiều lần do tự chuyển (notebook §5–6).
- **Sau 05.5:** trên ô gộp, lần ghé đầu tiên và các lần sau có kỳ vọng khác nhau (notebook ô 37).
- **Sau 05.16:** TD dùng được chuyển của lượt bị cắt ngắn; tự chuyển làm thông tin lan chậm (notebook §7.1).
- **Sau 05.20 và 05.23:** đường học TD bắt đầu gần $J(\mathbf 0)$; MC giảm nhanh (notebook §8, kết luận định tính).
- **Sau 05.25:** $\alpha_n=1/n$ thỏa điều kiện nhưng chậm, khác bước hằng (notebook §8.1).
- **Sau 05.29:** nghiệm MC và TD theo lô khác nhau vì ô không Markov (notebook §9.2).
- Chỉ nêu số chạy kèm điều kiện "theo output của bài thực hành" và phiên bản gói, vì các số phụ thuộc phiên bản gymnasium.

**Tình huống áp dụng**
- **05.1 (gắn bài thực hành):** dự đoán giá trị của chính sách heuristic với $\varepsilon=0.1$ trên Lunar Lander.
  - Mô hình hóa: ô, $\gamma=0.99$, kết thúc và cắt ngắn.
  - Kiểm giả thiết: Markov trên ô không thỏa; lượt bị cắt ngắn không phải kết thúc thật.
  - Áp dụng: 05.11, 05.16, 05.27–05.29.
  - Diễn giải: so sánh $J$ của hai nghiệm; giới hạn.
- **05.2 (giả thiết không thỏa):** coi bước 1000 là trạng thái kết thúc, tức đặt giá trị tiếp nối bằng 0.
  - Hậu quả cho mục tiêu MC và TD (notebook ô 39, lời giải).
  - Dẫn ngược 05.2, 05.17.
- Tùy chọn **05.3:** HW05 bài 4, lượt dài thưởng thưa (dãy bảy ô), chọn phương pháp.

**Danh mục ứng dụng.** Mục tiêu MC và TD dùng lại ở Bài 06 (MC điều khiển; mục tiêu Sarsa $R+\gamma Q(S',A')$; ghi chú Bài 06 đã có). Các mục Bài 07 (TD với xấp xỉ hàm) và Bài 08 (mục tiêu bootstrap, mạng mục tiêu, bộ nhớ phát lại) cần xác minh nội dung trước khi dẫn.

**Đoạn kết mục.** Viết bằng văn xuôi cho cả 4 mục.

**Tóm tắt chương**
- Đoạn văn 5–8 câu.
- Định nghĩa và kết quả theo mục.
- Công thức cần nhớ: $G_t$ truy hồi; trung bình gia tăng; bước hằng; TD(0); độ chệch; bất đẳng thức phương sai; điều kiện Robbins–Monro; $V=\hat r+\gamma\hat PV$.
- Giả thiết hay bị bỏ quên: cắt ngắn không phải kết thúc; trạng thái Markov; $\pi$ cố định và dữ liệu theo $\pi$; bước học giảm; $V$ cố định khi nói về mục tiêu; đọc bảng trước khi ghi.

**Bài tập củng cố ba mức**
- **Nhận biết:** bài (a)(b)(c) ở dòng 638; chọn lịch bước học thỏa Robbins–Monro ($1/n$, $1/\sqrt n$, $0.1$, $1/n^2$).
- **Tính toán hoặc chứng minh:** chứng minh 05.9 bằng quy nạp; tính độ chệch mục tiêu TD với bảng MC sau $e_1$.
- **Vận dụng:** bài ở dòng 606; tự chuyển trên Lunar Lander.
- Phủ đủ MT1–MT6; không trùng với `exercises.md`.

**Độ dài.** Hiện khoảng 9 700 token theo `wc -w` (có LaTeX), tức chưa tới 8 000 từ văn xuôi. Đích là 15 000–18 000. Để so sánh, ghi chú mẫu Bài 07 của math-4-AI có khoảng 35 000 token.

### B5. Giáo trình cần đối chiếu cho từng mục

| Mục | Nguồn |
|---|---|
| Mở đầu, 1.1 | Sutton và Barto (2018) §5 (đoạn mở), §6.1; giáo trình *Học máy thống kê* `sec_q_learning.tex` (mở mục bằng giới hạn của quy hoạch động; thuật ngữ, giọng kể) |
| 1.2 Lượt và lợi tức | Sutton và Barto §3.3 (lượt, $G_t$), §5.1 |
| 1.3–1.4 Lần ghé, ước lượng MC | Sutton và Barto §5.1 tr. 92–93 (lần ghé đầu tiên và mọi lần ghé, sơ đồ dự phòng); Bertsekas và Tsitsiklis (1996) *Neuro-Dynamic Programming* ch. 5 (Monte Carlo trên bảng tra) |
| 1.5–1.6 Trung bình gia tăng, bước hằng | Sutton và Barto §2.4 tr. 30–31, §2.5 tr. 32–33 (điều kiện (2.7)) |
| 1.7 Thuật toán MC | Sutton và Barto §5.1 (khung giả mã); Szepesvári (2010) *Algorithms for RL* §2.1 (MC mọi lần ghé, phát biểu gọn) |
| 1.8 Hội tụ MC | Sutton và Barto §5.1; Singh và Sutton (1996) cho mọi lần ghé (cần xác minh trang) |
| 2.1–2.3 TD(0) | Sutton và Barto §6.1 tr. 119–121 (giả mã TD(0), sơ đồ dự phòng); Szepesvári §2.1.1; *Học máy thống kê* (cập nhật kinh nghiệm với bước học, thuật ngữ) |
| 3.1–3.4 Độ chệch, phương sai | Sutton và Barto §6.2 tr. 124 (ưu điểm của TD), §6.1 (sai số TD và sai số Bellman); luật phương sai toàn phần (giáo trình xác suất có trang) |
| 3.5 Hội tụ TD(0) | Sutton và Barto §6.2 tr. 124–125 và các nguồn sách dẫn (Dayan 1992; Jaakkola, Jordan và Singh 1994; Tsitsiklis 1994; cần xác minh); Bertsekas và Tsitsiklis (1996) ch. 4–5 (xấp xỉ ngẫu nhiên) |
| 4 Cập nhật theo lô | Sutton và Barto §6.3 tr. 126–128 (Ví dụ 6.4, ước lượng tương đương chắc chắn); *Học máy thống kê* "Học mô hình quá trình quyết định Markov" (mô hình thực nghiệm) |
| Tình huống áp dụng | Notebook; Sutton và Barto §3.4 (kết thúc so với cắt ngắn); Bài 04 (dạng ma trận) |

Puterman và Bertsekas (2019) chỉ cần cho phương trình Bellman nếu Bài 04 chưa có số hiệu. Mọi mục đã tham khảo phải ghi vào `review-log.md`.

### B6. Bảng ký hiệu đề xuất và các chỗ lệch

**Bảng ký hiệu đề xuất**

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$ | trạng thái không kết thúc | tập hữu hạn |
| $\mathcal S^+$ | $\mathcal S$ cùng các trạng thái kết thúc | tập hữu hạn |
| $\mathcal A(s)$ | hành động hợp lệ tại $s$ | tập hữu hạn |
| $\pi(a\mid s)$ | chính sách đang đánh giá | phân phối trên $\mathcal A(s)$; Markov, cố định |
| $S_t,A_t,R_{t+1}$ | trạng thái, hành động, thưởng của chuyển $t\to t+1$ | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathbb R$ bị chặn |
| $t$; $T$ | thời điểm; thời điểm kết thúc lượt | $\mathbb N$; hữu hạn hầu chắc chắn |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; $\gamma=1$ chỉ khi kết thúc hợp lệ |
| $G_t$ | lợi tức (return) | biến ngẫu nhiên thực; $G_T=0$ |
| $v_\pi(s)$ | giá trị thật | $\mathbb R$; bằng 0 tại trạng thái kết thúc |
| $V$; $V_t$ | bảng ước lượng; bảng trước cập nhật tại bước $t$ | $\mathbb R^{\mathcal S^+}$ |
| $\mathbb E_\pi[\cdot\mid S_t=s]$ | kỳ vọng theo $\pi$ và động lực môi trường | — |
| $g_i(s)$ | mẫu lợi tức thứ $i$ được chọn tại $s$ | $\mathbb R$ |
| $N(s)$, $n$ | bộ đếm mẫu hoặc cập nhật của riêng $s$ | $\mathbb N$ |
| $\alpha$, $\alpha_n(s)$ | bước học | $(0,1]$ |
| $Y_t$ | mục tiêu TD | $\mathbb R$ |
| $\delta_t$ | sai số TD | $\mathbb R$ |
| $Y^*$ | mục tiêu lý tưởng dùng $v_\pi$ | $\mathbb R$ |
| $T_\pi$ | toán tử Bellman kỳ vọng (Bài 04) | $\mathbb R^{\mathcal S}\to\mathbb R^{\mathcal S}$ |
| $M$, $B$ | ngân sách lượt (MC) và ngân sách chuyển (TD) | $\mathbb N$ |
| $\mathcal D$; $k$, $K$, $V_k$ | tập dữ liệu cố định; lượt quét, ngân sách quét, bảng đầu lượt quét | — |
| $\hat r,\hat P$ | thưởng và xác suất chuyển thực nghiệm | — |

Sau bảng nêu tương ứng với *Học máy thống kê* ($V^\pi$; $T(s,a,s')$, $R(s,a,s')$).

**Các chỗ lệch giữa deck, ghi chú và notebook**
1. **Dấu thập phân.**
   - Dấu chấm: deck 05 (204 lần), ghi chú 05 (100 lần), deck và ghi chú 06.
   - Dấu phẩy `{,}`: notebook 05, deck và ghi chú Bài 04, bộ mẫu math-4-AI.
   - Cần người dùng chọn.
2. **$\varepsilon$ có hai nghĩa.** Notebook dùng $\varepsilon=0{,}1$ cho chính sách và cùng chữ cho ngưỡng dừng theo lô (deck D09, ghi chú 548). Đề xuất đổi tên ngưỡng.
3. **$\Delta$ có hai nghĩa.** Bài 04 dùng $\Delta_\pi(V)$ cho phần dư Bellman; Bài 05 dùng $\Delta_k(s)$ cho tổng gia số theo lô.
   - Ghi chú dòng 439 gọi $(T_\pi V)-V$ là "sai số Bellman kỳ vọng", trong khi Bài 04 gọi là "phần dư Bellman".
   - Đề xuất đổi tên ký hiệu gia số và thống nhất thuật ngữ.
4. **Tên trạng thái trùng biến ngẫu nhiên:** $S$ so với $S_t$, $S(s)$. Đề xuất viết chữ đứng (A5).
5. **$\mathcal S$ được định nghĩa hai lần:** A04 và ghi chú dòng 18 viết "hữu hạn"; B01 và dòng 79 giới hạn là "không kết thúc". Cần định nghĩa một lần.
6. **$c$ có nhiều nghĩa trong notebook:** ô, điểm cắt $c_{j,k}$, chi phí nhiên liệu $c(A_k)$. Ghi chú dùng $c_1..c_5$ cho dãy năm ô. Chỉ cần ghi trong notebook.
7. **Bước học theo lô.** Ghi chú và deck dùng $\alpha=1/8$ hằng; notebook dùng $\alpha/N(s)$ với $\alpha=1$. Cần nêu quan hệ.
8. **Notebook vi phạm giả thiết Markov.** Deck và ghi chú giả thiết trạng thái Markov; notebook dùng ô gộp không Markov. Cần nói thẳng trong Tình huống 05.1.
9. **Notebook dẫn ghi chú theo tên mục** ("mục Thuật toán TD(0) và các trường hợp biên", "mục Độ chệch…", "mục Phương sai…", "quy trình sáu bước"). Sau khi đánh số lại phải sửa các ô Markdown này.
10. **Khuôn bảng TD không thống nhất** giữa C07 và C08 (A3).

---

## C. Bài tập (`exercises.md` mới)

| Số hiệu | Mạch | Mức | Đối tượng / dữ kiện tóm tắt | Trùng trang chiếu hay mới | Năng lực đo |
|---|---|---|---|---|---|
| 05.1 (giữ số của ghi chú) | 2 | nhận biết | Mẫu $(s,a,0,s')$ trên dãy ô; thông tin còn thiếu để dùng quy hoạch động (HW05 bài 2) | trùng ghi chú; câu hỏi gốc của A05 (đã gộp) | Phân biệt mẫu, mô hình, giá trị |
| 05.4 (giữ) | 2 | tính toán | Lợi tức tại $X$ theo hai quy tắc trên $e_1,e_2$; $\alpha=0.5$ | trùng L05-B13 và B13b | Chọn mẫu, trọng số |
| 05.23 | 2 | tính toán | Lượt mới $S\to X\to S\to X\to S\to L$, $\gamma=0.9$: tính $G_t$ ngược, hai tập mẫu, hai trung bình | mới | Lợi tức chiết khấu, chọn lần ghé |
| 05.24 | 2 | chứng minh | Khai triển bước hằng; tổng trọng số $1-(1-\alpha)^n$; bốn cấu hình (HW05 bài 5, đã hiệu chỉnh tiền đề) | mới | Chứng minh, tách hai trục |
| 05.7 (giữ) | 3 | tính toán | Hai chuyển từ bảng $(0.25,0.5,0)$ | trùng L05-C10 và C10b | Mục tiêu, sai số, trạng thái kết thúc |
| 05.25 | 3 | tính toán | HW05 bài 7: MC (hai quy tắc) và TD(0) trên $e_1,e_2$, $\alpha=0.5$ | mới; kết quả khớp B11, C07, C08 | Thứ tự đọc–ghi, chạy từng phương pháp |
| 05.26 | 3 | vận dụng [Lập trình] | Notebook §7: ô tự chuyển, $V^*=r/(1-\gamma)$; đo tỉ lệ tự chuyển; so $1/n$ với $\alpha$ hằng | mới, gắn notebook | Giải thích thông tin lan chậm |
| 05.27 | 4 | tính toán | HW05 bài 6: giá trị chuẩn dãy năm ô, $\gamma=0.9$ (nghiệm khoảng $2.659$, $4.417$, $6.639$, $9.228$); rồi độ chệch mục tiêu TD tại $c_3$ với một bảng cho trước | mới | Bellman kỳ vọng, công thức độ chệch |
| 05.28 | 4 | chứng minh | Bất đẳng thức phương sai bằng luật phương sai toàn phần; phản ví dụ $V(X)=10$ trên dãy bốn ô ($19.36>0.726$) | mới | Chứng minh, vai trò giả thiết |
| 05.29 | 4 | vận dụng | HW05 bài 4: lượt dài, thưởng thưa, hành động nhiễu; Lunar Lander với $\gamma=0.99$ ($1/(1-\gamma)=100$ bước, thưởng ±100 ở cuối) | mới | Phân tích độ chệch và phương sai có điều kiện |
| 05.30 | 5 | tính toán | Ba lượt $A\xrightarrow1B\xrightarrow0$ kết thúc, $B\xrightarrow1$ kết thúc (hai lần), $\gamma=1$. Dự kiến MC cho $(1,2/3)$, TD cho $(5/3,2/3)$; cần tính lại | mới | Hai tiêu chuẩn theo lô |
| 05.31 | 5 | vận dụng [Lập trình] | Notebook §9.2 và nhiệm vụ 1: đổi cách chia ô, so $J$ của MC và TD theo lô | mới, gắn notebook | Đánh giá giả thiết Markov trên ô |

Tùy chọn 05.32 "dãy bốn ô, lượt thứ ba", trùng L05-E06 và E06b.

- **Phủ mạch:** mạch 2 có 4 bài, mạch 3 có 3, mạch 4 có 3, mạch 5 có 2.
- **Vận dụng:** 3 bài (05.26, 05.29, 05.31).
- **Đoạn mở của tệp** nêu: bài nào giữ số của ghi chú, bài nào chỉ có trong tệp này, bài nào trùng trang chiếu.
- **Bảng `Mạch | Mở phần | Bài tập`** trỏ `lecture-05-du-doan-phi-mo-hinh.html#/N/1`.

---

## D. Rủi ro, thứ tự thực hiện và câu hỏi cho người dùng

**Thứ tự thực hiện**
1. **Đồng bộ kế hoạch trước** (một tác tử ghi): ghi bổ sung `bc95338` vào `review-log.md`; sửa thứ tự D03, D04, D05 và bảng phương sai trong outline và storyboard; bỏ câu "không tạo notebook"; thêm nhóm "Bài tập: Chưa có" vào `index.html` nếu người dùng đồng ý.
2. **Giai đoạn I, ghi chú:** dựng lại theo mẫu (B1–B6), đánh số môi trường, đổi giọng kể, thêm "Trong thực hành" và tình huống áp dụng.
   - Năm vai rà soát; tác tử rà toán tính lại toàn bộ số liệu (kể cả 05.30 và E06).
   - Kiểm viewer; commit `fix(materials-05)`.
3. **Giai đoạn II, deck:** trang tiêu đề mạch, mạch mở đầu và kết luận, các phép tách theo A3, khuôn bảng cố định, xóa CSS thu chữ, ghi chú diễn giả dẫn "(Định lý 05.k)".
   - Storyboard ghi số âm tiết trước và sau cho 22 trang vượt trần.
   - Rà lại; kiểm trình duyệt ở 1600×900 và 390×844 trên cổng 8766.
4. **Giai đoạn III, bài tập:** `exercises.md`; cập nhật E03, ghi chú, index; sửa các tham chiếu tên mục trong ô Markdown của notebook (không cần chạy lại mã).

**Rủi ro**
- Số trang tăng từ 45 lên khoảng 69 trong cùng 120 phút; cần bảng phút mới.
- Đổi `id` hoặc thứ tự phá liên kết `#/N/M`. Giữ mọi mã cũ cho phần đầu của trang tách và dùng hậu tố b, c.
- Số chạy của notebook phụ thuộc phiên bản gói.
- Các định lý hội tụ dẫn nguồn ngoài cần trang chính xác.
- Ghi chú các bài 03, 04, 06 chưa có số hiệu môi trường, nên mục "Kiến thức tiên quyết" tạm dẫn theo mục kèm phát biểu lại.

**Câu hỏi cho người dùng**
1. Dùng 6 mạch hay 7 mạch? Có chấp nhận mã `L05-DT` cho trang tiêu đề mạch 5 không?
2. Dấu thập phân cho toàn học phần: phẩy hay chấm?
3. Có viết tên ô bằng chữ đứng không?
4. Có bỏ liên kết tới PDF nguồn không được theo dõi (HW05, bài giảng gốc) và thay bằng `exercises.md` không?
5. Có cho phép đặt câu chuyện "tàu đổ bộ thu nhỏ" cho dãy bốn ô và dùng ô tự chuyển Lunar Lander ở C06b không?
6. Có thêm ngay nhóm "Bài tập: Chưa có" vào index không?
7. Chọn ký hiệu thay $\Delta_k$ và ngưỡng $\varepsilon$ như thế nào?

Không cần ngoại lệ raster: mọi hình hiện là SVG, và hình cấu trúc chương có thể dùng lại `learning-route.svg`. Hai tệp SVG chưa dùng ở đâu: `design-grid.svg` và `mc-td-timeline.svg`. Cần quyết định giữ hay bỏ.
