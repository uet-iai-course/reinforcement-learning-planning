# Dàn ý triển khai — Bài 03: Quá trình quyết định Markov

Bản này thay dàn ý trước đợt sửa 2026-10-12. Deck `2627-1/lecture-03-qua-trinh-quyet-dinh-markov.html` có 7 mạch, 72 trang (6 trang tiêu đề mạch; cập nhật sau vòng biên tập năm vai rà soát 2026-10-12), phủ 120 phút; 30 phút còn lại dùng chữa bài tập. Deck là bản tóm tắt của ghi chú bài giảng đã commit (`ceab04c`): số liệu, ký hiệu, thứ tự khái niệm, tên ví dụ xuyên suốt và số hiệu kết quả lấy theo ghi chú.

## 1. Đối tượng và mục tiêu học tập

Sinh viên năm 3 đã học xác suất, kỳ vọng có điều kiện, đại số tuyến tính và Bài 02. Bài 02 đã phát biểu hình thức tính Markov, hàm động lực, lợi tức với hệ thức truy hồi và cận $\lvert G_t\rvert\le R_{\max}/(1-\gamma)$, và $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ (ghi chú Bài 02, Mục 2–4); deck nhắc lại các kết quả này ở `01-01b`, và trang vấn đề của mạch 2–4 mở bằng "Nhắc lại:" rồi "Nhu cầu:". Phần mới của Bài 03: điều kiện xác suất dương, quy tắc sinh quỹ đạo của MDP hữu hạn, mô hình robot, quy ước hấp thụ, $v_\pi$ trên quá trình xuất phát tại $s$, $q_\pi$, phương trình Bellman và cách giải. Mục tiêu (trang `L03R-01-01c`, khớp mục Mục tiêu học tập của ghi chú):

