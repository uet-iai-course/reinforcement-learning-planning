# Bài 07: Xấp xỉ hàm trong Học tăng cường

Bản viết lại ngày 2026-10-12 (giai đoạn II của đợt sửa theo chuẩn 2026-10-12), khớp deck `2627-1/lecture-07-xap-xi-ham.html` gồm 7 mạch, 75 trang (cập nhật 2026-10-14 sau vòng rà soát năm vai và biên tập), và ghi chú bài giảng đã commit (`7d686bf`). Bản trước được giữ trong lịch sử git.

## Phạm vi

- Nguồn chính: bài giảng gốc (2025–2026), *Hàm xấp xỉ trong Reinforcement Learning*, 45 trang (tệp PDF không được theo dõi; trích dẫn dạng "bài giảng gốc (2025–2026), trang N").
- Nguồn bài tập: Bài tập tuần 7 (2025–2026), 8 bài.
- Nguồn chuẩn cho ký hiệu, số liệu, số hiệu kết quả: `2627-1/materials/lec-07/lecture-note.md` (bộ đếm chung 07.1–07.41, Ví dụ 07.1–07.16, Bài tập 07.1–07.19, Tình huống 07.1–07.2).
- Đối tượng: sinh viên đã học MDP, quy hoạch động, Monte Carlo, TD(0), Sarsa và Q-learning dạng bảng (Bài 03–06).
- Thời lượng: phần trình chiếu chính 120 phút (7 mạch: 9 + 22,5 + 17 + 30 + 14 + 16 + 11,5). Khối 30 phút ngoài 120 phút: ba bài chữa trên trang (`X01`/`X01b` 6 phút, `X02`/`X02b` 7 phút, `X03`/`X03b` 9 phút, nằm trong mạch 3 và mạch 5) và 8 phút trình diễn notebook.
- Không có code demo trong deck; hai notebook thực hành (Lunar Lander, Flappy Bird) chỉ được dẫn số liệu "một lần chạy đã nhúng trong notebook".
- Bảng phân loại tr. 4 của nguồn (actor-critic) nằm ngoài phạm vi. Kết quả MDP tuyến tính (tr. 42) chỉ ở ghi chú diễn giả `L07-34` và phần đọc thêm của ghi chú bài giảng.

## Mục tiêu học tập

Khớp mặt trang `L07-03` và mục "Mục tiêu học tập" của ghi chú bài giảng.

1. Viết $\hat v(s,w)=x(s)^\top w$, $\hat q(s,a,w)=x(s,a)^\top w$; tính mức lan; nhận diện nhập nhằng (Bài tập 07.1–07.3, 07.12, 07.15, 07.16).
2. Tính tay một cập nhật Monte Carlo gradient, TD(0), Sarsa và Q-learning bán gradient (Bài tập 07.7, 07.10, 07.11, 07.13).
3. Phân biệt gradient đầy đủ với bán gradient, chỉ ra số hạng bị bỏ (Bài tập 07.4, 07.5, 07.7).
4. Tính điểm cố định Bellman chiếu, nghiệm Monte Carlo trên ví dụ nhỏ; nêu đủ giả thiết hội tụ của TD(0) tuyến tính (Bài tập 07.8, 07.9, 07.17).
5. Phân biệt mục tiêu Sarsa với mục tiêu Q-learning; nhận diện bộ ba bất ổn (Bài tập 07.13, 07.14, 07.18).
6. Đối chiếu kết quả chạy với giả thiết trước khi kết luận về hội tụ hay phân kỳ (Bài tập 07.6, 07.19).

## Khung lý thuyết chung

