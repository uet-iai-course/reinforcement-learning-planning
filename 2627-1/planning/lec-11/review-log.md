# Nhật ký rà soát Bài 11

## Nguồn

- Nguồn chính: `RL-hk2-2025-2026/lecture11_part3.pdf`, 78 trang.
- Nguồn sơ cấp dùng để kiểm chứng: Xie et al. (2025), SPO; Lee & Yoon (2025), SAM+PPO; Mnih et al. (2016), A3C; Silver et al. (2014), DPG; Lillicrap et al. (2016), DDPG; Barth-Maron et al. (2018), D4PG; Lowe et al. (2017), MADDPG; Wang et al. (2017), ACER; Wu et al. (2017), ACKTR; Haarnoja et al. (2018), SAC; Fujimoto et al. (2018), TD3; Liu et al. (2017), SVPG; Espeholt et al. (2018), IMPALA; Cobbe et al. (2021), PPG.
- Không dùng ảnh raster hoặc tài nguyên mạng. Mười một hình được vẽ lại bằng SVG.

## Sai khác và sửa lỗi nguồn

| mức độ | trang nguồn | vấn đề | xử lý |
|---|---|---|---|
| nghiêm trọng | 4–43 | Lặp toàn bộ Bài 10. | Gộp thành một cầu nối tiên quyết. |
| nghiêm trọng | 45–46 | Thiếu miền, đạo hàm bậc hai và ca $A=0$. | Viết đủ $f$, hai đạo hàm, $0<\epsilon\le1$, $w\ge0$ và nghiệm không duy nhất khi $A=0$. |
| nghiêm trọng | 48–49 | Dấu nhiễu SAM dễ bị đảo theo quy ước loss minimization. | Dùng max–min reward và $\xi_{adv}=-\rho g/\|g\|$. |
| nghiêm trọng | 50–51 | Liên kết độ phẳng với độ bền được nêu quá rộng. | Yêu cầu điều kiện Jacobian/rank; coi liên hệ transition/reward là trực giác và bằng chứng thực nghiệm; ghi phạm vi ba tác vụ MuJoCo. |
| nghiêm trọng | 55–56 | Action IS có thể bị suy rộng sang replay. | Nêu fixed-state identity, support, trajectory products và occupancy caveat. |
| nghiêm trọng | 59 | DPG thiếu quy ước occupancy và kiểu. | Thêm occupancy chuẩn hóa, $1/(1-\gamma)$, miền, Jacobian và khả vi. |
| nghiêm trọng | 57–58 | A3C/A2C chỉ có mô tả. | Thêm n-step target, mask, entropy, stale gradients và đồng bộ. |
| nghiêm trọng | 60–64 | DDPG, D4PG, MADDPG thiếu target/gradient thực thi. | Thêm bốn mạng DDPG, distributional return và CTDE target. |
| nghiêm trọng | 65–67 | ACER/ACKTR chỉ liệt kê tên cơ chế. | Thêm residual correction identity và Fisher/Gauss–Newton K-FAC. |
| nghiêm trọng | 68–71 | SAC/TD3 thiếu exact targets; có tuyên bố thực hành rộng. | Thêm soft target/actor, giữ alpha cố định; thêm exact TD3 target, delayed actor/targets; bỏ “best/default/stable”. |
| trung bình | 72–74 | Survey chỉ mô tả bằng lời; PPG thiếu cloning KL. | Mỗi phương pháp có phương trình hoặc cơ chế định nghĩa; thêm KL cloning. |
| nghiêm trọng | 75–77 | Khuyến nghị xếp hạng hoặc mặc định không có điều kiện. | Thay bằng bản đồ cơ chế và checklist đọc thuật toán. |

## Kiểm số và công thức

