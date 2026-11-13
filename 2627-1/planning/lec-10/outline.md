# Dàn ý Bài 10: TRPO và PPO

## Phạm vi (Giai đoạn II, viết lại 2026-11-04)

- Nguồn chính của bộ trang chiếu: ghi chú bài giảng đã duyệt `materials/lec-10/lecture-note.md` (commit `1c9ef05`; commit `567c96c` chỉ bỏ mục "Bản đồ chủ đề" theo yêu cầu người dùng, ghi chú ngắn đi 63 dòng, số hiệu khối và mốc `note-topic-id` không đổi). Bộ trang chiếu tóm tắt ghi chú: cùng thuật ngữ, ký hiệu, giả thiết, ví dụ, số hiệu kết quả và thứ tự khái niệm, trừ các sai khác ghi ở mục "Sai khác có chủ ý".
- Nguồn bài giảng gốc: `RL-hk2-2025-2026/lecture10_policy_gradient_part2.pdf`, 43 trang (trang bìa ghi "Lecture 10: Overview on Policy Gradient Algorithms, Part 1"). Phần I (tr. 3–42) thuộc bài này; Phần II (A3C, DDPG, SAC, …) thuộc Bài 11 và chỉ xuất hiện trong một dòng nối ở trang cuối.
- Kế hoạch đã duyệt: kế hoạch bộ trang chiếu của điều phối viên (7 mạch, 101 trang), áp dụng phương án nén 11 cặp trang thành 90 trang; cổng storyboard (2026-11-04, hai lần) tách lại năm trang (`L10-110`, `L10-412`, `L10-510`, `L10-608`, `L10-710`), còn 95 trang; bản viết tách `L10-212b`, `L10-702b`, và đợt sửa D1 (sau năm báo cáo rà soát, 2026-11-04) tách `L10-412b`, `L10-502b`, `L10-611b`, `L10-617b`: **101 trang**, giữ phút từng mạch $12+23+14{,}5+22{,}5+13{,}5+25{,}5+9=120$. Ghi chú bài giảng dùng làm nguồn ở D1 là bản sau commit `9a5478a` (sửa ví dụ miền tin cậy sau Hệ quả 10.31 và Ví dụ 10.4). Mã trang đánh số liên tiếp; bảng đối chiếu mã kế hoạch → mã mới ở cuối `storyboard.md`.
- Bản cũ: bộ trang chiếu `lecture-10-trpo-va-ppo.html` (42 trang, mã `L10-01`…`L10-38`, `L10-37B`, `X01`–`X03`, ký hiệu $w_t$) và các tệp `outline.md`, `storyboard.md` cũ (còn trong git) viết trước chuẩn hiện hành; chỉ dùng để ghi quyết định so với bản cũ. `note-for-author.md` thuộc vòng soạn cũ, các cảnh báo của nó đã được ghi chú bài giảng mới xử lý; tệp này không phải đầu vào của vòng này.
- Bài tập: chưa có `materials/lec-10/exercises.md`. Trang "Bài tập về nhà và tài liệu đọc" ánh xạ Bài tập củng cố 10.1–10.12 của ghi chú theo mạch và liên kết viewer của ghi chú bài giảng. Cập nhật 2026-11-13: `exercises.md` có Bài tập 10.13–10.17 (làm lại 2026-11-12); `L10-709` chép bảng mạch của tệp đó (bảy hàng, tách cột tệp bài tập và cột ghi chú).
- Thời lượng: 120 phút trình chiếu; 30 phút còn lại chữa bài (lời giải đầy đủ của bài tập trên trang và bài về nhà).

## Khung lý thuyết chung

**Bài toán trung tâm** (ghi chú §1.1). Giảm phương sai của ước lượng gradient chính sách mà vẫn giữ kỳ vọng của nó, và dùng lại dữ liệu của $\pi_{\mathrm{old}}$ để chọn một bước cập nhật lớn mà chính sách mới không kém chính sách cũ. Hai nửa ứng với hai hàng của hình `img/lec-10/central-problem.svg`: hàng trên (mạch 2–3) chọn hệ số nhân với hàm điểm, hàng dưới (mạch 4–6) giới hạn độ lớn bước; hai hàng gặp nhau ở Thuật toán 10.49 (PPO kiểu actor–critic).

**Đối tượng và ký hiệu chung** (bảng ký hiệu của ghi chú).

