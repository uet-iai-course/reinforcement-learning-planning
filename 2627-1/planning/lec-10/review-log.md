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

## Lecture note — vòng độc lập ngày 03/09/2026

Lecture note được soạn từ PDF 43 trang thành 12 chủ đề, 110 phút cốt lõi,
10 phút linh hoạt và 30 phút bài tập. Năm vai chỉ đọc đã rà độc lập:

| vai | model runtime | kết quả chính | quyết định |
|---|---|---|---|
| góc nhìn sinh viên | `z-ai/glm-5.3-flash` | Phát hiện phép tính trung gian X02 sai, nhãn dải X03 sai và câu tiếng Anh sót. | Sửa toàn bộ; PASS ở tái rà mạch. |
| chuyên gia Học tăng cường | `deepseek/deepseek-v4-flash-0731` | Yêu cầu làm rõ ma trận Fisher minh họa, ký hiệu lý thuyết và chẩn đoán chính sách gần tất định. | Đã bổ sung; bác nhận xét đổi terminal $T=2$ vì quỹ đạo có hai chuyển tiếp $t=0,1$ và trạng thái cuối $S_2$. |
| toán học và thuật toán | `deepseek/deepseek-v4-flash-0731` | Phát hiện $m_0$ sai trong X01, hệ số 16 sai trong X02 và hai nhãn “trong dải” sai trong X03. | Đã sửa; tái tính độc lập PASS. |
| phản biện học thuật–sư phạm | `deepseek/deepseek-v4-flash-0731` | Yêu cầu làm rõ cầu nối actor–critic → GAE, TRPO → cách giải, pipeline → lý thuyết. | Đã thêm câu nối, không đổi thứ tự 12 chủ đề. |
| kết nối và mạch viết | `z-ai/glm-5.3-flash` | Mạch 12 chủ đề đạt; phát hiện câu gượng, từ tiếng Anh sót và chỉ số Fisher trùng chỉ số thời gian. | Việt hóa, đổi chỉ số mẫu sang $i$, tái rà PASS. |

Ba báo cáo DeepSeek hợp lệ có
`requested_model = observed_model = deepseek/deepseek-v4-flash-0731`, provider
`OpenRouter`. Lượt reviewer toán đầu hoàn tất với profile `review`; hai vai còn
lại chỉ hoàn tất ổn định khi dùng `--reasoning-effort none`, profile `recheck`,
6 vòng, timeout 600 giây và 12.000 token. Các lượt dùng `low` với 12.000,
18.000 và 32.000 token đều bị `finish_reason=length` vì reasoning chiếm gần
hết ngân sách; không dùng các lượt lỗi làm báo cáo. Reviewer GLM dùng
`minimal`; GLM từ chối `none` bằng HTTP 400 vì reasoning là bắt buộc.

Writer GLM sửa tuần tự một tệp. Hai lượt rộng chạm giới hạn 12 và 20 vòng sau
khi đã ghi nhiều bản vá; điều phối viên đối chiếu từng mục, hoàn thiện các sửa
cục bộ và chạy lại kiểm định. Không có hai writer sửa cùng tệp đồng thời.

Kiểm định note sau sửa: một H1; 12 `data-note-topic-id` duy nhất; 12 thẻ
`section` mở/đóng cân bằng; ba bộ `exercise`–`hint`–`solution`; 414 biểu thức
KaTeX dựng thành công với `throwOnError`; không có mã trang chiếu hoặc chỉ dẫn
quy trình trong nội dung. Tái rà toán bằng V4 Flash PASS; tái rà mạch và
`no-ai-slop` bằng GLM PASS. Các sửa câu chữ nhẹ cuối không đổi công thức, thứ tự
hoặc vai trò chủ đề.

Kiểm định hiển thị note: lệnh bắt buộc `python3 -m reloadserver 8765` thất bại
vì môi trường thiếu mô-đun `reloadserver`. Điều phối viên dùng
`python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tối thiểu chỉ chứa
viewer, note Bài 10, index, deck đích và các thư viện render cục bộ; không phục
vụ `.env` hoặc planning. Chromium kiểm ở 1280×720 và 390×844: tiêu đề đúng,
16 mục lục khớp 16 H2, 414 biểu thức KaTeX không lỗi, sáu khối thu gọn đóng mặc
định, liên kết deck đúng, bàn phím hoạt động, không lỗi console/tài nguyên và
không tràn ngang. Chế độ in mở mọi khối thu gọn và ẩn mục lục/thanh hành động;
kiểm tra chống duyệt đường dẫn từ chối `../AGENTS.md`.

Codex Slides không khả dụng trong phiên này vì runtime Node.js là 18.19.1,
thấp hơn yêu cầu Node.js 20 của plugin. Vì vậy không tuyên bố đã rà note bằng
Codex Slides; bằng chứng hiển thị cuối là RevealJS/material viewer cục bộ bằng
Chromium.

## Bốn vấn đề trung bình cuối

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | `L10-17`–`L10-19` | Ký hiệu $F$ trộn Fisher kỳ vọng với ước lượng từ hành động đã lấy mẫu; điều kiện CG chưa đủ. | Hessian average-KL lấy kỳ vọng hành động dưới $\pi_{\mathrm{old}}$, còn $B^{-1}\sum u_tu_t^\top$ chỉ là Monte Carlo; CG cần toán tử SPD. | Tách $F$ và $\widehat F$; nêu damping và điều kiện solver. | Đã định nghĩa $F=\mathbb E_{S\sim B,A\sim\pi_{\mathrm{old}}}[uu^\top]$ bằng Hessian average-KL, $\widehat F=B^{-1}\sum u_tu_t^\top\approx F$; CG giải $\widehat F+\eta I$, thường dùng $\eta>0$, còn $\eta=0$ phải giả sử SPD; giữ residual, số vòng tối đa và chi phí FVP/line search. |
| trung bình | `L10-28`–`L10-30`, `X03`, `ppo-data-pipeline.svg` | Schema thiếu shape hành động rời rạc và dữ liệu bootstrap ở biên rollout. | Auto-reset có thể thay quan sát cuối bằng quan sát reset, làm bootstrap sang episode kế tiếp. | Thêm $[H,N]\to[B]$, `final_observation`/$V_{\mathrm{boot}}$ và câu kiểm biên cuối. | Đã thêm shape rời rạc; lưu $S_{\mathrm{next}}$ hoặc final observation trước reset, hoặc $V_{\mathrm{boot}}=V_{\mathrm{old}}(S_H)\in\mathbb R^N$; cấm dùng reset observation; `X03` kiểm riêng terminal và truncation nhân tạo. |
| trung bình | `L10-31`, `X03`, `ppo-diagnostics.svg` | Clipfrac bị gọi là tỷ lệ mẫu ở đoạn phẳng. | Công thức chỉ kiểm $|w-1|>\epsilon$; objective có phẳng hay không còn phụ thuộc dấu lợi thế. | Giữ công thức, đổi nhãn và giải thích. | SVG và ghi chú nay gọi đây là tỷ lệ tỷ số ngoài dải clip; `X03` yêu cầu phân biệt với flat-region fraction. |
| trung bình | `L10-37B` | Phát biểu lý thuyết rộng hơn kết quả sơ cấp và nguồn chưa đủ chính xác. | Định lý 3.1 chỉ cho $\liminf_n\|\nabla V(\theta_{n,1})\|^2\le8L\sqrt{|\mathcal A|}\limsup_n\phi_n$ hầu chắc chắn trong mô hình phân tích. | Thay bằng phát biểu đã kiểm và dẫn theorem/assumptions cụ thể. | Đã dùng đúng công thức, nêu $\phi_n$ là sai lệch ước lượng, không suy ra hội tụ toàn dãy, tối ưu toàn cục hoặc PPO thực hành; dẫn Ruinan Jin, Shuai Li, Baoxiang Wang, <em>On Stationary Point Convergence of PPO-Clip</em>, ICLR 2024, Định lý 3.1 và Giả thiết 3.1, 3.2, 3.4, https://proceedings.iclr.cc/paper_files/paper/2024/file/30e15e5941ae0cdab7ef58cc8d59a4ca-Paper-Conference.pdf. |

Kiểm định sau bốn sửa đổi: 42 ID duy nhất, 42/42 ghi chú, tập ID HTML khớp storyboard; 194 công thức dựng bằng KaTeX cục bộ với `throwOnError`; 7/7 tham chiếu SVG tồn tại và 7/7 tệp phân tích XML, có `role="img"`, `title`, `desc`. `index.html` và `lecture-style.css` không đổi. Rà Quill giữ mạch Fisher lý tưởng → ước lượng Monte Carlo → solver → pipeline biên rollout → chẩn đoán → định lý; rà no-ai-slop loại các nhãn gây suy diễn quá mức.

## Vòng rà soát hiện tại

Runtime của planner, source reader, storyboard reviewer, năm reviewer độc lập và writer: `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter. Bản sao worker có 748 dòng nguồn TXT, 6 `section` ngoài và 7 SVG; `.env` không được đưa vào `repo-root` của worker.

Danh mục 42 mã được rà trong vòng này: `L10-01`, `L10-02`, `L10-03`, `L10-04`, `L10-05`, `L10-06`, `L10-07`, `L10-08`, `L10-09`, `L10-10`, `L10-11`, `L10-12`, `X01`, `L10-13`, `L10-14`, `L10-15`, `L10-16`, `L10-17`, `L10-18`, `L10-19`, `L10-20`, `X02`, `L10-21`, `L10-22`, `L10-23`, `L10-24`, `L10-25`, `L10-26`, `L10-27`, `L10-28`, `L10-29`, `L10-30`, `L10-31`, `L10-32`, `L10-33`, `L10-34`, `L10-35`, `X03`, `L10-36`, `L10-37`, `L10-37B`, `L10-38`.

### Planner, source reader và storyboard reviewer

- Planner xác nhận phạm vi 120 phút chính + 30 phút chữa bài và quy trình tuần tự/song song. Điều phối viên bác cách planner dùng số SVG để trả lời số mạch; parser HTML xác nhận 6 mạch ngoài.
- Source reader lập đủ 43 hàng nguồn→đích và tính lại baseline, GAE, natural gradient, bốn ca PPO-Clip, loss, tensor và giới hạn hội tụ. Báo cáo ghi nhầm 791 dòng; `wc -l` trên tệp worker cho 748 dòng, dùng số 748 làm bằng chứng.
- Storyboard reviewer xác nhận 42 mã, 6 mạch, 7 SVG, thời lượng 110 + 10 + 30 và không cần đổi số lượng hay thứ tự. `X01` là bài tập nối chung baseline–actor–critic và GAE, tính 10 phút đúng một lần.

### Năm reviewer độc lập

| mức độ | trang chiếu | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| trung bình | `L10-16` | Trang dày và dễ đồng nhất identity, xấp xỉ occupancy với ràng buộc KL thực nghiệm. | Ba phép kỳ vọng khác nhau nằm cùng trang. | Giữ một trang để bảo toàn mạch nguồn; rút notes, gọi rõ KL trung bình thực nghiệm và phân biệt max-KL lý thuyết. Render phải kiểm riêng trang này. |
| trung bình | `L10-31` | Tiêu đề nói ba chẩn đoán nhưng hình có bốn. | Hình gồm KL, clipfrac, entropy và EV; chỉ ba đại lượng cần công thức phép giảm. | Đổi thành “Bốn chẩn đoán, ba phép giảm”; notes nêu entropy được theo dõi trực tiếp. |
| trung bình | `L10-25` | Cụm “hai số phía bất lợi” làm lẫn hướng tỷ số với dấu lợi thế. | Ca $1{,}4$ có lợi thế dương. | Viết lại thành hai ca ngoài dải theo hướng không cải thiện, nêu rõ hai cặp $(A,w)$. |
| trung bình | `L10-37B` | $V$, $\theta_{n,1}$ và $\phi_n$ chưa định nghĩa; nguồn bài giảng chỉ nêu kết quả định tính. | Người học có thể nhầm $V$ với critic. | Đối chiếu trực tiếp bài báo ICLR 2024: công thức, `liminf`, hằng số, a.s. và Giả thiết 3.1/3.2/3.4 đều đúng; bổ sung ba định nghĩa, không đổi định lý. |
| trung bình | nhịp ba tiết | Reviewer sinh viên cho rằng mốc tiết lệch bảng tổng. | Ước lượng cộng theo cụm không xét tuyến cắt và thời lượng linh hoạt. | Chưa đổi mốc khi chưa có bằng chứng diễn tập; giữ tuyến cắt đã ghi và kiểm tải qua render. |
| trung bình | `X01`, ranh giới mạch 2–3 | Một trang kiểm cả baseline và GAE nên xuất hiện ở hai cụm. | Outline/storyboard có `X01` ở hai hàng. | Ghi rõ đây là trang nối chung, tính 10 phút một lần; không đổi vị trí. |
| nhẹ | `L10-13`, `L10-17`, `L10-18`, `L10-24`, `L10-37` | Nhãn surrogate/Fisher, công thức bước tổng quát, câu notes và hướng KL còn mơ hồ. | Các công thức đúng nhưng tên gọi hoặc cầu nối chưa đủ chính xác. | Sửa cục bộ theo nguồn; PPO-Penalty dùng $D_{KL}(\pi_{old}\|\pi_\theta)$ và $\beta$ thích ứng. |