- SPO: $\partial f/\partial w=A-|A|(w-1)/\epsilon$; $\partial^2f/\partial w^2=-|A|/\epsilon$; ca số cho $2{,}2$ và $-1{,}8$.
- SAM: $\|(3,4)\|=5$ và $\xi=(-0{,}06,-0{,}08)$.
- Action IS: ví dụ hai hành động cho kỳ vọng $1{,}6$ ở cả hai vế.
- DPG: occupancy chuẩn hóa đi cùng $1/(1-\gamma)$; $D_\theta\mu$ có kích thước $d_a\times d_\theta$ và được chuyển vị trước khi nhân $\nabla_aQ$.
- TD3: $1+0{,}9\min(4,5{,}5)=4{,}6$.
- ACER residual identity được kiểm bằng tách miền $\rho\le\bar c$ và $\rho>\bar c$.

## Tự kiểm biên tập của tác tử soạn

- Đã áp dụng `no-ai-slop`: cắt lời dẫn rỗng, câu hỏi tu từ, khẩu hiệu, nhịp câu máy móc và tuyên bố phổ quát không có căn cứ.
- Đã dùng `quill` để rà mạch: PPO → SPO/SAM → off-policy identity → actor–critic → DPG/DDPG → các mở rộng → survey; không tạo `quill.json`.
- Đã dùng nguyên tắc `codex-slides`: kế thừa template/CSS/thư viện cục bộ, một luận điểm trung tâm, hình đủ lớn và ghi chú có nguồn. Điều phối viên thực hiện bước nhập dự án và rà trực quan.
- Không sửa `index.html`, `lecture-style.css`, RevealJS hoặc plugin.

## Trạng thái vòng hiện tại

Bản nháp có 43 trang chính, 3 bài tập dọc, 5 mạch ngoài, 11 SVG, 110 phút cốt lõi, 10 phút mở rộng và 30 phút bài tập. Nguồn văn bản trích xuất có 1.326 dòng theo `wc -l`; số 1.404 do worker báo là số dòng đã chuẩn hóa qua cầu nối và không được dùng làm chuẩn. Bản này đã qua kiểm định storyboard và năm phản biện độc lập; kiểm định hiển thị cuối được ghi sau khi hoàn tất.

## Đóng SB11-01–SB11-12

