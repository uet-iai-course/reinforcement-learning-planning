# Lưu ý cho người soạn và người dạy Bài 10

## Phân bổ thời gian

- Giữ 110 phút cho tuyến cốt lõi và 10 phút cho phần mở rộng.
- Nếu thiếu thời gian, rút 5 phút diễn giải sâu GAE ở `L10-10` và 5 phút khai triển shape ở `L10-28`. Không bỏ hai mặt nạ ở `L10-11`, công thức từng dấu ở `L10-24`, bảng trong/ngoài dải ở `L10-25`, hoặc schema batch ở `L10-30`.
- Ba bài tập dùng 10, 8 và 12 phút. `X03` là kiểm toán batch PPO sau `L10-35`, không lặp bảng bốn số clipping.
- Mốc 50 phút: dừng tiết 1 sau `L10-16`, tiết 2 sau `L10-32`; tiết 3 dành khoảng 20 phút cho phần còn lại và 30 phút cho `X01`–`X03`.
- Tuyến cắt thêm khi trễ: nén phần trình bày `L10-33`–`L10-34` và bảng `L10-36`. Không bỏ `L10-27`–`L10-31` hoặc hai trang lý thuyết `L10-37`, `L10-37B`.

## Điểm phải nhấn khi giảng

- Nói rõ $R_{t+1}$ là reward sau $A_t$; không quay lại ký hiệu $r_t$ của nguồn.
- Với $J=\mathbb E[G_0]$, estimator REINFORCE trong bài có $\gamma^tG_t$.
- Ở `L10-05`–`L10-06`, đọc score là đạo hàm của $\log\pi_\theta$ theo $\theta$, rồi đánh giá tại $\theta_{\mathrm{old}}$; không nói “đạo hàm log pi theta old”.
- Baseline phải độc lập hành động khi điều kiện theo trạng thái; actor dùng `stop-gradient` trên baseline hoặc lợi thế.
- Critic học bằng đích Monte Carlo vẫn có thể thuộc actor–critic. Trong bài, “nhánh bootstrap” chỉ quy ước cho TD/GAE, không phải ranh giới định nghĩa phổ quát.
- Chỉ bootstrap tại truncation nhân tạo hoặc ngoại sinh khi có quan sát cuối hợp lệ. Nếu chân trời là một phần của MDP, hết chân trời là terminal. Phân biệt $m_t$ với $c_t$ bằng ví dụ số.
- Ở biên rollout, lấy `final_observation` trước reset hoặc lưu trực tiếp $V_{\mathrm{boot}}=V_{\mathrm{old}}(S_H)$. Không dùng quan sát reset của episode kế tiếp để bootstrap.
- Performance-difference lemma dùng phân bố chiếm dụng chiết khấu đã chuẩn hóa của chính sách mới; surrogate thay bằng dữ liệu cũ. Nêu đây là chuỗi đẳng thức rồi xấp xỉ, không phải một bảo đảm duy nhất.
- $J=\mathbb E[G_0]$ và REINFORCE $\gamma^tG_t$ dùng hợp đồng chiết khấu. TRPO lý thuyết dùng $\mathbb E_{\mathrm{disc},\pi}$; PPO thực hành dùng trung bình đều $\mathbb E_B$ trên rollout. Không gọi hai phép kỳ vọng này là cùng một objective chính xác.
- TRPO thực hành dùng empirical average-KL, FVP, conjugate gradient và line search. Không gọi nó là bảo đảm đơn điệu vô điều kiện.
- Khi giải PPO-Clip, luôn tách $\widehat A^{\mathrm{actor}}>0$ và $\widehat A^{\mathrm{actor}}<0$. Hai phía bất lợi không bị clipping cứu.
- Dùng $w_t$ cho tỷ số chính sách trong toàn bài; $\rho_0$ chỉ ký hiệu phân bố trạng thái đầu.
- Chỉ trước minibatch đầu tiên của một lần cập nhật mới có $\theta=\theta_{\mathrm{old}}$ và $w_t=1$. Trong các minibatch và epoch sau, giữ log-probability cũ nhưng tính lại log-probability mới và $w_t$ theo $\theta$ hiện tại.
- Dùng $T$ cho thời điểm episode kết thúc, $H$ cho độ dài rollout, $N$ cho số môi trường và $B=HN$. Không dùng $T$ làm chiều rollout của buffer PPO.
- Với hành động nhiều chiều, cộng log-probability theo chiều hành động trước khi tạo tỷ số.
- Không tính lại log-probability cũ, lợi thế hoặc target trong các epoch của cùng batch.
- Phân biệt $\widehat A^{\mathrm{raw}}$, $\widehat A^{\mathrm{actor}}$ đã chuẩn hóa và $\widehat V=\operatorname{sg}(V_{\mathrm{old}}+\widehat A^{\mathrm{raw}})$. Critic không dùng lợi thế actor đã chuẩn hóa làm target.
- Value clipping là biến thể. Ghi rõ nếu cài đặt dùng nó.
- `L10-37` trình bày mô hình outer–inner và Clip–Penalty; `L10-37B` nêu kết quả điểm dừng có điều kiện. Không suy ra PPO thực hành với Adam và GAE luôn hội tụ.
- Nguồn chính xác cho `L10-37B`: Ruinan Jin, Shuai Li, Baoxiang Wang, “On Stationary Point Convergence of PPO-Clip”, ICLR 2024, Định lý 3.1 và Giả thiết 3.1, 3.2, 3.4. Chỉ phát biểu chặn liminf chuẩn gradient bởi $\phi_n$; không đổi thành hội tụ toàn dãy hoặc tối ưu toàn cục.
- Khi giảng `L10-31`, gọi clipfrac là tỷ lệ tỷ số ngoài dải clip. Đừng gọi là tỷ lệ đoạn phẳng vì đoạn phẳng còn phụ thuộc dấu lợi thế.

## Nội dung không mở rộng trên lớp

- Danh sách A3C/A2C, DPG, DDPG, D4PG, MADDPG, ACER, ACKTR, SAC, TD3, SVPG, IMPALA và PPG ở nguồn chỉ phục vụ định vị họ thuật toán.
- SPO và SAM+PPO chỉ nên dùng làm gợi ý đọc thêm khi người học hỏi. Không thêm công thức hoặc kết quả thực nghiệm nếu chưa bổ sung nguồn gốc và kiểm tra giả thiết.
- Không chuẩn bị notebook hay chương trình PPO vì bản nguồn không có code demo.

## Kiểm tra trước buổi học

- Tự tính lại bốn số PPO: $2{,}4$, $-1{,}6$, $1{,}4$, $-2{,}6$; chỉ hai số đầu hiển thị ở `L10-23`, hai số sau nằm trong ghi chú `L10-25`.
- Tự tính lại GAE: $0{,}98$ cho terminal và $3{,}572$ cho truncation.
- Tự tính lại bước TRPO: $(0{,}05,0{,}1)$ và dạng toàn phương bằng $0{,}01$.
- Kiểm tra thư viện môi trường có phân biệt `terminated` và `truncated`; không gộp hai cờ trước khi tính bootstrap.
