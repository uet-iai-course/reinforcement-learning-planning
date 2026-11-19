# Storyboard Bài 11: Lập kế hoạch dựa trên mô hình

Giai đoạn III.1 (2026-11-19). Bộ trang chiếu dựng mới `rl-plan/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html`, thay hoàn toàn bản storyboard của Bài 11 cũ (gradient chính sách nâng cao; bản cũ còn trong git, Q2). Nguồn nội dung duy nhất (P1, ngoại lệ Bài 11 ở `NGUYEN-TAC-HOC-PHAN.md` mục 3; Q1): ghi chú `materials/lec-11/lecture-note.md` đã duyệt (commit `a6329c2`) và `materials/lec-11/exercises.md` đã duyệt (commit `397e3d5`). Không có deck nguồn. Kế hoạch mạch: `ke-hoach-trang-chieu.md`, điều chỉnh theo ghi chú đã biên tập (mục "Sai khác so với kế hoạch" cuối tệp). Khung lý thuyết, bảng thuật ngữ, phân loại chủ đề: `outline.md`.

Quy định áp dụng: `NGUYEN-TAC-TRANG-CHIEU.md` (NT1–NT28), `NGUYEN-TAC-HOC-PHAN.md` (P1–P11 tóm tắt, NT-RL-7…11, lược đồ mã mục 5), `AGENTS.md` "Tham số trang chiếu của học phần" (NT-RL-1…6), `NGUYEN-TAC-VAN-PHONG.md` (VP1–VP24). Chuỗi lên mặt trang trong tệp này (tiêu đề, `p.strand-lead`, câu trên trang) đã sửa bằng `no-ai-slop` chế độ Edit; người soạn deck giữ nguyên nghĩa, chỉ chỉnh khi `deck_lint.py` báo vượt trần.

**Quy ước của tệp.** Âm tiết: token cách nhau bởi khoảng trắng, không tính tiêu đề, KaTeX, số trong ô bảng, nhãn hình, ghi chú diễn giả; số viết trong câu có tính (NT17). Số âm tiết ở đây là **ước lượng** trên câu dự kiến; số chính thức lấy từ `deck_lint.py --course rl-plan`. Mỗi gạch đầu dòng, câu, dòng nhãn, công thức hiển thị và mỗi hàng bảng là một dòng; hàng tiêu đề cột không tính. Mọi số thập phân viết `0{,}5` trong KaTeX (VP-RL-6). Quyết định của mọi trang là `thêm` (deck dựng mới, không có trang nguồn); lý do ghi ở từng mục. Ghi chú diễn giả mọi trang 40–150 âm tiết (trang tiêu đề mạch 40–100; ý tưởng chứng minh, bài tập, lời giải đến khoảng 250), kết bằng `<p class="note-source"><strong>Nguồn:</strong> ghi chú bài giảng Bài 11, §k (…); Sutton và Barto (2018), §… .</p>` (NT22), không mã trang, không thời lượng (VP8). Mỗi trang mang `data-note-topic-id` của chủ đề chính.

## 1. Câu hỏi trung tâm và khung lý thuyết chung

**Câu hỏi trung tâm** (ghi chú §1.1, "Bài toán trung tâm của chương"; chuỗi của `outline.md` đã sửa bằng `no-ai-slop` Edit). Hộp "Câu hỏi:" duy nhất của `L11-1-07` (NT11):

> **Câu hỏi:** tác tử chỉ được đi ít bước thật, nhưng sau mỗi bước được tính thêm trên một mô hình học từ các bước đã đi. Dùng mô hình đó thế nào để chọn hành động tốt hơn phương pháp phi mô hình với cùng số bước thật, và sai số của mô hình làm mất những bảo đảm nào?

Câu trả lời có điều kiện (ghi chú §6.2, bốn ý) chỉ ở ghi chú diễn giả của `L11-1-07` và trên mặt trang `L11-6-03` (NT11, NT15).

**Khung lý thuyết chung** (từ `outline.md`, mục "Khung lý thuyết chung"):

