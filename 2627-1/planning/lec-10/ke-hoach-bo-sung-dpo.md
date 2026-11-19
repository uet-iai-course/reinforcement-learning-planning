# Bài 10 — Bổ sung DPO: kế hoạch ghi chú, bài tập và trang chiếu

> **Mục đích.** Kế hoạch bổ sung tối ưu ưu tiên trực tiếp (Direct Preference Optimization, DPO) vào Bài 10 "TRPO và PPO" theo thứ tự ghi chú → bài tập → deck (BT-RL-9). Tệp planning nội bộ, không công khai, không liên kết từ `index.html`. Đi kèm prompt `prompt-bo-sung-dpo-bai-10.md` cùng thư mục; mã câu hỏi mở QG… (ghi chú), QB… (bài tập), QT… (trang chiếu) ở mục cuối, có cột ánh xạ sang bảng Q của prompt.
>
> **Ngày:** 2026-11-19. **Trạng thái:** tác giả duyệt 2026-11-19 cùng bảng Q của prompt (mọi đề xuất). Chỗ kế hoạch khác bảng Q thì bảng Q thắng; riêng số hiệu bài tập theo Q4 (giữ số đã công bố): bài mới của ghi chú là 10.18–10.21 (10.13–10.16 của kế hoạch theo thứ tự), Bài tập 2.9 của Sutton và Barto là 10.22 trong `exercises.md`.
>
> **Luận điểm trọng tâm (tác giả).** PPO trong RLHF và DPO xuất phát từ cùng một mục tiêu: cực đại hóa phần thưởng trong khi giữ chính sách gần một chính sách tham chiếu cố định bằng phạt phân kỳ KL. DPO là cách thay thế trực tiếp, giải cùng bài toán đó mà không dùng PPO hay vòng học tăng cường trực tuyến nào.
>
> **Đầu vào đã đọc.** `NGUYEN-TAC-HOC-PHAN.md` (toàn tệp); `NGUYEN-TAC-GHI-CHU.md` (GC1–GC26), `NGUYEN-TAC-BAI-TAP.md` (BT1–BT13), `NGUYEN-TAC-TRANG-CHIEU.md` (NT1–NT28), `NGUYEN-TAC-VAN-PHONG.md` (VP1–VP24); `AGENTS.md` mục "Tham số trang chiếu của học phần" (P1–P11) và "Mẫu RevealJS bắt buộc"; ghi chú Bài 10 (Mục tiêu, Kiến thức tiên quyết, Bảng ký hiệu, §1.1, §4.3, §6 toàn bộ, §7, Tình huống, Tóm tắt, Bài tập củng cố, tài liệu tham khảo); `exercises.md` Bài 10; deck `lecture-10-trpo-va-ppo.html` (danh sách 101 trang, các trang L10-101, 109, 110, 700–710); `planning/lec-10/{outline,storyboard}.md` (bảng mạch, bảng thuật ngữ, phân bổ thời lượng, bảng phút từng trang); mẫu kế hoạch `planning/lec-11/ke-hoach-{ghi-chu,bai-tap,trang-chieu}.md` (chỉ lấy hình thức); mục lục giáo trình `giao-trinh/muc-luc-giao-trinh-hoc-tang-cuong-2026.pdf` (trang PDF 10 và 13); Sutton và Barto (2018), bản trích `/data/tqlong/qa/sources/sutton-barto-rl2020/extracted.md` (§2.8, §13.7); tám bài báo đã lưu (mục "Nguồn đã lưu" cuối tệp).
>
> **Đã tính lại.** Mọi con số ở mục A7, A9, B2 được tính tay và chạy lại bằng Python trong scratchpad của phiên (`tools/nums.py`, `nums2.py`, `nums3.py`, `ppo.py`; không vào repo). Tác tử soạn và tác tử rà toán vẫn phải tự tính lại (GC26, BT12).
>
> **Quy ước chỗ dẫn bài báo.** "tr. N" là trang PDF của bản arXiv đã lưu (đếm ký tự trang trong `extracted.md`; với các bản này trang PDF trùng số trang in khi bài có số trang). Số phương trình, mục, định lý, bổ đề, phụ lục đều đã đối chiếu với `extracted.md`; chỗ nào chưa kiểm được ghi "chưa kiểm".

## 0. Tóm tắt quyết định của kế hoạch

- **Vị trí.** Mục mới `## 7. Tối ưu chính sách từ phản hồi ưu tiên` đứng sau §6 (PPO) và trước phần kết; §7 hiện có thành `## 8. Tổng kết` (đổi tên theo GC-RL-15, QG3), các tiểu mục 7.1–7.6 thành 8.1–8.6. Mục mới ứng với mạch mới thứ 7 của deck; "Tổng kết" thành mạch 8 (QT1).
- **Nguồn** (QG1, ngoại lệ P1 và GC25 như "P1, Bài 11 (riêng)"): không có deck nguồn trong `RL-hk2-2025-2026/` và không giáo trình nào của GC-RL-5 trình bày RLHF hay DPO. Phạm vi và thứ tự theo mục lục giáo trình của học phần, Chương 13, mục 13.4–13.6; nội dung theo bài báo gốc đã lưu, mỗi chỗ dẫn số phương trình, mục, định lý.
- **Luận điểm trọng tâm thành hai kết quả có số hiệu và một bảng:** Định lý 10.57 (nghiệm dạng đóng của mục tiêu có phạt KL, điểm gặp của hai con đường), Định lý 10.65 (tương đương giữa con đường RLHF và con đường DPO, đủ giả thiết), bảng so sánh ở §7.5; nhắc lại ở §8.1–8.3, Tóm tắt chương và các trang `L10-D05`, `L10-D12`, `L10-D15`.
- **Ví dụ xuyên suốt:** bài toán một bước của Ví dụ 10.1, 10.17, 10.19 (một trạng thái, hai hành động, chính sách $(\tfrac23;\,\tfrac13)$), đọc trạng thái là lời nhắc $x$ và hai hành động là hai câu trả lời $y_1$, $y_2$; chính sách tham chiếu là chính sách softmax của Ví dụ 10.1 với $\theta_{\mathrm{ref}}=(\log2;\,0)$. Mục A7 ghi mọi phép tính.
- **Độ dài** (QG2): mục mới 4 000–5 000 từ `prose`, các chỗ sửa khác không quá 2 800 từ; ghi chú lên khoảng 36 000–37 000 từ, vượt trần 30 000 của GC-RL-4. Đề xuất ngoại lệ trần 37 000 cho Bài 10 (mục A12).
- **Bài tập** (QB1–QB3): bốn bài mới ở cuối "Bài tập củng cố", mức vận dụng; một bài sách Sutton và Barto (2018, Bài tập 2.9) vào `exercises.md`. Đánh số: đề xuất đánh lại `exercises.md` (ngoại lệ BT4), phương án giữ số ở QB1.
- **Deck:** mạch mới 19 trang `L10-D00` … `L10-D18`, `id="mach-7"`; "Tổng kết" giữ mọi `data-slide-id` `L10-7xx`, đổi `id="mach-8"`; tám mạch, vượt khoảng 5–7 của NT10 theo yêu cầu cụ thể của tác giả (QT1).
- **Chỗ của brief cần sửa:** liệt kê ở mục "Kiểm lại các dữ kiện của brief" cuối tệp (bốn điểm, quan trọng nhất: với ưu tiên tất định, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$ không vô hạn mà tiến tới $\log\tfrac32=0{,}4055$).

---

# A. Ghi chú bài giảng

## A1. Ánh xạ nguồn: tiểu mục ↔ mục lục giáo trình ↔ bài báo

Mục lục giáo trình (trang PDF 13, trang in xi): 13.4 Học phần thưởng từ phản hồi ưu tiên (13.4.1 Mô hình Bradley–Terry và huấn luyện mô hình phần thưởng; 13.4.2 Thu thập và chuẩn hoá dữ liệu ưu tiên); 13.5 Học tăng cường từ phản hồi con người (13.5.1 Quy trình ba giai đoạn: SFT, mô hình phần thưởng, tối ưu chính sách; 13.5.2 Ràng buộc KL và vấn đề tối ưu quá mức); 13.6 Phương pháp căn chỉnh trực tiếp (13.6.1 Direct Preference Optimization và quan hệ với RLHF). Cùng mục lục đặt TRPO và PPO ở 9.4–9.5 (trang PDF 10). Thứ tự của mục mới theo 13.4 → 13.5 → 13.6, chỉ chèn §7.2 (mục tiêu có phạt KL) trước RLHF vì đó là điểm chung của 13.5.2 và 13.6.1.

Viết tắt: **DPO** = Rafailov và cộng sự (2023); **IG** = Ouyang và cộng sự (2022); **ST** = Stiennon và cộng sự (2020); **ZI** = Ziegler và cộng sự (2019); **CH** = Christiano và cộng sự (2017); **IPO** = Gheshlaghi Azar và cộng sự (2024); **XU** = Xu và cộng sự (2024); **RQ** = Rafailov, Hejna, Park và Finn (2024).

| Tiểu mục ghi chú | Mục lục | Nguồn nội dung (đã kiểm trong `extracted.md`) | Nguồn đối chiếu |
|---|---|---|---|
| 7.1 Dữ liệu ưu tiên và mô hình Bradley–Terry | 13.4.1, 13.4.2 | DPO §3, (1), (2), tr. 3; CH §2.2.3, (1) và mất mát entropy chéo, tr. 5; IG §3.5, (1), tr. 8 ($K$ câu trả lời cho $\binom K2$ so sánh, chuẩn hóa để bản mẫu của người gán nhãn có điểm trung bình $0$, tr. 9); ST §3.4 "Reward models", tr. 6 (chuẩn hóa để bản tóm tắt tham chiếu có trung bình $0$); ZI §2, (1), tr. 3 (chuẩn hóa trung bình $0$, phương sai $1$); DPO Định nghĩa 1, Bổ đề 1, tr. 5, chứng minh Phụ lục A.5, tr. 17 | RQ §3.1, tr. 3 (MDP mức token: chuyển tất định, ghép token); ST chú thích 8, tr. 6 (phần thưởng chỉ ở cuối bản tóm tắt, lượt kết thúc ở ký hiệu kết thúc, $\gamma=1$); IG §3.5, tr. 9 ("bandit environment") |
| 7.2 Mục tiêu có phạt KL theo chính sách tham chiếu | 13.5.2 | DPO (3), tr. 3; DPO (4), tr. 4, chứng minh Phụ lục A.1, (11)–(15), tr. 15–16 (bất đẳng thức Gibbs; lớp chính sách không tham số, tr. 15); DPO Bổ đề 2, tr. 5 | IG (2), tr. 9; ZI (2), tr. 3; ST §3.4, tr. 6; Mệnh đề 10.24(a) của ghi chú |
| 7.3 RLHF với PPO | 13.5.1, 13.5.2 | IG §3.1 và Hình 2, tr. 3, 6; IG §3.5, tr. 8–9 (phạt KL theo từng token, hàm giá trị khởi tạo từ mô hình phần thưởng); IG Phụ lục C.4, tr. 42 ($\beta=0{,}02$, bán kính cắt $0{,}2$, một epoch trong, không chiết khấu khi tính GAE); ST §3.4, tr. 6 (hai vai của số hạng KL; hàm giá trị là mạng riêng khởi tạo từ mô hình phần thưởng); ST §4.3 và Hình 5, tr. 7–8 (tối ưu quá mức); ZI §2, quy trình bốn bước, tr. 3; ZI §2.2, bộ điều khiển $\beta$ theo KL mục tiêu, $K_\beta=0{,}1$, tr. 3 | DPO §3 (dạng $r(x,y)=r_\phi-\beta(\log\pi_\theta-\log\pi_{\mathrm{ref}})$ tối ưu bằng PPO), tr. 4; DPO §5.2, (10), tr. 6; RQ §3.2, (2), tr. 3–4 |
| 7.4 Tối ưu ưu tiên trực tiếp | 13.6.1 | DPO §4, (5), (6), (7), tr. 4; gradient và trọng số, tr. 5; "DPO outline", tr. 5; DPO §5.1, Định lý 1, tr. 6; Phụ lục A.2 (tr. 16), A.4, (21)–(22) (tr. 17), A.5 (tr. 17–18), A.6 gồm phát biểu lại Định lý 1 với giả thiết $\pi_{\mathrm{ref}}(y\mid x)>0$, $\beta>0$ và Mệnh đề 1 (tr. 18–19); Phụ lục B, $\beta=0{,}1$, cỡ lô 64, RMSprop, tốc độ học $10^{-6}$ (tr. 20) | XU Định lý 4.1, nửa đầu chứng minh, tr. 3–4; IPO Mệnh đề 1, tr. 4 |
| 7.5 So sánh RLHF với PPO và DPO | 13.6.1 | DPO §6.1, tr. 8 ("DPO and PPO optimize the same objective"); IPO §4.2, tr. 4; XU Định lý 4.1 và Bảng 1, tr. 3–4 | RQ §5.4, (16), tr. 9 |
| 7.6 Đọc thêm: biến thể và so sánh thực nghiệm | 13.6 | IPO §5, (17), Thuật toán 1, §5.3.1, tr. 6–7; RQ §3.1, Định lý 1, (11), tr. 6; DPO §6.1, Hình 2, tr. 7–8; XU tóm tắt, §5 (chuẩn hóa lợi thế, lô lớn, trung bình trượt của mô hình tham chiếu), tr. 1, 6 | — |

Nơi công bố của IG, CH, IPO, XU không có trong bản arXiv đã lưu (chưa kiểm); DPO ghi "NeurIPS 2023", ST ghi "NeurIPS 2020", RQ ghi "COLM 2024" trên trang đầu. Mục tài liệu tham khảo của ghi chú dẫn số arXiv, chỉ ghi nơi công bố sau khi kiểm.

## A2. Câu hỏi của mục mới và chỗ nối vào bài toán trung tâm

**Kết quả kế thừa** (câu nối đặt ở kết §6, GC15, GC-RL-2): Thuật toán 10.49 dùng phần thưởng $R_{t+1}$ do môi trường trả về; PPO-Penalty (Định nghĩa 10.43) phạt $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$ để giữ mỗi bước gần chính sách vừa sinh dữ liệu.

**Bài toán mở mục** (đoạn đầu §7.1, GC5, có số liệu): một lời nhắc $x$, hai câu trả lời $y_1$, $y_2$ do chính sách tham chiếu $\pi_{\mathrm{ref}}(\cdot\mid x)=(\tfrac23;\,\tfrac13)$ sinh ra; không có hàm phần thưởng, chỉ có sáu lần người gán nhãn so sánh: bốn lần chọn $y_1$, hai lần chọn $y_2$.

**Câu hỏi của mục** (bản nháp, theo VP-RL-2 đặt sau đoạn bài toán, được trả lời trong §7; tác tử soạn chỉnh bằng `no-ai-slop` Edit):

> **Câu hỏi.** Từ các phép so sánh này, chính sách mới nên chọn mỗi câu trả lời với xác suất bao nhiêu, nếu nó phải gần chính sách tham chiếu, và có cần một vòng học tăng cường để tìm chính sách đó không?

**Câu trả lời của mục** (đoạn kết §7.5 và dòng 6 của §8.3): mô hình Bradley–Terry cho phần thưởng $\hat r=(\log2;\,0)$ (Mệnh đề 10.54); mục tiêu có phạt KL với $\beta=1$ có nghiệm $\pi^*=(\tfrac45;\,\tfrac15)$ (Định lý 10.57); PPO đi tới nghiệm đó bằng mẫu sinh trực tuyến (Ví dụ 10.27), còn DPO cực tiểu hóa một hàm mất mát phân loại trên sáu phép so sánh và cho cùng $(\tfrac45;\,\tfrac15)$ (Ví dụ 10.28, Định lý 10.65), với điều kiện các giả thiết của Định lý 10.65 thỏa; với ba so sánh cùng chọn $y_1$, giả thiết đó hỏng và DPO đẩy $\pi_\theta(y_2)$ về $0$ với mọi $\beta$ (Tình huống 10.5).

**Nối vào bài toán trung tâm của chương** (QG4): bài toán trung tâm ở §1.1 hiện có hai nửa (giảm phương sai; bước lớn mà chính sách mới không kém chính sách cũ). Đề xuất thêm một câu vào cuối đoạn bài toán trung tâm của §1.1 và một dòng trên `L10-109`: "khi phần thưởng chỉ được biết qua so sánh ưu tiên, cùng một phép phạt KL giữ nghiệm cuối gần một chính sách tham chiếu cố định". Hình `central-problem.svg` thêm một hàng thứ ba (QG4, mục A11).

## A3. Mục tiêu học tập mới (GC16, VP21: bằng lời, không ký hiệu mới, không số hiệu khối)

Thêm hai mục sau mục tiêu 7 (bản nháp; tác tử soạn chỉnh bằng `no-ai-slop` Edit, giữ thuật ngữ của A10):

8. **Phần thưởng từ dữ liệu ưu tiên và mục tiêu có phạt KL.** Ước lượng *mô hình phần thưởng* (reward model) theo *mô hình Bradley–Terry* (Bradley–Terry model) từ *dữ liệu ưu tiên* (preference data) bằng hợp lý cực đại; chứng minh nghiệm dạng đóng của mục tiêu cực đại hóa phần thưởng có phạt KL theo một *chính sách tham chiếu* (reference policy) cố định; mô tả ba giai đoạn của *học tăng cường từ phản hồi con người* (reinforcement learning from human feedback, RLHF) với PPO và phân biệt chính sách cũ của PPO với chính sách tham chiếu.
9. **Tối ưu ưu tiên trực tiếp.** Suy ra hàm mất mát của *tối ưu ưu tiên trực tiếp* (Direct Preference Optimization, DPO) bằng phép đổi biến giữa phần thưởng và chính sách; tính bằng tay một bước DPO; phát biểu điều kiện để DPO và RLHF với PPO cho cùng chính sách, và nêu hậu quả khi điều kiện đó không thỏa.

Câu dẫn của mục "Bài tập củng cố" cập nhật danh sách theo mục tiêu (mục B4). Trang `L10-104` thêm hai mục (QT4 về mật độ).

## A4. Kiến thức tiên quyết thêm (GC16, GC3, GC-RL-16)

Danh sách hiện có đã gồm softmax và hàm điểm (Định nghĩa 09.11, 09.15, Mệnh đề 09.16, 09.17), định lý gradient chính sách (Định lý 09.23), tính chất tháp (Bổ đề 09.21, 09.22): đủ cho Bổ đề 10.59 và Mệnh đề 10.60. KL và Mệnh đề 10.24 nằm trong chương, không đưa vào danh sách. Thêm một gạch đầu dòng, kiến thức học máy mà đối tượng đã học (GC-RL-16), phát biểu lại trong hai câu:

- **Hồi quy logistic và mô hình ngôn ngữ tự hồi quy** (kiến thức học máy và học sâu). Với hàm logistic $\sigma(z)=1/(1+e^{-z})$, hồi quy logistic cực tiểu hóa trung bình của $-\log\sigma(z_i)$ trên các mẫu có nhãn dương, với $\sigma'(z)=\sigma(z)\sigma(-z)$ và $1-\sigma(z)=\sigma(-z)$. Một mô hình ngôn ngữ tự hồi quy gán cho chuỗi token $y=(a_0,\dots,a_{T-1})$ sau lời nhắc $x$ xác suất $\prod_{t}\pi(a_t\mid x,a_0,\dots,a_{t-1})$.

