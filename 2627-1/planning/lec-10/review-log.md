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