| mã | mức độ | trang chiếu | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|---|
| SB11-01 | nghiêm trọng | storyboard | Các cụm khái niệm và bài tập làm mờ tổng 120+30 phút. | Bảng cũ cộng thời lượng theo chu trình có trang dùng chung. | Đổi thành bảy khoảng chính không chồng lặp: 7; 24+4; 18; 25; 24; 8+6; 4 phút. `X01/X02/X03` tách riêng 8/12/10 phút; phần linh hoạt gắn `L11-10` và `L11-39`. |
| SB11-02 | nghiêm trọng | `L11-04`–`L11-07` | SPO đưa công thức trước trực giác và ví dụ. | Bản cũ có objective ở `L11-05`, đạo hàm ở `L11-06`, số ở `L11-07`. | Sắp vấn đề → lực kéo tỷ số → số $A=\pm2$ → objective/đạo hàm/$A=0$; `L11-07` ghi SPO chỉ thay policy loss, giữ old batch, critic và pipeline. |
| SB11-03 | nghiêm trọng | `L11-08`–`L11-12` | SAM đưa max–min trước ví dụ và hình chưa thể hiện sharp/flat. | `L11-08` mở bằng công thức, `L11-10` mới có $g=(3,4)$. | Đổi `L11-08` thành vấn đề sharp/flat và vẽ lại SVG; `L11-09` tính nhiễu; `L11-10` mới nêu max–min, dấu $\xi$ và ba bước; giữ cầu nối có điều kiện và phạm vi bằng chứng ở `L11-11/12`. |
| SB11-04 | nghiêm trọng | `L11-17` | Target A3C có thể cộng reward và bootstrap qua terminal đến đủ $n$ bước. | Công thức cũ chỉ nhân một mặt nạ ở bước cuối. | Định nghĩa $n_t$ là số chuyển tiếp thực đến terminal hoặc cutoff và $b_t$ chỉ bật ở cutoff chưa terminal; ghi rõ không bootstrap qua reset. |
| SB11-05 | nghiêm trọng | `L11-20`–`L11-24` | DPG bắt đầu bằng mô tả/định lý, thiếu ví dụ trước hình thức. | Không có phép chain-rule số trước `L11-21`. | `L11-20` nêu bài toán hành động liên tục và ví dụ scalar $2\times3=6$; sau đó mới đến định lý, behavior/target, gradient và thuật toán DDPG. |
| SB11-06 | nghiêm trọng | `L11-32`–`L11-37` | SAC/TD3 trộn hình thức trước trực giác; ví dụ twin target nằm cuối. | Bản cũ bắt đầu bằng soft objective và đặt số $4{,}6$ ở `L11-37`. | Sắp vấn đề critic lạc quan → trực giác hai hướng → số twin target → SAC formal → ba cơ chế TD3 → so sánh stochastic entropy với deterministic external noise/update. |
| SB11-07 | nghiêm trọng | `X03`, `L11-42` | Bài tập chỉ nhận dạng và đứng trước bản đồ chọn phương pháp. | Người học chưa dùng thuật toán cho bối cảnh quyết định. | Chuyển `X03` sau `L11-42`; yêu cầu chọn họ cho continuous replay, CTDE, policy lag và population diversity, kèm tradeoff; giữ hai mục nhận dạng PPG/ACER. |
| SB11-08 | trung bình | `L11-14` | Identity importance sampling xuất hiện trước ví dụ. | Công thức tổng quát đi trước số $1{,}6$. | Đưa phép tính hai vế $1{,}6$ lên trước, rồi mới nêu identity và support trên cùng trang. |
| SB11-09 | trung bình | `L11-01`–`L11-40` | Nhiều viết tắt xuất hiện sớm. | `L11-02` từng liệt kê tên viết tắt trước nội dung. | Bỏ viết tắt khỏi `L11-02`; mở rộng GAE/TRPO/PPO trong ghi chú mở bài và mở rộng SPO, SAM, A3C, A2C, DPG, DDPG, D4PG, MADDPG/CTDE, SAC, TD3 ở lần giới thiệu. Các tên khảo sát giữ nguồn truy nguyên ở trang định nghĩa. |
| SB11-10 | trung bình | `L11-42` | Nhãn “on-policy hoặc gần on-policy” mơ hồ; ACKTR và SVPG thiếu khỏi bản đồ. | Không rõ tiêu chuẩn “gần”; SVPG không có vị trí. | Đổi trục hàng thành rollout, replay, actor phân tán có lag và quần thể; thêm ACKTR và SVPG. |
| SB11-11 | trung bình | HTML, outline, storyboard, notes | Thứ tự và nguồn truy nguyên có thể lệch sau đổi vai trò trang. | Nhiều ID giữ nguyên nhưng chức năng đã đổi. | Đồng bộ vai trò từng ID, ánh xạ nguồn, truyền dữ kiện và chuyển ý lân cận; giữ nguyên ID để bảo toàn trace. |
| SB11-12 | trung bình | toàn bài | Cần kiểm lại cấu trúc sau khi dời X03 và vẽ lại SVG. | Thay đổi thứ tự vật lý, công thức và tài sản. | Chạy lại tập ID, notes, storyboard, KaTeX nghiêm ngặt, XML/metadata SVG và đường dẫn tài sản; kết quả ghi dưới đây. |

Kiểm định sau sửa: 46 ID duy nhất gồm 43 trang chính và 3 bài tập; 46/46 trang có ghi chú; tập ID HTML khớp storyboard và thứ tự kết thúc là `L11-42` → `X03` → `L11-43`. Có 113 công thức KaTeX dựng thành công với `throwOnError`. Có đúng 11 tham chiếu SVG duy nhất; 11/11 tệp tồn tại, phân tích XML thành công và có `role="img"`, `title`, `desc`. Không có thời lượng hoặc nhãn linh hoạt trên mặt trang/ghi chú. `index.html` và `lecture-style.css` không đổi. Rà Quill xác nhận các chu trình ví dụ-trước-hình-thức và chuyển ý lân cận; rà no-ai-slop loại tiêu đề tiến trình, tuyên bố phổ quát và lời dẫn rỗng.