Câu quy ước số hiệu đầu mục giữ nguyên "Số hiệu `03.k`, …, `09.k` …"; câu về bài tập của tệp `exercises.md` đổi dải số theo QB1.

## A5. Bảng ký hiệu: dòng mới, quy ước, tương ứng với bài báo (GC-RL-6, GC7, VP-RL-5; QG5)

**Kiểm xung đột** (quét mọi công thức của `lecture-note.md` và `exercises.md` Bài 10, 2026-11-19):

- $Z_{t+1}$ là cờ kết thúc, nên hàm phân hoạch $Z(x)$ của bài báo viết $\mathcal Z(x)$ ($\mathcal Z$ chưa dùng).
- $\mathcal D$ là bộ đệm của PPO, nên tập dữ liệu ưu tiên viết $\mathcal D_{\mathrm{pref}}$; trung bình đều $\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}$ theo đúng quy ước $\widehat{\mathbb E}_{\mathcal D}$ đã có.
- $\phi(s,a)$ là đặc trưng của chính sách softmax, nên mô hình phần thưởng $r_\phi$ của DPO (và $r_\theta$ của IG, nơi $\theta$ là tham số của mô hình phần thưởng) viết $\hat r(x,y)$, theo khuôn $\hat v(s,w)$ của critic.
- $\beta$ đã là hệ số phạt KL của PPO-Penalty (Định nghĩa 10.43): giữ chữ $\beta$ cho hệ số phạt KL của mục tiêu RLHF, mở rộng nghĩa trong bảng và nói rõ hai KL khác nhau (Nhận xét 10.58).
- $\sigma$ đã dùng cục bộ cho hàm logistic ở Ví dụ 10.2, 10.6, 10.7 với cùng nghĩa: đưa vào bảng.
- $x$, $y$ đang có nghĩa cục bộ: $\sigma(x)$ ở Ví dụ 10.2; $x_k$, $y_k$ là bước lặp và tích $Fp_k$ của Thuật toán 10.36; $\langle x,y\rangle_F$; $y_t=V^{\mathrm{targ}}_t$ ở dòng 1825. Đề xuất giữ $x$, $y$ cho lời nhắc và câu trả lời (ký hiệu của mọi bài báo, QG5) và thêm vào danh sách nghĩa cục bộ sau bảng: "$x_k$, $y_k$, $\langle x,y\rangle_F$ của Thuật toán 10.36 và $y_t$ ở Mục 6.3 là ký hiệu cục bộ"; biến của hàm logistic viết $\sigma(z)$.
- $q$, $q'$ là hai phân phối tổng quát của Định nghĩa 10.23, còn $u=(1;\,-1)$ là vector cục bộ ở Mục 5.1: không dùng $q$ cho tỉ lệ ưu tiên và $u$ cho hiệu logit như bản nháp của brief. Ví dụ dùng số lần so sánh trực tiếp ("bốn trong sáu"), hiệu logit viết $\theta_1-\theta_2$, hiệu phần thưởng ngầm định viết $\Delta r_\theta$ (cùng họ với $\Delta J$, $\Delta p$ mà danh sách nghĩa cục bộ đã ghi là "các hiệu"). Trong bài tập, số cặp và số cặp chọn $y_1$ viết $n$, $k$ cục bộ trong khối.
- $\tau$ (hệ số KL của IPO) không dùng; $\gamma$ của IG (2) là hệ số trộn dữ liệu tiền huấn luyện, không phải hệ số chiết khấu: không đưa vào ghi chú.

**Dòng mới của bảng ký hiệu** (đặt sau dòng $N,h,K,M,E$; bảng lên khoảng 30 dòng, vượt "khoảng 20" của GC-RL-6 như bảng hiện có 26 dòng):

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $x$, $\mathcal X$; $y$, $\mathcal Y(x)$ | lời nhắc, tập lời nhắc; câu trả lời, tập câu trả lời cho $x$ (Mục 7) | $\mathcal X$, $\mathcal Y(x)$ hữu hạn trong các chứng minh |
| $\pi_{\mathrm{ref}}$, $\theta_{\mathrm{ref}}$ | chính sách tham chiếu, cố định trong cả Mục 7; tham số của nó | phân phối trên $\mathcal Y(x)$ với mỗi $x$ |
| $y_w$, $y_l$; $\mathcal D_{\mathrm{pref}}$ | câu trả lời được chọn, bị loại trong một phép so sánh; tập dữ liệu ưu tiên | bộ ba $(x,y_w,y_l)$ |
| $\sigma$ | hàm logistic $\sigma(z)=1/(1+e^{-z})$ | $\mathbb R\to(0,1)$ |
| $r(x,y)$, $\hat r(x,y)$ | phần thưởng (chưa biết) của mô hình Bradley–Terry, tức $r(s,a)$ với $s=x$, $a=y$; mô hình phần thưởng học được | $\mathbb R$ |
| $J_\beta$, $\pi^*_r$, $\mathcal Z_r(x)$ | mục tiêu có phạt KL; nghiệm của nó với phần thưởng $r$; hàm phân hoạch | $\mathbb R$; phân phối; $(0,\infty)$ |
| $r_\theta(x,y)$, $\Delta r_\theta$; $\tilde r_\theta(x,y)$ | phần thưởng ngầm định $\beta\log\bigl(\pi_\theta(y\mid x)/\pi_{\mathrm{ref}}(y\mid x)\bigr)$; hiệu của nó giữa $y_w$ và $y_l$; phần thưởng đã trừ KL $r-r_\theta$ | $\mathbb R$ |
| $L^{\mathrm{BT}}$, $L^{\mathrm{DPO}}$ | mất mát Bradley–Terry của mô hình phần thưởng; mất mát DPO (đều được cực tiểu hóa, cùng họ với $L^V$) | $\mathbb R_{\ge0}$ |
| $\mathcal V$ | tập token (Mục 7.1, 7.3) | hữu hạn |

Dòng $\epsilon,\beta,c_1,c_2$ sửa nghĩa của $\beta$ thành "hệ số phạt KL (theo $\pi_{\mathrm{old}}$ ở Mục 6.2, theo $\pi_{\mathrm{ref}}$ ở Mục 7)". Chỉ số dưới $r$ của $\pi^*_r$, $\mathcal Z_r$ được bỏ khi phần thưởng rõ từ ngữ cảnh. Dấu sao trên $\pi^*_r$ theo quy ước "tối ưu" đã có ($b^*$, $\Delta^*$, $p^*$); vì vậy phần thưởng sinh dữ liệu viết $r$, không $r^*$ như DPO.

**Tương ứng với bài báo** (thêm vào gạch đầu dòng "Ký hiệu của các bài báo" sau bảng, một lần):

| Bài báo | Ký hiệu của bài báo | Ghi chú |
|---|---|---|
| DPO | $r^*$, $r_\phi$, $\hat r_\theta$, $Z(x)$, $\mathcal D$, $\mathcal L_R$, $\mathcal L_{\mathrm{DPO}}$, $p^*(y_1\succ y_2\mid x)$, $\pi_r$ | $r$, $\hat r$, $r_\theta$, $\mathcal Z(x)$, $\mathcal D_{\mathrm{pref}}$, $L^{\mathrm{BT}}$, $L^{\mathrm{DPO}}$, $\Pr(y_1\succ y_2\mid x)$, $\pi^*_r$ |
| IG | $r_\theta$ (mô hình phần thưởng), $\pi^{\mathrm{RL}}_\phi$, $\pi^{\mathrm{SFT}}$, $\gamma$ (hệ số trộn tiền huấn luyện) | $\hat r$, $\pi_\theta$, $\pi_{\mathrm{ref}}=\pi^{\mathrm{SFT}}$; $\gamma$ không dùng |
| ZI | $\rho$ (mô hình ngôn ngữ ban đầu), $\beta$ | $\pi_{\mathrm{ref}}$ ($\rho$ là tỉ số chính sách) |
| IPO | $\tau$, $\Psi$, $\mu$ | $\beta$; $\Psi$, $\mu$ chỉ ở §7.6 |
| RQ | $\rho_0$, $f$, $\tau^w$, $\tau^l$ | $\mu_0$; chuyển tất định viết bằng lời |

## A6. Cấu trúc mục mới, `note-topic-id` và phân loại chủ đề (GC-RL-1, GC-RL-12, GC-RL-17)

Tên mục là cụm danh từ tiếng Việt (VP7, GC-RL-17); "PPO", "DPO" là tên thuật toán (VP2). `note-topic-id` mới tiếp sau `lec-10-topic-24`; hai mã cũ của phần kết (`lec-10-topic-23`, `-24`) giữ nguyên để không đổi `data-note-topic-id` của deck, nên mã không theo thứ tự đọc (chấp nhận được: mã là định danh).

| Phần ghi chú | Tiêu đề đề xuất | `note-topic-id` | Mạch deck | Phân loại |
|---|---|---|---|---|
| §7 | `## 7. Tối ưu chính sách từ phản hồi ưu tiên` (QG6 về tên) | — | 7 | — |
| 7.1 | `### 7.1 Dữ liệu ưu tiên và mô hình Bradley–Terry` | `lec-10-topic-25` | 7 | cầu nối (từ hồi quy logistic của học máy sang phần thưởng; nguồn DPO §3, CH §2.2.3) |
| 7.2 | `### 7.2 Mục tiêu có phạt KL theo chính sách tham chiếu` | `lec-10-topic-26` | 7 | cốt lõi |
| 7.3 | `### 7.3 RLHF với PPO` | `lec-10-topic-27` | 7 | cốt lõi |
| 7.4 | `### 7.4 Tối ưu ưu tiên trực tiếp` | `lec-10-topic-28` | 7 | cốt lõi |
| 7.5 | `### 7.5 So sánh hai con đường và giới hạn` | `lec-10-topic-29` | 7 | cốt lõi (luận điểm của tác giả) |
| 7.6 | `### 7.6 Đọc thêm: biến thể và so sánh thực nghiệm` | `lec-10-topic-30` | 7 (chỉ ghi chú diễn giả) | đọc thêm |
| §8 (cũ §7) | `## 8. Tổng kết` (GC-RL-15, QG3); 8.1–8.6 giữ tên, 8.2 thành "So sánh sáu phương pháp" | `lec-10-topic-23` (8.1), `-24` (8.6) | 8 | như cũ |

Quy định "nội dung dựa chủ yếu vào bài báo xếp nhóm `bổ sung`" của "P1, Bài 11 (riêng)" không áp dụng cho mục này (QG1): tác giả yêu cầu DPO là nội dung của bài, và mục lục giáo trình đặt nó ở 13.4–13.6. `outline.md` Bài 10 hiện chưa có mục "Phân loại chủ đề" (GC-RL-12): tác tử cập nhật outline thêm mục đó, ghi phân loại cho cả 24 chủ đề cũ (lấy từ bảng ánh xạ `note-topic-id` ↔ `data-slide-id` đã có) hoặc chỉ cho sáu chủ đề mới (QG7).

## A7. Ví dụ xuyên suốt và các phép tính tay

Dữ kiện tự dựng viết "Giả sử …" (VP18); nguồn gốc ghi ở `review-log.md`. Số thập phân ở đây đủ bốn đến sáu chữ số để kiểm; ghi chú làm tròn bốn chữ số. Mỗi khối `example` chép lại đủ dữ kiện (GC23).

**Dữ kiện chung.** Một lời nhắc $x$, hai câu trả lời $y_1$, $y_2$. Chính sách softmax với đặc trưng đơn vị như Ví dụ 10.1: $\pi_\theta(y_1\mid x)=\sigma(\theta_1-\theta_2)$. Chính sách tham chiếu $\theta_{\mathrm{ref}}=(\log2;\,0)$, nên $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$. Hệ số $\beta=1$ trừ khi ghi khác. Dữ liệu $\mathcal D_{\mathrm{pref}}$: sáu bộ ba, mỗi bộ một dòng (VP12): bốn bộ $(x,y_w,y_l)=(x,y_1,y_2)$, hai bộ $(x,y_2,y_1)$.

**(1) Mô hình Bradley–Terry và hợp lý cực đại** (Ví dụ 10.23, 10.24; Mệnh đề 10.54).

- Với hiệu phần thưởng $d=\hat r(x,y_1)-\hat r(x,y_2)$: $L^{\mathrm{BT}}(d)=-\tfrac16\bigl[4\log\sigma(d)+2\log\sigma(-d)\bigr]$.
- Đạo hàm: $\tfrac{d}{dd}L^{\mathrm{BT}}=-\tfrac16\bigl[4\sigma(-d)-2\sigma(d)\bigr]=\sigma(d)-\tfrac23$ (dùng $\sigma'=\sigma(\cdot)\sigma(-\cdot)$, $\sigma(-d)=1-\sigma(d)$). Bằng $0$ khi $\sigma(d)=\tfrac23$, tức $d=\log2=0{,}693147$; $L^{\mathrm{BT}}$ lồi theo $d$ (đạo hàm tăng) nên đây là cực tiểu duy nhất.
- Giá trị: $L^{\mathrm{BT}}(0)=\log2=0{,}693147$; $L^{\mathrm{BT}}(\log2)=-\tfrac23\log\tfrac23-\tfrac13\log\tfrac13=0{,}636514$.
- Chuẩn hóa $\hat r(x,y_2)=0$: $\hat r=(\log2;\,0)$. Kiểm: $\Pr(y_1\succ y_2\mid x)=\sigma(\log2)=1/(1+\tfrac12)=\tfrac23$, đúng tỉ lệ bốn trên sáu.
- Mọi $\hat r+f(x)$ cho cùng $L^{\mathrm{BT}}$ (chỉ hiệu xuất hiện).

**(2) Ba chính sách dưới mục tiêu có phạt KL** (Ví dụ 10.25), $J_\beta(p)=p\log2-\beta\bigl[p\log\frac{p}{2/3}+(1-p)\log\frac{1-p}{1/3}\bigr]$ với $p=\pi(y_1\mid x)$, $\hat r=(\log2;\,0)$, $\beta=1$:

| Chính sách | $\mathbb E_\pi\hat r$ | $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ | $J_1$ |
|---|---|---|---|
| $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ | $\tfrac23\log2=0{,}462098$ | $0$ | $0{,}462098$ |
| tham lam $(1;\,0)$ | $\log2=0{,}693147$ | $\log\tfrac32=0{,}405465$ | $0{,}287682$ |
| $(0{,}8;\,0{,}2)$ | $0{,}8\log2=0{,}554518$ | $0{,}8\log1{,}2+0{,}2\log0{,}6=0{,}145857-0{,}102165=0{,}043692$ | $0{,}510826$ |

Kiểm chéo với ghi chú: $D_{\mathrm{KL}}\bigl((0{,}8;\,0{,}2)\Vert(\tfrac23;\,\tfrac13)\bigr)=0{,}04369$ chính là $D_{\mathrm{KL}}(\pi'\Vert\pi)$ tại $s_B$ ở §4.3 (sau Định nghĩa 10.23), vì $(0{,}8;\,0{,}2)$ là $\pi'(\cdot\mid s_B)$ của Ví dụ 10.11. Với chính sách tham lam, chiều ngược $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi)=+\infty$ (Định nghĩa 10.23, vì $\pi(y_2)=0<\pi_{\mathrm{ref}}(y_2)$).

**(3) Nghiệm dạng đóng** (Ví dụ 10.26; Định lý 10.57).

- $\beta=1$: $\pi_{\mathrm{ref}}e^{\hat r}=(\tfrac23\cdot2;\,\tfrac13\cdot1)=(\tfrac43;\,\tfrac13)$; $\mathcal Z=\tfrac53$; $\pi^*=(\tfrac45;\,\tfrac15)$; $\beta\log\mathcal Z=\log\tfrac53=0{,}510826=J_1(0{,}8)$ ở bảng (2).
- Dạng $J_\beta(\pi)=\beta\log\mathcal Z-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*)$: với $\pi_{\mathrm{ref}}$, $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi^*)=\tfrac23\log\tfrac{2/3}{0{,}8}+\tfrac13\log\tfrac{1/3}{0{,}2}=-0{,}121548+0{,}170275=0{,}048728$, và $0{,}510826-0{,}048728=0{,}462098$, đúng $J_1(\pi_{\mathrm{ref}})$; với chính sách tham lam, $D_{\mathrm{KL}}=\log\tfrac1{0{,}8}=0{,}223144$ và $0{,}510826-0{,}223144=0{,}287682$, đúng.
- Phần thưởng đã trừ KL tại $\pi^*$: $\log2-\log\tfrac{0{,}8}{2/3}=0{,}693147-0{,}182322=0{,}510826$ và $0-\log\tfrac{0{,}2}{1/3}=0{,}510826$: bằng nhau và bằng $\beta\log\mathcal Z$ (Định lý 10.57(d)).
- Vai trò của $\beta$: $\pi^*(y_1)/\pi^*(y_2)=2\cdot2^{1/\beta}$.
  - $\beta=\tfrac12$: tỉ số $8$, $\pi^*=(\tfrac89;\,\tfrac19)=(0{,}8889;\,0{,}1111)$, $\mathcal Z=\tfrac23\cdot4+\tfrac13=3$, $\beta\log\mathcal Z=0{,}549306$.
  - $\beta=2$: tỉ số $2\sqrt2=2{,}828427$, $\pi^*=(0{,}738796;\,0{,}261204)$, $\mathcal Z=\tfrac23\sqrt2+\tfrac13=1{,}276142$, $\beta\log\mathcal Z=0{,}487684$.
  - $\beta\to\infty$: $\pi^*\to\pi_{\mathrm{ref}}$; $\beta\to0^+$: $\pi^*\to(1;\,0)$.
- Kiểm $\beta=\tfrac12$: $\mathbb E_{\pi^*}\hat r=\tfrac89\log2=0{,}616131$, $D_{\mathrm{KL}}=0{,}133649$, $0{,}616131-\tfrac12\cdot0{,}133649=0{,}549306$. Kiểm $\beta=2$: $0{,}512094-2\cdot0{,}012205=0{,}487684$.

**(4) Gradient chính sách của mục tiêu có phạt KL tại $\pi_{\mathrm{ref}}$** (Mệnh đề 10.60, dùng trong Ví dụ 10.27). Tại $\theta=\theta_{\mathrm{ref}}$, phần thưởng đã trừ KL bằng $\hat r=(\log2;\,0)$, giá trị $v=\tfrac23\log2=0{,}462098$, lợi thế $(\log2-0{,}462098;\,-0{,}462098)=(\tfrac13\log2;\,-\tfrac23\log2)=(0{,}231049;\,-0{,}462098)$. Với $\psi(y_1)=(\tfrac13;\,-\tfrac13)$, $\psi(y_2)=(-\tfrac23;\,\tfrac23)$ (Ví dụ 10.1): $\nabla_\theta J_1=\tfrac23\cdot\tfrac13\log2\cdot(\tfrac13;\,-\tfrac13)+\tfrac13\cdot(-\tfrac23\log2)(-\tfrac23;\,\tfrac23)=\tfrac29\log2\,(1;\,-1)=(0{,}154033;\,-0{,}154033)$. Kiểm bằng sai phân số: $\frac{d}{d(\theta_1-\theta_2)}J_1\bigl(\sigma(\theta_1-\theta_2)\bigr)$ tại $\log2$ bằng $0{,}154033$. Lợi thế này đúng bằng $\tfrac13\log2$ nhân lợi thế $(1;\,1;\,-2)$ của bộ đệm Ví dụ 10.17.

