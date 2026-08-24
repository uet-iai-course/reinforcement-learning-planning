# Nhật ký rà soát Bài 10

## Nguồn và phạm vi

- Nguồn chính: `RL-hk2-2025-2026/lecture10_policy_gradient_part2.pdf`, 43 trang.
- Nguồn được bản gốc dẫn: Williams (1992); Schulman et al. (2015, 2016, 2017); Engstrom et al. (2020); Jin, Li và Wang (2024).
- Không thêm dữ liệu thực nghiệm, benchmark hoặc tuyên bố định lượng ngoài nguồn.
- Không có ngoại lệ ảnh raster. Tám hình kỹ thuật được vẽ lại bằng SVG cục bộ.

## Sai khác có chủ ý so với nguồn

| mức độ | vị trí | vấn đề nguồn | quyết định |
|---|---|---|---|
| nghiêm trọng | tr. 5–10 | Reward và tỷ số cùng dùng $r_t$; REINFORCE thiếu $\gamma^t$ dưới mục tiêu $J=\mathbb E[G_0]$. | Dùng $R_{t+1}$ và $w_t$; thêm $\gamma^t$. |
| nghiêm trọng | tr. 11–12 | Baseline và actor–critic được nối quá nhanh, thiếu điều kiện độc lập hành động và đường gradient. | Tách Monte Carlo baseline khỏi bootstrap; thêm `stop-gradient`. |
| nghiêm trọng | tr. 13 | GAE không phân biệt terminal và truncation. | Thêm $m_t$ cho bootstrap, $c_t$ cho đệ quy và ví dụ hai ca. |
| nghiêm trọng | tr. 15–18 | Performance difference, surrogate và ràng buộc TRPO dễ bị đọc như cùng một bảo đảm. | Tách ba bước; hạ kết luận average-KL; thêm damping, FVP, CG và line search. |
| nghiêm trọng | tr. 21–22 | Công thức clip đúng nhưng thiếu phân tích dấu và phía bất lợi. | Viết dạng từng dấu và bốn ca số. |
| nghiêm trọng | tr. 23–25 | Thiếu hợp đồng loss descent, frozen batch và kích thước log-probability đa chiều. | Thêm dấu loss, dừng gradient, shape và tổng theo chiều hành động. |
| trung bình | tr. 29–36 | Một số lựa chọn triển khai được trình bày gần như thành phần chuẩn. | Ghi value clipping là biến thể; chuyển checklist thành trường tái lập. |
| nghiêm trọng | tr. 37–42 | Diễn đạt lý thuyết có thể bị suy rộng thành hội tụ của PPO thực hành. | Chỉ giữ stationary-point result có điều kiện; loại nhận định “mild assumptions”. |
| trung bình | tr. 3, 43 | Danh sách họ policy gradient vượt thời lượng. | Không mở tuyến mới; ghi cho người soạn trong `note-for-author.md`. |

## Kiểm tra số và công thức

- Baseline: với $A\sim\operatorname{Bernoulli}(0{,}25)$, $\mathbb E[4(A-0{,}25)]=0$.
- GAE: $\delta_0=1{,}7$; terminal có $\delta_1=-1$, nên $\widehat A_0=0{,}98$; truncation với $V(S_2)=4$ có $\delta_1=2{,}6$, nên $\widehat A_0=3{,}572$.
- Natural gradient: $F^{-1}g=(0{,}5,1)$, $g^\top F^{-1}g=2$, hệ số chuẩn hóa $0{,}1$, bước $(0{,}05,0{,}1)$.
- PPO-Clip với $\epsilon=0{,}2$: $(\widehat A,w)=(2,1{,}3),(-2,0{,}7),(2,0{,}7),(-2,1{,}3)$ cho $2{,}4,-1{,}6,1{,}4,-2{,}6$.
- Loss tối thiểu hóa dùng $-L^{\mathrm{clip}}+c_VL^V-c_H\mathcal H$.
- Gaussian đa chiều factorized cộng log-probability theo $d_a$ để tạo một tỷ số cho mỗi mẫu.

## Rà mạch và biên tập của tác tử soạn