- **Bài toán trung tâm:** học giá trị và chính sách khi không lưu được một ô cho mỗi trạng thái (`L07-03c`).
- **Đối tượng và ký hiệu chung:** đặc trưng $x(s)$, $x(s,a)\in\mathbb R^d$; tham số dùng chung $w$, $w_n$ sau $n$ lần cập nhật với bước $\alpha_n$; $t$ là thời điểm của mẫu; mục tiêu cập nhật $y_t$; $J_\mu$; $\Phi$, $D=\operatorname{diag}(d_\pi)$, $\Pi_D$, $T_\pi$, $A$, $b$.
- **Khung cập nhật:** $w_{n+1}=w_n+\alpha_n\bigl(y_t-\hat v(S_t,w_n)\bigr)\nabla_w\hat v(S_t,w_n)$ (`L07-02`), với ba điểm đối chiếu: mục tiêu (lợi tức hay bootstrap), dữ liệu (theo hay khác chính sách), chính sách (cố định hay cải thiện theo $w$).
- **Giả thiết chung:** MDP hữu hạn khi dùng dạng ma trận; phần thưởng bị chặn; $\gamma<1$ hoặc lượt kết thúc với thời gian kỳ vọng hữu hạn; giá trị tại trạng thái kết thúc bằng $0$; lượt bị cắt ngắn không phải lượt kết thúc.
- **Chuỗi định nghĩa → kết quả → phương pháp:** hàm tuyến tính (Định nghĩa 07.1) → mức lan (Mệnh đề 07.2) → sai số giá trị $J_\mu$ (07.5) → nhập nhằng (07.10) → mục tiêu cập nhật, gradient đầy đủ (07.12) → Monte Carlo là SGD trên $J_\mu$ (07.14) → hội tụ tới $w_{\mathrm{MC}}$ (07.17) → bán gradient (07.21) → hướng trung bình $b-Aw$ (07.25) → điểm cố định Bellman chiếu (07.26) → $A$ xác định dương (07.28) → hội tụ tới $w_{\mathrm{TD}}$ (07.29) → Sarsa (07.33, không có bảo đảm chung, 07.34) → Q-learning (07.35, 07.36) → phân kỳ khi đủ bộ ba bất ổn (07.37, 07.38) → bảng phạm vi (07.40), năm bước phân tích (07.41).
- **Giới hạn áp dụng:** mọi bảo đảm của bài chỉ phủ dự đoán với chính sách cố định và hàm tuyến tính; điều khiển tuyến tính không có bảo đảm chung; mạng nơ-ron thuộc Bài 08.

## Dàn ý bảy mạch và thời lượng

| N | Mạch | Trang tiêu đề (`id`) | Trang | Mục ghi chú | Phút |
|---|---|---|---|---|---:|
| 1 | Mở đầu | bìa `L07-01` | `L07-01`, `L07-01b`, `L07-01c`, `L07-03`, `L07-03b`, `L07-03c`, `L07-02` | Mục tiêu, Tiên quyết | 9 |
| 2 | Hàm giá trị tuyến tính theo đặc trưng | `L07-M2T` (`mach-2`) | `L07-04`–`L07-11b` (11 trang nội dung) | Mục 1 | 22,5 |
| 3 | Monte Carlo gradient với hàm xấp xỉ | `L07-M3T` (`mach-3`) | `L07-12`–`L07-17b`, `X01`, `X01b` | Mục 2 | 17 (+6 chữa bài) |
| 4 | TD(0) bán gradient và điểm cố định Bellman chiếu | `L07-M4T` (`mach-4`) | `L07-18`–`L07-25` (14 trang nội dung, có `L07-19b`) | Mục 3 | 30 |
| 5 | Sarsa bán gradient cho điều khiển | `L07-M5T` (`mach-5`) | `L07-26`, `L07-27`, `L07-30`, `L07-28`, `L07-29`, `X02`, `X02b`, `X03`, `X03b` | Mục 4 | 14 (+16 chữa bài) |
| 6 | Q-learning bán gradient và bộ ba bất ổn | `L07-M6T` (`mach-6`) | `L07-31`, `L07-31b`, `L07-31c`, `L07-31d`, `L07-31e`, `L07-32b`, `L07-32c`, `L07-32`, `L07-33`, `L07-33b` | Mục 5 | 16 |
| 7 | Tổng kết và chuyển tiếp | `L07-M7T` (`mach-7`) | `L07-36`, `L07-36b`, `L07-36c`, `L07-34`, `L07-35`, `L07-35b`, `L07-36d`, `L07-36e`, `L07-36f` | Mục 6, Tóm tắt | 11,5 |
| | Tổng | | 75 trang (69 trang trong 120 phút, 6 trang chữa bài) | | 120 (+30) |

Tổng kiểm tra: $9+22{,}5+17+30+14+16+11{,}5=120$; khối 30 phút: $6+7+9$ chữa bài $+\,8$ trình diễn notebook. Thời lượng từng trang ở `storyboard.md`.

## Ánh xạ nguồn