**(5) Hai vòng PPO-Clip trên phần thưởng đã trừ KL** (Ví dụ 10.27; bước tính tay trước Thuật toán 10.61). Giả sử bộ đệm ba mẫu $y_1,y_1,y_2$ đúng tần suất của $\pi_{\mathrm{old}}$ (như Ví dụ 10.17), $\epsilon=0{,}2$, phần thưởng đã trừ KL tính tại $\pi_{\mathrm{old}}$ và giữ cố định trong vòng, vòng trong cực đại hóa $\mathcal L^{\mathrm{CLIP}}$ bằng các bước nhỏ xuất phát từ $\pi_{\mathrm{old}}$.

- Vòng 1, $\pi_{\mathrm{old}}=\pi_{\mathrm{ref}}$: lợi thế $(0{,}231049;\,0{,}231049;\,-0{,}462098)=\tfrac13\log2\cdot(1;\,1;\,-2)$, nên $\mathcal L^{\mathrm{CLIP}}$ bằng $\tfrac13\log2$ nhân hàm của Ví dụ 10.17: tăng tới $p=0{,}8$ rồi phẳng. Vòng trong dừng ở $p=0{,}8$ (biên của đoạn phẳng); giá trị $\tfrac13\log2\cdot0{,}2\overline6=0{,}061613$.
- Vòng 2, $\pi_{\mathrm{old}}=(0{,}8;\,0{,}2)$: phần thưởng đã trừ KL $(0{,}510826;\,0{,}510826)$ theo (3), lợi thế $(0;\,0)$, gradient của $\mathcal L^{\mathrm{CLIP}}$ bằng $0$ (Mệnh đề 10.40(c)): chính sách đứng yên ở $\pi^*$.
- Kiểm: $J_1(0{,}8)=0{,}510826=\log\tfrac53$.
- Ghi cho tác tử soạn (Nhận xét hoặc bài tập, không bắt buộc): việc dừng đúng ở $\pi^*$ sau vòng 1 là do $\pi_{\mathrm{old}}(y_1)(1+\epsilon)=0{,}8$ trùng $\pi^*(y_1)$. Với $\epsilon=0{,}1$ và cùng cách cực đại hóa, dãy $p$ là $0{,}733333$; $0{,}806667$; $0{,}726000$; $0{,}798600$ (mỗi vòng đi tới biên đầu tiên của đoạn phẳng: $1{,}1\cdot\tfrac23$, $1{,}1\cdot 0{,}733333$, $0{,}9\cdot 0{,}806667$, $1{,}1\cdot 0{,}726$; kiểm bằng mô phỏng `ppo.py`; vòng 3 có lợi thế $(-0{,}00817;\,0{,}03409)$ và đi xuống tới biên $0{,}9\cdot0{,}806667$): $\pi_{\mathrm{old}}$ giới hạn từng bước, $\pi_{\mathrm{ref}}$ quyết định điểm dừng $p=0{,}8$, còn dãy dao động quanh điểm đó. Đây là Bài tập 10.16 đề xuất (mục B2).

**(6) Đổi biến và phần thưởng ngầm định** (Mệnh đề 10.63, đoạn mở §7.4). Từ $\pi^*=(\tfrac45;\,\tfrac15)$ và $\mathcal Z=\tfrac53$: $\beta\log\frac{\pi^*(y_1)}{\pi_{\mathrm{ref}}(y_1)}+\beta\log\mathcal Z=\log1{,}2+\log\tfrac53=0{,}182322+0{,}510826=0{,}693147=\hat r(y_1)$ và $\log0{,}6+\log\tfrac53=-0{,}510826+0{,}510826=0=\hat r(y_2)$. Hiệu phần thưởng ngầm định $\log1{,}2-\log0{,}6=\log2$, trùng hiệu $\hat r(y_1)-\hat r(y_2)$: $\mathcal Z$ triệt tiêu.

**(7) Một bước DPO tính tay và hội tụ** (Ví dụ 10.28; trước Thuật toán 10.67). Hạ gradient, $\beta=1$, bước học $\alpha=1$, khởi tạo $\theta=\theta_{\mathrm{ref}}$.

- Hiệu phần thưởng ngầm định của cặp $(y_1,y_2)$: $\Delta r_\theta=\beta\bigl[(\theta_1-\theta_2)-\log2\bigr]$, vì $\log\frac{\pi_\theta(y_1)}{\pi_\theta(y_2)}=\theta_1-\theta_2$ với softmax.
- $L^{\mathrm{DPO}}(\theta)=-\tfrac16\bigl[4\log\sigma(\Delta r_\theta)+2\log\sigma(-\Delta r_\theta)\bigr]$; tại $\theta_{\mathrm{ref}}$: $\Delta r_\theta=0$, $L^{\mathrm{DPO}}=\log2=0{,}693147$.
- Trọng số của Mệnh đề 10.66 tại $\theta_{\mathrm{ref}}$: $\sigma(0)=\tfrac12$ cho mọi bộ ba. $\nabla\log\pi_\theta(y_1)-\nabla\log\pi_\theta(y_2)=\psi(y_1)-\psi(y_2)=(1;\,-1)$ với mọi $\theta$ (Mệnh đề 09.16).
- Gradient: $-\beta\bigl[\tfrac46\cdot\tfrac12(1;\,-1)+\tfrac26\cdot\tfrac12(-1;\,1)\bigr]=(-\tfrac16;\,\tfrac16)$.
- Bước: $\theta=(\log2+\tfrac16;\,-\tfrac16)=(0{,}859814;\,-0{,}166667)$; $\theta_1-\theta_2=1{,}026481$; $\pi_\theta(y_1)=\sigma(1{,}026481)=0{,}736233$; $L^{\mathrm{DPO}}=0{,}651417$.
- Phần thưởng ngầm định sau bước: $r_\theta(y_1)=\log\frac{0{,}736233}{2/3}=0{,}099256$, $r_\theta(y_2)=\log\frac{0{,}263767}{1/3}=-0{,}234077$; hiệu $0{,}333333=\tfrac13$. Kiểm: $\Delta r_\theta=\beta(\tfrac16+\tfrac16)=\tfrac13$.
- Trọng số ở bước 2: $\sigma(-\tfrac13)=0{,}417430$ cho bốn bộ chọn $y_1$, $\sigma(\tfrac13)=0{,}582570$ cho hai bộ chọn $y_2$: cặp đang bị xếp sai theo phần thưởng ngầm định nhận trọng số lớn hơn.
- Các bước tiếp: $\pi_\theta(y_1)=0{,}767576$; $0{,}782853$; $0{,}790730$; $0{,}794927$ (bước 2–5), $L^{\mathrm{DPO}}=0{,}640676$; $0{,}637728$; $0{,}636877$; $0{,}636624$.
- Cực tiểu: đạo hàm theo $\Delta r_\theta$ là $\sigma(\Delta r_\theta)-\tfrac23$, bằng $0$ khi $\Delta r_\theta=\log2$, tức $\theta_1-\theta_2=2\log2$ và $\pi_\theta=(\tfrac45;\,\tfrac15)=\pi^*$ của (3); $\min L^{\mathrm{DPO}}=0{,}636514=\min L^{\mathrm{BT}}$ của (1). Hai con đường gặp nhau.
- Với $\beta$ tổng quát, cực tiểu là $\theta_1-\theta_2=\log2+\tfrac1\beta\log2$, cho $\pi_\theta(y_1)/\pi_\theta(y_2)=2\cdot2^{1/\beta}$, trùng (3).
- Đẳng thức (16) của RQ trên bước 1: $\mathbb E_{\pi_{\mathrm{ref}}}r_\theta=\tfrac23\cdot0{,}099256+\tfrac13\cdot(-0{,}234077)=-0{,}011855=-\beta D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)$ (dùng ở Nhận xét 10.68).

**(8) Ưu tiên tất định từ ít dữ liệu** (Tình huống 10.5). Giả sử phần thưởng thật $(\log2;\,0)$, nên mỗi phép so sánh chọn $y_1$ với xác suất $\tfrac23$; chỉ thu ba phép so sánh và cả ba chọn $y_1$, biến cố có xác suất $(\tfrac23)^3=\tfrac8{27}=0{,}296296$.

- $L^{\mathrm{BT}}(d)=-\log\sigma(d)$ giảm ngặt, tiến về $0$ khi $d\to\infty$, không có cực tiểu (Mệnh đề 10.54(c)).
- $L^{\mathrm{DPO}}=-\log\sigma\bigl(\beta(\theta_1-\theta_2-\log2)\bigr)$ giảm ngặt theo $\theta_1-\theta_2$ với mọi $\beta>0$.
- Bảng theo $\theta_1-\theta_2$ (với $\beta=1$; $J_1$ tính với phần thưởng thật):

| $\theta_1-\theta_2$ | $\pi_\theta(y_1)$ | $L^{\mathrm{DPO}}$ | $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$ | $J_1$ |
|---|---|---|---|---|
| $2$ | $0{,}880797$ | $0{,}239545$ | $0{,}122756$ | $0{,}487766$ |
| $4$ | $0{,}982014$ | $0{,}035976$ | $0{,}327837$ | $0{,}352843$ |
| $10$ | $0{,}999955$ | $0{,}000091$ | $0{,}404997$ | $0{,}288119$ |
| $\to\infty$ | $\to1$ | $\to0$ | $\to\log\tfrac32=0{,}405465$ | $\to0{,}287682$ |

- So với nghiệm của bài toán thật, $J_1(\pi^*)=0{,}510826$. KL theo chiều của mục tiêu bị chặn bởi $\log\tfrac32$; đại lượng không bị chặn là $r_\theta(y_2)=\log\frac{\pi_\theta(y_2)}{1/3}\to-\infty$ và KL chiều ngược $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)$.
- IPO cùng dữ liệu, $\tau=\beta=1$: cực tiểu của (17) của IPO cho hiệu log-tỉ số $\log\frac{\pi(y_1)\pi_{\mathrm{ref}}(y_2)}{\pi(y_2)\pi_{\mathrm{ref}}(y_1)}=\tfrac1{2\tau}=0{,}5$, nên $\pi(y_1)=\sigma(\log2+0{,}5)=0{,}767303$ (dùng ở §7.6; tính theo (17), bài báo chỉ cho trường hợp $\pi_{\mathrm{ref}}$ đều ở §5.3.1).

**(9) Ba bản tóm tắt** (Tình huống 10.4). Giả sử một bài đăng $x$, ba bản tóm tắt $y_1,y_2,y_3$ do $\pi_{\mathrm{ref}}=(0{,}5;\,0{,}3;\,0{,}2)$ sinh ra, 45 phép so sánh, 15 cho mỗi cặp: $(y_1,y_2)$ 10 chọn $y_1$, 5 chọn $y_2$; $(y_1,y_3)$ 12 chọn $y_1$, 3 chọn $y_3$; $(y_2,y_3)$ 10 chọn $y_2$, 5 chọn $y_3$.

- Tỉ lệ $\tfrac23$, $\tfrac45$, $\tfrac23$ bằng $\sigma(\log2)$, $\sigma(\log4)$, $\sigma(\log2)$ và $\log2+\log2=\log4$, nên $\hat r=(\log4;\,\log2;\,0)$ cực tiểu từng số hạng của $L^{\mathrm{BT}}$ (Mệnh đề 10.54(c) cho từng cặp), do đó cực tiểu tổng; $L^{\mathrm{BT}}$: $\log2=0{,}693147$ tại $\hat r=0$, $0{,}591144$ tại $\hat r$.
- $\beta=1$: $\pi_{\mathrm{ref}}e^{\hat r}=(2;\,0{,}6;\,0{,}2)$, $\mathcal Z=2{,}8$, $\pi^*=(\tfrac57;\,\tfrac3{14};\,\tfrac1{14})=(0{,}714286;\,0{,}214286;\,0{,}071429)$, $J_1=\log2{,}8=1{,}029619$; kiểm $\mathbb E_{\pi^*}\hat r-D_{\mathrm{KL}}=1{,}138742-0{,}109122=1{,}029619$; dưới $\pi_{\mathrm{ref}}$, $\mathbb E\hat r=0{,}901091$.
- $\beta=2$: $\pi_{\mathrm{ref}}e^{\hat r/2}=(1;\,0{,}3\sqrt2;\,0{,}2)=(1;\,0{,}424264;\,0{,}2)$, $\mathcal Z=1{,}624264$, $\pi^*=(0{,}615663;\,0{,}261204;\,0{,}123134)$, $\beta\log\mathcal Z=2\log1{,}624264=0{,}970110$, $D_{\mathrm{KL}}=0{,}032217$. $\beta=\tfrac12$: $(0{,}85106;\,0{,}12766;\,0{,}02128)$, $\beta\log\mathcal Z=\tfrac12\log9{,}4=1{,}120352$.
- Phần thưởng ngầm định tại $\pi^*$ ($\beta=1$): $(0{,}356675;\,-0{,}336472;\,-1{,}029619)=\hat r-\log2{,}8$, cùng lớp với $\hat r$ (Mệnh đề 10.63(c)).

**(10) Ví dụ cho Bổ đề 10.59 (KL theo token)** (đoạn sau chứng minh, không đánh số). Hai token, $\mathcal V=\{\mathrm a,\mathrm b\}$, $\pi_{\mathrm{ref}}$ đều ở mỗi bước; $\pi$ chọn token đầu $(0{,}6;\,0{,}4)$, token thứ hai sau $\mathrm a$ là $(0{,}9;\,0{,}1)$, sau $\mathrm b$ là $(0{,}5;\,0{,}5)$. KL của chuỗi $0{,}240974$; KL bước đầu $0{,}020136$, KL bước hai sau $\mathrm a$ là $0{,}368064$, sau $\mathrm b$ là $0$; $0{,}020136+0{,}6\cdot0{,}368064+0{,}4\cdot0=0{,}240974$.

## A8. Kế hoạch từng tiểu mục: khối, vai, số hiệu, mức chứng minh, chỗ dẫn

Bộ đếm chung tiếp sau Nhận xét 10.51: khối mới 10.52–10.70; ví dụ tiếp sau Ví dụ 10.22: 10.23–10.28; tình huống tiếp sau Tình huống 10.3: 10.4–10.5 (mục A9). Mỗi khái niệm trọng tâm đi đủ các bước của GC18; không bài tập cuối mục (BT-RL-6). Ngân sách từ `prose` ở A12.

### §7.1 Dữ liệu ưu tiên và mô hình Bradley–Terry (`lec-10-topic-25`; khoảng 900 từ)