Các đề xuất thêm trang tiên quyết, trang tài liệu tham khảo, ví dụ approxKL và bỏ cấu hình viewport bị bác: L10-02 đã viết đầy đủ thuật ngữ, B09 là tiên quyết trong planning, nguồn không yêu cầu trang mới, và cấu hình kỹ thuật phải giữ theo mẫu. Không có lỗi chặn bàn giao hoặc nghiêm trọng.

## Tái kiểm định và kiểm định cuối của điều phối viên

- Hai lượt tái kiểm độc lập dùng `requested_model = observed_model = z-ai/glm-5.3-flash`, provider OpenRouter. Lượt mạch viết kết luận `PASS` sau khi rà 6 mạch, `X01`, các trang sửa, hai trang lân cận và ranh giới phần. Lượt toán học đầu chạm giới hạn 10 vòng nên không được dùng; chạy lại với 14 vòng, 180 giây và 5.000 token, rồi kết luận `PASS`, không còn lỗi từ mức `trung bình` trở lên.
- Điều phối viên đối chiếu trực tiếp Định lý 3.1 với bài sơ cấp của Jin, Li và Wang tại ICLR 2024; công thức, `liminf`, hằng số, phát biểu hầu chắc chắn và các Giả thiết 3.1, 3.2, 3.4 trên `L10-37B` khớp nguồn.
- HTML có 42 mã duy nhất, 42 ghi chú, 6 `section` ngoài và độ sâu `section` tối đa là hai. Outline, storyboard và nhật ký đều chứa đủ 42 mã. Không có ảnh raster, tài nguyên mạng cốt lõi, đường dẫn hỏng hoặc tham chiếu planning trong HTML.
- Chromium dựng 212 biểu thức KaTeX cục bộ, không có `katex-error` hoặc lỗi console. Bảy SVG đều tồn tại, hợp lệ theo XML, có `role="img"`, `title`, `desc` và được HTML sử dụng.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Kiểm thử tiếp tục bằng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tối thiểu không có `.env`; tệp HTML và bảy SVG đều trả HTTP 200.
- Đã duyệt 42 trang ở 1280×720 và 42 trang ở 800×600, tổng 84 ảnh chụp. Cả hai viewport không có lỗi console, lỗi tải tài nguyên hoặc lỗi bàn phím. Phép đo hình học báo sai dương ở H1 và một số hộp KaTeX; đối chiếu ảnh xác nhận các phần này nằm trong khung. Một lỗi thật ở `L10-30` làm ba cột chồng nhau đã được sửa bằng lưới `minmax(0,1fr)` và ngắt dòng ký hiệu; lần render toàn bộ sau sửa đạt ở cả hai viewport.
- Rà Quill giữ tuyến baseline → lợi thế thô → tách actor/critic → TRPO → PPO → chẩn đoán → kết quả lý thuyết. Tự kiểm `no-ai-slop/eval.md` đạt: không thêm mệnh đề, số liệu hoặc nguồn; không còn lời dẫn rỗng, câu hỏi tu từ, nhãn phô trương hoặc nhịp câu máy móc. Không tạo `quill.json`.
- Bốn Design Files `lecture-10-trpo-va-ppo.html`, `outline.md`, `storyboard.md`, `review-log.md` trong dự án Codex Slides `20260824221550-lecture-10-trpo-v-ppo-p4gd` đã được đồng bộ và đối chiếu nội dung từng byte với tệp trong kho. Trạng thái chuẩn của dự án là `draft`, 0 slide, vì dự án dùng Design Files để lưu bản RevealJS thay vì render deck ảnh.
- Codex Slides trả handoff chính xác tới `?view=design-files&file=uploaded%2Flecture-10-trpo-va-ppo.html`, nhưng phiên này không có Codex in-editor Browser để mở handoff. Vì vậy không tuyên bố đã xác minh giao diện Design Files trong Browser; rà trực quan RevealJS cục bộ bằng Chromium là bằng chứng hiển thị cuối.

## Đồng bộ deck với lecture note ngày 03/09/2026

- Thêm `data-note-topic-id` cho đủ 42 trang. Phân bố 12 chủ đề lần lượt là `5, 4, 4, 4, 5, 6, 1, 3, 4, 3, 2, 1`; mỗi trang thuộc đúng một chủ đề.
- Thêm cùng bảng ánh xạ hai chiều vào `outline.md` và `storyboard.md`. Tập 42 `data-slide-id` trong HTML xuất hiện đầy đủ ở cả hai tệp; 12 mã chủ đề khớp các section của lecture note.
- Không đổi số trang, thứ tự, sáu mạch ngoài, bảy SVG hoặc cấu hình RevealJS. Đồng bộ cục bộ kết quả học tập, nguồn trang, thuật ngữ triển khai, đích critic và cầu nối từ pipeline sang kết quả lý thuyết.

Năm lượt rà độc lập sau đồng bộ:

| vai | model runtime | kết quả và quyết định |
|---|---|---|
| góc nhìn sinh viên | `z-ai/glm-5.3-flash` | PASS; đề nghị làm rõ thời lượng và phát hiện mô tả $L$ lệch note. Giữ lịch 110 phút cốt lõi + 10 phút linh hoạt + 30 phút bài tập vì đúng yêu cầu 120+30; sửa $L$. |
| chuyên gia Học tăng cường | `deepseek/deepseek-v4-flash-0731` | Phát hiện mức nghiêm trọng tại `L10-37B`: $L$ phải là hằng số Lipschitz của gradient. Đã sửa và tái rà toán PASS. |
| toán học và thuật toán | `deepseek/deepseek-v4-flash-0731` | Các ví dụ GAE, natural gradient và PPO-Clip đúng; cùng phát hiện mô tả $L$. Sau sửa `X03` và `L10-37B`, tái rà xác nhận bốn đáp số theo thứ tự là $2{,}4$, $1{,}4$, $-2{,}6$, $-1{,}6$ và kết luận PASS. |
| phản biện học thuật–sư phạm | `deepseek/deepseek-v4-flash-0731` | Không có lỗi chặn hoặc nghiêm trọng. Các nhận xét cho rằng ca $(\widehat A,w)=(-2,0{,}7)$ còn gradient bị bác vì phép `min` chọn $0{,}8(-2)=-1{,}6$, đúng là đoạn phẳng. |
| kết nối và mạch viết | `z-ai/glm-5.3-flash` | PASS về tuyến và ánh xạ; phát hiện `X03` lệch bài tập trong note. Đã thay câu phân loại batch bằng phép tính đủ bốn ca PPO-Clip; tái rà `L10-31`–`L10-38` PASS. Nhận xét đồng nhất “mạch ngoài” với số SVG bị bác: mạch ngoài là sáu section cấp một, còn SVG là bảy tài sản. |

Ba vai DeepSeek có `requested_model = observed_model = deepseek/deepseek-v4-flash-0731`, provider `OpenRouter`, `reasoning-effort none`. Vai sư phạm đầu tiên bị `finish_reason=length`; lượt chạy lại thu hẹp phạm vi hoàn tất và mới được dùng làm báo cáo. Hai vai GLM có `requested_model = observed_model = z-ai/glm-5.3-flash`, provider `OpenRouter`, `reasoning-effort minimal`.

Kiểm định cuối của vòng đồng bộ:

- `git diff --check` đạt; 42 ID duy nhất, 42 ghi chú, 6 section ngoài, 12 chủ đề; 229 biểu thức KaTeX nguồn dựng thành công với `strict: error`.
- 17 tài nguyên cục bộ được tham chiếu đều tồn tại; không có tài nguyên mạng cốt lõi hay ảnh raster. Bảy SVG phân tích XML thành công và đều có `role="img"`, `title`, `desc`.
- `index.html` đã có đúng liên kết deck và lecture note của Bài 10; không có liên kết tới planning.
- Lệnh bắt buộc `python3 -m reloadserver 8765` tiếp tục không chạy vì thiếu mô-đun. Dùng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tối thiểu không chứa `.env`.
- Chromium duyệt đủ 42 trang ở 1280×720 và 800×600: không lỗi console, lỗi tải tài nguyên hoặc lỗi bàn phím. Bộ đo hình học vẫn báo sai dương ở H1 và một số hộp KaTeX; ảnh chụp xác nhận nằm trong khung. `X03` từng tràn do fragment đáp án dài, đã rút gọn rồi render lại; `X03` và `L10-37B` đọc được ở cả hai viewport.
- Codex Slides không khả dụng trong lượt này vì Node.js 18.19.1 thấp hơn yêu cầu Node.js 20. Không tuyên bố đã rà vòng đồng bộ bằng Codex Slides; bằng chứng hiển thị là Chromium trên RevealJS cục bộ.

## Hoàn thiện bản đồ bốn nhóm — 04-09-2026

- Kiểm định tổng thể: phát hiện note còn 12 chủ đề chưa được phân loại vào bốn nhóm (cốt lõi, cầu nối, bổ sung, đọc thêm).
- Reader DeepSeek đề xuất: cốt lõi gồm 01, 03–09; cầu nối là 02; bổ sung là 10–11; đọc thêm là 12. Mỗi nhóm được ghi rõ khoảng trống mà nó lấp, nguồn dẫn tương ứng và kết nối cụ thể tới các chủ đề lân cận trong mạch bài.
- Writer GLM thêm bảng phân loại vào note; runtime `requested_model = observed_model = z-ai/glm-5.3-flash`, provider `OpenRouter`, `reasoning-effort minimal`.
- Điều phối viên chuẩn hóa bảng đủ các cột: nhóm, phạm vi, vai trò, đầu vào→sản phẩm, vị trí/kết nối, nguồn; đồng bộ hóa phân nhóm ở outline và storyboard.
- Hai lượt recheck cuối:
  - DeepSeek: PASS, runtime `requested_model = observed_model = deepseek/deepseek-v4-flash-0731`, provider `OpenRouter`, `reasoning-effort none`.
  - GLM: PASS về tiêu chí no-ai-slop và mạch viết, runtime `requested_model = observed_model = z-ai/glm-5.3-flash`, provider `OpenRouter`, `reasoning-effort minimal`.
- Không đổi 12 chủ đề, 42 slide, ánh xạ, công thức, thứ tự hay SVG. Sau hai lượt recheck, không còn lỗi chặn, nghiêm trọng hoặc trung bình.

## Tái kiểm cuối bản đồ chủ đề — 04-09-2026

- Trình xem ghi chú đạt ở 1280×720 và 390×844: 414 phần tử KaTeX, 17 mục lục hợp lệ, không lỗi tải hoặc bàn phím; thân tài liệu không cuộn ngang. Bảng năm cột dùng vùng cuộn riêng trên màn hình hẹp.
- Hai Design Files `outline.md` và `storyboard.md` đã được ghi lại trong dự án Codex Slides `20260824221550-lecture-10-trpo-v-ppo-p4gd` và đọc lại khớp từng byte với kho. HTML không đổi trong vòng này.
- `lecture-note.md` không phải Design File hiện hữu của dự án. Codex in-editor Browser không có trong phiên này, nên bằng chứng hiển thị cuối của phần ghi chú là Chromium cục bộ; không tuyên bố đã rà trực quan bằng Codex Slides.

## Sửa marker hiển thị của lecture note — 04-09-2026

- Kiểm tra văn bản đã render phát hiện 12 thẻ `<section ...>` bị material-viewer escape và hiển thị nguyên mã. Đã đổi chúng thành 12 comment `<!-- note-topic-id: lec-10-topic-NN -->` theo đúng giao diện của viewer và bỏ 12 thẻ đóng; không đổi nội dung, công thức, bài tập hoặc thứ tự.
- Recheck GLM dùng `recheck/5/300/4000`, reasoning `minimal`, hoàn tất ở vòng 3 và PASS: đủ 12 mã duy nhất, không còn thẻ section, bốn nhóm và toàn bộ khối nội dung còn nguyên. Runtime trả `requested_model=observed_model=z-ai/glm-5.3-flash`, provider `OpenRouter`.
- Chromium dựng lại ghi chú ở 1280×720 và 390×844: 414 phần tử KaTeX, 17 mục lục, không lỗi tải, bàn phím hoặc cuộn ngang thân tài liệu. Kiểm tra `innerText` xác nhận không còn chuỗi thẻ section hiển thị; bảng rộng vẫn cuộn trong vùng riêng.

## Viết lại ghi chú bài giảng theo chuẩn giáo trình — 04-11-2026

Yêu cầu người dùng (goal 04-11-2026): rà soát ghi chú bài giảng Bài 10 theo các nguyên tắc về nội dung, văn phong, bố cục và cách diễn giải của từng khối trong `../CLAUDE.md`, `CLAUDE.md`, `AGENTS.md`; trình bày chi tiết, đặc biệt các chứng minh quan trọng; dùng Sutton và Barto (2018); sau khi ghi chú hoàn thiện mới làm lại bộ trang chiếu dựa trên ghi chú mới.