## Hợp nhất bốn phản biện độc lập — vòng sau

| báo cáo | mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|---|
| sinh viên | nghiêm trọng | `L11-02` | Mọi thuật toán bị đặt cùng mức thành thạo. | Mục tiêu cũ yêu cầu viết target/gradient cho cả survey. | Tách core và orientation. | Core: A3C/A2C, DDPG/MADDPG, SAC/TD3; D4PG, ACER, ACKTR, SVPG, IMPALA, PPG chỉ nhận dạng cơ chế/giới hạn. |
| sinh viên | nghiêm trọng | `L11-03`, `L11-16`–`L11-15` | Thiếu recap trực tiếp và tuyến actor–critic bị off-policy ngắt trước khi vào A3C. | `L11-03` chỉ có khung trừu tượng; thứ tự cũ `L13`–`L15` trước core. | Hiện $w$, dấu $A$, frozen batch; đưa core trước replay. | `L11-03` đã có ba dữ kiện PPO; thứ tự vật lý sau X01 là `L16`–`L19` → `L13`–`L15` → DPG. |
| sinh viên | trung bình | `L11-38`–`L11-40` | Survey quá tải với công thức nhưng mục tiêu chỉ nhận dạng. | Ba trang nằm trong 8+6 phút. | Giữ một cơ chế trên mặt, chuyển định nghĩa phụ vào notes. | SVPG chỉ giữ gradient+lực đẩy; V-trace giữ hợp đồng tính tối thiểu; PPG giữ joint loss và frozen quantities. |
| sinh viên | trung bình | toàn bài | Bảng thực tế nhỏ hơn 0,75em. | `.87×.86=.7482`. | Tăng table multiplier. | Đặt table cục bộ `.87em`, effective khoảng `.7569em`; giảm câu trong bảng dày. |
| chuyên gia RL | nghiêm trọng | `L11-04`–`L11-07` | SPO mở rộng sai thành “Smooth”. | Tên paper/thuật toán là Simple Policy Optimization. | Đổi tên thuần Việt và tiếng Anh. | Dùng “Tối ưu chính sách đơn giản (Simple Policy Optimization, SPO)” trong HTML/planning. |
| chuyên gia RL | nghiêm trọng | `L11-11`, `X01` | Độ phẳng tham số bị suy thành robustness cho mọi action perturbation. | Chặn Jacobian chỉ cho chiều thuận; chiều phủ ngược cần rank/singular value. | Thu hẹp claim và ghép điều kiện. | Chỉ nêu forward sensitivity; notes ghi Gaussian covariance cố định + first-order mapping; X01 yêu cầu đồng thời Jacobian, full rank và singular-value bound. |
| chuyên gia RL | nghiêm trọng | `L11-25`, `L11-29`, `L11-30` | Các thuật toán orientation được trình bày như contract triển khai đầy đủ. | D4PG thiếu projection; ACER thiếu Retrace/trust-region; ACKTR chỉ có K-FAC core. | Sửa công thức tối thiểu và hạ scope. | D4PG có $Y_t$ n bước và $\Pi$; ACER định nghĩa support/threshold/correction và nói phần không hiển thị; ACKTR ghi rõ damping/trust scaling ngoài công thức. |
| chuyên gia RL | nghiêm trọng | `L11-32`–`L11-37` | Động cơ SAC và TD3 bị trộn. | Entropy đổi objective, không phải target correction; TD3 xử lý function approximation/overestimation. | Tách hai bài toán, chỉ coi twin-min là phần giao. | Đã sửa `L32/33`, dùng SAC no-V-network và TD3 exact mechanisms; `L37` so sánh explicit stochastic/entropy với deterministic/noise/cadence. |
| chuyên gia RL | trung bình | `L11-38`, `L11-40` | SVPG thiếu prior; PPG thiếu định nghĩa auxiliary head/frozen target. | Công thức SVPG bỏ prior gradient; joint loss PPG chưa khóa pre-aux policy. | Nêu giả thiết và frozen quantities. | SVPG giả sử prior đều, notes định nghĩa particle/kernel/$\alpha$; PPG dùng $L_{joint}$, auxiliary value head, pre-aux $\pi_{old}$ và target frozen. |
| toán/thuật toán | chặn bàn giao | `L11-21`, `L11-23`, `L11-26`, `dpg-chain-rule.svg` | Quy ước Jacobian và phép kỳ vọng DPG/DDPG/MADDPG không nhất quán. | $D_\theta\mu\in\mathbb R^{d_a\times d_\theta}$ phải được chuyển vị; replay không phải on-policy theorem. | Đồng bộ $D^\top\nabla_aQ$ và ghi surrogate. | HTML/SVG dùng $D_\theta\mu^\top\nabla_aQ$; occupancy DPG thống nhất $d_{\rho_0,\gamma}^\mu$; DDPG/MADDPG dùng $S\sim\mathcal D$ và được gắn nhãn surrogate thực hành. |
| toán/thuật toán | chặn bàn giao | `L11-17` | $\phi^-$ dễ bị hiểu là target network của A3C. | A3C dùng tham số local của worker, không có target network DQN-style. | Dùng $\phi_{loc}$ và detach bootstrap. | Đã đổi ký hiệu, định nghĩa snapshot và dừng gradient; target dừng đúng $n_t$. |
| toán/thuật toán | nghiêm trọng | `L11-39` | V-trace thiếu behavior/learner, clipping roles, support và terminal discount. | Không thể kiểm công thức hoặc cài đúng chỉ từ bản cũ. | Định nghĩa $\mu,\pi,u,\rho,c,\bar\rho\ge\bar c,\gamma_t$. | Mặt trang có đủ hợp đồng; notes phân biệt $\rho$ cho residual, $c$ cho trace và support. |
| toán/thuật toán | nghiêm trọng | `L11-35`, `L11-36` | SAC/TD3 thiếu variant/source và chi tiết update. | SAC có nhiều phiên bản; TD3 actor dùng $Q_1$, noise/action clip và delayed targets. | Chốt variant và exact recipe. | SAC dùng modern no-V-network, $\alpha$ cố định; TD3 có $\xi$ clip, action clip, $Q_1$, critic mỗi bước, actor/target mỗi $d$, behavior noise riêng. |
| sư phạm RL | nghiêm trọng | `X02`, `X03` | Bài tập thiếu support/terminal và tính target TD3; X03 có bốn scenario. | Đáp án cũ chủ yếu nhận dạng tên. | Thêm phép tính và giới hạn ba scenario. | X02 kiểm support, shape, terminal/cutoff DDPG; X03 tính $4{,}6$ rồi chọn đúng ba scenario, chia answer fragments. |
| sư phạm RL | trung bình | `L11-42`, `L11-43` | Bản đồ tạo cảm giác category loại trừ và thiếu đường về nguồn sơ cấp. | D4PG, SVPG có nhiều thuộc tính; notes cuối chỉ ghi “tổng hợp”. | Dùng multi-attribute map và source appendix trong notes. | `L11-42` dùng bốn thuộc tính; `L11-43` liệt kê nguồn sơ cấp theo cụm mà không tăng thời lượng chính. |

