# Bài 11 — Lập kế hoạch dựa trên mô hình: kế hoạch ghi chú bài giảng

> **Mục đích.** Kế hoạch soạn `materials/lec-11/lecture-note.md` mới cho Bài 11 theo Chương 11 "Lập kế hoạch dựa trên mô hình" của giáo trình *Học tăng cường và lập kế hoạch* (Tạ Việt Cường – Trần Quốc Long). Tệp planning nội bộ, không công khai, không liên kết từ `index.html`.
>
> **Ngày:** 2026-11-19. **Trạng thái:** kế hoạch, chưa duyệt (chờ điều phối viên và tác giả quyết các điểm QG ở mục 17).
>
> **Đầu vào đã đọc.** `NGUYEN-TAC-HOC-PHAN.md` (GC-RL-1…17, BT-RL-1…9, mục 3, mục 5, mục 6, mục 7); `NGUYEN-TAC-GHI-CHU.md` (GC1–GC26); `NGUYEN-TAC-BAI-TAP.md` (BT1–BT13); `NGUYEN-TAC-TRANG-CHIEU.md` (NT1–NT28); `NGUYEN-TAC-VAN-PHONG.md` (VP1–VP24); `AGENTS.md` mục "Tham số trang chiếu của học phần", "Tiêu chuẩn nội dung Học tăng cường", "Cấu trúc bắt buộc của một chương", "Mẫu trình bày một khái niệm"; `CLAUDE.md` của học phần; mẫu `materials/_templates/{lecture-note,exercises}.md`; mục lục giáo trình `giao-trinh/muc-luc-giao-trinh-hoc-tang-cuong-2026.pdf` (trang PDF 3–15); phần đầu và danh sách khối của ghi chú 01, 03, 04, 05, 06, 08, 10; Sutton và Barto (2018), bản trích `/data/tqlong/qa/sources/sutton-barto-rl2020/extracted.md` (§2.7, Chương 8, §16.6, §17.2, kiểm số trang in bằng trang PDF trừ 22); mẫu kế hoạch `ds-foundation-algorithms/2627-1/planning/lec-11/{outline,storyboard}.md` (chỉ lấy cấu trúc).
>
> **Tệp đi kèm.** `ke-hoach-bai-tap.md` (bài tập), `ke-hoach-trang-chieu.md` (bộ trang chiếu). Ba tệp dùng chung số mục, số mạch, số hiệu khối, hai ví dụ xuyên suốt và các con số ở mục 7 của tệp này. Mã câu hỏi mở: QG… (tệp này), QB… (bài tập), QT… (trang chiếu).
>
> **Đã tính lại.** Mọi con số ở mục 7 được người lập kế hoạch tính tay và chạy lại bằng Python trong scratchpad của phiên (không vào repo). Tác tử soạn và tác tử rà toán vẫn phải tự tính lại (GC26, BT12).

## 0. Tóm tắt quyết định của kế hoạch

- **Nguồn nội dung** (đề xuất ngoại lệ QG1): học phần không có bộ trang chiếu nguồn cho chủ đề này (đã kiểm `RL-hk2-2025-2026/`: `lecture11_part3.pdf` là "Lecture 10: Overview on Policy Gradient Algorithms, Part 2", không có Dyna, MCTS, tùy chọn). Phạm vi và thứ tự lấy từ mục lục Chương 11 của giáo trình tác giả (11.1–11.5); nội dung lấy từ các giáo trình chuẩn của GC-RL-5, chủ yếu Sutton và Barto (2018) Chương 8, §2.7, §16.6, §17.2; Bertsekas (2019) cho rollout và điều khiển dự báo; Szepesvári (2010) cho phát biểu gọn của UCB. Ghi chú đã kiểm định là chuẩn nội dung của deck (NT1–NT3).
- **Sáu mục nội dung = sáu mạch của deck** (GC-RL-1, NT10): §1 mở đầu; §2 ↔ 11.1; §3 ↔ 11.2; §4 ↔ 11.3; §5 ↔ 11.4; §6 "Tổng kết" ↔ 11.5 (GC-RL-15). Phương án bảy mạch (tách 11.1) ghi ở QT2.
- **Hai ví dụ xuyên suốt** gọi bằng tên đối tượng (GC-RL-11): **mê cung hai phòng** (tám ô, trượt với xác suất $0{,}2$, dùng cho mô hình đếm, Dyna-Q, rollout, MCTS, tùy chọn) và **xe trên đường ray** (hệ tuyến tính một chiều, dùng cho tối ưu kế hoạch bằng đạo hàm, điều khiển dự báo, phương pháp entropy chéo, sai số tích lũy). Không có bài thực hành cho Bài 11 (BT-RL-7 chỉ khi người dùng yêu cầu), nên NT-RL-1 và phần "đối chiếu bài thực hành" của GC-RL-8 không áp dụng.
- **Công cụ chưa dạy được phát biểu lại trong bài** (GC3): Chương 4 của giáo trình (tìm kiếm, rollout, điều khiển dự báo, UCB1/UCT ở 4.3 và 4.7) không có bài giảng trong học phần, nên Bài 11 tự trình bày thuật toán rollout (§3.1), quy tắc cận tin cậy trên (§3.2) và điều khiển dự báo theo chân trời lùi (§4.3), phân loại `cầu nối` (mục 12).
- **Bài tập của ghi chú:** chỉ có mục "Bài tập củng cố" cuối chương (đề xuất mở rộng BT-RL-6 cho Bài 11, QG4), mười một bài 11.1–11.11; `exercises.md` tiếp số từ 11.12 (xem `ke-hoach-bai-tap.md`).
- **Độ dài đề xuất:** 15 000–18 000 từ `prose` (GC-RL-4; mục 15).
- **Không có câu trỏ tới Chương 14** (mô hình thế giới, Dreamer, MuZero) hay bài sau trong chữ của sinh viên (VP20); giới hạn đó chỉ nêu trong phần "Phạm vi." của các kết quả bằng nguyên nhân ("mô hình là bảng hoặc hàm tường minh trên trạng thái quan sát được").

## 1. Ánh xạ nguồn: mục ghi chú ↔ mục lục giáo trình ↔ giáo trình chuẩn

Số trang Sutton và Barto (viết tắt **SB**) là trang in, đã kiểm trên bản trích (trang PDF trừ 22): §8.1 bắt đầu ở trang PDF 181 → tr. 159; hộp Dyna-Q ở trang PDF 186 → tr. 164; §17.2 ở trang PDF 483 → tr. 461. Bertsekas (2019), Szepesvári (2010), Puterman (1994) dẫn theo mục (GC-RL-5); **số mục của ba sách này chưa kiểm được trong máy** (không có bản trong `sources/`), ghi "cần kiểm" (QG9).

| Mục ghi chú | Mục lục giáo trình | Nguồn nội dung chính | Nguồn đối chiếu, kiểm chứng (P8) |
|---|---|---|---|
| §1 Bài toán lập kế hoạch với mô hình học được | (mở chương) | SB §8.1 tr. 159–161 (khung "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách"); SB Ví dụ 8.1, Hình 8.2–8.3, tr. 164–165 (mê cung Dyna: khoảng 25 lượt với $n=0$, khoảng 5 lượt với $n=5$, 3 lượt với $n=50$) | Định nghĩa 01.14 (mô hình, lập kế hoạch) |
| §2.1 Mô hình phân phối và mô hình mẫu | 11.1 | SB §8.1 tr. 159–160; SB §8.8 tr. 180–181 (lập kế hoạch nền, lập kế hoạch tại thời điểm quyết định) | — |
| §2.2 Mô hình đếm và hai loại bất định | 11.1 | ước lượng tần suất (Mệnh đề 05.34 đã dùng $\hat r$, $\hat P$); phân phối nhị thức | Chua và cộng sự (2018), mục mô hình động lực có tính bất định (định nghĩa bất định ngẫu nhiên, bất định nhận thức; cần kiểm số mục) |
| §2.3 Tập mô hình (bổ sung) | 11.1 | lấy mẫu lại có hoàn lại | Chua và cộng sự (2018), mục tập mô hình (cần kiểm số mục) |
| §2.4 Q-planning và kiến trúc Dyna | 11.1 | SB §8.1 tr. 161 (hộp Q-planning, điều kiện hội tụ); SB §8.2 tr. 161–166 (Hình 8.1, hộp Dyna-Q tr. 164, Ví dụ 8.1) | Định lý 06.21 |
| §2.5 Mô hình sai và thưởng thăm dò | 11.1 | SB §8.3 tr. 166–168 (Ví dụ 8.2 mê cung bị chặn, Ví dụ 8.3 mê cung có lối tắt, Hình 8.4–8.5 tr. 167; thưởng $\kappa\sqrt\tau$ và chú thích 1, tr. 168) | — |
| §2.6 Cập nhật kỳ vọng và cập nhật mẫu | 11.1 | SB §8.5 tr. 172–174 (hệ số phân nhánh $b$, Hình 8.7 tr. 174, sai số $\sqrt{(b-1)/(bt)}$) | tự chứng minh (mục 8, Mệnh đề 11.15) |
| §2.7 Đọc thêm: phân bổ cập nhật | 11.1 | SB §8.4 tr. 168–172 (quét ưu tiên); §8.6 tr. 174–177 (lấy mẫu theo quỹ đạo, Hình 8.8 tr. 176); §8.7 tr. 177–180 (RTDP, bốn điều kiện hội tụ tr. 178) | Barto, Bradtke và Singh (1995), dẫn qua SB tr. 178 |
| §3.1 Thuật toán rollout | 11.2 (phát biểu lại giáo trình 4.3.1) | SB §8.10 tr. 183–185 | Bertsekas (2019), mục rollout và nguyên lý cải thiện chính sách (cần kiểm: §2.4); Hoeffding (1963, Định lý 2, tr. 16), như Mệnh đề 06.26 |
| §3.2 Chọn hành động theo cận tin cậy trên | 11.2 (phát biểu lại giáo trình 4.7.1–4.7.2) | SB §2.7 tr. 35–36, công thức (2.10), Hình 2.4 | Auer, Cesa-Bianchi và Fischer (2002, Định lý 1) cho chặn hối tiếc của UCB1; Szepesvári (2010, mục bandit trực tuyến, cần kiểm: §4.2.1) |
| §3.3 Bốn pha của MCTS | 11.2 | SB §8.11 tr. 185–188 (Hình 8.10 tr. 186, bốn bước tr. 187) | Kocsis và Szepesvári (2006) cho quy tắc UCT |
| §3.4 Bảo đảm của UCT và giá trị học được | 11.2 | SB §16.6 tr. 441–450 (§16.6.1 AlphaGo tr. 444, §16.6.2 AlphaGo Zero tr. 447) | Kocsis và Szepesvári (2006, định lý tính nhất quán; cần kiểm số định lý và hằng số); Silver và cộng sự (2017, phần Methods, quy tắc chọn có xác suất tiên nghiệm; cần kiểm) |
| §4.1–4.2 Tối ưu kế hoạch, đạo hàm qua mô hình | 11.3 | quy tắc dây chuyền (Goodfellow, Bengio và Courville 2016, §6.5, lan truyền ngược) | Deisenroth và Rasmussen (2011, PILCO) chỉ để kiểm chứng câu "tối ưu chính sách bằng gradient qua mô hình khả vi" |
| §4.3 Điều khiển dự báo theo chân trời lùi | 11.3 (phát biểu lại giáo trình 4.3.2) | Bertsekas (2019), mục điều khiển dự báo (cần kiểm: §2.5) | — |
| §4.4 Phương án không dùng đạo hàm (bổ sung) | 11.3 | bắn ngẫu nhiên (không cần nguồn); phương pháp entropy chéo | Chua và cộng sự (2018), phần tối ưu kế hoạch bằng CEM (cần kiểm số mục); QG3 |
| §4.5 Sai số mô hình tích lũy | 11.3 | tự chứng minh bằng quy nạp (Mệnh đề 11.36) | — |
| §5.1 Tùy chọn | 11.4, 11.4.1 | SB §17.2 tr. 461–462 (tùy chọn $\langle\pi_\omega,\gamma_\omega\rangle$) | Sutton, Precup và Singh (1999, định nghĩa tùy chọn $\langle\mathcal I,\pi,\beta\rangle$; cần kiểm số mục) |
| §5.2 Mô hình tùy chọn và bán-MDP | 11.4.1 | SB §17.2 tr. 462–463, công thức (17.2), (17.3), (17.4) | Sutton, Precup và Singh (1999, định lý "MDP + tùy chọn = bán-MDP"); Puterman (1994, chương bán-MDP, cần kiểm: Chương 11) |
| §5.3 Lập kế hoạch ở nhiều mức trừu tượng thời gian | 11.4.2 | SB §17.2 tr. 463 (lặp giá trị với tùy chọn, hội tụ tới chính sách phân cấp tốt nhất) | Sutton, Precup và Singh (1999, Q-learning bán-MDP và ví dụ các phòng; cần kiểm) |
| §5.4 Đọc thêm: học mô hình tùy chọn | 11.4 | SB §17.1–17.2 tr. 459–463 (hàm giá trị tổng quát, học trong tùy chọn) | — |
| §6 Tổng kết | 11.5 | tổng hợp các mục trên | — |

## 2. Câu hỏi trung tâm

**Kết quả kế thừa** (mở §1, GC-RL-2, GC15): Q-learning dạng bảng hội tụ tới $q_*$ khi mọi cặp được cập nhật vô hạn lần và bước học thỏa Robbins–Monro (Định lý 06.21); mỗi mẫu thật chỉ được dùng cho một cập nhật. Lặp giá trị bất đồng bộ hội tụ khi biết mô hình và mọi trạng thái được cập nhật vô hạn lần (Định lý 04.32).

**Bài toán cụ thể có số liệu** (đoạn mở §1.1):

- Trên mê cung hai phòng (Ví dụ 11.1), sau lượt thật thứ nhất $(\mathrm A,\rightarrow,\mathrm A)$, $(\mathrm A,\rightarrow,\mathrm B)$, $(\mathrm B,\downarrow,\mathrm F)$, $(\mathrm F,\rightarrow,\mathrm K)$, $(\mathrm K,\rightarrow,\mathrm Z)$, Q-learning với bảng khởi tạo $0$, $\alpha=0{,}5$, $\gamma=0{,}9$ chỉ có một ô khác $0$: $Q(\mathrm K,\rightarrow)=0{,}5$. Bốn mẫu chuyển còn lại đã nằm trong bộ nhớ nhưng không được dùng thêm.
- Trên mê cung Dyna của SB (Ví dụ 8.1, tr. 164), tác tử không lập kế hoạch cần khoảng 25 lượt để đạt hiệu năng gần tối ưu, còn tác tử làm 50 cập nhật lập kế hoạch sau mỗi bước thật chỉ cần 3 lượt.
- Mô hình học từ một lượt sai ở chỗ khác nhau: cặp $(\mathrm A,\rightarrow)$ mới được thử hai lần, một lần trượt; cặp $(\mathrm C,\cdot)$ chưa được thử lần nào.

**Câu hỏi trung tâm** (đoạn mở §1.1 và hộp "Câu hỏi:" của trang `L11-1-06`; bản nháp, tác tử soạn chỉnh bằng `no-ai-slop` Edit):

> Tác tử chỉ được thực hiện ít bước thật nhưng sau mỗi bước được làm thêm một số phép tính trên mô hình học từ các bước đã đi. Dùng mô hình đó thế nào để chọn hành động tốt hơn học phi mô hình với cùng số bước thật, và sai lệch của mô hình làm hỏng kết luận ở đâu?

**Câu trả lời có điều kiện của chương** (đoạn §6.2, trang "Vấn đề trung tâm" của mạch Tổng kết, ghi chú diễn giả trang `L11-1-06`):

- **Lập kế hoạch nền** (§2): Q-planning là Q-learning trên MDP của mô hình, hội tụ tới $q_*$ của mô hình (Mệnh đề 11.9). Dyna-Q dùng mỗi bước thật thêm $n$ lần; trên mê cung hai phòng, hai cập nhật lập kế hoạch sau lượt thứ nhất đã đưa giá trị về $\mathrm F$: $Q(\mathrm F,\rightarrow)=0{,}225$ (Ví dụ 11.7). Điều kiện: mô hình đúng trên các cặp được lấy mẫu. Môi trường ngẫu nhiên cần mô hình đếm (Định nghĩa 11.4); môi trường thay đổi cần thưởng thăm dò (Định nghĩa 11.12). Bất định nhận thức giảm theo $1/\sqrt{C(s,a)}$ (Mệnh đề 11.5).
- **Lập kế hoạch tại thời điểm quyết định** (§3): với $q_\pi$ chính xác, rollout không làm giảm giá trị (Mệnh đề 11.21); tại $\mathrm F$, chính sách ngẫu nhiên đều có $v=0{,}2016$, chính sách rollout đạt $0{,}8566=v_*(\mathrm F)$. Với ước lượng Monte Carlo, $m=70$ mô phỏng mỗi hành động đủ để xác suất chọn $\downarrow$ thay vì $\rightarrow$ không vượt $0{,}05$ (Mệnh đề 11.22). UCT nhất quán khi chân trời hữu hạn và phần thưởng trong $[0,1]$ (Định lý 11.27).
- **Tối ưu kế hoạch bằng đạo hàm** (§4): với mô hình khả vi và hành động liên tục, một bước hạ gradient giảm chi phí của xe trên đường ray từ $8$ xuống $2{,}88$, nghiệm tối ưu $2{,}4$ (Ví dụ 11.18, 11.19). Điều khiển dự báo sửa sai số mô hình bằng cách lập lại kế hoạch: với mô hình $a=1$ cho hệ thật $a=1{,}2$, vòng kín vẫn co về $0$ với hệ số $0{,}6$ (Ví dụ 11.23), còn sai số dự báo vòng hở tăng theo $\bar e(L^k-1)/(L-1)$ (Mệnh đề 11.36).
- **Tùy chọn** (§5): lặp giá trị với hai tùy chọn cho đúng $v_*(\mathrm A)=0{,}6604$ sau hai vòng, trong khi lặp giá trị trên hành động một bước sau sáu lượt quét mới cho $0{,}6103$ (Ví dụ 11.26). Chỉ dùng tùy chọn thì kết quả là chính sách phân cấp tốt nhất trong tập tùy chọn, có thể kém $v_*$; thêm mọi hành động một bước vào $\Omega(s)$ thì hội tụ tới $v_*$ (Định lý 11.44).

## 3. Mục tiêu học tập (dự thảo, bằng lời, không ký hiệu mới, không số hiệu khối; GC16, VP21)

Sau chương này, người học có thể:

1. **Mô hình và tính bất định.** Phân biệt mô hình phân phối với mô hình mẫu, lập kế hoạch nền với lập kế hoạch tại thời điểm quyết định; ước lượng mô hình bằng tần suất từ dữ liệu, tách bất định ngẫu nhiên khỏi bất định nhận thức và tính độ lệch chuẩn của xác suất ước lượng (Mục 2).
2. **Dyna.** Thực hiện bằng tay một bước thật của Dyna-Q gồm cập nhật trực tiếp, cập nhật mô hình và các cập nhật lập kế hoạch; nêu điều kiện hội tụ của Q-planning; giải thích vì sao mô hình sai cần thưởng thăm dò (Mục 2).
3. **Cập nhật kỳ vọng và cập nhật mẫu.** So sánh hai loại cập nhật theo số phép tính và sai số khi ngân sách tính toán nhỏ hơn hệ số phân nhánh (Mục 2).
4. **Rollout và tìm kiếm theo cây.** Phát biểu tính chất cải thiện của thuật toán rollout cùng giả thiết; tính số mô phỏng đủ cho một xác suất chọn sai; tính chỉ số cận tin cậy trên; thực hiện một vòng tìm kiếm theo cây Monte Carlo qua bốn pha (Mục 3).
5. **Tối ưu kế hoạch bằng đạo hàm.** Tính gradient của chi phí kế hoạch theo chuỗi hành động qua mô hình khả vi bằng truy hồi ngược, thực hiện một bước hạ gradient và một vòng phương pháp entropy chéo; mô tả điều khiển dự báo theo chân trời lùi và chặn sai số dự báo tích lũy (Mục 4).
6. **Tùy chọn.** Định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của một tùy chọn; viết phương trình Bellman bán-MDP; thực hiện lặp giá trị và một cập nhật Q-learning với tùy chọn (Mục 5).
7. **Chọn cách dùng mô hình.** Với một bài toán cụ thể, chọn cách dùng mô hình phù hợp và kiểm các giả thiết mà bảo đảm của cách đó cần (Mục 6, Tình huống áp dụng).