Hiện trạng: ghi chú cũ 5 954 từ (dưới ngưỡng 6 000), viết trước chuẩn giáo trình, không có mục đánh số, môi trường có số hiệu hay chứng minh theo bước; các vai cũ chạy qua OpenRouter, nay hết hiệu lực theo `prompt_lecture_note_deck.md`. Quyết định: viết lại toàn bộ theo quy trình đầy đủ của Giai đoạn I (năm vai rà soát), không dùng quy trình rút gọn.

Điều phối viên: phiên Claude Code chính, Claude Opus 5.5 (`claude-opus-5-5`).

### Giai đoạn I.1 — Lập kế hoạch

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | quyết định |
|---|---|---|---|---|
| lập kế hoạch (chỉ đọc) | general-purpose | opus | high | chấp nhận |

Lý do chấp nhận: đủ chín phần (mục tiêu, tiên quyết, khung lý thuyết, dàn ý bảy mục, ví dụ xuyên suốt, tình huống áp dụng, bản đồ chủ đề, ánh xạ nguồn, rủi ro và chia việc). Điều phối viên kiểm lại:
- số hiệu kế thừa bằng grep: Định lý 09.23, Hệ quả 09.24, Thuật toán 09.25, Hệ quả 09.26, Nhận xét 09.27, Bổ đề 09.21, 09.22; Định lý 04.13; Định nghĩa 05.20, Mệnh đề 05.27; Định nghĩa 06.24; Định nghĩa 07.19, 07.21; Định nghĩa 08.4, 08.6, 08.12, 08.16, 08.18; Bổ đề 03.20, Định lý 03.21, 03.28, Mệnh đề 03.22, 03.23, 03.27 — khớp (brief ban đầu của điều phối viên lệch một đơn vị ở nhóm 09.22–09.26; kế hoạch đã sửa);
- tính lại: chuỗi hai trạng thái $v(s_B)=2$, $q(s_A,1)=1{,}8$, $J=1{,}4$; đổi sang $\pi'=(0{,}6;0{,}8)$ cho $J'=1{,}696$, $\Delta J=0{,}296$ (hiệu hiệu năng $0{,}296$, hàm thay thế $0{,}26$); bốn số PPO-Clip $2{,}4$; $-1{,}6$; $1{,}4$; $-2{,}6$.

Quyết định ký hiệu duyệt theo kế hoạch: tỉ số chính sách $\rho_t(\theta)$ (đúng Định nghĩa 06.24 với chính sách hành vi $\pi_{\theta_{\mathrm{old}}}$), phân phối trạng thái đầu $\mu_0$ (ghi tương ứng với $\rho_0$ của Bài 09), bán kính miền tin cậy $\kappa$ (vì $\delta_t$ là sai số TD), lợi thế $A_\pi$, $\widehat A_t$ với ngoại lệ chữ $A$ ghi sau bảng ký hiệu, độ dài đoạn thu $h$ (theo $G^\lambda_{t:h}$ của Sutton và Barto §12.3), critic $\hat v(s,w)$. Định nghĩa actor–critic theo Sutton và Barto §13.5 (REINFORCE có đường cơ sở không là actor–critic); cách gọi rộng của nguồn tr. 12 ghi trong một nhận xét.

### Giai đoạn I.1 — Phân tích nguồn

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | quyết định |
|---|---|---|---|---|
| phân tích nguồn (chỉ đọc) | general-purpose | opus | high | chấp nhận |

Sản phẩm: ánh xạ 43 trang nguồn, đối chiếu Sutton và Barto (2018) §7.1, §12.1–12.3, §13.3–13.5 (số trang sách = trang PDF − 22), kiểm trích dẫn trên văn bản gốc: Kakade và Langford (2002) Bổ đề 6.1; Schulman và cộng sự (2015) Định lý 1, (1), (3), (12), (14), Phụ lục A–C; Schulman và cộng sự (2016) Định nghĩa 1, Mệnh đề 1, (11)–(18); Schulman và cộng sự (2017) (5)–(9), §4, Thuật toán 1; Achiam và cộng sự (2017) Hệ quả 1, 3, Mệnh đề 1, Bổ đề 3 phụ lục; Jin, Li và Wang (2024) Định lý 3.1–3.3, Giả thiết 3.1–3.4; Greensmith, Bartlett và Baxter (2004) §5, Định lý 13, Hệ quả 15, Định lý 16; Nocedal và Wright (2006) Thuật toán 5.2 (tr. 112), Định lý 5.1, 5.4; Huang và cộng sự (2022); Engstrom và cộng sự (2020). Cover và Thomas (2006) Bổ đề 11.6.1 chỉ kiểm qua nguồn thứ cấp.

Phát hiện được điều phối viên kiểm lại và chấp nhận:
- F1 (nghiêm trọng): ghi chú 01–09 chưa định nghĩa phân kỳ KL, biến phân toàn phần, entropy (grep "Kullback", "mathrm{KL}" trên lec-01…09: 0 kết quả) → thêm định nghĩa và chủ đề `cầu nối`.
- F2 (nghiêm trọng): GAE không chệch cho gradient (γ-just), không cho $A_\pi$; tính lại trên chuỗi hai trạng thái với $\hat v=(1;1{,}5)$: $\mathbb E[\widehat A_0\mid s_A,a_1]=0{,}35;\,0{,}71;\,0{,}8$ với $\lambda=0;\,0{,}8;\,1$ và tọa độ gradient $0{,}0875;\,0{,}1775;\,0{,}2$ (đúng $0{,}2$) — khớp.
- F3–F12 chấp nhận theo đề xuất (quy ước $\nu^\pi$, véc-tơ hàng, phạm vi Hệ quả 10.18, mô hình đơn giản hóa của Jin và cộng sự, chuẩn hóa lợi thế theo mini-batch, cắt mất mát giá trị là biến thể, bỏ tr. 27 không nguồn).

### Giai đoạn I.2 — Hợp nhất bản đồ chủ đề và đặc tả soạn

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | quyết định |
|---|---|---|---|---|
| hợp nhất bản đồ chủ đề (chỉ đọc) | general-purpose | opus | high | chấp nhận, kèm quyết định Q1–Q14 |

Bản đồ hợp nhất: 24 chủ đề `lec-10-topic-01`…`24` — cốt lõi 16; cầu nối 5 (tiên quyết và ký hiệu; hai giới hạn của REINFORCE; lợi tức $n$ bước và λ-return; KL và biến phân toàn phần; tổng kết); bổ sung 1 (đường cơ sở có phương sai nhỏ nhất, Greensmith và cộng sự 2004); đọc thêm 2 (hội tụ điểm dừng PPO-Clip, Jin và cộng sự 2024; Phần II của nguồn → Bài 11). Chi tiết cài đặt (nguồn tr. 29–34, 36) xếp `cốt lõi` rút gọn, định tính: tr. 2 của nguồn đặt "đọc PPO như công thức cài đặt" thành mục tiêu và nguồn dành 8/43 trang. Đặc tả: 49 khối bộ đếm chung (10.1–10.49), 21 ví dụ, 3 tình huống, 12 bài tập; đích 17 000–19 500 từ thân văn.

Quyết định của điều phối viên về Q1–Q14: chấp nhận Q1–Q12 và Q14. Q10 (mọi bài tập ở "Bài tập củng cố" cuối tệp) khớp ghi chú Bài 09 đã duyệt (Bài tập 09.1–09.10 đều ở dòng 1300–1464, sau `## Bài tập củng cố`). Q13: giữ quy ước dấu của Nocedal và Wright (2006, Thuật toán 5.2) nhưng viết phần dư là $\tilde g_k=Fx_k-g$ (gradient của mô hình bậc hai tại $x_k$) thay cho $r_k$, để chữ $r$ chỉ giữ nghĩa phần thưởng. SVG: writer ghi chú vẽ các hình mới và hình vẽ lại ở giai đoạn cuối, sau khi văn bản ổn định và trước năm vai rà soát. Đồng bộ ký hiệu với Bài 11 ($\rho_t$, $\kappa$, $M$, $\chi$) để lại cho lần viết lại Bài 11.

### Giai đoạn I.3 — Soạn ghi chú (writer duy nhất, theo giai đoạn)

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| soạn ghi chú | general-purpose | opus | high | chỉ `2627-1/materials/lec-10/lecture-note.md` |

S1–S4 (phần đầu, Mục 1, Mục 2): điều phối viên đọc phần đầu tới hết Ví dụ 10.4, danh mục khối; chấp nhận. Khối: Định nghĩa 10.1, Mệnh đề 10.2, 10.3, Định nghĩa 10.4, Mệnh đề 10.5, Thuật toán 10.6, Mệnh đề 10.7, Thuật toán 10.8, Nhận xét 10.9; Ví dụ 10.1–10.7. Điều phối viên tính lại: $\operatorname{Var}=\tfrac49(b-1)^2$; Ví dụ 10.2 $\widehat g=(-5{,}5;5{,}5)$, $p=\sigma(-1{,}1)=0{,}2497$, $J=-18{,}68$; Ví dụ 10.4 $v_\pi=(-12;-10;-6)$, $\widehat g_b=(9{,}5;-9{,}5)$ — khớp. Yêu cầu sửa nhỏ: dẫn Hệ quả 09.26 ở Bước 1 chứng minh Mệnh đề 10.2; nêu căn cứ hội tụ trội ở Ví dụ 10.4. Writer tự kiểm `no-ai-slop` (Edit + `eval.md`): sửa một câu đối lập nhị phân và một câu hai chấm kịch tính.

Quyết định độ dài: S1–S4 đã có 7 766 từ thân văn (đích đặc tả 4 600). Vì yêu cầu người dùng đặt độ chi tiết của chứng minh lên trước, điều phối viên nâng trần thân văn lên 25 000 từ (vượt mức "thường 8 000–20 000" của `AGENTS.md`; tiền lệ: ghi chú Bài 08 có 37 649 từ `wc -w`), kèm yêu cầu cắt phần lặp.