1. **Bài toán** (đoạn mở mục, GC5, GC-RL-2): Thuật toán 10.49 cần $R_{t+1}$ từ môi trường; với lời nhắc và câu trả lời, môi trường không trả phần thưởng, chỉ có phép so sánh. Dữ kiện A2; "**Câu hỏi.**" của A2.
2. **Định nghĩa 10.52 (Bài toán sinh câu trả lời)**: (a) dạng một bước: $x\sim\mu_0$ trên $\mathcal X$, hành động $y\in\mathcal Y(x)$, lượt kết thúc sau một hành động, phần thưởng $r(x,y)$, chính sách $\pi(y\mid x)$; là bài toán một bước của Ví dụ 10.1 với $s=x$, $a=y$; (b) dạng mức token: $S_0=x$, $A_t\in\mathcal V$, $S_{t+1}=(S_t,A_t)$ tất định, kết thúc khi $A_t$ là ký hiệu kết thúc hoặc $t+1=T_{\max}$, $\pi_\theta(y\mid x)=\prod_t\pi_\theta(A_t\mid S_t)$, phần thưởng chỉ ở bước cuối. Chỗ dẫn: RQ §3.1, tr. 3; ST chú thích 8, tr. 6; IG §3.5, tr. 9. Sau định nghĩa: đoạn diễn giải (GC9), một phân biệt: (a) và (b) cùng một chính sách, khác cách đếm bước.
3. **Ví dụ 10.23 (Dữ liệu ưu tiên trên bài toán một bước)**: dữ kiện A7, mỗi bộ ba một dòng; tỉ lệ $\tfrac23$; trước định nghĩa (GC10).
4. **"Một cách trực quan"**: xác suất chọn tăng theo hiệu phần thưởng, chỉ hiệu có nghĩa.
5. **Định nghĩa 10.53 (Dữ liệu ưu tiên, mô hình Bradley–Terry)**: bộ ba $(x,y_w,y_l)$; $\Pr(y\succ y'\mid x)=\frac{e^{r(x,y)}}{e^{r(x,y)}+e^{r(x,y')}}=\sigma\bigl(r(x,y)-r(x,y')\bigr)$; lớp tương đương $[r]=\{r+f:\ f \text{ chỉ phụ thuộc } x\}$. Chỗ dẫn: DPO (1), tr. 3; DPO Định nghĩa 1, tr. 5; CH (1), tr. 5 (CH viết cho đoạn quỹ đạo, tổng phần thưởng trên đoạn).
6. **Mệnh đề 10.54 (Hợp lý cực đại của mô hình phần thưởng)**, bốn phần GC-RL-7. Giả thiết: $\mathcal D_{\mathrm{pref}}$ hữu hạn, mỗi bộ ba độc lập theo Định nghĩa 10.53. Kết luận: (a) đối hợp lý trung bình là $L^{\mathrm{BT}}(\hat r)=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\log\sigma\bigl(\hat r(x,y_w)-\hat r(x,y_l)\bigr)$, hàm mất mát của hồi quy logistic trên hiệu; (b) $L^{\mathrm{BT}}(\hat r+f)=L^{\mathrm{BT}}(\hat r)$; (c) với hai câu trả lời và $k$ trong $n$ bộ ba chọn $y_1$: nếu $0<k<n$, các cực tiểu đúng là $\hat r(x,y_1)-\hat r(x,y_2)=\log\frac k{n-k}$; nếu $k=n$, $L^{\mathrm{BT}}>0$ với mọi $\hat r$, có cận dưới $0$ không đạt. Điều kiện áp dụng: mô hình phần thưởng tùy ý trên các cặp xuất hiện trong dữ liệu. Phạm vi: không nói về phần thưởng trên câu trả lời không xuất hiện. Chứng minh đầy đủ: (a) định nghĩa; (b) chỉ hiệu xuất hiện; (c) đạo hàm $\sigma(d)-k/n$, tính lồi. Nguồn: DPO (2), tr. 3; IG (1), tr. 8; DPO Bổ đề 1, tr. 5, A.5, tr. 17.
7. **Ví dụ 10.24 (Khớp mô hình phần thưởng)**: số A7(1); dòng kiểm.
8. **Nhận xét 10.55 (Thu thập và chuẩn hóa dữ liệu ưu tiên)** (ứng với 13.4.2): xếp hạng $K$ câu trả lời cho $\binom K2$ bộ ba, $K$ từ 4 đến 9, cả $\binom K2$ bộ ba của một lời nhắc vào cùng một phần tử lô để tránh quá khớp (IG §3.5, tr. 8); vì (b), mô hình phần thưởng được chuẩn hóa: IG (trung bình $0$ trên bản mẫu của người gán nhãn, tr. 9), ST (trung bình $0$ trên bản tóm tắt tham chiếu, tr. 6), ZI (trung bình $0$, phương sai $1$ dưới mô hình ban đầu, tr. 3). Nhầm lẫn thường gặp (GC11): coi $\hat r(x,y)$ là điểm tuyệt đối; chỉ hiệu trong cùng một lời nhắc được xác định.
9. Kết tiểu mục: có $\hat r$, chưa có chính sách.

### §7.2 Mục tiêu có phạt KL theo chính sách tham chiếu (`lec-10-topic-26`; khoảng 900 từ; giáo trình 13.5.2)

1. **Bài toán**: với $\hat r=(\log2;\,0)$, chính sách cực đại hóa $\mathbb E\hat r$ là $(1;\,0)$; nhưng $\hat r$ chỉ được khớp trên câu trả lời của $\pi_{\mathrm{ref}}$ (ST §3.4, tr. 6: số hạng KL giữ đầu ra không quá khác dữ liệu mô hình phần thưởng đã thấy; DPO tr. 4: tránh sụp về một câu trả lời).
2. **"Một cách trực quan"**: trả một chi phí cho mỗi đơn vị KL rời khỏi $\pi_{\mathrm{ref}}$.
3. **Ví dụ 10.25 (Ba chính sách trên bài toán một bước)**: bảng A7(2), trước định nghĩa.
4. **Định nghĩa 10.56 (Mục tiêu có phạt KL, chính sách tham chiếu)**: $\mu_0$ trên $\mathcal X$, $\pi_{\mathrm{ref}}(\cdot\mid x)$ cố định, $\beta>0$:
   $$J_\beta(\pi)=\mathbb E_{x\sim\mu_0}\Bigl[\mathbb E_{y\sim\pi(\cdot\mid x)}r(x,y)-\beta D_{\mathrm{KL}}\bigl(\pi(\cdot\mid x)\Vert\pi_{\mathrm{ref}}(\cdot\mid x)\bigr)\Bigr].$$
   Chỗ dẫn: DPO (3), tr. 3; IG (2), tr. 9 (với hệ số trộn tiền huấn luyện bằng $0$ cho mô hình "PPO"); ZI (2), tr. 3.
5. **Định lý 10.57 (Nghiệm của mục tiêu có phạt KL)** — kết quả chính thứ nhất của luận điểm ("cùng mục tiêu"; điểm gặp). Bốn phần:
   - Giả thiết: $\mathcal Y(x)$ hữu hạn; $r$ nhận giá trị thực; $\beta>0$; $\pi_{\mathrm{ref}}(\cdot\mid x)$ là phân phối; chính sách được chọn tự do cho mỗi $x$ (mọi phân phối có điều kiện).
   - Kết luận: (a) với $\mathcal Z_r(x)=\sum_y\pi_{\mathrm{ref}}(y\mid x)e^{r(x,y)/\beta}$ và $\pi^*_r(y\mid x)=\pi_{\mathrm{ref}}(y\mid x)e^{r(x,y)/\beta}/\mathcal Z_r(x)$, mọi $\pi$ có KL hữu hạn thỏa $\mathbb E_{y\sim\pi}r-\beta D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})=\beta\log\mathcal Z_r(x)-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r)$ tại mỗi $x$; (b) $\pi^*_r$ là nghiệm duy nhất, $\max J_\beta=\mathbb E_x\beta\log\mathcal Z_r(x)$; (c) $r(x,y)-\beta\log\frac{\pi^*_r(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}=\beta\log\mathcal Z_r(x)$ với mọi $y$ có $\pi_{\mathrm{ref}}(y\mid x)>0$; (d) miền hỗ trợ của $\pi^*_r$ là miền hỗ trợ của $\pi_{\mathrm{ref}}$.
   - Điều kiện áp dụng: cực đại hóa riêng cho từng $x$; với lớp tham số, kết luận chỉ cho nghiệm khi $\pi^*_r$ thuộc lớp.
   - Phạm vi: nói về nghiệm, không nói thuật toán nào tìm được nó.
   - Chứng minh đầy đủ, ba bước: viết $\log\frac{\pi}{\pi_{\mathrm{ref}}}-\frac r\beta=\log\frac\pi{\pi^*_r}-\log\mathcal Z_r$; lấy kỳ vọng theo $\pi$; áp dụng Mệnh đề 10.24(a). Nguồn: DPO (4), tr. 4; Phụ lục A.1, (11)–(15), tr. 15–16. Sau định lý: GC9 (bỏ $\beta>0$: $\beta=0$ cho mọi chính sách trên tập $\arg\max r$, không duy nhất; bỏ "chọn tự do theo $x$": lớp tham số có thể không chứa $\pi^*_r$); "**Trong thực hành.**": $\mathcal Z_r(x)$ là tổng trên mọi chuỗi token, không tính được với mô hình ngôn ngữ (DPO tr. 4), nên định lý cho dạng nghiệm chứ không cho thuật toán.
6. **Ví dụ 10.26 (Nghiệm dạng đóng và vai trò của $\beta$)**: số A7(3); nhắc lại Ví dụ 10.25 để chỉ chỗ định lý bao hàm ví dụ (GC10).
7. **Nhận xét 10.58 (Hai mỏ neo, hai chiều KL)** (GC11, GC14 khái niệm với khái niệm): "**Câu hỏi.** Hệ số $\beta$ ở đây và $\beta$ của PPO-Penalty có cùng vai trò không?" Trả lời ngay: Định nghĩa 10.43 phạt $D_{\mathrm{KL}}(\pi_{\mathrm{old}}\Vert\pi_\theta)$ với $\pi_{\mathrm{old}}$ đổi sau mỗi lần cập nhật, giới hạn một bước; Định nghĩa 10.56 phạt $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ với $\pi_{\mathrm{ref}}$ cố định, quyết định nghiệm cuối. Chiều KL: $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ hữu hạn khi $\pi$ bỏ hẳn một câu trả lời ($\log\tfrac32$ cho $(1;\,0)$), vô hạn khi $\pi$ đặt xác suất lên câu trả lời mà $\pi_{\mathrm{ref}}$ không sinh; chiều ngược cho $+\infty$ với $(1;\,0)$. Bộ điều khiển $\beta$ theo KL mục tiêu của ZI §2.2 (tr. 3) đo KL tới mô hình ban đầu, khác quy tắc của Định nghĩa 10.43 đo KL tới $\pi_{\mathrm{old}}$.

### §7.3 RLHF với PPO (`lec-10-topic-27`; khoảng 900 từ; giáo trình 13.5.1, 13.5.2)

1. **Bài toán**: tập câu trả lời của mô hình ngôn ngữ quá lớn để tính $\mathcal Z_r(x)$; cần cực đại hóa $J_\beta$ bằng mẫu, tức bằng một phương pháp gradient chính sách.
2. **Bổ đề 10.59 (KL của câu trả lời bằng tổng KL theo token)**: Giả thiết: dạng (b) của Định nghĩa 10.52, độ dài không quá $T_{\max}$, $\pi_{\mathrm{ref}}>0$ ở mọi token mà $\pi>0$. Kết luận: $\log\frac{\pi(y\mid x)}{\pi_{\mathrm{ref}}(y\mid x)}=\sum_t\log\frac{\pi(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}$ và $D_{\mathrm{KL}}(\pi(\cdot\mid x)\Vert\pi_{\mathrm{ref}}(\cdot\mid x))=\mathbb E_\pi\bigl[\sum_tD_{\mathrm{KL}}(\pi(\cdot\mid S_t)\Vert\pi_{\mathrm{ref}}(\cdot\mid S_t))\bigr]$. Chứng minh đầy đủ (quy tắc nhân, tính chất tháp của Kiến thức tiên quyết). Ví dụ A7(10) ngay sau. Nối thực hành: "phạt KL theo từng token" của IG §3.5 (tr. 9) có kỳ vọng bằng KL của câu trả lời. Phân loại: bổ đề là công cụ (GC19).
3. **Mệnh đề 10.60 (Gradient của mục tiêu có phạt KL)**: Giả thiết: $\pi_\theta$ softmax, $\pi_\theta>0$, $\mathcal Y(x)$ hữu hạn, $\pi_{\mathrm{ref}}>0$. Kết luận: $\nabla_\theta J_\beta(\theta)=\mathbb E_{x,\,y\sim\pi_\theta}\bigl[\tilde r_\theta(x,y)\nabla_\theta\log\pi_\theta(y\mid x)\bigr]$ với *phần thưởng đã trừ KL* $\tilde r_\theta=r-\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$; do đó tại $\theta_{\mathrm{old}}$, gradient của $J_\beta$ bằng gradient chính sách của bài toán một bước có phần thưởng $\tilde r_{\theta_{\mathrm{old}}}$ giữ cố định. Chứng minh: lấy đạo hàm, số hạng $-\beta\mathbb E[\nabla\log\pi_\theta]=0$ theo Mệnh đề 09.17. Hệ quả cho §6: hàm thay thế mẫu của PPO với lợi thế của $\tilde r_{\theta_{\mathrm{old}}}$ có gradient đúng bằng $\nabla J_\beta$ tại $\theta_{\mathrm{old}}$ (Mệnh đề 10.41(c), với lợi thế đúng). Chỗ dẫn: DPO tr. 4 (dạng $r_\phi-\beta(\log\pi_\theta-\log\pi_{\mathrm{ref}})$ tối ưu bằng PPO); ZI (2), tr. 3; ST §3.4, tr. 6.
4. **Ví dụ 10.27 (Hai vòng PPO trên phần thưởng đã trừ KL)**: A7(4)–(5); bước tính tay trước thuật toán (GC-RL-11); "**Diễn giải.**" về hai mỏ neo.
5. **Thuật toán 10.61 (RLHF với PPO)** (GC-RL-7): Đầu vào: mô hình ngôn ngữ đã tiền huấn luyện, bản mẫu của người gán nhãn, tập lời nhắc, người gán nhãn; $\beta$; tham số của Thuật toán 10.49. Đầu ra: $\pi_\theta$. Giả thiết: dữ liệu ưu tiên theo Định nghĩa 10.53. Các bước: (1) tinh chỉnh có giám sát cho $\pi^{\mathrm{SFT}}$; đặt $\pi_{\mathrm{ref}}\leftarrow\pi^{\mathrm{SFT}}$ (giữ cố định), $\pi_\theta\leftarrow\pi^{\mathrm{SFT}}$; (2) sinh câu trả lời bằng $\pi^{\mathrm{SFT}}$, thu so sánh, khớp $\hat r$ bằng Mệnh đề 10.54, chuẩn hóa theo Nhận xét 10.55; khởi tạo critic từ $\hat r$; (3) lặp Thuật toán 10.49 trên MDP mức token với $R_{t+1}=-\beta\log\frac{\pi_{\mathrm{old}}(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}+\mathbb 1\{t+1=T\}\,\hat r(x,y)$, $\gamma=1$. Mô hình trong bộ nhớ: $\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic. Điều kiện dừng: ngân sách số lượt (IG: 256 nghìn lượt). Chi phí mỗi vòng: sinh $N$ câu trả lời bằng $\pi_{\mathrm{old}}$, một lần chạy $\hat r$ cho mỗi câu trả lời, log-xác suất của $\pi_{\mathrm{ref}}$ cho mỗi token, cộng chi phí của Thuật toán 10.49. Chỗ dẫn: IG §3.1, Hình 2 (tr. 3, 6), §3.5 (tr. 8–9), C.4 (tr. 42); ST §3.4 và chú thích 8 (tr. 6); ZI quy trình bốn bước (tr. 3). Ghi rõ đây là khung chung của các bài báo, mỗi bài khác chi tiết (ZI thu dữ liệu trực tuyến, tr. 3).
6. **Nhận xét 10.62 (Tối ưu quá mức mô hình phần thưởng)** (giáo trình 13.5.2): ST §4.3 và Hình 5 (tr. 7–8): tối ưu mạnh theo mô hình phần thưởng (KL lớn) làm ưu tiên của người gán nhãn giảm; hai vai của số hạng KL (ST §3.4, tr. 6; ZI §2, tr. 3); giá trị dùng trong IG C.4 (tr. 42): $\beta=0{,}02$, bán kính cắt $0{,}2$, một epoch trong, không chiết khấu khi tính GAE. Chỉ ghi điều bài báo đo, không khái quát (VP6).
7. **"Trong thực hành"** (GC-RL-9) sau Thuật toán 10.61: $\pi_{\mathrm{ref}}$ là bản sao đóng băng của $\pi^{\mathrm{SFT}}$; $\gamma=1$ với độ dài bị chặn thỏa (G3) của Định lý 09.23, còn các kết quả của Mục 4 giả thiết $\gamma<1$ nên không áp dụng nguyên dạng; phần thưởng thưa (chỉ ở bước cuối) cộng KL ở mọi bước; dữ liệu theo chính sách: mỗi vòng sinh mẫu mới.

### §7.4 Tối ưu ưu tiên trực tiếp (`lec-10-topic-28`; khoảng 1 200 từ; giáo trình 13.6.1)

1. **Bài toán**: Thuật toán 10.61 giữ bốn mô hình và sinh mẫu ở mọi vòng, trong khi $\hat r$ chỉ được dùng để đi tới $\pi^*_{\hat r}$. Ví dụ đảo: A7(6), từ $\pi^*$ đọc lại $\hat r$.
2. **"Một cách trực quan"**: mỗi chính sách xác định một phần thưởng mà nó là nghiệm.
3. **Mệnh đề 10.63 (Đổi biến giữa phần thưởng và chính sách)**: Giả thiết: như Định lý 10.57, thêm $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $y$. Kết luận: (a) $r=\beta\log\frac{\pi^*_r}{\pi_{\mathrm{ref}}}+\beta\log\mathcal Z_r(x)$; (b) dưới Định nghĩa 10.53, $\Pr(y\succ y'\mid x)=\sigma\bigl(\beta\log\frac{\pi^*_r(y)}{\pi_{\mathrm{ref}}(y)}-\beta\log\frac{\pi^*_r(y')}{\pi_{\mathrm{ref}}(y')}\bigr)$, không còn $\mathcal Z_r$; (c) với $r_\pi:=\beta\log(\pi/\pi_{\mathrm{ref}})$: $r_{\pi^*_r}=r-\beta\log\mathcal Z_r\in[r]$, và đó là phần tử duy nhất của $[r]$ có dạng $r_\pi$ với $\pi$ là phân phối. Chứng minh đầy đủ (lấy log Định lý 10.57(a); thế vào hiệu; tính duy nhất: $r_\pi+f=r_{\pi'}$ kéo theo $\pi e^{f/\beta}=\pi'$, lấy tổng theo $y$ được $f=0$). Nguồn: DPO (5), (6), tr. 4; A.2, tr. 16; Định lý 1, tr. 6; Mệnh đề 1, A.6, tr. 18–19.
4. **Định nghĩa 10.64 (Phần thưởng ngầm định, hàm mất mát DPO)**: $r_\theta=\beta\log\frac{\pi_\theta}{\pi_{\mathrm{ref}}}$, $\Delta r_\theta=r_\theta(x,y_w)-r_\theta(x,y_l)$, $L^{\mathrm{DPO}}(\theta)=-\widehat{\mathbb E}_{\mathcal D_{\mathrm{pref}}}\log\sigma(\Delta r_\theta)$. Đọc: $L^{\mathrm{DPO}}(\theta)=L^{\mathrm{BT}}(r_\theta)$. Chỗ dẫn: DPO (7), tr. 4; tên "implicit reward", tr. 5. Ví dụ hai câu trả lời: $\Delta r_\theta=\beta(\theta_1-\theta_2-\log2)$.
5. **Định lý 10.65 (Tương đương giữa RLHF và DPO)** — kết quả chính thứ hai ("cùng nghiệm, không cần học tăng cường"). Bốn phần:
   - Giả thiết: (H1) $\mathcal Y(x)$ hữu hạn và $\pi_{\mathrm{ref}}(y\mid x)>0$ với mọi $x$, $y$; (H2) $\beta>0$; (H3) lớp chính sách gồm mọi phân phối có miền hỗ trợ đầy đủ trên $\mathcal Y(x)$, chọn tự do theo $x$ (softmax với một logit cho mỗi cặp $(x,y)$ đủ); (H4) $L^{\mathrm{BT}}$ trên $\mathcal D_{\mathrm{pref}}$ đạt cực tiểu, và tập cực tiểu là đúng một lớp $[\hat r]$ trên mọi $(x,y)$, $y\in\mathcal Y(x)$.
   - Kết luận: (a) $\pi^*_{\hat r}$ (khớp $\hat r$, rồi giải $J_\beta$ bằng Định lý 10.57) cực tiểu $L^{\mathrm{DPO}}$; (b) mọi cực tiểu của $L^{\mathrm{DPO}}$ bằng $\pi^*_{\hat r}$; (c) $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$.
   - Điều kiện áp dụng: cực tiểu hóa chính xác cả hai hàm mất mát và giải chính xác $J_\beta$.
   - Phạm vi: không nói về các bước lặp của PPO hay của hạ gradient; khi (H4) hỏng (ưu tiên tất định, so sánh không nối mọi câu trả lời), hai con đường có thể khác nhau (Tình huống 10.5, Bài tập 10.15).
   - Chứng minh đầy đủ, bốn bước: $L^{\mathrm{DPO}}(\pi)=L^{\mathrm{BT}}(r_\pi)$; theo Mệnh đề 10.63(c) và 10.54(b), $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$; $r_{\pi^*_{\hat r}}\in[\hat r]$ cho (a); cực tiểu $\pi$ có $r_\pi\in[\hat r]$, nên $\pi=\pi_{\mathrm{ref}}e^{(\hat r+f)/\beta}$, chuẩn hóa cho $\pi=\pi^*_{\hat r}$.
   - Nguồn (ghi trong ghi chú bằng một câu dẫn ở tài liệu tham khảo, không câu nguồn gốc tại chỗ, VP18): DPO Định lý 1 (tr. 6) và phát biểu lại ở A.6 với giả thiết $\pi_{\mathrm{ref}}>0$, $\beta>0$ (tr. 18), Mệnh đề 1 (tr. 18), Bổ đề 1–2 (tr. 5; A.5, tr. 17–18), lớp chính sách không tham số (A.1, tr. 15); XU Định lý 4.1, nửa đầu chứng minh (tr. 3–4); IPO Mệnh đề 1 (tr. 4). (H4) là giả thiết do kế hoạch tách ra để kết luận (b) đúng; DPO viết "under mild assumptions" (tr. 6). Tác tử rà toán kiểm lại (QG8).
   - Sau định lý: GC9 với một phản ví dụ cho mỗi giả thiết: bỏ (H1): Bảng 1 của XU (tr. 3), $\pi_{\mathrm{ref}}(y_3)=0$ mà một cực tiểu của DPO đặt $0{,}9$ lên $y_3$; bỏ (H4): A7(8); bỏ (H3): lớp tham số không chứa $\pi^*_{\hat r}$. Kết luận của luận điểm: một câu "PPO trong RLHF và DPO giải cùng bài toán $\max J_\beta$; dưới (H1)–(H4), cả hai cho $\pi^*_{\hat r}$" (DPO §6.1, tr. 8: "DPO and PPO optimize the same objective").
6. **Mệnh đề 10.66 (Gradient của hàm mất mát DPO)**: $\nabla_\theta L^{\mathrm{DPO}}=-\beta\,\widehat{\mathbb E}\bigl[\sigma(-\Delta r_\theta)\bigl(\nabla\log\pi_\theta(y_w\mid x)-\nabla\log\pi_\theta(y_l\mid x)\bigr)\bigr]$. Chứng minh: $\frac d{dz}[-\log\sigma(z)]=-\sigma(-z)$. Nguồn: DPO tr. 5; A.4, (21)–(22), tr. 17. Đọc: trọng số lớn khi phần thưởng ngầm định xếp sai cặp; DPO tr. 5 ghi bản bỏ trọng số làm mô hình suy biến (Phụ lục, Bảng 3: chưa kiểm số liệu bảng).
7. **Ví dụ 10.28 (Một bước DPO tính tay)**: A7(7); hai bản cho cùng kết quả (bước tay và bước 1 của thuật toán); kết bằng hội tụ về $(\tfrac45;\,\tfrac15)$, trùng Ví dụ 10.26 và 10.27.
8. **Thuật toán 10.67 (DPO)** (GC-RL-7): Đầu vào: $\mathcal D_{\mathrm{pref}}$ cố định; $\pi_{\mathrm{ref}}$ đóng băng (thường là $\pi^{\mathrm{SFT}}$; khi không có, DPO tr. 5 khớp $\pi_{\mathrm{ref}}$ bằng hợp lý cực đại trên $(x,y_w)$); $\beta$; bộ tối ưu, bước học, cỡ mini-batch. Đầu ra: $\pi_\theta$. Giả thiết: (H1), (H2). Khởi tạo: $\theta\leftarrow\theta_{\mathrm{ref}}$; tính trước $\log\pi_{\mathrm{ref}}(y_w\mid x)$, $\log\pi_{\mathrm{ref}}(y_l\mid x)$. Mỗi mini-batch: log-xác suất của chuỗi bằng tổng log-xác suất token (Bổ đề 10.59); $\Delta r_\theta$; $L^{\mathrm{DPO}}$; một bước của bộ tối ưu. Điều kiện dừng: số epoch đã định (ngân sách). Chi phí mỗi bộ ba: hai lượt tính $\log\pi_\theta$ trên chuỗi có sẵn và gradient; không sinh mẫu, không mô hình phần thưởng, không critic; hai mô hình. Giá trị của bài báo (DPO Phụ lục B, tr. 20): $\beta=0{,}1$ (tóm tắt TL;DR $0{,}5$), cỡ lô 64, RMSprop, tốc độ học $10^{-6}$.
9. **Nhận xét 10.68 (Đọc kết quả của DPO)**: (1) dữ liệu nên sinh từ $\pi_{\mathrm{ref}}$ (DPO tr. 5); (2) nhầm lẫn thường gặp: DPO điều khiển hiệu $\Delta r_\theta$, không bảo đảm xác suất của $y_w$ tăng; RQ §5.4, (16), tr. 9: $\mathbb E_{\pi_{\mathrm{ref}}}r_\theta=-\beta D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)\le0$; số A7(7): $-0{,}011855$.

### §7.5 So sánh hai con đường và giới hạn (`lec-10-topic-29`; khoảng 400 từ)

1. **Bảng so sánh** (luận điểm của tác giả; P4 cho bảng bổ sung). Cột: `Tiêu chí | RLHF với PPO (Thuật toán 10.61) | DPO (Thuật toán 10.67)`. Hàng:
   - mục tiêu: $\max J_\beta$, $\pi_{\mathrm{ref}}$ cố định (cả hai, Định nghĩa 10.56);
   - đại lượng được tối ưu: $\hat r$ bằng $L^{\mathrm{BT}}$, rồi $\mathcal L^{\mathrm{CLIP}}$ với $\tilde r$ | $L^{\mathrm{DPO}}$;
   - dữ liệu: $\mathcal D_{\mathrm{pref}}$ cộng câu trả lời sinh trực tuyến từ $\pi_{\mathrm{old}}$ | chỉ $\mathcal D_{\mathrm{pref}}$, ngoại tuyến;
   - mô hình trong bộ nhớ: $\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic | $\pi_\theta$, $\pi_{\mathrm{ref}}$;
   - mỏ neo và chiều KL: $\pi_{\mathrm{ref}}$ trong mục tiêu, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})$; thêm $\pi_{\mathrm{old}}$ của phép cắt | chỉ $\pi_{\mathrm{ref}}$, qua tỉ số trong $r_\theta$;
   - điều kiện dừng: ngân sách vòng lặp | ngân sách epoch;
   - bảo đảm: gradient đúng tại $\theta_{\mathrm{old}}$ (Mệnh đề 10.60), không bảo đảm hội tụ | cực tiểu toàn cục trùng nghiệm RLHF dưới (H1)–(H4) (Định lý 10.65).