- Đã dùng nguyên tắc `no-ai-slop`: bỏ lời dẫn rỗng, câu hỏi tu từ, khẩu hiệu, kết luận phô trương và các từ cấm; mỗi trang giữ một luận điểm trung tâm.
- Đã dùng `quill` để rà liên tục thuật ngữ và ký hiệu theo chuỗi REINFORCE → baseline → bootstrap → GAE → surrogate → TRPO → PPO; không tạo `quill.json`.
- Đã tuân thủ quy tắc `codex-slides` ở mức tệp thiết kế cục bộ: dùng template, CSS và thư viện RevealJS hiện có; việc nhập dự án và rà trực quan do điều phối viên thực hiện ở bước kiểm định sau.
- Không sửa `lecture-style.css`, `index.html`, RevealJS hoặc plugin dùng chung.

## Trạng thái trước phản biện độc lập

Bản nháp ban đầu có 38 trang chính và 3 trang bài tập dọc; thư mục hình còn một SVG không dùng; 110 phút cốt lõi, 10 phút bổ sung và 30 phút bài tập. Chưa ghi nhận báo cáo của tác tử kiểm định storyboard hoặc bốn tác tử rà soát độc lập; điều phối viên sẽ bổ sung sau các vòng đó.

## Vòng chỉnh sửa storyboard và công thức