| Trang nguồn | Quyết định | Trang đích | Lý do |
|---:|---|---|---|
| 1–4 | giữ, gộp, tách | `L07-01`, `L07-03`, `L07-03b`, `L07-02` | Tên bài, mục tiêu; ba điểm đối chiếu tr. 3 thành khung chung `L07-02`; bỏ trang mục lục lặp. |
| 5–20 | gộp | `L07-01b` (Nhắc lại), ghi chú diễn giả | Chỉ nhắc điều kiện hội tụ dạng bảng; chi tiết ở ghi chú Bài 05–06. |
| 21 | bỏ | — | Mục lục trung gian. |
| 22–23 | giữ, tách | `L07-04`–`L07-06` | Vấn đề bảng tra (thêm số liệu Lunar Lander, Flappy Bird từ notebook), hàm tham số, ví dụ mức lan. |
| 24–26 | giữ, gộp | `L07-08`, ghi chú `L07-08`, `L07-34` | Dạy lớp tuyến tính; các lớp khác chỉ gọi tên. |
| 27 | giữ, sửa | `L07-12`, `L07-13`, `L07-18` | Mục tiêu không chứa $w$ và chứa $w$. |
| 28–31 | giữ, vẽ lại, tách | `L07-09`, `L07-10`, `L07-10b`, `L07-11` | Vector điều hướng, ba miền (SVG), mã hóa bốn khối $(\phi;\mathbf 1_a;\phi\otimes\mathbf 1_a;1)$, nhập nhằng. |
| 32 | sửa, tách | `L07-13`, `L07-15`, `L07-20` | Monte Carlo là gradient đầy đủ; TD là bán gradient. |
| 33–34 | giữ, sửa | `L07-14`–`L07-17b`, `X01`, `X01b` | Ví dụ, gradient, thuật toán, định lý có đủ giả thiết, chứng minh. |
| 35–37 | giữ, mở rộng | `L07-18`–`L07-25` | Mục tiêu TD, bán gradient, thuật toán, Bellman chiếu, ví dụ hai trạng thái (bổ sung), định lý, chứng minh, so sánh. |
| 38–40 | giữ, sắp lại | `L07-26`–`L07-29`, `L07-30`, `X02`, `X03` | Giá trị hành động, chuỗi năm trạng thái, Sarsa; ví dụ tính tay trước công thức. |
| 38, 41 | giữ, mở rộng | `L07-31`–`L07-33b` | Mục tiêu Q-learning, thuật toán (bổ sung theo notebook), ví dụ phân kỳ (bổ sung, Sutton–Barto §11.2), bộ ba bất ổn. |
| 42–43 | gộp | `L07-34` (ghi chú diễn giả) | MDP tuyến tính, vấn đề mở: chỉ ở ghi chú. |
| 44–45 | giữ | `L07-36`–`L07-36f` | Tổng kết, phạm vi, tài liệu. |
| HW 1–3 | tự ôn, trang | `L07-36e`, `L07-33`, `L07-33b` | Bài 3 thành bài tập trên trang (Bài tập 07.14). |
| HW 4 | giữ | `X01`, `X01b` | Bài tập 07.5. |
| HW 5–6 | trang, tự ôn | `L07-22`, `L07-23`, `L07-24c`; `L07-36f` | Bài tập 07.8, 07.6. |
| HW 7 | giữ | `X02`, `X02b` | Bài tập 07.10. |
| HW 8 | giữ | `L07-30`, `X03`, `X03b`, `L07-31` | Bài tập 07.11; mẫu 2 dùng lại để so Sarsa với Q-learning. |

## Thuật ngữ Việt–Anh

