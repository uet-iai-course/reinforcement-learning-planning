# Kế hoạch sửa Bài 06 theo chuẩn 2026-10-12

Phạm vi: kiểm toán chỉ đọc. Các tệp đã đọc gồm deck `2627-1/lecture-06-dieu-khien-phi-mo-hinh.html` (45 trang, 7 mạch A–G), ghi chú `2627-1/materials/lec-06/lecture-note.md` (1 015 dòng, khoảng 10 800 từ văn xuôi khi bỏ công thức và URL), các ô Markdown và kết quả in ra của notebook `thuc-hanh-lunarlander-dieu-khien-phi-mo-hinh.ipynb`, cùng `planning/lec-06/{outline,storyboard,review-log,analysis}.md`. Tôi đã đối chiếu với `AGENTS.md` (các mục được giao), `CLAUDE.md`, hai mẫu `_templates/` và bộ sản phẩm mẫu `math-4-AI/.../lec-07`. Mật độ đo bằng `density.py`. Lưu ý: script đếm cả ô số và nhãn cột của bảng và đếm mỗi hàng bảng là một dòng, nên ở các trang có bảng con số thật thấp hơn. Mọi kết luận "vượt trần" bên dưới vẫn đúng sau khi trừ phần ấy, trừ khi có ghi chú khác. Không có tệp nào bị sửa và không có commit.

Ba phát hiện nền tảng ảnh hưởng đến toàn bộ kế hoạch:
1. **Bài 03–05 đã định nghĩa** $q_\pi$, $v_\pi=\sum_a\pi q_\pi$, định lý cải thiện chính sách tham lam và chứng minh (deck 04: "Hàm giá trị hành động", "Cải thiện chính sách tham lam", "Chứng minh định lý cải thiện"), lần ghé đầu và mọi lần ghé, trung bình gia tăng, khung $V\leftarrow V+\alpha[\text{mục tiêu}-V]$, và điều kiện Robbins–Monro theo trạng thái (deck 05, "Trung bình gia tăng", "Điều kiện hội tụ của TD(0)"). Bài 06 hiện trình bày lại các nội dung này như khái niệm mới (B02, C03, F03; ghi chú §2.2, §3.3, §6.3). Theo chuẩn mới, các nội dung này phải chuyển thành "Nhắc lại:" kèm phát biểu lại. Đóng góp mới của Bài 06 nằm ở ba chỗ: ước lượng $Q$ theo cặp, cải thiện trong lớp $\varepsilon$-mềm (mở rộng định lý của Bài 04), và Robbins–Monro theo cặp cùng GLIE (mở rộng điều kiện của TD(0)).
2. **Ghi chú các bài 02–05 chưa có số hiệu** (0 khối được đánh số). Vì vậy "Kiến thức tiên quyết" của Bài 06 chưa dẫn được dạng `(Định lý 05.k)`.
3. **Notebook dẫn tới số mục của ghi chú hiện tại** (mục 2.1, 2.3, 2.5, 4.4, 4.5, 5.3, 5.4, 5.6, 6.1–6.5). Khi ghi chú đổi số mục, các tham chiếu này hỏng.

---

## A. Deck

### A1. Mạch hiện tại → đề xuất

Giữ **7 mạch** (nằm trong khoảng 5–7), không gộp hay tách mạch. Mạch mở đầu được tái cấu trúc. Các mạch 2–7 mỗi mạch thêm một trang tiêu đề mạch. Hiện chưa có mã `<tiền tố>00` nào, nên dùng `L06-B00` … `L06-G00`. Lớp `strand-title` đã có trong `lecture-slide.css` (dòng 122–175), nên không cần sửa CSS.

| N | Mạch hiện tại | Tên mạch đề xuất | Dòng dẫn (≤ 25 âm tiết) | Từ khóa (≤ 5) | Mã trang tiêu đề | id |
|---|---|---|---|---|---|---|
| 1 | A. Bài toán điều khiển | Mở đầu (trang bìa L06-A01 là trang tiêu đề, không thêm trang "Mở đầu") | — | — | L06-A01 | `mach-1` (tùy chọn, đặt trên A01) |
| 2 | B. Giá trị hành động và thăm dò | Giá trị hành động và thăm dò | "Muốn so sánh hai hành động tại D khi thiếu mô hình, phải ước lượng giá trị từng cặp và thử cả hai." (23) | Giá trị hành động · Chính sách ε-tham lam · Chính sách ε-mềm · Cải thiện chính sách · Thăm dò | L06-B00 | `mach-2` |
| 3 | C. Điều khiển Monte Carlo | Điều khiển Monte Carlo | "Muốn ước lượng giá trị cặp từ lượt hoàn chỉnh, phải gắn lợi tức với lần ghé đầu của cặp." (20) | Lần ghé đầu · Lợi tức của cặp · Trung bình gia tăng · Chính sách cố định trong lượt | L06-C00 | `mach-3` |
| 4 | D. Sarsa | Sarsa và mục tiêu một bước | "Muốn cập nhật trước khi lượt kết thúc, phải thay lợi tức chưa quan sát bằng giá trị của hành động kế tiếp." (22) | Mục tiêu một bước · Bộ năm $(S,A,R,S',A')$ · Học theo chính sách · Trạng thái kết thúc · Ngân sách | L06-D00 | `mach-4` |
| 5 | E. Q-learning | Q-learning và học khác chính sách | "Muốn học giá trị của chính sách tham lam khi hành vi còn thăm dò, phải tách chính sách hành vi khỏi chính sách đích." (25) | Chính sách hành vi · Chính sách đích · Mục tiêu cực đại · Học khác chính sách | L06-E00 | `mach-5` |
| 6 | F. Điều kiện bảo đảm | Điều kiện hội tụ | "Muốn kết luận bảng hội tụ tới $q_*$, phải kiểm độ phủ, lịch thăm dò và lịch bước học theo cặp." (20) | Độ phủ · GLIE · Robbins–Monro · Hội tụ gần chắc chắn | L06-F00 | `mach-6` |
| 7 | G. Tổng hợp và kết luận | Tổng kết và chuyển tiếp | "Muốn chọn MC, Sarsa hay Q-learning, phải đối chiếu dữ liệu có được, mục tiêu cập nhật và giả thiết hội tụ." (21) | Giả thiết không được bỏ · Khung cập nhật chung · Câu hỏi tự kiểm tra · Xấp xỉ hàm | L06-G00 | `mach-7` |

Tên mạch không được trùng tiêu đề trang nội dung đầu tiên. Hai mạch cần sửa: mạch 3 trùng với C01 "Điều khiển Monte Carlo", nên đổi tiêu đề C01. Mạch 4 có trang đầu D01 mang tiêu đề "Từ … sang …" bị cấm, nên đổi tiêu đề D01. Ghi chú diễn giả của mỗi trang tiêu đề mạch dài 40–100 âm tiết và nêu ba ý: kết quả kế thừa, nhiệm vụ của mạch, đầu ra cho mạch sau. Storyboard ghi các trang này là "điểm vào mạch N". Các trang B00–F00 có dòng dẫn trùng nhu cầu của khái niệm đầu tiên trong mạch nên được ghi là bước `vấn đề`. G00 ghi "ngoài hành trình khái niệm". Mọi trang mới mang `data-note-topic-id` của mạch tương ứng.

### A2. Mạch mở đầu và mạch kết luận

**Đối chiếu mạch mở đầu:**