Ghi chú cho tác tử soạn: như ghi chú 06, câu cuối mục có thể kèm danh sách bài tập theo mục tiêu ("(Bài tập 11.1, 11.2, 11.10, 11.17)"); bảng ánh xạ ở `ke-hoach-bai-tap.md` mục 4.

## 4. Kiến thức tiên quyết (dự thảo danh sách; GC16, GC3, `AGENTS.md` "Cấu trúc bắt buộc của một chương" mục 4)

Câu quy ước: "Số hiệu `01.k`, …, `10.k` chỉ khối trong ghi chú Bài 01–10; `11.k` chỉ ghi chú này." Mỗi gạch đầu dòng mở bằng tên nhóm in đậm kèm số hiệu, rồi phát biểu lại trong một đến hai câu (tác tử soạn chép đúng phát biểu từ ghi chú gốc, không diễn đạt lại sai nghĩa).

1. **Mô hình, lập kế hoạch, thăm dò** (Định nghĩa 01.14, 01.16). Mô hình cho dự báo $(\widehat S_{t+1},\widehat R_{t+1})$ hoặc phân phối của chúng khi biết trạng thái và hành động; lập kế hoạch là dùng mô hình để chọn hành động bằng cách xét diễn biến tương lai trước khi chúng xảy ra. Trong bài toán chọn lặp lại một bước, $N(a)$ là số lần chọn $a$, $\bar r(a)$ là trung bình mẫu của phần thưởng; thăm dò là chọn hành động không tham lam theo $\bar r$.
2. **MDP hữu hạn, động lực, giá trị** (Định nghĩa 03.4, 03.7, 03.9; Mệnh đề 03.6, 03.22; Bổ đề 03.20; Định lý 03.28). Động lực $p(s',r\mid s,a)$ cho xác suất chuyển $p(s'\mid s,a)$ và phần thưởng kỳ vọng $r(s,a)$; $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$; phần tương lai của lượt chỉ phụ thuộc trạng thái hiện tại (dùng ở chứng minh Định lý 11.42); với $0\le\gamma<1$, hệ đánh giá chính sách có nghiệm duy nhất (dùng để tính $v$ của chính sách ngẫu nhiên đều ở Ví dụ 11.12).
3. **Toán tử Bellman và ánh xạ co** (Định nghĩa 04.1, 04.22; Mệnh đề 04.4, 04.24; Định lý 04.5, 04.25). $T_*$ co với hệ số $\gamma$ theo chuẩn vô cùng; ánh xạ co trên $\mathbb R^n$ có điểm bất động duy nhất và phép lặp hội tụ với $\lVert V_k-\bar V\rVert_\infty\le\beta^k\lVert V_0-\bar V\rVert_\infty$ (dùng ở Định lý 11.44).
4. **Cải thiện chính sách** (Định lý 04.13). Nếu $q_\pi(s,\pi'(s))\ge v_\pi(s)$ với mọi $s$ thì $v_{\pi'}\ge v_\pi$; nghiêm ngặt tại $s$ khi điều kiện nghiêm ngặt tại $s$; điều kiện áp dụng: $v_\pi$ chính xác (dùng ở Mệnh đề 11.21).
5. **Lặp giá trị bất đồng bộ** (Thuật toán 04.31, Định lý 04.32). Cập nhật từng trạng thái theo lịch tùy ý, mỗi trạng thái vô hạn lần, hội tụ về $v_*$ (dùng ở §2.7 và Nhận xét 11.17).
6. **Trung bình mẫu, mô hình thực nghiệm** (Định nghĩa 05.8, Mệnh đề 05.9, 05.34). Trung bình gia tăng $V_n=V_{n-1}+(g_n-V_{n-1})/n$; nghiệm TD theo lô là nghiệm của MDP thực nghiệm với $\hat r(s)$ và $\hat P(s'\mid s)$ tính từ dữ liệu (nối với mô hình đếm, Định nghĩa 11.4).
7. **Q-learning và hội tụ** (Định nghĩa 06.3, 06.15, 06.19; Thuật toán 06.16; Nhận xét 06.20; Định lý 06.21). Chính sách $\varepsilon$-tham lam; mục tiêu $R+\gamma\max_{a'}Q(S',a')$; dưới các giả thiết nền (MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, mẫu theo $p(\cdot,\cdot\mid s,a)$), mọi cặp cập nhật vô hạn lần và bước học thỏa Robbins–Monro theo cặp, $Q_t\to q_*$ hầu chắc chắn (dùng ở Mệnh đề 11.9).
8. **Bất đẳng thức Hoeffding** (Mệnh đề 06.26; Hoeffding 1963, Định lý 2, tr. 16). Phát biểu lại dạng một phía cho tổng các biến độc lập không cùng phân phối: nếu $X_i\in[a_i,b_i]$ độc lập thì $\Pr\{\sum_iX_i-\mathbb E\sum_iX_i\le-t\}\le\exp\bigl(-2t^2/\sum_i(b_i-a_i)^2\bigr)$ (dùng ở Mệnh đề 11.22). Ghi chú 06 chỉ phát biểu dạng hai phía cho trung bình cùng phân phối, nên dạng này cần phát biểu đầy đủ tại đây (GC3).
9. **Bộ nhớ phát lại, bộ tối ưu theo gradient** (Định nghĩa 08.7, 08.15, 08.16). Bộ nhớ phát lại lưu $N$ mẫu chuyển gần nhất và rút đều; hạ gradient với tốc độ học $\eta$ cập nhật $\theta\leftarrow\theta-\eta g$ (dùng ở Nhận xét 11.11 và Thuật toán 11.31).
10. **Giải tích và xác suất** (kiến thức đại học, GC-RL-16): quy tắc dây chuyền; phân phối nhị thức, phương sai của trung bình mẫu độc lập; bất đẳng thức hợp (union bound).

Công cụ không có trong Bài 01–10 và được trình bày đầy đủ trong chính ghi chú (không đưa vào danh sách tiên quyết): thuật toán rollout (§3.1), quy tắc cận tin cậy trên và chặn hối tiếc UCB1 (§3.2), điều khiển dự báo theo chân trời lùi (§4.3). Chúng thuộc Chương 4 của giáo trình, chương không có bài giảng trong học phần.

## 5. Bảng ký hiệu (dự thảo, 24 dòng; GC-RL-6, GC16, VP-RL-5)

Câu dẫn: bảng gồm ký hiệu dùng xuyên suốt chương; mỗi chữ giữ một nghĩa trong cả chương; ký hiệu cục bộ được giới thiệu tại chỗ. Các xung đột đã tránh (QG5): $c$ dành cho chi phí mỗi bước (VP-RL-5), nên hằng số của quy tắc cận tin cậy trên viết $c_{\mathrm{ucb}}$ (SB viết $c$); $\varepsilon$ dành cho chính sách $\varepsilon$-tham lam, nên chặn sai số một bước của mô hình viết $\bar e$; SB viết $\tau$ cho số bước kể từ lần thử gần nhất trong Dyna-Q+, ghi chú viết $\ell(s,a)$ để $\tau$ chỉ thời điểm kết thúc của tùy chọn; chân trời viết $h$ như (7.13) của SB, để $H_t$ giữ nghĩa lịch sử; bộ đếm của mô hình viết $C(s,a)$, để $N(s,a)$ chỉ số lần thăm trên cây tìm kiếm.

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $\mathcal S^+$ | tập trạng thái không kết thúc; thêm trạng thái kết thúc | tập hữu hạn (§1–§3, §5) |
| $\mathcal A(s)$ | tập hành động hợp lệ tại $s$ | tập hữu hạn khác rỗng |
| $t$, $T$ | chỉ số bước; thời điểm kết thúc lượt | $\{0,1,\dots\}$; nguyên dương hoặc $\infty$ |
| $S_t$, $A_t$, $R_{t+1}$ | trạng thái, hành động, phần thưởng của chuyển từ $t$ sang $t+1$ | $\mathcal S^+$, $\mathcal A(S_t)$, $\mathbb R$ |
| $p(s',r\mid s,a)$; $p(s'\mid s,a)$, $r(s,a)$ | động lực thật; xác suất chuyển, phần thưởng kỳ vọng | phân phối; $[0,1]$; $\mathbb R$ |
| $\hat p(s'\mid s,a)$, $\hat r(s,a)$ | mô hình học được (mô hình đếm ở §2) | phân phối trên $\mathcal S^+$; $\mathbb R$ |
| $C(s,a)$, $C(s,a,s')$ | số lần thử thật cặp $(s,a)$; số lần trong đó đi tới $s'$ | $\{0,1,\dots\}$ |
| $\gamma$ | hệ số chiết khấu | $[0,1)$ |
| $\pi$, $\pi_0$ | chính sách; chính sách cơ sở của rollout | phân phối trên $\mathcal A(s)$ với mỗi $s$ |
| $v_\pi$, $q_\pi$, $v_*$, $q_*$ | giá trị thật của $\pi$; giá trị tối ưu | hàm thực |
| $Q$ | bảng giá trị hành động đang học hoặc đang lập kế hoạch | $\mathbb R$ trên mỗi cặp hợp lệ |
| $\alpha$, $\varepsilon$ | bước học; tham số của chính sách $\varepsilon$-tham lam | $(0,1]$; $[0,1]$ |
| $n$ | số cập nhật lập kế hoạch sau mỗi bước thật | số nguyên không âm |
| $\kappa$, $\ell(s,a)$ | hệ số thưởng thăm dò; số bước thật kể từ lần thử gần nhất của $(s,a)$ | $\kappa>0$; $\{0,1,\dots\}$ |
| $b$ | hệ số phân nhánh: số trạng thái kế có xác suất dương | số nguyên dương |
| $m$ | số mô phỏng cho mỗi hành động của thuật toán rollout | số nguyên dương |
| $N(s)$, $N(s,a)$, $W(s,a)$, $\bar Q(s,a)$ | số lần thăm nút, cạnh trên cây; tổng lợi tức; trung bình $W/N$ | $\{0,1,\dots\}$; $\mathbb R$ |
| $c_{\mathrm{ucb}}$ | hằng số thăm dò của quy tắc cận tin cậy trên | $c_{\mathrm{ucb}}>0$ |
| $x_t$, $u_t$; $f$, $\hat f$ | trạng thái, hành động liên tục của §4; động lực thật, mô hình | $\mathbb R$; $\mathbb R\times\mathbb R\to\mathbb R$ |
| $h$, $c(x,u)$, $J$ | chân trời; chi phí mỗi bước; chi phí của một kế hoạch | nguyên dương; $\mathbb R_{\ge0}$; $\mathbb R^h\to\mathbb R$ |
| $\eta$; $\bar e$, $e_k$, $L$ | tốc độ học; chặn sai số một bước của mô hình, sai số dự báo $k$ bước, hằng số Lipschitz | dương; $\mathbb R_{\ge0}$; $L\ge0$ |
| $\omega$, $\Omega(s)$; $\mathcal I_\omega$, $\pi_\omega$, $\beta_\omega$ | tùy chọn, tập tùy chọn dùng được tại $s$; tập khởi đầu, chính sách, hàm kết thúc | $\mathcal I_\omega\subseteq\mathcal S$; $\beta_\omega:\mathcal S^+\to[0,1]$ |
| $\tau$; $r(s,\omega)$, $p(s'\mid s,\omega)$ | thời điểm kết thúc của tùy chọn; hai phần của mô hình tùy chọn | $\{1,2,\dots\}$; $\mathbb R$; $[0,\gamma]$ |
| $\mu$, $v_\mu$, $v_\Omega$ | chính sách phân cấp; giá trị của nó; giá trị tối ưu trên tập tùy chọn | phân phối trên $\Omega(s)$; hàm thực |

Đoạn quy ước sau bảng (GC-RL-6): $R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$; giá trị của trạng thái kết thúc bằng $0$ trong hàm thật, bảng và mô hình; kỳ vọng $\mathbb E_\pi$ lấy theo chính sách và động lực thật, $\hat{\mathbb E}$ theo mô hình; bất đẳng thức giữa hai hàm hiểu theo từng trạng thái; tên ô viết chữ đứng ($\mathrm A$, …, $\mathrm Z$), hành động của mê cung viết bằng mũi tên $\uparrow,\downarrow,\leftarrow,\rightarrow$ (không viết chữ tiếng Việt trong KaTeX, NT26); số thập phân dùng dấu phẩy (VP-RL-6). Tương ứng với *Học máy thống kê* nêu một lần: $v_\pi$ ứng với $V^\pi$, $p(s'\mid s,a)$ ứng với $T(s,a,s')$. Tương ứng với SB nêu một lần: SB viết tùy chọn $\langle\pi_\omega,\gamma_\omega\rangle$ với $\gamma_\omega$ là xác suất **tiếp tục**, ghi chú dùng $\beta_\omega=1-\gamma_\omega$ là xác suất **kết thúc** và thêm tập khởi đầu $\mathcal I_\omega$ theo Sutton, Precup và Singh (1999).

## 6. Cấu trúc chương, mạch và `note-topic-id` (GC-RL-1, GC-RL-12)

Tên mục là cụm danh từ (VP7, GC-RL-17); không có tiêu đề "Nhu cầu"; chú thích `note-topic-id` đặt ngay trước tiêu đề `###` như ghi chú 10.

| Phần ghi chú | Tiêu đề dự kiến | `note-topic-id` | Mạch deck |
|---|---|---|---|
| Tiêu đề | `# Bài 11 — Lập kế hoạch dựa trên mô hình` | — | — |
| Giới thiệu | bỏ, hoặc một đoạn ngắn (GC-RL-1) | — | 1 |
| Mục tiêu, Tiên quyết, Ký hiệu | `## Mục tiêu học tập`, `## Kiến thức tiên quyết`, `## Bảng ký hiệu` | `lec-11-topic-01` (tiên quyết) | 1 |
| §1 | `## 1. Bài toán lập kế hoạch với mô hình học được` | — | 1 Mở đầu |
| 1.1 | `### 1.1 Kết quả kế thừa và bài toán trung tâm` | `lec-11-topic-02` | 1 |
| 1.2 | `### 1.2 Ba cách dùng mô hình` | `lec-11-topic-03` | 1 |
| §2 | `## 2. Tính bất định của môi trường và lập kế hoạch nền` | — | 2 |
| 2.1 | `### 2.1 Mô hình phân phối và mô hình mẫu` | `lec-11-topic-04` | 2 |
| 2.2 | `### 2.2 Mô hình đếm và hai loại bất định` | `lec-11-topic-05` | 2 |
| 2.3 | `### 2.3 Tập mô hình` | `lec-11-topic-06` | 2 |
| 2.4 | `### 2.4 Q-planning và kiến trúc Dyna` | `lec-11-topic-07` | 2 |
| 2.5 | `### 2.5 Mô hình sai và thưởng thăm dò` | `lec-11-topic-08` | 2 |
| 2.6 | `### 2.6 Cập nhật kỳ vọng và cập nhật mẫu` | `lec-11-topic-09` | 2 |
| 2.7 | `### 2.7 Đọc thêm: phân bổ các cập nhật` | `lec-11-topic-10` | 2 (chỉ ghi chú diễn giả) |
| §3 | `## 3. Tìm kiếm theo cây Monte Carlo` | — | 3 |
| 3.1 | `### 3.1 Lập kế hoạch tại thời điểm quyết định và thuật toán rollout` | `lec-11-topic-11` | 3 |
| 3.2 | `### 3.2 Chọn hành động theo cận tin cậy trên` | `lec-11-topic-12` | 3 |
| 3.3 | `### 3.3 Bốn pha của tìm kiếm theo cây Monte Carlo` | `lec-11-topic-13` | 3 |
| 3.4 | `### 3.4 Bảo đảm của UCT và giá trị học được` | `lec-11-topic-14` | 3 |
| §4 | `## 4. Tối ưu kế hoạch dựa trên đạo hàm` | — | 4 |
| 4.1 | `### 4.1 Bài toán tối ưu kế hoạch trên mô hình khả vi` | `lec-11-topic-15` | 4 |
| 4.2 | `### 4.2 Đạo hàm qua mô hình` | `lec-11-topic-16` | 4 |
| 4.3 | `### 4.3 Điều khiển dự báo theo chân trời lùi` | `lec-11-topic-17` | 4 |
| 4.4 | `### 4.4 Bắn ngẫu nhiên và phương pháp entropy chéo` | `lec-11-topic-18` | 4 |
| 4.5 | `### 4.5 Sai số mô hình tích lũy` | `lec-11-topic-19` | 4 |
| §5 | `## 5. Học tăng cường phân cấp` | — | 5 |
| 5.1 | `### 5.1 Tùy chọn và chính sách phân cấp` | `lec-11-topic-20` | 5 |
| 5.2 | `### 5.2 Mô hình tùy chọn và bán-MDP` | `lec-11-topic-21` | 5 |
| 5.3 | `### 5.3 Lập kế hoạch ở nhiều mức trừu tượng thời gian` | `lec-11-topic-22` | 5 |
| 5.4 | `### 5.4 Đọc thêm: học mô hình tùy chọn` | `lec-11-topic-23` | 5 (chỉ ghi chú diễn giả) |
| §6 | `## 6. Tổng kết` (6.1 So sánh bốn cách dùng mô hình; 6.2 Trả lời bài toán trung tâm; 6.3 Câu hỏi tự kiểm tra) | `lec-11-topic-24` | 6 Tổng kết |
| Tình huống | `## Tình huống áp dụng và ứng dụng` | `lec-11-topic-25` | 6 |
| Tóm tắt | `## Tóm tắt chương` | `lec-11-topic-26` | 6 |
| Bài tập | `## Bài tập củng cố` | `lec-11-topic-27` | 6 (trang "Bài tập về nhà") |
| Tham khảo | `## Hướng dẫn đọc thêm và tài liệu tham khảo` | `lec-11-topic-28` | 6 (trang "Tài liệu tham khảo") |

Mục §6 "Tổng kết" theo mẫu §7 của ghi chú 10 (đổi tên theo GC-RL-15); có cần giữ song song với "Tóm tắt chương" hay không: QG6.

## 7. Hai ví dụ xuyên suốt và các phép tính tay

Mỗi khối dưới đây ghi dữ kiện, phép tính từng bước và dòng kiểm tra. Tác tử soạn chép đủ dữ kiện vào từng khối `example` dùng nó (GC23: ví dụ nối tiếp mở bằng đoạn "Dữ kiện"). Số thập phân viết đủ sáu chữ số ở đây để kiểm; ghi chú làm tròn bốn chữ số khi không cần hơn. Dữ kiện tự dựng viết "Giả sử …" (VP18); nguồn gốc của chúng ghi ở `review-log.md`, không ghi trong ghi chú.

### 7.1 Mê cung hai phòng (ví dụ xuyên suốt thứ nhất; Ví dụ 11.1)

**Bố cục** (hình `me-cung-hai-phong.svg`, mục 14):

```
            cột 1   cột 2 ‖ cột 3   cột 4
hàng trên:    A       B   ‖   C       D
hàng dưới:    E       F       K       Z
```

- Tám ô; $\mathrm Z$ là ô đích, trạng thái kết thúc. Tường đứng giữa $\mathrm B$ và $\mathrm C$ (chỉ ở hàng trên); hàng dưới thông, nên **cửa** giữa hai phòng là cạnh $\mathrm F$–$\mathrm K$. Phòng trái $\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$, phòng phải $\{\mathrm C,\mathrm D,\mathrm K\}$ cùng ô đích $\mathrm Z$. Lượt bắt đầu ở $\mathrm A$.
- Hành động $\mathcal A(s)=\{\uparrow,\downarrow,\leftarrow,\rightarrow\}$ tại mọi ô không kết thúc.
- Động lực: với xác suất $0{,}8$ tác tử sang ô kề theo hướng đã chọn, nếu hướng đó đụng tường hoặc biên thì ở yên; với xác suất $0{,}2$ tác tử **trượt** và ở yên.
- Phần thưởng $+1$ cho mọi chuyển vào $\mathrm Z$, $0$ cho mọi chuyển khác; $\gamma=0{,}9$.
- Khoảng cách tới đích (số bước đi đúng tối thiểu) $d(s)$: $d(\mathrm K)=d(\mathrm D)=1$; $d(\mathrm F)=d(\mathrm C)=2$; $d(\mathrm B)=d(\mathrm E)=3$; $d(\mathrm A)=4$.

**Giá trị tối ưu** (Ví dụ 11.1, kiểm bằng phương trình Bellman tối ưu, Định lý 04.25). Với chính sách đi theo đường ngắn nhất, một ô ở khoảng cách $d$ thỏa $v(d)=0{,}8\,[\mathbb 1\{d=1\}+\gamma v(d-1)\mathbb 1\{d\ge2\}]+0{,}2\gamma\,v(d)$:

- $d=1$: $v(1)=0{,}8+0{,}18\,v(1)$, nên $v(1)=0{,}8/0{,}82=0{,}975610$.
- $d\ge2$: $v(d)=0{,}72\,v(d-1)+0{,}18\,v(d)$, nên $v(d)=\dfrac{0{,}72}{0{,}82}v(d-1)=0{,}878049\,v(d-1)$.
- $v_*(\mathrm K)=v_*(\mathrm D)=0{,}975610$; $v_*(\mathrm F)=v_*(\mathrm C)=0{,}856633$; $v_*(\mathrm B)=v_*(\mathrm E)=0{,}752166$; $v_*(\mathrm A)=0{,}660438$.
- Kiểm tối ưu tại $\mathrm F$: $q_*(\mathrm F,\rightarrow)=0{,}72\cdot0{,}975610+0{,}18\cdot0{,}856633=0{,}702439+0{,}154194=0{,}856633$; $q_*(\mathrm F,\downarrow)=0{,}9\cdot0{,}856633=0{,}770970$ (đụng biên, ở yên); $q_*(\mathrm F,\uparrow)=q_*(\mathrm F,\leftarrow)=0{,}72\cdot0{,}752166+0{,}154194=0{,}695753$. Cực đại là $\rightarrow$, khớp $v_*(\mathrm F)$.
- Đã chạy lặp giá trị 2 000 lượt quét bằng Python: khớp sáu chữ số.

**Mô hình tất định sai** (dùng ở Tình huống 11.2): nếu bỏ trượt, giá trị là $\gamma^{d-1}$: $\mathrm K$: $1$; $\mathrm F$: $0{,}9$; $\mathrm B$: $0{,}81$; $\mathrm A$: $0{,}729$. Chênh so với $v_*$ tại $\mathrm A$: $0{,}729-0{,}660438=0{,}068562$.

**Lượt thật thứ nhất** (dùng ở §1.1, Ví dụ 11.3, 11.7; "Giả sử" trong ghi chú): năm mẫu chuyển $(S,A,R,S')$:

1. $(\mathrm A,\rightarrow,0,\mathrm A)$ (trượt);
2. $(\mathrm A,\rightarrow,0,\mathrm B)$;
3. $(\mathrm B,\downarrow,0,\mathrm F)$;
4. $(\mathrm F,\rightarrow,0,\mathrm K)$;
5. $(\mathrm K,\rightarrow,+1,\mathrm Z)$.

**Ví dụ 11.2 (mô hình phân phối và mô hình mẫu của $(\mathrm F,\rightarrow)$).** Mô hình phân phối trả cả bảng $\{\mathrm K:0{,}8;\ \mathrm F:0{,}2\}$ với phần thưởng $0$; mô hình mẫu trả một ô, chẳng hạn $\mathrm K$, rút theo các xác suất đó. Kỳ vọng của mục tiêu một bước với $\max_aQ(\mathrm K,a)=0{,}5$, $\max_aQ(\mathrm F,a)=0$: mô hình phân phối cho $0{,}9(0{,}8\cdot0{,}5+0{,}2\cdot0)=0{,}36$; mô hình mẫu cho $0{,}45$ (mẫu $\mathrm K$) hoặc $0$ (mẫu $\mathrm F$), trung bình theo xác suất $0{,}8\cdot0{,}45+0{,}2\cdot0=0{,}36$. Kiểm: hai cách cùng kỳ vọng.

**Ví dụ 11.3 (bảng đếm sau lượt thứ nhất) và Ví dụ 11.4 (hai loại bất định).** Từ năm mẫu: $C(\mathrm A,\rightarrow)=2$, $C(\mathrm A,\rightarrow,\mathrm A)=C(\mathrm A,\rightarrow,\mathrm B)=1$, nên $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$; $C(\mathrm B,\downarrow)=C(\mathrm F,\rightarrow)=C(\mathrm K,\rightarrow)=1$ với $\hat p=1$ cho ô đã gặp; các cặp còn lại có $C=0$, mô hình chưa xác định. Giả sử sau bốn lượt nữa $C(\mathrm F,\rightarrow)=5$ với $4$ lần tới $\mathrm K$: $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=0{,}8$. Theo Mệnh đề 11.5, nếu xác suất thật là $p=0{,}8$, độ lệch chuẩn của $\hat p$ là $\sqrt{p(1-p)/C}$:

| $C(s,a)$ | $2$ | $5$ | $50$ |
|---|---:|---:|---:|
| $\sqrt{0{,}16/C}$ | $0{,}282843$ | $0{,}178885$ | $0{,}056569$ |

Bất định ngẫu nhiên của trạng thái kế là phương sai Bernoulli $p(1-p)=0{,}16$, không đổi theo $C$. Kiểm: $0{,}16/2=0{,}08$, $\sqrt{0{,}08}=0{,}282843$.

**Ví dụ 11.5 (tập ba mô hình tại $(\mathrm A,\rightarrow)$).** Dữ liệu $\{\mathrm A,\mathrm B\}$. Giả sử ba lần lấy lại mẫu có hoàn lại cỡ $2$ cho $\{\mathrm A,\mathrm A\}$, $\{\mathrm A,\mathrm B\}$, $\{\mathrm B,\mathrm B\}$: ba mô hình cho $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0$, $0{,}5$, $1$. Trung bình $0{,}5$; độ lệch chuẩn tổng thể $\sqrt{(0{,}25+0+0{,}25)/3}=\sqrt{0{,}166667}=0{,}408248$. Với $(\mathrm B,\downarrow)$, dữ liệu $\{\mathrm F\}$ chỉ có một mẫu nên mọi lần lấy lại mẫu đều cho $\hat p(\mathrm F)=1$: tập mô hình **không** thấy bất định nhận thức ở cặp chỉ có một mẫu (Nhận xét 11.7, nhầm lẫn thường gặp theo GC11).

**Ví dụ 11.6 (một cập nhật Q-planning).** Dữ kiện: $Q\equiv0$ trừ $Q(\mathrm K,\rightarrow)=0{,}5$; $\alpha=0{,}5$, $\gamma=0{,}9$; mô hình mẫu trả $(0,\mathrm K)$ cho $(\mathrm F,\rightarrow)$. Mục tiêu $0+0{,}9\cdot\max_aQ(\mathrm K,a)=0{,}9\cdot0{,}5=0{,}45$; sai lệch $0{,}45-0=0{,}45$; giá trị mới $0+0{,}5\cdot0{,}45=0{,}225$.

**Ví dụ 11.7 (lượt thứ nhất của Dyna-Q, $n=2$).** Dữ kiện: $Q\equiv0$, $\alpha=0{,}5$, $\gamma=0{,}9$, $\varepsilon$-tham lam với phá hòa ngẫu nhiên; mô hình tất định của hộp Dyna-Q (SB tr. 164) lưu kết quả gần nhất. Trong bốn bước đầu, mọi mục tiêu bằng $0$, nên $Q$ không đổi; các cập nhật lập kế hoạch sau bốn bước đó cũng chỉ thấy giá trị $0$ (mô hình chỉ có phần thưởng $0$), nên $Q$ vẫn bằng $0$. Sau bước 2, mô hình ghi $\mathrm{Model}(\mathrm A,\rightarrow)=(0,\mathrm B)$, ghi đè kết quả trượt của bước 1. Bước thứ năm:

- cập nhật trực tiếp (d): mục tiêu $1+0{,}9\cdot0=1$ ($\mathrm Z$ kết thúc); sai lệch $1$; $Q(\mathrm K,\rightarrow)=0+0{,}5\cdot1=0{,}5$;
- cập nhật mô hình (e): $\mathrm{Model}(\mathrm K,\rightarrow)=(+1,\mathrm Z)$;
- lập kế hoạch (f), giả sử bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$:
  - $(\mathrm F,\rightarrow)$: mục tiêu $0+0{,}9\cdot0{,}5=0{,}45$; sai lệch $0{,}45$; $Q(\mathrm F,\rightarrow)=0{,}225$;
  - $(\mathrm K,\rightarrow)$: mục tiêu $1+0=1$; sai lệch $1-0{,}5=0{,}5$; $Q(\mathrm K,\rightarrow)=0{,}5+0{,}25=0{,}75$.
- So sánh: với $n=0$ (Q-learning, Thuật toán 06.16), sau lượt thứ nhất chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$; $Q(\mathrm F,\rightarrow)$ chỉ đổi khi tác tử thật sự đi lại qua $\mathrm F$ ở lượt sau. Đây là hiện tượng của SB Hình 8.3, tr. 165, trên mê cung nhỏ hơn.
- Kiểm: đảo thứ tự hai cập nhật lập kế hoạch, $(\mathrm K,\rightarrow)$ trước rồi $(\mathrm F,\rightarrow)$, cho $Q(\mathrm K,\rightarrow)=0{,}75$ rồi $Q(\mathrm F,\rightarrow)=0{,}5\cdot0{,}9\cdot0{,}75=0{,}3375$: thứ tự cập nhật đổi kết quả (gợi ý cho quét ưu tiên, §2.7).

**Ví dụ 11.8 (mê cung đổi cửa) và Ví dụ 11.9 (một cập nhật Dyna-Q+).** Giả sử sau 3 000 bước thật, môi trường đổi: cửa $\mathrm F$–$\mathrm K$ bị chặn (thêm tường giữa $\mathrm F$ và $\mathrm K$), tường $\mathrm B$–$\mathrm C$ được dỡ. Đường ngắn nhất mới từ $\mathrm A$ là $\mathrm A\to\mathrm B\to\mathrm C\to\mathrm D\to\mathrm Z$, vẫn bốn bước. Ví dụ ghép hai kiểu sai của SB §8.3 trên cùng một mê cung:

- **Mô hình quá lạc quan** (kiểu mê cung bị chặn, SB Ví dụ 8.2, tr. 166): mô hình cũ ghi $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$. Khi tác tử thật sự đi $\rightarrow$ tại $\mathrm F$, nó ở yên; bước (e) ghi $(\mathrm F,\rightarrow)\mapsto(0,\mathrm F)$, và các cập nhật lập kế hoạch sau đó hạ $Q(\mathrm F,\rightarrow)$. Sai số tự được sửa vì chính sách tham lam dẫn tác tử tới chỗ sai.
- **Mô hình quá bi quan** (kiểu mê cung có lối tắt, SB Ví dụ 8.3, tr. 167): mô hình cũ ghi $(\mathrm B,\rightarrow)\mapsto(0,\mathrm B)$ (đụng tường). Chính sách tham lam theo mô hình không bao giờ chọn $\rightarrow$ tại $\mathrm B$, nên sai số chỉ được phát hiện nhờ thăm dò.

Phép tính của Dyna-Q+ tại cặp bi quan:

- Dữ kiện: mô hình cũ ghi $(\mathrm B,\rightarrow)\mapsto(0,\mathrm B)$ (đụng tường); $\ell(\mathrm B,\rightarrow)=400$; $\kappa=0{,}01$; $Q(\mathrm B,\rightarrow)=0{,}54$; $\max_aQ(\mathrm B,a)=Q(\mathrm B,\downarrow)=0{,}6$; $\alpha=0{,}5$, $\gamma=0{,}9$.
- Thưởng thăm dò $\kappa\sqrt{\ell}=0{,}01\cdot20=0{,}2$.
- Mục tiêu $0+0{,}2+0{,}9\cdot0{,}6=0{,}74$; sai lệch $0{,}74-0{,}54=0{,}2$; giá trị mới $0{,}54+0{,}5\cdot0{,}2=0{,}64$.
- Diễn giải: $0{,}64>0{,}6$, nên hành động tham lam tại $\mathrm B$ đổi sang $\rightarrow$, tác tử thử lại bức tường và phát hiện lối mở. Không có thưởng: mục tiêu $0{,}54$, sai lệch $0$, $Q$ giữ $0{,}54$ (Dyna-Q không bao giờ thử lại).
- Kiểm: $0{,}54=0{,}9\cdot0{,}6$ là giá trị mà mô hình "ở yên" cho, nên không có thưởng thì cặp này đã ở điểm bất động.

**Ví dụ 11.10 (cập nhật kỳ vọng và cập nhật mẫu tại $(\mathrm A,\rightarrow)$, $b=2$).** Dữ kiện: mô hình đếm $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=\hat p(\mathrm A\mid\mathrm A,\rightarrow)=0{,}5$, phần thưởng $0$; giả sử $\max_aQ(\mathrm B,a)=0{,}6$, $\max_aQ(\mathrm A,a)=0{,}4$; $\gamma=0{,}9$.

- Cập nhật kỳ vọng: mục tiêu $0{,}9(0{,}5\cdot0{,}6+0{,}5\cdot0{,}4)=0{,}9\cdot0{,}5=0{,}45$; đánh giá $\max_aQ$ tại hai trạng thái kế ($b=2$ lần).
- Cập nhật mẫu: mục tiêu $0{,}54$ (mẫu $\mathrm B$) hoặc $0{,}36$ (mẫu $\mathrm A$), mỗi lần một đánh giá. Trung bình của hai mẫu khác nhau với $\alpha=1/k$: $(0{,}54+0{,}36)/2=0{,}45$. Kiểm: trùng cập nhật kỳ vọng.

**Ví dụ 11.11 (sai số của cập nhật mẫu).** Theo Mệnh đề 11.15(b), sai số căn bình phương trung bình sau $k$ cập nhật mẫu là $\sqrt{(b-1)/(bk)}$:

| $b$ | $k$ | $\sqrt{(b-1)/(bk)}$ | số đánh giá $\max_aQ$ |
|---:|---:|---:|---:|
| $2$ | $1$ | $0{,}707107$ | $1$ (cập nhật kỳ vọng: $2$) |
| $100$ | $10$ | $0{,}314643$ | $10$ (cập nhật kỳ vọng: $100$) |
| $100$ | $100$ | $0{,}099499$ | $100$ |

Diễn giải: với $b=100$, mười phép đánh giá (một phần mười chi phí của cập nhật kỳ vọng) đã giảm sai số từ $1$ xuống khoảng $0{,}31$; đó là lập luận của SB Hình 8.7, tr. 174.

**Ví dụ 11.12 (rollout tại $\mathrm F$ với chính sách ngẫu nhiên đều).** Chính sách cơ sở $\pi_0$ chọn mỗi mũi tên với xác suất $1/4$. Giải hệ đánh giá chính sách bảy phương trình (Định lý 03.28; người lập kế hoạch giải bằng `numpy.linalg.solve`, tác tử rà toán giải lại):

| $s$ | $\mathrm A$ | $\mathrm B$ | $\mathrm C$ | $\mathrm D$ | $\mathrm E$ | $\mathrm F$ | $\mathrm K$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| $v_{\pi_0}(s)$ | $0{,}088969$ | $0{,}113683$ | $0{,}426962$ | $0{,}601855$ | $0{,}113683$ | $0{,}201554$ | $0{,}489270$ |

Giá trị hành động tại $\mathrm F$ theo $q_{\pi_0}(\mathrm F,a)=0{,}72\,v_{\pi_0}(\text{ô đích của }a)+0{,}18\,v_{\pi_0}(\mathrm F)$ (Mệnh đề 03.22), với $0{,}18\cdot0{,}201554=0{,}036280$:

- $\rightarrow$: $0{,}72\cdot0{,}489270+0{,}036280=0{,}352274+0{,}036280=0{,}388554$;
- $\downarrow$ (đụng biên): $0{,}9\cdot0{,}201554=0{,}181399$;
- $\uparrow$: $0{,}72\cdot0{,}113683+0{,}036280=0{,}081852+0{,}036280=0{,}118132$; $\leftarrow$: như $\uparrow$ (ô $\mathrm E$ đối xứng với $\mathrm B$).

Kiểm: $v_{\pi_0}(\mathrm F)=\tfrac14(0{,}388554+0{,}181399+2\cdot0{,}118132)=\tfrac14\cdot0{,}806217=0{,}201554$.

**Ví dụ 11.13 (chính sách rollout trên cả mê cung).** Tham lam theo $q_{\pi_0}$ ở mọi ô cho: $\mathrm A$: $\downarrow$ hoặc $\rightarrow$ (hòa, cùng $0{,}0979$); $\mathrm B$: $\downarrow$ ($0{,}1656$); $\mathrm C$: $\rightarrow$ ($0{,}5102$ so với $\downarrow$ $0{,}4291$); $\mathrm D$: $\downarrow$ ($0{,}9083$); $\mathrm E$: $\rightarrow$; $\mathrm F$: $\rightarrow$; $\mathrm K$: $\rightarrow$ ($0{,}8881$). Mọi lựa chọn là một bước của đường ngắn nhất, nên chính sách rollout có giá trị $v_*$ của Ví dụ 11.1: tại $\mathrm F$ từ $0{,}2016$ lên $0{,}8566$. Kiểm với Mệnh đề 11.21: $0{,}8566\ge0{,}2016$; ví dụ cho thấy cải thiện có thể lớn hơn nhiều so với bảo đảm, nhưng bảo đảm chỉ là "không giảm" (GC9, nêu phạm vi). Kiểm $q_{\pi_0}(\mathrm C,\rightarrow)=0{,}72\cdot0{,}601855+0{,}18\cdot0{,}426962=0{,}433336+0{,}076853=0{,}510189$.

**Ví dụ 11.14 (số mô phỏng của rollout).** Lợi tức của một mô phỏng nằm trong $[0,1]$ (phần thưởng chỉ $+1$ khi vào $\mathrm Z$, đã chiết khấu), nên $B=1$. Khoảng cách giữa hai hành động tốt nhất tại $\mathrm F$: $\Delta=0{,}388554-0{,}181399=0{,}207155$, $\Delta^2=0{,}042913$. Theo Mệnh đề 11.22, xác suất trung bình mẫu của $\downarrow$ không nhỏ hơn của $\rightarrow$ không vượt $\exp(-m\Delta^2)$:

- $m\ge\ln20/\Delta^2=2{,}995732/0{,}042913=69{,}81$, nên $m=70$ cho $\exp(-70\cdot0{,}042913)=0{,}049591\le0{,}05$;
- $m=50$ chỉ cho $0{,}116988$.
- Dùng cho Bài tập 11.8: thêm hai hành động $\uparrow$, $\leftarrow$ với $\Delta'=0{,}388554-0{,}118132=0{,}270422$, $\Delta'^2=0{,}073129$; chặn hợp $\exp(-m\Delta^2)+2\exp(-m\Delta'^2)$ bằng $0{,}061555$ khi $m=70$ và lần đầu không vượt $0{,}05$ ở $m=75$ ($0{,}048314$).

**Ví dụ 11.15 (quy tắc cận tin cậy trên, hai hành động).** Dữ kiện (bài toán chọn lặp lại một bước, Định nghĩa 01.16): sau $8$ lần chọn, hành động 1 có $\bar r=0{,}6$, $N=6$; hành động 2 có $\bar r=0{,}4$, $N=2$; $c_{\mathrm{ucb}}=1$; $\ln8=2{,}079442$.

- Hành động 1: $0{,}6+\sqrt{2{,}079442/6}=0{,}6+0{,}588704=1{,}188704$.
- Hành động 2: $0{,}4+\sqrt{2{,}079442/2}=0{,}4+1{,}019667=1{,}419667$.
- Chọn hành động 2 dù trung bình thấp hơn: thăm dò có định hướng. Kiểm: $\sqrt{0{,}346574}=0{,}588704$.

**Ví dụ 11.16 (một vòng MCTS tại $\mathrm F$, $c_{\mathrm{ucb}}=1$).** Dữ kiện, giả sử sau tám vòng lặp: thống kê các cạnh gốc

| cạnh | $N(\mathrm F,a)$ | $W(\mathrm F,a)$ | $\bar Q$ | $\sqrt{\ln8/N}$ | chỉ số UCT |
|---|---:|---:|---:|---:|---:|
| $\rightarrow$ | $4$ | $2{,}8$ | $0{,}70$ | $0{,}721013$ | $1{,}421013$ |
| $\downarrow$ | $2$ | $1{,}2$ | $0{,}60$ | $1{,}019667$ | $1{,}619667$ |
| $\uparrow$ | $1$ | $0{,}3$ | $0{,}30$ | $1{,}442027$ | $1{,}742027$ |
| $\leftarrow$ | $1$ | $0{,}2$ | $0{,}20$ | $1{,}442027$ | $1{,}642027$ |

$N(\mathrm F)=4+2+1+1=8$.

1. **Chọn:** cạnh $\uparrow$ có chỉ số lớn nhất $1{,}742$.
2. **Mở rộng:** mô hình mẫu trả trạng thái kế; giả sử ra $\mathrm B$ (xác suất $0{,}8$). Thêm nút $\mathrm B$ với $N(\mathrm B)=0$, mọi cạnh của $\mathrm B$ có $N=0$.
3. **Mô phỏng:** từ $\mathrm B$ theo chính sách rollout ngẫu nhiên đều; giả sử dãy mô phỏng là $\mathrm B\xrightarrow{\downarrow}\mathrm F\xrightarrow{\rightarrow}\mathrm K\xrightarrow{\rightarrow}\mathrm Z$ không trượt. Lợi tức tính từ cạnh gốc: phần thưởng $0,0,0,1$ ở các bước $1$–$4$, nên $G=\gamma^3=0{,}729$.
4. **Cập nhật ngược:** $N(\mathrm F,\uparrow)=2$, $W(\mathrm F,\uparrow)=0{,}3+0{,}729=1{,}029$, $\bar Q(\mathrm F,\uparrow)=0{,}5145$; $N(\mathrm F)=9$; $N(\mathrm B)=1$. Không lưu giá trị cho các trạng thái của đoạn mô phỏng ngoài cây (SB tr. 187).
5. **Chọn hành động thật** khi hết ngân sách: cạnh có $N$ lớn nhất, $\rightarrow$ ($N=4$).

Kiểm: $\ln 8/4=0{,}519860$, $\sqrt{\cdot}=0{,}721013$. Dùng cho Bài tập 11.5 (vòng kế tiếp, $\ln9=2{,}197225$): $\rightarrow$: $0{,}70+0{,}741152=1{,}441152$; $\downarrow$: $0{,}60+1{,}048147=1{,}648147$; $\uparrow$: $0{,}5145+1{,}048147=1{,}562647$; $\leftarrow$: $0{,}20+1{,}482304=1{,}682304$; chọn $\leftarrow$.

**Ví dụ 11.24 và 11.25 (hai tùy chọn và mô hình của chúng).**

- $\omega_{\mathrm{cửa}}$ ("đi tới cửa"): $\mathcal I=\{\mathrm A,\mathrm B,\mathrm E,\mathrm F\}$; $\pi_\omega$: $\mathrm A\mapsto\rightarrow$, $\mathrm B\mapsto\downarrow$, $\mathrm E\mapsto\rightarrow$, $\mathrm F\mapsto\rightarrow$; $\beta_\omega(\mathrm K)=1$, $\beta_\omega=0$ ở phòng trái. (Tên dùng chữ "cửa" trong chỉ số dưới: kiểm hiển thị KaTeX; nếu lỗi, viết $\omega_1$, $\omega_2$ và gọi tên bằng lời; QG5.)
- $\omega_{\mathrm{đích}}$ ("đi tới đích"): $\mathcal I=\{\mathrm C,\mathrm D,\mathrm K\}$; $\pi_\omega$: $\mathrm C\mapsto\rightarrow$, $\mathrm D\mapsto\downarrow$, $\mathrm K\mapsto\rightarrow$; kết thúc khi vào $\mathrm Z$.
- Một bước đi đúng cần số lần thử có phân phối hình học $\Pr\{\text{số lần}=j\}=0{,}2^{j-1}0{,}8$. Thừa số chiết khấu kỳ vọng của một bước đi đúng: $\rho=\sum_{j\ge1}\gamma^j0{,}2^{j-1}0{,}8=\dfrac{0{,}8\gamma}{1-0{,}2\gamma}=\dfrac{0{,}72}{0{,}82}=0{,}878049$. Các bước đi độc lập, nên $\mathbb E[\gamma^{\tau}]$ của $d$ bước đi là $\rho^d$.
- Mô hình của $\omega_{\mathrm{cửa}}$ (phần thưởng trong phòng trái bằng $0$): $r(s,\omega_{\mathrm{cửa}})=0$; $p(\mathrm K\mid\mathrm F,\omega)=\rho=0{,}878049$; $p(\mathrm K\mid\mathrm B,\omega)=p(\mathrm K\mid\mathrm E,\omega)=\rho^2=0{,}770970$; $p(\mathrm K\mid\mathrm A,\omega)=\rho^3=0{,}676949$.
- Mô hình của $\omega_{\mathrm{đích}}$: phần thưởng $+1$ nhận ở bước cuối, $r(\mathrm K,\omega)=\mathbb E[\gamma^{\tau-1}]=\sum_j\gamma^{j-1}0{,}2^{j-1}0{,}8=0{,}8/0{,}82=0{,}975610$; $r(\mathrm C,\omega)=0{,}975610\cdot0{,}878049=0{,}856633$; $p(\cdot\mid s,\omega_{\mathrm{đích}})$ chỉ có trạng thái kết thúc, giá trị $0$.
- Kiểm (Mệnh đề 11.41): $\sum_{s'}p(s'\mid\mathrm A,\omega_{\mathrm{cửa}})=0{,}676949\le\gamma=0{,}9$.

**Ví dụ 11.26 (lặp giá trị với tùy chọn).** $\Omega(s)$ chỉ gồm tùy chọn có $s$ trong tập khởi đầu; khởi tạo $v_0\equiv0$:

- vòng 1: phòng phải $v_1(\mathrm K)=v_1(\mathrm D)=0{,}975610$, $v_1(\mathrm C)=0{,}856633$; phòng trái $v_1=0+p\cdot v_0(\mathrm K)=0$;
- vòng 2: $v_2(\mathrm F)=0{,}878049\cdot0{,}975610=0{,}856633$; $v_2(\mathrm B)=v_2(\mathrm E)=0{,}770970\cdot0{,}975610=0{,}752166$; $v_2(\mathrm A)=0{,}676949\cdot0{,}975610=0{,}660438$;
- vòng 3: không đổi. Kiểm: trùng $v_*$ của Ví dụ 11.1, vì hai tùy chọn đi đúng đường ngắn nhất.
- So với lặp giá trị đồng bộ trên hành động một bước từ $v_0\equiv0$ (chạy bằng Python):

| lượt quét | $v(\mathrm K)$ | $v(\mathrm F)$ | $v(\mathrm B)$ | $v(\mathrm A)$ |
|---:|---:|---:|---:|---:|
| 1 | $0{,}8000$ | $0$ | $0$ | $0$ |
| 2 | $0{,}9440$ | $0{,}5760$ | $0$ | $0$ |
| 3 | $0{,}9699$ | $0{,}7834$ | $0{,}4147$ | $0$ |
| 4 | $0{,}9746$ | $0{,}8393$ | $0{,}6387$ | $0{,}2986$ |
| 6 | $0{,}9756$ | $0{,}8558$ | $0{,}7435$ | $0{,}6103$ |

Kiểm lượt 2 tại $\mathrm K$: $0{,}8+0{,}18\cdot0{,}8=0{,}944$; tại $\mathrm F$: $0{,}72\cdot0{,}8+0{,}18\cdot0=0{,}576$. Chi phí công bằng phải tính cả việc tính mô hình tùy chọn trước (Nhận xét sau Định lý 11.44).

**Ví dụ 11.27 (một cập nhật Q-learning bán-MDP).** Dữ kiện: tại $\mathrm B$ tác tử chạy $\omega_{\mathrm{cửa}}$, tùy chọn kết thúc ở $\mathrm K$ sau $k=3$ bước (một lần trượt), tổng phần thưởng chiết khấu trên đường $0$; giả sử $\max_{\omega'}Q(\mathrm K,\omega')=Q(\mathrm K,\omega_{\mathrm{đích}})=0{,}9$, $Q(\mathrm B,\omega_{\mathrm{cửa}})=0$, $\alpha=0{,}5$.

- Mục tiêu $0+\gamma^3\cdot0{,}9=0{,}729\cdot0{,}9=0{,}6561$; sai lệch $0{,}6561$; giá trị mới $0{,}5\cdot0{,}6561=0{,}32805$.
- Kiểm: chiết khấu là $\gamma^k$ theo số bước thật, không phải $\gamma$ một lần cho cả tùy chọn (nhầm lẫn thường gặp, GC11: dùng $\gamma$ cho kết quả $0{,}405$).

### 7.2 Xe trên đường ray (ví dụ xuyên suốt thứ hai; Ví dụ 11.17)

**Dữ kiện.** Vị trí $x_t\in\mathbb R$ của một xe trên đường ray thẳng, mốc $0$ là vị trí cần giữ; hành động $u_t\in\mathbb R$ là độ dịch chuyển lệnh cho bước $t$. Mô hình $\hat f(x,u)=x+u$ (tức $\hat a=1$, $\hat b=1$); hệ thật ở §4.5 và Tình huống 11.1 là $f(x,u)=1{,}2x+u$ (đường ray nghiêng làm xe trôi ra xa mốc). Chi phí mỗi bước $c(x_{t+1},u_t)=x_{t+1}^2+u_t^2$; chân trời $h=2$; không chiết khấu; $x_0=2$. Chi phí của kế hoạch $(u_0,u_1)$ trên mô hình:

$$J(u_0,u_1)=x_1^2+u_0^2+x_2^2+u_1^2,\quad x_1=x_0+u_0,\ x_2=x_1+u_1.$$

Đây là dạng chi phí (cost) của §4 theo quy ước $c$ của VP-RL-5; ghi chú nói rõ cực tiểu chi phí tương đương cực đại phần thưởng $-c$ (một câu, GC14).

**Ví dụ 11.17 (kế hoạch không làm gì).** $u=(0,0)$: $x_1=x_2=2$, $J=4+0+4+0=8$.

**Ví dụ 11.18 (một bước hạ gradient).** Khai triển trực tiếp: $J=(x_0+u_0)^2+u_0^2+(x_0+u_0+u_1)^2+u_1^2$, nên

- $\partial J/\partial u_0=2(x_0+u_0)+2u_0+2(x_0+u_0+u_1)$, tại $(0,0)$ bằng $4+0+4=8$;
- $\partial J/\partial u_1=2(x_0+u_0+u_1)+2u_1$, tại $(0,0)$ bằng $4$.
- Với $\eta=0{,}1$: $u\leftarrow(0,0)-0{,}1(8,4)=(-0{,}8,-0{,}4)$; khi đó $x_1=1{,}2$, $x_2=0{,}8$, $J=1{,}44+0{,}64+0{,}64+0{,}16=2{,}88$.

**Mệnh đề 11.30, bản truy hồi ngược (hai bản cho cùng kết quả, GC-RL-11).** Đặt $\lambda_2=\partial J/\partial x_2=2x_2$, $\lambda_1=2x_1+\lambda_2\,\partial\hat f/\partial x=2x_1+\lambda_2$; rồi $\partial J/\partial u_1=2u_1+\lambda_2\,\partial\hat f/\partial u=2u_1+\lambda_2$, $\partial J/\partial u_0=2u_0+\lambda_1$. Tại $(0,0)$: $x_1=x_2=2$, $\lambda_2=4$, $\lambda_1=4+4=8$, gradient $(8,4)$. Kiểm: trùng khai triển trực tiếp.

**Ví dụ 11.19 (kế hoạch tối ưu).** Đặt hai đạo hàm bằng $0$ với $x_0=2$: $4+3u_0+u_1=0$ và $2+u_0+2u_1=0$. Từ phương trình sau $u_0=-2-2u_1$; thế vào phương trình đầu: $4-6-6u_1+u_1=0$, nên $u_1=-0{,}4$, $u_0=-1{,}2$. Khi đó $x_1=0{,}8$, $x_2=0{,}4$, $J^*=0{,}64+1{,}44+0{,}16+0{,}16=2{,}40$. $J$ là hàm bậc hai lồi chặt (ma trận Hessian $\begin{pmatrix}6&2\\2&4\end{pmatrix}$, định thức $20>0$), nên điểm dừng là cực tiểu toàn cục. Kiểm: bước gradient ở Ví dụ 11.18 đưa $J$ từ $8$ về $2{,}88$, còn cách tối ưu $0{,}48$.

**Ví dụ 11.20 (điều khiển dự báo trên mô hình).** Bài toán chân trời 2 là bậc hai thuần nhất theo $(x_0,u)$, nên nghiệm tỉ lệ với $x_0$: $u_0^*=-0{,}6\,x_0$ (từ $-1{,}2=-0{,}6\cdot2$). Điều khiển dự báo áp dụng $u_0^*$, quan sát trạng thái mới, giải lại: luật vòng kín $u_t=-0{,}6x_t$. Nếu hệ thật trùng mô hình: $x_{t+1}=0{,}4x_t$, dãy $2;\ 0{,}8;\ 0{,}32;\ 0{,}128$. Kiểm: $0{,}8\cdot0{,}4=0{,}32$.

Công thức chung cho Tình huống 11.1 (hệ $x'=ax+u$, cùng chi phí, $h=2$): tối ưu $u_1$ cho $u_1=-a x_1/2$, $x_2=ax_1/2$; chi phí còn $(1+a^2/2)x_1^2+u_0^2$; đạo hàm theo $u_0$ cho $u_0^*=-\dfrac{(1+a^2/2)\,a}{2+a^2/2}\,x_0$. Với $a=1$: $-1{,}5/2{,}5=-0{,}6$ (khớp). Với $a=1{,}2$: $-1{,}72\cdot1{,}2/2{,}72=-0{,}758824$.

**Ví dụ 11.21 (bắn ngẫu nhiên và một vòng entropy chéo).** Giả sử bốn chuỗi ứng viên rút từ phân phối ban đầu:

| ứng viên | $(u_0,u_1)$ | $x_1$, $x_2$ | $J$ |
|---|---|---|---:|
| 1 | $(0;\ 0)$ | $2$; $2$ | $8$ |
| 2 | $(-1;\ 0)$ | $1$; $1$ | $3$ |
| 3 | $(-1;\ -0{,}5)$ | $1$; $0{,}5$ | $2{,}5$ |
| 4 | $(-2;\ 0)$ | $0$; $0$ | $4$ |

- Bắn ngẫu nhiên chọn ứng viên 3 ($J=2{,}5$, cách tối ưu $0{,}1$).
- Phương pháp entropy chéo giữ hai mẫu ưu tú (3 và 2): trung bình mới $(-1;\ -0{,}25)$, độ lệch chuẩn theo từng tọa độ $(0;\ 0{,}25)$; vòng sau rút quanh trung bình này.
- Kiểm ứng viên 4: $x_1=0$, $x_2=0$, $J=0+4+0+0=4$.
- Nhận xét cần nêu (GC11): độ lệch chuẩn $0$ ở tọa độ $u_0$ làm phân phối suy biến sau một vòng; cài đặt thường đặt sàn cho độ lệch chuẩn (nguồn: cần kiểm ở Chua và cộng sự 2018 hoặc bỏ câu này, QG3).

**Ví dụ 11.22 (sai số tích lũy của mô hình).** Hệ thật $f(x,u)=1{,}2x+u$, mô hình $\hat f(x,u)=x+u$; kế hoạch $u\equiv0$ (để tách riêng sai số mô hình), $x_0=2$. Dự báo mô hình $\hat x_k=2$; thật $x_k=2\cdot1{,}2^k$; sai số $e_k=2(1{,}2^k-1)$:

| $k$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---:|---:|---:|---:|---:|
| $e_k$ | $0{,}4$ | $0{,}88$ | $1{,}456$ | $2{,}1472$ | $2{,}97664$ |

Mệnh đề 11.36 với $\bar e=\sup|f-\hat f|$ trên các trạng thái mô hình dự báo ($\hat x_k=2$, sai số một bước $0{,}2\cdot2=0{,}4$) và $L=1{,}2$ (hằng số Lipschitz của $f$ theo $x$): $e_k\le0{,}4(1{,}2^k-1)/0{,}2=2(1{,}2^k-1)$. Kiểm: chặn đạt dấu bằng trong ví dụ tuyến tính này. Lưu ý cho tác tử soạn: $\bar e$ lấy trên quỹ đạo **dự báo** của mô hình, không trên quỹ đạo thật (quỹ đạo thật ra khỏi $|x|\le2$); chứng minh của Mệnh đề 11.36 phải tách đúng hai số hạng như vậy.

**Ví dụ 11.23 (vòng hở và điều khiển dự báo với mô hình sai).** Kế hoạch tối ưu trên mô hình từ $x_0=2$ là $(-1{,}2;\ -0{,}4)$ (Ví dụ 11.19).

- Vòng hở trên hệ thật: $x_1=1{,}2\cdot2-1{,}2=1{,}2$ (mô hình dự báo $0{,}8$); $x_2=1{,}2\cdot1{,}2-0{,}4=1{,}04$ (mô hình dự báo $0{,}4$).
- Điều khiển dự báo với cùng mô hình sai: luật $u=-0{,}6x$, hệ thật $x_{t+1}=(1{,}2-0{,}6)x_t=0{,}6x_t$: $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$. Vòng kín co về $0$ dù mô hình sai.
- Dùng cho Bài tập 11.11: luật $u=-0{,}6x$ ổn định hệ $x'=ax+u$ khi và chỉ khi $|a-0{,}6|<1$, tức $-0{,}4<a<1{,}6$.

**Tình huống 11.1 (mô hình học bằng bình phương tối thiểu).** Giả sử ba mẫu chuyển của hệ thật: $(x,u,x')=(2;\ 0;\ 2{,}4)$, $(1;\ -1;\ 0{,}2)$, $(0;\ 1;\ 1)$. Hồi quy $x'=ax+bu$: mẫu thứ ba cho $b=1$, mẫu thứ nhất cho $a=1{,}2$; mẫu thứ hai kiểm $1{,}2-1=0{,}2$. Ba mẫu khớp đúng, nên bình phương tối thiểu cho $\hat a=1{,}2$, $\hat b=1$ (tác tử soạn trình bày hệ phương trình chuẩn đầy đủ: $\sum x^2=5$, $\sum xu=-1$, $\sum u^2=2$, $\sum xx'=5$, $\sum ux'=0{,}8$; nghiệm $(1{,}2;\ 1)$, kiểm $5\cdot1{,}2-1\cdot1=5$ và $-1\cdot1{,}2+2\cdot1=0{,}8$). Luật dự báo $u=-0{,}758824x$; vòng kín $x_{t+1}=0{,}441176x_t$: $2;\ 0{,}882353;\ 0{,}389273;\ 0{,}171738$.

## 8. Kế hoạch chi tiết từng mục

Quy ước của mục này: mỗi tiểu mục ghi các bước GC18 theo thứ tự (vấn đề → trực quan → định nghĩa → kết quả hoặc thuật toán → chứng minh → ví dụ → nhận xét), khối có số hiệu kèm vai trò, mức chứng minh (**đầy đủ** / **ý tưởng** / **dẫn**, theo GC22), đoạn "Trong thực hành" (GC-RL-9, GC14) và đoạn kết mục (GC15, GC-RL-2: câu nối chỉ ở phía kết mục; mục sau mở thẳng bằng bài toán trên ví dụ xuyên suốt). Kết quả theo bốn phần **Giả thiết.**, **Kết luận.**, **Điều kiện áp dụng.**, **Phạm vi.** (GC-RL-7). Thuật toán ghi đầu vào, đầu ra, giả thiết, khởi tạo, tham số, các bước đánh số, điều kiện dừng, chi phí mỗi bước (GC-RL-7), và có ví dụ chạy tay đứng trước (GC-RL-11, NT-RL-2). Không bài tập cuối mục (QG4).

### §1. Bài toán lập kế hoạch với mô hình học được (mạch 1)

- **1.1 Kết quả kế thừa và bài toán trung tâm.** Mở bằng Định lý 06.21 (một câu phát biểu lại) và Định lý 04.32. Bài toán có số liệu: Ví dụ 11.1 (mê cung hai phòng: bố cục, động lực, $v_*$ theo khoảng cách, lượt thật thứ nhất, Q-learning sau lượt thứ nhất chỉ có $Q(\mathrm K,\rightarrow)=0{,}5$); số liệu mê cung Dyna của SB (25 lượt so với 3 lượt, tr. 164) nêu bằng một câu có nguồn. Đoạn câu hỏi trung tâm (mục 2). "**Câu hỏi.**" theo VP-RL-2 nếu cần: "Mỗi mẫu chuyển đã lưu có thể dùng thêm bao nhiêu lần?" trả lời ngay bằng ý của §2.4.
- **1.2 Ba cách dùng mô hình.** Đoạn trực quan "Về mặt ý tưởng" theo SB §8.1 tr. 160: mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị → chính sách. Ba cách dùng: cập nhật bảng giá trị cho mọi trạng thái trong lúc tác tử hành động (§2); tìm kiếm từ trạng thái hiện tại tại lúc ra quyết định (§3 cho hành động rời rạc, §4 cho hành động liên tục); gộp nhiều bước thành tùy chọn để lập kế hoạch trên thang thời gian dài hơn (§5). Hình `cau-truc-chuong.svg` có đoạn đọc hình (GC12, GC-RL-2). Không khối có số hiệu ở §1 ngoài Ví dụ 11.1.
- **Kết mục §1:** Q-learning bỏ phí mẫu đã có; muốn dùng lại mẫu cần biết mô hình là gì, ước lượng từ dữ liệu ra sao, và sai đến đâu.

### §2. Tính bất định của môi trường và lập kế hoạch nền (mạch 2; giáo trình 11.1)

**2.1 Mô hình phân phối và mô hình mẫu** (`cốt lõi`).

1. Vấn đề: cặp $(\mathrm F,\rightarrow)$ có hai kết cục; để cập nhật $Q(\mathrm F,\rightarrow)$ cần cả phân phối hay chỉ một mẫu?
2. Trực quan: ví dụ mười hai con xúc xắc của SB tr. 159 (một câu, có nguồn) và trên mê cung.
3. **Ví dụ 11.2** (mục 7.1).
4. **Định nghĩa 11.1 (Mô hình phân phối, mô hình mẫu, kinh nghiệm mô phỏng).** Mô hình phân phối: ánh xạ $(s,a)\mapsto\hat p(\cdot,\cdot\mid s,a)$; mô hình mẫu: thủ tục ngẫu nhiên trả một cặp $(R,S')$ có phân phối $\hat p(\cdot,\cdot\mid s,a)$; kinh nghiệm mô phỏng là dãy chuyển sinh từ mô hình. Móc nối: trường hợp riêng của "mô hình" ở Định nghĩa 01.14; mô hình phân phối mạnh hơn (luôn sinh được mẫu), mô hình mẫu dễ có hơn (SB tr. 160).
5. **Định nghĩa 11.2 (Lập kế hoạch nền, lập kế hoạch tại thời điểm quyết định).** Lập kế hoạch (trong không gian trạng thái) là quá trình nhận mô hình, trả hoặc cải thiện chính sách (SB tr. 160); nền: cải thiện bảng giá trị hoặc chính sách cho nhiều trạng thái trước khi gặp chúng; tại thời điểm quyết định: bắt đầu và kết thúc sau khi gặp $S_t$, đầu ra là $A_t$ (SB §8.8 tr. 180–181).
6. **Nhận xét 11.3 (Quy hoạch động là lập kế hoạch nền với mô hình phân phối).** Lượt quét của Thuật toán 04.28 và 04.31 dùng mô hình phân phối đã biết; Bài 11 bỏ giả thiết biết mô hình.

**2.2 Mô hình đếm và hai loại bất định** (`cốt lõi`).

1. Vấn đề: sau lượt thứ nhất, $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}5$ dựa trên hai mẫu; con số đó tin được đến đâu?
2. Trực quan: hai nguồn bất định khác bản chất: trượt là thuộc tính của môi trường (không giảm khi có thêm dữ liệu); sai lệch của $\hat p$ do ít dữ liệu (giảm khi có thêm dữ liệu).
3. **Ví dụ 11.3** (bảng đếm, mục 7.1).
4. **Định nghĩa 11.4 (Mô hình đếm).** $\hat p(s'\mid s,a)=C(s,a,s')/C(s,a)$, $\hat r(s,a)$ = trung bình phần thưởng của các lần thử, xác định khi $C(s,a)\ge1$. Móc nối: cùng tần suất $\hat r$, $\hat P$ của Mệnh đề 05.34 (cho cặp thay vì trạng thái); ước lượng hợp lý cực đại của phân phối phân loại (một câu, không chứng minh: kiến thức thống kê đã học; tác tử soạn kiểm có nên thêm hay bỏ câu này, VP21).
5. **Mệnh đề 11.5 (Kỳ vọng và phương sai của xác suất ước lượng).** Giả thiết: $C(s,a)=n\ge1$ cố định trước; các trạng thái kế của $n$ lần thử độc lập, cùng phân phối $p(\cdot\mid s,a)$ (môi trường dừng, Markov). Kết luận: với mọi $s'$, $\mathbb E[\hat p(s'\mid s,a)]=p(s'\mid s,a)$ và $\operatorname{Var}[\hat p(s'\mid s,a)]=p(1-p)/n$ với $p=p(s'\mid s,a)$. Điều kiện áp dụng: $n$ không phụ thuộc kết quả thử (khi tác tử chọn thử lại dựa trên kết quả, $n$ ngẫu nhiên và mệnh đề không áp dụng trực tiếp). Phạm vi: chỉ bảng; không nói về sai số của giá trị lập kế hoạch. **Chứng minh đầy đủ:** $C(s,a,s')$ là tổng $n$ biến Bernoulli độc lập.
6. **Ví dụ 11.4** (bảng $0{,}283$; $0{,}179$; $0{,}057$).
7. **Định nghĩa 11.6 (Bất định ngẫu nhiên, bất định nhận thức).** Bất định ngẫu nhiên (aleatoric uncertainty): phân phối $p(\cdot\mid s,a)$ của trạng thái kế, kể cả khi biết mô hình đúng; bất định nhận thức (epistemic uncertainty): sai lệch của $\hat p$ so với $p$ do dữ liệu hữu hạn. Phát biểu bằng hai đại lượng của Mệnh đề 11.5 cho trường hợp hai kết cục: $p(1-p)$ và $p(1-p)/n$. Nguồn định nghĩa: Chua và cộng sự (2018) (QG3); GC9: đọc định nghĩa, phản ví dụ (môi trường tất định: không có bất định ngẫu nhiên, vẫn có bất định nhận thức ở cặp chưa thử).
8. Nhầm lẫn thường gặp (GC11): coi $\hat p=1$ sau một lần thử là "chắc chắn" (cặp $(\mathrm B,\downarrow)$).

**2.3 Tập mô hình** (`bổ sung`).

- Vấn đề: mô hình đếm cho bất định nhận thức bằng công thức; mô hình là mạng nơ-ron thì không có công thức đó.
- **Ví dụ 11.5** (ba mô hình $0$; $0{,}5$; $1$; độ lệch chuẩn $0{,}408$).
- **Nhận xét 11.7 (Tập mô hình).** Mỗi mô hình học trên một lần lấy lại mẫu; độ phân tán giữa các dự báo dùng làm thước đo bất định nhận thức; giới hạn: cặp một mẫu cho độ phân tán $0$; dùng trong PETS (Chua và cộng sự 2018) cùng lập kế hoạch bằng phương pháp entropy chéo. Không phát biểu định lý. Tránh dùng chữ "bootstrap" trơn vì trùng "mục tiêu bootstrap" (VP-RL-3): viết "lấy lại mẫu có hoàn lại".

**2.4 Q-planning và kiến trúc Dyna** (`cốt lõi`).

1. Vấn đề: Ví dụ 11.1 cho thấy sau lượt thứ nhất chỉ một ô khác $0$.
2. Trực quan (NT-RL-3: mở bằng giới hạn của Q-learning trong một dòng): áp dụng chính quy tắc Q-learning lên mẫu do mô hình sinh.
3. **Ví dụ 11.6** (một cập nhật Q-planning: $0{,}225$).
4. **Thuật toán 11.8 (Q-planning một bước, chọn ngẫu nhiên, dạng bảng).** SB tr. 161. Đầu vào: mô hình mẫu, $\alpha$, $\gamma$; các bước: chọn $(S,A)$ ngẫu nhiên trong các cặp đã thử; lấy $(R,S')$ từ mô hình; cập nhật Q-learning; chi phí mỗi bước $O(\lvert\mathcal A\rvert)$.
5. **Mệnh đề 11.9 (Hội tụ của Q-planning).** Giả thiết: mô hình $\hat p$ cố định, xác định trên một tập cặp $\mathcal P$ đóng (mọi trạng thái kế có xác suất dương theo $\hat p$ đều có mọi hành động trong $\mathcal P$, hoặc là trạng thái kết thúc; cần kiểm cách phát biểu gọn nhất); phần thưởng của mô hình bị chặn; $0\le\gamma<1$; mỗi cặp của $\mathcal P$ được chọn vô hạn lần; bước học thỏa Định nghĩa 06.19. Kết luận: $Q\to\hat q_*$ hầu chắc chắn, với $\hat q_*$ là giá trị hành động tối ưu của MDP mà mô hình định nghĩa. Điều kiện áp dụng: mô hình không đổi trong lúc lập kế hoạch. Phạm vi: $\hat q_*$ có thể khác $q_*$ khi mô hình sai (Tình huống 11.2). **Chứng minh đầy đủ ngắn:** các mẫu do mô hình sinh thỏa giả thiết nền của Nhận xét 06.20 cho MDP của mô hình; áp dụng Định lý 06.21. Nguồn phát biểu: SB tr. 161.
6. **Ví dụ 11.7** (lượt thứ nhất của Dyna-Q, $0{,}5$ → $0{,}225$, $0{,}75$; so sánh $n=0$).
7. **Thuật toán 11.10 (Dyna-Q dạng bảng).** Hộp SB tr. 164 với các bước (a)–(f), kèm hình `kien-truc-dyna.svg` (vẽ lại SB Hình 8.1) và đoạn đọc hình: học trực tiếp, học mô hình, điều khiển tìm kiếm (search control), lập kế hoạch. Giả thiết ghi rõ: môi trường tất định (bước (e) ghi kết quả gần nhất). Chi phí mỗi bước thật: $O((n+1)\lvert\mathcal A\rvert)$.
8. **Nhận xét 11.11 (Dyna-Q, bộ nhớ phát lại và bảo đảm).** Bước (f) với mô hình lưu nguyên các bộ chuyển giống việc rút từ bộ nhớ phát lại (Định nghĩa 08.7) rồi cập nhật Q-learning; khác ở chỗ mô hình gộp các bộ chuyển theo cặp. Bảo đảm kế thừa: khi mô hình đúng và cố định, các cập nhật lập kế hoạch có tính chất của Mệnh đề 11.9; khi mô hình còn đổi (mỗi bước thật), không phát biểu định lý hội tụ cho Dyna-Q (không nguồn trong GC-RL-5).
9. **Trong thực hành** (GC-RL-9): đối tượng là bảng $Q$ và từ điển $\mathrm{Model}$; giả thiết tất định bị vi phạm khi môi trường có trượt (Tình huống 11.2); $n$ là núm điều chỉnh giữa chi phí tính toán và số bước thật (SB Hình 8.2: $n=0,5,50$).

**2.5 Mô hình sai và thưởng thăm dò** (`cốt lõi`).

1. Vấn đề: **Ví dụ 11.8** (mê cung đổi cửa; hai kiểu sai).
2. Trực quan: mô hình lạc quan bị chính sách tham lam kiểm lại; mô hình bi quan thì không (SB tr. 166–167).
3. **Định nghĩa 11.12 (Thưởng thăm dò của Dyna-Q+).** Trong bước lập kế hoạch, phần thưởng mô phỏng là $\hat r+\kappa\sqrt{\ell(s,a)}$; thêm hai thay đổi của chú thích 1 SB tr. 168 (cặp chưa thử được lập kế hoạch với mô hình "ở yên, phần thưởng $0$").
4. **Ví dụ 11.9** ($0{,}54\to0{,}64$, đổi hành động tham lam).
5. **Nhận xét 11.13 (Thăm dò trong lập kế hoạch).** Thưởng thăm dò làm $Q$ không còn ước lượng $q_*$ của mô hình (Mệnh đề 11.9 không áp dụng cho bảng có thưởng); đây là câu hỏi của Bài tập 11.19 (SB Bài tập 8.4). Không giải bài tập trong nhận xét.

**2.6 Cập nhật kỳ vọng và cập nhật mẫu** (`cốt lõi`).

1. Vấn đề: với mô hình đếm, $(\mathrm A,\rightarrow)$ có hai trạng thái kế; một cập nhật dùng cả phân phối tốn gấp đôi.
2. **Ví dụ 11.10** ($0{,}45$ so với $0{,}54$ / $0{,}36$).
3. **Định nghĩa 11.14 (Cập nhật kỳ vọng, cập nhật mẫu, hệ số phân nhánh).** SB §8.5 tr. 172–173, sơ đồ của SB Hình 8.6 thu gọn cho $Q$ tối ưu (chỉ dạng $q_*$).
4. **Mệnh đề 11.15 (Sai số của trung bình các cập nhật mẫu).** Giả thiết: giá trị tại trạng thái kế đúng và cố định ($x_{s'}=\hat r+\gamma\max_{a'}Q(s',a')$ không đổi); $k$ trạng thái kế rút độc lập theo $\hat p(\cdot\mid s,a)$; bước học $\alpha_j=1/j$ (ước lượng là trung bình của $k$ mục tiêu mẫu). Kết luận: (a) sai số bình phương trung bình bằng $\sigma^2/k$, với $\sigma^2=\sum_{s'}\hat p(s')(x_{s'}-\bar x)^2$; (b) nếu thêm $b$ trạng thái kế đồng khả năng và các giá trị $x_{s'}$ là biến ngẫu nhiên độc lập phương sai $1$ (mô hình bài toán ngẫu nhiên của SB Hình 8.7), thì $\mathbb E[\sigma^2]=(b-1)/b$ và sai số căn bình phương trung bình là $\sqrt{(b-1)/(bk)}$. Điều kiện áp dụng: cập nhật kỳ vọng cho sai số $0$ sau $b$ phép đánh giá. Phạm vi: giá trị kế trong bài toán thật cũng đang được cập nhật; SB tr. 174 cho rằng điều đó làm lợi thế của cập nhật mẫu còn lớn hơn (nêu như nhận định của nguồn, không như kết quả). **Chứng minh đầy đủ:** (a) phương sai của trung bình mẫu độc lập; (b) $\mathbb E[\frac1b\sum(x_i-\bar x)^2]=\frac{b-1}{b}$ (kỳ vọng của phương sai mẫu chia $b$). Người lập kế hoạch đã kiểm: với phân phối tổng quát $\hat p$, $\mathbb E[\sigma^2]=1-\sum\hat p_i^2$; dạng tổng quát này **không** đưa vào ghi chú vì là lời giải của Bài tập 11.14 (SB Bài tập 8.6).
5. **Ví dụ 11.11** (bảng $b$, $k$; $0{,}315$ với $b=100$, $k=10$) và hình `cap-nhat-ky-vong-va-mau.svg` (vẽ lại SB Hình 8.7 từ công thức).
6. **Nhận xét 11.16 (Khi nào chọn cập nhật mẫu).** Theo SB tr. 174: hệ số phân nhánh lớn và quá nhiều trạng thái để giải chính xác.

**2.7 Đọc thêm: phân bổ các cập nhật** (`đọc thêm`).

- **Nhận xét 11.17 (Quét ưu tiên).** SB §8.4: hàng đợi ưu tiên theo độ lớn thay đổi, lan ngược tới các cặp dẫn vào trạng thái vừa đổi; nối với lịch cập nhật bất đồng bộ của Định lý 04.32 (mọi trạng thái vẫn phải được cập nhật vô hạn lần để áp dụng định lý). Ví dụ 11.7 phần "kiểm" (thứ tự ngược cho $0{,}3375$) là động lực.
- **Nhận xét 11.18 (Lấy mẫu theo quỹ đạo).** SB §8.6: phân bổ cập nhật theo phân phối theo chính sách; Hình 8.8 nêu bằng lời, không chép số.
- **Định lý 11.19 (Hội tụ của RTDP).** **Dẫn** (Barto, Bradtke và Singh 1995, qua SB tr. 178): bài toán có kết thúc, không chiết khấu, trạng thái đích hấp thụ có phần thưởng $0$; bốn điều kiện (giá trị đầu tại đích bằng $0$; tồn tại chính sách tới đích với xác suất $1$ từ mọi trạng thái đầu; phần thưởng ở trạng thái không phải đích âm ngặt; giá trị đầu không nhỏ hơn giá trị tối ưu). Kết luận: hội tụ với xác suất $1$ tới chính sách tối ưu trên các trạng thái liên quan. Phạm vi: mê cung hai phòng với phần thưởng $+1$ ở đích không thỏa điều kiện thứ ba (nêu bằng nguyên nhân, VP18).
- **Kết mục §2 (GC15):** đã có Mệnh đề 11.5, 11.9, 11.15, Thuật toán 11.10; còn thiếu: lập kế hoạch nền tốn tính toán cho mọi trạng thái, kể cả trạng thái tác tử không đến gần; khi chỉ cần một quyết định tại trạng thái hiện tại, phép tính nên dồn vào đó.

### §3. Tìm kiếm theo cây Monte Carlo (mạch 3; giáo trình 11.2)

**3.1 Lập kế hoạch tại thời điểm quyết định và thuật toán rollout** (`cầu nối`: phát biểu lại giáo trình 4.3.1).

1. Vấn đề (mở thẳng bằng bài toán trên mê cung, GC-RL-2): tác tử đang ở $\mathrm F$, có mô hình mẫu đúng và một chính sách đơn giản $\pi_0$ (ngẫu nhiên đều), cần chọn một hành động.
2. Trực quan: thử từng hành động trong mô hình rồi đi tiếp theo $\pi_0$, lấy trung bình lợi tức (SB §8.10 tr. 183).
3. **Ví dụ 11.12** ($q_{\pi_0}(\mathrm F,\cdot)$; bảng $v_{\pi_0}$).
4. **Định nghĩa 11.20 (Thuật toán rollout, chính sách rollout).** Chính sách cơ sở $\pi_0$ (SB gọi là rollout policy); chính sách rollout $\pi_{\mathrm{ro}}(s)\in\arg\max_a q_{\pi_0}(s,a)$, ước lượng bằng $m$ mô phỏng mỗi hành động. Thuật ngữ: "chính sách rollout" theo mục lục giáo trình 4.3.1; phân biệt với "đoạn thu (rollout)" của Bài 10 bằng một câu (QG13). Cần chốt tên: SB gọi $\pi_0$ là "rollout policy"; Bertsekas gọi $\pi_0$ là "base policy" và chính sách cải thiện là "rollout policy". Đề xuất theo Bertsekas: $\pi_0$ là **chính sách cơ sở**, $\pi_{\mathrm{ro}}$ là **chính sách rollout**; ghi tương ứng với SB một lần (QG13).
5. **Mệnh đề 11.21 (Tính chất cải thiện của rollout).** Giả thiết: MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; $\pi_0$ Markov dừng; $q_{\pi_0}$ chính xác; $\pi_{\mathrm{ro}}$ tham lam theo $q_{\pi_0}$ tại **mọi** trạng thái. Kết luận: $v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$, nghiêm ngặt tại $s$ khi $\max_aq_{\pi_0}(s,a)>v_{\pi_0}(s)$. Điều kiện áp dụng: $q_{\pi_0}$ chính xác; với ước lượng Monte Carlo xem Mệnh đề 11.22. Phạm vi: không bảo đảm tối ưu (SB tr. 184: mục đích là cải thiện chính sách cơ sở, không tìm chính sách tối ưu). **Chứng minh đầy đủ** (là trường hợp của Định lý 04.13): $q_{\pi_0}(s,\pi_{\mathrm{ro}}(s))=\max_aq_{\pi_0}(s,a)\ge\sum_a\pi_0(a\mid s)q_{\pi_0}(s,a)=v_{\pi_0}(s)$, rồi áp dụng Định lý 04.13(a), (b). Đây là kết quả chính của mạch 3 có trang "Ý tưởng chứng minh" (QT4). Nhận xét móc nối: thuật toán rollout thực hành chỉ đổi hành động tại trạng thái hiện tại rồi lặp lại ở trạng thái sau, nên chính sách thật sự được thực hiện chính là $\pi_{\mathrm{ro}}$ (mỗi trạng thái gặp đều dùng cùng quy tắc); giống một bước lặp chính sách (SB tr. 184).
6. **Ví dụ 11.13** ($0{,}2016\to0{,}8566$).
7. **Mệnh đề 11.22 (Xác suất chọn sai của rollout với $m$ mô phỏng).** Giả thiết: hai hành động $a$, $a'$ với $\Delta=q_{\pi_0}(s,a)-q_{\pi_0}(s,a')>0$; $2m$ lợi tức mô phỏng độc lập, mỗi lợi tức trong đoạn độ rộng $B$; $m$ cố định trước. Kết luận: $\Pr\{\bar G(a')\ge\bar G(a)\}\le\exp(-m\Delta^2/B^2)$. Điều kiện áp dụng: mô hình đúng; mô phỏng độc lập. Phạm vi: với nhiều hành động dùng chặn hợp; không áp dụng khi $m$ chọn theo kết quả (dừng thích nghi). **Chứng minh đầy đủ:** Hoeffding một phía (tiên quyết 8) cho tổng $2m$ biến $G_i(a)$ và $-G_j(a')$, độ lệch $t=m\Delta$: $\exp(-2m^2\Delta^2/(2mB^2))$.
8. **Ví dụ 11.14** ($m=70$).
9. **Trong thực hành:** mô phỏng độc lập nên chạy song song được; có thể cắt mô phỏng sớm và cộng giá trị ước lượng (SB tr. 185); thời gian quyết định giới hạn $m$.

**3.2 Chọn hành động theo cận tin cậy trên** (`cầu nối`: phát biểu lại giáo trình 4.7.1–4.7.2).

1. Vấn đề: rollout chia đều $m$ mô phỏng cho mọi hành động, kể cả hành động đã thấy rõ là kém ($\uparrow$ tại $\mathrm F$).
2. Trực quan: lựa chọn tại gốc là bài toán chọn lặp lại một bước (Định nghĩa 01.16); ưu tiên hành động có trung bình cao hoặc còn ít mẫu.
3. **Ví dụ 11.15** ($1{,}1887$ và $1{,}4197$).
4. **Định nghĩa 11.23 (Quy tắc cận tin cậy trên).** $A=\arg\max_a\bigl[\bar r(a)+c_{\mathrm{ucb}}\sqrt{\ln t/N(a)}\bigr]$, $N(a)=0$ được coi là cực đại (SB (2.10), tr. 35–36); UCB1 là trường hợp $c_{\mathrm{ucb}}=\sqrt2$ với phần thưởng trong $[0,1]$.
5. **Định lý 11.24 (Chặn hối tiếc của UCB1).** **Dẫn** (Auer, Cesa-Bianchi và Fischer 2002, Định lý 1; cần kiểm số trang). Giả thiết: $K$ hành động, phần thưởng độc lập theo thời gian, trong $[0,1]$, phân phối của mỗi hành động không đổi. Kết luận: số lần chọn kỳ vọng của hành động kém $a$ sau $t$ lần không vượt $8\ln t/\Delta_a^2+1+\pi^2/3$, nên hối tiếc kỳ vọng tăng theo $\ln t$. Điều kiện áp dụng, phạm vi: không áp dụng khi phân phối đổi theo thời gian (SB tr. 36 nêu khó khăn với bài toán không dừng), điều xảy ra ở các nút trong của cây (dẫn sang 3.4). Ý tưởng chứng minh: một đoạn (hành động kém bị chọn khi cận trên của nó vượt cận trên của hành động tốt nhất, và Hoeffding chặn xác suất của biến cố đó). Cần kiểm hằng số chính xác trong bài báo trước khi viết.
6. **Nhận xét** (gộp vào đoạn văn, không khối riêng): SB Hình 2.4 và hiện tượng "đỉnh ở bước 11" là Bài tập 11.18 (SB Bài tập 2.8); không giải trong ghi chú.

**3.3 Bốn pha của tìm kiếm theo cây Monte Carlo** (`cốt lõi`).

1. Vấn đề: rollout không nhớ gì giữa các mô phỏng; mô phỏng tốt nên được dùng để hướng các mô phỏng sau (SB tr. 185).
2. Trực quan: giữ một cây gốc $\mathrm F$, trong cây chọn bằng chỉ số cận tin cậy trên, ngoài cây dùng chính sách rollout.
3. **Ví dụ 11.16** (một vòng; bảng chỉ số; $G=0{,}729$; $\bar Q(\mathrm F,\uparrow)=0{,}5145$) với hình `mcts-bon-pha.svg`.
4. **Định nghĩa 11.25 (Cây tìm kiếm, chính sách cây, chính sách rollout, thống kê cạnh).** Nút là trạng thái gặp trong mô phỏng; mỗi cạnh $(s,a)$ giữ $N(s,a)$, $W(s,a)$; $\bar Q=W/N$; chính sách cây UCT: chỉ số $\bar Q(s,a)+c_{\mathrm{ucb}}\sqrt{\ln N(s)/N(s,a)}$.
5. **Thuật toán 11.26 (MCTS với UCT).** Đầu vào: trạng thái hiện tại, mô hình mẫu, chính sách rollout, $c_{\mathrm{ucb}}$, ngân sách vòng lặp; các bước: chọn, mở rộng, mô phỏng, cập nhật ngược (SB tr. 187); đầu ra: hành động ở gốc có $N$ lớn nhất (hoặc $\bar Q$ lớn nhất, SB tr. 187); dùng lại cây con của trạng thái kế (SB tr. 187). Chi phí mỗi vòng: độ sâu cây cộng độ dài mô phỏng. Ghi chú cho tác tử soạn: lợi tức cập nhật ngược cho cạnh ở độ sâu $j$ là lợi tức chiết khấu tính từ cạnh đó (Ví dụ 11.16 chỉ có một cạnh trong cây).
6. **Trong thực hành:** mô hình mẫu phải nhanh (SB tr. 185); MCTS không cần xấp xỉ hàm toàn cục (SB tr. 188).

**3.4 Bảo đảm của UCT và giá trị học được** (`cốt lõi` cho định lý; `bổ sung` cho nhận xét).

- **Định lý 11.27 (Tính nhất quán của UCT).** **Dẫn** (Kocsis và Szepesvári 2006). Giả thiết: MDP chân trời hữu hạn $D$, hữu hạn hành động, phần thưởng chuẩn hóa trong $[0,1]$, hệ số của số hạng thăm dò được nhân theo độ sâu như bài báo yêu cầu. Kết luận: độ chệch của ước lượng giá trị tại gốc là $O(\ln n/n)$ theo số vòng $n$; xác suất chọn sai tại gốc tiến về $0$ với tốc độ đa thức. **Cần kiểm** số định lý, cách phát biểu hằng số và giả thiết tất định hay ngẫu nhiên trước khi viết; nếu không kiểm được, chỉ giữ câu định tính có nguồn và bỏ bậc $O(\ln n/n)$. Ý tưởng chứng minh: mỗi nút là bài toán chọn lặp lại không dừng (giá trị của cạnh trôi khi cây con thay đổi), quy nạp theo độ sâu từ lá lên gốc.
- **Nhận xét 11.28 (Xác suất tiên nghiệm và giá trị học được: AlphaGo Zero).** SB §16.6.2 tr. 447–449: mạng cho xác suất tiên nghiệm của hành động và giá trị của nút lá, thay mô phỏng ngẫu nhiên; MCTS dùng làm toán tử cải thiện chính sách khi tự chơi. Quy tắc chọn có số hạng tiên nghiệm (Silver và cộng sự 2017, phần Methods; cần kiểm dạng công thức trước khi viết công thức, nếu không thì chỉ nêu bằng lời). Không câu về "hệ thống thắng nhà vô địch" ngoài dữ kiện của SB tr. 441 (VP6). Không nhắc MuZero (giới hạn chương, VP20).
- **Trong thực hành** (GC-RL-9): khi trạng thái chỉ quan sát được một phần hoặc mô hình là mạng học được, giả thiết "mô hình đúng" của Mệnh đề 11.21 và Định lý 11.27 không còn; MCTS vẫn chạy nhưng bảo đảm không áp dụng.
- **Kết mục §3:** MCTS cần tập hành động hữu hạn để liệt kê cạnh và một mô hình mẫu nhanh; với hành động liên tục (xe trên đường ray) không liệt kê được, nhưng nếu mô hình khả vi thì đạo hàm cho hướng sửa kế hoạch.

### §4. Tối ưu kế hoạch dựa trên đạo hàm (mạch 4; giáo trình 11.3)

**4.1 Bài toán tối ưu kế hoạch trên mô hình khả vi** (`cốt lõi`). Mở thẳng bằng **Ví dụ 11.17** (xe trên đường ray, $J(0,0)=8$). **Định nghĩa 11.29 (Bài toán tối ưu kế hoạch chân trời $h$, phép bắn).** Biến quyết định là chuỗi hành động $u_{0:h-1}$; trạng thái được thế bằng mô hình $x_{t+1}=\hat f(x_t,u_t)$ (phép bắn đơn, single shooting); cực tiểu $J=\sum_{t=0}^{h-1}c(x_{t+1},u_t)$. Móc nối: khác bài toán MDP của Bài 03 ở chỗ tìm một chuỗi hành động cho một trạng thái đầu (vòng hở), không tìm chính sách; hành động liên tục.

**4.2 Đạo hàm qua mô hình** (`cốt lõi`).

- **Ví dụ 11.18** (gradient $(8,4)$, $J=2{,}88$) đứng trước thuật toán.
- **Mệnh đề 11.30 (Gradient theo chuỗi hành động bằng truy hồi ngược).** Giả thiết: $\hat f$, $c$ khả vi liên tục. Kết luận: với $\lambda_h=\partial c(x_h,u_{h-1})/\partial x_h$ và $\lambda_t=\partial c(x_t,u_{t-1})/\partial x_t+\lambda_{t+1}\,\partial\hat f(x_t,u_t)/\partial x_t$ ($t=h-1,\dots,1$), ta có $\partial J/\partial u_t=\partial c(x_{t+1},u_t)/\partial u_t+\lambda_{t+1}\,\partial\hat f(x_t,u_t)/\partial u_t$. Điều kiện áp dụng: tính một lượt xuôi rồi một lượt ngược, chi phí $O(h)$ lần đạo hàm của $\hat f$. Phạm vi: gradient của $J$ trên **mô hình**; điểm dừng có thể là cực tiểu địa phương khi $\hat f$ phi tuyến. **Chứng minh đầy đủ** bằng quy tắc dây chuyền (quy nạp ngược theo $t$); nối với lan truyền ngược (Goodfellow và cộng sự 2016, §6.5). Dạng một chiều; tác tử soạn có thể viết dạng vector nếu không làm nặng ký hiệu (đề xuất: giữ một chiều, một câu nêu dạng ma trận Jacobi).
- **Thuật toán 11.31 (Tối ưu kế hoạch bằng hạ gradient).** Khởi tạo $u$, lặp: lượt xuôi, lượt ngược (Mệnh đề 11.30), $u\leftarrow u-\eta\nabla J$; dừng khi $\lVert\nabla J\rVert\le\theta$ hoặc hết ngân sách. Chi phí mỗi vòng $O(h)$.
- **Ví dụ 11.19** (nghiệm tối ưu, $J^*=2{,}4$, Hessian xác định dương).
- Nhận xét móc nối (đoạn văn): PILCO (Deisenroth và Rasmussen 2011) tối ưu tham số chính sách bằng gradient qua mô hình xác suất; chỉ nêu một câu có nguồn, không chi tiết (`đọc thêm`).

**4.3 Điều khiển dự báo theo chân trời lùi** (`cầu nối`: phát biểu lại giáo trình 4.3.2).

- Vấn đề: kế hoạch vòng hở tính một lần không phản ứng với trạng thái thật.
- **Định nghĩa 11.32 (Điều khiển dự báo theo chân trời lùi, MPC).** Tại mỗi $t$: giải bài toán của Định nghĩa 11.29 từ $x_t$, thực hiện $u_t$ đầu tiên, bỏ phần còn lại. Nguồn: Bertsekas (2019), mục điều khiển dự báo (cần kiểm §2.5).
- **Ví dụ 11.20** ($u=-0{,}6x$; $2;\ 0{,}8;\ 0{,}32;\ 0{,}128$).
- **Thuật toán 11.33 (Điều khiển dự báo).** Bao Thuật toán 11.31 (hoặc 11.34) trong vòng lặp thời gian; khởi động ấm bằng phần đuôi của kế hoạch trước (một câu, cần nguồn: Bertsekas 2019 hoặc bỏ).
- Móc nối: MPC là lập kế hoạch tại thời điểm quyết định cho hành động liên tục, như rollout và MCTS cho hành động rời rạc (Định nghĩa 11.2).

**4.4 Bắn ngẫu nhiên và phương pháp entropy chéo** (`bổ sung`).

- Vấn đề: mô hình không khả vi (bảng, mô phỏng hộp đen) hoặc $J$ nhiều cực tiểu địa phương.
- **Ví dụ 11.21** (bốn ứng viên; mẫu ưu tú; trung bình mới).
- **Thuật toán 11.34 (Tối ưu kế hoạch bằng phương pháp entropy chéo).** Rút $M$ chuỗi từ phân phối chuẩn theo tọa độ, đánh giá $J$ trên mô hình, giữ $M_{\mathrm e}$ chuỗi tốt nhất, khớp lại trung bình và độ lệch chuẩn, lặp. Không phát biểu định lý hội tụ (không có nguồn trong GC-RL-5); nguồn mô tả: Chua và cộng sự (2018) (QG3).
- **Nhận xét 11.35 (Đạo hàm hay lấy mẫu).** So sánh bằng bảng: yêu cầu về mô hình, số lần gọi mô hình mỗi vòng ($O(h)$ cộng lượt ngược so với $M$ lượt xuôi), nhạy với cực tiểu địa phương.

**4.5 Sai số mô hình tích lũy** (`cốt lõi`).

- Vấn đề: **Ví dụ 11.22** (bảng $e_k$).
- **Mệnh đề 11.36 (Chặn sai số dự báo $k$ bước).** Giả thiết: $f$ Lipschitz theo $x$ với hằng số $L$ (với mọi $u$); $\lvert f(\hat x_j,u_j)-\hat f(\hat x_j,u_j)\rvert\le\bar e$ tại các trạng thái dự báo $\hat x_j$, $j<k$; cùng chuỗi hành động; cùng $x_0$. Kết luận: $e_k=\lvert x_k-\hat x_k\rvert\le\bar e\sum_{j=0}^{k-1}L^j$, bằng $\bar e(L^k-1)/(L-1)$ khi $L\ne1$ và $k\bar e$ khi $L=1$. Điều kiện áp dụng: chuỗi hành động cố định (vòng hở). Phạm vi: chặn tăng theo cấp số nhân khi $L>1$; không áp dụng trực tiếp cho vòng kín. **Chứng minh đầy đủ:** $e_{j+1}\le\lvert f(x_j,u_j)-f(\hat x_j,u_j)\rvert+\lvert f(\hat x_j,u_j)-\hat f(\hat x_j,u_j)\rvert\le Le_j+\bar e$, quy nạp. Kết quả phụ (một dòng "Chứng minh." trên trang chiếu, QT4).
- **Ví dụ 11.23** (vòng hở $1{,}2$; $1{,}04$ so với điều khiển dự báo $2;\ 1{,}2;\ 0{,}72;\ 0{,}432$).
- **Nhận xét 11.37 (Tính bất định khi lập kế hoạch liên tục).** Lập kế hoạch qua tập mô hình (Nhận xét 11.7) hoặc mô hình xác suất (PILCO) để tránh khai thác chỗ mô hình sai; một đến hai câu có nguồn (`đọc thêm`).
- **Trong thực hành:** chân trời $h$ dài làm sai số tích lũy lớn và gradient qua nhiều lần nhân $\partial\hat f/\partial x$ dễ bùng nổ hoặc tiêu biến (một câu, nguồn: Goodfellow và cộng sự 2016, §10.7 về gradient qua chuỗi dài; cần kiểm số mục). Không nhắc mô hình thế giới học từ ảnh (VP20); nếu cần, "Phạm vi." của Mệnh đề 11.36 nói "mô hình là hàm tường minh của trạng thái quan sát được".
- **Kết mục §4:** gradient và MPC cho hành động liên tục ở bước thời gian nhỏ; để nhìn xa, kế hoạch phải đi qua nhiều bước, sai số tích lũy và chi phí tăng theo $h$. Cần một đơn vị hành động kéo dài nhiều bước.

### §5. Học tăng cường phân cấp (mạch 5; giáo trình 11.4)

**5.1 Tùy chọn và chính sách phân cấp** (`cốt lõi`; giáo trình 11.4.1).

1. Vấn đề (mở thẳng trên mê cung): lặp giá trị trên hành động một bước cần nhiều lượt quét để giá trị của $\mathrm Z$ lan về $\mathrm A$ (bảng của Ví dụ 11.26: sau sáu lượt quét $v(\mathrm A)=0{,}6103$, còn cách $v_*(\mathrm A)=0{,}6604$); con người lập kế hoạch "ra cửa rồi tới đích".
2. Trực quan: SB tr. 461 (các thang thời gian khác nhau của cùng một MDP), một đoạn.
3. **Ví dụ 11.24** (hai tùy chọn trên mê cung).
4. **Định nghĩa 11.38 (Tùy chọn).** Bộ ba $\omega=\langle\mathcal I_\omega,\pi_\omega,\beta_\omega\rangle$: tập khởi đầu, chính sách Markov, hàm kết thúc; thực hiện: chọn $A_t\sim\pi_\omega(\cdot\mid S_t)$, kết thúc tại $t+1$ với xác suất $\beta_\omega(S_{t+1})$; $\tau$ là bước kết thúc. Hành động một bước là tùy chọn với $\pi_\omega(s)=a$, $\beta_\omega\equiv1$ (SB tr. 462 viết bằng $\gamma_\omega\equiv0$). Nguồn: Sutton, Precup và Singh (1999); SB §17.2. Đọc định nghĩa, phản ví dụ (GC9): tùy chọn có $\beta_\omega\equiv0$ trên một vùng không ra được thì không bao giờ kết thúc; giả thiết cần thêm: tùy chọn kết thúc với xác suất $1$ (ghi rõ trong định nghĩa hoặc giả thiết của các kết quả sau).
5. **Định nghĩa 11.39 (Chính sách phân cấp, giá trị tùy chọn).** $\mu(\omega\mid s)$ trên $\Omega(s)=\{\omega:s\in\mathcal I_\omega\}$; chạy tùy chọn được chọn tới khi kết thúc rồi chọn tiếp; $v_\mu(s)$, $q_\mu(s,\omega)$ là lợi tức kỳ vọng.
6. Móc nối: chính sách phân cấp sinh ra một chính sách (không Markov theo trạng thái nói chung, vì phụ thuộc tùy chọn đang chạy) trên MDP gốc; khác "hành động" ở chỗ kéo dài nhiều bước.

**5.2 Mô hình tùy chọn và bán-MDP** (`cốt lõi`; giáo trình 11.4.1).

1. **Ví dụ 11.25** (mô hình của $\omega_{\mathrm{cửa}}$ từ $\mathrm F$, $\mathrm B$, $\mathrm A$: $0{,}878$; $0{,}771$; $0{,}677$; của $\omega_{\mathrm{đích}}$ từ $\mathrm K$: $r=0{,}9756$).
2. **Định nghĩa 11.40 (Mô hình tùy chọn).** $r(s,\omega)$ theo SB (17.2), $p(s'\mid s,\omega)=\sum_{k\ge1}\gamma^k\Pr\{S_k=s',\tau=k\}$ theo SB (17.3), tr. 462. Đọc: $p$ không phải xác suất, đã chứa chiết khấu.
3. **Mệnh đề 11.41 (Tổng hệ số chuyển của mô hình tùy chọn).** Giả thiết: tùy chọn kết thúc với xác suất $1$, $0\le\gamma<1$. Kết luận: $\sum_{s'}p(s'\mid s,\omega)=\mathbb E[\gamma^\tau\mid S_0=s]\le\gamma$. **Chứng minh đầy đủ** ($\tau\ge1$). Dùng ở Định lý 11.44.
4. **Định lý 11.42 (Phương trình Bellman cho chính sách phân cấp).** Giả thiết: MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$; mọi tùy chọn có $\pi_\omega$ Markov, $\beta_\omega$ chỉ phụ thuộc trạng thái, kết thúc với xác suất $1$; $\mu$ Markov theo trạng thái tại các thời điểm chọn. Kết luận: $v_\mu(s)=\sum_{\omega\in\Omega(s)}\mu(\omega\mid s)\bigl[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)v_\mu(s')\bigr]$ (SB (17.4), tr. 463). Điều kiện áp dụng: khi $\Omega(s)$ chỉ gồm hành động một bước, công thức trở về phương trình Bellman kỳ vọng (Định lý 03.21) với $\gamma$ nằm trong $p$. Phạm vi: không áp dụng khi tùy chọn có kết thúc phụ thuộc lịch sử (tùy chọn bán-Markov, Sutton, Precup và Singh 1999). **Chứng minh: đầy đủ** theo bốn bước — (1) tách lợi tức tại $\tau$: $G_0=\sum_{k=1}^{\tau}\gamma^{k-1}R_k+\gamma^\tau G_\tau$; (2) kỳ vọng phần đầu là $r(s,\omega)$; (3) có điều kiện theo $(\tau,S_\tau)$, phần sau có kỳ vọng $v_\mu(S_\tau)$ nhờ tính Markov tại thời điểm dừng $\tau$ (mở rộng Bổ đề 03.20; tác tử soạn kiểm mức chặt và có thể ghi "tính Markov mạnh" kèm một câu lý do: $\tau$ là thời điểm dừng vì $\beta_\omega$ chỉ phụ thuộc trạng thái); (4) gom theo $\mu$. Kết quả chính của mạch 5 có trang "Ý tưởng chứng minh" (QT4).
5. **Nhận xét 11.43 (Bán-MDP).** Nhìn ở các thời điểm chọn tùy chọn, quá trình là quá trình quyết định bán-Markov (semi-Markov decision process, SMDP): thời gian lưu trú ngẫu nhiên; định lý "MDP + tùy chọn = SMDP" của Sutton, Precup và Singh (1999) (dẫn, cần kiểm số định lý); Puterman (1994, chương bán-MDP) cho lý thuyết tổng quát (cần kiểm số chương). Thuật ngữ mục lục giáo trình: "mô hình bán-MDP".

**5.3 Lập kế hoạch ở nhiều mức trừu tượng thời gian** (`cốt lõi`; giáo trình 11.4.2).

1. **Ví dụ 11.26** (hai vòng lặp giá trị với tùy chọn so với bảng sáu lượt quét).
2. **Định lý 11.44 (Hội tụ của lặp giá trị với tùy chọn).** Giả thiết: như Định lý 11.42; $\Omega(s)\ne\emptyset$ với mọi $s$; mô hình tùy chọn đúng. Kết luận: (a) toán tử $(T_\Omega v)(s)=\max_{\omega\in\Omega(s)}[r(s,\omega)+\sum_{s'}p(s'\mid s,\omega)v(s')]$ co với hệ số $\gamma$; (b) lặp $v_{k+1}=T_\Omega v_k$ hội tụ tới điểm bất động duy nhất $v_\Omega$, giá trị của chính sách phân cấp tốt nhất trên $\Omega$ (SB tr. 463); (c) nếu $\Omega(s)\supseteq\mathcal A(s)$ (hành động một bước như tùy chọn) với mọi $s$ thì $v_\Omega=v_*$. Điều kiện áp dụng, phạm vi: với $\Omega$ chỉ gồm tùy chọn, $v_\Omega\le v_*$ và có thể nhỏ hơn ngặt. **Chứng minh:** (a), (b) **đầy đủ** (Mệnh đề 11.41 cho hệ số co; Bổ đề 04.23 cho phép max; Định lý 04.5); phần "$v_\Omega$ là giá trị tối ưu trên các chính sách phân cấp" và (c) **dẫn** Sutton, Precup và Singh (1999) (cần kiểm) cùng SB tr. 463; ý tưởng một đoạn.
3. **Thuật toán 11.45 (Lặp giá trị với tùy chọn).** Đầu vào: mô hình tùy chọn; các bước như Thuật toán 04.28 với $T_\Omega$; chi phí mỗi lượt quét $O(\sum_s\lvert\Omega(s)\rvert\cdot\lvert\mathcal S\rvert)$. Nhận xét chi phí: tính mô hình tùy chọn cũng tốn; lợi ích đến khi dùng lại mô hình cho nhiều bài toán (một câu, SB tr. 463).
4. **Ví dụ 11.27** (một cập nhật Q-learning bán-MDP: $0{,}32805$).
5. **Thuật toán 11.46 (Q-learning bán-MDP).** Cập nhật khi tùy chọn kết thúc: $Q(s,\omega)\leftarrow Q(s,\omega)+\alpha[\sum_{j=1}^{k}\gamma^{j-1}R_j+\gamma^k\max_{\omega'}Q(S_k,\omega')-Q(s,\omega)]$. Nguồn: Sutton, Precup và Singh (1999) (cần kiểm số mục và định lý hội tụ; nếu định lý được kiểm, thêm một câu dẫn; nếu không, không phát biểu hội tụ, GC21). SB tr. 462 nêu ý "nhảy từ lúc bắt đầu tới lúc kết thúc tùy chọn".
6. **Nhận xét** gộp vào đoạn: tùy chọn chỉ giúp khi được chọn tốt; tùy chọn sai mục tiêu làm $v_\Omega<v_*$ (Bài tập 11.9 hoặc tình huống tùy chọn, QG12).
7. **Trong thực hành:** tùy chọn thường do người thiết kế viết tay (như "đi tới cửa") hoặc học được; mô hình tùy chọn phải học (5.4).

**5.4 Đọc thêm: học mô hình tùy chọn** (`đọc thêm`). **Nhận xét 11.47 (Học mô hình tùy chọn và học trong tùy chọn).** SB tr. 463: mô hình tùy chọn là các hàm giá trị tổng quát (SB §17.1, tr. 459–461) với tín hiệu tích lũy $C_t=R_t$ và kết thúc $\gamma\cdot\gamma_\omega$; phần chuyển cần một hàm cho mỗi trạng thái kết thúc; học trong tùy chọn cần học khác chính sách (SB tr. 462). Văn xuôi, không công thức mới ngoài một dòng.

**Kết mục §5 → §6.** Không có kết mục kiểu nối tiếp; §6 tổng hợp.

### §6. Tổng kết (mạch 6; giáo trình 11.5)

- **6.1 So sánh bốn cách dùng mô hình.** Bảng `Phương pháp | Mô hình cần có | Khi nào tính | Đầu ra | Bảo đảm (số hiệu) | Sai số mô hình ảnh hưởng thế nào`, bốn hàng: Dyna-Q (11.10, 11.9), MCTS (11.26, 11.21, 11.27), tối ưu bằng đạo hàm và MPC (11.31, 11.33, 11.36), lặp giá trị với tùy chọn (11.45, 11.44). Bảng này là nguồn của hai bảng P4 trên deck.
- **6.2 Trả lời bài toán trung tâm.** Bốn câu trả lời có điều kiện của mục 2 (văn xuôi, có số hiệu và số liệu).
- **6.3 Câu hỏi tự kiểm tra.** Ba đến bốn câu, mỗi câu kiểm một giả thiết hoặc một phân biệt (NT-RL-9), trả lời được chỉ bằng ghi chú; lời đáp ngắn ngay sau mỗi câu hoặc trong khối `solution`. Dự thảo:
  1. Mệnh đề 11.9 bảo đảm Dyna-Q hội tụ tới $q_*$ của môi trường hay của mô hình? (giả thiết: mô hình cố định và đúng).
  2. Vì sao tập mô hình không phát hiện bất định ở cặp chỉ có một mẫu? (Nhận xét 11.7).
  3. Mệnh đề 11.21 còn đúng không khi $q_{\pi_0}$ được thay bằng trung bình của $m=5$ mô phỏng? (điều kiện áp dụng; Mệnh đề 11.22).
  4. Khi tập tùy chọn không chứa hành động một bước, lặp giá trị với tùy chọn hội tụ tới đâu? (Định lý 11.44(b), (c)).
- Câu nối sang bài sau: theo QG7.

## 9. Tình huống áp dụng và ứng dụng (GC24, GC-RL-8: ít nhất hai, một tình huống giả thiết không thỏa)

| Mã | Tên dự kiến | Giả thiết | Kết quả dùng (dẫn ngược, GC14) | Số liệu (mục 7) |
|---|---|---|---|---|
| Tình huống 11.1 | Điều khiển dự báo cho xe trên đường ray với mô hình học bằng bình phương tối thiểu | thỏa: lớp mô hình tuyến tính chứa hệ thật, dữ liệu không nhiễu | Định nghĩa 11.29, 11.32; Mệnh đề 11.30; Thuật toán 11.33; so với Ví dụ 11.23 (mô hình $a=1$) | $\hat a=1{,}2$, $\hat b=1$; $u=-0{,}758824x$; $2;\ 0{,}882353;\ 0{,}389273;\ 0{,}171738$ |
| Tình huống 11.2 | Dyna-Q với mô hình tất định trên mê cung có trượt | **không thỏa**: Thuật toán 11.10 giả thiết môi trường tất định; trượt $0{,}2$ | Thuật toán 11.10; Mệnh đề 11.9 (hội tụ tới $\hat q_*$ của mô hình sai); Định nghĩa 11.4 (cách sửa) | lưu kết quả thành công: $\hat v$ = $1;\ 0{,}9;\ 0{,}81;\ 0{,}729$ so với $v_*$ = $0{,}9756;\ 0{,}8566;\ 0{,}7522;\ 0{,}6604$; chênh tại $\mathrm A$: $0{,}0686$. Lưu kết quả trượt cho $(\mathrm A,\rightarrow)$: mô hình nói $\rightarrow$ tại $\mathrm A$ không đi đâu, $Q(\mathrm A,\rightarrow)\to\gamma\max_aQ(\mathrm A,a)$, tác tử chọn $\downarrow$ (vẫn là một đường ngắn nhất) |
| Tình huống 11.3 (tùy chọn, QG12) | Tùy chọn viết cho đích cũ khi đích đổi | không thỏa: tập tùy chọn không chứa chính sách tối ưu mới | Định lý 11.44(b), (c) | tác tử soạn dựng và tính; chỉ thêm nếu tác giả đồng ý |

Phần "Ứng dụng" (cuối mục, `AGENTS.md` dòng 463 đã bị thay theo mục 6 của `NGUYEN-TAC-HOC-PHAN.md`): không liệt kê bài sau; chỉ một đoạn ngắn nêu chỗ các khái niệm của chương xuất hiện trong ứng dụng có nguồn (MCTS trong AlphaGo, AlphaGo Zero: SB §16.6; mô hình tập hợp trong PETS: Chua và cộng sự 2018), mỗi chỗ một câu.

## 10. Tóm tắt chương (GC-RL-3)

- **Đoạn kể 5–8 câu** có số hiệu: câu hỏi xuất phát (mẫu thật đắt, phép tính rẻ); mô hình đếm và hai loại bất định (Định nghĩa 11.4, 11.6, Mệnh đề 11.5); Dyna-Q dùng lại mẫu (Thuật toán 11.10, Mệnh đề 11.9) và Dyna-Q+ khi mô hình sai (Định nghĩa 11.12); lập kế hoạch tại thời điểm quyết định bằng rollout và MCTS (Mệnh đề 11.21, Thuật toán 11.26, Định lý 11.27); hành động liên tục với gradient qua mô hình và MPC (Mệnh đề 11.30, Định nghĩa 11.32), cái giá là sai số tích lũy (Mệnh đề 11.36); tùy chọn rút ngắn chân trời lập kế hoạch (Định lý 11.42, 11.44); giới hạn còn lại: mọi bảo đảm là theo mô hình.
- **Định nghĩa và kết quả theo mục:** mỗi mục §2–§5 một gạch đầu dòng.
- **Công thức cần nhớ** (hiển thị): mô hình đếm; $\operatorname{Var}\hat p=p(1-p)/n$; cập nhật Dyna-Q+ với $\kappa\sqrt\ell$; $\sqrt{(b-1)/(bk)}$; chỉ số UCT; $\exp(-m\Delta^2/B^2)$; truy hồi ngược $\lambda_t$; $\bar e(L^k-1)/(L-1)$; (17.2)–(17.4) dạng ghi chú; mục tiêu Q-learning bán-MDP.
- **Giả thiết hay bị bỏ quên:** mô hình cố định và đúng (Mệnh đề 11.9); $q_{\pi_0}$ chính xác (Mệnh đề 11.21); $m$ chọn trước (Mệnh đề 11.22); phần thưởng trong $[0,1]$ và chân trời hữu hạn (Định lý 11.24, 11.27); chuỗi hành động cố định, sai số đo trên quỹ đạo dự báo (Mệnh đề 11.36); tùy chọn kết thúc với xác suất $1$, kết thúc chỉ phụ thuộc trạng thái (Định lý 11.42); $\Omega(s)\supseteq\mathcal A(s)$ mới có $v_\Omega=v_*$ (Định lý 11.44); chiết khấu $\gamma^k$ theo số bước thật (Thuật toán 11.46).

## 11. Bài tập củng cố (BT-RL-5; chi tiết trong `ke-hoach-bai-tap.md`)

- Ba tiểu mục `### Mức nhận biết` (11.1–11.3), `### Mức tính toán hoặc chứng minh` (11.4–11.8), `### Mức vận dụng` (11.9–11.11); mỗi bài có `hint` và `solution`, lời giải chia câu, kết bằng dòng kiểm tra (BT5, GC4). Đề tự chứa (BT6, GC23).
- Mỗi mục tiêu học tập có ít nhất một bài trong ghi chú hoặc `exercises.md` (BT9; bảng phủ ở `ke-hoach-bai-tap.md` mục 4).
- Không bài tập cuối mục (đề xuất mở rộng BT-RL-6 cho Bài 11, QG4).
- Câu cuối mục: một câu và liên kết tới `exercises.md` (Bài tập 11.12–11.19), như ghi chú 06, 10.

## 12. Phân loại chủ đề (GC-RL-12; sẽ chép sang `outline.md`, mục "Phân loại chủ đề"; không đặt trong ghi chú, GC17)

| `note-topic-id` | Chủ đề | Nhóm | Lý do, nguồn |
|---|---|---|---|
| `lec-11-topic-01` | Kiến thức tiên quyết | cầu nối | nhắc 01.14, 01.16, 03–06, 08 |
| `lec-11-topic-02` | Kết quả kế thừa và bài toán trung tâm | cốt lõi | SB §8.2 Ví dụ 8.1 |
| `lec-11-topic-03` | Ba cách dùng mô hình | cốt lõi | SB §8.1 tr. 160 |
| `lec-11-topic-04` | Mô hình phân phối, mô hình mẫu; lập kế hoạch nền và tại thời điểm quyết định | cốt lõi | SB §8.1, §8.8 |
| `lec-11-topic-05` | Mô hình đếm và hai loại bất định | cốt lõi | giáo trình 11.1; Chua và cộng sự 2018 cho thuật ngữ |
| `lec-11-topic-06` | Tập mô hình | bổ sung | khoảng trống: biểu diễn bất định nhận thức khi không có công thức; nguồn Chua và cộng sự 2018 |
| `lec-11-topic-07` | Q-planning và Dyna-Q | cốt lõi | SB §8.1–8.2 |
| `lec-11-topic-08` | Mô hình sai, Dyna-Q+ | cốt lõi | SB §8.3 |
| `lec-11-topic-09` | Cập nhật kỳ vọng và cập nhật mẫu | cốt lõi | SB §8.5 |
| `lec-11-topic-10` | Quét ưu tiên, lấy mẫu theo quỹ đạo, RTDP | đọc thêm | SB §8.4, §8.6, §8.7 |
| `lec-11-topic-11` | Thuật toán rollout | cầu nối | khoảng trống: giáo trình 4.3.1 không có bài giảng; SB §8.10, Bertsekas 2019 |
| `lec-11-topic-12` | Quy tắc cận tin cậy trên, UCB1 | cầu nối | khoảng trống: giáo trình 4.7 không có bài giảng; SB §2.7, Auer và cộng sự 2002 |
| `lec-11-topic-13` | Bốn pha của MCTS | cốt lõi | SB §8.11 |
| `lec-11-topic-14` | Bảo đảm của UCT; AlphaGo Zero | cốt lõi (định lý); bổ sung (nhận xét) | Kocsis và Szepesvári 2006; SB §16.6 |
| `lec-11-topic-15` | Bài toán tối ưu kế hoạch | cốt lõi | giáo trình 11.3 |
| `lec-11-topic-16` | Đạo hàm qua mô hình | cốt lõi | giáo trình 11.3; Goodfellow và cộng sự 2016 §6.5 |
| `lec-11-topic-17` | Điều khiển dự báo theo chân trời lùi | cầu nối | khoảng trống: giáo trình 4.3.2 không có bài giảng; Bertsekas 2019 |
| `lec-11-topic-18` | Bắn ngẫu nhiên, phương pháp entropy chéo | bổ sung | khoảng trống: phương án khi mô hình không khả vi; Chua và cộng sự 2018 (QG3) |
| `lec-11-topic-19` | Sai số mô hình tích lũy | cốt lõi | giáo trình 11.3 (chủ đề 14.6.2 chỉ là giới hạn, không trỏ tới) |
| `lec-11-topic-20` | Tùy chọn, chính sách phân cấp | cốt lõi | giáo trình 11.4.1; SB §17.2 |
| `lec-11-topic-21` | Mô hình tùy chọn, bán-MDP | cốt lõi | giáo trình 11.4.1; SB (17.2)–(17.4) |
| `lec-11-topic-22` | Lập kế hoạch nhiều mức, Q-learning bán-MDP | cốt lõi | giáo trình 11.4.2; SB tr. 463; Sutton, Precup và Singh 1999 |
| `lec-11-topic-23` | Học mô hình tùy chọn | đọc thêm | SB §17.1–17.2 |
| `lec-11-topic-24` … `-28` | Tổng kết, tình huống, tóm tắt, bài tập, tham khảo | cốt lõi | GC-RL-1 |

## 13. Bảng thuật ngữ Việt–Anh (GC-RL-13, VP2–VP4, VP-RL-3/4; sẽ chép sang `outline.md`)

| Tiếng Việt | Tiếng Anh (mọi tên thông dụng) | Ghi chú |
|---|---|---|
| mô hình phân phối | distribution model | |
| mô hình mẫu | sample model | |
| kinh nghiệm mô phỏng | simulated experience | |
| lập kế hoạch | planning | Định nghĩa 01.14 |
| lập kế hoạch trong không gian trạng thái | state-space planning | |
| lập kế hoạch nền | background planning | |
| lập kế hoạch tại thời điểm quyết định | decision-time planning | |
| học tăng cường trực tiếp | direct reinforcement learning, direct RL | |
| học mô hình | model learning | |
| điều khiển tìm kiếm | search control | |
| mô hình đếm | count-based model; maximum-likelihood model | đề xuất tên; QG5 |
| bất định ngẫu nhiên | aleatoric uncertainty | |
| bất định nhận thức | epistemic uncertainty | |
| tập mô hình | ensemble (of models) | |
| lấy lại mẫu có hoàn lại | bootstrap resampling | không viết "bootstrap" trơn (trùng "mục tiêu bootstrap") |
| Q-planning một bước, chọn ngẫu nhiên, dạng bảng | random-sample one-step tabular Q-planning | |
| thưởng thăm dò | exploration bonus | |
| cập nhật kỳ vọng; cập nhật mẫu | expected update; sample update | SB cũng gọi "backup" |
| hệ số phân nhánh | branching factor | |
| quét ưu tiên | prioritized sweeping | |
| lấy mẫu theo quỹ đạo | trajectory sampling | |
| phân phối theo chính sách | on-policy distribution | |
| quy hoạch động thời gian thực | real-time dynamic programming, RTDP | |
| thuật toán rollout; chính sách rollout; chính sách cơ sở | rollout algorithm; rollout policy; base policy | giữ "rollout" như mục lục giáo trình 4.3.1; QG13 |
| quy tắc cận tin cậy trên | upper confidence bound, UCB; UCB1 | |
| hối tiếc | regret | |
| bài toán chọn lặp lại một bước | multi-armed bandit | như Bài 01 |
| tìm kiếm theo cây Monte Carlo | Monte Carlo tree search, MCTS | như mục lục giáo trình 11.2 |
| chính sách cây | tree policy | |
| chọn; mở rộng; mô phỏng; cập nhật ngược | selection; expansion; simulation; backup | "cập nhật ngược" để tránh trùng "lan truyền ngược"; QG14 |
| cận tin cậy trên áp dụng cho cây | upper confidence bounds applied to trees, UCT | |
| tối ưu kế hoạch dựa trên đạo hàm | gradient-based planning | như mục lục giáo trình 11.3 |
| tối ưu quỹ đạo | trajectory optimization | |
| phép bắn (đơn) | (single) shooting | |
| chân trời | horizon | |
| điều khiển dự báo; chân trời lùi | model predictive control, MPC; receding horizon | như mục lục giáo trình 4.3.2 |
| vòng hở; vòng kín | open-loop; closed-loop | |
| lan truyền ngược | backpropagation | |
| bắn ngẫu nhiên | random shooting | |
| phương pháp entropy chéo; mẫu ưu tú | cross-entropy method, CEM; elite samples | |
| sai số tích lũy | compounding error | |
| học tăng cường phân cấp | hierarchical reinforcement learning, hierarchical RL | |
| tùy chọn | option | mục lục giáo trình viết "tuỳ chọn"; học phần viết "tùy" (QG11) |
| tập khởi đầu; hàm kết thúc | initiation set; termination function, termination condition | |
| chính sách phân cấp | hierarchical policy | |
| mô hình tùy chọn | option model | |
| bán-MDP, quá trình quyết định bán-Markov | semi-Markov decision process, SMDP | |
| trừu tượng thời gian | temporal abstraction | |
| hàm giá trị tổng quát | general value function, GVF | |
| học trong tùy chọn | intra-option learning | |

## 14. Hình (SVG trong `2627-1/img/lec-11/`; GC12, VP10, NT25)

Mỗi hình vẽ lại bằng số liệu của chương, có `role="img"`, `<title>`, `alt` nêu đủ nội dung toán học, đoạn đọc hình trong văn bản; chữ $\ge16$ px ở 390 px khi lên trang chiếu (bản `-slide.svg` riêng khi cần). Hình của SB chỉ lấy ý, không chép (GC25).

| Tệp | Nội dung | Dùng ở |
|---|---|---|
| `cau-truc-chuong.svg` | khung "mô hình → kinh nghiệm mô phỏng → cập nhật → giá trị/chính sách" với ba nhánh: lập kế hoạch nền (§2), tại thời điểm quyết định (§3, §4), trừu tượng thời gian (§5) | §1.2 (chỉ ghi chú; `L11-1-05` thay bằng một dòng khung) |
| `me-cung-hai-phong.svg` | lưới 2 × 4, tường $\mathrm B$–$\mathrm C$, cửa $\mathrm F$–$\mathrm K$, đích $\mathrm Z$, $v_*$ ghi trong ô, ghi chú trượt $0{,}2$ | Ví dụ 11.1; `L11-1-05` |
| `kien-truc-dyna.svg` | vẽ lại SB Hình 8.1: học trực tiếp, học mô hình, điều khiển tìm kiếm, lập kế hoạch | §2.4; `L11-2-05` |
| `cap-nhat-ky-vong-va-mau.svg` | sai số theo số phép đánh giá cho $b=2,10,100$: đường $\sqrt{(b-1)/(bk)}$ và bậc thang của cập nhật kỳ vọng tại $k=b$ | §2.6; `L11-2-09` |
| `mcts-bon-pha.svg` | cây gốc $\mathrm F$ với bốn cạnh và số liệu của Ví dụ 11.16; bốn khung chọn, mở rộng, mô phỏng, cập nhật ngược | §3.3; `L11-3-05`, `L11-3-06` |
| `xe-tren-duong-ray.svg` | trục $x$, mốc $0$, quỹ đạo $x_t$: kế hoạch trên mô hình, vòng hở trên hệ thật, điều khiển dự báo với mô hình đúng và mô hình sai (số liệu Ví dụ 11.20, 11.23) | §4.3, §4.5; `L11-4-05`, `L11-4-08` |
| `sai-so-tich-luy.svg` | $e_k$ theo $k=1,\dots,5$ và chặn $\bar e(L^k-1)/(L-1)$ | §4.5; `L11-4-07` |
| `tuy-chon-hai-phong.svg` | mê cung với hai tùy chọn tô theo phòng, mũi tên $\pi_\omega$, hệ số $p$ và $r$ ghi cạnh ô | §5.1–5.2; `L11-5-01`, `L11-5-03` |

Màu không là tín hiệu duy nhất (nét liền, nét đứt, nhãn chữ).

## 15. Độ dài (GC-RL-4)

- Đề xuất **15 000–18 000 từ** ở cột `prose` của `count_note_words.py` (QG10): bốn cụm phương pháp, 27 ví dụ, 47 khối số hiệu (ghi chú 10 có khoảng 2 560 dòng với 51 khối). Phân bổ dự kiến: §1 1 000; §2 5 000; §3 3 500; §4 3 000; §5 3 000; §6, tình huống, tóm tắt 1 500; bài tập củng cố không tính vào mục tiêu (nằm ngoài cột `prose` hay không: tác tử soạn kiểm cách đếm của script).
- Không thêm nội dung chỉ để đạt độ dài (GC-RL-4).

## 16. Hướng dẫn đọc thêm và tài liệu tham khảo (GC25, GC16)

Ghi tác giả, năm, tên, chương hoặc mục, trang; nêu mục nào của chương dựa trên nguồn nào.

- **Sutton, R. S. và Barto, A. G. (2018).** *Reinforcement Learning: An Introduction*, ấn bản 2, MIT Press. §2.7, tr. 35–36 (§3.2); §8.1, tr. 159–161 (§1.2, §2.1, §2.4); §8.2, tr. 161–166 (§2.4); §8.3, tr. 166–168 (§2.5); §8.4, tr. 168–172, §8.6, tr. 174–177, §8.7, tr. 177–180 (§2.7); §8.5, tr. 172–174 (§2.6); §8.8, tr. 180–181 (§2.1); §8.10, tr. 183–185 (§3.1); §8.11, tr. 185–188 (§3.3); §16.6, tr. 441–450 (§3.4); §17.1–17.2, tr. 459–464 (§5).
- **Bertsekas, D. P. (2019).** *Reinforcement Learning and Optimal Control*, Athena Scientific. Mục rollout và cải thiện chính sách; mục điều khiển dự báo (dùng ở §3.1, §4.3 của ghi chú; số mục cần kiểm, QG9).
- **Szepesvári, C. (2010).** *Algorithms for Reinforcement Learning*, Morgan & Claypool. Mục học trực tuyến trong bài toán bandit (dùng ở §3.2; số mục cần kiểm).
- **Puterman, M. L. (1994).** *Markov Decision Processes*, Wiley. Chương bán-MDP (dùng ở §5.2; số chương cần kiểm).
- **Goodfellow, I., Bengio, Y. và Courville, A. (2016).** *Deep Learning*, MIT Press. §6.5 (§4.2).
- Nguồn dẫn để kiểm chứng mệnh đề cụ thể (P8, QG3): Auer, Cesa-Bianchi và Fischer (2002), *Machine Learning* 47, Định lý 1 (Định lý 11.24); Kocsis và Szepesvári (2006), ECML (Định lý 11.27); Sutton, Precup và Singh (1999), *Artificial Intelligence* 112 (§5); Chua, Calandra, McAllister và Levine (2018), NeurIPS (§2.2–2.3, §4.4); Deisenroth và Rasmussen (2011), ICML (§4.2, Nhận xét 11.37); Silver và cộng sự (2017), *Nature* 550 (Nhận xét 11.28); Barto, Bradtke và Singh (1995), *Artificial Intelligence* 72 (Định lý 11.19, qua SB tr. 178); Hoeffding (1963), *JASA* 58, Định lý 2, tr. 16 (Mệnh đề 11.22). Số trang và số định lý của các bài báo phải kiểm trên bản gốc trước khi vào ghi chú.

## 17. Câu hỏi mở cho điều phối viên và tác giả

| Mã | Câu hỏi | Đề xuất |
|---|---|---|
| QG1 | P1 = `deck nguồn + ghi chú`, nhưng `RL-hk2-2025-2026/` không có bộ trang chiếu nào cho chủ đề này. Lấy gì làm nguồn phạm vi, thứ tự và nội dung? | Ngoại lệ cho Bài 11, ghi vào `NGUYEN-TAC-HOC-PHAN.md` mục 3 (ngày, căn cứ) và storyboard: phạm vi, thứ tự theo mục lục Chương 11 của giáo trình tác giả (11.1–11.5); nội dung theo giáo trình chuẩn GC-RL-5 (chủ yếu SB Chương 8, §2.7, §16.6, §17.2; Bertsekas 2019); ghi chú đã kiểm định là chuẩn nội dung duy nhất của deck (P1 về thực chất là `ghi chú` cho bài này). |
| QG2 | Ghi chú cũ `materials/lec-11/lecture-note.md` (gradient chính sách nâng cao, 2026-09, 3 756 từ `prose`) và các tệp planning cũ của Bài 11 xử lý thế nào? | Ghi chú mới ghi đè cùng đường dẫn trong commit `feat(materials-11)` (bản cũ còn trong git); tác giả quyết riêng chủ đề gradient chính sách nâng cao có cần chỗ khác không (Chương 9–10 của giáo trình đã gồm TRPO, PPO, actor–critic, DDPG, SAC). Planning cũ: xem QT6. |
| QG3 | Các định nghĩa và kết quả không có trong giáo trình chuẩn (bất định ngẫu nhiên/nhận thức, tập mô hình, phương pháp entropy chéo, UCB1, UCT, tùy chọn có tập khởi đầu, Q-learning bán-MDP, quy tắc chọn của AlphaGo Zero) có được dẫn từ bài báo gốc không? | Cho phép theo P8 ("kiểm chứng một mệnh đề"), mỗi chỗ dẫn cụ thể số định lý hoặc mục; nội dung dựa nhiều vào bài báo (tập mô hình, CEM) xếp `bổ sung`; nếu tác giả không đồng ý, bỏ §2.3 và §4.4 khỏi ghi chú, giữ một câu có nguồn. |
| QG4 | BT-RL-6 (không bài tập cuối mục) chỉ cho Bài 08–10. Bài 11 có theo không? | Theo: không bài tập cuối mục, chỉ "Bài tập củng cố"; ghi quyết định vào `NGUYEN-TAC-HOC-PHAN.md` mục 2. |
| QG5 | Ký hiệu riêng của chương: $c_{\mathrm{ucb}}$ (SB: $c$), $\ell(s,a)$ (SB: $\tau$), $C(s,a)$ cho bộ đếm mô hình, $h$ cho chân trời, $x_t$, $u_t$ cho §4, $\beta_\omega$ thay $\gamma_\omega$ của SB, chỉ số $\omega_{\mathrm{cửa}}$ có chữ Việt trong KaTeX, tên "mô hình đếm". | Chấp nhận; bảng ký hiệu nêu tương ứng với SB một lần. Với tên tùy chọn, dùng $\omega_1$, $\omega_2$ nếu chữ có dấu trong `\mathrm{}` không hiển thị ổn định (NT26 cấm `\text{}` tiếng Việt). |
| QG6 | Ghi chú có cả §6 "Tổng kết" (như §7 ghi chú 10) lẫn "Tóm tắt chương"? | Giữ cả hai như ghi chú 10: §6 là nguồn của mạch "Tổng kết" (bảng so sánh, câu trả lời trung tâm, câu hỏi tự kiểm tra), "Tóm tắt chương" theo GC-RL-3; tránh lặp câu giữa hai phần. |
| QG7 | Câu nối sang bài sau: giáo trình Chương 12 là Học tăng cường ngoại tuyến, còn Bài 12 trong repo là Học tăng cường đa tác tử (ghi chú 2026-09). | Chỉ nối tới bài đã có trong kho (GC15); khi Bài 12 chưa được dựng lại, bỏ câu nối nội dung, chỉ giữ dòng nối trên trang "Tài liệu tham khảo" theo tên Bài 12 hiện có, sau khi tác giả xác nhận thứ tự. |
| QG8 | Công thức $\sqrt{(b-1)/(bt)}$ của SB tr. 174 không nêu mô hình xác suất của giá trị trạng thái kế. | Phát biểu Mệnh đề 11.15(b) với giá trị kế độc lập phương sai $1$ (đã kiểm: cho đúng $(b-1)/b$); ghi "cách đọc" này trong `review-log.md`; tác tử rà toán kiểm lại. |
| QG9 | Bertsekas (2019), Szepesvári (2010), Puterman (1994) không có bản trong `sources/`; số mục chưa kiểm. | Điều phối viên bổ sung bản tra cứu hoặc tác giả xác nhận số mục; trước đó ghi chú dẫn theo chương và tên mục, không bịa số mục. |
| QG10 | Độ dài mục tiêu. | 15 000–18 000 từ `prose`. |
| QG11 | Chính tả "tùy chọn" (học phần) hay "tuỳ chọn" (mục lục giáo trình); "bán-MDP" có gạch nối. | "tùy chọn" theo chính tả hiện hành của học phần; giữ "bán-MDP" như mục lục. |
| QG12 | Có thêm Tình huống 11.3 cho tùy chọn không (tùy chọn viết cho đích cũ, hoặc tùy chọn không bao giờ kết thúc như Bài tập 11.3(c))? | Không bắt buộc (GC-RL-8 đã đủ với 11.1, 11.2; trường hợp không kết thúc đã có ở Bài tập 11.3(c)); thêm nếu tác giả muốn mạch 5 có một ví dụ $v_\Omega<v_*$ bằng số. |
| QG13 | "rollout": SB gọi chính sách cơ sở là "rollout policy", Bertsekas gọi chính sách cải thiện là "rollout policy"; Bài 10 dịch rollout (đoạn dữ liệu) là "đoạn thu". | Theo Bertsekas và mục lục giáo trình: "chính sách cơ sở" $\pi_0$, "chính sách rollout" $\pi_{\mathrm{ro}}$, "thuật toán rollout"; một câu phân biệt với "đoạn thu (rollout)" của Bài 10; ghi tương ứng với SB. |
| QG14 | "backup" của MCTS dịch thế nào khi §4 dùng "lan truyền ngược" cho backpropagation? | "cập nhật ngược (backup)". |