2. **Nhận xét 10.69 (Giới hạn của hai con đường)**: (a) cả hai dựa vào mô hình Bradley–Terry và miền hỗ trợ của $\pi_{\mathrm{ref}}$ (Định lý 10.57(d)); (b) DPO không đánh giá câu trả lời ngoài dữ liệu: XU Định lý 4.1 và Bảng 1 (tr. 3–4); PPO đánh giá mẫu mới bằng $\hat r$, nhưng $\hat r$ có thể sai ở đó (Nhận xét 10.62); (c) ưu tiên tất định hoặc ít dữ liệu làm (H4) hỏng: IPO §4.2 (tr. 4), Tình huống 10.5; (d) không con đường nào thăm dò ngoài miền hỗ trợ của $\pi_{\mathrm{ref}}$.
3. **Kết mục** (GC15, một phía): kết quả đã có, giới hạn còn lại, vì sao cần phần kết; không dẫn số mục sau.

### §7.6 Đọc thêm: biến thể và so sánh thực nghiệm (`lec-10-topic-30`; khoảng 200 từ)

**Nhận xét 10.70 (Biến thể và so sánh thực nghiệm)**, chỉ phát biểu điều từng bài báo nêu, ghi tên bài (VP6):
- IPO: hàm mất mát bình phương (17) đưa hiệu log-tỉ số về $\tfrac1{2\tau}$, nên nghiệm còn gần $\pi_{\mathrm{ref}}$ khi ưu tiên tất định (IPO §5, Thuật toán 1, §5.3.1, tr. 6–7); trên A7(8), $\pi(y_1)=0{,}7673$ thay cho $1$.
- Cách đọc mức token: RQ §3.1 và Định lý 1, (11) (tr. 3, 6) viết lại DPO trên MDP mức token của Định nghĩa 10.52(b).
- So sánh thực nghiệm: DPO §6.1, Hình 2 (tr. 7–8) báo DPO có đường biên phần thưởng–KL tốt hơn PPO trên bài toán sinh văn bản theo cảm xúc; XU (tóm tắt, §5, tr. 1, 6) báo PPO với chuẩn hóa lợi thế, lô lớn và trung bình trượt của mô hình tham chiếu vượt DPO trên các bài thử của họ. Hai kết quả đo trên các bài toán khác nhau; ghi chú không kết luận phương pháp nào tốt hơn.

## A9. Các chỗ sửa ở phần còn lại của ghi chú

Mọi chỗ dưới đây là phần bổ sung kéo theo; không sửa khối nào của §1–§6 ngoài các dòng liệt kê.

| Vị trí (dòng hiện tại) | Sửa | Căn cứ |
|---|---|---|
| Tiêu đề, dòng 1 | giữ `# Bài 10 — TRPO và PPO`, hoặc `# Bài 10 — TRPO, PPO và DPO` | QG9 |
| Mục tiêu học tập, dòng 3–13 | thêm mục tiêu 8, 9 (A3) | GC16, BT9 |
| Kiến thức tiên quyết, dòng 18 | câu về `exercises.md` đổi dải số theo QB1; thêm gạch đầu dòng A4 | GC16, BT4 |
| Bảng ký hiệu, dòng 42–91 | thêm các dòng A5; sửa nghĩa $\beta$; thêm nghĩa cục bộ của $x_k$, $y_k$, $y_t$; thêm tương ứng với bài báo | GC-RL-6, GC7 |
| §1.1, đoạn "bài toán trung tâm" (dòng 162) và hình `central-problem.svg` (dòng 164–166) | thêm một câu và hàng thứ ba của hình (A2) | QG4, GC-RL-2 |
| Kết §6.6 (dòng 2035, sau đoạn "Cái giá của PPO …") | thêm câu nối một phía: PPO cần phần thưởng do môi trường trả về; mục sau mở thẳng bằng bài toán | GC15, GC-RL-2 |
| `## 7. Tổng kết và chuyển tiếp` (dòng 2039) | thành `## 8. Tổng kết`; câu dẫn "Mỗi kết quả của Mục 2–6" thành "Mục 2–7" | GC-RL-15 (QG3), GC19 |
| 8.1 bảng kết quả (dòng 2048–2064) | thêm năm hàng (dưới bảng này) và câu sau bảng "Sáu hàng đầu … các hàng sau" thêm "năm hàng cuối thuộc Mục 7" | P4, GC-RL-3 |
| 8.2 bảng phương pháp (dòng 2070–2075) | tiêu đề "So sánh sáu phương pháp"; thêm hàng "RLHF với PPO (Thuật toán 10.61)" và "DPO (Thuật toán 10.67)"; bảng bảo đảm thêm hàng "DPO (Định lý 10.65)" | P4 |
| 8.3 (dòng 2087–2093) | "gồm năm phần" thành "gồm sáu phần"; thêm phần 6 (dưới bảng này) | NT15, luận điểm |
| 8.4 (dòng 2097–2105) | thêm câu hỏi 3 và lời giải ngắn: "Vì sao hệ số $\beta$ của PPO-Penalty không giữ chính sách gần $\pi_{\mathrm{ref}}$?" | GC-RL-3, NT-RL-9 |
| 8.5 (dòng 2109–2119) | câu dẫn đổi dải số; bảng thêm hàng "7. Tối ưu chính sách từ phản hồi ưu tiên"; hàng "7. Tổng kết và chuyển tiếp" thành "8. Tổng kết" | QB1, BT4 |
| 8.6 (dòng 2122–2128) | QG10: bỏ đoạn SPO, SAM+PPO và câu "Bài 11 xử lý …"; giữ một đoạn giới hạn còn lại không trỏ tới bài sau, hoặc cầu nối tới Bài 11 mới khi bài đó đã có trong kho | GC15, VP20 |
| "Ứng dụng" sau Tình huống 10.3 (dòng 2172–2175) | hai gạch đầu dòng trỏ Bài 11 cũ: bỏ hoặc viết lại theo QG10 | VP20 |
| Tình huống | thêm 10.4, 10.5 (dưới bảng này) | GC24, GC-RL-8 |
| Tóm tắt chương (dòng 2177–2226) | đoạn kể thêm hai câu (luận điểm, số $(\tfrac45;\,\tfrac15)$); "Định nghĩa và kết quả theo mục" thêm gạch Mục 7; "Công thức cần nhớ" thêm $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$ và $L^{\mathrm{DPO}}$; "Giả thiết hay bị bỏ quên" thêm hai dòng | GC-RL-3 |
| Bài tập củng cố, câu dẫn (dòng 2232) | danh sách theo mục tiêu thêm 8, 9; thêm bốn bài cuối "Mức vận dụng" (mục B2) | BT-RL-5, BT9 |
| Tài liệu tham khảo (dòng 2538–2560) | "Hướng dẫn đọc thêm" thêm một câu; thêm tám mục (dưới bảng này); mục 1 (bài giảng gốc) "Mục 7" thành "Mục 8"; mục 17 bỏ phần SPO, SAM+PPO theo QG10 | GC16, GC25 |

**Năm hàng mới của bảng 8.1** (`Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`):

| Kết quả | Giả thiết không được bỏ | Công thức |
|---|---|---|
| Hợp lý cực đại của mô hình phần thưởng (Mệnh đề 10.54) | mô hình Bradley–Terry; $0<k<n$ | $L^{\mathrm{BT}}=-\widehat{\mathbb E}\log\sigma(\hat r(x,y_w)-\hat r(x,y_l))$; cực tiểu $\log\frac k{n-k}$ |
| Nghiệm có phạt KL (Định lý 10.57) | $\beta>0$; chính sách chọn tự do theo $x$ | $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$; $J_\beta(\pi)=\beta\log\mathcal Z_r-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r)$ |
| Gradient có phạt KL (Mệnh đề 10.60) | $\pi_\theta>0$; $\pi_{\mathrm{ref}}>0$ | $\nabla J_\beta=\mathbb E[(r-\beta\log\frac{\pi_\theta}{\pi_{\mathrm{ref}}})\nabla\log\pi_\theta]$ |
| Tương đương RLHF và DPO (Định lý 10.65) | (H1)–(H4) | $\arg\min L^{\mathrm{DPO}}=\{\pi^*_{\hat r}\}$ |
| Gradient DPO (Mệnh đề 10.66) | $\beta>0$ | $-\beta\widehat{\mathbb E}[\sigma(-\Delta r_\theta)(\nabla\log\pi_\theta(y_w)-\nabla\log\pi_\theta(y_l))]$ |

**Phần 6 của 8.3** (bản nháp): "6. Khi phần thưởng chỉ được biết qua so sánh ưu tiên, RLHF với PPO và DPO cực đại hóa cùng mục tiêu có phạt KL theo chính sách tham chiếu cố định, có nghiệm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57); PPO đi tới nghiệm bằng mẫu sinh trực tuyến và bốn mô hình, DPO cực tiểu hóa một hàm mất mát phân loại trên dữ liệu cố định, và hai con đường cho cùng chính sách dưới (H1)–(H4) (Định lý 10.65), không khi ưu tiên tất định (Tình huống 10.5)."

**Tình huống 10.4 (Chọn bản tóm tắt bằng dữ liệu ưu tiên)** (GC24): bài toán A7(9); mô hình hóa theo Định nghĩa 10.52(a), 10.53; kiểm giả thiết (H1) $\pi_{\mathrm{ref}}>0$, (H4) mỗi cặp có cả hai kết quả và ba cặp nối ba câu trả lời; áp dụng Mệnh đề 10.54, Định lý 10.57, 10.65; diễn giải: với $\beta=1$, bản thứ nhất được chọn với xác suất $0{,}7143$ thay cho $0{,}5$, bản thứ ba còn $0{,}0714$; giới hạn: một lời nhắc, ba câu trả lời; với mô hình ngôn ngữ, $\mathcal Z$ không tính được và lời giải phải đi qua Thuật toán 10.61 hoặc 10.67.

**Tình huống 10.5 (Vi phạm giả thiết: ưu tiên tất định từ ít dữ liệu)** (GC-RL-8): bài toán A7(8); kiểm giả thiết: (H4) hỏng vì $k=n=3$; hậu quả: DPO đẩy $\pi_\theta(y_1)\to1$ với mọi $\beta$, $J_1$ theo phần thưởng thật giảm từ $0{,}5108$ (nghiệm) về $0{,}2877$, KL theo chiều của mục tiêu tiến tới $0{,}4055$; con đường RLHF cũng không có ước lượng hợp lý cực đại hữu hạn, còn mô hình phần thưởng có điều chuẩn (CH §2.2.3, tr. 5: điều chuẩn $\ell_2$) cho $\hat r$ hữu hạn và nghiệm có $\pi(y_2)>0$ (IPO §4.2, tr. 4). Nêu nguyên nhân bằng giả thiết (VP18), không khuyến nghị thực hành ngoài nguồn.

**Tài liệu tham khảo mới** (GC25: tác giả, năm, tên, mục, trang; mục nào của chương dựa trên nguồn nào):

18. Rafailov và cộng sự. "Direct Preference Optimization: Your Language Model is Secretly a Reward Model." *NeurIPS* 2023 (arXiv 2305.18290). §3–5, (1)–(9), Định nghĩa 1, Bổ đề 1–2, Định lý 1, Phụ lục A.1–A.6, B: Mục 7.1–7.5.
19. Ouyang và cộng sự. "Training language models to follow instructions with human feedback." arXiv 2203.02155, 2022. §3.1, §3.5, (1)–(2), Phụ lục C.4: Mục 7.1, 7.3.
20. Stiennon và cộng sự. "Learning to summarize from human feedback." *NeurIPS* 2020 (arXiv 2009.01325). §3.4, §4.3: Mục 7.1–7.3.
21. Ziegler và cộng sự. "Fine-Tuning Language Models from Human Preferences." arXiv 1909.08593, 2019. §2, (1)–(2), §2.2: Mục 7.1–7.3.
22. Christiano và cộng sự. "Deep Reinforcement Learning from Human Preferences." arXiv 1706.03741, 2017. §2.2.3, (1): Mục 7.1.
23. Gheshlaghi Azar và cộng sự. "A General Theoretical Paradigm to Understand Learning from Human Preferences." arXiv 2310.12036, 2023. Mệnh đề 1, §4.2, §5, (17): Mục 7.5–7.6, Tình huống 10.5.
24. Xu và cộng sự. "Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study." arXiv 2404.10719, 2024. Định lý 4.1, Bảng 1, §5: Mục 7.4–7.6.
25. Rafailov, Hejna, Park, Finn. "From $r$ to $Q^*$: Your Language Model is Secretly a Q-Function." *COLM* 2024 (arXiv 2404.12358). §3.1, Định lý 1, §5.4: Mục 7.4, 7.6.

Tên đầy đủ các tác giả lấy từ trang đầu của bản đã lưu khi soạn; nơi công bố của 19, 22, 23, 24 chỉ thêm sau khi kiểm. Câu "Hướng dẫn đọc thêm" (bản nháp): "Mục 7 dựa vào Rafailov và cộng sự (2023, §3–5, Phụ lục A); quy trình RLHF theo Ouyang và cộng sự (2022, §3) và Stiennon và cộng sự (2020, §3.4)."

## A10. Bảng thuật ngữ Việt–Anh của phần mới (GC-RL-13, VP2–VP4; chép sang `outline.md`)

Đã kiểm: ghi chú, bài tập, deck Bài 01–10 không dùng thuật ngữ nào dưới đây với nghĩa này. "Chính sách tham chiếu" đã xuất hiện ở BT-RL-7 và trong `review-log.md` Bài 04, 08 với nghĩa "chính sách đối chứng trong notebook"; trong Bài 10 chỉ có nghĩa của Mục 7. Các khóa học khác trong workspace không có bản dịch cho "prompt" theo nghĩa mô hình ngôn ngữ (QG11).

| Tiếng Việt | Tiếng Anh | Quy ước |
|---|---|---|
| lời nhắc; câu trả lời | prompt; response, completion | $x$; $y$ (QG11) |
| token; tập token | token; vocabulary | giữ "token" như "entropy", "critic" |
| dữ liệu ưu tiên; phép so sánh ưu tiên | preference data; pairwise comparison | $\mathcal D_{\mathrm{pref}}$; như mục lục 13.4.2 |
| câu trả lời được chọn, bị loại | preferred, dispreferred completion | $y_w$, $y_l$ |
| mô hình Bradley–Terry | Bradley–Terry model | tên riêng |
| mô hình phần thưởng | reward model | $\hat r$; như mục lục 13.4.1 |
| lớp tương đương của phần thưởng | reward equivalence class | $[r]$ |
| chính sách tham chiếu | reference policy, reference model | $\pi_{\mathrm{ref}}$ |
| tinh chỉnh có giám sát (SFT) | supervised fine-tuning | $\pi^{\mathrm{SFT}}$ |
| học tăng cường từ phản hồi con người (RLHF) | reinforcement learning from human feedback | theo mục lục 13.5 (QG11) |
| mục tiêu có phạt KL | KL-regularized objective, KL-constrained reward maximization | $J_\beta$ |
| hàm phân hoạch | partition function | $\mathcal Z_r(x)$ |
| phần thưởng đã trừ KL | KL-penalized reward | $\tilde r_\theta$ |
| phạt KL theo từng token | per-token KL penalty | IG §3.5 |
| tối ưu quá mức mô hình phần thưởng | reward model over-optimization | như mục lục 13.5.2 |
| tối ưu ưu tiên trực tiếp (DPO) | Direct Preference Optimization | tên đầy đủ ở lần đầu, sau đó "DPO" |
| phương pháp căn chỉnh trực tiếp; căn chỉnh | direct alignment methods; alignment | như mục lục 13.6 |
| phần thưởng ngầm định | implicit reward | $r_\theta$ |
| đổi biến phần thưởng | reparameterization | |
| ưu tiên tất định | deterministic preference | $\Pr(y_1\succ y_2)=1$ |
| tối ưu ưu tiên đồng nhất (IPO) | Identity Preference Optimization, ΨPO | chỉ ở §7.6 |
| MDP mức token | token-level MDP | Định nghĩa 10.52(b) |
| ngoại tuyến; trực tuyến | offline; online | dữ liệu cố định; mẫu sinh trong khi học |