Các quyết định trên thay thế mọi mô tả cũ mâu thuẫn trong nhật ký. Không có đề xuất nghiêm trọng hoặc chặn bàn giao nào bị từ chối.

Kiểm định cuối sau hợp nhất bốn phản biện: 46 ID duy nhất gồm 43 trang chính và 3 bài tập; 46/46 trang có notes; tập ID HTML khớp storyboard. Tuyến vật lý đã kiểm là `X01` → `L11-16`–`L11-19` → `L11-13`–`L11-15` → `L11-20`; phần cuối là `L11-42` → `X03` → `L11-43`. KaTeX cục bộ dựng nghiêm ngặt 139 công thức với `throwOnError`. Có đúng 11 SVG được tham chiếu; 11/11 tồn tại, hợp lệ XML và có `role="img"`, `title`, `desc`. Cỡ bảng cục bộ là `.87em`, cho effective `.7569em` dưới cỡ slide `.87em`. Không còn “Smooth Policy”, $\phi^-$ trong nội dung hiện hành, lỗi lặp ở `L11-15`, hoặc metadata thời lượng trên slide/notes. `index.html` và `lecture-style.css` không đổi. Rà Quill xác nhận chuỗi recap → SPO/SAM → actor–critic core → off-policy → DPG → orientation → SAC/TD3 → survey; rà no-ai-slop giữ câu trực tiếp, bỏ tuyên bố vượt nguồn và không thêm khẩu hiệu.

