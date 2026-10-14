# Dàn bài Bài 04 — Giải MDP bằng quy hoạch động

Bản dàn bài theo chuẩn 2026-10-12 (giai đoạn II của `prompt_lecture_note_deck.md`). Học phần Học tăng cường, học kỳ 1 năm học 2026–2027. Người học: sinh viên đại học đã học học máy, học sâu, thuật toán và Bài 01–03 của học phần.

Nguồn chính: Bài giảng gốc (2025–2026), Bài 04 "Giải MDP", 38 trang; Bài tập tuần 3 và tuần 4 (2025–2026). Ghi chú bài giảng đã commit tại `36e8a5b` (`materials/lec-04/lecture-note.md`) là nguồn chuẩn cho số liệu, ký hiệu, thứ tự khái niệm và số hiệu kết quả; deck là bản tóm tắt của ghi chú. Thứ tự mạch theo Sutton và Barto (2018), chương 4, đã được người dùng duyệt từ đợt 2026-09-28.

Quy mô: **78 trang, 7 mạch, 120 phút** trình chiếu (sau vòng biên tập theo năm báo cáo rà soát); 30 phút còn lại của buổi 150 phút dành cho chữa bài tập và bài thực hành CartPole đã có. Kế hoạch sửa: `revision-plan-2026-10-12.md`, mục A. Quyết định theo từng trang và thời lượng: `storyboard.md`. Nhật ký: `review-log.md`, mục "Đợt sửa 2026-10-12 — Giai đoạn II: bộ trang chiếu".

## Mục tiêu học tập

| Mã | Mục tiêu trên trang L04-A02 | Sản phẩm kiểm tra | Trang kiểm tra |
|---|---|---|---|
| MT1 | Tính lượt quét, giá trị chính xác và chặn sai số theo phần dư | Bài tập 04.1 | L04-B08, L04-B08b |
| MT2 | Lập chính sách tham lam, kiểm giá trị không giảm | Bài tập 04.2 | L04-C07, L04-C07b |
| MT3 | Chạy lặp chính sách; phân biệt chứng nhận tối ưu với dừng gần đúng | Bài tập 04.3 | L04-D06, L04-D06b |
| MT4 | Chạy lặp giá trị, trích chính sách, chọn ngưỡng dừng | Bài tập 04.4 | L04-E08, L04-E08b |
| MT5 | So sánh lịch cập nhật; nêu điều kiện bao phủ và điều kiện mô hình | Bài tập 04.5, 04.6; Tình huống 04.1–04.2 | L04-F06, L04-F06b, L04-F05b |

Bài tập tổng hợp 04.6 (L04-G04, L04-G04b) kiểm đồng thời MT3, MT4 và điều kiện mô hình của MT5. Năng lực đầu vào (lợi tức, vai trò của mô hình) được kiểm ở L04-A05.

## Khung lý thuyết chung