## A11. Hình (SVG trong `2627-1/img/lec-10/`; GC12, VP10, NT25)

| Tệp | Nội dung | Dùng ở |
|---|---|---|
| `rlhf-dpo-hai-con-duong.svg` (mới) | từ $\mathcal D_{\mathrm{pref}}$ hai nhánh: nhánh trên, nét liền: mô hình phần thưởng (Mệnh đề 10.54) → PPO với $\pi_{\mathrm{ref}}$, critic, mẫu trực tuyến (Thuật toán 10.61); nhánh dưới, nét đứt: $L^{\mathrm{DPO}}$ với $\pi_{\mathrm{ref}}$ (Thuật toán 10.67); hai nhánh gặp ở khung đậm $\pi^*\propto\pi_{\mathrm{ref}}e^{r/\beta}$ (Định lý 10.57, 10.65); chữ ghi số mô hình trong bộ nhớ của mỗi nhánh (4 và 2) | đầu §7.4 hoặc §7.5; `L10-D15` (bản `-slide.svg` nếu chữ dưới 16 px ở 390 px) |
| `muc-tieu-phat-kl.svg` (mới, tùy chọn) | $J_1(p)$ trên $p\in(0;\,1)$ của A7(2): cực đại $0{,}5108$ tại $p=0{,}8$; ba điểm $\pi_{\mathrm{ref}}$ $(0{,}6667;\,0{,}4621)$, $(0{,}8;\,0{,}5108)$, tham lam $(1;\,0{,}2877)$; đường nét đứt $\mathbb E\hat r=p\log2$ | Ví dụ 10.26; `L10-D07` |
| `central-problem.svg` (sửa, QG4) | thêm hàng thứ ba "Mục 7: phạt KL theo $\pi_{\mathrm{ref}}$ cố định — RLHF với PPO, DPO" nối vào khung PPO | §1.1; `L10-110` |

Script vẽ đặt ở `tools/courses/rl-plan/2627-1/img/lec-10/` (theo prompt), không vào repo. Công thức trong hình chỉ là nhãn ngắn; mọi công thức đầy đủ ở KaTeX (NT25).

## A12. Độ dài (GC-RL-4; QG2)

Đã đo (`count_note_words.py 10`): 29 302 từ `prose`; còn 698 từ tới trần 30 000. Số từ theo mục (đo bằng cùng hàm đếm): §6.1 1 618, §6.2 685, §6.3 1 724, §6.4 546, §6.5 567, §6.6 513, §7 hiện có tổng 1 104, Tình huống 889, Tóm tắt 739, Bài tập củng cố 1 935, tài liệu tham khảo 657.

**Ngân sách đề xuất:**

| Phần | Từ `prose` |
|---|---|
| §7.1 / 7.2 / 7.3 / 7.4 / 7.5 / 7.6 | 900 / 900 / 900 / 1 200 / 400 / 200 (tổng 4 500; trần cứng 5 000) |
| Bốn bài tập củng cố mới | 1 300 |
| Tình huống 10.4, 10.5 | 800 |
| Mục tiêu, tiên quyết, ký hiệu, §1.1, kết §6.6 | 350 |
| §8, Tóm tắt, tài liệu tham khảo | 500 |
| Trừ: §7.6 cũ và "Ứng dụng" theo QG10 | khoảng −150 |
| **Tổng thêm** | **khoảng 7 300 → ghi chú khoảng 36 600** |

**Phương án:**

- (a) **Đề xuất:** ngoại lệ trần cho Bài 10 là 37 000 từ `prose`, ghi vào GC-RL-4 của `NGUYEN-TAC-HOC-PHAN.md` (người dùng, ngày, lý do: bổ sung theo yêu cầu tác giả). Giữ §1–§6 nguyên vẹn.
- (b) Bản gọn: §7 3 300 từ (gộp 7.5 vào kết 7.4, §7.6 còn hai câu, Nhận xét 10.55 và 10.62 mỗi nhận xét ba câu), ba bài tập, một tình huống mới (10.5); tổng khoảng 34 500, cần trần 35 000. Mất phần 13.4.2 và 13.5.2 của mục lục ở mức chi tiết.
- (c) Giữ trần 30 000: phải cắt khoảng 7 000 từ của §1–§6 (gần một phần tư nội dung cũ, kể cả khối có số hiệu mà VP21 không cho cắt và deck dẫn tới). Không đề xuất.

Không thêm nội dung chỉ để dùng phần trần được nới (GC-RL-4).

---

# B. Bài tập

## B1. Bài của giáo trình (BT-RL-1, BT8): đã kiểm

- **Sutton và Barto (2018)**: không có bài về dữ liệu ưu tiên, RLHF hay DPO. Bài gần nhất là **Bài tập 2.9** (§2.8, trang PDF 59, trang in 37, dòng 2550 của bản trích): "Show that in the case of two actions, the soft-max distribution is the same as that given by the logistic, or sigmoid, function". Với hai câu trả lời, mô hình Bradley–Terry là đúng phân phối softmax trên hai phần thưởng, nên bài kiểm phần nhận biết của mục tiêu 8 (Định nghĩa 10.53). Bài chưa dùng ở `exercises.md` nào (đã tìm "Bài tập 2.9" trong `materials/`). Bài 13.5 (đơn vị Bernoulli–logistic, §13.7, tr. 336) đã là bài của `exercises.md` Bài 09, không dùng lại (BT1). Đề giữ nguyên câu chữ của sách; lời giải tự viết theo ký hiệu của ghi chú (BT7), "Kiểm tra lại" có thể nối với Định nghĩa 10.53 (QB2).
- **Goodfellow, Bengio và Courville (2016)**: sách không có bài tập. **Puterman, Bertsekas, Szepesvári, Bertsekas và Tsitsiklis**: không trình bày chủ đề.
- Kết luận (BT9, BT-RL-1): mục tiêu 8 có một bài sách ở mức nhận biết; phần còn lại của mục tiêu 8 và toàn bộ mục tiêu 9 dựa vào bài tập của ghi chú; ghi lý do vào `review-log.md`.

## B2. Bài tập củng cố mới của ghi chú (BT-RL-5, BT2, BT5, BT6)

Bốn bài, đặt cuối `### Mức vận dụng`, sau Bài tập 10.12, để số hiệu tăng theo thứ tự đọc (GC19). Số hiệu theo phương án 1 của QB1 (10.13–10.16); theo phương án 2 là 10.18–10.21. Mỗi bài: một `hint`, một `solution` chia "**Câu (a).**", kết bằng "**Kiểm tra lại.**" (theo mẫu các bài 10.1–10.12). Đề tự chứa (GC23).

**Bài tập 10.13 (Nghiệm có phạt KL trên ba câu trả lời).** Mục tiêu 8. Dữ kiện: một lời nhắc, $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, $r=(\log2;\,0;\,0)$.
- (a) Với $\beta=1$, tính $\mathcal Z$, $\pi^*$, $\max J_1$; kiểm bằng $\mathbb E_{\pi^*}r-D_{\mathrm{KL}}(\pi^*\Vert\pi_{\mathrm{ref}})$.
- (b) Tính phần thưởng ngầm định $\beta\log(\pi^*/\pi_{\mathrm{ref}})$ và chỉ ra nó thuộc $[r]$.
- (c) Lặp lại (a) với $\beta=\tfrac12$.
- Lời giải: (a) $\pi_{\mathrm{ref}}e^r=(1;\,\tfrac14;\,\tfrac14)$, $\mathcal Z=\tfrac32$, $\pi^*=(\tfrac23;\,\tfrac16;\,\tfrac16)$, $\max J_1=\log\tfrac32=0{,}405465$; kiểm $\tfrac23\log2=0{,}462098$, $D_{\mathrm{KL}}=\tfrac23\log\tfrac43+2\cdot\tfrac16\log\tfrac23=0{,}191788-0{,}135155=0{,}056633$, hiệu $0{,}405465$. (b) $(\log\tfrac43;\,\log\tfrac23;\,\log\tfrac23)=(0{,}287682;\,-0{,}405465;\,-0{,}405465)=r-\log\tfrac32$. (c) $\pi_{\mathrm{ref}}e^{2r}=(2;\,\tfrac14;\,\tfrac14)$, $\mathcal Z=\tfrac52$, $\pi^*=(0{,}8;\,0{,}1;\,0{,}1)$, $\max J_{1/2}=\tfrac12\log\tfrac52=0{,}458145$.
- Kiểm tra lại: lỗi chuẩn hóa bằng $\sum e^{r/\beta}$ thay cho $\sum\pi_{\mathrm{ref}}e^{r/\beta}$ cho $\pi^*=(\tfrac12;\,\tfrac14;\,\tfrac14)$ ở (a); lỗi dùng $e^{\beta r}$ thay cho $e^{r/\beta}$ ở (c) cho $(\tfrac{\sqrt2}{\sqrt2+1};\,\dots)$, sai chiều tác dụng của $\beta$.

**Bài tập 10.14 (Hàm mất mát DPO với hai câu trả lời).** Mục tiêu 9. Dữ kiện: $\pi_{\mathrm{ref}}$ là chính sách softmax với $\theta_{\mathrm{ref}}=(\log2;\,0)$, tức $(\tfrac23;\,\tfrac13)$; $n$ phép so sánh giữa $y_1$ và $y_2$, $k$ phép chọn $y_1$.
- (a) Chứng minh: nếu $0<k<n$, $L^{\mathrm{DPO}}$ đạt cực tiểu đúng khi $\beta(\theta_1-\theta_2-\log2)=\log\frac k{n-k}$, và chính sách đó là $\pi^*_{\hat r}$ của con đường RLHF (Mệnh đề 10.54(c), Định lý 10.57).
- (b) Với $n=5$, $k=4$, $\beta=1$: tính chính sách cực tiểu, gradient tại $\theta_{\mathrm{ref}}$, và một bước hạ gradient với bước học $1$.
- (c) Với $k=n$: chứng minh $L^{\mathrm{DPO}}$ không có cực tiểu.
- Lời giải: (a) $L^{\mathrm{DPO}}=-\tfrac1n[k\log\sigma(\Delta)+(n-k)\log\sigma(-\Delta)]$ với $\Delta=\beta(\theta_1-\theta_2-\log2)$; đạo hàm theo $\Delta$ là $\sigma(\Delta)-\tfrac kn$; con đường RLHF cho $\hat r(y_1)-\hat r(y_2)=\log\frac k{n-k}$ và $\pi^*(y_1)/\pi^*(y_2)=2\bigl(\frac k{n-k}\bigr)^{1/\beta}$, trùng. (b) $\Delta=\log4$, $\theta_1-\theta_2=\log8$, $\pi=(\tfrac89;\,\tfrac19)$; gradient theo $\theta$ là $-\beta(\tfrac45-\tfrac12)(1;\,-1)=(-0{,}3;\,0{,}3)$; sau một bước $\theta_1-\theta_2=\log2+0{,}6=1{,}293147$, $\pi_\theta(y_1)=0{,}784679$, $L^{\mathrm{DPO}}$ từ $0{,}693147$ xuống $0{,}557488$, cực tiểu $0{,}500402$. (c) $-\log\sigma(\Delta)>0$ và giảm ngặt về $0$.
- Kiểm tra lại: quên $\log\pi_{\mathrm{ref}}$ cho cực tiểu $\theta_1-\theta_2=\log4$, $\pi=(0{,}8;\,0{,}2)$; nhầm dấu trọng số cho gradient $(0{,}3;\,-0{,}3)$, làm giảm $\pi(y_1)$.

**Bài tập 10.15 (Dữ liệu không phủ một câu trả lời).** Mục tiêu 9 (giả thiết của Định lý 10.65). Dữ kiện: $\pi_{\mathrm{ref}}=(\tfrac12;\,\tfrac14;\,\tfrac14)$, $\beta=1$; $\mathcal D_{\mathrm{pref}}$ chỉ gồm sáu so sánh giữa $y_1$ và $y_2$, bốn chọn $y_1$; không so sánh nào chứa $y_3$.
- (a) Chứng minh mọi chính sách có $\pi(y_1)=4\pi(y_2)>0$ đều cực tiểu $L^{\mathrm{DPO}}$.
- (b) Tính $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$ cho ba cực tiểu $(\tfrac23;\,\tfrac16;\,\tfrac16)$, $(0{,}6;\,0{,}15;\,0{,}25)$, $(0{,}4;\,0{,}1;\,0{,}5)$.
- (c) Con đường RLHF: $\hat r(y_1)-\hat r(y_2)=\log2$, còn $\hat r(y_3)=c$ không được dữ liệu xác định; viết $\pi^*_{\hat r}$ theo $c$ và chỉ ra giả thiết nào của Định lý 10.65 không thỏa.
- Lời giải: (a) $\Delta r_\theta$ chỉ phụ thuộc $\pi(y_1)/\pi(y_2)$; cực tiểu khi $\log\frac{\pi(y_1)/\pi(y_2)}{2}=\log2$. (b) $0{,}056633$; $0{,}032770$; $0{,}165687$. (c) $\pi^*\propto(1;\,\tfrac14;\,\tfrac14e^c)$: $c=0$ cho $(\tfrac23;\,\tfrac16;\,\tfrac16)$, $c=\log2$ cho $(\tfrac47;\,\tfrac17;\,\tfrac27)$, $c=-\log2$ cho $(\tfrac8{11};\,\tfrac2{11};\,\tfrac1{11})$; tập cực tiểu của $L^{\mathrm{BT}}$ không là một lớp $[\hat r]$, nên (H4) hỏng; hai con đường đều không xác định $\pi(y_3)$ từ dữ liệu.
- Kiểm tra lại: kết luận "DPO cho $\pi(y_3)=\pi_{\mathrm{ref}}(y_3)$" sai vì $L^{\mathrm{DPO}}$ không chứa $\pi(y_3)$; với lớp tham số chung tham số giữa các câu trả lời, $\pi(y_3)$ còn đổi theo các bước gradient.

**Bài tập 10.16 (Hai mỏ neo khi bán kính cắt nhỏ).** Mục tiêu 8 (phân biệt chính sách cũ và chính sách tham chiếu). Dữ kiện như Ví dụ 10.27 với $\epsilon=0{,}1$: $\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$, $\hat r=(\log2;\,0)$, $\beta=1$, bộ đệm $y_1,y_1,y_2$ đúng tần suất của $\pi_{\mathrm{old}}$, mỗi vòng cực đại hóa $\mathcal L^{\mathrm{CLIP}}$ từ $\pi_{\mathrm{old}}$ tới biên đầu tiên của đoạn phẳng.
- (a) Tính $p$ sau vòng 1, 2, 3 và lợi thế của mỗi vòng.
- (b) So các giá trị $J_1$ với $\max J_1=0{,}510826$.
- (c) Giải thích vì sao phép cắt không làm dãy dừng ở $p=0{,}8$.
- Lời giải: vòng 1 từ $\tfrac23$: lợi thế $(0{,}231049;\,-0{,}462098)$, $p=1{,}1\cdot\tfrac23=0{,}733333$; vòng 2: phần thưởng đã trừ KL $(0{,}597837;\,0{,}223144)$, lợi thế $(0{,}099918;\,-0{,}274775)$, $p=1{,}1\cdot0{,}733333=0{,}806667$; vòng 3: phần thưởng $(0{,}502527;\,0{,}544727)$, lợi thế $(-0{,}008159;\,0{,}034042)$, $p=0{,}9\cdot0{,}806667=0{,}726000$. $J_1=0{,}497919$; $0{,}510686$; $0{,}495034$ (đúng bằng giá trị $v$ của phần thưởng đã trừ KL). (c) Phép cắt chỉ chặn độ dài bước so với $\pi_{\mathrm{old}}$; dấu của lợi thế do $\pi_{\mathrm{ref}}$ quyết định đổi khi $p$ vượt $0{,}8$, nhưng mỗi vòng vẫn đi hết tới biên của khoảng cắt.
- Kiểm tra lại: tính phần thưởng đã trừ KL theo $\pi_{\mathrm{ref}}$ thay cho $\pi_{\mathrm{old}}$ ở vòng 2 cho lợi thế của vòng 1 và $p$ tiếp tục tăng; cắt theo $\pi_{\mathrm{ref}}$ thay cho $\pi_{\mathrm{old}}$ cho $p$ dừng ở $0{,}733333$.

Lý do không có bài nhận biết mới trong ghi chú: bài nhận biết đặt ở giữa "Mức nhận biết" làm số hiệu không tăng theo thứ tự đọc (GC19); phần nhận biết dựa vào Bài tập 2.9 của sách (B1), câu hỏi tự kiểm tra mới ở §8.4 và trang `L10-708` (QB3).

## B3. Số hiệu và mọi chỗ phải sửa (BT4; QB1)

BT4 có hai câu mâu thuẫn trong lượt này: "bài trong `exercises.md` tiếp nối sau bài tập cuối cùng của ghi chú" và "Không đánh lại số đã công bố". `exercises.md` Bài 10 đã lên `index.html` (dòng 331).

**Phương án 1 (đề xuất, cần ngoại lệ BT4 ghi vào `NGUYEN-TAC-HOC-PHAN.md`):** ghi chú 10.1–10.16; `exercises.md` đánh lại: 10.13 → 10.17; bài mới (Sách 2.9) 10.18; 10.14 → 10.19; 10.15 → 10.20; 10.16 → 10.21; 10.17 → 10.22. Chỉ chọn nếu tác giả xác nhận chưa giao bài cho sinh viên theo số cũ.

**Phương án 2 (giữ số đã công bố):** ghi chú thêm 10.18–10.21 sau 10.12 (tăng theo thứ tự đọc, có khoảng trống); `exercises.md` giữ 10.13–10.17; Bài tập 2.9 của sách không thêm, hoặc thêm thành 10.22 ở cuối "Mức nhận biết" (số không tăng trong tệp). Câu quy ước ở Kiến thức tiên quyết ghi hai dải.

**Chỗ phải sửa theo phương án 1** (chỉ đổi số của **bài tập**; không đổi "Định nghĩa 10.13", "Mệnh đề 10.14", "Thuật toán 10.16", "Ví dụ 10.13"–"Ví dụ 10.17" cùng xuất hiện trong hai tệp; thay theo thứ tự từ số lớn xuống số nhỏ để tránh đè):

- `lecture-note.md`: dòng 18 ("Bài tập 10.13–10.17 thuộc tệp bài tập"); §8.5 dòng 2109 (câu dẫn) và bảng dòng 2111–2119 (cột "Tệp bài tập": 10.14 ×2, 10.13, 10.15, 10.16, 10.17); câu dẫn "Bài tập củng cố" dòng 2232.
- `exercises.md`: đoạn mở dòng 3 (số bài, dải, các mức); bảng dòng 6–13; mọi tiêu đề `### Bài tập 10.k.` và `::: exercise Bài tập 10.k` (dòng 29, 35, 62, 68, 126, 132, 179, 185, 238, 244); các chỗ bài này dẫn bài kia trong đề hoặc lời giải (dòng 21, 42, 46, 55, 82, 86, 133, 143, 147, 170, 200, 204, 257, 261: tác tử kiểm từng dòng, nhiều dòng là số khối, không đổi); tài liệu tham khảo dòng 288.
- Deck (giai đoạn III, ghi thành đề xuất ở giai đoạn II): bảng `L10-709` (dòng 1047–1051 của HTML) và ghi chú diễn giả `L10-709` (dòng 1054: "10.13–10.17", "(10.13)", "(10.14–10.17)", "Bài tập 10.14").
- Planning: `outline.md` (2 dòng), `storyboard.md` (2 dòng) của Bài 10. Không sửa `planning/lec-11/*` (phiên khác): `prompt-xay-dung-bai-11.md` dòng 11 dẫn "10.13–10.17" là mô tả trạng thái, báo cho phiên Bài 11.