| Yêu cầu | Hiện trạng | Đề xuất |
|---|---|---|
| Bìa có câu luận đề, đơn vị | A01 thiếu câu luận đề và đơn vị. Liên kết "Ghi chú bài giảng và bài tập" trỏ tới một tài liệu bài tập chưa có. | **Sửa A01.** Thêm câu luận đề: "Mục tiêu cập nhật quyết định giá trị được học: lợi tức của lượt, hành động kế tiếp đã chọn hoặc cực đại của bảng." Đơn vị: cần hỏi người dùng (outline cấm gán đơn vị chưa xác minh). Liên kết đổi thành "Ghi chú bài giảng · Bài tập" sau khi `exercises.md` đạt kiểm định. |
| Trang "Tiên quyết và quy ước" | Chưa có. Tiên quyết nằm ở dòng cuối A04 với nhãn "Tiên quyết:" không thuộc danh sách nhãn cho phép. Các ký hiệu $\mathcal S,\mathcal S^+,\mathcal A(s)$ chỉ có trong ghi chú diễn giả A03. | **Thêm L06-A07.** Dòng "**Nhắc lại:** $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ và $v_\pi=\sum_a\pi q_\pi$ (Bài 03); cải thiện tham lam theo $q_\pi$ (Bài 04); MC dự đoán và TD(0) có dạng $V\leftarrow V+\alpha[\text{mục tiêu}-V]$ (Bài 05)." Dòng "**Ký hiệu:** $\mathcal S$ là tập trạng thái không kết thúc, $\mathcal S^+$ thêm trạng thái kết thúc, $\mathcal A(s)$ hữu hạn, $\pi(a\mid s)$, $R_{t+1}$ là thưởng sau $A_t$, $T$ là thời điểm kết thúc, $\mathbb E_\pi$ lấy theo chính sách và động lực." |
| Mục tiêu đánh giá được | Nằm trong A02 (3 mục, gộp với mục lục, 11 dòng). Ghi chú có 5 mục tiêu, outline có 7. | **Tách A02 → "Mục tiêu học tập".** Năm mục tiêu thống nhất giữa deck, ghi chú, storyboard và Bài tập củng cố: (1) phân biệt $q_\pi$, $Q$, $q_*$ và thông tin có trong một mẫu; (2) tính phân phối $\varepsilon$-tham lam, kể cả khi đồng hạng; (3) thực hiện MC lần ghé đầu theo cặp; (4) thực hiện Sarsa và Q-learning, xử lý trạng thái kết thúc, phân biệt chính sách hành vi với chính sách đích; (5) kiểm giả thiết hội tụ và phân biệt chúng với việc dừng theo ngân sách. Trần 80 âm tiết. |
| Trang "Nội dung" | Mục lục 7 mục trong A02 không đánh số "Mở đầu" và tên lệch tên mạch. | **Thêm L06-A08 "Nội dung".** Danh sách 1–7 trùng đúng tên ở A1. Thêm dòng đọc trước: "Sutton và Barto (2018), §§5.3–5.4, §§6.4–6.5". |
| "Vấn đề trung tâm" | Box ở A03 ("Học giá trị của hai hành động tại D…") và A04 đảm nhận một phần, chưa có câu trả lời theo mạch. | **Sửa A03 thành "Vấn đề trung tâm"** và giữ hình `chain-five-states.svg`. Box: "Chọn hành động tại D của dãy năm ô khi không biết mô hình." Năm dòng trả lời có điều kiện, mỗi mạch 2–6 một dòng: (2) cần $Q$ theo cặp và xác suất thử dương; (3) có lượt kết thúc thì dùng trung bình lợi tức của lần ghé đầu; (4) chưa kết thúc thì dùng $R+\gamma Q(S',A')$; (5) hành vi thăm dò, đích tham lam thì dùng $R+\gamma\max_aQ(S',a)$; (6) hữu hạn, $\gamma<1$, độ phủ, Robbins–Monro theo cặp (thêm GLIE với Sarsa) thì $Q_t\to q_*$. Chuyển các chi tiết $\mathcal S$, kết thúc, $\gamma=1$ sang A07 hoặc ghi chú. |
| Khung chung | D01 nêu dạng $Q\leftarrow Q+\alpha[\text{mục tiêu}-Q]$, nhưng ở giữa bài. | **Thêm L06-A09 "Khung chung của quy tắc cập nhật"** (3–4 dòng): Nhắc lại khung của Bài 05; $Q(S_t,A_t)\leftarrow Q(S_t,A_t)+\alpha[Y-Q(S_t,A_t)]$; "Ba phương pháp của bài khác nhau ở dữ liệu tạo $Y$ và thời điểm cập nhật." Chưa nêu ba dạng $Y$ để không mở thuật toán bằng công thức. |
| A04, A05 | A04 có tiêu đề "Từ dự đoán đến điều khiển" (bị cấm), 3 khung, 73 âm tiết. A05 là câu hỏi nằm trong mạch mở đầu. | **Bỏ A04**: phần nhắc lại sang A07, phân biệt dự đoán/điều khiển sang ghi chú diễn giả B00. **Chuyển A05** sang mạch 2 làm trang vấn đề kèm ví dụ dẫn nhập (xem A3). |

**Mạch kết luận** (thứ tự theo AGENTS): G00 → G05 → G01 → G06 → G03 + G07 → G02 → G08 → G04.

- **G05 (thêm) "Tổng kết".** Bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`. Nếu vượt 80 âm tiết thì tách hai trang.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Giá trị hành động của $\pi$ | hành động đầu cố định; lợi tức khả tích | $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ |
| Chính sách $\varepsilon$-tham lam | tập cực đại; chia đều khi đồng hạng | $\pi_\varepsilon(a\mid s)=\varepsilon/m(s)+(1-\varepsilon)\mathbf1\{a\in\mathcal G_Q\}/|\mathcal G_Q|$ |
| Cải thiện $\varepsilon$-tham lam (Mệnh đề 06.8) | $q_\pi$ chính xác; cùng $\varepsilon$; $\gamma<1$ | $\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$ |
| MC lần ghé đầu | lượt hoàn chỉnh; $N_0=0$; chính sách cố định trong lượt | $Q\leftarrow Q+(G_{f(s,a)}-Q)/N$ |
| Sarsa | $A'$ lấy trước cập nhật; $Y=R$ khi kết thúc | $Y=R+\gamma Q(S',A')$ |
| Q-learning | cực đại trên bảng trước cập nhật; $Y=R$ khi kết thúc | $Y=R+\gamma\max_aQ(S',a)$ |

- **G01 (sửa) "Khung chung của ba phương pháp".** Bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng`:
  - MC: $Q\leftarrow Q+(G_t-Q)/N$ sau lượt; dữ liệu là lượt hoàn chỉnh; dừng sau $K$ lượt.
  - Sarsa: $Q\leftarrow Q+\alpha[R+\gamma Q(S',A')-Q]$; dữ liệu là bộ năm; dừng sau $H$ cập nhật.
  - Q-learning: $Q\leftarrow Q+\alpha[R+\gamma\max_aQ(S',a)-Q]$; dữ liệu là bộ bốn; dừng sau $H$ cập nhật.
  - Ghi chú diễn giả nêu: ngân sách là điểm dừng thực hành, không phải tiêu chuẩn hội tụ.
- **G06 (thêm) "Điều kiện hội tụ của ba phương pháp".** Bảng `Phương pháp | Giả thiết không được bỏ | Kết luận`:
  - Sarsa: MDP hữu hạn, thưởng chặn, $\gamma<1$, mọi cặp cập nhật vô hạn, Robbins–Monro theo cặp, GLIE → $Q_t\to q_*$ gần chắc chắn (Định lý 06.25).
  - Q-learning: như Sarsa nhưng thay GLIE bằng "hành vi duy trì độ phủ" → $Q_t\to q_*$ (Định lý 06.24).
  - MC điều khiển: lượt kết thúc, chính sách cố định trong lượt → mỗi ô là trung bình các lợi tức đã chọn. Bài không phát biểu định lý hội tụ tới $q_*$ (nguồn tr. 26 nêu, nhưng không chứng minh trong bài).
- **G03 (sửa) "Bài tập: chọn phương pháp cho tàu đổ bộ"** và **G07 (thêm) cùng tiêu đề, nhãn "Lời giải:"** trên mặt trang. Đây là bài tập tổng hợp trên một bài toán Học tăng cường cụ thể: lượt LunarLander dài tới 1000 bước và bị cắt ngắn, hành vi $\varepsilon=0{,}05$, bốn hành động, lưới 2187 ô. Câu hỏi: chọn MC, Sarsa hay Q-learning; xác định mục tiêu tại bước cắt ngắn; chỉ ra hai giả thiết hội tụ bị vi phạm (quan sát gộp không Markov; sàn bước học $\alpha_{\min}=0{,}05$). Lời giải dùng đúng kết quả của notebook §10.
- **G02 (sửa) "Trả lời vấn đề trung tâm".** Kết luận có điều kiện: các bảng sau dữ liệu hữu hạn cho quyết định hiện thời (MC: trái; Sarsa và Q-learning: phải). Chỉ khi thêm các giả thiết của G06 thì $Q_t\to q_*$ và chính sách tham lam theo $Q$ mới tối ưu. Dòng "Nguồn:" tổng hợp: Tạ Việt Cường tr. 15–30; Sutton và Barto (2018) §§5.3–5.4, 6.4–6.5; Singh và cộng sự (2000); Watkins và Dayan (1992).
- **G08 (thêm) "Câu hỏi tự kiểm tra".** Mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng." Bốn câu: (1) Sarsa với $\varepsilon=0{,}25$ cố định có thỏa Định lý 06.25 không; (2) mục tiêu Sarsa và Q-learning khi $S'$ là trạng thái kết thúc; (3) lượt bị cắt ở bước 1000 có cho MC lợi tức hoàn chỉnh không; (4) Q-learning với hành vi đều có cần tỉ số lấy mẫu quan trọng không.
- **G04 (sửa) "Bài tập về nhà và tài liệu đọc".** Bảng `Mạch | Bài tập` lấy theo `exercises.md`. Dòng "Tài liệu đọc:" ghi Sutton và Barto (2018) §§5.3–5.4, §§6.4–6.5; Singh và cộng sự (2000) §2–3. Dòng "Ghi chú bài giảng · Bài tập" trỏ tới viewer. Dòng nối sang Bài 07: "Bảng không tổng quát hóa giữa các trạng thái; Bài 07 thay bảng bằng xấp xỉ hàm." Câu này chuyển từ caption G01. **Bỏ hai liên kết `../RL-hk2-2025-2026/*.pdf`**: tệp nguồn không được theo dõi, nằm ngoài `2627-1/`, và hỏng khi phát hành.

### A3. Bảng từng trang (45/45 trang)

Ký hiệu cột "âm tiết" lấy theo script, trần 60 (80 với trang mục tiêu, nội dung, tổng kết và bảng so sánh). Chú thích: "Câu hỏi→Bài tập" nghĩa là đổi tiêu đề sang "Bài tập: <chủ đề>", thêm dòng "Gợi ý:" và câu nêu năng lực được đo vào ghi chú diễn giả. Hiện **không trang câu hỏi nào có "Gợi ý:"** và **không cụm nào có lời giải trên mặt trang**.

| Mã | Âm tiết | Vấn đề theo chuẩn mới | Quyết định | Đề xuất cụ thể |
|---|---:|---|---|---|
| A01 | 32 | Thiếu câu luận đề và đơn vị; ghi chú diễn giả mở bằng "Bài học xét…" (tài liệu làm chủ ngữ); liên kết bài tập chưa có. | sửa | Theo A2. Ghi chú diễn giả mở bằng đối tượng ("Điều khiển phi mô hình học bảng giá trị hành động…"). |
| A02 | 74 | 11 dòng; 2 chức năng trên một trang; mục lục không khớp tên mạch; chỉ 3 mục tiêu. | tách | Thành "Mục tiêu học tập" (A02) và "Nội dung" (L06-A08 mới), mỗi trang ≤ 6 dòng. |
| A04 | 73 | Tiêu đề "Từ…đến…"; 10 dòng; dòng 24 âm tiết; 3 khung; nhãn "Tiên quyết:" ngoài danh sách. | bỏ (gộp) | Nội dung nhắc lại sang A07; phân biệt dự đoán/điều khiển sang ghi chú diễn giả B00 và ghi chú bài giảng. |
| A03 | 45 | Tên ví dụ là "chuỗi năm trạng thái" (nên gọi theo đối tượng); box là vấn đề trung tâm nhưng chưa có câu trả lời theo mạch. | sửa | Thành "Vấn đề trung tâm" (A2). Tên ví dụ thống nhất là "dãy năm ô A–E". |
| A05 | 40 | Câu hỏi đặt trong mạch mở đầu; tiêu đề "Kiểm tra…" không có tiền tố; lời giải chỉ trong ghi chú diễn giả. | sửa (chuyển sang mạch 2) | Thành trang vấn đề đầu mạch 2 "Thông tin trong một mẫu chuyển": "**Nhu cầu:** so sánh hai hành động tại D từ dữ liệu", ví dụ dẫn nhập $(D,1,10,E)$ và kết luận "mẫu không chứa dữ liệu về $(D,0)$". Giữ một dòng "Câu hỏi:" ngắn. |
| B01 | 90 | Dòng 32 âm tiết; 10 dòng; 2 khung (card và box); dùng $v(s')$ không chỉ số và chưa nhắc lại; trộn vấn đề, ví dụ và kết luận. | tách | Câu vấn đề sang trang A05 đã chuyển. B01 thành "Ví dụ: bảng khởi tạo nghiêng phải trên dãy năm ô" (bảng I, hai ô tại D, "Diễn giải: số khởi tạo chưa là quan sát"). Đích ≤ 40 âm tiết. |
| B08 *(mới)* | — | Ví dụ $\pi_L$ (998 và 10) hiện đứng sau định nghĩa ở B02 và trong ghi chú diễn giả B01, sai thứ tự "ví dụ trước hình thức". | thêm | "Ví dụ: chính sách luôn đi trái trên dãy năm ô". Dữ kiện, yêu cầu "Tính $G$ khi hành động đầu là 0 hoặc 1", hai dòng tính, "Diễn giải:" hành động đầu cố định và chính sách tiếp nối. Đây là bước trực giác và ví dụ trước B02. |
| B02 | 39 | Trình bày như định nghĩa mới dù $q_\pi$ đã có ở Bài 03; dùng dấu ":" thay động từ ("$Q$: bảng ước lượng"); thiếu nhãn; ghi chú diễn giả 213 âm tiết (nhẹ). | sửa | "**Nhắc lại:** $G_t$, $q_\pi$ (Bài 03)", rồi "**Định nghĩa.** $Q$ là bảng ước lượng…; giá trị hành động tối ưu $q_*(s,a)$ là $\max_\pi q_\pi(s,a)$". Bỏ dòng $\pi_L$ (đã sang B08). |
| B03 | 47 | Dòng trong box 30 âm tiết; chưa mở bằng "Nhu cầu:". | sửa | "**Nhu cầu:** ô chưa được thử không nhận mẫu." Tách box thành hai câu ≤ 20 âm tiết; câu "998 > 10" giữ làm kết luận có số. |
| B04 | 30 | 2 khung (hai card); thiếu tiền tố "Ví dụ:". | sửa | "Ví dụ: xác suất chọn hành động tại D". Bỏ card, thay bằng hai dòng "Khai thác…" và "Thăm dò…". |
| B05 | 34 | Thiếu nhãn "Định nghĩa."; hai định nghĩa trên một trang ($\varepsilon$-tham lam và $\varepsilon$-mềm, trong box). | sửa | Thêm "**Định nghĩa.**" cho cả hai, viết bằng "là/gọi là". Nếu vượt 6 dòng thì đưa $\varepsilon$-mềm thành dòng "**Định nghĩa.**" thứ hai ngoài box. |
| B06 | 61 | Vượt 60; dòng 25 âm tiết; thiếu "Mệnh đề.", "Giả thiết:", "Kết luận:"; chứng minh dài chỉ có trong ghi chú diễn giả; chưa nêu quan hệ với định lý cải thiện của Bài 04. | tách | B06 giữ "**Mệnh đề.** Giả thiết / Kết luận / **Ý nghĩa:** mở rộng cải thiện tham lam (Bài 04) sang lớp ε-mềm (Mệnh đề 06.8)", ≤ 40 âm tiết. Thêm **B09 "Chứng minh: cải thiện chính sách ε-tham lam"** gồm trọng số $w$, chuỗi `aligned`, và một dòng "toán tử đơn điệu và co". Phép kiểm số $q=(3,3,-1)$ giữ trong ghi chú diễn giả. |
| B07 | 59 | Dòng 21 âm tiết; tiêu đề "Kiểm tra…"; không có Lời giải trên mặt trang (cụm 2 cần ít nhất một). | sửa + thêm | Câu hỏi→Bài tập "Bài tập: chính sách ε-tham lam trên dãy năm ô". Thêm **B10** cùng tiêu đề, "**Lời giải:**" mỗi dòng một bước: $(1/8,7/8)$; $(1/2,1/2)$; $q_\pi(D,0)$ cố định hành động đầu; bảng khởi tạo chưa là $q_\pi$ nên Mệnh đề 06.8 chưa áp dụng. |
| C01 | 50 | Tiêu đề trùng tên mạch; dòng 33 âm tiết; chuỗi mũi tên trong box; câu "của trang Nhu cầu thăm dò" là tham chiếu nội bộ; hình trùng B03. | sửa | Đổi tiêu đề thành "Lợi tức của cặp trạng thái–hành động". "**Nhu cầu:** so sánh hành động cần lợi tức gắn với cặp." Thêm một dòng nêu MC điều khiển là học theo chính sách vì chính sách sinh lượt cũng là chính sách được đánh giá. Bỏ chuỗi mũi tên; cân nhắc bỏ hình lặp. |
| C02 | 27 | Thiếu tiền tố "Ví dụ:". | sửa | "Ví dụ: một lượt tham lam trên dãy năm ô". |
| C03 | 36 | Định nghĩa lần ghé đầu viết bằng dấu ":"; $N$ được giải thích sau công thức; trung bình gia tăng là nội dung của Bài 05. | sửa | "**Nhắc lại:** trung bình gia tăng $1/N$ (Bài 05)". "**Định nghĩa.** Lần ghé đầu của cặp $(s,a)$ là thời điểm nhỏ nhất…". Đặt dòng $N$ trước công thức. |
| C04 | 63 | Vượt 60; 9 dòng; bộ sinh số chiếm 4 dòng; tiêu đề thiếu tiền tố. | sửa | "Ví dụ: lượt thăm dò trên dãy năm ô". Ghi trực tiếp dãy $u=(4/5,3/5,1/5,2/5)$; công thức đồng dư $x_j$ chuyển sang ghi chú diễn giả và ghi chú bài giảng. Bảng II đổi tên theo đối tượng ("bảng khởi tạo nghiêng trái"). Đích ≤ 45 âm tiết. |
| C07 | 34 | Hàng bảng làm script báo 7 dòng (thực tế khoảng 3 dòng chữ); thiếu tiền tố. | sửa (tiêu đề) | "Ví dụ: lượt thăm dò trên dãy năm ô, cập nhật lần ghé đầu". |
| C05 | 86 | Vượt 60 (dưới 1,5 lần trần); dòng 23 âm tiết; thiếu nhãn "Thuật toán.". | sửa | "**Thuật toán.**", "**Đầu vào:**" rút gọn, "**Đầu ra:**", "**Giả thiết:** lượt kết thúc gần chắc chắn". Ví dụ $\varepsilon_k=1/k$ sang ghi chú diễn giả. Đích ≤ 55 âm tiết, giả mã ≤ 8 dòng. |
| C06 | 55 | Gần trần; dòng chi phí. | giữ (sửa nhẹ) | Dòng chi phí $O(M+T)$ và $O(T)$ gộp một dòng; thêm dòng dừng "$K$ là ngân sách, không phải tiêu chuẩn hội tụ". |
| C08 | 34 | Tiêu đề "Kiểm tra…"; "(quy tắc của Bài 05)" chưa phát biểu lại; không có lời giải trên mặt trang. | sửa + thêm | Câu hỏi→Bài tập "Bài tập: lần ghé đầu trên lượt có cặp lặp". "**Nhắc lại:** mọi lần ghé dùng mọi lợi tức của cặp." Thêm **C09** "**Lời giải:**": lợi tức 996, 997, 998, 999, 1000; $(D,0)$ tại $t=0,2$; lần ghé đầu cho 996 với $N=1$; mọi lần ghé cho 997 với $N=2$. |
| D01 | 62 | Tiêu đề "Từ…sang…" bị cấm; 3 khung; câu box định nghĩa tên Sarsa; dòng 21 âm tiết. | sửa | Đổi tiêu đề thành "Mục tiêu một bước cho giá trị hành động". "**Nhu cầu:** tiền tố D→C chưa có lợi tức" và "**Nhắc lại:** TD(0) dùng $R+\gamma V(S')$". Bỏ hai card và box; tên Sarsa chuyển sang D04. |
| D02 | 105 | **Vượt 1,5 lần trần (nghiêm trọng)**; 13 dòng; caption 40 âm tiết; hai bảng. | tách/sửa | "Ví dụ: năm mẫu chuyển trên dãy năm ô" chỉ giữ bảng mẫu. Bảng khởi tạo viết lại một dòng "B $(0,1)$, C $(1,0)$, D $(0,1)$". Caption sang ghi chú diễn giả. Đích ≤ 40 âm tiết chữ. |
| D03 | 20 | Thiếu tiền tố. | sửa (tiêu đề) | "Ví dụ: năm mẫu chuyển, hai cập nhật Sarsa đầu". |
| D04 | 36 | Dòng 21 âm tiết; "học theo chính sách" xuất hiện lần đầu không kèm "(on-policy)"; thiếu nhãn. | sửa | "**Định nghĩa.** Mục tiêu Sarsa $Y_t$ là…". Câu cuối tách đôi và thêm "(on-policy)" ở lần xuất hiện đầu. |
| D05 | 91 | **Vượt 1,5 lần trần (nghiêm trọng)**; dòng 23 âm tiết. | tách | Thành "Thuật toán Sarsa: đầu vào và khởi tạo" (D05) và "Thuật toán Sarsa: một bước cập nhật" (**D10** mới), mỗi trang ≤ 45 âm tiết. Chi tiết chọn bước học $\alpha_{n+1}$ sang ghi chú diễn giả. |
| D06 | 85 | Vượt 60; box và dòng chi phí. | sửa | Giữ các bước 4–6 và một dòng "**Lưu ý:** kết thúc lượt khác dừng thuật toán". Chi phí sang G01 hoặc ghi chú diễn giả. Đích ≤ 50. |
| D07 | 54 | Hai h3 và box làm thành 8 dòng; thiếu tiền tố. | sửa | "Ví dụ: năm mẫu chuyển, mẫu vào trạng thái kết thúc". Box sang ghi chú diễn giả. |
| D08 | 51 | Tiêu đề "Kiểm tra…"; không có lời giải trên mặt trang. | sửa + thêm | "Bài tập: cập nhật Sarsa từ mẫu thứ năm". **D11** "**Lời giải:**" $Y=-1{,}6$; $\delta=-1{,}6$; $Q(D,0)=-1{,}28$; $A'$ lấy trước cập nhật và giữ để thực hiện. |
| E01 | 66 | Vượt 60; dòng 33 âm tiết; định nghĩa viết "$b=\pi$: học theo chính sách"; câu "như … ở các phần trước" là lời chỉ đường. | tách | E01 "Mục tiêu Sarsa phụ thuộc hành động thăm dò": "**Nhu cầu:**" và hình. **E09 (mới)** "Chính sách hành vi và chính sách đích": "**Định nghĩa.** Học theo chính sách (on-policy) là trường hợp $b$ trùng $\pi$; học khác chính sách (off-policy) là $b\ne\pi$." Dẫn MC/Sarsa bằng số hiệu. |
| E02 | 12 | Thiếu tiền tố. | sửa (tiêu đề) | "Ví dụ: năm mẫu chuyển, một cập nhật Q-learning". |
| E03 | 24 | Thiếu nhãn. | giữ (sửa nhẹ) | Thêm "**Định nghĩa.**" cho mục tiêu $Y_t$. |
| E04 | 88 | Vượt 60; dòng 31 âm tiết. | tách | Thành E04 "Thuật toán Q-learning: đầu vào và khởi tạo" và **E10** "Thuật toán Q-learning: một bước cập nhật", mỗi trang ≤ 45 âm tiết. |
| E05 | 69 | Vượt 60; 2 khung (hai card). | sửa | Giữ các bước 4–6. Hai card chi phí sang G01 hoặc ghi chú diễn giả. Đích ≤ 45. |
| E06 | 47 | Bảng so sánh (trần 80, đạt); thiếu tiền tố. | giữ (sửa tiêu đề) | "Ví dụ: năm mẫu chuyển, Sarsa và Q-learning". |
| E11 *(mới, khuyến nghị)* | — | Chưa có cầu nối tới bài thực hành. | thêm | "Ví dụ: một chuyển của tàu đổ bộ" với dữ kiện notebook §6–7: $\gamma=0{,}99$, $\alpha=0{,}1$, $Q(S,A)=3$, $R=-1{,}5$, hàng $Q(S',\cdot)=(2;5;5;1)$, $A'=0$. Sarsa cho $Y=0{,}48$ và $Q=2{,}748$; Q-learning cho $Y=3{,}45$ và $Q=3{,}045$. |
| E07 | 40 | Dòng 30 âm tiết trong box; nhãn "Điều kiện:" ngoài danh sách; hình lặp E01; ghi chú diễn giả 161 âm tiết. | sửa | Đổi sang "**Giả thiết:**". Tách box thành hai câu. Phần lấy mẫu quan trọng trong ghi chú diễn giả rút gọn và dẫn tới mục đọc thêm. |
| E08 | 44 | Dòng 22 âm tiết; tiêu đề "Kiểm tra…"; không có lời giải trên mặt trang. | sửa + thêm | "Bài tập: mục tiêu Sarsa và Q-learning trên cùng chuyển". **E12** "**Lời giải:**" $0$ và $799$; hai mục tiêu trùng khi và chỉ khi $A'\in\mathcal G_Q(S')$. |
| F01 | 70 | Vượt 60; 2 khung (card và box); câu đầu chỉ chuyển ý. | sửa | "**Giả thiết:**" thành danh sách 3–4 dòng; "**Lưu ý:** dãy năm ô ($\gamma=1$, $\alpha=0{,}8$) nằm ngoài miền này." Bỏ card. Đích ≤ 45. |
| F02 | 71 | Vượt 60; dòng 40 âm tiết; 2 khung; ví dụ và định nghĩa trên cùng trang. | tách | **F06 (mới)** "Ví dụ: khối xác suất tham lam khi ε giảm": $7/8$ với $\varepsilon=1/4$, tiến tới 1 khi $\varepsilon_k=1/k$, kèm "Diễn giải:" giảm $\varepsilon$ chưa bảo đảm thăm vô hạn. F02 "**Định nghĩa.** GLIE" với hai điều kiện, không dùng card. |
| F03 | 40 | 3 khung; ví dụ $1/n$ và $0{,}8$ đứng sau định nghĩa; Robbins–Monro theo trạng thái đã có ở Bài 05 nhưng chưa nhắc lại. | tách/sửa | **F07 (mới)** "Ví dụ: ba lịch bước học của một cặp" ($1/n$; $0{,}8$; $1/t$ toàn cục với $t_n=2^n$). F03 "**Nhắc lại:** Robbins–Monro theo trạng thái (Bài 05)" và "**Định nghĩa.** điều kiện theo cặp". |
| F04 | 99 | **Vượt 1,5 lần trần (nghiêm trọng)**; dòng 28 âm tiết; "Bài trình bày…" lấy tài liệu làm chủ ngữ; ghi "nguồn tr. 26" trên mặt trang; ghi chú diễn giả 240 âm tiết. | tách | F04 "**Định lý.** Hội tụ của Q-learning" (Giả thiết / Kết luận / "**Ý nghĩa:**" / "(Định lý 06.24)"). **F08 (mới)** "**Định lý.** Hội tụ của Sarsa" (thêm GLIE, "(Định lý 06.25)"). Câu về MC sang G06 và ghi chú diễn giả. Nêu "Chứng minh nằm ngoài phạm vi" kèm nguồn trong ghi chú diễn giả. |
| F05 | 84 | Vượt 60; dòng 26 âm tiết; tiêu đề "Kiểm tra…". | sửa + thêm | "Bài tập: kiểm giả thiết hội tụ". Dòng giả thiết rút còn "Giả thiết của Định lý 06.24–06.25, $\gamma=0{,}9$". Bảng 3 trường hợp giữ nguyên. **F09** "**Lời giải:**" a đủ điều kiện; b thiếu điều kiện tham lam trong giới hạn ($7/8$); c vi phạm tổng bình phương. |
| G01 | 81 | Vượt trần tổng kết 80; dòng 22 âm tiết; chưa đúng khuôn bảng của AGENTS. | sửa | Thành bảng khung chung `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng` (A2). |
| G02 | 63 | Dòng 22 âm tiết; chưa là trang trả lời vấn đề trung tâm; thiếu "Nguồn:". | sửa | Theo A2, giữ bảng ba hàng D. |
| G03 | 80 | Vượt 60 (không phải bảng); tiêu đề "Kiểm tra…"; là bài tập tổng hợp nhưng chưa có bài toán Học tăng cường cụ thể và lời giải trên mặt trang. | sửa + thêm | Theo A2 (G03 và G07, dữ kiện LunarLander). |
| G04 | 72 | Vượt 60; liên kết tới nguồn ngoài `2627-1/`; "Bài 10 trong hw3.pdf" là mã; 2 khung. | sửa | Theo A2. Bài hw3 trở thành Bài tập 06.13 "dãy sáu ô A–F" trong `exercises.md`. |

Những trang được thêm và không có trong bảng trên: A07, A08, A09, B00, C00, D00, E00, F00, G00, G05, G06, G08. Deck dự kiến có khoảng 70–71 trang. Phân bổ thời gian: mở đầu 8, mạch 2 20, mạch 3 20, mạch 4 20, mạch 5 21, mạch 6 17, mạch 7 14, tổng 120 phút; mỗi trang tiêu đề mạch khoảng 0,5 phút.

Các vấn đề chung cả deck:
- **Thuật ngữ tiếng Anh thiếu ở lần đầu:** lợi tức (return), thăm dò (exploration), khai thác (exploitation), tham lam (greedy), ε-mềm (ε-soft), lần ghé đầu (first-visit), mọi lần ghé (every-visit), bước học (step size), mục tiêu cập nhật (update target), chính sách hành vi (behavior policy), chính sách đích (target policy), giá trị hành động (action value).
- **Ghi chú diễn giả dài hơn 150 âm tiết** (mức nhẹ): B01, B02, C05, C06, D05, D06, E07, F01, F02, F03, F04, G01, G02, G03, G04.
- **CSS cục bộ** (dòng 9–29) tham chiếu mã cũ (A02, B01, D02, G01 …). Cần dọn sau khi tách trang.
- **Storyboard** phải ghi số âm tiết trước và sau của 21 trang vượt trần, kèm quyết định `tách` hoặc `sửa`.
- **outline.md** chưa có cột tiếng Anh trong bảng thuật ngữ, trong khi AGENTS yêu cầu bảng Việt–Anh.

### A4. Cụm khái niệm và sáu bước

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Bước thiếu, lỗi thứ tự |
|---|---|---|---|---|---|---|---|
| Giá trị hành động $Q$ và $q_\pi$ | A05→B01 | chỉ trong ghi chú diễn giả B01 | $\pi_L$ ở dòng cuối B02, **sau** định nghĩa | B02 | B03 | B07(2) | Trực giác chưa có trên mặt trang; ví dụ đặt sau định nghĩa. Thêm B08. B02 phải chuyển thành Nhắc lại. Thiếu lời giải trên mặt trang. |
| $\varepsilon$-tham lam | B03 | B04 | B04 | B05 | B06, C04 | B07(1) | Đủ sáu bước; thiếu lời giải trên mặt trang. |
| Cải thiện $\varepsilon$-tham lam | B03 (gián tiếp) | không có | chỉ trong ghi chú diễn giả ($q=(3,3,-1)$) | B06 | B07(3) | B07 | Thiếu trực giác và ví dụ trên mặt trang; chứng minh chưa tách trang. Chưa móc nối với định lý cải thiện của Bài 04. |
| MC điều khiển (thuật toán) | C01 | C01 hình | **tính tay** C02, C04, C07 trước giả mã C05–C06 ✓ | C03, C05, C06 | C07 (đứng trước thuật toán), G02 | C08 | Ứng dụng sau quy trình đầy đủ còn yếu. Vai "theo chính sách" chỉ có trong ghi chú diễn giả C01. Không có bảo đảm hội tụ trong bài, cần ghi rõ ở G06. |
| Sarsa (thuật toán) | D01 | D01 card | **tính tay** D02–D03 trước D04–D06 ✓ | D04, D05, D06 | D07, E06 | D08 | Đủ bước; on-policy nêu ở D04 nhưng thiếu thuật ngữ Anh. Hành vi bằng đích ✓. |
| Q-learning (thuật toán) | E01 | E01 hình | **tính tay** E02 trước E03–E05 ✓ | E03, E04, E05 | E06, E07 (thêm E11) | E08 | Đủ bước; hành vi $b$ và đích tham lam ✓ (E01, E07). Hành vi sinh dữ liệu và đích dùng trong mục tiêu được nêu ở E04 và E07 ✓. |
| GLIE | F01 | không có | F02 dòng 2, cùng trang với định nghĩa | F02 | F04 | F05 | Thiếu trực giác; ví dụ chung trang với định nghĩa. Tách F06. |
| Robbins–Monro theo cặp | F01 | chỉ trong ghi chú diễn giả | F03 card, **sau** định nghĩa | F03 | F04 | F05 | Sai thứ tự; chưa nhắc lại Bài 05. Tách F07. |
| Định lý hội tụ | F01 | không có | không có trước định lý | F04 | F05, G03 | F05 | Thiếu trực giác (xấp xỉ ngẫu nhiên kết hợp ánh xạ co, một dòng trong ghi chú diễn giả); trường hợp áp dụng nên dùng LunarLander (G03). |

### A5. Ví dụ xuyên suốt

- **Hiện có:** chuỗi A–E (nguồn tr. 15); bảng I và bảng II; chính sách $\pi_L$; dãy số $x_j,u_j$; lượt D–C–B–A; năm mẫu chuyển; lượt D–C–D–C–B–A (C08); bài A–F của hw3 (G04, ghi chú §7.4).
- **Tên đề xuất theo đối tượng:** "dãy năm ô A–E"; "bảng khởi tạo nghiêng phải" (bảng I, D ưu tiên phải); "bảng khởi tạo nghiêng trái" (bảng II); "chính sách luôn đi trái"; "năm mẫu chuyển chung"; "dãy sáu ô A–F". Không dùng "Bài 10 trong hw3.pdf" trên mặt trang.
- **Nối với LunarLander.** Dãy năm ô không phải phiên bản thu nhỏ của LunarLander. Vì nguồn có thứ tự ưu tiên cao hơn, giữ dãy năm ô làm ví dụ chính và thêm ba cầu nối:
  1. E11 dùng chuyển tính tay của notebook §6–7.
  2. Ví dụ $\varepsilon$-tham lam bốn hành động $(1;3;3;0)$ với $\varepsilon=0{,}2$ cho $(0{,}05;0{,}45;0{,}45;0{,}05)$, đặt trong ghi chú bài giảng hoặc bài tập.
  3. Song song giữa "mẫu 5 dừng ở C chưa kết thúc" và "cắt ngắn ở 1000 bước vẫn bootstrap" (notebook §6).

  Notebook **không có MC điều khiển**. Với MC, phần "Trong thực hành" chỉ nối định tính: lượt dài 267–773 bước và lượt bị cắt ngắn làm thiếu lợi tức hoàn chỉnh.

---

## B. Ghi chú bài giảng

### B1. Đối chiếu từng mục

Trong bảng: "TP" là thành phần trong cấu trúc 11 phần; "mạch" là mạch của deck mới.

| Mục hiện có (dòng) | Mạch | Vai trò theo 11 TP | Vấn đề | Kế hoạch |
|---|---|---|---|---|
| `# Bài 06. Điều khiển phi mô hình` (1) | — | TP1 | Sai khuôn "Bài 06 — …". | Đổi thành `# Bài 06 — Điều khiển phi mô hình`. |
| Đoạn 3–5 | — | TP2 | Dòng 3 là câu mảnh siêu dữ liệu. | Giữ một đoạn ngắn và bỏ dòng 3. |
| `## 1.` Bài toán điều khiển từ kinh nghiệm (8) | 1→2 | Đang chứa TP3, TP4 và mở chương | Mục tiêu (16–22) và tiên quyết (14) nằm lẫn trong §1.1; chưa có TP5 và TP6. | Tách `## Mục tiêu học tập`, `## Kiến thức tiên quyết`, `## Bảng ký hiệu`, `## Bản đồ chủ đề`. Phần còn lại thành đoạn mở của `## 1. Giá trị hành động và thăm dò`. |
| §1.1 Từ dự đoán đến điều khiển (10) | 2 | TP4 / mở §1 | Tiêu đề "Từ…đến…"; đoạn 14 chứa 4 ý; tài liệu làm chủ ngữ ("Bài học xét"). | Chuyển sang TP4 (Nhắc lại Bài 03–05) và đoạn mở §1 (kết quả bài trước, bài toán tại D, việc chương làm, hình cấu trúc chương). |
| §1.2 Chuỗi năm trạng thái (24) | 2 | TP7, ví dụ | Chưa là khối `example`; mở bằng "Xét…" mà chưa nêu nhu cầu. | Ví dụ 06.1 (dãy năm ô), có đoạn đọc hình. |
| §1.3 Kiểm tra thông tin trong một mẫu (42) | 2 | TP7, bài tập | Khối `exercise` chưa đánh số; có tiêu đề "Câu hỏi:". | Bài tập 06.1. |
| `## 2.` Giá trị hành động và thăm dò (61) | 2 | TP7 | Không có đoạn mở mục; kết mục chỉ là dòng "Nguồn:" (233). | Gộp vào `## 1.`; thêm đoạn kết mục. |
| §2.1 Giá trị hành động (63) | 2 | vấn đề + ví dụ | $v(s')$ và $p(s',r\mid s,a)$ chưa giới thiệu; bảng I chưa nằm trong khối. | Vấn đề và Ví dụ 06.2 (bảng khởi tạo nghiêng phải). |
| §2.2 Giá trị hành động của một chính sách (77) | 2 | hình thức | Định nghĩa viết lẫn trong văn (87–92); "Do đó" (96) thiếu căn cứ; ví dụ $\pi_L$ (102) đặt sau. | Ví dụ 06.3 ($\pi_L$) đưa lên trước. Nhắc lại $q_\pi$ (Bài 03) trong văn. Định nghĩa 06.1 ($Q$, $q_*$). Nhận xét 06.2 (vòng B–C). |
| §2.3 Nhu cầu thăm dò (114) | 2 | vấn đề | Đạt; hình 118 thiếu đoạn đọc hình đầy đủ. | Giữ, thêm đoạn đọc hình. |
| §2.4 Xác suất chọn hành động tại D (122) | 2 | ví dụ | Chưa thành khối. | Ví dụ 06.4. |
| §2.5 Chính sách ε-tham lam (134) | 2 | hình thức | Hai định nghĩa viết lẫn trong văn (142–158). | Định nghĩa 06.3 và Định nghĩa 06.4, mỗi định nghĩa kèm đoạn móc nối. |
| §2.6 Cải thiện chính sách ε-tham lam (162) | 2 | kết quả | Phát biểu viết bằng văn (164–168), không có khối `proposition`; chứng minh không chia bước và không kết thúc bằng $\square$; chưa móc nối với Bài 04. | Bổ đề 06.5, Mệnh đề 06.6, Nhận xét 06.7, theo B2. |
| §2.7 Kiểm tra chính sách ε-tham lam (212) | 2 | bài tập | Chưa đánh số. | Bài tập 06.2. |
| `## 3.` Điều khiển Monte Carlo (236) | 3 | TP7 | Không có đoạn mở và đoạn kết. | `## 2.` |
| §3.1 Vòng điều khiển Monte Carlo (238) | 3 | vấn đề + trực giác | Một đoạn; thiếu "Một cách trực quan…" và câu "chưa phải định nghĩa". | Viết lại theo mẫu. |
| §3.2 Monte Carlo với chính sách tham lam (242) | 3 | ví dụ | Chưa thành khối. | Ví dụ 06.5. |
| §3.3 Cập nhật Monte Carlo theo lần ghé đầu (252) | 3 | hình thức | Trùng nội dung Bài 05; chuỗi ba dấu bằng trên một dòng (277–279). | Nhắc lại Bài 05; Định nghĩa 06.8 (lần ghé đầu theo cặp); `derivation` chuyển thành nhắc lại kèm `aligned`. |
| §3.4 Lấy mẫu ε-tham lam bằng dãy số cho trước (285) | 3 | ví dụ | Chưa thành khối. | Ví dụ 06.6. |
| §3.5 Cập nhật từ lượt D–C–B–A (311) | 3 | ví dụ | Hình 313 thiếu đoạn đọc; chưa nêu lại bảng II trong khối. | Ví dụ 06.7. |
| §3.6 Thuật toán điều khiển Monte Carlo (325) | 3 | thuật toán | Là danh sách thường, chưa là khối `algorithm`. | Thuật toán 06.9; Nhận xét 06.10 (chi phí, ngân sách, tiền tố). Thêm "Trong thực hành". |
| §3.7 Kiểm tra lần ghé đầu của cặp (339) | 3 | bài tập | "quy tắc của Bài 05" chưa phát biểu lại (342). | Bài tập 06.3. |
| `## 4.` Sarsa: cập nhật theo hành động kế tiếp (358) | 4 | TP7 | Không có đoạn kết mục. | `## 3.` |
| §4.1 Từ Monte Carlo sang cập nhật một bước (360) | 4 | vấn đề | Tiêu đề bị cấm. | Đổi thành "Mục tiêu một bước cho giá trị hành động"; Nhắc lại TD(0). |
| §4.2 Năm mẫu chuyển dùng chung (364) | 4 | dữ kiện | Chưa thành khối. | Khối "Dữ kiện" đặt trong Ví dụ 06.8. |
| §4.3 Hai cập nhật Sarsa đầu tiên (388) | 4 | ví dụ | Hình 398 đặt sau phép tính. | Ví dụ 06.8. |
| §4.4 Quy tắc cập nhật Sarsa (402) | 4 | hình thức | Mở bằng ký hiệu; công thức không có câu đọc. | Định nghĩa 06.11 và đoạn đọc. |
| §4.5 Thuật toán Sarsa (429) | 4 | thuật toán | Chưa là khối `algorithm`. | Thuật toán 06.12; Nhận xét 06.13 (kết thúc lượt, cắt ngắn, ngân sách). |
| §4.6 Sarsa tại trạng thái kết thúc (443) | 4 | ứng dụng | Đạt về số liệu. | Ví dụ 06.9. |
| §4.7 Kiểm tra cập nhật Sarsa từ tiền tố (470) | 4 | bài tập | — | Bài tập 06.4. |
| `## 5.` Q-learning: tách hành vi và mục tiêu (493) | 5 | TP7 | Không có đoạn kết mục. | `## 4.` |
| §5.1 Chính sách hành vi và chính sách đích (495) | 5 | vấn đề + định nghĩa | Định nghĩa viết lẫn trong văn (499); hình 501 thiếu đoạn đọc. | Định nghĩa 06.14 và đoạn móc nối với MC, Sarsa. |
| §5.2 Một cập nhật Q-learning (503) | 5 | ví dụ | "Đặt lại bảng I" nhưng không nêu lại bảng. | Ví dụ 06.10, có đoạn "Dữ kiện". |
| §5.3 Quy tắc cập nhật Q-learning (516) | 5 | hình thức | "Sau đó dùng" là câu dẫn rỗng. | Định nghĩa 06.15. |
| §5.4 Thuật toán Q-learning (540) | 5 | thuật toán | Chưa là khối `algorithm`. | Thuật toán 06.16 và "Trong thực hành" (LunarLander). |
| §5.5 Sarsa và Q-learning trên cùng năm mẫu (552) | 5 | ứng dụng | "đã công bố ở phần Sarsa" (554), không nêu lại dữ kiện. | Ví dụ 06.11, nêu lại đủ năm mẫu. |
| §5.6 Dữ liệu hành vi trong Q-learning (584) | 5 | nhận xét | Đoạn 586 có 6 câu và nhiều ý. | Nhận xét 06.17, chia thành ba đoạn. |
| §5.7 Kiểm tra mục tiêu Sarsa và Q-learning (592) | 5 | bài tập | — | Bài tập 06.5. |
| `## 6.` Điều kiện hội tụ (620) | 6 | TP7 | Không có đoạn kết mục. | `## 5.` |
| §6.1 Giả thiết chung của các định lý hội tụ (622) | 6 | vấn đề | Đạt một phần. | Giữ; Nhận xét 06.18 (dãy năm ô ngoài miền). |
| §6.2 Điều kiện GLIE (630) | 6 | ví dụ + định nghĩa | Định nghĩa viết lẫn trong văn. | Ví dụ 06.12; Định nghĩa 06.19. |
| §6.3 Điều kiện Robbins–Monro (654) | 6 | định nghĩa + ví dụ | Định nghĩa đặt **trước** ví dụ; chưa nhắc lại Bài 05. | Ví dụ 06.13 (ba lịch) đưa lên trước; Định nghĩa 06.20. |
| §6.4 Hội tụ của Sarsa và Q-learning (680) | 6 | định lý | Không có khối `theorem` và không có bốn phần; thiếu danh sách "Bỏ <giả thiết>: phản ví dụ". | Định lý 06.21, Định lý 06.22, Nhận xét 06.23 (MC). |
| §6.5 Kiểm tra giả thiết hội tụ (698) | 6 | bài tập | — | Bài tập 06.6. |
| `## 7.` Tổng hợp, bài tập và đọc thêm (727) | 7 | trộn TP8–TP11 | Không có TP8, TP9, TP10. | Tách thành các mục chuẩn (dưới đây). |
| §7.1 Tổng kết ba phương pháp (729) | 7 | TP9 | Bảng đã có. | Chuyển vào "Tóm tắt chương"; thêm đoạn 5–8 câu, "Công thức cần nhớ", "Giả thiết hay bị bỏ quên". |
| §7.2 Quyết định tại D sau các cập nhật (743) | 7 | đóng vấn đề | — | Đoạn cuối §5 hoặc đoạn mở "Tóm tắt chương". |
| §7.3 Kiểm tra lựa chọn phương pháp (756) | 7 | bài tập | — | Bài tập củng cố mức vận dụng hoặc chuyển sang `exercises.md` (trùng G03). |
| §7.4 Bài 10 trong bộ bài tập (778) | 3, 5 | bài tập | Tài liệu làm chủ ngữ ("Bài tập này dùng"). | Chuyển sang `exercises.md` thành Bài tập 06.13. |
| §7.5 Đọc thêm: dự đoán TD(0) khác chính sách (864) | đọc thêm | — | "Phần này xét" (866); chứng minh không chia bước, không có $\square$. | `## 6. Đọc thêm: dự đoán khác chính sách và sai số đánh giá`, nhóm `đọc thêm`, không có mạch deck tương ứng (ghi lý do trong review-log). |
| §7.6 Đọc thêm: sai số đánh giá một chính sách cố định (948) | đọc thêm | — | "Trong mục này" (956). | Trong `## 6.` |
| §7.7 Tài liệu học tiếp (1011) | 7 | TP11 | Thiếu tác giả, năm, trang và ánh xạ mục→nguồn; liên kết tới PDF không được theo dõi. | `## Hướng dẫn đọc thêm và tài liệu tham khảo`. |
| — | — | TP5, TP6, TP8, TP10 | Chưa có. | Thêm mới. |

Thứ tự đích: tiêu đề → giới thiệu → Mục tiêu → Tiên quyết → Bảng ký hiệu → Bản đồ chủ đề → `## 1.`–`## 5.` (mạch 2–6) → `## 6.` Đọc thêm → Tình huống áp dụng và ứng dụng → Tóm tắt chương → Bài tập củng cố → Hướng dẫn đọc thêm. Giữ `note-topic-id` `lec-06-topic-01`…`07`. Đề xuất ánh xạ: topic-01 cho phần mở đầu và đoạn mở §1, topic-02 đến 06 cho §1–§5, topic-07 cho phần tổng kết, đọc thêm và bài tập, để mọi `data-note-topic-id` của deck vẫn còn hợp lệ.

### B2. Kế hoạch đánh số môi trường

Bộ đếm chung (Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán):

| Số | Khối `:::` | Nội dung | Nguồn hiện tại |
|---|---|---|---|
| 06.1 | definition | Bảng ước lượng $Q$; giá trị hành động tối ưu $q_*$ ($q_\pi$ là nhắc lại Bài 03) | 2.2 (100) |
| 06.2 | remark | Vòng B–C với $\gamma=1$: lợi tức không khả tích | 2.2 (109) |
| 06.3 | definition | Chính sách $\varepsilon$-tham lam, tập cực đại, quy ước đồng hạng | 2.5 |
| 06.4 | definition | Chính sách $\varepsilon$-mềm | 2.5 (153) |
| 06.5 | lemma | Toán tử $T^{\pi}$ đơn điệu và co (nhắc lại Bài 04, có chứng minh ngắn) | 2.6 (190–205) |
| 06.6 | proposition | Cải thiện chính sách $\varepsilon$-tham lam. Chứng minh 4 bước: trọng số $w$; bất đẳng thức một bước; đơn điệu; co và giới hạn; thêm trường hợp $\varepsilon=1$ | 2.6 |
| 06.7 | remark | Giới hạn: $Q$ từ mẫu; lớp mềm; quan hệ với định lý Bài 04 | 2.6 (210) |
| 06.8 | definition | Lần ghé đầu của cặp | 3.3 |
| 06.9 | algorithm | Điều khiển MC theo chính sách, lần ghé đầu | 3.6 |
| 06.10 | remark | Chi phí $O(M+T)$; ngân sách $K$; tiền tố bị cắt | 3.6 (335–337) |
| 06.11 | definition | Mục tiêu và sai lệch Sarsa | 4.4 |
| 06.12 | algorithm | Sarsa | 4.5 |
| 06.13 | remark | Kết thúc lượt, cắt ngắn do môi trường và hết ngân sách là ba sự kiện khác nhau | 4.4–4.5 |
| 06.14 | definition | Chính sách hành vi, chính sách đích; học theo / khác chính sách | 5.1 |
| 06.15 | definition | Mục tiêu Q-learning | 5.3 |
| 06.16 | algorithm | Q-learning | 5.4 |
| 06.17 | remark | Không cần tỉ số lấy mẫu quan trọng; độ phủ; phát lại tập mẫu hữu hạn | 5.6 |
| 06.18 | remark | Giả thiết nền; dãy năm ô nằm ngoài miền | 6.1 |
| 06.19 | definition | GLIE | 6.2 |
| 06.20 | definition | Robbins–Monro theo cặp | 6.3 |
| 06.21 | theorem | Hội tụ của Q-learning dạng bảng (Watkins–Dayan) | 6.4 |
| 06.22 | theorem | Hội tụ của Sarsa dạng bảng với GLIE (Singh và cộng sự) | 6.4 |
| 06.23 | remark | MC điều khiển: nguồn tr. 26; Tsitsiklis (2002) | 6.4 (696) |
| 06.24 | definition | Tỉ số lấy mẫu quan trọng và điều kiện hỗ trợ (đọc thêm) | 7.5 |
| 06.25 | proposition | Kỳ vọng có điều kiện của gia số TD(0) khác chính sách | 7.5 proof |
| 06.26 | proposition | Chặn Hoeffding cho đánh giá chính sách cố định | 7.6 |
| 06.27 | remark | Độ rộng $B$; không áp dụng được cho $\gamma=1$ | 7.6 (996–1007) |

Lưu ý về số hiệu ở A2, A3 và C: các số hiệu ghi trong A2, A3 là số hiệu tạm. Theo bảng B2 cuối cùng, hai định lý hội tụ là **06.21 (Q-learning)** và **06.22 (Sarsa)**, mệnh đề cải thiện là **06.6**. Tác tử soạn phải đồng bộ lại các số này trên deck sau khi ghi chú được chốt.

Bộ đếm Ví dụ (06.1–06.13):
- 06.1 dãy năm ô
- 06.2 bảng khởi tạo nghiêng phải
- 06.3 chính sách luôn đi trái
- 06.4 xác suất tại D
- 06.5 lượt tham lam D→E
- 06.6 lượt thăm dò bằng dãy số cho trước
- 06.7 cập nhật lượt D–C–B–A
- 06.8 năm mẫu chuyển, hai cập nhật Sarsa đầu
- 06.9 Sarsa trên năm mẫu
- 06.10 một cập nhật Q-learning
- 06.11 Sarsa và Q-learning trên năm mẫu
- 06.12 khối xác suất tham lam khi $\varepsilon$ giảm
- 06.13 ba lịch bước học, gồm trường hợp $t_n=2^n$

Thêm 06.14 "một chuyển của tàu đổ bộ" nếu dùng E11.

Bộ đếm Bài tập: 06.1–06.6 là bài trong các mục (trùng trang chiếu); 06.7–06.12 là Bài tập củng cố; 06.13 trở đi thuộc `exercises.md`. Khối `application`: Tình huống 06.1 và 06.2 (B4).

### B3. Bảng kiểm "Tiêu chuẩn thứ nhất" và "Trình bày sáng sủa"

| Tiêu chí | Vi phạm (dòng) | Cách sửa |
|---|---|---|
| **Giọng kể** | Toàn văn dùng giọng khách quan và bị động. `grep` cho **0** lần "chúng ta" và **0** lần "ta". Tài liệu làm chủ ngữ ở các dòng 14 ("Bài học xét…"), 696 ("bài không chứng minh"), 780 ("Bài tập này dùng"), 866 ("Phần này xét"), 956 ("Trong mục này"), 1015 ("Các bảng và lời giải ở trên chỉ rõ"). | Câu kế hoạch hoặc lựa chọn viết "chúng ta" (ví dụ: "Để so sánh hai hành động tại D mà không có mô hình, chúng ta cần ước lượng riêng từng cặp"). Câu tính toán viết "ta được". Bên trong các khối định nghĩa, định lý, thuật toán vẫn giữ câu khách quan. |
| Vấn đề đi trước công cụ | Các `##` §2 (61), §3 (236) không có đoạn mở; §2.2 mở bằng ký hiệu (79); §4.4 (404) và §5.3 (518) mở bằng ký hiệu. | Mỗi `##` mở bằng thiếu hụt của mục trước, nêu trên dãy năm ô có số liệu. |
| Công thức được bao bởi lời | 96–98 ("Do đó" không có căn cứ); 264–269 và 394–396 không có câu đọc sau; 529 ("Sau đó dùng"). | Câu dẫn nêu công thức tính gì; câu đọc sau nêu từng thành phần nghĩa là gì. |
| Ký hiệu gọi tên khi xuất hiện | $v(s')$ và $p(s',r\mid s,a)$ ở dòng 65 không được gọi tên và không ghi chỉ số chính sách. | Đổi thành $v_\pi(s')$, kèm câu nhắc lại mô hình $p$ (Bài 03). |
| Mỗi bước suy diễn nêu lý do | 96 (luật kỳ vọng lặp chưa nêu); 180–187 (đẳng thức đầu dùng định nghĩa $\pi'$, đẳng thức cuối dùng định nghĩa $w$, đều chưa ghi); 205 (định lý điểm bất động Banach chưa nêu tên); 277–279 (ba dấu bằng trên một dòng). | Thêm cột căn cứ `&&\text{(…)}`; mỗi dấu bằng một dòng. |
| Phát biểu có bản đọc bằng lời, vai trò giả thiết, phản ví dụ | Mệnh đề §2.6 (210) và các định lý §6.4 (682–692) không có danh sách "Bỏ <giả thiết>: phản ví dụ". | Dùng ví dụ trong chương. Bỏ "$q_\pi$ chính xác": bảng I xếp sai (0 so với 998). Bỏ "$\gamma<1$": vòng B–C. Bỏ độ phủ: $Q(D,0)$ không bao giờ được cập nhật dưới chính sách tham lam. Bỏ Robbins–Monro: với $\alpha=0{,}8$, ước lượng theo mẫu cuối. Bỏ GLIE: khối xác suất dừng ở $7/8$. |
| Ví dụ cụ thể trước phát biểu tổng quát | §2.2 (ví dụ 102 sau định nghĩa 87); §6.3 (ví dụ 668–678 sau định nghĩa 656); §6.4 không có ví dụ trước định lý. | Đảo thứ tự; thêm ví dụ trước định lý (LunarLander hoặc một MDP hữu hạn nhỏ). |
| Nối mục bằng kết quả | Mọi `##` kết thúc bằng dòng "Nguồn:" (58, 233, 355, 490, 617, 724). Thiếu đoạn kết mục. | Thêm 1–2 đoạn văn xuôi gồm kết quả đã thu được (có số hiệu), điều còn thiếu, và việc của mục sau. Dòng "Nguồn:" chuyển vào TP11 hoặc dẫn tại chỗ. |
| Không tham chiếu ra ngoài tệp mà thiếu nội dung | 342 ("quy tắc của Bài 05"); các tham chiếu mơ hồ "ở phần sau" (100), "phần 6" (337), "phần MC" (386), "phần Sarsa" (554), "phần chính" (889, 944); liên kết `../RL-hk2-2025-2026/*.pdf` ở 58, 233, 355, 490, 617, 724, 946, 1009, 1015. | Dẫn bằng số hiệu và phát biểu lại. Liên kết PDF nguồn thay bằng trích dẫn văn bản (tác giả, năm, trang). |
| Câu đủ thành phần, đoạn có một luận điểm | Đoạn nhiều ý: 12, 14, 85, 100, 586, 696, 1003, 1007. Câu mảnh: dòng 3. | Mỗi đoạn một luận điểm, tối đa khoảng 4 câu. |
| Nhầm lẫn thường gặp nói thẳng | Đã có trong văn (250, 423, 427) nhưng chưa là khối `remark`. | Chuyển thành khối `remark` có số hiệu. |
| Hình được đọc trong văn bản | Hình 112 (greedy-chain) không có đoạn đọc; 501 (behavior-target) không có; 313 và 398 có đoạn đọc yếu. | Thêm đoạn đọc hình. Thêm SVG cấu trúc chương cho §1. |
| Chứng minh chia bước | Ba chứng minh 170–208, 891–940, 976–994 không có nhãn **Bước k** và không có $\square$. | Chia bước có nhãn, kết thúc bằng $\square$. |
| Tách phần của phát biểu | Định lý §6.4 thiếu bốn phần Giả thiết / Kết luận / Điều kiện áp dụng / Phạm vi. | Theo mẫu `theorem` của template. |
| Ví dụ tự chứa | 505 và 554 không nêu lại bảng I và năm mẫu. | Mở khối bằng đoạn "Dữ kiện". |
| Thuật ngữ Anh ở lần đầu | Chỉ có MC, TD, MDP, GLIE, on-/off-policy, importance sampling. | Bổ sung danh sách như phần deck (A3, cuối). |

### B4. Phần cần thêm và độ dài

- **Đoạn móc nối.**
  - Định nghĩa 06.1 nối với $q_\pi$ của Bài 03 và với $V$ của Bài 05.
  - Mệnh đề 06.6 mở rộng định lý cải thiện tham lam của Bài 04 sang lớp $\varepsilon$-mềm; cái giá là chỉ tối ưu trong lớp ấy.
  - Định nghĩa 06.20 mở rộng điều kiện Robbins–Monro theo trạng thái của TD(0) (Bài 05) thành điều kiện theo cặp.
  - Thuật toán 06.12 và 06.16 chỉ khác nhau ở số hạng tiếp nối; hệ quả là thay đổi dữ liệu cần dùng (bộ năm so với bộ bốn) và giá trị được học (chính sách mềm so với $q_*$).
  - Thuật toán 06.9 so với 06.12: lượt hoàn chỉnh so với bootstrap.
- **"Trong thực hành"**, đặt sau mỗi kết quả hoặc thuật toán chính:
  - Sau Mệnh đề 06.6: bảng $Q$ chỉ là ước lượng.
  - Sau Thuật toán 06.9: lượt LunarLander dài 267–773 bước, cắt ngắn ở 1000 bước, nên MC thiếu lợi tức hoàn chỉnh (notebook §6, đoạn "Vấn đề").
  - Sau Thuật toán 06.12 và 06.16: lưới 2187 ô và 8748 cặp; bước cắt ngắn vẫn bootstrap; trên `TEST_SEED`, chính sách tham lam của Sarsa đạt $26{,}2\pm14{,}0$ và của Q-learning đạt $-6{,}6\pm17{,}2$, hiệu $32{,}8\pm46{,}2$ chứa 0 nên chưa xếp hạng được.
  - Sau Định lý 06.21 và 06.22: quan sát gộp không Markov; sàn $\alpha_{\min}=0{,}05$ vi phạm Robbins–Monro; khối xác suất dừng ở $0{,}9625$ nên vi phạm GLIE; 45–48 % số cặp trong các ô được ghé có $n<10$ (notebook §10).
  - Các con số trên phải ghi "một lần chạy đã nhúng trong notebook", không khẳng định ngoài phạm vi đó.
- **Tình huống áp dụng.**
  - **06.1 (gắn bài thực hành):** Sarsa và Q-learning trên LunarLander. Mô hình hóa (ô, bốn hành động, $\gamma=0{,}99$), kiểm giả thiết của Định lý 06.21–06.22 (cả ba đều không thỏa), áp dụng Thuật toán 06.12 và 06.16, diễn giải theo khoảng tin cậy ghép cặp, nêu giới hạn. Thiết lập tinh chỉnh đạt 202,8 và 235,5, nhưng vẫn không thỏa định lý.
  - **06.2 (giả thiết không thỏa):** chính sách tham lam từ bảng khởi tạo nghiêng phải tạo vòng B–C trên dãy năm ô. Lượt bắt đầu ở B hoặc C không kết thúc, nên giả thiết của Thuật toán 06.9 và tính khả tích của lợi tức khi $\gamma=1$ bị vi phạm. Hậu quả: MC không cập nhật được; Sarsa và Q-learning vẫn cập nhật từng bước nhưng nằm ngoài miền Định lý 06.21–06.22. Căn cứ nguồn: tr. 16.
- **Mục "Ứng dụng".**
  - Bài 07: xấp xỉ hàm; hai notebook `thuc-hanh-lunarlander-xap-xi-tuyen-tinh` và `thuc-hanh-flappybird-dieu-khien-tuyen-tinh` (có Double Q-learning).
  - Bài 08 (Deep Q-learning) và Bài 09 (Double DQN): mục tiêu cực đại và mạng mục tiêu.
  - Notebook Bài 06 §9.2: Q-learning đánh giá cao, với $\max_aQ(S_0,a)-G_0=21{,}5\pm7{,}2$.
- **Tóm tắt chương:** một đoạn 5–8 câu kể lại chương; "Định nghĩa và kết quả theo mục"; "Công thức cần nhớ" (ba mục tiêu $Y$ và cập nhật MC); "Giả thiết hay bị bỏ quên" ($q_\pi$ chính xác; $\gamma<1$; Robbins–Monro theo cặp; GLIE chỉ cần cho Sarsa; kết thúc khác cắt ngắn).
- **Bài tập củng cố 06.7–06.12** (mỗi mục tiêu ít nhất một bài):
  - Nhận biết: 06.7 phân loại theo hoặc khác chính sách cho MC, Sarsa, Q-learning; 06.8 đúng/sai về $q_\pi$, $Q$, $q_*$.
  - Tính toán hoặc chứng minh: 06.9 chứng minh $\alpha_n=n^{-p}$ thỏa Robbins–Monro khi và chỉ khi $1/2<p\le1$; 06.10 một lượt Q-learning trên dãy năm ô với $\alpha=1/2$ từ bảng khởi tạo nghiêng trái; 06.11 kiểm Mệnh đề 06.6 với $q=(3,3,-1)$, $\varepsilon=0{,}3$, $\pi=(0{,}2;0{,}1;0{,}7)$ (kết quả 0,2 và 2,6).
  - Vận dụng: 06.12 phân phối $\varepsilon$-tham lam bốn hành động $(5;1;1;1)$, xác định $\varepsilon$ để $\pi(0)=0{,}9$ (lời giải $\varepsilon=0{,}4/3$; trùng câu hỏi notebook §5, cần ghi nguồn).
- **Độ dài:** hiện khoảng 10 800 từ văn xuôi (11 557 theo `wc`). Đích **16 000–19 000 từ**. Phần tăng đến từ đoạn mở và kết mục, đoạn đọc phát biểu, đoạn móc nối, "Trong thực hành", hai tình huống, tóm tắt và 6 bài tập củng cố. Phần giảm đến từ việc chuyển §7.4 sang `exercises.md` và chuyển nội dung trùng Bài 05 thành nhắc lại.

### B5. Giáo trình cần đối chiếu theo mục

Số trang của Szepesvári và Bertsekas–Tsitsiklis cần tác tử soạn xác minh.

| Mục mới | Sutton và Barto (2018) | Khác |
|---|---|---|
| Mở chương, §1 | §3.5–3.6 ($q_\pi$, $q_*$); §4.2 (định lý cải thiện, tr. 78–80); §5.2 (tr. 96–97); §5.3 (GPI, tr. 97–100); §5.4 ($\varepsilon$-mềm và chứng minh, tr. 100–103); §2.2–2.4 ($\varepsilon$-tham lam, trung bình gia tăng) | Giáo trình *Học máy thống kê*, `sec_q_learning.tex` ("Học hàm Q thông qua kinh nghiệm", ε-greedy, thuật toán SARSA) cho giọng kể và thuật ngữ; `sec_dynamic_progamming.tex` cho toán tử co. Puterman (1994) §6.2 cho tính co. |
| §2 MC | §5.3–5.4; §5.1 (lần ghé đầu, tr. 92–93) | Tsitsiklis (2002), JMLR 3, tr. 59–72 |
| §3 Sarsa | §6.4 (tr. 129–130); §6.1–6.2 (TD(0)) | Szepesvári (2010) §3.4.1 (SARSA trong mục cài đặt critic) |
| §4 Q-learning | §6.5 (tr. 131–132); §5.5 (hành vi và đích) | Szepesvári (2010) §3.3.1 (Q-learning trong MDP hữu hạn); Watkins và Dayan (1992), *Machine Learning* 8:279–292 |
| §5 Hội tụ | §2.5 (Robbins–Monro, tr. 33); §6.4–6.5 | Singh, Jaakkola, Littman và Szepesvári (2000), *Machine Learning* 38:287–308 (GLIE, Định lý 1, tr. 294–295); Bertsekas và Tsitsiklis (1996), Ch. 4 (xấp xỉ ngẫu nhiên) và §5.6 (Q-learning); Robbins và Monro (1951) |
| §6 Đọc thêm | §5.5, §7.3 (công thức 7.9–7.10, tr. 148) | Hoeffding (1963), JASA 58:13–30, Định lý 2 |
| Tình huống, Ứng dụng | §6.6–6.7 (chỉ dẫn, không giảng) | Notebook Bài 06; tài liệu `LunarLander` của Gymnasium |

### B6. Bảng ký hiệu đề xuất và các chỗ lệch

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $\mathcal S^+$ | trạng thái không kết thúc; thêm trạng thái kết thúc | hữu hạn |
| $\mathcal A(s)$, $m(s)$ | hành động hợp lệ; số phần tử | hữu hạn; $\mathbb N$ |
| $M$ | số cặp hợp lệ $\sum_s m(s)$ | $\mathbb N$ |
| $S_t,A_t,R_{t+1}$ | trạng thái, hành động, thưởng sau $A_t$ | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathbb R$ |
| $T$ | thời điểm kết thúc thật của lượt | $\mathbb N$ |
| $\gamma$ | hệ số chiết khấu | $[0,1]$; định lý cần $[0,1)$ |
| $G_t$ | lợi tức, $G_T=0$ | biến ngẫu nhiên thực |
| $\pi(a\mid s)$, $b(a\mid s)$ | chính sách đích; chính sách hành vi | phân phối trên $\mathcal A(s)$ |
| $v_\pi,q_\pi,q_*$ | giá trị thật | $\mathbb R$ |
| $Q$, $Q_t$, $Q^{[k]}$ | bảng ước lượng; trước cập nhật bước $t$; trước lượt $k$ | $\mathbb R^{M}$ |
| $\varepsilon$, $\varepsilon_k$ | tham số thăm dò; lịch theo lượt | $[0,1]$ |
| $\mathcal G_Q(s)$, $\pi_\varepsilon$ | tập cực đại; chính sách $\varepsilon$-tham lam | tập con của $\mathcal A(s)$; phân phối |
| $N(s,a)$ | số lợi tức MC đã dùng | $\mathbb N$ |
| $n(s,a)$, $\alpha_n(s,a)$, $\alpha_t$ | số cập nhật của cặp; bước học theo cặp; $\alpha_t=\alpha_{n(S_t,A_t)+1}(S_t,A_t)$ | $\mathbb N$; $(0,1]$ |
| $Y_t,\delta_t$ | mục tiêu cập nhật; sai lệch | $\mathbb R$ |
| $C_t(s,a)$ | số lần thăm tới bước $t$ (GLIE) | $\mathbb N$ |
| $K$, $H$, $h$ | ngân sách lượt (MC); ngân sách cập nhật; số cập nhật đã làm | $\mathbb N$ |
| $d_0$ | phân phối trạng thái đầu | phân phối trên $\mathcal S$ |
| $\rho_t$ | tỉ số lấy mẫu quan trọng (đọc thêm) | $[0,\infty)$ |

Câu nêu tương ứng với giáo trình *Học máy thống kê*: $q_\pi \leftrightarrow Q^\pi$, $v_\pi\leftrightarrow V^\pi$, mục tiêu $Y_t\leftrightarrow q$ trong `sec_q_learning`.

**Các chỗ lệch giữa deck, ghi chú và notebook:**
1. $v(s')$ không chỉ số ở deck B01 và ghi chú dòng 65, trong khi notebook ô 15 viết $V(s')$ (vốn là bảng ước lượng). Thống nhất thành $v_\pi(s')$.
2. **Dấu thập phân:** deck và ghi chú dùng "0.8" (cả Bài 05 cũng vậy); notebook và bộ mẫu math-4-AI dùng "0{,}99". Cần chọn một quy ước (xem D).
3. Ngân sách: ghi chú dùng $H$ cập nhật cho Sarsa và Q-learning; notebook dùng $K$ lượt (notebook có ghi rõ). Deck D05 và E04 viết "ngân sách cập nhật" mà không có ký hiệu.
4. Bước học: deck D03 dùng $\alpha=0{,}8$, D04 dùng $\alpha_t$, F03 dùng $\alpha_n(s,a)$. Cần dòng tương ứng trong bảng ký hiệu (đã có ở dòng $\alpha_t$ phía trên).
5. Cắt ngắn ở 1000 bước (notebook) chưa được ghi chú nêu thành loại sự kiện thứ ba bên cạnh kết thúc lượt và hết ngân sách. Bổ sung bằng Nhận xét 06.13.
6. Mục tiêu học tập: deck có 3, ghi chú 5, outline 7, notebook 5. Thống nhất theo A2.
7. Notebook trích dẫn "ghi chú Bài 06, mục 2.1 … 6.1–6.5" và "bài giảng gốc, tr. …". Sau khi đánh số lại ghi chú, phải cập nhật Markdown của notebook.
8. "quá trình quyết định Markov" được dùng ở deck 03, ghi chú 04–06, notebook và giáo trình *Học máy thống kê*, trong khi AGENTS dòng 159 viết "quy trình quyết định Markov". Đề xuất giữ "quá trình" và ghi vào bảng thuật ngữ.
9. Tiêu đề: ghi chú là "Bài 06. …", deck là "Bài 06: …", mẫu là "Bài 06 — …".

---

## C. Bài tập (`exercises.md` mới)

| Số hiệu | Mạch | Mức | Đối tượng và dữ kiện tóm tắt | Trùng trang chiếu hay mới | Năng lực đo |
|---|---|---|---|---|---|
| 06.1 | 2 | nhận biết | Mẫu $(D,1,10,E)$ trên dãy năm ô | trùng trang vấn đề đầu mạch 2 (L06-A05 sau khi chuyển) | đọc thông tin của mẫu; phân biệt hành động chưa được quan sát |
| 06.2 | 2 | tính toán | $\varepsilon=1/4$ tại D, có trường hợp đồng hạng; diễn giải $q_\pi(D,0)$ | trùng B07/B10 | tính phân phối; phân biệt $q_\pi$ với $Q$; điều kiện áp dụng Mệnh đề 06.6 |
| 06.3 | 3 | tính toán | Lượt D–C–D–C–B–A; lần ghé đầu so với mọi lần ghé | trùng C08/C09 | lợi tức tính lùi; lần ghé đầu theo cặp; bộ đếm $N$ |
| 06.4 | 4 | tính toán | Mẫu thứ năm Sarsa, $Q(C,0)=-0{,}6$ | trùng D08/D11 | mục tiêu và sai lệch; thời điểm lấy $A'$; ngân sách khác kết thúc |
| 06.5 | 5 | tính toán | B $=(800,1)$, $A'=1$; so sánh hai mục tiêu | trùng E08/E12 | phân biệt số hạng tiếp nối; điều kiện trùng mục tiêu |
| 06.6 | 6 | nhận biết | Ba trường hợp hành vi và bước học, $\gamma=0{,}9$ | trùng F05/F09 | kiểm giả thiết của Định lý 06.21–06.22 |
| 06.13 | 3, 5 | tính toán | Dãy sáu ô A–F, $\gamma=1/2$, chuyển ngẫu nhiên ở B; MC lần ghé đầu và Q-learning với $\alpha=1$ (nguồn: hw3 Bài 10, lời giải ở ghi chú §7.4) | mới (chuyển từ ghi chú) | thực hiện trọn hai thuật toán trên dữ liệu mới; xử lý chuyển tự quay về B |
| 06.14 | 2 | chứng minh | Ba hành động, $q=(3,3,-1)$, $\varepsilon=0{,}3$; chứng minh $\pi_\varepsilon$ là $\varepsilon$-mềm và phản ví dụ chiều ngược | mới | dùng Định nghĩa 06.3–06.4 và Mệnh đề 06.6 |
| 06.15 | 4 | vận dụng [Lập trình] | Notebook LunarLander: đặt $Y=R$ khi cắt ngắn rồi so với bootstrap, cùng hạt giống | mới | phân biệt kết thúc, cắt ngắn và ngân sách; đọc hiệu ghép cặp |
| 06.16 | 6 | vận dụng [Lập trình] | Notebook §10 và §13 nhiệm vụ 2–3: $\varepsilon_k=\min(1,c/k)$, $\alpha_n=1/n$; tính khối xác suất trên cực đại | mới | đưa cấu hình về thỏa GLIE và Robbins–Monro; chỉ ra giả thiết Markov vẫn không thỏa |
| 06.17 | 7 | vận dụng | Tàu đổ bộ: lượt ≤ 1000 bước, hành vi $\varepsilon=0{,}05$; chọn phương pháp và mục tiêu tại bước cắt ngắn | trùng G03/G07 | tổng hợp dữ liệu, mục tiêu và giả thiết |

Mỗi mạch nội dung 2–7 có ít nhất một bài; có 3 bài vận dụng (06.15–06.17). Phần mở đầu tệp nêu: 06.1–06.6 giữ số hiệu và lời giải của ghi chú; 06.7–06.12 thuộc "Bài tập củng cố" và không chép lại; 06.13–06.17 chỉ có trong tệp này. Bảng `Mạch | Mở phần | Bài tập` trỏ tới `#/N/1`. Phần "Hướng dẫn và ký hiệu" nêu quy ước dấu thập phân và dữ kiện dãy năm ô. Tránh Expected Sarsa và thiên lệch cực đại trong bài tập chính vì ngoài phạm vi deck; nếu người dùng muốn, chỉ thêm ở dạng [Tìm hiểu].

---

## D. Rủi ro, thứ tự thực hiện, câu hỏi cho người dùng

**Thứ tự** (theo `prompt_lecture_note_deck.md`):
1. **Ghi chú** (Giai đoạn I): tác tử soạn viết lại theo B1–B6 ở chế độ `no-ai-slop` Edit, tự đối chiếu `eval.md`; rà toán tính lại toàn bộ số liệu; rà mạch viết kiểm tám bước và đoạn kết mục; điều phối viên duyệt; commit `fix(materials-06)` và push.
2. **Deck** (Giai đoạn II): sửa theo A1–A5; đồng bộ storyboard (âm tiết trước và sau cho 21 trang), outline (bảng Việt–Anh) và review-log; dọn CSS cục bộ; tái kiểm toán và mạch; kiểm trực quan ở 1600×900 và 390×844 trên mọi trang; commit `fix(lecture-06)`.
3. **`exercises.md`**: soạn → rà → thêm nhóm "Bài tập" vào thẻ Bài 06 trong `index.html` khi đã đạt.
4. **Notebook**: chỉ cập nhật tham chiếu mục trong các ô Markdown (rủi ro 1 dưới đây).

**Rủi ro:**
- (1) Tham chiếu mục của notebook hỏng sau khi đánh số lại. Mọi chỉnh notebook phải qua ba lượt rà theo AGENTS.
- (2) Bài 03–05 chưa có số hiệu, nên tiên quyết chỉ dẫn được theo tên bài và mục kèm phát biểu lại.
- (3) Deck tăng từ 45 lên khoảng 70 trang; phải giữ đúng 120 phút.
- (4) Số hiệu tạm trong A3 lệch số hiệu cuối của B2; phải đồng bộ.
- (5) Thêm trang tiêu đề mạch làm dịch chỉ số dọc; `exercises.md` và G04 chỉ được dẫn `#/N/1`.
- (6) Không có raster. Có thể cần một SVG mới cho cấu trúc chương ở §1 (`img/lec-06/`). Không cần ngoại lệ raster.

**Câu hỏi cho người dùng:**
1. Đơn vị in trên bìa: dùng "Trường Đại học Công nghệ · ĐHQGHN" như học phần chị em, hay giữ quy định "không gán đơn vị chưa xác minh"?
2. Dấu thập phân của học phần: dấu phẩy (notebook, math-4-AI) hay dấu chấm (deck và ghi chú Bài 05–06)?
3. Giữ thuật ngữ "quá trình" hay đổi theo AGENTS thành "quy trình quyết định Markov"?
4. Có nâng cấp ghi chú Bài 05 (đánh số) trước để Bài 06 dẫn được `05.k` không?
5. Có cho phép sửa Markdown của notebook Bài 06 trong đợt này để cập nhật tham chiếu không?
6. Có đồng ý bỏ các liên kết tới PDF nguồn `../RL-hk2-2025-2026/` trên deck và ghi chú, thay bằng trích dẫn văn bản không?