## Tái kiểm định và kiểm định cuối của điều phối viên

- Tác tử toán học–thuật toán đã tái kiểm định bản sửa cuối và kết luận `PASS`: không còn vấn đề từ mức `trung bình` trở lên.
- Tác tử storyboard đã rà toàn bộ trang bị đổi và hai trang lân cận; kết luận `PASS`.
- HTML có 46 mã duy nhất, 46 ghi chú và độ sâu `section` tối đa là hai; storyboard chứa đủ 46 mã theo đúng thứ tự.
- KaTeX cục bộ dựng nghiêm ngặt 139 biểu thức, không có lỗi. Mười một SVG hợp lệ theo XML, có `role="img"`, `title`, `desc` và đều được HTML sử dụng.
- Tệp HTML và 11 SVG đều trả HTTP 200 tại cổng 8765. Không có ảnh raster, liên kết planning trong HTML, phụ thuộc mạng cốt lõi hoặc lỗi từ `git diff --check`.
- Bản HTML và bốn tệp quy trình đã được đưa vào Design Files của dự án Codex Slides và đối chiếu từng byte với tệp trong kho.
- Codex Slides Browser không khả dụng trong phiên này. Vì vậy chưa thể tuyên bố đã rà trực quan bằng Codex Slides; giới hạn còn lại là kiểm tra tràn, chồng lấn và khả năng đọc bằng trình duyệt đồ họa ở khung 16:9 và màn hình hẹp.

## Năm phản biện độc lập — vòng hiện tại