## B4. Bảng phủ mục tiêu học tập (BT9, GC26; số theo phương án 1)

| Mục tiêu | Kết quả hoặc ví dụ của ghi chú | Bài tập của ghi chú | `exercises.md` | Trên deck |
|---|---|---|---|---|
| 1–7 | như hiện có | như câu dẫn hiện có | 10.17, 10.19–10.22 (số mới) | như hiện có |
| 8. Phần thưởng từ dữ liệu ưu tiên, mục tiêu có phạt KL | Mệnh đề 10.54, Định lý 10.57, Mệnh đề 10.60, Thuật toán 10.61; Ví dụ 10.23–10.27 | 10.13, 10.16 | 10.18 (Sách 2.9) | `L10-D17`, `L10-D18` (Bài tập 10.13) |
| 9. Tối ưu ưu tiên trực tiếp | Mệnh đề 10.63, Định lý 10.65, Mệnh đề 10.66, Thuật toán 10.67; Ví dụ 10.28; Tình huống 10.4, 10.5 | 10.14, 10.15 | — (không có bài sách, BT9) | `L10-D13` (Ví dụ 10.28), `L10-D16` |

Câu dẫn mới của "Bài tập củng cố": "Các bài phủ chín mục tiêu học tập: … 8 (10.13, 10.16), 9 (10.14, 10.15)."

## B5. Sửa `exercises.md` (BT3, BT-RL-3, BT-RL-4; giai đoạn II)

- Đoạn mở: "Tệp gồm sáu bài, Bài tập 10.17–10.22, đánh số tiếp theo mười sáu bài tập của ghi chú …"; các mức: nhận biết (10.17, 10.18); tính toán hoặc chứng minh (10.19–10.22); một câu: mục tiêu 9 dựa vào Bài tập 10.14, 10.15 của ghi chú vì các giáo trình của học phần không có bài về DPO.
- Bảng `Mạch | Mở phần | Bài tập`: thêm hàng `7. Tối ưu chính sách từ phản hồi ưu tiên | [Mở phần](lecture-10-trpo-va-ppo.html#/7/1) | 10.18; ghi chú: 10.13–10.16`; hàng cuối thành `8. Tổng kết | [Mở phần](lecture-10-trpo-va-ppo.html#/8/1) | ghi chú: 10.3`. Liên kết `#/7/1`, `#/8/1` chỉ đúng sau giai đoạn III; điền ở giai đoạn II, kiểm lại sau deck (BT-RL-9).
- "Hướng dẫn và ký hiệu": thêm một đoạn cho Bài tập 10.18: hàm logistic $\sigma$, phân phối softmax trên hai hành động; sách viết ưu tiên hành động $H_t(a)$ (§2.8), ghi chú viết logit $\theta$.
- Bài mới `### Bài tập 10.18. Softmax hai hành động và hàm logistic`: "**Mức độ:** nhận biết; mục tiêu học tập 8; mạch 7."; "**Nguồn:** Sutton và Barto (2018), Bài tập 2.9, §2.8, trang 37."; đề dịch sát câu của sách; một `hint` (chia tử và mẫu cho $e^{H(a_1)}$); `solution`: $\frac{e^{H_1}}{e^{H_1}+e^{H_2}}=\frac1{1+e^{-(H_1-H_2)}}=\sigma(H_1-H_2)$; "**Kiểm tra lại.**": nhầm dấu cho $\sigma(H_2-H_1)$; hai lỗi thường gặp. Không thêm câu tự dựng nối với Bradley–Terry vào đề (BT-RL-1); câu nối nếu có chỉ trong lời giải, dẫn Định nghĩa 10.53 (QB2).
- Tài liệu tham khảo cuối tệp: thêm "§2.8, Bài tập 2.9 (tr. 37)".

## B6. Bài tập trên trang chiếu (NT24, NT-RL-10, BT11)

- Cụm khái niệm "mục tiêu có phạt KL và DPO" có một bài với "Lời giải:" trên mặt trang: **Bài tập 10.13** (a)–(b) trên `L10-D17` (đề) và `L10-D18` (lời giải), giữ dữ liệu, câu chữ, kết quả của ghi chú; ghi chú diễn giả của `L10-D17` nêu năng lực kiểm tra và một dòng "Gợi ý:" (NT-RL-10). Câu (c) để tự làm, đáp số trong ghi chú diễn giả.
- Ví dụ 10.28 là trang "Ví dụ: …", không phải "Bài tập" (NT24).
- Bảng "Bài tập về nhà" (`L10-709`): hàng mạch 7 ghi `10.18` (tệp bài tập) và `10.13 (trên lớp), 10.14, 10.15, 10.16` (ghi chú).
- `exercises.md` không lặp Bài tập 10.13, nên không có dòng "Trùng trang chiếu" mới (BT11 áp dụng cho bài của tệp xuất hiện trên deck).

---

# C. Trang chiếu

Deck 10 là deck đã có, giữ quy định cũ trừ các trang mới (mục 3 của `NGUYEN-TAC-HOC-PHAN.md`); trang mới theo NT1–NT28 và P1–P11 với ngoại lệ nguồn QG1 (ghi chú là chuẩn duy nhất của mạch mới). Mọi `data-slide-id` đã có được giữ.

## C1. Bảng mạch (NT10, NT12, NT13)

| Mạch | Tên (trang tiêu đề) | Câu hỏi của mạch | Đầu vào | Đầu ra | Đóng góp cho bài toán trung tâm | Trang | Phút |
|---|---|---|---|---|---|---:|---:|
| 1–6 | như hiện có | | | | | 89 | 111 → 100 (C4) |
| **7** | **Tối ưu chính sách từ phản hồi ưu tiên** (`L10-D00`, `id="mach-7"`) | Khi chỉ có so sánh ưu tiên, chính sách nào cực đại phần thưởng mà vẫn gần chính sách tham chiếu, và có cần học tăng cường trực tuyến để tìm nó không? | Thuật toán 10.49; phạt KL của Định nghĩa 10.43; KL và Mệnh đề 10.24 | Định lý 10.57, 10.65; Thuật toán 10.61, 10.67; bảng so sánh | nửa thứ ba (QG4): cùng phép phạt KL, mỏ neo cố định | 19 | 22 |
| **8** | **Tổng kết** (`L10-700`, `id="mach-8"`; QT5 về tên) | như hiện có | thêm Mục 7 | bảng thêm hàng Mục 7 | trả lời cả sáu phần | 12 (hoặc 14, QT6) | 9 → 10 |

Dòng dẫn của `L10-D00` (bản nháp, ≤ 25 âm tiết, không khuôn "Muốn …, phải …", khác khuôn câu của các mạch khác): "Cùng một mục tiêu có phạt KL được giải bằng PPO với mẫu trực tuyến hoặc bằng DPO trên dữ liệu cố định." (23 âm tiết theo khoảng trắng; tác tử đếm lại bằng `deck_lint.py`). `p.strand-keys`: "Bradley–Terry · Phạt KL · RLHF với PPO · DPO · Hai mỏ neo". Ghi chú diễn giả 40–100 âm tiết: kết quả kế thừa (Thuật toán 10.49, Định nghĩa 10.43), việc của mạch, kết quả trao cho "Tổng kết".

## C2. Danh sách trang của mạch 7 (mã mới; NT8 hành trình khái niệm)

Mã `L10-Dmm`: tiền tố mạch `L10-D`, trang tiêu đề `L10-D00` theo mẫu `<tiền tố mạch>00` của P7; chữ cái theo tiền lệ deck 05 (`L05-B00`, `L05-DT`); không dùng `L10-8xx` vì "Tổng kết" giữ `L10-7xx` (QT2). Mỗi trang có `data-note-topic-id` của tiểu mục.

| Mã | Tiêu đề | Bước NT8 | Nội dung mặt trang | Khối ghi chú | Phút |
|---|---|---|---|---|---:|
| `L10-D00` | 7. Tối ưu chính sách từ phản hồi ưu tiên | tiêu đề mạch | C1 | §7 | 0,5 |
| `L10-D01` | Phần thưởng từ so sánh ưu tiên | vấn đề (NT-RL-3, NT13 câu nối trên mặt trang) | "PPO cần phần thưởng $R_{t+1}$ từ môi trường; ở đây chỉ có so sánh." Dữ kiện sáu bộ ba, mỗi loại một dòng; "Câu hỏi:" của mạch | Ví dụ 10.23; topic-25 | 1 |
| `L10-D02` | Mô hình Bradley–Terry | trực quan, định nghĩa, kết quả | "Trực quan." một dòng; $\Pr(y\succ y'\mid x)=\sigma(r(x,y)-r(x,y'))$; $L^{\mathrm{BT}}$; "Kết luận:" cực tiểu $\log\frac k{n-k}$, chỉ hiệu được xác định | Định nghĩa 10.53, Mệnh đề 10.54 | 1,5 |
| `L10-D03` | Ví dụ: khớp mô hình phần thưởng | ví dụ | $d=\log2$, $L^{\mathrm{BT}}$: $0{,}6931\to0{,}6365$, $\hat r=(\log2;\,0)$, kiểm $\sigma(\log2)=\tfrac23$ | Ví dụ 10.24 | 1 |
| `L10-D04` | Mục tiêu có phạt KL | vấn đề, trực quan, định nghĩa | chính sách tham lam $(1;\,0)$ có $J_1=0{,}2877<0{,}4621$ của $\pi_{\mathrm{ref}}$; định nghĩa $J_\beta$ | Ví dụ 10.25, Định nghĩa 10.56; topic-26 | 1 |
| `L10-D05` | Nghiệm của mục tiêu có phạt KL | phát biểu (luận điểm, phần 1) | "Giả thiết:" $\beta>0$, chọn tự do theo $x$; "Kết luận:" $\pi^*_r\propto\pi_{\mathrm{ref}}e^{r/\beta}$, $J_\beta(\pi)=\beta\log\mathcal Z_r-\beta D_{\mathrm{KL}}(\pi\Vert\pi^*_r)$; "Ý nghĩa:" đây là đích chung của PPO trong RLHF và DPO | Định lý 10.57 | 1,5 |
| `L10-D06` | Ý tưởng chứng minh: nghiệm của mục tiêu có phạt KL | ý tưởng chứng minh (NT6) | ba bước; bất đẳng thức then chốt $D_{\mathrm{KL}}\ge0$ (Mệnh đề 10.24) một công thức hiển thị; "(giả thiết $\beta>0$)" ở bước chia cho $\beta$ | Định lý 10.57, chứng minh | 1,5 |
| `L10-D07` | Ví dụ: nghiệm có phạt KL trên bài toán một bước | ví dụ, ứng dụng | $\mathcal Z=\tfrac53$, $\pi^*=(\tfrac45;\,\tfrac15)$, $J_1=0{,}5108$; phần thưởng đã trừ KL $0{,}5108$ ở cả hai câu trả lời; dòng $\beta=\tfrac12$, $\beta=2$ | Ví dụ 10.26 (hình tùy chọn `muc-tieu-phat-kl.svg`) | 1 |
| `L10-D08` | RLHF với PPO | phát biểu thuật toán, kết quả | ba giai đoạn; $R_{t+1}=-\beta\log\frac{\pi_{\mathrm{old}}(A_t\mid S_t)}{\pi_{\mathrm{ref}}(A_t\mid S_t)}+\mathbb 1\{t+1=T\}\hat r$; "Nhắc lại:" Thuật toán 10.49; bốn mô hình | Bổ đề 10.59, Mệnh đề 10.60, Thuật toán 10.61; topic-27 | 1,5 |
| `L10-D09` | Ví dụ: hai vòng PPO, hai mỏ neo | ví dụ tính tay (NT-RL-2) | vòng 1: lợi thế $\tfrac13\log2\,(1;\,1;\,-2)$, dừng ở $p=0{,}8$ do phép cắt; vòng 2: lợi thế $0$; "Diễn giải:" $\pi_{\mathrm{old}}$ giới hạn bước, $\pi_{\mathrm{ref}}$ quyết định điểm dừng | Ví dụ 10.27, Nhận xét 10.58 | 1,5 |
| `L10-D10` | Đổi biến phần thưởng thành chính sách | vấn đề, trực quan, kết quả | "Trực quan."; $r=\beta\log\frac{\pi^*_r}{\pi_{\mathrm{ref}}}+\beta\log\mathcal Z_r$; trong hiệu của Bradley–Terry, $\mathcal Z_r$ triệt tiêu; số A7(6) | Mệnh đề 10.63; topic-28 | 1 |
| `L10-D11` | Hàm mất mát DPO | định nghĩa, kết quả | $r_\theta$, $L^{\mathrm{DPO}}$, gradient với trọng số $\sigma(-\Delta r_\theta)$ | Định nghĩa 10.64, Mệnh đề 10.66 | 1,5 |
| `L10-D12` | Tương đương giữa RLHF và DPO | phát biểu (luận điểm, phần 2) | "Giả thiết:" (H1)–(H4) rút gọn, đủ lượng từ; "Kết luận:" $\arg\min L^{\mathrm{DPO}}=\{\pi^*_{\hat r}\}$, $\min L^{\mathrm{DPO}}=\min L^{\mathrm{BT}}$; một câu kết có điều kiện: cùng nghiệm, không vòng học tăng cường | Định lý 10.65 | 1,5 |
| `L10-D13` | Ví dụ: một bước DPO trên bài toán một bước | ví dụ tính tay (NT-RL-2), trước thuật toán | gradient $(-\tfrac16;\,\tfrac16)$, $\pi_\theta(y_1)=0{,}7362$, $\Delta r_\theta=\tfrac13$; dòng hội tụ $\to(\tfrac45;\,\tfrac15)$, trùng `L10-D07` | Ví dụ 10.28 | 1,5 |
| `L10-D14` | Thuật toán DPO | thuật toán | "Đầu vào:", "Đầu ra:", các bước, điều kiện dừng; hai mô hình, không sinh mẫu | Thuật toán 10.67 | 1 |
| `L10-D15` | So sánh PPO trong RLHF và DPO | bảng so sánh (luận điểm, phần 3) | bảng §7.5, bảy hàng; hình `rlhf-dpo-hai-con-duong.svg` có thể thay hai hàng đầu (QT7) | §7.5; topic-29 | 1,5 |
| `L10-D16` | Giới hạn: ưu tiên tất định | ứng dụng, phản ví dụ | ba so sánh cùng chọn $y_1$ (xác suất $\tfrac8{27}$); DPO: $\pi_\theta(y_1)\to1$ với mọi $\beta$, $J_1\to0{,}2877$; (H4) hỏng | Tình huống 10.5, Nhận xét 10.69 | 1 |
| `L10-D17` | Bài tập: nghiệm có phạt KL trên ba câu trả lời | kiểm tra (đề) | Bài tập 10.13 (a)–(b), "Câu hỏi:" | Bài tập 10.13 | 1 |
| `L10-D18` | Bài tập: nghiệm có phạt KL trên ba câu trả lời | lời giải | "Lời giải:" từng dòng, kết luận ngắn | Bài tập 10.13 | 1 |

Tổng: 19 trang, 22 phút ($0{,}5+1+1{,}5+1+1+1{,}5+1{,}5+1+1{,}5+1{,}5+1+1{,}5+1{,}5+1{,}5+1+1{,}5+1+1+1=22$). Nội dung §7.6 chỉ ở ghi chú diễn giả của `L10-D15`, `L10-D16` (NT5: nói rõ là đọc thêm). Ba trang mang luận điểm của tác giả: `L10-D05` (cùng mục tiêu, nghiệm chung), `L10-D12` (cùng nghiệm mà không cần học tăng cường trực tuyến, có giả thiết), `L10-D15` (khác nhau ở dữ liệu, mô hình, lấy mẫu, mỏ neo).

## C3. Trang đã có phải sửa (giữ mã; chỉ các trang liệt kê)

| Trang | Sửa |
|---|---|
| `L10-101` bìa | luận điểm một câu, có điều kiện (NT11, NT-RL-8), bản nháp: "Đường cơ sở giữ kỳ vọng của gradient; sai số hàm thay thế bị chặn theo khoảng cách chính sách, nên TRPO ràng buộc khoảng cách, PPO cắt tỉ số; với phạt KL theo một chính sách tham chiếu cố định, PPO và DPO giải cùng một bài toán." Tên bài theo QG9; phụ đề thêm "và tối ưu ưu tiên trực tiếp (DPO)" nếu đổi tên |
| `L10-104` mục tiêu | thêm mục tiêu 8, 9 đúng nghĩa ghi chú; trang lên khoảng 9 dòng, vượt trần 80 âm tiết: tách `L10-104b` (QT4) |
| `L10-105` nội dung | tám mục, liên kết `#/1` … `#/8`; mục 7 "Tối ưu chính sách từ phản hồi ưu tiên", mục 8 "Tổng kết" (hoặc giữ tên cũ, QT5) |
| `L10-109` vấn đề trung tâm | hộp "Câu hỏi:" theo bài toán trung tâm của ghi chú sau QG4; ghi chú diễn giả thêm câu trả lời của mạch 7 |
| `L10-110` khung chung | hình `central-problem.svg` đã sửa; câu "Hai hàng gặp nhau ở PPO" thêm một câu cho hàng thứ ba (QG4) |
| `L10-600` ghi chú diễn giả | "Kết quả giao cho phần 7 là thuật toán PPO …": giữ, vì mạch 7 mới dùng Thuật toán 10.49; kiểm lại câu |
| `L10-620` | ghi chú diễn giả thêm một câu nối sang mạch 7 (câu nối trên mặt trang đặt ở `L10-D01`, NT13) |
| `L10-700` | `id="mach-8"`; số "8."; tên (QT5); `p.strand-keys` bỏ "Bài 11" theo QG10; dòng dẫn hiện có dùng khuôn "Muốn …, phải …" (NT12 cấm với deck mới): thay nếu trang được sửa ở lượt này (QT5) |
| `L10-701`, `L10-702`, `L10-702b` | thêm năm hàng của A9: tách `L10-702c` (QT6) |
| `L10-703` | "So sánh sáu phương pháp", thêm hai hàng; nếu vượt 80 âm tiết, tách `L10-703b` (QT6) |
| `L10-704` | thêm hàng DPO (Định lý 10.65) |
| `L10-707` | thêm dòng 6 theo phần 6 của §8.3 |
| `L10-708` | NT15 cho tối đa bốn câu, trang đã có bốn câu: thay câu 3 ("Tỉ lệ cắt bằng $\tfrac33$ …") bằng câu về hai mỏ neo, câu cũ chuyển vào ghi chú diễn giả (QT8) |
| `L10-709` | bảng thêm hàng mạch 7, hàng "8."; số bài tập theo QB1; ghi chú diễn giả dòng 1054 |
| `L10-710` | tài liệu đọc thêm Rafailov và cộng sự (2023, §3–5), Ouyang và cộng sự (2022, §3), Stiennon và cộng sự (2020, §3.4); dòng "Bài 11: SPO …" theo QG10 |
| ghi chú diễn giả có `§7.x` | `L10-701`, `702`, `702b`, `703`, `704`, `707`, `708`, `709`, `710` (dòng 958–1063): "§7.k" thành "§8.k" |