1. Kiểm tra tính Markov; lập bộ MDP hữu hạn và bảng $p(s',r\mid s,a)$ (Bài tập 03.1, 03.2).
2. Tính lợi tức chiết khấu và cận $M/(1-\gamma)$ (Bài tập 03.3, 03.10, 03.12).
3. Phân biệt mô hình, chính sách, $v_\pi$, $q_\pi$; tính kỳ vọng trên cây hai bước (Bài tập 03.4, 03.5).
4. Chứng minh phương trình Bellman kỳ vọng cho $v_\pi$, $q_\pi$; chỉ ra bước dùng tính Markov và tính dừng (Bài tập 03.6, 03.7, 03.11).
5. Lập, giải, kiểm tra hệ $(I-\gamma P^\pi)v=r^\pi$ (Bài tập 03.8, 03.9, 03.13, 03.14).

Số hiệu trong danh sách trên là của ghi chú. Bài của `materials/lec-03/exercises.md` theo mục tiêu (dòng "Mức độ" của từng bài; ghi chú diễn giả `01-01c`): mục tiêu 1: 03.1, 03.2, 03.15, 03.22, 03.24; mục tiêu 2: 03.3, 03.18, 03.20, 03.23; mục tiêu 3: 03.4, 03.5, 03.16, 03.17; mục tiêu 4: 03.6, 03.7, 03.17, 03.19, 03.24, 03.25; mục tiêu 5: 03.8, 03.20, 03.21, 03.23, 03.24, 03.25.

## 2. Khung lý thuyết chung

- **Bài toán trung tâm.** Tính giá trị dài hạn của một chính sách khi phản hồi của môi trường là ngẫu nhiên (bài toán dự đoán, có mô hình).
- **Đối tượng và ký hiệu chung.** MDP hữu hạn $\mathcal M=(\mathcal S^+,\{\mathcal A(s)\},\mathcal R,p)$; hệ số chiết khấu $\gamma$ đứng ngoài $\mathcal M$; lợi tức $G_t$; chính sách Markov dừng $\pi(a\mid s)$; $\Pr_\pi$, $\mathbb E_\pi$; $v_\pi$, $q_\pi$ (chữ thường, theo Sutton và Barto); $P^\pi$, $r^\pi$, véc-tơ $v$.
- **Giả thiết.** Trạng thái có tính Markov; $p$ và $\pi$ không đổi theo thời gian; các tập hữu hạn; phần thưởng bị chặn; $0\le\gamma<1$ (nhiệm vụ có kết thúc với $\gamma=1$ chỉ nêu ở phạm vi, không chứng minh).
- **Chuỗi định nghĩa → kết quả → phương pháp.** Tính Markov (Định nghĩa 03.2) → hàm động lực (Định nghĩa 03.4), MDP hữu hạn (Định nghĩa 03.7) → lợi tức (Định nghĩa 03.9), cận (Mệnh đề 03.11) → chính sách (Định nghĩa 03.13), $v_\pi$, $q_\pi$ (Định nghĩa 03.15, 03.16) → hệ thức đệ quy, hai tầng kỳ vọng, tính Markov của phần tương lai (Bổ đề 03.18–03.20) → Bellman cho $v_\pi$ (Định lý 03.21), quan hệ $v$–$q$ (Mệnh đề 03.22, 03.23), Bellman cho $q_\pi$ (Hệ quả 03.24) → MRP cảm sinh (Định nghĩa 03.26), dạng ma trận (Mệnh đề 03.27), nghiệm duy nhất (Định lý 03.28) → Thuật toán 03.29.
- **Giới hạn.** Cần biết $p$ (Bài 05–06 bỏ giả thiết này); chi phí giải trực tiếp cỡ $n^3$ (Bài 04 dùng phép lặp); đánh giá một chính sách chưa cho cách chọn chính sách tốt hơn (Bài 04); trạng thái phải có tính Markov (Tình huống 03.2, CartPole rời rạc hóa; Bài 07).

## 3. Bản đồ mạch

| N | Mạch | Trang tiêu đề | Đầu vào | Đầu ra cho mạch sau | Trang | Phút |
|---|---|---|---|---|---:|---:|
| 1 | Mở đầu | `L03R-01-01` (bìa) | Bài 02 (kết quả kế thừa nhắc lại ở `01-01b`) | Vấn đề trung tâm và năm câu trả lời có điều kiện | 6 | 9 |
| 2 | Trạng thái Markov và mô hình môi trường | `L03R-02-00` | Vòng tương tác, tính Markov, hàm động lực của Bài 02 | Bộ MDP hữu hạn của robot, bảng $p$, $p(s'\mid s,a)$, $r(s,a)$ | 15 | 26,5 |
| 3 | Lợi tức chiết khấu | `L03R-03-00` | Một bước được mô tả bằng $p$; lợi tức của Bài 02 | $G_t$, quy ước hấp thụ, cận $M/(1-\gamma)$ | 7 | 12 |
| 4 | Chính sách và hàm giá trị | `L03R-04-00` | $p$, $G_t$, $v_\pi$ của Bài 02 | $\pi$, xác suất đoạn quỹ đạo, $v_\pi$, $q_\pi$ | 10 | 14 (+3 khối 30 phút) |
| 5 | Phương trình Bellman kỳ vọng | `L03R-05-00` | Định nghĩa $v_\pi$, $q_\pi$ | Hệ Bellman cho $v_\pi$, $q_\pi$, quan hệ $v$–$q$ | 12 | 22,5 (+2 khối 30 phút) |
| 6 | Đánh giá chính sách bằng hệ tuyến tính | `L03R-06-00` | Hệ Bellman | $v_\pi=(13/4,\,7/4)$, MRP, dạng ma trận, nghiệm duy nhất, Thuật toán 03.29 | 14 | 25,5 |
| 7 | Tổng kết và chuyển tiếp | `L03R-07-00` | Mọi kết quả | Bảng giả thiết, bài tập tổng hợp, kết luận song song với vấn đề trung tâm, bốn giới hạn, Bài 04 | 8 | 10,5 |
| | **Tổng** | | | | **72** | **120** |

`id="mach-N"` đặt trên trang tiêu đề mạch N; số trên mặt trang trùng số trên trang "Nội dung" và chỉ số ngang của RevealJS.

## 4. Nguồn

| Nội dung | Nguồn | Trang deck |
|---|---|---|
| Một bước, quỹ đạo, $R_{t+1}$ | Sutton và Barto (2018), (3.1), tr. 48 | `01-04` |
| Tính Markov | Sutton và Barto (2018), §3.1, tr. 49; Bài giảng gốc (2025–2026), trang 29 | `01-05`, `01-06` |
| Robot thu gom lon | Sutton và Barto (2018), ví dụ 3.3, tr. 52–53 | xuyên suốt |
| Hàm động lực, chuẩn hóa | Sutton và Barto (2018), (3.2)–(3.3), tr. 48–49 | `02-04` |
| Xác suất chuyển, thưởng kỳ vọng | Sutton và Barto (2018), (3.4)–(3.5), tr. 49 | `02-05` |
| MDP hữu hạn | Sutton và Barto (2018), §3.1, tr. 47–49; Bài giảng gốc (2025–2026), trang 49 | `02-06` |
| Lượt, lợi tức, trạng thái hấp thụ | Sutton và Barto (2018), §3.3–3.4, tr. 54–57; Bài giảng gốc (2025–2026), trang 36–38 | `03-02`–`03-05` |
| Chính sách, $v_\pi$, $q_\pi$ | Sutton và Barto (2018), §3.5, (3.12)–(3.13), tr. 58; Bài giảng gốc (2025–2026), trang 39, 52–53 | mạch 4 |
| Bellman cho $v_\pi$ | Sutton và Barto (2018), (3.14), tr. 59; Bài giảng gốc (2025–2026), trang 44–46, 56–57 | `05-06b` |
| Quan hệ $v$–$q$, Bellman cho $q_\pi$ | Sutton và Barto (2018), bài tập 3.12–3.13 (tr. 58), 3.17 (tr. 61), 3.18–3.19 (tr. 62) | `05-07`–`05-09` |
| Chuỗi Markov, MRP | Bài giảng gốc (2025–2026), trang 30, 34; Bài tập tuần 2 (2025–2026), bài 4 | `06-05`, `06-06` |
| Dạng ma trận, nghiệm duy nhất, giải hệ | Puterman (1994), §6.1; Sutton và Barto (2018), §4.1, tr. 74; Bài giảng gốc (2025–2026), trang 47–48 | `06-07`–`06-07d` |
| Lưới 5×5 | Sutton và Barto (2018), ví dụ 3.5 và hình 3.2, tr. 60 | `06-07e` |

Các mức thưởng của robot và các chính sách cụ thể là số liệu sư phạm tự xây dựng (ghi trong ghi chú diễn giả).

## 5. Đặc tả ví dụ xuyên suốt

**Robot thu gom lon hai mức pin** (Ví dụ 03.1 của ghi chú). Trạng thái $\mathrm H$ (pin cao), $\mathrm L$ (pin thấp); $\mathcal A(\mathrm H)=\{\mathrm{tim},\mathrm{cho}\}$, $\mathcal A(\mathrm L)=\{\mathrm{tim},\mathrm{cho},\mathrm{sac}\}$; $\mathcal R=\{-3,0,1,2\}$; nhiệm vụ tiếp diễn; phần thưởng cố định trên mỗi nhánh.

| $s$ | $a$ | $s'$ | $r$ | $p(s',r\mid s,a)$ |
|---|---|---|---:|---:|
| H | tim | H | 2 | 1/2 |
| H | tim | L | 2 | 1/2 |
| H | cho | H | 1 | 1 |
| L | tim | L | 2 | 1/2 |
| L | tim | H | −3 | 1/2 |
| L | cho | L | 1 | 1 |
| L | sac | H | 0 | 1 |

- **Chính sách chia đều tại pin thấp:** ở H luôn Tìm; ở L Chờ hoặc Sạc, mỗi hành động 1/2; $\gamma=1/2$. Kết quả: kỳ vọng hai bước từ H là $21/8$, từ L là $9/8$; $v_\pi=(13/4,\,7/4)$; $q_\pi(\mathrm L,\cdot)=(3/4,\,15/8,\,13/8)$; $q_\pi(\mathrm H,\mathrm{tim})=13/4$, $q_\pi(\mathrm H,\mathrm{cho})=21/8$; $P^\pi$ có hai hàng $(1/2,\,1/2)$, $r^\pi=(2,\,1/2)$; $(I-\gamma P^\pi)^{-1}$ có hàng $(3/2,\,1/2)$, $(1/2,\,3/2)$.
- **Chính sách luôn Chờ tại pin thấp:** $v=(10/3,\,2)$.
- **Robot với rủi ro cứu hộ thấp hơn** (Tìm từ L: $(\mathrm L,2)$ xác suất 3/4, $(\mathrm H,-3)$ xác suất 1/4): $v_\pi$ không đổi; $r(\mathrm L,\mathrm{tim})=3/4$; $q_\pi(\mathrm L,\mathrm{tim})=29/16$.
- **Trạng thái thiếu phòng làm việc** (Ví dụ 03.4, phản ví dụ, số liệu sư phạm tự xây dựng).
- **Lưới 5×5** (Tình huống 03.1): chính sách chọn đều, $\gamma=0{,}9$, $v_\pi(\mathrm A)\approx8{,}789$, $v_\pi(\mathrm B)\approx5{,}322$.

Mọi số trên được tính lại bằng `fractions` của Python trong đợt này.

## 6. Thứ tự đưa ký hiệu vào deck

| Ký hiệu | Lần đầu | Có trước |
|---|---|---|
| $R_{t+1}$, $G_t$, $\gamma$, $M$, $p$, $\pi$, $v_\pi$, $\mathbb E_\pi$ (nhắc lại) | `01-01b` | Bài 02 |
| $t$, $\mathcal S$, $\mathcal S^+$, $\mathcal A(s)$, $\mathcal R$, $\Pr_\pi$, $\mathbb E_\pi$, quy ước chữ hoa, $\mathrm H$, $\mathrm L$, $\mathrm{tim},\mathrm{cho},\mathrm{sac}$ | `01-01d` | Bài 02 |
| $(S_t,A_t,R_{t+1},S_{t+1})$, quỹ đạo, $H_t$ | `01-04` | Một bước của robot |
| Tính Markov | `01-06` | Hai lịch sử ở `01-05` |
| $p(s',r\mid s,a)$ | `02-04` | Bảng phản hồi `02-03` |
| $p(s'\mid s,a)$, $r(s,a)$ | `02-05` | Phép tính trên cặp $(\mathrm L,\mathrm{tim})$ |
| $\mathcal M$ | `02-06` | Bốn thành phần đã có |
| $T$, lượt | `03-02` | Hai dãy phần thưởng `03-01` |
| $\gamma$, $G_t$ (định nghĩa với quy ước hấp thụ) | `03-04` | Nhắc lại ở `01-01b`, `03-01` |
| $M$ | `01-01b` (nhắc lại), `03-05` | Bài 02 viết $R_{\max}$ |
| $\pi(a\mid s)$ (định nghĩa chính sách Markov dừng) | `04-03` | Bảng chính sách `04-02` |
| $G_0^{[2]}$ | `04-04` | Cây hai bước |
| $v_\pi$ | `04-05` | Cây hai bước kéo dài |
| $q_\pi$ | `04-07` | Ba thí nghiệm `04-06` |
| $v_H$, $v_L$ | `05-10b` | Viết tắt của $v_\pi(\mathrm H)$, $v_\pi(\mathrm L)$ |
| $P^\pi$, $r^\pi$, chuỗi Markov, MRP | `06-06` | Bảng gộp nhánh `06-05` |
| $v\in\mathbb R^n$, $I$, $\lVert\cdot\rVert_\infty$ | `06-07`, `06-07b` | Hệ hai phương trình đã giải |
| $\delta$, $\rho$ | `06-07c`, `06-07d` | Thuật toán |

## 7. Bảng thuật ngữ Việt–Anh của bài

| Tiếng Việt | Tiếng Anh | Lần đầu trên deck |
|---|---|---|
| quá trình quyết định Markov | Markov decision process (MDP) | `01-01` |
| chính sách | policy | ghi chú Bài 02 (deck chỉ ghi "stationary policy" ở `01-01b`) |
| chính sách dừng, chính sách Markov dừng | stationary policy | `01-01b` |
| chính sách xác định | deterministic policy | ghi chú diễn giả `04-03` (dạng chốt của học phần) |
| phần thưởng | reward | `01-01b` |
| mô hình | model | `01-01c`; `02-06` "Mô hình của môi trường là $p$" |
| lợi tức | return | `01-01b` |
| phương trình Bellman kỳ vọng | Bellman expectation equation | `01-01c` |
| tác tử | agent | `01-01b` |
| quỹ đạo | trajectory | `01-03` |
| lịch sử | history | `01-04` |
| tính Markov | Markov property | `01-01b` |
| hàm động lực | dynamics function | `01-01b` |
| xác suất chuyển trạng thái | state-transition probability | `02-05` |
| thưởng kỳ vọng | expected reward | `02-05` |
| nhiệm vụ có kết thúc | episodic task | `03-02` |
| lượt | episode | `03-02` |
| trạng thái kết thúc | terminal state | `03-02` |
| nhiệm vụ tiếp diễn | continuing task | `03-02` |
| hệ số chiết khấu | discount factor | `01-01b` |
| cận thị | myopic | ghi chú diễn giả `03-06b` |
| giá trị trạng thái | state-value function | `01-01b` |
| giá trị hành động | action-value function | `04-07` |
| sơ đồ cập nhật | backup diagram | ghi chú diễn giả `05-09` (thống nhất với Bài 04; ghi chú bài giảng đã khớp 2026-10-14) |
| mục tiêu bootstrap | bootstrap target | ghi chú diễn giả `05-09` |
| đánh giá chính sách, còn gọi là bài toán dự đoán | policy evaluation; prediction | `06-01` |
| chuỗi Markov | Markov chain | `06-06` |
| quá trình phần thưởng Markov | Markov reward process (MRP) | `06-06` |
| chuỗi Neumann | Neumann series | ghi chú diễn giả `06-07b` |

Thuật ngữ thống nhất với `planning/quyet-dinh-chuan-2026-10-12.md` mục 1 (lợi tức, lượt, tác tử, quá trình quyết định Markov).

## 8. Danh sách trang

| Mạch | Trang (`data-slide-id`: tiêu đề) |
|---|---|
| 1 | `L03R-01-01` bìa; `01-01b`, `01-01d` Tiên quyết và quy ước; `01-01c` Mục tiêu học tập; `01-02` Nội dung; `01-02b` Vấn đề trung tâm |
| 2 | `02-00` tiêu đề mạch; `01-03` Lựa chọn của robot ở pin thấp; `01-04` Quỹ đạo và lịch sử; `01-05` Hai lịch sử, cùng trạng thái hiện tại; `01-06` Tính Markov; `01-06b` Ví dụ: trạng thái thiếu phòng làm việc; `01-07`, `01-07b` Bài tập: trạng thái của robot; `02-02` Ví dụ: hai phản hồi của hành động Tìm; `02-03` Ví dụ: bảng phản hồi của robot; `02-04` Hàm động lực; `02-05` Xác suất chuyển và thưởng kỳ vọng; `02-06` Quá trình quyết định Markov hữu hạn; `02-07`, `02-07b` Bài tập: đọc hàm động lực của robot |
| 3 | `03-00` tiêu đề mạch; `03-01` Lợi tức của robot; `03-02` Lượt và hai loại nhiệm vụ; `03-04` Lợi tức chiết khấu; `03-05` Cận của lợi tức; `03-06`, `03-06b` Bài tập: lợi tức và cận của robot |
| 4 | `04-00` tiêu đề mạch; `04-02` Ví dụ: chính sách chia đều tại pin thấp; `04-03` Chính sách Markov dừng; `04-03b` Xác suất của một đoạn quỹ đạo; `04-04` Ví dụ: kỳ vọng hai bước từ pin cao; `04-05` Giá trị trạng thái; `04-06` Ví dụ: ba thí nghiệm từ pin thấp; `04-07` Giá trị hành động; `04-08`, `04-08b` Bài tập: mô hình, chính sách và giá trị |
| 5 | `05-00` tiêu đề mạch; `05-01` Nhóm quỹ đạo theo bước đầu; `05-02` Ví dụ: phương trình một bước tại pin thấp; `05-03` Hệ thức đệ quy của lợi tức; `05-04` Hai tầng kỳ vọng; `05-06` Tính Markov của phần tương lai; `05-06b` Phương trình Bellman kỳ vọng cho giá trị trạng thái; `05-07` Giá trị hành động theo giá trị trạng thái; `05-08` Giá trị trạng thái theo giá trị hành động; `05-09` Phương trình Bellman kỳ vọng cho giá trị hành động; `05-10` Bài tập: chỗ dùng tính Markov; `05-10b` Bài tập: phương trình Bellman tại pin cao |
| 6 | `06-00` tiêu đề mạch; `06-01` Bài toán đánh giá chính sách; `06-02` Ví dụ: hệ Bellman của robot; `06-03` Ví dụ: hệ Bellman của robot, lời giải; `06-04` Ví dụ: kiểm tra nghiệm bằng giá trị hành động; `06-05` Ví dụ: gộp các nhánh của robot; `06-06` Chuỗi Markov và quá trình phần thưởng Markov cảm sinh; `06-07` Phương trình Bellman dạng ma trận; `06-07b` Nghiệm duy nhất của hệ đánh giá chính sách; `06-07c`, `06-07d` Đánh giá chính sách bằng giải hệ tuyến tính; `06-07e` Ví dụ: lưới 5×5; `06-08`, `06-08b` Bài tập: đánh giá chính sách luôn Chờ tại pin thấp |
| 7 | `07-00` tiêu đề mạch; `07-01a`, `07-01b` Tổng kết; `07-01`, `07-02` Bài tập: robot với rủi ro cứu hộ thấp hơn; `07-02b` Kết luận về vấn đề trung tâm; `07-04` Câu hỏi tự kiểm tra; `07-03` Bài tập về nhà và tài liệu đọc |

Mọi mã đầy đủ có tiền tố `L03R-`.

## 9. Liên kết với ghi chú bài giảng

| Mạch | Mục ghi chú | `note-topic-id` |
|---|---|---|
| 1 | Mục tiêu, Kiến thức tiên quyết, Bảng ký hiệu | `lec-03-part-09` |
| 2 | Mục 1 | `lec-03-part-01`, `lec-03-part-02` |
| 3 | Mục 2 | `lec-03-part-03` |
| 4 | Mục 3 | `lec-03-part-04` |
| 5 | Mục 4 | `lec-03-part-05` |
| 6 | Mục 5; Tình huống 03.1 | `lec-03-part-06`, `lec-03-part-07` |
| 7 | Tóm tắt chương, Bài tập củng cố, Hướng dẫn đọc thêm | `lec-03-part-08`, `lec-03-part-10` |

Tệp bài tập `materials/lec-03/exercises.md` (mười chín bài: 03.1–03.8, 03.15–03.25) xếp bài theo mạch; trang `07-03` chép đúng bảng đó, thêm cột "Chỉ trong ghi chú" (03.9–03.14) và liên kết viewer của tệp.

Không có bài thực hành riêng (quyết định chung, mục 8); Tình huống 03.2 về CartPole dẫn sang notebook của Bài 04 và chỉ được nhắc trong ghi chú diễn giả.