Năm báo cáo hợp lệ đều chạy qua `openrouter-mcp-reviewer --json --progress jsonl` với `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Lượt sinh viên đầu hết thời gian, lượt toán đầu bị cắt đầu ra và lượt kết nối đầu hết giới hạn công cụ; ba lượt đó không được dùng làm bằng chứng. Các lượt chạy lại là tiến trình độc lập.

| vai | mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|---|
| góc nhìn sinh viên | trung bình | `L11-02`, `X01` | Mục tiêu gọi SPO/SAM là định hướng trong khi bài tập yêu cầu tính. | `X01` tính cả objective SPO và nhiễu SAM. | Đưa SPO/SAM vào tầng core; giữ các thuật toán khảo sát ở tầng nhận dạng. Đã áp dụng. |
| góc nhìn sinh viên | trung bình | `L11-39`, `L11-42` | Công thức V-trace và bảng tổng hợp dày. | Trang `L11-39` từng hiển thị cả tổng trace; `L11-42` có tám hàng. | Chuyển tổng trace đầy đủ sang ghi chú; giữ bảng ở `.87em` và kiểm bằng render. Đã áp dụng phần nội dung, chờ render. |
| chuyên gia Học tăng cường | trung bình | `L11-16`, `L11-19` | Toán tử dừng gradient và mô tả staleness chưa đủ trực tiếp. | `sg` chưa được định nghĩa; A2C chỉ loại staleness giữa worker. | Định nghĩa $\operatorname{sg}$ và target critic; thu hẹp phát biểu A2C. Đã áp dụng. |
| chuyên gia Học tăng cường | trung bình | `L11-42` | Bản đồ bỏ A3C/A2C và gán dữ liệu/actor cho SAM, ACKTR như thuộc tính cố định. | Hai thuật toán actor–critic core không có hàng; SAM/ACKTR là cơ chế tối ưu. | Thêm A3C/A2C; ghi “không do cơ chế xác định” cho SAM/ACKTR. Đã áp dụng. |
| toán học và thuật toán | nhẹ | `L11-35`–`L11-36` | Dấu phẩy trên trạng thái/hành động kế tiếp chưa nhất quán. | Một số công thức dùng ký hiệu kế tiếp không có dấu phẩy. | Đồng bộ $S'$ và $A'$ trong công thức SAC/TD3. Đã áp dụng. |
| toán học và thuật toán | nhẹ | `L11-38`–`L11-39` | Cần khóa quy ước $1/n$ và vai trò riêng của $\rho_t,c_t$. | Scale SVPG và hai tỷ số cắt có thể bị đọc như cùng chức năng. | Nêu $1/n$ là quy ước trung bình; $\rho_t$ sửa residual, $c_t$ truyền trace. Đã áp dụng. |
| phản biện học thuật và giảng dạy | trung bình | `X02`, `L11-41` | Tên bước kiểm và cầu nối sang bản đồ chưa khớp nội dung hiện hành. | `X02` kiểm terminal/cutoff, không kiểm noise; `L11-41` chưa dẫn sang trục tổng hợp. | Sửa storyboard và thêm câu nối trong ghi chú. Đã áp dụng. |
| kết nối và mạch viết | trung bình | `L11-41`–`L11-43` | Vai trò trong mạch: so sánh ba khảo sát; kết nối vào từ survey rõ nhưng kết nối ra sang bản đồ và checklist còn mờ. | Bản cũ chuyển trực tiếp từ bảng ba phương pháp sang bảng toàn bài rồi bài tập. | Dẫn `L11-41` sang bản đồ, `L11-42` sang `X03`, và `X03` sang checklist. Đã áp dụng. |
| kết nối và mạch viết | nhẹ | `L11-43` | Vai trò trong mạch: thu hồi bài; kết nối vào từ `X03` có, kết nối ra nguồn sơ cấp chưa rõ. | Ghi chú cuối chỉ liệt kê nguồn mà chưa gắn với năm phép kiểm. | Nêu `X03` đã dùng bốn phép kiểm và phép thứ năm giới hạn kết luận theo nguồn. Đã áp dụng. |

Không có lỗi `chặn bàn giao` hoặc `nghiêm trọng` trong năm báo cáo hợp lệ. Đề xuất cũ thêm tình huống đa dạng quần thể và hai mục nhận dạng PPG/ACER vào `X03` không áp dụng: rubric hiện hành gồm bốn câu trong 10 phút và đã kiểm đủ target, tradeoff, CTDE, policy lag. Quyết định này thay thế mô tả SB11-07 cũ.

## Danh mục mã trang vòng hiện tại

`L11-01`, `L11-02`, `L11-03`, `L11-04`, `L11-05`, `L11-06`, `L11-07`, `L11-08`, `L11-09`, `L11-10`, `L11-11`, `L11-12`, `X01`, `L11-16`, `L11-17`, `L11-18`, `L11-19`, `L11-13`, `L11-14`, `L11-15`, `L11-20`, `L11-21`, `L11-22`, `L11-23`, `L11-24`, `L11-25`, `L11-26`, `L11-27`, `L11-28`, `X02`, `L11-29`, `L11-30`, `L11-31`, `L11-32`, `L11-33`, `L11-34`, `L11-35`, `L11-36`, `L11-37`, `L11-38`, `L11-39`, `L11-40`, `L11-41`, `L11-42`, `X03`, `L11-43`.

Các cảnh báo “nguồn có 1.404 dòng”, “HTML có 70 dòng so với nguồn” và “không có mạch ngoài” bị bác bỏ vì lần lượt dùng số dòng chuẩn hóa của cầu nối, so nhầm HTML với văn bản nguồn và không phân tích cấu trúc `section` lồng nhau. Chuẩn điều phối viên là 1.326 dòng theo `wc -l`, 46 trang đích và 5 mạch ngoài.

## Kiểm định cuối vòng 30-08-2026

Mục này thay thế các số kiểm định cũ ở phía trên.

- Tái kiểm toán học dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Các trang trong phạm vi đều đạt. Cảnh báo đặt $\beta_{\mathrm{clone}}$ nhầm hạng ở `L11-40` bị bác bỏ sau khi đối chiếu phương trình gốc của Cobbe et al. (2021): $L_{\mathrm{joint}}=L_{\mathrm{aux}}+\beta_{\mathrm{clone}}\,\mathbb E[D_{\mathrm{KL}}(\pi_{\mathrm{old}}\|\pi_\theta)]$. Công thức hiện hành đúng nguồn.
- Tái kiểm kết nối dùng cùng runtime trên và kết luận `PASS`: đủ 5 mạch ngoài; tuyến 110 phút cốt lõi + 10 phút linh hoạt; 30 phút cho `X01/X02/X03`. Sau hai sửa nhẹ, lượt rà hẹp xác nhận `L11-36` → `L11-37` → `L11-38` và `L11-42` → `X03` → `L11-43` liền mạch.
- HTML có 46 mã duy nhất, 46 ghi chú, 5 `section` ngoài và độ sâu tối đa hai. Tập mã khớp outline, storyboard và nhật ký. Có 11 tham chiếu SVG duy nhất; tất cả tồn tại, hợp lệ XML và có `role="img"`, `title`, `desc`. Không có ảnh raster hoặc tài nguyên cốt lõi từ mạng.
- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Kiểm thử dùng phương án cục bộ `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm không chứa `.env`.
- HTML và 11 SVG đều trả HTTP 200. RevealJS dựng 46 trang và 46 ghi chú; 149 biểu thức KaTeX, 0 lỗi KaTeX, 0 lỗi console. Điều hướng bàn phím lên, xuống và sang phải đúng.
- Đã chụp và duyệt 92 ảnh, gồm toàn bộ 46 trang ở 1280 × 720 và 800 × 600. Cảnh báo biên tự động trên một số hộp KaTeX là dương tính giả do hộp span sau scale; ảnh không có nội dung bị cắt. Ba trang câu hỏi được kiểm thêm khi hiện toàn bộ 2, 2 và 4 fragment; không có fragment tràn hoặc bị cắt.
- Rà `no-ai-slop` không thấy tiêu đề câu hỏi tu từ, khẩu hiệu, lời ca tụng hoặc tuyên bố phổ quát mới. Rà mạch theo `quill` xác nhận chuỗi PPO → SPO/SAM → actor–critic → khác chính sách → DPG/DDPG → SAC/TD3 → khảo sát → bản đồ/checklist; không tạo `quill.json`.
- Năm Design Files của dự án Codex Slides `20260825000420-lecture-11-c-c-ph-ng-ph-p-gradient-ch-nh-w00c` đã được đồng bộ và đối chiếu chính xác với HTML, outline, storyboard, ghi chú tác giả và nhật ký trong kho. Dự án vẫn ở trạng thái draft với 0 slide native; liên kết Design Files đã tạo, nhưng Codex in-editor Browser không khả dụng trong phiên nên không tuyên bố đã rà trực quan trong giao diện Codex Slides.
- `2627-1/index.html` đã có đúng một liên kết tới Bài 11 và không liên kết tệp quy trình. `git diff --check` đạt.