- **Bài toán trung tâm.** Tác tử có một mô hình của môi trường, cho sẵn hoặc học từ ít bước thật, và một ngân sách tính toán trên mô hình sau mỗi bước thật; cần dùng ngân sách đó để chọn hành động tốt hơn phương pháp phi mô hình với cùng số bước thật, và biết bảo đảm nào còn đúng khi mô hình sai. Bốn cách dùng mô hình ứng với bốn mạch nội dung: cập nhật bảng giá trị cho nhiều trạng thái trong lúc hành động (mạch 2, §2); tìm kiếm từ trạng thái hiện tại với hành động rời rạc (mạch 3, §3) hoặc liên tục (mạch 4, §4); gộp nhiều bước thành tùy chọn (mạch 5, §5).
- **Đối tượng và ký hiệu chung.** MDP hữu hạn, động lực thật $p(s',r\mid s,a)$, $\gamma\in[0,1)$; mô hình học được $\hat p(s'\mid s,a)$, $\hat r(s,a)$; mô hình phân phối khác mô hình mẫu (Định nghĩa 11.1). Mọi bảo đảm là bảo đảm **trên mô hình** ($\hat q_*$ của MDP mà mô hình định nghĩa). Mạch 4 đổi sang $x_t,u_t\in\mathbb R$, mô hình tất định khả vi $\hat f$, chi phí $c\ge0$, chân trời $h$, không chiết khấu. Mạch 5 thêm $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$, $\tau$, mô hình tùy chọn $r(s,\omega)$, $p(s'\mid s,\omega)$ có chiết khấu nằm trong $p$.
- **Giả thiết chung.** (M1) MDP hữu hạn, trạng thái quan sát được, Markov, động lực dừng; (M2) phần thưởng bị chặn, $0\le\gamma<1$ (mạch 2, 3, 5); (M3) mô hình cố định trong lúc lập kế hoạch; (M4) mô hình đúng trên những cặp mà kế hoạch đi qua. Từng trang kết quả nêu giả thiết nó dùng; (M4) bị vi phạm ở Tình huống 11.2 (ghi chú diễn giả `L11-2-08`).
- **Chuỗi định nghĩa → kết quả → phương pháp.** Định nghĩa 11.1, 11.2 → 11.4, Mệnh đề 11.5, Định nghĩa 11.6 → Thuật toán 11.8, Mệnh đề 11.9 → Thuật toán 11.10 → Định nghĩa 11.12 → Định nghĩa 11.14, Mệnh đề 11.15 → Thuật toán 11.20, Mệnh đề 11.21, 11.22 → Định nghĩa 11.23, Định lý 11.24 → Định nghĩa 11.25, Thuật toán 11.26, Định lý 11.27 → Định nghĩa 11.29, Mệnh đề 11.30, Thuật toán 11.31 → Định nghĩa 11.32, Thuật toán 11.33 (11.34 chỉ một dòng "Cách khác:") → Mệnh đề 11.36 → Định nghĩa 11.38–11.40, Mệnh đề 11.41 → Định lý 11.42 → Định lý 11.44, Thuật toán 11.45 → Thuật toán 11.46.
- **Giới hạn áp dụng.** Mệnh đề 11.9 nói về $\hat q_*$ của mô hình cố định, xác định ở mọi cặp; Dyna-Q không thỏa (Nhận xét 11.11). Mệnh đề 11.21 cần $q_{\pi_0}$ chính xác; 11.22 cần $m$ chọn trước, mô phỏng độc lập, không cắt. Định lý 11.27(a) nói về UCT của Kocsis và Szepesvári, không về Thuật toán 11.26. Mệnh đề 11.36 chỉ cho vòng hở. Định lý 11.42, 11.44 cần tùy chọn kết thúc với xác suất $1$; $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$.

**Trang khung chung và "Ngữ cảnh"** (P5; Q16, QT7): gộp thành một trang `L11-1-06` "Ngữ cảnh" (ba dòng: mê cung, khung chung, lượt thứ nhất với Q-learning; cùng hình mê cung).

## 2. Bảng mạch (NT10, NT12, NT13)

Sáu mạch (Q14), mỗi mạch nội dung ứng đúng một mục của ghi chú và một mục 11.1–11.4 của giáo trình. **Tên mạch theo đúng tên mục của ghi chú, cả trên trang tiêu đề mạch lẫn trang "Nội dung"; không dùng tên rút gọn.** Lý do: NT11 đòi tên trên "Nội dung" trùng tên trang tiêu đề mạch; `exercises.md` (quyết định E-7 ở giai đoạn II) đã ghi tên mạch theo ghi chú trong bảng `Mạch | Mở phần | Bài tập`; tên dài nhất ("Tính bất định của môi trường và lập kế hoạch nền", 11 âm tiết) vẫn vừa một dòng `h2`. Đ7 của `outline.md` (tên rút gọn "Tính bất định và lập kế hoạch nền") không còn cần; xem câu hỏi C3.

| Mạch | Tên (trang tiêu đề mạch, "Nội dung") | Loại | Câu hỏi của mạch (NT13) | Đầu vào | Đầu ra | Đóng góp cho câu hỏi trung tâm | Trang tiêu đề | Trang | Phút |
|---:|---|---|---|---|---|---|---|---:|---:|
| 1 | Bài toán lập kế hoạch với mô hình học được | mở đầu | (mạch mở đầu đặt câu hỏi trung tâm) | Định nghĩa 01.14; Định lý 06.21, 04.13; Mệnh đề 03.22, 03.23 | mê cung hai phòng; Q-learning chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$ sau lượt thứ nhất; khung "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách"; câu hỏi trung tâm | đặt câu hỏi | không có (bìa `L11-1-01`) | 7 | 9 |
| 2 | Tính bất định của môi trường và lập kế hoạch nền | khái niệm; kết quả; thuật toán | "Câu hỏi: mô hình học từ ít bước thật sai đến đâu, và dùng nó thế nào để có thêm cập nhật?" | bốn mẫu chuyển bị Q-learning bỏ (`L11-1-06`) | Định nghĩa 11.1, 11.2, 11.4, 11.6, 11.12, 11.14; Mệnh đề 11.5, 11.9, 11.15; Thuật toán 11.8, 11.10. Giới hạn: lập kế hoạch nền tốn phép tính cho cả $\mathrm A$, $\mathrm B$, $\mathrm E$ | câu trả lời 1 (lập kế hoạch nền) | `L11-2-00`, `id="mach-2"` | 13 | 30 |
| 3 | Tìm kiếm theo cây Monte Carlo | thuật toán; kết quả | câu khẳng định "Tại $\mathrm F$ chỉ cần một quyết định; phép tính dồn vào các hành động tại $\mathrm F$." | giới hạn của mạch 2; mô hình mẫu (Định nghĩa 11.1); Định nghĩa 11.2 | Thuật toán 11.20, 11.26; Mệnh đề 11.21, 11.22; Định nghĩa 11.23, 11.25; Định lý 11.24, 11.27. Giới hạn: cần tập hành động hữu hạn | câu trả lời 2 (tại thời điểm quyết định, hành động rời rạc) | `L11-3-00`, `id="mach-3"` | 12 | 28 |
| 4 | Tối ưu kế hoạch dựa trên đạo hàm | thuật toán; kết quả | câu khẳng định "Mô hình khả vi cho đạo hàm của chi phí theo $u_t$.", sau câu nối "độ dịch chuyển $u_t\in\mathbb R$ của xe không liệt kê được" trên `L11-4-01` | giới hạn của mạch 3 | Định nghĩa 11.29, 11.32; Mệnh đề 11.30, 11.36; Thuật toán 11.31, 11.33 (11.34 một dòng). Giới hạn: chân trời dài làm sai số và số hành động cần tối ưu cùng tăng | câu trả lời 3 (hành động liên tục, sai số tích lũy) | `L11-4-00`, `id="mach-4"` | 9 | 20 |
| 5 | Học tăng cường phân cấp | khái niệm; kết quả; thuật toán | câu khẳng định "Mọi phương pháp tới đây quyết định theo từng bước gốc." cùng số đo $V_6(\mathrm A)=0{,}6103<v_*(\mathrm A)=0{,}6604$ trên `L11-5-01` | giới hạn của mạch 4 (quyết định theo từng bước gốc); lặp giá trị (Bài 04) | Định nghĩa 11.38–11.40; Nhận xét 11.43; Mệnh đề 11.41; Định lý 11.42, 11.44; Thuật toán 11.45, 11.46 | câu trả lời 4 (trừu tượng thời gian) | `L11-5-00`, `id="mach-5"` | 10 | 22 |
| 6 | Tổng kết | tổng kết | (không khái niệm mới) | mọi kết quả mạch 2–5 | bảng tổng kết (gộp bảng thứ ba của P4), bảng phương pháp, câu trả lời có điều kiện, bài tập tổng hợp 11.10 | trả lời câu hỏi trung tâm | `L11-6-00`, `id="mach-6"` | 9 | 11 |
| | **Tổng** | | | | | | | **60** | **120** |

Mạch $k$ mở tại `#/k/1` (`hashOneBasedIndex: true`); mạch 1 mở tại `#/1/1` là bìa. Trang tiêu đề mạch (NT12; `div.strand-title-body` > `h2` với `span.strand-number` + `p.strand-lead` + `p.strand-keys`). Dòng dẫn đã sửa bằng `no-ai-slop` Edit; năm câu có năm khuôn khác nhau; âm tiết đếm tay:

| Trang | `h2` | `p.strand-lead` (âm tiết) | `p.strand-keys` |
|---|---|---|---|
| `L11-2-00` | 2. Tính bất định của môi trường và lập kế hoạch nền | "Mô hình học từ ít mẫu có sai số, nhưng mỗi bước thật vẫn cho thêm nhiều cập nhật." (19) | mô hình phân phối · mô hình đếm · bất định nhận thức · Dyna-Q · cập nhật mẫu |
| `L11-3-00` | 3. Tìm kiếm theo cây Monte Carlo | "Tìm kiếm từ trạng thái hiện tại dồn phép tính vào đúng một quyết định." (15) | thuật toán rollout · số mô phỏng · cận tin cậy trên · chính sách cây |
| `L11-4-00` | 4. Tối ưu kế hoạch dựa trên đạo hàm | "Khi mô hình khả vi, đạo hàm theo chuỗi hành động cho biết hướng sửa kế hoạch." (17) | tối ưu kế hoạch · truy hồi ngược · điều khiển dự báo · sai số tích lũy |
| `L11-5-00` | 5. Học tăng cường phân cấp | "Gộp nhiều bước thành một quyết định vẫn giữ được phương trình Bellman và tính co." (18) | tùy chọn · mô hình tùy chọn · bán-MDP · lặp giá trị với tùy chọn |
| `L11-6-00` | 6. Tổng kết | "Bốn cách dùng mô hình khác nhau ở thời điểm tính, loại hành động và bảo đảm." (17) | — |

Tên mạch khác tiêu đề trang nội dung đầu tiên (NT12): `L11-2-01` "Ví dụ: mô hình của cặp $(\mathrm F,\rightarrow)$", `L11-3-01` "Ví dụ: thuật toán rollout tại ô $\mathrm F$", `L11-4-01` "Ví dụ: xe trên đường ray", `L11-5-01` "Ví dụ: hai tùy chọn trên mê cung hai phòng", `L11-6-01` "Bảng tổng kết": đạt. Dòng dẫn chỉ dùng từ thông thường và khái niệm đã có trước mạch (mô hình, mẫu, bước thật, cập nhật, trạng thái hiện tại, đạo hàm, kế hoạch, MDP); "tùy chọn" chỉ ở `p.strand-keys`, không ở dòng dẫn. Dòng dẫn mạch 6 nêu ba tiêu chí của bảng so sánh §6.1 (thời điểm tính, loại hành động, bảo đảm), không lặp luận điểm bìa (biên tập III.5, vai mạch). Dòng dẫn mạch 4 dùng "cho biết hướng", mạch 5 nêu điều tùy chọn giữ được (phương trình Bellman, tính co), cả năm khuôn câu vẫn khác nhau.

## 3. Danh sách trang và thời lượng (P6, NT27; thời lượng chỉ ở planning)

Cột `note-topic-id` ghi giá trị của thuộc tính `data-note-topic-id` của trang; mã trong ngoặc là chủ đề phụ có mặt trên trang (ánh xạ đầy đủ ở mục 8).

| Mạch | Mã | Tiêu đề | Bước hành trình (NT8) | Khối ghi chú | `note-topic-id` | Hình | Phút |
|---:|---|---|---|---|---|---|---:|
| 1 | `L11-1-01` | Lập kế hoạch dựa trên mô hình | bìa | tiêu đề, §1.1 | `lec-11-topic-02` | — | 0,5 |
| 1 | `L11-1-02` | Tiên quyết và quy ước | nhắc lại | Kiến thức tiên quyết, Bảng ký hiệu | `lec-11-topic-01` | — | 2 |
| 1 | `L11-1-03` | Mục tiêu học tập | mục tiêu 1–4 | Mục tiêu học tập | `lec-11-topic-01` | — | 1 |
| 1 | `L11-1-04` | Mục tiêu học tập | mục tiêu 5–7 | Mục tiêu học tập | `lec-11-topic-01` | — | 0,5 |
| 1 | `L11-1-05` | Nội dung | nội dung | §1–§6 | `lec-11-topic-03` | — | 0,5 |
| 1 | `L11-1-06` | Ngữ cảnh | vấn đề (ví dụ dẫn nhập), khung chung | Ví dụ 11.1, §1.1, §1.2 | `lec-11-topic-02` (+03) | `me-cung-hai-phong-slide.svg` | 2,5 |
| 1 | `L11-1-07` | Vấn đề trung tâm | vấn đề | §1.1 | `lec-11-topic-02` | — | 2 |
| 2 | `L11-2-00` | 2. Tính bất định của môi trường và lập kế hoạch nền | tiêu đề mạch | §2 | `lec-11-topic-04` | — | 0,5 |
| 2 | `L11-2-01` | Ví dụ: mô hình của cặp $(\mathrm F,\rightarrow)$ | vấn đề → ví dụ → định nghĩa | §2.1; Ví dụ 11.2; Định nghĩa 11.1 | `lec-11-topic-04` | — | 3 |
| 2 | `L11-2-02` | Lập kế hoạch nền và lập kế hoạch tại thời điểm quyết định | vấn đề → ví dụ → định nghĩa | Định nghĩa 11.2; Nhận xét 11.3 | `lec-11-topic-04` | — | 2 |
| 2 | `L11-2-03` | Mô hình đếm | vấn đề → ví dụ → định nghĩa → kết quả | §2.2; Ví dụ 11.3; Định nghĩa 11.4; Mệnh đề 11.5 | `lec-11-topic-05` | — | 3 |
| 2 | `L11-2-04` | Bất định ngẫu nhiên và bất định nhận thức | trực quan → ví dụ → định nghĩa → ứng dụng | Ví dụ 11.4, 11.5; Định nghĩa 11.6; Nhận xét 11.7 | `lec-11-topic-05` (+06) | — | 2,5 |
| 2 | `L11-2-05` | Bài tập: hai loại bất định | kiểm tra (lời giải fragment) | Bài tập 11.2 | `lec-11-topic-27` | — | 2 |
| 2 | `L11-2-06` | Q-planning | vấn đề → trực quan → ví dụ → thuật toán → bảo đảm | §2.4; Ví dụ 11.6; Thuật toán 11.8; Mệnh đề 11.9 | `lec-11-topic-07` | — | 2,5 |
| 2 | `L11-2-07` | Ví dụ: lượt thứ nhất của Dyna-Q | vấn đề → trực quan → ví dụ tính tay trước giả mã | Ví dụ 11.7 | `lec-11-topic-07` | — | 3 |
| 2 | `L11-2-08` | Thuật toán Dyna-Q | thuật toán → kiểm tra giả thiết | Thuật toán 11.10; Nhận xét 11.11 | `lec-11-topic-07` | `kien-truc-dyna-slide.svg` | 2,5 |
| 2 | `L11-2-09` | Mô hình sai và thưởng thăm dò | vấn đề → ví dụ → trực quan → ví dụ số → định nghĩa | §2.5; Ví dụ 11.8, 11.9; Định nghĩa 11.12 | `lec-11-topic-08` | — | 2,5 |
| 2 | `L11-2-10` | Cập nhật kỳ vọng và cập nhật mẫu | vấn đề → ví dụ → định nghĩa → kết quả → ứng dụng | §2.6; Ví dụ 11.10, 11.11; Định nghĩa 11.14; Mệnh đề 11.15 | `lec-11-topic-09` | — | 3 |
| 2 | `L11-2-11` | Bài tập: bước thật đầu của lượt thứ hai | kiểm tra (đề) | Bài tập 11.4 | `lec-11-topic-27` | — | 1,5 |
| 2 | `L11-2-12` | Bài tập: bước thật đầu của lượt thứ hai | kiểm tra (lời giải); câu nối sang mạch 3 | Bài tập 11.4; kết mục §2 | `lec-11-topic-27` | — | 2 |
| 3 | `L11-3-00` | 3. Tìm kiếm theo cây Monte Carlo | tiêu đề mạch | §3 | `lec-11-topic-11` | — | 0,5 |
| 3 | `L11-3-01` | Ví dụ: thuật toán rollout tại ô $\mathrm F$ | vấn đề → trực quan → ví dụ tính tay | §3.1; Ví dụ 11.12 | `lec-11-topic-11` | — | 3 |
| 3 | `L11-3-02` | Thuật toán rollout | thuật toán; chính sách rollout | Thuật toán 11.20 | `lec-11-topic-11` | — | 2 |
| 3 | `L11-3-03` | Tính chất cải thiện của rollout | trực quan → phát biểu → ứng dụng | Mệnh đề 11.21; Ví dụ 11.13 | `lec-11-topic-11` | — | 2,5 |
| 3 | `L11-3-04` | Ý tưởng chứng minh: tính chất cải thiện của rollout | ý tưởng chứng minh → kiểm tra | chứng minh Mệnh đề 11.21 | `lec-11-topic-11` | — | 2,5 |
| 3 | `L11-3-05` | Số mô phỏng của rollout | vấn đề → phát biểu → ví dụ số | Mệnh đề 11.22; Ví dụ 11.14 | `lec-11-topic-11` | — | 2,5 |
| 3 | `L11-3-06` | Quy tắc cận tin cậy trên | vấn đề → ví dụ → định nghĩa → bảo đảm | §3.2; Ví dụ 11.15; Định nghĩa 11.23; Định lý 11.24 | `lec-11-topic-12` | — | 3 |
| 3 | `L11-3-07` | Ví dụ: một vòng tìm kiếm theo cây tại $\mathrm F$, pha chọn | vấn đề → trực quan → ví dụ tính tay → định nghĩa | §3.3; Ví dụ 11.16; Định nghĩa 11.25 | `lec-11-topic-13` | — | 2,5 |
| 3 | `L11-3-08` | Ví dụ: một vòng tìm kiếm theo cây tại $\mathrm F$, mở rộng, mô phỏng, cập nhật ngược | ví dụ tính tay → ứng dụng (AlphaGo Zero) | Ví dụ 11.16; Nhận xét 11.28 | `lec-11-topic-13` (+14) | `mcts-bon-pha-slide.svg` | 2,5 |
| 3 | `L11-3-09` | Thuật toán tìm kiếm theo cây Monte Carlo với UCT | thuật toán | Thuật toán 11.26 | `lec-11-topic-13` | — | 2 |
| 3 | `L11-3-10` | Bảo đảm của UCT | vấn đề → phát biểu → ứng dụng | §3.4; Định lý 11.27 | `lec-11-topic-14` | — | 2,5 |
| 3 | `L11-3-11` | Bài tập: vòng tìm kiếm theo cây tiếp theo | kiểm tra (đề, lời giải fragment) | Bài tập 11.5 | `lec-11-topic-27` | — | 2,5 |
| 4 | `L11-4-00` | 4. Tối ưu kế hoạch dựa trên đạo hàm | tiêu đề mạch | §4 | `lec-11-topic-15` | — | 0,5 |
| 4 | `L11-4-01` | Ví dụ: xe trên đường ray | vấn đề (câu nối từ mạch 3) → trực quan → ví dụ dẫn nhập | kết mục §3; §4.1; Ví dụ 11.17 | `lec-11-topic-15` | — | 2 |
| 4 | `L11-4-02` | Bài toán tối ưu kế hoạch | định nghĩa → ví dụ tính tay | Định nghĩa 11.29; Ví dụ 11.18 | `lec-11-topic-15` (+16) | — | 2,5 |
| 4 | `L11-4-03` | Đạo hàm qua mô hình bằng truy hồi ngược | trực quan → phát biểu → ví dụ (bản thứ hai) | §4.2; Mệnh đề 11.30 | `lec-11-topic-16` | — | 3 |
| 4 | `L11-4-04` | Thuật toán tối ưu kế hoạch bằng hạ gradient | thuật toán → ứng dụng | Thuật toán 11.31; Ví dụ 11.19; Thuật toán 11.34 (một dòng) | `lec-11-topic-16` (+18) | — | 2,5 |
| 4 | `L11-4-05` | Điều khiển dự báo theo chân trời lùi | vấn đề → trực quan → ví dụ → định nghĩa → thuật toán | §4.3; Ví dụ 11.20; Định nghĩa 11.32; Thuật toán 11.33 | `lec-11-topic-17` | — | 3 |
| 4 | `L11-4-06` | Sai số mô hình tích lũy | vấn đề → trực quan → ví dụ → phát biểu | §4.5; Ví dụ 11.22; Mệnh đề 11.36 | `lec-11-topic-19` | `sai-so-tich-luy-slide.svg` | 2,5 |
| 4 | `L11-4-07` | Ví dụ: vòng hở và điều khiển dự báo với mô hình sai | ứng dụng | Ví dụ 11.23 | `lec-11-topic-19` | — | 1,5 |
| 4 | `L11-4-08` | Bài tập: kế hoạch hai bước từ $x_0=1$ | kiểm tra (đề, lời giải fragment) | Bài tập 11.6 | `lec-11-topic-27` | — | 2,5 |
| 5 | `L11-5-00` | 5. Học tăng cường phân cấp | tiêu đề mạch | §5 | `lec-11-topic-20` | — | 0,5 |
| 5 | `L11-5-01` | Ví dụ: hai tùy chọn trên mê cung hai phòng | vấn đề (câu nối từ mạch 4) → trực quan → ví dụ | kết mục §4; §5.1; Ví dụ 11.24 | `lec-11-topic-20` | — | 2,5 |
| 5 | `L11-5-02` | Tùy chọn và chính sách phân cấp | định nghĩa | Định nghĩa 11.38, 11.39 | `lec-11-topic-20` | — | 2 |
| 5 | `L11-5-03` | Ví dụ: mô hình của hai tùy chọn | trực quan → ví dụ tính tay | §5.2; Ví dụ 11.25 | `lec-11-topic-21` | `tuy-chon-hai-phong-slide.svg` | 2,5 |
| 5 | `L11-5-04` | Mô hình tùy chọn | định nghĩa → kết quả | Định nghĩa 11.40; Mệnh đề 11.41 | `lec-11-topic-21` | — | 2 |
| 5 | `L11-5-05` | Phương trình Bellman cho chính sách phân cấp | vấn đề → trực quan → phát biểu | Định lý 11.42 | `lec-11-topic-21` | — | 2,5 |
| 5 | `L11-5-06` | Ý tưởng chứng minh: phương trình Bellman cho chính sách phân cấp | ý tưởng chứng minh → kiểm tra | chứng minh Định lý 11.42 | `lec-11-topic-21` | — | 2,5 |
| 5 | `L11-5-07` | Lặp giá trị với tùy chọn | ví dụ tính tay → thuật toán → bảo đảm | §5.3; Ví dụ 11.26; Định lý 11.44; Thuật toán 11.45 | `lec-11-topic-22` | — | 3 |
| 5 | `L11-5-08` | Q-learning bán-MDP | vấn đề → trực quan → ví dụ tính tay → thuật toán | Nhận xét 11.43; Ví dụ 11.27; Thuật toán 11.46 | `lec-11-topic-22` (+21) | — | 2 |
| 5 | `L11-5-09` | Bài tập: mô hình tùy chọn khi trượt nhiều hơn | kiểm tra (đề, lời giải fragment) | Bài tập 11.7 | `lec-11-topic-27` | — | 2,5 |
| 6 | `L11-6-00` | 6. Tổng kết | tiêu đề mạch | §6 | `lec-11-topic-24` | — | 0,5 |
| 6 | `L11-6-01` | Bảng tổng kết | tổng kết (gộp bảng thứ ba của P4) | §6, Tóm tắt chương | `lec-11-topic-26` | — | 1,5 |
| 6 | `L11-6-02` | So sánh bốn cách dùng mô hình | bảng phương pháp (P4) | §6.1 | `lec-11-topic-24` | — | 1,5 |
| 6 | `L11-6-03` | Vấn đề trung tâm | trả lời câu hỏi trung tâm | §6.2 | `lec-11-topic-24` | — | 2 |
| 6 | `L11-6-04` | Bài tập: mô hình đếm và tùy chọn trên mê cung hai phòng | bài tập tổng hợp (đề) | Bài tập 11.10 | `lec-11-topic-27` | — | 1,5 |
| 6 | `L11-6-05` | Bài tập: mô hình đếm và tùy chọn trên mê cung hai phòng | lời giải | Bài tập 11.10 | `lec-11-topic-27` | — | 2 |
| 6 | `L11-6-06` | Câu hỏi tự kiểm tra | kiểm tra | §6.3 | `lec-11-topic-24` | — | 1 |
| 6 | `L11-6-07` | Bài tập về nhà | bài tập | Bài tập củng cố; `exercises.md` | `lec-11-topic-27` | — | 0,5 |
| 6 | `L11-6-08` | Tài liệu tham khảo | tài liệu | Hướng dẫn đọc thêm và tài liệu tham khảo | `lec-11-topic-28` | — | 0,5 |
| | | **60 trang** | | | | | **120** |

Thời lượng theo mạch: 9 + 30 + 28 + 20 + 22 + 11 = 120 phút; 30 phút còn lại của ba tiết dành chữa bài tập (P6). So với kế hoạch: mạch 1 thêm 1 phút (trang mục tiêu thứ hai); mạch 3 thêm 2 phút (trang Thuật toán 11.20, trang Mệnh đề 11.22); mạch 4 bớt 4 phút (bỏ trang entropy chéo, gộp đề và lời giải 11.6); mạch 6 thêm 1 phút.

### Số trang: 60 (trần P6) và lý do

Q15 đặt mục tiêu 58 (phương án QT3: bỏ trang entropy chéo, gộp đề và lời giải Bài tập 11.7). Storyboard áp cả hai cắt giảm đó (`L11-4-04` có một dòng "Cách khác:" cho Thuật toán 11.34; `L11-5-09` là một trang với lời giải fragment) và gộp thêm các cặp trang của kế hoạch: đề và lời giải 11.5, 11.6 thành một trang mỗi bài; hai trang ví dụ Dyna-Q thành một bảng ba hàng; Ví dụ 11.6 với Thuật toán 11.8 và Mệnh đề 11.9; Ví dụ 11.10 với Mệnh đề 11.15; Ví dụ 11.26 với Định lý 11.44; bảng tổng kết một trang. Ba trang phát sinh từ ghi chú đã duyệt và từ NT, không có trong phương án 58:

1. **`L11-3-02` Thuật toán rollout.** Ghi chú sau biên tập đổi Định nghĩa 11.20 thành Thuật toán 11.20 có lượt tính tay riêng (Q-B của `bang-phat-hien-I6.md`); NT-RL-2 đòi trang thuật toán sau lượt tính tay `L11-3-01`.
2. **`L11-3-05` Số mô phỏng của rollout.** Mệnh đề 11.22 và Ví dụ 11.14 là sản phẩm của mục tiêu 4 ("tính số mô phỏng đủ cho một xác suất chọn sai cho trước"); kế hoạch chỉ đặt một dòng "Lưu ý:" trên trang Mệnh đề 11.21, làm trang đó vượt 1,5 lần trần và trộn hai kết quả.
3. **`L11-1-04` Mục tiêu học tập (tiếp).** Bảy mục tiêu của ghi chú, giữ đủ động từ và đối tượng (NT11), sau khi rút chữ vẫn còn khoảng 200 âm tiết, vượt 120 (1,5 lần trần 80) nếu đặt trên một trang; chia 4 + 3 mục.

Thêm vào đó, `L11-2-02` (Định nghĩa 11.2) tách khỏi trang ví dụ mô hình `L11-2-01`, bù bằng việc gộp bảng tổng kết về một trang. Phương án 58 và 59 để điều phối viên chọn: câu hỏi C1.

**Bảng thứ ba của P4** (`Phương pháp | Giả thiết không được bỏ | Kết luận`) gộp vào bảng tổng kết `L11-6-01` (Q16, QT5). Lý do: các định lý hội tụ và cải thiện của bài (11.9, 11.21, 11.22, 11.27, 11.44) đã là hàng của bảng tổng kết với cột "Giả thiết không được bỏ" và công thức kết luận; bảng thứ ba sẽ lặp đúng các ô đó (NT13: không trùng lặp bảng).

## 4. Mật độ: ngoại lệ có lý do (NT17, NT18, NT-RL-7)

Số đo cuối của deck đã qua biên tập (giai đoạn III.5, hai vòng; bảng của điều phối viên `lec11/mat-do-cuoi.md` trong scratchpad), theo hàm đếm của `deck_lint.py --course rl-plan` (chữ trong bảng có tính; KaTeX và số trong ô bảng không tính; trang tiêu đề mạch đo dòng dẫn, trần 25). Trần: 60 cho trang thường và trang hai cột; 80 cho trang mục tiêu, nội dung, thuật toán, ý tưởng chứng minh, bảng tổng kết, bảng so sánh, trả lời câu hỏi trung tâm, bài tập về nhà, tài liệu tham khảo; bìa không áp. Chữ thân bài từ `0.75em` (NT-RL-7), không thu nhỏ chữ; lời giải thích chuyển sang ghi chú diễn giả. **Không trang nào đạt 1,5 lần trần**; lớn nhất `L11-1-03` 119/80 = 1,49, rồi `L11-2-01`, `L11-3-06`, `L11-3-10` 89/60 = 1,48. "Giữ 60 trang" không dùng làm lý do.

**Ngoại lệ còn lại (28 trang).** Cột "storyboard" là số của bản storyboard sau cổng (ước lượng trên chuỗi dự kiến); "cuối" là số đo trên deck.

| Trang | Trần | Storyboard | Cuối | Tỉ lệ | Lý do (NT17) |
|---|---:|---:|---:|---:|---|
| `L11-1-02` | 60 | 75 | 75 | 1,25 | bốn "Nhắc lại:" đủ giả thiết, kết luận (NT9, NT2) cùng "Ký hiệu:" có $\mathcal S^+$, $v_*$, $q_*$ (NT9) |
| `L11-1-03` | 80 | 120 | 119 | 1,49 | mục tiêu 1–4 giữ đúng nghĩa ghi chú (NT11, NT17) |
| `L11-1-04` | 80 | 90 | 97 | 1,21 | mục tiêu 5–7 giữ đúng nghĩa ghi chú, có tên tiếng Anh option, SMDP (NT11, NT21) |
| `L11-1-06` | 60 | 55 | 65 | 1,08 | ba dòng ngữ cảnh (P5): dữ kiện mê cung, khung chung, kết quả Q-learning có số (NT14) |
| `L11-1-07` | 60 | 62 | 61 | 1,02 | hộp "Câu hỏi:" giữ nguyên câu hỏi trung tâm của ghi chú (NT11) |
| `L11-2-01` | 60 | 84 | 89 | 1,48 | câu hỏi của mạch (NT13), Ví dụ 11.2, "Trực quan." (NT8), Định nghĩa 11.1 đủ ba vế (NT2) |
| `L11-2-02` | 60 | 62 | 66 | 1,10 | "Trực quan.", ví dụ và Định nghĩa 11.2 đủ hai vế (NT8, NT2) |
| `L11-2-03` | 60 | 58 | 77 | 1,28 | "Trực quan." của hai loại bất định đặt trước Mệnh đề 11.5 (NT8), định nghĩa và mệnh đề đủ giả thiết (NT2) |
| `L11-2-05` | 60 | 75 | 86 | 1,43 | đề Bài tập 11.2 giữ nguyên câu chữ (NT17, NT24) |
| `L11-2-07` | 60 | 64 | 69 | 1,15 | giới hạn của Q-planning (NT-RL-3), "Trực quan." (NT8), lượt tính tay ba hàng (NT-RL-2) |
| `L11-2-09` | 60 | 72 | 87 | 1,45 | Ví dụ 11.8, "Trực quan." lạc quan/bi quan đứng cạnh Định nghĩa 11.12 (NT8), Ví dụ 11.9 (NT-RL-2) |
| `L11-2-10` | 60 | 83 | 88 | 1,47 | Mệnh đề 11.15(b) đủ giả thiết, có định nghĩa $\bar y$, $Q_k$ (NT2, NT9) cùng "Trực quan." (NT8) |
| `L11-2-12` | 60 | 57 | 64 | 1,07 | lời giải (b) giữ bốn giả thiết của Mệnh đề 11.9 (NT2) cùng câu nối sang mạch 3 (NT13) |
| `L11-3-06` | 60 | 85 | 89 | 1,48 | định nghĩa và định lý của công cụ cầu nối có "Giả thiết:", "Bảo đảm:" (NT5), "Trực quan." gộp Ví dụ 11.15 (NT8), nhắc lại $N(a)$, $\bar r(a)$ (NT9) |
| `L11-3-07` | 60 | 71 | 65 | 1,08 | giới hạn của rollout (NT-RL-3), "Trực quan." (NT8), Định nghĩa 11.25 trên trang dùng chỉ số (NT9) |
| `L11-3-10` | 60 | 85 | 89 | 1,48 | định lý hai phần đủ giả thiết và phạm vi (NT2), "Trực quan." (NT8) |
| `L11-4-01` | 60 | 62 | 66 | 1,10 | câu nối từ mạch 3 (NT13, NT-RL-3), dữ kiện liệt kê (NT14), "Trực quan." |
| `L11-4-06` | 60 | 56 | 65 | 1,08 | Ví dụ 11.22 có dãy năm giá trị $e_k$ (NT25), "Trực quan." có tên compounding error (NT21), Mệnh đề 11.36 đủ giả thiết |
| `L11-5-01` | 60 | 56 | 62 | 1,03 | giới hạn của mạch 4 có số (NT13, NT-RL-3), "Trực quan.", Ví dụ 11.24 |
| `L11-5-02` | 60 | 75 | 76 | 1,27 | hai định nghĩa liền nhau, mỗi thành phần một dòng (VP11) |
| `L11-5-05` | 60 | 69 | 72 | 1,20 | kết quả chính giữ đủ năm giả thiết (NT2) cùng "Trực quan." (NT8) |
| `L11-5-09` | 60 | 76 | 69 | 1,15 | đề Bài tập 11.7 giữ nguyên câu chữ cùng lời giải (NT17, NT24) |
| `L11-6-02` | 80 | 70 | 97 | 1,21 | bảng so sánh bốn phương pháp, có phân loại nền/thời điểm quyết định (NT-RL-4) và điều kiện dừng đúng Thuật toán 11.33 |
| `L11-6-03` | 80 | 107 | 111 | 1,39 | câu trả lời có điều kiện cho cả bài (NT15), bốn ý và dòng kết |
| `L11-6-04` | 60 | 89 | 72 | 1,20 | đề Bài tập 11.10 (a)–(d) giữ nguyên câu chữ (NT17, NT24) |
| `L11-6-05` | 60 | 66 | 71 | 1,18 | đề câu (e) giữ nguyên câu chữ cùng lời giải (NT17, NT24) |
| `L11-6-06` | 60 | 75 | 74 | 1,23 | bốn câu của §6.3, mỗi câu kiểm một giả thiết hoặc phân biệt (NT15, NT-RL-9) |
| `L11-6-08` | 80 | 70 | 86 | 1,07 | trang tài liệu tham khảo, nguồn có mục (D-10; NT15) |

Lý do chung của phần tăng so với storyboard: các phát hiện của năm vai rà deck (D-1 … D-12 trong `lec11/bang-phat-hien-III5.md`) thêm dòng "Trực quan." trước phát biểu (NT8), định nghĩa ký hiệu trước khi dùng (NT9: $\mathcal S^+$, $v_*$, $q_*$, $\bar y$, $Q_k$, $N(a)$, $\bar r(a)$), tên tiếng Anh ở lần đầu (NT21, VP2), số hiệu công thức trong câu dẫn (D-3), phân loại nền/thời điểm quyết định ở bảng so sánh (NT-RL-4) và tài liệu có mục (D-10).

**Trang theo trần 80 không vượt** (thuật toán, ý tưởng chứng minh, mục tiêu, nội dung, bảng, bài tập về nhà): `L11-1-05` 52, `L11-2-06` 79, `L11-2-08` 56, `L11-3-02` 76, `L11-3-04` 47, `L11-3-09` 80, `L11-4-04` 75, `L11-4-05` 78, `L11-5-06` 67, `L11-5-07` 57, `L11-5-08` 80, `L11-6-01` 79, `L11-6-07` 51. Trang hai cột đều ≤ 60 trừ `L11-1-06` (65) và `L11-4-06` (65), có lý do ở bảng trên.

Trang thuật toán giữ ≤ 6 dòng (`deck_lint` báo 0 `LINES6`); không giả mã quá 8 dòng.

**Rút chữ (NT, mục 3 "Rút chữ để hạ mật độ").** Phải giữ: "$C$ cố định trước" (11.5); "xác định ở mọi cặp", "mô hình cố định" (11.9); "phần thưởng $0$", "đồng khả năng", "cùng kỳ vọng, phương sai $1$", "$k$ mẫu độc lập" (11.15(b), trên `L11-2-10`); "$q_{\pi_0}$ chính xác" (11.21); "$m$ chọn trước", "không cắt" (11.22); "mô hình đúng", "bài toán cắt ở độ sâu $D$", "$c_{\mathrm{ucb}}=\sqrt2\,D$", "hành động tối ưu duy nhất", "không được chứng minh cho Thuật toán 11.26" (11.27(a)); "phần thưởng không âm", "lợi tức trong $[0,1]$" (11.27(b)); "chuỗi hành động cố định" (11.36); "kết thúc với xác suất $1$", "$\beta_\omega$ chỉ phụ thuộc trạng thái", "$\mu$ chỉ phụ thuộc trạng thái" (11.42); "mô hình tùy chọn đúng", "$\Omega(s)\supseteq\mathcal A(s)$" (11.44).

## 5. Khuôn bảng cố định (NT-RL-5)

| Khuôn | Cột | Trang |
|---|---|---|
| T1 cập nhật một cặp | cặp · mục tiêu · sai lệch · giá trị mới | `L11-2-06`, `L11-2-07`, `L11-2-09`, `L11-2-12` (lời giải), `L11-5-08`, `L11-6-05` (câu (e)) |
| T2 cạnh gốc của cây | cạnh · $N(\mathrm F,a)$ · $W(\mathrm F,a)$ · $\bar Q(\mathrm F,a)$ · $\sqrt{\ln N(\mathrm F)/N(\mathrm F,a)}$ · chỉ số | `L11-3-07` ($\ln 8$), `L11-3-11` ($\ln 9$; hai cột cuối là fragment) |
| T3 kế hoạch của xe | kế hoạch $(u_0;\,u_1)$ · $x_1$; $x_2$ · $J$ | `L11-4-01`, `L11-4-02`, `L11-4-04`, `L11-4-08` (lời giải) |
| T4 quỹ đạo của xe | quỹ đạo · $x_0$ · $x_1$ · $x_2$ · $x_3$ | `L11-4-05`, `L11-4-07` |
| T5 lặp giá trị | cách · $k$ · $V_k(\mathrm K)$ · $V_k(\mathrm F)$ · $V_k(\mathrm B)$ · $V_k(\mathrm A)$ | `L11-5-07` (hàng tùy chọn $k=2$ và hàng một bước $k=6$; `L11-5-01` nêu $V_6(\mathrm A)$ bằng chữ) |

Dữ kiện bài tập dùng cùng khuôn với ví dụ dẫn nhập: Bài tập 11.4 ↔ T1 của `L11-2-07`; Bài tập 11.5 ↔ T2 của `L11-3-07`; Bài tập 11.6 ↔ T3 của `L11-4-02`; Bài tập 11.10(e) ↔ T1 của `L11-5-08`.

## 6. Hình (NT25), kỹ thuật (NT7), nhãn (NT19, P3)

**Hình trên trang chiếu.** Chỉ SVG trong `2627-1/img/lec-11/`; không dùng lại 11 SVG của Bài 11 cũ; không raster. Hình ghi chú có cỡ chữ 15–22 đơn vị trong `viewBox` rộng 860–1000 (đo bằng grep 2026-11-19), nên khi đặt trên trang chiếu cạnh chữ (bề rộng hiển thị khoảng 480–600 px trong khung 1280 × 720) chữ còn khoảng 10–15 px, dưới 16 px. **Cả năm hình dùng trên deck cần bản `-slide.svg`** cùng dữ liệu (không sửa SVG của ghi chú); người viết deck vẽ bằng script trong `/data/tqlong/lectures/tools/courses/rl-plan/2627-1/img/lec-11/` (quyết định C6). Bố cục hai cột dùng lớp có sẵn của `lecture-course.css`: `.grid2` (1fr 1fr), `.grid3`, `.grid2.wide-right` (2fr 3fr) (quyết định C7); `.grid2` xếp một cột ở màn hẹp, nên chữ trên hình phải ≥ 16 px cả ở 390 × 844:

| Hình ghi chú | Bản trang chiếu | Trang | Bố cục và yêu cầu |
|---|---|---|---|
| `me-cung-hai-phong.svg` (chữ 20–34) | `me-cung-hai-phong-slide.svg` | `L11-1-06` | `.grid2`, cột phải, bề rộng hiển thị khoảng 520 px; nhãn ô và $v_*$ ≥ 16 px ở kích thước đó; giữ tường $\mathrm B$–$\mathrm C$, cửa $\mathrm F$–$\mathrm K$, $v_*$ trong ô (mọi số $v_*$ có trong chữ ở `L11-1-06` hoặc ghi chú diễn giả; trang sau dùng $v_*(\mathrm F)=0{,}8566$, $v_*(\mathrm A)=0{,}6604$ nêu lại trong chữ, NT25) |
| `kien-truc-dyna.svg` (chữ 20–24) | `kien-truc-dyna-slide.svg` | `L11-2-08` | `.grid2`, cột phải khoảng 560 px, `viewBox` gần vuông; nhãn bước (d), (e), (f) trùng chữ của thuật toán |
| `mcts-bon-pha.svg` (chữ 15–24) | `mcts-bon-pha-slide.svg` | `L11-3-08` | dải ngang toàn bề rộng nội dung (khoảng 1100 × 360 px), bốn khung; chữ nhỏ nhất ≥ 16 px; mọi số trên hình ($1{,}7558$; $0{,}729$; $2$; $1{,}0428$; $0{,}5214$; $9$; $0$) có trong chữ trên `L11-3-07` hoặc `L11-3-08` |
| `sai-so-tich-luy.svg` (chữ 19–21) | `sai-so-tich-luy-slide.svg` | `L11-4-06` | `.grid2`, cột phải khoảng 560 px; trục và nhãn ≥ 16 px; năm giá trị $e_k$ có trong dòng ví dụ của trang |
| `tuy-chon-hai-phong.svg` (chữ 20–40) | `tuy-chon-hai-phong-slide.svg` | `L11-5-03` | `.grid2`, cột phải khoảng 560 px; mọi hệ số $p$, $r$ trên hình có trong chữ của trang |

Bản `-slide-narrow.svg` chỉ vẽ khi kiểm 390 × 844 thấy chữ dưới 16 px hoặc hình tràn (NT25); kết quả ghi vào `review-log.md`. Không dùng trên deck: `cau-truc-chuong.svg` (thay bằng dòng khung ở `L11-1-06`), `cap-nhat-ky-vong-va-mau.svg` (`L11-2-10` dùng bảng số), `xe-tren-duong-ray.svg` (`L11-4-07` dùng bảng T4 với đúng các số đó, cổng); ba hình này chỉ ở ghi chú. Mỗi `<img>` có `alt` cụ thể nêu dữ liệu; chú thích nêu dữ liệu, không "minh họa".

**Kỹ thuật** (NT7; danh sách kỹ thuật đã giới thiệu trong deck):

| Kỹ thuật | Xử lý | Trang |
|---|---|---|
| bất đẳng thức Hoeffding | đã có ở Bài 06 (Mệnh đề 06.26): dòng "Nhắc lại:" cùng tên | `L11-3-05` |
| bất đẳng thức hợp (union bound) | nhắc lại một câu trong ghi chú diễn giả (Bài tập 11.8, tự làm) | `L11-3-05` |
| hiệu hai cực đại (Bổ đề 04.23) và ánh xạ co (Định lý 04.5) | nhắc lại trong ghi chú diễn giả, nơi nêu chứng minh của Định lý 11.44 | `L11-5-07` |
| tách lợi tức tại thời điểm dừng $\tau$ | dòng "Kỹ thuật." trên trang ý tưởng chứng minh (mẹo dùng trong một chứng minh) | `L11-5-06` |
| truy hồi ngược theo quy tắc dây chuyền | là nội dung của Mệnh đề 11.30, không phải trang "Kỹ thuật." | `L11-4-03` |

**Nhãn** (NT19, P3): "Kết luận:" cho kết quả tất định (11.5, 11.15, 11.21, 11.30, 11.36, 11.41, 11.42); "Bảo đảm:" cho kết quả hội tụ hoặc xác suất (11.9, 11.22, 11.24, 11.27, 11.44); "Đầu vào:", "Đầu ra:" cho trang thuật toán; "Cách khác:" cho dòng entropy chéo (`L11-4-04`); "Trực quan.", "Ý nghĩa:", "Diễn giải:", "Lưu ý:", "Nhắc lại:", "Ký hiệu:", "Giả thiết:", "Câu hỏi:", "Lời giải:", "Chứng minh.", "Ý tưởng chứng minh.", "Kỹ thuật.". Số hiệu ghi chú trên mặt trang một lần mỗi trang (NT5). Không "Nhu cầu:", không "Đáp án".

**Kết quả chính và trang ý tưởng chứng minh** (NT4, NT6; Q16): kết quả chính có trang riêng là Mệnh đề 11.21 (`L11-3-04`) và Định lý 11.42 (`L11-5-06`). Kết quả phụ có dòng "Chứng minh." trên trang phát biểu: 11.5 (tổng Bernoulli), 11.41 ($\tau\ge1$). Kết quả phụ có lý do chứng minh trong ghi chú diễn giả (NT6 cho phép; chuyển để trang đạt trần, cổng): 11.30 (quy nạp ngược bằng quy tắc dây chuyền), 11.36 ($e_{j+1}\le Le_j+\bar e$), 11.9 (Định lý 06.21 áp cho MDP của mô hình), 11.15 (trung bình mẫu, khai triển quanh kỳ vọng chung), 11.22 (Hoeffding một phía cho $2m$ biến), 11.27(b) (hiệu lợi tức sau bước $D$), 11.44 (Bổ đề 04.23 và Mệnh đề 11.41). Kết quả dẫn nguồn, không chứng minh (11.24; 11.27(a)): ghi chú diễn giả nêu nguồn và ý tưởng một câu như ghi chú (NT5).

## 7. Mục từng trang

Mỗi mục ghi: vị trí và bước hành trình (NT8); lý do tồn tại, nhu cầu lấp; liên kết trước và sau; mục tiêu học tập (đánh số theo ghi chú, mục "Mục tiêu học tập"); nguồn trong ghi chú (mục, khối, `note-topic-id`); nội dung mặt trang dự kiến (chuỗi trong ngoặc kép là câu lên mặt trang, đã sửa bằng `no-ai-slop` Edit); mật độ ước lượng; hình và phút; quyết định; ý chính của ghi chú diễn giả. Mọi quyết định là `thêm`: deck dựng mới, không có trang nguồn (P1, ngoại lệ Bài 11).

### Mạch 1. Bài toán lập kế hoạch với mô hình học được (7 trang, 9 phút)

Hành trình của câu hỏi trung tâm: vấn đề (`L11-1-06`: bốn mẫu chuyển bị Q-learning bỏ, có số) → câu hỏi (`L11-1-07`). Không khái niệm mới ngoài khung chung (NT9: các trang tổng quan viết bằng lời).

#### `L11-1-01` Lập kế hoạch dựa trên mô hình (bìa)
- **Vị trí, bước:** trang 1 của mạch 1; bìa, là trang tiêu đề của mạch mở đầu (`AGENTS.md` "Trang tiêu đề mạch"); ngoài hành trình khái niệm.
- **Lý do tồn tại:** tên bài như ghi chú, luận điểm một câu có điều kiện (NT11, NT-RL-8).
- **Liên kết:** trước —; sau `L11-1-02`.
- **Mục tiêu:** định hướng cả bảy mục tiêu.
- **Nguồn:** tiêu đề ghi chú; §1.1; Tóm tắt chương (câu cuối: "Các bảo đảm hội tụ và cải thiện của chương nói về MDP của mô hình; sai số do mô hình chỉ được chặn cho một ô của bảng đếm … và cho dự báo vòng hở"); `lec-11-topic-02`.
- **Mặt trang:**
  - dòng học phần "Học tăng cường"; "Bài 11"; `h1` "Lập kế hoạch dựa trên mô hình".
  - "Khi mô hình cố định, các bảo đảm hội tụ và cải thiện của lập kế hoạch đúng trên bài toán mà mô hình định nghĩa; sai số của mô hình chỉ được chặn cho một ô của bảng đếm và cho dự báo vòng hở." (46)
  - "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội"; "Năm học 2026–2027, học kỳ 1". Không tên giảng viên, không chữ viết tắt (NT9).
- **Mật độ:** khoảng 68 âm tiết (luận đề 46; dòng học phần, số bài, đơn vị, năm học 22), 0 công thức, 1 hộp chữ một câu. Bìa không thuộc trần trang nội dung. **Số đo cuối** (`deck_lint`, sau III.5): 79 âm tiết, trần không áp.
- **Sau biên tập (2026-11-19):** phụ đề "Dyna, tìm kiếm theo cây, tối ưu kế hoạch, tùy chọn"; luận điểm như §7.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — bìa theo NT11, NT-RL-8.
- **Ghi chú diễn giả:** "bài toán mà mô hình định nghĩa" là MDP có động lực $\hat p$; ví dụ: Q-planning hội tụ tới $\hat q_*$ (Mệnh đề 11.9), rollout cải thiện giá trị trên MDP của mô hình (Mệnh đề 11.21, phần Phạm vi); chỉ hai chỗ sai số mô hình được chặn: một ô của bảng đếm (Mệnh đề 11.5) và dự báo vòng hở (Mệnh đề 11.36). Nguồn: ghi chú §1.1, Tóm tắt chương.

#### `L11-1-02` Tiên quyết và quy ước
- **Vị trí, bước:** trang 2; nhắc lại (NT9, NT11).
- **Lý do tồn tại:** bốn kết quả của Bài 01, 03, 04, 06 dùng ngay ở mạch 1–3; các nhắc lại khác đặt tại chỗ dùng: Robbins–Monro (Định nghĩa 06.19) ở `L11-2-06`; Hoeffding (Mệnh đề 06.26) ở `L11-3-05`; bài toán chọn lặp lại một bước (Định nghĩa 01.16) ở `L11-3-06`; lặp giá trị (Định lý 04.32, Thuật toán 04.28) ở `L11-5-01`; phương trình Bellman kỳ vọng (Định lý 03.21) ở `L11-5-05`; Bổ đề 04.23 và Định lý 04.5 ở `L11-5-07`.
- **Liên kết:** trước `L11-1-01`; sau `L11-1-03`.
- **Mục tiêu:** 1–7 (ký hiệu chung).
- **Nguồn:** Kiến thức tiên quyết, Bảng ký hiệu, Quy ước đọc; `lec-11-topic-01`.
- **Mặt trang:** "Nhắc lại:" bốn mục:
  1. "Mô hình cho trạng thái kế và phần thưởng, hoặc phân phối của chúng, khi biết trạng thái và hành động (Định nghĩa 01.14)."
  2. "Q-learning có mục tiêu $R+\gamma\max_{a'}Q(S',a')$; khi mọi cặp được cập nhật vô hạn lần và bước học thỏa Robbins–Monro, $Q_t\to q_*$ hầu chắc chắn (Định lý 06.21)."
  3. công thức hiển thị $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s')$, $v_\pi(s)=\sum_a\pi(a\mid s)\,q_\pi(s,a)$ (Mệnh đề 03.22, 03.23; ngắt bằng `aligned` nếu tràn ở 390 px).
  4. "Với $\pi$, $\pi'$ Markov dừng, $\pi'$ xác định, nếu $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$ thì $v_{\pi'}\ge v_\pi$ (Định lý 04.13)."
  Rồi "Ký hiệu: quá trình quyết định Markov (MDP) hữu hạn, $\gamma\in[0,1)$; $\hat p$, $\hat r$ là mô hình học được; $\mathbb E_\pi$ lấy theo $\pi$ và động lực thật."
- **Mật độ:** khoảng 75 âm tiết, 5 dòng, 1 công thức hiển thị: ngoại lệ (mục 4). **Số đo cuối** (`deck_lint`, sau III.5): 75 âm tiết, trần 60, tỉ lệ 1,25.
- **Sau biên tập (2026-11-19):** nhắc lại thứ nhất đứng trên dòng nhãn "Nhắc lại:", ba mục sau là danh sách bắt đầu từ 2; nhắc lại cải thiện chính sách viết "nếu … thì"; "Ký hiệu:" thêm $\mathcal S^+$ (gồm trạng thái kết thúc), $v_*$, $q_*$; điều kiện Robbins–Monro ở ghi chú diễn giả.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — trang tiên quyết theo NT11; bốn nhắc lại theo mục Kiến thức tiên quyết của ghi chú.
- **Ghi chú diễn giả:** giả thiết nền của Nhận xét 06.20 (MDP hữu hạn, động lực dừng, phần thưởng bị chặn, mẫu có phân phối $p(\cdot,\cdot\mid s,a)$); $R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$, giá trị trạng thái kết thúc bằng $0$ cả trong bảng và mô hình; tương ứng Sutton và Barto: $c_{\mathrm{ucb}}$ là $c$ của (2.10), $\ell(s,a)$ là $\tau$ của Dyna-Q+; tương ứng *Học máy thống kê*: $v_\pi$ là $V^\pi$, $p(s'\mid s,a)$ là $T(s,a,s')$.

#### `L11-1-03` Mục tiêu học tập
- **Vị trí, bước:** trang 3; mục tiêu 1–4 (mạch 2–3).
- **Lý do tồn tại:** giữ đủ bảy mục tiêu của ghi chú (NT11); chia hai trang vì bảy mục đầy đủ của ghi chú có khoảng 250 âm tiết, sau khi rút chữ vẫn còn khoảng 200, vượt 120 (1,5 lần trần 80) nếu đặt trên một trang.
- **Liên kết:** trước `L11-1-02`; sau `L11-1-04`.
- **Mục tiêu:** 1–4.
- **Nguồn:** Mục tiêu học tập 1–4; `lec-11-topic-01`.
- **Mặt trang:**
  - bốn mục đánh số 1–4:
  - "Phân biệt mô hình phân phối và mẫu, lập kế hoạch nền và tại thời điểm quyết định; ước lượng mô hình bằng tần suất, tách hai loại bất định, tính độ lệch chuẩn ước lượng." (36)
  - "Tính tay một bước thật của Dyna-Q; nêu điều kiện Q-planning hội tụ; giải thích vì sao mô hình sai cần thưởng thăm dò." (24)
  - "So sánh cập nhật kỳ vọng và mẫu về chi phí, sai số khi ngân sách dưới hệ số phân nhánh." (21)
  - "Phát biểu tính chất cải thiện của rollout cùng giả thiết; tính số mô phỏng cho xác suất chọn sai, chỉ số cận tin cậy trên; thực hiện một vòng tìm kiếm theo cây Monte Carlo qua bốn pha." (39)
- **Mật độ:** 120 âm tiết (trước sửa theo cổng 111), 4 mục, mỗi mục ≤ 2 dòng hiển thị: ngoại lệ NT17 "trang mục tiêu giữ đúng nghĩa ghi chú" (trần 80, 1,5 lần là 120). Mọi năng lực của mục tiêu 1 và 4 có động từ trên mặt trang (cổng, NT11); chỉ rút chữ, không bỏ năng lực ("độ lệch chuẩn" của tần suất ước lượng, "bốn pha" của tìm kiếm theo cây Monte Carlo). **Số đo cuối** (`deck_lint`, sau III.5): 119 âm tiết, trần 80, tỉ lệ 1,49.
- **Sau biên tập (2026-11-19):** chữ theo ghi chú: "độ lệch chuẩn của $\hat p$", "ước lượng $\hat p$", "đủ cho xác suất chọn sai cho trước" (rồi bỏ "đủ"), "dưới hệ số phân nhánh", "qua bốn pha"; tên "Monte Carlo tree search, MCTS" đặt ở `L11-3-09`.
- **Hình, phút:** —; 1.
- **Quyết định:** thêm — NT11.
- **Ghi chú diễn giả:** sản phẩm kiểm được của từng mục: $\operatorname{Var}\hat p=p(1-p)/C$ với $C=2,5,50$; $Q(\mathrm F,\rightarrow)=0{,}225$ sau lượt thứ nhất; $\sqrt{(b-1)/(bk)}=0{,}3146$ với $b=100$, $k=10$; $m=70$, chỉ số $1{,}4481$, chỉ số UCT $1{,}7558$.

#### `L11-1-04` Mục tiêu học tập
- **Vị trí, bước:** trang 4; mục tiêu 5–7 (mạch 4–6); tiêu đề lặp vì trang nối tiếp.
- **Lý do tồn tại:** như `L11-1-03`.
- **Liên kết:** trước `L11-1-03`; sau `L11-1-05`.
- **Mục tiêu:** 5–7.
- **Nguồn:** Mục tiêu học tập 5–7; `lec-11-topic-01`.
- **Mặt trang:** ba mục đánh số 5–7 (thẻ `<ol start="5">`):
  5. "Tính gradient của chi phí kế hoạch qua mô hình khả vi bằng truy hồi ngược; tính một bước hạ gradient và một vòng entropy chéo; mô tả điều khiển dự báo và chặn sai số tích lũy." (35)
  6. "Định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của một tùy chọn; viết phương trình Bellman bán-MDP; thực hiện lặp giá trị và một cập nhật Q-learning với tùy chọn." (33)
  7. "Với một bài toán cụ thể, chọn cách dùng mô hình phù hợp và kiểm các giả thiết mà bảo đảm của cách đó cần." (22)
- **Mật độ:** 90 âm tiết, 3 mục, mỗi mục ≤ 2 dòng hiển thị: ngoại lệ NT17 "trang mục tiêu giữ đúng nghĩa ghi chú" (trần 80). **Số đo cuối** (`deck_lint`, sau III.5): 97 âm tiết, trần 80, tỉ lệ 1,21.
- **Sau biên tập (2026-11-19):** thêm tên tiếng Anh option, semi-Markov decision process (SMDP); ghi chú diễn giả bỏ câu về trạng thái văn bản (VP19).
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT11.
- **Ghi chú diễn giả:** sản phẩm: gradient $(8;\,4)$ hai cách, $J$ từ $8$ xuống $2{,}88$; luật $u=-0{,}6x$; $e_k\le\bar e(L^k-1)/(L-1)$; $\rho=0{,}8780$, $V_2(\mathrm A)=0{,}6604$; mục tiêu 7 kiểm bằng Bài tập 11.9–11.11 và bài tập tổng hợp 11.10. Phương pháp entropy chéo chỉ có một dòng trên trang chiếu; lượt tính của nó ở Ví dụ 11.21 của ghi chú.

#### `L11-1-05` Nội dung
- **Vị trí, bước:** trang 5; nội dung.
- **Lý do tồn tại:** bản đồ sáu mạch, số trùng `#/N` và trang tiêu đề mạch (NT11).
- **Liên kết:** trước `L11-1-04`; sau `L11-1-06`.
- **Mục tiêu:** —.
- **Nguồn:** §1–§6 (tên mục); `lec-11-topic-03`.
- **Mặt trang:** danh sách đánh số, mỗi mục là liên kết `#/k`:
  1. Bài toán lập kế hoạch với mô hình học được (`#/1`)
  2. Tính bất định của môi trường và lập kế hoạch nền (`#/2`)
  3. Tìm kiếm theo cây Monte Carlo (`#/3`)
  4. Tối ưu kế hoạch dựa trên đạo hàm (`#/4`)
  5. Học tăng cường phân cấp (`#/5`)
  6. Tổng kết (`#/6`)
  Dòng cuối: "Đọc trước: Sutton và Barto (2018), Chương 8, §2.7, §17.2."
- **Mật độ:** khoảng 45 âm tiết, 7 dòng (sáu mạch và dòng đọc trước): ngoại lệ số dòng (mục 4), như trang nội dung của deck 10. Nếu điều phối viên không chấp nhận, dòng đọc trước chuyển vào ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 52 âm tiết, trần 80, tỉ lệ 0,65.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT11; tên mục theo ghi chú (mục 2 của tệp này).
- **Ghi chú diễn giả:** bốn mạch nội dung là bốn cách dùng mô hình (§6.1): lập kế hoạch nền; tìm kiếm tại thời điểm quyết định với hành động rời rạc, rồi liên tục; tùy chọn; mạch 6 so sánh bốn cách trên cùng các tiêu chí.

#### `L11-1-06` Ngữ cảnh
- **Vị trí, bước:** trang 6; trang bổ sung của P5, gộp "Ngữ cảnh" với trang khung chung (Q16); bước `vấn đề` (ví dụ dẫn nhập) của câu hỏi trung tâm: làm cụ thể vế "mỗi mẫu thật chỉ dùng một lần".
- **Lý do tồn tại:** đặt ví dụ xuyên suốt thứ nhất và khung chung trước câu hỏi trung tâm; con số $0{,}5$ cho câu hỏi một điểm xuất phát đo được.
- **Liên kết:** trước `L11-1-05`; sau `L11-1-07` (câu hỏi trung tâm hỏi về chính con số này).
- **Mục tiêu:** 1, 2 (dữ kiện dùng lại).
- **Nguồn:** Ví dụ 11.1; đoạn sau Ví dụ 11.1 (lượt thật thứ nhất, Q-learning); §1.2 (khung, tối ưu bằng đạo hàm bỏ khâu giá trị); `lec-11-topic-02`, `lec-11-topic-03`.
- **Mặt trang:** hai cột; cột trái ba dòng:
  - "Mê cung hai phòng (Ví dụ 11.1): đi đúng với xác suất $0{,}8$, trượt và ở yên với xác suất $0{,}2$; phần thưởng $+1$ khi vào $\mathrm Z$; $\gamma=0{,}9$."
  - "Khung chung: mô hình sinh kinh nghiệm mô phỏng, cập nhật trên đó cho giá trị và chính sách; tối ưu bằng đạo hàm bỏ khâu giá trị."
  - "Q-learning với $Q\equiv0$, $\alpha=0{,}5$, sau năm bước thật của lượt thứ nhất chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$; bốn mẫu chuyển còn lại bị bỏ."
  Cột phải: hình `me-cung-hai-phong-slide.svg` (tường $\mathrm B$–$\mathrm C$, cửa $\mathrm F$–$\mathrm K$, $v_*$ trong ô); `alt` nêu bố cục và tám giá trị $v_*$.
- **Mật độ:** khoảng 55 âm tiết, 3 dòng, 0 công thức hiển thị. Dòng cuối là con số (NT18). **Số đo cuối** (`deck_lint`, sau III.5): 65 âm tiết, trần 60, tỉ lệ 1,08.
- **Sau biên tập (2026-11-19):** dòng khung: "mô hình sinh mẫu chuyển, cập nhật trên các mẫu đó cho giá trị và chính sách; tối ưu bằng đạo hàm bỏ khâu giá trị"; dòng Q-learning kết bằng "bốn mẫu còn lại cho mục tiêu $0$, không được dùng lại".
- **Hình, phút:** `me-cung-hai-phong-slide.svg`; 2,5.
- **Quyết định:** thêm — P5 (Q16, QT7); `cau-truc-chuong.svg` không dùng, thay bằng dòng khung.
- **Ghi chú diễn giả:** bố cục: hàng trên $\mathrm A$, $\mathrm B$, $\mathrm C$, $\mathrm D$, hàng dưới $\mathrm E$, $\mathrm F$, $\mathrm K$, $\mathrm Z$, lượt bắt đầu ở $\mathrm A$; năm mẫu chuyển $(\mathrm A,\rightarrow,0,\mathrm A)$, $(\mathrm A,\rightarrow,0,\mathrm B)$, $(\mathrm B,\downarrow,0,\mathrm F)$, $(\mathrm F,\rightarrow,0,\mathrm K)$, $(\mathrm K,\rightarrow,+1,\mathrm Z)$; vì sao bốn mục tiêu đầu bằng $0$; $v_*(d)$: $0{,}9756$; $0{,}8566$; $0{,}7522$; $0{,}6604$ theo khoảng cách $1$–$4$; trên mê cung Dyna của Sutton và Barto (2018, Ví dụ 8.1, tr. 164), không lập kế hoạch cần khoảng 25 lượt, 50 cập nhật lập kế hoạch mỗi bước thật cần khoảng 3 lượt.

#### `L11-1-07` Vấn đề trung tâm
- **Vị trí, bước:** trang 7; vấn đề (NT11).
- **Lý do tồn tại:** một hộp "Câu hỏi:" duy nhất nêu đúng câu hỏi trung tâm của ghi chú.
- **Liên kết:** trước `L11-1-06` (con số $0{,}5$); sau `L11-2-00`.
- **Mục tiêu:** 7.
- **Nguồn:** §1.1, đoạn "Bài toán trung tâm của chương"; `lec-11-topic-02`.
- **Mặt trang:** một hộp: chuỗi ở mục 1 của tệp này.
- **Mật độ:** khoảng 62 âm tiết, 1 hộp hai câu: ngoại lệ (mục 4). **Số đo cuối** (`deck_lint`, sau III.5): 61 âm tiết, trần 60, tỉ lệ 1,02.
- **Sau biên tập (2026-11-19):** mặt trang không đổi; ghi chú diễn giả: "$m=70$: xác suất xếp $\downarrow$ trên $\rightarrow$ không quá $0{,}0496$", với cả bốn hành động cần $m=75$; hai vòng so với sáu lượt quét.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT11.
- **Ghi chú diễn giả:** bốn câu trả lời có điều kiện theo §6.2 (nền: Mệnh đề 11.9, $0{,}225$; quyết định: Mệnh đề 11.21, $0{,}2016\to0{,}8566$, $m=70$; liên tục: $8\to2{,}88$, hệ số $0{,}6$; tùy chọn: hai vòng so với sáu lượt quét), mỗi câu một mạch; khi mô hình sai, các bảo đảm nói về MDP của mô hình.

### Mạch 2. Tính bất định của môi trường và lập kế hoạch nền (13 trang, 30 phút)

Hai cụm khái niệm (QT2 giữ một mạch, Q14): mô hình và bất định (`L11-2-01`–`L11-2-05`), lập kế hoạch nền với Dyna (`L11-2-06`–`L11-2-12`).

| Cụm | Vấn đề | Trực quan | Ví dụ | Hình thức | Ý tưởng chứng minh | Ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|---|
| Mô hình phân phối, mô hình mẫu | `L11-2-01` (câu hỏi của mạch) | `L11-2-01` | `L11-2-01` (Ví dụ 11.2) | `L11-2-01` (Định nghĩa 11.1) | không áp dụng (định nghĩa) | `L11-2-10` (cập nhật kỳ vọng cần mô hình phân phối) | Bài tập 11.1(a) (tự làm) |
| Lập kế hoạch nền, tại thời điểm quyết định | `L11-2-02` | `L11-2-02` | `L11-2-02` (trên mê cung) | `L11-2-02` (Định nghĩa 11.2) | không áp dụng | `L11-2-06`, `L11-3-02`, `L11-4-05` | Bài tập 11.1(b) (tự làm) |
| Mô hình đếm, Mệnh đề 11.5 | `L11-2-03` ($0{,}5$ thay $0{,}8$) | ghi chú diễn giả `L11-2-03` | `L11-2-03` (Ví dụ 11.3) | `L11-2-03` | "Chứng minh." một dòng (kết quả phụ) | `L11-2-04` (bảng $C=2,5,50$) | `L11-2-05` |
| Hai loại bất định | `L11-2-04` | `L11-2-04` | `L11-2-04` (Ví dụ 11.4, 11.5) | `L11-2-04` (Định nghĩa 11.6) | không áp dụng | `L11-2-04` (tập mô hình) | `L11-2-05` (Bài tập 11.2, lời giải trên mặt trang) |
| Q-planning, Mệnh đề 11.9 | `L11-2-06` (giới hạn Q-learning) | `L11-2-06` | `L11-2-06` (Ví dụ 11.6) | `L11-2-06` (Thuật toán 11.8, Mệnh đề 11.9) | "Chứng minh." một dòng | `L11-2-07` | `L11-2-12` câu (b) |
| Dyna-Q | `L11-2-07` (giới hạn của Q-planning, NT-RL-3) | `L11-2-07` (ba việc sau mỗi bước thật) | `L11-2-07` (Ví dụ 11.7) | `L11-2-08` (Thuật toán 11.10) | không áp dụng | `L11-2-08` (Nhận xét 11.11) | `L11-2-11`, `L11-2-12` (Bài tập 11.4) |
| Thưởng thăm dò | `L11-2-09` (Ví dụ 11.8) | `L11-2-09` | `L11-2-09` (Ví dụ 11.9) | `L11-2-09` (Định nghĩa 11.12) | không áp dụng | ghi chú diễn giả (Nhận xét 11.13) | Bài tập 11.12, 11.13, 11.19 (tự làm) |
| Cập nhật kỳ vọng và mẫu | `L11-2-10` | `L11-2-10` (dòng "Trực quan.") | `L11-2-10` (Ví dụ 11.10) | `L11-2-10` (Định nghĩa 11.14, Mệnh đề 11.15) | "Chứng minh." một dòng | `L11-2-10` (Ví dụ 11.11) | Bài tập 11.1(c), (d), 11.14 (tự làm) |

Cái truyền từ ví dụ sang công thức: mục tiêu $0{,}36$ hai cách (`L11-2-01`) thành điều kiện "trung bình mục tiêu mẫu bằng mục tiêu kỳ vọng" dùng ở `L11-2-10`; tần suất $1/2$ (`L11-2-03`) thành (2.1); mục tiêu $0{,}45$ của Ví dụ 11.6 thành bước 3 của Thuật toán 11.8 và bước (f) của Thuật toán 11.10; $\kappa\sqrt{\ell}=0{,}2$ thành Định nghĩa 11.12. §2.7 (đọc thêm: quét ưu tiên, lấy mẫu theo quỹ đạo, Định lý 11.19) chỉ ở ghi chú diễn giả của `L11-2-07` (quét ưu tiên) và `L11-2-08` (lấy mẫu theo quỹ đạo, RTDP), nói rõ là nội dung đọc thêm của ghi chú (NT5).

#### `L11-2-00` 2. Tính bất định của môi trường và lập kế hoạch nền (trang tiêu đề mạch), điểm vào mạch 2
- **Vị trí, bước:** điểm vào mạch 2; `section.strand-title`, `id="mach-2"`, `data-note-topic-id="lec-11-topic-04"`. Dòng dẫn nêu nhu cầu của cả mạch (mô hình có sai số mà vẫn dùng lại mẫu), không phải của riêng khái niệm đầu: ngoài hành trình khái niệm.
- **Lý do tồn tại:** NT12; mở cách dùng mô hình thứ nhất.
- **Liên kết:** trước `L11-1-07`; sau `L11-2-01`.
- **Mục tiêu:** 1, 2, 3.
- **Mặt trang:** `span.strand-number` "2." + "Tính bất định của môi trường và lập kế hoạch nền"; `p.strand-lead` "Mô hình học từ ít mẫu có sai số, nhưng mỗi bước thật vẫn cho thêm nhiều cập nhật." (19); `p.strand-keys` "mô hình phân phối · mô hình đếm · bất định nhận thức · Dyna-Q · cập nhật mẫu".
- **Mật độ:** **Số đo cuối** (`deck_lint`, sau III.5): 19 âm tiết, trần 25, tỉ lệ 0,76.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT12.
- **Ghi chú diễn giả (40–100):** kế thừa: Q-learning dùng mỗi mẫu thật một lần, bỏ bốn trong năm mẫu của lượt thứ nhất; việc của mạch: mô hình là gì, ước lượng từ dữ liệu ra sao, sai đến đâu sau ít lần thử, và dùng lại mẫu qua mô hình (Q-planning, Dyna-Q); trao đi: Dyna-Q cùng giới hạn của lập kế hoạch nền (tính cho cả trạng thái không nằm trên đường đi).

#### `L11-2-01` Ví dụ: mô hình của cặp $(\mathrm F,\rightarrow)$
- **Vị trí, bước:** mạch 2, trang nội dung đầu; vấn đề (câu hỏi của mạch, NT13) → ví dụ (Ví dụ 11.2) → định nghĩa (Định nghĩa 11.1) của cụm "mô hình phân phối, mô hình mẫu". Bước trực quan nằm trong dòng ví dụ ("bảng" so với "một kết cục rút theo bảng"); câu mười hai con xúc xắc ở ghi chú diễn giả.
- **Lý do tồn tại:** làm cụ thể hai cách mô hình trả lời cùng một câu hỏi, trên đúng cặp mà Dyna sẽ cập nhật; đặt điều kiện "trung bình mục tiêu mẫu bằng mục tiêu kỳ vọng" dùng ở `L11-2-10`.
- **Liên kết:** trước `L11-2-00`; sau `L11-2-02` (hai mô hình phục vụ trạng thái nào).
- **Mục tiêu:** 1.
- **Nguồn:** §2.1; Ví dụ 11.2; Định nghĩa 11.1; `lec-11-topic-04`.
- **Mặt trang:**
  - "Câu hỏi: mô hình học từ ít bước thật sai đến đâu, và cho thêm cập nhật thế nào?" (19)
  - "Ví dụ 11.2: với $\max_aQ(\mathrm K,a)=0{,}5$, $\max_aQ(\mathrm F,a)=0$, bảng $\{\mathrm K:0{,}8;\ \mathrm F:0{,}2\}$ của $(\mathrm F,\rightarrow)$ cho mục tiêu kỳ vọng $0{,}36$; một kết cục rút theo bảng cho $0{,}45$ hoặc $0$." (19)
  - "Định nghĩa 11.1." (3) rồi ba gạch đầu dòng:
  - "Mô hình phân phối (distribution model) trả $\hat p(\cdot,\cdot\mid s,a)$ trên các cặp (trạng thái kế, phần thưởng)." (15)
  - "Mô hình mẫu (sample model) trả một cặp $(R,S')$ rút theo $\hat p$, độc lập giữa các lần gọi." (16)
  - "Kinh nghiệm mô phỏng (simulated experience): mẫu chuyển sinh từ mô hình." (12)
- **Mật độ:** 84 âm tiết (trước 66), 6 dòng, 0 công thức hiển thị: ngoại lệ NT17, lý do: Định nghĩa 11.1 giữ đủ ba vế của khối ghi chú (NT2, phát hiện của cổng) cùng câu hỏi của mạch bắt buộc trên trang nội dung đầu (NT13). Không trang nào khác của mạch nhận được định nghĩa này vì nó đứng trước mọi khái niệm sau (NT9). **Số đo cuối** (`deck_lint`, sau III.5): 89 âm tiết, trần 60, tỉ lệ 1,48.
- **Sau biên tập (2026-11-19):** thêm "Trực quan. Mô hình trả cả bảng, hoặc một lần rút." (D-7); dòng Ví dụ bỏ "của $(\mathrm F,\rightarrow)$", câu hỏi bỏ "và".
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — mở mạch bằng ví dụ có số (NT14, NT23); Định nghĩa 11.1 gọn sau ví dụ (NT8).
- **Ghi chú diễn giả:** mười hai con xúc xắc (Sutton và Barto, 2018, §8.1, tr. 159); mô hình phân phối luôn cho mô hình mẫu; mô hình tất định thuộc cả hai loại; nhầm lẫn thường gặp: đồng nhất mô hình với môi trường, $\hat p$ có thể khác $p$; bảng $Q$ dùng ở đây là bảng sau lượt thứ nhất.

#### `L11-2-02` Lập kế hoạch nền và lập kế hoạch tại thời điểm quyết định
- **Vị trí, bước:** mạch 2; vấn đề → ví dụ → định nghĩa của cụm thứ hai (NT-RL-4: phân biệt lập kế hoạch nền và tại thời điểm quyết định).
- **Lý do tồn tại:** Định nghĩa 11.2 là trục phân loại của cả bài (mạch 2, 5 là nền; mạch 3, 4 là tại thời điểm quyết định); đặt chung trang với `L11-2-01` sẽ thành khoảng 110 âm tiết và hai điểm trung tâm.
- **Liên kết:** trước `L11-2-01`; sau `L11-2-03` (mô hình học từ dữ liệu sai đến đâu). Được dùng lại ở `L11-2-06` (Q-planning là lập kế hoạch nền), `L11-3-02` (rollout), `L11-4-05` (điều khiển dự báo).
- **Mục tiêu:** 1, 7.
- **Nguồn:** §2.1; Định nghĩa 11.2; đoạn sau Định nghĩa 11.2; Nhận xét 11.3; `lec-11-topic-04`.
- **Mặt trang:**
  - "Phép tính trên mô hình phục vụ nhiều trạng thái, hoặc chỉ trạng thái đang đứng." (14)
  - "Ví dụ. Ở $\mathrm A$, cập nhật $Q(\mathrm F,\rightarrow)$; ở $\mathrm F$, thử trước bốn hành động." (11)
  - "Định nghĩa 11.2." rồi hai gạch đầu dòng: "Lập kế hoạch nền (background planning) cải thiện giá trị cho nhiều trạng thái trước khi gặp chúng." (18); "Lập kế hoạch tại thời điểm quyết định (decision-time planning) chạy sau khi quan sát $S_t$, trả $A_t$." (16)
- **Mật độ:** 62 âm tiết (trước 86), 4 dòng (dòng định nghĩa hai gạch đầu dòng), 0 công thức hiển thị; dòng Nhận xét 11.3 chỉ ở ghi chú diễn giả. Định nghĩa 11.2 giữ "cải thiện giá trị … trước khi gặp" và "sau khi quan sát $S_t$, trả $A_t$" (NT2); "hoặc chính sách" ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 66 âm tiết, trần 60, tỉ lệ 1,10.
- **Sau biên tập (2026-11-19):** dòng vấn đề mang nhãn "Trực quan.".
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT-RL-4; tách khỏi `L11-2-01` để mỗi trang một điểm trung tâm.
- **Ghi chú diễn giả:** lập kế hoạch nền chia phép tính cho mọi trạng thái nó cập nhật; tại thời điểm quyết định dồn phép tính vào trạng thái hiện tại, phù hợp khi có thời gian suy nghĩ trước mỗi bước (Sutton và Barto, 2018, §8.8, tr. 180–181); quy hoạch động (Thuật toán 04.28, 04.31) là lập kế hoạch nền với mô hình phân phối đã biết (Nhận xét 11.3); ở bài này $\hat p$ học từ ít mẫu.

#### `L11-2-03` Mô hình đếm
- **Vị trí, bước:** mạch 2; vấn đề (tần suất $0{,}5$ thay $0{,}8$) → ví dụ → định nghĩa → kết quả của cụm mô hình đếm.
- **Lý do tồn tại:** trả lời vế "sai đến đâu" bằng một công thức (phương sai của tần suất).
- **Liên kết:** trước `L11-2-02`; sau `L11-2-04` (tách $p(1-p)$ khỏi $p(1-p)/C$).
- **Mục tiêu:** 1.
- **Nguồn:** §2.2; Ví dụ 11.3; Định nghĩa 11.4; Mệnh đề 11.5 và chứng minh; `lec-11-topic-05`.
- **Mặt trang:**
  - "Sau lượt thứ nhất, $(\mathrm A,\rightarrow)$ được thử hai lần, một lần sang $\mathrm B$, một lần trượt: tần suất cho $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$, trong khi $p=0{,}8$ (Ví dụ 11.3)." (22)
  - "Định nghĩa 11.4. Với $C(s,a)\ge1$ lần thử, $C(s,a,s')$ lần tới $s'$, mô hình đếm (count-based model) là" (13), công thức hiển thị (2.1): $\hat p(s'\mid s,a)=C(s,a,s')/C(s,a)$, $\hat r(s,a)$ là trung bình phần thưởng đã nhận (KaTeX `\hat r(s,a)=\frac1{C(s,a)}\sum_iR^{(i)}(s,a)`).
  - "Mệnh đề 11.5. Giả thiết: $C$ cố định trước khi thử; $S'_1,\dots,S'_C$ độc lập, cùng phân phối $p(\cdot\mid s,a)$." (11)
  - "Kết luận:" công thức hiển thị $\mathbb E\,\hat p=p$, $\operatorname{Var}\hat p=p(1-p)/C$ (2.2).
  - "Chứng minh. $C(s,a,s')$ là tổng của $C$ biến Bernoulli độc lập, tham số $p$." (10)
- **Mật độ:** khoảng 58 âm tiết, 6 dòng, 2 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 77 âm tiết, trần 60, tỉ lệ 1,28.
- **Sau biên tập (2026-11-19):** dòng "Trực quan." của hai loại bất định chuyển từ `L11-2-04` lên trước Định nghĩa 11.4 và Mệnh đề 11.5 (D-7).
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — Mệnh đề 11.5 là kết quả phụ, có dòng "Chứng minh." (NT6).
- **Ghi chú diễn giả:** đếm của lượt thứ nhất ($2+1+1+1=5$ lần thử); cặp $C=0$ chưa xác định; mô hình đếm là MDP thực nghiệm của Mệnh đề 05.34 đếm theo cặp; phản ví dụ "$C$ cố định trước": dừng ở lần trượt đầu cho $\mathbb E\hat p=1-\tfrac14\ln5=0{,}5976\ne0{,}8$; Phạm vi: chỉ một ô của bảng, không chặn sai số giá trị lập kế hoạch.

#### `L11-2-04` Bất định ngẫu nhiên và bất định nhận thức
- **Vị trí, bước:** mạch 2; trực quan → ví dụ số → định nghĩa → ứng dụng (tập mô hình) của cụm hai loại bất định.
- **Lý do tồn tại:** cùng công thức (2.2) chứa hai đại lượng khác nhau về bản chất; mục tiêu 1 đòi tách chúng.
- **Liên kết:** trước `L11-2-03` (công thức (2.2)); sau `L11-2-05` (kiểm tra bằng Bài tập 11.2).
- **Mục tiêu:** 1.
- **Nguồn:** §2.2–2.3; Ví dụ 11.4, 11.5; Định nghĩa 11.6; Nhận xét 11.7; `lec-11-topic-05`, `lec-11-topic-06`.
- **Mặt trang:**
  - "Trực quan. Trượt thuộc về môi trường; sai lệch của $\hat p$ do ít dữ liệu, giảm khi $C$ tăng." (17)
  - Bảng (Ví dụ 11.4, $p=0{,}8$), hai hàng: $C(\mathrm F,\rightarrow)$: $2$; $5$; $50$ / $\sqrt{0{,}16/C}$: $0{,}2828$; $0{,}1789$; $0{,}0566$.
  - "Định nghĩa 11.6. Bất định ngẫu nhiên (aleatoric uncertainty) đo bằng $p(1-p)$, không đổi theo $C$; bất định nhận thức (epistemic uncertainty) đo bằng $\operatorname{Var}\hat p=p(1-p)/C$." (22)
  - "Lưu ý: tập mô hình (model ensemble) báo độ phân tán $0$ ở cặp một mẫu (Nhận xét 11.7)." (18)
- **Mật độ:** 59 âm tiết (trước 64), 5 dòng, 0 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 55 âm tiết, trần 60, tỉ lệ 0,92.
- **Sau biên tập (2026-11-19):** mở bằng "Cùng công thức phương sai chứa hai đại lượng …"; công thức nhóm `{…}` để ngắt dòng.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — Định nghĩa 11.6 là khái niệm của mục tiêu 1; tập mô hình (`bổ sung`) chỉ một dòng.
- **Ghi chú diễn giả:** Ví dụ 11.5: ba lần lấy lại mẫu cỡ $2$ từ $\{\mathrm A,\mathrm B\}$ cho $0$; $0{,}5$; $1$, độ lệch chuẩn không hiệu chỉnh $0{,}4082$; môi trường tất định không có bất định ngẫu nhiên nhưng vẫn có bất định nhận thức ở cặp chưa thử; Chua và cộng sự (2018, §4) cho thuật ngữ; với mô hình là mạng nơ-ron, (2.2) không dùng được.

#### `L11-2-05` Bài tập: hai loại bất định
- **Vị trí, bước:** mạch 2; kiểm tra của cụm mô hình và bất định (NT24: bài có "Lời giải:" trên mặt trang).
- **Lý do tồn tại:** kiểm phân biệt tử số $p(1-p)$ với $p(1-p)/C$ trước khi chuyển sang dùng mô hình.
- **Liên kết:** trước `L11-2-04`; sau `L11-2-06`.
- **Mục tiêu:** 1.
- **Nguồn:** Bài tập 11.2 (Mức nhận biết) và lời giải; `lec-11-topic-27`.
- **Mặt trang:** "Câu hỏi (Bài tập 11.2): mê cung hai phòng trượt với xác suất $0{,}2$; xác định đúng hay sai, giải thích một câu." Bảng `Câu | Phát biểu | Lời giải` (tiêu đề cột không có dấu hai chấm); cột cuối là fragment theo từng hàng, fragment đầu mở bằng nhãn "Lời giải:" (NT19):
  - (a) "thêm dữ liệu cho $(\mathrm F,\rightarrow)$ làm giảm xác suất trượt" | "Sai: trượt là bất định ngẫu nhiên; dữ liệu chỉ làm $\hat p$ gần $0{,}8$ hơn."
  - (b) "sau một lần thử $(\mathrm B,\downarrow)\to\mathrm F$, $\hat p(\mathrm F\mid\mathrm B,\downarrow)=1$ nên cặp này hết bất định" | "Sai: với $C=1$, độ lệch chuẩn của $\hat p$ là $\sqrt{p(1-p)}=0{,}4$ khi $p=0{,}8$."
  - (c) "môi trường tất định không có bất định nhận thức" | "Sai: cặp chưa thử vẫn có kết cục chưa biết."
  - (d) "với $C(s,a)=8$ và $p=0{,}5$, độ lệch chuẩn của $\hat p$ bằng $0{,}1768$" | "Đúng: $\sqrt{0{,}25/8}=0{,}1768$."
- **Mật độ:** khoảng 75 âm tiết, 5 dòng: ngoại lệ NT17 "đề bài tập giữ nguyên câu chữ" (Bài tập 11.2), trần 60, 1,5 lần là 90. **Số đo cuối** (`deck_lint`, sau III.5): 86 âm tiết, trần 60, tỉ lệ 1,43.
- **Sau biên tập (2026-11-19):** bỏ tiêu đề cột "Phát biểu" và nhãn trong ô; lời giải viết thống nhất "Sai; …"/"Đúng; …".
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT24, NT-RL-10.
- **Ghi chú diễn giả (NT-RL-10):** năng lực kiểm: tách bất định ngẫu nhiên khỏi bất định nhận thức. "Gợi ý: tách $p(1-p)$ khỏi $p(1-p)/C$ (Định nghĩa 11.6, Mệnh đề 11.5)." Lỗi thường gặp: quên chia cho $C$ ở (d) cho $0{,}5$.

#### `L11-2-06` Q-planning
- **Vị trí, bước:** mạch 2; vấn đề (giới hạn của Q-learning, NT-RL-3) → trực quan → ví dụ tính tay (Ví dụ 11.6, NT-RL-2) → thuật toán → bảo đảm của cụm Q-planning. Phân biệt có mô hình và không có mô hình (NT-RL-4): cùng một quy tắc, nguồn mẫu khác.
- **Lý do tồn tại:** cầu nối từ Q-learning (Bài 06) sang lập kế hoạch: mẫu từ mô hình đi vào đúng quy tắc cũ; Mệnh đề 11.9 nói rõ giới hạn là $\hat q_*$, không phải $q_*$.
- **Liên kết:** trước `L11-2-05`; sau `L11-2-07` (xen Q-planning với bước thật).
- **Mục tiêu:** 2.
- **Nguồn:** §2.4; Ví dụ 11.6; Thuật toán 11.8; Mệnh đề 11.9 và chứng minh; `lec-11-topic-07`.
- **Mặt trang:**
  - "Q-learning dùng mỗi mẫu thật một lần; quy tắc của nó áp được lên mẫu do mô hình sinh." (19)
  - Bảng khuôn T1, một hàng (Ví dụ 11.6; tiêu đề cột "cặp" ghi $\alpha=0{,}5$, $\gamma=0{,}9$; mô hình mẫu trả $(0,\mathrm K)$ ghi trong ghi chú diễn giả): $(\mathrm F,\rightarrow)$ | $0+0{,}9\cdot0{,}5=0{,}45$ | $0{,}45$ | $0{,}225$.
  - "Thuật toán 11.8. Lặp: chọn ngẫu nhiên một cặp hợp lệ $(S,A)$; mô hình mẫu trả $(R,S')$; cập nhật $Q(S,A)$ như Q-learning." (19)
  - "Giả thiết: mô hình cố định, xác định ở mọi cặp; mọi cặp được chọn vô hạn lần; bước học Robbins–Monro (Định nghĩa 06.19)." (24)
  - "Bảo đảm: $Q\to\hat q_*$, giá trị hành động tối ưu trên mô hình, hầu chắc chắn (Mệnh đề 11.9)." (17)
- **Mật độ:** 79 âm tiết (trước 80), 5 dòng, 0 công thức hiển thị; trang thuật toán (Thuật toán 11.8), trần thuật toán 80 của cổng. Dòng 1 là bước vấn đề (giới hạn của Q-learning, NT-RL-3) và trực quan (quy tắc không hỏi nguồn mẫu); $\hat q_*$ gọi tên trên mặt trang ("giá trị hành động tối ưu trên mô hình", kiểm lại của cổng), vì `L11-2-11`, `L11-6-03`, `L11-6-06` dùng nó. **Số đo cuối** (`deck_lint`, sau III.5): 79 âm tiết, trần 80, tỉ lệ 0,99.
- **Sau biên tập (2026-11-19):** câu vấn đề "Q-learning dùng mỗi mẫu thật một lần." và dòng "Trực quan. Quy tắc không hỏi mẫu từ đâu tới." tách riêng; "rút ngẫu nhiên cặp hợp lệ"; "bước học Robbins–Monro"; "Bảo đảm: $Q\to\hat q_*$ (tối ưu trên mô hình) hầu chắc chắn (Mệnh đề 11.9)", nghĩa đầy đủ của $\hat q_*$ ở ghi chú diễn giả.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — gộp Ví dụ 11.6, Thuật toán 11.8, Mệnh đề 11.9 (kế hoạch để Mệnh đề 11.9 trên trang Dyna; ghi chú đặt nó ngay sau Thuật toán 11.8, NT2).
- **Ghi chú diễn giả:** Q-planning là lập kế hoạch nền (Định nghĩa 11.2); "Chứng minh." trong ghi chú diễn giả (kết quả phụ, NT6): MDP của mô hình thỏa giả thiết nền của Nhận xét 06.20, mẫu có phân phối $\hat p$, Định lý 06.21 không dùng việc các cặp nối thành quỹ đạo (Bertsekas và Tsitsiklis, 1996, §5.6); phản ví dụ: mô hình chưa xác định tại $(\mathrm C,\cdot)$ thì $Q(\mathrm C,\cdot)$ giữ giá trị khởi tạo; $\hat p$ đổi sau mỗi bước thật thì không có $\hat q_*$ duy nhất. Kiểm tra lại: $(0+0{,}45)/2=0{,}225$.

#### `L11-2-07` Ví dụ: lượt thứ nhất của Dyna-Q
- **Vị trí, bước:** mạch 2; vấn đề (giới hạn của Q-planning: cần mô hình cho sẵn ở mọi cặp, NT-RL-3) → trực quan (ba việc sau mỗi bước thật) → ví dụ tính tay trước giả mã của Dyna-Q (NT-RL-2) → "Diễn giải:" (NT23).
- **Lý do tồn tại:** cho thấy hai cập nhật lập kế hoạch đã đưa giá trị của $\mathrm K$ về $\mathrm F$ ngay trong lượt thứ nhất; số $0{,}225$ là câu trả lời 1 của câu hỏi trung tâm.
- **Liên kết:** trước `L11-2-06` (quy tắc Q-planning); sau `L11-2-08` (thứ tự các bước thành thuật toán).
- **Mục tiêu:** 2.
- **Nguồn:** §2.4; Ví dụ 11.7; `lec-11-topic-07`.
- **Mặt trang:**
  - "Q-planning cần mô hình ở mọi cặp." (7)
  - "Trực quan. Khi mô hình học dần, mỗi bước thật kéo theo cập nhật trực tiếp, cập nhật mô hình, $n$ cập nhật lập kế hoạch." (25)
  - "Tính lượt thứ nhất (Ví dụ 11.7), $Q\equiv0$, $\alpha=0{,}5$, $\gamma=0{,}9$, $n=2$, mô hình lưu kết cục gần nhất; bốn bước đầu cho mục tiêu $0$." (20)
  - Bảng khuôn T1, ba hàng, hàng tiêu đề "cặp ở bước thứ năm" (không chú thích riêng): $(\mathrm K,\rightarrow)$ trực tiếp | $1$ | $1$ | $0{,}5$; $(\mathrm F,\rightarrow)$ kế hoạch | $0{,}45$ | $0{,}45$ | $0{,}225$; $(\mathrm K,\rightarrow)$ kế hoạch | $1$ | $0{,}5$ | $0{,}75$ (nhãn hàng 6 âm tiết).
  - câu kết của bảng (chú thích đặt dưới bảng, cùng khối bảng): "Diễn giải: với $n=0$, bảng chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$." (6)
- **Mật độ:** 64 âm tiết (trước 55, chưa có dòng giới hạn và trực quan), 6 dòng (câu giới hạn, dòng "Trực quan." đứng đầu dòng, dòng dữ kiện, bảng ba hàng có câu kết "Diễn giải:" dưới bảng), 0 công thức hiển thị. Lượt thật $\mathrm A\to\mathrm A\to\mathrm B\to\mathrm F\to\mathrm K\to\mathrm Z$ và việc mô hình ghi $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$ ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 69 âm tiết, trần 60, tỉ lệ 1,15.
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — gộp hai trang của kế hoạch (cập nhật trực tiếp; cập nhật lập kế hoạch) bằng một bảng ba hàng khuôn T1.
- **Ghi chú diễn giả:** mô hình ghi $(\mathrm A,\rightarrow)\mapsto(0,\mathrm A)$ rồi ghi đè $(0,\mathrm B)$; giả sử bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$; đảo thứ tự cho $(\mathrm F,\rightarrow)=0{,}3375$, thứ tự cập nhật đổi kết quả (quét ưu tiên, Nhận xét 11.17, nội dung đọc thêm của ghi chú); Sutton và Barto (2018, Hình 8.3, tr. 165): với $n=50$, chính sách tham lam phủ phần lớn mê cung ở giữa lượt thứ hai.

#### `L11-2-08` Thuật toán Dyna-Q
- **Vị trí, bước:** mạch 2; hình thức (thuật toán) → kiểm tra giả thiết (Nhận xét 11.11) của cụm Dyna-Q.
- **Lý do tồn tại:** NT-RL-2: đầu vào, đầu ra, giả thiết, thứ tự thao tác, quy tắc cập nhật, điều kiện dừng; khớp bảng của `L11-2-07` (bước (d), (e), (f)).
- **Liên kết:** trước `L11-2-07`; sau `L11-2-09` (mô hình sai khi môi trường đổi).
- **Mục tiêu:** 2.
- **Nguồn:** Thuật toán 11.10; Nhận xét 11.11; hình kiến trúc Dyna; `lec-11-topic-07`.
- **Mặt trang:**
  - `.grid2`; cột trái:
  - "Thuật toán 11.10. Đầu vào: môi trường, $\gamma$, $\alpha$, $\varepsilon$, $n$. Đầu ra: $Q$, $\mathrm{Model}$. Giả thiết: môi trường tất định." (15)
  - "Mỗi bước thật: chọn $A$ $\varepsilon$-tham lam theo $Q(S,\cdot)$, nhận $R$, $S'$." (8)
  - "(d) $Q(S,A)\leftarrow Q(S,A)+\alpha[R+\gamma\max_{a'}Q(S',a')-Q(S,A)]$." (1)
  - "(e) $\mathrm{Model}(S,A)\leftarrow(R,S')$." (1)
  - "(f) Lặp $n$ lần: chọn một cặp đã thử, lấy $(\tilde R,\tilde S')$ từ mô hình, cập nhật như (d). Dừng khi hết ngân sách bước thật." (23)
  - "Lưu ý: Mệnh đề 11.9 không áp dụng (Nhận xét 11.11)." (11)
  - Cột phải: `kien-truc-dyna-slide.svg` (nhãn bước (d), (e), (f) trùng chữ của thuật toán).
- **Mật độ:** 59 âm tiết (trước 77), 6 dòng; trang hai cột, đích ≤ 60 của cổng: đạt. Tên ba bước (học trực tiếp, học mô hình, điều khiển tìm kiếm) và lý do của dòng "Lưu ý:" (bước (f) chỉ chọn cặp đã thử, mô hình đổi sau mỗi bước thật) ở ghi chú diễn giả. Công thức (d) ngắt bằng `aligned` nếu tràn cột. **Số đo cuối** (`deck_lint`, sau III.5): 56 âm tiết, trần 80, tỉ lệ 0,70.
- **Sau biên tập (2026-11-19):** lý do của "Lưu ý:" có trên mặt trang; bước (e), (f) một đoạn ngắt bằng `<br>` (tránh chạm chân trang); ghi chú diễn giả nêu điều kiện của giá trị $0{,}729$ và trang Sutton và Barto.
- **Hình, phút:** `kien-truc-dyna-slide.svg`; 2,5.
- **Quyết định:** thêm — trang thuật toán riêng (`CLAUDE.md` "Density"); Nhận xét 11.11 là bước kiểm tra giả thiết của Mệnh đề 11.9.
- **Ghi chú diễn giả:** tên ba bước: học tăng cường trực tiếp (direct reinforcement learning), học mô hình (model learning), điều khiển tìm kiếm (search control) cùng Q-planning; chi phí $O((n+1)\max_s\lvert\mathcal A(s)\rvert)$ mỗi bước thật; với mô hình tất định, bước (f) giống rút từ bộ nhớ phát lại (Định nghĩa 08.7) nhưng gộp theo cặp; Tình huống 11.2: trên mê cung có trượt, mô hình lưu kết cục gần nhất là mô hình tất định sai, giá trị trên mô hình quá lạc quan (tại $\mathrm A$ là $0{,}729$ so với $0{,}6604$); cách sửa là mô hình đếm. Lấy mẫu theo quỹ đạo, Định lý 11.19 (RTDP): đọc thêm của ghi chú.

#### `L11-2-09` Mô hình sai và thưởng thăm dò
- **Vị trí, bước:** mạch 2; vấn đề (môi trường đổi) → ví dụ (Ví dụ 11.8) → trực quan (lạc quan tự sửa, bi quan không) → ví dụ số (Ví dụ 11.9, NT-RL-2) → định nghĩa (Định nghĩa 11.12). Thứ tự ví dụ trước định nghĩa theo ghi chú.
- **Lý do tồn tại:** mục tiêu 2 ("giải thích vì sao mô hình sai cần thưởng thăm dò"); dùng lại mê cung với một câu hỏi mới (NT23).
- **Liên kết:** trước `L11-2-08` (bước (e), (f)); sau `L11-2-10` (một cập nhật lập kế hoạch tốn bao nhiêu).
- **Mục tiêu:** 2.
- **Nguồn:** §2.5; Ví dụ 11.8, 11.9; Định nghĩa 11.12; Nhận xét 11.13; `lec-11-topic-08`.
- **Mặt trang:**
  - "Ví dụ 11.8: cửa $\mathrm F$–$\mathrm K$ bị chặn, tường $\mathrm B$–$\mathrm C$ được dỡ." (9)
  - "Lạc quan ở $(\mathrm F,\rightarrow)$: tác tử tới $\mathrm F$, ở yên, bước (e) sửa mô hình." (13)
  - "Bi quan ở $(\mathrm B,\rightarrow)$: chính sách tham lam tránh cặp này, mô hình không được sửa." (15)
  - "Định nghĩa 11.12. Dyna-Q+ cộng thưởng thăm dò (exploration bonus) $\kappa\sqrt{\ell(\tilde S,\tilde A)}$ vào $\tilde R$ ở bước (f); $\ell$ là số bước thật từ lần thử gần nhất." (23)
  - Bảng khuôn T1, một hàng; tiêu đề cột "cặp" ghi "Ví dụ 11.9, $\kappa=0{,}01$, $\ell=400$, $\max_aQ(\mathrm B,a)=0{,}6$": $(\mathrm B,\rightarrow)$, $Q=0{,}54$ | $0+0{,}2+0{,}9\cdot0{,}6=0{,}74$ | $0{,}2$ | $0{,}64$.
  - "Diễn giải: $0{,}64>0{,}6$, hành động tham lam tại $\mathrm B$ đổi sang $\rightarrow$." (9)
- **Mật độ:** 72 âm tiết (trước 80), 6 dòng, 0 công thức hiển thị: ngoại lệ NT17, lý do: bước trực quan của cụm là chính phép so hai kiểu mô hình sai ("lạc quan", "bi quan") trên cùng mê cung đổi cửa, phải đứng cạnh định nghĩa mà nó dẫn tới; mọi câu giải thích khác ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 87 âm tiết, trần 60, tỉ lệ 1,45.
- **Sau biên tập (2026-11-19):** hai trường hợp lạc quan, bi quan gộp thành dòng "Trực quan."; "mô hình còn ghi kết cục cũ"; "sau $3\,000$ bước thật" chuyển vào ghi chú diễn giả; ghi chú diễn giả chỉ ghi "tất định".
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — gộp Ví dụ 11.8, 11.9 và Định nghĩa 11.12 thành một trang (mã L11-2-08 của `ke-hoach-trang-chieu.md`).
- **Ghi chú diễn giả:** hai thay đổi cuối của Dyna-Q+ (chọn cả hành động chưa thử; mô hình khởi tạo "ở yên, thưởng $0$"; chú thích 1 của Sutton và Barto, 2018, tr. 168); không có thưởng, mục tiêu $0{,}54$, sai lệch $0$: cặp đã ở điểm bất động của mô hình; Nhận xét 11.13: thưởng làm MDP lập kế hoạch đổi theo thời gian, nên bảng không còn ước lượng $\hat q_*$ và Mệnh đề 11.9 không áp dụng; bài tự làm 11.12, 11.13, 11.19 (Sutton và Barto Bài tập 8.2–8.4).

#### `L11-2-10` Cập nhật kỳ vọng và cập nhật mẫu
- **Vị trí, bước:** mạch 2; vấn đề → trực quan → ví dụ (Ví dụ 11.10) → định nghĩa (Định nghĩa 11.14) → kết quả (Mệnh đề 11.15(b)) → ứng dụng (Ví dụ 11.11). Phân biệt mô hình phân phối và mô hình mẫu (NT-RL-4) ở mức phép cập nhật.
- **Lý do tồn tại:** mục tiêu 3; giải thích vì sao Dyna dùng cập nhật mẫu.
- **Liên kết:** trước `L11-2-09`; sau `L11-2-11` (bài tập tính tay của cụm Dyna).
- **Mục tiêu:** 3.
- **Nguồn:** §2.6; Ví dụ 11.10, 11.11; Định nghĩa 11.14; Mệnh đề 11.15; Nhận xét 11.16; `lec-11-topic-09`.
- **Mặt trang:**
  - "Trực quan. Cập nhật kỳ vọng hỏi mọi kết cục, không nhiễu nhưng tốn; cập nhật mẫu hỏi một kết cục, rẻ nhưng nhiễu." (24)
  - Bảng hai hàng `cập nhật | mục tiêu | số lần đánh giá`, tiêu đề cột "cập nhật" ghi "Ví dụ 11.10, $(\mathrm A,\rightarrow)$: $\mathrm B$, $\mathrm A$ mỗi trạng thái $0{,}5$; $\max_aQ(\mathrm B,a)=0{,}6$, $\max_aQ(\mathrm A,a)=0{,}4$": cập nhật kỳ vọng (expected update) | $0{,}9\,(0{,}5\cdot0{,}6+0{,}5\cdot0{,}4)=0{,}45$ | $2$; cập nhật mẫu (sample update) | $0{,}54$ hoặc $0{,}36$ | $1$ (nhãn hàng 10 âm tiết).
  - "Mệnh đề 11.15(b). Giả thiết: phần thưởng $0$; $b$ trạng thái kế đồng khả năng (hệ số phân nhánh, branching factor); giá trị kế cố định, là $b$ biến độc lập, cùng kỳ vọng, phương sai $1$; $k$ mẫu độc lập, $\alpha_j=1/j$. Kết luận:" (38)
  - công thức hiển thị (2.5) $\sqrt{\mathbb E(Q_k-\bar y)^2}=\sqrt{(b-1)/(bk)}$.
  - "$b=100$, $k=10$: sai số $0{,}3146$, chi phí bằng một phần mười (Ví dụ 11.11)." (11)
- **Mật độ:** 83 âm tiết (trước 78, khi đó thiếu giả thiết), 6 dòng (gạch đầu dòng mệnh đề hai dòng hiển thị), 1 công thức hiển thị: ngoại lệ NT17, lý do: Mệnh đề 11.15(b) phải giữ đủ năm giả thiết của ghi chú (NT2; phát hiện nghiêm trọng của cổng), cùng bước trực quan của cụm (NT8). Hai cập nhật viết thành bảng (VP11) để bù. **Số đo cuối** (`deck_lint`, sau III.5): 88 âm tiết, trần 60, tỉ lệ 1,47.
- **Sau biên tập (2026-11-19):** "Trực quan. Bước (f) hỏi một kết cục: rẻ mà nhiễu; hỏi mọi kết cục: đúng mà tốn."; cột "trạng thái kế xét"; Mệnh đề 11.15(b) thêm "độc lập với lần rút" và định nghĩa $\bar y$, $Q_k$ ngay trong "Kết luận:" (D-8); Ví dụ 11.11 "tốn một phần mười".
- **Hình, phút:** —; 3 (hình `cap-nhat-ky-vong-va-mau.svg` chỉ ở ghi chú).
- **Quyết định:** thêm — gộp ví dụ, định nghĩa, mệnh đề (mã L11-2-09 của `ke-hoach-trang-chieu.md`); bỏ hình khỏi deck để giữ mật độ.
- **Ghi chú diễn giả:** "Chứng minh." (kết quả phụ): trung bình mẫu với $\alpha_j=1/j$ (Mệnh đề 05.9) có phương sai $\sigma^2/k$; với $b$ giá trị độc lập phương sai $1$, $\mathbb E\sigma^2=(b-1)/b$; sai số ban đầu chuẩn hóa bằng $1$ (Sutton và Barto, 2018, tr. 174, Hình 8.7); Nhận xét 11.16: khi $b$ nhỏ ($b=2$), cập nhật kỳ vọng chỉ tốn gấp đôi và cho sai số $0$ thay vì $0{,}7071$; với trình mô phỏng chỉ có cập nhật mẫu; bài tự làm 11.1(c), (d), 11.14.

#### `L11-2-11` Bài tập: bước thật đầu của lượt thứ hai
- **Vị trí, bước:** mạch 2; kiểm tra của cụm Dyna-Q (đề).
- **Lý do tồn tại:** NT24: cụm Dyna có một bài có lời giải trên mặt trang; dùng cùng khuôn T1 với `L11-2-07` (NT-RL-5).
- **Liên kết:** trước `L11-2-10`; sau `L11-2-12`.
- **Mục tiêu:** 2.
- **Nguồn:** Bài tập 11.4 (Mức tính toán hoặc chứng minh); `lec-11-topic-27`.
- **Mặt trang:**
  - "Câu hỏi (Bài tập 11.4): sau Ví dụ 11.7, $Q(\mathrm K,\rightarrow)=0{,}75$, $Q(\mathrm F,\rightarrow)=0{,}225$, ô khác bằng $0$; $\alpha=0{,}5$, $\gamma=0{,}9$, $n=2$." (11)
  - "Mô hình ghi $(\mathrm A,\rightarrow)\mapsto(0,\mathrm B)$, $(\mathrm B,\downarrow)\mapsto(0,\mathrm F)$, $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$, $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$." (3)
  - "Bước thật là $(\mathrm A,\rightarrow,0,\mathrm B)$; bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm B,\downarrow)$." (10)
  - "(a) Tính các ô thay đổi." (6)
  - "(b) Nêu điều kiện để Q-planning trên một mô hình hội tụ tới $\hat q_*$, và giải thích vì sao Dyna-Q trong bài này không thỏa điều kiện đó." (28)
- **Mật độ:** khoảng 56 âm tiết, 5 dòng; đề giữ câu chữ của ghi chú. **Số đo cuối** (`deck_lint`, sau III.5): 56 âm tiết, trần 60, tỉ lệ 0,93.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm — NT24; đề và lời giải tách hai trang cùng tiêu đề vì dữ kiện dài.
- **Ghi chú diễn giả (NT-RL-10):** năng lực kiểm: thực hiện đúng thứ tự (d), (e), (f) và kiểm giả thiết của Mệnh đề 11.9. "Gợi ý: ghi mục tiêu, sai lệch, giá trị mới cho từng cập nhật, theo thứ tự; với (b), dùng Mệnh đề 11.9."

#### `L11-2-12` Bài tập: bước thật đầu của lượt thứ hai
- **Vị trí, bước:** mạch 2; kiểm tra (lời giải); câu nối sang mạch 3 (NT13).
- **Lý do tồn tại:** lời giải trên mặt trang, mỗi dòng một bước (NT24); câu nối nêu giới hạn của lập kế hoạch nền.
- **Liên kết:** trước `L11-2-11`; sau `L11-3-00`.
- **Mục tiêu:** 2.
- **Nguồn:** lời giải Bài tập 11.4; kết mục §2; `lec-11-topic-27`, `lec-11-topic-07`.
- **Mặt trang:** "Lời giải:" bảng khuôn T1, ba hàng (mỗi hàng một fragment): trực tiếp $(\mathrm A,\rightarrow)$ | $0{,}9\max_aQ(\mathrm B,a)=0$ | $0$ | $0$; lập kế hoạch $(\mathrm F,\rightarrow)$ | $0{,}675$ | $0{,}45$ | $0{,}45$; lập kế hoạch $(\mathrm B,\downarrow)$ | $0{,}9\cdot0{,}45=0{,}405$ | $0{,}405$ | $0{,}2025$.
  - "(b) Mệnh đề 11.9 cần mô hình cố định, xác định ở mọi cặp, mọi cặp được chọn vô hạn lần, bước học Robbins–Monro; ở đây mô hình chỉ có bốn cặp, đổi sau mỗi bước thật, và $\alpha=0{,}5$ hằng." (39; hai dòng hiển thị)
  - Câu nối (chỉ giữ giới hạn; ý "dồn phép tính" để cho `L11-3-01`): "Lập kế hoạch nền tốn phép tính cả cho $\mathrm A$, $\mathrm B$, $\mathrm E$, ngoài đường ngắn nhất từ $\mathrm F$." (17)
- **Mật độ:** khoảng 57 âm tiết (trước 70), 5 dòng. **Số đo cuối** (`deck_lint`, sau III.5): 64 âm tiết, trần 60, tỉ lệ 1,07.
- **Sau biên tập (2026-11-19):** lời giải (b) giữ bốn giả thiết của Mệnh đề 11.9; câu nối là dòng thường, không fragment: "Đứng ở $\mathrm F$ chỉ cần hành động tại $\mathrm F$; lập kế hoạch nền vẫn tính cho $\mathrm A$, $\mathrm B$, $\mathrm E$."
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT24, NT13.
- **Ghi chú diễn giả:** kiểm tra lại: đảo thứ tự, $(\mathrm B,\downarrow)$ trước có mục tiêu $0{,}2025$ và giá trị mới $0{,}10125$; lỗi thường gặp: dùng $Q(\mathrm F,\rightarrow)=0{,}225$ cũ khi cập nhật $(\mathrm B,\downarrow)$. Kết quả của mạch: mô hình đếm và phương sai của nó, Q-planning hội tụ tới $\hat q_*$, Dyna-Q, sai số của cập nhật mẫu.

### Mạch 3. Tìm kiếm theo cây Monte Carlo (12 trang, 28 phút)

| Cụm | Vấn đề | Trực quan | Ví dụ | Hình thức | Ý tưởng chứng minh | Ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|---|
| Thuật toán rollout | `L11-3-01` (câu khẳng định của mạch; $0{,}2016$ so với $0{,}8566$) | `L11-3-01` | `L11-3-01` (Ví dụ 11.12, tính tay trước giả mã) | `L11-3-02` (Thuật toán 11.20) | không áp dụng | `L11-3-03` (Ví dụ 11.13) | Bài tập 11.8 (tự làm, ghi chú diễn giả `L11-3-05`) |
| Tính chất cải thiện (Mệnh đề 11.21, kết quả chính) | `L11-3-01` (chính sách cơ sở kém) | `L11-3-03` (một bước cải thiện chính sách) | `L11-3-03` (Ví dụ 11.13) | `L11-3-03` | `L11-3-04` | `L11-3-03` | `L11-3-04` (bỏ giả thiết); `L11-6-06` câu 3 |
| Số mô phỏng (Mệnh đề 11.22) | `L11-3-05` (cần $q_{\pi_0}$ chính xác, chỉ có trung bình) | ghi chú diễn giả | `L11-3-05` (Ví dụ 11.14) | `L11-3-05` | "Chứng minh." ở ghi chú diễn giả (kết quả phụ) | `L11-3-05` ($m=70$) | Bài tập 11.8 (tự làm) |
| Quy tắc cận tin cậy trên | `L11-3-06` (rollout chia đều) | `L11-3-06` (ưu tiên trung bình cao hoặc ít mẫu) | `L11-3-06` (Ví dụ 11.15) | `L11-3-06` (Định nghĩa 11.23, Định lý 11.24) | không áp dụng (dẫn nguồn) | `L11-3-07` (chỉ số UCT) | Bài tập 11.18 (tự làm) |
| Bốn pha của MCTS | `L11-3-07` (rollout không dùng mô phỏng trước) | `L11-3-07` | `L11-3-07`, `L11-3-08` (Ví dụ 11.16) | `L11-3-07` (Định nghĩa 11.25), `L11-3-09` (Thuật toán 11.26) | không áp dụng | `L11-3-08` (AlphaGo Zero, NT-RL-11) | `L11-3-11` (Bài tập 11.5, lời giải trên mặt trang) |
| Bảo đảm của UCT (Định lý 11.27) | `L11-3-10` (lợi tức ở gốc trôi) | ghi chú diễn giả (quy nạp theo độ sâu) | `L11-3-10` ($D=20$, $0{,}1216$) | `L11-3-10` | (a) dẫn nguồn; (b) "Chứng minh." ở ghi chú diễn giả | `L11-3-10` ($c_{\mathrm{ucb}}=28{,}28$) | Bài tập 11.9(a) (tự làm) |

Cái truyền từ ví dụ sang công thức: bảng $\bar G(a)$ với $m=2$ (`L11-3-01`) thành bước 1–3 của Thuật toán 11.20; $q_{\pi_0}(\mathrm F,\cdot)$ thành $\Delta=0{,}2072$ của Mệnh đề 11.22 và $0{,}2704$ của `L11-3-06`; chỉ số $1{,}4481$ thành (3.2); bảng T2 thành (3.3) và bốn pha của Thuật toán 11.26. Câu nối sang mạch 4 đặt ở dòng mở của `L11-4-01` (NT13, NT-RL-3).

#### `L11-3-00` 3. Tìm kiếm theo cây Monte Carlo (trang tiêu đề mạch), điểm vào mạch 3
- **Vị trí, bước:** điểm vào mạch 3; `section.strand-title`, `id="mach-3"`, `data-note-topic-id="lec-11-topic-11"`. Dòng dẫn nêu đúng nhu cầu của khái niệm đầu (lập kế hoạch tại thời điểm quyết định): bước `vấn đề` chung của cụm rollout.
- **Lý do tồn tại:** NT12.
- **Liên kết:** trước `L11-2-12` (giới hạn của lập kế hoạch nền); sau `L11-3-01`.
- **Mục tiêu:** 4.
- **Mặt trang:** "3." + "Tìm kiếm theo cây Monte Carlo"; `p.strand-lead` "Tìm kiếm từ trạng thái hiện tại dồn phép tính vào đúng một quyết định." (15); `p.strand-keys` "thuật toán rollout · số mô phỏng · cận tin cậy trên · chính sách cây".
- **Mật độ:** **Số đo cuối** (`deck_lint`, sau III.5): 15 âm tiết, trần 25, tỉ lệ 0,60.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT12.
- **Ghi chú diễn giả (40–100):** kế thừa: mô hình mẫu, Định nghĩa 11.2, và giới hạn của Dyna-Q (tính cho mọi cặp đã thử); việc của mạch: chọn tốt một hành động tại trạng thái hiện tại bằng mô phỏng (rollout), chia mô phỏng thông minh (cận tin cậy trên), dựng cây (MCTS); trao đi: hai bảo đảm cho mô hình đúng và giới hạn tập hành động hữu hạn.

#### `L11-3-01` Ví dụ: thuật toán rollout tại ô $\mathrm F$
- **Vị trí, bước:** mạch 3, trang nội dung đầu; vấn đề (câu khẳng định của mạch, NT13) → trực quan → ví dụ tính tay trước giả mã (NT-RL-2) của cụm rollout. NT-RL-3: dòng đầu nêu điều lập kế hoạch nền không làm (dồn phép tính vào $\mathrm F$).
- **Lý do tồn tại:** cho số cụ thể của chính sách cơ sở kém và ước lượng bằng mô phỏng trước khi phát biểu thuật toán.
- **Liên kết:** trước `L11-3-00`; sau `L11-3-02` (các bước thành thuật toán).
- **Mục tiêu:** 4.
- **Nguồn:** §3.1; Ví dụ 11.12; `lec-11-topic-11`.
- **Mặt trang:**
  - "Tại $\mathrm F$ chỉ cần một quyết định; phép tính dồn vào các hành động tại $\mathrm F$." (14)
  - "Chính sách cơ sở (base policy) $\pi_0$ chọn mỗi mũi tên với xác suất $1/4$: $v_{\pi_0}(\mathrm F)=0{,}2016<v_*(\mathrm F)=0{,}8566$." (13)
  - "Trực quan. Thử từng hành động trên mô hình, đi tiếp theo $\pi_0$ tới hết lượt, lấy trung bình lợi tức." (20)
  - Bảng hai hàng, cột $\rightarrow$, $\downarrow$, $\uparrow$, $\leftarrow$: $q_{\pi_0}(\mathrm F,a)$: $0{,}3886$; $0{,}1814$; $0{,}1181$; $0{,}1181$ / $\bar G(a)$, $m=2$: $0{,}5912$; $0{,}4658$; $0{,}3311$; $0{,}2364$.
  - "Diễn giải: $\bar G(\rightarrow)$ lớn nhất; hai mô phỏng mỗi hành động còn lệch $0{,}2027$." (12)
- **Mật độ:** 59 âm tiết (trước 67), 6 dòng. "Trùng hành động tham lam theo $q_{\pi_0}$" ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 58 âm tiết, trần 60, tỉ lệ 0,97.
- **Sau biên tập (2026-11-19):** $\bar G$, $m$ gọi tên trên mặt trang; độ lệch viết "$\bar G(\rightarrow)-q_{\pi_0}(\mathrm F,\rightarrow)=0{,}2027$".
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — lượt tính tay của thuật toán rollout (ghi chú thêm ở biên tập vòng 1, Q-B).
- **Ghi chú diễn giả:** $v_{\pi_0}$ là nghiệm hệ bảy phương trình (Định lý 03.28); $q_{\pi_0}(\mathrm F,a)=0{,}72\,v_{\pi_0}(s_a)+0{,}18\,v_{\pi_0}(\mathrm F)$ (Mệnh đề 03.22), $\downarrow$ đụng biên cho $0{,}9\,v_{\pi_0}(\mathrm F)$; tám mô phỏng: $\rightarrow$ vào $\mathrm Z$ ở bước $2$ và $13$, lợi tức $0{,}9$ và $\gamma^{12}=0{,}2824$, v.v.; $D=\infty$ vì với $\pi_0$ ngẫu nhiên đều lượt kết thúc với xác suất $1$; "thuật toán rollout" khác "đoạn thu (rollout)" của Bài 10.

#### `L11-3-02` Thuật toán rollout
- **Vị trí, bước:** mạch 3; hình thức (thuật toán) của cụm rollout; định nghĩa chính sách rollout. NT-RL-4: rollout là lập kế hoạch tại thời điểm quyết định.
- **Lý do tồn tại:** NT-RL-2 (đầu vào, đầu ra, tham số, thứ tự, điều kiện dừng; khớp `L11-3-01` với $m=2$, $D=\infty$); đặt tên $\pi_{\mathrm{ro}}$ dùng ở Mệnh đề 11.21.
- **Liên kết:** trước `L11-3-01`; sau `L11-3-03` ($\pi_{\mathrm{ro}}$ có tốt hơn $\pi_0$ không).
- **Mục tiêu:** 4.
- **Nguồn:** Thuật toán 11.20; đoạn sau thuật toán (chính sách rollout, luật số lớn); `lec-11-topic-11`.
- **Mặt trang:** "Thuật toán 11.20 (lập kế hoạch tại thời điểm quyết định)." rồi:
  - "Đầu vào: mô hình mẫu, chính sách cơ sở $\pi_0$ Markov dừng, trạng thái $s$; tham số $m$, độ sâu cắt $D$. Đầu ra: $A_t$." (21)
  - "Với mỗi $a\in\mathcal A(s)$: chạy $m$ mô phỏng từ $(s,a)$ theo $\pi_0$, dừng ở trạng thái kết thúc hoặc độ sâu $D$; $\bar G(a)$ là trung bình lợi tức." (23)
  - "Chọn $A_t\in\arg\max_a\bar G(a)$, phá hòa theo một quy tắc cố định." (10)
  - "Chính sách rollout (rollout policy): $\pi_{\mathrm{ro}}(s)\in\arg\max_aq_{\pi_0}(s,a)$; với mô hình đúng, $D=\infty$ và $m\to\infty$, $\bar G(a)\to q_{\pi_0}(s,a)$ hầu chắc chắn." (13)
- **Mật độ:** khoảng 77 âm tiết, 5 dòng: ngoại lệ (trang thuật toán, mục 4). **Số đo cuối** (`deck_lint`, sau III.5): 76 âm tiết, trần 80, tỉ lệ 0,95.
- **Sau biên tập (2026-11-19):** ghi chú diễn giả thêm trang Sutton và Barto.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — Thuật toán 11.20 có trong ghi chú đã duyệt (sai khác so với kế hoạch, mục 8).
- **Ghi chú diễn giả:** $D=\infty$ chỉ khi lượt kết thúc với xác suất $1$; chi phí $O(\lvert\mathcal A(s)\rvert\,m\,D)$ lời gọi mô hình mỗi quyết định; chạy rollout ở mọi trạng thái gặp trên đường là thực hiện $\pi_{\mathrm{ro}}$; Sutton và Barto (2018, §8.10) gọi $\pi_0$ là "rollout policy", bài theo cách gọi của Bertsekas; với mô hình sai, giới hạn là giá trị của $\pi_0$ trên MDP của mô hình.

#### `L11-3-03` Tính chất cải thiện của rollout
- **Vị trí, bước:** mạch 3; trực quan → phát biểu → ứng dụng (Ví dụ 11.13) của kết quả chính thứ nhất.
- **Lý do tồn tại:** câu trả lời 2 của câu hỏi trung tâm; phát biểu với đủ giả thiết (NT5).
- **Liên kết:** trước `L11-3-02`; sau `L11-3-04` (vì sao đúng).
- **Mục tiêu:** 4.
- **Nguồn:** Mệnh đề 11.21; Ví dụ 11.13; `lec-11-topic-11`.
- **Mặt trang:**
  - "Trực quan. Chọn tham lam theo $q_{\pi_0}$ ở mọi trạng thái là một bước cải thiện chính sách." (17)
  - "Mệnh đề 11.21. Giả thiết: MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; $\pi_0$ Markov dừng với $q_{\pi_0}$, $v_{\pi_0}$ chính xác; $\pi_{\mathrm{ro}}$ tham lam theo $q_{\pi_0}$ ở mọi $s$." (22)
  - "Kết luận: $v_{\pi_{\mathrm{ro}}}(s)\ge v_{\pi_0}(s)$ với mọi $s$, nghiêm ngặt tại $s$ khi $\max_aq_{\pi_0}(s,a)>v_{\pi_0}(s)$." (8)
  - "Ví dụ 11.13. Trên mê cung, $\pi_{\mathrm{ro}}$ đi đường ngắn nhất: tại $\mathrm F$, $0{,}2016$ lên $0{,}8566$." (12)
- **Mật độ:** 59 âm tiết (trước 58, chưa có trực quan), 4 dòng (dòng mệnh đề hai dòng hiển thị), 0 công thức hiển thị: ngoại lệ NT17, lý do: kết quả chính phát biểu đủ ba giả thiết (NT2, NT5) cùng bước trực quan bắt buộc đứng trước phát biểu (NT8, cổng). **Số đo cuối** (`deck_lint`, sau III.5): 58 âm tiết, trần 60, tỉ lệ 0,97.
- **Sau biên tập (2026-11-19):** "Trực quan. Tham lam theo $q_{\pi_0}$ là một bước cải thiện chính sách."; ví dụ viết "giá trị tại $\mathrm F$".
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — kết quả chính (NT6, Q16).
- **Ghi chú diễn giả:** "Ý nghĩa": rollout là một bước cải thiện chính sách (Định lý 04.13) thực hiện tại trạng thái gặp trên đường, cũng so được với một bước lặp giá trị bất đồng bộ (Sutton và Barto, 2018, tr. 184); Phạm vi: chỉ so với $\pi_0$, không bảo đảm tối ưu, Ví dụ 11.13 vượt xa "không giảm"; với mô hình sai, kết luận áp cho MDP của mô hình; Bertsekas (2020, Mệnh đề 5.4.2) phát biểu dạng chi phí. Bảng giá trị: $\mathrm A$ hòa $\downarrow$, $\rightarrow$ ở $0{,}0979$; $\mathrm C$: $\rightarrow$ $0{,}5102$ so với $\downarrow$ $0{,}4291$.

#### `L11-3-04` Ý tưởng chứng minh: tính chất cải thiện của rollout
- **Vị trí, bước:** mạch 3; ý tưởng chứng minh (NT6) → kiểm tra (bỏ giả thiết, NT4).
- **Lý do tồn tại:** Q16; cho thấy giả thiết "$q_{\pi_0}$ chính xác" vào ở bước nào.
- **Liên kết:** trước `L11-3-03`; sau `L11-3-05` (khi chỉ có trung bình của $m$ mô phỏng).
- **Mục tiêu:** 4.
- **Nguồn:** chứng minh Mệnh đề 11.21; đoạn "Hai giả thiết có vai trò riêng"; `lec-11-topic-11`.
- **Mặt trang:** ba bước đánh số và một dòng:
  1. "$q_{\pi_0}(s,\pi_{\mathrm{ro}}(s))=\max_aq_{\pi_0}(s,a)$ (giả thiết: $\pi_{\mathrm{ro}}$ tham lam)." (4)
  2. "Cực đại không nhỏ hơn trung bình có trọng số; đẳng thức cuối là Mệnh đề 03.23 (giả thiết: $\pi_0$ Markov dừng):" (19), công thức hiển thị $\max_aq_{\pi_0}(s,a)\ge\sum_a\pi_0(a\mid s)\,q_{\pi_0}(s,a)=v_{\pi_0}(s)$.
  3. "Định lý 04.13 cho $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$, nghiêm ngặt tại $s$ khi bước 2 nghiêm ngặt (giả thiết: $q_{\pi_0}$ chính xác)." (16)
  - "Lưu ý: với $m=1$, một mô phỏng may mắn có thể cho $\bar G(\uparrow)>\bar G(\rightarrow)$; hành động được chọn khi đó có $q_{\pi_0}(\mathrm F,\uparrow)=0{,}1181<v_{\pi_0}(\mathrm F)=0{,}2016$." (19); vế "và bước 1 không còn đúng" ở ghi chú diễn giả.
- **Mật độ:** khoảng 58 âm tiết (trước 61), 5 dòng, 1 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 47 âm tiết, trần 80, tỉ lệ 0,59.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — NT6, Q16.
- **Ghi chú diễn giả:** bỏ "$\pi_0$ Markov dừng": với $\pi_0$ phụ thuộc lịch sử, đẳng thức cuối của bước 2 không còn; Định lý 04.13 (nhắc lại ở `L11-1-02`) cần $\pi_0$ có giá trị chính xác; thực hiện rollout ở mọi trạng thái là thực hiện $\pi_{\mathrm{ro}}$.

#### `L11-3-05` Số mô phỏng của rollout
- **Vị trí, bước:** mạch 3; vấn đề (Mệnh đề 11.21 cần giá trị chính xác) → phát biểu → ví dụ số của Mệnh đề 11.22.
- **Lý do tồn tại:** mục tiêu 4 ("tính số mô phỏng đủ cho một xác suất chọn sai cho trước"); câu trả lời 2 dùng $m=70$.
- **Liên kết:** trước `L11-3-04` (bỏ giả thiết "$q_{\pi_0}$ chính xác"); sau `L11-3-06` (chia đều $m$ cho cả hành động kém).
- **Mục tiêu:** 4.
- **Nguồn:** §3.1; Mệnh đề 11.22 và chứng minh; Ví dụ 11.14; `lec-11-topic-11`.
- **Mặt trang:**
  - "Rollout chỉ có trung bình của $m$ mô phỏng thay cho $q_{\pi_0}$ chính xác." (12)
  - "Nhắc lại: bất đẳng thức Hoeffding (Mệnh đề 06.26)." (9)
  - "Mệnh đề 11.22. Giả thiết: mô hình mẫu đúng; $\Delta=q_{\pi_0}(s,a)-q_{\pi_0}(s,a')>0$; $m$ chọn trước; mô phỏng độc lập, không cắt, lợi tức trong một đoạn độ rộng $B$. Bảo đảm:" (26)
  - công thức hiển thị (3.1) $\Pr\{\bar G(a')\ge\bar G(a)\}\le\exp(-m\Delta^2/B^2)$.
  - "Ví dụ 11.14. Tại $\mathrm F$, $\Delta=0{,}2072$, $B=1$: chặn không vượt $0{,}05$ khi $m\ge\ln20/\Delta^2=69{,}8$; $m=70$ cho $0{,}0496$." (9)
- **Mật độ:** 56 âm tiết (trước 68), 5 dòng, 1 công thức hiển thị. Phát biểu của Hoeffding ở ghi chú diễn giả (đã có ở Bài 06). **Số đo cuối** (`deck_lint`, sau III.5): 56 âm tiết, trần 60, tỉ lệ 0,93.
- **Sau biên tập (2026-11-19):** cặp hành động gọi tên: $a=\rightarrow$, $a'=\downarrow$ (D-1).
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — tách khỏi trang Mệnh đề 11.21 của kế hoạch (mục 3, lý do 2).
- **Ghi chú diễn giả:** "Chứng minh." (kết quả phụ): $Z=\sum_iG_i(a')-\sum_iG_i(a)$ có kỳ vọng $-m\Delta$, là tổng $2m$ biến độc lập độ rộng $B$; Hoeffding một phía với $t=m\Delta$ cho $\exp(-2m^2\Delta^2/(2mB^2))$. Phạm vi: không áp dụng khi $m$ chọn theo kết quả mô phỏng; cắt ở $D=20$ cho $\Delta^{20}=0{,}2122$, chặn $0{,}0428$. Nhắc lại bất đẳng thức hợp $\Pr(\bigcup_iE_i)\le\sum_i\Pr(E_i)$: với bốn hành động, Bài tập 11.8 (tự làm) cho $m=75$; $m=50$ cho $0{,}1170$.

#### `L11-3-06` Quy tắc cận tin cậy trên
- **Vị trí, bước:** mạch 3; vấn đề (giới hạn của rollout, NT-RL-3) → trực quan → ví dụ (Ví dụ 11.15) → định nghĩa (Định nghĩa 11.23) → bảo đảm (Định lý 11.24) của cụm cận tin cậy trên (công cụ `cầu nối`, Q3).
- **Lý do tồn tại:** chỉ số (3.2) là phép chọn cạnh của MCTS; mục tiêu 4 ("tính chỉ số cận tin cậy trên").
- **Liên kết:** trước `L11-3-05` ($\exp(-0{,}0731\,m)$ đã nhỏ); sau `L11-3-07` (áp chỉ số ở mỗi nút của cây).
- **Mục tiêu:** 4.
- **Nguồn:** §3.2; Ví dụ 11.15; Định nghĩa 11.23; Định lý 11.24; `lec-11-topic-12`.
- **Mặt trang:**
  - "Rollout chia đều $m$ mô phỏng, kể cả cho $\uparrow$: $0{,}1181$, kém xa $0{,}3886$ của $\rightarrow$." (11)
  - "Nhắc lại: chọn lặp lại một bước (multi-armed bandit, Định nghĩa 01.16), $N(a)$ lần chọn, trung bình phần thưởng $\bar r(a)$." (18)
  - "Ví dụ 11.15, bước $t=9$: $\bar r(1)=0{,}6$, $N(1)=6$ cho chỉ số $1{,}2051$; $\bar r(2)=0{,}4$, $N(2)=2$ cho $1{,}4481$: chọn hành động 2." (12)
  - "Định nghĩa 11.23. Quy tắc cận tin cậy trên (upper confidence bound, UCB) chọn" (14)
  - công thức hiển thị (3.2) $A_t\in\arg\max_a\bigl[\bar r(a)+c_{\mathrm{ucb}}\sqrt{\ln t/N(a)}\bigr]$, hành động có $N(a)=0$ chọn trước (chữ dưới công thức, KaTeX).
  - "Định lý 11.24. Giả thiết: phần thưởng trong $[0,1]$, độc lập, phân phối không đổi; quy tắc UCB1, biến thể của (3.2) với $c_{\mathrm{ucb}}=\sqrt2$. Bảo đảm: hối tiếc kỳ vọng tăng theo $\ln t$." (30)
- **Mật độ:** 85 âm tiết (trước 85), 6 dòng, 1 công thức hiển thị: ngoại lệ NT17, lý do: định nghĩa và định lý của công cụ `cầu nối` (Q3) phải có "Giả thiết:" và "Bảo đảm:" riêng (NT5, cổng); UCB1 gọi là "biến thể của (3.2) với $c_{\mathrm{ucb}}=\sqrt2$" trên mặt trang; hai điểm khác còn lại ($\ln(t-1)$, khởi tạo chọn mỗi hành động một lần) và bước trực quan ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 89 âm tiết, trần 60, tỉ lệ 1,48.
- **Sau biên tập (2026-11-19):** "Trực quan." gộp với Ví dụ 11.15 (D-7); dòng mở "cả cho $\uparrow$ ($0{,}1181$) lẫn $\rightarrow$ ($0{,}3886$)"; "chọn 2"; câu dẫn mang số (3.2) (D-3); "chọn trước $a$ có $N(a)=0$"; định nghĩa "hối tiếc (regret)" ở ghi chú diễn giả.
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — gộp ví dụ, định nghĩa và bảo đảm (mã L11-3-04 của `ke-hoach-trang-chieu.md`); số liệu theo ghi chú đã biên tập ($\ln9$, chỉ số $1{,}2051$ và $1{,}4481$; kế hoạch ghi $1{,}189$, $1{,}420$ với $\ln8$).
- **Ghi chú diễn giả:** trực quan; UCB1 khác (3.2) ở ba điểm ($c_{\mathrm{ucb}}=\sqrt2$, $\ln(t-1)$, khởi tạo chọn mỗi hành động một lần); Định lý 11.24 dẫn Auer, Cesa-Bianchi và Fischer (2002, Định lý 1), không chứng minh; chặn số lần chọn $8\ln t/\Delta_a^2+1+\pi^2/3$; phản ví dụ: phân phối đổi từ bước $1\,000$ thì quy tắc chậm phát hiện; ở các nút trong của cây, giả thiết "cùng phân phối" không thỏa (Kocsis và Szepesvári, 2006, §2.2). Bài tự làm 11.18 (Sutton và Barto Bài tập 2.8).

#### `L11-3-07` Ví dụ: một vòng tìm kiếm theo cây tại $\mathrm F$, pha chọn
- **Vị trí, bước:** mạch 3; vấn đề (giới hạn của rollout, NT-RL-3) → trực quan → ví dụ tính tay trước giả mã (NT-RL-2) → định nghĩa (Định nghĩa 11.25) của cụm MCTS.
- **Lý do tồn tại:** pha chọn với số cụ thể; khuôn bảng T2 dùng lại ở Bài tập 11.5 (NT-RL-5).
- **Liên kết:** trước `L11-3-06` (chỉ số (3.2)); sau `L11-3-08` (ba pha còn lại).
- **Mục tiêu:** 4.
- **Nguồn:** §3.3; Ví dụ 11.16 (dữ kiện, bảng, bước chọn); Định nghĩa 11.25; `lec-11-topic-13`.
- **Mặt trang:**
  - "Rollout không dùng mô phỏng trước để chọn mô phỏng sau." (11)
  - "Trực quan. Cây gốc $\mathrm F$ ghi $N$, $W$, $\bar Q=W/N$ ở mỗi cạnh và chọn cạnh theo cận tin cậy trên; tính bốn chỉ số sau tám vòng (Ví dụ 11.16):" (26)
  - Bảng khuôn T2 bốn hàng; tiêu đề cột ghi $\sqrt{\ln8/N(\mathrm F,a)}$ và "chỉ số, $c_{\mathrm{ucb}}=1$" (không chú thích riêng): $\rightarrow$ | $4$ | $2{,}7729$ | $0{,}6932$ | $0{,}7210$ | $1{,}4142$; $\downarrow$ | $2$ | $1{,}1875$ | $0{,}5938$ | $1{,}0197$ | $1{,}6134$; $\uparrow$ | $1$ | $0{,}3138$ | $0{,}3138$ | $1{,}4420$ | **$1{,}7558$, chọn**; $\leftarrow$ | $1$ | $0{,}2059$ | $0{,}2059$ | $1{,}4420$ | $1{,}6479$ (hàng chọn đánh dấu bằng chữ, không chỉ bằng màu).
  - "Định nghĩa 11.25. Với $N(s)=\sum_aN(s,a)$, chính sách cây (tree policy) chọn cạnh có chỉ số UCT (upper confidence bounds applied to trees) $\bar Q(s,a)+c_{\mathrm{ucb}}\sqrt{\ln N(s)/N(s,a)}$ lớn nhất; cạnh có $N(s,a)=0$ được chọn trước; ngoài cây theo $\pi_0$." (32)
- **Mật độ:** 71 âm tiết (trước 50, chưa có định nghĩa), 7 dòng (câu giới hạn, dòng "Trực quan.", bảng bốn hàng, dòng định nghĩa hai dòng hiển thị), công thức chỉ số viết trong dòng: ngoại lệ NT17 về âm tiết và số dòng, lý do: câu giới hạn của rollout (NT-RL-3) và nhãn "Trực quan." đứng đầu dòng (NT19) không gộp được; Định nghĩa 11.25 chuyển về đây để $\bar Q$, $N(\mathrm F)$ và chỉ số được định nghĩa trên trang dùng chúng (NT9, cổng), đứng sau bảng (ví dụ trước phát biểu, NT8). $D=20$ và hai lần trượt trước đó ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 65 âm tiết, trần 60, tỉ lệ 1,08.
- **Sau biên tập (2026-11-19):** "và chọn cạnh theo cận tin cậy trên" trên mặt trang, vế "dùng cho mô phỏng sau" ở ghi chú diễn giả (trang sát chân trang).
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — ví dụ tính tay trước Thuật toán 11.26 (NT-RL-2).
- **Ghi chú diễn giả:** lợi tức đã nhận qua tám vòng: $\gamma,\gamma^2,\gamma^6,\gamma^6$ qua $\rightarrow$; $\gamma^4,\gamma^6$ qua $\downarrow$; $\gamma^{11}$ qua $\uparrow$; $\gamma^{15}$ qua $\leftarrow$; vì hai lần trượt, $\mathrm B$ và $\mathrm E$ ở độ sâu $1$ chưa có trong cây; $\ln8=2{,}0794$, $\sqrt{0{,}5199}=0{,}7210$; cạnh ít mẫu có số hạng thăm dò lớn nên $\uparrow$ thắng dù $\bar Q$ nhỏ.

#### `L11-3-08` Ví dụ: một vòng tìm kiếm theo cây tại $\mathrm F$, mở rộng, mô phỏng, cập nhật ngược
- **Vị trí, bước:** mạch 3; ví dụ tính tay (tiếp) → ứng dụng (AlphaGo Zero, NT-RL-11).
- **Lý do tồn tại:** hoàn tất một vòng; cho số $N=2$, $W=1{,}0428$, $\bar Q=0{,}5214$, $N(\mathrm F)=9$ mà Bài tập 11.5 dùng.
- **Liên kết:** trước `L11-3-07`; sau `L11-3-09` (bốn pha thành thuật toán).
- **Mục tiêu:** 4.
- **Nguồn:** Ví dụ 11.16 (mở rộng, mô phỏng, cập nhật ngược, hành động thật); hình bốn pha; Nhận xét 11.28; Ứng dụng sau Tình huống 11.2; `lec-11-topic-13`, `lec-11-topic-14`.
- **Mặt trang:**
  - "Mở rộng: mô hình mẫu trả $\mathrm B$ cho $(\mathrm F,\uparrow)$; cây thêm nút $\mathrm B$, mọi thống kê bằng $0$." (17)
  - "Mô phỏng theo $\pi_0$: $\mathrm B\to\mathrm F\to\mathrm K\to\mathrm Z$ không trượt; tính từ cạnh gốc, $G=\gamma^3=0{,}729$." (11)
  - "Cập nhật ngược: $N(\mathrm F,\uparrow)=2$, $W(\mathrm F,\uparrow)=0{,}3138+0{,}729=1{,}0428$, $\bar Q(\mathrm F,\uparrow)=0{,}5214$; $N(\mathrm F)=9$; $N(\mathrm B)=0$." (3)
  - "Hết ngân sách thì chọn cạnh gốc có $N$ lớn nhất: $\rightarrow$, $N=4$." (13)
  - "Lưu ý: AlphaGo Zero thay pha mô phỏng bằng giá trị nút lá do một mạng nơ-ron cho (Nhận xét 11.28)." (19)
  Dưới các dòng: dải hình `mcts-bon-pha-slide.svg`.
- **Mật độ:** khoảng 63 âm tiết (trước 72), 5 dòng, dải hình toàn bề rộng dưới chữ: ngoại lệ NT17 nhỏ, lý do: ba pha còn lại của ví dụ tính tay giữ một bước mỗi dòng (NT23) cùng dòng lịch sử NT-RL-11; nếu `deck_lint` > 60, chuyển dòng "Hết ngân sách …" vào ghi chú diễn giả (còn khoảng 50). Ghi chú diễn giả nói Nhận xét 11.28 là nội dung đọc thêm (NT5). **Số đo cuối** (`deck_lint`, sau III.5): 47 âm tiết, trần 60, tỉ lệ 0,78.
- **Sau biên tập (2026-11-19):** ghi chú diễn giả trình bày AlphaGo, AlphaGo Zero theo NT-RL-11, có mục và trang nguồn.
- **Hình, phút:** `mcts-bon-pha-slide.svg`; 2,5.
- **Quyết định:** thêm — ví dụ tiếp, cùng tiêu đề thêm tên bước (NT16, NT23); dòng lịch sử theo NT-RL-11: đặt ngay sau pha mô phỏng vừa tính, nêu thay đổi phương pháp (bỏ pha mô phỏng, mạng cho giá trị lá và xác suất tiên nghiệm); tên AlphaGo Zero giữ vì nó gọi tên thay đổi đó; không mốc năm, không danh sách niên đại.
- **Ghi chú diễn giả:** nút $\mathrm B$ giữ $N(\mathrm B)=0$ vì chưa cạnh nào ra từ $\mathrm B$ được đi trong cây; đoạn mô phỏng ngoài cây chỉ góp lợi tức rồi bị bỏ; quan hệ AlphaGo → AlphaGo Zero (NT-RL-11, chỉ tên khi giải thích thay đổi): AlphaGo dùng tìm kiếm theo cây cùng mạng chính sách và mạng giá trị; AlphaGo Zero dùng một mạng hai đầu ra, chính sách cây là biến thể của PUCT (Silver và cộng sự, 2017; Sutton và Barto, 2018, §16.6.2, tr. 447–450); Nhận xét 11.28 là nội dung đọc thêm của ghi chú (NT5).

#### `L11-3-09` Thuật toán tìm kiếm theo cây Monte Carlo với UCT
- **Vị trí, bước:** mạch 3; thuật toán (Thuật toán 11.26) của cụm MCTS; Định nghĩa 11.25 đã ở `L11-3-07`.
- **Lý do tồn tại:** NT-RL-2: thứ tự bốn pha, tham số, điều kiện dừng, khớp `L11-3-07`, `L11-3-08`.
- **Liên kết:** trước `L11-3-08`; sau `L11-3-10` (thuật toán này có bảo đảm gì).
- **Mục tiêu:** 4.
- **Nguồn:** Thuật toán 11.26; `lec-11-topic-13`.
- **Mặt trang:**
  - "Thuật toán 11.26. Đầu vào: $s_0$, mô hình mẫu, $\pi_0$, $c_{\mathrm{ucb}}$, ngân sách vòng lặp, độ sâu $D$. Đầu ra: cạnh gốc có $N(s_0,a)$ lớn nhất. Mỗi vòng:" (23)
  - danh sách đánh số ba dòng:
  - "Chọn theo chỉ số UCT từ gốc tới trạng thái mới, trạng thái kết thúc hoặc độ sâu $D$." (18)
  - "Mở rộng: thêm trạng thái đó; mô phỏng theo $\pi_0$ tới kết thúc hoặc độ sâu $D$." (15)
  - "Cập nhật ngược: mỗi cạnh đã đi trong cây tăng $N$ thêm $1$, cộng lợi tức từ cạnh đó vào $W$." (18)
- **Mật độ:** 74 âm tiết (trước 90–99), 4 dòng, 0 công thức hiển thị; trang thuật toán, trần 80 của cổng: đạt. **Số đo cuối** (`deck_lint`, sau III.5): 80 âm tiết, trần 80, tỉ lệ 1,00.
- **Sau biên tập (2026-11-19):** bốn bước đánh số có tên tiếng Anh (selection, expansion, simulation, backup), khớp "bốn pha"; tên "Monte Carlo tree search, MCTS" lần đầu; độ sâu cắt (truncation depth).
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — trang thuật toán riêng.
- **Ghi chú diễn giả:** UCT là "upper confidence bounds applied to trees"; (3.3) là (3.2) áp ở mỗi nút với $N(s)$ ở vị trí $t-1$; nút là cặp (trạng thái, độ sâu); bốn pha của Sutton và Barto (2018, §8.11, tr. 187): selection, expansion, simulation, backup; khi cây chỉ có gốc và chính sách cây chọn đều, thuật toán trở về thuật toán rollout; chi phí: mỗi vòng nhiều nhất $D$ lời gọi mô hình, bộ nhớ tăng một nút.

#### `L11-3-10` Bảo đảm của UCT
- **Vị trí, bước:** mạch 3; vấn đề (lợi tức ở gốc trôi) → phát biểu (Định lý 11.27) → ứng dụng ($D=20$).
- **Lý do tồn tại:** kết quả nêu trong câu trả lời 2; phân biệt UCT của nguồn với Thuật toán 11.26 (Q-F của biên tập ghi chú).
- **Liên kết:** trước `L11-3-09`; sau `L11-3-11`.
- **Mục tiêu:** 4, 7.
- **Nguồn:** §3.4; Định lý 11.27 và chứng minh (b); đoạn sau chứng minh; `lec-11-topic-14`.
- **Mặt trang:**
  - "Lợi tức ở gốc trôi, nên Định lý 11.24 không áp dụng trực tiếp." (14)
  - "Định lý 11.27. Giả thiết: hành động hữu hạn; mô hình mẫu đúng; bài toán cắt ở độ sâu $D$, giá trị tối ưu $v^D_*$." (23)
  - "Bảo đảm: (a) với phần thưởng trong $[0,1]$, $c_{\mathrm{ucb}}=\sqrt2\,D$, hành động tối ưu duy nhất: xác suất UCT chọn sai ở gốc $\to0$ khi số vòng lặp $\to\infty$." (24)
  - "(b) Với phần thưởng không âm, lợi tức trong $[0,1]$: $0\le v_*(s)-v^D_*(s)\le\gamma^D$; $D=20$ cho $0{,}1216$." (10)
  - "Lưu ý: (a) không có chứng minh cho Thuật toán 11.26; với $D=20$, (a) cần $c_{\mathrm{ucb}}=28{,}28$." (14)
- **Mật độ:** 85 âm tiết (trước 88 sau rút), 5 dòng, 0 công thức hiển thị: ngoại lệ NT17, lý do: định lý hai phần giữ đủ giả thiết và phạm vi như ghi chú (NT2; phát hiện nghiêm trọng của cổng: $v^D_*$ định nghĩa trên mặt trang, (a) không được chứng minh cho Thuật toán 11.26). **Số đo cuối** (`deck_lint`, sau III.5): 89 âm tiết, trần 60, tỉ lệ 1,48.
- **Sau biên tập (2026-11-19):** "Trực quan. Trung bình ở mỗi nút trôi theo các nút dưới, trái giả thiết của Định lý 11.24." thay câu "lợi tức ở gốc trôi" (D-7); (a): "hành động tối ưu duy nhất của bài toán cắt: xác suất UCT chọn hành động khác ở gốc $\to0$" (D-2); "Lưu ý: (a) không được chứng minh cho Thuật toán 11.26; $D=20$: $c_{\mathrm{ucb}}=28{,}28$"; "$D=20$ cho $0{,}1216$" ở ghi chú diễn giả.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — kết quả dẫn nguồn (Kocsis và Szepesvári, 2006, Định lý 6), không trang ý tưởng chứng minh riêng (Q16).
- **Ghi chú diễn giả:** $v^D_\pi$ là giá trị của bài toán cắt (lợi tức trong $D$ bước đầu); trực quan: ở mỗi nút UCT giải một bài toán chọn lặp lại có trung bình trôi dần; khi các nút sâu ổn định, nút trên ổn định; ý tưởng (a): quy nạp theo $D$, $D=1$ là UCB1 (Kocsis, Szepesvári và Willemson, 2006, Định lý 7); "Chứng minh." (b): hiệu hai lợi tức là phần thưởng từ bước $D$, bằng $\gamma^D\mathbb E[\mathbb 1\{D<T\}v_\pi(S_D)]\in[0,\gamma^D]$, rồi so qua $\pi_*$; (a) là tiệm cận, không cho số vòng lặp; phản ví dụ: phần thưởng $+10$ cho chặn $10\gamma^D$.

#### `L11-3-11` Bài tập: vòng tìm kiếm theo cây tiếp theo
- **Vị trí, bước:** mạch 3; kiểm tra của cụm MCTS (đề, lời giải fragment).
- **Lý do tồn tại:** NT24; cùng khuôn T2 với `L11-3-07` (NT-RL-5).
- **Liên kết:** trước `L11-3-10`; sau `L11-4-00`.
- **Mục tiêu:** 4.
- **Nguồn:** Bài tập 11.5 và lời giải; `lec-11-topic-27`.
- **Mặt trang:**
  - "Câu hỏi (Bài tập 11.5): sau Ví dụ 11.16, $N(\mathrm F)=9$, $c_{\mathrm{ucb}}=1$, $\gamma=0{,}9$. (a) Cạnh nào được chọn? (b) Mở rộng ra $\mathrm E$ và mô phỏng $\mathrm E\to\mathrm F\to\mathrm K\to\mathrm Z$ không trượt: tính thống kê mới của cạnh đó." (31; hai dòng hiển thị)
  - Bảng khuôn T2 bốn hàng; ba cột đầu là dữ kiện, hai cột cuối là fragment: $\rightarrow$ | $4$ | $2{,}7729$ | $0{,}6932$ | $0{,}7412$ | $1{,}4344$; $\downarrow$ | $2$ | $1{,}1875$ | $0{,}5938$ | $1{,}0481$ | $1{,}6419$; $\uparrow$ | $2$ | $1{,}0428$ | $0{,}5214$ | $1{,}0481$ | $1{,}5696$; $\leftarrow$ | $1$ | $0{,}2059$ | $0{,}2059$ | $1{,}4823$ | $1{,}6882$.
  - fragment "Lời giải: (a) chọn $\leftarrow$, chỉ số $1{,}6882$; (b) $G=\gamma^3=0{,}729$, $N=2$, $W=0{,}2059+0{,}729=0{,}9349$, $\bar Q=0{,}4674$; $N(\mathrm F)=10$; $N(\mathrm E)=0$." (6)
- **Mật độ:** khoảng 50 âm tiết, 6 dòng (dòng câu hỏi tính một gạch đầu dòng hai dòng hiển thị), 0 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 43 âm tiết, trần 60, tỉ lệ 0,72.
- **Sau biên tập (2026-11-19):** lời giải hai dòng fragment ((a); (b) với $N(\mathrm F)$, $N(\mathrm E)$); phép cộng $W$ ở ghi chú diễn giả (trang tràn khung khi để trên mặt).
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — gộp đề và lời giải (mã L11-3-09, L11-3-10 của `ke-hoach-trang-chieu.md`) bằng fragment; số liệu theo ghi chú đã biên tập (kế hoạch ghi $1{,}441$; $1{,}648$; $1{,}563$; $1{,}682$ và $0{,}4645$).
- **Ghi chú diễn giả (NT-RL-10):** năng lực kiểm: tính chỉ số UCT với $N(\mathrm F)$ mới và cập nhật ngược đúng cạnh. "Gợi ý: dùng (3.3) với $\ln9=2{,}1972$." Lỗi thường gặp: dùng $\ln8$ của vòng trước; đường $\mathrm F\to\mathrm E\to\mathrm F\to\mathrm K\to\mathrm Z$ có bốn bước tính từ cạnh gốc, phần thưởng ở bước cuối, nên $G=\gamma^3$. Kết quả của mạch: rollout không làm giảm giá trị khi $q_{\pi_0}$ chính xác, $m=70$ đủ cho chặn $0{,}0496$, UCT nhất quán cho bài toán cắt; cả hai cần tập hành động hữu hạn.

### Mạch 4. Tối ưu kế hoạch dựa trên đạo hàm (9 trang, 20 phút)

| Cụm | Vấn đề | Trực quan | Ví dụ | Hình thức | Ý tưởng chứng minh | Ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|---|
| Bài toán tối ưu kế hoạch | `L11-4-01` (giới hạn của MCTS; câu khẳng định của mạch) | `L11-4-01` | `L11-4-01` (Ví dụ 11.17, $J=8$) | `L11-4-02` (Định nghĩa 11.29) | không áp dụng | `L11-4-02` (một bước gradient) | `L11-4-08` |
| Gradient qua mô hình (Mệnh đề 11.30) | `L11-4-02` (cần $\partial J/\partial u_t$) | `L11-4-03` | `L11-4-02` (khai triển), `L11-4-03` (truy hồi ngược) | `L11-4-03` | "Chứng minh." một dòng | `L11-4-04` (Thuật toán 11.31, Ví dụ 11.19) | `L11-4-08` (a) |
| Điều khiển dự báo | `L11-4-05` (vòng hở không phản ứng) | `L11-4-05` | `L11-4-05` (Ví dụ 11.20) | `L11-4-05` (Định nghĩa 11.32, Thuật toán 11.33) | không áp dụng | `L11-4-07` | Bài tập 11.11 (tự làm) |
| Phương pháp entropy chéo (`bổ sung`) | ghi chú diễn giả `L11-4-04` | ghi chú diễn giả | Ví dụ 11.21 chỉ ở ghi chú (Q15) | `L11-4-04`, một dòng "Cách khác:" | không áp dụng | — | — |
| Sai số tích lũy (Mệnh đề 11.36) | `L11-4-06` (hệ thật nghiêng) | `L11-4-06` | `L11-4-06` (Ví dụ 11.22) | `L11-4-06` | "Chứng minh." một dòng | `L11-4-07` (Ví dụ 11.23) | Bài tập 11.11(c) (tự làm) |

Cái truyền từ ví dụ sang công thức: $J(0;0)=8$ và khai triển (`L11-4-01`, `L11-4-02`) thành (4.1); gradient $(8;\,4)$ hai cách thành (4.2), (4.3); điểm dừng $(-1{,}2;\,-0{,}4)$ thành Thuật toán 11.31; $u_0^*=-0{,}6x_0$ thành Định nghĩa 11.32; $e_k=2(1{,}2^k-1)$ thành (4.4) với dấu bằng. Bước tính tay đứng trước mọi giả mã (NT-RL-2): `L11-4-02` trước `L11-4-04`; Ví dụ 11.20 trước dòng Thuật toán 11.33 trên `L11-4-05`. Câu nối sang mạch 5 ở dòng mở của `L11-5-01`.

#### `L11-4-00` 4. Tối ưu kế hoạch dựa trên đạo hàm (trang tiêu đề mạch), điểm vào mạch 4
- **Vị trí, bước:** điểm vào mạch 4; `section.strand-title`, `id="mach-4"`, `data-note-topic-id="lec-11-topic-15"`. Dòng dẫn nêu đúng nhu cầu của khái niệm đầu (tối ưu kế hoạch bằng đạo hàm): bước `vấn đề` chung.
- **Lý do tồn tại:** NT12.
- **Liên kết:** trước `L11-3-11`; sau `L11-4-01`.
- **Mục tiêu:** 5.
- **Mặt trang:** "4." + "Tối ưu kế hoạch dựa trên đạo hàm"; `p.strand-lead` "Khi mô hình khả vi, đạo hàm theo chuỗi hành động cho biết hướng sửa kế hoạch." (17); `p.strand-keys` "tối ưu kế hoạch · truy hồi ngược · điều khiển dự báo · sai số tích lũy".
- **Mật độ:** **Số đo cuối** (`deck_lint`, sau III.5): 17 âm tiết, trần 25, tỉ lệ 0,68.
- **Sau biên tập (2026-11-19):** dòng dẫn "Khi mô hình khả vi, đạo hàm theo chuỗi hành động cho biết hướng sửa kế hoạch." (17).
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT12.
- **Ghi chú diễn giả (40–100):** kế thừa: lập kế hoạch tại thời điểm quyết định (Định nghĩa 11.2) và giới hạn của cây (tập hành động hữu hạn); việc của mạch: đổi sang trạng thái và hành động liên tục, tối ưu chuỗi hành động qua mô hình khả vi, lập kế hoạch lại mỗi bước; trao đi: sai số mô hình tích lũy theo chân trời, số hành động cần tối ưu tăng theo $h$.

#### `L11-4-01` Ví dụ: xe trên đường ray
- **Vị trí, bước:** mạch 4, trang nội dung đầu; vấn đề (giới hạn của MCTS, NT-RL-3; câu khẳng định của mạch, NT13) → trực quan → ví dụ dẫn nhập (ví dụ xuyên suốt thứ hai).
- **Lý do tồn tại:** dữ kiện liệt kê ngay (NT14); kế hoạch "không làm gì" cho mốc $J=8$.
- **Liên kết:** trước `L11-4-00`; sau `L11-4-02`.
- **Mục tiêu:** 5.
- **Nguồn:** kết mục §3; §4.1; Ví dụ 11.17; `lec-11-topic-15`.
- **Mặt trang:**
  - "Rollout và cây tìm kiếm cần tập hành động hữu hạn; độ dịch chuyển $u_t\in\mathbb R$ của xe không liệt kê được, nhưng mô hình khả vi cho đạo hàm theo $u_t$." (29)
  - "Ví dụ 11.17: vị trí $x_t\in\mathbb R$, mốc $0$; mô hình $\hat f(x,u)=x+u$; chi phí mỗi bước $x_{t+1}^2+u_t^2$; chân trời $h=2$, không chiết khấu; $x_0=2$." (17)
  - "Trực quan. Chạy thử chuỗi hành động trên mô hình, sửa chuỗi cho chi phí giảm." (16)
  - Bảng khuôn T3, một hàng: $(0;\,0)$ | $2$; $2$ | $8$.
- **Mật độ:** 62 âm tiết (trước 67), 4 dòng. **Số đo cuối** (`deck_lint`, sau III.5): 66 âm tiết, trần 60, tỉ lệ 1,10.
- **Sau biên tập (2026-11-19):** dữ kiện Ví dụ 11.17 thành danh sách hai mục, giữ 6 dòng.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — ví dụ xuyên suốt thứ hai của ghi chú.
- **Ghi chú diễn giả:** chi phí $c\ge0$, cực tiểu tổng chi phí tương đương cực đại tổng phần thưởng $-c$; $J(u_0,u_1)=x_1^2+u_0^2+x_2^2+u_1^2$ với $x_1=x_0+u_0$, $x_2=x_1+u_1$; mạch này dùng $x_t,u_t$ thay $S_t,A_t$ vì trạng thái và hành động liên tục.

#### `L11-4-02` Bài toán tối ưu kế hoạch
- **Vị trí, bước:** mạch 4; hình thức (Định nghĩa 11.29) → ví dụ tính tay một bước gradient (Ví dụ 11.18, NT-RL-2).
- **Lý do tồn tại:** đặt (4.1) và phép bắn; cho gradient $(8;\,4)$ bằng khai triển trước khi có công thức truy hồi.
- **Liên kết:** trước `L11-4-01`; sau `L11-4-03` (tính gradient khi $h$ lớn).
- **Mục tiêu:** 5.
- **Nguồn:** Định nghĩa 11.29; đoạn sau định nghĩa (vòng hở); Ví dụ 11.18; `lec-11-topic-15`, `lec-11-topic-16`.
- **Mặt trang:**
  - "Định nghĩa 11.29. Cho $x_0$, mô hình tất định $\hat f$, chi phí $c\ge0$, chân trời $h$; bài toán tối ưu kế hoạch (trajectory optimization) là" (15), công thức hiển thị (4.1) $\min_{u_0,\dots,u_{h-1}}J=\sum_{t=0}^{h-1}c(x_{t+1},u_t)$, $x_{t+1}=\hat f(x_t,u_t)$.
  - "Viết $J$ chỉ theo chuỗi hành động là phép bắn (shooting); lời giải là kế hoạch vòng hở (open-loop) cho một trạng thái đầu." (22)
  - "Ví dụ 11.18. $J=(x_0+u_0)^2+u_0^2+(x_0+u_0+u_1)^2+u_1^2$; tại $(0;\,0)$, $\partial J/\partial u_0=8$, $\partial J/\partial u_1=4$." (2)
  - "Một bước hạ gradient, tốc độ học $\eta=0{,}1$:" (7), bảng khuôn T3 một hàng: $(-0{,}8;\,-0{,}4)$ | $1{,}2$; $0{,}8$ | $2{,}88$.
- **Mật độ:** khoảng 52 âm tiết, 5 dòng, 1 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 59 âm tiết, trần 60, tỉ lệ 0,98.
- **Sau biên tập (2026-11-19):** câu dẫn "… là bài toán (4.1):" (D-3); tên "phép bắn đơn (single shooting)"; "tốc độ học" chuyển vào ghi chú diễn giả.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — định nghĩa sau ví dụ dẫn nhập (NT8).
- **Ghi chú diễn giả:** đạo hàm khai triển: $\partial J/\partial u_0=2(x_0+u_0)+2u_0+2(x_0+u_0+u_1)$; kế hoạch vòng hở khác chính sách Markov dừng (Định nghĩa 03.13); giải (4.1) bằng đạo hàm là tối ưu kế hoạch dựa trên đạo hàm (gradient-based planning); hạ gradient nhắc lại Định nghĩa 08.16 ($\theta\leftarrow\theta-\eta g$); $J$ giảm từ $8$ xuống $2{,}88$.

#### `L11-4-03` Đạo hàm qua mô hình bằng truy hồi ngược
- **Vị trí, bước:** mạch 4; trực quan → phát biểu (Mệnh đề 11.30) → ví dụ (bản thứ hai của Ví dụ 11.18, hai bản cùng kết quả, GC-RL-11).
- **Lý do tồn tại:** với $h$ lớn, khai triển không dùng được; truy hồi ngược cho mọi đạo hàm trong một lượt.
- **Liên kết:** trước `L11-4-02` (gradient $(8;\,4)$ bằng khai triển); sau `L11-4-04`.
- **Mục tiêu:** 5.
- **Nguồn:** §4.2; Mệnh đề 11.30 và chứng minh; "Bản truy hồi ngược của Ví dụ 11.18"; `lec-11-topic-16`.
- **Mặt trang:**
  - "Trực quan. $u_t$ ảnh hưởng chi phí bước $t$ trực tiếp, và mọi bước sau qua các vị trí sau." (17)
  - "Mệnh đề 11.30. Giả thiết: $\hat f$, $c$ khả vi liên tục; $x_{t+1}=\hat f(x_t,u_t)$. Kết luận: với truy hồi ngược (backward recursion)" (13), công thức hiển thị (4.2) $\lambda_h=\partial_{x_h}c(x_h,u_{h-1})$, $\lambda_t=\partial_{x_t}c(x_t,u_{t-1})+\lambda_{t+1}\partial_{x_t}\hat f(x_t,u_t)$; công thức hiển thị (4.3) $\partial J/\partial u_t=\partial_{u_t}c(x_{t+1},u_t)+\lambda_{t+1}\partial_{u_t}\hat f(x_t,u_t)$.
  - "Ví dụ 11.18, truy hồi ngược: $\lambda_2=2x_2=4$, $\lambda_1=2x_1+\lambda_2=8$; $\partial J/\partial u_1=4$, $\partial J/\partial u_0=8$, trùng khai triển." (6)
- **Mật độ:** khoảng 36 âm tiết (trước 53), 5 dòng, 2 công thức hiển thị; (4.2) dùng `aligned` hai dòng. Dòng "Chứng minh." (quy nạp ngược: $\lambda_t$ là đạo hàm của chi phí còn lại theo $x_t$) ở ghi chú diễn giả (NT6, kết quả phụ). **Số đo cuối** (`deck_lint`, sau III.5): 59 âm tiết, trần 60, tỉ lệ 0,98.
- **Sau biên tập (2026-11-19):** $\lambda_t$ gọi tên "đạo hàm theo $x_t$ của chi phí còn lại tính từ $x_t$"; miền $1\le t\le h-1$, $0\le t\le h-1$ trong công thức; "theo (4.2); gradient theo (4.3):" (D-3).
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — kết quả phụ, chứng minh ở ghi chú diễn giả (NT6).
- **Ghi chú diễn giả:** "Chứng minh." quy nạp ngược bằng quy tắc dây chuyền; mệnh đề là lan truyền ngược (backpropagation) viết cho một chuỗi thời gian; với vector, $\partial\hat f/\partial x_t$ là ma trận Jacobi; một lượt xuôi lưu $x_1,\dots,x_h$, một lượt ngược tốn $O(h)$; Phạm vi: gradient tính trên mô hình, $J$ có thể không lồi khi $\hat f$ phi tuyến; không dùng được với mô hình bảng hay trình mô phỏng hộp đen.

#### `L11-4-04` Thuật toán tối ưu kế hoạch bằng hạ gradient
- **Vị trí, bước:** mạch 4; thuật toán (Thuật toán 11.31) → ứng dụng (nghiệm tối ưu, Ví dụ 11.19); phương án không đạo hàm một dòng (Thuật toán 11.34, `bổ sung`, Q15).
- **Lý do tồn tại:** NT-RL-2 (đầu vào, đầu ra, tham số, thứ tự, dừng); nghiệm $J^*=2{,}40$ đo một bước của `L11-4-02`.
- **Liên kết:** trước `L11-4-03`; sau `L11-4-05` (kế hoạch tính một lần thì không phản ứng).
- **Mục tiêu:** 5.
- **Nguồn:** Thuật toán 11.31; Ví dụ 11.19; Thuật toán 11.34, Nhận xét 11.35; `lec-11-topic-16`, `lec-11-topic-18`.
- **Mặt trang:**
  - "Thuật toán 11.31. Đầu vào: $x_0$, $\hat f$ và $c$ khả vi, $h$; tham số $\eta$, ngưỡng $\theta$, ngân sách. Đầu ra: kế hoạch $u_{0:h-1}$." (13)
  - "Lặp: lượt xuôi tính $x_1,\dots,x_h$ và $J$; lượt ngược tính $\nabla J$ theo (4.2), (4.3); $u\leftarrow u-\eta\nabla J$; dừng khi $\lVert\nabla J\rVert\le\theta$ hoặc hết ngân sách." (19)
  - "Ví dụ 11.19. Gradient bằng $0$ tại $(-1{,}2;\,-0{,}4)$; $J$ bậc hai với Hessian xác định dương, nên đó là cực tiểu toàn cục:" (21), bảng khuôn T3 một hàng: $(-1{,}2;\,-0{,}4)$ | $0{,}8$; $0{,}4$ | $2{,}40$.
  - "Cách khác: phương pháp entropy chéo (cross-entropy method) chỉ dùng lượt xuôi, không cần đạo hàm." (14)
- **Mật độ:** khoảng 67 âm tiết (trước 83), 5 dòng; trang thuật toán, trần 80 của cổng: đạt. Số hiệu Thuật toán 11.34 và cách rút mẫu ưu tú ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 75 âm tiết, trần 80, tỉ lệ 0,94.
- **Sau biên tập (2026-11-19):** "ma trận Hessian"; tên "phương pháp entropy chéo (cross-entropy method, CEM)".
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — bỏ trang entropy chéo (mã L11-4-06 của `ke-hoach-trang-chieu.md`), thay bằng một dòng "Cách khác:" (Q15).
- **Ghi chú diễn giả:** hệ $4+3u_0+u_1=0$, $2+u_0+2u_1=0$ cho $u_1=-0{,}4$, $u_0=-1{,}2$; Hessian $\begin{pmatrix}6&2\\2&4\end{pmatrix}$, định thức $20$; một bước $\eta=0{,}1$ còn cách tối ưu $0{,}48$; Ví dụ 11.21 của ghi chú (bốn ứng viên $J=8;\ 3;\ 2{,}5;\ 4$, trung bình ưu tú $(-1;\,-0{,}25)$, độ lệch chuẩn $0$ ở $u_0$ làm phân phối suy biến) là nội dung `bổ sung`; entropy chéo dùng được với trình mô phỏng hộp đen, như PETS (Chua và cộng sự, 2018, §5).

#### `L11-4-05` Điều khiển dự báo theo chân trời lùi
- **Vị trí, bước:** mạch 4; vấn đề (giới hạn của kế hoạch vòng hở, NT-RL-3) → trực quan → ví dụ (Ví dụ 11.20) → định nghĩa (Định nghĩa 11.32) → thuật toán gọn (Thuật toán 11.33). Thứ tự ví dụ trước định nghĩa theo ghi chú. NT-RL-4: lập kế hoạch tại thời điểm quyết định cho hành động liên tục.
- **Lý do tồn tại:** chuyển kế hoạch vòng hở thành chính sách vòng kín; luật $u=-0{,}6x$ dùng ở `L11-4-07`.
- **Liên kết:** trước `L11-4-04`; sau `L11-4-06` (mô hình sai thì dự báo lệch bao nhiêu).
- **Mục tiêu:** 5.
- **Nguồn:** §4.3; Ví dụ 11.20; Định nghĩa 11.32; Thuật toán 11.33; `lec-11-topic-17`.
- **Mặt trang:**
  - "Kế hoạch vòng hở $(-1{,}2;\,-0{,}4)$ không phản ứng khi xe trôi khác dự báo." (11)
  - "Trực quan. Chỉ thực hiện hành động đầu, rồi lập kế hoạch lại từ vị trí thật." (15)
  - "Ví dụ 11.20. Giải (4.1) từ $x_0$ bất kỳ cho $u_0^*=-0{,}6x_0$; luật $u_t=-0{,}6x_t$ trên mô hình cho" (14), bảng khuôn T4 một hàng: điều khiển dự báo, mô hình đúng | $2$ | $0{,}8$ | $0{,}32$ | $0{,}128$.
  - "Định nghĩa 11.32, Thuật toán 11.33. Điều khiển dự báo (model predictive control, MPC): mỗi bước thật, quan sát $x_t$, giải (4.1) từ $x_t$, thực hiện $u^*_0(x_t)$, bỏ phần còn lại." (26)
  - "Đây là lập kế hoạch tại thời điểm quyết định cho hành động liên tục." (14)
- **Mật độ:** khoảng 80 âm tiết (trước 88), 6 dòng; trang có thuật toán (Thuật toán 11.33), trần 80 của cổng: đạt. Tên "điều khiển theo chân trời lùi (receding horizon control)" ở tiêu đề và ghi chú diễn giả; "bằng Thuật toán 11.31" ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 78 âm tiết, trần 80, tỉ lệ 0,97.
- **Sau biên tập (2026-11-19):** nhãn "Định nghĩa 11.32, Thuật toán 11.33." trên mặt trang (trang thuật toán, trần 80); tên "receding horizon control", "vòng kín (closed-loop)"; ghi chú diễn giả bỏ câu VP19.
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — gộp ví dụ, định nghĩa, thuật toán (mã L11-4-05 của `ke-hoach-trang-chieu.md`).
- **Ghi chú diễn giả:** hai đạo hàm bằng $0$: $2x_0+3u_0+u_1=0$, $x_0+u_0+2u_1=0$, nghiệm tỉ lệ với $x_0$: $u_1=-0{,}2x_0$, $u_0=-0{,}6x_0$; vòng kín $x_{t+1}=0{,}4x_t$, co hệ số $0{,}4$; kiểm: giải lại từ $x_1=0{,}8$ cho $-0{,}48$; điều khiển dự báo cùng vai với rollout và tìm kiếm theo cây (Bertsekas, 2019, §2.5.1); bài không có bảo đảm ổn định tổng quát (Bertsekas, 2020, §3.1 cần ràng buộc cuối), nên hệ số co được kiểm trực tiếp.

#### `L11-4-06` Sai số mô hình tích lũy
- **Vị trí, bước:** mạch 4; vấn đề (hệ thật nghiêng) → trực quan → ví dụ (Ví dụ 11.22) → phát biểu (Mệnh đề 11.36).
- **Lý do tồn tại:** câu trả lời 3 ("sai số tích lũy"); vế thứ hai của câu hỏi trung tâm cho hành động liên tục.
- **Liên kết:** trước `L11-4-05`; sau `L11-4-07` (vòng hở và vòng kín trên hệ thật).
- **Mục tiêu:** 5.
- **Nguồn:** §4.5; Ví dụ 11.22; Mệnh đề 11.36 và chứng minh; đoạn sau chứng minh; `lec-11-topic-19`.
- **Mặt trang:** hai cột `.grid2`; cột trái:
  - "Ví dụ 11.22: hệ thật $f(x,u)=1{,}2x+u$, mô hình $x+u$, $x_0=2$, $u\equiv0$; sai số dự báo $e_k=2(1{,}2^k-1)$: $0{,}4$; $0{,}88$; $1{,}456$; $2{,}1472$; $2{,}9766$." (13)
  - "Trực quan. Mỗi bước dự báo cộng sai số một bước, còn hệ thật khuếch đại sai số đã có." (18)
  - "Mệnh đề 11.36. Giả thiết: $f$ Lipschitz theo $x$, hằng số $L$; cùng $x_0$, cùng chuỗi hành động cố định; sai số một bước trên quỹ đạo dự báo $\le\bar e$. Kết luận, $L\ne1$:" (25), công thức hiển thị (4.4) $e_k\le\bar e\,(L^k-1)/(L-1)$.
  Cột phải: `sai-so-tich-luy-slide.svg`.
- **Mật độ:** khoảng 56 âm tiết (trước 88), 4 dòng, 1 công thức hiển thị; trang hai cột (`.grid2`), đích ≤ 60 của cổng: đạt. Dòng "Ở ví dụ, $\bar e=0{,}4$, $L=1{,}2$: chặn đạt dấu bằng" và "Chứng minh." ($e_{j+1}\le Le_j+\bar e$, quy nạp) ở ghi chú diễn giả (NT6, kết quả phụ). **Số đo cuối** (`deck_lint`, sau III.5): 65 âm tiết, trần 60, tỉ lệ 1,08.
- **Sau biên tập (2026-11-19):** "Trực quan." có tên "sai số tích lũy (compounding error)"; dãy năm giá trị $e_k$ là dòng riêng; trang Goodfellow và cộng sự ở ghi chú diễn giả.
- **Hình, phút:** `sai-so-tich-luy-slide.svg`; 2,5.
- **Quyết định:** thêm — kết quả phụ (NT6), chứng minh ở ghi chú diễn giả.
- **Ghi chú diễn giả:** "Chứng minh." bất đẳng thức tam giác và tính Lipschitz cho $e_{j+1}\le Le_j+\bar e$, rồi quy nạp; ở ví dụ, $\bar e=0{,}4$, $L=1{,}2$ cho $2(1{,}2^k-1)$, đạt dấu bằng; trường hợp $L=1$: $k\bar e$; Phạm vi: chỉ cho vòng hở; trên quỹ đạo thật, sai số một bước $0{,}2x$ tại $x_5=4{,}9766$ bằng $0{,}9953>\bar e$; gradient qua $h$ lần nhân $\partial\hat f/\partial x$ có thể bùng nổ hoặc tiêu biến (Goodfellow, Bengio và Courville, 2016); PETS và PILCO đưa bất định của mô hình vào dự báo (Nhận xét 11.37, đọc thêm).

#### `L11-4-07` Ví dụ: vòng hở và điều khiển dự báo với mô hình sai
- **Vị trí, bước:** mạch 4; ứng dụng (Ví dụ 11.23): so hai công cụ trên cùng số (NT23).
- **Lý do tồn tại:** câu trả lời 3 dùng hệ số $0{,}6$; cho thấy vòng kín chịu được một mức sai số mô hình.
- **Liên kết:** trước `L11-4-06`; sau `L11-4-08`.
- **Mục tiêu:** 5, 7.
- **Nguồn:** Ví dụ 11.23; `lec-11-topic-19`.
- **Mặt trang:** toàn bề rộng, không hình (hình xe trên đường ray lặp đúng số của bảng nên chỉ ở ghi chú):
  - "Ví dụ 11.23: hệ thật $1{,}2x+u$, mô hình $x+u$, $x_0=2$; kế hoạch tối ưu trên mô hình $(-1{,}2;\,-0{,}4)$; luật dự báo $u=-0{,}6x$." (14)
  - Bảng khuôn T4, bốn hàng: kế hoạch trên mô hình | $2$ | $0{,}8$ | $0{,}4$ | —; vòng hở, hệ thật | $2$ | $1{,}2$ | $1{,}04$ | —; dự báo, mô hình đúng | $2$ | $0{,}8$ | $0{,}32$ | $0{,}128$; dự báo, hệ thật | $2$ | $1{,}2$ | $0{,}72$ | $0{,}432$ (nhãn hàng 15 âm tiết).
  - "Diễn giải: vòng hở để xe ở $1{,}04$ thay vì $0{,}4$; vòng kín co về $0$ với hệ số $0{,}6$ dù mô hình sai, vì mỗi bước giải lại từ vị trí thật." (31)
- **Mật độ:** khoảng 60 âm tiết (cả nhãn hàng bảng), 6 dòng, 0 công thức hiển thị; bảng toàn bề rộng (cổng). **Số đo cuối** (`deck_lint`, sau III.5): 58 âm tiết, trần 60, tỉ lệ 0,97.
- **Hình, phút:** — (`xe-tren-duong-ray.svg` chỉ ở ghi chú); 1,5.
- **Quyết định:** thêm — ví dụ ứng dụng của ghi chú.
- **Ghi chú diễn giả:** $x_1=1{,}2\cdot2-1{,}2=1{,}2$, $x_2=1{,}2\cdot1{,}2-0{,}4=1{,}04$; vòng kín trên hệ thật $x_{t+1}=(1{,}2-0{,}6)x_t$; Tình huống 11.1: học mô hình bằng bình phương tối thiểu từ ba mẫu cho đúng $\hat a_1=1{,}2$, luật $u=-0{,}7588x$, vòng kín $0{,}4412$; Bài tập 11.11 (tự làm): vòng kín co khi và chỉ khi $-0{,}4<a<1{,}6$.

#### `L11-4-08` Bài tập: kế hoạch hai bước từ $x_0=1$
- **Vị trí, bước:** mạch 4; kiểm tra (đề và lời giải fragment) của cụm gradient qua mô hình.
- **Lý do tồn tại:** NT24; cùng khuôn T3 với `L11-4-02`, `L11-4-04`.
- **Liên kết:** trước `L11-4-07`; sau `L11-5-00`.
- **Mục tiêu:** 5.
- **Nguồn:** Bài tập 11.6 và lời giải; `lec-11-topic-27`.
- **Mặt trang:**
  - "Câu hỏi (Bài tập 11.6): mô hình $\hat f(x,u)=x+u$, chi phí $x_{t+1}^2+u_t^2$, $h=2$, $x_0=1$. (a) Tính gradient tại $(0;\,0)$ bằng khai triển và bằng truy hồi ngược. (b) Thực hiện một bước $\eta=0{,}1$. (c) Tìm kế hoạch tối ưu và $J^*$." (31; hai dòng hiển thị)
  - fragment "Lời giải: (a) khai triển cho $\partial J/\partial u_0=2+0+2=4$, $\partial J/\partial u_1=2$; truy hồi ngược $\lambda_2=2$, $\lambda_1=4$ cho cùng $(4;\,2)$." (14)
  - fragment bảng khuôn T3, hai hàng: (b) $(-0{,}4;\,-0{,}2)$ | $0{,}6$; $0{,}4$ | $0{,}72$; (c) $(-0{,}6;\,-0{,}2)$ | $0{,}4$; $0{,}2$ | $0{,}6$.
  - fragment "$J$ bậc hai thuần nhất theo $(x_0,u)$, nên $x_0$ giảm một nửa thì $J^*$ chia $4$: $2{,}40/4=0{,}6$." (17)
- **Mật độ:** khoảng 62 âm tiết, 5 dòng: ngoại lệ nhẹ (mục 4). **Số đo cuối** (`deck_lint`, sau III.5): 59 âm tiết, trần 60, tỉ lệ 0,98.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — gộp đề và lời giải (mã L11-4-09, L11-4-10 của `ke-hoach-trang-chieu.md`).
- **Ghi chú diễn giả (NT-RL-10):** năng lực kiểm: hai cách tính gradient cho cùng kết quả, một bước hạ gradient, điểm dừng. "Gợi ý: so với Ví dụ 11.18, 11.19." Hệ điểm dừng $2+3u_0+u_1=0$, $1+u_0+2u_1=0$. Kết quả của mạch: gradient qua mô hình và điều khiển dự báo xử lý hành động liên tục; cái giá là sai số tích lũy (4.4) và số hành động cần tối ưu tăng theo $h$.

### Mạch 5. Học tăng cường phân cấp (10 trang, 22 phút)

| Cụm | Vấn đề | Trực quan | Ví dụ | Hình thức | Ý tưởng chứng minh | Ứng dụng | Kiểm tra |
|---|---|---|---|---|---|---|---|
| Tùy chọn, chính sách phân cấp | `L11-5-01` (giới hạn từng bước gốc; $V_6(\mathrm A)=0{,}6103$) | `L11-5-01` | `L11-5-01` (Ví dụ 11.24) | `L11-5-02` (Định nghĩa 11.38, 11.39) | không áp dụng | `L11-5-02` (hành động một bước là tùy chọn) | Bài tập 11.3 (tự làm) |
| Mô hình tùy chọn | `L11-5-03` (cần phần thưởng và nơi kết thúc của cả tùy chọn) | `L11-5-03` | `L11-5-03` (Ví dụ 11.25, tính tay) | `L11-5-04` (Định nghĩa 11.40, Mệnh đề 11.41) | "Chứng minh." một dòng | `L11-5-07` | `L11-5-09` (Bài tập 11.7, lời giải trên mặt trang) |
| Phương trình Bellman phân cấp (Định lý 11.42, kết quả chính) | `L11-5-05` (dòng "Nhắc lại:" Định lý 03.21) | `L11-5-05` | `L11-5-03` (kiểm $\rho^3\cdot0{,}9756=v_*(\mathrm A)$) | `L11-5-05` | `L11-5-06` | `L11-5-07` | `L11-5-06` (bỏ giả thiết) |
| Lặp giá trị với tùy chọn (Định lý 11.44) | `L11-5-07` (thay trung bình bằng cực đại) | ghi chú diễn giả | `L11-5-07` (Ví dụ 11.26, tính tay trước thuật toán) | `L11-5-07` (Định lý 11.44, Thuật toán 11.45) | "Chứng minh." ở ghi chú diễn giả | `L11-5-07` (hai vòng so với sáu lượt quét) | `L11-6-06` câu 4 |
| Q-learning bán-MDP | `L11-5-08` (không có mô hình tùy chọn) | `L11-5-08` (Nhận xét 11.43) | `L11-5-08` (Ví dụ 11.27, tính tay trước thuật toán) | `L11-5-08` (Thuật toán 11.46) | không áp dụng (không có định lý trong ghi chú) | `L11-6-05` câu (e) | Bài tập 11.10(e) |

Cái truyền từ ví dụ sang công thức: $\rho=0{,}72/0{,}82$ và các hệ số $p$, $r$ (`L11-5-03`) thành (5.1); kiểm $\rho^3\cdot0{,}9756=v_*(\mathrm A)$ thành (5.2); hai vòng với tùy chọn thành $T_\Omega$; mục tiêu $\gamma^3\cdot0{,}9$ thành (5.3). §5.4 (đọc thêm: học mô hình tùy chọn, Nhận xét 11.47) chỉ ở ghi chú diễn giả của `L11-5-08` (NT5).

#### `L11-5-00` 5. Học tăng cường phân cấp (trang tiêu đề mạch), điểm vào mạch 5
- **Vị trí, bước:** điểm vào mạch 5; `section.strand-title`, `id="mach-5"`, `data-note-topic-id="lec-11-topic-20"`. Dòng dẫn nêu đúng nhu cầu của khái niệm đầu (tùy chọn): bước `vấn đề` chung.
- **Lý do tồn tại:** NT12.
- **Liên kết:** trước `L11-4-08`; sau `L11-5-01`.
- **Mục tiêu:** 6.
- **Mặt trang:** "5." + "Học tăng cường phân cấp"; `p.strand-lead` "Gộp nhiều bước thành một quyết định vẫn giữ được phương trình Bellman và tính co." (18); `p.strand-keys` "tùy chọn · mô hình tùy chọn · bán-MDP · lặp giá trị với tùy chọn".
- **Mật độ:** **Số đo cuối** (`deck_lint`, sau III.5): 16 âm tiết, trần 25, tỉ lệ 0,64.
- **Sau biên tập (2026-11-19):** dòng dẫn "Gộp nhiều bước thành một quyết định vẫn giữ được phương trình Bellman và tính co." (18), không chữ "tùy chọn".
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT12.
- **Ghi chú diễn giả (40–100):** kế thừa: lặp giá trị và phương trình Bellman (Bài 03–04), giới hạn của mọi phương pháp trước (quyết định theo từng bước gốc); việc của mạch: định nghĩa tùy chọn, tính mô hình của nó, chứng minh phương trình Bellman phân cấp, lặp giá trị và Q-learning trên tùy chọn; trao đi: bảo đảm $v_\Omega\le v_*$, dấu bằng khi $\Omega(s)\supseteq\mathcal A(s)$.

#### `L11-5-01` Ví dụ: hai tùy chọn trên mê cung hai phòng
- **Vị trí, bước:** mạch 5, trang nội dung đầu; vấn đề (giới hạn của mạch 2–4, NT-RL-3; câu khẳng định của mạch, NT13) → trực quan → ví dụ (Ví dụ 11.24).
- **Lý do tồn tại:** số đo của giới hạn ($V_6(\mathrm A)=0{,}6103$ sau sáu lượt quét) và hai tùy chọn cụ thể trước định nghĩa.
- **Liên kết:** trước `L11-5-00`; sau `L11-5-02`.
- **Mục tiêu:** 6.
- **Nguồn:** kết mục §4; §5.1; Ví dụ 11.24; bảng lượt quét của Ví dụ 11.26; `lec-11-topic-20`.
- **Mặt trang:**
  - "Mọi phương pháp tới đây quyết định theo từng bước gốc." (11)
  - "Lặp giá trị đồng bộ một bước (Thuật toán 04.28) từ $V_0\equiv0$: $V_3(\mathrm A)=0$, $V_6(\mathrm A)=0{,}6103<v_*(\mathrm A)=0{,}6604$." (12)
  - "Trực quan. Người đi trong tòa nhà nghĩ theo "ra cửa phòng", không theo từng bước chân." (17)
  - "Ví dụ 11.24. Tùy chọn $\omega_1$ "đi tới cửa": $\mathrm A,\mathrm E,\mathrm F\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$, dừng khi tới $\mathrm K$; $\omega_2$ "đi tới đích": $\mathrm C,\mathrm K\mapsto\rightarrow$, $\mathrm D\mapsto\downarrow$, dừng khi vào $\mathrm Z$." (17)
- **Mật độ:** khoảng 56 âm tiết (trước 63), 4 dòng (dòng ví dụ hai dòng hiển thị), 0 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 62 âm tiết, trần 60, tỉ lệ 1,03.
- **Sau biên tập (2026-11-19):** câu giới hạn của mạch 4 có số (nối 4→5, NT13).
- **Hình, phút:** — (hình tùy chọn đặt ở `L11-5-03`, nơi các số trên hình được tính); 2,5.
- **Quyết định:** thêm — mở mạch bằng giới hạn có số và ví dụ (NT14, NT-RL-3).
- **Ghi chú diễn giả:** kết mục §4: lặp giá trị đẩy giá trị lùi một bước sau mỗi lượt quét, Q-planning sau mỗi cập nhật, kế hoạch nhìn xa $h$ bước phải tối ưu $h$ hành động; cùng một MDP có nhiều thang thời gian (Sutton và Barto, 2018, §17.2, tr. 461); học tăng cường phân cấp (hierarchical reinforcement learning), trừu tượng thời gian (temporal abstraction); mỗi chính sách con đi đường ngắn nhất trong phòng của nó, trượt chỉ làm ở yên nên tùy chọn tới đích với xác suất $1$.

#### `L11-5-02` Tùy chọn và chính sách phân cấp
- **Vị trí, bước:** mạch 5; hình thức (Định nghĩa 11.38, 11.39) → ứng dụng (hành động một bước là tùy chọn).
- **Lý do tồn tại:** đặt $\omega$, $\beta_\omega$, $\tau$, $\mu$, $v_\mu$ dùng trong mọi trang sau của mạch.
- **Liên kết:** trước `L11-5-01`; sau `L11-5-03`.
- **Mục tiêu:** 6.
- **Nguồn:** Định nghĩa 11.38, 11.39; đoạn sau mỗi định nghĩa; `lec-11-topic-20`.
- **Mặt trang:**
  - "Định nghĩa 11.38. Tùy chọn (option) $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$ gồm:" (5) rồi ba gạch đầu dòng: "tập khởi đầu (initiation set) $\mathcal I_\omega\subseteq\mathcal S$;" (5); "chính sách $\pi_\omega(a\mid s)$ Markov dừng;" (4); "hàm kết thúc (termination function) $\beta_\omega:\mathcal S^+\to[0,1]$, xác suất dừng tại trạng thái vừa tới; $\tau\ge1$ là bước dừng đầu tiên." (20)
  - "Hành động một bước $a$ là tùy chọn với $\pi(s)=a$, $\beta\equiv1$." (10)
  - "Định nghĩa 11.39. Chính sách phân cấp (hierarchical policy) $\mu(\omega\mid s)$ chọn một tùy chọn tại $s$ và chạy nó tới khi kết thúc; $v_\mu(s)$ là lợi tức kỳ vọng tính trên các bước gốc." (31)
- **Mật độ:** khoảng 75 âm tiết, 6 dòng: ngoại lệ (mục 4; hai định nghĩa liền nhau của ghi chú, mỗi thành phần một dòng theo VP11). **Số đo cuối** (`deck_lint`, sau III.5): 76 âm tiết, trần 60, tỉ lệ 1,27.
- **Sau biên tập (2026-11-19):** tên tiếng Anh "termination condition" cùng "termination function".
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT8 bước hình thức sau ví dụ.
- **Ghi chú diễn giả:** giả thiết $\{s:\beta_\omega(s)<1\}\subseteq\mathcal I_\omega$; $\beta_\omega=1$ tại trạng thái kết thúc; Sutton và Barto (2018, tr. 462) viết tùy chọn là $\langle\pi_\omega,\gamma_\omega\rangle$ với $\beta_\omega=1-\gamma_\omega$, chính sách phân cấp là $\pi$; tùy chọn có thể không kết thúc ($\pi_{\omega_1}(\mathrm A)=\leftarrow$ với $\beta=0$), nên mô hình tùy chọn chỉ định nghĩa cho tùy chọn kết thúc với xác suất $1$; chính sách mà $\mu$ sinh trên MDP gốc nói chung không Markov theo trạng thái.

#### `L11-5-03` Ví dụ: mô hình của hai tùy chọn
- **Vị trí, bước:** mạch 5; trực quan → ví dụ tính tay (Ví dụ 11.25) của cụm mô hình tùy chọn, trước định nghĩa (thứ tự của ghi chú).
- **Lý do tồn tại:** cho các hệ số $p$, $r$ dùng ở `L11-5-07` và trên hình; mục tiêu 6 ("tính mô hình của một tùy chọn").
- **Liên kết:** trước `L11-5-02`; sau `L11-5-04` (công thức chung).
- **Mục tiêu:** 6.
- **Nguồn:** §5.2; Ví dụ 11.25; hình hai tùy chọn; `lec-11-topic-21`.
- **Mặt trang:**
  - hai cột `.grid2`; cột trái:
  - "Trực quan. Mô hình của tùy chọn cho phần thưởng chiết khấu khi chạy hết tùy chọn và nơi kết thúc; chiết khấu theo số bước gộp vào hệ số chuyển." (31)
  - "Tính thừa số của một bước đi đúng, cần $j$ lần thử với xác suất $0{,}2^{j-1}\cdot0{,}8$:" (14)
  - công thức hiển thị $\rho=\sum_{j\ge1}\gamma^j\,0{,}2^{j-1}\,0{,}8=0{,}72/0{,}82=0{,}8780$.
  - "$\omega_1$: $r=0$; $p(\mathrm K\mid\mathrm F,\omega_1)=0{,}8780$, $p(\mathrm K\mid\mathrm B,\omega_1)=p(\mathrm K\mid\mathrm E,\omega_1)=\rho^2=0{,}7710$, $p(\mathrm K\mid\mathrm A,\omega_1)=\rho^3=0{,}6769$." (1)
  - "$\omega_2$: $r(\mathrm K,\omega_2)=r(\mathrm D,\omega_2)=0{,}8/0{,}82=0{,}9756$, $r(\mathrm C,\omega_2)=0{,}8566$." (1)
  - "Diễn giải: $\rho^3\cdot0{,}9756=0{,}6604=v_*(\mathrm A)$, nên chạy $\omega_1$ rồi $\omega_2$ từ $\mathrm A$ là đi theo đường ngắn nhất." (12)
  - Cột phải: `tuy-chon-hai-phong-slide.svg`.
- **Mật độ:** 59 âm tiết (trước 56), 6 dòng, 1 công thức hiển thị; trang hai cột, đích ≤ 60: đạt. **Số đo cuối** (`deck_lint`, sau III.5): 47 âm tiết, trần 60, tỉ lệ 0,78.
- **Sau biên tập (2026-11-19):** ghi chú diễn giả: $r=\rho/\gamma$ tại $\mathrm K$, $\mathrm D$; $\rho^2/\gamma$ tại $\mathrm C$.
- **Hình, phút:** `tuy-chon-hai-phong-slide.svg`; 2,5.
- **Quyết định:** thêm — ví dụ tính tay (NT-RL-2 cho lặp giá trị với tùy chọn: hệ số mô hình là đầu vào); số bốn chữ số theo ghi chú (kế hoạch ghi ba chữ số).
- **Ghi chú diễn giả:** các bước đi đúng liên tiếp độc lập nên $d$ bước cho $\rho^d$; $\omega_1$ luôn kết thúc ở $\mathrm K$; $\omega_2$ chỉ kết thúc ở $\mathrm Z$ có giá trị $0$, phần thưởng $+1$ đến ở bước $\tau$ nên $r=\mathbb E[\gamma^{\tau-1}]$; đọc hình: mũi tên là $\pi_\omega$, số cạnh ô là $p$ của việc tới $\mathrm K$ (phòng trái) và $r$ (phòng phải).

#### `L11-5-04` Mô hình tùy chọn
- **Vị trí, bước:** mạch 5; hình thức (Định nghĩa 11.40) → kết quả (Mệnh đề 11.41).
- **Lý do tồn tại:** công thức chung của Ví dụ 11.25; tổng hệ số $\le\gamma$ là bước then chốt của tính co ở `L11-5-07`.
- **Liên kết:** trước `L11-5-03`; sau `L11-5-05`.
- **Mục tiêu:** 6.
- **Nguồn:** Định nghĩa 11.40; đoạn sau định nghĩa; Mệnh đề 11.41 và chứng minh; `lec-11-topic-21`.
- **Mặt trang:**
  - "Định nghĩa 11.40. Với tùy chọn $\omega$ kết thúc với xác suất $1$ và $s\in\mathcal I_\omega$, mô hình tùy chọn (option model) gồm" (17), công thức hiển thị (5.1) $r(s,\omega)=\mathbb E[R_1+\dots+\gamma^{\tau-1}R_\tau\mid S_0=s,\omega]$, $p(s'\mid s,\omega)=\sum_{k\ge1}\gamma^k\Pr\{S_k=s',\tau=k\mid S_0=s,\omega\}$ (`aligned`, hai dòng).
  - "Phần $p$ đã chứa chiết khấu: $p(\mathrm K\mid\mathrm F,\omega_1)=0{,}8780$, trong khi xác suất tới $\mathrm K$ bằng $1$." (15)
  - "Mệnh đề 11.41. Với $0\le\gamma<1$, kết luận:" (7), công thức hiển thị $\sum_{s'\in\mathcal S^+}p(s'\mid s,\omega)=\mathbb E[\gamma^\tau\mid S_0=s,\omega]\le\gamma$.
  - "Chứng minh. Đổi thứ tự tổng theo $s'$ và $k$, rồi dùng $\tau\ge1$." (12)
- **Mật độ:** khoảng 51 âm tiết, 6 dòng, 2 công thức hiển thị. **Số đo cuối** (`deck_lint`, sau III.5): 56 âm tiết, trần 60, tỉ lệ 0,93.
- **Sau biên tập (2026-11-19):** nhãn "Giả thiết:", "Kết luận:"; câu dẫn "gồm hai đại lượng (5.1):" (D-3); ghi chú diễn giả "$0<\gamma<1$" cho dấu bằng.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — kết quả phụ có dòng "Chứng minh." (NT6).
- **Ghi chú diễn giả:** (5.1) là (17.2)–(17.3) của Sutton và Barto (2018, tr. 462) và (6)–(7) của Sutton, Precup và Singh (1999, tr. 189); với hành động một bước, $p$ là xác suất chuyển nhân $\gamma$; ở Ví dụ 11.25, tổng tại $\mathrm A$ là $0{,}6769\le0{,}9$; dấu bằng khi và chỉ khi $\tau=1$ hầu chắc chắn; tùy chọn có thể không kết thúc vẫn cho tổng $\le\gamma\Pr\{\tau<\infty\}$.

#### `L11-5-05` Phương trình Bellman cho chính sách phân cấp
- **Vị trí, bước:** mạch 5; vấn đề (dòng "Nhắc lại:" phương trình Bellman của hành động một bước) → trực quan → phát biểu kết quả chính thứ hai (Định lý 11.42).
- **Lý do tồn tại:** nền của lặp giá trị và Q-learning trên tùy chọn; câu trả lời 4.
- **Liên kết:** trước `L11-5-04` (mô hình (5.1)); sau `L11-5-06` (vì sao đúng).
- **Mục tiêu:** 6.
- **Nguồn:** Định lý 11.42; đoạn sau chứng minh; `lec-11-topic-21`.
- **Mặt trang:**
  - "Nhắc lại: $v_\pi(s)=\sum_a\pi(a\mid s)\bigl[r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)\,v_\pi(s')\bigr]$ (Định lý 03.21)." (4)
  - "Trực quan. Chạy hết một tùy chọn rồi đứng ở trạng thái mới, như sau một hành động một bước." (20)
  - "Định lý 11.42. Giả thiết: MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; mỗi tùy chọn có $\pi_\omega$ Markov dừng, $\beta_\omega$ chỉ phụ thuộc trạng thái, kết thúc với xác suất $1$; $\mu$ chỉ phụ thuộc trạng thái tại mỗi thời điểm chọn." (37; hai dòng hiển thị)
  - "Kết luận ($v_\mu=0$ ở trạng thái kết thúc):" (8), công thức hiển thị (5.2) $v_\mu(s)=\sum_{\omega\in\Omega(s)}\mu(\omega\mid s)\bigl[r(s,\omega)+\sum_{s'\in\mathcal S^+}p(s'\mid s,\omega)\,v_\mu(s')\bigr]$ (`aligned` nếu tràn).
- **Mật độ:** khoảng 69 âm tiết (trước 69), 5 dòng, 1 công thức hiển thị: ngoại lệ NT17, lý do: kết quả chính giữ đủ năm giả thiết (NT2) cùng bước trực quan bắt buộc (NT8, cổng); dòng "Ý nghĩa:" chuyển vào ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 72 âm tiết, trần 60, tỉ lệ 1,20.
- **Sau biên tập (2026-11-19):** nhãn "Kết luận:" và câu dẫn mang số (5.2).
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — kết quả chính (Q16).
- **Ghi chú diễn giả:** "Ý nghĩa": chiết khấu nằm trong $p$, với hành động một bước (5.2) trở về Định lý 03.21; số hạng trong ngoặc là $q_\mu(s,\omega)$; tùy chọn dài ngắn khác nhau được so trên cùng thang thời gian gốc; điều kiện áp dụng: mỗi tùy chọn chạy tới khi kết thúc, không bị ngắt; Phạm vi: Sutton, Precup và Singh (1999, (8), tr. 190 và Định lý 1) phát biểu cả cho tùy chọn bán-Markov, chứng minh của bài dùng $\beta_\omega$ chỉ phụ thuộc trạng thái; ngắt tùy chọn trước $\tau$ hay chính sách cấp trên dùng lịch sử thì vi phạm giả thiết.

#### `L11-5-06` Ý tưởng chứng minh: phương trình Bellman cho chính sách phân cấp
- **Vị trí, bước:** mạch 5; ý tưởng chứng minh (NT6) → kiểm tra (bỏ giả thiết).
- **Lý do tồn tại:** Q16; giả thiết "kết thúc với xác suất $1$" vào ở bước 1, tính Markov vào ở bước 3.
- **Liên kết:** trước `L11-5-05`; sau `L11-5-07` (thay trung bình bằng cực đại).
- **Mục tiêu:** 6.
- **Nguồn:** chứng minh Định lý 11.42; đoạn "Hai giả thiết của định lý có vai trò riêng"; `lec-11-topic-21`.
- **Mặt trang:** bốn bước đánh số và một dòng:
  1. "Tách lợi tức tại $\tau$ (giả thiết: kết thúc với xác suất $1$, nên $\tau<\infty$):" (13), công thức hiển thị $G_0=\sum_{t=0}^{\tau-1}\gamma^tR_{t+1}+\gamma^\tau G_\tau$.
  2. "Kỳ vọng của phần đầu khi biết $S_0=s$ và $\omega$ là $r(s,\omega)$, theo (5.1)." (15)
  3. "Trên $\{\tau=k,S_k=s'\}$, tương lai như quá trình theo $\mu$ từ $s'$ (giả thiết: $\pi_\omega$ Markov, $\beta_\omega$ và $\mu$ chỉ phụ thuộc trạng thái), nên phần sau có kỳ vọng $\sum_{s'}p(s'\mid s,\omega)\,v_\mu(s')$." (23)
  4. "Lấy trung bình theo $\mu(\omega\mid s)$ được (5.2)." (8)
  - "Kỹ thuật. Tách lợi tức tại thời điểm dừng ngẫu nhiên, dùng tính Markov tại đó." (16)
- **Mật độ:** 75 âm tiết (trước 84), 6 dòng, 1 công thức hiển thị; trang ý tưởng chứng minh, trần 80 của cổng: đạt. Không rút các cụm "(giả thiết: …)", vì giả thiết phải ghi ở bước dùng nó (NT6). **Số đo cuối** (`deck_lint`, sau III.5): 67 âm tiết, trần 80, tỉ lệ 0,84.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — NT6, Q16; "Kỹ thuật." một dòng cho mẹo dùng trong một chứng minh (NT7).
- **Ghi chú diễn giả:** bước 3 dùng lập luận của Bổ đề 03.20 tại thời điểm cố định $k$, rồi lấy kỳ vọng theo lịch sử; đổi thứ tự tổng được vì $v_\mu$ bị chặn. Bỏ "kết thúc với xác suất $1$": không có $\tau$ hữu hạn để tách ở bước 1. Bỏ "$\mu$ chỉ phụ thuộc trạng thái": phần sau $\tau$ phụ thuộc lịch sử, bước 3 không cho $v_\mu(S_\tau)$.

#### `L11-5-07` Lặp giá trị với tùy chọn
- **Vị trí, bước:** mạch 5; ví dụ tính tay (Ví dụ 11.26, NT-RL-2) → thuật toán (Thuật toán 11.45) → bảo đảm (Định lý 11.44); so hai công cụ trên cùng số (một bước và tùy chọn, NT23).
- **Lý do tồn tại:** câu trả lời 4 ("hai vòng so với sáu lượt quét"); mục tiêu 6.
- **Liên kết:** trước `L11-5-06`; sau `L11-5-08` (khi không có mô hình tùy chọn).
- **Mục tiêu:** 6, 7.
- **Nguồn:** §5.3; Ví dụ 11.26; Định lý 11.44 và chứng minh; Thuật toán 11.45; `lec-11-topic-22`.
- **Mặt trang:**
  - "Thay trung bình theo $\mu$ trong (5.2) bằng cực đại theo $\omega$:" (12), công thức hiển thị $(T_\Omega V)(s)=\max_{\omega\in\Omega(s)}\bigl[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)V(s')\bigr]$.
  - Bảng khuôn T5, chú thích "Ví dụ 11.26, từ $V_0\equiv0$; $\Omega(s)=\{\omega_1\}$ ở phòng trái, $\{\omega_2\}$ ở phòng phải; vòng 1 cho $0$ ở phòng trái", hai hàng: tùy chọn | $2$ | $0{,}9756$ | $0{,}8566$ | $0{,}7522$ | $0{,}6604$; một bước | $6$ | $0{,}9756$ | $0{,}8558$ | $0{,}7435$ | $0{,}6103$.
  - "Thuật toán 11.45 lặp $V_{k+1}=T_\Omega V_k$ tới khi $\lVert V_{k+1}-V_k\rVert_\infty\le\theta$." (6)
  - "Định lý 11.44. Giả thiết: như Định lý 11.42; $\Omega(s)$ hữu hạn, khác rỗng; mô hình tùy chọn đúng. Bảo đảm: $T_\Omega$ co hệ số $\gamma$, $V_k\to v_\Omega$; $v_\Omega\le v_*$, bằng nhau khi $\Omega(s)\supseteq\mathcal A(s)$." (29)
- **Mật độ:** khoảng 73 âm tiết (cả chú thích bảng; trước 75), 6 dòng, 1 công thức hiển thị; trang có thuật toán (Thuật toán 11.45), trần 80 của cổng: đạt. **Số đo cuối** (`deck_lint`, sau III.5): 57 âm tiết, trần 80, tỉ lệ 0,71.
- **Sau biên tập (2026-11-19):** "bằng nhau khi"; $v_\Omega$ giải thích ở ghi chú diễn giả (trang tràn khung khi đặt trên mặt).
- **Hình, phút:** —; 3.
- **Quyết định:** thêm — gộp ví dụ, thuật toán và định lý (mã L11-5-07 của `ke-hoach-trang-chieu.md`); bảng lượt quét dùng khuôn T5.
- **Ghi chú diễn giả:** "Chứng minh." (a): Bổ đề 04.23 (nhắc lại: $\lvert\max_ax_a-\max_ay_a\rvert\le\max_a\lvert x_a-y_a\rvert$) và Mệnh đề 11.41 ($p\ge0$, tổng $\le\gamma$); (b): Định lý 04.5; (c) dẫn Sutton và Barto (2018, §17.2, tr. 463) và Sutton, Precup và Singh (1999, (10), (13)). Hai vòng đủ vì mỗi vòng đi qua cả một phòng, hệ số co vẫn là $\gamma$; trên mê cung $v_\Omega=v_*$ dù $\Omega(s)$ không chứa hành động một bước; phản ví dụ: phòng trái chỉ có tùy chọn về $\mathrm A$ cho $v_\Omega=0<v_*$; chi phí phải cộng phép tính mô hình tùy chọn.

#### `L11-5-08` Q-learning bán-MDP
- **Vị trí, bước:** mạch 5; vấn đề (không có mô hình tùy chọn, NT-RL-3) → trực quan (bán-MDP, Nhận xét 11.43) → ví dụ tính tay (Ví dụ 11.27, NT-RL-2) → thuật toán (Thuật toán 11.46). NT-RL-4: phiên bản không có mô hình của lặp giá trị với tùy chọn.
- **Lý do tồn tại:** mục tiêu 6 ("một cập nhật Q-learning với tùy chọn"); nhầm lẫn $\gamma$ với $\gamma^k$.
- **Liên kết:** trước `L11-5-07`; sau `L11-5-09`.
- **Mục tiêu:** 6.
- **Nguồn:** Nhận xét 11.43; Ví dụ 11.27; Thuật toán 11.46; đoạn sau thuật toán; `lec-11-topic-21`, `lec-11-topic-22`.
- **Mặt trang:**
  - "Không có mô hình tùy chọn, tác tử học $Q(s,\omega)$ từ các lần chạy thật." (14)
  - "Nhận xét 11.43. Ở các thời điểm chọn, quá trình là một quá trình quyết định bán-Markov (semi-Markov decision process, SMDP), gọi tắt là bán-MDP." (24)
  - Bảng khuôn T1, một hàng, chú thích "Ví dụ 11.27: tại $\mathrm B$ chạy $\omega_1$, tới $\mathrm K$ sau $k=3$ bước, phần thưởng $0$; $\max_{\omega'}Q(\mathrm K,\omega')=0{,}9$, $\alpha=0{,}5$": $(\mathrm B,\omega_1)$ | $\gamma^3\cdot0{,}9=0{,}6561$ | $0{,}6561$ | $0{,}32805$.
  - "Thuật toán 11.46. Chọn $\omega$ $\varepsilon$-tham lam theo $Q(s,\cdot)$, chạy tới khi kết thúc sau $k$ bước ở $S_k$, rồi cập nhật" (19), công thức hiển thị (5.3) $Q(s,\omega)\leftarrow Q(s,\omega)+\alpha\bigl[\sum_{j=1}^k\gamma^{j-1}R_j+\gamma^k\max_{\omega'}Q(S_k,\omega')-Q(s,\omega)\bigr]$ (`aligned`).
  - "Lưu ý: chiết khấu là $\gamma^k$ theo số bước thật; dùng $\gamma$ thay $\gamma^k$ cho mục tiêu $0{,}81$ và giá trị mới $0{,}405$." (19)
- **Mật độ:** khoảng 80 âm tiết (trước 105 khi giữ nguyên năm dòng), 5 dòng, 1 công thức hiển thị; trang thuật toán (Thuật toán 11.46), trần 80 của cổng: đạt. Thứ tự ví dụ trước thuật toán (NT-RL-2); chú thích bảng rút còn "Ví dụ 11.27: $\omega_1$ từ $\mathrm B$ tới $\mathrm K$ sau $k=3$ bước, $\max_{\omega'}Q(\mathrm K,\omega')=0{,}9$"; dòng "Lưu ý:" nêu chỗ sai, không lời phán (`no-ai-slop`, cổng). **Số đo cuối** (`deck_lint`, sau III.5): 80 âm tiết, trần 80, tỉ lệ 1,00.
- **Sau biên tập (2026-11-19):** dữ kiện Ví dụ 11.27 trên mặt trang (D-8); tên đầy đủ "quá trình quyết định bán-Markov"; "chạy tới khi kết thúc ở $S_k$ sau $k$ bước"; "chiết khấu $\gamma^k$"; câu dẫn mang số (5.3); giữ "gọi tắt bán-MDP"; ghi chú diễn giả bỏ câu VP19.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — gộp ví dụ và thuật toán gọn (mã L11-5-08 của `ke-hoach-trang-chieu.md`); Nhận xét 11.43 đặt ở đây, nơi tên "bán-MDP" được dùng.
- **Ghi chú diễn giả:** tổng chiết khấu trên đường là mẫu không chệch của $r(s,\omega)$, $\gamma^k\mathbb 1\{S_k=s'\}$ là mẫu không chệch của $p(s'\mid s,\omega)$; khi mọi tùy chọn là hành động một bước, $k=1$ và (5.3) là Q-learning (Thuật toán 06.16); Sutton, Precup và Singh (1999, §3.2, tr. 195–196) trình bày thuật toán (Bradtke và Duff, 1995) và nêu ước lượng hội tụ dưới điều kiện tương tự Q-learning, ghi chú không phát biểu định lý; §5.4 đọc thêm: Q-learning trong tùy chọn (Nhận xét 11.47).

#### `L11-5-09` Bài tập: mô hình tùy chọn khi trượt nhiều hơn
- **Vị trí, bước:** mạch 5; kiểm tra (đề và lời giải fragment) của cụm mô hình tùy chọn.
- **Lý do tồn tại:** NT24; Q15 (đề và lời giải một trang).
- **Liên kết:** trước `L11-5-08`; sau `L11-6-00`.
- **Mục tiêu:** 6.
- **Nguồn:** Bài tập 11.7 và lời giải; `lec-11-topic-27`.
- **Mặt trang:**
  - "Câu hỏi (Bài tập 11.7): mê cung hai phòng trượt với xác suất $\delta=0{,}5$ (trượt thì ở yên), $+1$ khi vào $\mathrm Z$, $\gamma=0{,}9$; $\omega_1$, $\omega_2$ như Ví dụ 11.24. (a) Chứng minh $\rho=(1-\delta)\gamma/(1-\delta\gamma)$. (b) Tính $p(\mathrm K\mid\mathrm B,\omega_1)$, $r(\mathrm K,\omega_2)$ và giá trị của $\mathrm B$ theo "$\omega_1$ rồi $\omega_2$". (c) Kiểm Mệnh đề 11.41." (39; hai dòng hiển thị)
  - fragment "Lời giải: (a) bước đi đúng ở lần thử thứ $j$ với xác suất $\delta^{j-1}(1-\delta)$, nên $\rho=\sum_{j\ge1}\gamma^j\delta^{j-1}(1-\delta)=(1-\delta)\gamma/(1-\delta\gamma)$." (16)
  - fragment "(b) $\rho=0{,}8182$; $p(\mathrm K\mid\mathrm B,\omega_1)=\rho^2=0{,}6694$; $r(\mathrm K,\omega_2)=0{,}5/0{,}55=0{,}9091$; $v_\mu(\mathrm B)=0{,}6694\cdot0{,}9091=0{,}6086$." (1)
  - fragment "(c) $\omega_1$ chỉ kết thúc ở $\mathrm K$, nên tổng hệ số là $0{,}6694\le0{,}9$." (12)
  - fragment "Với $\delta=0{,}2$, công thức cho lại $\rho=0{,}8780$." (8)
- **Mật độ:** khoảng 76 âm tiết, 5 dòng: ngoại lệ (đề giữ câu chữ, mục 4). **Số đo cuối** (`deck_lint`, sau III.5): 69 âm tiết, trần 60, tỉ lệ 1,15.
- **Hình, phút:** —; 2,5.
- **Quyết định:** thêm — gộp đề và lời giải bằng fragment (Q15, QT3).
- **Ghi chú diễn giả (NT-RL-10):** năng lực kiểm: tính mô hình tùy chọn qua chuỗi hình học và dùng (5.2). "Gợi ý: số lần thử của một bước đi đúng có phân phối hình học." $r(\mathrm K,\omega_2)=\rho/\gamma$; $v_\mu(\mathrm K)=r(\mathrm K,\omega_2)$ vì $\omega_2$ kết thúc ở $\mathrm Z$ có giá trị $0$. Kết quả của mạch: tùy chọn gộp nhiều bước mà vẫn giữ phương trình Bellman và tính co; cái giá là phải tính hoặc học mô hình tùy chọn.

### Mạch 6. Tổng kết (9 trang, 11 phút)

Không khái niệm mới (NT15). Thứ tự: bảng tổng kết (P4 cột ba, bảng thứ ba gộp vào, mục 3) → bảng phương pháp (P4) → "Vấn đề trung tâm" → bài tập tổng hợp (NT-RL-9) → câu hỏi tự kiểm tra → bài tập về nhà → tài liệu tham khảo.

#### `L11-6-00` 6. Tổng kết (trang tiêu đề mạch), điểm vào mạch 6
- **Vị trí, bước:** điểm vào mạch 6; `section.strand-title`, `id="mach-6"`, `data-note-topic-id="lec-11-topic-24"`; ngoài hành trình khái niệm.
- **Lý do tồn tại:** NT12, NT15 (tên "Tổng kết").
- **Liên kết:** trước `L11-5-09`; sau `L11-6-01`.
- **Mục tiêu:** 7.
- **Mặt trang:** "6." + "Tổng kết"; `p.strand-lead` "Bốn cách dùng mô hình khác nhau ở thời điểm tính, loại hành động và bảo đảm." (17); không `p.strand-keys`.
- **Mật độ:** **Số đo cuối** (`deck_lint`, sau III.5): 17 âm tiết, trần 25, tỉ lệ 0,68.
- **Sau biên tập (2026-11-19):** dòng dẫn "Bốn cách dùng mô hình khác nhau ở thời điểm tính, loại hành động và bảo đảm." (17), theo vai mạch (bản "hai chỗ" bị thay vì lặp luận điểm bìa).
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT12, NT15.
- **Ghi chú diễn giả (40–100):** kế thừa: kết quả của bốn mạch nội dung; việc của mạch: so bốn cách dùng mô hình trên cùng tiêu chí, trả lời câu hỏi trung tâm có điều kiện, luyện một bài tổng hợp; không thêm khái niệm mới; "hai chỗ" là một ô của bảng đếm (Mệnh đề 11.5) và dự báo vòng hở (Mệnh đề 11.36), theo Tóm tắt chương.

#### `L11-6-01` Bảng tổng kết
- **Vị trí, bước:** mạch 6; tổng kết (NT15).
- **Lý do tồn tại:** mỗi kết quả chính một hàng, giữ lượng từ và loại bảo đảm (NT2, NT15); đồng thời là bảng thứ ba của P4 (mục 3).
- **Liên kết:** trước `L11-6-00`; sau `L11-6-02`.
- **Mục tiêu:** 1–6.
- **Nguồn:** §6.1; Tóm tắt chương ("Định nghĩa và kết quả theo mục", "Giả thiết hay bị bỏ quên"); `lec-11-topic-26`.
- **Mặt trang:** bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`, tám hàng:
  - Mệnh đề 11.5 | $C$ cố định trước; lần thử độc lập, cùng phân phối | $\mathbb E\hat p=p$, $\operatorname{Var}\hat p=p(1-p)/C$
  - Mệnh đề 11.9 | mô hình cố định, xác định ở mọi cặp; mọi cặp vô hạn lần; Robbins–Monro | $Q\to\hat q_*$ hầu chắc chắn
  - Mệnh đề 11.15(b) | phần thưởng $0$; $b$ kế đồng khả năng; giá trị kế cố định, độc lập, cùng kỳ vọng, phương sai $1$; $k$ mẫu độc lập, $\alpha_j=1/j$ | $\sqrt{(b-1)/(bk)}$
  - Mệnh đề 11.21, 11.22 | $q_{\pi_0}$ chính xác; với 11.22: mô hình đúng, $m$ chọn trước, mô phỏng độc lập, không cắt | $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$; $\Pr\{\bar G(a')\ge\bar G(a)\}\le e^{-m\Delta^2/B^2}$
  - Định lý 11.27 | mô hình đúng; cắt ở độ sâu $D$; (a) phần thưởng trong $[0,1]$, $c_{\mathrm{ucb}}=\sqrt2\,D$ | (a) xác suất chọn sai ở gốc $\to0$; (b) $0\le v_*-v^D_*\le\gamma^D$
  - Mệnh đề 11.30 | $\hat f$, $c$ khả vi liên tục | $\partial J/\partial u_t=\partial_{u_t}c+\lambda_{t+1}\partial_{u_t}\hat f$
  - Mệnh đề 11.36 | chuỗi hành động cố định; $f$ Lipschitz hằng số $L$ | $e_k\le\bar e\,(L^k-1)/(L-1)$
  - Định lý 11.42, 11.44 | tùy chọn Markov, kết thúc với xác suất $1$; mô hình tùy chọn đúng; $\Omega(s)$ hữu hạn | $v_\mu=\sum_\omega\mu\,[r+\sum_{s'}p\,v_\mu]$; $T_\Omega$ co hệ số $\gamma$; $v_\Omega\le v_*$, bằng nhau khi $\Omega(s)\supseteq\mathcal A(s)$
- **Mật độ:** khoảng 100 âm tiết (cột một, hai và chữ trong cột ba; trước 85), 8 hàng: ngoại lệ NT17, lý do: mỗi kết quả chính một hàng giữ đủ lượng từ và giả thiết (NT15, NT2; phát hiện nghiêm trọng của cổng về 11.15(b)); trần bảng tổng kết 80, 1,5 lần là 120. **Số đo cuối** (`deck_lint`, sau III.5): 79 âm tiết, trần 80, tỉ lệ 0,99.
- **Sau biên tập (2026-11-19):** cột "Kết quả" chỉ có số hiệu, tên tám kết quả ở ghi chú diễn giả (D-4: thêm tên làm bảng tràn khung); hàng 11.27: "mô hình đúng; cắt ở $D$; (a): $c_{\mathrm{ucb}}=\sqrt2\,D$, UCT nguyên bản, không cho Thuật toán 11.26" và "chọn sai $\to0$ (bài toán cắt); $v_*-v^D_*\le\gamma^D$" (D-2); hàng 11.42, 11.44: "$\Pr\{\tau<\infty\}=1$; mô hình tùy chọn đúng"; ô giả thiết các hàng khác rút để vừa khung (11.9: "mô hình cố định, xác định ở mọi cặp"; 11.15(b): "$b$ kế đồng khả năng, cùng kỳ vọng"); ghi chú diễn giả: "Chỉ 11.5 và 11.36 chặn sai số của mô hình." (D-5). Xem câu hỏi C8 ở mục 14.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm — NT15; gộp 11.21 với 11.22 và 11.42 với 11.44 thành một hàng mỗi cặp: hai kết quả của mỗi cặp dùng chung đối tượng và giả thiết gốc ($\pi_0$ và $q_{\pi_0}$; tùy chọn và mô hình tùy chọn), Q16.
- **Ghi chú diễn giả:** loại bảo đảm từng hàng: hội tụ hầu chắc chắn (11.9), xác suất (11.22, 11.27(a)), tất định (11.5, 11.15, 11.21, 11.30, 11.36, 11.42); 11.27(a) nói về UCT của Kocsis và Szepesvári, không về Thuật toán 11.26; 11.36 đo sai số trên quỹ đạo dự báo; mọi hàng trừ 11.5 và 11.36 nói về MDP của mô hình.

#### `L11-6-02` So sánh bốn cách dùng mô hình
- **Vị trí, bước:** mạch 6; bảng phương pháp của P4 (bài nhiều thuật toán).
- **Lý do tồn tại:** so bốn phương pháp trên cùng tiêu chí (NT-RL-5, `CLAUDE.md` "Tables").
- **Liên kết:** trước `L11-6-01`; sau `L11-6-03`.
- **Mục tiêu:** 7.
- **Nguồn:** §6.1 (bảng bốn hàng); Thuật toán 11.10, 11.26, 11.31, 11.33, 11.45; `lec-11-topic-24`.
- **Mặt trang:** bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng`, bốn hàng:
  - Dyna-Q | Q-learning trên mẫu thật (bước (d)) và mẫu của mô hình (bước (f)) | bước thật; mô hình học từ bước thật | hết ngân sách bước thật
  - Tìm kiếm theo cây với UCT | chọn theo (3.3); $N\leftarrow N+1$, $W\leftarrow W+G$ trên các cạnh đã đi | mô phỏng từ trạng thái hiện tại trên mô hình mẫu | hết ngân sách vòng lặp; trả cạnh gốc có $N$ lớn nhất
  - Hạ gradient trong điều khiển dự báo | $u\leftarrow u-\eta\nabla J$; mỗi bước thật giải lại từ $x_t$ | mô hình khả vi; trạng thái thật $x_t$ | $\lVert\nabla J\rVert\le\theta$ hoặc hết ngân sách
  - Lặp giá trị với tùy chọn | $V_{k+1}=T_\Omega V_k$ | mô hình tùy chọn $r(s,\omega)$, $p(s'\mid s,\omega)$ | $\lVert V_{k+1}-V_k\rVert_\infty\le\theta$
- **Mật độ:** khoảng 70 âm tiết, 4 hàng (trần 80 của bảng so sánh). **Số đo cuối** (`deck_lint`, sau III.5): 97 âm tiết, trần 80, tỉ lệ 1,21.
- **Sau biên tập (2026-11-19):** cột "Phương pháp" ghi "(nền)" / "(thời điểm quyết định)" (D-8, NT-RL-4); điều kiện dừng của điều khiển dự báo đúng Thuật toán 11.33 ("mỗi bước: …; hết số bước điều khiển"); ô quy tắc ngắt bằng `<br>`; ghi chú diễn giả theo D-5.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm — P4.
- **Ghi chú diễn giả:** cột "khi nào tính" của §6.1: Dyna-Q và lặp giá trị với tùy chọn là lập kế hoạch nền, hai hàng giữa là tại thời điểm quyết định; ba cách dùng mô hình của §1.2 thành bốn hàng vì tìm kiếm lúc ra quyết định tách theo hành động rời rạc và liên tục; sai số mô hình: Dyna-Q tới $\hat q_*$ của mô hình sai, MCTS có bảo đảm cho MDP của mô hình, vòng hở theo (4.4), lặp giá trị với tùy chọn tới điểm bất động của $T_\Omega$ trên mô hình sai.

#### `L11-6-03` Vấn đề trung tâm
- **Vị trí, bước:** mạch 6; trả lời câu hỏi trung tâm của cả bài (NT15), không theo mạch; mỗi dòng một cách dùng mô hình, dòng kết trả lời vế "bảo đảm nào mất đi".
- **Lý do tồn tại:** NT15, NT11 (câu hỏi ở `L11-1-07`).
- **Liên kết:** trước `L11-6-02`; sau `L11-6-04`.
- **Mục tiêu:** 7.
- **Nguồn:** §6.2 (bốn ý); Tóm tắt chương (câu cuối); `lec-11-topic-24`.
- **Mặt trang:** năm dòng:
  - "Q-planning hội tụ tới $\hat q_*$ khi mô hình cố định, xác định ở mọi cặp; Dyna-Q với $n=2$ cho $Q(\mathrm F,\rightarrow)=0{,}225$ sau một lượt." (21)
  - "Với $q_{\pi_0}$ chính xác, rollout đưa $\mathrm F$ từ $0{,}2016$ lên $0{,}8566$; $m=70$ giữ xác suất chọn sai không quá $0{,}0496$." (17)
  - "Một bước gradient giảm $J$ từ $8$ xuống $2{,}88$; điều khiển dự báo co về $0$ với hệ số $0{,}6$ trên hệ thật dù mô hình sai." (24)
  - "Hai tùy chọn cho $v_*(\mathrm A)=0{,}6604$ sau hai vòng, so với $0{,}6103$ sau sáu lượt quét; $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$." (16)
  - "Khi mô hình sai, các bảo đảm trên nói về MDP của mô hình; sai số mô hình chỉ được chặn cho một ô của bảng đếm và cho dự báo vòng hở." (29)
- **Mật độ:** khoảng 107 âm tiết, 5 dòng: ngoại lệ (mục 4; trần 80 như trang trả lời bài toán của deck 10, 1,5 lần là 120). Dòng kết là kết luận có điều kiện (NT18). **Số đo cuối** (`deck_lint`, sau III.5): 111 âm tiết, trần 80, tỉ lệ 1,39.
- **Sau biên tập (2026-11-19):** năm dòng (D-1, D-8): Q-planning hội tụ tới $\hat q_*$ khi mô hình cố định, xác định ở mọi cặp; Dyna-Q ngoài giả thiết đó vẫn cho $0{,}225$ sau một lượt, Q-learning cho $0$ / rollout đưa giá trị tại $\mathrm F$ từ $0{,}2016$ lên $0{,}8566$; "$m=70$: xác suất xếp $\downarrow$ trên $\rightarrow$ không quá $0{,}0496$" / "Với mô hình khả vi", $8\to2{,}88$; trên hệ thật $1{,}2x+u$, điều khiển dự báo với mô hình $x+u$ co hệ số $0{,}6$ / hai vòng cho $0{,}6604$, sáu lượt quét chỉ cho $0{,}6103$; $v_\Omega=v_*$ khi $\Omega(s)\supseteq\mathcal A(s)$ / khi mô hình sai, bảo đảm nói về MDP của mô hình; sai số chỉ được chặn "ở một ô của bảng đếm và ở dự báo vòng hở".
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT15.
- **Ghi chú diễn giả:** nguồn từng dòng: Mệnh đề 11.9, Ví dụ 11.7, Nhận xét 11.11 (Dyna-Q không thỏa giả thiết của 11.9); Mệnh đề 11.21, 11.22, Ví dụ 11.13, 11.14; Định lý 11.27 (UCT nhất quán cho bài toán cắt, $\gamma^{20}=0{,}1216$); Mệnh đề 11.30, 11.36, Ví dụ 11.18, 11.19, 11.23; Định lý 11.44, Ví dụ 11.26; Mệnh đề 11.5 và 11.36 cho hai chỗ có chặn sai số mô hình. Môi trường ngẫu nhiên cần mô hình đếm, môi trường thay đổi cần thưởng thăm dò.

#### `L11-6-04` Bài tập: mô hình đếm và tùy chọn trên mê cung hai phòng
- **Vị trí, bước:** mạch 6; bài tập tổng hợp (đề), dùng kết quả của mạch 2 và 5 trên một bài toán Học tăng cường cụ thể (NT15, NT-RL-9; Q13).
- **Lý do tồn tại:** NT15 một bài tập tổng hợp với lời giải trên mặt trang.
- **Liên kết:** trước `L11-6-03`; sau `L11-6-05`.
- **Mục tiêu:** 1, 6, 7.
- **Nguồn:** Bài tập 11.10 (Mức vận dụng); `lec-11-topic-27`.
- **Mặt trang:**
  - "Câu hỏi (Bài tập 11.10): mê cung hai phòng ($\gamma=0{,}9$, $+1$ khi vào $\mathrm Z$, không đi đúng thì ở yên). Giả sử $C(\mathrm B,\downarrow)=4$ với $3$ lần tới $\mathrm F$; $C(\mathrm F,\rightarrow)=10$ với $8$ lần tới $\mathrm K$; $C(\mathrm K,\rightarrow)=5$ với $4$ lần tới $\mathrm Z$." (31; hai dòng hiển thị)
  - "(a) Tính mô hình đếm và độ lệch chuẩn ước lượng của $\hat p(\mathrm F\mid\mathrm B,\downarrow)$." (14)
  - "Tùy chọn $\omega_1$ đi $\mathrm B\mapsto\downarrow$, $\mathrm F\mapsto\rightarrow$, kết thúc khi tới $\mathrm K$; $\omega_2$ đi $\mathrm K\mapsto\rightarrow$, kết thúc khi vào $\mathrm Z$. (b) Tính $p(\mathrm K\mid\mathrm B,\omega_1)$, $r(\mathrm K,\omega_2)$ trên mô hình đếm." (25)
  - "(c) Tính $\hat v(\mathrm B)$ theo "$\omega_1$ rồi $\omega_2$". (d) So với $v_*(\mathrm B)=0{,}7522$ và với $0{,}81$ của mô hình tất định." (19)
- **Mật độ:** khoảng 89 âm tiết sau khi chuyển câu (e) sang `L11-6-05` (trước 115), 4 dòng: ngoại lệ NT17 "đề bài tập giữ nguyên câu chữ" (Bài tập 11.10, câu (a)–(d) nguyên văn ghi chú; trần 60, 1,5 lần là 90). Không rút câu chữ (NT24, cổng). **Số đo cuối** (`deck_lint`, sau III.5): 72 âm tiết, trần 60, tỉ lệ 1,20.
- **Sau biên tập (2026-11-19):** mặt trang không đổi; ghi chú diễn giả bỏ câu về bố cục trang.
- **Hình, phút:** —; 1,5.
- **Quyết định:** thêm — NT15, NT-RL-9; bài 11.10 là bài tổng hợp theo Q13.
- **Ghi chú diễn giả (NT-RL-10):** năng lực kiểm: nối mô hình đếm (mạch 2) với mô hình tùy chọn và Q-learning bán-MDP (mạch 5), tách sai số do bất định nhận thức khỏi sai số hệ thống. "Gợi ý: một bước đi đúng với xác suất $\hat p$ có thừa số $\hat p\gamma/(1-(1-\hat p)\gamma)$." Câu (e) ở trang sau, ngay trên lời giải của nó.

#### `L11-6-05` Bài tập: mô hình đếm và tùy chọn trên mê cung hai phòng
- **Vị trí, bước:** mạch 6; lời giải bài tập tổng hợp, mỗi dòng một bước, kết bằng kết luận ngắn (NT24).
- **Lý do tồn tại:** NT15.
- **Liên kết:** trước `L11-6-04`; sau `L11-6-06`.
- **Mục tiêu:** 1, 6, 7.
- **Nguồn:** lời giải Bài tập 11.10; `lec-11-topic-27`.
- **Mặt trang:** dòng đầu là đề câu (e) nguyên văn ghi chú: "(e) Tại $\mathrm B$, tác tử chạy $\omega_1$ trên mê cung thật, tới $\mathrm K$ sau $k=2$ bước, phần thưởng trên đường bằng $0$; với $Q(\mathrm B,\omega_1)=0$, $\max_{\omega'}Q(\mathrm K,\omega')=0{,}9756$, $\alpha=0{,}5$, thực hiện một cập nhật (5.3)." (24); rồi "Lời giải:" và:
  - "(a) $\hat p(\mathrm F\mid\mathrm B,\downarrow)=0{,}75$, $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=\hat p(\mathrm Z\mid\mathrm K,\rightarrow)=0{,}8$; độ lệch chuẩn ước lượng $\sqrt{0{,}75\cdot0{,}25/4}=0{,}2165$." (6)
  - "(b) Thừa số hai bước $0{,}675/0{,}775=0{,}8710$ và $0{,}72/0{,}82=0{,}8780$, nên $p(\mathrm K\mid\mathrm B,\omega_1)=0{,}7648$; $r(\mathrm K,\omega_2)=0{,}9756$. (c) $\hat v(\mathrm B)=0{,}7648\cdot0{,}9756=0{,}7461$." (8)
  - Bảng khuôn T1, một hàng (e): $(\mathrm B,\omega_1)$ | $\gamma^2\cdot0{,}9756=0{,}7902$ | $0{,}7902$ | $0{,}3951$.
  - "(d) Sai số $-0{,}0061$ đến từ bất định nhận thức ở cặp có $4$ mẫu; mô hình tất định sai $+0{,}0578$, sai số hệ thống không giảm khi thêm dữ liệu." (28)
- **Mật độ:** 66 âm tiết (trước 45), 6 dòng (đề (e); (a); (b) gộp (c); bảng (e); (d)): ngoại lệ NT17 "đề bài tập giữ nguyên câu chữ" (câu (e) chuyển từ `L11-6-04` theo cổng). Câu (d) đặt cuối làm kết luận (thứ tự (a), (b), (c), (e), (d) trên mặt trang; ghi chú diễn giả nói rõ). **Số đo cuối** (`deck_lint`, sau III.5): 71 âm tiết, trần 60, tỉ lệ 1,18.
- **Sau biên tập (2026-11-19):** (b) và (c) chung một dòng ngắn ("(c)&nbsp;"); ghi chú diễn giả bỏ câu về bố cục trang.
- **Hình, phút:** —; 2.
- **Quyết định:** thêm — NT15, NT24.
- **Ghi chú diễn giả:** kiểm tra lại: $\hat p(\mathrm F\mid\mathrm B,\downarrow)=0{,}8$ cho lại $0{,}7522$; độ lệch chuẩn ở (a) thay $p$ chưa biết bằng $\hat p$; với (e), chiết khấu $\gamma^k$, $k=2$; lỗi thường gặp: dùng $\gamma$ một lần cho cả tùy chọn.

#### `L11-6-06` Câu hỏi tự kiểm tra
- **Vị trí, bước:** mạch 6; kiểm tra (NT15, NT-RL-9): mỗi câu kiểm một giả thiết hoặc một phân biệt.
- **Lý do tồn tại:** NT15.
- **Liên kết:** trước `L11-6-05`; sau `L11-6-07`.
- **Mục tiêu:** 1, 2, 4, 6.
- **Nguồn:** §6.3; `lec-11-topic-24`.
- **Mặt trang:** "Câu hỏi: trả lời và nêu kết quả đã dùng." rồi bốn câu đánh số:
  1. "Mệnh đề 11.9 bảo đảm hội tụ tới $q_*$ hay tới $\hat q_*$, dưới giả thiết nào?" (14; phân biệt môi trường và mô hình)
  2. "Vì sao tập mô hình báo độ phân tán $0$ ở cặp chỉ có một mẫu?" (14; phân biệt hai loại bất định)
  3. "Mệnh đề 11.21 còn áp dụng không khi $q_{\pi_0}$ thay bằng trung bình của $m=5$ mô phỏng?" (17; giả thiết "$q_{\pi_0}$ chính xác")
  4. "Khi tập tùy chọn không chứa hành động một bước, lặp giá trị với tùy chọn hội tụ tới đâu?" (20; giả thiết $\Omega(s)\supseteq\mathcal A(s)$)
- **Mật độ:** 75 âm tiết (trước 79), 5 dòng: ngoại lệ NT17, lý do: bốn câu của §6.3 giữ câu chữ của ghi chú, mỗi câu kiểm một giả thiết hoặc một phân biệt (NT15, NT-RL-9); phân biệt "của môi trường" và "của mô hình" nói ở ghi chú diễn giả. **Số đo cuối** (`deck_lint`, sau III.5): 74 âm tiết, trần 60, tỉ lệ 1,23.
- **Hình, phút:** —; 1.
- **Quyết định:** thêm — NT15; giữ đủ bốn câu của §6.3 (NT15 cho 2–4 câu).
- **Ghi chú diễn giả:** lời đáp theo §6.3: (1) $\hat q_*$ của mô hình, khi mô hình cố định và xác định ở mọi cặp; (2) mọi tập lấy lại từ một mẫu trùng mẫu đó (Nhận xét 11.7), trong khi $\operatorname{Var}\hat p=p(1-p)$ với $C=1$ (Mệnh đề 11.5); (3) không: giả thiết bị vi phạm; Mệnh đề 11.22 chỉ cho $\exp(-5\Delta^2)=0{,}8069$, tổng chặn cho bốn hành động vượt $1$; (4) tới $v_\Omega$, với $v_\Omega\le v_*$, có thể nhỏ hơn ngặt (Định lý 11.44(b), (c)).

#### `L11-6-07` Bài tập về nhà
- **Vị trí, bước:** mạch 6; bài tập (NT15).
- **Lý do tồn tại:** xếp mỗi bài của `exercises.md` (11.12–11.19) và của ghi chú (11.1–11.11) vào mạch cung cấp kiến thức cuối cùng bài đó cần; liên kết trình xem.
- **Liên kết:** trước `L11-6-06`; sau `L11-6-08`.
- **Mục tiêu:** 1–7.
- **Nguồn:** Bài tập củng cố (bảng phủ mục tiêu); `exercises.md` (bảng `Mạch | Mở phần | Bài tập`); `lec-11-topic-27`.
- **Mặt trang:** bảng `Mục | Bài tập`, bốn hàng (mạch 1 và 6 không có bài):
  - 2. Tính bất định của môi trường và lập kế hoạch nền | 11.2 (trên lớp), 11.4 (trên lớp), 11.12, 11.13, 11.14, 11.16, 11.17, 11.19
  - 3. Tìm kiếm theo cây Monte Carlo | 11.5 (trên lớp), 11.8, 11.18
  - 4. Tối ưu kế hoạch dựa trên đạo hàm | 11.1, 11.6 (trên lớp), 11.11
  - 5. Học tăng cường phân cấp | 11.3, 11.7 (trên lớp), 11.9, 11.10 (trên lớp), 11.15
  Dòng cuối: "Ghi chú bài giảng · Bài tập", hai liên kết `material-viewer.html?doc=materials/lec-11/lecture-note.md&deck=lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` và `material-viewer.html?doc=materials/lec-11/exercises.md&deck=lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html`.
- **Mật độ:** khoảng 40 âm tiết (tên mục; số bài trong ô không tính), 5 dòng (trần 80 của bảng). **Số đo cuối** (`deck_lint`, sau III.5): 51 âm tiết, trần 80, tỉ lệ 0,64.
- **Sau biên tập (2026-11-19):** ghi chú diễn giả bỏ câu về bố cục trang.
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT15.
- **Căn cứ xếp mạch** (kiến thức cuối cùng bài cần, đối chiếu đề): 11.12, 11.13, 11.19 (Dyna-Q+, mạch 2); 11.14 (cập nhật mẫu, mạch 2); 11.16 (Dyna-Q so với bootstrap nhiều bước, mạch 2); 11.17 (Dyna-Q cho môi trường ngẫu nhiên và thay đổi, mạch 2); 11.18 (cận tin cậy trên, mạch 3); 11.15 (tùy chọn trong thiết lập phần thưởng trung bình, mạch 5); 11.1 (cần điều khiển dự báo, mạch 4); 11.8 (Mệnh đề 11.22, mạch 3); 11.11 (điều khiển dự báo với mô hình sai, mạch 4); 11.3, 11.7 (tùy chọn, mạch 5); 11.9 (tùy chọn ở câu (c), mạch 5); 11.10 (mô hình tùy chọn và (5.3), mạch 5). Khớp bảng mở đầu của `exercises.md`.
- **Ghi chú diễn giả:** bài "[Lập trình]" 11.19 chạy thí nghiệm của Sutton và Barto Bài tập 8.4; bài tự làm của ghi chú có gợi ý và lời giải trong trình xem.

#### `L11-6-08` Tài liệu tham khảo
- **Vị trí, bước:** trang cuối; tài liệu (NT15).
- **Lý do tồn tại:** nguồn mà ghi chú dẫn ở mục "Hướng dẫn đọc thêm và tài liệu tham khảo".
- **Liên kết:** trước `L11-6-07`; sau —.
- **Mục tiêu:** —.
- **Nguồn:** Hướng dẫn đọc thêm và tài liệu tham khảo (mục 1–17); `lec-11-topic-28`.
- **Mặt trang:** danh sách:
  - "Tạ Việt Cường, Trần Quốc Long. *Giáo trình Học tăng cường và lập kế hoạch*, Chương 11."
  - "Sutton, R. S., Barto, A. G. (2018). *Reinforcement Learning: An Introduction*, ấn bản 2: §2.7, Chương 8, §16.6, §17.1–17.2."
  - "Bertsekas, D. P. (2019). *Reinforcement Learning and Optimal Control*: §2.4, §2.5.1, §5.1.2; Bertsekas (2020). *Rollout, Policy Iteration, and Distributed Reinforcement Learning*: §3.1, Mệnh đề 5.4.2."
  - "Sutton, Precup và Singh (1999); Kocsis và Szepesvári (2006); Auer, Cesa-Bianchi và Fischer (2002)."
  - "Chua và cộng sự (2018); Silver và cộng sự (2017); Szepesvári (2010), §4.2.1; Puterman (1994)."
  **Không có dòng nối sang bài sau** (Q8: chờ tác giả xác nhận thứ tự Bài 12; ghi chú cũng không có câu nối nội dung). Không URL trên mặt trang.
- **Mật độ:** khoảng 70 âm tiết, 5 dòng (trần 80 của trang tài liệu tham khảo). **Số đo cuối** (`deck_lint`, sau III.5): 86 âm tiết, trần 80, tỉ lệ 1,07.
- **Sau biên tập (2026-11-19):** năm dòng có mục (D-10): giáo trình của học phần (Chương 11; mục 4.3.1, 4.3.2, 4.7); Sutton và Barto (§2.7, §8.1–8.11, §16.6, §17.1–17.2); Bertsekas 2019, 2020; Sutton, Precup và Singh (tr. 186–205); Kocsis và Szepesvári (Định lý 6); Auer và cộng sự (Định lý 1); Hoeffding; Chua và cộng sự (§4–6); Silver và cộng sự (Phương pháp, mục "Select"); nguồn còn lại và câu "Danh mục đầy đủ ở ghi chú bài giảng" ở ghi chú diễn giả; không dòng nối (Q8).
- **Hình, phút:** —; 0,5.
- **Quyết định:** thêm — NT15, trừ dòng nối (Q8).
- **Ghi chú diễn giả:** vai của từng nguồn theo ghi chú: Sutton và Barto Chương 8 cho Mục 1–3, §2.7 cho cận tin cậy trên, §17.2 cho tùy chọn; Bertsekas cho rollout và điều khiển dự báo; Sutton, Precup và Singh cho bán-MDP; Kocsis và Szepesvári cho UCT; Auer và cộng sự cho UCB1; Chua và cộng sự cho tập mô hình và entropy chéo trong PETS; Silver và cộng sự cho PUCT.

## 8. Ánh xạ hai chiều `note-topic-id` ↔ `data-slide-id` (GC-RL-12)

Thuộc tính `data-note-topic-id` của mỗi trang lấy mã đầu tiên ở cột `note-topic-id` của mục 3. Bảng dưới gồm cả chủ đề phụ có mặt trên trang và chủ đề chỉ có ở ghi chú diễn giả.

| `note-topic-id` | Chủ đề (nhóm theo `outline.md`) | Trang trên mặt | Chỉ ở ghi chú diễn giả |
|---|---|---|---|
| `lec-11-topic-01` | Kiến thức tiên quyết, bảng ký hiệu (cầu nối) | `L11-1-02`, `L11-1-03`, `L11-1-04` | — |
| `lec-11-topic-02` | Kết quả kế thừa và bài toán trung tâm (cốt lõi) | `L11-1-01`, `L11-1-06`, `L11-1-07` | — |
| `lec-11-topic-03` | Ba cách dùng mô hình (cốt lõi) | `L11-1-05`, `L11-1-06` | — |
| `lec-11-topic-04` | Mô hình phân phối, mô hình mẫu; lập kế hoạch nền và tại thời điểm quyết định (cốt lõi) | `L11-2-00`, `L11-2-01`, `L11-2-02` | — |
| `lec-11-topic-05` | Mô hình đếm và hai loại bất định (cốt lõi) | `L11-2-03`, `L11-2-04` | — |
| `lec-11-topic-06` | Tập mô hình (bổ sung) | `L11-2-04` (một dòng "Lưu ý:") | `L11-2-04` (Ví dụ 11.5) |
| `lec-11-topic-07` | Q-planning và Dyna-Q (cốt lõi) | `L11-2-06`, `L11-2-07`, `L11-2-08`, `L11-2-12` | — |
| `lec-11-topic-08` | Mô hình sai, Dyna-Q+ (cốt lõi) | `L11-2-09` | — |
| `lec-11-topic-09` | Cập nhật kỳ vọng và cập nhật mẫu (cốt lõi) | `L11-2-10` | — |
| `lec-11-topic-10` | Quét ưu tiên, lấy mẫu theo quỹ đạo, RTDP (đọc thêm) | — | `L11-2-07`, `L11-2-08` |
| `lec-11-topic-11` | Thuật toán rollout (cầu nối) | `L11-3-00`–`L11-3-05` | — |
| `lec-11-topic-12` | Quy tắc cận tin cậy trên, UCB1 (cầu nối) | `L11-3-06` | — |
| `lec-11-topic-13` | Bốn pha của MCTS (cốt lõi) | `L11-3-07`, `L11-3-08`, `L11-3-09` | — |
| `lec-11-topic-14` | Bảo đảm của UCT (cốt lõi); AlphaGo Zero, Nhận xét 11.28 (đọc thêm) | `L11-3-08` (dòng "Lưu ý:"), `L11-3-10` | `L11-3-08` (PUCT) |
| `lec-11-topic-15` | Bài toán tối ưu kế hoạch (cốt lõi) | `L11-4-00`, `L11-4-01`, `L11-4-02` | — |
| `lec-11-topic-16` | Đạo hàm qua mô hình (cốt lõi) | `L11-4-02`, `L11-4-03`, `L11-4-04` | — (đoạn PILCO sau Ví dụ 11.19 không lên deck) |
| `lec-11-topic-17` | Điều khiển dự báo theo chân trời lùi (cầu nối) | `L11-4-05` | — |
| `lec-11-topic-18` | Bắn ngẫu nhiên, phương pháp entropy chéo (bổ sung) | `L11-4-04` (dòng "Cách khác:") | `L11-4-04` (Ví dụ 11.21) |
| `lec-11-topic-19` | Sai số mô hình tích lũy (cốt lõi) | `L11-4-06`, `L11-4-07` | `L11-4-06` (Nhận xét 11.37) |
| `lec-11-topic-20` | Tùy chọn, chính sách phân cấp (cốt lõi) | `L11-5-00`, `L11-5-01`, `L11-5-02` | — |
| `lec-11-topic-21` | Mô hình tùy chọn, bán-MDP (cốt lõi) | `L11-5-03`–`L11-5-06`, `L11-5-08` (Nhận xét 11.43) | — |
| `lec-11-topic-22` | Lập kế hoạch nhiều mức, Q-learning bán-MDP (cốt lõi) | `L11-5-07`, `L11-5-08` | — |
| `lec-11-topic-23` | Học mô hình tùy chọn (đọc thêm) | — | `L11-5-08` (Nhận xét 11.47) |
| `lec-11-topic-24` | Tổng kết (§6.1–6.3) | `L11-6-00`, `L11-6-02`, `L11-6-03`, `L11-6-06` | — |
| `lec-11-topic-25` | Tình huống áp dụng và ứng dụng | — | `L11-2-08` (Tình huống 11.2), `L11-4-07` (Tình huống 11.1), `L11-3-08` (Ứng dụng: AlphaGo) |
| `lec-11-topic-26` | Tóm tắt chương | `L11-6-01` | — |
| `lec-11-topic-27` | Bài tập củng cố | `L11-2-05`, `L11-2-11`, `L11-2-12`, `L11-3-11`, `L11-4-08`, `L11-5-09`, `L11-6-04`, `L11-6-05`, `L11-6-07` | bài tự làm 11.1, 11.3, 11.8, 11.9, 11.11 ở ghi chú diễn giả các trang liên quan |
| `lec-11-topic-28` | Hướng dẫn đọc thêm và tài liệu tham khảo | `L11-6-08` | — |

Chiều ngược (mỗi `data-slide-id` → mã chính): theo cột `note-topic-id` của mục 3; mọi trang có đúng một mã chính, mọi mã `lec-11-topic-01` … `-28` có ít nhất một trang hoặc một ghi chú diễn giả. Chủ đề đọc thêm (`-10`, `-23`) và tình huống (`-25`) không lên mặt trang; ghi chú diễn giả nói rõ "nội dung đọc thêm của ghi chú" (NT5).

## 9. Kiểm tra máy và ngoại lệ `deck_lint.py` đã biết (NT28, P10, `NGUYEN-TAC-HOC-PHAN.md` mục 5)

- **Ngoại lệ cấu trúc của mục 5:** không áp dụng. Deck dựng mới theo lược đồ `L11-k-mm` (bìa `L11-1-01`, trang tiêu đề mạch `L11-k-00`, `id="mach-k"`), nên phép kiểm ID bìa đạt; không dự kiến `<style>` hay `style=""` (P7). Bố cục hai cột hình–chữ ở `L11-1-06`, `L11-2-08`, `L11-4-06`, `L11-5-03` dùng `.grid2` có sẵn (C7); không CSS cục bộ.
- **Ngoại lệ mật độ đã biết của `deck_lint.py`:** 35 phát hiện `SYLL60` trên deck cuối (0 `NOTES150`, `LINES6`, `LABEL`, `BANNED`, `REPEAT`, `STRUCT`). Công cụ dùng trần 60 cho mọi trang; trong 35 phát hiện, các trang có trần 80 theo NT17 (mục tiêu, nội dung, thuật toán, ý tưởng chứng minh, bảng tổng kết, bảng so sánh, trả lời câu hỏi trung tâm, bài tập về nhà, tài liệu tham khảo) không phải ngoại lệ khi ≤ 80, còn các trang vượt trần của chúng là ngoại lệ có lý do ở mục 4; bìa `L11-1-01` (79) không áp trần. Ghi nhận như ngoại lệ đã biết tới khi `tools/deck/courses.json` có trần theo loại trang.
- **Nhãn hình ở 390 × 844 (quyết định D-11, 2026-11-19):** nhãn trên năm `-slide.svg` chỉ khoảng 5 px ở 390 × 844 vì Reveal thu nhỏ cả khung 1280 × 720 ở màn hẹp, như mọi deck của học phần; NT25 (chữ ≥ 16 px) áp ở kích thước chiếu. Không sửa, không vẽ bản `-slide-narrow.svg`; điều phối viên ghi quyết định vào `review-log.md`.
- **Ngoại lệ nội dung đã biết:** `L11-6-08` không có dòng nối sang bài sau (Q8); `deck_lint.py` không báo.
- **Kết quả kiểm sau III.5** (theo nhật ký của biên tập viên): `formula_overflow.py` `[]`; `footer_check.py` 0 trang chạm chân trang; Playwright 1600 × 900 trên cả 60 trang (vòng 1) và 22 trang đổi (vòng 2), 390 × 844 trên các trang đổi: 0 lỗi console, 0 request hỏng, 0 `.katex-error`.
- **Kiểm khác** (NT28): `deck_check.py` (bản math-4-AI), `footer_check.py`, `formula_overflow.py` ở 390 × 844 (các công thức dài: (d) của `L11-2-08`, (3.2) ở `L11-3-06`, (4.2)–(4.3) ở `L11-4-03`, (5.1) ở `L11-5-04`, (5.2) ở `L11-5-05`, $T_\Omega$ ở `L11-5-07`, (5.3) ở `L11-5-08`: ngắt bằng `aligned`, không `\tag`, không `\text{}` tiếng Việt); ảnh 1600 × 900 và 390 × 844; liên kết `#/1` … `#/6` của `L11-1-05`; liên kết trình xem ở `L11-6-07`; fragment ở `L11-2-05`, `L11-2-12`, `L11-3-11`, `L11-4-08`, `L11-5-09`, `L11-6-05` hiện đủ bằng phím.

## 10. Sai khác so với kế hoạch `ke-hoach-trang-chieu.md` (điều chỉnh theo ghi chú đã duyệt và bảng Q)

- **Số trang:** 60 thay 60 của kế hoạch nhưng khác phân bổ (7 + 13 + 12 + 9 + 10 + 9 thay 6 + 12 + 11 + 11 + 11 + 9); mục tiêu 58 của Q15 không đạt, lý do ở mục 3, câu hỏi C1.
- **Tên mạch:** theo đúng tên mục của ghi chú, kể cả mạch 1 "Bài toán lập kế hoạch với mô hình học được" và mạch 2 "Tính bất định của môi trường và lập kế hoạch nền" (kế hoạch: "Mở đầu", "Tính bất định và lập kế hoạch nền"); câu hỏi C3.
- **Mạch 1:** thêm `L11-1-04` (mục tiêu 5–7); "Ngữ cảnh" là tiêu đề trang (kế hoạch: "Ngữ cảnh: mê cung hai phòng"; NT16 không có tiền tố "Ngữ cảnh:"); luận điểm của bìa viết lại: "Các bảo đảm của lập kế hoạch nói về bài toán mà mô hình định nghĩa; chúng đúng cho môi trường thật khi mô hình đúng trên những trạng thái mà kế hoạch đi qua." (kế hoạch nói "sai số … tích lũy theo chân trời", chỉ đúng cho vòng hở của Mệnh đề 11.36).
- **Mạch 2:** tách Định nghĩa 11.2 ra `L11-2-02`; Mệnh đề 11.9 đứng cùng Ví dụ 11.6 và Thuật toán 11.8 (`L11-2-06`) như thứ tự ghi chú, không ở trang Dyna-Q; hai trang ví dụ Dyna-Q gộp thành `L11-2-07`; hình `cap-nhat-ky-vong-va-mau` không lên deck; số liệu theo ghi chú (bảng $0{,}2828$; $0{,}1789$; $0{,}0566$; sai số $0{,}3146$).
- **Mạch 3:** thêm trang Thuật toán 11.20 (`L11-3-02`) và trang Mệnh đề 11.22 (`L11-3-05`); Ví dụ 11.15 dùng $\ln9$, chỉ số $1{,}2051$, $1{,}4481$ (kế hoạch $1{,}189$, $1{,}420$); Ví dụ 11.16 theo dữ kiện mới ($W$ bốn chữ số, $\bar Q(\mathrm F,\uparrow)=0{,}5214$, $N(\mathrm B)=0$); Bài tập 11.5 theo số mới ($1{,}4344$; $1{,}6419$; $1{,}5696$; $1{,}6882$; $\bar Q=0{,}4674$) và gộp đề với lời giải; Định lý 11.27 phát biểu (a) cho UCT của Kocsis và Szepesvári với $c_{\mathrm{ucb}}=\sqrt2\,D$, (b) với $\gamma^D$; dòng AlphaGo Zero chuyển sang `L11-3-08`.
- **Mạch 4:** bỏ trang entropy chéo (Q15), thay bằng dòng "Cách khác:" ở `L11-4-04`; đề và lời giải Bài tập 11.6 gộp; câu nối từ mạch 3 đặt ở `L11-4-01`.
- **Mạch 5:** Nhận xét 11.43 (bán-MDP) đặt ở `L11-5-08`; Ví dụ 11.26 và Định lý 11.44 cùng `L11-5-07`; số theo ghi chú ($0{,}7710$; $0{,}6769$; $v_\mu(\mathrm B)=0{,}6086$; kiểm $\delta=0{,}2$ cho $\rho=0{,}8780$).
- **Mạch 6:** bảng tổng kết một trang, tám hàng, gộp bảng thứ ba của P4; Bài tập 11.10 có năm câu (kế hoạch ghi bốn); `L11-6-08` không có dòng nối sang bài sau (Q8, thay QT8).
- **Câu hỏi của mạch 2:** "…, và dùng nó thế nào để có thêm cập nhật?" (rút từ "để mỗi bước thật cho nhiều cập nhật", 24 → 22 âm tiết; nghĩa giữ).

## 11. Đề xuất sửa ghi chú (NT3; không sửa trong giai đoạn này)

| Mức độ | Vị trí | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| trung bình | §6.1, bảng "So sánh bốn cách dùng mô hình", hàng Dyna-Q, cột "Sai số mô hình ảnh hưởng thế nào" | Ô ghi "tới $\hat q_*$ của mô hình sai" như thể Dyna-Q hội tụ tới $\hat q_*$; Mệnh đề 11.9 chỉ bảo đảm điều đó cho Q-planning trên mô hình cố định, xác định ở mọi cặp, và Nhận xét 11.11 nói Dyna-Q không thỏa giả thiết này (phát hiện của vai toán khi rà deck, D-5) | ô của ghi chú: "tới $\hat q_*$ của mô hình sai; cặp bi quan cần thưởng thăm dò"; cột "Bảo đảm" cùng hàng: "Dyna-Q không thỏa giả thiết đó (Nhận xét 11.11)"; deck `L11-6-02` ghi chú diễn giả đã viết "Q-planning trên mô hình sai cố định tiến tới $\hat q_*$ của mô hình đó, còn Dyna-Q không thỏa giả thiết của Mệnh đề 11.9" | đổi ô thành "Q-planning trên mô hình sai cố định tiến tới $\hat q_*$ của mô hình đó; Dyna-Q không có bảo đảm này; cặp bi quan cần thưởng thăm dò" |
| nhẹ | chứng minh Mệnh đề 11.15, Bước 3; đoạn "Bỏ 'cùng kỳ vọng' ở (b)" | Chữ $m$ mang hai nghĩa, trái quy ước "mỗi chữ giữ một nghĩa trong cả chương" của Bảng ký hiệu | Bảng ký hiệu: "$m$ \| số mô phỏng cho mỗi hành động của thuật toán rollout"; chứng minh 11.15: "Gọi $m$ là kỳ vọng chung của các $y_i$"; phản ví dụ: "$y_i$ có kỳ vọng $m_i$ với trung bình $\bar m$" | đổi kỳ vọng chung thành một chữ chưa dùng, ví dụ $\upsilon$, $\upsilon_i$, $\bar\upsilon$ |
| nhẹ | Thuật toán 11.45, bước 2 và điều kiện dừng | Chữ $\Delta$ đã là khoảng cách giá trị hành động (Mệnh đề 11.22, Ví dụ 11.14, §3.2) và $\Delta_a$ (Định lý 11.24); ở đây $\Delta_k$ là phần dư của lặp giá trị | "$\Delta_k\leftarrow\lVert V_{k+1}-V_k\rVert_\infty$ … Điều kiện dừng. $\Delta_k\le\theta$" | viết thẳng điều kiện dừng $\lVert V_{k+1}-V_k\rVert_\infty\le\theta$ (deck `L11-5-07`, `L11-6-02` viết như vậy), bỏ tên $\Delta_k$ |
| nhẹ | Bài tập 11.5, đề | Dữ kiện cho $\bar Q$ ở ba cạnh và $W$ ở cạnh $\leftarrow$, khác khuôn bảng của Ví dụ 11.16 (cạnh, $N$, $W$, $\bar Q$, số hạng thăm dò, chỉ số) | "$\rightarrow$: $N=4$, $\bar Q=0{,}6932$; … $\leftarrow$: $N=1$, $W=0{,}2059$" | ghi dữ kiện bằng cùng bảng với Ví dụ 11.16 ($W$: $2{,}7729$; $1{,}1875$; $1{,}0428$; $0{,}2059$), như deck `L11-3-11` (NT-RL-5 đòi dữ kiện bài tập cùng khuôn với ví dụ dẫn nhập; deck tự tính $W=N\bar Q$ từ số của Ví dụ 11.16) |

Đề xuất hàng đầu đến từ vòng rà deck (III.4, quyết định D-5); ba đề xuất sau có từ khi lập storyboard. Không phát hiện sai số liệu: mọi số lên mặt trang đã tính lại bằng Python (chỉ số UCT với $\ln8$, $\ln9$; $\exp(-70\Delta^2)=0{,}0496$; $\sqrt{0{,}099}=0{,}3146$; $\rho$, $\rho^2$, $\rho^3$; Bài tập 11.7, 11.10; $\gamma^{20}=0{,}1216$; $20\sqrt2=28{,}28$; Ví dụ 11.27), khớp ghi chú.

## 12. Câu hỏi cho điều phối viên và quyết định (2026-11-19)

| Mã | Câu hỏi | Quyết định của điều phối viên (sau cổng) |
|---|---|---|
| C1 | 58, 59 hay 60 trang | Giữ 60 (trần P6), lý do ở mục 3; rút mật độ không thêm trang |
| C2 | Danh sách ngoại lệ mật độ | Không chấp nhận danh sách cũ; rút theo bảng đề xuất của cổng (mục 4) |
| C3 | Tên mạch | Theo tên mục ghi chú, khớp `exercises.md`; trang "Nội dung" được phép rút gọn có lý do, nhưng bản này giữ tên đầy đủ (dòng dài nhất 11 âm tiết, vừa một dòng; NT11 đòi trùng tên trang tiêu đề mạch) |
| C4 | Câu chữ đề Bài tập 11.10 | Giữ nguyên câu chữ; câu (e) sang `L11-6-05` |
| C5 | Dòng nối sang bài sau | Không có (Q8) |
| C6 | Bản `-slide.svg` | Người viết deck vẽ bằng script trong `/data/tqlong/lectures/tools/courses/rl-plan/2627-1/img/lec-11/` (năm hình, mục 6) |
| C7 | Lớp CSS hai cột | Dùng `.grid2`, `.grid3`, `.grid2.wide-right` có sẵn trong `lecture-course.css` |

Không còn câu hỏi mở cho giai đoạn viết deck.

## 13. Sửa theo cổng (2026-11-19)

Báo cáo cổng: scratchpad `lec11/cong-storyboard.md` (nghiêm trọng 3, trung bình 9, nhẹ 10); điều phối viên quyết định áp mọi phát hiện theo đề xuất. Bản trước cổng lưu ở scratchpad `lec11/storyboard-v1.md`. Thay đổi (chuỗi mặt trang sửa bằng `no-ai-slop` Edit):

- **Nghiêm trọng.** `L11-2-10`: Mệnh đề 11.15(b) đủ giả thiết của ghi chú (phần thưởng $0$; $b$ kế đồng khả năng; giá trị kế cố định, độc lập, cùng kỳ vọng, phương sai $1$; $k$ mẫu độc lập; $\alpha_j=1/j$); hai cập nhật thành bảng hai hàng; hàng 11.15(b) của `L11-6-01` cùng giả thiết. `L11-3-10`: "Lưu ý: (a) không có chứng minh cho Thuật toán 11.26; …"; $v^D_*$ định nghĩa trong dòng giả thiết; "khi số vòng lặp $\to\infty$". Trang hai cột: `L11-2-08` (59, gộp (a)–(c), lý do của "Lưu ý:" sang ghi chú diễn giả), `L11-4-06` (56, "Ở ví dụ …" và "Chứng minh." sang ghi chú diễn giả), `L11-4-07` (bảng toàn bề rộng, bỏ hình).
- **Trung bình.** Mật độ rút theo bảng của cổng (mục 4; 25 ngoại lệ còn lại, mỗi trang có lý do NT17 và số trước/sau). "Trực quan." trên mặt trang của Mệnh đề 11.21 (`L11-3-03`), Định lý 11.42 (`L11-5-05`), Dyna-Q (`L11-2-07`), cập nhật kỳ vọng và mẫu (`L11-2-10`). Dyna-Q mở bằng giới hạn của Q-planning (NT-RL-3). Mục tiêu 1 và 4 có đủ động từ ("ước lượng mô hình bằng tần suất", "cùng giả thiết", "bốn pha"). Luận điểm bìa theo câu cuối Tóm tắt chương. Dòng dẫn mạch 6: "Các bảo đảm của lập kế hoạch đúng trên mô hình; sai số của mô hình chỉ được chặn ở hai chỗ." Nhãn "Giả thiết:" cho Định lý 11.24 (`L11-3-06`, "quy tắc UCB1" thay cho đồng nhất với (3.2)) và Định lý 11.44 (`L11-5-07`). Định nghĩa 11.25 chuyển sang `L11-3-07` (thêm $\bar Q=W/N$, $N(s)=\sum_aN(s,a)$, tên tiếng Anh của UCT); `L11-3-09` chỉ còn Thuật toán 11.26. Đề Bài tập 11.10 giữ nguyên câu chữ; câu (e) sang `L11-6-05`.
- **Nhẹ.** Hàng 11.42/11.44 của bảng tổng kết: cột giả thiết thêm "mô hình tùy chọn đúng", "$\Omega(s)$ hữu hạn", kết luận $v_\Omega\le v_*$ sang cột ba. Mục 1 dẫn đúng `L11-6-03`. `L11-2-01`: nhãn "Định nghĩa 11.1." đứng trước ba vế, có "trên các cặp (trạng thái kế, phần thưởng)" và "độc lập giữa các lần gọi". Câu nối `L11-2-12` chỉ giữ giới hạn (không lặp "dồn phép tính" với `L11-3-00`, `L11-3-01`). `L11-3-08`: dòng AlphaGo Zero bản 19 âm tiết, ghi chú diễn giả nói "đọc thêm". `L11-4-04`: bỏ số hiệu Thuật toán 11.34 khỏi mặt trang. `L11-4-02`: "tốc độ học $\eta=0{,}1$". Bảy dòng: chú thích bảng vào hàng tiêu đề (`L11-2-07`, `L11-3-07`), "Chứng minh." của `L11-4-03` sang ghi chú diễn giả. "Tính …"/"Diễn giải:" ở `L11-2-07`, `L11-3-07`, `L11-5-03`. `L11-2-05`: tiêu đề cột "Lời giải", nhãn "Lời giải:" ở fragment đầu. `p.strand-keys` của mạch 3 không có "UCT" ("thuật toán rollout · số mô phỏng · cận tin cậy trên · chính sách cây"). `L11-5-08`: dòng "Lưu ý:" nêu chỗ sai, bỏ "một nhầm lẫn thường gặp".
- **Thêm ngoài báo cáo để đạt trần:** `L11-2-02` (62, trước 71), `L11-5-06` (75, trước 84; giả thiết ở từng bước giữ nguyên), `L11-6-06` (75, trước 79), `L11-2-04`, `L11-3-01`, `L11-3-05`, `L11-5-01` về ≤ 60.
- **Số trang, thời lượng:** không đổi, 60 trang (7 + 13 + 12 + 9 + 10 + 9), 120 phút; mọi `data-slide-id` giữ nguyên.
- **Kiểm lại của cổng (2026-11-19; trung bình 1, nhẹ 5).** `L11-2-06`: "Bảo đảm: $Q\to\hat q_*$, giá trị hành động tối ưu trên mô hình, hầu chắc chắn (Mệnh đề 11.9)." (79 âm tiết sau khi rút "cả" ở dòng 1 và "thỏa" ở dòng giả thiết; dưới trần thuật toán 80). `L11-1-03`: mục tiêu 1 thêm đối tượng ("độ lệch chuẩn ước lượng"), mục tiêu 4 thêm "một vòng", "Monte Carlo"; bù bằng "mô hình phân phối và mẫu", "dưới hệ số phân nhánh", "cho xác suất chọn sai", "độ lệch chuẩn ước lượng" (thuật ngữ của Bài tập 11.10), "điều kiện để Q-planning hội tụ" (120 âm tiết, ≤ 120). `L11-2-07`, `L11-3-07`: nhãn "Trực quan." đứng đầu dòng riêng; `L11-2-07` giữ 6 dòng bằng câu kết "Diễn giải:" dưới bảng, `L11-3-07` thành 7 dòng (ngoại lệ có lý do ở mục 4). `L11-3-06`: "quy tắc UCB1, biến thể của (3.2) với $c_{\mathrm{ucb}}=\sqrt2$" (85 âm tiết). `L11-3-07`: "cạnh có $N(s,a)=0$ được chọn trước" thay "cạnh chưa đi trước". `L11-6-05`: (c) gộp vào cuối (b), còn 6 dòng.

## 14. Đồng bộ sau biên tập (2026-11-19)

Deck cuối `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` (60 trang, cùng 60 `data-slide-id`, cùng thứ tự, cùng sáu mạch, 120 phút) sau năm vai rà (III.4) và biên tập hai vòng (III.5). Nguồn đồng bộ: `lec11/bang-phat-hien-III5.md` (quyết định D-1 … D-12), `lec11/nhat-ky-sua-III5.md` (nhật ký sửa), `lec11/mat-do-cuoi.md` (số đo cuối), trong scratchpad của phiên. Bản storyboard trước lượt đồng bộ lưu ở `lec11/storyboard-v3-truoc-dong-bo.md`. Khi mục 7 và deck khác nhau, deck và dòng "Sau biên tập" của từng trang là bản hiện hành; mục 7 giữ lý do tồn tại, liên kết, nguồn của từng trang.

- **Đã cập nhật trong tệp này:** mục 2 (dòng dẫn mạch 4, 5, 6); mục 4 (bảng ngoại lệ theo số đo cuối, số storyboard và số cuối); mục 7 (mỗi trang thêm "Số đo cuối"; trang có mặt trang đổi thêm "Sau biên tập (2026-11-19)", tóm tắt thay đổi, không chép HTML); mục 9 (35 `SYLL60` đã biết, D-11, kết quả kiểm); mục 11 (đề xuất NT3 về ô §6.1 hàng Dyna-Q).
- **Quyết định của điều phối viên áp vào deck** (tóm tắt, chi tiết ở các trang): D-1 chặn $0{,}0496$ chỉ cho cặp $(\rightarrow,\downarrow)$, bốn hành động cần $m=75$; D-2 phạm vi 11.27(a) trên `L11-6-01`, `L11-3-10`; D-3 số hiệu công thức trong câu dẫn ở trang công thức xuất hiện lần đầu ((3.2) `L11-3-06`; (4.1) `L11-4-02`; (4.2), (4.3) `L11-4-03`; (5.1) `L11-5-04`; (5.2) `L11-5-05`; (5.3) `L11-5-08`); D-4 cột "Kết quả" giữ số hiệu, tên ở ghi chú diễn giả; D-5 ghi chú diễn giả `L11-6-01`, `L11-6-02`, đề xuất NT3 cho ghi chú; D-6 mật độ; D-7 "Trực quan." ở `L11-2-01`, `L11-2-03`, `L11-3-06`, `L11-3-10`; D-8 ký hiệu, dữ kiện, phân loại NT-RL-4, tên MCTS; D-9 bốn pha, lời giải `L11-3-11`, nhãn `L11-5-04`, VP19 trong ghi chú diễn giả; D-10 trang tài liệu tham khảo; D-11 không sửa nhãn hình ở 390 × 844; D-12 các phát hiện nhẹ còn lại.
- **Khác storyboard trước đồng bộ, có lý do của biên tập viên:** `L11-4-07` vẫn bảng toàn bề rộng; `L11-2-01` 89 (storyboard 84) vì thêm dòng "Trực quan."; `L11-6-02` 97/80 vì phân loại nền/thời điểm quyết định và điều kiện dừng đúng Thuật toán 11.33; `L11-6-08` 86/80 vì nguồn có mục (D-10); `L11-1-02` 75 vì ký hiệu $\mathcal S^+$, $v_*$, $q_*$; dòng dẫn mạch 4, 5, 6 đổi theo vai rà; `L11-1-03` chữ của mục tiêu 1, 3, 4 lấy lại từ ghi chú (119/80).
- **Câu hỏi C8 cho điều phối viên.** Trên `L11-6-01`, để bảng vừa khung, ô giả thiết của 11.9 còn "mô hình cố định, xác định ở mọi cặp" (thiếu "mọi cặp vô hạn lần; Robbins–Monro") và của 11.15(b) còn "$b$ kế đồng khả năng, cùng kỳ vọng" (thiếu "phần thưởng $0$; giá trị kế cố định, độc lập, phương sai $1$; $k$ mẫu độc lập, $\alpha_j=1/j$"). Cổng storyboard xếp việc thiếu giả thiết của 11.15(b) ở hàng này là nghiêm trọng (NT2, NT15). Đề xuất: điều phối viên xác nhận cách rút này (giả thiết đầy đủ ở trang phát biểu `L11-2-06`, `L11-2-10`) hoặc giao biên tập viên chuyển bảng sang lớp `.compact` hai dòng mỗi ô cho hai hàng đó.