Không trang cũ nào khác đổi. Các phát hiện `deck_lint.py` trên trang cũ chưa sửa là ngoại lệ đã biết (mục 3, 5 của `NGUYEN-TAC-HOC-PHAN.md`); trang mới và trang đã sửa phải sạch.

## C4. Số trang và thời lượng (P6, NT27; chỉ trong planning)

- Số trang: 101 + 19 (mạch 7) + tối đa 3 trang tách (`L10-104b`, `L10-702c`, `L10-703b`) = 120–123. Deck đã có giữ số trang, không bớt trang (mục 3).
- Thời lượng: hiện 120 phút; thêm 22 (mạch 7) và khoảng 1 (bảng tổng kết) thành 143, vượt 120 của P6.
- Giảm được mà không bỏ trang (phút từ `storyboard.md`): trang lời giải bài tập `L10-414`, `L10-510`, `L10-620`, `L10-706` (4 phút) chuyển sang 30 phút chữa bài; trang chứng minh `L10-205`, `L10-404`, `L10-409` từ 4,5 xuống 3; trang chi tiết cài đặt và đọc thêm `L10-614`, `L10-615`, `L10-617`, `L10-617b`, `L10-618` từ 4,5 xuống 2,5; `L10-505` từ 2 xuống 1,5. Tổng giảm 8 phút → 135 phút.
- Đề xuất (QT3): deck 132–135 phút, phần chữa bài còn 15–18 phút; hoặc dạy mạch 7 trong 22 phút của buổi chữa bài. Tác giả chọn.

## C5. Mật độ: rủi ro và ngoại lệ dự kiến (NT17, NT18, NT-RL-7)

| Trang | Rủi ro | Xử lý |
|---|---|---|
| `L10-D05`, `L10-D12` | phát biểu đủ giả thiết vượt 60 âm tiết (bốn giả thiết của Định lý 10.65) | (H1)–(H4) viết gọn bằng công thức; nếu vẫn vượt, ngoại lệ ≤ 90 âm tiết ghi storyboard; không bỏ lượng từ "với mọi $x$, $y$" (NT2) |
| `L10-D08` | ba giai đoạn cộng công thức phần thưởng theo token | tách giai đoạn 1–2 lên dòng ngắn; chi tiết IG C.4 vào ghi chú diễn giả |
| `L10-D15` | bảy hàng × ba cột | trần 80 cho bảng so sánh; hàng "bảo đảm" có thể chuyển vào ghi chú diễn giả |
| `L10-D13` | sáu bước tính | mỗi bước một dòng, gộp trọng số và gradient; bước 2–5 chỉ một dòng kết quả |
| `L10-104b`, `L10-702c` | trang mục tiêu, bảng tổng kết | trần 80 |

Câu trên mặt trang không "chúng ta" (NT18, VP-RL-1); nhãn hợp lệ của NT19 và P3 ("Trực quan.", "Giả thiết:", "Kết luận:", "Ý nghĩa:", "Nhắc lại:", "Đầu vào:", "Đầu ra:", "Câu hỏi:", "Lời giải:", "Diễn giải:"); không "KL:" làm nhãn.

## C6. Hình, kỹ thuật và kiểm tra

- Hình của mạch: `rlhf-dpo-hai-con-duong.svg` (`L10-D15`), tùy chọn `muc-tieu-phat-kl.svg` (`L10-D07`); bản `-slide.svg` khi chữ dưới 16 px ở 390 px (NT25). Không raster.
- Kỹ thuật: CSS cục bộ chỉ theo P7; không `\tag`, không `\text{}` tiếng Việt (NT26); công thức dài như $J_\beta$, $R_{t+1}$ theo token, $\nabla L^{\mathrm{DPO}}$ ngắt bằng `aligned` khi tràn ở 390 px.
- Kiểm theo NT28 và P10 (prompt, giai đoạn III bước 6): `deck_check.py`, `deck_lint.py --course rl-plan`, `footer_check.py`, `formula_overflow.py`; liên kết `#/1` … `#/8` của `L10-105`; liên kết `#/7/1`, `#/8/1` của `exercises.md`; trình xem với `&deck=`.
- Kỹ thuật NT7: "Kỹ thuật." đổi biến (reparameterization) dùng lần đầu ở `L10-D10` nếu tác giả muốn một trang kỹ thuật; đề xuất chỉ một dòng "Kỹ thuật." trên `L10-D06` (mẹo hoàn thành KL) và trên `L10-D10` (đổi biến).

---

# Câu hỏi mở cho điều phối viên và tác giả

Cột "Bảng Q" ghi mã tương ứng trong bảng Q của `prompt-bo-sung-dpo-bai-10.md` (Q1 nguồn, Q2 độ dài, Q3 số mục, Q4 bài tập, Q5 ký hiệu, Q6 chỉ mục và tên bài, Q7 deck, Q8 chuyển tiếp).

| Mã | Bảng Q | Câu hỏi | Đề xuất |
|---|---|---|---|
| QG1 | Q1 | P1 là `deck nguồn + ghi chú`, nhưng `RL-hk2-2025-2026/` không có deck về RLHF, DPO; không giáo trình nào của GC-RL-5 trình bày chủ đề; P8 chỉ cho dẫn bài báo "để kiểm chứng một mệnh đề". | Ngoại lệ "P1, Bài 10, Mục 7 (riêng)" ghi vào mục 3 của `NGUYEN-TAC-HOC-PHAN.md`, theo khuôn "P1, Bài 11 (riêng)": phạm vi, thứ tự theo mục lục giáo trình 13.4–13.6; nội dung theo tám bài báo đã lưu, dẫn số phương trình, mục, định lý; ghi chú là chuẩn duy nhất của mạch 7; mở rộng P8 cho các bài báo đó; không áp quy định "nội dung dựa vào bài báo xếp `bổ sung`". |
| QG2 | Q2 | Ghi chú 29 302 từ; phần bổ sung làm vượt trần 30 000. | Ngoại lệ trần 37 000 từ `prose` cho Bài 10 (GC-RL-4); mục mới 4 000–5 000 từ, các chỗ sửa khác ≤ 2 800 (A12). Phương án gọn: trần 35 000. |
| QG3 | Q3 | Đổi `## 7. Tổng kết và chuyển tiếp` thành `## 8. Tổng kết` (GC-RL-15) ngay trong lượt này? | Có: mục đã phải đổi số; đổi tên cùng lúc với `L10-700` và bảng của `exercises.md` (GC-RL-15 cho phép "cùng đợt sửa deck tương ứng"); chỉ Bài 10. |
| QG4 | — | Bài toán trung tâm của §1.1 (hai nửa) có thêm nửa thứ ba cho Mục 7 không? Hình `central-problem.svg` có thêm hàng không? | Có: thêm một câu vào §1.1, một dòng vào `L10-109`, hàng thứ ba vào hình; nếu không, phần 6 của §8.3 trả lời một câu hỏi không có trong bài toán trung tâm (NT15). |
| QG5 | Q5 | Ký hiệu: $x$, $y$ (đã có nghĩa cục bộ $x_k$, $y_k$, $y_t$), $\mathcal Z$ thay $Z$, $\mathcal D_{\mathrm{pref}}$, $\hat r$ thay $r_\phi$, $r_\theta$ thay $\hat r_\theta$, $\Delta r_\theta$, $\beta$ dùng chung với PPO-Penalty. | Chấp nhận như A5; ghi tương ứng với bài báo một lần sau bảng; $\sigma(x)$ ở Ví dụ 10.2 không đổi (cục bộ, đã có). |
| QG6 | — | Tên mục 7. | "Tối ưu chính sách từ phản hồi ưu tiên" (thuần Việt, theo "phản hồi ưu tiên" của mục lục 13.4); phương án: "Học tăng cường từ phản hồi con người và DPO". |
| QG7 | — | `outline.md` Bài 10 chưa có mục "Phân loại chủ đề" (GC-RL-12). | Thêm mục đó trong lượt này, phân loại cả 30 chủ đề (24 cũ lấy từ bảng ánh xạ chủ đề–trang). |
| QG8 | — | Giả thiết (H4) của Định lý 10.65 do kế hoạch tách ra từ "under mild assumptions" của DPO (tr. 6); phát biểu và chứng minh là của học phần. | Giữ (H4) và chứng minh bốn bước; tác tử rà toán kiểm; ghi trong `review-log.md` rằng phát biểu ghép Định lý 1, Mệnh đề 1 của DPO và nửa đầu Định lý 4.1 của XU. |
| QG9 | Q6 | Tên bài: giữ "TRPO và PPO" hay "TRPO, PPO và DPO"? | Đổi tên hiển thị thành "TRPO, PPO và DPO" (ghi chú, `exercises.md`, deck, thẻ `index.html`); giữ tên tệp `lecture-10-trpo-va-ppo.html` để không vỡ liên kết. Mô tả thẻ chỉ mục thêm "mục tiêu có phạt KL, RLHF với PPO và DPO". |
| QG10 | Q8 | §8.6 (cũ 7.6), "Ứng dụng" sau Tình huống 10.3, `L10-710`, tài liệu tham khảo 17 trỏ nội dung Bài 11 cũ (SPO, SAM+PPO), còn Bài 11 đang dựng lại ở phiên khác. | Bỏ mọi câu trỏ SPO, SAM+PPO và "Bài 11 xử lý …" trong lượt này; §8.6 giữ đoạn giới hạn còn lại (dữ liệu theo chính sách) không trỏ bài sau; câu cầu nối tới Bài 11 mới thêm sau khi Bài 11 mới được commit (GC15: chỉ dẫn tới bài đã có); báo phiên Bài 11. |
| QG11 | Q5 | Thuật ngữ: "lời nhắc" cho prompt; "học tăng cường từ phản hồi con người" (mục lục) hay "… phản hồi của con người" (brief); "hàm phân hoạch" cho partition function; giữ "token". | "lời nhắc (prompt)"; theo mục lục: "học tăng cường từ phản hồi con người"; "hàm phân hoạch"; "token" giữ nguyên; bảng A10 vào `outline.md`. |
| QB1 | Q4 | Số hiệu: BT4 vừa đòi `exercises.md` tiếp số sau ghi chú, vừa cấm đánh lại số đã công bố (`exercises.md` Bài 10 đã lên chỉ mục). | Phương án 1 (đánh lại `exercises.md` thành 10.17–10.22, ghi chú 10.13–10.16) với ngoại lệ BT4 ghi trong `NGUYEN-TAC-HOC-PHAN.md`, nếu tác giả xác nhận chưa giao bài theo số cũ; nếu đã giao, phương án 2 (ghi chú 10.18–10.21, `exercises.md` giữ nguyên, không thêm Bài tập 2.9). |
| QB2 | Q4 | Thêm Sutton và Barto (2018), Bài tập 2.9 (§2.8, tr. 37) vào `exercises.md` cho mục tiêu 8? | Thêm (bài sách duy nhất chạm tới mô hình Bradley–Terry); đề nguyên văn của sách, câu nối với Định nghĩa 10.53 chỉ trong lời giải. |
| QB3 | Q4 | Bốn bài mới đều ở "Mức vận dụng" để giữ số tăng theo thứ tự đọc; không có bài nhận biết mới trong ghi chú. | Chấp nhận; phần nhận biết do Bài tập 2.9 của sách và câu hỏi tự kiểm tra mới ở §8.4 đảm nhận. Nếu tác giả muốn một bài nhận biết trong ghi chú, cần đánh lại cả 10.4–10.12 (deck dẫn nhiều số này): không đề xuất. |
| QB4 | Q4 | Bài tập 10.16 (bán kính cắt $0{,}1$) dựa vào cách cực đại hóa "tới biên đầu tiên của đoạn phẳng"; có giữ không? | Giữ, đề nêu rõ cách cực đại hóa; nếu bỏ, mục tiêu 8 vẫn có Bài tập 10.13 và Bài tập 2.9 của sách. |
| QT1 | Q7 | Tám mạch, vượt khoảng 5–7 của NT10 và `AGENTS.md`. | Chấp nhận theo yêu cầu cụ thể của tác giả; ghi lý do và ảnh hưởng trong `storyboard.md` và `review-log.md`. Phương án gộp DPO vào mạch 6 làm mạch 6 lên 42 trang và tách mục khỏi mạch (GC16): không đề xuất. |
| QT2 | Q7 | Mã trang của mạch mới. | `L10-D00` … `L10-D18`, `id="mach-7"`; "Tổng kết" giữ `L10-700` … `L10-710`, đổi `id="mach-8"`; trang tách mới `L10-104b`, `L10-702c`, `L10-703b` theo khuôn hậu tố chữ đã có; liên kết `exercises.md` `#/7/1` (mạch mới), `#/8/1` (Tổng kết). |
| QT3 | Q7 | Thời lượng 143 phút so với 120 của P6. | Giảm 8 phút ở các trang lời giải, chứng minh, chi tiết cài đặt (C4), deck 135 phút, chữa bài 15 phút; hoặc dạy mạch 7 trong thời gian chữa bài. Tác giả chọn. |
| QT4 | Q7 | Trang mục tiêu với chín mục tiêu vượt trần. | Tách `L10-104b` (mục tiêu 6–9). |
| QT5 | Q7 | Tên và dòng dẫn của `L10-700` ("Muốn dùng đúng …, phải …", khuôn bị NT12 cấm với deck mới). | Đổi tên thành "Tổng kết" (QG3) và viết lại dòng dẫn trong lượt này, vì trang đã phải sửa số và từ khóa. |
| QT6 | Q7 | Bảng tổng kết thêm năm hàng và bảng phương pháp thêm hai hàng. | Tách `L10-702c` (năm hàng của Mục 7); `L10-703b` chỉ khi `L10-703` vượt 80 âm tiết. |
| QT7 | Q7 | `L10-D15` dùng bảng hay hình `rlhf-dpo-hai-con-duong.svg`? | Bảng trên mặt trang (bảng so sánh có trần 80), hình ở ghi chú §7.5; nếu bảng vượt trần, hình thay hai hàng "dữ liệu" và "mô hình". |
| QT8 | Q7 | `L10-708` đã có bốn câu (trần của NT15). | Thay câu 3 bằng câu về hai mỏ neo; câu cũ chuyển vào ghi chú diễn giả. |

# Nguồn đã lưu (2026-11-19)

Mỗi thư mục có `original.pdf`, `extracted.md` (`pdftotext -layout`, ký tự trang giữ nguyên), `manifest.json` (trường như `auer-ucb1-2002-20261119/manifest.json`; trạng thái `extracted_needs_content_review`).

| Thư mục trong `/data/tqlong/qa/sources/` | Bài | Bản |
|---|---|---|
| `rafailov-dpo-2023-20261119` | Rafailov và cộng sự (2023), DPO | arXiv 2305.18290v3, 27 trang |
| `ouyang-instructgpt-2022-20261119` | Ouyang và cộng sự (2022), InstructGPT | arXiv 2203.02155v1, 68 trang |
| `stiennon-summarize-feedback-2020-20261119` | Stiennon và cộng sự (2020) | arXiv 2009.01325v3, 45 trang (pdftotext báo một lỗi xref đã tự dựng lại) |
| `ziegler-finetuning-preferences-2019-20261119` | Ziegler và cộng sự (2019) | arXiv 1909.08593v2, 26 trang |
| `christiano-deep-rl-preferences-2017-20261119` | Christiano và cộng sự (2017) | arXiv 1706.03741v4, 17 trang |
| `azar-ipo-2024-20261119` | Gheshlaghi Azar và cộng sự (2024), IPO | arXiv 2310.12036v2, 13 trang |
| `xu-dpo-vs-ppo-2024-20261119` | Xu và cộng sự (2024) | arXiv 2404.10719v3, 16 trang |
| `rafailov-r-to-q-2024-20261119` | Rafailov, Hejna, Park, Finn (2024) | arXiv 2404.12358v2, 32 trang |

Chưa kiểm: số liệu trong Phụ lục, Bảng 3 của DPO; nơi công bố của IG, CH, IPO, XU; nội dung các hình (cần xem trực quan, `visual_review_required: true`).

# Kiểm lại các dữ kiện của brief

1. **Đúng:** 29 302 từ `prose`; không deck nguồn, không giáo trình của GC-RL-5 về chủ đề; mục lục 13.4–13.6 đúng như brief (trang PDF 13, trang in xi); deck có 101 trang, mã `L10-101` … `L10-710`, đã có `id="mach-2"` … `id="mach-7"`; số khối cuối Nhận xét 10.51, Ví dụ 10.22, Tình huống 10.3, chủ đề `lec-10-topic-24`; mọi số của ví dụ xuyên suốt ở điểm 7 của brief (tính lại ở A7).
2. **Sai: KL khi ưu tiên tất định.** Brief ghi "KL to $\pi_{\mathrm{ref}}$ unbounded" khi $q=1$. Theo chiều của mục tiêu, $D_{\mathrm{KL}}(\pi_\theta\Vert\pi_{\mathrm{ref}})\to\log\tfrac32=0{,}405465$ (bị chặn); đại lượng không bị chặn là phần thưởng ngầm định $r_\theta(y_2)\to-\infty$ và KL chiều ngược $D_{\mathrm{KL}}(\pi_{\mathrm{ref}}\Vert\pi_\theta)$. Hậu quả đúng là nghiệm trở thành tất định với mọi $\beta$ (IPO §4.2, tr. 4), và $J_1$ theo phần thưởng thật giảm từ $0{,}5108$ về $0{,}2877$.
3. **Cần chỉnh: deck dẫn số bài tập.** Deck không dẫn "Bài tập 10.13", "Bài tập 10.14" mỗi số một lần trên trang nội dung; các số của `exercises.md` nằm ở bảng `L10-709` (10.13, 10.14 hai lần, 10.15, 10.16, 10.17) và ghi chú diễn giả của `L10-709` ("10.13–10.17", "(10.13)", "Bài tập 10.14").
4. **Cần chỉnh: ký hiệu.** $x$, $y$ đã có nghĩa cục bộ ($x_k$, $y_k$, $\langle x,y\rangle_F$ ở Thuật toán 10.36, $y_t=V^{\mathrm{targ}}_t$ ở Mục 6.3, $\sigma(x)$ ở Ví dụ 10.2); $q$, $q'$ là phân phối của Định nghĩa 10.23 và $u=(1;\,-1)$ là vector cục bộ ở Mục 5.1, nên tỉ lệ ưu tiên $q$ và hiệu logit $u$ của brief đổi (A5). $\sigma$ đã là hàm logistic cục bộ với cùng nghĩa.
5. **Cần chỉnh: nguồn của phạt KL theo token.** ST §3.4 (tr. 6, công thức không đánh số) và ZI (2) (tr. 3) viết phạt KL cho cả câu trả lời; cụm "per-token KL penalty … at each token" nằm ở IG §3.5 (tr. 9). Hai cách viết bằng nhau theo kỳ vọng (Bổ đề 10.59).
6. **Bổ sung cho BT-RL-1:** Sutton và Barto (2018) có Bài tập 2.9 (§2.8, tr. 37) chạm tới mô hình Bradley–Terry hai câu trả lời; brief ghi "none has DPO exercises", đúng với DPO nhưng có một bài dùng được cho mục tiêu 8 (QB2).
7. **Bổ sung: mâu thuẫn trong BT4** khi thêm bài tập vào bài đã công bố (QB1); và NT10 bị vượt khi thêm mạch thứ tám (QT1).