| Tiếng Việt | Tiếng Anh | Trang dùng lần đầu |
|---|---|---|
| xấp xỉ hàm | function approximation | `L07-01c` |
| đặc trưng | feature | `L07-01c` |
| lợi tức | return | `L07-01b` |
| lượt | episode | `L07-04` |
| nhập nhằng | aliasing | `L07-03` |
| bán gradient | semi-gradient | `L07-03` |
| gradient đầy đủ | full gradient | `L07-03` (mặt trang) |
| bộ ba bất ổn | deadly triad | `L07-03` |
| mục tiêu bootstrap | bootstrap target | `L07-02` |
| theo chính sách / khác chính sách | on-policy / off-policy | `L07-03c` / `L07-02` |
| sai phân thời gian | temporal difference, TD | `L07-03` |
| quá trình quyết định Markov | Markov decision process, MDP | ghi chú `L07-07b` |
| tác tử | agent | ghi chú `L07-07b` |
| hàm nhân; mã hóa lưới ô | kernel; tile coding | ghi chú `L07-08` |
| cắt ngắn | truncation | `L07-16` |
| mọi lần ghé; lần ghé đầu tiên | every-visit; first-visit | `L07-16`; ghi chú `L07-16` |
| hạ gradient ngẫu nhiên | stochastic gradient descent, SGD | `L07-15` |
| hầu chắc chắn | almost surely | `L07-17` |
| sai số giá trị | value error ($\overline{\mathrm{VE}}=2J_\mu$) | `L07-07b` |
| phân phối dừng | stationary distribution | `L07-01b` |
| tối giản; không tuần hoàn (chuỗi Markov) | irreducible; aperiodic | `L07-24` |
| điểm cố định Bellman chiếu | projected Bellman fixed point | `L07-03` |
| toán tử Bellman chiếu | projected Bellman operator | `L07-23` |
| mục tiêu TD, còn gọi là mục tiêu một bước | TD target | `L07-12` |
| TD bình phương tối thiểu | least-squares TD, LSTD | ghi chú `L07-25` |
| phá hòa | tie-breaking | ghi chú `L07-26` |
| chính sách hành vi / chính sách đích | behavior policy / target policy | `L07-31b` |
| (tỉ số) lấy mẫu quan trọng | importance sampling | `L07-32b` (tỉ số $\rho=\pi/\pi_b$, nhắc lại Bài 06); `L07-33` dùng tên tiếng Việt |
| chính sách xác định | deterministic policy | dạng chốt của học phần (quyết định chung mục 5); bài không dùng trên mặt trang |
| mạng mục tiêu; bộ nhớ phát lại | target network; replay buffer | ghi chú `L07-32`, `L07-36f` |
| hạt giống ngẫu nhiên | random seed | ghi chú `L07-35b` |

## Ký hiệu