| mức độ | trang chiếu | vấn đề | bằng chứng | quyết định sửa |
|---|---|---|---|---|
| chặn bàn giao | `L10-05`, `L10-06` | Công thức lấy đạo hàm của $\log\pi_{\theta_{\mathrm{old}}}$, trong khi $\theta_{\mathrm{old}}$ là hằng của batch. | Score phải lấy đạo hàm theo biến $\theta$ rồi mới đánh giá tại chính sách cũ. | Đổi thành $\left.\nabla_\theta\log\pi_\theta(A_t\mid S_t)\right|_{\theta=\theta_{\mathrm{old}}}$; rà `L10-03`–`L10-08` và sửa ghi chú. |
| nghiêm trọng | `L10-04` | Ghi chú nói mục tiêu không quyết định hệ số $\gamma^t$, mâu thuẫn với estimator đã chọn. | `L10-04` định nghĩa $J=\mathbb E[G_0]$ và $G_t$ từ thời điểm $t$. | Ghi rõ estimator trong bài mang $\gamma^t$ theo đúng quy ước này; không trộn với mục tiêu khác. |
| nghiêm trọng | `L10-13`–`L10-20` | Trực giác, ví dụ và hình thức TRPO đặt sai thứ tự. | Bản cũ đưa performance-difference trước hình trust-region và thiếu ví dụ old-data nhỏ. | Sắp thành vấn đề → SVG miền tin cậy → ví dụ $w\widehat A$ → performance difference/surrogate/KL → natural gradient → ví dụ Fisher → thuật toán → kiểm nhận bước. Giữ nguyên ID. |
| nghiêm trọng | `L10-16` | Performance-difference chưa định nghĩa rõ occupancy và chưa dẫn nguồn sơ cấp. | Công thức dùng $d^{\pi'}$ nhưng không nêu chuẩn hóa. | Thêm $d^\pi(s)=(1-\gamma)\sum_t\gamma^t\Pr(S_t=s)$ và dẫn Schulman et al. (2015), Eq. 1–7. |
| nghiêm trọng | `L10-21`–`L10-25` | PPO đưa công thức trước trực giác và ví dụ; bốn số xuất hiện như bảng kiểm trước chu trình. | Thứ tự cũ là vấn đề → công thức → hai trang từng dấu → bảng số. | Sắp thành vấn đề → tỷ số quanh một và SVG đoạn phẳng → hai số đại diện → công thức tổng quát/từng dấu → bốn vùng ứng dụng. |
| nghiêm trọng | `X03` | Bài tập lặp bảng bốn số, xuất hiện trước pipeline và không kiểm hợp đồng batch. | Nội dung cũ chỉ kiểm clipping và một shape. | Chuyển sau `L10-35`; đổi thành kiểm toán old log-probability, frozen quantities, log-probability đa chiều, terminal/truncation và KL/clip fraction/entropy. |
| nghiêm trọng | `L10-36`, `L10-37` | So sánh đứng sau lý thuyết và slide lý thuyết có thể bị đọc thành tuyên bố hội tụ thực hành. | Nguồn chỉ tóm tắt, không cho phát biểu định lý đủ điều kiện. | Đặt `L10-36` là so sánh, `L10-37` là giới hạn tuyên bố; không khẳng định practical PPO hội tụ. |
| trung bình | toàn bài và SVG | Ký hiệu tỷ số cũ dễ lẫn với phân bố ban đầu $\rho_0$. | `L10-04` đã dùng $\rho_0$. | Dùng $w_t$ cho tỷ số trong HTML, SVG và planning; giữ $\rho_0$ chỉ cho phân bố ban đầu. |
| trung bình | `L10-07` | `sg` xuất hiện trước khi được định nghĩa trên mặt trang. | Công thức baseline là lần dùng đầu tiên. | Thêm định nghĩa giá trị lượt thuận và đạo hàm bằng không ngay trước công thức. |
| trung bình | planning | Các khoảng thời gian baseline/GAE chồng lặp; phần linh hoạt chưa gắn trang cụ thể. | Storyboard cũ gán `L10-03`–`L10-09` 23 phút và `L10-09`–`L10-12` 12 phút. | Đổi sang bảy khoảng không chồng lặp; gắn 5 phút linh hoạt cho `L10-10` và 5 phút cho `L10-28`, chỉ trong planning. |

Sau vòng sửa, thứ tự kết thúc là `L10-35` → `X03` → `L10-36` (so sánh) → `L10-37` (giới hạn lý thuyết) → `L10-38` (tổng kết). `L10-28` nối thẳng sang `L10-29`; bài tập không còn ngắt giữa công thức PPO và pipeline.

## Kiểm định sau chỉnh sửa

- Có 42 `data-slide-id` duy nhất: 39 trang chính và `X01`–`X03`; thứ tự HTML khớp storyboard.
- Cả 42 trang đều có `<aside class="notes">`.
- KaTeX cục bộ dựng thành công 194 công thức với `throwOnError`; các cặp `$...$`, `$$...$$`, `\left` và `\right` cân bằng.
- Bảy tham chiếu hình trong HTML đều tồn tại. Cả bảy SVG đang dùng trong `img/lec-10/` phân tích XML thành công, có `role="img"`, `title` và `desc`.
- Không có tham chiếu ảnh raster trong HTML. Không còn ký hiệu tỷ số cũ trong HTML hoặc SVG; $\rho_0$ chỉ còn là phân bố trạng thái đầu.
- Không sửa `index.html` hoặc `lecture-style.css`. Rà trực quan bằng Codex Slides vẫn thuộc bước kiểm định cuối của điều phối viên.

## Vòng sửa cuối NEW-01–NEW-03

| mức độ | trang chiếu | vấn đề | quyết định sửa |
|---|---|---|---|
| nghiêm trọng | `L10-22`, `L10-24`, `L10-29`, `L10-30` | Ghi chú cũ nói mọi epoch bắt đầu với $w=1$, làm lẫn dữ liệu old được giữ cố định với tỷ số phải tính lại. | Chỉ khẳng định $w=1$ trước minibatch đầu khi $\theta=\theta_{\mathrm{old}}$. Trong các minibatch sau, giữ log-probability cũ nhưng tính lại log-probability mới và $w$ theo $\theta$ hiện tại. |
| nghiêm trọng | `L10-10`–`L10-12`, `L10-26`–`L10-30`, `X03` | $T$ vừa chỉ thời điểm episode kết thúc vừa chỉ độ dài rollout, gây mâu thuẫn ở terminal/truncation và shape. | Dành $T$ cho thời điểm episode kết thúc; dùng $H$ cho độ dài rollout, $N$ cho số môi trường, $B=HN$ và shape $[H,N,\cdot]$. Đồng bộ HTML, storyboard, outline, ghi chú và `ppo-data-pipeline.svg`. |
| nhẹ | tài sản SVG | `ratio-surrogate.svg` không còn được HTML tham chiếu sau khi `L10-15` chuyển thành ví dụ số. | Xóa SVG không dùng bằng `apply_patch`; danh mục còn đúng bảy SVG, trùng với bảy tham chiếu HTML. |

Sau NEW-01–NEW-03, kiểm tra lại đạt: 41 ID duy nhất, 41 ghi chú, thứ tự HTML khớp storyboard, 169 công thức KaTeX dựng thành công, 7/7 đường dẫn hình hợp lệ và 7/7 SVG phân tích XML thành công.

## Hợp nhất bốn phản biện độc lập

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | `L10-04`–`L10-05`, `L10-16`, `L10-24` | Hợp đồng chiết khấu trộn $J=\mathbb E[G_0]$, occupancy chiết khấu và trung bình đều PPO. | REINFORCE dùng $\gamma^tG_t$, còn surrogate PPO được giảm đều trên rollout. | Định nghĩa riêng kỳ vọng lý thuyết và thực hành. | Giữ $J=\mathbb E[G_0]$ và $\gamma^t$; thêm $\mathbb E_{\mathrm{disc},\pi}$ ở TRPO và $\mathbb E_B$ ở PPO; ghi rõ PPO là surrogate thực hành, không đồng nhất chính xác với objective chiết khấu. |
| nghiêm trọng | `L10-10`–`L10-12`, `L10-27`–`L10-30` | Lợi thế actor đã chuẩn hóa có thể bị dùng nhầm làm target critic. | Bản trước chỉ có một ký hiệu lợi thế và target không có công thức nguồn dữ liệu. | Tách lợi thế thô, lợi thế actor và target critic. | Định nghĩa $\widehat A^{\mathrm{raw}}$, $\widehat A^{\mathrm{actor}}=\operatorname{sg}((A^{\mathrm{raw}}-\mu_B)/(\sigma_B+\varepsilon_A))$ và $\widehat V=\operatorname{sg}(V_{\mathrm{old}}+A^{\mathrm{raw}})$; target giữ thô. |
| nghiêm trọng | `L10-27`, `L10-30` | Đường gradient actor/critic và vai trò $V_{\mathrm{old}}$ chưa đủ rõ. | Target và lợi thế được gọi “đóng băng” nhưng chưa chỉ đại lượng nào nhận gradient. | Viết schema lưu/suy ra/tính lại và đường gradient. | Actor advantage và target đều detach; critic gradient đi qua $V_\phi$ hiện tại; $V_{\mathrm{old}}$ tạo TD, target và tùy chọn value clipping. |
| nghiêm trọng | `L10-08` | Bootstrap bị dùng như ranh giới phổ quát của actor–critic. | Critic học bằng đích Monte Carlo vẫn có thể là critic của actor–critic. | Trình bày hai biến thể và nêu quy ước khóa học. | Đổi thành actor–critic Monte Carlo so với TD/GAE; “nhánh bootstrap” chỉ là quy ước cục bộ của bài. |
| nghiêm trọng | `L10-07`, `X01` | Chứng minh baseline chỉ có ví dụ Bernoulli. | Ví dụ $b=4$ chưa cho thấy $b(s)\nabla\sum_a\pi(a\mid s)=0$. | Thêm chứng minh một dòng và điều kiện liên tục. | Thêm tổng rời rạc; ghi tích phân liên tục cần support cố định và phép đổi đạo hàm–tích phân hợp lệ; giữ ví dụ $b=4$. |
| nghiêm trọng | `L10-37`, `L10-37B` | Một trang giới hạn tuyên bố chưa đủ trình bày mô hình và kết quả lý thuyết. | Nguồn tách vòng ngoài–vòng trong và kết quả stationary-point. | Dùng ít nhất hai trang chính. | `L10-37` trình bày outer/inner cùng PPO-Clip/Penalty; thêm `L10-37B` cho giả thiết hữu hạn, trơn, reward bị chặn, truncated-advantage bias, step sizes và kết luận neighborhood/zero-bias. |
| nghiêm trọng | `L10-31`, `X03` | Chẩn đoán chỉ có diễn giải định tính và bài tập thiếu số. | clip fraction, approximate KL và explained variance chưa định nghĩa phép giảm. | Thêm công thức, chiều KL, caveat và dữ kiện số. | Dùng $\mathbb E_B[\mathbf1\{|w-1|&gt;\epsilon\}]$, $\mathbb E_B[(w-1)-\log w]$ theo chiều old đến new, EV có điều kiện phương sai target dương; `X03` tính $w=e^{0.2}$. |
| trung bình | `L10-16` | Identity, approximation và empirical constraint dễ bị đọc như một dòng tương đương. | Ba bước dùng occupancy khác nhau và ràng buộc khác nhau. | Gắn nhãn và nêu giả thiết. | Tiêu đề và bố cục theo đúng identity → old-distribution approximation → empirical average-KL; ghi cùng $\rho_0$, $\gamma&lt;1$ và absorbing zero-reward; dẫn TRPO sơ cấp. |
| trung bình | `L10-15`, `L10-22` | Tỷ số chưa nêu điều kiện hỗ trợ và dễ bị hiểu là khoảng cách toàn chính sách. | $w$ chỉ dùng mass/density tại hành động mẫu. | Nêu absolute continuity và sửa tiêu đề. | Phân biệt khối xác suất/mật độ, yêu cầu hỗ trợ của policy mới nằm trong policy cũ trên dữ liệu; đổi tiêu đề `L10-22`. |
| trung bình | `L10-17`–`L10-19` | Fisher và solver thiếu định nghĩa, tiêu chí dừng và chi phí. | Chỉ nêu hướng natural gradient. | Thêm Hessian KL, score outer product, hệ damped, residual/max iterations và FVP cost. | Đã bổ sung toàn bộ; ví dụ `L10-18` là trường hợp $\eta=0$ của hệ damped. |
| trung bình | `L10-11`–`L10-12`, `X01`, `X03` | Mọi time limit bị xem là truncation được bootstrap. | Chân trời thuộc MDP có thể là terminal, khác giới hạn ngoại sinh. | Ràng buộc $m=1$ vào truncation ngoại sinh có final observation. | Đã sửa bảng, ví dụ và đáp án; chân trời thuộc trạng thái dùng terminal semantics. |
| trung bình | `L10-25` | Bảng chỉ có vùng ngoài clipping. | Người học chưa thấy trong dải dùng surrogate gốc. | Thêm hàng trong dải và đổi tiêu đề. | Đổi thành “Trong và ngoài dải clipping”, thêm hành vi $1-\epsilon\le w\le1+\epsilon$. |
| trung bình | `L10-01`–`L10-02`, `L10-08`, `L10-19` | Viết tắt xuất hiện trước dạng đầy đủ. | TRPO, PPO, GAE, KL, TD, FVP, CG xuất hiện sớm. | Viết đầy đủ ở lần dùng đầu. | Đã mở rộng tên trên title/goal/algorithm slides; các lần sau giữ viết tắt. |
| trung bình | `actor-critic-advantage.svg` | Hình critic không chỉ rõ hai giá trị đầu vào. | Chỉ có nhãn critic tổng quát. | Thêm $V(S_t)$ và $V(S_{t+1})$, tăng chữ. | SVG đã được vẽ lại cục bộ với hai giá trị và luồng raw-to-actor. |
| trung bình | planning, `note-for-author.md` | Chưa có mốc ba tiết và tuyến cắt khi chậm. | Tổng 150 phút nhưng không có điểm dừng phút 50/100. | Ghi breakpoints và cut route ngoài slide. | Tiết 1 dừng `L10-16`, tiết 2 dừng `L10-32`; tuyến cắt nén `L10-33`–`L10-34`, `L10-36`; không đưa metadata này lên slide/notes. |

Sau hợp nhất, bài có 39 trang chính và 3 bài tập dọc. Thời lượng vẫn là 110 phút cốt lõi, 10 phút linh hoạt và 30 phút bài tập.

Kiểm định cuối sau hợp nhất: 42 ID duy nhất; 42/42 trang có ghi chú; HTML khớp toàn bộ ID trong storyboard; 194 công thức dựng thành công bằng KaTeX cục bộ với `throwOnError`; 7/7 tham chiếu hình tồn tại; 7/7 SVG hợp lệ, có `role="img"`, `title`, `desc`; không có ảnh raster. Rà `quill` xác nhận mạch baseline → raw advantage → actor/critic split → TRPO → PPO → diagnostics → theory; rà `no-ai-slop` loại lời dẫn rỗng và không thêm tuyên bố ngoài nguồn.

## Bốn vấn đề trung bình cuối

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | `L10-17`–`L10-19` | Ký hiệu $F$ trộn Fisher kỳ vọng với ước lượng từ hành động đã lấy mẫu; điều kiện CG chưa đủ. | Hessian average-KL lấy kỳ vọng hành động dưới $\pi_{\mathrm{old}}$, còn $B^{-1}\sum u_tu_t^\top$ chỉ là Monte Carlo; CG cần toán tử SPD. | Tách $F$ và $\widehat F$; nêu damping và điều kiện solver. | Đã định nghĩa $F=\mathbb E_{S\sim B,A\sim\pi_{\mathrm{old}}}[uu^\top]$ bằng Hessian average-KL, $\widehat F=B^{-1}\sum u_tu_t^\top\approx F$; CG giải $\widehat F+\eta I$, thường dùng $\eta>0$, còn $\eta=0$ phải giả sử SPD; giữ residual, số vòng tối đa và chi phí FVP/line search. |
| trung bình | `L10-28`–`L10-30`, `X03`, `ppo-data-pipeline.svg` | Schema thiếu shape hành động rời rạc và dữ liệu bootstrap ở biên rollout. | Auto-reset có thể thay quan sát cuối bằng quan sát reset, làm bootstrap sang episode kế tiếp. | Thêm $[H,N]\to[B]$, `final_observation`/$V_{\mathrm{boot}}$ và câu kiểm biên cuối. | Đã thêm shape rời rạc; lưu $S_{\mathrm{next}}$ hoặc final observation trước reset, hoặc $V_{\mathrm{boot}}=V_{\mathrm{old}}(S_H)\in\mathbb R^N$; cấm dùng reset observation; `X03` kiểm riêng terminal và truncation nhân tạo. |
| trung bình | `L10-31`, `X03`, `ppo-diagnostics.svg` | Clipfrac bị gọi là tỷ lệ mẫu ở đoạn phẳng. | Công thức chỉ kiểm $|w-1|>\epsilon$; objective có phẳng hay không còn phụ thuộc dấu lợi thế. | Giữ công thức, đổi nhãn và giải thích. | SVG và ghi chú nay gọi đây là tỷ lệ tỷ số ngoài dải clip; `X03` yêu cầu phân biệt với flat-region fraction. |
| trung bình | `L10-37B` | Phát biểu lý thuyết rộng hơn kết quả sơ cấp và nguồn chưa đủ chính xác. | Định lý 3.1 chỉ cho $\liminf_n\|\nabla V(\theta_{n,1})\|^2\le8L\sqrt{|\mathcal A|}\limsup_n\phi_n$ hầu chắc chắn trong mô hình phân tích. | Thay bằng phát biểu đã kiểm và dẫn theorem/assumptions cụ thể. | Đã dùng đúng công thức, nêu $\phi_n$ là sai lệch ước lượng, không suy ra hội tụ toàn dãy, tối ưu toàn cục hoặc PPO thực hành; dẫn Ruinan Jin, Shuai Li, Baoxiang Wang, <em>On Stationary Point Convergence of PPO-Clip</em>, ICLR 2024, Định lý 3.1 và Giả thiết 3.1, 3.2, 3.4, https://proceedings.iclr.cc/paper_files/paper/2024/file/30e15e5941ae0cdab7ef58cc8d59a4ca-Paper-Conference.pdf. |

Kiểm định sau bốn sửa đổi: 42 ID duy nhất, 42/42 ghi chú, tập ID HTML khớp storyboard; 194 công thức dựng bằng KaTeX cục bộ với `throwOnError`; 7/7 tham chiếu SVG tồn tại và 7/7 tệp phân tích XML, có `role="img"`, `title`, `desc`. `index.html` và `lecture-style.css` không đổi. Rà Quill giữ mạch Fisher lý tưởng → ước lượng Monte Carlo → solver → pipeline biên rollout → chẩn đoán → định lý; rà no-ai-slop loại các nhãn gây suy diễn quá mức.

## Tái kiểm định và kiểm định cuối của điều phối viên

- Tác tử toán học–thuật toán đã tái kiểm định bản sửa cuối và kết luận `PASS`: không còn vấn đề từ mức `trung bình` trở lên.
- Tác tử storyboard đã rà trang mới `L10-37B`, hai trang lân cận và toàn bộ cụm bị ảnh hưởng; kết luận `PASS`.
- Điều phối viên đối chiếu Định lý 3.1 với bài sơ cấp của Jin, Li và Wang tại ICLR 2024; công thức và phạm vi phát biểu trên `L10-37B` khớp nguồn.
- HTML có 42 mã duy nhất, 42 ghi chú và độ sâu `section` tối đa là hai; storyboard chứa đủ 42 mã theo đúng thứ tự.
- KaTeX cục bộ dựng nghiêm ngặt 194 biểu thức, không có lỗi. Bảy SVG hợp lệ theo XML, có `role="img"`, `title`, `desc` và đều được HTML sử dụng.
- Tệp HTML và bảy SVG đều trả HTTP 200 tại cổng 8765. Không có ảnh raster, liên kết planning trong HTML, phụ thuộc mạng cốt lõi hoặc lỗi từ `git diff --check`.
- Bản HTML và bốn tệp quy trình đã được đưa vào Design Files của dự án Codex Slides và đối chiếu từng byte với tệp trong kho.
- Codex Slides Browser không khả dụng trong phiên này. Vì vậy chưa thể tuyên bố đã rà trực quan bằng Codex Slides; giới hạn còn lại là kiểm tra tràn, chồng lấn và khả năng đọc bằng trình duyệt đồ họa ở khung 16:9 và màn hình hẹp.