- **Bài toán trung tâm.** Từ mô hình $p(s',r\mid s,a)$ đã biết, tìm chính sách có $v_\pi(s)$ lớn nhất đồng thời tại mọi trạng thái (bài toán lập kế hoạch, planning).
- **Đối tượng và ký hiệu chung.** MDP hữu hạn: $\mathcal S$ gồm $n$ trạng thái chưa kết thúc, $\mathcal A(s)$ hữu hạn, $s_{\mathrm{term}}$ với $V(s_{\mathrm{term}})=0$; chính sách Markov dừng $\pi(a\mid s)$; $P_\pi$, $r_\pi$; bảng giá trị $V\in\mathbb R^n$; giá trị nhìn trước $Q_V(s,a)$; toán tử $T_\pi$, $T_*$; phần dư $\Delta_\pi$, $\Delta_*$; ngưỡng $\theta$, sai số cho phép $\kappa$; chỉ số $t$ (tương tác), $k$ (lượt quét), $i$ (vòng cải thiện), $j$ (bước của lịch bất đồng bộ).
- **Giả thiết chung.** Tính Markov, tập trạng thái và hành động hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, $p$ đã biết. Giả thiết riêng: giá trị chính xác (định lý cải thiện, chính sách ổn định), quy tắc phá hòa (dừng hữu hạn), cập nhật vô hạn lần (bất đồng bộ).
- **Chuỗi định nghĩa → kết quả → phương pháp.** $T_\pi$ (Định nghĩa 04.1) → tính co (Mệnh đề 04.4) → nghiệm và hội tụ (Hệ quả 04.6) → phần dư và chặn (Định nghĩa 04.7, Hệ quả 04.8) → đánh giá chính sách (Thuật toán 04.9) → $Q_V$, tham lam (Định nghĩa 04.11, 04.12) → định lý cải thiện (Định lý 04.13) → chính sách ổn định, lặp chính sách, dừng hữu hạn, Bellman tối ưu (Định nghĩa 04.16, Thuật toán 04.17, Mệnh đề 04.18, Định lý 04.20) → $T_*$ và tính co (Định nghĩa 04.22, Mệnh đề 04.24) → tồn tại chính sách tối ưu (Định lý 04.25) → hội tụ và chặn (Hệ quả 04.26, 04.27) → lặp giá trị (Thuật toán 04.28) → bất đồng bộ (Thuật toán 04.31, Định lý 04.32) → GPI (Định nghĩa 04.34).
- **Giới hạn áp dụng.** Mọi bảo đảm thuộc về MDP đã cho; $\gamma=1$ làm mất tính co; mô hình gộp của CartPole có thể mất tính Markov, nên chứng nhận Bellman trên MDP ước lượng không chặn sai số trong môi trường liên tục (Nhận xét 04.35).

## Bản đồ bảy mạch

| N | Mạch | Trang tiêu đề mạch | Trang | Chức năng | Đầu vào | Đầu ra | Phút |
|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu | L04-A01 (bìa) | L04-A01–A05 (9 trang) | Đặt bài toán, khung chung, ví dụ xuyên suốt | MDP, lợi tức, Bellman kỳ vọng (Bài 03) | Mô hình hai trạng thái, $\pi_0$, nhu cầu tính giá trị dài hạn | 10 |
| 2 | Đánh giá chính sách | L04-B00, `mach-2` | 13 trang | Tính $v_\pi$ bằng lặp có chặn sai số | Mô hình, $\pi$ cố định | $v_{\pi_0}=(10,11)$, phần dư, $\theta=(1-\gamma)\kappa$ | 24 |
| 3 | Cải thiện chính sách | L04-C00, `mach-3` | 10 trang | Đổi hành động không làm giảm giá trị | $v_{\pi_0}$ | $\pi_1=(\mathrm a,\mathrm b)$, $v_{\pi_1}=(10,30)$, nhu cầu đánh giá lại | 18 |
| 4 | Lặp chính sách | L04-D00, `mach-4` | 10 trang | Xen kẽ tới chính sách ổn định, tối ưu | Định lý cải thiện | $(\mathrm b,\mathrm b)$, $(27,30)$; chi phí đánh giá đầy đủ | 18 |
| 5 | Lặp giá trị | L04-E00, `mach-5` | 16 trang | Gộp cải thiện vào lượt quét; tồn tại và hội tụ | Phương trình Bellman tối ưu, chi phí | $T_*$, tối ưu trên mọi chính sách, ngưỡng dừng | 24,5 |
| 6 | Lịch cập nhật và giới hạn của mô hình bảng | L04-F00, `mach-6` | 10 trang | Chi phí, tại chỗ, bất đồng bộ, GPI, CartPole | $T_*$, chi phí một lượt quét | Điều kiện lịch, điều kiện mô hình | 14 |
| 7 | Tổng kết và chuyển tiếp | L04-G00, `mach-7` | 10 trang | Bảng tổng kết, bài tập tổng hợp, trả lời vấn đề trung tâm | Kết quả mạch 2–6 | Giả thiết không được bỏ; nhu cầu của Bài 05 | 11,5 |

## Bảng thuật ngữ Việt–Anh

| Tiếng Việt | Tiếng Anh | Lần đầu trên deck |
|---|---|---|
| quá trình quyết định Markov | Markov decision process, MDP | L04-A01 |
| lập kế hoạch | planning | L04-A01 |
| quy hoạch động | dynamic programming | L04-A01 |
| lợi tức | return | L04-A01b |
| chính sách Markov dừng | stationary policy | L04-A01b (khác nghĩa với dừng thuật toán) |
| chính sách xác định | deterministic policy | L04-C04 (dạng chốt cho học phần) |
| lượt (tương tác) | episode | ghi chú của L04-A01b |
| lượt quét | sweep | L04-B02 (L04-A01b dùng thuật ngữ trong dòng "Ký hiệu:") |
| đánh giá chính sách | policy evaluation | L04-B01 |
| bài toán dự đoán | prediction | L04-B01 |
| cập nhật kỳ vọng | expected update | ghi chú của L04-B01 |
| toán tử Bellman | Bellman operator | L04-B04 |
| mục tiêu bootstrap | bootstrap target | L04-B04 |
| chuẩn vô cùng | sup norm | L04-B06 |
| ánh xạ co | contraction | L04-B06 |
| phần dư Bellman | Bellman residual | L04-B05 |
| bài toán điều khiển | control | L04-C01 |
| giá trị nhìn trước một bước | one-step lookahead | L04-C03 |
| chính sách tham lam | greedy policy | L04-C04 |
| quy tắc phá hòa | tie-breaking | L04-C04 |
| lặp chính sách | policy iteration | L04-D01 |
| phương trình Bellman tối ưu | Bellman optimality equation | ghi chú của L04-D04b |
| lặp giá trị | value iteration | L04-E01b |
| toán tử Bellman tối ưu | Bellman optimality operator | L04-E03 |
| cập nhật tại chỗ | in-place | L04-F02 |
| quy hoạch động bất đồng bộ | asynchronous dynamic programming | L04-F03 |
| lặp chính sách tổng quát | generalized policy iteration, GPI | L04-F04 |
| lời nguyền số chiều | curse of dimensionality | ghi chú của L04-F05 |
| dựa trên mô hình | model-based | ghi chú của L04-G06 |
| hạt giống ngẫu nhiên | random seed | ghi chú của L04-F05b |
| sơ đồ cập nhật | backup diagram | (không dùng trên deck Bài 04; hình cập nhật kỳ vọng ở L04-B01) |

Không dùng: "tổng thưởng chiết khấu" (thay bằng lợi tức), "quy tắc giữ hòa", "lưới năm ô", "MDP hai trạng thái" (thay bằng mô hình hai trạng thái), "lưới ngẫu nhiên" (thay bằng dãy năm ô trơn trượt), $\eta$ và $\varepsilon$ cho ngưỡng (thay bằng $\theta$, $\kappa$), $\theta$ cho góc cột CartPole (thay bằng $\phi$), "Đáp án", "tổng thưởng" (thay bằng lợi tức không chiết khấu hoặc số bước).

## Ký hiệu đặc thù của bài

- Tên trạng thái và hành động trong ví dụ viết chữ đứng: $\mathrm s_0,\mathrm s_1$; $\mathrm a,\mathrm b$; $\mathrm c_1,\dots,\mathrm c_5$; $\mathrm{trai},\mathrm{phai}$. Chính sách xác định trên mô hình hai trạng thái viết cặp theo thứ tự $(\mathrm s_0,\mathrm s_1)$.
- $p(s'\mid s,a)$ và $r(s,a)$ chỉ dùng khi đếm chi phí (L04-F01); $P_\pi$, $r_\pi$ cho dạng ma trận (L04-B07, L04-D03).
- Dấu thập phân là dấu phẩy, viết `0{,}9` trong KaTeX.
- Tiêu đề trang không chứa công thức KaTeX: chủ đề `white` của RevealJS đặt `text-transform: uppercase` cho `h2`, làm $\mathrm s_1$ thành "S1" và $\pi$ thành "Π".

## Ví dụ xuyên suốt

| Ví dụ | Dữ kiện | Nguồn | Trang dùng | Câu hỏi mới mỗi lần dùng |
|---|---|---|---|---|
| Mô hình hai trạng thái | $\mathrm s_0\xrightarrow{\mathrm a}\mathrm s_0$ thưởng 1; $\mathrm s_0\xrightarrow{\mathrm b}\mathrm s_1$ thưởng 0; $\mathrm s_1\xrightarrow{\mathrm a}\mathrm s_0$ thưởng 2; $\mathrm s_1\xrightarrow{\mathrm b}\mathrm s_1$ thưởng 3; $\gamma=0{,}9$ | Bài giảng gốc tr. 17–18; Bài tập tuần 4, bài 1 | A04–A05, B02–B08b, C01–C07b, D02–D06b, E01–E07, F02, F06–F06b, G04–G04b | Lợi tức cắt ngắn; lượt quét; giá trị chính xác; phần dư; nhìn trước; cải thiện; ba vòng lặp chính sách; ổn định; lặp giá trị; tính co của $T_*$; chặn $30\cdot0{,}9^k$; cập nhật tại chỗ; lịch bỏ sót; chứng nhận tối ưu |
| Dãy năm ô | $\mathrm c_1..\mathrm c_5$, $\mathrm c_5$ kết thúc, thưởng 10 khi vào $\mathrm c_5$, $-1$ khác, $\gamma=0{,}9$ | Bài giảng gốc tr. 25–28 | E06–E08b, F02, F03b (ghi chú) | Lan truyền giá trị; điểm bất động; thứ tự cập nhật ngược |
| Dãy năm ô trơn trượt | như trên, đúng hướng 0,8, đứng yên 0,1, ngược hướng 0,1 | Bài tập tuần 4, bài 10 | E06c | Kỳ vọng theo $p$ với ba kết quả chuyển ($V_1(\mathrm c_4)=7{,}8$); phần $V_2(\mathrm c_3)$ và chọn $\theta$ thuộc Bài tập 04.13 của tệp bài tập |
| CartPole rời rạc hóa | 324 ô, $\hat p$ từ 200 mẫu, $\gamma=0{,}99$ | Bài giảng gốc tr. 35–37; notebook CartPole | F01, F05, F05b | Chi phí; hai lượt quét tại ô 71; khoảng cách giữa MDP ước lượng và môi trường; số ô $k^4$ (ghi chú) |

## Dàn bài theo mạch

Danh sách trang đầy đủ, theo thứ tự trình chiếu, kèm lý do và quyết định nằm trong `storyboard.md`. Tóm tắt:

1. **Mở đầu.** L04-A01 bìa (luận đề: "Với MDP hữu hạn và $\gamma<1$, giá trị tối ưu là điểm bất động duy nhất của toán tử Bellman tối ưu. Chính sách tham lam theo nó là tối ưu."); A01b, A01c Tiên quyết và quy ước; A02 Mục tiêu học tập; A02b Nội dung; A03 Vấn đề trung tâm; A03b Cấu trúc một phép cập nhật quy hoạch động; A04 Ví dụ: mô hình hai trạng thái; A05 Bài tập: lợi tức của chính sách ban đầu.
2. **Đánh giá chính sách.** B00; B01 Giá trị dài hạn của chính sách cố định; B02 Ví dụ: hai lượt quét; B03 Phương trình Bellman kỳ vọng; B04 Toán tử Bellman đánh giá (Định nghĩa 04.1); B06 Tính co của toán tử đánh giá (Mệnh đề 04.4); B06c Hội tụ của đánh giá chính sách (Hệ quả 04.6); B07 Ví dụ: giá trị chính xác (Ví dụ 04.5); B05 Phần dư Bellman (Định nghĩa 04.7); B06b Chặn sai số theo phần dư (Hệ quả 04.8); B05b Thuật toán đánh giá chính sách đồng bộ (Thuật toán 04.9); B08/B08b Bài tập 04.1.
3. **Cải thiện chính sách.** C00; C01 Phép đổi hành động tại một trạng thái; C02 Ví dụ: hai nhánh hành động (Ví dụ 04.8); C03 Giá trị nhìn trước một bước (Định nghĩa 04.11); C04 Chính sách tham lam (Định nghĩa 04.12); C04b Định lý cải thiện chính sách (Định lý 04.13); C05 Chứng minh; C06 Ví dụ: lần cải thiện thứ nhất; C07/C07b Bài tập 04.2.
4. **Lặp chính sách.** D00; D01 Đánh giá lại sau mỗi lần cải thiện; D02 Ví dụ: ba vòng (Ví dụ 04.11); D02b Chính sách ổn định (Định nghĩa 04.16); D03 Thuật toán lặp chính sách (Thuật toán 04.17); D05 Dừng hữu hạn (Mệnh đề 04.18); D04 Giá trị tối ưu (Định nghĩa 04.19); D04b Phương trình Bellman tối ưu (Định lý 04.20); D06/D06b Bài tập 04.3.
5. **Lặp giá trị.** E00; E01 Chi phí của đánh giá đầy đủ; E01b Ý tưởng lặp giá trị; E02 Ví dụ: hai lượt quét lặp giá trị (Ví dụ 04.13); E03 Toán tử Bellman tối ưu (Định nghĩa 04.22); E03b Tính co của toán tử tối ưu (Mệnh đề 04.24); E05b Tồn tại chính sách tối ưu (Định lý 04.25, dạng $q_*$); E05c Chứng minh: tồn tại chính sách tối ưu; E05 Hội tụ của lặp giá trị (Hệ quả 04.26); E07 Chặn sai số theo phần dư tối ưu (Hệ quả 04.27); E04 Thuật toán lặp giá trị đồng bộ (Thuật toán 04.28); E06, E06b Ví dụ: dãy năm ô (Ví dụ 04.14); E06c Ví dụ: dãy năm ô trơn trượt; E08/E08b Bài tập 04.4.
6. **Lịch cập nhật và giới hạn của mô hình bảng.** F00; F01 Chi phí một lượt quét (Nhận xét 04.30); F02 Ví dụ: cập nhật tại chỗ (Ví dụ 04.16); F03 Thuật toán lặp giá trị bất đồng bộ (Thuật toán 04.31); F03b Hội tụ của quy hoạch động bất đồng bộ (Định lý 04.32); F04 Lặp chính sách tổng quát (Định nghĩa 04.34); F05 Ví dụ: CartPole rời rạc hóa (Ví dụ 04.17–04.18); F05b Chính sách tối ưu của CartPole rời rạc hóa (Tình huống 04.1–04.2); F06/F06b Bài tập 04.5.
7. **Tổng kết và chuyển tiếp.** G00; G01, G01b Tổng kết; G02 So sánh các phương pháp quy hoạch động; G02b Hội tụ của các phương pháp quy hoạch động; G04/G04b Bài tập: chứng nhận nghiệm tối ưu (Bài tập 04.6, bài tổng hợp); G06 Trả lời vấn đề trung tâm; G07 Câu hỏi tự kiểm tra; G05 Bài tập về nhà và tài liệu đọc. G03 (dãy năm ô trơn trượt) đã chuyển thành E06c.