- MDP hữu hạn; $\mathcal S$ là tập trạng thái chưa kết thúc, $\mathcal A$ hữu hạn với $m$ hành động; $R_{t+1}$ nhận sau $A_t$; lượt kết thúc tại $T$, sau đó là trạng thái hấp thụ với $G_T=0$ và $v_\pi=q_\pi=A_\pi=0$; $\gamma\in[0,1)$ trong các định lý. Hành lang ngắn có $\gamma=1$, nằm ngoài giả thiết và chỉ dùng ở mạch 1–2.
- $\mu_0$ (Bài 09 viết $\rho_0$), $P(s'\mid s,a)$, $P_\pi$, $\Gamma_\pi=(I-\gamma P_\pi)^{-1}$.
- $\pi_\theta$, $\theta\in\mathbb R^d$; $\theta_{\mathrm{old}}$, $\pi_{\mathrm{old}}$ là tham số và chính sách sinh dữ liệu; $\psi_\theta=\nabla_\theta\log\pi_\theta$, $\psi_t$ ($=0$ khi $t\ge T$); $H_t$ lịch sử.
- $v_\pi$, $q_\pi$, $A_\pi=q_\pi-v_\pi$, $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$. Chữ $A$ hai vai: $A_t$ (chỉ số thời gian) là hành động; $A_\pi$, $\widehat A_t$ là lợi thế.
- $b(s)$ đường cơ sở; $\hat v(s,w)$ critic, $w_{\mathrm{old}}$, $\hat v_{\mathrm{old}}$; $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\hat v(S_{t+1},w)-\hat v(S_t,w)$; cờ $Z_{t+1}$ (kết thúc của MDP), $U_{t+1}$ (cắt ngắn).
- $G_{t:t+n}$, $\widehat A^{(n)}_t$, $G^\lambda_t$, $\widehat A_t$ (GAE); từ mạch 6: $\widehat A^{\mathrm{raw}}_t$ (trước chuẩn hóa), $V^{\mathrm{targ}}_t=\widehat A^{\mathrm{raw}}_t+\hat v_{\mathrm{old}}(S_t)$.
- $\nu^\pi(s)=(1-\gamma)\sum_t\gamma^t\Pr_\pi(S_t=s,\,t<T)$ trên $\mathcal S$, khối $\le1$.
- $\rho_\theta(s,a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$, $\rho_t(\theta)$; $\mathcal L_{\theta_{\mathrm{old}}}$, $\mathcal L^{\mathrm{CPI}}$, $\mathcal L^{\mathrm{CLIP}}$, $\ell^{\mathrm{CLIP}}_t$ (cực đại hóa); $L(\theta,w)$, $L^V$ (cực tiểu hóa).
- $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$ (theo $\nu^{\mathrm{old}}$), $\widehat D$ (trung bình trên bộ đệm), $\mathcal H$; $\kappa$, $\kappa_{\mathrm{targ}}$; $\chi_{\pi'}$, $\bar\chi$; $F$, $g$, $\Delta$; $\epsilon$, $\beta$, $c_1$, $c_2$; $N$, $h$, $K$, $M$; $\mathcal D$, $\mathcal B$.
- Quy ước: $\log$ tự nhiên; dấu phẩy thập phân, tọa độ ngăn bằng dấu chấm phẩy $(0{,}2;\,0{,}3)$; kỳ vọng $\mathbb E_{S\sim\nu^\pi}$ (có chiết khấu) khác trung bình đều $\widehat{\mathbb E}_{\mathcal D}$ trên bộ đệm.

**Ví dụ xuyên suốt.**

- *Bài toán một bước* (thẻ `img/lec-09/one-step-card.svg`): $\pi_\theta(\cdot\mid s)=(\tfrac23;\,\tfrac13)$, $\theta=(\log2;\,0)$, $r=(3;\,0)$, $\nabla J=(\tfrac23;\,-\tfrac23)$, $v_\pi(s)=2$, $A_\pi(s,\cdot)=(1;\,-2)$. Dùng ở mạch 1, 2, 5, 6.
- *Chuỗi hai trạng thái* (`img/lec-10/two-state-chain.svg`): $\gamma=0{,}9$, $p_A=\tfrac12$, $p_B=\tfrac23$, $v_\pi=(1{,}4;\,2)$, $\nabla J=(0{,}2;\,0{,}3)$, $\nu^\pi=(0{,}1;\,0{,}045)$. Dùng ở mạch 2, 3, 4.
- *Hành lang ngắn* (`img/lec-09/short-corridor.svg`): $\gamma=1$, $p=\tfrac12$, $J=-12$, $\nabla J=(2;\,-2)$; chỉ ở mạch 1–2.

**Giả thiết chung.** (G1) $\mu_0$, $P$ không phụ thuộc $\theta$, trạng thái Markov; (G2) $\pi_\theta$ khả vi, miền hỗ trợ không đổi; (G3) $\lvert R\rvert\le R_{\max}$, $T\le T_{\max}$; (G4) softmax hoặc Gaussian phương sai cố định, đặc trưng bị chặn. Mạch 4–5 thêm: MDP hữu hạn, cùng $P$ và $\mu_0$, $\gamma<1$, chính sách Markov dừng, điều kiện hỗ trợ $\pi'>0\Rightarrow\pi>0$, lợi thế và phân bố chiếm dụng chính xác. Mọi kết quả dùng dữ liệu theo chính sách.

**Chuỗi định nghĩa → kết quả → phương pháp.** Hai giới hạn của REINFORCE (Ví dụ 10.1, 10.2) → đường cơ sở (Định nghĩa 10.1) → không làm chệch (Mệnh đề 10.2), đường cơ sở tối ưu (Mệnh đề 10.3) → hàm lợi thế (Định nghĩa 10.4) → gradient dạng lợi thế (Mệnh đề 10.5) → REINFORCE có đường cơ sở (Thuật toán 10.6) → critic, actor–critic (Định nghĩa 10.7) → $\mathbb E[\delta_t\mid s,a]=A_\pi$ khi critic đúng (Mệnh đề 10.8) → actor–critic một bước (Thuật toán 10.9) → lợi tức $n$ bước (Định nghĩa 10.11, Bổ đề 10.12) → lợi tức λ, GAE (Định nghĩa 10.13) → dạng tổng, truy hồi (Mệnh đề 10.14) → γ-just (Mệnh đề 10.15) → GAE trên đoạn thu (Thuật toán 10.16) → phân bố chiếm dụng (Định nghĩa 10.18) → hiệu hiệu năng (Bổ đề 10.19, Hệ quả 10.20) → hàm thay thế (Định nghĩa 10.21), khớp bậc một (Mệnh đề 10.22) → TV, KL, Pinsker (Định nghĩa 10.23, Mệnh đề 10.24) → chặn cải thiện (Định lý 10.26, Hệ quả 10.27; Bổ đề 10.25 trong chứng minh) → cải thiện đơn điệu (Hệ quả 10.29) → bài toán miền tin cậy (Định nghĩa 10.30, Hệ quả 10.31) → Fisher, KL bậc hai (Định nghĩa 10.32, Mệnh đề 10.33) → gradient tự nhiên (Mệnh đề 10.34) → gradient liên hợp, TRPO (Thuật toán 10.36, 10.37, Nhận xét 10.38) → PPO-Clip (Định nghĩa 10.39, Mệnh đề 10.40, 10.41, Nhận xét 10.42) → PPO-Penalty (Định nghĩa 10.43) → entropy, mất mát tổng, chẩn đoán (Định nghĩa 10.45–10.47, Mệnh đề 10.48) → PPO (Thuật toán 10.49) → chi tiết cài đặt (Nhận xét 10.50) → hội tụ về điểm dừng (Nhận xét 10.51, đọc thêm).

**Giới hạn áp dụng** (ghi chú §7.1–7.3, "Giả thiết hay bị bỏ quên").

- Đường cơ sở không được phụ thuộc hành động đã chọn khi biết $H_t$.
- Critic sai làm chệch actor–critic (Mệnh đề 10.8(b)).
- GAE γ-just chỉ khi $\lambda=1$ với lượt đầy đủ hoặc $\hat v=v_\pi$; γ-just không có nghĩa không chệch cho lợi thế.
- Mọi bảo đảm của mạch 4 cần lợi thế, $\nu^\pi$ và phép tối ưu chính xác, nên không áp dụng cho TRPO, PPO thực hành; TRPO thực hành chỉ bảo đảm KL trung bình mẫu $\le\kappa$ và hàm thay thế mẫu tăng.
- Mục tiêu cắt không chặn KL; approxKL không chệch chỉ khi $\theta$ không phụ thuộc các mẫu.
- Kết quả hội tụ của PPO-Clip chỉ nói về điểm dừng trong một mô hình đơn giản hóa.
- Dữ liệu phải theo chính sách; Bài 11 bỏ giới hạn này.

**Trang bìa.** Tiêu đề `h1` "TRPO và PPO" (trùng tên ghi chú và `index.html`); dòng `h2` "Tối ưu chính sách miền tin cậy (TRPO) và tối ưu chính sách gần kề (PPO)" là dòng tiêu đề, không đếm âm tiết (quyết định của điều phối viên), để hai chữ viết tắt có tên đầy đủ ở lần đầu. Luận đề một câu, 30 âm tiết, không tên tiếng Anh: "Đường cơ sở giữ kỳ vọng của gradient; sai số hàm thay thế bị chặn theo khoảng cách chính sách, nên TRPO ràng buộc khoảng cách, PPO cắt tỉ số." Mặt bìa 49 âm tiết. Câu không dùng đề xuất "critic và GAE đổi phương sai lấy độ chệch" của kế hoạch, vì ghi chú chỉ nêu đánh đổi đó ở mức định tính và cấm khẳng định critic hay GAE luôn giảm phương sai; điều kiện "critic chỉ giữ kỳ vọng khi critic đúng" nằm trong ghi chú diễn giả của bìa và ở `L10-109`.

**Quy ước tên tiếng Anh.** Tên tiếng Anh và tên đầy đủ của chữ viết tắt ghi trong ngoặc ở lần đầu thuật ngữ xuất hiện trong một câu trên mặt trang, trừ bìa: luận đề không có tên tiếng Anh, và tên tiếng Anh của các thuật ngữ trong luận đề (đường cơ sở, hàm thay thế, tỉ số chính sách) ghi ở trang mục tiêu `L10-104`. Trang "Nội dung" và trang tiêu đề mạch giữ đúng tên mạch nên không chèn tên tiếng Anh; ký hiệu chưa được nêu ($\delta_t$, $\nu^\pi$, $\kappa$, $\rho_t$) không xuất hiện trước trang định nghĩa hoặc nhắc lại của nó.

## Mục tiêu học tập (trang `L10-104`)

Sáu dòng (sửa 2026-11-13 theo bảng phát hiện, trước đó năm dòng), mỗi dòng một sản phẩm kiểm được; ghi chú diễn giả nêu sản phẩm. Ánh xạ với bảy mục tiêu của ghi chú: dòng 1 ↔ mục tiêu 1–2; dòng 2 ↔ 3; dòng 3 ↔ 4 và nửa đầu của 5; dòng 4 ↔ nửa sau của 5; dòng 5 ↔ 6–7 (phần tính); dòng 6 ↔ 6–7 (phần chứng minh). Các sản phẩm của mục tiêu 2 (độ chệch của sai số TD khi critic sai), 6 (quy tắc PPO-Penalty) và 7 (một vòng PPO, phạm vi kết quả hội tụ của PPO-Clip) nêu trong ghi chú diễn giả, vì trang đã ở trần 80.

1. (Mạch 2) "Chứng minh đường cơ sở (baseline) không làm chệch; tính hai bước actor–critic." Sản phẩm: $\operatorname{Var}(X_b)=\tfrac49(b-1)^2$; $p_A$ từ $0{,}5$ lên $0{,}5436$; trong ghi chú diễn giả: $\mathbb E[\delta_0\mid s_A,1]=0{,}35\ne0{,}4$ khi critic sai.
2. (Mạch 3) "Tính ước lượng lợi thế tổng quát (GAE) trên đoạn thu (rollout) có cắt ngắn." Sản phẩm: $\widehat A_0=0{,}98$ và $3{,}572$.
3. (Mạch 4) "Chứng minh bổ đề hiệu hiệu năng (performance difference lemma); tính hàm thay thế (surrogate objective), chặn cải thiện." Sản phẩm: $\Delta J=0{,}296$, $\mathcal L-J=0{,}26$, cận chặn cải thiện $-0{,}892$. Tên tiếng Anh của chặn cải thiện ghi ở `L10-408`.
4. (Mạch 5) "Tính bước gradient tự nhiên (natural gradient), gradient liên hợp (conjugate gradient)." Sản phẩm: $\Delta^*=(0{,}15;\,-0{,}15)$; $\Delta=(0{,}05;\,0{,}1)$.
5. (Mạch 6) "Tính mục tiêu cắt (clipped objective), approxKL, tỉ lệ cắt (clip fraction)." Sản phẩm: $\mathcal L^{\mathrm{CLIP}}=0{,}2167$, approxKL $0{,}01737$, tỉ lệ cắt $\tfrac13$; quy tắc PPO-Penalty cho $\beta=2$ (ghi chú diễn giả).
6. (Mạch 6) "Chứng minh chặn dưới bi quan; approxKL không chệch." Sản phẩm: $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$, trùng quanh $\theta_{\mathrm{old}}$ (Mệnh đề 10.41); $\mathbb E[(\rho-1)-\log\rho]=D_{\mathrm{KL}}$ khi $\theta$ không phụ thuộc mẫu (Mệnh đề 10.48).

Tổng 80 âm tiết theo `deck_check` (trần 80 của trang mục tiêu), 6 dòng, dòng dài nhất 19 âm tiết. Tên tiếng Anh "probability ratio" chuyển sang định nghĩa ở `L10-405`.

## Bảy mạch

HTML có đúng 7 section ngoài. Mạch $N$ mở tại `#/N`; từ mạch 2, trang đầu là trang tiêu đề mạch `L10-N00`, `id="mach-N"`. Số mạch $N$ trùng số mục $N$ của ghi chú với $N=2,\dots,7$; Mục 1 của ghi chú (một chủ đề, `lec-10-topic-02`) cùng phần tiên quyết vào mạch mở đầu, vì tách riêng sẽ thành 8 mạch, vượt khoảng 5–7.

| mạch | tên (trang tiêu đề mạch) | chức năng | đầu vào | đầu ra | đóng góp cho bài toán trung tâm | dòng dẫn (âm tiết) | từ khóa | phút |
|---|---|---|---|---|---|---|---|---:|
| 1 | Mở đầu và hai giới hạn của REINFORCE (bìa là trang tiêu đề) | Ký hiệu, nhắc lại Bài 03–09, mục tiêu, nội dung; đo phương sai và tác hại của bước lớn; phát biểu bài toán | REINFORCE, (G1)–(G4), hàm điểm (Bài 09) | Hai nhu cầu: giảm phương sai giữ kỳ vọng; bước lớn bằng dữ liệu cũ | Phát biểu bài toán và khung hai hàng | — | — | 12 |
| 2 | Đường cơ sở, hàm lợi thế và actor–critic (`L10-200`) | Trừ đường cơ sở, đặt tên lợi thế, bootstrap bằng critic | $\operatorname{Var}$ tăng $\tfrac49\to\tfrac{16}9$ khi cộng $1$ vào phần thưởng | $\widehat g_b$ không chệch; $\nabla J$ dạng lợi thế; $\delta_t$ ước lượng lợi thế khi critic đúng; Thuật toán 10.6, 10.9 | Nửa thứ nhất, hai đầu Monte Carlo và một bước | "Muốn giảm phương sai mà giữ kỳ vọng của gradient, phải trừ khỏi lợi tức một mức không phụ thuộc hành động đã chọn." (24) | Đường cơ sở · Hàm lợi thế · Critic · Sai số sai phân thời gian · Actor–critic một bước (2026-11-13: tên đầy đủ thay "Sai số TD", vì viết tắt chỉ có tên đầy đủ từ `L10-212b`) | 23 |
| 3 | Ước lượng lợi thế tổng quát (`L10-300`) | Nối $\delta_t$ và $G_t-\hat v$ bằng $\lambda$; điều kiện γ-just; tính trên đoạn thu có cờ | Hai ước lượng $0{,}35$ và $1{,}7$ của cùng $A_\pi(s_A,1)=0{,}4$ | $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$, truy hồi lùi với $Z$, $U$, $V^{\mathrm{targ}}$ (Thuật toán 10.16) | Hoàn tất nửa thứ nhất; giao lợi thế cho mạch 6 | "Muốn chọn mức trung gian giữa sai số TD và lợi tức Monte Carlo, phải trộn các lợi tức nhiều bước bằng một tham số." (25, D1) | Lợi tức n bước · Lợi tức λ · GAE · Tính không chệch cho gradient · Đoạn thu | 14,5 |
| 4 | Hàm thay thế và chặn cải thiện (`L10-400`) | Hiệu hiệu năng, hàm thay thế, TV và KL, chặn cải thiện, miền tin cậy | Giới hạn thứ hai: dữ liệu cũ sau một bước | Bài toán miền tin cậy (Định nghĩa 10.30), mức giảm bị chặn khi giải chính xác (Hệ quả 10.31) | Căn cứ định lượng cho việc giới hạn bước | "Muốn dùng dữ liệu cũ cho một bước lớn, phải chặn sai số khi đánh giá chính sách mới bằng dữ liệu đó." (23) | Hiệu hiệu năng · Hàm thay thế · Phân kỳ KL · Chặn cải thiện · Miền tin cậy | 22,5 |
| 5 | TRPO và gradient tự nhiên (`L10-500`) | KL bậc hai, gradient tự nhiên, gradient liên hợp, tìm kiếm lùi | Bài toán miền tin cậy phi tuyến | Thuật toán 10.37; điều TRPO bảo đảm trên bộ đệm (Nhận xét 10.38) | Giải xấp xỉ bài toán của mạch 4 | "Muốn giải bài toán miền tin cậy với nhiều tham số, phải xấp xỉ KL bậc hai và tránh lập ma trận Fisher." (23) | Ma trận Fisher · Gradient tự nhiên · Gradient liên hợp · Tìm kiếm lùi | 13,5 |
| 6 | Tối ưu chính sách gần kề (PPO) (`L10-600`) | Mục tiêu cắt, PPO-Penalty, mất mát tổng, chẩn đoán, thuật toán, cài đặt, phạm vi lý thuyết | Chi phí bậc hai của TRPO; hàm thay thế mẫu tuyến tính theo $\rho_t$ | Thuật toán 10.49 với GAE và mục tiêu cắt; điều không được bảo đảm | Hai hàng gặp nhau | "Muốn giữ chính sách mới gần chính sách cũ bằng tối ưu bậc một, phải đưa giới hạn khoảng cách vào hàm mục tiêu." (24) | Mục tiêu cắt · PPO-Penalty · Hàm mất mát tổng · Đại lượng chẩn đoán · Chi tiết cài đặt | 25,5 |
| 7 | Tổng kết và chuyển tiếp (`L10-700`) | Bảng kết quả–giả thiết, bảng phương pháp, bảng kết luận có bảo đảm, bài tổng hợp, trả lời bài toán, câu hỏi, bài về nhà, nối Bài 11 | Kết quả mạch 2–6 | Câu trả lời có điều kiện; giới hạn dữ liệu theo chính sách chuyển sang Bài 11 | Tổng hợp, không khái niệm mới | "Muốn dùng đúng các phương pháp của bài, phải giữ giả thiết của từng kết quả." (16) | Kết quả và giả thiết · Bốn phương pháp · Vấn đề trung tâm · Bài 11 (D1: thống nhất tên với `L10-109`, `L10-707`) | 9 |

Âm tiết đếm bằng số từ tách theo khoảng trắng, không tính KaTeX (công cụ đếm trong thư mục tạm của phiên). Tên mạch khác tiêu đề trang nội dung đầu mạch: `L10-201` "Mức so sánh của trạng thái", `L10-301` "Ví dụ: ba ước lượng lợi thế trên một lượt", `L10-401` "Dữ liệu cũ và chính sách mới", `L10-501` "Ví dụ: cùng một bước tham số, hai khoảng cách chính sách", `L10-601` "Giới hạn của TRPO", `L10-701` "Kết quả và giả thiết của bài".

Trang "Nội dung" (`L10-105`) liệt kê bảy tên theo cột "tên", mục 1 là "Mở đầu và hai giới hạn của REINFORCE".

## Bảng thuật ngữ Việt–Anh

Kế thừa bảng của Bài 09 (`planning/lec-09/outline.md`). Lần đầu xuất hiện trên mặt trang, viết tên tiếng Việt kèm tên tiếng Anh trong ngoặc; các lần sau chỉ dùng tên tiếng Việt. Cột "lần đầu" là trang dự kiến.

| Tiếng Việt | Tiếng Anh | Quy ước | lần đầu |
|---|---|---|---|
| đường cơ sở | baseline | $b(s)$; không để "baseline" trần | `L10-104` |
| hàm lợi thế, lợi thế | advantage function, advantage | $A_\pi$; ước lượng $\widehat A_t$ | `L10-102` ("lợi thế (advantage)"); `L10-207` ("hàm lợi thế (advantage function)") |
| critic; actor; phương pháp actor–critic | critic; actor; actor–critic method | tên giữ nguyên; định nghĩa theo Định nghĩa 10.7 (critic bootstrap từ $S_{t+1}$) | `L10-104`; định nghĩa ở `L10-212` |
| quá trình quyết định Markov (MDP) | Markov decision process | viết tắt sau lần đầu | `L10-103` (dòng (G1), 2026-11-13); `L10-102` chỉ còn tên cờ |
| sai số sai phân thời gian (sai số TD) | temporal-difference error | $\delta_t$ có mặt nạ $(1-Z_{t+1})$; $\delta$ không dùng cho nghĩa khác | `L10-212b` ("Nhắc lại:", tên đầy đủ kèm viết tắt, 2026-11-13); `L10-200` (từ khóa, tên đầy đủ) |
| cập nhật bán gradient | semi-gradient | | `L10-212` (ghi chú diễn giả) |
| lợi tức; lợi tức $n$ bước; lợi tức λ | return; n-step return; λ-return | $G_t$, $G_{t:t+n}$, $G^\lambda_t$ | `L10-103`; `L10-302`; `L10-303` |
| lợi tức λ cắt | truncated λ-return | chỉ trong ghi chú diễn giả | `L10-307` |
| ước lượng lợi thế tổng quát (GAE) | generalized advantage estimation | $\widehat A_t$, tham số $\lambda$ | `L10-104` |
| γ-just (không chệch cho gradient) | γ-just | thuật ngữ của Schulman và cộng sự (2016) | `L10-306` |
| đoạn thu | rollout | độ dài $h$ (bài báo PPO và nguồn tr. 24 viết $T$) | `L10-104` |
| kết thúc; cắt ngắn | termination; truncation | cờ $Z$; cờ $U$ | `L10-102` |
| bộ đệm | buffer | $\mathcal D$, $hN$ mẫu | `L10-507` |
| phân bố chiếm dụng (chiết khấu) | discounted occupancy distribution | $\nu^\pi$, chuẩn hóa trên $\mathcal S$, khối $\le1$ | `L10-403` |
| bổ đề hiệu hiệu năng | performance difference lemma | | `L10-104` |
| hàm thay thế | surrogate objective | $\mathcal L_{\theta_{\mathrm{old}}}$; không để "surrogate" trần | `L10-104` |
| tỉ số chính sách | probability ratio | $\rho_t(\theta)$; viết "tỉ số", không "tỷ số"; Bài 11 viết $w_t$ | `L10-405` (định nghĩa, có tên tiếng Anh từ 2026-11-13) |
| tỉ số lấy mẫu quan trọng | importance sampling ratio | nhắc lại Định nghĩa 06.24 | `L10-405` |
| biến phân toàn phần (TV) | total variation distance | $D_{\mathrm{TV}}$ | `L10-407` |
| phân kỳ Kullback–Leibler (KL) | Kullback–Leibler divergence | $D_{\mathrm{KL}}$, $\bar D_{\mathrm{KL}}$, $\widehat D$; chiều cũ‖mới; trước `L10-407` mặt trang chỉ nói "khoảng cách giữa hai chính sách" | `L10-407` |
| chặn cải thiện (còn gọi là cận cải thiện) | policy improvement bound | tên tiếng Anh ở trang định nghĩa | `L10-104`; tên tiếng Anh ở `L10-408` |
| cực đại hóa qua hàm chặn dưới | minorize–maximize (MM) | chỉ trong ghi chú diễn giả | `L10-411` |
| miền tin cậy; bài toán miền tin cậy | trust region; trust region problem | bán kính $\kappa$ (là $\delta$ của Schulman và cộng sự, 2015) | `L10-412` |
| tối ưu chính sách miền tin cậy (TRPO) | Trust Region Policy Optimization | tên đầy đủ ở phụ đề bìa; sau đó viết TRPO | `L10-101` |
| ma trận thông tin Fisher | Fisher information matrix | $F$ | `L10-502` |
| gradient tự nhiên | natural gradient | $F^{-1}g$ | `L10-104` |
| gradient liên hợp | conjugate gradient | $\tilde g_k$, $\omega_k$, $\xi_k$ giới thiệu tại thuật toán | `L10-104` |
| tích Fisher–vector | Fisher–vector product | $v\mapsto Fv$ | `L10-506` |
| tìm kiếm lùi | backtracking line search | hệ số $\zeta$ | `L10-507` |
| tối ưu chính sách gần kề (PPO) | Proximal Policy Optimization | tên đầy đủ ở phụ đề bìa; sau đó viết PPO | `L10-101` |
| mục tiêu cắt; bán kính cắt | clipped objective; clip range | $\mathcal L^{\mathrm{CLIP}}$, $\epsilon$ | `L10-104`; `L10-603` |
| lặp chính sách bảo thủ (CPI) | conservative policy iteration | chỉ số trên $\mathcal L^{\mathrm{CPI}}$ | `L10-603` (mặt trang từ 2026-11-13) |
| chặn dưới bi quan | pessimistic bound | | `L10-606` |
| mục tiêu phạt KL; hệ số phạt thích nghi | KL-penalized objective; adaptive KL penalty coefficient | $\beta$, $\kappa_{\mathrm{targ}}$ | `L10-607` |
| entropy | entropy | $\mathcal H$; giữ nguyên | `L10-609` |
| hàm mất mát tổng; mất mát giá trị | total loss; value loss | $L(\theta,w)$; $L^V$ | `L10-609` |
| approxKL (KL xấp xỉ) | approximate KL | tên đại lượng chẩn đoán, giữ nguyên | `L10-104` (tên); định nghĩa ở `L10-611` |
| tỉ lệ cắt | clip fraction | không trùng tập mẫu có gradient bằng $0$ | `L10-104`; định nghĩa ở `L10-611` |
| phương sai được giải thích | explained variance | | `L10-611` |
| dừng sớm | early stopping | theo approxKL | `L10-613` |
| cắt mất mát giá trị | value function clipping | biến thể của Định nghĩa 10.46; công thức và $\epsilon$ trên mặt trang (D1) | `L10-617` |
| tối ưu mức mã | code-level optimization(s) | Engstrom và cộng sự (2020) | `L10-617` (dòng "Nhu cầu:") |
| điểm dừng | stationary point | $\nabla V(\theta)=0$; tên tiếng Anh trong ghi chú diễn giả (mặt trang ở trần 60 âm tiết) | `L10-618` |
| hầu chắc chắn | almost surely | không dùng "gần như chắc chắn" | `L10-618` |
| hai thang thời gian | two-timescale | mô hình của Jin, Li và Wang (2024); chỉ trong ghi chú diễn giả (D1) | `L10-618` |
| môi trường vector hóa | vectorized environments | $N$ môi trường song song; tên tiếng Anh trong ghi chú diễn giả | `L10-617b` |
| giả nghịch đảo | pseudoinverse (Moore–Penrose) | $F^+$ | `L10-503` |
| mini-batch; epoch | mini-batch; epoch | giữ như Bài 08–09 | `L10-606`; `L10-613` |
| hạ gradient ngẫu nhiên (SGD); Adam | stochastic gradient descent; Adam | | `L10-103` (ghi chú diễn giả) |
| bài toán nhiều cần gạt | multi-armed bandit | chỉ trong ghi chú diễn giả | `L10-201` |

Thuật ngữ bỏ của bộ trang chiếu cũ: "surrogate", "truncation", "rollout", "batch", "value clipping", "clip fraction" để trần; "hợp đồng"; $\widehat A^{\mathrm{actor}}$; $w_t$; $d^\pi$, $\mathbb E_{\mathrm{disc},\pi}$, $\mathbb E_B$; $m_t$, $c_t$ (thay bằng $1-Z_{t+1}$, $(1-Z_{t+1})(1-U_{t+1})$); $H$ cho độ dài đoạn (thay bằng $h$).

## Quyết định ký hiệu

- Phân phối đầu $\mu_0$ (Bài 09: $\rho_0$), nêu ở `L10-102` và trong ghi chú diễn giả.
- Tỉ số $\rho_t(\theta)$, $\rho_\theta(s,a)$; Bài 11 viết $w_t$ cho tỉ số này và $\rho_t$ cho tỉ số với chính sách hành vi, nêu trong ghi chú diễn giả `L10-709`.
- $\epsilon$ (bán kính cắt), $\kappa$ (bán kính KL), $\kappa_{\mathrm{targ}}$ (PPO-Penalty), $\varepsilon_{\mathrm{cg}}$ (ngưỡng gradient liên hợp, chỉ trong thuật toán); $\delta_t$ chỉ là sai số TD.
- $T$ là bước kết thúc lượt; $h$ là độ dài đoạn thu.
- $b$ là đường cơ sở; $\beta$ là hệ số phạt; chính sách hành vi luôn là $\pi_{\mathrm{old}}$.
- $\sigma$ là hàm logistic; độ lệch chuẩn mini-batch viết $s_{\mathcal B}$.
- Chiều KL: ràng buộc TRPO, $D_t$ của PPO-Penalty và approxKL đều là cũ‖mới.
- Không viết $A$ trần cho lợi thế.

## Ánh xạ hai chiều `note-topic-id` ↔ `data-slide-id`

**Chủ đề → trang.**

| `note-topic-id` | nhóm | khối của ghi chú | trang |
|---|---|---|---|
| `lec-10-topic-01` | cầu nối | Kiến thức tiên quyết, Bảng ký hiệu, Quy ước đọc | `L10-102`, `L10-103` |
| `lec-10-topic-02` | cầu nối | Mục tiêu, Bảy phần, §1.1, Ví dụ 10.1, 10.2, hình cấu trúc | `L10-101`, `L10-104`–`L10-110` |
| `lec-10-topic-03` | cốt lõi | §2.1, Ví dụ 10.3, Định nghĩa 10.1, Mệnh đề 10.2, Ví dụ 10.4, Bài tập 10.1 | `L10-200`–`L10-206`, `L10-210` |
| `lec-10-topic-04` | bổ sung | §2.2, Mệnh đề 10.3 | một dòng "Lưu ý:" trên `L10-202` (thuộc tính của trang là `topic-03`) |
| `lec-10-topic-05` | cốt lõi | §2.3, Định nghĩa 10.4, Mệnh đề 10.5, Ví dụ 10.5, Thuật toán 10.6 | `L10-207`–`L10-209` |
| `lec-10-topic-06` | cốt lõi | §2.4, Ví dụ 10.6, 10.7, Định nghĩa 10.7, Mệnh đề 10.8, Thuật toán 10.9, Nhận xét 10.10, Bài tập 10.5 | `L10-211`–`L10-216` (kể cả `L10-212b`) |
| `lec-10-topic-07` | cầu nối | §3.1, Ví dụ 10.8, Định nghĩa 10.11, Bổ đề 10.12 | `L10-300`–`L10-302` |
| `lec-10-topic-08` | cốt lõi | §3.2, Định nghĩa 10.13, Mệnh đề 10.14, 10.15, Ví dụ 10.9 | `L10-303`–`L10-306` |
| `lec-10-topic-09` | cốt lõi | §3.3, Ví dụ 10.10, Thuật toán 10.16, Nhận xét 10.17, Bài tập 10.7 | `L10-307`–`L10-309` |
| `lec-10-topic-10` | cốt lõi | §4.1, Ví dụ 10.11, Định nghĩa 10.18, Bổ đề 10.19, Hệ quả 10.20 | `L10-400`–`L10-404` |
| `lec-10-topic-11` | cốt lõi | §4.2, Định nghĩa 10.21, Mệnh đề 10.22 | `L10-405`, `L10-406` |
| `lec-10-topic-12` | cầu nối | §4.3, Định nghĩa 10.23, Mệnh đề 10.24 | `L10-407` |
| `lec-10-topic-13` | cốt lõi | §4.4, Bổ đề 10.25, Định lý 10.26, Ví dụ 10.12, Hệ quả 10.27 | `L10-408`–`L10-410` |
| `lec-10-topic-14` | cốt lõi | §4.5, Hệ quả 10.29, Định nghĩa 10.30, Hệ quả 10.31, Bài tập 10.11 | `L10-411`–`L10-414` (kể cả `L10-412b`) |
| `lec-10-topic-15` | cốt lõi | §5.1, Ví dụ 10.13–10.15, Định nghĩa 10.32, Mệnh đề 10.33, 10.34, Nhận xét 10.35 | `L10-500`–`L10-504` (kể cả `L10-502b`) |
| `lec-10-topic-16` | cốt lõi | §5.2, Ví dụ 10.16, Thuật toán 10.36, 10.37, Nhận xét 10.38, Bài tập 10.8 | `L10-505`–`L10-510` |
| `lec-10-topic-17` | cốt lõi | §6.1, Ví dụ 10.17, 10.18, Định nghĩa 10.39, Mệnh đề 10.40, 10.41, Nhận xét 10.42 | `L10-600`–`L10-606` |
| `lec-10-topic-18` | cốt lõi | §6.2, Ví dụ 10.19, Định nghĩa 10.43, Nhận xét 10.44 (và câu (d) của Bài tập 10.12) | `L10-607`, `L10-608` |
| `lec-10-topic-19` | cốt lõi | §6.3, Định nghĩa 10.45–10.47, Ví dụ 10.20, Mệnh đề 10.48, Thuật toán 10.49, Bài tập 10.12 | `L10-609`–`L10-613` (kể cả `L10-611b`), `L10-619`, `L10-620` |
| `lec-10-topic-20` | cốt lõi | §6.4, Ví dụ 10.21, bảng siêu tham số, bảng so sánh | `L10-614`–`L10-616` |
| `lec-10-topic-21` | cốt lõi | §6.5, Ví dụ 10.22, Nhận xét 10.50 | `L10-617`, `L10-617b` |
| `lec-10-topic-22` | đọc thêm | §6.6, Nhận xét 10.51 | `L10-618` |
| `lec-10-topic-23` | cầu nối | §7.1–7.5, Tình huống 10.1, 10.2 | `L10-700`–`L10-710` (kể cả `L10-702b`) |
| `lec-10-topic-24` | đọc thêm | §7.6 | một dòng nối Bài 11 trên `L10-710` (thuộc tính của trang là `topic-23`) |

**Trang → chủ đề.** Mỗi trang mang đúng một `data-note-topic-id` theo bảng trên; trang tiêu đề mạch mang chủ đề của khái niệm đầu tiên trong mạch (`L10-200` → `topic-03`, `L10-300` → `topic-07`, `L10-400` → `topic-10`, `L10-500` → `topic-15`, `L10-600` → `topic-17`, `L10-700` → `topic-23`). Đủ 24/24 chủ đề: 22 chủ đề có trang mang thuộc tính; `topic-04` (bổ sung) và `topic-24` (đọc thêm) mỗi chủ đề một dòng. Mọi chủ đề cốt lõi (03, 05, 06, 08–11, 13–21) có ít nhất một trang nội dung. Tổng 101 `data-slide-id` duy nhất (kiểm bằng Playwright ở D1). `L10-705`, `L10-706` (Tình huống 10.1, 10.2) mang `topic-23` dù trong ghi chú các tình huống đứng sau mốc `topic-24`: hai trang là bài tổng hợp của mạch kết luận, và ghi chú cũng xếp tình huống vào `topic-23`; liên kết từ trang chiếu sang ghi chú vì vậy mở §7, không mở mục tình huống. Cột "nhóm" lấy từ bản đồ chủ đề của commit `1c9ef05` (đã bỏ khỏi ghi chú ở `567c96c`) để kiểm độ phủ. Bài tập 10.11 phủ chủ đề 10–14, gán `topic-14` vì đứng cuối mạch; Bài tập 10.12 phủ 17–19, gán `topic-19`.

## Sai khác có chủ ý

**So với ghi chú bài giảng** (cần điều phối viên ghi `review-log.md`).

1. Ví dụ 10.9 (`L10-305`) đặt trước Mệnh đề 10.15 (`L10-306`); ghi chú đặt sau. Lý do: ví dụ đi trước phát biểu trong hành trình khái niệm; ví dụ chỉ dùng $\delta_t$, $\widehat A_t$ đã có ở `L10-302`–`L10-304`.
2. Mệnh đề 10.3 (`topic-04`) thu thành một dòng "Lưu ý:" trên `L10-202`; chứng minh và phạm vi chỉ trong ghi chú diễn giả. Lý do: chủ đề bổ sung, phương án nén.
3. Chứng minh Mệnh đề 10.14 thu thành một dòng "Chứng minh." trên `L10-304`; chứng minh Bổ đề 10.12 chỉ trong ghi chú diễn giả `L10-302` (D1, để có chỗ cho dòng "Trực quan."). Lý do: phương án nén; các bước đầy đủ ở ghi chú bài giảng.
4. Bổ đề 10.25 không có trang riêng: phát biểu trong bước cuối của `L10-409` (chứng minh chặn cải thiện); số kiểm $0{,}009\le0{,}288$ trong ghi chú diễn giả `L10-408`. Lý do: phương án nén.
5. Định nghĩa 10.18 gộp với Bổ đề 10.19 (`L10-403`), Hệ quả 10.20 chỉ trong ghi chú diễn giả. Lý do: phương án nén, rút theo cổng storyboard. Đợt sửa D1 tách các trang kết quả quá tải: Định nghĩa 10.30 (`L10-412`) và Hệ quả 10.31 (`L10-412b`); Định nghĩa 10.32 (`L10-502`) và Mệnh đề 10.33 (`L10-502b`); Định nghĩa 10.47 (`L10-611`, kèm dạng $-\log\rho$ và phương sai được giải thích; entropy trung bình và mất mát giá trị chỉ trong ghi chú diễn giả) và Mệnh đề 10.48 (`L10-611b`). Hệ quả 10.29 ở `L10-411`; Ví dụ 10.19 (`L10-607`) và Định nghĩa 10.43 (`L10-608`) ở hai trang, ví dụ trước quy tắc.
6. Nhận xét 10.42 thành dòng "Lưu ý:" của `L10-606`; Nhận xét 10.44 thành dòng "Lưu ý:" của `L10-608`; Nhận xét 10.35 vào `L10-504`; Nhận xét 10.10 và 10.17 chỉ trong ghi chú diễn giả (`L10-215`, `L10-308`); Nhận xét 10.28 chỉ trong ghi chú diễn giả `L10-408`.
7. Biến thể cắt mất mát giá trị (cuối Định nghĩa 10.46) trình bày ở `L10-617` cùng Ví dụ 10.22, không ở `L10-609`; D1 đặt ví dụ này (`L10-617`) trước bảng của Nhận xét 10.50 (`L10-617b`), đúng thứ tự Ví dụ 10.22 → Nhận xét 10.50 của ghi chú.
8. Tình huống 10.3 (Breakout) không lên mặt trang; số đo notebook không trình chiếu như số đo của PPO. Câu (e) của Bài tập 10.11 ($0{,}317$) chỉ trong ghi chú diễn giả `L10-414`.
9. Bài tập 10.1, 10.5, 10.7, 10.8, 10.11(a)–(d), 10.12 và Tình huống 10.1–10.2 lên mặt trang làm bài tập có lời giải; câu (d) của Bài tập 10.12 (PPO-Penalty) đặt ở `L10-608`, ngay sau định nghĩa, còn (a)–(c) ở `L10-619`–`L10-620`; các bài còn lại là bài về nhà (bảng `Mạch | Bài tập` ở `L10-709` trùng bảng §7.5 của ghi chú, sáu hàng như ghi chú).
10. `L10-207` đặt phần đầu của Ví dụ 10.5 (bài toán một bước, $q_\pi=(3;\,0)$, $v_\pi=2$) ngay sau dòng trực quan, trước Định nghĩa 10.4; ghi chú đi theo thứ tự Định nghĩa 10.4 → Mệnh đề 10.5 → Ví dụ 10.5. Lý do: ví dụ đi trước định nghĩa trong hành trình khái niệm; chuỗi suy luận không đổi. (Vai mạch, vòng D1.)
11. `L10-408` phát biểu Hệ quả 10.27 (dạng KL) ngay sau Định lý 10.26, trước Ví dụ 10.12 (`L10-410`); ghi chú đặt Ví dụ 10.12 trước Hệ quả 10.27. Lý do: một trang kết quả giữ định lý và hệ quả dạng KL cạnh nhau; ví dụ chỉ dùng dạng TV trên mặt trang, dạng KL ở ghi chú diễn giả. (Vai mạch, vòng D1.)
12. `L10-612` (đường dữ liệu, bảng "giữ cố định / tính lại", ở ghi chú đứng sau Thuật toán 10.49) đứng trước `L10-613` (Thuật toán 10.49). Lý do: trang đóng vai trực giác của cụm thuật toán PPO, trước giả mã. (Vai mạch, vòng D1.)
13. Số hiệu của ghi chú đứng trong nhãn của trang phát biểu kết quả ("**Mệnh đề 10.2.**"), một số hiệu mỗi trang; khi trang có hai kết quả, chỉ kết quả chính mang số (`L10-302` Định nghĩa 10.11; `L10-403` Bổ đề 10.19; `L10-407` Định nghĩa 10.23; `L10-408` Định lý 10.26), số hiệu còn lại ở ghi chú diễn giả. (Quyết định E2.)

**So với bài giảng gốc** (theo ánh xạ của ghi chú).

1. Tr. 5–8 (ôn REINFORCE, định lý gradient chính sách) thành trang nhắc lại `L10-103`; tr. 1–2 thành bìa và mục tiêu.
2. Tr. 24 (GAE trên đoạn thu) đưa lên mạch 3 (`L10-307`–`L10-309`), trước phần PPO, vì thuật toán GAE lùi là tiên quyết của Thuật toán 10.49.
3. Tr. 38 (PPO-Penalty) đưa lên ngay sau PPO-Clip (`L10-607`), vì ghi chú đặt hai biến thể cạnh nhau.
4. Tr. 26 (bảng siêu tham số không ghi nguồn) thay bằng Bảng 3 và Bảng 5 của Schulman và cộng sự (2017) (`L10-615`).
5. Tr. 29–34, 36 (chi tiết cài đặt) nén vào `L10-617`; tr. 35 (chẩn đoán miền tin cậy) chia cho `L10-606`, `L10-611`.
6. Tr. 37, 39–42 (lý thuyết PPO-Clip) nén vào trang đọc thêm `L10-618`; kết luận theo Jin, Li và Wang (2024), có giả thiết và phạm vi.
7. Bổ sung không có trong nguồn, theo ghi chú: hai ví dụ dẫn nhập định lượng (tr. 9–10, 14 chỉ nêu bằng lời), đường cơ sở tối ưu (Greensmith và cộng sự, 2004), chứng minh bổ đề hiệu hiệu năng (Kakade và Langford, 2002), chặn cải thiện dạng trung bình (Achiam và cộng sự, 2017), gradient liên hợp (Nocedal và Wright, 2006), approxKL và mệnh đề không chệch.

## Nguồn theo trang

| trang nguồn | nội dung | trang đích |
|---|---|---|
| 1–3 | bìa, mục tiêu, dàn ý | `L10-101`, `L10-104`, `L10-105` |
| 4 | bức tranh chung, bước lớn đổi phân bố trạng thái | `L10-108`, `L10-109`, `L10-401` |
| 5 | ký hiệu | `L10-102` |
| 6–10 | hàm mục tiêu, định lý gradient chính sách, REINFORCE | `L10-103`, `L10-106`, `L10-107` |
| 11 | đường cơ sở | `L10-201`–`L10-206`, `L10-209`, `L10-210` |
| 12 | actor–critic | `L10-211`–`L10-216` |
| 13 | GAE | `L10-301`–`L10-306` |
| 14 | vì sao cần TRPO | `L10-108`, `L10-401`, `L10-408` |
| 15 | hiệu hiệu năng, hàm thay thế | `L10-402`–`L10-406`, `L10-413`, `L10-414` |
| 16 | bài toán ràng buộc của TRPO | `L10-408`, `L10-410`, `L10-411`, `L10-412`, `L10-412b` |
| 17 | KL bậc hai, gradient tự nhiên | `L10-501`–`L10-504` (kể cả `L10-502b`) |
| 18–19 | TRPO thực hành, chi phí | `L10-505`–`L10-509`, `L10-601` |
| 20–22 | PPO-Clip, gradient sau khi cắt | `L10-601`–`L10-606` |
| 23 | hàm mất mát tổng | `L10-609`, `L10-610` |
| 24 | thu dữ liệu, GAE trên đoạn | `L10-307`–`L10-309`, `L10-612`, `L10-613` |
| 25 | vòng tối ưu PPO | `L10-613` |
| 26 | siêu tham số (thay bằng bảng có nguồn) | `L10-615` |
| 27 | chẩn đoán | `L10-611`, `L10-614` |
| 28 | so sánh TRPO và PPO | `L10-616`, `L10-703` |
| 29–34, 36 | chi tiết cài đặt | `L10-617`, `L10-617b` |
| 35 | chẩn đoán miền tin cậy | `L10-606`, `L10-611b` |
| 37, 39–42 | lý thuyết PPO-Clip | `L10-618`, `L10-704` |
| 38 | PPO-Penalty | `L10-607`, `L10-608` |
| 43 | tài liệu tham khảo | `L10-707`, `L10-710` |

## Hình

| hình | trạng thái | trang |
|---|---|---|
| `img/lec-10/central-problem.svg` | đã duyệt (ghi chú) | `L10-110` |
| `img/lec-10/two-state-chain.svg` | đã duyệt | `L10-211` (lưới hai cột, dữ kiện phần thưởng và chính sách ghi thành chữ bên cạnh, quyết định E5); bản nhỏ ở `L10-301` (dữ kiện cần dùng ghi trong dòng chữ); bản viết bỏ hình nhỏ ở `L10-402` |
| `img/lec-10/actor-critic-advantage.svg` | đã duyệt | `L10-212b` |
| `img/lec-10/gae-weights.svg` | đã duyệt | `L10-303` |
| `img/lec-10/policy-update-feedback.svg` | đã duyệt | `L10-401` |
| `img/lec-10/trpo-trust-region.svg` | đã duyệt | `L10-505` |
| `img/lec-10/ppo-one-step-plateau.svg` | đã duyệt | `L10-602` |
| `img/lec-10/ppo-clipping-signs.svg` | đã duyệt | `L10-605` |
| `img/lec-10/ppo-data-pipeline.svg` | đã duyệt | `L10-612` |
| `img/lec-09/one-step-card.svg` | dùng lại | `L10-106`, `L10-202`, `L10-504` (bản viết bỏ ở `L10-610`) |
| `img/lec-09/short-corridor.svg` | dùng lại | `L10-107` |
| `img/lec-08/termination-truncation.svg` | không dùng (D1 bỏ khỏi `L10-307`: nhãn mục tiêu DQN gây nhầm, bảng đủ dữ kiện; mô tả hai cờ ở ghi chú diễn giả) | — |
| `img/lec-10/gae-bias-variance.svg`, `img/lec-10/ppo-diagnostics.svg` | đã xóa | không trang nào tham chiếu (khẳng định không căn cứ; thay bằng bảng) |

Không vẽ hình mới. Các phép tính lặp dùng bảng HTML cố định thay hình (xem `storyboard.md`, mục "Khuôn bảng cố định").

## Phân bổ thời lượng

| mạch | trang | số trang | phút |
|---|---|---:|---:|
| 1 | `L10-101`–`L10-110` | 10 | 12 |
| 2 | `L10-200`–`L10-216` | 18 | 23 |
| 3 | `L10-300`–`L10-309` | 10 | 14,5 |
| 4 | `L10-400`–`L10-414` | 16 | 22,5 |
| 5 | `L10-500`–`L10-510` | 12 | 13,5 |
| 6 | `L10-600`–`L10-620` | 23 | 25,5 |
| 7 | `L10-700`–`L10-710` | 12 | 9 |
| **Tổng** | | **101** | **120** |

Phút từng trang nằm trong `storyboard.md`.