Theo bảng ký hiệu của ghi chú bài giảng; các điểm đã đổi so với deck cũ: `^T` → `^\top`; $e_a$ → $\mathbf 1_a$ (tránh trùng sai lệch $e$); số chiều $p$ của $\phi$ → $k$ (tránh trùng $p(s',r\mid s,a)$); $c_a$, $u_a$, $b$ (khối bốn) → $[w^{(2)}]_a$, $w^{(3)}_a$, $w^{(4)}$; $w_t$, $\alpha_t$ → $w_n$, $\alpha_n$ (chỉ số lần cập nhật), $t$ chỉ thời điểm mẫu; tên trạng thái chuỗi $\mathrm A$–$\mathrm E$ chữ đứng; giữ $u(a)$; vector viết $(a;b)$ không có dấu chuyển vị; dấu phẩy thập phân.

| Ký hiệu | Nghĩa và miền |
|---|---|
| $x(s)$, $x(s,a)\in\mathbb R^d$ | vector đặc trưng |
| $\phi(s)\in\mathbb R^k$, $\mathbf 1_a\in\{0,1\}^m$ | đặc trưng trạng thái của mã hóa bốn khối; vector chỉ thị hành động |
| $w$, $w_n$, $[w]_i$ | tham số; tham số sau $n$ lần cập nhật; thành phần thứ $i$ |
| $\alpha_n$, $\alpha$ | bước học của lần cập nhật từ $w_n$; bước hằng trong ví dụ |
| $\hat v(s,w)=x(s)^\top w$, $\hat q(s,a,w)=x(s,a)^\top w$ | giá trị ước lượng |
| $y_t$, $e_t$, $\delta_t$ | mục tiêu cập nhật; sai lệch Monte Carlo; sai số TD |
| $\ell_t$, $J_\mu$, $\mu$ | mất mát mẫu; sai số giá trị; phân phối trọng số |
| $\Sigma_\mu$, $w_{\mathrm{MC}}$ | $\sum_s\mu(s)x(s)x(s)^\top$; điểm cực tiểu của $J_\mu$ |
| $d_\pi$, $D$ | phân phối dừng dưới $\pi$; $\operatorname{diag}(d_\pi)$ |
| $\Phi$ | ma trận đặc trưng, hàng $x(s)^\top$ |
| $P_\pi$, $r_\pi$, $T_\pi$ | ma trận chuyển, phần thưởng kỳ vọng, toán tử Bellman |
| $\Pi_D$, $\lVert\cdot\rVert_D$ | phép chiếu lên $\{\Phi w\}$; chuẩn có trọng số |
| $A$, $b$, $w_{\mathrm{TD}}$ | $\Phi^\top D(I-\gamma P_\pi)\Phi$; $\Phi^\top Dr_\pi$; nghiệm $Aw=b$ |
| $\pi_w$, $\pi_b$, $\rho_t$ | chính sách $\varepsilon$-tham lam theo $\hat q(\cdot,\cdot,w)$; chính sách hành vi; tỉ số lấy mẫu quan trọng |
| $d_{\text{trái}}(s)$, $u(a)$ | khoảng cách tới tường trái, dấu của hành động (chuỗi năm trạng thái) |
| $J_{\mathrm{kt}}$ | thước đo trên tập kiểm tra của notebook Lunar Lander |
| $\kappa$ | hằng của bước học chuẩn hóa $\alpha=\kappa/\mathbb E\lVert x\rVert^2$ (chỉ trong ghi chú bài giảng) |

## Ví dụ xuyên suốt

- **Trạng thái hai đặc trưng** (dự đoán): `L07-06` (mức lan), `L07-12` và `L07-14` (cùng mẫu: hai mục tiêu, một cập nhật Monte Carlo), `L07-19`, `L07-20c` (TD(0), số hạng bị bỏ). Số liệu sư phạm tự xây dựng, giữ nguyên số cũ (quyết định chung mục 8).
- **Hai trạng thái với đặc trưng 1 và 2**: `L07-23b`, `L07-24c` (Bellman chiếu, $w_{\mathrm{TD}}$ so với $w_{\mathrm{MC}}$), `L07-32b`, `L07-32c` (cùng hai đặc trưng, mảnh MDP khác; TD(0) dự đoán khác chính sách với $\rho=1$ trên $s_1\to s_2$, $\rho=0$ tại $s_2$, phân kỳ; Q-learning chỉ được nói là có phản ví dụ tương tự theo Sutton và Barto §11.2).
- **Chuỗi năm trạng thái** (điều khiển): `L07-27`, `L07-30`, `X02`, `X03`, `L07-31` (Sarsa và Q-learning trên cùng mẫu thứ hai), `L07-31d`/`L07-31e` (ba cập nhật Q-learning so với Sarsa).
- **Lunar Lander, Flappy Bird** (notebook): `L07-04`, `L07-09`, `L07-11`, `L07-12`, `L07-18`, `L07-35`; số liệu theo ghi chú bài giảng.

## Danh mục 75 mã trang

Mạch 1: `L07-01`, `L07-01b`, `L07-01c`, `L07-03`, `L07-03b`, `L07-03c`, `L07-02`. Mạch 2: `L07-M2T`, `L07-04`, `L07-05`, `L07-06`, `L07-08`, `L07-07`, `L07-07b`, `L07-09`, `L07-10`, `L07-10b`, `L07-11`, `L07-11b`. Mạch 3: `L07-M3T`, `L07-12`, `L07-13`, `L07-14`, `L07-15`, `L07-16`, `L07-17`, `L07-17b`, `X01`, `X01b`. Mạch 4: `L07-M4T`, `L07-18`, `L07-19`, `L07-19b`, `L07-20`, `L07-20b`, `L07-20c`, `L07-21`, `L07-22`, `L07-23`, `L07-23b`, `L07-24`, `L07-24b`, `L07-24c`, `L07-25`. Mạch 5: `L07-M5T`, `L07-26`, `L07-27`, `L07-30`, `L07-28`, `L07-29`, `X02`, `X02b`, `X03`, `X03b`. Mạch 6: `L07-M6T`, `L07-31`, `L07-31b`, `L07-31c`, `L07-31d`, `L07-31e`, `L07-32b`, `L07-32c`, `L07-32`, `L07-33`, `L07-33b`. Mạch 7: `L07-M7T`, `L07-36`, `L07-36b`, `L07-36c`, `L07-34`, `L07-35`, `L07-35b`, `L07-36d`, `L07-36e`, `L07-36f`.

Thứ tự trình chiếu khác thứ tự số ở `L07-08` trước `L07-07`, `L07-30` trước `L07-28`, `L07-32b` trước `L07-32`, và `L07-36`–`L07-36c` trước `L07-34`; mã được giữ để không đổi định danh của trang cũ.

## Ánh xạ hai chiều ghi chú–trang chiếu

Mỗi trang mang đúng một `data-note-topic-id`; trang tiêu đề mạch mang mã của chủ đề đầu tiên trong mạch.

| Topic | Mục ghi chú | Trang chiếu |
|---|---|---|
| `lec-07-topic-13` | Kiến thức tiên quyết | `L07-01`, `L07-01b`, `L07-01c`, `L07-03`, `L07-03b`, `L07-03c`, `L07-02` |
| `lec-07-topic-01` | 1.1 | `L07-M2T`, `L07-04` |
| `lec-07-topic-02` | 1.2 | `L07-05`, `L07-06`, `L07-08` |
| `lec-07-topic-03` | 1.3 | `L07-07`, `L07-07b` |
| `lec-07-topic-04` | 1.4 | `L07-09`, `L07-10`, `L07-10b`, `L07-11`, `L07-11b` |
| `lec-07-topic-05` | 2.1 | `L07-M3T`, `L07-12`, `L07-13` |
| `lec-07-topic-06` | 2.2 | `L07-14`, `L07-15`, `L07-16` |
| `lec-07-topic-15` | 2.3 | `L07-17`, `L07-17b`, `X01`, `X01b` |
| `lec-07-topic-07` | 3.1 | `L07-M4T`, `L07-18`, `L07-19`, `L07-19b`, `L07-20`, `L07-20b`, `L07-20c` |
| `lec-07-topic-08` | 3.2 | `L07-21`, `L07-22`, `L07-23`, `L07-23b`, `L07-24`, `L07-24b`, `L07-24c` |
| `lec-07-topic-09` | 3.3 | `L07-25` |
| `lec-07-topic-10` | 4.1–4.2 | `L07-M5T`, `L07-26`, `L07-27`, `L07-30`, `L07-28`, `L07-29` |
| `lec-07-topic-16` | 4.3 | `X02`, `X02b`, `X03`, `X03b` |
| `lec-07-topic-11` | 5.1 | `L07-M6T`, `L07-31`, `L07-31b`, `L07-31c`, `L07-31d`, `L07-31e` |
| `lec-07-topic-17` | 5.2 | `L07-32b`, `L07-32c`, `L07-32`, `L07-33`, `L07-33b` |
| `lec-07-topic-14` | 6.1 | `L07-M7T`, `L07-36`, `L07-36b`, `L07-36c`, `L07-34` |
| `lec-07-topic-12` | 6.2 | `L07-35`, `L07-35b`, `L07-36d`, `L07-36e`, `L07-36f` |
| `lec-07-topic-18` | Hướng dẫn đọc thêm (MDP tuyến tính) | không có trang riêng; nhắc trong ghi chú diễn giả `L07-34` |

## Tài sản trực quan

Mười một SVG trong `2627-1/img/lec-07/` được deck dùng; không có raster. Vòng biên tập 2026-10-14: thêm `two-state-offpolicy.svg`; sửa nhãn `projected-bellman.svg` và `two-state-features.svg`.

1. `tabular-vs-parametric.svg` (`L07-05`);
2. `shared-parameter-effect.svg` (`L07-06`);
3. `linear-pipeline.svg` (`L07-08`);
4. `feature-domains.svg` (`L07-09`);
5. `mc-update-vector.svg` (`L07-14`; nhãn $w_n$, $w_{n+1}$ đã sửa ở giai đoạn I);
6. `projected-bellman.svg` (`L07-21`; nhãn hình chiếu đổi thành $\Pi_D T_\pi(\Phi w)$, RL 13);
7. `control-loop.svg` (`L07-26`);
8. `five-state-features.svg` (`L07-27`);
9. `chain-strip-dc.svg` (`L07-30`);
10. `two-state-offpolicy.svg` (`L07-32b`; mới: chỉ ô khác chính sách, chữ 32–34 trong viewBox 1200, $\rho=1$ trên $s_1\to s_2$, $\rho=0$ tại $s_2$). `two-state-features.svg` không còn trên deck, chỉ dùng trong ghi chú bài giảng; nhãn ô đổi thành "(a) Theo chính sách", "(b) Khác chính sách", bỏ số hiệu ví dụ;
11. `deadly-triad.svg` (`L07-32`).

`chapter-map.svg` chỉ dùng trong ghi chú bài giảng: nhãn "Mục 1–6" theo số mục của ghi chú, lệch một với số mạch của deck, nên không đặt lên trang chiếu.