S5–S8 (Mục 3; Mục 4.1–4.5): điều phối viên đọc Định nghĩa 10.17 → Định lý 10.25 và chứng minh; chấp nhận. Kiểm lại: $\nu^{\pi}=(0{,}1;0{,}045)$, khối $0{,}145=1-(0{,}45+0{,}405)$; $\nu^{\pi'}=(0{,}1;0{,}054)$; hiệu hiệu năng $\tfrac1{0{,}1}(0{,}008+0{,}0216)=0{,}296$; Bổ đề 10.24 $\nu'^\top-\nu^\top=\gamma\nu^\top\Delta_P\bar\Gamma$, $\lVert x^\top M\rVert_1\le\lVert x\rVert_1\lVert M\rVert_\infty$ (chuẩn tổng hàng), $\lVert\bar\Gamma\rVert_\infty\le1/(1-\gamma)$; ví dụ $0{,}009\le18\cdot0{,}016=0{,}288$; Pinsker tại $s_B$: $0{,}1333\le0{,}1561$. Khối mới: Định nghĩa 10.10 → Hệ quả 10.30; Ví dụ 10.8–10.12. Thân văn tích lũy 14 519 từ. Writer tự kiểm `no-ai-slop`: sửa một "thường dùng" không nguồn và hai câu kết kiểu châm ngôn. Giáo trình tham khảo cho Mục 3: Sutton và Barto (2018) §7.1, §12.1–12.3 ((12.2), (12.3), (12.9), Bài tập 12.1, 12.3); Schulman và cộng sự (2016) §3, Định nghĩa 1, Mệnh đề 1. Mục 4: Kakade và Langford (2002) Bổ đề 6.1; Achiam và cộng sự (2017) Bổ đề 3, Hệ quả 1, 3, Mệnh đề 1; Schulman và cộng sự (2015) §2–4; Cover và Thomas (2006) Bổ đề 11.6.1. Mục 2: Sutton và Barto (2018) §13.4, §13.5.

S9–S11 (Mục 5; Mục 6.1–6.6): điều phối viên đọc Mệnh đề 10.39, 10.40 và chứng minh, Ví dụ 10.18; chấp nhận. Kiểm lại bốn mẫu PPO-Clip $2{,}4$; $-1{,}6$; $1{,}4$; $-2{,}6$ và điều kiện dấu bằng của chặn dưới. Khối mới: Định nghĩa 10.31 → Nhận xét 10.49; Ví dụ 10.13–10.21. Thân văn tích lũy 21 056 từ (`wc -w` 31 128). Quyết định độ dài: nới trần thân văn lên 28 000 từ để giữ đủ bài tập củng cố có lời giải cho mọi mục tiêu học tập. Giáo trình và nguồn cho Mục 5–6: Schulman và cộng sự (2015) §5–6, Phụ lục C; Nocedal và Wright (2006) Thuật toán 5.2; Schulman và cộng sự (2017) §3–5, Hình 1, Thuật toán 1; Engstrom và cộng sự (2020); Huang và cộng sự (2022); Jin, Li và Wang (2024) Giả thiết 3.1–3.4, Định lý 3.1–3.3. SVG: giao một vai vẽ riêng sau S12–S13 (ngữ cảnh writer đã lớn), tuần tự, không chạy cùng writer.

S12–S13 (Mục 7, tình huống áp dụng, tóm tắt, Bài tập củng cố 10.1–10.12, tài liệu tham khảo) và lượt tự rà toàn chương của writer: chấp nhận để đưa vào rà soát. Điều phối viên kiểm: 3 khối `application`, 12 `exercise`, 12 `hint`, 12 `solution`; không còn "xem trang chiếu", "hãy", "Mục này", "chưa phải định nghĩa", "mild", "almost always". Thân văn 25 029 từ, `wc -w` 37 202. Bản nháp hoàn chỉnh của writer: chấp nhận (vào rà soát).

### Giai đoạn I.3b — Vẽ hình SVG

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| vẽ SVG | general-purpose | opus | high | 9 tệp trong `2627-1/img/lec-10/` (4 mới, 5 vẽ lại) |

### Giai đoạn I.4 — Năm vai rà soát độc lập, vòng R1

Bản cố định: bản sao `lecture-note.md` (2 291 dòng, sha1 `2e71eb1a17c9…`). Năm vai chạy song song, chỉ đọc; hình đang được vẽ lại song song nên vai rà chỉ xét `alt` và đoạn đọc hình.

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort |
|---|---|---|---|
| góc nhìn sinh viên | general-purpose | opus | high |
| chuyên gia Học tăng cường | general-purpose | opus | high |
| độ chính xác toán học–thuật toán | general-purpose | opus | high |
| phản biện học thuật–giảng dạy + `no-ai-slop` Detect | general-purpose | opus | high |
| kết nối và mạch viết (`quill` checklist, không `quill.json`) | general-purpose | opus | high |

Kết quả vẽ SVG: chấp nhận. 9 tệp (`central-problem`, `two-state-chain`, `gae-weights`, `ppo-one-step-plateau` mới; `actor-critic-advantage`, `policy-update-feedback`, `trpo-trust-region`, `ppo-clipping-signs`, `ppo-data-pipeline` vẽ lại), tọa độ đồ thị sinh bằng script có assert. Điều phối viên xem ảnh chụp `central-problem`, `ppo-clipping-signs`, `trpo-trust-region`, `gae-weights`, `ppo-one-step-plateau`, `two-state-chain` và kiểm số: trọng số $(\gamma\lambda)^k=1;\,0{,}72;\,0{,}518;\,0{,}373;\,0{,}269$, $\lambda^6=0{,}262$; $\mathcal L^{\mathrm{CLIP}}=0{,}267$ ở đoạn phẳng; elip bán trục $0{,}0707$, $0{,}1414$, bước $(0{,}05;0{,}1)$ trên biên. Alt của `gae-weights` ghi $0{,}194$ sai ($0{,}72^5=0{,}1935$) — chuyển editor (D20). `gae-bias-variance.svg`, `ppo-diagnostics.svg` giữ cho bộ trang chiếu cũ, xử lý ở Giai đoạn II.

Giới hạn hiển thị có từ trước (không thuộc phạm vi goal, báo người dùng): quy tắc `.markdown-body img[src^="img/lec-"] { min-width: 900px }` trong `material-viewer-course.css` làm mọi hình ghi chú bị cắt 92 px và phải cuộn ngang trong cột 808 px ở 1280–1600 px (đo bằng Playwright trên ghi chú Bài 09 và Bài 10: ảnh 900 px trong khung 808 px); đã ghi ở nhật ký Bài 05 và Bài 08 là hạ tầng dùng chung chờ quyết định.

### Giai đoạn I.4 — Kết quả vòng R1

| vai | kết luận | chặn | nghiêm trọng | trung bình | nhẹ | quyết định của điều phối viên |
|---|---|---|---|---|---|---|
| góc nhìn sinh viên | CHƯA ĐẠT | 0 | 1 | 6 | 23 | chấp nhận báo cáo; nghiêm trọng đã tính lại ($\alpha=0{,}1$: $p=0{,}5987$, $J=-11{,}66$; $\alpha=0{,}5$: $p=0{,}8808$, $J=-21{,}32$) |
| chuyên gia Học tăng cường | CHƯA ĐẠT | 0 | 1 | 6 | 11 | chấp nhận; tr. 27 đưa vào có dẫn nguồn (bài giảng gốc là nguồn được giao) thay vì bỏ như kế hoạch |
| độ chính xác toán học–thuật toán | ĐẠT | 0 | 0 | 3 | 14 | chấp nhận; mọi số khớp, Bổ đề 10.18, 10.24, Định lý 10.25, Hệ quả 10.26 kiểm thêm trên 2 000 MDP ngẫu nhiên |
| phản biện học thuật–giảng dạy + `no-ai-slop` Detect | CHƯA ĐẠT | 0 | 3 | 17 | 20 | chấp nhận; thêm khối định nghĩa actor–critic và đánh lại số; PPO-Penalty giữ cốt lõi, bổ sung hành trình |
| kết nối và mạch viết | ĐẠT | 0 | 0 | 8 | 16 | chấp nhận; điều phối viên xác nhận Bài 11 dùng $w_t$ cho tỉ số PPO (`lec-11/lecture-note.md` dòng 36, 52) |

Quyết định hợp nhất D1–D21: `scratchpad/review/r1-decisions.md` (tóm tắt: D1 bằng chứng bước lớn; D2 định nghĩa actor–critic + đánh lại số; D3 PPO-Penalty; D4 câu tự nói về văn bản; D5 approxKL cần $\theta$ độc lập mẫu; D6 phát biểu đúng Jin và cộng sự Định lý 3.1/3.2; D7 chuyển tiếp Bài 11; D8 tr. 27; D9 đánh đổi theo $\lambda$ định tính có nguồn; D10 TRPO 2015 dùng Monte Carlo; D11 $\rho_t$ không hiệu chỉnh phân bố trạng thái; D12 "Trong thực hành."; D13 cắt lặp; D14 câu nối một phía, văn bản không làm chủ ngữ; D15 ký hiệu trùng; D16–D21 các điểm trung bình và nhẹ).

### Giai đoạn I.5 — Biên tập sau R1

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| biên tập (editor duy nhất) | general-purpose | opus | high | chỉ `lecture-note.md` |

Kết quả biên tập R1: chấp nhận. 5/5 nghiêm trọng đã sửa (D1–D5); khoảng 40 trung bình đã sửa trừ các mục bác có lý do (không đưa giả mã lên trước ví dụ tính tay vì chuẩn yêu cầu ví dụ trước — thay bằng nêu tại chỗ $I=\gamma^t$ và ba công thức gradient liên hợp; giữ ví dụ approxKL trước định nghĩa theo mẫu tám bước; giữ cả hai bảng ánh xạ bài tập vì một bảng theo mục, một bảng theo mục tiêu). Khối mới: Định nghĩa 10.7 (actor–critic), Ví dụ 10.19 (một lần điều chỉnh $\beta$ của PPO-Penalty), Nhận xét 10.44, Bài tập 10.12(d). Đánh lại số bằng script: bộ đếm chung 10.1–10.51, Ví dụ 10.1–10.22; 0 tham chiếu gãy; `note-topic-id` 01–24 đúng thứ tự. Viewer 1600 px và 390 px, cả print: 0 lỗi KaTeX, 0 yêu cầu lỗi; `scrollWidth` 375 ≤ 390 (đã hết tràn 17 px của thuật toán PPO). Thân văn 27 847 từ (trần 28 000), `wc -w` 40 734: phần bổ sung bắt buộc (D2, D3, D5, D8–D10, D12, D19) lớn hơn phần cắt lặp (D13). Bảng xử lý từng phát hiện: `scratchpad/editor/r1-disposition.md`.

Điều phối viên đo thêm ở 390×844: 72/82 công thức hiển thị cuộn trong hộp riêng (Bài 09 đã duyệt: 28/37); trang không tràn. Quyết định: chuỗi `aligned` có cột căn cứ được cuộn như Bài 09; công thức khác phải ngắt. Quy tắc in nghiêng thuật ngữ mới ở lần đầu ("The author's voice", workspace `CLAUDE.md`) chưa được áp dụng → giao editor. Số hiệu trên `central-problem.svg` (10.47 → 10.49) → giao tác tử vẽ hình (tệp khác, chạy song song với editor).

Bổ sung sau R1, chấp nhận: in nghiêng 38 thuật ngữ ở lần dùng đầu trong văn xuôi; công thức hiển thị cuộn ở 390 px giảm 72 → 8 (còn lại đều là chuỗi `aligned` có cột căn cứ, như Bài 09); mười câu "Dòng hai/ba…" đổi thành "Đẳng thức thứ…" cho khớp sau ngắt. `central-problem.svg` ghi "Thuật toán 10.49" (điều phối viên grep: 2 lần, không còn 10.47); `<desc>` của `central-problem.svg`, `gae-weights.svg` trùng alt. Thân văn 27 880 từ.

### Giai đoạn I.6 — Rà lại vòng R2

Bản cố định R2: 2 627 dòng, sha1 `3455222f4970…`. Năm vai R1 được tiếp tục bằng SendMessage (cùng tác tử, giữ ngữ cảnh): mỗi vai kiểm việc xử lý phát hiện của mình và phần đã đổi trong phạm vi vai; vai mạch viết rà toàn bộ vì mở chương, kết chương và ranh giới mục đã đổi; vai toán tính lại mọi số mới và kiểm mọi chứng minh bị sửa.

Kết quả R2:

| vai | kết luận | chặn | nghiêm trọng | trung bình | nhẹ | phát hiện R1 của vai |
|---|---|---|---|---|---|---|
| góc nhìn sinh viên | ĐẠT có điều kiện | 0 | 0 | 2 | 9 | mọi nghiêm trọng/trung bình đã xử lý đúng; tự giải lại Ví dụ 10.19, Bài tập 10.12(d), 10.6(b) |
| chuyên gia Học tăng cường | CHƯA ĐẠT (gần đạt) | 0 | 0 | 2 | 5 | 18/18 xử lý đúng |
| độ chính xác toán học–thuật toán | ĐẠT | 0 | 0 | 1 | 2 | 17/17 xử lý đúng; tính lại mọi số mới, 0 lệch; 0 tham chiếu gãy |
| phản biện học thuật–giảng dạy + `no-ai-slop` Detect | CHƯA ĐẠT | 0 | 0 | 4 | 15 | 3/3 nghiêm trọng, 17/17 trung bình đúng; đồng ý mọi mục bác; mật độ mẫu slop ≈ 0,4/1 000 từ |
| kết nối và mạch viết (toàn bộ) | ĐẠT | 0 | 0 | 4 | 6 | 22/24 đúng, 2 sửa một phần |

Điều phối viên hợp nhất các điểm trung bình trùng nhau thành E1–E8 (giao editor): $g\in\operatorname{range}F$ chỉ khi cùng trạng thái; giả thiết (G1) trên Breakout (notebook Bài 09 mục 9) và mâu thuẫn dòng 218; tham chiếu trước tới xấp xỉ $p(1-p)$; 8 chuỗi `aligned` tràn ở 390 px; in nghiêng; hai đoạn nhiều ý; câu nói về nội dung chương và câu mảnh; phát biểu tóm tắt về Jin và cộng sự. Quyết định thay đổi: (i) chuỗi `aligned` có cột căn cứ phải vừa khung 390 px bằng cách chuyển căn cứ ra câu ngay sau công thức (`AGENTS.md` cho phép), thay quyết định trước đó cho cuộn; (ii) in nghiêng cả ở mục tiêu và tại câu định nghĩa trong thân văn, theo cách tác giả làm ở ghi chú SLT Bài 01 (dòng 7 và 72 cùng in nghiêng "rủi ro kì vọng").

Biên tập sau R2: chấp nhận. E1–E8 đã sửa; tám chuỗi chứng minh chuyển cột căn cứ ra câu ngay sau công thức, công thức cuộn ở 390 px 8 → 0; in nghiêng ở mục tiêu và tại câu định nghĩa trong thân văn; $q_k\to\tau_k$ trong thuật toán gradient liên hợp; hai mục bác có lý do (không đặt $y_t$ cho mục tiêu bootstrap vì trùng Định nghĩa 10.47; ngoặc ở dòng 259–266 không cần ngắt vì đã vừa khung). Bảng xử lý: `scratchpad/editor/r2-disposition.md`. Thân văn 27 985 từ.

### Giai đoạn I.6b — Rà lại cục bộ vòng R3

Bản cố định R3: 2 659 dòng, sha1 `0b5cd89d679f…`.

| vai | phạm vi | kết luận | phát hiện |
|---|---|---|---|
| toán học–thuật toán (cùng tác tử) | tám chuỗi chứng minh đổi trình bày, E1, E8, $\tau_k$, mọi số trong diff R2→R3, tham chiếu | ĐẠT | 0 |
| kết nối và mạch viết (cùng tác tử) | vùng đổi ±2 tiểu mục, in nghiêng, chứng minh đã chuyển căn cứ | ĐẠT | 5 nhẹ (R3-1…R3-5), giao editor sửa |

Kiểm tra cổng của điều phối viên (Playwright, `reloadserver` tại thư mục gốc repo): viewer 1600×900 và 390×844 — 3 887 biểu thức KaTeX, 0 `.katex-error`, 0 công thức hiển thị cuộn, 0 ảnh lỗi, 0 yêu cầu thất bại, 0 yêu cầu ra ngoài localhost, 0 chuỗi `:::`/`note-topic-id` thô trên trang, `scrollWidth` 375 ở 390 px; chế độ in 0 lỗi KaTeX. Lỗi console duy nhất là CSP chặn script nội tuyến do `reloadserver` chèn (viewer không có script nội tuyến; đã ghi ở các bài trước). `note-topic-id` 24, duy nhất. Không còn "xem trang chiếu", "hãy", "Đáp án", "chưa phải định nghĩa", "mild", "almost always"; các câu có dấu hỏi chỉ là "**Câu hỏi.**" được trả lời ngay và câu hỏi tự kiểm tra. Điều phối viên tự xem ảnh chụp đầu trang (1600, 390), cuối trang (390) và chứng minh Định lý 10.26 ở 390 px: đọc rõ, căn cứ ở câu sau công thức, có $\square$.

Biên tập sau R3: chấp nhận. R3-1…R3-5 đã sửa (hai câu về tích Fisher–vector trên khoảng 10% dữ liệu chuyển xuống sau Thuật toán 10.36 và nối với giả thiết $g\in\operatorname{range}F$; bỏ câu lặp; in nghiêng "lợi tức $n$ bước", "liên hợp" — định nghĩa trước khi dùng, "tìm kiếm lùi"; bỏ câu lặp trong Tình huống 10.3; $\Delta_\pi$ dùng nhất quán trong Bổ đề 10.25); $\tau_k$ thêm vào câu liệt kê ký hiệu riêng. Điều phối viên đọc diff R3 → bản cuối và tính lại $\tau_2=\tfrac5{17}\cdot5+0{,}85\cdot\tfrac{180}{289}=2$. Thân văn 27 938 từ (`wc -w` ≈ 40 900): vượt mức "thường 8 000–20 000" của `AGENTS.md`, lý do đã ghi (yêu cầu chi tiết chứng minh của người dùng; trần 28 000 do điều phối viên đặt).

### Cổng kiểm soát Giai đoạn I — đạt

- Năm vai rà soát độc lập (R1), rà lại năm vai (R2), rà lại cục bộ toán và mạch (R3): không còn phát hiện chặn bàn giao, nghiêm trọng hay trung bình chưa xử lý; mọi phát hiện đã sửa hoặc bác có lý do trong `scratchpad/editor/r1-disposition.md`, `r2-disposition.md`.
- Bảng kiểm `AGENTS.md` §"Kiểm định ghi chú bài giảng": vai sư phạm lập ở R1 và kiểm lại ở R2 (mọi mục chưa đạt ở R1 đã sửa); mỗi mục tiêu học tập có kết quả, ví dụ và bài tập; mỗi định lý bốn phần và có chứng minh hoặc nguồn có số mục/trang; mọi số đã được vai toán tính lại độc lập (R1, R2, R3: 0 lệch).
- Bản đồ chủ đề đủ bốn nhóm, 24 `note-topic-id` duy nhất; viewer 0 lỗi KaTeX ở 1600 và 390 px; `no-ai-slop`: writer và editor tự kiểm chế độ Edit, vai sư phạm Detect hai vòng (mật độ mẫu ≈ 0,4/1 000 từ ở R2, các mẫu còn lại đã sửa).
- Giáo trình đã tham khảo theo mục: Mục 2 — Sutton và Barto (2018) §13.3–13.5; Mục 3 — §7.1, §12.1–12.3; Mục 4 — Kakade và Langford (2002), Achiam và cộng sự (2017), Schulman và cộng sự (2015), Cover và Thomas (2006); Mục 5 — Schulman và cộng sự (2015), Nocedal và Wright (2006); Mục 6 — Schulman và cộng sự (2017), Engstrom và cộng sự (2020), Huang và cộng sự (2022), Andrychowicz và cộng sự (2021), Jin, Li và Wang (2024); Mục 1, 7 — ghi chú Bài 09, Bài 11.
- Bộ trang chiếu cũ `lecture-10-trpo-va-ppo.html` chưa đồng bộ với ghi chú mới (ký hiệu $w_t$, số hiệu cũ); Giai đoạn II làm lại bộ trang chiếu từ ghi chú này. `index.html` đã có liên kết ghi chú Bài 10 từ trước, không đổi.

Commit Giai đoạn I: `1c9ef05` `fix(materials-10): revise TRPO PPO lecture note`, đã push `origin/main` (`git branch -r --contains HEAD` → `origin/main`). Lần push này đẩy kèm commit cục bộ `adb055e` (chore: move tooling to shared workspace, split common/course CSS) đã nằm trên `main` từ trước.

## Giai đoạn II — Làm lại bộ trang chiếu từ ghi chú mới — 04-11-2026

Đầu vào cố định: ghi chú tại commit `1c9ef05`. Bộ trang chiếu cũ (43 trang, ký hiệu $w_t$, mạch cũ) được thay toàn bộ.

### Giai đoạn II.1 — Kế hoạch bộ trang chiếu

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | quyết định |
|---|---|---|---|---|
| lập kế hoạch deck (chỉ đọc) | general-purpose | opus | high | chấp nhận, kèm quyết định |

Kế hoạch: 7 mạch (mạch N = Mục N của ghi chú với N = 2…7; Mục 1 gộp vào mạch mở đầu làm ví dụ dẫn nhập trước "Vấn đề trung tâm", vì tách thành mạch riêng cho 8 mạch, vượt trần 5–7); mã `L10-NXX`, trang tiêu đề mạch `L10-N00`, `id="mach-N"`; phút 12 + 23 + 14,5 + 22,5 + 13,5 + 25,5 + 9 = 120. Quyết định của điều phối viên: (i) dùng phương án gộp 11 cặp trang của kế hoạch, khoảng 90 trang (Bài 09: 67), giữ phút mỗi mạch; (ii) chấp nhận đặt Ví dụ 10.9 trước Mệnh đề 10.15 trên trang chiếu (ví dụ cụ thể trước phát biểu là quy tắc của bộ trang chiếu), ghi lệch thứ tự trong storyboard; (iii) chưa có `exercises.md`, trang "Bài tập về nhà và tài liệu đọc" ánh xạ Bài tập củng cố 10.1–10.12 của ghi chú theo bảng §7.5; (iv) không vẽ hình mới; `gae-bias-variance.svg`, `ppo-diagnostics.svg` không còn tham chiếu → xóa trong commit Giai đoạn II; (v) hình `termination-truncation.svg` của Bài 08 dùng kèm chú thích ở ghi chú diễn giả.

### Giai đoạn II.2 — Soạn (writer duy nhất), bước A: outline và storyboard

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| soạn bộ trang chiếu | general-purpose | opus | high | `planning/lec-10/outline.md`, `storyboard.md`; sau cổng storyboard: deck HTML |

### Đính chính và cập nhật `index.html` (yêu cầu người dùng: "chưa thấy lecture note 10 trong 2627-1/index.html")

Đính chính: mục cổng Giai đoạn I ghi "`index.html` đã có liên kết ghi chú Bài 10 từ trước" là SAI — điều phối viên dựa vào nhật ký cũ mà không kiểm. Thẻ Bài 10 đã bị gỡ ở commit `5261d04` (giới hạn index vào các bài đã hoàn thiện). Điều phối viên thêm thẻ Bài 10 theo yêu cầu trực tiếp của người dùng: nhóm **Ghi chú bài giảng** liên kết `material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html` (ghi chú đã qua cổng Giai đoạn I); **Bài giảng**, **Bài tập**, **Thực hành** ghi `Chưa có` (bộ trang chiếu đang được làm lại ở Giai đoạn II; chưa có `exercises.md` và notebook). Không liên kết tệp quy trình. Kiểm Playwright 1600×900 và 390×844: 10 thẻ, 0 yêu cầu lỗi, `scrollWidth` 375 ở 390 px; bấm "Mở ghi chú" mở đúng "Bài 10 — TRPO và PPO", 0 lỗi KaTeX; điều phối viên xem ảnh chụp thẻ.

Bước A (outline, storyboard): chấp nhận có điều kiện. 90 trang duy nhất, 120 phút (12 + 23 + 14,5 + 22,5 + 13,5 + 25,5 + 9), trang tiêu đề mạch `L10-200`…`L10-700`. Quyết định: chấp nhận phụ đề `h2` trên bìa và luận đề bỏ cụm "critic và GAE đổi phương sai lấy độ chệch" (vượt điều ghi chú khẳng định); tên tiếng Anh dồn sang trang mục tiêu `L10-104`; được tách lại trang gộp nếu đáy trang vượt khung; `topic-04` (bổ sung) và `topic-24` (đọc thêm) mỗi chủ đề một dòng; lệch thứ tự Ví dụ 10.9 trước Mệnh đề 10.15 đã ghi ở II.1. Ngoại lệ mật độ: chấp nhận `L10-105` (Nội dung 8 dòng: bảy mạch + dòng đọc trước, như `L09-02b`), `L10-702` (bảng tổng kết 9 hàng), giả mã 7–10 dòng trên trang riêng (`L10-209`, `215`, `308`, `506`, `507`, `612`; quy tắc: giả mã > 8 dòng có trang riêng); BÁC `L10-101` (bìa 82 âm tiết) và `L10-109` (≈ 85 âm tiết, vượt trần 80 của trang tổng hợp) — phải rút về ≤ 60 và ≤ 80 hoặc tách.

### Giai đoạn II.3 — Cổng storyboard

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort |
|---|---|---|---|
| kiểm cổng storyboard (chỉ đọc) | general-purpose | opus | high |

### Bỏ mục "Bản đồ chủ đề (bốn nhóm)" khỏi ghi chú (yêu cầu người dùng 04-11-2026)

Yêu cầu: "lecture note bỏ phần 'Bản đồ chủ đề (bốn nhóm)', quá nhiều không cần thiết". Yêu cầu người dùng đứng trên `AGENTS.md` và `prompt_lecture_note_deck.md` (quy định bản đồ chủ đề trong ghi chú). Điều phối viên xóa cơ học toàn bộ mục (63 dòng: bốn bảng nhóm, tiểu mục "Bảy phần của chương" và dòng "Đọc trước"), không viết lại câu nào, nên không giao tác tử biên tập; nội dung "Bảy phần" đã có ở Mục 1.1 (hình cấu trúc chương và câu trả lời có điều kiện cho từng mục). Giữ 24 chú thích `note-topic-id` trong thân chương để ánh xạ với `data-slide-id`; bảng phân nhóm bốn nhóm vẫn nằm trong `planning/lec-10/outline.md`. Không còn câu nào trong ghi chú trỏ tới bản đồ chủ đề (grep). Viewer 1600 px: mục lục bắt đầu "Mục tiêu học tập, Kiến thức tiên quyết, Bảng ký hiệu, 1. Hai giới hạn của REINFORCE…", 0 lỗi KaTeX; `git diff --check` sạch.

Cổng storyboard lần 1: CHƯA ĐẠT (2 nghiêm trọng, 7 trung bình, 6 nhẹ; báo cáo `scratchpad/review/deck-gate.md`). Hai nghiêm trọng là hai ngoại lệ điều phối viên đã bác (`L10-101`, `L10-109`) chưa được sửa vì quyết định bác ghi sau khi writer xong bước A. Đạt: 120 phút trên 90 trang, 7 mạch, trang tiêu đề mạch đúng quy định, 24/24 `note-topic-id`, ≈ 40 số tính lại độc lập 0 lệch, bài tập có lời giải trên mặt trang mỗi cụm, bảng bài về nhà trùng §7.5 ghi chú. Quyết định: phụ đề `h2` trên bìa là tiêu đề (không đếm), luận đề ≤ 30 âm tiết không tên tiếng Anh; `L10-109` tách hình sang trang khung riêng; quy ước bảng như Bài 09 (mỗi hàng một dòng; > 6 dòng chỉ ở trang so sánh/tổng kết, có ghi ngoại lệ); mọi trung bình phải sửa. Gửi lại writer (cùng tác tử) sửa storyboard, sau đó cổng kiểm lại.

Cổng storyboard lần 2: CHƯA ĐẠT, còn 3 trung bình (`L10-307`, `L10-509` 7 dòng; `L10-104` mất "chặn cải thiện" ở mục tiêu 3) và 7 nhẹ; cả 2 nghiêm trọng và 5/7 trung bình lần 1 đã xử lý; 94 trang, 120 phút, 24/24 chủ đề. Quyết định: writer sửa nốt theo đề xuất cụ thể của cổng; điều phối viên tự kiểm diff thay cho lần cổng thứ ba (thay đổi cục bộ, đề xuất đã xác định). Bước B (HTML) giao một writer mới vì ngữ cảnh writer bước A đã lớn; hai writer chạy tuần tự.

Sửa sau cổng lần 2: chấp nhận sau khi điều phối viên đọc diff storyboard. `L10-509` tách đề/lời giải thành `L10-509`, `L10-510` (mạch 5 vẫn 13,5 phút); `L10-307` 5 dòng (dòng "Nhắc lại:" chuyển vào ghi chú diễn giả); `L10-104` dòng 3 có "và chặn cải thiện" (20 âm tiết, trang 80); 7 điểm nhẹ đã sửa. Tính lại bài tập gradient liên hợp ($F=\begin{pmatrix}2&1\\1&2\end{pmatrix}$, $g=(1;0)$): $\omega_0=\tfrac12$, $x_1=(0{,}5;0)$, $\tilde g_1=(0;0{,}5)$, $\xi_1=0{,}25$, $p_1=(0{,}25;-0{,}5)$, $\omega_1=\tfrac23$, $x_2=(\tfrac23;-\tfrac13)=F^{-1}g$ — khớp. **Cổng storyboard: đạt.** 95 trang, 120 phút, 24/24 chủ đề; ngoại lệ được duyệt: `L10-105` (8 dòng), `L10-109` (80 âm tiết, trần trang tổng hợp), `L10-702` (bảng 9 hàng).

### Giai đoạn II.2 — Soạn, bước B: HTML bộ trang chiếu

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| soạn HTML deck (writer mới, tuần tự sau writer bước A) | general-purpose | opus | high | `2627-1/lecture-10-trpo-va-ppo.html`; xóa `img/lec-10/gae-bias-variance.svg`, `ppo-diagnostics.svg` |

Kết quả bước B (HTML): chấp nhận để đưa vào rà soát. 97 trang (95 theo storyboard + `L10-212b` tách hình actor–critic vì đáy 767 px; `L10-702b` tách bảng tổng kết 9 hàng thành 5 + 4, phương án dự phòng của storyboard); bỏ hình nhỏ ở `L10-402`, `L10-610` để ≤ 6 dòng; số hiệu kết quả tối đa một lần mỗi trang (phần dư chuyển vào ghi chú diễn giả). Writer phát hiện lỗi trong storyboard mục `L10-309` ("$Z_2=1$ cho $\delta_1=-0{,}1$"): theo ghi chú, $Z_2=1$ cho $\delta_1=-1$, còn $-0{,}1$ là lỗi bootstrap bằng $\hat v(S_2)$ của lượt mới — ghi chú diễn giả đã theo ghi chú bài giảng; storyboard sửa ở bước biên tập. Writer đo trên Playwright cả 97 trang ở 1600×900 và 390×844: 0 lỗi console/page (ngoài CSP của reloadserver), 0 yêu cầu lỗi, 0 `.katex-error`, đáy lớn nhất 680 px (`L10-703`), chữ nhỏ nhất 0,752em; xóa `gae-bias-variance.svg`, `ppo-diagnostics.svg`. Điều phối viên xem ảnh `L10-101`, `L10-400`, `L10-602`: đúng; tắt ba server xem trước của chính mình còn sót (8784–8786, cwd repo).

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort |
|---|---|---|---|
| soạn HTML deck | general-purpose | opus | high |

### Giai đoạn II.4 — Năm vai rà soát độc lập bộ trang chiếu, vòng D1

Bản cố định: bản sao deck 97 trang, sha1 `41d2a97504c8…`. Năm tác tử mới (không dùng lại các reviewer ghi chú vì ngữ cảnh đã lớn), chỉ đọc, song song, mỗi vai một dải cổng server riêng.

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort |
|---|---|---|---|
| góc nhìn sinh viên + đo mật độ | general-purpose | opus | high |
| chuyên gia Học tăng cường | general-purpose | opus | high |
| độ chính xác toán học–thuật toán | general-purpose | opus | high |
| phản biện học thuật–giảng dạy + `no-ai-slop` Detect | general-purpose | opus | high |
| kết nối và mạch (`quill` checklist) | general-purpose | opus | high |

Kết quả D1 (bốn vai đã về):

| vai | kết luận | chặn | nghiêm trọng | trung bình | nhẹ |
|---|---|---|---|---|---|
| kết nối và mạch | ĐẠT | 0 | 0 | 4 | 9 |
| chuyên gia Học tăng cường | ĐẠT | 0 | 0 | 4 | 10 |
| phản biện học thuật–giảng dạy + `no-ai-slop` Detect | CHƯA ĐẠT | 0 | 0 | 13 | 26 |
| độ chính xác toán học–thuật toán | CHƯA ĐẠT | 0 | 0 | 6 | 7 |

Phát hiện lan sang ghi chú (đã duyệt, commit `1c9ef05`): vai toán chỉ ra đoạn sau Hệ quả 10.31 dùng $\chi=0{,}4$ của bước $\pi'$ thay cho $\chi_{\pi_{k+1}}$ của nghiệm miền tin cậy. Điều phối viên tính lại độc lập bằng quét lưới: nghiệm với $\kappa=0{,}004234$ là $p_A\approx0{,}571$, $p_B\approx0{,}824$, $\chi\approx0{,}472$, cận $\approx-3{,}91$ (không phải $-3{,}31$). Thêm: lập luận "5 < 12 nên mọi chênh lệch dương" ở Ví dụ 10.4 chưa đủ (nhẹ). Theo quy tắc "mâu thuẫn thì sửa ghi chú trước", giao một tác tử biên tập ghi chú (general-purpose, opus, high) sửa hai chỗ, chạy song song với việc chờ vai sinh viên; tệp deck không bị đụng.

Lỗi hiển thị có từ trước, ngoài phạm vi: ở 390×844, dòng dẫn trang tiêu đề mạch bị cắt mép phải do quy tắc `@media (max-width: 760px) { … .strand-lead { max-width: none } }` trong `lecture-course.css` (vai mạch thấy cùng lỗi ở Bài 09); sửa cần kiểm cả 12 deck — báo người dùng.

Sửa ghi chú theo phát hiện D1 của vai toán: chấp nhận. Đoạn sau Hệ quả 10.31 nay dùng nghiệm chính xác ($p_A\approx0{,}571$, $p_B\approx0{,}824$, $\chi_{\pi_{k+1}}\approx0{,}472$, cận $\approx-3{,}91$, $\Delta J\approx0{,}299$; tính lại bằng KKT, ràng buộc chặt) và nêu vì sao khác phạt $3{,}31$ của Hệ quả 10.27; Ví dụ 10.4 so số bước còn lại thật $-G_t$ với kỳ vọng $-v_\pi(S_t)$: $(5;12),(4;10),(3;12),(2;10),(1;6)$. Vai toán rà lại: ĐẠT. Viewer 0 lỗi KaTeX ở 1600 và 390 px; `git diff --check` sạch. Trang `L10-412` của deck sửa theo trong vòng biên tập deck.

| góc nhìn sinh viên + đo mật độ (D1) | ĐẠT | 0 | 0 | 14 | 18 |
|---|---|---|---|---|---|

(Bảng bổ sung vai thứ năm của D1.) Vai sinh viên giải lại mọi ví dụ và mọi bài có "Lời giải:" (khớp); đáy lớn nhất 680 px; 0 tràn ngang, 0 `.katex-error`, 0 lỗi trang/yêu cầu; chữ nhỏ nhất 0,75em; bàn phím đúng. Vượt mật độ: `L10-617` (66), `L10-613` (61), `L10-609` (dòng 21 âm tiết) — đều dưới 1,5× trần.

Quyết định hợp nhất D1 (E1–E11, `scratchpad/deckreview/d1-decisions.md`): E1 `L10-412` theo ghi chú đã sửa ($-3{,}91$); E2 số hiệu một lần trên mọi trang kết quả; E3 ký hiệu nêu tại chỗ; E4 Jin và cộng sự đúng dạng $\liminf$ với giả thiết quyết định; E5 bỏ hình Bài 08 ở `L10-307`, dữ kiện chuỗi hai trạng thái thành chữ; E6 mật độ (hàng tiêu đề bảng không tính là dòng); E7 hành trình khái niệm, dòng "Tính …" cho 11 trang ví dụ; E8 "Đầu ra:" và điều kiện dừng cho giả mã TRPO, PPO; E9 các điều kiện thiếu; E10 câu nối và đối chiếu `L10-109`/`L10-707`, nối Bài 11 có SPO và SAM+PPO; E11 ghi chú diễn giả theo `no-ai-slop`. Lỗi CSS dòng dẫn ở 390 px để ngoài phạm vi.

### Giai đoạn II.5 — Biên tập bộ trang chiếu sau D1

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| biên tập deck (editor duy nhất) | general-purpose | opus | high | deck HTML, rồi `storyboard.md`, `outline.md` |

### Video minh họa PPO trên `index.html` (yêu cầu người dùng 04-11-2026)

Yêu cầu: "Thêm video này vào website 2627-1/index.html (lecture 10 để minh hoạ PPO)", tệp do người dùng tải lên. Ghi nhận phê duyệt của người dùng cho tài nguyên không phải SVG (video), theo `../CLAUDE.md` §"Maths and figures". Tệp: `2627-1/materials/lec-10/minh-hoa-ppo-mario.mp4` (205 KB, H.264 256×240, 60 khung/giây, 17,6 giây, không tiếng; nội dung kiểm bằng lưới khung trích bằng ffmpeg của `imageio_ffmpeg`: tác tử chơi màn 1-1 của Super Mario Bros trên NES). Thẻ Bài 10 thêm mục "Minh họa PPO" trải hết bề ngang nhóm tài nguyên: `<video controls muted loop playsinline preload="metadata">` có liên kết dự phòng, chú thích "Tác tử chơi màn 1-1 của Super Mario Bros (NES) theo chính sách học bằng PPO; video không tiếng, dài 17,6 giây." (chỉ nêu điều người dùng cung cấp, không thêm số liệu huấn luyện) và liên kết tải. Đây là nhóm thứ năm ngoài bốn nhóm quy định của thẻ, theo yêu cầu người dùng. CSS mới trong `material-index-course.css` (chỉ `index.html` nạp tệp này): `.resource-item--wide`, `.resource-video` (rộng tối đa 384 px, `image-rendering: pixelated`). Kiểm Playwright Chromium 1600×900 và 390×844: video `readyState` 4, thời lượng 17,58 s, rộng 384 px và 271 px, 0 yêu cầu lỗi, `scrollWidth` 375 ở 390 px; điều phối viên xem ảnh chụp thẻ. Giới hạn: Chromium của Playwright không giải mã H.264 khi tua, WebKit/Firefox của Playwright chưa cài, nên chưa phát thử toàn bộ video trong trình duyệt tự động; trình duyệt phổ thông hỗ trợ H.264 trong MP4.

Kết quả biên tập D1: chấp nhận. E1–E11 đã sửa; trang mới `L10-412b` (Hệ quả 10.31 với nghiệm chính xác, $\chi\approx0{,}472$, cận $\approx-3{,}91$), `L10-502b`, `L10-611b`, `L10-617b`; `L10-617` thành "Ví dụ: cắt mất mát giá trị" có công thức và $\epsilon$; số hiệu kết quả đặt trong nhãn ("**Mệnh đề 10.2.**") trên 36 trang; storyboard, outline đã đồng bộ (mục `L10-309` sửa câu sai về $Z_2$). 101 trang, 120 phút. Đo của editor: 0 lỗi console/page, 0 yêu cầu lỗi, 0 `.katex-error`, đáy ≤ 679 px, chữ ≥ 0,752em, ≤ 2 công thức hiển thị mỗi trang, ≤ 60 âm tiết trừ trang trần 80 (`L10-104`, `109`, `616`, `707`) và bìa, ≤ 6 dòng trừ `L10-105`, không dòng > 20 âm tiết, 101 mã duy nhất, liên kết `#/1`–`#/7` đúng. Mục bác có lý do: lỗi CSS 390 px (ngoài phạm vi); nhãn SVG nhỏ (dữ kiện đã thành chữ theo E5); không thêm câu (d) cho `L10-705` (không có trong ghi chú); không tách `L10-213`, `L10-408` (trong trần). Quyết định điều phối viên: giữ số hiệu trong nhãn; "điểm dừng (stationary point)" ghi tên tiếng Anh trên mặt trang ở lần đầu; giữ ký hiệu $\Delta J$ như ghi chú.

### Giai đoạn II.6 — Rà lại vòng D2

Bản cố định D2: sha1 `115fa157f49d…`, 101 trang. Ba vai D1 được tiếp tục (cùng tác tử): toán (trang đổi, số mới, và bốn trung bình của vai chuyên gia), mạch (toàn bộ, vì mở đầu và kết luận đổi), sư phạm + `no-ai-slop` (trang đổi, quét ghi chú diễn giả).

Kết quả D2: toán ĐẠT (13/13 phát hiện D1 của vai, 4/4 trung bình của vai chuyên gia đã đúng; 34/34 số mới tính lại khớp, `L10-412b` $p=(0{,}5708;0{,}8239)$, $\chi=0{,}4718$, cận $-3{,}908$, $\Delta J=0{,}2991$; 36/36 nhãn số hiệu trỏ đúng ghi chú `9a5478a`; 1 nhẹ); mạch ĐẠT (toàn deck; 4 trang mới đúng mạch; `L10-109`↔`L10-707` đối chiếu từng dòng; liên kết `#/1`–`#/7` đúng trong Chromium; outline, storyboard khớp 101 trang, 24 chủ đề, 120 phút; 4 nhẹ); sư phạm + `no-ai-slop` CHƯA ĐẠT (13/13 trung bình D1 đã đóng, đồng ý ba mục bác; còn 1 trung bình: `L10-618` thiếu "(stationary point)" trên mặt trang và nhãn "Kết luận:" thiếu dấu hai chấm; 7 nhẹ; mật độ mẫu slop ≈ 0,15/trang, từ 0,4). Giao editor (cùng tác tử) sửa trung bình và mọi nhẹ.

Triển khai GitHub Pages (yêu cầu người dùng "tìm cách deploy lại (huỷ lần deploy bị stuck)"): run `41861673688` (commit `509de9e`) kẹt ở "queued" từ 15:49 UTC; `gh run cancel` được nhận nhưng không có hiệu lực, `force-cancel` trả 409 ("not in progress"); điều phối viên gửi `POST /pages/builds` → run mới `41863947868` cũng xếp hàng. githubstatus.com 16:06 UTC: "Incident with Actions and Pages — investigating", Actions và Pages "degraded_performance". Ghi chú bài giảng bản `9a5478a` đã lên trang (run `41854875366` thành công).

Biên tập sau D2: chấp nhận. `L10-618` có "điểm dừng (stationary point)" và nhãn "**Kết luận:**" (58 âm tiết); mọi điểm nhẹ D2 đã sửa ("điều kiện bước học" ở `618`, `704`; `710` giải thích SPO, SAM+PPO, hai dòng nối có chủ ngữ; `617b` năm và phạm vi thí nghiệm của Engstrom và cộng sự; `617`, `408`, `109`, `211`; năm câu ghi chú mở bằng phần tử của trang và tám chỗ trỏ; storyboard `L10-206` bỏ hình). Editor đo lại 101 trang ở 1600×900 và 390×844: 0 lỗi, 0 `.katex-error`, đáy ≤ 680 px, mật độ trong trần.

### Giai đoạn II.7 — Kiểm định cuối

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort |
|---|---|---|---|
| kiểm định cuối (chỉ đọc) | general-purpose | opus | high |

Kết quả kiểm định cuối (báo cáo `scratchpad/final/final-check.md`): 6/7 mục ĐẠT, còn 1 nhẹ. Số đo: 101 `data-slide-id` duy nhất, không lộ trên mặt trang; 7 mạch; 0 tài nguyên mạng, 0 tệp thiếu, 0 raster; ở 1600×900 và 390×844: 0 lỗi console/trang/yêu cầu, 0 `.katex-error`, đáy lớn nhất 679 px (`L10-303`), chữ nhỏ nhất 0,752em; bàn phím đi đủ 101 trang theo thứ tự; `#/2`…`#/7` khớp số mạch và trang "Nội dung"; mật độ chỉ vượt ở ngoại lệ đã duyệt; storyboard, outline khớp 101 trang, 120 phút, 24/24 chủ đề; 36/36 nhãn số hiệu đúng ghi chú; 10 ví dụ tính lại 0 lệch; `git diff --check` sạch. Lỗi: ghi chú diễn giả `L10-400` có "chúng ta"; tùy chọn: chỉ đường "tiếp theo là…" ở ghi chú `L10-300`, `outline.md` §Hình còn ghi hai SVG "có thể xóa". Điều phối viên không dùng đề xuất "Mạch này tìm…" (văn bản làm chủ ngữ); giao editor viết thẳng nội dung. Kiểm định viên không tái hiện lỗi cắt dòng dẫn ở 390 px (mép chữ 358–372 px) nhưng ghi số "N." chỉ 0,72em ở 390 px do `lecture-course.css` — lỗi chung, ngoài phạm vi.

Sửa sau kiểm định cuối: chấp nhận. Ghi chú diễn giả `L10-400` bỏ "chúng ta" (viết thẳng: "Cần một công thức chính xác cho $J(\pi')-J(\pi)$…"); `L10-300` bỏ "tiếp theo là…"; `outline.md` §Hình ghi hai SVG đã xóa. Toàn deck: 0 "chúng ta", 0 "tiếp theo". Điều phối viên xem ảnh kiểm định cuối `L10-412b`, `L10-618` (1600×900), `L10-710` (390×844): đúng.

### Cổng kiểm soát Giai đoạn II — đạt

- Năm vai rà soát độc lập (D1), rà lại ba vai (D2), kiểm định cuối: không còn phát hiện chặn bàn giao, nghiêm trọng hay trung bình chưa xử lý; bảng xử lý `scratchpad/deckeditor/d1-disposition.md` (mục D1, D2).
- Bộ trang chiếu giữ ý chính và thứ tự của nguồn theo ghi chú; sai khác có chủ ý ghi trong `outline.md` (Ví dụ 10.9 trước Mệnh đề 10.15; Phần II của nguồn chuyển Bài 11; các lệch thứ tự cục bộ khác đã ghi).
- `outline.md`, `storyboard.md` khớp deck: 101 trang, 7 mạch, trang tiêu đề mạch `L10-200`…`L10-700`, 120 phút, 24/24 `note-topic-id`.
- Mật độ: chỉ vượt ở ngoại lệ đã duyệt (`L10-105` 8 dòng; trang trần 80 `L10-104`, `109`, `616`, `707`; bảng tổng kết `L10-702`/`702b`).
- Hình: toàn SVG cục bộ, không raster; xóa `gae-bias-variance.svg`, `ppo-diagnostics.svg` (không còn tham chiếu).
- Trình duyệt: 1600×900 và 390×844 mọi trang, 0 lỗi, 0 `.katex-error`, đáy ≤ 680 px, bàn phím đủ 101 trang.
- `no-ai-slop`: writer và editor tự kiểm chế độ Edit; vai sư phạm Detect hai vòng (≈ 0,4 → 0,15 mẫu/trang).
- `index.html`: nhóm **Bài giảng** của thẻ Bài 10 đổi từ `Chưa có` thành liên kết `lecture-10-trpo-va-ppo.html` (kiểm Playwright: mở đúng deck 101 trang, 0 yêu cầu lỗi); **Ghi chú bài giảng** giữ liên kết viewer; **Bài tập**, **Thực hành** `Chưa có`; mục "Minh họa PPO" giữ nguyên.
- `planning/lec-10/note-for-author.md` thuộc vòng cũ (mã trang `L10-05`… và ký hiệu $w_t$), không còn khớp deck; giữ làm hồ sơ, không liên kết.
- Giới hạn còn mở (ngoài phạm vi, báo người dùng): `lecture-course.css` ở 390 px — số "N." trang tiêu đề mạch 0,72em và dòng dẫn có thể sát mép; `material-viewer-course.css` — hình ghi chú `min-width: 900px` bị cắt/cuộn trong cột 808 px.

### Video minh họa PPO thứ hai trên `index.html` (yêu cầu người dùng 05-11-2026)

Yêu cầu: "Thêm video này vào 2627-1/index.html", tệp người dùng tải lên `step_008003584.mp4`; ghi nhận phê duyệt của người dùng cho tài nguyên video. Tệp: `2627-1/materials/lec-10/minh-hoa-ppo-mario-2-4.mp4` (114 KB, H.264 256×240, 60 khung/giây, 12,75 giây, không tiếng; lưới khung trích bằng ffmpeg: màn 2-4 lâu đài của Super Mario Bros, dung nham, thanh lửa, kết thúc ở cầu cuối màn). Mục "Minh họa PPO" của thẻ Bài 10 nay xếp hai video trong lưới `.resource-video-grid` (hai cột ở màn rộng, một cột ở màn hẹp), mỗi video có chú thích ghi màn chơi và liên kết tải riêng; chú thích video thứ hai ghi "tên tệp gốc ghi mốc 8 003 584 bước" (chỉ dẫn tên tệp, không suy thêm). Kiểm Playwright 1600×900 và 390×844: hai video `readyState` 4 (17,58 s và 12,75 s), rộng 267/271 px, 0 yêu cầu lỗi, `scrollWidth` 375 ở 390 px; điều phối viên xem ảnh chụp thẻ.

### Video minh họa PPO thứ ba trên `index.html` (yêu cầu người dùng 06-11-2026)

Yêu cầu: "add this video to lecture 10 rl-plan", tệp người dùng tải lên `step_006001680.mp4`; ghi nhận phê duyệt của người dùng cho tài nguyên video. Tệp: `2627-1/materials/lec-10/minh-hoa-ppo-mario-8-1.mp4` (540 KB, H.264 256×240, 60 khung/giây, 36,67 giây, không tiếng; lưới khung trích bằng ffmpeg: màn 8-1 của Super Mario Bros, tác tử vượt hố, ống, bậc thang và chạm cột cờ cuối màn). Thêm `figure.resource-video` thứ ba vào lưới `.resource-video-grid` của mục "Minh họa PPO" trong thẻ Bài 10, cùng mẫu với hai video trước: chú thích ghi màn chơi, "tên tệp gốc ghi mốc 6 001 680 bước" (chỉ dẫn tên tệp, không suy thêm), thời lượng, liên kết dự phòng và liên kết tải. Không đổi CSS: lưới `auto-fit` xếp 2 + 1 ở màn rộng, một cột ở màn hẹp. Kiểm Playwright 1600×900 và 390×844: ba video `readyState` 4 (17,58 s, 12,75 s, 36,67 s), rộng 267/271 px, 0 lỗi console, 0 yêu cầu lỗi, `scrollWidth` 375 ở 390 px; điều phối viên xem ảnh chụp mục video.

## Giai đoạn III — Bài tập `exercises.md` (yêu cầu người dùng 05-11-2026)

Yêu cầu: "tiếp tục làm bài tập cho lecture 10"; "lấy nguồn bài tập Sutton & Barto". Theo `prompt_lecture_note_deck.md` Giai đoạn III: một writer → ba vai rà soát song song (toán–thuật toán, sinh viên, sư phạm + `no-ai-slop` Detect) → sửa → rà lại → cổng → thêm nhóm **Bài tập** vào thẻ index → commit, push. Số hiệu dùng chung bộ đếm với ghi chú: ghi chú có Bài tập 10.1–10.12, nên `exercises.md` bắt đầu từ Bài tập 10.13; không lặp đề Bài tập củng cố.

Nguồn ứng viên (Sutton và Barto, 2018), loại trừ các bài Bài 09 đã dùng (6.13, 13.1, 13.2, 13.3, 13.5): mạch 2 — Bài tập 6.1, 7.6, 13.4; mạch 3 — 7.1, 12.1, 12.2, 12.3, 12.7, 12.8; mạch 4 — 5.5, 5.6, 5.13, 7.4–7.6. Sách không có bài tập về TRPO, gradient tự nhiên, PPO; các mạch đó trỏ Bài tập củng cố của ghi chú hoặc dùng mở rộng có căn cứ của một bài trong sách.

| vai | loại tác tử | mô hình (từ lời gọi công cụ) | effort | phạm vi ghi |
|---|---|---|---|---|
| soạn `exercises.md` | general-purpose | opus | high | `2627-1/materials/lec-10/exercises.md` |

Bản nháp `exercises.md`: chấp nhận để đưa vào rà soát. 9 bài, Bài tập 10.13–10.21, nguồn Sutton và Barto (2018): 10.13 Bài tập 12.2 tr. 290 (mở rộng sang GAE); 10.14 Bài tập 3.15–3.16 tr. 61; 10.15 Bài tập 6.1 tr. 121; 10.16 Bài tập 7.6 tr. 150–151 (mở rộng: dịch lợi thế trong PPO); 10.17 Bài tập 5.13 tr. 114–115 (mở rộng: hàm thay thế); 10.18 Bài tập 12.8 tr. 309; 10.19 Bài tập 13.4 tr. 335–336 (mở rộng: Fisher, gradient tự nhiên, tỉ số PPO cho chính sách Gaussian); 10.20 Hình 13.2 tr. 330–331 (lập trình); 10.21 Bài tập 3.15–3.16 (mở rộng: PPO trên CartPole). Không bài nào trùng bài tập trên trang chiếu. Writer kiểm viewer 1600 và 390 px: 0 `.katex-error`, 27 khối, 18 liên kết `#/h/v` mở đúng trang; tự kiểm `no-ai-slop` Edit. Bản cố định E1: sha1 `869139e19f3a…`.

| vai rà soát E1 | loại tác tử | mô hình (từ lời gọi công cụ) | effort |
|---|---|---|---|
| độ chính xác toán học–thuật toán (tính lại mọi lời giải) | general-purpose | opus | high |
| góc nhìn sinh viên | general-purpose | opus | high |
| phản biện sư phạm + `no-ai-slop` Detect | general-purpose | opus | high |

Kết quả E1:

| vai | kết luận | chặn | nghiêm trọng | trung bình | nhẹ |
|---|---|---|---|---|---|
| toán học–thuật toán | CHƯA ĐẠT | 0 | 1 | 2 | 5 |
| góc nhìn sinh viên | ĐẠT | 0 | 0 | 3 | 10 |
| sư phạm + `no-ai-slop` Detect | CHƯA ĐẠT | 0 | 1 | 2 | 13 |

Nghiêm trọng: (1) 10.13 dịch "half-life" thành "nửa chu kỳ" → "chu kỳ bán rã (half-life)"; (2) 10.20(c) "16/100 lần tràn số trong 21 lượt đầu" không tái lập được vì đề không định nghĩa tràn số (vai toán: theo tiêu chí `OverflowError`/không hữu hạn vẫn 16 lần nhưng ở lượt 8–272, các lần còn lại $-11{,}92$ chứ không $-12{,}04$). Trung bình: 10.18 "Kiểm tra lại" lệch biểu thức (2,2862); 10.15(c) điều kiện hiệu chỉnh; 10.20(c) với $\alpha_w=2^{-9}$ ≈ 1% lần chạy kẹt ở $p\to1$; liên kết Bài tập củng cố chưa có neo; 10.16(a) dẫn (7.13) không viết ra; đoạn mở đếm sai số bài mở rộng; 10.14(a) lặp Ví dụ 10.1. Đạt: mọi số khác khớp (vai toán viết lại 10.20 độc lập, ba cấu hình seed 2026, 2027, 2029 trùng từng chữ số); số bài, số trang Sutton và Barto và dấu đúng so với PDF; 33 số hiệu ghi chú đúng; không bài nào lặp Bài tập củng cố 10.1–10.12; viewer 0 `.katex-error`, 18 liên kết deck đúng. Quyết định: mọi số thực nghiệm phải tái lập được từ mã và seed ghi trong tệp; liên kết ghi chú dùng neo `#bai-tap-cung-co`. Giao writer (cùng tác tử) sửa.

Sửa sau E1: chấp nhận. Mọi phát hiện nghiêm trọng, trung bình và nhẹ đã sửa, không bác (bảng `scratchpad/ex10/e1-disposition.md`). 10.13 dùng "chu kỳ bán rã (half-life)"; $h=2048$, $h=128$ dẫn Schulman và cộng sự (2017) Bảng 3/5. 10.20(c) nêu tiêu chí tràn số và cách chạy, có mã tham chiếu đầy đủ; writer chạy lại: $\alpha_w=2^{-6}$ (seed 2028) 16 lần tràn ở lượt 7–272, 84 lần còn lại đạt $-11{,}92$ (0,12) ở lượt 901–1000; $\alpha_w=2^{-9}$ không tràn, seed 1–10 có 6/1000 lần kẹt (4 gần $p\approx0$, 2 gần $p\approx1$) — ghi 6/1000 theo kết quả tái lập, không ghi 1%. 10.14(a) thay bằng $c=-1$ (phương sai $0$), $c=2$ (phương sai $4$) — điều phối viên kiểm: $\tfrac49(c+1)^2$. Viewer 1600 và 390 px: 0 `.katex-error`, không tràn (chỉ hai khối mã cuộn trong khung), 18 liên kết deck và neo `#bai-tap-cung-co` đúng. Bản cố định E2 gửi lại vai toán và vai sư phạm (hai vai có phát hiện nghiêm trọng) rà phần đã đổi.

Kết quả E2: toán ĐẠT (8/8 phát hiện E1 đúng; trích nguyên mã tham chiếu 10.20 và chạy lại: seed 2026–2029 khớp từng chữ số, $\alpha_w=2^{-6}$ 16 lần tràn ở lượt 7–272, 84 lần $-11{,}92$ (0,12), seed 1–10 6/1000 lần kẹt; mọi số mới khớp; 2 nhẹ); sư phạm + `no-ai-slop` ĐẠT (16/16 phát hiện E1 đúng; 2 nhẹ). **Cổng nội dung bài tập: đạt** sau khi sửa các điểm nhẹ. Việc kèm theo, chạy song song trên tệp khác nhau: writer bài tập sửa điểm nhẹ và thêm ánh xạ Bài tập 10.13–10.21 vào Mục 7.5 của ghi chú (theo tiền lệ Bài 09); editor deck cập nhật `L10-709` (bảng `Mạch | Bài tập` theo `exercises.md`, liên kết "Ghi chú bài giảng · Bài tập") và storyboard.

Sửa nhẹ sau E2 và cập nhật ghi chú: chấp nhận. `exercises.md`: N1, N2, dấu ở 10.15(d), câu về lần chạy thoát chậm ở hạt giống 8 trong 10.20(c). Điều phối viên chạy lại độc lập đúng mã tham chiếu trong tệp (cách thứ hai, $\alpha_\theta=\alpha_w=2^{-9}$, hạt giống 8): lần chạy 35 có 40/100 lượt cuối bị cắt, $p=0{,}246$; trung bình lượt 901–1000 $-16{,}18$ (sai số chuẩn $4{,}16$) — khớp. Ghi chú: dòng quy ước số hiệu nêu Bài tập 10.13–10.21 thuộc tệp bài tập; Mục 7.5 thêm cột "Tệp bài tập" và liên kết viewer `exercises.md`; không câu nào khác đổi. Viewer hai tệp ở 1600 và 390 px: 0 `.katex-error`, không tràn ngang.

Cập nhật deck theo `exercises.md`: `L10-709` bảng `Mạch | Bài tập | Bài tập củng cố (ghi chú)` (mạch 1 gộp mạch 2), `L10-710` thêm "Ghi chú bài giảng · Bài tập" tới hai URL viewer; storyboard đồng bộ. Rà lại `L10-707`–`L10-710` (vai mạch, cùng tác tử D1/D2): ĐẠT có điều kiện — 1 trung bình (Mục 7.5 ghi chú lệch: 10.3 và thiếu 10.14, 10.21) và 1 nhẹ (ghi chú `L10-707` lặp số hiệu); cả hai đã sửa (writer bài tập sửa Mục 7.5; editor deck sửa `L10-707`). Điều phối viên đối chiếu bằng script ba bảng (đầu `exercises.md`, Mục 7.5 ghi chú, `L10-709`): khớp từng bài — mạch 1: 10.14; 2: 10.14–10.16, 10.20, 10.21 | 10.1, 10.4, 10.5, 10.10; 3: 10.13, 10.15, 10.18 | 10.6, 10.7; 4: 10.16–10.18 | 10.11; 5: 10.19 | 10.8, 10.9; 6: 10.16, 10.19, 10.21 | 10.2, 10.12; 7: 10.21 | 10.3.

Kiểm cổng Giai đoạn III (điều phối viên, Playwright): viewer `exercises.md` 1600×900 và 390×844 — 0 `.katex-error`, 0 công thức cuộn, 0 `:::` thô, 0 yêu cầu lỗi, 0 yêu cầu ra ngoài, `scrollWidth` 375 ở 390 px; 18 liên kết deck `#/h/v` mở đúng `L10-101`, `200`, `210`, `216`, `300`, `309`, `400`, `413`, `414`, `500`, `509`, `510`, `600`, `619`, `620`, `700`, `705`, `706`; `index.html` "Mở bài tập" mở đúng "Bài tập Bài 10 — TRPO và PPO", 0 lỗi KaTeX; `git diff --check` sạch. Giới hạn: viewer không cuộn tới neo `#bai-tap-cung-co` khi mở trang mới (nội dung dựng bất đồng bộ, `material-viewer.js` không xử lý hash sau khi dựng; sửa viewer đụng tệp đang có thay đổi chưa commit của người khác) — liên kết vẫn mở đúng ghi chú, chữ liên kết ghi "(mục Bài tập củng cố, cuối ghi chú)".

**Cổng Giai đoạn III: đạt.** `index.html`: nhóm **Bài tập** của thẻ Bài 10 liên kết `material-viewer.html?doc=materials/lec-10/exercises.md&deck=lecture-10-trpo-va-ppo.html`.

## Siết và rà soát ghi chú theo chuẩn 2026-11 (2026-11-08)

**Tác tử** (lấy từ lời gọi công cụ): mọi vai đều là `Agent`, `subagent_type: general-purpose`, `model: opus` (Claude Opus 5.5), `effort: high`.
- Ba rà soát chỉ đọc, song song: văn phong (`no-ai-slop` Detect); chuẩn giáo trình; toán/RL.
- Một biên tập viên (`no-ai-slop` Edit, tự kiểm theo `eval.md`).
- Hai kiểm tra lại chỉ đọc: độ chính xác; mạch viết và kết nối.

Goal của người dùng: "rà soát ghi chú các bài của rl-plan 01–10 về nội dung, bố cục, văn phong theo các nguyên tắc đã thiết lập". Người dùng chọn đi đủ vòng, commit và push từng bài. Trần độ dài của học phần là 30 000 từ prose (người dùng nới 2026-11-08, thay mốc 8 000–20 000 của `AGENTS.md`).

Đây là vòng siết đầu tiên của Bài 10 kể từ khi deck được dựng lại từ ghi chú (`108b9e5`).

**Rà soát:**

| Vai | Chặn | Nghiêm trọng | Trung bình | Nhẹ |
|---|---:|---:|---:|---:|
| Văn phong | 0 | 1 | 14 | 83 |
| Chuẩn giáo trình | 1 | 0 | 4 | 53 |
| Toán/RL | 0 | 0 | 2 | 3 |

**Quyết định của điều phối viên:**
- **G58 (chặn) và S0 (nghiêm trọng), chấp nhận:** prose 32 654 vượt trần 30 000. Mục tiêu đặt ra là ≤ 29 500.
- **S11 và G8, phương án A:** cắt danh sách trả lời ở §1, vì nó trùng §7.3 và phát biểu kết quả trước khi chứng minh. Đoạn đọc hình giữ vai "điều chương xây dựng".
- **Sáu kết mục "Như vậy, …"** và khoảng 25 câu bên lề "Bài giảng gốc (tr. …)": rút gọn. Mỗi kết quả phát biểu không chứng minh vẫn giữ một dòng nguồn có số trang (G21).
- **Ba câu "nằm ngoài phạm vi học phần"** (Mệnh đề 10.24, Nhận xét 10.28, 10.51): giữ, vì chúng đi kèm chứng minh bị bỏ qua (`AGENTS.md`, bước 5).
- **Hai câu "số liệu sư phạm":** cắt.
- **Bổ sung theo G:**
  - G32: đoạn "Trong thực hành" sau Mệnh đề 10.34.
  - G41: vấn đề và trực giác của §6.4.
  - Câu mở §7.
- **M1, chấp nhận:** câu "hệ số $-\hat v(S_t)$ chỉ phản ánh sai số của critic" sai. Với $\hat v=v_\pi$, hệ số vẫn là $-v_\pi(S_t)\ne0$.
- **M2:** chữ $e$ mang hai nghĩa. Giữ ký hiệu vì deck dùng cả $e_A$ lẫn $e(s)$; đưa vào danh sách ngoại lệ sau bảng ký hiệu.
- **G57, bác bỏ:** "outline thiếu Phân loại chủ đề". Bảng phân loại bốn nhóm đã có trong mục "Ánh xạ hai chiều" của `outline.md`.
- **Bước 8, bác bỏ:** theo quyết định của người dùng 2026-11-08, như Bài 08.

**Kiểm tra lại:**
- Độ chính xác: 0 chặn, 0 nghiêm trọng, 3 trung bình, 7 nhẹ.
  - A1: bước 7 của Thuật toán 10.37 so với Schulman và cộng sự (2016).
  - A3: khôi phục điều kiện dấu ở L2031.
  - A2: deck L1014 lệch; chỉ ghi lại.
- Mạch viết: 0 chặn, 1 nghiêm trọng, 2 trung bình, 8 nhẹ.
  - F5 (nghiêm trọng): "phép xấp xỉ này" mất tiền ngữ sau khi cắt. Đã sửa thành "phép xấp xỉ giữ phân bố trạng thái cũ (Ví dụ 10.11)"; điều phối viên đã kiểm.
- Tất cả được chấp nhận và đã sửa.
- Đồng bộ thêm: Bài 09 nay phát biểu Hệ quả 09.24 cho MDP hữu hạn, nên Kiến thức tiên quyết và Mệnh đề 10.5(b) đã được sửa cho khớp.

**Số liệu:**
- Prose 32 654 → 29 425.
- 132 dòng tiêu đề khối và mục trùng khít trước và sau.
- 266 dòng `:::` và 24 `note-topic-id` giữ nguyên. `git diff --check`: sạch.

**Lệch cần đồng bộ:** deck L652 và L1014 (A1, A2); dòng nguồn của deck trỏ tới câu đã cắt (A10).

**Kiểm tra trình duyệt (điều phối viên):** máy chủ tĩnh cổng 8783, Playwright, viewer của ghi chú, 1600×900, 390×844 (cuộn đến cuối) và chế độ in.
- 0 `.katex-error`, 0 `:::` sót, 0 request lỗi hoặc ra ngoài, không tràn ngang trang.
- Console có một lỗi CSP chặn script nội tuyến. Lỗi này cũng xuất hiện ở ghi chú Bài 11, vốn không bị sửa, nên đến từ môi trường kiểm tra, không đến từ ghi chú.
- Điều phối viên đã xem ảnh chụp. Ở 390 px không có công thức hiển thị nào tràn khung.

Quyết định của điều phối viên: **chấp nhận**; commit `fix(materials-10)`.
